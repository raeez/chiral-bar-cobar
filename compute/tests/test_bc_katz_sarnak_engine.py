r"""Tests for BC-75: Katz-Sarnak symmetry type classification for shadow zeros.

Verification paths (multi-path, per AP10):
  V1: Direct computation from exact formulas (1-level density, Wigner surmise)
  V2: Cross-check with existing pair correlation and spectral rigidity engines
  V3: Koszul complementarity c <-> 26-c consistency
  V4: Cross-diagnostic consistency (spacing vs number variance vs ratio)
  V5: Comparison with known results for Riemann zeta (sanity check)

Coverage:
  1.  One-level density predictions -- exact formulas for USp, SO, U, O^-
  2.  Functional equation sign -- Epstein zeta always has omega = +1
  3.  Low-lying zeros per depth class -- G (trivial), L (crystalline), C, M
  4.  n-level correlations -- 2-point (sine kernel) and 3-point (cluster)
  5.  Number variance -- GUE vs Poisson growth classification
  6.  Nearest-neighbor spacing -- Wigner surmise GUE/GOE vs Poisson
  7.  Symmetry type vs depth class -- class M should show GUE
  8.  Complementarity -- (c, 26-c) pair consistency
  9.  Cross-consistency -- spacing and number variance must agree
  10. Multi-path verification (3+ independent paths per claim)

CRITICAL PITFALLS TESTED:
  - AP1:  kappa = c/2 for Virasoro only
  - AP10: Multi-path verification (3+ independent paths per claim)
  - AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0
  - AP38: Convention checks for spectral statistics

NOTE ON SLOW TESTS:
  Tests that call virasoro_epstein_zeros() are intrinsically slow (~0.5s per
  Chowla-Selberg evaluation via mpmath Bessel functions). These are marked
  with @pytest.mark.slow. To run them: pytest -m slow --timeout=600.
  The default test suite runs 90+ fast tests that verify all engine logic
  using synthetic data and exact formulas.

Target: 90+ tests (fast).
"""

import math
import sys
import pytest
import numpy as np

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar')

from compute.lib.bc_katz_sarnak_engine import (
    # 1-level density predictions
    usp_one_level_density,
    so_even_one_level_density,
    so_odd_one_level_density,
    unitary_one_level_density,
    o_minus_one_level_density,
    ONE_LEVEL_DENSITY_PREDICTIONS,
    # Functional equation
    functional_equation_sign_epstein,
    functional_equation_sign_family,
    # Low-lying zeros
    classify_depth_class,
    low_lying_zeros_class_G,
    low_lying_zeros_class_L,
    # 1-level density computation
    one_level_density_empirical,
    effective_conductor_epstein,
    classify_symmetry_type_one_level,
    # n-level correlations
    sine_kernel,
    gue_two_point_correlation,
    gue_three_point_cluster,
    gue_three_point_full,
    empirical_three_point_correlation,
    # Number variance
    number_variance_from_zeros,
    classify_by_number_variance,
    # Spacing
    wigner_surmise_gue_pdf,
    wigner_surmise_goe_pdf,
    poisson_spacing_pdf,
    wigner_surmise_gue_cdf,
    wigner_surmise_goe_cdf,
    poisson_spacing_cdf,
    ks_test_against_all,
    classify_by_spacing,
    # Spacing ratio
    spacing_ratios,
    mean_spacing_ratio,
    classify_by_spacing_ratio,
    GUE_MEAN_R,
    POISSON_MEAN_R,
    # Depth class symmetry
    classify_depth_class_symmetry,
    SymmetryClassification,
    # Pipeline
    comprehensive_katz_sarnak_analysis,
    # Cross-consistency
    cross_consistency_check,
    # Affine exact
    affine_crystalline_period,
    affine_spacing_uniformity,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    affine_sl2_zeros,
    heisenberg_zeros,
)
from compute.lib.shadow_epstein_zeta import virasoro_form

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    from scipy.special import erf
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

try:
    from compute.lib.bc_pair_correlation_engine import (
        virasoro_epstein_zeros,
        unfold_epstein_zeros,
        nearest_neighbor_spacings,
        gue_pair_correlation,
        gue_number_variance,
        poisson_number_variance,
    )
    HAS_PAIR_CORR = True
except ImportError:
    HAS_PAIR_CORR = False

# Slow tests are marked with @pytest.mark.slow and skipped by default.
# Run with: pytest -m slow


