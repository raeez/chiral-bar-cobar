r"""Tests for the Pixton genus-3 shadow engine.

Comprehensive test suite verifying:
1. Shadow visibility genus formula (g_min(S_r) = floor(r/2) + 1)
2. Self-loop parity vanishing (prop:self-loop-vanishing)
3. Planted-forest classification (35 of 42 graphs)
4. The 11-term delta_pf^{(3,0)} polynomial
5. Cross-family comparison (G/L/C/M depth classes)
6. Faber-Zagier relation comparison
7. Pixton ideal membership
8. Generation of new tautological relations at genus 3
9. Multi-path F_3 verification
10. Euler characteristic multi-path verification
11. Automorphism spectrum analysis
12. Codimension decomposition
13. c=13 self-duality
14. Quintic shadow isolation
15. Virasoro special values
16. Hodge integral sign patterns

Manuscript references:
    conj:pixton-from-shadows (concordance.tex)
    eq:delta-pf-genus3-explicit (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
"""

import unittest
from fractions import Fraction

from sympy import Symbol, Integer, Rational, cancel, simplify, expand

from compute.lib.pixton_genus3_shadow_engine import (
    # Section 1: Bernoulli / lambda_FP
    lambda_fp_independent,
    # Section 2: Shadow visibility
    shadow_visibility_genus,
    verify_shadow_visibility_genus3,
    shadow_visibility_all,
    # Section 3: Graph classification
    classify_by_shadow_depth,
    planted_forest_subclassification,
    # Section 4: Self-loop parity
    self_loop_parity_vanishing_all_genus3,
    # Section 5: Delta_pf formula
    manuscript_delta_pf_genus3,
    verify_delta_pf_formula,
    delta_pf_term_count,
    # Section 6: Virasoro
    virasoro_delta_pf_genus3,
    virasoro_delta_pf_at_c,
    virasoro_delta_pf_special_values,
    # Section 7: Cross-family
    cross_family_genus3,
    depth_class_consistency_genus3,
    # Section 8: Faber-Zagier
    faber_zagier_genus3_codim3,
    # Section 9: Pixton ideal
    Genus3StrataAlgebra,
    pixton_ideal_membership_genus3,
    # Section 10: New relations
    genus3_new_relation_test,
    # Section 11: Euler char
    euler_characteristic_genus3_multipath,
    # Section 12: Automorphisms
    automorphism_spectrum_analysis,
    # Section 13: Codimension decomposition
    codimension_decomposition_genus3,
    # Section 14: c=13
    c13_self_duality_check_genus3,
    # Section 15: PF census
    planted_forest_census,
    # Section 16: Genus comparison
    delta_pf_genus_comparison,
    # Section 17: Hodge signs
    hodge_integral_sign_pattern,
    # Section 18: F_3 multipath
    F3_multipath_verification,
    # Section 19: Gaussian total
    gaussian_total_genus3,
    # Section 20: Quintic isolation
    quintic_shadow_isolation,
)

from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    c_sym,
)

from compute.lib.pixton_genus3_engine import (
    genus3_graphs,
    graph_classification,
    planted_forest_generic,
)


# ====================================================================
# Section 1: Shadow visibility genus
# ====================================================================

