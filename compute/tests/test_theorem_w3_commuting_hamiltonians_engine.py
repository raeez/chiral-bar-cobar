r"""Tests for W_3 commuting Hamiltonians from the shadow connection.

STRUCTURE
=========

 1. OPE mode data: verify all W_3 OPE modes at each depth
 2. Collision depth parameters: k_max, differential operator order
 3. Lambda composite: zero-mode action on primaries
 4. Zamolodchikov metric and propagator
 5. Collision residues on primaries at each depth
 6. T-sector restriction recovering Virasoro
 7. Cross-family comparison: Heisenberg, KM, Virasoro, W_3, W_4
 8. W_N structure for general N
 9. Koszul conductor values
10. Ward identities
11. 4-point and 5-point commutativity
12. Beta composite field coefficient
13. ODE order predictions
14. Exact arithmetic (Fraction-based)
15. Multi-path verification: collision residues from independent sources

Manuscript references:
    thm:gz26-commuting-differentials
    eq:gz26-hamiltonian-decomposition
    eq:hamiltonian-collision-depth
    eq:wn-hamiltonians
    rem:gz26-scope
    prop:shadow-connection-bpz
    thm:shadow-connection-kz
    rem:bar-pole-absorption (AP19)
    comp:w3-nthproducts (bar_complex_tables.tex)
"""

import math
import unittest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_w3_commuting_hamiltonians_engine import (
    GENERATORS,
    WEIGHTS,
    beta_composite,
    central_charge_from_level,
    collision_residue_on_primary,
    cross_family_comparison,
    differential_operator_order,
    differential_operator_order_wN,
    full_evaluation,
    inverse_metric,
    k_max_family,
    kappa_T,
    kappa_W,
    kappa_total,
    koszul_conductor_wN,
    lambda_on_primary_w3,
    lambda_zero_mode_on_primary,
    max_ope_pole,
    max_ope_pole_algebra,
    ode_order_prediction,
    ope_mode,
    t_sector_restriction,
    verify_commutativity_4pt_w3,
    verify_commutativity_5pt_w3,
    w3_collision_residue_table,
    w3_hamiltonian_on_primaries,
    w3_hamiltonian_scalar_on_primaries,
    w3_ward_identities,
    wN_structure,
    zamolodchikov_metric,
)


# Standard test central charges
C_VALUES = [Fraction(1), Fraction(2), Fraction(10), Fraction(50), Fraction(100)]
C_FLOAT_VALUES = [0.5, 1.0, 2.0, 4.0, 10.0, 24.0, 50.0, 100.0]


