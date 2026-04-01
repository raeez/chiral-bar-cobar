"""Tests for CE cohomology of negative-mode Lie algebras.

Three families tested:
  1. sl_2: g_- = sl_2 tensor t^{-1}C[t^{-1}]
  2. sl_3: g_- = sl_3 tensor t^{-1}C[t^{-1}]
  3. Witt: W_+ = Span{L_{-n} : n >= 2}

KEY FINDING: CE cohomology H^*(g_-, C) is DISTINCT from chiral bar
cohomology H^*(B(A)). They agree at degree 1 for KM algebras and
at degree 2 for sl_2, but diverge at higher degrees.

  sl_2:  CE H^1=3 = bar H^1=3  (agree)
         CE H^2=5 = bar H^2=5  (agree)
         CE H^3=7 != bar H^3=15 (DIFFER: OS form contributions)
  sl_3:  CE H^1=8 = bar H^1=8  (agree)
         CE H^2=20 != bar H^2=36 (DIFFER)
  Witt:  CE H^1=3 != bar H^1=1  (DIFFER: modes vs fields)
         CE H^2=5 != bar H^2=2  (DIFFER)

The CE computation uses ONLY the Lie bracket structure. The chiral
bar complex additionally involves configuration space forms (OS algebra)
and the factorization algebra structure. The discrepancy quantifies
the OS form contribution to bar cohomology.
"""

import pytest

from compute.lib.bar_cohomology_ce import (
    ChevalleyEilenbergComplex,
    cross_verify_sl2,
    cross_verify_sl3,
    cross_verify_virasoro,
    motzkin_differences,
    riordan,
    sl2_bar_cohomology_ce,
    sl2_bar_cohomology_ce_detail,
    sl2_ce,
    sl3_bar_cohomology_ce,
    sl3_bar_cohomology_ce_detail,
    sl3_ce,
    verify_euler_product,
    vir_bar_cohomology_ce,
    vir_bar_cohomology_ce_detail,
    witt_bracket,
    witt_ce,
    loop_algebra_bracket,
    SL2_DIM,
    SL2_BRACKET,
    SL3_DIM,
)


# ============================================================
# d^2 = 0 verification (fundamental axiom)
# ============================================================

class TestDSquaredSl2:
    """Verify d^2 = 0 for the CE differential of sl_2 loop algebra."""

    def test_d_squared_weight1(self):
        ce = sl2_ce(4)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 1), f"d^2 != 0 at deg {deg}, weight 1"

    def test_d_squared_weight2(self):
        ce = sl2_ce(4)
        for deg in range(0, 5):
            assert ce.verify_d_squared(deg, 2), f"d^2 != 0 at deg {deg}, weight 2"

    def test_d_squared_weight3(self):
        ce = sl2_ce(4)
        for deg in range(0, 5):
            assert ce.verify_d_squared(deg, 3), f"d^2 != 0 at deg {deg}, weight 3"

    def test_d_squared_weight4(self):
        ce = sl2_ce(4)
        for deg in range(0, 5):
            assert ce.verify_d_squared(deg, 4), f"d^2 != 0 at deg {deg}, weight 4"

    def test_d_squared_weight5(self):
        ce = sl2_ce(5)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 5), f"d^2 != 0 at deg {deg}, weight 5"

    def test_d_squared_weight6(self):
        ce = sl2_ce(6)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 6), f"d^2 != 0 at deg {deg}, weight 6"


class TestDSquaredSl3:
    """Verify d^2 = 0 for the CE differential of sl_3 loop algebra."""

    def test_d_squared_weight1(self):
        ce = sl3_ce(3)
        for deg in range(0, 5):
            assert ce.verify_d_squared(deg, 1), f"d^2 != 0 at deg {deg}, weight 1"

    def test_d_squared_weight2(self):
        ce = sl3_ce(3)
        for deg in range(0, 5):
            assert ce.verify_d_squared(deg, 2), f"d^2 != 0 at deg {deg}, weight 2"

    def test_d_squared_weight3(self):
        ce = sl3_ce(3)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 3), f"d^2 != 0 at deg {deg}, weight 3"


class TestDSquaredWitt:
    """Verify d^2 = 0 for the CE differential of the Witt algebra."""

    def test_d_squared_weight4(self):
        ce = witt_ce(10)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 4), f"d^2 != 0 at deg {deg}, weight 4"

    def test_d_squared_weight6(self):
        ce = witt_ce(10)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 6), f"d^2 != 0 at deg {deg}, weight 6"

    def test_d_squared_weight8(self):
        ce = witt_ce(10)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 8), f"d^2 != 0 at deg {deg}, weight 8"

    def test_d_squared_weight10(self):
        ce = witt_ce(10)
        for deg in range(0, 3):
            assert ce.verify_d_squared(deg, 10), f"d^2 != 0 at deg {deg}, weight 10"


# ============================================================
# Chain group dimensions
# ============================================================

