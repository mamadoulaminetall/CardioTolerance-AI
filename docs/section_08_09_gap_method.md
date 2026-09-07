# Sections 8–11 — Gap scientifique, projet IA, stratégie multi-omics, méthodologie statistique

*CardioTolerance-AI · v1 (2026-09-03). S'appuie sur
[`section_03_state_of_the_art.md`](section_03_state_of_the_art.md) et
[`section_04_systematic_review.md`](section_04_systematic_review.md). Références [Rxx] =
[`references.md`](references.md).*

> Garde-fou : identifier des **biomarqueurs et des profils de tolérance** à valider
> prospectivement. Le projet ne propose ni n'organise l'arrêt de l'immunosuppression.

---

# Section 8 — Gap scientifique (réponses Q1–Q10 du brief §6)

## Q1 — Qu'est-ce qui est déjà bien établi ?

1. **Épidémiologie** : une minorité de transplantés cardiaques ne présente jamais de
   rejet cliniquement significatif et reste indemne de CAV sur 10–20 ans [R2, R3].
2. **La tolérance opérationnelle existe et est biomarquée** en transplantation **hépatique
   et rénale**, avec des empreintes **organe-spécifiques** [R5, R6, R7, R8].
3. **Signature de tolérance rénale** : dominée par les transcrits **lymphocytes B**
   (MS4A1/CD20, TCL1A), reproductible entre cohortes (ITN, RISET, Nantes) [R5, R10, R17].
4. **Mécanisme TCR chez les tolérants** : **délétion clonale** des lymphocytes T
   donneur-réactifs ; répertoire moins biaisé [R19, R20].
5. **Caractérisation moléculaire du rejet cardiaque** : mature — **MMDx-Heart** (453
   transcrits associés au rejet, > 3 200 biopsies), panel Banff HOT pour l'AMR [R24, R25,
   R29].
6. **Détection non invasive du rejet cardiaque** : **AlloMap** (GEP sanguin, recommandé
   ISHLT) et **dd-cfDNA** (marqueur de lésion), avec méta-analyse pour le dd-cfDNA [R30,
   R31, R32].
7. **Rôle des DSA anti-HLA de novo** (surtout anti-DQ) dans l'AMR et la perte de greffon ;
   valeur du **mismatch HLA moléculaire** (eplets, PIRCHE-II) [R22, R23].
8. **Treg** : en préclinique, prolongation de survie de l'allogreffe cardiaque et
   prévention de la CAV ; thérapie Treg sûre en phase I/II (rein, foie) [R14, R16].

## Q2 — Qu'est-ce qui reste controversé ?

1. **Transposabilité inter-organes** d'une signature de tolérance : les empreintes
   foie/rein diffèrent [R8] → une signature « cardiaque » doit être découverte *de novo*,
   pas empruntée.
2. **Compartiment de mesure** : sang périphérique vs biopsie/tissu — lequel porte le
   signal de tolérance cardiaque ? Non tranché.
3. **Signature B de tolérance rénale** : sensible aux traitements et au contexte
   (déplétion B, DSA) ; sa robustesse et sa causalité restent discutées.
4. **Valeur ajoutée réelle des biomarqueurs non invasifs** au-delà de la clinique :
   performances hétérogènes selon les séries (dd-cfDNA), pas de standardisation [R31].
5. **Généralisation des modèles IA** : bons résultats internes, **chute en validation
   externe** (ex. pathologie DL 0,85 → 0,72) [R39] ; qualité méthodologique jugée
   sous-optimale [R38].
6. **Faisabilité clinique d'une minimisation guidée par biomarqueur** en cardiaque :
   aucun essai positif publié ; le retrait complet d'ICN reste risqué [R11, R13].

## Q3 — Qu'est-ce qui n'a pratiquement pas été étudié ?

**Preuve bibliométrique directe** (PubMed, 2026-09-07 — cf. §4.3bis) : la requête
*transplantation cardiaque* ∧ *tolérance* ∧ *IA/ML* renvoie **0 article** ;
*cœur* ∧ *tolérance* ∧ *multi-omics* n'en renvoie que **8**.

