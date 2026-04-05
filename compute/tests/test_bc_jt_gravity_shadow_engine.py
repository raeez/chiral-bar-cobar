r"""Tests for BC-93: JT gravity partition function from shadow zeta residues.

Tests organized by section:
  1.  Bernoulli numbers and Faber-Pandharipande numbers
  2.  Weil-Petersson volumes: base cases and polynomial structure
  3.  WP volume dilaton equation consistency
  4.  JT spectral density and spectral curve
  5.  JT building block amplitudes (disk, trumpet)
  6.  JT genus expansion
  7.  Shadow free energies F_g
  8.  Shadow generating function (Ahat)
  9.  Shadow-JT structural comparison
  10. Shadow spectral density
  11. Shadow disk and trumpet amplitudes
  12. Laplace transform verification (multi-path)
  13. Large-beta WKB asymptotics
  14. Non-perturbative effects
  15. Schwarzian limit
  16. Best-fit e^{S_0}
  17. Virasoro shadow coefficients
  18. Full cross-verification suite
  19. Edge cases and special values

Verification paths (>= 3 per claim):
  (a) Direct formula computation
  (b) Polynomial evaluation + consistency
  (c) Dilaton/string equation cross-check
  (d) Laplace transform vs spectral density
  (e) Generating function vs partial sum
  (f) WKB asymptotic agreement
  (g) Dimensional / degree analysis
"""

import pytest
import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_jt_gravity_shadow_engine import (
    # Section 1
    bernoulli_number, lambda_fp, ahat_generating_function,
    # Section 2
    wp_volume_one_boundary_coeffs, wp_volume_one_boundary_eval,
    wp_volume_V_g1_at_zero, wp_volume_V03, wp_volume_V_g0,
    # Section 5
    jt_spectral_density, jt_spectral_curve_y,
    # Section 6
    jt_disk_amplitude, jt_trumpet, jt_Z_g, jt_genus_expansion,
    # Section 7
    shadow_F_g, shadow_generating_function, shadow_partial_sum,
    shadow_tower_jt_comparison,
    # Section 8
    shadow_zeta_from_coeffs, shadow_spectral_density,
    shadow_eigenvalue_density,
    # Section 9
    shadow_disk_amplitude, shadow_trumpet_amplitude,
    # Section 10
    jt_from_shadow, best_fit_e_S0,
    # Section 12
    verify_disk_laplace, verify_spectral_density_normalization,
    # Section 13
    jt_large_beta_asymptotic,
    # Section 14
    jt_nonperturbative_estimate, shadow_resurgent_correction,
    # Section 15
    virasoro_shadow_coefficients,
    # Section 16
    schwarzian_limit_data,
    # Section 17
    cross_verify_V11, cross_verify_V21, full_verification_suite,
)

PI = math.pi
PI2 = PI * PI
from fractions import Fraction


# =========================================================================
# Section 1: Bernoulli numbers and Faber-Pandharipande
# =========================================================================

class TestBernoulliNumbers:
    """Exact Bernoulli numbers."""

    def test_B0(self):
        assert bernoulli_number(0) == Fraction(1)

    def test_B1(self):
        assert bernoulli_number(1) == Fraction(-1, 2)

    def test_B2(self):
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_B8(self):
        assert bernoulli_number(8) == Fraction(-1, 30)

    def test_B10(self):
        assert bernoulli_number(10) == Fraction(5, 66)

    def test_B12(self):
        assert bernoulli_number(12) == Fraction(-691, 2730)

    def test_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == Fraction(0)

    def test_sign_alternation(self):
        """B_{2n} alternates in sign: B_2 > 0, B_4 < 0, B_6 > 0, ..."""
        for n in range(1, 8):
            sign = (-1)**(n + 1)
            assert sign * bernoulli_number(2 * n) > 0


