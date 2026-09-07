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
| **Controlled access — demande** | accord d'usage / DUA | CTOT03-PIENING-2022 (dépôt exact à localiser) |
| **Non public — collaboration nécessaire** | données de centre non déposées | INTERHEART-MMDX (ATAGC / Paris Transplant Group) ; cohorte rétrospective du partenaire (Scénario B) |

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
- **CTOT03-PIENING-2022** — Piening BD et al., *J Heart Lung Transplant* 2022;41(6):840–848
  (PubMed 35317953). RNA-seq (whole transcriptome) sur **125 biopsies** endomyocardiques,
  **26 receveurs** (jusqu'à 6 biopsies chacun, 12 premiers mois) → **longitudinal**.
  Cohorte **CTOT-03** (NCT00531921). Random forest ; signature pronostique 0R/1R → prédit
  la prochaine biopsie 2R/3R avec **~90 % de précision**. Accès probable sous **DUA** ;
  **localisation exacte des données brutes à confirmer** (GEO / SRA / dbGaP).
  *(Fusionne les ex-entrées « CTOT-03 » et « JHLT-2022-EMB » : c'était la même étude.)*
- **INTERHEART-MMDX** — biopsies cardiaques du consortium **INTERHEART** (NCT02670408) +
  biopsies de service, socle du système **MMDx-Heart** (Halloran ; 3230 biopsies dans
  l'analyse 2024, *Am J Transplant* 2024;24(8), PubMed 38527588). **Non public** — accès
  uniquement **via collaboration** (ATAGC U. Alberta / Paris Transplant Group). Plateforme
  microarray propriétaire.

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
