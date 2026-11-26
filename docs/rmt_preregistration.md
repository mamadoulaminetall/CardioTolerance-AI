# Preregistration — v1 (ready for deposit)

**Random matrix theory to separate signal from noise in small heart-transplant biopsy
transcriptomic cohorts: a preregistered reanalysis of GEO GSE124897**

> **Status: v1, 2026-11-26. Not yet deposited on OSF.** Code and this text are frozen at the
> repository tag `prereg-v1`. Cohort 558 stays sealed until the OSF registration is time-stamped.
> Structure follows the usual questions of OSF templates for secondary data (hypotheses, data,
> prior knowledge of the data, variables, analysis plan, inference criteria, deviations); adapt
> the headings to the template chosen at deposit.

### Key decisions (settled 2026-11-26)

| # | Decision | Choice | Reason |
|---|---|---|---|
| D1 | Normalisation | Primary: RMA run **separately per cohort** from the CEL files. Sensitivity: authors' RMA values from GEO | GEO does not say whether the 889 arrays were normalised together; per-cohort RMA guarantees that cohort 558 cannot influence cohort 331 |
| D2 | Array exclusion | Primary: **none**. Sensitivity: exclude the 26 arrays flagged by the cohort-331 QC | Flags are concentrated in archetype groups 2 and 4 (18.5 % and 47.1 % vs 3.7 % in group 1): excluding them would mainly remove abnormal biopsies |
| D3 | Features | Probesets collapsed to genes (highest mean in cohort 331); AFFX controls and multi-gene probesets removed | Several probesets per gene would create artificial correlations; the rule is fixed on the discovery cohort only |
| D4 | Main comparator | PCA with a fixed number of components (k = 10) | Common practice in transcriptomics; parallel analysis, the stronger competitor, is reported as a secondary comparator |
| D5 | Reference structure | Cohort-558 principal subspace, size chosen by permutation parallel analysis | A reference that does not use the tested method, so it does not favour RMT |
| D6 | Decision rule for H1 | RMT better than PCA-10 in ≥ 80 % of 200 paired subsamples, at n = 20, 40 and 80 | Subsamples overlap, so p-values would be invalid; a paired, pre-specified rule is transparent and stringent |
| D7 | Affiliation | Independent researcher, MedFlow AI project, Castelnau-le-Lez, France | MedFlow AI is a research project, not yet a registered company |

---

## 1. Study information

**Author.** Mamadou Lamine Tall, PhD (bioinformatics). Independent researcher, MedFlow AI
project, Castelnau-le-Lez, France.

**Use of AI.** Code and text drafting were assisted by an AI assistant (Claude, Anthropic).
All scientific decisions are the author's. This will be stated in the article's methods.

**Background.** Transcriptomic cohorts in heart transplantation contain tens to a few hundred
biopsies for about 20,000 genes. In this regime, sample correlation matrices are dominated by
noise, and classical rules for choosing the number of principal components retain components
that do not replicate. Random matrix theory gives the expected spectrum of pure noise
(Marčenko–Pastur law) and the fluctuations of its upper edge (Tracy–Widom law), which allows
signal components to be separated from noise and their reliability to be predicted. To the
author's knowledge, random matrix theory has not yet been applied to organ-transplant
transcriptomic data (PubMed and Europe PMC searches, full text and preprints, 26 November 2026;
to be repeated before submission).

**Research question.** With a small cohort (20, 40, 80 or 160 biopsies drawn from cohort 331 of
GSE124897), does an RMT-guided method recover the molecular structure observed in the
independent cohort 558 better than classical methods?

**Hypotheses.**
- **H1 (primary).** For n ≤ 80, RMT selection (Marčenko–Pastur edge + Tracy–Widom test) yields
  higher agreement with the cohort-558 reference subspace than PCA with k = 10 components.
- **H2.** On permuted data (each gene permuted independently within the subsample), RMT
  retains at least one component in no more than 8 % of subsamples (nominal α = 5 %, plus a
  Monte Carlo margin for 200 subsamples).
- **H3 (exploratory).** For components retained by RMT on the full cohort 331, the
  reliability predicted by the spiked model agrees with the overlap observed against cohort 558.

**Scope.** This is a methods study on molecular rejection structure. It makes no diagnostic
claim and no claim about tolerance. It never assumes reduction or withdrawal of
immunosuppression.

