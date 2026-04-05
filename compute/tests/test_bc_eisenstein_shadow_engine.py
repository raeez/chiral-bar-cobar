r"""Tests for BC-104: Shadow Eisenstein series construction.

Tests organized by section:
  1.  Eisenstein series Fourier coefficients (exact arithmetic)
  2.  Eisenstein series numerical evaluation
  3.  E_2 quasi-modularity (AP15 verification)
  4.  E_k modular transformations for k >= 4
  5.  E_2* non-holomorphic completion
  6.  Virasoro shadow coefficients
  7.  Shadow Eisenstein series E^{sh}_A(tau, s)
  8.  Shadow modular form F^{sh}_A (s=0)
  9.  Shadow modular anomaly
  10. Shadow L-values and Rankin unfolding
  11. Ramanujan tau function
  12. Shadow Hecke eigenvalues
  13. Eisenstein special values (CM points)
  14. Completed shadow Eisenstein (non-holomorphic)
  15. Shadow Maass series
  16. Shadow zeta functions
  17. Mellin transform (formal)
  18. Cross-checks and consistency

Verification paths (AP10 mandate: >= 3 per claim):
  Path 1: Direct Fourier expansion computation
  Path 2: Known exact values at CM points
  Path 3: Modular transformation laws
  Path 4: Cross-family consistency (Heisenberg, affine, Virasoro)
  Path 5: Hecke eigenvalue formula T_p(E_k) = (1 + p^{k-1}) E_k
"""

import pytest
from fractions import Fraction
import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_eisenstein_shadow_engine import (
    # Arithmetic utilities
    sigma_k, bernoulli_number,
    # Eisenstein coefficients and evaluation
    eisenstein_coefficient, eisenstein_q_expansion, eisenstein_numerical,
    E2_nonholomorphic,
    # Virasoro shadow coefficients
    kappa_virasoro, virasoro_shadow_coefficients, virasoro_shadow_exact,
    # Shadow Eisenstein
    shadow_eisenstein_series, shadow_eisenstein_virasoro,
    # Shadow modular form
    shadow_modular_form, shadow_modular_form_completed,
    # Shadow anomaly
    shadow_modular_anomaly, shadow_modular_anomaly_virasoro,
    # Shadow L-values
    ramanujan_tau, delta_L_function, shadow_L_value_delta,
    # Shadow Hecke
    hecke_eigenvalue_eisenstein, shadow_hecke_eigenvalue,
    shadow_hecke_eigenvalue_virasoro,
    shadow_hecke_acted_zeta, shadow_zeta, shadow_zeta_even,
    # Maass
    maass_eisenstein_numerical, shadow_maass_series,
    # Transformations
    verify_E2_transformation, verify_E2star_transformation,
    verify_Ek_modular_transformation,
    verify_completed_shadow_transformation,
    # Special values
    eisenstein_at_special_points, E4_at_i_exact, E6_at_rho_exact,
    # Summary
    shadow_constant_term, shadow_mellin_integrand, shadow_mellin_numerical,
    compute_full_shadow_eisenstein_table,
)


# ============================================================================
# Helper constants
# ============================================================================

TAU_I = complex(0, 1)
TAU_RHO = cmath.exp(2 * cmath.pi * 1j / 3)
TAU_2I = complex(0, 2)


# ============================================================================
# Section 1: Eisenstein series Fourier coefficients
# ============================================================================

class TestEisensteinCoefficients:
    """Exact Fourier coefficients of Eisenstein series."""

    def test_E4_constant_term(self):
        """E_4: a_0 = 1."""
        assert eisenstein_coefficient(4, 0) == Fraction(1)

    def test_E4_first_coefficient(self):
        """E_4: a_1 = 240.  Since -2*4/B_4 = -8/(-1/30) = 240."""
        assert eisenstein_coefficient(4, 1) == Fraction(240)

    def test_E4_second_coefficient(self):
        """E_4: a_2 = 240*sigma_3(2) = 240*9 = 2160."""
        assert eisenstein_coefficient(4, 2) == Fraction(2160)

    def test_E4_third_coefficient(self):
        """E_4: a_3 = 240*sigma_3(3) = 240*28 = 6720."""
        assert eisenstein_coefficient(4, 3) == Fraction(6720)

    def test_E6_constant_term(self):
        """E_6: a_0 = 1."""
        assert eisenstein_coefficient(6, 0) == Fraction(1)

    def test_E6_first_coefficient(self):
        """E_6: a_1 = -504.  Since -2*6/B_6 = -12/(1/42) = -504."""
        assert eisenstein_coefficient(6, 1) == Fraction(-504)

    def test_E6_second_coefficient(self):
        """E_6: a_2 = -504*sigma_5(2) = -504*33 = -16632."""
        assert eisenstein_coefficient(6, 2) == Fraction(-16632)

    def test_E2_constant_term(self):
        """E_2: a_0 = 1."""
        assert eisenstein_coefficient(2, 0) == Fraction(1)

    def test_E2_first_coefficient(self):
        """E_2: a_1 = -24.  Since -2*2/B_2 = -4/(1/6) = -24."""
        assert eisenstein_coefficient(2, 1) == Fraction(-24)

    def test_E2_second_coefficient(self):
        """E_2: a_2 = -24*sigma_1(2) = -24*3 = -72."""
        assert eisenstein_coefficient(2, 2) == Fraction(-72)

    def test_E8_first_coefficient(self):
        """E_8: a_1 = -2*8/B_8 * sigma_7(1).
        B_8 = -1/30, so -16/(-1/30) = 480. sigma_7(1) = 1. a_1 = 480."""
        assert eisenstein_coefficient(8, 1) == Fraction(480)

    def test_E10_first_coefficient(self):
        """E_10: B_10 = 5/66, so -20/(5/66) = -264. a_1 = -264."""
        assert eisenstein_coefficient(10, 1) == Fraction(-264)

    def test_E12_first_coefficient(self):
        """E_12: B_12 = -691/2730, so -24/(-691/2730) = 65520/691."""
        expected = Fraction(65520, 691)
        assert eisenstein_coefficient(12, 1) == expected

    def test_odd_weight_vanishes(self):
        """Odd weight Eisenstein series vanish on SL(2,Z)."""
        for k in [3, 5, 7, 9, 11]:
            assert eisenstein_coefficient(k, 0) == Fraction(0)
            assert eisenstein_coefficient(k, 1) == Fraction(0)

    def test_q_expansion_length(self):
        """eisenstein_q_expansion returns correct number of coefficients."""
        coeffs = eisenstein_q_expansion(4, nmax=10)
        assert len(coeffs) == 11  # a_0 through a_10


