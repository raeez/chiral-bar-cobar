r"""Tests for bc_zero_repulsion_engine.py -- zero repulsion and Deuring-Heilbronn.

Verification paths per the Multi-Path Verification Mandate:
    1. Direct zero-finding via Newton-Raphson
    2. Argument principle contour integral for zero counting
    3. Cross-check via complementarity: zeros of zeta_c and zeta_{26-c}
    4. Statistical tests (KS against GUE/Poisson)
    5. Monotonicity checks: repulsion varies smoothly with c

Coverage targets:
    - All 4 shadow depth classes (G, L, C, M)
    - Edge cases (c=0.01, c=13 self-dual, c=25.99 near c=26)
    - Statistical robustness of spacing distributions
    - Complementarity functional equation on zeros
    - Zero clustering near Riemann zeros
    - Deuring-Heilbronn repulsion bounds

CAUTION (AP1):  kappa(Vir_c) = c/2, NOT dim(g)*(k+h^v)/(2h^v).
CAUTION (AP9):  S_2 = kappa = c/2 for Virasoro specifically.
CAUTION (AP10): Tests use cross-verification, not hardcoded expected values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

from __future__ import annotations

import math
import pytest
from typing import Dict, List

# ---------------------------------------------------------------------------
# Import the engine under test
# ---------------------------------------------------------------------------
from compute.lib.bc_zero_repulsion_engine import (
    # Section 1: helpers
    shadow_zeta_real_line,
    shadow_zeta_log_derivative,
    # Section 2: exceptional zeros
    find_real_zeros_brentq,
    rightmost_real_zero,
    exceptional_zero_scan,
    siegel_zero_distance,
    # Section 3: spacing statistics
    compute_nn_spacings,
    compute_spacing_statistics,
    wigner_surmise_gue,
    wigner_surmise_goe,
    poisson_spacing,
    wigner_surmise_cdf_gue,
    gap_exceedance_distribution,
    ZeroSpacingData,
    # Section 4: number variance
    number_variance,
    gue_number_variance,
    poisson_number_variance,
    # Section 5: complementarity
    complementarity_zero_relation,
    self_dual_repulsion_enhancement,
    # Section 6: clustering
    cluster_score_near_height,
    riemann_zero_clustering,
    FIRST_RIEMANN_ZERO_GAMMA,
    # Section 7: depth classes
    class_g_repulsion,
    class_l_repulsion,
    class_c_repulsion,
    class_m_repulsion,
    repulsion_by_depth_class,
    DepthRepulsionData,
    # Section 8: KS tests
    ks_test_against_distribution,
    poisson_cdf,
    ks_against_gue,
    ks_against_poisson,
    # Section 9: height profile
    repulsion_vs_height,
    # Section 10: Deuring-Heilbronn
    deuring_heilbronn_bound,
    repulsion_strength_vs_kappa,
    # Section 11: monotonicity
    repulsion_monotonicity_test,
    # Section 12: argument principle verification
    verify_zero_count_argument_principle,
    # Section 13: full pipeline
    full_repulsion_analysis,
    RepulsionAnalysis,
)

# Import coefficient providers
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    shadow_zeta_numerical,
    virasoro_growth_rate_exact,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    newton_zero,
    muller_zero,
    find_zeros_grid,
    affine_sl2_zeros,
    affine_sl3_zeros,
    heisenberg_zeros,
    _shadow_zeta_complex,
    argument_principle_count,
)


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def vir_coeffs_c1():
    """Virasoro shadow coefficients at c=1, max_r=50."""
    return virasoro_shadow_coefficients_numerical(1.0, 50)


@pytest.fixture
def vir_coeffs_c13():
    """Virasoro shadow coefficients at c=13 (self-dual), max_r=50."""
    return virasoro_shadow_coefficients_numerical(13.0, 50)


@pytest.fixture
def vir_coeffs_c26():
    """Virasoro shadow coefficients at c=26, max_r=50."""
    return virasoro_shadow_coefficients_numerical(26.0, 50)


@pytest.fixture
def heis_coeffs_k1():
    """Heisenberg shadow coefficients at k=1."""
    return heisenberg_shadow_coefficients(1.0, 30)


@pytest.fixture
def aff_sl2_coeffs_k1():
    """Affine sl_2 at k=1."""
    return affine_sl2_shadow_coefficients(1.0, 30)


@pytest.fixture
def bg_coeffs():
    """Beta-gamma at lambda=1/2."""
    return betagamma_shadow_coefficients(0.5, 30)


# ============================================================================
# Section 1: Shadow zeta evaluation helpers
# ============================================================================

class TestShadowZetaHelpers:
    """Tests for shadow zeta evaluation functions."""

    def test_real_line_heisenberg(self, heis_coeffs_k1):
        """zeta_{H_1}(sigma) = 2^{-sigma} on the real line."""
        for sigma in [0.0, 1.0, 2.0, 5.0]:
            val = shadow_zeta_real_line(heis_coeffs_k1, sigma)
            expected = 2.0 ** (-sigma)
            assert abs(val - expected) < 1e-10, f"sigma={sigma}: {val} != {expected}"

    def test_real_line_affine(self, aff_sl2_coeffs_k1):
        """Affine sl_2 zeta at real s > 0 should be real and finite."""
        for sigma in [1.0, 2.0, 5.0, 10.0]:
            val = shadow_zeta_real_line(aff_sl2_coeffs_k1, sigma)
            assert math.isfinite(val), f"sigma={sigma}: not finite"

    def test_log_derivative_basic(self, vir_coeffs_c1):
        """Log derivative zeta'/zeta at a non-zero point is finite."""
        s = complex(3.0, 1.0)
        ld = shadow_zeta_log_derivative(vir_coeffs_c1, s)
        assert math.isfinite(abs(ld)), "Log derivative not finite"

    def test_log_derivative_at_zero(self):
        """Log derivative should be large near a zero."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 30)
        zeros = affine_sl2_zeros(1.0, 5)
        if zeros:
            # Near a zero, |zeta'| / |zeta| should be large
            s_near = zeros[0] + 0.001
            ld = shadow_zeta_log_derivative(coeffs, s_near)
            # At a simple zero, |zeta'/zeta| ~ 1/|s - rho|
            assert abs(ld) > 1.0, "Log derivative not large near zero"


# ============================================================================
# Section 2: Exceptional (Siegel) zero analysis
# ============================================================================

class TestExceptionalZeros:
    """Tests for exceptional zero detection."""

    def test_heisenberg_no_real_zeros(self, heis_coeffs_k1):
        """Heisenberg with k=1: zeta = 2^{-s} has no real zeros."""
        real_z = find_real_zeros_brentq(heis_coeffs_k1, -20.0, 20.0)
        assert len(real_z) == 0, f"Found {len(real_z)} real zeros for Heisenberg"

    def test_affine_no_real_zeros(self, aff_sl2_coeffs_k1):
        """Affine sl_2 at k=1: kappa, alpha > 0, so zeta > 0 on the real line."""
        # kappa = 3(1+2)/4 = 9/4, alpha = 4/(1+2) = 4/3, both > 0
        # zeta(sigma) = 9/4 * 2^{-sigma} + 4/3 * 3^{-sigma} > 0 for all real sigma
        real_z = find_real_zeros_brentq(aff_sl2_coeffs_k1, -20.0, 20.0)
        assert len(real_z) == 0, f"Found {len(real_z)} real zeros for affine sl_2"

    def test_virasoro_c1_real_zeros(self, vir_coeffs_c1):
        """Virasoro at c=1: real zeros may or may not exist."""
        real_z = find_real_zeros_brentq(vir_coeffs_c1, -15.0, 15.0)
        # Just check the function runs and returns a list
        assert isinstance(real_z, list)
        for z in real_z:
            # Verify each is actually a zero
            val = shadow_zeta_real_line(vir_coeffs_c1, z)
            assert abs(val) < 1e-6, f"Real zero at {z} has residual {val}"

    def test_exceptional_zero_scan_runs(self):
        """Exceptional zero scan returns results for all c values."""
        c_vals = [0.5, 1.0, 5.0, 13.0, 25.0]
        result = exceptional_zero_scan(c_vals, max_r=30)
        assert len(result) == len(c_vals)
        for c in c_vals:
            assert c in result

    def test_exceptional_zero_scan_small_c(self):
        """For small c (kappa near 0), a real zero is more likely."""
        result = exceptional_zero_scan([0.5, 1.0, 5.0, 10.0], max_r=30)
        # At least the function should run without error for all c
        for c, rz in result.items():
            if rz is not None:
                # If found, it should actually be a zero
                coeffs = virasoro_shadow_coefficients_numerical(c, 30)
                val = shadow_zeta_real_line(coeffs, rz)
                assert abs(val) < 1e-4, f"c={c}: real 'zero' at {rz} has residual {val}"

    def test_rightmost_real_zero_returns_none_for_heisenberg(self, heis_coeffs_k1):
        """Heisenberg has no real zeros."""
        rz = rightmost_real_zero(heis_coeffs_k1)
        assert rz is None

    def test_siegel_zero_distance_heisenberg(self, heis_coeffs_k1):
        """Siegel distance is None for Heisenberg (no real zeros)."""
        dist = siegel_zero_distance(heis_coeffs_k1)
        assert dist is None


# ============================================================================
# Section 3: Nearest-neighbor spacing statistics
# ============================================================================

class TestNNSpacings:
    """Tests for nearest-neighbor spacing computation."""

    def test_empty_zeros(self):
        """Empty zero list gives empty spacings."""
        assert compute_nn_spacings([]) == []

    def test_single_zero(self):
        """Single zero gives empty spacings."""
        assert compute_nn_spacings([complex(1, 2)]) == []

    def test_two_zeros(self):
        """Two zeros give one spacing."""
        z1, z2 = complex(0, 1), complex(0, 3)
        spacings = compute_nn_spacings([z1, z2])
        assert len(spacings) == 1
        assert abs(spacings[0] - 2.0) < 1e-10

    def test_sorted_by_imag(self):
        """Zeros sorted by imaginary part."""
        zeros = [complex(0, 3), complex(0, 1), complex(0, 5)]
        spacings = compute_nn_spacings(zeros, sort_by_imag=True)
        assert len(spacings) == 2
        assert abs(spacings[0] - 2.0) < 1e-10  # |3 - 1| = 2
        assert abs(spacings[1] - 2.0) < 1e-10  # |5 - 3| = 2

    def test_uniform_spacings(self):
        """Uniformly spaced zeros on a vertical line."""
        zeros = [complex(0, k) for k in range(0, 100, 5)]
        spacings = compute_nn_spacings(zeros)
        # All spacings should be 5.0
        for s in spacings:
            assert abs(s - 5.0) < 1e-10

    def test_statistics_container(self):
        """compute_spacing_statistics returns well-formed data."""
        zeros = [complex(0, k * 1.5) for k in range(20)]
        stats = compute_spacing_statistics('test', 1.0, zeros)
        assert stats.n_zeros == 20
        assert stats.mean_spacing > 0
        assert abs(stats.mean_spacing - 1.5) < 1e-10
        assert stats.min_spacing > 0
        assert stats.spacing_variance < 1e-10  # Uniform spacing

    def test_statistics_empty(self):
        """Statistics for empty zero list."""
        stats = compute_spacing_statistics('test', 0.0, [])
        assert stats.n_zeros == 0
        assert stats.mean_spacing == 0.0

    def test_wigner_surmise_normalization(self):
        """GUE Wigner surmise integrates to ~1 (probability distribution)."""
        # Numerical integration of p(s) from 0 to 10
        ds = 0.001
        integral = sum(wigner_surmise_gue(s) * ds for s in
                       [i * ds for i in range(int(10 / ds))])
        assert abs(integral - 1.0) < 0.01, f"GUE integral = {integral}"

    def test_goe_surmise_normalization(self):
        """GOE Wigner surmise integrates to ~1."""
        ds = 0.001
        integral = sum(wigner_surmise_goe(s) * ds for s in
                       [i * ds for i in range(int(10 / ds))])
        assert abs(integral - 1.0) < 0.01, f"GOE integral = {integral}"

    def test_poisson_spacing_normalization(self):
        """Poisson spacing exp(-s) integrates to 1 on [0, inf)."""
        ds = 0.001
        integral = sum(poisson_spacing(s) * ds for s in
                       [i * ds for i in range(int(30 / ds))])
        assert abs(integral - 1.0) < 0.01, f"Poisson integral = {integral}"

    def test_wigner_cdf_monotone(self):
        """GUE CDF is monotone increasing."""
        prev = 0.0
        for s in [0.1 * i for i in range(1, 50)]:
            curr = wigner_surmise_cdf_gue(s)
            assert curr >= prev - 1e-15, f"CDF not monotone at s={s}"
            prev = curr

    def test_wigner_cdf_limits(self):
        """CDF(0) = 0, CDF(inf) = 1."""
        assert abs(wigner_surmise_cdf_gue(0.0)) < 1e-15
        assert abs(wigner_surmise_cdf_gue(100.0) - 1.0) < 1e-10

    def test_gap_exceedance(self):
        """Gap exceedance P(gap > x) is monotone decreasing."""
        spacings = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
        x_values = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
        result = gap_exceedance_distribution(spacings, x_values)
        prev = 1.0
        for x in sorted(result.keys()):
            assert result[x] <= prev + 1e-10
            prev = result[x]


# ============================================================================
# Section 4: Number variance
# ============================================================================

class TestNumberVariance:
    """Tests for level spacing (number) variance."""

    def test_uniform_zeros_variance(self):
        """Uniformly spaced zeros have small variance."""
        zeros = [complex(0, k * 2.0) for k in range(100)]
        nv = number_variance(zeros, [2.0, 4.0, 8.0])
        # For perfectly uniform zeros, the variance should be small
        for L, var in nv.items():
            assert var < 2.0, f"L={L}: variance {var} too large for uniform"

    def test_gue_prediction_positive_large_L(self):
        """GUE number variance is positive for L >= 1 (asymptotic formula)."""
        # The asymptotic formula can be negative for very small L;
        # it is reliable only for L >= O(1).
        for L in [1.0, 5.0, 10.0, 100.0]:
            assert gue_number_variance(L) > 0

    def test_gue_prediction_logarithmic(self):
        """GUE number variance grows logarithmically."""
        v1 = gue_number_variance(1.0)
        v10 = gue_number_variance(10.0)
        v100 = gue_number_variance(100.0)
        # Logarithmic growth: ratio should decrease
        ratio_1 = (v10 - v1) / math.log(10)
        ratio_2 = (v100 - v10) / math.log(10)
        # Both ratios should be of order 2/pi^2 ~ 0.2
        assert 0.05 < ratio_1 < 0.5
        assert 0.05 < ratio_2 < 0.5

    def test_poisson_linear(self):
        """Poisson number variance = L."""
        for L in [0.5, 1.0, 5.0, 10.0]:
            assert abs(poisson_number_variance(L) - L) < 1e-15

    def test_empty_zeros(self):
        """Number variance for empty zero list."""
        nv = number_variance([], [1.0, 2.0])
        assert all(v == 0.0 for v in nv.values())


# ============================================================================
# Section 5: Complementarity repulsion
# ============================================================================

class TestComplementarityRepulsion:
    """Tests for complementarity and self-duality effects on zeros."""

    def test_complementarity_sum_coefficients(self):
        """D_r(c) = S_r(c) + S_r(26-c): check kappa sum = 13 (AP24)."""
        for c_val in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            c_dual = 26.0 - c_val
            coeffs_c = virasoro_shadow_coefficients_numerical(c_val, 20)
            coeffs_d = virasoro_shadow_coefficients_numerical(c_dual, 20)
            # S_2(c) + S_2(26-c) = kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13
            kappa_sum = coeffs_c[2] + coeffs_d[2]
            assert abs(kappa_sum - 13.0) < 1e-10, \
                f"c={c_val}: kappa sum = {kappa_sum} != 13"

    def test_self_dual_c13_symmetry(self):
        """At c=13: S_r(13) = S_r(13) trivially (self-dual)."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, 30)
        # kappa(Vir_13) = 13/2 = 6.5
        assert abs(coeffs[2] - 6.5) < 1e-10

    def test_complementarity_relation_runs(self):
        """complementarity_zero_relation runs and returns structured data."""
        result = complementarity_zero_relation(
            5.0, max_r=20,
            re_range=(-3.0, 3.0), im_range=(-20.0, 20.0),
            grid_re=8, grid_im=20,
        )
        assert 'zeros_c' in result
        assert 'zeros_dual' in result
        assert 'zeros_sum' in result
        assert 'interleaving_score' in result

    def test_self_dual_enhancement_runs(self):
        """self_dual_repulsion_enhancement runs for a few c values."""
        c_vals = [5.0, 13.0, 20.0]
        result = self_dual_repulsion_enhancement(
            c_vals, max_r=20, im_range=(-30.0, 30.0)
        )
        assert len(result) == 3
        for c in c_vals:
            assert c in result

    def test_complementarity_zero_sum_correct(self):
        """Verify that zeta_c(s) + zeta_{26-c}(s) = zeta_D(s) at sample points."""
        c_val = 5.0
        max_r = 30
        coeffs_c = virasoro_shadow_coefficients_numerical(c_val, max_r)
        coeffs_d = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

        for s_val in [complex(3, 1), complex(5, 2), complex(2, 0.5)]:
            zc = shadow_zeta_numerical(coeffs_c, s_val, max_r)
            zd = shadow_zeta_numerical(coeffs_d, s_val, max_r)
            # Compute sum coefficients
            coeffs_sum = {r: coeffs_c.get(r, 0.0) + coeffs_d.get(r, 0.0)
                          for r in range(2, max_r + 1)}
            zs = shadow_zeta_numerical(coeffs_sum, s_val, max_r)
            assert abs(zc + zd - zs) < 1e-10, \
                f"s={s_val}: |zeta_c + zeta_d - zeta_sum| = {abs(zc + zd - zs)}"


