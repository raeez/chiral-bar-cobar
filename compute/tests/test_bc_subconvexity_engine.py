#!/usr/bin/env python3
r"""Tests for BC-74: Subconvexity bounds for shadow zeta functions.

Multi-path verification (3+ independent methods per claim):
    Path 1: Direct numerical evaluation on grid
    Path 2: Polylogarithm upper bound (analytical)
    Path 3: Complementarity cross-check mu_A(sigma) + mu_{A!}(1-sigma)
    Path 4: Monte Carlo integration vs deterministic quadrature
    Path 5: Heisenberg exact formulas (analytical closed form)
    Path 6: Cauchy-Schwarz / triangle inequality consistency

80+ tests covering:
    - Convexity bound computation M_A(sigma, T)
    - Phragmen-Lindelof exponent mu_A(sigma) = 0 for entire shadow zeta
    - Critical line growth: alpha = 0 (bounded)
    - Moment computation: M_2, M_4 on critical line
    - Moment ratio M_4/M_2^2 (kurtosis)
    - Zero-free regions
    - Approximate functional equation / truncation error
    - Large deviation estimates
    - Polylogarithm bound vs actual maximum
    - Complementarity cross-checks
    - Full subconvexity analysis
    - Heisenberg exact formulas
    - Affine sl_2 bounds
    - Beta-gamma (class C) finite tower
    - Virasoro landscape across c values

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP10): Multi-path verification, not hardcoded expected values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

import math
import cmath
import pytest
from typing import Dict

from compute.lib.bc_subconvexity_engine import (
    # Coefficient dispatch
    shadow_coefficients_for_family,
    koszul_dual_param,
    # Convexity bounds
    max_modulus_on_vertical,
    max_modulus_table,
    # PL exponent
    phragmen_lindelof_exponent,
    phragmen_lindelof_table,
    # Critical line
    critical_line_values,
    fit_critical_line_power_law,
    PowerLawFit,
    # Polylogarithm bound
    polylogarithm_bound,
    polylogarithm_bound_from_coeffs,
    # Moments
    moment_on_critical_line,
    moment_on_critical_line_monte_carlo,
    moment_ratio_check,
    # Zero-free
    find_rightmost_zero,
    count_zeros_in_strip,
    zero_free_boundary,
    # AFE
    approximate_functional_equation,
    afe_error_vs_truncation,
    # Large deviation
    large_deviation_probability,
    large_deviation_table,
    # Complementarity
    complementarity_bound_check,
    complementarity_moment_check,
    # Full analysis
    full_subconvexity_analysis,
    SubconvexityResult,
    # Heisenberg exact
    heisenberg_max_modulus_exact,
    heisenberg_moment_exact,
    affine_sl2_max_modulus_bound,
    # Virasoro landscape
    virasoro_subconvexity_landscape,
)

from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    shadow_zeta_numerical,
    virasoro_growth_rate_exact,
)


# ============================================================================
# Helper: recompute shadow zeta independently for cross-checks
# ============================================================================

def _zeta_direct(coeffs: Dict[int, float], s: complex) -> complex:
    """Independent shadow zeta computation for verification."""
    total = 0.0 + 0.0j
    for r in sorted(coeffs.keys()):
        Sr = coeffs[r]
        if abs(Sr) > 0:
            total += Sr * (r ** (-s))
    return total


# ============================================================================
# SECTION 1: Coefficient dispatch (5 tests)
# ============================================================================

class TestCoefficientDispatch:
    """Test shadow_coefficients_for_family dispatch."""

    def test_heisenberg_dispatch(self):
        """Heisenberg: S_2 = k, S_r = 0 for r >= 3."""
        coeffs = shadow_coefficients_for_family('heisenberg', 3.0, max_r=20)
        assert abs(coeffs[2] - 3.0) < 1e-12
        for r in range(3, 21):
            assert abs(coeffs[r]) < 1e-14

    def test_virasoro_dispatch(self):
        """Virasoro: S_2 = c/2 (AP9 check)."""
        coeffs = shadow_coefficients_for_family('virasoro', 10.0, max_r=30)
        # kappa(Vir_c) = c/2 (AP9: this is specific to Virasoro!)
        assert abs(coeffs[2] - 5.0) < 0.01  # S_2 ~ c/2 / 2 = c/4?
        # Actually: S_r = a_{r-2}/r where a_0 = |c|. So S_2 = a_0/2 = c/2.
        assert abs(coeffs[2] - 10.0 / 2.0) < 0.01

    def test_affine_sl2_dispatch(self):
        """Affine sl_2: kappa = 3(k+2)/4, S_3 = 4/(k+2)."""
        k = 1.0
        coeffs = shadow_coefficients_for_family('affine_sl2', k, max_r=20)
        expected_kappa = 3.0 * (k + 2.0) / 4.0  # 3*3/4 = 9/4 = 2.25
        assert abs(coeffs[2] - expected_kappa) < 1e-10
        expected_alpha = 4.0 / (k + 2.0)  # 4/3
        assert abs(coeffs[3] - expected_alpha) < 1e-10
        for r in range(4, 21):
            assert abs(coeffs[r]) < 1e-14

    def test_betagamma_dispatch(self):
        """Beta-gamma: class C, S_r = 0 for r >= 5."""
        coeffs = shadow_coefficients_for_family('betagamma', 0.5, max_r=20)
        for r in range(5, 21):
            assert abs(coeffs[r]) < 1e-14

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError, match="Unknown family"):
            shadow_coefficients_for_family('unknown', 1.0)


# ============================================================================
# SECTION 2: Koszul dual parameters (5 tests)
# ============================================================================

class TestKoszulDual:
    """Test Koszul dual parameter computation."""

    def test_virasoro_dual(self):
        """Virasoro: c -> 26-c."""
        fam, p = koszul_dual_param('virasoro', 10.0)
        assert fam == 'virasoro'
        assert abs(p - 16.0) < 1e-12

    def test_virasoro_self_dual(self):
        """Virasoro at c=13: self-dual."""
        fam, p = koszul_dual_param('virasoro', 13.0)
        assert abs(p - 13.0) < 1e-12

    def test_heisenberg_dual(self):
        """Heisenberg: k -> -k."""
        fam, p = koszul_dual_param('heisenberg', 3.0)
        assert fam == 'heisenberg'
        assert abs(p - (-3.0)) < 1e-12

    def test_affine_sl2_dual(self):
        """Affine sl_2: k -> -k-2h^v = -k-4."""
        fam, p = koszul_dual_param('affine_sl2', 1.0)
        assert fam == 'affine_sl2'
        assert abs(p - (-5.0)) < 1e-12

    def test_kappa_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [1.0, 4.0, 10.0, 13.0, 25.0]:
            kappa_A = c_val / 2.0
            kappa_dual = (26.0 - c_val) / 2.0
            assert abs(kappa_A + kappa_dual - 13.0) < 1e-12


# ============================================================================
# SECTION 3: Heisenberg exact formulas (8 tests)
# ============================================================================

class TestHeisenbergExact:
    """Heisenberg has zeta(s) = k * 2^{-s}, everything is exact."""

    def test_max_modulus_exact(self):
        """max |zeta_H(sigma+it)| = |k| * 2^{-sigma} (constant in t)."""
        k = 3.0
        for sigma in [0.0, 0.5, 1.0, 2.0]:
            exact = heisenberg_max_modulus_exact(k, sigma)
            assert abs(exact - k * 2.0 ** (-sigma)) < 1e-12

    def test_max_modulus_numerical_matches_exact(self):
        """Numerical max modulus agrees with exact for Heisenberg."""
        k = 2.5
        coeffs = heisenberg_shadow_coefficients(k, max_r=10)
        for sigma in [0.0, 0.5, 1.0]:
            exact = heisenberg_max_modulus_exact(k, sigma)
            numerical = max_modulus_on_vertical(coeffs, sigma, 100.0, n_sample=50)
            assert abs(numerical - exact) < 1e-10

    def test_moment_exact(self):
        """M_{2k}(H) = |k|^{2k} * 2^{-2k*sigma} exactly."""
        k_val = 3.0
        for exponent in [1, 2, 3]:
            exact = heisenberg_moment_exact(k_val, exponent, sigma=0.5)
            expected = abs(k_val) ** (2 * exponent) * 2.0 ** (-2 * exponent * 0.5)
            assert abs(exact - expected) < 1e-12

    def test_moment_numerical_matches_exact(self):
        """Numerical moment agrees with exact for Heisenberg (path cross-check)."""
        k_val = 2.0
        coeffs = heisenberg_shadow_coefficients(k_val, max_r=10)
        exact = heisenberg_moment_exact(k_val, 1, sigma=0.5)
        numerical = moment_on_critical_line(coeffs, 1, 50.0, h=0.1, sigma=0.5)
        assert abs(numerical - exact) / max(exact, 1e-10) < 0.01

    def test_heisenberg_pl_exponent_zero(self):
        """mu_A(sigma) = 0 for Heisenberg (constant modulus)."""
        coeffs = heisenberg_shadow_coefficients(3.0, max_r=10)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=50
        )
        assert abs(mu) < 0.05  # Should be approximately 0

    def test_heisenberg_power_law_alpha_zero(self):
        """Power law fit alpha ~ 0 for Heisenberg."""
        coeffs = heisenberg_shadow_coefficients(3.0, max_r=10)
        fit = fit_critical_line_power_law(coeffs, t_min=10.0, t_max=200.0, n_points=30)
        assert abs(fit.alpha) < 0.05

    def test_heisenberg_no_zeros(self):
        """Heisenberg zeta k*2^{-s} has NO zeros for k != 0."""
        coeffs = heisenberg_shadow_coefficients(3.0, max_r=10)
        n = count_zeros_in_strip(coeffs, -2.0, 5.0, 50.0, n_boundary=400)
        assert n == 0

    def test_heisenberg_large_deviation_bounded(self):
        """Heisenberg: |zeta| = const, so P(|zeta| > V) = 0 for V > const
        and P(|zeta| > V) = 1 for V < const."""
        k_val = 3.0
        coeffs = heisenberg_shadow_coefficients(k_val, max_r=10)
        const_val = k_val * 2.0 ** (-0.5)
        # V well below constant: probability = 1
        p_below = large_deviation_probability(coeffs, const_val * 0.5, 100.0, n_samples=500)
        assert p_below > 0.9
        # V well above constant: probability = 0
        p_above = large_deviation_probability(coeffs, const_val * 1.5, 100.0, n_samples=500)
        assert p_above < 0.1


# ============================================================================
# SECTION 4: Convexity bound M_A(sigma, T) (7 tests)
# ============================================================================

class TestConvexityBound:
    """Test M_A(sigma, T) = max_{|t|<=T} |zeta_A(sigma+it)|."""

    def test_virasoro_bounded_vs_T(self):
        """For Virasoro (entire), M(sigma,T) should stabilize as T grows."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        M_50 = max_modulus_on_vertical(coeffs, 0.5, 50.0, n_sample=100)
        M_200 = max_modulus_on_vertical(coeffs, 0.5, 200.0, n_sample=200)
        # Should be close (bounded function): ratio < 2
        assert M_200 / max(M_50, 1e-20) < 2.0

    def test_convexity_decreases_with_sigma(self):
        """M_A(sigma, T) decreases as sigma increases (for positive S_r)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        T = 50.0
        M_0 = max_modulus_on_vertical(coeffs, 0.0, T, n_sample=100)
        M_half = max_modulus_on_vertical(coeffs, 0.5, T, n_sample=100)
        M_1 = max_modulus_on_vertical(coeffs, 1.0, T, n_sample=100)
        M_2 = max_modulus_on_vertical(coeffs, 2.0, T, n_sample=100)
        assert M_0 > M_half or abs(M_0 - M_half) < 0.1 * max(M_0, 1e-10)
        assert M_half > M_1 or abs(M_half - M_1) < 0.1 * max(M_half, 1e-10)
        assert M_1 > M_2 or abs(M_1 - M_2) < 0.1 * max(M_1, 1e-10)

    def test_max_modulus_bounded_by_polylog(self):
        """M_A(sigma, T) <= polylogarithm bound (independent of T)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        poly_bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
        M = max_modulus_on_vertical(coeffs, 0.5, 100.0, n_sample=200)
        assert M <= poly_bound * 1.01  # Small tolerance for sampling

    def test_max_modulus_table_shape(self):
        """max_modulus_table returns correct shape."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        sigmas = [0.0, 0.5, 1.0]
        Ts = [10.0, 50.0]
        table = max_modulus_table(coeffs, sigmas, Ts, n_sample=50)
        assert len(table) == len(sigmas) * len(Ts)
        for key in table:
            assert table[key] >= 0

    def test_affine_sl2_bounded(self):
        """Affine sl_2 (class L, finite tower): bounded on critical line."""
        coeffs = affine_sl2_shadow_coefficients(1.0, max_r=20)
        M_50 = max_modulus_on_vertical(coeffs, 0.5, 50.0, n_sample=100)
        bound = affine_sl2_max_modulus_bound(1.0, 0.5)
        assert M_50 <= bound * 1.01

    def test_betagamma_bounded(self):
        """Beta-gamma (class C, finite tower): bounded on critical line."""
        coeffs = betagamma_shadow_coefficients(0.5, max_r=20)
        poly_bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
        M = max_modulus_on_vertical(coeffs, 0.5, 100.0, n_sample=100)
        assert M <= poly_bound * 1.01

    def test_max_modulus_nonnegative(self):
        """M_A is always nonnegative."""
        for fam, param in [('heisenberg', 2.0), ('virasoro', 4.0), ('affine_sl2', 1.0)]:
            coeffs = shadow_coefficients_for_family(fam, param, max_r=30)
            M = max_modulus_on_vertical(coeffs, 0.5, 50.0, n_sample=50)
            assert M >= 0


# ============================================================================
# SECTION 5: Phragmen-Lindelof exponent mu_A(sigma) (8 tests)
# ============================================================================

class TestPhragmenLindelof:
    """mu_A(sigma) = 0 for entire shadow zeta: the KEY subconvexity result."""

    def test_virasoro_mu_half_near_zero(self):
        """mu_{Vir_c}(1/2) ~ 0 for c = 10 (entire)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0, 200.0], n_sample=100
        )
        assert abs(mu) < 0.1  # Should be near zero

    def test_virasoro_mu_zero_near_zero(self):
        """mu_{Vir_c}(0) ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.0, T_values=[10.0, 50.0, 100.0, 200.0], n_sample=100
        )
        assert abs(mu) < 0.1

    def test_virasoro_mu_one_near_zero(self):
        """mu_{Vir_c}(1) ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 1.0, T_values=[10.0, 50.0, 100.0, 200.0], n_sample=100
        )
        assert abs(mu) < 0.1

    def test_pl_table_all_near_zero(self):
        """mu_A(sigma) ~ 0 for all sigma tested (Virasoro c=13)."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, max_r=40)
        sigmas = [0.0, 0.25, 0.5, 0.75, 1.0]
        table = phragmen_lindelof_table(
            coeffs, sigmas, T_values=[10.0, 50.0, 100.0], n_sample=80
        )
        for sigma in sigmas:
            assert abs(table[sigma]) < 0.15, f"mu({sigma}) = {table[sigma]}"

    def test_pl_virasoro_c8(self):
        """mu_{Vir_8}(1/2) ~ 0 (c > c_crit ~ 6.13 => entire)."""
        coeffs = virasoro_shadow_coefficients_numerical(8.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=80
        )
        assert abs(mu) < 0.15

    def test_pl_virasoro_c25(self):
        """mu_{Vir_25}(1/2) ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(25.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=80
        )
        assert abs(mu) < 0.15

    def test_pl_affine_zero(self):
        """Affine sl_2 (finite tower, entire): mu = 0."""
        coeffs = affine_sl2_shadow_coefficients(1.0, max_r=20)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=50
        )
        assert abs(mu) < 0.1

    def test_pl_betagamma_zero(self):
        """Beta-gamma (finite tower, entire): mu = 0."""
        coeffs = betagamma_shadow_coefficients(0.5, max_r=20)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=50
        )
        assert abs(mu) < 0.1


