# GSE124897 — résultats de l'analyse PRÉENREGISTRÉE

> Plan enregistré : https://osf.io/6htjn (2026-11-26 12:32 UTC). Code : étiquette `prereg-v1`
> + scripts `rmt_gse124897_03`–`05`. Généré par `scripts/rmt_gse124897_05_report.py` : ne pas éditer.
> Données publiques GEO ; cohorte 558 ouverte après vérification de son empreinte.

## Verdicts (critères de la section 6 du préenregistrement)

| Hypothèse | Résultat | Détail |
|---|---|---|
| **H1** RMT > ACP-10 (n = 20, 40, 80) | **NON soutenue** | n = 20 : RMT meilleur dans 100,0 % des tirages, différence médiane 0,0084 ; n = 40 : RMT meilleur dans 94,5 % des tirages, différence médiane 0,0094 ; n = 80 : RMT meilleur dans 2,5 % des tirages, différence médiane -0,0153 |
| **H2** faux axes sur données permutées ≤ 8 % | **soutenue** | n = 20 : 1,0 % ; n = 40 : 2,0 % ; n = 80 : 5,0 % ; n = 160 : 3,0 % |
| **H3** (exploratoire) fiabilité prédite | décrite | 145 axes RMT ; écart absolu moyen prédit/observé 0,366 |

Référence (cohorte 558, 558 biopsies, 18836 gènes) : K_ref = 37 axes par analyse parallèle (plan) ; RMT y retient 244 axes (variance du bruit réestimée à 0,219).

## Critère principal D et nombre d'axes (médianes sur 200 tirages)

| méthode | k (n = 20) | k (n = 40) | k (n = 80) | k (n = 160) | D (n = 20) | D (n = 40) | D (n = 80) | D (n = 160) |
|---|---|---|---|---|---|---|---|---|
| RMT : bord MP + Tracy-Widom (testé) | 16 | 30 | 52 | 89 | 0,207 | 0,258 | 0,277 | 0,261 |
| RMT, α = 0,01 | 15 | 29 | 52 | 89 | 0,207 | 0,258 | 0,277 | 0,262 |
| Permutations (analyse parallèle) | 4 | 7 | 12 | 17 | 0,140 | 0,215 | 0,310 | 0,403 |
| Bord MP seul (σ² = 1) | 5 | 7 | 12 | 17 | 0,141 | 0,216 | 0,310 | 0,403 |
| ACP à 10 axes (comparateur principal) | 10 | 10 | 10 | 10 | 0,199 | 0,249 | 0,291 | 0,321 |
| 80 % de variance | 11 | 19 | 34 | 61 | 0,202 | 0,277 | 0,327 | 0,327 |
| Kaiser (λ > 1) | 19 | 39 | 79 | 159 | 0,203 | 0,235 | 0,221 | 0,173 |

## Analyses de vérification (préenregistrées) : RMT meilleur que l'ACP-10, % des tirages

| variante | n = 20 | n = 40 | n = 80 | n = 160 |
|---|---|---|---|---|
| principale | 100,0 % | 94,5 % | 2,5 % | 0,0 % |
| geo | 100,0 % | 86,5 % | 0,5 % | 0,0 % |
| exclusion | 100,0 % | 88,5 % | 0,5 % | 0,0 % |
| top5000 | 100,0 % | 100,0 % | 93,0 % | 0,0 % |

Avec la référence choisie par RMT (K_ref = 244) : voir colonne `D_refRMT` des fichiers de tirages.

## S2 stabilité entre tirages (D médian entre paires) et S3 faux axes sur données permutées (%)

| méthode | S2 n = 20 | S2 n = 40 | S2 n = 80 | S2 n = 160 | S3 n = 20 | S3 n = 40 | S3 n = 80 | S3 n = 160 |
|---|---|---|---|---|---|---|---|---|
| RMT : bord MP + Tracy-Widom (testé) | 0,219 | 0,262 | 0,346 | 0,503 | 1,0 | 2,0 | 5,0 | 3,0 |
| RMT, α = 0,01 | 0,223 | 0,263 | 0,346 | 0,503 | 0,0 | 1,0 | 0,0 | 2,0 |
| Permutations (analyse parallèle) | 0,408 | 0,483 | 0,601 | 0,736 | 4,0 | 2,0 | 6,0 | 3,5 |
| Bord MP seul (σ² = 1) | 0,407 | 0,483 | 0,601 | 0,736 | 4,0 | 3,0 | 12,5 | 8,0 |
| ACP à 10 axes (comparateur principal) | 0,280 | 0,437 | 0,621 | 0,793 | 100,0 | 100,0 | 100,0 | 100,0 |
| 80 % de variance | 0,271 | 0,325 | 0,398 | 0,535 | 100,0 | 100,0 | 100,0 | 100,0 |
| Kaiser (λ > 1) | 0,196 | 0,241 | 0,331 | 0,521 | 100,0 | 100,0 | 100,0 | 100,0 |

## S5 / H3 : recouvrement observé vs prédit (axes RMT de la cohorte 331 entière)

| axes | recouvrement observé (moy.) | prédit (moy.) |
|---|---|---|
| 1–10 | 0,360 | 0,955 |
| 11–37 | 0,080 | 0,731 |
| 38–145 | 0,007 | 0,281 |

## Écart déclaré au plan

- α = 0,01 appliqué à RMT seulement : avec 99 permutations, « p < 0,01 » est impossible pour l'analyse parallèle.

## Lecture (à reprendre dans l'article)

- Contre du bruit pur, le test de Tracy-Widom tient son niveau (H2). Le bord MP seul, sans test, dépasse 8 % à n = 80.
- Sur ces données réelles, le modèle « quelques axes + bruit homogène » ne tient pas : la variance du bruit est
  réestimée très bas et RMT retient de nombreux axes faibles (médiane 16 à 89 selon n ; 145 sur la 331 entière).
- RMT ne fait mieux que l'ACP-10 qu'à n = 20 et 40, avec un faible écart ; au-delà, les permutations et le bord MP
  seul (σ² = 1) donnent le meilleur accord avec la cohorte 558.
- La fiabilité prédite des axes (H3) est très optimiste sur données réelles : les axes individuels se répliquent
  mal d'une cohorte à l'autre, même quand le sous-espace se réplique.
- Limite du critère D : avec une référence de 37 axes, D favorise mécaniquement les méthodes qui retiennent
  plus d'axes aux petits n.
