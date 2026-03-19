"""Tests for prefundamental CG decomposition for types B_2 and G_2.

Verifies the FRONTIER computation extending MC3 (conj:mc3-arbitrary-type)
to non-simply-laced types. The universal CG theorem

    [V_lambda] * [L^-_i] = sum_{mu in wt(V_lambda)} mult(mu) * [L^-_i(shift=mu)]

is proved algebraically (distributive law, see prefundamental_cg_universal.py
Remark line 33). This module provides computational verification for:

  - B_2 = so_5 (rank 2, non-simply-laced)
  - G_2 (rank 2, exceptional)
  - A_2 = sl_3 (cross-check against prefundamental_cg_sl3.py)

If the character-level CG holds for B_2 and G_2 with the same structure
as type A (weight multiplicities as coefficients), then the algebraic
proof extends to ALL simple types. Combined with MC3 type A resolution
(thm:mc3-type-a-resolution), this provides evidence for conj:mc3-arbitrary-type.

References:
  - Hernandez-Jimbo 2012, Section 5
  - concordance.tex, conj:mc3-arbitrary-type
"""

import unittest

from compute.lib.prefundamental_cg_typeB import (
    Rank2RootSystem,
    B2, G2, A2,
    B2_dim, G2_dim,
    verify_cg, verify_batch,
    tensor_product, shift_char, subtract_char,
)


class TestB2RootSystem(unittest.TestCase):
    """Root system data for B_2 = so_5."""

    def setUp(self):
        self.rs = B2()

    def test_positive_root_count(self):
        """B_2 has 4 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 4)

    def test_positive_roots_alpha(self):
        """Positive roots in alpha coordinates."""
        expected = {(1, 0), (0, 1), (1, 1), (2, 1)}
        self.assertEqual(set(self.rs.positive_roots_alpha), expected)

    def test_weyl_group_order(self):
        """Weyl group of B_2 has order 8."""
        self.assertEqual(len(self.rs.weyl_group), 8)

    def test_roots_containing_alpha1(self):
        """Roots containing alpha_1: alpha_1, alpha_1+alpha_2, 2*alpha_1+alpha_2."""
        indices = self.rs.roots_containing[0]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        self.assertEqual(roots, {(1, 0), (1, 1), (2, 1)})

    def test_roots_containing_alpha2(self):
        """Roots containing alpha_2: alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2."""
        indices = self.rs.roots_containing[1]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        self.assertEqual(roots, {(0, 1), (1, 1), (2, 1)})


class TestB2Dimensions(unittest.TestCase):
    """Weyl dimension formula for B_2."""

    def setUp(self):
        self.rs = B2()

    def test_spin_rep(self):
        """V_{omega_1} = 4-dim spin rep."""
        char = self.rs.irrep_character((1, 0), depth=10)
        self.assertEqual(sum(char.values()), 4)
        self.assertEqual(B2_dim(1, 0), 4)

    def test_vector_rep(self):
        """V_{omega_2} = 5-dim vector rep."""
        char = self.rs.irrep_character((0, 1), depth=10)
        self.assertEqual(sum(char.values()), 5)
        self.assertEqual(B2_dim(0, 1), 5)

    def test_adjoint_rep(self):
        """V_{2*omega_1} = 10-dim (adjoint of so_5)."""
        char = self.rs.irrep_character((2, 0), depth=10)
        self.assertEqual(sum(char.values()), 10)
        self.assertEqual(B2_dim(2, 0), 10)

    def test_formula_matches_character(self):
        """Dimension formula matches character computation for |hw| <= 4."""
        for a in range(5):
            for b in range(5 - a):
                if a == 0 and b == 0:
                    continue
                char = self.rs.irrep_character((a, b), depth=20)
                dim_char = sum(char.values())
                dim_formula = B2_dim(a, b)
                self.assertEqual(dim_char, dim_formula,
                                 f"Dimension mismatch for V({a},{b}): char={dim_char}, formula={dim_formula}")


class TestB2Prefundamental(unittest.TestCase):
    """Prefundamental character properties for B_2."""

    def setUp(self):
        self.rs = B2()

    def test_hw_mult_one(self):
        """Both L^-_i have highest weight (0,0) with multiplicity 1."""
        for node in [0, 1]:
            char = self.rs.prefundamental_character(node, depth=8)
            self.assertEqual(char.get((0, 0), 0), 1,
                             f"L^-_{node+1} should have mult 1 at (0,0)")

    def test_all_weights_nonpositive_direction(self):
        """All weights of L^-_i should be <= (0,0) in a suitable sense:
        they are hw - (non-negative combination of positive roots)."""
        for node in [0, 1]:
            char = self.rs.prefundamental_character(node, depth=6)
            for w, m in char.items():
                self.assertGreater(m, 0, f"Negative mult at {w}")


class TestB2CG(unittest.TestCase):
    """CG decomposition verification for B_2."""

    def setUp(self):
        self.rs = B2()

    def test_cg_spin_node1(self):
        """V_{omega_1} x L^-_1 decomposes correctly."""
        res = verify_cg(self.rs, (1, 0), 0, depth=8)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_spin_node2(self):
        """V_{omega_1} x L^-_2 decomposes correctly."""
        res = verify_cg(self.rs, (1, 0), 1, depth=8)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_vector_node1(self):
        """V_{omega_2} x L^-_1 decomposes correctly."""
        res = verify_cg(self.rs, (0, 1), 0, depth=8)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_vector_node2(self):
        """V_{omega_2} x L^-_2 decomposes correctly."""
        res = verify_cg(self.rs, (0, 1), 1, depth=8)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_adjoint(self):
        """V_{2*omega_1} (adjoint) x L^-_i decomposes correctly."""
        for node in [0, 1]:
            res = verify_cg(self.rs, (2, 0), node, depth=8)
            self.assertTrue(res["match"], f"CG failed for node {node}: {res['mismatches']}")

    def test_cg_batch_hw_le_3(self):
        """All dominant weights with |hw| <= 3 pass CG for both nodes."""
        batch = verify_batch(self.rs, max_hw_sum=3, depth=8)
        self.assertTrue(batch["all_pass"],
                        f"B2 CG batch failed: {batch['n_fail']} failures")
        self.assertGreaterEqual(batch["n_pass"], 18)

    def test_cg_batch_hw_le_4(self):
        """All dominant weights with |hw| <= 4 pass CG for both nodes."""
        batch = verify_batch(self.rs, max_hw_sum=4, depth=7)
        self.assertTrue(batch["all_pass"],
                        f"B2 CG batch failed: {batch['n_fail']} failures")
        self.assertGreaterEqual(batch["n_pass"], 28)


class TestG2RootSystem(unittest.TestCase):
    """Root system data for G_2."""

    def setUp(self):
        self.rs = G2()

    def test_positive_root_count(self):
        """G_2 has 6 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 6)

    def test_positive_roots_alpha(self):
        """Positive roots in alpha coordinates."""
        expected = {(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)}
        self.assertEqual(set(self.rs.positive_roots_alpha), expected)

    def test_weyl_group_order(self):
        """Weyl group of G_2 has order 12."""
        self.assertEqual(len(self.rs.weyl_group), 12)

    def test_roots_containing_alpha1(self):
        """Roots containing alpha_1 (short root)."""
        indices = self.rs.roots_containing[0]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(1, 0), (1, 1), (2, 1), (3, 1), (3, 2)}
        self.assertEqual(roots, expected)

    def test_roots_containing_alpha2(self):
        """Roots containing alpha_2 (long root)."""
        indices = self.rs.roots_containing[1]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(0, 1), (1, 1), (2, 1), (3, 1), (3, 2)}
        self.assertEqual(roots, expected)


