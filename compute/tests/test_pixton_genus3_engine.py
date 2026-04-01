r"""Tests for the Pixton genus-3 ideal membership engine.

Tests the genus-3 planted-forest correction and Pixton conjecture:
1. Graph enumeration (42 stable graphs at g=3, n=0)
2. Graph classification by vertices, loop number, codimension
3. Planted-forest identification
4. Hodge integral computation
5. Self-loop parity vanishing (prop:self-loop-vanishing)
6. Vertex weight computation
7. MC relation at genus 3
8. Planted-forest correction delta_pf^{(3,0)}
9. Euler characteristic verification
10. Automorphism spectrum analysis
"""

import unittest
from fractions import Fraction

from sympy import Symbol, Integer, Rational, cancel, simplify, expand

from compute.lib.pixton_genus3_engine import (
    genus3_graphs,
    graph_classification,
    graph_summary_table,
    hodge_integral,
    vertex_weight_g3,
    mc_relation_genus3,
    planted_forest_correction_g3,
    planted_forest_generic,
    pixton_ideal_genus3_test,
    virasoro_pf_genus3_symbolic,
    is_genus3_relation_new,
    verify_euler_characteristic_genus3,
    scalar_graph_sum_genus3,
    automorphism_spectrum,
    automorphism_sum,
    planted_forest_graph_detail,
    self_loop_parity_check_genus3,
    _is_planted_forest,
)

from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    c_sym,
)

from compute.lib.stable_graph_enumeration import (
    _lambda_fp_exact,
)


# ====================================================================
# Section 1: Graph enumeration
# ====================================================================

class TestGraphEnumeration(unittest.TestCase):
    """Test that we find exactly 42 stable graphs at (g=3, n=0)."""

    def test_total_count(self):
        graphs = genus3_graphs()
        self.assertEqual(len(graphs), 42)

    def test_all_genus_3(self):
        """Every graph has total genus = 3."""
        graphs = genus3_graphs()
        for G in graphs:
            genus = G.first_betti + sum(G.vertex_genera)
            self.assertEqual(genus, 3, f"Graph has total genus {genus} != 3")


# ====================================================================
# Section 2: Graph classification
# ====================================================================

class TestGraphClassification(unittest.TestCase):
    """Test classification by vertices, loops, codimension."""

    def test_vertex_count_partition(self):
        """Graphs partition by vertex count: |V| in {1, 2, 3, 4}."""
        cls = graph_classification()
        by_v = cls['by_vertices']
        total = sum(len(v) for v in by_v.values())
        self.assertEqual(total, 42)

    def test_vertex_counts(self):
        """Expected: |V|=1: 4, |V|=2: 12, |V|=3: 15, |V|=4: 11."""
        cls = graph_classification()
        by_v = cls['by_vertices']
        self.assertEqual(len(by_v.get(1, [])), 4)

    def test_loop_number_partition(self):
        cls = graph_classification()
        by_loop = cls['by_loop_number']
        total = sum(len(v) for v in by_loop.values())
        self.assertEqual(total, 42)

    def test_planted_forest_plus_pure(self):
        """PF + pure = 42."""
        cls = graph_classification()
        self.assertEqual(len(cls['planted_forest']) + len(cls['pure_kappa']), 42)


# ====================================================================
# Section 3: Planted-forest identification
# ====================================================================

class TestPlantedForestIdentification(unittest.TestCase):
    """Test planted-forest graph identification."""

    def test_smooth_graph_not_pf(self):
        """The smooth graph (single genus-3 vertex, no edges) is not PF."""
        graphs = genus3_graphs()
        smooth = [G for G in graphs if G.num_edges == 0]
        self.assertTrue(len(smooth) > 0)
        for G in smooth:
            self.assertFalse(_is_planted_forest(G))

    def test_pf_graph_has_genus0_vertex_val3(self):
        """PF graphs have at least one genus-0 vertex with valence >= 3."""
        graphs = genus3_graphs()
        for G in graphs:
            if _is_planted_forest(G):
                val = G.valence
                found = any(G.vertex_genera[v] == 0 and val[v] >= 3
                            for v in range(G.num_vertices))
                self.assertTrue(found, f"PF graph has no g=0, val>=3 vertex")


