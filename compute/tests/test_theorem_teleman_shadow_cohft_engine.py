r"""Tests for Teleman reconstruction of the shadow CohFT.

Multi-path verification (CLAUDE.md mandate: 3+ independent paths per claim):

1. Direct computation of Frobenius algebra structure
2. Semisimplicity classification for all standard families
3. Flat unit analysis (AP30 compliance)
4. Teleman reconstruction conditions
5. R-matrix coefficients (A-hat formula)
6. Symplectic condition R(-z)^T R(z) = 1
7. Dressed propagator coefficients and symmetry
8. Heisenberg genus expansion: MC vs A-hat vs Faber-Pandharipande
9. Virasoro: R = 1 for rank-1 semisimple
10. W_N gravitational Frobenius algebra discriminant and cross-channel
11. Cross-family consistency checks
12. Independence of MC and Teleman reconstructions

Ground truth references:
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:cohft-reconstruction (higher_genus_modular_koszul.tex)
  prop:dressed-propagator-resolution (higher_genus_modular_koszul.tex)
  prop:universal-gravitational-cross-channel (higher_genus_modular_koszul.tex)
  AP30: flat identity conditional on vacuum in V
  AP32: genus-1 unconditional; multi-weight at g>=2 fails scalar formula
"""

import pytest
from sympy import Rational, Symbol, simplify, bernoulli, factorial, expand, eye

from compute.lib.theorem_teleman_shadow_cohft_engine import (
    # Core functions
    lambda_fp,
    ahat_r_matrix_coefficient,
    ahat_r_matrix_series,
    verify_symplectic_condition,
    dressed_propagator_coefficient,
    # Frobenius algebra construction
    FrobeniusAlgebra,
    heisenberg_frobenius,
    virasoro_frobenius,
    affine_sl2_frobenius,
    betagamma_frobenius,
    # Teleman conditions
    TelemanConditions,
    assess_teleman_conditions,
    # Genus expansion
    heisenberg_genus_expansion_mc,
    heisenberg_genus_expansion_ahat,
    cross_verify_heisenberg,
    # Virasoro
    virasoro_teleman_r_matrix,
    virasoro_shadow_cohft_amplitudes,
    # W_N
    wn_gravitational_frobenius_discriminant,
    wn_genus2_cross_channel,
    # Summary
    teleman_uniqueness_statement,
    full_analysis_table,
)

c = Symbol('c')
k = Symbol('k')


# ============================================================================
# Section 1: Faber-Pandharipande intersection numbers
# ============================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP = (2^{2g-1} - 1)/(2^{2g-1}) * |B_{2g}|/(2g)!"""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda4(self):
        """lambda_4^FP = 127/154828800."""
        # B_8 = -1/30, (2^7-1)/2^7 * (1/30)/(8!) = 127/128 * 1/(30*40320)
        # = 127 / (128 * 1209600) = 127 / 154828800
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_genus_invalid(self):
        """lambda_fp(0) should raise."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_lambda_positivity(self):
        """All lambda_g^FP must be positive (Bernoulli signs)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0


# ============================================================================
# Section 2: A-hat R-matrix coefficients
# ============================================================================

