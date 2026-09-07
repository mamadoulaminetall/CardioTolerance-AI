"""03 — Méta-analyse diagnostique dd-cfDNA (rejet aigu, greffe cardiaque).

Cette version est **exécutable**. Elle attend un fichier d'extraction 2x2 :

    data/ddcfdna_2x2.csv   colonnes : study_id, year, country, threshold, tp, fp, fn, tn

à remplir à partir des **textes intégraux** (accès bibliothèque / institutionnel requis —
les abstracts ne donnent pas toujours les effectifs bruts). Tant que ce fichier n'existe
pas, le script s'arrête proprement en expliquant ce qui manque : il ne fabrique aucune
donnée.

Quand le fichier existe, le script produit :
  - pooling par effets aleatoires (DerSimonian-Laird) de la sensibilite et de la
    specificite (echelle logit), avec I^2 et intervalle de prediction ;
  - un nuage sensibilite vs (1 - specificite) dans l'espace ROC ;
  - meta-analysis/figures/forest_sens.png, forest_spec.png, roc_space.png ;
  - mise a jour de la ligne 'Re-analyse CardioTolerance-AI' de data/meta_estimates.csv.

NB : un vrai modele bivarie (Reitsma) estimerait aussi la correlation sens/spec. Le
pooling separe logit ci-dessous en est une approximation transparente et sans dependance
lourde ; a remplacer par `statsmodels`/`metadta` si disponible et si k le justifie.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
IN = ROOT / "data" / "ddcfdna_2x2.csv"
FIGDIR = ROOT / "meta-analysis" / "figures"
ESTIMATES = ROOT / "data" / "meta_estimates.csv"

CC = 0.5  # correction de continuite pour les cellules nulles


def logit(p: float) -> float:
    return float(np.log(p / (1 - p)))


def inv_logit(x: float) -> float:
    return float(1 / (1 + np.exp(-x)))


def dersimonian_laird(y: np.ndarray, v: np.ndarray) -> dict:
    """Pooling a effets aleatoires sur l'echelle logit."""
    w_fixed = 1 / v
    y_fixed = np.sum(w_fixed * y) / np.sum(w_fixed)
    q = float(np.sum(w_fixed * (y - y_fixed) ** 2))
    k = len(y)
    c = np.sum(w_fixed) - np.sum(w_fixed ** 2) / np.sum(w_fixed)
    tau2 = max(0.0, (q - (k - 1)) / c) if c > 0 else 0.0
    w = 1 / (v + tau2)
    mu = float(np.sum(w * y) / np.sum(w))
    se = float(np.sqrt(1 / np.sum(w)))
    i2 = max(0.0, (q - (k - 1)) / q) * 100 if q > 0 else 0.0
    # intervalle de prediction (t de Student, k-2 ddl)
    from scipy import stats

    tcrit = stats.t.ppf(0.975, max(1, k - 2))
    pi = (mu - tcrit * np.sqrt(se ** 2 + tau2), mu + tcrit * np.sqrt(se ** 2 + tau2))
    return dict(mu=mu, se=se, tau2=tau2, q=q, i2=i2, k=k,
               ci=(mu - 1.96 * se, mu + 1.96 * se), pi=pi)