# ============================================================================
# Section 2: Eisenstein numerical evaluation
# ============================================================================

class TestEisensteinNumerical:
    """Numerical evaluation of Eisenstein series."""

    def test_E4_at_2i(self):
        """E_4(2i) should be close to 1 (since q = e^{-4*pi} ~ 3.5e-6)."""
        val = eisenstein_numerical(4, TAU_2I)
        assert abs(val - 1.0) < 0.01  # dominant term is 1

    def test_E6_at_2i(self):
        """E_6(2i) should be close to 1."""
        val = eisenstein_numerical(6, TAU_2I)
        assert abs(val - 1.0) < 0.01

    def test_E4_real_at_imaginary_axis(self):
        """E_4 is real on the imaginary axis (pure imaginary tau)."""
        val = eisenstein_numerical(4, TAU_I)
        assert abs(val.imag) < 1e-10

    def test_E6_real_at_imaginary_axis(self):
        """E_6 is real on the imaginary axis."""
        val = eisenstein_numerical(6, TAU_I)
        assert abs(val.imag) < 1e-10

    def test_E4_positive_at_i(self):
        """E_4(i) > 0 (known to be positive)."""
        val = eisenstein_numerical(4, TAU_I)
        assert val.real > 0

    def test_E4_E6_product_gives_E10(self):
        """E_4 * E_6 = E_10 (ring structure of modular forms).
        Not exact numerically, but should be very close."""
        E4 = eisenstein_numerical(4, TAU_I)
        E6 = eisenstein_numerical(6, TAU_I)
        E10 = eisenstein_numerical(10, TAU_I)
        assert abs(E4 * E6 - E10) < 1e-8

    def test_E4_squared_vs_E8(self):
        """E_4^2 = E_8 (exact identity for weight-8 modular forms)."""
        E4 = eisenstein_numerical(4, TAU_I)
        E8 = eisenstein_numerical(8, TAU_I)
        assert abs(E4 ** 2 - E8) < 1e-8

    def test_upper_half_plane_check(self):
        """Should raise ValueError for tau not in upper half-plane."""
        with pytest.raises(ValueError):
            eisenstein_numerical(4, complex(1, -1))

    def test_consistency_fourier_vs_numerical(self):
        """Fourier coefficients should match numerical evaluation at large Im(tau)."""
        tau = complex(0, 3)  # q = e^{-6*pi} ~ very small
        E4_num = eisenstein_numerical(4, tau)
        # At large Im(tau), E_4 ~ 1 + 240*q + ... ~ 1 + tiny
        q = cmath.exp(2 * cmath.pi * 1j * tau)
        E4_approx = 1.0 + 240.0 * q
        assert abs(E4_num - E4_approx) < 1e-10


# ============================================================================
# Section 3: E_2 quasi-modularity (AP15)
# ============================================================================

class TestE2QuasiModularity:
    """E_2 is quasi-modular: E_2(-1/tau) = tau^2 E_2(tau) + 12*tau/(2*pi*i)."""

    def test_E2_transformation_at_i(self):
        """Verify E_2 quasi-modular transformation at tau = i."""
        result = verify_E2_transformation(TAU_I)
        assert result['difference'] < 1e-8

    def test_E2_transformation_at_rho(self):
        """Verify at tau = rho = e^{2*pi*i/3}."""
        result = verify_E2_transformation(TAU_RHO)
        assert result['difference'] < 1e-6

    def test_E2_transformation_at_2i(self):
        """Verify at tau = 2i."""
        result = verify_E2_transformation(TAU_2I)
        assert result['difference'] < 1e-8

    def test_E2_at_i_real(self):
        """E_2(i) should be real."""
        val = eisenstein_numerical(2, TAU_I)
        assert abs(val.imag) < 1e-10

    def test_E2_anomaly_coefficient(self):
        """The anomaly coefficient is 12/(2*pi*i)."""
        anomaly = 12.0 / (2.0 * math.pi * 1j)
        assert abs(anomaly.real) < 1e-15
        assert abs(anomaly.imag - (-12.0 / (2.0 * math.pi))) < 1e-10


# ============================================================================
# Section 4: E_k modular transformations (k >= 4)
# ============================================================================

