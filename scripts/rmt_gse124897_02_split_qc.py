"""Volet A, étape 2b — GSE124897 : séparer les cohortes 331 / 558, sceller la 558,
contrôle qualité (CQ) de la 331.

RÈGLE DU PRÉENREGISTREMENT
  La cohorte 558 (validation) n'est PAS analysée avant le dépôt du préenregistrement
  sur OSF par Dr Tall. Sur elle, ce script ne calcule que : nombre d'échantillons, nombre
  de sondes, effectifs des groupes (métadonnées GEO) et une empreinte SHA-256 du contenu.
  Le fichier est écrit en lecture seule ; si on relance le script, le sceau est vérifié,
  jamais réécrit.

CQ de la cohorte 331 (découverte) : rien n'est exclu ici. Les puces atypiques sont
seulement SIGNALÉES ; la règle d'exclusion sera fixée dans le préenregistrement.
  - échelle des valeurs (log2), valeurs manquantes, sondes de contrôle AFFX ;
  - par puce : médiane, écart interquartile (IQR), distance moyenne aux autres puces
    (moyenne des |x_i − x_j| sur les sondes), corrélation médiane avec les autres ;
  - signal « distance » : distance moyenne > Q3 + 1,5 × IQR (règle de la boîte à moustaches) ;
  - signal « distribution » : score z modifié de la médiane ou de l'IQR > 3,5
    (seuil d'Iglewicz & Hoaglin) ;
  - doublons possibles : paires de puces avec r > 0,999 ;
  - variabilité des sondes (pour fixer plus tard le filtrage).

Entrée  : data/geo/GSE124897/raw/GSE124897_series_matrix.txt.gz (rmt_gse124897_01_download.py)
Sorties locales (non versionnées) : data/geo/GSE124897/derived/ (331), data/geo/GSE124897/sealed/ (558)
Sorties versionnées : results/rmt_gse124897/ (SCELLE_cohorte558.*, QC_cohorte331.*)

Usage : python -I scripts/rmt_gse124897_02_split_qc.py
"""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import stat
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
GEO = ROOT / "data" / "geo" / "GSE124897"
SRC = GEO / "raw" / "GSE124897_series_matrix.txt.gz"
DERIVED, SEALED = GEO / "derived", GEO / "sealed"
OUT = ROOT / "results" / "rmt_gse124897"

INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
BLUE, ORANGE = "#2a78d6", "#eb6834"


# ---------------------------------------------------------------------------
# Lecture
# ---------------------------------------------------------------------------
def read_series_matrix(path: Path):
    meta, begin = {}, None
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if line.startswith("!series_matrix_table_begin"):
                begin = i
                break
            if line.startswith("!Sample_"):
                parts = line.rstrip("\n").split("\t")
                meta.setdefault(parts[0], []).append([v.strip('"') for v in parts[1:]])
    if begin is None:
        raise ValueError("table de la série introuvable")
    table = pd.read_csv(path, sep="\t", skiprows=begin + 1, index_col=0, comment="!")
    table.index = table.index.astype(str)

    gsm = meta["!Sample_geo_accession"][0]
    ann = pd.DataFrame({"gsm": gsm, "titre": meta["!Sample_title"][0]})
    for row in meta.get("!Sample_characteristics_ch1", []):
        key = row[0].split(":", 1)[0].strip()
        ann[key] = [v.split(":", 1)[1].strip() if ":" in v else v for v in row]
    ann["traitement"] = meta["!Sample_data_processing"][0]
    if list(table.columns) != gsm:
        raise ValueError("ordre des colonnes ≠ liste des échantillons")
    return table, ann


# ---------------------------------------------------------------------------
# Sceau de la cohorte 558
# ---------------------------------------------------------------------------
def canonical_sha256(values: np.ndarray, samples, probes, label: str) -> str:
    """Empreinte reproductible : en-tête + identifiants + valeurs float64 (petit-boutiste, ordre C)."""
    h = hashlib.sha256()
    h.update(f"{label}\n".encode())
    h.update(("\n".join(samples) + "\n").encode())
    h.update(("\n".join(probes) + "\n").encode())
    h.update(np.ascontiguousarray(values, dtype="<f8").tobytes())
    return h.hexdigest()


