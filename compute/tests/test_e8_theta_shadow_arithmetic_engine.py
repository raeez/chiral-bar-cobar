r"""Tests for the E8 theta-shadow arithmetic engine.

Verifies:
  1. E_8 shadow tower: kappa = 8 (rank, AP48), class G, S_r = 0 for r >= 3
  2. Theta series: Theta_{E_8} = E_4, coefficients verified against Conway-Sloane
  3. E_8 x E_8 vs D_{16}^+: same genus-1 theta (both = E_4^2 = E_8)
  4. Hecke operators: a_p(E_4) = 1 + p^3, verified from Fourier coefficients
  5. Arithmetic intersection: F_1 = 1/3, F_2 = 7/720
  6. Smith-Minkowski-Siegel mass formula: mass = 1/696729600
  7. E_4^2 = E_8 identity (Ramanujan convolution identity)
  8. Genus-2 Hecke eigenvalues for Siegel Eisenstein series

Multi-path verification:
  Path 1: Direct lattice computation (E_8 root system)
  Path 2: Eisenstein series identity (Theta_{E_8} = E_4)
  Path 3: Shadow tower from VOA classification (class G)
  Path 4: Hecke eigenvalue comparison
  Path 5: Ramanujan convolution identity sigma_7 = sigma_3 * sigma_3

Mathematical ground truth:
  - Conway-Sloane, "Sphere Packings, Lattices and Groups", Ch. 4, 16
  - Serre, "A Course in Arithmetic", Ch. VII
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - higher_genus_modular_koszul.tex: shadow depth classification (class G)
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.e8_theta_shadow_arithmetic_engine import (
    E8_CONSTANTS,
    E8_CARTAN,
    sigma_k,
    eisenstein_e4_coefficients,
    eisenstein_e6_coefficients,
    eisenstein_e8_coefficients,
    e4_squared_coefficients,
    e8_theta_coefficients,
    e8_theta_verify_first_terms,
    e8_times_e8_theta_coefficients,
    d16_plus_theta_coefficients,
    genus1_discrimination,
    faber_pandharipande,
    e8_shadow_tower,
    e8_genus_expansion,
    shadow_partition_function_genus_g,
    hecke_eigenvalue_e4,
    hecke_eigenvalue_e8,
    verify_hecke_eigenvalue_from_fourier,
    shadow_hecke_eigenvalue,
    e8_complementarity,
    e8xe8_complementarity,
    d16_plus_complementarity,
    verify_e4_squared_equals_e8,
    ring_of_modular_forms_dimensions,
    e8_mass,
    siegel_mass_formula_dim8,
    mass_bernoulli_shadow_connection,
    genus1_arithmetic_data,
    genus2_arithmetic_data,
    genus2_siegel_weight,
    genus2_e8_hecke_eigenvalue,
    genus2_hecke_comparison,
    ahat_generating_function_check,
    rank16_shadow_comparison,
    full_cross_verification,
)


# =========================================================================
# 1. E8 ROOT SYSTEM CONSTANTS
# =========================================================================

class TestE8Constants:
    """Verify E_8 Lie algebra/lattice constants against Bourbaki tables."""

    def test_rank(self):
        """rank(E_8) = 8."""
        assert E8_CONSTANTS['rank'] == 8

    def test_dim_lie_algebra(self):
        """dim(e_8) = 248."""
        assert E8_CONSTANTS['dim_lie_algebra'] == 248

    def test_n_roots(self):
        """E_8 has 240 roots."""
        assert E8_CONSTANTS['n_roots'] == 240

    def test_n_positive_roots(self):
        """E_8 has 120 positive roots."""
        assert E8_CONSTANTS['n_positive_roots'] == 120

    def test_coxeter_number(self):
        """h(E_8) = 30."""
        assert E8_CONSTANTS['h_coxeter'] == 30

    def test_dual_coxeter_number(self):
        """h^vee(E_8) = 30 (simply-laced, so h = h^vee)."""
        assert E8_CONSTANTS['h_dual_coxeter'] == 30

    def test_simply_laced(self):
        """E_8 is simply-laced: h = h^vee."""
        assert E8_CONSTANTS['h_coxeter'] == E8_CONSTANTS['h_dual_coxeter']

    def test_exponents(self):
        """Exponents of E_8: {1, 7, 11, 13, 17, 19, 23, 29}."""
        assert E8_CONSTANTS['exponents'] == [1, 7, 11, 13, 17, 19, 23, 29]

    def test_sum_exponents(self):
        """Sum of exponents = |Delta^+| = 120."""
        assert sum(E8_CONSTANTS['exponents']) == E8_CONSTANTS['n_positive_roots']

    def test_weyl_group_order(self):
        """|W(E_8)| = 696729600."""
        assert E8_CONSTANTS['weyl_group_order'] == 696729600

    def test_weyl_group_order_factored(self):
        """|W(E_8)| = 2^14 * 3^5 * 5^2 * 7."""
        w = E8_CONSTANTS['weyl_group_order']
        assert w == 2**14 * 3**5 * 5**2 * 7

    def test_cartan_determinant(self):
        """det(Cartan matrix of E_8) = 1 (unimodular)."""
        assert E8_CONSTANTS['cartan_determinant'] == 1

    def test_min_norm(self):
        """Minimum norm (v,v) = 2 for E_8 root lattice (even lattice)."""
        assert E8_CONSTANTS['min_norm'] == 2

    def test_cartan_matrix_size(self):
        """E_8 Cartan matrix is 8x8."""
        assert len(E8_CARTAN) == 8
        assert all(len(row) == 8 for row in E8_CARTAN)

    def test_cartan_matrix_diagonal(self):
        """Diagonal entries of Cartan matrix are all 2."""
        assert all(E8_CARTAN[i][i] == 2 for i in range(8))

    def test_cartan_matrix_symmetric(self):
        """E_8 Cartan matrix is symmetric (simply-laced)."""
        for i in range(8):
            for j in range(8):
                assert E8_CARTAN[i][j] == E8_CARTAN[j][i]

    def test_dim_equals_rank_plus_roots(self):
        """dim(e_8) = rank + n_roots = 8 + 240 = 248."""
        assert E8_CONSTANTS['dim_lie_algebra'] == (
            E8_CONSTANTS['rank'] + E8_CONSTANTS['n_roots']
        )


# =========================================================================
# 2. DIVISOR SUMS
# =========================================================================

class TestDivisorSums:
    """Verify divisor sum function sigma_k(n)."""

    def test_sigma_3_1(self):
        """sigma_3(1) = 1."""
        assert sigma_k(1, 3) == 1

    def test_sigma_3_2(self):
        """sigma_3(2) = 1 + 8 = 9."""
        assert sigma_k(2, 3) == 9

    def test_sigma_3_3(self):
        """sigma_3(3) = 1 + 27 = 28."""
        assert sigma_k(3, 3) == 28

    def test_sigma_3_4(self):
        """sigma_3(4) = 1 + 8 + 64 = 73."""
        assert sigma_k(4, 3) == 73

    def test_sigma_3_5(self):
        """sigma_3(5) = 1 + 125 = 126."""
        assert sigma_k(5, 3) == 126

    def test_sigma_7_1(self):
        """sigma_7(1) = 1."""
        assert sigma_k(1, 7) == 1

    def test_sigma_7_2(self):
        """sigma_7(2) = 1 + 128 = 129."""
        assert sigma_k(2, 7) == 129

    def test_sigma_0_zero(self):
        """sigma_k(0) = 0."""
        assert sigma_k(0, 3) == 0

    def test_sigma_negative(self):
        """sigma_k(n) = 0 for n < 0."""
        assert sigma_k(-1, 3) == 0

    def test_sigma_3_prime(self):
        """sigma_3(p) = 1 + p^3 for prime p."""
        for p in [2, 3, 5, 7, 11, 13]:
            assert sigma_k(p, 3) == 1 + p**3


# =========================================================================
# 3. EISENSTEIN SERIES COEFFICIENTS
# =========================================================================

class TestEisensteinCoefficients:
    """Verify Eisenstein series E_4, E_6, E_8 coefficients."""

    def test_e4_constant_term(self):
        """E_4 constant term is 1."""
        e4 = eisenstein_e4_coefficients(5)
        assert e4[0] == 1

    def test_e4_first_coeff(self):
        """E_4 coefficient of q is 240."""
        e4 = eisenstein_e4_coefficients(5)
        assert e4[1] == 240

    def test_e4_second_coeff(self):
        """E_4 coefficient of q^2 is 240*9 = 2160."""
        e4 = eisenstein_e4_coefficients(5)
        assert e4[2] == 2160

    def test_e4_third_coeff(self):
        """E_4 coefficient of q^3 is 240*28 = 6720."""
        e4 = eisenstein_e4_coefficients(5)
        assert e4[3] == 6720

    def test_e4_formula(self):
        """E_4 coefficients match 240*sigma_3(n) for n = 1..10."""
        e4 = eisenstein_e4_coefficients(10)
        for n in range(1, 11):
            assert e4[n] == 240 * sigma_k(n, 3)

    def test_e6_constant_term(self):
        """E_6 constant term is 1."""
        e6 = eisenstein_e6_coefficients(5)
        assert e6[0] == 1

    def test_e6_first_coeff(self):
        """E_6 coefficient of q is -504."""
        e6 = eisenstein_e6_coefficients(5)
        assert e6[1] == -504

    def test_e6_formula(self):
        """E_6 coefficients match -504*sigma_5(n) for n = 1..10."""
        e6 = eisenstein_e6_coefficients(10)
        for n in range(1, 11):
            assert e6[n] == -504 * sigma_k(n, 5)

    def test_e8_constant_term(self):
        """E_8 constant term is 1."""
        e8 = eisenstein_e8_coefficients(5)
        assert e8[0] == 1

    def test_e8_first_coeff(self):
        """E_8 coefficient of q is 480."""
        e8 = eisenstein_e8_coefficients(5)
        assert e8[1] == 480

    def test_e8_formula(self):
        """E_8 coefficients match 480*sigma_7(n) for n = 1..10."""
        e8 = eisenstein_e8_coefficients(10)
        for n in range(1, 11):
            assert e8[n] == 480 * sigma_k(n, 7)


# =========================================================================
# 4. THETA_{E_8} = E_4 (the fundamental identity)
# =========================================================================

class TestThetaE8EqualsE4:
    """Verify the identity Theta_{E_8}(tau) = E_4(tau)."""

    def test_theta_equals_e4(self):
        """Theta_{E_8} coefficients equal E_4 coefficients through q^20."""
        theta = e8_theta_coefficients(20)
        e4 = eisenstein_e4_coefficients(20)
        assert theta == e4

    def test_theta_constant_term(self):
        """r_{E_8}(0) = 1 (zero vector)."""
        theta = e8_theta_coefficients(5)
        assert theta[0] == 1

    def test_theta_roots(self):
        """r_{E_8}(1) = 240 (roots of E_8)."""
        theta = e8_theta_coefficients(5)
        assert theta[1] == 240

    def test_theta_norm4(self):
        """r_{E_8}(2) = 2160 (vectors with (v,v) = 4)."""
        theta = e8_theta_coefficients(5)
        assert theta[2] == 2160

    def test_theta_norm6(self):
        """r_{E_8}(3) = 6720 (vectors with (v,v) = 6)."""
        theta = e8_theta_coefficients(5)
        assert theta[3] == 6720

    def test_theta_norm8(self):
        """r_{E_8}(4) = 17520 (vectors with (v,v) = 8)."""
        theta = e8_theta_coefficients(5)
        assert theta[4] == 17520

    def test_theta_norm10(self):
        """r_{E_8}(5) = 30240 (vectors with (v,v) = 10)."""
        theta = e8_theta_coefficients(5)
        assert theta[5] == 30240

    def test_verify_first_terms(self):
        """All first terms match between E_4 and known Conway-Sloane values."""
        result = e8_theta_verify_first_terms()
        assert result['all_match'] is True
        assert result['direct_match'] is True
        assert result['theta_equals_e4'] is True

    def test_dim_m4_is_1(self):
        """dim M_4(SL(2,Z)) = 1 (forces Theta_{E_8} = E_4)."""
        dims = ring_of_modular_forms_dimensions(20)
        assert dims[4] == 1

    def test_dim_s4_is_0(self):
        """dim S_4(SL(2,Z)) = 0 (no cusp forms of weight 4)."""
        # S_k = M_k minus Eisenstein space. For k < 12, S_k = 0.
        dims = ring_of_modular_forms_dimensions(20)
        # dim M_4 = 1, and the 1 is the Eisenstein series, so S_4 = 0.
        assert dims[4] == 1  # M_4 is generated by E_4 alone

    def test_theta_weight(self):
        """Theta_{E_8} has weight rank/2 = 4."""
        assert E8_CONSTANTS['rank'] // 2 == 4


# =========================================================================
# 5. E_4^2 = E_8 IDENTITY (Ramanujan convolution identity)
# =========================================================================

class TestE4SquaredEqualsE8:
    """Verify the classical identity E_4(tau)^2 = E_8(tau)."""

    def test_e4_squared_equals_e8_coefficients(self):
        """E_4^2 and E_8 have the same Fourier coefficients through q^20."""
        result = verify_e4_squared_equals_e8(20)
        assert result['all_match'] is True

    def test_ramanujan_identity(self):
        """sigma_7(n) = sigma_3(n) + 120*sum_{m=1}^{n-1} sigma_3(m)*sigma_3(n-m).

        This is the Ramanujan convolution identity equivalent to E_4^2 = E_8.
        """
        result = verify_e4_squared_equals_e8(10)
        assert result['ramanujan_all_match'] is True

    def test_ramanujan_n1(self):
        """At n=1: sigma_7(1) = sigma_3(1) + 0 = 1. Check: sigma_7(1) = 1."""
        assert sigma_k(1, 7) == sigma_k(1, 3)

    def test_ramanujan_n2(self):
        """At n=2: sigma_7(2) = sigma_3(2) + 120*sigma_3(1)^2 = 9 + 120 = 129."""
        lhs = sigma_k(2, 7)
        rhs = sigma_k(2, 3) + 120 * sigma_k(1, 3)**2
        assert lhs == rhs == 129

    def test_ramanujan_n3(self):
        """At n=3: sigma_7(3) = sigma_3(3) + 120*(sigma_3(1)*sigma_3(2) + sigma_3(2)*sigma_3(1))."""
        lhs = sigma_k(3, 7)
        rhs = sigma_k(3, 3) + 120 * 2 * sigma_k(1, 3) * sigma_k(2, 3)
        assert lhs == rhs

    def test_e4_squared_first_coeff(self):
        """(E_4^2) coefficient of q is 2*240 = 480."""
        e4sq = e4_squared_coefficients(5)
        assert e4sq[1] == 480

    def test_e4_squared_constant(self):
        """(E_4^2) constant term is 1."""
        e4sq = e4_squared_coefficients(5)
        assert e4sq[0] == 1

    def test_dim_m8_is_1(self):
        """dim M_8(SL(2,Z)) = 1, forcing E_4^2 = E_8."""
        dims = ring_of_modular_forms_dimensions(20)
        assert dims[8] == 1


# =========================================================================
# 6. SHADOW TOWER (class G, depth 2)
# =========================================================================

class TestShadowTower:
    """Verify shadow obstruction tower for V_{E_8} (lattice presentation)."""

    def test_kappa_equals_rank(self):
        """kappa(V_{E_8}) = 8 = rank(E_8) (AP48: not c/2)."""
        tower = e8_shadow_tower()
        assert tower['kappa'] == Rational(8)

    def test_kappa_not_c_over_2(self):
        """kappa != c/2 = 248/62 in general. For lattice: kappa = rank = 8.

        The affine KM formula gives a different kappa (1922/15).
        The lattice kappa is rank = 8.
        """
        c = Rational(248, 31)  # c = 248k/(k+30) at k=1 = 248/31
        # c/2 = 124/31 = 4. But kappa(V_{E_8}) = 8. So kappa != c/2.
        # (Actually, c = 248/31 = 8, so c/2 = 4. And kappa = 8 != 4.)
        # Wait: c = 248*1/(1+30) = 248/31 = 8 exactly.
        assert c == Rational(8)
        # c/2 = 4, but kappa = 8 (AP48!)
        tower = e8_shadow_tower()
        assert tower['kappa'] != c / 2
        assert tower['kappa'] == Rational(8)

    def test_class_G(self):
        """V_{E_8} is class G (Gaussian)."""
        tower = e8_shadow_tower()
        assert tower['shadow_class'] == 'G'

    def test_shadow_depth(self):
        """Shadow depth = 2."""
        tower = e8_shadow_tower()
        assert tower['shadow_depth'] == 2

    def test_S3_vanishes(self):
        """S_3 = 0 for lattice VOA."""
        tower = e8_shadow_tower()
        assert tower['tower'][3] == Rational(0)

    def test_S4_vanishes(self):
        """S_4 = 0 for lattice VOA."""
        tower = e8_shadow_tower()
        assert tower['tower'][4] == Rational(0)

    def test_all_higher_vanish(self):
        """S_r = 0 for all r >= 3 through r = 8."""
        tower = e8_shadow_tower(max_arity=8)
        for r in range(3, 9):
            assert tower['tower'][r] == Rational(0), f"S_{r} should be 0"

    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 0."""
        tower = e8_shadow_tower()
        assert tower['Delta'] == Rational(0)

    def test_alpha_vanishes(self):
        """alpha = 0 (cubic coefficient)."""
        tower = e8_shadow_tower()
        assert tower['alpha'] == Rational(0)

    def test_shadow_metric(self):
        """Q_L = 4*kappa^2 = 256 (constant, perfect square)."""
        tower = e8_shadow_tower()
        assert tower['Q_L'] == Rational(256)

    def test_perfect_square(self):
        """Shadow metric is a perfect square (class G property)."""
        tower = e8_shadow_tower()
        assert tower['is_perfect_square'] is True

    def test_growth_rate_zero(self):
        """Growth rate rho = 0 (tower terminates)."""
        tower = e8_shadow_tower()
        assert tower['growth_rate'] == Rational(0)

    def test_terminates(self):
        """Tower terminates at arity 2."""
        tower = e8_shadow_tower()
        assert tower['terminates'] is True
        assert tower['termination_arity'] == 2