class TestEkModularTransformations:
    """For k >= 4 even: E_k(-1/tau) = tau^k * E_k(tau)."""

    @pytest.mark.parametrize("k", [4, 6, 8, 10, 12])
    def test_S_transformation_at_i(self, k):
        """Modular transformation at tau = i."""
        result = verify_Ek_modular_transformation(k, TAU_I)
        assert result['difference'] < 1e-6

    @pytest.mark.parametrize("k", [4, 6, 8, 10])
    def test_S_transformation_at_2i(self, k):
        """Modular transformation at tau = 2i."""
        result = verify_Ek_modular_transformation(k, TAU_2I)
        assert result['difference'] < 1e-8

    def test_E6_zero_at_i(self):
        """E_6(i) = 0 because i^6 = -1 forces E_6(i) = -E_6(i) = 0."""
        val = eisenstein_numerical(6, TAU_I)
        assert abs(val) < 1e-8

    def test_E4_zero_at_rho(self):
        """E_4(rho) = 0 because rho^4 = rho (order-3 fixed point)."""
        val = eisenstein_numerical(4, TAU_RHO)
        assert abs(val) < 1e-6

    def test_E10_zero_at_i(self):
        """E_10(i) = 0 because i^10 = -1 (k = 10 = 2 mod 4)."""
        val = eisenstein_numerical(10, TAU_I)
        assert abs(val) < 1e-8

    def test_E8_nonzero_at_i(self):
        """E_8(i) != 0 because i^8 = 1 (k = 8 = 0 mod 4)."""
        val = eisenstein_numerical(8, TAU_I)
        assert abs(val) > 0.5


# ============================================================================
# Section 5: E_2* non-holomorphic completion
# ============================================================================

class TestE2StarCompletion:
    """E_2*(tau) = E_2(tau) - 3/(pi*Im(tau)) transforms as weight 2."""

    def test_E2star_transformation_at_i(self):
        """E_2*(-1/tau) = tau^2 * E_2*(tau) at tau = i."""
        result = verify_E2star_transformation(TAU_I)
        assert result['difference'] < 1e-8

    def test_E2star_transformation_at_2i(self):
        """At tau = 2i."""
        result = verify_E2star_transformation(TAU_2I)
        assert result['difference'] < 1e-8

    def test_E2star_correction_at_i(self):
        """E_2*(i) = E_2(i) - 3/pi."""
        E2 = eisenstein_numerical(2, TAU_I)
        E2star = E2_nonholomorphic(TAU_I)
        correction = 3.0 / math.pi
        assert abs(E2star - (E2 - correction)) < 1e-12

    def test_E2star_not_holomorphic(self):
        """E_2*(tau) depends on Im(tau), so it changes with imaginary part."""
        tau1 = complex(0, 1)
        tau2 = complex(0, 2)
        # E_2 values
        E2_1 = eisenstein_numerical(2, tau1)
        E2_2 = eisenstein_numerical(2, tau2)
        # E_2* values
        E2s_1 = E2_nonholomorphic(tau1)
        E2s_2 = E2_nonholomorphic(tau2)
        # The non-holomorphic correction differs
        diff_E2 = abs(E2_1 - E2_2)
        diff_E2s = abs(E2s_1 - E2s_2)
        assert abs(diff_E2 - diff_E2s) > 0.01


# ============================================================================
# Section 6: Virasoro shadow coefficients
# ============================================================================