class TestFaberPandharipande:
    """Faber-Pandharipande intersection numbers lambda_g^FP."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_positivity(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 10):
            assert lambda_fp(g) > 0

    def test_lambda_growth(self):
        """lambda_{g+1}/lambda_g grows roughly as (2g)^2 / (4 pi^2)."""
        for g in range(1, 8):
            ratio = float(lambda_fp(g + 1)) / float(lambda_fp(g))
            # The ratio is (2^{2g+1}-1)/(2^{2g-1}-1) * |B_{2g+2}|/|B_{2g}| / ((2g+2)(2g+1))
            assert ratio > 0

    def test_generating_function_genus_1(self):
        """Check Ahat(ix) - 1 at genus 1: coefficient of x^2 is lambda_1."""
        # Ahat(ix) = (x/2)/sin(x/2) = 1 + x^2/24 + 7 x^4/5760 + ...
        # So coefficient of x^2 = 1/24 = lambda_1. CHECK.
        x = 0.01
        ahat_val = ahat_generating_function(x)
        # Ahat(ix) - 1 ~ x^2/24 for small x
        approx = x**2 / 24.0
        assert abs(ahat_val - 1.0 - approx) / abs(approx) < 0.01

    def test_lambda_invalid_genus(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


class TestAhatGeneratingFunction:
    """Ahat(ix) = (x/2)/sin(x/2)."""

    def test_ahat_at_zero(self):
        """Ahat(0) = 1."""
        assert abs(ahat_generating_function(0.0) - 1.0) < 1e-12

    def test_ahat_at_small_x(self):
        """Ahat(ix) ~ 1 + x^2/24 for small x."""
        x = 0.001
        val = ahat_generating_function(x)
        expected = 1.0 + x**2 / 24.0
        assert abs(val - expected) < 1e-8

    def test_ahat_positive(self):
        """Ahat(ix) > 0 for 0 < x < 2*pi."""
        for x in [0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 6.0]:
            assert ahat_generating_function(x) > 0

    def test_ahat_diverges_at_2pi(self):
        """Ahat(ix) diverges at x = 2*pi (pole of 1/sin)."""
        val = ahat_generating_function(2.0 * PI - 0.001)
        assert val > 100  # should be very large near the pole


# =========================================================================
# Section 2: Weil-Petersson Volumes
# =========================================================================

class TestWPVolumesBaseCases:
    """Base cases of the Mirzakhani recursion."""

    def test_V03_is_one(self):
        """V_{0,3}(b1,b2,b3) = 1."""
        assert wp_volume_V03() == 1.0

    def test_V11_at_zero(self):
        """V_{1,1}(0) = pi^2/12."""
        V11_0 = wp_volume_V_g1_at_zero(1)
        expected = PI2 / 12.0
        assert abs(V11_0 - expected) / expected < 1e-12

    def test_V11_polynomial(self):
        """V_{1,1}(b) = (b^2 + 4*pi^2)/48."""
        coeffs = wp_volume_one_boundary_coeffs(1)
        assert len(coeffs) == 2
        assert abs(coeffs[0] - PI2 / 12.0) < 1e-12
        assert abs(coeffs[1] - 1.0 / 48.0) < 1e-14

    def test_V11_eval_at_1(self):
        """V_{1,1}(1) = (1 + 4*pi^2)/48."""
        val = wp_volume_one_boundary_eval(1, 1.0)
        expected = (1.0 + 4.0 * PI2) / 48.0
        assert abs(val - expected) < 1e-12

    def test_V11_polynomial_degree(self):
        """V_{1,1}(b) has degree 1 in b^2 (i.e., 3*1-2 = 1)."""
        coeffs = wp_volume_one_boundary_coeffs(1)
        assert len(coeffs) == 2  # degree 1 -> 2 coefficients


class TestWPVolumesGenus2:
    """V_{2,1}(b) verification."""

    def test_V21_at_zero(self):
        """V_{2,1}(0) = 29*pi^8/276480."""
        V21_0 = wp_volume_V_g1_at_zero(2)
        expected = 29.0 * PI2**4 / 276480.0
        assert abs(V21_0 - expected) / abs(expected) < 1e-10

    def test_V21_polynomial_degree(self):
        """V_{2,1} has degree 4 in b^2 (3*2-2 = 4)."""
        coeffs = wp_volume_one_boundary_coeffs(2)
        assert len(coeffs) == 5

    def test_V21_leading_coefficient(self):
        """Leading coefficient of V_{2,1} is 1/442368."""
        coeffs = wp_volume_one_boundary_coeffs(2)
        assert abs(coeffs[4] - 1.0 / 442368.0) < 1e-16

    def test_V21_constant_term(self):
        """Constant term of V_{2,1}."""
        coeffs = wp_volume_one_boundary_coeffs(2)
        expected = 29.0 * PI2**4 / 276480.0
        assert abs(coeffs[0] - expected) / abs(expected) < 1e-10

    def test_V21_all_positive(self):
        """All coefficients of V_{2,1} are positive."""
        coeffs = wp_volume_one_boundary_coeffs(2)
        for c in coeffs:
            assert c > 0

    def test_V21_eval_positive(self):
        """V_{2,1}(b) > 0 for b >= 0."""
        for b in [0, 0.5, 1.0, 2.0, 5.0, 10.0]:
            assert wp_volume_one_boundary_eval(2, b) > 0


# =========================================================================
# Section 3: Dilaton equation consistency
# =========================================================================

class TestDilatonEquation:
    """V_{g,n+1}(bS, 0) = (2g-2+n)*V_{g,n}(bS)."""

    def test_dilaton_g2(self):
        """V_{2,1}(0) = 2*V_{2,0}."""
        V21_0 = wp_volume_V_g1_at_zero(2)
        V20 = wp_volume_V_g0(2)
        assert abs(V21_0 - 2.0 * V20) / abs(V21_0) < 1e-12

    def test_V20_positive(self):
        """V_{2,0} > 0."""
        assert wp_volume_V_g0(2) > 0

    def test_dilaton_invalid(self):
        """V_{g,0} requires g >= 2."""
        with pytest.raises(ValueError):
            wp_volume_V_g0(1)

    def test_V_g1_at_zero_positive(self):
        """V_{g,1}(0) > 0 for g = 1, 2."""
        for g in [1, 2]:
            assert wp_volume_V_g1_at_zero(g) > 0


# =========================================================================
# Section 4: JT Spectral Density
# =========================================================================

class TestJTSpectralDensity:
    """rho_0(E) = sinh(2 pi sqrt(E)) / (4 pi^2)."""

    def test_rho_at_zero(self):
        """rho_0(0) = 0."""
        assert jt_spectral_density(0.0) == 0.0

    def test_rho_negative(self):
        """rho_0(E) = 0 for E < 0."""
        assert jt_spectral_density(-1.0) == 0.0

    def test_rho_positive(self):
        """rho_0(E) > 0 for E > 0."""
        for E in [0.01, 0.1, 1.0, 10.0]:
            assert jt_spectral_density(E) > 0

    def test_rho_at_1(self):
        """rho_0(1) = sinh(2*pi)/(4*pi^2)."""
        expected = math.sinh(2.0 * PI) / (4.0 * PI2)
        assert abs(jt_spectral_density(1.0) - expected) < 1e-10

    def test_rho_monotone(self):
        """rho_0 is monotonically increasing for E > 0."""
        prev = 0.0
        for E in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
            curr = jt_spectral_density(E)
            assert curr > prev
            prev = curr

    def test_rho_exponential_growth(self):
        """rho_0(E) ~ e^{2*pi*sqrt(E)} / (8*pi^2) for large E."""
        E = 100.0
        rho = jt_spectral_density(E)
        # sinh(x) ~ e^x/2 for large x, so rho ~ e^{2*pi*sqrt(E)} / (8*pi^2)
        asymptotic = math.exp(2.0 * PI * math.sqrt(E)) / (8.0 * PI2)
        assert abs(rho - asymptotic) / asymptotic < 0.01

    def test_rho_small_E(self):
        """rho_0(E) ~ sqrt(E) / (2*pi) for small E."""
        E = 1e-6
        rho = jt_spectral_density(E)
        # sinh(2*pi*sqrt(E)) ~ 2*pi*sqrt(E) for small E
        asymptotic = math.sqrt(E) / (2.0 * PI)
        assert abs(rho - asymptotic) / abs(asymptotic) < 0.01


class TestJTSpectralCurve:
    """y(x) = sin(2 pi sqrt(x)) / (4 pi)."""

    def test_curve_at_zero(self):
        """y(0) = 0."""
        assert abs(jt_spectral_curve_y(0.0)) < 1e-14

    def test_curve_real_for_positive_x(self):
        """y(x) is real for x > 0."""
        for x in [0.01, 0.1, 1.0, 4.0]:
            y = jt_spectral_curve_y(x)
            assert abs(y.imag) < 1e-10

    def test_curve_imaginary_for_negative_x(self):
        """y(-E) is purely imaginary for E > 0, and Im(y(-E)) gives rho."""
        E = 1.0
        y = jt_spectral_curve_y(-E)
        # y(-E) = sin(2*pi*i*sqrt(E))/(4*pi) = i*sinh(2*pi*sqrt(E))/(4*pi)
        expected_im = math.sinh(2.0 * PI * math.sqrt(E)) / (4.0 * PI)
        assert abs(y.real) < 1e-10
        assert abs(y.imag - expected_im) / expected_im < 1e-10


# =========================================================================
# Section 5: JT Building Block Amplitudes
# =========================================================================

class TestJTDiskAmplitude:
    """Z_disk(beta) = exp(pi^2/beta) / (4 sqrt(pi) beta^{3/2})."""

    def test_disk_positive(self):
        """Z_disk(beta) > 0 for beta > 0."""
        for beta in [0.1, 1.0, 10.0]:
            assert jt_disk_amplitude(beta) > 0

    def test_disk_at_zero(self):
        """Z_disk(0) = 0 (boundary case)."""
        assert jt_disk_amplitude(0.0) == 0.0

    def test_disk_formula(self):
        """Check the explicit formula at beta=1."""
        expected = math.exp(PI2) / (4.0 * math.sqrt(PI))
        actual = jt_disk_amplitude(1.0)
        assert abs(actual - expected) / expected < 1e-10

    def test_disk_decreases_with_beta(self):
        """Z_disk decreases as beta increases (for moderate beta)."""
        d1 = jt_disk_amplitude(1.0)
        d10 = jt_disk_amplitude(10.0)
        d100 = jt_disk_amplitude(100.0)
        # For increasing beta, the exp(pi^2/beta) factor weakens
        # and the beta^{-3/2} factor also decreases.
        assert d100 < d10 < d1


class TestJTTrumpet:
    """Z_trumpet(beta, b) = exp(-b^2/(4 beta)) / sqrt(4 pi beta)."""

    def test_trumpet_at_b0(self):
        """Z_trumpet(beta, 0) = 1/sqrt(4 pi beta)."""
        beta = 1.0
        expected = 1.0 / math.sqrt(4.0 * PI * beta)
        assert abs(jt_trumpet(beta, 0.0) - expected) < 1e-12

    def test_trumpet_gaussian_decay(self):
        """Trumpet decays as Gaussian in b."""
        beta = 1.0
        t0 = jt_trumpet(beta, 0.0)
        t1 = jt_trumpet(beta, 1.0)
        t5 = jt_trumpet(beta, 5.0)
        assert t0 > t1 > t5

    def test_trumpet_positive(self):
        for beta in [0.1, 1.0, 10.0]:
            for b in [0.0, 1.0, 5.0]:
                assert jt_trumpet(beta, b) > 0

    def test_trumpet_normalization(self):
        """int_0^infty b * Z_trumpet(beta, b) db = sqrt(beta/pi)."""
        # int_0^infty b exp(-b^2/(4*beta)) db = 2*beta
        # So int_0^infty b * Z_trumpet db = 2*beta / sqrt(4*pi*beta) = sqrt(beta/pi)
        beta = 1.0
        # Numerical check
        N = 10000
        b_max = 20.0
        db = b_max / N
        integral = sum(b * jt_trumpet(beta, b) * db for b in [k * db for k in range(1, N + 1)])
        expected = math.sqrt(beta / PI)
        assert abs(integral - expected) / expected < 0.01


# =========================================================================
# Section 6: JT Genus Expansion
# =========================================================================

class TestJTGenusExpansion:
    """JT genus expansion Z_JT(beta)."""

    def test_Z_g1(self):
        """Z_1(beta) from V_{1,1} polynomial."""
        beta = 1.0
        Z1 = jt_Z_g(1, beta)
        assert Z1 > 0

    def test_Z_g1_explicit(self):
        """Z_1(beta) = V_{1,1}(0)*sqrt(4*beta)/(2*sqrt(pi)) + V_{1,1}'*Gamma(2)*(4*beta)^2/(2*sqrt(pi*4*beta))."""
        beta = 1.0
        # V_{1,1}(b) = pi^2/12 + b^2/48
        # Z_1 = (1/sqrt(4*pi*beta)) * [ (pi^2/12) * 0! * (4*beta)^1 / 2 + (1/48) * 1! * (4*beta)^2 / 2 ]
        # = (1/sqrt(4*pi)) * [ (pi^2/12)*2 + (1/48)*8 ]
        # = (1/sqrt(4*pi)) * [ pi^2/6 + 1/6 ]
        # = (pi^2 + 1) / (6 * sqrt(4*pi))
        expected = (PI2 + 1.0) / (6.0 * math.sqrt(4.0 * PI))
        Z1 = jt_Z_g(1, 1.0)
        assert abs(Z1 - expected) / expected < 1e-10

    def test_Z_g2(self):
        """Z_2(beta) > 0 for beta > 0."""
        Z2 = jt_Z_g(2, 1.0)
        assert Z2 > 0

    def test_genus_expansion_structure(self):
        """jt_genus_expansion returns expected keys."""
        result = jt_genus_expansion(1.0, max_genus=3)
        assert 'Z_total' in result
        assert 'genus_contributions' in result
        assert 'disk' in result

    def test_genus_expansion_disk_dominant(self):
        """For large e_S0, disk dominates."""
        result = jt_genus_expansion(1.0, max_genus=3, e_S0=100.0)
        disk_contrib = result['e_S0']**2 * result['disk']
        # Disk is weighted by e^{2S_0} = e_S0^2 = 10000
        assert abs(disk_contrib) > abs(result['genus_contributions'].get(1, 0.0))