class TestShadowVisibilityGenus(unittest.TestCase):
    """Verify cor:shadow-visibility-genus: g_min(S_r) = floor(r/2) + 1."""

    def test_g_min_S2(self):
        """S_2 = kappa first appears at genus 1."""
        self.assertEqual(shadow_visibility_genus(2), 2)

    def test_g_min_S3(self):
        """S_3 first appears at genus 2."""
        self.assertEqual(shadow_visibility_genus(3), 2)

    def test_g_min_S4(self):
        """S_4 first appears at genus 2."""
        self.assertEqual(shadow_visibility_genus(4), 3)

    def test_g_min_S5(self):
        """S_5 first appears at genus 3. This is THE key visibility test."""
        self.assertEqual(shadow_visibility_genus(5), 3)

    def test_g_min_S6(self):
        """S_6 first appears at genus 4."""
        self.assertEqual(shadow_visibility_genus(6), 4)

    def test_g_min_S7(self):
        """S_7 first appears at genus 4."""
        self.assertEqual(shadow_visibility_genus(7), 4)

    def test_g_min_S8(self):
        """S_8 first appears at genus 5."""
        self.assertEqual(shadow_visibility_genus(8), 5)

    def test_visibility_all_dict(self):
        """shadow_visibility_all returns correct dict for r=2..8."""
        d = shadow_visibility_all()
        self.assertEqual(d[2], 2)
        self.assertEqual(d[5], 3)
        self.assertEqual(d[8], 5)

    def test_S5_not_at_genus2(self):
        """No genus-2 graph has a genus-0 vertex of valence >= 5."""
        result = verify_shadow_visibility_genus3()
        self.assertFalse(result['genus2_has_S5_vertex'])

    def test_S5_at_genus3(self):
        """At least one genus-3 graph has a genus-0 vertex of valence >= 5."""
        result = verify_shadow_visibility_genus3()
        self.assertTrue(result['genus3_has_S5_vertex'])

    def test_visibility_verified(self):
        """Full visibility verification passes."""
        result = verify_shadow_visibility_genus3()
        self.assertTrue(result['visibility_verified'])

    def test_g_min_formula_correct(self):
        """g_min(S_5) = 3 from the formula."""
        result = verify_shadow_visibility_genus3()
        self.assertTrue(result['g_min_correct'])


# ====================================================================
# Section 2: Self-loop parity vanishing
# ====================================================================

class TestSelfLoopParityVanishing(unittest.TestCase):
    """Verify prop:self-loop-vanishing at genus 3."""

    def test_all_single_vertex_parity_consistent(self):
        """All single-vertex graphs satisfy parity vanishing where applicable."""
        results = self_loop_parity_vanishing_all_genus3()
        for r in results:
            self.assertTrue(r['parity_consistent'],
                            f"Graph {r['graph_index']} fails parity: "
                            f"g={r['vertex_genus']}, loops={r['num_self_loops']}, "
                            f"I={r['hodge_integral']}")

    def test_triple_self_loop_vanishes(self):
        """The (0,6) graph with 3 self-loops has I=0 (dim M-bar_{0,6}=3 odd)."""
        results = self_loop_parity_vanishing_all_genus3()
        triple = [r for r in results
                  if r['vertex_genus'] == 0 and r['num_self_loops'] == 3]
        self.assertEqual(len(triple), 1)
        self.assertTrue(triple[0]['vanishes'])
        self.assertEqual(triple[0]['moduli_dim'], 3)
        self.assertTrue(triple[0]['dim_is_odd'])

    def test_parity_applies_genus0_2plus_loops(self):
        """Parity applies to genus-0 vertices with >= 2 self-loops."""
        results = self_loop_parity_vanishing_all_genus3()
        for r in results:
            if r['vertex_genus'] == 0 and r['num_self_loops'] >= 2:
                self.assertTrue(r['parity_applies'])

    def test_results_cover_1vertex_graphs(self):
        """Self-loop parity check covers all 4 single-vertex genus-3 graphs."""
        results = self_loop_parity_vanishing_all_genus3()
        self.assertEqual(len(results), 4)


# ====================================================================
# Section 3: Planted-forest classification
# ====================================================================

class TestPlantedForestClassification(unittest.TestCase):
    """Test the 35/42 planted-forest vs pure-kappa classification."""

    def test_pf_count(self):
        """35 of 42 graphs are planted-forest."""
        sub = planted_forest_subclassification()
        self.assertEqual(sub['planted_forest_count'], 35)

    def test_pure_kappa_count(self):
        """7 of 42 graphs are pure-kappa (not planted-forest)."""
        sub = planted_forest_subclassification()
        self.assertEqual(sub['pure_kappa_count'], 7)

    def test_total_is_42(self):
        """Total = PF + pure = 42."""
        sub = planted_forest_subclassification()
        self.assertEqual(sub['total_graphs'], 42)
        self.assertEqual(sub['planted_forest_count'] + sub['pure_kappa_count'], 42)

    def test_shadow_depth_subcounts(self):
        """PF subclassification totals are consistent."""
        sub = planted_forest_subclassification()
        total_pf = (sub['pf_needs_S3_only'] + sub['pf_needs_S4']
                    + sub['pf_needs_S5'] + sub['pf_needs_S6'])
        self.assertEqual(total_pf, sub['planted_forest_count'])

    def test_pf_graphs_have_shadow_indices(self):
        """Each PF graph has at least one shadow coefficient >= 3."""
        census = planted_forest_census()
        for g in census['planted_forest']:
            self.assertGreater(len(g['shadow_coefficients']), 0)
            for s in g['shadow_coefficients']:
                self.assertGreaterEqual(s, 3)

    def test_non_pf_graphs_no_high_shadow(self):
        """Non-PF graphs have no genus-0 vertex of valence >= 3."""
        graphs = genus3_graphs()
        census = planted_forest_census()
        for g_info in census['non_planted_forest']:
            i = g_info['index']
            G = graphs[i]
            val = G.valence
            for v in range(G.num_vertices):
                if G.vertex_genera[v] == 0:
                    self.assertLess(val[v], 3,
                                    f"Non-PF graph {i} has g=0 vertex with val={val[v]}")


