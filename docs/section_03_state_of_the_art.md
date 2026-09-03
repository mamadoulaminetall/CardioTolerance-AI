# Section 3 — État de l'art

*CardioTolerance-AI · v1 (2026-09-03). Synthèse de littérature ciblée. Toutes les
affirmations importantes sont sourcées ; les points non vérifiés portent la mention
« à confirmer ». Les références complètes sont dans [`references.md`](references.md).*

> Garde-fou : le projet ne suppose jamais l'arrêt de l'immunosuppression. Cette section
> décrit l'état des connaissances sur les **signatures de tolérance** et leur détection.

---

## 3.1 Contexte clinique — survie, rejet, rejet chronique

- Selon les rapports du registre **ISHLT**, la survie de l'adulte après transplantation
  cardiaque est d'environ **95 % à 1 an, 84 % à 5 ans, 72 % à 10 ans** ; survie médiane
  ~10,7 ans (greffes 1982–2015)
  ([registre ISHLT, JHLT](https://www.jhltonline.org/article/S1053-2498(12)01210-7/pdf)).
- Le **rejet reste une cause majeure de décès** (~21 % des décès), avec la malignité
  (~21 %), l'infection (~15 %) et la **vasculopathie du greffon cardiaque / CAV** (~14 %)
  ([StatPearls — Heart Transplantation Rejection](https://www.ncbi.nlm.nih.gov/books/NBK537057/)).
- La **CAV** (rejet chronique) touche ~8 % des patients à 1 an, ~30 % à 5 ans, ~50 % à
  10 ans (rapport de registre ISHLT, cité par
  [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537057/)) — chiffres à considérer
  comme ordres de grandeur.
- Chez les **survivants à très long terme** (analyse des survivants à 20 ans, registre
  ISHLT), la survie **sans aucun épisode de rejet** est d'environ 19 % à 1 an et **13 % à
  10 et 20 ans** ; survie sans CAV ~42 % à 20 ans
  ([Twenty-Year Survivors, AJT](https://www.amjtransplant.org/article/S1600-6135(22)05687-8/pdf)).
  → Autrement dit, une **minorité de patients ne fait jamais de rejet** et garde un
  greffon indemne de CAV très longtemps : c'est la population d'intérêt du projet.

**Diagnostic de référence du rejet** : la **biopsie endomyocardique (BEM)** avec
gradation histologique ISHLT (TCMR) et critères d'AMR. Limites reconnues : geste
invasif, coûteux, **erreur d'échantillonnage** et **variabilité inter-observateur**
importante ([Frontiers in Transplantation 2025, « Diagnosis of rejection following heart
transplantation »](https://www.frontiersin.org/journals/transplantation/articles/10.3389/frtra.2025.1693821/full)).

---

## 3.2 La tolérance opérationnelle — définition et réalité par organe

**Définition consensuelle** : arrêt de **tout** immunosuppresseur depuis **> 1 an**, avec
fonction de greffon stable, **absence de rejet aigu** et absence de rejet infraclinique
sur biopsie
([Brouard et al., revue tolérance rénale, PMC5508347](https://pmc.ncbi.nlm.nih.gov/articles/PMC5508347/)).

- **Foie** : phénomène le mieux documenté. Dans des essais de sevrage contrôlé,
  **~20–40 %** des receveurs hépatiques sélectionnés peuvent être sevrés (p. ex. 16/59 =
  27 % dans une série contrôlée), et des **biomarqueurs longitudinaux** de tolérance ont
  été validés dans un essai multicentrique prospectif
  ([Longitudinal biomarker progression, liver IS-withdrawal trial, PMC12685220](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12685220/)).
- **Rein** : la tolérance opérationnelle existe mais est **rare** (estimation < 300–500
  cas rapportés au total), le plus souvent **découverte fortuitement** après arrêt non
  planifié / non-observance ; les cas induits prospectivement sont exceptionnels
  ([Approaching the Promise of Operational Tolerance, Transplantation](https://journals.lww.com/transplantjournal/fulltext/10.1097/tp.0b013e318215e742~approaching-the-promise-of-operational-tolerance-in-clinical);
  [case report + revue, PMC9948746](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9948746/)).
- **Cœur** : la tolérance opérationnelle est **quasi absente de la littérature**. Les
  revues transversales sur la tolérance en organe solide la décrivent « presque
  exclusivement » pour le foie et le rein ; **aucune série de cas robuste** de sevrage
  complet en transplantation cardiaque isolée n'a été identifiée à ce stade (à confirmer
  par la revue systématique — Phase 2).
  → C'est le **cœur du gap** (voir Section 8).

**Point méthodologique clé** : les « empreintes » de tolérance du foie et du rein sont
**différentes** l'une de l'autre (mécanismes distincts), ce qui interdit de transposer
directement une signature d'un organe à l'autre
([Biomarkers of operational tolerance in SOT, PMC3442251](https://pmc.ncbi.nlm.nih.gov/articles/PMC3442251/)).

---

## 3.3 Minimisation / allègement de l'immunosuppression en transplantation cardiaque

- **Sevrage des corticoïdes** : pratique courante — **~40 %** des transplantés cardiaques
  sont sans corticoïdes à long terme
  ([Minimization of Immunosuppression in Heart Transplantation, Springer 2025](https://link.springer.com/chapter/10.1007/978-3-031-88290-6_14)).
- **Réduction / retrait des inhibiteurs de la calcineurine (ICN)** : des protocoles de
  retrait progressif des ICN sont **en cours d'évaluation** dans un essai multicentrique
  chez le transplanté cardiaque de novo (référence exacte à confirmer)
  ([Minimization of Immunosuppression in Heart Transplantation, Springer 2025](https://link.springer.com/chapter/10.1007/978-3-031-88290-6_14)).
- **Photophérèse extracorporelle (ECP) + immunosuppression allégée** : dans une étude
  pilote chez des patients à haut risque, l'ECP associée à une IS réduite a été jugée
  sûre (AMR 3,6 %, ACR 14,3 %)
  ([ECP pilot study, PMC8983826](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8983826/)).
- **Obstacle central reconnu** : l'impossibilité actuelle de **sélectionner de façon
  fiable les patients à très faible risque immunologique** — précisément le besoin auquel
  une signature + un modèle IA prétendent répondre
  ([Immunosuppression Management in Heart Transplantation, PMC12082473](https://pmc.ncbi.nlm.nih.gov/articles/PMC12082473/)).

---

## 3.4 Signatures immunologiques candidates

### 3.4.1 Lymphocytes T régulateurs (Treg)
- Le rôle des Treg dans la **survie prolongée de l'allogreffe cardiaque** est solidement
  établi **en préclinique** (transfert de Treg → prolongation de survie, prévention de la
  CAV) ; le transfert seul **ne suffit pas** à induire une tolérance robuste en
  MHC-mismatch complet
  ([Preclinical & clinical Treg therapy for heart transplantation, ScienceDirect 2026](https://www.sciencedirect.com/science/article/pii/S0198885926000273)).
- Biomarqueur candidat : **PD-1 élevé sur les Treg intra-greffon** chez la souris
  tolérante
  ([TCR-Tg tracking, PMC6241514](https://ncbi.nlm.nih.gov/pmc/articles/PMC6241514)).
- Essais de **thérapie Treg** de phase I/II : sécurité confirmée en rein et foie, avec
  réduction d'IS chez des patients sélectionnés ; en cardiaque, surtout envisagé pour la
  **prévention de la CAV pédiatrique**
  ([Frontiers Immunol 2024, Treg therapy & CAV](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1444924/full)).

### 3.4.2 Signature B de la tolérance (rein) et scores sanguins
- **Newell et al. et Sagoo et al. (JCI 2010)** : la tolérance opérationnelle rénale est
  associée à une **signature transcriptomique sanguine dominée par les transcrits B**
  (↑ **MS4A1/CD20**, **TCL1A**) ; un set de **3 gènes** validé par PCR a une bonne valeur
  prédictive
  ([revue Brouard, PMC5508347](https://pmc.ncbi.nlm.nih.gov/articles/PMC5508347/) ;
  [common gene signature across studies, PMC4424816](https://ncbi.nlm.nih.gov/pmc/articles/PMC4424816)).
- **Nantes (CR2TI)** : **score sanguin à 6 gènes** associé à la tolérance opérationnelle,
  **diminué** chez les patients développant des DSA anti-HLA ; et diagnostic
  d'**absence de rejet infraclinique** par expression génique sanguine
  ([Kidney Int 2023, PubMed 36990211](https://pubmed.ncbi.nlm.nih.gov/36990211/)).
- **scRNA-seq PBMC** d'un receveur rénal tolérant : paysage immunitaire cellulaire
  associé à la tolérance
  ([AJT 2023, S1600-6135(23)00466-5](https://www.amjtransplant.org/article/S1600-6135(23)00466-5/fulltext)).
- **Non démontré en transplantation cardiaque** — transposition à tester.

### 3.4.3 Répertoire TCR / BCR
- Chez des patients **tolérants** (rein + moelle), la tolérance à long terme s'accompagne
  d'une **délétion clonale des lymphocytes T donneur-réactifs**
  ([Sci Transl Med 2015, clonal deletion in tolerant kidney patients](https://www.science.org/doi/10.1126/scitranslmed.3010760)).
- Les répertoires TCR des patients tolérants sont **moins biaisés / plus divers** que
  ceux des patients en rejet
  ([Analysis of TCR repertoire in transplantation, PMC8790170](https://pmc.ncbi.nlm.nih.gov/articles/PMC8790170/)).
- Le séquençage du répertoire (TCR/BCR) permet de **tracer les clones donneur-réactifs**
  dans le sang et le greffon
  ([Clinical application of immune repertoire sequencing in SOT, PMC9971933](https://pmc.ncbi.nlm.nih.gov/articles/PMC9971933/)).
- **Données cardiaques humaines rares** — à confirmer en Phase 2.

### 3.4.4 DSA et mismatch HLA moléculaire
- Les **DSA anti-HLA de novo** (surtout **anti-DQ**) sont un moteur majeur de l'AMR et de
  la perte de greffon
  ([HLA-DQ mismatches & dnDSA in heart transplant, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S019888592030149X)).
- Le **mismatch HLA au niveau moléculaire** (eplets — HLAMatchmaker/HLA-EMMA ; épitopes T
  — PIRCHE-II) est un **biomarqueur puissant du risque de rejet**, encore **peu étudié en
  cardiaque adulte** ; testé en pédiatrie cardiaque (HLA-EMMA + PIRCHE-II)
  ([immunologic risk stratification, pediatric heart, PMC10043167](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10043167/)).
- Un profil de **faible charge de mismatch moléculaire** est un candidat naturel de
  composante « pro-tolérance » d'une signature intégrée.

---

## 3.5 Multi-omics du rejet cardiaque — ce qui existe

### 3.5.1 Transcriptome de biopsie — Molecular Microscope (MMDx-Heart)
- Système **MMDx-Heart** (P. Halloran, U. Alberta) : microarray sur BEM + **ensembles de
  modèles ML** comparant chaque biopsie à un set de référence ; évalue TCMR, AMR, lésion
  parenchymateuse récente, atrophie-fibrose. Construit à partir de **453 transcrits
  associés au rejet (RATs)** dérivés du rein
  ([The Molecular Microscope Diagnostic System, Transplantation 2022, PubMed 36508644](https://pubmed.ncbi.nlm.nih.gov/36508644/)).
- **« Redefining the molecular rejection states in 3230 heart transplant biopsies »**
  (AJT 2024) : relations entre états moléculaires, lésion parenchymateuse et survie du
  greffon — **grand jeu de données réel** de BEM cardiaques
  ([ScienceDirect S1600613524002417](https://www.sciencedirect.com/science/article/pii/S1600613524002417)).
- Développement initial : 331 BEM, 221 sujets, 3 centres (**Edmonton, Bologne, Paris**)
  ([Building a tissue-based molecular diagnostic system, JHLT](https://www.sciencedirect.com/science/article/abs/pii/S1053249817318302)).
- Essai en cours : **NCT06436027** — diagnostic moléculaire du rejet d'allogreffe
  cardiaque par profilage d'expression génique intra-greffon ciblé (« heart HistoMX »),
  Paris Transplant Group
  ([ClinicalTrials NCT06436027](https://clinicaltrials.gov/study/NCT06436027)).

### 3.5.2 Transcriptome sanguin & biomarqueurs non invasifs
- **AlloMap** (GEP sanguin, panel **11 gènes informatifs** + 9 de normalisation ; score
  0–40) : seul test sanguin **recommandé par l'ISHLT** pour la surveillance du rejet chez
  les patients stables à faible probabilité d'ACR modéré/sévère
  ([CareDx / HeartCare interpretive guide](https://www.caredx.com/wp-content/uploads/2021/09/LK-10482-Heartcare-Interpretive-Guide.pdf)).
- **dd-cfDNA** (AlloSure Heart, NGS ciblé) : biomarqueur de **lésion** du greffon ;
  méta-analyse 2025 = biomarqueur non invasif **prometteur** pour le diagnostic de rejet
  aigu, performance à optimiser
  ([dd-cfDNA meta-analysis, PubMed 40132451](https://pubmed.ncbi.nlm.nih.gov/40132451/)).
- Signatures **ML sur sang périphérique** : des workflows rapportent des signatures
  géniques de rejet (p. ex. *ALAS2, HBD, KLRD1*) avec **AUC > 0,90** et détection
  précoce — chiffres issus d'une **revue narrative**, à vérifier étude par étude
  ([AI narrative review, Front Cardiovasc Med 2026](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1790244/full)).

### 3.5.3 Single-cell / single-nucleus & spatial
- **scRNA-seq du rejet cardiaque aigu : essentiellement murin** (modèle hétérotopique) —
  atlas des sous-populations, rôle des macrophages infiltrants m3/m4, voie CXCR3
  ([Front Immunol 2022, PMC8866760](https://pmc.ncbi.nlm.nih.gov/articles/PMC8866760/) ;
  [Theranostics 2022, PMC9475451](https://pmc.ncbi.nlm.nih.gov/articles/PMC9475451/)).
- **snRNA-seq de BEM humaines** : faisable ; a montré la **persistance d'un chimérisme
  donneur-receveur** avec signatures distinctes dans la CAV sévère
  ([PMC9852032](https://pmc.ncbi.nlm.nih.gov/articles/PMC9852032/)).
- **Transcriptomique spatiale, protéomique, métabolomique, microbiome** en tolérance
  cardiaque : **quasi inexistantes** chez l'humain (à confirmer Phase 2).

---

## 3.6 IA / Machine learning pour la prédiction du rejet cardiaque

- **Pathologie computationnelle** : deep learning auto-supervisé sur lames de BEM de
  routine — AUROC ~**0,85 en validation croisée**, mais **0,72–0,73 en validation
  externe** ; un autre modèle rapporte AUC 0,96 (rejet global), 0,96 (ACR), 0,87 (AMR)
  ([EHJ Digital Health 2023, PMC10232288](https://pmc.ncbi.nlm.nih.gov/articles/PMC10232288/)).
- **ECG + deep learning** : détection non invasive du rejet, AUC ~**0,84**, sensibilité
  95 %
  ([PubMed 36974261](https://pubmed.ncbi.nlm.nih.gov/36974261/)).
- **Modèles sur expression génique** (JPM 2024) : prédiction du rejet cardiaque aigu à
  partir de profils d'expression
  ([J Pers Med 2024;14:410](https://doi.org/10.3390/jpm14040410)).
- **iBox / Paris Transplant Group** : score de risque individuel de perte de greffon par
  analyse algorithmique de **> 85 paramètres** péri/post-greffe (validé en rein, décliné
  vers d'autres organes)
  ([Paris Transplant Group](https://paristransplantgroup.com/current-team/alexandre-loupy/)).
- **Limite transversale reconnue** : qualité méthodologique **sous-optimale** — design
  **monocentrique rétrospectif**, **petits effectifs**, **absence de validation externe
  indépendante**
  ([AI narrative review, Front Cardiovasc Med 2026](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1790244/full)).

---

## 3.7 Ce que la littérature établit — et ce qu'elle ne dit pas

**Établi :**
1. Une minorité de transplantés cardiaques ne fait **jamais** de rejet et reste indemne
   de CAV très longtemps (registre ISHLT).
2. La **tolérance opérationnelle** est réelle et **biomarquée** en foie et en rein, avec
   des empreintes **organe-spécifiques** (signature B sanguine en rein ; délétion clonale
   TCR chez les tolérants).
3. Le **rejet** cardiaque est **finement caractérisable au plan moléculaire** (MMDx-Heart,
   453 RATs, > 3000 biopsies) et **détectable de façon non invasive** (AlloMap, dd-cfDNA).
4. L'**IA** atteint des performances correctes pour **détecter** le rejet, mais
   généralise mal (chute en validation externe).

**Non établi / lacunaire :**
1. **Aucune signature de tolérance validée en transplantation cardiaque humaine**, ni de
   série de cas robuste de sevrage complet en greffe cardiaque isolée.
2. Quasi **pas de données multi-omiques longitudinales humaines** orientées *tolérance*
   (vs rejet) dans le cœur ; scRNA-seq surtout murin.
3. **Pas de modèle IA longitudinal** prédisant la *trajectoire* du risque de rejet /
   tolérance sur données cardiaques multimodales, avec validation externe.
4. Les **répertoires TCR/BCR** et le **mismatch HLA moléculaire** ne sont pas intégrés
   aux signatures cardiaques existantes.

→ Ces quatre manques structurent la Section 8 (Gap) et la proposition (Section 9).
