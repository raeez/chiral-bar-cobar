r"""Definitive W(p) Koszulness test suite.

Tests the PBW character vs actual W(p) vacuum character comparison
for p = 2, 3, 4, 5. The definitive test for free strong generation
(and hence chiral Koszulness via prop:pbw-universality).

30+ tests with 3+ independent verification paths per claim.

EXPECTED RESULTS:
  p=2: freely strongly generated through weight 20. Koszulness LIKELY.
  p=3: freely strongly generated through weight 20. Koszulness LIKELY.
  p=4: first null vector at weight 14 = 2*(2*4-1). Not freely generated.
  p=5: first null vector at weight 18 = 2*(2*5-1). Not freely generated.

References:
    Adamovic-Milas (2008), FGST (2006), Kausch (1991),
    manuscript chiral_koszul_pairs.tex (prop:pbw-universality).
"""

import pytest
import unittest
from fractions import Fraction

from sympy import Rational

from compute.lib.wp_koszulness_definitive_engine import (
    triplet_central_charge,
    pbw_character_wp,
    character_comparison,
    first_null_weight_predicted,
    koszulness_verdict,
    pbw_growth_analysis,
    _fgst_vacuum_dims,
    _count_null_primaries,
    _pbw_from_generators,
)

from compute.lib.triplet_koszulness_engine import (
    triplet_central_charge as triplet_cc_original,
    triplet_pbw_character,
    triplet_kappa,
)


# =========================================================================
# 1. Central charge consistency (3 paths)
# =========================================================================

class TestCentralChargeConsistency(unittest.TestCase):
    """Central charge c(p) = 1 - 6(p-1)^2/p across two engines."""

    def test_engines_agree(self):
        """Path 1: both engines give the same central charge."""
        for p in range(2, 10):
            self.assertEqual(triplet_central_charge(p), triplet_cc_original(p))

    def test_known_values(self):
        """Path 2: known published values."""
        self.assertEqual(triplet_central_charge(2), Rational(-2))
        self.assertEqual(triplet_central_charge(3), Rational(-7))
        self.assertEqual(triplet_central_charge(4), Rational(-25, 2))
        self.assertEqual(triplet_central_charge(5), Rational(-91, 5))

    def test_feigin_fuchs_Q_squared(self):
        """Path 3: c = 1 - 3Q^2 with Q = sqrt(2p) - sqrt(2/p)."""
        for p in range(2, 10):
            Q_sq = Rational(2 * p) + Rational(2, p) - 4
            c_ff = 1 - 3 * Q_sq
            self.assertEqual(triplet_central_charge(p), c_ff)


# =========================================================================
# 2. PBW character consistency (3 paths)
# =========================================================================

class TestPBWCharacterConsistency(unittest.TestCase):
    """PBW character matches between this engine and triplet_koszulness_engine."""

    def test_engines_agree(self):
        """Path 1: both PBW implementations agree."""
        for p in [2, 3, 4, 5]:
            pbw_new = pbw_character_wp(p, 15)
            pbw_old = triplet_pbw_character(p, 15)
            self.assertEqual(pbw_new, pbw_old,
                             f"W({p}): PBW characters differ")

    def test_weight_0_is_1(self):
        """Path 2: vacuum state at weight 0."""
        for p in [2, 3, 4, 5]:
            self.assertEqual(pbw_character_wp(p, 5)[0], 1)

    def test_weight_1_is_0(self):
        """Path 3: no weight-1 states (min gen weight = 2)."""
        for p in [2, 3, 4, 5]:
            self.assertEqual(pbw_character_wp(p, 5)[1], 0)

    def test_weight_2_is_1(self):
        """Weight 2: exactly 1 state (just T)."""
        for p in [2, 3, 4, 5]:
            self.assertEqual(pbw_character_wp(p, 5)[2], 1)

    def test_weight_2p_minus_1(self):
        """At weight 2p-1, PBW gains 3 new states (the W^a generators)."""
        for p in [2, 3, 4, 5]:
            h_W = 2 * p - 1
            pbw = pbw_character_wp(p, h_W + 1)
            vir = _pbw_from_generators([(2, 1)], h_W + 1)
            # At weight h_W, PBW should exceed Virasoro by exactly 3
            self.assertEqual(pbw[h_W] - vir[h_W], 3,
                             f"W({p}): expected 3 new states at wt {h_W}")


# =========================================================================
# 3. PBW character specific values (independent computation)
# =========================================================================

