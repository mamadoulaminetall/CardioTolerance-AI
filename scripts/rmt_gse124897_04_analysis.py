"""Volet A, étape 4b — analyse PRÉENREGISTRÉE de GSE124897 (https://osf.io/6htjn).

Applique le plan enregistré (docs/rmt_preregistration.md, étiquette prereg-v1) :
  - gènes : D3 (sans contrôles AFFX ni sondes multi-gènes ; une sonde par gène, la plus
    exprimée dans la cohorte 331 ; même liste appliquée à la 558) ;
  - référence (D5) : sous-espace principal de la cohorte 558, taille K_ref par analyse
    parallèle (199 permutations, α = 0,05) ; vérification : K_ref par RMT ;
  - 200 sous-échantillons de la cohorte 331 pour n = 20, 40, 80, 160 (graine 20261126),
    méthodes appliquées aux mêmes tirages (plan apparié) + cohorte 331 entière ;
  - critère principal D = 2‖U_refᵀ V‖²_F / (K_ref + k) (D = 0 si k = 0) ;
  - S1 nombre d'axes ; S2 stabilité (100 paires de tirages : 1-2, 3-4, …) ; S3 faux positifs
    sur données permutées ; S4 part de la variance inter-groupes 4AA de la 558 captée ;
    S5 (H3) recouvrement observé vs prédit ψ²(331) × ψ²(558) ;
  - vérifications : valeurs GEO des auteurs, exclusion des 26 puces signalées, 5 000 gènes
    les plus variables (choisis dans chaque tirage), K_ref par RMT, α = 0,01.

Règle : avant toute lecture de la cohorte 558, l'empreinte du sceau est vérifiée ; si elle
ne correspond pas, le script s'arrête.

Écarts nécessaires, déclarés dans les sorties (à reprendre dans l'article) :
  - α = 0,01 n'est appliqué qu'à RMT : avec 99 permutations, la plus petite p-valeur
    possible est 0,01, donc « p < 0,01 » est impossible pour l'analyse parallèle.

Usage :
  python -I scripts/rmt_gse124897_04_analysis.py --selftest      # données synthétiques
  python -I scripts/rmt_gse124897_04_analysis.py                 # analyse réelle complète
"""

from __future__ import annotations

import argparse
import io
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rmt_denoise as rmt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
GEO = ROOT / "data" / "geo" / "GSE124897"
RES = ROOT / "results" / "rmt_gse124897"
OSF_URL = "https://osf.io/6htjn"

SEED = 20261126
NS = (20, 40, 80, 160)
R = 200
N_PAIRS = 100
B_SUB, B_REF = 99, 199
KCAP = 50
METHODS = ("rmt", "rmt_a01", "pca10", "kaiser", "var80", "mp", "perm")


# ---------------------------------------------------------------------------
# Données
# ---------------------------------------------------------------------------
def verify_seal() -> dict:
    from rmt_gse124897_02_split_qc import canonical_sha256
    rec = json.loads((RES / "SCELLE_cohorte558.json").read_text())
    arr = np.load(GEO / "sealed" / "cohort558_expression.npy")
    s = (GEO / "sealed" / "cohort558_samples.txt").read_text().split("\n")
    p = (GEO / "sealed" / "cohort558_probes.txt").read_text().split("\n")
    digest = canonical_sha256(arr, s, p, "GSE124897 cohorte 558 (sondes x echantillons)")
    if digest != rec["sha256_contenu"]:
        raise SystemExit("SCEAU ROMPU : l'empreinte de la cohorte 558 ne correspond pas. Arrêt.")
    return {"sha256_verifie": digest, "scelle_le": rec["scelle_le"]}


def load_rma(cohort: int) -> pd.DataFrame:
    base = GEO / "rma" / f"cohort{cohort}_rma"
    probes = [l for l in (base.parent / f"{base.name}_probes.txt").read_text().split("\n") if l]
    samples = [l for l in (base.parent / f"{base.name}_samples.txt").read_text().split("\n") if l]
    x = np.fromfile(base.parent / f"{base.name}.f64", dtype="<f8")
    return pd.DataFrame(x.reshape(len(samples), len(probes)).T, index=probes, columns=samples)


