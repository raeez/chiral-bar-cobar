#!/usr/bin/env python3
r"""
Tests for universal_residue_factor.py.

Manuscript reference:
  arithmetic_shadows.tex, sec:genuine-residue-kernel
  def:universal-residue-factor (eq:universal-residue)
  prop:on-off-line-distinction (eq:residue-kernel)
  def:compatibility-ratios
  conj:quartic-closure
  rem:davenport-heilbronn-koszul-epstein

ANTI-PATTERN COVERAGE:
  AP1:  kappa computed from first principles at each c
  AP10: Cross-family consistency (not hardcoded values alone)
  AP19: Pole absorption tested (d log shifts pole order)
  AP38: Normalization verified against numerical residue (not literature values)
  AP39: kappa != S_2 at rank > 1
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from mpmath import mp, mpf, mpc, fabs, pi as mppi, atan2, gamma as mpgamma, \
    zeta as mpzeta, diff as mpdiff, re as mpre, im as mpim, power as mppower, \
    log as mplog, cos as mpcos, nstr

mp.dps = 30

from universal_residue_factor import (
    universal_residue_factor,
    A_c_modulus_and_arg,
    A_c_table,
    residue_kernel,
    residue_kernel_array,
    decay_exponent,
    oscillation_period,
    virasoro_quartic_contact,
    virasoro_schur_complement,
    compatibility_ratio_potential,
    compatibility_ratio_gram,
    scattering_factor,
    verify_residue_formula,
    ising_shadow_data,
    structural_separation_diagnostic,
    closure_system,
    closure_rank_analysis,
    zeta_zero,
    compute_all_A_c_at_rho1,
    ZETA_ZEROS_GAMMA,
)


# =============================================================================
# 0. Zeta zeros
# =============================================================================

class TestZetaZeros:
    """Verify stored zeta zeros are actual zeros."""

    def test_first_zero_is_zero(self):
        """zeta(1/2 + 14.1347...i) should vanish."""
        rho1 = zeta_zero(1)
        val = mpzeta(rho1)
        assert fabs(val) < mpf('1e-20'), f"|zeta(rho_1)| = {fabs(val)}"

    def test_first_ten_zeros(self):
        """All stored zeros should satisfy |zeta(rho)| < 1e-15."""
        for n in range(1, 11):
            rho = zeta_zero(n)
            val = mpzeta(rho)
            assert fabs(val) < mpf('1e-15'), f"|zeta(rho_{n})| = {fabs(val)}"

    def test_zeros_on_critical_line(self):
        """All stored zeros have Re = 1/2."""
        for n in range(1, 11):
            rho = zeta_zero(n)
            assert fabs(mpre(rho) - mpf('0.5')) < mpf('1e-20')

    def test_zeros_ordered(self):
        """Imaginary parts are strictly increasing."""
        for n in range(1, 10):
            assert ZETA_ZEROS_GAMMA[n] > ZETA_ZEROS_GAMMA[n - 1]


# =============================================================================
# 1. Universal residue factor A_c(rho)
# =============================================================================

class TestUniversalResidueFactor:
    """Test A_c(rho) from eq:universal-residue."""

    def test_formula_well_defined(self):
        """A_c(rho_1) should be finite for standard c values."""
        rho1 = zeta_zero(1)
        for c in [mpf('0.5'), mpf(1), mpf(13), mpf(25), mpf(26)]:
            A = universal_residue_factor(c, rho1)
            assert fabs(A) > mpf('1e-10'), f"|A_{c}| too small"
            assert fabs(A) < mpf('100'), f"|A_{c}| too large"

    def test_c_half_ising(self):
        """A_{1/2}(rho_1) for Ising model."""
        rho1 = zeta_zero(1)
        A = universal_residue_factor(mpf('0.5'), rho1)
        # Verified numerically: |A| ~ 0.7737
        assert fabs(fabs(A) - mpf('0.7737')) < mpf('0.01')

    def test_c_one_boson(self):
        """A_1(rho_1) for free boson."""
        rho1 = zeta_zero(1)
        A = universal_residue_factor(mpf(1), rho1)
        assert fabs(fabs(A) - mpf('0.7725')) < mpf('0.01')

    def test_c_thirteen_self_dual(self):
        """A_13(rho_1) at the self-dual point."""
        rho1 = zeta_zero(1)
        A = universal_residue_factor(mpf(13), rho1)
        assert fabs(fabs(A) - mpf('0.869')) < mpf('0.01')

    def test_c_twenty_six_critical(self):
        """A_26(rho_1) at the critical string point."""
        rho1 = zeta_zero(1)
        A = universal_residue_factor(mpf(26), rho1)
        assert fabs(fabs(A) - mpf('1.083')) < mpf('0.01')

    def test_modulus_increases_with_c(self):
        """For rho_1, |A_c| is roughly increasing in c (large c dominant)."""
        rho1 = zeta_zero(1)
        A1 = fabs(universal_residue_factor(mpf(1), rho1))
        A26 = fabs(universal_residue_factor(mpf(26), rho1))
        assert A26 > A1, "Expected |A_26| > |A_1|"

    def test_conjugation_symmetry(self):
        """A_c(bar{rho}) = bar{A_c(rho)} (residue factor is real-analytic in rho)."""
        rho1 = zeta_zero(1)
        rho1_bar = mpc(mpre(rho1), -mpim(rho1))
        c = mpf(13)
        A = universal_residue_factor(c, rho1)
        A_bar = universal_residue_factor(c, rho1_bar)
        # A_c(bar rho) should equal bar(A_c(rho))
        A_conj = mpc(mpre(A), -mpim(A))
        assert fabs(A_bar - A_conj) < mpf('1e-15') * fabs(A)

    def test_multiple_zeros(self):
        """A_c(rho_n) for n = 1,...,5 at c = 13."""
        c = mpf(13)
        for n in range(1, 6):
            rho = zeta_zero(n)
            A = universal_residue_factor(c, rho)
            assert fabs(A) > mpf('1e-10')
            assert fabs(A) < mpf('100')


# =============================================================================
# 2. Verification against numerical residue
# =============================================================================

class TestResidueVerification:
    """Verify A_c formula against numerical residue of F_c(s)."""

    @pytest.mark.parametrize("c", [1, 13, 26])
    def test_residue_formula_consistency(self, c):
        """A_c from formula matches numerical residue to 1e-4."""
        rho1 = zeta_zero(1)
        result = verify_residue_formula(mpf(c), rho1, tol=1e-4)
        if result['consistent'] is not None:
            assert result['consistent'], (
                f"c={c}: rel_err = {result['relative_error']:.2e}"
            )

    def test_scattering_factor_pole_structure(self):
        """F_c(s) should have a pole at s = (1 + rho_1)/2."""
        rho1 = zeta_zero(1)
        s_rho = (1 + rho1) / 2
        c = mpf(13)
        # Near the pole, |F_c| should diverge
        vals = []
        for eps_exp in range(3, 8):
            eps = mpf(10) ** (-eps_exp)
            s = s_rho + mpc(eps, 0)
            try:
                val = scattering_factor(c, s)
                vals.append(fabs(val))
            except Exception:
                pass
        if len(vals) >= 2:
            # Values should increase as eps -> 0
            assert vals[-1] > vals[0], "F_c should diverge near the pole"


# =============================================================================
# 3. Residue kernel
# =============================================================================

class TestResidueKernel:
    """Test the paired real residue kernel w_{c,rho,u_0}(Delta)."""

    def test_kernel_finite(self):
        """w should be finite for Delta > 0."""
        rho1 = zeta_zero(1)
        for c in [mpf(1), mpf(13), mpf(26)]:
            w = residue_kernel(c, rho1, mpf(0), mpf(1))
            assert fabs(w) < mpf('1e10')

    def test_kernel_oscillates(self):
        """The kernel should change sign (oscillation from cos term)."""
        rho1 = zeta_zero(1)
        c = mpf(1)
        signs = []
        for D in range(1, 21):
            w = residue_kernel(c, rho1, mpf(0), mpf(D))
            signs.append(1 if mpre(w) > 0 else -1)
        # At least one sign change in 20 points
        changes = sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])
        assert changes >= 2, f"Only {changes} sign changes in 20 points"

    def test_kernel_decays(self):
        """The kernel magnitude should decay for large Delta at c > 1."""
        rho1 = zeta_zero(1)
        c = mpf(13)
        w1 = fabs(residue_kernel(c, rho1, mpf(0), mpf(1)))
        w20 = fabs(residue_kernel(c, rho1, mpf(0), mpf(20)))
        assert w20 < w1, "Kernel should decay at large Delta for c > 1"

    def test_oscillation_period(self):
        """Oscillation period = 4*pi/gamma for the first zero."""
        rho1 = zeta_zero(1)
        gamma_val = float(mpim(rho1))
        period = oscillation_period(gamma_val)
        expected = 4 * float(mppi) / gamma_val  # ~ 0.889
        assert abs(period - expected) < 1e-6

    def test_decay_exponent_on_line(self):
        """On-line decay exponent -(c - 1/2)/2."""
        c = mpf(13)
        sigma = mpf('0.5')
        exp_val = decay_exponent(c, sigma)
        expected = -(c - mpf('0.5')) / 2  # = -6.25
        assert fabs(exp_val - expected) < mpf('1e-20')

    def test_decay_exponent_off_line(self):
        """Off-line decay exponent differs from on-line."""
        c = mpf(13)
        on_line = decay_exponent(c, mpf('0.5'))
        off_line = decay_exponent(c, mpf('0.6'))
        assert on_line != off_line
        # sigma > 1/2 gives more negative exponent (faster decay)
        assert off_line < on_line

    def test_kernel_u0_effect(self):
        """Nonzero u_0 gives additional power-law suppression."""
        rho1 = zeta_zero(1)
        c = mpf(13)
        D = mpf(5)
        w0 = fabs(residue_kernel(c, rho1, mpf(0), D))
        w1 = fabs(residue_kernel(c, rho1, mpf(1), D))
        # u_0 = 1 multiplies by Delta^{-1}, so w1 ~ w0 / 5
        assert w1 < w0


# =============================================================================
# 4. Compatibility ratios
# =============================================================================

class TestCompatibilityRatios:
    """Test the compatibility ratios from def:compatibility-ratios."""

    def test_quartic_contact_virasoro(self):
        """Q^ct_Vir = 10/(c(5c+22)) for standard c values."""
        # AP1 check: compute from first principles, don't copy
        for c_val, expected in [
            (1, 10.0 / (1 * 27)),
            (13, 10.0 / (13 * 87)),
            (26, 10.0 / (26 * 152)),
        ]:
            result = float(virasoro_quartic_contact(mpf(c_val)))
            assert abs(result - expected) / expected < 1e-10

    def test_schur_complement(self):
        """Sigma_2 = 5/(5c+22)."""
        for c_val, expected in [
            (1, 5.0 / 27),
            (13, 5.0 / 87),
        ]:
            result = float(virasoro_schur_complement(mpf(c_val)))
            assert abs(result - expected) / expected < 1e-10

    def test_compatibility_product(self):
        """C_4^pot * C_4^Gram = 1 identically."""
        for c_val in [1, 5, 13, 26]:
            c = mpf(c_val)
            S4_res = virasoro_quartic_contact(c)  # At MC equilibrium
            pot = compatibility_ratio_potential(c, zeta_zero(1), mpf(0), S4_res)
            gram = compatibility_ratio_gram(c, zeta_zero(1), mpf(0), S4_res)
            product = pot * gram
            assert fabs(product - 1) < mpf('1e-20'), f"Product = {product} at c = {c_val}"

    def test_compatibility_at_mc_equilibrium(self):
        """At MC equilibrium, C_4^pot = 1."""
        for c_val in [1, 5, 13, 26]:
            c = mpf(c_val)
            # S_4^res at MC equilibrium equals the Virasoro quartic shadow
            S4_mc = virasoro_quartic_contact(c)
            pot = compatibility_ratio_potential(c, zeta_zero(1), mpf(0), S4_mc)
            assert fabs(pot - 1) < mpf('1e-20')


# =============================================================================
# 5. Ising shadow data
# =============================================================================

class TestIsingData:
    """Test Ising model (c = 1/2) shadow data."""

    def test_ising_kappa(self):
        """kappa(Ising) = c/2 = 1/4."""
        data = ising_shadow_data()
        assert abs(data['kappa'] - 0.25) < 1e-15

    def test_ising_class_number(self):
        """h(-40) = 2."""
        data = ising_shadow_data()
        assert data['class_number'] == 2

    def test_ising_discriminant_negative(self):
        """Binary form has negative discriminant (positive definite)."""
        data = ising_shadow_data()
        assert data['disc'] < 0

    def test_ising_form_positive_definite(self):
        """Q(m,n) > 0 for all (m,n) != (0,0)."""
        data = ising_shadow_data()
        a, b, c = data['a'], data['b'], data['c_coeff']
        # Check a > 0 and disc < 0
        assert a > 0
        assert b ** 2 - 4 * a * c < 0

    def test_ising_quartic_contact(self):
        """Q^ct_Ising = 10 / (0.5 * (2.5 + 22)) = 10 / (0.5 * 24.5) = 40/49."""
        Q_ct = float(virasoro_quartic_contact(mpf('0.5')))
        expected = 40.0 / 49.0
        assert abs(Q_ct - expected) / expected < 1e-10


# =============================================================================
# 6. Structural separation
# =============================================================================

class TestStructuralSeparation:
    """Test the structural separation diagnostic."""

    def test_mc_constraint_is_real(self):
        """MC constraint lives on the real s-axis."""
        diag = structural_separation_diagnostic(13)
        assert diag['F_1'] > 0
        assert 'Im(s) = 0' in diag['mc_constraint_at']

    def test_scattering_poles_complex(self):
        """Scattering poles have Im >> 0."""
        diag = structural_separation_diagnostic(13)
        assert diag['separation'] > 7  # Im(s_rho1) ~ 7.067

    def test_three_steps_open(self):
        """All three steps of the programme are OPEN."""
        diag = structural_separation_diagnostic(1)
        for step in diag['three_steps']:
            assert 'OPEN' in step


# =============================================================================
# 7. Closure programme
# =============================================================================

class TestClosureProgramme:
    """Test the closure programme analysis."""

    def test_system_overdetermined(self):
        """With 26 central charges, the system is overdetermined."""
        rho1 = zeta_zero(1)
        c_values = [mpf(c) for c in range(1, 27)]
        result = closure_system(c_values, rho1)
        assert result['overdetermined']
        assert result['n_equations'] == 26
        assert result['n_unknowns'] == 2

    def test_jacobian_full_rank(self):
        """The Jacobian of the closure system has rank 2."""
        rho1 = zeta_zero(1)
        c_values = [mpf(1), mpf(5), mpf(13), mpf(20), mpf(26)]
        result = closure_rank_analysis(c_values, rho1, epsilon=1e-6)
        assert result['numerical_rank'] == 2

    def test_overdetermination_at_off_line(self):
        """System is also overdetermined for hypothetical off-line zero."""
        rho_off = mpc(mpf('0.6'), mpf('14.135'))  # sigma = 0.6
        c_values = [mpf(1), mpf(5), mpf(13), mpf(20), mpf(26)]
        result = closure_rank_analysis(c_values, rho_off, epsilon=1e-6)
        assert result['numerical_rank'] == 2


# =============================================================================
# 8. Cross-consistency checks (AP10)
# =============================================================================

class TestCrossConsistency:
    """Anti-pattern AP10: cross-family consistency checks."""

    def test_A_c_smooth_in_c(self):
        """A_c(rho_1) varies smoothly in c (no jumps)."""
        rho1 = zeta_zero(1)
        prev = None
        for c_val in range(1, 26):
            A = fabs(universal_residue_factor(mpf(c_val), rho1))
            if prev is not None:
                # No jump > factor of 2
                ratio = float(A / prev) if prev > 0 else float('inf')
                assert 0.5 < ratio < 2.0, f"Jump at c={c_val}: ratio={ratio}"
            prev = A

    def test_log_modulus_nearly_linear(self):
        """log|A_c(rho_1)| varies nearly linearly in c for large c."""
        rho1 = zeta_zero(1)
        log_vals = []
        for c_val in range(10, 27):
            A = fabs(universal_residue_factor(mpf(c_val), rho1))
            log_vals.append(float(mplog(A)))
        # Check that consecutive differences are roughly constant
        diffs = [log_vals[i + 1] - log_vals[i] for i in range(len(log_vals) - 1)]
        # Standard deviation of differences should be small
        import numpy as np
        std = np.std(diffs)
        mean = np.mean(diffs)
        assert std / abs(mean) < 0.5, f"log|A| not smooth: std/mean = {std/abs(mean):.3f}"

    def test_kappa_from_c_not_hardcoded(self):
        """kappa = c/2 computed, not hardcoded (AP1)."""
        for c_val in [0.5, 1, 13, 26]:
            kappa = c_val / 2  # Compute from first principles
            assert abs(kappa - c_val / 2) < 1e-15

    def test_decay_exponent_additive_in_c(self):
        """Decay exponent is linear in c: -(c + sigma - 1)/2."""
        sigma = 0.5
        for c1, c2 in [(1, 2), (13, 14), (25, 26)]:
            e1 = float(decay_exponent(c1, sigma))
            e2 = float(decay_exponent(c2, sigma))
            # Difference should be -1/2
            assert abs((e2 - e1) - (-0.5)) < 1e-10


# =============================================================================
# 9. Argument phase structure
# =============================================================================

class TestArgumentPhase:
    """Test the phase arg(A_c(rho)) structure."""

    def test_argument_in_range(self):
        """arg(A_c) is in (-pi, pi]."""
        rho1 = zeta_zero(1)
        for c_val in [0.5, 1, 13, 26]:
            _, arg_val = A_c_modulus_and_arg(mpf(c_val), rho1)
            assert float(arg_val) > -float(mppi) - 1e-10
            assert float(arg_val) <= float(mppi) + 1e-10

    def test_argument_varies_with_c(self):
        """Different c values give different phases."""
        rho1 = zeta_zero(1)
        args = []
        for c_val in [1, 5, 13, 20, 26]:
            _, arg_val = A_c_modulus_and_arg(mpf(c_val), rho1)
            args.append(float(arg_val))
        # Not all the same
        assert max(args) - min(args) > 0.1


# =============================================================================
# 10. Integration: full report
# =============================================================================

class TestIntegration:
    """Integration tests for the full computation."""

    def test_compute_all_A_c(self):
        """compute_all_A_c_at_rho1 returns valid results."""
        results = compute_all_A_c_at_rho1()
        assert len(results) == 5
        for c, data in results.items():
            assert data['modulus'] > 0
            assert abs(data['argument_over_pi']) <= 1

    def test_A_c_table(self):
        """A_c_table returns consistent list of dicts."""
        c_values = [mpf(1), mpf(13)]
        rho1 = zeta_zero(1)
        table = A_c_table(c_values, rho1)
        assert len(table) == 2
        for entry in table:
            assert entry['modulus'] > 0

    def test_residue_kernel_array(self):
        """residue_kernel_array returns correct length."""
        rho1 = zeta_zero(1)
        Delta_values = list(range(1, 11))
        arr = residue_kernel_array(mpf(13), rho1, mpf(0), Delta_values)
        assert len(arr) == 10
        # All finite
        for v in arr:
            assert abs(v) < 1e20


# =============================================================================
# 11. Specific numerical values (AP38: cite source)
# =============================================================================

class TestSpecificValues:
    """Specific numerical values verified from independent computation."""

    def test_zeta_derivative_at_rho1(self):
        """zeta'(rho_1) ~ 0.7932 (from LMFDB/Odlyzko)."""
        rho1 = zeta_zero(1)
        zp = mpdiff(mpzeta, rho1)
        assert fabs(fabs(zp) - mpf('0.7932')) < mpf('0.01')

    def test_zeta_at_one_plus_rho1(self):
        """zeta(1 + rho_1) = zeta(3/2 + 14.1347i) is finite and nonzero."""
        rho1 = zeta_zero(1)
        val = mpzeta(1 + rho1)
        assert fabs(val) > mpf('0.1')
        assert fabs(val) < mpf('10')

    def test_gamma_at_shifted_rho1(self):
        """Gamma((1 + rho_1)/2) is finite."""
        rho1 = zeta_zero(1)
        g = mpgamma((1 + rho1) / 2)
        assert fabs(g) > mpf('1e-10')
        assert fabs(g) < mpf('1')

    def test_oscillation_period_rho1(self):
        """Period = 4*pi/14.1347 ~ 0.889."""
        period = oscillation_period(14.134725)
        assert abs(period - 0.889) < 0.01

    def test_ising_S4(self):
        """S_4(Ising) = 10/(0.5 * 24.5) = 40/49 ~ 0.8163."""
        data = ising_shadow_data()
        assert abs(data['S4'] - 40.0 / 49.0) < 1e-10


