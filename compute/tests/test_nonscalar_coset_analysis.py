"""Tests for non-scalar saturation Candidate 1: Multi-parameter cosets.

Verifies:
    - Sugawara central charge formula for all simple Lie algebras
    - GKO coset central charges and Jacobian rank = 1
    - Non-GKO coset parameter reduction
    - Minimal model identification via GKO construction
    - W-algebra central charge under DS reduction
    - Comprehensive scan: all cosets are one-parameter families
"""

import pytest
import unittest
from fractions import Fraction

from compute.lib.nonscalar_coset_analysis import (
    # Data
    lie_data,
    lie_data_type_a,
    all_lie_names,
    SimpleLieData,
    # Sugawara
    sugawara_central_charge,
    # GKO
    gko_coset,
    gko_coset_central_charge_formula,
    gko_jacobian,
    gko_effective_parameter_rank,
    gko_level_set_dimension,
    gko_sl2_virasoro_central_charge,
    gko_minimal_model_identification,
    gko_degenerate_point,
    # Non-GKO
    non_gko_coset,
    non_gko_jacobian,
    non_gko_parameter_rank,
    # W-algebra
    wn_central_charge,
    wn_rho_factor,
    wn_kappa,
    # Scans
    scan_gko_jacobian_rank,
    scan_non_gko_parameter_rank,
    # Verification
    verify_gko_is_virasoro_sl2,
    verify_coset_parameter_reduction_comprehensive,
    coset_deformation_dimension,
)


class TestLieAlgebraData(unittest.TestCase):
    """Verify simple Lie algebra data."""

    def test_sl2_data(self):
        g = lie_data("sl2")
        self.assertEqual(g.dim, 3)
        self.assertEqual(g.h_dual, 2)
        self.assertEqual(g.rank, 1)

    def test_sl3_data(self):
        g = lie_data("sl3")
        self.assertEqual(g.dim, 8)
        self.assertEqual(g.h_dual, 3)

    def test_type_a_formula(self):
        """dim(sl_{n+1}) = n(n+2), h^vee = n+1."""
        for n in range(1, 8):
            g = lie_data_type_a(n)
            self.assertEqual(g.dim, n * (n + 2))
            self.assertEqual(g.h_dual, n + 1)

    def test_exceptional_data(self):
        """Verify exceptional Lie algebra invariants."""
        self.assertEqual(lie_data("G2").dim, 14)
        self.assertEqual(lie_data("G2").h_dual, 4)
        self.assertEqual(lie_data("F4").dim, 52)
        self.assertEqual(lie_data("F4").h_dual, 9)
        self.assertEqual(lie_data("E6").dim, 78)
        self.assertEqual(lie_data("E6").h_dual, 12)
        self.assertEqual(lie_data("E7").dim, 133)
        self.assertEqual(lie_data("E7").h_dual, 18)
        self.assertEqual(lie_data("E8").dim, 248)
        self.assertEqual(lie_data("E8").h_dual, 30)

    def test_b2_equals_c2(self):
        """B2 = C2 = sp4 = so5 (dimension and h^vee)."""
        self.assertEqual(lie_data("so5").dim, lie_data("sp4").dim)
        self.assertEqual(lie_data("so5").h_dual, lie_data("sp4").h_dual)

    def test_all_registered(self):
        """At least 18 algebras registered."""
        self.assertGreaterEqual(len(all_lie_names()), 18)