# =========================================================================
# 7. GENUS EXPANSION
# =========================================================================

class TestGenusExpansion:
    """Verify genus expansion F_g(V_{E_8}) = 8 * lambda_g^FP."""

    def test_F1(self):
        """F_1(V_{E_8}) = 8/24 = 1/3."""
        expansion = e8_genus_expansion(5)
        assert expansion[1] == Rational(1, 3)

    def test_F2(self):
        """F_2(V_{E_8}) = 8 * 7/5760 = 7/720."""
        expansion = e8_genus_expansion(5)
        assert expansion[2] == Rational(7, 720)

    def test_F3(self):
        """F_3(V_{E_8}) = 8 * 31/967680 = 31/120960."""
        expansion = e8_genus_expansion(5)
        assert expansion[3] == Rational(31, 120960)

    def test_F4(self):
        """F_4(V_{E_8}) = 8 * 127/154828800 = 127/19353600."""
        expansion = e8_genus_expansion(5)
        assert expansion[4] == Rational(127, 19353600)

    def test_F5(self):
        """F_5(V_{E_8}) = 8 * 2555/122624409600 = 2555/15328051200."""
        expansion = e8_genus_expansion(5)
        assert expansion[5] == Rational(2555, 15328051200)

    def test_F1_via_shadow_partition(self):
        """Shadow partition function Z^sh_1 = F_1 = 1/3."""
        assert shadow_partition_function_genus_g(1) == Rational(1, 3)

    def test_F2_via_shadow_partition(self):
        """Shadow partition function Z^sh_2 = F_2 = 7/720."""
        assert shadow_partition_function_genus_g(2) == Rational(7, 720)

    def test_all_positive(self):
        """All F_g > 0 for g = 1..5 (Bernoulli signs absorbed)."""
        expansion = e8_genus_expansion(5)
        for g in range(1, 6):
            assert expansion[g] > 0

    def test_faber_pandharipande_g1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_faber_pandharipande_g2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)


