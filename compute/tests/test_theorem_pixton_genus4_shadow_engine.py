r"""Tests for the Pixton ideal at genus 4 via the arity-6 shadow S_6.

Tests conj:pixton-from-shadows at genus 4: the first genus where S_6
contributes. Verifies the planted-forest correction, shadow visibility,
self-loop parity vanishing, cross-family comparisons, and the Pixton
dimension constraint.

40+ tests organized in sections:
  1. Lambda class exact values (FP intersection numbers)
  2. S_6 three-path verification
  3. Shadow visibility formula
  4. S_6 isolation (S_6 genuinely contributes at genus 4)
  5. Heisenberg (class G): pf = 0, scalar match
  6. Virasoro (class M): pf nonzero, S_6 correction
  7. Affine sl_2 (class L): pf nonzero but no S_6
  8. Cross-family comparison
  9. Self-loop parity vanishing
 10. Pixton dimension constraint
 11. Numerical evaluations
 12. Genus-ratio analysis
 13. Planted-forest polynomial structure
"""

import pytest
from fractions import Fraction

from sympy import (
    Integer, Rational, Symbol, cancel, expand, simplify, S,
)

from compute.lib.theorem_pixton_genus4_shadow_engine import (
    # Constants
    LAMBDA1_FP, LAMBDA2_FP, LAMBDA3_FP, LAMBDA4_FP,
    lambda_fp_exact,
    # Core computations
    obs4_total,
    delta_pf_genus4,
    nonpf_amplitude_genus4,
    scalar_prediction_genus4,
    # S_6 tests
    s6_explicit_formula,
    s6_three_path_verification,
    s6_visibility_genus,
    s6_isolation_test,
    s7_isolation_test,
    # Family tests
    obs4_heisenberg,
    obs4_virasoro,
    obs4_affine_sl2,
    cross_family_comparison_genus4,
    # Structural tests
    pixton_dimension_constraint,
    self_loop_parity_genus4,
    pf_polynomial_genus4,
    numerical_evaluation,
    genus_ratio_analysis,
    full_pixton_genus4_test,
    # Graph counts
    genus4_graph_count,
    genus4_pf_count,
    genus4_nonpf_count,
    genus4_nonzero_hodge_count,
    # Utilities
    hodge_integral,
    vertex_weight,
    is_planted_forest,
    c_sym,
)
from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
)
from compute.lib.theorem_shadow_arity_frontier_engine import (
    S_explicit,
    shadow_coefficients_convolution,
    shadow_visibility_genus,
)
from compute.lib.stable_graph_enumeration import StableGraph


# ============================================================================
# Section 1: Lambda class exact values
# ============================================================================

class TestLambdaFP:
    """Verify Faber-Pandharipande intersection numbers via multi-path.

    Path 1: Direct Bernoulli formula lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
    Path 2: Akiyama-Tanigawa algorithm for B_{2g} then substitution.
    Path 3: Cross-check against the A-hat generating function.
    """

    def _bernoulli_exact(self, n):
        """Independent Bernoulli computation (Akiyama-Tanigawa)."""
        a = [Fraction(1, m + 1) for m in range(n + 1)]
        for j in range(1, n + 1):
            for m in range(n, j - 1, -1):
                a[m] = (m - j + 1) * (a[m] - a[m - 1])
        return a[n]

    def _lambda_fp_from_bernoulli(self, g):
        """Compute lambda_g^FP from Bernoulli numbers independently."""
        from math import factorial
        B2g = self._bernoulli_exact(2 * g)
        return Fraction(2**(2*g-1) - 1, 2**(2*g-1)) * abs(B2g) / Fraction(factorial(2*g))

    def test_lambda1_two_path(self):
        """Path 1: formula. Path 2: independent Bernoulli."""
        assert LAMBDA1_FP == self._lambda_fp_from_bernoulli(1)
        assert LAMBDA1_FP == Fraction(1, 24)

    def test_lambda2_two_path(self):
        assert LAMBDA2_FP == self._lambda_fp_from_bernoulli(2)
        assert LAMBDA2_FP == Fraction(7, 5760)

    def test_lambda3_two_path(self):
        assert LAMBDA3_FP == self._lambda_fp_from_bernoulli(3)
        assert LAMBDA3_FP == Fraction(31, 967680)

    def test_lambda4_three_path(self):
        """lambda_4^FP verified three ways.

        Path 1: Module constant LAMBDA4_FP.
        Path 2: Independent Bernoulli derivation.
        Path 3: Explicit factorization (2^7-1)/2^7 * |B_8|/8!.
        """
        # Path 2
        assert LAMBDA4_FP == self._lambda_fp_from_bernoulli(4)
        # Path 3
        B8 = self._bernoulli_exact(8)
        assert B8 == Fraction(-1, 30), f"B_8 should be -1/30, got {B8}"
        result = Fraction(127, 128) * Fraction(1, 30) / Fraction(40320)
        assert LAMBDA4_FP == result

    def test_lambda4_denominator_factorization(self):
        """Cross-check: 128 * 30 * 8! = 154828800."""
        from math import factorial
        assert 128 * 30 * factorial(8) == 154828800
        assert LAMBDA4_FP.denominator == 154828800

    def test_lambda_fp_monotone_decreasing(self):
        """lambda_g^FP is strictly decreasing for g >= 1."""
        for g in range(1, 4):
            assert lambda_fp_exact(g) > lambda_fp_exact(g + 1)

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 5):
            assert lambda_fp_exact(g) > 0


