"""Tests for prefundamental CG decomposition for Y(sl_3).

Verifies the FRONTIER computation extending MC3 from type A_1 to A_2.

MAIN RESULT (character level):
  [V_lambda] * [L^-_i] = sum_{mu in weights(V_lambda)} mult_lambda(mu) * [L^-_i(shift=mu)]

This is the exact rank-2 generalization of the sl_2 CG closure theorem
(prop:prefundamental-clebsch-gordan). The decomposition:
  (1) Is EXACT (no remainder).
  (2) Uses only L^-_i of the SAME index i.
  (3) Multiplicity equals weight multiplicity of V_lambda at the shift.

References:
  - Hernandez-Jimbo 2012, Section 5
  - concordance.tex, conj:mc3-arbitrary-type
"""

import unittest

from compute.lib.prefundamental_cg_sl3 import (
    weyl_dim_sl3,
    sl3_irrep_character,
    sl3_weight_multiplicity,
    prefundamental_character_sl3_1,
    prefundamental_character_sl3_2,
    tensor_product_sl3,
    sum_characters_sl3,
    shift_character_sl3,
    subtract_characters_sl3,
    cg_test_sl3,
    analytical_cg_V10_L1,
    verify_sl3_weight_formula,
    verify_prefundamental_basic,
    verify_cg_closes,
)
from compute.lib.utils import partition_number


# ---------------------------------------------------------------------------
# Weight formula tests
# ---------------------------------------------------------------------------

class TestSl3WeightFormula(unittest.TestCase):
    """Verify sl_3 weight multiplicities and dimensions."""

    def test_V10_dim(self):
        self.assertEqual(weyl_dim_sl3(1, 0), 3)

    def test_V01_dim(self):
        self.assertEqual(weyl_dim_sl3(0, 1), 3)

    def test_V11_dim(self):
        self.assertEqual(weyl_dim_sl3(1, 1), 8)

    def test_V20_dim(self):
        self.assertEqual(weyl_dim_sl3(2, 0), 6)

    def test_V02_dim(self):
        self.assertEqual(weyl_dim_sl3(0, 2), 6)

    def test_V21_dim(self):
        self.assertEqual(weyl_dim_sl3(2, 1), 15)

    def test_V30_dim(self):
        self.assertEqual(weyl_dim_sl3(3, 0), 10)

    def test_V10_weights(self):
        char = sl3_irrep_character((1, 0), depth=5)
        self.assertEqual(sum(char.values()), 3)
        self.assertEqual(char.get((1, 0), 0), 1)
        self.assertEqual(char.get((-1, 1), 0), 1)
        self.assertEqual(char.get((0, -1), 0), 1)

    def test_V01_weights(self):
        char = sl3_irrep_character((0, 1), depth=5)
        self.assertEqual(sum(char.values()), 3)
        self.assertEqual(char.get((0, 1), 0), 1)
        self.assertEqual(char.get((1, -1), 0), 1)
        self.assertEqual(char.get((-1, 0), 0), 1)

    def test_V11_zero_weight_mult(self):
        """Adjoint has 2-dim zero weight space (Cartan subalgebra)."""
        char = sl3_irrep_character((1, 1), depth=5)
        self.assertEqual(char.get((0, 0), 0), 2)

    def test_V11_total_dim(self):
        char = sl3_irrep_character((1, 1), depth=5)
        self.assertEqual(sum(char.values()), 8)

    def test_V20_total_dim(self):
        char = sl3_irrep_character((2, 0), depth=5)
        self.assertEqual(sum(char.values()), 6)

    def test_V22_dim(self):
        self.assertEqual(weyl_dim_sl3(2, 2), 27)

    def test_V22_character_dim(self):
        char = sl3_irrep_character((2, 2), depth=8)
        self.assertEqual(sum(char.values()), 27)

    def test_all_weight_formulas(self):
        results = verify_sl3_weight_formula()
        for name, ok in results.items():
            self.assertTrue(ok, f"weight formula check failed: {name}")


# ---------------------------------------------------------------------------
# Prefundamental character tests
# ---------------------------------------------------------------------------