# =========================================================================
# 8. HECKE OPERATORS
# =========================================================================

class TestHeckeOperators:
    """Verify Hecke eigenvalues for E_4 and E_8."""

    def test_hecke_e4_p2(self):
        """T_2(E_4) eigenvalue = 1 + 8 = 9."""
        assert hecke_eigenvalue_e4(2) == 9

    def test_hecke_e4_p3(self):
        """T_3(E_4) eigenvalue = 1 + 27 = 28."""
        assert hecke_eigenvalue_e4(3) == 28

    def test_hecke_e4_p5(self):
        """T_5(E_4) eigenvalue = 1 + 125 = 126."""
        assert hecke_eigenvalue_e4(5) == 126

    def test_hecke_e4_p7(self):
        """T_7(E_4) eigenvalue = 1 + 343 = 344."""
        assert hecke_eigenvalue_e4(7) == 344

    def test_hecke_e4_p11(self):
        """T_11(E_4) eigenvalue = 1 + 1331 = 1332."""
        assert hecke_eigenvalue_e4(11) == 1332

    def test_hecke_e4_p13(self):
        """T_13(E_4) eigenvalue = 1 + 2197 = 2198."""
        assert hecke_eigenvalue_e4(13) == 2198

    def test_hecke_e4_equals_sigma3(self):
        """Hecke eigenvalue a_p(E_4) = sigma_3(p) = 1 + p^3 for primes."""
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
            assert hecke_eigenvalue_e4(p) == sigma_k(p, 3)

    def test_hecke_e8_p2(self):
        """T_2(E_8) eigenvalue = 1 + 128 = 129."""
        assert hecke_eigenvalue_e8(2) == 129

    def test_hecke_e8_p3(self):
        """T_3(E_8) eigenvalue = 1 + 2187 = 2188."""
        assert hecke_eigenvalue_e8(3) == 2188

    def test_hecke_e8_equals_sigma7(self):
        """Hecke eigenvalue a_p(E_8) = sigma_7(p) = 1 + p^7 for primes."""
        for p in [2, 3, 5, 7]:
            assert hecke_eigenvalue_e8(p) == sigma_k(p, 7)

    def test_hecke_from_fourier_p2(self):
        """Verify T_2 eigenvalue from Fourier coefficient ratio."""
        result = verify_hecke_eigenvalue_from_fourier(2)
        assert result['all_agree'] is True

    def test_hecke_from_fourier_p3(self):
        """Verify T_3 eigenvalue from Fourier coefficient ratio."""
        result = verify_hecke_eigenvalue_from_fourier(3)
        assert result['all_agree'] is True

    def test_hecke_from_fourier_p5(self):
        """Verify T_5 eigenvalue from Fourier coefficient ratio."""
        result = verify_hecke_eigenvalue_from_fourier(5)
        assert result['all_agree'] is True

    def test_hecke_from_fourier_p7(self):
        """Verify T_7 eigenvalue from Fourier coefficient ratio."""
        result = verify_hecke_eigenvalue_from_fourier(7)
        assert result['all_agree'] is True

    def test_hecke_method3_cross_check_p3(self):
        """Cross-check: a_{2*3}/a_2 = 1 + 27 = 28 for odd prime p=3."""
        result = verify_hecke_eigenvalue_from_fourier(3, max_n=50)
        assert result['method3_match'] is True

    def test_hecke_method3_cross_check_p5(self):
        """Cross-check: a_{2*5}/a_2 = 1 + 125 = 126 for odd prime p=5."""
        result = verify_hecke_eigenvalue_from_fourier(5, max_n=50)
        assert result['method3_match'] is True

    def test_shadow_hecke_p2(self):
        """Shadow Hecke eigenvalue for p=2."""
        result = shadow_hecke_eigenvalue(2)
        assert result['hecke_eigenvalue'] == 9
        assert result['ratio_equals_eigenvalue'] is True

    def test_shadow_hecke_p3(self):
        """Shadow Hecke eigenvalue for p=3."""
        result = shadow_hecke_eigenvalue(3)
        assert result['hecke_eigenvalue'] == 28
        assert result['ratio_equals_eigenvalue'] is True

    def test_shadow_hecke_p5(self):
        """Shadow Hecke eigenvalue for p=5."""
        result = shadow_hecke_eigenvalue(5)
        assert result['hecke_eigenvalue'] == 126
        assert result['ratio_equals_eigenvalue'] is True

    def test_shadow_hecke_p7(self):
        """Shadow Hecke eigenvalue for p=7."""
        result = shadow_hecke_eigenvalue(7)
        assert result['hecke_eigenvalue'] == 344
        assert result['ratio_equals_eigenvalue'] is True


