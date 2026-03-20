"""Tests for prefundamental CG decomposition for types B_3 and C_3.

Verifies the FRONTIER computation extending MC3 (conj:mc3-arbitrary-type)
to rank-3 non-simply-laced types. The universal CG theorem

    [V_lambda] * [L^-_i] = sum_{mu in wt(V_lambda)} mult(mu) * [L^-_i(shift=mu)]

is a formal identity (distributive law of finite sum times power series).
This module provides computational verification for:

  - B_3 = so_7 (rank 3, non-simply-laced, alpha_3 short)
  - C_3 = sp_6 (rank 3, non-simply-laced, Langlands dual to B_3)
  - A_3 = sl_4 (cross-check, simply-laced)

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
    check_langlands_duality,
    verify_verma_containment3,
)


# ===================================================================
# Root system structure
# ===================================================================

class TestB3RootSystem(unittest.TestCase):
    """Root system data for B_3 = so_7."""

    def setUp(self):
        self.rs = B3()

    def test_positive_root_count(self):
        """B_3 has 9 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 9)

    def test_positive_roots_alpha(self):
        """Positive roots in alpha coordinates for B_3.

        The 9 positive roots of B_3 (alpha_3 short):
          alpha_1, alpha_2, alpha_3,
          alpha_1+alpha_2, alpha_2+alpha_3, alpha_2+2*alpha_3,
          alpha_1+alpha_2+alpha_3, alpha_1+alpha_2+2*alpha_3,
          alpha_1+2*alpha_2+2*alpha_3
        """
        expected = {
            (1,0,0), (0,1,0), (0,0,1),
            (1,1,0), (0,1,1), (0,1,2),
            (1,1,1), (1,1,2), (1,2,2),
        }
        self.assertEqual(set(self.rs.positive_roots_alpha), expected)

    def test_weyl_group_order(self):
        """Weyl group of B_3 has order 48 = 2^3 * 3!."""
        self.assertEqual(len(self.rs.weyl_group), 48)

    def test_roots_containing_alpha1(self):
        """Roots containing alpha_1 in B_3."""
        indices = self.rs.roots_containing[0]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(1,0,0), (1,1,0), (1,1,1), (1,1,2), (1,2,2)}
        self.assertEqual(roots, expected)

    def test_roots_containing_alpha2(self):
        """Roots containing alpha_2 in B_3."""
        indices = self.rs.roots_containing[1]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(0,1,0), (1,1,0), (0,1,1), (0,1,2),
                    (1,1,1), (1,1,2), (1,2,2)}
        self.assertEqual(roots, expected)

    def test_roots_containing_alpha3(self):
        """Roots containing alpha_3 (short root) in B_3."""
        indices = self.rs.roots_containing[2]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(0,0,1), (0,1,1), (0,1,2),
                    (1,1,1), (1,1,2), (1,2,2)}
        self.assertEqual(roots, expected)