class TestPrefundamentalCharacterSl3(unittest.TestCase):
    """Verify prefundamental character structure."""

    def test_L1_hw(self):
        L1 = prefundamental_character_sl3_1(depth=5)
        self.assertEqual(L1.get((0, 0), 0), 1)

    def test_L2_hw(self):
        L2 = prefundamental_character_sl3_2(depth=5)
        self.assertEqual(L2.get((0, 0), 0), 1)

    def test_L1_alpha1_mult(self):
        """Weight -alpha_1 = (-2, 1) has mult p(1)*p(0) = 1."""
        L1 = prefundamental_character_sl3_1(depth=5)
        self.assertEqual(L1.get((-2, 1), 0), 1)

    def test_L1_alpha12_mult(self):
        """Weight -(alpha_1+alpha_2) = (-1, -1) has mult p(0)*p(1) = 1."""
        L1 = prefundamental_character_sl3_1(depth=5)
        self.assertEqual(L1.get((-1, -1), 0), 1)

    def test_L2_alpha2_mult(self):
        L2 = prefundamental_character_sl3_2(depth=5)
        self.assertEqual(L2.get((1, -2), 0), 1)

    def test_L1_swap_equals_L2(self):
        """L^-_2 is L^-_1 with omega_1 <-> omega_2 swapped."""
        results = verify_prefundamental_basic()
        self.assertTrue(results["L1 swap = L2"])

    def test_L1_deeper_mult(self):
        """Weight at (a=2, b=1) has mult p(2)*p(1) = 2."""
        L1 = prefundamental_character_sl3_1(depth=10)
        self.assertEqual(L1.get((-5, 1), 0), 2)

    def test_L1_a3_b2_mult(self):
        """Weight at (a=3, b=2) has mult p(3)*p(2) = 6."""
        L1 = prefundamental_character_sl3_1(depth=10)
        # (a=3, b=2): weight = (-2*3-2, 3-2) = (-8, 1)
        self.assertEqual(L1.get((-8, 1), 0), 6)

    def test_all_prefundamental_basic(self):
        results = verify_prefundamental_basic()
        for name, ok in results.items():
            self.assertTrue(ok, f"prefundamental check failed: {name}")


# ---------------------------------------------------------------------------
# CG decomposition: fundamental representations
# ---------------------------------------------------------------------------

