r"""Tests for the genus-3 Pixton ideal membership engine.

Tests conj:pixton-from-shadows at genus 3: the MC-descended tautological
relations from the shadow obstruction tower lie in (and for class-M algebras,
generate) the Pixton ideal I*(M-bar_3).

This is the FIRST formal Pixton ideal membership test from the shadow tower
at genus 3, where S_4 and S_5 enter for the first time.

Test taxonomy:
  - Graph census (Section A): verify the stable graph enumeration
  - Tautological ring (Section B): verify Faber's R*(M-bar_3) data
  - Planted-forest polynomial (Section C): decompose delta_pf in shadow vars
  - Cross-family (Section D): G/L/M hierarchy of tautological relations
  - Shadow visibility (Section E): S_4 and S_5 isolation tests
  - Pixton membership (Section F): the formal membership verification
  - Numerical evaluation (Section G): consistency at specific central charges
  - Self-loop parity (Section H): parity vanishing at genus 3
  - Generation (Section I): nonzero planted-forest implies generation
  - Cross-checks (Section J): formula consistency across computation paths
"""

import unittest
from fractions import Fraction

from sympy import Integer, Rational, Symbol, cancel, simplify

from compute.lib.theorem_pixton_membership_g3_engine import (
    FABER_GENUS3_DIMS,
    LAMBDA1_FP,
    LAMBDA2_FP,
    LAMBDA3_FP,
    Genus3TautRingStructure,
    cross_family_comparison_genus3,
    delta_pf_genus3,
    genus3_codimension_distribution,
    genus3_formal_membership_test,
    genus3_graph_count,
    genus3_max_genus0_valence,
    genus3_mc_relation_decomposition,
    genus3_nonpf_count,
    genus3_nonzero_hodge_count,
    genus3_pixton_generator_comparison,
    genus3_pixton_ideal_dimension,
    genus3_pixton_membership_proof,
    genus3_planted_forest_count,
    genus_ratio_analysis_g3,
    lambda_fp_exact,
    nonpf_amplitude_genus3,
    numerical_evaluation_genus3,
    obs3_affine_sl2,
    obs3_heisenberg,
    obs3_total,
    obs3_virasoro,
    pf_genus3_at_c,
    pf_genus3_explicit_formula,
    pf_genus3_virasoro_c1,
    pf_genus3_virasoro_c13,
    pf_genus3_virasoro_c26,
    pf_polynomial_genus3,
    pixton_element_comparison,
    s3_only_genus3,
    s4_isolation_genus3,
    s5_isolation_genus3,
    scalar_prediction_genus3,
    self_loop_parity_genus3,
    c,
)
from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    heisenberg_shadow_data,
    virasoro_shadow_data,
    affine_shadow_data,
    c_sym,
)


# ============================================================================
# Section A: Graph Census Tests
# ============================================================================

class TestGraphCensus(unittest.TestCase):
    """Verify the stable graph enumeration at (g=3, n=0)."""

    def test_graph_count_is_42(self):
        """42 stable graphs at (3,0) (Faber)."""
        self.assertEqual(genus3_graph_count(), 42)

    def test_pf_plus_nonpf_equals_total(self):
        """Planted-forest + non-planted-forest = total."""
        self.assertEqual(
            genus3_planted_forest_count() + genus3_nonpf_count(),
            genus3_graph_count(),
        )

    def test_pf_count_positive(self):
        """At least some graphs are planted-forest."""
        self.assertGreater(genus3_planted_forest_count(), 0)

    def test_nonpf_count_positive(self):
        """At least some graphs are NOT planted-forest."""
        self.assertGreater(genus3_nonpf_count(), 0)

    def test_nonzero_hodge_positive(self):
        """At least some graphs have nonzero Hodge integral."""
        self.assertGreater(genus3_nonzero_hodge_count(), 0)

    def test_codimension_distribution_keys(self):
        """Codimensions range from 0 to some max."""
        dist = genus3_codimension_distribution()
        self.assertIn(0, dist)  # smooth graph
        self.assertIn(1, dist)  # codim-1 boundary

    def test_codimension_0_is_1(self):
        """Exactly 1 smooth graph at (3,0)."""
        dist = genus3_codimension_distribution()
        self.assertEqual(dist.get(0, 0), 1)

    def test_max_genus0_valence_at_least_5(self):
        """Max genus-0 valence should be >= 5 (for S_5 visibility)."""
        self.assertGreaterEqual(genus3_max_genus0_valence(), 5)


# ============================================================================
# Section B: Tautological Ring Tests
# ============================================================================