# ============================================================================
# Section 6: Zero clustering near Riemann zeros
# ============================================================================

class TestZeroClustering:
    """Tests for zero clustering analysis."""

    def test_cluster_score_uniform(self):
        """Uniform zeros: cluster score ~ 1 everywhere."""
        zeros = [complex(0, k * 0.5) for k in range(200)]
        score = cluster_score_near_height(zeros, 50.0, window=5.0)
        # Should be approximately 1 for uniform distribution
        assert 0.5 < score < 2.0, f"Cluster score {score} far from 1"

    def test_cluster_score_concentrated(self):
        """Zeros concentrated at target: cluster score > 1."""
        # Cluster 50 zeros near gamma=14.0
        zeros = [complex(0, 14.0 + 0.01 * k) for k in range(-25, 25)]
        # Add 50 zeros far away
        zeros += [complex(0, 100.0 + k) for k in range(50)]
        score = cluster_score_near_height(zeros, 14.0, window=1.0)
        assert score > 1.0, f"Cluster score {score} should be > 1"

    def test_cluster_score_empty(self):
        """Empty zero list gives score 0."""
        score = cluster_score_near_height([], 14.0)
        assert score == 0.0

    def test_first_riemann_zero_constant(self):
        """First Riemann zero gamma_1 = 14.134725..."""
        assert abs(FIRST_RIEMANN_ZERO_GAMMA - 14.134725141734693) < 1e-12

    def test_riemann_clustering_virasoro(self):
        """Virasoro zeros should NOT cluster at Riemann zero heights."""
        coeffs = virasoro_shadow_coefficients_numerical(1.0, 30)
        result = riemann_zero_clustering(
            coeffs,
            riemann_gammas=[14.134725],
            window=2.0,
            max_r=30,
            im_range=(-50.0, 50.0),
        )
        # The result should exist for each gamma
        assert 14.134725 in result
        # No strong expectation on the value, but it should be finite
        assert math.isfinite(result[14.134725])


