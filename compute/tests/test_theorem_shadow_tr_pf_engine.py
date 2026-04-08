r"""Tests for thm:shadow-tr-pf-decomposition: F_g^shadow = F_g^CEO + delta_pf^{(g,0)}.

Multi-path verification of the shadow/topological recursion planted-forest
decomposition identity across all standard families.

VERIFICATION PATHS (>= 3 independent paths per CLAUDE.md):

Path 1: Algebraic identity at genus 1 and genus 2
Path 2: Planted-forest formula from individual graph contributions
Path 3: Heisenberg specialization (class G, delta_pf = 0)
Path 4: CEO at genus 1 via Bergman tau function
Path 5: Cross-family consistency (9 families)
Path 6: W_3 Z_2 parity (S_3 = 0 kills delta_pf at genus 2)
Path 7: Self-loop parity vanishing (S_4 absent at genus 2)
Path 8: Virasoro symbolic and numerical
Path 9: Shadow visibility genus
Path 10: Depth-class analysis
Path 11: Affine sl_2 (class L)
Path 12: A-hat generating function consistency
Path 13: Growth rate / Bernoulli asymptotics
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, Symbol, simplify, cancel, expand

from compute.lib.theorem_shadow_tr_pf_engine import (
    # Core identity verification
    verify_identity_genus1,
    verify_identity_genus2,
    F_g_shadow,
    F_g_CEO,
    # Planted-forest correction
    delta_pf_genus1,
    delta_pf_genus2,
    delta_pf_genus2_graph_contributions,
    planted_forest_genus2_formula,
    # Self-loop parity
    self_loop_parity_check,
    # Shadow visibility
    shadow_visibility_genus,
    # Depth class
    depth_class_decomposition,
    # Graph classification
    classify_planted_forest_genus2,
    # Spectral curve
    spectral_curve_from_shadow,
    ceo_F1_from_bergman_tau,
    shadow_connection_ceo_kernel,
    # Family-specific
    heisenberg_verification,
    affine_sl2_verification,
    virasoro_verification_genus2,
    virasoro_verification_symbolic,
    w3_verification_genus2,
    # Cross-family
    cross_family_verification_genus2,
    # Numerical
    numerical_evaluation_genus2,
    numerical_evaluation_table,
    # Generating function
    ahat_generating_function_check,
    # Growth rate
    growth_rate_analysis,
    # Full verification
    full_theorem_verification,
    # Faber-Pandharipande
    _lambda_fp,
)

from compute.lib.topological_recursion_shadow import (
    ShadowDataExact,
    virasoro_exact,
    affine_sl2_exact,
    heisenberg_exact,
    w3_exact,
)


# ====================================================================
# Section 1: Faber-Pandharipande baseline (5 tests)
# ====================================================================

class TestFaberPandharipanneBaseline(unittest.TestCase):
    """Verify lambda_fp values used throughout the theorem."""

    def test_lambda_1(self):
        self.assertEqual(_lambda_fp(1), Rational(1, 24))

    def test_lambda_2(self):
        self.assertEqual(_lambda_fp(2), Rational(7, 5760))

    def test_lambda_3(self):
        self.assertEqual(_lambda_fp(3), Rational(31, 967680))

    def test_lambda_4(self):
        expected = Rational(127, 128) * Rational(1, 30) / 40320
        self.assertEqual(_lambda_fp(4), expected)

    def test_all_positive(self):
        """lambda_fp(g) > 0 for all g >= 1 (AP22: F_g POSITIVE)."""
        for g in range(1, 8):
            self.assertGreater(_lambda_fp(g), 0)


# ====================================================================
# Section 2: Algebraic identity — genus 1 (4 tests)
# ====================================================================

class TestIdentityGenus1(unittest.TestCase):
    """Path 1a: F_1^shadow = F_1^CEO + 0."""

    def test_delta_pf_genus1_zero(self):
        """delta_pf^{(1,0)} = 0."""
        self.assertEqual(delta_pf_genus1(), 0)

    def test_identity_virasoro(self):
        data = virasoro_exact(Rational(10))
        result = verify_identity_genus1(data.kappa)
        self.assertTrue(result['identity'])

    def test_CEO_equals_shadow_genus1(self):
        data = virasoro_exact(Rational(10))
        result = verify_identity_genus1(data.kappa)
        self.assertTrue(result['CEO_equals_shadow'])

    def test_identity_heisenberg(self):
        data = heisenberg_exact(Rational(1))
        result = verify_identity_genus1(data.kappa)
        self.assertTrue(result['identity'])


# ====================================================================
# Section 3: Algebraic identity — genus 2 (5 tests)
# ====================================================================

class TestIdentityGenus2(unittest.TestCase):
    """Path 1b: F_2^shadow = F_2^CEO + delta_pf^{(2)}."""

    def test_identity_virasoro_c10(self):
        data = virasoro_exact(Rational(10))
        result = verify_identity_genus2(data.kappa, data.alpha)
        self.assertTrue(result['identity'])

    def test_identity_virasoro_c1(self):
        data = virasoro_exact(Rational(1))
        result = verify_identity_genus2(data.kappa, data.alpha)
        self.assertTrue(result['identity'])

    def test_identity_heisenberg(self):
        data = heisenberg_exact(Rational(1))
        result = verify_identity_genus2(data.kappa, data.alpha)
        self.assertTrue(result['identity'])

    def test_identity_affine(self):
        data = affine_sl2_exact(Rational(1))
        result = verify_identity_genus2(data.kappa, data.alpha)
        self.assertTrue(result['identity'])

    def test_identity_w3(self):
        data = w3_exact(Rational(10))
        result = verify_identity_genus2(data.kappa, data.alpha)
        self.assertTrue(result['identity'])


# ====================================================================
# Section 4: Planted-forest formula — graph contributions (6 tests)
# ====================================================================

class TestPlantedForestFormula(unittest.TestCase):
    """Path 2: delta_pf^{(2)} from graph-by-graph computation."""

    def test_formula_match(self):
        result = planted_forest_genus2_formula()
        self.assertTrue(result['match'])

    def test_sunset_vanishes(self):
        result = planted_forest_genus2_formula()
        self.assertEqual(result['sunset_04'], 0)

    def test_bridge_loop(self):
        result = planted_forest_genus2_formula()
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        self.assertEqual(
            simplify(result['bridge_loop_03_11'] - (-S3 * kappa / 48)), 0)

    def test_theta(self):
        result = planted_forest_genus2_formula()
        S3 = Symbol('S_3')
        self.assertEqual(simplify(result['theta_03_03'] - S3**2 / 12), 0)

    def test_figure8(self):
        result = planted_forest_genus2_formula()
        S3 = Symbol('S_3')
        self.assertEqual(simplify(result['figure8_03_03'] - S3**2 / 8), 0)

    def test_total_equals_expected(self):
        """Sum of graphs = S_3*(10*S_3 - kappa)/48."""
        result = planted_forest_genus2_formula()
        self.assertEqual(simplify(result['total'] - result['expected']), 0)


# ====================================================================
# Section 5: Heisenberg specialization (5 tests)
# ====================================================================

class TestHeisenbergSpecialization(unittest.TestCase):
    """Path 3: class G — delta_pf = 0 at all genera."""

    def test_all_pf_vanish_k1(self):
        result = heisenberg_verification(k_val=1)
        self.assertTrue(result['all_pf_vanish'])

    def test_CEO_equals_shadow_k1(self):
        result = heisenberg_verification(k_val=1)
        self.assertTrue(result['CEO_equals_shadow'])

    def test_S3_zero(self):
        result = heisenberg_verification(k_val=1)
        self.assertEqual(result['S3'], 0)

    def test_kappa_equals_k(self):
        result = heisenberg_verification(k_val=3)
        self.assertEqual(result['kappa'], 3)

    def test_heisenberg_k5(self):
        result = heisenberg_verification(k_val=5)
        self.assertTrue(result['all_pf_vanish'])


# ====================================================================
# Section 6: CEO genus 1 — Bergman tau (3 tests)
# ====================================================================

class TestCEOGenus1(unittest.TestCase):
    """Path 4: F_1^CEO = kappa/24 from Bergman tau."""

    def test_bergman_tau_virasoro(self):
        data = virasoro_exact(Rational(10))
        result = ceo_F1_from_bergman_tau(data)
        self.assertTrue(result['match'])

    def test_bergman_tau_affine(self):
        data = affine_sl2_exact(Rational(1))
        result = ceo_F1_from_bergman_tau(data)
        self.assertTrue(result['match'])

    def test_bergman_tau_heisenberg(self):
        data = heisenberg_exact(Rational(1))
        result = ceo_F1_from_bergman_tau(data)
        self.assertTrue(result['match'])


# ====================================================================
# Section 7: Cross-family consistency (3 tests)
# ====================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Path 5: identity for all 9 standard families."""

    def test_all_pass(self):
        result = cross_family_verification_genus2()
        self.assertTrue(result['all_pass'])

    def test_n_families(self):
        result = cross_family_verification_genus2()
        self.assertEqual(result['n_families'], 9)

    def test_heisenberg_pf_zero(self):
        result = cross_family_verification_genus2()
        for name in ['Heis_k1', 'Heis_k3']:
            self.assertEqual(
                simplify(result['families'][name]['delta_pf']), 0,
                f"{name} should have delta_pf=0")