def seal_558(X558: pd.DataFrame, ann558: pd.DataFrame, src_sha: str):
    label = "GSE124897 cohorte 558 (sondes x echantillons)"
    record = OUT / "SCELLE_cohorte558.json"
    npy = SEALED / "cohort558_expression.npy"
    digest = canonical_sha256(X558.to_numpy(), list(X558.columns), list(X558.index), label)

    if npy.exists() and record.exists():          # relance : on vérifie, on ne réécrit pas
        rec = json.loads(record.read_text())
        on_disk = np.load(npy)
        s = (SEALED / "cohort558_samples.txt").read_text().split("\n")
        p = (SEALED / "cohort558_probes.txt").read_text().split("\n")
        ok = canonical_sha256(on_disk, s, p, label) == rec["sha256_contenu"] == digest
        print(f"  sceau 558 déjà posé le {rec['scelle_le']} : {'INTACT' if ok else 'DIFFÉRENT !'}")
        if not ok:
            raise SystemExit("Le contenu scellé de la cohorte 558 ne correspond plus au sceau.")
        return rec

    SEALED.mkdir(parents=True, exist_ok=True)
    np.save(npy, np.ascontiguousarray(X558.to_numpy(), dtype="<f8"))
    (SEALED / "cohort558_samples.txt").write_text("\n".join(X558.columns))
    (SEALED / "cohort558_probes.txt").write_text("\n".join(X558.index))
    ann558.to_csv(SEALED / "cohort558_annotation.csv", index=False)
    for f in SEALED.iterdir():
        os.chmod(f, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)   # lecture seule

    groups = {c: ann558[c].value_counts().sort_index().to_dict()
              for c in ann558.columns if c.startswith(("3aa", "4aa"))}
    rec = {
        "cohorte": 558,
        "scelle_le": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "regle": "Aucune analyse avant le dépôt du préenregistrement sur OSF.",
        "n_echantillons": int(X558.shape[1]),
        "n_sondes": int(X558.shape[0]),
        "effectifs_groupes_metadonnees_GEO": groups,
        "sha256_contenu": digest,
        "methode_empreinte": ("sha256( '" + label + "\\n' + échantillons joints par \\n + '\\n' "
                              "+ sondes jointes par \\n + '\\n' + valeurs float64 petit-boutiste, "
                              "ordre C, sondes en lignes )"),
        "sha256_fichier_source": src_sha,
        "fichiers_locaux": "data/geo/GSE124897/sealed/ (lecture seule, non versionnés)",
    }
    record.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md = [
        "# Cohorte 558 de GSE124897 : SCELLÉE",
        "",
        "> **Aucune analyse de cette cohorte avant le dépôt du préenregistrement sur OSF.**",
        "> Seuls les éléments ci-dessous ont été calculés. Généré par "
        "`scripts/rmt_gse124897_02_split_qc.py`.",
        "",
        f"- Scellée le : {rec['scelle_le']} (UTC)",
        f"- Échantillons : {rec['n_echantillons']} · sondes : {rec['n_sondes']}",
        f"- Empreinte SHA-256 du contenu : `{digest}`",
        f"- Fichier source (série GEO) SHA-256 : `{src_sha}`",
        f"- Méthode de l'empreinte : {rec['methode_empreinte']}",
        "- Effectifs des groupes (métadonnées GEO, pas les données d'expression) : "
        + " ; ".join(f"{k} = {v}" for k, v in groups.items()),
        "",
        "À citer dans le préenregistrement : l'empreinte permet de prouver que le fichier",
        "analysé après le dépôt est celui scellé avant.",
        "",
    ]
    (OUT / "SCELLE_cohorte558.md").write_text("\n".join(md), encoding="utf-8")
    print(f"  cohorte 558 scellée : {X558.shape[1]} échantillons, sha256 {digest[:16]}…")
    return rec


# ---------------------------------------------------------------------------
# Contrôle qualité de la cohorte 331
# ---------------------------------------------------------------------------
def modified_z(x):
    med = np.median(x)
    mad = np.median(np.abs(x - med))
    return 0.6745 * (x - med) / mad if mad > 0 else np.zeros_like(x)


