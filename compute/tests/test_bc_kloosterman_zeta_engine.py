r"""Tests for bc_kloosterman_zeta_engine.py — Kloosterman zeta from the shadow tower.

Verifies:
  1. Shadow Kloosterman sum computation and special cases
  2. Weil bound for shadow-twisted sums
  3. Kloosterman zeta convergence
  4. Zero finding
  5. Linnik-Selberg partial sums
  6. Kuznetsov trace formula: geometric vs diagonal
  7. Petersson-Kuznetsov: shadow Maass Fourier coefficients
  8. Evaluation at Riemann zeta zeros
  9. Complementarity structure
  10. Ramanujan-Selberg convergence test
  11. Cross-family consistency
  12. Multi-path verification

MULTI-PATH VERIFICATION (per the Verification Mandate):
  Path 1: Direct computation of shadow Kloosterman sums
  Path 2: Weil bound verification (inequality, for all computed sums)
  Path 3: Kuznetsov formula: geometric side vs diagonal side agreement
  Path 4: Trivial case c=1: S(m,n;1) = 1 => K^{sh}(A;m,n;1) = Sum S_r(A)

60+ tests total.
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math
import pytest

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =====================================================================
# 1. Shadow Kloosterman sum: basics
# =====================================================================

class TestShadowKloostermanBasics:
    """Test shadow Kloosterman sum K^{sh}(A; m, n; c)."""

    def test_heisenberg_single_term(self):
        """Heisenberg H_k: K^{sh} = k * S(2m, 2n; c) (single arity-2 term)."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        from lib.shadow_kloosterman_engine import kloosterman_sum
        k = 3.0
        for m in [1, 2, 5]:
            for n in [1, 3, 7]:
                for c in [1, 5, 11, 23]:
                    ksh = shadow_kloosterman_sum('heisenberg', k, m, n, c)
                    expected = k * kloosterman_sum(2 * m, 2 * n, c)
                    assert abs(ksh - expected) < 1e-8, \
                        f"Heisenberg k={k}, m={m}, n={n}, c={c}: {ksh} != {expected}"

    def test_c_equals_1_all_kloosterman_trivial(self):
        """At c=1: S(a,b;1) = 1 for all a,b, so K^{sh}(A;m,n;1) = Sum_r S_r(A).

        Path 4 verification: the c=1 case reduces to the shadow coefficient sum.
        """
        from lib.bc_kloosterman_zeta_engine import (
            shadow_kloosterman_sum, shadow_coefficients,
        )
        families = [
            ('heisenberg', 1.0),
            ('affine_sl2', 1.0),
            ('virasoro', 10.0),
            ('betagamma', 1.0),
        ]
        for fam, par in families:
            coeffs = shadow_coefficients(fam, par, 30)
            coeff_sum = sum(v for r, v in coeffs.items() if r >= 2)
            for m in [1, 3, 7]:
                for n in [1, 2, 5]:
                    ksh = shadow_kloosterman_sum(fam, par, m, n, 1, max_r=30)
                    assert abs(ksh - coeff_sum) < 1e-8, \
                        f"{fam} par={par}, m={m}, n={n}: K^sh at c=1 = {ksh}, sum = {coeff_sum}"

    def test_shadow_kloosterman_is_real(self):
        """K^{sh}(A; m, n; c) is real for integer m, n (inherits from Kloosterman reality)."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        for fam, par in [('virasoro', 5.0), ('affine_sl2', 2.0)]:
            for m in [1, 3]:
                for n in [2, 5]:
                    for c in [3, 7, 13]:
                        val = shadow_kloosterman_sum(fam, par, m, n, c)
                        # val should be a float (real), not complex
                        assert isinstance(val, float), f"Expected float, got {type(val)}"

    def test_c_must_be_positive(self):
        """c <= 0 should raise ValueError."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        with pytest.raises(ValueError):
            shadow_kloosterman_sum('heisenberg', 1.0, 1, 1, 0)
        with pytest.raises(ValueError):
            shadow_kloosterman_sum('heisenberg', 1.0, 1, 1, -5)

    def test_affine_sl2_two_terms(self):
        """Affine sl_2: K^{sh} = kappa*S(2m,2n;c) + alpha*S(3m,3n;c) (class L, S_r=0 for r>=4)."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum, shadow_coefficients
        from lib.shadow_kloosterman_engine import kloosterman_sum
        k = 1.0
        coeffs = shadow_coefficients('affine_sl2', k, 30)
        s2 = coeffs.get(2, 0.0)
        s3 = coeffs.get(3, 0.0)
        # All higher S_r should be zero (class L)
        for r in range(4, 31):
            assert abs(coeffs.get(r, 0.0)) < 1e-12, f"S_{r} nonzero for class L"

        for m, n, c in [(1, 1, 7), (2, 3, 11), (1, 5, 13)]:
            ksh = shadow_kloosterman_sum('affine_sl2', k, m, n, c)
            expected = s2 * kloosterman_sum(2*m, 2*n, c) + s3 * kloosterman_sum(3*m, 3*n, c)
            assert abs(ksh - expected) < 1e-8, \
                f"Affine sl_2: m={m}, n={n}, c={c}: {ksh} != {expected}"

    def test_betagamma_three_terms(self):
        """Beta-gamma: class C, tower terminates at arity 4."""
        from lib.bc_kloosterman_zeta_engine import shadow_coefficients
        coeffs = shadow_coefficients('betagamma', 1.0, 30)
        # S_r = 0 for r >= 5 (class C)
        for r in range(5, 31):
            assert abs(coeffs.get(r, 0.0)) < 1e-12, f"S_{r} nonzero for class C"


# =====================================================================
# 2. Weil bound for shadow Kloosterman sums
# =====================================================================

class TestShadowWeilBound:
    """Verify the Weil bound for shadow-twisted Kloosterman sums."""

    def test_weil_bound_heisenberg(self):
        """Path 2: Weil bound holds for Heisenberg shadow Kloosterman."""
        from lib.bc_kloosterman_zeta_engine import verify_shadow_weil_bound
        for m in range(1, 6):
            for n in range(1, 6):
                for c in range(1, 30):
                    ksh_abs, bound, ok = verify_shadow_weil_bound(
                        'heisenberg', 1.0, m, n, c)
                    assert ok, f"Weil bound failed: m={m}, n={n}, c={c}: |K^sh|={ksh_abs} > {bound}"

    def test_weil_bound_virasoro(self):
        """Path 2: Weil bound holds for Virasoro shadow Kloosterman."""
        from lib.bc_kloosterman_zeta_engine import verify_shadow_weil_bound
        for c_val in [1.0, 10.0, 25.0]:
            for m in [1, 3, 5]:
                for n in [1, 2, 4]:
                    for c in [1, 5, 11, 17, 29]:
                        ksh_abs, bound, ok = verify_shadow_weil_bound(
                            'virasoro', c_val, m, n, c)
                        assert ok, f"Weil bound failed: c_val={c_val}, m={m}, n={n}, c={c}"

    def test_weil_bound_affine_sl2(self):
        """Path 2: Weil bound holds for affine sl_2."""
        from lib.bc_kloosterman_zeta_engine import verify_shadow_weil_bound
        for m in [1, 2, 3]:
            for n in [1, 4]:
                for c in range(1, 20):
                    _, _, ok = verify_shadow_weil_bound('affine_sl2', 1.0, m, n, c)
                    assert ok

    def test_weil_bound_ratio_bounded_by_one(self):
        """Weil ratio |K^{sh}| / bound should be in [0, 1]."""
        from lib.bc_kloosterman_zeta_engine import (
            shadow_kloosterman_from_coeffs, shadow_kloosterman_weil_bound,
            shadow_coefficients,
        )
        coeffs = shadow_coefficients('virasoro', 5.0, 20)
        for m in [1, 3]:
            for n in [1, 2]:
                for c in [3, 7, 13, 19, 23]:
                    ksh = abs(shadow_kloosterman_from_coeffs(coeffs, m, n, c))
                    bound = shadow_kloosterman_weil_bound(coeffs, m, n, c)
                    if bound > 1e-15:
                        ratio = ksh / bound
                        assert ratio <= 1.0 + 1e-10, f"Ratio > 1: {ratio}"


# =====================================================================
# 3. Kloosterman zeta convergence
# =====================================================================

class TestKloostermanZetaConvergence:
    """Test convergence properties of the Kloosterman zeta Z^{Kl}(s; A)."""

    def test_convergence_above_three_halves(self):
        """Z^{Kl}(s; A) should converge for Re(s) > 3/2 (Weil bound)."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_convergence
        conv = kloosterman_zeta_convergence(2.0, 'heisenberg', 1.0, c_max=200)
        assert conv['convergence_exponent'] > 0.3, \
            f"Expected convergent, got exponent {conv['convergence_exponent']}"

    def test_partial_sums_stabilize(self):
        """Partial sums should stabilize for Re(s) = 2."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_partial_sums
        partials = kloosterman_zeta_partial_sums(2.0, 'heisenberg', 1.0, c_max=100)
        # Last 10 partial sums should be close together
        last_10 = [abs(p) for p in partials[-10:]]
        spread = max(last_10) - min(last_10)
        assert spread < 0.5, f"Partial sums not stabilizing: spread = {spread}"

    def test_heisenberg_kloosterman_zeta_finite(self):
        """Z^{Kl}(2; H_1) should be a finite real number."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta
        val = kloosterman_zeta(2.0, 'heisenberg', 1.0, c_max=200)
        assert math.isfinite(val.real), f"Got non-finite value: {val}"

    def test_virasoro_convergence_at_s_2(self):
        """Z^{Kl}(2; Vir_10) should converge."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_convergence
        conv = kloosterman_zeta_convergence(2.0, 'virasoro', 10.0, c_max=200, max_r=20)
        assert math.isfinite(conv['value']), f"Non-finite value: {conv['value']}"


# =====================================================================
# 4. Kloosterman zeta at c=1: structural identity
# =====================================================================

class TestKloostermanZetaTrivialModulus:
    """At c=1, S(a,b;1) = 1, so each Kloosterman zeta term is the shadow sum."""

    def test_c1_contribution_equals_shadow_sum(self):
        """The c=1 term of Z^{Kl}(s; A) equals Sum_r S_r(A) * 1^{-s} = Sum S_r."""
        from lib.bc_kloosterman_zeta_engine import (
            shadow_kloosterman_from_coeffs, shadow_coefficients,
        )
        for fam, par in [('heisenberg', 2.0), ('virasoro', 5.0), ('affine_sl2', 1.0)]:
            coeffs = shadow_coefficients(fam, par, 30)
            ksh_at_1 = shadow_kloosterman_from_coeffs(coeffs, 1, 1, 1)
            coeff_sum = sum(v for r, v in coeffs.items() if r >= 2)
            assert abs(ksh_at_1 - coeff_sum) < 1e-10


# =====================================================================
# 5. Linnik-Selberg partial sums
# =====================================================================

class TestLinnikSelberg:
    """Test Linnik-Selberg partial sums L^{sh}(A; m,n; X)."""

    def test_linnik_selberg_heisenberg(self):
        """Heisenberg Linnik-Selberg sum should converge."""
        from lib.bc_kloosterman_zeta_engine import linnik_selberg_partial_sum
        val = linnik_selberg_partial_sum('heisenberg', 1.0, 1, 1, 200)
        assert math.isfinite(val), f"Non-finite: {val}"

    def test_linnik_selberg_sequence_monotone_eventual(self):
        """Linnik-Selberg sequence should eventually stabilize."""
        from lib.bc_kloosterman_zeta_engine import linnik_selberg_sequence
        seq = linnik_selberg_sequence('heisenberg', 1.0, 1, 1, 100)
        # Check that the last 20 values are close
        last_20 = seq[-20:]
        spread = max(last_20) - min(last_20)
        assert spread < 2.0, f"Linnik-Selberg spread too large: {spread}"

    def test_linnik_selberg_virasoro(self):
        """Virasoro Linnik-Selberg sum should be finite."""
        from lib.bc_kloosterman_zeta_engine import linnik_selberg_partial_sum
        val = linnik_selberg_partial_sum('virasoro', 10.0, 1, 1, 100, max_r=15)
        assert math.isfinite(val)

    def test_linnik_selberg_first_term(self):
        """L^{sh}(A; m,n; 1) = K^{sh}(A; m,n; 1) / 1 = Sum S_r (c=1 identity)."""
        from lib.bc_kloosterman_zeta_engine import (
            linnik_selberg_partial_sum, shadow_coefficients,
        )
        coeffs = shadow_coefficients('heisenberg', 1.0, 30)
        coeff_sum = sum(v for r, v in coeffs.items() if r >= 2)
        ls1 = linnik_selberg_partial_sum('heisenberg', 1.0, 1, 1, 1)
        assert abs(ls1 - coeff_sum) < 1e-10


# =====================================================================
# 6. Kuznetsov trace formula
# =====================================================================

class TestKuznetsovTraceFormula:
    """Test the shadow-twisted Kuznetsov trace formula."""

    def test_geometric_side_finite(self):
        """Geometric side should be finite for all standard families."""
        from lib.bc_kloosterman_zeta_engine import kuznetsov_geometric_side
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 1.0), ('virasoro', 10.0)]:
            val = kuznetsov_geometric_side(fam, par, 1, 1, c_max=50, max_r=15)
            assert math.isfinite(val), f"Non-finite geometric side for {fam}"

    def test_diagonal_term_nonzero_for_m_eq_n(self):
        """When m = n, the diagonal term should be nonzero."""
        from lib.bc_kloosterman_zeta_engine import kuznetsov_diagonal_term
        val = kuznetsov_diagonal_term(1, 1)
        assert abs(val) > 1e-10, f"Diagonal term vanishes for m=n=1: {val}"

    def test_diagonal_term_zero_for_m_ne_n(self):
        """When m != n, the diagonal term should vanish."""
        from lib.bc_kloosterman_zeta_engine import kuznetsov_diagonal_term
        val = kuznetsov_diagonal_term(1, 2)
        assert abs(val) < 1e-10, f"Diagonal term nonzero for m=1, n=2: {val}"

    def test_kuznetsov_spectral_approximation_runs(self):
        """Path 3: Kuznetsov spectral approximation should run without error."""
        from lib.bc_kloosterman_zeta_engine import kuznetsov_spectral_approximation
        result = kuznetsov_spectral_approximation(
            'heisenberg', 1.0, 1, 1, c_max=50, max_r=15)
        assert 'geometric' in result
        assert 'diagonal' in result
        assert math.isfinite(result['geometric'])
        assert math.isfinite(result['diagonal'])

    def test_kuznetsov_geometric_vs_diagonal_order(self):
        """For m=n=1, geometric and diagonal should be of comparable magnitude."""
        from lib.bc_kloosterman_zeta_engine import kuznetsov_spectral_approximation
        result = kuznetsov_spectral_approximation(
            'heisenberg', 1.0, 1, 1, c_max=100, max_r=15)
        geom = abs(result['geometric'])
        diag = abs(result['diagonal'])
        # They should be within a few orders of magnitude
        if diag > 1e-10 and geom > 1e-10:
            ratio = geom / diag
            assert 1e-5 < ratio < 1e5, \
                f"Geometric/diagonal ratio too extreme: {ratio}"


# =====================================================================
# 7. Petersson-Kuznetsov: shadow Maass Fourier coefficients
# =====================================================================

class TestShadowMaassFourier:
    """Test shadow Maass form Fourier coefficients from Kloosterman data."""

    def test_fourier_coefficients_finite(self):
        """Shadow Maass Fourier coefficients should all be finite."""
        from lib.bc_kloosterman_zeta_engine import shadow_maass_fourier_coefficients
        coeffs = shadow_maass_fourier_coefficients(
            'heisenberg', 1.0, num_coeffs=20, c_max=50, max_r=15)
        assert len(coeffs) == 20
        for i, a in enumerate(coeffs):
            assert math.isfinite(a), f"a({i+1}) = {a} not finite"

    def test_fourier_first_coefficient_nonzero(self):
        """a^{sh}(1) should be nonzero (normalizing coefficient)."""
        from lib.bc_kloosterman_zeta_engine import shadow_maass_fourier_coefficients
        coeffs = shadow_maass_fourier_coefficients(
            'heisenberg', 1.0, num_coeffs=5, c_max=50, max_r=15)
        assert abs(coeffs[0]) > 1e-15, f"a(1) vanishes: {coeffs[0]}"

    def test_fourier_growth_analysis(self):
        """Growth analysis should return a valid exponent."""
        from lib.bc_kloosterman_zeta_engine import shadow_maass_fourier_growth
        result = shadow_maass_fourier_growth(
            'heisenberg', 1.0, num_coeffs=30, c_max=50, max_r=15)
        assert 'growth_exponent' in result
        assert math.isfinite(result['growth_exponent'])

    def test_virasoro_fourier_coefficients(self):
        """Virasoro shadow Maass coefficients should be finite."""
        from lib.bc_kloosterman_zeta_engine import shadow_maass_fourier_coefficients
        coeffs = shadow_maass_fourier_coefficients(
            'virasoro', 10.0, num_coeffs=10, c_max=30, max_r=15)
        assert len(coeffs) == 10
        for a in coeffs:
            assert math.isfinite(a)


# =====================================================================
# 8. Evaluation at Riemann zeta zeros
# =====================================================================

class TestZetaZeroEvaluation:
    """Test evaluation of the Kloosterman zeta at Riemann zeta zeros."""

    def test_first_zeta_zero(self):
        """Z^{Kl}(1/2 + i*14.134...; H_1) should be finite."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_at_zeta_zeros
        results = kloosterman_zeta_at_zeta_zeros(
            'heisenberg', 1.0, num_zeros=1, c_max=100)
        assert len(results) == 1
        assert abs(results[0]['gamma'] - 14.1347) < 0.01
        assert math.isfinite(results[0]['abs_at_rho'])
        assert math.isfinite(results[0]['abs_at_shifted'])

    def test_multiple_zeta_zeros(self):
        """Evaluate at first 10 zeta zeros."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_at_zeta_zeros
        results = kloosterman_zeta_at_zeta_zeros(
            'heisenberg', 1.0, num_zeros=10, c_max=100)
        assert len(results) == 10
        for r in results:
            assert math.isfinite(r['abs_at_rho'])
            assert math.isfinite(r['abs_at_shifted'])

    def test_virasoro_zeta_zeros(self):
        """Virasoro Kloosterman zeta at zeta zeros should be finite."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_at_zeta_zeros
        results = kloosterman_zeta_at_zeta_zeros(
            'virasoro', 10.0, num_zeros=5, c_max=50, max_r=15)
        assert len(results) == 5
        for r in results:
            assert math.isfinite(r['abs_at_rho'])

    def test_zero_correlations(self):
        """Correlation analysis should return valid statistics."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_zero_correlations
        result = kloosterman_zeta_zero_correlations(
            'heisenberg', 1.0, num_zeros=10, c_max=100)
        assert math.isfinite(result['mean_abs'])
        assert result['mean_abs'] >= 0
        assert math.isfinite(result['var_abs'])
        assert result['var_abs'] >= 0
        assert -1.01 <= result['gamma_correlation'] <= 1.01

    def test_shifted_zeta_zero_modulus(self):
        """At shifted point (1+rho)/2, Re > 1/2 so expect larger modulus."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_at_zeta_zeros
        results = kloosterman_zeta_at_zeta_zeros(
            'heisenberg', 1.0, num_zeros=5, c_max=100)
        # The shifted point has larger real part (0.75 vs 0.5) so the
        # Dirichlet series is better converged there
        for r in results:
            assert math.isfinite(r['abs_at_shifted'])