class TestC3RootSystem(unittest.TestCase):
    """Root system data for C_3 = sp_6."""

    def setUp(self):
        self.rs = C3()

    def test_positive_root_count(self):
        """C_3 has 9 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 9)

    def test_positive_roots_alpha(self):
        """Positive roots in alpha coordinates for C_3.

        The 9 positive roots of C_3 (alpha_3 long, alpha_1 short):
          alpha_1, alpha_2, alpha_3,
          alpha_1+alpha_2, alpha_2+alpha_3, 2*alpha_2+alpha_3,
          alpha_1+alpha_2+alpha_3, alpha_1+2*alpha_2+alpha_3,
          2*alpha_1+2*alpha_2+alpha_3
        """
        expected = {
            (1,0,0), (0,1,0), (0,0,1),
            (1,1,0), (0,1,1), (0,2,1),
            (1,1,1), (1,2,1), (2,2,1),
        }
        self.assertEqual(set(self.rs.positive_roots_alpha), expected)

    def test_weyl_group_order(self):
        """Weyl group of C_3 has order 48 = 2^3 * 3!."""
        self.assertEqual(len(self.rs.weyl_group), 48)

    def test_roots_containing_alpha1(self):
        """Roots containing alpha_1 in C_3."""
        indices = self.rs.roots_containing[0]
        roots = {self.rs.positive_roots_alpha[i] for i in indices}
        expected = {(1,0,0), (1,1,0), (1,1,1), (1,2,1), (2,2,1)}
        self.assertEqual(roots, expected)


class TestLanglandsDuality(unittest.TestCase):
    """B_3 and C_3 are Langlands dual."""

    def test_cartan_transpose(self):
        """Cartan matrices of B_3 and C_3 are transposes."""
        self.assertTrue(check_langlands_duality())

    def test_same_root_count(self):
        """Langlands dual pairs have the same number of positive roots."""
        b3 = B3()
        c3 = C3()
        self.assertEqual(len(b3.positive_roots), len(c3.positive_roots))

    def test_same_weyl_group_order(self):
        """Langlands dual pairs have the same Weyl group order."""
        b3 = B3()
        c3 = C3()
        self.assertEqual(len(b3.weyl_group), len(c3.weyl_group))


# ===================================================================
# Dimension formulas
# ===================================================================

class TestB3Dimensions(unittest.TestCase):
    """Weyl dimension formula for B_3 = so_7."""

    def setUp(self):
        self.rs = B3()

    def test_vector_rep(self):
        """V(omega_1) = 7-dim vector representation of so_7."""
        self.assertEqual(B3_dim(1, 0, 0), 7)
        char = self.rs.irrep_character((1, 0, 0), depth=15)
        self.assertEqual(sum(char.values()), 7)

    def test_omega2_rep(self):
        """V(omega_2) = 21-dim (adjoint) for so_7."""
        self.assertEqual(B3_dim(0, 1, 0), 21)
        char = self.rs.irrep_character((0, 1, 0), depth=15)
        self.assertEqual(sum(char.values()), 21)

    def test_spin_rep(self):
        """V(omega_3) = 8-dim spin representation of so_7."""
        self.assertEqual(B3_dim(0, 0, 1), 8)
        char = self.rs.irrep_character((0, 0, 1), depth=15)
        self.assertEqual(sum(char.values()), 8)

    def test_formula_matches_character_fundamentals(self):
        """Dimension formula matches character for all fundamental reps."""
        for hw, expected_dim in [((1,0,0), 7), ((0,1,0), 21), ((0,0,1), 8)]:
            dim_f = B3_dim(*hw)
            char = self.rs.irrep_character(hw, depth=20)
            dim_c = sum(char.values())
            self.assertEqual(dim_f, expected_dim,
                             f"B3 formula wrong for {hw}")
            self.assertEqual(dim_c, expected_dim,
                             f"B3 character wrong for {hw}")

    def test_formula_matches_character_hw_sum_2(self):
        """Dimension formula matches character for |hw| = 2."""
        for hw in [(2,0,0), (0,2,0), (0,0,2), (1,1,0), (1,0,1), (0,1,1)]:
            dim_f = B3_dim(*hw)
            char = self.rs.irrep_character(hw, depth=20)
            dim_c = sum(char.values())
            self.assertEqual(dim_c, dim_f,
                             f"B3 dim mismatch for V{hw}: char={dim_c}, formula={dim_f}")


class TestC3Dimensions(unittest.TestCase):
    """Weyl dimension formula for C_3 = sp_6."""

    def setUp(self):
        self.rs = C3()

    def test_standard_rep(self):
        """V(omega_1) = 6-dim standard representation of sp_6."""
        self.assertEqual(C3_dim(1, 0, 0), 6)
        char = self.rs.irrep_character((1, 0, 0), depth=15)
        self.assertEqual(sum(char.values()), 6)

    def test_omega2_rep(self):
        """V(omega_2) = 14-dim for sp_6 (Lambda^2 standard, traceless)."""
        self.assertEqual(C3_dim(0, 1, 0), 14)
        char = self.rs.irrep_character((0, 1, 0), depth=15)
        self.assertEqual(sum(char.values()), 14)

    def test_omega3_rep(self):
        """V(omega_3) = 14'-dim for sp_6 (Lambda^3 standard)."""
        self.assertEqual(C3_dim(0, 0, 1), 14)
        char = self.rs.irrep_character((0, 0, 1), depth=15)
        self.assertEqual(sum(char.values()), 14)

    def test_formula_matches_character_fundamentals(self):
        """Dimension formula matches character for all fundamental reps."""
        for hw, expected_dim in [((1,0,0), 6), ((0,1,0), 14), ((0,0,1), 14)]:
            dim_f = C3_dim(*hw)
            char = self.rs.irrep_character(hw, depth=20)
            dim_c = sum(char.values())
            self.assertEqual(dim_f, expected_dim,
                             f"C3 formula wrong for {hw}")
            self.assertEqual(dim_c, expected_dim,
                             f"C3 character wrong for {hw}")

    def test_formula_matches_character_hw_sum_2(self):
        """Dimension formula matches character for |hw| = 2."""
        for hw in [(2,0,0), (0,2,0), (0,0,2), (1,1,0), (1,0,1), (0,1,1)]:
            dim_f = C3_dim(*hw)
            char = self.rs.irrep_character(hw, depth=20)
            dim_c = sum(char.values())
            self.assertEqual(dim_c, dim_f,
                             f"C3 dim mismatch for V{hw}: char={dim_c}, formula={dim_f}")


