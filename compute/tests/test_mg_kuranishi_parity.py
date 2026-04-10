r"""Tests for the Kuranishi map parity analysis at genus 2 for multi-weight algebras.

Verifies:
  1. Cyclic cohomology dimensions (H^0, H^1, H^2) for W_3 at genus 0, 1, 2
  2. Kuranishi map parity vanishing at all genera (independent of weight structure)
  3. Cross-channel correction computation at genus 2 for W_3
  4. Z_2 parity analysis of graph channel assignments
  5. Comparison of cross-channel corrections against w3_genus2.py (the existing engine)
  6. Parity obstruction classification for the W_N family
  7. Decisive genus-2 analysis: quantitative evidence against universality
  8. Consistency checks: uniform-weight algebras have no cross-channel corrections

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct computation from graph-sum Feynman rules
  Path 2: Cross-check against w3_genus2.py (independent engine)
  Path 3: Limiting cases (c -> infinity, single-generator specialization)
  Path 4: Z_2 parity selection rules (structural argument)
  Path 5: Dimensional analysis (degree counting in the deformation complex)

Manuscript references:
  thm:algebraic-family-rigidity (higher_genus_modular_koszul.tex)
  op:multi-generator-universality (higher_genus_modular_koszul.tex)
  rem:w3-genus2-cross-channel (higher_genus_modular_koszul.tex)
  rem:multi-gen-independence (higher_genus_modular_koszul.tex)
"""

import unittest
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from mg_kuranishi_parity_engine import (
    # Cyclic cohomology
    w3_cyclic_cohomology_genus0,
    w3_cyclic_cohomology_genus1,
    w3_cyclic_cohomology_genus2,
    heisenberg_cyclic_cohomology_genus2,
    virasoro_cyclic_cohomology_genus2,
    # Kuranishi parity
    kuranishi_parity_genus0,
    kuranishi_parity_genus1,
    kuranishi_parity_genus2,
    # Graph channel analysis
    analyze_genus2_graph_channels,
    # Cross-channel computation
    w3_cross_channel_at_genus2,
    # Parity classification
    classify_parity_obstruction,
    # Complex dimensions
    genus2_deformation_complex_dimensions,
    # Decisive analysis
    decisive_genus2_analysis,
    # W_N analysis
    wn_generator_weights,
    wn_kappa_components,
    wn_parity_analysis_genus2,
    # Summary
    universality_gap_summary,
)


# Standard test central charges
C_VALUES = [
    Fraction(1), Fraction(2), Fraction(4), Fraction(13),
    Fraction(26), Fraction(50), Fraction(100),
]


# ============================================================================
# 1. Cyclic cohomology dimensions
# ============================================================================

class TestCyclicCohomologyDimensions(unittest.TestCase):
    """Verify H^p(Def_cyc) dimensions for W_3 and comparison algebras."""

    def test_w3_genus0_h2_is_one(self):
        """H^2_cyc(W_3) = 1 at genus 0 (thm:algebraic-family-rigidity)."""
        data = w3_cyclic_cohomology_genus0()
        self.assertEqual(data.h2, 1)

    def test_w3_genus0_h1_is_one(self):
        """H^1 = 1 (level deformation direction)."""
        data = w3_cyclic_cohomology_genus0()
        self.assertEqual(data.h1, 1)

    def test_w3_genus0_h0_is_zero(self):
        """H^0 = 0 in the cyclic quotient."""
        data = w3_cyclic_cohomology_genus0()
        self.assertEqual(data.h0, 0)

    def test_w3_genus1_h2_is_one(self):
        """H^2_cyc(W_3) = 1 at genus 1."""
        data = w3_cyclic_cohomology_genus1()
        self.assertEqual(data.h2, 1)

    def test_w3_genus2_h2_is_one(self):
        """H^2_cyc(W_3) = 1 at genus 2 (key claim)."""
        data = w3_cyclic_cohomology_genus2()
        self.assertEqual(data.h2, 1)

    def test_w3_genus2_h1_is_one(self):
        """H^1 = 1 at genus 2."""
        data = w3_cyclic_cohomology_genus2()
        self.assertEqual(data.h1, 1)

    def test_euler_characteristic_zero(self):
        """chi(Def_cyc^{(2,0)}) = h^0 - h^1 + h^2 = 0 for W_3."""
        data = w3_cyclic_cohomology_genus2()
        chi = data.h0 - data.h1 + data.h2
        self.assertEqual(chi, 0)

    def test_heisenberg_genus2_h2_is_one(self):
        """Heisenberg baseline: H^2 = 1 at genus 2."""
        data = heisenberg_cyclic_cohomology_genus2()
        self.assertEqual(data.h2, 1)

    def test_virasoro_genus2_h2_is_one(self):
        """Virasoro baseline: H^2 = 1 at genus 2."""
        data = virasoro_cyclic_cohomology_genus2()
        self.assertEqual(data.h2, 1)

    def test_w3_genus2_parity_broken(self):
        """W_3 at genus 2: Z_2 parity does NOT force all mixed terms to vanish."""
        data = w3_cyclic_cohomology_genus2()
        self.assertFalse(data.parity_grading_intact)

    def test_heisenberg_parity_intact(self):
        """Heisenberg at genus 2: parity is intact (single generator)."""
        data = heisenberg_cyclic_cohomology_genus2()
        self.assertTrue(data.parity_grading_intact)

    def test_virasoro_parity_intact(self):
        """Virasoro at genus 2: parity is intact (single generator)."""
        data = virasoro_cyclic_cohomology_genus2()
        self.assertTrue(data.parity_grading_intact)