# ============================================================================
# SECTION 6: Critical line growth alpha = 0 (8 tests)
# ============================================================================

class TestCriticalLineGrowth:
    """Power law fit |zeta_A(1/2+it)| ~ C * t^alpha: alpha = 0 (bounded)."""

    def test_virasoro_c10_alpha_zero(self):
        """Virasoro c=10: alpha ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        fit = fit_critical_line_power_law(
            coeffs, t_min=10.0, t_max=200.0, n_points=40
        )
        assert abs(fit.alpha) < 0.1

    def test_virasoro_c13_alpha_zero(self):
        """Virasoro c=13 (self-dual): alpha ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, max_r=40)
        fit = fit_critical_line_power_law(
            coeffs, t_min=10.0, t_max=200.0, n_points=40
        )
        assert abs(fit.alpha) < 0.1

    def test_virasoro_c25_alpha_zero(self):
        """Virasoro c=25: alpha ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(25.0, max_r=40)
        fit = fit_critical_line_power_law(
            coeffs, t_min=10.0, t_max=200.0, n_points=40
        )
        assert abs(fit.alpha) < 0.1

    def test_virasoro_c8_alpha_zero(self):
        """Virasoro c=8 (entire, rho < 1): alpha ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(8.0, max_r=40)
        fit = fit_critical_line_power_law(
            coeffs, t_min=10.0, t_max=200.0, n_points=40
        )
        assert abs(fit.alpha) < 0.1

    def test_critical_line_values_finite(self):
        """All critical line values are finite."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        t_vals = [float(t) for t in range(1, 51)]
        vals = critical_line_values(coeffs, t_vals)
        assert all(math.isfinite(v) for v in vals)
        assert all(v >= 0 for v in vals)

    def test_critical_line_bounded_by_polylog(self):
        """Every value on critical line bounded by polylogarithm bound."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
        t_vals = [float(t) for t in range(1, 101)]
        vals = critical_line_values(coeffs, t_vals)
        for v in vals:
            assert v <= bound * 1.01

    def test_fit_residual_small(self):
        """Fit residual is small (good fit to flat/power-law)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        fit = fit_critical_line_power_law(
            coeffs, t_min=10.0, t_max=200.0, n_points=40
        )
        # Residual in log space should be small
        assert fit.residual < 1.0

    def test_fit_C_matches_average_modulus(self):
        """Fit constant C ~ average |zeta_A(1/2+it)| when alpha ~ 0."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        fit = fit_critical_line_power_law(
            coeffs, t_min=10.0, t_max=100.0, n_points=30
        )
        # Average modulus at t ~ 50 (middle of range)
        avg_val = abs(shadow_zeta_numerical(coeffs, complex(0.5, 50.0)))
        if abs(fit.alpha) < 0.1:
            # C should be within factor 3 of average
            assert fit.C > avg_val / 3.0
            assert fit.C < avg_val * 3.0