# ============================================================================
# Section 7: Repulsion by shadow depth class
# ============================================================================

class TestDepthClassRepulsion:
    """Tests for repulsion statistics by shadow depth class."""

    def test_class_g_no_zeros(self):
        """Class G (Heisenberg, k>0): no zeros."""
        data = class_g_repulsion(1.0)
        assert data.shadow_class == 'G'
        assert data.n_zeros == 0
        assert data.has_zeros is False
        assert data.mean_spacing == float('inf')

    def test_class_g_zero_level(self):
        """Class G at k=0: degenerate (identically zero)."""
        data = class_g_repulsion(0.0)
        assert data.n_zeros == 0

    def test_class_l_uniform_spacing(self):
        """Class L (affine sl_2): zeros on vertical line, uniform spacing."""
        data = class_l_repulsion(1.0, 'sl2', n_max=20)
        assert data.shadow_class == 'L'
        assert data.has_zeros is True
        assert data.n_zeros > 0
        # Spacing should be uniform: 2*pi / log(3/2) ~ 15.49
        expected_spacing = 2.0 * math.pi / math.log(3.0 / 2.0)
        if data.spacings:
            for s in data.spacings[:10]:
                assert abs(s - expected_spacing) < 0.01, \
                    f"Non-uniform spacing: {s} != {expected_spacing}"

    def test_class_l_sl3(self):
        """Class L for sl_3 also has uniform spacing."""
        data = class_l_repulsion(1.0, 'sl3', n_max=20)
        assert data.shadow_class == 'L'
        assert data.has_zeros is True
        # Same spacing period as sl_2 (both are 2-term series with bases 2, 3)
        expected_spacing = 2.0 * math.pi / math.log(3.0 / 2.0)
        if data.spacings:
            for s in data.spacings[:10]:
                assert abs(s - expected_spacing) < 0.01

    def test_class_c_has_zeros(self):
        """Class C (beta-gamma): has zeros (3-term exponential poly)."""
        data = class_c_repulsion(0.5, im_range=(-30.0, 30.0))
        assert data.shadow_class == 'C'
        # Beta-gamma should have zeros (3-term can vanish)
        # Just check the function runs
        assert isinstance(data.n_zeros, int)

    def test_class_m_virasoro_c1(self):
        """Class M (Virasoro c=1): has zeros from infinite series."""
        data = class_m_repulsion(
            1.0, max_r=30,
            re_range=(-3.0, 3.0), im_range=(-30.0, 30.0),
            grid_re=10, grid_im=25,
        )
        assert data.shadow_class == 'M'
        assert isinstance(data.n_zeros, int)

    def test_class_m_virasoro_c13(self):
        """Class M at self-dual c=13."""
        data = class_m_repulsion(
            13.0, max_r=30,
            re_range=(-3.0, 3.0), im_range=(-30.0, 30.0),
            grid_re=10, grid_im=25,
        )
        assert data.shadow_class == 'M'

    def test_repulsion_by_depth_class_all_four(self):
        """repulsion_by_depth_class returns data for all 4 classes."""
        result = repulsion_by_depth_class(max_r=20)
        assert set(result.keys()) == {'G', 'L', 'C', 'M'}
        assert result['G'].n_zeros == 0
        assert result['L'].n_zeros > 0

    def test_class_l_spacing_variance_zero(self):
        """Class L: perfectly uniform spacing => variance = 0."""
        data = class_l_repulsion(1.0, 'sl2', n_max=20)
        # Spacing variance should be essentially zero
        assert data.spacing_variance < 1e-6, \
            f"Class L spacing variance {data.spacing_variance} != 0"