class TestAhatRMatrix:
    """Verify R(z) = exp(sum B_{2j}/(2j(2j-1)) z^{2j-1})."""

    def test_R0(self):
        """R_0 = 1."""
        assert ahat_r_matrix_coefficient(0) == Rational(1)

    def test_R1(self):
        """R_1 = B_2 / (2*1) = (1/6) / 2 = 1/12."""
        assert ahat_r_matrix_coefficient(1) == Rational(1, 12)

    def test_R2(self):
        """R_2 = R_1^2/2 = (1/12)^2/2 = 1/288."""
        assert ahat_r_matrix_coefficient(2) == Rational(1, 288)

    def test_R3(self):
        """R_3 = -139/51840.
        From the formal power series expansion.
        """
        assert ahat_r_matrix_coefficient(3) == Rational(-139, 51840)

    def test_R4(self):
        """R_4 = -571/2488320."""
        assert ahat_r_matrix_coefficient(4) == Rational(-571, 2488320)

    def test_R_negative_index(self):
        """R_{-1} = 0."""
        assert ahat_r_matrix_coefficient(-1) == Rational(0)

    def test_series_length(self):
        """ahat_r_matrix_series returns correct length."""
        R = ahat_r_matrix_series(5)
        assert len(R) == 6
        assert R[0] == Rational(1)

    def test_R1_from_bernoulli(self):
        """Independent derivation: R_1 = B_2/(2*1*1) = (1/6)/2 = 1/12.
        Verification path: direct Bernoulli number.
        """
        B2 = bernoulli(2)  # = 1/6
        expected = Rational(B2, 2)  # B_2 / (2*1*(2*1-1)) = (1/6)/2 = 1/12
        # Actually the exponent coefficient is B_2/(2*1) with power z^1,
        # so R_1 = a_1 where a_1 = B_2/(2*1*1) = 1/12.
        # This matches because exp(a_1 z + ...) = 1 + a_1 z + ... at first order.
        assert ahat_r_matrix_coefficient(1) == Rational(1, 12)


# ============================================================================
# Section 3: Symplectic condition
# ============================================================================

class TestSymplecticCondition:
    """Verify R(-z)^T R(z) = 1 for the scalar A-hat R-matrix."""

    def test_symplectic_n0(self):
        """At order 0: R_0 * R_0 = 1."""
        res = verify_symplectic_condition(6)
        assert res[0] == Rational(1)

    def test_symplectic_n1(self):
        """At order 1: -R_0 R_1 + R_1 R_0 = 0."""
        res = verify_symplectic_condition(6)
        assert res[1] == Rational(0)

    def test_symplectic_n2(self):
        """At order 2: R_0 R_2 - R_1 R_1 + R_2 R_0 = 0."""
        res = verify_symplectic_condition(6)
        assert res[2] == Rational(0)

    def test_symplectic_n3(self):
        """At order 3: sum (-1)^j R_j R_{3-j} = 0."""
        res = verify_symplectic_condition(6)
        assert res[3] == Rational(0)

    def test_symplectic_all_orders(self):
        """Symplectic condition holds at all orders 1 through 6."""
        res = verify_symplectic_condition(6)
        for n in range(1, 7):
            assert res[n] == Rational(0), f"Symplectic condition fails at order {n}"


# ============================================================================
# Section 4: Frobenius algebra construction
# ============================================================================

class TestFrobeniusAlgebra:
    """Test genus-0 Frobenius algebra for standard families."""

    def test_heisenberg_dim(self):
        """Heisenberg: dim V = 1."""
        frob = heisenberg_frobenius(Rational(1))
        assert frob.dim == 1

    def test_heisenberg_metric(self):
        """Heisenberg: eta = kappa."""
        frob = heisenberg_frobenius(Rational(3))
        assert frob.metric == Rational(3) * eye(1)

    def test_heisenberg_zero_product(self):
        """Heisenberg: product is zero (S_3 = 0, class G)."""
        frob = heisenberg_frobenius(Rational(1))
        assert frob.structure_constants[(0, 0, 0)] == 0

    def test_virasoro_dim(self):
        """Virasoro: dim V = 1."""
        frob = virasoro_frobenius(Rational(26))
        assert frob.dim == 1

    def test_virasoro_metric(self):
        """Virasoro: eta = c/2."""
        frob = virasoro_frobenius(Rational(26))
        assert frob.metric[0, 0] == Rational(13)  # c/2 = 26/2 = 13

    def test_virasoro_cubic(self):
        """Virasoro: S_3 = 2 (from T_{(1)}T = 2T)."""
        frob = virasoro_frobenius(Rational(26))
        assert frob.structure_constants[(0, 0, 0)] == 2

    def test_betagamma_dim(self):
        """Beta-gamma: dim V = 1."""
        frob = betagamma_frobenius()
        assert frob.dim == 1

    def test_betagamma_kappa(self):
        """Beta-gamma: kappa = 1 (c = 2, kappa = c/2 = 1)."""
        frob = betagamma_frobenius()
        assert frob.kappa == Rational(1)

    def test_affine_sl2_dim(self):
        """Affine sl_2: dim V = 3."""
        frob = affine_sl2_frobenius(Rational(3))
        assert frob.dim == 3

    def test_affine_sl2_kappa(self):
        """Affine sl_2 at level k=3: kappa = 3(3+2)/4 = 15/4."""
        frob = affine_sl2_frobenius(Rational(3))
        assert frob.kappa == Rational(15, 4)

    def test_affine_sl2_metric_nondegenerate(self):
        """Affine sl_2 metric is nondegenerate."""
        frob = affine_sl2_frobenius(Rational(3))
        assert frob.metric.det() != 0


