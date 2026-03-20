#!/usr/bin/env python3
r"""Tests for lattice shadow periods: the arithmetic sieve for lattice VOAs.

Verifies the fundamental correspondence:
  Shadow arity 2 (kappa) -> Riemann zeta periods
  Shadow arity 3 (cubic) -> Eisenstein / Dedekind periods
  Shadow arity >= 4      -> Cusp form / Hecke periods

Five principal lattice VOAs:
  V_Z, V_{Z^2}, V_{A_2}, V_{E_8}, V_{Leech}

References:
  - arithmetic_shadows.tex: thm:shadow-spectral-correspondence
  - concordance.tex: sec:concordance-spectral-continuation
"""

import pytest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from compute.lib.lattice_shadow_periods import (
    sigma_k,
    ramanujan_tau,
    eisenstein_series_weight_k,
    eisenstein_coefficient,
    cusp_form_dim,
    theta_function_rank1,
    theta_function_e8,
    theta_leech,
    leech_delta_coefficient,
    theta_coefficient_e8,
    theta_coefficient_leech,
    hecke_decompose,
    epstein_zeta_lattice,
    l_function_content,
    shadow_depth_from_hecke,
    shadow_arity_to_l_function,
    verify_arithmetic_sieve,
    period_matrix,
    lattice_data,
    shadow_period_dictionary,
    L_ramanujan_delta,
    _bernoulli,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# =========================================================================
# Divisor sums
# =========================================================================

class TestDivisorSums:
    def test_sigma0_1(self):
        """sigma_0(1) = 1 (number of divisors)."""
        assert sigma_k(1, 0) == 1

    def test_sigma0_6(self):
        """sigma_0(6) = 4 (divisors: 1,2,3,6)."""
        assert sigma_k(6, 0) == 4

    def test_sigma1_6(self):
        """sigma_1(6) = 1+2+3+6 = 12."""
        assert sigma_k(6, 1) == 12

    def test_sigma3_1(self):
        """sigma_3(1) = 1."""
        assert sigma_k(1, 3) == 1

    def test_sigma3_2(self):
        """sigma_3(2) = 1 + 8 = 9."""
        assert sigma_k(2, 3) == 9

    def test_sigma3_3(self):
        """sigma_3(3) = 1 + 27 = 28."""
        assert sigma_k(3, 3) == 28

    def test_sigma3_4(self):
        """sigma_3(4) = 1 + 8 + 64 = 73."""
        assert sigma_k(4, 3) == 73

    def test_sigma11_1(self):
        """sigma_11(1) = 1."""
        assert sigma_k(1, 11) == 1

    def test_sigma11_2(self):
        """sigma_11(2) = 1 + 2^11 = 2049."""
        assert sigma_k(2, 11) == 1 + 2048


# =========================================================================
# Theta functions
# =========================================================================

class TestThetaFunctions:
    @skip_no_mpmath
    def test_e4_leading(self):
        """E_4 = 1 + 240q + ...: the constant term is 1."""
        tau = mpmath.mpc(0, 1)  # tau = i, q = e^{-2pi} ~ 0.00187
        val = theta_function_e8(tau, nmax=20)
        # At tau = i, q ~ 0.00187, so E_4(i) ~ 1 + 240*0.00187 + ...
        assert abs(val - 1) < 1  # E_4(i) is close to 1

    @skip_no_mpmath
    def test_e4_sigma3(self):
        """E_4 coefficient of q^n is 240*sigma_3(n)."""
        # Check via eisenstein_coefficient
        for n in range(1, 8):
            coeff = eisenstein_coefficient(4, n)
            expected = 240 * sigma_k(n, 3)
            assert coeff == expected, f"E_4 coefficient mismatch at n={n}"

    @skip_no_mpmath
    def test_e4_first_coefficients(self):
        """E_4 = 1 + 240q + 2160q^2 + 6720q^3 + ..."""
        assert eisenstein_coefficient(4, 0) == 1
        assert eisenstein_coefficient(4, 1) == 240
        assert eisenstein_coefficient(4, 2) == 2160
        assert eisenstein_coefficient(4, 3) == 6720

    @skip_no_mpmath
    def test_leech_theta_no_roots(self):
        """Theta_Leech has 0 vectors of norm 2 (no roots in the Leech lattice)."""
        assert theta_coefficient_leech(1) == 0

    @skip_no_mpmath
    def test_leech_theta_minimal_vectors(self):
        """Theta_Leech coefficient at q^2 is 196560 (minimal vectors)."""
        assert theta_coefficient_leech(2) == 196560

    @skip_no_mpmath
    def test_leech_theta_norm6(self):
        """Theta_Leech coefficient at q^3 is 16773120."""
        assert theta_coefficient_leech(3) == 16773120

    @skip_no_mpmath
    def test_leech_coefficient_exact(self):
        """The Leech coefficient c_Delta = -65520/691."""
        c = leech_delta_coefficient()
        assert c == Fraction(-65520, 691)
        assert c.numerator == -65520
        assert c.denominator == 691

    @skip_no_mpmath
    def test_theta_rank1_symmetry(self):
        """theta_3(2*tau) is even: same contribution from +n and -n."""
        tau = mpmath.mpc(0, 0.5)
        val = theta_function_rank1(tau, nmax=100)
        # Should be real and positive (all terms are real positive)
        assert abs(mpmath.im(val)) < 1e-30

    @skip_no_mpmath
    def test_e4_at_i(self):
        """E_4(i) is known exactly: E_4(i) = 12*Gamma(1/4)^8/(2*pi)^6 / (16*pi^2)."""
        # Just check it's a real number close to known numerical value ~ 1.4557...
        tau = mpmath.mpc(0, 1)
        val = theta_function_e8(tau, nmax=50)
        assert abs(mpmath.im(val)) < 1e-30
        # E_4(i) > 1 (positive coefficients)
        assert mpmath.re(val) > 1


# =========================================================================
# Ramanujan Delta and tau function
# =========================================================================

class TestRamanujanDelta:
    def test_tau_1(self):
        """tau(1) = 1."""
        assert ramanujan_tau(1) == 1

    def test_tau_2(self):
        """tau(2) = -24."""
        assert ramanujan_tau(2) == -24

    def test_tau_3(self):
        """tau(3) = 252."""
        assert ramanujan_tau(3) == 252

    def test_tau_4(self):
        """tau(4) = -1472."""
        assert ramanujan_tau(4) == -1472

    def test_tau_5(self):
        """tau(5) = 4830."""
        assert ramanujan_tau(5) == 4830

    def test_tau_6(self):
        """tau(6) = -6048."""
        assert ramanujan_tau(6) == -6048

    def test_tau_7(self):
        """tau(7) = -16744."""
        assert ramanujan_tau(7) == -16744

    def test_tau_8(self):
        """tau(8) = 84480."""
        assert ramanujan_tau(8) == 84480

    def test_tau_multiplicative_2_3(self):
        """tau(6) = tau(2)*tau(3) for coprime 2,3."""
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)

    def test_tau_multiplicative_2_5(self):
        """tau(10) = tau(2)*tau(5) for coprime 2,5."""
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)

    def test_tau_multiplicative_3_5(self):
        """tau(15) = tau(3)*tau(5) for coprime 3,5."""
        assert ramanujan_tau(15) == ramanujan_tau(3) * ramanujan_tau(5)

    def test_tau_ramanujan_bound_small_primes(self):
        """|tau(p)| <= 2*p^{11/2} for primes p (Deligne's theorem)."""
        primes = [2, 3, 5, 7, 11, 13]
        for p in primes:
            bound = 2 * p ** 5.5
            assert abs(ramanujan_tau(p)) <= bound, \
                f"|tau({p})| = {abs(ramanujan_tau(p))} > {bound}"

    def test_delta_is_cusp(self):
        """Delta vanishes at cusp: the constant term (q^0 coefficient) is 0."""
        # Delta = sum_{n>=1} tau(n) q^n, so there is no q^0 term.
        assert ramanujan_tau(0) == 0

    def test_tau_0(self):
        """tau(0) = 0 by convention."""
        assert ramanujan_tau(0) == 0

    def test_tau_negative(self):
        """tau(n) = 0 for n < 0."""
        assert ramanujan_tau(-1) == 0
        assert ramanujan_tau(-5) == 0