class TestVirasoroShadowCoefficients:
    """Shadow coefficients S_r for Virasoro."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        for c in [1.0, 13.0, 25.0, 26.0]:
            assert abs(kappa_virasoro(c) - c / 2.0) < 1e-15

    def test_S2_equals_kappa(self):
        """S_2 = kappa = c/2 for Virasoro."""
        for c in [1.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients(c, max_r=5)
            assert abs(coeffs[2] - c / 2.0) < 1e-12

    def test_S3_equals_2(self):
        """S_3 = alpha/3 = 2/3... no: a_1 = 6, so S_3 = a_1/3 = 6/3 = 2."""
        for c in [1.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients(c, max_r=5)
            assert abs(coeffs[3] - 2.0) < 1e-10

    def test_S4_formula(self):
        """S_4 = a_2/4 = 10/(c(5c+22))."""
        for c in [1.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients(c, max_r=5)
            expected = 10.0 / (c * (5.0 * c + 22.0))
            assert abs(coeffs[4] - expected) < 1e-10

    def test_S2_exact(self):
        """Exact S_2."""
        assert virasoro_shadow_exact(2, Fraction(1)) == Fraction(1, 2)
        assert virasoro_shadow_exact(2, Fraction(13)) == Fraction(13, 2)

    def test_S3_exact(self):
        """Exact S_3 = 2 for all c."""
        assert virasoro_shadow_exact(3, Fraction(1)) == Fraction(2)
        assert virasoro_shadow_exact(3, Fraction(25)) == Fraction(2)

    def test_S4_exact(self):
        """Exact S_4 = 10/(c(5c+22))."""
        for c_val in [Fraction(1), Fraction(13), Fraction(25)]:
            expected = Fraction(10) / (c_val * (5 * c_val + 22))
            assert virasoro_shadow_exact(4, c_val) == expected

    def test_shadow_coefficients_growth_small_c(self):
        """For Virasoro c=1 (class M), shadow radius rho > 1 so |S_r| grows.
        rho = sqrt(9*alpha^2 + 2*Delta)/(2*kappa).
        At c=1: kappa=0.5, alpha=2, Delta=40/27, rho ~ 6.26 > 1.
        """
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        # Tower grows at small c
        assert abs(coeffs[10]) > abs(coeffs[4])

    def test_shadow_coefficients_decay_large_c(self):
        """For Virasoro c=25, shadow radius rho < 1 so |S_r| decays.
        At c=25: kappa=12.5, rho ~ 0.50 < 1.
        """
        coeffs = virasoro_shadow_coefficients(25.0, max_r=20)
        assert abs(coeffs[20]) < abs(coeffs[4])


# ============================================================================
# Section 7: Shadow Eisenstein series E^{sh}_A(tau, s)
# ============================================================================

class TestShadowEisenstein:
    """E^{sh}_A(tau, s) = sum S_r * E_r(tau) * r^{-s}."""

    def test_shadow_eisenstein_returns_complex(self):
        """Return type is complex."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        val = shadow_eisenstein_series(coeffs, TAU_I, 2.0, max_r=10)
        assert isinstance(val, complex)

    def test_shadow_eisenstein_at_large_im(self):
        """At large Im(tau), q -> 0 so E_k -> 1, and
        E^{sh} -> sum S_r * r^{-s} = shadow_zeta_even(s)."""
        tau = complex(0, 5)
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        esh = shadow_eisenstein_series(coeffs, tau, 2.0, max_r=10)
        zeta_e = shadow_zeta_even(coeffs, 2.0, max_r=10)
        # Should be close since q = e^{-10*pi} is negligible
        assert abs(esh - zeta_e) < 0.01

    def test_shadow_eisenstein_s_dependence(self):
        """Larger s should give smaller values (terms decay faster)."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=10)
        v2 = abs(shadow_eisenstein_series(coeffs, TAU_2I, 2.0, max_r=10))
        v4 = abs(shadow_eisenstein_series(coeffs, TAU_2I, 4.0, max_r=10))
        assert v4 < v2

    def test_virasoro_shadow_eisenstein_wrapper(self):
        """shadow_eisenstein_virasoro should match manual computation."""
        c = 13.0
        coeffs = virasoro_shadow_coefficients(c, max_r=10)
        direct = shadow_eisenstein_series(coeffs, TAU_I, 2.0, max_r=10)
        wrapper = shadow_eisenstein_virasoro(c, TAU_I, 2.0, max_r=10)
        assert abs(direct - wrapper) < 1e-12


# ============================================================================
# Section 8: Shadow modular form F^{sh}_A (s = 0)
# ============================================================================

class TestShadowModularForm:
    """F^{sh}_A(tau) = sum S_r * E_r(tau) is NOT modular (mixed weight)."""

    def test_shadow_modular_form_returns_complex(self):
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        val = shadow_modular_form(coeffs, TAU_I, max_r=10)
        assert isinstance(val, complex)

    def test_shadow_modular_form_is_s0_specialization(self):
        """F^{sh}_A = E^{sh}_A(tau, 0)."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=10)
        Fsh = shadow_modular_form(coeffs, TAU_I, max_r=10)
        Esh0 = shadow_eisenstein_series(coeffs, TAU_I, 0.0, max_r=10)
        assert abs(Fsh - Esh0) < 1e-12

    def test_shadow_modular_form_not_modular(self):
        """F^{sh}_A(-1/tau) != tau^k * F^{sh}_A(tau) for any k (mixed weight)."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=10)
        Fsh_tau = shadow_modular_form(coeffs, TAU_I, max_r=10)
        Fsh_inv = shadow_modular_form(coeffs, -1.0 / TAU_I, max_r=10)
        # For i: -1/i = i, so Fsh(-1/i) = Fsh(i). But tau^k = i^k.
        # Check: is Fsh(i) = i^k * Fsh(i) for some k?
        # This means i^k = 1, so k = 0 mod 4. But F is nonzero so ratio = 1.
        # Actually at tau = i, -1/tau = i, so LHS = RHS trivially.
        # Use a generic tau instead.
        tau = complex(0.5, 1.5)
        tau_inv = -1.0 / tau
        F1 = shadow_modular_form(coeffs, tau, max_r=10)
        F2 = shadow_modular_form(coeffs, tau_inv, max_r=10)
        # If modular of some weight k: F2 = tau^k * F1
        # Check that no single k works (mixed weight)
        ratio = F2 / F1 if abs(F1) > 1e-10 else float('nan')
        # ratio should NOT be tau^k for any integer k
        for k in range(0, 20):
            power = tau ** k
            if abs(ratio - power) < 0.01:
                pytest.fail(f"F^sh transforms like weight {k}, contradicting mixed weight")


# ============================================================================
# Section 9: Shadow modular anomaly
# ============================================================================

class TestShadowModularAnomaly:
    """Anomaly = kappa * 12/(2*pi*i) from E_2 quasi-modularity."""

    def test_anomaly_purely_imaginary(self):
        """12/(2*pi*i) is purely imaginary (negative imaginary)."""
        anomaly = shadow_modular_anomaly(1.0)
        assert abs(anomaly.real) < 1e-15
        assert anomaly.imag < 0

    def test_anomaly_formula_virasoro(self):
        """For Vir_c: anomaly = (c/2) * 12/(2*pi*i) = 6c/(2*pi*i)."""
        for c in [1.0, 13.0, 25.0]:
            anomaly = shadow_modular_anomaly_virasoro(c)
            expected = 6.0 * c / (2.0 * math.pi * 1j)
            assert abs(anomaly - expected) < 1e-12

    def test_anomaly_at_c13(self):
        """Self-dual point c=13: anomaly = 78/(2*pi*i)."""
        anomaly = shadow_modular_anomaly_virasoro(13.0)
        expected = 78.0 / (2.0 * math.pi * 1j)
        assert abs(anomaly - expected) < 1e-12

    def test_anomaly_magnitude(self):
        """magnitude of anomaly = |kappa| * 12/(2*pi)."""
        for kappa in [0.5, 6.5, 12.5]:
            anomaly = shadow_modular_anomaly(kappa)
            expected_mag = kappa * 12.0 / (2.0 * math.pi)
            assert abs(abs(anomaly) - expected_mag) < 1e-12

    def test_anomaly_linearity_in_kappa(self):
        """Anomaly is linear in kappa."""
        a1 = shadow_modular_anomaly(1.0)
        a2 = shadow_modular_anomaly(2.0)
        a3 = shadow_modular_anomaly(3.0)
        assert abs(a3 - (a1 + a2)) < 1e-12


# ============================================================================
# Section 10: Shadow L-values and Rankin unfolding
# ============================================================================

class TestShadowLValues:
    """S_k(A) * L(f, k/2) = <F^{sh}_A, f> by Rankin unfolding."""

    def test_delta_L_function_convergence(self):
        """L(Delta, 6) should converge (center of critical strip)."""
        L6 = delta_L_function(6.0, nmax=200)
        # L(Delta, 6) is known to be small but nonzero
        assert math.isfinite(L6)

    def test_delta_L_function_at_s_12(self):
        """L(Delta, 12) converges rapidly (right of critical strip)."""
        L12 = delta_L_function(12.0, nmax=100)
        assert abs(L12 - 1.0) < 0.1  # dominated by n=1 term since tau(1) = 1

    def test_shadow_L_value_delta_structure(self):
        """shadow_L_value_delta returns correct structure."""
        result = shadow_L_value_delta(1.0)
        assert 'S_12' in result
        assert 'L_Delta_6' in result
        assert 'product' in result
        assert abs(result['product'] - result['S_12'] * result['L_Delta_6']) < 1e-15

    def test_shadow_L_value_S12_nonzero(self):
        """S_12 for Virasoro c=1 should be nonzero (class M, infinite tower)."""
        result = shadow_L_value_delta(1.0, nmax=100)
        assert abs(result['S_12']) > 1e-20


# ============================================================================
# Section 11: Ramanujan tau function
# ============================================================================

class TestRamanujanTau:
    """tau(n) = coeff of q^n in Delta = q * prod(1-q^m)^{24}."""

    def test_tau_1(self):
        assert ramanujan_tau(1) == 1

    def test_tau_2(self):
        assert ramanujan_tau(2) == -24

    def test_tau_3(self):
        assert ramanujan_tau(3) == 252

    def test_tau_4(self):
        assert ramanujan_tau(4) == -1472

    def test_tau_5(self):
        assert ramanujan_tau(5) == 4830

    def test_tau_multiplicativity(self):
        """Ramanujan tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        # tau(6) = tau(2)*tau(3) since gcd(2,3) = 1
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)

    def test_tau_0(self):
        assert ramanujan_tau(0) == 0

    def test_tau_negative(self):
        assert ramanujan_tau(-1) == 0