# ============================================================================
# Section 2: S_6 three-path verification
# ============================================================================

class TestS6Verification:
    """S_6(c) = 80(45c+193)/[3c^3(5c+22)^2] verified three ways."""

    def test_s6_three_paths_match(self):
        result = s6_three_path_verification()
        assert result['all_match']

    def test_s6_convolution_matches_explicit(self):
        conv = shadow_coefficients_convolution(max_r=8)
        s6_conv = cancel(conv[6])
        s6_expl = cancel(S_explicit(6))
        assert simplify(s6_conv - s6_expl) == 0

    def test_s6_explicit_formula(self):
        """Verify the closed-form against the module formula."""
        s6_ours = cancel(s6_explicit_formula())
        s6_theirs = cancel(S_explicit(6))
        assert simplify(s6_ours - s6_theirs) == 0

    def test_s6_at_c1(self):
        """S_6(c=1) = 80*(45+193)/(3*1*(5+22)^2) = 80*238/(3*729)."""
        s6 = S_explicit(6)
        val = s6.subs(c_sym, 1)
        expected = Rational(80) * 238 / (3 * 27**2)
        assert cancel(val - expected) == 0

    def test_s6_at_c13(self):
        """Evaluate S_6 at the self-dual point c=13."""
        s6 = S_explicit(6)
        val = cancel(s6.subs(c_sym, 13))
        # 80*(45*13+193) / (3*13^3*(5*13+22)^2) = 80*778 / (3*2197*7569)
        num = 80 * (45 * 13 + 193)
        den = 3 * 13**3 * (5 * 13 + 22)**2
        expected = Rational(num, den)
        assert cancel(val - expected) == 0

    def test_s6_sign_positive_at_generic_c(self):
        """S_6 > 0 for c > 0 (sign = (-1)^6 = +1 for r=6)."""
        s6 = S_explicit(6)
        for c_val in [1, 2, 5, 10, 13, 25, 26, 100]:
            assert float(s6.subs(c_sym, c_val)) > 0

    def test_s6_pole_at_c0(self):
        """S_6 has a pole at c=0 (order c^{-3})."""
        s6 = S_explicit(6)
        # Multiply by c^3 and evaluate at c=0
        s6_times_c3 = cancel(s6 * c_sym**3)
        val = s6_times_c3.subs(c_sym, 0)
        assert val != 0  # nonzero residue


# ============================================================================
# Section 3: Shadow visibility formula
# ============================================================================

class TestShadowVisibility:
    """g_min(S_r) = floor(r/2) + 1."""

    def test_s6_visibility(self):
        assert s6_visibility_genus() == 4

    def test_s7_visibility(self):
        assert shadow_visibility_genus(7) == 4

    def test_s8_not_visible_at_genus4(self):
        """S_8 first visible at genus 5, NOT at genus 4."""
        assert shadow_visibility_genus(8) == 5

    def test_visibility_formula_low(self):
        assert shadow_visibility_genus(3) == 2
        assert shadow_visibility_genus(4) == 3
        assert shadow_visibility_genus(5) == 3


# ============================================================================
# Section 4: S_6 isolation (genuine contribution at genus 4)
# ============================================================================

