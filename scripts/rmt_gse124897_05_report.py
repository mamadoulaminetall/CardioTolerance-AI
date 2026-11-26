"""Volet A, étape 4c — rapport des résultats PRÉENREGISTRÉS (https://osf.io/6htjn).

Lit results/rmt_gse124897/analyse/*.csv (rmt_gse124897_04_analysis.py) et écrit :
  results/rmt_gse124897/RESULTATS.md   verdicts H1-H3 + tableaux (généré, ne pas éditer)
  results/rmt_gse124897/RESULTATS_fig.png

Aucune analyse nouvelle : uniquement la mise en forme des sorties préenregistrées.
Usage : python -I scripts/rmt_gse124897_05_report.py
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "results" / "rmt_gse124897"
AN = RES / "analyse"
NS = (20, 40, 80, 160)
METHODS = [  # même code couleur que la simulation (palette validée)
    ("rmt", "RMT : bord MP + Tracy-Widom (testé)", "#2a78d6", "o"),
    ("perm", "Permutations (analyse parallèle)", "#eb6834", "s"),
    ("mp", "Bord MP seul (σ² = 1)", "#1baf7a", "^"),
    ("pca10", "ACP à 10 axes (comparateur principal)", "#eda100", "D"),
    ("var80", "80 % de variance", "#e87ba4", "v"),
    ("kaiser", "Kaiser (λ > 1)", "#008300", "P"),
]
LABEL = {k: l for k, l, _, _ in METHODS} | {"rmt_a01": "RMT, α = 0,01"}
INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"


def fr(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


def style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def figure(main: pd.DataFrame, s5: pd.DataFrame, path: Path):
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.3), facecolor=SURFACE)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.78, bottom=0.27, wspace=0.25)
    ax = axes[0]
    style(ax)
    med = main.groupby(["methode", "n"]).D.median()
    xs = np.arange(len(NS))
    for key, label, color, marker in METHODS:
        ax.plot(xs, [med[(key, n)] for n in NS], color=color, lw=2, marker=marker, ms=8,
                markeredgecolor=SURFACE, markeredgewidth=1.5, label=label)
    ax.set_xticks(xs, [str(n) for n in NS])
    ax.set_xlabel("Biopsies tirées de la cohorte 331 (n)", color=INK, fontsize=10)
    ax.set_ylabel("Accord D avec la cohorte 558 (médiane)", color=INK, fontsize=10)
    ax.set_title("A. Critère principal", loc="left", fontsize=11, color=INK)
    ax.text(xs[0], med[("perm", 160)], "Permutations et bord MP seul :\ncourbes confondues",
            ha="left", va="top", fontsize=8.5, color=INK2)

    ax = axes[1]
    style(ax)
    ax.plot([0, 1], [0, 1], color=INK2, lw=1)
    ax.text(0.50, 0.80, "diagonale : prédit = observé", ha="right", fontsize=9, color=INK2)
    top = s5.axe_331 <= 37
    ax.scatter(s5.loc[~top, "recouvrement_predit"], s5.loc[~top, "recouvrement_observe"], s=18,
               color="#9ec5f4", edgecolor=SURFACE, linewidth=0.5, label="Axes RMT 38 à 145")
    ax.scatter(s5.loc[top, "recouvrement_predit"], s5.loc[top, "recouvrement_observe"], s=26,
               color="#2a78d6", edgecolor=SURFACE, linewidth=0.6, label="Axes RMT 1 à 37")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Recouvrement prédit ψ²(331) × ψ²(558)", color=INK, fontsize=10)
    ax.set_ylabel("Recouvrement observé avec la 558", color=INK, fontsize=10)
    ax.set_title("B. H3 : fiabilité prédite des axes", loc="left", fontsize=11, color=INK)

    fig.text(0.07, 0.94, "GSE124897 : résultats de l'analyse préenregistrée (osf.io/6htjn)",
             fontsize=12.5, color=INK, weight="bold")
    fig.text(0.07, 0.895, "Données réelles publiques. 200 tirages par taille ; référence : 37 axes "
             "de la cohorte 558 (analyse parallèle).", fontsize=9.5, color=INK2)
    fig.text(0.07, 0.855, "H1 non soutenue (RMT > ACP-10 à n = 20 et 40 seulement) ; H2 soutenue ; "
             "H3 : fiabilité surestimée.", fontsize=9.5, color=INK2)
    h1, l1 = axes[0].get_legend_handles_labels()
    h2, l2 = axes[1].get_legend_handles_labels()
    fig.legend(h1 + h2, l1 + l2, loc="lower center", bbox_to_anchor=(0.5, 0.0), ncol=3,
               frameon=False, fontsize=8.5, labelcolor=INK)
    fig.savefig(path, dpi=200, facecolor=SURFACE)
    plt.close(fig)


def main():
    summ = json.loads((AN / "resume.json").read_text())
    v = summ["verdicts"]
    main_ = pd.read_csv(AN / "tirages_principale.csv")
    s2 = pd.read_csv(AN / "S2_stabilite.csv")
    s3 = pd.read_csv(AN / "S3_permutees.csv")
    s5 = pd.read_csv(AN / "S5_H3_recouvrement.csv")
    ref = summ["variantes"]["principale"]["reference"]
    figure(main_, s5, RES / "RESULTATS_fig.png")

    order = ["rmt", "rmt_a01", "perm", "mp", "pca10", "var80", "kaiser"]
    L = ["# GSE124897 — résultats de l'analyse PRÉENREGISTRÉE",
         "",
         "> Plan enregistré : https://osf.io/6htjn (2026-11-26 12:32 UTC). Code : étiquette `prereg-v1`",
         "> + scripts `rmt_gse124897_03`–`05`. Généré par `scripts/rmt_gse124897_05_report.py` : ne pas éditer.",
         "> Données publiques GEO ; cohorte 558 ouverte après vérification de son empreinte.",
         "",
         "## Verdicts (critères de la section 6 du préenregistrement)",
         "",
         "| Hypothèse | Résultat | Détail |",
         "|---|---|---|"]
    h1 = v["H1"]
    L.append("| **H1** RMT > ACP-10 (n = 20, 40, 80) | **" + ("soutenue" if h1["soutenue"] else "NON soutenue")
             + "** | " + " ; ".join(f"n = {n} : RMT meilleur dans {fr(100 * h1[str(n)]['part_RMT_superieur'], 1)} % "
                                    f"des tirages, différence médiane {fr(h1[str(n)]['mediane_difference'], 4)}"
                                    for n in (20, 40, 80)) + " |")
    h2 = v["H2"]
    L.append("| **H2** faux axes sur données permutées ≤ 8 % | **" + ("soutenue" if h2["soutenue"] else "NON soutenue")
             + "** | " + " ; ".join(f"n = {n} : {fr(100 * h2[str(n)]['part_tirages_faux_axe'], 1)} %" for n in NS) + " |")
    L.append(f"| **H3** (exploratoire) fiabilité prédite | décrite | {v['H3']['axes']} axes RMT ; écart absolu moyen "
             f"prédit/observé {fr(v['H3']['ecart_absolu_moyen'])} |")
    L += ["", f"Référence (cohorte 558, {ref['n']} biopsies, {ref['p']} gènes) : K_ref = {ref['K_ref_analyse_parallele']} "
          f"axes par analyse parallèle (plan) ; RMT y retient {ref['K_ref_rmt']} axes (variance du bruit "
          f"réestimée à {fr(ref['sigma2_rmt'])}).", "",
          "## Critère principal D et nombre d'axes (médianes sur 200 tirages)", "",
          "| méthode | " + " | ".join(f"k (n = {n})" for n in NS) + " | " + " | ".join(f"D (n = {n})" for n in NS) + " |",
          "|---|" + "---|" * 8]
    med = main_.groupby(["methode", "n"])[["k", "D"]].median()
    for m in order:
        L.append(f"| {LABEL.get(m, m)} | " + " | ".join(f"{med.loc[(m, n), 'k']:.0f}" for n in NS) + " | "
                 + " | ".join(fr(med.loc[(m, n), "D"]) for n in NS) + " |")
    L += ["", "## Analyses de vérification (préenregistrées) : RMT meilleur que l'ACP-10, % des tirages", "",
          "| variante | n = 20 | n = 40 | n = 80 | n = 160 |", "|---|---|---|---|---|"]
    for name in ("principale", "geo", "exclusion", "top5000"):
        t = pd.read_csv(AN / f"tirages_{name}.csv").pivot_table(index=["n", "tirage"], columns="methode", values="D")
        L.append(f"| {name} | " + " | ".join(fr(100 * (t.loc[n].rmt > t.loc[n].pca10).mean(), 1) + " %" for n in NS) + " |")
    L += ["", "Avec la référence choisie par RMT (K_ref = " + str(ref["K_ref_rmt"]) + ") : voir colonne `D_refRMT` des fichiers de tirages.",
          "", "## S2 stabilité entre tirages (D médian entre paires) et S3 faux axes sur données permutées (%)", "",
          "| méthode | " + " | ".join(f"S2 n = {n}" for n in NS) + " | " + " | ".join(f"S3 n = {n}" for n in NS) + " |",
          "|---|" + "---|" * 8]
    st = s2.groupby(["methode", "n"]).D_stabilite.median()
    fp = s3.assign(f=s3.k > 0).groupby(["methode", "n"]).f.mean()
    for m in order:
        L.append(f"| {LABEL.get(m, m)} | " + " | ".join(fr(st[(m, n)]) for n in NS) + " | "
                 + " | ".join(fr(100 * fp[(m, n)], 1) for n in NS) + " |")
    L += ["", "## S5 / H3 : recouvrement observé vs prédit (axes RMT de la cohorte 331 entière)", "",
          "| axes | recouvrement observé (moy.) | prédit (moy.) |", "|---|---|---|"]
    for lo, hi in [(1, 10), (11, 37), (38, int(s5.axe_331.max()))]:
        d = s5[(s5.axe_331 >= lo) & (s5.axe_331 <= hi)]
        L.append(f"| {lo}–{hi} | {fr(d.recouvrement_observe.mean())} | {fr(d.recouvrement_predit.mean())} |")
    L += ["", "## Écart déclaré au plan", "",
          "- α = 0,01 appliqué à RMT seulement : avec 99 permutations, « p < 0,01 » est impossible pour l'analyse parallèle.",
          "", "## Lecture (à reprendre dans l'article)", "",
          "- Contre du bruit pur, le test de Tracy-Widom tient son niveau (H2). Le bord MP seul, sans test, dépasse 8 % à n = 80.",
          "- Sur ces données réelles, le modèle « quelques axes + bruit homogène » ne tient pas : la variance du bruit est",
          "  réestimée très bas et RMT retient de nombreux axes faibles (médiane 16 à 89 selon n ; 145 sur la 331 entière).",
          "- RMT ne fait mieux que l'ACP-10 qu'à n = 20 et 40, avec un faible écart ; au-delà, les permutations et le bord MP",
          "  seul (σ² = 1) donnent le meilleur accord avec la cohorte 558.",
          "- La fiabilité prédite des axes (H3) est très optimiste sur données réelles : les axes individuels se répliquent",
          "  mal d'une cohorte à l'autre, même quand le sous-espace se réplique.",
          "- Limite du critère D : avec une référence de 37 axes, D favorise mécaniquement les méthodes qui retiennent",
          "  plus d'axes aux petits n.", ""]
    (RES / "RESULTATS.md").write_text("\n".join(L), encoding="utf-8")
    print("écrit : results/rmt_gse124897/RESULTATS.md et RESULTATS_fig.png")


if __name__ == "__main__":
    main()