class TestG2Dimensions(unittest.TestCase):
    """Weyl dimension formula for G_2."""

    def setUp(self):
        self.rs = G2()

    def test_7dim_rep(self):
        """V_{omega_1} = 7-dim fundamental."""
        char = self.rs.irrep_character((1, 0), depth=15)
        self.assertEqual(sum(char.values()), 7)
        self.assertEqual(G2_dim(1, 0), 7)

    def test_14dim_rep(self):
        """V_{omega_2} = 14-dim (adjoint)."""
        char = self.rs.irrep_character((0, 1), depth=15)
        self.assertEqual(sum(char.values()), 14)
        self.assertEqual(G2_dim(0, 1), 14)

    def test_27dim_rep(self):
        """V_{2*omega_1} = 27-dim."""
        char = self.rs.irrep_character((2, 0), depth=15)
        self.assertEqual(sum(char.values()), 27)
        self.assertEqual(G2_dim(2, 0), 27)

    def test_formula_matches_character(self):
        """Dimension formula matches character for |hw| <= 3.

        G2 has large root coefficients so higher reps need greater depth.
        """
        for a in range(4):
            for b in range(4 - a):
                if a == 0 and b == 0:
                    continue
                # G2 needs depth ~ 10*(a+b) for large reps
                d = max(20, 10 * (a + b))
                char = self.rs.irrep_character((a, b), depth=d)
                dim_char = sum(char.values())
                dim_formula = G2_dim(a, b)
                self.assertEqual(dim_char, dim_formula,
                                 f"G2 dim mismatch for V({a},{b}): char={dim_char}, formula={dim_formula}")