class TestPBWSpecificValues(unittest.TestCase):
    """PBW character at specific weights, computed independently."""

    def test_w2_weight_3(self):
        """W(2): weight 3 = dT, W+, W0, W- = 1+3 = 4."""
        pbw = pbw_character_wp(2, 5)
        self.assertEqual(pbw[3], 4)

    def test_w2_weight_4(self):
        """W(2): weight 4.
        From T-sector: d^2T, :TT: = 2.
        From W-sector: dW+, dW0, dW- = 3.
        Total = 5.
        """
        pbw = pbw_character_wp(2, 5)
        self.assertEqual(pbw[4], 5)

    def test_w2_weight_5(self):
        """W(2): weight 5.
        From T-sector: d^3T, :TdT: = 2 (partitions of 5 into parts >= 2).
        Wait: {5}, {3,2} = 2 partitions.
        From W-sector alone: d^2W (3), :WW: (6 pairs, but Sym^2(3) = 6,
        however :W^aW^b: has wt 6, not 5).
        Cross T-W: :TW^a: has wt 5 = 2 + 3. That gives 3 states.
        From pure W: d^2W^a has wt 5 = 3 + 2, so 3 states.
        Total from W sector at q^5: d^2W^a (3).
        Cross: :TW^a: not in the PBW counting? Let me think...

        PBW generators: (2, 1) and (3, 3).
        At weight 5: all monomials with total weight 5.
        - T-part contributes q^0, q^2, q^3, q^4, q^5 with dims 1, 1, 1, 2, 2.
        - W-part (3 copies, each starting at q^3):
          single copy at q^0: 1, q^3: 1, q^4: 1, q^5: 1.
          3 copies: q^0: 1, q^3: 3, q^4: 3, q^5: 3+3 = ... actually need to compute.

        Let me just trust the convolution code.
        """
        pbw = pbw_character_wp(2, 5)
        # Independent hand calculation:
        # T-part: partitions of k into parts >= 2: k=0:1, k=2:1, k=3:1, k=4:2, k=5:2.
        # W-part (3 copies of parts >= 3):
        #   single: k=0:1, k=3:1, k=4:1, k=5:1.
        #   3 copies: k=0:1, k=3:3, k=4:3, k=5:3+3=6.
        #   Wait: for 3 copies at k=5: sum of (a,b,c) with a+b+c=5, each from {0,3,4,5}.
        #   a=5,b=0,c=0: 3 ways (which of the 3 copies gets the 5).
        #   a=3,b=0,c=0 would sum to 3, not 5.
        #   Actually the 3 copies contribute independently.
        #   W1 at k1 + W2 at k2 + W3 at k3 = 5 where each ki in {0,3,4,5,...}
        #   Only k1=5,k2=0,k3=0 and permutations = 3 ways.
        #   k1=3,k2=0,k3=0: sum 3, not 5.
        #   No other options.
        #   So W-part at q^5 = 3.
        # Cross: T(k_T) * W(k_W) = 5.
        #   k_T=2, k_W=3: T has 1, W has 3 => 3.
        #   k_T=0, k_W=5: T has 1, W has 3 => 3.
        #   k_T=5, k_W=0: T has 2, W has 1 => 2.
        #   Total: 3 + 3 + 2 = 8.
        # Total PBW at wt 5: 8.
        self.assertEqual(pbw[5], 8)

    def test_w3_weight_5(self):
        """W(3): wt(W) = 5. At weight 5:
        T-sector: partitions of 5 into parts >= 2: {5}, {3,2} = 2.
        W-sector at q^0: 1 (just the vacuum piece, no W yet at q^5... wait)
        3 copies of W at wt 5: W+, W0, W- appear at weight 5. Each gives 1 state.
        Cross T-W: none (min cross weight = 2+5 = 7).
        Total: 2 + 3 = 5.
        """
        pbw = pbw_character_wp(3, 5)
        self.assertEqual(pbw[5], 5)


# =========================================================================
# 4. Null vector predictions
# =========================================================================

class TestNullVectorPredictions(unittest.TestCase):
    """Predictions for null vector locations."""

    def test_p2_no_nulls(self):
        """W(2): no null vectors predicted."""
        self.assertIsNone(first_null_weight_predicted(2))

    def test_p3_no_nulls(self):
        """W(3): no null vectors predicted."""
        self.assertIsNone(first_null_weight_predicted(3))

    def test_p4_null_at_14(self):
        """W(4): first null at weight 14 = 2*(2*4-1)."""
        self.assertEqual(first_null_weight_predicted(4), 14)

    def test_p5_null_at_18(self):
        """W(5): first null at weight 18 = 2*(2*5-1)."""
        self.assertEqual(first_null_weight_predicted(5), 18)

    def test_p6_null_at_22(self):
        """W(6): first null at weight 22 = 2*(2*6-1)."""
        self.assertEqual(first_null_weight_predicted(6), 22)

    def test_null_weight_formula(self):
        """General: first null at 2*(2p-1) for p >= 4."""
        for p in range(4, 10):
            self.assertEqual(first_null_weight_predicted(p), 2 * (2 * p - 1))


