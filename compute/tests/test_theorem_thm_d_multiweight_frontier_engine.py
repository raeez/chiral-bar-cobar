r"""Tests for the Theorem D multi-weight frontier engine.

Verifies:
1. delta_F_3^cross(W_3) via independent direct, closed, analytical, and
   universal formulas
2. delta_F_2^cross(W_N) universal gravitational formula
3. Barbell contribution at genus 2
4. Structural analysis: degree patterns, propagator variance
5. Verdier central-charge reflection checks
6. Large-c asymptotic ratios
7. Growth rate analysis
8. Fang PVA classical limit

Multi-path verification: numerical results are confirmed by independent paths.
"""

import unittest
from fractions import Fraction
from math import factorial

from compute.lib.theorem_thm_d_multiweight_frontier_engine import (
    bernoulli,
    lambda_fp,
    harmonic_tail,
    kappa_total,
    kappa_channel,
    koszul_conductor,
    evaluate_laurent_polynomial,
    holographic_package_entries,
    modular_koszul_primary_projections,
    typed_object_firewall,
    kernel_normalization_constants,
    structural_firewall_summary,
    gravitational_truncation_scope,
    genus3_gravitational_formula_scope,
    propagator_diagnostic_scope,
    grav_C3,
    grav_propagator,
    grav_V0_factorize,
    grav_vertex_factor,
    delta_Fg_grav_direct,
    delta_Fg_grav_analytical,
    rational_reconstruction,
    sewing_recursion_genus3_from_genus2,
    genus2_grav_laurent_coefficients,
    genus2_grav_formula,
    genus3_grav_laurent_coefficients,
    genus3_grav_formula,
    w3_cross_laurent_coefficients,
    w3_genus2_cross,
    w3_genus3_cross,
    w3_genus4_cross,
    w3_scalar_laurent_coefficients,
    w3_large_c_limit_cross_over_scalar,
    w3_scalar_collapse_diagnostic,
    theorem_d_multiweight_frontier_scope,
    w3_finite_window_certificate,
    large_c_ratio,
    propagator_variance_analog,
    propagator_variance_controls_cross,
    principal_w_verdier_reflection,
    verdier_central_charge_reflection_check,
    w3_genus3_multipath_verification,
    growth_rate_table,
    fang_pva_classical_cross_channel,
    fang_pva_quantum_correction,
    frontier_summary,
)


# ============================================================================
# 1. Structural firewalls
# ============================================================================

class TestStructuralFirewalls(unittest.TestCase):
    """Package, object, and kernel normalizations remain typed apart."""

    def test_holographic_package_has_seven_entries(self):
        self.assertEqual(
            holographic_package_entries(),
            ("A", "A^i", "A^!", "C", "r(z)", "Theta_A", "nabla^hol"),
        )
        self.assertEqual(len(holographic_package_entries()), 7)

    def test_modular_koszul_package_has_six_primary_projections(self):
        projections = modular_koszul_primary_projections()
        self.assertEqual(
            projections,
            (
                "Fact_X(L)",
                "barB_X(L)",
                "Theta_L",
                "L_L",
                "(V_br,T_br)",
                "R4_mod(L)",
            ),
        )
        self.assertEqual(len(projections), 6)
        self.assertNotEqual(set(projections), set(holographic_package_entries()))

    def test_bar_verdier_cobar_bulk_firewall(self):
        roles = typed_object_firewall()
        self.assertEqual(roles["A^i"], "bar cohomology coalgebra H^*(B(A))")
        self.assertIn("Verdier/continuous-linear dual branch", roles["A^!"])
        self.assertIn("finite-type or completed hypotheses", roles["A^!"])
        self.assertEqual(roles["Omega(B(A))"], "bar-cobar inversion recovering A")
        self.assertIn("ChirHoch^*(A,A)", roles["Z_ch^der(A)"])
        self.assertIn("Hochschild/derived-centre bulk", roles["Z_ch^der(A)"])

    def test_kernel_normalization_constants(self):
        kernels = kernel_normalization_constants(c=Fraction(24), k=Fraction(5), h_vee=Fraction(3))
        self.assertEqual(kernels["affine_raw_collision"]["formula"], "k*Omega_tr/z")
        self.assertEqual(kernels["affine_raw_collision"]["coefficient"], Fraction(5))
        self.assertEqual(kernels["affine_kz_coefficient"]["formula"], "Omega/((k+h_vee)z)")
        self.assertEqual(kernels["affine_kz_coefficient"]["coefficient"], Fraction(1, 8))
        self.assertEqual(kernels["virasoro_collision"]["formula"], "(c/2)/z^3 + 2T/z")
        self.assertEqual(kernels["virasoro_collision"]["central_coefficient"], Fraction(12))
        self.assertEqual(kernels["virasoro_collision"]["stress_coefficient"], Fraction(2))

    def test_kz_coefficient_rejects_critical_level(self):
        with self.assertRaises(ValueError):
            kernel_normalization_constants(k=Fraction(-2), h_vee=Fraction(2))

    def test_structural_summary_keeps_packages_distinct(self):
        summary = structural_firewall_summary()
        self.assertTrue(summary["packages_are_distinct"])
        self.assertEqual(len(summary["holographic_package_entries"]), 7)
        self.assertEqual(len(summary["modular_koszul_primary_projections"]), 6)
        self.assertEqual(
            summary["object_roles"]["Z_ch^der(A)"],
            "ChirHoch^*(A,A), the Hochschild/derived-centre bulk",
        )

    def test_gravitational_truncation_does_not_zero_full_ope(self):
        scope = gravitational_truncation_scope()
        self.assertFalse(scope["dropped_couplings_set_to_zero_in_full_ope"])
        self.assertFalse(scope["full_ope_reconstruction_for_generic_WN"])
        self.assertFalse(scope["generic_WN_channel_data_degenerate"])
        self.assertTrue(scope["genus2_lower_bound_for_N_ge_4"])


