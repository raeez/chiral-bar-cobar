"""Tests for bar-relevant range and the admissible sl_2 audit surface.

Verifies:
    1. Bar-relevant range computation for hat{sl}_2
    2. First null vector weight formula h_null = (p-1)*q via Kac-Kazhdan
    3. Numerical Shapovalov verification at integrable and admissible levels
    4. Separation between theorem status and obstruction-model verdict
    5. Consistency with cautious manuscript claims on admissible simple quotients

References:
    - Manuscript: prop:bar-admissible, thm:kw-bar-spectral,
      rem:sl2-admissible, rem:admissible-koszul-status
    - Kac-Wakimoto (1988), Arakawa (2017)
"""

import pytest
import unittest
from fractions import Fraction
from math import gcd

from compute.lib.bar_relevant_admissible import (
    bar_relevant_range_sl2,
    first_null_vector_weight_sl2,
    all_null_vector_grades_sl2,
    koszulness_sl2,
    koszulness_classification_sl2,
    shapovalov_null_dimension,
    verify_first_null_weight,
    NullVectorData,
    KoszulnessData,
)


class TestBarRelevantRange(unittest.TestCase):
    """Test bar-relevant range computation."""

    def test_bar_relevant_min(self):
        """Bar-relevant range starts at h = 2."""
        br = bar_relevant_range_sl2()
        self.assertEqual(br['bar_relevant_min'], 2)

    def test_generators_all_weight_one(self):
        """All hat{sl}_2 generators have conformal weight 1."""
        br = bar_relevant_range_sl2()
        for gen in br['generators']:
            self.assertEqual(gen['weight'], 1)

    def test_three_generators(self):
        """hat{sl}_2 has 3 strong generators."""
        br = bar_relevant_range_sl2()
        self.assertEqual(len(br['generators']), 3)


class TestFirstNullVectorWeight(unittest.TestCase):
    """Test the Kac-Kazhdan null vector weight formula."""

    def test_integrable_k0(self):
        """k=0 (p=2,q=1): h_null = 1."""
        nv = first_null_vector_weight_sl2(2, 1)
        self.assertEqual(nv.h_null, 1)
        self.assertFalse(nv.in_bar_range)

    def test_integrable_k1(self):
        """k=1 (p=3,q=1): h_null = 2."""
        nv = first_null_vector_weight_sl2(3, 1)
        self.assertEqual(nv.h_null, 2)
        self.assertTrue(nv.in_bar_range)

    def test_integrable_k2(self):
        """k=2 (p=4,q=1): h_null = 3."""
        nv = first_null_vector_weight_sl2(4, 1)
        self.assertEqual(nv.h_null, 3)
        self.assertTrue(nv.in_bar_range)

    def test_integrable_k3(self):
        """k=3 (p=5,q=1): h_null = 4."""
        nv = first_null_vector_weight_sl2(5, 1)
        self.assertEqual(nv.h_null, 4)

    def test_integrable_k_general(self):
        """k = n (p=n+2, q=1): h_null = n+1 = k+1."""
        for n in range(10):
            nv = first_null_vector_weight_sl2(n + 2, 1)
            self.assertEqual(nv.h_null, n + 1)
            self.assertEqual(nv.k, Fraction(n))

    def test_admissible_k_minus_half(self):
        """k = -1/2 (p=3, q=2): h_null = 4."""
        nv = first_null_vector_weight_sl2(3, 2)
        self.assertEqual(nv.h_null, 4)
        self.assertEqual(nv.k, Fraction(-1, 2))
        self.assertTrue(nv.in_bar_range)

    def test_admissible_k_minus_four_thirds(self):
        """k = -4/3 (p=2, q=3): h_null = 3."""
        nv = first_null_vector_weight_sl2(2, 3)
        self.assertEqual(nv.h_null, 3)
        self.assertEqual(nv.k, Fraction(-4, 3))

    def test_admissible_k_half(self):
        """k = 1/2 (p=5, q=2): h_null = 8."""
        nv = first_null_vector_weight_sl2(5, 2)
        self.assertEqual(nv.h_null, 8)

    def test_admissible_k_minus_third(self):
        """k = -1/3 (p=5, q=3): h_null = 12."""
        nv = first_null_vector_weight_sl2(5, 3)
        self.assertEqual(nv.h_null, 12)

    def test_admissible_k_minus_two_thirds(self):
        """k = -2/3 (p=4, q=3): h_null = 9."""
        nv = first_null_vector_weight_sl2(4, 3)
        self.assertEqual(nv.h_null, 9)

    def test_formula_h_null_equals_p_minus_1_times_q(self):
        """h_null = (p-1)*q for all admissible (p,q)."""
        for q in range(1, 8):
            for p in range(2, 15):
                if gcd(p, q) == 1:
                    nv = first_null_vector_weight_sl2(p, q)
                    self.assertEqual(nv.h_null, (p - 1) * q,
                                     f"Failed for p={p}, q={q}")

    def test_only_k0_below_bar_range(self):
        """Only k=0 (p=2,q=1) has h_null < 2."""
        for q in range(1, 6):
            for p in range(2, 15):
                if gcd(p, q) == 1:
                    nv = first_null_vector_weight_sl2(p, q)
                    if not nv.in_bar_range:
                        self.assertEqual(p, 2)
                        self.assertEqual(q, 1)

    def test_sl2_weight_of_null(self):
        """The null vector has sl_2 weight 2*(p-1)."""
        for p, q in [(3, 1), (4, 1), (3, 2), (2, 3), (5, 2)]:
            nv = first_null_vector_weight_sl2(p, q)
            self.assertEqual(nv.sl2_weight, 2 * (p - 1))

    def test_invalid_parameters(self):
        """Invalid parameters raise ValueError."""
        with self.assertRaises(ValueError):
            first_null_vector_weight_sl2(1, 1)  # p < 2
        with self.assertRaises(ValueError):
            first_null_vector_weight_sl2(4, 2)  # gcd(4,2) = 2

    def test_kk_root_type(self):
        """The null comes from Type II root."""
        nv = first_null_vector_weight_sl2(3, 2)
        self.assertIn('Type II', nv.kk_root_type)