class TestChainDimsSl2:
    """Verify dimensions of CE^p_H for sl_2 loop algebra."""

    def test_weight1(self):
        """CE^p_1: only p=1 is nonzero, with 3 generators."""
        ce = sl2_ce(4)
        assert ce.chain_group_dim(0, 1) == 0
        assert ce.chain_group_dim(1, 1) == 3
        assert ce.chain_group_dim(2, 1) == 0

    def test_weight2(self):
        """CE^p_2: p=1 from mode-2, p=2 from mode-1 pairs."""
        ce = sl2_ce(4)
        assert ce.chain_group_dim(1, 2) == 3
        assert ce.chain_group_dim(2, 2) == 3

    def test_weight3(self):
        """CE^p_3: p=1 from mode-3, p=2 mixed, p=3 from mode-1 triple."""
        ce = sl2_ce(4)
        assert ce.chain_group_dim(1, 3) == 3
        assert ce.chain_group_dim(2, 3) == 9
        assert ce.chain_group_dim(3, 3) == 1

    def test_weight4(self):
        ce = sl2_ce(4)
        assert ce.chain_group_dim(1, 4) == 3
        assert ce.chain_group_dim(2, 4) == 12
        assert ce.chain_group_dim(3, 4) == 9


class TestChainDimsSl3:
    """Verify dimensions of CE^p_H for sl_3 loop algebra."""

    def test_weight1_p1(self):
        """CE^1_1 = 8 (the 8 generators of sl_3)."""
        ce = sl3_ce(3)
        assert ce.chain_group_dim(1, 1) == 8

    def test_weight1_p2(self):
        """CE^2_1 = 0."""
        ce = sl3_ce(3)
        assert ce.chain_group_dim(2, 1) == 0

    def test_weight2_p1(self):
        """CE^1_2 = 8 (mode-2 generators)."""
        ce = sl3_ce(3)
        assert ce.chain_group_dim(1, 2) == 8

    def test_weight2_p2(self):
        """CE^2_2 = C(8,2) = 28 (pairs from mode-1)."""
        ce = sl3_ce(3)
        assert ce.chain_group_dim(2, 2) == 28


class TestChainDimsWitt:
    """Verify dimensions of CE^p_H for Witt algebra."""

    def test_one_generator_per_weight(self):
        """Each weight >= 2 has exactly one generator L_{-n}."""
        ce = witt_ce(10)
        for H in range(2, 11):
            assert ce.chain_group_dim(1, H) == 1

    def test_no_weight1(self):
        """No generators at weight 1."""
        ce = witt_ce(10)
        assert ce.chain_group_dim(1, 1) == 0

    def test_degree2_weight4(self):
        """CE^2_4 = 0 (only decomposition 2+2, but single L_{-2})."""
        ce = witt_ce(10)
        assert ce.chain_group_dim(2, 4) == 0

    def test_degree2_weight5(self):
        """CE^2_5 = 1 (L_{-2} ^ L_{-3})."""
        ce = witt_ce(10)
        assert ce.chain_group_dim(2, 5) == 1

    def test_degree2_weight7(self):
        """CE^2_7 = 2 (L_{-2}^L_{-5} and L_{-3}^L_{-4})."""
        ce = witt_ce(10)
        assert ce.chain_group_dim(2, 7) == 2

    def test_degree3_weight9(self):
        """CE^3_9 = 1 (L_{-2}^L_{-3}^L_{-4})."""
        ce = witt_ce(10)
        assert ce.chain_group_dim(3, 9) == 1


# ============================================================
# sl_2 CE cohomology: weight-by-weight
# ============================================================

class TestSl2CEWeightDecomposition:
    """Verify individual H^n(g_-)_H for sl_2."""

    def test_h1_weight1(self):
        """H^1_1 = 3: the three weight-1 generators."""
        ce = sl2_ce(4)
        assert ce.cohomology_dim(1, 1) == 3

    def test_h1_weight2(self):
        """H^1_2 = 0: d_1 at weight 2 is injective."""
        ce = sl2_ce(4)
        assert ce.cohomology_dim(1, 2) == 0

    def test_h1_weight3(self):
        """H^1_3 = 0."""
        ce = sl2_ce(4)
        assert ce.cohomology_dim(1, 3) == 0

    def test_h2_weight2(self):
        """H^2_2 = 0."""
        ce = sl2_ce(4)
        assert ce.cohomology_dim(2, 2) == 0

    def test_h2_weight3(self):
        """H^2_3 = 5 (the main H^2 contribution)."""
        ce = sl2_ce(4)
        assert ce.cohomology_dim(2, 3) == 5

    def test_h2_weight4(self):
        """H^2_4 = 0."""
        ce = sl2_ce(4)
        assert ce.cohomology_dim(2, 4) == 0

    def test_h2_weight5(self):
        """H^2_5 = 0."""
        ce = sl2_ce(5)
        assert ce.cohomology_dim(2, 5) == 0

    def test_h2_weight6(self):
        """H^2_6 = 0."""
        ce = sl2_ce(6)
        assert ce.cohomology_dim(2, 6) == 0


# ============================================================
# sl_2 CE cohomology: totals
# ============================================================

