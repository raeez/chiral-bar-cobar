r"""Tests for the betagamma genus-2 cross-channel engine.

Verifies the central result: delta_F_g^cross(betagamma) = 0 for all g >= 1,
as a consequence of the Mumford isomorphism.

Test structure:
    1. Central charge and kappa formulas
    2. Faber-Pandharipande intersection numbers
    3. Genus-g free energy F_g = kappa * lambda_FP
    4. Cross-channel vanishing at genus 2 (main result)
    5. Cross-channel vanishing at all genera 1-4
    6. Mumford isomorphism consistency
    7. Off-diagonal metric / ghost number obstruction
    8. Lambda-symmetry: F_g(lambda) = F_g(1-lambda)
    9. Uniform-weight limit lambda=1/2
   10. Complementarity: c_bg + c_bc = 0
   11. Contrast with W_3 (nonzero cross-channel)
   12. Five-path verification
   13. Bernoulli polynomial analysis
   14. Full evaluation table

Manuscript references:
    thm:multi-weight-genus-expansion, thm:theorem-d,
    ex:betagamma-fermion-koszul-duality
"""

import sys
import os
import unittest
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from betagamma_genus2_cross_channel_engine import (
    F_g_betagamma,
    bernoulli_analysis,
    bernoulli_poly,
    c_bc,
    c_betagamma,
    comparison_table,
    delta_F2_W3,
    delta_F_g_cross_betagamma,
    five_path_verification,
    full_evaluation,
    graph_sum_offdiagonal,
    kappa_betagamma,
    lambda_fp,
    mumford_exponent,
    structural_analysis,
    verify_mumford_at_boundary,
)


class TestCentralCharge(unittest.TestCase):
    """Test c_bg(lambda) = 2(6*lambda^2 - 6*lambda + 1)."""

    def test_c_bg_lambda_half(self):
        # VERIFIED: [DC] 2*(3/2-3+1) = -1, [LT] symplectic boson c=-1
        self.assertEqual(c_betagamma(Fraction(1, 2)), Fraction(-1))

    def test_c_bg_lambda_one(self):
        # VERIFIED: [DC] 2*(6-6+1) = 2, [LT] grand_synthesis c_bg=2
        self.assertEqual(c_betagamma(Fraction(1)), Fraction(2))

    def test_c_bg_lambda_two(self):
        # VERIFIED: [DC] 2*(24-12+1) = 26, [CF] c_bg(2)+c_bc(2) = 26+(-26) = 0
        self.assertEqual(c_betagamma(Fraction(2)), Fraction(26))

    def test_c_bg_lambda_zero(self):
        # VERIFIED: [DC] 2*(0-0+1) = 2, [SY] c_bg(0) = c_bg(1)
        self.assertEqual(c_betagamma(Fraction(0)), Fraction(2))

    def test_c_bg_symmetry(self):
        """c_bg(lambda) = c_bg(1-lambda) for all lambda."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 3),
                     Fraction(2, 5), Fraction(3, 7)]:
            with self.subTest(lam=lam):
                self.assertEqual(c_betagamma(lam), c_betagamma(1 - lam))


class TestKappa(unittest.TestCase):
    """Test kappa(lambda) = c_bg/2 = 6*lambda^2 - 6*lambda + 1."""

    def test_kappa_lambda_one(self):
        # VERIFIED: [DC] c/2 = 2/2 = 1, [LT] grand_synthesis_engine kappa(bg) = 1
        self.assertEqual(kappa_betagamma(Fraction(1)), Fraction(1))

    def test_kappa_lambda_half(self):
        # VERIFIED: [DC] c/2 = -1/2, [SY] self-dual point
        self.assertEqual(kappa_betagamma(Fraction(1, 2)), Fraction(-1, 2))

    def test_kappa_lambda_two(self):
        # VERIFIED: [DC] c/2 = 26/2 = 13, [CF] kappa(bg,2) = 13
        self.assertEqual(kappa_betagamma(Fraction(2)), Fraction(13))

    def test_kappa_equals_c_over_2(self):
        """kappa = c_bg/2 at all lambda values."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 2),
                     Fraction(1), Fraction(2), Fraction(-1)]:
            with self.subTest(lam=lam):
                self.assertEqual(
                    kappa_betagamma(lam),
                    c_betagamma(lam) / 2,
                )

    def test_kappa_symmetry(self):
        """kappa(lambda) = kappa(1-lambda)."""
        for lam in [Fraction(0), Fraction(1, 3), Fraction(2, 5)]:
            with self.subTest(lam=lam):
                self.assertEqual(
                    kappa_betagamma(lam),
                    kappa_betagamma(1 - lam),
                )