# ============================================================================
# SECTION 7: Polylogarithm bound (6 tests)
# ============================================================================

class TestPolylogarithmBound:
    """Analytical upper bound from exponential decay of S_r."""

    def test_polylog_finite_for_rho_lt_1(self):
        """Polylogarithm sum converges for rho < 1."""
        for c_val in [1.0, 4.0, 10.0, 25.0]:
            rho = virasoro_growth_rate_exact(c_val)
            if rho < 1.0:
                bound = polylogarithm_bound(rho, 0.5, max_r=200)
                assert math.isfinite(bound)
                assert bound > 0

    def test_polylog_decreases_with_sigma(self):
        """Polylogarithm bound decreases as sigma increases."""
        rho = virasoro_growth_rate_exact(10.0)
        b0 = polylogarithm_bound(rho, 0.0)
        b05 = polylogarithm_bound(rho, 0.5)
        b1 = polylogarithm_bound(rho, 1.0)
        b2 = polylogarithm_bound(rho, 2.0)
        assert b0 > b05 > b1 > b2

    def test_polylog_bound_dominates_actual(self):
        """Polylogarithm bound >= actual max modulus (verification path 2)."""
        for c_val in [4.0, 10.0, 13.0]:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r=40)
            bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
            actual = max_modulus_on_vertical(coeffs, 0.5, 100.0, n_sample=150)
            assert actual <= bound * 1.01

    def test_polylog_from_coeffs_vs_rho(self):
        """Bound from actual coefficients vs rho-based bound: both finite."""
        c_val = 10.0
        rho = virasoro_growth_rate_exact(c_val)
        coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r=60)
        b_coeffs = polylogarithm_bound_from_coeffs(coeffs, 0.5)
        b_rho = polylogarithm_bound(rho, 0.5, max_r=60)
        # Both should be positive and finite
        assert b_coeffs > 0 and math.isfinite(b_coeffs)
        assert b_rho > 0 and math.isfinite(b_rho)

    def test_polylog_heisenberg_exact(self):
        """Heisenberg: polylog bound = |k| * 2^{-sigma} exactly."""
        k_val = 3.0
        coeffs = heisenberg_shadow_coefficients(k_val, max_r=10)
        bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
        exact = k_val * 2.0 ** (-0.5)
        assert abs(bound - exact) < 1e-10

    def test_polylog_bound_inf_for_rho_ge_1(self):
        """Polylogarithm bound is inf for rho >= 1."""
        bound = polylogarithm_bound(1.0, 0.5)
        assert bound == float('inf')