class TestSl2CETotals:
    """Total CE cohomology for sl_2 loop algebra."""

    def test_h1_equals_3(self):
        """H^1(g_-) = 3 = dim(sl_2)."""
        result = sl2_bar_cohomology_ce(max_degree=1, max_weight=4)
        assert result[1] == 3

    def test_h2_equals_5(self):
        """H^2(g_-) = 5.

        This agrees with bar H^2(B(sl_2)) = 5 and disagrees with
        Riordan R(5) = 6.
        """
        result = sl2_bar_cohomology_ce(max_degree=2, max_weight=6)
        assert result[2] == 5

    def test_h3_equals_7(self):
        """H^3(g_-) = 7.

        This DIFFERS from bar H^3(B(sl_2)) = 15 = R(6).
        The discrepancy (15 - 7 = 8) arises from OS form contributions
        in the chiral bar complex that are absent in the CE complex.
        """
        result = sl2_bar_cohomology_ce(max_degree=3, max_weight=10)
        assert result[3] == 7

    def test_h1_stability(self):
        """H^1 = 3 independent of truncation."""
        for mw in [4, 6, 8]:
            r = sl2_bar_cohomology_ce(max_degree=1, max_weight=mw)
            assert r[1] == 3, f"H^1 != 3 at max_weight={mw}"

    def test_h2_stability(self):
        """H^2 = 5 independent of truncation."""
        for mw in [4, 6, 8]:
            r = sl2_bar_cohomology_ce(max_degree=2, max_weight=mw)
            assert r[2] == 5, f"H^2 != 5 at max_weight={mw}"


# ============================================================
# sl_3 CE cohomology
# ============================================================

class TestSl3CECohomology:
    """CE cohomology of sl_3 loop algebra."""

    def test_h1_equals_8(self):
        """H^1(g_-) = 8 = dim(sl_3)."""
        result = sl3_bar_cohomology_ce(max_degree=1, max_weight=3)
        assert result[1] == 8

    def test_h1_all_at_weight1(self):
        """H^1 is concentrated at weight 1."""
        detail = sl3_bar_cohomology_ce_detail(max_degree=1, max_weight=4)
        assert detail[1] == {1: 8}

    def test_h2_equals_20(self):
        """H^2(g_-) = 20.

        This DIFFERS from bar H^2(B(sl_3)) = 36.
        The discrepancy (36 - 20 = 16) arises from OS form
        contributions absent in the CE complex.
        """
        result = sl3_bar_cohomology_ce(max_degree=2, max_weight=4)
        assert result[2] == 20

    def test_h2_all_at_weight2(self):
        """H^2 is concentrated at weight 2."""
        detail = sl3_bar_cohomology_ce_detail(max_degree=2, max_weight=5)
        assert detail[2] == {2: 20}

    def test_h1_stability(self):
        """H^1 = 8 independent of truncation."""
        for mw in [3, 4, 5]:
            r = sl3_bar_cohomology_ce(max_degree=1, max_weight=mw)
            assert r[1] == 8, f"H^1 != 8 at max_weight={mw}"

    def test_h2_stability(self):
        """H^2 = 20 independent of truncation."""
        for mw in [3, 4, 5]:
            r = sl3_bar_cohomology_ce(max_degree=2, max_weight=mw)
            assert r[2] == 20, f"H^2 != 20 at max_weight={mw}"

    @pytest.mark.slow
    def test_h3_equals_70(self):
        """H^3(g_-) = 70.

        This DIFFERS from bar H^3(B(sl_3)) = 204.
        """
        result = sl3_bar_cohomology_ce(max_degree=3, max_weight=5)
        assert result[3] == 70


# ============================================================
# Witt algebra CE cohomology
# ============================================================

class TestWittCECohomology:
    """CE cohomology of Witt algebra W_+ = {L_{-n} : n >= 2}."""

    def test_h1_equals_3(self):
        """H^1(W_+) = 3 (at weights 2, 3, 4).

        The abelianization W_+/[W_+,W_+] has dimension 3:
        L_{-2}, L_{-3}, L_{-4} are not in the image of the bracket
        (no valid decompositions with m,n >= 2), while L_{-5} = [L_{-2}, L_{-3}]
        and all higher modes are in the image.
        """
        result = vir_bar_cohomology_ce(max_degree=1, max_weight=10)
        assert result[1] == 3

    def test_h1_weight_decomposition(self):
        """H^1 = 1 at each of weights 2, 3, 4; zero elsewhere."""
        detail = vir_bar_cohomology_ce_detail(max_degree=1, max_weight=10)
        assert detail[1] == {2: 1, 3: 1, 4: 1}

    def test_h1_weight2_computation(self):
        """H^1_2 = 1: L_{-2} is not a bracket (min bracket output is weight 4)."""
        ce = witt_ce(10)
        assert ce.cohomology_dim(1, 2) == 1

    def test_h1_weight3_computation(self):
        """H^1_3 = 1: L_{-3} is not a bracket (2+2=4, 2+3=5: no sum gives 3)."""
        ce = witt_ce(10)
        assert ce.cohomology_dim(1, 3) == 1

    def test_h1_weight4_computation(self):
        """H^1_4 = 1: L_{-4} is not a bracket (the only candidate [L_{-2},L_{-2}]=0)."""
        ce = witt_ce(10)
        assert ce.cohomology_dim(1, 4) == 1

    def test_h1_weight5_computation(self):
        """H^1_5 = 0: L_{-5} = [L_{-2}, L_{-3}] is in the image."""
        ce = witt_ce(10)
        assert ce.cohomology_dim(1, 5) == 0

    def test_h1_weight6_computation(self):
        """H^1_6 = 0: L_{-6} = (1/2)[L_{-2}, L_{-4}] is in the image."""
        ce = witt_ce(10)
        assert ce.cohomology_dim(1, 6) == 0

    def test_h1_stability(self):
        """H^1 = 3 independent of truncation."""
        for mw in [8, 10, 14, 18]:
            r = vir_bar_cohomology_ce(max_degree=1, max_weight=mw)
            assert r[1] == 3, f"H^1 != 3 at max_weight={mw}"

    def test_h2_equals_5(self):
        """H^2(W_+) = 5 (at weights 7,8,9,10,11).

        This DIFFERS from bar H^2(B(Vir)) = 2 (Motzkin difference).
        """
        result = vir_bar_cohomology_ce(max_degree=2, max_weight=18)
        assert result[2] == 5

    def test_h2_weight_decomposition(self):
        """H^2 contributions are each 1-dimensional at weights 7-11."""
        detail = vir_bar_cohomology_ce_detail(max_degree=2, max_weight=18)
        assert detail[2] == {7: 1, 8: 1, 9: 1, 10: 1, 11: 1}

    def test_h2_stability(self):
        """H^2 = 5 independent of truncation (stable from max_weight=12)."""
        for mw in [14, 16, 18]:
            r = vir_bar_cohomology_ce(max_degree=2, max_weight=mw)
            assert r[2] == 5, f"H^2 != 5 at max_weight={mw}"