def load_geo(cohort: int) -> pd.DataFrame:
    d = GEO / ("derived" if cohort == 331 else "sealed")
    x = np.load(d / f"cohort{cohort}_expression.npy")
    probes = [l for l in (d / f"cohort{cohort}_probes.txt").read_text().split("\n") if l]
    samples = [l for l in (d / f"cohort{cohort}_samples.txt").read_text().split("\n") if l]
    return pd.DataFrame(x, index=probes, columns=samples)


def gene_symbols() -> pd.Series:
    lines = (GEO / "raw" / "GPL15207_table.txt").read_text(encoding="utf-8", errors="replace").split("\n")
    b = next(i for i, l in enumerate(lines) if l.startswith("!platform_table_begin"))
    e = next(i for i, l in enumerate(lines) if l.startswith("!platform_table_end"))
    df = pd.read_csv(io.StringIO("\n".join(lines[b + 1:e])), sep="\t", dtype=str,
                     usecols=["ID", "Gene Symbol"])
    sym = df["Gene Symbol"].fillna("").str.strip()
    ok = ~df["ID"].str.startswith("AFFX") & (sym != "") & ~sym.str.contains("///", regex=False)
    return pd.Series(sym[ok].values, index=df["ID"][ok].values)


def collapse(X331: pd.DataFrame, X558: pd.DataFrame, sym: pd.Series):
    """D3 : une sonde par gène, la plus exprimée en moyenne dans la cohorte 331."""
    common = X331.index.intersection(X558.index).intersection(sym.index)
    df = pd.DataFrame({"probe": common, "gene": sym.loc[common].values,
                       "moyenne_331": X331.loc[common].mean(axis=1).values})
    best = (df.sort_values(["gene", "moyenne_331", "probe"], ascending=[True, False, True], kind="mergesort")
              .drop_duplicates("gene").reset_index(drop=True))
    A = X331.loc[best.probe].to_numpy().T          # échantillons × gènes
    B = X558.loc[best.probe].to_numpy().T
    return A, B, best


# ---------------------------------------------------------------------------
# Méthodes et mesures
# ---------------------------------------------------------------------------
def lead(flags) -> int:
    flags = np.asarray(flags, dtype=bool)
    return int(len(flags) if flags.all() else np.argmin(flags))


def method_ks(Z, eig, rng, with_perm=True) -> dict:
    n, p = Z.shape
    N, m = n - 1, len(eig)
    ks = {
        "rmt": rmt.select_components(eig, N, p, alpha=0.05, n_report=0)["k"],
        "rmt_a01": rmt.select_components(eig, N, p, alpha=0.01, n_report=0)["k"],
        "pca10": min(10, m),
        "kaiser": int((eig > 1.0).sum()),
        "var80": int(min(m, np.searchsorted(np.cumsum(eig) / p, 0.80) + 1)),
        "mp": int((eig > rmt.mp_edges(N, p, 1.0)[1]).sum()),
    }
    if with_perm:
        null = rmt.permutation_null(Z, B_SUB, rng)
        ks["perm"] = lead(rmt.permutation_pvalues(eig[:KCAP], null) < 0.05)
    return ks


def cum_overlap(U_rows, V):
    """Sommes cumulées de ‖U_refᵀ v_j‖² sur les axes j = 1…kmax."""
    if U_rows.shape[1] == 0 or V.shape[1] == 0:
        return np.zeros(V.shape[1])
    return np.cumsum(((U_rows.T @ V) ** 2).sum(axis=0))


def dice_from_cum(cum, K, k) -> float:
    return 0.0 if k == 0 or K == 0 else float(2 * cum[k - 1] / (K + k))