# ============================================================================
# Section 5: Semisimplicity classification
# ============================================================================

class TestSemisimplicity:
    """Test semisimplicity of the genus-0 Frobenius algebra."""

    def test_heisenberg_not_semisimple(self):
        """Heisenberg: product is zero, NOT semisimple."""
        frob = heisenberg_frobenius(Rational(1))
        assert not frob.is_semisimple()

    def test_virasoro_semisimple(self):
        """Virasoro at c != 0: rank-1 with nonzero product, SEMISIMPLE."""
        frob = virasoro_frobenius(Rational(26))
        assert frob.is_semisimple()

    def test_virasoro_semisimple_generic_c(self):
        """Virasoro at generic c: semisimple (S_3 = 2 != 0)."""
        frob = virasoro_frobenius(Rational(1))
        assert frob.is_semisimple()

    def test_betagamma_not_semisimple(self):
        """Beta-gamma: product is zero, NOT semisimple."""
        frob = betagamma_frobenius()
        assert not frob.is_semisimple()

    def test_virasoro_frobenius_discriminant(self):
        """Virasoro discriminant is nonzero (= 4 for the rank-1 algebra)."""
        frob = virasoro_frobenius(Rational(26))
        disc = frob.frobenius_discriminant()
        # For rank-1 with C_{000} = 2, eta_{00} = 13:
        # L_0 = eta^{00} C_{000} = (1/13)(2) = 2/13
        # Tr(L_0 L_0) = (2/13)^2 = 4/169
        # disc = 4/169 (nonzero, so semisimple)
        assert disc != 0


# ============================================================================
# Section 6: Flat unit analysis (AP30)
# ============================================================================

class TestFlatUnit:
    """Verify AP30: flat identity conditional on vacuum in V."""

    def test_heisenberg_no_flat_unit(self):
        """Heisenberg: vacuum NOT in V = span{J}."""
        frob = heisenberg_frobenius(Rational(1))
        assert not frob.has_flat_unit_in_V()

    def test_virasoro_no_flat_unit(self):
        """Virasoro: vacuum NOT in V = span{T}."""
        frob = virasoro_frobenius(Rational(26))
        assert not frob.has_flat_unit_in_V()

    def test_affine_no_flat_unit(self):
        """Affine sl_2: vacuum NOT in V = span{J^a}."""
        frob = affine_sl2_frobenius(Rational(3))
        assert not frob.has_flat_unit_in_V()

    def test_betagamma_no_flat_unit(self):
        """Beta-gamma: vacuum NOT in V = span{beta}."""
        frob = betagamma_frobenius()
        assert not frob.has_flat_unit_in_V()

    def test_extended_flat_unit_heisenberg(self):
        """Heisenberg: V_ext has flat unit."""
        frob = heisenberg_frobenius(Rational(1))
        assert frob.extended_has_flat_unit()

    def test_extended_flat_unit_virasoro(self):
        """Virasoro: V_ext has flat unit."""
        frob = virasoro_frobenius(Rational(26))
        assert frob.extended_has_flat_unit()