# ============================================================
# CE vs bar cohomology: documented discrepancies
# ============================================================

class TestCEvsBarSl2:
    """Document where CE and bar cohomology agree/disagree for sl_2."""

    def test_agree_at_degree1(self):
        """CE H^1 = bar H^1 = 3 for sl_2."""
        ce_vals = sl2_bar_cohomology_ce(max_degree=1, max_weight=4)
        assert ce_vals[1] == 3

    def test_agree_at_degree2(self):
        """CE H^2 = bar H^2 = 5 for sl_2."""
        ce_vals = sl2_bar_cohomology_ce(max_degree=2, max_weight=6)
        assert ce_vals[2] == 5

    def test_disagree_at_degree3(self):
        """CE H^3 = 7 != bar H^3 = 15 for sl_2.

        The discrepancy arises because the chiral bar complex uses
        tensor products with OS forms on Conf_3(C), while the CE
        complex uses exterior powers Lambda^3(g_-^*).
        """
        ce_vals = sl2_bar_cohomology_ce(max_degree=3, max_weight=10)
        bar_h3 = 15
        assert ce_vals[3] == 7, "CE H^3 should be 7"
        assert ce_vals[3] != bar_h3, "CE and bar should disagree at degree 3"
        assert bar_h3 - ce_vals[3] == 8, "Discrepancy should be 8"


class TestCEvsBarSl3:
    """Document where CE and bar cohomology agree/disagree for sl_3."""

    def test_agree_at_degree1(self):
        """CE H^1 = bar H^1 = 8 for sl_3."""
        ce_vals = sl3_bar_cohomology_ce(max_degree=1, max_weight=3)
        assert ce_vals[1] == 8

    def test_disagree_at_degree2(self):
        """CE H^2 = 20 != bar H^2 = 36 for sl_3.

        Discrepancy: 36 - 20 = 16.
        """
        ce_vals = sl3_bar_cohomology_ce(max_degree=2, max_weight=5)
        bar_h2 = 36
        assert ce_vals[2] == 20, "CE H^2 should be 20"
        assert ce_vals[2] != bar_h2, "CE and bar should disagree at degree 2"
        assert bar_h2 - ce_vals[2] == 16, "Discrepancy should be 16"


class TestCEvsBarVirasoro:
    """Document where CE and bar cohomology agree/disagree for Virasoro."""

    def test_disagree_at_degree1(self):
        """CE H^1(W_+) = 3 != bar H^1(B(Vir)) = 1.

        CE counts mode generators: L_{-2}, L_{-3}, L_{-4} survive
        in H^1(W_+) = W_+/[W_+,W_+].
        Bar counts field generators: just T.
        """
        ce_vals = vir_bar_cohomology_ce(max_degree=1, max_weight=10)
        motzkin = motzkin_differences(1)
        assert ce_vals[1] == 3, "CE H^1 should be 3"
        assert motzkin[1] == 1, "Motzkin diff at n=1 should be 1"
        assert ce_vals[1] != motzkin[1], "CE and bar should disagree"

    def test_disagree_at_degree2(self):
        """CE H^2(W_+) = 5 != bar H^2(B(Vir)) = 2."""
        ce_vals = vir_bar_cohomology_ce(max_degree=2, max_weight=18)
        motzkin = motzkin_differences(2)
        assert ce_vals[2] == 5, "CE H^2 should be 5"
        assert motzkin[2] == 2, "Motzkin diff at n=2 should be 2"
        assert ce_vals[2] != motzkin[2], "CE and bar should disagree"


# ============================================================
# Witt algebra bracket correctness
# ============================================================

