"""Tests for bc_topological_recursion_shadow_engine.py.

Comprehensive test suite covering:
- Faber-Pandharipande intersection numbers
- Witten-Kontsevich intersection numbers
- Shadow curve data for standard families
- Shadow spectral curve parametrization
- Shadow tower from Q_L Taylor expansion
- Signed-branch normalization
- WKB expansion
- Verdier-complementarity scalar partners
- Airy curve cross-checks
- String/dilaton equations
- Finite scalar verification report

Key scalar identities are checked by independent oracle routes.
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, factorial

from compute.lib.bc_topological_recursion_shadow_engine import (
    lambda_fp,
    _odd_double_factorial,
    _witten_kontsevich,
    ShadowCurveData,
    ShadowSpectralCurve,
    virasoro_shadow,
    affine_sl2_shadow,
    heisenberg_shadow,
    betagamma_shadow,
    w3_shadow,
    shadow_tower_from_QL,
    stationary_primary_line_riccati_diagnostic,
    self_data_to_rat,
    symplectic_check_free_energy,
    wkb_expansion,
    koszul_dual_curve,
    complementarity_check,
    verify_shadow_eo_match,
    kw_tau_function_log,
    shadow_scalar_tau_log,
    finite_scalar_kw_coefficient_identity,
    wp_jt_sine_curve_input,
    multi_weight_stable_graph_scope,
    claim_scope_firewall_report,
    dilaton_equation_check,
    string_equation_check,
    full_verification_suite,
    MirrorCurveConifold,
    _bernoulli_number,
    holographic_package_entries,
    modular_koszul_primary_projections,
    typed_firewall_objects,
    typed_firewall_roles,
    collision_kernel_constants,
    AiryCurveRecursion,
)


# =====================================================================
# 1. Faber-Pandharipande intersection numbers
# =====================================================================

class TestLambdaFP(unittest.TestCase):
    """Test Faber-Pandharipande intersection numbers lambda_g^FP."""

    def test_g1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Rational(1, 24))

    def test_g2(self):
        """lambda_2^FP = 7/5760.

        Cross-check: (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 24 = 7/5760.
        """
        B4 = Rational(abs(_bernoulli_number(4)))  # |B_4| = 1/30
        expected = Rational(2**3 - 1, 2**3) * B4 / factorial(4)
        self.assertEqual(lambda_fp(2), expected)
        self.assertEqual(lambda_fp(2), Rational(7, 5760))

    def test_g3(self):
        """lambda_3^FP via formula: (2^5-1)/2^5 * |B_6|/6!."""
        B6 = abs(_bernoulli_number(6))
        expected = Rational(2**5 - 1, 2**5) * B6 / factorial(6)
        self.assertEqual(lambda_fp(3), expected)

    def test_positivity(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_g0_raises(self):
        with self.assertRaises(ValueError):
            lambda_fp(0)

    def test_decreasing(self):
        """lambda_g^FP is rapidly decreasing in g."""
        for g in range(1, 6):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1))

    def test_independent_computation(self):
        """Cross-check lambda_g via independent Bernoulli computation."""
        for g in range(1, 5):
            B2g = _bernoulli_number(2 * g)
            num = (2**(2*g - 1) - 1) * abs(B2g)
            den = 2**(2*g - 1) * factorial(2 * g)
            expected = Rational(num, den)
            self.assertEqual(lambda_fp(g), expected)


# =====================================================================
# 2. Witten-Kontsevich intersection numbers
# =====================================================================

class TestWittenKontsevich(unittest.TestCase):
    """Test Witten-Kontsevich intersection numbers."""

    def test_tau0_cubed_g0(self):
        """<tau_0^3>_0 = 1."""
        self.assertEqual(_witten_kontsevich(0, (0, 0, 0)), Rational(1))

    def test_tau1_g1(self):
        """<tau_1>_1 = 1/24."""
        self.assertEqual(_witten_kontsevich(1, (1,)), Rational(1, 24))

    def test_dimension_check(self):
        """Return 0 if dim constraint sum(d_i) != 3g-3+n fails."""
        # For g=0, n=3: need sum=0. (1,0,0) has sum=1 != 0.
        self.assertEqual(_witten_kontsevich(0, (1, 0, 0)), Rational(0))

    def test_stability_check(self):
        """Return 0 if 2g-2+n <= 0."""
        self.assertEqual(_witten_kontsevich(0, (0, 0)), Rational(0))  # n=2, g=0

    def test_negative_d(self):
        self.assertEqual(_witten_kontsevich(0, (-1, 0, 0, 0)), Rational(0))

    def test_genus0_multinomial(self):
        """<tau_0^{n-1} tau_{n-3}>_0 = 1 for n >= 3."""
        # For n=4 the dimension is n-3=1, so tau_0^3 tau_1 is the
        # first nontrivial string-equation case.
        val = _witten_kontsevich(0, (0, 0, 0, 1))
        self.assertEqual(val, Rational(1))

    def test_genus0_multinomial_symmetric(self):
        """Genus-zero values are symmetric in the insertions."""
        self.assertEqual(_witten_kontsevich(0, (2, 0, 0, 0, 0)), Rational(1))
        self.assertEqual(_witten_kontsevich(0, (0, 2, 0, 0, 0)), Rational(1))

    def test_string_equation_nonbase(self):
        """<tau_0 tau_2>_1 = <tau_1>_1 = 1/24."""
        self.assertEqual(_witten_kontsevich(1, (0, 2)), Rational(1, 24))

    def test_dilaton_equation_nonbase(self):
        """<tau_1 tau_1>_1 = (2*1-2+1)<tau_1>_1 = 1/24."""
        self.assertEqual(_witten_kontsevich(1, (1, 1)), Rational(1, 24))

    def test_tau3_g2_dimension_fail(self):
        """<tau_3>_2 = 0: dimension constraint fails (3 != 3*2-3+1=4)."""
        self.assertEqual(_witten_kontsevich(2, (3,)), Rational(0))

    def test_tau4_g2_dvv(self):
        """<tau_4>_2 = 1/(24^2*2!) = 1/1152."""
        self.assertEqual(_witten_kontsevich(2, (4,)), Rational(1, 1152))

    def test_tau1_cubed_g2(self):
        """<tau_1^3>_2 = 0 because the dimension is 6, not 3."""
        # dim check: sum(d_i)=3, 3g-3+n = 6-3+3 = 6. 3 != 6 => returns 0
        self.assertEqual(_witten_kontsevich(2, (1, 1, 1)), Rational(0))

    def test_odd_double_factorial_base(self):
        """The DVV convention uses (-1)!! = 1."""
        self.assertEqual(_odd_double_factorial(-1), 1)
        self.assertEqual(_odd_double_factorial(7), 105)


# =====================================================================
# 3. Shadow curve data for standard families
# =====================================================================

class TestShadowCurveData(unittest.TestCase):
    """Test ShadowCurveData properties and construction."""

    def test_virasoro_kappa(self):
        """Virasoro: kappa = c/2."""
        for c_val in [Fraction(2), Fraction(10), Fraction(13)]:
            data = virasoro_shadow(c_val)
            self.assertEqual(data.kappa, c_val / 2)

    def test_virasoro_alpha(self):
        """Virasoro: alpha = 2."""
        data = virasoro_shadow(Fraction(2))
        self.assertEqual(data.alpha, Fraction(2))

    def test_virasoro_S4(self):
        """Virasoro: S4 = 10/(c*(5c+22))."""
        for c_val in [Fraction(2), Fraction(10)]:
            data = virasoro_shadow(c_val)
            expected = Fraction(10) / (c_val * (5 * c_val + 22))
            self.assertEqual(data.S4, expected)

    def test_virasoro_depth_class(self):
        data = virasoro_shadow(Fraction(2))
        self.assertEqual(data.depth_class, 'M')

    def test_heisenberg_kappa(self):
        """Heisenberg: kappa = k."""
        data = heisenberg_shadow(Fraction(3))
        self.assertEqual(data.kappa, Fraction(3))

    def test_heisenberg_alpha_zero(self):
        data = heisenberg_shadow()
        self.assertEqual(data.alpha, Fraction(0))

    def test_heisenberg_S4_zero(self):
        data = heisenberg_shadow()
        self.assertEqual(data.S4, Fraction(0))

    def test_heisenberg_depth_G(self):
        data = heisenberg_shadow()
        self.assertEqual(data.depth_class, 'G')

    def test_affine_sl2_kappa(self):
        """sl_2: kappa = 3(k+2)/4."""
        data = affine_sl2_shadow(Fraction(1))
        self.assertEqual(data.kappa, Fraction(3) * Fraction(3) / 4)

    def test_affine_sl2_S4_zero(self):
        data = affine_sl2_shadow(Fraction(1))
        self.assertEqual(data.S4, Fraction(0))

    def test_affine_sl2_depth_L(self):
        data = affine_sl2_shadow(Fraction(1))
        self.assertEqual(data.depth_class, 'L')

    def test_w3_kappa(self):
        """W_3: kappa = 5c/6."""
        data = w3_shadow(Fraction(6))
        self.assertEqual(data.kappa, Fraction(5))

    def test_w3_alpha_zero(self):
        data = w3_shadow(Fraction(6))
        self.assertEqual(data.alpha, Fraction(0))

    def test_q0_formula(self):
        """q0 = 4*kappa^2."""
        data = virasoro_shadow(Fraction(10))
        self.assertEqual(data.q0, 4 * data.kappa ** 2)

    def test_q1_formula(self):
        """q1 = 12*kappa*alpha."""
        data = virasoro_shadow(Fraction(10))
        self.assertEqual(data.q1, 12 * data.kappa * data.alpha)

    def test_q2_formula(self):
        """q2 = 9*alpha^2 + 16*kappa*S4."""
        data = virasoro_shadow(Fraction(10))
        self.assertEqual(data.q2, 9 * data.alpha ** 2 + 16 * data.kappa * data.S4)

    def test_delta_formula(self):
        """Delta = 8*kappa*S4."""
        data = virasoro_shadow(Fraction(2))
        self.assertEqual(data.Delta, 8 * data.kappa * data.S4)

    def test_heisenberg_delta_zero(self):
        data = heisenberg_shadow()
        self.assertEqual(data.Delta, Fraction(0))

    def test_discriminant_formula(self):
        """disc = q1^2 - 4*q0*q2."""
        data = virasoro_shadow(Fraction(10))
        self.assertEqual(data.disc_QL, data.q1 ** 2 - 4 * data.q0 * data.q2)

    def test_betagamma_same_as_virasoro_c2(self):
        bg = betagamma_shadow()
        vir = virasoro_shadow(Fraction(2))
        self.assertEqual(bg.kappa, vir.kappa)
        self.assertEqual(bg.alpha, vir.alpha)
        self.assertEqual(bg.S4, vir.S4)

    def test_betagamma_keeps_contact_family_label(self):
        """Beta-gamma has Vir_c=2 scalar data but class C depth."""
        bg = betagamma_shadow()
        self.assertEqual(bg.name, "betagamma")
        self.assertEqual(bg.depth_class, "C")


# =====================================================================
# 4. Spectral curve parametrization
# =====================================================================

class TestShadowSpectralCurve(unittest.TestCase):
    """Test the spectral curve class."""

    def test_heisenberg_degenerate(self):
        data = heisenberg_shadow()
        curve = ShadowSpectralCurve(data)
        self.assertTrue(curve.degenerate)

    def test_virasoro_nondegenerate(self):
        data = virasoro_shadow(Fraction(10))
        curve = ShadowSpectralCurve(data)
        self.assertFalse(curve.degenerate)

    def test_deck_involution(self):
        """sigma(z) = 1/z."""
        data = virasoro_shadow(Fraction(10))
        curve = ShadowSpectralCurve(data)
        z = 2.0 + 1j
        self.assertAlmostEqual(curve.sigma(z), 1.0 / z, places=10)

    def test_t_at_branch_points(self):
        """t(z=1) = t_+, t(z=-1) = t_-."""
        data = virasoro_shadow(Fraction(10))
        curve = ShadowSpectralCurve(data)
        if not curve.degenerate:
            self.assertAlmostEqual(curve.t_of_z(1.0), curve.t_plus, places=8)
            self.assertAlmostEqual(curve.t_of_z(-1.0), curve.t_minus, places=8)

    def test_y_vanishes_at_branch_points(self):
        """y(z=1) = 0 and y(z=-1) = 0."""
        data = virasoro_shadow(Fraction(10))
        curve = ShadowSpectralCurve(data)
        if not curve.degenerate:
            self.assertAlmostEqual(abs(curve.y_of_z(1.0)), 0.0, places=8)
            self.assertAlmostEqual(abs(curve.y_of_z(-1.0)), 0.0, places=8)

    def test_QL_at_branch_point(self):
        """Q_L(t_+) = 0 by definition."""
        data = virasoro_shadow(Fraction(10))
        curve = ShadowSpectralCurve(data)
        if not curve.degenerate:
            self.assertAlmostEqual(abs(curve.Q_L(curve.t_plus)), 0.0, places=6)

    def test_degenerate_t_of_z(self):
        data = heisenberg_shadow()
        curve = ShadowSpectralCurve(data)
        self.assertEqual(curve.t_of_z(2.0), curve.t_mid)


# =====================================================================
# 5. Shadow tower from Q_L
# =====================================================================

class TestShadowTowerFromQL(unittest.TestCase):
    """Test shadow tower coefficient extraction from Q_L."""

    def test_heisenberg_tower(self):
        """Heisenberg: S_2 = kappa, all S_r = 0 for r >= 3 (class G)."""
        data = heisenberg_shadow(Fraction(3))
        tower = shadow_tower_from_QL(data, max_arity=6)
        # S_2 = sqrt(q0)*1/2 = 2*kappa/2 = kappa = 3
        self.assertEqual(tower[2], Rational(3))
        for r in range(3, 7):
            self.assertEqual(tower[r], 0, f"S_{r} should vanish for Heisenberg")

    def test_affine_sl2_tower(self):
        """Affine sl_2: S_2 = kappa, S_3 != 0, S_r = 0 for r >= 4 (class L)."""
        data = affine_sl2_shadow(Fraction(1))
        tower = shadow_tower_from_QL(data, max_arity=8)
        self.assertNotEqual(tower[2], 0)
        self.assertEqual(tower[2], Rational(9, 4))
        self.assertNotEqual(tower[3], 0)
        self.assertEqual(tower[3], Rational(2))
        for r in range(4, 9):
            self.assertEqual(tower[r], 0)

    def test_virasoro_tower_nonzero(self):
        """Virasoro: class M, infinite tower, S_r != 0 for large r."""
        data = virasoro_shadow(Fraction(10))
        tower = shadow_tower_from_QL(data, max_arity=8)
        self.assertNotEqual(tower[2], 0)
        self.assertNotEqual(tower[3], 0)
        self.assertNotEqual(tower[4], 0)

    def test_S2_equals_kappa(self):
        """S_2 = kappa for all families.

        The formal branch is sqrt(Q_L(0)) = 2*kappa, including negative
        scalar complementarity branches.
        """
        for name, data in [
            ('Heis', heisenberg_shadow(Fraction(5))),
            ('sl2', affine_sl2_shadow(Fraction(2))),
            ('Vir', virasoro_shadow(Fraction(6))),
            ('HeisDualScalar', heisenberg_shadow(Fraction(-5))),
        ]:
            tower = shadow_tower_from_QL(data, max_arity=4)
            self.assertEqual(tower[2], Rational(data.kappa.numerator, data.kappa.denominator),
                             f"S_2 != kappa for {name}")

    def test_virasoro_tower_recovers_S4(self):
        """The Taylor tower recovers S_4 = 10/(c(5c+22))."""
        data = virasoro_shadow(Fraction(10))
        tower = shadow_tower_from_QL(data, max_arity=4)
        self.assertEqual(tower[4], Rational(data.S4.numerator, data.S4.denominator))


# =====================================================================
# 6. Signed-branch normalization
# =====================================================================

class TestSignedBranchNormalization(unittest.TestCase):
    """Test scalar normalization without global EO invariance."""

    def test_virasoro_invariant(self):
        data = virasoro_shadow(Fraction(10))
        for g in range(1, 4):
            result = symplectic_check_free_energy(data, g)
            self.assertTrue(result['symplectic_invariant'])
            self.assertFalse(result['full_eo_symplectic_invariance_asserted'])
            self.assertEqual(result['F_g_original'], result['F_g_invariant'])

    def test_affine_invariant(self):
        data = affine_sl2_shadow(Fraction(1))
        result = symplectic_check_free_energy(data, 1)
        self.assertTrue(result['symplectic_invariant'])


# =====================================================================
# 7. WKB expansion
# =====================================================================

class TestWKBExpansion(unittest.TestCase):
    """Test WKB expansion coefficients."""

    def test_S1_equals_F1(self):
        """WKB S_1 = F_1 = kappa/24."""
        data = virasoro_shadow(Fraction(10))
        wkb = wkb_expansion(data, max_order=3)
        self.assertEqual(wkb[1], Rational(5, 1) / 24)

    def test_Sg_equals_Fg(self):
        """WKB S_g = F_g = kappa*lambda_g for g >= 2."""
        data = virasoro_shadow(Fraction(10))
        wkb = wkb_expansion(data, max_order=4)
        kappa_rat = Rational(5)
        for g in range(2, 5):
            self.assertEqual(wkb[g], kappa_rat * lambda_fp(g))

    def test_S0_leading(self):
        """WKB S_0 = 2*kappa (leading coefficient)."""
        data = heisenberg_shadow(Fraction(3))
        wkb = wkb_expansion(data, max_order=2)
        self.assertEqual(wkb[0], Rational(6))


# =====================================================================
# 8. Airy residue oracle
# =====================================================================

class TestAiryResidues(unittest.TestCase):
    """Test the Airy coefficient convention against contour residues."""

    def test_omega_11_exact_matches_contour(self):
        airy = AiryCurveRecursion(dps=50, contour_radius=0.001, contour_points=1024)
        z0 = 2.0
        numeric = airy.omega_11_airy(z0)
        exact = airy.omega_11_airy_exact(z0)
        self.assertLess(float(abs(numeric - exact)), 1e-30)
        self.assertEqual(exact, 1 / (4 * z0**3))

    def test_omega_03_exact_matches_contour(self):
        airy = AiryCurveRecursion(dps=50, contour_radius=0.001, contour_points=1024)
        z0, z1, z2 = 2.0, 3.0, 4.0
        numeric = airy.omega_03_airy(z0, z1, z2)
        exact = airy.omega_03_airy_exact(z0, z1, z2)
        self.assertLess(float(abs(numeric - exact)), 1e-15)
        self.assertEqual(exact, 2 / (z0 * z1**2 * z2**2))


# =====================================================================
# 9. Verdier-complementarity scalar partners
# =====================================================================

class TestKoszulDualCurve(unittest.TestCase):
    """Test scalar partner data for Verdier complementarity."""

    def test_virasoro_dual(self):
        """Vir_c -> Vir_{26-c}."""
        data = virasoro_shadow(Fraction(10))
        dual = koszul_dual_curve(data)
        self.assertIsNotNone(dual)
        # Dual should have kappa' = (26-10)/2 = 8
        self.assertEqual(dual.kappa, Fraction(8))

    def test_heisenberg_dual(self):
        """Heisenberg scalar partner has kappa = -k."""
        data = heisenberg_shadow(Fraction(3))
        dual = koszul_dual_curve(data)
        self.assertIsNotNone(dual)
        self.assertEqual(dual.kappa, Fraction(-3))

    def test_affine_sl2_scalar_partner(self):
        """Affine sl_2 scalar partner has kappa sum zero."""
        data = affine_sl2_shadow(Fraction(1))
        dual = koszul_dual_curve(data)
        self.assertIsNotNone(dual)
        self.assertEqual(data.kappa + dual.kappa, Fraction(0))

    def test_virasoro_c13_self_dual(self):
        """Vir_{13} is self-dual: kappa=13/2, dual kappa=(26-13)/2=13/2."""
        data = virasoro_shadow(Fraction(13))
        dual = koszul_dual_curve(data)
        self.assertIsNotNone(dual)
        self.assertEqual(dual.kappa, data.kappa)

    def test_virasoro_c26_boundary(self):
        """c=26: dual has c=0 which is degenerate."""
        data = virasoro_shadow(Fraction(26))
        dual = koszul_dual_curve(data)
        self.assertIsNone(dual)


# =====================================================================
# 9. Complementarity
# =====================================================================

class TestComplementarityCheck(unittest.TestCase):
    """Test scalar complementarity relations."""

    def test_virasoro_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        data = virasoro_shadow(Fraction(10))
        result = complementarity_check(data, 1)
        self.assertEqual(result['kappa_sum'], Fraction(13))

    def test_virasoro_Fg_sum(self):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g."""
        data = virasoro_shadow(Fraction(6))
        for g in range(1, 4):
            result = complementarity_check(data, g)
            expected = Rational(13) * lambda_fp(g)
            self.assertEqual(result['sum'], expected)
            self.assertTrue(result['complementarity'])

    def test_various_c_values(self):
        """Complementarity holds for all c in (0,26)."""
        for c_val in [Fraction(1), Fraction(5), Fraction(13), Fraction(20), Fraction(25)]:
            data = virasoro_shadow(c_val)
            result = complementarity_check(data, 1)
            if result['complementarity'] is not None:
                self.assertTrue(result['complementarity'])

    def test_heisenberg_sum_zero(self):
        """Heisenberg scalar complementarity has zero kappa sum."""
        result = complementarity_check(heisenberg_shadow(Fraction(7)), 2)
        self.assertEqual(result['kappa_sum'], Fraction(0))
        self.assertEqual(result['sum'], Rational(0))
        self.assertTrue(result['complementarity'])

    def test_affine_sl2_sum_zero(self):
        """Affine sl_2 scalar complementarity has zero kappa sum."""
        result = complementarity_check(affine_sl2_shadow(Fraction(1)), 2)
        self.assertEqual(result['kappa_sum'], Fraction(0))
        self.assertEqual(result['sum'], Rational(0))
        self.assertTrue(result['complementarity'])


# =====================================================================
# 10. Finite scalar coefficient identity
# =====================================================================

class TestFiniteScalarCoefficientIdentity(unittest.TestCase):
    """Test the scalar coefficient check without EO overclaim."""

    def test_virasoro_match(self):
        data = virasoro_shadow(Fraction(10))
        results = verify_shadow_eo_match(data, max_genus=3)
        for g in range(1, 4):
            self.assertTrue(results[g]['match'])
            self.assertEqual(results[g]['tower_S2'], Rational(5))
            self.assertEqual(results[g]['eo_contour_integral'], 'not_evaluated')
            self.assertFalse(results[g]['full_eo_recursion_theorem_asserted'])
            self.assertTrue(results[g]['finite_scalar_identity'])

    def test_heisenberg_match(self):
        data = heisenberg_shadow(Fraction(1))
        results = verify_shadow_eo_match(data, max_genus=2)
        for g in range(1, 3):
            self.assertTrue(results[g]['match'])

    def test_riccati_diagnostic_is_finite(self):
        data = virasoro_shadow(Fraction(10))
        result = stationary_primary_line_riccati_diagnostic(data, max_arity=8)
        self.assertEqual(result['identity'], 'H(t)^2 = t^4 Q_L(t)')
        self.assertTrue(result['all_checked_degrees_match'])
        self.assertFalse(result['certifies_full_eo_recursion'])
        self.assertFalse(result['certifies_kw_tau_theorem'])
        self.assertFalse(result['certifies_convergence_radius'])
        self.assertFalse(result['includes_multi_weight_stable_graph_data'])

    def test_finite_kw_identity_refuses_analytic_claims(self):
        data = virasoro_shadow(Fraction(10))
        report = finite_scalar_kw_coefficient_identity(data, g_max=5)
        self.assertEqual(report['status'], 'finite_scalar_coefficient_identity')
        self.assertTrue(report['all_coefficients_match'])
        self.assertEqual(kw_tau_function_log(5)[2], Rational(7, 5760))
        self.assertEqual(
            shadow_scalar_tau_log(data, 5)[2],
            Rational(5) * Rational(7, 5760),
        )
        self.assertFalse(report['global_kw_tau_theorem_asserted'])
        self.assertFalse(report['analytic_tau_power_asserted'])
        self.assertFalse(report['full_eo_recursion_theorem_asserted'])
        self.assertFalse(report['convergence_radius_asserted'])
        self.assertFalse(report['multi_weight_all_genus_theorem_asserted'])

    def test_wp_jt_sine_curve_is_separate_input(self):
        scope = wp_jt_sine_curve_input()
        self.assertEqual(scope['shadow_curve'], 'y^2 = Q_L(t)')
        self.assertEqual(scope['wp_jt_curve'], 'y = sin(2*pi*sqrt(x))/(4*pi)')
        self.assertFalse(scope['same_spectral_curve'])
        self.assertFalse(scope['wp_jt_from_shadow_curve_certified'])
        self.assertTrue(scope['requires_separate_input'])

    def test_multi_weight_stable_graphs_are_not_included(self):
        scope = multi_weight_stable_graph_scope()
        self.assertFalse(scope['planted_forest_diagnostics_computed'])
        self.assertFalse(scope['multi_weight_stable_graph_data_present'])
        self.assertFalse(scope['multi_weight_cross_channel_terms_included'])
        self.assertFalse(scope['multi_weight_all_genus_theorem_asserted'])
        self.assertIn('stable-graph engine', scope['open_obligation'])

    def test_claim_scope_report_separates_inputs(self):
        report = claim_scope_firewall_report(virasoro_shadow(Fraction(10)))
        self.assertFalse(
            report['shadow_spectral_curve']['certifies_full_eo_recursion']
        )
        self.assertTrue(
            report['stationary_primary_line_riccati']['all_checked_degrees_match']
        )
        self.assertFalse(
            report['finite_scalar_kw_coefficients']['global_kw_tau_theorem_asserted']
        )
        self.assertFalse(report['wp_jt_sine_curve']['same_spectral_curve'])
        self.assertFalse(
            report['multi_weight_stable_graphs']
            ['multi_weight_stable_graph_data_present']
        )
        self.assertFalse(
            report['unsupported_claims']
            ['multi_weight_all_genus_from_scalar_curve']
        )


# =====================================================================
# 11. String and dilaton equations
# =====================================================================

class TestStringEquation(unittest.TestCase):
    """Test string equation verification."""

    def test_base_case(self):
        result = string_equation_check()
        self.assertTrue(result['string_eq_verified'])
        self.assertEqual(result['value'], Rational(1))


class TestDilatonEquation(unittest.TestCase):
    """Test dilaton equation structural check."""

    def test_g1_n1(self):
        result = dilaton_equation_check(None, 1, 1, [])
        # 2*1-2+1 = 1 > 0 so valid
        self.assertTrue(result['valid'])
        self.assertEqual(result['dilaton_factor'], 1)
        self.assertFalse(result['checked_numerically'])

    def test_g0_n2_unstable(self):
        result = dilaton_equation_check(None, 0, 2, [])
        # 2*0-2+2 = 0 <= 0
        self.assertFalse(result['valid'])
        self.assertFalse(result['checked_numerically'])

    def test_g2_n1(self):
        result = dilaton_equation_check(None, 2, 1, [])
        self.assertEqual(result['euler_char'], 3)


# =====================================================================
# 12. Mirror curve (conifold)
# =====================================================================

class TestMirrorCurveConifold(unittest.TestCase):
    """Test mirror curve for resolved conifold."""

    def test_catalan_numbers(self):
        mc = MirrorCurveConifold()
        self.assertEqual(mc.catalan_number(0), 1)
        self.assertEqual(mc.catalan_number(1), 1)
        self.assertEqual(mc.catalan_number(2), 2)
        self.assertEqual(mc.catalan_number(3), 5)
        self.assertEqual(mc.catalan_number(4), 14)

    def test_catalan_formula(self):
        """C_n = (2n)!/((n+1)!*n!)."""
        mc = MirrorCurveConifold()
        for n in range(0, 8):
            expected = int(factorial(2 * n) / (factorial(n + 1) * factorial(n)))
            self.assertEqual(mc.catalan_number(n), expected)

    def test_catalan_recursion(self):
        """C_n = sum_{i=0}^{n-1} C_i * C_{n-1-i}."""
        mc = MirrorCurveConifold()
        for n in range(1, 8):
            expected = sum(mc.catalan_number(i) * mc.catalan_number(n - 1 - i)
                           for i in range(n))
            self.assertEqual(mc.catalan_number(n), expected)


# =====================================================================
# 13. Finite scalar verification report
# =====================================================================

class TestFiniteVerificationReport(unittest.TestCase):
    """Test the finite scalar verification report."""

    def test_virasoro(self):
        data = virasoro_shadow(Fraction(10))
        result = full_verification_suite(data)
        self.assertIn('tower', result)
        self.assertIn('free_energies', result)
        self.assertIn('koszul_dual', result)
        self.assertIn('symplectic', result)
        self.assertIn('wkb', result)
        self.assertIn('claim_scope', result)
        self.assertFalse(
            result['claim_scope']['unsupported_claims']['full_eo_recursion_theorem']
        )

    def test_heisenberg(self):
        data = heisenberg_shadow(Fraction(1))
        result = full_verification_suite(data)
        self.assertIn('tower', result)

    def test_affine(self):
        data = affine_sl2_shadow(Fraction(1))
        result = full_verification_suite(data)
        self.assertIn('free_energies', result)


# =====================================================================
# 14. Self-data conversion utility
# =====================================================================

class TestSelfDataToRat(unittest.TestCase):
    """Test Fraction -> Rational conversion."""

    def test_fraction_conversion(self):
        from sympy import Rational as SRat
        result = self_data_to_rat(Fraction(3, 7))
        self.assertEqual(result, SRat(3, 7))

    def test_int_passthrough(self):
        result = self_data_to_rat(5)
        self.assertEqual(result, 5)


# =====================================================================
# 15. Cross-verification
# =====================================================================

class TestCrossVerification(unittest.TestCase):
    """Multi-path cross-verification tests."""

    def test_F1_three_paths(self):
        """F_1 = kappa/24 verified via:
        Path 1: lambda_fp(1) formula.
        Path 2: kappa * lambda_fp(1).
        Path 3: WKB expansion coefficient.
        """
        data = virasoro_shadow(Fraction(10))
        kappa = Rational(5)

        # Path 1
        self.assertEqual(lambda_fp(1), Rational(1, 24))

        # Path 2
        F1_shadow = kappa * lambda_fp(1)
        self.assertEqual(F1_shadow, Rational(5, 24))

        # Path 3
        wkb = wkb_expansion(data, max_order=1)
        self.assertEqual(wkb[1], Rational(5, 24))

    def test_F2_two_paths(self):
        """F_2 = kappa * lambda_2 verified via two paths."""
        data = virasoro_shadow(Fraction(10))
        kappa = Rational(5)

        F2_path1 = kappa * lambda_fp(2)
        wkb = wkb_expansion(data, max_order=2)
        F2_path2 = wkb[2]
        self.assertEqual(F2_path1, F2_path2)

    def test_kappa_additivity_heisenberg(self):
        """kappa is additive for direct sums: kappa(H_k1 + H_k2) = k1 + k2."""
        k1, k2 = Fraction(3), Fraction(5)
        self.assertEqual(
            heisenberg_shadow(k1).kappa + heisenberg_shadow(k2).kappa,
            k1 + k2
        )

    def test_complementarity_sum_constant(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c_val in [Fraction(1), Fraction(5), Fraction(10), Fraction(13), Fraction(25)]:
            data = virasoro_shadow(c_val)
            dual = koszul_dual_curve(data)
            if dual is not None:
                self.assertEqual(data.kappa + dual.kappa, Fraction(13))

    def test_tower_S2_matches_kappa_all_families(self):
        """S_2 from the tower equals kappa for every family."""
        families = [
            heisenberg_shadow(Fraction(7)),
            affine_sl2_shadow(Fraction(3)),
            virasoro_shadow(Fraction(4)),
        ]
        for data in families:
            tower = shadow_tower_from_QL(data, max_arity=4)
            self.assertEqual(
                tower[2],
                Rational(data.kappa.numerator, data.kappa.denominator),
                f"S_2 mismatch for {data.name}"
            )

    def test_virasoro_Delta_formula(self):
        """Delta = 8*kappa*S4 = 40/(5c+22) for Virasoro.

        Cross-check: at c=2, Delta = 40/32 = 5/4.
        """
        data = virasoro_shadow(Fraction(2))
        expected = Fraction(40, 32)
        self.assertEqual(data.Delta, expected)

    def test_virasoro_Q_L_at_zero(self):
        """Q_L(0) = q0 = 4*kappa^2 = c^2."""
        for c_val in [Fraction(2), Fraction(10)]:
            data = virasoro_shadow(c_val)
            self.assertEqual(data.q0, c_val ** 2)


# =====================================================================
# 16. Package and object firewalls
# =====================================================================

class TestPackageFirewalls(unittest.TestCase):
    """Test package arity, object typing, and kernel constants."""

    def test_holographic_package_has_seven_entries(self):
        self.assertEqual(
            holographic_package_entries(),
            ("A", "A^i", "A^!", "C", "r(z)", "Theta_A", "nabla^hol"),
        )
        self.assertEqual(len(holographic_package_entries()), 7)

    def test_modular_koszul_package_has_six_projections(self):
        self.assertEqual(
            modular_koszul_primary_projections(),
            (
                "Fact_X(L)",
                "barB_X(L)",
                "Theta_L",
                "L_L",
                "(V_L^br, T_L^br)",
                "R_4^mod(L)",
            ),
        )
        self.assertEqual(len(modular_koszul_primary_projections()), 6)
        self.assertNotEqual(
            holographic_package_entries(),
            modular_koszul_primary_projections(),
        )

    def test_bar_koszul_hochschild_objects_are_typed_apart(self):
        roles = typed_firewall_roles()
        self.assertEqual(set(typed_firewall_objects()), set(roles))
        self.assertIn("H^*(B(A))", roles["A^i"])
        self.assertIn("Verdier/continuous-linear dual", roles["A^!"])
        self.assertIn("recovering A", roles["Omega(B(A))"])
        self.assertIn("ChirHoch^*(A,A)", roles["Z_ch^der(A)"])
        self.assertEqual(len(set(roles.values())), len(roles))

    def test_affine_collision_and_kz_constants_are_distinct(self):
        kernel = collision_kernel_constants(
            "affine_km", k=Fraction(3, 2), h_dual=Fraction(2)
        )
        self.assertEqual(kernel["collision_formula"], "3/2*Omega_tr/z")
        self.assertEqual(kernel["raw_coefficient"], Fraction(3, 2))
        self.assertEqual(kernel["kz_formula"], "Omega/((3/2+2)*z)")
        self.assertEqual(kernel["kz_coefficient"], Fraction(2, 7))
        self.assertTrue(kernel["raw_and_kz_distinct"])

    def test_virasoro_kernel_constants(self):
        kernel = collision_kernel_constants("virasoro", c=Fraction(26))
        self.assertEqual(kernel["collision_formula"], "(13)/z^3 + 2T/z")
        self.assertEqual(kernel["central_prefactor"], Fraction(13))
        self.assertEqual(kernel["highest_pole_order"], 3)

    def test_heisenberg_kernel_constant(self):
        kernel = collision_kernel_constants("heisenberg", k=Fraction(5))
        self.assertEqual(kernel["collision_formula"], "5/z")
        self.assertEqual(kernel["raw_coefficient"], Fraction(5))
        self.assertEqual(kernel["pole_order"], 1)


class TestBernoulliNumbers(unittest.TestCase):
    """Test Bernoulli number computation."""

    def test_B0(self):
        self.assertEqual(_bernoulli_number(0), Rational(1))

    def test_B1(self):
        # Sympy convention: B_1 = +1/2 (not -1/2 as in some references)
        self.assertEqual(_bernoulli_number(1), Rational(1, 2))

    def test_B2(self):
        self.assertEqual(_bernoulli_number(2), Rational(1, 6))

    def test_B4(self):
        self.assertEqual(_bernoulli_number(4), Rational(-1, 30))

    def test_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(_bernoulli_number(n), Rational(0))


class TestAdditionalShadowData(unittest.TestCase):
    """Additional tests for shadow data consistency."""

    def test_virasoro_q0_positive(self):
        for c_val in [Fraction(1), Fraction(10), Fraction(25)]:
            data = virasoro_shadow(c_val)
            self.assertGreater(data.q0, 0)

    def test_affine_sl2_q2(self):
        """For sl_2 with S4=0: q2 = 9*alpha^2."""
        data = affine_sl2_shadow(Fraction(1))
        self.assertEqual(data.q2, 9 * data.alpha ** 2)

    def test_w3_depth_class(self):
        data = w3_shadow(Fraction(6))
        self.assertEqual(data.depth_class, 'M')

    def test_heisenberg_constant_QL(self):
        """Heisenberg: Q_L = 4*k^2 (constant, q1=q2=0)."""
        data = heisenberg_shadow(Fraction(5))
        self.assertEqual(data.q1, Fraction(0))
        self.assertEqual(data.q2, Fraction(0))
        self.assertEqual(data.q0, Fraction(100))


if __name__ == '__main__':
    unittest.main()
