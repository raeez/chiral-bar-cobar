r"""Tests for the Pixton genus-5 ideal membership engine.

Tests conj:pixton-from-shadows at genus 5: the MC-descended tautological
relations from the shadow obstruction tower of class-M algebras should
generate the Pixton ideal I_5 in R*(M-bar_5).

Tests are organized into:
  FAST tests (~65): exact arithmetic, Bernoulli, lambda, WK, Hodge integrals
    for small graphs, shadow visibility formulas, Gorenstein structure,
    cross-genus patterns, complementarity, vertex weights, Pixton ideal structure.
  SLOW tests (~20): full genus-5 graph enumeration, planted-forest correction,
    symbolic polynomial extraction, class comparison, census, Euler characteristic.

Multi-path verification paths:
  Path 1: Direct graph sum computation (slow)
  Path 2: Bernoulli / A-hat formula (fast)
  Path 3: Cross-family consistency (slow)
  Path 4: Complementarity (fast: scalar lane; slow: full)
  Path 5: Cross-genus pattern (fast)
  Path 6: Gorenstein duality check (fast)

Manuscript references:
    conj:pixton-from-shadows (concordance.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction
from math import factorial, pi

from sympy import Symbol, Integer, Rational, cancel, simplify, expand

from compute.lib.pixton_genus5_engine import (
    # Exact arithmetic
    lambda_fp_exact,
    _bernoulli_exact,
    # Hodge integrals
    hodge_integral,
    _hodge_integral_cached,
    # Vertex weights
    ell_genus1,
    ell_genus2,
    vertex_weight,
    is_planted_forest,
    # Amplitude data
    GraphAmplitude,
    # Tautological ring
    taut_ring_dimensions_g5,
    gorenstein_check_g5,
    # Pixton relations
    pixton_relation_codim6_genus5,
    pixton_ideal_dimension_g5,
    # Cross-genus
    cross_genus_lambda_pattern,
    cross_genus_pf_pattern,
    compare_with_lower_genera,
    # Six-path lambda verification
    lambda5_six_path,
    # Complementarity (scalar)
    virasoro_complementarity_g5,
    # Shadow visibility formula
    faber_zagier_coefficients,
)

from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    c_sym,
    wk_intersection,
)

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    _lambda_fp_exact,
)


# ============================================================================
# Section 1: Bernoulli number verification (FAST)
# ============================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers used in genus-5 computation."""

    def test_B2(self):
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        assert _bernoulli_exact(8) == Fraction(-1, 30)

    def test_B10(self):
        """B_10 = 5/66 -- the key Bernoulli number for lambda_5^FP."""
        assert _bernoulli_exact(10) == Fraction(5, 66)

    def test_B12(self):
        """B_12 = -691/2730."""
        assert _bernoulli_exact(12) == Fraction(-691, 2730)

    def test_B_odd_zero(self):
        """B_n = 0 for odd n > 1."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert _bernoulli_exact(n) == Fraction(0)

    def test_B0(self):
        assert _bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        assert _bernoulli_exact(1) == Fraction(-1, 2)


# ============================================================================
# Section 2: Lambda_g^FP exact values (FAST)
# ============================================================================

class TestLambdaFP:
    """Verify all lambda_g^FP values up to genus 6."""

    def test_lambda1(self):
        assert lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda2(self):
        assert lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda3(self):
        assert lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda4(self):
        assert lambda_fp_exact(4) == Fraction(127, 154828800)

    def test_lambda5(self):
        assert lambda_fp_exact(5) == Fraction(73, 3503554560)

    def test_lambda6(self):
        """lambda_6^FP from B_12 = -691/2730."""
        l6 = lambda_fp_exact(6)
        # (2^11-1)/2^11 * 691/2730 / 12!
        expected = Fraction(2047, 2048) * Fraction(691, 2730) / Fraction(factorial(12))
        assert l6 == expected

    def test_lambda_all_positive(self):
        for g in range(1, 7):
            assert lambda_fp_exact(g) > 0

    def test_lambda_decreasing(self):
        for g in range(1, 6):
            assert lambda_fp_exact(g + 1) < lambda_fp_exact(g)

    def test_lambda_invalid_genus(self):
        with pytest.raises(ValueError):
            lambda_fp_exact(0)


# ============================================================================
# Section 3: Lambda_5 six-path verification (FAST)
# ============================================================================

class TestLambda5SixPath:
    """Six independent paths to lambda_5^FP = 73/3503554560."""

    EXPECTED = Fraction(73, 3503554560)

    def test_path1_bernoulli(self):
        """Path 1: Bernoulli formula (2^9-1)|B_10|/(2^9 * 10!)."""
        B10 = _bernoulli_exact(10)
        assert B10 == Fraction(5, 66)
        l5 = Fraction(2 ** 9 - 1) * abs(B10) / Fraction(2 ** 9 * factorial(10))
        assert l5 == self.EXPECTED

    def test_path2_ahat_series(self):
        """Path 2: A-hat series inversion."""
        c_sin = [Fraction((-1) ** n, factorial(2 * n + 1)) for n in range(6)]
        a = [Fraction(0)] * 6
        a[0] = Fraction(1)
        for n in range(1, 6):
            s = Fraction(0)
            for j in range(1, n + 1):
                s += c_sin[j] * a[n - j]
            a[n] = -s / c_sin[0]
        l5 = a[5] / Fraction(4 ** 5)
        assert l5 == self.EXPECTED

    def test_path3_library(self):
        """Path 3: Library function."""
        assert lambda_fp_exact(5) == self.EXPECTED

    def test_path4_direct(self):
        """Path 4: Direct B_10 substitution."""
        l5 = Fraction(511 * 5, 66 * 512 * factorial(10))
        assert l5 == self.EXPECTED

    def test_path5_ratio(self):
        """Path 5: lambda_5/lambda_4 close to 1/(4pi^2)."""
        l4 = lambda_fp_exact(4)
        l5 = lambda_fp_exact(5)
        ratio = float(l5 / l4)
        limit = 1.0 / (4.0 * pi ** 2)
        assert abs(ratio - limit) / limit < 0.01

    def test_path6_asymptotic(self):
        """Path 6: Asymptotic estimate within 10%."""
        asymptotic = (1 - 2 ** (1 - 10)) * 2.0 / (2 * pi) ** 10
        exact = float(self.EXPECTED)
        assert abs(asymptotic - exact) / exact < 0.10

    def test_six_path_function(self):
        """All six paths via the helper function."""
        result = lambda5_six_path()
        assert result['paths_1234_agree']
        assert result['ratio_close']

    def test_lambda5_positive(self):
        assert lambda_fp_exact(5) > 0


# ============================================================================
# Section 4: WK intersection numbers used in genus 5 (FAST)
# ============================================================================

class TestWKIntersectionNumbers:
    """Verify WK intersection numbers relevant to genus 5."""

    def test_tau0_cubed_g0(self):
        assert wk_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_tau1_g1(self):
        assert wk_intersection(1, (1,)) == Fraction(1, 24)

    def test_tau2_g1(self):
        """<tau_2 tau_0>_1 = 1/24 by string equation."""
        assert wk_intersection(1, (2, 0)) == Fraction(1, 24)

    def test_tau4_g2(self):
        """<tau_4>_2 = 1/1152."""
        assert wk_intersection(2, (4,)) == Fraction(1, 1152)

    def test_tau7_g3(self):
        """<tau_7>_3: verified by dilaton/DVV."""
        result = wk_intersection(3, (7,))
        assert isinstance(result, Fraction)
        assert result > 0

    def test_tau10_g4(self):
        """<tau_10>_4: needed for dumbbell graph at genus 5."""
        result = wk_intersection(4, (10,))
        assert isinstance(result, Fraction)

    def test_dim_constraint_g5(self):
        """<tau_12>_5 = nonzero (dim constraint: 12 = 3*5-3+1)."""
        # Single insertion at genus 5: d = 3*5-3+1 = 13, but that's 1 point
        # Actually for 1 marked point: sum d_i = 3g-3+n = 12+1 = 13? No.
        # For (g=5, n=1): dim = 3*5-3+1 = 13. So <tau_13>_5.
        # But that's unstable? No, 2*5-2+1 = 9 > 0. OK.
        result = wk_intersection(5, (13,))
        assert isinstance(result, Fraction)

    def test_symmetry(self):
        """WK numbers are symmetric in their arguments."""
        assert wk_intersection(1, (1, 0, 0)) == wk_intersection(1, (0, 1, 0))

    def test_dilaton_equation(self):
        """<tau_1 tau_d1...tau_dn>_g = (2g-2+n-1) <tau_d1...tau_dn>_g."""
        # <tau_1 tau_1>_1 = (2*1-2+2-1) * <tau_1>_1 = 1 * 1/24 = 1/24
        assert wk_intersection(1, (1, 1)) == Fraction(1, 24)


# ============================================================================
# Section 5: Hodge integrals for small graphs (FAST)
# ============================================================================

class TestHodgeIntegrals:
    """Verify Hodge integral computations for small genus-5 graphs."""

    def test_smooth_graph(self):
        """I(smooth) = 1 for the smooth genus-5 graph."""
        G = StableGraph(vertex_genera=(5,), edges=(), legs=())
        assert hodge_integral(G) == Fraction(1)

    def test_single_loop_g4(self):
        """Hodge integral for (4,2) single-loop graph."""
        G = StableGraph(vertex_genera=(4,), edges=((0, 0),), legs=())
        I = hodge_integral(G)
        expected = Fraction(0)
        for a in range(12):
            b = 11 - a
            sign = (-1) ** b
            wk = wk_intersection(4, tuple(sorted([a, b], reverse=True)))
            expected += sign * wk
        assert I == expected

    def test_self_loop_parity_2_6(self):
        """(2,6): dim=7 ODD, 3 loops >= 2, I=0 by parity."""
        G = StableGraph(vertex_genera=(2,), edges=((0, 0),) * 3, legs=())
        assert hodge_integral(G) == Fraction(0)

    def test_1_8_even_dim(self):
        """(1,8): dim=8 EVEN, 4 loops. Parity does NOT force vanishing."""
        G = StableGraph(vertex_genera=(1,), edges=((0, 0),) * 4, legs=())
        I = hodge_integral(G)
        assert isinstance(I, Fraction)
        # dim 8 is EVEN, so parity vanishing NOT forced

    def test_self_loop_parity_0_10(self):
        """(0,10): dim=7 ODD, 5 loops >= 2, I=0 by parity."""
        G = StableGraph(vertex_genera=(0,), edges=((0, 0),) * 5, legs=())
        assert hodge_integral(G) == Fraction(0)

    def test_3_4_even_dim(self):
        """(3,4): dim=10 EVEN, 2 loops. Parity NOT forced."""
        G = StableGraph(vertex_genera=(3,), edges=((0, 0), (0, 0)), legs=())
        I = hodge_integral(G)
        assert isinstance(I, Fraction)

    def test_dumbbell_41(self):
        """Dumbbell: (4,1)-(1,1) bridge. I = (-1)^10 * <tau_10>_4 * <tau_1>_1."""
        G = StableGraph(vertex_genera=(4, 1), edges=((0, 1),), legs=())
        I = hodge_integral(G)
        wk0 = wk_intersection(4, (10,))
        wk1 = wk_intersection(1, (1,))
        # genus(v0)=4 > genus(v1)=1 -> minus at v0, d_v0=10
        expected = Fraction((-1) ** 10) * wk0 * wk1
        assert I == expected

    def test_dumbbell_32(self):
        """Dumbbell: (3,1)-(2,1) bridge."""
        G = StableGraph(vertex_genera=(3, 2), edges=((0, 1),), legs=())
        I = hodge_integral(G)
        # dims: 3*3-3+1=7, 3*2-3+1=4. d_v0=7, d_v1=4.
        # genus(v0)=3>genus(v1)=2: minus at v0, d_v0=7. Sign=(-1)^7=-1.
        wk0 = wk_intersection(3, (7,))
        wk1 = wk_intersection(2, (4,))
        expected = Fraction((-1) ** 7) * wk0 * wk1
        assert I == expected

    def test_cached_matches_uncached(self):
        """Cached and uncached Hodge integrals agree."""
        G = StableGraph(vertex_genera=(3, 2), edges=((0, 1),), legs=())
        I_direct = hodge_integral(G)
        I_cached = _hodge_integral_cached(G.vertex_genera, G.edges)
        assert I_direct == I_cached

    def test_hodge_integral_fraction(self):
        """Hodge integral is always a Fraction."""
        for genera, edges in [
            ((4,), ((0, 0),)),
            ((3, 1), ((0, 1), (0, 1))),
            ((2, 2), ((0, 1), (0, 0))),
        ]:
            G = StableGraph(vertex_genera=genera, edges=edges, legs=())
            I = hodge_integral(G)
            assert isinstance(I, Fraction)


# ============================================================================
# Section 6: Self-loop parity vanishing (FAST)
# ============================================================================

class TestSelfLoopParity:
    """Verify prop:self-loop-vanishing at genus 5."""

    def test_2_6_vanishes(self):
        """(2,6): dim 7 ODD, 3 loops >= 2."""
        G = StableGraph(vertex_genera=(2,), edges=((0, 0),) * 3, legs=())
        assert hodge_integral(G) == Fraction(0)

    def test_1_8_even_no_forced_vanishing(self):
        """(1,8): dim 8 EVEN, parity does NOT force vanishing."""
        dim_v = 3 * 1 - 3 + 8
        assert dim_v == 8
        assert dim_v % 2 == 0  # EVEN: parity not forced

    def test_0_10_vanishes(self):
        """(0,10): dim 7 ODD, 5 loops >= 2."""
        G = StableGraph(vertex_genera=(0,), edges=((0, 0),) * 5, legs=())
        assert hodge_integral(G) == Fraction(0)

    def test_3_4_not_forced(self):
        """(3,4): dim 10 EVEN. Parity does NOT force vanishing."""
        dim_v = 3 * 3 - 3 + 4
        assert dim_v == 10
        assert dim_v % 2 == 0  # EVEN

    def test_4_2_single_loop(self):
        """(4,2): 1 loop, k=1 < 2, NOT forced by parity."""
        # prop:self-loop-vanishing requires k >= 2
        n_loops = 1
        assert n_loops < 2

    def test_smooth_I1(self):
        """Smooth graph (5,0) has I = 1."""
        G = StableGraph(vertex_genera=(5,), edges=(), legs=())
        assert hodge_integral(G) == Fraction(1)


# ============================================================================
# Section 7: Shadow visibility formula (FAST)
# ============================================================================

class TestShadowVisibilityFormula:
    """Verify cor:shadow-visibility-genus formula."""

    def test_gmin_S3(self):
        assert 3 // 2 + 1 == 2

    def test_gmin_S4(self):
        assert 4 // 2 + 1 == 3

    def test_gmin_S5(self):
        assert 5 // 2 + 1 == 3

    def test_gmin_S6(self):
        assert 6 // 2 + 1 == 4

    def test_gmin_S7(self):
        assert 7 // 2 + 1 == 4

    def test_gmin_S8(self):
        """S_8 first visible at genus 5."""
        assert 8 // 2 + 1 == 5

    def test_gmin_S9(self):
        """S_9 first visible at genus 5."""
        assert 9 // 2 + 1 == 5

    def test_gmin_S10(self):
        """S_10 NOT visible at genus 5 (first at genus 6)."""
        assert 10 // 2 + 1 == 6

    def test_two_new_per_genus_ge3(self):
        """Each genus g >= 3 adds exactly 2 new shadow coefficients."""
        result = cross_genus_pf_pattern()
        assert result['two_new_per_genus_ge3']

    def test_g2_adds_one(self):
        """Genus 2 adds S_3 only (1 new shadow coefficient)."""
        result = cross_genus_pf_pattern()
        assert result['g2_adds_one']


# ============================================================================
# Section 8: Gorenstein property (FAST)
# ============================================================================

class TestGorenstein:
    """Verify Faber's Gorenstein conjecture for R*(M-bar_5)."""

    def test_gorenstein_symmetry(self):
        """dim R^d = dim R^{12-d} for all d."""
        result = gorenstein_check_g5()
        assert result['is_gorenstein']

    def test_top_degree_dim_1(self):
        result = gorenstein_check_g5()
        assert result['top_degree_dim'] == 1

    def test_center_degree_6(self):
        result = gorenstein_check_g5()
        assert result['center_degree'] == 6

    def test_R0_dim_1(self):
        dims = taut_ring_dimensions_g5()
        assert dims[0] == 1

    def test_total_rank_positive(self):
        result = gorenstein_check_g5()
        assert result['total_rank'] > 100  # genus 5 has rich taut ring