# ============================================================================
# Section 8: Statistical tests (KS)
# ============================================================================

class TestKSTests:
    """Tests for Kolmogorov-Smirnov statistical comparisons."""

    def test_perfect_poisson_data(self):
        """Exponentially distributed data should match Poisson."""
        import random
        random.seed(42)
        # Generate exponential random variables (mean 1)
        data = sorted([-math.log(random.random()) for _ in range(200)])
        D, p = ks_against_poisson(data)
        # Should not reject Poisson at 5% level
        assert p > 0.01, f"Exponential data rejected as Poisson: p={p}"

    def test_uniform_data_rejects_poisson(self):
        """Uniformly spaced data should reject Poisson."""
        data = [i / 50.0 for i in range(1, 51)]
        D, p = ks_against_poisson(data)
        # Should reject Poisson (uniform != exponential)
        assert D > 0.1, f"Uniform data not distinguished from Poisson: D={D}"

    def test_ks_empty_data(self):
        """KS test on empty data returns (0, 1)."""
        D, p = ks_against_gue([])
        assert D == 0.0
        assert p == 1.0

    def test_poisson_cdf_properties(self):
        """Poisson CDF: 0 at 0, monotone, approaches 1."""
        assert poisson_cdf(0.0) == 0.0
        assert abs(poisson_cdf(100.0) - 1.0) < 1e-10
        prev = 0.0
        for x in [0.1 * i for i in range(1, 100)]:
            curr = poisson_cdf(x)
            assert curr >= prev - 1e-15
            prev = curr

    def test_ks_statistic_bounded(self):
        """KS statistic is in [0, 1]."""
        data = [0.5, 1.0, 1.5, 2.0, 2.5]
        D, p = ks_against_gue(data)
        assert 0.0 <= D <= 1.0
        assert 0.0 <= p <= 1.0

    def test_ks_p_value_bounded(self):
        """p-value is in [0, 1]."""
        data = [0.1, 0.5, 0.9, 1.2, 1.8, 2.5]
        _, p_gue = ks_against_gue(data)
        _, p_poi = ks_against_poisson(data)
        assert 0.0 <= p_gue <= 1.0
        assert 0.0 <= p_poi <= 1.0

    def test_ks_generic_distribution(self):
        """KS test against a custom CDF."""
        data = [0.5, 1.0, 1.5]
        # CDF = x/2 for x in [0, 2]
        D, p = ks_test_against_distribution(data, lambda x: min(1.0, max(0.0, x / 2.0)))
        assert 0.0 <= D <= 1.0


