# CardioTolerance-AI — Rapport de faisabilité

**AI-driven discovery of immune tolerance signatures after heart transplantation**

MedFlow AI · Dr. Mamadou Lamine Tall, PhD (Bioinformatique & Data Science) — Montpellier
· contact@medflow-ai.fr · https://medflow-ai.fr

*Document assemblé automatiquement le 2026-09-08 par
`scripts/05_assemble_report.py` à partir des sections de `docs/`. Ne pas éditer ici —
éditer les sections sources puis relancer le script.*

> **Statut : v1 de travail.** Plusieurs éléments sont marqués « à confirmer » (identifiants
> de références, effectifs de datasets, coordonnées d'équipes). La revue systématique
> formelle (requêtes journalisées + extraction sur texte intégral) et la méta-analyse
> dd-cfDNA restent à exécuter (Phase 2). Les brouillons d'emails **ne doivent pas être
> envoyés** sans validation de Dr. Tall.

> **Garde-fou scientifique :** le projet ne présuppose jamais l'arrêt de
> l'immunosuppression. Objectif = biomarqueurs et profils de tolérance à valider
> prospectivement, sous supervision médicale.

---

## Sommaire

1. [1. Executive Summary](#1-executive-summary)
2. [2. Question scientifique](#2-question-scientifique)
3. [3. État de l'art](#3-état-de-l'art)
4. [4. Revue systématique](#4-revue-systématique)
5. [5. Méta-analyse / synthèse de preuves](#5-méta-analyse--synthèse-de-preuves)
6. [6. Données réellement disponibles](#6-données-réellement-disponibles)
7. [7. Paysage français](#7-paysage-français)
8. [8–12. Gap, projet IA, multi-omics, méthodo statistique, validation biologique](#8–12-gap-projet-ia-multi-omics-méthodo-statistique-validation-biologique)
9. [13–15. Faisabilité, impact attendu, publications](#13–15-faisabilité-impact-attendu-publications)
10. [16–17. Collaboration, TOP 5, premier contact](#16–17-collaboration-top-5-premier-contact)
11. [18. Brouillon d'email — Français](#18-brouillon-d'email--français)
12. [19. Brouillon d'email — English](#19-brouillon-d'email--english)
13. [20. Références](#20-références)


---

# 1. Executive Summary
# Section 1 — Executive Summary

*CardioTolerance-AI · v1 (2026-09-03). Résumé exécutif du dossier de faisabilité
« AI-driven discovery of immune tolerance signatures after heart transplantation ».
Porteur : Dr. M. L. Tall, PhD — MedFlow AI (Montpellier). Toutes les affirmations
importantes sont sourcées dans les sections détaillées et [`references.md`](references.md).*

> **Garde-fou** : le projet ne présuppose jamais l'arrêt de l'immunosuppression. Objectif
> = identifier des **biomarqueurs et des profils de tolérance / stabilité immunologique
> profonde**, à valider prospectivement, sous supervision médicale.

---

## Question

Chez les receveurs de greffe cardiaque **très stables à long terme** (sans rejet, sans DSA
de novo, sans vasculopathie du greffon, sous immunosuppression minimale), existe-t-il une
**signature immunologique ou multi-omique reproductible** de tolérance, que l'IA peut
identifier, distinguer des profils de rejet, et dont elle peut **prédire la trajectoire
longitudinale** ?

## Ce que dit la littérature (Sections 3–5)

- La **tolérance opérationnelle** est réelle et **biomarquée** en transplantation
  **hépatique et rénale** (ex. signature sanguine à dominante lymphocytaire B en rein ;
  délétion clonale TCR chez les tolérants), mais avec des empreintes **organe-spécifiques**.
- **En transplantation cardiaque** : **aucune signature de tolérance validée**, et
  **aucune série de cas robuste** de sevrage complet en greffe cardiaque isolée.
- Le **rejet** cardiaque, lui, est finement caractérisé au plan moléculaire (systèmes de
  transcriptome de biopsie type MMDx-Heart, > 3 000 biopsies) et détectable de façon non
  invasive (dd-cfDNA, GEP sanguin).
- Les modèles d'**IA** détectent le rejet mais **généralisent mal** (chute nette en
  validation externe) et ne modélisent pas la *trajectoire* du risque.
- **Méta-analyse** : quantitative seulement pour les biomarqueurs non invasifs de rejet
  aigu (dd-cfDNA) ; pour la *tolérance* et l'*IA*, une **evidence synthesis** est la
  méthode justifiée.

## Le gap (Section 8)

Il est d'abord **conceptuel** : le phénotype « tolérance / stabilité profonde » en greffe
cardiaque n'est **ni défini ni profilé**. S'y ajoutent la rareté des données -omiques
longitudinales humaines, l'hétérogénéité, l'absence de validation externe, et le régime
**p ≫ n**.

## Proposition (Sections 9–12)

- **Aim 1 — Intégration** : construire une cohorte multimodale (clinique longitudinale,
  biopsies, HLA/mismatch moléculaire, DSA, transcriptome, profil cellulaire, TCR/BCR),
  avec une **définition préspécifiée** du phénotype cible.
- **Aim 2 — Découverte** : clustering multimodal non supervisé puis modèles pénalisés /
  ensembles avec **sélection de variables stable** ; éviter la circularité histologie ↔
  moléculaire.
- **Aim 3 — Prédiction** : comparer familles de modèles (Elastic Net, RF/XGBoost, survie,
  multimodal) en **nested CV par patient**, calibration, **validation externe = critère
  principal**, SHAP, robustesse.
- **Multi-omics** : quantifier la **valeur ajoutée incrémentale** clinique → immuno →
  transcriptome → multi-omique → multimodal (net benefit).
- **Validation biologique** : annotation mécanistique + confirmation
  qPCR/cytométrie/IHC/single-cell/TCR sur cohorte indépendante.

## Faisabilité (Section 13)

- **Scénario A (immédiat, sans partenaire)** : réanalyse harmonisée de jeux de biopsies
  cardiaques publics (GEO/ImmPort) → proof-of-concept méthodologique publiable. Faisabilité
  **élevée**, 6–12 mois, coût faible.
- **Scénario B (avec un centre FR)** : + cohorte rétrospective → découverte **et
  validation clinique** d'une signature. Faisabilité **moyenne**, 18–30 mois.
- **Scénario C (translationnel)** : cohorte multicentrique prospective + multi-omics →
  biomarqueur candidat qualifié. Nécessite consortium + financement dédié.
- Séquencement **A → B → C** ; le projet ne dépend jamais de C.

## Impact (Section 14)

Informatif **quelle que soit l'issue** : signature reproductible (fort impact), plusieurs
phénotypes (reconceptualisation), ou **absence de signature robuste** (démontre les
limites des biomarqueurs actuels — publiable et utile pour éviter des essais prématurés).

## Collaboration & premier contact (Sections 7, 15–17)

- **Cible n°1 : Paris Transplant Group / PITOR (PARCC, INSERM UMR-S 970)** — angle cœur
  via **Guillaume Coutance**, sous l'égide d'**Alexandre Loupy** (score 60,25/70). Seule
  équipe française réunissant cohortes cardiaques + transcriptome de biopsie + IA.
- Positionnement : apporter **l'angle *tolérance*** (peu couvert par eux) + méthodologie
  signature multi-omique + une paire de bras dédiée, en démarrant sur **données publiques**
  (Scénario A) avant toute demande d'accès.
- **n°2 méthodologique sans concurrence** : CR2TI Nantes (Sophie Brouard), co-encadrement
  signature.
- Emails FR/EN + one-pager prêts ([`../outreach/`](../outreach/)) — **à valider par Dr.
  Tall avant tout envoi**.

## Demande

Un échange de **20–30 minutes** avec l'équipe cible pour évaluer la pertinence
scientifique et la faisabilité d'un accès à une cohorte rétrospective.

---

# 2. Question scientifique
# Section 2 — Question scientifique

*CardioTolerance-AI · v1 (2026-09-03). Reprend le brief §1 en le cadrant pour un
partenaire académique.*

> **Garde-fou (répété)** : le projet **ne présuppose jamais** qu'un patient puisse arrêter
> son immunosuppression. L'objectif est d'identifier des **biomarqueurs et des profils de
> tolérance / stabilité immunologique profonde**, susceptibles d'être validés
> prospectivement, sous supervision médicale stricte.

## 2.1 Question centrale

Existe-t-il, chez certains receveurs de transplantation cardiaque, une **signature
immunologique, moléculaire, cellulaire ou multi-omique** associée à une tolérance
particulièrement élevée du greffon — et l'intelligence artificielle permet-elle :

1. d'**identifier** cette signature ;
2. de **distinguer** les patients en rejet des patients en stabilité durable ;
3. de repérer des **profils compatibles avec une tolérance immunologique exceptionnelle** ;
4. de **prédire longitudinalement** l'évolution du risque de rejet ;
5. à terme, d'aider à identifier les patients qui pourraient être **candidats à une
   réduction contrôlée et médicalement supervisée** de l'immunosuppression (jamais un
   arrêt).

## 2.2 Sous-questions opérationnelles

| # | Sous-question | Traitée en |
|---|---|---|
| SQ1 | Comment **définir** opérationnellement le phénotype « stabilité immunologique profonde » chez le transplanté cardiaque ? | §9 (Aim 1) |
| SQ2 | Quel **compartiment** porte le signal : sang, biopsie, ou les deux ? | §9–§10 |
| SQ3 | Une signature de tolérance **rénale** connue (dominante B) est-elle transposable au cœur, ou faut-il une découverte *de novo* ? | §3, §8 (Q2/Q7) |
| SQ4 | La **dynamique temporelle** des biomarqueurs prédit-elle mieux que leur valeur ponctuelle ? | §9 (approche longitudinale, brief §8) |
| SQ5 | L'**intégration multimodale** apporte-t-elle une valeur prédictive au-delà du modèle clinique ? | §10 |
| SQ6 | La signature est-elle **biologiquement interprétable** et **reproductible en validation externe** ? | §11–§12 |

## 2.3 Ce qui est explicitement hors périmètre

- Toute recommandation ou organisation d'un allègement thérapeutique chez un patient réel.
- Le développement d'un dispositif médical ou d'un test diagnostique commercialisable.
- La transposition directe, sans validation, d'une signature d'un autre organe.
- La conception d'un essai interventionnel (ce serait une **suite** possible, portée par
  le centre clinique, avec comité de surveillance indépendant).

---

# 3. État de l'art
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

---

# 4. Revue systématique
# Section 4 — Revue systématique : protocole & état d'avancement

*CardioTolerance-AI · v1 (2026-09-03). Protocole opérationnel (non déposé sur PROSPERO à
ce stade). Suit l'esprit PRISMA 2020.*

---

## 4.1 Question (format PICO adapté)

| Élément | Définition |
|---|---|
| **Population** | Receveurs d'une transplantation cardiaque (adultes en priorité ; pédiatrie en sous-groupe) |
| **Exposition / facteur** | Signature immunologique / moléculaire / cellulaire / multi-omique (transcriptome, single-cell, TCR/BCR, cytométrie, protéomique, DSA/HLA, épigénome, métabolome) |
| **Comparateur** | Patients en rejet (TCMR et/ou AMR, aigu ou chronique/CAV) vs patients stables ; et, si documenté, patients en tolérance/IS minimisée |
| **Outcomes** | (1) rejet aigu / chronique ; (2) stabilité durable sans rejet ; (3) tolérance opérationnelle ou réduction majeure d'IS documentée ; (4) survie du greffon / du patient, événements CV ; (5) performances prédictives des modèles (AUC, C-index, sensibilité, spécificité) |
| **Design** | Cohortes prospectives/rétrospectives, cas-témoins, séries de cas, études omiques, études de développement/validation de modèles. Revues et éditoriaux exclus du décompte quantitatif mais lus pour le contexte. |

## 4.2 Bases interrogées (brief §2 & §4)

PubMed / MEDLINE · Europe PMC (EMBL-EBI) · Web of Science (si accès) · Cochrane CENTRAL ·
ClinicalTrials.gov + EU-CTR (essais) · **bioRxiv / medRxiv** (preprints, étiquetés
séparément). Repositories de données traités en Section 6 : GEO, SRA, ArrayExpress,
dbGaP, EGA, ImmPort, BioStudies, Zenodo, Figshare.

## 4.3 Blocs de mots-clés (à combiner en AND entre blocs, OR intra-bloc)

Repris de [`00_PROMPT_BRIEF.md`](00_PROMPT_BRIEF.md) §2 et figés dans
[`../scripts/01_build_lit_corpus.py`](../scripts/01_build_lit_corpus.py) :

- **Bloc A — tolérance / greffe cardiaque** : `heart transplantation` OR
  `cardiac allograft` AND (`operational tolerance` OR `immune tolerance` OR
  `spontaneous tolerance` OR `immunosuppression minimization` OR
  `immunosuppression withdrawal` OR `rejection-free` OR `long-term survivors`)
- **Bloc B — signatures immunologiques** : `Treg` OR `regulatory B cells` OR `NK cells`
  OR `T-cell exhaustion` OR `TCR sequencing` OR `BCR sequencing` OR
  `donor-specific antibodies` OR `HLA molecular mismatch` OR `mass cytometry` OR
  `immune transcriptomics`
- **Bloc C — multi-omics** : `RNA-seq` OR `single-cell RNA-seq` OR
  `spatial transcriptomics` OR `methylation` OR `proteomics` OR `metabolomics` OR
  `microbiome` OR `multi-omics` OR `longitudinal omics`
- **Bloc D — IA / ML** : `machine learning` OR `deep learning` OR `survival model` OR
  `multimodal learning` OR `explainable AI` OR `biomarker discovery` OR
  `rejection prediction` OR `transplant outcome prediction`

Requêtes principales : **A∧B**, **A∧C**, **A∧D**, **A∧B∧C**, **A∧C∧D**. Chaque requête
exécutée est journalisée (chaîne exacte, base, date, nombre de hits) pour la traçabilité
PRISMA.

### 4.3bis Premier passage PubMed (journalisé le 2026-09-07)

Exécuté par [`../scripts/01_build_lit_corpus.py`](../scripts/01_build_lit_corpus.py) via
E-utilities → [`../meta-analysis/data/query_log.csv`](../meta-analysis/data/query_log.csv)
et [`../meta-analysis/data/lit_corpus.csv`](../meta-analysis/data/lit_corpus.csv).

| Requête | Hits |
|---|---|
| Q1 — cœur ∧ tolérance | 437 |
| Q2 — cœur ∧ tolérance ∧ signatures immunitaires | 86 |
| Q3 — cœur ∧ tolérance ∧ multi-omics | 8 |
| **Q4 — cœur ∧ tolérance ∧ IA/ML** | **0** |
| Q5 — cœur ∧ omics ∧ IA ∧ rejet | 10 |
| Q6 — cœur ∧ dd-cfDNA ∧ rejet | 149 |
| Q7 — cœur ∧ signatures immunitaires ∧ omics ∧ rejet | 20 |
| Q8 — cœur ∧ répertoire TCR/BCR / délétion clonale | 84 |
| **Total dédoublonné (PMID)** | **670** (652 avec résumé) |

**Résultat marquant** : **Q4 = 0** — aucun article PubMed n'associe *transplantation
cardiaque* + *tolérance* + *IA/ML* dans le titre/résumé. Confirmation directe du gap
(Section 8, Q3/Q10). À ce stade : PubMed uniquement ; Europe PMC, Cochrane, registres et
preprints restent à ajouter pour le décompte PRISMA définitif.

## 4.4 Critères d'éligibilité

**Inclusion** : population de transplantés cardiaques humains ; ≥ 1 mesure immunologique
ou -omique ; ≥ 1 outcome de la liste 4.1 ; anglais ou français ; toute date.
**Inclusion élargie (contexte, marquée à part)** : études rein/foie/poumon sur les
**signatures de tolérance** (pour la transposition méthodologique).
**Exclusion** : purement précliniques (animal/in vitro) sauf revues mécanistiques citées
en contexte ; xénogreffe ; absence d'outcome exploitable ; doublons.

## 4.5 Processus

1. Dédoublonnage (DOI/PMID) → `meta-analysis/data/lit_corpus.csv`
2. Screening titre/résumé (2 passes, motifs d'exclusion tracés)
3. Texte intégral des retenus → décision finale
4. Extraction structurée → `data/studies_registry.csv` (colonnes = variables brief §3,
   schéma dans [`../scripts/02_screen_and_extract.py`](../scripts/02_screen_and_extract.py))
5. Évaluation du risque de biais : **QUADAS-2** (études diagnostiques),
   **PROBAST** (modèles prédictifs), **Newcastle-Ottawa** (cohortes/cas-témoins)
6. Diagramme de flux PRISMA → `meta-analysis/figures/prisma_flow.png`

## 4.6 Évaluation préliminaire de la faisabilité d'une méta-analyse quantitative

*(hypothèse de travail, à confirmer une fois `studies_registry.csv` rempli — Phase 2)*

**Ce qui semble méta-analysable :**
- **dd-cfDNA pour le diagnostic de rejet aigu cardiaque** : une méta-analyse existe déjà
  ([PubMed 40132451](https://pubmed.ncbi.nlm.nih.gov/40132451/)) → on peut la
  **mettre à jour / répliquer** (modèle bivarié sensibilité-spécificité, HSROC).
- **Troponine** et **IRM multiparamétrique (T1/T2 mapping)** pour le rejet aigu : deux
  méta-analyses de précision diagnostique publiées
  ([troponine, PMC9215116](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9215116/) ;
  [CMR, JACC Cardiovasc Imaging](https://www.sciencedirect.com/science/article/pii/S1936878X21004277))
  → utiles comme comparateurs non invasifs, pas au cœur du sujet « tolérance ».

**Ce qui ne l'est probablement pas :**
- **Signatures de tolérance en transplantation cardiaque** : très peu d'études humaines,
  outcomes hétérogènes (« tolérance » quasi jamais définie de façon homogène en
  cardiaque), modalités -omiques et plateformes non comparables, absence de mesure
  d'effet standardisée. → une **méta-analyse quantitative sur la tolérance cardiaque
  n'est a priori pas justifiable**.
- **Modèles IA de prédiction du rejet cardiaque** : effectifs faibles, endpoints et
  splits non homogènes, forte hétérogénéité méthodologique, quasi pas de validation
  externe → **synthèse structurée (evidence synthesis) avec tableau de performances +
  évaluation PROBAST**, plutôt qu'un pooling d'AUC (qui serait trompeur).

**Conclusion provisoire (§17 point 5) :** méta-analyse quantitative **ciblée** faisable
sur les **biomarqueurs non invasifs de rejet aigu** (dd-cfDNA en priorité) ; pour la
**tolérance** et pour l'**IA**, livrer une **systematic review + evidence synthesis**
argumentée, avec justification explicite du refus du pooling. Décision définitive après
extraction.

## 4.7 État d'avancement

- ☑ Protocole rédigé (ce document)
- ☑ Blocs de mots-clés figés
- ☑ 1er passage PubMed journalisé (8 requêtes → 670 PMID dédoublonnés,
  `meta-analysis/data/{query_log,lit_corpus}.csv`) ; **Q4 = 0** (cœur ∧ tolérance ∧ IA)
- ☐ Étendre : Europe PMC, Cochrane CENTRAL, ClinicalTrials.gov/EU-CTR, bioRxiv/medRxiv
- ☐ Screening titre/résumé des 670 (2 relecteurs) → journal des exclusions
- ◐ `data/studies_registry.csv` v0 = 12 études seed (S01–S12), métadonnées d'abstracts
  vérifiées ; **effectifs bruts (2×2) non extraits** — nécessite l'accès aux textes
  intégraux
- ☑ `scripts/03_meta_analysis.py` **implémenté et exécutable** : attend
  `data/ddcfdna_2x2.csv` (study_id, threshold, tp, fp, fn, tn) ; s'arrête proprement tant
  que ce fichier n'existe pas ; produit ensuite pooling DL (logit) sens/spéc + I² +
  intervalle de prédiction + espace ROC + forest plots
- ☐ Extraction 2×2 sur textes intégraux → `data/ddcfdna_2x2.csv` *(bloquant : accès
  bibliothèque / institutionnel requis)*
- ☐ Exécution des requêtes formelles + `lit_corpus.csv` + journal PRISMA
- ☐ Risque de biais (QUADAS-2 / PROBAST / NOS)
- ☐ Décision finale méta-analyse vs evidence synthesis

**Ce qui bloque la méta-analyse quantitative aujourd'hui** : les abstracts donnent
sensibilité/spécificité mais rarement les **effectifs par cellule** (TP/FP/FN/TN)
nécessaires au modèle. C'est une tâche d'extraction sur PDF (Dr. Tall / partenaire /
accès institutionnel), pas un verrou méthodologique. Le code est prêt.

---

# 5. Méta-analyse / synthèse de preuves
# Section 5 — Méta-analyse / synthèse de preuves

*CardioTolerance-AI · v1 (2026-09-03). Décision **provisoire**, à figer après extraction
(`data/studies_registry.csv`, Phase 2). Voir aussi
[`section_04_systematic_review.md`](section_04_systematic_review.md) §4.6.*

---

## 5.1 Décision de méthode (brief §3 & §17.5)

| Domaine | Méta-analyse quantitative ? | Méthode retenue |
|---|---|---|
| **Signatures de tolérance en greffe cardiaque** | **Non** — non justifiable | Systematic review + evidence synthesis structurée |
| **Modèles IA de prédiction du rejet cardiaque** | **Non** — pooling trompeur | Evidence synthesis + tableau de performances + PROBAST |
| **Biomarqueurs non invasifs de rejet aigu (dd-cfDNA en priorité)** | **Oui — ciblée** | Modèle bivarié sensibilité-spécificité / HSROC ; sous-groupes ; biais |

## 5.2 Pourquoi pas de méta-analyse quantitative sur la tolérance cardiaque

1. **Trop peu d'études humaines** dédiées (voir Section 8 Q3/Q8) — le phénotype n'est
   même pas défini de façon homogène.
2. **Outcomes hétérogènes** : « tolérance », « stabilité », « rejection-free » recouvrent
   des définitions différentes selon les séries ; pas de dénominateur commun.
3. **Modalités et plateformes non comparables** (microarray vs RNA-seq vs single-cell vs
   cytométrie ; sang vs biopsie).
4. **Absence de mesure d'effet standardisée** extractible (souvent des listes de gènes,
   pas des HR/OR/AUC sur un même critère).
5. Un pooling forcé produirait une estimation **précise mais fausse** (hétérogénéité non
   interprétable). → **evidence synthesis** avec tableau structuré (par étude : design,
   n, définition, modalité, résultat qualitatif, risque de biais NOS/PROBAST).

## 5.3 Pourquoi pas de pooling d'AUC pour les modèles IA

- AUC dépend de la **prévalence**, du **spectre** des patients, du **schéma de
  validation** (interne vs externe), et du **critère** (ACR ≥ 2R ? AMR ? tout rejet ?).
- La littérature est **majoritairement monocentrique, rétrospective, sans validation
  externe** [R38, R39].
- → **Tableau comparatif** (modèle, données, n, endpoint, validation, AUC/C-index,
  calibration rapportée ?) + **PROBAST** par étude + synthèse narrative des tendances
  (ex. chute systématique interne → externe).

## 5.4 Méta-analyse ciblée réalisable : dd-cfDNA pour le rejet aigu cardiaque

- **Base** : méta-analyse publiée — *Transplantation Reviews* 2025 ([R31], PubMed
  40132451 ; recherche jusqu'au 2024-08-01) : **10 études**, **sensibilité poolée 65 %**
  (IC95 61–68), **spécificité poolée 79 %** (IC95 78–80), **AUC 0,83**. → objectif :
  **réplication / actualisation** (recherche étendue, QUADAS-2, études post-2024).
- **Études primaires déjà identifiées** (extraites d'abstracts, à confirmer sur texte
  intégral — voir [`../data/studies_registry.csv`](../data/studies_registry.csv) S01–S05) :
  - **Khush 2019 (D-OAR)**, prospective multicentrique USA, seuil ≥ 0,15 % → sens 78,5 %
    (60,7–96,3), spéc 76,9 % (71,1–82,7).
  - **Quantification absolue 2023** (Transplant Int), 52 patients / 557 échantillons,
    seuil 0,1 % → AUC 0,78 (0,68–0,88), sens 92 %, spéc 56 %.
  - **FreeDNA-CAR** (Jiménez-Blanco / Crespo-Leiro, *J Heart Lung Transplant*
    2025;44:560–569 ; PubMed 39577511), prospective multicentrique **espagnole
    (12 centres)**, 206 patients / 1090 paires EMB–dd-cfDNA, seuil 0,10 % → **AUC 0,603**
    (0,513–0,692), sens 67 %, spéc 51 %, VPN 97 %, VPP 6,4 % — **performance modeste** ;
    à pondérer fortement dans la synthèse (design prospectif per-protocole rigoureux).
  - **Algorithme à deux seuils 2025** (AJT) — fraction + quantité.
  - **dd-cfDNA vs CAV 2022** (Front Cardiovasc Med) — **résultat négatif** (délimite le
    périmètre : dd-cfDNA pour le rejet **aigu**, pas la vasculopathie).
- **Modèle** : bivarié à effets aléatoires (Reitsma) ; courbe **HSROC** ; sensibilité,
  spécificité, DOR, LR+ / LR− poolés.
- **Hétérogénéité** : I² adapté aux études diagnostiques ; **méta-régression** (seuil de
  positivité, type de rejet, assay, délai post-greffe, design prospectif per-protocole vs
  cas-témoins).
- **Sous-groupes** : AMR vs TCMR ; seuil dd-cfDNA (0,10 % vs 0,15 % vs 0,20 %) ; adulte vs
  pédiatrie ; surveillance vs suspicion clinique.
- **Biais** : test de Deeks ; sensibilité (études à faible risque de biais uniquement) ;
  **attention à l'écart estimations rétrospectives vs prospectives** (l'AUC 0,60 de
  FreeDNA-CAR suggère un optimisme des séries antérieures).
- **Comparateurs non invasifs** (méta-analyses existantes, à citer, pas à recalculer) :
  troponine ([R33], sensibilité 0,41 / spécificité 0,79) ; **IRM T2 mapping** ([R34],
  sens ~85–90 % / spéc ~70–85 %). Consolidés dans
  [`../data/meta_estimates.csv`](../data/meta_estimates.csv).

## 5.5 Livrables de la section

- `data/studies_registry.csv` (toutes études) + sous-table `dd-cfDNA` pour la méta-analyse.
- `scripts/03_meta_analysis.py` → `meta-analysis/figures/` (HSROC, forest sens/spéc,
  funnel de Deeks) + `data/meta_estimates.csv` (consommé par l'app page 4).
- Diagramme **PRISMA** ; tables de risque de biais (**QUADAS-2**, **PROBAST**, **NOS**).
- Texte : synthèse narrative *tolérance* + tableau IA + résultats méta-analyse dd-cfDNA.

## 5.6 Statut

- ☑ Décision de méthode (ce document)
- ◐ `data/studies_registry.csv` v0 = 11 études seed (S01–S11 : 5 dd-cfDNA, 2 MMDx, 2 IA,
  2 comparateurs tolérance rénale) — métadonnées extraites d'abstracts, à confirmer sur
  texte intégral
- ◐ `data/meta_estimates.csv` v0 = MA publiée (dd-cfDNA : 10 études, sens 65 % / spéc
  79 % / AUC 0,83, **rapportée, non recalculée**) + ligne « re-analyse prévue » + 2
  comparateurs
- ☐ Requêtes PubMed/Europe PMC formelles journalisées + extraction 2×2 sur texte intégral
- ☐ Exécution `scripts/03_meta_analysis.py` (bivarié + HSROC + Deeks)
- ☐ Risque de biais (QUADAS-2 / PROBAST) + diagramme PRISMA
- ☐ Rédaction finale

---

# 6. Données réellement disponibles
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

---

# 7. Paysage français
# Section 7 — Paysage français : équipes, cohortes, biobanques

*CardioTolerance-AI · v1 (2026-09-03). 5 équipes seed, identifiées et vérifiées par
recherche web. **Statut « seed »** : à consolider (pages institutionnelles, annuaires,
échange direct). Détail machine-lisible : [`../data/french_teams.csv`](../data/french_teams.csv).*

> Règle de rigueur : coordonnées via **canaux institutionnels** uniquement (page équipe,
> formulaire du laboratoire, adresse postale du service). Pas d'adresse personnelle
> récupérée par scraping. Toute information non confirmée est marquée
> « Donnée non disponible / à confirmer auprès de l'équipe ».

---

## 7.1 Vue d'ensemble

La France dispose d'un **écosystème dense** en immunologie de la transplantation, mais
l'expertise **cardiaque + multi-omique + IA** est concentrée quasi exclusivement autour du
**Paris Transplant Group** ; les autres pôles majeurs (Nantes, Lyon) sont d'excellence
mais **orientés rein**, avec une passerelle cardiaque à construire.

Centres français historiquement actifs sur le **rejet d'allogreffe cardiaque avec
biopsie / omique** (cohorte 2006–2011, 137 biopsies / 109 patients, 4 centres) :
**HEGP et Pitié-Salpêtrière (Paris), Hôpital Laennec (Nantes), Hôpital Charles Nicolle
(Rouen)** [R & étude GEP-AMR, cf. `references.md`].

## 7.2 Fiches équipes

### A. Paris Transplant Group / PITOR — PARCC, INSERM UMR-S 970 (Paris) — *cible n°1*
- **Institution** : Université Paris Cité, INSERM, AP-HP (HEGP / Necker). Équipe
  « Paris Expertise Center for Organ Transplantation (PITOR) » au PARCC.
- **PI / figures** : Alexandre Loupy (chef), Guillaume Coutance (volet cœur), Jean-Paul
  Duong Van Huyen (pathologie cardiaque, Necker), Carmen Lefaucheur (DSA).
- **Expertise** : IA multi-organe du rejet et de la perte de greffon ; phénotypage
  moléculaire (MMDx-Heart, panel Banff HOT AMR cardiaque, « heart HistoMX ») ; iBox ;
  population sciences. **Pipeline biopsie → transcriptome → ML déjà opérationnel sur le
  cœur.**
- **Cohortes / biobanques** : cohortes multicentriques multi-organes ; cohorte historique
  de rejet cardiaque (4 centres FR) ; essai **NCT06436027**.
- **Contact** : page équipe PARCC
  (`parcc.inserm.fr/research-teams/paris-expertise-center-for-organ-transplantation/`),
  contact PARCC (`parcc.inserm.fr/contact/`, HEGP, 56 rue Leblanc, 75015 Paris), site
  `paristransplantgroup.com`.
- **Pourquoi** : alignement maximal (cœur + omique + IA + cohortes). **Risque** : équipe
  très sollicitée et **très forte en IA en interne** → se positionner en **partenaire sur
  l'angle *tolérance*** (peu couvert par eux), pas en prestataire ML.

### B. Programme de transplantation cardiaque — Pitié-Salpêtrière, AP-HP (Paris)
- **PI / figures** : Guillaume Coutance (recherche, rattaché aussi au PTG), Shaida
  Varnous (chirurgie).
- **Expertise** : plus grand programme européen ; allocation ; rejet aigu/chronique ;
  stratification individuelle du risque ; programme de désensibilisation depuis 2009.
- **Cohortes** : cohorte cardiaque bien phénotypée 2009–2019 (partagée avec Cedars-Sinai).
- **Contact** : AP-HP Pitié-Salpêtrière, Institut de Cardiologie, 47-83 bd de l'Hôpital,
  75013 Paris ; recherche via PARCC.
- **Pourquoi** : volume et phénotypage ; expertise bioinfo interne plus limitée → **plus
  de place pour un partenaire IA**. **Recouvre en partie l'équipe A** (Coutance).

### C. CR2TI — UMR 1064 (Nantes)
- **PI / figures** : Sophie Brouard, Richard Danger.
- **Expertise** : **référence française des signatures de tolérance** (score sanguin
  6 gènes, signature B, immuno-monitoring, absence de rejet infraclinique par expression
  génique). **Alignement conceptuel maximal.**
- **Limite** : expertise surtout **rénale** ; pas d'accès établi à une cohorte
  **cardiaque** multi-omique longitudinale. Programme de greffe cardiaque au CHU de Nantes
  (Laennec) = passerelle possible.
- **Contact** : CR2TI, CHU de Nantes / Nantes Université, INSERM UMR 1064, ITUN.
- **Pourquoi** : méthodologie signature/score mature, directement transposable ;
  co-encadrement méthodologique idéal.

### D. CIRI — INSERM U1111 / CNRS UMR 5308, équipe NOPAB (Lyon)
- **PI** : Olivier Thaunat.
- **Expertise** : immunologie de la transplantation, lymphocytes B mémoire, AMR,
  **profilage transcriptomique et spatial de l'allogreffe**.
- **Limite** : orienté rein ; lien avec le programme cardiaque (Hôpital Louis Pradel, HCL)
  à construire.
- **Contact** : CIRI, Faculté de Médecine Lyon-Est / Hôpital Édouard Herriot, HCL.
- **Pourquoi** : apport mécanistique B/anticorps + spatial, complémentaire d'une approche
  signature.

### E. C2VN — Équipe 3 « Endothélium, cellules circulantes et pathologies vasculaires » (Marseille)
- **PI / unité** : **Pascale Paul** (C2VN — Centre de recherche en CardioVasculaire et
  Nutrition, INSERM 1263 / INRAE 1260, Aix-Marseille Université) ; **Christophe Picard**
  (EFS PACA, HLA) — rôles exacts à préciser.
- **Expertise** : **activation NK CD16-dépendante et risque de CAV** ([Paul et al.,
  *Front Immunol* 2019;10:1208] — profilage génétique et fonctionnel identifiant les
  patients à haut risque de vasculopathie du greffon) ; biomarqueurs non invasifs de
  lésion / réparation endothéliale immune (étude NCT01569334) ; immunogénétique HLA (EFS).
- **Contact** : page équipe C2VN
  (`c2vn.univ-amu.fr/equipes/equipe-3-endothelium-cellules-circulantes-et-pathologies-vasculaires/`) ;
  AP-HM (Timone / Hôpital Nord) ; EFS PACA.
- **Pourquoi** : angle **NK / CAV / endothélium** original et complémentaire d'une
  approche signature ; plateau HLA EFS ; **proximité de Montpellier**. Apport attendu =
  **partenaire biologie / validation**, pas fournisseur de cohorte multi-omique
  longitudinale (score 43,75/70).

## 7.2bis Modèle multicentrique de référence : FreeDNA-CAR (Espagne, pas France)

⚠️ **Correction** : contrairement à une première lecture, **FreeDNA-CAR est une étude
espagnole**, pas française — 12 centres espagnols, coordonnée par M. Jiménez-Blanco et
M. G. Crespo-Leiro (*J Heart Lung Transplant* 2025;44:560–569 ; PubMed 39577511),
prospective per-protocole (7 EMB + dd-cfDNA la 1ʳᵉ année ; 206 patients ; 1090 paires ;
inclusions 2019–2023). Enseignements :
- **modèle méthodologique** de collecte prospective harmonisée EMB + sang à l'échelle
  nationale — utile comme référence de design pour un Scénario C français.
- résultat scientifique : **AUC 0,60** pour le rejet aigu → argument fort pour une
  approche **multi-omique / multimodale** plutôt que mono-marqueur.
- le groupe de **M. G. Crespo-Leiro (A Coruña)** est un **collaborateur européen
  potentiel** (hors France) pour une extension ou une validation externe — à garder en
  réserve, pas en cible primaire.
- **Côté français**, l'infrastructure multicentrique équivalente à mobiliser est celle du
  **Paris Transplant Group** et des 4 centres historiques de la cohorte de rejet cardiaque
  (HEGP + Pitié Paris, Laennec Nantes, Charles Nicolle Rouen).

## 7.3 À compléter (Phase 4 — suite)

- CHU avec programme de greffe cardiaque non encore fichés : **Rouen (Charles Nicolle)**,
  Bordeaux, Lille, Strasbourg, Rennes, Toulouse (Rangueil), Montpellier (Arnaud de
  Villeneuve), Clermont-Ferrand, Grenoble, Tours, Nancy.
- **EFS / laboratoires HLA** (national) : typage haute résolution, eplets, DSA.
- **Plateformes single-cell / génomique** mobilisables (ex. réseaux France Génomique).
- Registre **CRISTAL (Agence de la biomédecine)** : données nationales de greffe — voie
  d'accès réglementée à explorer pour la partie clinique/survie.

---

# 8–12. Gap, projet IA, multi-omics, méthodo statistique, validation biologique
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
| **p ≫ n** (grande dimension, petit n) | filtrage a priori (variance, expression) ; réduction par couche (PCA/MOFA) ; modèles **pénalisés** en 1ʳᵉ intention ; **stability selection** ; pas de deep learning si n insuffisant (règle EPV / taille minimale préspécifiée) |
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

---

# 13–15. Faisabilité, impact attendu, publications
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

---

# 16–17. Collaboration, TOP 5, premier contact
# Sections 15–17 — Proposition de collaboration, TOP 5, premier contact

*CardioTolerance-AI · v1 (2026-09-03). Scoring machine-lisible :
[`../data/french_teams_scoring.csv`](../data/french_teams_scoring.csv). Fiches :
[`section_07_french_landscape.md`](section_07_french_landscape.md).*

---

# Section 15 — Ce que chaque partie apporte

## Le chercheur bioinformatique / IA (MedFlow AI — Dr. M. L. Tall)
- Analyse **multi-omique** (transcriptome bulk & single-cell, TCR/BCR, intégration MOFA+).
- **Machine learning** : modèles pénalisés, ensembles d'arbres, modèles de survie,
  fusion multimodale ; **nested CV, calibration, validation externe, SHAP**.
- **Intégration et harmonisation** de données hétérogènes multi-sources ; correction de
  lot ; modèle de données commun.
- **Biomarker discovery** avec sélection de variables **stable**, anti-leakage.
- **Pipelines reproductibles** (Snakemake/Nextflow, conteneurs, versioning données/modèles).
- **Analyse statistique** et reporting normé (**TRIPOD+AI**, **PROBAST**, PRISMA).
- Recalcul homogène des scores immunogénétiques (**eplets HLA-EMMA, PIRCHE-II**).

## Le centre clinique / l'équipe académique
- **Cohorte** de transplantés cardiaques rétrospective (idéalement longitudinale).
- **Données cliniques** longitudinales et **suivi** (rejets, DSA, CAV, IS, survie).
- **Échantillons biologiques** et **biopsies** (histologie ISHLT ± moléculaire).
- **Données HLA / DSA** et expertise immunogénétique.
- **Expertise médicale** : définition clinique du phénotype, plausibilité, garde-fous.
- **Validation biologique** (cytométrie, qPCR, IHC, single-cell, essais fonctionnels).
- **Cadre réglementaire et éthique** (promoteur, CPP, CNIL/MR-004, conventions).

## Valeur de la collaboration — la boucle
`Données cliniques → IA / bioinformatique → biomarqueur candidat → validation biologique → validation clinique`
Chaque tour resserre la définition du phénotype et la signature ; aucune étape n'est
franchie sans relecture clinique.

---

# Section 16 — TOP 5 des collaborations françaises

Grille (chaque axe /10 ; total pondéré /70 ; poids : accès données ×1,5 ; expertise Tx
cardiaque ×1,25 ; potentiel collaboration ×1,25 ; sci., immuno., IA ×1,0).

| Rang | Équipe | Sci. | Accès données | Tx cardiaque | Immuno. | IA/bioinfo | Collab. | **Total /70** |
|---|---|---|---|---|---|---|---|---|
| 1 | **Paris Transplant Group / PITOR** (Loupy, Coutance, Duong Van Huyen) — PARCC | 9 | 8 | 9 | 8 | 10 | 8 | **60,25** |
| 2 | **Pitié-Salpêtrière — programme greffe cardiaque** (Coutance, Varnous) | 8 | 8 | 10 | 7 | 7 | 8 | **56,50** |
| 3 | **CR2TI Nantes** (Brouard, Danger) | 9 | 6 | 5 | 9 | 8 | 8 | **51,25** |
| 4 | **CIRI Lyon — NOPAB** (Thaunat) | 8 | 6 | 5 | 9 | 6 | 7 | **47,00** |
| 5 | **C2VN Équipe 3 / immunogénétique — AP-HM Marseille** (Pascale Paul) | 7 | 5 | 7 | 8 | 5 | 6 | **43,75** |

**Lecture** :
- Le **duo parisien** (1 & 2, en partie la même personne côté recherche : G. Coutance)
  domine sur *cœur + données + IA*.
- **Nantes** est n°3 malgré un accès cardiaque faible, parce que c'est l'équipe la plus
  alignée sur le **concept même de signature de tolérance** — précieuse en
  **co-encadrement méthodologique** même si elle n'apporte pas la cohorte cardiaque.
- **Marseille (C2VN Éq. 3, P. Paul)** : PI/unité confirmés ; angle NK CD16 / CAV
  original mais rôle attendu = **partenaire biologie/validation**, pas fournisseur de
  cohorte multi-omique longitudinale.

---

# Section 17 — « Si vous ne deviez en contacter qu'une, laquelle ? »

## Recommandation : **Paris Transplant Group / PITOR (PARCC), en visant l'angle cœur avec Guillaume Coutance, sous l'égide d'Alexandre Loupy.**

**Pourquoi eux :**
1. **Seule équipe française** réunissant déjà *cohortes cardiaques + transcriptome de
   biopsie + IA* opérationnels (MMDx-Heart, panel Banff HOT AMR cardiaque, heart HistoMX,
   essai NCT06436027).
2. G. Coutance fait le **pont** entre la recherche (PARCC) et le **plus gros programme de
   greffe cardiaque d'Europe** (Pitié) → un seul contact ouvre les deux.
3. Culture **explicite de l'IA en transplantation** (iBox) : ils parlent le même langage
   méthodologique (validation externe, calibration, TRIPOD).

**Le risque à gérer, et comment :**
- Ils sont **très forts en ML en interne** → ne pas se présenter comme « le ML ». Se
  présenter comme apportant **l'angle *tolérance / stabilité immunologique profonde***
  (qu'ils n'ont pas priorisé), la **méthodologie signature multi-omique** (inspirée des
  travaux de tolérance rénale de Nantes), et une **paire de bras** dédiée, reproductible,
  sur données publiques dès le départ (Scénario A) — donc **peu coûteuse** pour eux.
- Proposer d'emblée un **livrable Scénario A** (réanalyse harmonisée MMDx/GEO pour définir
  la classe « absence durable de signal moléculaire de rejet ») comme **preuve de
  sérieux** avant toute demande d'accès à leurs données.

**Plan de contact :**
1. **Email court** (Section 18/19) → Guillaume Coutance, en copie/mention d'Alexandre
   Loupy, via l'adresse institutionnelle PARCC (`parcc.inserm.fr/contact/`) ou le
   formulaire `paristransplantgroup.com`. Objet centré « signature de tolérance / IA ».
2. Joindre le **one-pager** ([`../outreach/one_pager.md`](../outreach/one_pager.md)).
3. Proposer un **échange de 20–30 min** ; venir avec le plan Scénario A prêt.
4. **En parallèle, contact « méthodologique » de Nantes (Brouard)** possible en n°2, sans
   concurrence : rôle de co-encadrement signature, pas d'accès données requis.
5. Relance à **J+10** si pas de réponse.

**Avant envoi : validation par Dr. Tall** (identité, périmètre de l'offre, cible
nominative).

---

# 18. Brouillon d'email — Français
# Brouillon email — Français  *(non validé — ne pas envoyer sans accord de Dr. Tall)*

> **Cible n°1 :** Dr Guillaume Coutance (volet cœur), en mentionnant le Pr Alexandre Loupy
> — Paris Transplant Group / PITOR, PARCC (INSERM UMR-S 970).
> Voie : adresse institutionnelle PARCC (https://parcc.inserm.fr/contact/) ou formulaire
> https://paristransplantgroup.com — **pas** d'adresse personnelle non vérifiée.
> Court, professionnel, non commercial, orienté collaboration. Ne rien affirmer de non validé.

---

**Objet :** Collaboration possible — signature IA / multi-omique de tolérance après transplantation cardiaque

Bonjour Docteur Coutance,

Je suis Mamadou Lamine Tall, PhD en bioinformatique et data science (MedFlow AI,
Montpellier). Je travaille sur l'intégration multi-omique et le machine learning
appliqués aux données de transplantation.

Vos travaux avec le Paris Transplant Group sur le phénotypage moléculaire du rejet
d'allogreffe cardiaque (panel Banff HOT, diagnostic moléculaire intra-greffon, approches
IA du risque) font de votre équipe la mieux placée en France sur ce sujet.

Nous avons identifié une question qui nous semble peu explorée du côté cardiaque : chez
les receveurs très stables à long terme — sans rejet, sans DSA de novo, sans vasculopathie
du greffon, sous immunosuppression minimale — existe-t-il une **signature immunologique ou
multi-omique reproductible de tolérance / stabilité profonde**, que l'IA permettrait
d'identifier et de suivre longitudinalement ? L'objectif est la découverte de
biomarqueurs, à visée de validation prospective ; le projet ne présuppose jamais un arrêt
de l'immunosuppression.

Ce que nous pourrions apporter concrètement : intégration multi-omique, modèles
prédictifs (survie, approches multimodales), pipelines reproductibles, et une
méthodologie de découverte de signature adaptée aux petites cohortes très
multidimensionnelles, avec validation externe. Nous pouvons démarrer sur données
publiques (réanalyse harmonisée de jeux de biopsies cardiaques) avant toute sollicitation
de vos données.

Seriez-vous disponible pour un échange de 20 à 30 minutes afin d'évaluer la pertinence de
cette question et une éventuelle collaboration ? Je m'adapte à vos disponibilités dans les
prochaines semaines. Un résumé d'une page est joint.

Bien cordialement,

Dr. Mamadou Lamine Tall
PhD, Bioinformatique & Data Science — MedFlow AI
contact@medflow-ai.fr · https://medflow-ai.fr

---

# 19. Brouillon d'email — English
# Draft email — English  *(not validated — do not send without Dr. Tall's approval)*

> **Target #1:** Dr Guillaume Coutance (heart programme), mentioning Prof. Alexandre Loupy
> — Paris Transplant Group / PITOR, PARCC (INSERM UMR-S 970).
> Route: PARCC institutional contact (https://parcc.inserm.fr/contact/) or the form at
> https://paristransplantgroup.com — **not** an unverified personal address.
> Short, professional, non-commercial, collaboration-oriented. State nothing unverified.

---

**Subject:** Possible collaboration — AI / multi-omic signature of tolerance after heart transplantation

Dear Dr Coutance,

I am Mamadou Lamine Tall, PhD in bioinformatics and data science (MedFlow AI, Montpellier,
France). My work focuses on multi-omics integration and machine learning applied to
transplantation data.

Your work with the Paris Transplant Group on molecular phenotyping of cardiac allograft
rejection (Banff HOT panel, intra-graft molecular diagnosis, AI-based risk approaches)
makes your team the best positioned in France on this topic.

We have identified a question that seems under-explored on the cardiac side: among
long-term, very stable recipients — no rejection, no de novo DSA, no cardiac allograft
vasculopathy, on minimal immunosuppression — is there a **reproducible immunological or
multi-omic signature of tolerance / deep stability** that AI could identify and track
longitudinally? The aim is biomarker discovery toward prospective validation; the project
never assumes withdrawal of immunosuppression.

What we could concretely contribute: multi-omics integration, predictive models (survival,
multimodal approaches), reproducible pipelines, and a signature-discovery methodology
suited to small, high-dimensional cohorts, with external validation. We can start on
public data (harmonised re-analysis of cardiac biopsy datasets) before requesting any of
your data.

Would you be available for a 20–30 minute call to assess the relevance of this question
and a possible collaboration? I can work around your availability over the coming weeks.
A one-page summary is attached.

Best regards,

Dr. Mamadou Lamine Tall
PhD, Bioinformatics & Data Science — MedFlow AI
contact@medflow-ai.fr · https://medflow-ai.fr

---

# 20. Références
# Références

Bibliographie du dossier CardioTolerance-AI. Une entrée par source **vérifiée**
(consultée via recherche web, lien confirmé). Preprints (bioRxiv / medRxiv) explicitement
étiquetés. Les identifiants précis (DOI, PMID, volume/pages) restant à confirmer sont
marqués « [ref exacte à confirmer] ». Ordre : par thème de la Section 3.

---

## Contexte clinique — survie, rejet, CAV

- [R1] Registry of the ISHLT (rapport annuel). *J Heart Lung Transplant.* — survie
  adulte ~95 %/84 %/72 % à 1/5/10 ans, médiane ~10,7 ans.
  https://www.jhltonline.org/article/S1053-2498(12)01210-7/pdf — [contexte]
- [R2] Heart Transplantation Rejection. *StatPearls*, NCBI Bookshelf.
  https://www.ncbi.nlm.nih.gov/books/NBK537057/ — [contexte : causes de décès ; CAV
  ~8 %/30 %/50 % à 1/5/10 ans]
- [R3] Twenty-Year Survivors of Heart Transplantation (registre ISHLT). *Am J
  Transplant.* https://www.amjtransplant.org/article/S1600-6135(22)05687-8/pdf —
  [survie sans rejet ~19 %/13 %/13 % à 1/10/20 ans ; sans CAV ~42 % à 20 ans]
- [R4] Diagnosis of rejection following heart transplantation: diving into the future.
  *Front Transplant.* 2025.
  https://www.frontiersin.org/journals/transplantation/articles/10.3389/frtra.2025.1693821/full
  — [revue ; limites de la BEM]

## Tolérance opérationnelle — foie, rein, organe solide

- [R5] Brouard S, et al. Operational tolerance in kidney transplantation and associated
  biomarkers. *PMC5508347.* https://pmc.ncbi.nlm.nih.gov/articles/PMC5508347/ —
  [définition ; signature B ; MS4A1/TCL1A]
- [R6] Approaching the Promise of Operational Tolerance in Clinical Transplantation.
  *Transplantation.*
  https://journals.lww.com/transplantjournal/fulltext/10.1097/tp.0b013e318215e742~approaching-the-promise-of-operational-tolerance-in-clinical
  — [rareté ; foie 27 % sevrés (16/59)]
- [R7] Longitudinal biomarker progression and validation for predicting operational
  tolerance in a prospective multicenter liver IS-withdrawal trial. *PMC12685220.*
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12685220/ — [biomarqueurs longitudinaux, foie]
- [R8] Biomarkers of operational tolerance in solid organ transplantation. *PMC3442251.*
  https://pmc.ncbi.nlm.nih.gov/articles/PMC3442251/ — [empreintes foie ≠ rein]
- [R9] Incidental detection of operational tolerance in a kidney recipient lost to
  follow-up >10 years: case report + review. *PMC9948746.*
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9948746/ — [découverte fortuite]
- [R10a] Newell KA, et al. Identification of a B cell signature associated with renal
  transplant tolerance in humans. *J Clin Invest.* 2010;120(6):1836–47.
  https://www.jci.org/articles/view/39933 — [signature sanguine B ; set de 3 gènes ;
  ↑ CD20 dans le sédiment urinaire ; ↑ B naïfs/transitionnels]
- [R10b] Sagoo P, et al. Development of a cross-platform biomarker signature to detect
  renal transplant tolerance in humans. *J Clin Invest.* 2010;120(6):1848–61.
  https://www.jci.org/articles/view/39922 — [signature cross-platform ; 170 gènes,
  enrichis en gènes B]
- [R10c] Common gene signature across multiple studies — tolerance to renal allograft.
  *PMC4424816.* https://ncbi.nlm.nih.gov/pmc/articles/PMC4424816 — [ITN/RISET ; MS4A1, TCL1A]

## Minimisation de l'immunosuppression en transplantation cardiaque

- [R11] Minimization of Immunosuppression in Heart Transplantation. In: *SpringerLink*,
  2025. https://link.springer.com/chapter/10.1007/978-3-031-88290-6_14 —
  [~40 % sans corticoïdes à long terme ; essai multicentrique retrait ICN de novo — ref à confirmer]
- [R12] Extracorporeal Photopheresis With Low-Dose Immunosuppression in High-Risk Heart
  Transplant Patients — pilot. *PMC8983826.*
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8983826/ — [AMR 3,6 %, ACR 14,3 %]
- [R13] Immunosuppression Management in Heart Transplantation. *PMC12082473.*
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12082473/ — [difficulté de sélection des
  patients à très faible risque immunologique]

## Signatures immunologiques — Treg, B, TCR/BCR, DSA/HLA

- [R14] Preclinical and clinical developments in Treg therapy for heart transplantation.
  *ScienceDirect S0198885926000273*, 2026.
  https://www.sciencedirect.com/science/article/pii/S0198885926000273 —
  [Treg → survie prolongée, prévention CAV ; transfert seul insuffisant en MHC-mismatch]
- [R15] Tracking of TCR-Tg T cells reveals multiple mechanisms maintaining cardiac
  transplant tolerance in mice. *PMC6241514.*
  https://ncbi.nlm.nih.gov/pmc/articles/PMC6241514 — [PD-1 élevé sur Treg intra-greffon ; murin]
- [R16] Autologous Treg therapy to prevent CAV in paediatric heart transplant recipients.
  *Front Immunol.* 2024.
  https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1444924/full
- [R17] Subclinical rejection-free diagnostic after kidney transplantation using blood
  gene expression. *Kidney Int.* 2023. PubMed 36990211.
  https://pubmed.ncbi.nlm.nih.gov/36990211/ — [Nantes/CR2TI ; score 6 gènes ↓ si DSA]
- [R18] scRNA-seq reveals PBMC immune landscape associated with operational tolerance in
  a kidney transplant recipient. *Am J Transplant.* 2023.
  https://www.amjtransplant.org/article/S1600-6135(23)00466-5/fulltext
- [R19] Tracking donor-reactive T cells: evidence for clonal deletion in tolerant kidney
  transplant patients. *Sci Transl Med.* 2015.
  https://www.science.org/doi/10.1126/scitranslmed.3010760
- [R20] Analysis of T-Cell Receptor Repertoire in Transplantation: Fingerprint of T
  Cell-mediated Alloresponse. *PMC8790170.*
  https://pmc.ncbi.nlm.nih.gov/articles/PMC8790170/ — [répertoire tolérant moins biaisé]
- [R21] Clinical application of immune repertoire sequencing in solid organ transplant.
  *PMC9971933.* https://pmc.ncbi.nlm.nih.gov/articles/PMC9971933/
- [R22] HLA-DQ mismatches stimulate de novo DSA in heart transplant recipients.
  *ScienceDirect S019888592030149X.*
  https://www.sciencedirect.com/science/article/abs/pii/S019888592030149X
- [R23] Immunologic risk stratification of pediatric heart transplant patients combining
  HLA-EMMA and PIRCHE-II. *PMC10043167.*
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10043167/

## Multi-omics du rejet cardiaque

- [R24] Molecular Microscope Diagnostic System: Assessment of Rejection and Injury in
  Heart Transplant Biopsies. *Transplantation.* 2022. PubMed 36508644.
  https://pubmed.ncbi.nlm.nih.gov/36508644/ — [453 RATs ; TCMR/AMR/injury/atrophy-fibrosis]
- [R25] Halloran PF, et al. Redefining the molecular rejection states in 3230 heart
  transplant biopsies: relationships to parenchymal injury and graft survival. *Am J
  Transplant.* 2024;24(8). PubMed 38527588 ;
  https://www.sciencedirect.com/science/article/pii/S1600613524002417 — [3230 biopsies =
  1641 INTERHEART (NCT02670408) + 1589 de service ; 6 classifieurs, 7 archétypes : No
  rejection 48 %, Minor 24 %, TCMR1 2,3 %, TCMR2 2,7 %, TCMR/mixte 2,7 %, ABMR précoce
  3,9 %, ABMR établie 16 %]
- [R25b] Molecular Diagnosis of Rejection Phenotypes in 889 Heart Transplant Biopsies:
  The INTERHEART Study. ~2018.
  https://www.researchgate.net/publication/324148015 — [étude princeps INTERHEART]
- [R26] Building a tissue-based molecular diagnostic system in heart transplant
  rejection: the heart MMDx system. *J Heart Lung Transplant.*
  https://www.sciencedirect.com/science/article/abs/pii/S1053249817318302 —
  [331 BEM, 221 sujets, Edmonton/Bologne/Paris]
- [R27] Molecular Diagnosis of Heart Allograft Rejection Using Intra-Graft Targeted Gene
  Expression Profiling (heart HistoMX). ClinicalTrials NCT06436027 + *medRxiv*
  2024.09.24.24314238 (**preprint**).
  https://clinicaltrials.gov/study/NCT06436027 ·
  https://www.medrxiv.org/content/10.1101/2024.09.24.24314238.full.pdf
- [R28] Heart allograft rejection: molecular diagnosis using intra-graft targeted gene
  expression profiling. *Eur Heart J.* 2026;47(8):956. [pages/DOI à confirmer]
  https://academic.oup.com/eurheartj/article-abstract/47/8/956/8365742
- [R29] Banff Human Organ Transplant Consensus Gene Panel for AMR in Heart Allograft
  Biopsies. *PMC10515212.* https://pmc.ncbi.nlm.nih.gov/articles/PMC10515212/
- [R30] CareDx HeartCare Interpretive Guide (AlloMap 11 gènes informatifs ; AlloSure
  dd-cfDNA). https://www.caredx.com/wp-content/uploads/2021/09/LK-10482-Heartcare-Interpretive-Guide.pdf
  — [document industriel ; recommandation ISHLT pour AlloMap]
- [R31] Donor-derived cell-free DNA as a diagnostic biomarker for acute rejection in
  heart transplantation: systematic review and meta-analysis. PubMed 40132451, 2025.
  https://pubmed.ncbi.nlm.nih.gov/40132451/
- [R32] Noninvasive detection of graft injury after heart transplant using dd-cfDNA:
  prospective multicenter study (D-OAR). *PMC6790566.*
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6790566/ — [ref exacte à confirmer]
- [R33] Elevated Cardiac Troponin to Detect ACR After Cardiac Transplantation: SR &
  meta-analysis. *PMC9215116.* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9215116/ —
  [sensibilité 0,41 / spécificité 0,79]
- [R34] Diagnostic Accuracy of CMR for Cardiac Transplant Rejection: meta-analysis.
  *JACC Cardiovasc Imaging.* https://www.sciencedirect.com/science/article/pii/S1936878X21004277
  — [T2 mapping meilleure performance]

## Single-cell / single-nucleus & spatial

- [R35] scRNA-seq Identifies Intra-Graft Population Heterogeneity in Acute Heart
  Allograft Rejection in Mouse. *Front Immunol.* 2022. PMC8866760.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC8866760/ — [murin ; macrophages m3/m4]
- [R36] scRNA-seq reveals immune cell dynamics and local intercellular communication in
  acute murine cardiac allograft rejection. *Theranostics.* 2022. PMC9475451.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC9475451/ — [voie CXCR3]
- [R37] Single-nuclear RNA-seq of endomyocardial biopsies identifies persistence of
  donor-recipient chimerism with distinct signatures in severe CAV. *PMC9852032.*
  https://pmc.ncbi.nlm.nih.gov/articles/PMC9852032/ — [snRNA-seq BEM humaines faisable]

## IA / Machine learning — prédiction du rejet cardiaque

- [R38] Artificial intelligence optimizes immune rejection prediction and management in
  heart transplantation: structured narrative review. *Front Cardiovasc Med.* 2026.
  https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1790244/full
  — [signatures sang ALAS2/HBD/KLRD1 AUC>0,90 — à vérifier étude par étude ; qualité
  méthodo sous-optimale]
- [R39] Prediction of heart transplant rejection from routine pathology slides with
  self-supervised deep learning. *Eur Heart J Digit Health.* 2023. PMC10232288.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC10232288/ — [AUROC ~0,85 CV / 0,72–0,73 ext.]
- [R40] Non-invasive detection of cardiac allograft rejection using an ECG-based deep
  learning model. PubMed 36974261, 2023. https://pubmed.ncbi.nlm.nih.gov/36974261/ —
  [AUC ~0,84]
- [R41] Prediction of Acute Cardiac Rejection Based on Gene Expression Profiles. *J Pers
  Med.* 2024;14(4):410. https://doi.org/10.3390/jpm14040410
- [R42] Loupy A, et al. Prediction system for risk of allograft loss in patients
  receiving kidney transplants: international derivation and validation study (**iBox**).
  *BMJ.* 2019;366:l4923. PubMed 31530561 — [dérivation 4000 receveurs (3 hôpitaux FR,
  2005–2014) ; validation Europe 2129 + Amérique du Nord 1428 + 3 essais randomisés ;
  C-index 0,81 / 0,81 / 0,80]
- [R42b] Piening BD, et al. Whole transcriptome profiling of prospective endomyocardial
  biopsies reveals prognostic and diagnostic signatures of cardiac allograft rejection.
  *J Heart Lung Transplant.* 2022;41(6):840–848. PubMed 35317953 — [cohorte CTOT-03
  (NCT00531921) ; 26 receveurs / 125 EMB ; RNA-seq + random forest ; signature
  pronostique 0R/1R → prédit la prochaine biopsie 2R/3R avec ~90 % de précision ;
  fusionne les ex-entrées « CTOT-03 » et « JHLT-2022-EMB » du registre datasets]
- [R42c] Paul P, et al. Genetic and Functional Profiling of CD16-Dependent Natural Killer
  Activation Identifies Patients at Higher Risk of Cardiac Allograft Vasculopathy.
  *Front Immunol.* 2019;10:1208.
  https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2019.01208/pdf —
  [équipe C2VN, AP-HM Marseille ; NK CD16 / CAV]

## Méta-analyse dd-cfDNA & études primaires (Phase 2 — intégrées v0)

- [R43] Donor-derived cell-free DNA as a diagnostic biomarker for acute rejection in heart
  transplantation: a systematic review and meta-analysis. *Transplantation Reviews* 2025.
  PubMed 40132451 ; https://www.sciencedirect.com/science/article/abs/pii/S0955470X25000163
  — [10 études ; sens poolée 65 % (61–68), spéc 79 % (78–80), AUC 0,83 ; recherche
  jusqu'au 2024-08-01]
- [R44] Khush KK et al. Noninvasive detection of graft injury after heart transplant using
  donor-derived cell-free DNA: a prospective multicenter study (D-OAR). *Am J Transplant*
  2019. PubMed 30835940 ;
  https://www.amjtransplant.org/article/S1600-6135(22)09273-5/fulltext — [seuil ≥ 0,15 % ;
  sens 78,5 % (60,7–96,3), spéc 76,9 % (71,1–82,7)]
- [R45] Absolute Quantification of Donor-Derived Cell-Free DNA in Pediatric and Adult
  Patients After Heart Transplantation: a Prospective Study. *Transplant Int* 2023. PMC10641041 ;
  https://www.frontierspartnerships.org/journals/transplant-international/articles/10.3389/ti.2023.11260/full
  — [52 patients / 557 échantillons ; seuil 0,1 % ; AUC 0,78 (0,68–0,88), sens 92 %, spéc 56 %]
- [R46] Jiménez-Blanco M, Crespo-Leiro MG, et al. Donor-derived cell-free DNA as a new
  biomarker for cardiac allograft rejection: a prospective study (**FreeDNA-CAR**).
  *J Heart Lung Transplant* 2025;44:560–569. PubMed 39577511 ;
  https://www.jhltonline.org/article/S1053-2498(24)01953-3/fulltext — [**étude espagnole,
  12 centres** (Puerta de Hierro, 12 de Octubre, Gregorio Marañón, A Coruña, Bellvitge,
  Clínic, Sant Pau, CU Navarra, HU Central Asturias, V. Arrixaca, V. Rocío, La Fe) ;
  206 patients, 1090 paires EMB/dd-cfDNA, Allonext/NGS ; seuil 0,10 % ; **AUC 0,603**
  (0,513–0,692), sens 67 %, spéc 51 %, VPN 97 %, VPP 6,4 % ; inclusions 2019–2023]
- [R47] A two-threshold algorithm using donor-derived cell-free DNA fraction and quantity
  to detect acute rejection after heart transplantation. *Am J Transplant* 2025.
  https://www.amjtransplant.org/article/S1600-6135(25)00226-6/fulltext ; PMC12435761
- [R48] Lack of Usefulness of Donor-Derived Cell-Free DNA as a Biomarker for Cardiac
  Allograft Vasculopathy: a Prospective Study. *Front Cardiovasc Med* 2022.
  https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2022.856600/full
  — [**résultat négatif** pour la CAV]

## À ajouter en Phase 2 (identifiés, non encore intégrés)

- Piening BD et al. 2022 — localiser le **dépôt des données brutes** (section Data
  Availability : GEO / SRA / dbGaP ?).
- INTERHEART 889 — référence exacte (auteurs, journal, année).
- MMDx-Heart 3230 — n° de volume/pages exact (*Am J Transplant* 2024;24(8):xxxx).

## Corrections apportées

- **FreeDNA-CAR [R46]** : identifié à tort comme « français » dans une 1ʳᵉ version →
  **étude espagnole** (12 centres), Jiménez-Blanco / Crespo-Leiro, *JHLT* 2025;44:560–569.
  Corrigé dans §5, §7, `studies_registry.csv` (S03).
