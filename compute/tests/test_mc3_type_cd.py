"""Tests for prefundamental CG closure at rank 3: B_3, C_3, A_3.

Verifies the FRONTIER computation extending MC3 (conj:mc3-arbitrary-type)
to rank-3 classical types. The universal CG identity

    ch(V_lambda) * ch(L^-_i) = sum_{mu in wt(V_lambda)} mult(mu) * ch(L^-_i(shift=mu))

is verified by explicit coefficient comparison at finite depth.

Combined with MC3 type A resolution (thm:mc3-type-a-resolution) and
rank-2 verification (prefundamental_cg_typeB.py), this completes
character-level CG verification through rank 3 for all classical types.

References:
  - Hernandez-Jimbo 2012, Section 5
  - concordance.tex, conj:mc3-arbitrary-type
"""

import unittest

from compute.lib.mc3_type_cd import (
    Rank3RootSystem,
    B3, C3, A3,
    B3_dim, C3_dim, A3_dim,
    verify_cg3, verify_batch3,
    tensor_product3, shift_char3, subtract_char3,
    char_dim,
    check_langlands_duality,
    verify_verma_containment3,
    verma_character3,
    prefundamental_product_character,
)


# ===================================================================
# B_3 = so_7 root system structure
# ===================================================================

class TestB3RootSystem(unittest.TestCase):
    """Root system data for B_3 = so_7."""

    def setUp(self):
        self.rs = B3()

    def test_positive_root_count(self):
        """B_3 has 9 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 9)

    def test_positive_roots_alpha(self):
        """Positive roots in alpha coordinates for B_3."""
        expected = {
            (1, 0, 0), (0, 1, 0), (0, 0, 1),
            (1, 1, 0), (0, 1, 1), (0, 1, 2),
            (1, 1, 1), (1, 1, 2), (1, 2, 2),
        }
        self.assertEqual(set(self.rs.positive_roots_alpha), expected)

    def test_weyl_group_order(self):
        """Weyl group of B_3 has order 48 = 2^3 * 3!."""
        self.assertEqual(len(self.rs.weyl_group), 48)

    def test_roots_containing_alpha1(self):
        """Roots containing alpha_1 in B_3: 5 roots."""
        indices = self.rs.roots_containing[0]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 2)}
        self.assertEqual(roots, expected)
        self.assertEqual(len(indices), 5)

    def test_roots_containing_alpha2(self):
        """Roots containing alpha_2 in B_3: 7 roots."""
        indices = self.rs.roots_containing[1]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(0, 1, 0), (1, 1, 0), (0, 1, 1), (0, 1, 2),
                    (1, 1, 1), (1, 1, 2), (1, 2, 2)}
        self.assertEqual(roots, expected)
        self.assertEqual(len(indices), 7)

    def test_roots_containing_alpha3(self):
        """Roots containing alpha_3 (short root) in B_3: 6 roots."""
        indices = self.rs.roots_containing[2]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(0, 0, 1), (0, 1, 1), (0, 1, 2),
                    (1, 1, 1), (1, 1, 2), (1, 2, 2)}
        self.assertEqual(roots, expected)
        self.assertEqual(len(indices), 6)

    def test_highest_root(self):
        """Highest root of B_3 is alpha_1 + 2*alpha_2 + 2*alpha_3."""
        max_ht = max(sum(c) for c in self.rs.positive_roots_alpha)
        highest = [c for c in self.rs.positive_roots_alpha if sum(c) == max_ht]
        self.assertEqual(len(highest), 1)
        self.assertEqual(highest[0], (1, 2, 2))

    def test_simple_roots_omega_basis(self):
        """Simple roots in omega basis from Cartan matrix."""
        self.assertEqual(self.rs.alpha[0], (2, -1, 0))
        self.assertEqual(self.rs.alpha[1], (-1, 2, -2))
        self.assertEqual(self.rs.alpha[2], (0, -1, 2))


# ===================================================================
# C_3 = sp_6 root system structure
# ===================================================================

class TestC3RootSystem(unittest.TestCase):
    """Root system data for C_3 = sp_6."""

    def setUp(self):
        self.rs = C3()

    def test_positive_root_count(self):
        """C_3 has 9 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 9)

    def test_positive_roots_alpha(self):
        """Positive roots in alpha coordinates for C_3."""
        expected = {
            (1, 0, 0), (0, 1, 0), (0, 0, 1),
            (1, 1, 0), (0, 1, 1), (0, 2, 1),
            (1, 1, 1), (1, 2, 1), (2, 2, 1),
        }
        self.assertEqual(set(self.rs.positive_roots_alpha), expected)

    def test_weyl_group_order(self):
        """Weyl group of C_3 has order 48."""
        self.assertEqual(len(self.rs.weyl_group), 48)

    def test_roots_containing_alpha1(self):
        """Roots containing alpha_1 in C_3: 5 roots."""
        indices = self.rs.roots_containing[0]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 1), (2, 2, 1)}
        self.assertEqual(roots, expected)

    def test_roots_containing_alpha2(self):
        """Roots containing alpha_2 in C_3: 7 roots."""
        indices = self.rs.roots_containing[1]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(0, 1, 0), (1, 1, 0), (0, 1, 1), (0, 2, 1),
                    (1, 1, 1), (1, 2, 1), (2, 2, 1)}
        self.assertEqual(roots, expected)

    def test_roots_containing_alpha3(self):
        """Roots containing alpha_3 (long root) in C_3: 6 roots."""
        indices = self.rs.roots_containing[2]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(0, 0, 1), (0, 1, 1), (0, 2, 1),
                    (1, 1, 1), (1, 2, 1), (2, 2, 1)}
        self.assertEqual(roots, expected)

    def test_highest_root(self):
        """Highest root of C_3 is 2*alpha_1 + 2*alpha_2 + alpha_3."""
        max_ht = max(sum(c) for c in self.rs.positive_roots_alpha)
        highest = [c for c in self.rs.positive_roots_alpha if sum(c) == max_ht]
        self.assertEqual(len(highest), 1)
        self.assertEqual(highest[0], (2, 2, 1))


