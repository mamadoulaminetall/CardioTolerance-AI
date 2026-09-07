"""05 — Assemblage du rapport final unique.

Concatène les sections rédigées dans l'ordre imposé par le brief §17, préfixe un en-tête
et un sommaire, et écrit docs/RAPPORT_FINAL.md. Idempotent : réécrase le fichier.

Usage : python scripts/05_assemble_report.py
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = DOCS / "RAPPORT_FINAL.md"

# (titre de partie, chemin) — dans l'ordre du livrable final (brief §17)
PARTS = [
    ("1. Executive Summary", DOCS / "section_01_executive_summary.md"),
    ("2. Question scientifique", DOCS / "section_02_question.md"),
    ("3. État de l'art", DOCS / "section_03_state_of_the_art.md"),
    ("4. Revue systématique", DOCS / "section_04_systematic_review.md"),
    ("5. Méta-analyse / synthèse de preuves", DOCS / "section_05_meta_analysis.md"),
    ("6. Données réellement disponibles", DOCS / "section_06_datasets.md"),
    ("7. Paysage français", DOCS / "section_07_french_landscape.md"),
    ("8–12. Gap, projet IA, multi-omics, méthodo statistique, validation biologique",
     DOCS / "section_08_09_gap_method.md"),
    ("13–15. Faisabilité, impact attendu, publications", DOCS / "section_13_feasibility.md"),
    ("16–17. Collaboration, TOP 5, premier contact", DOCS / "section_15_16_17_collab.md"),
    ("18. Brouillon d'email — Français", ROOT / "outreach" / "email_fr.md"),
    ("19. Brouillon d'email — English", ROOT / "outreach" / "email_en.md"),
    ("20. Références", DOCS / "references.md"),
]

HEADER = f"""# CardioTolerance-AI — Rapport de faisabilité

**AI-driven discovery of immune tolerance signatures after heart transplantation**

MedFlow AI · Dr. Mamadou Lamine Tall, PhD (Bioinformatique & Data Science) — Montpellier
· contact@medflow-ai.fr · https://medflow-ai.fr

*Document assemblé automatiquement le {dt.date.today().isoformat()} par
`scripts/05_assemble_report.py` à partir des sections de `docs/`. Ne pas éditer ici —
éditer les sections sources puis relancer le script.*

> **Statut : v1 de travail.** Plusieurs éléments sont marqués « à confirmer » (identifiants
> de références, effectifs de datasets, coordonnées d'équipes). La revue systématique
> formelle (requêtes journalisées + extraction sur texte intégral) et la méta-analyse
> dd-cfDNA restent à exécuter (Phase 2). Les brouillons d'emails **ne doivent pas être
> envoyés** sans validation de Dr. Tall.

> **Garde-fou scientifique :** le projet ne présuppose jamais l'arrêt de
> l'immunosuppression. Objectif = biomarqueurs et profils de tolérance à valider
> prospectivement, sous supervision médicale.

---

## Sommaire

"""


def main() -> None:
    toc = []
    body = []
    missing = []
    for i, (title, path) in enumerate(PARTS, 1):
        anchor = title.lower().replace(" ", "-").replace(".", "").replace(",", "").replace("—", "").replace("/", "")
        toc.append(f"{i}. [{title}](#{anchor})")
        body.append(f"\n\n---\n\n# {title}\n")
        if path.exists():
            body.append(path.read_text(encoding="utf-8").strip())
        else:
            body.append(f"*(source manquante : `{path.relative_to(ROOT)}` — à produire)*")
            missing.append(str(path.relative_to(ROOT)))

    OUT.write_text(HEADER + "\n".join(toc) + "\n" + "".join(body) + "\n", encoding="utf-8")
    print(f"Écrit : {OUT.relative_to(ROOT)}  ({OUT.stat().st_size // 1024} Ko)")
    if missing:
        print("Sources manquantes :")
        for m in missing:
            print("  -", m)


if __name__ == "__main__":
    main()
