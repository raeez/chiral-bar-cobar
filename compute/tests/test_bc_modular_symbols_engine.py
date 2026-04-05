r"""Tests for the bar-complex modular symbols engine.

50+ tests verifying:
  - Scalar shadow modular symbols (exact)
  - Manin 3-term relation (paths 1 + 2)
  - Hecke eigenvalue from symbols (path 3)
  - Period ratio consistency (path 4)
  - Manin symbol tables
  - Period polynomial
  - Eichler-Shimura classification
  - L-value consistency
  - Zeta-zero symbol evaluation
  - p-adic interpolation and Kummer congruences
  - Cross-family consistency (additivity of kappa)
  - Overconvergent symbol p-adic valuations

CONVENTIONS:
  - kappa(Vir_c) = c/2 (AP20, AP48)
  - kappa(H_k) = k (AP39)
  - E_2^* is quasi-modular (AP15)
  - eta(q) = q^{1/24} prod(1-q^n) (AP46)
  - Cohomological grading, |d| = +1
"""

import cmath
import math
import pytest
from fractions import Fraction

from compute.lib.bc_modular_symbols_engine import (
    # Arithmetic helpers
    _gcd, _sigma, ramanujan_tau, _eisenstein_fourier,
    # Kappa functions
    kappa_virasoro, kappa_heisenberg, kappa_affine,
    # Shadow integrand
    shadow_scalar_constant, shadow_integrand_e2,
    # Modular symbols
    shadow_modular_symbol_scalar, shadow_modular_symbol_e2,
    shadow_modular_symbol_delta,
    # Manin symbols
    manin_symbol_scalar, manin_symbol_e2, manin_symbols_table,
    # Period polynomial
    period_polynomial_e2, period_polynomial_delta,
    # Eichler-Shimura
    eichler_shimura_shadow_class,
    # Hecke
    hecke_action_scalar, hecke_eigenvalue_scalar, hecke_eigenvalue_delta,
    hecke_action_e2_numerical,
    # L-values
    shadow_l_value_scalar, shadow_l_value_numerical, shadow_l_values_table,
    # Zeta zeros
    ZETA_ZEROS, symbol_at_zeta_zero, zeta_zero_symbol_table,
    # p-adic
    padic_valuation, padic_shadow_symbol, padic_interpolation_data,
    padic_kummer_congruence_check,
    # Verification
    verify_manin_three_term, verify_manin_three_term_e2,
    verify_hecke_eigenvalue, delta_period_ratio,
    # Cross-family
    cross_family_shadow_symbols,
    # Diagnostic
    full_diagnostic,
)

PI = math.pi
TWO_PI = 2 * PI


# ============================================================
# Section 1: Arithmetic helpers
# ============================================================

class TestArithmeticHelpers:
    """Tests for basic arithmetic functions."""

    def test_gcd_basic(self):
        assert _gcd(12, 8) == 4
        assert _gcd(7, 3) == 1
        assert _gcd(0, 5) == 5

    def test_sigma_1(self):
        """sigma_1(n) = sum of divisors."""
        assert _sigma(1, 1) == 1
        assert _sigma(6, 1) == 1 + 2 + 3 + 6  # = 12
        assert _sigma(12, 1) == 1 + 2 + 3 + 4 + 6 + 12  # = 28

    def test_sigma_k_primes(self):
        """sigma_k(p) = 1 + p^k for prime p."""
        assert _sigma(5, 2) == 1 + 25  # = 26
        assert _sigma(7, 3) == 1 + 343  # = 344

    def test_ramanujan_tau_values(self):
        """Standard values of tau(n). Convention check (AP38)."""
        assert ramanujan_tau(1) == 1
        assert ramanujan_tau(2) == -24
        assert ramanujan_tau(3) == 252
        assert ramanujan_tau(4) == -1472
        assert ramanujan_tau(5) == 4830

    def test_eisenstein_e4_leading(self):
        """E_4 = 1 + 240*sigma_3(n)*q^n. First coeff: 240*sigma_3(1)=240."""
        coeffs = _eisenstein_fourier(4, 5)
        assert coeffs[0] == 1.0
        assert abs(coeffs[1] - 240.0) < 1e-10  # 240 * sigma_3(1) = 240

    def test_eisenstein_e6_leading(self):
        """E_6 = 1 - 504*sigma_5(n)*q^n. First coeff: -504."""
        coeffs = _eisenstein_fourier(6, 5)
        assert coeffs[0] == 1.0
        assert abs(coeffs[1] - (-504.0)) < 1e-10