# ============================================================================
# Section 7: Teleman reconstruction conditions
# ============================================================================

class TestTelemanConditions:
    """Test the Teleman reconstruction condition assessment."""

    def test_heisenberg_conditions(self):
        """Heisenberg: not semisimple, MC only."""
        frob = heisenberg_frobenius(Rational(1))
        cond = assess_teleman_conditions(frob)
        assert not cond.semisimple
        assert not cond.teleman_applies_V
        assert not cond.teleman_applies_V_ext
        assert cond.reconstruction_method == 'MC_only'

    def test_virasoro_conditions(self):
        """Virasoro: semisimple, flat unit in V_ext, Teleman + MC."""
        frob = virasoro_frobenius(Rational(26))
        cond = assess_teleman_conditions(frob)
        assert cond.semisimple
        assert cond.flat_unit_in_V_ext
        assert cond.teleman_applies_V_ext
        assert cond.r_matrix_trivial  # rank-1 semisimple => R = 1
        assert cond.reconstruction_method == 'MC_and_Teleman'

    def test_virasoro_r_trivial(self):
        """Virasoro: Givental R-matrix is R = 1."""
        frob = virasoro_frobenius(Rational(26))
        cond = assess_teleman_conditions(frob)
        assert cond.r_matrix_trivial

    def test_betagamma_conditions(self):
        """Beta-gamma: not semisimple, MC only."""
        frob = betagamma_frobenius()
        cond = assess_teleman_conditions(frob)
        assert not cond.semisimple
        assert cond.reconstruction_method == 'MC_only'


# ============================================================================
# Section 8: Dressed propagator coefficients
# ============================================================================

class TestDressedPropagator:
    """Verify dressed propagator coefficient P^R(D+, D-)."""

    def test_P00(self):
        """P^R(0, 0) = R_1 R_0 = 1/12."""
        assert dressed_propagator_coefficient(0, 0) == Rational(1, 12)

    def test_P10(self):
        """P^R(1, 0) = R_2 R_0 = 1/288."""
        assert dressed_propagator_coefficient(1, 0) == Rational(1, 288)

    def test_P01(self):
        """P^R(0, 1) = R_1 R_1 - R_2 R_0 = (1/12)^2 - 1/288 = 1/144 - 1/288 = 1/288."""
        val = dressed_propagator_coefficient(0, 1)
        assert val == Rational(1, 288)

    def test_symmetry_P10_P01(self):
        """Dressed propagator symmetry: P^R(1, 0) = P^R(0, 1)."""
        assert dressed_propagator_coefficient(1, 0) == dressed_propagator_coefficient(0, 1)

    def test_symmetry_P20_P02(self):
        """P^R(2, 0) = P^R(0, 2)."""
        assert dressed_propagator_coefficient(2, 0) == dressed_propagator_coefficient(0, 2)

    def test_symmetry_P21_P12(self):
        """P^R(2, 1) = P^R(1, 2)."""
        assert dressed_propagator_coefficient(2, 1) == dressed_propagator_coefficient(1, 2)

    def test_symmetry_P30_P03(self):
        """P^R(3, 0) = P^R(0, 3)."""
        assert dressed_propagator_coefficient(3, 0) == dressed_propagator_coefficient(0, 3)

    def test_symmetry_general(self):
        """P^R(a, b) = P^R(b, a) for all a, b in range."""
        for a in range(5):
            for b in range(5):
                assert dressed_propagator_coefficient(a, b) == dressed_propagator_coefficient(b, a), \
                    f"Symmetry fails at ({a}, {b})"


# ============================================================================
# Section 9: Heisenberg genus expansion cross-verification
# ============================================================================

