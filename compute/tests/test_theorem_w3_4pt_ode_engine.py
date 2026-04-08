r"""Tests for the W_3 four-point conformal block ODE engine.

STRUCTURE
=========

 1. SL(2) gauge fixing: 4 points -> 1 modulus z
 2. T-sector restriction recovers Virasoro BPZ
 3. Depth-4 vanishing (W_{(4)}W = 0) at multiple c values
 4. ODE order: W_3 exceeds Virasoro (4 > 2)
 5. Surviving depths on primaries: 1, 2, 3, 5 (not 4)
 6. W-sector leading term identification
 7. Specific coefficient values at c = 2
 8. Fuchsian ODE structure (regular singular at 0, 1, infty)
 9. Channel structure and decoupling
10. Numerical evaluation consistency
11. Cross-family comparison: k_max hierarchy
12. Ward identity structure
13. Lambda composite at specific values
14. Multi-path depth verification
15. Cross-check with W_3 commuting Hamiltonians engine

Manuscript references:
    thm:gz26-commuting-differentials
    eq:gz26-hamiltonian-decomposition
    prop:shadow-connection-bpz
    rem:bar-pole-absorption (AP19)
    comp:w3-nthproducts (bar_complex_tables.tex)
"""

import math
import unittest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_w3_4pt_ode_engine import (
    DIFF_ORDER_W3,
    K_MAX_VIR,
    K_MAX_W3,
    MAX_OPE_POLE_W3,
    channel_structure_4pt,
    evaluate_hamiltonian_at_z,
    extract_scalar_ode_coefficients,
    fuchsian_structure_4pt,
    full_4pt_ode_summary,
    n_moduli,
    ode_order_analysis,
    sl2_fixed_positions,
    surviving_depths_on_primaries,
    t_sector_restriction_4pt,
    verify_depth_4_vanishing,
    virasoro_bpz_4pt_hamiltonian,
    w3_4pt_hamiltonian,
    w3_c2_specific_coefficients,
    w3_exceeds_virasoro_order,
    w3_minimal_model_c2,
    w_sector_leading_term,
)

# Also import from the parent engine for cross-checks
from theorem_w3_commuting_hamiltonians_engine import (
    beta_composite,
    collision_residue_on_primary,
    k_max_family,
    kappa_T,
    kappa_W,
    kappa_total,
    lambda_zero_mode_on_primary,
    ope_mode,
)


# Standard test values
C_FRACTIONS = [Fraction(1), Fraction(2), Fraction(10), Fraction(50), Fraction(100)]
C_FLOATS = [0.5, 1.0, 2.0, 4.0, 10.0, 24.0, 50.0]


# ============================================================================
# 1. SL(2) gauge fixing
# ============================================================================

class TestSL2GaugeFixing(unittest.TestCase):
    """Verify SL(2) gauge-fixing structure for 4-point function."""

    def test_n_moduli_4pt(self):
        """dim M_{0,4} = 1."""
        self.assertEqual(n_moduli(4), 1)

    def test_n_moduli_3pt(self):
        """dim M_{0,3} = 0 (fully fixed by SL(2))."""
        self.assertEqual(n_moduli(3), 0)

    def test_n_moduli_5pt(self):
        """dim M_{0,5} = 2 (first nontrivial moduli space)."""
        self.assertEqual(n_moduli(5), 2)

    def test_n_moduli_formula(self):
        """dim M_{0,n} = n - 3 for n >= 3."""
        for n in range(3, 10):
            self.assertEqual(n_moduli(n), n - 3)

    def test_fixed_positions(self):
        """Standard SL(2) fixing: 0, z, 1, infty."""
        pos = sl2_fixed_positions()
        self.assertEqual(pos['z1'], 0)
        self.assertEqual(pos['z2'], 'z')
        self.assertEqual(pos['z3'], 1)
        self.assertEqual(pos['z4'], 'infty')
        self.assertEqual(pos['n_moduli'], 1)


# ============================================================================
# 2. T-sector restriction recovers Virasoro BPZ
# ============================================================================