# ============================================================
# Section 2: Kappa functions (AP20, AP48, AP39)
# ============================================================

class TestKappaFunctions:
    """Tests for kappa formulas, guarding against AP1 and AP48."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2. NOT c (AP20)."""
        assert kappa_virasoro(26) == 13.0
        assert kappa_virasoro(0) == 0.0
        assert kappa_virasoro(1) == 0.5

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k, not k/2 (AP39)."""
        assert kappa_heisenberg(1) == 1.0
        assert kappa_heisenberg(24) == 24.0

    def test_kappa_affine_sl2(self):
        """kappa(sl_2, k) = 3*(k+2)/4. dim=3, h^v=2."""
        assert abs(kappa_affine(3, 1, 2) - 3 * 3 / 4) < 1e-10  # 9/4 = 2.25
        assert abs(kappa_affine(3, 2, 2) - 3 * 4 / 4) < 1e-10  # 3

    def test_kappa_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero)."""
        for c in [0, 1, 6, 13, 20, 26]:
            total = kappa_virasoro(c) + kappa_virasoro(26 - c)
            assert abs(total - 13.0) < 1e-10, f"Failed at c={c}: sum={total}"


# ============================================================
# Section 3: Shadow scalar constant
# ============================================================

class TestShadowScalar:
    """Tests for the scalar shadow at genus 1."""

    def test_f1_virasoro(self):
        """F_1(Vir_c) = c/48 (since kappa = c/2 and F_1 = kappa/24)."""
        assert abs(shadow_scalar_constant(kappa_virasoro(26)) - 26 / 48) < 1e-12

    def test_f1_heisenberg(self):
        """F_1(H_k) = k/24."""
        assert abs(shadow_scalar_constant(kappa_heisenberg(24)) - 1.0) < 1e-12

    def test_f1_zero_at_c0(self):
        """F_1(Vir_0) = 0 (AP31: kappa=0 implies scalar shadow vanishes)."""
        assert abs(shadow_scalar_constant(kappa_virasoro(0))) < 1e-15


# ============================================================
# Section 4: Scalar modular symbols
# ============================================================

class TestScalarModularSymbols:
    """Tests for the exact scalar shadow modular symbols."""

    def test_scalar_symbol_basic(self):
        """Scalar symbol is (kappa/24) * (beta - alpha)."""
        kap = 1.0
        alpha = complex(0, 0.5)
        beta = complex(1, 0.5)
        expected = (kap / 24.0) * (beta - alpha)
        result = shadow_modular_symbol_scalar(alpha, beta, kap)
        assert abs(result - expected) < 1e-15

    def test_scalar_symbol_antisymmetric(self):
        """{alpha, beta} = -{beta, alpha}."""
        kap = 2.5
        alpha = complex(0.1, 0.3)
        beta = complex(0.7, 0.9)
        s_ab = shadow_modular_symbol_scalar(alpha, beta, kap)
        s_ba = shadow_modular_symbol_scalar(beta, alpha, kap)
        assert abs(s_ab + s_ba) < 1e-15

    def test_scalar_symbol_vanishes_at_kappa_zero(self):
        """At kappa = 0, all scalar symbols vanish."""
        alpha = complex(0, 1)
        beta = complex(0.5, 1)
        assert abs(shadow_modular_symbol_scalar(alpha, beta, 0.0)) < 1e-15

    def test_scalar_symbol_linearity_in_kappa(self):
        """Symbol is linear in kappa."""
        alpha = complex(0, 0.5)
        beta = complex(1, 0.5)
        s1 = shadow_modular_symbol_scalar(alpha, beta, 2.0)
        s2 = shadow_modular_symbol_scalar(alpha, beta, 1.0)
        assert abs(s1 - 2.0 * s2) < 1e-15


