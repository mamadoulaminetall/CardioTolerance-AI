# Brief source — prompt d'origine (verbatim)

> Ce fichier conserve, sans modification, le prompt fondateur du projet transmis par
> Dr. Mamadou Lamine TALL le 2026-09-03. Il sert de cahier des charges de référence.
> Toute la production (`docs/`, `app/`, `meta-analysis/`, `outreach/`) doit y rester conforme.

---

# Prompt — Projet de recherche IA / Bioinformatique sur la tolérance immunologique après transplantation cardiaque

## Rôle

Agis comme une équipe multidisciplinaire composée de :

* un chercheur senior en transplantation cardiaque ;
* un immunologiste spécialisé en immunologie de transplantation ;
* un bioinformaticien expert en multi-omics ;
* un chercheur en machine learning / deep learning appliqué aux données biomédicales ;
* un méthodologiste spécialisé en systematic reviews et méta-analyses ;
* un expert en conception de projets de recherche translationnelle et en montage de collaborations académiques.

L'objectif est de construire une **proposition de recherche scientifique réaliste, originale et suffisamment solide pour être présentée à un centre français de transplantation cardiaque ou à une équipe académique spécialisée**, dans le cadre d'une potentielle collaboration avec un chercheur/PhD en bioinformatique et IA.

---

# 1. Question scientifique centrale

Étudier s'il existe, chez certains patients ayant reçu une transplantation cardiaque, une **signature immunologique, moléculaire, cellulaire ou multi-omique associée à une tolérance particulièrement élevée du greffon**, et déterminer si l'intelligence artificielle peut permettre :

1. d'identifier cette signature ;
2. de distinguer les patients présentant un rejet des patients présentant une stabilité durable ;
3. d'identifier des profils compatibles avec une forme de tolérance immunologique exceptionnelle ;
4. de prédire longitudinalement l'évolution du risque de rejet ;
5. à terme, d'identifier les patients susceptibles d'être candidats à une réduction contrôlée et médicalement supervisée de l'immunosuppression.

Attention : le projet ne doit jamais supposer qu'un patient peut arrêter ses immunosuppresseurs. L'objectif scientifique est d'identifier des biomarqueurs et des profils de tolérance pouvant éventuellement être validés prospectivement.

---

# 2. Recherche bibliographique approfondie

Effectue une recherche bibliographique aussi exhaustive que possible sur :

### A. Tolérance après transplantation cardiaque

Rechercher les concepts :

* operational tolerance
* immune tolerance
* spontaneous tolerance
* immunological tolerance
* cardiac allograft tolerance
* heart transplant tolerance
* long-term heart transplant survivors
* immunosuppression minimization
* immunosuppression withdrawal
* rejection-free heart transplant recipients

### B. Signatures immunologiques

Rechercher notamment :

* Treg
* regulatory T cells
* B cells
* regulatory B cells
* NK cells
* T-cell exhaustion
* T-cell repertoire
* TCR sequencing
* BCR sequencing
* donor-specific antibodies
* DSA
* HLA
* cytokines
* chemokines
* immune cell profiling
* flow cytometry
* mass cytometry
* immune transcriptomics

### C. Multi-omics

Rechercher :

* RNA-seq
* single-cell RNA-seq
* scRNA-seq
* spatial transcriptomics
* epigenomics
* methylation
* proteomics
* metabolomics
* microbiome
* multi-omics
* longitudinal omics
* transplant immunology omics

### D. IA / Machine Learning

Rechercher :

* artificial intelligence
* machine learning
* deep learning
* survival models
* longitudinal machine learning
* multimodal learning
* multi-omics machine learning
* explainable AI
* biomarker discovery
* rejection prediction
* transplant outcome prediction

---

# 3. Revue systématique et méta-analyse

Détermine s'il existe suffisamment de littérature pour réaliser une **méta-analyse quantitative**.

Ne te contente pas d'une revue narrative.

Pour chaque étude pertinente, extrais si disponible :

* année ;
* pays ;
* centre ;
* taille de cohorte ;
* type de transplantation ;
* âge ;
* durée du suivi ;
* régime immunosuppresseur ;
* définition du rejet ;
* type de rejet ;
* nombre de patients avec rejet ;
* nombre de patients sans rejet ;
* présence de DSA ;
* HLA ;
* biopsies ;
* transcriptomique ;
* single-cell ;
* TCR/BCR ;
* cytométrie ;
* protéomique ;
* autres biomarqueurs ;
* mortalité ;
* survie du greffon ;
* événements cardiovasculaires ;
* réduction ou arrêt des immunosuppresseurs ;
* cas de tolérance documentée.

