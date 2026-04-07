r"""Tests for the triplet W(p) Koszulness analysis engine.

Verifies:
  1. Central charge and kappa (multi-path, AP48)
  2. Generator data (weights, multiplicities)
  3. PBW character computation
  4. OPE structure
  5. Koszulness status = OPEN (Beilinson rectification)
  6. Shadow classification (independent of Koszulness)
  7. Feigin-Fuchs realization data
  8. PBW vs Virasoro comparison
  9. Cross-family consistency
  10. Proved vs open classification

MANDATE: 3+ independent verification paths per result.

Beilinson rectification: the previous test suite in
test_logarithmic_voa_shadow_engine.py asserted W(p) is Koszul based on
the false claim of free strong generation.  This suite tests the CORRECTED
status (OPEN) and documents exactly what is proved vs open.

References:
    Adamovic-Milas (2008), FGST (2006), Nagatomo-Tsuchiya (2009),
    Creutzig-Ridout (2013), manuscript chiral_koszul_pairs.tex.
"""

import pytest
import unittest
from fractions import Fraction

from sympy import Rational

from compute.lib.triplet_koszulness_engine import (
    triplet_central_charge,
    triplet_kappa,
    generator_data,
    pbw_character,
    triplet_pbw_character,
    virasoro_pbw_character,
    ope_data,
    koszulness_status,
    pbw_vs_virasoro,
    feigin_fuchs_data,
    shadow_classification,
    proved_vs_open,
)


# =========================================================================
# 1. Central charge (3 paths)
# =========================================================================

class TestCentralCharge(unittest.TestCase):
    """Central charge c(p) = 1 - 6(p-1)^2/p, verified by 3 paths."""

    def test_direct_formula(self):
        """Path 1: direct computation from definition."""
        for p in range(2, 15):
            c = triplet_central_charge(p)
            expected = Rational(1) - Rational(6 * (p - 1)**2, p)
            self.assertEqual(c, expected)

    def test_known_values(self):
        """Path 2: known published values."""
        known = {
            2: Rational(-2),
            3: Rational(-7),
            4: Rational(-25, 2),
            5: Rational(-91, 5),
            6: Rational(-24),
        }
        for p, c_exp in known.items():
            self.assertEqual(triplet_central_charge(p), c_exp)

    def test_feigin_fuchs_consistency(self):
        """Path 3: consistency with Feigin-Fuchs Q^2 formula."""
        for p in range(2, 10):
            ff = feigin_fuchs_data(p)
            self.assertEqual(ff['c'], triplet_central_charge(p))

    def test_monotone_decreasing(self):
        for p in range(2, 20):
            self.assertGreater(triplet_central_charge(p),
                               triplet_central_charge(p + 1))

    def test_always_negative(self):
        for p in range(2, 100):
            self.assertLess(triplet_central_charge(p), 0)

    def test_p_equals_1_raises(self):
        with self.assertRaises(ValueError):
            triplet_central_charge(1)


# =========================================================================
# 2. Kappa (3 paths)
# =========================================================================

class TestKappa(unittest.TestCase):
    """kappa(W(p)) = c(p)/2, verified by 3 paths."""

    def test_kappa_equals_c_over_2(self):
        """Path 1: direct formula."""
        for p in range(2, 15):
            self.assertEqual(triplet_kappa(p),
                             triplet_central_charge(p) / 2)

    def test_explicit_values(self):
        """Path 2: explicit known values."""
        self.assertEqual(triplet_kappa(2), Rational(-1))
        self.assertEqual(triplet_kappa(3), Rational(-7, 2))
        self.assertEqual(triplet_kappa(4), Rational(-25, 4))

    def test_always_negative(self):
        """Path 3: kappa < 0 for all p >= 2 (c < 0)."""
        for p in range(2, 50):
            self.assertLess(triplet_kappa(p), 0)

    def test_complementarity_sum_is_13(self):
        """AP24: kappa + kappa^! = 13 for Virasoro-type families."""
        for p in range(2, 20):
            kappa = triplet_kappa(p)
            c = triplet_central_charge(p)
            kappa_dual = (26 - c) / 2
            self.assertEqual(kappa + kappa_dual, 13)


# =========================================================================
# 3. Generator data
# =========================================================================

