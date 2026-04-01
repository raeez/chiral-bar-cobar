"""Tests for the N=2 SCA shadow tower via FREE-FIELD REALIZATION.

Adversarial to the direct OPE approach: the free-field realization
decomposes kappa as a sum of constituent contributions from sl(2)_k,
free fermions, and U(1). Any disagreement with the direct OPE
computation exposes an error in the naive Zamolodchikov sum.

Key finding: kappa(N=2) = (6-c)/(2(3-c)), NOT 7c/6.
The naive Zamolodchikov metric sum 7c/6 is WRONG because kappa(sl(2)_k)
= 3(k+2)/4, not the Zamolodchikov sum 3k/2.

Structure: 67 tests organized as:
  1-5.   Central charge (5 tests)
  6-12.  Coset kappa decomposition (7 tests)
  13-19. Kappa formula verification (7 tests)
  20-26. Adversarial: correct vs naive kappa (7 tests)
  27-35. Koszul duality: ADDITIVE c+c'=6 (9 tests)
  36-41. Complementarity kappa+kappa'=1 (6 tests)
  42-44. Critical central charge (3 tests)
  45-52. Shadow tower T-line (8 tests)
  53-56. Shadow tower J-line and class (4 tests)
  57-60. Genus expansion (4 tests)
  61-64. OPE consistency (4 tests)
  65-67. Full verification suite (3 tests)

Manuscript references:
    thm:modular-characteristic, thm:mc2-bar-intrinsic, thm:shadow-radius,
    AP19, AP20, AP27
"""

import math
import pytest
from sympy import Rational, Symbol, simplify, sqrt, N as Neval, oo

from compute.lib.n2_free_field_shadow import (
    # Constituents
    kappa_sl2,
    kappa_fermion_pair,
    kappa_u1_denominator,
    # Central charge
    n2_central_charge,
    k_from_c,
    # Kappa
    kappa_n2_from_k,
    kappa_n2,
    sigma_n2,
    # Coset decomposition
    coset_kappa_decomposition,
    # Adversarial
    naive_zamolodchikov_kappa,
    kappa_discrepancy,
    # Koszul duality
    n2_ff_dual_level,
    n2_ff_dual_central_charge,
    n2_complementarity_sum,
    n2_self_dual_analysis,
    # Critical
    n2_critical_central_charge,
    n2_special_values,
    # Per-channel
    n2_per_channel_kappa,
    # Shadow data
    n2_shadow_data_T_line,
    n2_shadow_data_J_line,
    n2_shadow_data_G_line,
    # Shadow towers
    n2_shadow_tower_T_line,
    n2_shadow_tower_J_line,
    n2_full_shadow_coefficients,
    # Growth rate
    n2_shadow_growth_rate_T_line,
    # Genus expansion
    n2_F_g,
    n2_genus_table,
    # OPE
    n2_nth_products,
    n2_nth_product,
    n2_curvature,
    n2_bar_diff_deg2,
    # Cross-channels
    n2_cross_channel_curvatures,
    # Shadow class
    n2_shadow_class,
    # Jacobi
    verify_n2_jacobi_TJG,
    verify_n2_jacobi_JGG,
    verify_n2_jacobi_GGT,
    # Full verification
    verify_all,
)

c = Symbol('c')


# ================================================================
# 1. CENTRAL CHARGE (5 tests)
# ================================================================

class TestCentralCharge:
    """Test c = 3k/(k+2)."""

    def test_c_at_k1(self):
        assert n2_central_charge(1) == Rational(1)

    def test_c_at_k2(self):
        assert n2_central_charge(2) == Rational(3, 2)

    def test_c_at_k3(self):
        assert n2_central_charge(3) == Rational(9, 5)

    def test_k_from_c_inverse(self):
        """k_from_c is the inverse of n2_central_charge."""
        for k_val in [1, 2, 3, 5, 10]:
            c_val = n2_central_charge(k_val)
            k_back = k_from_c(c_val)
            assert simplify(k_back - Rational(k_val)) == 0

    def test_c_large_k(self):
        c_large = n2_central_charge(10000)
        assert abs(float(c_large) - 3.0) < 0.001


# ================================================================
# 2. COSET KAPPA DECOMPOSITION (7 tests)
# ================================================================

