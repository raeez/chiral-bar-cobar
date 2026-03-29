"""Tests for the exceptional type RTT scaffold.

Verifies root system data, representation dimensions, Yang-Baxter equation,
and prefundamental CG decomposition for exceptional Dynkin types G_2, E_6,
E_7, E_8 (and root system for F_4).

MC3 difficulty grades:
  G_2: grade C- (rank 2, 7-dim fundamental, fully accessible)
  E_6: grade B (27-dim fundamental, Weyl dim works, Freudenthal slow)
  E_7: grade C+ (56-dim fundamental)
  E_8: grade D (248-dim = adjoint, extreme)
  F_4: grade D (non-simply-laced, representation theory deferred)

References:
  - Humphreys, "Introduction to Lie Algebras and Representation Theory"
  - concordance.tex, conj:mc3-arbitrary-type
"""

import unittest

from compute.lib.yangian_rtt_exceptional import (
    ExceptionalRootSystem,
    EXCEPTIONAL_DATA,
    FUNDAMENTAL_DIMS,
    verify_all_exceptional_root_systems,
    verify_fundamental_dims,
    verify_cg_G2,
    verify_cg_G2_batch,
    G2_root_system,
    G2_dim,
    weyl_dim_explicit,
    yang_baxter_check_generic,
)


# ===================================================================
# Root system verification — all exceptional types
# ===================================================================

class TestG2RootSystem(unittest.TestCase):
    """Root system for G_2."""

    def setUp(self):
        self.rs = ExceptionalRootSystem("G2")

    def test_rank(self):
        self.assertEqual(self.rs.rank, 2)

    def test_positive_root_count(self):
        self.assertEqual(len(self.rs.positive_roots), 6)

    def test_dim_algebra(self):
        self.assertEqual(self.rs.dim_algebra, 14)

    def test_coxeter(self):
        self.assertEqual(self.rs.coxeter_number, 6)

    def test_dual_coxeter(self):
        self.assertEqual(self.rs.dual_coxeter_number, 4)


class TestF4RootSystem(unittest.TestCase):
    """Root system for F_4."""

    def setUp(self):
        self.rs = ExceptionalRootSystem("F4")

    def test_rank(self):
        self.assertEqual(self.rs.rank, 4)

    def test_positive_root_count(self):
        self.assertEqual(len(self.rs.positive_roots), 24)

    def test_dim_algebra(self):
        self.assertEqual(self.rs.dim_algebra, 52)

    def test_coxeter(self):
        self.assertEqual(self.rs.coxeter_number, 12)

    def test_dual_coxeter(self):
        self.assertEqual(self.rs.dual_coxeter_number, 9)


class TestE6RootSystem(unittest.TestCase):
    """Root system for E_6."""

    def setUp(self):
        self.rs = ExceptionalRootSystem("E6")

    def test_rank(self):
        self.assertEqual(self.rs.rank, 6)

    def test_positive_root_count(self):
        self.assertEqual(len(self.rs.positive_roots), 36)

    def test_dim_algebra(self):
        self.assertEqual(self.rs.dim_algebra, 78)

    def test_coxeter(self):
        self.assertEqual(self.rs.coxeter_number, 12)


class TestE7RootSystem(unittest.TestCase):
    """Root system for E_7."""

    def setUp(self):
        self.rs = ExceptionalRootSystem("E7")

    def test_rank(self):
        self.assertEqual(self.rs.rank, 7)

    def test_positive_root_count(self):
        self.assertEqual(len(self.rs.positive_roots), 63)

    def test_dim_algebra(self):
        self.assertEqual(self.rs.dim_algebra, 133)


class TestE8RootSystem(unittest.TestCase):
    """Root system for E_8."""

    def setUp(self):
        self.rs = ExceptionalRootSystem("E8")

    def test_rank(self):
        self.assertEqual(self.rs.rank, 8)

    def test_positive_root_count(self):
        self.assertEqual(len(self.rs.positive_roots), 120)

    def test_dim_algebra(self):
        self.assertEqual(self.rs.dim_algebra, 248)

    def test_coxeter(self):
        self.assertEqual(self.rs.coxeter_number, 30)