# =========================================================================
# Eisenstein series coefficients
# =========================================================================

class TestEisensteinCoefficients:
    def test_e4_constant(self):
        assert eisenstein_coefficient(4, 0) == 1

    def test_e6_constant(self):
        assert eisenstein_coefficient(6, 0) == 1

    def test_e6_q1(self):
        """E_6 coefficient of q^1 is -504."""
        assert eisenstein_coefficient(6, 1) == -504

    def test_e12_q1(self):
        """E_{12} coefficient of q^1."""
        # E_{12} = 1 + (-24/B_{12}) * sigma_11(1) * q + ...
        # B_{12} = -691/2730
        # -24 / (-691/2730) = 24 * 2730 / 691 = 65520/691
        coeff = eisenstein_coefficient(12, 1)
        assert coeff == Fraction(65520, 691)

    def test_e4_e6_relation(self):
        """E_4 and E_6 first coefficients are standard."""
        assert eisenstein_coefficient(4, 1) == 240
        assert eisenstein_coefficient(6, 1) == -504

    def test_bernoulli_b2(self):
        """B_2 = 1/6."""
        assert _bernoulli(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        """B_4 = -1/30."""
        assert _bernoulli(4) == Fraction(-1, 30)

    def test_bernoulli_b6(self):
        """B_6 = 1/42."""
        assert _bernoulli(6) == Fraction(1, 42)

    def test_bernoulli_b12(self):
        """B_{12} = -691/2730."""
        assert _bernoulli(12) == Fraction(-691, 2730)


# =========================================================================
# Cusp form dimensions
# =========================================================================

class TestCuspFormDim:
    def test_s2(self):
        """dim S_2(SL_2(Z)) = 0."""
        assert cusp_form_dim(2) == 0

    def test_s4(self):
        """dim S_4(SL_2(Z)) = 0."""
        assert cusp_form_dim(4) == 0

    def test_s6(self):
        """dim S_6(SL_2(Z)) = 0."""
        assert cusp_form_dim(6) == 0

    def test_s8(self):
        """dim S_8(SL_2(Z)) = 0."""
        assert cusp_form_dim(8) == 0

    def test_s10(self):
        """dim S_{10}(SL_2(Z)) = 0."""
        assert cusp_form_dim(10) == 0

    def test_s12(self):
        """dim S_{12}(SL_2(Z)) = 1 (Ramanujan Delta)."""
        assert cusp_form_dim(12) == 1

    def test_s14(self):
        """dim S_{14}(SL_2(Z)) = 0."""
        assert cusp_form_dim(14) == 0

    def test_s16(self):
        """dim S_{16}(SL_2(Z)) = 1."""
        assert cusp_form_dim(16) == 1

    def test_s18(self):
        """dim S_{18}(SL_2(Z)) = 1."""
        assert cusp_form_dim(18) == 1

    def test_s20(self):
        """dim S_{20}(SL_2(Z)) = 1."""
        assert cusp_form_dim(20) == 1

    def test_s22(self):
        """dim S_{22}(SL_2(Z)) = 1."""
        assert cusp_form_dim(22) == 1

    def test_s24(self):
        """dim S_{24}(SL_2(Z)) = 2."""
        assert cusp_form_dim(24) == 2

    def test_s26(self):
        """dim S_{26}(SL_2(Z)) = 1 (26 = 2 mod 12, so floor(26/12) - 1 = 1)."""
        assert cusp_form_dim(26) == 1

    def test_odd_weight(self):
        """No cusp forms of odd weight for SL_2(Z)."""
        for k in [1, 3, 5, 7, 9, 11, 13]:
            assert cusp_form_dim(k) == 0

    def test_negative_weight(self):
        """No cusp forms of negative weight."""
        assert cusp_form_dim(-2) == 0
        assert cusp_form_dim(0) == 0


# =========================================================================
# Epstein zeta factorizations
# =========================================================================

class TestEpsteinZeta:
    @skip_no_mpmath
    def test_e8_factorization_at_s5(self):
        """epsilon^8_s = 240*4^{-s}*zeta(s)*zeta(s-3) at s=5."""
        val = epstein_zeta_lattice('E8', 5.0)
        expected = 240 * 4 ** (-5.0) * float(mpmath.zeta(5)) * float(mpmath.zeta(2))
        assert abs(float(val) - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_e8_factorization_at_s6(self):
        """epsilon^8_s at s=6."""
        val = epstein_zeta_lattice('E8', 6.0)
        expected = 240 * 4 ** (-6.0) * float(mpmath.zeta(6)) * float(mpmath.zeta(3))
        assert abs(float(val) - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_e8_factorization_at_s8(self):
        """epsilon^8_s at s=8."""
        val = epstein_zeta_lattice('E8', 8.0)
        expected = 240 * 4 ** (-8.0) * float(mpmath.zeta(8)) * float(mpmath.zeta(5))
        assert abs(float(val) - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_rank1_factorization_at_s2(self):
        """epsilon^1_s = 2*zeta(2s) at s=2."""
        val = epstein_zeta_lattice('Z', 2.0)
        expected = 2 * float(mpmath.zeta(4))
        assert abs(float(val) - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_rank1_factorization_at_s3(self):
        """epsilon^1_s = 2*zeta(2s) at s=3."""
        val = epstein_zeta_lattice('Z', 3.0)
        expected = 2 * float(mpmath.zeta(6))
        assert abs(float(val) - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_z2_factorization_positive(self):
        """epsilon^2_s for Z^2 at s=3 is positive and finite."""
        val = epstein_zeta_lattice('Z2', 3.0)
        assert float(mpmath.re(val)) > 0

    @skip_no_mpmath
    def test_a2_factorization_positive(self):
        """epsilon^2_s for A_2 at s=3 is positive and finite."""
        val = epstein_zeta_lattice('A2', 3.0)
        assert float(mpmath.re(val)) > 0

    @skip_no_mpmath
    def test_z2_vs_a2_different(self):
        """Z^2 and A_2 Epstein zetas differ (different lattices)."""
        z2_val = float(mpmath.re(epstein_zeta_lattice('Z2', 3.0)))
        a2_val = float(mpmath.re(epstein_zeta_lattice('A2', 3.0)))
        assert abs(z2_val - a2_val) / max(abs(z2_val), abs(a2_val)) > 0.01


# =========================================================================
# Hecke decomposition
# =========================================================================

class TestHeckeDecomposition:
    def test_e8_pure_eisenstein(self):
        """E_4 is pure Eisenstein: no cusp forms in S_4."""
        decomp = hecke_decompose('E8')
        assert decomp['eisenstein_only'] is True
        assert decomp['cusp_dim'] == 0
        assert len(decomp['cusp_coeffs']) == 0

    def test_leech_has_cusp_form(self):
        """Theta_Leech = E_{12} + c*Delta: cusp form is present."""
        decomp = hecke_decompose('Leech')
        assert decomp['eisenstein_only'] is False
        assert decomp['cusp_dim'] == 1
        assert len(decomp['cusp_coeffs']) == 1
        name, coeff = decomp['cusp_coeffs'][0]
        assert name == 'Delta'
        assert coeff == Fraction(-65520, 691)

    def test_z_pure_eisenstein(self):
        """V_Z: no cusp forms in M_{1/2}."""
        decomp = hecke_decompose('Z')
        assert decomp['eisenstein_only'] is True

    def test_z2_pure_eisenstein(self):
        """V_{Z^2}: no cusp forms in M_1."""
        decomp = hecke_decompose('Z2')
        assert decomp['eisenstein_only'] is True

    def test_a2_pure_eisenstein(self):
        """V_{A_2}: no cusp forms in M_1(Gamma_0(3))."""
        decomp = hecke_decompose('A2')
        assert decomp['eisenstein_only'] is True

    def test_e8_weight(self):
        """E_8 theta function has weight 4 = rank/2."""
        decomp = hecke_decompose('E8')
        assert decomp['weight'] == 4

    def test_leech_weight(self):
        """Leech theta function has weight 12 = rank/2."""
        decomp = hecke_decompose('Leech')
        assert decomp['weight'] == 12


# =========================================================================
# Arithmetic sieve
# =========================================================================

class TestArithmeticSieve:
    def test_arity2_is_zeta_e8(self):
        """Arity 2 for E_8 -> zeta(s) (Riemann)."""
        result = shadow_arity_to_l_function('E8', 2)
        assert result is not None
        assert result['type'] == 'riemann'
        assert result['period_type'] == 'Riemann'

    def test_arity3_is_dedekind_e8(self):
        """Arity 3 for E_8 -> zeta(s-3) (Dedekind)."""
        result = shadow_arity_to_l_function('E8', 3)
        assert result is not None
        assert result['type'] == 'riemann'
        assert result['period_type'] == 'Dedekind'

    def test_arity4_leech_is_delta(self):
        """Arity 4 for Leech -> L(s, Delta) (Hecke)."""
        result = shadow_arity_to_l_function('Leech', 4)
        assert result is not None
        assert result['type'] == 'hecke'
        assert result['cusp_form'] == 'Delta'
        assert result['period_type'] == 'Hecke'

    def test_e8_no_arity4(self):
        """E_8 has no arity-4 shadow: no cusp forms in S_4."""
        result = shadow_arity_to_l_function('E8', 4)
        assert result is None

    def test_z_no_arity3(self):
        """V_Z has no arity-3 shadow: rank too small."""
        result = shadow_arity_to_l_function('Z', 3)
        assert result is None

    def test_z_arity2(self):
        """V_Z arity 2 -> zeta(2s)."""
        result = shadow_arity_to_l_function('Z', 2)
        assert result is not None
        assert result['factor'] == 'zeta(2s)'

    def test_leech_arity2(self):
        """Leech arity 2 -> zeta(s)."""
        result = shadow_arity_to_l_function('Leech', 2)
        assert result is not None
        assert result['type'] == 'riemann'

    def test_leech_arity3(self):
        """Leech arity 3 -> zeta(s-11) (Dedekind)."""
        result = shadow_arity_to_l_function('Leech', 3)
        assert result is not None
        assert result['period_type'] == 'Dedekind'

    def test_leech_no_arity5(self):
        """Leech has no arity-5 shadow: only 1 cusp form in S_{12}."""
        result = shadow_arity_to_l_function('Leech', 5)
        assert result is None


# =========================================================================
# Depth formula
# =========================================================================

class TestDepthFormula:
    def test_rank1_depth2(self):
        """V_Z: rank 1, depth 2 (Gaussian)."""
        assert shadow_depth_from_hecke(1, 0) == 2

    def test_rank2_depth2(self):
        """V_{Z^2}: rank 2, depth 2."""
        assert shadow_depth_from_hecke(2, 0) == 2

    def test_e8_depth3(self):
        """V_{E_8}: rank 8, cusp_dim 0, depth 3 (Lie/tree)."""
        assert shadow_depth_from_hecke(8, 0) == 3

    def test_leech_depth4(self):
        """V_Leech: rank 24, cusp_dim 1, depth 4 (contact)."""
        assert shadow_depth_from_hecke(24, 1) == 4

    def test_depth_from_cusp_dim_generic(self):
        """For rank > 2 with cusp_dim > 0: depth = 1 + 2 + 1 = 4."""
        assert shadow_depth_from_hecke(16, 1) == 4

    def test_depth_rank0(self):
        """Rank 0: trivial, depth 1."""
        assert shadow_depth_from_hecke(0, 0) == 1

    def test_depth_matches_catalog(self):
        """Depth formula matches catalog values for all 5 principal lattices."""
        for name in ['Z', 'Z2', 'A2', 'E8', 'Leech']:
            data = lattice_data(name)
            decomp = hecke_decompose(name)
            computed = shadow_depth_from_hecke(data['rank'], decomp['cusp_dim'])
            assert computed == data['shadow_depth'], \
                f"{name}: computed {computed}, expected {data['shadow_depth']}"


# =========================================================================
# L-functions
# =========================================================================

class TestLFunctions:
    @skip_no_mpmath
    def test_L_delta_convergence(self):
        """L(s, Delta) converges for Re(s) > 13/2: check at s=8."""
        # s=8 > 6.5, should converge
        val = L_ramanujan_delta(8.0, num_terms=50)
        # Check it's a finite real number
        assert mpmath.isfinite(val)

    @skip_no_mpmath
    def test_L_delta_euler_product_at_p2(self):
        """L(s, Delta) Euler factor at p=2: 1/(1 - tau(2)*2^{-s} + 2^{11-2s}).

        At s=8: factor = 1/(1 - (-24)*2^{-8} + 2^{11-16})
                       = 1/(1 + 24/256 + 1/32)
                       = 1/(1 + 0.09375 + 0.03125)
                       = 1/1.125
        """
        s = 8.0
        tau_2 = ramanujan_tau(2)
        euler_factor = 1.0 / (1 - tau_2 * 2 ** (-s) + 2 ** (11 - 2 * s))
        expected = 1.0 / (1 + 24 / 256 + 1 / 32)
        assert abs(euler_factor - expected) < 1e-10

    def test_critical_line_count_z(self):
        """V_Z: 1 critical line (Re(s)=1/4 from zeta(2s))."""
        content = l_function_content('Z')
        assert len(content['l_functions']) == 1

    def test_critical_line_count_e8(self):
        """V_{E_8}: 2 critical lines (Re(s)=1/2 and Re(s)=7/2)."""
        content = l_function_content('E8')
        assert len(content['l_functions']) == 2
        lines = {lf['critical_line'] for lf in content['l_functions']}
        assert Fraction(1, 2) in lines
        assert Fraction(7, 2) in lines

    def test_critical_line_count_leech(self):
        """V_Leech: 3 critical lines (Re(s)=1/2, 23/2, 6)."""
        content = l_function_content('Leech')
        assert len(content['l_functions']) == 3
        lines = {lf['critical_line'] for lf in content['l_functions']}
        assert Fraction(1, 2) in lines
        assert Fraction(23, 2) in lines
        assert Fraction(6, 1) in lines

    def test_leech_has_hecke_l(self):
        """Leech L-content includes a Hecke L-function (from Delta)."""
        content = l_function_content('Leech')
        types = {lf['type'] for lf in content['l_functions']}
        assert 'hecke' in types


# =========================================================================
# Shadow period matrix
# =========================================================================

class TestShadowPeriodMatrix:
    def test_e8_period_matrix(self):
        """E_8 period matrix: arity 2 and 3 active, rest None."""
        pm = period_matrix('E8', num_arities=6)
        assert pm[2] is not None  # kappa
        assert pm[3] is not None  # cubic
        assert pm[4] is None      # no cusp forms
        assert pm[5] is None
        assert pm[6] is None

    def test_leech_period_matrix(self):
        """Leech period matrix: arities 2, 3, 4 active, rest None."""
        pm = period_matrix('Leech', num_arities=6)
        assert pm[2] is not None  # kappa
        assert pm[3] is not None  # cubic (Dedekind)
        assert pm[4] is not None  # quartic (Delta)
        assert pm[5] is None      # only 1 cusp form
        assert pm[6] is None

    def test_z_period_matrix(self):
        """V_Z period matrix: only arity 2 active."""
        pm = period_matrix('Z', num_arities=6)
        assert pm[2] is not None
        assert pm[3] is None
        assert pm[4] is None

    def test_z2_period_matrix(self):
        """V_{Z^2} period matrix: only arity 2 active."""
        pm = period_matrix('Z2', num_arities=6)
        assert pm[2] is not None
        assert pm[3] is None

    def test_period_matrix_types(self):
        """Period matrix entries have correct period types."""
        pm = period_matrix('Leech', num_arities=4)
        assert pm[2]['period_type'] == 'Riemann'
        assert pm[3]['period_type'] == 'Dedekind'
        assert pm[4]['period_type'] == 'Hecke'


# =========================================================================
# Full sieve verification
# =========================================================================

class TestFullSieveVerification:
    def test_verify_z(self):
        """Full sieve verification for V_Z."""
        result = verify_arithmetic_sieve('Z')
        assert result['depth_match'] is True
        assert result['archetype'] == 'G'

    def test_verify_z2(self):
        """Full sieve verification for V_{Z^2}."""
        result = verify_arithmetic_sieve('Z2')
        assert result['depth_match'] is True
        assert result['archetype'] == 'G'

    def test_verify_a2(self):
        """Full sieve verification for V_{A_2}."""
        result = verify_arithmetic_sieve('A2')
        assert result['depth_match'] is True
        assert result['archetype'] == 'G'

    def test_verify_e8(self):
        """Full sieve verification for V_{E_8}."""
        result = verify_arithmetic_sieve('E8')
        assert result['depth_match'] is True
        assert result['archetype'] == 'L'

    def test_verify_leech(self):
        """Full sieve verification for V_Leech."""
        result = verify_arithmetic_sieve('Leech')
        assert result['depth_match'] is True
        assert result['archetype'] == 'C'

    def test_all_lattices_consistent(self):
        """All 5 principal lattices pass the arithmetic sieve."""
        for name in ['Z', 'Z2', 'A2', 'E8', 'Leech']:
            result = verify_arithmetic_sieve(name)
            assert result['depth_match'] is True, \
                f"Sieve failed for {name}"


# =========================================================================
# Shadow period dictionary
# =========================================================================

class TestShadowPeriodDictionary:
    def test_dictionary_length(self):
        """Dictionary has 4 entries (arities 2-5)."""
        d = shadow_period_dictionary()
        assert len(d) == 4

    def test_arity2_riemann(self):
        """Arity 2 is Riemann period type."""
        d = shadow_period_dictionary()
        entry = [e for e in d if e['arity'] == 2][0]
        assert entry['period_type'] == 'Riemann'
        assert entry['shadow_name'] == 'kappa'

    def test_arity3_dedekind(self):
        """Arity 3 is Dedekind period type."""
        d = shadow_period_dictionary()
        entry = [e for e in d if e['arity'] == 3][0]
        assert entry['period_type'] == 'Dedekind'
        assert entry['shadow_name'] == 'cubic'

    def test_arity4_hecke(self):
        """Arity 4 is Hecke period type."""
        d = shadow_period_dictionary()
        entry = [e for e in d if e['arity'] == 4][0]
        assert entry['period_type'] == 'Hecke'
        assert entry['shadow_name'] == 'quartic'


# =========================================================================
# Lattice data catalog
# =========================================================================

class TestLatticeData:
    def test_z_rank(self):
        assert lattice_data('Z')['rank'] == 1

    def test_z2_rank(self):
        assert lattice_data('Z2')['rank'] == 2

    def test_a2_rank(self):
        assert lattice_data('A2')['rank'] == 2

    def test_e8_rank(self):
        assert lattice_data('E8')['rank'] == 8

    def test_leech_rank(self):
        assert lattice_data('Leech')['rank'] == 24

    def test_unknown_lattice(self):
        with pytest.raises(ValueError):
            lattice_data('D16')

    def test_archetype_gaussian(self):
        """Rank 1 and 2 lattices are Gaussian (G)."""
        for name in ['Z', 'Z2', 'A2']:
            assert lattice_data(name)['archetype'] == 'G'

    def test_archetype_lie(self):
        """E_8 is Lie/tree (L)."""
        assert lattice_data('E8')['archetype'] == 'L'

    def test_archetype_contact(self):
        """Leech is contact (C)."""
        assert lattice_data('Leech')['archetype'] == 'C'


# =========================================================================
# E_8 theta coefficients
# =========================================================================

class TestE8ThetaCoefficients:
    def test_zero_vector(self):
        """r_8(0) = 1 (the zero vector)."""
        assert theta_coefficient_e8(0) == 1

    def test_roots(self):
        """r_8(1) = 240 (the 240 roots of E_8)."""
        assert theta_coefficient_e8(1) == 240

    def test_norm4(self):
        """r_8(2) = 2160 = 240*sigma_3(2) = 240*9."""
        assert theta_coefficient_e8(2) == 2160

    def test_norm6(self):
        """r_8(3) = 6720 = 240*sigma_3(3) = 240*28."""
        assert theta_coefficient_e8(3) == 6720

    def test_negative(self):
        """No vectors of negative norm."""
        assert theta_coefficient_e8(-1) == 0