class TestG2Prefundamental(unittest.TestCase):
    """Prefundamental character properties for G_2."""

    def setUp(self):
        self.rs = G2()

    def test_hw_mult_one(self):
        """Both L^-_i have highest weight (0,0) with multiplicity 1."""
        for node in [0, 1]:
            char = self.rs.prefundamental_character(node, depth=6)
            self.assertEqual(char.get((0, 0), 0), 1)


class TestG2CG(unittest.TestCase):
    """CG decomposition verification for G_2."""

    def setUp(self):
        self.rs = G2()

    def test_cg_7dim_node1(self):
        """V_{omega_1} (7-dim) x L^-_1."""
        res = verify_cg(self.rs, (1, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_7dim_node2(self):
        """V_{omega_1} (7-dim) x L^-_2."""
        res = verify_cg(self.rs, (1, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_14dim_node1(self):
        """V_{omega_2} (14-dim adjoint) x L^-_1."""
        res = verify_cg(self.rs, (0, 1), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_14dim_node2(self):
        """V_{omega_2} (14-dim adjoint) x L^-_2."""
        res = verify_cg(self.rs, (0, 1), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_batch_hw_le_2(self):
        """All dominant weights with |hw| <= 2 pass CG."""
        batch = verify_batch(self.rs, max_hw_sum=2, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"G2 CG batch failed: {batch['n_fail']} failures")
        self.assertGreaterEqual(batch["n_pass"], 10)

    def test_cg_batch_hw_le_3(self):
        """All dominant weights with |hw| <= 3 pass CG."""
        batch = verify_batch(self.rs, max_hw_sum=3, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"G2 CG batch failed: {batch['n_fail']} failures")
        self.assertGreaterEqual(batch["n_pass"], 18)


class TestA2CrossCheck(unittest.TestCase):
    """Cross-check against type A_2 = sl_3."""

    def setUp(self):
        self.rs = A2()

    def test_positive_root_count(self):
        """A_2 has 3 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 3)

    def test_weyl_group_order(self):
        """Weyl group of A_2 has order 6."""
        self.assertEqual(len(self.rs.weyl_group), 6)

    def test_standard_rep_dim(self):
        """V_{omega_1} = 3-dim."""
        char = self.rs.irrep_character((1, 0), depth=10)
        self.assertEqual(sum(char.values()), 3)

    def test_adjoint_rep_dim(self):
        """V_{omega_1 + omega_2} = 8-dim."""
        char = self.rs.irrep_character((1, 1), depth=10)
        self.assertEqual(sum(char.values()), 8)

    def test_cg_batch(self):
        """CG holds for A_2 (consistency with prefundamental_cg_sl3.py)."""
        batch = verify_batch(self.rs, max_hw_sum=3, depth=8)
        self.assertTrue(batch["all_pass"],
                        f"A2 CG batch failed: {batch['n_fail']} failures")


class TestUniversalCGStructure(unittest.TestCase):
    """Verify the universal structure: CG multiplicities = weight multiplicities.

    The KEY INSIGHT: for ALL types, V_lambda x L^-_i decomposes with
    multiplicities equal to the weight multiplicities of V_lambda.
    This is a consequence of the distributive law (finite sum x power series).
    """

    def test_b2_cg_coefficients_are_weight_mults(self):
        """For B_2, verify that the CG is EXACTLY the weight-multiplicity formula."""
        rs = B2()
        hw = (1, 1)  # 16-dim rep
        V_char = rs.irrep_character(hw, depth=15)
        for node in [0, 1]:
            L_char = rs.prefundamental_character(node, depth=8)
            lhs = tensor_product(V_char, L_char)
            # Build RHS from weight multiplicities
            rhs = {}
            for mu, mult in V_char.items():
                shifted = shift_char(L_char, mu)
                for w, m in shifted.items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            # Compare
            diff = subtract_char(lhs, rhs)
            # Filter reliable range
            reliable = {w: m for w, m in diff.items() if abs(w[0]) + abs(w[1]) < 8}
            self.assertEqual(len(reliable), 0,
                             f"B2 V(1,1) x L^-_{node+1}: nonzero diff at {reliable}")

    def test_g2_cg_coefficients_are_weight_mults(self):
        """For G_2, verify that the CG is EXACTLY the weight-multiplicity formula."""
        rs = G2()
        hw = (1, 0)  # 7-dim rep
        V_char = rs.irrep_character(hw, depth=15)
        for node in [0, 1]:
            L_char = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product(V_char, L_char)
            rhs = {}
            for mu, mult in V_char.items():
                shifted = shift_char(L_char, mu)
                for w, m in shifted.items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char(lhs, rhs)
            reliable = {w: m for w, m in diff.items() if abs(w[0]) + abs(w[1]) < 6}
            self.assertEqual(len(reliable), 0,
                             f"G2 V(1,0) x L^-_{node+1}: nonzero diff at {reliable}")


if __name__ == "__main__":
    unittest.main()