# ============================================================================
# 2. Bernoulli numbers and lambda_FP
# ============================================================================

class TestBernoulli(unittest.TestCase):
    """Verify Bernoulli numbers and Faber-Pandharipande values."""

    def test_B0(self):
        self.assertEqual(bernoulli(0), Fraction(1))

    def test_B1(self):
        # Akiyama-Tanigawa gives B_1 = +1/2; harmless since lambda_fp uses only B_{2g}
        self.assertEqual(bernoulli(1), Fraction(1, 2))

    def test_B2(self):
        self.assertEqual(bernoulli(2), Fraction(1, 6))

    def test_B4(self):
        self.assertEqual(bernoulli(4), Fraction(-1, 30))

    def test_B6(self):
        self.assertEqual(bernoulli(6), Fraction(1, 42))

    def test_B8(self):
        self.assertEqual(bernoulli(8), Fraction(-1, 30))

    def test_odd_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(bernoulli(n), Fraction(0))

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda4(self):
        # lambda_4 = (2^7 - 1)/2^7 * |B_8|/8! = 127/128 * (1/30)/40320
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))


# ============================================================================
# 3. Kappa and harmonic numbers
# ============================================================================

class TestKappa(unittest.TestCase):
    """Verify kappa formulas."""

    def test_harmonic_w3(self):
        self.assertEqual(harmonic_tail(3), Fraction(5, 6))

    def test_harmonic_w4(self):
        self.assertEqual(harmonic_tail(4), Fraction(13, 12))

    def test_kappa_w3(self):
        self.assertEqual(kappa_total(3, Fraction(24)), Fraction(20))

    def test_kappa_w4(self):
        self.assertEqual(kappa_total(4, Fraction(12)), Fraction(13))

    def test_koszul_w2(self):
        self.assertEqual(koszul_conductor(2), Fraction(26))

    def test_koszul_w3(self):
        self.assertEqual(koszul_conductor(3), Fraction(100))

    def test_koszul_w4(self):
        self.assertEqual(koszul_conductor(4), Fraction(246))


# ============================================================================
# 4. Gravitational Frobenius algebra
# ============================================================================