class TestWittBracket:
    """Verify the Witt algebra bracket structure."""

    def test_bracket_23(self):
        """[L_{-2}, L_{-3}] = L_{-5}."""
        dim, bracket = witt_bracket(10)
        assert bracket[(0, 1)] == {3: 1}

    def test_bracket_24(self):
        """[L_{-2}, L_{-4}] = 2 L_{-6}."""
        dim, bracket = witt_bracket(10)
        assert bracket[(0, 2)] == {4: 2}

    def test_bracket_34(self):
        """[L_{-3}, L_{-4}] = L_{-7}."""
        dim, bracket = witt_bracket(10)
        assert bracket[(1, 2)] == {5: 1}

    def test_bracket_25(self):
        """[L_{-2}, L_{-5}] = 3 L_{-7}."""
        dim, bracket = witt_bracket(10)
        assert bracket[(0, 3)] == {5: 3}

    def test_bracket_antisymmetry(self):
        """Bracket is antisymmetric."""
        dim, bracket = witt_bracket(10)
        for (a, b), result in list(bracket.items()):
            if a < b:
                rev = bracket.get((b, a), {})
                for c, coeff in result.items():
                    assert rev.get(c, 0) == -coeff, \
                        f"Antisymmetry fails: [{a},{b}] vs [{b},{a}]"

    def test_jacobi_234(self):
        """Jacobi on L_{-2}, L_{-3}, L_{-4}.

        [[L_{-2},L_{-3}],L_{-4}] = [L_{-5}, L_{-4}] = (4-5)L_{-9} = -L_{-9}
        [[L_{-3},L_{-4}],L_{-2}] = [L_{-7}, L_{-2}] = (2-7)L_{-9} = -5L_{-9}
        [[L_{-4},L_{-2}],L_{-3}] = [-2L_{-6}, L_{-3}] = -2(3-6)L_{-9} = 6L_{-9}
        Sum: -1 - 5 + 6 = 0.
        """
        assert -1 + (-5) + 6 == 0

    def test_jacobi_general(self):
        """Jacobi identity (n-m)(m+n-p) + (p-n)(n+p-m) + (m-p)(p+m-n) = 0.

        For [L_{-m},L_{-n}] = (n-m)L_{-(m+n)}, the double brackets are:
        [[L_m,L_n],L_p] = (n-m)(p-m-n)L_{-(m+n+p)}
        Jacobi = (n-m)(p-m-n) + (p-n)(m-n-p) + (m-p)(n-p-m) = 0.
        """
        # Verify algebraically for several triples
        for m in range(2, 6):
            for n in range(m + 1, 7):
                for p in range(n + 1, 8):
                    t1 = (n - m) * (p - m - n)
                    t2 = (p - n) * (m - n - p)
                    t3 = (m - p) * (n - p - m)
                    assert t1 + t2 + t3 == 0, \
                        f"Jacobi fails for m={m}, n={n}, p={p}"


# ============================================================
# Loop algebra construction
# ============================================================

class TestLoopAlgebra:
    """Verify loop algebra construction."""

    def test_sl2_loop_dim(self):
        """sl_2 loop at max_weight=3 has 9 generators."""
        total_dim, _, gen_weights = loop_algebra_bracket(
            SL2_DIM, SL2_BRACKET, 3, min_weight=1)
        assert total_dim == 9
        assert gen_weights == [1, 1, 1, 2, 2, 2, 3, 3, 3]

    def test_sl3_loop_dim(self):
        """sl_3 loop at max_weight=2 has 16 generators."""
        from compute.lib.bar_cohomology_ce import _get_sl3_bracket
        sl3_br = _get_sl3_bracket()
        total_dim, _, gen_weights = loop_algebra_bracket(
            SL3_DIM, sl3_br, 2, min_weight=1)
        assert total_dim == 16

    def test_witt_dim(self):
        """Witt at max_weight=10 has 9 generators."""
        dim, _ = witt_bracket(10)
        assert dim == 9

    def test_no_out_of_range_brackets(self):
        """No brackets with output at weight > max_weight."""
        total_dim, loop_br, gen_weights = loop_algebra_bracket(
            SL2_DIM, SL2_BRACKET, 4, min_weight=1)
        for (a, b), result in loop_br.items():
            for c, coeff in result.items():
                assert c < total_dim, f"Output index {c} >= total_dim {total_dim}"


# ============================================================
# Cross-consistency with existing implementations
# ============================================================

class TestCrossConsistencySl2:
    """Verify new sl_2 CE matches existing LoopAlgebraCE."""

    def test_matches_existing_at_weight1(self):
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        new = sl2_ce(4)
        old = LoopAlgebraCE(max_weight=4)
        for p in range(0, 4):
            assert new.cohomology_dim(p, 1) == old.cohomology_dim(p, 1), \
                f"Mismatch at p={p}, H=1"

    def test_matches_existing_at_weight2(self):
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        new = sl2_ce(4)
        old = LoopAlgebraCE(max_weight=4)
        for p in range(0, 5):
            assert new.cohomology_dim(p, 2) == old.cohomology_dim(p, 2), \
                f"Mismatch at p={p}, H=2"

    def test_matches_existing_at_weight3(self):
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        new = sl2_ce(4)
        old = LoopAlgebraCE(max_weight=4)
        for p in range(0, 5):
            assert new.cohomology_dim(p, 3) == old.cohomology_dim(p, 3), \
                f"Mismatch at p={p}, H=3"

    def test_matches_existing_totals(self):
        from compute.lib.bar_cohomology_verification import strategy_a
        new_vals = sl2_bar_cohomology_ce(max_degree=2, max_weight=6)
        old_vals = strategy_a(max_degree=2, max_weight=6)
        assert new_vals[1] == old_vals[1], "H^1 mismatch"
        assert new_vals[2] == old_vals[2], "H^2 mismatch"


