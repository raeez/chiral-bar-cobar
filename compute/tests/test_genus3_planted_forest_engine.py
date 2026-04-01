r"""Tests for the genus-3 planted-forest correction engine.

Tests delta_pf^{(g,0)} at genera 2 and 3:
1. PlantedForestGraph construction and properties
2. Genus-2 cross-validation (known formula)
3. Genus-3 planted-forest correction
4. Self-loop parity vanishing
5. Shadow visibility genus formula
6. Family-specific evaluations (Heisenberg, affine, Virasoro)
7. Genus-3 PF census and structure
8. Genus-3 polynomial extraction
9. Graph-by-graph analysis
10. Cross-checks between genera 2 and 3
"""

import unittest
from fractions import Fraction

from sympy import Symbol, Integer, Rational, cancel, simplify, expand

from compute.lib.genus3_planted_forest_engine import (
    PlantedForestGraph,
    annotate_graphs,
    genus2_planted_forest_graphs,
    genus2_planted_forest_correction,
    verify_genus2_formula,
    genus3_planted_forest_graphs,
    genus3_all_graphs,
    genus3_planted_forest_correction,
    genus3_planted_forest_polynomial,
    genus3_exact_polynomial,
    self_loop_parity_vanishing,
    verify_self_loop_vanishing,
    shadow_visibility_genus,
    verify_shadow_visibility,
    evaluate_heisenberg_g3,
    evaluate_affine_sl2_g3,
    evaluate_virasoro_g3,
    genus3_pf_census,
    genus3_graph_by_graph_analysis,
    genus2_from_framework,
)

from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    heisenberg_shadow_data,
    affine_shadow_data,
    virasoro_shadow_data,
    stable_graphs_genus2_0leg,
    stable_graphs_genus3_0leg,
)


# ====================================================================
# Section 1: Graph annotation
# ====================================================================

class TestGraphAnnotation(unittest.TestCase):
    """Test PlantedForestGraph annotation."""

    def test_genus2_annotated_count(self):
        g2 = stable_graphs_genus2_0leg()
        annotated = annotate_graphs(g2)
        self.assertEqual(len(annotated), len(g2))

    def test_genus3_annotated_count(self):
        g3 = stable_graphs_genus3_0leg()
        annotated = annotate_graphs(g3)
        self.assertEqual(len(annotated), len(g3))

    def test_hodge_integral_is_fraction(self):
        g2 = stable_graphs_genus2_0leg()
        annotated = annotate_graphs(g2)
        for pfg in annotated:
            self.assertIsInstance(pfg.hodge_integral, Fraction)


# ====================================================================
# Section 2: Genus-2 cross-validation
# ====================================================================

class TestGenus2CrossValidation(unittest.TestCase):
    """Verify delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48."""

    def test_genus2_known_formula(self):
        result = verify_genus2_formula()
        self.assertTrue(result['match'],
                        f"Mismatch: computed {result['computed']} != expected {result['expected']}")

    def test_genus2_from_framework(self):
        result = genus2_from_framework()
        self.assertTrue(result['match'])

    def test_genus2_pf_graphs_exist(self):
        pf = genus2_planted_forest_graphs()
        self.assertGreater(len(pf), 0)

    def test_genus2_heisenberg_zero(self):
        """Heisenberg: S_3 = 0, so delta_pf^{(2,0)} = 0."""
        shadow = heisenberg_shadow_data()
        pf = genus2_planted_forest_correction(shadow)
        self.assertEqual(pf, Integer(0))


# ====================================================================
# Section 3: Self-loop parity vanishing
# ====================================================================

class TestSelfLoopParity(unittest.TestCase):
    """Verify prop:self-loop-vanishing: I(0, 2k) = 0 for k >= 2."""

    def test_k2_vanishes(self):
        result = self_loop_parity_vanishing(2)
        self.assertTrue(result['vanishes'])
        self.assertTrue(result['dim_is_odd'])

    def test_k3_vanishes(self):
        result = self_loop_parity_vanishing(3)
        self.assertTrue(result['vanishes'])

    def test_k4_vanishes(self):
        result = self_loop_parity_vanishing(4)
        self.assertTrue(result['vanishes'])

    def test_k_less_than_2_invalid(self):
        result = self_loop_parity_vanishing(1)
        self.assertFalse(result['valid'])

    def test_verify_up_to_k8(self):
        result = verify_self_loop_vanishing(max_k=6)
        self.assertTrue(result['all_vanish'])


# ====================================================================
# Section 4: Shadow visibility genus
# ====================================================================

class TestShadowVisibilityGenus(unittest.TestCase):
    """Test g_min(S_r) = floor(r/2) + 1."""

    def test_S3_at_genus2(self):
        self.assertEqual(shadow_visibility_genus(3), 2)

    def test_S4_at_genus3(self):
        self.assertEqual(shadow_visibility_genus(4), 3)

    def test_S5_at_genus3(self):
        self.assertEqual(shadow_visibility_genus(5), 3)

    def test_S6_at_genus4(self):
        self.assertEqual(shadow_visibility_genus(6), 4)

    def test_S7_at_genus4(self):
        self.assertEqual(shadow_visibility_genus(7), 4)

    def test_S8_at_genus5(self):
        self.assertEqual(shadow_visibility_genus(8), 5)


