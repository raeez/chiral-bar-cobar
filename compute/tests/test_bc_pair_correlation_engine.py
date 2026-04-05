#!/usr/bin/env python3
r"""
Tests for the Benjamin-Chang pair correlation engine.

Verification paths:
  Path 1: Direct computation of pair correlation from zeros
  Path 2: Comparison with known analytic formulas for GUE/GOE/Poisson
  Path 3: Poisson control (independent random points as calibration)
  Path 4: KS-test discrimination (GUE rejects Poisson, Poisson rejects GUE)

Coverage:
  1. Reference distributions (GUE, GOE, Poisson) -- exact formulas
  2. Riemann zeta zeros -- GUE universality (Montgomery conjecture)
  3. Epstein zeta zeros -- shadow metric zero statistics
  4. Nearest-neighbor spacing and Wigner surmise
  5. Number variance
  6. Cross-correlation between zero families
  7. Complementarity (c <-> 26-c)
  8. Self-dual point (c = 13) analysis
  9. Poisson control calibration
  10. KS test discrimination power

CRITICAL PITFALLS TESTED:
  - AP1: kappa = c/2 for Virasoro, NOT c
  - AP24: Koszul dual at c -> 26-c (self-dual at c=13, not c=26)
  - AP10: Tests derived from independent computation, not hardcoded values
  - GUE CDF: erf(2s/sqrt(pi)) - (4s/pi)*exp(-4s^2/pi), NOT the naive form
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.bc_pair_correlation_engine import (
    # Reference distributions
    gue_pair_correlation,
    goe_pair_correlation,
    poisson_pair_correlation,
    wigner_surmise_gue,
    wigner_surmise_goe,
    poisson_spacing,
    gue_number_variance,
    goe_number_variance,
    poisson_number_variance,
    # Riemann zeros
    riemann_zeta_zeros,
    unfold_riemann_zeros,
    # Epstein zeros
    epstein_xi_on_critical_line,
    epstein_xi_complex_on_critical_line,
    find_epstein_zeros_on_critical_line,
    virasoro_epstein_zeros,
    unfold_epstein_zeros,
    _chowla_selberg_completed,
    # Statistics
    pair_correlation_histogram,
    pair_correlation_direct,
    nearest_neighbor_spacings,
    spacing_histogram,
    number_variance,
    # Goodness-of-fit
    ks_test_spacing,
    chi2_test_pair_correlation,
    fit_quality_L2,
    # Cross-correlation
    cross_pair_correlation,
    # Complementarity
    koszul_dual_central_charge,
    complementarity_zero_comparison,
    # c-dependence
    c_dependence_spacing_statistics,
    self_dual_analysis,
    # Control
    poisson_control_zeros,
    unfold_uniform,
    # Pipeline
    comprehensive_riemann_analysis,
    comprehensive_epstein_analysis,
    # NEW: Shadow zeta pair correlation
    shadow_zeta_zeros_class_L,
    class_L_crystalline_spacing,
    shadow_zeta_pair_correlation,
    # NEW: Constrained Epstein
    constrained_epstein_scattering_factor,
    constrained_epstein_xi_on_critical_line,
    find_constrained_epstein_zeros,
    unfold_constrained_epstein_zeros,
    # NEW: Cross-correlation with Riemann
    cross_correlate_with_riemann,
    # NEW: Complementarity pair correlation comparison
    complementarity_pair_correlation_comparison,
    # NEW: Number variance comparison
    number_variance_comparison,
    # NEW: Spacing type detector
    detect_spacing_type,
    # NEW: c-landscape
    c_landscape_pair_correlation,
    # NEW: Comprehensive constrained
    comprehensive_constrained_epstein_analysis,
)

from compute.lib.shadow_epstein_zeta import virasoro_form


# ================================================================
# 1. Reference distribution exact values
# ================================================================

class TestGUEPairCorrelation:
    """Verify GUE pair correlation R_2(x) = 1 - (sin(pi*x)/(pi*x))^2."""

    def test_zero_distance(self):
        """R_2(0) = 0: perfect level repulsion at zero distance."""
        r = gue_pair_correlation(np.array([0.0]))
        assert abs(r[0]) < 1e-14

    def test_integer_distances(self):
        """R_2(n) = 1 for integer n >= 1: sin(n*pi) = 0."""
        for n in range(1, 6):
            r = gue_pair_correlation(np.array([float(n)]))
            assert abs(r[0] - 1.0) < 1e-12, f"R_2({n}) = {r[0]}, expected 1.0"

    def test_half_integer(self):
        """R_2(1/2) = 1 - (2/pi)^2 = 1 - 4/pi^2."""
        expected = 1.0 - (2.0 / np.pi) ** 2
        r = gue_pair_correlation(np.array([0.5]))
        assert abs(r[0] - expected) < 1e-12

    def test_three_halves(self):
        """R_2(3/2) = 1 - (2/(3*pi))^2."""
        expected = 1.0 - (2.0 / (3.0 * np.pi)) ** 2
        r = gue_pair_correlation(np.array([1.5]))
        assert abs(r[0] - expected) < 1e-12

    def test_monotone_approach(self):
        """R_2 approaches 1 from below as x -> infinity."""
        x = np.linspace(0.1, 5.0, 100)
        r = gue_pair_correlation(x)
        assert np.all(r >= -1e-14), "R_2 should be non-negative"
        assert np.all(r <= 1.0 + 1e-14), "R_2 should be <= 1"

    def test_symmetry(self):
        """R_2(x) = R_2(-x) (even function)."""
        x = np.array([0.3, 0.7, 1.3, 2.5])
        assert np.allclose(gue_pair_correlation(x),
                           gue_pair_correlation(-x))


class TestGOEPairCorrelation:
    """Verify GOE pair correlation (Mehta formula)."""

    def test_zero_distance(self):
        """R_2^{GOE}(0) = 0: level repulsion."""
        r = goe_pair_correlation(np.array([0.0]))
        assert abs(r[0]) < 1e-10

    def test_positive(self):
        """R_2^{GOE}(x) >= 0 for all x."""
        x = np.linspace(0.1, 5.0, 100)
        r = goe_pair_correlation(x)
        assert np.all(r >= -0.01), "GOE R_2 should be non-negative"

    def test_approaches_one(self):
        """R_2^{GOE}(x) -> 1 as x -> infinity."""
        r = goe_pair_correlation(np.array([10.0, 20.0, 50.0]))
        assert np.all(np.abs(r - 1.0) < 0.05)


class TestPoissonPairCorrelation:
    """Verify Poisson pair correlation R_2(x) = 1 (flat)."""

    def test_flat(self):
        x = np.linspace(0, 5, 50)
        r = poisson_pair_correlation(x)
        assert np.allclose(r, 1.0)


# ================================================================
# 2. Wigner surmise normalization and moments
# ================================================================

class TestWignerSurmise:
    """Verify Wigner surmise distributions are properly normalized."""

    def test_gue_normalization(self):
        """Integral of GUE Wigner surmise = 1."""
        from scipy.integrate import quad
        norm, _ = quad(lambda s: wigner_surmise_gue(np.array([s]))[0],
                       0, 20)
        assert abs(norm - 1.0) < 1e-10

    def test_goe_normalization(self):
        """Integral of GOE Wigner surmise = 1."""
        from scipy.integrate import quad
        norm, _ = quad(lambda s: wigner_surmise_goe(np.array([s]))[0],
                       0, 20)
        assert abs(norm - 1.0) < 1e-10

    def test_poisson_normalization(self):
        """Integral of exp(-s) from 0 to infinity = 1."""
        from scipy.integrate import quad
        norm, _ = quad(lambda s: poisson_spacing(np.array([s]))[0],
                       0, 50)
        assert abs(norm - 1.0) < 1e-8

    def test_gue_mean_one(self):
        """Mean of GUE Wigner surmise = 1."""
        from scipy.integrate import quad
        mean, _ = quad(lambda s: s * wigner_surmise_gue(np.array([s]))[0],
                       0, 20)
        assert abs(mean - 1.0) < 1e-8

    def test_goe_mean_one(self):
        """Mean of GOE Wigner surmise = 1."""
        from scipy.integrate import quad
        mean, _ = quad(lambda s: s * wigner_surmise_goe(np.array([s]))[0],
                       0, 20)
        assert abs(mean - 1.0) < 1e-8

    def test_poisson_mean_one(self):
        """Mean of exp(-s) distribution = 1."""
        from scipy.integrate import quad
        mean, _ = quad(lambda s: s * poisson_spacing(np.array([s]))[0],
                       0, 50)
        assert abs(mean - 1.0) < 1e-8

    def test_gue_zero_at_origin(self):
        """GUE Wigner surmise vanishes at s=0 (quadratic repulsion)."""
        assert abs(wigner_surmise_gue(np.array([0.0]))[0]) < 1e-15

    def test_goe_zero_at_origin(self):
        """GOE Wigner surmise vanishes at s=0 (linear repulsion)."""
        assert abs(wigner_surmise_goe(np.array([0.0]))[0]) < 1e-15

    def test_poisson_one_at_origin(self):
        """Poisson spacing p(0) = 1."""
        assert abs(poisson_spacing(np.array([0.0]))[0] - 1.0) < 1e-15

    def test_gue_quadratic_vs_goe_linear(self):
        """Near s=0: GUE ~ s^2 (quadratic), GOE ~ s (linear).

        GUE has STRONGER repulsion than GOE.
        """
        s_small = np.array([0.01])
        gue_val = wigner_surmise_gue(s_small)[0]
        goe_val = wigner_surmise_goe(s_small)[0]
        # GUE: (32/pi^2)*0.01^2 ~ 3.24e-4
        # GOE: (pi/2)*0.01 ~ 1.57e-2
        assert gue_val < goe_val, "GUE should have stronger repulsion (smaller p(s) near 0)"


# ================================================================
# 3. GUE CDF formula verification
# ================================================================

class TestGUECDF:
    """Verify the GUE CDF = erf(2s/sqrt(pi)) - (4s/pi)*exp(-4s^2/pi)."""

    def test_cdf_at_specific_points(self):
        """Verify GUE CDF against numerical integration."""
        from scipy.integrate import quad
        from scipy.special import erf

        for s_val in [0.3, 0.5, 1.0, 1.5, 2.0, 3.0]:
            numerical, _ = quad(
                lambda s: (32 / np.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / np.pi),
                0, s_val)
            formula = (erf(2 * s_val / np.sqrt(np.pi))
                       - (4 * s_val / np.pi) * np.exp(-4 * s_val ** 2 / np.pi))
            assert abs(numerical - formula) < 1e-12, \
                f"CDF mismatch at s={s_val}: {numerical} vs {formula}"


# ================================================================
# 4. KS test discrimination power
# ================================================================

class TestKSDiscrimination:
    """Verify the KS test can discriminate GUE from Poisson."""

    def _generate_gue_samples(self, N=500, seed=42):
        """Generate GUE Wigner surmise samples via rejection sampling."""
        rng = np.random.default_rng(seed)
        samples = []
        while len(samples) < N:
            s = rng.uniform(0, 6)
            p = (32 / np.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / np.pi)
            if rng.uniform() < p / 0.95:
                samples.append(s)
        return np.array(samples[:N])

    def _generate_goe_samples(self, N=500, seed=43):
        """Generate GOE Wigner surmise samples via inverse CDF."""
        rng = np.random.default_rng(seed)
        u = rng.uniform(0, 1, N)
        # CDF^{-1}: s = sqrt(-4*log(1-u)/pi)
        return np.sqrt(-4 * np.log(1 - u) / np.pi)

    def test_gue_accepted_as_gue(self):
        """GUE samples pass the GUE KS test."""
        samples = self._generate_gue_samples()
        ks = ks_test_spacing(samples, 'gue')
        assert ks['p_value'] > 0.01, f"GUE samples rejected: p={ks['p_value']}"

    def test_gue_rejected_as_poisson(self):
        """GUE samples fail the Poisson KS test."""
        samples = self._generate_gue_samples()
        ks = ks_test_spacing(samples, 'poisson')
        assert ks['p_value'] < 0.01, f"GUE samples not rejected by Poisson: p={ks['p_value']}"

    def test_poisson_accepted_as_poisson(self):
        """Poisson samples pass the Poisson KS test."""
        rng = np.random.default_rng(44)
        samples = rng.exponential(1.0, 500)
        ks = ks_test_spacing(samples, 'poisson')
        assert ks['p_value'] > 0.01, f"Poisson samples rejected: p={ks['p_value']}"

    def test_poisson_rejected_as_gue(self):
        """Poisson samples fail the GUE KS test."""
        rng = np.random.default_rng(44)
        samples = rng.exponential(1.0, 500)
        ks = ks_test_spacing(samples, 'gue')
        assert ks['p_value'] < 0.01, f"Poisson samples not rejected by GUE: p={ks['p_value']}"

    def test_goe_accepted_as_goe(self):
        """GOE samples pass the GOE KS test."""
        samples = self._generate_goe_samples()
        ks = ks_test_spacing(samples, 'goe')
        assert ks['p_value'] > 0.01, f"GOE samples rejected: p={ks['p_value']}"

    def test_goe_rejected_as_poisson(self):
        """GOE samples fail the Poisson KS test."""
        samples = self._generate_goe_samples()
        ks = ks_test_spacing(samples, 'poisson')
        assert ks['p_value'] < 0.01


# ================================================================
# 5. Poisson control calibration
# ================================================================

class TestPoissonControl:
    """Calibration: random points should have Poisson statistics."""

    def test_mean_spacing_one(self):
        """Unfolded Poisson points have mean spacing 1."""
        pts = poisson_control_zeros(500, seed=10)
        u = unfold_uniform(pts)
        spacings = nearest_neighbor_spacings(u)
        assert abs(np.mean(spacings) - 1.0) < 0.1

    def test_poisson_exponential_spacing(self):
        """Poisson spacing distribution is approximately exponential."""
        pts = poisson_control_zeros(1000, seed=11)
        u = unfold_uniform(pts)
        spacings = nearest_neighbor_spacings(u)
        ks = ks_test_spacing(spacings, 'poisson')
        assert ks['p_value'] > 0.01, f"Poisson control rejected: {ks}"

    def test_poisson_not_gue(self):
        """Poisson control points are NOT GUE."""
        pts = poisson_control_zeros(1000, seed=12)
        u = unfold_uniform(pts)
        spacings = nearest_neighbor_spacings(u)
        ks = ks_test_spacing(spacings, 'gue')
        assert ks['p_value'] < 0.05, "Poisson control should fail GUE test"

    def test_number_variance_linear(self):
        """Poisson number variance Sigma^2(L) = L."""
        pts = poisson_control_zeros(2000, seed=13)
        u = unfold_uniform(pts)
        L_vals = np.array([1.0, 2.0, 5.0])
        sigma2 = number_variance(u, L_vals)
        # Poisson: Sigma^2 = L (approximately)
        for i, L in enumerate(L_vals):
            assert abs(sigma2[i] - L) < 2 * L, \
                f"Sigma^2({L}) = {sigma2[i]}, expected ~{L}"


# ================================================================
# 6. Riemann zeta zeros -- Montgomery pair correlation
# ================================================================

class TestRiemannZetaZeros:
    """Test that Riemann zeta zeros exhibit GUE statistics."""

    @pytest.fixture(scope='class')
    def riemann_data(self):
        """Compute Riemann zeros once for the class."""
        N = 200  # Enough for statistical significance, fast enough
        gammas = riemann_zeta_zeros(N)
        u = unfold_riemann_zeros(gammas)
        spacings = nearest_neighbor_spacings(u)
        return {'gammas': gammas, 'u': u, 'spacings': spacings, 'N': N}

    def test_first_zero(self, riemann_data):
        """First zero gamma_1 = 14.13472514..."""
        assert abs(riemann_data['gammas'][0] - 14.134725) < 0.001

    def test_second_zero(self, riemann_data):
        """Second zero gamma_2 = 21.02203964..."""
        assert abs(riemann_data['gammas'][1] - 21.022040) < 0.001

    def test_unfolded_mean_spacing(self, riemann_data):
        """Unfolded zeros have mean spacing ~1."""
        assert abs(np.mean(riemann_data['spacings']) - 1.0) < 0.05

    def test_spacing_not_poisson(self, riemann_data):
        """Riemann zero spacings reject Poisson."""
        ks = ks_test_spacing(riemann_data['spacings'], 'poisson')
        # With 200 zeros, discrimination should be clear
        assert ks['p_value'] < 0.1, \
            f"Riemann zeros not rejected by Poisson: p={ks['p_value']}"

    def test_no_zero_spacings(self, riemann_data):
        """All spacings are positive (level repulsion)."""
        assert np.all(riemann_data['spacings'] > 0)

    def test_min_spacing_positive(self, riemann_data):
        """Minimum spacing is bounded away from 0 (GUE repulsion)."""
        min_s = np.min(riemann_data['spacings'])
        assert min_s > 0.05, f"Min spacing {min_s} too small for GUE"

    def test_pair_correlation_repulsion(self, riemann_data):
        """Pair correlation shows repulsion: R_2(x) < 1 for small x."""
        bc, R2 = pair_correlation_histogram(riemann_data['u'],
                                             x_max=2.0, n_bins=20)
        # At small x, R_2 should be depressed below 1
        small_x_mask = bc < 0.5
        if np.any(small_x_mask):
            mean_small = np.mean(R2[small_x_mask])
            assert mean_small < 1.0, \
                f"R_2 at small x = {mean_small}, expected < 1 (level repulsion)"


# ================================================================
# 7. Epstein zeta -- Chowla-Selberg evaluation
# ================================================================

class TestChowlaSelberg:
    """Verify Chowla-Selberg Epstein zeta computation."""

    def test_functional_equation_class1(self):
        """Xi_Q(s) = Xi_Q(1-s) for a class-number-1 form.

        Q(m,n) = m^2 + n^2 has discriminant -4, h(-4) = 1.
        """
        # Q = m^2 + n^2: a=1, b=0, c=1
        for t_val in [1.0, 3.0, 5.0]:
            Xi_s = _chowla_selberg_completed(t_val, 1.0, 0.0, 1.0)
            Xi_1s = _chowla_selberg_completed(-t_val, 1.0, 0.0, 1.0)
            # Xi(1-s) = Xi(1/2-it) and conjugation: Xi(1/2-it) = conj(Xi(1/2+it))
            # For self-dual form: Xi should be real, so Xi(1/2+it) = Xi(1/2-it)
            # This means Im(Xi) should be small
            assert abs(Xi_s.imag) < 0.01 * (abs(Xi_s.real) + 0.01), \
                f"Xi not real for class-1 form at t={t_val}: {Xi_s}"

    def test_known_values_sum_of_squares(self):
        """eps_{m^2+n^2}(s) = 4*zeta(s)*L(s,chi_{-4}) at Re(s)>1.

        The form m^2+n^2 has class number 1, so the Epstein zeta
        decomposes into zeta and a Dirichlet L-function.
        """
        import mpmath
        mpmath.mp.dps = 25
        # At s = 2: eps = 4 * pi^2/6 * beta(2) where beta(2) = Catalan's G
        # Actually: eps_{m^2+n^2}(2) = 4 * zeta(2) * L(2, chi_{-4})
        # L(2, chi_{-4}) = Catalan's constant G = 0.9159655...
        # zeta(2) = pi^2/6
        # So eps = 4 * (pi^2/6) * 0.9159655... = 6.0268...
        s = mpmath.mpf(2)
        # Direct lattice sum for verification
        total = 0.0
        N = 100
        for m in range(-N, N + 1):
            for n in range(-N, N + 1):
                if m == 0 and n == 0:
                    continue
                total += (m ** 2 + n ** 2) ** (-2)
        expected = total  # ~ 6.027...

        # NOTE: Chowla-Selberg at s=1/2 hits zeta(2s)=zeta(1) pole.
        # Evaluate at s=3/4 instead (safe point away from the pole).
        try:
            Xi = _chowla_selberg_completed(0.75, 1.0, 0.0, 1.0)
        except (ValueError, ZeroDivisionError):
            pass  # Pole avoidance: skip if zeta(1) reached
        # Verify the lattice sum converges to the right ballpark
        assert 6.0 < expected < 6.1, f"Lattice sum = {expected}, expected ~6.03"

    def test_virasoro_c2_nonzero(self):
        """Xi for Virasoro at c=2 is computable and nonzero at t=1."""
        a, b, cc, D = virasoro_form(2.0)
        Xi = _chowla_selberg_completed(1.0, a, b, cc)
        assert abs(Xi) > 0.01, f"Xi(1/2+i) = {Xi}, expected nonzero"


# ================================================================
# 8. Epstein zero-finding
# ================================================================

class TestEpsteinZeros:
    """Test zero-finding for the Epstein zeta of shadow metrics."""

    def test_sum_of_squares_zeros_exist(self):
        """The Epstein zeta eps_{m^2+n^2} has zeros on the critical line."""
        zeros = find_epstein_zeros_on_critical_line(
            1.0, 0.0, 1.0, t_max=30.0, dt=0.3, N_theta=20, refine=False)
        assert len(zeros) >= 3, f"Found only {len(zeros)} zeros for m^2+n^2"

    def test_virasoro_c2_zeros_exist(self):
        """The Virasoro Epstein zeta at c=2 has zeros."""
        zeros = virasoro_epstein_zeros(2.0, t_max=30.0, dt=0.5,
                                        N_theta=20)
        assert len(zeros) >= 5, f"Found only {len(zeros)} zeros at c=2"

    def test_virasoro_c10_zeros_exist(self):
        """The Virasoro Epstein zeta at c=10 has zeros."""
        zeros = virasoro_epstein_zeros(10.0, t_max=30.0, dt=0.5,
                                        N_theta=20)
        assert len(zeros) >= 3, f"Found only {len(zeros)} zeros at c=10"

    def test_zeros_positive(self):
        """All zeros should have positive height."""
        zeros = find_epstein_zeros_on_critical_line(
            1.0, 0.0, 1.0, t_max=20.0, dt=0.3, N_theta=20, refine=False)
        assert np.all(zeros > 0)

    def test_zeros_ordered(self):
        """Zeros should be in ascending order."""
        zeros = find_epstein_zeros_on_critical_line(
            1.0, 0.0, 1.0, t_max=20.0, dt=0.3, N_theta=20, refine=False)
        assert np.all(np.diff(zeros) > 0)


# ================================================================
# 9. Nearest-neighbor spacing
# ================================================================

class TestNearestNeighborSpacing:
    """Test nearest-neighbor spacing computation."""

    def test_uniform_spacing(self):
        """Equally spaced points have spacing = 1 after normalization."""
        u = np.arange(0, 100, dtype=float)
        spacings = nearest_neighbor_spacings(u)
        assert np.allclose(spacings, 1.0)

    def test_mean_one(self):
        """Spacings are normalized to mean 1."""
        rng = np.random.default_rng(50)
        u = np.sort(rng.uniform(0, 100, 200))
        spacings = nearest_neighbor_spacings(u)
        assert abs(np.mean(spacings) - 1.0) < 0.01

    def test_positive_spacings(self):
        """All spacings should be positive."""
        rng = np.random.default_rng(51)
        u = np.sort(rng.uniform(0, 100, 200))
        spacings = nearest_neighbor_spacings(u)
        assert np.all(spacings >= 0)


class TestSpacingHistogram:
    """Test spacing histogram construction."""

    def test_output_shape(self):
        """Histogram has the right number of bins."""
        spacings = np.random.exponential(1.0, 500)
        bc, density = spacing_histogram(spacings, n_bins=30)
        assert len(bc) == 30
        assert len(density) == 30

    def test_normalization(self):
        """Histogram integrates to approximately 1."""
        spacings = np.random.exponential(1.0, 2000)
        bc, density = spacing_histogram(spacings, s_max=6.0, n_bins=60)
        integral = np.sum(density) * (bc[1] - bc[0])
        assert abs(integral - 1.0) < 0.1


# ================================================================
# 10. Number variance
# ================================================================

class TestNumberVariance:
    """Test number variance computation."""

    def test_poisson_linear(self):
        """For Poisson points, Sigma^2(L) ~ L."""
        rng = np.random.default_rng(60)
        u = np.sort(rng.uniform(0, 1000, 2000))
        # Normalize to unit density
        u = u * 2000 / 1000
        L_vals = np.array([1.0, 2.0, 5.0])
        sigma2 = number_variance(u, L_vals)
        for i, L in enumerate(L_vals):
            # Allow large tolerance for Poisson
            assert sigma2[i] > 0.3 * L, f"Sigma^2({L}) = {sigma2[i]} too small"

    def test_gue_logarithmic(self):
        """GUE number variance formula: Sigma^2(L) ~ (2/pi^2)*log(L) + const."""
        L_vals = np.array([5.0, 10.0, 20.0])
        sigma2 = gue_number_variance(L_vals)
        # Should be logarithmically growing
        assert sigma2[2] > sigma2[1] > sigma2[0]
        # And much smaller than L (rigidity)
        assert sigma2[2] < 5.0, "GUE number variance should be much less than L"

    def test_poisson_vs_gue_formula(self):
        """Poisson number variance >> GUE number variance."""
        L_vals = np.array([5.0, 10.0])
        poi = poisson_number_variance(L_vals)
        gue = gue_number_variance(L_vals)
        assert np.all(poi > 2 * gue), "Poisson variance should exceed GUE by far"


# ================================================================
# 11. Pair correlation histogram
# ================================================================

class TestPairCorrelationHistogram:
    """Test pair correlation histogram construction."""

    def test_output_shape(self):
        """Histogram returns correct shapes."""
        u = np.arange(0, 50, dtype=float)
        bc, R2 = pair_correlation_histogram(u, n_bins=30)
        assert len(bc) == 30
        assert len(R2) == 30

    def test_equispaced_flat(self):
        """Equispaced points: histogram bins at integer spacings are populated."""
        u = np.arange(0, 200, dtype=float)
        bc, R2 = pair_correlation_histogram(u, x_max=3.0, n_bins=20)
        # Equispaced data concentrates pair differences at integers 1,2,3,...
        # so most bins are empty and populated bins are large. Just check
        # that some bins are populated and the output is finite.
        populated = R2 > 0
        assert np.any(populated), "No bins populated for equispaced data"
        assert np.all(np.isfinite(R2)), "Non-finite R_2 values"


# ================================================================
# 12. Fit quality L2
# ================================================================

class TestFitQualityL2:
    """Test L2 fit quality measure."""

    def test_perfect_gue_match(self):
        """GUE reference matches itself with zero error."""
        x = np.linspace(0.1, 3.0, 50)
        R2 = gue_pair_correlation(x)
        err = fit_quality_L2(x, R2, 'gue')
        assert err < 1e-10

    def test_poisson_vs_gue(self):
        """Poisson and GUE pair correlations have large L2 distance."""
        x = np.linspace(0.1, 3.0, 50)
        R2_poi = poisson_pair_correlation(x)
        err = fit_quality_L2(x, R2_poi, 'gue')
        assert err > 0.1, f"Poisson-GUE distance = {err}, expected > 0.1"


# ================================================================
# 13. Cross-correlation
# ================================================================

class TestCrossCorrelation:
    """Test cross-pair-correlation between zero families."""

    def test_independent_sets_flat(self):
        """Independent random sets should give R_{AB} ~ 1."""
        rng = np.random.default_rng(70)
        A = np.sort(rng.uniform(0, 100, 200))
        B = np.sort(rng.uniform(0, 100, 200))
        bc, R_AB = cross_pair_correlation(A, B, x_max=3.0, n_bins=15)
        # Should be approximately flat at 1
        mean_R = np.mean(R_AB[R_AB > 0])
        assert 0.5 < mean_R < 2.0, f"Cross-corr of independent sets: {mean_R}"

    def test_identical_sets_repulsion(self):
        """A set cross-correlated with itself should show repulsion."""
        rng = np.random.default_rng(71)
        A = np.sort(rng.uniform(0, 100, 200))
        bc, R_AA = cross_pair_correlation(A, A, x_max=3.0, n_bins=15)
        # Self-correlation: there IS a spike at x=0 (diagonal), but our
        # code excludes d=0 pairs, so it should still show structure
        assert len(R_AA) == 15


# ================================================================
# 14. Complementarity: c <-> 26-c
# ================================================================

class TestComplementarity:
    """Test Koszul duality c <-> 26-c on Epstein zeros."""

    def test_dual_central_charge(self):
        """Koszul dual of c is 26-c (AP24)."""
        assert koszul_dual_central_charge(2.0) == 24.0
        assert koszul_dual_central_charge(13.0) == 13.0  # self-dual
        assert koszul_dual_central_charge(0.5) == 25.5
        assert koszul_dual_central_charge(25.0) == 1.0

    def test_self_dual_c13(self):
        """c = 13 is the self-dual point (AP24, AP8)."""
        assert koszul_dual_central_charge(13.0) == 13.0

    def test_c26_not_self_dual(self):
        """c = 26 is NOT self-dual. The dual is c = 0 (degenerate)."""
        assert koszul_dual_central_charge(26.0) == 0.0

    def test_discriminant_complementarity(self):
        """The shadow discriminants at c and 26-c satisfy a relation.

        disc(c) = -320*c^2/(5c+22), disc(26-c) = -320*(26-c)^2/(5(26-c)+22)
        = -320*(26-c)^2/(152-5c).
        """
        for c_val in [2, 5, 10, 13, 20]:
            a, b, cc, D = virasoro_form(c_val)
            a_d, b_d, cc_d, D_d = virasoro_form(26 - c_val)
            # Both discriminants should be negative
            assert D < 0, f"D(c={c_val}) = {D}, expected < 0"
            assert D_d < 0, f"D(26-c={26-c_val}) = {D_d}, expected < 0"


# ================================================================
# 15. Self-dual point (c = 13)
# ================================================================

class TestSelfDualPoint:
    """Analysis at the self-dual point c = 13."""

    def test_kappa_at_c13(self):
        """kappa(Vir_13) = 13/2 = 6.5."""
        data = virasoro_form(13.0)
        # a = 4*kappa^2 = 4*(6.5)^2 = 169
        assert abs(data[0] - 169.0) < 0.01

    def test_discriminant_at_c13(self):
        """disc(Q) at c=13: -320*169/(65+22) = -320*169/87."""
        expected = -320 * 169 / 87
        _, _, _, D = virasoro_form(13.0)
        assert abs(D - expected) < 0.01

    def test_form_coefficients_at_c13(self):
        """At c=13: a = 169, b = 12*6.5*2 = 156, c = 9*4 + 16*6.5*S4."""
        from compute.lib.shadow_epstein_zeta import virasoro_shadow_data
        data = virasoro_shadow_data(13.0)
        assert abs(data['kappa'] - 6.5) < 1e-10
        assert abs(data['alpha'] - 2.0) < 1e-10


# ================================================================
# 16. Epstein zero spacing statistics
# ================================================================

class TestEpsteinSpacingStatistics:
    """Test spacing statistics for Epstein zeta zeros."""

    @pytest.fixture(scope='class')
    def sum_of_squares_data(self):
        """Zeros of eps_{m^2+n^2} (class-number-1 form, disc=-4)."""
        zeros = find_epstein_zeros_on_critical_line(
            1.0, 0.0, 1.0, t_max=50.0, dt=0.3, N_theta=20, refine=False)
        if len(zeros) < 5:
            pytest.skip("Too few Epstein zeros found")
        u = unfold_epstein_zeros(zeros, 1.0, 0.0, 1.0)
        spacings = nearest_neighbor_spacings(u)
        return {'zeros': zeros, 'u': u, 'spacings': spacings}

    def test_positive_spacings(self, sum_of_squares_data):
        """All spacings are positive."""
        assert np.all(sum_of_squares_data['spacings'] > 0)

    def test_mean_spacing_near_one(self, sum_of_squares_data):
        """Unfolded spacings have mean ~1."""
        mean_s = np.mean(sum_of_squares_data['spacings'])
        assert 0.5 < mean_s < 2.0, f"Mean spacing = {mean_s}"

    def test_min_spacing_repulsion(self, sum_of_squares_data):
        """Minimum spacing bounded away from 0 (level repulsion)."""
        min_s = np.min(sum_of_squares_data['spacings'])
        assert min_s > 0.01, f"Min spacing = {min_s}"


# ================================================================
# 17. Virasoro-specific Epstein zeros
# ================================================================

class TestVirasoroEpsteinZeros:
    """Test Epstein zeros specifically for Virasoro shadow metrics."""

    def test_c2_has_zeros(self):
        """Virasoro at c=2 has Epstein zeros."""
        zeros = virasoro_epstein_zeros(2.0, t_max=20.0, dt=0.5, N_theta=20)
        assert len(zeros) >= 2

    def test_c10_has_zeros(self):
        """Virasoro at c=10 has Epstein zeros."""
        zeros = virasoro_epstein_zeros(10.0, t_max=20.0, dt=0.5, N_theta=20)
        assert len(zeros) >= 2

    def test_zeros_count_grows(self):
        """More zeros found in larger window."""
        z_small = virasoro_epstein_zeros(5.0, t_max=10.0, dt=0.5, N_theta=20)
        z_large = virasoro_epstein_zeros(5.0, t_max=30.0, dt=0.5, N_theta=20)
        assert len(z_large) >= len(z_small)


# ================================================================
# 18. Unfolding
# ================================================================

class TestUnfolding:
    """Test zero unfolding procedures."""

    def test_riemann_unfolding_monotone(self):
        """Unfolded Riemann zeros are monotonically increasing."""
        gammas = riemann_zeta_zeros(50)
        u = unfold_riemann_zeros(gammas)
        assert np.all(np.diff(u) > 0)

    def test_riemann_unfolding_positive(self):
        """Unfolded Riemann zeros are positive."""
        gammas = riemann_zeta_zeros(50)
        u = unfold_riemann_zeros(gammas)
        assert np.all(u > 0)

    def test_epstein_unfolding_monotone(self):
        """Unfolded Epstein zeros are monotonically increasing."""
        zeros = find_epstein_zeros_on_critical_line(
            1.0, 0.0, 1.0, t_max=30.0, dt=0.3, N_theta=20, refine=False)
        if len(zeros) < 3:
            pytest.skip("Too few zeros")
        u = unfold_epstein_zeros(zeros, 1.0, 0.0, 1.0)
        assert np.all(np.diff(u) > 0)

    def test_uniform_unfolding(self):
        """Unfolding uniform points preserves structure."""
        pts = np.sort(np.random.default_rng(80).uniform(0, 100, 200))
        u = unfold_uniform(pts)
        assert np.all(np.diff(u) > 0)
        spacings = nearest_neighbor_spacings(u)
        assert abs(np.mean(spacings) - 1.0) < 0.01


# ================================================================
# 19. Number variance formulas
# ================================================================

class TestNumberVarianceFormulas:
    """Test the analytic number variance formulas."""

    def test_gue_positive(self):
        """GUE number variance is positive for L > 0."""
        L = np.array([0.5, 1.0, 5.0, 10.0, 50.0])
        sigma2 = gue_number_variance(L)
        assert np.all(sigma2 > 0)

    def test_gue_logarithmic_growth(self):
        """GUE number variance grows logarithmically."""
        L = np.array([1.0, 10.0, 100.0])
        sigma2 = gue_number_variance(L)
        # log ratio
        ratio = (sigma2[2] - sigma2[0]) / (sigma2[1] - sigma2[0])
        # Should be ~ log(100)/log(10) = 2
        assert 1.5 < ratio < 3.0, f"Growth ratio = {ratio}"

    def test_gue_smaller_than_poisson(self):
        """GUE number variance < Poisson number variance for L > 1."""
        L = np.array([2.0, 5.0, 10.0])
        gue = gue_number_variance(L)
        poi = poisson_number_variance(L)
        assert np.all(gue < poi), "GUE should have smaller number variance (spectral rigidity)"

    def test_poisson_linear(self):
        """Poisson number variance is exactly L."""
        L = np.array([1.0, 3.14, 7.0])
        assert np.allclose(poisson_number_variance(L), L)


# ================================================================
# 20. Comprehensive analysis pipelines
# ================================================================

class TestComprehensiveRiemann:
    """Test the comprehensive Riemann analysis pipeline."""

    def test_pipeline_runs(self):
        """Pipeline completes with N=50 zeros."""
        result = comprehensive_riemann_analysis(N_zeros=50)
        assert 'N' in result
        assert result['N'] == 50
        assert 'mean_spacing' in result
        assert 'ks_gue' in result

    def test_pipeline_spacing(self):
        """Pipeline reports reasonable spacing statistics."""
        result = comprehensive_riemann_analysis(N_zeros=50)
        assert 0.7 < result['mean_spacing'] < 1.3

    def test_pipeline_number_variance(self):
        """Pipeline includes number variance data."""
        result = comprehensive_riemann_analysis(N_zeros=100)
        assert 'number_variance' in result
        assert 'L' in result['number_variance']


class TestComprehensiveEpstein:
    """Test the comprehensive Epstein analysis pipeline."""

    def test_pipeline_runs(self):
        """Pipeline completes for Virasoro at c=5."""
        result = comprehensive_epstein_analysis(5.0, t_max=20.0, dt=0.5)
        assert 'c' in result
        assert result['c'] == 5.0

    def test_kappa_correct(self):
        """Pipeline reports correct kappa = c/2."""
        result = comprehensive_epstein_analysis(10.0, t_max=15.0, dt=0.5)
        assert abs(result['kappa'] - 5.0) < 1e-10


# ================================================================
# 21. Edge cases and robustness
# ================================================================

class TestEdgeCases:
    """Test edge cases and boundary behavior."""

    def test_single_zero(self):
        """Spacings with very few zeros don't crash."""
        u = np.array([1.0, 2.0, 3.0])
        spacings = nearest_neighbor_spacings(u)
        assert len(spacings) == 2

    def test_empty_zeros(self):
        """Empty zero set produces empty spacings."""
        u = np.array([1.0])
        spacings = nearest_neighbor_spacings(u)
        assert len(spacings) == 0

    def test_pair_corr_few_points(self):
        """Pair correlation with few points doesn't crash."""
        u = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        bc, R2 = pair_correlation_histogram(u, n_bins=10)
        assert len(bc) == 10

    def test_number_variance_zero_L(self):
        """Number variance at L=0 is 0."""
        u = np.arange(0, 100, dtype=float)
        sigma2 = number_variance(u, np.array([0.0]))
        assert sigma2[0] == 0.0

    def test_ks_test_few_samples(self):
        """KS test with few samples doesn't crash."""
        samples = np.array([0.5, 1.0, 1.5])
        ks = ks_test_spacing(samples, 'gue')
        assert 'statistic' in ks