class TestCosetDecomposition:
    """Verify kappa = kappa(sl_2) + kappa(fermion) - kappa(U(1))."""

    def test_kappa_sl2_at_k1(self):
        """kappa(sl(2)_1) = 3*3/4 = 9/4."""
        assert kappa_sl2(1) == Rational(9, 4)

    def test_kappa_sl2_at_k2(self):
        """kappa(sl(2)_2) = 3*4/4 = 3."""
        assert kappa_sl2(2) == Rational(3)

    def test_kappa_fermion_pair(self):
        """kappa(complex fermion) = 1/2."""
        assert kappa_fermion_pair() == Rational(1, 2)

    def test_kappa_u1_at_k1(self):
        """kappa(U(1) at k=1) = 1/2 + 1 = 3/2."""
        assert kappa_u1_denominator(1) == Rational(3, 2)

    def test_coset_at_k1(self):
        """At k=1: kappa = 9/4 + 1/2 - 3/2 = 5/4."""
        dec = coset_kappa_decomposition(1)
        assert dec['kappa_sum'] == Rational(5, 4)
        assert dec['consistent_k']
        assert dec['consistent_c']

    def test_coset_at_k2(self):
        """At k=2: kappa = 3 + 1/2 - 2 = 3/2."""
        dec = coset_kappa_decomposition(2)
        assert dec['kappa_sum'] == Rational(3, 2)
        assert dec['consistent_k']

    def test_coset_at_k3(self):
        """At k=3: kappa = 15/4 + 1/2 - 5/2 = 7/4."""
        dec = coset_kappa_decomposition(3)
        assert dec['kappa_sum'] == Rational(7, 4)
        assert dec['consistent_k']


# ================================================================
# 3. KAPPA FORMULA VERIFICATION (7 tests)
# ================================================================

class TestKappaFormula:
    """Verify kappa(N=2, c) = (6-c)/(2(3-c))."""

    def test_kappa_symbolic(self):
        """kappa = (6-c)/(2(3-c)) symbolically."""
        expected = (6 - c) / (2 * (3 - c))
        assert simplify(kappa_n2() - expected) == 0

    def test_kappa_from_k_at_k1(self):
        """kappa(k=1) = 5/4."""
        assert kappa_n2_from_k(1) == Rational(5, 4)

    def test_kappa_from_c_at_c1(self):
        """kappa(c=1) = 5/4."""
        assert kappa_n2(1) == Rational(5, 4)

    def test_kappa_from_c_at_c3_2(self):
        """kappa(c=3/2) = 3/2."""
        assert kappa_n2(Rational(3, 2)) == Rational(3, 2)

    def test_kappa_k_and_c_agree(self):
        """kappa_from_k and kappa_from_c agree at all test levels."""
        for k_val in [1, 2, 3, 5, 10]:
            c_val = n2_central_charge(k_val)
            assert simplify(
                kappa_n2_from_k(k_val) - kappa_n2(c_val)
            ) == 0

    def test_kappa_at_c0(self):
        """kappa(c=0) = 6/(2*3) = 1."""
        assert kappa_n2(0) == Rational(1)

    def test_sigma_not_constant(self):
        """sigma = kappa/c is NOT constant (unlike W-algebras)."""
        s1 = sigma_n2(1)
        s2 = sigma_n2(Rational(3, 2))
        assert s1 != s2, "sigma should vary with c for a coset"


# ================================================================
# 4. ADVERSARIAL: CORRECT VS NAIVE KAPPA (7 tests)
# ================================================================