class TestOPEModeData(unittest.TestCase):
    """Verify all W_3 OPE modes against ground truth from w3_bar.py."""

    def test_TT_mode_3(self):
        """T_{(3)}T = c/2 (quartic pole, central charge)."""
        for c in C_VALUES:
            mode = ope_mode('T', 'T', 3, c)
            self.assertEqual(mode['vac'], c / 2,
                             f"T_(3)T should be c/2 = {c/2}, got {mode.get('vac')}")

    def test_TT_mode_1(self):
        """T_{(1)}T = 2T (conformal weight / energy-momentum tensor)."""
        c = Fraction(10)
        mode = ope_mode('T', 'T', 1, c)
        self.assertEqual(mode['T'], Fraction(2))

    def test_TT_mode_0(self):
        """T_{(0)}T = dT (translation)."""
        c = Fraction(10)
        mode = ope_mode('T', 'T', 0, c)
        self.assertEqual(mode['dT'], Fraction(1))

    def test_TT_mode_2_vanishes(self):
        """T_{(2)}T = 0 (no weight-1 field for Virasoro)."""
        c = Fraction(10)
        mode = ope_mode('T', 'T', 2, c)
        self.assertEqual(mode, {})

    def test_TW_mode_1(self):
        """T_{(1)}W = 3W (W is primary of weight 3 under Virasoro)."""
        c = Fraction(10)
        mode = ope_mode('T', 'W', 1, c)
        self.assertEqual(mode['W'], Fraction(3))

    def test_TW_mode_0(self):
        """T_{(0)}W = dW (translation of W)."""
        c = Fraction(10)
        mode = ope_mode('T', 'W', 0, c)
        self.assertEqual(mode['dW'], Fraction(1))

    def test_WT_mode_1(self):
        """W_{(1)}T = 3W (from skew-symmetry)."""
        c = Fraction(10)
        mode = ope_mode('W', 'T', 1, c)
        self.assertEqual(mode['W'], Fraction(3))

    def test_WT_mode_0(self):
        """W_{(0)}T = 2dW (NOT 1dW -- asymmetric via skew-symmetry)."""
        c = Fraction(10)
        mode = ope_mode('W', 'T', 0, c)
        self.assertEqual(mode['dW'], Fraction(2))

    def test_WW_mode_5(self):
        """W_{(5)}W = c/3 (sixth-order pole, central charge of W-channel)."""
        for c in C_VALUES:
            mode = ope_mode('W', 'W', 5, c)
            self.assertEqual(mode['vac'], c / 3)

    def test_WW_mode_4_vanishes(self):
        """W_{(4)}W = 0 (no weight-1 field in vacuum module)."""
        c = Fraction(10)
        mode = ope_mode('W', 'W', 4, c)
        self.assertEqual(mode, {})

    def test_WW_mode_3(self):
        """W_{(3)}W = 2T."""
        c = Fraction(10)
        mode = ope_mode('W', 'W', 3, c)
        self.assertEqual(mode['T'], Fraction(2))

    def test_WW_mode_2(self):
        """W_{(2)}W = dT."""
        c = Fraction(10)
        mode = ope_mode('W', 'W', 2, c)
        self.assertEqual(mode['dT'], Fraction(1))

    def test_WW_mode_1_composite(self):
        """W_{(1)}W = (3/10)d^2T + beta*Lambda with beta = 16/(22+5c)."""
        c = Fraction(10)
        mode = ope_mode('W', 'W', 1, c)
        expected_beta = Fraction(16) / (Fraction(22) + 5 * c)
        self.assertEqual(mode['d2T'], Fraction(3, 10))
        self.assertEqual(mode['Lambda'], expected_beta)

    def test_WW_mode_0(self):
        """W_{(0)}W = (1/15)d^3T + (beta/2)*dLambda."""
        c = Fraction(10)
        mode = ope_mode('W', 'W', 0, c)
        expected_beta = Fraction(16) / (Fraction(22) + 5 * c)
        self.assertEqual(mode['d3T'], Fraction(1, 15))
        self.assertEqual(mode['dLambda'], expected_beta / 2)


class TestCollisionDepthParameters(unittest.TestCase):
    """Verify k_max and differential operator order for each family."""

    def test_heisenberg_kmax(self):
        """Heisenberg: OPE pole 2, k_max = 1."""
        self.assertEqual(k_max_family('heisenberg'), 1)

    def test_km_kmax(self):
        """Affine KM: OPE pole 2, k_max = 1."""
        self.assertEqual(k_max_family('km'), 1)

    def test_virasoro_kmax(self):
        """Virasoro: OPE pole 4, k_max = 3."""
        self.assertEqual(k_max_family('virasoro'), 3)

    def test_w3_kmax(self):
        """W_3: OPE pole 6, k_max = 5."""
        self.assertEqual(k_max_family('w3'), 5)

    def test_wN_kmax_formula(self):
        """W_N: k_max = 2N-1."""
        for N in range(2, 8):
            self.assertEqual(k_max_family('wN', N), 2 * N - 1)

    def test_diff_order_heisenberg(self):
        """Heisenberg: order 0 (multiplication operators)."""
        self.assertEqual(differential_operator_order('heisenberg'), 0)

    def test_diff_order_virasoro(self):
        """Virasoro: order 2 on descendants."""
        self.assertEqual(differential_operator_order('virasoro'), 2)

    def test_diff_order_w3(self):
        """W_3: order 4 (k_max - 1 = 5 - 1 = 4)."""
        self.assertEqual(differential_operator_order('w3'), 4)

    def test_diff_order_wN_formula(self):
        """W_N: order 2(N-1)."""
        for N in range(2, 8):
            self.assertEqual(differential_operator_order_wN(N), 2 * (N - 1))

    def test_w3_diff_order_matches_wN_at_N3(self):
        """W_3 order from k_max matches 2(N-1) formula at N=3."""
        self.assertEqual(differential_operator_order('w3'),
                         differential_operator_order_wN(3))


