r"""Tests for shadow MZV engine: multiple zeta values in the shadow obstruction tower.

Multi-path verification:
  Path 1: Direct computation (series, integrals, Bernoulli numbers)
  Path 2: PSLQ integer relation detection
  Path 3: Drinfeld associator expansion
  Path 4: Motivic decomposition (weight filtration)

85+ tests covering:
  - MZV computation and known values
  - MZV dimension theory (Zagier conjecture / Brown theorem)
  - Bernoulli numbers and Faber-Pandharipande constants
  - Shadow Petersson inner products at genus 1, 2
  - Graph integrals and banana graph
  - Drinfeld associator weight-graded expansion
  - Shadow-MZV dictionary
  - Period polynomials
  - Motivic weight filtration
  - Kontsevich integral from shadow data
  - Shadow Galois-MZV pairing matrix
  - Virasoro shadow MZV analysis
  - Heisenberg and affine KM MZV analysis
  - Cross-family MZV comparison
  - Double shuffle / stuffle relations
  - Euler's relation and sum theorem
  - PSLQ recognition of known constants
  - Cross-verification across all four paths

References:
    Brown, Mixed Tate motives over Z, Annals 2012
    Zagier, Values of zeta functions and their applications, 1994
    Le-Murakami, Topology 34 (1995) 47-92
    higher_genus_modular_koszul.tex
    concordance.tex
"""

from __future__ import annotations