class TestAdversarialKappa:
    """Verify that kappa != 7c/6 (the naive Zamolodchikov sum is wrong)."""

    def test_naive_kappa_wrong_at_c1(self):
        """7*1/6 = 7/6 != 5/4 = correct kappa at c=1."""
        naive = naive_zamolodchikov_kappa(1)
        correct = kappa_n2(1)
        assert naive == Rational(7, 6)
        assert correct == Rational(5, 4)
        assert naive != correct

    def test_naive_kappa_wrong_at_c3_2(self):
        """7*3/12 = 7/4 != 3/2 = correct kappa at c=3/2."""
        naive = naive_zamolodchikov_kappa(Rational(3, 2))
        correct = kappa_n2(Rational(3, 2))
        assert naive == Rational(7, 4)
        assert correct == Rational(3, 2)
        assert naive != correct

    def test_discrepancy_nonzero(self):
        """Discrepancy is nonzero for all c != 0."""
        for c_val in [1, 2, Rational(3, 2), Rational(9, 5)]:
            d = kappa_discrepancy(c_val)
            assert d['discrepancy'] != 0

    def test_discrepancy_sign_varies(self):
        """The sign of (correct - naive) varies with c.

        At c=1: correct = 5/4 > naive = 7/6 (naive underestimates).
        At c=2: correct = 2 < naive = 7/3 (naive overestimates).
        The crossover is at c where (6-c)/(2(3-c)) = 7c/6.
        """
        d1 = kappa_discrepancy(1)
        d2 = kappa_discrepancy(2)
        assert d1['kappa_correct'] > d1['kappa_naive']  # c=1: correct > naive
        assert d2['kappa_correct'] < d2['kappa_naive']  # c=2: correct < naive

    def test_relative_error_at_c1(self):
        """Relative error at c=1: |5/4 - 7/6| / (5/4) = 1/15 ~ 6.7%."""
        d = kappa_discrepancy(1)
        expected = Rational(5, 4) - Rational(7, 6)
        assert d['discrepancy'] == expected

    def test_discrepancy_diverges_near_c3(self):
        """Near c=3, correct kappa -> infinity but naive stays finite.

        The relative error diverges. At c=2.99: correct = 3.01/0.02
        = 150.5, naive = 7*2.99/6 ~ 3.49. So correct >> naive.
        """
        d = kappa_discrepancy(Rational(299, 100))  # c = 2.99
        correct = float(d['kappa_correct'])
        naive = float(d['kappa_naive'])
        assert correct > 10 * naive

    def test_discrepancy_formula(self):
        """Discrepancy = (6-c)/(2(3-c)) - 7c/6 = (3c^2-22c+18)/(6(3-c)) ... check.

        Actually: (6-c)/(2(3-c)) - 7c/6.
        Common denominator 6(3-c):
        = 3(6-c)/(6(3-c)) - 7c(3-c)/(6(3-c))
        = (18-3c-21c+7c^2)/(6(3-c))
        = (7c^2-24c+18)/(6(3-c))
        """
        d = kappa_discrepancy(1)
        # At c=1: (7-24+18)/(6*2) = 1/12
        assert d['discrepancy'] == Rational(1, 12)


# ================================================================
# 5. KOSZUL DUALITY: ADDITIVE c + c' = 6 (9 tests)
# ================================================================

class TestKoszulDuality:
    """Test Koszul duality: c + c' = 6 (ADDITIVE, not multiplicative)."""

    def test_ff_dual_level(self):
        """k' = -k - 4."""
        assert n2_ff_dual_level(1) == Rational(-5)
        assert n2_ff_dual_level(2) == Rational(-6)

    def test_c_sum_at_k1(self):
        """At k=1: c=1, c'=5. c+c'=6."""
        ff = n2_ff_dual_central_charge(k_val=1)
        assert ff['c'] == Rational(1)
        assert ff['c_dual'] == Rational(5)
        assert ff['c_sum'] == Rational(6)

    def test_c_sum_at_k2(self):
        """At k=2: c=3/2, c'=9/2. c+c'=6."""
        ff = n2_ff_dual_central_charge(k_val=2)
        assert ff['c'] == Rational(3, 2)
        assert ff['c_dual'] == Rational(9, 2)
        assert ff['c_sum'] == Rational(6)

    def test_c_sum_at_k3(self):
        """At k=3: c=9/5, c'=21/5. c+c'=6."""
        ff = n2_ff_dual_central_charge(k_val=3)
        assert ff['c_sum'] == Rational(6)

    def test_additive_complementarity(self):
        """c + c' = 6 for all k."""
        for k_val in [1, 2, 3, 5, 10]:
            ff = n2_ff_dual_central_charge(k_val=k_val)
            assert simplify(ff['c_sum'] - 6) == 0

    def test_additive_from_c(self):
        """c + c' = 6 when starting from c."""
        for c_val in [1, 2, Rational(3, 2), Rational(9, 5)]:
            ff = n2_ff_dual_central_charge(c_val=c_val)
            assert simplify(ff['c_sum'] - 6) == 0

    def test_involution(self):
        """FF involution is an involution: (c')' = c."""
        ff1 = n2_ff_dual_central_charge(c_val=1)
        ff2 = n2_ff_dual_central_charge(c_val=ff1['c_dual'])
        assert ff2['c_dual'] == Rational(1)

    def test_not_multiplicative(self):
        """c * c' = c(6-c) is NOT constant (varies with c)."""
        p1 = Rational(1) * (6 - Rational(1))  # c=1: 5
        p2 = Rational(2) * (6 - Rational(2))  # c=2: 8
        assert p1 != p2

    def test_self_dual_at_c3(self):
        """Self-dual point c = c' iff c = 3 (k -> infinity)."""
        sd = n2_self_dual_analysis()
        assert sd['c_self_dual'] == Rational(3)
        assert sd['is_finite'] is False


