# Contrôle technique : RMA par cohorte (D1) vs valeurs GEO des auteurs — cohorte 331

Fait le 2026-11-26, après l'enregistrement public du préenregistrement (https://osf.io/6htjn).
But : vérifier que les fichiers RMA sont lus correctement (orientation sondes × échantillons).
Ce contrôle ne fait pas partie des critères préenregistrés.

- RMA : `affy::justRMA` sur les 331 fichiers CEL de la cohorte 331 seuls (R 4.4.3, affy 1.84.0,
  primeviewcdf 2.18.0 ; voir `rma_sessionInfo_cohort331.txt`). 49 495 sondes (CDF) dont
  49 395 communes avec la série GEO.
- Corrélation par échantillon (49 395 sondes) entre notre RMA et les valeurs GEO :
  médiane 0,9982, minimum 0,9865. L'ordre des échantillons est identique.
- Corrélation par sonde entre échantillons (2 000 sondes tirées au hasard, graine 0) : médiane 0,924.
- Écart absolu moyen : 0,332 (log2).

Lecture : les fichiers sont bien lus. Les deux versions ne sont pas identiques : les auteurs ont
normalisé différemment (peut-être avec les 889 puces ensemble, ce que la fiche GEO ne précise pas).
C'est la raison de la décision D1 ; les valeurs GEO sont testées en analyse de vérification.

Sceau de la cohorte 558 vérifié (SHA-256 `5a44ac4ac80dda22c083b921941161410935bf26a25b21d7728b15e249ab5a0f`,
intact) avant la lecture de ses fichiers CEL, le 2026-11-26 vers 12:47 UTC.