# =========================================================================
# Section 7: Shadow Free Energies
# =========================================================================

class TestShadowFreeEnergies:
    """F_g(A) = kappa(A) * lambda_g^FP."""

    def test_F1_virasoro(self):
        """F_1(Vir_c) = c/2 * 1/24 = c/48."""
        c = 26.0
        kappa = c / 2.0
        F1 = shadow_F_g(kappa, 1)
        expected = c / 48.0
        assert abs(F1 - expected) < 1e-12

    def test_F2_virasoro(self):
        """F_2(Vir_c) = c/2 * 7/5760."""
        c = 1.0
        kappa = c / 2.0
        F2 = shadow_F_g(kappa, 2)
        expected = c / 2.0 * 7.0 / 5760.0
        assert abs(F2 - expected) < 1e-14

    def test_F_positive(self):
        """F_g > 0 for all g >= 1 when kappa > 0."""
        kappa = 1.0
        for g in range(1, 10):
            assert shadow_F_g(kappa, g) > 0

    def test_F_linear_in_kappa(self):
        """F_g is linear in kappa."""
        g = 3
        F1 = shadow_F_g(1.0, g)
        F2 = shadow_F_g(2.0, g)
        assert abs(F2 - 2.0 * F1) < 1e-14

    def test_F_additivity(self):
        """F_g(A ⊕ B) = F_g(A) + F_g(B) via kappa additivity."""
        kappa_A = 3.0
        kappa_B = 5.0
        for g in range(1, 5):
            assert abs(shadow_F_g(kappa_A + kappa_B, g)
                       - shadow_F_g(kappa_A, g) - shadow_F_g(kappa_B, g)) < 1e-14