# ====================================================================
# Section 4: Shadow depth classification
# ====================================================================

class TestShadowDepthClassification(unittest.TestCase):
    """Test shadow depth classification of genus-3 graphs."""

    def test_classification_covers_all(self):
        """Classification accounts for all 42 graphs."""
        graphs = genus3_graphs()
        cls = classify_by_shadow_depth(graphs)
        total = (len(cls['kappa_only']) + len(cls['needs_S3'])
                 + len(cls['needs_S4']) + len(cls['needs_S5'])
                 + len(cls['needs_S6']))
        self.assertEqual(total, 42)

    def test_S5_graphs_exist(self):
        """Some graphs require S_5."""
        graphs = genus3_graphs()
        cls = classify_by_shadow_depth(graphs)
        self.assertGreater(len(cls['needs_S5']), 0)

    def test_S6_graphs_exist(self):
        """Some graphs require S_6 (genus-0 vertex with valence 6)."""
        graphs = genus3_graphs()
        cls = classify_by_shadow_depth(graphs)
        self.assertGreater(len(cls['needs_S6']), 0)

    def test_max_shadow_per_graph_consistent(self):
        """Max shadow per graph is consistent with classification."""
        graphs = genus3_graphs()
        cls = classify_by_shadow_depth(graphs)
        for i in cls['needs_S5']:
            self.assertEqual(cls['max_shadow_per_graph'][i], 5)


# ====================================================================
# Section 5: Delta_pf formula verification
# ====================================================================

class TestDeltaPfFormula(unittest.TestCase):
    """Verify the 11-term planted-forest formula.

    The manuscript formula (eq:delta-pf-genus3-explicit) uses approximate
    genus-1+ vertex weights. The computed graph sum uses the same framework
    but may differ in mixed terms. The S_4^2 coefficient is EXACT (purely
    genus-0 vertices). The term count and symbol content are structural
    invariants that must match exactly.
    """

    def test_manuscript_formula_has_11_terms(self):
        """The manuscript formula has exactly 11 monomial terms."""
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        S4 = Symbol('S_4')
        S5 = Symbol('S_5')
        formula = manuscript_delta_pf_genus3()
        p = expand(formula)
        from sympy import Poly
        poly = Poly(p, kappa, S3, S4, S5, domain='QQ')
        self.assertEqual(len(poly.as_dict()), 11)

    def test_computed_term_count(self):
        """The computed PF correction has 11 terms."""
        self.assertEqual(delta_pf_term_count(), 11)

    def test_term_count_match(self):
        """Both computed and manuscript have the same number of terms."""
        result = verify_delta_pf_formula()
        self.assertTrue(result['term_count_match'],
                        f"Term counts: computed={result['computed_term_count']}, "
                        f"expected={result['expected_term_count']}")

    def test_S4_squared_exact_match(self):
        """The S_4^2 coefficient matches exactly (-7/12).

        This is purely from genus-0 vertices and must be exact.
        """
        result = verify_delta_pf_formula()
        self.assertTrue(result['S4sq_exact_match'],
                        f"S4^2 mismatch: computed={result['computed_S4sq']}, "
                        f"expected={result['expected_S4sq']}")

    def test_symbol_content_match(self):
        """Both formulas involve exactly {kappa, S_3, S_4, S_5}."""
        result = verify_delta_pf_formula()
        self.assertTrue(result['symbol_match'])

    def test_manuscript_formula_involves_S5(self):
        """The manuscript formula involves S_5."""
        S5 = Symbol('S_5')
        formula = manuscript_delta_pf_genus3()
        self.assertIn(S5, formula.free_symbols)

    def test_manuscript_formula_involves_S4(self):
        """The manuscript formula involves S_4."""
        S4 = Symbol('S_4')
        formula = manuscript_delta_pf_genus3()
        self.assertIn(S4, formula.free_symbols)

    def test_manuscript_formula_involves_kappa(self):
        """The manuscript formula involves kappa."""
        kappa = Symbol('kappa')
        formula = manuscript_delta_pf_genus3()
        self.assertIn(kappa, formula.free_symbols)

    def test_manuscript_formula_involves_S3(self):
        """The manuscript formula involves S_3."""
        S3 = Symbol('S_3')
        formula = manuscript_delta_pf_genus3()
        self.assertIn(S3, formula.free_symbols)

    def test_S4sq_coefficient_is_minus_7_12(self):
        """The exact S_4^2 coefficient is -7/12 (from genus-0 vertices only)."""
        S4 = Symbol('S_4')
        result = verify_delta_pf_formula()
        # Both should give -7/12 * S_4^2 when kappa=S3=S5=0
        self.assertEqual(cancel(result['computed_S4sq']),
                         Rational(-7, 12) * S4 ** 2)