1. **Signature multi-omique de tolérance en transplantation cardiaque humaine** : absente.
2. **Données -omiques longitudinales humaines orientées *tolérance*** (vs rejet) dans le
   cœur : quasi nulles ; **scRNA-seq du rejet cardiaque surtout murin** [R35, R36] ;
   snRNA-seq de BEM humaines faisable mais rarissime [R37].
3. **Répertoire TCR/BCR chez le transplanté cardiaque stable à long terme** : non
   caractérisé (données humaines surtout rénales) [R21].
4. **Intégration multimodale** (clinique + HLA moléculaire + DSA + transcriptome +
   profil cellulaire + TCR/BCR) dans un même modèle cardiaque : jamais faite.
5. **Modèle IA *longitudinal*** prédisant la *trajectoire* du risque de rejet/tolérance
   (t0→t1→t2→t3) sur données cardiaques : inexistant.
6. **Épigénome / méthylation, protéome, métabolome, microbiome** en tolérance cardiaque :
   pratiquement rien.
7. **Phénotype « super-tolérant »** (stable, sans DSA, sans CAV, IS minimale, très long
   recul) : jamais défini opérationnellement ni profilé.

## Q4 — Existe-t-il réellement des preuves d'une tolérance immunologique exceptionnelle après transplantation cardiaque ?

**Preuve directe : non, à ce stade.** Aucune série de cas robuste de **sevrage complet et
durable** d'immunosuppression en greffe **cardiaque isolée** n'a été identifiée ; les
revues de tolérance en organe solide la décrivent « presque exclusivement » pour le foie
et le rein [R6, R8]. *(À confirmer formellement par la revue systématique — Phase 2 ;
inclure recherche ciblée de case reports, cohortes de non-observance, greffes combinées
cœur-rein/cœur-foie, protocoles de tolérance avec chimérisme.)*