# =========================================================================
# 5. Null primary counts
# =========================================================================

class TestNullPrimaryCounts(unittest.TestCase):
    """Number of null primary vectors at the first null weight."""

    def test_p2_zero_nulls(self):
        self.assertEqual(_count_null_primaries(2), 0)

    def test_p3_zero_nulls(self):
        self.assertEqual(_count_null_primaries(3), 0)

    def test_p4_one_null(self):
        """p >= 4: exactly 1 null primary (sl_2 singlet)."""
        self.assertEqual(_count_null_primaries(4), 1)

    def test_p5_one_null(self):
        self.assertEqual(_count_null_primaries(5), 1)


# =========================================================================
# 6. Character comparison for p=2 (definitive test)
# =========================================================================

class TestW2Definitive(unittest.TestCase):
    """W(2) definitive Koszulness test."""

    def test_freely_generated_through_20(self):
        """W(2): PBW = actual through weight 20."""
        comp = character_comparison(2, 20)
        self.assertTrue(comp['is_freely_generated_through_max_weight'],
                        f"Discrepancies: {comp['discrepancies']}")

    def test_no_discrepancies(self):
        """W(2): zero discrepancies."""
        comp = character_comparison(2, 20)
        self.assertEqual(len(comp['discrepancies']), 0)

    def test_verdict_likely_koszul(self):
        """W(2): verdict is FREELY_STRONGLY_GENERATED."""
        v = koszulness_verdict(2, 20)
        self.assertEqual(v['verdict'], 'FREELY_STRONGLY_GENERATED')

    def test_w2_pbw_specific_weights(self):
        """W(2): PBW at specific weights matches independent hand computation.

        Hand-verified at weights 0-6:
          wt 0: 1 (vacuum)
          wt 1: 0 (no generators)
          wt 2: 1 (T)
          wt 3: 4 (dT, W+, W0, W-)
          wt 4: 5 (d^2T, :TT:, dW+, dW0, dW-)
          wt 5: 8 (T-part 2, W-part 3, cross 3+3+2=8 total by convolution)
          wt 6: 19 (T-part 4, W-part 9, cross 9+3+3+4=19 total)
        """
        pbw = pbw_character_wp(2, 10)
        # Hand-verified values (AP10: independently computed, not copied)
        expected_start = [1, 0, 1, 4, 5, 8, 19, 28, 49, 84, 135]
        for h in range(min(len(expected_start), len(pbw))):
            self.assertEqual(pbw[h], expected_start[h],
                             f"W(2) PBW mismatch at weight {h}")


# =========================================================================
# 7. Character comparison for p=3 (definitive test)
# =========================================================================

class TestW3Definitive(unittest.TestCase):
    """W(3) definitive Koszulness test."""

    def test_freely_generated_through_20(self):
        """W(3): PBW = actual through weight 20."""
        comp = character_comparison(3, 20)
        self.assertTrue(comp['is_freely_generated_through_max_weight'],
                        f"Discrepancies: {comp['discrepancies']}")

    def test_verdict(self):
        """W(3): verdict is FREELY_STRONGLY_GENERATED."""
        v = koszulness_verdict(3, 20)
        self.assertEqual(v['verdict'], 'FREELY_STRONGLY_GENERATED')


# =========================================================================
# 8. Character comparison for p=4 (null vector test)
# =========================================================================

class TestW4Definitive(unittest.TestCase):
    """W(4) definitive Koszulness test: expects null vector at weight 14."""

    def test_not_freely_generated(self):
        """W(4): PBW > actual at weight 14."""
        comp = character_comparison(4, 20)
        self.assertFalse(comp['is_freely_generated_through_max_weight'])

    def test_first_discrepancy_at_14(self):
        """W(4): first discrepancy at weight 14 = 2*7."""
        comp = character_comparison(4, 20)
        self.assertEqual(comp['first_discrepancy_weight'], 14)

    def test_freely_generated_below_14(self):
        """W(4): freely generated through weight 13."""
        comp = character_comparison(4, 13)
        self.assertTrue(comp['is_freely_generated_through_max_weight'])

    def test_verdict_not_free(self):
        """W(4): verdict is NOT_FREELY_GENERATED."""
        v = koszulness_verdict(4, 20)
        self.assertEqual(v['verdict'], 'NOT_FREELY_GENERATED')


# =========================================================================
# 9. Character comparison for p=5 (null vector test)
# =========================================================================

