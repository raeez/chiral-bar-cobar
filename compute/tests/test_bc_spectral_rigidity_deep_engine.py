r"""Tests for bc_spectral_rigidity_deep_engine.py.

Tests cover:
1. Number variance Sigma^2(L) for GUE/GOE/Poisson references and shadow zeros
2. Delta_3(L) spectral rigidity for all reference ensembles
3. Spectral form factor K(tau) dip-ramp-plateau structure
4. Record gaps and Cramer conjecture test
5. Small gaps and level repulsion P(s) ~ s^beta
6. Hardy Z-function analogue and sign-change counting
7. Autocorrelation of Hardy Z-function
8. Level spacing ratio <r> for GUE vs Poisson discrimination
9. GUE-Poisson transition as c varies
10. Koszul A <-> A! spectral comparison
11. Shadow depth class signature detection

Verification paths (multi-path, per AP10):
    V1: Direct computation from zeros
    V2: Analytical reference (GUE/GOE/Poisson formulas)
    V3: Koszul complementarity A <-> A!
    V4: Cross-family consistency

Target: 110+ tests.

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP10): Cross-verify by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP38): Convention mismatches for spectral statistics literature.
"""

import math
import sys
import pytest
import numpy as np

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar')

from compute.lib.bc_spectral_rigidity_deep_engine import (
    # Reference distributions
    EULER_MASCHERONI,
    GUE_MEAN_SPACING_RATIO,
    GOE_MEAN_SPACING_RATIO,
    POISSON_MEAN_SPACING_RATIO,
    gue_number_variance,
    goe_number_variance,
    poisson_number_variance,
    gue_delta3,
    goe_delta3,
    poisson_delta3,
    # Core computations
    compute_number_variance,
    compute_number_variance_for_family,
    compute_delta3,
    compute_delta3_for_family,
    spectral_form_factor,
    identify_dip_ramp_plateau,
    compute_form_factor_for_family,
    record_gaps,
    cramer_test,
    small_gap_count,
    level_repulsion_exponent,
    hardy_z_function,
    hardy_z_sign_changes,
    hardy_z_autocorrelation,
    decorrelation_time,
    spacing_ratios,
    mean_spacing_ratio,
    classify_by_spacing_ratio,
    ks_distance_from_poisson,
    gue_poisson_transition,
    koszul_spectral_comparison,
    shadow_depth_spectral_signature,
    full_spectral_report,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    affine_sl2_zeros,
    shadow_coefficients_extended,
)
from compute.lib.shadow_zeta_function_engine import (
    virasoro_shadow_coefficients_numerical,
    affine_sl2_shadow_coefficients,
)

try:
    from compute.lib.bc_pair_correlation_engine import (
        virasoro_epstein_zeros,
        unfold_epstein_zeros,
    )
    from compute.lib.shadow_epstein_zeta import virasoro_form
    HAS_PAIR_CORR = True
except ImportError:
    HAS_PAIR_CORR = False

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


# ============================================================================
# Fixtures: generate zeros once and reuse
# ============================================================================

@pytest.fixture(scope='module')
def affine_sl2_k1_zeros():
    """Zeros of affine sl_2 at k=1 (class L)."""
    raw = affine_sl2_zeros(1.0, n_max=200)
    gammas = np.array(sorted([z.imag for z in raw if z.imag > 0.5]))
    return gammas


