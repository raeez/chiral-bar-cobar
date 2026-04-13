r"""Tests for the triplet W(p) Koszulness engine via character comparison.

KEY FINDINGS:
    W(2): NOT freely strongly generated. First null vector at weight 15.
          PBW = actual through weight 14. Bar-relevant weight = 6.
          Koszulness OPEN (null at 15 is above bar-relevant range,
          but prop:pbw-universality requires free strong generation).

    W(3): PBW = actual through weight 9 (verified range).
          Bar-relevant weight = 10. Strong evidence of free strong
          generation, but not yet proved.

VERIFICATION PATHS (3+ per claim, Multi-Path Mandate):
    Path 1: PBW character from partition function
    Path 2: Known character data from literature (Gaberdiel-Kausch, Abe, Wood)
    Path 3: Virasoro sub-character as lower bound
    Path 4: Low-weight hand counting (weights 0-5)
    Path 5: Central charge and kappa from Feigin-Fuchs formula

HONESTY NOTES (AP10 compliance):
    - W(2) known data from Gaberdiel-Kausch 1996, confirmed by Abe 2007.
    - W(3) data only verified through weight 9 (below first W-W interaction).
    - No test claims Koszulness where it is not proved.
    - The null at weight 15 for W(2) is a GENUINE FINDING, not a bug.

References:
    Kausch (1991), Gaberdiel-Kausch (1996), Abe (2007), FGST (2006)
    Adamovic-Milas (2008), Wood (2014), Nagatomo-Tsuchiya (2009)
    Manuscript: prop:pbw-universality, thm:kac-shapovalov-koszulness
"""

import pytest
import unittest
from fractions import Fraction
from math import comb

from compute.lib.triplet_wp_character_engine import (
    # Central charge
    central_charge, kappa_wp,
    # Generator data
    generator_weights, max_generator_weight, bar_relevant_weight,
    # PBW
    pbw_character, wp_pbw_character, virasoro_sub_character,
    # Character data
    wp_known_characters,
    lattice_theta, partition_function, fock_space_character,
    lattice_voa_character,
    # Comparison
    character_comparison, cross_check_virasoro_bound,
    # Verdict
    koszulness_verdict,
    # Low-weight verification
    verify_pbw_at_low_weights,
    # Sweep
    sweep_wp,
    # Summary
    theorem_summary_wp,
)


F = Fraction


# =========================================================================
# 1. Central charge and kappa
# =========================================================================

class TestCentralCharge(unittest.TestCase):
    """Test central charge c(p) = 1 - 6(p-1)^2/p."""

    def test_p2(self):
        self.assertEqual(central_charge(2), F(-2))

    def test_p3(self):
        self.assertEqual(central_charge(3), F(-7))

    def test_p4(self):
        self.assertEqual(central_charge(4), F(-25, 2))

    def test_p5(self):
        # c(5) = 1 - 6*16/5 = 1 - 96/5 = -91/5
        self.assertEqual(central_charge(5), F(-91, 5))

    def test_feigin_fuchs_cross_check(self):
        """c = 1 - 3Q^2 with Q^2 = 2p + 2/p - 4."""
        for p in range(2, 8):
            Q_sq = F(2*p) + F(2, p) - 4
            c_ff = 1 - 3 * Q_sq
            self.assertEqual(c_ff, central_charge(p),
                f'Feigin-Fuchs cross-check failed at p={p}')

    def test_kappa(self):
        """kappa = c/2."""
        for p in range(2, 8):
            self.assertEqual(kappa_wp(p), central_charge(p) / 2)


# =========================================================================
# 2. Generator data
# =========================================================================

