"""Tests for the type D Yangian RTT engine.

Verifies the FRONTIER computation for MC3 extension to orthogonal Dynkin
types (conj:mc3-arbitrary-type). The key results tested:

  1. D_N root system data: positive roots, Weyl group, Coxeter numbers
  2. Orthogonal R-matrix: Yang-Baxter equation, spectral decomposition,
     symmetry properties (PT, unitarity)
  3. D_3 = so(6) ~ sl(4) consistency check
  4. D_4 = so(8) triality: three 8-dimensional representations
  5. Representation dimensions via Weyl formula and character computation
  6. Prefundamental CG decomposition for type D
  7. RTT relation structure

References:
  - Molev, "Yangians and classical Lie algebras", AMS 2007, Ch. 4
  - concordance.tex, conj:mc3-arbitrary-type
"""

import unittest

from compute.lib.yangian_rtt_typeD import (
    TypeDRootSystem,
    orthogonal_r_matrix,
    yang_baxter_check,
    r_matrix_spectral_decomposition,
    r_matrix_symmetry_check,
    d3_sl4_consistency,
    d4_triality_check,
    D3_dim,
    D4_dim,
    verify_cg_typeD,
    verify_cg_batch_typeD,
    rtt_relation_count,
    rtt_generators_per_level,
)


# ===================================================================
# D_N root system tests
# ===================================================================

class TestD3RootSystem(unittest.TestCase):
    """Root system for D_3 = so(6)."""

    def setUp(self):
        self.rs = TypeDRootSystem(3)

    def test_rank(self):
        self.assertEqual(self.rs.rank, 3)

    def test_positive_root_count(self):
        """D_3 has 6 positive roots."""
        self.assertEqual(self.rs.num_positive_roots(), 6)
        self.assertEqual(self.rs.num_positive_roots(),
                         self.rs.expected_num_positive_roots())

    def test_dim_algebra(self):
        """dim so(6) = 15."""
        self.assertEqual(self.rs.dim_algebra(), 15)

    def test_coxeter_number(self):
        """h(D_3) = 2(3-1) = 4."""
        self.assertEqual(self.rs.coxeter_number(), 4)

    def test_dual_coxeter(self):
        """h*(D_3) = 2*3-2 = 4 (simply-laced: h = h*)."""
        self.assertEqual(self.rs.dual_coxeter_number(), 4)

    def test_weyl_order(self):
        """|W(D_3)| = 2^2 * 3! = 24."""
        W = self.rs.weyl_group()
        self.assertEqual(len(W), 24)
        self.assertEqual(len(W), self.rs.expected_weyl_order())

    def test_cartan_matrix(self):
        """D_3 Cartan: branching at node 0."""
        A = self.rs.cartan
        self.assertEqual(A[0][0], 2)
        self.assertEqual(A[0][1], -1)
        self.assertEqual(A[0][2], -1)
        self.assertEqual(A[1][2], 0)  # spinor nodes not connected

    def test_dim_vector_rep(self):
        """V(omega_1) = 6 (vector rep of so(6))."""
        char = self.rs.irrep_character((1, 0, 0), depth=10)
        self.assertEqual(sum(char.values()), 6)

    def test_dim_spinor_reps(self):
        """V(omega_2) = V(omega_3) = 4 (half-spinors of so(6))."""
        for hw in [(0, 1, 0), (0, 0, 1)]:
            char = self.rs.irrep_character(hw, depth=10)
            self.assertEqual(sum(char.values()), 4)


class TestD4RootSystem(unittest.TestCase):
    """Root system for D_4 = so(8)."""

    def setUp(self):
        self.rs = TypeDRootSystem(4)

    def test_rank(self):
        self.assertEqual(self.rs.rank, 4)

    def test_positive_root_count(self):
        """D_4 has 12 positive roots."""
        self.assertEqual(self.rs.num_positive_roots(), 12)

    def test_dim_algebra(self):
        """dim so(8) = 28."""
        self.assertEqual(self.rs.dim_algebra(), 28)

    def test_coxeter_number(self):
        """h(D_4) = 6."""
        self.assertEqual(self.rs.coxeter_number(), 6)

    def test_weyl_order(self):
        """|W(D_4)| = 2^3 * 4! = 192."""
        W = self.rs.weyl_group()
        self.assertEqual(len(W), 192)

    def test_dim_vector_rep(self):
        """V(omega_1) = 8 (vector)."""
        char = self.rs.irrep_character((1, 0, 0, 0), depth=10)
        self.assertEqual(sum(char.values()), 8)

    def test_dim_adjoint(self):
        """V(omega_2) = 28 (adjoint)."""
        char = self.rs.irrep_character((0, 1, 0, 0), depth=12)
        self.assertEqual(sum(char.values()), 28)

    def test_dim_spinors(self):
        """V(omega_3) = V(omega_4) = 8 (half-spinors)."""
        for hw in [(0, 0, 1, 0), (0, 0, 0, 1)]:
            char = self.rs.irrep_character(hw, depth=10)
            self.assertEqual(sum(char.values()), 8)