# ================================================================
# 6. COMPLEMENTARITY kappa + kappa' = 1 (6 tests)
# ================================================================

class TestComplementarity:
    """Test kappa + kappa' = 1 (constant, Theorem D)."""

    def test_kappa_sum_at_k1(self):
        """kappa(k=1) + kappa(k'=-5) = 5/4 + (-1/4) = 1."""
        comp = n2_complementarity_sum(k_val=1)
        assert comp['sum'] == Rational(1)

    def test_kappa_sum_at_k2(self):
        """kappa(k=2) + kappa(k'=-6) = 3/2 + (-1/2) = 1."""
        comp = n2_complementarity_sum(k_val=2)
        assert comp['sum'] == Rational(1)

    def test_kappa_sum_at_k3(self):
        comp = n2_complementarity_sum(k_val=3)
        assert comp['sum'] == Rational(1)

    def test_kappa_sum_from_c(self):
        """kappa(c) + kappa(6-c) = 1 for various c."""
        for c_val in [1, 2, Rational(3, 2), Rational(9, 5)]:
            comp = n2_complementarity_sum(c_val=c_val)
            assert comp['sum'] == Rational(1)

    def test_kappa_sum_at_c6(self):
        """kappa(6) + kappa(0) = 0 + 1 = 1."""
        comp = n2_complementarity_sum(c_val=6)
        assert comp['sum'] == Rational(1)

    def test_kappa_sum_symbolic(self):
        """Symbolic: kappa + kappa' = 1."""
        comp = n2_complementarity_sum()
        assert comp['sum'] == Rational(1)


# ================================================================
# 7. CRITICAL CENTRAL CHARGE (3 tests)
# ================================================================

class TestCritical:
    """Test critical point kappa = 0 at c = 6."""

    def test_kappa_zero_at_c6(self):
        """kappa(c=6) = 0."""
        assert kappa_n2(6) == Rational(0)

    def test_critical_is_sl2_critical(self):
        """c=6 corresponds to k=-4 = -2*h^v(sl_2)."""
        crit = n2_critical_central_charge()
        assert crit['k_critical'] == Rational(-4)
        assert crit['is_sl2_critical']

    def test_dual_of_critical(self):
        """Dual of c=6 is c=0 with kappa=1."""
        crit = n2_critical_central_charge()
        assert crit['dual_c'] == Rational(0)
        assert crit['dual_kappa'] == Rational(1)


# ================================================================
# 8. SHADOW TOWER: T-LINE (8 tests)
# ================================================================

class TestShadowTowerTLine:
    """Test shadow tower on the T-line (Virasoro subalgebra)."""

    def test_T_line_kappa(self):
        data = n2_shadow_data_T_line()
        assert simplify(data['kappa'] - c / 2) == 0

    def test_T_line_alpha(self):
        data = n2_shadow_data_T_line()
        assert data['alpha'] == Rational(2)

    def test_T_line_S4(self):
        data = n2_shadow_data_T_line()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(data['S4'] - expected) == 0

    def test_T_line_class_M(self):
        data = n2_shadow_data_T_line()
        assert data['class'] == 'M'

    def test_T_line_matches_virasoro_at_c1(self):
        tower = n2_shadow_tower_T_line(1, max_arity=5)
        assert tower[2] == Rational(1, 2)
        assert tower[3] == Rational(2)
        assert tower[4] == Rational(10, 27)

    def test_T_line_matches_virasoro_at_c3_2(self):
        tower = n2_shadow_tower_T_line(Rational(3, 2), max_arity=4)
        assert tower[2] == Rational(3, 4)
        assert tower[3] == Rational(2)

    def test_T_line_growth_rate_positive(self):
        """Growth rate > 0 for c = 3 (large volume)."""
        rho = n2_shadow_growth_rate_T_line(3)
        assert rho > 0

    def test_T_line_growth_at_c1(self):
        """Virasoro rho at c=1: check it is > 1 (divergent tower)."""
        rho = n2_shadow_growth_rate_T_line(1)
        assert rho > 1.0