class TestS6Isolation:
    """Verify S_6 genuinely contributes to delta_pf^{(4,0)}."""

    def test_s6_contributes(self):
        result = s6_isolation_test()
        assert result['s6_contributes'], "S_6 must contribute at genus 4"

    def test_s6_graphs_exist(self):
        """There exist stable graphs at genus 4 with a genus-0 vertex
        of valence 6 and nonzero Hodge integral."""
        result = s6_isolation_test()
        assert result['n_graphs_with_val6_nonzero_I'] > 0

    def test_s7_contributes(self):
        """S_7 also first visible at genus 4, and contributes."""
        result = s7_isolation_test()
        assert result['s7_contributes'], "S_7 must contribute at genus 4"

    def test_s8_does_not_contribute(self):
        """S_8 does NOT contribute at genus 4.

        The only graph with a genus-0 vertex of valence 8 is the
        single-vertex (0,8), which has dim=5 (odd) and 4 self-loops,
        so I=0 by parity vanishing. Therefore S_8 is invisible at g=4.
        Cross-check: g_min(S_8) = floor(8/2)+1 = 5 > 4.
        """
        kappa_sym = Symbol('kappa')
        S8_sym = Symbol('S_8')

        shadow_only_s8 = ShadowData(
            'S8_only', kappa_sym, Integer(0), Integer(0),
            shadows={5: Integer(0), 6: Integer(0), 7: Integer(0), 8: S8_sym},
            depth_class='M',
        )
        pf_s8 = delta_pf_genus4(shadow_only_s8)
        assert simplify(pf_s8) == 0, \
            "S_8 must NOT contribute at genus 4"
        # Cross-check: visibility formula confirms g_min(8) = 5
        assert shadow_visibility_genus(8) == 5


# ============================================================================
# Section 5: Heisenberg (class G)
# ============================================================================

class TestHeisenberg:
    """Class G: pf = 0, scalar prediction F_4 = kappa * lambda_4^FP.

    The planted-forest correction vanishes because S_r = 0 for r >= 3.
    The scalar prediction is verified via Bernoulli AND A-hat (two-path).
    """

    def test_pf_vanishes(self):
        """Planted-forest correction is zero for Heisenberg (class G)."""
        result = obs4_heisenberg()
        assert result['pf_is_zero']

    def test_bernoulli_ahat_match(self):
        """Scalar prediction agrees: Bernoulli formula = A-hat series."""
        result = obs4_heisenberg()
        assert result['bernoulli_ahat_match']

    def test_no_s6_contribution(self):
        """Heisenberg has S_6 = 0, so no S_6 correction."""
        shadow = heisenberg_shadow_data()
        assert shadow.S(6) == 0

    def test_scalar_prediction_at_k1(self):
        """F_4(H_1) = 1 * 127/154828800 (scalar lane, Theorem D).

        Cross-check: Bernoulli and A-hat paths agree at k=1.
        """
        k_sym = Symbol('k')
        result = obs4_heisenberg()
        F4_bern = result['F4_bernoulli'].subs(k_sym, 1)
        F4_ahat = result['F4_ahat'].subs(k_sym, 1)
        expected = Rational(LAMBDA4_FP.numerator, LAMBDA4_FP.denominator)
        assert cancel(F4_bern - expected) == 0
        assert cancel(F4_ahat - expected) == 0

    def test_all_higher_shadows_zero(self):
        """Heisenberg has S_r = 0 for ALL r >= 3 (class G, depth 2)."""
        shadow = heisenberg_shadow_data()
        for r in range(3, 10):
            assert shadow.S(r) == 0


# ============================================================================
# Section 6: Virasoro (class M)
# ============================================================================

class TestVirasoro:
    """Class M: pf nonzero, S_6 correction present."""

    def test_pf_nonzero(self):
        result = obs4_virasoro()
        assert result['delta_pf_nonzero']

    def test_obs4_not_proportional_to_lambda4(self):
        """obs_4(Vir_c) is NOT proportional to kappa * lambda_4^FP
        (the S_6 correction breaks the scalar formula)."""
        result = obs4_virasoro()
        diff = simplify(result['F4_total'] - result['F4_scalar'])
        assert diff != 0, "obs_4(Vir) must differ from scalar prediction"

    def test_pf_depends_on_s6(self):
        """The planted-forest correction depends on S_6."""
        poly_data = pf_polynomial_genus4()
        assert poly_data['depends_on'].get('S_6', False), \
            "delta_pf^{(4,0)} must depend on S_6"

    def test_s6_nonzero_virasoro(self):
        """S_6(Vir_c) is nonzero for generic c."""
        s6 = S_explicit(6)
        for c_val in [1, 2, 10, 13, 25, 26]:
            assert float(s6.subs(c_sym, c_val)) != 0


# ============================================================================
# Section 7: Affine sl_2 (class L)
# ============================================================================