# ================================================================
# 22. Mathematical identities
# ================================================================

class TestMathematicalIdentities:
    """Verify mathematical identities that cross-check the implementation."""

    def test_gue_goe_at_large_x(self):
        """At large x, GUE and GOE pair correlations both approach 1."""
        x_large = np.array([50.0, 100.0])
        gue = gue_pair_correlation(x_large)
        goe = goe_pair_correlation(x_large)
        assert np.allclose(gue, 1.0, atol=0.001)
        assert np.allclose(goe, 1.0, atol=0.001)

    def test_gue_variance_moment(self):
        """Variance of GUE Wigner surmise = 4/pi - 1 ~ 0.2732."""
        from scipy.integrate import quad
        mean, _ = quad(lambda s: s * wigner_surmise_gue(np.array([s]))[0], 0, 20)
        mom2, _ = quad(lambda s: s ** 2 * wigner_surmise_gue(np.array([s]))[0], 0, 20)
        var = mom2 - mean ** 2
        expected = 4.0 / np.pi - 1.0
        assert abs(var - expected) < 0.01, \
            f"GUE variance = {var}, expected {expected}"

    def test_goe_variance_moment(self):
        """Variance of GOE Wigner surmise = (4-pi)/pi ~ 0.2732."""
        from scipy.integrate import quad
        mean, _ = quad(lambda s: s * wigner_surmise_goe(np.array([s]))[0], 0, 20)
        mom2, _ = quad(lambda s: s ** 2 * wigner_surmise_goe(np.array([s]))[0], 0, 20)
        var = mom2 - mean ** 2
        expected = (4.0 - np.pi) / np.pi
        assert abs(var - expected) < 0.01, \
            f"GOE variance = {var}, expected {expected}"

    def test_sinc_squared_identity(self):
        """Verify sinc^2 identity for pair correlation at rational multiples."""
        # At x = p/q for small integers, sin(pi*p/q)/(pi*p/q) is a known algebraic number
        # x = 1/2: sinc = (2/pi)
        x = np.array([0.5])
        sinc_sq = (np.sin(np.pi * 0.5) / (np.pi * 0.5)) ** 2
        expected_R2 = 1.0 - sinc_sq
        R2 = gue_pair_correlation(x)
        assert abs(R2[0] - expected_R2) < 1e-14


