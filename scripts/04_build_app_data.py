"""04 — Consolidation des données pour l'application Streamlit.

Vérifie la présence et l'intégrité de schéma des fichiers que app/app.py consomme, puis
copie/normalise ce qui doit l'être vers data/. Ne fabrique rien : signale ce qui manque.

Fichiers attendus par l'app (docs/01_PROJECT_SPEC.md §8) :
  data/studies_registry.csv
  data/datasets_registry.csv
  data/french_teams.csv
  data/french_teams_scoring.csv
  data/meta_estimates.csv
  docs/section_01_executive_summary.md
  docs/section_03_state_of_the_art.md
  docs/section_04_systematic_review.md
  docs/section_05_meta_analysis.md
  docs/section_06_datasets.md
  docs/section_07_french_landscape.md
  docs/section_08_09_gap_method.md
  docs/section_13_feasibility.md
  docs/section_15_16_17_collab.md
  outreach/one_pager.md
  outreach/email_fr.md
  outreach/email_en.md

STATUT : STUB — implémenter les checks de schéma au fur et à mesure du remplissage.

Rappel workflow : après toute mise à jour de chiffre/donnée, propager git + Streamlit +
OVH dans le même passage (skill medflow-sync-deploy).
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPECTED = [
    "data/studies_registry.csv",
    "data/datasets_registry.csv",
    "data/french_teams.csv",
    "data/french_teams_scoring.csv",
    "data/meta_estimates.csv",
    "docs/section_01_executive_summary.md",
    "docs/section_03_state_of_the_art.md",
    "docs/section_04_systematic_review.md",
    "docs/section_05_meta_analysis.md",
    "docs/section_06_datasets.md",
    "docs/section_07_french_landscape.md",
    "docs/section_08_09_gap_method.md",
    "docs/section_13_feasibility.md",
    "docs/section_15_16_17_collab.md",
    "outreach/one_pager.md",
    "outreach/email_fr.md",
    "outreach/email_en.md",
]


def main() -> None:
    missing = [rel for rel in EXPECTED if not (ROOT / rel).exists()]
    present = [rel for rel in EXPECTED if (ROOT / rel).exists()]
    print(f"Présents ({len(present)}/{len(EXPECTED)}):")
    for rel in present:
        print(f"  ok  {rel}")
    print(f"\nManquants ({len(missing)}):")
    for rel in missing:
        print(f"  --  {rel}")
    if missing:
        raise SystemExit(1)
    print("\nTous les livrables attendus sont présents.")


if __name__ == "__main__":
    main()
