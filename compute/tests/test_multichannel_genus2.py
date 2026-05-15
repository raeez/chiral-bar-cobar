r"""Tests for the finite W3 two-channel genus-2 boundary engine.

The tests verify exact arithmetic and typed firewalls.  They do not
upgrade the finite boundary model to a proof of full W3 CohFT
universality.
"""

from fractions import Fraction
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from multichannel_genus2 import (
    C3,
    _lambda_fp,
    associator_3d,
    barbell_mixed_amplitude,
    compute_delta_F2_numerical,
    delta_F2_rational,
    euler_field_eigenvalue,
    euler_eigenvalues_3d,
    faber_pandharipande,
    frobenius_3d_metric,
    frobenius_3d_multiplication_matrix_T,
    frobenius_mult,
    gamma1_all_channels,
    gamma2_all_channels,
    gamma2_mixed_amplitude,
    gamma3_all_channels,
    gamma4_all_channels,
    gamma4_mixed_amplitude,
    gamma5_all_channels,
    gamma5_mixed_amplitude,
    gamma7_all_channels,
    genus2_boundary_sum,
    genus2_cross_channel_banana,
    genus2_cross_channel_corrections,
    genus2_graph_catalogue,
    genus2_per_channel_sum,
    holographic_package_entries,
    is_truncated_product_associative,
    kappa_T,
    kappa_W,
    kappa_total,
    kernel_normalizations,
    metric,
    modular_koszul_primary_projections,
    object_firewall,
    product_3d,
    propagator,
    teleman_reconstruction_check,
    vertex_g0_4pt,
    vertex_g1_1pt,
    vertex_g1_2pt,
)


C_VALUES = (
    Fraction(1),
    Fraction(2),
    Fraction(13),
    Fraction(26),
    Fraction(50),
    Fraction(100),
)


class TestPackageFirewalls(unittest.TestCase):
    def test_holographic_and_compute_packages_are_distinct(self):
        self.assertEqual(
            holographic_package_entries(),
            ("A", "A^i", "A^!", "C", "r(z)", "Theta_A", "nabla^hol"),
        )
        projections = modular_koszul_primary_projections()
        self.assertEqual(len(projections), 6)
        self.assertNotEqual(projections, holographic_package_entries())

    def test_object_firewall(self):
        firewall = object_firewall()
        self.assertIn("ordered bar coalgebra", firewall["B(A)"])
        self.assertIn("H^*(B(A))", firewall["A^i"])
        self.assertIn("Verdier/continuous-linear dual branch", firewall["A^!"])
        self.assertIn("inversion recovering A", firewall["Omega(B(A))"])
        self.assertIn("ChirHoch^*(A,A)", firewall["Z_ch^der(A)"])

    def test_kernel_normalizations(self):
        kernels = kernel_normalizations()
        self.assertEqual(kernels["affine_raw_collision"], "k*Omega_tr/z")
        self.assertEqual(kernels["affine_KZ_coefficient"], "Omega/((k+h^vee)z)")
        self.assertEqual(kernels["heisenberg_raw_collision"], "k/z")
        self.assertEqual(kernels["virasoro_collision"], "(c/2)/z^3 + 2T/z")