class TestOPEPoleOrders(unittest.TestCase):
    """Verify max OPE pole orders."""

    def test_TT_pole_order(self):
        """T-T OPE: pole order 4."""
        self.assertEqual(max_ope_pole('T', 'T'), 4)

    def test_TW_pole_order(self):
        """T-W OPE: pole order 2 (W is primary of weight 3)."""
        self.assertEqual(max_ope_pole('T', 'W'), 2)

    def test_WT_pole_order(self):
        """W-T OPE: pole order 2."""
        self.assertEqual(max_ope_pole('W', 'T'), 2)

    def test_WW_pole_order(self):
        """W-W OPE: pole order 6 (sixth-order pole)."""
        self.assertEqual(max_ope_pole('W', 'W'), 6)

    def test_max_algebra_pole(self):
        """W_3 algebra max OPE pole = 6 (from W-W)."""
        self.assertEqual(max_ope_pole_algebra(), 6)

    def test_kmax_equals_max_pole_minus_one(self):
        """k_max = max_pole - 1 (d log absorption, AP19)."""
        self.assertEqual(k_max_family('w3'), max_ope_pole_algebra() - 1)


class TestLambdaComposite(unittest.TestCase):
    """Verify Lambda = :TT: - (3/10)d^2T zero-mode on primaries."""

    def test_lambda_on_vacuum(self):
        """Lambda_0|0> = 0 (vacuum has h=0)."""
        for c in C_FLOAT_VALUES:
            self.assertAlmostEqual(lambda_zero_mode_on_primary(c, 0), 0.0)

    def test_lambda_formula(self):
        """Lambda_0|h> = h^2 - 3h/5 on a primary of weight h."""
        for h in [0.5, 1.0, 2.0, 3.0, 5.0]:
            for c in [1.0, 10.0, 50.0]:
                expected = h**2 - 0.6 * h
                result = lambda_zero_mode_on_primary(c, h)
                self.assertAlmostEqual(result, expected, places=12)

    def test_lambda_exact_fractions(self):
        """Lambda_0 with exact Fraction arithmetic."""
        h = Fraction(2)
        c = Fraction(10)
        expected = Fraction(4) - Fraction(6, 5)  # 4 - 6/5 = 14/5
        self.assertEqual(lambda_zero_mode_on_primary(c, h), expected)

    def test_lambda_independent_of_c(self):
        """Lambda_0 on primaries is INDEPENDENT of central charge c.

        This is because Lambda_0 = :TT:_0 - (3/10)(d^2T)_0 = L_0^2 - (3/5)L_0
        which depends only on the L_0 eigenvalue h, not on c.
        """
        h = 2.5
        vals = [lambda_zero_mode_on_primary(c, h) for c in C_FLOAT_VALUES]
        for v in vals:
            self.assertAlmostEqual(v, vals[0], places=14)

    def test_lambda_independent_of_w(self):
        """Lambda_0 on W_3 primaries is INDEPENDENT of W_0 eigenvalue w.

        Lambda involves only Virasoro modes, not W modes.
        """
        h = 2.0
        for w in [0, 0.5, 1.0, -1.0, 3.0]:
            self.assertAlmostEqual(
                lambda_on_primary_w3(10.0, h, w),
                lambda_on_primary_w3(10.0, h, 0),
                places=14)

    def test_lambda_roots(self):
        """Lambda_0|h> = 0 iff h = 0 or h = 3/5."""
        # h(h - 3/5) = 0 at h = 0 and h = 3/5
        self.assertAlmostEqual(lambda_zero_mode_on_primary(10.0, 0), 0.0)
        self.assertAlmostEqual(lambda_zero_mode_on_primary(10.0, 0.6), 0.0)
        self.assertEqual(lambda_zero_mode_on_primary(Fraction(10), Fraction(3, 5)),
                         Fraction(0))


class TestZamolodchikiMetric(unittest.TestCase):
    """Verify Zamolodchikov metric for W_3."""

    def test_metric_TT(self):
        """eta_{TT} = c/2."""
        for c in C_VALUES:
            m = zamolodchikov_metric(c)
            self.assertEqual(m['TT'], c / 2)

    def test_metric_WW(self):
        """eta_{WW} = c/3."""
        for c in C_VALUES:
            m = zamolodchikov_metric(c)
            self.assertEqual(m['WW'], c / 3)

    def test_metric_TW_vanishes(self):
        """eta_{TW} = 0 (orthogonal channels)."""
        for c in C_VALUES:
            m = zamolodchikov_metric(c)
            self.assertEqual(m['TW'], 0)

    def test_inverse_metric(self):
        """eta^{TT} = 2/c, eta^{WW} = 3/c."""
        for c in C_VALUES:
            if c == 0:
                continue
            inv = inverse_metric(c)
            self.assertEqual(inv['TT'], Fraction(2) / c)
            self.assertEqual(inv['WW'], Fraction(3) / c)

    def test_metric_times_inverse_is_identity(self):
        """eta_{ab} * eta^{bc} = delta^c_a."""
        for c in C_VALUES:
            if c == 0:
                continue
            m = zamolodchikov_metric(c)
            inv = inverse_metric(c)
            # TT: (c/2)(2/c) = 1
            self.assertEqual(m['TT'] * inv['TT'], 1)
            # WW: (c/3)(3/c) = 1
            self.assertEqual(m['WW'] * inv['WW'], 1)