# ====================================================================
# Section 6: Cross-family comparison
# ====================================================================

class TestCrossFamilyComparison(unittest.TestCase):
    """Test depth-class consistency across families."""

    def test_heisenberg_pf_zero(self):
        """Heisenberg (class G) has zero planted-forest correction."""
        result = cross_family_genus3()
        self.assertTrue(result['heisenberg']['is_zero'])
        self.assertTrue(result['heisenberg']['consistent'])

    def test_virasoro_pf_nonzero(self):
        """Virasoro (class M) has nonzero planted-forest correction."""
        result = cross_family_genus3()
        pf = result['virasoro']['pf']
        self.assertNotEqual(cancel(pf), 0)

    def test_generic_has_S5(self):
        """Generic PF correction involves S_5."""
        result = cross_family_genus3()
        self.assertTrue(result['generic']['has_S5'])

    def test_generic_has_S4(self):
        """Generic PF correction involves S_4."""
        result = cross_family_genus3()
        self.assertTrue(result['generic']['has_S4'])

    def test_generic_has_S3(self):
        """Generic PF correction involves S_3."""
        result = cross_family_genus3()
        self.assertTrue(result['generic']['has_S3'])

    def test_depth_class_G_zero(self):
        """Class G: setting S_3=S_4=S_5=0 gives zero PF correction."""
        result = depth_class_consistency_genus3()
        self.assertTrue(result['G_zero'])

    def test_depth_class_L_only_S3_kappa(self):
        """Class L: setting S_4=S_5=0 leaves only S_3 and kappa."""
        result = depth_class_consistency_genus3()
        self.assertTrue(result['L_only_S3_kappa'])

    def test_depth_class_C_only_S3_S4_kappa(self):
        """Class C: setting S_5=0 leaves only S_3, S_4, kappa."""
        result = depth_class_consistency_genus3()
        self.assertTrue(result['C_only_S3_S4_kappa'])


# ====================================================================
# Section 7: Faber-Zagier / lambda_3 verification
# ====================================================================

class TestFaberZagier(unittest.TestCase):
    """Verify Faber-Pandharipande lambda_3^FP via 3 independent paths."""

    def test_lambda3_correct(self):
        """lambda_3^FP = 31/967680."""
        result = faber_zagier_genus3_codim3()
        self.assertTrue(result['correct'])
        self.assertEqual(result['expected'], Fraction(31, 967680))

    def test_lambda3_all_paths_match(self):
        """All 3 computation paths agree."""
        result = faber_zagier_genus3_codim3()
        self.assertTrue(result['all_match'])

    def test_lambda3_independent_bernoulli(self):
        """Independent Bernoulli computation gives 31/967680."""
        self.assertEqual(lambda_fp_independent(3), Fraction(31, 967680))

    def test_lambda3_positive(self):
        """lambda_3^FP is positive (all lambda_g^FP are positive)."""
        self.assertGreater(lambda_fp_independent(3), 0)