**Preuve indirecte : oui, modérée.** (i) Une fraction de patients ne fait jamais de rejet
sur 20 ans [R3] ; (ii) la minimisation (sans corticoïdes ~40 % ; retrait progressif d'ICN
à l'étude) est possible chez des patients sélectionnés [R11, R12] ; (iii) les mécanismes
de tolérance (Treg, délétion clonale) opèrent dans les modèles cardiaques [R14, R15].
→ Il est **plausible** qu'existe un continuum de « tolérance relative / stabilité
immunologique profonde » non encore caractérisé — c'est l'hypothèse du projet.

## Q5 — Existe-t-il des patients ayant réussi une réduction majeure ou un sevrage de l'immunosuppression ?

- **Réduction majeure : oui.** Sevrage des corticoïdes courant (~40 % à long terme)
  [R11] ; protocoles de **retrait progressif d'ICN** en cours d'évaluation
  multicentrique de novo [R11] ; ECP + IS allégée sûre chez des patients à haut risque
  [R12].
- **Sevrage complet : pas de preuve solide** en greffe cardiaque isolée (voir Q4).
- **Donnée non disponible / à confirmer** : nombre de patients réellement sevrés, durée,
  devenir — à extraire en Phase 2.

## Q6 — Existe-t-il des biomarqueurs permettant de les identifier ?

- **En cardiaque, spécifiquement pour la *tolérance* : non.** Les biomarqueurs cardiaques
  validés (AlloMap, dd-cfDNA, MMDx) ciblent le **rejet / la lésion**, pas la tolérance
  [R24, R30, R31].
- **Candidats importables à tester** : signature B sanguine [R5, R17], score génique
  sanguin [R17], délétion clonale TCR [R19], faible charge de mismatch HLA moléculaire
  [R23], profil Treg (PD-1) [R15]. Aucun n'est validé en cardiaque.
- **AlloMap à score très bas / dd-cfDNA durablement indétectable** pourrait servir de
  **proxy de départ** d'un phénotype de stabilité — à évaluer.

## Q7 — Existe-t-il une signature transcriptomique, cellulaire, TCR/BCR ou multi-omique reproductible ?

- **Transcriptomique de *tolérance* reproductible : oui en rein** (signature B, plusieurs
  cohortes) [R5, R10] ; **non en cœur**.
- **Transcriptomique du *rejet* cardiaque : oui et robuste** (MMDx-Heart, > 3 200
  biopsies, multicentrique) [R25] — utile comme **cible négative** (définir la tolérance
  comme l'absence stable de signal de rejet moléculaire).
- **Cellulaire (scRNA-seq) reproductible en cœur humain : non** (surtout murin) [R35–R37].
- **TCR/BCR reproductible en cœur : non** (données humaines surtout rénales) [R20, R21].
- **Multi-omique intégrée reproductible en cœur : non**.

## Q8 — Les études existantes sont-elles suffisamment grandes pour développer de l'IA ?

- **Pour le *rejet* (biopsie) : oui.** MMDx-Heart et cohortes associées = milliers de
  biopsies ; datasets GEO publics (GSE124897 ~800+ biopsies) [R25 ; registre datasets].
- **Pour la *tolérance* cardiaque : non.** Pas de cohorte dédiée ; le phénotype n'est même
  pas défini. Les études de tolérance rénale portent sur des **dizaines** de patients
  tolérants au total [R5].
- **Pour un modèle *longitudinal multimodal* cardiaque : non** — il faudra **construire**
  la cohorte intégrée (Aim 1).

## Q9 — Quel est le principal obstacle ?

Par ordre d'importance :
1. **Absence de définition opérationnelle et de cohorte de phénotype « tolérance/stabilité
   profonde » en cardiaque** (le problème est d'abord conceptuel, pas algorithmique).
2. **Rareté des données -omiques longitudinales humaines** avec métadonnées cliniques
   riches (HLA, DSA, IS, biopsies) et suivi long.
3. **Hétérogénéité** : plateformes, définitions du rejet, régimes d'IS, centres.
4. **Absence de validation externe** dans les modèles publiés [R38, R39].
5. **Petits effectifs + très grande dimension (p ≫ n)** → surapprentissage (Section 11).
6. **Cadre réglementaire** de l'accès aux cohortes rétrospectives multi-omiques (CPP,
   CNIL/MR-004, conventions) — surmontable via collaboration.

## Q10 — Quelle contribution spécifique de l'IA / bioinformatique pourrait apporter une réelle nouveauté ?

1. **Définir le phénotype par les données** : clustering non supervisé multimodal pour
   isoler un/des sous-groupe(s) de « stabilité immunologique profonde » (pas un seuil
   arbitraire).
2. **Signature de tolérance cardiaque *de novo*** : découverte + sélection de variables
   **stable** (résampling), sur données humaines, avec **validation externe** sur cohorte
   ou dataset public indépendant.
3. **Cadre longitudinal** : modèles de trajectoire / survie dynamique / joint models —
   tester si le **changement temporel** des biomarqueurs prédit mieux que la valeur
   ponctuelle (landmark analysis) [Section 8, brief §8].
4. **Fusion multimodale quantifiée** : mesurer la **valeur ajoutée incrémentale** de
   chaque couche (clinique → +HLA/DSA → +transcriptome → +cellulaire/TCR → complet)
   (Section 10).
5. **Explicabilité orientée biologie** : SHAP + mapping gènes/voies/types
   cellulaires/clones → hypothèses mécanistiques testables (Section 12).
6. **Réutilisation de l'existant** : réanalyse harmonisée des grands jeux MMDx/GEO pour
   **définir la classe « absence durable de signal moléculaire de rejet »** comme ancre
   de la tolérance — faisable **dès aujourd'hui** sur données publiques (Scénario A).

**Nouveauté défendable** = première **caractérisation multi-omique et longitudinale, avec
validation externe, d'un phénotype de tolérance/stabilité profonde en transplantation
cardiaque humaine**, et un modèle IA qui en prédit la trajectoire.

---

# Section 9 — Projet IA proposé : « AI-driven discovery of immune tolerance signatures after heart transplantation »

## Aim 1 — Intégration des données (construire la cohorte intégrée)

**Objectif** : assembler, harmoniser et documenter une cohorte multimodale de
transplantés cardiaques, en maximisant les couches disponibles.

| Couche | Source (par scénario) | Harmonisation |
|---|---|---|
| Clinique longitudinale | centre partenaire (rétrospectif) ; registres | modèle de données commun (OMOP-like), dictionnaire de variables |
| Biopsies (histologie ISHLT + moléculaire) | centre ; MMDx si accessible ; **GEO GSE124897 / GSE2445 / GSE2596** | remap vers grades ISHLT harmonisés ; batch correction |
| HLA + mismatch moléculaire | typage centre → **eplets (HLA-EMMA), PIRCHE-II** | recalcul uniforme des scores |
| DSA (présence, MFI, spécificité, C1q si dispo) | labo HLA du centre / EFS | seuils harmonisés |
| Transcriptome (biopsie et/ou sang) | centre ; **CTOT-03** (RNA-seq longitudinal) ; datasets publics | normalisation, correction de lot (ComBat / RUV), contrôle qualité |
| Profil cellulaire (cytométrie / CyTOF) | centre si disponible | gating harmonisé / réanalyse |
| scRNA-seq / snRNA-seq | sous-échantillon prospectif (Scénario C) ; réanalyse publique | intégration (Harmony/scVI), annotation commune |
| TCR/BCR | sous-échantillon (Scénario B/C) | pipeline commun (MiXCR/Immcantation), métriques de diversité/clonalité |

**Livrables Aim 1** : jeu de données analytique versionné + fiche FAIR ; pipeline
reproductible (Snakemake/Nextflow, conteneurs) ; rapport de qualité (missingness, lots,
confusion).

**Définition du phénotype d'intérêt (préspécifiée, à affiner avec les cliniciens)** :
- *Stabilité profonde* : ≥ N années post-greffe, **aucun rejet ≥ 1R/pAMR1** documenté,
  **pas de DSA de novo**, **pas de CAV significative** (ISHLT CAV ≤ 1), fonction stable,
  **IS à exposition minimale** selon le protocole du centre.
- *Rejet* : ≥ 1 épisode TCMR ≥ 2R et/ou AMR prouvé.
- *Intermédiaire* : le reste.
- Ancre moléculaire complémentaire : **absence durable de signal MMDx de rejet** [R25].

## Aim 2 — Découverte de signatures (biomarker discovery)

- **Non supervisé d'abord** : réduction de dimension par couche (PCA/UMAP, MOFA+ pour le
  multi-omique) puis **clustering multimodal** (similarity network fusion, MOFA factors,
  clustering consensus) → tester l'existence de sous-groupes de tolérance/stabilité.
- **Supervisé ensuite** : modèles pénalisés (**Elastic Net**, group-lasso par couche),
  **Random Forest / XGBoost** avec importance par permutation, pour discriminer
  rejet / stabilité / stabilité profonde.
- **Sélection de variables stable** : résampling (bootstrap/subsampling) + **stability
  selection**, seuil de sélection préspécifié ; rapporter la fréquence de sélection.
- **Signature = petit panel** (transcrits, scores cellulaires, métriques TCR/BCR, score
  de mismatch) reproductible, testé en **validation externe** (dataset/cohorte
  indépendants).
- **Cibles négatives** : la « tolérance » est aussi définie comme **absence stable** de
  signature de rejet — éviter le raisonnement circulaire (leakage histologie→moléculaire).

## Aim 3 — Prédiction par IA

**Familles de modèles à comparer** (mêmes splits, même préprocessing) :
- Régularisés : **Elastic Net** (classification et Cox).
- Ensembles d'arbres : **Random Forest**, **XGBoost** (+ survie : RSF, XGBoost-AFT).
- **Modèles de survie** : Cox pénalisé, **Random Survival Forest**, DeepSurv *si* n le
  justifie.
- **Réseaux de neurones / multimodaux** : fusion tardive (concat d'embeddings par
  couche) ; **uniquement si** la taille d'échantillon le permet (sinon s'en tenir aux
  modèles pénalisés — cf. Section 11 et brief §8/§18).