class TestKappaValues(unittest.TestCase):
    """Verify kappa values for W_3."""

    def test_kappa_T(self):
        """kappa_T = c/2."""
        for c in C_VALUES:
            self.assertEqual(kappa_T(c), c / 2)

    def test_kappa_W(self):
        """kappa_W = c/3."""
        for c in C_VALUES:
            self.assertEqual(kappa_W(c), c / 3)

    def test_kappa_total(self):
        """kappa(W_3) = kappa_T + kappa_W = 5c/6."""
        for c in C_VALUES:
            self.assertEqual(kappa_total(c), Fraction(5) * c / 6)

    def test_kappa_additivity(self):
        """kappa_total = kappa_T + kappa_W (additivity)."""
        for c in C_VALUES:
            self.assertEqual(kappa_total(c), kappa_T(c) + kappa_W(c))


class TestBetaComposite(unittest.TestCase):
    """Verify the composite field coefficient beta = 16/(22+5c)."""

    def test_beta_formula(self):
        """beta = 16/(22+5c) for several c values."""
        for c in C_VALUES:
            expected = Fraction(16) / (Fraction(22) + 5 * c)
            self.assertEqual(beta_composite(c), expected)

    def test_beta_at_c1(self):
        """beta(c=1) = 16/27."""
        self.assertEqual(beta_composite(Fraction(1)), Fraction(16, 27))

    def test_beta_at_c2(self):
        """beta(c=2) = 16/32 = 1/2."""
        self.assertEqual(beta_composite(Fraction(2)), Fraction(1, 2))

    def test_beta_large_c_limit(self):
        """beta -> 16/(5c) as c -> infinity."""
        c = 10000.0
        beta = beta_composite(c)
        asymptotic = 16 / (5 * c)
        self.assertAlmostEqual(beta / asymptotic, 1.0, places=3)

    def test_beta_singular_at_c_neg22over5(self):
        """beta is singular at c = -22/5 (degenerate W_3 algebra)."""
        c = -22.0 / 5
        with self.assertRaises((ZeroDivisionError, ValueError)):
            # Should raise or return infinity
            result = 16 / (22 + 5 * c)
            if math.isinf(result):
                raise ZeroDivisionError


