# CardioTolerance-AI — Spécification structurée

Dérivée de [`00_PROMPT_BRIEF.md`](00_PROMPT_BRIEF.md). Décrit **quoi produire**, **dans quel
format**, **avec quel niveau de preuve**. La rédaction du contenu se fait par étapes
(voir [`02_ROADMAP.md`](02_ROADMAP.md)).

---

## 1. Titre de travail

**« AI-driven discovery of immune tolerance signatures after heart transplantation »**
Nom d'outil MedFlow AI : **CardioTolerance-AI**.

## 2. Question scientifique centrale

Existe-t-il, chez certains receveurs de greffe cardiaque, une **signature immunologique /
moléculaire / cellulaire / multi-omique** associée à une tolérance particulièrement élevée
du greffon, et l'IA peut-elle :

1. identifier cette signature ;
2. séparer rejet vs stabilité durable ;
3. repérer des profils de tolérance immunologique exceptionnelle ;
4. prédire longitudinalement l'évolution du risque de rejet ;
5. à terme, aider à identifier des candidats à une **réduction contrôlée et supervisée**
   de l'immunosuppression (jamais un arrêt).

## 3. Contraintes non négociables (garde-fous)

- Ne jamais suggérer l'arrêt de l'immunosuppression.
- Ne jamais inventer : données, patients, résultats, datasets, DOI, coordonnées,
  performances de modèles, biomarqueurs, essais, collaborations.
- Information absente → « Donnée non disponible / à confirmer auprès de l'équipe. »
- Toute affirmation importante = 1 référence (PubMed / repo officiel / page institutionnelle).
- Preprints (bioRxiv/medRxiv) explicitement étiquetés comme tels.
- Distinguer clairement narratif vs quantitatif pour la synthèse de preuves.

---

## 4. Plan du livrable final (20 sections — ordre imposé par le brief §17)

| # | Section | Contenu attendu | Source de preuve |
|---|---------|-----------------|------------------|
| 1 | Executive Summary | 1 page : question, gap, ce que l'IA apporte, faisabilité, 1er contact recommandé | synthèse |
| 2 | Scientific question | reformulation + sous-questions 1–5, garde-fous | brief §1 |
| 3 | State of the art | tolérance opérationnelle (rein/foie vs cœur), Treg/Breg/NK, exhaustion, TCR/BCR, DSA/HLA, omics du rejet | PubMed peer-review |
| 4 | Systematic review | stratégie de recherche (bases, mots-clés A–D), PRISMA flow, tableau d'extraction par étude (variables listées brief §3) | registre `data/studies_registry.csv` |
| 5 | Meta-analysis | faisabilité quantitative ? si oui : effets aléatoires, I², sensibilité, sous-groupes, méta-régression, biais de publication, funnel. Sinon : justification + evidence synthesis | `meta-analysis/` |
| 6 | Existing datasets | GEO/SRA/ArrayExpress/EBI/dbGaP/EGA/ImmPort/BioStudies/Zenodo/Figshare… ; par dataset : ID, organisme, type, n échantillons/patients, longitudinal, contrôle, rejet/non-rejet, donneur/receveur, tissu, accès (Public / Controlled / Non public / À contacter), licence, lien, publication, limites | `data/datasets_registry.csv` |
| 7 | French research landscape | équipes FR : labo/service, institution, PI, expertise (Tx cardiaque / immuno / HLA / IS / biomarqueurs rejet / multi-omics / single-cell / bioinfo / IA), publis récentes, cohortes/biobanques, collaborations, coordonnées publiques, pourquoi bon partenaire | `data/french_teams.csv` + pages institutionnelles |
| 8 | Scientific gap | réponses explicites Q1–Q10 du brief §6 | synthèse sourcée |
| 9 | Proposed AI project | Aim 1 Data integration · Aim 2 Biomarker discovery · Aim 3 AI prediction (RF, XGBoost, Elastic Net, survival, NN, multimodal) ; CV / nested CV / calibration / validation externe / SHAP / robustesse | méthodo |
| 10 | Multi-omics strategy | comparaison 5 modèles : clinique seul → immuno → transcriptome → multi-omique → multimodal complet ; valeur ajoutée incrémentale | méthodo |
| 11 | Statistical methodology | endpoints (primary/secondary), missing data, batch effects, confounders, class imbalance, data leakage, multiple testing + FDR, validation externe, power/sample size ; **p >> n** → régularisation, sélection de variables stable, priors, réduction de dimension | méthodo |
| 12 | Validation strategy | par signature : gènes / voies / types cellulaires / clones T-B / protéines / mécanismes ; validations : cytométrie, qPCR, RNA-seq, single-cell, TCR/BCR, IHC, essais fonctionnels | méthodo |
| 13 | Feasibility | scénarios A / B / C (voir §5 ci-dessous) | analyse |
| 14 | Expected impact | hypothèses positive / intermédiaire / négative ; le négatif reste publiable | analyse |
| 15 | Potential publications | 3–5 articles : question, dataset, méthode, nouveauté, journal cible | plan |
| 16 | Potential French collaborators | shortlist raisonnée depuis §7 | synthèse |
| 17 | Recommended first contact | 1 équipe + justification | synthèse |
| 18 | Draft email — FR | court, pro, non commercial, personnalisé, propose échange 20–30 min | `outreach/email_fr.md` |
| 19 | Draft email — EN | idem | `outreach/email_en.md` |
| 20 | References | liste complète, PubMed/DOI, preprints étiquetés | `docs/references.md` |