class TestD5RootSystem(unittest.TestCase):
    """Root system for D_5 = so(10)."""

    def setUp(self):
        self.rs = TypeDRootSystem(5)

    def test_positive_root_count(self):
        """D_5 has 20 positive roots."""
        self.assertEqual(self.rs.num_positive_roots(), 20)

    def test_dim_algebra(self):
        """dim so(10) = 45."""
        self.assertEqual(self.rs.dim_algebra(), 45)

    def test_expected_weyl_order(self):
        """|W(D_5)| = 2^4 * 5! = 1920."""
        self.assertEqual(self.rs.expected_weyl_order(), 1920)


# ===================================================================
# D_3 ~ sl(4) consistency
# ===================================================================

class TestD3Sl4Consistency(unittest.TestCase):
    """Verify D_3 = so(6) ~ sl(4) at root system level."""

    def setUp(self):
        self.checks = d3_sl4_consistency()

    def test_rank(self):
        self.assertTrue(self.checks["rank"])

    def test_num_pos_roots(self):
        self.assertTrue(self.checks["num_pos_roots"])

    def test_dim_algebra(self):
        self.assertTrue(self.checks["dim_algebra"])

    def test_coxeter(self):
        self.assertTrue(self.checks["coxeter"])

    def test_weyl_order(self):
        self.assertTrue(self.checks["weyl_order"])

    def test_dim_vector(self):
        self.assertTrue(self.checks["dim_vector"])

    def test_dim_spinor(self):
        self.assertTrue(self.checks["dim_spinor"])


# ===================================================================
# D_4 triality
# ===================================================================

class TestD4Triality(unittest.TestCase):
    """Verify D_4 = so(8) triality symmetry."""

    def setUp(self):
        self.checks = d4_triality_check()

    def test_dim_vector(self):
        """Vector representation is 8-dimensional."""
        self.assertTrue(self.checks["dim_vector"])

    def test_dim_spinor_plus(self):
        """Half-spinor S+ is 8-dimensional."""
        self.assertTrue(self.checks["dim_spinor_plus"])

    def test_dim_spinor_minus(self):
        """Half-spinor S- is 8-dimensional."""
        self.assertTrue(self.checks["dim_spinor_minus"])

    def test_dim_adjoint(self):
        """Adjoint is 28-dimensional."""
        self.assertTrue(self.checks["dim_adjoint"])

    def test_triality_weight_count(self):
        """All three 8-dim reps have the same number of weights."""
        self.assertTrue(self.checks["triality_weight_count"])


# ===================================================================
# Weyl dimension formulas
# ===================================================================

class TestD3DimensionFormula(unittest.TestCase):
    """Weyl dimension formula for D_3 = so(6)."""

    def setUp(self):
        self.rs = TypeDRootSystem(3)

    def test_fundamental_dims(self):
        for hw, expected in [((1, 0, 0), 6), ((0, 1, 0), 4), ((0, 0, 1), 4)]:
            self.assertEqual(D3_dim(*hw), expected)

    def test_adjoint(self):
        """V(omega_1 + omega_2) should have dim 20."""
        self.assertEqual(D3_dim(1, 1, 0), 20)

    def test_formula_matches_character(self):
        for hw in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0), (1, 1, 0)]:
            char = self.rs.irrep_character(hw, depth=12)
            self.assertEqual(sum(char.values()), D3_dim(*hw))


