"""Tests de scripts/rmt_denoise.py — données synthétiques uniquement.

Lancer : python -m pytest tests/ -q
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import rmt_denoise as rmt  # noqa: E402


# --- Tracy-Widom β = 1 : comparaison à la table publiée (Johnstone 2001, Table 1) ---
@pytest.mark.parametrize("q, s", [(0.10, -2.78), (0.50, -1.27), (0.90, 0.45),
                                  (0.95, 0.98), (0.99, 2.02)])
def test_tw1_matches_published_percentiles(q, s):
    assert abs(rmt.tw1_quantile(q) - s) < 0.006


def test_tw1_cdf_converged_and_tails():
    assert rmt.tw1_cdf(0.9793, m=60) == pytest.approx(rmt.tw1_cdf(0.9793, m=160), abs=1e-9)
    assert 0 < rmt.tw1_sf(10.0) < 1e-9          # queue droite calculée sans perte
    assert rmt.tw1_cdf(-11.0) == 0.0


# --- Marchenko-Pastur ---
@pytest.mark.parametrize("N, p", [(79, 5000), (500, 200)])
def test_mp_pdf_integrates_to_one(N, p):
    lo, hi = rmt.mp_edges(N, p)
    x = np.linspace(lo, hi, 200_001)
    assert np.trapezoid(rmt.mp_pdf(x, N, p), x) == pytest.approx(1.0, abs=1e-4)


def test_pure_noise_largest_eigenvalue_near_mp_edge():
    rng = np.random.default_rng(0)
    n, p = 200, 1000
    Z, _ = rmt.standardize(rng.standard_normal((n, p)))
    lam = rmt.top_eigenvalues(Z, 1)[0]
    _, hi = rmt.mp_edges(n - 1, p)
    assert abs(lam / hi - 1) < 0.05


def test_spectrum_matches_gram_shortcut():
    rng = np.random.default_rng(1)
    Z, _ = rmt.standardize(rng.standard_normal((30, 400)))
    eig, U, s, V = rmt.spectrum(Z)
    assert len(eig) == 29
    assert np.allclose(eig, rmt.top_eigenvalues(Z))
    assert eig.sum() == pytest.approx(400, rel=1e-9)   # trace de la corrélation = p


# --- Contrôle négatif : bruit pur ---
def test_false_positive_rate_on_pure_noise():
    rng = np.random.default_rng(2)
    n, p, R = 40, 2000, 60
    hits = 0
    for _ in range(R):
        Z, _ = rmt.standardize(rng.standard_normal((n, p)))
        hits += rmt.select_components(rmt.top_eigenvalues(Z, 10), n - 1, p, n_report=0)["k"] > 0
    assert hits / R <= 0.15


def test_permutation_keeps_each_gene_values():
    rng = np.random.default_rng(3)
    Z = rng.standard_normal((25, 50))
    Zp = rng.permuted(Z, axis=0)
    assert np.allclose(np.sort(Z, axis=0), np.sort(Zp, axis=0))
    assert not np.allclose(Z, Zp)


# --- Signal caché : détection, taille et fiabilité ---
def _spiked(n, p, m, rho, rng):
    X = rng.standard_normal((n, p))
    f = rng.standard_normal((n, 1))
    X[:, :m] = np.sqrt(rho) * f + np.sqrt(1 - rho) * X[:, :m]
    u = np.zeros(p)
    u[:m] = 1 / np.sqrt(m)
    return X, u, 1 + (m - 1) * rho


def test_strong_signature_found_with_predicted_reliability():
    rng = np.random.default_rng(4)
    n, p = 120, 3000
    obs, pred, ell_hat = [], [], []
    for _ in range(20):
        X, u, ell = _spiked(n, p, 150, 0.2, rng)
        res = rmt.denoise(X, n_keep=3)
        assert res.k == 1
        e, c = res.spikes()
        obs.append((res.loadings[:, 0] @ u) ** 2)
        pred.append(c[0])
        ell_hat.append(e[0])
    assert np.mean(ell_hat) == pytest.approx(ell, rel=0.10)
    assert abs(np.mean(obs) - np.mean(pred)) < 0.05


def test_spike_inversion_roundtrip():
    gamma = 40.0
    ell = np.array([8.0, 15.0, 60.0])            # tous au-dessus de 1 + √40 ≈ 7,3
    lam = rmt.spike_forward(ell, gamma)
    back, cos2 = rmt.spike_estimates(lam, n_eff=100, p=4000)
    assert np.allclose(back, ell)
    assert np.all(np.diff(cos2) > 0) and np.all((cos2 > 0) & (cos2 < 1))


def test_cleaned_correlation_keeps_trace_and_is_positive():
    rng = np.random.default_rng(5)
    X, _, _ = _spiked(60, 300, 60, 0.3, rng)
    res = rmt.denoise(X)
    C = res.cleaned_correlation().to_dense()
    assert np.trace(C) == pytest.approx(res.p, rel=1e-9)
    assert np.linalg.eigvalsh(C).min() > 0
    x = rng.standard_normal(res.p)
    assert np.allclose(res.cleaned_correlation().matvec(x), C @ x)


def test_dataframe_input_keeps_gene_names_and_drops_constant_genes():
    pd = pytest.importorskip("pandas")
    rng = np.random.default_rng(6)
    X, _, _ = _spiked(50, 200, 40, 0.4, rng)
    df = pd.DataFrame(X, columns=[f"G{i}" for i in range(200)])
    df["CONST"] = 1.0
    res = rmt.denoise(df)
    assert res.p == 200 and not res.genes_kept[-1]
    top = res.top_genes(1, 20)
    assert top.gene.str.startswith("G").all()
    assert {"axe", "valeur_propre", "retenu", "cos2_attendu"} <= set(res.summary().columns)
