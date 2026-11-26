"""SIMULATION — étape 0 du volet A (RMT-Transplant). DONNÉES ENTIÈREMENT SYNTHÉTIQUES.

Aucune donnée de patient. Aucun résultat sur données réelles. Ces chiffres montrent
seulement comment la méthode se comporte quand on connaît la vérité.

Question : quand peu d'échantillons cachent quelques « signatures » (groupes de gènes
corrélés) dans beaucoup de bruit, combien d'axes chaque méthode retient-elle, combien
sont faux, et peut-on prédire la fiabilité de la liste de gènes d'un axe ?

Plan
  - p = 5000 gènes ; n ∈ {20, 40, 80, 160} échantillons (tailles du plan préenregistré).
  - Scénario « signal » : 3 groupes de gènes cachés, corrélation 0,2 dans chaque groupe :
      facteur 1 : 246 gènes → valeur propre de population ℓ = 1 + 245 × 0,2 = 50
      facteur 2 :  76 gènes → ℓ = 16
      facteur 3 :  38 gènes → ℓ = 8,4
    Limite théorique (Baik, Ben Arous & Péché 2005) : un axe n'est récupérable que si
    ℓ > 1 + √(p / (n − 1)), donc à partir de n ≈ 4, 24 et 93 échantillons.
  - Scénario « bruit pur » (contrôle négatif) : aucun signal, tout axe retenu est faux.
  - R répétitions par cas (200 par défaut), graine fixe.

Méthodes comparées
  - Kaiser (λ > 1), 80 % de variance cumulée, ACP à 10 axes fixes : pratiques courantes ;
  - bord de Marchenko-Pastur seul (σ² = 1, sans test) ;
  - RMT : bord MP + test de Tracy-Widom, σ² réestimée (rmt_denoise, réglage par défaut) ;
  - analyse parallèle par permutations (Horn 1965), 39 permutations par tirage.

Un axe retenu est « vrai » s'il recouvre un facteur caché (cos² > 0,01, soit 50 fois le
niveau du hasard 1/p) ; chaque facteur ne compte qu'une fois. Sinon il est « faux ».

Sorties : results/rmt_simulation/ (toutes préfixées SIMULATION_)
  SIMULATION_resume.csv       méthode × n × scénario : axes retenus, vrais, faux
  SIMULATION_detection.csv    taux de détection de chaque facteur par n (RMT, permutations)
  SIMULATION_fiabilite.csv    axes retenus par RMT : cos² prédit vs observé, précision des gènes
  SIMULATION_fig1_spectre.png, SIMULATION_fig2_faux_axes.png, SIMULATION_fig3_fiabilite.png
  LISEZMOI.md                 résumé généré à partir des CSV

Usage : python scripts/rmt_simulation.py [--reps 200] [--n-perm 39] [--seed 20261126]
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rmt_denoise as rmt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "results" / "rmt_simulation"

P = 5000
NS = (20, 40, 80, 160)
RHO = 0.2
SIZES = (246, 76, 38)              # gènes par facteur caché
MATCH_THR = 0.01                   # cos² minimal pour dire qu'un axe recouvre un facteur
ALPHA = 0.05

METHODS = [  # (clé, libellé, couleur, marqueur) — palette validée (dataviz), ordre fixe
    ("rmt", "RMT : bord MP + Tracy-Widom", "#2a78d6", "o"),
    ("perm", "Permutations (analyse parallèle)", "#eb6834", "s"),
    ("mp", "Bord MP seul", "#1baf7a", "^"),
    ("fixed10", "ACP à 10 axes fixes", "#eda100", "D"),
    ("var80", "80 % de variance", "#e87ba4", "v"),
    ("kaiser", "Kaiser (λ > 1)", "#008300", "P"),
]
FACTOR_COLORS = ("#2a78d6", "#eb6834", "#1baf7a")
INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
LABEL = "SIMULATION — données synthétiques, aucune donnée de patient"


def ell_true():
    return np.array([1 + (m - 1) * RHO for m in SIZES])


def n_threshold(ell):
    """Plus petit n tel que ℓ > 1 + √(p/(n−1))."""
    return int(np.floor(1 + P / (ell - 1) ** 2)) + 1


def simulate(n, signal, rng):
    X = rng.standard_normal((n, P))
    if signal:
        start = 0
        for m in SIZES:
            f = rng.standard_normal((n, 1))
            X[:, start:start + m] = np.sqrt(RHO) * f + np.sqrt(1 - RHO) * X[:, start:start + m]
            start += m
    return X


def true_directions():
    U = np.zeros((P, len(SIZES)))
    start = 0
    for j, m in enumerate(SIZES):
        U[start:start + m, j] = 1 / np.sqrt(m)
        start += m
    return U


def count_true(cos2_axes, k):
    """Nombre d'axes parmi les k premiers qui recouvrent un facteur distinct (glouton)."""
    used, matches = set(), {}
    for i in range(k):
        j = int(np.argmax(cos2_axes[i]))
        if cos2_axes[i, j] > MATCH_THR and j not in used:
            used.add(j)
            matches[i] = j
    return len(matches), matches