Pour les études quantitatives, extrais les mesures d'effet disponibles :

* Hazard Ratio ;
* Odds Ratio ;
* Risk Ratio ;
* différence moyenne ;
* corrélation ;
* AUC ;
* sensibilité ;
* spécificité ;
* C-index ;
* autres métriques prédictives.

Lorsque les données le permettent, réalise une méta-analyse avec :

* modèle à effets aléatoires ;
* estimation de l'hétérogénéité ;
* I² ;
* analyse de sensibilité ;
* subgroup analysis ;
* meta-regression lorsque pertinente ;
* publication bias ;
* funnel plot lorsque suffisamment d'études sont disponibles.

Si une méta-analyse quantitative n'est PAS méthodologiquement justifiable, explique précisément pourquoi et propose une **systematic review + evidence synthesis** alternative.

Ne fabrique aucune donnée manquante.

---

# 4. Recherche de données réelles disponibles

Identifie les **datasets réellement accessibles** pouvant permettre de développer le projet.

Cherche notamment :

### Bases publiques

* GEO
* SRA
* ArrayExpress
* EMBL-EBI
* dbGaP
* EGA
* ImmPort
* BioStudies
* Zenodo
* Figshare
* NIH repositories
* UK Biobank lorsque pertinent
* autres biobanques ou repositories spécialisés.

Rechercher spécifiquement les datasets contenant :

* heart transplantation ;
* cardiac allograft ;
* transplant rejection ;
* heart biopsy ;
* donor-specific antibodies ;
* TCR/BCR ;
* single-cell ;
* RNA-seq ;
* immune profiling.

Pour chaque dataset trouvé, fournir :

* identifiant ;
* organisme ;
* type de données ;
* nombre d'échantillons ;
* nombre de patients si disponible ;
* données longitudinales ou non ;
* présence d'un groupe contrôle ;
* présence de rejet ;
* présence de non-rejet ;
* données donneur/receveur ;
* type de tissu ;
* disponibilité réelle ;
* licence/accessibilité ;
* lien officiel ;
* publication associée ;
* limites.

**Ne jamais inventer l'existence d'un dataset.**

Distingue clairement :

**Public → accessible immédiatement**

**Controlled access → demande d'accès nécessaire**

**Non public → collaboration nécessaire**

**Mentionné dans une publication mais dataset non disponible → à contacter**

---

# 5. Recherche des cohortes et équipes françaises

Identifier les équipes françaises ayant une expertise dans :

* transplantation cardiaque ;
* immunologie de transplantation ;
* histocompatibilité/HLA ;
* immunosuppression ;
* biomarqueurs du rejet ;
* multi-omics ;
* single-cell ;
* bioinformatique ;
* intelligence artificielle appliquée à la transplantation.

Rechercher en priorité :

* AP-HP ;
* Inserm ;
* CNRS ;
* Universités ;
* CHU ;
* instituts de recherche ;
* laboratoires de génomique ;
* centres de transplantation cardiaque.

Pour chaque équipe pertinente, fournir :

* nom du laboratoire/service ;
* institution ;
* chercheurs principaux ;
* expertise ;
* publications récentes ;
* travaux spécifiquement liés à la transplantation ;
* travaux liés à l'immunologie ;
* travaux liés à l'IA/bioinformatique ;
* cohortes disponibles ou potentielles ;
* biobanques ;
* collaborations existantes ;
* coordonnées institutionnelles publiques lorsque disponibles ;
* raisons scientifiques pour lesquelles cette équipe serait un bon partenaire.

Prioriser les équipes dont les travaux récents démontrent une réelle activité dans le domaine.

---

# 6. Identification du GAP scientifique

À partir de la littérature et des données disponibles, réponds précisément :

### Question 1

Qu'est-ce qui est déjà bien établi ?

### Question 2

Qu'est-ce qui reste controversé ?

### Question 3

Qu'est-ce qui n'a pratiquement pas été étudié ?

### Question 4

Existe-t-il réellement des preuves d'une tolérance immunologique exceptionnelle après transplantation cardiaque ?

### Question 5

Existe-t-il des patients ayant réussi une réduction majeure ou un sevrage de l'immunosuppression ?

### Question 6

Existe-t-il des biomarqueurs permettant de les identifier ?

### Question 7

Existe-t-il une signature transcriptomique, cellulaire, TCR/BCR ou multi-omique reproductible ?

### Question 8

Les études existantes sont-elles suffisamment grandes pour développer de l'IA ?

### Question 9

Quel est le principal obstacle : manque de données, hétérogénéité, faible nombre de patients, absence de longitudinalité, absence de validation externe, etc. ?