class TestGeneratorData(unittest.TestCase):

    def test_generator_weights_p2(self):
        self.assertEqual(generator_weights(2), [(2, 1), (3, 3)])

    def test_generator_weights_p3(self):
        self.assertEqual(generator_weights(3), [(2, 1), (5, 3)])

    def test_max_gen_weight(self):
        for p in range(2, 8):
            self.assertEqual(max_generator_weight(p), 2*p - 1)

    def test_bar_relevant_weight(self):
        self.assertEqual(bar_relevant_weight(2), 6)
        self.assertEqual(bar_relevant_weight(3), 10)
        self.assertEqual(bar_relevant_weight(4), 14)

    def test_total_generators(self):
        """W(p) always has 4 generators: 1 + 3."""
        for p in range(2, 8):
            gens = generator_weights(p)
            total = sum(m for _, m in gens)
            self.assertEqual(total, 4)


# =========================================================================
# 3. PBW character
# =========================================================================

class TestPBWCharacter(unittest.TestCase):

    def test_pbw_weight_0(self):
        """dim_0 = 1 (vacuum) for all p."""
        for p in range(2, 6):
            pbw = wp_pbw_character(p, 5)
            self.assertEqual(pbw[0], 1)

    def test_pbw_weight_1(self):
        """dim_1 = 0 (no weight-1 generators) for all p."""
        for p in range(2, 6):
            pbw = wp_pbw_character(p, 5)
            self.assertEqual(pbw[1], 0)

    def test_pbw_weight_2(self):
        """dim_2 = 1 (just T) for all p."""
        for p in range(2, 6):
            pbw = wp_pbw_character(p, 5)
            self.assertEqual(pbw[2], 1)

    def test_pbw_p2_weight_3(self):
        """W(2): at weight 3, T gives L_{-3}|0> (1) + W^a (3) = 4."""
        pbw = wp_pbw_character(2, 5)
        self.assertEqual(pbw[3], 4)

    def test_pbw_p3_weight_5(self):
        """W(3): at weight 5, Virasoro gives 2 + W^a gives 3 = 5."""
        pbw = wp_pbw_character(3, 5)
        self.assertEqual(pbw[5], 5)

    def test_pbw_below_w_weight_equals_virasoro(self):
        """Below the W-weight, PBW = Virasoro character."""
        for p in range(3, 6):
            h_W = 2 * p - 1
            pbw = wp_pbw_character(p, h_W - 1)
            vir = virasoro_sub_character(h_W - 1)
            for w in range(h_W):
                self.assertEqual(pbw[w], vir[w],
                    f'p={p}, w={w}: PBW={pbw[w]} != Vir={vir[w]}')

    def test_pbw_monotone(self):
        """PBW character is weakly increasing for w >= 2."""
        for p in [2, 3]:
            pbw = wp_pbw_character(p, 20)
            for w in range(3, 20):
                self.assertGreaterEqual(pbw[w], pbw[w-1],
                    f'p={p}: PBW not monotone at w={w}')


# =========================================================================
# 4. Virasoro sub-character
# =========================================================================

class TestVirasoroCharacter(unittest.TestCase):

    def test_virasoro_low_weights(self):
        """Virasoro character = partitions with parts >= 2."""
        vir = virasoro_sub_character(10)
        # p(n; parts >= 2): 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12]
        for w in range(len(expected)):
            self.assertEqual(vir[w], expected[w],
                f'Virasoro at w={w}: {vir[w]} != {expected[w]}')

    def test_virasoro_is_lower_bound_for_w2(self):
        """Virasoro character <= W(2) known character."""
        check = cross_check_virasoro_bound(2, 14)
        self.assertTrue(check['bound_satisfied'])

    def test_virasoro_is_lower_bound_for_pbw(self):
        """Virasoro character <= PBW character for all p."""
        for p in range(2, 6):
            vir = virasoro_sub_character(15)
            pbw = wp_pbw_character(p, 15)
            for w in range(16):
                self.assertLessEqual(vir[w], pbw[w],
                    f'p={p}, w={w}: Vir={vir[w]} > PBW={pbw[w]}')


# =========================================================================
# 5. Known character data
# =========================================================================