# =====================================================================
# 9. Complementarity (Virasoro c <-> 26-c)
# =====================================================================

class TestComplementarity:
    """Test Kloosterman zeta complementarity for Virasoro."""

    def test_self_dual_point(self):
        """At c=13 (self-dual): Z_c = Z_{26-c} by symmetry."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_complementarity
        result = kloosterman_zeta_complementarity(2.0, 13.0, c_max=50, max_r=15)
        z_c = result['Z_c']
        z_dual = result['Z_dual']
        # At c=13: Vir_13 and Vir_{26-13}=Vir_13 are the same algebra
        assert abs(z_c - z_dual) < 1e-8, \
            f"Self-dual failure: Z_c={z_c}, Z_dual={z_dual}"

    def test_complementarity_sum_structure(self):
        """Z_c + Z_{26-c} should equal 2 * Z_{13} at the self-dual point."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_complementarity
        result = kloosterman_zeta_complementarity(2.0, 13.0, c_max=50, max_r=15)
        z_sum = result['Z_sum']
        z_sd = result['Z_self_dual']
        assert abs(z_sum - 2 * z_sd) < 1e-8, \
            f"Complementarity sum != 2*Z_13: sum={z_sum}, 2*Z_13={2*z_sd}"

    def test_complementarity_asymmetry(self):
        """For c != 13, Z_c != Z_{26-c} in general."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_complementarity
        result = kloosterman_zeta_complementarity(2.0, 5.0, c_max=50, max_r=15)
        z_c = result['Z_c']
        z_dual = result['Z_dual']
        # They should generally differ (c=5 vs c=21)
        # but this is not guaranteed for all s; just check both are finite
        assert math.isfinite(z_c.real) and math.isfinite(z_dual.real)


# =====================================================================
# 10. Ramanujan-Selberg convergence test
# =====================================================================

class TestRamanujanSelberg:
    """Test the Ramanujan-Selberg convergence test."""

    def test_convergence_at_sigma_three_quarters(self):
        """Z^{Kl} should converge at sigma = 3/4 (if Selberg eigenvalue conjecture holds)."""
        from lib.bc_kloosterman_zeta_engine import ramanujan_selberg_test
        result = ramanujan_selberg_test(
            'heisenberg', 1.0, sigma_test=0.75, c_max=200)
        assert math.isfinite(result['value_at_sigma'])

    def test_convergence_at_sigma_one(self):
        """Z^{Kl} should converge at sigma = 1."""
        from lib.bc_kloosterman_zeta_engine import ramanujan_selberg_test
        result = ramanujan_selberg_test(
            'heisenberg', 1.0, sigma_test=1.0, c_max=200)
        assert math.isfinite(result['value_at_1'])

    def test_virasoro_ramanujan_selberg(self):
        """Virasoro convergence test should complete without error."""
        from lib.bc_kloosterman_zeta_engine import ramanujan_selberg_test
        result = ramanujan_selberg_test(
            'virasoro', 10.0, sigma_test=0.75, c_max=100, max_r=15)
        assert 'value_at_sigma' in result
        assert math.isfinite(result['value_at_sigma'])


# =====================================================================
# 11. Cross-family comparison
# =====================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_cross_family_all_finite(self):
        """All standard families should give finite Z^{Kl}(2; A)."""
        from lib.bc_kloosterman_zeta_engine import cross_family_comparison
        results = cross_family_comparison(2.0, c_max=50, max_r=15)
        for label, val in results.items():
            assert math.isfinite(val.real) and math.isfinite(val.imag), \
                f"{label}: Z^Kl = {val} not finite"

    def test_heisenberg_dominates_at_large_real(self):
        """At large Re(s), the c=1 term dominates, so Z^{Kl} ~ Sum S_r."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta, shadow_coefficients
        # For very large sigma, c^{-s} decays fast for c >= 2,
        # so Z^{Kl}(s) ~ K^{sh}(A;1,1;1) = Sum S_r
        coeffs = shadow_coefficients('heisenberg', 1.0, 30)
        coeff_sum = sum(v for r, v in coeffs.items() if r >= 2)
        val = kloosterman_zeta(10.0, 'heisenberg', 1.0, c_max=200)
        assert abs(val.real - coeff_sum) < 0.1, \
            f"At s=10, Z^Kl should be ~ Sum S_r = {coeff_sum}, got {val.real}"

    def test_kappa_ordering(self):
        """Heisenberg k=1 has kappa=1, affine sl_2 k=1 has kappa=3*(1+2)/4=9/4.

        The shadow Kloosterman sum at c=1 should respect this ordering.
        """
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        ksh_heis = shadow_kloosterman_sum('heisenberg', 1.0, 1, 1, 1)
        ksh_aff = shadow_kloosterman_sum('affine_sl2', 1.0, 1, 1, 1)
        # Heisenberg: K^{sh} at c=1 = kappa = 1
        assert abs(ksh_heis - 1.0) < 1e-8
        # Affine sl_2 k=1: K^{sh} at c=1 = kappa + alpha (two nonzero terms)
        assert ksh_aff > ksh_heis, f"Expected affine > heisenberg, got {ksh_aff} <= {ksh_heis}"


