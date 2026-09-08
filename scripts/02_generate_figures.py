"""02 — Figures pour l'app et le dossier.

Génère à partir des données seed :
  figures/fig_scoring_radar.png    — radar des 5 équipes françaises (6 axes /10)
  figures/fig_scoring_bars.png     — total pondéré /70, trié
  figures/fig_ddcfdna_landscape.png— sens/spéc des études dd-cfDNA + MA publiée
  figures/fig_prisma_template.png  — diagramme PRISMA (compteurs réels + étapes à remplir)

Règles de mise en page (feedback utilisateur, sept. 2026) :
  - aucun texte qui se superpose (titre vs ticks vs légende) ;
  - légende entièrement dans le canvas, hors zone de tracé, libellés courts ;
  - légendes/notes via fig.text avec marge réservée, jamais de ax.text qui déborde.

Aucune donnée inventée : les figures reflètent strictement data/*.csv.

Usage : python scripts/02_generate_figures.py
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MADIR = ROOT / "meta-analysis" / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

ACCENT = "#8b5cf6"
MINT = "#34d399"
INK = "#10151f"
SERIES = ["#6d28d9", "#0ea5e9", "#16a34a", "#dc2626", "#d97706"]
plt.rcParams.update({
    "font.size": 10,
    "axes.edgecolor": "#c9cbd6",
    "savefig.dpi": 140,
    "figure.facecolor": "white",
})

AXES = [
    ("score_scientifique", "Science"),
    ("acces_donnees", "Accès\ndonnées"),
    ("expertise_tx_cardiaque", "Tx\ncardiaque"),
    ("expertise_immunologie", "Immuno"),
    ("compat_ia_bioinfo", "IA /\nbioinfo"),
    ("potentiel_collaboration", "Collab."),
]

# libellés courts et stables pour les légendes (jamais tronqués)
SHORT = {
    "PTG-PARCC": "Paris Transplant Group (Loupy/Coutance)",
    "PITIE-HTX": "Pitié-Salpêtrière HTx (Coutance)",
    "CR2TI-NANTES": "CR2TI Nantes (Brouard)",
    "CIRI-NOPAB-LYON": "CIRI Lyon (Thaunat)",
    "APHM-MARSEILLE": "C2VN Marseille (Paul)",
}


def label_for(row) -> str:
    return SHORT.get(row["team_id"], str(row.get("team_label", row["team_id"]))[:38])


def scoring_radar(df: pd.DataFrame) -> None:
    cats = [a[1] for a in AXES]
    ang = np.linspace(0, 2 * np.pi, len(cats), endpoint=False).tolist()
    ang += ang[:1]

    fig = plt.figure(figsize=(8.4, 8.6))
    # zone de tracé : haut de la figure ; bas réservé à la légende
    ax = fig.add_axes([0.13, 0.30, 0.74, 0.60], polar=True)

    for i, (_, r) in enumerate(df.iterrows()):
        vals = [float(r[a[0]]) for a in AXES]
        vals += vals[:1]
        c = SERIES[i % len(SERIES)]
        ax.plot(ang, vals, linewidth=1.8, color=c, label=label_for(r))
        ax.fill(ang, vals, color=c, alpha=0.07)

    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(cats, fontsize=9)
    ax.tick_params(axis="x", pad=12)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=7.5, color="#888")
    ax.set_rlabel_position(198)  # secteur vide (entre Immuno et IA)

    fig.text(0.5, 0.965, "Scoring des équipes françaises — 6 axes notés /10",
             ha="center", va="top", fontsize=13, weight="bold")
    fig.legend(loc="lower center", bbox_to_anchor=(0.5, 0.02), ncol=1,
               fontsize=8.5, frameon=False, handlelength=1.6, labelspacing=0.55)
    fig.savefig(FIG / "fig_scoring_radar.png")
    plt.close(fig)


def scoring_bars(df: pd.DataFrame) -> None:
    d = df.sort_values("total_pondere")
    labels = [label_for(r) for _, r in d.iterrows()]
    fig, ax = plt.subplots(figsize=(9.2, 3.6))
    fig.subplots_adjust(left=0.34, right=0.97, top=0.84, bottom=0.16)
    y = np.arange(len(d))
    ax.barh(y, d["total_pondere"], color=ACCENT, height=0.62)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9)
    xmax = float(d["total_max"].max()) if "total_max" in d else 70
    ax.set_xlim(0, xmax + 4)
    ax.set_xlabel("Score pondéré /70")
    for yi, v in zip(y, d["total_pondere"]):
        ax.text(v + 0.8, yi, f"{v:.1f}", va="center", fontsize=9)
    ax.set_title("Classement des collaborations françaises", loc="left", pad=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(FIG / "fig_scoring_bars.png")
    plt.close(fig)


def ddcfdna_landscape(reg: pd.DataFrame, meta: pd.DataFrame) -> None:
    def pct(x):
        try:
            return float(str(x).split("%")[0].replace(",", ".").strip())
        except Exception:
            return np.nan

    rows = []
    for _, r in reg.iterrows():
        if "dd-cfDNA" in str(r.get("other_biomarkers", "")) and str(r["study_id"]).startswith("S0"):
            sid = str(r["study_id"])
            short = sid.split("-", 1)[1].rsplit("-", 1)[0] if "-" in sid else sid
            rows.append((short, pct(r["sensitivity"]), pct(r["specificity"])))
    ma = meta[meta["analysis"].str.contains("MA publiee", na=False)]
    if not ma.empty:
        rows.append(("MA 2025\n(k=10)", pct(ma.iloc[0]["pooled_sensitivity"]),
                     pct(ma.iloc[0]["pooled_specificity"])))
    if not rows:
        return
    labels, sens, spec = zip(*rows)
    x = np.arange(len(labels))
    w = 0.38
    fig, ax = plt.subplots(figsize=(9.4, 4.2))
    fig.subplots_adjust(left=0.09, right=0.97, top=0.82, bottom=0.30)
    b1 = ax.bar(x - w / 2, sens, w, label="Sensibilité %", color=ACCENT)
    b2 = ax.bar(x + w / 2, spec, w, label="Spécificité %", color=MINT)
    for bars in (b1, b2):
        for rect in bars:
            h = rect.get_height()
            if not np.isnan(h):
                ax.text(rect.get_x() + rect.get_width() / 2, h + 1.5, f"{h:.0f}",
                        ha="center", va="bottom", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylim(0, 105)
    ax.set_ylabel("%")
    ax.set_title("dd-cfDNA — rejet aigu cardiaque : précision diagnostique rapportée",
                 loc="left", pad=10)
    ax.legend(loc="upper right", fontsize=8.5, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.09, 0.06,
             "Valeurs extraites d'abstracts, à confirmer sur texte intégral. "
             "S04/S05 : sens/spéc non rapportées. FreeDNA-CAR (S03) : AUC prospective 0,60.",
             fontsize=7.5, color="#666")
    fig.savefig(FIG / "fig_ddcfdna_landscape.png")
    plt.close(fig)


def prisma_template() -> None:
    corpus = MADIR / "lit_corpus.csv"
    qlog = MADIR / "query_log.csv"
    n_dedup = "à remplir"
    n_ident = "à remplir"
    if corpus.exists():
        n_dedup = f"{len(pd.read_csv(corpus))}"
    if qlog.exists():
        ql = pd.read_csv(qlog)
        ql = ql[ql["count"].astype(str).str.isdigit()]
        if len(ql):
            n_ident = f"{int(ql['count'].astype(int).sum())} (8 requêtes, {ql['date'].iloc[0]})"

    steps = [
        ("Records identifiés — PubMed, 8 requêtes journalisées", f"n = {n_ident}"),
        ("Après déduplication (PMID)", f"n = {n_dedup}"),
        ("Screening titre / résumé", "exclus : n = à remplir"),
        ("Texte intégral évalué", "exclus : n = à remplir (avec motifs)"),
        ("Études incluses — synthèse qualitative", "n = à remplir"),
        ("Études incluses — méta-analyse dd-cfDNA", "n ≈ 10 (MA 2025) — à confirmer"),
    ]

    fig, ax = plt.subplots(figsize=(7.6, 9.2))
    fig.subplots_adjust(left=0.04, right=0.96, top=0.9, bottom=0.05)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("Diagramme PRISMA — compteurs réels + étapes à compléter (Phase 2)",
                 fontsize=12, pad=16)

    n = len(steps)
    slot = 0.92 / n            # hauteur par étape (boîte + flèche)
    box_h = slot * 0.62
    for i, (title, note) in enumerate(steps):
        top = 0.95 - i * slot
        ax.add_patch(plt.Rectangle((0.08, top - box_h), 0.84, box_h,
                                   facecolor="#f2f1f6", edgecolor=ACCENT, linewidth=1.2))
        ax.text(0.5, top - box_h * 0.36, textwrap.fill(title, 46),
                ha="center", va="center", fontsize=9.5, color=INK)
        ax.text(0.5, top - box_h * 0.80, note,
                ha="center", va="center", fontsize=8, color="#6b6b6b")
        if i < n - 1:
            ax.annotate("", xy=(0.5, top - slot + 0.002),
                        xytext=(0.5, top - box_h - 0.002),
                        arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=1.4))
    fig.savefig(FIG / "fig_prisma_template.png")
    plt.close(fig)


def main() -> None:
    teams = pd.read_csv(DATA / "french_teams_scoring.csv")
    reg = pd.read_csv(DATA / "studies_registry.csv")
    meta = pd.read_csv(DATA / "meta_estimates.csv")
    scoring_radar(teams)
    scoring_bars(teams)
    ddcfdna_landscape(reg, meta)
    prisma_template()
    print("Figures écrites dans", FIG)
    for p in sorted(FIG.glob("*.png")):
        print("  ", p.name)


if __name__ == "__main__":
    main()