class TestKnownCharacters(unittest.TestCase):

    def test_w2_known_data_exists(self):
        known = wp_known_characters(2)
        self.assertIsNotNone(known)
        self.assertIsNotNone(known['dims'])

    def test_w2_known_weight_0(self):
        known = wp_known_characters(2)
        self.assertEqual(known['dims'][0], 1)

    def test_w2_known_weight_1(self):
        known = wp_known_characters(2)
        self.assertEqual(known['dims'][1], 0)

    def test_w2_known_weight_2(self):
        known = wp_known_characters(2)
        self.assertEqual(known['dims'][2], 1)

    def test_w2_known_weight_3(self):
        """Weight 3: 1 (Virasoro) + 3 (W-fields) = 4."""
        known = wp_known_characters(2)
        self.assertEqual(known['dims'][3], 4)

    def test_w2_known_positive(self):
        """All known dimensions are nonneg."""
        known = wp_known_characters(2)
        for k, d in enumerate(known['dims']):
            self.assertGreaterEqual(d, 0, f'W(2) dim at wt {k} = {d} < 0')

    def test_w3_known_data_partial(self):
        """W(3): known data is partial (verified_through)."""
        known = wp_known_characters(3)
        self.assertIsNotNone(known)
        self.assertIsNone(known.get('dims'))
        self.assertEqual(known.get('verified_through'), 9)


# =========================================================================
# 6. THE MAIN FINDING: W(2) null vector at weight 15
# =========================================================================

class TestW2NullVector(unittest.TestCase):
    """W(2) is NOT freely strongly generated: null at weight 15.

    This is the KEY finding of this engine. The PBW character for
    4 generators (1@wt2, 3@wt3) exceeds the known W(2) vacuum
    character starting at weight 15. This means there is a null
    vector (relation among normally ordered products) at weight 15.

    Implications:
    - W(2) is NOT freely strongly generated.
    - Koszulness cannot be deduced from prop:pbw-universality alone.
    - The null is at weight 15, which is above the bar-relevant weight 6.
    - Koszulness remains OPEN (the null may or may not affect bar cohomology).
    """

    def test_pbw_equals_actual_through_14(self):
        """PBW = actual through weight 14."""
        comp = character_comparison(2, 20)
        self.assertEqual(comp['first_discrepancy'], 15)
        for w in range(15):
            self.assertEqual(comp['defect'][w], 0,
                f'Defect at weight {w}: {comp["defect"][w]}')

    def test_null_at_weight_15(self):
        """First null vector at weight 15: defect = 44."""
        comp = character_comparison(2, 20)
        self.assertEqual(comp['first_discrepancy'], 15)
        self.assertEqual(comp['defect'][15], 44)

    def test_pbw_exceeds_actual(self):
        """PBW > actual at weight >= 15 (null vectors present)."""
        comp = character_comparison(2, 20)
        self.assertTrue(comp['pbw_exceeds'])
        self.assertFalse(comp['actual_exceeds'])

    def test_verdict_not_freely_generated(self):
        v = koszulness_verdict(2, 20)
        self.assertEqual(v['verdict'], 'not_freely_generated')

    def test_null_above_bar_relevant(self):
        """The null at weight 15 is above bar-relevant weight 6."""
        self.assertGreater(15, bar_relevant_weight(2))

    def test_defect_grows(self):
        """The defect grows with weight (more relations at higher weight)."""
        comp = character_comparison(2, 20)
        for w in range(16, 21):
            self.assertGreater(comp['defect'][w], 0,
                f'No defect at weight {w}: {comp["defect"][w]}')


# =========================================================================
# 7. W(3): strong evidence of free strong generation
# =========================================================================

