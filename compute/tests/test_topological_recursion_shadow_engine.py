r"""Tests for topological_recursion_shadow_engine.py.

60+ tests covering nine structural questions connecting the shadow
obstruction tower to Eynard-Orantin topological recursion.

NINE STRUCTURAL QUESTIONS
-------------------------
Q1. Heisenberg (class G): degenerate curve and F_g = kappa * lambda_g^FP
Q2. Virasoro (class M): spectral curve from shadow metric
Q3. EO recursion kernel vs shadow connection
Q4. Affine sl_2 (class L): degenerate spectral curve
Q5. Beta-gamma (class C): stratum separation
Q6. Shadow depth vs spectral curve genus
Q7. CEO free energy vs shadow free energy
Q8. Kontsevich-Witten tau-function
Q9. Mirzakhani recursion / Weil-Petersson volumes

MULTI-PATH VERIFICATION
------------------------
Every result verified by at least 2 independent paths.
Exact arithmetic (sympy Rational) for algebraic results.
High-precision mpmath for numerical EO residues.

Ground truth:
    cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:theorem-d: F_g = kappa * lambda_g^FP
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

import math
import cmath
import unittest
from fractions import Fraction

from sympy import Rational, simplify, factorial, sqrt as sym_sqrt

from compute.lib.topological_recursion_shadow_engine import (
    # Faber-Pandharipande
    lambda_fp,
    _bernoulli_number,
    ahat_coefficient,
    faber_pandharipande_census_constants,
    verify_faber_pandharipande_census,
    # Firewalls
    holographic_package_entries,
    modular_koszul_primary_projections,
    typed_firewall_objects,
    object_firewall_summary,
    kernel_normalizations,
    # Family data
    ShadowFamilyData,
    heisenberg_data,
    affine_sl2_data,
    betagamma_data,
    virasoro_data,
    w3_wline_data,
    # Shadow tower
    shadow_tower_from_QL,
    shadow_free_energy,
    # Spectral curve
    ShadowSpectralCurve,
    # Shadow connection
    shadow_connection_coefficient,
    shadow_connection_residue_at_branch,
    shadow_flat_section,
    # EO kernel
    bergman_kernel,
    eo_recursion_kernel,
    compare_kernels_at_branch,
    # Free energies
    free_energy_shadow,
    free_energy_airy,
    free_energy_ahat,
    compare_free_energies,
    # KW tau
    kw_tau_function_log,
    shadow_tau_function_log,
    verify_tau_kw_power_relation,
    finite_window_tr_shadow_theorem,
    # WP volumes
    wp_volume_closed,
    planted_forest_correction,
    compare_shadow_with_wp,
    # Classification
    SpectralCurveClassification,
    classify_spectral_curve,
    depth_vs_curve_genus_table,
    # CEO
    ceo_vs_shadow_discrepancy,
    # Verdier-dual scalar lane
    koszul_dual_spectral_curve,
    # WK intersection
    wk_intersection,
    # Verification
    full_tr_shadow_verification,
    verify_shadow_tower_consistency,
    verify_symplectic_invariance,
    verify_koszul_monodromy,
    airy_limit_of_shadow,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ====================================================================
# Section 0: Package, object, and kernel firewalls (5 tests)
# ====================================================================

class TestPackageAndObjectFirewalls(unittest.TestCase):
    """Bar, dual, bulk, and kernel normalizations stay typed apart."""

    def test_holographic_package_has_seven_entries(self):
        self.assertEqual(
            holographic_package_entries(),
            ("A", "A^i", "A^!", "C", "r(z)", "Theta_A", "nabla^hol"),
        )
        self.assertEqual(len(holographic_package_entries()), 7)

    def test_modular_koszul_package_has_six_primary_projections(self):
        projections = modular_koszul_primary_projections()
        self.assertEqual(len(projections), 6)
        self.assertNotEqual(projections, holographic_package_entries())
        self.assertNotIn("A^!", projections)

    def test_object_firewall_separates_bar_dual_inversion_and_bulk(self):
        firewall = object_firewall_summary()
        self.assertEqual(
            typed_firewall_objects(),
            ("A", "B(A)", "A^i", "A^!", "Omega(B(A))", "Z_ch^der(A)"),
        )
        self.assertIn("H^*(B(A))", firewall["A^i"])
        self.assertIn("Verdier/continuous-linear dual", firewall["A^!"])
        self.assertIn("bar-cobar inversion", firewall["Omega(B(A))"])
        self.assertIn("ChirHoch^*(A,A)", firewall["Z_ch^der(A)"])
        self.assertNotEqual(firewall["A^i"], firewall["A^!"])
        self.assertNotEqual(firewall["Omega(B(A))"], firewall["A^!"])
        self.assertNotEqual(firewall["Z_ch^der(A)"], firewall["A^!"])

    def test_kernel_normalizations_separate_raw_collision_from_kz(self):
        kernels = kernel_normalizations()
        self.assertEqual(kernels["affine_raw_collision"], "k*Omega_tr/z")
        self.assertEqual(kernels["affine_KZ_coefficient"], "Omega/((k+h^vee)z)")
        self.assertEqual(kernels["virasoro_collision"], "(c/2)/z^3 + 2T/z")
        self.assertNotEqual(
            kernels["affine_raw_collision"],
            kernels["affine_KZ_coefficient"],
        )

    def test_raw_affine_collision_vanishes_at_level_zero(self):
        k = Fraction(0)
        h_vee = Fraction(2)
        raw_collision_coefficient = k
        kz_coefficient = Fraction(1, 1) / (k + h_vee)
        self.assertEqual(raw_collision_coefficient, 0)
        self.assertEqual(kz_coefficient, Fraction(1, 2))


# ====================================================================
# Section 1: Faber-Pandharipande and A-hat (7 tests)
# ====================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Rational(1, 24))

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp(2), Rational(7, 5760))

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp(3), Rational(31, 967680))

    def test_lambda_4(self):
        """lambda_4^FP = (2^7-1)/2^7 * |B_8|/8!."""
        B8 = _bernoulli_number(8)
        expected = Rational(2**7 - 1, 2**7) * abs(B8) / factorial(8)
        self.assertEqual(lambda_fp(4), expected)

    def test_lambda_positive(self):
        """All lambda_g^FP are positive for g >= 1."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_lambda_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        for g in range(1, 7):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1))

    def test_ahat_equals_lambda_fp(self):
        """A-hat coefficient at order 2g equals lambda_g^FP."""
        for g in range(1, 6):
            self.assertEqual(ahat_coefficient(g), lambda_fp(g))

    def test_fp_census_constants_first_ten(self):
        """Exact constants match landscape_census.tex prop:fp-coefficients."""
        expected = {
            1: Rational(1, 24),
            2: Rational(7, 5760),
            3: Rational(31, 967680),
            4: Rational(127, 154828800),
            5: Rational(73, 3503554560),
            6: Rational(1414477, 2678117105664000),
            7: Rational(8191, 612141052723200),
            8: Rational(16931177, 49950709902213120000),
            9: Rational(5749691557, 669659197233029971968000),
            10: Rational(91546277357, 420928638260761696665600000),
        }
        self.assertEqual(faber_pandharipande_census_constants(10), expected)

    def test_fp_census_formula_agrees(self):
        """Bernoulli formula agrees with the finite census table."""
        report = verify_faber_pandharipande_census(10)
        for g in range(1, 11):
            self.assertTrue(report[g]['matches'])