# ============================================================================
# 2. Kuranishi map parity vanishing
# ============================================================================

class TestKuranishiParityVanishing(unittest.TestCase):
    """Verify Kuranishi map vanishes at ALL genera by parity of s^{-1}eta."""

    def test_desuspended_degree_is_one(self):
        """s^{-1}eta has degree |eta| - 1 = 2 - 1 = 1 (odd)."""
        for genus in [0, 1, 2]:
            func = [kuranishi_parity_genus0, kuranishi_parity_genus1,
                    kuranishi_parity_genus2][genus]
            result = func("W_3")
            self.assertEqual(result.desuspended_degree, 1,
                             f"Genus {genus}: desuspended degree should be 1")

    def test_parity_forces_vanishing_all_genera(self):
        """l_n(eta,...,eta) = 0 for n >= 2 at ALL genera."""
        for genus in [0, 1, 2]:
            func = [kuranishi_parity_genus0, kuranishi_parity_genus1,
                    kuranishi_parity_genus2][genus]
            for algebra in ["W_3", "Heisenberg", "Virasoro"]:
                result = func(algebra)
                self.assertTrue(result.parity_forces_vanishing,
                                f"Genus {genus}, {algebra}: parity should force vanishing")

    def test_kuranishi_map_vanishes_all_genera(self):
        """The Kuranishi map Obs_g vanishes at all genera for ALL algebras."""
        for genus in [0, 1, 2]:
            func = [kuranishi_parity_genus0, kuranishi_parity_genus1,
                    kuranishi_parity_genus2][genus]
            for algebra in ["W_3", "Heisenberg", "Virasoro"]:
                result = func(algebra)
                self.assertTrue(result.kuranishi_map_vanishes,
                                f"Genus {genus}, {algebra}: Kuranishi should vanish")

    def test_genus0_no_cross_channel(self):
        """At genus 0 (tree level), no cross-channel corrections exist."""
        result = kuranishi_parity_genus0("W_3")
        self.assertTrue(result.cross_channel_correction_vanishes)

    def test_genus1_no_cross_channel(self):
        """At genus 1, cross-channel corrections vanish (single-edge graphs)."""
        result = kuranishi_parity_genus1("W_3")
        self.assertTrue(result.cross_channel_correction_vanishes)

    def test_genus1_universality_proved(self):
        """Genus-1 universality is PROVED unconditionally for all algebras."""
        result = kuranishi_parity_genus1("W_3")
        self.assertTrue(result.tautological_identification_proved)

    def test_genus2_w3_cross_channel_nonzero(self):
        """At genus 2, W_3 has nonzero cross-channel correction."""
        result = kuranishi_parity_genus2("W_3")
        self.assertFalse(result.cross_channel_correction_vanishes)

    def test_genus2_heisenberg_cross_channel_zero(self):
        """At genus 2, Heisenberg has zero cross-channel correction."""
        result = kuranishi_parity_genus2("Heisenberg")
        self.assertTrue(result.cross_channel_correction_vanishes)

    def test_genus2_virasoro_cross_channel_zero(self):
        """At genus 2, Virasoro has zero cross-channel correction."""
        result = kuranishi_parity_genus2("Virasoro")
        self.assertTrue(result.cross_channel_correction_vanishes)

    def test_w3_universality_open_at_genus2(self):
        """W_3 tautological identification is OPEN at genus 2."""
        result = kuranishi_parity_genus2("W_3")
        self.assertFalse(result.tautological_identification_proved)

    def test_uniform_universality_proved_at_genus2(self):
        """Uniform-weight algebras: universality PROVED at genus 2."""
        for algebra in ["Heisenberg", "Virasoro"]:
            result = kuranishi_parity_genus2(algebra)
            self.assertTrue(result.tautological_identification_proved,
                            f"{algebra}: should be proved at genus 2")