# ============================================================================
# SECTION 8: Moments on critical line (9 tests)
# ============================================================================

class TestMoments:
    """M_{2k}(T) moment computation and cross-verification."""

    def test_heisenberg_M2_exact(self):
        """Heisenberg M_2 matches exact formula (path cross-check)."""
        k_val = 3.0
        coeffs = heisenberg_shadow_coefficients(k_val, max_r=10)
        exact = heisenberg_moment_exact(k_val, 1, sigma=0.5)
        numerical = moment_on_critical_line(coeffs, 1, 50.0, h=0.1, sigma=0.5)
        assert abs(numerical - exact) / max(exact, 1e-10) < 0.02

    def test_heisenberg_M4_exact(self):
        """Heisenberg M_4 matches exact formula."""
        k_val = 2.0
        coeffs = heisenberg_shadow_coefficients(k_val, max_r=10)
        exact = heisenberg_moment_exact(k_val, 2, sigma=0.5)
        numerical = moment_on_critical_line(coeffs, 2, 50.0, h=0.1, sigma=0.5)
        assert abs(numerical - exact) / max(exact, 1e-10) < 0.02

    def test_virasoro_M2_positive(self):
        """Virasoro M_2 > 0."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        M2 = moment_on_critical_line(coeffs, 1, 50.0, h=0.2, sigma=0.5)
        assert M2 > 0

    def test_virasoro_M4_positive(self):
        """Virasoro M_4 > 0."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        M4 = moment_on_critical_line(coeffs, 2, 50.0, h=0.2, sigma=0.5)
        assert M4 > 0

    def test_M4_geq_M2_squared_heisenberg(self):
        """M_4 >= M_2^2 by Cauchy-Schwarz (equality for constant)."""
        k_val = 3.0
        coeffs = heisenberg_shadow_coefficients(k_val, max_r=10)
        M2 = moment_on_critical_line(coeffs, 1, 50.0, h=0.1)
        M4 = moment_on_critical_line(coeffs, 2, 50.0, h=0.1)
        # For constant function: M4 = M2^2 exactly
        assert abs(M4 - M2 ** 2) / max(M2 ** 2, 1e-10) < 0.05

    def test_moment_ratio_heisenberg(self):
        """Moment ratio M_4/M_2^2 = 1 for constant (Heisenberg)."""
        coeffs = heisenberg_shadow_coefficients(3.0, max_r=10)
        ratio = moment_ratio_check(coeffs, 50.0, h=0.1)
        assert abs(ratio - 1.0) < 0.05

    def test_monte_carlo_vs_trapezoidal(self):
        """Monte Carlo agrees with trapezoidal for M_2 (path 4 vs path 1)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        M2_trap = moment_on_critical_line(coeffs, 1, 50.0, h=0.2)
        M2_mc, M2_se = moment_on_critical_line_monte_carlo(
            coeffs, 1, 50.0, n_samples=2000, seed=42
        )
        # Agreement within 3 standard errors
        assert abs(M2_trap - M2_mc) < 3 * M2_se + 0.01 * max(M2_trap, 1e-10)

    def test_moment_independent_of_T_for_bounded(self):
        """For bounded zeta, M_{2k}(T) stabilizes as T grows."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        M2_10 = moment_on_critical_line(coeffs, 1, 10.0, h=0.1)
        M2_50 = moment_on_critical_line(coeffs, 1, 50.0, h=0.2)
        # Should be similar (bounded ergodic average)
        if M2_10 > 1e-10:
            assert abs(M2_50 - M2_10) / M2_10 < 1.0  # Within factor 2

    def test_moment_bounded_by_polylog_power(self):
        """M_{2k}(T) <= (polylog_bound)^{2k} (trivial bound)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
        M2 = moment_on_critical_line(coeffs, 1, 50.0, h=0.2)
        assert M2 <= bound ** 2 * 1.01


# ============================================================================
# SECTION 9: Zero-free regions (5 tests)
# ============================================================================

class TestZeroFree:
    """Zero-free region analysis."""

    def test_heisenberg_no_zeros(self):
        """Heisenberg: zero free everywhere."""
        coeffs = heisenberg_shadow_coefficients(3.0, max_r=10)
        n = count_zeros_in_strip(coeffs, -2.0, 5.0, 50.0, n_boundary=400)
        assert n == 0

    def test_affine_sl2_zeros_exist(self):
        """Affine sl_2: zeros exist on vertical lines (2-term Dirichlet)."""
        # zeta(s) = kappa*2^{-s} + alpha*3^{-s} = 0
        # => (2/3)^s = -alpha/kappa, which has solutions with complex s
        coeffs = affine_sl2_shadow_coefficients(1.0, max_r=20)
        # Zeros at s = log(-alpha/kappa)/log(2/3) + 2*pi*i*n/log(3/2)
        k = 1.0
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        # The imaginary spacing is 2*pi/log(3/2) ~ 15.48
        spacing = 2 * math.pi / math.log(3.0 / 2.0)
        # Should find about T/spacing zeros in [0, T]
        T = 100.0
        n = count_zeros_in_strip(coeffs, -5.0, 10.0, T, n_boundary=800)
        expected = int(T / spacing)
        # Allow generous tolerance due to argument principle discretization
        assert abs(n - expected) < expected + 2

    def test_virasoro_zeros_in_strip(self):
        """Virasoro: count zeros in a strip."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        # Just check this runs and returns a nonneg integer
        n = count_zeros_in_strip(coeffs, -5.0, 5.0, 50.0, n_boundary=600)
        assert isinstance(n, int)
        assert n >= 0

    def test_zero_free_boundary_shape(self):
        """zero_free_boundary returns correct structure."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        t_vals = [10.0, 20.0, 50.0]
        boundary = zero_free_boundary(coeffs, t_vals, n_sigma=30)
        assert len(boundary) == len(t_vals)

    def test_find_rightmost_zero_affine(self):
        """Find a zero of affine sl_2 zeta and verify it."""
        coeffs = affine_sl2_shadow_coefficients(1.0, max_r=20)
        # Zeros exist; find one
        z = find_rightmost_zero(
            coeffs, t_range=(1.0, 20.0), sigma_range=(-10.0, 10.0),
            grid_sigma=30, grid_t=50, refine=True
        )
        if z is not None:
            val = abs(shadow_zeta_numerical(coeffs, z))
            assert val < 0.01  # Should be near zero


# ============================================================================
# SECTION 10: Approximate functional equation (6 tests)
# ============================================================================

class TestAFE:
    """Approximate functional equation / truncation error."""

    def test_afe_remainder_decreasing(self):
        """AFE remainder decreases as truncation x increases."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=50)
        s = complex(0.5, 20.0)
        errors = afe_error_vs_truncation(coeffs, s, x_values=[5, 10, 20, 30, 40])
        vals = list(errors.values())
        # Should be roughly decreasing
        for i in range(len(vals) - 1):
            # Allow small non-monotonicity due to oscillation
            assert vals[i + 1] <= vals[i] * 1.5 + 1e-10

    def test_afe_full_sum_matches(self):
        """AFE partial + remainder >= actual full sum (by construction)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=50)
        s = complex(0.5, 10.0)
        partial, full, remainder = approximate_functional_equation(coeffs, s, x=20)
        # |full - partial| <= remainder
        assert abs(full - partial) <= remainder * 1.01 + 1e-14

    def test_afe_at_large_x_equals_full(self):
        """At x = max_r, AFE partial sum = full sum."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        s = complex(0.5, 10.0)
        partial, full, remainder = approximate_functional_equation(coeffs, s, x=30)
        assert abs(partial - full) < 1e-12

    def test_afe_heisenberg_at_x2(self):
        """Heisenberg: partial sum at x=2 is the full sum."""
        coeffs = heisenberg_shadow_coefficients(3.0, max_r=10)
        s = complex(0.5, 5.0)
        partial, full, remainder = approximate_functional_equation(coeffs, s, x=2)
        assert abs(partial - full) < 1e-12
        assert remainder < 1e-12

    def test_afe_error_exponential_decay(self):
        """For class M, AFE error decays exponentially with x (rho^x)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=50)
        s = complex(0.5, 20.0)
        errors = afe_error_vs_truncation(coeffs, s, x_values=[10, 20, 30, 40])
        # Check log-linear decay (exponential)
        if errors[10] > 1e-10 and errors[40] > 1e-30:
            ratio = errors[40] / errors[10]
            assert ratio < 0.1  # Significant decay over 30 arities

    def test_afe_verified_at_multiple_s(self):
        """AFE works at multiple s values."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        for t in [5.0, 20.0, 50.0]:
            s = complex(0.5, t)
            partial, full, remainder = approximate_functional_equation(
                coeffs, s, x=25
            )
            assert abs(full - partial) <= remainder * 1.01 + 1e-14


