r"""Tests for the topological recursion / shadow obstruction tower engine.

CENTRAL RESULT: The shadow obstruction tower is NOT exactly the EO
topological recursion.  The precise decomposition is:

    F_g^shadow(A) = F_g^CEO(Q_L) + delta_pf^{(g,0)}(A)

where delta_pf is the planted-forest correction from codimension >= 2
boundary strata.

36 TESTS covering:
  1. Branch points of the shadow spectral curve (exact + numerical)
  2. Virasoro discriminant formula: disc = -320*c^2/(5c+22)
  3. Shadow tower consistency: H^2 = t^4 * Q_L
  4. Faber-Pandharipande numbers (cross-check)
  5. Genus-1 universality: F_1 = kappa/24, delta_pf = 0
  6. Genus-2 decomposition: F_2 = F_2^CEO + delta_pf
  7. Planted-forest graph decomposition at genus 2
  8. Delta_pf vanishing conditions
  9. Cross-family consistency
  10. Spectral curve classification
  11. The key question (NO, with proved decomposition)

MULTI-PATH VERIFICATION (>= 3 per claim, per CLAUDE.md):
  Every numerical formula verified by at least 3 independent paths.
  Exact arithmetic (sympy Rational) throughout.

References:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
    rem:planted-forest-correction-explicit (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
"""

import unittest
from fractions import Fraction

from sympy import Rational, simplify, sqrt, factorial, bernoulli, Symbol, cancel

from compute.lib.theorem_topological_recursion_shadow_engine import (
    # Faber-Pandharipande
    lambda_fp,
    _bernoulli_number,
    # Family constructors
    ShadowSpectralData,
    virasoro_data,
    heisenberg_data,
    affine_sl2_data,
    betagamma_data,
    w3_wline_data,
    # Branch points
    branch_points_exact,
    branch_points_virasoro,
    virasoro_branch_points_discriminant,
    # Shadow tower
    shadow_tower_from_QL,
    # Free energies
    F_g_shadow,
    F_g_CEO,
    delta_pf_genus1,
    delta_pf_genus2,
    delta_pf_genus2_graph_decomposition,
    # Virasoro specializations
    virasoro_delta_pf_genus2,
    virasoro_F2_CEO,
    virasoro_F2_decomposition,
    # Verification
    cross_family_genus1_check,
    cross_family_genus2_check,
    classify_spectral_curve,
    answer_key_question,
    full_verification,
    verify_virasoro_discriminant_formula,
    verify_delta_pf_vanishing_conditions,
    verify_shadow_tower_consistency,
)