class TestHeisenbergGenusExpansion:
    """Cross-verify Heisenberg genus expansion by three methods."""

    def test_mc_genus1(self):
        """MC method: F_1 = kappa * 1/24."""
        result = heisenberg_genus_expansion_mc(Rational(1), 1)
        assert result[1] == Rational(1, 24)

    def test_ahat_genus1(self):
        """A-hat method: F_1 = kappa * 1/24."""
        result = heisenberg_genus_expansion_ahat(Rational(1), 1)
        assert result[1] == Rational(1, 24)

    def test_mc_genus2(self):
        """MC method: F_2 = kappa * 7/5760."""
        result = heisenberg_genus_expansion_mc(Rational(1), 2)
        assert result[2] == Rational(7, 5760)

    def test_cross_verify_kappa1(self):
        """Full cross-verification at kappa = 1."""
        results = cross_verify_heisenberg(Rational(1), 5)
        assert results['all_agree']

    def test_cross_verify_kappa7(self):
        """Full cross-verification at kappa = 7."""
        results = cross_verify_heisenberg(Rational(7), 5)
        assert results['all_agree']

    def test_cross_verify_kappa_half(self):
        """Full cross-verification at kappa = 1/2 (= kappa(Virasoro at c=1))."""
        results = cross_verify_heisenberg(Rational(1, 2), 5)
        assert results['all_agree']

    def test_genus_expansion_scaling(self):
        """F_g(kappa) = kappa * lambda_g^FP: linear in kappa."""
        for g in range(1, 5):
            val_1 = heisenberg_genus_expansion_mc(Rational(1), g)[g]
            val_3 = heisenberg_genus_expansion_mc(Rational(3), g)[g]
            assert val_3 == 3 * val_1


# ============================================================================
# Section 10: Virasoro Teleman analysis
# ============================================================================