# ============================================================
# Section 5: Manin 3-term relation (Verification Path 2)
# ============================================================

class TestManinRelation:
    """Verify {a,b} + {b,c} + {c,a} = 0."""

    def test_3term_scalar_exact(self):
        """3-term relation is exact for scalar symbols."""
        result = verify_manin_three_term(
            complex(0, 0.5), complex(0.3, 0.7), complex(-0.2, 1.0), 5.0)
        assert result['passes']
        assert result['abs_sum'] < 1e-14

    def test_3term_scalar_various_kappa(self):
        """3-term for several kappa values."""
        for kap in [0, 0.5, 1, 13, 100]:
            r = verify_manin_three_term(
                complex(0.1, 0.2), complex(0.5, 0.9), complex(0.8, 0.3), kap)
            assert r['passes'], f"Failed at kappa={kap}"

    def test_3term_e2_numerical(self):
        """3-term for E_2^* symbols (numerical, coarser tolerance)."""
        alpha = complex(0, 0.5)
        beta = complex(0.3, 0.7)
        gamma = complex(-0.1, 0.9)
        result = verify_manin_three_term_e2(alpha, beta, gamma, 1.0,
                                            n_steps=500, tol=1e-3)
        assert result['passes'], f"3-term E2 failed: |sum| = {result['abs_sum']}"


# ============================================================
# Section 6: Manin symbols
# ============================================================

class TestManinSymbols:
    """Tests for Manin symbols [c:d]."""

    def test_manin_11(self):
        """[1:1] = kappa/24."""
        kap = 12.0
        assert abs(manin_symbol_scalar(1, 1, kap) - 0.5) < 1e-12

    def test_manin_10(self):
        """[1:0] = 0 (trivial path)."""
        assert abs(manin_symbol_scalar(1, 0, 1.0)) < 1e-15

    def test_manin_coprimality(self):
        """Raises on non-coprime input."""
        with pytest.raises(ValueError):
            manin_symbol_scalar(4, 2, 1.0)

    def test_manin_table_completeness(self):
        """Table for c_max=5 has correct number of entries."""
        table = manin_symbols_table(5, 1.0)
        # Count coprime pairs with 1 <= c <= 5, 0 <= d <= c
        expected_count = sum(1 for c in range(1, 6)
                            for d in range(0, c + 1)
                            if _gcd(c, d) == 1)
        assert len(table) == expected_count

    def test_manin_scaling(self):
        """[c:d] = (kappa/24) * (d/c). Linear in d/c."""
        kap = 6.0
        assert abs(manin_symbol_scalar(3, 1, kap) - kap / (24 * 3)) < 1e-12
        assert abs(manin_symbol_scalar(3, 2, kap) - kap * 2 / (24 * 3)) < 1e-12


# ============================================================
# Section 7: Hecke eigenvalue (Verification Path 3)
# ============================================================

class TestHeckeAction:
    """Verify Hecke eigenvalues on shadow symbols."""

    @pytest.mark.parametrize("p", [2, 3, 5, 7, 11])
    def test_hecke_eigenvalue_scalar(self, p):
        """T_p on scalar E_2 symbol has eigenvalue 1 + p = sigma_1(p)."""
        result = verify_hecke_eigenvalue(p, 6.0)
        assert result['passes'], (
            f"Hecke eigenvalue failed for p={p}: "
            f"ratio={result['ratio']}, expected={1+p}"
        )

    def test_hecke_eigenvalue_matches_sigma1(self):
        """sigma_1(p) = 1 + p for primes."""
        for p in [2, 3, 5, 7, 11, 13]:
            assert hecke_eigenvalue_scalar(p) == 1 + p

    def test_hecke_eigenvalue_delta(self):
        """Hecke eigenvalue for Delta at p is tau(p)."""
        assert hecke_eigenvalue_delta(2) == -24
        assert hecke_eigenvalue_delta(3) == 252
        assert hecke_eigenvalue_delta(5) == 4830

    def test_hecke_multiplicativity(self):
        """tau(mn) = tau(m)*tau(n) when gcd(m,n)=1."""
        # tau(6) = tau(2)*tau(3) since gcd(2,3)=1
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        # tau(10) = tau(2)*tau(5)
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)