# ===================================================================
# Langlands duality B_3 <-> C_3
# ===================================================================

class TestLanglandsDuality(unittest.TestCase):
    """B_3 and C_3 are Langlands dual."""

    def test_cartan_transpose(self):
        """Cartan matrices are transposes: A_{C_3} = A_{B_3}^T."""
        self.assertTrue(check_langlands_duality())

    def test_same_root_count(self):
        """Langlands dual pairs have the same number of positive roots."""
        self.assertEqual(len(B3().positive_roots), len(C3().positive_roots))

    def test_same_weyl_group_order(self):
        """Langlands dual pairs have the same Weyl group order."""
        self.assertEqual(len(B3().weyl_group), len(C3().weyl_group))

    def test_root_height_multisets_equal(self):
        """Root height multisets are equal for Langlands duals."""
        b3_heights = sorted(sum(c) for c in B3().positive_roots_alpha)
        c3_heights = sorted(sum(c) for c in C3().positive_roots_alpha)
        self.assertEqual(b3_heights, c3_heights)


# ===================================================================
# B_3 dimensions
# ===================================================================

class TestB3Dimensions(unittest.TestCase):
    """Weyl dimension formula vs character computation for B_3."""

    def setUp(self):
        self.rs = B3()

    def test_vector_rep(self):
        """V(omega_1) = 7-dim vector representation of so_7."""
        self.assertEqual(B3_dim(1, 0, 0), 7)
        ch = self.rs.irrep_character((1, 0, 0), depth=15)
        self.assertEqual(char_dim(ch), 7)

    def test_adjoint_rep(self):
        """V(omega_2) = 21-dim adjoint of so_7."""
        self.assertEqual(B3_dim(0, 1, 0), 21)
        ch = self.rs.irrep_character((0, 1, 0), depth=15)
        self.assertEqual(char_dim(ch), 21)

    def test_spin_rep(self):
        """V(omega_3) = 8-dim spin representation of so_7."""
        self.assertEqual(B3_dim(0, 0, 1), 8)
        ch = self.rs.irrep_character((0, 0, 1), depth=15)
        self.assertEqual(char_dim(ch), 8)

    def test_formula_matches_character_fundamentals(self):
        """Dimension formula = character computation for all fundamentals."""
        for hw, d in [((1, 0, 0), 7), ((0, 1, 0), 21), ((0, 0, 1), 8)]:
            self.assertEqual(B3_dim(*hw), d)
            ch = self.rs.irrep_character(hw, depth=20)
            self.assertEqual(char_dim(ch), d, f"B3 V{hw}")

    def test_formula_matches_character_hw_sum_2(self):
        """Dimension formula = character for |hw| = 2."""
        for hw in [(2, 0, 0), (0, 2, 0), (0, 0, 2),
                   (1, 1, 0), (1, 0, 1), (0, 1, 1)]:
            df = B3_dim(*hw)
            ch = self.rs.irrep_character(hw, depth=20)
            dc = char_dim(ch)
            self.assertEqual(dc, df, f"B3 V{hw}: char={dc} formula={df}")

    def test_known_dims_hw_sum_2(self):
        """Known dimensions for B_3 at |hw| = 2."""
        self.assertEqual(B3_dim(2, 0, 0), 27)
        self.assertEqual(B3_dim(0, 2, 0), 168)
        self.assertEqual(B3_dim(0, 0, 2), 35)
        self.assertEqual(B3_dim(1, 1, 0), 105)
        self.assertEqual(B3_dim(1, 0, 1), 48)
        self.assertEqual(B3_dim(0, 1, 1), 112)