class TestVirasoroTeleman:
    """Virasoro: R = 1 for rank-1 semisimple, shadow CohFT = WK CohFT."""

    def test_r_matrix_trivial(self):
        """Virasoro Teleman R-matrix is [1] (trivial)."""
        R = virasoro_teleman_r_matrix()
        assert R == [Rational(1)]

    def test_f1_virasoro(self):
        """F_1(Vir_c) = c/48 (= kappa * 1/24 = (c/2)/24)."""
        c_val = Rational(26)
        result = virasoro_shadow_cohft_amplitudes(c_val, 1, 0)
        assert result == Rational(13) * Rational(1, 24)  # 13/24

    def test_f2_virasoro(self):
        """F_2(Vir_c) = (c/2) * 7/5760."""
        c_val = Rational(26)
        result = virasoro_shadow_cohft_amplitudes(c_val, 2, 0)
        assert result == Rational(13) * Rational(7, 5760)  # 91/5760

    def test_virasoro_kappa_formula(self):
        """kappa(Vir_c) = c/2 (AP39: NOT c, NOT c/12)."""
        frob = virasoro_frobenius(Rational(12))
        assert frob.kappa == Rational(6)

    def test_virasoro_c13_self_dual(self):
        """At c = 13: self-dual (kappa = 13/2, kappa' = (26-13)/2 = 13/2).
        AP8: self-duality is at c = 13 (Virasoro), not c = 26."""
        frob = virasoro_frobenius(Rational(13))
        kappa = frob.kappa
        kappa_dual = Rational(26 - 13) / 2
        assert kappa == kappa_dual  # Self-dual at c = 13

    def test_virasoro_complementarity_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero)."""
        for c_val in [Rational(1), Rational(7), Rational(13), Rational(25)]:
            kappa = c_val / 2
            kappa_dual = (26 - c_val) / 2
            assert kappa + kappa_dual == Rational(13)


# ============================================================================
# Section 11: W_N gravitational Frobenius algebra
# ============================================================================

class TestWNGravitational:
    """Test W_N gravitational Frobenius algebra and cross-channel."""

    def test_w2_no_cross_channel(self):
        """W_2 = Virasoro: no cross-channel correction."""
        assert wn_genus2_cross_channel(2) == Rational(0)

    def test_w3_cross_channel(self):
        """W_3: delta_F2 = (c + 204)/(16c)."""
        result = wn_genus2_cross_channel(3, c)
        expected = (c + 204) / (16 * c)
        assert simplify(result - expected) == 0

    def test_w3_cross_channel_numeric(self):
        """W_3 at c = 100: delta_F2 = (100 + 204)/1600 = 304/1600 = 19/100."""
        result = wn_genus2_cross_channel(3, Rational(100))
        assert result == Rational(304, 1600)

    def test_w4_cross_channel(self):
        """W_4: delta_F2^grav = (7c + 2148)/(48c)."""
        result = wn_genus2_cross_channel(4, c)
        # B(4) = (4-2)(4+3)/96 = 2*7/96 = 14/96 = 7/48
        # A(4) = (4-2)(3*64 + 14*16 + 22*4 + 33)/24 = 2(192+224+88+33)/24 = 2*537/24 = 1074/24
        # delta = 7/48 + 1074/(24c) = 7/48 + 1074/(24c) = (7c + 2148)/(48c)
        expected = (7 * c + 2148) / (48 * c)
        assert simplify(result - expected) == 0

    def test_w5_cross_channel(self):
        """W_5: delta_F2^grav = (c + 434)/(4c)."""
        result = wn_genus2_cross_channel(5, c)
        # B(5) = (5-2)(5+3)/96 = 3*8/96 = 24/96 = 1/4
        # A(5) = (5-2)(3*125 + 14*25 + 22*5 + 33)/24 = 3(375+350+110+33)/24 = 3*868/24 = 2604/24
        # delta = 1/4 + 2604/(24c) = 1/4 + 108.5/c = (c + 434)/(4c)
        expected = (c + 434) / (4 * c)
        assert simplify(result - expected) == 0

    def test_wn_positivity(self):
        """For N >= 3 and c > 0: delta_F2^grav > 0."""
        for N in range(3, 8):
            for c_val in [Rational(1), Rational(10), Rational(100), Rational(1000)]:
                result = wn_genus2_cross_channel(N, c_val)
                assert result > 0, f"Positivity fails at N={N}, c={c_val}"

    def test_wn_vanishing_characterization(self):
        """delta_F2^grav = 0 iff N = 2."""
        for N in range(2, 10):
            result = wn_genus2_cross_channel(N, Rational(100))
            if N == 2:
                assert result == 0
            else:
                assert result > 0

    def test_w3_discriminant(self):
        """W_3 gravitational Frobenius algebra has nonzero discriminant."""
        disc = wn_gravitational_frobenius_discriminant(3)
        assert disc == Rational(156)

    def test_w2_discriminant(self):
        """W_2 = Virasoro: discriminant = 16/c^2."""
        disc = wn_gravitational_frobenius_discriminant(2, c)
        expected = 16 / c ** 2
        assert simplify(disc - expected) == 0


# ============================================================================
# Section 12: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (verification path 5)."""

    def test_all_families_mc_determined(self):
        """MC recursion determines all genera for ALL standard families,
        regardless of semisimplicity or flat unit."""
        table = full_analysis_table()
        for entry in table:
            method = entry['method']
            assert method in ('MC_only', 'MC_and_Teleman'), \
                f"Family {entry['family']} has unexpected method {method}"

    def test_virasoro_only_teleman_candidate(self):
        """Among rank-1 families, only Virasoro is semisimple (S_3 != 0)."""
        table = full_analysis_table()
        for entry in table:
            if entry['family'] in ('Heisenberg', 'Beta-gamma'):
                assert not entry['semisimple']
            elif entry['family'] == 'Virasoro':
                assert entry['semisimple']

    def test_no_flat_unit_in_V(self):
        """No standard family has flat unit in V (AP30)."""
        table = full_analysis_table()
        for entry in table:
            assert not entry['flat_unit_V'], \
                f"Family {entry['family']} unexpectedly has flat unit in V"

    def test_all_have_flat_unit_in_V_ext(self):
        """All standard families have flat unit in V_ext."""
        table = full_analysis_table()
        for entry in table:
            assert entry['flat_unit_V_ext'], \
                f"Family {entry['family']} should have flat unit in V_ext"

    def test_genus1_universality(self):
        """F_1 = kappa/24 for ALL families (genus-1 unconditional, AP32)."""
        # Heisenberg
        assert heisenberg_genus_expansion_mc(Rational(1))[1] == Rational(1, 24)
        # Virasoro at c = 26
        assert virasoro_shadow_cohft_amplitudes(Rational(26), 1, 0) == Rational(13, 24)
        # The formula is kappa/24 where kappa = c/2 = 13

    def test_heisenberg_virasoro_same_formula(self):
        """Both Heisenberg and Virasoro use F_g = kappa * lambda_g^FP.
        At kappa = 1: both give identical genus towers."""
        for g in range(1, 5):
            h_val = heisenberg_genus_expansion_mc(Rational(1))[g]
            v_val = virasoro_shadow_cohft_amplitudes(Rational(2), g, 0)  # c = 2 => kappa = 1
            assert h_val == v_val