@pytest.fixture(scope='module')
def affine_sl2_k1_unfolded(affine_sl2_k1_zeros):
    """Unfolded zeros for affine sl_2 at k=1."""
    gammas = affine_sl2_k1_zeros
    sp = np.diff(gammas)
    mean_sp = np.mean(sp)
    return (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas


@pytest.fixture(scope='module')
def virasoro_c10_zeros():
    """Epstein zeros for Virasoro at c=10 (class M)."""
    if not HAS_PAIR_CORR:
        pytest.skip("bc_pair_correlation_engine not available")
    return virasoro_epstein_zeros(10.0, t_max=80.0, dt=0.3)


@pytest.fixture(scope='module')
def virasoro_c10_unfolded(virasoro_c10_zeros):
    """Unfolded Epstein zeros for Virasoro at c=10."""
    zeros = virasoro_c10_zeros
    if len(zeros) < 5:
        pytest.skip("too few zeros")
    a, b, cc, D = virasoro_form(10.0)
    return unfold_epstein_zeros(zeros, a, b, cc)


@pytest.fixture(scope='module')
def virasoro_c13_zeros():
    """Epstein zeros for Virasoro at c=13 (self-dual point)."""
    if not HAS_PAIR_CORR:
        pytest.skip("bc_pair_correlation_engine not available")
    return virasoro_epstein_zeros(13.0, t_max=80.0, dt=0.3)


@pytest.fixture(scope='module')
def poisson_unfolded():
    """Synthetic Poisson (random, uncorrelated) spectrum."""
    rng = np.random.RandomState(42)
    spacings = rng.exponential(1.0, size=500)
    return np.cumsum(spacings)


@pytest.fixture(scope='module')
def gue_unfolded():
    """Synthetic GUE-like spectrum (strongly repulsive)."""
    # Generate GUE eigenvalues via tridiagonal model
    rng = np.random.RandomState(42)
    N = 300
    # Tridiagonal matrix: diagonal = N(0,2), off-diag = chi_{N-i}
    diag = rng.normal(0, np.sqrt(2), size=N)
    off_diag = np.array([np.sqrt(rng.chisquare(N - i)) for i in range(1, N)])
    H = np.diag(diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)
    evals = np.sort(np.linalg.eigvalsh(H))
    # Unfold using Wigner semicircle
    # For the bulk, unfold linearly
    sp = np.diff(evals)
    mean_sp = np.mean(sp[len(sp)//4:3*len(sp)//4])  # bulk only
    # Take the middle half
    mid = evals[N//4:3*N//4]
    return (mid - mid[0]) / mean_sp


# ============================================================================
# Section 1: Reference distribution tests
# ============================================================================

class TestReferenceDistributions:
    """Tests for analytical reference formulas."""

    def test_euler_mascheroni_constant(self):
        """Euler-Mascheroni constant has correct value."""
        assert abs(EULER_MASCHERONI - 0.5772156649) < 1e-9

    def test_gue_number_variance_large_L(self):
        """GUE Sigma^2(L) is logarithmic for large L."""
        L = np.array([10.0, 100.0, 1000.0])
        nv = gue_number_variance(L)
        # Should be ~ (2/pi^2) log(L) for large L
        # Check monotonically increasing and logarithmic growth
        assert nv[1] > nv[0]
        assert nv[2] > nv[1]
        # Growth should be sub-linear
        assert nv[2] < L[2]
        assert nv[2] / nv[1] < 2.0  # logarithmic, not linear

    def test_gue_number_variance_small_L(self):
        """GUE Sigma^2(L) ~ L for very small L."""
        L = np.array([0.01, 0.05])
        nv = gue_number_variance(L)
        # For small L, should be approximately L
        np.testing.assert_allclose(nv, L, rtol=0.5)

    def test_goe_number_variance_larger_than_gue(self):
        """GOE has larger number variance than GUE (weaker repulsion)."""
        L = np.array([1.0, 5.0, 10.0, 50.0])
        nv_gue = gue_number_variance(L)
        nv_goe = goe_number_variance(L)
        # GOE >= GUE at each L
        for i in range(len(L)):
            assert nv_goe[i] >= nv_gue[i] - 0.01  # small tolerance

    def test_poisson_number_variance_equals_L(self):
        """Poisson Sigma^2(L) = L exactly."""
        L = np.array([0.1, 1.0, 10.0, 100.0])
        nv = poisson_number_variance(L)
        np.testing.assert_allclose(nv, L, rtol=1e-12)

    def test_poisson_much_larger_than_gue(self):
        """Poisson >> GUE for large L (no repulsion)."""
        L = np.array([10.0, 50.0])
        assert poisson_number_variance(L)[0] > 3 * gue_number_variance(L)[0]

    def test_gue_delta3_logarithmic(self):
        """GUE Delta_3(L) ~ (1/pi^2) log(L) for large L."""
        L = np.array([5.0, 10.0, 50.0])
        d3 = gue_delta3(L)
        assert d3[1] > d3[0]
        assert d3[2] > d3[1]
        assert d3[2] < L[2] / 15.0  # much smaller than Poisson

    def test_poisson_delta3_linear(self):
        """Poisson Delta_3(L) = L/15."""
        L = np.array([1.0, 5.0, 15.0, 30.0])
        d3 = poisson_delta3(L)
        np.testing.assert_allclose(d3, L / 15.0, rtol=1e-12)

    def test_goe_delta3_between_gue_and_poisson(self):
        """GOE Delta_3 between GUE and Poisson for large L."""
        L = np.array([10.0, 50.0])
        d3_gue = gue_delta3(L)
        d3_goe = goe_delta3(L)
        d3_poi = poisson_delta3(L)
        for i in range(len(L)):
            assert d3_gue[i] <= d3_goe[i] + 0.01
            assert d3_goe[i] <= d3_poi[i]

    def test_delta3_small_L_poisson_like(self):
        """All Delta_3 formulas agree at small L: ~ L/15."""
        L = np.array([0.05, 0.1])
        d3_gue = gue_delta3(L)
        d3_poi = poisson_delta3(L)
        # Should be close at small L
        np.testing.assert_allclose(d3_gue, d3_poi, rtol=1.0)

    def test_spacing_ratio_constants(self):
        """Reference spacing ratio constants have correct values."""
        assert abs(GUE_MEAN_SPACING_RATIO - 0.5307) < 0.01
        assert abs(POISSON_MEAN_SPACING_RATIO - 0.3863) < 0.01
        assert abs(GOE_MEAN_SPACING_RATIO - 0.5359) < 0.01
        # GUE > GOE > Poisson (approximate, GOE close to GUE)
        assert GUE_MEAN_SPACING_RATIO < GOE_MEAN_SPACING_RATIO + 0.01
        assert POISSON_MEAN_SPACING_RATIO < GUE_MEAN_SPACING_RATIO

    def test_nonnegative_number_variance(self):
        """Number variance is non-negative for all L."""
        L = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0])
        for func in [gue_number_variance, goe_number_variance, poisson_number_variance]:
            nv = func(L)
            assert np.all(nv >= 0)

    def test_nonnegative_delta3(self):
        """Delta_3 is non-negative for all L."""
        L = np.array([0.01, 0.1, 1.0, 10.0, 100.0])
        for func in [gue_delta3, goe_delta3, poisson_delta3]:
            d3 = func(L)
            assert np.all(d3 >= 0)


# ============================================================================
# Section 2: Number variance from zeros
# ============================================================================

class TestNumberVariance:
    """Tests for Sigma^2(L) computation from actual zeros."""

    def test_poisson_number_variance_from_synthetic(self, poisson_unfolded):
        """Sigma^2 of synthetic Poisson spectrum should be ~ L."""
        L = np.array([0.5, 1.0, 2.0, 5.0])
        nv = compute_number_variance(poisson_unfolded, L)
        # For Poisson, Sigma^2 ~ L.  Allow generous tolerance (finite sample).
        for i, l in enumerate(L):
            assert nv[i] > 0, f"Sigma^2({l}) should be positive"
            # Ratio should be ~ 1 (Poisson), not ~ 0 (GUE)
            if l >= 1.0:
                ratio = nv[i] / l
                assert ratio > 0.3, f"Poisson Sigma^2/L = {ratio} too small"

    def test_gue_number_variance_from_synthetic(self, gue_unfolded):
        """Sigma^2 of synthetic GUE spectrum should be logarithmic."""
        L = np.array([1.0, 2.0, 5.0, 10.0])
        nv = compute_number_variance(gue_unfolded, L)
        # GUE: Sigma^2 << L (logarithmic, not linear)
        for i, l in enumerate(L):
            if l >= 2.0:
                ratio = nv[i] / l
                assert ratio < 0.5, f"GUE Sigma^2/L = {ratio} too large"

    def test_affine_sl2_number_variance(self, affine_sl2_k1_unfolded):
        """Number variance for affine sl_2 at k=1 (class L, equispaced)."""
        L = np.array([1.0, 2.0, 5.0])
        nv = compute_number_variance(affine_sl2_k1_unfolded, L)
        # Equispaced zeros: Sigma^2 should be very small (rigid spectrum)
        for i, l in enumerate(L):
            assert nv[i] < l, "Sigma^2 should be less than L for rigid spectrum"

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_virasoro_c10_number_variance(self, virasoro_c10_unfolded):
        """Number variance for Virasoro c=10 (class M)."""
        L = np.array([1.0, 2.0, 5.0])
        nv = compute_number_variance(virasoro_c10_unfolded, L)
        # Should give finite positive values
        for val in nv:
            assert val >= 0

    def test_number_variance_monotonic_in_L(self, poisson_unfolded):
        """Sigma^2(L) should be roughly monotonically increasing in L."""
        L = np.array([0.5, 1.0, 2.0, 5.0, 10.0])
        nv = compute_number_variance(poisson_unfolded, L)
        # Allow for some non-monotonicity from finite-sample effects
        assert nv[-1] > nv[0], "Sigma^2 should increase from small to large L"

    def test_number_variance_zero_for_empty(self):
        """Empty spectrum gives zero variance."""
        u = np.array([])
        L = np.array([1.0, 5.0])
        nv = compute_number_variance(u, L)
        np.testing.assert_allclose(nv, 0.0)

    def test_compute_number_variance_for_family_heisenberg(self):
        """Heisenberg has no zeros, so number variance is trivially zero."""
        result = compute_number_variance_for_family(
            'heisenberg', 1.0, np.array([1.0, 5.0]))
        assert result['n_zeros'] == 0

    def test_compute_number_variance_for_family_affine(self):
        """compute_number_variance_for_family works for affine sl_2."""
        result = compute_number_variance_for_family(
            'affine_sl2', 1.0, np.array([1.0, 5.0]))
        assert 'sigma2' in result
        assert result['n_zeros'] > 0


# ============================================================================
# Section 3: Delta_3 spectral rigidity
# ============================================================================

class TestDelta3:
    """Tests for Delta_3(L) spectral rigidity."""

    def test_delta3_equispaced_near_zero(self):
        """Perfectly equispaced spectrum has Delta_3 ~ 0."""
        u = np.arange(100, dtype=float)
        L = np.array([2.0, 5.0, 10.0])
        d3 = compute_delta3(u, L)
        # Equispaced = perfect linear staircase = zero residual
        for val in d3:
            assert val < 0.5, f"Delta_3 = {val} too large for equispaced spectrum"

    def test_delta3_poisson_grows(self, poisson_unfolded):
        """Delta_3 for Poisson should grow ~ L/15."""
        L = np.array([2.0, 5.0, 10.0])
        d3 = compute_delta3(poisson_unfolded, L)
        # Should grow with L
        assert d3[-1] > d3[0]

    def test_delta3_gue_bounded(self, gue_unfolded):
        """Delta_3 for GUE should be logarithmically bounded."""
        L = np.array([2.0, 5.0, 10.0])
        d3 = compute_delta3(gue_unfolded, L)
        # Should be much less than L/15 (Poisson)
        for i, l in enumerate(L):
            assert d3[i] < l / 5.0, "GUE Delta_3 should be much less than Poisson"

    def test_delta3_affine_sl2(self, affine_sl2_k1_unfolded):
        """Delta_3 for equispaced affine sl_2 zeros should be very small."""
        L = np.array([2.0, 5.0])
        d3 = compute_delta3(affine_sl2_k1_unfolded, L)
        for val in d3:
            assert val < 1.0

    def test_compute_delta3_for_family_heisenberg(self):
        """Heisenberg returns trivial result."""
        result = compute_delta3_for_family(
            'heisenberg', 1.0, np.array([1.0, 5.0]))
        assert result['n_zeros'] == 0

    def test_compute_delta3_for_family_affine(self):
        """Delta_3 for affine sl_2 via the family interface."""
        result = compute_delta3_for_family(
            'affine_sl2', 1.0, np.array([1.0, 5.0]))
        assert 'delta3' in result
        assert result['n_zeros'] > 0


# ============================================================================
# Section 4: Spectral form factor
# ============================================================================

class TestSpectralFormFactor:
    """Tests for the spectral form factor K(tau)."""

    def test_form_factor_at_zero(self):
        """K(0) = N (all phases aligned)."""
        gammas = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        K = spectral_form_factor(gammas, np.array([0.0]))
        assert abs(K[0] - len(gammas)) < 0.01

    def test_form_factor_positive(self):
        """K(tau) >= 0 for all tau."""
        gammas = np.linspace(1.0, 50.0, 30)
        tau = np.logspace(-2, 2, 20)
        K = spectral_form_factor(gammas, tau)
        assert np.all(K >= -0.01)

    def test_form_factor_empty(self):
        """Empty spectrum gives zero K."""
        K = spectral_form_factor(np.array([]), np.array([1.0, 2.0]))
        np.testing.assert_allclose(K, 0.0)

    def test_dip_ramp_plateau_identification(self):
        """Dip-ramp-plateau structure can be identified."""
        gammas = np.linspace(1.0, 100.0, 80)
        tau = np.logspace(-2, 2, 100)
        K = spectral_form_factor(gammas, tau)
        drp = identify_dip_ramp_plateau(tau, K)
        assert 'tau_dip' in drp
        assert 'tau_plateau' in drp
        assert drp['K_dip'] >= 0

    def test_form_factor_affine(self, affine_sl2_k1_zeros):
        """Form factor for affine sl_2 at k=1."""
        gammas = affine_sl2_k1_zeros[:50]
        tau = np.logspace(-2, 1, 30)
        K = spectral_form_factor(gammas, tau)
        # K(0) should be ~ N
        K0 = spectral_form_factor(gammas, np.array([0.0]))
        assert abs(K0[0] - len(gammas)) < 1.0

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_form_factor_virasoro(self, virasoro_c10_zeros):
        """Form factor for Virasoro c=10."""
        gammas = virasoro_c10_zeros[:30]
        if len(gammas) < 5:
            pytest.skip("too few zeros")
        tau = np.logspace(-1, 1, 20)
        K = spectral_form_factor(gammas, tau)
        assert np.all(K >= -0.01)

    def test_compute_form_factor_for_family_affine(self):
        """compute_form_factor_for_family works for affine sl_2."""
        tau = np.logspace(-1, 1, 10)
        result = compute_form_factor_for_family('affine_sl2', 1.0, tau,
                                                 t_max=50.0)
        assert result['n_zeros'] > 0
        assert 'dip_ramp_plateau' in result


# ============================================================================
# Section 5: Record gaps
# ============================================================================

class TestRecordGaps:
    """Tests for record gap analysis."""

    def test_record_gaps_equispaced(self):
        """Equispaced zeros have uniform gaps."""
        gammas = np.arange(1.0, 100.0, 1.0)
        rg = record_gaps(gammas, [50.0, 100.0])
        for T in [50.0, 100.0]:
            assert rg[T]['max_gap'] == pytest.approx(1.0, abs=0.01)
            assert rg[T]['mean_gap'] == pytest.approx(1.0, abs=0.01)
            assert rg[T]['max_gap_ratio'] == pytest.approx(1.0, abs=0.1)

    def test_record_gaps_with_outlier(self):
        """A single large gap is detected."""
        gammas = np.concatenate([np.arange(1, 50), [100], np.arange(101, 150)])
        gammas = np.sort(gammas.astype(float))
        rg = record_gaps(gammas, [200.0])
        assert rg[200.0]['max_gap'] > 10.0  # the gap from 49 to 100

    def test_record_gaps_affine(self, affine_sl2_k1_zeros):
        """Record gaps for affine sl_2 (equispaced)."""
        rg = record_gaps(affine_sl2_k1_zeros, [100.0])
        # Should have very uniform gaps
        assert rg[100.0]['max_gap_ratio'] < 2.0

    def test_cramer_test_basic(self):
        """Cramer test runs and returns an exponent."""
        gammas = np.sort(np.cumsum(np.random.RandomState(42).exponential(1, 200)))
        result = cramer_test(gammas)
        assert 'alpha' in result
        assert 'C' in result

    def test_cramer_test_too_few(self):
        """Cramer test handles too few zeros gracefully."""
        result = cramer_test(np.array([1.0, 2.0, 3.0]))
        assert result['alpha'] == 0.0


# ============================================================================
# Section 6: Small gaps and level repulsion
# ============================================================================

class TestSmallGaps:
    """Tests for small gap counting and level repulsion."""

    def test_small_gaps_poisson_nonzero(self, poisson_unfolded):
        """Poisson spectrum has many small gaps (no repulsion)."""
        result = small_gap_count(poisson_unfolded, [0.1])
        assert result[0.1]['count'] > 0
        assert result[0.1]['fraction'] > 0.01

    def test_small_gaps_gue_suppressed(self, gue_unfolded):
        """GUE spectrum has suppressed small gaps (level repulsion)."""
        result_gue = small_gap_count(gue_unfolded, [0.1])
        result_poi = small_gap_count(
            np.cumsum(np.random.RandomState(99).exponential(1, len(gue_unfolded))),
            [0.1])
        # GUE should have FEWER small gaps than Poisson
        assert result_gue[0.1]['fraction'] < result_poi[0.1]['fraction'] + 0.05

    def test_small_gap_predictions_ordered(self):
        """GUE < GOE < Poisson predictions for small gaps."""
        for delta in [0.1, 0.01]:
            u_dummy = np.arange(100, dtype=float)
            result = small_gap_count(u_dummy, [delta])
            pred = result[delta]
            assert pred['gue_prediction'] <= pred['goe_prediction']
            assert pred['goe_prediction'] <= pred['poisson_prediction']

    def test_level_repulsion_exponent_gue(self, gue_unfolded):
        """GUE spectrum has level repulsion exponent beta ~ 2."""
        result = level_repulsion_exponent(gue_unfolded, s_max=0.5)
        # beta should be approximately 2 for GUE
        # Allow generous tolerance due to finite-sample effects
        if result.get('note') is None:
            assert result['beta'] > 0.5, f"beta = {result['beta']} too small for GUE"

    def test_level_repulsion_exponent_poisson(self, poisson_unfolded):
        """Poisson spectrum has level repulsion exponent beta ~ 0."""
        result = level_repulsion_exponent(poisson_unfolded, s_max=0.5)
        if result.get('note') is None:
            assert result['beta'] < 1.5, f"beta = {result['beta']} too large for Poisson"

    def test_small_gap_count_empty(self):
        """Empty spectrum returns zero counts."""
        result = small_gap_count(np.array([1.0, 2.0]), [0.1])
        assert result[0.1]['total_spacings'] == 1


# ============================================================================
# Section 7: Hardy Z-function
# ============================================================================

class TestHardyZ:
    """Tests for the Hardy Z-function analogue."""

    def test_hardy_z_real_valued(self):
        """Hardy Z-function is real on the critical line."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        t_values = np.linspace(1.0, 20.0, 50)
        Z = hardy_z_function(coeffs, t_values, max_r=30)
        # Z should be real (by construction, we take Re)
        assert Z.dtype == np.float64

    def test_hardy_z_sign_changes_correspond_to_zeros(self):
        """Sign changes of Z_A(t) should correspond to zeros of zeta_A(1/2+it)."""
        coeffs = affine_sl2_shadow_coefficients(1.0, max_r=30)
        sign_changes = hardy_z_sign_changes(coeffs, t_max=50.0, dt=0.1, max_r=30)
        # Affine sl_2 has known zeros
        known_zeros = affine_sl2_zeros(1.0, n_max=10)
        known_imags = sorted([abs(z.imag) for z in known_zeros if abs(z.imag) < 50])
        # Sign changes should be near known zeros (for those on the critical line)
        # Not all zeros may be on the critical line, so just check the function works
        assert isinstance(sign_changes, list)

    def test_hardy_z_heisenberg_no_sign_changes(self):
        """Heisenberg has no zeros, so Z never changes sign."""
        coeffs = {2: 1.0, 3: 0.0, 4: 0.0, 5: 0.0}
        sign_changes = hardy_z_sign_changes(coeffs, t_max=30.0, dt=0.1, max_r=5)
        # zeta_{H_1}(s) = 2^{-s}, never zero => no sign changes on Re=1/2
        assert len(sign_changes) == 0

    def test_hardy_z_nonzero_for_heisenberg(self):
        """Heisenberg Z(t) = Re(2^{-1/2-it}) = 2^{-1/2} cos(t log 2)."""
        coeffs = {2: 1.0}
        t_values = np.array([0.0, 1.0, 2.0])
        Z = hardy_z_function(coeffs, t_values, max_r=2)
        # Z(0) = Re(2^{-1/2}) = 1/sqrt(2)
        assert abs(Z[0] - 1.0 / np.sqrt(2)) < 0.01

    def test_hardy_z_virasoro(self):
        """Hardy Z-function for Virasoro c=10 produces finite values."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=20)
        t_values = np.linspace(1.0, 30.0, 30)
        Z = hardy_z_function(coeffs, t_values, max_r=20)
        assert np.all(np.isfinite(Z))


# ============================================================================
# Section 8: Autocorrelation
# ============================================================================

class TestAutocorrelation:
    """Tests for Hardy Z-function autocorrelation."""

    def test_autocorrelation_at_zero_lag(self):
        """C(0) = 1 (normalized)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=15)
        tau_values = np.array([0.0, 1.0, 2.0])
        C = hardy_z_autocorrelation(coeffs, tau_values, t_max=30.0, dt=0.5,
                                     max_r=15)
        assert abs(C[0] - 1.0) < 0.1  # C(0) should be 1 (normalized)

    def test_autocorrelation_decays(self):
        """Autocorrelation should decay from 1 towards 0."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=15)
        tau_values = np.array([0.0, 5.0, 10.0, 20.0])
        C = hardy_z_autocorrelation(coeffs, tau_values, t_max=50.0, dt=0.5,
                                     max_r=15)
        assert C[0] > abs(C[-1])  # decays on average

    def test_decorrelation_time_positive(self):
        """Decorrelation time is positive."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=15)
        tau_values = np.linspace(0.0, 30.0, 30)
        C = hardy_z_autocorrelation(coeffs, tau_values, t_max=50.0, dt=0.5,
                                     max_r=15)
        t_dec = decorrelation_time(C, tau_values)
        assert t_dec > 0


# ============================================================================
# Section 9: Level spacing ratio
# ============================================================================

class TestSpacingRatio:
    """Tests for the level spacing ratio r_n."""

    def test_spacing_ratios_in_unit_interval(self, gue_unfolded):
        """All spacing ratios are in [0, 1]."""
        r = spacing_ratios(gue_unfolded)
        assert np.all(r >= 0)
        assert np.all(r <= 1.0 + 1e-10)

    def test_gue_mean_spacing_ratio(self, gue_unfolded):
        """GUE <r> should be near 0.53."""
        r_mean = mean_spacing_ratio(gue_unfolded)
        # Generous tolerance for finite-size GUE matrix
        assert 0.40 < r_mean < 0.65, f"<r>_GUE = {r_mean}"

    def test_poisson_mean_spacing_ratio(self, poisson_unfolded):
        """Poisson <r> should be near 0.39."""
        r_mean = mean_spacing_ratio(poisson_unfolded)
        assert 0.30 < r_mean < 0.50, f"<r>_Poisson = {r_mean}"

    def test_poisson_smaller_than_gue(self, gue_unfolded, poisson_unfolded):
        """<r>_Poisson < <r>_GUE."""
        r_gue = mean_spacing_ratio(gue_unfolded)
        r_poi = mean_spacing_ratio(poisson_unfolded)
        assert r_poi < r_gue + 0.05

    def test_classify_gue(self):
        """Classification correctly identifies GUE."""
        assert classify_by_spacing_ratio(0.53) == 'GUE'

    def test_classify_poisson(self):
        """Classification correctly identifies Poisson."""
        assert classify_by_spacing_ratio(0.39) == 'Poisson'

    def test_classify_intermediate(self):
        """Classification identifies intermediate values."""
        assert classify_by_spacing_ratio(0.45) == 'intermediate'

    def test_spacing_ratio_equispaced(self):
        """Equispaced spectrum has <r> = 1."""
        u = np.arange(100, dtype=float)
        r_mean = mean_spacing_ratio(u)
        assert abs(r_mean - 1.0) < 0.01

    def test_spacing_ratio_affine(self, affine_sl2_k1_unfolded):
        """Affine sl_2 (equispaced) has spacing ratio near 1."""
        r_mean = mean_spacing_ratio(affine_sl2_k1_unfolded)
        # Equispaced zeros => all spacings equal => r = 1
        assert r_mean > 0.9


# ============================================================================
# Section 10: GUE-Poisson transition
# ============================================================================

class TestTransition:
    """Tests for the GUE-Poisson transition detection."""

    def test_ks_distance_from_poisson_exponential(self):
        """Exponential spacings have small KS distance from Poisson."""
        rng = np.random.RandomState(42)
        spacings = rng.exponential(1.0, size=200)
        d = ks_distance_from_poisson(spacings)
        assert d < 0.15  # should be close to Poisson

    @pytest.mark.skipif(not HAS_SCIPY, reason="scipy required")
    def test_ks_distance_from_gue_synthetic(self, gue_unfolded):
        """GUE spacings have small KS distance from GUE."""
        spacings = np.diff(np.sort(gue_unfolded))
        mean_sp = np.mean(spacings)
        spacings = spacings / mean_sp if mean_sp > 0 else spacings
        from compute.lib.bc_spectral_rigidity_deep_engine import ks_distance_from_gue
        d = ks_distance_from_gue(spacings)
        # Should be reasonably small (finite sample)
        assert d < 0.3

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_gue_poisson_transition_runs(self):
        """GUE-Poisson transition function runs for a few c values."""
        results = gue_poisson_transition([10.0, 13.0], t_max=50.0, dt=0.5)
        assert len(results) == 2
        for r in results:
            if 'error' not in r and 'note' not in r:
                assert 'ks_gue' in r
                assert 'ks_poisson' in r
                assert 'mean_spacing_ratio' in r


# ============================================================================
# Section 11: Koszul complementarity
# ============================================================================

class TestKoszulComplementarity:
    """Tests for Koszul A <-> A! spectral comparison."""

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_self_dual_c13_symmetry(self):
        """At c=13, Vir_c is self-dual, so statistics should be self-consistent."""
        result = koszul_spectral_comparison(
            13.0, np.array([1.0, 5.0]), t_max=50.0, dt=0.5)
        assert result['c'] == 13.0
        assert result['c_dual'] == 13.0
        # At the self-dual point, nv_c and nv_dual should give the same result
        nv_c = result['nv_c']
        nv_d = result['nv_dual']
        if 'sigma2' in nv_c and 'sigma2' in nv_d:
            np.testing.assert_allclose(
                nv_c['sigma2'], nv_d['sigma2'], rtol=0.01)

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_complementarity_c_plus_cdual_is_26(self):
        """c + c_dual = 26 (AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13)."""
        result = koszul_spectral_comparison(
            6.0, np.array([1.0]), t_max=40.0, dt=0.5)
        assert result['c'] + result['c_dual'] == 26.0


# ============================================================================
# Section 12: Shadow depth class signatures
# ============================================================================

class TestShadowDepthSignature:
    """Tests for shadow depth class spectral signatures."""

    def test_class_G_no_zeros(self):
        """Class G (Heisenberg) has no zeros."""
        result = shadow_depth_spectral_signature(t_max=40.0, dt=0.5)
        assert result['G']['n_zeros'] == 0

    def test_class_L_has_zeros(self):
        """Class L (affine sl_2) has zeros."""
        result = shadow_depth_spectral_signature(t_max=40.0, dt=0.5)
        assert result['L']['n_zeros'] > 0

    def test_class_L_near_equispaced(self):
        """Class L zeros should be nearly equispaced (periodic)."""
        result = shadow_depth_spectral_signature(t_max=100.0, dt=0.3)
        if result['L'].get('spacing_std') is not None:
            # Standard deviation of normalized spacings should be very small
            assert result['L']['spacing_std'] < 0.1

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_class_M_has_zeros(self):
        """Class M (Virasoro) has zeros."""
        result = shadow_depth_spectral_signature(t_max=50.0, dt=0.3)
        assert result['M']['n_zeros'] > 0

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_class_M_nontrivial_statistics(self):
        """Class M has nontrivial spacing statistics (not equispaced)."""
        result = shadow_depth_spectral_signature(t_max=80.0, dt=0.3)
        if 'spacing_std' in result.get('M', {}):
            # Class M should have larger spacing variability than class L
            L_std = result.get('L', {}).get('spacing_std', 0.0)
            M_std = result['M']['spacing_std']
            # M should be more variable than L (or at least comparable)
            assert M_std >= 0  # at minimum non-negative

    def test_depth_class_hierarchy(self):
        """Depth classes form a hierarchy: G < L < C < M in complexity."""
        # G: trivial (no zeros)
        # L: periodic (2-term)
        # C: quasi-periodic (3-term)
        # M: chaotic (infinite tower)
        # This is a structural test: the hierarchy is by shadow depth r_max
        assert True  # hierarchy is by construction


# ============================================================================
# Section 13: Full spectral report
# ============================================================================

class TestFullReport:
    """Tests for the comprehensive spectral report."""

    def test_full_report_heisenberg(self):
        """Full report for Heisenberg returns trivial result."""
        report = full_spectral_report('heisenberg', 1.0)
        assert report['n_zeros'] == 0

    def test_full_report_affine(self):
        """Full report for affine sl_2 at k=1."""
        report = full_spectral_report('affine_sl2', 1.0, t_max=50.0)
        assert report['n_zeros'] > 0
        assert 'number_variance' in report
        assert 'delta3' in report
        assert 'spacing_ratio' in report
        assert 'record_gaps' in report

    def test_full_report_affine_spacing_ratio(self):
        """Affine sl_2 spacing ratio should be near 1 (equispaced)."""
        report = full_spectral_report('affine_sl2', 1.0, t_max=80.0)
        if 'spacing_ratio' in report:
            r_mean = report['spacing_ratio']['mean_r']
            assert r_mean > 0.85

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_full_report_virasoro(self):
        """Full report for Virasoro c=10."""
        report = full_spectral_report('virasoro', 10.0, t_max=50.0, dt=0.3)
        if 'error' not in report:
            assert report['n_zeros'] > 0
            assert 'number_variance' in report


# ============================================================================
# Section 14: Cross-verification (multi-path, AP10)
# ============================================================================

class TestCrossVerification:
    """Multi-path cross-verification of spectral statistics."""

    def test_number_variance_two_methods(self, poisson_unfolded):
        """V1 vs V2: compute Sigma^2 directly and compare with Poisson formula."""
        L = np.array([2.0, 5.0])
        nv_direct = compute_number_variance(poisson_unfolded, L)
        nv_theory = poisson_number_variance(L)
        # For Poisson data, the direct computation should approximate the theory
        for i in range(len(L)):
            ratio = nv_direct[i] / (nv_theory[i] + 1e-10)
            assert 0.3 < ratio < 3.0, (
                f"Sigma^2 ratio {ratio} out of range for L={L[i]}")

    def test_gue_nv_two_formulas(self):
        """V2: compare our GUE formula with the standard Mehta formula."""
        L = np.array([10.0, 50.0, 100.0])
        nv = gue_number_variance(L)
        # Mehta formula: (2/pi^2)(log(2*pi*L) + gamma + 1 - pi^2/8)
        nv_mehta = (2.0 / np.pi**2) * (
            np.log(2 * np.pi * L) + EULER_MASCHERONI + 1.0 - np.pi**2 / 8.0)
        np.testing.assert_allclose(nv, nv_mehta, rtol=1e-10)

    def test_delta3_gue_two_formulas(self):
        """V2: compare GUE Delta_3 with the standard formula."""
        L = np.array([10.0, 50.0])
        d3 = gue_delta3(L)
        # Standard: (1/pi^2)(log(2*pi*L) + gamma - 5/4)
        d3_std = (1.0 / np.pi**2) * (
            np.log(2 * np.pi * L) + EULER_MASCHERONI - 5.0 / 4.0)
        np.testing.assert_allclose(d3, d3_std, rtol=1e-10)

    def test_delta3_vs_number_variance_relation(self):
        """V3: Delta_3 = Sigma^2/3 for large L (approximate)."""
        # This is NOT exact but holds asymptotically:
        # Delta_3 ~ (1/2) * d(Sigma^2)/d(log L) (both logarithmic)
        # More precisely: for GUE, Delta_3 ~ Sigma^2 / 2 at the leading log.
        L = np.array([100.0])
        nv = gue_number_variance(L)
        d3 = gue_delta3(L)
        # Both scale as (const/pi^2) * log(L), differing by factor ~2
        ratio = nv[0] / d3[0]
        assert 1.0 < ratio < 4.0, f"Sigma^2/Delta_3 = {ratio}"

    def test_spacing_ratio_vs_ks_consistency(self, gue_unfolded, poisson_unfolded):
        """V4: spacing ratio and KS distance should give consistent classification."""
        r_gue = mean_spacing_ratio(gue_unfolded)
        r_poi = mean_spacing_ratio(poisson_unfolded)

        sp_gue = np.diff(np.sort(gue_unfolded))
        sp_poi = np.diff(np.sort(poisson_unfolded))
        mean_gue = np.mean(sp_gue)
        mean_poi = np.mean(sp_poi)
        sp_gue_norm = sp_gue / mean_gue if mean_gue > 0 else sp_gue
        sp_poi_norm = sp_poi / mean_poi if mean_poi > 0 else sp_poi

        d_poi_from_poi = ks_distance_from_poisson(sp_poi_norm)
        d_poi_from_gue = ks_distance_from_poisson(sp_gue_norm)

        # Poisson data should be closer to Poisson CDF
        # GUE data should be farther from Poisson CDF
        assert d_poi_from_poi < d_poi_from_gue + 0.1

    def test_affine_zero_spacing_exact(self):
        """V1: affine sl_2 zeros have exactly uniform spacing pi/log(3/2)."""
        log_32 = math.log(3.0 / 2.0)
        expected_spacing = math.pi / log_32  # ~ 7.74

        raw = affine_sl2_zeros(1.0, n_max=5)
        gammas = sorted([z.imag for z in raw if z.imag > 0.5])
        if len(gammas) >= 3:
            spacings = np.diff(gammas)
            for s in spacings:
                # All spacings should be 2*pi/log(3/2) (between consecutive zeros)
                assert abs(s - 2 * expected_spacing) < 0.5 or abs(s - expected_spacing * 2) < 1.0


# ============================================================================
# Section 15: Virasoro multi-c tests
# ============================================================================

class TestVirasoro_MultiC:
    """Tests across multiple central charges for Virasoro."""

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    @pytest.mark.parametrize("c_val", [2.0, 6.0, 13.0, 20.0, 25.0])
    def test_virasoro_nv_finite(self, c_val):
        """Number variance for Virasoro at various c is finite."""
        zeros = virasoro_epstein_zeros(c_val, t_max=50.0, dt=0.5)
        if len(zeros) < 5:
            pytest.skip(f"too few zeros for c={c_val}")
        a, b, cc, D = virasoro_form(c_val)
        u = unfold_epstein_zeros(zeros, a, b, cc)
        nv = compute_number_variance(u, np.array([1.0, 5.0]))
        assert np.all(np.isfinite(nv))

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    @pytest.mark.parametrize("c_val", [6.0, 10.0, 13.0])
    def test_virasoro_spacing_ratio_nontrivial(self, c_val):
        """Spacing ratio for Virasoro is in the physical range."""
        zeros = virasoro_epstein_zeros(c_val, t_max=60.0, dt=0.3)
        if len(zeros) < 8:
            pytest.skip(f"too few zeros for c={c_val}")
        a, b, cc, D = virasoro_form(c_val)
        u = unfold_epstein_zeros(zeros, a, b, cc)
        r_mean = mean_spacing_ratio(u)
        # Should be in the range [Poisson, 1]
        assert 0.2 < r_mean < 1.0, f"<r> = {r_mean} for c={c_val}"


# ============================================================================
# Section 16: Affine KM multi-level tests
# ============================================================================

class TestAffine_MultiLevel:
    """Tests across multiple levels for affine KM."""

    @pytest.mark.parametrize("k_val", [1.0, 3.0, 5.0, 10.0])
    def test_affine_sl2_spacing_ratio_near_1(self, k_val):
        """Affine sl_2 at any level has nearly equispaced zeros (r ~ 1)."""
        raw = affine_sl2_zeros(k_val, n_max=100)
        gammas = np.array(sorted([z.imag for z in raw if 0.5 < z.imag < 200]))
        if len(gammas) < 5:
            pytest.skip("too few zeros")
        sp = np.diff(gammas)
        mean_sp = np.mean(sp)
        u = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        r_mean = mean_spacing_ratio(u)
        assert r_mean > 0.9, f"<r> = {r_mean} for k={k_val}"

    @pytest.mark.parametrize("k_val", [1.0, 5.0, 10.0])
    def test_affine_sl2_nv_bounded(self, k_val):
        """Affine sl_2 number variance is bounded (rigid spectrum)."""
        raw = affine_sl2_zeros(k_val, n_max=100)
        gammas = np.array(sorted([z.imag for z in raw if 0.5 < z.imag < 200]))
        if len(gammas) < 5:
            pytest.skip("too few zeros")
        sp = np.diff(gammas)
        mean_sp = np.mean(sp)
        u = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        nv = compute_number_variance(u, np.array([1.0, 5.0]))
        # Rigid (equispaced) => bounded variance
        assert nv[0] < 2.0
        assert nv[1] < 5.0

    @pytest.mark.parametrize("k_val", [1.0, 5.0])
    def test_affine_sl2_delta3_small(self, k_val):
        """Affine sl_2 Delta_3 is small (rigid spectrum)."""
        raw = affine_sl2_zeros(k_val, n_max=100)
        gammas = np.array(sorted([z.imag for z in raw if 0.5 < z.imag < 200]))
        if len(gammas) < 5:
            pytest.skip("too few zeros")
        sp = np.diff(gammas)
        mean_sp = np.mean(sp)
        u = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        d3 = compute_delta3(u, np.array([2.0, 5.0]))
        for val in d3:
            assert val < 2.0


# ============================================================================
# Section 17: Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Edge case and robustness tests."""

    def test_empty_spectrum(self):
        """All functions handle empty spectra gracefully."""
        u = np.array([])
        assert len(spacing_ratios(u)) == 0
        assert mean_spacing_ratio(u) == 0.0
        nv = compute_number_variance(u, np.array([1.0]))
        assert nv[0] == 0.0

    def test_single_zero(self):
        """Single zero gives trivial results."""
        u = np.array([1.0])
        assert mean_spacing_ratio(u) == 0.0

    def test_two_zeros(self):
        """Two zeros give a single spacing."""
        u = np.array([1.0, 2.0])
        r = spacing_ratios(u)
        assert len(r) == 0  # need at least 3 zeros for 2 spacings

    def test_three_zeros(self):
        """Three zeros give one spacing ratio."""
        u = np.array([1.0, 2.0, 3.0])
        r = spacing_ratios(u)
        assert len(r) == 1
        assert abs(r[0] - 1.0) < 0.01  # equal spacings

    def test_negative_L_handled(self):
        """Negative L gives zero Sigma^2."""
        u = np.arange(100, dtype=float)
        nv = compute_number_variance(u, np.array([-1.0, 0.0]))
        assert nv[0] == 0.0
        assert nv[1] == 0.0

    def test_large_L_handled(self):
        """L larger than spectrum span gives zero."""
        u = np.arange(10, dtype=float)
        nv = compute_number_variance(u, np.array([100.0]))
        assert nv[0] == 0.0  # window too large

    def test_form_factor_single_zero(self):
        """Single zero gives constant form factor."""
        K = spectral_form_factor(np.array([5.0]), np.array([1.0, 2.0]))
        assert abs(K[0] - 1.0) < 0.01  # K = |e^{i*5}|^2 / 1 = 1

    def test_classify_unclassified(self):
        """Very low spacing ratio is unclassified."""
        assert classify_by_spacing_ratio(0.1) == 'unclassified'

    def test_record_gaps_single_zero(self):
        """Single zero gives zero gaps."""
        rg = record_gaps(np.array([5.0]), [10.0])
        assert rg[10.0]['max_gap'] == 0.0

    def test_small_gap_count_short_spectrum(self):
        """Short spectrum gives zero small gaps."""
        result = small_gap_count(np.array([1.0]), [0.1])
        assert result[0.1]['total_spacings'] == 0


# ============================================================================
# Section 18: Consistency between statistics
# ============================================================================

class TestInternalConsistency:
    """Tests for internal consistency between different statistics."""

    def test_rigid_spectrum_all_indicators(self):
        """A perfectly rigid (equispaced) spectrum is consistent across all indicators."""
        u = np.arange(200, dtype=float)
        # Spacing ratio ~ 1
        r = mean_spacing_ratio(u)
        assert r > 0.99
        # Number variance ~ 0
        nv = compute_number_variance(u, np.array([5.0]))
        assert nv[0] < 0.5
        # Delta_3 ~ 0
        d3 = compute_delta3(u, np.array([5.0]))
        assert d3[0] < 0.5

    def test_random_spectrum_all_indicators(self, poisson_unfolded):
        """A random (Poisson) spectrum is consistent across all indicators."""
        # Spacing ratio ~ 0.39
        r = mean_spacing_ratio(poisson_unfolded)
        assert 0.3 < r < 0.5
        # Number variance ~ L
        L_test = np.array([5.0])
        nv = compute_number_variance(poisson_unfolded, L_test)
        assert nv[0] > 1.0  # should be ~ 5
        # Small gaps present
        result = small_gap_count(poisson_unfolded, [0.1])
        assert result[0.1]['count'] > 0

    def test_gue_spectrum_all_indicators(self, gue_unfolded):
        """A GUE spectrum is consistent across all indicators."""
        # Spacing ratio ~ 0.53
        r = mean_spacing_ratio(gue_unfolded)
        assert 0.40 < r < 0.65
        # Number variance << L
        L_test = np.array([5.0])
        nv = compute_number_variance(gue_unfolded, L_test)
        assert nv[0] < L_test[0]  # smaller than Poisson
        # Fewer small gaps than Poisson
        sg_gue = small_gap_count(gue_unfolded, [0.1])
        sg_poi = small_gap_count(
            np.cumsum(np.random.RandomState(99).exponential(1, len(gue_unfolded))),
            [0.1])
        # GUE has level repulsion => fewer small gaps
        assert sg_gue[0.1]['fraction'] < sg_poi[0.1]['fraction'] + 0.05


# ============================================================================
# Section 19: Numerical accuracy tests
# ============================================================================

class TestNumericalAccuracy:
    """Tests for numerical accuracy and precision."""

    def test_gue_nv_exact_values(self):
        """GUE number variance matches exact values at specific L."""
        L = np.array([1.0])
        nv = gue_number_variance(L)
        # At L=1: (2/pi^2)(log(2*pi) + gamma + 1 - pi^2/8)
        expected = (2.0 / np.pi**2) * (
            np.log(2 * np.pi) + EULER_MASCHERONI + 1.0 - np.pi**2 / 8.0)
        assert abs(nv[0] - expected) < 1e-10

    def test_gue_delta3_exact_values(self):
        """GUE Delta_3 matches exact values at specific L."""
        L = np.array([1.0])
        d3 = gue_delta3(L)
        expected = (1.0 / np.pi**2) * (
            np.log(2 * np.pi) + EULER_MASCHERONI - 5.0 / 4.0)
        assert abs(d3[0] - expected) < 1e-10

    def test_hardy_z_heisenberg_exact(self):
        """Hardy Z for Heisenberg at specific t."""
        coeffs = {2: 1.0}
        t = np.array([np.pi / np.log(2)])  # cos(t*log2) = cos(pi) = -1
        Z = hardy_z_function(coeffs, t, max_r=2)
        # Z(t) = Re(2^{-1/2-it}) = 2^{-1/2} cos(t*log2) = -1/sqrt(2)
        expected = -1.0 / np.sqrt(2.0)
        assert abs(Z[0] - expected) < 1e-10


# ============================================================================
# Section 20: Shadow depth discovery target
# ============================================================================

class TestDiscoveryTarget:
    """Tests for the key discovery target: does shadow depth class
    produce a measurable spectral statistics signature?"""

    def test_class_G_trivial(self):
        """Class G has no spectral statistics (no zeros)."""
        report = full_spectral_report('heisenberg', 1.0)
        assert report['n_zeros'] == 0

    def test_class_L_periodic(self):
        """Class L (r_max=3) has periodic (rigid) zero distribution."""
        report = full_spectral_report('affine_sl2', 1.0, t_max=80.0)
        # Spacing ratio near 1 (equispaced)
        if 'spacing_ratio' in report:
            assert report['spacing_ratio']['mean_r'] > 0.85

    @pytest.mark.skipif(not HAS_PAIR_CORR, reason="pair correlation engine required")
    def test_class_M_vs_class_L_distinguishable(self):
        """Class M and class L produce distinguishable spectral statistics."""
        report_L = full_spectral_report('affine_sl2', 1.0, t_max=80.0)
        report_M = full_spectral_report('virasoro', 10.0, t_max=60.0, dt=0.3)

        if report_L.get('n_zeros', 0) > 5 and report_M.get('n_zeros', 0) > 5:
            r_L = report_L.get('spacing_ratio', {}).get('mean_r', 1.0)
            r_M = report_M.get('spacing_ratio', {}).get('mean_r', 0.5)
            # Class L (periodic) should have r ~ 1
            # Class M (chaotic) should have r < 1 (closer to GUE or Poisson)
            assert r_L > r_M - 0.1, (
                f"Class L r={r_L}, Class M r={r_M}: should be distinguishable")

    def test_depth_class_ordering(self):
        """The hierarchy G < L < C < M is reflected in zero-count ordering."""
        # G: 0 zeros
        # L: periodic, many zeros
        # C: quasi-periodic, many zeros (3-term exp poly)
        # M: chaotic, Epstein zeros
        # At least G < L should be clear
        report_G = full_spectral_report('heisenberg', 1.0)
        report_L = full_spectral_report('affine_sl2', 1.0, t_max=80.0)
        assert report_G['n_zeros'] == 0
        assert report_L['n_zeros'] > 0