- **Baselines obligatoires** : score clinique seul ; règle « AlloMap bas + dd-cfDNA
  indétectable ».

**Évaluation (systématique)** :
- **Nested cross-validation** (boucle externe = estimation non biaisée, boucle interne =
  réglage) ; répétée ; **groupes = patients** (jamais une biopsie du même patient des
  deux côtés du split).
- Métriques : AUROC, AUPRC (classes déséquilibrées), **C-index** et **time-dependent
  AUC / Brier** pour la survie.
- **Calibration** : courbes + calibration slope/intercept ; recalibration si besoin.
- **Validation externe** : dataset public ou 2ᵉ centre — critère de succès principal.
- **Explicabilité** : SHAP (global + local), stabilité des attributions ; cohérence
  biologique (Section 12).
- **Robustesse** : sensibilité au batch, aux valeurs manquantes, au centre, au régime
  d'IS ; analyses en sous-groupes préspécifiées.

**Livrables Aim 3** : tableau comparatif des modèles ; modèle retenu + carte de
calibration ; rapport SHAP ; code + poids versionnés ; **rapport TRIPOD+AI**.

---

# Section 10 — Stratégie multi-omics (comparaison incrémentale)

Combinaison cible : **clinique + HLA/mismatch moléculaire + DSA + transcriptome +
profil cellulaire + TCR/BCR** (brief §9).