def one_run(n, signal, rng, n_perm, U_true):
    X = simulate(n, signal, rng)
    Z, _ = rmt.standardize(X)
    eig, U, s, V = rmt.spectrum(Z)
    N, m = n - 1, len(eig)
    cos2_axes = (V.T @ U_true) ** 2 if signal else np.zeros((m, len(SIZES)))

    sel = rmt.select_components(eig, N, P, alpha=ALPHA, n_report=0)
    null_max = rmt.permutation_null(Z, n_perm, rng)
    perm_p = rmt.permutation_pvalues(eig[:20], null_max)
    _, lam_plus1 = rmt.mp_edges(N, P, 1.0)
    k = {
        "rmt": sel["k"],
        "perm": int(np.argmin(perm_p < ALPHA)) if not (perm_p < ALPHA).all() else 20,
        "mp": int(np.sum(eig > lam_plus1)),
        "fixed10": min(10, m),
        "var80": int(np.searchsorted(np.cumsum(eig) / P, 0.80) + 1),
        "kaiser": int(np.sum(eig > 1.0)),
    }
    rows, rel = [], []
    for key, kk in k.items():
        n_true, matches = count_true(cos2_axes, kk) if signal else (0, {})
        rows.append({"methode": key, "k": kk, "vrais": n_true, "faux": kk - n_true,
                     **{f"detecte_f{j + 1}": int(j in matches.values()) for j in range(len(SIZES))}})
        if key == "rmt" and kk > 0 and signal:
            ell_hat, cos2_pred = rmt.spike_estimates(eig[:kk], N, P, sel["sigma2"])
            for i in range(kk):
                j = matches.get(i)
                row = {"axe": i + 1, "facteur": None if j is None else j + 1,
                       "ell_vrai": None if j is None else ell_true()[j],
                       "ell_estime": ell_hat[i], "cos2_predit": cos2_pred[i],
                       "cos2_observe": cos2_axes[i].max(), "precision_genes": None}
                if j is not None:
                    mj = SIZES[j]
                    top = np.argsort(-np.abs(V[:, i]))[:mj]
                    row["precision_genes"] = float(np.mean(U_true[top, j] > 0))
                rel.append(row)
    return rows, rel


def run_all(reps, n_perm, seed):
    rng = np.random.default_rng(seed)
    U_true = true_directions()
    res, rel = [], []
    for scen, signal in (("signal", True), ("bruit_pur", False)):
        for n in NS:
            t0 = time.time()
            for r in range(reps):
                rows, rr = one_run(n, signal, rng, n_perm, U_true)
                for row in rows:
                    res.append({"scenario": scen, "n": n, "tirage": r, **row})
                for row in rr:
                    rel.append({"n": n, "tirage": r, **row})
            print(f"  {scen:9s} n = {n:3d} : {reps} tirages en {time.time() - t0:.0f} s", flush=True)
    return pd.DataFrame(res), pd.DataFrame(rel)