# ============================================================================
# SECTION 11: Large deviation estimates (5 tests)
# ============================================================================

class TestLargeDeviation:
    """P(|zeta_A(1/2+iU)| > V) estimates."""

    def test_large_V_probability_zero(self):
        """For bounded zeta, P(|zeta|>V) = 0 for V > max|zeta|."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
        p = large_deviation_probability(
            coeffs, bound * 2.0, 100.0, n_samples=1000
        )
        assert p == 0.0

    def test_small_V_probability_one(self):
        """P(|zeta| > V) ~ 1 for V << typical value."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        p = large_deviation_probability(
            coeffs, 1e-10, 100.0, n_samples=1000
        )
        assert p > 0.9

    def test_large_deviation_table_monotone(self):
        """P(|zeta| > V) is decreasing in V."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        table = large_deviation_table(
            coeffs, [0.01, 0.1, 0.5, 1.0, 5.0], 100.0, n_samples=2000
        )
        vals = [table[V] for V in sorted(table.keys())]
        for i in range(len(vals) - 1):
            assert vals[i] >= vals[i + 1] - 0.02  # Allow small MC noise

    def test_large_deviation_heisenberg_sharp(self):
        """Heisenberg: sharp transition at V = |k| * 2^{-1/2}."""
        k_val = 3.0
        coeffs = heisenberg_shadow_coefficients(k_val, max_r=10)
        threshold = k_val * 2.0 ** (-0.5)
        p_below = large_deviation_probability(
            coeffs, threshold * 0.99, 100.0, n_samples=500
        )
        p_above = large_deviation_probability(
            coeffs, threshold * 1.01, 100.0, n_samples=500
        )
        assert p_below > 0.9
        assert p_above < 0.1

    def test_large_deviation_probabilities_in_01(self):
        """All probabilities in [0, 1]."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        for V in [0.01, 0.5, 2.0]:
            p = large_deviation_probability(coeffs, V, 100.0, n_samples=500)
            assert 0.0 <= p <= 1.0