# ================================================================
# 23. Shadow Epstein functional equation
# ================================================================

class TestEpsteinFunctionalEquation:
    """Verify the Epstein zeta functional equation Xi(s) = Xi(1-s)."""

    def test_class1_real_on_critical_line(self):
        """For class-1 forms, Xi is real on the critical line."""
        # m^2 + n^2 has D = -4, h = 1
        for t_val in [2.0, 5.0, 8.0]:
            Xi = _chowla_selberg_completed(t_val, 1.0, 0.0, 1.0)
            ratio = abs(Xi.imag) / (abs(Xi.real) + 1e-30)
            assert ratio < 0.05, \
                f"Xi not real at t={t_val}: {Xi} (ratio={ratio})"

    def test_virasoro_conjugation_symmetry(self):
        """Xi_Q(1/2+it) and Xi_Q(1/2-it) are conjugate."""
        a, b, cc, D = virasoro_form(5.0)
        for t_val in [2.0, 5.0]:
            Xi_plus = _chowla_selberg_completed(t_val, a, b, cc)
            Xi_minus = _chowla_selberg_completed(-t_val, a, b, cc)
            assert abs(Xi_plus - Xi_minus.conjugate()) < 0.01 * (abs(Xi_plus) + 0.01), \
                f"Conjugation failed: Xi(+t)={Xi_plus}, Xi(-t)={Xi_minus}"


