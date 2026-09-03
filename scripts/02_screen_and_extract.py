"""02 — Screening PRISMA + extraction structurée des études.

Entrée : meta-analysis/data/lit_corpus.csv (produit par 01)
Sorties :
  - meta-analysis/data/prisma_flow.json  (identified / screened / eligible / included + motifs d'exclusion)
  - data/studies_registry.csv            (1 ligne par étude incluse)

Colonnes de data/studies_registry.csv (brief §3) :
  study_id, first_author, year, country, center, cohort_size, tx_type, age_summary,
  follow_up, immunosuppression, rejection_definition, rejection_type, n_rejection,
  n_no_rejection, dsa, hla, biopsies, transcriptomics, single_cell, tcr_bcr, cytometry,
  proteomics, other_biomarkers, mortality, graft_survival, cv_events, is_reduction_or_withdrawal,
  documented_tolerance_cases, effect_measure, effect_value, ci_low, ci_high,
  auc, sensitivity, specificity, c_index, notes, source_doi

STATUT : STUB. L'extraction est manuelle/assistée, jamais inventée. Ce script sert à
valider le schéma et à consolider les fiches d'extraction en un CSV unique.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "studies_registry.csv"

COLUMNS = [
    "study_id", "first_author", "year", "country", "center", "cohort_size", "tx_type",
    "age_summary", "follow_up", "immunosuppression", "rejection_definition",
    "rejection_type", "n_rejection", "n_no_rejection", "dsa", "hla", "biopsies",
    "transcriptomics", "single_cell", "tcr_bcr", "cytometry", "proteomics",
    "other_biomarkers", "mortality", "graft_survival", "cv_events",
    "is_reduction_or_withdrawal", "documented_tolerance_cases", "effect_measure",
    "effect_value", "ci_low", "ci_high", "auc", "sensitivity", "specificity",
    "c_index", "notes", "source_doi",
]


def main() -> None:
    raise SystemExit(
        "STUB — consolider ici les fiches d'extraction validées.\n"
        f"Schéma cible ({len(COLUMNS)} colonnes) : {', '.join(COLUMNS)}\n"
        f"Sortie : {REGISTRY}"
    )


if __name__ == "__main__":
    main()