class TestAllNullGrades(unittest.TestCase):
    """Test enumeration of all null vector grades."""

    def test_first_null_matches(self):
        """First entry matches first_null_vector_weight."""
        for p, q in [(3, 1), (3, 2), (2, 3), (5, 2)]:
            nv = first_null_vector_weight_sl2(p, q)
            nulls = all_null_vector_grades_sl2(p, q, max_grade=100)
            if nulls:
                self.assertEqual(nulls[0][0], nv.h_null,
                                 f"Mismatch for p={p}, q={q}")

    def test_integrable_k1_nulls(self):
        """k=1: nulls at grades 2, 4, 6, ... (from successive KK roots)."""
        nulls = all_null_vector_grades_sl2(3, 1, max_grade=20)
        grades = [n[0] for n in nulls]
        self.assertIn(2, grades)  # First null

    def test_ordering(self):
        """Null grades are returned in increasing order."""
        for p, q in [(3, 2), (5, 3)]:
            nulls = all_null_vector_grades_sl2(p, q, max_grade=200)
            for i in range(len(nulls) - 1):
                self.assertLessEqual(nulls[i][0], nulls[i + 1][0])


class TestAdmissibleAuditStatus(unittest.TestCase):
    """Test admissible-level audit bookkeeping for L_k(sl_2)."""

    def test_k0_is_the_only_promoted_koszul_case(self):
        """Only the trivial level k=0 is promoted to a theorem verdict here."""
        kd = koszulness_sl2(2, 1)
        self.assertTrue(kd.is_koszul)
        self.assertEqual(kd.theorem_status, 'proved-trivial')
        self.assertTrue(kd.obstruction_model_verdict)

    def test_positive_integrable_levels_are_not_over_promoted(self):
        """Positive integrable levels stay supported, not theoremized, here."""
        for n in range(1, 8):
            kd = koszulness_sl2(n + 2, 1)
            self.assertIsNone(kd.is_koszul)
            self.assertEqual(kd.theorem_status, 'integrable-supported-not-promoted')
            self.assertTrue(kd.ordinary_semisimple)

    def test_fractional_admissible_levels_are_live_audit(self):
        """Fractional admissible levels are not promoted to theorem verdicts."""
        for p, q in [(3, 2), (2, 3), (5, 2), (5, 3), (4, 3), (7, 2), (7, 3)]:
            kd = koszulness_sl2(p, q)
            self.assertIsNone(kd.is_koszul)
            self.assertFalse(kd.obstruction_model_verdict)
            self.assertFalse(kd.is_integrable)

    def test_documented_nondegenerate_example_marked_semisimple(self):
        """The k=-1/2 example retains its ordinary-category finiteness input."""
        kd = koszulness_sl2(3, 2)
        self.assertTrue(kd.ordinary_semisimple)
        self.assertEqual(kd.theorem_status, 'nondegenerate-admissible-live-audit')

    def test_central_charge_formula(self):
        """c = 3k/(k+2) = 3(p-2q)/p."""
        for p, q in [(3, 2), (5, 2), (4, 3)]:
            kd = koszulness_sl2(p, q)
            expected_c = 3 * (Fraction(p) - 2 * Fraction(q)) / Fraction(p)
            self.assertEqual(kd.c, expected_c)

    def test_k_minus_half_is_live_audit_with_model_obstruction(self):
        """k=-1/2 remains open theoremically even though the model flags it."""
        kd = koszulness_sl2(3, 2)
        self.assertIsNone(kd.is_koszul)
        self.assertFalse(kd.obstruction_model_verdict)
        self.assertEqual(kd.h_null, 4)
        self.assertEqual(kd.c, Fraction(-1))

    def test_n_admissible_modules(self):
        """Number of admissible modules = (p-1)*q."""
        for p, q in [(3, 2), (2, 3), (5, 2), (3, 1), (4, 1)]:
            kd = koszulness_sl2(p, q)
            self.assertEqual(kd.n_admissible_modules, (p - 1) * q)

    def test_classification_table_sorted(self):
        """Classification table is sorted by level k."""
        data = koszulness_classification_sl2(max_level=3.0, max_q=4)
        for i in range(len(data) - 1):
            self.assertLessEqual(float(data[i].k), float(data[i + 1].k))