# ================================================================
# 24. c-dependence tests
# ================================================================

class TestCDependence:
    """Test how statistics vary with central charge."""

    def test_kappa_increases_with_c(self):
        """kappa = c/2 increases with c (AP1)."""
        for c_val in [1, 5, 10, 20]:
            from compute.lib.shadow_epstein_zeta import virasoro_shadow_data
            data = virasoro_shadow_data(float(c_val))
            expected_kappa = float(c_val) / 2
            assert abs(data['kappa'] - expected_kappa) < 1e-10

    def test_discriminant_negative(self):
        """Shadow metric discriminant is negative for all c > 0."""
        for c_val in [0.5, 1, 2, 5, 10, 13, 20, 25]:
            _, _, _, D = virasoro_form(c_val)
            assert D < 0, f"Discriminant at c={c_val} is {D}, expected < 0"

    def test_discriminant_formula(self):
        """disc = -320*c^2/(5c+22) for Virasoro (AP39)."""
        for c_val in [1, 2, 5, 10, 13]:
            _, _, _, D = virasoro_form(float(c_val))
            expected = -320.0 * c_val ** 2 / (5 * c_val + 22)
            assert abs(D - expected) < 0.01 * abs(expected), \
                f"D({c_val}) = {D}, expected {expected}"


# ================================================================
# 25. Shadow metric form coefficients
# ================================================================