Protocole de comparaison, **mêmes patients, mêmes splits, même métrique** :

| Modèle | Entrées | Question |
|---|---|---|
| M1 — clinique seul | démographie, IS, fonction, délais, CAV, DSA binaire | référence pragmatique |
| M2 — immunologique | M1 + DSA détaillés + mismatch HLA moléculaire (eplets, PIRCHE-II) | l'immuno « facile à obtenir » suffit-elle ? |
| M3 — transcriptomique | transcriptome (biopsie et/ou sang) seul | signal moléculaire pur |
| M4 — multi-omique | M2 + M3 + profil cellulaire | gain de l'ajout du tissu/cellulaire |
| M5 — multimodal complet | M4 + TCR/BCR (+ single-cell si dispo) | gain du répertoire immun |

- **Critère** : amélioration de l'AUROC/C-index **en validation externe** avec IC (test
  de DeLong / bootstrap apparié), + **reclassification** (NRI/IDI) et **courbes de
  décision** (net benefit).
- **Analyse de coût-information** : gain prédictif rapporté au coût/invasivité de chaque
  couche → recommandation d'un panel « minimal suffisant ».
- **Attendu réaliste** : il est possible que M2 ou M3 capturent l'essentiel et que
  M4/M5 n'apportent qu'un gain marginal — **résultat publiable dans les deux sens**
  (Section 14).

---

# Section 11 — Méthodologie statistique (plan préspécifié)

## Endpoints

- **Primary** : discrimination du **phénotype de stabilité profonde** (vs rejet /
  intermédiaire) à un temps de référence (landmark), mesurée par **AUROC en validation
  externe**.
- **Secondary** : (i) prédiction du **temps jusqu'au premier rejet** (C-index,
  time-dependent AUC) ; (ii) valeur ajoutée incrémentale des couches -omiques (Section
  10) ; (iii) stabilité et interprétabilité de la signature ; (iv) association de la
  signature avec survie du greffon / événements CV (exploratoire).

## Pièges spécifiques et parades

| Problème | Parade préspécifiée |
|---|---|
| **p ≫ n** (grande dimension, petit n) | filtrage a priori (variance, expression) ; réduction par couche (PCA/MOFA) ; modèles **pénalisés** en 1ʳᵉ intention ; **stability selection** ; pas de deep learning si n insuffisant (règle EPV/►taille min. préspécifiée) |
| **Data leakage** | splits **par patient** ; tout le préprocessing (imputation, sélection, batch) **dans la boucle CV** ; séparer histologie (définit le label) et features moléculaires |
| **Batch effects** | plan d'analyse des lots ; ComBat / RUV / covariables de lot ; vérifier que le « centre » n'est pas prédicteur du label ; validation **cross-centre** |
| **Confounders** | ajustement sur âge, délai post-greffe, régime d'IS, fonction rénale, indication ; analyses stratifiées ; g-computation exploratoire |
| **Class imbalance** | AUPRC en plus de l'AUROC ; rééchantillonnage **dans la boucle interne** uniquement ; class weights ; seuils choisis sur la boucle interne |
| **Multiple testing** | contrôle du **FDR (Benjamini-Hochberg)** pour la découverte ; hypothèses primaires préspécifiées et limitées |
| **Overfitting d'optimisme** | **nested CV** répétée ; validation externe obligatoire ; rapport de l'écart interne↔externe |
| **Missing data** | quantifier et cartographier ; imputation multiple (MICE) ou par couche (KNN/softImpute) **dans la CV** ; analyses de sensibilité complete-case ; couche omise si missingness > seuil |
| **Petit nombre d'événements** | privilégier endpoints fréquents ; Firth/pénalisation ; ne pas multiplier les modèles complexes |

