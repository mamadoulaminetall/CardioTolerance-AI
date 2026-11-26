"""rmt_denoise — séparer le signal du bruit dans une matrice d'expression
grâce à la théorie des matrices aléatoires (loi de Marchenko-Pastur).

Volet A de CardioTolerance-AI · cerveau du volet : coffre Obsidian `RMT-Transplant/`.
Statut : module méthodologique, vérifié par `tests/test_rmt_denoise.py` et par la
simulation `scripts/rmt_simulation.py`. AUCUN résultat sur données réelles à ce stade.

Entrée : matrice X (n échantillons × p gènes), déjà normalisée et corrigée des effets
de lot. La théorie suppose un bruit à peu près homogène entre gènes et entre lots.

Étapes (fonction `denoise`) :
  1. standardize          z-score par gène ; gènes de variance nulle retirés.
  2. spectrum             valeurs propres de la matrice de corrélation p × p,
                          calculées par SVD sans jamais former la matrice p × p.
  3. mp_edges             bords de Marchenko-Pastur : λ± = σ²(1 ± √γ)², γ = p / N,
                          N = n − 1 (un degré de liberté perdu au centrage).
  4. tracy_widom_pvalues  fluctuations du plus grand « bruit » près de λ₊ :
                          loi de Tracy-Widom (β = 1), centrage de Johnstone (2001).
  5. select_components    axes retenus = valeurs propres au-dessus de λ₊ ET
                          significatives, test séquentiel arrêté au premier échec.
                          σ² (variance du bruit) est réestimée par point fixe :
                          trace = p = σ²(p − k + Σ ℓ_i).
  6. spike_estimates      taille réelle estimée de chaque axe retenu (ℓ) et fiabilité
                          attendue de son vecteur de gènes (cos² avec le vrai axe),
                          modèle « spiked » (Baik, Ben Arous & Péché 2005 ; Paul 2007).
  7. CleanedCorrelation   matrice de corrélation nettoyée par écrêtage des valeurs
                          propres (eigenvalue clipping, Bun, Bouchaud & Potters 2017),
                          stockée sous forme compacte (k vecteurs + une constante).
  8. permutation_null     contrôle négatif / analyse parallèle : chaque gène est
                          permuté indépendamment, ce qui détruit toute corrélation.

Garde-fous : outil de recherche, pas un dispositif médical. À exécuter en local ;
aucune donnée de patient ne doit être envoyée en ligne.

Références (volume et pages à revérifier avant l'article) :
  Marčenko VA, Pastur LA. Math USSR-Sbornik 1967;1(4):457-483.
  Johnstone IM. Ann Stat 2001;29(2):295-327.
  Baik J, Ben Arous G, Péché S. Ann Probab 2005;33(5):1643-1697.
  Paul D. Stat Sin 2007;17(4):1617-1642.
  Bun J, Bouchaud JP, Potters M. Phys Rep 2017;666:1-109.
  Ferrari PL, Spohn H. J Phys A 2005;38(33):L557-L561 (formule de F1 utilisée).
  Bornemann F. Math Comp 2010;79(270):871-915 (quadrature des déterminants de Fredholm).

Usage en ligne de commande :
  python scripts/rmt_denoise.py --input matrice.csv [--genes-in-rows] [--alpha 0.05]
         [--method tw|perm] [--n-perm 200] [--out axes.csv]
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from functools import lru_cache

import numpy as np
from scipy.special import airy

__all__ = [
    "standardize", "spectrum", "top_eigenvalues", "mp_edges", "mp_pdf",
    "tw1_cdf", "tw1_sf", "tw1_quantile", "johnstone_center_scale", "tracy_widom_pvalues",
    "spike_forward", "spike_estimates", "select_components", "permutation_null",
    "CleanedCorrelation", "RMTResult", "denoise",
]


# ---------------------------------------------------------------------------
# 1. Préparation
# ---------------------------------------------------------------------------
def standardize(X, ddof: int = 1):
    """z-score par colonne (gène). Renvoie (Z, masque des gènes gardés).

    Les gènes de variance nulle sont retirés (ils n'ont pas de corrélation définie).
    Les valeurs manquantes doivent être traitées avant (imputation ou filtrage).
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X doit être une matrice 2D (échantillons × gènes)")
    if X.shape[0] < 3:
        raise ValueError("il faut au moins 3 échantillons")
    if not np.isfinite(X).all():
        raise ValueError("valeurs manquantes ou infinies : les traiter avant")
    mu = X.mean(axis=0)
    sd = X.std(axis=0, ddof=ddof)
    keep = sd > 1e-12 * (np.abs(mu) + 1.0)
    if keep.sum() < 2:
        raise ValueError("moins de 2 gènes de variance non nulle")
    Z = (X[:, keep] - mu[keep]) / sd[keep]
    return Z, keep


# ---------------------------------------------------------------------------
# 2. Spectre
# ---------------------------------------------------------------------------
def spectrum(Z):
    """Valeurs propres non nulles de C = ZᵀZ / N (N = n − 1), triées par ordre décroissant.

    Renvoie (valeurs propres, U, s, V) avec Z = U diag(s) Vᵀ :
      V : vecteurs propres dans l'espace des gènes (p × m), « loadings » ;
      U·s : coordonnées des échantillons sur chaque axe (« scores »).
    m = min(N, p) : au-delà, les valeurs propres sont nulles par construction.
    """
    n, p = Z.shape
    N = n - 1
    U, s, Vt = np.linalg.svd(Z, full_matrices=False)
    m = min(N, p)
    return s[:m] ** 2 / N, U[:, :m], s[:m], Vt[:m].T


def top_eigenvalues(Z, k: int | None = None):
    """Valeurs propres seulement (rapide), via la plus petite des deux matrices de Gram."""
    n, p = Z.shape
    N = n - 1
    G = Z @ Z.T if n <= p else Z.T @ Z
    ev = np.linalg.eigvalsh(G)[::-1][: min(N, p)] / N
    return ev if k is None else ev[:k]


# ---------------------------------------------------------------------------
# 3. Marchenko-Pastur
# ---------------------------------------------------------------------------
def mp_edges(n_eff: int, p: int, sigma2: float = 1.0):
    """Bords (λ−, λ₊) du spectre de bruit pur : σ²(1 ± √γ)², γ = p / n_eff."""
    g = p / n_eff
    return sigma2 * (1 - np.sqrt(g)) ** 2, sigma2 * (1 + np.sqrt(g)) ** 2


def mp_pdf(x, n_eff: int, p: int, sigma2: float = 1.0):
    """Densité de Marchenko-Pastur des valeurs propres NON NULLES (intègre à 1 sur [λ−, λ₊]).

    Pour p > N, la loi complète a en plus une masse 1 − N/p en zéro ; on l'exclut ici
    pour pouvoir comparer directement à l'histogramme des min(N, p) valeurs propres.
    """
    g = p / n_eff
    lo, hi = mp_edges(n_eff, p, sigma2)
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    inside = (x > lo) & (x < hi)
    xi = x[inside]
    out[inside] = np.sqrt((hi - xi) * (xi - lo)) / (2 * np.pi * sigma2 * g * xi)
    return out / min(1.0, 1.0 / g)


# ---------------------------------------------------------------------------
# 4. Tracy-Widom (β = 1)
# ---------------------------------------------------------------------------
@lru_cache(maxsize=8)
def _leggauss(m: int):
    return np.polynomial.legendre.leggauss(m)


def _tw1_logcdf(s: float, m: int = 100) -> float:
    """log F1(s), F1(s) = det(I − K) sur L²(s, ∞), K(x, y) = ½ Ai((x + y) / 2).

    Quadrature de Gauss-Legendre sur [s, b] (Bornemann 2010) ; b est choisi pour que
    le noyau soit < 1e-12 au-delà. Passer par les valeurs propres μ_i de la matrice
    discrétisée donne log F1 = Σ log(1 − μ_i), précis aussi dans les queues.
    """
    if s < -10.0:
        return -np.inf
    t, w = _leggauss(m)
    b = max(24.0 - s, s + 8.0)
    x = 0.5 * (b - s) * t + 0.5 * (b + s)
    sw = np.sqrt(0.5 * (b - s) * w)
    A = 0.5 * airy(0.5 * (x[:, None] + x[None, :]))[0] * sw[:, None] * sw[None, :]
    mu = np.linalg.eigvalsh(A)
    if np.any(mu >= 1.0):
        return -np.inf
    return float(np.sum(np.log1p(-mu)))


def tw1_cdf(s, m: int = 100):
    """Fonction de répartition de Tracy-Widom β = 1 (cas réel)."""
    s_arr = np.atleast_1d(np.asarray(s, dtype=float))
    out = np.array([np.exp(_tw1_logcdf(v, m)) for v in s_arr])
    return out if np.ndim(s) else float(out[0])


def tw1_sf(s, m: int = 100):
    """1 − F1(s), calculée sans perte de précision dans la queue droite."""
    s_arr = np.atleast_1d(np.asarray(s, dtype=float))
    out = np.array([-np.expm1(_tw1_logcdf(v, m)) for v in s_arr])
    return out if np.ndim(s) else float(out[0])


@lru_cache(maxsize=32)
def tw1_quantile(q: float) -> float:
    """Quantile de Tracy-Widom β = 1 (ex. q = 0,95 → 0,9793 ; q = 0,99 → 2,0234)."""
    from scipy.optimize import brentq
    return float(brentq(lambda x: tw1_cdf(x) - q, -9.0, 12.0, xtol=1e-10))


def johnstone_center_scale(n_obs: int, p: int):
    """Centrage μ et échelle σ de Johnstone (2001) pour la plus grande valeur propre de XᵀX.

    X : n_obs observations gaussiennes indépendantes de dimension p, variance 1.
    (ℓ_max − μ) / σ suit approximativement Tracy-Widom β = 1.
    """
    a, b = np.sqrt(n_obs - 1.0), np.sqrt(float(p))
    return (a + b) ** 2, (a + b) * (1.0 / a + 1.0 / b) ** (1.0 / 3.0)


def tracy_widom_pvalues(eig, n_eff: int, p: int, sigma2: float = 1.0):
    """p-valeur de chaque valeur propre (triées) sous H0 « c'est du bruit ».

    Pour la i-ème (i = 0, 1, …), on suppose les i premières réelles et on compare λ_i
    à la plus grande valeur propre d'un bruit de dimension p − i (approximation
    séquentielle ; avec p ≫ i, le retrait de i dimensions change très peu le seuil).
    Les données centrées comptent pour N = n − 1 observations (n_eff).
    """
    eig = np.asarray(eig, dtype=float)
    pv = np.empty_like(eig)
    for i, lam in enumerate(eig):
        mu, sd = johnstone_center_scale(n_eff, p - i)
        pv[i] = tw1_sf((n_eff * lam / sigma2 - mu) / sd)
    return pv


# ---------------------------------------------------------------------------
# 5–6. Modèle « spiked » : taille réelle et fiabilité des axes
# ---------------------------------------------------------------------------
def spike_forward(ell, gamma: float):
    """Valeur propre d'échantillon attendue pour un axe réel de taille ℓ (unités de σ²).

    Au-dessus du seuil ℓ > 1 + √γ : λ = ℓ (1 + γ / (ℓ − 1)). En dessous, l'axe est
    noyé dans le bruit et sa valeur propre colle au bord (1 + √γ)².
    """
    ell = np.asarray(ell, dtype=float)
    thr = 1 + np.sqrt(gamma)
    with np.errstate(divide="ignore", invalid="ignore"):
        lam = ell * (1 + gamma / (ell - 1))
    return np.where(ell > thr, lam, thr ** 2)


def spike_estimates(eig, n_eff: int, p: int, sigma2: float = 1.0):
    """Pour chaque valeur propre : (ℓ estimé en unités de corrélation, cos² attendu).

    ℓ : inversion de `spike_forward` (Baik, Ben Arous & Péché 2005).
    cos² : (1 − γ/(ℓ−1)²) / (1 + γ/(ℓ−1)), recouvrement attendu entre le vecteur de
    gènes estimé et le vrai (Paul 2007). Proche de 1 : liste de gènes fiable ;
    proche de 0 : l'axe existe mais ses gènes sont surtout du bruit.
    En dessous du bord : ℓ = NaN et cos² = 0 (axe indiscernable du bruit).
    """
    g = p / n_eff
    x = np.asarray(eig, dtype=float) / sigma2
    ell = np.full_like(x, np.nan)
    cos2 = np.zeros_like(x)
    ok = x > (1 + np.sqrt(g)) ** 2
    a = 1 + x[ok] - g
    e = 0.5 * (a + np.sqrt(np.maximum(a * a - 4 * x[ok], 0.0)))
    ell[ok] = e
    cos2[ok] = np.clip((1 - g / (e - 1) ** 2) / (1 + g / (e - 1)), 0.0, 1.0)
    return ell * sigma2, cos2


# ---------------------------------------------------------------------------
# 5. Sélection des axes
# ---------------------------------------------------------------------------
def _leading_run(flags) -> int:
    flags = np.asarray(flags, dtype=bool)
    return int(len(flags) if flags.all() else np.argmin(flags))


def _sequential_k(eig, n_eff: int, p: int, sigma2: float, alpha: float) -> int:
    """Axes 1, 2, … gardés tant que λ_i > λ₊ ET statistique TW > quantile 1 − α."""
    _, lam_plus = mp_edges(n_eff, p, sigma2)
    s_crit = tw1_quantile(1.0 - alpha)
    k = 0
    while k < len(eig) and eig[k] > lam_plus:
        mu, sd = johnstone_center_scale(n_eff, p - k)
        if (n_eff * eig[k] / sigma2 - mu) / sd <= s_crit:
            break
        k += 1
    return k


def select_components(eig, n_eff: int, p: int, alpha: float = 0.05,
                      sigma2="auto", max_iter: int = 100, n_report: int = 20):
    """Nombre d'axes réels k, par le bord de Marchenko-Pastur + test de Tracy-Widom.

    sigma2 = "auto" : point fixe σ² = p / (p − k + Σ ℓ_i/σ²) (trace de la corrélation = p),
    ce qui abaisse le bord quand de vrais axes « prennent » de la variance au bruit.
    Renvoie un dict : k, sigma2, lambda_plus, k_mp, tw_pvalues (n_report premiers axes ;
    n_report = 0 pour ne pas les calculer, plus rapide).
    """
    eig = np.asarray(eig, dtype=float)
    s2 = 1.0 if sigma2 == "auto" else float(sigma2)
    k = 0
    for _ in range(max_iter):
        k = _sequential_k(eig, n_eff, p, s2, alpha)
        if sigma2 != "auto":
            break
        if k == 0:
            new = 1.0
        else:
            ell, _ = spike_estimates(eig[:k], n_eff, p, s2)
            new = p / (p - k + np.nansum(ell) / s2)
        if abs(new - s2) < 1e-10:
            break
        s2 = new
    _, lam_plus = mp_edges(n_eff, p, s2)
    n_rep = min(len(eig), max(n_report, k + 1)) if n_report else 0
    return {
        "k": k,
        "sigma2": s2,
        "lambda_plus": lam_plus,
        "k_mp": int(np.sum(eig > lam_plus)),
        "tw_pvalues": tracy_widom_pvalues(eig[:n_rep], n_eff, p, s2),
    }


# ---------------------------------------------------------------------------
# 8. Contrôle négatif par permutations
# ---------------------------------------------------------------------------
def permutation_null(Z, n_perm: int = 200, rng=None):
    """Plus grande valeur propre après permutation indépendante de chaque gène.

    Chaque colonne garde exactement ses valeurs (moyenne, variance, forme de la loi) ;
    seules les corrélations entre gènes sont détruites. Renvoie un tableau (n_perm,).
    """
    rng = np.random.default_rng(rng)
    out = np.empty(n_perm)
    for b in range(n_perm):
        out[b] = top_eigenvalues(rng.permuted(Z, axis=0), 1)[0]
    return out


def permutation_pvalues(eig, null_max):
    """p-valeur empirique de chaque λ_i contre le maximum du bruit permuté (variante prudente)."""
    null_max = np.asarray(null_max)
    return np.array([(1 + np.sum(null_max >= lam)) / (len(null_max) + 1) for lam in eig])


# ---------------------------------------------------------------------------
# 7. Matrice de corrélation nettoyée
# ---------------------------------------------------------------------------
@dataclass
class CleanedCorrelation:
    """C_nettoyée = V_k diag(λ_k) V_kᵀ + δ (I − V_k V_kᵀ), δ = (p − Σλ_k) / (p − k).

    Les valeurs propres du bruit sont toutes remplacées par leur moyenne δ (trace = p
    conservée). Forme compacte : la matrice p × p n'est construite que sur demande.
    """
    vectors: np.ndarray      # p × k
    eigenvalues: np.ndarray  # k
    bulk_value: float        # δ

    @property
    def p(self) -> int:
        return self.vectors.shape[0]

    def matvec(self, x):
        proj = self.vectors.T @ x
        return self.vectors @ ((self.eigenvalues - self.bulk_value) * proj) + self.bulk_value * x

    def to_dense(self, max_p: int = 5000):
        if self.p > max_p:
            raise MemoryError(f"p = {self.p} > {max_p} : utiliser matvec() ou augmenter max_p")
        V = self.vectors
        return (V * (self.eigenvalues - self.bulk_value)) @ V.T + self.bulk_value * np.eye(self.p)


# ---------------------------------------------------------------------------
# Résultat et fonction principale
# ---------------------------------------------------------------------------
@dataclass
class RMTResult:
    n: int
    p: int
    n_eff: int
    alpha: float
    method: str
    eigenvalues: np.ndarray        # toutes les valeurs propres non nulles
    sigma2: float
    lambda_minus: float
    lambda_plus: float
    k_mp: int                      # nombre au-dessus du bord de MP (sans test)
    k: int                         # nombre d'axes retenus
    tw_pvalues: np.ndarray
    perm_pvalues: np.ndarray | None
    loadings: np.ndarray           # p × r (r ≥ k premiers axes)
    scores: np.ndarray             # n × r
    singular_values: np.ndarray    # r
    genes_kept: np.ndarray         # masque sur les gènes d'entrée
    gene_names: np.ndarray | None = None
    sample_names: np.ndarray | None = None
    extra: dict = field(default_factory=dict)

    @property
    def gamma(self) -> float:
        return self.p / self.n_eff

    def spikes(self):
        """(ℓ estimé, cos² attendu) pour les k axes retenus."""
        return spike_estimates(self.eigenvalues[: self.k], self.n_eff, self.p, self.sigma2)

    def summary(self, n_rows: int | None = None):
        import pandas as pd
        r = len(self.tw_pvalues) if n_rows is None else min(n_rows, len(self.tw_pvalues))
        ell, cos2 = spike_estimates(self.eigenvalues[:r], self.n_eff, self.p, self.sigma2)
        df = pd.DataFrame({
            "axe": np.arange(1, r + 1),
            "valeur_propre": self.eigenvalues[:r],
            "pct_variance": 100 * self.eigenvalues[:r] / self.p,
            "au_dessus_bord_MP": self.eigenvalues[:r] > self.lambda_plus,
            "p_tracy_widom": self.tw_pvalues[:r],
            "retenu": np.arange(r) < self.k,
            "taille_reelle_estimee": ell,
            "cos2_attendu": cos2,
        })
        if self.perm_pvalues is not None:
            df.insert(5, "p_permutation", self.perm_pvalues[:r])
        return df

    def top_genes(self, axis: int = 1, n_top: int = 50):
        """Gènes les plus chargés sur un axe (1 = premier), avec leur poids signé."""
        import pandas as pd
        v = self.loadings[:, axis - 1]
        idx = np.argsort(-np.abs(v))[:n_top]
        names = self.gene_names[idx] if self.gene_names is not None else idx
        return pd.DataFrame({"gene": names, "poids": v[idx]})

    def cleaned_correlation(self) -> CleanedCorrelation:
        k = self.k
        lam = self.eigenvalues[:k]
        delta = (self.p - lam.sum()) / (self.p - k)
        return CleanedCorrelation(self.loadings[:, :k].copy(), lam.copy(), float(delta))

    def reconstruct(self):
        """Données standardisées débruitées (n × p) : rang k, seuls les axes retenus."""
        k = self.k
        return (self.scores[:, :k]) @ self.loadings[:, :k].T

    def report(self) -> str:
        lines = [
            f"n = {self.n} échantillons, p = {self.p} gènes, γ = p/(n−1) = {self.gamma:.2f}",
            f"variance du bruit σ² = {self.sigma2:.4f} ; bord de Marchenko-Pastur λ₊ = {self.lambda_plus:.3f}",
            f"au-dessus du bord : {self.k_mp} ; retenus ({self.method}, α = {self.alpha}) : {self.k}",
        ]
        tab = self.summary(max(self.k + 3, 5)).round(4).to_string(index=False)
        return "\n".join(lines) + "\n" + tab


def denoise(X, alpha: float = 0.05, sigma2="auto", method: str = "tw",
            n_perm: int = 0, n_keep: int = 20, rng=None) -> RMTResult:
    """Chaîne complète. X : matrice ou DataFrame (lignes = échantillons, colonnes = gènes).

    method = "tw"   : bord de MP + test de Tracy-Widom (par défaut, analytique).
    method = "perm" : test par permutations (n_perm ≥ 99 conseillé), sans hypothèse
                      de loi ; plus lent. Si n_perm > 0 avec "tw", les p-valeurs par
                      permutation sont calculées en plus, pour contrôle.
    """
    gene_names = sample_names = None
    if hasattr(X, "columns"):
        gene_names, sample_names = np.asarray(X.columns), np.asarray(X.index)
        X = X.to_numpy(dtype=float)
    Z, keep = standardize(X)
    if gene_names is not None:
        gene_names = gene_names[keep]
    n, p = Z.shape
    n_eff = n - 1
    eig, U, s, V = spectrum(Z)
    sel = select_components(eig, n_eff, p, alpha=alpha, sigma2=sigma2)

    perm_p = None
    k = sel["k"]
    if method == "perm" or n_perm > 0:
        if n_perm < 19:
            raise ValueError("n_perm ≥ 19 requis (≥ 99 conseillé)")
        null_max = permutation_null(Z, n_perm, rng)
        perm_p = permutation_pvalues(eig[: len(sel["tw_pvalues"])], null_max)
        if method == "perm":
            k = _leading_run(perm_p < alpha)
    elif method != "tw":
        raise ValueError("method doit être 'tw' ou 'perm'")

    r = min(len(eig), max(k, n_keep))
    lam_minus, _ = mp_edges(n_eff, p, sel["sigma2"])
    return RMTResult(
        n=n, p=p, n_eff=n_eff, alpha=alpha, method=method, eigenvalues=eig,
        sigma2=sel["sigma2"], lambda_minus=lam_minus, lambda_plus=sel["lambda_plus"],
        k_mp=sel["k_mp"], k=k, tw_pvalues=sel["tw_pvalues"], perm_pvalues=perm_p,
        loadings=V[:, :r], scores=U[:, :r] * s[:r], singular_values=s[:r],
        genes_kept=keep, gene_names=gene_names, sample_names=sample_names,
    )


def _cli():
    ap = argparse.ArgumentParser(description="Séparer signal et bruit (matrices aléatoires).")
    ap.add_argument("--input", required=True, help="CSV/TSV, 1re colonne = identifiants")
    ap.add_argument("--genes-in-rows", action="store_true",
                    help="les lignes sont des gènes (format GEO habituel)")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--method", choices=["tw", "perm"], default="tw")
    ap.add_argument("--n-perm", type=int, default=0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", help="CSV du résumé par axe")
    args = ap.parse_args()

    import pandas as pd
    sep = "\t" if args.input.endswith((".tsv", ".txt")) else ","
    df = pd.read_csv(args.input, sep=sep, index_col=0)
    if args.genes_in_rows:
        df = df.T
    res = denoise(df, alpha=args.alpha, method=args.method, n_perm=args.n_perm, rng=args.seed)
    print(res.report())
    if args.out:
        res.summary().to_csv(args.out, index=False)
        print(f"résumé écrit : {args.out}")


if __name__ == "__main__":
    _cli()