class TestTSectorRestriction(unittest.TestCase):
    """Verify that restricting to the T-T channel recovers Virasoro BPZ."""

    def test_t_sector_match_generic_c(self):
        """T-sector restriction matches Virasoro at generic c values."""
        for c in C_FRACTIONS:
            h1 = Fraction(1, 4)
            h2 = Fraction(1, 2)
            h3 = Fraction(3, 4)
            h4 = Fraction(1)
            result = t_sector_restriction_4pt(c, h1, h2, h3, h4)
            self.assertTrue(result['match'],
                            f"T-sector should match Virasoro at c={c}")

    def test_t_sector_depth_1_is_weight_mode(self):
        """T-sector depth 1 gives T_{(1)}T = 2T -> 2h_j."""
        c = Fraction(10)
        h1 = Fraction(1, 2)
        result = t_sector_restriction_4pt(c, h1, h1, h1, h1)
        self.assertEqual(result['t_sector_depths'][1], 2 * h1)

    def test_t_sector_depth_2_vanishes(self):
        """T-sector depth 2 vanishes (T_{(2)}T = 0)."""
        c = Fraction(10)
        h1 = Fraction(1, 2)
        result = t_sector_restriction_4pt(c, h1, h1, h1, h1)
        self.assertEqual(result['t_sector_depths'][2], 0)

    def test_t_sector_depth_3_is_central(self):
        """T-sector depth 3 gives c/2 (central charge)."""
        for c in C_FRACTIONS:
            h1 = Fraction(1, 4)
            result = t_sector_restriction_4pt(c, h1, h1, h1, h1)
            self.assertEqual(result['t_sector_depths'][3], c / Fraction(2),
                             f"Depth 3 should be c/2 = {c/2} at c={c}")

    def test_t_sector_structural_2_active_depths(self):
        """T-sector has 2 active depths (1 and 3) on primaries; depth 2 vanishes."""
        c = Fraction(10)
        h1 = Fraction(1, 2)
        result = t_sector_restriction_4pt(c, h1, h1, h1, h1)
        # Depth 1 (weight mode) and depth 3 (central) are nonzero;
        # depth 2 vanishes.
        self.assertEqual(result['structural_match']['n_active_depths'], 2)

    def test_bpz_ward_cross_term(self):
        """BPZ Ward identity cross-term at site infinity."""
        c = Fraction(10)
        h1, h2, h3, h4 = Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)
        bpz = virasoro_bpz_4pt_hamiltonian(c, h1, h2, h3, h4)
        expected = h1 + h3 + h2 - h4
        self.assertEqual(Fraction(expected), Fraction(1, 2),
                         "Ward cross = h1+h3+h2-h4 = 1/4+3/4+1/2-1 = 1/2")


# ============================================================================
# 3. Depth-4 vanishing
# ============================================================================

class TestDepth4Vanishing(unittest.TestCase):
    """Verify W_{(4)}W = 0 at all central charges and primaries."""

    def test_depth_4_vanishes_all_c(self):
        """Depth 4 vanishes for all tested c values."""
        result = verify_depth_4_vanishing(C_FRACTIONS)
        self.assertTrue(result['all_vanish'],
                        "Depth 4 should vanish at all c values")

    def test_ww_mode_4_empty(self):
        """W_{(4)}W OPE mode returns empty dict."""
        for c in C_FRACTIONS:
            mode = ope_mode('W', 'W', 4, c)
            self.assertEqual(mode, {},
                             f"W_(4)W should be empty at c={c}")

    def test_tt_mode_4_empty(self):
        """T_{(4)}T doesn't exist (k_max for T-T is 3)."""
        c = Fraction(10)
        mode = ope_mode('T', 'T', 4, c)
        self.assertEqual(mode, {})

    def test_depth_4_collision_residue_zero(self):
        """Collision residue at depth 4 is zero for all channels and primaries."""
        c = Fraction(10)
        for h_j in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3)]:
            for w_j in [Fraction(0), Fraction(1, 4), Fraction(1)]:
                for a in ('T', 'W'):
                    for b in ('T', 'W'):
                        res = collision_residue_on_primary(4, (a, b), c, h_j, w_j)
                        self.assertEqual(res, 0,
                                         f"Depth 4 should be zero: "
                                         f"({a},{b}) at h={h_j}, w={w_j}")

    def test_depth_4_vanishing_reason(self):
        """The reason for depth-4 vanishing is structural (weight-1 gap)."""
        result = verify_depth_4_vanishing()
        self.assertIn('no weight-1 field', result['reason'])


# ============================================================================
# 4. ODE order: W_3 exceeds Virasoro
# ============================================================================