class TestAllRootSystems(unittest.TestCase):
    """Batch root system verification."""

    def test_all_positive_root_counts(self):
        results = verify_all_exceptional_root_systems()
        for name, data in results.items():
            with self.subTest(name=name):
                self.assertTrue(data["pos_roots_match"],
                                f"{name}: {data['num_pos_roots']} != "
                                f"{data['expected_pos_roots']}")


# ===================================================================
# Representation dimensions
# ===================================================================

class TestG2Dimensions(unittest.TestCase):
    """Representation dimensions for G_2."""

    def test_fundamental_7(self):
        """V(omega_1) = 7 for G_2."""
        g2 = G2_root_system()
        char = g2.irrep_character((1, 0), depth=15)
        self.assertEqual(sum(char.values()), 7)
        self.assertEqual(G2_dim(1, 0), 7)

    def test_adjoint_14(self):
        """V(omega_2) = 14 (adjoint) for G_2."""
        g2 = G2_root_system()
        char = g2.irrep_character((0, 1), depth=15)
        self.assertEqual(sum(char.values()), 14)
        self.assertEqual(G2_dim(0, 1), 14)

    def test_dim_formula_consistency(self):
        """Weyl formula matches character for small reps."""
        g2 = G2_root_system()
        for a in range(3):
            for b in range(3 - a):
                if a == 0 and b == 0:
                    continue
                char = g2.irrep_character((a, b), depth=20)
                dim_char = sum(char.values())
                dim_form = G2_dim(a, b)
                self.assertEqual(dim_char, dim_form,
                                 f"G2: V({a},{b}): char={dim_char} != form={dim_form}")


class TestE6Dimensions(unittest.TestCase):
    """Weyl dimensions for E_6 (simply-laced, formula works)."""

    def test_omega1_is_27(self):
        """V(omega_1) = 27."""
        self.assertEqual(weyl_dim_explicit("E6", (1, 0, 0, 0, 0, 0)), 27)

    def test_omega6_is_27(self):
        """V(omega_6) = 27 (dual of omega_1)."""
        self.assertEqual(weyl_dim_explicit("E6", (0, 0, 0, 0, 0, 1)), 27)

    def test_omega2_is_78(self):
        """V(omega_2) = 78 (adjoint)."""
        self.assertEqual(weyl_dim_explicit("E6", (0, 1, 0, 0, 0, 0)), 78)


class TestE7Dimensions(unittest.TestCase):
    """Weyl dimensions for E_7."""

    def test_omega7_is_56(self):
        """V(omega_7) = 56 (minimal representation)."""
        self.assertEqual(weyl_dim_explicit("E7", (0, 0, 0, 0, 0, 0, 1)), 56)

    def test_omega1_is_133(self):
        """V(omega_1) = 133 (adjoint)."""
        self.assertEqual(weyl_dim_explicit("E7", (1, 0, 0, 0, 0, 0, 0)), 133)


class TestE8Dimensions(unittest.TestCase):
    """Weyl dimensions for E_8."""

    def test_omega8_is_248(self):
        """V(omega_8) = 248 (adjoint = minimal)."""
        self.assertEqual(
            weyl_dim_explicit("E8", (0, 0, 0, 0, 0, 0, 0, 1)), 248
        )


class TestFundamentalDims(unittest.TestCase):
    """Batch fundamental dimension verification."""

    def test_all_accessible(self):
        results = verify_fundamental_dims()
        for key, data in results.items():
            with self.subTest(key=key):
                self.assertTrue(data["match"], f"{key}: {data}")


# ===================================================================
# G_2 Clebsch-Gordan decomposition
# ===================================================================