# ===================================================================
# Prefundamental characters
# ===================================================================

class TestB3Prefundamental(unittest.TestCase):
    """Prefundamental character properties for B_3."""

    def setUp(self):
        self.rs = B3()

    def test_L1_hw_mult_one(self):
        """L^-_1 has highest weight (0,0,0) with multiplicity 1."""
        char = self.rs.prefundamental_character(0, depth=6)
        self.assertEqual(char.get((0, 0, 0), 0), 1)

    def test_L2_hw_mult_one(self):
        """L^-_2 has highest weight (0,0,0) with multiplicity 1."""
        char = self.rs.prefundamental_character(1, depth=6)
        self.assertEqual(char.get((0, 0, 0), 0), 1)

    def test_L3_hw_mult_one(self):
        """L^-_3 has highest weight (0,0,0) with multiplicity 1."""
        char = self.rs.prefundamental_character(2, depth=6)
        self.assertEqual(char.get((0, 0, 0), 0), 1)

    def test_all_multiplicities_positive(self):
        """All weight multiplicities of L^-_i are positive."""
        for node in range(3):
            char = self.rs.prefundamental_character(node, depth=5)
            for w, m in char.items():
                self.assertGreater(m, 0,
                                   f"B3 L^-_{node+1}: negative mult at {w}")


class TestC3Prefundamental(unittest.TestCase):
    """Prefundamental character properties for C_3."""

    def setUp(self):
        self.rs = C3()

    def test_L1_hw_mult_one(self):
        """L^-_1 has highest weight (0,0,0) with multiplicity 1."""
        char = self.rs.prefundamental_character(0, depth=6)
        self.assertEqual(char.get((0, 0, 0), 0), 1)

    def test_L2_hw_mult_one(self):
        """L^-_2 has highest weight (0,0,0) with multiplicity 1."""
        char = self.rs.prefundamental_character(1, depth=6)
        self.assertEqual(char.get((0, 0, 0), 0), 1)

    def test_L3_hw_mult_one(self):
        """L^-_3 has highest weight (0,0,0) with multiplicity 1."""
        char = self.rs.prefundamental_character(2, depth=6)
        self.assertEqual(char.get((0, 0, 0), 0), 1)

    def test_all_multiplicities_positive(self):
        """All weight multiplicities of L^-_i are positive."""
        for node in range(3):
            char = self.rs.prefundamental_character(node, depth=5)
            for w, m in char.items():
                self.assertGreater(m, 0,
                                   f"C3 L^-_{node+1}: negative mult at {w}")


# ===================================================================
# CG closure
# ===================================================================

