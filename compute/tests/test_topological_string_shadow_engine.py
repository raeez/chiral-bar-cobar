r"""Tests for topological string amplitudes from the shadow obstruction tower.

Verifies:
 1. Conifold F_g for g=1,...,5 (exact rational numbers)
 2. GV integrality: n_g^d in Z for all computed cases
 3. BCOV splitting from MC equation
 4. Castelnuovo bound from shadow depth
 5. Local P^2 GV invariants match KKV
 6. Constant map contribution formula
 7. Gap condition for compact CY3
 8. AGT at self-dual point
 9. Modular properties of F_g under monodromy
10. Genus-0 prepotential matches classical intersection theory
11. Large-radius limit
12. GV coefficient expansion consistency
13. Shadow free energy formula
14. GV multi-covering roundtrip
15. Ahat generating function identity
16. Kodaira-Spencer amplitudes
17. CY data construction
18. Shadow-top string dictionary completeness
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, bernoulli, factorial, simplify, Integer

from compute.lib.topological_string_shadow_engine import (
    # Bernoulli / Faber-Pandharipande
    _bernoulli_number,
    lambda_fp,
    # CY data
    CYData,
    resolved_conifold,
    local_P2,
    local_P1xP1,
    quintic,
    # Constant map
    constant_map_Fg,
    shadow_free_energy,
    verify_conifold_Fg_formula,
    # GV invariants
    conifold_gv_invariants,
    local_P2_gv,
    gv_to_Fg,
    extract_gv_from_Fg,
    verify_gv_integrality,
    _gv_coefficient,
    _inverse_sine_sq_coeff,
    _sinc_power_coeff,
    # Conifold
    conifold_Fg,
    conifold_Fg_instanton_coefficients,
    conifold_prepotential_coefficients,
    # Castelnuovo
    castelnuovo_bound_P2,
    castelnuovo_bound_P1,
    verify_castelnuovo,
    # BCOV
    BCOVData,
    verify_bcov_splitting_conifold,
    # Gap
    verify_gap_condition,
    # AGT
    nekrasov_selfdual_genus_expansion,
    # Monodromy
    conifold_monodromy_weight,
    # Prepotential
    local_P2_prepotential_coefficients,
    # Dictionary
    shadow_topstring_dictionary,
    # KS amplitudes
    kodaira_spencer_amplitude,
    # Ahat
    ahat_generating_function,
    # GV table
    gv_table,
    compute_gv_invariants,
    large_radius_Fg,
    full_verification_suite,
)


# ====================================================================
# Section 1: Faber-Pandharipande numbers (foundation)
# ====================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify lambda_g^FP intersection numbers."""

    def test_lambda_1(self):
        self.assertEqual(lambda_fp(1), Rational(1, 24))

    def test_lambda_2(self):
        self.assertEqual(lambda_fp(2), Rational(7, 5760))

    def test_lambda_3(self):
        self.assertEqual(lambda_fp(3), Rational(31, 967680))

    def test_lambda_4(self):
        # (2^7 - 1)/2^7 * |B_8|/8! = 127/128 * (1/30)/40320
        self.assertEqual(lambda_fp(4), Rational(127, 154828800))

    def test_lambda_5(self):
        self.assertEqual(lambda_fp(5), Rational(73, 3503554560))

    def test_lambda_positive(self):
        """All lambda_g^FP must be positive (AP22)."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_lambda_decreasing(self):
        """lambda_g^FP is decreasing for g >= 1."""
        for g in range(1, 7):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1))


# ====================================================================
# Section 2: Calabi-Yau geometry data
# ====================================================================

class TestCYData(unittest.TestCase):
    """Verify CY threefold data construction."""

    def test_conifold_chi(self):
        cy = resolved_conifold()
        self.assertEqual(cy.chi, 2)
        self.assertEqual(cy.h11, 1)
        self.assertFalse(cy.is_compact)

    def test_conifold_kappa(self):
        cy = resolved_conifold()
        self.assertEqual(cy.kappa_shadow, Rational(1))

    def test_local_P2_chi(self):
        cy = local_P2()
        self.assertEqual(cy.chi, 3)
        self.assertEqual(cy.kappa_shadow, Rational(3, 2))

    def test_local_P1xP1_chi(self):
        cy = local_P1xP1()
        self.assertEqual(cy.chi, 4)
        self.assertEqual(cy.kappa_shadow, Rational(2))

    def test_quintic_chi(self):
        cy = quintic()
        self.assertEqual(cy.chi, -200)
        self.assertEqual(cy.h11, 1)
        self.assertEqual(cy.h21, 101)
        self.assertTrue(cy.is_compact)
        self.assertEqual(cy.kappa_shadow, Rational(-100))

    def test_quintic_hodge_sum(self):
        """chi = 2(h^{1,1} - h^{2,1}) for CY3."""
        cy = quintic()
        self.assertEqual(cy.chi, 2 * (cy.h11 - cy.h21))


# ====================================================================
# Section 3: Conifold free energies (exact)
# ====================================================================

class TestConifoldFg(unittest.TestCase):
    """Verify exact conifold free energies F_g."""

    def test_F1_conifold(self):
        """F_1 = 1/12 for the resolved conifold."""
        self.assertEqual(conifold_Fg(1), Rational(1, 12))

    def test_F2_conifold(self):
        """F_2 = (-1)^1 B_4 / (4*2) = (1/30)/8 = 1/240."""
        self.assertEqual(conifold_Fg(2), Rational(1, 240))

    def test_F3_conifold(self):
        """F_3 = (-1)^2 B_6 / (6*4) = (1/42)/24 = 1/1008."""
        self.assertEqual(conifold_Fg(3), Rational(1, 1008))

    def test_F4_conifold(self):
        """F_4 = (-1)^3 B_8 / (8*6) = (1/30)/48 = 1/1440."""
        self.assertEqual(conifold_Fg(4), Rational(1, 1440))

    def test_F5_conifold(self):
        """F_5 = (-1)^4 B_10 / (10*8) = (5/66)/80 = 5/5280 = 1/1056."""
        self.assertEqual(conifold_Fg(5), Rational(1, 1056))

    def test_conifold_formula_verification(self):
        """Verify F_g = (-1)^{g-1} B_{2g} / (2g(2g-2)) for all g."""
        for g in range(1, 8):
            Fg, correct = verify_conifold_Fg_formula(g)
            self.assertTrue(correct, f"Conifold formula fails at g={g}")

    def test_conifold_Fg_positive(self):
        """All conifold F_g should be positive."""
        for g in range(1, 8):
            self.assertGreater(conifold_Fg(g), 0,
                               f"F_{g}^con = {conifold_Fg(g)} should be positive")

    def test_conifold_Fg_invalid_genus(self):
        with self.assertRaises(ValueError):
            conifold_Fg(0)


# ====================================================================
# Section 4: Constant map contribution
# ====================================================================

class TestConstantMapContribution(unittest.TestCase):
    """Verify F_g^{const} = (-1)^g chi B_{2g} B_{2g-2} / (4g(2g-2)(2g-2)!)."""

    def test_quintic_F2(self):
        """F_2^{const}(quintic) = (-1)^2 (-200) (-1/30)(1/6) / (4*2*2*2!)."""
        # = (-200)(-1/30)(1/6) / 32 = (-200)(- 1/180) / 32 = 200/(180*32) = 5/144
        self.assertEqual(constant_map_Fg(2, -200), Rational(5, 144))

    def test_conifold_const_map_F2(self):
        """Constant map for conifold (chi=2) at g=2."""
        # (-1)^2 * 2 * (-1/30) * (1/6) / (4*2*2*2!) = 2 * (-1/180) / 32 = -1/2880
        self.assertEqual(constant_map_Fg(2, 2), Rational(-1, 2880))

    def test_constant_map_sign_pattern(self):
        """For quintic (chi < 0), F_g^const alternates sign starting positive."""
        # B_{2g} has sign (-1)^{g+1}, B_{2g-2} has sign (-1)^g
        # Product: (-1)^{2g+1} = -1 always
        # With (-1)^g * chi: (-1)^g * (-200) * (-1) = 200 * (-1)^{g+1}
        # So F_2 > 0, F_3 < 0, F_4 > 0, ...
        self.assertGreater(constant_map_Fg(2, -200), 0)
        self.assertLess(constant_map_Fg(3, -200), 0)
        self.assertGreater(constant_map_Fg(4, -200), 0)

    def test_constant_map_invalid_genus(self):
        with self.assertRaises(ValueError):
            constant_map_Fg(1, 2)


# ====================================================================
# Section 5: Shadow free energy
# ====================================================================

class TestShadowFreeEnergy(unittest.TestCase):
    """Verify F_g^{shadow} = kappa * lambda_g^FP."""

    def test_shadow_F1(self):
        """F_1 = kappa/24."""
        for kappa in [Rational(1), Rational(1, 2), Rational(25, 2)]:
            self.assertEqual(shadow_free_energy(1, kappa), kappa * Rational(1, 24))

    def test_shadow_F2(self):
        """F_2 = kappa * 7/5760."""
        self.assertEqual(shadow_free_energy(2, Rational(1)),
                         Rational(7, 5760))

    def test_shadow_linearity_in_kappa(self):
        """Shadow free energy is linear in kappa (additivity)."""
        k1 = Rational(3)
        k2 = Rational(5)
        for g in range(1, 5):
            self.assertEqual(
                shadow_free_energy(g, k1) + shadow_free_energy(g, k2),
                shadow_free_energy(g, k1 + k2)
            )

    def test_shadow_different_from_constant_map(self):
        """Shadow free energy != constant map contribution in general.

        These are different intersection numbers on M_g.
        """
        kappa = Rational(1)  # chi = 2
        F_shadow = shadow_free_energy(2, kappa)
        F_const = constant_map_Fg(2, 2)
        self.assertNotEqual(F_shadow, F_const)


# ====================================================================
# Section 6: GV coefficient expansion
# ====================================================================

class TestGVCoefficients(unittest.TestCase):
    """Verify (2 sin(x/2))^{2h-2} expansion coefficients."""

    def test_inverse_sine_sq_g0(self):
        """Coefficient of x^{-2} in (2sin(x/2))^{-2} is 1."""
        self.assertEqual(_inverse_sine_sq_coeff(0), Rational(1))

    def test_inverse_sine_sq_g1(self):
        """Coefficient of x^0 in (2sin(x/2))^{-2} is 1/12."""
        self.assertEqual(_inverse_sine_sq_coeff(1), Rational(1, 12))

    def test_inverse_sine_sq_g2(self):
        """Coefficient of x^2 in (2sin(x/2))^{-2} is 1/240."""
        self.assertEqual(_inverse_sine_sq_coeff(2), Rational(1, 240))

    def test_inverse_sine_sq_g3(self):
        """Coefficient of x^4 in (2sin(x/2))^{-2} is 1/6048."""
        self.assertEqual(_inverse_sine_sq_coeff(3), Rational(1, 6048))

    def test_inverse_sine_sq_g4(self):
        """Coefficient of x^6 is 1/172800."""
        self.assertEqual(_inverse_sine_sq_coeff(4), Rational(1, 172800))

    def test_inverse_sine_sq_g5(self):
        """Coefficient of x^8 is 1/5322240."""
        self.assertEqual(_inverse_sine_sq_coeff(5), Rational(1, 5322240))

    def test_gv_coeff_h0(self):
        """c_{g,0} = [x^{2g-2}] (2sin(x/2))^{-2}."""
        for g in range(6):
            self.assertEqual(_gv_coefficient(g, 0), _inverse_sine_sq_coeff(g))

    def test_gv_coeff_h1(self):
        """c_{g,1} = delta_{g,1}."""
        self.assertEqual(_gv_coefficient(0, 1), Rational(0))
        self.assertEqual(_gv_coefficient(1, 1), Rational(1))
        self.assertEqual(_gv_coefficient(2, 1), Rational(0))
        self.assertEqual(_gv_coefficient(3, 1), Rational(0))

    def test_gv_coeff_diagonal(self):
        """c_{g,g} = 1 for all g >= 0 (leading term)."""
        for g in range(6):
            self.assertEqual(_gv_coefficient(g, g), Rational(1))

    def test_gv_coeff_below_diagonal(self):
        """c_{g,h} = 0 for h > g and h >= 1."""
        for g in range(5):
            for h in range(g + 1, g + 3):
                if h >= 1:
                    self.assertEqual(_gv_coefficient(g, h), Rational(0))

    def test_sinc_power_m0(self):
        """(sinc(x/2))^p at x=0 is 1."""
        for p in range(1, 5):
            self.assertEqual(_sinc_power_coeff(p, 0), Rational(1))


# ====================================================================
# Section 7: GV integrality
# ====================================================================

class TestGVIntegrality(unittest.TestCase):
    """Verify Gopakumar-Vafa invariants are integers."""

    def test_conifold_gv_values(self):
        """Conifold: n_0^d = 1 for all d, n_g^d = 0 for g >= 1."""
        gv = conifold_gv_invariants(3, 10)
        for d in range(1, 11):
            self.assertEqual(gv[(0, d)], 1)
            for g in range(1, 4):
                self.assertEqual(gv[(g, d)], 0)

    def test_conifold_gv_integrality(self):
        gv = conifold_gv_invariants(5, 10)
        all_int, failures = verify_gv_integrality(gv)
        self.assertTrue(all_int, f"Non-integer GV: {failures}")

    def test_local_P2_gv_integrality(self):
        gv = local_P2_gv(4, 10)
        all_int, failures = verify_gv_integrality(gv)
        self.assertTrue(all_int, f"Non-integer GV: {failures}")

    def test_local_P2_genus0_values(self):
        """Verify specific GV invariants for local P^2 at genus 0."""
        gv = local_P2_gv(0, 5)
        self.assertEqual(gv[(0, 1)], 3)
        self.assertEqual(gv[(0, 2)], -6)
        self.assertEqual(gv[(0, 3)], 27)
        self.assertEqual(gv[(0, 4)], -192)
        self.assertEqual(gv[(0, 5)], 1695)

    def test_local_P2_genus1_values(self):
        """Verify genus-1 GV for local P^2."""
        gv = local_P2_gv(1, 6)
        self.assertEqual(gv[(1, 1)], 0)
        self.assertEqual(gv[(1, 2)], 0)
        self.assertEqual(gv[(1, 3)], -10)
        self.assertEqual(gv[(1, 4)], 231)
        self.assertEqual(gv[(1, 5)], -4452)
        self.assertEqual(gv[(1, 6)], 80948)

    def test_local_P2_higher_genus_values(self):
        """Check selected higher-genus GV for local P^2."""
        gv = local_P2_gv(4, 10)
        self.assertEqual(gv[(2, 5)], 15)
        self.assertEqual(gv[(2, 6)], -1136)
        self.assertEqual(gv[(3, 7)], -21)
        self.assertEqual(gv[(3, 8)], 3426)
        self.assertEqual(gv[(4, 9)], 28)
        self.assertEqual(gv[(4, 10)], -10488)


# ====================================================================
# Section 8: GV multi-covering roundtrip
# ====================================================================

class TestGVRoundtrip(unittest.TestCase):
    """Verify GV -> N_{g,d} -> GV roundtrip."""

    def test_conifold_roundtrip(self):
        """Conifold: extract GV from computed N_{g,d}, should recover input."""
        g_max, d_max = 3, 8
        gv_known = conifold_gv_invariants(g_max, d_max)
        Fg_inst = gv_to_Fg(gv_known, g_max, d_max)
        gv_extracted = extract_gv_from_Fg(Fg_inst, g_max, d_max)
        for g in range(g_max + 1):
            for d in range(1, d_max + 1):
                self.assertEqual(
                    gv_extracted.get((g, d), Rational(0)),
                    gv_known.get((g, d), 0),
                    f"Roundtrip fails at (g,d)=({g},{d})"
                )

    def test_local_P2_roundtrip(self):
        """Local P^2: GV -> N_{g,d} -> GV roundtrip."""
        g_max, d_max = 3, 8
        gv_known = local_P2_gv(g_max, d_max)
        Fg_inst = gv_to_Fg(gv_known, g_max, d_max)
        gv_extracted = extract_gv_from_Fg(Fg_inst, g_max, d_max)
        for g in range(g_max + 1):
            for d in range(1, d_max + 1):
                self.assertEqual(
                    gv_extracted.get((g, d), Rational(0)),
                    gv_known.get((g, d), 0),
                    f"Roundtrip fails at (g,d)=({g},{d})"
                )

    def test_extracted_gv_integrality_conifold(self):
        """GV extracted from conifold Fg data should be integers."""
        g_max, d_max = 4, 6
        gv_known = conifold_gv_invariants(g_max, d_max)
        Fg_inst = gv_to_Fg(gv_known, g_max, d_max)
        gv_extracted = extract_gv_from_Fg(Fg_inst, g_max, d_max)
        all_int, failures = verify_gv_integrality(gv_extracted)
        self.assertTrue(all_int, f"Non-integer extracted GV: {failures}")

    def test_extracted_gv_integrality_P2(self):
        """GV extracted from local P^2 Fg data should be integers."""
        g_max, d_max = 3, 6
        gv_known = local_P2_gv(g_max, d_max)
        Fg_inst = gv_to_Fg(gv_known, g_max, d_max)
        gv_extracted = extract_gv_from_Fg(Fg_inst, g_max, d_max)
        all_int, failures = verify_gv_integrality(gv_extracted)
        self.assertTrue(all_int, f"Non-integer extracted GV: {failures}")


# ====================================================================
# Section 9: Castelnuovo bound
# ====================================================================

class TestCastelnuovoBound(unittest.TestCase):
    """Verify GV invariants respect Castelnuovo bounds."""

    def test_castelnuovo_P2_values(self):
        """Check specific Castelnuovo bounds for P^2."""
        self.assertEqual(castelnuovo_bound_P2(1), 0)
        self.assertEqual(castelnuovo_bound_P2(2), 0)
        self.assertEqual(castelnuovo_bound_P2(3), 1)
        self.assertEqual(castelnuovo_bound_P2(4), 3)
        self.assertEqual(castelnuovo_bound_P2(5), 6)
        self.assertEqual(castelnuovo_bound_P2(6), 10)

    def test_castelnuovo_P1(self):
        """For conifold (P^1 base): g_max = 0 for all d."""
        for d in range(1, 11):
            self.assertEqual(castelnuovo_bound_P1(d), 0)

    def test_conifold_respects_castelnuovo(self):
        """Conifold GV invariants respect g_max = 0."""
        gv = conifold_gv_invariants(5, 10)
        violations = verify_castelnuovo(gv, castelnuovo_bound_P1, 10)
        self.assertEqual(violations, [])

    def test_local_P2_respects_castelnuovo(self):
        """Local P^2 GV invariants respect Castelnuovo bound."""
        gv = local_P2_gv(4, 10)
        violations = verify_castelnuovo(gv, castelnuovo_bound_P2, 10)
        self.assertEqual(violations, [])

    def test_local_P2_boundary_saturation(self):
        """Some GV invariants saturate the Castelnuovo bound."""
        gv = local_P2_gv(1, 3)
        # n_1^3 = -10 != 0, and g_max(3) = 1. So genus 1, degree 3 saturates.
        self.assertNotEqual(gv[(1, 3)], 0)
        self.assertEqual(castelnuovo_bound_P2(3), 1)


# ====================================================================
# Section 10: BCOV splitting from MC equation
# ====================================================================

class TestBCOVSplitting(unittest.TestCase):
    """Verify MC/BCOV splitting relations."""

    def test_bcov_splitting_rational(self):
        """Splitting ratios are rational numbers."""
        bcov = verify_bcov_splitting_conifold(6)
        for g, data in bcov.items():
            ratio = data['ratio']
            self.assertIsNotNone(ratio)
            # Ratio should be a rational number
            self.assertIsInstance(ratio, Rational)

    def test_bcov_splitting_positive(self):
        """Splitting sums are positive."""
        bcov = verify_bcov_splitting_conifold(6)
        for g, data in bcov.items():
            self.assertGreater(data['splitting_lambda_sum'], 0)

    def test_bcov_splitting_grows(self):
        """Splitting ratios increase with genus."""
        bcov = verify_bcov_splitting_conifold(6)
        ratios = [float(bcov[g]['ratio']) for g in range(2, 7)]
        for i in range(len(ratios) - 1):
            self.assertLess(ratios[i], ratios[i + 1])

    def test_bcov_g2_ratio(self):
        """At g=2: splitting ratio = 10/7."""
        bcov = verify_bcov_splitting_conifold(3)
        self.assertEqual(bcov[2]['ratio'], Rational(10, 7))

    def test_bcov_g3_ratio(self):
        """At g=3: splitting ratio = 98/31."""
        bcov = verify_bcov_splitting_conifold(4)
        self.assertEqual(bcov[3]['ratio'], Rational(98, 31))


# ====================================================================
# Section 11: Gap condition
# ====================================================================

class TestGapCondition(unittest.TestCase):
    """Verify gap condition for compact CY3."""

    def test_quintic_gap(self):
        """Quintic: gap condition satisfied at all verified genera."""
        gap = verify_gap_condition(None, -200, 5)
        for g, data in gap.items():
            self.assertTrue(data['gap_satisfied'])

    def test_quintic_shadow_constant_map_structure(self):
        """For quintic, shadow and constant map have same structure."""
        gap = verify_gap_condition(None, -200, 5)
        for g, data in gap.items():
            # Both F_const and F_shadow should be nonzero
            self.assertNotEqual(data['F_const'], 0)
            self.assertNotEqual(data['F_shadow'], 0)

    def test_large_radius_limit(self):
        """At t -> infinity, F_g -> F_g^{const}."""
        for g in range(2, 6):
            F_lr = large_radius_Fg(g, -200)
            F_const = constant_map_Fg(g, -200)
            self.assertEqual(F_lr, F_const)


# ====================================================================
# Section 12: AGT at self-dual point
# ====================================================================

class TestAGTSelfdual(unittest.TestCase):
    """Verify AGT correspondence at self-dual Omega-background."""

    def test_selfdual_central_charge(self):
        """At eps1 = -eps2: c = 25."""
        result = nekrasov_selfdual_genus_expansion(Rational(1), max_inst=1)
        self.assertEqual(result['c'], 25)

    def test_selfdual_kappa(self):
        """At eps1 = -eps2: kappa = 25/2."""
        result = nekrasov_selfdual_genus_expansion(Rational(1), max_inst=1)
        self.assertEqual(result['kappa'], Rational(25, 2))

    def test_selfdual_beta_zero(self):
        """At eps1 = -eps2: beta = 0 (undeformed)."""
        result = nekrasov_selfdual_genus_expansion(Rational(1), max_inst=1)
        self.assertEqual(result['beta'], 0)

    def test_selfdual_Z0(self):
        """Z_0 = 1 (perturbative normalization)."""
        result = nekrasov_selfdual_genus_expansion(Rational(1), max_inst=2)
        self.assertEqual(result['Z_coefficients'][0], 1)

    def test_selfdual_Z1_nonzero(self):
        """Z_1 should be nonzero (first instanton contribution)."""
        result = nekrasov_selfdual_genus_expansion(Rational(1), max_inst=2)
        self.assertNotEqual(result['Z_coefficients'][1], 0)


# ====================================================================
# Section 13: Modular / monodromy properties
# ====================================================================

class TestMonodromyProperties(unittest.TestCase):
    """Verify modular/monodromy weights of F_g."""

    def test_monodromy_weights(self):
        """F_g has monodromy weight 2g-2."""
        for g in range(0, 6):
            self.assertEqual(conifold_monodromy_weight(g), 2*g - 2)

    def test_weight_pattern(self):
        """Weight pattern: -2, 0, 2, 4, 6, ..."""
        weights = [conifold_monodromy_weight(g) for g in range(6)]
        self.assertEqual(weights, [-2, 0, 2, 4, 6, 8])


# ====================================================================
# Section 14: Genus-0 prepotential
# ====================================================================

class TestPrepotential(unittest.TestCase):
    """Verify genus-0 instanton coefficients."""

    def test_conifold_N01(self):
        """N_{0,1} = 1 for conifold (single cover of the BPS state)."""
        coeffs = conifold_prepotential_coefficients(5)
        self.assertEqual(coeffs[1], Rational(1))

    def test_conifold_N02(self):
        """N_{0,2} = 1 + 1/8 = 9/8 (degree 2: single and double covers)."""
        coeffs = conifold_prepotential_coefficients(5)
        self.assertEqual(coeffs[2], Rational(9, 8))

    def test_conifold_N0d_divisor_sum(self):
        """N_{0,d} = sigma_{-3}(d) for all d."""
        coeffs = conifold_prepotential_coefficients(10)
        for d in range(1, 11):
            sigma = sum(Rational(1, k**3) for k in range(1, d+1) if d % k == 0)
            self.assertEqual(coeffs[d], sigma)

    def test_local_P2_N01(self):
        """N_{0,1}(P^2) = n_0^1 = 3 (no multi-covering at d=1)."""
        coeffs = local_P2_prepotential_coefficients(3)
        self.assertEqual(coeffs[1], Rational(3))

    def test_local_P2_N02(self):
        """N_{0,2}(P^2) = n_0^2 + n_0^1/8 = -6 + 3/8 = -45/8."""
        coeffs = local_P2_prepotential_coefficients(3)
        self.assertEqual(coeffs[2], Rational(-45, 8))


# ====================================================================
# Section 15: Conifold instanton coefficients
# ====================================================================

class TestConifoldInstanton(unittest.TestCase):
    """Verify higher-genus instanton coefficients for conifold."""

    def test_N_g1_d1(self):
        """N_{1,1}^{con} = c_{1,0} = 1/12."""
        coeffs = conifold_Fg_instanton_coefficients(1, 5)
        self.assertEqual(coeffs[1], Rational(1, 12))

    def test_N_g2_d1(self):
        """N_{2,1}^{con} = c_{2,0} = 1/240."""
        coeffs = conifold_Fg_instanton_coefficients(2, 5)
        self.assertEqual(coeffs[1], Rational(1, 240))

    def test_N_g1_sigma(self):
        """N_{1,d}^{con} = (1/12) * sigma_{-3}(d)."""
        coeffs = conifold_Fg_instanton_coefficients(1, 10)
        for d in range(1, 11):
            sigma = sum(Rational(1, k**3) for k in range(1, d+1) if d % k == 0)
            self.assertEqual(coeffs[d], Rational(1, 12) * sigma)


# ====================================================================
# Section 16: Kodaira-Spencer amplitudes
# ====================================================================

class TestKodairaSpencer(unittest.TestCase):
    """Verify KS field theory amplitudes from shadow tower."""

    def test_KS_g1_n0(self):
        """KS amplitude A_{1,0} = kappa * lambda_1 = kappa/24."""
        kappa = Rational(1)
        self.assertEqual(kodaira_spencer_amplitude(1, 0, kappa), kappa / 24)

    def test_KS_g2_n0(self):
        """KS amplitude A_{2,0} = kappa * lambda_2 = 7*kappa/5760."""
        kappa = Rational(5)
        expected = kappa * Rational(7, 5760)
        self.assertEqual(kodaira_spencer_amplitude(2, 0, kappa), expected)

    def test_KS_g1_n1(self):
        """KS amplitude A_{1,1} = kappa/24."""
        kappa = Rational(1)
        self.assertEqual(kodaira_spencer_amplitude(1, 1, kappa), kappa / 24)

    def test_KS_unstable(self):
        """Unstable cases (2g-2+n <= 0) return 0 except (0,3)."""
        kappa = Rational(1)
        self.assertEqual(kodaira_spencer_amplitude(0, 0, kappa), 0)
        self.assertEqual(kodaira_spencer_amplitude(0, 1, kappa), 0)
        self.assertEqual(kodaira_spencer_amplitude(0, 2, kappa), 0)

    def test_KS_yukawa(self):
        """(0,3) amplitude = Yukawa coupling = normalized to 1."""
        kappa = Rational(1)
        self.assertEqual(kodaira_spencer_amplitude(0, 3, kappa), 1)


# ====================================================================
# Section 17: Ahat generating function identity
# ====================================================================

class TestAhatGeneratingFunction(unittest.TestCase):
    """Verify A-hat GF identity: F_g = kappa * [x^{2g}] (Ahat(ix) - 1)."""

    def test_ahat_first_few_coeffs(self):
        """A-hat GF coefficients match lambda_g^FP."""
        ahat = ahat_generating_function(5)
        self.assertEqual(ahat[1], lambda_fp(1))
        self.assertEqual(ahat[2], lambda_fp(2))
        self.assertEqual(ahat[3], lambda_fp(3))
        self.assertEqual(ahat[4], lambda_fp(4))
        self.assertEqual(ahat[5], lambda_fp(5))

    def test_ahat_positive(self):
        """All Ahat(ix)-1 coefficients are positive (AP22)."""
        ahat = ahat_generating_function(8)
        for g, coeff in ahat.items():
            self.assertGreater(coeff, 0,
                               f"Ahat coefficient at g={g} should be positive")


# ====================================================================
# Section 18: Shadow-topological string dictionary
# ====================================================================

class TestDictionary(unittest.TestCase):
    """Verify completeness of the shadow <-> top string dictionary."""

    def test_dictionary_nonempty(self):
        d = shadow_topstring_dictionary()
        self.assertGreater(len(d), 0)

    def test_dictionary_keys(self):
        d = shadow_topstring_dictionary()
        expected_keys = {'kappa', 'MC equation', 'shadow depth r_max'}
        for key in expected_keys:
            self.assertIn(key, d)

    def test_dictionary_values_nonempty(self):
        d = shadow_topstring_dictionary()
        for key, val in d.items():
            self.assertGreater(len(val), 0, f"Empty value for key '{key}'")


# ====================================================================
# Section 19: GV table formatting
# ====================================================================

class TestGVTable(unittest.TestCase):
    """Test GV table formatting."""

    def test_conifold_table(self):
        gv = conifold_gv_invariants(2, 5)
        table = gv_table(gv, 2, 5)
        self.assertIn('1', table)
        self.assertIn('0', table)

    def test_local_P2_table(self):
        gv = local_P2_gv(2, 5)
        table = gv_table(gv, 2, 5)
        self.assertIn('3', table)
        self.assertIn('-6', table)


# ====================================================================
# Section 20: Compute GV dispatcher
# ====================================================================

class TestComputeGVDispatcher(unittest.TestCase):
    """Test the compute_gv_invariants dispatcher."""

    def test_conifold_dispatch(self):
        cy = resolved_conifold()
        gv = compute_gv_invariants(cy, 2, 5)
        self.assertEqual(gv[(0, 1)], 1)
        self.assertEqual(gv[(1, 1)], 0)

    def test_P2_dispatch(self):
        cy = local_P2()
        gv = compute_gv_invariants(cy, 2, 5)
        self.assertEqual(gv[(0, 1)], 3)
        self.assertEqual(gv[(0, 2)], -6)

    def test_unknown_cy_dispatch(self):
        cy = quintic()
        gv = compute_gv_invariants(cy, 2, 5)
        self.assertEqual(gv, {})


# ====================================================================
# Section 21: Cross-checks between formulas
# ====================================================================

class TestCrossChecks(unittest.TestCase):
    """Cross-checks verifying internal consistency."""

    def test_conifold_F_equals_c_sigma(self):
        """For conifold: F_g^{inst} = c_{g,0} * Li_{3-2g}(q) at each degree."""
        for g in range(1, 4):
            coeffs = conifold_Fg_instanton_coefficients(g, 5)
            c_g0 = _gv_coefficient(g, 0)
            for d in range(1, 6):
                sigma = sum(Rational(1, k**3) for k in range(1, d+1) if d % k == 0)
                self.assertEqual(coeffs[d], c_g0 * sigma)

    def test_gv_summation_genus0_conifold(self):
        """At genus 0: N_{0,d} = sigma_{-3}(d) for the conifold."""
        gv = conifold_gv_invariants(0, 10)
        Fg = gv_to_Fg(gv, 0, 10)
        prep = conifold_prepotential_coefficients(10)
        for d in range(1, 11):
            self.assertEqual(Fg[0][d], prep[d])

    def test_local_P2_genus0_sign_pattern(self):
        """Local P^2 genus-0: n_0^d alternates sign starting positive."""
        gv = local_P2_gv(0, 6)
        self.assertGreater(gv[(0, 1)], 0)
        self.assertLess(gv[(0, 2)], 0)
        self.assertGreater(gv[(0, 3)], 0)
        self.assertLess(gv[(0, 4)], 0)
        self.assertGreater(gv[(0, 5)], 0)
        self.assertLess(gv[(0, 6)], 0)

    def test_castelnuovo_monotone(self):
        """Castelnuovo bound is non-decreasing in d."""
        for d in range(1, 20):
            self.assertLessEqual(castelnuovo_bound_P2(d),
                                 castelnuovo_bound_P2(d + 1))


# ====================================================================
# Section 22: Full verification suite
# ====================================================================

class TestFullVerificationSuite(unittest.TestCase):
    """Run the comprehensive verification suite."""

    def test_suite_runs(self):
        """Full suite runs without error."""
        results = full_verification_suite(g_max=4, d_max=6)
        self.assertIn('conifold_Fg', results)
        self.assertIn('conifold_gv_integrality', results)
        self.assertIn('local_P2_gv_integrality', results)
        self.assertIn('bcov_splitting', results)

    def test_suite_conifold_integrality(self):
        results = full_verification_suite(g_max=4, d_max=6)
        self.assertTrue(results['conifold_gv_integrality']['all_integer'])

    def test_suite_P2_integrality(self):
        results = full_verification_suite(g_max=4, d_max=6)
        self.assertTrue(results['local_P2_gv_integrality']['all_integer'])

    def test_suite_castelnuovo(self):
        results = full_verification_suite(g_max=4, d_max=6)
        self.assertEqual(results['conifold_castelnuovo']['violations'], [])
        self.assertEqual(results['local_P2_castelnuovo']['violations'], [])


# ====================================================================
# Section 23: Bernoulli number sanity
# ====================================================================

class TestBernoulliSanity(unittest.TestCase):
    """Verify Bernoulli numbers used in computations."""

    def test_B2(self):
        self.assertEqual(_bernoulli_number(2), Rational(1, 6))

    def test_B4(self):
        self.assertEqual(_bernoulli_number(4), Rational(-1, 30))

    def test_B6(self):
        self.assertEqual(_bernoulli_number(6), Rational(1, 42))

    def test_B8(self):
        self.assertEqual(_bernoulli_number(8), Rational(-1, 30))

    def test_B10(self):
        self.assertEqual(_bernoulli_number(10), Rational(5, 66))

    def test_B12(self):
        self.assertEqual(_bernoulli_number(12), Rational(-691, 2730))

    def test_bernoulli_sign_pattern(self):
        """B_{2g} has sign (-1)^{g+1} for g >= 1."""
        for g in range(1, 8):
            B = _bernoulli_number(2 * g)
            expected_sign = (-1)**(g + 1)
            self.assertEqual(B / abs(B), expected_sign,
                             f"B_{2*g} = {B} has wrong sign")


# ====================================================================
# Section 24: Edge cases and error handling
# ====================================================================

class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    def test_lambda_fp_invalid(self):
        with self.assertRaises(ValueError):
            lambda_fp(0)

    def test_constant_map_invalid(self):
        with self.assertRaises(ValueError):
            constant_map_Fg(1, 2)

    def test_shadow_free_energy_invalid(self):
        with self.assertRaises(ValueError):
            shadow_free_energy(0, Rational(1))

    def test_large_radius_invalid(self):
        with self.assertRaises(ValueError):
            large_radius_Fg(1, -200)

    def test_conifold_Fg_invalid(self):
        with self.assertRaises(ValueError):
            conifold_Fg(0)

    def test_ks_invalid(self):
        with self.assertRaises(ValueError):
            kodaira_spencer_amplitude(-1, 0, Rational(1))

    def test_empty_gv_integrality(self):
        """Empty dict should be all-integer."""
        all_int, failures = verify_gv_integrality({})
        self.assertTrue(all_int)
        self.assertEqual(failures, [])


if __name__ == '__main__':
    unittest.main()