class TestG2ClebschGordan(unittest.TestCase):
    """Prefundamental CG for G_2."""

    def test_cg_omega1_node1(self):
        res = verify_cg_G2((1, 0), 0, depth=8)
        self.assertTrue(res["match"])

    def test_cg_omega1_node2(self):
        res = verify_cg_G2((1, 0), 1, depth=8)
        self.assertTrue(res["match"])

    def test_cg_omega2_node1(self):
        res = verify_cg_G2((0, 1), 0, depth=8)
        self.assertTrue(res["match"])

    def test_cg_omega2_node2(self):
        res = verify_cg_G2((0, 1), 1, depth=8)
        self.assertTrue(res["match"])

    def test_cg_batch(self):
        batch = verify_cg_G2_batch(max_hw_sum=2, depth=8)
        self.assertTrue(batch["all_pass"],
                        f"G2 CG: {batch['n_fail']} failures")

    def test_cg_batch_count(self):
        """At least 10 tests in the batch."""
        batch = verify_cg_G2_batch(max_hw_sum=2, depth=8)
        total = batch["n_pass"] + batch["n_fail"]
        self.assertGreaterEqual(total, 10)


# ===================================================================
# Yang-Baxter equation for generic R-matrix
# ===================================================================

class TestYangBaxterGeneric(unittest.TestCase):
    """Yang-Baxter equation R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12}
    for the generic R-matrix R(u) = I - P/u + Q/(u-kappa)."""

    def test_ybe_7dim(self):
        """7-dim (G_2 fundamental)."""
        res = yang_baxter_check_generic(7, 2.5, 1.5, 2.3)
        self.assertTrue(res["passes"])

    def test_ybe_7dim_alt_params(self):
        res = yang_baxter_check_generic(7, 2.5, 0.5, 3.7)
        self.assertTrue(res["passes"])

    def test_ybe_14dim(self):
        """14-dim (G_2 adjoint)."""
        res = yang_baxter_check_generic(14, 6.0, 1.5, 2.3)
        self.assertTrue(res["passes"])

    def test_ybe_correct_kappa_values(self):
        """YBE holds for kappa = N/2 - 1 (the correct orthogonal value)."""
        for N_rep in [4, 6, 8, 10]:
            kappa = N_rep / 2.0 - 1.0
            res = yang_baxter_check_generic(N_rep, kappa, 1.5, 2.3)
            self.assertTrue(res["passes"],
                            f"YBE failed for N={N_rep}, kappa={kappa}")


# ===================================================================
# Inner product and symmetrizer
# ===================================================================

class TestSymmetrizer(unittest.TestCase):
    """Symmetrizer computation for exceptional types."""

    def test_g2_symmetrizer(self):
        """G_2 symmetrizer: d = (3, 1) or (1, 3) depending on convention."""
        rs = ExceptionalRootSystem("G2")
        # With our Cartan [[2,-1],[-3,2]], the symmetrizer satisfies
        # d_i A_{ij} = d_j A_{ji} (symmetric DA).
        d = rs.symmetrizer
        A = rs.cartan
        for i in range(2):
            for j in range(2):
                self.assertEqual(d[i] * A[i][j], d[j] * A[j][i],
                                 f"DA not symmetric at ({i},{j})")

    def test_e6_symmetrizer(self):
        """E_6 is simply-laced: all d_i = 1."""
        rs = ExceptionalRootSystem("E6")
        self.assertEqual(rs.symmetrizer, [1, 1, 1, 1, 1, 1])

    def test_e8_symmetrizer(self):
        """E_8 is simply-laced: all d_i = 1."""
        rs = ExceptionalRootSystem("E8")
        self.assertEqual(rs.symmetrizer, [1] * 8)


# ===================================================================
# Exponents
# ===================================================================

class TestExponents(unittest.TestCase):
    """Verify Lie algebra exponents from the data table."""

    def test_g2_exponents(self):
        self.assertEqual(EXCEPTIONAL_DATA["G2"][5], [1, 5])

    def test_e6_exponents(self):
        self.assertEqual(EXCEPTIONAL_DATA["E6"][5], [1, 4, 5, 7, 8, 11])

    def test_e8_exponents(self):
        exps = EXCEPTIONAL_DATA["E8"][5]
        self.assertEqual(len(exps), 8)
        self.assertEqual(exps[0], 1)
        self.assertEqual(exps[-1], 29)

    def test_exponent_count_equals_rank(self):
        """Number of exponents = rank."""
        for name in ["G2", "F4", "E6", "E7", "E8"]:
            rs = ExceptionalRootSystem(name)
            self.assertEqual(len(EXCEPTIONAL_DATA[name][5]), rs.rank)


if __name__ == "__main__":
    unittest.main()