---

## 2. Data

- **Dataset.** GEO GSE124897 (public since 2019): 889 endomyocardial biopsies from 454 recipients
  at eight centres. Initial cohort N = 331 and new cohort N = 558 (GEO overall design).
  Affymetrix PrimeView (GPL15207), 49,395 probesets. Original publication: Parkes MD et al.
  *J Heart Lung Transplant* 2019;38(6):636-646 (PMID 30795962).
- **Labels.** Sample characteristics give the cohort and the molecular archetype groups 3AA
  (groups 1–3) and 4AA (groups 1–4). These archetypes are **molecular** (derived from expression
  data), not histological. Group meanings will be quoted from Parkes et al. 2019.
- **Counts (GEO metadata).** Cohort 331: 3AA 210/38/83; 4AA 218/27/69/17.
  Cohort 558: 3AA 424/39/95; 4AA 427/25/75/31.
- **Files and versions.** Series matrix SHA-256 `50b9bb17700b31e77db597d01d59220bb8eb7c44ffd2c6d829fc45e24ada3b6c`
  (downloaded 2026-11-26). CEL archive: `GSE124897_RAW.tar` (889 CEL files), to be downloaded
  for D1 with its SHA-256 recorded before use.
- **Known limits.** Several biopsies per patient but no patient identifier in GEO (biopsies are
  not independent). No centre label in GEO (centre effects cannot be corrected). The authors'
  preprocessing is described only as "RMA implemented in Bioconductor"; whether the 889 arrays
  were normalised together is not stated.

---

## 3. Prior knowledge of the data (as of deposit)

- **Synthetic data only** were used to develop and test the method (`scripts/rmt_simulation.py`,
  results public in the repository).
- **Cohort 331.** Array-level quality control only: per-array median and interquartile range,
  mean distance and median correlation to other arrays, per-probe standard deviations. 26 of 331
  arrays were flagged (none excluded). The flags were cross-tabulated with 4AA groups: flag rates
  were 3.7 %, 18.5 %, 7.2 % and 47.1 % in groups 1 to 4. **Apart from this cross-tabulation of
  QC flags, no eigen-decomposition, PCA, RMT analysis or association with labels was computed on
  real expression data.**
- **Cohort 558. Sealed** on 2026-11-26T11:08:12Z before any analysis. Only its dimensions
  (558 × 49,395), the metadata group counts above and a content hash were computed:
  SHA-256 `5a44ac4ac80dda22c083b921941161410935bf26a25b21d7728b15e249ab5a0f`
  (method in `results/rmt_gse124897/SCELLE_cohorte558.md`, public on GitHub, commit c009f39).
  The hash will be checked before the first analysis of cohort 558.
- The author knows the design and abstract of the original publication (archetypes derived in
  cohort 331 and tested in cohort 558).

---

## 4. Preprocessing

1. **Normalisation (D1).** RMA run separately on cohort 331 and on cohort 558 from the CEL files
   (Bioconductor, PrimeView CDF; package versions recorded). Sensitivity analysis: the authors'
   GEO values.
2. **Features (D3).** Remove the 102 AFFX control probesets and probesets without a single gene
   symbol (annotations containing "///"). For each gene, keep the probeset with the highest mean
   expression in cohort 331. The same probeset list is then applied unchanged to cohort 558.
   Expected number of genes: about 18,836 (from the platform annotation).
3. **Arrays (D2).** No exclusion in the primary analysis, because the QC flags are concentrated
   in archetype groups 2 and 4 and may reflect biology. Sensitivity: exclusion of the 26 flagged
   arrays (list frozen in `results/rmt_gse124897/QC_cohorte331_puces.csv`).
4. **Standardisation.** Each gene is z-scored within the dataset being analysed (each subsample,
   the full cohort 331, cohort 558). No batch correction is possible (no centre label).

---

## 5. Analysis plan

**Methods compared** (all on the gene × gene correlation matrix of the same standardised data):
- **RMT** (tested method): components above the Marčenko–Pastur edge that pass a sequential
  Tracy–Widom test (α = 0.05), noise variance re-estimated. Implemented in
  `scripts/rmt_denoise.py`, default settings, code frozen at a tagged commit (`prereg-v1`).