def qc_331(X: pd.DataFrame, ann: pd.DataFrame):
    V = X.to_numpy(dtype=float)
    n_probes, n = V.shape
    q1, med, q3 = np.percentile(V, [25, 50, 75], axis=0)
    iqr = q3 - q1
    dist = np.empty(n)
    for i in range(n):
        dist[i] = np.abs(V - V[:, [i]]).mean(axis=0).sum() / (n - 1)
    R = np.corrcoef(V.T)
    np.fill_diagonal(R, np.nan)
    corr_med = np.nanmedian(R, axis=1)
    dq1, dq3 = np.percentile(dist, [25, 75])
    thr = dq3 + 1.5 * (dq3 - dq1)
    z_med, z_iqr = modified_z(med), modified_z(iqr)

    arrays = pd.DataFrame({
        "gsm": X.columns, "groupe_3aa": ann["3aa group (1,2,3)"].values,
        "groupe_4aa": ann["4aa group (1,2,3,4)"].values,
        "mediane": med, "iqr": iqr, "distance_moyenne": dist, "correlation_mediane": corr_med,
        "z_mediane": z_med, "z_iqr": z_iqr,
        "signal_distance": dist > thr,
        "signal_distribution": (np.abs(z_med) > 3.5) | (np.abs(z_iqr) > 3.5),
    })
    arrays["signalee"] = arrays.signal_distance | arrays.signal_distribution

    iu = np.triu_indices(n, 1)
    dup = [(X.columns[i], X.columns[j], R[i, j]) for i, j in zip(*iu) if R[i, j] > 0.999]
    sorted_cols = np.sort(V, axis=0)
    sd = V.std(axis=1, ddof=1)
    stats = {
        "n_puces": n, "n_sondes": n_probes,
        "valeurs_manquantes": int(np.isnan(V).sum()),
        "min": float(np.nanmin(V)), "max": float(np.nanmax(V)),
        "sondes_controle_AFFX": int(X.index.str.startswith("AFFX").sum()),
        "ecart_max_entre_distributions": float(np.abs(sorted_cols - sorted_cols[:, [0]]).max()),
        "seuil_distance": float(thr),
        "doublons_r_sup_0999": len(dup),
        "sd_sondes_quantiles": {q: float(np.percentile(sd, q)) for q in (5, 25, 50, 75, 95)},
        "sondes_sd_inf_0_1": int((sd < 0.1).sum()), "sondes_sd_inf_0_2": int((sd < 0.2).sum()),
        "moyenne_sondes_quantiles": {q: float(np.percentile(V.mean(axis=1), q)) for q in (5, 50, 95)},
    }
    return arrays, stats, dup


def _style(ax):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def qc_figure(arrays: pd.DataFrame, stats: dict):
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.0), facecolor=SURFACE)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.75, bottom=0.25, wspace=0.28)
    ok, fl = arrays[~arrays.signalee], arrays[arrays.signalee]

    ax = axes[0]
    _style(ax)
    ax.scatter(ok.mediane, ok.iqr, s=20, color=BLUE, edgecolor=SURFACE, linewidth=0.6,
               label=f"Puces sans signal ({len(ok)})")
    ax.scatter(fl.mediane, fl.iqr, s=34, color=ORANGE, edgecolor=SURFACE, linewidth=0.8,
               marker="D", label=f"Puces signalées ({len(fl)})")
    ax.set_xlabel("Médiane de la puce (log2)", color=INK, fontsize=10)
    ax.set_ylabel("Écart interquartile (log2)", color=INK, fontsize=10)
    ax.set_title("A. Distribution de chaque puce", loc="left", fontsize=11, color=INK)

    ax = axes[1]
    _style(ax)
    bins = np.linspace(arrays.distance_moyenne.min(), arrays.distance_moyenne.max(), 36)
    ax.hist(ok.distance_moyenne, bins=bins, color=BLUE, edgecolor=SURFACE, linewidth=1.2)
    ax.hist(fl.distance_moyenne, bins=bins, color=ORANGE, edgecolor=SURFACE, linewidth=1.2)
    ax.axvline(stats["seuil_distance"], color=INK2, lw=1, ls=(0, (4, 3)))
    ymax = ax.get_ylim()[1]
    ax.text(stats["seuil_distance"], ymax * 0.96, "  seuil Q3 + 1,5 × IQR", color=INK2,
            fontsize=9, va="top")
    ax.set_xlabel("Distance moyenne aux autres puces (log2)", color=INK, fontsize=10)
    ax.set_ylabel("Nombre de puces", color=INK, fontsize=10)
    ax.set_title("B. Écart de chaque puce aux autres", loc="left", fontsize=11, color=INK)

    fig.text(0.08, 0.94, "GSE124897, cohorte 331 (découverte) : contrôle qualité des puces",
             fontsize=12.5, color=INK, weight="bold")
    fig.text(0.08, 0.89, "Données publiques GEO. Puces signalées, aucune exclue : la règle "
             "sera fixée dans le préenregistrement.", fontsize=9.5, color=INK2)
    fig.text(0.08, 0.85, "La cohorte 558 (validation) est scellée et n'apparaît pas ici.",
             fontsize=9.5, color="#b4231f")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", bbox_to_anchor=(0.5, 0.01), ncol=2, frameon=False,
               fontsize=9, labelcolor=INK)
    path = OUT / "QC_cohorte331.png"
    fig.savefig(path, dpi=200, facecolor=SURFACE)
    plt.close(fig)
    return path