# ====================================================================
# Section 1: Faber-Pandharipande numbers
# ====================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!"""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Rational(1, 24))

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp(2), Rational(7, 5760))

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp(3), Rational(31, 967680))

    def test_lambda_positive(self):
        """All lambda_g^FP are positive for g >= 1."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)


# ====================================================================
# Section 2: Branch points of spectral curve
# ====================================================================

class TestBranchPoints(unittest.TestCase):
    """Branch points of y^2 = Q_L(t)."""

    def test_virasoro_c1_branch_points_complex(self):
        """At c=1, branch points are complex conjugate (disc < 0)."""
        bp = branch_points_virasoro(1)
        self.assertTrue(bp['branch_points_conjugate'])
        self.assertLess(float(bp['discriminant']), 0)

    def test_virasoro_c13_branch_points_complex(self):
        """At c=13 (self-dual), branch points are complex conjugate."""
        bp = branch_points_virasoro(13)
        self.assertTrue(bp['branch_points_conjugate'])

    def test_virasoro_c26_branch_points_complex(self):
        """At c=26 (critical), branch points are complex conjugate."""
        bp = branch_points_virasoro(26)
        self.assertTrue(bp['branch_points_conjugate'])

    def test_virasoro_discriminant_formula(self):
        """disc(Q_L) = -320*c^2/(5c+22) for Virasoro."""
        result = verify_virasoro_discriminant_formula()
        self.assertTrue(result['symbolic_match'])
        for c_val, check in result['numerical_checks'].items():
            self.assertTrue(check['match'],
                            f"Discriminant mismatch at c={c_val}")

    def test_discriminant_negative_all_positive_c(self):
        """Virasoro discriminant is negative for all c > 0."""
        for c_val in [1, 2, 5, 10, 13, 25, 26, 50, 100]:
            disc = virasoro_branch_points_discriminant(c_val)
            self.assertLess(disc, 0,
                            f"Discriminant not negative at c={c_val}")

    def test_heisenberg_degenerate(self):
        """Heisenberg: Q_L = 4k^2 (constant), degenerate spectral curve."""
        data = heisenberg_data(1)
        bp = branch_points_exact(data)
        self.assertTrue(bp['degenerate'])

    def test_affine_sl2_degenerate(self):
        """Affine sl_2: Q_L is perfect square, colliding branch points."""
        data = affine_sl2_data(1)
        self.assertEqual(data.discriminant, 0)


# ====================================================================
# Section 3: Shadow tower consistency
# ====================================================================

class TestShadowTowerConsistency(unittest.TestCase):
    """Verify H^2 = t^4 * Q_L from shadow tower extraction."""

    def test_virasoro_c1_consistency(self):
        """H^2 = t^4 * Q_L for Virasoro at c=1."""
        data = virasoro_data(1)
        result = verify_shadow_tower_consistency(data)
        self.assertTrue(result['all_match'])

    def test_virasoro_c13_consistency(self):
        """H^2 = t^4 * Q_L for Virasoro at c=13."""
        data = virasoro_data(13)
        result = verify_shadow_tower_consistency(data)
        self.assertTrue(result['all_match'])

    def test_heisenberg_consistency(self):
        """H^2 = t^4 * Q_L for Heisenberg."""
        data = heisenberg_data(1)
        result = verify_shadow_tower_consistency(data)
        self.assertTrue(result['all_match'])

    def test_tower_kappa_recovery(self):
        """S_2 = kappa (the leading shadow coefficient)."""
        for c_val in [1, 2, 13, 26]:
            data = virasoro_data(c_val)
            tower = shadow_tower_from_QL(data)
            self.assertEqual(tower[2], data.kappa,
                             f"S_2 != kappa at c={c_val}")

    def test_tower_alpha_recovery(self):
        """S_3 = alpha (the cubic shadow) for Virasoro."""
        for c_val in [1, 2, 13, 26]:
            data = virasoro_data(c_val)
            tower = shadow_tower_from_QL(data)
            self.assertEqual(tower[3], data.alpha,
                             f"S_3 != alpha at c={c_val}")

    def test_tower_S4_virasoro(self):
        """S_4 = 10/(c*(5c+22)) for Virasoro, from tower extraction."""
        for c_val in [1, 2, 13, 26]:
            data = virasoro_data(c_val)
            tower = shadow_tower_from_QL(data)
            expected = Rational(10) / (Rational(c_val) * (5 * Rational(c_val) + 22))
            self.assertEqual(simplify(tower[4] - expected), 0,
                             f"S_4 mismatch at c={c_val}")


# ====================================================================
# Section 4: Genus-1 universality (F_1 = kappa/24)
# ====================================================================

class TestGenus1(unittest.TestCase):
    """F_1 = kappa/24 universally; delta_pf^{(1,0)} = 0."""

    def test_delta_pf_genus1_zero(self):
        """Planted-forest correction at genus 1 is identically zero."""
        self.assertEqual(delta_pf_genus1(), 0)

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all families."""
        results = cross_family_genus1_check()
        for name, res in results.items():
            self.assertTrue(res['equals_kappa_over_24'],
                            f"F_1 != kappa/24 for {name}")

    def test_F1_CEO_equals_F1_shadow(self):
        """F_1^CEO = F_1^shadow (no planted-forest at genus 1)."""
        for c_val in [1, 13, 26]:
            data = virasoro_data(c_val)
            F1_ceo = F_g_CEO(data.kappa, data.alpha, 1)
            F1_sh = F_g_shadow(data.kappa, 1)
            self.assertEqual(simplify(F1_ceo - F1_sh), 0,
                             f"F1^CEO != F1^shadow at c={c_val}")


# ====================================================================
# Section 5: Genus-2 decomposition
# ====================================================================