# ================================================================
# 9. SHADOW TOWER: J-LINE AND CLASS (4 tests)
# ================================================================

class TestShadowJLineAndClass:
    """Test J-line (class G) and overall shadow class."""

    def test_J_line_class_G(self):
        data = n2_shadow_data_J_line()
        assert data['class'] == 'G'

    def test_J_line_terminates(self):
        """J-line has S_r = 0 for r >= 3."""
        tower = n2_shadow_tower_J_line(1, max_arity=10)
        for r in range(3, 11):
            assert tower[r] == Rational(0)

    def test_overall_class_M(self):
        sc = n2_shadow_class()
        assert sc['class'] == 'M'

    def test_G_line_conjectured_L(self):
        data = n2_shadow_data_G_line()
        assert data['class'] == 'L'


# ================================================================
# 10. GENUS EXPANSION (4 tests)
# ================================================================

class TestGenusExpansion:
    """Test F_g = kappa * lambda_g^FP with CORRECT kappa."""

    def test_F1_at_c1(self):
        """F_1(c=1) = (5/4) * (1/24) = 5/96."""
        f1 = n2_F_g(1, 1)
        assert f1 == Rational(5, 96)

    def test_F1_at_c3_2(self):
        """F_1(c=3/2) = (3/2) * (1/24) = 1/16."""
        f1 = n2_F_g(Rational(3, 2), 1)
        assert f1 == Rational(1, 16)

    def test_F1_at_c6(self):
        """F_1(c=6) = 0 (kappa = 0 at critical)."""
        f1 = n2_F_g(6, 1)
        assert f1 == Rational(0)

    def test_genus_table_positive_for_positive_kappa(self):
        """F_g > 0 for all g >= 1 when kappa > 0."""
        table = n2_genus_table(1, max_genus=5)
        for g, fg in table.items():
            assert fg > 0


# ================================================================
# 11. OPE CONSISTENCY (4 tests)
# ================================================================

class TestOPEConsistency:
    """Test OPE data for the N=2 SCA."""

    def test_TT_quartic_pole(self):
        prod = n2_nth_product("T", "T", 3)
        assert simplify(prod["vac"] - c / 2) == 0

    def test_GpGm_cubic_pole(self):
        prod = n2_nth_product("G+", "G-", 2)
        assert simplify(prod["vac"] - c / 3) == 0

    def test_JJ_double_pole(self):
        prod = n2_nth_product("J", "J", 1)
        assert simplify(prod["vac"] - c / 3) == 0

    def test_GpGp_vanishes(self):
        products = n2_nth_products()
        assert len(products[("G+", "G+")]) == 0


# ================================================================
# 12. FULL VERIFICATION (3 tests)
# ================================================================

class TestFullVerification:
    """Run the full internal verification suite."""

    def test_verify_all_passes(self):
        results = verify_all()
        for name, passed in results.items():
            assert passed, f"Verification failed: {name}"

    def test_coset_all_levels(self):
        """Coset decomposition consistent at levels 1-10."""
        for k_val in range(1, 11):
            dec = coset_kappa_decomposition(k_val)
            assert dec['consistent_k'], f"Failed at k={k_val}"
            assert dec['consistent_c'], f"Failed at k={k_val} (c-formula)"

    def test_kappa_formula_from_k_and_c_agree(self):
        """kappa_from_k and kappa_from_c agree at 10 levels."""
        for k_val in range(1, 11):
            c_val = n2_central_charge(k_val)
            kap_k = kappa_n2_from_k(k_val)
            kap_c = kappa_n2(c_val)
            assert simplify(kap_k - kap_c) == 0, (
                f"Disagreement at k={k_val}: from_k={kap_k}, from_c={kap_c}"
            )