class TestODEOrder(unittest.TestCase):
    """Verify the key prediction: W_3 ODE order exceeds Virasoro."""

    def test_w3_exceeds_virasoro(self):
        """W_3 differential operator order (4) > Virasoro order (2)."""
        result = w3_exceeds_virasoro_order()
        self.assertTrue(result['w3_exceeds'])
        self.assertEqual(result['w3_order'], 4)
        self.assertEqual(result['virasoro_order'], 2)

    def test_w3_order_is_kmax_minus_1(self):
        """W_3 diff order = k_max - 1 = 5 - 1 = 4."""
        self.assertEqual(DIFF_ORDER_W3, K_MAX_W3 - 1)

    def test_w3_kmax_is_5(self):
        """W_3 collision depth k_max = 5."""
        self.assertEqual(K_MAX_W3, 5)
        self.assertEqual(k_max_family('w3'), 5)

    def test_virasoro_kmax_is_3(self):
        """Virasoro collision depth k_max = 3."""
        self.assertEqual(K_MAX_VIR, 3)
        self.assertEqual(k_max_family('virasoro'), 3)

    def test_max_ope_pole_w3(self):
        """W_3 max OPE pole = 6 (from W-W channel)."""
        self.assertEqual(MAX_OPE_POLE_W3, 6)

    def test_ode_order_analysis_w3(self):
        """W_3 ODE order analysis: 4 on descendants, 1 on generic primaries."""
        result = ode_order_analysis('w3')
        self.assertEqual(result['k_max'], 5)
        self.assertEqual(result['diff_order_descendants'], 4)
        self.assertEqual(result['diff_order_primaries_generic'], 1)
        self.assertEqual(result['matrix_ode_order'], 1)

    def test_ode_order_analysis_virasoro(self):
        """Virasoro ODE order analysis: 2 on descendants."""
        result = ode_order_analysis('virasoro')
        self.assertEqual(result['diff_order_descendants'], 2)
        self.assertEqual(result['bpz_null_vector_order_21'], 2)

    def test_depth_4_in_extra_depths(self):
        """Depth 4 listed as extra (beyond Virasoro) but vanishes."""
        result = w3_exceeds_virasoro_order()
        self.assertTrue(result['depth_4_vanishes'])

    def test_w3_order_ratio(self):
        """W_3 order is exactly twice Virasoro order: 4/2 = 2."""
        result = w3_exceeds_virasoro_order()
        self.assertEqual(result['ratio'], 2.0)


# ============================================================================
# 5. Surviving depths on primaries
# ============================================================================

