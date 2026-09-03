# CardioTolerance-AI — Projet en une page  *(BROUILLON v1 — non validé)*

> Destiné à un·e PI / directeur·rice de laboratoire. Les crochets `[...]` restent à
> remplir avec des éléments **vérifiés** après le premier échange (prévalence du
> phénotype, taille de cohorte, calendrier réglementaire).

---

**Titre :** AI-driven discovery of immune tolerance signatures after heart transplantation
**Porteur :** Dr. Mamadou Lamine Tall, PhD (Bioinformatique & Data Science) — MedFlow AI, Castelnau-le-Lez (Montpellier)
**Contact :** contact@medflow-ai.fr · https://medflow-ai.fr
**Nature :** proposition de collaboration académique, non commerciale.

### Question scientifique
Chez les receveurs de greffe cardiaque **très stables à long terme** (sans rejet, sans DSA
de novo, sans vasculopathie du greffon, sous immunosuppression minimale), existe-t-il une
**signature immunologique / multi-omique reproductible de tolérance ou de stabilité
immunologique profonde** ? L'IA peut-elle l'identifier, la distinguer des profils de
rejet, et en **prédire la trajectoire longitudinale** ?
*Garde-fou : le projet ne présuppose jamais l'arrêt de l'immunosuppression ; il vise des
biomarqueurs et des profils à valider prospectivement, sous supervision médicale.*

### Le gap (d'après une revue de littérature ciblée — sources disponibles)
- La **tolérance opérationnelle** est réelle et **biomarquée** en transplantation
  **hépatique et rénale** (ex. signature sanguine à dominante lymphocytaire B en rein),
  mais avec des empreintes **organe-spécifiques**.
- **En transplantation cardiaque** : aucune signature de tolérance validée, aucune série
  de cas robuste de sevrage complet en greffe cardiaque isolée.
- Le **rejet** cardiaque, lui, est finement caractérisé au plan moléculaire (systèmes de
  transcriptome de biopsie) et détectable de façon non invasive.
- Les modèles d'**IA** publiés détectent le rejet mais **généralisent mal** (chute en
  validation externe) et ne modélisent pas la *trajectoire* du risque.

### Ce que MedFlow AI apporte
Intégration multi-omique (transcriptome bulk & single-cell, TCR/BCR, recalcul des scores
de mismatch HLA moléculaire) · machine learning (modèles pénalisés, ensembles d'arbres,
modèles de survie, fusion multimodale) · découverte de signature avec **sélection de
variables stable** et **validation externe** · pipelines reproductibles · reporting normé
(TRIPOD+AI, PROBAST, PRISMA).

### Ce que le centre apporte
Cohorte rétrospective de greffe cardiaque · données cliniques longitudinales et suivi
(rejets, DSA, CAV, immunosuppression, survie) · biopsies · données HLA/DSA · expertise
médicale et **validation biologique** (cytométrie, qPCR, IHC, single-cell).

### Boucle de valeur
`Données cliniques → IA / bioinformatique → biomarqueur candidat → validation biologique → validation clinique`

### Démarrage proposé — en deux temps
1. **Scénario A (dès maintenant, sans données du centre)** : réanalyse harmonisée de jeux
   de biopsies cardiaques publics pour définir la classe « absence durable de signal
   moléculaire de rejet » et poser la méthode → note méthodologique / proof-of-concept.
2. **Scénario B (avec le centre)** : datasets publics + **cohorte rétrospective** d'un
   centre français → découverte et **validation clinique** de la signature, 1–2
   publications méthodologiques.

### Demande concrète
Un échange de **20–30 minutes** pour évaluer ensemble la pertinence scientifique et la
faisabilité d'un accès à une cohorte rétrospective.