## Puissance / taille d'échantillon

- Calcul **préspécifié** selon le scénario (Section 13) : pour une signature
  discriminante attendue AUROC ~0,75–0,85, viser un **n d'événements** suffisant (EPV ≥
  10–20 pour les modèles pénalisés ; règles de Riley et al. pour les modèles de
  prédiction).
- **Donnée non disponible / à confirmer** : prévalence exacte du phénotype cible dans la
  cohorte partenaire → conditionne le n total. À estimer avec le centre lors du premier
  échange.

## Reproductibilité & reporting

Pipelines conteneurisés (Snakemake/Nextflow) ; graines fixées ; données et modèles
versionnés (DVC/git-annex) ; **rapport selon TRIPOD+AI** ; risque de biais **PROBAST** ;
code publié ; plan d'analyse figé avant l'accès aux données de validation externe.

---

# Section 12 — Stratégie de validation biologique

**Principe** : aucune signature n'est présentée comme résultat tant qu'elle n'a pas de
**lecture biologique** et une **confirmation sur échantillon indépendant**. L'IA produit
des hypothèses, pas des conclusions.

## 12.1 Annotation mécanistique de chaque signature retenue

Pour tout panel sélectionné (transcrits, scores cellulaires, métriques TCR/BCR, score de
mismatch) :
- **Gènes** : fonction, appartenance à des modules connus (quiescence, co-stimulation,
  épuisement, régulation B, réponse interféron, fibrose) ; recoupement avec les
  transcrits associés au rejet (MMDx RATs [R24]) — la tolérance doit s'en **distinguer**,
  pas juste être « moins de rejet ».
- **Voies** : enrichissement (GSEA / ORA, FDR contrôlé) ; réseaux de régulation.
- **Types cellulaires** : déconvolution (CIBERSORTx / BisqueRNA) sur le bulk ;
  confirmation sur single-cell/snRNA-seq quand disponible ; localisation (spatial, si
  accès via ex. l'équipe de Lyon).
- **Clones T/B** : diversité, clonalité, expansion/contraction, partage inter-patients ;
  recherche de motifs CDR3 publics ; lien avec le mismatch HLA.
- **Protéines** : correspondance transcrit→protéine (si sérothèque / Olink accessible).

## 12.2 Confirmation expérimentale (avec le centre partenaire — Scénario B/C)

| Signal à confirmer | Technique | Échantillon |
|---|---|---|
| Sur-/sous-expression de transcrits clés | **qPCR** ciblée / NanoString | biopsie ou sang appariés, cohorte de confirmation |
| Proportions de sous-populations (Treg, Breg, NK, T épuisés) | **cytométrie de flux / spectrale**, CyTOF | sang (± digestat de biopsie) |
| Localisation intra-greffon | **IHC / immunofluorescence multiplex** | blocs FFPE de biopsie |
| Hétérogénéité cellulaire fine | **scRNA-seq / snRNA-seq** ciblé | sous-échantillon prospectif |
| Répertoire immun | **séquençage TCR/BCR** (MiXCR/Immcantation) | sang ± tissu |
| Fonction régulatrice | **essais de suppression Treg**, réponse allogénique in vitro (MLR) | PBMC, si pertinent et faisable |

## 12.3 Critères de succès de la validation
1. **Réplication** du sens de l'effet sur une **cohorte de confirmation indépendante**
   (interne au centre ou 2ᵉ centre).
2. **Cohérence multimodale** : le signal transcriptomique correspond à un signal
   cellulaire/protéique plausible.
3. **Association clinique** : la signature (ou son évolution) est associée aux outcomes
   (temps jusqu'au rejet, DSA de novo, CAV) après ajustement.
4. **Spécificité** : la signature n'est pas un simple reflet de l'exposition
   médicamenteuse ou de la fonction rénale (analyses de confusion, Section 11).

## 12.4 Garde-fou clinique
Une signature validée **n'autorise aucune modification thérapeutique**. Elle ne peut
servir qu'à **concevoir une étude prospective** de minimisation contrôlée et supervisée,
avec comité de surveillance indépendant — hors du périmètre de ce projet.
