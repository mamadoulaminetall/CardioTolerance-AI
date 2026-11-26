# GSE124897 — cohorte 331 (découverte) : contrôle qualité

> Données publiques GEO (Parkes et al., *J Heart Lung Transplant* 2019). Généré par
> `scripts/rmt_gse124897_02_split_qc.py` : ne pas modifier à la main.
> **La cohorte 558 est scellée** (voir `SCELLE_cohorte558.md`) et n'entre dans aucun calcul ici.

## Données
- 331 puces × 49395 sondes (GPL15207, PrimeView), dont 102 sondes de contrôle AFFX.
- Prétraitement des auteurs (fiche GEO) : « Microarray data files were preprocessed using robust multi-chip averaging (RMA) implemented in Bioconductor. »
- Valeurs manquantes : 0 · étendue : 1.34 à 14.91 (échelle log2).
- Écart maximal entre les distributions triées des puces : 0.616 (0 = distributions identiques).
- Groupes (métadonnées GEO) : 3AA {'1': 210, '2': 38, '3': 83} ; 4AA {'1': 218, '2': 27, '3': 69, '4': 17}.

## Puces signalées (aucune exclue)
- Signal « distance » (distance moyenne > 0.391) : 26 puces.
- Signal « distribution » (score z modifié > 3,5) : 2 puces.
- Au total : 26 puces signalées sur 331.
- Doublons possibles (r > 0,999) : 0.

Répartition par groupe 4AA (un signal dans un groupe de rejet peut être biologique, pas technique) :

| groupe 4AA | non signalées | signalées | % signalées |
|---|---|---|---|
| 1 | 210 | 8 | 3,7 % |
| 2 | 22 | 5 | 18,5 % |
| 3 | 64 | 5 | 7,2 % |
| 4 | 9 | 8 | 47,1 % |

Les signaux sont inégalement répartis : de 3,7 % à 47,1 % selon le groupe (maximum : groupe 4). Une puce « éloignée des autres » dans un groupe de rejet ou de lésion peut être une biopsie biologiquement différente, pas une puce défectueuse : les exclure retirerait surtout des biopsies anormales. Signification exacte des groupes 4AA : à confirmer dans Parkes et al. 2019.

Détail par puce : `QC_cohorte331_puces.csv`.

## Variabilité des sondes (pour fixer le filtrage dans le préenregistrement)
- Écart-type par sonde, quantiles 5/25/50/75/95 % : 0.151 / 0.194 / 0.242 / 0.337 / 0.622.
- Sondes d'écart-type < 0,1 : 28 ; < 0,2 : 14092.

## Points à trancher dans le préenregistrement (étape 3)
1. **Normalisation.** Les valeurs GEO viennent d'un RMA fait par les auteurs ; la fiche ne dit pas
   si les 889 puces ont été normalisées ensemble. Si oui, la cohorte 558 a influencé les valeurs de
   la 331 (fuite légère). Option propre : refaire un RMA séparé par cohorte à partir des fichiers
   CEL (1,7 Go ; R/Bioconductor n'est pas installé sur ce poste).
2. **Exclusion des puces** : quelle règle (signaux ci-dessus ou aucune exclusion).
3. **Filtrage des sondes** : contrôles AFFX, sondes peu variables, passage sonde → gène.
4. **Non-indépendance** : 889 biopsies pour 454 patients, sans identifiant patient dans GEO.
5. **Effets de centre** : 8 centres, sans étiquette de centre dans GEO.