class TestSugawaraCentralCharge(unittest.TestCase):
    """Verify Sugawara central charge formula."""

    def test_sl2_level_1(self):
        """c(sl_2, 1) = 3*1/(1+2) = 1."""
        g = lie_data("sl2")
        c = sugawara_central_charge(g, Fraction(1))
        self.assertEqual(c, Fraction(1))

    def test_sl2_level_2(self):
        """c(sl_2, 2) = 3*2/(2+2) = 3/2."""
        g = lie_data("sl2")
        c = sugawara_central_charge(g, Fraction(2))
        self.assertEqual(c, Fraction(3, 2))

    def test_sl2_large_k(self):
        """c(sl_2, k) -> 3 as k -> infinity."""
        g = lie_data("sl2")
        c = sugawara_central_charge(g, Fraction(10000))
        self.assertAlmostEqual(float(c), 3.0, places=2)

    def test_sl3_level_1(self):
        """c(sl_3, 1) = 8*1/(1+3) = 2."""
        g = lie_data("sl3")
        c = sugawara_central_charge(g, Fraction(1))
        self.assertEqual(c, Fraction(2))

    def test_e8_level_1(self):
        """c(E_8, 1) = 248*1/(1+30) = 8."""
        g = lie_data("E8")
        c = sugawara_central_charge(g, Fraction(1))
        self.assertEqual(c, Fraction(248, 31))
        self.assertEqual(c, Fraction(8))

    def test_critical_level_raises(self):
        """Critical level k = -h^vee should raise."""
        g = lie_data("sl2")
        with self.assertRaises(ValueError):
            sugawara_central_charge(g, Fraction(-2))

    def test_negative_level(self):
        """c(sl_2, -1/2) = 3*(-1/2)/(-1/2+2) = (-3/2)/(3/2) = -1."""
        g = lie_data("sl2")
        c = sugawara_central_charge(g, Fraction(-1, 2))
        self.assertEqual(c, Fraction(-1))

    def test_all_algebras_level_1(self):
        """c(g, 1) = dim(g)/(1+h^vee) for all simple g."""
        for name in all_lie_names():
            g = lie_data(name)
            c = sugawara_central_charge(g, Fraction(1))
            expected = Fraction(g.dim, 1 + g.h_dual)
            self.assertEqual(c, expected, f"Failed for {name}")


class TestGKOCoset(unittest.TestCase):
    """Verify GKO diagonal coset computations."""

    def test_gko_sl2_basic(self):
        """GKO coset for sl_2 at (k1,k2) = (1,1)."""
        data = gko_coset("sl2", Fraction(1), Fraction(1))
        self.assertEqual(data.c_ambient1, Fraction(1))
        self.assertEqual(data.c_ambient2, Fraction(1))
        # c(sl2, 2) = 3/2
        self.assertEqual(data.c_diagonal, Fraction(3, 2))
        # c_coset = 1 + 1 - 3/2 = 1/2
        self.assertEqual(data.c_coset, Fraction(1, 2))

    def test_gko_sl2_ising(self):
        """GKO at (1,1) gives Ising central charge c = 1/2."""
        c = gko_sl2_virasoro_central_charge(Fraction(1), Fraction(1))
        self.assertEqual(c, Fraction(1, 2))

    def test_gko_formula_consistency(self):
        """Two methods of computing c_coset agree."""
        for k1_n in range(1, 5):
            for k2_n in range(1, 5):
                k1 = Fraction(k1_n)
                k2 = Fraction(k2_n)
                data = gko_coset("sl2", k1, k2)
                formula = gko_coset_central_charge_formula(3, 2, k1, k2)
                self.assertEqual(data.c_coset, formula,
                                 f"Mismatch at (k1,k2)=({k1},{k2})")

    def test_gko_symmetry(self):
        """c_coset(k1, k2) = c_coset(k2, k1) (symmetric in levels)."""
        for k1 in [Fraction(1), Fraction(3, 2), Fraction(5, 3)]:
            for k2 in [Fraction(2), Fraction(7, 4), Fraction(1, 3)]:
                c12 = gko_coset_central_charge_formula(3, 2, k1, k2)
                c21 = gko_coset_central_charge_formula(3, 2, k2, k1)
                self.assertEqual(c12, c21)

    def test_gko_sl3_basic(self):
        """GKO coset for sl_3 at (1,1)."""
        data = gko_coset("sl3", Fraction(1), Fraction(1))
        # c(sl3, 1) = 2, c(sl3, 2) = 16/5
        self.assertEqual(data.c_ambient1, Fraction(2))
        self.assertEqual(data.c_ambient2, Fraction(2))
        self.assertEqual(data.c_diagonal, Fraction(16, 5))
        self.assertEqual(data.c_coset, Fraction(4, 5))