# ---------------------------------------------------------------------------
# Figures (règles : aucun texte superposé, légende dans le canvas, vérifier le PNG)
# ---------------------------------------------------------------------------
def _style(ax):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def fig_spectrum(seed):
    rng = np.random.default_rng(seed + 1)
    n = 80
    X = simulate(n, True, rng)
    res = rmt.denoise(X, n_keep=5)
    eig, N = res.eigenvalues, res.n_eff
    fig, ax = plt.subplots(figsize=(8.6, 4.9), facecolor=SURFACE)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.80, bottom=0.21)
    _style(ax)
    bulk = eig[res.k:]
    ax.hist(bulk, bins=24, density=True, color="#9ec5f4", edgecolor=SURFACE, linewidth=1.5,
            label=f"Valeurs propres du bruit ({len(bulk)})")
    x = np.linspace(res.lambda_minus, res.lambda_plus, 800)
    ax.plot(x, rmt.mp_pdf(x, N, res.p, res.sigma2), color=INK, lw=2,
            label="Loi de Marchenko-Pastur (prédiction)")
    ax.axvline(res.lambda_plus, color=INK2, lw=1.2)
    ymax = ax.get_ylim()[1]
    ax.text(res.lambda_plus, ymax * 0.97, r"  bord $\lambda_+$", color=INK2, fontsize=9, va="top")
    for i in range(res.k):
        y = ymax * (0.10 + 0.12 * i)
        ax.plot([eig[i]], [y], marker="o", ms=9, color="#2a78d6",
                markeredgecolor=SURFACE, markeredgewidth=2, linestyle="none",
                label="Axes retenus (signal)" if i == 0 else None)
        ax.annotate(f"axe {i + 1} (λ = {eig[i]:.0f})", (eig[i], y), xytext=(9, 0),
                    textcoords="offset points", ha="left", va="center", fontsize=9, color=INK)
    ax.set_xlim(res.lambda_minus * 0.9, max(eig[0] * 1.18, res.lambda_plus * 1.4))
    ax.set_xlabel("Valeur propre de la matrice de corrélation", color=INK, fontsize=10)
    ax.set_ylabel("Densité", color=INK, fontsize=10)
    fig.text(0.08, 0.95, "Un tirage : 80 échantillons × 5 000 gènes, 3 signatures cachées",
             fontsize=12.5, color=INK, weight="bold")
    fig.text(0.08, 0.895, LABEL, fontsize=9.5, color="#b4231f")
    fig.text(0.08, 0.85, f"Retenus : {res.k} axes. La 3e signature (38 gènes) est sous la limite "
             f"théorique de détection à n = 80.", fontsize=9.5, color=INK2)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=3, frameon=False,
              fontsize=9, labelcolor=INK)
    path = OUT / "SIMULATION_fig1_spectre.png"
    fig.savefig(path, dpi=200, facecolor=SURFACE)
    plt.close(fig)
    return path