# ============================================================================
# 3. Graph channel analysis at genus 2
# ============================================================================

class TestGraphChannelAnalysis(unittest.TestCase):
    """Verify Z_2 parity selection rules on genus-2 stable graphs."""

    def setUp(self):
        self.analyses = analyze_genus2_graph_channels()

    def test_seven_graphs(self):
        """There are 7 stable graphs at (g=2, n=0)."""
        self.assertEqual(len(self.analyses), 7)

    def test_smooth_no_edges(self):
        """Smooth graph has 0 edges and no mixed channels."""
        a = self.analyses[0]
        self.assertEqual(a.graph_name, "smooth")
        self.assertEqual(a.num_edges, 0)
        self.assertEqual(a.num_mixed, 0)

    def test_fig_eight_no_mixed(self):
        """Figure-eight has 1 self-loop: no mixed channels possible."""
        a = self.analyses[1]
        self.assertEqual(a.graph_name, "fig_eight")
        self.assertEqual(a.num_edges, 1)
        self.assertEqual(a.num_mixed, 0)

    def test_banana_mixed_survive(self):
        """Banana has 2 self-loops: 2 mixed assignments, both survive Z_2."""
        a = self.analyses[2]
        self.assertEqual(a.graph_name, "banana")
        self.assertEqual(a.num_edges, 2)
        self.assertEqual(a.num_mixed, 2)
        self.assertEqual(a.z2_vanishing_count, 0)
        self.assertEqual(a.z2_surviving_mixed, 2)

    def test_dumbbell_no_mixed(self):
        """Dumbbell has 1 bridge: no mixed channels."""
        a = self.analyses[3]
        self.assertEqual(a.graph_name, "dumbbell")
        self.assertEqual(a.num_edges, 1)
        self.assertEqual(a.num_mixed, 0)

    def test_theta_z2_kills_three(self):
        """Theta graph: 6 mixed, Z_2 kills 3 (TTW-type), 3 survive (TWW-type)."""
        a = self.analyses[4]
        self.assertEqual(a.graph_name, "theta")
        self.assertEqual(a.num_edges, 3)
        self.assertEqual(a.num_channels, 8)
        self.assertEqual(a.num_mixed, 6)
        self.assertEqual(a.z2_vanishing_count, 3)
        self.assertEqual(a.z2_surviving_mixed, 3)

    def test_lollipop_z2_kills_one(self):
        """Lollipop: 2 mixed, Z_2 kills 1 (T,W with C_{TTW}=0), 1 survives."""
        a = self.analyses[5]
        self.assertEqual(a.graph_name, "lollipop")
        self.assertEqual(a.num_edges, 2)
        self.assertEqual(a.num_mixed, 2)
        self.assertEqual(a.z2_vanishing_count, 1)
        self.assertEqual(a.z2_surviving_mixed, 1)

    def test_barbell_z2_kills_three(self):
        """Barbell: 6 mixed, Z_2 kills 3 (bridge=W), 3 survive (bridge=T)."""
        a = self.analyses[6]
        self.assertEqual(a.graph_name, "barbell")
        self.assertEqual(a.num_edges, 3)
        self.assertEqual(a.num_channels, 8)
        self.assertEqual(a.num_mixed, 6)
        self.assertEqual(a.z2_vanishing_count, 3)
        self.assertEqual(a.z2_surviving_mixed, 3)

    def test_total_surviving_mixed(self):
        """Total surviving mixed assignments: 2 + 3 + 1 + 3 = 9."""
        total = sum(a.z2_surviving_mixed for a in self.analyses)
        self.assertEqual(total, 9)

    def test_total_z2_killed(self):
        """Total Z_2-killed assignments: 3 + 1 + 3 = 7."""
        total = sum(a.z2_vanishing_count for a in self.analyses)
        self.assertEqual(total, 7)


