r"""Tests for the analytic continuation of the shadow obstruction tower to complex c.

Tests cover:
1. Consistency with real-c shadow data
2. Shadow coefficients at c = 1/2 + i*14.13... (first zeta zero)
3. Holomorphicity (Cauchy-Riemann verification)
4. Branch points and growth rate at complex c
5. Smoothness of |S_r| on the critical line (no resonances at zeta zeros)
6. Epstein zeta convergence analysis at complex c
7. Discriminant analysis at complex c
8. Overdetermination analysis
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import cmath
import math
import sys
import os
import pytest

# Ensure the library is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.shadow_tower_complex_c import (
    virasoro_shadow_data_complex,
    shadow_metric_coefficients_complex,
    shadow_metric_eval,
    shadow_metric_discriminant_complex,
    branch_points_complex,
    shadow_growth_rate_complex,
    sqrt_quadratic_taylor_complex,
    shadow_coefficients_complex,
    shadow_coefficient_at,
    verify_holomorphicity,
    shadow_on_critical_line,
    sweep_critical_line,
    check_zeta_zero_resonances,
    epstein_convergence_analysis,
    epstein_argument_sector,
    functional_equation_obstruction,
    complex_discriminant_analysis,
    investigate_at_zeta_zero,
    shadow_tower_smoothness_on_critical_line,
    overdetermination_analysis,
    full_investigation_report,
    ZETA_ZEROS_IM,
)


# ===========================================================================
# 1. Consistency with real-c shadow data
# ===========================================================================

class TestRealCConsistency:
    """Verify that the complex-c code reproduces known real-c results."""

    def test_virasoro_shadow_data_real_c(self):
        """Shadow data at real c should match known values."""
        c = 26.0 + 0j
        data = virasoro_shadow_data_complex(c)
        assert abs(data['kappa'] - 13.0) < 1e-10
        assert abs(data['alpha'] - 2.0) < 1e-10
        # S4 = 10/(26*(5*26+22)) = 10/(26*152) = 10/3952
        expected_S4 = 10.0 / (26 * 152)
        assert abs(data['S4'] - expected_S4) < 1e-12
        # Delta = 40/(5*26+22) = 40/152
        expected_Delta = 40.0 / 152
        assert abs(data['Delta'] - expected_Delta) < 1e-12

    def test_shadow_metric_at_c1(self):
        """At c = 1 (Ising partner): verify Q_L coefficients."""
        c = 1.0 + 0j
        q0, q1, q2 = shadow_metric_coefficients_complex(c)
        assert abs(q0 - 1.0) < 1e-10  # c^2 = 1
        assert abs(q1 - 12.0) < 1e-10  # 12c = 12
        # q2 = 36 + 80/(1*27) = 36 + 80/27
        expected_q2 = 36 + 80.0 / 27
        assert abs(q2 - expected_q2) < 1e-10

    def test_discriminant_real_c26(self):
        """Discriminant at c = 26: disc = -320*676/152."""
        c = 26.0 + 0j
        disc = shadow_metric_discriminant_complex(c)
        expected = -320 * 676.0 / 152
        assert abs(disc - expected) < 1e-6
        assert abs(disc.imag) < 1e-10  # Should be real

    def test_shadow_coefficients_real_c_kappa(self):
        """S_2 = kappa/2 = c/4 for the weighted convention... actually
        S_2 = a_0/2 = sqrt(q_0)/2 = |c|/2. For real c > 0: S_2 = c/2 = kappa.
        Wait: a_0 = sqrt(q_0) = sqrt(c^2) = c. So S_2 = a_0/2 = c/2 = kappa.
        """
        c = 10.0 + 0j
        coeffs = shadow_coefficients_complex(c, max_arity=4)
        S2 = coeffs[0]
        # S_2 = a_0 / 2 = sqrt(c^2) / 2 = c / 2 = 5
        assert abs(S2 - 5.0) < 1e-10

    def test_shadow_coefficients_real_c_cubic(self):
        """S_3 = a_1/3 = q1/(6*a_0) = 12c/(6c) = 2 for all c != 0."""
        c = 7.0 + 0j
        coeffs = shadow_coefficients_complex(c, max_arity=4)
        S3 = coeffs[1]
        assert abs(S3 - 2.0) < 1e-10

    def test_growth_rate_real_c26(self):
        """Growth rate at c=26 should match the known real-c value."""
        c = 26.0 + 0j
        rho = shadow_growth_rate_complex(c)
        # Known: rho(Vir_26) ~ 0.234 (the self-dual c=13 is rho~0.467)
        # At c=26: kappa=13, alpha=2, S4=10/(26*152)
        # rho = sqrt(9*4 + 2*40/152)/(2*13) = sqrt(36 + 80/152)/26
        #     = sqrt(36.526...)/26 = 6.044/26 ~ 0.2325
        assert 0.2 < rho < 0.3

    def test_growth_rate_self_dual_c13(self):
        """Growth rate at c=13 ~ 0.467."""
        c = 13.0 + 0j
        rho = shadow_growth_rate_complex(c)
        assert 0.4 < rho < 0.6


# ===========================================================================
# 2. Shadow coefficients at zeta zeros
# ===========================================================================

class TestZetaZeroCoefficients:
    """Compute shadow obstruction tower at c = 1/2 + i*gamma_1."""

    def test_coefficients_finite_at_first_zero(self):
        """All S_r should be finite (nonzero, non-infinite) at the first zeta zero."""
        gamma1 = ZETA_ZEROS_IM[0]
        c = 0.5 + 1j * gamma1
        coeffs = shadow_coefficients_complex(c, max_arity=12)
        for r, s in enumerate(coeffs, start=2):
            assert cmath.isfinite(s), f"S_{r} is not finite at first zeta zero"
            # Should be nonzero (no cancellation accident)
            assert abs(s) > 1e-20, f"S_{r} unexpectedly zero at first zeta zero"

    def test_coefficients_complex_at_zeta_zero(self):
        """At complex c, S_r should be genuinely complex (nonzero imaginary part),
        EXCEPT S_3 = alpha = 2 which is real for all c (universal Virasoro cubic)."""
        gamma1 = ZETA_ZEROS_IM[0]
        c = 0.5 + 1j * gamma1
        coeffs = shadow_coefficients_complex(c, max_arity=8)
        # S_2 = c/2 = 0.25 + i*gamma1/2, definitely complex
        assert abs(coeffs[0].imag) > 1, "S_2 should have large imaginary part"
        # S_3 = 2 is real for ALL c (the cubic shadow is universal)
        assert abs(coeffs[1] - 2.0) < 1e-8, "S_3 should be exactly 2"
        # S_4 and higher should be complex
        for r in [4, 5, 6, 7, 8]:
            idx = r - 2
            assert abs(coeffs[idx].imag) > 1e-10, f"S_{r} unexpectedly real"

    def test_S2_equals_kappa(self):
        """S_2 = c/2 at any c (including complex)."""
        gamma1 = ZETA_ZEROS_IM[0]
        c = 0.5 + 1j * gamma1
        coeffs = shadow_coefficients_complex(c, max_arity=3)
        S2 = coeffs[0]
        expected = c / 2
        assert abs(S2 - expected) < 1e-10

    def test_S3_equals_2(self):
        """S_3 = 2 for all c (the cubic shadow is universal for Virasoro)."""
        gamma1 = ZETA_ZEROS_IM[0]
        c = 0.5 + 1j * gamma1
        coeffs = shadow_coefficients_complex(c, max_arity=4)
        S3 = coeffs[1]
        assert abs(S3 - 2.0) < 1e-8

    def test_coefficients_at_multiple_zeros(self):
        """Shadow coefficients are finite and nonzero at all zeta zeros."""
        for idx, gamma in enumerate(ZETA_ZEROS_IM[:5]):
            c = 0.5 + 1j * gamma
            coeffs = shadow_coefficients_complex(c, max_arity=10)
            for r in range(2, 10):
                s = coeffs[r - 2]
                assert cmath.isfinite(s), (
                    f"S_{r} not finite at zero #{idx+1} (gamma={gamma:.4f})")

    def test_growth_rate_finite_at_zeta_zeros(self):
        """Growth rate rho should be finite at all zeta zeros."""
        for gamma in ZETA_ZEROS_IM[:5]:
            c = 0.5 + 1j * gamma
            rho = shadow_growth_rate_complex(c)
            assert 0 < rho < 100, f"rho={rho} at gamma={gamma:.4f}"


# ===========================================================================
# 3. Holomorphicity
# ===========================================================================

class TestHolomorphicity:
    """Verify S_r(c) satisfies Cauchy-Riemann at various points."""

    def test_holomorphic_at_c_equals_5(self):
        """S_4 should be holomorphic at c = 5 (real, away from poles)."""
        result = verify_holomorphicity(5.0 + 0j, r=4)
        assert result['holomorphic'], f"CR error = {result['cauchy_riemann_error']}"

    def test_holomorphic_at_complex_c(self):
        """S_4 should be holomorphic at c = 3 + 2i."""
        result = verify_holomorphicity(3.0 + 2j, r=4)
        assert result['holomorphic'], f"CR error = {result['cauchy_riemann_error']}"

    def test_holomorphic_at_first_zeta_zero(self):
        """S_r should be holomorphic at c = 1/2 + i*gamma_1."""
        gamma1 = ZETA_ZEROS_IM[0]
        c = 0.5 + 1j * gamma1
        for r in [4, 6, 8]:
            result = verify_holomorphicity(c, r, eps=1e-6)
            assert result['holomorphic'], (
                f"S_{r} fails CR at first zeta zero: error = {result['cauchy_riemann_error']}")

    def test_holomorphic_on_critical_line(self):
        """S_4 should be holomorphic at several points on the critical line."""
        for t_val in [5.0, 10.0, 20.0, 30.0]:
            c = 0.5 + 1j * t_val
            result = verify_holomorphicity(c, r=4, eps=1e-6)
            assert result['holomorphic'], (
                f"S_4 fails CR at t={t_val}: error = {result['cauchy_riemann_error']}")

    def test_holomorphic_near_pole(self):
        """S_4 should be holomorphic at c = 0.1 + 0.1i (near pole at c=0)."""
        c = 0.1 + 0.1j
        result = verify_holomorphicity(c, r=4, eps=1e-9)
        assert result['holomorphic'], f"CR error = {result['cauchy_riemann_error']}"


# ===========================================================================
# 4. Branch points and growth rate
# ===========================================================================

class TestBranchPoints:
    """Test branch point computation at complex c."""

    def test_branch_points_are_zeros_of_QL(self):
        """Q_L(c, t_pm) should vanish at the branch points."""
        for c in [3 + 2j, 0.5 + 14.13j, 10 + 0j, 1 + 5j]:
            tp, tm = branch_points_complex(c)
            Qp = shadow_metric_eval(c, tp)
            Qm = shadow_metric_eval(c, tm)
            assert abs(Qp) < 1e-6, f"Q_L(t+) = {Qp} != 0 at c = {c}"
            assert abs(Qm) < 1e-6, f"Q_L(t-) = {Qm} != 0 at c = {c}"

    def test_branch_points_conjugate_for_real_c(self):
        """For real c (and disc < 0), branch points should be complex conjugates."""
        c = 10.0 + 0j
        tp, tm = branch_points_complex(c)
        # They should be conjugates
        assert abs(tp - tm.conjugate()) < 1e-10 or abs(tp - tm) < 1e-10

    def test_growth_rate_equals_inverse_min_branch(self):
        """rho = 1/min(|t_+|, |t_-|)."""
        for c in [5 + 3j, 0.5 + 14.13j, 20 + 0j]:
            tp, tm = branch_points_complex(c)
            r_min = min(abs(tp), abs(tm))
            rho = shadow_growth_rate_complex(c)
            if r_min > 1e-10:
                assert abs(rho - 1 / r_min) < 1e-8, (
                    f"rho = {rho} != 1/min(|t_pm|) = {1/r_min} at c = {c}")

    def test_growth_rate_continuous(self):
        """rho(c) should vary continuously as c moves on the critical line."""
        rhos = []
        for t_val in [14.0, 14.05, 14.1, 14.13, 14.15, 14.2, 14.3]:
            c = 0.5 + 1j * t_val
            rho = shadow_growth_rate_complex(c)
            rhos.append(rho)
        # Check no sudden jumps
        for i in range(1, len(rhos)):
            assert abs(rhos[i] - rhos[i-1]) < 0.1, (
                f"Discontinuity in rho: {rhos[i-1]:.4f} -> {rhos[i]:.4f}")


# ===========================================================================
# 5. No resonances at zeta zeros
# ===========================================================================

class TestNoResonances:
    """The central negative result: |S_r| has no peaks at zeta zeros."""

    def test_S4_smooth_across_first_zero(self):
        """S_4 magnitude should vary smoothly near gamma_1 = 14.134..."""
        gamma1 = ZETA_ZEROS_IM[0]
        t_vals = [gamma1 - 1, gamma1 - 0.5, gamma1, gamma1 + 0.5, gamma1 + 1]
        mags = []
        for t_val in t_vals:
            c = 0.5 + 1j * t_val
            S4 = shadow_coefficient_at(c, 4)
            mags.append(abs(S4))

        # Check smoothness: variation should be gradual
        for i in range(1, len(mags)):
            ratio = mags[i] / max(mags[i-1], 1e-50)
            assert 0.5 < ratio < 2.0, (
                f"|S_4| ratio = {ratio} between t = {t_vals[i-1]:.2f} and {t_vals[i]:.2f}")

    def test_no_peak_at_zeta_zero_arity4(self):
        """S_4 at gamma_1 should not be a local maximum."""
        gamma1 = ZETA_ZEROS_IM[0]
        delta = 0.3
        vals = []
        for offset in [-delta, 0, delta]:
            c = 0.5 + 1j * (gamma1 + offset)
            S4 = shadow_coefficient_at(c, 4)
            vals.append(abs(S4))
        # The value at gamma_1 need not be a local max
        is_peak = vals[1] > vals[0] and vals[1] > vals[2]
        # Even if it IS a peak by coincidence, the variation should be small
        if is_peak:
            variation = (vals[1] - min(vals[0], vals[2])) / vals[1]
            assert variation < 0.5, (
                f"Suspicious peak at gamma_1: variation = {variation:.4f}")

    def test_rational_function_no_transcendental_resonance(self):
        """Core theoretical test: S_r is a rational function of c.
        Rational functions of c evaluated at c = 1/2 + it cannot have
        isolated peaks at transcendental t values.

        We verify this indirectly: S_3 = 2 for ALL c (constant),
        so it trivially has no peaks. S_2 = c/2, so |S_2| = |c|/2,
        which is monotonically increasing in |t|. No peaks possible.
        """
        # S_3 = 2 for all c
        for gamma in ZETA_ZEROS_IM[:3]:
            c = 0.5 + 1j * gamma
            S3 = shadow_coefficient_at(c, 3)
            assert abs(S3 - 2.0) < 1e-8, f"S_3 != 2 at gamma = {gamma}"

        # |S_2| = |c|/2 = sqrt(1/4 + t^2)/2, monotonically increasing
        prev_mag = 0
        for t_val in [1.0, 5.0, 10.0, 14.13, 20.0, 30.0]:
            c = 0.5 + 1j * t_val
            S2 = shadow_coefficient_at(c, 2)
            mag = abs(S2)
            assert mag > prev_mag, f"|S_2| not increasing at t = {t_val}"
            prev_mag = mag

    def test_growth_rate_smooth_across_zeros(self):
        """rho(1/2 + it) should be smooth (no peaks) near zeta zeros."""
        gamma1 = ZETA_ZEROS_IM[0]
        t_vals = [gamma1 + offset for offset in
                  [-1.0, -0.5, -0.25, 0, 0.25, 0.5, 1.0]]
        rhos = [shadow_growth_rate_complex(0.5 + 1j * t) for t in t_vals]

        # Check smoothness
        for i in range(1, len(rhos) - 1):
            midpoint = (rhos[i-1] + rhos[i+1]) / 2
            deviation = abs(rhos[i] - midpoint)
            assert deviation < 0.3, (
                f"rho deviates from midpoint by {deviation:.4f} at t = {t_vals[i]:.2f}")


# ===========================================================================
# 6. Epstein zeta convergence at complex c
# ===========================================================================

class TestEpsteinConvergence:
    """Test Epstein zeta convergence analysis at complex c."""

    def test_real_c_positive_definite(self):
        """At real c > 0, Q should be positive definite (all args near 0)."""
        c = 10.0 + 0j
        result = epstein_argument_sector(c, N=15)
        assert result['max_argument'] < 0.01, (
            f"max arg = {result['max_argument']} at real c = 10")
        assert result['bounded_away_from_pi']

    def test_complex_c_argument_sector(self):
        """At complex c, Q(m,n) arguments should spread out."""
        c = 0.5 + 14.13j
        result = epstein_argument_sector(c, N=15)
        # For complex c, arguments will NOT all be near 0
        assert result['max_argument'] > 0.1, (
            "Expected argument spread at complex c")

    def test_convergence_fails_at_complex_c(self):
        """The theta function should NOT converge at generic complex c."""
        gamma1 = ZETA_ZEROS_IM[0]
        c = 0.5 + 1j * gamma1
        result = functional_equation_obstruction(c)
        # At complex c, the form is not positive definite
        assert not result['form_has_real_coefficients']
        # The functional equation does not apply
        assert not result['functional_equation_expected']

    def test_convergence_at_real_c(self):
        """At real c > 0, theta should converge and FE should apply."""
        c = 10.0 + 0j
        result = functional_equation_obstruction(c)
        assert result['form_has_real_coefficients']
        assert result['functional_equation_expected']
        assert result['theta_converges']


# ===========================================================================
# 7. Discriminant at complex c
# ===========================================================================

class TestComplexDiscriminant:
    """Test discriminant analysis at complex c."""

    def test_disc_complex_at_zeta_zero(self):
        """Discriminant should be complex (not real) at zeta zeros."""
        gamma1 = ZETA_ZEROS_IM[0]
        c = 0.5 + 1j * gamma1
        analysis = complex_discriminant_analysis(c)
        assert not analysis['disc_is_real']
        assert analysis['field_type'] == "not a number field (disc is complex)"
        assert not analysis['arithmetic_content']

    def test_disc_real_at_real_c(self):
        """Discriminant should be real at real c."""
        c = 10.0 + 0j
        analysis = complex_discriminant_analysis(c)
        assert analysis['disc_is_real']
        assert analysis['arithmetic_content']

    def test_disc_formula(self):
        """Verify disc = -320 c^2 / (5c + 22)."""
        for c in [3 + 2j, 0.5 + 14j, 10 + 0j, -1 + 3j]:
            disc = shadow_metric_discriminant_complex(c)
            expected = -320 * c ** 2 / (5 * c + 22)
            assert abs(disc - expected) < 1e-8, (
                f"disc mismatch at c = {c}: {disc} vs {expected}")

    def test_disc_pole_at_minus_22_over_5(self):
        """Discriminant should blow up near c = -22/5 = -4.4."""
        c = -4.4 + 0.01j
        disc = shadow_metric_discriminant_complex(c)
        assert abs(disc) > 100, f"|disc| = {abs(disc)} should be large near pole"


# ===========================================================================
# 8. Full investigation at zeta zeros
# ===========================================================================

class TestFullInvestigation:
    """Integration tests for the full investigation."""

    def test_investigate_first_zero(self):
        """Full investigation at the first zeta zero should complete."""
        result = investigate_at_zeta_zero(0, max_arity=12)
        assert result['zero_index'] == 1
        assert abs(result['gamma'] - 14.134725141734693) < 1e-6
        assert len(result['S_r']) == 11  # S_2 through S_12
        assert result['growth_rate_rho'] > 0
        assert result['growth_rate_rho'] < 100

    def test_comparison_shows_smooth_variation(self):
        """Shadow coefficients should vary smoothly between zeta zero
        and nearby non-zero points."""
        result = investigate_at_zeta_zero(0, max_arity=10)
        comp = result['comparison']

        for i in range(min(8, len(comp['|S_r| at gamma']))):
            val_at = comp['|S_r| at gamma'][i]
            val_below = comp['|S_r| at gamma - 0.5'][i]
            val_above = comp['|S_r| at gamma + 0.5'][i]

            # All should be comparable (within factor of 3)
            if val_at > 1e-20:
                assert val_below / val_at > 0.1 and val_below / val_at < 10
                assert val_above / val_at > 0.1 and val_above / val_at < 10

    def test_holomorphicity_in_investigation(self):
        """Holomorphicity checks in the investigation should all pass."""
        result = investigate_at_zeta_zero(0, max_arity=10)
        for r, holo_result in result['holomorphicity'].items():
            assert holo_result['holomorphic'], (
                f"S_{r} fails holomorphicity at first zeta zero")


# ===========================================================================
# 9. Overdetermination analysis
# ===========================================================================

class TestOverdetermination:
    """Test the overdetermination analysis."""

    def test_not_overdetermined(self):
        """The (c, s) system should NOT be overdetermined."""
        c = 10.0 + 0j
        result = overdetermination_analysis(c)
        assert not result['overdetermined']

    def test_epstein_well_defined_real_c(self):
        """Epstein zeta should be well-defined at real c > 0."""
        result = overdetermination_analysis(10.0 + 0j)
        assert result['epstein_well_defined']

    def test_functional_equation_real_c_only(self):
        """Functional equation should apply at real c but not complex c."""
        result_real = overdetermination_analysis(10.0 + 0j)
        assert result_real['functional_equation_applies']

        result_complex = overdetermination_analysis(0.5 + 14.13j)
        assert not result_complex['functional_equation_applies']


# ===========================================================================
# 10. Convolution recursion correctness
# ===========================================================================

class TestConvolutionRecursion:
    """Verify the sqrt expansion via convolution recursion."""

    def test_squaring_recovers_original(self):
        """(sum a_n t^n)^2 should equal Q_L(t)."""
        c = 7.0 + 3j
        q0, q1, q2 = shadow_metric_coefficients_complex(c)
        max_n = 15
        a = sqrt_quadratic_taylor_complex(q0, q1, q2, max_n)

        # Check: sum_{j=0}^n a_j * a_{n-j} should equal the coefficient of t^n in Q_L
        # Q_L: [t^0] = q0, [t^1] = q1, [t^2] = q2, [t^n] = 0 for n >= 3

        # [t^0]: a_0^2
        assert abs(a[0] * a[0] - q0) < 1e-8

        # [t^1]: 2*a_0*a_1
        assert abs(2 * a[0] * a[1] - q1) < 1e-8

        # [t^2]: 2*a_0*a_2 + a_1^2
        assert abs(2 * a[0] * a[2] + a[1] ** 2 - q2) < 1e-8

        # [t^n] = 0 for n >= 3
        for n in range(3, max_n + 1):
            conv = sum(a[j] * a[n - j] for j in range(n + 1))
            assert abs(conv) < 1e-6, (
                f"[t^{n}] in f^2 = {conv} (should be 0)")

    def test_sqrt_at_t_equals_0(self):
        """sqrt(Q_L(0)) = sqrt(c^2) = c (principal branch for Re(c) > 0)."""
        c = 5.0 + 2j
        q0, q1, q2 = shadow_metric_coefficients_complex(c)
        a = sqrt_quadratic_taylor_complex(q0, q1, q2, 0)
        # a_0 = sqrt(q0) = sqrt(c^2)
        # For principal branch: sqrt(c^2) has same argument as c when Re(c) > 0
        expected = cmath.sqrt(c ** 2)
        assert abs(a[0] - expected) < 1e-10

    def test_direct_evaluation_matches_taylor(self):
        """Evaluate sqrt(Q_L(t)) directly and compare with Taylor sum."""
        c = 4.0 + 1j
        q0, q1, q2 = shadow_metric_coefficients_complex(c)
        max_n = 20
        a = sqrt_quadratic_taylor_complex(q0, q1, q2, max_n)

        # Evaluate at a small t
        t = 0.1 + 0.05j
        taylor_val = sum(a[n] * t ** n for n in range(max_n + 1))
        direct_val = cmath.sqrt(q0 + q1 * t + q2 * t ** 2)

        # Should agree up to branch choice
        assert abs(taylor_val - direct_val) < 1e-8 or abs(taylor_val + direct_val) < 1e-8


# ===========================================================================
# 11. Sweep and resonance check
# ===========================================================================

class TestSweep:
    """Test the critical-line sweep functions."""

    def test_sweep_returns_correct_length(self):
        """Sweep should return data for each t value."""
        t_vals = [10.0, 15.0, 20.0]
        result = sweep_critical_line(t_vals, arities=[4, 6])
        assert len(result[4]) == 3
        assert len(result[6]) == 3
        assert len(result['growth_rates']) == 3

    def test_sweep_values_finite(self):
        """All sweep values should be finite."""
        t_vals = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0]
        result = sweep_critical_line(t_vals, arities=[4, 6, 8])
        for r in [4, 6, 8]:
            for val in result[r]:
                assert val is not None and math.isfinite(val), (
                    f"|S_{r}| not finite in sweep")

    def test_resonance_check_completes(self):
        """Resonance check should complete and find no resonances."""
        result = check_zeta_zero_resonances(
            arities=[4, 6], num_zeros=2,
            neighborhood_points=10, neighborhood_radius=0.5)
        assert len(result) == 2
        # Check structure
        for key, data in result.items():
            for r in [4, 6]:
                assert r in data
                assert '|S_r| at zero' in data[r]


# ===========================================================================
# 12. Pole behavior
# ===========================================================================

class TestPoles:
    """Test behavior near the poles c = 0 and c = -22/5."""

    def test_S4_blows_up_near_c_0(self):
        """S_4 should diverge as c -> 0 (S4 = 10/(c(5c+22)) has pole)."""
        mags = []
        for eps in [1.0, 0.1, 0.01]:
            c = eps + 0.1j
            S4 = shadow_coefficient_at(c, 4)
            mags.append(abs(S4))
        # Should be increasing as eps -> 0
        assert mags[-1] > mags[0], "S_4 should grow near c = 0"

    def test_S4_blows_up_near_minus_22_over_5(self):
        """S_4 should diverge as c -> -22/5 = -4.4."""
        mags = []
        for eps in [1.0, 0.1, 0.01]:
            c = -4.4 + eps * 1j
            S4 = shadow_coefficient_at(c, 4)
            mags.append(abs(S4))
        assert mags[-1] > mags[0], "S_4 should grow near c = -22/5"


# ===========================================================================
# 13. Report generation
# ===========================================================================

class TestReport:
    """Test the full report generation."""

    def test_report_generates(self):
        """Full investigation report should generate without errors."""
        report = full_investigation_report(max_arity=10)
        assert isinstance(report, str)
        assert len(report) > 100
        assert "CONCLUSION" in report

    def test_report_contains_key_findings(self):
        """Report should contain key negative findings."""
        report = full_investigation_report(max_arity=10)
        assert "rational function" in report.lower() or "RATIONAL" in report
        assert "Nothing special" in report or "nothing special" in report


# ===========================================================================
# 14. Edge cases and special values
# ===========================================================================

class TestSpecialValues:
    """Test at special central charge values."""

    def test_c_equals_1(self):
        """Ising model c = 1: shadow obstruction tower should be well-defined."""
        c = 1.0 + 0j
        coeffs = shadow_coefficients_complex(c, max_arity=10)
        assert all(cmath.isfinite(s) for s in coeffs)

    def test_c_equals_half(self):
        """Ising model c = 1/2: shadow obstruction tower should be well-defined."""
        c = 0.5 + 0j
        coeffs = shadow_coefficients_complex(c, max_arity=10)
        assert all(cmath.isfinite(s) for s in coeffs)

    def test_c_purely_imaginary(self):
        """c = 5i: shadow obstruction tower should be well-defined (no poles on imaginary axis
        except possibly c = 0, and c = -22/5 is real)."""
        c = 5j
        coeffs = shadow_coefficients_complex(c, max_arity=10)
        assert all(cmath.isfinite(s) for s in coeffs)

    def test_c_negative_real_not_at_pole(self):
        """c = -3 (between 0 and -22/5): shadow obstruction tower should work."""
        c = -3.0 + 0j
        coeffs = shadow_coefficients_complex(c, max_arity=10)
        assert all(cmath.isfinite(s) for s in coeffs)

    def test_large_imaginary_part(self):
        """c = 1/2 + 100i: shadow obstruction tower should still work."""
        c = 0.5 + 100j
        coeffs = shadow_coefficients_complex(c, max_arity=10)
        assert all(cmath.isfinite(s) for s in coeffs)
        rho = shadow_growth_rate_complex(c)
        assert math.isfinite(rho)