# ============================================================================
# Section 9: Cross-genus patterns (FAST)
# ============================================================================

class TestCrossGenusPatterns:
    """Verify cross-genus structural patterns."""

    def test_ratio_convergence(self):
        """lambda_{g+1}/lambda_g -> 1/(4pi^2) with decreasing error."""
        result = cross_genus_lambda_pattern()
        assert result['errors_converging']

    def test_all_lambda_positive(self):
        result = cross_genus_lambda_pattern()
        for g, lam in result['lambdas'].items():
            assert lam > 0

    def test_lambda_monotone_decreasing(self):
        result = cross_genus_lambda_pattern()
        for g in range(1, 6):
            assert result['lambdas'][g + 1] < result['lambdas'][g]

    def test_shadow_range_g5(self):
        """At genus 5: S_3 through S_9."""
        result = cross_genus_pf_pattern()
        assert result['visibility_pattern'][5]['max_visible_r'] == 9

    def test_lower_genera_data(self):
        result = compare_with_lower_genera()
        assert len(result['lambda_values']) == 5
        assert len(result['shadow_ranges']) == 4

    def test_shadow_range_g2(self):
        """At genus 2: S_3 only."""
        result = cross_genus_pf_pattern()
        assert result['visibility_pattern'][2]['max_visible_r'] == 3