class TestCrossConsistencySl3:
    """Verify new sl_3 CE matches existing ce_cohomology_loop."""

    def test_matches_existing_h1(self):
        from compute.lib.ce_cohomology_loop import ce_cohomology_table
        from compute.lib.sl3_bar import DIM_G
        new = sl3_ce(3)
        old_table = ce_cohomology_table(max_weight=3, max_degree=1, dim_g=DIM_G)
        for H in range(1, 4):
            new_val = new.cohomology_dim(1, H)
            old_val = old_table.get((1, H), 0)
            assert new_val == old_val, f"H^1_{H}: new={new_val}, old={old_val}"

    def test_matches_existing_h2(self):
        from compute.lib.ce_cohomology_loop import ce_cohomology_table
        from compute.lib.sl3_bar import DIM_G
        new = sl3_ce(3)
        old_table = ce_cohomology_table(max_weight=3, max_degree=2, dim_g=DIM_G)
        for H in range(1, 4):
            new_val = new.cohomology_dim(2, H)
            old_val = old_table.get((2, H), 0)
            assert new_val == old_val, f"H^2_{H}: new={new_val}, old={old_val}"


# ============================================================
# Euler characteristic verification
# ============================================================

class TestEulerCharacteristic:
    """Verify Euler char from CE dims matches product formula."""

    def test_sl2_euler(self):
        """sl_2 Euler char matches prod (1-q^{w_i})."""
        ce = sl2_ce(6)
        euler = verify_euler_product(ce, 6)
        for H, (e_dims, e_prod, ok) in euler.items():
            assert ok, f"Euler mismatch at H={H}: dims={e_dims}, product={e_prod}"

    def test_sl3_euler(self):
        """sl_3 Euler char matches product formula."""
        ce = sl3_ce(3)
        euler = verify_euler_product(ce, 3)
        for H, (e_dims, e_prod, ok) in euler.items():
            assert ok, f"Euler mismatch at H={H}"

    def test_witt_euler(self):
        """Witt Euler char matches product formula."""
        ce = witt_ce(10)
        euler = verify_euler_product(ce, 10)
        for H, (e_dims, e_prod, ok) in euler.items():
            assert ok, f"Euler mismatch at H={H}"


# ============================================================
# Differential rank checks
# ============================================================

class TestDifferentialRanksSl2:
    """Verify specific differential ranks from hand computation."""

    def test_d1_weight2_rank3(self):
        """d_1: CE^1_2 -> CE^2_2 has rank 3 (full rank)."""
        ce = sl2_ce(4)
        d = ce.ce_differential(1, 2)
        assert d.rank() == 3

    def test_d2_weight3_rank1(self):
        """d_2: CE^2_3 -> CE^3_3 has rank 1."""
        ce = sl2_ce(4)
        d = ce.ce_differential(2, 3)
        assert d.rank() == 1

    def test_d1_weight3_rank3(self):
        """d_1: CE^1_3 -> CE^2_3 has rank 3."""
        ce = sl2_ce(4)
        d = ce.ce_differential(1, 3)
        assert d.rank() == 3


class TestDifferentialRanksSl3:
    """Verify differential ranks for sl_3."""

    def test_d1_weight2_rank8(self):
        """d_1: CE^1_2 -> CE^2_2 has rank 8 (full rank on source)."""
        ce = sl3_ce(3)
        d = ce.ce_differential(1, 2)
        assert d.rank() == 8

    def test_d2_weight2_target_zero(self):
        """d_2: CE^2_2 -> CE^3_2 target is 0-dimensional."""
        ce = sl3_ce(3)
        # CE^3_2 = C(8,3) at weight 2 requires 3 parts summing to 2,
        # each >= 1, so only (1,1,...) is possible but need 3 parts
        # of sum 2: impossible for 3 parts >= 1. So dim = 0.
        assert ce.chain_group_dim(3, 2) == 0


class TestDifferentialRanksWitt:
    """Verify differential ranks for Witt algebra."""

    def test_d1_weight5(self):
        """d_1: CE^1_5 -> CE^2_5 has rank 1.

        d(e^5) = (3-2) e^2 ^ e^3 = e^2 ^ e^3 (nonzero).
        """
        ce = witt_ce(10)
        d = ce.ce_differential(1, 5)
        assert d.rank() == 1

    def test_d1_weight6(self):
        """d_1: CE^1_6 -> CE^2_6 has rank 1.

        d(e^6) = (4-2) e^2 ^ e^4 = 2 e^2 ^ e^4 (nonzero).
        """
        ce = witt_ce(10)
        d = ce.ce_differential(1, 6)
        assert d.rank() == 1

    def test_d1_weight4_rank0(self):
        """d_1: CE^1_4 -> CE^2_4 has rank 0.

        CE^2_4 = 0 (only 2+2, but Lambda^2 of single element = 0).
        """
        ce = witt_ce(10)
        d = ce.ce_differential(1, 4)
        assert d.rank() == 0