# ============================================================================
# 4. Cross-channel correction computation
# ============================================================================

class TestCrossChannelCorrection(unittest.TestCase):
    """Verify the W_3 genus-2 cross-channel correction delta_F2."""

    def test_closed_form_match(self):
        """delta_F2 = (c+204)/(16c) at all test values."""
        for c_val in C_VALUES:
            result = w3_cross_channel_at_genus2(c_val)
            self.assertTrue(result['match'],
                            f"c={c_val}: closed form mismatch")

    def test_banana_contribution(self):
        """Banana cross-channel: 3/c."""
        for c_val in C_VALUES:
            result = w3_cross_channel_at_genus2(c_val)
            self.assertEqual(result['delta_banana'], Fraction(3) / c_val)

    def test_theta_contribution(self):
        """Theta cross-channel: 9/(2c)."""
        for c_val in C_VALUES:
            result = w3_cross_channel_at_genus2(c_val)
            self.assertEqual(result['delta_theta'], Fraction(9) / (2 * c_val))

    def test_lollipop_contribution(self):
        """Lollipop cross-channel: 1/16 (c-independent)."""
        for c_val in C_VALUES:
            result = w3_cross_channel_at_genus2(c_val)
            self.assertEqual(result['delta_lollipop'], Fraction(1, 16))

    def test_lollipop_c_independent(self):
        """The lollipop contribution 1/16 does not depend on c."""
        values = set()
        for c_val in C_VALUES:
            result = w3_cross_channel_at_genus2(c_val)
            values.add(result['delta_lollipop'])
        self.assertEqual(len(values), 1)
        self.assertEqual(values.pop(), Fraction(1, 16))

    def test_delta_always_positive(self):
        """delta_F2 > 0 for all c > 0."""
        for c_val in C_VALUES:
            result = w3_cross_channel_at_genus2(c_val)
            self.assertGreater(result['delta_total'], 0)

    def test_delta_at_c_4(self):
        """Spot check: delta_F2 at c = 4 is (4+204)/(64) = 208/64 = 13/4."""
        result = w3_cross_channel_at_genus2(Fraction(4))
        expected = (Fraction(4) + 204) / (16 * Fraction(4))
        self.assertEqual(result['delta_total'], expected)
        self.assertEqual(expected, Fraction(208, 64))

    def test_delta_at_c_50(self):
        """Spot check: delta_F2 at c = 50 is (50+204)/(800) = 254/800 = 127/400."""
        result = w3_cross_channel_at_genus2(Fraction(50))
        expected = Fraction(254, 800)
        self.assertEqual(result['delta_total'], expected)


# ============================================================================
# 5. Cross-check against w3_genus2.py
# ============================================================================

