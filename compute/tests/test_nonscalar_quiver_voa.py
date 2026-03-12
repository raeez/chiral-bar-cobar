"""Tests for non-scalar saturation Candidate 2: 4d N=2 quiver VOAs.

Verifies:
    - 4d anomaly coefficients for SQCD and necklace quiver theories
    - Central charge c_2d = -12 c_4d
    - VOA identification for specific theories
    - Schur index coupling-independence
    - Conformal manifold dimension vs. VOA parameter count
    - OPE rigidity for Virasoro, sl_2 KM, W_3, W_N
    - Master verification: all quiver VOAs are scalar-saturated
"""

import pytest
import unittest
from fractions import Fraction

from compute.lib.nonscalar_quiver_voa import (
    # Theory data
    N2TheoryData,
    sqcd_theory,
    necklace_quiver_theory,
    class_s_theory,
    # Schur index
    schur_index_sqcd_su2_nf4,
    schur_index_coupling_independence_test,
    # Analysis
    conformal_manifold_analysis,
    verify_quiver_voa_saturation,
    verify_sqcd_voa_identification,
    # OPE rigidity
    ope_rigidity_sl2_km,
    ope_rigidity_virasoro,
    ope_rigidity_w3,
    ope_rigidity_wn,
)


class TestSQCDTheories(unittest.TestCase):
    """Verify SU(N) SQCD theory data."""

    def test_su2_sqcd(self):
        """SU(2) SQCD with Nf=4."""
        t = sqcd_theory(2)
        self.assertEqual(t.dim_conformal_manifold, 1)
        self.assertEqual(t.voa_parameters, 1)
        self.assertIn("SU(2)", t.name)

    def test_su3_sqcd(self):
        """SU(3) SQCD with Nf=6."""
        t = sqcd_theory(3)
        self.assertEqual(t.dim_conformal_manifold, 1)
        self.assertEqual(t.voa_parameters, 1)

    def test_sqcd_central_charge_formula(self):
        """c_2d = -12 * c_4d for all SQCD."""
        for N in range(2, 7):
            t = sqcd_theory(N)
            self.assertEqual(t.c_2d, -12 * t.c_anomaly)

    def test_sqcd_no_coupling_dependence(self):
        """SQCD conformal manifold is 1d, VOA has 1 parameter => no reduction."""
        for N in range(2, 7):
            t = sqcd_theory(N)
            self.assertEqual(
                t.dim_conformal_manifold - t.voa_parameters, 0,
                f"SU({N}) SQCD should have no parameter reduction"
            )


class TestNecklaceQuiver(unittest.TestCase):
    """Verify necklace quiver theory data."""

    def test_a1_necklace_su2(self):
        """A_hat_1 necklace with 2 SU(2) nodes: dim_CM = 2."""
        t = necklace_quiver_theory(2, 2)
        self.assertEqual(t.dim_conformal_manifold, 2)
        self.assertEqual(t.voa_parameters, 1)

    def test_a2_necklace_su2(self):
        """A_hat_2 necklace with 3 SU(2) nodes: dim_CM = 3."""
        t = necklace_quiver_theory(2, 3)
        self.assertEqual(t.dim_conformal_manifold, 3)
        self.assertEqual(t.voa_parameters, 1)

    def test_necklace_parameter_reduction(self):
        """For r-node necklace: dim_CM - voa_params = r - 1 >= 1."""
        for r in range(2, 5):
            for N in range(2, 5):
                t = necklace_quiver_theory(N, r)
                reduction = t.dim_conformal_manifold - t.voa_parameters
                self.assertEqual(reduction, r - 1,
                                 f"Necklace r={r}, N={N}")

    def test_necklace_central_charge(self):
        """c_2d = -12 c_4d for all necklace theories."""
        for r in range(2, 4):
            for N in range(2, 4):
                t = necklace_quiver_theory(N, r)
                self.assertEqual(t.c_2d, -12 * t.c_anomaly)


class TestClassS(unittest.TestCase):
    """Verify class S theory data."""

    def test_t3_theory(self):
        """T_3 = Minahan-Nemeschansky E_6 theory."""
        t = class_s_theory(3)
        self.assertEqual(t.dim_conformal_manifold, 0)
        self.assertEqual(t.voa_parameters, 0)

    def test_t3_anomalies(self):
        """T_3 (E_6 MN theory): a = 41/24, c = 13/6."""
        t = class_s_theory(3)
        self.assertEqual(t.a_anomaly, Fraction(41, 24))
        self.assertEqual(t.c_anomaly, Fraction(13, 6))
        self.assertEqual(t.c_2d, -12 * Fraction(13, 6))

    def test_class_s_isolated(self):
        """Class S theories T_n are isolated (no conformal manifold)."""
        for n in range(3, 6):
            t = class_s_theory(n)
            self.assertEqual(t.dim_conformal_manifold, 0)

    def test_class_s_requires_n_ge_3(self):
        """T_N requires N >= 3."""
        with self.assertRaises(ValueError):
            class_s_theory(2)

    def test_class_s_shapere_tachikawa(self):
        """Shapere-Tachikawa: 2a - c = (N^2-4)/4 for all T_N."""
        for n in range(3, 8):
            t = class_s_theory(n)
            st = 2 * t.a_anomaly - t.c_anomaly
            expected = Fraction(n * n - 4, 4)
            self.assertEqual(st, expected,
                             f"T_{n}: 2a-c = {st}, expected {expected}")

    def test_class_s_coupling_proved(self):
        """Class S theories are isolated => coupling-independent trivially."""
        for n in range(3, 6):
            t = class_s_theory(n)
            self.assertEqual(t.coupling_independence_status, "proved")