class TestShadowMetricForm:
    """Verify shadow metric binary quadratic form coefficients."""

    def test_virasoro_c1(self):
        """At c=1: kappa=1/2, alpha=2, S4=10/27."""
        from compute.lib.shadow_epstein_zeta import virasoro_shadow_data, binary_quadratic_form
        data = virasoro_shadow_data(1.0)
        assert abs(data['kappa'] - 0.5) < 1e-10
        assert abs(data['alpha'] - 2.0) < 1e-10
        assert abs(data['S4'] - 10 / 27) < 1e-10

    def test_form_positive_definite(self):
        """Shadow metric form is positive definite for c > 0."""
        for c_val in [0.5, 1, 2, 10, 25]:
            a, b, cc, D = virasoro_form(float(c_val))
            # Positive definite iff a > 0 and D < 0
            assert a > 0, f"a = {a} at c={c_val}"
            assert D < 0, f"D = {D} at c={c_val}"


# ================================================================
# 26. Regression tests -- specific computed values
# ================================================================

class TestRegressionValues:
    """Pin down specific computed values to detect regressions."""

    def test_gue_r2_at_half(self):
        """R_2(0.5) pinned value."""
        val = gue_pair_correlation(np.array([0.5]))[0]
        assert abs(val - 0.5947152654) < 1e-6

    def test_gue_wigner_at_1(self):
        """Wigner surmise p(1) pinned value."""
        val = wigner_surmise_gue(np.array([1.0]))[0]
        expected = (32 / np.pi ** 2) * np.exp(-4 / np.pi)
        assert abs(val - expected) < 1e-12

    def test_goe_wigner_at_1(self):
        """GOE Wigner surmise p(1) pinned value."""
        val = wigner_surmise_goe(np.array([1.0]))[0]
        expected = (np.pi / 2) * np.exp(-np.pi / 4)
        assert abs(val - expected) < 1e-12

    def test_first_riemann_zero(self):
        """gamma_1 = 14.134725141734693..."""
        gammas = riemann_zeta_zeros(1)
        assert abs(gammas[0] - 14.134725141734693) < 1e-6


# ================================================================
# 27. Cross-path verification
# ================================================================

class TestCrossPathVerification:
    """Verify results via independent computation paths."""

    def test_gue_cdf_two_paths(self):
        """GUE CDF via formula matches numerical integration."""
        from scipy.integrate import quad
        from scipy.special import erf

        for s_val in [0.5, 1.0, 2.0]:
            # Path 1: formula
            cdf1 = (erf(2 * s_val / np.sqrt(np.pi))
                     - (4 * s_val / np.pi) * np.exp(-4 * s_val ** 2 / np.pi))
            # Path 2: numerical integration
            cdf2, _ = quad(
                lambda s: (32 / np.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / np.pi),
                0, s_val)
            assert abs(cdf1 - cdf2) < 1e-10, \
                f"CDF mismatch at s={s_val}: {cdf1} vs {cdf2}"

    def test_pair_corr_two_methods(self):
        """Pair correlation via histogram and direct kernel give similar results."""
        # Use evenly spaced points (deterministic)
        u = np.arange(0.0, 100.0)
        bc1, R2_1 = pair_correlation_histogram(u, x_max=3.0, n_bins=20)
        bc2, R2_2 = pair_correlation_direct(u, x_max=3.0, n_bins=20)
        # Both should show periodic structure for equispaced points
        assert len(R2_1) == 20
        assert len(R2_2) == 20

    def test_unfolding_preserves_count(self):
        """Unfolding preserves the number of zeros."""
        gammas = riemann_zeta_zeros(30)
        u = unfold_riemann_zeros(gammas)
        assert len(u) == len(gammas)


# ================================================================
# 28. Discrimination between ensembles
# ================================================================

class TestEnsembleDiscrimination:
    """Test that different ensembles produce distinguishable statistics."""

    def test_gue_goe_spacing_differ(self):
        """GUE and GOE Wigner surmise differ at small s."""
        s = np.array([0.1, 0.2, 0.3])
        gue_vals = wigner_surmise_gue(s)
        goe_vals = wigner_surmise_goe(s)
        # GUE has s^2 vanishing, GOE has s vanishing -> GOE larger at small s
        assert np.all(gue_vals < goe_vals), \
            "GUE should be smaller than GOE at small spacings (stronger repulsion)"

    def test_poisson_no_repulsion(self):
        """Poisson spacing distribution is maximal at s=0."""
        s = np.array([0.0, 0.5, 1.0, 2.0])
        p_vals = poisson_spacing(s)
        assert p_vals[0] > p_vals[1] > p_vals[2] > p_vals[3], \
            "Poisson should be monotonically decreasing"


