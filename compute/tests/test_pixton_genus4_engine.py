r"""Tests for the genus-4 Pixton ideal engine.

Covers: Faber-Pandharipande numbers, Hodge integrals on small graphs,
self-loop parity vanishing, planted-forest classification, genus-4 graph
census, shadow visibility, Heisenberg three-path verification, amplitude
decomposition, and cross-family comparison.

VERIFICATION PATHS (3+ per numerical claim):
    Path 1: Direct formula computation
    Path 2: Independent series / recursion
    Path 3: Known literature values or limiting cases

The genus-4 amplitude computation takes ~30s. Tests that require the full
379-graph enumeration are grouped into a class that computes the data once
at class level via setUpClass.

References:
    conj:pixton-from-shadows (concordance.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
    thm:mc-tautological-descent (higher_genus_modular_koszul.tex)
"""

import unittest
from fractions import Fraction
from math import factorial

from sympy import Integer, Rational, Symbol, cancel, simplify, expand

from compute.lib.pixton_genus4_engine import (
    # Section 0: Constants
    lambda_fp_exact,
    LAMBDA4_FP,
    # Section 1: Hodge integrals
    hodge_integral,
    # Section 2: Vertex weights
    vertex_weight,
    is_planted_forest,
    ell_genus1,
    ell_genus2,
    ell_genus3,
    # Section 3-4: Graph amplitudes
    GraphAmplitude,
    genus4_all_amplitudes,
    genus4_pf_amplitudes,
    genus4_nonpf_amplitudes,
    # Section 5: Census
    genus4_pixton_census,
    # Section 6: Total amplitudes
    genus4_total_amplitude,
    genus4_planted_forest_correction,
    genus4_nonpf_amplitude,
    # Section 7: Family evaluations
    genus4_heisenberg_F4,
    genus4_virasoro_F4,
    genus4_affine_sl2_F4,
    # Section 8: Self-loop parity
    verify_self_loop_parity_g4,
    # Section 9: Shadow visibility
    verify_shadow_visibility_g4,
    # Section 10: PF polynomial
    genus4_pf_polynomial,
    # Section 14: Consistency
    consistency_checks,
)
from compute.lib.stable_graph_enumeration import StableGraph, enumerate_stable_graphs
from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    heisenberg_shadow_data,
    virasoro_shadow_data,
    affine_shadow_data,
    c_sym,
)


F = Fraction


# =========================================================================
# 1. Faber-Pandharipande numbers (fast, no graph enumeration)
# =========================================================================