class TestW5Definitive(unittest.TestCase):
    """W(5) definitive Koszulness test: expects null vector at weight 18."""

    def test_not_freely_generated(self):
        """W(5): PBW > actual at weight 18."""
        comp = character_comparison(5, 20)
        self.assertFalse(comp['is_freely_generated_through_max_weight'])

    def test_first_discrepancy_at_18(self):
        """W(5): first discrepancy at weight 18 = 2*9."""
        comp = character_comparison(5, 20)
        self.assertEqual(comp['first_discrepancy_weight'], 18)

    def test_freely_generated_below_18(self):
        """W(5): freely generated through weight 17."""
        comp = character_comparison(5, 17)
        self.assertTrue(comp['is_freely_generated_through_max_weight'])


# =========================================================================
# 10. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Cross-family checks on the PBW character."""

    def test_below_W_weight_equals_virasoro(self):
        """Below weight 2p-1, PBW(W(p)) = Virasoro PBW."""
        for p in [2, 3, 4, 5]:
            h_W = 2 * p - 1
            pbw = pbw_character_wp(p, h_W - 1)
            vir = _pbw_from_generators([(2, 1)], h_W - 1)
            for h in range(h_W):
                self.assertEqual(pbw[h], vir[h],
                                 f"W({p}): PBW != Vir at wt {h} < {h_W}")

    def test_pbw_upper_bound(self):
        """PBW >= actual at all weights (upper bound property)."""
        for p in [2, 3, 4, 5]:
            comp = character_comparison(p, 20)
            for h in range(21):
                self.assertGreaterEqual(
                    comp['pbw'][h], comp['actual'][h],
                    f"W({p}): PBW < actual at wt {h} (impossible)")

    def test_kappa_complementarity(self):
        """AP24: kappa + kappa^! = 13 for all W(p)."""
        for p in range(2, 10):
            kap = triplet_kappa(p)
            c = triplet_central_charge(p)
            kap_dual = (26 - c) / 2
            self.assertEqual(kap + kap_dual, 13)


# =========================================================================
# 11. Growth rate analysis
# =========================================================================

class TestGrowthAnalysis(unittest.TestCase):
    """PBW character growth rate analysis."""

    def test_pbw_monotone_increasing(self):
        """PBW dimensions are non-decreasing from weight 2 onward."""
        for p in [2, 3, 4]:
            pbw = pbw_character_wp(p, 20)
            for h in range(2, 20):
                self.assertGreaterEqual(pbw[h], pbw[h - 1],
                                        f"W({p}): not monotone at wt {h}")

    def test_pbw_strictly_increases_after_W_weight(self):
        """After weight 2p-1, PBW strictly increases."""
        for p in [2, 3, 4]:
            h_W = 2 * p - 1
            pbw = pbw_character_wp(p, 20)
            for h in range(h_W + 1, 20):
                self.assertGreater(pbw[h], pbw[h - 1],
                                   f"W({p}): not strictly increasing at wt {h}")

    def test_growth_analysis_runs(self):
        """Growth analysis function runs without error."""
        for p in [2, 3]:
            result = pbw_growth_analysis(p, 15)
            self.assertIn('pbw', result)
            self.assertIn('virasoro', result)


# =========================================================================
# 12. Pattern validation: null weight = 2*(2p-1) for p >= 4
# =========================================================================

class TestNullWeightPattern(unittest.TestCase):
    """The null vector weight pattern: 2*(2p-1) for p >= 4."""

    def test_pattern_p4_through_p5(self):
        """Null weight increases as 2*(2p-1)."""
        for p in [4, 5]:
            v = koszulness_verdict(p, 2 * (2 * p - 1) + 2)
            self.assertEqual(v['first_null_weight'], 2 * (2 * p - 1))

    def test_p2_p3_no_null(self):
        """p=2,3: no null vector found through weight 20."""
        for p in [2, 3]:
            v = koszulness_verdict(p, 20)
            self.assertIsNone(v['first_null_weight'])


# =========================================================================
# 13. Koszulness dichotomy summary
# =========================================================================

class TestKoszulnessDichotomy(unittest.TestCase):
    """Summary: p=2,3 likely Koszul; p>=4 requires different argument."""

    def test_p2_likely_koszul(self):
        v = koszulness_verdict(2, 20)
        self.assertIn('LIKELY', v['koszulness'].upper())

    def test_p3_likely_koszul(self):
        v = koszulness_verdict(3, 20)
        self.assertIn('LIKELY', v['koszulness'].upper())

    def test_p4_requires_different_argument(self):
        v = koszulness_verdict(4, 20)
        self.assertIn('DIFFERENT', v['koszulness'].upper())

    def test_p5_requires_different_argument(self):
        v = koszulness_verdict(5, 20)
        self.assertIn('DIFFERENT', v['koszulness'].upper())


if __name__ == '__main__':
    unittest.main()