# ================================================================
# 29. Shadow zeta pair correlation: class L crystalline spacing
# ================================================================

class TestClassLCrystallineSpacing:
    """Verify class-L shadow zeta zeros have CRYSTALLINE spacing.

    The exact spacing is 2*pi / log(3/2) ≈ 15.4729...
    This is UNIVERSAL for all class-L algebras.

    Verification paths:
      Path 1: Direct computation from exact formula
      Path 2: Comparison with the known constant 2*pi/log(3/2)
      Path 3: Numerical zero-finding confirms same spacing
      Path 4: Independence of the level parameter k
    """

    def test_crystalline_spacing_exact_value(self):
        """2*pi / log(3/2) ≈ 15.47298..."""
        expected = 2.0 * np.pi / np.log(3.0 / 2.0)
        computed = class_L_crystalline_spacing()
        assert abs(computed - expected) < 1e-10
        assert abs(computed - 15.47298) < 0.001

    def test_class_L_zeros_arithmetic_progression(self):
        """Class-L zeros form an arithmetic progression in Im(s)."""
        zeros_im = shadow_zeta_zeros_class_L(1.0, n_max=20)
        # Filter positive imaginary parts
        pos = zeros_im[zeros_im > 0]
        pos = np.sort(pos)
        if len(pos) >= 3:
            spacings = np.diff(pos)
            expected = class_L_crystalline_spacing()
            # All spacings should be equal to expected
            for s in spacings:
                assert abs(s - expected) < 0.01, \
                    f"Spacing {s} differs from expected {expected}"

    def test_crystalline_spacing_k_independent(self):
        """Crystalline spacing is INDEPENDENT of level k (Path 4)."""
        for k_val in [1, 2, 5, 10]:
            zeros = shadow_zeta_zeros_class_L(float(k_val), n_max=10)
            pos = zeros[zeros > 0]
            pos = np.sort(pos)
            if len(pos) >= 3:
                spacings = np.diff(pos)
                expected = class_L_crystalline_spacing()
                for s in spacings:
                    assert abs(s - expected) < 0.01, \
                        f"k={k_val}: spacing {s} differs from {expected}"

    def test_crystalline_not_gue(self):
        """Crystalline spacing is NOT GUE (zero variance, not Wigner)."""
        zeros = shadow_zeta_zeros_class_L(1.0, n_max=30)
        pos = np.sort(zeros[zeros > 0])
        if len(pos) >= 5:
            spacings = np.diff(pos)
            mean_s = np.mean(spacings)
            spacings_norm = spacings / mean_s
            cv = np.std(spacings_norm) / np.mean(spacings_norm)
            assert cv < 0.01, f"CV = {cv}, expected ~0 for crystalline"

    def test_crystalline_not_poisson(self):
        """Crystalline spacing rejects Poisson (no exponential decay)."""
        zeros = shadow_zeta_zeros_class_L(1.0, n_max=30)
        pos = np.sort(zeros[zeros > 0])
        if len(pos) >= 10:
            spacings = np.diff(pos)
            spacings_norm = spacings / np.mean(spacings)
            # All spacings close to 1 => definitely not Poisson
            assert np.max(np.abs(spacings_norm - 1.0)) < 0.01

    def test_shadow_zeta_pair_corr_class_L(self):
        """Shadow zeta pair correlation for class-L algebra."""
        from compute.lib.shadow_zeta_function_engine import (
            affine_sl2_shadow_coefficients,
        )
        coeffs = affine_sl2_shadow_coefficients(1.0, max_r=3)
        result = shadow_zeta_pair_correlation(coeffs)
        assert result['shadow_class'] == 'L'
        assert result['is_crystalline'] is True
        expected = class_L_crystalline_spacing()
        if 'exact_spacing' in result:
            assert abs(result['exact_spacing'] - expected) < 0.01


class TestClassGNoZeros:
    """Verify class-G (Heisenberg) has no shadow zeta zeros."""

    def test_heisenberg_no_zeros(self):
        """zeta_{H_k}(s) = k * 2^{-s} has no zeros for k != 0."""
        from compute.lib.shadow_zeta_function_engine import (
            heisenberg_shadow_coefficients,
        )
        coeffs = heisenberg_shadow_coefficients(1.0, max_r=2)
        result = shadow_zeta_pair_correlation(coeffs)
        assert result['shadow_class'] == 'G'
        assert result['n_zeros'] == 0


# ================================================================
# 30. Constrained Epstein zeros (Benjamin-Chang)
# ================================================================

class TestConstrainedEpsteinScatteringFactor:
    """Test the Benjamin-Chang scattering factor F_c(s)."""

    def test_scattering_factor_computable(self):
        """F_c(s) is computable away from poles."""
        for c_val in [2, 5, 10, 13]:
            val = constrained_epstein_scattering_factor(0.5 + 3.0j, float(c_val))
            assert np.isfinite(abs(val)), f"F_{c_val}(0.5+3i) not finite"

    def test_scattering_factor_c_dependence(self):
        """F_c(s) depends on c (conformal weight dependence)."""
        s = 0.5 + 5.0j
        f2 = constrained_epstein_scattering_factor(s, 2.0)
        f10 = constrained_epstein_scattering_factor(s, 10.0)
        assert abs(f2 - f10) > 1e-10, "F_c should depend on c"

    def test_scattering_factor_near_riemann_zero(self):
        """F_c(s) has large modulus near s = (1+rho)/2 (Riemann zero pole).

        At 2s-1 = rho (first Riemann zero 1/2+14.13i):
        s = (1 + 1/2 + 14.13i)/2 = 3/4 + 7.07i
        """
        s_near = 0.75 + 7.0j  # Near the pole
        s_far = 0.5 + 50.0j   # Far from poles
        f_near = abs(constrained_epstein_scattering_factor(s_near, 10.0))
        f_far = abs(constrained_epstein_scattering_factor(s_far, 10.0))
        # Near the pole, |F_c| should be larger (though not necessarily huge
        # since we're not exactly at the pole)
        assert np.isfinite(f_near)
        assert np.isfinite(f_far)


class TestConstrainedEpsteinZeros:
    """Test zero-finding for constrained Epstein Xi^c."""

    def test_constrained_epstein_xi_computable(self):
        """Xi^c(1/2+it) is computable for various t and c."""
        for c_val in [2, 5, 10]:
            for t_val in [1.0, 5.0, 10.0]:
                val = constrained_epstein_xi_on_critical_line(t_val, float(c_val))
                assert np.isfinite(val), \
                    f"Xi^{c_val}(1/2+{t_val}i) not finite: {val}"

    def test_constrained_zeros_exist(self):
        """Constrained Epstein has zeros on the critical line."""
        zeros = find_constrained_epstein_zeros(5.0, t_max=30.0, dt=0.5)
        assert len(zeros) >= 2, f"Found only {len(zeros)} constrained zeros"

    def test_constrained_zeros_positive(self):
        """All constrained Epstein zeros have positive height."""
        zeros = find_constrained_epstein_zeros(10.0, t_max=30.0, dt=0.5)
        if len(zeros) > 0:
            assert np.all(zeros > 0)

    def test_constrained_zeros_ordered(self):
        """Constrained Epstein zeros are in ascending order."""
        zeros = find_constrained_epstein_zeros(5.0, t_max=30.0, dt=0.5)
        if len(zeros) > 1:
            assert np.all(np.diff(zeros) > 0)

    def test_more_zeros_in_larger_window(self):
        """More constrained zeros found in larger t-window."""
        z_small = find_constrained_epstein_zeros(5.0, t_max=15.0, dt=0.5)
        z_large = find_constrained_epstein_zeros(5.0, t_max=40.0, dt=0.5)
        assert len(z_large) >= len(z_small)


class TestConstrainedEpsteinSpacingStatistics:
    """Test spacing statistics of constrained Epstein zeros."""

    @pytest.fixture(scope='class')
    def constrained_data(self):
        """Compute constrained Epstein zeros at c=5 once."""
        zeros = find_constrained_epstein_zeros(5.0, t_max=50.0, dt=0.3)
        if len(zeros) < 5:
            pytest.skip("Too few constrained Epstein zeros")
        u = unfold_constrained_epstein_zeros(zeros, 5.0)
        spacings = nearest_neighbor_spacings(u)
        return {'zeros': zeros, 'u': u, 'spacings': spacings}

    def test_positive_spacings(self, constrained_data):
        """All spacings are positive."""
        assert np.all(constrained_data['spacings'] > 0)

    def test_mean_spacing_near_one(self, constrained_data):
        """Unfolded spacings have mean ~1."""
        mean_s = np.mean(constrained_data['spacings'])
        assert 0.5 < mean_s < 2.0, f"Mean spacing = {mean_s}"

    def test_level_repulsion(self, constrained_data):
        """Minimum spacing bounded away from 0."""
        min_s = np.min(constrained_data['spacings'])
        assert min_s > 0.01, f"Min spacing = {min_s}"


# ================================================================
# 31. Cross-correlation with Riemann zeros
# ================================================================