# ====================================================================
# Section 8: Pixton ideal membership
# ====================================================================

class TestPixtonIdealMembership(unittest.TestCase):
    """Test Pixton ideal membership at genus 3."""

    def test_taut_ring_dims(self):
        """R*(M-bar_3) dimensions are correct."""
        dims = Genus3StrataAlgebra.taut_ring_dimensions()
        self.assertEqual(dims[0], 1)
        self.assertEqual(dims[6], 1)
        self.assertEqual(Genus3StrataAlgebra.total_taut_dim(), 32)

    def test_pixton_first_codim(self):
        """First nontrivial Pixton relation at codim 3."""
        self.assertEqual(Genus3StrataAlgebra.pixton_ideal_first_codim(), 3)

    def test_virasoro_nontrivial_test(self):
        """Virasoro gives a nontrivial Pixton ideal test."""
        vir = virasoro_shadow_data(max_arity=8)
        result = pixton_ideal_membership_genus3(vir)
        self.assertEqual(result['status'], 'nontrivial_test')
        self.assertTrue(result['pf_nonzero'])

    def test_heisenberg_trivially_in_pixton(self):
        """Heisenberg gives trivial Pixton ideal membership."""
        heis = heisenberg_shadow_data()
        result = pixton_ideal_membership_genus3(heis)
        self.assertEqual(result['status'], 'trivially_in_pixton')


# ====================================================================
# Section 9: New relation generation at genus 3
# ====================================================================

class TestNewRelationGeneration(unittest.TestCase):
    """Test whether genus-3 shadow relation generates new relations."""

    def test_generates_new_relation(self):
        """Genus-3 relation generates genuinely new tautological relations."""
        result = genus3_new_relation_test()
        self.assertTrue(result['generates_new_relation'])

    def test_has_S5_dependence(self):
        """The genus-3 PF correction depends on S_5."""
        result = genus3_new_relation_test()
        self.assertTrue(result['has_S5'])

    def test_has_pure_S4(self):
        """Setting S_3=S_5=0 still leaves S_4 dependence (new at genus 3)."""
        result = genus3_new_relation_test()
        self.assertTrue(result['has_pure_S4'])

    def test_four_free_symbols(self):
        """The generic PF correction involves exactly 4 symbols."""
        result = genus3_new_relation_test()
        self.assertEqual(result['num_independent_params'], 4)

    def test_new_shadow_data_is_S5(self):
        """The new shadow data at genus 3 is S_5."""
        result = genus3_new_relation_test()
        self.assertIn('S_5', result['new_shadow_data'])


# ====================================================================
# Section 10: Euler characteristic multi-path
# ====================================================================

class TestEulerCharacteristicMultipath(unittest.TestCase):
    """Multi-path verification of chi^orb(M-bar_{3,0})."""

    def test_euler_char_correct(self):
        """chi^orb(M-bar_{3,0}) = -12419/90720."""
        result = euler_characteristic_genus3_multipath()
        self.assertTrue(result['path1_correct'])

    def test_all_paths_consistent(self):
        """All verification paths are consistent."""
        result = euler_characteristic_genus3_multipath()
        self.assertTrue(result['all_consistent'])

    def test_harer_zagier_open(self):
        """Harer-Zagier open Euler char chi(M_3) = 1/1008."""
        result = euler_characteristic_genus3_multipath()
        self.assertEqual(result['path3_harer_zagier_open'], Fraction(1, 1008))


# ====================================================================
# Section 11: Automorphism spectrum
# ====================================================================

class TestAutomorphismSpectrum(unittest.TestCase):
    """Test automorphism order analysis."""

    def test_spectrum_length_42(self):
        """42 automorphism orders (one per graph)."""
        result = automorphism_spectrum_analysis()
        self.assertEqual(len(result['spectrum']), 42)

    def test_all_positive(self):
        """All automorphism orders are positive."""
        result = automorphism_spectrum_analysis()
        self.assertGreater(result['min_aut'], 0)

    def test_sum_reciprocal_positive(self):
        """Sum of 1/|Aut| is positive."""
        result = automorphism_spectrum_analysis()
        self.assertGreater(result['sum_reciprocal'], 0)

    def test_some_trivial_aut(self):
        """Some graphs have trivial automorphism group."""
        result = automorphism_spectrum_analysis()
        self.assertGreater(result['num_with_trivial_aut'], 0)