class TestD4DimensionFormula(unittest.TestCase):
    """Weyl dimension formula for D_4 = so(8)."""

    def test_fundamental_dims(self):
        self.assertEqual(D4_dim(1, 0, 0, 0), 8)
        self.assertEqual(D4_dim(0, 1, 0, 0), 28)
        self.assertEqual(D4_dim(0, 0, 1, 0), 8)
        self.assertEqual(D4_dim(0, 0, 0, 1), 8)

    def test_triality_symmetry(self):
        """D_4 triality: dim V(omega_1) = dim V(omega_3) = dim V(omega_4)."""
        self.assertEqual(D4_dim(1, 0, 0, 0), D4_dim(0, 0, 1, 0))
        self.assertEqual(D4_dim(1, 0, 0, 0), D4_dim(0, 0, 0, 1))

    def test_symmetric_square(self):
        """V(2*omega_1) = Sym^2(V_8) = 36-dim."""
        self.assertEqual(D4_dim(2, 0, 0, 0), 35)
        # Actually Sym^2(8) = 36, but V(2*omega_1) might be 35 (traceless).
        # Let me check: so(8) vector rep, Sym^2 = traceless symmetric + trace
        # = 35 + 1 = 36. V(2*omega_1) = 35 (traceless).


# ===================================================================
# Orthogonal R-matrix: Yang-Baxter equation
# ===================================================================

class TestYangBaxterEquation(unittest.TestCase):
    """Yang-Baxter equation for the orthogonal R-matrix."""

    def test_ybe_so4(self):
        res = yang_baxter_check(4, 1.5, 2.3)
        self.assertTrue(res["passes"])

    def test_ybe_so6(self):
        res = yang_baxter_check(6, 1.5, 2.3)
        self.assertTrue(res["passes"])

    def test_ybe_so8(self):
        res = yang_baxter_check(8, 1.5, 2.3)
        self.assertTrue(res["passes"])

    def test_ybe_so4_multiple_params(self):
        for u, v in [(0.5, 3.7), (2.1, -1.3), (0.1, 0.2)]:
            res = yang_baxter_check(4, u, v)
            self.assertTrue(res["passes"],
                            f"YBE failed for so(4) u={u} v={v}")

    def test_ybe_so6_multiple_params(self):
        for u, v in [(0.5, 3.7), (2.1, -1.3)]:
            res = yang_baxter_check(6, u, v)
            self.assertTrue(res["passes"],
                            f"YBE failed for so(6) u={u} v={v}")

    def test_ybe_so8_multiple_params(self):
        for u, v in [(0.5, 3.7), (2.1, -1.3)]:
            res = yang_baxter_check(8, u, v)
            self.assertTrue(res["passes"],
                            f"YBE failed for so(8) u={u} v={v}")


# ===================================================================
# R-matrix spectral decomposition
# ===================================================================

class TestSpectralDecomposition(unittest.TestCase):
    """Spectral structure of the orthogonal R-matrix."""

    def test_operator_identities_so4(self):
        sd = r_matrix_spectral_decomposition(4)
        self.assertTrue(sd["P_squared_is_I"])
        self.assertTrue(sd["Q_squared_is_NQ"])
        self.assertTrue(sd["PQ_is_Q"])
        self.assertTrue(sd["QP_is_Q"])

    def test_operator_identities_so6(self):
        sd = r_matrix_spectral_decomposition(6)
        self.assertTrue(sd["P_squared_is_I"])
        self.assertTrue(sd["Q_squared_is_NQ"])
        self.assertTrue(sd["PQ_is_Q"])

    def test_operator_identities_so8(self):
        sd = r_matrix_spectral_decomposition(8)
        self.assertTrue(sd["P_squared_is_I"])
        self.assertTrue(sd["Q_squared_is_NQ"])

    def test_sym_alt_dimensions_so4(self):
        """so(4): Sym^2(C^4) = 10, Alt^2(C^4) = 6."""
        sd = r_matrix_spectral_decomposition(4)
        self.assertTrue(sd["sym_matches"])
        self.assertTrue(sd["alt_matches"])

    def test_sym_alt_dimensions_so6(self):
        """so(6): Sym = 21, Alt = 15."""
        sd = r_matrix_spectral_decomposition(6)
        self.assertTrue(sd["sym_matches"])
        self.assertTrue(sd["alt_matches"])

    def test_sym_alt_dimensions_so8(self):
        """so(8): Sym = 36, Alt = 28 (= adjoint)."""
        sd = r_matrix_spectral_decomposition(8)
        self.assertTrue(sd["sym_matches"])
        self.assertTrue(sd["alt_matches"])


# ===================================================================
# R-matrix symmetry
# ===================================================================