class TestB3CG(unittest.TestCase):
    """CG decomposition verification for B_3 = so_7."""

    def setUp(self):
        self.rs = B3()

    def test_cg_vector_node1(self):
        """V(omega_1) (7-dim vector) x L^-_1 in B_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_vector_node2(self):
        """V(omega_1) (7-dim vector) x L^-_2 in B_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_vector_node3(self):
        """V(omega_1) (7-dim vector) x L^-_3 in B_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_adjoint_node1(self):
        """V(omega_2) (21-dim) x L^-_1 in B_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_adjoint_node2(self):
        """V(omega_2) (21-dim) x L^-_2 in B_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_adjoint_node3(self):
        """V(omega_2) (21-dim) x L^-_3 in B_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_spin_node1(self):
        """V(omega_3) (8-dim spin) x L^-_1 in B_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_spin_node2(self):
        """V(omega_3) (8-dim spin) x L^-_2 in B_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_spin_node3(self):
        """V(omega_3) (8-dim spin) x L^-_3 in B_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_batch_fundamentals(self):
        """All fundamental reps pass CG for all three nodes."""
        batch = verify_batch3(self.rs, max_hw_sum=1, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"B3 CG batch failed: {batch['n_fail']} failures")
        # 3 fundamental weights x 3 nodes = 9
        self.assertEqual(batch["n_pass"], 9)


class TestC3CG(unittest.TestCase):
    """CG decomposition verification for C_3 = sp_6."""

    def setUp(self):
        self.rs = C3()

    def test_cg_standard_node1(self):
        """V(omega_1) (6-dim standard) x L^-_1 in C_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_standard_node2(self):
        """V(omega_1) (6-dim standard) x L^-_2 in C_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_standard_node3(self):
        """V(omega_1) (6-dim standard) x L^-_3 in C_3."""
        res = verify_cg3(self.rs, (1, 0, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega2_node1(self):
        """V(omega_2) (14-dim) x L^-_1 in C_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega2_node2(self):
        """V(omega_2) (14-dim) x L^-_2 in C_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega2_node3(self):
        """V(omega_2) (14-dim) x L^-_3 in C_3."""
        res = verify_cg3(self.rs, (0, 1, 0), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega3_node1(self):
        """V(omega_3) (14'-dim) x L^-_1 in C_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 0, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega3_node2(self):
        """V(omega_3) (14'-dim) x L^-_2 in C_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 1, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_omega3_node3(self):
        """V(omega_3) (14'-dim) x L^-_3 in C_3."""
        res = verify_cg3(self.rs, (0, 0, 1), 2, depth=6)
        self.assertTrue(res["match"], f"CG failed: {res['mismatches']}")

    def test_cg_batch_fundamentals(self):
        """All fundamental reps pass CG for all three nodes."""
        batch = verify_batch3(self.rs, max_hw_sum=1, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"C3 CG batch failed: {batch['n_fail']} failures")
        self.assertEqual(batch["n_pass"], 9)


# ===================================================================
# K_0 generation: Verma containment
# ===================================================================

class TestB3VermaContainment(unittest.TestCase):
    """Verify ch(M(lambda)) <= ch(V_lambda tensor prod_i L^-_i) for B_3.

    In rank 3, K_0-generation requires the product of ALL three
    prefundamental modules (not just one as in rank 1).
    """

    def setUp(self):
        self.rs = B3()

    def test_verma_vector(self):
        """Verma M(omega_1) contained in V(omega_1) tensor prod L^-_i."""
        res = verify_verma_containment3(self.rs, (1, 0, 0), depth=5)
        self.assertTrue(res["contained"],
                        f"Verma not contained: {res['violations']}")

    def test_verma_spin(self):
        """Verma M(omega_3) contained in V(omega_3) tensor prod L^-_i."""
        res = verify_verma_containment3(self.rs, (0, 0, 1), depth=5)
        self.assertTrue(res["contained"],
                        f"Verma not contained: {res['violations']}")

    def test_verma_adjoint(self):
        """Verma M(omega_2) contained in V(omega_2) tensor prod L^-_i."""
        res = verify_verma_containment3(self.rs, (0, 1, 0), depth=5)
        self.assertTrue(res["contained"],
                        f"Verma not contained: {res['violations']}")


class TestC3VermaContainment(unittest.TestCase):
    """Verify ch(M(lambda)) <= ch(V_lambda tensor prod_i L^-_i) for C_3."""

    def setUp(self):
        self.rs = C3()

    def test_verma_standard(self):
        """Verma M(omega_1) contained in V(omega_1) tensor prod L^-_i."""
        res = verify_verma_containment3(self.rs, (1, 0, 0), depth=5)
        self.assertTrue(res["contained"],
                        f"Verma not contained: {res['violations']}")

    def test_verma_omega2(self):
        """Verma M(omega_2) contained in V(omega_2) tensor prod L^-_i."""
        res = verify_verma_containment3(self.rs, (0, 1, 0), depth=5)
        self.assertTrue(res["contained"],
                        f"Verma not contained: {res['violations']}")

    def test_verma_omega3(self):
        """Verma M(omega_3) contained in V(omega_3) tensor prod L^-_i."""
        res = verify_verma_containment3(self.rs, (0, 0, 1), depth=5)
        self.assertTrue(res["contained"],
                        f"Verma not contained: {res['violations']}")


# ===================================================================
# A_3 cross-check
# ===================================================================

class TestA3CrossCheck(unittest.TestCase):
    """Cross-check against type A_3 = sl_4 (simply-laced)."""

    def setUp(self):
        self.rs = A3()

    def test_positive_root_count(self):
        """A_3 has 6 positive roots."""
        self.assertEqual(len(self.rs.positive_roots), 6)

    def test_weyl_group_order(self):
        """Weyl group of A_3 has order 24 = 4!."""
        self.assertEqual(len(self.rs.weyl_group), 24)

    def test_standard_rep_dim(self):
        """V(omega_1) = 4-dim for sl_4."""
        char = self.rs.irrep_character((1, 0, 0), depth=10)
        self.assertEqual(sum(char.values()), 4)
        self.assertEqual(A3_dim(1, 0, 0), 4)

    def test_adjoint_rep_dim(self):
        """V(omega_1+omega_3) = 15-dim for sl_4 (adjoint)."""
        char = self.rs.irrep_character((1, 0, 1), depth=10)
        self.assertEqual(sum(char.values()), 15)
        self.assertEqual(A3_dim(1, 0, 1), 15)

    def test_cg_batch_fundamentals(self):
        """CG holds for A_3 fundamental weights."""
        batch = verify_batch3(self.rs, max_hw_sum=1, depth=6)
        self.assertTrue(batch["all_pass"],
                        f"A3 CG batch failed: {batch['n_fail']} failures")


# ===================================================================
# Universal CG structure
# ===================================================================

class TestUniversalCGStructure(unittest.TestCase):
    """Verify the universal structure: CG multiplicities = weight multiplicities.

    The KEY INSIGHT: for ALL types, V_lambda x L^-_i decomposes with
    multiplicities equal to the weight multiplicities of V_lambda.
    This is a consequence of the distributive law (finite sum x power series).
    """

    def test_b3_cg_coefficients_are_weight_mults(self):
        """For B_3, verify CG = weight-multiplicity formula on V(omega_1)."""
        rs = B3()
        hw = (1, 0, 0)
        V_char = rs.irrep_character(hw, depth=15)
        for node in range(3):
            L_char = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product3(V_char, L_char)
            rhs = {}
            for mu, mult in V_char.items():
                shifted = shift_char3(L_char, mu)
                for w, m in shifted.items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char3(lhs, rhs)
            reliable = {w: m for w, m in diff.items()
                        if sum(abs(w[k]) for k in range(3)) < 6}
            self.assertEqual(len(reliable), 0,
                             f"B3 V(1,0,0) x L^-_{node+1}: diff at {reliable}")

    def test_c3_cg_coefficients_are_weight_mults(self):
        """For C_3, verify CG = weight-multiplicity formula on V(omega_1)."""
        rs = C3()
        hw = (1, 0, 0)
        V_char = rs.irrep_character(hw, depth=15)
        for node in range(3):
            L_char = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product3(V_char, L_char)
            rhs = {}
            for mu, mult in V_char.items():
                shifted = shift_char3(L_char, mu)
                for w, m in shifted.items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char3(lhs, rhs)
            reliable = {w: m for w, m in diff.items()
                        if sum(abs(w[k]) for k in range(3)) < 6}
            self.assertEqual(len(reliable), 0,
                             f"C3 V(1,0,0) x L^-_{node+1}: diff at {reliable}")

    def test_b3_spin_all_nodes(self):
        """B_3 spin rep V(omega_3) satisfies CG for all three nodes."""
        rs = B3()
        hw = (0, 0, 1)
        V_char = rs.irrep_character(hw, depth=15)
        for node in range(3):
            L_char = rs.prefundamental_character(node, depth=6)
            lhs = tensor_product3(V_char, L_char)
            rhs = {}
            for mu, mult in V_char.items():
                shifted = shift_char3(L_char, mu)
                for w, m in shifted.items():
                    rhs[w] = rhs.get(w, 0) + mult * m
            diff = subtract_char3(lhs, rhs)
            reliable = {w: m for w, m in diff.items()
                        if sum(abs(w[k]) for k in range(3)) < 6}
            self.assertEqual(len(reliable), 0,
                             f"B3 V(0,0,1) x L^-_{node+1}: diff at {reliable}")


if __name__ == "__main__":
    unittest.main()