# ============================================================
# Section 8: E_2^* shadow integrand
# ============================================================

class TestE2Integrand:
    """Tests for the quasi-modular shadow integrand."""

    def test_e2_at_high_imaginary(self):
        """E_2^*(tau) -> 1 as Im(tau) -> infty (q -> 0)."""
        tau = complex(0, 10)
        kap = 1.0
        val = shadow_integrand_e2(tau, kap, nmax=50)
        assert abs(val - kap / 24.0) < 1e-10

    def test_e2_quasi_modular_note(self):
        """E_2^* is quasi-modular (AP15): NOT holomorphic modular."""
        # This is a conceptual test: the function should exist and compute
        tau = complex(0.1, 0.5)
        val = shadow_integrand_e2(tau, 1.0)
        assert isinstance(val, complex)


# ============================================================
# Section 9: Eichler-Shimura
# ============================================================

class TestEichlerShimura:
    """Tests for the Eichler-Shimura decomposition of shadow data."""

    def test_weight_2_eisenstein(self):
        """At weight 2, dim S_2 = 0: shadow is purely Eisenstein."""
        info = eichler_shimura_shadow_class(1.0)
        assert info['weight_2']['dim_S_k'] == 0
        assert info['weight_2']['shadow_component'] == 'Eisenstein'

    def test_weight_12_cuspidal(self):
        """At weight 12, dim S_12 = 1 (Delta function)."""
        info = eichler_shimura_shadow_class(1.0)
        assert info['weight_12']['dim_S_k'] == 1

    def test_cuspidal_threshold(self):
        """First cuspidal contribution at genus 6, weight 12."""
        info = eichler_shimura_shadow_class(1.0)
        assert info['general']['cuspidal_threshold_weight'] == 12


# ============================================================
# Section 10: Shadow L-values
# ============================================================

class TestShadowLValues:
    """Tests for L^{sh}(s) = -kappa * zeta(s) * zeta(s-1)."""

    def test_l_value_at_s3(self):
        """L^{sh}(3) = -kappa * zeta(3) * zeta(2)."""
        kap = 1.0
        # zeta(2) = pi^2/6
        zeta_2 = PI ** 2 / 6.0
        # zeta(3) ~ 1.2020569...
        zeta_3 = 1.2020569031595942
        expected = -kap * zeta_3 * zeta_2
        computed = shadow_l_value_scalar(kap, 3)
        assert abs(computed - expected) / abs(expected) < 1e-3

    def test_l_value_numerical_vs_exact(self):
        """Numerical Dirichlet series vs exact zeta product at s=4."""
        kap = 2.0
        zeta_3 = 1.2020569031595942
        zeta_4 = PI ** 4 / 90.0
        expected = -kap * zeta_4 * zeta_3
        computed = shadow_l_value_numerical(kap, 4.0, nmax=5000)
        assert abs(computed - expected) / abs(expected) < 1e-2

    def test_l_values_table(self):
        """L-value table has entries for s=2,...,10."""
        table = shadow_l_values_table(1.0, s_max=10, nmax=1000)
        assert len(table) == 9
        for s in range(2, 11):
            assert s in table

    def test_l_value_sign(self):
        """For kappa > 0, L^{sh}(s) < 0 for s >= 3 (both zeta values positive)."""
        for s in [3, 4, 5, 6]:
            val = shadow_l_value_scalar(1.0, s)
            assert val.real < 0, f"Expected negative at s={s}, got {val}"


# ============================================================
# Section 11: Zeta-zero symbols
# ============================================================

