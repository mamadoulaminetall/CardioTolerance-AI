# CardioTolerance-AI — Roadmap & état d'avancement

Légende : ☐ à faire · ◐ en cours · ☑ fait

---

## Phase 0 — Scaffold  ☑ (2026-09-03)

- ☑ Arborescence du dépôt
- ☑ `docs/00_PROMPT_BRIEF.md` (prompt verbatim)
- ☑ `docs/01_PROJECT_SPEC.md` (plan 20 sections, scénarios, scoring)
- ☑ `docs/02_ROADMAP.md` (ce fichier)
- ☑ `README.md`, `requirements.txt`, `.streamlit/config.toml`, `.gitignore`
- ☑ `app/app.py` squelette 10 pages
- ☑ stubs `outreach/` (one-pager + emails FR/EN)
- ☑ stubs `scripts/01..04`
- ☐ `git init` + 1er commit (à la demande de l'utilisateur)

## Phase 1 — Revue de littérature & état de l'art  ◐ (v1 rédigée 2026-09-03)

- ☑ 1er balayage bibliographique (recherche web) sur les blocs A/B/C/D — ~12 requêtes
- ☑ Rédaction section 3 « State of the art » sourcée → `docs/section_03_state_of_the_art.md` (v1, ~42 réfs)
- ☑ `docs/references.md` alimenté (R1–R42 + liste « à ajouter Phase 2 »)
- ☐ Requêtes PubMed/Europe PMC formelles + journalisées → `meta-analysis/data/lit_corpus.csv`
- ☐ Confirmer les identifiants marqués « [ref exacte à confirmer] » (Newell/Sagoo JCI 2010, iBox BMJ 2019, EHJ 2026 47(8):956, D-OAR, CTOT-03, JHLT 2022)
- ☐ Screening titre/résumé → texte intégral, journal des exclusions (PRISMA)

## Phase 2 — Revue systématique & méta-analyse  ◐

- ☑ Protocole revue systématique rédigé → `docs/section_04_systematic_review.md` (PICO, bases, mots-clés, éligibilité, QUADAS-2/PROBAST/NOS)
- ☑ Évaluation préliminaire faisabilité méta-analyse : **quantitative ciblée** possible sur biomarqueurs non invasifs de rejet aigu (dd-cfDNA en priorité) ; pour la **tolérance** et l'**IA** → evidence synthesis structurée justifiée
- ☐ Tableau d'extraction par étude → `data/studies_registry.csv` (colonnes = variables brief §3)
- ☐ Décision finale méta-analyse vs evidence synthesis (après extraction)
- ☐ Si méta-analyse → `scripts/03_meta_analysis.py` : modèle bivarié sens/spéc + HSROC (dd-cfDNA) ; sinon effets aléatoires DL/REML, I²/τ², forest, funnel, Egger, leave-one-out, sous-groupes, méta-régression
- ☐ Risque de biais (QUADAS-2 / PROBAST / NOS) + diagramme PRISMA
- ☐ Section 5 (méta-analyse / synthèse) rédigée

## Phase 3 — Datasets réellement accessibles  ◐

- ◐ Recherche systématique repositories (liste brief §4) avec requêtes tracées — *1er balayage GEO/ImmPort fait*
- ◐ `data/datasets_registry.csv` : v0 = 5 entrées seed (GSE124897, GSE2445, GSE2596, CTOT-03, JHLT-2022-EMB), champ `access` renseigné, colonnes marquées « à confirmer » là où non vérifié
- ☐ Vérification manuelle de CHAQUE lien + publication associée (GEO/ImmPort/EGA)
- ☐ Élargir : SRA, ArrayExpress, dbGaP, EGA, BioStudies, Zenodo, Figshare + single-cell / TCR-BCR / DSA
- ☐ Section 6 rédigée + synthèse « ce qu'on peut faire dès aujourd'hui vs sous collaboration »

## Phase 4 — Paysage français & scoring  ◐

- ◐ `data/french_teams.csv` : v0 = 5 équipes seed vérifiées par recherche web
      (PTG-PARCC / Loupy, PITIE-HTX / Coutance, CR2TI-NANTES / Brouard, CIRI-NOPAB-LYON / Thaunat, APHM-MARSEILLE à confirmer)
- ☐ Compléter : Toulouse (HLA), EFS national, plateformes single-cell/génomique, autres CHU greffe cardiaque (Bordeaux, Lille, Strasbourg, Rennes, Montpellier)
- ☐ Vérifier coordonnées publiques (site labo / annuaire institutionnel uniquement)
- ☐ `data/french_teams_scoring.csv` : 6 axes /10 + total pondéré (poids dans SPEC §6)
- ☐ Sections 7, 16, 17 + grille TOP 5 + recommandation « une seule équipe »

## Phase 5 — Méthodologie IA / multi-omics / stats  ☐

- ☐ Section 9 (Aims 1–3, familles de modèles, CV/nested CV/calibration/SHAP/robustesse)
- ☐ Section 10 (comparaison 5 modèles, valeur ajoutée incrémentale)
- ☐ Section 11 (endpoints, missing data, batch, confounders, imbalance, leakage, FDR, p>>n)
- ☐ Section 12 (validation biologique par signature)

## Phase 6 — Faisabilité, impact, publications  ☐

- ☐ Section 13 : scénarios A/B/C chiffrés (n patients, durée, coûts, réglementaire)
- ☐ Section 14 : hypothèses positive/intermédiaire/négative
- ☐ Section 15 : 3–5 articles (question, dataset, méthode, nouveauté, journal cible)

## Phase 7 — Application Streamlit  ☐

- ☐ `scripts/04_build_app_data.py` : agrège `docs/` + `data/` + `meta-analysis/` pour l'app
- ☐ Remplir les 10 pages avec le contenu validé
- ☐ Figures → `figures/` via script
- ☐ Test local `streamlit run app/app.py`
- ☐ Déploiement : git + Streamlit Cloud + OVH `landing/cardiotolerance/` (skill `medflow-sync-deploy`)

## Phase 8 — Kit de prise de contact  ☐

- ☐ `outreach/one_pager.md` finalisé (1 page, envoyable à un PI)
- ☐ `outreach/email_fr.md` + `email_en.md` personnalisés pour l'équipe #1
- ☐ Sections 1, 18, 19 du rapport
- ☐ Validation par Dr. Tall AVANT tout envoi réel
- ☐ Envoi + suivi (relance J+10)

---

## Décisions ouvertes (à trancher avec Dr. Tall)

- Nom d'outil définitif : `CardioTolerance-AI` (proposé) — OK ?
- Cible du 1er contact : sortira du scoring Phase 4, mais préférence a priori ?
- Périmètre app v1 : dossier complet interactif, ou d'abord une landing + one-pager, puis
  l'app ensuite ?
- Utiliser le logo mark v2 dans l'app (pas encore validé pour la prod) ?