class TestRMatrixSymmetry(unittest.TestCase):
    """PT-symmetry and unitarity of the orthogonal R-matrix."""

    def test_pt_symmetry_so4(self):
        sym = r_matrix_symmetry_check(4)
        self.assertTrue(sym["pt_symmetry"])

    def test_pt_symmetry_so6(self):
        sym = r_matrix_symmetry_check(6)
        self.assertTrue(sym["pt_symmetry"])

    def test_pt_symmetry_so8(self):
        sym = r_matrix_symmetry_check(8)
        self.assertTrue(sym["pt_symmetry"])

    def test_unitarity_so4(self):
        sym = r_matrix_symmetry_check(4)
        self.assertTrue(sym["unitarity_proportional"])

    def test_unitarity_so6(self):
        sym = r_matrix_symmetry_check(6)
        self.assertTrue(sym["unitarity_proportional"])

    def test_unitarity_so8(self):
        sym = r_matrix_symmetry_check(8)
        self.assertTrue(sym["unitarity_proportional"])


# ===================================================================
# RTT structure
# ===================================================================

class TestRTTStructure(unittest.TestCase):
    """RTT relation and generator counts."""

    def test_rtt_so4(self):
        self.assertEqual(rtt_relation_count(4), 16)

    def test_rtt_so6(self):
        self.assertEqual(rtt_relation_count(6), 36)

    def test_rtt_so8(self):
        self.assertEqual(rtt_relation_count(8), 64)

    def test_generators_so4(self):
        """Y(so(4)) has 6 generators per level (dim so(4) = 6)."""
        self.assertEqual(rtt_generators_per_level(4), 6)

    def test_generators_so6(self):
        """Y(so(6)) has 15 generators per level."""
        self.assertEqual(rtt_generators_per_level(6), 15)

    def test_generators_so8(self):
        """Y(so(8)) has 28 generators per level."""
        self.assertEqual(rtt_generators_per_level(8), 28)


# ===================================================================
# Prefundamental CG for type D
# ===================================================================

class TestCGTypeD3(unittest.TestCase):
    """Prefundamental CG for D_3 = so(6)."""

    def test_cg_vector_node1(self):
        res = verify_cg_typeD(3, (1, 0, 0), 0, depth=6)
        self.assertTrue(res["match"])

    def test_cg_spinor_node2(self):
        res = verify_cg_typeD(3, (0, 1, 0), 1, depth=6)
        self.assertTrue(res["match"])

    def test_cg_cospinor_node3(self):
        res = verify_cg_typeD(3, (0, 0, 1), 2, depth=6)
        self.assertTrue(res["match"])

    def test_cg_batch_fundamentals(self):
        batch = verify_cg_batch_typeD(3, depth=6)
        self.assertTrue(batch["all_pass"])


class TestCGTypeD4(unittest.TestCase):
    """Prefundamental CG for D_4 = so(8)."""

    def test_cg_vector(self):
        res = verify_cg_typeD(4, (1, 0, 0, 0), 0, depth=5)
        self.assertTrue(res["match"])

    def test_cg_spinor_plus(self):
        res = verify_cg_typeD(4, (0, 0, 1, 0), 2, depth=5)
        self.assertTrue(res["match"])

    def test_cg_spinor_minus(self):
        res = verify_cg_typeD(4, (0, 0, 0, 1), 3, depth=5)
        self.assertTrue(res["match"])

    def test_cg_batch_fundamentals(self):
        batch = verify_cg_batch_typeD(4, depth=5)
        self.assertTrue(batch["all_pass"])


# ===================================================================
# Kappa parameter
# ===================================================================

class TestKappaParameter(unittest.TestCase):
    """The kappa parameter in the R-matrix."""

    def test_kappa_so4(self):
        """kappa(so(4)) = 4/2 - 1 = 1."""
        sd = r_matrix_spectral_decomposition(4)
        self.assertAlmostEqual(sd["kappa"], 1.0)

    def test_kappa_so6(self):
        """kappa(so(6)) = 6/2 - 1 = 2."""
        sd = r_matrix_spectral_decomposition(6)
        self.assertAlmostEqual(sd["kappa"], 2.0)

    def test_kappa_so8(self):
        """kappa(so(8)) = 8/2 - 1 = 3."""
        sd = r_matrix_spectral_decomposition(8)
        self.assertAlmostEqual(sd["kappa"], 3.0)


if __name__ == "__main__":
    unittest.main()