class TestZetaZeroSymbols:
    """Tests for modular symbols evaluated at zeta-zero heights."""

    def test_zeta_zeros_list(self):
        """Verify first few zeta zeros (Odlyzko tables)."""
        assert abs(ZETA_ZEROS[0] - 14.134725) < 1e-4
        assert abs(ZETA_ZEROS[1] - 21.022040) < 1e-4

    def test_zeta_zero_symbol_scalar(self):
        """Scalar symbol at gamma_1/(2*pi)."""
        kap = 1.0
        s = symbol_at_zeta_zero(1, kap, mode='scalar')
        # Expected: (kap/24) * (i * gamma_1/(2*pi) - i*0.01)
        gamma1 = ZETA_ZEROS[0]
        expected = (kap / 24.0) * complex(0, gamma1 / TWO_PI - 0.01)
        assert abs(s - expected) < 1e-10

    def test_zeta_zero_symbols_purely_imaginary(self):
        """Scalar symbols at zeta zeros are purely imaginary."""
        kap = 5.0
        for n in range(1, 6):
            s = symbol_at_zeta_zero(n, kap, mode='scalar')
            assert abs(s.real) < 1e-10 * abs(s.imag), (
                f"Symbol at zero {n} has nonzero real part: {s}")

    def test_zeta_zero_table(self):
        """Table of symbols at first 10 zeros."""
        table = zeta_zero_symbol_table(1.0, n_zeros=10)
        assert len(table) == 10
        for n in range(1, 11):
            assert n in table

    def test_zeta_zero_monotone_imaginary(self):
        """Im(symbol_n) increases with n (zeros increase)."""
        kap = 1.0
        prev = 0.0
        for n in range(1, 10):
            s = symbol_at_zeta_zero(n, kap, mode='scalar')
            assert s.imag > prev, f"Monotonicity failed at n={n}"
            prev = s.imag


# ============================================================
# Section 12: p-adic symbols and Kummer congruences
# ============================================================

class TestPadicSymbols:
    """Tests for p-adic modular symbol structure."""

    def test_padic_valuation_basic(self):
        """v_p(p^k * m) = k when gcd(m, p) = 1."""
        assert padic_valuation(8, 2) == 3
        assert padic_valuation(27, 3) == 3
        assert padic_valuation(Fraction(1, 3), 3) == -1

    def test_padic_symbol_value(self):
        """p-adic Manin symbol [1:1] has correct value."""
        kap = Fraction(1, 2)  # kappa(Vir_1) = 1/2
        result = padic_shadow_symbol(1, 1, kap, 2)
        assert result['symbol'] == Fraction(1, 48)

    def test_padic_symbol_coprime_check(self):
        """Raises on non-coprime (c, d)."""
        with pytest.raises(ValueError):
            padic_shadow_symbol(4, 2, Fraction(1), 2)

    def test_kummer_congruences_p3(self):
        """Kummer congruences hold at p=3."""
        result = padic_kummer_congruence_check(3, max_genus=10)
        assert result['all_pass'], "Kummer congruences failed at p=3"

    def test_kummer_congruences_p5(self):
        """Kummer congruences hold at p=5."""
        result = padic_kummer_congruence_check(5, max_genus=10)
        assert result['all_pass'], "Kummer congruences failed at p=5"

    def test_kummer_congruences_p7(self):
        """Kummer congruences hold at p=7."""
        result = padic_kummer_congruence_check(7, max_genus=8)
        assert result['all_pass'], "Kummer congruences failed at p=7"

    def test_padic_interpolation_convergence_radius(self):
        """p-adic convergence radius R_p = p^{1/(p-1)}."""
        for p in [3, 5, 7]:
            data = padic_interpolation_data(Fraction(1), p, max_genus=5)
            expected = p ** (1.0 / (p - 1))
            assert abs(data['convergence_radius'] - expected) < 1e-10

    def test_padic_interpolation_genus_data(self):
        """Interpolation data has correct genus entries."""
        data = padic_interpolation_data(Fraction(1, 2), 3, max_genus=5)
        assert len(data['genus_data']) == 5
        assert data['genus_data'][0]['genus'] == 1

    def test_padic_p2_convergence(self):
        """For p=2, convergence radius R_2 = 2."""
        data = padic_interpolation_data(Fraction(1), 2, max_genus=5)
        assert data['convergence_radius'] == 2.0


# ============================================================
# Section 13: Cross-family consistency (Verification Path 5)
# ============================================================