class TestFaberPandharipande(unittest.TestCase):
    """Test lambda_g^FP values."""

    def test_lambda_1(self):
        # VERIFIED: [DC] (1/1)*(1/6)/2 = 1/24, [LT] Faber 1999
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda_2(self):
        # VERIFIED: [DC] (7/8)*(1/30)/24 = 7/5760, [LT] Faber 1999
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda_3(self):
        # VERIFIED: [DC] (31/32)*(1/42)/720 = 31/967680, [LT] Faber 1999
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))


class TestFreeEnergy(unittest.TestCase):
    """Test F_g(lambda) = kappa(lambda) * lambda_g^FP."""

    def test_F1_lambda_one(self):
        # VERIFIED: [DC] kappa=1, F_1=1/24, [LT] torus partition function
        self.assertEqual(F_g_betagamma(1, Fraction(1)), Fraction(1, 24))

    def test_F1_lambda_two(self):
        # VERIFIED: [DC] kappa=13, F_1=13/24
        self.assertEqual(F_g_betagamma(1, Fraction(2)), Fraction(13, 24))

    def test_F2_lambda_one(self):
        # VERIFIED: [DC] kappa=1, F_2=7/5760
        self.assertEqual(F_g_betagamma(2, Fraction(1)), Fraction(7, 5760))

    def test_F2_lambda_two(self):
        # VERIFIED: [DC] kappa=13, F_2=91/5760
        self.assertEqual(F_g_betagamma(2, Fraction(2)), Fraction(91, 5760))

    def test_Fg_symmetry(self):
        """F_g(lambda) = F_g(1-lambda) for all g."""
        for g in range(1, 5):
            for lam in [Fraction(1, 3), Fraction(2, 5), Fraction(3, 7)]:
                with self.subTest(g=g, lam=lam):
                    self.assertEqual(
                        F_g_betagamma(g, lam),
                        F_g_betagamma(g, 1 - lam),
                    )