class TestGenerators(unittest.TestCase):
    """Generator structure for W(p)."""

    def test_four_generators(self):
        """W(p) has exactly 4 strong generators."""
        for p in range(2, 10):
            gen = generator_data(p)
            self.assertEqual(gen['n_generators'], 4)

    def test_T_weight_2(self):
        for p in range(2, 10):
            self.assertEqual(generator_data(p)['T_weight'], 2)

    def test_W_weight_2p_minus_1(self):
        for p in range(2, 10):
            self.assertEqual(generator_data(p)['W_weight'], 2 * p - 1)

    def test_W_multiplicity_3(self):
        """The sl_2 triplet gives multiplicity 3."""
        for p in range(2, 10):
            self.assertEqual(generator_data(p)['W_multiplicity'], 3)

    def test_strongly_generated_proved(self):
        for p in range(2, 10):
            self.assertTrue(generator_data(p)['strongly_generated'])

    def test_freely_strongly_generated_open(self):
        """Free strong generation is OPEN (not proved)."""
        for p in range(2, 10):
            self.assertIsNone(generator_data(p)['freely_strongly_generated'])


# =========================================================================
# 4. PBW character computation
# =========================================================================

class TestPBWCharacter(unittest.TestCase):
    """PBW character computation for various generator sets."""

    def test_single_generator_wt1(self):
        """1 generator at weight 1 gives partition function."""
        partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        pbw = pbw_character([(1, 1)], 10)
        self.assertEqual(pbw, partitions)

    def test_single_generator_wt2(self):
        """1 generator at weight 2: partitions into parts >= 2."""
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12]
        pbw = pbw_character([(2, 1)], 10)
        self.assertEqual(pbw, expected)

    def test_virasoro_character(self):
        """Virasoro character = single gen at wt 2."""
        vir = virasoro_pbw_character(10)
        single = pbw_character([(2, 1)], 10)
        self.assertEqual(vir, single)

    def test_pbw_w2_starts_correctly(self):
        """W(2) PBW: 4 generators (1@wt2, 3@wt3)."""
        pbw = triplet_pbw_character(2, 10)
        # Weight 0: 1 (vacuum)
        self.assertEqual(pbw[0], 1)
        # Weight 1: 0 (min gen wt = 2)
        self.assertEqual(pbw[1], 0)
        # Weight 2: 1 (just T)
        self.assertEqual(pbw[2], 1)
        # Weight 3: dT + W^+, W^0, W^- = 4
        self.assertEqual(pbw[3], 4)

    def test_pbw_w3_starts_correctly(self):
        """W(3) PBW: 4 generators (1@wt2, 3@wt5)."""
        pbw = triplet_pbw_character(3, 10)
        self.assertEqual(pbw[0], 1)
        self.assertEqual(pbw[1], 0)
        self.assertEqual(pbw[2], 1)
        self.assertEqual(pbw[3], 1)  # just dT
        self.assertEqual(pbw[4], 2)  # d^2T, :TT:
        # Weight 5: from T-sector: 2 + 3 new W^a = 5
        self.assertEqual(pbw[5], 5)

    def test_pbw_monotone(self):
        """PBW dimensions are non-decreasing (for p >= 2)."""
        for p in [2, 3, 5]:
            pbw = triplet_pbw_character(p, 20)
            for h in range(2, 20):
                self.assertGreaterEqual(pbw[h], pbw[h - 1],
                                        f"W({p}): not monotone at wt {h}")

    def test_pbw_exceeds_virasoro(self):
        """PBW(W(p)) >= Virasoro character at all weights."""
        for p in [2, 3, 4, 5]:
            pbw = triplet_pbw_character(p, 15)
            vir = virasoro_pbw_character(15)
            for h in range(16):
                self.assertGreaterEqual(pbw[h], vir[h],
                                        f"W({p}): PBW < Vir at wt {h}")

    def test_pbw_increases_with_p(self):
        """PBW character at fixed weight decreases as p increases.

        Higher p means higher W-weight, so fewer states at low weights.
        PBW(W(2)) >= PBW(W(3)) >= PBW(W(4)) at each weight.
        """
        for h in range(10):
            dims = [triplet_pbw_character(p, h)[h] for p in [2, 3, 4, 5]]
            for i in range(len(dims) - 1):
                self.assertGreaterEqual(dims[i], dims[i + 1],
                                        f"PBW not decreasing in p at wt {h}")