class Reference:
    """Cohorte 558 : référence (D5), centres de groupes 4AA (S4), fiabilités ψ² (S5)."""

    def __init__(self, B, groups, p_all, rng):
        Z, keep = rmt.standardize(B)
        n, p = Z.shape
        eig, U, s, V = rmt.spectrum(Z)
        null = rmt.permutation_null(Z, B_REF, rng)
        self.K_pa = lead(rmt.permutation_pvalues(eig[:KCAP], null) < 0.05)
        sel = rmt.select_components(eig, n - 1, p, n_report=0)
        self.K_rmt, self.sigma2 = sel["k"], sel["sigma2"]
        top = max(self.K_pa, self.K_rmt, KCAP)
        self.V = np.zeros((p_all, top))
        self.V[keep] = V[:, :top]
        self.eig = eig
        _, self.psi2 = rmt.spike_estimates(eig[:top], n - 1, p, self.sigma2)
        self.U_pa, self.U_rmt = self.V[:, :self.K_pa], self.V[:, :self.K_rmt]
        Zf = np.zeros((n, p_all))
        Zf[:, keep] = Z
        g = pd.Series(groups)
        rows = [np.sqrt((g == lab).sum()) * Zf[(g == lab).values].mean(axis=0) for lab in sorted(g.unique())]
        self.Mw = np.vstack(rows)
        self.between_total = float((self.Mw ** 2).sum())
        self.info = {"n": n, "p": p, "K_ref_analyse_parallele": self.K_pa, "K_ref_rmt": self.K_rmt,
                     "sigma2_rmt": self.sigma2, "valeurs_propres_10": eig[:10].round(3).tolist()}


def analyse_subsample(X, idx, ref, rng, top_genes=None, with_perm=True):
    """Un tirage : renvoie k et D de chaque méthode + vecteurs (espace complet) pour S2."""
    Xs = X[idx]
    cols = np.arange(X.shape[1])
    if top_genes:
        cols = np.argsort(-Xs.var(axis=0, ddof=1), kind="mergesort")[:top_genes]
        Xs = Xs[:, cols]
    Z, keep = rmt.standardize(Xs)
    eig, U, s, V = rmt.spectrum(Z)
    ks = method_ks(Z, eig, rng, with_perm)
    kmax = max(ks.values())
    rows_full = cols[keep]
    Vk = V[:, :kmax]
    cum_pa = cum_overlap(ref.U_pa[rows_full], Vk)
    cum_rmt = cum_overlap(ref.U_rmt[rows_full], Vk)
    cum_s4 = np.cumsum(((ref.Mw[:, rows_full] @ Vk) ** 2).sum(axis=0)) if kmax else np.zeros(0)
    out = {}
    for mth, k in ks.items():
        out[mth] = {"k": k, "D": dice_from_cum(cum_pa, ref.K_pa, k),
                    "D_refRMT": dice_from_cum(cum_rmt, ref.K_rmt, k),
                    "S4_capture": float(cum_s4[k - 1] / ref.between_total) if k else 0.0}
    return out, ks, (rows_full, Vk), (Z, eig)


def pair_dice(a, b, ka, kb) -> float:
    if ka == 0 or kb == 0:
        return 0.0
    (ra, Va), (rb, Vb) = a, b
    p = max(ra.max(), rb.max()) + 1
    A = np.zeros((p, ka)); A[ra] = Va[:, :ka]
    Bm = np.zeros((p, kb)); Bm[rb] = Vb[:, :kb]
    return float(2 * ((A.T @ Bm) ** 2).sum() / (ka + kb))


def draw_subsamples(pool_size):
    rng = np.random.default_rng(SEED)
    return {n: [np.sort(rng.choice(pool_size, n, replace=False)) for _ in range(R)] for n in NS}


def run_variant(name, A, ref, pool, top_genes=None, full=True, extras=False, log=print):
    """Une variante : tirages appariés (+ cohorte entière ; + S2/S3 si extras)."""
    rows, stab, perm_rows = [], [], []
    draws = draw_subsamples(len(pool))
    X = A[pool]
    for n in NS:
        t0 = time.time()
        prev = None
        for r, idx in enumerate(draws[n]):
            res, ks, vec, (Z, eig) = analyse_subsample(
                X, idx, ref, np.random.default_rng([SEED, n, r, 1]), top_genes)
            for mth, v in res.items():
                rows.append({"variante": name, "n": n, "tirage": r, "methode": mth, **v})
            if extras:
                if r % 2 == 0:
                    prev = (vec, ks)
                else:
                    for mth in ks:
                        stab.append({"n": n, "paire": r // 2, "methode": mth,
                                     "D_stabilite": pair_dice(prev[0], vec, prev[1][mth], ks[mth])})
                rngp = np.random.default_rng([SEED, n, r, 2])
                Zp = rngp.permuted(Z, axis=0)
                kp = method_ks(Zp, rmt.top_eigenvalues(Zp), rngp)
                for mth, k in kp.items():
                    perm_rows.append({"n": n, "tirage": r, "methode": mth, "k": k})
        log(f"  [{name}] n = {n:3d} : {R} tirages en {time.time() - t0:.0f} s")
    full_rows = []
    if full:
        res, ks, vec, _ = analyse_subsample(X, np.arange(len(pool)), ref,
                                            np.random.default_rng([SEED, 331, 0, 1]), top_genes)
        for mth, v in res.items():
            full_rows.append({"variante": name, "n": len(pool), "methode": mth, **v})
    return (pd.DataFrame(rows), pd.DataFrame(stab), pd.DataFrame(perm_rows), pd.DataFrame(full_rows))


