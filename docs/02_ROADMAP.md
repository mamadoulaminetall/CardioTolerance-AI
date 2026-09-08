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
- ☑ `data/studies_registry.csv` v0 = 12 études seed (S01–S12) — métadonnées vérifiées (dont S12 Piening/CTOT-03, S07 MMDx-3230 archétypes)
- ☑ `data/meta_estimates.csv` v0 = MA publiée dd-cfDNA (10 études ; sens 65 / spéc 79 / AUC 0,83 — **rapportée, non recalculée**) + ligne re-analyse + 2 comparateurs
- ☑ Section 5 rédigée + chiffres réels (FreeDNA-CAR AUC 0,60 — **étude espagnole**, corrigée)
- ☑ `scripts/03_meta_analysis.py` **implémenté et runnable** (pooling DL logit sens/spéc + I² + IP + espace ROC + forest) ; s'arrête proprement en l'absence de `data/ddcfdna_2x2.csv`
- ☐ **Extraction 2×2 (TP/FP/FN/TN) sur textes intégraux** → `data/ddcfdna_2x2.csv` *(bloquant : accès bibliothèque/institutionnel — pas un verrou méthodo)*
- ☐ Requêtes PubMed/Europe PMC **formelles journalisées** → `lit_corpus.csv` + journal PRISMA
- ☐ Risque de biais (QUADAS-2 / PROBAST / NOS)
- ☐ Décision finale confirmée après extraction complète

## Phase 3 — Datasets réellement accessibles  ◐