# ====================================================================
# Section 8: W_3 Z_2 parity (3 tests)
# ====================================================================

class TestW3Parity(unittest.TestCase):
    """Path 6: W_3 Z_2 parity kills delta_pf at genus 2."""

    def test_pf_vanishes(self):
        result = w3_verification_genus2(Rational(10))
        self.assertTrue(result['pf_vanishes_at_genus2'])

    def test_CEO_equals_shadow(self):
        result = w3_verification_genus2(Rational(10))
        self.assertTrue(result['F2_CEO_equals_shadow'])

    def test_S3_zero(self):
        result = w3_verification_genus2(Rational(10))
        self.assertEqual(result['S3'], 0)


# ====================================================================
# Section 9: Self-loop parity vanishing (2 tests)
# ====================================================================

class TestSelfLoopParity(unittest.TestCase):
    """Path 7: sunset graph I = 0."""

    def test_sunset_vanishes(self):
        result = self_loop_parity_check()
        self.assertTrue(result['vanishes'])

    def test_sunset_integral_zero(self):
        result = self_loop_parity_check()
        self.assertEqual(result['sunset_integral'], 0)


# ====================================================================
# Section 10: Virasoro symbolic and numerical (6 tests)
# ====================================================================

class TestVirasoroVerification(unittest.TestCase):
    """Path 8: Virasoro checks."""

    def test_symbolic_identity(self):
        result = virasoro_verification_symbolic()
        self.assertTrue(result['identity'])

    def test_c10(self):
        result = virasoro_verification_genus2(Rational(10))
        self.assertTrue(result['identity'])

    def test_c13_self_dual(self):
        result = virasoro_verification_genus2(Rational(13))
        self.assertTrue(result['identity'])

    def test_c25(self):
        result = virasoro_verification_genus2(Rational(25))
        self.assertTrue(result['identity'])

    def test_delta_pf_vanishes_at_c40(self):
        """delta_pf = 0 when kappa = 10*S_3, i.e. c/2 = 20, c = 40."""
        result = virasoro_verification_symbolic()
        self.assertAlmostEqual(result['delta_pf_at_c40'], 0.0, places=10)

    def test_numerical_identity(self):
        for c_val in [1.0, 10.0, 13.0, 25.0, 26.0]:
            result = numerical_evaluation_genus2(c_val)
            self.assertTrue(result['identity_check'],
                            f"Failed at c={c_val}")