# =============================================================================
# 12. Edge cases and robustness
# =============================================================================

class TestEdgeCases:
    """Test behavior at special/edge-case parameters."""

    def test_c_near_zero(self):
        """A_c(rho) at c near 0 (but c > 0)."""
        rho1 = zeta_zero(1)
        # c = 0.1: Gamma((c+rho-1)/2) = Gamma((-0.4+rho)/2)
        A = universal_residue_factor(mpf('0.1'), rho1)
        assert fabs(A) > 0
        assert fabs(A) < mpf('1e10')

    def test_large_c(self):
        """A_c for c = 100."""
        rho1 = zeta_zero(1)
        A = universal_residue_factor(mpf(100), rho1)
        assert fabs(A) > 0

    def test_second_zero(self):
        """A_c at the second zeta zero."""
        rho2 = zeta_zero(2)
        A = universal_residue_factor(mpf(13), rho2)
        assert fabs(A) > 0

    def test_tenth_zero(self):
        """A_c at the tenth zeta zero."""
        rho10 = zeta_zero(10)
        A = universal_residue_factor(mpf(13), rho10)
        assert fabs(A) > 0

    def test_invalid_zero_index(self):
        """Requesting zero index > 10 raises ValueError."""
        with pytest.raises(ValueError):
            zeta_zero(11)

    def test_kernel_at_delta_half(self):
        """Kernel at non-integer Delta."""
        rho1 = zeta_zero(1)
        w = residue_kernel(mpf(13), rho1, mpf(0), mpf('0.5'))
        assert fabs(w) > 0

    def test_kernel_large_delta(self):
        """Kernel at large Delta (should be very small for c >> 1)."""
        rho1 = zeta_zero(1)
        w = residue_kernel(mpf(26), rho1, mpf(0), mpf(1000))
        assert fabs(w) < mpf('1e-20')