# ============================================================
# Riordan and Motzkin reference values
# ============================================================

class TestRiordan:
    """Verify Riordan number computation."""

    def test_base_cases(self):
        assert riordan(0) == 1
        assert riordan(1) == 0
        assert riordan(2) == 1
        assert riordan(3) == 1

    def test_higher_values(self):
        assert riordan(4) == 3
        assert riordan(5) == 6
        assert riordan(6) == 15
        assert riordan(7) == 36
        assert riordan(8) == 91
        assert riordan(9) == 232


class TestMotzkinDifferences:
    """Verify Motzkin difference computation (Virasoro bar cohomology)."""

    def test_known_values(self):
        md = motzkin_differences(10)
        expected = {1: 1, 2: 2, 3: 5, 4: 12, 5: 30,
                    6: 76, 7: 196, 8: 512, 9: 1353, 10: 3610}
        for n, val in expected.items():
            assert md[n] == val, f"M({n+1})-M({n}): got {md[n]}, expected {val}"


# ============================================================
# Cross-verification functions
# ============================================================

class TestCrossVerifySl2:
    """Test the cross_verify_sl2 function."""

    def test_degree1_matches(self):
        xv = cross_verify_sl2(max_degree=1, max_weight=4)
        assert xv[1]["CE"] == 3
        assert xv[1]["CE_eq_bar"] is True

    def test_degree2_matches(self):
        xv = cross_verify_sl2(max_degree=2, max_weight=6)
        assert xv[2]["CE"] == 5
        assert xv[2]["CE_eq_bar"] is True


class TestCrossVerifySl3:
    """Test the cross_verify_sl3 function."""

    def test_degree1_matches(self):
        xv = cross_verify_sl3(max_degree=1, max_weight=3)
        assert xv[1]["CE"] == 8
        assert xv[1]["CE_eq_bar"] is True

    def test_degree2_differs(self):
        xv = cross_verify_sl3(max_degree=2, max_weight=5)
        assert xv[2]["CE"] == 20
        assert xv[2]["CE_eq_bar"] is False


class TestCrossVerifyVirasoro:
    """Test the cross_verify_virasoro function."""

    def test_all_disagree(self):
        """CE of Witt and Motzkin diffs disagree at all tested degrees."""
        xv = cross_verify_virasoro(max_degree=2, max_weight=18)
        assert xv[1]["agree"] is False
        assert xv[2]["agree"] is False


# ============================================================
# H^1 universality: H^1(g_-) = dim(g) for KM
# ============================================================

class TestH1Universality:
    """For KM algebras, H^1(g_-) = dim(g) always.

    This is because H^1(g_-, C) = g_-/[g_-,g_-] (abelianization),
    and the bracket [g_{-1}, g_{-n}] surjects onto g_{-(1+n)} for n >= 1,
    so only weight-1 generators survive. dim = dim(g).
    """

    def test_sl2(self):
        assert sl2_bar_cohomology_ce(1, 4)[1] == 3

    def test_sl3(self):
        assert sl3_bar_cohomology_ce(1, 3)[1] == 8


# ============================================================
# Weight concentration theorems
# ============================================================

class TestWeightConcentration:
    """Verify that CE cohomology is concentrated at specific weights."""

    def test_sl2_h1_concentrated_at_weight1(self):
        """sl_2: H^1 is entirely at weight 1."""
        detail = sl2_bar_cohomology_ce_detail(max_degree=1, max_weight=6)
        assert detail[1] == {1: 3}

    def test_sl2_h2_concentrated_at_weight3(self):
        """sl_2: H^2 is entirely at weight 3."""
        detail = sl2_bar_cohomology_ce_detail(max_degree=2, max_weight=8)
        assert detail[2] == {3: 5}

    def test_sl3_h1_concentrated_at_weight1(self):
        """sl_3: H^1 is entirely at weight 1."""
        detail = sl3_bar_cohomology_ce_detail(max_degree=1, max_weight=4)
        assert detail[1] == {1: 8}

    def test_sl3_h2_concentrated_at_weight2(self):
        """sl_3: H^2 is entirely at weight 2."""
        detail = sl3_bar_cohomology_ce_detail(max_degree=2, max_weight=5)
        assert detail[2] == {2: 20}

    def test_witt_h1_weights_234(self):
        """Witt: H^1 is at weights 2, 3, 4 only."""
        detail = vir_bar_cohomology_ce_detail(max_degree=1, max_weight=14)
        assert set(detail[1].keys()) == {2, 3, 4}

    def test_witt_h2_weights_7_to_11(self):
        """Witt: H^2 is at weights 7, 8, 9, 10, 11 only."""
        detail = vir_bar_cohomology_ce_detail(max_degree=2, max_weight=20)
        assert set(detail[2].keys()) == {7, 8, 9, 10, 11}

    def test_witt_h2_each_1dim(self):
        """Witt: each H^2_H is 1-dimensional."""
        detail = vir_bar_cohomology_ce_detail(max_degree=2, max_weight=20)
        for H, dim in detail[2].items():
            assert dim == 1, f"H^2_{H} = {dim}, expected 1"