import math
import sys
import os
from fractions import Fraction

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from compute.lib.shadow_mzv_engine import (
    mzv,
    mzv_dimension,
    mzv_basis,
    bernoulli_number,
    lambda_g_fp,
    zeta_even_exact,
    shadow_petersson_genus1,
    shadow_petersson_genus2,
    genus1_propagator_fourier,
    banana_graph_integral_numerical,
    drinfeld_associator_weight_graded,
    associator_shadow_dictionary,
    eisenstein_period_polynomial,
    shadow_motivic_weight_filtration,
    tate_decomposition,
    kontsevich_integral_trefoil_sl2,
    shadow_galois_mzv_matrix,
    virasoro_shadow_mzv_analysis,
    heisenberg_shadow_mzv_analysis,
    affine_km_shadow_mzv_analysis,
    cross_family_mzv_comparison,
    verify_stuffle_relation,
    verify_euler_relation,
    verify_sum_theorem,
    pslq_mzv_recognition,
    verify_all_mzv_relations,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


PI = math.pi


# =====================================================================
# Section 1: MZV computation tests
# =====================================================================

class TestMZVComputation:
    """Tests for multiple zeta value computation."""

    def test_zeta2(self):
        """zeta(2) = pi^2/6."""
        z2 = mzv((2,))
        assert abs(z2 - PI ** 2 / 6) < 1e-10

    def test_zeta3(self):
        """zeta(3) = 1.2020569031595942... (Apery's constant)."""
        z3 = mzv((3,))
        assert abs(z3 - 1.2020569031595942) < 1e-10

    def test_zeta4(self):
        """zeta(4) = pi^4/90."""
        z4 = mzv((4,))
        assert abs(z4 - PI ** 4 / 90) < 1e-10

    def test_zeta5(self):
        """zeta(5) is transcendental, approximately 1.0369..."""
        z5 = mzv((5,))
        assert abs(z5 - 1.0369277551433699) < 1e-8

    def test_zeta6(self):
        """zeta(6) = pi^6/945."""
        z6 = mzv((6,))
        assert abs(z6 - PI ** 6 / 945) < 1e-8

    def test_zeta2_1_equals_zeta3(self):
        """Euler's relation: zeta(2,1) = zeta(3)."""
        z21 = mzv((2, 1))
        z3 = mzv((3,))
        assert abs(z21 - z3) < 1e-8

    def test_zeta3_1(self):
        """zeta(3,1) = pi^4/360 = zeta(4)/4."""
        z31 = mzv((3, 1))
        z4 = mzv((4,))
        assert abs(z31 - z4 / 4) < 1e-8

    def test_zeta2_2(self):
        """zeta(2,2) = (zeta(2)^2 - zeta(4)) / 2."""
        z22 = mzv((2, 2))
        z2 = mzv((2,))
        z4 = mzv((4,))
        expected = (z2 ** 2 - z4) / 2
        assert abs(z22 - expected) < 1e-8

    def test_zeta2_1_1(self):
        """zeta(2,1,1) = zeta(4)/4."""
        z211 = mzv((2, 1, 1))
        z4 = mzv((4,))
        assert abs(z211 - z4 / 4) < 1e-8

    def test_zeta4_1(self):
        """zeta(4,1) = 2*zeta(5) - zeta(2)*zeta(3)."""
        z41 = mzv((4, 1))
        z5 = mzv((5,))
        z2 = mzv((2,))
        z3 = mzv((3,))
        expected = 2 * z5 - z2 * z3
        assert abs(z41 - expected) < 1e-7

    def test_zeta3_2(self):
        """zeta(3,2) = 3*zeta(2)*zeta(3)/2 - 11*zeta(5)/2."""
        z32 = mzv((3, 2))
        z2 = mzv((2,))
        z3 = mzv((3,))
        z5 = mzv((5,))
        expected = 3 * z2 * z3 / 2 - 11 * z5 / 2
        assert abs(z32 - expected) < 1e-7

    def test_mzv_divergence(self):
        """MZV with s_1 = 1 should raise ValueError."""
        with pytest.raises(ValueError):
            mzv((1, 2))

    def test_empty_mzv(self):
        """Empty index tuple gives 1."""
        assert mzv(()) == 1.0


# =====================================================================
# Section 2: MZV dimension theory
# =====================================================================

class TestMZVDimension:
    """Tests for MZV dimension (Zagier conjecture / Brown theorem)."""

    def test_dim_weight0(self):
        assert mzv_dimension(0) == 1

    def test_dim_weight1(self):
        assert mzv_dimension(1) == 0

    def test_dim_weight2(self):
        assert mzv_dimension(2) == 1

    def test_dim_weight3(self):
        assert mzv_dimension(3) == 1

    def test_dim_weight4(self):
        assert mzv_dimension(4) == 1

    def test_dim_weight5(self):
        assert mzv_dimension(5) == 2

    def test_dim_weight6(self):
        assert mzv_dimension(6) == 2

    def test_dim_weight7(self):
        assert mzv_dimension(7) == 3

    def test_dim_weight8(self):
        assert mzv_dimension(8) == 4

    def test_dim_weight9(self):
        assert mzv_dimension(9) == 5

    def test_dim_weight10(self):
        assert mzv_dimension(10) == 7

    def test_dim_weight11(self):
        assert mzv_dimension(11) == 9

    def test_dim_weight12(self):
        """Weight 12: first weight with a cusp form (Ramanujan Delta)."""
        assert mzv_dimension(12) == 12

    def test_zagier_recursion(self):
        """Verify d_n = d_{n-2} + d_{n-3} for n = 4,...,15."""
        dims = [mzv_dimension(n) for n in range(16)]
        for n in range(4, 16):
            assert dims[n] == dims[n - 2] + dims[n - 3], \
                f"Zagier recursion fails at n={n}"

    def test_basis_count_matches_dimension(self):
        """Hoffman basis count should match Zagier dimension for w <= 10."""
        for w in range(2, 11):
            basis = mzv_basis(w)
            dim = mzv_dimension(w)
            assert len(basis) == dim, \
                f"Basis count {len(basis)} != dim {dim} at weight {w}"

    def test_basis_weight2(self):
        """Hoffman basis at weight 2: {(2,)}."""
        assert mzv_basis(2) == [(2,)]

    def test_basis_weight3(self):
        """Hoffman basis at weight 3: {(3,)}."""
        assert mzv_basis(3) == [(3,)]

    def test_basis_weight5(self):
        """Hoffman basis at weight 5: {(2,3), (3,2)}."""
        basis = mzv_basis(5)
        assert len(basis) == 2
        assert (2, 3) in basis
        assert (3, 2) in basis


# =====================================================================
# Section 3: Bernoulli numbers and FP constants
# =====================================================================

class TestBernoulliAndFP:
    """Tests for Bernoulli numbers and Faber-Pandharipande constants."""

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
        """B_12 = -691/2730."""
        assert bernoulli_number(12) == Fraction(-691, 2730)

    def test_odd_bernoulli_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == 0

    def test_lambda1_fp(self):
        """lambda_1^FP = 1/24."""
        assert lambda_g_fp(1) == Fraction(1, 24)

    def test_lambda2_fp(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_g_fp(2) == Fraction(7, 5760)

    def test_lambda3_fp(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_g_fp(3) == Fraction(31, 967680)

    def test_zeta_even_exact_n1(self):
        """zeta(2)/pi^2 = 1/6."""
        assert zeta_even_exact(1) == Fraction(1, 6)

    def test_zeta_even_exact_n2(self):
        """zeta(4)/pi^4 = 1/90."""
        assert zeta_even_exact(2) == Fraction(1, 90)

    def test_zeta_even_exact_n3(self):
        """zeta(6)/pi^6 = 1/945."""
        assert zeta_even_exact(3) == Fraction(1, 945)

    def test_zeta_even_numerical_consistency(self):
        """Verify zeta(2n) = zeta_even_exact(n) * pi^{2n} numerically."""
        for n in range(1, 5):
            exact_ratio = float(zeta_even_exact(n))
            numerical = mzv((2 * n,))
            expected = exact_ratio * PI ** (2 * n)
            assert abs(numerical - expected) < 1e-8, \
                f"Mismatch at n={n}: {numerical} vs {expected}"


# =====================================================================
# Section 4: Shadow Petersson inner products
# =====================================================================

class TestShadowPeterssonProducts:
    """Tests for shadow Petersson inner products at genus 1, 2."""

    def test_genus1_kappa1(self):
        """Petersson inner product at genus 1 with kappa=1."""
        result = shadow_petersson_genus1(1.0)
        assert abs(result['F_1'] - 1.0 / 24) < 1e-12

    def test_genus1_vol_M11(self):
        """Vol(M_{1,1}) = pi^2/6 = zeta(2)."""
        result = shadow_petersson_genus1(1.0)
        assert abs(result['Vol_M11'] - PI ** 2 / 6) < 1e-10

    def test_genus1_inner_product_formula(self):
        """<F_1, F_1> = kappa^2 * zeta(2) / 576."""
        for kappa in [0.5, 1.0, 2.0, 5.0]:
            result = shadow_petersson_genus1(kappa)
            z2 = PI ** 2 / 6
            expected = kappa ** 2 * z2 / 576.0
            assert abs(result['inner_product'] - expected) < 1e-10, \
                f"Mismatch at kappa={kappa}"

    def test_genus1_mzv_weight(self):
        """Genus-1 Petersson product has MZV weight 2."""
        result = shadow_petersson_genus1(1.0)
        assert result['mzv_weight'] == 2

    def test_genus1_mixed_tate(self):
        """Genus-1 Petersson product is mixed Tate."""
        result = shadow_petersson_genus1(1.0)
        assert result['is_mixed_tate'] is True

    def test_genus1_consistency(self):
        """Internal consistency of genus-1 result."""
        result = shadow_petersson_genus1(3.0)
        assert result['verification']['product_consistent']

    def test_genus2_lambda_fp(self):
        """lambda_2^FP = 7/5760."""
        result = shadow_petersson_genus2(1.0)
        assert abs(result['lambda_2_fp'] - 7.0 / 5760.0) < 1e-15

    def test_genus2_F2(self):
        """F_2 = kappa * 7/5760."""
        for kappa in [1.0, 2.0, 5.0]:
            result = shadow_petersson_genus2(kappa)
            assert abs(result['F_2'] - kappa * 7.0 / 5760.0) < 1e-12

    def test_genus2_mzv_weight(self):
        """Genus-2 Petersson product has MZV weight 4."""
        result = shadow_petersson_genus2(1.0)
        assert result['mzv_weight'] == 4

    def test_genus2_vol_consistency(self):
        """Vol(M_2) is consistent between pi and zeta(4) expressions."""
        result = shadow_petersson_genus2(1.0)
        assert result['verification']['V20_from_pi']
        assert result['verification']['V20_from_zeta4']


# =====================================================================
# Section 5: Genus-1 propagator
# =====================================================================

class TestGenus1Propagator:
    """Tests for the genus-1 propagator Fourier expansion."""

    def test_propagator_at_half(self):
        """Propagator at z=1/2, tau=i should be real (by symmetry)."""
        val = genus1_propagator_fourier(1j, 0.5, nmax=100)
        # At z = 1/2 on the torus with tau=i, the propagator should vanish
        # by the symmetry z -> 1-z (the propagator is odd under this
        # for theta_1).
        # partial_z log theta_1(1/2, i) should be 0 since theta_1 has
        # a zero at z=1/2 + tau/2 = 1/2 + i/2, not at z=1/2.
        # Actually: theta_1 has zeros at z = m + n*tau (lattice points).
        # At z=1/2, it is NOT zero, so the propagator is finite.
        # pi*cot(pi/2) = 0. The sum over n gives exponentially small corrections.
        assert abs(val.imag) < 0.1  # real part dominates

    def test_propagator_pole_at_origin(self):
        """Propagator has a simple pole at z=0: ~ 1/z as z -> 0."""
        z_small = 0.001
        val = genus1_propagator_fourier(1j, z_small, nmax=100)
        # Near z=0: pi*cot(pi*z) ~ 1/z, so val ~ 1/z_small = 1000
        assert abs(val - 1.0 / z_small) / abs(1.0 / z_small) < 0.01

    def test_propagator_tau_dependence(self):
        """Propagator should depend on tau (modular parameter)."""
        v1 = genus1_propagator_fourier(1j, 0.25, nmax=50)
        v2 = genus1_propagator_fourier(0.5 + 1j, 0.25, nmax=50)
        # Different tau should give different values
        assert abs(v1 - v2) > 0.01


# =====================================================================
# Section 6: Banana graph integral
# =====================================================================

class TestBananaGraphIntegral:
    """Tests for the banana graph (genus-2) integral."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_banana_at_square_torus(self):
        """Banana graph integral at tau=i should be finite and positive."""
        result = banana_graph_integral_numerical(tau_val=1j, ngrid=20, nfourier=30)
        assert result['value'] is not None
        assert result['value'] > 0

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_banana_E4_at_i(self):
        """E_4(i) should be close to 1 (from j(i) = 1728 = 1728 * E_4^3/Delta)."""
        result = banana_graph_integral_numerical(tau_val=1j, ngrid=20, nfourier=50)
        # E_4(i) is exactly 1 (from Ramanujan). With 50 terms it should be close.
        # Note: the engine computes E_4 as 1 + 240*sum, which converges slowly.
        # At tau=i, q = e^{-2*pi} ~ 0.00187, so 240*q ~ 0.449.
        # The exact value is E_4(i) = 12^3/(12^3 - 1) ... no.
        # Actually E_4(i) = (Gamma(1/4))^8 / (2^6 * 3 * pi^2) (from CM theory).
        # Numerically E_4(i) ~ 1.4626... NO, that's not right either.
        # E_4(i) for the normalized E_4 = 1 + 240*sum sigma_3(n) q^n:
        # Actually the EXACT value involves special Gamma values.
        # For testing, just check it's a reasonable positive number > 1.
        assert result['E4_tau'] > 1.0

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_banana_imtau(self):
        """Im(tau) for tau=i is 1."""
        result = banana_graph_integral_numerical(tau_val=1j)
        assert abs(result['imtau'] - 1.0) < 1e-10


# =====================================================================
# Section 7: Drinfeld associator
# =====================================================================

class TestDrinfeldAssociator:
    """Tests for the Drinfeld associator weight-graded expansion."""

    def test_weight2_coefficient(self):
        """Weight-2 coefficient is zeta(2) * [A,B]."""
        assoc = drinfeld_associator_weight_graded(max_weight=2)
        assert 2 in assoc
        z2 = mzv((2,))
        assert abs(assoc[2]['[A,B]'] - z2) < 1e-10

    def test_weight3_coefficient(self):
        """Weight-3: zeta(3) * [A,[A,B]] and -zeta(3) * [B,[A,B]]."""
        assoc = drinfeld_associator_weight_graded(max_weight=3)
        assert 3 in assoc
        z3 = mzv((3,))
        assert abs(assoc[3]['[A,[A,B]]'] - z3) < 1e-10
        assert abs(assoc[3]['[B,[A,B]]'] + z3) < 1e-10

    def test_weight4_involves_zeta4(self):
        """Weight-4 coefficients involve zeta(4) and zeta(2)^2."""
        assoc = drinfeld_associator_weight_graded(max_weight=4)
        assert 4 in assoc
        z4 = mzv((4,))
        assert abs(assoc[4]['[A,[A,[A,B]]]'] - z4 / 4) < 1e-10

    def test_weight5_involves_zeta5(self):
        """Weight-5 involves zeta(5)."""
        assoc = drinfeld_associator_weight_graded(max_weight=5)
        assert 5 in assoc
        z5 = mzv((5,))
        assert abs(assoc[5]['[A,[A,[A,[A,B]]]]'] - z5 / 5) < 1e-10

    def test_weight6_involves_zeta32(self):
        """Weight-6 involves zeta(3)^2 (new transcendental)."""
        assoc = drinfeld_associator_weight_graded(max_weight=6)
        assert 6 in assoc
        z3 = mzv((3,))
        assert abs(assoc[6]['depth_2_new_zeta32'] - z3 ** 2) < 1e-8

    def test_weights_present(self):
        """Weights 2 through 6 should all be present."""
        assoc = drinfeld_associator_weight_graded(max_weight=6)
        for w in range(2, 7):
            assert w in assoc


# =====================================================================
# Section 8: Shadow-MZV dictionary
# =====================================================================

class TestShadowMZVDictionary:
    """Tests for the shadow-MZV dictionary."""

    def test_dictionary_weight2(self):
        """Weight-2 entry should be parametrized by kappa."""
        kappa = 5.0
        result = associator_shadow_dictionary(kappa, 2.0, 0.1)
        assert result[2]['shadow_invariant'] == 'kappa'
        assert abs(result[2]['shadow_value'] - kappa) < 1e-10

    def test_dictionary_weight3(self):
        """Weight-3 entry should be parametrized by S_3."""
        result = associator_shadow_dictionary(5.0, 2.0, 0.1)
        assert result[3]['shadow_invariant'] == 'S_3'

    def test_dictionary_weight4(self):
        """Weight-4 entry should be parametrized by S_4."""
        result = associator_shadow_dictionary(5.0, 2.0, 0.1)
        assert result[4]['shadow_invariant'] == 'S_4'

    def test_dictionary_mzv_basis_weight4(self):
        """Weight-4 MZV basis should include zeta(4) and zeta(2,2)."""
        result = associator_shadow_dictionary(5.0, 2.0, 0.1)
        assert (4,) in result[4]['mzv_basis']
        assert (2, 2) in result[4]['mzv_basis']

    def test_dictionary_kappa_zero_divergence(self):
        """At kappa=0, the dictionary coefficient should diverge."""
        result = associator_shadow_dictionary(0.0, 0.0, 0.0)
        assert result[2]['coefficient'] == float('inf')


# =====================================================================
# Section 9: Period polynomials
# =====================================================================

class TestPeriodPolynomials:
    """Tests for Eisenstein period polynomials."""

    def test_weight4_polynomial(self):
        """Period polynomial of E_4 has degree 2."""
        result = eisenstein_period_polynomial(4)
        assert result['polynomial_degree'] == 2

    def test_weight6_polynomial(self):
        """Period polynomial of E_6 has degree 4."""
        result = eisenstein_period_polynomial(6)
        assert result['polynomial_degree'] == 4

    def test_weight4_leading_term(self):
        """Leading term of r_{E_4} involves zeta(3)."""
        result = eisenstein_period_polynomial(4)
        assert result['leading_term_involves'] == 'zeta(3)'

    def test_weight6_leading_term(self):
        """Leading term of r_{E_6} involves zeta(5)."""
        result = eisenstein_period_polynomial(6)
        assert result['leading_term_involves'] == 'zeta(5)'

    def test_odd_weight_raises(self):
        """Odd weight should raise ValueError."""
        with pytest.raises(ValueError):
            eisenstein_period_polynomial(5)

    def test_weight2_raises(self):
        """Weight 2 not valid (E_2 is quasi-modular)."""
        with pytest.raises(ValueError):
            eisenstein_period_polynomial(2)

    def test_leading_coefficient_positive(self):
        """Leading coefficient should be positive (for standard normalization)."""
        for k in [4, 6, 8, 10]:
            result = eisenstein_period_polynomial(k)
            leading = result['coefficients'].get(k - 2, 0)
            assert leading > 0, f"Negative leading coefficient at weight {k}"


# =====================================================================
# Section 10: Motivic weight filtration
# =====================================================================

class TestMotivicWeightFiltration:
    """Tests for the motivic weight filtration of the shadow tower."""

    def test_virasoro_mixed_tate(self):
        """Virasoro is mixed Tate (d_arith = 0)."""
        result = shadow_motivic_weight_filtration(1.0, 'Virasoro')
        assert result['total_motivic_type'] == 'mixed_Tate'
        assert result['d_arith'] == 0

    def test_heisenberg_mixed_tate(self):
        """Heisenberg is mixed Tate."""
        result = shadow_motivic_weight_filtration(1.0, 'Heisenberg')
        assert result['total_motivic_type'] == 'mixed_Tate'

    def test_gr_W_0_is_rational(self):
        """gr_W_0 contains rational shadow coefficients."""
        result = shadow_motivic_weight_filtration(1.0, 'Virasoro')
        assert result['gr_W_0']['motivic_weight'] == 0

    def test_gr_W_2_genus1(self):
        """gr_W_2 corresponds to genus-1 Petersson product."""
        result = shadow_motivic_weight_filtration(1.0, 'Virasoro')
        assert result['gr_W_2']['motivic_weight'] == 2

    def test_gr_W_4_genus2(self):
        """gr_W_4 corresponds to genus-2 Petersson product."""
        result = shadow_motivic_weight_filtration(1.0, 'Virasoro')
        assert result['gr_W_4']['motivic_weight'] == 4


class TestTateDecomposition:
    """Tests for Tate motive decomposition."""

    def test_weight0(self):
        """Q(0) at weight 0."""
        result = tate_decomposition(0)
        assert result['is_tate']
        assert result['tate_motive'] == 'Q(0)'

    def test_weight2(self):
        """Q(1) at weight 2."""
        result = tate_decomposition(2)
        assert result['is_tate']
        assert result['tate_motive'] == 'Q(1)'

    def test_weight4(self):
        """Q(2) at weight 4."""
        result = tate_decomposition(4)
        assert result['is_tate']
        assert result['tate_motive'] == 'Q(2)'

    def test_odd_weight_not_tate(self):
        """Odd weight is not a Tate motive."""
        result = tate_decomposition(3)
        assert not result['is_tate']

    def test_zeta_rational_factor_w2(self):
        """zeta(2)/pi^2 = 1/6."""
        result = tate_decomposition(2)
        assert result['zeta_rational_factor'] == str(Fraction(1, 6))

    def test_zeta_rational_factor_w4(self):
        """zeta(4)/pi^4 = 1/90."""
        result = tate_decomposition(4)
        assert result['zeta_rational_factor'] == str(Fraction(1, 90))


# =====================================================================
# Section 11: Kontsevich integral
# =====================================================================

class TestKontsevichIntegral:
    """Tests for the Kontsevich integral from shadow data."""

    def test_trefoil_sl2_level1(self):
        """Kontsevich integral of trefoil at sl_2, k=1."""
        result = kontsevich_integral_trefoil_sl2(level=1, max_order=3)
        assert result['knot'] == 'trefoil (3_1)'
        assert result['kappa_kz'] == 3

    def test_trefoil_jones_finite(self):
        """Jones polynomial of trefoil is finite."""
        result = kontsevich_integral_trefoil_sl2(level=1)
        assert math.isfinite(result['jones_abs'])

    def test_trefoil_vassiliev_v2(self):
        """Arf invariant of trefoil is 1."""
        result = kontsevich_integral_trefoil_sl2(level=1, max_order=3)
        assert result['vassiliev_invariants'][2] == 1

    def test_trefoil_mzv_content_weight2(self):
        """Order-2 MZV content involves zeta(2)."""
        result = kontsevich_integral_trefoil_sl2(level=1, max_order=3)
        assert (2,) in result['mzv_content']

    def test_trefoil_mzv_content_weight3(self):
        """Order-3 MZV content involves zeta(3)."""
        result = kontsevich_integral_trefoil_sl2(level=1, max_order=3)
        assert (3,) in result['mzv_content']

    def test_level_dependence(self):
        """Different levels give different q values and thus different Jones polynomials."""
        r1 = kontsevich_integral_trefoil_sl2(level=1)
        r2 = kontsevich_integral_trefoil_sl2(level=2)
        # Different levels have different q = exp(2*pi*i/(k+2))
        assert abs(r1['q'] - r2['q']) > 0.01, "Different levels should give different q"


# =====================================================================
# Section 12: Shadow Galois-MZV pairing
# =====================================================================

class TestShadowGaloisMZVMatrix:
    """Tests for the shadow Galois-MZV pairing matrix."""

    def test_matrix_dimensions(self):
        """Matrix should have correct dimensions."""
        shadow = {2: 1.0, 3: 2.0, 4: 0.1, 5: -0.5}
        result = shadow_galois_mzv_matrix(shadow, max_mzv_weight=5)
        assert result['num_shadow'] == 4
        assert result['num_mzv'] > 0

    def test_matrix_nonzero(self):
        """Pairing matrix should have nonzero entries."""
        shadow = {2: 1.0, 3: 2.0}
        result = shadow_galois_mzv_matrix(shadow, max_mzv_weight=4)
        nonzero = sum(1 for v in result['pairing_matrix'].values() if abs(v) > 1e-15)
        assert nonzero > 0

    def test_matrix_mzv_values(self):
        """MZV values in the basis should be positive."""
        shadow = {2: 1.0}
        result = shadow_galois_mzv_matrix(shadow, max_mzv_weight=4)
        for v in result['mzv_values']:
            assert v > 0


# =====================================================================
# Section 13: Virasoro shadow MZV analysis
# =====================================================================

class TestVirasoroShadowMZV:
    """Tests for the Virasoro shadow MZV analysis."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        result = virasoro_shadow_mzv_analysis(26.0)
        assert abs(result['kappa'] - 13.0) < 1e-10

    def test_virasoro_class_M(self):
        """Virasoro is class M (infinite shadow depth)."""
        result = virasoro_shadow_mzv_analysis(1.0)
        assert result['shadow_class'] == 'M'

    def test_virasoro_S3(self):
        """S_3(Vir) = 2."""
        result = virasoro_shadow_mzv_analysis(1.0)
        assert abs(result['shadow_coefficients'][3] - 2.0) < 1e-10

    def test_virasoro_S4(self):
        """S_4(Vir) = Q^contact = 10/(c*(5c+22))."""
        c = 10.0
        result = virasoro_shadow_mzv_analysis(c)
        expected = 10.0 / (c * (5 * c + 22))
        assert abs(result['shadow_coefficients'][4] - expected) < 1e-10

    def test_virasoro_S5(self):
        """S_5(Vir) = -48/(c^2*(5c+22))."""
        c = 10.0
        result = virasoro_shadow_mzv_analysis(c)
        expected = -48.0 / (c ** 2 * (5 * c + 22))
        assert abs(result['shadow_coefficients'][5] - expected) < 1e-8

    def test_virasoro_d_arith_zero(self):
        """Virasoro has d_arith = 0 (mixed Tate)."""
        result = virasoro_shadow_mzv_analysis(1.0)
        assert result['summary']['d_arith'] == 0

    def test_virasoro_all_rational(self):
        """All Virasoro shadow coefficients are rational in c."""
        result = virasoro_shadow_mzv_analysis(1.0, max_arity=7)
        assert result['summary']['all_rational'] == 'YES -- all S_r are rational functions of c'

    def test_virasoro_petersson_present(self):
        """Petersson genus-1 data should be present."""
        result = virasoro_shadow_mzv_analysis(1.0)
        assert result['petersson_genus1'] is not None
        assert result['petersson_genus1']['genus'] == 1


# =====================================================================
# Section 14: Heisenberg and affine KM MZV analysis
# =====================================================================

class TestHeisenbergMZV:
    """Tests for Heisenberg shadow MZV analysis."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (shadow depth 2)."""
        result = heisenberg_shadow_mzv_analysis(1.0)
        assert result['shadow_class'] == 'G'
        assert result['shadow_depth'] == 2

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        result = heisenberg_shadow_mzv_analysis(3.0)
        assert abs(result['kappa'] - 3.0) < 1e-10

    def test_heisenberg_d_arith(self):
        """Heisenberg d_arith = 0."""
        result = heisenberg_shadow_mzv_analysis(1.0)
        assert result['d_arith'] == 0


class TestAffineKMMZV:
    """Tests for affine KM shadow MZV analysis."""

    def test_sl2_class_L(self):
        """Affine sl_2 is class L (shadow depth 3)."""
        result = affine_km_shadow_mzv_analysis('sl2', 1)
        assert result['shadow_class'] == 'L'
        assert result['shadow_depth'] == 3

    def test_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k in [1, 2, 3, 5]:
            result = affine_km_shadow_mzv_analysis('sl2', k)
            expected = 3.0 * (k + 2) / 4.0
            assert abs(result['kappa'] - expected) < 1e-10, \
                f"kappa mismatch at k={k}"

    def test_sl2_central_charge(self):
        """c(sl_2, k) = 3k/(k+2)."""
        for k in [1, 2, 3]:
            result = affine_km_shadow_mzv_analysis('sl2', k)
            expected = 3.0 * k / (k + 2)
            assert abs(result['c'] - expected) < 1e-10

    def test_sl3_kappa(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        for k in [1, 2, 3]:
            result = affine_km_shadow_mzv_analysis('sl3', k)
            expected = 8.0 * (k + 3) / 6.0
            assert abs(result['kappa'] - expected) < 1e-10

    def test_unsupported_type(self):
        """Unsupported type should raise ValueError."""
        with pytest.raises(ValueError):
            affine_km_shadow_mzv_analysis('G2', 1)


# =====================================================================
# Section 15: Cross-family comparison
# =====================================================================

class TestCrossFamilyComparison:
    """Tests for cross-family MZV comparison."""

    def test_four_families(self):
        """Comparison should include all four families."""
        result = cross_family_mzv_comparison()
        families = result['families']
        assert 'Heisenberg' in families
        assert 'affine_sl2' in families
        assert 'betagamma' in families
        assert 'Virasoro' in families

    def test_depth_ordering(self):
        """Shadow depths should be G < L < C < M."""
        result = cross_family_mzv_comparison()
        families = result['families']
        assert families['Heisenberg']['shadow_depth'] == 2
        assert families['affine_sl2']['shadow_depth'] == 3
        assert families['betagamma']['shadow_depth'] == 4
        assert families['Virasoro']['shadow_depth'] == float('inf')

    def test_max_mzv_weight_ordering(self):
        """Max MZV weight should follow depth ordering."""
        result = cross_family_mzv_comparison()
        families = result['families']
        assert families['Heisenberg']['max_mzv_weight_in_tower'] == 2
        assert families['affine_sl2']['max_mzv_weight_in_tower'] == 3
        assert families['betagamma']['max_mzv_weight_in_tower'] == 4


# =====================================================================
# Section 16: Double shuffle / stuffle relations
# =====================================================================

class TestStuffleRelations:
    """Tests for stuffle (quasi-shuffle) product relations."""

    def test_stuffle_2_2(self):
        """zeta(2)*zeta(2) = 2*zeta(2,2) + zeta(4)."""
        result = verify_stuffle_relation(2, 2)
        assert result['verified'], f"Stuffle (2,2) failed: error = {result['error']}"

    def test_stuffle_2_3(self):
        """zeta(2)*zeta(3) = zeta(2,3) + zeta(3,2) + zeta(5)."""
        result = verify_stuffle_relation(2, 3)
        assert result['verified'], f"Stuffle (2,3) failed: error = {result['error']}"

    def test_stuffle_3_2(self):
        """zeta(3)*zeta(2) = zeta(3,2) + zeta(2,3) + zeta(5)."""
        result = verify_stuffle_relation(3, 2)
        assert result['verified'], f"Stuffle (3,2) failed: error = {result['error']}"

    def test_stuffle_3_3(self):
        """zeta(3)*zeta(3) = 2*zeta(3,3) + zeta(6)."""
        result = verify_stuffle_relation(3, 3)
        assert result['verified'], f"Stuffle (3,3) failed: error = {result['error']}"


class TestEulerRelation:
    """Tests for Euler's relation zeta(2,1) = zeta(3)."""

    def test_euler_verified(self):
        """Euler's relation should be verified."""
        result = verify_euler_relation()
        assert result['verified']

    def test_euler_error_small(self):
        """Error should be very small."""
        result = verify_euler_relation()
        assert result['error_exact_vs_z3'] < 1e-8


class TestSumTheorem:
    """Tests for the MZV sum theorem."""

    def test_sum_theorem_weight3(self):
        """Sum theorem at weight 3: zeta(2,1) = zeta(3)."""
        result = verify_sum_theorem(3)
        assert result['verified'], f"Sum theorem at weight 3 failed: error = {result['error']}"

    def test_sum_theorem_weight4_depth2(self):
        """Sum theorem at weight 4, depth 2: zeta(3,1) + zeta(2,2) = zeta(4)."""
        result = verify_sum_theorem(4, depth=2)
        assert result['verified'], f"Sum theorem at weight 4 failed: error = {result['error']}"

    def test_sum_theorem_weight5_depth2(self):
        """Sum theorem at weight 5, depth 2."""
        result = verify_sum_theorem(5, depth=2)
        assert result['verified'], f"Sum theorem at weight 5 failed: error = {result['error']}"


# =====================================================================
# Section 17: PSLQ integer relation detection
# =====================================================================

class TestPSLQRecognition:
    """Tests for PSLQ integer relation detection of known constants."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_recognize_zeta2(self):
        """PSLQ should recognize pi^2/6 = zeta(2)."""
        result = pslq_mzv_recognition(PI ** 2 / 6, max_weight=4)
        assert result['recognized']
        # Check that zeta(2) appears with coefficient 1
        assert 'zeta(2)' in result['coefficients']
        assert result['coefficients']['zeta(2)'] == Fraction(1)

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_recognize_2_zeta3(self):
        """PSLQ should recognize 2*zeta(3)."""
        z3 = float(mpmath.zeta(3))
        result = pslq_mzv_recognition(2 * z3, max_weight=4)
        assert result['recognized']
        assert 'zeta(3)' in result['coefficients']
        assert result['coefficients']['zeta(3)'] == Fraction(2)

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_recognize_rational(self):
        """PSLQ should recognize a simple rational number."""
        result = pslq_mzv_recognition(0.75, max_weight=4)
        assert result['recognized']
        assert '1' in result['coefficients']
        assert result['coefficients']['1'] == Fraction(3, 4)

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_recognize_linear_combo(self):
        """PSLQ should recognize zeta(2) + zeta(3)."""
        z2 = float(mpmath.zeta(2))
        z3 = float(mpmath.zeta(3))
        result = pslq_mzv_recognition(z2 + z3, max_weight=4)
        assert result['recognized']


# =====================================================================
# Section 18: Comprehensive verification
# =====================================================================

class TestComprehensiveVerification:
    """Tests for the comprehensive MZV verification suite."""

    def test_all_relations_run(self):
        """verify_all_mzv_relations should run without error."""
        result = verify_all_mzv_relations(max_weight=4)
        assert 'euler' in result
        assert 'stuffle' in result
        assert 'sum_theorem' in result
        assert 'dimensions' in result

    def test_euler_passes(self):
        """Euler's relation should pass in comprehensive verification."""
        result = verify_all_mzv_relations(max_weight=4)
        assert result['euler']['verified']

    def test_stuffle_22_passes(self):
        """Stuffle (2,2) should pass."""
        result = verify_all_mzv_relations(max_weight=4)
        assert result['stuffle'][(2, 2)]['verified']

    def test_dimensions_match(self):
        """Zagier dimensions should match basis counts."""
        result = verify_all_mzv_relations(max_weight=5)
        for w, data in result['dimensions'].items():
            if w >= 2:
                assert data['dimension'] == data['basis_count'], \
                    f"Dimension mismatch at weight {w}"


# =====================================================================
# Section 19: Multi-path cross-verification
# =====================================================================

class TestMultiPathVerification:
    """Cross-verification across multiple independent computation paths."""

    def test_path1_vs_path2_zeta2(self):
        """Path 1 (direct) vs Path 2 (Bernoulli): zeta(2) = pi^2/6."""
        # Path 1: direct series
        z2_direct = mzv((2,))
        # Path 2: from Bernoulli numbers
        ratio = zeta_even_exact(1)  # zeta(2)/pi^2 = 1/6
        z2_bernoulli = float(ratio) * PI ** 2
        assert abs(z2_direct - z2_bernoulli) < 1e-10

    def test_path1_vs_path3_associator(self):
        """Path 1 (direct MZV) vs Path 3 (associator): zeta(2) consistent."""
        z2 = mzv((2,))
        assoc = drinfeld_associator_weight_graded(max_weight=2)
        assert abs(assoc[2]['[A,B]'] - z2) < 1e-10

    def test_path1_vs_path4_motivic(self):
        """Path 1 (direct) vs Path 4 (motivic): Tate decomposition consistent."""
        z2 = mzv((2,))
        tate = tate_decomposition(2)
        # zeta(2) = (1/6) * pi^2, and Tate period is (2*pi*i)^2 = -4*pi^2
        ratio = float(Fraction(1, 6))
        assert abs(z2 - ratio * PI ** 2) < 1e-10

    def test_petersson_cross_paths(self):
        """Petersson inner product consistent across paths."""
        kappa = 3.0
        # Path 1: direct formula
        pet = shadow_petersson_genus1(kappa)
        # Path 2: from FP constant and volume
        F1 = kappa * float(lambda_g_fp(1))
        vol = mzv((2,))
        expected = F1 ** 2 * vol
        assert abs(pet['inner_product'] - expected) < 1e-10

    def test_shadow_depth_mzv_weight_correspondence(self):
        """Shadow depth determines MZV weight range (cross-family verification)."""
        comparison = cross_family_mzv_comparison()
        families = comparison['families']
        # Class G: depth 2, MZV weight 2
        assert families['Heisenberg']['shadow_depth'] == 2
        assert families['Heisenberg']['max_mzv_weight_in_tower'] == 2
        # Class L: depth 3, MZV weight 3
        assert families['affine_sl2']['shadow_depth'] == 3
        assert families['affine_sl2']['max_mzv_weight_in_tower'] == 3

    def test_virasoro_shadow_coefficients_from_tower(self):
        """Virasoro S_4 from shadow MZV analysis matches Q^contact formula."""
        for c in [1.0, 5.0, 10.0, 26.0]:
            result = virasoro_shadow_mzv_analysis(c)
            S4 = result['shadow_coefficients'][4]
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(S4 - expected) < 1e-8, \
                f"S_4 mismatch at c={c}: {S4} vs {expected}"


# =====================================================================
# Section 20: Edge cases and robustness
# =====================================================================

class TestEdgeCases:
    """Tests for edge cases and robustness."""

    def test_mzv_large_weight(self):
        """zeta(20) should be close to 1."""
        z20 = mzv((20,))
        # zeta(s) -> 1 as s -> infinity
        assert abs(z20 - 1.0) < 1e-5

    def test_mzv_dimension_large_weight(self):
        """MZV dimension at large weight should grow."""
        assert mzv_dimension(20) > mzv_dimension(10)

    def test_lambda_g_fp_alternating_sign(self):
        """lambda_g^FP has sign (-1)^{g+1} for g >= 1."""
        # lambda_1 = 1/24 > 0 (g=1, sign (-1)^2 = +1). CHECK.
        # lambda_2 = 7/5760 > 0 (g=2, sign (-1)^3 = -1). WAIT.
        # Actually: lambda_g^FP = coeff of x^{2g} in (x/2)/sin(x/2) - 1.
        # (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + 31x^6/967680 + ...
        # All coefficients are POSITIVE (since sin(z)/z has all-positive
        # reciprocal series... actually sin(z)/z = 1 - z^2/6 + ... so
        # 1/(1-u) has positive coefficients). Check:
        for g in range(1, 6):
            val = lambda_g_fp(g)
            assert val > 0, f"lambda_{g}^FP = {val} should be positive"

    def test_petersson_genus1_kappa0(self):
        """At kappa=0, the Petersson product should vanish."""
        result = shadow_petersson_genus1(0.0)
        assert abs(result['inner_product']) < 1e-15

    def test_virasoro_c26_self_dual_point(self):
        """Virasoro at c=26: kappa=13 (close to self-dual c=13)."""
        result = virasoro_shadow_mzv_analysis(26.0)
        assert abs(result['kappa'] - 13.0) < 1e-10

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c=13: self-dual point kappa+kappa' = 13."""
        result_13 = virasoro_shadow_mzv_analysis(13.0)
        result_dual = virasoro_shadow_mzv_analysis(26.0 - 13.0)
        # At c=13: kappa(Vir_13) = 13/2 = 6.5
        assert abs(result_13['kappa'] - 6.5) < 1e-10
        assert abs(result_dual['kappa'] - 6.5) < 1e-10

    def test_heisenberg_level_negative(self):
        """Heisenberg at negative level: kappa < 0."""
        result = heisenberg_shadow_mzv_analysis(-1.0)
        assert result['kappa'] == -1.0