# ===================================================================
# C_3 dimensions
# ===================================================================

class TestC3Dimensions(unittest.TestCase):
    """Weyl dimension formula vs character computation for C_3."""

    def setUp(self):
        self.rs = C3()

    def test_standard_rep(self):
        """V(omega_1) = 6-dim standard of sp_6."""
        self.assertEqual(C3_dim(1, 0, 0), 6)
        ch = self.rs.irrep_character((1, 0, 0), depth=15)
        self.assertEqual(char_dim(ch), 6)

    def test_omega2_rep(self):
        """V(omega_2) = 14-dim for sp_6."""
        self.assertEqual(C3_dim(0, 1, 0), 14)
        ch = self.rs.irrep_character((0, 1, 0), depth=15)
        self.assertEqual(char_dim(ch), 14)

    def test_omega3_rep(self):
        """V(omega_3) = 14'-dim for sp_6."""
        self.assertEqual(C3_dim(0, 0, 1), 14)
        ch = self.rs.irrep_character((0, 0, 1), depth=15)
        self.assertEqual(char_dim(ch), 14)

    def test_formula_matches_character_fundamentals(self):
        """Dimension formula = character for all fundamentals."""
        for hw, d in [((1, 0, 0), 6), ((0, 1, 0), 14), ((0, 0, 1), 14)]:
            self.assertEqual(C3_dim(*hw), d)
            ch = self.rs.irrep_character(hw, depth=20)
            self.assertEqual(char_dim(ch), d, f"C3 V{hw}")

    def test_formula_matches_character_hw_sum_2(self):
        """Dimension formula = character for |hw| = 2."""
        for hw in [(2, 0, 0), (0, 2, 0), (0, 0, 2),
                   (1, 1, 0), (1, 0, 1), (0, 1, 1)]:
            df = C3_dim(*hw)
            ch = self.rs.irrep_character(hw, depth=20)
            dc = char_dim(ch)
            self.assertEqual(dc, df, f"C3 V{hw}: char={dc} formula={df}")

    def test_known_dims_hw_sum_2(self):
        """Known dimensions for C_3 at |hw| = 2."""
        self.assertEqual(C3_dim(2, 0, 0), 21)
        self.assertEqual(C3_dim(0, 2, 0), 90)
        self.assertEqual(C3_dim(0, 0, 2), 84)
        self.assertEqual(C3_dim(1, 1, 0), 64)
        self.assertEqual(C3_dim(1, 0, 1), 70)
        self.assertEqual(C3_dim(0, 1, 1), 126)