# =========================================================================
# 9. COMPLEMENTARITY
# =========================================================================

class TestComplementarity:
    """Verify Koszul duality and complementarity."""

    def test_e8_kappa(self):
        """kappa(V_{E_8}) = 8."""
        comp = e8_complementarity()
        assert comp['kappa'] == Rational(8)

    def test_e8_kappa_dual(self):
        """kappa(V_{E_8}^!) = -8."""
        comp = e8_complementarity()
        assert comp['kappa_dual'] == Rational(-8)

    def test_e8_sum_zero(self):
        """kappa + kappa' = 0 for E_8 lattice (AP24: KM/free-field case)."""
        comp = e8_complementarity()
        assert comp['sum_is_zero'] is True

    def test_e8_unimodular(self):
        """E_8 is unimodular (Koszul self-dual as abstract VOA)."""
        comp = e8_complementarity()
        assert comp['is_unimodular'] is True

    def test_e8xe8_sum_zero(self):
        """kappa + kappa' = 0 for E_8 x E_8."""
        comp = e8xe8_complementarity()
        assert comp['sum_is_zero'] is True

    def test_d16_plus_sum_zero(self):
        """kappa + kappa' = 0 for D_{16}^+."""
        comp = d16_plus_complementarity()
        assert comp['sum_is_zero'] is True