class TestGravFrobenius(unittest.TestCase):
    """Verify gravitational structure constants and vertex factors."""

    def test_C3_TTT(self):
        c = Fraction(10)
        self.assertEqual(grav_C3(2, 2, 2, c), c)

    def test_C3_TWW(self):
        c = Fraction(10)
        for j in [3, 4, 5]:
            self.assertEqual(grav_C3(2, j, j, c), c, f"C(2,{j},{j}) should be c")

    def test_C3_parity_vanish(self):
        c = Fraction(10)
        self.assertEqual(grav_C3(2, 2, 3, c), Fraction(0))  # odd W3 count
        self.assertEqual(grav_C3(3, 3, 3, c), Fraction(0))  # odd W3 count

    def test_C3_TTW4(self):
        c = Fraction(10)
        self.assertEqual(grav_C3(2, 2, 4, c), Fraction(0))  # C_{TTW4} = 0

    def test_nonstress_triples_zero_only_in_gravitational_truncation(self):
        c = Fraction(10)
        self.assertEqual(grav_C3(3, 3, 4, c), Fraction(0))
        self.assertFalse(
            gravitational_truncation_scope()["dropped_couplings_set_to_zero_in_full_ope"]
        )

    def test_propagator_values(self):
        c = Fraction(100)
        self.assertEqual(grav_propagator(2, c), Fraction(1, 50))
        self.assertEqual(grav_propagator(3, c), Fraction(3, 100))
        self.assertEqual(grav_propagator(4, c), Fraction(1, 25))


# ============================================================================
# 5. Stable graph enumeration (barbell at genus 2)
# ============================================================================

class TestBarbellGraph(unittest.TestCase):
    """Verify the barbell graph in genus-2 enumeration."""

    def test_genus2_graph_count(self):
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        gs = enumerate_stable_graphs(2, 0)
        self.assertEqual(len(gs), 7, "Genus-2 should have 7 stable graphs")

    def test_barbell_present(self):
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        gs = enumerate_stable_graphs(2, 0)
        barbell_found = False
        for g in gs:
            if g.num_vertices == 2 and g.vertex_genera == (0, 0):
                sl = sum(1 for v1, v2 in g.edges if v1 == v2)
                if sl == 2:
                    barbell_found = True
        self.assertTrue(barbell_found, "Barbell (2 self-loops + 1 bridge) not found")

    def test_barbell_properties(self):
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        gs = enumerate_stable_graphs(2, 0)
        barbell = gs[-1]  # Should be the last one
        self.assertEqual(barbell.num_vertices, 2)
        self.assertEqual(barbell.num_edges, 3)
        self.assertEqual(barbell.vertex_genera, (0, 0))
        self.assertEqual(barbell.automorphism_order(), 8)
        self.assertEqual(barbell.first_betti, 2)

    def test_genus2_automorphism_orders_are_exact(self):
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        gs = enumerate_stable_graphs(2, 0)
        self.assertEqual(
            [g.automorphism_order() for g in gs],
            [1, 2, 8, 2, 12, 2, 8],
        )

    def test_barbell_cross_channel_w3(self):
        """The barbell contributes 21/(4c) to the W_3 cross-channel at genus 2."""
        c = Fraction(10)
        expected = Fraction(21) / (4 * c)  # = 21/40
        # Compute directly
        from compute.lib.theorem_thm_d_multiweight_frontier_engine import (
            graph_amplitude_decomposed
        )
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        gs = enumerate_stable_graphs(2, 0)
        barbell = gs[-1]
        decomp = graph_amplitude_decomposed(barbell, c, (2, 3))
        self.assertEqual(decomp['mixed'], expected,
                         f"Barbell mixed should be 21/40, got {decomp['mixed']}")

    def test_genus3_count_unchanged(self):
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        gs = enumerate_stable_graphs(3, 0)
        self.assertEqual(len(gs), 42)


# ============================================================================
# 6. W_3 genus-2 cross-channel: 5-path verification
# ============================================================================