def s5_table(A, ref):
    Z, keep = rmt.standardize(A)
    n, p = Z.shape
    eig, U, s, V = rmt.spectrum(Z)
    sel = rmt.select_components(eig, n - 1, p, n_report=0)
    k = sel["k"]
    _, psi331 = rmt.spike_estimates(eig[:k], n - 1, p, sel["sigma2"])
    rows = []
    for j in range(k):
        v = np.zeros(ref.V.shape[0]); v[keep] = V[:, j]
        ov = (ref.V.T @ v) ** 2
        i = int(np.argmax(ov))
        rows.append({"axe_331": j + 1, "valeur_propre_331": eig[j], "psi2_331": psi331[j],
                     "axe_558_apparie": i + 1, "psi2_558": ref.psi2[i],
                     "recouvrement_observe": ov[i], "recouvrement_predit": psi331[j] * ref.psi2[i]})
    return pd.DataFrame(rows), {"k_rmt_331": k, "sigma2_331": sel["sigma2"]}


# ---------------------------------------------------------------------------
# Verdicts (critères du préenregistrement, section 6)
# ---------------------------------------------------------------------------
def verdicts(main: pd.DataFrame, perm: pd.DataFrame, s5: pd.DataFrame) -> dict:
    v = {"H1": {}, "H2": {}}
    w = main.pivot_table(index=["n", "tirage"], columns="methode", values="D")
    for n in (20, 40, 80):
        d = w.loc[n]
        diff = d["rmt"] - d["pca10"]
        frac = float((d["rmt"] > d["pca10"]).mean())
        v["H1"][n] = {"mediane_difference": float(diff.median()), "part_RMT_superieur": frac,
                      "critere_rempli": bool(diff.median() > 0 and frac >= 0.80)}
    v["H1"]["soutenue"] = all(v["H1"][n]["critere_rempli"] for n in (20, 40, 80))
    pr = perm[perm.methode == "rmt"].groupby("n").k.apply(lambda k: float((k >= 1).mean()))
    for n, x in pr.items():
        v["H2"][int(n)] = {"part_tirages_faux_axe": x, "critere_rempli": bool(x <= 0.08)}
    v["H2"]["soutenue"] = all(v["H2"][int(n)]["critere_rempli"] for n in pr.index)
    v["H3"] = {"axes": int(len(s5)),
               "ecart_absolu_moyen": float((s5.recouvrement_observe - s5.recouvrement_predit).abs().mean())
               if len(s5) else None}
    return v


# ---------------------------------------------------------------------------
def selftest():
    """Données synthétiques étiquetées : vérifie que la chaîne tourne et se comporte bien."""
    out = Path(sys.argv[0]).resolve().parent.parent / "results" / "rmt_gse124897" / "selftest_SYNTHETIQUE"
    rng = np.random.default_rng(1)
    p, n331, n558 = 1500, 120, 200
    load = np.zeros((p, 2)); load[:150, 0] = 1; load[150:230, 1] = 1

    def make(n):
        f = rng.standard_normal((n, 2))
        return rng.standard_normal((n, p)) + 0.55 * f @ load.T

    A, B = make(n331), make(n558)
    groups = np.where(rng.random(n558) < 0.7, "1", "2")
    ref = Reference(B, groups, p, np.random.default_rng(5))
    global NS, R
    NS, R = (20, 40), 6
    main, stab, perm, full = run_variant("SYNTHETIQUE", A, ref, np.arange(n331), extras=True)
    s5, _ = s5_table(A, ref)
    out.mkdir(parents=True, exist_ok=True)
    main.to_csv(out / "SYNTHETIQUE_tirages.csv", index=False)
    print("SELFTEST (données synthétiques) — référence :", ref.info)
    print(main.groupby(["n", "methode"])[["k", "D"]].mean().round(3).to_string())
    print("stabilité :", stab.groupby("methode").D_stabilite.mean().round(3).to_dict())
    print("faux positifs RMT sur permutées :", perm[perm.methode == "rmt"].groupby("n").k.apply(lambda k: (k > 0).mean()).to_dict())
    print("S5 :", s5.round(3).to_dict("records"))
    assert ref.K_pa >= 1 and main[main.methode == "rmt"].D.mean() > main[main.methode == "pca10"].D.mean()
    print("SELFTEST OK")