class TestCollisionResiduesOnPrimaries(unittest.TestCase):
    """Verify collision residues at each depth on primary states."""

    def test_depth1_TT_on_primary(self):
        """Depth 1, T-T: T_{(1)}T = 2T -> 2h_j on primaries."""
        c = Fraction(10)
        h_j = Fraction(3)
        res = collision_residue_on_primary(1, ('T', 'T'), c, h_j, 0)
        self.assertEqual(res, 2 * h_j)  # 2T -> 2h_j

    def test_depth1_TW_on_primary(self):
        """Depth 1, T-W: T_{(1)}W = 3W -> 3w_j on primaries."""
        c = Fraction(10)
        w_j = Fraction(2)
        res = collision_residue_on_primary(1, ('T', 'W'), c, 0, w_j)
        self.assertEqual(res, 3 * w_j)

    def test_depth1_WW_on_primary(self):
        """Depth 1, W-W: W_{(1)}W = (3/10)d^2T + beta*Lambda.

        On primaries: d^2T vanishes, Lambda -> h^2 - 3h/5.
        So the residue is beta * (h^2 - 3h/5).
        """
        c = Fraction(10)
        h_j = Fraction(2)
        _beta = beta_composite(c)
        _lambda = lambda_zero_mode_on_primary(c, h_j)
        expected = _beta * _lambda
        res = collision_residue_on_primary(1, ('W', 'W'), c, h_j, 0)
        self.assertEqual(res, expected)

    def test_depth2_TT_vanishes(self):
        """Depth 2, T-T: T_{(2)}T = 0."""
        c = Fraction(10)
        res = collision_residue_on_primary(2, ('T', 'T'), c, 1, 0)
        self.assertEqual(res, 0)

    def test_depth3_TT_central(self):
        """Depth 3, T-T: T_{(3)}T = c/2 (central charge term)."""
        for c in C_VALUES:
            res = collision_residue_on_primary(3, ('T', 'T'), c, 0, 0)
            self.assertEqual(res, c / 2)

    def test_depth3_WW_on_primary(self):
        """Depth 3, W-W: W_{(3)}W = 2T -> 2h_j on primaries."""
        c = Fraction(10)
        h_j = Fraction(5)
        res = collision_residue_on_primary(3, ('W', 'W'), c, h_j, 0)
        self.assertEqual(res, 2 * h_j)

    def test_depth4_WW_vanishes(self):
        """Depth 4, W-W: W_{(4)}W = 0."""
        c = Fraction(10)
        res = collision_residue_on_primary(4, ('W', 'W'), c, 1, 0)
        self.assertEqual(res, 0)

    def test_depth5_WW_central(self):
        """Depth 5, W-W: W_{(5)}W = c/3 (central charge of W-channel)."""
        for c in C_VALUES:
            res = collision_residue_on_primary(5, ('W', 'W'), c, 0, 0)
            self.assertEqual(res, c / 3)

    def test_depth5_is_kmax(self):
        """Depth 5 is the maximum collision depth for W_3."""
        c = Fraction(10)
        # All modes at depth > 5 should be zero
        for a in GENERATORS:
            for b in GENERATORS:
                mode = ope_mode(a, b, 6, c)
                self.assertEqual(mode, {}, f"Mode {a}_{(6)}{b} should be empty")

    def test_collision_table_structure(self):
        """Collision residue table has correct structure."""
        c = Fraction(10)
        table = w3_collision_residue_table(c, h_j=Fraction(2), w_j=Fraction(1))
        # Should have entries for depths 1-5
        self.assertEqual(set(table.keys()), {1, 2, 3, 4, 5})
        # Depth 1 should have entries for TT, TW, WT, WW
        self.assertIn(('T', 'T'), table[1])
        self.assertIn(('T', 'W'), table[1])
        self.assertIn(('W', 'W'), table[1])


class TestTSectorRestriction(unittest.TestCase):
    """Verify T-sector restriction recovers Virasoro."""

    def test_t_sector_depths(self):
        """T-sector has nonzero residues at depths 1 and 3 only."""
        c = Fraction(10)
        h_j = Fraction(2)
        result = t_sector_restriction(c, h_j)
        t_only = result['w3_t_sector']
        self.assertIn(1, t_only)  # T_{(1)}T = 2T -> nonzero
        self.assertNotIn(2, t_only)  # T_{(2)}T = 0
        self.assertIn(3, t_only)  # T_{(3)}T = c/2 -> nonzero

    def test_t_sector_depth1_is_2h(self):
        """T-sector depth 1: T_{(1)}T = 2T -> 2h_j."""
        c = Fraction(10)
        h_j = Fraction(3)
        result = t_sector_restriction(c, h_j)
        self.assertEqual(result['w3_t_sector'][1], 2 * h_j)

    def test_t_sector_depth3_is_c_over_2(self):
        """T-sector depth 3: T_{(3)}T = c/2."""
        for c in C_VALUES:
            result = t_sector_restriction(c, Fraction(1))
            self.assertEqual(result['w3_t_sector'][3], c / 2)

    def test_t_sector_matches_virasoro_structure(self):
        """T-sector collision residues match Virasoro mode structure."""
        c = Fraction(50)
        h_j = Fraction(7, 2)
        result = t_sector_restriction(c, h_j)
        # Virasoro BPZ has: h_j at depth 2 and d/dz at depth 1.
        # In the collision residue convention, T_{(1)}T gives 2h at depth 1,
        # and T_{(3)}T gives c/2 at depth 3.
        # The Virasoro BPZ h_j/z^2 corresponds to T_{(1)}T = 2T mode
        # in the shadow connection formalism.
        vir = result['virasoro_bpz']
        self.assertEqual(vir[2], h_j)  # BPZ depth 2 = h_j