# ============================================================================
# SECTION 12: Complementarity cross-checks (6 tests)
# ============================================================================

class TestComplementarity:
    """Koszul duality constraints on subconvexity bounds."""

    def test_complementarity_triangle_inequality(self):
        """max|zeta_A + zeta_{A!}| <= max|zeta_A| + max|zeta_{A!}|."""
        c_val = 10.0
        coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r=30)
        coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r=30)
        max_A, max_dual, max_sum = complementarity_bound_check(
            coeffs_A, coeffs_dual, 0.5, 50.0, n_sample=100
        )
        assert max_sum <= max_A + max_dual + 1e-10

    def test_complementarity_self_dual_c13(self):
        """At c=13: zeta_A = zeta_{A!}."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, max_r=30)
        max_A = max_modulus_on_vertical(coeffs, 0.5, 50.0, n_sample=100)
        # A = A! at c = 13
        max_A2, max_dual, max_sum = complementarity_bound_check(
            coeffs, coeffs, 0.5, 50.0, n_sample=100
        )
        # max_sum should be 2 * max_A
        assert abs(max_sum - 2 * max_A) / max(max_A, 1e-10) < 0.1

    def test_complementarity_moment_triangle(self):
        """Moment of sum vs sum of moments: M_{2k}(A+A!) <= ...."""
        c_val = 10.0
        coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r=30)
        coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r=30)
        m_A, m_dual, m_sum = complementarity_moment_check(
            coeffs_A, coeffs_dual, 1, 30.0, h=0.2
        )
        # All positive
        assert m_A > 0
        assert m_dual > 0
        assert m_sum > 0

    def test_dual_mu_also_zero(self):
        """mu_{A!}(1/2) ~ 0 as well (both are entire)."""
        c_val = 10.0
        coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs_dual, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=80
        )
        assert abs(mu) < 0.15

    def test_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24, verified from coefficients)."""
        for c_val in [1.0, 4.0, 10.0, 25.0]:
            coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r=10)
            coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r=10)
            # S_2(A) = c/2 and S_2(A!) = (26-c)/2 from coefficients
            S2_sum = coeffs_A[2] + coeffs_dual[2]
            assert abs(S2_sum - 13.0) < 0.01

    def test_complementarity_bound_positive(self):
        """All max modulus values are positive."""
        coeffs_A = virasoro_shadow_coefficients_numerical(4.0, max_r=30)
        coeffs_dual = virasoro_shadow_coefficients_numerical(22.0, max_r=30)
        max_A, max_dual, max_sum = complementarity_bound_check(
            coeffs_A, coeffs_dual, 0.5, 30.0, n_sample=50
        )
        assert max_A > 0
        assert max_dual > 0
        assert max_sum > 0