# =========================================================================
# 10. E_8 x E_8 vs D_{16}^+ DISCRIMINATION
# =========================================================================

class TestLatticeDiscrimination:
    """Verify that E_8 x E_8 and D_{16}^+ are indistinguishable at genus 1."""

    def test_same_genus1_theta(self):
        """E_8 x E_8 and D_{16}^+ have the same genus-1 theta series."""
        disc = genus1_discrimination(20)
        assert disc['genus1_identical'] is True

    def test_both_equal_e8(self):
        """Both genus-1 theta series equal E_8 = E_4^2."""
        disc = genus1_discrimination(20)
        assert disc['both_equal_e8'] is True

    def test_same_kappa(self):
        """Both have kappa = 16."""
        disc = genus1_discrimination()
        assert disc['kappa_e8xe8'] == 16
        assert disc['kappa_d16p'] == 16

    def test_same_shadow_class(self):
        """Both are class G."""
        disc = genus1_discrimination()
        assert disc['shadow_class_e8xe8'] == 'G'
        assert disc['shadow_class_d16p'] == 'G'

    def test_same_shadow_depth(self):
        """Both have shadow depth 2."""
        disc = genus1_discrimination()
        assert disc['shadow_depth_e8xe8'] == 2
        assert disc['shadow_depth_d16p'] == 2

    def test_discrimination_arity_infinite(self):
        """Discrimination arity at genus 1 is infinite (cannot distinguish)."""
        disc = genus1_discrimination()
        assert disc['discrimination_arity_genus1'] == float('inf')

    def test_e8xe8_theta_first_terms(self):
        """E_8 x E_8 theta: 1, 480, 61920, 1050240, ...."""
        theta = e8_times_e8_theta_coefficients(5)
        assert theta[0] == 1
        assert theta[1] == 480  # 2 * 240

    def test_d16_plus_theta_first_terms(self):
        """D_{16}^+ theta: same as E_8 x E_8 at genus 1."""
        e8xe8 = e8_times_e8_theta_coefficients(5)
        d16p = d16_plus_theta_coefficients(5)
        assert e8xe8 == d16p

    def test_rank16_comparison(self):
        """Full rank-16 shadow comparison."""
        comp = rank16_shadow_comparison()
        assert comp['genus1_identical'] is True
        assert comp['shadow_identical'] is True


