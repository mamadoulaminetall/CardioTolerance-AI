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

- **Base** : une méta-analyse existe déjà ([R31], PubMed 40132451, 2025) → **réplication /
  mise à jour** avec recherche étendue et grille QUADAS-2.
- **Modèle** : bivarié à effets aléatoires (Reitsma) ; courbe **HSROC** ; sensibilité,
  spécificité, DOR, LR+ / LR− poolés.
- **Hétérogénéité** : I² adapté aux études diagnostiques ; exploration par **méta-régression**
  (seuil de positivité, type de rejet, assay, délai post-greffe).
- **Sous-groupes** : AMR vs TCMR ; seuil dd-cfDNA (0,15 % vs autres) ; adulte vs pédiatrie.
- **Biais** : Deeks' funnel plot test ; analyse de sensibilité (études à faible risque de
  biais uniquement).
- **Comparateurs non invasifs** (méta-analyses existantes, à citer, pas à recalculer) :
  troponine ([R33], sensibilité 0,41 / spécificité 0,79) ; **IRM T2 mapping** ([R34]).

## 5.5 Livrables de la section

- `data/studies_registry.csv` (toutes études) + sous-table `dd-cfDNA` pour la méta-analyse.
- `scripts/03_meta_analysis.py` → `meta-analysis/figures/` (HSROC, forest sens/spéc,
  funnel de Deeks) + `data/meta_estimates.csv` (consommé par l'app page 4).
- Diagramme **PRISMA** ; tables de risque de biais (**QUADAS-2**, **PROBAST**, **NOS**).
- Texte : synthèse narrative *tolérance* + tableau IA + résultats méta-analyse dd-cfDNA.

## 5.6 Statut

- ☑ Décision de méthode (ce document)
- ☐ Extraction `studies_registry.csv`
- ☐ Exécution méta-analyse dd-cfDNA
- ☐ Risque de biais + PRISMA
- ☐ Rédaction finale (bascule possible si l'extraction révèle plus d'études exploitables
  que prévu)