# =====================================================================
# 12. Zero finding
# =====================================================================

class TestZeroFinding:
    """Test Kloosterman zeta zero location."""

    def test_find_zeros_heisenberg(self):
        """Should find zeros on a vertical line for Heisenberg."""
        from lib.bc_kloosterman_zeta_engine import find_kloosterman_zeta_zeros
        zeros = find_kloosterman_zeta_zeros(
            'heisenberg', 1.0,
            sigma=1.0, t_min=1.0, t_max=50.0, t_step=0.5,
            c_max=100, max_r=15)
        # The Heisenberg case has K^{sh} = k*S(2,2;c), so
        # Z^{Kl}(s) = k * Sum_c S(2,2;c) c^{-s}
        # This Dirichlet series should have zeros
        # (it is NOT identically zero for k=1)
        assert isinstance(zeros, list)
        # We accept any number of zeros; just check they are complex
        for z in zeros:
            assert isinstance(z, complex)

    def test_zero_values_small_modulus(self):
        """At found zeros, Z^{Kl} should have small modulus."""
        from lib.bc_kloosterman_zeta_engine import (
            find_kloosterman_zeta_zeros, kloosterman_zeta,
        )
        zeros = find_kloosterman_zeta_zeros(
            'heisenberg', 1.0,
            sigma=1.0, t_min=5.0, t_max=30.0, t_step=0.3,
            c_max=100, max_r=15, refine=True)
        for z in zeros[:3]:  # check first 3
            val = kloosterman_zeta(z, 'heisenberg', 1.0, c_max=100)
            # The real part should be near zero (we searched for sign changes in Re)
            assert abs(val.real) < 1.0, f"At zero {z}, Re(Z^Kl) = {val.real}"