### Question 10

Quelle contribution spécifique de l'IA/bioinformatique pourrait apporter une réelle nouveauté ?

---

# 7. Proposition scientifique

À partir des résultats précédents, construis un projet intitulé provisoirement :

**"AI-driven discovery of immune tolerance signatures after heart transplantation"**

Propose :

## Aim 1 — Data integration

Construire une cohorte intégrée comprenant autant que possible :

* données cliniques ;
* données longitudinales ;
* biopsies ;
* HLA ;
* DSA ;
* cytométrie ;
* transcriptomique ;
* single-cell ;
* TCR/BCR ;
* protéomique ;
* autres données immunologiques.

## Aim 2 — Biomarker discovery

Identifier les signatures moléculaires et cellulaires associées à :

* rejet ;
* stabilité ;
* excellente tolérance ;
* éventuelle tolérance opérationnelle.

## Aim 3 — AI prediction

Développer des modèles :

* Random Forest ;
* XGBoost ;
* Elastic Net ;
* survival models ;
* neural networks ;
* modèles multimodaux si la quantité de données le permet.

Comparer les performances.

Inclure systématiquement :

* cross-validation ;
* nested cross-validation lorsque nécessaire ;
* calibration ;
* external validation ;
* explainability ;
* SHAP ou méthodes similaires ;
* analyse de robustesse.

---

# 8. Approche longitudinale

Ne considère pas uniquement une photographie du patient.

Propose un modèle dynamique :

**Patient t0 → t1 → t2 → t3 → évolution immunologique → risque de rejet/tolérance**

Étudier si les changements temporels des biomarqueurs sont plus prédictifs que leur valeur à un instant donné.

Explorer notamment :

* trajectories ;
* time-series models ;
* dynamic survival models ;
* recurrent neural networks si justifiées ;
* temporal transformers si la taille du dataset le permet ;
* joint models ;
* landmark analysis.

Ne propose pas de deep learning complexe si la taille de cohorte ne le justifie pas.

---

# 9. Multi-omics

Déterminer quelle combinaison serait scientifiquement et techniquement la plus pertinente :

**HLA + DSA + transcriptome + immune-cell profiling + TCR/BCR + clinical data**

Comparer :

1. modèle clinique seul ;
2. modèle immunologique ;
3. modèle transcriptomique ;
4. modèle multi-omique ;
5. modèle multimodal complet.

L'objectif est de démontrer si l'intégration des différentes modalités apporte réellement une valeur prédictive supplémentaire.

---

# 10. Validation biologique

L'IA ne doit pas seulement produire une "black box".

Pour chaque signature identifiée :

* identifier les gènes ;
* voies biologiques ;
* types cellulaires ;
* clones T/B ;
* protéines ;
* mécanismes immunologiques potentiels.

Proposer ensuite des validations :

* cytométrie ;
* qPCR ;
* RNA-seq ;
* single-cell ;
* TCR/BCR ;
* immunohistochimie ;
* expériences fonctionnelles lorsque pertinentes.

---

# 11. Faisabilité

Évaluer le projet selon trois scénarios.

### Scénario A — Minimal

Utilisation uniquement de datasets publics.

Objectif : publication méthodologique/proof-of-concept.

### Scénario B — Collaboration clinique

Datasets publics + cohorte rétrospective d'un centre français.

Objectif : développement + validation clinique.

### Scénario C — Projet translationnel

Cohorte multicentrique prospective + multi-omics + IA.

Objectif : biomarqueur candidat et préparation d'une validation prospective.

Pour chaque scénario, préciser :

* nombre approximatif de patients nécessaire ;
* données nécessaires ;
* durée ;
* ressources ;
* compétences ;
* infrastructures ;
* coûts principaux ;
* difficultés réglementaires ;
* faisabilité.

---

# 12. Design statistique

Proposer un plan statistique complet.

Inclure :

* définition des endpoints ;
* primary endpoint ;
* secondary endpoints ;
* gestion des données manquantes ;
* batch effects ;
* confounders ;
* class imbalance ;
* data leakage ;
* multiple testing ;
* correction FDR ;
* validation externe ;
* power/sample-size considerations.

Attention particulière au problème :

**petite cohorte + très grand nombre de variables.**

Proposer des méthodes permettant de limiter le surapprentissage.

---

# 13. Résultats attendus

Définir les résultats potentiels :

### Hypothèse positive

Identification d'une signature reproductible de tolérance.

### Hypothèse intermédiaire

Identification de plusieurs phénotypes immunologiques différents.

### Hypothèse négative

Absence de signature robuste.

Même un résultat négatif doit être considéré comme scientifiquement exploitable s'il permet de démontrer les limites des biomarqueurs actuels.