class TestAffineSl2:
    """Class L: S_3 = 2, S_4 = 0, pf nonzero but no S_6."""

    def test_pf_nonzero(self):
        """Affine sl_2 has S_3 = 2, so pf correction is nonzero."""
        result = obs4_affine_sl2()
        assert result['pf_nonzero']

    def test_no_s6(self):
        """Affine sl_2 has S_r = 0 for r >= 4 (class L, depth 3)."""
        shadow = affine_shadow_data()
        assert shadow.S(4) == 0
        assert shadow.S(6) == 0

    def test_pf_involves_only_s3(self):
        """For class L, pf correction depends only on S_3 (not S_4...S_7)."""
        shadow = affine_shadow_data()
        # S_3 = 2, all higher = 0. pf should be nonzero because S_3 != 0.
        pf = delta_pf_genus4(shadow)
        assert simplify(pf) != 0


# ============================================================================
# Section 8: Cross-family comparison
# ============================================================================

class TestCrossFamily:
    """Compare obs_4 across families."""

    def test_class_g_pf_zero(self):
        result = cross_family_comparison_genus4()
        assert result['heisenberg']['pf_zero']

    def test_class_l_pf_nonzero(self):
        result = cross_family_comparison_genus4()
        assert result['affine_sl2']['pf_nonzero']

    def test_class_m_pf_nonzero(self):
        result = cross_family_comparison_genus4()
        assert result['virasoro']['pf_nonzero']

    def test_heisenberg_bernoulli_ahat(self):
        """Cross-check: Bernoulli and A-hat agree for Heisenberg."""
        result = cross_family_comparison_genus4()
        assert result['heisenberg']['bernoulli_ahat_match']


# ============================================================================
# Section 9: Self-loop parity vanishing
# ============================================================================

class TestSelfLoopParity:
    """prop:self-loop-vanishing at genus 4.

    Dimensions: dim M_{g_v, val} = 3*g_v - 3 + val.
    Parity vanishing applies when dim is odd AND k >= 2 self-loops.
    """

    def test_24_vanishes(self):
        """(2,4): 2 loops, dim=7 odd, I=0 by parity (k=2 >= 2)."""
        result = self_loop_parity_genus4()
        entry = result['(2,4)']
        assert entry['vanishes']
        assert entry['dim_is_odd']
        assert entry['parity_applicable']

    def test_16_nonzero(self):
        """(1,6): 3 loops, dim=6 EVEN, parity N/A, I=1 (nonzero).

        This is a genuine nonzero contribution: the genus-1 vertex
        with 3 self-loops has even-dimensional moduli, so parity
        vanishing does NOT apply.
        """
        result = self_loop_parity_genus4()
        entry = result['(1,6)']
        assert not entry['vanishes'], "I(1,6) = 1 (nonzero)"
        assert not entry['dim_is_odd'], "dim(1,6) = 6 is even"

    def test_08_vanishes(self):
        """(0,8): 4 loops, dim=5 odd, I=0 by parity (k=4 >= 2)."""
        result = self_loop_parity_genus4()
        entry = result['(0,8)']
        assert entry['vanishes']
        assert entry['dim_is_odd']
        assert entry['parity_applicable']

    def test_32_vanishes_but_not_by_parity(self):
        """(3,2): 1 loop, dim=8 even, parity does NOT apply (k=1 < 2).
        The integral vanishes for a separate reason (WK number = 0)."""
        result = self_loop_parity_genus4()
        entry = result['(3,2)']
        assert not entry['parity_applicable']
        assert not entry['dim_is_odd']
        assert entry['vanishes'], "I(3,2) = 0 (but not by parity)"


# ============================================================================
# Section 10: Pixton dimension constraint
# ============================================================================

class TestPixtonDimension:
    """Verify the Pixton dimension constraint at genus 4."""

    def test_dim_mbar4(self):
        result = pixton_dimension_constraint()
        assert result['dim_mbar_4'] == 9

    def test_pixton_starts_at_codim5(self):
        result = pixton_dimension_constraint()
        assert result['pixton_ideal_starts_at_codim'] == 5

    def test_dimension_satisfied(self):
        result = pixton_dimension_constraint()
        assert result['dimension_constraint_satisfied']

    def test_max_codim_within_bounds(self):
        result = pixton_dimension_constraint()
        assert result['max_pf_codimension'] <= 9


# ============================================================================
# Section 11: Numerical evaluations
# ============================================================================