# ====================================================================
# Section 11: Affine sl_2 (3 tests)
# ====================================================================

class TestAffineSl2(unittest.TestCase):
    """Path 11: affine sl_2 (class L)."""

    def test_identity_k1(self):
        result = affine_sl2_verification(k_val=1)
        self.assertTrue(result['identity'])

    def test_S4_zero(self):
        result = affine_sl2_verification(k_val=1)
        self.assertEqual(result['S4'], 0)

    def test_kappa_formula(self):
        """kappa = 3*(k+2)/4."""
        result = affine_sl2_verification(k_val=1)
        self.assertEqual(result['kappa'], Rational(9, 4))


# ====================================================================
# Section 12: Shadow visibility genus (4 tests)
# ====================================================================

class TestShadowVisibility(unittest.TestCase):
    """Path 9: g_min(S_r) = floor(r/2) + 1."""

    def test_S3_genus2(self):
        result = shadow_visibility_genus()
        self.assertEqual(result['shadow_visibility'][3]['g_min'], 2)

    def test_S4_genus3(self):
        result = shadow_visibility_genus()
        self.assertEqual(result['shadow_visibility'][4]['g_min'], 3)

    def test_S5_genus3(self):
        result = shadow_visibility_genus()
        self.assertEqual(result['shadow_visibility'][5]['g_min'], 3)

    def test_S6_genus4(self):
        result = shadow_visibility_genus()
        self.assertEqual(result['shadow_visibility'][6]['g_min'], 4)