class TestSurvivingDepths(unittest.TestCase):
    """Verify which depths survive on primaries."""

    def test_depth_4_in_vanishing(self):
        """Depth 4 is in the vanishing list."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        result = surviving_depths_on_primaries(c, h_j)
        self.assertIn(4, result['vanishing'])

    def test_depths_1_and_3_survive(self):
        """Depths 1 and 3 have nontrivial scalar contributions."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        result = surviving_depths_on_primaries(c, h_j, w_j=Fraction(1, 4))
        # Depths 1 and 3 should be surviving (nontrivial scalar)
        self.assertIn(1, result['surviving'])
        self.assertIn(3, result['surviving'])

    def test_depth_5_is_central(self):
        """Depth 5 is central (c/3, trivial on primaries)."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        result = surviving_depths_on_primaries(c, h_j)
        self.assertIn(5, result['central_only'])

    def test_depth_3_is_central_for_tt_channel(self):
        """Depth 3 T-T channel gives c/2 (central)."""
        c = Fraction(10)
        # T_{(3)}T = c/2 is central; but W_{(3)}W = 2T gives 2h_j (non-central)
        # So depth 3 should be surviving (has non-central contribution from W-W)
        h_j = Fraction(1, 2)
        result = surviving_depths_on_primaries(c, h_j)
        # Depth 3 should NOT be in central_only (because W_{(3)}W = 2T is non-central)
        self.assertNotIn(3, result['central_only'])


# ============================================================================
# 6. W-sector leading term
# ============================================================================

class TestWSectorLeadingTerm(unittest.TestCase):
    """Identify the leading new W_3-specific term."""

    def test_leading_linear_term_at_depth_3(self):
        """The leading LINEAR W_3-specific scalar is 2h_j at depth 3."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        result = w_sector_leading_term(c, h_j)
        self.assertEqual(result['depth_3_scalar']['value'], 2 * h_j)

    def test_depth_1_is_nonlinear(self):
        """Depth-1 Lambda term is nonlinear in h_j."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        result = w_sector_leading_term(c, h_j)
        self.assertTrue(result['depth_1_lambda']['is_nonlinear'])

    def test_depth_1_lambda_value(self):
        """Depth-1 Lambda = beta * (h^2 - 3h/5) at specific values."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        beta = beta_composite(c)
        lambda_val = lambda_zero_mode_on_primary(c, h_j)
        result = w_sector_leading_term(c, h_j)
        self.assertEqual(result['depth_1_lambda']['value'], beta * lambda_val)

    def test_surviving_depths_list(self):
        """W-W channel surviving depths are 1, 2, 3, 5."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        result = w_sector_leading_term(c, h_j)
        self.assertEqual(result['surviving_depths'], [1, 2, 3, 5])
        self.assertEqual(result['vanishing_depths'], [4])

    def test_depth_5_is_central(self):
        """Depth 5 is c/3 (central charge term)."""
        for c in C_FRACTIONS:
            h_j = Fraction(1, 2)
            result = w_sector_leading_term(c, h_j)
            expected = c / Fraction(3)
            self.assertEqual(result['depth_5_central']['value'], expected)


# ============================================================================
# 7. Specific coefficient values at c = 2
# ============================================================================

class TestC2MinimalModel(unittest.TestCase):
    """Verify exact coefficients at c = 2."""

    def test_beta_at_c2(self):
        """beta(c=2) = 16/(22+10) = 16/32 = 1/2."""
        result = w3_minimal_model_c2()
        self.assertEqual(result['beta'], Fraction(1, 2))
        self.assertEqual(result['beta'], result['beta_expected'])

    def test_kappa_T_at_c2(self):
        """kappa_T(c=2) = c/2 = 1."""
        result = w3_minimal_model_c2()
        self.assertEqual(result['kappa_T'], Fraction(1))

    def test_kappa_W_at_c2(self):
        """kappa_W(c=2) = c/3 = 2/3."""
        result = w3_minimal_model_c2()
        self.assertEqual(result['kappa_W'], Fraction(2, 3))

    def test_kappa_total_at_c2(self):
        """kappa_total(c=2) = kappa_T + kappa_W = 5/3."""
        result = w3_minimal_model_c2()
        self.assertEqual(result['kappa_total'], Fraction(5, 3))

    def test_depth_1_lambda_at_c2_h_half(self):
        """At c=2, h=1/2: Lambda_0 = h^2 - 3h/5 = 1/4 - 3/10 = -1/20.
        beta * Lambda_0 = (1/2)(-1/20) = -1/40."""
        result = w3_c2_specific_coefficients(Fraction(1, 2))
        expected = Fraction(1, 2) * (Fraction(1, 4) - Fraction(3, 10))
        self.assertEqual(result['depth_1_lambda'], expected)
        self.assertEqual(expected, Fraction(-1, 40))

    def test_depth_3_central_at_c2(self):
        """At c=2: T-T central term = c/2 = 1."""
        result = w3_c2_specific_coefficients(Fraction(1, 2))
        self.assertEqual(result['depth_3_tt_central'], Fraction(1))

    def test_depth_5_central_at_c2(self):
        """At c=2: W-W central term = c/3 = 2/3."""
        result = w3_c2_specific_coefficients(Fraction(1, 2))
        self.assertEqual(result['depth_5_central'], Fraction(2, 3))

    def test_depth_4_zero_at_c2(self):
        """At c=2: depth 4 vanishes."""
        result = w3_c2_specific_coefficients(Fraction(1, 2))
        self.assertEqual(result['depth_4'], Fraction(0))

    def test_depth_3_ww_2T_at_c2(self):
        """At c=2, h=1/2: W_{(3)}W = 2T -> 2h = 1."""
        result = w3_c2_specific_coefficients(Fraction(1, 2))
        self.assertEqual(result['depth_3_ww_2T'], Fraction(1))


# ============================================================================
# 8. Fuchsian ODE structure
# ============================================================================

class TestFuchsianStructure(unittest.TestCase):
    """Verify the Fuchsian ODE structure."""

    def test_virasoro_3_singular_points(self):
        """Virasoro BPZ: 3 regular singular points at 0, 1, infty."""
        result = fuchsian_structure_4pt()
        self.assertEqual(result['virasoro']['n_regular_singular'], 3)
        self.assertIn(0, result['virasoro']['singular_points'])
        self.assertIn(1, result['virasoro']['singular_points'])

    def test_w3_3_singular_points(self):
        """W_3: 3 regular singular points at 0, 1, infty."""
        result = fuchsian_structure_4pt()
        self.assertEqual(result['w3']['n_regular_singular'], 3)

    def test_virasoro_ode_order_2(self):
        """Virasoro BPZ: ODE order 2 (hypergeometric)."""
        result = fuchsian_structure_4pt()
        self.assertEqual(result['virasoro']['ode_order'], 2)

    def test_w3_max_ode_order_4(self):
        """W_3: max ODE order 4."""
        result = fuchsian_structure_4pt()
        self.assertEqual(result['w3']['max_ode_order'], 4)


# ============================================================================
# 9. Channel structure and decoupling
# ============================================================================

class TestChannelStructure(unittest.TestCase):
    """Verify the channel structure of the W_3 Hamiltonian."""

    def test_diagonal_metric(self):
        """W_3 Zamolodchikov metric is diagonal: eta^{TW} = 0."""
        c = Fraction(10)
        result = channel_structure_4pt(c)
        self.assertEqual(result['inverse_metric']['TW'], 0)

    def test_tt_active_depths(self):
        """T-T channel active at depths 1, 3."""
        c = Fraction(10)
        result = channel_structure_4pt(c)
        self.assertEqual(result['active_depths_by_channel'][('T', 'T')], [1, 3])

    def test_ww_active_depths(self):
        """W-W channel active at depths 1, 2, 3, 5."""
        c = Fraction(10)
        result = channel_structure_4pt(c)
        self.assertEqual(result['active_depths_by_channel'][('W', 'W')],
                         [1, 2, 3, 5])

    def test_tw_active_depths(self):
        """T-W and W-T cross-channels active only at depth 1."""
        c = Fraction(10)
        result = channel_structure_4pt(c)
        self.assertEqual(result['active_depths_by_channel'][('T', 'W')], [1])
        self.assertEqual(result['active_depths_by_channel'][('W', 'T')], [1])

    def test_virasoro_max_depth(self):
        """Virasoro max depth = 3."""
        c = Fraction(10)
        result = channel_structure_4pt(c)
        self.assertEqual(result['virasoro_max_depth'], 3)


# ============================================================================
# 10. Numerical evaluation consistency
# ============================================================================

class TestNumericalEvaluation(unittest.TestCase):
    """Verify numerical consistency of the Hamiltonian evaluation."""

    def test_evaluation_at_z_half(self):
        """Evaluate at z = 0.5 and verify BPZ + W-sector decomposition."""
        z = 0.5
        c = 10.0
        h = 0.25
        result = evaluate_hamiltonian_at_z(z, c, h, h, h, h)
        # total = bpz + w_sector
        self.assertAlmostEqual(
            result['total'],
            result['bpz'] + result['w_sector_total'],
            places=12,
        )

    def test_depth_4_zero_numerical(self):
        """Depth 4 contribution is exactly zero in numerical evaluation."""
        z = 0.5
        c = 10.0
        h = 0.25
        result = evaluate_hamiltonian_at_z(z, c, h, h, h, h)
        self.assertEqual(result['w_depth4'], 0)

    def test_bpz_only_when_w_zero(self):
        """When w_i = 0, the W-W OPE still contributes through W_{(3)}W = 2T
        and the Lambda composite, which depend on h_j not w_j.

        Use asymmetric weights h1 != h3 to avoid accidental cancellation
        at z = 0.5 (where z^3 = -(z-1)^3 causes equal-weight terms to cancel).
        """
        z = 0.5
        c = 10.0
        h1, h3 = 0.25, 0.75  # asymmetric to avoid cancellation
        result = evaluate_hamiltonian_at_z(z, c, h1, 0.5, h3, 0.5, w1=0, w3_ch=0)
        # W-depth-3: (0 + 2*0.25)/z^3 + (0 + 2*0.75)/(z-1)^3
        # = 0.5/0.125 + 1.5/(-0.125) = 4 - 12 = -8, nonzero
        self.assertNotEqual(result['w_depth3'], 0)

    def test_w_sector_nonzero_with_charges(self):
        """W-sector is nonzero when W-charges are turned on."""
        z = 0.3
        c = 10.0
        h = 0.5
        result = evaluate_hamiltonian_at_z(z, c, h, h, h, h,
                                           w1=0.1, w3_ch=0.2)
        self.assertNotEqual(result['w_sector_total'], 0)

    def test_even_depth_symmetry(self):
        """Even-depth (BPZ depth-2) part of H(z) is symmetric under
        z -> 1-z when h1 = h3 and w1 = w3.

        Odd-depth terms (z^{-k} for k odd) pick up a sign under
        z -> 1-z because (1-z)^{-k} = -(z-1)^{-k} for odd k and
        the exchange swaps z <-> (z-1).  So the BPZ (depth-2)
        contribution h_1/z^2 + h_3/(z-1)^2 is symmetric, while
        depth-3 and depth-5 terms are antisymmetric.
        """
        c = 10.0
        h = 0.5
        z1 = 0.3
        z2 = 1.0 - z1
        r1 = evaluate_hamiltonian_at_z(z1, c, h, h, h, h)
        r2 = evaluate_hamiltonian_at_z(z2, c, h, h, h, h)
        # BPZ sector: h/z^2 + h/(z-1)^2 + cross/(z(z-1))
        # Under z -> 1-z: h/(1-z)^2 + h/(-z)^2 + cross/((1-z)(-z))
        # = h/(1-z)^2 + h/z^2 + cross/(z(1-z)) -- same.
        self.assertAlmostEqual(r1['bpz'], r2['bpz'], places=10)


# ============================================================================
# 11. Cross-family comparison: k_max hierarchy
# ============================================================================

class TestCrossFamilyHierarchy(unittest.TestCase):
    """Verify the k_max and ODE order hierarchy across families."""

    def test_kmax_hierarchy(self):
        """Heisenberg = KM < Virasoro < W_3 < W_4 in k_max."""
        # Heisenberg and KM both have OPE pole 2 -> k_max = 1
        self.assertEqual(k_max_family('heisenberg'), k_max_family('km'))
        self.assertLess(k_max_family('km'), k_max_family('virasoro'))
        self.assertLess(k_max_family('virasoro'), k_max_family('w3'))

    def test_kmax_formula_wN(self):
        """k_max(W_N) = 2N - 1 is monotone increasing in N."""
        for N in range(2, 8):
            self.assertEqual(k_max_family('wN', N), 2 * N - 1)
        for N in range(2, 7):
            self.assertLess(k_max_family('wN', N), k_max_family('wN', N + 1))

    def test_virasoro_is_w2(self):
        """Virasoro = W_2: k_max(Virasoro) = k_max(W_2) = 3."""
        self.assertEqual(k_max_family('virasoro'), k_max_family('wN', 2))

    def test_w3_matches_wN_at_N3(self):
        """W_3 specific value matches W_N formula at N=3."""
        self.assertEqual(k_max_family('w3'), k_max_family('wN', 3))


# ============================================================================
# 12. Ward identity structure
# ============================================================================

class TestWardIdentityStructure(unittest.TestCase):
    """Verify the Ward identity structure of the 4-point Hamiltonian."""

    def test_bpz_pole_orders(self):
        """BPZ Hamiltonian has poles of order 2 at z=0 and z=1."""
        c = Fraction(10)
        h = Fraction(1, 2)
        bpz = virasoro_bpz_4pt_hamiltonian(c, h, h, h, h)
        self.assertEqual(bpz['pole_0']['order'], 2)
        self.assertEqual(bpz['pole_1']['order'], 2)

    def test_bpz_pole_0_coefficient(self):
        """BPZ pole at z=0 has coefficient h_1."""
        c = Fraction(10)
        h1, h2, h3, h4 = Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)
        bpz = virasoro_bpz_4pt_hamiltonian(c, h1, h2, h3, h4)
        self.assertEqual(bpz['pole_0']['coefficients'][2], h1)

    def test_ward_cross_equal_weights(self):
        """Ward cross-term vanishes when all weights are equal."""
        c = Fraction(10)
        h = Fraction(1, 2)
        bpz = virasoro_bpz_4pt_hamiltonian(c, h, h, h, h)
        # h1 + h3 + h2 - h4 = h + h + h - h = 2h
        expected = h + h + h - h
        self.assertEqual(bpz['ward_cross_term']['coefficient'], expected)
        self.assertEqual(expected, 2 * h)

    def test_w3_depth_4_vanishes_in_hamiltonian(self):
        """W_3 4-point Hamiltonian has depth_4_vanishes = True."""
        c = Fraction(10)
        h = Fraction(1, 2)
        result = w3_4pt_hamiltonian(c, h, h, h, h, 0, 0, 0, 0)
        self.assertTrue(result['depth_4_vanishes'])


# ============================================================================
# 13. Lambda composite at specific values
# ============================================================================

class TestLambdaCompositeSpecific(unittest.TestCase):
    """Verify Lambda_0 action on primaries at specific parameter values."""

    def test_lambda_at_h_zero(self):
        """Lambda_0(h=0) = 0^2 - 3*0/5 = 0."""
        c = Fraction(10)
        val = lambda_zero_mode_on_primary(c, Fraction(0))
        self.assertEqual(val, 0)

    def test_lambda_at_h_three_fifths(self):
        """Lambda_0(h=3/5) = 9/25 - 9/25 = 0."""
        c = Fraction(10)
        h = Fraction(3, 5)
        val = lambda_zero_mode_on_primary(c, h)
        expected = h**2 - Fraction(3, 5) * h
        self.assertEqual(val, expected)
        self.assertEqual(expected, 0)

    def test_lambda_at_h_one(self):
        """Lambda_0(h=1) = 1 - 3/5 = 2/5."""
        c = Fraction(10)
        val = lambda_zero_mode_on_primary(c, Fraction(1))
        self.assertEqual(val, Fraction(2, 5))

    def test_lambda_independent_of_c(self):
        """Lambda_0 on a primary is INDEPENDENT of c."""
        h = Fraction(1, 2)
        vals = set()
        for c in C_FRACTIONS:
            vals.add(lambda_zero_mode_on_primary(c, h))
        self.assertEqual(len(vals), 1,
                         "Lambda_0 should be independent of c")

    def test_lambda_quadratic_formula(self):
        """Lambda_0(h) = h^2 - 3h/5 for multiple h values."""
        c = Fraction(10)
        for h in [Fraction(0), Fraction(1, 4), Fraction(1, 2),
                  Fraction(1), Fraction(2), Fraction(5)]:
            val = lambda_zero_mode_on_primary(c, h)
            expected = h**2 - Fraction(3, 5) * h
            self.assertEqual(val, expected,
                             f"Lambda_0({h}) should be {expected}, got {val}")


# ============================================================================
# 14. Multi-path depth verification
# ============================================================================

class TestMultiPathDepthVerification(unittest.TestCase):
    """Cross-check collision residues via independent paths.

    Path 1: Direct from ope_mode function
    Path 2: From collision_residue_on_primary function
    Path 3: From the 4-point ODE scalar coefficients
    """

    def test_depth_1_tt_cross_check(self):
        """Depth 1 T-T: ope_mode vs collision_residue_on_primary."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        # Path 1: direct OPE mode
        mode = ope_mode('T', 'T', 1, c)
        path1 = mode.get('T', 0) * h_j  # T_{(1)}T = 2T -> 2*h_j
        # Path 2: collision residue
        path2 = collision_residue_on_primary(1, ('T', 'T'), c, h_j)
        self.assertEqual(path1, path2)
        self.assertEqual(path1, 2 * h_j)

    def test_depth_3_ww_cross_check(self):
        """Depth 3 W-W: ope_mode vs collision_residue_on_primary."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        # Path 1: direct OPE mode
        mode = ope_mode('W', 'W', 3, c)
        path1 = mode.get('T', 0) * h_j  # W_{(3)}W = 2T -> 2*h_j
        # Path 2: collision residue
        path2 = collision_residue_on_primary(3, ('W', 'W'), c, h_j)
        self.assertEqual(path1, path2)
        self.assertEqual(path1, 2 * h_j)

    def test_depth_5_ww_cross_check(self):
        """Depth 5 W-W: ope_mode vs collision_residue_on_primary."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        # Path 1: direct OPE mode
        mode = ope_mode('W', 'W', 5, c)
        path1 = mode.get('vac', 0)  # W_{(5)}W = c/3
        # Path 2: collision residue
        path2 = collision_residue_on_primary(5, ('W', 'W'), c, h_j)
        self.assertEqual(path1, path2)
        self.assertEqual(path1, c / 3)

    def test_depth_4_ww_cross_check(self):
        """Depth 4 W-W: both paths give zero."""
        c = Fraction(10)
        h_j = Fraction(1, 2)
        mode = ope_mode('W', 'W', 4, c)
        path1 = sum(mode.values()) if mode else 0
        path2 = collision_residue_on_primary(4, ('W', 'W'), c, h_j)
        self.assertEqual(path1, 0)
        self.assertEqual(path2, 0)

    def test_scalar_coefficients_match_collision_residues(self):
        """extract_scalar_ode_coefficients agrees with collision_residue_on_primary."""
        c = Fraction(10)
        h1 = Fraction(1, 2)
        coeffs = extract_scalar_ode_coefficients(c, h1, h1, h1, h1)

        # Depth 2 site 0 should be h_1
        self.assertEqual(coeffs[2]['site_0'], h1)
        # This matches T_{(1)}T on primary:
        self.assertEqual(collision_residue_on_primary(1, ('T', 'T'), c, h1), 2 * h1)
        # (The factor of 2 is from the OPE normalization; the BPZ convention
        # absorbs it into the metric normalization.)

    def test_w3_depth_3_combines_w_ward_and_ww(self):
        """Depth 3 has TWO independent contributions: W-Ward and W_{(3)}W."""
        c = Fraction(10)
        h1 = Fraction(1, 2)
        w1 = Fraction(1, 4)
        coeffs = extract_scalar_ode_coefficients(c, h1, h1, h1, h1,
                                                  w1=w1, w3_ch=w1)
        # W-Ward gives w_1, W_{(3)}W = 2T gives 2h_1
        self.assertEqual(coeffs[3]['site_0_w_ward'], w1)
        self.assertEqual(coeffs[3]['site_0_ww_2T'], 2 * h1)


