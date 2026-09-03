# Sections 13–15 — Faisabilité, impact attendu, stratégie de publication

*CardioTolerance-AI · v1 (2026-09-03). Les chiffres (n patients, durées, coûts) sont des
**ordres de grandeur à confirmer** avec l'équipe partenaire — ils ne reposent sur aucune
donnée interne et devront être révisés au premier échange. Rien n'est présenté comme
acquis.*

---

# Section 13 — Faisabilité selon trois scénarios

## Vue synthétique

| Axe | **A — Minimal** | **B — Collaboration clinique** | **C — Translationnel** |
|---|---|---|---|
| Données | datasets **publics** uniquement (GEO/ImmPort : biopsies cardiaques transcriptome) | publics **+ cohorte rétrospective** 1 centre FR (clinique + biopsies + HLA/DSA ± transcriptome) | **cohorte multicentrique prospective** + multi-omics dédié (biopsie + sang + single-cell + TCR/BCR) |
| Objectif | proof-of-concept méthodologique ; définir la classe « absence durable de signal moléculaire de rejet » ; 1 publication méthodo | découverte **+ validation clinique** d'une signature de tolérance/stabilité ; 1–2 publications | **biomarqueur candidat** qualifié + préparation d'une validation prospective / essai de minimisation guidée |
| n patients (ordre de grandeur, **à confirmer**) | n/a (réutilisation ; ~10³ biopsies agrégées disponibles publiquement) | ~150–400 receveurs rétrospectifs d'un centre à fort volume, dont un sous-groupe « très stable » possiblement faible (**prévalence à estimer**) | ~500–1 000 patients multicentriques, suivi longitudinal ≥ 3–5 ans |
| Durée | 6–12 mois | 18–30 mois | 4–6 ans |
| Ressources humaines | 1 bioinformaticien/IA (MedFlow AI) + relecture clinique ponctuelle | + 1 ARC/data manager côté centre, 1 immunologiste référent, temps pathologiste | + coordination multicentrique, plateaux single-cell/TCR, biostatisticien dédié, chef de projet |
| Infrastructure | poste calcul GPU modeste / cloud ; stockage ~1–5 To | + accès sécurisé aux données du centre (enclave / SFTP chiffré), environnement conforme | + LIMS/biobanque, plateforme séquençage, entrepôt de données de santé |
| Coûts principaux (**estimations grossières à valider**) | calcul/stockage + temps chercheur : **faible** (quelques k€) | + data management, extraction, éventuel séquençage de rattrapage ciblé : **dizaines de k€** | + séquençage multi-omique prospectif, single-cell, coordination : **plusieurs centaines de k€** (financement type ANR / PHRC / Fondation) |
| Réglementaire | usage secondaire de données publiques anonymisées (revue éthique légère) | **CPP** + **CNIL / MR-004**, convention de collaboration, information des patients selon le cadre rétrospectif | **RIPH** (catégorie à définir), CPP, promoteur institutionnel, éventuellement ANSM, comité de biobanque |
| Risques clés | signal de tolérance peut ne pas être présent dans des données pensées pour le rejet | prévalence du phénotype cible trop faible ; données -omiques absentes ou hétérogènes | financement, durée, attrition, complexité de coordination |
| Faisabilité (côté MedFlow AI, aujourd'hui) | **élevée** — démarrable immédiatement | **moyenne** — dépend d'un partenaire et de la gouvernance données | **faible seul** — nécessite un consortium et un financement dédié |

## Séquencement recommandé

**A → B → C**, avec chevauchement : livrer **A** comme carte de visite (preuve de méthode,
publiable seul), enclencher **B** avec le partenaire dès que l'accès aux données est
cadré, et n'écrire **C** (dossier de financement) qu'une fois une signature candidate
obtenue en B. Ne jamais faire dépendre l'existence du projet de C.

## Points à clarifier au premier échange avec le centre

1. Prévalence réelle, dans leur file active, du phénotype « très stable » préspécifié
   (§9) → conditionne le n et donc la puissance.
2. Modalités -omiques déjà disponibles rétrospectivement (transcriptome de biopsie ?
   sérothèque ? ADN pour typage HLA haute résolution ?).
3. Gouvernance des données : enclave sécurisée, delais CPP/CNIL, personne référente.
4. Attentes de co-signature / rôle scientifique de chaque partie.

---

# Section 14 — Impact et résultats attendus

Le projet est **conçu pour être informatif quel que soit le résultat** (brief §13).

### Hypothèse positive — signature reproductible de tolérance/stabilité profonde
- **Résultat** : un panel multi-omique compact discrimine, en **validation externe**, les
  receveurs « très stables » des profils de rejet, et sa **trajectoire** prédit le risque.
- **Impact** : premier candidat-biomarqueur de tolérance en greffe cardiaque humaine ;
  base d'un essai prospectif de **minimisation guidée** (sous supervision médicale
  stricte, jamais d'arrêt) ; publication à fort impact.

### Hypothèse intermédiaire — plusieurs phénotypes immunologiques
- **Résultat** : pas une signature unique mais **2–3 sous-groupes** de stabilité
  (p. ex. « quiescence T », « profil régulateur B », « faible charge antigénique HLA »).
- **Impact** : reconceptualise la « tolérance cardiaque » comme hétérogène ; oriente des
  stratégies de suivi différenciées ; publication solide + hypothèses mécanistiques.

### Hypothèse négative — pas de signature robuste
- **Résultat** : aucune signature ne généralise ; la stabilité clinique n'a pas de
  corrélat -omique reproductible détectable avec les données disponibles.
- **Impact (réel et publiable)** : démontre les **limites des biomarqueurs actuels** et
  des tailles de cohorte, quantifie le signal maximal atteignable, et **cadre les
  besoins** (longitudinalité, single-cell, multicentrique) pour la communauté — utile
  pour éviter des essais de minimisation prématurés.

### Valeur méthodologique transverse (dans tous les cas)
Pipeline reproductible d'intégration multi-omique + IA avec validation externe et
reporting TRIPOD+AI, réutilisable pour d'autres organes / questions de tolérance.

---

# Section 15 — Stratégie de publication (3–5 articles)

| # | Question | Dataset | Méthode | Nouveauté | Journal cible (à confirmer) |
|---|---|---|---|---|---|
| 1 | Que sait-on des signatures de tolérance et de la prédiction du rejet en transplantation cardiaque ? | littérature (revue systématique) | systematic review + evidence synthesis ; méta-analyse ciblée dd-cfDNA (QUADAS-2, bivarié/HSROC) | 1ʳᵉ synthèse centrée *tolérance* cardiaque + cartographie datasets/équipes | *J Heart Lung Transplant* ; *Transplant Rev* ; *Am J Transplant* |
| 2 | Peut-on définir, sur données publiques, une classe « absence durable de signal moléculaire de rejet » et une méthode de découverte de signature ? | GEO/ImmPort (biopsies cardiaques transcriptome) | réanalyse harmonisée, clustering multimodal, stability selection, validation croisée inter-dataset | proof-of-concept méthodologique reproductible (Scénario A) | *Bioinformatics* ; *Front Immunol* ; *Sci Rep* |
| 3 | Existe-t-il une signature multi-omique de tolérance/stabilité profonde chez des receveurs cardiaques réels ? | cohorte rétrospective 1 centre FR + publics | intégration multimodale, modèles pénalisés/ensembles, SHAP, validation externe | 1ʳᵉ signature de tolérance en greffe cardiaque humaine (Scénario B) | *Am J Transplant* ; *Circulation* ; *JACC* |
| 4 | La signature est-elle biologiquement et cliniquement valide ? | échantillons du centre | cytométrie/qPCR/IHC/single-cell ciblés (Section 12) + association aux outcomes | validation biologique + clinique de la signature | *Am J Transplant* ; *J Clin Invest Insight* |
| 5 | Peut-on prédire prospectivement la trajectoire du risque et préparer une minimisation guidée ? | cohorte prospective multicentrique (Scénario C) | modèles longitudinaux/joint models, landmark analysis, calibration prospective | cadre prédictif longitudinal validé prospectivement | *NEJM Evid* ; *Lancet* ; *Circulation* |

Articles 1 et 2 sont réalisables **sans partenaire clinique** et servent de socle de
crédibilité pour engager 3–5.