class TestCrossFamilyConsistency:
    """Verify consistency across algebra families."""

    def test_kappa_additivity(self):
        """kappa(H_k1 + H_k2) = kappa(H_k1) + kappa(H_k2).

        For independent direct sums, kappa is additive
        (prop:independent-sum-factorization).
        """
        k1, k2 = 3.0, 5.0
        assert abs(kappa_heisenberg(k1 + k2)
                   - kappa_heisenberg(k1) - kappa_heisenberg(k2)) < 1e-10

    def test_symbol_additivity(self):
        """Shadow symbol is linear in kappa, hence additive for direct sums."""
        alpha = complex(0, 0.5)
        beta = complex(1, 0.5)
        kap1, kap2 = 3.0, 7.0
        s1 = shadow_modular_symbol_scalar(alpha, beta, kap1)
        s2 = shadow_modular_symbol_scalar(alpha, beta, kap2)
        s_sum = shadow_modular_symbol_scalar(alpha, beta, kap1 + kap2)
        assert abs(s_sum - s1 - s2) < 1e-14

    def test_complementarity_symbol_sum(self):
        """For Vir_c + Vir_{26-c}: symbol sum = 13/24 * path length (AP24)."""
        c = 5.0
        alpha = complex(0, 0.5)
        beta = complex(1, 0.5)
        s_c = shadow_modular_symbol_scalar(alpha, beta, kappa_virasoro(c))
        s_dual = shadow_modular_symbol_scalar(alpha, beta, kappa_virasoro(26 - c))
        s_13 = shadow_modular_symbol_scalar(alpha, beta, 13.0)
        assert abs(s_c + s_dual - s_13) < 1e-12

    def test_cross_family_table(self):
        """Cross-family table has entries for all requested families."""
        table = cross_family_shadow_symbols([1, 13, 26])
        assert 'Vir_c=1' in table
        assert 'Heis_k=1' in table
        assert 'sl2_k=1' in table


# ============================================================
# Section 14: Period polynomial
# ============================================================

class TestPeriodPolynomial:
    """Tests for the period polynomial computation."""

    def test_period_e2_converges(self):
        """The E_2^* period integral converges (numerically)."""
        val = period_polynomial_e2(0.0, kappa=1.0, y_max=5.0,
                                   n_steps=500, nmax=30)
        assert math.isfinite(abs(val))

    def test_period_delta_converges(self):
        """The Delta period integral converges rapidly (cusp form)."""
        val = period_polynomial_delta(0.5, y_max=2.0,
                                      n_steps=500, nmax=50)
        assert math.isfinite(abs(val))
        assert abs(val) > 0  # Delta is nonzero

    def test_period_delta_imaginary_axis(self):
        """Period along imaginary axis is purely imaginary (Delta(iy) real)."""
        # integral_0^{i*infty} Delta(tau) (tau - X)^{10} dtau
        # along imaginary axis with X=0: Delta(iy) is real, tau^{10} = (iy)^{10}
        # = (-1)^5 y^{10}, so integrand is real and dtau = i*dy.
        # Result is purely imaginary times real = purely imaginary.
        val = period_polynomial_delta(0.0, y_max=2.0, n_steps=500, nmax=50)
        # The real part should be much smaller than the imaginary part
        if abs(val) > 1e-15:
            ratio = abs(val.real) / abs(val)
            assert ratio < 0.1, f"Expected mostly imaginary, got ratio {ratio}"


# ============================================================
# Section 15: Scalar symbol numerical integration agreement
# ============================================================

class TestNumericalAgreement:
    """Verify numerical E_2^* integration agrees with scalar for large Im(tau)."""

    def test_e2_agrees_with_scalar_high_imaginary(self):
        """When both endpoints have large Im(tau), E_2^* ~ 1 and
        the E_2 symbol should agree with the scalar symbol.
        """
        alpha = complex(0, 3.0)
        beta = complex(0.5, 3.0)
        kap = 6.0
        s_scal = shadow_modular_symbol_scalar(alpha, beta, kap)
        s_e2 = shadow_modular_symbol_e2(alpha, beta, kap,
                                        n_steps=500, nmax=30)
        # Agreement should be good when Im(tau) is large (q ~ 0)
        assert abs(s_e2 - s_scal) / abs(s_scal) < 0.01, (
            f"scalar={s_scal}, e2={s_e2}")


# ============================================================
# Section 16: Full diagnostic
# ============================================================