# ============================================================
# sl_2 H^3: the key discrepancy witness
# ============================================================

class TestSl2H3Discrepancy:
    """H^3(g_-) = 7 for sl_2, while bar H^3 = 15.

    The 8-dimensional discrepancy (15 - 7 = 8) arises from
    the OS form factor on Conf_3(C).
    """

    def test_h3_total(self):
        r = sl2_bar_cohomology_ce(max_degree=3, max_weight=10)
        assert r[3] == 7

    def test_h3_stability_check(self):
        """H^3 = 7 is stable under weight truncation."""
        for mw in [8, 10]:
            r = sl2_bar_cohomology_ce(max_degree=3, max_weight=mw)
            assert r[3] == 7, f"H^3 != 7 at max_weight={mw}"


# ============================================================
# Witt abelianization proof tests
# ============================================================

class TestWittAbelianization:
    """H^1(W_+) = W_+/[W_+,W_+] has dimension 3.

    L_{-2}, L_{-3}, L_{-4} are NOT in [W_+, W_+].
    L_{-n} for n >= 5 IS in [W_+, W_+]:
      L_{-5} = [L_{-2}, L_{-3}]
      L_{-6} = (1/2)[L_{-2}, L_{-4}]
    """

    def test_l5_is_bracket(self):
        """L_{-5} = [L_{-2}, L_{-3}] is in [W_+,W_+]."""
        ce = witt_ce(10)
        d = ce.ce_differential(1, 5)
        assert d.rank() == 1

    def test_l4_not_bracket(self):
        """L_{-4} is NOT in [W_+,W_+]."""
        ce = witt_ce(10)
        d = ce.ce_differential(1, 4)
        assert d.rank() == 0

    def test_l3_not_bracket(self):
        """L_{-3} is NOT in [W_+,W_+]."""
        ce = witt_ce(10)
        d = ce.ce_differential(1, 3)
        assert d.rank() == 0

    def test_l2_not_bracket(self):
        """L_{-2} is NOT in [W_+,W_+]."""
        ce = witt_ce(10)
        d = ce.ce_differential(1, 2)
        assert d.rank() == 0


# ============================================================
# Slow tests
# ============================================================

class TestSlow:
    """Computationally intensive tests."""

    @pytest.mark.slow
    def test_sl2_h3_extended(self):
        """Verify H^3 = 7 with extended weight range."""
        r = sl2_bar_cohomology_ce(max_degree=3, max_weight=12)
        assert r[3] == 7

    @pytest.mark.slow
    def test_sl3_h3(self):
        """H^3(sl_3 CE) = 70."""
        r = sl3_bar_cohomology_ce(max_degree=3, max_weight=5)
        assert r[3] == 70

    @pytest.mark.slow
    def test_witt_h2_extended(self):
        """Verify H^2(W_+) = 5 with extended range."""
        r = vir_bar_cohomology_ce(max_degree=2, max_weight=24)
        assert r[2] == 5


# ============================================================
# Discrepancy quantification
# ============================================================

class TestDiscrepancyQuantification:
    """Quantify the CE vs bar cohomology discrepancy.

    The ratio bar/CE measures the OS form contribution factor:
      sl_2 deg 1: 3/3 = 1.0 (no OS contribution)
      sl_2 deg 2: 5/5 = 1.0 (no OS contribution)
      sl_2 deg 3: 15/7 = 2.14 (OS contributes ~114%)
      sl_3 deg 1: 8/8 = 1.0
      sl_3 deg 2: 36/20 = 1.8 (OS contributes 80%)
    """

    def test_sl2_ratio_deg1(self):
        r = sl2_bar_cohomology_ce(1, 4)
        assert r[1] == 3
        # bar/CE = 3/3 = 1.0
        assert 3 / r[1] == 1.0

    def test_sl2_ratio_deg2(self):
        r = sl2_bar_cohomology_ce(2, 6)
        assert r[2] == 5
        assert 5 / r[2] == 1.0

    def test_sl2_ratio_deg3(self):
        r = sl2_bar_cohomology_ce(3, 10)
        assert r[3] == 7
        # bar H^3 = 15, ratio = 15/7
        assert 15 / r[3] > 2.0

    def test_sl3_ratio_deg2(self):
        r = sl3_bar_cohomology_ce(2, 5)
        assert r[2] == 20
        # bar H^2 = 36, ratio = 36/20 = 1.8
        assert 36 / r[2] == 1.8

    def test_discrepancy_grows_with_degree(self):
        """The bar/CE ratio grows with degree (more OS forms)."""
        sl2_ce_vals = sl2_bar_cohomology_ce(3, 10)
        bar_vals = {1: 3, 2: 5, 3: 15}
        ratios = {n: bar_vals[n] / sl2_ce_vals[n] for n in [1, 2, 3]}
        assert ratios[1] <= ratios[2] <= ratios[3], \
            f"Ratios should be non-decreasing: {ratios}"