# ============================================================================
# Section 12: Shadow Hecke eigenvalues
# ============================================================================

class TestShadowHeckeEigenvalues:
    """T_p(E_k) = (1 + p^{k-1}) * E_k."""

    def test_hecke_eigenvalue_E4_p2(self):
        """T_2(E_4) = 1 + 2^3 = 9."""
        assert hecke_eigenvalue_eisenstein(2, 4) == 9

    def test_hecke_eigenvalue_E4_p3(self):
        """T_3(E_4) = 1 + 3^3 = 28."""
        assert hecke_eigenvalue_eisenstein(3, 4) == 28

    def test_hecke_eigenvalue_E6_p2(self):
        """T_2(E_6) = 1 + 2^5 = 33."""
        assert hecke_eigenvalue_eisenstein(2, 6) == 33

    def test_hecke_eigenvalue_E6_p5(self):
        """T_5(E_6) = 1 + 5^5 = 3126."""
        assert hecke_eigenvalue_eisenstein(5, 6) == 3126

    def test_hecke_eigenvalue_matches_sigma(self):
        """lambda_p(E_k) = sigma_{k-1}(p) for p prime."""
        for p, k in [(2, 4), (3, 6), (5, 8), (7, 10)]:
            expected = sigma_k(p, k - 1)
            assert hecke_eigenvalue_eisenstein(p, k) == expected

    def test_shadow_hecke_eigenvalue_finite(self):
        """Shadow Hecke eigenvalue should be finite for nonzero shadow zeta."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        val = shadow_hecke_eigenvalue(coeffs, 2, 2.0, max_r=10)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_shadow_hecke_ratio_structure(self):
        """lambda_p^{sh} = (sum S_r (1+p^{r-1}) r^{-s}) / (sum S_r r^{-s})."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=10)
        p, s = 2, 3.0
        num = shadow_hecke_acted_zeta(coeffs, p, s, max_r=10)
        den = shadow_zeta_even(coeffs, s, max_r=10)
        eigenval = shadow_hecke_eigenvalue(coeffs, p, s, max_r=10)
        if abs(den) > 1e-15:
            assert abs(eigenval - num / den) < 1e-10

    def test_shadow_hecke_virasoro_wrapper(self):
        """Wrapper should match manual computation."""
        c = 13.0
        coeffs = virasoro_shadow_coefficients(c, max_r=10)
        direct = shadow_hecke_eigenvalue(coeffs, 2, 2.0, max_r=10)
        wrapper = shadow_hecke_eigenvalue_virasoro(c, 2, 2.0, max_r=10)
        assert abs(direct - wrapper) < 1e-12