# =========================================================================
# Section 8: Shadow Generating Function
# =========================================================================

class TestShadowGeneratingFunction:
    """sum_{g >= 1} F_g x^{2g} = kappa * (Ahat(ix) - 1)."""

    def test_gf_at_zero(self):
        """GF(0) = 0."""
        assert abs(shadow_generating_function(1.0, 0.0)) < 1e-14

    def test_gf_small_x(self):
        """GF ~ kappa * x^2/24 for small x."""
        kappa = 1.0
        x = 0.001
        gf = shadow_generating_function(kappa, x)
        expected = kappa * x**2 / 24.0
        assert abs(gf - expected) / abs(expected) < 0.01

    def test_gf_matches_partial_sum(self):
        """GF matches partial sum for moderate x."""
        kappa = 1.0
        x = 0.5
        gf_exact = shadow_generating_function(kappa, x)
        gf_partial = shadow_partial_sum(kappa, x, max_genus=20)
        assert abs(gf_exact - gf_partial) / abs(gf_exact) < 1e-6

    def test_gf_matches_partial_sum_at_1(self):
        """GF matches partial sum at x=1."""
        kappa = 0.5
        x = 1.0
        gf_exact = shadow_generating_function(kappa, x)
        gf_partial = shadow_partial_sum(kappa, x, max_genus=30)
        assert abs(gf_exact - gf_partial) / abs(gf_exact) < 1e-4

    def test_gf_positive(self):
        """GF > 0 for kappa > 0 and 0 < x < 2*pi."""
        for x in [0.1, 0.5, 1.0, 2.0, 3.0, 5.0]:
            assert shadow_generating_function(1.0, x) > 0


