# CardioTolerance-AI

*AI-driven discovery of immune tolerance signatures after heart transplantation*

**Porteur :** MedFlow AI · Dr. Mamadou Lamine TALL, PhD Bioinformatique & Data Science
**Localisation :** Castelnau-le-Lez, France (Montpellier) — collaborations académiques recherchées
**Contact :** contact@medflow-ai.fr · https://medflow-ai.fr
**Statut :** cadrage scientifique + montage de collaboration — **pas** un dispositif médical, **pas** un protocole PROSPERO déposé, **pas** un avis médical.
**Créé :** 2026-09-03

---

## Objet du dossier

Ce dépôt porte deux livrables couplés :

1. **L'application MedFlow AI `CardioTolerance-AI`** — un outil interactif (Streamlit) qui
   présente la question scientifique, la synthèse de littérature, la cartographie des
   datasets réellement accessibles, le paysage français des équipes, le gap et la
   méthodologie IA/multi-omics proposée. Sert de support de discussion avec un centre
   de transplantation cardiaque.
2. **Le kit de prise de contact** (`outreach/`) — dossier 1 page + emails FR/EN
   personnalisables, destinés au·à la responsable d'une équipe française pertinente, dans
   le but d'obtenir l'accès à une cohorte rétrospective pour **entraîner et valider les
   modèles**.

> Garde-fou scientifique répété du brief : le projet **ne suppose jamais** qu'un patient
> puisse arrêter son immunosuppression. L'objectif est d'identifier des **biomarqueurs et
> des profils de tolérance** susceptibles d'être validés prospectivement, sous supervision
> médicale.

---

## Structure du dépôt

```
CardioTolerance-AI/
├── README.md                  ← ce fichier
├── requirements.txt
├── .streamlit/config.toml     ← thème sombre MedFlow AI
├── docs/
│   ├── 00_PROMPT_BRIEF.md     ← prompt fondateur, verbatim (cahier des charges)
│   ├── 01_PROJECT_SPEC.md     ← spec structurée : plan du rapport en 20 sections, scénarios A/B/C, grille TOP 5
│   └── 02_ROADMAP.md          ← plan de travail par étapes + état d'avancement
├── app/
│   └── app.py                 ← application Streamlit (squelette + sections)
├── scripts/
│   ├── 01_build_lit_corpus.py     ← collecte PubMed/EBI (stub)
│   ├── 02_screen_and_extract.py   ← screening + extraction tableau d'études (stub)
│   ├── 03_meta_analysis.py        ← effets aléatoires, I², funnel (stub)
│   └── 04_build_app_data.py       ← agrège docs/ + meta-analysis/ vers data/ pour l'app (stub)
├── data/                      ← CSV générés (registre d'études, datasets, équipes) — ne pas éditer à la main
├── figures/                   ← figures générées pour l'app / le dossier
├── meta-analysis/             ← pipeline revue systématique + méta-analyse
│   ├── scripts/  data/  figures/  manuscript/
└── outreach/
    ├── one_pager.md           ← version 1 page du projet (PI / directeur de labo)
    ├── email_fr.md            ← brouillon email français
    └── email_en.md            ← brouillon email anglais
```

---

## Workflow de mise à jour (obligatoire)

Cet outil vit sur **trois surfaces** qui dérivent si on les touche séparément :
**git** (ce dépôt + éventuel `streamlit_app/`), **Streamlit** (app locale + déployée),
**OVH** (`landing/cardiotolerance/` sur medflow-ai.fr).

➡️ À chaque changement de chiffre / donnée / claim : suivre la skill **`medflow-sync-deploy`**
et propager sur les trois surfaces dans le même passage. Ne jamais dire « corrigé » sans
avoir vérifié les trois.

---

## Lancer l'application

```bash
cd "Claude Code/MedFlowAI/tools/CardioTolerance-AI"
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/app.py
```

---

## Rigueur — rappel

Aucune donnée, cohorte, coordonnée, performance de modèle, DOI ou collaboration inventée.
Toute affirmation importante est sourcée (PubMed / repositories officiels / pages
institutionnelles). Information manquante → écrire explicitement
**« Donnée non disponible / à confirmer auprès de l'équipe. »**
