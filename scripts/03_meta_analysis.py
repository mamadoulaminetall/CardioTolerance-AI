"""03 — Méta-analyse quantitative (si justifiable) ou synthèse de preuves structurée.

Entrée : data/studies_registry.csv (produit par 02)

Décision préalable (à documenter dans meta-analysis/manuscript/) :
  méta-analyse quantitative uniquement si des études comparables rapportent une mesure
  d'effet homogène sur des endpoints alignés (indicativement >= 5). Sinon → evidence
  synthesis narrative structurée, avec justification explicite.

Si quantitative :
  - modèle à effets aléatoires (DerSimonian-Laird et REML)
  - hétérogénéité : tau^2, I^2, Q, intervalle de prédiction
  - forest plot        -> meta-analysis/figures/forest.png
  - funnel + Egger     -> meta-analysis/figures/funnel.png
  - sensibilité leave-one-out
  - sous-groupes (type de rejet, modalité omique, longitudinal vs transversal)
  - méta-régression (année, taille de cohorte, durée de suivi) si >= 10 études
  - sorties chiffrées  -> data/meta_estimates.csv  (consommé par l'app, page 4)

STATUT : STUB. Ne produire aucune estimation tant que le registre n'est pas rempli et
la décision quantitative/narrative tranchée.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "studies_registry.csv"
ESTIMATES = ROOT / "data" / "meta_estimates.csv"
FIG_DIR = ROOT / "meta-analysis" / "figures"


def main() -> None:
    raise SystemExit(
        "STUB — implémenter après remplissage de data/studies_registry.csv.\n"
        f"Entrée : {REGISTRY}\nSorties : {ESTIMATES}, {FIG_DIR}/forest.png, {FIG_DIR}/funnel.png"
    )


if __name__ == "__main__":
    main()