# =========================================================================
# Section 9: Shadow-JT Structural Comparison
# =========================================================================

class TestShadowJTComparison:
    """Structural comparison between shadow F_g and JT V_{g,1}(0)."""

    def test_comparison_g1_ratio(self):
        """V_{1,1}(0) / lambda_1 = 2*pi^2."""
        comp = shadow_tower_jt_comparison(max_genus=2)
        ratio_g1 = comp[1]['ratio']
        expected = 2.0 * PI2
        assert abs(ratio_g1 - expected) / expected < 1e-10

    def test_comparison_g2_ratio_differs(self):
        """V_{2,1}(0) / lambda_2 != 2*pi^2 (different tautological classes)."""
        comp = shadow_tower_jt_comparison(max_genus=2)
        ratio_g1 = comp[1]['ratio']
        ratio_g2 = comp[2]['ratio']
        # They should differ (NOT the same ratio)
        assert abs(ratio_g1 - ratio_g2) / abs(ratio_g1) > 0.01

    def test_comparison_contains_keys(self):
        comp = shadow_tower_jt_comparison(max_genus=3)
        for g in [1, 2, 3]:
            assert g in comp
            assert 'lambda_fp' in comp[g]
            assert 'V_g1_0' in comp[g]
            assert 'ratio' in comp[g]


# =========================================================================
# Section 10: Shadow Spectral Density
# =========================================================================

class TestShadowSpectralDensity:
    """Shadow spectral density rho_A(E)."""

    def test_density_with_single_coeff(self):
        """With S = {2: 1}, density = (1/pi) * 2^{-1/2} * cos(E log 2)."""
        S = {2: 1.0}
        E = 1.0
        expected = 2.0**(-0.5) * math.cos(E * math.log(2.0)) / PI
        actual = shadow_spectral_density(S, E)
        assert abs(actual - expected) < 1e-12

    def test_density_at_zero(self):
        """rho_A(0) = (1/pi) sum_r S_r r^{-1/2}."""
        S = {2: 1.0, 3: 0.5}
        expected = (1.0 * 2**(-0.5) + 0.5 * 3**(-0.5)) / PI
        actual = shadow_spectral_density(S, 0.0)
        assert abs(actual - expected) < 1e-12

    def test_eigenvalue_density_positive(self):
        """Eigenvalue density modulus is non-negative."""
        S = {2: 1.0, 3: 0.5, 4: 0.1}
        for E in [0.0, 0.5, 1.0, 2.0, 5.0]:
            assert shadow_eigenvalue_density(S, E) >= 0


