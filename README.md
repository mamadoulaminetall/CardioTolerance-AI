# CardioTolerance-AI

**AI-driven discovery of immune tolerance signatures after heart transplantation**

Projet de recherche translationnelle — MedFlow AI · Dr. Mamadou Lamine TALL, PhD
(Bioinformatique & Data Science), Castelnau-le-Lez / Montpellier, France.
Contact : contact@medflow-ai.fr · https://medflow-ai.fr ·
page publique : https://medflow-ai.fr/cardiotolerance-ai.html

| | |
|---|---|
| **Statut** | Cadrage scientifique + montage de collaboration — **document de travail v1** |
| **Ce n'est pas** | un dispositif médical · un protocole PROSPERO déposé · un avis médical · un produit |
| **Créé** | 2026-09-03 |
| **Rapport** | [`docs/RAPPORT_FINAL.md`](docs/RAPPORT_FINAL.md) · [`docs/RAPPORT_FINAL.pdf`](docs/RAPPORT_FINAL.pdf) (58 p., figures incluses) |

> **Garde-fou scientifique (non négociable).** Le projet **ne suppose jamais** qu'un
> patient puisse arrêter ou réduire son immunosuppression. L'objectif est d'identifier des
> **biomarqueurs et des profils de tolérance** susceptibles d'être validés
> prospectivement, sous supervision médicale stricte.

---

## 1. La question

Chez certains receveurs de greffe cardiaque très stables à long terme — sans rejet, sans
DSA de novo, sans vasculopathie du greffon, sous immunosuppression minimale — existe-t-il
une **signature immunologique / moléculaire / cellulaire / multi-omique reproductible** de
tolérance, que l'IA peut identifier, distinguer des profils de rejet, et dont elle peut
**prédire la trajectoire longitudinale** ?

**Le gap, en une ligne :** la tolérance opérationnelle est biomarquée en transplantation
hépatique et rénale, mais **aucune signature validée n'existe pour le cœur** — et une
recherche PubMed « cœur + tolérance + IA » renvoie **0 article** (cf.
[`docs/section_04_systematic_review.md`](docs/section_04_systematic_review.md) §4.3bis).

---

## 1bis. Volet A en cours : séparer le signal du bruit (matrices aléatoires)

**Statut (26/11/2026) : étapes 1 et 2 faites (registre corrigé, module `scripts/rmt_denoise.py`,
simulation étiquetée ; GSE124897 téléchargé, cohorte 558 scellée, contrôle qualité de la 331).
Analyse principale non commencée : aucun résultat réel.**
Cerveau du volet : coffre Obsidian `RMT-Transplant/` (`/cerveau rmt`).

**Le problème.** Une cohorte de greffés cardiaques compte quelques dizaines à quelques centaines
de patients pour des milliers de gènes. Dans ce cas, le bruit seul fabrique de fausses
« signatures ». La théorie des matrices aléatoires fixe la limite que le bruit ne peut pas
dépasser : la loi de **Marchenko-Pastur** (λ₊ = (1 + √(p/n))² pour des données standardisées).
Seul ce qui la dépasse est retenu, puis doit se reproduire sur une cohorte indépendante.

**L'algorithme (module : `scripts/rmt_denoise.py` ; tests : `tests/test_rmt_denoise.py`)**
1. Préparation : normalisation, correction des effets de lot, standardisation par gène.
2. Spectre : valeurs propres de la matrice de corrélation gène × gène.
3. Seuil de Marchenko-Pastur, test de Tracy-Widom près du seuil.
4. Nettoyage : seuls les axes au-dessus du seuil sont gardés, et la matrice de corrélation est nettoyée (Bun, Bouchaud & Potters, *Phys Rep* 2017).
5. Validation : plan préenregistré (OSF), découverte sur une cohorte, validation sur l'autre, comparaison aux méthodes classiques.

Le module donne aussi, pour chaque axe retenu, sa taille réelle estimée et la **fiabilité attendue
de sa liste de gènes** (cos² entre l'axe estimé et le vrai, modèle « spiked » : Baik, Ben Arous &
Péché 2005 ; Paul 2007). Tests : la loi de Tracy-Widom calculée retrouve les quantiles publiés
(Johnstone 2001 : 0,45 / 0,98 / 2,02 pour 90 / 95 / 99 %).

**Simulation (étape 0) — DONNÉES SYNTHÉTIQUES, aucune donnée de patient.**
`scripts/rmt_simulation.py` → [`results/rmt_simulation/LISEZMOI.md`](results/rmt_simulation/LISEZMOI.md).
5 000 gènes, 20 à 160 échantillons, 3 signatures cachées, 200 tirages par cas :
- Les règles classiques retiennent des axes de pur bruit : en moyenne 7 à 8 (10 axes fixes), 13 à 115
  (80 % de variance) et 17 à 156 (Kaiser). RMT : au plus 0,01.