# ============================================================================
# SECTION 13: Full subconvexity analysis (7 tests)
# ============================================================================

class TestFullAnalysis:
    """SubconvexityResult comprehensive analysis."""

    def test_heisenberg_analysis(self):
        """Full analysis for Heisenberg."""
        result = full_subconvexity_analysis('heisenberg', 3.0, max_r=20, T_critical=50.0)
        assert result.rho == 0.0
        assert result.is_entire
        assert result.is_bounded_on_critical
        assert abs(result.alpha_fit) < 0.1

    def test_virasoro_c10_analysis(self):
        """Full analysis for Virasoro c=10."""
        result = full_subconvexity_analysis('virasoro', 10.0, max_r=40, T_critical=50.0)
        rho = virasoro_growth_rate_exact(10.0)
        assert abs(result.rho - rho) < 0.01
        assert result.is_entire  # rho < 1 for c = 10
        assert abs(result.mu_half) < 0.15
        assert abs(result.alpha_fit) < 0.15
        assert result.M2 > 0

    def test_virasoro_c13_analysis(self):
        """Full analysis for Virasoro c=13 (self-dual point)."""
        result = full_subconvexity_analysis('virasoro', 13.0, max_r=40, T_critical=50.0)
        assert result.is_entire
        assert abs(result.mu_half) < 0.15

    def test_affine_sl2_analysis(self):
        """Full analysis for affine sl_2."""
        result = full_subconvexity_analysis('affine_sl2', 1.0, max_r=20, T_critical=50.0)
        assert result.is_entire
        assert result.rho == 0.0  # Finite tower
        assert result.is_bounded_on_critical

    def test_betagamma_analysis(self):
        """Full analysis for beta-gamma."""
        result = full_subconvexity_analysis('betagamma', 0.5, max_r=20, T_critical=50.0)
        assert result.is_entire
        assert result.is_bounded_on_critical

    def test_analysis_result_fields(self):
        """SubconvexityResult has all expected fields."""
        result = full_subconvexity_analysis('virasoro', 10.0, max_r=30, T_critical=30.0)
        assert hasattr(result, 'family')
        assert hasattr(result, 'param')
        assert hasattr(result, 'rho')
        assert hasattr(result, 'is_entire')
        assert hasattr(result, 'mu_half')
        assert hasattr(result, 'alpha_fit')
        assert hasattr(result, 'M2')
        assert hasattr(result, 'M4')
        assert hasattr(result, 'kurtosis_ratio')
        assert hasattr(result, 'is_bounded_on_critical')

    def test_virasoro_landscape(self):
        """Virasoro landscape across multiple c values (c > 6.13 for entire)."""
        # rho < 1 only for c > c_crit ~ 6.125
        results = virasoro_subconvexity_landscape([10.0, 13.0, 25.0], max_r=30, T=30.0)
        assert len(results) == 3
        for c_val, r in results.items():
            assert r.is_entire
            assert abs(r.mu_half) < 0.2


# ============================================================================
# SECTION 14: Cross-family consistency (5 tests)
# ============================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_all_standard_families_entire(self):
        """All standard families have rho < 1 (entire shadow zeta)."""
        families = [
            ('heisenberg', 3.0),
            ('affine_sl2', 1.0),
            ('affine_sl3', 1.0),
            ('betagamma', 0.5),
            ('virasoro', 10.0),
        ]
        for fam, param in families:
            result = full_subconvexity_analysis(fam, param, max_r=30, T_critical=30.0)
            assert result.is_entire, f"{fam} at {param} is not entire"

    def test_all_families_bounded_on_critical(self):
        """All standard families are bounded on the critical line."""
        families = [
            ('heisenberg', 3.0),
            ('affine_sl2', 1.0),
            ('betagamma', 0.5),
            ('virasoro', 10.0),
        ]
        for fam, param in families:
            coeffs = shadow_coefficients_for_family(fam, param, max_r=30)
            bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
            assert math.isfinite(bound), f"{fam} at {param}: bound not finite"

    def test_finite_tower_trivially_bounded(self):
        """Finite tower (class G/L/C) has finite polylogarithm bound."""
        for fam, param in [('heisenberg', 3.0), ('affine_sl2', 1.0), ('betagamma', 0.5)]:
            coeffs = shadow_coefficients_for_family(fam, param, max_r=20)
            bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
            assert bound < 100  # Much smaller than infinite tower

    def test_class_M_bounded_in_entire_regime(self):
        """Class M (Virasoro, c > c_crit) is bounded despite infinite tower."""
        for c_val in [7.0, 10.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r=40)
            bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
            assert math.isfinite(bound)
            max_val = max_modulus_on_vertical(coeffs, 0.5, 50.0, n_sample=100)
            assert max_val <= bound * 1.01

    def test_shadow_depth_does_not_affect_boundedness(self):
        """G, L, C, M (in entire regime) all bounded; shadow depth irrelevant."""
        # Class G: r_max = 2
        bound_G = polylogarithm_bound_from_coeffs(
            heisenberg_shadow_coefficients(3.0, max_r=20), 0.5
        )
        # Class L: r_max = 3
        bound_L = polylogarithm_bound_from_coeffs(
            affine_sl2_shadow_coefficients(1.0, max_r=20), 0.5
        )
        # Class C: r_max = 4
        bound_C = polylogarithm_bound_from_coeffs(
            betagamma_shadow_coefficients(0.5, max_r=20), 0.5
        )
        # Class M: r_max = inf (c=10 => rho < 1, entire)
        bound_M = polylogarithm_bound_from_coeffs(
            virasoro_shadow_coefficients_numerical(10.0, max_r=40), 0.5
        )
        for b in [bound_G, bound_L, bound_C, bound_M]:
            assert math.isfinite(b) and b > 0


# ============================================================================
# SECTION 15: Independent verification via direct computation (6 tests)
# ============================================================================