class TestCrossCheckWithW3Genus2(unittest.TestCase):
    """Verify consistency with the independent w3_genus2.py engine."""

    def test_cross_channel_matches_w3_genus2(self):
        """Our delta_F2 matches w3_genus2.cross_channel_correction."""
        try:
            from w3_genus2 import cross_channel_correction
        except ImportError:
            self.skipTest("w3_genus2 not importable")

        for c_val in C_VALUES:
            our_result = w3_cross_channel_at_genus2(c_val)
            their_result = cross_channel_correction(c_val)
            self.assertEqual(
                our_result['delta_total'], their_result,
                f"c={c_val}: mismatch with w3_genus2"
            )

    def test_cross_channel_exact_matches(self):
        """Compare per-graph breakdown against w3_genus2."""
        try:
            from w3_genus2 import cross_channel_correction_exact
        except ImportError:
            self.skipTest("w3_genus2 not importable")

        for c_val in C_VALUES:
            ours = w3_cross_channel_at_genus2(c_val)
            theirs = cross_channel_correction_exact(c_val)
            self.assertEqual(ours['delta_banana'], theirs['delta_banana'],
                             f"c={c_val}: banana mismatch")
            self.assertEqual(ours['delta_theta'], theirs['delta_theta'],
                             f"c={c_val}: theta mismatch")
            self.assertEqual(ours['delta_lollipop'], theirs['delta_lollipop'],
                             f"c={c_val}: lollipop mismatch")

    def test_diagonal_matches_kappa_lambda(self):
        """Per-channel diagonal sum = kappa * lambda_2^FP."""
        try:
            from w3_genus2 import (
                kappa_total as w3_kappa_total,
                lambda_fp as w3_lambda_fp,
                diagonal_graph_sum,
            )
        except ImportError:
            self.skipTest("w3_genus2 not importable")

        for c_val in C_VALUES:
            kappa = w3_kappa_total(c_val)
            fp2 = w3_lambda_fp(2)
            expected = kappa * fp2
            diag = diagonal_graph_sum(c_val)
            self.assertEqual(diag['F2_diagonal'], expected,
                             f"c={c_val}: diagonal != kappa * lambda_2^FP")


# ============================================================================
# 6. Parity obstruction classification
# ============================================================================

class TestParityObstructionClassification(unittest.TestCase):
    """Classify parity obstruction for various algebras."""

    def test_heisenberg_never_obstructed(self):
        """Heisenberg: no obstruction at any genus."""
        for g in [0, 1, 2, 3, 5]:
            result = classify_parity_obstruction("Heisenberg", (1,), g)
            self.assertFalse(result.kuranishi_obstructed)
            self.assertFalse(result.amplitude_correction_nonzero)

    def test_virasoro_never_obstructed(self):
        """Virasoro: no obstruction at any genus (single generator)."""
        for g in [0, 1, 2, 3, 5]:
            result = classify_parity_obstruction("Virasoro", (2,), g)
            self.assertFalse(result.kuranishi_obstructed)
            self.assertFalse(result.amplitude_correction_nonzero)

    def test_w3_no_obstruction_genus0(self):
        """W_3 at genus 0: no amplitude correction."""
        result = classify_parity_obstruction("W_3", (2, 3), 0)
        self.assertFalse(result.amplitude_correction_nonzero)

    def test_w3_no_obstruction_genus1(self):
        """W_3 at genus 1: no amplitude correction."""
        result = classify_parity_obstruction("W_3", (2, 3), 1)
        self.assertFalse(result.amplitude_correction_nonzero)

    def test_w3_obstruction_genus2(self):
        """W_3 at genus 2: amplitude correction IS nonzero."""
        result = classify_parity_obstruction("W_3", (2, 3), 2)
        self.assertTrue(result.amplitude_correction_nonzero)

    def test_w3_kuranishi_never_obstructed(self):
        """W_3: Kuranishi map NEVER obstructed (at any genus)."""
        for g in [0, 1, 2, 3, 5]:
            result = classify_parity_obstruction("W_3", (2, 3), g)
            self.assertFalse(result.kuranishi_obstructed)

    def test_min_genus_for_mixed_channels(self):
        """Multi-weight algebras: mixed channels appear at genus 2."""
        result = classify_parity_obstruction("W_3", (2, 3), 2)
        self.assertEqual(result.min_genus_for_mixed_channels, 2)

    def test_uniform_weight_no_mixed_channels(self):
        """Uniform-weight: mixed channels impossible at any genus."""
        result = classify_parity_obstruction("Heisenberg", (1,), 2)
        self.assertEqual(result.min_genus_for_mixed_channels, -1)

    def test_w4_obstruction_genus2(self):
        """W_4 (weights 2,3,4) also has amplitude correction at genus 2."""
        result = classify_parity_obstruction("W_4", (2, 3, 4), 2)
        self.assertTrue(result.amplitude_correction_nonzero)

    def test_w5_obstruction_genus2(self):
        """W_5 (weights 2,3,4,5) also has amplitude correction at genus 2."""
        result = classify_parity_obstruction("W_5", (2, 3, 4, 5), 2)
        self.assertTrue(result.amplitude_correction_nonzero)


# ============================================================================
# 7. Deformation complex dimensions
# ============================================================================