# =========================================================================
# 5. OPE data
# =========================================================================

class TestOPEData(unittest.TestCase):
    """OPE structure tests."""

    def test_ww_pole_order(self):
        for p in [2, 3, 4, 5]:
            od = ope_data(p)
            self.assertEqual(od['WW_max_pole'], 2 * (2 * p - 1))

    def test_not_quadratic(self):
        for p in range(2, 10):
            self.assertFalse(ope_data(p)['is_quadratic'])

    def test_bar_pole_ap19(self):
        """AP19: bar r-matrix pole = OPE pole - 1."""
        for p in range(2, 10):
            od = ope_data(p)
            self.assertEqual(od['bar_r_matrix_max_pole'],
                             od['overall_max_pole'] - 1)


# =========================================================================
# 6. Koszulness status = OPEN (Beilinson rectification)
# =========================================================================

class TestKoszulnessOpen(unittest.TestCase):
    """Koszulness of W(p) is OPEN for all p >= 2.

    This is the Beilinson rectification of the previous false claim.
    """

    def test_status_is_open(self):
        """Koszulness status is OPEN."""
        for p in range(2, 15):
            ks = koszulness_status(p)
            self.assertEqual(ks['status'], 'OPEN')

    def test_pbw_universality_not_applicable(self):
        """prop:pbw-universality requires free strong gen (unproved)."""
        for p in range(2, 10):
            ks = koszulness_status(p)
            self.assertIsNone(ks['pbw_universality_applicable'])

    def test_kac_shapovalov_not_resolved(self):
        for p in range(2, 10):
            ks = koszulness_status(p)
            self.assertIsNone(ks['kac_shapovalov_applicable'])

    def test_has_obstructions_and_evidence(self):
        """Both obstructions and evidence are documented."""
        for p in [2, 3, 5]:
            ks = koszulness_status(p)
            self.assertGreater(len(ks['obstructions_to_koszulness']), 0)
            self.assertGreater(len(ks['evidence_for_koszulness']), 0)

    def test_definitive_test_documented(self):
        for p in [2, 3]:
            ks = koszulness_status(p)
            self.assertIn('PBW character', ks['definitive_test'])


# =========================================================================
# 7. Shadow classification (independent of Koszulness)
# =========================================================================

class TestShadowClassification(unittest.TestCase):
    """Shadow depth: class M for all W(p), independent of Koszulness."""

    def test_all_class_M(self):
        for p in range(2, 15):
            sc = shadow_classification(p)
            self.assertEqual(sc['shadow_class'], 'M')

    def test_infinite_tower(self):
        for p in range(2, 10):
            sc = shadow_classification(p)
            self.assertEqual(sc['r_max'], float('inf'))

    def test_independent_of_koszulness(self):
        """Shadow class is determined by OPE, not by Koszulness."""
        for p in [2, 3, 5]:
            sc = shadow_classification(p)
            self.assertIn('INDEPENDENT', sc['reason'])


# =========================================================================
# 8. PBW vs Virasoro comparison
# =========================================================================

class TestPBWVsVirasoro(unittest.TestCase):
    """PBW character exceeds Virasoro starting at weight 2p-1."""

    def test_first_difference_at_W_weight(self):
        """PBW first exceeds Virasoro at weight of W generators."""
        for p in [2, 3, 4, 5]:
            comp = pbw_vs_virasoro(p, 15)
            h_W = 2 * p - 1
            # The first weight where PBW > Virasoro should be h_W
            # (the W generators add new states at their weight)
            self.assertEqual(comp['first_difference_weight'], h_W,
                             f"W({p}): first diff at wt {comp['first_difference_weight']}, expected {h_W}")


# =========================================================================
# 9. Feigin-Fuchs realization
# =========================================================================

class TestFeiginFuchs(unittest.TestCase):
    """Feigin-Fuchs free-field realization data."""

    def test_c_consistency(self):
        for p in range(2, 10):
            ff = feigin_fuchs_data(p)
            self.assertEqual(ff['c'], triplet_central_charge(p))

    def test_screening_weight_1(self):
        """Both screening operators have conformal weight 1."""
        for p in range(2, 10):
            ff = feigin_fuchs_data(p)
            self.assertEqual(ff['screening_weights'], (1, 1))