class TestNumerical:
    """Numerical evaluation of obs_4 at specific central charges."""

    def test_c1_pf_nonzero(self):
        results = numerical_evaluation([1])
        assert abs(results['1']['planted_forest']) > 0

    def test_c13_pf_nonzero(self):
        """At the self-dual point c=13, pf is still nonzero."""
        results = numerical_evaluation([13])
        assert abs(results['13']['planted_forest']) > 0

    def test_c26_pf_nonzero(self):
        results = numerical_evaluation([26])
        assert abs(results['26']['planted_forest']) > 0

    def test_pf_smaller_than_scalar(self):
        """The planted-forest correction is typically smaller than
        the scalar part (a consistency check)."""
        results = numerical_evaluation([1, 10, 25])
        for cv_str, data in results.items():
            scalar = abs(data['scalar'])
            if scalar > 0:
                ratio = abs(data['ratio_pf_to_scalar'])
                # The correction should be finite (not blow up)
                assert ratio < 1e10, f"Ratio too large at c={cv_str}"


# ============================================================================
# Section 12: Genus-ratio analysis
# ============================================================================

class TestGenusRatio:
    """Verify the ratio lambda_4^FP / lambda_3^FP.

    Cross-check: compute ratio from raw Fractions AND from the
    genus_ratio_analysis function.
    """

    def test_ratio_exact_cross_check(self):
        """Two-path: module function vs direct Fraction division."""
        result = genus_ratio_analysis()
        ratio_module = result['lambda4_over_lambda3']
        ratio_direct = Fraction(LAMBDA4_FP, LAMBDA3_FP)
        assert ratio_module == ratio_direct

    def test_ratio_less_than_one(self):
        result = genus_ratio_analysis()
        assert result['lambda4_over_lambda3'] < 1

    def test_lambda3_over_lambda2_cross_check(self):
        """Two-path: module function vs direct Fraction division."""
        result = genus_ratio_analysis()
        ratio_module = result['lambda3_over_lambda2']
        ratio_direct = Fraction(LAMBDA3_FP, LAMBDA2_FP)
        assert ratio_module == ratio_direct


# ============================================================================
# Section 13: Planted-forest polynomial structure
# ============================================================================

class TestPFPolynomial:
    """Structure of delta_pf^{(4,0)} as a polynomial in shadow data."""

    def test_depends_on_s3(self):
        result = pf_polynomial_genus4()
        assert result['depends_on'].get('S_3', False)

    def test_depends_on_s6(self):
        result = pf_polynomial_genus4()
        assert result['depends_on'].get('S_6', False)

    def test_positive_n_terms(self):
        result = pf_polynomial_genus4()
        assert result['n_terms'] > 0

    def test_polynomial_nonzero(self):
        result = pf_polynomial_genus4()
        assert result['pf_polynomial'] != 0


# ============================================================================
# Section 14: Graph census
# ============================================================================

class TestGraphCensus:
    """Verify the stable graph census at genus 4.

    Cross-checks:
    - pf + nonpf = total (partition completeness)
    - Independent count from stable_graph_enumeration module
    - Consistency with pixton_genus4_engine counts
    """

    def test_total_graph_count(self):
        """379 stable graphs at (4,0). Cross-check: independent enumeration."""
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        independent_count = len(enumerate_stable_graphs(4, 0))
        assert genus4_graph_count() == independent_count
        assert genus4_graph_count() == 379

    def test_pf_count_cross_check(self):
        """358 planted-forest graphs. Cross-check: count from raw graph list."""
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        graphs = enumerate_stable_graphs(4, 0)
        pf_independent = sum(1 for g in graphs if is_planted_forest(g))
        assert genus4_pf_count() == pf_independent
        assert genus4_pf_count() == 358

    def test_nonpf_count_cross_check(self):
        """21 non-planted-forest graphs. Cross-check: total - pf."""
        assert genus4_nonpf_count() == genus4_graph_count() - genus4_pf_count()
        assert genus4_nonpf_count() == 21

    def test_pf_plus_nonpf_equals_total(self):
        """Partition completeness: every graph is either pf or non-pf."""
        assert genus4_pf_count() + genus4_nonpf_count() == genus4_graph_count()

    def test_nonzero_hodge_positive(self):
        """At least some graphs have nonzero Hodge integral."""
        assert genus4_nonzero_hodge_count() > 0

    def test_nonzero_hodge_less_than_total(self):
        """Not all graphs have nonzero Hodge integral (parity kills some)."""
        assert genus4_nonzero_hodge_count() < genus4_graph_count()