En complément (brief §19) : **grille TOP 5** + **recommandation « une seule équipe »** +
**one-pager** (`outreach/one_pager.md`).

---

## 5. Scénarios de faisabilité (section 13)

| Axe | A — Minimal | B — Collaboration clinique | C — Translationnel |
|-----|-------------|---------------------------|--------------------|
| Données | datasets publics uniquement | publics + cohorte rétrospective 1 centre FR | cohorte multicentrique prospective + multi-omics |
| Objectif | proof-of-concept méthodologique, publication | développement + validation clinique | biomarqueur candidat + préparation validation prospective |
| n patients | *à estimer d'après §6* | *à estimer* | *à estimer* |
| Durée | *à estimer* | *à estimer* | *à estimer* |
| Ressources / infra / compétences | *à détailler* | *à détailler* | *à détailler* |
| Coûts principaux | *à détailler* | *à détailler* | *à détailler* |
| Réglementaire | usage secondaire données publiques | CPP / CNIL / MR-004, convention | RIPH, CPP, promoteur, ANSM le cas échéant |
| Faisabilité (côté MedFlow AI) | élevée | moyenne, dépend du partenaire | faible sans consortium |

## 6. Grille de scoring TOP 5 équipes françaises (section 19)

Pour chaque équipe, note /10 sur 6 axes + total pondéré :

| Axe | Poids proposé |
|-----|---------------|
| Score scientifique | 1.0 |
| Accès potentiel aux données | 1.5 |
| Expertise transplantation cardiaque | 1.25 |
| Expertise immunologie | 1.0 |
| Compatibilité IA / bioinformatique | 1.0 |
| Potentiel de collaboration (ouverture, taille, agenda) | 1.25 |

Stocké dans `data/french_teams_scoring.csv` ; rendu dans l'app en tableau trié + radar.

---

## 7. Application `app/app.py` — pages

1. **Accueil / Résumé** — question, garde-fous, schéma boucle *Clinical data → AI → biomarker → validation*.
2. **État de l'art** — synthèse sourcée, frise tolérance rein/foie/cœur.
3. **Revue systématique** — PRISMA flow + tableau d'études filtrable.
4. **Méta-analyse** — forest plot / funnel / I² (ou justification evidence synthesis).
5. **Datasets** — tableau filtrable par accès (Public / Controlled / Non public / À contacter).
6. **Paysage français** — carte + tableau des équipes, filtres par expertise.
7. **Gap & méthodologie** — Q1–Q10, Aims 1–3, comparaison 5 modèles, plan stat p>>n.
8. **Faisabilité** — scénarios A/B/C côte à côte.
9. **Collaboration** — apports respectifs, TOP 5 scoring + radar, recommandation.
10. **Prise de contact** — one-pager + emails FR/EN, bouton copie.

Thème : dark MedFlow AI (`.streamlit/config.toml`), typo Inter, accent violet `#8b5cf6`
(cohérent brand), sans réutiliser encore le logo v2 en prod tant que non validé.

---

## 8. Données à produire (fichiers `data/`)

| Fichier | Clé | Remplissage |
|---------|-----|-------------|
| `studies_registry.csv` | 1 ligne / étude incluse | screening manuel + `scripts/02` |
| `datasets_registry.csv` | 1 ligne / dataset | recherche repositories, `scripts/01` |
| `french_teams.csv` | 1 ligne / équipe | pages institutionnelles + PubMed affiliations |
| `french_teams_scoring.csv` | 1 ligne / équipe TOP candidates | scoring manuel argumenté |
| `meta_estimates.csv` | estimations poolées si méta-analyse | `scripts/03` |

Tous générés / mis à jour par script, jamais édités à la main (règle MedFlow AI).