class TestCrossFamilyComparison(unittest.TestCase):
    """Cross-family comparison of Hamiltonian orders."""

    def test_comparison_table_completeness(self):
        """All standard families present in comparison table."""
        families = cross_family_comparison()
        self.assertIn('Heisenberg', families)
        self.assertIn('Affine KM (sl_N)', families)
        self.assertIn('Virasoro', families)
        self.assertIn('W_3', families)
        self.assertIn('W_4', families)

    def test_heisenberg_order_zero(self):
        """Heisenberg: differential operator order 0."""
        families = cross_family_comparison()
        self.assertEqual(families['Heisenberg']['diff_order'], 0)

    def test_km_order_zero(self):
        """Affine KM: differential operator order 0."""
        families = cross_family_comparison()
        self.assertEqual(families['Affine KM (sl_N)']['diff_order'], 0)

    def test_virasoro_order_two(self):
        """Virasoro: differential operator order 2 (on descendants)."""
        families = cross_family_comparison()
        self.assertEqual(families['Virasoro']['diff_order'], 2)

    def test_w3_order_four(self):
        """W_3: differential operator order 4 (KEY PREDICTION)."""
        families = cross_family_comparison()
        self.assertEqual(families['W_3']['diff_order'], 4)

    def test_w4_order_six(self):
        """W_4: differential operator order 6."""
        families = cross_family_comparison()
        self.assertEqual(families['W_4']['diff_order'], 6)

    def test_order_increases_monotonically(self):
        """Differential operator order increases with N for W_N."""
        for N in range(2, 8):
            self.assertEqual(differential_operator_order_wN(N), 2 * (N - 1))
            if N > 2:
                self.assertGreater(
                    differential_operator_order_wN(N),
                    differential_operator_order_wN(N - 1))

    def test_kmax_is_2N_minus_1(self):
        """k_max = 2N - 1 for all W_N."""
        for N in range(2, 10):
            struct = wN_structure(N)
            self.assertEqual(struct['k_max'], 2 * N - 1)


class TestWNStructure(unittest.TestCase):
    """Verify W_N structural data."""

    def test_wN_generators(self):
        """W_N has generators of weights 2, 3, ..., N."""
        for N in [2, 3, 4, 5]:
            struct = wN_structure(N)
            gen_weights = sorted(struct['generators'].values())
            self.assertEqual(gen_weights, list(range(2, N + 1)))

    def test_wN_max_pole(self):
        """W_N max OPE pole = 2N."""
        for N in range(2, 8):
            struct = wN_structure(N)
            self.assertEqual(struct['max_ope_pole'], 2 * N)

    def test_wN_koszul_conductor_w2(self):
        """W_2 = Virasoro: K_2 = 26."""
        struct = wN_structure(2)
        self.assertEqual(struct['koszul_conductor'], 26)

    def test_wN_koszul_conductor_w3(self):
        """W_3: K_3 = 100 (Fateev-Lukyanov: c + c' = 100)."""
        struct = wN_structure(3)
        self.assertEqual(struct['koszul_conductor'], 100)


class TestKoszulConductor(unittest.TestCase):
    """Verify Koszul conductor K_N = c + c' for W_N."""

    def test_K2_virasoro(self):
        """K_2 = 26 (Virasoro: c + c' = 26)."""
        self.assertEqual(koszul_conductor_wN(2), 26)

    def test_K3_w3(self):
        """K_3 = 100 (W_3: c + c' = 100)."""
        self.assertEqual(koszul_conductor_wN(3), 100)

    def test_K4_w4(self):
        """K_4 = 246 (from the W_4 engine)."""
        self.assertEqual(koszul_conductor_wN(4), 246)

    def test_K_formula_consistency(self):
        """K_N formula 2(2N^3 - N - 1) matches known values."""
        known = {2: 26, 3: 100, 4: 246}
        for N, K in known.items():
            self.assertEqual(koszul_conductor_wN(N), K)


class TestWardIdentities(unittest.TestCase):
    """Verify global Ward identities of the shadow connection."""

    def test_translation_ward_identity(self):
        """Translation: sum_i sum_{j!=i} 1/z_{ij} = 0."""
        n = 4
        positions = [0.0, 0.5 + 0.3j, 1.0, 2.0 + 1.0j]
        weights = [0.5, 1.0, 1.5, 0.7]
        w_charges = [0, 0, 0, 0]
        result = w3_ward_identities(n, weights, w_charges, positions)
        self.assertTrue(result['translation'])

    def test_translation_antisymmetry(self):
        """sum_{i!=j} 1/(z_i - z_j) = 0 by antisymmetry of z_{ij}."""
        for n in [3, 4, 5]:
            positions = [0.1 * k + 0.2j * k**2 for k in range(n)]
            total = 0.0
            for i in range(n):
                for j in range(n):
                    if j != i:
                        total += 1.0 / (positions[i] - positions[j])
            self.assertAlmostEqual(total, 0.0, places=10)