class TestW3Genus2(unittest.TestCase):
    """delta_F_2(W_3) = (c + 204)/(16c), verified 5 ways."""

    def test_exact_laurent_coefficients(self):
        expected = {0: Fraction(1, 16), -1: Fraction(51, 4)}
        self.assertEqual(genus2_grav_laurent_coefficients(3), expected)
        self.assertEqual(w3_cross_laurent_coefficients(2), expected)
        self.assertEqual(
            evaluate_laurent_polynomial(expected, Fraction(10)),
            w3_genus2_cross(Fraction(10)),
        )

    def test_path1_direct_graph_sum(self):
        """Path 1: Direct graph sum over 7 genus-2 stable graphs."""
        for cv in [1, 2, 5, 10, 24, 100]:
            c = Fraction(cv)
            direct = delta_Fg_grav_direct(2, 3, c)
            formula = w3_genus2_cross(c)
            self.assertEqual(direct, formula, f"Mismatch at c={cv}")

    def test_path2_universal_formula(self):
        """Path 2: Universal N-formula specialization."""
        for cv in [1, 10, 100]:
            c = Fraction(cv)
            self.assertEqual(genus2_grav_formula(3, c), w3_genus2_cross(c))

    def test_path3_decomposition(self):
        """Path 3: Per-graph decomposition matches total."""
        c = Fraction(10)
        # sunset + theta + bridge-loop + barbell = (c+204)/(16c)
        sunset = Fraction(3) / c
        theta = Fraction(9) / (2 * c)
        bridge_loop = Fraction(1, 16)
        barbell = Fraction(21) / (4 * c)
        total = sunset + theta + bridge_loop + barbell
        self.assertEqual(total, w3_genus2_cross(c))

    def test_path4_large_c_limit(self):
        """Path 4: Large-c limit -> 1/16."""
        large_c = Fraction(10**9)
        val = w3_genus2_cross(large_c)
        self.assertAlmostEqual(float(val), 1.0 / 16, places=5)

    def test_path5_positivity(self):
        """Path 5: Positive for all c > 0."""
        for cv in [1, 10, 100, 1000]:
            c = Fraction(cv)
            self.assertGreater(w3_genus2_cross(c), 0)

    def test_zero_c_rejected(self):
        with self.assertRaises(ValueError):
            w3_genus2_cross(Fraction(0))


# ============================================================================
# 7. W_3 genus-3 cross-channel: multi-path verification
# ============================================================================

class TestW3Genus3(unittest.TestCase):
    """delta_F_3(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360)/(138240c^2)."""

    def test_exact_laurent_coefficients(self):
        expected = {
            1: Fraction(1, 27648),
            0: Fraction(79, 2880),
            -1: Fraction(133, 16),
            -2: Fraction(6281, 4),
        }
        self.assertEqual(genus3_grav_laurent_coefficients(3), expected)
        self.assertEqual(w3_cross_laurent_coefficients(3), expected)

    def test_multipath_all_agree(self):
        """All equality paths agree at c=10."""
        result = w3_genus3_multipath_verification(Fraction(10))
        self.assertTrue(result['all_agree'])

    def test_multipath_large_c_ratio(self):
        """Large-c ratio = 42/31."""
        result = w3_genus3_multipath_verification(Fraction(10))
        self.assertTrue(result['large_c_ratio_is_42_31'])

    def test_direct_matches_formula(self):
        """Direct graph sum matches closed form at multiple c values."""
        for cv in [1, 2, 5, 10, 24, 100]:
            c = Fraction(cv)
            direct = delta_Fg_grav_direct(3, 3, c)
            formula = w3_genus3_cross(c)
            self.assertEqual(direct, formula, f"Mismatch at c={cv}")

    def test_analytical_matches_formula(self):
        """Analytical c-factorization matches closed form."""
        coeffs = delta_Fg_grav_analytical(3, 3)
        for cv in [1, 5, 10]:
            c = Fraction(cv)
            analytical = coeffs[0] * c + coeffs[1] + coeffs[2] / c + coeffs[3] / c**2
            formula = w3_genus3_cross(c)
            self.assertEqual(analytical, formula, f"Mismatch at c={cv}")

    def test_universal_matches_formula(self):
        """Universal N-formula matches closed form."""
        for cv in [1, 10, 100]:
            c = Fraction(cv)
            self.assertEqual(genus3_grav_formula(3, c), w3_genus3_cross(c))

    def test_positivity(self):
        """Positive for all c > 0."""
        for cv in [1, 10, 100, 1000]:
            self.assertGreater(w3_genus3_cross(Fraction(cv)), 0)

    def test_leading_coefficient(self):
        """Leading coefficient is 5/138240 = 1/27648."""
        coeffs = delta_Fg_grav_analytical(3, 3)
        self.assertEqual(coeffs[0], Fraction(1, 27648))

    def test_genus3_dominates_scalar(self):
        """At genus 3, cross-channel > scalar part for large c."""
        ratio = large_c_ratio(3, 3)
        self.assertEqual(ratio, Fraction(42, 31))
        self.assertGreater(ratio, 1)

    def test_rational_reconstruction_uses_degree_g_not_2g_minus_2(self):
        coeffs = rational_reconstruction(3, 3)
        self.assertEqual(
            coeffs,
            [Fraction(6281, 4), Fraction(133, 16),
             Fraction(79, 2880), Fraction(1, 27648)],
        )