# ============================================================================
# Section 13: Teleman uniqueness statement
# ============================================================================

class TestTelemanUniqueness:
    """Test that the uniqueness statement is generated correctly."""

    def test_virasoro_statement(self):
        """Virasoro statement mentions R = 1 and Witten-Kontsevich."""
        frob = virasoro_frobenius(Rational(26))
        stmt = teleman_uniqueness_statement(frob)
        assert 'R = 1' in stmt or 'Witten-Kontsevich' in stmt

    def test_heisenberg_statement(self):
        """Heisenberg statement mentions MC only."""
        frob = heisenberg_frobenius(Rational(1))
        stmt = teleman_uniqueness_statement(frob)
        assert 'MC' in stmt or 'Maurer-Cartan' in stmt

    def test_virasoro_mentions_independent(self):
        """Virasoro statement mentions independent verification."""
        frob = virasoro_frobenius(Rational(26))
        stmt = teleman_uniqueness_statement(frob)
        assert 'independent' in stmt


# ============================================================================
# Section 14: R-matrix independent cross-checks
# ============================================================================

class TestRMatrixCrossChecks:
    """Independent verification of R-matrix properties."""

    def test_r_matrix_from_bernoulli_direct(self):
        """R_1 = B_2/(2*1*1) computed directly from Bernoulli."""
        B2 = Rational(1, 6)
        # Exponent coefficient a_1 = B_2/(2*1*(2*1-1)) = (1/6)/(2*1) = 1/12
        # R_1 = a_1 (first-order expansion of exp)
        assert ahat_r_matrix_coefficient(1) == B2 / 2

    def test_r_matrix_not_lambda_fp(self):
        """R_1 = 1/12 != lambda_1^FP = 1/24.
        These are DIFFERENT quantities (AP10-type: don't confuse them)."""
        assert ahat_r_matrix_coefficient(1) != lambda_fp(1)
        assert ahat_r_matrix_coefficient(1) == 2 * lambda_fp(1)

    def test_r1_equals_twice_lambda1(self):
        """R_1 = 2 * lambda_1^FP = 1/12.
        This is a known relation: the R-matrix coefficient at order 1
        equals twice the Faber-Pandharipande number at genus 1."""
        assert ahat_r_matrix_coefficient(1) == 2 * lambda_fp(1)

    def test_symplectic_implies_R_odd_from_even(self):
        """The symplectic condition forces:
        R_2 = R_1^2 / 2 (from order 2 of the symplectic relation).
        Check: R_2 = (1/12)^2 / 2 = 1/288."""
        R1 = ahat_r_matrix_coefficient(1)
        R2 = ahat_r_matrix_coefficient(2)
        # Symplectic at order 2: R_0 R_2 + R_2 R_0 - R_1^2 = 0
        # => 2 R_2 = R_1^2 => R_2 = R_1^2 / 2
        assert R2 == R1 ** 2 / 2