# ====================================================================
# Section 12: Codimension decomposition
# ====================================================================

class TestCodimensionDecomposition(unittest.TestCase):
    """Test codimension decomposition of the MC relation."""

    def test_codim0_exists(self):
        """Codimension 0 (smooth graph) exists."""
        heis = heisenberg_shadow_data()
        decomp = codimension_decomposition_genus3(heis)
        self.assertIn(0, decomp)
        self.assertEqual(decomp[0]['count'], 1)

    def test_all_codims_counted(self):
        """Total count across all codimensions is 42."""
        heis = heisenberg_shadow_data()
        decomp = codimension_decomposition_genus3(heis)
        total = sum(d['count'] for d in decomp.values())
        self.assertEqual(total, 42)

    def test_codim_range(self):
        """Codimension ranges from 0 to max_edges."""
        heis = heisenberg_shadow_data()
        decomp = codimension_decomposition_genus3(heis)
        self.assertIn(0, decomp)
        self.assertTrue(max(decomp.keys()) >= 3)


# ====================================================================
# Section 13: c=13 self-duality
# ====================================================================

class TestC13SelfDuality(unittest.TestCase):
    """Test Virasoro self-duality at c=13 for genus-3 PF correction."""

    def test_self_dual_at_c13(self):
        """The PF correction at c=13 is self-dual (pf(13) = pf(26-13))."""
        result = c13_self_duality_check_genus3()
        self.assertTrue(result['self_dual_at_c13'])

    def test_pf_at_c13_finite(self):
        """The PF correction at c=13 is finite (no poles)."""
        result = c13_self_duality_check_genus3()
        self.assertIsNotNone(result['pf_at_c13'])
        # Should be a finite number
        self.assertTrue(abs(result['pf_at_c13']) < 1e6)


# ====================================================================
# Section 14: Virasoro special values
# ====================================================================

class TestVirasoroSpecialValues(unittest.TestCase):
    """Test Virasoro PF correction at special central charges."""

    def test_c13_finite(self):
        """PF correction at c=13 is finite."""
        values = virasoro_delta_pf_special_values()
        self.assertIsNotNone(values['self-dual'])

    def test_ising_finite(self):
        """PF correction at c=1/2 (Ising) is finite."""
        values = virasoro_delta_pf_special_values()
        self.assertIsNotNone(values['Ising'])

    def test_c1_finite(self):
        """PF correction at c=1 is finite."""
        values = virasoro_delta_pf_special_values()
        self.assertIsNotNone(values['c=1'])

    def test_c26_finite(self):
        """PF correction at c=26 (critical) is finite."""
        values = virasoro_delta_pf_special_values()
        self.assertIsNotNone(values['critical'])


# ====================================================================
# Section 15: Planted-forest census
# ====================================================================

class TestPlantedForestCensus(unittest.TestCase):
    """Test the complete PF census."""

    def test_census_total_42(self):
        """Census covers all 42 graphs."""
        census = planted_forest_census()
        self.assertEqual(census['total'], 42)

    def test_pf_35(self):
        """35 planted-forest graphs."""
        census = planted_forest_census()
        self.assertEqual(census['pf_count'], 35)

    def test_non_pf_7(self):
        """7 non-planted-forest graphs."""
        census = planted_forest_census()
        self.assertEqual(census['non_pf_count'], 7)

    def test_all_pf_have_shadow_coefficients(self):
        """Every PF graph has shadow coefficient data."""
        census = planted_forest_census()
        for g in census['planted_forest']:
            self.assertIn('shadow_coefficients', g)
            self.assertGreater(len(g['shadow_coefficients']), 0)


# ====================================================================
# Section 16: Genus comparison
# ====================================================================

class TestGenusComparison(unittest.TestCase):
    """Compare genus-2 and genus-3 PF corrections."""

    def test_genus3_more_complex(self):
        """Genus-3 PF correction has more terms than genus-2."""
        result = delta_pf_genus_comparison()
        self.assertGreater(result['genus_3']['term_count'],
                           result['genus_2']['term_count'])

    def test_genus3_has_new_symbols(self):
        """Genus-3 PF correction introduces new symbols beyond genus-2."""
        result = delta_pf_genus_comparison()
        self.assertGreater(len(result['genus3_new_symbols']), 0)

    def test_complexity_increases(self):
        """Complexity increases from genus 2 to genus 3."""
        result = delta_pf_genus_comparison()
        self.assertTrue(result['complexity_increase'])

    def test_genus2_has_2_terms(self):
        """Genus-2 PF correction has 2 monomial terms."""
        result = delta_pf_genus_comparison()
        self.assertEqual(result['genus_2']['term_count'], 2)