def fig_false_axes(summary):
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.2), facecolor=SURFACE)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.78, bottom=0.27, wspace=0.25)
    xs = np.arange(len(NS))
    classical = ("fixed10", "var80", "kaiser")
    panels = [
        (axes[0], "signal", "faux", "Faux axes retenus (moyenne)",
         "A. Trois signatures cachées", [k for k, *_ in METHODS]),
        (axes[1], "bruit_pur", "pct_au_moins_un_faux", "Tirages avec ≥ 1 faux axe (%)",
         "B. Bruit pur : zoom sur 0–15 %", [k for k, *_ in METHODS if k not in classical]),
    ]
    for ax, scen, col, ylab, title, keys in panels:
        _style(ax)
        sub = summary[summary.scenario == scen]
        for key, label, color, marker in METHODS:
            d = sub[sub.methode == key].set_index("n").loc[list(NS)]
            ax.plot(xs, d[col] if key in keys else np.full(len(NS), np.nan), color=color, lw=2,
                    marker=marker, ms=8, markeredgecolor=SURFACE, markeredgewidth=1.5, label=label)
        ax.set_xticks(xs, [str(n) for n in NS])
        ax.set_xlabel("Nombre d'échantillons n", color=INK, fontsize=10)
        ax.set_ylabel(ylab, color=INK, fontsize=10)
        ax.set_title(title, loc="left", fontsize=11, color=INK)
    # A : trois courbes confondues à zéro → étiquette directe
    axes[0].text(xs[-1], 19, "RMT, permutations et bord MP seul :\n≈ 0 (courbes confondues en bas)",
                 ha="right", va="center", fontsize=9, color=INK2)
    # B : les règles classiques sont à 100 % → hors échelle, dit en clair
    null = summary[summary.scenario == "bruit_pur"]
    pct_cl = null[null.methode.isin(classical)].pct_au_moins_un_faux
    axes[1].set_ylim(-0.6, 15)
    axes[1].axhline(100 * ALPHA, color=INK2, lw=1, ls=(0, (4, 3)))
    axes[1].text(xs[-1], 100 * ALPHA + 0.3, f"niveau visé {100 * ALPHA:.0f} %", fontsize=9,
                 color=INK2, va="bottom", ha="right")
    axes[1].text(xs[0], 14.6, f"10 axes fixes, 80 % de variance, Kaiser :\n"
                 f"{pct_cl.min():.0f} % des tirages (hors échelle)", fontsize=9, color=INK2, va="top")
    fig.text(0.07, 0.94, "Les règles classiques retiennent des dizaines d'axes de pur bruit",
             fontsize=12.5, color=INK, weight="bold")
    fig.text(0.07, 0.895, LABEL, fontsize=9.5, color="#b4231f")
    sig = summary[summary.scenario == "signal"]
    worst = {k: sig[sig.methode == k].faux.max() for k in ("rmt", "kaiser")}
    fig.text(0.07, 0.855, f"Faux axes en moyenne, pire cas : RMT {worst['rmt']:.2f} ; Kaiser "
             f"{worst['kaiser']:.0f} (valeurs exactes : SIMULATION_resume.csv).",
             fontsize=9.5, color=INK2)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", bbox_to_anchor=(0.5, 0.01), ncol=3, frameon=False,
               fontsize=9, labelcolor=INK)
    path = OUT / "SIMULATION_fig2_faux_axes.png"
    fig.savefig(path, dpi=200, facecolor=SURFACE)
    plt.close(fig)
    return path


def fig_reliability(rel, detection):
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.2), facecolor=SURFACE)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.78, bottom=0.27, wspace=0.25)
    ells = ell_true()
    labels = [f"Facteur {j + 1} ({m} gènes, ℓ = {ells[j]:g})" for j, m in enumerate(SIZES)]

    ax = axes[0]
    _style(ax)
    ax.plot([0, 1], [0, 1], color=INK2, lw=1)
    ax.text(0.50, 0.82, "diagonale : prédit = observé", ha="right", fontsize=9, color=INK2)
    d = rel.dropna(subset=["facteur"])
    for j in range(len(SIZES)):
        dj = d[d.facteur == j + 1]
        ax.scatter(dj.cos2_predit, dj.cos2_observe, s=22, color=FACTOR_COLORS[j],
                   edgecolor=SURFACE, linewidth=0.6, alpha=0.8, label=labels[j])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("cos² prédit par la théorie", color=INK, fontsize=10)
    ax.set_ylabel("cos² observé (vrai facteur connu)", color=INK, fontsize=10)
    ax.set_title("A. Fiabilité de la liste de gènes d'un axe", loc="left", fontsize=11, color=INK)

    ax = axes[1]
    _style(ax)
    xs = np.arange(len(NS))
    for j in range(len(SIZES)):
        dj = detection[(detection.methode == "rmt") & (detection.facteur == j + 1)].set_index("n")
        ax.plot(xs, 100 * dj.loc[list(NS), "taux_detection"], color=FACTOR_COLORS[j], lw=2,
                marker="o", ms=8, markeredgecolor=SURFACE, markeredgewidth=1.5)
    ax.set_xticks(xs, [str(n) for n in NS])
    ax.set_ylim(-4, 104)
    ax.set_xlabel("Nombre d'échantillons n", color=INK, fontsize=10)
    ax.set_ylabel("Facteur détecté par RMT (% des tirages)", color=INK, fontsize=10)
    ax.set_title("B. Détection selon la taille de la cohorte", loc="left", fontsize=11, color=INK)

    fig.text(0.07, 0.94, "La théorie prédit la fiabilité de chaque axe avant toute validation",
             fontsize=12.5, color=INK, weight="bold")
    fig.text(0.07, 0.895, LABEL, fontsize=9.5, color="#b4231f")
    thr = ", ".join(f"F{j + 1} dès n ≈ {n_threshold(e)}" for j, e in enumerate(ells))
    fig.text(0.07, 0.855, f"Limite théorique de détection : {thr}.", fontsize=9.5, color=INK2)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", bbox_to_anchor=(0.5, 0.01), ncol=3, frameon=False,
               fontsize=9, labelcolor=INK, markerscale=1.6)
    path = OUT / "SIMULATION_fig3_fiabilite.png"
    fig.savefig(path, dpi=200, facecolor=SURFACE)
    plt.close(fig)
    return path


