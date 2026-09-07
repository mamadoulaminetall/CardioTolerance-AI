"""02 — Figures pour l'app et le dossier.

Génère à partir des données seed :
  figures/fig_scoring_radar.png    — radar des 5 équipes françaises (6 axes /10)
  figures/fig_scoring_bars.png     — total pondéré /70, trié
  figures/fig_ddcfdna_landscape.png— sens/spéc/AUC des études dd-cfDNA + MA publiée
  figures/fig_prisma_template.png  — gabarit de diagramme PRISMA (compteurs = "à remplir")

Aucune donnée inventée : les figures reflètent strictement data/*.csv. Le PRISMA est un
gabarit tant que la recherche formelle (Phase 2) n'a pas produit les comptes.

Usage : python scripts/02_generate_figures.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

ACCENT = "#8b5cf6"
MINT = "#34d399"
INK = "#10151f"
plt.rcParams.update({"font.size": 10, "axes.edgecolor": "#c9cbd6", "savefig.dpi": 140})

AXES = [
    ("score_scientifique", "Science"),
    ("acces_donnees", "Accès données"),
    ("expertise_tx_cardiaque", "Tx cardiaque"),
    ("expertise_immunologie", "Immuno"),
    ("compat_ia_bioinfo", "IA / bioinfo"),
    ("potentiel_collaboration", "Collab."),
]


def short(label: str) -> str:
    return label.split(" - ")[0].split(" (")[0][:34]


def scoring_radar(df: pd.DataFrame) -> None:
    cats = [a[1] for a in AXES]
    ang = np.linspace(0, 2 * np.pi, len(cats), endpoint=False).tolist()
    ang += ang[:1]
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    for _, r in df.iterrows():
        vals = [r[a[0]] for a in AXES]
        vals += vals[:1]
        ax.plot(ang, vals, linewidth=1.6, label=short(str(r.get("team_label", r["team_id"]))))
        ax.fill(ang, vals, alpha=0.08)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(cats)
    ax.set_ylim(0, 10)
    ax.set_title("Scoring des équipes françaises (6 axes /10)", pad=18)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.12), fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig_scoring_radar.png", bbox_inches="tight")
    plt.close(fig)


def scoring_bars(df: pd.DataFrame) -> None:
    d = df.sort_values("total_pondere")
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.barh([short(str(x)) for x in d.get("team_label", d["team_id"])],
            d["total_pondere"], color=ACCENT)
    ax.set_xlabel("Score pondéré /70")
    ax.set_xlim(0, float(d["total_max"].max()) if "total_max" in d else 70)
    for y, v in enumerate(d["total_pondere"]):
        ax.text(v + 0.6, y, f"{v:.1f}", va="center", fontsize=9)
    ax.set_title("Classement des collaborations françaises", loc="left")
    fig.tight_layout()
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
            rows.append((r["study_id"].replace("-", "\n", 1), pct(r["sensitivity"]), pct(r["specificity"])))
    ma = meta[meta["analysis"].str.contains("MA publiee", na=False)]
    if not ma.empty:
        rows.append(("MA 2025\n(10 études)", pct(ma.iloc[0]["pooled_sensitivity"]), pct(ma.iloc[0]["pooled_specificity"])))
    if not rows:
        return
    labels, sens, spec = zip(*rows)
    x = np.arange(len(labels))
    w = 0.38
    fig, ax = plt.subplots(figsize=(9, 3.6))
    ax.bar(x - w / 2, sens, w, label="Sensibilité %", color=ACCENT)
    ax.bar(x + w / 2, spec, w, label="Spécificité %", color=MINT)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylim(0, 100)
    ax.set_title("dd-cfDNA pour le rejet aigu cardiaque — précision diagnostique rapportée", loc="left")
    ax.legend()
    ax.text(0.0, -0.32, "Valeurs extraites d'abstracts (à confirmer sur texte intégral). "
            "FreeDNA-CAR : AUC prospective 0,60.", transform=ax.transAxes, fontsize=7.5, color="#555")
    fig.tight_layout()
    fig.savefig(FIG / "fig_ddcfdna_landscape.png")
    plt.close(fig)


def prisma_template() -> None:
    fig, ax = plt.subplots(figsize=(6.5, 8))
    ax.axis("off")
    steps = [
        ("Records identifiés\n(PubMed + Europe PMC + registres)", "n = à remplir"),
        ("Après déduplication", "n = à remplir"),
        ("Screening titre/résumé", "exclus : n = à remplir"),
        ("Texte intégral évalué", "exclus : n = à remplir (motifs)"),
        ("Études incluses (synthèse)", "n = à remplir"),
        ("Études incluses (méta-analyse dd-cfDNA)", "n ≈ 10 (cf. MA 2025) — à confirmer"),
    ]
    y = 0.94
    for title, note in steps:
        ax.add_patch(plt.Rectangle((0.1, y - 0.1), 0.8, 0.09, fill=True,
                                   facecolor="#f2f1f6", edgecolor=ACCENT))
        ax.text(0.5, y - 0.037, title, ha="center", va="center", fontsize=9, color=INK)
        ax.text(0.5, y - 0.075, note, ha="center", va="center", fontsize=7.5, color="#777")
        if y > 0.3:
            ax.annotate("", xy=(0.5, y - 0.11), xytext=(0.5, y - 0.1 + 0.001),
                        arrowprops=dict(arrowstyle="-|>", color=ACCENT))
        y -= 0.155
    ax.set_title("Diagramme PRISMA — gabarit (Phase 2)", fontsize=11)
    fig.savefig(FIG / "fig_prisma_template.png", bbox_inches="tight")
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