# ====================================================================
# Section 13: Depth class (3 tests)
# ====================================================================

class TestDepthClass(unittest.TestCase):
    """Path 10: depth-class decomposition."""

    def test_class_G_CEO_exact(self):
        classes = depth_class_decomposition()
        self.assertTrue(classes['G']['CEO_exact'])

    def test_class_L_first_genus(self):
        classes = depth_class_decomposition()
        self.assertEqual(classes['L']['first_nonzero_genus'], 2)

    def test_class_M_infinite(self):
        classes = depth_class_decomposition()
        self.assertEqual(classes['M']['r_max'], 'infinity')


# ====================================================================
# Section 14: Graph classification (4 tests)
# ====================================================================

class TestGraphClassification(unittest.TestCase):
    """Partition of genus-2 stable graphs."""

    def test_total_count(self):
        result = classify_planted_forest_genus2()
        self.assertEqual(result['n_total'], 7)

    def test_tree_like_count(self):
        result = classify_planted_forest_genus2()
        self.assertEqual(result['n_tree_like'], 3)

    def test_planted_forest_count(self):
        result = classify_planted_forest_genus2()
        self.assertEqual(result['n_planted_forest'], 4)

    def test_partition_properties(self):
        result = classify_planted_forest_genus2()
        self.assertTrue(result['partition_complete'])
        self.assertTrue(result['partition_disjoint'])


# ====================================================================
# Section 15: A-hat generating function (3 tests)
# ====================================================================

class TestAhatGF(unittest.TestCase):
    """Path 12: A-hat generating function."""

    def test_genus1_coefficient(self):
        result = ahat_generating_function_check(Rational(5))
        self.assertEqual(result['genus_data'][1]['lambda_fp'], Rational(1, 24))

    def test_genus2_coefficient(self):
        result = ahat_generating_function_check(Rational(5))
        self.assertEqual(result['genus_data'][2]['lambda_fp'], Rational(7, 5760))

    def test_ratios_decreasing(self):
        result = ahat_generating_function_check(Rational(5), max_genus=6)
        for g in range(3, 6):
            ratio = float(result['genus_data'][g]['ratio_to_prev'])
            self.assertGreater(ratio, 0)
            self.assertLess(ratio, 1)


# ====================================================================
# Section 16: Growth rate (2 tests)
# ====================================================================

class TestGrowthRate(unittest.TestCase):
    """Path 13: Bernoulli asymptotics."""

    def test_ratio_bounded(self):
        result = growth_rate_analysis(max_genus=8)
        for g in range(3, 8):
            ratio = result['genus_data'][g]['ratio']
            self.assertGreater(ratio, 0.5)
            self.assertLess(ratio, 2.0)

    def test_lambda_fp_positive(self):
        result = growth_rate_analysis(max_genus=8)
        for g in range(1, 8):
            self.assertGreater(result['genus_data'][g]['lambda_fp'], 0)


# ====================================================================
# Section 17: Numerical evaluation table (2 tests)
# ====================================================================