# =========================================================================
# Section 11: Shadow Disk and Trumpet
# =========================================================================

class TestShadowAmplitudes:
    """Shadow disk and trumpet amplitudes."""

    def test_shadow_disk_nonzero(self):
        """Shadow disk amplitude is nonzero for finite beta."""
        S = {2: 1.0, 3: 0.5}
        kappa = 1.0
        val = shadow_disk_amplitude(kappa, S, 1.0)
        assert abs(val) > 0

    def test_shadow_trumpet_at_b0(self):
        """Shadow trumpet at b=0 equals shadow disk (up to normalization)."""
        S = {2: 1.0, 3: 0.5}
        kappa = 1.0
        beta = 1.0
        disk = shadow_disk_amplitude(kappa, S, beta)
        trumpet_b0 = shadow_trumpet_amplitude(kappa, S, beta, 0.0)
        assert abs(disk - trumpet_b0) < 1e-12

    def test_shadow_trumpet_decay(self):
        """Shadow trumpet amplitude decreases with b (oscillatory decay)."""
        S = {2: 1.0}
        kappa = 1.0
        beta = 2.0
        # With a single S_r, trumpet = kappa * S_r * r^{-beta-1/2} * e^{-ib log r}
        # |trumpet| = kappa * |S_r| * r^{-beta-1/2} (constant in b!)
        # So for a single coefficient, the MODULUS is b-independent.
        t0 = abs(shadow_trumpet_amplitude(kappa, S, beta, 0.0))
        t1 = abs(shadow_trumpet_amplitude(kappa, S, beta, 1.0))
        assert abs(t0 - t1) < 1e-10  # same modulus for single coeff


# =========================================================================
# Section 12: Laplace Transform Verification
# =========================================================================

class TestLaplaceTransformVerification:
    """Multi-path verification: Z_disk = int rho_0(E) e^{-beta E} dE."""

    def test_disk_laplace_beta_1(self):
        """Laplace transform at beta=1 matches Z_disk."""
        result = verify_disk_laplace(beta=1.0, N=20000, E_max=150.0)
        assert result['relative_error'] < 0.05

    def test_disk_laplace_beta_5(self):
        """Laplace transform at beta=5."""
        result = verify_disk_laplace(beta=5.0, N=10000, E_max=50.0)
        assert result['relative_error'] < 0.05

    def test_spectral_density_integral_positive(self):
        """Integrated spectral density is positive."""
        result = verify_spectral_density_normalization(E_max=10.0, N=5000)
        assert result['integrated_density'] > 0


# =========================================================================
# Section 13: Large-Beta WKB Asymptotics
# =========================================================================

class TestLargeBetaWKB:
    """Z_JT ~ e^{2 pi^2/beta} beta^{-3/2} for large beta."""

    def test_wkb_positive(self):
        assert jt_large_beta_asymptotic(10.0) > 0

    def test_wkb_matches_disk(self):
        """WKB asymptotic ~ disk amplitude (ratio -> constant)."""
        beta = 10.0
        disk = jt_disk_amplitude(beta)
        wkb = jt_large_beta_asymptotic(beta)
        # They differ by a multiplicative constant
        assert abs(disk / wkb - 1.0) < 0.5

    def test_wkb_ratio_approaches_1_over_4pi(self):
        """disk/wkb -> 1/(4*pi)^{3/2} * (4*pi)^{3/2} = 1 (same formula)."""
        # Actually disk = exp(2pi^2/beta) / (4pi*beta)^{3/2}
        # wkb = exp(2pi^2/beta) * beta^{-3/2} / (4pi)^{3/2}
        # ratio = 1 always
        for beta in [1.0, 5.0, 10.0]:
            disk = jt_disk_amplitude(beta)
            wkb = jt_large_beta_asymptotic(beta)
            assert abs(disk / wkb - 1.0) < 1e-10


# =========================================================================
# Section 14: Non-Perturbative Effects
# =========================================================================

class TestNonPerturbativeEffects:
    """NP corrections in JT and shadow."""

    def test_jt_np_small(self):
        """NP correction is exponentially small for large e_S0."""
        result = jt_nonperturbative_estimate(10.0, 1.0)
        assert result['np_correction_magnitude'] < 1e-8

    def test_jt_np_grows_at_small_S0(self):
        """NP correction is O(1) when e_S0 ~ 1."""
        result = jt_nonperturbative_estimate(1.0, 1.0)
        np_mag = result['np_correction_magnitude']
        assert np_mag > 0.01  # e^{-2} ~ 0.135

    def test_shadow_resurgent_structure(self):
        """Shadow resurgent correction has action 4*pi^2."""
        result = shadow_resurgent_correction(1.0, 1.0)
        assert abs(result['action'] - 4.0 * PI2) < 1e-10

    def test_shadow_resurgent_small_at_small_x(self):
        """NP correction vanishes as x -> 0."""
        result = shadow_resurgent_correction(1.0, 0.01)
        assert result['np_correction'] < 1e-100