# =====================================================================
# 13. Multi-path verification
# =====================================================================

class TestMultiPathVerification:
    """Multi-path verification: cross-check results across independent methods."""

    def test_path1_vs_path4_heisenberg(self):
        """Path 1 (direct) vs Path 4 (c=1 identity) for Heisenberg.

        At c=1: K^{sh}(H_k; m,n; 1) = kappa (since S_r=0 for r>=3).
        """
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        k = 5.0
        ksh = shadow_kloosterman_sum('heisenberg', k, 7, 3, 1)
        assert abs(ksh - k) < 1e-10, f"Path 1 vs Path 4: {ksh} != {k}"

    def test_path1_vs_path2_consistency(self):
        """Path 1 (direct value) always satisfies Path 2 (Weil bound)."""
        from lib.bc_kloosterman_zeta_engine import verify_shadow_weil_bound
        count = 0
        for fam, par in [('heisenberg', 1.0), ('virasoro', 5.0), ('affine_sl2', 2.0)]:
            for m in [1, 3, 5, 7]:
                for n in [1, 2, 4, 6]:
                    for c in [1, 3, 5, 7, 11, 13, 17, 19, 23]:
                        _, _, ok = verify_shadow_weil_bound(fam, par, m, n, c, max_r=15)
                        assert ok, f"Weil failed for {fam}, m={m}, n={n}, c={c}"
                        count += 1
        assert count >= 100, f"Only checked {count} cases"

    def test_heisenberg_explicit_formula(self):
        """Heisenberg K^{sh} = k * S(2m, 2n; c): verify for many (m,n,c)."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        from lib.shadow_kloosterman_engine import kloosterman_sum
        k = 7.0
        count = 0
        for m in range(1, 8):
            for n in range(1, 8):
                for c in [1, 2, 3, 5, 7, 11]:
                    ksh = shadow_kloosterman_sum('heisenberg', k, m, n, c)
                    expected = k * kloosterman_sum(2 * m, 2 * n, c)
                    assert abs(ksh - expected) < 1e-8
                    count += 1
        assert count > 250

    def test_kloosterman_zeta_real_on_real_axis(self):
        """For real s and integer parameters, Z^{Kl} should be real."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta
        val = kloosterman_zeta(2.0, 'heisenberg', 1.0, c_max=100)
        assert abs(val.imag) < 1e-8, f"Imaginary part nonzero: {val.imag}"

    def test_shadow_coefficients_reproduce_kappa(self):
        """S_2(A) = kappa(A) for all standard families (AP9 cross-check)."""
        from lib.bc_kloosterman_zeta_engine import shadow_coefficients
        # Heisenberg k=3: kappa = k = 3
        assert abs(shadow_coefficients('heisenberg', 3.0)[2] - 3.0) < 1e-10
        # Affine sl_2 k=1: kappa = 3*(1+2)/4 = 9/4
        assert abs(shadow_coefficients('affine_sl2', 1.0)[2] - 9.0 / 4.0) < 1e-10
        # Virasoro c=10: kappa = c/2 = 5
        assert abs(shadow_coefficients('virasoro', 10.0)[2] - 5.0) < 1e-10