def write_qc_md(arrays, stats, ann331, processing):
    fl = arrays[arrays.signalee]
    cross = pd.crosstab(arrays.groupe_4aa, arrays.signalee).rename(
        columns={False: "non signalées", True: "signalées"})
    rate = (100 * arrays.groupe_4aa.map(arrays.groupby("groupe_4aa").signalee.mean())
            .groupby(arrays.groupe_4aa).first())
    worst = rate.idxmax()
    sdq = stats["sd_sondes_quantiles"]
    L = [
        "# GSE124897 — cohorte 331 (découverte) : contrôle qualité",
        "",
        "> Données publiques GEO (Parkes et al., *J Heart Lung Transplant* 2019). Généré par",
        "> `scripts/rmt_gse124897_02_split_qc.py` : ne pas modifier à la main.",
        "> **La cohorte 558 est scellée** (voir `SCELLE_cohorte558.md`) et n'entre dans aucun calcul ici.",
        "",
        "## Données",
        f"- {stats['n_puces']} puces × {stats['n_sondes']} sondes (GPL15207, PrimeView), dont "
        f"{stats['sondes_controle_AFFX']} sondes de contrôle AFFX.",
        f"- Prétraitement des auteurs (fiche GEO) : « {processing} »",
        f"- Valeurs manquantes : {stats['valeurs_manquantes']} · étendue : "
        f"{stats['min']:.2f} à {stats['max']:.2f} (échelle log2).",
        f"- Écart maximal entre les distributions triées des puces : "
        f"{stats['ecart_max_entre_distributions']:.3f} (0 = distributions identiques).",
        "- Groupes (métadonnées GEO) : 3AA "
        + str(ann331["3aa group (1,2,3)"].value_counts().sort_index().to_dict())
        + " ; 4AA " + str(ann331["4aa group (1,2,3,4)"].value_counts().sort_index().to_dict()) + ".",
        "",
        "## Puces signalées (aucune exclue)",
        f"- Signal « distance » (distance moyenne > {stats['seuil_distance']:.3f}) : "
        f"{int(arrays.signal_distance.sum())} puces.",
        f"- Signal « distribution » (score z modifié > 3,5) : {int(arrays.signal_distribution.sum())} puces.",
        f"- Au total : {len(fl)} puces signalées sur {stats['n_puces']}.",
        f"- Doublons possibles (r > 0,999) : {stats['doublons_r_sup_0999']}.",
        "",
        "Répartition par groupe 4AA (un signal dans un groupe de rejet peut être biologique, pas technique) :",
        "",
        "| groupe 4AA | non signalées | signalées | % signalées |",
        "|---|---|---|---|",
    ]
    for g, row in cross.iterrows():
        L.append(f"| {g} | {row.get('non signalées', 0)} | {row.get('signalées', 0)} | "
                 f"{rate[g]:.1f} % |".replace(".", ","))
    L += ["",
          f"Les signaux sont inégalement répartis : de {rate.min():.1f} % à {rate.max():.1f} % "
          f"selon le groupe (maximum : groupe {worst}).".replace(".", ",", 2)
          + " Une puce « éloignée des autres » dans un groupe de rejet ou de lésion peut être une"
          " biopsie biologiquement différente, pas une puce défectueuse : les exclure retirerait"
          " surtout des biopsies anormales. Signification exacte des groupes 4AA : à confirmer"
          " dans Parkes et al. 2019.",
          "", "Détail par puce : `QC_cohorte331_puces.csv`.", "",
          "## Variabilité des sondes (pour fixer le filtrage dans le préenregistrement)",
          f"- Écart-type par sonde, quantiles 5/25/50/75/95 % : "
          + " / ".join(f"{sdq[q]:.3f}" for q in (5, 25, 50, 75, 95)) + ".",
          f"- Sondes d'écart-type < 0,1 : {stats['sondes_sd_inf_0_1']} ; < 0,2 : {stats['sondes_sd_inf_0_2']}.",
          "",
          "## Points à trancher dans le préenregistrement (étape 3)",
          "1. **Normalisation.** Les valeurs GEO viennent d'un RMA fait par les auteurs ; la fiche ne dit pas",
          "   si les 889 puces ont été normalisées ensemble. Si oui, la cohorte 558 a influencé les valeurs de",
          "   la 331 (fuite légère). Option propre : refaire un RMA séparé par cohorte à partir des fichiers",
          "   CEL (1,7 Go ; R/Bioconductor n'est pas installé sur ce poste).",
          "2. **Exclusion des puces** : quelle règle (signaux ci-dessus ou aucune exclusion).",
          "3. **Filtrage des sondes** : contrôles AFFX, sondes peu variables, passage sonde → gène.",
          "4. **Non-indépendance** : 889 biopsies pour 454 patients, sans identifiant patient dans GEO.",
          "5. **Effets de centre** : 8 centres, sans étiquette de centre dans GEO.",
          ""]
    (OUT / "QC_cohorte331.md").write_text("\n".join(L), encoding="utf-8")