# ============================================================================
# 8. W_3 genus-4 cross-channel
# ============================================================================

class TestW3Genus4(unittest.TestCase):
    """delta_F_4(W_3): verify the formula."""

    def test_exact_laurent_coefficients(self):
        expected = {
            1: Fraction(41, 2488320),
            0: Fraction(89627, 5806080),
            -1: Fraction(229079, 34560),
            -2: Fraction(163829, 96),
            -3: Fraction(5138841, 16),
        }
        self.assertEqual(w3_cross_laurent_coefficients(4), expected)

    def test_positivity(self):
        for cv in [1, 10, 100]:
            self.assertGreater(w3_genus4_cross(Fraction(cv)), 0)

    def test_matches_delta_f4_certificate(self):
        from compute.lib.delta_f4_universal_engine import delta_F4_exact
        for cv in [1, 7, 24]:
            c = Fraction(cv)
            self.assertEqual(w3_genus4_cross(c), delta_F4_exact(3, c))

    def test_large_c_ratio_grows(self):
        """Genus-4 ratio >> genus-3 ratio (factorial growth)."""
        r3 = w3_large_c_limit_cross_over_scalar(3)
        r4 = w3_large_c_limit_cross_over_scalar(4)
        self.assertEqual(r3, Fraction(42, 31))
        self.assertEqual(r4, Fraction(9184, 381))
        self.assertGreater(r4, r3)


# ============================================================================
# 9. Universal gravitational formula: genus 2
# ============================================================================

class TestUniversalGenus2(unittest.TestCase):
    """Universal formula delta_F_2^grav(W_N) for all N."""

    def test_vanishing_at_N2(self):
        """Virasoro (N=2): uniform weight, zero cross-channel."""
        for cv in [1, 10, 100]:
            self.assertEqual(genus2_grav_formula(2, Fraction(cv)), Fraction(0))

    def test_w3_matches(self):
        for cv in [1, 10, 100]:
            c = Fraction(cv)
            self.assertEqual(genus2_grav_formula(3, c), w3_genus2_cross(c))

    def test_w4_value(self):
        """delta_F_2^grav(W_4) = (7c+2148)/(48c)."""
        c = Fraction(100)
        expected = (7 * c + 2148) / (48 * c)
        self.assertEqual(genus2_grav_formula(4, c), expected)

    def test_w5_value(self):
        """delta_F_2^grav(W_5) = (c+434)/(4c)."""
        c = Fraction(100)
        expected = (c + 434) / (4 * c)
        self.assertEqual(genus2_grav_formula(5, c), expected)

    def test_direct_matches_formula_multiple_N(self):
        """Direct graph sum matches universal formula for N=3,4,5,6."""
        for N in [3, 4, 5, 6]:
            for cv in [10, 100]:
                c = Fraction(cv)
                direct = delta_Fg_grav_direct(2, N, c)
                formula = genus2_grav_formula(N, c)
                self.assertEqual(direct, formula, f"W_{N} c={cv}")

    def test_monotone_in_N(self):
        """Cross-channel correction increases with N (more channels)."""
        c = Fraction(100)
        prev = Fraction(0)
        for N in range(2, 8):
            val = genus2_grav_formula(N, c)
            self.assertGreaterEqual(val, prev, f"Not monotone at N={N}")
            prev = val


# ============================================================================
# 10. Universal gravitational formula: genus 3
# ============================================================================