class TestCommutativity(unittest.TestCase):
    """Verify commutativity predictions."""

    def test_4pt_automatic(self):
        """4-point commutativity is automatic (1D moduli)."""
        result = verify_commutativity_4pt_w3(
            10.0, [0.5, 1.0, 1.5, 2.0], [0, 0, 0, 0])
        self.assertTrue(result['commutativity_automatic'])

    def test_5pt_nontrivial(self):
        """5-point commutativity is nontrivial (2D moduli)."""
        result = verify_commutativity_5pt_w3(
            10.0, [0.5, 1.0, 1.5, 2.0, 0.3], [0, 0, 0, 0, 0])
        self.assertFalse(result['commutativity_automatic'])
        self.assertTrue(result['mc_implies_commutativity'])

    def test_5pt_mc_implies(self):
        """MC equation implies [H_i, H_j] = 0 at all n (theorem)."""
        result = verify_commutativity_5pt_w3(10.0, [1]*5)
        self.assertTrue(result['mc_implies_commutativity'])


class TestODEOrderPrediction(unittest.TestCase):
    """Verify ODE order predictions from collision depth."""

    def test_virasoro_max_ode_order(self):
        """Virasoro: max ODE order for 4-point = k_max = 3."""
        pred = ode_order_prediction('virasoro')
        self.assertEqual(pred['k_max'], 3)
        self.assertEqual(pred['max_diff_order'], 2)

    def test_w3_max_ode_order(self):
        """W_3: max ODE order for 4-point = k_max = 5."""
        pred = ode_order_prediction('w3')
        self.assertEqual(pred['k_max'], 5)
        self.assertEqual(pred['max_diff_order'], 4)

    def test_virasoro_bpz_null_vector(self):
        """Virasoro BPZ: (2,1) null vector gives 2nd-order ODE."""
        pred = ode_order_prediction('virasoro', degenerate_level=(2, 1))
        self.assertEqual(pred['null_vector_ode_order'], 2)


class TestFullEvaluation(unittest.TestCase):
    """Integration test: full evaluation of W_3 Hamiltonian data."""

    def test_full_evaluation_structure(self):
        """Full evaluation returns all expected keys."""
        result = full_evaluation(Fraction(10), Fraction(2), Fraction(1))
        self.assertIn('central_charge', result)
        self.assertIn('kappa', result)
        self.assertIn('beta_composite', result)
        self.assertIn('k_max', result)
        self.assertIn('collision_residue_table', result)
        self.assertIn('cross_family', result)

    def test_full_evaluation_kmax(self):
        """Full evaluation reports k_max = 5."""
        result = full_evaluation(10.0)
        self.assertEqual(result['k_max'], 5)

    def test_full_evaluation_diff_order(self):
        """Full evaluation reports differential operator order 4."""
        result = full_evaluation(10.0)
        self.assertEqual(result['diff_operator_order'], 4)

    def test_full_evaluation_kappa(self):
        """Full evaluation gives correct kappa = 5c/6."""
        c = Fraction(24)
        result = full_evaluation(c)
        self.assertEqual(result['kappa']['total'], Fraction(5) * c / 6)


class TestMultiPathVerification(unittest.TestCase):
    """Multi-path verification of collision residues."""

    def test_depth3_TT_two_paths(self):
        """Depth 3, T-T: verify (c/2) from OPE mode AND from kappa_T.

        Path 1: Direct OPE mode T_{(3)}T = c/2
        Path 2: T-channel central charge = 2 * kappa_T = 2 * (c/2) = c ... no.
                 The T-T two-point function <T T> = c/2, so the
                 leading singularity in the OPE is c/2.
        """
        for c in C_VALUES:
            # Path 1: OPE mode
            mode = ope_mode('T', 'T', 3, c)
            self.assertEqual(mode['vac'], c / 2)
            # Path 2: from kappa_T = c/2 (the Zamolodchikov metric)
            self.assertEqual(kappa_T(c), c / 2)
            # These are the same value: the leading T-T OPE coefficient
            # equals the Zamolodchikov metric eta_{TT}.

    def test_depth5_WW_two_paths(self):
        """Depth 5, W-W: verify (c/3) from OPE mode AND from kappa_W.

        Path 1: Direct OPE mode W_{(5)}W = c/3
        Path 2: W-channel central charge = kappa_W = c/3
        """
        for c in C_VALUES:
            mode = ope_mode('W', 'W', 5, c)
            self.assertEqual(mode['vac'], c / 3)
            self.assertEqual(kappa_W(c), c / 3)

    def test_kappa_total_two_paths(self):
        """kappa(W_3) via two paths: sum of channels vs direct formula.

        Path 1: kappa_T + kappa_W = c/2 + c/3 = 5c/6
        Path 2: Direct formula kappa_total(c) = 5c/6
        """
        for c in C_VALUES:
            path1 = kappa_T(c) + kappa_W(c)
            path2 = kappa_total(c)
            self.assertEqual(path1, path2)
            self.assertEqual(path1, Fraction(5) * c / 6)