class TestDeformationComplexDimensions(unittest.TestCase):
    """Verify deformation complex dimension computations."""

    def test_w3_h2_cyc(self):
        """H^2_cyc(W_3) = 1 at genus 2."""
        dims = genus2_deformation_complex_dimensions("W_3", (2, 3))
        self.assertEqual(dims['h2_cyc'], 1)

    def test_w3_kuranishi_vanishes(self):
        """Kuranishi map vanishes for W_3."""
        dims = genus2_deformation_complex_dimensions("W_3", (2, 3))
        self.assertTrue(dims['kuranishi_vanishes'])

    def test_w3_graph_sum_space_dim(self):
        """Graph-sum space: 1 + 2 + 4 + 2 + 8 + 4 = 21 total assignments."""
        dims = genus2_deformation_complex_dimensions("W_3", (2, 3))
        # smooth: 2^0=1, fig8: 2^1=2, banana: 2^2=4, dumbbell: 2^1=2,
        # theta: 2^3=8, lollipop: 2^2=4. Total = 21.
        self.assertEqual(dims['graph_sum_space_dim'], 21)

    def test_w3_z2_killed(self):
        """Z_2 kills 4 mixed assignments (3 theta + 1 lollipop)."""
        dims = genus2_deformation_complex_dimensions("W_3", (2, 3))
        self.assertEqual(dims['z2_killed_assignments'], 4)

    def test_w3_surviving_mixed(self):
        """6 surviving mixed-channel assignments at genus 2."""
        dims = genus2_deformation_complex_dimensions("W_3", (2, 3))
        self.assertEqual(dims['z2_surviving_mixed'], 6)

    def test_w3_cross_channel_nonzero(self):
        """W_3 has nonzero cross-channel corrections at genus 2."""
        dims = genus2_deformation_complex_dimensions("W_3", (2, 3))
        self.assertTrue(dims['cross_channel_nonzero'])

    def test_heisenberg_no_mixed(self):
        """Heisenberg has 0 mixed-channel assignments."""
        dims = genus2_deformation_complex_dimensions("Heisenberg", (1,))
        self.assertEqual(dims['z2_surviving_mixed'], 0)
        self.assertFalse(dims['cross_channel_nonzero'])


# ============================================================================
# 8. Decisive genus-2 analysis
# ============================================================================

class TestDecisiveGenus2Analysis(unittest.TestCase):
    """Verify the decisive analysis of multi-generator universality."""

    def test_universality_fails_generic_c(self):
        """Universality fails at generic c (delta_F2 != 0)."""
        for c_val in C_VALUES:
            result = decisive_genus2_analysis(c_val)
            self.assertFalse(result['universality_holds'],
                             f"c={c_val}: universality should fail")

    def test_delta_matches_cross_channel(self):
        """delta_F2 from decisive analysis matches cross-channel engine."""
        for c_val in C_VALUES:
            decisive = decisive_genus2_analysis(c_val)
            cross = w3_cross_channel_at_genus2(c_val)
            self.assertEqual(decisive['delta_F2'], cross['delta_total'],
                             f"c={c_val}: delta mismatch")

    def test_kappa_value(self):
        """kappa(W_3) = 5c/6."""
        for c_val in C_VALUES:
            result = decisive_genus2_analysis(c_val)
            self.assertEqual(result['kappa'], Fraction(5) * c_val / 6)

    def test_F2_diagonal(self):
        """F_2^{diagonal} = kappa * lambda_2^FP = 7c/6912."""
        # kappa = 5c/6, lambda_2^FP = 7/5760.
        # F2_diag = 5c/6 * 7/5760 = 35c/34560 = 7c/6912.
        for c_val in C_VALUES:
            result = decisive_genus2_analysis(c_val)
            expected = Fraction(7) * c_val / 6912
            self.assertEqual(result['F2_diagonal'], expected,
                             f"c={c_val}: F2_diagonal wrong")

    def test_delta_positive_for_positive_c(self):
        """delta_F2 > 0 for all c > 0."""
        for c_val in C_VALUES:
            result = decisive_genus2_analysis(c_val)
            self.assertGreater(result['delta_F2'], 0)

    def test_universality_only_at_c_minus_204(self):
        """Universality (delta=0) only at c = -204 (unphysical)."""
        for c_val in C_VALUES:
            result = decisive_genus2_analysis(c_val)
            self.assertEqual(result['universality_c_value'], Fraction(-204))

    def test_ratio_large_at_small_c(self):
        """delta/diagonal ratio is large at small c."""
        result = decisive_genus2_analysis(Fraction(1))
        self.assertGreater(result['ratio_delta_over_diag'], 10)

    def test_ratio_decreases_with_c(self):
        """delta/diagonal ratio decreases monotonically with c."""
        ratios = []
        for c_val in sorted(C_VALUES):
            result = decisive_genus2_analysis(c_val)
            ratios.append(result['ratio_delta_over_diag'])
        for i in range(len(ratios) - 1):
            self.assertGreater(ratios[i], ratios[i + 1],
                               f"Ratio should decrease with c")