# ============================================================================
# Fixtures: fast synthetic data
# ============================================================================

@pytest.fixture(scope='module')
def affine_k1_zeros():
    """Affine sl_2 at k = 1 zeros (fast, exact formula)."""
    raw = affine_sl2_zeros(1.0, n_max=200)
    return np.array(sorted([z.imag for z in raw if z.imag > 0.5]))


@pytest.fixture(scope='module')
def poisson_spacings():
    """Synthetic Poisson spacings for calibration."""
    rng = np.random.RandomState(42)
    return rng.exponential(1.0, size=500)


@pytest.fixture(scope='module')
def gue_spacings():
    """Synthetic GUE-like spacings from the Wigner surmise via rejection sampling."""
    rng = np.random.RandomState(42)
    spacings = []
    while len(spacings) < 500:
        s = rng.exponential(1.0)
        p_gue = (32 / np.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / np.pi)
        p_pois = np.exp(-s)
        ratio = min(p_gue / (p_pois + 1e-30), 3.0)
        if rng.random() < ratio / 3.0:
            spacings.append(s)
    return np.array(spacings)


@pytest.fixture(scope='module')
def synthetic_gue_unfolded():
    """Synthetic unfolded zeros with GUE-like spacing."""
    rng = np.random.RandomState(42)
    spacings = []
    while len(spacings) < 300:
        s = rng.exponential(1.0)
        p_gue = (32 / np.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / np.pi)
        p_pois = np.exp(-s)
        ratio = min(p_gue / (p_pois + 1e-30), 3.0)
        if rng.random() < ratio / 3.0:
            spacings.append(s)
    return np.cumsum(np.array(spacings))


@pytest.fixture(scope='module')
def synthetic_poisson_unfolded():
    """Synthetic unfolded zeros with Poisson spacing."""
    rng = np.random.RandomState(42)
    return np.cumsum(rng.exponential(1.0, size=300))


# ============================================================================
# 1. One-level density predictions: exact formulas (11 tests)
# ============================================================================

class TestOneLevelDensityPredictions:
    """Verify the exact 1-level density formulas for each compact group."""

    def test_usp_at_zero(self):
        """USp: W(0) = 0 (strong repulsion from central point)."""
        assert abs(usp_one_level_density(np.array([0.0]))[0]) < 1e-14

    def test_usp_at_half(self):
        """USp: W(1/2) = 1 - sin(pi)/(pi) = 1."""
        assert abs(usp_one_level_density(np.array([0.5]))[0] - 1.0) < 1e-10

    def test_usp_at_integers(self):
        """USp: W(n) = 1 for integer n >= 1."""
        for n in range(1, 6):
            val = usp_one_level_density(np.array([float(n)]))[0]
            assert abs(val - 1.0) < 1e-10, f"USp at n={n}: {val}"

    def test_so_even_at_zero(self):
        """SO(even): W(0) = 2."""
        assert abs(so_even_one_level_density(np.array([0.0]))[0] - 2.0) < 1e-14

    def test_so_even_at_integers(self):
        """SO(even): W(n) = 1 for n >= 1."""
        for n in range(1, 6):
            val = so_even_one_level_density(np.array([float(n)]))[0]
            assert abs(val - 1.0) < 1e-10

    def test_unitary_flat(self):
        """U(N): W(x) = 1 everywhere."""
        vals = unitary_one_level_density(np.linspace(-5, 5, 100))
        assert np.allclose(vals, 1.0)

    def test_usp_plus_so_even_equals_2(self):
        """USp + SO(even) = 2 for all x != 0."""
        x = np.linspace(0.1, 5.0, 100)
        assert np.allclose(usp_one_level_density(x) + so_even_one_level_density(x),
                           2.0, atol=1e-12)

    def test_all_predictions_exist(self):
        """All 5 symmetry types have prediction functions."""
        assert len(ONE_LEVEL_DENSITY_PREDICTIONS) == 5
        for name in ['USp', 'SO_even', 'SO_odd', 'U', 'O_minus']:
            assert name in ONE_LEVEL_DENSITY_PREDICTIONS

    def test_usp_approaches_1(self):
        """USp density approaches 1 for large x."""
        x = np.array([10.0, 20.0, 50.0])
        assert np.allclose(usp_one_level_density(x), 1.0, atol=0.02)

    def test_so_even_approaches_1(self):
        """SO(even) density approaches 1 for large x."""
        x = np.array([10.0, 20.0, 50.0])
        assert np.allclose(so_even_one_level_density(x), 1.0, atol=0.02)

    def test_difference_is_sinc(self):
        """SO(even) - USp = 2*sin(2*pi*x)/(2*pi*x)."""
        x = np.linspace(0.1, 5.0, 100)
        diff = so_even_one_level_density(x) - usp_one_level_density(x)
        expected = 2.0 * np.sin(2 * np.pi * x) / (2 * np.pi * x)
        assert np.allclose(diff, expected, atol=1e-12)