# ---------------------------------------------------------------------------
def summarise(res):
    g = res.groupby(["scenario", "n", "methode"])
    summary = g.agg(k_moyen=("k", "mean"), vrais_moyen=("vrais", "mean"),
                    faux=("faux", "mean"),
                    pct_au_moins_un_faux=("faux", lambda s: 100 * np.mean(s > 0))).reset_index()
    order = {k: i for i, (k, *_) in enumerate(METHODS)}
    summary = summary.sort_values(["scenario", "n", "methode"], key=lambda c: c.map(order)
                                  if c.name == "methode" else c).reset_index(drop=True)
    det = []
    sig = res[res.scenario == "signal"]
    ells = ell_true()
    for key in ("rmt", "perm"):
        for n in NS:
            d = sig[(sig.methode == key) & (sig.n == n)]
            for j in range(len(SIZES)):
                det.append({"methode": key, "n": n, "facteur": j + 1, "genes": SIZES[j],
                            "ell": ells[j], "detectable_en_theorie": n >= n_threshold(ells[j]),
                            "taux_detection": d[f"detecte_f{j + 1}"].mean()})
    return summary, pd.DataFrame(det)


def _range_pct(summary, key):
    v = summary[(summary.scenario == "bruit_pur") & (summary.methode == key)].pct_au_moins_un_faux
    return f"{v.min():.1f} % à {v.max():.1f} %".replace(".", ",")