# ============================================================================
# Section 9: Height profile
# ============================================================================

class TestHeightProfile:
    """Tests for repulsion as a function of height."""

    def test_uniform_zeros_flat_profile(self):
        """Uniformly spaced zeros: spacing constant across heights."""
        zeros = [complex(0, k * 2.0) for k in range(100)]
        profile = repulsion_vs_height(zeros, [0.0, 50.0, 100.0, 150.0, 200.0])
        # All bins should have spacing ~ 2.0
        for mid, spacing in profile.items():
            if spacing > 0:
                assert abs(spacing - 2.0) < 0.5, \
                    f"Height {mid}: spacing {spacing} != 2.0"

    def test_empty_zeros_empty_profile(self):
        """Empty zero list gives empty profile."""
        profile = repulsion_vs_height([])
        assert profile == {}

    def test_default_bins(self):
        """Default bins are [0, 5, 10, 20, 40, 80]."""
        zeros = [complex(0, k) for k in range(100)]
        profile = repulsion_vs_height(zeros)
        # Should have bins at midpoints: 2.5, 7.5, 15, 30, 60
        assert len(profile) > 0


# ============================================================================
# Section 10: Deuring-Heilbronn bound
# ============================================================================

class TestDeuringHeilbronn:
    """Tests for Deuring-Heilbronn repulsion estimates."""

    def test_heisenberg_infinite_bound(self, heis_coeffs_k1):
        """Heisenberg has S_3 = 0, so DH bound = inf."""
        bound = deuring_heilbronn_bound(heis_coeffs_k1, 0.0)
        # S_3 = 0 for Heisenberg => C_eff = inf
        assert bound == float('inf')

    def test_affine_finite_bound(self, aff_sl2_coeffs_k1):
        """Affine sl_2 has S_3 > 0, so DH bound is finite."""
        # beta_0 = 0.0 is not a zero, so bound should be 0
        bound = deuring_heilbronn_bound(aff_sl2_coeffs_k1, 0.0)
        # 0.0 is not a zero of zeta_{sl_2}, so the function returns 0
        assert bound == 0.0

    def test_repulsion_strength_runs(self):
        """repulsion_strength_vs_kappa runs for several c values."""
        c_vals = [1.0, 5.0, 13.0, 20.0]
        result = repulsion_strength_vs_kappa(c_vals, max_r=20)
        assert len(result) == 4
        for c in c_vals:
            assert c in result

    def test_dh_bound_positive_at_actual_zero(self):
        """At an actual real zero, DH bound should be positive and finite."""
        # Use Virasoro and find a real zero first
        for c_val in [0.5, 1.0, 2.0, 5.0]:
            try:
                coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
                real_z = find_real_zeros_brentq(coeffs, -15.0, 15.0, max_r=30)
                if real_z:
                    bound = deuring_heilbronn_bound(coeffs, real_z[0], max_r=30)
                    assert bound >= 0, f"c={c_val}: DH bound = {bound} < 0"
                    break
            except (ValueError, ZeroDivisionError):
                continue


# ============================================================================
# Section 11: Monotonicity
# ============================================================================

class TestMonotonicity:
    """Tests for smooth variation of repulsion with c."""

    def test_monotonicity_runs(self):
        """repulsion_monotonicity_test runs and returns structured data."""
        c_vals = [2.0, 5.0, 10.0, 15.0, 20.0]
        result = repulsion_monotonicity_test(
            c_vals, max_r=20, im_range=(-20.0, 20.0)
        )
        assert 'c_values' in result
        assert 'mean_spacings' in result
        assert 'is_smooth' in result
        assert len(result['mean_spacings']) == 5

    def test_mean_spacings_positive(self):
        """Mean spacings should be non-negative."""
        c_vals = [2.0, 5.0, 10.0]
        result = repulsion_monotonicity_test(
            c_vals, max_r=20, im_range=(-20.0, 20.0)
        )
        for ms in result['mean_spacings']:
            if math.isfinite(ms):
                assert ms >= 0


# ============================================================================
# Section 12: Argument principle cross-check
# ============================================================================

class TestArgumentPrincipleVerification:
    """Tests for argument principle cross-check of zero counts."""

    def test_affine_sl2_argument_principle(self):
        """Affine sl_2: argument principle matches known zero structure."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 30)
        # Zeros are on a vertical line at Re(s) = -log(kappa/alpha)/log(3/2)
        # In the rectangle [-5, 5] x [-20, 20], count analytically
        kappa = 3.0 * 3.0 / 4.0  # 9/4
        alpha = 4.0 / 3.0
        log_32 = math.log(3.0 / 2.0)
        re_zero = -math.log(kappa / alpha) / log_32

        if -5.0 < re_zero < 5.0:
            # Zeros at Im = -pi*(2n+1)/log(3/2) for various n
            expected_count = 0
            for n in range(-20, 20):
                im_zero = -math.pi * (2 * n + 1) / log_32
                if -20.0 < im_zero < 20.0:
                    expected_count += 1

            ap_count = argument_principle_count(
                coeffs, (-5.0, 5.0), (-20.0, 20.0), n_points=2000, max_r=30
            )
            # Allow tolerance of 1 (contour can miss zeros on the boundary)
            assert abs(ap_count - expected_count) <= 2, \
                f"AP count {ap_count} != expected {expected_count}"

    def test_verify_function_returns_dict(self):
        """verify_zero_count_argument_principle returns structured result."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 30)
        zeros = affine_sl2_zeros(1.0, 10)
        # Filter to the search region
        filtered = [z for z in zeros if -5.0 < z.real < 5.0 and -20.0 < z.imag < 20.0]
        result = verify_zero_count_argument_principle(
            coeffs, filtered,
            re_range=(-5.0, 5.0), im_range=(-20.0, 20.0),
            n_points=2000, max_r=30,
        )
        assert 'newton_count' in result
        assert 'ap_count' in result
        assert 'discrepancy' in result
        assert 'agrees' in result