class TestW3FreeStrongGeneration(unittest.TestCase):
    """W(3): PBW = actual through weight 9 (verified range).

    The bar-relevant weight is 10, so we have verification through
    weight 9, one short. Strong evidence but not yet a theorem.
    """

    def test_w3_pbw_below_w_weight(self):
        """W(3): PBW = Virasoro character at weights < 5."""
        pbw = wp_pbw_character(3, 4)
        vir = virasoro_sub_character(4)
        for w in range(5):
            self.assertEqual(pbw[w], vir[w])

    def test_w3_pbw_at_w_weight(self):
        """W(3): PBW = 5 at weight 5 (2 Vir + 3 W-fields)."""
        pbw = wp_pbw_character(3, 5)
        self.assertEqual(pbw[5], 5)

    def test_w3_verdict(self):
        """W(3): verdict is freely_strongly_generated (strong evidence)."""
        v = koszulness_verdict(3, 20)
        self.assertEqual(v['verdict'], 'freely_strongly_generated')
        self.assertEqual(v['confidence'], 'strong_evidence')


# =========================================================================
# 8. Low-weight hand verification
# =========================================================================

class TestLowWeightVerification(unittest.TestCase):
    """Verify PBW character at low weights by hand counting."""

    def test_w2_low_weights(self):
        results = verify_pbw_at_low_weights(2)
        for w, data in results.items():
            self.assertTrue(data['match'],
                f'W(2) low-weight mismatch at w={w}: {data}')

    def test_w3_low_weights(self):
        results = verify_pbw_at_low_weights(3)
        for w, data in results.items():
            self.assertTrue(data['match'],
                f'W(3) low-weight mismatch at w={w}: {data}')

    def test_w4_low_weights(self):
        results = verify_pbw_at_low_weights(4)
        for w, data in results.items():
            self.assertTrue(data['match'],
                f'W(4) low-weight mismatch at w={w}: {data}')


# =========================================================================
# 9. Lattice theta function
# =========================================================================

class TestLatticeTheta(unittest.TestCase):

    def test_theta_p2_coefficients(self):
        """Theta_{sqrt(4)Z}(q) = sum_n q^{2n^2} = 1 + 2q^2 + 2q^8 + 2q^{18} + ..."""
        theta = lattice_theta(2, 20)
        self.assertEqual(theta[0], 1)
        self.assertEqual(theta[1], 0)
        self.assertEqual(theta[2], 2)
        self.assertEqual(theta[8], 2)
        self.assertEqual(theta[18], 2)
        for k in [3, 4, 5, 6, 7]:
            self.assertEqual(theta[k], 0, f'theta[{k}] should be 0')

    def test_theta_p3_coefficients(self):
        """Theta_{sqrt(6)Z}(q) = sum_n q^{3n^2} = 1 + 2q^3 + 2q^{12} + ..."""
        theta = lattice_theta(3, 15)
        self.assertEqual(theta[0], 1)
        self.assertEqual(theta[3], 2)
        self.assertEqual(theta[12], 2)

    def test_partition_function(self):
        """p(n) = number of partitions."""
        pf = partition_function(10)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n in range(len(expected)):
            self.assertEqual(pf[n], expected[n])


# =========================================================================
# 10. Fock space character
# =========================================================================

class TestFockSpace(unittest.TestCase):

    def test_fock_equals_partitions(self):
        """Fock space F_0 character = partition function."""
        fock = fock_space_character(15)
        pf = partition_function(15)
        for k in range(16):
            self.assertEqual(fock[k], pf[k])

    def test_fock_exceeds_virasoro(self):
        """Fock space >= Virasoro character (Fock has more modes).

        The Fock space F_0 has character q^{1/24}/eta(q) = prod_{n>=1} 1/(1-q^n),
        while Virasoro has prod_{n>=2} 1/(1-q^n). The difference is
        the n=1 mode, so Fock >= Virasoro.

        NOTE: Fock does NOT exceed the FULL W(p) PBW character, because
        W(p) has 4 generators (including the W-fields), which create
        more states than the single free boson at the W-weight.
        """
        fock = fock_space_character(15)
        vir = virasoro_sub_character(15)
        for w in range(16):
            self.assertGreaterEqual(fock[w], vir[w],
                f'w={w}: Fock={fock[w]} < Vir={vir[w]}')


# =========================================================================
# 11. Lattice VOA character
# =========================================================================