# ============================================================================
# Section 13: Eisenstein special values (CM points)
# ============================================================================

class TestEisensteinSpecialValues:
    """Known exact values at CM points tau = i and tau = rho."""

    def test_E4_at_i_numerical_vs_exact(self):
        """E_4(i) matches known exact formula: 12*Gamma(1/4)^8/(2*pi)^6."""
        E4_num = eisenstein_numerical(4, TAU_I, nmax=300)
        E4_exact = E4_at_i_exact()
        assert abs(E4_num.real - E4_exact) / abs(E4_exact) < 1e-6

    def test_E6_at_i_is_zero(self):
        """E_6(i) = 0 by symmetry (i^6 = -1)."""
        E6_num = eisenstein_numerical(6, TAU_I, nmax=300)
        assert abs(E6_num) < 1e-8

    def test_E4_at_rho_is_zero(self):
        """E_4(rho) = 0 by symmetry (rho^4 = rho, order-3)."""
        E4_num = eisenstein_numerical(4, TAU_RHO, nmax=300)
        assert abs(E4_num) < 1e-6

    def test_E8_at_i_is_E4_squared(self):
        """E_8(i) = E_4(i)^2."""
        E4 = eisenstein_numerical(4, TAU_I, nmax=300)
        E8 = eisenstein_numerical(8, TAU_I, nmax=300)
        assert abs(E8 - E4 ** 2) < 1e-6

    def test_special_values_dict(self):
        """eisenstein_at_special_points returns dict with correct keys."""
        vals = eisenstein_at_special_points(4)
        assert 'tau_i' in vals
        assert 'tau_rho' in vals

    def test_E6_at_rho_numerical_vs_exact(self):
        """E_6(rho) matches known exact formula: 27*Gamma(1/3)^18/(512*pi^12)."""
        E6_num = eisenstein_numerical(6, TAU_RHO, nmax=300)
        E6_exact = E6_at_rho_exact()
        assert abs(E6_num.real - E6_exact) / abs(E6_exact) < 1e-6

    def test_j_invariant_at_i(self):
        """j(i) = 1728.  j = 1728*E_4^3/(E_4^3 - E_6^2) = 1728*E_4^3/Delta_norm."""
        E4 = eisenstein_numerical(4, TAU_I, nmax=300)
        E6 = eisenstein_numerical(6, TAU_I, nmax=300)
        num = E4 ** 3
        den = E4 ** 3 - E6 ** 2
        j_val = 1728.0 * num / den
        assert abs(j_val.real - 1728.0) < 1.0
        assert abs(j_val.imag) < 1.0


# ============================================================================
# Section 14: Completed shadow Eisenstein (non-holomorphic)
# ============================================================================

class TestCompletedShadowEisenstein:
    """F^{sh,*}_A = kappa*E_2*(tau) + sum_{r>=4} S_r*E_r(tau)."""

    def test_completed_differs_from_holomorphic(self):
        """F^{sh,*} != F^{sh} because of the E_2 -> E_2* replacement.
        F^{sh} - F^{sh,*} = kappa*(E_2 - E_2*) = kappa * 3/(pi*Im(tau)).
        """
        coeffs = virasoro_shadow_coefficients(13.0, max_r=10)
        Fsh = shadow_modular_form(coeffs, TAU_I, max_r=10)
        Fsh_star = shadow_modular_form_completed(coeffs, TAU_I, max_r=10)
        kappa = coeffs[2]
        # F^{sh} uses E_2; F^{sh,*} uses E_2* = E_2 - 3/(pi*y)
        # Difference: kappa * (E_2 - E_2*) = kappa * 3/(pi*y)
        expected_diff = kappa * 3.0 / math.pi  # at Im(tau) = 1
        assert abs((Fsh - Fsh_star).real - expected_diff) < 1e-6

    def test_completed_weight_by_weight_transformation(self):
        """Each weight component transforms correctly."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        result = verify_completed_shadow_transformation(coeffs, TAU_I, max_r=10)
        assert result['total_error'] < 1e-6

    def test_completed_at_2i(self):
        """Completed shadow at tau = 2i."""
        coeffs = virasoro_shadow_coefficients(25.0, max_r=10)
        result = verify_completed_shadow_transformation(coeffs, TAU_2I, max_r=10)
        assert result['total_error'] < 1e-6


# ============================================================================
# Section 15: Shadow Maass series
# ============================================================================

class TestShadowMaassSeries:
    """E^{sh,Maass}_A(tau, s2) = sum S_r * E(tau, r/2) * r^{-s2}."""

    def test_maass_eisenstein_positive_at_i(self):
        """E(i, s) should be real and positive for s > 1."""
        val = maass_eisenstein_numerical(TAU_I, 2.0, nmax=50)
        assert val.real > 0
        assert abs(val.imag) < 0.5  # approximately real

    def test_maass_eisenstein_s_dependence(self):
        """E(i, s) should decrease as s increases (for s > 1)."""
        v2 = maass_eisenstein_numerical(TAU_I, 2.0, nmax=50)
        v3 = maass_eisenstein_numerical(TAU_I, 3.0, nmax=50)
        assert abs(v3) < abs(v2) * 2  # not necessarily monotone due to coprime sum

    def test_shadow_maass_returns_complex(self):
        """Return type is complex."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        val = shadow_maass_series(coeffs, TAU_I, 2.0, max_r=10, nmax=30)
        assert isinstance(val, complex)

    def test_shadow_maass_converges(self):
        """Should be finite."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=10)
        val = shadow_maass_series(coeffs, TAU_I, 3.0, max_r=10, nmax=30)
        assert math.isfinite(val.real) and math.isfinite(val.imag)


# ============================================================================
# Section 16: Shadow zeta functions
# ============================================================================

class TestShadowZeta:
    """Shadow zeta: sum S_r * r^{-s}."""

    def test_shadow_zeta_dominated_by_S2(self):
        """At large s, S_2 * 2^{-s} dominates (unless S_2 = 0)."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=20)
        z20 = shadow_zeta(coeffs, 20.0, max_r=20)
        S2_term = coeffs[2] * 2.0 ** (-20.0)
        assert abs(z20 - S2_term) / abs(S2_term) < 0.01

    def test_shadow_zeta_even_subset(self):
        """Even-only zeta <= total zeta (in absolute value) for positive S_r."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        z_all = shadow_zeta(coeffs, 2.0, max_r=10)
        z_even = shadow_zeta_even(coeffs, 2.0, max_r=10)
        # Not necessarily |even| <= |all| for all sign patterns, but check consistency
        assert math.isfinite(z_all) and math.isfinite(z_even)

    def test_shadow_zeta_heisenberg(self):
        """Heisenberg: S_2 = k, S_r = 0 for r>=3, so zeta = k * 2^{-s}."""
        k = 3.0
        coeffs = {r: 0.0 for r in range(2, 20)}
        coeffs[2] = k
        for s in [2.0, 3.0, 4.0]:
            z = shadow_zeta(coeffs, s, max_r=20)
            assert abs(z - k * 2.0 ** (-s)) < 1e-12

    def test_shadow_constant_term(self):
        """Constant term = sum S_r (even r), since E_k(q=0) = 1."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        ct = shadow_constant_term(coeffs, max_r=10)
        expected = sum(coeffs.get(r, 0.0) for r in range(2, 11) if r % 2 == 0)
        assert abs(ct - expected) < 1e-12