- **PCA, k = 10** (main comparator, D4).
- Secondary comparators: Kaiser rule (eigenvalue > 1), 80 % cumulative variance, Marčenko–Pastur
  edge alone, permutation parallel analysis (99 permutations, α = 0.05, sequential).

**Reference structure (D5).** In cohort 558 (after unsealing), the number of reference
components K_ref is chosen by permutation parallel analysis (199 permutations, α = 0.05).
The reference subspace U_ref is spanned by the K_ref leading eigenvectors of its correlation
matrix. Sensitivity: K_ref chosen by RMT.

**Subsampling.** For each n ∈ {20, 40, 80, 160}, 200 random subsamples of cohort 331 are drawn
without replacement (seed 20261126). All methods are applied to the same subsamples (paired
design). Each method is also applied once to the full cohort 331 (n = 331).

**Theoretical detection limit** (from p ≈ 18,836 alone). A component is recoverable only if its
population eigenvalue exceeds 1 + √(p/(n−1)): about 32.5 (n = 20), 23.0 (n = 40), 16.4 (n = 80),
11.9 (n = 160) and 8.6 (n = 331). This is a property of the data dimensions, not a result.

**Primary outcome.** Subspace agreement with the reference:
D = 2‖U_refᵀ V‖²_F / (K_ref + k), where V holds the k orthonormal gene loadings retained by a
method (D = 0 if k = 0). D lies between 0 and 1 and penalises both missed structure and noise
components.

**Secondary outcomes.**
- S1. Number of components retained, per method and n.
- S2. Stability: D between pairs of subsamples of the same size (100 random pairs per n).
- S3. False positives on permuted data (H2): each gene permuted within the subsample, 200
  subsamples per n.
- S4. Capture of archetype structure in cohort 558: fraction of the between-group (4AA)
  variance lying in the subspace learned on the subsample, reported with k. These labels are
  derived from expression data, so this outcome is descriptive and makes no diagnostic claim.
- S5 (H3, exploratory). For each RMT component of the full cohort 331, matched to the cohort-558
  eigenvector with the largest overlap: observed squared overlap compared with the prediction
  ψ²(331) × ψ²(558) (product of the two predicted reliabilities).

**Sensitivity analyses.** GEO-processed values; exclusion of the 26 flagged arrays; the 5,000
most variable genes (chosen within each subsample); K_ref chosen by RMT; α = 0.01.

---

## 6. Inference criteria

Subsamples overlap, so no p-values are computed across subsamples; results are reported as
medians, interquartile ranges and paired comparisons.
- **H1 is supported** if, at each n ∈ {20, 40, 80}, the median paired difference D(RMT) − D(PCA-10)
  is positive **and** RMT has the higher D in at least 80 % of the 200 paired subsamples (D6).
  Results at n = 160 and n = 331 are reported without a decision rule.
- **H2 is supported** if the proportion of permuted subsamples in which RMT retains ≥ 1
  component is ≤ 8 % at every n.
- **H3** is exploratory: agreement is described (mean absolute difference, plot), with no
  decision rule.
- Results are reported whatever their direction, including if H1 is not supported or if
  parallel analysis performs as well as RMT.

---

## 7. Exploratory analysis (no hypothesis)

GSE2596 (63 two-colour arrays = 52 biological samples + 11 technical replicates; GPL1053;
Morgun et al. *Circ Res* 2006): average the technical replicates; keep acute rejection,
non-rejection and pre-rejection samples; exclude infection samples (Chagas reactivation,
toxoplasmosis); centre genes within each of the two batches ("summer", "winter"); apply RMT and
describe the retained components and their association with rejection status. GSE2445 (blood
PBMC) is not analysed in this study.

---

## 8. Deviations, data and code

- Any deviation from this plan will be reported in the article with its reason. Analyses not
  listed here will be labelled exploratory.
- Code: public repository CardioTolerance-AI (`scripts/rmt_*.py`, `tests/`), tag `prereg-v1` at
  deposit. Python 3.13, NumPy 2.4, SciPy 1.17, pandas 2.3; R/Bioconductor versions recorded at
  the normalisation step. Fixed random seeds.
- Data: public GEO data only. No patient data are collected or shared.
- Reporting: TRIPOD+AI where applicable. Preprint on bioRxiv before journal submission.