# ============================================================================
# 9. W_N family analysis
# ============================================================================

class TestWNFamilyAnalysis(unittest.TestCase):
    """Verify W_N family parity analysis."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: single generator of weight 2."""
        weights = wn_generator_weights(2)
        self.assertEqual(weights, (2,))

    def test_w3_weights(self):
        """W_3: generators of weights (2, 3)."""
        self.assertEqual(wn_generator_weights(3), (2, 3))

    def test_w4_weights(self):
        """W_4: generators of weights (2, 3, 4)."""
        self.assertEqual(wn_generator_weights(4), (2, 3, 4))

    def test_w3_kappa_components(self):
        """kappa_j(W_3) = c/j for j = 2, 3."""
        c_val = Fraction(12)
        comps = wn_kappa_components(3, c_val)
        self.assertEqual(comps[2], Fraction(6))   # c/2
        self.assertEqual(comps[3], Fraction(4))   # c/3

    def test_w3_kappa_sum(self):
        """sum kappa_j = 5c/6 for W_3."""
        c_val = Fraction(30)
        comps = wn_kappa_components(3, c_val)
        total = sum(comps.values())
        self.assertEqual(total, Fraction(25))  # 5*30/6 = 25

    def test_w2_universality_proved(self):
        """W_2 = Virasoro: universality PROVED."""
        result = wn_parity_analysis_genus2(2)
        self.assertTrue(result['universality_proved'])
        self.assertFalse(result['cross_channel_exists'])

    def test_w3_universality_open(self):
        """W_3: universality OPEN at genus 2."""
        result = wn_parity_analysis_genus2(3)
        self.assertTrue(result['universality_open'])
        self.assertTrue(result['cross_channel_exists'])

    def test_wn_kuranishi_always_vanishes(self):
        """Kuranishi map vanishes for ALL W_N."""
        for N in range(2, 8):
            result = wn_parity_analysis_genus2(N)
            self.assertTrue(result['kuranishi_vanishes'])

    def test_wn_channel_count_grows(self):
        """Total channel assignments grows with N."""
        counts = []
        for N in range(2, 7):
            result = wn_parity_analysis_genus2(N)
            counts.append(result['total_genus2_assignments'])
        for i in range(len(counts) - 1):
            self.assertLess(counts[i], counts[i + 1])


# ============================================================================
# 10. Summary and gap analysis
# ============================================================================

class TestUniversalityGapSummary(unittest.TestCase):
    """Verify the universality gap summary."""

    def test_kuranishi_vanishes(self):
        summary = universality_gap_summary()
        self.assertTrue(summary['kuranishi_map_vanishes'])

    def test_parity_genus_independent(self):
        summary = universality_gap_summary()
        self.assertTrue(summary['parity_argument_genus_independent'])

    def test_genus1_proved(self):
        summary = universality_gap_summary()
        self.assertIn('PROVED', summary['genus_1_universality'])

    def test_genus2_uniform_proved(self):
        summary = universality_gap_summary()
        self.assertIn('PROVED', summary['genus_2_uniform_weight'])

    def test_genus2_multi_open(self):
        summary = universality_gap_summary()
        self.assertIn('OPEN', summary['genus_2_multi_weight'])

    def test_w3_delta_formula(self):
        summary = universality_gap_summary()
        self.assertEqual(summary['w3_genus2_delta'], '(c + 204) / (16c)')

    def test_gap_not_kuranishi(self):
        summary = universality_gap_summary()
        self.assertIn('NOT the Kuranishi map', summary['gap_location'])


