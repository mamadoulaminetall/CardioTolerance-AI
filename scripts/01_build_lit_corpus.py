"""01 — Construction du corpus bibliographique.

Objectif : interroger PubMed (E-utilities) et EMBL-EBI Europe PMC avec les blocs de
mots-clés A/B/C/D du brief (docs/00_PROMPT_BRIEF.md §2), dédupliquer par DOI/PMID, et
exporter un corpus brut pour screening.

Sortie : meta-analysis/data/lit_corpus.csv
Colonnes : pmid, doi, year, journal, title, abstract, query_block, retrieved_at

STATUT : STUB. Remplir les requêtes réelles + implémenter la pagination E-utilities avant
usage. Ne rien exporter de simulé.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "meta-analysis" / "data" / "lit_corpus.csv"

# Blocs de mots-clés — à figer et à versionner (traçabilité PRISMA).
QUERY_BLOCKS: dict[str, list[str]] = {
    "A_tolerance": [
        "operational tolerance", "immune tolerance", "spontaneous tolerance",
        "cardiac allograft tolerance", "heart transplant tolerance",
        "long-term heart transplant survivors", "immunosuppression minimization",
        "immunosuppression withdrawal", "rejection-free heart transplant recipients",
    ],
    "B_immune_signatures": [
        "Treg", "regulatory T cells", "regulatory B cells", "NK cells",
        "T-cell exhaustion", "T-cell repertoire", "TCR sequencing", "BCR sequencing",
        "donor-specific antibodies", "HLA", "cytokines", "immune cell profiling",
        "mass cytometry", "immune transcriptomics",
    ],
    "C_multiomics": [
        "RNA-seq", "single-cell RNA-seq", "spatial transcriptomics", "epigenomics",
        "methylation", "proteomics", "metabolomics", "microbiome", "multi-omics",
        "longitudinal omics", "transplant immunology omics",
    ],
    "D_ai_ml": [
        "machine learning", "deep learning", "survival models",
        "longitudinal machine learning", "multimodal learning",
        "multi-omics machine learning", "explainable AI", "biomarker discovery",
        "rejection prediction", "transplant outcome prediction",
    ],
}


def main() -> None:
    raise SystemExit(
        "STUB — implémenter la collecte PubMed/Europe PMC.\n"
        f"Sortie attendue : {OUT}\n"
        "Ne pas générer de données simulées."
    )


if __name__ == "__main__":
    main()