class TestShapovalovVerification(unittest.TestCase):
    """Numerical verification via Shapovalov determinant."""

    def test_grade1_k1_no_null(self):
        """k=1: no null at grade 1."""
        n, r, nd = shapovalov_null_dimension(1.0, 1)
        self.assertEqual(nd, 0)
        self.assertEqual(n, 3)

    def test_grade2_k1_has_null(self):
        """k=1: null at grade 2 (the (e_{-1})^2 null vector)."""
        n, r, nd = shapovalov_null_dimension(1.0, 2)
        self.assertGreater(nd, 0)

    def test_grade1_k0_all_null(self):
        """k=0: all states null at grade 1."""
        n, r, nd = shapovalov_null_dimension(0.0, 1)
        self.assertEqual(nd, 3)  # all 3 states are null

    def test_grade3_k2_has_null(self):
        """k=2: null at grade 3."""
        n, r, nd = shapovalov_null_dimension(2.0, 3)
        self.assertGreater(nd, 0)

    def test_grade2_k2_no_null(self):
        """k=2: no null at grade 2."""
        n, r, nd = shapovalov_null_dimension(2.0, 2)
        self.assertEqual(nd, 0)

    def test_grade3_k_minus_half_no_null(self):
        """k=-1/2: no null at grade 3 (null expected at grade 4)."""
        n, r, nd = shapovalov_null_dimension(-0.5, 3)
        self.assertEqual(nd, 0)

    def test_grade4_k_minus_half_has_null(self):
        """k=-1/2: null at grade 4 = (p-1)*q = 2*2."""
        n, r, nd = shapovalov_null_dimension(-0.5, 4)
        self.assertGreater(nd, 0)

    def test_grade2_k_minus_four_thirds_no_null(self):
        """k=-4/3: no null at grade 2."""
        n, r, nd = shapovalov_null_dimension(-4/3, 2)
        self.assertEqual(nd, 0)

    def test_grade3_k_minus_four_thirds_has_null(self):
        """k=-4/3: null at grade 3 = (p-1)*q = 1*3."""
        n, r, nd = shapovalov_null_dimension(-4/3, 3)
        self.assertGreater(nd, 0)

    def test_grade5_generic_k_no_null(self):
        """At generic k (irrational), no null through grade 5."""
        k_generic = np.pi - 2  # irrational
        for g in range(1, 5):
            n, r, nd = shapovalov_null_dimension(k_generic, g)
            self.assertEqual(nd, 0, f"Unexpected null at grade {g}")

    def test_verify_integrable_k1(self):
        """Full verification for k=1."""
        result = verify_first_null_weight(3, 1, max_grade=3)
        self.assertTrue(result['match'])
        self.assertEqual(result['found_h_null'], 2)
        self.assertEqual(result['expected_h_null'], 2)

    def test_verify_integrable_k2(self):
        """Full verification for k=2."""
        result = verify_first_null_weight(4, 1, max_grade=4)
        self.assertTrue(result['match'])
        self.assertEqual(result['found_h_null'], 3)

    def test_verify_admissible_k_minus_half(self):
        """Full verification for k=-1/2."""
        result = verify_first_null_weight(3, 2, max_grade=5)
        self.assertTrue(result['match'])
        self.assertEqual(result['found_h_null'], 4)

    def test_verify_admissible_k_minus_four_thirds(self):
        """Full verification for k=-4/3."""
        result = verify_first_null_weight(2, 3, max_grade=4)
        self.assertTrue(result['match'])
        self.assertEqual(result['found_h_null'], 3)