class TestKappaMetricAndCubicData(unittest.TestCase):
    def test_kappa_values(self):
        for c in C_VALUES:
            self.assertEqual(kappa_T(c), c / 2)
            self.assertEqual(kappa_W(c), c / 3)
            self.assertEqual(kappa_total(c), Fraction(5) * c / 6)
            self.assertEqual(kappa_T(c) + kappa_W(c), kappa_total(c))

    def test_metric_and_propagator_inverse(self):
        for c in C_VALUES:
            self.assertEqual(metric("T", c), c / 2)
            self.assertEqual(metric("W", c), c / 3)
            for channel in ("T", "W"):
                self.assertEqual(metric(channel, c) * propagator(channel, c), 1)

    def test_invalid_channel(self):
        with self.assertRaises(ValueError):
            propagator("X", Fraction(26))

    def test_cubic_constants(self):
        for c in C_VALUES:
            self.assertEqual(C3("T", "T", "T", c), c)
            self.assertEqual(C3("T", "W", "W", c), c)
            self.assertEqual(C3("W", "T", "W", c), c)
            self.assertEqual(C3("T", "T", "W", c), 0)
            self.assertEqual(C3("W", "W", "W", c), 0)

    def test_truncated_primary_product(self):
        c = Fraction(26)
        self.assertEqual(frobenius_mult("T", "T", c), {"T": Fraction(2), "W": 0})
        self.assertEqual(frobenius_mult("T", "W", c), {"T": 0, "W": Fraction(3)})
        self.assertEqual(frobenius_mult("W", "W", c), {"T": Fraction(2), "W": 0})
        self.assertEqual(euler_field_eigenvalue("T"), 2)
        self.assertEqual(euler_field_eigenvalue("W"), 3)


class TestTruncatedProductObstruction(unittest.TestCase):
    def test_vacuum_TW_table(self):
        c = Fraction(26)
        self.assertEqual(product_3d("T", "T", c), {"1": Fraction(13), "T": 2})
        self.assertEqual(product_3d("T", "W", c), {"W": 3})
        self.assertEqual(product_3d("W", "W", c), {"1": Fraction(26, 3), "T": 2})

    def test_associator_blocks_teleman_for_generic_c(self):
        c = Fraction(26)
        self.assertEqual(associator_3d("T", "T", "W", c), {"W": Fraction(10)})
        self.assertFalse(is_truncated_product_associative(c))

    def test_exceptional_c6_associator_check(self):
        self.assertEqual(associator_3d("T", "T", "W", Fraction(6)), {})
        self.assertTrue(is_truncated_product_associative(Fraction(6)))

    def test_3d_matrix_and_eigenvalue_data(self):
        c = Fraction(26)
        self.assertEqual(
            frobenius_3d_multiplication_matrix_T(c),
            [[0, 13, 0], [1, 2, 0], [0, 0, 3]],
        )
        self.assertEqual(frobenius_3d_metric(c), [[1, 0, 0], [0, 13, 0], [0, 0, Fraction(26, 3)]])
        self.assertEqual(euler_eigenvalues_3d(c), (Fraction(3), Fraction(14)))


class TestFaberPandharipande(unittest.TestCase):
    def test_low_genus_values(self):
        self.assertEqual(_lambda_fp(1), Fraction(1, 24))
        self.assertEqual(_lambda_fp(2), Fraction(7, 5760))
        self.assertEqual(_lambda_fp(3), Fraction(31, 967680))

    def test_external_or_fallback_matches_local(self):
        self.assertEqual(faber_pandharipande(2), _lambda_fp(2))


class TestGraphCatalogue(unittest.TestCase):
    def test_catalogue_has_seven_stable_graphs(self):
        graphs = genus2_graph_catalogue()
        self.assertEqual(len(graphs), 7)
        self.assertTrue(all(graph.stable() for graph in graphs))
        self.assertTrue(all(graph.arithmetic_genus == 2 for graph in graphs))

    def test_barbell_metadata(self):
        barbell = [graph for graph in genus2_graph_catalogue() if graph.key == "Gamma_7"][0]
        self.assertEqual(barbell.name, "barbell")
        self.assertEqual(barbell.edges, 3)
        self.assertEqual(barbell.aut_order, 8)