- Sur bruit pur, RMT retient au moins un faux axe dans 1 à 4 % des tirages (niveau visé 5 %) ;
  le bord de Marchenko-Pastur seul monte à 10 %, d'où le test de Tracy-Widom.
- La fiabilité prédite des listes de gènes colle à la réalité (écart moyen 0,015 sur 1 315 axes).
  Message pour l'article : à 20 échantillons, même la signature la plus forte n'a que 41 % de vrais
  gènes parmi ses gènes les plus chargés (99 % à 160 échantillons).
- Limite : bruit idéal (gaussien, homogène). Ces chiffres valident l'outil, pas un résultat sur le rejet.

**Données publiques vérifiées dans GEO le 26/11/2026**
| Jeu | Contenu réel | Remarque |
|---|---|---|
| GSE124897 | 889 biopsies endomyocardiques, 2 cohortes (331 et 558), puce GPL15207 | Étiquettes = archétypes **moléculaires** 3AA/4AA, pas d'histologie, donc aucune prétention diagnostique (source : Parkes et al., *JHLT* 2019;38:636-646) |
| GSE2596 | 63 puces bicolores = 52 échantillons biologiques + 11 réplicats ; étiquettes R (16) / N (34) / pré-R (3), plus des infections (Chagas 8, toxoplasmose 1) ; 2 lots | Validation externe exploratoire (source : Morgun et al., *Circ Res* 2006) |
| GSE2445 | 285 échantillons de **sang (PBMC)**, 3 plateformes ; étiquette = grade de la biopsie concomitante | Ce ne sont pas des biopsies (source : Deng et al., *Am J Transplant* 2006, étude CARGO) |