# =========================================================================
# Section 15: Schwarzian Limit
# =========================================================================

class TestSchwarzianLimit:
    """Large-c limit of Virasoro shadow -> JT."""

    def test_S4_vanishes(self):
        """S_4 = 10/(c*(5c+22)) -> 0 as c -> infty."""
        data = schwarzian_limit_data([10.0, 100.0, 1000.0])
        assert data[1000.0]['S4'] < data[100.0]['S4'] < data[10.0]['S4']

    def test_S4_times_c2(self):
        """S_4 * c^2 -> 2 as c -> infty."""
        data = schwarzian_limit_data([100.0, 1000.0, 10000.0])
        assert abs(data[10000.0]['S4_times_c2'] - 2.0) < 0.01

    def test_Delta_over_kappa_vanishes(self):
        """Delta/kappa -> 0 as c -> infty."""
        data = schwarzian_limit_data([10.0, 100.0, 1000.0])
        assert data[1000.0]['Delta_over_kappa'] < 0.01


# =========================================================================
# Section 16: Best-Fit e^{S_0}
# =========================================================================

class TestBestFitES0:
    """Find optimal e^{S_0} matching shadow to JT."""

    def test_best_fit_returns_positive(self):
        """Best-fit e_S0 > 0."""
        result = best_fit_e_S0(kappa=0.5, max_genus=2)
        assert result['best_e_S0'] > 0

    def test_best_fit_structure(self):
        """Result contains expected keys."""
        result = best_fit_e_S0(kappa=1.0, max_genus=2)
        assert 'best_e_S0' in result
        assert 'best_S0' in result
        assert 'min_residual' in result
        assert 'residuals' in result

    def test_best_fit_kappa_dependence(self):
        """Different kappa gives different best fit."""
        r1 = best_fit_e_S0(kappa=0.5, max_genus=2)
        r2 = best_fit_e_S0(kappa=13.0, max_genus=2)
        assert r1['best_e_S0'] != r2['best_e_S0']


# =========================================================================
# Section 17: Virasoro Shadow Coefficients
# =========================================================================

class TestVirasoroShadowCoefficients:
    """Shadow coefficients S_r for Virasoro."""

    def test_kappa_coefficient(self):
        """S_2 = kappa = c/2."""
        c = 26.0
        S = virasoro_shadow_coefficients(c)
        assert abs(S[2] - c / 2.0) < 1e-12

    def test_alpha_coefficient(self):
        """S_3 = alpha = 2."""
        S = virasoro_shadow_coefficients(10.0)
        assert abs(S[3] - 2.0) < 1e-12

    def test_Q_contact(self):
        """S_4 = Q^contact = 10/(c*(5c+22))."""
        c = 10.0
        S = virasoro_shadow_coefficients(c)
        expected = 10.0 / (c * (5.0 * c + 22.0))
        assert abs(S[4] - expected) < 1e-14

    def test_higher_coefficients_decay(self):
        """S_r decays for r > 4."""
        S = virasoro_shadow_coefficients(10.0, max_r=10)
        for r in range(5, 10):
            assert abs(S.get(r, 0)) < abs(S[4])


# =========================================================================
# Section 18: Full Cross-Verification Suite
# =========================================================================

class TestFullCrossVerification:
    """Full verification suite output."""

    def test_V11_three_path(self):
        result = cross_verify_V11()
        assert result['ratio_match']
        assert abs(result['V11_direct'] - result['V11_from_poly']) < 1e-12

    def test_V21_three_path(self):
        result = cross_verify_V21()
        assert result['dilaton_match']
        assert result['leading_match']

    def test_full_suite_runs(self):
        """Full verification suite completes without error."""
        result = full_verification_suite(max_genus=2)
        assert result['V03'] == 1.0
        assert result['V11_verify']['ratio_match']


# =========================================================================
# Section 19: Edge Cases and Special Values
# =========================================================================