# ============================================================================
# 11. Limiting cases (multi-path verification)
# ============================================================================

class TestLimitingCases(unittest.TestCase):
    """Verify limiting cases for multi-path verification."""

    def test_large_c_delta_approaches_one_over_16(self):
        """As c -> infinity, delta_F2 -> 1/16."""
        # At c = 10000, delta = (10000 + 204)/(16*10000) = 10204/160000 ~ 1/16
        c_large = Fraction(10000)
        result = w3_cross_channel_at_genus2(c_large)
        delta = result['delta_total']
        # delta - 1/16 = 51/(4c) -> 0
        remainder = delta - Fraction(1, 16)
        self.assertEqual(remainder, Fraction(51) / (4 * c_large))
        self.assertLess(float(remainder), 0.002)

    def test_delta_decomposition(self):
        """delta_F2 = 51/(4c) + 1/16 for all c."""
        for c_val in C_VALUES:
            result = w3_cross_channel_at_genus2(c_val)
            expected = Fraction(51) / (4 * c_val) + Fraction(1, 16)
            self.assertEqual(result['delta_total'], expected)

    def test_cross_channel_only_from_multi_edge_graphs(self):
        """Cross-channel corrections come only from graphs with >= 2 edges."""
        # Graphs with 0 or 1 edges (smooth, fig_eight, dumbbell) have no mixed
        analyses = analyze_genus2_graph_channels()
        for a in analyses:
            if a.num_edges <= 1:
                self.assertEqual(a.z2_surviving_mixed, 0,
                                 f"{a.graph_name}: should have no mixed channels")

    def test_genus2_smooth_vertex_excluded(self):
        """The smooth genus-2 vertex does not contribute to cross-channel."""
        analyses = analyze_genus2_graph_channels()
        smooth = analyses[0]
        self.assertEqual(smooth.num_edges, 0)
        self.assertEqual(smooth.num_mixed, 0)


# ============================================================================
# 12. Consistency with the parity argument
# ============================================================================

class TestParityArgumentConsistency(unittest.TestCase):
    """Verify internal consistency of the parity argument."""

    def test_degree_of_eta_is_2(self):
        """eta has degree 2 in the cyclic deformation complex."""
        # eta in H^2_cyc has cohomological degree 2.
        # s^{-1}eta has degree 2 - 1 = 1 (odd).
        for func in [kuranishi_parity_genus0, kuranishi_parity_genus1,
                     kuranishi_parity_genus2]:
            result = func("W_3")
            # desuspended degree = |eta| - 1 = 2 - 1 = 1
            self.assertEqual(result.desuspended_degree, 1)
            # 1 is odd, so graded antisymmetry forces vanishing
            self.assertTrue(result.desuspended_degree % 2 == 1)

    def test_parity_independent_of_generator_count(self):
        """Parity vanishing depends on dim H^2 = 1, not on number of generators."""
        # For any algebra with dim H^2_cyc = 1, the parity argument works.
        # This is because eta generates the ENTIRE H^2, so all MC elements
        # on the cyclic line are scalar multiples of eta tensor Gamma.
        for algebra in ["W_3", "Heisenberg", "Virasoro"]:
            result = kuranishi_parity_genus2(algebra)
            self.assertEqual(result.dim_h2_cyc, 1)
            self.assertTrue(result.kuranishi_map_vanishes)

    def test_cross_channel_is_not_kuranishi_obstruction(self):
        """Cross-channel correction is NOT a Kuranishi obstruction.

        The Kuranishi map Obs_g: H^1 -> H^2 measures whether the
        MC equation can be solved.  The cross-channel correction
        measures whether the SOLUTION has a specific form.

        These are logically independent: the MC equation CAN be solved
        (Kuranishi vanishes), but the solution may not equal kappa*lambda_g.
        """
        result = kuranishi_parity_genus2("W_3")
        # Kuranishi vanishes (MC solvable)
        self.assertTrue(result.kuranishi_map_vanishes)
        # But cross-channel is nonzero (solution differs from universal form)
        self.assertFalse(result.cross_channel_correction_vanishes)
        # These are BOTH true simultaneously — not contradictory


if __name__ == '__main__':
    unittest.main()