✅ `data/datasets_registry.csv` corrigé le 26/11/2026 d'après les fiches GEO (série et échantillons) :
GSE2596 = 63 puces (et non 43), GSE2445 = sang PBMC (et non des biopsies), GSE124897 = 889 biopsies
à étiquettes moléculaires (l'ancien « ~841 » oubliait le groupe 4AA n° 4).

**Originalité, formulation validée :** « À notre connaissance, la théorie des matrices aléatoires
n'a pas encore été appliquée à des données transcriptomiques de transplantation d'organe
(recherche PubMed et Europe PMC, texte intégral et prépublications, 26 novembre 2026). »
Ne jamais écrire « premier », *first* ou *novel* seuls, et refaire la recherche avant soumission.

**Article visé.** Prépublication bioRxiv, puis le JHLT (avec un coauteur clinicien) ou
Transplant International (en solo). Le module en ligne pourra faire l'objet d'un article dans JOSS.
Rédaction selon TRIPOD+AI, code ouvert. L'usage de l'IA sera déclaré dans les méthodes.

**Feuille de route.**
1. ✅ Correction du registre, `rmt_denoise.py`, simulation (étiquetée comme telle), 26/11/2026.
2. ✅ Téléchargement et contrôle qualité de GSE124897, 26/11/2026 : cohorte 558 **scellée** (empreinte SHA-256,
   aucune analyse avant OSF : [`results/rmt_gse124897/SCELLE_cohorte558.md`](results/rmt_gse124897/SCELLE_cohorte558.md)) ;
   cohorte 331 : 26 puces sur 331 signalées, aucune exclue, surtout dans les groupes 4AA 2 et 4
   ([`results/rmt_gse124897/QC_cohorte331.md`](results/rmt_gse124897/QC_cohorte331.md)). Les données restent en local (`data/geo/`, non versionné).
3. Préenregistrement : texte v1 prêt, [`docs/rmt_preregistration.md`](docs/rmt_preregistration.md)
   (code figé à l'étiquette `prereg-v1`). ✅ **Enregistré et public sur OSF : https://osf.io/6htjn**
   (Secondary Data Preregistration, 26/11/2026 12:32 UTC, après le sceau de la 558 posé à 11:08 UTC).
4. Analyse principale.
5. Manuscrit et prépublication.
6. Mail à PITOR, après validation.

**Garde-fous.** Ce volet porte sur la méthode et le rejet, pas sur la tolérance (aucun jeu public de greffés
cardiaques tolérants). Aucune donnée de patient en ligne. Jamais d'hypothèse d'arrêt de
l'immunosuppression. Riemann n'est **pas** utilisé : on peut le citer comme inspiration
(les zéros de zêta suivent les statistiques des matrices aléatoires), jamais comme base technique.

---

## 2. Ce que contient ce dépôt

| Livrable | Où |
|---|---|
| **Dossier de faisabilité** (20 parties : état de l'art, revue systématique, méta-analyse, datasets, paysage FR, gap Q1–Q10, projet IA, multi-omics, stats, validation, faisabilité A/B/C, impact, publications, collaboration, 1er contact, emails) | `docs/section_*.md` → assemblé en `docs/RAPPORT_FINAL.{md,pdf}` |
| **Application Streamlit** — support de discussion interactif (10 pages) | `app/app.py` |
| **Données seed** — registres d'études, de datasets, d'équipes ; scoring pondéré ; corpus PubMed | `data/*.csv`, `meta-analysis/data/*.csv` |
| **Figures** — radar & barres du scoring, paysage dd-cfDNA, diagramme PRISMA | `figures/*.png` |
| **Kit de prise de contact** — one-pager + emails FR/EN personnalisés (cible n°1) | `outreach/` |

---

## 3. Arborescence

```
CardioTolerance-AI/
├── README.md
├── requirements.txt                  streamlit · pandas · numpy · plotly (+ matplotlib, reportlab, pypdf pour les scripts)
├── .streamlit/config.toml            thème sombre
├── app/
│   └── app.py                        application Streamlit — 10 pages, filtres, graphes
├── docs/
│   ├── 00_PROMPT_BRIEF.md            prompt fondateur, verbatim (cahier des charges)
│   ├── 01_PROJECT_SPEC.md            plan du rapport (20 sections), scénarios A/B/C, grille de scoring
│   ├── 02_ROADMAP.md                 plan de travail en 8 phases + état d'avancement (☑ / ◐ / ☐)
│   ├── 02_question.md .. 15_16_17_collab.md   les sections rédigées du dossier
│   ├── references.md                 bibliographie vérifiée (R1–R48)
│   ├── RAPPORT_FINAL.md              rapport assemblé (régénéré par scripts/05)
│   └── RAPPORT_FINAL.pdf             export PDF (régénéré par scripts/06)
├── scripts/
│   ├── 01_build_lit_corpus.py        PubMed E-utilities → meta-analysis/data/{query_log,lit_corpus}.csv
│   ├── 02_generate_figures.py        data/*.csv → figures/*.png
│   ├── 03_meta_analysis.py           pooling DL sens/spéc + I² + ROC-space + forest (attend data/ddcfdna_2x2.csv)
│   ├── 04_build_app_data.py          contrôle de présence des 17 livrables de l'app
│   ├── 05_assemble_report.py         docs/section_*.md → docs/RAPPORT_FINAL.md
│   ├── 06_report_pdf.py              docs/RAPPORT_FINAL.md → docs/RAPPORT_FINAL.pdf (reportlab, police Unicode, figures embarquées)
│   ├── rmt_denoise.py                volet A : signal / bruit par matrices aléatoires (module + ligne de commande)
│   ├── rmt_simulation.py             volet A : SIMULATION sur données synthétiques → results/rmt_simulation/
│   ├── rmt_gse124897_01_download.py  volet A : téléchargement GEO + provenance SHA-256
│   └── rmt_gse124897_02_split_qc.py  volet A : cohortes 331/558, sceau de la 558, contrôle qualité de la 331
├── tests/
│   └── test_rmt_denoise.py           16 tests (Tracy-Widom vs table publiée, Marchenko-Pastur, bruit pur, signal caché)
├── results/
│   ├── rmt_simulation/               SIMULATION_*.csv / *.png + LISEZMOI.md (données synthétiques uniquement)
│   └── rmt_gse124897/                provenance, sceau de la cohorte 558, contrôle qualité de la 331 (aucune donnée brute)
├── data/                             CSV — générés/curés, ne pas éditer à la main
│   ├── studies_registry.csv          12 études seed (S01–S12) : dd-cfDNA, MMDx, IA, comparateurs tolérance
│   ├── datasets_registry.csv         5 jeux de données (GEO public / CTOT-03 / INTERHEART collaboration)
│   ├── french_teams.csv              5 équipes françaises vérifiées
│   ├── french_teams_scoring.csv      6 axes /10, total pondéré /70
│   └── meta_estimates.csv            méta-analyse dd-cfDNA publiée (rapportée) + ligne re-analyse + comparateurs
├── figures/                          PNG générés par scripts/02
├── meta-analysis/
│   ├── data/query_log.csv            8 requêtes PubMed journalisées (2026-09-07)
│   ├── data/lit_corpus.csv           670 références dédoublonnées (652 avec résumé)
│   ├── figures/                      sorties de scripts/03 (quand data/ddcfdna_2x2.csv existe)
│   └── scripts/  manuscript/
└── outreach/
    ├── one_pager.md                  projet en 1 page (PI / directeur de labo)
    ├── email_fr.md  email_en.md      brouillons personnalisés — NON envoyés, à valider par Dr. Tall
```

---

## 4. Lancer l'application

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/app.py
```

Pages : Résumé · État de l'art · Revue systématique (journal des requêtes + PRISMA) ·
Méta-analyse · Datasets (filtre par accès) · Paysage français (filtre par ville) ·
Gap & méthodologie · Faisabilité A/B/C · Collaboration & TOP 5 (radar + barres) ·
Prise de contact.

---

## 5. Régénérer les livrables

Tout est reproductible depuis `scripts/` (ordre indicatif) :

```bash
python scripts/01_build_lit_corpus.py     # requêtes PubMed → corpus (nécessite curl + accès réseau)
python scripts/02_generate_figures.py     # figures/*.png depuis data/*.csv
python scripts/03_meta_analysis.py        # méta-analyse dd-cfDNA — s'arrête tant que data/ddcfdna_2x2.csv n'existe pas
python scripts/04_build_app_data.py       # vérifie que les 17 livrables de l'app sont présents
python scripts/05_assemble_report.py      # docs/RAPPORT_FINAL.md
python scripts/06_report_pdf.py           # docs/RAPPORT_FINAL.pdf
python -m pytest tests/ -q                # tests du module rmt_denoise (~5 s)
python scripts/rmt_simulation.py          # SIMULATION volet A (~3 min) → results/rmt_simulation/
python -I scripts/rmt_gse124897_01_download.py   # GEO → data/geo/GSE124897/raw/ (545 Mo, local)
python -I scripts/rmt_gse124897_02_split_qc.py   # sceau 558 (vérifié si déjà posé) + CQ 331 (~10 s)
python scripts/rmt_denoise.py --input matrice.csv --genes-in-rows --out axes.csv   # sur une vraie matrice (en local)
```

Dépendances scripts (au-delà de `requirements.txt`) : `matplotlib`, `reportlab`, `pypdf`, `scipy`, `pytest`.

---

## 6. Données, provenance & règles de rigueur

- Les CSV de `data/` sont **curés à la main à partir de sources vérifiées** (abstracts
  PubMed, repositories officiels, pages institutionnelles) puis relus par script. Chaque
  champ non confirmé porte la mention littérale **« nd / à confirmer »** ou
  **« Donnée non disponible / à confirmer auprès de l'équipe. »**
- `meta-analysis/data/` est **entièrement généré** par `scripts/01` (API NCBI, read-only).
- **Rien n'est inventé** : ni donnée, ni dataset, ni DOI, ni coordonnée, ni performance de
  modèle, ni collaboration. Les preprints sont étiquetés comme tels.
- Statut connu à corriger : effectifs bruts (TP/FP/FN/TN) des études dd-cfDNA non extraits
  (nécessite l'accès aux textes intégraux) → `scripts/03` est prêt, il attend
  `data/ddcfdna_2x2.csv`.

---

## 7. Déploiement

| Surface | État |
|---|---|
| **Git** | ce dépôt |
| **OVH — page publique** | ✅ `landing/cardiotolerance-ai.html` en ligne : https://medflow-ai.fr/cardiotolerance-ai.html (page recherche/collaboration, hors grille d'outils). Section **Algorithme (volet A)** ajoutée le 26/11/2026 : `#algorithme` |
| **Streamlit Cloud** | ☐ à connecter — `share.streamlit.io` → New app → ce repo, branche `main`, **main file `app/app.py`** |

Workflow de mise à jour (chiffres / données / claims) : suivre la skill
`medflow-sync-deploy` et propager git + Streamlit + OVH dans le même passage.

---

## 8. Avancement

Voir [`docs/02_ROADMAP.md`](docs/02_ROADMAP.md). En bref : 20/20 sections rédigées (v1),
app fonctionnelle, corpus PubMed réel (670 réf.), cible n°1 = **Paris Transplant Group /
PITOR** (angle cœur via G. Coutance). Restent : screening des 670, extraction 2×2 pour la
méta-analyse, tables QUADAS-2/PROBAST, connexion Streamlit Cloud, envoi de l'email
(après validation de Dr. Tall).

**Depuis le 26/11/2026 :** le volet A (matrices aléatoires, données publiques) est cadré, voir §1bis.
Prochaine action : étape 1 (registre, `rmt_denoise.py`, simulation).

---

## 9. Collaborer

Ce projet cherche **un centre français de transplantation cardiaque** prêt à explorer,
sur une cohorte rétrospective anonymisée, l'existence d'une signature de tolérance.
Apports respectifs et boucle de valeur : `docs/section_15_16_17_collab.md`.
Écrire à **contact@medflow-ai.fr**.

---

## 10. Licence & mentions

© 2026 MedFlow AI · Dr. Mamadou Lamine TALL, PhD. Dépôt privé, usage interne et
partage contrôlé avec des partenaires académiques. Non-dispositif médical, non-avis
médical. Le contenu est un document de travail et peut évoluer.