# ---------------------------------------------------------------------------
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src_sha = hashlib.sha256(SRC.read_bytes()).hexdigest()
    print("lecture de la série…", flush=True)
    table, ann = read_series_matrix(SRC)
    coh = ann["cohort (331 or 558)"].astype(int).to_numpy()
    print(f"  {table.shape[1]} échantillons × {table.shape[0]} sondes ; cohortes : "
          f"{(coh == 331).sum()} / {(coh == 558).sum()}")
    if table.shape[1] != 889 or (coh == 331).sum() != 331 or (coh == 558).sum() != 558:
        raise SystemExit("effectifs inattendus : arrêt")

    X331, ann331 = table.loc[:, coh == 331], ann[coh == 331].reset_index(drop=True)
    X558, ann558 = table.loc[:, coh == 558], ann[coh == 558].reset_index(drop=True)
    del table
    seal_558(X558, ann558, src_sha)
    del X558

    DERIVED.mkdir(parents=True, exist_ok=True)
    np.save(DERIVED / "cohort331_expression.npy", np.ascontiguousarray(X331.to_numpy(), dtype="<f8"))
    (DERIVED / "cohort331_samples.txt").write_text("\n".join(X331.columns))
    (DERIVED / "cohort331_probes.txt").write_text("\n".join(X331.index))
    ann331.to_csv(DERIVED / "cohort331_annotation.csv", index=False)

    print("contrôle qualité de la cohorte 331…", flush=True)
    arrays, stats, dup = qc_331(X331, ann331)
    arrays.to_csv(OUT / "QC_cohorte331_puces.csv", index=False, float_format="%.4f")
    (OUT / "QC_cohorte331_stats.json").write_text(
        json.dumps({**stats, "doublons": [[a, b, round(float(r), 5)] for a, b, r in dup]},
                   indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("  figure :", qc_figure(arrays, stats).relative_to(ROOT))
    write_qc_md(arrays, stats, ann331, ann["traitement"].iloc[0])
    print(f"  puces signalées : {int(arrays.signalee.sum())} / {stats['n_puces']} ; "
          f"doublons r>0,999 : {stats['doublons_r_sup_0999']}")
    print(f"terminé → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