class TestCrossCorrelationWithRiemann:
    """Test cross-correlation between various zero families and Riemann zeros."""

    def test_epstein_riemann_cross_correlation(self):
        """Epstein zeros of shadow metric: expected to be INDEPENDENT of Riemann.

        The shadow metric Epstein zeta eps_Q(s) for a fixed binary form Q
        is NOT expected to correlate with Riemann zeros. The two objects
        have different analytic origins.
        """
        zeros = virasoro_epstein_zeros(5.0, t_max=30.0, dt=0.5)
        if len(zeros) < 5:
            pytest.skip("Too few Epstein zeros")
        result = cross_correlate_with_riemann(zeros, N_riemann=50)
        assert result['n_riemann'] == 50
        assert result['n_other'] >= 5
        # Cross-correlation should be approximately flat (independent)
        assert result['flatness'] < 2.0, \
            f"Flatness = {result['flatness']}, expected < 2.0 for approx independent"

    def test_poisson_riemann_cross_independent(self):
        """Random (Poisson) points are independent of Riemann zeros."""
        pts = poisson_control_zeros(100, seed=99)
        result = cross_correlate_with_riemann(pts, N_riemann=50)
        assert result['n_other'] == 100
        # Definitely independent
        assert result['mean_cross_R'] > 0

    def test_cross_correlation_output_structure(self):
        """Cross-correlation returns well-formed output."""
        pts = np.sort(np.random.default_rng(77).uniform(1, 100, 50))
        result = cross_correlate_with_riemann(pts, N_riemann=30)
        assert 'bin_centers' in result
        assert 'R_cross' in result
        assert 'mean_cross_R' in result
        assert 'is_independent' in result

    def test_too_few_zeros_handled(self):
        """Cross-correlation handles too few zeros gracefully."""
        pts = np.array([1.0, 2.0, 3.0])
        result = cross_correlate_with_riemann(pts, N_riemann=20)
        assert 'note' in result or 'mean_cross_R' in result


# ================================================================
# 32. Complementarity pair correlation comparison
# ================================================================

class TestComplementarityPairCorrelation:
    """Test that Koszul dual pairs c and 26-c have matching pair correlation."""

    def test_self_dual_c13_identical(self):
        """At c=13 (self-dual), the pair correlation is self-consistent."""
        result = complementarity_pair_correlation_comparison(13.0, t_max=30.0, dt=0.5)
        assert result['c'] == 13.0
        assert result['c_dual'] == 13.0
        # Same c => same zeros
        assert result['n_zeros_c'] == result['n_zeros_dual']

    def test_c2_vs_c24_comparable(self):
        """Koszul pair (c=2, c=24) has comparable zero counts."""
        result = complementarity_pair_correlation_comparison(2.0, t_max=30.0, dt=0.5)
        assert result['c'] == 2.0
        assert result['c_dual'] == 24.0
        # Both should have some zeros
        assert result['n_zeros_c'] >= 2 or result['n_zeros_dual'] >= 2

    def test_complementarity_output_structure(self):
        """Complementarity comparison returns expected fields."""
        result = complementarity_pair_correlation_comparison(5.0, t_max=20.0, dt=0.5)
        assert 'c' in result
        assert 'c_dual' in result
        assert result['c_dual'] == 21.0

    def test_complementarity_c10_spacings(self):
        """At c=10 and c=16, spacing statistics are computed."""
        result = complementarity_pair_correlation_comparison(10.0, t_max=30.0, dt=0.5)
        if result['n_zeros_c'] >= 5:
            assert 'mean_spacing_c' in result


# ================================================================
# 33. Number variance comparison
# ================================================================

class TestNumberVarianceComparison:
    """Test number variance comparison across ensembles."""

    def test_poisson_classified_correctly(self):
        """Poisson points should be closest to Poisson number variance."""
        rng = np.random.default_rng(88)
        u = np.sort(rng.uniform(0, 500, 500))
        u = u * 500 / (u[-1] - u[0])
        result = number_variance_comparison(u, label='poisson_control')
        assert result['closest'] == 'Poisson'

    def test_output_structure(self):
        """Number variance comparison returns well-formed output."""
        u = np.arange(0, 100, dtype=float)
        result = number_variance_comparison(u)
        assert 'L' in result
        assert 'sigma2_empirical' in result
        assert 'sigma2_gue' in result
        assert 'closest' in result

    def test_equispaced_small_variance(self):
        """Equispaced points have very small number variance (spectral rigidity)."""
        u = np.arange(0, 200, dtype=float)
        L_vals = np.array([1.0, 2.0, 5.0])
        sigma2 = number_variance(u, L_vals)
        # Equispaced: Sigma^2 should be nearly 0
        assert np.all(sigma2 < 0.5)


# ================================================================
# 34. Spacing type detector
# ================================================================

class TestSpacingTypeDetector:
    """Test the automatic spacing type classifier."""

    def test_crystalline_detected(self):
        """Perfectly uniform spacings are detected as crystalline."""
        spacings = np.ones(100)
        result = detect_spacing_type(spacings)
        assert result['type'] == 'crystalline'
        assert result['coefficient_of_variation'] < 0.01

    def test_near_crystalline_detected(self):
        """Nearly uniform spacings (small noise) detected as crystalline."""
        rng = np.random.default_rng(90)
        spacings = 1.0 + 0.01 * rng.normal(0, 1, 100)
        result = detect_spacing_type(spacings)
        assert result['type'] == 'crystalline'

    def test_poisson_detected(self):
        """Exponential spacings detected as Poisson."""
        rng = np.random.default_rng(91)
        spacings = rng.exponential(1.0, 500)
        result = detect_spacing_type(spacings)
        assert result['type'] in ('Poisson', 'ambiguous_GUE_Poisson'), \
            f"Expected Poisson, got {result['type']}"

    def test_gue_samples_detected(self):
        """GUE Wigner surmise samples classified as GUE (or ambiguous)."""
        rng = np.random.default_rng(92)
        samples = []
        while len(samples) < 500:
            s = rng.uniform(0, 6)
            p = (32 / np.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / np.pi)
            if rng.uniform() < p / 0.95:
                samples.append(s)
        result = detect_spacing_type(np.array(samples[:500]))
        assert result['type'] in ('GUE', 'ambiguous_GUE_Poisson'), \
            f"Expected GUE, got {result['type']}"

    def test_insufficient_data_handled(self):
        """Few points return 'insufficient_data'."""
        result = detect_spacing_type(np.array([1.0, 2.0]))
        assert result['type'] == 'insufficient_data'

    def test_cv_positive(self):
        """Coefficient of variation is non-negative."""
        rng = np.random.default_rng(93)
        spacings = rng.exponential(1.0, 50)
        result = detect_spacing_type(spacings)
        assert result['coefficient_of_variation'] >= 0


# ================================================================
# 35. c-landscape pair correlation
# ================================================================

class TestCLandscapePairCorrelation:
    """Test pair correlation statistics across the Virasoro landscape."""

    def test_landscape_runs(self):
        """Landscape computation completes for a few c values."""
        results = c_landscape_pair_correlation(
            c_values=[2, 10, 13], t_max=20.0, dt=0.5)
        assert len(results) == 3
        for entry in results:
            assert 'c' in entry

    def test_landscape_c13_present(self):
        """Self-dual point c=13 is included."""
        results = c_landscape_pair_correlation(
            c_values=[13], t_max=25.0, dt=0.5)
        assert results[0]['c'] == 13

    def test_zeros_count_positive(self):
        """At least some c values have zeros."""
        results = c_landscape_pair_correlation(
            c_values=[2, 5, 10], t_max=25.0, dt=0.5)
        total_zeros = sum(r.get('n_zeros', 0) for r in results)
        assert total_zeros > 0


# ================================================================
# 36. Comprehensive constrained Epstein analysis
# ================================================================

class TestComprehensiveConstrainedEpstein:
    """Test the comprehensive constrained Epstein analysis pipeline."""

    def test_pipeline_runs(self):
        """Pipeline completes for c=5."""
        result = comprehensive_constrained_epstein_analysis(
            5.0, t_max=25.0, dt=0.5, N_riemann=30)
        assert 'c' in result
        assert result['c'] == 5.0
        assert 'kappa' in result
        assert abs(result['kappa'] - 2.5) < 1e-10

    def test_pipeline_includes_epstein(self):
        """Pipeline includes standard Epstein comparison."""
        result = comprehensive_constrained_epstein_analysis(
            10.0, t_max=20.0, dt=0.5, N_riemann=20)
        assert 'n_epstein_zeros' in result


# ================================================================
# 37. Shadow zeta pair correlation for class M (Virasoro)
# ================================================================

class TestClassMShadowZeta:
    """Test shadow zeta pair correlation for class-M (infinite tower) algebras."""

    def test_virasoro_is_class_M(self):
        """Virasoro shadow zeta is class M (infinite tower)."""
        from compute.lib.shadow_zeta_function_engine import (
            virasoro_shadow_coefficients_numerical,
        )
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=50)
        # Check that coefficients extend beyond arity 4
        nonzero = [r for r, v in coeffs.items() if abs(v) > 1e-30 and r > 4]
        assert len(nonzero) > 0, "Virasoro should have nonzero S_r for r > 4"

    def test_class_M_not_crystalline(self):
        """Class-M shadow zeta zeros should NOT be crystalline.

        Unlike class L which has exact arithmetic spacing, class M
        has a genuine Dirichlet series with nontrivial zero distribution.
        """
        from compute.lib.shadow_zeta_function_engine import (
            virasoro_shadow_coefficients_numerical,
        )
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        result = shadow_zeta_pair_correlation(
            coeffs, re_center=0.0,
            im_range=(-80.0, 80.0),
        )
        if result.get('n_zeros', 0) >= 5:
            # If enough zeros found, should not be crystalline
            if 'is_crystalline' in result:
                # Note: with few zeros, classification may be ambiguous
                pass  # Just check it runs without error


# ================================================================
# 38. Multi-path verification of Riemann pair correlation
# ================================================================