class TestVertexNormalizations(unittest.TestCase):
    def test_genus0_four_point_s_channel(self):
        c = Fraction(26)
        for left in ("T", "W"):
            for right in ("T", "W"):
                self.assertEqual(vertex_g0_4pt(left, left, right, right, c), 2 * c)
        self.assertEqual(vertex_g0_4pt("T", "T", "T", "W", c), 0)

    def test_genus1_vertex_normalizations(self):
        c = Fraction(26)
        self.assertEqual(vertex_g1_2pt("T", "T", c), Fraction(13, 24))
        self.assertEqual(vertex_g1_2pt("W", "W", c), Fraction(26, 72))
        self.assertEqual(vertex_g1_2pt("T", "W", c), 0)
        self.assertEqual(vertex_g1_1pt("T", c), Fraction(13, 24))
        self.assertEqual(vertex_g1_1pt("W", c), Fraction(26, 72))


class TestBoundaryGraphAmplitudes(unittest.TestCase):
    def test_individual_graph_values_at_c26(self):
        c = Fraction(26)
        self.assertEqual(gamma1_all_channels(c), Fraction(1, 24))
        self.assertEqual(gamma2_all_channels(c), Fraction(25, 104))
        self.assertEqual(gamma3_all_channels(c), Fraction(65, 3456))
        self.assertEqual(gamma4_all_channels(c), Fraction(31, 156))
        self.assertEqual(gamma5_all_channels(c), Fraction(5, 48))
        self.assertEqual(gamma7_all_channels(c), Fraction(25, 104))

    def test_boundary_sum_includes_barbell(self):
        c = Fraction(26)
        result = genus2_boundary_sum(c)
        for key in ("Gamma_1", "Gamma_2", "Gamma_3", "Gamma_4", "Gamma_5", "Gamma_7"):
            self.assertIn(key, result)
        self.assertEqual(result["boundary_sum"], sum(result[key] for key in result if key != "boundary_sum"))


class TestCrossChannelCorrections(unittest.TestCase):
    def test_exact_mixed_graph_constants(self):
        for c in C_VALUES:
            self.assertEqual(gamma2_mixed_amplitude(c), Fraction(3, c))
            self.assertEqual(gamma4_mixed_amplitude(c), Fraction(9, 2 * c))
            self.assertEqual(gamma5_mixed_amplitude(c), Fraction(1, 16))
            self.assertEqual(barbell_mixed_amplitude(c), Fraction(21, 4 * c))

    def test_total_cross_channel_formula(self):
        for c in C_VALUES:
            corrections = genus2_cross_channel_corrections(c)
            self.assertEqual(corrections["delta_total"], Fraction(c + 204, 16 * c))
            self.assertEqual(delta_F2_rational(c), Fraction(c + 204, 16 * c))

    def test_cross_channel_wrapper_status(self):
        result = genus2_cross_channel_banana(Fraction(26))
        self.assertFalse(result["universality_holds"])
        self.assertEqual(result["delta_cross_channel"], Fraction(115, 208))
        self.assertIn("finite boundary correction", result["status"])


class TestSectorFormulaAndTelemanStatus(unittest.TestCase):
    def test_per_channel_sector_sum(self):
        for c in C_VALUES:
            result = genus2_per_channel_sum(c)
            self.assertEqual(result["F2_T"] + result["F2_W"], result["F2_per_channel"])
            self.assertEqual(result["F2_per_channel"], result["kappa_times_fp2"])

    def test_sector_formula_is_not_full_graph_computation(self):
        result = compute_delta_F2_numerical(Fraction(26))
        self.assertTrue(result["sector_formula_matches_universal"])
        self.assertEqual(result["delta_sector_sum"], 0)
        self.assertIsNone(result["delta_F2"])
        self.assertIsNone(result["universality_holds"])
        self.assertFalse(result["full_cohft_universality_proved"])

    def test_teleman_reconstruction_status(self):
        result = teleman_reconstruction_check(Fraction(26))
        self.assertFalse(result["frobenius_closed"])
        self.assertFalse(result["teleman_applicable_to_truncation"])
        self.assertIsNone(result["match"])
        self.assertEqual(result["open_obligation"], "compute full R-matrix/idempotent CohFT graph data")


if __name__ == "__main__":
    unittest.main()