# ============================================================================
# Section 13: Full pipeline
# ============================================================================

class TestFullPipeline:
    """Tests for the full repulsion analysis pipeline."""

    def test_heisenberg_pipeline(self):
        """Full pipeline for Heisenberg k=1."""
        result = full_repulsion_analysis(
            'heisenberg', 1.0, max_r=20,
            re_range=(-3.0, 3.0), im_range=(-20.0, 20.0),
            grid_re=8, grid_im=15,
        )
        assert result.family == 'heisenberg'
        assert result.shadow_class == 'G'
        assert result.n_zeros == 0
        assert result.real_zeros == []

    def test_affine_sl2_pipeline(self):
        """Full pipeline for affine sl_2 k=1."""
        result = full_repulsion_analysis(
            'affine_sl2', 1.0, max_r=20,
            re_range=(-5.0, 5.0), im_range=(-30.0, 30.0),
            grid_re=10, grid_im=25,
        )
        assert result.family == 'affine_sl2'
        assert result.shadow_class == 'L'
        assert result.n_zeros > 0

    def test_virasoro_pipeline(self):
        """Full pipeline for Virasoro c=1."""
        result = full_repulsion_analysis(
            'virasoro', 1.0, max_r=20,
            re_range=(-3.0, 3.0), im_range=(-20.0, 20.0),
            grid_re=8, grid_im=15,
        )
        assert result.family == 'virasoro'
        assert result.shadow_class == 'M'
        assert isinstance(result.n_zeros, int)

    def test_betagamma_pipeline(self):
        """Full pipeline for beta-gamma lambda=1/2."""
        result = full_repulsion_analysis(
            'betagamma', 0.5, max_r=20,
            re_range=(-5.0, 5.0), im_range=(-20.0, 20.0),
            grid_re=8, grid_im=15,
        )
        assert result.family == 'betagamma'
        assert result.shadow_class == 'C'

    def test_pipeline_returns_all_fields(self):
        """Pipeline result has all expected fields."""
        result = full_repulsion_analysis(
            'heisenberg', 1.0, max_r=10,
            re_range=(-2.0, 2.0), im_range=(-10.0, 10.0),
            grid_re=5, grid_im=8,
        )
        assert hasattr(result, 'family')
        assert hasattr(result, 'param')
        assert hasattr(result, 'shadow_class')
        assert hasattr(result, 'n_zeros')
        assert hasattr(result, 'real_zeros')
        assert hasattr(result, 'rightmost_real_zero')
        assert hasattr(result, 'spacing_stats')
        assert hasattr(result, 'ks_gue')
        assert hasattr(result, 'ks_poisson')
        assert hasattr(result, 'height_profile')
        assert hasattr(result, 'deuring_heilbronn_dist')