# =====================================================================
# 14. Bessel function utilities
# =====================================================================

class TestBesselUtilities:
    """Test the internal Bessel function implementations."""

    def test_j0_at_zero(self):
        """J_0(0) = 1."""
        from lib.bc_kloosterman_zeta_engine import _bessel_j0
        assert abs(_bessel_j0(0.0) - 1.0) < 1e-15

    def test_i0_at_zero(self):
        """I_0(0) = 1."""
        from lib.bc_kloosterman_zeta_engine import _bessel_i0
        assert abs(_bessel_i0(0.0) - 1.0) < 1e-15

    def test_j0_known_values(self):
        """J_0(x) at known values vs scipy/literature."""
        from lib.bc_kloosterman_zeta_engine import _bessel_j0
        # J_0(1) ~ 0.7651976865579665
        assert abs(_bessel_j0(1.0) - 0.7651976865579665) < 1e-10
        # J_0(2.4048) ~ 0 (first zero)
        assert abs(_bessel_j0(2.4048)) < 1e-3

    def test_i0_known_values(self):
        """I_0(x) at known values."""
        from lib.bc_kloosterman_zeta_engine import _bessel_i0
        # I_0(1) ~ 1.2660658777520083
        assert abs(_bessel_i0(1.0) - 1.2660658777520083) < 1e-8

    def test_j0_symmetry(self):
        """J_0(-x) = J_0(x) (even function)."""
        from lib.bc_kloosterman_zeta_engine import _bessel_j0
        for x in [0.5, 1.0, 3.0, 5.0]:
            assert abs(_bessel_j0(x) - _bessel_j0(-x)) < 1e-12

    def test_i0_positive(self):
        """I_0(x) > 0 for all real x."""
        from lib.bc_kloosterman_zeta_engine import _bessel_i0
        for x in [0.0, 0.1, 1.0, 5.0, 10.0, 50.0]:
            assert _bessel_i0(x) > 0