---

# 14. Publications potentielles

Proposer une stratégie de publication en 3–5 articles potentiels :

1. systematic review/meta-analysis ;
2. public-data multi-omics study ;
3. AI biomarker discovery ;
4. validation clinique ;
5. prospective translational study.

Pour chaque article :

* question ;
* dataset ;
* méthode ;
* nouveauté ;
* journal cible potentiel.

---

# 15. Proposition de collaboration

Construire ensuite une proposition destinée à un laboratoire/centre français.

Elle doit expliquer clairement :

### Ce que le chercheur en bioinformatique/IA apporte

* analyse multi-omique ;
* machine learning ;
* intégration de données ;
* biomarker discovery ;
* modèles prédictifs ;
* pipelines reproductibles ;
* analyse statistique.

### Ce que le centre clinique apporte

* cohorte ;
* données cliniques ;
* échantillons biologiques ;
* biopsies ;
* données HLA/DSA ;
* expertise médicale ;
* validation biologique ;
* suivi longitudinal.

### Valeur de la collaboration

Créer une boucle :

**Clinical data → AI/Bioinformatics → candidate biomarker → biological validation → clinical validation**

---

# 16. Lettre/email de prise de contact

À la fin, rédige une première proposition de contact scientifique en français et en anglais.

Le message doit être :

* court ;
* professionnel ;
* crédible ;
* personnalisé pour le chercheur ciblé ;
* non commercial ;
* orienté collaboration.

Ne pas prétendre que le projet est déjà validé.

Présenter plutôt :

> "Nous avons identifié une question scientifique potentiellement intéressante et souhaiterions explorer avec votre équipe la possibilité d'une collaboration."

Le message doit mentionner :

* la question scientifique ;
* le rôle de l'IA/bioinformatique ;
* le potentiel des données existantes ;
* pourquoi leur équipe est pertinente ;
* proposition d'un échange de 20–30 minutes.

---

# 17. Livrable final

Organise le rapport final dans cet ordre :

1. **Executive Summary**
2. **Scientific question**
3. **State of the art**
4. **Systematic review**
5. **Meta-analysis**
6. **Existing datasets**
7. **French research landscape**
8. **Scientific gap**
9. **Proposed AI project**
10. **Multi-omics strategy**
11. **Statistical methodology**
12. **Validation strategy**
13. **Feasibility**
14. **Expected impact**
15. **Potential publications**
16. **Potential French collaborators**
17. **Recommended first contact**
18. **Draft email in French**
19. **Draft email in English**
20. **References**

---

# 18. Exigences de rigueur

Utilise uniquement des informations vérifiables.

Pour chaque affirmation importante, fournir une référence scientifique.

Prioriser :

* PubMed ;
* articles peer-reviewed ;
* Nature ;
* Cell ;
* Science ;
* Lancet ;
* NEJM ;
* JACC ;
* Circulation ;
* American Journal of Transplantation ;
* Transplantation ;
* Journal of Heart and Lung Transplantation ;
* Frontiers lorsque pertinent ;
* bioRxiv uniquement en distinguant clairement les preprints.

Pour les datasets, utiliser prioritairement les repositories officiels.

Pour les équipes françaises, utiliser les pages institutionnelles officielles et les publications scientifiques.

**Ne jamais inventer :**

* données ;
* patients ;
* résultats ;
* collaborations ;
* datasets ;
* coordonnées ;
* performances de modèles ;
* biomarqueurs ;
* essais cliniques.

Lorsque l'information n'est pas disponible, écrire explicitement :

**"Donnée non disponible / à confirmer auprès de l'équipe."**

---

# 19. Niveau d'analyse attendu

Ne produis pas simplement une revue bibliographique.

Je veux une véritable **analyse de faisabilité d'un projet de recherche translationnelle IA + transplantation cardiaque**, permettant à un PhD en bioinformatique de passer de :

**question scientifique → littérature → données → gap → méthodologie → validation → collaboration → prise de contact.**

À la fin, donne également un classement :

### TOP 5 — collaborations françaises les plus pertinentes

Pour chaque équipe :

**Score scientifique /10**
**Accès potentiel aux données /10**
**Expertise transplantation /10**
**Expertise immunologie /10**
**Compatibilité IA/bioinformatique /10**
**Potentiel de collaboration /10**

Puis donne une recommandation finale :

> **"Si vous deviez contacter une seule équipe en premier, laquelle choisiriez-vous et pourquoi ?"**

Enfin, propose une **version courte du projet (1 page)** pouvant être envoyée directement à un PI ou à un directeur de laboratoire.