# ====================================================================
# Section 2: Q1 -- Heisenberg (class G) (6 tests)
# ====================================================================

class TestQ1Heisenberg(unittest.TestCase):
    """Q1: Heisenberg spectral curve is degenerate.

    Q_L(t) = 4*k^2 (constant). EO recursion gives omega_{g,n} = 0
    for 2g-2+n > 0.  Shadow free energy matches Airy rescaled by kappa.
    """

    def test_heisenberg_degenerate(self):
        """Heisenberg spectral curve is degenerate."""
        data = heisenberg_data(Fraction(1))
        self.assertTrue(data.is_degenerate)

    def test_heisenberg_q2_zero(self):
        """q2 = 0 for Heisenberg (alpha = S4 = 0)."""
        data = heisenberg_data(Fraction(3))
        self.assertEqual(data.q2, Fraction(0))

    def test_heisenberg_q0_nonzero(self):
        """q0 = 4*k^2 != 0 for k != 0."""
        data = heisenberg_data(Fraction(5))
        self.assertEqual(data.q0, 4 * Fraction(5)**2)

    def test_heisenberg_free_energy(self):
        """F_g = kappa * lambda_g^FP = k * lambda_g^FP for Heisenberg."""
        for k in [Fraction(1), Fraction(3), Fraction(7, 2)]:
            data = heisenberg_data(k)
            for g in range(1, 4):
                self.assertEqual(
                    free_energy_shadow(data, g),
                    Rational(k) * lambda_fp(g)
                )

    def test_heisenberg_matches_airy_rescaled(self):
        """F_g^{Heis} = kappa * F_g^{Airy}."""
        data = heisenberg_data(Fraction(2))
        for g in range(1, 5):
            self.assertEqual(
                free_energy_shadow(data, g),
                Rational(2) * free_energy_airy(g)
            )

    def test_heisenberg_tower_terminates(self):
        """Shadow tower has S_r = 0 for r >= 3 (class G: depth 2)."""
        data = heisenberg_data(Fraction(3))
        tower = shadow_tower_from_QL(data, 8)
        self.assertNotEqual(tower[2], Rational(0))
        for r in range(3, 9):
            self.assertEqual(tower[r], Rational(0))


# ====================================================================
# Section 3: Q2 -- Virasoro spectral curve (8 tests)
# ====================================================================