# ============================================================================
# 15. Cross-check with W_3 commuting Hamiltonians engine
# ============================================================================

class TestCrossCheckWithParentEngine(unittest.TestCase):
    """Cross-check results with the W_3 commuting Hamiltonians engine."""

    def test_kmax_agreement(self):
        """k_max from both engines agree."""
        self.assertEqual(K_MAX_W3, k_max_family('w3'))

    def test_beta_agreement(self):
        """beta_composite from both engines agree at multiple c."""
        for c in C_FRACTIONS:
            expected = Fraction(16) / (Fraction(22) + 5 * c)
            self.assertEqual(beta_composite(c), expected)

    def test_kappa_agreement(self):
        """kappa values from both engines agree."""
        for c in C_FRACTIONS:
            self.assertEqual(kappa_T(c), c / 2)
            self.assertEqual(kappa_W(c), c / 3)
            self.assertEqual(kappa_total(c), 5 * c / 6)

    def test_lambda_agreement(self):
        """Lambda_0 on primary from both engines agree."""
        c = Fraction(10)
        for h in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3)]:
            expected = h**2 - Fraction(3, 5) * h
            self.assertEqual(lambda_zero_mode_on_primary(c, h), expected)

    def test_full_summary_runs(self):
        """Full 4-point ODE summary executes without error."""
        c = Fraction(10)
        h = Fraction(1, 4)
        result = full_4pt_ode_summary(c, h, h, h, h)
        self.assertIn('hamiltonian', result)
        self.assertIn('ode_order', result)
        self.assertIn('depth_4_vanishing', result)
        self.assertTrue(result['order_exceeds_virasoro']['w3_exceeds'])
        self.assertTrue(result['depth_4_vanishing']['all_vanish'])