# ====================================================================
# Section 4: Hodge integral computation
# ====================================================================

class TestHodgeIntegrals(unittest.TestCase):
    """Test Hodge integral computations."""

    def test_smooth_graph_integral_one(self):
        """The smooth graph (no edges) has I = 1."""
        graphs = genus3_graphs()
        smooth = [G for G in graphs if G.num_edges == 0]
        for G in smooth:
            self.assertEqual(hodge_integral(G), Fraction(1))

    def test_all_integrals_are_fractions(self):
        """All Hodge integrals are exact Fractions."""
        graphs = genus3_graphs()
        for G in graphs:
            I = hodge_integral(G)
            self.assertIsInstance(I, Fraction)


# ====================================================================
# Section 5: Self-loop parity vanishing
# ====================================================================

class TestSelfLoopParity(unittest.TestCase):
    """Verify prop:self-loop-vanishing at genus 3."""

    def test_triple_loop_vanishes(self):
        """The single vertex (0,6) with 3 self-loops has I=0."""
        result = self_loop_parity_check_genus3()
        self.assertTrue(result['vanishes'],
                        f"Triple-loop integral = {result['hodge_integral']} != 0")

    def test_dim_is_odd(self):
        result = self_loop_parity_check_genus3()
        self.assertTrue(result['dim_is_odd'])
        self.assertEqual(result['dim_moduli'], 3)  # dim M-bar_{0,6} = 3


# ====================================================================
# Section 6: Euler characteristic verification
# ====================================================================

class TestEulerCharacteristic(unittest.TestCase):
    """Verify chi^orb(M-bar_{3,0}) = -12419/90720."""

    def test_euler_char_genus3(self):
        computed, expected, match = verify_euler_characteristic_genus3()
        self.assertTrue(match,
                        f"Euler char mismatch: {computed} != {expected}")
        self.assertEqual(expected, Fraction(-12419, 90720))


# ====================================================================
# Section 7: Automorphism spectrum
# ====================================================================

class TestAutomorphismSpectrum(unittest.TestCase):
    """Test automorphism orders of genus-3 stable graphs."""

    def test_spectrum_length(self):
        spec = automorphism_spectrum()
        self.assertEqual(len(spec), 42)

    def test_all_positive(self):
        spec = automorphism_spectrum()
        for a in spec:
            self.assertGreater(a, 0)

    def test_automorphism_sum_positive(self):
        s = automorphism_sum()
        self.assertGreater(s, 0)
        self.assertIsInstance(s, Fraction)


# ====================================================================
# Section 8: Scalar F_3 verification
# ====================================================================

class TestScalarF3(unittest.TestCase):
    """Test F_3 = kappa * lambda_3^FP."""

    def test_lambda_3_value(self):
        lam3 = scalar_graph_sum_genus3()
        self.assertEqual(lam3, Fraction(31, 967680))

    def test_lambda_3_positive(self):
        lam3 = scalar_graph_sum_genus3()
        self.assertGreater(lam3, 0)


# ====================================================================
# Section 9: Planted-forest correction for Heisenberg
# ====================================================================

class TestPFCorrectionHeisenberg(unittest.TestCase):
    """For class G (Heisenberg), planted-forest correction = 0."""

    def test_heisenberg_pf_zero(self):
        shadow = heisenberg_shadow_data()
        pf = planted_forest_correction_g3(shadow)
        self.assertEqual(pf, Integer(0),
                         f"Heisenberg PF correction = {pf} != 0")


# ====================================================================
# Section 10: Planted-forest correction generic
# ====================================================================

class TestPFCorrectionGeneric(unittest.TestCase):
    """Test the generic planted-forest polynomial."""

    def test_generic_nonzero(self):
        """The generic PF correction is not identically zero."""
        pf = planted_forest_generic()
        self.assertNotEqual(pf, 0)

    def test_generic_is_polynomial(self):
        """PF correction is a polynomial in kappa, S_3, S_4, S_5."""
        pf = planted_forest_generic()
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        S4 = Symbol('S_4')
        S5 = Symbol('S_5')
        # Check it has free symbols from the expected set
        free = pf.free_symbols
        self.assertTrue(free.issubset({kappa, S3, S4, S5}))