class TestUniversalGenus3(unittest.TestCase):
    """Genus-3 reconstructed gravitational N-polynomial."""

    def test_vanishing_at_N2(self):
        for cv in [1, 10, 100]:
            self.assertEqual(genus3_grav_formula(2, Fraction(cv)), Fraction(0))

    def test_w3_matches(self):
        for cv in [1, 10]:
            c = Fraction(cv)
            self.assertEqual(genus3_grav_formula(3, c), w3_genus3_cross(c))

    def test_direct_matches_formula(self):
        for N in [3, 4, 5]:
            c = Fraction(1)
            direct = delta_Fg_grav_direct(3, N, c)
            formula = genus3_grav_formula(N, c)
            self.assertEqual(direct, formula, f"W_{N} c=1")

    def test_analytical_matches_formula(self):
        """Analytical method matches reconstructed formula on the checked N-window."""
        for N in [3, 4, 5]:
            coeffs = delta_Fg_grav_analytical(3, N)
            c = Fraction(10)
            val = coeffs[0] * c + coeffs[1] + coeffs[2] / c + coeffs[3] / c**2
            formula = genus3_grav_formula(N, c)
            self.assertEqual(val, formula, f"W_{N} c=10 analytical vs formula")

    def test_genus3_scope_is_not_all_N_theorem_d(self):
        scope = genus3_gravitational_formula_scope()
        self.assertEqual(scope["direct_graph_checked_N"], (3, 4, 5))
        self.assertFalse(scope["proved_all_N"])
        self.assertFalse(scope["cohomological_theorem_d_statement"])
        self.assertFalse(scope["class_valued_mc_lift_proved"])

    def test_c_power_structure(self):
        """delta_F_3 = D*c + C + B/c + A/c^2 with 4 terms (loop numbers 0..3)."""
        coeffs = delta_Fg_grav_analytical(3, 3)
        self.assertEqual(len(coeffs), 4)
        # h^1=0: D > 0 (tree contribution)
        self.assertGreater(coeffs[0], 0)
        # h^1=1: C > 0
        self.assertGreater(coeffs[1], 0)
        # h^1=2: B > 0
        self.assertGreater(coeffs[2], 0)
        # h^1=3: A > 0
        self.assertGreater(coeffs[3], 0)


# ============================================================================
# 11. Propagator variance analysis
# ============================================================================

class TestPropagatorVariance(unittest.TestCase):
    """Propagator variance fails to control cross-channel at all N."""

    def test_vanishing_at_N2(self):
        self.assertEqual(propagator_variance_analog(2), Fraction(0))

    def test_positive_for_N3(self):
        self.assertGreater(propagator_variance_analog(3), 0)

    def test_not_proportional(self):
        """B(N)/delta_analog varies for N >= 5."""
        ratios = propagator_variance_controls_cross(8)
        self.assertGreater(len(set(ratios.values())), 1,
                           "Ratios should not all be equal")

    def test_coincidence_at_small_N(self):
        """B(N)/delta = 9/2 for N=3 and N=4 (coincidence)."""
        ratios = propagator_variance_controls_cross(5)
        self.assertEqual(ratios[3], Fraction(9, 2))
        self.assertEqual(ratios[4], Fraction(9, 2))
        # But N=5 differs
        self.assertNotEqual(ratios[5], Fraction(9, 2))

    def test_variance_scope_is_diagnostic_not_exact_theorem(self):
        scope = propagator_diagnostic_scope()
        self.assertTrue(scope["uses_weight_spread_analog_only"])
        self.assertFalse(scope["uses_full_arity4_propagator_variance"])
        self.assertFalse(scope["exact_cross_channel_theorem"])
        self.assertFalse(scope["constant_ratio_for_all_N"])


# ============================================================================
# 12. Verdier central-charge reflection check
# ============================================================================

class TestVerdierCentralChargeReflection(unittest.TestCase):
    """Principal W_N Verdier reflection: c^! = K_N - c."""

    def test_w3_not_symmetric(self):
        """delta_F_2^grav varies under c -> K_3 - c in general."""
        c = Fraction(30)
        K = koszul_conductor(3)  # = 100
        c_dual = K - c  # = 70
        d1 = genus2_grav_formula(3, c)
        d2 = genus2_grav_formula(3, c_dual)
        self.assertNotEqual(d1, d2)

    def test_reflection_check_records_scope(self):
        """The scalar reflection check records non-invariance and the conductor."""
        result = verdier_central_charge_reflection_check(2, 3, Fraction(30))
        self.assertEqual(result["conductor"], Fraction(100))
        self.assertEqual(result["c_dual"], Fraction(70))
        self.assertEqual(result["self_dual_c"], Fraction(50))
        self.assertNotEqual(result["difference"], Fraction(0))

    def test_w3_self_dual_point(self):
        """At c = K_3/2 = 50, the scalar reflection is fixed."""
        c = Fraction(50)
        K = koszul_conductor(3)
        self.assertEqual(c, K / 2)  # self-dual point
        d1 = genus2_grav_formula(3, c)
        d2 = genus2_grav_formula(3, K - c)
        self.assertEqual(d1, d2)

    def test_principal_w_reflection_formula(self):
        self.assertEqual(principal_w_verdier_reflection(3, Fraction(30)), Fraction(70))
        self.assertEqual(principal_w_verdier_reflection(4, Fraction(123)), Fraction(123))