class TestConsistencyWithManuscript(unittest.TestCase):
    """Verify consistency with manuscript claims."""

    def test_universal_always_koszul(self):
        """V_k(sl_2) is Koszul for all k != -2 (prop:pbw-universality).

        This is NOT about L_k; V_k has no null vectors.
        Our audit function concerns L_k only, so it should not be used to
        theoremize the simple quotient from the universal statement.
        """
        for n in range(1, 5):
            kd = koszulness_sl2(n + 2, 1)
            self.assertIsNone(kd.is_koszul)

    def test_rem_sl2_admissible_tracks_live_audit(self):
        """The admissible remark should no longer force a theorem verdict.

        The compute layer mirrors this by keeping q>=2 levels on the live
        audit surface while still recording the obstruction-model signal.
        """
        for p, q in [(3, 2), (2, 3), (5, 2)]:
            kd = koszulness_sl2(p, q)
            self.assertIsNone(kd.is_koszul)
            self.assertFalse(kd.obstruction_model_verdict)

    def test_kw_formula_via_bar_ss(self):
        """The KW theorem gives finite-page control, not global Koszulness.

        The documented sl_2 examples split into a non-degenerate rational case
        and a degenerate nilcone case, both still fenced from a theorem verdict.
        """
        kd_nondeg = koszulness_sl2(3, 2)
        self.assertEqual(kd_nondeg.theorem_status,
                         'nondegenerate-admissible-live-audit')
        kd_deg = koszulness_sl2(2, 3)
        self.assertEqual(kd_deg.theorem_status,
                         'degenerate-admissible-live-audit')

    def test_central_charge_complementarity(self):
        """c(k) + c(-k-4) = 6 (= 2*dim(sl_2))."""
        for p, q in [(3, 2), (5, 2), (4, 3), (3, 1), (4, 1)]:
            k = Fraction(p, q) - 2
            k_dual = -k - 4
            c = 3 * k / (k + 2)
            c_dual = 3 * k_dual / (k_dual + 2)
            self.assertEqual(c + c_dual, 6)

    def test_feigin_frenkel_dual_level(self):
        """Koszul dual level k' = -k - 4 is NOT admissible for q >= 2."""
        for p, q in [(3, 2), (2, 3), (5, 2)]:
            k = Fraction(p, q) - 2
            k_dual = -k - 4  # = -(p/q - 2) - 4 = -p/q - 2
            # k' + 2 = -p/q < 0 -> not admissible
            self.assertTrue(k_dual + 2 < 0)


# Import numpy only for the Shapovalov tests
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


if __name__ == '__main__':
    unittest.main()