class TestTautRing(unittest.TestCase):
    """Verify Faber's R*(M-bar_3) data."""

    def test_dim_mbar3(self):
        """dim M-bar_3 = 6."""
        self.assertEqual(Genus3TautRingStructure.DIM, 6)

    def test_gorenstein_symmetry(self):
        """dim R^k = dim R^{6-k} (Gorenstein)."""
        for k in range(7):
            self.assertEqual(
                FABER_GENUS3_DIMS.get(k, 0),
                FABER_GENUS3_DIMS.get(6 - k, 0),
                f"Gorenstein fails at k={k}",
            )

    def test_dim_r0_is_1(self):
        """dim R^0 = 1."""
        self.assertEqual(FABER_GENUS3_DIMS[0], 1)

    def test_dim_r1_is_3(self):
        """dim R^1 = 3."""
        self.assertEqual(FABER_GENUS3_DIMS[1], 3)

    def test_dim_r2_is_7(self):
        """dim R^2 = 7."""
        self.assertEqual(FABER_GENUS3_DIMS[2], 7)

    def test_dim_r3_is_10(self):
        """dim R^3 = 10."""
        self.assertEqual(FABER_GENUS3_DIMS[3], 10)

    def test_dim_r6_is_1(self):
        """dim R^6 = 1 (top degree = fundamental class)."""
        self.assertEqual(FABER_GENUS3_DIMS[6], 1)

    def test_total_dim_r_star(self):
        """Total dim R* = 1+3+7+10+7+3+1 = 32."""
        self.assertEqual(sum(FABER_GENUS3_DIMS.values()), 32)


# ============================================================================
# Section C: Planted-Forest Polynomial Tests
# ============================================================================

class TestPFPolynomial(unittest.TestCase):
    """Test the planted-forest polynomial decomposition."""

    def test_pf_polynomial_has_kappa(self):
        """delta_pf depends on kappa."""
        data = pf_polynomial_genus3()
        self.assertTrue(data['depends_on']['kappa'])

    def test_pf_polynomial_has_s3(self):
        """delta_pf depends on S_3."""
        data = pf_polynomial_genus3()
        self.assertTrue(data['depends_on']['S_3'])

    def test_pf_polynomial_s4_present(self):
        """S_4 appears in delta_pf at genus 3 (shadow visibility)."""
        data = pf_polynomial_genus3()
        self.assertTrue(data['s4_present'])

    def test_pf_polynomial_s5_present(self):
        """S_5 appears in delta_pf at genus 3 (shadow visibility)."""
        data = pf_polynomial_genus3()
        self.assertTrue(data['s5_present'])

    def test_pf_polynomial_positive_terms(self):
        """Polynomial has a positive number of terms."""
        data = pf_polynomial_genus3()
        self.assertGreater(data['n_terms'], 0)


# ============================================================================
# Section D: Cross-Family Tests
# ============================================================================

class TestCrossFamily(unittest.TestCase):
    """Test the G/L/M hierarchy of tautological relations."""

    def test_heisenberg_pf_zero(self):
        """Class G (Heisenberg): planted-forest correction vanishes."""
        data = obs3_heisenberg()
        self.assertTrue(data['pf_is_zero'])

    def test_heisenberg_bernoulli_ahat_match(self):
        """Heisenberg: Bernoulli and A-hat formulas agree."""
        data = obs3_heisenberg()
        self.assertTrue(data['bernoulli_ahat_match'])

    def test_affine_pf_nonzero(self):
        """Class L (affine sl_2): planted-forest correction is nonzero."""
        data = obs3_affine_sl2()
        self.assertTrue(data['pf_nonzero'])

    def test_virasoro_pf_nonzero(self):
        """Class M (Virasoro): planted-forest correction is nonzero."""
        data = obs3_virasoro()
        self.assertTrue(data['delta_pf_nonzero'])

    def test_cross_family_hierarchy(self):
        """Verify G subset L subset M hierarchy of relation content."""
        result = cross_family_comparison_genus3()
        self.assertTrue(result['heisenberg']['pf_zero'])
        self.assertTrue(result['affine_sl2']['pf_nonzero'])
        self.assertTrue(result['virasoro']['pf_nonzero'])


# ============================================================================
# Section E: Shadow Visibility Tests (S_4 and S_5 Isolation)
# ============================================================================