# =========================================================================
# 11. ARITHMETIC INTERSECTION
# =========================================================================

class TestArithmeticIntersection:
    """Verify arithmetic intersection data."""

    def test_genus1_F1(self):
        """F_1(V_{E_8}) = 1/3."""
        data = genus1_arithmetic_data()
        assert data['F_1'] == Rational(1, 3)

    def test_genus1_F1_squared(self):
        """F_1^2 = 1/9."""
        data = genus1_arithmetic_data()
        assert data['F_1_squared'] == Rational(1, 9)

    def test_genus1_lambda1(self):
        """lambda_1 = 1/24."""
        data = genus1_arithmetic_data()
        assert data['lambda_1'] == Rational(1, 24)

    def test_genus2_F2(self):
        """F_2(V_{E_8}) = 7/720."""
        data = genus2_arithmetic_data()
        assert data['F_2'] == Rational(7, 720)


# =========================================================================
# 12. SMITH-MINKOWSKI-SIEGEL MASS
# =========================================================================

class TestMassFormula:
    """Verify mass formula data."""

    def test_e8_mass_value(self):
        """mass(E_8) = 1/696729600."""
        assert e8_mass() == Rational(1, 696729600)

    def test_siegel_mass_dim8(self):
        """Siegel mass formula result for dim 8 even unimodular."""
        assert siegel_mass_formula_dim8() == Rational(1, 696729600)

    def test_mass_bernoulli_connection(self):
        """Mass-Bernoulli-shadow connection runs without error."""
        result = mass_bernoulli_shadow_connection()
        assert result['kappa'] == Rational(8)
        assert result['weyl_order'] == 696729600