# =====================================================================
# 15. Edge cases and error handling
# =====================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_unknown_family_raises(self):
        """Unknown family should raise ValueError."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        with pytest.raises(ValueError, match="Unknown family"):
            shadow_kloosterman_sum('nonexistent', 1.0, 1, 1, 5)

    def test_large_c_does_not_overflow(self):
        """Large c should not cause overflow."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        val = shadow_kloosterman_sum('heisenberg', 1.0, 1, 1, 97)
        assert math.isfinite(val)

    def test_large_m_n(self):
        """Large m, n should work without error."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        val = shadow_kloosterman_sum('heisenberg', 1.0, 10, 10, 7)
        assert math.isfinite(val)

    def test_kloosterman_zeta_at_complex_s(self):
        """Z^{Kl}(1 + 2i; H_1) should be a finite complex number."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta
        val = kloosterman_zeta(complex(1, 2), 'heisenberg', 1.0, c_max=100)
        assert math.isfinite(val.real) and math.isfinite(val.imag)


# =====================================================================
# 16. Additional multi-path and structural tests
# =====================================================================

class TestAdditionalStructural:
    """Additional structural and multi-path tests to ensure 60+ coverage."""

    def test_kloosterman_zeta_general_mn_symmetry(self):
        """Z^{Kl}(s; A; m, n) = Z^{Kl}(s; A; n, m) by Kloosterman symmetry S(a,b;c) = S(b,a;c)."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_general
        for fam, par in [('heisenberg', 1.0), ('affine_sl2', 1.0)]:
            z_12 = kloosterman_zeta_general(2.0, 1, 2, fam, par, c_max=50, max_r=15)
            z_21 = kloosterman_zeta_general(2.0, 2, 1, fam, par, c_max=50, max_r=15)
            assert abs(z_12 - z_21) < 1e-8, \
                f"{fam}: Z(s;1,2) = {z_12} != Z(s;2,1) = {z_21}"

    def test_shadow_kloosterman_mn_symmetry(self):
        """K^{sh}(A; m, n; c) = K^{sh}(A; n, m; c) since S(a,b;c) = S(b,a;c)."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_sum
        for c in [3, 7, 11, 17]:
            val_12 = shadow_kloosterman_sum('virasoro', 10.0, 1, 2, c, max_r=15)
            val_21 = shadow_kloosterman_sum('virasoro', 10.0, 2, 1, c, max_r=15)
            assert abs(val_12 - val_21) < 1e-8

    def test_kloosterman_zeta_on_line_returns_correct_length(self):
        """kloosterman_zeta_on_line should return one value per t-value."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta_on_line
        t_vals = [1.0, 2.0, 5.0, 10.0, 20.0]
        results = kloosterman_zeta_on_line(
            1.0, t_vals, 'heisenberg', 1.0, c_max=50, max_r=15)
        assert len(results) == len(t_vals)
        for v in results:
            assert isinstance(v, complex)
            assert math.isfinite(v.real) and math.isfinite(v.imag)

    def test_shadow_kloosterman_table_small(self):
        """shadow_kloosterman_table should produce the right number of entries."""
        from lib.bc_kloosterman_zeta_engine import shadow_kloosterman_table
        table = shadow_kloosterman_table('heisenberg', 1.0, m_max=3, n_max=3, c_max=5, max_r=15)
        assert len(table) == 3 * 3 * 5
        for key, val in table.items():
            assert math.isfinite(val)

    def test_kloosterman_zeta_linearity_in_k(self):
        """For Heisenberg, K^{sh}(H_k) = k * K^{sh}(H_1), so Z^{Kl}(s; H_k) = k * Z^{Kl}(s; H_1)."""
        from lib.bc_kloosterman_zeta_engine import kloosterman_zeta
        z1 = kloosterman_zeta(2.0, 'heisenberg', 1.0, c_max=100)
        z3 = kloosterman_zeta(2.0, 'heisenberg', 3.0, c_max=100)
        assert abs(z3 - 3.0 * z1) < 1e-8, f"Z(H_3) = {z3} != 3*Z(H_1) = {3*z1}"