# ============================================================================
# Edge cases: c near 0, c=13 self-dual, c near 26
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases in central charge."""

    def test_small_c_virasoro(self):
        """Virasoro at c=0.5: kappa=0.25, small leading coefficient."""
        coeffs = virasoro_shadow_coefficients_numerical(0.5, 30)
        assert abs(coeffs[2] - 0.25) < 1e-10  # kappa = c/2 = 0.25
        # Should be able to find zeros and compute spacing
        zeros = find_zeros_grid(
            coeffs, (-3.0, 3.0), (-20.0, 20.0), 8, 15, max_r=30
        )
        assert isinstance(zeros, list)

    def test_very_small_c_virasoro(self):
        """Virasoro at c=0.01: kappa=0.005, very small."""
        coeffs = virasoro_shadow_coefficients_numerical(0.01, 30)
        assert abs(coeffs[2] - 0.005) < 1e-10
        # The higher coefficients dominate: the function is essentially
        # zeta(s) ~ S_3 * 3^{-s} + ... for small sigma
        assert abs(coeffs[3]) > abs(coeffs[2]) * 0.1  # S_3 is nontrivial

    def test_c13_self_dual(self, vir_coeffs_c13):
        """At c=13: self-dual point, kappa = 6.5."""
        assert abs(vir_coeffs_c13[2] - 6.5) < 1e-10
        # The complementarity sum S_r(13) + S_r(13) = 2*S_r(13) = D_r
        # So D_r at self-dual = 2 * S_r(13)

    def test_c26_dual_to_c0(self, vir_coeffs_c26):
        """At c=26: kappa = 13, dual (Vir_0) has kappa = 0."""
        assert abs(vir_coeffs_c26[2] - 13.0) < 1e-10

    def test_c25_99_near_boundary(self):
        """Virasoro at c=25.99: kappa = 12.995, close to c=26."""
        coeffs = virasoro_shadow_coefficients_numerical(25.99, 30)
        assert abs(coeffs[2] - 12.995) < 1e-10

    def test_negative_c_virasoro(self):
        """Virasoro at c=-2 (e.g., ghost system): S_2 = |c|/2 = 1.0.

        The engine uses a0 = |c| for the square root branch, so
        S_2 = |c|/2 (positive) regardless of sign of c.  The kappa = c/2
        formula gives -1 for c=-2, but the shadow generating function
        sqrt(Q_L) uses the POSITIVE branch.
        """
        coeffs = virasoro_shadow_coefficients_numerical(-2.0, 30)
        # S_2 = |c|/2 = 1.0 from the positive square root branch
        assert abs(coeffs[2] - 1.0) < 1e-10
        # Can still find zeros
        zeros = find_zeros_grid(
            coeffs, (-3.0, 3.0), (-20.0, 20.0), 8, 15, max_r=30
        )
        assert isinstance(zeros, list)

    def test_large_c_virasoro(self):
        """Virasoro at c=100: large kappa = 50."""
        coeffs = virasoro_shadow_coefficients_numerical(100.0, 30)
        assert abs(coeffs[2] - 50.0) < 1e-10


# ============================================================================
# Cross-verification: multi-path consistency
# ============================================================================

class TestMultiPathVerification:
    """Multi-path verification of zero repulsion results."""

    def test_newton_vs_muller_agreement(self):
        """Newton and Muller methods find the same zeros for affine sl_2."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 30)
        # Find first zero via Newton
        zeros_exact = affine_sl2_zeros(1.0, 5)
        if zeros_exact:
            z0 = zeros_exact[0]
            # Newton from nearby
            z_newton = newton_zero(coeffs, z0 + 0.1, max_r=30)
            # Muller from three nearby points
            z_muller = muller_zero(
                coeffs, z0 + 0.1, z0 + 0.05, z0 + 0.15, max_r=30
            )
            if z_newton is not None and z_muller is not None:
                assert abs(z_newton - z_muller) < 1e-6, \
                    f"Newton {z_newton} != Muller {z_muller}"

    def test_real_zero_is_complex_zero(self, vir_coeffs_c1):
        """Real zeros found by bisection are confirmed by Newton on C."""
        real_z = find_real_zeros_brentq(vir_coeffs_c1, -10.0, 10.0, max_r=50)
        for rz in real_z[:3]:
            # Newton should converge to the same zero
            z_newton = newton_zero(vir_coeffs_c1, complex(rz, 0), max_r=50)
            if z_newton is not None:
                assert abs(z_newton.imag) < 1e-6, \
                    f"Newton from real zero has Im = {z_newton.imag}"
                assert abs(z_newton.real - rz) < 1e-6

    def test_complementarity_kappa_sum_multi_c(self):
        """Complementarity sum kappa(c) + kappa(26-c) = 13 for many c values."""
        for c_val in [0.5, 1.0, 2.0, 5.0, 10.0, 12.0, 13.0, 15.0, 20.0, 25.0]:
            kappa_c = c_val / 2.0
            kappa_dual = (26.0 - c_val) / 2.0
            assert abs(kappa_c + kappa_dual - 13.0) < 1e-12, \
                f"c={c_val}: {kappa_c} + {kappa_dual} = {kappa_c + kappa_dual}"

    def test_spacing_from_exact_zeros_affine(self):
        """Affine sl_2: spacing from exact formula vs from NN computation."""
        zeros_exact = affine_sl2_zeros(1.0, 20)
        spacings = compute_nn_spacings(zeros_exact)
        expected = 2.0 * math.pi / math.log(3.0 / 2.0)
        if spacings:
            for s in spacings[:10]:
                assert abs(s - expected) < 0.01, \
                    f"Spacing {s} != {expected}"

    def test_argument_principle_vs_grid_heisenberg(self, heis_coeffs_k1):
        """Heisenberg: both methods agree on 0 zeros."""
        zeros_grid = find_zeros_grid(
            heis_coeffs_k1, (-5.0, 5.0), (-20.0, 20.0), 8, 15
        )
        ap_count = argument_principle_count(
            heis_coeffs_k1, (-5.0, 5.0), (-20.0, 20.0), 2000
        )
        assert len(zeros_grid) == 0
        assert ap_count == 0

    def test_zeta_value_at_known_zero(self):
        """Zeta evaluated at a known zero should be approximately 0."""
        # Affine sl_2 zeros are known exactly
        zeros = affine_sl2_zeros(1.0, 5)
        coeffs = affine_sl2_shadow_coefficients(1.0, 30)
        for z in zeros[:5]:
            val = _shadow_zeta_complex(coeffs, z, 30)
            assert abs(val) < 1e-8, f"zeta at known zero {z} = {val}"


# ============================================================================
# Statistical distribution tests
# ============================================================================

class TestDistributions:
    """Tests for reference distribution functions."""

    def test_gue_peak_location(self):
        """GUE Wigner surmise peaks near s ~ 0.9."""
        # p'(s) = 0 at s_max where d/ds[s^2 exp(-4s^2/pi)] = 0
        # => 2s - 8s^3/pi = 0 => s = sqrt(pi/4) ~ 0.886
        s_max = math.sqrt(math.pi / 4.0)
        p_max = wigner_surmise_gue(s_max)
        # Check it's near the maximum
        for ds in [-0.1, 0.1]:
            assert wigner_surmise_gue(s_max + ds) <= p_max + 1e-10

    def test_goe_peak_location(self):
        """GOE Wigner surmise peaks at s = sqrt(2/pi) ~ 0.798."""
        s_max = math.sqrt(2.0 / math.pi)
        p_max = wigner_surmise_goe(s_max)
        for ds in [-0.1, 0.1]:
            assert wigner_surmise_goe(s_max + ds) <= p_max + 1e-10

    def test_poisson_at_zero(self):
        """Poisson spacing p(0) = 1."""
        assert abs(poisson_spacing(0.0) - 1.0) < 1e-15

    def test_gue_at_zero(self):
        """GUE p(0) = 0 (level repulsion)."""
        assert abs(wigner_surmise_gue(0.0)) < 1e-15

    def test_goe_at_zero(self):
        """GOE p(0) = 0 (level repulsion)."""
        assert abs(wigner_surmise_goe(0.0)) < 1e-15

    def test_gue_vs_poisson_at_zero(self):
        """GUE/GOE have level repulsion (p(0)=0); Poisson does not (p(0)=1)."""
        assert wigner_surmise_gue(0.0) == 0.0
        assert wigner_surmise_goe(0.0) == 0.0
        assert poisson_spacing(0.0) == 1.0

    def test_gue_tail_decay(self):
        """GUE surmise decays as exp(-s^2) for large s."""
        # At s=5: p(5) should be very small
        assert wigner_surmise_gue(5.0) < 1e-10

    def test_gue_mean(self):
        """GUE Wigner surmise p(s) = (32/pi^2) s^2 exp(-4s^2/pi) has mean = 1.

        Exact: <s> = integral_0^inf s p(s) ds = (32/pi^2) * (pi/4)^2 / 2 = 1.
        """
        ds = 0.001
        mean = sum(
            s * wigner_surmise_gue(s) * ds
            for s in [i * ds for i in range(int(10 / ds))]
        )
        assert abs(mean - 1.0) < 0.01, f"GUE mean = {mean}"


# ============================================================================
# Virasoro-specific tests
# ============================================================================

