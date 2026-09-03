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

### E. Immunogénétique de la transplantation / CAV — AP-HM (Marseille)
- **PI / unité** : **Donnée non disponible / à confirmer** (noms cités dans la
  littérature transplantation marseillaise : Pascale Paul, Christophe Picard — à
  vérifier ; unité C2VN à confirmer).
- **Expertise** : biomarqueurs non invasifs de lésion endothéliale immune ; **CAV** ;
  immunogénétique HLA (EFS PACA). Étude NCT01569334.
- **Contact** : AP-HM (Timone / Hôpital Nord), Aix-Marseille Université, EFS PACA.
- **Pourquoi** : angle CAV/endothélium complémentaire ; **proximité de Montpellier**.
  Score prudent tant que PI/unité non confirmés.

## 7.3 À compléter (Phase 4 — suite)

- CHU avec programme de greffe cardiaque non encore fichés : **Rouen (Charles Nicolle)**,
  Bordeaux, Lille, Strasbourg, Rennes, Toulouse (Rangueil), Montpellier (Arnaud de
  Villeneuve), Clermont-Ferrand, Grenoble, Tours, Nancy.
- **EFS / laboratoires HLA** (national) : typage haute résolution, eplets, DSA.
- **Plateformes single-cell / génomique** mobilisables (ex. réseaux France Génomique).
- Registre **CRISTAL (Agence de la biomédecine)** : données nationales de greffe — voie
  d'accès réglementée à explorer pour la partie clinique/survie.