# ===================================================================
# B_3 prefundamental characters
# ===================================================================

class TestB3Prefundamental(unittest.TestCase):
    """Prefundamental character properties for B_3."""

    def setUp(self):
        self.rs = B3()

    def test_all_hw_mult_one(self):
        """All L^-_i have highest weight (0,0,0) with multiplicity 1."""
        for node in range(3):
            ch = self.rs.prefundamental_character(node, depth=6)
            self.assertEqual(ch.get((0, 0, 0), 0), 1,
                             f"L^-_{node + 1} hw mult != 1")

    def test_all_multiplicities_positive(self):
        """All weight multiplicities are positive."""
        for node in range(3):
            ch = self.rs.prefundamental_character(node, depth=5)
            for w, m in ch.items():
                self.assertGreater(m, 0,
                                   f"B3 L^-_{node + 1}: negative mult at {w}")

    def test_L1_has_multiple_weights(self):
        """L^-_1 has nontrivial character (more than just hw)."""
        ch = self.rs.prefundamental_character(0, depth=6)
        self.assertGreater(len(ch), 1)

    def test_depth1_mult_node0(self):
        """Depth-1 weight -alpha_1 of L^-_1 has multiplicity 1.

        Only the factor 1/(1 - e^{-alpha_1}) at n=1 contributes to
        weight -alpha_1; other relevant roots shift to different positions.
        """
        m = self.rs.prefundamental_depth1_mult(0, depth=8)
        self.assertEqual(m, 1)

    def test_depth1_mult_node1(self):
        """Depth-1 weight -alpha_2 of L^-_2 has multiplicity 1."""
        m = self.rs.prefundamental_depth1_mult(1, depth=8)
        self.assertEqual(m, 1)

    def test_depth1_mult_node2(self):
        """Depth-1 weight -alpha_3 of L^-_3 has multiplicity 1."""
        m = self.rs.prefundamental_depth1_mult(2, depth=8)
        self.assertEqual(m, 1)


# ===================================================================
# C_3 prefundamental characters
# ===================================================================

class TestC3Prefundamental(unittest.TestCase):
    """Prefundamental character properties for C_3."""

    def setUp(self):
        self.rs = C3()

    def test_all_hw_mult_one(self):
        """All L^-_i have highest weight (0,0,0) with multiplicity 1."""
        for node in range(3):
            ch = self.rs.prefundamental_character(node, depth=6)
            self.assertEqual(ch.get((0, 0, 0), 0), 1)

    def test_all_multiplicities_positive(self):
        """All weight multiplicities are positive."""
        for node in range(3):
            ch = self.rs.prefundamental_character(node, depth=5)
            for w, m in ch.items():
                self.assertGreater(m, 0,
                                   f"C3 L^-_{node + 1}: negative mult at {w}")

    def test_depth1_mult_node0(self):
        """Depth-1 weight -alpha_1 of L^-_1 has multiplicity 1."""
        m = self.rs.prefundamental_depth1_mult(0, depth=8)
        self.assertEqual(m, 1)

    def test_depth1_mult_node2(self):
        """Depth-1 weight -alpha_3 of L^-_3 has multiplicity 1."""
        m = self.rs.prefundamental_depth1_mult(2, depth=8)
        self.assertEqual(m, 1)


# ===================================================================
# B_3 CG closure
# ===================================================================