- ◐ Recherche systématique repositories (liste brief §4) avec requêtes tracées — *1er balayage GEO/ImmPort fait*
- ◐ `data/datasets_registry.csv` : v0 = 5 entrées seed (GSE124897, GSE2445, GSE2596, CTOT-03, JHLT-2022-EMB), champ `access` renseigné, colonnes marquées « à confirmer » là où non vérifié
- ☑ Section 6 rédigée → `docs/section_06_datasets.md` (classification par accès + « faisable dès aujourd'hui » Scénario A)
- ☐ Vérification manuelle de CHAQUE lien + publication associée (GEO/ImmPort/EGA)
- ☐ Élargir : SRA, ArrayExpress, dbGaP, EGA, BioStudies, Zenodo, Figshare + single-cell / TCR-BCR / DSA

## Phase 4 — Paysage français & scoring  ◐ (v1 — cible n°1 arrêtée 2026-09-03)

- ☑ `data/french_teams.csv` : 5 équipes seed vérifiées ; contacts ramenés aux canaux institutionnels
- ☑ `data/french_teams_scoring.csv` : 6 axes /10 + total pondéré /70
- ☑ Section 7 (`section_07_french_landscape.md`), Sections 15-16-17 (`section_15_16_17_collab.md`) : grille TOP 5 + reco « une seule équipe »
- ☑ **Cible n°1 = Paris Transplant Group / PITOR (PARCC)** — angle cœur via G. Coutance, sous l'égide d'A. Loupy — total 60,25/70. n°2 méthodo sans concurrence : CR2TI Nantes (Brouard).
- ☐ Compléter le paysage : Rouen (Charles Nicolle), Bordeaux, Lille, Strasbourg, Rennes, Toulouse, Montpellier ; EFS/HLA national ; registre CRISTAL (Agence de la biomédecine) ; plateformes single-cell
- ☐ Vérifier AP-HM Marseille (PI + unité de rattachement non confirmés)
- ☐ Confirmer la voie de contact exacte du PTG (formulaire vs adresse générique PARCC)

## Phase 5 — Méthodologie IA / multi-omics / stats  ◐ (v1 rédigée 2026-09-03)

- ☑ Section 8 (Gap Q1–Q10) → `docs/section_08_09_gap_method.md`
- ☑ Section 9 (Aims 1–3, familles de modèles, nested CV/calibration/SHAP/robustesse, définition préspécifiée du phénotype)
- ☑ Section 10 (comparaison M1→M5, gain incrémental, coût-information, net benefit)
- ☑ Section 11 (endpoints, p≫n, leakage, batch, confounders, imbalance, FDR, missing data, puissance, TRIPOD+AI/PROBAST)
- ☐ Relecture clinicien/immunologiste de la définition du phénotype « stabilité profonde »
- ☐ Section 12 (validation biologique par signature) — à rédiger

## Phase 6 — Faisabilité, impact, publications  ☑ (v1 rédigée 2026-09-03)

- ☑ Section 13 : scénarios A/B/C chiffrés (n, durée, ressources, coûts, réglementaire, risques) → `docs/section_13_feasibility.md`
- ☑ Section 14 : hypothèses positive/intermédiaire/négative + valeur méthodo transverse
- ☑ Section 15 : 5 articles (question, dataset, méthode, nouveauté, journal cible)
- ☐ Chiffres à réviser avec l'équipe partenaire au 1er échange (prévalence phénotype, coûts réels)

## Phase 6bis — Executive summary & sections restantes  ◐

- ☑ Section 1 (executive summary) → `docs/section_01_executive_summary.md`
- ☑ Section 2 (question scientifique) → `docs/section_02_question.md`
- ☑ Section 5 (décision méta-analyse / evidence synthesis) → `docs/section_05_meta_analysis.md`
- ☑ Section 12 (validation biologique) → ajoutée à `docs/section_08_09_gap_method.md`
- ☑ Section 20 (références) → `docs/references.md` (R1–R48)
- ☑ **Assemblage** : `scripts/05_assemble_report.py` → `docs/RAPPORT_FINAL.md` (20 parties, ~1700 lignes)
- ☑ **Export PDF** : `scripts/06_report_pdf.py` → `docs/RAPPORT_FINAL.pdf` (reportlab, 54 pages, police Arial Unicode, tables/gras/italique/liens rendus, en-tête + pagination)
- ☑ Figures : `scripts/02_generate_figures.py` → `figures/` — **mise en page corrigée** (zéro superposition de texte, légende dans le cadre, PRISMA aux compteurs réels), vérifiées visuellement
- ☐ Régénérer `RAPPORT_FINAL.{md,pdf}` + figures à chaque mise à jour de section (part du workflow sync)

## Phase 7 — Application Streamlit  ◐

- ☑ `scripts/04_build_app_data.py` : contrôle de présence des 17 livrables (15/17 OK ; manquent studies_registry + meta_estimates)
- ☑ Les 10 pages chargent leur contenu (docs/ + data/) ; filtres datasets (accès) & équipes (ville) ; barres de scoring plotly page 9
- ☑ Test local OK — `streamlit run app/app.py` démarre (HTTP 200), tous les chemins data-dépendants exercés sans erreur
- ☐ Contenu pages 3 & 4 incomplet tant que `studies_registry.csv` / `meta_estimates.csv` absents (Phase 2)
- ☐ Figures → `figures/` via `scripts/02_generate_figures.py` (PRISMA flow, HSROC, radar scoring)
- ☐ Colonne courte `access_class` dans `datasets_registry.csv` pour des filtres plus lisibles
- ☑ **OVH** : page `landing/cardiotolerance-ai.html` déployée (SFTP) → https://medflow-ai.fr/cardiotolerance-ai.html (HTTP 200) + entrée `sitemap.xml`. Palette teal du site, garde-fous explicites, 5 réfs vérifiées, CTA « proposer une collaboration ».
- ☑ **Accueil medflow-ai.fr** : section `#recherche` « Projets de recherche en cours » ajoutée (entre les outils et l'écosystème) + lien « Recherche » dans le menu → carte CardioTolerance-AI (statut « Cadrage »). Déployé, vérifié live.
- ☑ **GitHub** : repo privé `github.com/mamadoulaminetall/CardioTolerance-AI` — `main` poussé (2026-09-08, 16 commits, 181 objets)
- ☐ **Streamlit Cloud** : à connecter sur share.streamlit.io → New app → ce repo, branche `main`, **main file `app/app.py`** (autoriser l'accès au repo privé). Puis ajouter le bouton « Ouvrir l'app » sur `landing/cardiotolerance-ai.html`.
- ☐ Option : entrée grille/JSON-LD sur l'accueil medflow-ai.fr si mise en avant souhaitée

## Phase 8 — Kit de prise de contact  ◐ (v1 rédigé 2026-09-03)

- ☑ `outreach/one_pager.md` v1 (démarrage en 2 temps Scénario A puis B)
- ☑ `outreach/email_fr.md` + `email_en.md` personnalisés pour la cible n°1 (G. Coutance / PTG-PARCC)
- ☐ Sections 1 (executive summary), 18, 19 du rapport (reprennent les emails)
- ☐ Confirmer avec Dr. Tall : cible nominative, périmètre de l'offre, voie d'envoi
- ☐ Vérifier la voie de contact institutionnelle exacte avant envoi
- ☐ Validation par Dr. Tall AVANT tout envoi réel
- ☐ Envoi + suivi (relance J+10) ; contact méthodo Nantes (Brouard) en parallèle

---

## Décisions ouvertes (à trancher avec Dr. Tall)

- Nom d'outil définitif : `CardioTolerance-AI` (proposé) — OK ?
- Cible du 1er contact : sortira du scoring Phase 4, mais préférence a priori ?
- Périmètre app v1 : dossier complet interactif, ou d'abord une landing + one-pager, puis
  l'app ensuite ?
- Utiliser le logo mark v2 dans l'app (pas encore validé pour la prod) ?