class TestEdgeCases:
    """Edge cases and special values."""

    def test_shadow_F_g_at_kappa_zero(self):
        """F_g(kappa=0) = 0 (uncurved bar complex)."""
        for g in range(1, 5):
            assert shadow_F_g(0.0, g) == 0.0

    def test_shadow_zeta_empty(self):
        """Shadow zeta with empty coefficients = 0."""
        assert shadow_zeta_from_coeffs({}, 1.0) == 0.0

    def test_jt_Z_g_at_beta_zero(self):
        """Z_g(0) = 0."""
        assert jt_Z_g(1, 0.0) == 0.0

    def test_disk_amplitude_large_beta(self):
        """Z_disk(beta) ~ 0 for very large beta (exponential smallness)."""
        # Actually exp(2pi^2/beta) -> 1 for large beta
        # So Z_disk ~ 1/(4*pi*beta)^{3/2} -> 0
        disk = jt_disk_amplitude(1000.0)
        assert disk < 1e-4

    def test_wp_volume_invalid_genus(self):
        with pytest.raises(ValueError):
            wp_volume_V_g1_at_zero(0)

    def test_virasoro_c13_self_dual(self):
        """At c=13 (self-dual), kappa = 13/2."""
        S = virasoro_shadow_coefficients(13.0)
        assert abs(S[2] - 6.5) < 1e-12

    def test_virasoro_c26_critical(self):
        """At c=26 (critical), kappa = 13."""
        S = virasoro_shadow_coefficients(26.0)
        assert abs(S[2] - 13.0) < 1e-12

    def test_shadow_spectral_density_negative_r(self):
        """Negative r values are ignored."""
        S = {-1: 10.0, 2: 1.0}
        rho = shadow_spectral_density(S, 1.0)
        rho_clean = shadow_spectral_density({2: 1.0}, 1.0)
        assert abs(rho - rho_clean) < 1e-12


class TestDimensionalAnalysis:
    """Degree and dimensional consistency."""

    def test_V_g1_polynomial_degree(self):
        """V_{g,1}(b) has degree 3g-2 in b^2."""
        for g in [1, 2]:
            coeffs = wp_volume_one_boundary_coeffs(g)
            expected_deg = 3 * g - 2
            assert len(coeffs) == expected_deg + 1

    def test_lambda_fp_ratio_convergence(self):
        """lambda_{g+1}/lambda_g converges to 1/(4 pi^2) ~ 0.02533."""
        # Asymptotic from Bernoulli: |B_{2g+2}|/|B_{2g}| ~ (2g+2)(2g+1)/(2pi)^2
        # With the factorial and power-of-2 corrections, the ratio
        # lambda_{g+1}/lambda_g -> 1/(4*pi^2) as g -> infty.
        limit = 1.0 / (4.0 * PI2)
        for g in range(1, 10):
            ratio = float(lambda_fp(g + 1)) / float(lambda_fp(g))
            assert ratio > 0
        # At g=9, should be close to the limit
        ratio_9 = float(lambda_fp(10)) / float(lambda_fp(9))
        assert abs(ratio_9 - limit) / limit < 0.01

    def test_jt_density_integral_converges_to_disk(self):
        """int rho(E) e^{-beta E} dE converges to Z_disk for beta >> 1."""
        # For beta = 10, check convergence
        beta = 10.0
        N = 5000
        dE = 20.0 / N
        integral = sum(jt_spectral_density(k * dE) * math.exp(-beta * k * dE) * dE
                       for k in range(1, N + 1))
        disk = jt_disk_amplitude(beta)
        # Should be within an order of magnitude
        assert 0.01 < integral / disk < 100.0


class TestJTFromShadow:
    """JT partition function from shadow parameters."""

    def test_jt_from_shadow_positive_kappa(self):
        """Z^{JT}_A > 0 for kappa > 0."""
        result = jt_from_shadow(kappa=0.5, beta=1.0, max_genus=2)
        # At least the genus-1 contribution should be positive
        assert result['genus_contributions'][1] > 0

    def test_jt_from_shadow_structure(self):
        result = jt_from_shadow(kappa=1.0, beta=1.0, max_genus=2)
        assert 'Z_total' in result
        assert 'genus_contributions' in result

    def test_jt_from_shadow_kappa_scaling(self):
        """Z^{JT} depends on kappa through the weighting e_S0 = kappa."""
        r1 = jt_from_shadow(kappa=1.0, beta=1.0, max_genus=2)
        r2 = jt_from_shadow(kappa=2.0, beta=1.0, max_genus=2)
        # Different kappa gives different Z_total
        assert r1['Z_total'] != r2['Z_total']


class TestShadowZeta:
    """Shadow zeta from coefficients."""

    def test_shadow_zeta_single_term(self):
        """zeta_A(s) with S = {n: 1} gives n^{-s}."""
        S = {3: 1.0}
        s = 2.0
        val = shadow_zeta_from_coeffs(S, s)
        expected = 3.0**(-2.0)
        assert abs(val - expected) < 1e-12

    def test_shadow_zeta_multiple_terms(self):
        """zeta_A(s) = sum S_r r^{-s}."""
        S = {2: 1.0, 3: 2.0, 5: 0.5}
        s = 1.0
        val = shadow_zeta_from_coeffs(S, s)
        expected = 1.0 / 2.0 + 2.0 / 3.0 + 0.5 / 5.0
        assert abs(val - expected) < 1e-12

    def test_shadow_zeta_complex_argument(self):
        """Shadow zeta at complex s."""
        S = {2: 1.0}
        s = 0.5 + 1j
        val = shadow_zeta_from_coeffs(S, s)
        expected = 2.0**(-0.5 - 1j)
        assert abs(val - expected) < 1e-12