class TestB3CG(unittest.TestCase):
    """CG decomposition verification for B_3 = so_7."""

    def setUp(self):
        self.rs = B3()

    def test_cg_vector_node1(self):
        """V(omega_1) (7-dim) x L^-_1."""
        res = verify_cg3(self.rs, (1, 0, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_vector_node2(self):
        """V(omega_1) (7-dim) x L^-_2."""
        res = verify_cg3(self.rs, (1, 0, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_vector_node3(self):
        """V(omega_1) (7-dim) x L^-_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_adjoint_node1(self):
        """V(omega_2) (21-dim) x L^-_1."""
        res = verify_cg3(self.rs, (0, 1, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_adjoint_node2(self):
        """V(omega_2) (21-dim) x L^-_2."""
        res = verify_cg3(self.rs, (0, 1, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_adjoint_node3(self):
        """V(omega_2) (21-dim) x L^-_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_spin_node1(self):
        """V(omega_3) (8-dim spin) x L^-_1."""
        res = verify_cg3(self.rs, (0, 0, 1), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_spin_node2(self):
        """V(omega_3) (8-dim spin) x L^-_2."""
        res = verify_cg3(self.rs, (0, 0, 1), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_spin_node3(self):
        """V(omega_3) (8-dim spin) x L^-_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_batch_fundamentals(self):
        """All fundamental reps pass CG for all three nodes (9 cases)."""
        batch = verify_batch3(self.rs, max_hw_sum=1, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"B3 CG batch failed: {batch['n_fail']} failures")
        self.assertEqual(batch["n_pass"], 9)

    def test_cg_2omega1_all_nodes(self):
        """V(2*omega_1) (27-dim) x L^-_i for all i."""
        for node in range(3):
            res = verify_cg3(self.rs, (2, 0, 0), node, depth=6)
            self.assertTrue(res["match"],
                            f"CG failed for 2w1 node {node}: {res['mismatches']}")

    def test_cg_omega1_omega2(self):
        """V(omega_1 + omega_2) (105-dim) x L^-_1."""
        res = verify_cg3(self.rs, (1, 1, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")


# ===================================================================
# C_3 CG closure
# ===================================================================

class TestC3CG(unittest.TestCase):
    """CG decomposition verification for C_3 = sp_6."""

    def setUp(self):
        self.rs = C3()

    def test_cg_standard_node1(self):
        """V(omega_1) (6-dim) x L^-_1."""
        res = verify_cg3(self.rs, (1, 0, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_standard_node2(self):
        """V(omega_1) (6-dim) x L^-_2."""
        res = verify_cg3(self.rs, (1, 0, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_standard_node3(self):
        """V(omega_1) (6-dim) x L^-_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega2_node1(self):
        """V(omega_2) (14-dim) x L^-_1."""
        res = verify_cg3(self.rs, (0, 1, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega2_node2(self):
        """V(omega_2) (14-dim) x L^-_2."""
        res = verify_cg3(self.rs, (0, 1, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega2_node3(self):
        """V(omega_2) (14-dim) x L^-_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega3_node1(self):
        """V(omega_3) (14'-dim) x L^-_1."""
        res = verify_cg3(self.rs, (0, 0, 1), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega3_node2(self):
        """V(omega_3) (14'-dim) x L^-_2."""
        res = verify_cg3(self.rs, (0, 0, 1), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega3_node3(self):
        """V(omega_3) (14'-dim) x L^-_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_batch_fundamentals(self):
        """All fundamental reps pass CG for all three nodes (9 cases)."""
        batch = verify_batch3(self.rs, max_hw_sum=1, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"C3 CG batch failed: {batch['n_fail']} failures")
        self.assertEqual(batch["n_pass"], 9)

    def test_cg_2omega1_all_nodes(self):
        """V(2*omega_1) (21-dim) x L^-_i for all i."""
        for node in range(3):
            res = verify_cg3(self.rs, (2, 0, 0), node, depth=6)
            self.assertTrue(res["match"],
                            f"CG failed for 2w1 node {node}: {res['mismatches']}")

    def test_cg_omega1_omega2(self):
        """V(omega_1 + omega_2) (64-dim) x L^-_1."""
        res = verify_cg3(self.rs, (1, 1, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")


# ===================================================================
# B_3 Verma containment
# ===================================================================

class TestB3VermaContainment(unittest.TestCase):
    """Verify ch(M(lambda)) <= ch(V_lambda tensor prod_i L^-_i) for B_3."""

    def setUp(self):
        self.rs = B3()

    def test_verma_vector(self):
        """Verma M(omega_1) contained in V(omega_1) x prod L^-_i."""
        res = verify_verma_containment3(self.rs, (1, 0, 0), depth=5)
        self.assertTrue(res["contained"], f"Violations: {res['violations']}")

    def test_verma_adjoint(self):
        """Verma M(omega_2) contained."""
        res = verify_verma_containment3(self.rs, (0, 1, 0), depth=5)
        self.assertTrue(res["contained"], f"Violations: {res['violations']}")

    def test_verma_spin(self):
        """Verma M(omega_3) contained."""
        res = verify_verma_containment3(self.rs, (0, 0, 1), depth=5)
        self.assertTrue(res["contained"], f"Violations: {res['violations']}")


# ===================================================================
# C_3 Verma containment
# ===================================================================

class TestC3VermaContainment(unittest.TestCase):
    """Verify ch(M(lambda)) <= ch(V_lambda tensor prod_i L^-_i) for C_3."""

    def setUp(self):
        self.rs = C3()

    def test_verma_standard(self):
        res = verify_verma_containment3(self.rs, (1, 0, 0), depth=5)
        self.assertTrue(res["contained"], f"Violations: {res['violations']}")

    def test_verma_omega2(self):
        res = verify_verma_containment3(self.rs, (0, 1, 0), depth=5)
        self.assertTrue(res["contained"], f"Violations: {res['violations']}")

    def test_verma_omega3(self):
        res = verify_verma_containment3(self.rs, (0, 0, 1), depth=5)
        self.assertTrue(res["contained"], f"Violations: {res['violations']}")


# ===================================================================
# A_3 = sl_4 cross-check (simply-laced control)
# ===================================================================

class TestA3RootSystem(unittest.TestCase):
    """Root system structure for A_3 = sl_4."""

    def setUp(self):
        self.rs = A3()

    def test_positive_root_count(self):
        """A_3 has 6 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 6)

    def test_positive_roots_alpha(self):
        """Positive roots: 3 simple + alpha12 + alpha23 + alpha123."""
        expected = {
            (1, 0, 0), (0, 1, 0), (0, 0, 1),
            (1, 1, 0), (0, 1, 1), (1, 1, 1),
        }
        self.assertEqual(set(self.rs.positive_roots_alpha), expected)

    def test_weyl_group_order(self):
        """Weyl group of A_3 has order 24 = 4!."""
        self.assertEqual(len(self.rs.weyl_group), 24)


class TestA3Dimensions(unittest.TestCase):
    """Dimensions for A_3 = sl_4."""

    def setUp(self):
        self.rs = A3()

    def test_standard_rep(self):
        """V(omega_1) = 4-dim."""
        self.assertEqual(A3_dim(1, 0, 0), 4)
        ch = self.rs.irrep_character((1, 0, 0), depth=10)
        self.assertEqual(char_dim(ch), 4)

    def test_wedge2_rep(self):
        """V(omega_2) = 6-dim (Lambda^2 of standard)."""
        self.assertEqual(A3_dim(0, 1, 0), 6)
        ch = self.rs.irrep_character((0, 1, 0), depth=10)
        self.assertEqual(char_dim(ch), 6)

    def test_dual_standard_rep(self):
        """V(omega_3) = 4-dim (dual standard)."""
        self.assertEqual(A3_dim(0, 0, 1), 4)
        ch = self.rs.irrep_character((0, 0, 1), depth=10)
        self.assertEqual(char_dim(ch), 4)

    def test_adjoint_rep(self):
        """V(omega_1 + omega_3) = 15-dim (adjoint of sl_4)."""
        self.assertEqual(A3_dim(1, 0, 1), 15)
        ch = self.rs.irrep_character((1, 0, 1), depth=10)
        self.assertEqual(char_dim(ch), 15)


class TestA3CG(unittest.TestCase):
    """CG verification for A_3 (cross-check vs type A module)."""

    def setUp(self):
        self.rs = A3()

    def test_cg_batch_fundamentals(self):
        """CG holds for all fundamental weights x all nodes."""
        batch = verify_batch3(self.rs, max_hw_sum=1, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"A3 CG batch failed: {batch['n_fail']} failures")

    def test_cg_adjoint_all_nodes(self):
        """V(omega_1 + omega_3) (adjoint, 15-dim) x L^-_i."""
        for node in range(3):
            res = verify_cg3(self.rs, (1, 0, 1), node, depth=6)
            self.assertTrue(res["match"],
                            f"A3 adjoint node {node}: {res['mismatches']}")


# ===================================================================
# Universal CG structure tests
# ===================================================================

class TestUniversalCGStructure(unittest.TestCase):
    """The CG multiplicities ARE the weight multiplicities.

    This is a consequence of the distributive law (finite sum x power series).
    Verified explicitly for B_3, C_3.
    """

    def test_b3_vector_all_nodes(self):
        """B_3 vector rep: CG = weight-multiplicity formula."""
        rs = B3()
        hw = (1, 0, 0)
        V = rs.irrep_character(hw, depth=15)
        for node in range(3):
            L = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product3(V, L)
            rhs = {}
            for mu, mult in V.items():
                for w, m in shift_char3(L, mu).items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char3(lhs, rhs)
            reliable = {w: m for w, m in diff.items()
                        if sum(abs(w[k]) for k in range(3)) < 6}
            self.assertEqual(len(reliable), 0,
                             f"B3 V(1,0,0) x L^-_{node + 1}: diff at {reliable}")

    def test_c3_standard_all_nodes(self):
        """C_3 standard rep: CG = weight-multiplicity formula."""
        rs = C3()
        hw = (1, 0, 0)
        V = rs.irrep_character(hw, depth=15)
        for node in range(3):
            L = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product3(V, L)
            rhs = {}
            for mu, mult in V.items():
                for w, m in shift_char3(L, mu).items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char3(lhs, rhs)
            reliable = {w: m for w, m in diff.items()
                        if sum(abs(w[k]) for k in range(3)) < 6}
            self.assertEqual(len(reliable), 0,
                             f"C3 V(1,0,0) x L^-_{node + 1}: diff at {reliable}")

    def test_b3_spin_all_nodes(self):
        """B_3 spin rep: CG = weight-multiplicity formula."""
        rs = B3()
        hw = (0, 0, 1)
        V = rs.irrep_character(hw, depth=15)
        for node in range(3):
            L = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product3(V, L)
            rhs = {}
            for mu, mult in V.items():
                for w, m in shift_char3(L, mu).items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char3(lhs, rhs)
            reliable = {w: m for w, m in diff.items()
                        if sum(abs(w[k]) for k in range(3)) < 6}
            self.assertEqual(len(reliable), 0,
                             f"B3 spin x L^-_{node + 1}: diff at {reliable}")

    def test_c3_omega3_all_nodes(self):
        """C_3 omega_3 rep: CG = weight-multiplicity formula."""
        rs = C3()
        hw = (0, 0, 1)
        V = rs.irrep_character(hw, depth=15)
        for node in range(3):
            L = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product3(V, L)
            rhs = {}
            for mu, mult in V.items():
                for w, m in shift_char3(L, mu).items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char3(lhs, rhs)
            reliable = {w: m for w, m in diff.items()
                        if sum(abs(w[k]) for k in range(3)) < 6}
            self.assertEqual(len(reliable), 0,
                             f"C3 omega3 x L^-_{node + 1}: diff at {reliable}")


# ===================================================================
# Character algebra sanity
# ===================================================================

class TestCharacterAlgebra(unittest.TestCase):
    """Basic character algebra operations."""

    def test_tensor_identity(self):
        """Tensoring with trivial = identity."""
        rs = B3()
        triv = {(0, 0, 0): 1}
        ch = rs.irrep_character((1, 0, 0), depth=10)
        product = tensor_product3(triv, ch)
        self.assertEqual(product, ch)

    def test_shift_inverse(self):
        """Shift by s then by -s is identity."""
        ch = {(1, 2, 3): 5, (0, 0, 0): 1}
        s = (1, -1, 2)
        shifted = shift_char3(shift_char3(ch, s), (-s[0], -s[1], -s[2]))
        self.assertEqual(shifted, ch)

    def test_subtract_self_is_zero(self):
        """ch - ch = empty."""
        ch = {(1, 2, 3): 5, (0, 0, 0): 1}
        self.assertEqual(subtract_char3(ch, ch), {})


# ===================================================================
# Coordinate conversion
# ===================================================================

class TestCoordinateConversion(unittest.TestCase):
    """Omega <-> alpha basis conversion."""

    def test_simple_root_roundtrip_b3(self):
        """Simple roots survive omega -> alpha -> omega roundtrip."""
        rs = B3()
        for i in range(3):
            c = [0, 0, 0]
            c[i] = 1
            c = tuple(c)
            w = rs.alpha_to_omega(c)
            self.assertEqual(w, rs.alpha[i])
            c_back = rs.omega_to_alpha(w)
            self.assertEqual(c_back, c)

    def test_simple_root_roundtrip_c3(self):
        """Simple roots survive omega -> alpha -> omega roundtrip for C_3."""
        rs = C3()
        for i in range(3):
            c = [0, 0, 0]
            c[i] = 1
            c = tuple(c)
            w = rs.alpha_to_omega(c)
            self.assertEqual(w, rs.alpha[i])
            c_back = rs.omega_to_alpha(w)
            self.assertEqual(c_back, c)

    def test_positive_root_roundtrip(self):
        """All positive roots survive alpha -> omega -> alpha roundtrip."""
        for constructor in [B3, C3, A3]:
            rs = constructor()
            for c in rs.positive_roots_alpha:
                w = rs.alpha_to_omega(c)
                c_back = rs.omega_to_alpha(w)
                self.assertEqual(c_back, c,
                                 f"{rs.name}: roundtrip failed for {c}")


# ===================================================================
# Weyl group properties
# ===================================================================

class TestWeylGroupProperties(unittest.TestCase):
    """Structural properties of the Weyl group."""

    def test_identity_present(self):
        """Identity matrix is in Weyl group with det = 1."""
        for constructor in [B3, C3, A3]:
            rs = constructor()
            has_identity = any(
                m == ((1, 0, 0), (0, 1, 0), (0, 0, 1))
                for _, m in rs.weyl_group
            )
            self.assertTrue(has_identity, f"{rs.name}: no identity")

    def test_det_pm1(self):
        """All Weyl group elements have det = +/- 1."""
        for constructor in [B3, C3, A3]:
            rs = constructor()
            for d, _ in rs.weyl_group:
                self.assertIn(d, [1, -1], f"{rs.name}: det = {d}")

    def test_even_odd_split(self):
        """Equal numbers of even and odd elements."""
        for constructor in [B3, C3, A3]:
            rs = constructor()
            n_even = sum(1 for d, _ in rs.weyl_group if d == 1)
            n_odd = sum(1 for d, _ in rs.weyl_group if d == -1)
            self.assertEqual(n_even, n_odd,
                             f"{rs.name}: even={n_even} odd={n_odd}")


# ===================================================================
# Kostant partition function
# ===================================================================

class TestKostantPartition(unittest.TestCase):
    """Kostant partition function spot checks."""

    def test_zero_gives_one(self):
        """K(0) = 1 for all types."""
        for constructor in [B3, C3, A3]:
            rs = constructor()
            self.assertEqual(rs._kostant_partition((0, 0, 0)), 1)

    def test_simple_root_gives_one(self):
        """K(alpha_i) = 1 for each simple root."""
        for constructor in [B3, C3, A3]:
            rs = constructor()
            for i in range(3):
                c = [0, 0, 0]
                c[i] = 1
                self.assertEqual(rs._kostant_partition(tuple(c)), 1,
                                 f"{rs.name}: K(e_{i}) != 1")

    def test_negative_gives_zero(self):
        """K(c) = 0 if any coefficient is negative."""
        rs = B3()
        self.assertEqual(rs._kostant_partition((-1, 0, 0)), 0)
        self.assertEqual(rs._kostant_partition((0, -1, 0)), 0)


if __name__ == "__main__":
    unittest.main()