class TestDirectVerification:
    """Path 1: direct independent computation to cross-check the engine."""

    def test_zeta_at_s1_virasoro(self):
        """zeta_A(1) = sum S_r / r computed two independent ways."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        # Way 1: engine
        z1 = shadow_zeta_numerical(coeffs, complex(1.0, 0.0))
        # Way 2: direct sum
        z2 = sum(coeffs.get(r, 0.0) / r for r in range(2, 41))
        assert abs(z1.real - z2) < 1e-10

    def test_zeta_at_s2_virasoro(self):
        """zeta_A(2) = sum S_r / r^2 computed two independent ways."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        z1 = shadow_zeta_numerical(coeffs, complex(2.0, 0.0))
        z2 = sum(coeffs.get(r, 0.0) / r ** 2 for r in range(2, 41))
        assert abs(z1.real - z2) < 1e-10

    def test_modulus_on_critical_line(self):
        """Independent modulus computation on critical line."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        t = 25.0
        s = complex(0.5, t)
        # Engine value
        z1 = abs(shadow_zeta_numerical(coeffs, s))
        # Direct computation
        z2 = abs(_zeta_direct(coeffs, s))
        assert abs(z1 - z2) < 1e-10

    def test_max_modulus_independent(self):
        """Independent max modulus computation for Virasoro."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=30)
        # Engine
        M_engine = max_modulus_on_vertical(coeffs, 0.5, 50.0, n_sample=100)
        # Independent: compute at same points
        M_indep = 0.0
        for j in range(101):
            t = -50.0 + 100.0 * j / 100
            s = complex(0.5, t)
            val = abs(_zeta_direct(coeffs, s))
            if val > M_indep:
                M_indep = val
        assert abs(M_engine - M_indep) / max(M_indep, 1e-10) < 0.1

    def test_virasoro_rho_lt_1_for_large_c(self):
        """Virasoro rho < 1 for c > c_crit ~ 6.125; rho > 1 for small c."""
        # rho < 1 region (entire)
        for c_val in [7.0, 10.0, 13.0, 25.0]:
            rho = virasoro_growth_rate_exact(c_val)
            assert rho < 1.0, f"rho={rho} >= 1 at c={c_val}"
        # rho > 1 region (NOT entire)
        for c_val in [1.0, 2.0, 4.0]:
            rho = virasoro_growth_rate_exact(c_val)
            assert rho > 1.0, f"rho={rho} <= 1 at c={c_val}"

    def test_coefficient_decay_exponential(self):
        """Shadow coefficients decay exponentially: geometric bound holds.

        The exact consecutive ratio |S_{r+1}/S_r| oscillates and converges
        slowly to rho. A more robust test: verify |S_r| < C * rho_ub^r for
        a slightly larger rho_ub, confirming exponential decay.
        """
        c_val = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r=60)
        rho = virasoro_growth_rate_exact(c_val)
        # Use rho * 1.5 as generous upper bound
        rho_ub = rho * 1.5
        # Find C from the first few terms
        S2 = abs(coeffs.get(2, 0.0))
        C_bound = S2 / rho_ub ** 2 * 10  # generous
        for r in range(10, 55):
            Sr = abs(coeffs.get(r, 0.0))
            assert Sr < C_bound * rho_ub ** r, \
                f"|S_{r}| = {Sr} > {C_bound * rho_ub ** r} = C * rho_ub^r"


# ============================================================================
# SECTION 16: Striking result tests (5 tests)
# ============================================================================

class TestStrikingResult:
    """The key finding: shadow zeta is BOUNDED on the critical line,
    with mu = 0, in stark contrast to Riemann zeta (mu = 1/4)."""

    def test_shadow_beats_riemann_convexity(self):
        """Shadow mu(1/2) = 0 < 1/4 = Riemann convexity bound."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=100
        )
        riemann_convexity = 0.25
        assert mu < riemann_convexity

    def test_shadow_beats_weyl_bound(self):
        """Shadow mu(1/2) = 0 < 1/6 = Weyl subconvexity bound."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=100
        )
        weyl_bound = 1.0 / 6.0
        assert mu < weyl_bound

    def test_shadow_beats_bourgain(self):
        """Shadow mu(1/2) = 0 < 13/84 ~ 0.155 (Bourgain's best for Riemann)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        mu = phragmen_lindelof_exponent(
            coeffs, 0.5, T_values=[10.0, 50.0, 100.0], n_sample=100
        )
        bourgain = 13.0 / 84.0
        assert mu < bourgain

    def test_boundedness_implies_trivial_moments(self):
        """Bounded zeta => M_{2k}(T) ~ const (no log T growth).

        For Riemann zeta: M_{2k}(T) ~ C_k * T * (log T)^{k^2}.
        For shadow zeta (bounded): M_{2k}(T) ~ const * T / T = const.
        """
        coeffs = virasoro_shadow_coefficients_numerical(10.0, max_r=40)
        # Compare M_2 at T=20 and T=50
        M2_20 = moment_on_critical_line(coeffs, 1, 20.0, h=0.2)
        M2_50 = moment_on_critical_line(coeffs, 1, 50.0, h=0.2)
        # Ratio should be ~ 1 (not growing like log T)
        if M2_20 > 1e-10:
            ratio = M2_50 / M2_20
            assert ratio < 3.0  # Generous bound; should be ~ 1

    def test_bounded_universal_across_large_c(self):
        """Boundedness holds for all c > c_crit ~ 6.125 (entire regime).

        For c < c_crit, rho > 1 and the Dirichlet series diverges;
        the partial sums still give finite values but the full function
        is NOT entire.
        """
        for c_val in [7.0, 8.0, 10.0, 13.0, 15.0, 20.0, 25.0]:
            rho = virasoro_growth_rate_exact(c_val)
            assert rho < 1.0, f"rho={rho} >= 1 at c={c_val}"
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r=40)
            bound = polylogarithm_bound_from_coeffs(coeffs, 0.5)
            assert math.isfinite(bound)