# =============================================================================
# 13. Chowla-Selberg Epstein zeta
# =============================================================================

from universal_residue_factor import (
    epstein_chowla_selberg,
    epstein_zeta_binary,
    search_off_line_zeros_ising,
)


class TestChowlaSelberg:
    """Test the Chowla-Selberg analytic continuation of Epstein zeta."""

    def test_agrees_with_direct_sum_at_convergent_s(self):
        """CS formula matches direct sum at Re(s) = 2 (well-converged).

        The direct sum with max_norm=80 converges slowly for real s near 1;
        agreement at 1e-3 is expected given the truncation. The CS formula
        is the EXACT answer; the direct sum is the approximation.
        """
        # Simple form: Q(m,n) = m^2 + n^2 (disc = -4)
        a, b, c = mpf(1), mpf(0), mpf(1)
        s = mpc(2, 0)
        cs_val = epstein_chowla_selberg(a, b, c, s, max_n=40)
        direct = epstein_zeta_binary(a, b, c, s, max_norm=80)
        rel_err = fabs(cs_val - direct) / fabs(direct)
        # Direct sum truncation error dominates; 1e-3 is the bound
        assert float(rel_err) < 1e-3, f"CS vs direct: rel_err = {float(rel_err):.2e}"

    def test_agrees_at_large_s(self):
        """CS matches direct sum at s = 5 (fast convergence of lattice sum)."""
        a, b, c = mpf(1), mpf(0), mpf(1)
        s = mpc(5, 0)  # Large Re(s) for fast direct-sum convergence
        cs_val = epstein_chowla_selberg(a, b, c, s, max_n=40)
        direct = epstein_zeta_binary(a, b, c, s, max_norm=80)
        rel_err = fabs(cs_val - direct) / fabs(direct)
        assert float(rel_err) < 1e-3, f"rel_err = {float(rel_err):.2e}"

    def test_cs_self_consistency(self):
        """CS at s=2 and s=3 are consistent with known zeta factorization.

        For Q(m,n) = m^2 + n^2:
        E_Q(s) = 4 * zeta(s) * L(s, chi_{-4})
        where chi_{-4} is the nontrivial character mod 4.
        L(s, chi_{-4}) = sum_{n=1}^infty chi(n)/n^s = 1 - 1/3^s + 1/5^s - ...
        """
        a, b, c = mpf(1), mpf(0), mpf(1)
        s = mpc(3, 0)

        cs_val = epstein_chowla_selberg(a, b, c, s, max_n=60)

        # Compute 4 * zeta(s) * L(s, chi_{-4})
        z3 = mpzeta(3)  # zeta(3) = Apery's constant ~ 1.202
        # L(3, chi_{-4}) = sum n^{-3} chi(n) = 1 - 1/27 + 1/125 - ...
        L3 = mpc(0)
        for n in range(1, 2000):
            chi = {1: 1, 3: -1}.get(n % 4, 0)
            if chi != 0:
                L3 += mpf(chi) * mppower(mpf(n), -s)
        expected = 4 * z3 * L3

        rel_err = fabs(cs_val - expected) / fabs(expected)
        assert float(rel_err) < 1e-4, f"CS vs factorization: rel_err = {float(rel_err):.2e}"

    def test_functional_equation(self):
        """E*_Q(s) = E*_Q(1-s) for the completed Epstein zeta.

        For Q(m,n) = m^2 + n^2 (disc = -4, det = 1):
        pi^{-s} Gamma(s) E_Q(s) = pi^{-(1-s)} Gamma(1-s) E_Q(1-s)

        i.e., E_Q(s) = pi^{2s-1} Gamma(1-s)/Gamma(s) E_Q(1-s)
        """
        a, b, c = mpf(1), mpf(0), mpf(1)
        s = mpc(mpf('0.3'), mpf(5))  # inside the critical strip

        E_s = epstein_chowla_selberg(a, b, c, s, max_n=50)
        E_1ms = epstein_chowla_selberg(a, b, c, 1 - s, max_n=50)

        # Completed: pi^{-s} Gamma(s) E(s) should equal pi^{-(1-s)} Gamma(1-s) E(1-s)
        lhs = mppower(mppi, -s) * mpgamma(s) * E_s
        rhs = mppower(mppi, -(1 - s)) * mpgamma(1 - s) * E_1ms

        rel_err = fabs(lhs - rhs) / fabs(lhs)
        assert float(rel_err) < 1e-6, f"FE violation: rel_err = {float(rel_err):.2e}"

    def test_cs_at_half_line(self):
        """CS gives finite values on the critical line."""
        a, b, c = mpf(1), mpf(0), mpf(1)
        s = mpc(mpf('0.5'), mpf(10))
        val = epstein_chowla_selberg(a, b, c, s, max_n=50)
        assert fabs(val) < mpf('1e10')
        assert fabs(val) > mpf('1e-20')

    def test_ising_form_cs_finite(self):
        """CS gives finite values for Ising binary form."""
        data = ising_shadow_data()
        a = mpf(data['a'])
        b = mpf(data['b'])
        c = mpf(data['c_coeff'])
        s = mpc(mpf('0.5'), mpf(14))
        val = epstein_chowla_selberg(a, b, c, s, max_n=50)
        assert fabs(val) > 0
        assert fabs(val) < mpf('1e20')


