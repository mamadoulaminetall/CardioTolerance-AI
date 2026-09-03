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