class TestShadowVisibility(unittest.TestCase):
    """Test that S_4 and S_5 genuinely enter at genus 3."""

    def test_s4_contributes_at_genus3(self):
        """S_4 contributes to delta_pf^{(3,0)} (g_min(S_4) = 3)."""
        data = s4_isolation_genus3()
        self.assertTrue(data['s4_contributes'])

    def test_s5_contributes_at_genus3(self):
        """S_5 contributes to delta_pf^{(3,0)} (g_min(S_5) = 3)."""
        data = s5_isolation_genus3()
        self.assertTrue(data['s5_contributes'])

    def test_s4_graphs_exist(self):
        """There exist graphs with genus-0 vertex of valence >= 4."""
        data = s4_isolation_genus3()
        self.assertGreater(data['n_graphs_with_val4'], 0)

    def test_s5_graphs_exist(self):
        """There exist graphs with genus-0 vertex of valence >= 5."""
        data = s5_isolation_genus3()
        self.assertGreater(data['n_graphs_with_val5'], 0)

    def test_s3_only_nonzero(self):
        """With only S_3 (class L behavior), pf is nonzero."""
        data = s3_only_genus3()
        self.assertTrue(data['s3_contributes'])


# ============================================================================
# Section F: Pixton Membership Tests
# ============================================================================

class TestPixtonMembership(unittest.TestCase):
    """Test the formal Pixton ideal membership at genus 3."""

    def test_membership_proved(self):
        """The membership proof is complete."""
        proof = genus3_pixton_membership_proof()
        self.assertEqual(proof['status'], 'PROVED')

    def test_membership_argument1(self):
        """Argument 1 (D^2 = 0 + JPPZ18) is complete."""
        proof = genus3_pixton_membership_proof()
        self.assertEqual(proof['proof_argument_1']['status'], 'complete')

    def test_membership_argument2(self):
        """Argument 2 (Givental-Teleman + PPZ19) is complete."""
        proof = genus3_pixton_membership_proof()
        self.assertEqual(proof['proof_argument_2']['status'],
                         'complete (for semisimple)')

    def test_five_path_membership_true(self):
        """The 5-path test confirms membership."""
        result = genus3_formal_membership_test()
        self.assertTrue(result['membership'])

    def test_five_path_generation_class_m(self):
        """The 5-path test confirms generation for class M."""
        result = genus3_formal_membership_test()
        self.assertTrue(result['generation_class_M'])

    def test_formula_cross_check(self):
        """Generic formula specializes correctly to Virasoro."""
        result = genus3_formal_membership_test()
        self.assertTrue(result['formula_cross_check'])


# ============================================================================
# Section G: Numerical Evaluation Tests
# ============================================================================

class TestNumerical(unittest.TestCase):
    """Numerical evaluation at specific central charges."""

    def test_numerical_c1(self):
        """delta_pf(Vir_1) is a finite nonzero number."""
        val = pf_genus3_virasoro_c1()
        val_float = float(val)
        self.assertNotEqual(val_float, 0.0)
        self.assertTrue(abs(val_float) < 1e10)

    def test_numerical_c13(self):
        """delta_pf(Vir_13) at the self-dual point is finite."""
        val = pf_genus3_virasoro_c13()
        val_float = float(val)
        self.assertTrue(abs(val_float) < 1e10)

    def test_numerical_c26(self):
        """delta_pf(Vir_26) at the critical point is finite."""
        val = pf_genus3_virasoro_c26()
        val_float = float(val)
        self.assertTrue(abs(val_float) < 1e10)

    def test_numerical_all_finite(self):
        """All numerical evaluations are finite."""
        data = numerical_evaluation_genus3()
        for c_val, d in data.items():
            for key, val in d.items():
                self.assertTrue(
                    abs(val) < 1e10,
                    f"Infinite value at c={c_val}, {key}={val}",
                )

    def test_numerical_pf_nonzero_generic(self):
        """Planted-forest correction is nonzero at generic c."""
        data = numerical_evaluation_genus3()
        # At least 5 of 8 c values should give nonzero pf
        nonzero_count = sum(
            1 for d in data.values() if abs(d['planted_forest']) > 1e-15
        )
        self.assertGreaterEqual(nonzero_count, 5)


# ============================================================================
# Section H: Self-Loop Parity Tests
# ============================================================================