class TestGKOJacobian(unittest.TestCase):
    """Verify Jacobian analysis for GKO cosets."""

    def test_jacobian_nonzero_generically(self):
        """At generic (k1,k2), both partials are nonzero."""
        dc1, dc2 = gko_jacobian(3, 2, Fraction(1), Fraction(2))
        self.assertNotEqual(dc1, 0)
        self.assertNotEqual(dc2, 0)

    def test_jacobian_rank_1(self):
        """Jacobian rank is 1 at generic points (submersion to c)."""
        rank = gko_effective_parameter_rank(3, 2, Fraction(1), Fraction(2))
        self.assertEqual(rank, 1)

    def test_level_set_dim_1(self):
        """Level sets are 1-dimensional curves."""
        dim = gko_level_set_dimension(3, 2, Fraction(1), Fraction(2))
        self.assertEqual(dim, 1)

    def test_scan_sl2_all_rank_1(self):
        """Systematic scan: GKO sl_2 has Jacobian rank 1 everywhere."""
        result = scan_gko_jacobian_rank("sl2")
        self.assertTrue(result["generic_rank_is_1"],
                        f"Found rank-0 points: {result['rank_0_points']}")
        self.assertGreater(result["total_points"], 100)

    def test_scan_sl3_all_rank_1(self):
        """Systematic scan: GKO sl_3 has Jacobian rank 1 everywhere."""
        result = scan_gko_jacobian_rank("sl3")
        self.assertTrue(result["generic_rank_is_1"])

    def test_scan_G2_all_rank_1(self):
        """Systematic scan: GKO G_2 has Jacobian rank 1 everywhere."""
        result = scan_gko_jacobian_rank("G2")
        self.assertTrue(result["generic_rank_is_1"])

    def test_degenerate_point_sl2(self):
        """Degenerate point k1 = k2 = -4/3 for sl_2 (h^vee=2)."""
        k_deg = gko_degenerate_point(2)
        self.assertEqual(k_deg, (Fraction(-4, 3), Fraction(-4, 3)))
        # Rank should be 0 at degenerate point
        rank = gko_effective_parameter_rank(3, 2, k_deg[0], k_deg[1])
        self.assertEqual(rank, 0)

    def test_degenerate_point_sl3(self):
        """Degenerate point k1 = k2 = -2 for sl_3 (h^vee=3)."""
        k_deg = gko_degenerate_point(3)
        self.assertEqual(k_deg, (Fraction(-2), Fraction(-2)))
        rank = gko_effective_parameter_rank(8, 3, k_deg[0], k_deg[1])
        self.assertEqual(rank, 0)

    def test_level_set_dim_2_at_degenerate(self):
        """Level set is 2-dimensional at the degenerate point."""
        k_deg = gko_degenerate_point(2)
        dim = gko_level_set_dimension(3, 2, k_deg[0], k_deg[1])
        self.assertEqual(dim, 2)

    def test_scan_finds_degenerate_for_sl2(self):
        """Scan detects the degenerate point for sl_2."""
        result = scan_gko_jacobian_rank("sl2")
        self.assertTrue(result["degenerate_found"])

    def test_scan_finds_degenerate_for_G2(self):
        """Scan detects the degenerate point for G_2 (k = -8/3)."""
        result = scan_gko_jacobian_rank("G2")
        self.assertTrue(result["degenerate_found"])

    def test_jacobian_critical_level_raises(self):
        """Jacobian at critical level should raise ValueError."""
        with self.assertRaises(ValueError):
            gko_jacobian(3, 2, Fraction(-2), Fraction(1))

    def test_wn_kappa_composition(self):
        """wn_kappa(n,k) = wn_rho_factor(n) * wn_central_charge(n,k)."""
        for n in [2, 3, 4]:
            for k in [Fraction(0), Fraction(1), Fraction(3, 2)]:
                kappa = wn_kappa(n, k)
                expected = wn_rho_factor(n) * wn_central_charge(n, k)
                self.assertEqual(kappa, expected,
                                 f"wn_kappa mismatch at n={n}, k={k}")