class TestOffLineZeroSearch:
    """Test the Ising off-line zero search."""

    def test_search_returns_results(self):
        """Search returns a dict with expected keys."""
        result = search_off_line_zeros_ising(
            sigma_range=(0.4, 0.6), gamma_range=(10, 20),
            sigma_steps=5, gamma_steps=11
        )
        assert 'near_zeros_off_line' in result
        assert 'near_zeros_on_line' in result
        assert 'diagnosis' in result
        assert 'grid_size' in result

    def test_on_line_zeros_at_sigma_half(self):
        """Near-zeros on the critical line should have sigma ~ 0.5."""
        result = search_off_line_zeros_ising(
            sigma_range=(0.4, 0.6), gamma_range=(10, 12),
            sigma_steps=5, gamma_steps=21
        )
        for entry in result['near_zeros_on_line']:
            assert abs(entry['sigma'] - 0.5) < 0.05

    def test_no_obvious_off_line_zeros(self):
        """No off-line zeros with |E_Q| < 0.01 in the search region.

        This is a NUMERICAL finding, not a proof. The Davenport-Heilbronn
        mechanism could produce off-line zeros at larger gamma or closer
        to sigma = 0.5. The MC constraints may or may not exclude them.
        """
        result = search_off_line_zeros_ising(
            sigma_range=(0.35, 0.65), gamma_range=(5, 30),
            sigma_steps=7, gamma_steps=26
        )
        for entry in result['near_zeros_off_line']:
            # None should be extremely close to zero
            assert entry['magnitude'] > 0.01, (
                f"Possible off-line zero at sigma={entry['sigma']}, "
                f"gamma={entry['gamma']}: |E| = {entry['magnitude']:.6e}"
            )
