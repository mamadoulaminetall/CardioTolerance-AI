"""Volet A — analyse EXPLORATOIRE de GSE2596 (section 7 du préenregistrement https://osf.io/6htjn).

AUCUNE HYPOTHÈSE, AUCUNE RÈGLE DE DÉCISION : description seulement.

Plan enregistré : moyenner les réplicats techniques ; garder rejet aigu, non-rejet et pré-rejet ;
exclure les infections (réactivation de Chagas, toxoplasmose) ; centrer chaque gène dans chacun
des deux lots (« summer », « winter ») ; appliquer RMT ; décrire les axes retenus et leur lien avec
le statut de rejet.

Sources fiables utilisées : listes de groupes et de lots du résumé de la série GEO ; numéro d'ARN
(1re ligne de description) pour les réplicats. Les autres champs de description sont décalés pour
une partie des puces et ne sont pas utilisés.

Choix NON prévus au plan (déclarés, exploratoires) :
  - valeurs manquantes (56 % des valeurs de la série) : spots présents dans ≥ 80 % des échantillons ;
    manques restants remplacés par 0 après centrage par lot (= moyenne du lot) ;
    vérification : spots complets seulement, sans remplacement ;
  - lien avec le rejet : aire sous la courbe ROC (AUC) rejet vs non-rejet des coordonnées de chaque
    axe retenu, avec p de Mann-Whitney NON corrigée ; le signe d'un axe est arbitraire (AUC < 0,5
    = même séparation dans l'autre sens).
Limites : 42 échantillons de 17 patients (non indépendants), puces bicolores anciennes.

Usage : python -I scripts/rmt_gse2596_exploratory.py   (télécharge la série si absente)
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rmt_denoise as rmt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "geo" / "GSE2596" / "raw" / "GSE2596_series_matrix.txt.gz"
URL = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE2nnn/GSE2596/matrix/GSE2596_series_matrix.txt.gz"
OUT = ROOT / "results" / "rmt_gse2596"
KEEP = ("acute rejection", "pre-rejection", "non-rejection")
LABELS = ("acute rejection", "pre-rejection", "Chagas disease reactivation", "Toxoplasma myocarditis", "non-rejection")
INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
COLORS = {"non-rejection": "#2a78d6", "acute rejection": "#eb6834", "pre-rejection": "#1baf7a"}
FR = {"non-rejection": "Non-rejet", "acute rejection": "Rejet aigu", "pre-rejection": "Pré-rejet"}


def load():
    if not SRC.exists():
        SRC.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["curl", "-fsSL", "-A", "geo-download-script", "-o", str(SRC), URL], check=True)
    lines, begin = [], None
    with gzip.open(SRC, "rt", encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f):
            if line.startswith("!series_matrix_table_begin"):
                begin = i
                break
            lines.append(line)
    rows = list(csv.reader(lines, delimiter="\t", quotechar='"'))
    groups, cur = {}, None
    for s in (r[1].strip() for r in rows if r and r[0] == "!Series_summary"):
        if s.endswith(":"):
            cur = s[:-1]
        elif cur and s.startswith("GSM"):
            groups[cur] = set(re.findall(r"GSM\d+", s))
            cur = None
    meta = {}
    for r in rows:
        if r and r[0].startswith("!Sample_"):
            meta.setdefault(r[0], []).append(r[1:])
    first = meta["!Sample_description"][0]
    assert all(v.strip().lower().startswith("arna") for v in first)
    ann = pd.DataFrame({"gsm": meta["!Sample_geo_accession"][0], "aRNA": [re.sub(r"\D", "", v) for v in first]})
    ann["groupe"] = ann.gsm.map(lambda g: next((k for k in LABELS if g in groups[k]), "sans étiquette"))
    ann["pre_chagas"] = ann.gsm.isin(groups["pre-Chagas disease reactivation"])
    ann["lot"] = ann.gsm.map(lambda g: "summer" if g in groups['first subset ("summer")'] else "winter")
    table = pd.read_csv(SRC, sep="\t", skiprows=begin + 1, index_col=0, comment="!")
    table.index = table.index.astype(str)
    assert list(table.columns) == list(ann.gsm)
    return table, ann, hashlib.sha256(SRC.read_bytes()).hexdigest()


def prepare(table, ann, min_present=0.8, impute=True):
    keep = ann[ann.groupe.isin(KEEP)]
    bio = keep.groupby("aRNA").agg(groupe=("groupe", "first"), lot=("lot", "first"),
                                   pre_chagas=("pre_chagas", "max"), puces=("gsm", list))
    X = pd.DataFrame({a: table[g].mean(axis=1, skipna=True) for a, g in bio.puces.items()})  # spots × échantillons
    present = X.notna().mean(axis=1)
    X = X[present >= min_present] if impute else X[present == 1.0]
    for lot in bio.lot.unique():
        cols = bio.index[bio.lot == lot]
        X[cols] = X[cols].sub(X[cols].mean(axis=1, skipna=True), axis=0)
    if impute:
        X = X.fillna(0.0)
    return X.T, bio  # échantillons × spots


def describe(Xs, bio, label):
    res = rmt.denoise(Xs, n_perm=199, rng=20261126, n_keep=10)
    k_show = max(res.k, 3)
    y = bio.loc[Xs.index, "groupe"].values
    rows = []
    for j in range(min(k_show, res.scores.shape[1])):
        sc = res.scores[:, j]
        r_, n_ = sc[y == "acute rejection"], sc[y == "non-rejection"]
        u = mannwhitneyu(r_, n_, alternative="two-sided")
        rows.append({"analyse": label, "axe": j + 1, "retenu_RMT": j < res.k,
                     "valeur_propre": res.eigenvalues[j], "pct_variance": 100 * res.eigenvalues[j] / res.p,
                     "p_tracy_widom": res.tw_pvalues[j], "p_permutation": res.perm_pvalues[j],
                     "AUC_rejet_vs_non_rejet": u.statistic / (len(r_) * len(n_)),
                     "p_mann_whitney_non_corrigee": u.pvalue})
    k_perm = int(np.argmin(res.perm_pvalues < 0.05)) if not (res.perm_pvalues < 0.05).all() else len(res.perm_pvalues)
    info = {"analyse": label, "n": res.n, "p": res.p, "gamma": res.gamma, "sigma2": res.sigma2,
            "lambda_plus": res.lambda_plus, "k_RMT": res.k, "k_MP_sigma1": int((res.eigenvalues > rmt.mp_edges(res.n_eff, res.p)[1]).sum()),
            "k_permutations": k_perm}
    return res, pd.DataFrame(rows), info


def style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def figure(res, bio, idx, info, path):
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.0), facecolor=SURFACE)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.77, bottom=0.27, wspace=0.25)
    ax = axes[0]
    style(ax)
    eig = res.eigenvalues
    K = min(40, len(eig))
    kk = min(res.k, K)
    ax.bar(np.arange(1, K + 1), eig[:K], color="#9ec5f4", edgecolor=SURFACE, linewidth=1.0,
           label="Axes non retenus")
    ax.bar(np.arange(1, kk + 1), eig[:kk], color="#2a78d6", edgecolor=SURFACE, linewidth=1.0,
           label=f"Axes retenus par RMT ({res.k})")
    ax.axhline(res.lambda_plus, color=INK2, lw=1.2,
               label=f"Bord MP, bruit réestimé (σ² = {fr(res.sigma2, 2)})")
    ax.axhline(rmt.mp_edges(res.n_eff, res.p, 1.0)[1], color=INK, lw=1.2, ls=(0, (4, 3)),
               label="Bord MP, σ² = 1")
    ax.set_xlabel("Rang de l'axe", color=INK, fontsize=10)
    ax.set_ylabel("Valeur propre", color=INK, fontsize=10)
    ax.set_title(f"A. Spectre ({K} premiers axes)", loc="left", fontsize=11, color=INK)

    ax = axes[1]
    style(ax)
    y = bio.loc[idx, "groupe"].values
    m = min(3, res.scores.shape[1])
    rng = np.random.default_rng(0)
    for j in range(m):
        for g in ("non-rejection", "acute rejection", "pre-rejection"):
            sc = res.scores[y == g, j] / res.singular_values[j]
            off = {"non-rejection": -0.2, "acute rejection": 0.0, "pre-rejection": 0.2}[g]
            ax.scatter(j + 1 + off + rng.uniform(-0.05, 0.05, len(sc)), sc, s=26, color=COLORS[g],
                       edgecolor=SURFACE, linewidth=0.6, label=FR[g] if j == 0 else None)
    ax.set_xticks(range(1, m + 1), [f"axe {j + 1}" for j in range(m)])
    ax.set_ylabel("Coordonnée de l'échantillon (normalisée)", color=INK, fontsize=10)
    ax.set_title("B. Échantillons sur les 3 premiers axes", loc="left", fontsize=11, color=INK)

    fig.text(0.07, 0.94, "GSE2596 : analyse EXPLORATOIRE (sans hypothèse)", fontsize=12.5, color=INK, weight="bold")
    fig.text(0.07, 0.895, f"{info['n']} biopsies (réplicats moyennés, infections exclues), {info['p']} spots, "
             f"centrage par lot. Données publiques GEO.", fontsize=9.5, color=INK2)
    fig.text(0.07, 0.855, "Section 7 du préenregistrement osf.io/6htjn : description seulement, aucune "
             "règle de décision.", fontsize=9.5, color="#b4231f")
    h = axes[0].get_legend_handles_labels()[0] + axes[1].get_legend_handles_labels()[0]
    lab = axes[0].get_legend_handles_labels()[1] + axes[1].get_legend_handles_labels()[1]
    fig.legend(h, lab, loc="lower center", bbox_to_anchor=(0.5, 0.0), ncol=4, frameon=False, fontsize=9, labelcolor=INK)
    fig.savefig(path, dpi=200, facecolor=SURFACE)
    plt.close(fig)


def fr(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    table, ann, sha = load()
    out_tables, infos = [], []
    for label, kw in (("principale (spots ≥ 80 % présents, manques = 0)", {}),
                      ("vérification (spots complets, sans remplacement)", {"impute": False})):
        Xs, bio = prepare(table, ann, **kw)
        res, tab, info = describe(Xs, bio, label)
        out_tables.append(tab)
        infos.append(info)
        if not kw:
            figure(res, bio, Xs.index, info, OUT / "EXPLORATOIRE_GSE2596_fig.png")
            n_groups = bio.groupe.value_counts().to_dict()
            n_prech = int(bio.pre_chagas.sum())
    tab = pd.concat(out_tables)
    tab.to_csv(OUT / "EXPLORATOIRE_GSE2596_axes.csv", index=False, float_format="%.6f")
    L = ["# GSE2596 — analyse EXPLORATOIRE (section 7 du préenregistrement https://osf.io/6htjn)", "",
         "> **Sans hypothèse ni règle de décision : description seulement.** Données publiques GEO",
         "> (Morgun et al., *Circ Res* 2006). Généré par `scripts/rmt_gse2596_exploratory.py`.", "",
         f"- Série GEO SHA-256 `{sha}`.",
         f"- Échantillons biologiques après fusion des 11 paires de réplicats et exclusion des infections : "
         f"{sum(n_groups.values())} ({', '.join(f'{FR[g]} {c}' for g, c in n_groups.items())}), dont {n_prech} "
         "non-rejets prélevés avant une réactivation de Chagas ; 17 patients au total dans la série (non indépendants).",
         "- Choix non prévus au plan (valeurs manquantes, AUC) : voir l'en-tête du script.", "",
         "## Résumé", "", "| analyse | n | spots | γ | σ² | axes RMT | bord MP (σ² = 1) | permutations |",
         "|---|---|---|---|---|---|---|---|"]
    for i in infos:
        L.append(f"| {i['analyse']} | {i['n']} | {i['p']} | {fr(i['gamma'], 1)} | {fr(i['sigma2'])} | {i['k_RMT']} | "
                 f"{i['k_MP_sigma1']} | {i['k_permutations']} |")
    L += ["", "## Axes et lien avec le rejet (rejet aigu vs non-rejet)", "",
          "| analyse | axe | retenu RMT | % variance | p Tracy-Widom | p permutations | AUC | p Mann-Whitney (non corrigée) |",
          "|---|---|---|---|---|---|---|---|"]
    def pfmt(x):  # p très petites : l'arrondi numérique peut donner ±0
        return "< 1e-15" if x < 1e-15 else f"{x:.2g}"

    for r in tab[tab.axe <= 10].itertuples():
        L.append(f"| {r.analyse} | {r.axe} | {'oui' if r.retenu_RMT else 'non'} | {fr(r.pct_variance, 1)} | "
                 f"{pfmt(r.p_tracy_widom)} | {fr(r.p_permutation)} | {fr(r.AUC_rejet_vs_non_rejet, 2)} | "
                 f"{pfmt(r.p_mann_whitney_non_corrigee)} |")
    L.append("")
    L.append("Tableau limité aux 10 premiers axes ; tous les axes sont dans `EXPLORATOIRE_GSE2596_axes.csv`.")
    L += ["", "Lecture : AUC proche de 0,5 = l'axe ne sépare pas rejet et non-rejet ; proche de 0 ou de 1 = il les "
          "sépare (le signe d'un axe est arbitraire). Avec 12 rejets et 28 non-rejets de 17 patients, ces chiffres "
          "sont indicatifs.", ""]
    (OUT / "EXPLORATOIRE_GSE2596.md").write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