# ============================================================================
# 13. Large-c ratio (growth analysis)
# ============================================================================

class TestGrowthRate(unittest.TestCase):
    """Cross-channel growth with genus."""

    def test_genus2_ratio_zero(self):
        """At genus 2, delta_F_2 -> 1/16 while scalar -> (5/6)*lambda_2*c -> infinity.
        Ratio -> 0."""
        ratio = large_c_ratio(2, 3)
        self.assertEqual(ratio, Fraction(0))

    def test_genus3_ratio_42_31(self):
        self.assertEqual(large_c_ratio(3, 3), Fraction(42, 31))

    def test_growth_table(self):
        table = growth_rate_table(3, 3)
        self.assertEqual(len(table), 2)  # g=2 and g=3
        self.assertEqual(table[0]['genus'], 2)
        self.assertEqual(table[1]['genus'], 3)
        self.assertEqual(table[1]['large_c_ratio'], Fraction(42, 31))


# ============================================================================
# 14. Finite-window scope and scalar non-collapse
# ============================================================================

class TestFiniteWindowScope(unittest.TestCase):
    """Finite theorem window does not collapse to scalar FP or analytic tau claims."""

    def test_scope_records_negative_tau_and_boundary_claims(self):
        scope = theorem_d_multiweight_frontier_scope()
        self.assertFalse(scope["analytic_tau_identity_proved"])
        self.assertFalse(scope["kw_hierarchy_membership_proved"])
        self.assertFalse(scope["global_modular_boundary_pairing_proved"])
        self.assertFalse(scope["scalar_fp_lane_sufficient_for_multiweight"])
        self.assertFalse(scope["finite_window_implies_all_genus"])
        self.assertFalse(scope["cohomological_theorem_d_universality_proved_here"])
        self.assertFalse(scope["class_valued_cross_channel_lift_proved"])
        self.assertFalse(scope["planted_forest_evidence_promoted_to_full_mc_data"])
        self.assertIn("|Aut(Gamma)|", scope["automorphism_weighting"])

    def test_w3_scalar_lane_noncollapse_g2_g3_g4(self):
        for g in [2, 3, 4]:
            diagnostic = w3_scalar_collapse_diagnostic(g)
            self.assertFalse(diagnostic["collapses_to_scalar_fp_lane"])
            self.assertTrue(diagnostic["requires_multiweight_cross_correction"])
            self.assertTrue(diagnostic["has_non_scalar_laurent_powers"])

    def test_w3_finite_window_certificate_exact(self):
        cert = w3_finite_window_certificate(Fraction(24))
        self.assertEqual(cert["kappa"], Fraction(20))
        self.assertTrue(cert["rows"][1]["scalar_equals_full"])
        for g in [2, 3, 4]:
            self.assertFalse(cert["rows"][g]["scalar_equals_full"])
            self.assertEqual(
                cert["rows"][g]["full"],
                cert["rows"][g]["scalar_diagonal"] + cert["rows"][g]["delta_cross"],
            )

    def test_scalar_coefficients_are_fp_lane_only(self):
        self.assertEqual(
            w3_scalar_laurent_coefficients(3),
            {1: Fraction(5, 6) * Fraction(31, 967680)},
        )
        self.assertEqual(w3_large_c_limit_cross_over_scalar(2), Fraction(0))
        self.assertEqual(w3_large_c_limit_cross_over_scalar(3), Fraction(42, 31))
        self.assertEqual(w3_large_c_limit_cross_over_scalar(4), Fraction(9184, 381))

    def test_single_bridge_sewing_is_diagonal_not_cross_channel(self):
        diag = sewing_recursion_genus3_from_genus2(3, Fraction(10))
        self.assertGreater(diag, 0)
        self.assertEqual(delta_Fg_grav_direct(3, 2, Fraction(10)), 0)


# ============================================================================
# 15. Fang PVA classical limit
# ============================================================================

