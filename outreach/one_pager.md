# CardioTolerance-AI — Projet en une page  *(BROUILLON — non validé)*

> À finaliser après les phases 1–6 de `docs/02_ROADMAP.md`. Les crochets `[...]` marquent
> ce qui doit être rempli avec des éléments **vérifiés** (pas d'estimation inventée).
> Ce document est destiné à un·e PI / directeur·rice de laboratoire.

---

**Titre :** AI-driven discovery of immune tolerance signatures after heart transplantation
**Porteur :** Dr. Mamadou Lamine Tall, PhD (Bioinformatique & Data Science) — MedFlow AI, Castelnau-le-Lez (Montpellier)
**Contact :** contact@medflow-ai.fr · https://medflow-ai.fr
**Nature :** proposition de collaboration académique, non commerciale.

### Question scientifique
Existe-t-il, chez certains receveurs de greffe cardiaque, une signature immunologique /
multi-omique associée à une tolérance particulièrement élevée du greffon ? L'IA peut-elle
l'identifier, distinguer rejet et stabilité durable, et prédire longitudinalement le
risque de rejet ?
*Garde-fou : le projet ne suppose jamais l'arrêt de l'immunosuppression ; il vise des
biomarqueurs et profils à valider prospectivement, sous supervision médicale.*

### Ce qui manque aujourd'hui (gap — à documenter)
- [ce qui est établi] · [ce qui est controversé] · [ce qui n'a presque pas été étudié]
- Obstacle principal identifié : [manque de données longitudinales / faible n / hétérogénéité / absence de validation externe — à trancher d'après la revue]

### Ce que MedFlow AI apporte
Analyse multi-omique · machine learning (RF, XGBoost, Elastic Net, modèles de survie,
modèles multimodaux) · intégration de données · biomarker discovery · pipelines
reproductibles · plan statistique adapté au régime *p ≫ n* (régularisation, sélection de
variables stable, validation externe, SHAP, calibration).

### Ce que le centre apporte
Cohorte rétrospective de greffe cardiaque · données cliniques longitudinales · biopsies ·
HLA / DSA · éventuellement cytométrie / transcriptomique · expertise médicale et
validation biologique.

### Boucle de valeur
`Données cliniques → IA / bioinformatique → biomarqueur candidat → validation biologique → validation clinique`

### Scénario proposé pour démarrer
Scénario B : datasets publics ([datasets réellement accessibles — cf. registre]) +
cohorte rétrospective d'un centre français, pour un travail de développement et de
validation clinique aboutissant à 1–2 publications méthodologiques.

### Demande concrète
Un échange de 20–30 minutes pour évaluer ensemble la pertinence scientifique et la
faisabilité d'accès à une cohorte rétrospective.