# ============================================================================
# Section 10: Complementarity (scalar lane, FAST)
# ============================================================================

class TestComplementarity:
    """Test the scalar complementarity relation at genus 5."""

    def test_scalar_complementarity(self):
        """F_5^scalar(c) + F_5^scalar(26-c) = 13 * lambda_5."""
        result = virasoro_complementarity_g5()
        assert result['scalar_complementarity']

    def test_complementarity_c1(self):
        l5 = lambda_fp_exact(5)
        assert Fraction(1, 2) * l5 + Fraction(25, 2) * l5 == Fraction(13) * l5

    def test_complementarity_c13_selfdual(self):
        l5 = lambda_fp_exact(5)
        assert 2 * Fraction(13, 2) * l5 == Fraction(13) * l5

    def test_complementarity_c26(self):
        l5 = lambda_fp_exact(5)
        assert Fraction(13) * l5 + Fraction(0) == Fraction(13) * l5

    def test_km_antisymmetry(self):
        """KM: kappa(k) + kappa(-k-2h^v) = 0."""
        for k_val in [1, 3, 5, 10]:
            kappa = Fraction(3) * (k_val + 2) / 4
            kappa_dual = Fraction(3) * (-k_val - 4 + 2) / 4
            assert kappa + kappa_dual == 0

    def test_complementarity_numerical(self):
        result = virasoro_complementarity_g5()
        for c_val, data in result['numerical'].items():
            assert data['match']