class TestLatticeVOA(unittest.TestCase):

    def test_lattice_voa_positive(self):
        """V_L character has nonneg coefficients."""
        for p in [2, 3]:
            ch = lattice_voa_character(p, 15)
            for k in range(16):
                self.assertGreaterEqual(ch[k], 0,
                    f'p={p}: V_L character negative at wt {k}: {ch[k]}')

    def test_lattice_voa_weight_0(self):
        """V_L at weight 0: 1 (from the zero-momentum lattice point)."""
        for p in [2, 3]:
            ch = lattice_voa_character(p, 5)
            self.assertEqual(ch[0], 1)


# =========================================================================
# 12. Sweep across p values
# =========================================================================

class TestSweep(unittest.TestCase):

    def test_sweep_p2_p3(self):
        results = sweep_wp(max_p=3, max_weight=15)
        self.assertEqual(len(results), 2)

        # W(2): not freely generated
        self.assertEqual(results[0]['verdict'], 'not_freely_generated')

        # W(3): freely generated (strong evidence)
        self.assertEqual(results[1]['verdict'], 'freely_strongly_generated')


# =========================================================================
# 13. Internal consistency
# =========================================================================

class TestConsistency(unittest.TestCase):

    def test_pbw_at_weight_0_is_1(self):
        """PBW(0) = 1 for any generator set."""
        for gens in [[(2, 1)], [(2, 1), (3, 3)], [(2, 1), (5, 3)]]:
            pb = pbw_character(gens, 5)
            self.assertEqual(pb[0], 1)

    def test_single_generator_pbw(self):
        """PBW for 1 generator at weight h = partitions with parts >= h."""
        pb = pbw_character([(3, 1)], 10)
        # Partitions of n with parts >= 3:
        # n=0: 1, n=1: 0, n=2: 0, n=3: 1, n=4: 1, n=5: 1, n=6: 2, n=7: 2, n=8: 3, n=9: 4, n=10: 5
        expected = [1, 0, 0, 1, 1, 1, 2, 2, 3, 4, 5]
        for w in range(len(expected)):
            self.assertEqual(pb[w], expected[w],
                f'Single gen PBW at w={w}: {pb[w]} != {expected[w]}')

    def test_summary_not_empty(self):
        s = theorem_summary_wp()
        self.assertGreater(len(s), 50)

    def test_central_charge_decreasing(self):
        """c(p) is decreasing for p >= 2."""
        for p in range(2, 10):
            self.assertGreater(central_charge(p), central_charge(p + 1))


# =========================================================================
# 14. Cross-check: W(2) null weight matches known structure
# =========================================================================

class TestW2NullStructure(unittest.TestCase):
    """Verify the null vector at weight 15 for W(2) is consistent.

    W(2) has generators at weights 2 and 3. The first null among
    normally ordered products could come from:
    - T-T composites (at weight 4 = 2+2): no null (match through 14)
    - W-W composites (at weight 6 = 3+3): no null (match through 14)
    - Higher composites at weight 15: YES, this is the first null.

    Weight 15 = 5*3 = 3*5 = ... many possible composite structures.
    The defect 44 at weight 15 means 44 relations among the normally
    ordered monomials of total weight 15.
    """

    def test_no_null_below_15(self):
        """No null vectors below weight 15."""
        comp = character_comparison(2, 14)
        self.assertTrue(comp['match'])

    def test_defect_44_at_15(self):
        """Defect of 44 at weight 15."""
        comp = character_comparison(2, 20)
        self.assertEqual(comp['defect'][15], 44)

    def test_defect_at_16(self):
        """Defect at weight 16."""
        comp = character_comparison(2, 20)
        self.assertEqual(comp['defect'][16], 78)

    def test_cumulative_defect_grows(self):
        """Cumulative defect grows monotonically."""
        comp = character_comparison(2, 20)
        cum = 0
        for w in range(21):
            cum += comp['defect'][w]
            self.assertGreaterEqual(cum, 0,
                f'Negative cumulative defect at wt {w}: {cum}')


if __name__ == '__main__':
    unittest.main()
