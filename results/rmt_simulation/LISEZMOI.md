# SIMULATION — volet A (matrices aléatoires)

> **Données entièrement synthétiques.** Aucune donnée de patient, aucun résultat sur
> données réelles. Généré par `scripts/rmt_simulation.py` : ne pas modifier à la main.

Paramètres : p = 5000 gènes ; n = 20, 40, 80, 160 ; 200 tirages par cas ; 39 permutations par tirage ; α = 0.05 ; graine 20261126 ; durée 2.8 min.
Signatures cachées : 246 gènes (ℓ = 50), 76 gènes (ℓ = 16), 38 gènes (ℓ = 8.4), corrélation 0.2 dans chaque groupe.

## Faux axes retenus

| n | RMT : bord MP + Tracy-Widom | Permutations (analyse parallèle) | Bord MP seul | ACP à 10 axes fixes | 80 % de variance | Kaiser (λ > 1) |
|---|---|---|---|---|---|---|
| 20 | 0.01 / 4.0 % | 0.00 / 3.5 % | 0.01 / 6.0 % | 8.06 / 100.0 % | 13.04 / 100.0 % | 17.03 / 100.0 % |
| 40 | 0.01 / 1.0 % | 0.00 / 0.5 % | 0.01 / 4.0 % | 7.49 / 100.0 % | 28.45 / 100.0 % | 36.45 / 100.0 % |
| 80 | 0.01 / 1.5 % | 0.00 / 2.0 % | 0.01 / 7.5 % | 7.12 / 100.0 % | 57.41 / 100.0 % | 76.07 / 100.0 % |
| 160 | 0.00 / 2.5 % | 0.00 / 2.0 % | 0.00 / 10.0 % | 7.00 / 100.0 % | 115.00 / 100.0 % | 156.00 / 100.0 % |

Lecture : « faux axes en moyenne avec 3 signatures cachées / % de tirages avec au moins un faux axe sur bruit pur ».

## Détection de chaque signature par RMT (% des tirages)

| n | Facteur 1 | Facteur 2 | Facteur 3 |
|---|---|---|---|
| 20 | 94 % | 2 % (sous la limite) | 0 % (sous la limite) |
| 40 | 100 % | 24 % | 1 % (sous la limite) |
| 80 | 100 % | 89 % | 2 % (sous la limite) |
| 160 | 100 % | 100 % | 46 % |

## Fiabilité des axes retenus par RMT

Écart absolu moyen entre cos² prédit et observé : 0.015 (1315 axes).

| n | facteur | cos² prédit (moy.) | cos² observé (moy.) | précision des gènes (moy.) | axes |
|---|---|---|---|---|---|
| 20 | 1 | 0.135 | 0.147 | 0.41 | 189 |
| 20 | 2 | 0.054 | 0.044 | 0.18 | 3 |
| 40 | 1 | 0.254 | 0.263 | 0.67 | 200 |
| 40 | 2 | 0.077 | 0.066 | 0.35 | 49 |
| 40 | 3 | 0.077 | 0.036 | 0.28 | 2 |
| 80 | 1 | 0.422 | 0.425 | 0.91 | 200 |
| 80 | 2 | 0.132 | 0.136 | 0.69 | 178 |
| 80 | 3 | 0.088 | 0.053 | 0.41 | 3 |
| 160 | 1 | 0.600 | 0.602 | 0.99 | 200 |
| 160 | 2 | 0.275 | 0.275 | 0.97 | 200 |
| 160 | 3 | 0.103 | 0.098 | 0.76 | 91 |

Précision des gènes : part des m gènes les plus chargés sur l'axe qui appartiennent vraiment à la signature (m = taille de la signature).

## Limites

- Bruit gaussien homogène et signatures en blocs : cas idéal. Les vraies données ont des effets de lot, des gènes très variables et des signatures qui se chevauchent.
- Le test de Tracy-Widom (centrage de Johnstone, établi pour une covariance) est appliqué ici à une matrice de corrélation. Sur bruit pur, RMT a retenu au moins un faux axe dans 1,0 % à 4,0 % des tirages selon n, pour un niveau visé de 5 % (permutations : 0,5 % à 3,5 %).
- Ces résultats ne disent rien du rejet ni de la tolérance : ils valident l'outil.