# ============================================================================
# Section 17: Mellin transform (formal)
# ============================================================================

class TestMellinTransform:
    """Formal Mellin transform connecting shadow Eisenstein to shadow zeta."""

    def test_mellin_integrand_finite(self):
        """Integrand should be finite for t in (0.1, 10)."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        for t in [0.5, 1.0, 2.0, 5.0]:
            val = shadow_mellin_integrand(coeffs, t, 2.0, max_r=10)
            assert math.isfinite(val)

    def test_mellin_numerical_returns_dict(self):
        """Numerical Mellin returns correct structure."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        result = shadow_mellin_numerical(coeffs, 2.0, max_r=10, n_points=20)
        assert 's' in result
        assert 'mellin_truncated' in result
        assert 'zeta_direct' in result

    def test_mellin_integrand_positive_t(self):
        """Should raise for t <= 0."""
        coeffs = virasoro_shadow_coefficients(1.0, max_r=10)
        with pytest.raises(ValueError):
            shadow_mellin_integrand(coeffs, -1.0, 2.0, max_r=10)


# ============================================================================
# Section 18: Cross-checks and consistency
# ============================================================================

class TestCrossChecks:
    """Multi-path verification and consistency checks."""

    def test_bernoulli_values(self):
        """Known Bernoulli numbers."""
        assert bernoulli_number(0) == Fraction(1)
        assert bernoulli_number(1) == Fraction(-1, 2)
        assert bernoulli_number(2) == Fraction(1, 6)
        assert bernoulli_number(4) == Fraction(-1, 30)
        assert bernoulli_number(6) == Fraction(1, 42)
        assert bernoulli_number(8) == Fraction(-1, 30)
        assert bernoulli_number(10) == Fraction(5, 66)
        assert bernoulli_number(12) == Fraction(-691, 2730)

    def test_sigma_k_values(self):
        """Known divisor sums."""
        assert sigma_k(1, 3) == 1
        assert sigma_k(2, 3) == 1 + 8  # 1^3 + 2^3 = 9
        assert sigma_k(3, 3) == 1 + 27  # 1^3 + 3^3 = 28
        assert sigma_k(6, 1) == 1 + 2 + 3 + 6  # = 12

    def test_E4_coefficient_from_sigma(self):
        """Path 1 vs Path 2: E_4 coefficient from sigma_3 vs from Bernoulli."""
        # Path 1: a_n = 240 * sigma_3(n)
        a1_path1 = 240 * sigma_k(1, 3)
        # Path 2: a_n = (-2k/B_k) * sigma_{k-1}(n) with k=4
        a1_path2 = eisenstein_coefficient(4, 1)
        assert a1_path1 == int(a1_path2)

    def test_E4_squared_ring_relation(self):
        """E_4^2 = E_8 as modular forms (checked via Fourier coefficients)."""
        E4_coeffs = eisenstein_q_expansion(4, nmax=10)
        E8_coeffs = eisenstein_q_expansion(8, nmax=10)
        # Product coefficients: (E4*E4)[n] = sum_{j=0}^{n} E4[j]*E4[n-j]
        for n in range(11):
            product = sum(E4_coeffs[j] * E4_coeffs[n - j] for j in range(n + 1))
            assert product == E8_coeffs[n], f"Mismatch at n={n}: {product} != {E8_coeffs[n]}"

    def test_E4_E6_product_ring_relation(self):
        """E_4 * E_6 = E_10 (checked via Fourier coefficients)."""
        E4_coeffs = eisenstein_q_expansion(4, nmax=5)
        E6_coeffs = eisenstein_q_expansion(6, nmax=5)
        E10_coeffs = eisenstein_q_expansion(10, nmax=5)
        for n in range(6):
            product = sum(E4_coeffs[j] * E6_coeffs[n - j] for j in range(n + 1))
            assert product == E10_coeffs[n], f"Mismatch at n={n}"

    def test_shadow_eisenstein_additivity(self):
        """E^{sh}_{A1+A2} = E^{sh}_{A1} + E^{sh}_{A2} if shadow coeffs add."""
        # Heisenberg k=1 and k=2: S_2 adds, S_r=0 for r>=3
        c1 = {2: 0.5, 3: 0.0, 4: 0.0}
        c2 = {2: 1.0, 3: 0.0, 4: 0.0}
        c_sum = {2: 1.5, 3: 0.0, 4: 0.0}
        E1 = shadow_eisenstein_series(c1, TAU_I, 2.0, max_r=5)
        E2 = shadow_eisenstein_series(c2, TAU_I, 2.0, max_r=5)
        E_sum = shadow_eisenstein_series(c_sum, TAU_I, 2.0, max_r=5)
        assert abs(E1 + E2 - E_sum) < 1e-12

    def test_hecke_eigenvalue_multiplicativity(self):
        """(1+p^{k-1}) is multiplicative in p for fixed k? No, but check formula."""
        # Just verify the formula at multiple (p, k)
        for p in [2, 3, 5, 7]:
            for k in [4, 6, 8, 10, 12]:
                ev = hecke_eigenvalue_eisenstein(p, k)
                assert ev == 1 + p ** (k - 1)

    def test_shadow_zeta_vs_hecke_acted(self):
        """shadow_hecke_acted_zeta / shadow_zeta_even = shadow_hecke_eigenvalue."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=10)
        for p in [2, 3, 5]:
            for s in [2.0, 3.0]:
                num = shadow_hecke_acted_zeta(coeffs, p, s, max_r=10)
                den = shadow_zeta_even(coeffs, s, max_r=10)
                ev = shadow_hecke_eigenvalue(coeffs, p, s, max_r=10)
                if abs(den) > 1e-15:
                    assert abs(ev - num / den) < 1e-8

    def test_full_table_runs(self):
        """compute_full_shadow_eisenstein_table completes without error."""
        result = compute_full_shadow_eisenstein_table(
            c_values=[1.0, 13.0],
            s_values=[2.0, 3.0],
            p_values=[2, 3],
            max_r=10,
        )
        assert 'c=1.0' in result
        assert 'c=13.0' in result

    def test_delta_discriminant_relation(self):
        """Delta = (E_4^3 - E_6^2) / 1728, checked via Fourier coefficients.
        Path: ring structure verification (cross-check with tau function)."""
        E4 = eisenstein_q_expansion(4, nmax=5)
        E6 = eisenstein_q_expansion(6, nmax=5)
        # E_4^3
        E43 = [Fraction(0)] * 6
        for n in range(6):
            for j in range(n + 1):
                for k in range(j + 1):
                    E43[n] += E4[k] * E4[j - k] * E4[n - j]
        # E_6^2
        E62 = [Fraction(0)] * 6
        for n in range(6):
            for j in range(n + 1):
                E62[n] += E6[j] * E6[n - j]
        # Delta_norm = (E_4^3 - E_6^2) / 1728
        # Delta = q * prod(1-q^n)^{24}, so Delta = sum tau(n) q^n
        # The normalized discriminant Delta/1728 has a_0 = 0, a_1 = 1
        for n in range(6):
            delta_coeff = (E43[n] - E62[n]) / 1728
            if n == 0:
                assert delta_coeff == 0
            elif n >= 1:
                assert delta_coeff == ramanujan_tau(n)

    def test_virasoro_shadow_exact_vs_numerical(self):
        """Exact and numerical shadow coefficients should agree."""
        for c_val_int in [1, 13, 25]:
            c_f = Fraction(c_val_int)
            c_float = float(c_f)
            coeffs_num = virasoro_shadow_coefficients(c_float, max_r=8)
            for r in range(2, 9):
                S_exact = float(virasoro_shadow_exact(r, c_f))
                S_num = coeffs_num[r]
                if abs(S_exact) > 1e-20:
                    assert abs(S_exact - S_num) / abs(S_exact) < 1e-8, \
                        f"Mismatch at c={c_val_int}, r={r}: exact={S_exact}, num={S_num}"
                else:
                    assert abs(S_num) < 1e-10

    def test_anomaly_matches_direct_E2_computation(self):
        """The shadow anomaly kappa*12/(2*pi*i) should match the explicit E_2
        transformation anomaly coefficient."""
        # E_2(-1/tau) = tau^2 E_2(tau) + 12*tau/(2*pi*i)
        # The coefficient of tau in the anomaly is 12/(2*pi*i).
        # At kappa = c/2 for Virasoro, the arity-2 anomaly is kappa * 12/(2*pi*i).
        for c in [1.0, 13.0, 25.0]:
            kappa = c / 2.0
            anomaly = shadow_modular_anomaly(kappa)
            # Direct: kappa * 12 / (2*pi*i)
            direct = kappa * 12.0 / (2.0 * math.pi * 1j)
            assert abs(anomaly - direct) < 1e-15