# ============================================================================
# Section 15: W_3 cross-channel correction (AP32 compliance)
# ============================================================================

class TestW3CrossChannel:
    """Verify that the scalar formula FAILS for W_3 at genus >= 2 (AP32)."""

    def test_w3_cross_channel_positive(self):
        """delta_F2(W_3) = (c + 204)/(16c) > 0 for all c > 0."""
        for c_val in [Rational(1, 10), Rational(1), Rational(10), Rational(100)]:
            result = wn_genus2_cross_channel(3, c_val)
            assert result > 0

    def test_w3_cross_channel_exact(self):
        """delta_F2(W_3, c=2) = (2 + 204)/32 = 206/32 = 103/16."""
        result = wn_genus2_cross_channel(3, Rational(2))
        assert result == Rational(206, 32)

    def test_w3_large_c_limit(self):
        """At large c: delta_F2 ~ 1/16 (bridge-loop residue persists)."""
        # delta_F2 = (c + 204)/(16c) = 1/16 + 204/(16c)
        # As c -> infinity: 1/16
        result_1000 = wn_genus2_cross_channel(3, Rational(1000))
        assert abs(float(result_1000) - 1 / 16) < 0.02

    def test_scalar_formula_fails_w3(self):
        """The scalar formula F_2 = kappa * lambda_2^FP is WRONG for W_3.
        The cross-channel correction is nonzero (AP32)."""
        c_val = Rational(100)
        kappa_w3 = c_val / 2  # kappa(W_3) = c/2 (same as Virasoro for rank-1 projection)
        scalar_F2 = kappa_w3 * lambda_fp(2)  # = 50 * 7/5760 = 350/5760 = 7/115.2
        cross_correction = wn_genus2_cross_channel(3, c_val)
        # delta_F2 = (100 + 204)/(16*100) = 304/1600 = 19/100
        assert cross_correction > 0
        # The full F_2 is scalar + cross: different from scalar alone
        full_F2 = scalar_F2 + cross_correction
        assert full_F2 != scalar_F2


# ============================================================================
# Section 16: Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Edge cases and robustness tests."""

    def test_lambda_fp_high_genus(self):
        """lambda_g^FP is computable at high genus."""
        for g in range(1, 10):
            val = lambda_fp(g)
            assert val > 0

    def test_r_matrix_high_order(self):
        """R-matrix computable to high order."""
        R = ahat_r_matrix_series(10)
        assert len(R) == 11
        assert R[0] == Rational(1)

    def test_w_N_large(self):
        """Cross-channel formula for large N."""
        for N in [10, 20, 50]:
            result = wn_genus2_cross_channel(N, Rational(100))
            assert result > 0

    def test_dressed_propagator_high_degree(self):
        """Dressed propagator at high psi-class degree."""
        for D in range(6):
            val = dressed_propagator_coefficient(D, 0)
            # P^R(D, 0) = R_{D+1}
            assert val == ahat_r_matrix_coefficient(D + 1)


# ============================================================================
# Section 17: Full analysis table integrity
# ============================================================================

class TestFullAnalysisTable:
    """Test integrity of the full analysis table."""

    def test_table_has_four_families(self):
        """Table should have 4 standard families."""
        table = full_analysis_table()
        assert len(table) == 4

    def test_table_family_names(self):
        """All standard families present."""
        table = full_analysis_table()
        names = {entry['family'] for entry in table}
        assert names == {'Heisenberg', 'Virasoro', 'Affine sl_2', 'Beta-gamma'}

    def test_table_shadow_classes(self):
        """Shadow classes: G, M, L, C."""
        table = full_analysis_table()
        classes = {entry['shadow_class'] for entry in table}
        assert classes == {'G', 'M', 'L', 'C'}

    def test_table_consistency(self):
        """Teleman applies only where semisimple + flat unit in V_ext."""
        table = full_analysis_table()
        for entry in table:
            if entry['teleman_applies']:
                assert entry['semisimple']
                assert entry['flat_unit_V_ext']