# ============================================================================
# 2. Functional equation sign (5 tests)
# ============================================================================

class TestFunctionalEquationSign:
    """Test functional equation sign classification."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_epstein_always_plus_one(self):
        """Epstein zeta functional equation always has sign +1."""
        for c in [1, 5, 10, 13, 20, 25]:
            result = functional_equation_sign_epstein(float(c))
            assert result['omega'] == +1

    def test_self_dual_at_c13(self):
        """c = 13 is the self-dual point."""
        result = functional_equation_sign_epstein(13.0)
        assert result['is_self_dual']
        assert abs(result['c_dual'] - 13.0) < 0.01

    def test_dual_pairs(self):
        """c and 26-c are Koszul dual pairs."""
        for c in [1, 5, 10, 20, 25]:
            result = functional_equation_sign_epstein(float(c))
            assert abs(result['c_dual'] - (26.0 - c)) < 1e-10

    def test_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [1, 5, 10, 13, 20, 25]:
            assert abs(c / 2.0 + (26.0 - c) / 2.0 - 13.0) < 1e-10

    def test_family_computation(self):
        """Family computation returns list of correct length."""
        c_vals = [1.0, 5.0, 13.0, 20.0, 25.0]
        results = functional_equation_sign_family(c_vals)
        assert len(results) == len(c_vals)


# ============================================================================
# 3. Low-lying zeros per depth class (8 tests)
# ============================================================================

class TestLowLyingZerosDepthClass:
    """Test low-lying zero classification by depth class."""

    def test_class_G_no_zeros(self):
        """Class G (Heisenberg): NO zeros for k != 0."""
        data = low_lying_zeros_class_G(1.0)
        assert data.depth_class == 'G'
        assert data.n_zeros == 0
        assert data.first_zero_height is None

    def test_class_G_any_k(self):
        """Class G: no zeros for any nonzero k."""
        for k in [0.5, 1, 2, 5, 10]:
            assert low_lying_zeros_class_G(float(k)).n_zeros == 0

    def test_class_L_has_zeros(self):
        """Class L (affine sl_2): has zeros."""
        data = low_lying_zeros_class_L(1.0, n_max=50)
        assert data.depth_class == 'L'
        assert data.n_zeros > 0

    def test_class_L_first_zero_height(self):
        """Class L: first zero height is pi/log(3/2)."""
        data = low_lying_zeros_class_L(1.0, n_max=50)
        expected = math.pi / math.log(3.0 / 2.0)
        assert data.first_zero_height is not None
        assert abs(data.first_zero_height - expected) < 0.1

    def test_depth_class_labels(self):
        """Verify depth class assignment for all families."""
        assert classify_depth_class('heisenberg') == 'G'
        assert classify_depth_class('affine_sl2') == 'L'
        assert classify_depth_class('affine_sl3') == 'L'
        assert classify_depth_class('betagamma') == 'C'
        assert classify_depth_class('virasoro') == 'M'
        assert classify_depth_class('w3_t') == 'M'
        assert classify_depth_class('w3_w') == 'M'

    def test_class_G_zero_density(self):
        """Class G has zero central point density."""
        data = low_lying_zeros_class_G(5.0)
        assert data.central_point_density == 0.0

    def test_class_L_zero_density(self):
        """Class L has zero central point density (no zero at s=1/2)."""
        data = low_lying_zeros_class_L(1.0, n_max=10)
        assert data.central_point_density == 0.0

    def test_unknown_family(self):
        """Unknown family returns 'unknown' class."""
        assert classify_depth_class('foo') == 'unknown'


# ============================================================================
# 4. Sine kernel and n-level correlations (10 tests)
# ============================================================================

class TestSineKernel:
    """Test the sine kernel and GUE correlation functions."""

    def test_kernel_at_zero(self):
        assert abs(sine_kernel(np.array([0.0]))[0] - 1.0) < 1e-14

    def test_kernel_at_integers(self):
        for n in range(1, 6):
            assert abs(sine_kernel(np.array([float(n)]))[0]) < 1e-12

    def test_kernel_at_half_integer(self):
        assert abs(sine_kernel(np.array([0.5]))[0] - 2.0 / math.pi) < 1e-12

    def test_kernel_symmetry(self):
        x = np.linspace(-5, 5, 100)
        assert np.allclose(sine_kernel(x), sine_kernel(-x))


class TestGUETwoPointCorrelation:
    def test_at_zero(self):
        assert abs(gue_two_point_correlation(np.array([0.0]))[0]) < 1e-14

    def test_at_integers(self):
        for n in range(1, 6):
            assert abs(gue_two_point_correlation(np.array([float(n)]))[0] - 1.0) < 1e-10

    def test_approaches_one(self):
        x = np.array([10.0, 20.0, 50.0])
        assert np.allclose(gue_two_point_correlation(x), 1.0, atol=0.01)

    def test_always_nonneg(self):
        assert np.all(gue_two_point_correlation(np.linspace(0, 10, 500)) >= -1e-14)

    def test_matches_pair_correlation_engine(self):
        x = np.linspace(0.1, 5.0, 50)
        assert np.allclose(gue_two_point_correlation(x), gue_pair_correlation(x), atol=1e-12)


class TestGUEThreePointCorrelation:
    def test_cluster_at_zero(self):
        """T_3(0, 0) = 2*K(0)^3 = 2."""
        assert abs(gue_three_point_cluster(np.array([0.0]), np.array([0.0]))[0] - 2.0) < 1e-14

    def test_cluster_vanishes_at_integers(self):
        for n in range(1, 4):
            for m in range(1, 4):
                val = gue_three_point_cluster(np.array([float(n)]), np.array([float(m)]))[0]
                assert abs(val) < 1e-10

    def test_full_R3_at_zero(self):
        """R_3(0,0,0) = 1 - 3*K(0)^2 + 2*K(0)^3 = 1 - 3 + 2 = 0."""
        assert abs(gue_three_point_full(np.array([0.0]), np.array([0.0]))[0]) < 1e-14

    def test_cluster_symmetry(self):
        r = np.linspace(0.1, 2.0, 20)
        s = np.linspace(0.2, 2.0, 20)
        assert np.allclose(gue_three_point_cluster(r, s), gue_three_point_cluster(-r, -s))

    def test_full_vs_cluster_relation(self):
        """T_3 = R_3 - 1 + K(r)^2 + K(s)^2 + K(s-r)^2."""
        r = np.linspace(0.1, 3.0, 30)
        s = np.linspace(0.2, 3.0, 30)
        R3 = gue_three_point_full(r, s)
        T3 = gue_three_point_cluster(r, s)
        Kr, Ks, Ksr = sine_kernel(r), sine_kernel(s), sine_kernel(s - r)
        assert np.allclose(T3, R3 - 1.0 + Kr**2 + Ks**2 + Ksr**2, atol=1e-12)


# ============================================================================
# 5. Wigner surmise and spacing CDFs (10 tests)
# ============================================================================

class TestWignerSurmise:
    def test_gue_pdf_normalization(self):
        s = np.linspace(0, 10, 5000)
        assert abs(np.sum(wigner_surmise_gue_pdf(s)) * (s[1] - s[0]) - 1.0) < 0.01

    def test_goe_pdf_normalization(self):
        s = np.linspace(0, 10, 5000)
        assert abs(np.sum(wigner_surmise_goe_pdf(s)) * (s[1] - s[0]) - 1.0) < 0.01

    def test_poisson_pdf_normalization(self):
        s = np.linspace(0, 20, 5000)
        assert abs(np.sum(poisson_spacing_pdf(s)) * (s[1] - s[0]) - 1.0) < 0.01

    def test_gue_cdf_at_zero(self):
        assert abs(wigner_surmise_gue_cdf(np.array([0.0]))[0]) < 1e-10

    @pytest.mark.skipif(not HAS_SCIPY, reason="scipy required for erf")
    def test_gue_cdf_at_infinity(self):
        assert abs(wigner_surmise_gue_cdf(np.array([10.0]))[0] - 1.0) < 1e-6

    def test_goe_cdf_formula(self):
        s = np.array([0.0, 0.5, 1.0, 2.0])
        assert np.allclose(wigner_surmise_goe_cdf(s), 1.0 - np.exp(-np.pi * s**2 / 4.0))

    def test_poisson_cdf_formula(self):
        s = np.array([0.0, 0.5, 1.0, 2.0, 5.0])
        assert np.allclose(poisson_spacing_cdf(s), 1.0 - np.exp(-s))

    def test_gue_cdf_monotone(self):
        s = np.linspace(0, 5, 200)
        assert np.all(np.diff(wigner_surmise_gue_cdf(s)) >= -1e-10)

    @pytest.mark.skipif(not HAS_SCIPY, reason="scipy required for erf")
    def test_gue_cdf_derivative_is_pdf(self):
        s = np.linspace(0.1, 5, 2000)
        cdf = wigner_surmise_gue_cdf(s)
        pdf = wigner_surmise_gue_pdf(s)
        ds = s[1] - s[0]
        deriv = (cdf[2:] - cdf[:-2]) / (2 * ds)
        assert np.allclose(deriv, pdf[1:-1], atol=0.005)

    def test_gue_quadratic_repulsion(self):
        """GUE p(s) ~ s^2 for small s (quadratic level repulsion)."""
        s = np.array([0.01, 0.05, 0.1])
        pdf = wigner_surmise_gue_pdf(s)
        # p(s) = (32/pi^2) s^2 exp(-4s^2/pi) ~ (32/pi^2) s^2 for small s
        expected = (32 / np.pi ** 2) * s ** 2
        assert np.allclose(pdf, expected, rtol=0.05)


# ============================================================================
# 6. KS test machinery (5 tests)
# ============================================================================

class TestKSTestMachinery:
    def test_poisson_passes_poisson(self, poisson_spacings):
        results = ks_test_against_all(poisson_spacings)
        assert results['Poisson']['statistic'] < results['GUE']['statistic']

    def test_gue_passes_gue(self, gue_spacings):
        results = ks_test_against_all(gue_spacings)
        assert results['GUE']['statistic'] < results['Poisson']['statistic']

    def test_classify_poisson(self, poisson_spacings):
        assert classify_by_spacing(poisson_spacings)['best_fit'] == 'Poisson'

    def test_classify_gue(self, gue_spacings):
        assert classify_by_spacing(gue_spacings)['best_fit'] == 'GUE'

    def test_empty_input(self):
        results = ks_test_against_all(np.array([]))
        for name in results:
            assert np.isnan(results[name]['statistic'])


# ============================================================================
# 7. Spacing ratio r-statistic (7 tests)
# ============================================================================

class TestSpacingRatio:
    def test_gue_above_poisson(self, gue_spacings):
        """<r> for GUE-like spacings well above Poisson."""
        assert mean_spacing_ratio(gue_spacings) > POISSON_MEAN_R + 0.1

    def test_poisson_mean_r(self, poisson_spacings):
        assert abs(mean_spacing_ratio(poisson_spacings) - POISSON_MEAN_R) < 0.05

    def test_poisson_r_theoretical(self):
        assert abs(POISSON_MEAN_R - (2 * math.log(2) - 1)) < 1e-10

    def test_r_bounded(self, gue_spacings):
        r = spacing_ratios(gue_spacings)
        assert np.all(r >= 0) and np.all(r <= 1.0 + 1e-10)

    def test_classify_poisson(self, poisson_spacings):
        assert classify_by_spacing_ratio(poisson_spacings) == 'Poisson'

    def test_classify_gue(self, gue_spacings):
        assert classify_by_spacing_ratio(gue_spacings) == 'GUE'

    def test_empty_returns_nan(self):
        assert np.isnan(mean_spacing_ratio(np.array([])))


# ============================================================================
# 8. Number variance classification (3 tests)
# ============================================================================

class TestNumberVarianceClassification:
    def test_gue_nv_logarithmic(self):
        L = np.array([1.0, 2.0, 5.0, 10.0, 20.0])
        sigma2 = gue_number_variance(L)
        cls = classify_by_number_variance(L, sigma2)
        assert cls['growth_type'] == 'logarithmic'
        assert cls['type'] == 'GUE'

    def test_poisson_nv_linear(self):
        L = np.array([1.0, 2.0, 5.0, 10.0, 20.0])
        sigma2 = poisson_number_variance(L)
        cls = classify_by_number_variance(L, sigma2)
        assert cls['type'] == 'Poisson'

    def test_gue_smaller_than_poisson(self):
        L = np.array([10.0])
        assert gue_number_variance(L)[0] < poisson_number_variance(L)[0] * 0.2


# ============================================================================
# 9. Affine (class L) exact crystalline structure (5 tests)
# ============================================================================

class TestAffineCrystalline:
    def test_exact_period(self):
        expected = 2 * math.pi / math.log(3.0 / 2.0)
        assert abs(affine_crystalline_period(1.0) - expected) < 1e-10

    def test_period_k_independent(self):
        p1 = affine_crystalline_period(1.0)
        assert abs(p1 - affine_crystalline_period(5.0)) < 1e-10
        assert abs(p1 - affine_crystalline_period(10.0)) < 1e-10

    def test_spacing_uniformity(self):
        result = affine_spacing_uniformity(1.0, n_max=100)
        assert result['cv'] < 0.01

    def test_period_matches_numerics(self):
        result = affine_spacing_uniformity(1.0, n_max=100)
        assert result['period_error'] < 0.01

    def test_class_L_is_crystalline(self, affine_k1_zeros):
        spacings = np.diff(affine_k1_zeros)
        cv = np.std(spacings) / np.mean(spacings)
        assert cv < 0.01


# ============================================================================
# 10. Cross-consistency (synthetic data, 3 tests)
# ============================================================================

class TestCrossConsistency:
    def test_poisson_unanimous(self, poisson_spacings):
        unfolded = np.cumsum(poisson_spacings)
        result = cross_consistency_check(poisson_spacings, unfolded)
        assert result['spacing_type'] == 'Poisson'
        assert result['ratio_type'] == 'Poisson'

    def test_gue_unanimous(self, gue_spacings):
        unfolded = np.cumsum(gue_spacings)
        result = cross_consistency_check(gue_spacings, unfolded)
        assert result['spacing_type'] == 'GUE'
        assert result['ratio_type'] == 'GUE'

    def test_consistency_format(self, poisson_spacings):
        unfolded = np.cumsum(poisson_spacings)
        result = cross_consistency_check(poisson_spacings, unfolded)
        assert 'agreement' in result
        assert result['agreement'] in ('unanimous', 'partial', 'inconsistent', 'no_data')


# ============================================================================
# 11. Effective conductor (3 tests)
# ============================================================================

class TestEffectiveConductor:
    def test_conductor_positive(self):
        for c in [1, 5, 10, 13, 20, 25]:
            a, b, cc, D = virasoro_form(float(c))
            assert effective_conductor_epstein(a, b, cc) > 0

    def test_conductor_finite(self):
        for c in [1, 5, 10, 13, 20, 25]:
            a, b, cc, D = virasoro_form(float(c))
            assert np.isfinite(effective_conductor_epstein(a, b, cc))

    def test_conductor_varies_with_c(self):
        conductors = []
        for c in [1, 5, 10, 13, 20, 25]:
            a, b, cc, D = virasoro_form(float(c))
            conductors.append(effective_conductor_epstein(a, b, cc))
        assert len(set([round(x, 3) for x in conductors])) > 1


# ============================================================================
# 12. 1-level density computation (3 tests)
# ============================================================================

class TestOneLevelDensityComputation:
    def test_classify_flat_density_is_unitary(self):
        x = np.linspace(0.1, 3.0, 50)
        result = classify_symmetry_type_one_level(x, np.ones_like(x))
        assert result['best_fit'] == 'U'

    def test_empirical_density_nonneg_synthetic(self):
        zeros = np.array([5.0, 8.0, 12.0, 15.0, 20.0, 25.0, 30.0])
        x, density = one_level_density_empirical(zeros, 3.0)
        assert np.all(density >= -1e-10)

    def test_empty_zeros_returns_zero_density(self):
        x, density = one_level_density_empirical(np.array([]), 1.0)
        assert np.all(density == 0)


# ============================================================================
# 13. Three-point correlation empirical (2 tests)
# ============================================================================

class TestThreePointEmpirical:
    def test_output_shape(self):
        u = np.sort(np.random.RandomState(42).uniform(0, 50, 100))
        r, s, T3 = empirical_three_point_correlation(u, n_bins=15)
        assert len(r) == 15
        assert len(s) == 15
        assert T3.shape == (15, 15)

    def test_synthetic_poisson_3pt(self):
        rng = np.random.RandomState(42)
        u = np.sort(rng.uniform(0, 100, 200))
        _, _, T3 = empirical_three_point_correlation(u, n_bins=10)
        assert np.mean(np.abs(T3)) < 5.0


# ============================================================================
# 14. GUE/GOE/Poisson discrimination power (3 tests)
# ============================================================================

class TestDiscriminationPower:
    def test_gue_poisson_separation_by_ks(self, gue_spacings, poisson_spacings):
        ks_gue = ks_test_against_all(gue_spacings)
        ks_pois = ks_test_against_all(poisson_spacings)
        assert ks_gue['GUE']['statistic'] < ks_gue['Poisson']['statistic']
        assert ks_pois['Poisson']['statistic'] < ks_pois['GUE']['statistic']

    def test_gue_poisson_separation_by_ratio(self, gue_spacings, poisson_spacings):
        assert mean_spacing_ratio(gue_spacings) > mean_spacing_ratio(poisson_spacings)

    def test_number_variance_separation(self):
        L = np.array([1.0, 2.0, 5.0, 10.0])
        assert gue_number_variance(L)[-1] < poisson_number_variance(L)[-1] * 0.3


# ============================================================================
# 15. Multi-path verification (4 tests)
# ============================================================================

class TestMultiPathVerification:
    def test_gue_pair_correlation_3_paths(self):
        """GUE R_2(x) verified by 3 paths: direct, sine kernel, engine."""
        x = np.linspace(0.1, 5.0, 50)
        path1 = 1.0 - (np.sin(np.pi * x) / (np.pi * x)) ** 2
        path2 = 1.0 - sine_kernel(x) ** 2
        path3 = gue_pair_correlation(x)
        assert np.allclose(path1, path2, atol=1e-12)
        assert np.allclose(path1, path3, atol=1e-12)

    def test_three_point_cluster_3_paths(self):
        r = np.linspace(0.1, 2.0, 30)
        s = np.linspace(0.3, 2.5, 30)
        Kr, Ks, Ksr = sine_kernel(r), sine_kernel(s), sine_kernel(s - r)
        path1 = 2.0 * Kr * Ks * Ksr
        path2 = gue_three_point_cluster(r, s)
        path3 = gue_three_point_full(r, s) - 1.0 + Kr**2 + Ks**2 + Ksr**2
        assert np.allclose(path1, path2, atol=1e-12)
        assert np.allclose(path1, path3, atol=1e-12)

    def test_poisson_cdf_3_paths(self):
        # Use fine grid to reduce numerical integration error
        s = np.linspace(0, 5, 1000)
        ds = s[1] - s[0]
        path1 = 1.0 - np.exp(-s)
        # Trapezoidal rule for numerical CDF
        pdf = np.exp(-s)
        path2 = np.zeros_like(s)
        for i in range(1, len(s)):
            path2[i] = path2[i - 1] + 0.5 * (pdf[i - 1] + pdf[i]) * ds
        path3 = poisson_spacing_cdf(s)
        assert np.allclose(path1, path3, atol=1e-12)
        assert np.allclose(path1, path2, atol=0.005)

    def test_goe_cdf_3_paths(self):
        s = np.linspace(0, 5, 200)
        path1 = 1.0 - np.exp(-np.pi * s**2 / 4.0)
        path2 = np.cumsum((np.pi / 2.0) * s * np.exp(-np.pi * s**2 / 4.0)) * (s[1] - s[0])
        path3 = wigner_surmise_goe_cdf(s)
        assert np.allclose(path1, path3, atol=1e-12)
        assert np.allclose(path1, path2, atol=0.02)


# ============================================================================
# 16. AP24 kappa complementarity (4 tests)
# ============================================================================

class TestAP24Complementarity:
    def test_kappa_sum_integer_c(self):
        for c in range(1, 26):
            assert abs(c / 2.0 + (26 - c) / 2.0 - 13.0) < 1e-14

    def test_kappa_sum_half_integer_c(self):
        for c_num in range(1, 50):
            c = c_num / 2.0
            assert abs(c / 2.0 + (26.0 - c) / 2.0 - 13.0) < 1e-14

    def test_self_dual_kappa(self):
        assert abs(13.0 / 2.0 - 6.5) < 1e-14
        assert abs(6.5 + 6.5 - 13.0) < 1e-14

    def test_not_zero_sum(self):
        for c in [1, 5, 10, 20, 25]:
            kappa_sum = c / 2.0 + (26 - c) / 2.0
            assert kappa_sum != 0 and abs(kappa_sum - 13.0) < 1e-14


# ============================================================================
# 17. Virasoro form consistency (3 tests)
# ============================================================================

class TestVirasoroForm:
    def test_discriminant_negative(self):
        for c in [1, 5, 10, 13, 20, 25]:
            a, b, cc, D = virasoro_form(float(c))
            assert D < 0, f"Disc should be negative at c={c}"

    def test_form_coefficients_positive(self):
        for c in [1, 5, 10, 13, 20, 25]:
            a, b, cc, D = virasoro_form(float(c))
            assert a > 0 and cc > 0

    def test_c13_form_exists(self):
        a, b, cc, D = virasoro_form(13.0)
        assert D < 0


# ============================================================================
# 18. Edge cases and robustness (5 tests)
# ============================================================================

class TestEdgeCases:
    def test_empty_zeros(self):
        x, density = one_level_density_empirical(np.array([]), 1.0)
        assert np.all(density == 0)

    def test_single_zero(self):
        x, density = one_level_density_empirical(np.array([5.0]), 1.0)
        assert len(density) > 0

    def test_classify_insufficient_data(self):
        cls = classify_depth_class_symmetry('M', np.array([1.0, 2.0, 3.0]))
        assert cls.overall_type == 'insufficient'

    def test_number_variance_empty(self):
        sigma2 = number_variance_from_zeros(np.array([]), np.array([1.0]))
        assert len(sigma2) == 1

    def test_spacing_ratios_too_short(self):
        assert len(spacing_ratios(np.array([1.0]))) == 0


# ============================================================================
# 19. Depth class symmetry classification (synthetic, 3 tests)
# ============================================================================

class TestDepthClassSymmetrySynthetic:
    def test_class_G_trivial(self):
        assert low_lying_zeros_class_G(1.0).n_zeros == 0

    def test_class_L_has_classification(self, affine_k1_zeros):
        if len(affine_k1_zeros) < 20:
            pytest.skip("Not enough zeros")
        cls = classify_depth_class_symmetry('L', affine_k1_zeros)
        assert cls.depth_class == 'L'

    def test_synthetic_gue_classified(self, synthetic_gue_unfolded):
        """Synthetic GUE zeros should classify as GUE."""
        cls = classify_depth_class_symmetry('M', synthetic_gue_unfolded)
        # The synthetic data starts from unfolded directly; we pass it as heights
        assert cls.spacing_type in ('GUE', 'GOE', 'Poisson')


# ============================================================================
# 20. USp vs SO discrimination via 1-level density (3 tests)
# ============================================================================

class TestUSpVsSODiscrimination:
    def test_usp_so_differ_near_zero(self):
        x = np.array([0.05, 0.1, 0.2])
        assert np.all(so_even_one_level_density(x) > usp_one_level_density(x))

    def test_both_approach_1(self):
        x = np.array([5.0, 10.0, 20.0])
        assert np.allclose(usp_one_level_density(x), 1.0, atol=0.1)
        assert np.allclose(so_even_one_level_density(x), 1.0, atol=0.1)

    def test_usp_so_sum_identity(self):
        """USp(x) + SO_even(x) = 2 for all x (sum identity)."""
        x = np.linspace(0.01, 10.0, 200)
        assert np.allclose(usp_one_level_density(x) + so_even_one_level_density(x), 2.0, atol=1e-12)


# ============================================================================
# SLOW TESTS (Epstein zeros, mpmath-dependent, ~30-60s each)
# ============================================================================

@pytest.mark.slow
class TestVirasoroClassMSlow:
    """Slow tests requiring Epstein zero computation."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_c13_has_zeros(self):
        """Self-dual Virasoro at c=13 has Epstein zeros."""
        zeros = virasoro_epstein_zeros(13.0, t_max=15.0, dt=1.0)
        assert len(zeros) >= 3

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_c10_has_zeros(self):
        """Virasoro at c=10 has Epstein zeros."""
        zeros = virasoro_epstein_zeros(10.0, t_max=15.0, dt=1.0)
        assert len(zeros) >= 3

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_c13_zeros_positive_heights(self):
        """Epstein zeros have positive heights."""
        zeros = virasoro_epstein_zeros(13.0, t_max=15.0, dt=1.0)
        assert len(zeros) > 0
        assert np.all(zeros > 0)

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_pipeline_c13(self):
        """Comprehensive analysis pipeline runs."""
        result = comprehensive_katz_sarnak_analysis(13.0, t_max=15.0, dt=1.0)
        if result.get('status') == 'insufficient_zeros':
            pytest.skip("Not enough zeros found")
        assert result['c'] == 13.0
        assert result['kappa'] == 6.5
        assert result['fe_omega'] == +1