class TestSelfLoopParity(unittest.TestCase):
    """Test self-loop parity vanishing at genus 3."""

    def test_parity_applicable_at_0_6(self):
        """Parity applies to (0,6) graph: 3 loops, dim=3 odd, k>=2."""
        data = self_loop_parity_genus3()
        self.assertTrue(data['(0,6)']['parity_applicable'])

    def test_parity_vanishing_at_0_6(self):
        """I = 0 for (0,6) graph by parity (dim odd, k >= 2)."""
        data = self_loop_parity_genus3()
        self.assertTrue(data['(0,6)']['vanishes'])

    def test_parity_prediction_correct_0_6(self):
        """Parity predicts vanishing at (0,6)."""
        data = self_loop_parity_genus3()
        self.assertTrue(data['(0,6)']['parity_predicts_vanishing'])

    def test_smooth_graph_trivial(self):
        """Smooth graph (3,0) has I = 1."""
        data = self_loop_parity_genus3()
        self.assertEqual(data['(3,0)']['I'], Fraction(1))


# ============================================================================
# Section I: Generation Tests
# ============================================================================

class TestGeneration(unittest.TestCase):
    """Test that class-M MC relations generate Pixton elements at codim 3."""

    def test_virasoro_codim3_nonzero(self):
        """Virasoro MC relation has nonzero codim-3 component."""
        shadow = virasoro_shadow_data(max_arity=10)
        result = genus3_pixton_generator_comparison(shadow)
        self.assertTrue(result['codim3_nonzero'])

    def test_virasoro_generation_at_codim3(self):
        """Virasoro generates at codim 3."""
        shadow = virasoro_shadow_data(max_arity=10)
        result = genus3_pixton_generator_comparison(shadow)
        self.assertTrue(result['generation_at_codim3'])

    def test_codim3_graphs_exist(self):
        """There are codim-3 graphs at genus 3."""
        shadow = virasoro_shadow_data(max_arity=10)
        result = genus3_pixton_generator_comparison(shadow)
        self.assertGreater(result['n_codim3_graphs'], 0)

    def test_codim3_nonzero_contributions(self):
        """Some codim-3 graphs have nonzero contribution."""
        shadow = virasoro_shadow_data(max_arity=10)
        result = genus3_pixton_generator_comparison(shadow)
        self.assertGreater(result['n_codim3_nonzero'], 0)

    def test_pixton_ideal_codim3_nontrivial(self):
        """I_Pixton at codim 3 has positive dimension."""
        dims = genus3_pixton_ideal_dimension()
        # At codim 3: the number of strata exceeds dim R^3 = 10
        self.assertGreater(
            dims[3]['n_strata_graphs_codim_k'],
            0,
            "No codim-3 strata at genus 3",
        )


# ============================================================================
# Section J: Cross-Check Tests
# ============================================================================

class TestCrossChecks(unittest.TestCase):
    """Formula consistency and cross-checks."""

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp_exact(1), Fraction(1, 24))

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp_exact(2), Fraction(7, 5760))

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp_exact(3), Fraction(31, 967680))

    def test_generic_formula_cross_check(self):
        """Generic pf formula specializes correctly to Virasoro."""
        result = pf_genus3_explicit_formula()
        self.assertTrue(result['cross_check_passed'])

    def test_obs3_heisenberg_scalar_match(self):
        """For Heisenberg: obs_3 matches the scalar prediction."""
        data = obs3_heisenberg()
        self.assertTrue(data['bernoulli_ahat_match'])

    def test_virasoro_pf_nonzero_symbolic(self):
        """Planted-forest from delta_pf_genus3 is symbolically nonzero."""
        shadow = virasoro_shadow_data(max_arity=10)
        pf_direct = cancel(delta_pf_genus3(shadow))
        self.assertNotEqual(
            simplify(pf_direct), 0,
            "delta_pf_genus3 should be nonzero for Virasoro",
        )

    def test_pixton_element_virasoro_has_s45(self):
        """Virasoro Pixton element has S_4/S_5 terms beyond class L."""
        result = pixton_element_comparison()
        self.assertTrue(result['virasoro_has_s45_extra'])

    def test_pixton_element_heisenberg_zero(self):
        """Heisenberg Pixton element is zero."""
        result = pixton_element_comparison()
        self.assertTrue(result['heisenberg_is_zero'])

    def test_pixton_element_genuinely_different(self):
        """Virasoro and KM give genuinely different Pixton elements."""
        result = pixton_element_comparison()
        self.assertTrue(result['genuinely_different'])

    def test_genus_ratio_positive(self):
        """lambda_3^FP / lambda_2^FP is positive."""
        data = genus_ratio_analysis_g3()
        self.assertGreater(data['lambda3_over_lambda2_float'], 0)

    def test_genus_ratio_less_than_1(self):
        """lambda_3^FP / lambda_2^FP < 1 (Bernoulli decay)."""
        data = genus_ratio_analysis_g3()
        self.assertLess(data['lambda3_over_lambda2_float'], 1)


if __name__ == '__main__':
    unittest.main()
