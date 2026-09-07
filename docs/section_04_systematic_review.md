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