def write_readme(summary, detection, rel, args, elapsed):
    def val(scen, n, key, col):
        return summary[(summary.scenario == scen) & (summary.n == n) & (summary.methode == key)][col].iloc[0]

    lines = [
        "# SIMULATION — volet A (matrices aléatoires)",
        "",
        "> **Données entièrement synthétiques.** Aucune donnée de patient, aucun résultat sur",
        "> données réelles. Généré par `scripts/rmt_simulation.py` : ne pas modifier à la main.",
        "",
        f"Paramètres : p = {P} gènes ; n = {', '.join(map(str, NS))} ; {args.reps} tirages par cas ; "
        f"{args.n_perm} permutations par tirage ; α = {ALPHA} ; graine {args.seed}"
        + (f" ; durée {elapsed / 60:.1f} min." if elapsed is not None else "."),
        f"Signatures cachées : {', '.join(f'{m} gènes (ℓ = {e:g})' for m, e in zip(SIZES, ell_true()))}, "
        f"corrélation {RHO} dans chaque groupe.",
        "",
        "## Faux axes retenus",
        "",
        "| n | " + " | ".join(lbl for _, lbl, _, _ in METHODS) + " |",
        "|---|" + "---|" * len(METHODS),
    ]
    for n in NS:
        cells = [f"{val('signal', n, k, 'faux'):.2f} / {val('bruit_pur', n, k, 'pct_au_moins_un_faux'):.1f} %"
                 for k, *_ in METHODS]
        lines.append(f"| {n} | " + " | ".join(cells) + " |")
    lines += ["", "Lecture : « faux axes en moyenne avec 3 signatures cachées / % de tirages avec au moins "
              "un faux axe sur bruit pur ».", "", "## Détection de chaque signature par RMT (% des tirages)", "",
              "| n | " + " | ".join(f"Facteur {j + 1}" for j in range(len(SIZES))) + " |",
              "|---|" + "---|" * len(SIZES)]
    for n in NS:
        d = detection[(detection.methode == "rmt") & (detection.n == n)].sort_values("facteur")
        cells = [f"{100 * r.taux_detection:.0f} %{'' if r.detectable_en_theorie else ' (sous la limite)'}"
                 for r in d.itertuples()]
        lines.append(f"| {n} | " + " | ".join(cells) + " |")
    d = rel.dropna(subset=["facteur"])
    mae = np.mean(np.abs(d.cos2_predit - d.cos2_observe))
    lines += ["", "## Fiabilité des axes retenus par RMT", "",
              f"Écart absolu moyen entre cos² prédit et observé : {mae:.3f} ({len(d)} axes).",
              "", "| n | facteur | cos² prédit (moy.) | cos² observé (moy.) | précision des gènes (moy.) | axes |",
              "|---|---|---|---|---|---|"]
    for (n, f), dd in d.groupby(["n", "facteur"]):
        lines.append(f"| {n} | {int(f)} | {dd.cos2_predit.mean():.3f} | {dd.cos2_observe.mean():.3f} | "
                     f"{dd.precision_genes.mean():.2f} | {len(dd)} |")
    lines += ["", "Précision des gènes : part des m gènes les plus chargés sur l'axe qui appartiennent "
              "vraiment à la signature (m = taille de la signature).", "",
              "## Limites", "",
              "- Bruit gaussien homogène et signatures en blocs : cas idéal. Les vraies données ont des "
              "effets de lot, des gènes très variables et des signatures qui se chevauchent.",
              "- Le test de Tracy-Widom (centrage de Johnstone, établi pour une covariance) est "
              "appliqué ici à une matrice de corrélation. Sur bruit pur, RMT a retenu au moins un "
              f"faux axe dans {_range_pct(summary, 'rmt')} des tirages selon n, pour un niveau "
              f"visé de {100 * ALPHA:.0f} % (permutations : {_range_pct(summary, 'perm')}).",
              "- Ces résultats ne disent rien du rejet ni de la tolérance : ils valident l'outil.", ""]
    (OUT / "LISEZMOI.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--reps", type=int, default=200)
    ap.add_argument("--n-perm", type=int, default=39)
    ap.add_argument("--seed", type=int, default=20261126)
    ap.add_argument("--figures-only", action="store_true",
                    help="redessiner figures et LISEZMOI à partir des CSV existants")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    print(LABEL)
    t0 = time.time()
    if args.figures_only:
        summary = pd.read_csv(OUT / "SIMULATION_resume.csv")
        detection = pd.read_csv(OUT / "SIMULATION_detection.csv")
        rel = pd.read_csv(OUT / "SIMULATION_fiabilite.csv")
        elapsed = None
    else:
        res, rel = run_all(args.reps, args.n_perm, args.seed)
        summary, detection = summarise(res)
        summary.to_csv(OUT / "SIMULATION_resume.csv", index=False, float_format="%.4f")
        detection.to_csv(OUT / "SIMULATION_detection.csv", index=False, float_format="%.4f")
        rel.to_csv(OUT / "SIMULATION_fiabilite.csv", index=False, float_format="%.4f")
        elapsed = time.time() - t0
    for f in (fig_spectrum(args.seed), fig_false_axes(summary), fig_reliability(rel, detection)):
        print("  figure :", f.relative_to(ROOT))
    write_readme(summary, detection, rel, args, elapsed)
    print(f"terminé en {(time.time() - t0) / 60:.1f} min → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