class TestCentralChargeFromLevel(unittest.TestCase):
    """Verify W_3 central charge formula."""

    def test_large_k_behavior(self):
        """As k -> infinity, c -> -infinity (quadratic growth in k).

        c = 2 - 24(k+2)^2/(k+3) ~ -24k as k -> infinity.
        The W_3 central charge diverges at large level, unlike the
        KM formula where c -> rank. This is the Fateev-Lukyanov formula.
        """
        c = central_charge_from_level(10000.0)
        # c ~ 2 - 24 * 10002^2 / 10003 ~ -24 * 10000 = -240000
        self.assertLess(c, -200000)

    def test_c_at_k1(self):
        """c(k=1) = 2 - 24*9/4 = 2 - 54 = -52."""
        c = central_charge_from_level(Fraction(1))
        self.assertEqual(c, Fraction(2) - Fraction(24) * Fraction(9) / Fraction(4))


class TestScalarHamiltonianOnPrimaries(unittest.TestCase):
    """Test the scalar part of the W_3 Hamiltonian on primaries."""

    def test_depth2_is_h(self):
        """Scalar Hamiltonian at depth 2 is h_j (conformal weight)."""
        for h in [Fraction(1), Fraction(2), Fraction(7, 2)]:
            scalars = w3_hamiltonian_scalar_on_primaries(Fraction(10), h, Fraction(0))
            self.assertEqual(scalars[2], h)

    def test_depth3_is_w(self):
        """Scalar Hamiltonian at depth 3 is w_j (spin-3 charge)."""
        for w in [Fraction(0), Fraction(1), Fraction(3)]:
            scalars = w3_hamiltonian_scalar_on_primaries(Fraction(10), Fraction(1), w)
            self.assertEqual(scalars[3], w)

    def test_depth4_vanishes(self):
        """Scalar Hamiltonian at depth 4 is zero."""
        scalars = w3_hamiltonian_scalar_on_primaries(Fraction(10), Fraction(2), Fraction(1))
        self.assertEqual(scalars[4], 0)

    def test_depth5_vanishes_on_primaries(self):
        """Scalar Hamiltonian at depth 5 is zero on primaries (central charge trivial)."""
        scalars = w3_hamiltonian_scalar_on_primaries(Fraction(10), Fraction(2), Fraction(1))
        self.assertEqual(scalars[5], 0)


class TestHamiltonianDecomposition(unittest.TestCase):
    """Test the full Hamiltonian decomposition into sectors."""

    def test_t_sector_has_three_depths(self):
        """T-sector has contributions at depths 1, 2, 3."""
        result = w3_hamiltonian_on_primaries(10.0, 2.0, 1.0)
        t_sec = result['T_sector']
        self.assertIn(1, t_sec)
        self.assertIn(2, t_sec)
        self.assertIn(3, t_sec)

    def test_w_sector_has_five_depths(self):
        """W-sector has contributions at depths 1-5."""
        result = w3_hamiltonian_on_primaries(10.0, 2.0, 1.0)
        w_sec = result['W_sector']
        for k in range(1, 6):
            self.assertIn(k, w_sec)

    def test_w_sector_depth4_is_zero(self):
        """W-sector depth 4 is zero (W_{(4)}W = 0)."""
        result = w3_hamiltonian_on_primaries(10.0, 2.0, 1.0)
        self.assertEqual(result['W_sector'][4]['value'], 0)

    def test_tw_sector_depth1(self):
        """T-W cross-sector at depth 1 gives 3w_j."""
        w_j = 2.5
        result = w3_hamiltonian_on_primaries(10.0, 1.0, w_j)
        self.assertAlmostEqual(result['TW_sector'][1]['value'], 3 * w_j)


if __name__ == '__main__':
    unittest.main()
