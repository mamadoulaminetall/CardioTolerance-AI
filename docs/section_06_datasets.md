# Section 6 — Données réellement disponibles

*CardioTolerance-AI · v1 (2026-09-03). Registre machine-lisible :
[`../data/datasets_registry.csv`](../data/datasets_registry.csv). **Statut « seed »** :
5 jeux de données identifiés par recherche web, chiffres et publications à confirmer
dataset par dataset. **Aucun dataset n'est inventé** ; les champs non vérifiés portent la
mention « à confirmer ».*

---

## 6.1 Classification par accessibilité (brief §4)

| Accès | Signification | Datasets (seed) |
|---|---|---|
| **Public — immédiat** | téléchargeable sans accord | GSE124897, GSE2445, GSE2596 (GEO) |
| **Controlled access — demande** | accord d'usage / DUA | CTOT-03 (ImmPort, à confirmer) |
| **Mentionné en publication, dépôt à localiser** | à retrouver / contacter les auteurs | JHLT-2022-EMB (whole transcriptome, biopsies prospectives) |
| **Non public — collaboration nécessaire** | données de centre non déposées | cohorte rétrospective du partenaire (Scénario B) ; MMDx-Heart complet |

## 6.2 Fiches (résumé — détail dans le CSV)

- **GSE124897** (GEO, *H. sapiens*) — microarray, **biopsies endomyocardiques**, ~841
  échantillons (≈ 645 stable / 52 TCMR / 144 ABMR — **à confirmer**). Associé aux travaux
  type MMDx-Heart. **Public.** Limites : phénotype histologique (variabilité
  inter-observateur), transversal, métadonnées cliniques limitées dans GEO.
- **GSE2445** (GEO) — microarray, biopsies **avant / pendant / après** rejet ; 14 patients
  (3 en microarray). **Public.** Limites : très petit effectif, plateforme ancienne.
  Intérêt : rare design **longitudinal** autour de l'épisode de rejet.
- **GSE2596** (GEO, GPL1053) — 16 rejet aigu / 27 non-rejet, biopsies. **Public.**
  Souvent utilisé comme **cohorte de validation externe** dans les réanalyses.
- **CTOT-03** — RNA-seq (bulk) sur biopsies endomyocardiques, ~125 biopsies, **26
  receveurs** (jusqu'à 6 biopsies chacun, 12 premiers mois) → **longitudinal**. Dépôt
  probable **ImmPort** (SDY à confirmer), accès probablement sous **DUA**. Design rare et
  précieux ; effectif patient modeste.
- **JHLT-2022-EMB** — *J Heart Lung Transplant* 2022, « Whole transcriptome profiling of
  prospective endomyocardial biopsies… prognostic and diagnostic signatures of cardiac
  allograft rejection ». Données brutes : **section Data Availability à vérifier** (GEO /
  EGA / dbGaP).

## 6.3 Ce qui manque dans les données publiques (et pourquoi la collaboration est nécessaire)

- **Aucun jeu public n'est pensé pour la *tolérance*** : tous sont construits autour du
  **rejet**. On peut définir la classe « absence durable de signal moléculaire de rejet »
  comme **proxy**, mais pas un phénotype clinique de stabilité profonde (IS minimale,
  absence de DSA de novo, recul long) → **métadonnées cliniques absentes**.
- **Peu de longitudinalité** (exceptions : GSE2445, CTOT-03).
- **Single-cell / snRNA-seq humain de biopsie cardiaque** : très rare (surtout murin) —
  voir Section 3.5.3.
- **Répertoire TCR/BCR de transplanté cardiaque** : non identifié en public.
- **Sang appairé + biopsie + HLA/DSA + suivi** : n'existe qu'en cohorte de centre.

## 6.4 Ce qui est faisable dès aujourd'hui (Scénario A)

Réanalyse harmonisée de **GSE124897 + GSE2596 + GSE2445** (± CTOT-03 si DUA obtenu) :
- pipeline de normalisation + correction de lot inter-dataset ;
- définition et caractérisation de la classe « no molecular rejection over time » ;
- test de transférabilité inter-dataset d'une signature de « quiescence » ;
- publication méthodologique (article 2 de la Section 15).

## 6.5 À faire (Phase 3 — suite)

- Vérifier **chaque** identifiant, effectif et publication sur GEO/ImmPort/EGA.
- Élargir la recherche : **ArrayExpress, SRA, dbGaP, EGA, BioStudies, Zenodo, Figshare**,
  mots-clés `cardiac allograft` + `single-cell` / `TCR` / `spatial` / `proteomics`.
- Chercher les jeux de **tolérance rénale/hépatique** (ITN, RISET, Nantes) réutilisables
  comme **comparateurs de méthode** (pas de transposition directe de signature).
- Explorer l'accès au registre **CRISTAL** (Agence de la biomédecine) pour la partie
  clinique/survie nationale.