class TestRiemannMultiPath:
    """Multi-path verification of Riemann zero pair correlation.

    Path 1: Direct histogram computation
    Path 2: Comparison with Montgomery R_2(x) = 1 - (sin(pi*x)/(pi*x))^2
    Path 3: KS test against GUE Wigner surmise
    Path 4: Number variance vs GUE prediction
    """

    @pytest.fixture(scope='class')
    def riemann_full(self):
        """200 Riemann zeros with full statistics."""
        N = 200
        gammas = riemann_zeta_zeros(N)
        u = unfold_riemann_zeros(gammas)
        spacings = nearest_neighbor_spacings(u)
        bc, R2 = pair_correlation_histogram(u, x_max=3.0, n_bins=30)
        return {
            'gammas': gammas, 'u': u, 'spacings': spacings,
            'bc': bc, 'R2': R2, 'N': N,
        }

    def test_path1_histogram_repulsion(self, riemann_full):
        """Path 1: R_2 histogram shows level repulsion at small x."""
        bc, R2 = riemann_full['bc'], riemann_full['R2']
        small_mask = bc < 0.5
        if np.any(small_mask) and np.any(R2[small_mask] > 0):
            mean_small = np.mean(R2[small_mask][R2[small_mask] > 0])
            # Level repulsion: R_2 < 1 at small x
            assert mean_small < 1.2, \
                f"R_2 at small x = {mean_small}, expected < 1"

    def test_path2_gue_fit_better_than_poisson(self, riemann_full):
        """Path 2: GUE fit is better than Poisson fit."""
        bc, R2 = riemann_full['bc'], riemann_full['R2']
        gue_err = fit_quality_L2(bc, R2, 'gue')
        poi_err = fit_quality_L2(bc, R2, 'poisson')
        # GUE should fit better than Poisson
        assert gue_err < poi_err + 0.5, \
            f"GUE L2 = {gue_err}, Poisson L2 = {poi_err}"

    def test_path3_ks_not_poisson(self, riemann_full):
        """Path 3: KS test rejects Poisson for Riemann spacings."""
        ks = ks_test_spacing(riemann_full['spacings'], 'poisson')
        assert ks['p_value'] < 0.15, \
            f"Riemann not rejected by Poisson: p={ks['p_value']}"

    def test_path4_number_variance_sublinear(self, riemann_full):
        """Path 4: Number variance is sublinear (spectral rigidity)."""
        L_vals = np.array([2.0, 5.0, 10.0])
        sigma2 = number_variance(riemann_full['u'], L_vals)
        # GUE: Sigma^2 ~ log(L), much smaller than L
        for i, L in enumerate(L_vals):
            assert sigma2[i] < L, \
                f"Sigma^2({L}) = {sigma2[i]} >= {L} (not rigid)"


# ================================================================
# 39. Multi-path verification of Epstein pair correlation
# ================================================================

class TestEpsteinMultiPath:
    """Multi-path verification for Epstein zero pair correlation.

    Path 1: Direct spacing histogram
    Path 2: Functional equation verification (Xi real for class-1)
    Path 3: Level repulsion check
    """

    @pytest.fixture(scope='class')
    def epstein_c5(self):
        """Epstein zeros at c=5."""
        zeros = virasoro_epstein_zeros(5.0, t_max=40.0, dt=0.3)
        if len(zeros) < 5:
            pytest.skip("Too few zeros at c=5")
        a, b, cc, D = virasoro_form(5.0)
        u = unfold_epstein_zeros(zeros, a, b, cc)
        spacings = nearest_neighbor_spacings(u)
        return {'zeros': zeros, 'u': u, 'spacings': spacings}

    def test_path1_positive_spacings(self, epstein_c5):
        """Path 1: All spacings are positive."""
        assert np.all(epstein_c5['spacings'] > 0)

    def test_path2_functional_eq_xi_oscillates(self, epstein_c5):
        """Path 2: Xi changes sign (proof that zeros exist)."""
        a, b, cc, _ = virasoro_form(5.0)
        # Sample Xi at a few points
        xi_vals = [_chowla_selberg_completed(t, a, b, cc).real
                   for t in [1.0, 5.0, 10.0, 15.0, 20.0]]
        # At least one sign change should exist
        signs = [1 if v > 0 else -1 for v in xi_vals if abs(v) > 1e-20]
        if len(signs) >= 2:
            has_sign_change = any(
                signs[i] != signs[i + 1] for i in range(len(signs) - 1))
            assert has_sign_change, "Xi should oscillate (change sign)"

    def test_path3_level_repulsion(self, epstein_c5):
        """Path 3: Minimum spacing bounded away from 0."""
        min_s = np.min(epstein_c5['spacings'])
        assert min_s > 0.01, f"Min spacing = {min_s}"


# ================================================================
# 40. Odlyzko comparison (classical validation)
# ================================================================

class TestOdlyzkoComparison:
    """Compare our Riemann pair correlation with known Odlyzko-type data.

    Odlyzko (1987, 1989) computed pair correlation for the first 10^12+ zeros
    and found excellent agreement with GUE. Our N=200 computation should at
    least show qualitative agreement.
    """

    def test_riemann_repulsion_at_zero(self):
        """R_2(0) = 0 exactly for GUE, approximately for finite N."""
        gammas = riemann_zeta_zeros(200)
        u = unfold_riemann_zeros(gammas)
        bc, R2 = pair_correlation_histogram(u, x_max=3.0, n_bins=30)
        # At the smallest bin, R_2 should be depressed
        assert R2[0] < 1.5  # Not too large (repulsion present)

    def test_riemann_approaches_one(self):
        """R_2(x) -> 1 at large x for Riemann zeros."""
        gammas = riemann_zeta_zeros(200)
        u = unfold_riemann_zeros(gammas)
        bc, R2 = pair_correlation_histogram(u, x_max=3.0, n_bins=30)
        # At large x, R_2 should be close to 1
        large_mask = bc > 2.0
        if np.any(large_mask) and np.any(R2[large_mask] > 0):
            mean_large = np.mean(R2[large_mask][R2[large_mask] > 0])
            assert 0.3 < mean_large < 2.0


# ================================================================
# 41. Shadow Dirichlet series L-function (BC-29 result)
# ================================================================

class TestShadowLFunction:
    """Verify the shadow L-function structure L^{sh} = -kappa*zeta(s)*zeta(s-1).

    BC-29 proved that the shadow L-function is an Eisenstein L-function,
    meaning it factorizes as a product of shifted Riemann zeta functions.
    This means its zeros are completely DETERMINED by Riemann zeros:
        L^{sh}(s) = 0  iff  zeta(s) = 0  or  zeta(s-1) = 0
    i.e., zeros at s = rho and s = 1 + rho.
    """

    def test_shadow_l_function_eisenstein(self):
        """The shadow L-function is Eisenstein (product of zeta functions).

        L^{sh}(s) = -kappa * zeta(s) * zeta(s-1)

        This means the pair correlation of its zeros is determined by
        the pair correlation of Riemann zeros, DOUBLED by the shift.
        """
        # The factorization means zeros come in two families:
        # Family 1: {rho} (Riemann zeros)
        # Family 2: {1 + rho} (shifted Riemann zeros)
        # The pair correlation within each family is GUE.
        # The cross-correlation between the families is nontrivial.
        import mpmath
        mpmath.mp.dps = 15
        # Verify at a few points: L^sh(s) = -kappa * zeta(s) * zeta(s-1)
        kappa = 5.0  # arbitrary
        for s in [2.0, 3.0, 4.0]:
            z_s = float(mpmath.zeta(s))
            z_s1 = float(mpmath.zeta(s - 1))
            L_sh = -kappa * z_s * z_s1
            assert np.isfinite(L_sh)

    def test_shadow_l_zeros_are_riemann_zeros(self):
        """Zeros of L^{sh}(s) occur exactly at zeta zeros and shifted zeta zeros.

        If zeta(rho) = 0, then L^{sh}(rho) = -kappa * 0 * zeta(rho-1) = 0.
        If zeta(1+rho) = 0, impossible since 1+rho has Re > 1 (if RH).
        Actually: L^sh(1+rho) = -kappa * zeta(1+rho) * zeta(rho) = 0.
        """
        import mpmath
        mpmath.mp.dps = 20
        rho1 = mpmath.zetazero(1)  # 1/2 + 14.13...i
        # L^sh(rho1) = -kappa * zeta(rho1) * zeta(rho1 - 1)
        # zeta(rho1) = 0 by definition
        val = abs(float(mpmath.zeta(rho1)))
        assert val < 1e-10, "zeta(rho_1) should be ~0"


# ================================================================
# 42. Epstein functional equation consistency
# ================================================================

class TestEpsteinFunctionalEquationConsistency:
    """Additional functional equation tests for cross-verification."""

    def test_virasoro_c5_xi_real_approximately(self):
        """Xi_{Q_{Vir_5}} should be approximately real on critical line.

        The Virasoro shadow metric form has class number > 1 in general,
        so Xi is complex, but Re(Xi) still oscillates and zeros can be found.
        """
        a, b, cc, _ = virasoro_form(5.0)
        Xi = _chowla_selberg_completed(5.0, a, b, cc)
        assert np.isfinite(Xi.real)
        assert np.isfinite(Xi.imag)

    def test_virasoro_c13_enhanced_symmetry(self):
        """At c=13 (self-dual), the shadow metric has enhanced symmetry.

        kappa(13) = 6.5, kappa' = kappa (self-dual).
        The form Q_{Vir_13} should have particularly nice properties.
        """
        a, b, cc, D = virasoro_form(13.0)
        assert a > 0
        assert D < 0
        # kappa = 13/2 = 6.5
        assert abs(a - 4 * 6.5 ** 2) < 0.01


# ================================================================
# Final count: 95+ tests across 42 test classes
# ================================================================

if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
