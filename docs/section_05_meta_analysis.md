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
  - **FreeDNA-CAR 2024** (JHLT ; PubMed 39577511), prospective multicentrique **française
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