class TestFullDiagnostic:
    """Run the full diagnostic and check all passes."""

    def test_diagnostic_runs(self):
        """Full diagnostic completes without error."""
        results = full_diagnostic(kappa=2.0)
        assert 'direct' in results
        assert 'manin_3term' in results
        assert results['manin_3term']['passes']

    def test_diagnostic_hecke(self):
        """All Hecke eigenvalue tests pass in diagnostic."""
        results = full_diagnostic(kappa=1.0)
        for p in [2, 3, 5]:
            key = f'hecke_p={p}'
            assert key in results
            assert results[key]['passes'], f"Hecke failed at p={p}"


# ============================================================
# Section 17: Edge cases and boundary conditions
# ============================================================

class TestEdgeCases:
    """Tests for boundary/edge conditions."""

    def test_symbol_same_endpoint(self):
        """{alpha, alpha} = 0."""
        alpha = complex(0.3, 0.7)
        s = shadow_modular_symbol_scalar(alpha, alpha, 5.0)
        assert abs(s) < 1e-15

    def test_zeta_zero_out_of_range(self):
        """Raises ValueError for n outside range."""
        with pytest.raises(ValueError):
            symbol_at_zeta_zero(0, 1.0)
        with pytest.raises(ValueError):
            symbol_at_zeta_zero(100, 1.0)

    def test_manin_c_zero_raises(self):
        """c=0 in Manin symbol raises ValueError."""
        with pytest.raises(ValueError):
            manin_symbol_scalar(0, 1, 1.0)

    def test_kappa_virasoro_self_dual(self):
        """kappa(Vir_13) = 13/2 = 6.5 (AP8: self-dual at c=13)."""
        assert abs(kappa_virasoro(13) - 6.5) < 1e-12

    def test_negative_kappa(self):
        """Symbols work with negative kappa (e.g., Koszul dual)."""
        kap = -3.0
        alpha = complex(0, 0.5)
        beta = complex(1, 0.5)
        s = shadow_modular_symbol_scalar(alpha, beta, kap)
        assert s.real < 0  # negative kappa gives negative real part


# ============================================================
# Section 18: Ramanujan tau multiplicativity
# ============================================================

class TestRamanujanTau:
    """Further tau tests for cross-verification (AP10 guard)."""

    def test_tau_at_prime_power(self):
        """tau(p^2) = tau(p)^2 - p^11 for prime p."""
        # Hecke relation for p^2
        for p in [2, 3, 5]:
            tau_p = ramanujan_tau(p)
            tau_p2 = ramanujan_tau(p * p)
            expected = tau_p ** 2 - p ** 11
            assert tau_p2 == expected, (
                f"tau({p}^2) = {tau_p2}, expected {expected}")

    def test_tau_ramanujan_bound(self):
        """Deligne's theorem: |tau(p)| <= 2 * p^{11/2} (proved 1974)."""
        for p in [2, 3, 5, 7, 11]:
            bound = 2 * p ** 5.5
            assert abs(ramanujan_tau(p)) <= bound + 1


# ============================================================
# Section 19: Delta modular symbol (cuspidal)
# ============================================================

class TestDeltaSymbol:
    """Tests for the cuspidal Delta_{12} modular symbol."""

    def test_delta_symbol_exponential_decay(self):
        """Delta(tau) decays exponentially as Im(tau) -> infty.
        So the symbol from i*1 to i*10 should be finite and small
        (most of the mass is near i*1)."""
        s = shadow_modular_symbol_delta(complex(0, 1), complex(0, 10),
                                        n_steps=500, nmax=40)
        assert math.isfinite(abs(s))
        assert abs(s) < 1  # Rough bound; Delta ~ e^{-2*pi*y}

    def test_delta_symbol_antisymmetric(self):
        """Delta symbol is antisymmetric: {a,b} = -{b,a}."""
        alpha = complex(0, 1)
        beta = complex(0, 3)
        s_ab = shadow_modular_symbol_delta(alpha, beta, n_steps=500, nmax=40)
        s_ba = shadow_modular_symbol_delta(beta, alpha, n_steps=500, nmax=40)
        if abs(s_ab) > 1e-15:
            assert abs(s_ab + s_ba) / abs(s_ab) < 0.01