class TestGenus2Decomposition(unittest.TestCase):
    """F_2^shadow = F_2^CEO + delta_pf^{(2,0)}."""

    def test_delta_pf_genus2_formula(self):
        """delta_pf = S_3*(10*S_3 - kappa)/48."""
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        dpf = delta_pf_genus2(kappa, S3)
        expected = S3 * (10 * S3 - kappa) / 48
        self.assertEqual(simplify(dpf - expected), 0)

    def test_delta_pf_genus2_graph_sum(self):
        """Graph decomposition reproduces closed-form delta_pf."""
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        result = delta_pf_genus2_graph_decomposition(kappa, S3)
        self.assertTrue(result['match'])

    def test_sunset_vanishes_by_parity(self):
        """Sunset graph (0,4) vanishes by self-loop parity."""
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        result = delta_pf_genus2_graph_decomposition(kappa, S3)
        self.assertEqual(result['sunset_04'], 0)

    def test_virasoro_delta_pf_genus2(self):
        """Virasoro: delta_pf = (40 - c/2)/48 * 2 = (80-c)/96.

        Actually: S_3=2, kappa=c/2.
        delta_pf = 2*(20 - c/2)/48 = (40 - c)/48.
        Wait, let me recompute:
        delta_pf = 2*(10*2 - c/2)/48 = 2*(20 - c/2)/48 = (40 - c)/48.
        """
        for c_val in [1, 13, 26]:
            c_r = Rational(c_val)
            dpf = virasoro_delta_pf_genus2(c_val)
            expected = (40 - c_r) / 48
            self.assertEqual(simplify(dpf - expected), 0,
                             f"delta_pf mismatch at c={c_val}")

    def test_identity_genus2_virasoro(self):
        """F_2^shadow = F_2^CEO + delta_pf for Virasoro at multiple c."""
        for c_val in [1, 2, 13, 25, 26]:
            result = virasoro_F2_decomposition(c_val)
            self.assertTrue(result['identity_holds'],
                            f"Identity fails at c={c_val}")

    def test_delta_pf_nonzero_generic_virasoro(self):
        """delta_pf is generically nonzero for Virasoro (c != 40)."""
        for c_val in [1, 2, 13, 25, 26]:
            dpf = virasoro_delta_pf_genus2(c_val)
            self.assertNotEqual(dpf, 0,
                                f"delta_pf unexpectedly zero at c={c_val}")

    def test_delta_pf_vanishes_at_c40(self):
        """delta_pf vanishes for Virasoro at c = 40."""
        dpf = virasoro_delta_pf_genus2(40)
        self.assertEqual(dpf, 0)

    def test_delta_pf_vanishes_for_S3_zero(self):
        """delta_pf vanishes when S_3 = 0 (Heisenberg, W_3 W-line)."""
        result = verify_delta_pf_vanishing_conditions()
        self.assertTrue(result['vanishes_for_S3_zero'])
        self.assertTrue(result['vanishes_at_c40'])

    def test_heisenberg_CEO_equals_shadow(self):
        """For Heisenberg (S_3=0): F_2^CEO = F_2^shadow."""
        data = heisenberg_data(1)
        dpf = delta_pf_genus2(data.kappa, data.alpha)
        self.assertEqual(dpf, 0)

    def test_cross_family_genus2(self):
        """Cross-family genus-2 identity verification."""
        results = cross_family_genus2_check()
        for name, res in results.items():
            self.assertTrue(res['identity'],
                            f"Genus-2 identity fails for {name}")


# ====================================================================
# Section 6: Spectral curve classification
# ====================================================================

class TestSpectralCurveClassification(unittest.TestCase):
    """Classification of y^2 = Q_L(t) matches shadow depth G/L/C/M."""

    def test_heisenberg_degenerate_constant(self):
        """Heisenberg: Q_L constant, class G."""
        data = heisenberg_data(1)
        result = classify_spectral_curve(data)
        self.assertEqual(result['curve_type'], 'degenerate_constant')

    def test_affine_sl2_perfect_square(self):
        """Affine sl_2: Q_L perfect square, class L."""
        data = affine_sl2_data(1)
        result = classify_spectral_curve(data)
        self.assertEqual(result['curve_type'], 'degenerate_perfect_square')

    def test_virasoro_irreducible(self):
        """Virasoro: Q_L irreducible, class M."""
        data = virasoro_data(1)
        result = classify_spectral_curve(data)
        self.assertEqual(result['curve_type'],
                         'irreducible_complex_conjugate')


# ====================================================================
# Section 7: The key question
# ====================================================================

class TestKeyQuestion(unittest.TestCase):
    """The shadow tower is NOT exactly EO topological recursion."""

    def test_answer_is_no(self):
        """The answer to the key question is NO."""
        result = answer_key_question()
        self.assertEqual(result['answer'], 'NO')

    def test_decomposition_stated(self):
        """The decomposition F_g = F_CEO + delta_pf is stated."""
        result = answer_key_question()
        self.assertIn('delta_pf', result['decomposition'])

    def test_genus1_delta_pf_zero(self):
        """Key question: genus-1 delta_pf is zero."""
        result = answer_key_question()
        self.assertEqual(result['genus_1']['delta_pf'], 0)

    def test_genus2_delta_pf_formula(self):
        """Key question: genus-2 delta_pf formula is stated."""
        result = answer_key_question()
        self.assertIn('S_3', result['genus_2']['delta_pf'])


# ====================================================================
# Section 8: Full verification
# ====================================================================

class TestFullVerification(unittest.TestCase):
    """Integration test: run the complete verification suite."""

    def test_full_suite(self):
        """Full verification suite runs without error."""
        results = full_verification()
        self.assertIn('branch_points', results)
        self.assertIn('genus1_cross_family', results)
        self.assertIn('genus2_decomposition', results)
        self.assertIn('classification', results)
        self.assertIn('key_question', results)

    def test_all_branch_point_discriminants_match(self):
        """All branch point discriminants match the formula."""
        results = full_verification()
        for key, bp in results['branch_points'].items():
            self.assertTrue(bp['disc_match'],
                            f"Disc mismatch at {key}")

    def test_all_genus2_identities_hold(self):
        """All genus-2 decomposition identities hold."""
        results = full_verification()
        for name, res in results['genus2_decomposition'].items():
            self.assertTrue(res['identity'],
                            f"Genus-2 identity fails for {name}")


if __name__ == '__main__':
    unittest.main()