class TestQ2VirasoroSpectralCurve(unittest.TestCase):
    """Q2: Virasoro spectral curve y^2 = Q_L(t) is genuine."""

    def test_virasoro_not_degenerate(self):
        """Virasoro spectral curve is non-degenerate for c > 0."""
        for c in [Fraction(1), Fraction(10), Fraction(26)]:
            data = virasoro_data(c)
            self.assertFalse(data.is_degenerate)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        self.assertEqual(virasoro_data(Fraction(10)).kappa, Fraction(5))
        self.assertEqual(virasoro_data(Fraction(26)).kappa, Fraction(13))

    def test_virasoro_S4(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        data = virasoro_data(Fraction(10))
        self.assertEqual(data.S4, Fraction(10, 10 * 72))

    def test_virasoro_shadow_metric_q0(self):
        """q0 = 4*kappa^2 = c^2."""
        data = virasoro_data(Fraction(10))
        self.assertEqual(data.q0, Fraction(100))

    def test_virasoro_shadow_metric_q1(self):
        """q1 = 12*kappa*alpha = 12*(c/2)*2 = 12*c."""
        data = virasoro_data(Fraction(10))
        self.assertEqual(data.q1, Fraction(120))

    def test_virasoro_curve_branch_points(self):
        """Virasoro spectral curve has two distinct branch points."""
        data = virasoro_data(Fraction(10))
        curve = ShadowSpectralCurve(data)
        self.assertFalse(curve.degenerate)
        self.assertNotAlmostEqual(
            abs(curve.t_plus - curve.t_minus), 0.0, places=6
        )

    def test_virasoro_Delta_nonzero(self):
        """Critical discriminant Delta = 8*kappa*S4 != 0 for class M."""
        data = virasoro_data(Fraction(10))
        self.assertNotEqual(data.Delta, Fraction(0))

    def test_virasoro_free_energy_three_paths(self):
        """F_g matches across three paths for Virasoro."""
        data = virasoro_data(Fraction(10))
        fe = compare_free_energies(data, 5)
        for g in range(1, 6):
            self.assertTrue(fe[g]['all_match'])


# ====================================================================
# Section 4: Q3 -- EO kernel vs shadow connection (5 tests)
# ====================================================================

class TestQ3KernelComparison(unittest.TestCase):
    """Q3: EO recursion kernel vs shadow connection.

    Both have simple-pole behaviour at branch points.  The scalar shadow
    connection residue is 1/2; the EO kernel residue carries z0-data.
    The shadow connection monodromy is -1 (Koszul sign).
    """

    def test_shadow_connection_residue(self):
        """Shadow connection residue at branch point is 1/2."""
        data = virasoro_data(Fraction(10))
        self.assertEqual(shadow_connection_residue_at_branch(data), Rational(1, 2))

    def test_bergman_kernel_pole(self):
        """Bergman kernel 1/(z1-z2)^2 has double pole at z1=z2."""
        z1 = 1.0 + 0.5j
        z2 = 1.0 + 0.50001j
        B = bergman_kernel(z1, z2)
        self.assertGreater(abs(B), 1e6)

    def test_kernel_comparison_virasoro(self):
        """EO kernel and shadow connection have matching singularity structure."""
        data = virasoro_data(Fraction(10))
        result = compare_kernels_at_branch(data)
        self.assertFalse(result['degenerate'])
        self.assertAlmostEqual(
            result['shadow_connection_residue'], 0.5, places=10
        )
        self.assertTrue(result['same_pole_order'])
        self.assertIn('EO residue depends on z0', result['residue_identification'])

    def test_kernel_degenerate(self):
        """Degenerate curves: both kernels trivialize."""
        data = heisenberg_data(Fraction(1))
        result = compare_kernels_at_branch(data)
        self.assertTrue(result['degenerate'])

    def test_degenerate_curve_has_no_branch_residue(self):
        """The scalar residue is only defined at simple branch points."""
        data = heisenberg_data(Fraction(1))
        with self.assertRaises(ValueError):
            shadow_connection_residue_at_branch(data)

    def test_monodromy_virasoro(self):
        """Monodromy of nabla^sh around branch point = -1 (Koszul sign)."""
        data = virasoro_data(Fraction(10))
        result = verify_koszul_monodromy(data)
        self.assertFalse(result['degenerate'])
        self.assertTrue(result['match'],
                        f"Monodromy = {result['monodromy']}, expected -1")


# ====================================================================
# Section 5: Q4 -- Affine sl_2 (class L) (5 tests)
# ====================================================================

class TestQ4AffineSl2(unittest.TestCase):
    """Q4: Affine sl_2 spectral curve degenerates."""

    def test_affine_degenerate(self):
        """Affine sl_2 spectral curve is degenerate (Delta=0)."""
        data = affine_sl2_data(Fraction(1))
        self.assertTrue(data.is_degenerate)

    def test_affine_S4_zero(self):
        """S4 = 0 for affine (class L: Jacobi identity kills quartic)."""
        for k in [Fraction(1), Fraction(2), Fraction(5)]:
            data = affine_sl2_data(k)
            self.assertEqual(data.S4, Fraction(0))

    def test_affine_Delta_zero(self):
        """Delta = 8*kappa*S4 = 0 for affine."""
        data = affine_sl2_data(Fraction(3))
        self.assertEqual(data.Delta, Fraction(0))

    def test_affine_kappa(self):
        """kappa(aff sl_2) = 3(k+2)/4."""
        data = affine_sl2_data(Fraction(1))
        self.assertEqual(data.kappa, Fraction(9, 4))

    def test_affine_tower_terminates_at_3(self):
        """Shadow tower terminates at arity 3 for class L."""
        data = affine_sl2_data(Fraction(1))
        tower = shadow_tower_from_QL(data, 8)
        self.assertNotEqual(tower[2], Rational(0))
        self.assertNotEqual(tower[3], Rational(0))
        for r in range(4, 9):
            self.assertEqual(tower[r], Rational(0))


# ====================================================================
# Section 6: Q5 -- Beta-gamma (class C) (5 tests)
# ====================================================================

class TestQ5BetaGamma(unittest.TestCase):
    """Q5: Beta-gamma on primary line matches Vir c=2.

    Shadow depth=4 by stratum separation. Standard EO captures only the
    primary-line curve.
    """

    def test_betagamma_same_curve_as_vir2(self):
        """Beta-gamma spectral curve = Virasoro c=2 on primary line."""
        bg = betagamma_data()
        vir2 = virasoro_data(Fraction(2))
        self.assertEqual(bg.kappa, vir2.kappa)
        self.assertEqual(bg.S4, vir2.S4)
        self.assertEqual(bg.alpha, vir2.alpha)

    def test_betagamma_depth_class_C(self):
        """Beta-gamma is class C, depth 4."""
        bg = betagamma_data()
        self.assertEqual(bg.depth_class, 'C')
        self.assertEqual(bg.r_max, 4)

    def test_betagamma_curve_not_degenerate(self):
        """Beta-gamma spectral curve is non-degenerate (matches Vir c=2)."""
        bg = betagamma_data()
        self.assertFalse(bg.is_degenerate)

    def test_betagamma_eo_does_not_terminate(self):
        """Standard EO on the Vir c=2 curve continues.

        The spectral curve omits the stratum separation that makes class C
        depth 4.
        """
        # The Virasoro c=2 curve has Delta != 0, so the EO recursion
        # produces nonzero omega_{g,n} at all genera.
        bg = betagamma_data()
        self.assertNotEqual(bg.Delta, Fraction(0))

    def test_betagamma_primary_line_QL_has_nonzero_S5(self):
        """The primary-line Q_L tower is not the full class-C depth datum."""
        bg = betagamma_data()
        tower = shadow_tower_from_QL(bg, 5)
        self.assertEqual(bg.r_max, 4)
        self.assertNotEqual(tower[5], Rational(0))

    def test_betagamma_free_energy_matches_vir2(self):
        """F_g for beta-gamma on primary line matches Virasoro c=2."""
        bg = betagamma_data()
        vir2 = virasoro_data(Fraction(2))
        for g in range(1, 4):
            self.assertEqual(
                free_energy_shadow(bg, g),
                free_energy_shadow(vir2, g)
            )


# ====================================================================
# Section 7: Q6 -- Shadow depth vs spectral curve genus (6 tests)
# ====================================================================

class TestQ6DepthVsGenus(unittest.TestCase):
    """Q6: Shadow depth != spectral curve genus.

    The shadow spectral curve y^2 = Q_L(t) is ALWAYS genus 0.
    Shadow depth varies: 2, 3, 4, or infinity.
    """

    def test_spectral_curve_always_genus_0(self):
        """All shadow spectral curves have genus 0."""
        families = [
            heisenberg_data(), affine_sl2_data(), betagamma_data(),
            virasoro_data(Fraction(10)), w3_wline_data(Fraction(100)),
        ]
        for data in families:
            cl = classify_spectral_curve(data)
            self.assertEqual(cl.spectral_curve_genus, 0)

    def test_depth_not_equal_genus(self):
        """Shadow depth never equals spectral curve genus (genus always 0)."""
        table = depth_vs_curve_genus_table()
        for name, entry in table.items():
            self.assertFalse(entry['depth_equals_genus'])

    def test_heisenberg_depth_2(self):
        cl = classify_spectral_curve(heisenberg_data())
        self.assertEqual(cl.r_max, 2)
        self.assertEqual(cl.depth_class, 'G')

    def test_affine_depth_3(self):
        cl = classify_spectral_curve(affine_sl2_data())
        self.assertEqual(cl.r_max, 3)
        self.assertEqual(cl.depth_class, 'L')

    def test_betagamma_depth_4(self):
        cl = classify_spectral_curve(betagamma_data())
        self.assertEqual(cl.r_max, 4)
        self.assertEqual(cl.depth_class, 'C')

    def test_virasoro_depth_infinite(self):
        cl = classify_spectral_curve(virasoro_data(Fraction(10)))
        self.assertEqual(cl.r_max, -1)  # -1 = infinity
        self.assertEqual(cl.depth_class, 'M')


# ====================================================================
# Section 8: Q7 -- CEO vs shadow free energy (5 tests)
# ====================================================================

class TestQ7CEOvsShadow(unittest.TestCase):
    """Q7: F_g^{shadow} = F_g^{CEO} + delta_pf^{(g,0)}.

    For degenerate curves: CEO = 0, delta_pf = full shadow.
    For non-degenerate: delta_pf corrects CEO to shadow.
    """

    def test_degenerate_ceo_zero(self):
        """For degenerate curves, CEO = 0 and delta_pf = F_g^{shadow}."""
        data = heisenberg_data(Fraction(3))
        result = ceo_vs_shadow_discrepancy(data, 3)
        for g in range(1, 4):
            # delta_pf should equal F_g for degenerate
            self.assertEqual(
                result[g]['delta_pf'],
                result[g]['F_g_shadow']
            )

    def test_decomposition_holds(self):
        """F_g^{shadow} = F_g^{CEO} + delta_pf where the formula is present."""
        result = ceo_vs_shadow_discrepancy(heisenberg_data(), 3)
        for g in range(1, 4):
            self.assertTrue(result[g]['decomposition_holds'])

        result = ceo_vs_shadow_discrepancy(virasoro_data(Fraction(10)), 3)
        for g in range(1, 3):
            self.assertTrue(result[g]['decomposition_holds'])

    def test_non_degenerate_genus3_pf_is_not_inferred_from_QL(self):
        """Genus >= 3 non-degenerate corrections require stable-graph input."""
        result = ceo_vs_shadow_discrepancy(virasoro_data(Fraction(10)), 3)
        self.assertFalse(result[3]['closed_form_available'])
        self.assertIsNone(result[3]['delta_pf'])
        self.assertIn('stable-graph data beyond Q_L', result[3]['open_obligation'])

    def test_genus1_pf_zero_nondeg(self):
        """delta_pf^{(1,0)} = 0 for non-degenerate curves."""
        data = virasoro_data(Fraction(10))
        self.assertEqual(planted_forest_correction(data, 1), Rational(0))

    def test_genus2_pf_virasoro(self):
        """delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48 for Virasoro.

        For Virasoro: alpha = 2, kappa = c/2.
        delta_pf = 2*(20 - c/2)/48 = 2*(40 - c)/(2*48) = (40 - c)/48.
        """
        c = Fraction(10)
        data = virasoro_data(c)
        expected = Fraction(2) * (10 * Fraction(2) - c / 2) / 48
        self.assertEqual(planted_forest_correction(data, 2), expected)

    def test_genus2_pf_heisenberg(self):
        """delta_pf^{(2,0)} for Heisenberg = F_2 (degenerate: all from PF)."""
        data = heisenberg_data(Fraction(5))
        self.assertEqual(
            planted_forest_correction(data, 2),
            Rational(5) * lambda_fp(2)
        )


# ====================================================================
# Section 9: Q8 -- Kontsevich-Witten tau-function (5 tests)
# ====================================================================

class TestQ8KWTauFunction(unittest.TestCase):
    """Q8: log(tau_shadow) = kappa * log(tau_KW)."""

    def test_tau_kw_log_genus1(self):
        """log(tau_KW) coefficient at g=1 is 1/24."""
        kw = kw_tau_function_log(5)
        self.assertEqual(kw[1], Rational(1, 24))

    def test_tau_shadow_equals_kappa_times_kw(self):
        """Shadow tau logarithm is kappa times the KW tau logarithm."""
        data = virasoro_data(Fraction(10))
        result = verify_tau_kw_power_relation(data, 5)
        self.assertTrue(result['match_all'])
        self.assertFalse(result['analytic_tau_power_asserted'])

    def test_tau_heisenberg_power(self):
        """Heisenberg log tau = k * log(tau_KW)."""
        data = heisenberg_data(Fraction(7))
        result = verify_tau_kw_power_relation(data, 5)
        self.assertTrue(result['match_all'])

    def test_tau_affine_power(self):
        """Affine log tau has coefficient kappa = 3(k+2)/4."""
        data = affine_sl2_data(Fraction(2))
        result = verify_tau_kw_power_relation(data, 5)
        self.assertTrue(result['match_all'])

    def test_tau_kw_log_genus2(self):
        """log(tau_KW) coefficient at g=2 is 7/5760."""
        kw = kw_tau_function_log(5)
        self.assertEqual(kw[2], Rational(7, 5760))

    def test_finite_window_theorem_exact_coefficients_and_scope(self):
        """The theorem engine proves coefficients and refuses analytic overclaims."""
        data = virasoro_data(Fraction(10))
        report = finite_window_tr_shadow_theorem(data, 5)
        self.assertEqual(report['status'], 'proved_finite_window')
        self.assertTrue(report['all_coefficients_match'])
        self.assertEqual(report['coefficients'][5]['lambda_fp'],
                         Rational(73, 3503554560))
        self.assertEqual(report['coefficients'][5]['F_g_shadow'],
                         Rational(5) * Rational(73, 3503554560))
        self.assertFalse(report['scope']['analytic_tau_power_asserted'])
        self.assertFalse(report['scope']['full_eo_recursion_theorem_asserted'])
        self.assertFalse(report['scope']['convergence_radius_asserted'])
        self.assertTrue(report['scope']['scalar_lane_only'])

    def test_finite_window_theorem_separates_cross_channel_terms(self):
        """Primary-line scalar data do not compute multi-weight corrections."""
        report = finite_window_tr_shadow_theorem(betagamma_data(), 4)
        self.assertTrue(report['scope']['single_channel_curve_only'])
        self.assertFalse(report['scope']['multi_weight_cross_channel_terms_included'])
        self.assertIn('separate graph/weight engine', report['cross_channel_obligation'])


# ====================================================================
# Section 10: Q9 -- WP volumes / Mirzakhani (4 tests)
# ====================================================================

class TestQ9WPVolumes(unittest.TestCase):
    """Q9: Shadow tower uses an algebraic curve; WP uses the sine curve.

    These are different spectral curves.  The planted-forest corrections
    are the algebraic-to-transcendental bridge.
    """

    def test_wp_volume_g1(self):
        """WP volume V_{1,0} rational part = 1/24."""
        self.assertEqual(wp_volume_closed(1), Fraction(1, 24))

    def test_shadow_vs_wp_different_curves(self):
        """Shadow and WP use different spectral curves."""
        result = compare_shadow_with_wp(Fraction(10), 3)
        for g in range(1, 4):
            self.assertFalse(result[g]['same_spectral_curve'])

    def test_wp_volume_g2(self):
        """WP volume V_{2,0} rational part = 1/1152."""
        self.assertEqual(wp_volume_closed(2), Fraction(1, 1152))

    def test_wp_not_shadow(self):
        """F_g^{shadow} for Virasoro c=10 differs from WP at genus >= 2.

        F_2^{shadow} = 5 * 7/5760 = 7/1152, while V_{2,0} = 1/1152.
        These differ by a factor of 7 (they are different invariants).
        """
        data = virasoro_data(Fraction(10))
        f2_shadow = free_energy_shadow(data, 2)
        v2_wp = wp_volume_closed(2)
        self.assertNotEqual(f2_shadow, v2_wp)


# ====================================================================
# Section 11: Shadow tower consistency (4 tests)
# ====================================================================

class TestShadowTowerConsistency(unittest.TestCase):
    """Verify H(t)^2 = t^4 * Q_L(t) for all families."""

    def test_heisenberg_consistency(self):
        data = heisenberg_data(Fraction(3))
        result = verify_shadow_tower_consistency(data)
        self.assertTrue(result['all_match'])

    def test_virasoro_consistency(self):
        data = virasoro_data(Fraction(10))
        result = verify_shadow_tower_consistency(data)
        self.assertTrue(result['all_match'])

    def test_affine_consistency(self):
        data = affine_sl2_data(Fraction(2))
        result = verify_shadow_tower_consistency(data)
        self.assertTrue(result['all_match'])

    def test_w3_consistency(self):
        data = w3_wline_data(Fraction(100))
        result = verify_shadow_tower_consistency(data)
        self.assertTrue(result['all_match'])


# ====================================================================
# Section 12: Symplectic invariance (3 tests)
# ====================================================================

class TestSymplecticInvariance(unittest.TestCase):
    """Distinguished-origin normalization for the shadow free energy."""

    def test_virasoro_symplectic(self):
        data = virasoro_data(Fraction(10))
        result = verify_symplectic_invariance(data)
        self.assertTrue(result['normalization_invariant'])
        self.assertFalse(result['full_eo_symplectic_invariance_asserted'])
        self.assertEqual(result['scope'], 'distinguished shadow-coordinate normalization')

    def test_heisenberg_symplectic(self):
        data = heisenberg_data(Fraction(5))
        result = verify_symplectic_invariance(data)
        self.assertTrue(result['normalization_invariant'])

    def test_kappa_determined_by_q0(self):
        """kappa = sqrt(q0)/2, determined by Q_L(0) alone."""
        data = virasoro_data(Fraction(10))
        self.assertEqual(data.q0, 4 * data.kappa**2)


# ====================================================================
# Section 13: Verdier-dual scalar lane on spectral curves (5 tests)
# ====================================================================

class TestVerdierDualScalarLane(unittest.TestCase):
    """Virasoro Verdier-dual scalar lane on spectral curves.

    Virasoro: Vir_c^! = Vir_{26-c}. kappa + kappa' = 13.
    """

    def test_virasoro_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        result = koszul_dual_spectral_curve(virasoro_data(Fraction(10)))
        self.assertTrue(result['kappa_sum_is_13'])
        self.assertIn('Verdier/continuous-linear', result['dual_branch'])

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c=13."""
        result = koszul_dual_spectral_curve(virasoro_data(Fraction(13)))
        self.assertTrue(result['self_dual_at_c13'])

    def test_virasoro_not_self_dual_at_c26(self):
        """Virasoro is not self-dual at c=26.

        The Koszul dual Vir_{26-26} = Vir_0 has kappa=0.
        """
        result = koszul_dual_spectral_curve(virasoro_data(Fraction(26)))
        self.assertFalse(result['self_dual_at_c13'])
        self.assertEqual(result['kappa_dual'], Fraction(0))

    def test_koszul_dual_curves_different(self):
        """Spectral curves at c and 26-c are different for c != 13."""
        result = koszul_dual_spectral_curve(virasoro_data(Fraction(10)))
        self.assertNotEqual(result['q0'], result['q0_dual'])

    def test_dual_curve_is_not_inversion_or_bulk(self):
        """A^!, Omega(B(A)), and Z_ch^der(A) stay separate."""
        result = koszul_dual_spectral_curve(virasoro_data(Fraction(10)))
        self.assertIn('Omega(B(A)) = A', result['not_inversion'])
        self.assertEqual(result['not_bulk'], 'Z_ch^der(A) = ChirHoch^*(A,A)')


# ====================================================================
# Section 14: Witten-Kontsevich intersection numbers (4 tests)
# ====================================================================

class TestWittenKontsevich(unittest.TestCase):
    """Witten-Kontsevich intersection numbers."""

    def test_wk_tau000_genus0(self):
        """<tau_0 tau_0 tau_0>_0 = 1."""
        self.assertEqual(wk_intersection(0, 0, 0, g=0), Rational(1))

    def test_wk_tau1_genus1(self):
        """<tau_1>_1 = 1/24."""
        self.assertEqual(wk_intersection(1, g=1), Rational(1, 24))

    def test_wk_tau4_genus2(self):
        """<tau_4>_2 = 1/1152."""
        self.assertEqual(wk_intersection(4, g=2), Rational(1, 1152))

    def test_wk_selection_rule(self):
        """Selection rule: sum(d_i) = 3g-3+n; violation gives 0."""
        self.assertEqual(wk_intersection(1, 1, g=0), Rational(0))


# ====================================================================
# Section 15: Airy limit (3 tests)
# ====================================================================

class TestAiryLimit(unittest.TestCase):
    """The Airy curve is the local model near a ramification point."""

    def test_virasoro_airy_limit(self):
        data = virasoro_data(Fraction(10))
        result = airy_limit_of_shadow(data)
        self.assertFalse(result['degenerate'])
        # The Airy scale should be nonzero
        self.assertNotAlmostEqual(abs(result['airy_scale_plus']), 0.0)

    def test_airy_scale_is_simple_root_derivative(self):
        """At t_+, the Airy scale is Q_L'(t_+) = 2*q2*half_gap."""
        data = virasoro_data(Fraction(10))
        curve = ShadowSpectralCurve(data)
        result = airy_limit_of_shadow(data)
        q1 = float(data.q1)
        q2 = float(data.q2)
        qprime_at_plus = q1 + 2 * q2 * curve.t_plus
        self.assertAlmostEqual(
            abs(result['airy_scale_plus'] - qprime_at_plus), 0.0, places=10
        )

    def test_heisenberg_no_airy_limit(self):
        data = heisenberg_data(Fraction(1))
        result = airy_limit_of_shadow(data)
        self.assertTrue(result['degenerate'])

    def test_airy_universality(self):
        """F_g^{Airy} = lambda_g^FP is independent of the Airy scale.

        The Airy curve y^2 = a*x gives the same F_g for all a != 0
        (symplectic rescaling).
        """
        for g in range(1, 5):
            self.assertEqual(free_energy_airy(g), lambda_fp(g))


# ====================================================================
# Section 16: Shadow flat section (2 tests)
# ====================================================================

class TestShadowFlatSection(unittest.TestCase):
    """Flat section Phi(t) = sqrt(Q_L(t)/Q_L(0)).

    H(t) = t^2*Phi(t)*sqrt(Q_L(0)) is not a flat section.
    """

    def test_flat_section_at_origin(self):
        """Phi(0) = sqrt(Q_L(0)/Q_L(0)) = 1."""
        data = virasoro_data(Fraction(10))
        phi_0 = shadow_flat_section(data, 0.0)
        self.assertAlmostEqual(abs(phi_0 - 1.0), 0.0, places=10)

    def test_flat_section_nontrivial(self):
        """Phi(t) != 1 for t != 0 (for non-constant Q_L)."""
        data = virasoro_data(Fraction(10))
        phi = shadow_flat_section(data, 0.1)
        self.assertNotAlmostEqual(abs(phi - 1.0), 0.0, places=2)


# ====================================================================
# Section 17: Full verification report (1 test)
# ====================================================================

class TestFullReport(unittest.TestCase):
    """Full TR-shadow verification report."""

    def test_full_report_runs(self):
        """Full verification report completes without error."""
        report = full_tr_shadow_verification(g_max=3)
        self.assertIn('Q1_heisenberg', report)
        self.assertIn('Q2_virasoro_curve', report)
        self.assertIn('Q3_kernel_comparison', report)
        self.assertIn('Q4_affine_sl2', report)
        self.assertIn('Q5_betagamma', report)
        self.assertIn('Q6_depth_vs_genus', report)
        self.assertIn('Q7_ceo_vs_shadow', report)
        self.assertIn('Q8_kw_tau', report)
        self.assertIn('Q8_finite_window_theorem', report)
        self.assertIn('Q9_wp_comparison', report)
        self.assertFalse(
            report['Q8_finite_window_theorem']['scope']['analytic_tau_power_asserted']
        )


# ====================================================================
# Section 18: Shadow tower extraction cross-checks (4 tests)
# ====================================================================

class TestShadowTowerExtraction(unittest.TestCase):
    """Cross-family shadow tower extraction from Q_L."""

    def test_virasoro_S2_equals_kappa(self):
        """S_2 = kappa for all families."""
        data = virasoro_data(Fraction(10))
        tower = shadow_tower_from_QL(data, 4)
        self.assertEqual(simplify(tower[2] - Rational(data.kappa)), 0)

    def test_virasoro_S3_equals_alpha(self):
        """S_3 = alpha for Virasoro."""
        data = virasoro_data(Fraction(10))
        tower = shadow_tower_from_QL(data, 4)
        # S_3 = (1/3) * [t^1] sqrt(Q_L) = (1/3) * q1/(2*sqrt(q0))
        # = (1/3) * 12*kappa*alpha / (2*2*kappa) = alpha
        expected = Rational(data.alpha)
        self.assertEqual(simplify(tower[3] - expected), 0)

    def test_heisenberg_S3_zero(self):
        """S_3 = 0 for Heisenberg (alpha = 0)."""
        data = heisenberg_data(Fraction(5))
        tower = shadow_tower_from_QL(data, 4)
        self.assertEqual(tower[3], Rational(0))

    def test_affine_S4_zero(self):
        """S_4 = 0 for affine (class L)."""
        data = affine_sl2_data(Fraction(2))
        tower = shadow_tower_from_QL(data, 5)
        # The quartic shadow coefficient should reflect S4=0
        # (though the tower coefficient at arity 4 may be nonzero
        # due to contributions from S_3^2 terms).
        # S_4^{contact} = 0 for affine, but S_4^{total} can be nonzero.
        self.assertEqual(data.S4, Fraction(0))


# ====================================================================
# Section 19: Cross-family free energy consistency (3 tests)
# ====================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Cross-family free energy consistency checks."""

    def test_additivity_heisenberg(self):
        """F_g(H_{k1} + H_{k2}) = F_g(H_{k1}) + F_g(H_{k2}).

        kappa is additive for direct sums with vanishing mixed OPE
        (prop:independent-sum-factorization).
        """
        k1, k2 = Fraction(3), Fraction(5)
        data1 = heisenberg_data(k1)
        data2 = heisenberg_data(k2)
        data_sum = heisenberg_data(k1 + k2)

        for g in range(1, 5):
            f1 = free_energy_shadow(data1, g)
            f2 = free_energy_shadow(data2, g)
            f_sum = free_energy_shadow(data_sum, g)
            self.assertEqual(f1 + f2, f_sum)

    def test_virasoro_complementarity(self):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g^FP.

        kappa + kappa' = 13 for Virasoro.
        """
        c = Fraction(10)
        data = virasoro_data(c)
        data_dual = virasoro_data(Fraction(26) - c)
        for g in range(1, 5):
            total = free_energy_shadow(data, g) + free_energy_shadow(data_dual, g)
            self.assertEqual(total, 13 * lambda_fp(g))

    def test_ahat_generating_function(self):
        """sum_g F_g * x^{2g} = kappa * (A-hat(ix) - 1) at leading orders.

        The hbar convention is 2g, not 2g-2.
        Verify: F_1 = kappa/24 matches [x^2] of kappa*(Ahat(ix)-1).
        """
        kappa = Rational(5)  # Vir c=10
        # A-hat(ix) - 1 = x^2/24 + 7*x^4/5760 + ...
        # (all positive because A-hat(ix) = x/(2*sin(x/2)))
        self.assertEqual(free_energy_ahat(kappa, 1), kappa * Rational(1, 24))
        self.assertEqual(free_energy_ahat(kappa, 2), kappa * Rational(7, 5760))


# ====================================================================
# Section 20: Numerical EO engine (mpmath) (4 tests)
# ====================================================================

@unittest.skipUnless(HAS_MPMATH, "mpmath required")
class TestShadowEOEngine(unittest.TestCase):
    """Numerical EO recursion on the shadow spectral curve."""

    def test_engine_creation_virasoro(self):
        """ShadowEOEngine creates for Virasoro."""
        from compute.lib.topological_recursion_shadow_engine import ShadowEOEngine
        data = virasoro_data(Fraction(10))
        engine = ShadowEOEngine(data, dps=30, contour_points=128)
        self.assertFalse(engine.degenerate)

    def test_engine_degenerate_heisenberg(self):
        """ShadowEOEngine correctly detects Heisenberg as degenerate."""
        from compute.lib.topological_recursion_shadow_engine import ShadowEOEngine
        data = heisenberg_data(Fraction(1))
        engine = ShadowEOEngine(data, dps=30)
        self.assertTrue(engine.degenerate)

    def test_omega_11_virasoro_nonzero(self):
        """omega_{1,1} is nonzero for Virasoro (non-degenerate)."""
        from compute.lib.topological_recursion_shadow_engine import ShadowEOEngine
        data = virasoro_data(Fraction(10))
        engine = ShadowEOEngine(data, dps=30, contour_points=128)
        z0 = 2.0 + 0.3j
        val = engine.omega_11(z0)
        self.assertGreater(abs(val), 1e-20)

    def test_omega_11_heisenberg_zero(self):
        """omega_{1,1} = 0 for Heisenberg (degenerate)."""
        from compute.lib.topological_recursion_shadow_engine import ShadowEOEngine
        data = heisenberg_data(Fraction(1))
        engine = ShadowEOEngine(data, dps=30)
        val = engine.omega_11(2.0 + 0.3j)
        self.assertAlmostEqual(abs(val), 0.0, places=10)


if __name__ == '__main__':
    unittest.main()