# =========================================================================
# 10. Proved vs open classification
# =========================================================================

class TestProvedVsOpen(unittest.TestCase):
    """Classification of proved vs open results."""

    def test_proved_items(self):
        for p in [2, 3, 5]:
            po = proved_vs_open(p)
            proved = po['proved']
            self.assertIsNotNone(proved['central_charge'])
            self.assertIsNotNone(proved['kappa'])
            self.assertTrue(proved['strong_generation'])
            self.assertTrue(proved['c2_cofinite'])
            self.assertFalse(proved['zhu_semisimple'])
            self.assertEqual(proved['n_generators'], 4)

    def test_open_items(self):
        for p in [2, 3, 5]:
            po = proved_vs_open(p)
            open_items = po['open']
            self.assertIsNone(open_items['freely_strongly_generated'])
            self.assertIsNone(open_items['koszul'])
            self.assertIsNone(open_items['pbw_collapse'])

    def test_zhu_dim_2p(self):
        for p in range(2, 10):
            po = proved_vs_open(p)
            self.assertEqual(po['proved']['zhu_dim'], 2 * p)

    def test_modular_dim_3p_minus_1(self):
        for p in range(2, 10):
            po = proved_vs_open(p)
            self.assertEqual(po['proved']['modular_rep_dim'], 3 * p - 1)

    def test_obs1_formula(self):
        """obs_1 = kappa/24."""
        for p in range(2, 10):
            po = proved_vs_open(p)
            self.assertEqual(po['proved']['obs_1'],
                             po['proved']['kappa'] / 24)

    def test_complementarity(self):
        """AP24: kappa + kappa^! = 13."""
        for p in range(2, 10):
            po = proved_vs_open(p)
            self.assertEqual(po['proved']['complementarity_sum'], 13)


# =========================================================================
# 11. Consistency with koszulness_landscape.py
# =========================================================================

class TestConsistencyWithLandscape(unittest.TestCase):
    """Cross-check with the koszulness_landscape.py module."""

    def test_agrees_with_landscape_open_status(self):
        """Our OPEN status agrees with koszulness_landscape.py."""
        try:
            from compute.lib.koszulness_landscape import triplet_w2, KoszulStatus
            w2 = triplet_w2()
            self.assertEqual(w2.koszul_status, KoszulStatus.OPEN)
        except ImportError:
            self.skipTest("koszulness_landscape not available")

    def test_agrees_with_landscape_kappa(self):
        """Kappa value agrees with koszulness_landscape.py."""
        try:
            from compute.lib.koszulness_landscape import triplet_w2
            w2 = triplet_w2()
            self.assertEqual(w2.kappa, triplet_kappa(2))
        except ImportError:
            self.skipTest("koszulness_landscape not available")


# =========================================================================
# 12. Consistency with logarithmic_voa_shadow_engine (CORRECTED)
# =========================================================================

class TestConsistencyWithLogEngine(unittest.TestCase):
    """Cross-check with the corrected logarithmic_voa_shadow_engine."""

    def test_log_engine_koszul_open(self):
        """The corrected log engine reports Koszulness as OPEN."""
        try:
            from compute.lib.logarithmic_voa_shadow_engine import (
                bar_cohomology_prediction,
            )
            for p in [2, 3, 5]:
                pred = bar_cohomology_prediction(p)
                self.assertIsNone(pred['koszul_prediction'],
                                  f"W({p}) should be OPEN in log engine")
        except ImportError:
            self.skipTest("logarithmic_voa_shadow_engine not available")

    def test_kappa_consistent_across_engines(self):
        """Kappa agrees between this engine and the log engine."""
        try:
            from compute.lib.logarithmic_voa_shadow_engine import (
                kappa_path1_virasoro,
            )
            for p in range(2, 10):
                self.assertEqual(triplet_kappa(p), kappa_path1_virasoro(p))
        except ImportError:
            self.skipTest("logarithmic_voa_shadow_engine not available")


if __name__ == '__main__':
    unittest.main()