class TestMinimalModelIdentification(unittest.TestCase):
    """Verify GKO construction reproduces Virasoro minimal models."""

    def test_ising_m43(self):
        """M(4,3) = Ising model: c = 1/2.

        GKO: (k1, k2) = (1, 1), c_coset = 1/2.
        """
        result = gko_minimal_model_identification(4, 3)
        self.assertTrue(result["match"])
        self.assertEqual(result["c_minimal_model"], Fraction(1, 2))
        self.assertTrue(result["unitary"])

    def test_tricritical_m54(self):
        """M(5,4) = tricritical Ising: c = 7/10.

        GKO: (k1, k2) = (2, 1), c_coset = 7/10.
        """
        result = gko_minimal_model_identification(5, 4)
        self.assertTrue(result["match"])
        self.assertEqual(result["c_minimal_model"], Fraction(7, 10))

    def test_three_state_potts_m65(self):
        """M(6,5) = three-state Potts: c = 4/5.

        GKO: (k1, k2) = (3, 1), c_coset = 4/5.
        """
        result = gko_minimal_model_identification(6, 5)
        self.assertTrue(result["match"])
        self.assertEqual(result["c_minimal_model"], Fraction(4, 5))

    def test_m76(self):
        """M(7,6): c = 6/7."""
        result = gko_minimal_model_identification(7, 6)
        self.assertTrue(result["match"])
        self.assertEqual(result["c_minimal_model"], Fraction(6, 7))

    def test_unitary_series(self):
        """Unitary minimal models M(m+1, m) for m = 2, ..., 10.

        c = 1 - 6/((m+1)*m)
        GKO: (k1, k2) = (m-2, 1) gives M(m+1, m).
        """
        for m in range(2, 11):
            result = gko_minimal_model_identification(m + 1, m)
            self.assertTrue(result["match"],
                            f"Failed for M({m+1},{m})")
            self.assertTrue(result["unitary"])

    def test_nonunitary_not_verified(self):
        """Non-unitary M(5,2): not verified via integer-level GKO."""
        result = gko_minimal_model_identification(5, 2)
        self.assertFalse(result["unitary"])
        self.assertIsNone(result["match"])  # not verified
        self.assertEqual(result["c_minimal_model"], Fraction(-22, 5))


class TestNonGKOCoset(unittest.TestCase):
    """Verify non-GKO coset analysis."""

    def test_non_gko_basic(self):
        """Non-GKO coset sl_2 -> sl_2 x sl_3 with Dynkin index (1,1)."""
        data = non_gko_coset(
            "sl2", "sl3", "sl2",
            Fraction(1), Fraction(1),
            Fraction(1), Fraction(1),
        )
        # k3 = 1*1 + 1*1 = 2
        self.assertEqual(data.k3, Fraction(2))
        # c_coset = c(sl2,1) + c(sl3,1) - c(sl2,2) = 1 + 2 - 3/2 = 3/2
        self.assertEqual(data.c_coset, Fraction(3, 2))

    def test_non_gko_jacobian_rank_1(self):
        """Non-GKO Jacobian rank is 1 generically."""
        rank = non_gko_parameter_rank(
            "sl2", "sl3", "sl2",
            Fraction(1), Fraction(1),
            Fraction(1), Fraction(2),
        )
        self.assertEqual(rank, 1)

    def test_non_gko_scan_all_rank_1(self):
        """Systematic scan: non-GKO sl_2 -> sl_2 x sl_3 is one-parameter."""
        result = scan_non_gko_parameter_rank(
            "sl2", "sl3", "sl2",
            Fraction(1), Fraction(1),
        )
        self.assertTrue(result["generic_rank_is_1"])

    def test_non_gko_scan_sl2_sp4(self):
        """Systematic scan: non-GKO sl_2 -> sl_2 x sp_4 is one-parameter."""
        result = scan_non_gko_parameter_rank(
            "sl2", "sp4", "sl2",
            Fraction(1), Fraction(1),
        )
        self.assertTrue(result["generic_rank_is_1"])