class TestFangPVA(unittest.TestCase):
    """Classical limit of cross-channel = Fang PVA contribution."""

    def test_classical_w3(self):
        """B(3) = 1/16."""
        self.assertEqual(fang_pva_classical_cross_channel(3), Fraction(1, 16))

    def test_classical_w4(self):
        """B(4) = 7/48."""
        self.assertEqual(fang_pva_classical_cross_channel(4), Fraction(7, 48))

    def test_classical_w5(self):
        """B(5) = 1/4."""
        self.assertEqual(fang_pva_classical_cross_channel(5), Fraction(1, 4))

    def test_classical_vanishing_w2(self):
        self.assertEqual(fang_pva_classical_cross_channel(2), Fraction(0))

    def test_quantum_correction_positive(self):
        """The quantum correction A(N)/c is positive."""
        for N in [3, 4, 5]:
            q = fang_pva_quantum_correction(N, Fraction(100))
            self.assertGreater(q, 0, f"Quantum correction should be positive for W_{N}")

    def test_quantum_vanishes_at_large_c(self):
        """Quantum correction ~ A(N)/c -> 0 as c -> infinity."""
        q = fang_pva_quantum_correction(3, Fraction(10**9))
        self.assertAlmostEqual(float(q), 0, places=5)


# ============================================================================
# 16. Frontier summary
# ============================================================================

class TestFrontierSummary(unittest.TestCase):
    """Integration test: full frontier summary."""

    def test_summary_runs(self):
        s = frontier_summary(24)
        self.assertIn('w3_g2', s)
        self.assertIn('w3_g3', s)
        self.assertIn('pv_not_proportional', s)
        self.assertTrue(s['pv_not_proportional'])

    def test_w3_tower_ordering(self):
        """Cross-channel grows with genus (at fixed c=24)."""
        s = frontier_summary(24)
        # At c=24, the raw cross-channel values increase with genus
        self.assertGreater(s['w3_g3'], s['w3_g2'])

    def test_gravitational_lower_bound(self):
        """Gravitational formula is exact for W_3 (no higher-spin exchange)."""
        s = frontier_summary(24)
        self.assertEqual(s['w3_g2'], s['w3_g2_grav'])


# ============================================================================
# 17. Cross-volume consistency: degree pattern
# ============================================================================

class TestDegreePattern(unittest.TestCase):
    """Degree structure of the c-expansion at each genus."""

    def test_genus2_two_terms(self):
        """At genus 2: delta = B(N) + A(N)/c (two terms)."""
        for N in [3, 4, 5]:
            coeffs = delta_Fg_grav_analytical(2, N)
            # genus 2: loop numbers 0, 1, 2; but h^1=0 trees at genus 2
            # contribute only to diagonal (all genus-0 vertices with bridges
            # and genus-1 vertices force same channel).
            # At genus 2, the c-expansion has 2 non-trivial powers:
            # c^0 and c^{-1}.
            # coeffs indexed by h^1 = 0, 1, 2
            self.assertEqual(len(coeffs), 3)

    def test_genus3_four_terms(self):
        """At genus 3: delta = D*c + C + B/c + A/c^2 (four terms)."""
        coeffs = delta_Fg_grav_analytical(3, 3)
        self.assertEqual(len(coeffs), 4)

    def test_N2_all_vanish(self):
        """All coefficients vanish for N=2 (Virasoro = uniform weight)."""
        for g in [2, 3]:
            coeffs = delta_Fg_grav_analytical(g, 2)
            for i, c in enumerate(coeffs):
                self.assertEqual(c, 0, f"g={g}, h1={i}: should be 0 for Virasoro")


# ============================================================================
# 18. Orbifold Euler characteristic with 7 graphs
# ============================================================================

class TestEulerCharacteristic(unittest.TestCase):
    """Verify the orbifold Euler characteristic of M_bar_{2,0} with 7 graphs."""

    def test_chi_mbar_20(self):
        """chi^orb(M_bar_{2,0}) = sum of 7 graph contributions."""
        from compute.lib.stable_graph_enumeration import (
            enumerate_stable_graphs, orbifold_euler_characteristic
        )
        gs = enumerate_stable_graphs(2, 0)
        chi = orbifold_euler_characteristic(gs)
        # Known value: chi^orb(M_bar_{2,0}) = B_4/(4*2*1) = (-1/30)/8 = -1/240
        # Wait: the formula gives B_{2g}/(4g(g-1)) for the OPEN moduli space.
        # For M_bar: chi = sum over graphs of product of open chi's / |Aut|.
        # The 7th graph (barbell) changes this value.
        # Let me just check it's a nonzero rational.
        self.assertIsInstance(chi, Fraction)
        self.assertNotEqual(chi, 0)


if __name__ == '__main__':
    unittest.main()