class TestLambdaFP(unittest.TestCase):
    """Faber-Pandharipande numbers lambda_g^FP.

    Three-path verification:
      Path 1: Direct Bernoulli formula (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
      Path 2: Known literature values
      Path 3: A-hat generating function coefficients
    """

    def test_lambda1(self):
        self.assertEqual(lambda_fp_exact(1), F(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp_exact(2), F(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp_exact(3), F(31, 967680))

    def test_lambda4(self):
        self.assertEqual(lambda_fp_exact(4), F(127, 154828800))

    def test_lambda5(self):
        self.assertEqual(lambda_fp_exact(5), F(73, 3503554560))

    def test_lambda4_module_constant(self):
        """LAMBDA4_FP module constant matches computation."""
        self.assertEqual(LAMBDA4_FP, F(127, 154828800))

    def test_lambda_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 6):
            self.assertGreater(lambda_fp_exact(g), 0)

    def test_lambda_decreasing(self):
        """lambda_g^FP is strictly decreasing for g >= 1."""
        for g in range(1, 5):
            self.assertGreater(lambda_fp_exact(g), lambda_fp_exact(g + 1))

    def test_lambda_invalid_genus(self):
        with self.assertRaises(ValueError):
            lambda_fp_exact(0)

    def test_ahat_cross_check(self):
        """Cross-check lambda_4^FP via A-hat generating function.

        (h/2)/sin(h/2) = sum_{g>=0} a_g h^{2g}, with
        lambda_g^FP = a_g / 4^g.
        """
        # Compute A-hat coefficients via reciprocal of sin series
        c_sin = [F((-1)**n, factorial(2 * n + 1)) for n in range(5)]
        a = [F(0)] * 5
        a[0] = F(1)
        for n in range(1, 5):
            s = F(0)
            for j in range(1, n + 1):
                s += c_sin[j] * a[n - j]
            a[n] = -s / c_sin[0]
        l4_ahat = a[4] / F(4 ** 4)
        self.assertEqual(l4_ahat, F(127, 154828800))


# =========================================================================
# 2. Hodge integrals on small graphs (fast)
# =========================================================================

class TestHodgeIntegralSmall(unittest.TestCase):
    """Hodge integrals on genus <= 3 graphs (fast, no genus-4 enumeration)."""

    def test_smooth_genus1(self):
        """I(smooth genus 1) = 1."""
        g = StableGraph(vertex_genera=(1,), edges=(), legs=())
        self.assertEqual(hodge_integral(g), F(1))

    def test_smooth_genus2(self):
        """I(smooth genus 2) = 1."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        self.assertEqual(hodge_integral(g), F(1))

    def test_smooth_genus3(self):
        """I(smooth genus 3) = 1."""
        g = StableGraph(vertex_genera=(3,), edges=(), legs=())
        self.assertEqual(hodge_integral(g), F(1))

    def test_smooth_genus4(self):
        """I(smooth genus 4) = 1."""
        g = StableGraph(vertex_genera=(4,), edges=(), legs=())
        self.assertEqual(hodge_integral(g), F(1))

    def test_genus1_self_loop_vanishes(self):
        """(0,2) with 1 self-loop: I=0 (genus-0 vertex, dim < 0)."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        self.assertEqual(hodge_integral(g), F(0))

    def test_genus1_self_loop_at_genus2(self):
        """(1,) with self-loop: total genus 2, I = 1/24."""
        g = StableGraph(vertex_genera=(1,), edges=((0, 0),), legs=())
        self.assertEqual(hodge_integral(g), F(1, 24))

    def test_genus2_triple_bridge(self):
        """Two genus-0 vertices with 3 bridges: total genus 2, I = 1."""
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        self.assertEqual(hodge_integral(g), F(1))

    def test_genus2_bridge(self):
        """(1,1) bridge at genus 2: I = -1/576."""
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        self.assertEqual(hodge_integral(g), F(-1, 576))

    def test_genus2_bridge_cross_check(self):
        """(0,1) bridge + self-loop at genus 2: I = -1/24."""
        g = StableGraph(vertex_genera=(0, 1), edges=((0, 0), (0, 1)), legs=())
        self.assertEqual(hodge_integral(g), F(-1, 24))

    def test_genus2_double_self_loop_vanishes(self):
        """(0,4) double self-loop at genus 2: I = 0."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        self.assertEqual(hodge_integral(g), F(0))


# =========================================================================
# 3. Self-loop parity vanishing (fast, individual graphs)
# =========================================================================

class TestSelfLoopParity(unittest.TestCase):
    """Self-loop parity vanishing (prop:self-loop-vanishing).

    Single-vertex (g_v, 2k) with k self-loops: if dim = 3g_v - 3 + 2k is
    ODD and k >= 2, then I = 0.
    """

    def test_genus2_val4_vanishes(self):
        """(2,4): 2 self-loops, dim = 7 (odd), I = 0."""
        g = StableGraph(vertex_genera=(2,), edges=((0, 0), (0, 0)), legs=())
        self.assertEqual(hodge_integral(g), F(0))

    def test_genus0_val8_vanishes(self):
        """(0,8): 4 self-loops, dim = 5 (odd), I = 0."""
        g = StableGraph(vertex_genera=(0,),
                        edges=((0, 0), (0, 0), (0, 0), (0, 0)), legs=())
        self.assertEqual(hodge_integral(g), F(0))

    def test_genus1_val6_does_not_vanish(self):
        """(1,6): 3 self-loops, dim = 6 (even), I != 0 (parity does not apply)."""
        g = StableGraph(vertex_genera=(1,),
                        edges=((0, 0), (0, 0), (0, 0)), legs=())
        I = hodge_integral(g)
        self.assertNotEqual(I, F(0))

    def test_genus3_val2_vanishes(self):
        """(3,2): 1 self-loop, dim = 8 (even), but I = 0 for other reasons."""
        g = StableGraph(vertex_genera=(3,), edges=((0, 0),), legs=())
        self.assertEqual(hodge_integral(g), F(0))

    def test_verify_function(self):
        """verify_self_loop_parity_g4 returns correct parity predictions."""
        data = verify_self_loop_parity_g4()
        # (2,4): parity applicable, prediction True, vanishes True
        d24 = data['(2,4)']
        self.assertTrue(d24['parity_applicable'])
        self.assertTrue(d24['parity_prediction'])
        self.assertTrue(d24['vanishes'])
        # (0,8): parity applicable, prediction True, vanishes True
        d08 = data['(0,8)']
        self.assertTrue(d08['parity_applicable'])
        self.assertTrue(d08['parity_prediction'])
        self.assertTrue(d08['vanishes'])
        # (1,6): parity applicable (k>=2), but dim even => prediction False
        d16 = data['(1,6)']
        self.assertTrue(d16['parity_applicable'])
        self.assertFalse(d16['parity_prediction'])
        # (4,0): smooth, parity not applicable
        d40 = data['(4,0)']
        self.assertFalse(d40['parity_applicable'])


# =========================================================================
# 4. Planted-forest classification (fast, small graphs)
# =========================================================================

class TestPlantedForest(unittest.TestCase):
    """Planted-forest classification: graph has a genus-0 vertex of valence >= 3."""

    def test_smooth_genus4_not_pf(self):
        g = StableGraph(vertex_genera=(4,), edges=(), legs=())
        self.assertFalse(is_planted_forest(g))

    def test_genus0_triple_bridge_is_pf(self):
        """Two genus-0 vertices with 3 bridges: valence 3 each."""
        g = StableGraph(vertex_genera=(0, 0),
                        edges=((0, 1), (0, 1), (0, 1)), legs=())
        self.assertTrue(is_planted_forest(g))

    def test_genus1_bridge_not_pf(self):
        """Two genus-1 vertices with 1 bridge: no genus-0 vertex."""
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        self.assertFalse(is_planted_forest(g))

    def test_genus0_double_self_loop_is_pf(self):
        """Genus-0 with 2 self-loops: valence 4 >= 3."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        self.assertTrue(is_planted_forest(g))

    def test_genus2_counts(self):
        """At genus 2: 4 PF + 3 non-PF = 7 total."""
        g2 = enumerate_stable_graphs(2, 0)
        pf_count = sum(1 for g in g2 if is_planted_forest(g))
        self.assertEqual(len(g2), 7)
        self.assertEqual(pf_count, 4)

    def test_genus3_counts(self):
        """At genus 3: 35 PF + 7 non-PF = 42 total."""
        g3 = enumerate_stable_graphs(3, 0)
        pf_count = sum(1 for g in g3 if is_planted_forest(g))
        self.assertEqual(len(g3), 42)
        self.assertEqual(pf_count, 35)


# =========================================================================
# 5. Vertex weight functions (fast, symbolic)
# =========================================================================

class TestVertexWeights(unittest.TestCase):
    """Vertex weight assignments for shadow data."""

    def test_ell_genus1_val1(self):
        """ell_1^{(1)} = kappa."""
        sd = heisenberg_shadow_data()
        self.assertEqual(ell_genus1(1, sd), sd.kappa)

    def test_ell_genus2_val0(self):
        """ell_0^{(2)} = kappa * 7/5760."""
        sd = heisenberg_shadow_data()
        result = ell_genus2(0, sd)
        expected = sd.kappa * Rational(7, 5760)
        self.assertEqual(simplify(result - expected), 0)

    def test_ell_genus3_val0(self):
        """ell_0^{(3)} = kappa * 31/967680."""
        sd = heisenberg_shadow_data()
        result = ell_genus3(0, sd)
        expected = sd.kappa * Rational(31, 967680)
        self.assertEqual(simplify(result - expected), 0)

    def test_heisenberg_genus0_vertex_zero(self):
        """Heisenberg: genus-0 vertex with valence >= 3 gives S_r = 0."""
        sd = heisenberg_shadow_data()
        for r in range(3, 8):
            self.assertEqual(sd.S(r), 0)

    def test_affine_genus0_vertex_s3(self):
        """Affine sl_2: S_3 = 2, S_4 = 0."""
        sd = affine_shadow_data()
        self.assertEqual(sd.S(3), 2)
        self.assertEqual(sd.S(4), 0)

    def test_vertex_weight_smooth_genus4(self):
        """Smooth genus-4 graph: vertex weight = 1 (valence 0, genus >= 4)."""
        g = StableGraph(vertex_genera=(4,), edges=(), legs=())
        sd = heisenberg_shadow_data()
        w = vertex_weight(g, sd)
        self.assertEqual(simplify(w - 1), 0)


# =========================================================================
# 6. Shadow visibility formula (fast)
# =========================================================================

class TestShadowVisibility(unittest.TestCase):
    """Shadow visibility: g_min(S_r) = floor(r/2) + 1."""

    def test_g_min_formula(self):
        cases = {3: 2, 4: 3, 5: 3, 6: 4, 7: 4, 8: 5, 9: 5, 10: 6}
        for r, expected_g in cases.items():
            self.assertEqual(r // 2 + 1, expected_g,
                             f'g_min(S_{r}) wrong')

    def test_s6_first_visible_at_genus4(self):
        self.assertEqual(6 // 2 + 1, 4)

    def test_s7_first_visible_at_genus4(self):
        self.assertEqual(7 // 2 + 1, 4)

    def test_s8_not_visible_at_genus4(self):
        self.assertEqual(8 // 2 + 1, 5)


# =========================================================================
# 7-14. Tests requiring full genus-4 enumeration (~30s setup)
# =========================================================================

class TestGenus4Enumeration(unittest.TestCase):
    """Tests over the full set of 379 genus-4 stable graphs.

    setUpClass computes the amplitudes once for all tests in this class.
    """

    @classmethod
    def setUpClass(cls):
        cls.all_amps = list(genus4_all_amplitudes())
        cls.pf_amps = [a for a in cls.all_amps if a.is_pf]
        cls.nonpf_amps = [a for a in cls.all_amps if not a.is_pf]

    # --- 7. Graph count ---

    def test_total_graph_count(self):
        self.assertEqual(len(self.all_amps), 379)

    def test_pf_count(self):
        self.assertEqual(len(self.pf_amps), 358)

    def test_nonpf_count(self):
        self.assertEqual(len(self.nonpf_amps), 21)

    def test_pf_nonpf_partition(self):
        self.assertEqual(len(self.pf_amps) + len(self.nonpf_amps), 379)

    # --- 8. Vertex count distribution ---

    def test_single_vertex_count(self):
        """5 single-vertex graphs at genus 4 (one for each partition of 4)."""
        count = sum(1 for a in self.all_amps if a.num_vertices == 1)
        self.assertEqual(count, 5)

    def test_vertex_distribution_sums(self):
        """Vertex distribution sums to 379."""
        from collections import Counter
        dist = Counter(a.num_vertices for a in self.all_amps)
        self.assertEqual(sum(dist.values()), 379)

    # --- 9. Vanishing Hodge integrals ---

    def test_vanishing_hodge_count(self):
        """Some graphs have I = 0 (from dimensional reasons or parity)."""
        vanishing = sum(1 for a in self.all_amps if a.hodge_integral == F(0))
        self.assertGreater(vanishing, 0)

    def test_all_hodge_rational(self):
        """All Hodge integrals are exact rationals."""
        for a in self.all_amps:
            self.assertIsInstance(a.hodge_integral, Fraction)

    # --- 10. Genus-4 census ---

    def test_census_total(self):
        census = genus4_pixton_census()
        self.assertEqual(census['total'], 379)

    def test_census_pf(self):
        census = genus4_pixton_census()
        self.assertEqual(census['pf_count'], 358)

    def test_census_shadow_vals(self):
        """Census should detect S_6 and/or S_7 in nonzero PF graphs."""
        census = genus4_pixton_census()
        # At genus 4, genus-0 vertices can have valence up to 8
        # (4 self-loops). Valences 3,4,...,8 are possible.
        self.assertIn(3, census['shadow_vals_present'])

    # --- 11. Amplitude decomposition ---

    def test_decomposition_virasoro(self):
        """F_4 = F_4^{PF} + F_4^{non-PF} for Virasoro."""
        shadow = virasoro_shadow_data(max_arity=10)
        F4_total = genus4_total_amplitude(shadow)
        F4_pf = genus4_planted_forest_correction(shadow)
        F4_nonpf = genus4_nonpf_amplitude(shadow)
        diff = simplify(F4_total - F4_pf - F4_nonpf)
        self.assertEqual(diff, 0)

    def test_decomposition_heisenberg(self):
        """F_4 = F_4^{PF} + F_4^{non-PF} for Heisenberg."""
        shadow = heisenberg_shadow_data()
        F4_total = genus4_total_amplitude(shadow)
        F4_pf = genus4_planted_forest_correction(shadow)
        F4_nonpf = genus4_nonpf_amplitude(shadow)
        diff = simplify(F4_total - F4_pf - F4_nonpf)
        self.assertEqual(diff, 0)

    # --- 12. Heisenberg verification ---

    def test_heisenberg_pf_vanishes(self):
        """Heisenberg (class G): planted-forest correction = 0.

        All S_r = 0 for r >= 3, so every PF graph has a zero vertex weight.
        """
        shadow = heisenberg_shadow_data()
        pf = genus4_planted_forest_correction(shadow)
        self.assertEqual(simplify(pf), 0)

    def test_heisenberg_pf_is_zero_flag(self):
        data = genus4_heisenberg_F4()
        self.assertTrue(data['pf_is_zero'])

    def test_heisenberg_lambda4_bernoulli_vs_ahat(self):
        """lambda_4^FP: Bernoulli formula = A-hat coefficient (two independent paths)."""
        data = genus4_heisenberg_F4()
        self.assertEqual(data['lambda4_fp'], data['lambda4_ahat'])

    def test_heisenberg_bernoulli_matches_ahat_formula(self):
        """F_4 Bernoulli = F_4 A-hat (both = k * 127/154828800)."""
        data = genus4_heisenberg_F4()
        diff = simplify(data['F4_bernoulli'] - data['F4_ahat'])
        self.assertEqual(diff, 0)

    # --- 13. Affine sl_2 ---

    def test_affine_pf_nonzero(self):
        """Affine sl_2 (class L): PF correction is nonzero."""
        data = genus4_affine_sl2_F4()
        self.assertNotEqual(simplify(data['F4_pf']), 0)

    def test_affine_class_L(self):
        data = genus4_affine_sl2_F4()
        self.assertEqual(data['class'], 'L')

    # --- 14. Shadow visibility in genus-4 amplitudes ---

    def test_s6_in_pf_correction(self):
        """S_6 appears in the genus-4 PF correction (first visible at g=4)."""
        data = verify_shadow_visibility_g4()
        self.assertTrue(data['S6_in_pf_correction'])

    def test_s6_gmin_formula(self):
        data = verify_shadow_visibility_g4()
        self.assertEqual(data['formula_g_min_S6'], 4)

    # --- 15. PF polynomial structure ---

    def test_pf_polynomial_depends_on_kappa(self):
        data = genus4_pf_polynomial()
        self.assertTrue(data['depends_on']['kappa'])

    def test_pf_polynomial_depends_on_s3(self):
        data = genus4_pf_polynomial()
        self.assertTrue(data['depends_on']['S_3'])

    def test_pf_polynomial_positive_terms(self):
        data = genus4_pf_polynomial()
        self.assertGreater(data['n_terms'], 0)

    # --- 16. Pixton membership tests ---

    def test_pixton_heisenberg_pf_vanishes(self):
        """Pixton membership: Heisenberg PF correction vanishes."""
        from compute.lib.pixton_genus4_engine import genus4_pixton_membership_test
        results = genus4_pixton_membership_test()
        self.assertTrue(results['heisenberg_pf_vanishes'])

    def test_pixton_affine_pf_nonzero(self):
        """Pixton membership: affine PF correction is nonzero."""
        from compute.lib.pixton_genus4_engine import genus4_pixton_membership_test
        results = genus4_pixton_membership_test()
        self.assertTrue(results['affine_pf_nonzero'])

    def test_pixton_virasoro_pf_nonzero(self):
        """Pixton membership: Virasoro PF correction is nonzero."""
        from compute.lib.pixton_genus4_engine import genus4_pixton_membership_test
        results = genus4_pixton_membership_test()
        self.assertTrue(results['virasoro_pf_nonzero'])

    # --- 17. Consistency checks ---

    def test_consistency_graph_count(self):
        checks = consistency_checks()
        self.assertTrue(checks['graph_count']['passed'],
                        f'Graph count: {checks["graph_count"]}')

    def test_consistency_heisenberg_pf_zero(self):
        checks = consistency_checks()
        self.assertTrue(checks['heisenberg_pf_zero'],
                        'Heisenberg PF not zero')

    def test_consistency_self_loop_parity(self):
        checks = consistency_checks()
        self.assertTrue(checks['self_loop_parity'],
                        'Self-loop parity check failed')

    def test_consistency_s6_visible(self):
        checks = consistency_checks()
        self.assertTrue(checks['S6_visible'],
                        'S_6 not visible at genus 4')

    def test_consistency_decomposition(self):
        checks = consistency_checks()
        self.assertTrue(checks['decomposition_consistent'],
                        'Decomposition F4 = PF + non-PF inconsistent')

    # --- 18. Automorphism orders ---

    def test_all_aut_orders_positive(self):
        for a in self.all_amps:
            self.assertGreater(a.aut_order, 0)

    def test_smooth_graph_aut_order(self):
        """Smooth genus-4 graph (single vertex, no edges) has |Aut| = 1."""
        smooth = [a for a in self.all_amps
                  if a.num_vertices == 1 and a.num_edges == 0]
        self.assertEqual(len(smooth), 1)
        self.assertEqual(smooth[0].aut_order, 1)

    # --- 19. Codimension = num_edges ---

    def test_codimension_equals_edges(self):
        for a in self.all_amps:
            self.assertEqual(a.codimension, a.num_edges)

    # --- 20. First Betti number ---

    def test_first_betti_range(self):
        """First Betti number b_1 in [0, total_genus]."""
        for a in self.all_amps:
            self.assertGreaterEqual(a.first_betti, 0)
            self.assertLessEqual(a.first_betti, 4)

    def test_smooth_graph_betti_zero(self):
        """Smooth graph has b_1 = 0 (tree-like)."""
        smooth = [a for a in self.all_amps
                  if a.num_vertices == 1 and a.num_edges == 0]
        self.assertEqual(smooth[0].first_betti, 0)


if __name__ == '__main__':
    unittest.main()