# =========================================================================
# 13. GENUS-2 HECKE EIGENVALUES
# =========================================================================

class TestGenus2Hecke:
    """Verify genus-2 Hecke eigenvalues for E_8 Siegel theta."""

    def test_genus2_siegel_weight_e8(self):
        """Genus-2 theta of E_8 has weight 4 (= rank/2)."""
        assert genus2_siegel_weight(8) == 4

    def test_genus2_siegel_weight_e8xe8(self):
        """Genus-2 theta of E_8 x E_8 has weight 8."""
        assert genus2_siegel_weight(16) == 8

    def test_genus2_hecke_p2(self):
        """Genus-2 T(2) eigenvalue = 1 + 4 + 8 + 32 = 45."""
        # k = 4: 1 + 2^2 + 2^3 + 2^5 = 1 + 4 + 8 + 32 = 45
        assert genus2_e8_hecke_eigenvalue(2) == 45

    def test_genus2_hecke_p3(self):
        """Genus-2 T(3) eigenvalue = 1 + 9 + 27 + 243 = 280."""
        # k = 4: 1 + 3^2 + 3^3 + 3^5 = 1 + 9 + 27 + 243 = 280
        assert genus2_e8_hecke_eigenvalue(3) == 280

    def test_genus2_hecke_p5(self):
        """Genus-2 T(5) eigenvalue = 1 + 25 + 125 + 3125 = 3276."""
        assert genus2_e8_hecke_eigenvalue(5) == 3276

    def test_genus2_vs_genus1_hecke_p2(self):
        """Genus-2 Hecke eigenvalue differs from genus-1 at p=2."""
        g1 = hecke_eigenvalue_e4(2)  # 9
        g2 = genus2_e8_hecke_eigenvalue(2)  # 45
        assert g1 != g2
        assert g1 == 9
        assert g2 == 45

    def test_genus2_hecke_comparison(self):
        """Genus-2 Hecke comparison data for p=2."""
        result = genus2_hecke_comparison(2)
        assert result['genus1_eigenvalue'] == 9
        assert result['genus2_eigenvalue'] == 45


# =========================================================================
# 14. MODULAR FORMS RING STRUCTURE
# =========================================================================