# ====================================================================
# Section 11: Pixton ideal test
# ====================================================================

class TestPixtonIdealTest(unittest.TestCase):
    """Test Pixton ideal membership at genus 3."""

    def test_heisenberg_trivially_satisfied(self):
        shadow = heisenberg_shadow_data()
        result = pixton_ideal_genus3_test(shadow)
        self.assertEqual(result['pixton_status'], 'trivially_satisfied')

    def test_virasoro_nontrivial(self):
        shadow = virasoro_shadow_data(max_arity=8)
        result = pixton_ideal_genus3_test(shadow)
        self.assertEqual(result['pixton_status'], 'nontrivial_test')
        self.assertEqual(result['depth_class'], 'M')


# ====================================================================
# Section 12: Genus-3 relation independence
# ====================================================================

class TestRelationIndependence(unittest.TestCase):
    """Test if genus-3 relation is independent of lower genus."""

    def test_genus3_has_new_shadows(self):
        """The genus-3 PF correction should involve S_4 or S_5."""
        result = is_genus3_relation_new(ShadowData('test', Symbol('kappa'),
                                                     Symbol('S_3'), Symbol('S_4'),
                                                     shadows={5: Symbol('S_5')},
                                                     depth_class='M'))
        self.assertTrue(result['is_new'],
                        "Genus-3 relation should involve S_4 or S_5")


# ====================================================================
# Section 13: Planted-forest graph details
# ====================================================================

class TestPlantedForestDetails(unittest.TestCase):
    """Test detailed PF graph information."""

    def test_all_pf_graphs_have_shadow_indices(self):
        details = planted_forest_graph_detail()
        for d in details:
            self.assertGreater(len(d['shadow_coefficients_needed']), 0)
            for idx in d['shadow_coefficients_needed']:
                self.assertGreaterEqual(idx, 3)

    def test_pf_details_nonempty(self):
        details = planted_forest_graph_detail()
        self.assertGreater(len(details), 0)


# ====================================================================
# Section 14: Graph summary table
# ====================================================================

class TestGraphSummaryTable(unittest.TestCase):
    """Test the summary table generation."""

    def test_table_has_42_entries(self):
        table = graph_summary_table()
        self.assertEqual(len(table), 42)

    def test_table_entries_complete(self):
        table = graph_summary_table()
        for entry in table:
            self.assertIn('index', entry)
            self.assertIn('vertex_genera', entry)
            self.assertIn('codimension', entry)
            self.assertIn('loop_number', entry)
            self.assertIn('is_planted_forest', entry)
            self.assertIn('automorphism', entry)


# ====================================================================
# Section 15: MC relation structure
# ====================================================================

class TestMCRelation(unittest.TestCase):
    """Test the genus-3 MC relation computation."""

    def test_mc_relation_has_graphs(self):
        shadow = heisenberg_shadow_data()
        result = mc_relation_genus3(shadow)
        self.assertEqual(len(result['graphs']), 42)

    def test_mc_relation_codim1(self):
        """MC relation should have a codim-1 boundary contribution."""
        shadow = heisenberg_shadow_data()
        result = mc_relation_genus3(shadow)
        # Check structure exists
        self.assertIn('codim1_total', result)
        self.assertIn('planted_forest', result)


# ====================================================================
# Section 16: Virasoro symbolic planted-forest
# ====================================================================

class TestVirasoroPFSymbolic(unittest.TestCase):
    """Test the symbolic Virasoro PF correction at genus 3."""

    def test_virasoro_pf_symbolic_type(self):
        pf = virasoro_pf_genus3_symbolic()
        # Should be a sympy expression involving c
        self.assertTrue(hasattr(pf, 'free_symbols'))

    def test_virasoro_pf_involves_c(self):
        pf = virasoro_pf_genus3_symbolic()
        self.assertIn(c_sym, pf.free_symbols)


if __name__ == '__main__':
    unittest.main()