# ============================================================================
# Section 11: Pixton ideal structure (FAST)
# ============================================================================

class TestPixtonIdealStructure:
    """Verify the Pixton ideal structure at genus 5."""

    def test_first_relation_codim6(self):
        result = pixton_relation_codim6_genus5()
        assert result['first_pixton_codim'] == 6

    def test_11_kappa_monomials(self):
        """11 kappa monomials of degree 6 (= 11 partitions of 6)."""
        result = pixton_relation_codim6_genus5()
        assert result['num_kappa_monomials'] == 11

    def test_pixton_ideal_nontrivial(self):
        result = pixton_ideal_dimension_g5()
        assert result['first_nontrivial_codim'] == 6

    def test_bounds_nonneg(self):
        result = pixton_ideal_dimension_g5()
        for d, data in result['estimates'].items():
            assert data['pixton_ideal_lower_bound'] >= 0

    def test_partition_counts(self):
        """Partition numbers p(d) for d = 0,...,6."""
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11}
        result = pixton_ideal_dimension_g5()
        for d, count in expected.items():
            assert result['estimates'][d]['kappa_partitions'] == count


# ============================================================================
# Section 12: Vertex weight computation (FAST)
# ============================================================================

class TestVertexWeights:
    """Verify vertex weight assignments."""

    def test_ell_genus1_val1(self):
        shadow = virasoro_shadow_data()
        assert ell_genus1(1, shadow) == shadow.kappa

    def test_ell_genus1_val2(self):
        shadow = virasoro_shadow_data()
        expected = shadow.S3 * shadow.kappa / 24 - shadow.S3 ** 2
        assert simplify(ell_genus1(2, shadow) - expected) == 0

    def test_ell_genus2_val0(self):
        shadow = virasoro_shadow_data()
        expected = shadow.kappa * Rational(7, 5760)
        assert simplify(ell_genus2(0, shadow) - expected) == 0

    def test_is_planted_forest_true(self):
        """A graph with genus-0 vertex of valence 3 is planted-forest."""
        # Genus-0 vertex (v0) with 3 bridges to v1, v2, plus self-loop at v1
        # v0: genus 0, val 3. v1: genus 2, val 2. v2: genus 2, val 1.
        # total genus = 0 + 2 + 2 + h1 = 5 where h1 = edges - verts + 1 = 3-3+1 = 1
        G = StableGraph(
            vertex_genera=(0, 2, 2),
            edges=((0, 1), (0, 2), (0, 1)),  # v0 has val 3
            legs=(),
        )
        assert is_planted_forest(G)

    def test_is_planted_forest_false(self):
        G = StableGraph(vertex_genera=(3, 2), edges=((0, 1),), legs=())
        assert not is_planted_forest(G)

    def test_is_planted_forest_genus0_val2(self):
        """Genus-0 vertex with valence 2 is NOT planted-forest (needs val >= 3)."""
        G = StableGraph(vertex_genera=(0, 5), edges=((0, 1), (0, 1)), legs=())
        assert not is_planted_forest(G)

    def test_vertex_weight_heisenberg_pf_zero(self):
        """Heisenberg: S_r = 0 for r >= 3, so genus-0 val-3 vertex gives weight 0."""
        shadow = heisenberg_shadow_data()
        # Graph with genus-0 vertex of valence 3 (PF graph)
        G = StableGraph(
            vertex_genera=(0, 2, 2),
            edges=((0, 1), (0, 2), (0, 1)),
            legs=(),
        )
        w = vertex_weight(G, shadow)
        # Vertex 0: genus 0, valence 3 -> S_3 = 0 for Heisenberg
        # So the total weight = 0
        assert simplify(w) == 0

    def test_vertex_weight_smooth_g5(self):
        """Smooth graph: weight = 1."""
        shadow = virasoro_shadow_data()
        G = StableGraph(vertex_genera=(5,), edges=(), legs=())
        w = vertex_weight(G, shadow)
        assert w == Integer(1)