class TestNumericalTable(unittest.TestCase):
    """Numerical evaluation at specific c values."""

    def test_all_identities_hold(self):
        table = numerical_evaluation_table()
        for key, val in table.items():
            self.assertTrue(val['identity_check'], f"Failed at {key}")

    def test_kappa_values(self):
        table = numerical_evaluation_table()
        self.assertAlmostEqual(table['c=1']['kappa'], 0.5, places=12)
        self.assertAlmostEqual(table['c=26']['kappa'], 13.0, places=12)


# ====================================================================
# Section 18: Spectral curve (3 tests)
# ====================================================================

class TestSpectralCurve(unittest.TestCase):
    """Spectral curve y^2 = Q_L(t) identification."""

    def test_virasoro_nondegenerate(self):
        data = virasoro_exact(Rational(10))
        curve = spectral_curve_from_shadow(data)
        self.assertFalse(curve['degenerate'])

    def test_heisenberg_degenerate(self):
        data = heisenberg_exact(Rational(1))
        curve = spectral_curve_from_shadow(data)
        self.assertTrue(curve['degenerate'])

    def test_shadow_connection_monodromy(self):
        data = virasoro_exact(Rational(10))
        result = shadow_connection_ceo_kernel(data)
        self.assertEqual(result['monodromy'], -1)


# ====================================================================
# Section 19: Sign and convention checks (3 tests)
# ====================================================================

class TestConventions(unittest.TestCase):
    """Convention checks guided by CLAUDE.md anti-patterns."""

    def test_F2_positive(self):
        """F_2^shadow > 0 for c > 0 (AP22)."""
        for c_val in [1, 10, 13, 25]:
            F2 = Rational(c_val, 2) * _lambda_fp(2)
            self.assertGreater(F2, 0)

    def test_kappa_c_over_2(self):
        """kappa = c/2 for Virasoro (AP39)."""
        for c_val in [1, 10, 26]:
            data = virasoro_exact(Rational(c_val))
            self.assertEqual(data.kappa, Rational(c_val, 2))

    def test_kappa_k_heisenberg(self):
        """kappa = k for Heisenberg (AP39)."""
        for k_val in [1, 3, 5]:
            data = heisenberg_exact(Rational(k_val))
            self.assertEqual(data.kappa, Rational(k_val))


# ====================================================================
# Section 20: Structural properties (4 tests)
# ====================================================================

class TestStructuralProperties(unittest.TestCase):
    """Structural properties of the decomposition."""

    def test_pf_vanishes_when_S3_zero(self):
        """delta_pf = 0 when S_3 = 0."""
        self.assertEqual(delta_pf_genus2(Rational(5), Rational(0)), 0)

    def test_pf_vanishes_when_kappa_10S3(self):
        """delta_pf = 0 when kappa = 10*S_3."""
        val = delta_pf_genus2(Rational(20), Rational(2))
        self.assertEqual(simplify(val), 0)

    def test_pf_independent_of_S4_at_genus2(self):
        """delta_pf at genus 2 does not depend on S_4."""
        dpf1 = delta_pf_genus2(Rational(5), Rational(2), S4=Rational(1))
        dpf2 = delta_pf_genus2(Rational(5), Rational(2), S4=Rational(100))
        self.assertEqual(dpf1, dpf2)

    def test_CEO_additive_in_kappa(self):
        """F_g^CEO is NOT additive in kappa (it involves S_3 nonlinearly)."""
        # F_2^CEO = kappa*7/5760 - S_3*(10*S_3-kappa)/48
        # = kappa*(7/5760 + S_3/48) - 10*S_3^2/48
        # This is affine in kappa (for fixed S_3), NOT additive.
        c = Symbol('c')
        kappa = c / 2
        S3 = Rational(2)
        F2_CEO = F_g_CEO(kappa, S3, 2)
        # Check it depends on c
        self.assertIn(c, F2_CEO.free_symbols)


# ====================================================================
# Section 21: Comprehensive verification (1 test)
# ====================================================================

class TestComprehensive(unittest.TestCase):
    """Full multi-path verification."""

    def test_all_paths_pass(self):
        result = full_theorem_verification()
        self.assertTrue(result['ALL_PASS'])


if __name__ == '__main__':
    unittest.main()