class TestWAlgebraCentralCharge(unittest.TestCase):
    """Verify W-algebra central charge computations."""

    def test_virasoro_from_w2(self):
        """W_2 = Virasoro via DS(sl_2).

        c = (N-1) - N(N^2-1)(t-1)^2/t with N=2, t=k+2.
        At k=0: t=2, c = 1 - 2*3*1/2 = 1-3 = -2.
        """
        c = wn_central_charge(2, Fraction(0))
        self.assertEqual(c, Fraction(-2))

    def test_w2_level_1(self):
        """W_2 at k=1: t=3, c = 1 - 6*4/3 = 1-8 = -7."""
        c = wn_central_charge(2, Fraction(1))
        self.assertEqual(c, Fraction(-7))

    def test_w3_level_0(self):
        """W_3 at k=0: N=3, t=k+3=3, |rho|^2 = 3*8/12 = 2.

        c = 2 - 12*2*(3-1)^2/3 = 2 - 96/3 = 2-32 = -30.
        """
        c = wn_central_charge(3, Fraction(0))
        self.assertEqual(c, Fraction(-30))

    def test_rho_factor_sl2(self):
        """rho(sl_2) = 1/2."""
        self.assertEqual(wn_rho_factor(2), Fraction(1, 2))

    def test_rho_factor_sl3(self):
        """rho(sl_3) = 1/2 + 1/3 = 5/6."""
        self.assertEqual(wn_rho_factor(3), Fraction(5, 6))


class TestDeformationDimension(unittest.TestCase):
    """Verify deformation space analysis."""

    def test_gko_diagonal(self):
        result = coset_deformation_dimension("gko_diagonal")
        self.assertEqual(result["effective_parameters"], 1)
        self.assertEqual(result["dim_H2_cyc"], 1)
        self.assertTrue(result["scalar_saturated"])

    def test_non_gko(self):
        result = coset_deformation_dimension("non_gko_different_factors")
        self.assertEqual(result["effective_parameters"], 1)
        self.assertTrue(result["scalar_saturated"])

    def test_hypothetical_two_param(self):
        result = coset_deformation_dimension("genuinely_two_parameter")
        self.assertEqual(result["effective_parameters"], 2)
        self.assertFalse(result["scalar_saturated"])


class TestComprehensiveVerification(unittest.TestCase):
    """Master verification of parameter reduction across all coset classes."""

    def test_all_gko_one_parameter(self):
        """All GKO cosets across sl_2, sl_3, sl_4, G_2 are one-parameter."""
        result = verify_coset_parameter_reduction_comprehensive()
        self.assertTrue(result["all_one_parameter"])

    def test_virasoro_identification(self):
        """GKO sl_2 cosets are identified as Virasoro (dim H^2_cyc = 1)."""
        for k1 in [Fraction(1), Fraction(2), Fraction(3, 2)]:
            for k2 in [Fraction(1), Fraction(5, 3)]:
                result = verify_gko_is_virasoro_sl2(k1, k2)
                self.assertTrue(result["scalar_saturated"])
                self.assertEqual(result["dim_H2_cyc"], 1)
                self.assertEqual(result["jacobian_rank"], 1)
