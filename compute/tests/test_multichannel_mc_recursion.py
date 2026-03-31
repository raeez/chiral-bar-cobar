r"""Rectification tests for compute/lib/multichannel_mc_recursion.py.

These tests lock in the corrected status of the module:

- the `(g,n)=(1,2)` graph surface includes both codimension-2 planted forests;
- the direct shadow-tensor lift of the genus-(1,2) recursion fails the
  single-channel benchmark;
- the alternative CohFT three-point lift matches the Virasoro benchmark but the
  resulting naive genus-2 graph sum still fails the proved scalar formula.
"""

from __future__ import annotations

import unittest
from fractions import Fraction

from compute.lib.multichannel_mc_recursion import (
    C3_func,
    S3,
    genus1_boundary_graph_audit,
    genus2_multichannel,
    kappa,
    lambda_fp,
    naive_genus2_single_channel,
    verify_ell2_single_channel,
    virasoro_ell2_reference,
)


class TestExactChannelData(unittest.TestCase):
    def test_per_channel_kappa(self) -> None:
        c = Fraction(30)
        self.assertEqual(kappa("T", c), Fraction(15))
        self.assertEqual(kappa("W", c), Fraction(10))

    def test_cubic_tensor(self) -> None:
        c = Fraction(30)
        self.assertEqual(S3("T", "T", "T", c), Fraction(2))
        self.assertEqual(S3("T", "W", "W", c), Fraction(1))
        self.assertEqual(S3("T", "T", "W", c), Fraction(0))
        self.assertEqual(S3("W", "W", "W", c), Fraction(0))

    def test_three_point_constants(self) -> None:
        c = Fraction(26)
        self.assertEqual(C3_func("T", "T", "T", c), c)
        self.assertEqual(C3_func("T", "W", "W", c), c)
        self.assertEqual(C3_func("T", "T", "W", c), Fraction(0))


class TestGenus1BoundaryAudit(unittest.TestCase):
    def test_both_codim2_graphs_exist(self) -> None:
        audit = genus1_boundary_graph_audit()
        self.assertEqual(audit["graph_count"], 5)
        self.assertTrue(audit["has_double_bridge"])
        self.assertTrue(audit["has_self_loop_plus_bridge"])


class TestEll2Rectification(unittest.TestCase):
    def test_reference_formula(self) -> None:
        self.assertEqual(virasoro_ell2_reference(Fraction(6)), Fraction(-15, 4))
        self.assertEqual(virasoro_ell2_reference(Fraction(26)), Fraction(-35, 12))

    def test_shadow_tensor_lift_fails_benchmark(self) -> None:
        for c in (Fraction(6), Fraction(26), Fraction(50)):
            audit = verify_ell2_single_channel(c)
            self.assertEqual(audit["reference"], virasoro_ell2_reference(c))
            self.assertFalse(audit["shadow_tensor_match"])
            self.assertFalse(audit["cohft_match"])


class TestGenus2Rectification(unittest.TestCase):
    def test_lambda_fp_genus2(self) -> None:
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_naive_single_channel_graph_sum_fails(self) -> None:
        for c in (Fraction(6), Fraction(26), Fraction(50)):
            audit = naive_genus2_single_channel(c)
            self.assertFalse(audit["matches"])
            self.assertNotEqual(audit["F2_naive"], audit["expected"])

    def test_naive_multichannel_graph_sum_fails(self) -> None:
        for c in (Fraction(6), Fraction(26), Fraction(50)):
            audit = genus2_multichannel(c)
            self.assertFalse(audit["single_channel_match"])
            self.assertFalse(audit["universality_holds"])
            self.assertNotEqual(audit["F2_multi"], audit["F2_expected"])


if __name__ == "__main__":
    unittest.main()