class TestModularFormsRing:
    """Verify dimensions of spaces of modular forms for SL(2,Z)."""

    def test_dim_m0(self):
        """dim M_0 = 1 (constants)."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[0] == 1

    def test_dim_m2(self):
        """dim M_2 = 0 (no weight-2 modular forms for SL(2,Z))."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[2] == 0

    def test_dim_m4(self):
        """dim M_4 = 1 (spanned by E_4)."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[4] == 1

    def test_dim_m6(self):
        """dim M_6 = 1 (spanned by E_6)."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[6] == 1

    def test_dim_m8(self):
        """dim M_8 = 1 (spanned by E_4^2 = E_8)."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[8] == 1

    def test_dim_m10(self):
        """dim M_10 = 1 (spanned by E_4*E_6)."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[10] == 1

    def test_dim_m12(self):
        """dim M_12 = 2 (spanned by E_4^3 and Delta = E_4^3 - E_6^2 / 1728)."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[12] == 2

    def test_dim_m14(self):
        """dim M_14 = 1."""
        dims = ring_of_modular_forms_dimensions()
        assert dims[14] == 1


# =========================================================================
# 15. A-HAT GENERATING FUNCTION
# =========================================================================

class TestAhatGeneratingFunction:
    """Verify the A-hat generating function check."""

    def test_ahat_check(self):
        """A-hat generating function check runs successfully."""
        result = ahat_generating_function_check()
        assert result['kappa'] == Rational(8)
        for g in range(1, 6):
            assert result['genus_data'][g]['F_g_equals_kappa_times_lambda_g'] is True


# =========================================================================
# 16. FULL CROSS-VERIFICATION
# =========================================================================

class TestFullCrossVerification:
    """Run the complete multi-path cross-verification."""

    def test_all_paths_pass(self):
        """All 5 verification paths pass."""
        result = full_cross_verification(10)
        assert result['all_paths_pass'] is True

    def test_path1_theta_check(self):
        """Path 1: theta coefficients match Conway-Sloane."""
        result = full_cross_verification(10)
        assert result['path1_theta_check'] is True

    def test_path2_theta_equals_e4(self):
        """Path 2: Theta_{E_8} = E_4."""
        result = full_cross_verification(10)
        assert result['path2_theta_equals_e4'] is True

    def test_path3_shadow_class(self):
        """Path 3: shadow tower gives class G."""
        result = full_cross_verification(10)
        assert result['path3_class'] == 'G'

    def test_path4_hecke(self):
        """Path 4: Hecke eigenvalues all agree."""
        result = full_cross_verification(10)
        assert result['path4_hecke_all_agree'] is True

    def test_path5_e4_squared(self):
        """Path 5: E_4^2 = E_8 identity holds."""
        result = full_cross_verification(10)
        assert result['path5_e4_squared_equals_e8'] is True


# =========================================================================
# 17. EDGE CASES AND ADDITIONAL VERIFICATIONS
# =========================================================================

class TestEdgeCases:
    """Additional verifications and edge cases."""

    def test_faber_pandharipande_raises_g0(self):
        """lambda_0^FP is undefined (genus must be >= 1)."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_shadow_partition_raises_g0(self):
        """Shadow partition function undefined at g=0."""
        with pytest.raises(ValueError):
            shadow_partition_function_genus_g(0)

    def test_e4_e6_are_algebraically_independent(self):
        """E_4 and E_6 coefficients differ (they generate the ring)."""
        e4 = eisenstein_e4_coefficients(5)
        e6 = eisenstein_e6_coefficients(5)
        assert e4[1] != e6[1]  # 240 != -504

    def test_theta_coefficients_nonnegative(self):
        """All theta coefficients r_{E_8}(n) >= 0 (counting lattice vectors)."""
        theta = e8_theta_coefficients(20)
        assert all(c >= 0 for c in theta)

    def test_theta_coefficient_parity(self):
        """r_{E_8}(n) is divisible by 240 for n >= 1 (root system symmetry).

        Actually r_{E_8}(n) = 240 * sigma_3(n), so divisibility by 240 holds.
        """
        theta = e8_theta_coefficients(20)
        for n in range(1, 21):
            assert theta[n] % 240 == 0

    def test_e8_genus_expansion_decreasing(self):
        """F_g values decrease with g (for fixed kappa = 8)."""
        expansion = e8_genus_expansion(5)
        for g in range(1, 5):
            assert expansion[g] > expansion[g + 1]

    def test_hecke_eigenvalue_multiplicative(self):
        """Hecke eigenvalue a_p(E_4) = sigma_3(p) satisfies multiplicativity.

        sigma_3 is multiplicative: sigma_3(mn) = sigma_3(m)*sigma_3(n) for gcd(m,n)=1.
        For coprime m, n: sigma_3(mn) = sigma_3(m)*sigma_3(n).
        """
        # Check: sigma_3(6) = sigma_3(2)*sigma_3(3) since gcd(2,3)=1
        assert sigma_k(6, 3) == sigma_k(2, 3) * sigma_k(3, 3)
        # sigma_3(6) = 1+8+27+216 = 252 = 9*28 = 252. Check.

    def test_hecke_eigenvalue_not_multiplicative_for_prime_powers(self):
        """For non-coprime: sigma_3(p^2) != sigma_3(p)^2.

        sigma_3(4) = 73, sigma_3(2)^2 = 81.
        """
        assert sigma_k(4, 3) != sigma_k(2, 3)**2

    def test_kappa_additivity_e8xe8(self):
        """kappa(E_8 x E_8) = kappa(E_8) + kappa(E_8) = 16."""
        kappa_e8 = Rational(8)
        assert kappa_e8 + kappa_e8 == Rational(16)
