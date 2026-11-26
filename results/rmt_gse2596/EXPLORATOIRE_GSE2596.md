# GSE2596 — analyse EXPLORATOIRE (section 7 du préenregistrement https://osf.io/6htjn)

> **Sans hypothèse ni règle de décision : description seulement.** Données publiques GEO
> (Morgun et al., *Circ Res* 2006). Généré par `scripts/rmt_gse2596_exploratory.py`.

- Série GEO SHA-256 `1fc1edf40d29fd902dda4fa9b8e79fd0d233bb6823250eb21a8f067265771adf`.
- Échantillons biologiques après fusion des 11 paires de réplicats et exclusion des infections : 42 (Non-rejet 28, Rejet aigu 12, Pré-rejet 2), dont 7 non-rejets prélevés avant une réactivation de Chagas ; 30 patients distincts parmi eux (31 dans toute la série) : biopsies non indépendantes. Code patient lu par le nom du champ.
- Choix non prévus au plan (valeurs manquantes, AUC) : voir l'en-tête du script.

## Résumé

| analyse | n | spots | γ | σ² | axes RMT | bord MP (σ² = 1) | permutations |
|---|---|---|---|---|---|---|---|
| principale (spots ≥ 80 % présents, manques = 0) | 42 | 4254 | 103,8 | 0,226 | 34 | 10 | 10 |
| vérification (spots complets, sans remplacement) | 42 | 1480 | 36,1 | 0,222 | 29 | 8 | 8 |

## Axes et lien avec le rejet (rejet aigu vs non-rejet)

| analyse | axe | retenu RMT | % variance | p Tracy-Widom | p permutations | AUC | p Mann-Whitney (non corrigée) |
|---|---|---|---|---|---|---|---|
| principale (spots ≥ 80 % présents, manques = 0) | 1 | oui | 15,7 | < 1e-15 | 0,005 | 0,05 | 1e-05 |
| principale (spots ≥ 80 % présents, manques = 0) | 2 | oui | 8,8 | < 1e-15 | 0,005 | 0,27 | 0.024 |
| principale (spots ≥ 80 % présents, manques = 0) | 3 | oui | 7,0 | < 1e-15 | 0,005 | 0,44 | 0.56 |
| principale (spots ≥ 80 % présents, manques = 0) | 4 | oui | 5,9 | < 1e-15 | 0,005 | 0,57 | 0.49 |
| principale (spots ≥ 80 % présents, manques = 0) | 5 | oui | 5,5 | < 1e-15 | 0,005 | 0,45 | 0.63 |
| principale (spots ≥ 80 % présents, manques = 0) | 6 | oui | 4,4 | < 1e-15 | 0,005 | 0,61 | 0.28 |
| principale (spots ≥ 80 % présents, manques = 0) | 7 | oui | 4,0 | < 1e-15 | 0,005 | 0,51 | 0.96 |
| principale (spots ≥ 80 % présents, manques = 0) | 8 | oui | 3,6 | < 1e-15 | 0,005 | 0,66 | 0.11 |
| principale (spots ≥ 80 % présents, manques = 0) | 9 | oui | 3,4 | < 1e-15 | 0,005 | 0,46 | 0.71 |
| principale (spots ≥ 80 % présents, manques = 0) | 10 | oui | 3,1 | < 1e-15 | 0,005 | 0,61 | 0.29 |
| vérification (spots complets, sans remplacement) | 1 | oui | 17,4 | < 1e-15 | 0,005 | 0,08 | 3.8e-05 |
| vérification (spots complets, sans remplacement) | 2 | oui | 11,1 | < 1e-15 | 0,005 | 0,79 | 0.0044 |
| vérification (spots complets, sans remplacement) | 3 | oui | 8,2 | < 1e-15 | 0,005 | 0,60 | 0.34 |
| vérification (spots complets, sans remplacement) | 4 | oui | 7,2 | < 1e-15 | 0,005 | 0,39 | 0.27 |
| vérification (spots complets, sans remplacement) | 5 | oui | 5,8 | < 1e-15 | 0,005 | 0,49 | 0.94 |
| vérification (spots complets, sans remplacement) | 6 | oui | 4,5 | < 1e-15 | 0,005 | 0,47 | 0.78 |
| vérification (spots complets, sans remplacement) | 7 | oui | 3,9 | < 1e-15 | 0,005 | 0,65 | 0.13 |
| vérification (spots complets, sans remplacement) | 8 | oui | 3,5 | < 1e-15 | 0,005 | 0,58 | 0.42 |
| vérification (spots complets, sans remplacement) | 9 | oui | 3,2 | < 1e-15 | 0,965 | 0,53 | 0.76 |
| vérification (spots complets, sans remplacement) | 10 | oui | 2,8 | < 1e-15 | 1,000 | 0,43 | 0.47 |

Tableau limité aux 10 premiers axes ; tous les axes sont dans `EXPLORATOIRE_GSE2596_axes.csv`.

Lecture : AUC proche de 0,5 = l'axe ne sépare pas rejet et non-rejet ; proche de 0 ou de 1 = il les sépare (le signe d'un axe est arbitraire). Avec 12 rejets et 28 non-rejets, plusieurs par patient, ces chiffres sont indicatifs.