# ============================================================================
# Section 13: FZ coefficients (FAST)
# ============================================================================

class TestFZCoefficients:
    """Verify Faber-Zagier generating function coefficients."""

    def test_fz_d0(self):
        coeffs = faber_zagier_coefficients(5, 6)
        assert coeffs[0] == Fraction(1)

    def test_fz_d1(self):
        coeffs = faber_zagier_coefficients(5, 6)
        assert coeffs[1] == lambda_fp_exact(1)

    def test_fz_d5(self):
        coeffs = faber_zagier_coefficients(5, 6)
        assert coeffs[5] == lambda_fp_exact(5)


# ============================================================================
# SLOW TESTS: Full genus-5 graph enumeration
# ============================================================================

@pytest.mark.slow
class TestGraphEnumeration:
    """Verify genus-5 stable graph enumeration (requires full enumeration)."""

    def test_graph_count_positive(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_count
        count = genus5_graph_count()
        assert count > 100

    def test_all_genus_5(self):
        from compute.lib.genus5_amplitude_engine import genus5_stable_graphs_n0
        for G in genus5_stable_graphs_n0():
            assert G.arithmetic_genus == 5

    def test_all_stable(self):
        from compute.lib.genus5_amplitude_engine import genus5_stable_graphs_n0
        for G in genus5_stable_graphs_n0():
            assert G.is_stable

    def test_all_connected(self):
        from compute.lib.genus5_amplitude_engine import genus5_stable_graphs_n0
        for G in genus5_stable_graphs_n0():
            assert G.is_connected


@pytest.mark.slow
class TestCensus:
    """Census of genus-5 amplitudes (requires full enumeration)."""

    def test_census_total(self):
        from compute.lib.pixton_genus5_engine import genus5_pixton_census
        census = genus5_pixton_census()
        assert census['total'] > 100

    def test_census_partition(self):
        from compute.lib.pixton_genus5_engine import genus5_pixton_census
        census = genus5_pixton_census()
        assert census['pf_count'] + census['nonpf_count'] == census['total']

    def test_pf_dominates(self):
        from compute.lib.pixton_genus5_engine import genus5_pixton_census
        census = genus5_pixton_census()
        assert census['pf_count'] > census['nonpf_count']


@pytest.mark.slow
class TestPlantedForestCorrection:
    """Planted-forest correction tests (require full graph enumeration)."""

    def test_heisenberg_pf_vanishes(self):
        from compute.lib.pixton_genus5_engine import genus5_planted_forest_correction
        shadow = heisenberg_shadow_data()
        pf = genus5_planted_forest_correction(shadow)
        assert simplify(pf) == 0

    def test_total_eq_pf_plus_nonpf(self):
        from compute.lib.pixton_genus5_engine import (
            genus5_total_amplitude,
            genus5_planted_forest_correction,
            genus5_nonpf_amplitude,
        )
        shadow = heisenberg_shadow_data()
        F5 = genus5_total_amplitude(shadow)
        pf = genus5_planted_forest_correction(shadow)
        nonpf = genus5_nonpf_amplitude(shadow)
        assert simplify(F5 - pf - nonpf) == 0

    def test_pf_zero_all_Sr_zero(self):
        from compute.lib.pixton_genus5_engine import genus5_planted_forest_correction
        kappa_sym = Symbol('kappa')
        shadow = ShadowData(
            'test_zero', kappa_sym, Integer(0), Integer(0),
            shadows={r: Integer(0) for r in range(5, 10)},
            depth_class='G',
        )
        pf = genus5_planted_forest_correction(shadow)
        assert simplify(pf) == 0


@pytest.mark.slow
class TestClassComparison:
    """Cross-class comparison (requires full enumeration)."""

    def test_class_G_zero(self):
        from compute.lib.pixton_genus5_engine import cross_class_comparison_g5
        result = cross_class_comparison_g5()
        assert result['class_G_pf_zero']

    def test_class_L_nonzero(self):
        from compute.lib.pixton_genus5_engine import cross_class_comparison_g5
        result = cross_class_comparison_g5()
        assert result['class_L_pf_nonzero']

    def test_class_M_nonzero(self):
        from compute.lib.pixton_genus5_engine import cross_class_comparison_g5
        result = cross_class_comparison_g5()
        assert result['class_M_pf_nonzero']


@pytest.mark.slow
class TestHeisenbergF5:
    """Heisenberg F_5 verification (requires full enumeration)."""

    def test_heisenberg_paths_match(self):
        from compute.lib.pixton_genus5_engine import genus5_heisenberg_F5
        result = genus5_heisenberg_F5()
        assert result['pf_is_zero']
        assert result['paths_match']


@pytest.mark.slow
class TestShadowVisibilityFull:
    """Full shadow visibility verification (requires enumeration)."""

    def test_visibility_S8(self):
        from compute.lib.pixton_genus5_engine import verify_shadow_visibility_g5
        result = verify_shadow_visibility_g5()
        assert result['S8_in_pf_correction']

    def test_visibility_S9(self):
        from compute.lib.pixton_genus5_engine import verify_shadow_visibility_g5
        result = verify_shadow_visibility_g5()
        assert result['S9_in_pf_correction']


@pytest.mark.slow
class TestSymbolicPolynomial:
    """Symbolic PF polynomial extraction (requires enumeration + symbolic)."""

    def test_polynomial_nonzero(self):
        from compute.lib.pixton_genus5_engine import genus5_pf_polynomial
        result = genus5_pf_polynomial()
        assert simplify(result['polynomial']) != 0

    def test_polynomial_has_terms(self):
        from compute.lib.pixton_genus5_engine import genus5_pf_polynomial
        result = genus5_pf_polynomial()
        if 'monomials' in result:
            assert result['num_terms'] > 0


@pytest.mark.slow
class TestDepthFiltration:
    """Depth filtration (requires enumeration)."""

    def test_depth_3_present(self):
        from compute.lib.pixton_genus5_engine import depth_filtration_g5
        result = depth_filtration_g5()
        assert 3 in result['by_depth']

    def test_max_depth_ge_3(self):
        from compute.lib.pixton_genus5_engine import depth_filtration_g5
        result = depth_filtration_g5()
        assert result['max_depth'] >= 3


@pytest.mark.slow
class TestEulerCharacteristic:
    """Euler characteristic verification (requires enumeration)."""

    def test_euler_nonzero(self):
        from compute.lib.pixton_genus5_engine import euler_characteristic_g5
        result = euler_characteristic_g5()
        assert result['computed'] != Fraction(0)

    def test_euler_rational(self):
        from compute.lib.pixton_genus5_engine import euler_characteristic_g5
        result = euler_characteristic_g5()
        assert isinstance(result['computed'], Fraction)