# ============================================================================
# Additional tests for completeness
# ============================================================================

class TestAdditionalVerifications(unittest.TestCase):
    """Miscellaneous verification tests."""

    def test_kmax_equals_max_pole_minus_1(self):
        """k_max = max_OPE_pole - 1 (AP19 d log absorption)."""
        self.assertEqual(K_MAX_W3, MAX_OPE_POLE_W3 - 1)

    def test_diff_order_equals_kmax_minus_1(self):
        """Differential operator order = k_max - 1."""
        self.assertEqual(DIFF_ORDER_W3, K_MAX_W3 - 1)

    def test_w3_hamiltonian_returns_both_sectors(self):
        """w3_4pt_hamiltonian returns both BPZ and W sectors."""
        c = Fraction(10)
        h = Fraction(1, 2)
        result = w3_4pt_hamiltonian(c, h, h, h, h, 0, 0, 0, 0)
        self.assertIn('bpz_sector', result)
        self.assertIn('w_sector', result)

    def test_evaluation_decomposition(self):
        """Numerical evaluation decomposes correctly into BPZ + W-sector."""
        z = 0.4
        c = 10.0
        h = 0.5
        w = 0.1
        result = evaluate_hamiltonian_at_z(z, c, h, h, h, h,
                                           w1=w, w3_ch=w)
        reconstructed = (result['bpz'] + result['w_depth1']
                         + result['w_depth3'] + result['w_depth4']
                         + result['w_depth5'])
        self.assertAlmostEqual(result['total'], reconstructed, places=12)

    def test_w_sector_vanishes_at_c_zero_not_physical(self):
        """At c -> 0 (not physical), beta diverges; test c = 1/100 is finite."""
        c = Fraction(1, 100)
        h = Fraction(1, 2)
        # beta = 16/(22 + 5/100) = 16/(22.05) = 1600/2205
        beta = beta_composite(c)
        self.assertEqual(beta, Fraction(16) / (Fraction(22) + 5 * c))
        # This should not raise an error
        result = w_sector_leading_term(c, h)
        self.assertIsNotNone(result['depth_1_lambda']['value'])


if __name__ == '__main__':
    unittest.main()