def main():
    ap = argparse.ArgumentParser(description="Analyse préenregistrée de GSE124897 (osf.io/6htjn).")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--only", choices=["principale", "geo", "exclusion", "top5000"], nargs="*")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    out = RES / "analyse"
    out.mkdir(parents=True, exist_ok=True)
    logf = open(out / "journal_analyse.txt", "a", encoding="utf-8")

    def log(msg):
        print(msg, flush=True)
        logf.write(msg + "\n"); logf.flush()

    seal = verify_seal()
    opened = {"ouverte_le": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "preenregistrement": OSF_URL, "enregistre_le": "2026-11-26T12:32:54Z", **seal}
    (RES / "OUVERTURE_cohorte558.json").write_text(json.dumps(opened, indent=2) + "\n")
    log(f"sceau de la 558 vérifié ({seal['sha256_verifie'][:16]}…), ouverture : {opened['ouverte_le']}")

    sym = gene_symbols()
    groups558 = pd.read_csv(GEO / "sealed" / "cohort558_annotation.csv", dtype=str)
    flagged = pd.read_csv(RES / "QC_cohorte331_puces.csv")
    variants = args.only or ["principale", "geo", "exclusion", "top5000"]
    sources = {"principale": "rma", "exclusion": "rma", "top5000": "rma", "geo": "geo"}
    cache, summary = {}, {"preenregistrement": OSF_URL, "variantes": {}}

    for name in variants:
        src = sources[name]
        if src not in cache:
            X331 = load_rma(331) if src == "rma" else load_geo(331)
            X558 = load_rma(558) if src == "rma" else load_geo(558)
            A, B, best = collapse(X331, X558, sym)
            g = groups558.set_index("gsm").loc[X558.columns, "4aa group (1,2,3,4)"].values
            ref = Reference(B, g, A.shape[1], np.random.default_rng([SEED, 558]))
            cache[src] = (A, ref, list(X331.columns), best)
            best.to_csv(out / f"genes_{src}.csv", index=False)
            log(f"données {src} : {A.shape[0]} + {X558.shape[1]} échantillons, {A.shape[1]} gènes ; "
                f"référence 558 : {ref.info}")
        A, ref, samples331, _ = cache[src]
        pool = np.arange(len(samples331))
        if name == "exclusion":
            bad = set(flagged.loc[flagged.signalee, "gsm"])
            pool = np.array([i for i, s in enumerate(samples331) if s not in bad])
        top = 5000 if name == "top5000" else None
        log(f"variante {name} : {len(pool)} puces, gènes = {top or 'tous'}")
        mres, stab, perm, full = run_variant(name, A, ref, pool, top, extras=(name == "principale"), log=log)
        mres.to_csv(out / f"tirages_{name}.csv", index=False, float_format="%.6f")
        full.to_csv(out / f"cohorte_entiere_{name}.csv", index=False, float_format="%.6f")
        summary["variantes"][name] = {"reference": ref.info, "puces": int(len(pool))}
        if name == "principale":
            stab.to_csv(out / "S2_stabilite.csv", index=False, float_format="%.6f")
            perm.to_csv(out / "S3_permutees.csv", index=False)
            s5, s5info = s5_table(A, ref)
            s5.to_csv(out / "S5_H3_recouvrement.csv", index=False, float_format="%.6f")
            summary["verdicts"] = verdicts(mres, perm, s5)
            summary["S5"] = s5info
            log("VERDICTS : " + json.dumps(summary["verdicts"], ensure_ascii=False))
        (out / "resume.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=float) + "\n")
    log("analyse terminée")


if __name__ == "__main__":
    main()
