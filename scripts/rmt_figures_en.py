"""Manuscript figures (English) for the RMT study — preregistration https://osf.io/6htjn.

Built only from existing outputs (no new analysis):
  results/rmt_simulation/*.csv           -> Fig 1, Fig 2, Fig S1 (one simulated draw, same seed)
  results/rmt_gse124897/analyse/*.csv    -> Fig 3
  results/rmt_gse2596 (recomputed view)  -> Fig 4 (exploratory)
  results/rmt_gse124897/QC_*.csv         -> Fig S2
Journal style: no title inside the image, panel letters, English labels, decimal points.
Captions go in the manuscript. Outputs: manuscript_rmt/figures/*.png (300 dpi) and *.pdf.

Usage : python -I scripts/rmt_figures_en.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rmt_denoise as rmt  # noqa: E402
import rmt_simulation as sim  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "manuscript_rmt" / "figures"
SIMD = ROOT / "results" / "rmt_simulation"
AN = ROOT / "results" / "rmt_gse124897" / "analyse"
QC = ROOT / "results" / "rmt_gse124897"

INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
METHODS = [
    ("rmt", "RMT: MP edge + Tracy–Widom", "#2a78d6", "o"),
    ("perm", "Permutation (parallel analysis)", "#eb6834", "s"),
    ("mp", "MP edge alone (σ² = 1)", "#1baf7a", "^"),
    ("pca10", "PCA, 10 fixed components", "#eda100", "D"),
    ("var80", "80% cumulative variance", "#e87ba4", "v"),
    ("kaiser", "Kaiser rule (λ > 1)", "#008300", "P"),
]
FACTOR_COLORS = ("#2a78d6", "#eb6834", "#1baf7a")
plt.rcParams.update({"font.size": 9, "axes.labelsize": 10})


def style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def panel(ax, letter, text):
    ax.set_title(f"$\\mathbf{{{letter}}}$   {text}", loc="left", fontsize=10.5, color=INK)


def new(figsize=(10.5, 4.9), bottom=0.25):
    fig, axes = plt.subplots(1, 2, figsize=figsize, facecolor=SURFACE)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.90, bottom=bottom, wspace=0.26)
    for a in axes:
        style(a)
    return fig, axes


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=300, facecolor=SURFACE)
    fig.savefig(OUT / f"{name}.pdf", facecolor=SURFACE)
    plt.close(fig)
    print("written:", (OUT / f"{name}.png").relative_to(ROOT))


def legend_below(fig, axes, ncol=3, y=0.0):
    h, l = [], []
    for a in axes:
        hh, ll = a.get_legend_handles_labels()
        for x, y_ in zip(hh, ll):
            if y_ not in l:
                h.append(x); l.append(y_)
    fig.legend(h, l, loc="lower center", bbox_to_anchor=(0.5, y), ncol=ncol, frameon=False,
               fontsize=8.5, labelcolor=INK)


# ---------------------------------------------------------------------------
def fig1():
    s = pd.read_csv(SIMD / "SIMULATION_resume.csv")
    fig, (a, b) = new()
    xs = np.arange(len(sim.NS))
    for key, label, color, marker in METHODS:
        key = {"pca10": "fixed10"}.get(key, key)  # nom utilisé dans la simulation
        d = s[(s.scenario == "signal") & (s.methode == key)].set_index("n").loc[list(sim.NS)]
        a.plot(xs, d.faux, color=color, lw=2, marker=marker, ms=7, markeredgecolor=SURFACE,
               markeredgewidth=1.3, label=label)
        if key in ("rmt", "perm", "mp"):
            d0 = s[(s.scenario == "bruit_pur") & (s.methode == key)].set_index("n").loc[list(sim.NS)]
            b.plot(xs, d0.pct_au_moins_un_faux, color=color, lw=2, marker=marker, ms=7,
                   markeredgecolor=SURFACE, markeredgewidth=1.3)
    a.text(xs[-1], 19, "RMT, permutation and MP edge alone:\n≈ 0 (curves overlap at the bottom)",
           ha="right", va="center", fontsize=8.5, color=INK2)
    for ax in (a, b):
        ax.set_xticks(xs, [str(n) for n in sim.NS])
        ax.set_xlabel("Number of samples (n)", color=INK)
    a.set_ylabel("Spurious components retained (mean)", color=INK)
    panel(a, "A", "Three hidden signatures (simulated data)")
    b.set_ylim(-0.6, 15)
    b.axhline(5, color=INK2, lw=1, ls=(0, (4, 3)))
    b.text(xs[-1], 5.3, "nominal 5%", ha="right", va="bottom", fontsize=8.5, color=INK2)
    b.text(xs[0], 14.6, "Fixed-10 PCA, 80% variance, Kaiser:\n100% of draws (off scale)", va="top",
           fontsize=8.5, color=INK2)
    b.set_ylabel("Draws with ≥ 1 spurious component (%)", color=INK)
    panel(b, "B", "Pure noise (negative control, simulated)")
    legend_below(fig, [a])
    save(fig, "Fig1_simulation_spurious_components")


def fig2():
    rel = pd.read_csv(SIMD / "SIMULATION_fiabilite.csv").dropna(subset=["facteur"])
    det = pd.read_csv(SIMD / "SIMULATION_detection.csv")
    ells = sim.ell_true()
    fig, (a, b) = new()
    a.plot([0, 1], [0, 1], color=INK2, lw=1)
    a.text(0.50, 0.82, "identity line", ha="right", fontsize=8.5, color=INK2)
    for j, m in enumerate(sim.SIZES):
        lab = f"Factor {j + 1} ({m} genes, ℓ = {ells[j]:g}; detectable from n ≈ {sim.n_threshold(ells[j])})"
        d = rel[rel.facteur == j + 1]
        a.scatter(d.cos2_predit, d.cos2_observe, s=16, color=FACTOR_COLORS[j], edgecolor=SURFACE,
                  linewidth=0.5, alpha=0.8, label=lab)
        dd = det[(det.methode == "rmt") & (det.facteur == j + 1)].set_index("n").loc[list(sim.NS)]
        b.plot(np.arange(len(sim.NS)), 100 * dd.taux_detection, color=FACTOR_COLORS[j], lw=2,
               marker="o", ms=7, markeredgecolor=SURFACE, markeredgewidth=1.3)
    a.set_xlim(0, 1); a.set_ylim(0, 1)
    a.set_xlabel("Predicted cos² (spiked model)", color=INK)
    a.set_ylabel("Observed cos² with the true factor", color=INK)
    panel(a, "A", "Reliability of gene loadings (simulated data)")
    b.set_xticks(range(len(sim.NS)), [str(n) for n in sim.NS])
    b.set_ylim(-4, 104)
    b.set_xlabel("Number of samples (n)", color=INK)
    b.set_ylabel("Factor detected by RMT (% of draws)", color=INK)
    panel(b, "B", "Detection versus cohort size (simulated)")
    legend_below(fig, [a], ncol=1, y=-0.01)
    fig.subplots_adjust(bottom=0.30)
    save(fig, "Fig2_simulation_reliability_detection")


def fig3():
    main = pd.read_csv(AN / "tirages_principale.csv")
    s5 = pd.read_csv(AN / "S5_H3_recouvrement.csv")
    ref = json.loads((AN / "resume.json").read_text())["variantes"]["principale"]["reference"]
    fig, (a, b) = new()
    med = main.groupby(["methode", "n"]).D.median()
    xs = np.arange(4)
    for key, label, color, marker in METHODS:
        a.plot(xs, [med[(key, n)] for n in (20, 40, 80, 160)], color=color, lw=2, marker=marker, ms=7,
               markeredgecolor=SURFACE, markeredgewidth=1.3, label=label)
    a.text(xs[0], med[("perm", 160)], "Permutation and MP edge alone:\ncurves overlap", va="top",
           fontsize=8.5, color=INK2)
    a.set_xticks(xs, ["20", "40", "80", "160"])
    a.set_xlabel("Biopsies drawn from cohort 331 (n)", color=INK)
    a.set_ylabel(f"Agreement D with cohort 558 (median)", color=INK)
    panel(a, "A", f"Primary outcome (reference: {ref['K_ref_analyse_parallele']} components)")
    b.plot([0, 1], [0, 1], color=INK2, lw=1)
    b.text(0.50, 0.82, "identity line", ha="right", fontsize=8.5, color=INK2)
    top = s5.axe_331 <= ref["K_ref_analyse_parallele"]
    b.scatter(s5.loc[~top, "recouvrement_predit"], s5.loc[~top, "recouvrement_observe"], s=16,
              color="#9ec5f4", edgecolor=SURFACE, linewidth=0.5,
              label=f"RMT components {ref['K_ref_analyse_parallele'] + 1}–{int(s5.axe_331.max())}")
    b.scatter(s5.loc[top, "recouvrement_predit"], s5.loc[top, "recouvrement_observe"], s=24,
              color="#2a78d6", edgecolor=SURFACE, linewidth=0.6,
              label=f"RMT components 1–{ref['K_ref_analyse_parallele']}")
    b.set_xlim(0, 1); b.set_ylim(0, 1)
    b.set_xlabel("Predicted overlap ψ²(331) × ψ²(558)", color=INK)
    b.set_ylabel("Observed overlap with cohort 558", color=INK)
    panel(b, "B", "H3: predicted reliability of components")
    legend_below(fig, [a, b])
    save(fig, "Fig3_GSE124897_preregistered_results")


def fig4():
    import rmt_gse2596_exploratory as ex
    table, ann, _ = ex.load()
    Xs, bio = ex.prepare(table, ann)
    res = rmt.denoise(Xs, n_keep=10)
    fig, (a, b) = new()
    eig = res.eigenvalues
    K = min(40, len(eig)); kk = min(res.k, K)
    a.bar(np.arange(1, K + 1), eig[:K], color="#9ec5f4", edgecolor=SURFACE, linewidth=1.0, label="Not retained")
    a.bar(np.arange(1, kk + 1), eig[:kk], color="#2a78d6", edgecolor=SURFACE, linewidth=1.0,
          label=f"Retained by RMT ({res.k})")
    a.axhline(res.lambda_plus, color=INK2, lw=1.2, label=f"MP edge, re-estimated noise (σ² = {res.sigma2:.2f})")
    a.axhline(rmt.mp_edges(res.n_eff, res.p, 1.0)[1], color=INK, lw=1.2, ls=(0, (4, 3)), label="MP edge, σ² = 1")
    a.set_xlabel("Component rank", color=INK)
    a.set_ylabel("Eigenvalue", color=INK)
    panel(a, "A", f"Spectrum ({res.n} biopsies, {res.p} spots)")
    y = bio.loc[Xs.index, "groupe"].values
    colors = {"non-rejection": "#2a78d6", "acute rejection": "#eb6834", "pre-rejection": "#1baf7a"}
    names = {"non-rejection": "No rejection", "acute rejection": "Acute rejection", "pre-rejection": "Pre-rejection"}
    rng = np.random.default_rng(0)
    for j in range(3):
        for g, off in (("non-rejection", -0.2), ("acute rejection", 0.0), ("pre-rejection", 0.2)):
            sc = res.scores[y == g, j] / res.singular_values[j]
            b.scatter(j + 1 + off + rng.uniform(-0.05, 0.05, len(sc)), sc, s=22, color=colors[g],
                      edgecolor=SURFACE, linewidth=0.6, label=names[g] if j == 0 else None)
    b.set_xticks([1, 2, 3], ["Component 1", "Component 2", "Component 3"])
    b.set_ylabel("Sample score (normalised)", color=INK)
    panel(b, "B", "Samples on components 1–3 (exploratory)")
    legend_below(fig, [a, b])
    save(fig, "Fig4_GSE2596_exploratory")


def figS1():
    rng = np.random.default_rng(20261126 + 1)
    X = sim.simulate(80, True, rng)
    res = rmt.denoise(X, n_keep=5)
    fig, ax = plt.subplots(figsize=(8.0, 4.4), facecolor=SURFACE)
    fig.subplots_adjust(left=0.09, right=0.97, top=0.90, bottom=0.25)
    style(ax)
    eig = res.eigenvalues
    bulk = eig[res.k:]
    ax.hist(bulk, bins=24, density=True, color="#9ec5f4", edgecolor=SURFACE, linewidth=1.2,
            label=f"Noise eigenvalues ({len(bulk)})")
    x = np.linspace(res.lambda_minus, res.lambda_plus, 800)
    ax.plot(x, rmt.mp_pdf(x, res.n_eff, res.p, res.sigma2), color=INK, lw=2, label="Marčenko–Pastur law")
    ax.axvline(res.lambda_plus, color=INK2, lw=1.2)
    ymax = ax.get_ylim()[1]
    ax.text(res.lambda_plus, ymax * 0.97, r"  edge $\lambda_+$", color=INK2, fontsize=9, va="top")
    for i in range(res.k):
        yy = ymax * (0.10 + 0.12 * i)
        ax.plot([eig[i]], [yy], marker="o", ms=8, color="#2a78d6", markeredgecolor=SURFACE,
                markeredgewidth=2, linestyle="none", label="Retained components" if i == 0 else None)
        ax.annotate(f"component {i + 1} (λ = {eig[i]:.0f})", (eig[i], yy), xytext=(9, 0),
                    textcoords="offset points", ha="left", va="center", fontsize=8.5, color=INK)
    ax.set_xlim(res.lambda_minus * 0.9, max(eig[0] * 1.2, res.lambda_plus * 1.4))
    ax.set_xlabel("Eigenvalue of the correlation matrix", color=INK)
    ax.set_ylabel("Density", color=INK)
    ax.set_title("One simulated draw: 80 samples × 5,000 genes, 3 hidden signatures (simulated data)",
                 loc="left", fontsize=10.5, color=INK)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=3, frameon=False, fontsize=8.5)
    save(fig, "FigS1_simulation_spectrum")


def figS2():
    arr = pd.read_csv(QC / "QC_cohorte331_puces.csv")
    stats = json.loads((QC / "QC_cohorte331_stats.json").read_text())
    ok, fl = arr[~arr.signalee], arr[arr.signalee]
    fig, (a, b) = new()
    a.scatter(ok.mediane, ok.iqr, s=16, color="#2a78d6", edgecolor=SURFACE, linewidth=0.5,
              label=f"Not flagged ({len(ok)})")
    a.scatter(fl.mediane, fl.iqr, s=26, color="#eb6834", edgecolor=SURFACE, linewidth=0.6, marker="D",
              label=f"Flagged ({len(fl)})")
    a.set_xlabel("Array median (log2)", color=INK)
    a.set_ylabel("Interquartile range (log2)", color=INK)
    panel(a, "A", "Distribution of each array (cohort 331)")
    bins = np.linspace(arr.distance_moyenne.min(), arr.distance_moyenne.max(), 36)
    b.hist(ok.distance_moyenne, bins=bins, color="#2a78d6", edgecolor=SURFACE, linewidth=1.0)
    b.hist(fl.distance_moyenne, bins=bins, color="#eb6834", edgecolor=SURFACE, linewidth=1.0)
    b.axvline(stats["seuil_distance"], color=INK2, lw=1, ls=(0, (4, 3)))
    b.text(stats["seuil_distance"], b.get_ylim()[1] * 0.96, "  Q3 + 1.5 × IQR", color=INK2, fontsize=8.5, va="top")
    b.set_xlabel("Mean distance to other arrays (log2)", color=INK)
    b.set_ylabel("Number of arrays", color=INK)
    panel(b, "B", "Distance of each array to the others")
    legend_below(fig, [a], ncol=2)
    save(fig, "FigS2_GSE124897_cohort331_QC")


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, figS1, figS2):
        f()