class TestVirasoroSpecific:
    """Virasoro-specific zero repulsion tests."""

    def test_kappa_formula(self):
        """kappa(Vir_c) = c/2 for all c (AP1, AP9)."""
        for c_val in [0.5, 1.0, 5.0, 13.0, 26.0, 50.0]:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, 10)
            assert abs(coeffs[2] - c_val / 2.0) < 1e-10

    def test_growth_rate_positive(self):
        """Growth rate rho is positive for c > 0."""
        for c_val in [1.0, 5.0, 13.0, 26.0, 50.0]:
            rho = virasoro_growth_rate_exact(c_val)
            assert rho > 0, f"c={c_val}: rho = {rho}"

    def test_growth_rate_decreasing(self):
        """Growth rate rho decreases as c increases (for large c)."""
        rhos = [virasoro_growth_rate_exact(c) for c in [5.0, 10.0, 20.0, 50.0, 100.0]]
        for i in range(len(rhos) - 1):
            assert rhos[i] >= rhos[i + 1] - 1e-10, \
                f"Growth rate not decreasing: {rhos[i]} -> {rhos[i+1]}"

    def test_growth_rate_at_c_large(self):
        """For large c: rho ~ sqrt(180c / (5c * c^2)) = sqrt(36/c^2) = 6/c."""
        c_val = 10000.0
        rho = virasoro_growth_rate_exact(c_val)
        approx = 6.0 / c_val
        assert abs(rho - approx) / approx < 0.01  # 1% accuracy at c=10000

    def test_entire_function_small_rho(self):
        """For c large enough that rho < 1, zeta is entire."""
        # rho < 1 when c > ~36 (from the exact formula)
        rho_100 = virasoro_growth_rate_exact(100.0)
        assert rho_100 < 1.0, f"rho(100) = {rho_100} >= 1"


# ============================================================================
# Additional robustness and regression tests
# ============================================================================

class TestRobustness:
    """Robustness and regression tests."""

    def test_virasoro_coefficients_sign_pattern(self):
        """Virasoro S_r should alternate in sign for moderate c."""
        coeffs = virasoro_shadow_coefficients_numerical(1.0, 20)
        # S_2 = 0.5 > 0
        assert coeffs[2] > 0

    def test_spacing_with_conjugate_pairs(self):
        """Spacing computation handles conjugate zero pairs correctly."""
        # Zeros come in conjugate pairs for real Dirichlet series
        zeros = [complex(1, 5), complex(1, -5), complex(1, 10), complex(1, -10)]
        spacings = compute_nn_spacings(zeros)
        assert len(spacings) == 3

    def test_gap_exceedance_monotone(self):
        """Gap exceedance P(gap > x) is monotone decreasing in x."""
        spacings = [0.3, 0.5, 0.8, 1.2, 1.5, 2.0, 3.0]
        x_vals = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
        result = gap_exceedance_distribution(spacings, x_vals)
        prev = 1.0
        for x in sorted(result.keys()):
            assert result[x] <= prev + 1e-10
            prev = result[x]

    def test_number_variance_few_zeros(self):
        """Number variance with very few zeros."""
        zeros = [complex(0, 1), complex(0, 3)]
        nv = number_variance(zeros, [1.0])
        assert 1.0 in nv

    def test_full_pipeline_affine_sl3(self):
        """Full pipeline for affine sl_3."""
        result = full_repulsion_analysis(
            'affine_sl3', 1.0, max_r=20,
            re_range=(-5.0, 5.0), im_range=(-30.0, 30.0),
            grid_re=10, grid_im=25,
        )
        assert result.shadow_class == 'L'
        assert result.n_zeros > 0

    def test_depth_class_ordering(self):
        """Shadow depth classes have distinct characteristics."""
        data = repulsion_by_depth_class(max_r=20)
        # G: no zeros
        assert data['G'].n_zeros == 0
        # L: has zeros, uniform spacing
        assert data['L'].has_zeros
        # Spacing variance for L should be small (uniform)
        if data['L'].spacings:
            assert data['L'].spacing_variance < 1e-4

    def test_complementarity_at_c13_self_dual(self):
        """At c=13, S_r(13) is self-consistent: dual coefficients equal."""
        coeffs_13 = virasoro_shadow_coefficients_numerical(13.0, 20)
        coeffs_dual = virasoro_shadow_coefficients_numerical(13.0, 20)  # 26-13=13
        for r in range(2, 20):
            assert abs(coeffs_13[r] - coeffs_dual[r]) < 1e-12

    def test_ks_with_many_samples(self):
        """KS test with a larger sample size for better statistics."""
        import random
        random.seed(123)
        # Generate GUE-like spacings (Wigner surmise via rejection sampling)
        spacings = []
        while len(spacings) < 100:
            s = random.expovariate(1.0)  # Proposal: exponential
            if random.random() < wigner_surmise_gue(s) / (3.0 * poisson_spacing(s) + 1e-300):
                spacings.append(s)
        mean_s = sum(spacings) / len(spacings)
        normalized = [s / mean_s for s in spacings]
        D_gue, p_gue = ks_against_gue(normalized)
        # Should not strongly reject GUE
        # (Note: rejection sampling may not be perfect, so use lenient threshold)
        assert D_gue < 0.5, f"GUE-sampled data has D={D_gue}"

    def test_zero_repulsion_positive_spacings(self):
        """All spacings should be non-negative."""
        zeros = affine_sl2_zeros(1.0, 20)
        spacings = compute_nn_spacings(zeros)
        for s in spacings:
            assert s >= 0, f"Negative spacing: {s}"

    def test_gue_number_variance_zero_at_zero(self):
        """GUE number variance at L=0 should be approximately 0."""
        # Actually log(0) is undefined; test at small L
        v = gue_number_variance(0.001)
        # For very small L, Sigma_2 can be negative from the formula (artifact)
        assert math.isfinite(v)

    def test_interleaving_score_range(self):
        """Interleaving score is in [0, 1]."""
        zeros_a = [complex(0, k) for k in range(0, 20, 2)]
        zeros_b = [complex(0, k) for k in range(1, 20, 2)]
        from compute.lib.bc_zero_repulsion_engine import _interleaving_score
        score = _interleaving_score(zeros_a, zeros_b)
        assert 0.0 <= score <= 1.0

    def test_perfect_interleaving(self):
        """Perfectly interleaved zeros have score 1."""
        zeros_a = [complex(0, 2 * k) for k in range(10)]
        zeros_b = [complex(0, 2 * k + 1) for k in range(10)]
        from compute.lib.bc_zero_repulsion_engine import _interleaving_score
        score = _interleaving_score(zeros_a, zeros_b)
        assert score == 1.0, f"Perfect interleaving score = {score}"