class TestCrossChannelVanishing(unittest.TestCase):
    """Test delta_F_g^cross(betagamma) = 0 at all genera (main result)."""

    def test_delta_F2_vanishes_generic(self):
        """delta_F_2 = 0 at lambda=2 (generic multi-weight point)."""
        # VERIFIED: [DC] Mumford isomorphism, [DC] off-diagonal metric
        self.assertEqual(
            delta_F_g_cross_betagamma(2, Fraction(2)),
            Fraction(0),
        )

    def test_delta_F2_vanishes_all_lambda(self):
        """delta_F_2 = 0 at several lambda values."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 2),
                     Fraction(3, 4), Fraction(1), Fraction(2),
                     Fraction(-1), Fraction(3)]:
            with self.subTest(lam=lam):
                self.assertEqual(
                    delta_F_g_cross_betagamma(2, lam),
                    Fraction(0),
                )

    def test_delta_vanishes_all_genera(self):
        """delta_F_g = 0 for g=1,2,3,4 at several lambda."""
        for g in range(1, 5):
            for lam in [Fraction(1, 3), Fraction(2), Fraction(-1)]:
                with self.subTest(g=g, lam=lam):
                    self.assertEqual(
                        delta_F_g_cross_betagamma(g, lam),
                        Fraction(0),
                    )

    def test_uniform_weight_limit(self):
        """At lambda=1/2, weights are equal (uniform weight); delta=0 is expected."""
        # VERIFIED: [DC] uniform-weight theorem, [SY] lambda=1/2 is self-dual
        self.assertEqual(
            delta_F_g_cross_betagamma(2, Fraction(1, 2)),
            Fraction(0),
        )


class TestMumfordIsomorphism(unittest.TestCase):
    """Test Mumford isomorphism consistency."""

    def test_exponent_equals_kappa(self):
        """Mumford exponent = kappa(lambda)."""
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
            with self.subTest(lam=lam):
                self.assertEqual(
                    mumford_exponent(lam),
                    kappa_betagamma(lam),
                )

    def test_boundary_verification(self):
        """Verify Mumford at boundary lambda values."""
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
            r = verify_mumford_at_boundary(lam)
            with self.subTest(lam=lam):
                self.assertEqual(r['delta_F_2'], Fraction(0))
                self.assertEqual(r['F_1'], r['F_1_check'])


class TestGraphSumOffdiagonal(unittest.TestCase):
    """Test off-diagonal metric graph sum analysis."""

    def test_all_graphs_vanish(self):
        """All per-graph cross-channel amplitudes vanish."""
        result = graph_sum_offdiagonal(2, Fraction(2))
        self.assertEqual(result['delta_F_2'], Fraction(0))
        for name, data in result['per_graph'].items():
            with self.subTest(graph=name):
                self.assertEqual(data['amplitude'], Fraction(0))

    def test_trivalent_obstruction(self):
        """Theta, lollipop, barbell vanish by ghost number."""
        result = graph_sum_offdiagonal(2, Fraction(2))
        for name in ['theta', 'lollipop', 'barbell']:
            with self.subTest(graph=name):
                self.assertIn('ghost number', result['per_graph'][name]['reason'])


class TestComplementarity(unittest.TestCase):
    """Test c_bg + c_bc = 0 (C7 census)."""

    def test_complementarity(self):
        # VERIFIED: [DC] direct, [LT] C7 census entry
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
            with self.subTest(lam=lam):
                self.assertEqual(
                    c_betagamma(lam) + c_bc(lam),
                    Fraction(0),
                )


class TestContrastW3(unittest.TestCase):
    """Contrast: W_3 has NONZERO cross-channel correction."""

    def test_W3_nonzero(self):
        """delta_F_2(W_3) = (c+204)/(16c) is nonzero for finite c."""
        # VERIFIED: [DC] multi_weight_cross_channel_engine,
        # [DC] 5+ agent computation in manuscript
        for c in [Fraction(2), Fraction(10), Fraction(26), Fraction(100)]:
            with self.subTest(c=c):
                dF = delta_F2_W3(c)
                self.assertNotEqual(dF, Fraction(0))
                self.assertGreater(dF, 0)

    def test_W3_at_c10(self):
        """W_3 at c=10: delta = (10+204)/(16*10) = 214/160 = 107/80."""
        # VERIFIED: [DC] direct, [CF] test_multi_weight_cross_channel_engine
        self.assertEqual(delta_F2_W3(Fraction(10)), Fraction(107, 80))

    def test_bg_vs_W3_contrast(self):
        """betagamma delta=0 vs W_3 delta>0 at same central charge."""
        c = Fraction(26)  # c_bg at lambda=2
        self.assertEqual(delta_F_g_cross_betagamma(2, Fraction(2)), Fraction(0))
        self.assertGreater(delta_F2_W3(c), 0)


class TestFivePathVerification(unittest.TestCase):
    """Test the 5-path verification at several lambda values."""

    def test_five_paths_lambda_2(self):
        result = five_path_verification(Fraction(2), g=2)
        self.assertTrue(result['all_pass'])
        self.assertTrue(result['path_1_mumford']['pass'])
        self.assertTrue(result['path_2_offdiag']['pass'])
        self.assertTrue(result['path_3_ghost_number']['pass'])
        self.assertTrue(result['path_4_symmetry']['pass'])
        self.assertTrue(result['path_5_uniform_weight']['pass'])

    def test_five_paths_lambda_third(self):
        result = five_path_verification(Fraction(1, 3), g=2)
        self.assertTrue(result['all_pass'])

    def test_five_paths_genus_3(self):
        result = five_path_verification(Fraction(2), g=3)
        self.assertTrue(result['all_pass'])


class TestBernoulliAnalysis(unittest.TestCase):
    """Test Bernoulli polynomial analysis."""

    def test_B2_equals_kappa_over_6(self):
        """B_2(lambda) = kappa(lambda)/6 at all lambda."""
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
            with self.subTest(lam=lam):
                result = bernoulli_analysis(lam)
                self.assertTrue(result['B_2_equals_kappa_over_6'])

    def test_B4_not_proportional_to_B2(self):
        """B_4(lambda)/B_2(lambda) is NOT constant (motivates Mumford argument)."""
        # Use lambda=0 and lambda=2 where B_2 != 0 and ratios differ.
        # B_4(0)/B_2(0) = (-1/30)/(1/6) = -1/5
        # B_4(2)/B_2(2) = (119/30)/(13/6) = 119/65
        # VERIFIED: [DC] direct Bernoulli polynomial evaluation
        b2_0 = bernoulli_poly(2, Fraction(0))
        b4_0 = bernoulli_poly(4, Fraction(0))
        b2_2 = bernoulli_poly(2, Fraction(2))
        b4_2 = bernoulli_poly(4, Fraction(2))
        ratio_0 = b4_0 / b2_0
        ratio_2 = b4_2 / b2_2
        self.assertEqual(ratio_0, Fraction(-1, 5))
        self.assertEqual(ratio_2, Fraction(119, 65))
        self.assertNotEqual(ratio_0, ratio_2)

    def test_bernoulli_poly_known_values(self):
        """B_2(0) = 1/6, B_4(0) = -1/30."""
        # VERIFIED: [DC] Bernoulli number definition, [LT] OEIS A027642
        self.assertEqual(bernoulli_poly(2, Fraction(0)), Fraction(1, 6))
        self.assertEqual(bernoulli_poly(4, Fraction(0)), Fraction(-1, 30))


class TestStructuralAnalysis(unittest.TestCase):
    """Test structural analysis documentation."""

    def test_three_reasons(self):
        result = structural_analysis()
        self.assertIn('Mumford', result['reason_1'])
        self.assertIn('Off-diagonal', result['reason_2'])
        self.assertIn('Free field', result['reason_3'])

    def test_W3_contrast(self):
        result = structural_analysis()
        self.assertIn('nonlinear OPE', result['contrast_W3'])


class TestComparisonTable(unittest.TestCase):
    """Test comparison table generation."""

    def test_table_structure(self):
        rows = comparison_table()
        self.assertEqual(len(rows), 6)
        for row in rows:
            self.assertEqual(row['delta_F_2_bg'], Fraction(0))

    def test_W3_positive_at_all_c(self):
        """W_3 cross-channel positive for all positive c."""
        rows = comparison_table()
        for row in rows:
            if row['c_bg'] > 0:
                self.assertGreater(row['delta_F_2_W3_at_c_bg'], 0)


class TestFullEvaluation(unittest.TestCase):
    """Test full evaluation at generic lambda."""

    def test_cross_channel_vanishes_flag(self):
        result = full_evaluation(Fraction(2))
        self.assertTrue(result['cross_channel_vanishes'])

    def test_all_genera_zero_delta(self):
        result = full_evaluation(Fraction(2), max_genus=4)
        for g in range(1, 5):
            with self.subTest(g=g):
                self.assertEqual(result['genera'][g]['delta_F_g'], Fraction(0))


if __name__ == '__main__':
    unittest.main()