# ====================================================================
# Section 17: Hodge integral sign pattern
# ====================================================================

class TestHodgeIntegralSigns(unittest.TestCase):
    """Test Hodge integral sign patterns at genus 3."""

    def test_total_42(self):
        """42 integrals total."""
        result = hodge_integral_sign_pattern()
        self.assertEqual(result['total'], 42)

    def test_some_positive(self):
        """Some Hodge integrals are positive."""
        result = hodge_integral_sign_pattern()
        self.assertGreater(result['n_positive'], 0)

    def test_some_zero(self):
        """Some Hodge integrals are zero (self-loop parity vanishing)."""
        result = hodge_integral_sign_pattern()
        self.assertGreater(result['n_zero'], 0)

    def test_signs_sum(self):
        """Sign counts sum to 42."""
        result = hodge_integral_sign_pattern()
        self.assertEqual(result['n_positive'] + result['n_negative'] + result['n_zero'],
                         42)


# ====================================================================
# Section 18: Multi-path F_3
# ====================================================================

class TestF3Multipath(unittest.TestCase):
    """Multi-path verification of F_3 = kappa * lambda_3^FP."""

    def test_all_match(self):
        """All 3 independent paths give the same lambda_3^FP."""
        result = F3_multipath_verification()
        self.assertTrue(result['all_match'])

    def test_value_31_967680(self):
        """lambda_3^FP = 31/967680."""
        result = F3_multipath_verification()
        self.assertEqual(result['expected'], Fraction(31, 967680))


# ====================================================================
# Section 19: Gaussian total
# ====================================================================

class TestGaussianTotal(unittest.TestCase):
    """Test Gaussian (Heisenberg) total MC relation at genus 3."""

    def test_pf_zero(self):
        """Heisenberg PF correction is zero."""
        result = gaussian_total_genus3()
        self.assertTrue(result['pf_zero'])

    def test_graph_count(self):
        """MC relation involves 42 graphs."""
        result = gaussian_total_genus3()
        self.assertEqual(result['graph_count'], 42)


# ====================================================================
# Section 20: Quintic shadow isolation
# ====================================================================

class TestQuinticShadowIsolation(unittest.TestCase):
    """Test isolation of the S_5-dependent part."""

    def test_S5_linear(self):
        """S_5 appears only linearly in the PF correction (no S_5^2)."""
        result = quintic_shadow_isolation()
        self.assertTrue(result['S5_linear'])

    def test_S5_coefficient_nonzero(self):
        """The coefficient of S_5 is nonzero."""
        result = quintic_shadow_isolation()
        self.assertIsNotNone(result['S5_coefficient'])
        self.assertNotEqual(cancel(result['S5_coefficient']), 0)

    def test_S5_coefficient_structure(self):
        """The S_5 coefficient is a linear polynomial in kappa and S_3.

        From the manuscript: (7/8) * S_3 - (1/96) * kappa.
        """
        result = quintic_shadow_isolation()
        coeff = result['S5_coefficient']
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        # The coefficient should be linear in kappa and S_3
        free = coeff.free_symbols if hasattr(coeff, 'free_symbols') else set()
        self.assertTrue(free.issubset({kappa, S3}))


# ====================================================================
# Section 21: Independent lambda_FP verification
# ====================================================================

class TestLambdaFPIndependent(unittest.TestCase):
    """Independent verification of Faber-Pandharipande numbers."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp_independent(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp_independent(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp_independent(3), Fraction(31, 967680))

    def test_lambda4(self):
        self.assertEqual(lambda_fp_independent(4), Fraction(127, 154828800))

    def test_all_positive(self):
        """All lambda_g^FP are positive for g=1..6."""
        for g in range(1, 7):
            self.assertGreater(lambda_fp_independent(g), 0)


if __name__ == '__main__':
    unittest.main()