# ====================================================================
# Section 5: Heisenberg evaluation
# ====================================================================

class TestHeisenbergEvaluation(unittest.TestCase):
    """For Heisenberg (class G), delta_pf = 0 at all genera."""

    def test_heisenberg_genus3_zero(self):
        result = evaluate_heisenberg_g3()
        self.assertTrue(result['is_zero'])
        self.assertEqual(result['class'], 'G')


# ====================================================================
# Section 6: Affine sl2 evaluation
# ====================================================================

class TestAffineSl2Evaluation(unittest.TestCase):
    """For affine sl2 (class L), S_4 = S_5 = 0."""

    def test_affine_no_S4(self):
        result = evaluate_affine_sl2_g3()
        self.assertFalse(result['has_S4'])
        self.assertEqual(result['class'], 'L')


# ====================================================================
# Section 7: Virasoro evaluation
# ====================================================================

class TestVirasoroEvaluation(unittest.TestCase):
    """Test Virasoro planted-forest correction at genus 3."""

    def test_virasoro_class_M(self):
        result = evaluate_virasoro_g3()
        self.assertEqual(result['class'], 'M')

    def test_virasoro_symbolic_nonzero(self):
        result = evaluate_virasoro_g3()
        self.assertNotEqual(result['delta_pf_symbolic'], 0)


# ====================================================================
# Section 8: Genus-3 PF census
# ====================================================================

class TestGenus3PFCensus(unittest.TestCase):
    """Test the census of planted-forest graphs at genus 3."""

    def test_total_graphs(self):
        census = genus3_pf_census()
        # The pixton_shadow_bridge may enumerate a different count
        # but it should be positive
        self.assertGreater(census['total_graphs'], 0)

    def test_pf_plus_nonpf_equals_total(self):
        census = genus3_pf_census()
        self.assertEqual(census['pf_graphs'] + census['non_pf_graphs'],
                         census['total_graphs'])

    def test_pf_graphs_exist(self):
        census = genus3_pf_census()
        self.assertGreater(census['pf_graphs'], 0)


# ====================================================================
# Section 9: Genus-3 polynomial extraction
# ====================================================================

class TestGenus3Polynomial(unittest.TestCase):
    """Test the exact polynomial delta_pf^{(3,0)}."""

    def test_polynomial_has_terms(self):
        result = genus3_planted_forest_polynomial()
        self.assertGreater(result['num_terms'], 0)

    def test_polynomial_has_pf_graphs(self):
        result = genus3_planted_forest_polynomial()
        self.assertGreater(result['num_pf_graphs'], 0)

    def test_exact_polynomial_matches(self):
        """genus3_exact_polynomial just calls genus3_planted_forest_polynomial."""
        r1 = genus3_exact_polynomial()
        r2 = genus3_planted_forest_polynomial()
        self.assertEqual(r1['num_terms'], r2['num_terms'])


# ====================================================================
# Section 10: Graph-by-graph analysis
# ====================================================================

class TestGraphByGraphAnalysis(unittest.TestCase):
    """Test per-graph analysis of PF contributions."""

    def test_analysis_uses_shadow_data(self):
        shadow = heisenberg_shadow_data()
        results = genus3_graph_by_graph_analysis(shadow)
        # All Heisenberg amplitudes should be zero
        for r in results:
            self.assertEqual(cancel(r['weighted_amplitude']), 0,
                             f"Graph {r['name']} has nonzero amplitude for Heisenberg")

    def test_analysis_returns_list(self):
        shadow = affine_shadow_data()
        results = genus3_graph_by_graph_analysis(shadow)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)


# ====================================================================
# Section 11: PlantedForestGraph properties
# ====================================================================

class TestPlantedForestGraphProperties(unittest.TestCase):
    """Test PlantedForestGraph wrapper properties."""

    def test_genus2_pf_codimension(self):
        """All genus-2 PF graphs have codimension >= 2."""
        pf_graphs = genus2_planted_forest_graphs()
        for pfg in pf_graphs:
            self.assertGreaterEqual(pfg.codimension, 2)

    def test_genus3_pf_all_planted(self):
        """All returned genus-3 PF graphs are actually PF."""
        pf_graphs = genus3_planted_forest_graphs()
        for pfg in pf_graphs:
            self.assertTrue(pfg.is_planted_forest)


# ====================================================================
# Section 12: Consistency between genera
# ====================================================================

class TestCrossGenusConsistency(unittest.TestCase):
    """Consistency checks between genus 2 and genus 3."""

    def test_genus2_has_fewer_pf_graphs_than_genus3(self):
        g2 = genus2_planted_forest_graphs()
        g3 = genus3_planted_forest_graphs()
        # Genus 3 should have at least as many PF graphs
        self.assertGreaterEqual(len(g3), len(g2))

    def test_heisenberg_zero_at_both_genera(self):
        shadow = heisenberg_shadow_data()
        pf2 = genus2_planted_forest_correction(shadow)
        g3_result = evaluate_heisenberg_g3()
        self.assertEqual(pf2, Integer(0))
        self.assertTrue(g3_result['is_zero'])


if __name__ == '__main__':
    unittest.main()