class TestCGFundamental(unittest.TestCase):
    """CG decomposition for fundamental V_{(1,0)} and V_{(0,1)}."""

    def test_V10_L1_exact(self):
        cg = cg_test_sl3((1, 0), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V10_L2_exact(self):
        cg = cg_test_sl3((1, 0), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V01_L1_exact(self):
        cg = cg_test_sl3((0, 1), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V01_L2_exact(self):
        cg = cg_test_sl3((0, 1), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V10_L1_three_summands(self):
        """V_{(1,0)} tensor L^-_1 has 3 summands (dim V_{(1,0)} = 3)."""
        cg = cg_test_sl3((1, 0), 1, depth=10)
        self.assertEqual(cg["n_summands"], 3)

    def test_V01_L2_three_summands(self):
        cg = cg_test_sl3((0, 1), 2, depth=10)
        self.assertEqual(cg["n_summands"], 3)

    def test_V10_L1_shifts_are_weights(self):
        """Shifts in CG = weights of V_{(1,0)}."""
        cg = cg_test_sl3((1, 0), 1, depth=10)
        shifts = {s["shift"] for s in cg["summands"]}
        expected = {(1, 0), (-1, 1), (0, -1)}
        self.assertEqual(shifts, expected)

    def test_V01_L1_shifts_are_weights(self):
        cg = cg_test_sl3((0, 1), 1, depth=10)
        shifts = {s["shift"] for s in cg["summands"]}
        expected = {(0, 1), (1, -1), (-1, 0)}
        self.assertEqual(shifts, expected)

    def test_V10_L1_all_mult_one(self):
        """All multiplicities = 1 (all weights of V_{(1,0)} have mult 1)."""
        cg = cg_test_sl3((1, 0), 1, depth=10)
        for s in cg["summands"]:
            self.assertEqual(s["multiplicity"], 1)

    def test_V10_L1_same_type(self):
        """All summands are L^-_1 (same index)."""
        cg = cg_test_sl3((1, 0), 1, depth=10)
        for s in cg["summands"]:
            self.assertEqual(s["type"], "L^-_1")

    def test_V10_L2_same_type(self):
        cg = cg_test_sl3((1, 0), 2, depth=10)
        for s in cg["summands"]:
            self.assertEqual(s["type"], "L^-_2")


# ---------------------------------------------------------------------------
# CG decomposition: adjoint representation
# ---------------------------------------------------------------------------

class TestCGAdjoint(unittest.TestCase):
    """CG for adjoint V_{(1,1)} (dim 8)."""

    def test_V11_L1_exact(self):
        cg = cg_test_sl3((1, 1), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V11_L2_exact(self):
        cg = cg_test_sl3((1, 1), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V11_L1_has_mult_2_at_zero(self):
        """Adjoint has (0,0) with mult 2, so L^-_1((0,0)) appears with mult 2."""
        cg = cg_test_sl3((1, 1), 1, depth=10)
        zero_summands = [s for s in cg["summands"] if s.get("shift") == (0, 0)]
        self.assertEqual(len(zero_summands), 1)
        self.assertEqual(zero_summands[0]["multiplicity"], 2)

    def test_V11_total_summand_mult(self):
        """Total multiplicity = dim V_{(1,1)} = 8."""
        cg = cg_test_sl3((1, 1), 1, depth=10)
        total = sum(s["multiplicity"] for s in cg["summands"])
        self.assertEqual(total, 8)


# ---------------------------------------------------------------------------
# CG decomposition: symmetric square representations
# ---------------------------------------------------------------------------

class TestCGSymmetricSquare(unittest.TestCase):
    """CG for V_{(2,0)} and V_{(0,2)} (dim 6 each)."""

    def test_V20_L1_exact(self):
        cg = cg_test_sl3((2, 0), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V20_L2_exact(self):
        cg = cg_test_sl3((2, 0), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V02_L1_exact(self):
        cg = cg_test_sl3((0, 2), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V02_L2_exact(self):
        cg = cg_test_sl3((0, 2), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V20_total_mult(self):
        cg = cg_test_sl3((2, 0), 1, depth=10)
        total = sum(s["multiplicity"] for s in cg["summands"])
        self.assertEqual(total, 6)

    def test_V02_total_mult(self):
        cg = cg_test_sl3((0, 2), 2, depth=10)
        total = sum(s["multiplicity"] for s in cg["summands"])
        self.assertEqual(total, 6)


# ---------------------------------------------------------------------------
# CG: higher representations
# ---------------------------------------------------------------------------

class TestCGHigher(unittest.TestCase):
    """CG for higher representations: (2,1), (1,2), (3,0), (0,3)."""

    def test_V21_L1_exact(self):
        cg = cg_test_sl3((2, 1), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V21_L2_exact(self):
        cg = cg_test_sl3((2, 1), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V12_L1_exact(self):
        cg = cg_test_sl3((1, 2), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V12_L2_exact(self):
        cg = cg_test_sl3((1, 2), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V30_L1_exact(self):
        cg = cg_test_sl3((3, 0), 1, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V03_L2_exact(self):
        cg = cg_test_sl3((0, 3), 2, depth=10)
        self.assertTrue(cg["decomposition_exact"])

    def test_V21_total_mult_is_dim(self):
        """Total multiplicity = dim V_{(2,1)} = 15."""
        cg = cg_test_sl3((2, 1), 1, depth=10)
        total = sum(s["multiplicity"] for s in cg["summands"])
        self.assertEqual(total, 15)

    def test_V30_total_mult_is_dim(self):
        """Total multiplicity = dim V_{(3,0)} = 10."""
        cg = cg_test_sl3((3, 0), 1, depth=10)
        total = sum(s["multiplicity"] for s in cg["summands"])
        self.assertEqual(total, 10)


# ---------------------------------------------------------------------------
# The main theorem: CG decomposes into same-index shifted prefundamentals
# ---------------------------------------------------------------------------

class TestMainTheorem(unittest.TestCase):
    """The sl_3 prefundamental CG theorem (character level).

    THEOREM: For all dominant weights lambda = (a, b) and i in {1, 2}:

      [V_lambda] * [L^-_i] = sum_{mu in weights(V_lambda)} mult_lambda(mu) * [L^-_i(mu)]

    where mult_lambda(mu) is the weight multiplicity of mu in V_lambda.

    This is the EXACT rank-2 generalization of the sl_2 CG closure.
    """

    def _verify_theorem(self, a: int, b: int, i: int, depth: int = 10):
        """Verify the theorem for V_{(a,b)} tensor L^-_i."""
        cg = cg_test_sl3((a, b), i, depth=depth)
        self.assertTrue(
            cg["decomposition_exact"],
            f"CG not exact for V({a},{b}) x L^-_{i}",
        )

        # Check same-index property
        for s in cg["summands"]:
            if "type" in s and s["type"] != "RESIDUAL":
                self.assertEqual(
                    s["type"], f"L^-_{i}",
                    f"Mixed-index summand in V({a},{b}) x L^-_{i}: {s}",
                )

        # Check total multiplicity = dim V_{(a,b)}
        total = sum(s["multiplicity"] for s in cg["summands"])
        self.assertEqual(
            total, weyl_dim_sl3(a, b),
            f"Total mult {total} != dim {weyl_dim_sl3(a, b)} for V({a},{b})",
        )

    def test_theorem_hw_sum_1(self):
        for a, b in [(1, 0), (0, 1)]:
            for i in [1, 2]:
                self._verify_theorem(a, b, i)

    def test_theorem_hw_sum_2(self):
        for a, b in [(2, 0), (1, 1), (0, 2)]:
            for i in [1, 2]:
                self._verify_theorem(a, b, i)

    def test_theorem_hw_sum_3(self):
        for a, b in [(3, 0), (2, 1), (1, 2), (0, 3)]:
            for i in [1, 2]:
                self._verify_theorem(a, b, i)

    def test_theorem_hw_sum_4(self):
        for a, b in [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]:
            for i in [1, 2]:
                self._verify_theorem(a, b, i, depth=12)


# ---------------------------------------------------------------------------
# Structural properties
# ---------------------------------------------------------------------------

class TestStructuralProperties(unittest.TestCase):
    """Properties of the CG decomposition."""

    def test_outer_automorphism_symmetry(self):
        """sl_3 outer automorphism swaps (a,b) <-> (b,a) and L^-_1 <-> L^-_2.

        So CG for V_{(a,b)} x L^-_1 should match CG for V_{(b,a)} x L^-_2
        after swapping omega indices.
        """
        for a, b in [(1, 0), (2, 1), (1, 1)]:
            cg1 = cg_test_sl3((a, b), 1, depth=10)
            cg2 = cg_test_sl3((b, a), 2, depth=10)
            self.assertEqual(cg1["n_summands"], cg2["n_summands"])
            self.assertTrue(cg1["decomposition_exact"])
            self.assertTrue(cg2["decomposition_exact"])

    def test_trivial_tensor_is_identity(self):
        """V_{(0,0)} tensor L^-_i = L^-_i (trivially)."""
        for i in [1, 2]:
            if i == 1:
                L = prefundamental_character_sl3_1(depth=8)
            else:
                L = prefundamental_character_sl3_2(depth=8)
            V0 = sl3_irrep_character((0, 0), depth=5)
            tensor = tensor_product_sl3(V0, L)
            # Should equal L
            diff = subtract_characters_sl3(tensor, L)
            self.assertEqual(
                len({w: m for w, m in diff.items() if m != 0}), 0,
                f"V(0,0) x L^-_{i} != L^-_{i}",
            )

    def test_evaluation_stability(self):
        """L^-_i is closed under tensoring with V_{(1,0)} and V_{(0,1)}.

        This means the set {L^-_i(shift)} is evaluation-stable,
        just as in the sl_2 case.
        """
        for i in [1, 2]:
            cg1 = cg_test_sl3((1, 0), i, depth=10)
            cg2 = cg_test_sl3((0, 1), i, depth=10)
            self.assertTrue(cg1["decomposition_exact"])
            self.assertTrue(cg2["decomposition_exact"])
            # All summands are same-index
            for s in cg1["summands"] + cg2["summands"]:
                self.assertEqual(s["type"], f"L^-_{i}")


# ---------------------------------------------------------------------------
# Analytical V_{(1,0)} tensor L^-_1 test
# ---------------------------------------------------------------------------

class TestAnalyticalCG(unittest.TestCase):
    """Direct analytical verification of V_{(1,0)} tensor L^-_1."""

    def test_analytical_nonneg_L1(self):
        """Subtracting L^-_1(shift=(1,0)) leaves non-negative remainder."""
        ana = analytical_cg_V10_L1(depth=12)
        self.assertTrue(ana["remainder_L1_shift_10_nonneg"])

    def test_analytical_L2_fails(self):
        """Subtracting L^-_2(shift=(1,0)) produces negative remainder."""
        ana = analytical_cg_V10_L1(depth=12)
        self.assertFalse(ana["remainder_L2_shift_10_nonneg"])

    def test_analytical_hw_mult_one(self):
        ana = analytical_cg_V10_L1(depth=12)
        self.assertEqual(ana["tensor_hw_mult"], 1)


# ---------------------------------------------------------------------------
# Direct formula verification
# ---------------------------------------------------------------------------

class TestDirectFormula(unittest.TestCase):
    """Verify the direct formula:

    ch(V_lambda tensor L^-_i) = sum_{mu} mult_lambda(mu) * ch(L^-_i(mu))

    by computing both sides independently.
    """

    def _check_formula(self, hw: tuple, i: int, depth: int = 10):
        V_char = sl3_irrep_character(hw, depth=depth + sum(hw))
        if i == 1:
            L = prefundamental_character_sl3_1(depth=depth)
        else:
            L = prefundamental_character_sl3_2(depth=depth)

        # LHS: tensor product
        lhs = tensor_product_sl3(V_char, L)

        # RHS: sum of shifted L^-_i weighted by V_lambda multiplicities
        rhs = {}
        for mu, mult in V_char.items():
            shifted = shift_character_sl3(L, mu)
            for w, m in shifted.items():
                rhs[w] = rhs.get(w, 0) + mult * m

        # Compare within reliable range
        all_weights = set(lhs.keys()) | set(rhs.keys())
        for w in all_weights:
            dist = abs(w[0]) + abs(w[1])
            if dist < 2 * (depth - 5):
                self.assertEqual(
                    lhs.get(w, 0), rhs.get(w, 0),
                    f"Mismatch at weight {w} for V{hw} x L^-_{i}: "
                    f"LHS={lhs.get(w,0)}, RHS={rhs.get(w,0)}",
                )

    def test_formula_V10_L1(self):
        self._check_formula((1, 0), 1)

    def test_formula_V01_L1(self):
        self._check_formula((0, 1), 1)

    def test_formula_V10_L2(self):
        self._check_formula((1, 0), 2)

    def test_formula_V01_L2(self):
        self._check_formula((0, 1), 2)

    def test_formula_V11_L1(self):
        self._check_formula((1, 1), 1)

    def test_formula_V11_L2(self):
        self._check_formula((1, 1), 2)

    def test_formula_V20_L1(self):
        self._check_formula((2, 0), 1)

    def test_formula_V21_L1(self):
        self._check_formula((2, 1), 1)

    def test_formula_V30_L1(self):
        self._check_formula((3, 0), 1)

    def test_formula_V22_L1(self):
        self._check_formula((2, 2), 1, depth=12)

    def test_formula_V40_L1(self):
        self._check_formula((4, 0), 1, depth=12)


if __name__ == "__main__":
    unittest.main()