class TestSchurIndex(unittest.TestCase):
    """Verify Schur index computations."""

    def test_su2_nf4_first_terms(self):
        """First terms of SU(2) Nf=4 Schur index."""
        coeffs = schur_index_sqcd_su2_nf4(4)
        self.assertEqual(coeffs[0], Fraction(1))
        self.assertEqual(coeffs[1], Fraction(11))
        self.assertEqual(coeffs[2], Fraction(66))

    def test_coupling_independence_sqcd(self):
        """SQCD Schur index is coupling-independent."""
        for N in range(2, 5):
            t = sqcd_theory(N)
            result = schur_index_coupling_independence_test(t)
            self.assertTrue(result["coupling_independent"])

    def test_coupling_independence_necklace(self):
        """Necklace quiver coupling independence status is 'open'."""
        for r in range(2, 4):
            t = necklace_quiver_theory(2, r)
            result = schur_index_coupling_independence_test(t)
            self.assertEqual(result["coupling_independence_status"], "open")
            self.assertGreater(result["parameter_reduction"], 0)


class TestOPERigidity(unittest.TestCase):
    """Verify OPE rigidity analysis."""

    def test_sl2_km_rigid(self):
        """sl_2 Kac-Moody: rigid up to level."""
        result = ope_rigidity_sl2_km(Fraction(1))
        self.assertTrue(result.is_rigid_up_to_level)
        self.assertEqual(result.effective_free_parameters, 1)

    def test_virasoro_rigid(self):
        """Virasoro: rigid up to c."""
        result = ope_rigidity_virasoro(Fraction(1, 2))
        self.assertTrue(result.is_rigid_up_to_level)
        self.assertEqual(result.effective_free_parameters, 1)

    def test_w3_rigid(self):
        """W_3: rigid up to c."""
        result = ope_rigidity_w3(Fraction(-2))
        self.assertTrue(result.is_rigid_up_to_level)
        self.assertEqual(result.effective_free_parameters, 1)

    def test_wn_rigid(self):
        """W_N: rigid up to c for N = 2, ..., 8."""
        for n in range(2, 9):
            result = ope_rigidity_wn(n, Fraction(0))
            self.assertTrue(result.is_rigid_up_to_level,
                            f"W_{n} should be rigid")
            self.assertEqual(result.effective_free_parameters, 1)


class TestSQCDIdentification(unittest.TestCase):
    """Verify VOA identification for SQCD theories."""

    def test_su2_not_critical(self):
        """SU(2) SQCD: k = -1 for sl_2, not at critical level -2."""
        result = verify_sqcd_voa_identification(2)
        self.assertFalse(result["critical"])
        self.assertEqual(result["level"], Fraction(-1))

    def test_su3_not_critical(self):
        """SU(3) SQCD: k = -3/2 for sl_3, not at critical level -3."""
        result = verify_sqcd_voa_identification(3)
        self.assertFalse(result["critical"])
        self.assertEqual(result["level"], Fraction(-3, 2))

    def test_all_sqcd_one_parameter(self):
        """All SU(N) SQCD VOAs are one-parameter."""
        for N in range(2, 10):
            result = verify_sqcd_voa_identification(N)
            self.assertTrue(result["one_parameter"])

    def test_sqcd_central_charges(self):
        """Central charges for sl_N at k = -N/2."""
        for N in range(2, 7):
            result = verify_sqcd_voa_identification(N)
            # c(sl_N, -N/2) = (-N/2)(N^2-1)/(N/2) = -(N^2-1)
            self.assertEqual(result["c_km"], Fraction(-(N * N - 1)))


class TestConformalManifoldAnalysis(unittest.TestCase):
    """Verify conformal manifold analysis."""

    def test_sqcd_theories_saturated(self):
        """SQCD theories (proved coupling-independence) are scalar-saturated."""
        results = conformal_manifold_analysis()
        sqcd_results = [r for r in results if "SQCD" in r["theory"]]
        for r in sqcd_results:
            self.assertTrue(r["scalar_saturated"],
                            f"{r['theory']} should be saturated")

    def test_necklace_theories_conjectural(self):
        """Necklace quivers have conjectural/open coupling status."""
        results = conformal_manifold_analysis()
        necklace_results = [r for r in results if "necklace" in r["theory"]]
        for r in necklace_results:
            self.assertEqual(r["coupling_status"], "open")

    def test_necklace_has_reduction(self):
        """Necklace quivers have parameter reduction > 0."""
        results = conformal_manifold_analysis()
        necklace_results = [r for r in results if "necklace" in r["theory"]]
        self.assertGreater(len(necklace_results), 0)
        for r in necklace_results:
            self.assertGreater(r["reduction"], 0,
                               f"{r['theory']} should have reduction")


class TestMasterVerification(unittest.TestCase):
    """Master verification that all quiver VOAs are scalar-saturated."""

    def test_all_one_parameter(self):
        """All theories have VOA depending on at most 1 parameter."""
        result = verify_quiver_voa_saturation()
        self.assertTrue(result["all_one_parameter"])
        self.assertEqual(result["max_voa_parameters"], 1)

    def test_significant_sample(self):
        """Sample includes theories with multi-dimensional CM."""
        result = verify_quiver_voa_saturation()
        self.assertGreater(result["max_cm_dimension"], 1)
        self.assertGreater(result["total_theories"], 10)

    def test_parameter_reduction(self):
        """At least some theories have genuine parameter reduction."""
        result = verify_quiver_voa_saturation()
        reduced = [
            t for t in result["theories"]
            if t["has_parameter_reduction"]
        ]
        self.assertGreater(len(reduced), 0)