def main() -> None:
    if not IN.exists():
        template = "study_id,year,country,threshold,tp,fp,fn,tn\n" \
                   "S01-KHUSH-2019,2019,USA,>=0.15%,,,,\n" \
                   "S02-ABSQUANT-2023,2023,nd,0.1%,,,,\n" \
                   "S03-FREEDNA-CAR-2025,2025,Espagne,0.10%,,,,\n"
        sys.exit(
            "STOP — fichier d'extraction absent : data/ddcfdna_2x2.csv\n\n"
            "A produire a partir des TEXTES INTEGRAUX (les abstracts ne suffisent pas pour\n"
            "les effectifs bruts tp/fp/fn/tn). Modele de fichier a creer :\n\n"
            + template +
            "\nUne fois rempli (une ligne par etude, cellules 2x2 completes), relancer :\n"
            "    python scripts/03_meta_analysis.py\n"
        )

    FIGDIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(IN)
    need = {"study_id", "tp", "fp", "fn", "tn"}
    if not need.issubset(df.columns):
        sys.exit(f"Colonnes manquantes dans {IN.name}: {need - set(df.columns)}")
    df = df.dropna(subset=["tp", "fp", "fn", "tn"]).copy()
    if len(df) < 3:
        sys.exit(f"Seulement {len(df)} etudes avec 2x2 complet — insuffisant pour un pooling (min 3).")

    for c in ["tp", "fp", "fn", "tn"]:
        df[c] = df[c].astype(float)
    zero = (df[["tp", "fp", "fn", "tn"]] == 0).any(axis=1)
    df.loc[zero, ["tp", "fp", "fn", "tn"]] += CC

    df["sens"] = df.tp / (df.tp + df.fn)
    df["spec"] = df.tn / (df.tn + df.fp)
    df["y_sens"] = df.sens.map(logit)
    df["v_sens"] = 1 / df.tp + 1 / df.fn
    df["y_spec"] = df.spec.map(logit)
    df["v_spec"] = 1 / df.tn + 1 / df.fp

    rs = dersimonian_laird(df.y_sens.values, df.v_sens.values)
    rp = dersimonian_laird(df.y_spec.values, df.v_spec.values)

    def fmt(r):
        return (f"{inv_logit(r['mu'])*100:.0f}% "
                f"(IC95 {inv_logit(r['ci'][0])*100:.0f}-{inv_logit(r['ci'][1])*100:.0f} ; "
                f"IP {inv_logit(r['pi'][0])*100:.0f}-{inv_logit(r['pi'][1])*100:.0f} ; I2={r['i2']:.0f}%)")

    sens_str, spec_str = fmt(rs), fmt(rp)
    print(f"k = {len(df)} etudes")
    print("Sensibilite poolee :", sens_str)
    print("Specificite poolee :", spec_str)

    # --- figures ---
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ACC, MINT = "#8b5cf6", "#34d399"

    def forest(col_y, col_v, pooled, title, fname, color):
        fig, ax = plt.subplots(figsize=(7, 0.5 * len(df) + 2))
        for i, (_, r) in enumerate(df.iterrows()):
            p = inv_logit(r[col_y])
            lo = inv_logit(r[col_y] - 1.96 * np.sqrt(r[col_v]))
            hi = inv_logit(r[col_y] + 1.96 * np.sqrt(r[col_v]))
            ax.plot([lo, hi], [i, i], color=color)
            ax.plot(p, i, "s", color=color)
        ax.axvline(inv_logit(pooled["mu"]), color="#888", ls="--")
        ax.set_yticks(range(len(df)))
        ax.set_yticklabels(df.study_id, fontsize=8)
        ax.set_xlim(0, 1)
        ax.set_xlabel(title)
        ax.set_title(f"{title} — poolee {inv_logit(pooled['mu'])*100:.0f}% (I2={pooled['i2']:.0f}%)", fontsize=10)
        fig.tight_layout()
        fig.savefig(FIGDIR / fname, dpi=140)
        plt.close(fig)

    forest("y_sens", "v_sens", rs, "Sensibilite", "forest_sens.png", ACC)
    forest("y_spec", "v_spec", rp, "Specificite", "forest_spec.png", MINT)

    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.scatter(1 - df.spec, df.sens, s=40, color=ACC, zorder=3)
    ax.scatter(1 - inv_logit(rp["mu"]), inv_logit(rs["mu"]), s=120, marker="*", color="#111", zorder=4,
               label="point poole")
    for _, r in df.iterrows():
        ax.annotate(r.study_id, (1 - r.spec, r.sens), fontsize=7, xytext=(3, 3), textcoords="offset points")
    ax.plot([0, 1], [0, 1], color="#ccc", lw=1)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xlabel("1 - specificite"); ax.set_ylabel("sensibilite")
    ax.set_title("Espace ROC — dd-cfDNA / rejet aigu cardiaque")
    ax.legend()
    fig.tight_layout(); fig.savefig(FIGDIR / "roc_space.png", dpi=140)
    plt.close(fig)

    # --- maj meta_estimates.csv ---
    est = pd.read_csv(ESTIMATES)
    mask = est["analysis"].str.contains("Re-analyse CardioTolerance-AI", na=False)
    if mask.any():
        j = est.index[mask][0]
        est.loc[j, "k_studies"] = len(df)
        est.loc[j, "pooled_sensitivity"] = sens_str
        est.loc[j, "pooled_specificity"] = spec_str
        est.loc[j, "pooled_auc"] = "cf. espace ROC (HSROC a ajouter)"
        est.loc[j, "i2"] = f"sens {rs['i2']:.0f}% / spec {rp['i2']:.0f}%"
        est.loc[j, "status"] = f"calcule le {pd.Timestamp.today().date()} (pooling logit DL)"
        est.to_csv(ESTIMATES, index=False)
        print("meta_estimates.csv mis a jour (ligne re-analyse).")

    print("Figures :", *(p.name for p in sorted(FIGDIR.glob("*.png"))))


if __name__ == "__main__":
    main()
