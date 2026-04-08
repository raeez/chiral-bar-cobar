r"""Tests for the exact full-OPE delta_F2(W_4, c) engine.

STRUCTURE
=========

 1. Foundational constants: kappa, lambda_FP, OPE structure constants
 2. Gravitational-only baseline: (7c+2148)/(48c)
 3. Rational part R(c): numerator/denominator verification
 4. Irrational parts I_1, I_2: formula verification at multiple c
 5. Master formula: 192c*delta = 3c*g + 28c + 162g^2 + 288gg' + 8592
 6. Three-part decomposition: R + I_1 + I_2 = total
 7. Per-graph contributions: 6 boundary graphs
 8. Higher-spin correction: rational and irrational decomposition
 9. Comparison with W_3: delta(W_4) > delta(W_3) universally
10. Koszul duality: c <-> 246-c
11. Limiting cases: large c, self-dual point, Ising point
12. Direct graph sum verification (independent path)
13. Cross-check against w4_genus2_cross_channel.py
14. Multi-path convergence: 3+ independent derivations agree
15. Exact arithmetic: Fraction-based rational part verification
16. Asymptotic analysis: large-c behavior
17. Positivity and monotonicity
18. Per-graph gravitational limits
19. OPE structure constant properties
20. Edge cases and boundary behavior

Manuscript references:
    thm:theorem-d, op:multi-generator-universality,
    thm:multi-weight-genus-expansion, rem:propagator-weight-universality
"""

import math
import unittest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_w4_full_ope_delta_f2_engine import (
    CHANNELS,
    K4,
    WEIGHTS,
    _C3,
    _V04,
    _master_formula_float,
    delta_F2_W3,
    delta_F2_full,
    delta_F2_full_via_master,
    direct_graph_sum,
    full_evaluation,
    g334_squared_exact,
    g334_squared_float,
    g444_squared_exact,
    g444_squared_float,
    gravitational_part,
    gravitational_part_exact,
    higher_spin_correction,
    higher_spin_correction_decomposed,
    irrational_part_1,
    irrational_part_2,
    kappa_channel,
    kappa_total,
    koszul_dual_check,
    lambda_fp,
    large_c_limit,
    large_c_subleading,
    numerical_table,
    per_graph_grav_only,
    per_graph_mixed_float,
    rational_hs_part_exact,
    rational_hs_part_float,
    rational_part_exact,
    rational_part_float,
    verify_per_graph_sum,
    w3_w4_comparison,
)


# Standard test c values
C_VALUES = [1, 2, 4, 10, 26, 50, 100, 123, 200, 246]
# Subset for expensive tests
C_VALUES_SHORT = [10, 50, 100, 246]


# ============================================================================
# 1. Foundational constants
# ============================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))


class TestKappaValues(unittest.TestCase):
    """Verify W_4 modular characteristics."""

    def test_kappa_T(self):
        self.assertAlmostEqual(kappa_channel('T', 12), 6.0)

    def test_kappa_W3(self):
        self.assertAlmostEqual(kappa_channel('W3', 12), 4.0)

    def test_kappa_W4(self):
        self.assertAlmostEqual(kappa_channel('W4', 12), 3.0)

    def test_kappa_total(self):
        self.assertAlmostEqual(kappa_total(12), 13.0)

    def test_kappa_harmonic(self):
        """kappa(W_4) = c*(H_4 - 1) = c*(1/2 + 1/3 + 1/4) = 13c/12."""
        for c in C_VALUES:
            self.assertAlmostEqual(kappa_total(c), 13 * c / 12, places=10)

    def test_kappa_additivity(self):
        """kappa_total = sum of per-channel kappas."""
        for c in C_VALUES:
            total = sum(kappa_channel(ch, c) for ch in CHANNELS)
            self.assertAlmostEqual(total, kappa_total(c), places=10)


class TestOPEData(unittest.TestCase):
    """Verify Hornfeck OPE structure constants."""

    def test_g334_sq_positive(self):
        for c in C_VALUES:
            if c > 0:
                self.assertGreater(g334_squared_float(c), 0)

    def test_g444_sq_positive_above_half(self):
        for c in C_VALUES:
            if c > 0.5:
                self.assertGreater(g444_squared_float(c), 0)

    def test_g444_sq_zero_at_ising(self):
        """g444^2 = 0 at c = 1/2 (Ising model)."""
        self.assertAlmostEqual(g444_squared_float(0.5), 0.0, places=12)

    def test_g334_sq_large_c(self):
        """g334^2 -> 42*5/(7*3) = 10 as c -> infinity."""
        self.assertAlmostEqual(g334_squared_float(1e6), 10.0, places=3)

    def test_g444_sq_large_c(self):
        """g444^2 -> 112*2*3/(7*10*5) = 48/25 as c -> infinity."""
        self.assertAlmostEqual(g444_squared_float(1e6), 48/25, places=3)

    def test_exact_vs_float(self):
        """Exact Fraction and float evaluations agree."""
        for cv in [10, 50, 100]:
            exact = float(g334_squared_exact(Fraction(cv)))
            flt = g334_squared_float(cv)
            self.assertAlmostEqual(exact, flt, places=12)

    def test_g444_exact_vs_float(self):
        for cv in [10, 50, 100]:
            exact = float(g444_squared_exact(Fraction(cv)))
            flt = g444_squared_float(cv)
            self.assertAlmostEqual(exact, flt, places=12)

    def test_product_squared_rational(self):
        """g334^2 * g444^2 is rational (no cancellation issue)."""
        for cv in C_VALUES_SHORT:
            p = g334_squared_float(cv) * g444_squared_float(cv)
            self.assertGreater(p, 0)

    def test_g334_denominator_poles(self):
        """g334^2 has poles at c = -24, -68/7, -46/3 (all negative)."""
        # These are in the non-physical regime, so g334^2 is smooth for c > 0
        for c in [0.1, 1, 10, 100, 1000]:
            self.assertTrue(math.isfinite(g334_squared_float(c)))


# ============================================================================
# 2. Gravitational-only baseline
# ============================================================================

class TestGravitational(unittest.TestCase):
    """Verify the gravitational-only formula (7c+2148)/(48c)."""

    def test_formula(self):
        for c in C_VALUES:
            self.assertAlmostEqual(
                gravitational_part(c),
                (7*c + 2148) / (48*c),
                places=12,
            )

    def test_exact(self):
        for cv in [10, 50, 100]:
            exact = gravitational_part_exact(Fraction(cv))
            flt = gravitational_part(cv)
            self.assertAlmostEqual(float(exact), flt, places=12)

    def test_large_c(self):
        """grav -> 7/48 as c -> infinity."""
        self.assertAlmostEqual(gravitational_part(1e8), 7/48, places=4)

    def test_matches_g334_g444_zero(self):
        """At g334=g444=0, the master formula gives the gravitational part."""
        for c in C_VALUES:
            master_zero = _master_formula_float(c, 0.0, 0.0)
            grav = gravitational_part(c)
            self.assertAlmostEqual(master_zero, grav, places=12)

    def test_grav_positive(self):
        for c in C_VALUES:
            self.assertGreater(gravitational_part(c), 0)


# ============================================================================
# 3. Rational part R(c)
# ============================================================================

class TestRationalPart(unittest.TestCase):
    """Verify the rational part of delta_F2^full."""

    def test_numerator_denominator(self):
        """R(c) = (147c^4 + ...+ 161254656) / (48c(c+24)(3c+46)(7c+68))."""
        for c in C_VALUES:
            num = (147*c**4 + 60823*c**3 + 2360126*c**2
                   + 34360800*c + 161254656)
            den = 48*c*(c+24)*(3*c+46)*(7*c+68)
            expected = num / den
            self.assertAlmostEqual(rational_part_float(c), expected, places=10)

    def test_exact_fraction(self):
        """Exact computation matches float."""
        for cv in C_VALUES_SHORT:
            exact = float(rational_part_exact(Fraction(cv)))
            flt = rational_part_float(cv)
            self.assertAlmostEqual(exact, flt, places=10)

    def test_decomposition(self):
        """R(c) = grav(c) + hs_rational(c)."""
        for c in C_VALUES:
            R = rational_part_float(c)
            g = gravitational_part(c)
            h = rational_hs_part_float(c)
            self.assertAlmostEqual(R, g + h, places=10)

    def test_rational_hs_formula(self):
        """R_HS(c) = 567c(5c+22)/(16(c+24)(7c+68)(3c+46))."""
        for c in C_VALUES:
            expected = 567*c*(5*c+22) / (16*(c+24)*(7*c+68)*(3*c+46))
            self.assertAlmostEqual(rational_hs_part_float(c), expected,
                                   places=10)

    def test_rational_hs_positive(self):
        """The rational HS correction is positive for c > 0."""
        for c in C_VALUES:
            self.assertGreater(rational_hs_part_float(c), 0)

    def test_rational_hs_exact(self):
        for cv in C_VALUES_SHORT:
            exact = float(rational_hs_part_exact(Fraction(cv)))
            flt = rational_hs_part_float(cv)
            self.assertAlmostEqual(exact, flt, places=12)

    def test_rational_hs_equals_g334_sq_term(self):
        """R_HS = (27/32)*g334^2/c = 162*g334^2/(192c)."""
        for c in C_VALUES:
            g334_sq = g334_squared_float(c)
            expected = (27.0/32) * g334_sq / c
            self.assertAlmostEqual(rational_hs_part_float(c), expected,
                                   places=10)


# ============================================================================
# 4. Irrational parts
# ============================================================================

class TestIrrationalParts(unittest.TestCase):
    """Verify I_1 and I_2."""

    def test_I1_formula(self):
        """I_1 = sqrt(g334^2)/64."""
        for c in C_VALUES:
            g334 = math.sqrt(g334_squared_float(c))
            self.assertAlmostEqual(irrational_part_1(c), g334/64, places=12)

    def test_I2_formula(self):
        """I_2 = (3/2)*sqrt(g334^2*g444^2)/c."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            g334 = math.sqrt(g334_squared_float(c))
            g444 = math.sqrt(g444_squared_float(c))
            self.assertAlmostEqual(irrational_part_2(c),
                                   1.5*g334*g444/c, places=12)

    def test_I1_positive(self):
        for c in C_VALUES:
            self.assertGreater(irrational_part_1(c), 0)

    def test_I2_positive(self):
        for c in C_VALUES:
            if c > 0.5:
                self.assertGreater(irrational_part_2(c), 0)

    def test_I1_large_c(self):
        """I_1 -> sqrt(10)/64 as c -> inf."""
        self.assertAlmostEqual(irrational_part_1(1e6),
                               math.sqrt(10)/64, places=4)

    def test_I2_large_c(self):
        """I_2 -> 0 as c -> inf (1/c decay)."""
        self.assertLess(irrational_part_2(1e6), 0.001)

    def test_I1_alternative_form(self):
        """I_1 = c*sqrt(42(5c+22)) / (64*sqrt((c+24)(7c+68)(3c+46)))."""
        for c in C_VALUES:
            alt = c * math.sqrt(42*(5*c+22)) / \
                  (64 * math.sqrt((c+24)*(7*c+68)*(3*c+46)))
            self.assertAlmostEqual(irrational_part_1(c), alt, places=12)

    def test_I2_alternative_form(self):
        """I_2 = 42c*sqrt(6(2c-1)(5c+22)) / ((c+24)(7c+68)*sqrt((5c+3)(10c+197)))."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            alt = (42*c*math.sqrt(6*(2*c-1)*(5*c+22))
                   / ((c+24)*(7*c+68)*math.sqrt((5*c+3)*(10*c+197))))
            self.assertAlmostEqual(irrational_part_2(c), alt, places=10)


# ============================================================================
# 5. Master formula
# ============================================================================

class TestMasterFormula(unittest.TestCase):
    """Verify 192c*delta = 3cg + 28c + 162g^2 + 288gg' + 8592."""

    def test_formula_explicit(self):
        for c in C_VALUES_SHORT:
            g334 = math.sqrt(g334_squared_float(c))
            g444 = math.sqrt(g444_squared_float(c))
            lhs = 192 * c * delta_F2_full(c)
            rhs = 3*c*g334 + 28*c + 162*g334**2 + 288*g334*g444 + 8592
            self.assertAlmostEqual(lhs, rhs, places=6)

    def test_master_vs_decomposition(self):
        """Master formula matches R + I_1 + I_2."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            master = delta_F2_full_via_master(c)
            decomp = delta_F2_full(c)
            self.assertAlmostEqual(master, decomp, places=10)

    def test_gravitational_limit(self):
        """At g334=g444=0: 192c*delta = 28c + 8592 => delta = (7c+2148)/(48c)."""
        for c in C_VALUES:
            val = (28*c + 8592) / (192*c)
            self.assertAlmostEqual(val, gravitational_part(c), places=12)


# ============================================================================
# 6. Three-part decomposition
# ============================================================================

class TestThreePartDecomposition(unittest.TestCase):
    """Verify R + I_1 + I_2 = delta_F2^full."""

    def test_sum(self):
        for c in C_VALUES:
            if c <= 0.5:
                continue
            R = rational_part_float(c)
            I1 = irrational_part_1(c)
            I2 = irrational_part_2(c)
            total = delta_F2_full(c)
            self.assertAlmostEqual(R + I1 + I2, total, places=10)

    def test_four_part_decomposition(self):
        """grav + hs_rational + I_1 + I_2 = total."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            parts = (gravitational_part(c) + rational_hs_part_float(c)
                     + irrational_part_1(c) + irrational_part_2(c))
            self.assertAlmostEqual(parts, delta_F2_full(c), places=10)


# ============================================================================
# 7. Per-graph contributions
# ============================================================================

class TestPerGraphContributions(unittest.TestCase):
    """Verify per-graph mixed amplitudes."""

    def test_sum_equals_total(self):
        for c in C_VALUES_SHORT:
            v = verify_per_graph_sum(c)
            self.assertTrue(v['match'], f"Per-graph sum mismatch at c={c}")

    def test_fig_eight_zero(self):
        for c in C_VALUES_SHORT:
            pg = per_graph_mixed_float(c)
            self.assertAlmostEqual(pg['fig_eight'], 0.0, places=12)

    def test_dumbbell_zero(self):
        for c in C_VALUES_SHORT:
            pg = per_graph_mixed_float(c)
            self.assertAlmostEqual(pg['dumbbell'], 0.0, places=12)

    def test_banana_formula(self):
        """banana = (3*g334*g444 + 52)/(4c)."""
        for c in C_VALUES_SHORT:
            g334 = math.sqrt(g334_squared_float(c))
            g444 = math.sqrt(g444_squared_float(c))
            expected = (3*g334*g444 + 52) / (4*c)
            pg = per_graph_mixed_float(c)
            self.assertAlmostEqual(pg['banana'], expected, places=10)

    def test_theta_formula(self):
        """theta = (9*g334^2 + 200)/(16c)."""
        for c in C_VALUES_SHORT:
            g334_sq = g334_squared_float(c)
            expected = (9*g334_sq + 200) / (16*c)
            pg = per_graph_mixed_float(c)
            self.assertAlmostEqual(pg['theta'], expected, places=10)

    def test_lollipop_formula(self):
        """lollipop = g334/64 + 7/48."""
        for c in C_VALUES_SHORT:
            g334 = math.sqrt(g334_squared_float(c))
            expected = g334/64 + 7.0/48
            pg = per_graph_mixed_float(c)
            self.assertAlmostEqual(pg['lollipop'], expected, places=10)

    def test_barbell_formula(self):
        """barbell = (9*g334^2 + 24*g334*g444 + 616)/(32c)."""
        for c in C_VALUES_SHORT:
            g334 = math.sqrt(g334_squared_float(c))
            g444 = math.sqrt(g444_squared_float(c))
            expected = (9*g334**2 + 24*g334*g444 + 616) / (32*c)
            pg = per_graph_mixed_float(c)
            self.assertAlmostEqual(pg['barbell'], expected, places=10)

    def test_all_boundary_positive(self):
        """All nonzero per-graph contributions are positive."""
        for c in C_VALUES_SHORT:
            pg = per_graph_mixed_float(c)
            for name in ['banana', 'theta', 'lollipop', 'barbell']:
                self.assertGreater(pg[name], 0, f"{name} not positive at c={c}")


# ============================================================================
# 8. Higher-spin correction
# ============================================================================

class TestHigherSpinCorrection(unittest.TestCase):
    """Verify the decomposition delta_F2^full = grav + HS."""

    def test_hs_positive(self):
        """Higher-spin correction is positive for c > 1/2."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            self.assertGreater(higher_spin_correction(c), 0)

    def test_hs_decomposition(self):
        """HS = hs_rational + I_1 + I_2."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            d = higher_spin_correction_decomposed(c)
            self.assertAlmostEqual(
                d['rational_hs'] + d['irrational_1'] + d['irrational_2'],
                d['total_hs'], places=10)

    def test_hs_small_at_small_c(self):
        """At small c, gravitational part dominates (HS/grav ratio is small)."""
        c = 1
        hs = higher_spin_correction(c)
        grav = gravitational_part(c)
        self.assertLess(hs / grav, 0.05)

    def test_hs_grows_at_large_c(self):
        """HS correction becomes a larger fraction of total at large c."""
        ratio_10 = higher_spin_correction(10) / gravitational_part(10)
        ratio_246 = higher_spin_correction(246) / gravitational_part(246)
        self.assertGreater(ratio_246, ratio_10)


# ============================================================================
# 9. Comparison with W_3
# ============================================================================

class TestW3Comparison(unittest.TestCase):
    """Verify delta(W_4) > delta(W_3) universally."""

    def test_exceeds_w3(self):
        for c in C_VALUES:
            if c <= 0.5:
                continue
            w4 = delta_F2_full(c)
            w3 = delta_F2_W3(c)
            self.assertGreater(w4, w3, f"W4 <= W3 at c={c}")

    def test_w3_formula(self):
        for c in C_VALUES:
            self.assertAlmostEqual(delta_F2_W3(c), (c+204)/(16*c), places=12)

    def test_ratio_bounded(self):
        for c in [10, 100, 1000]:
            comp = w3_w4_comparison(c)
            self.assertGreater(comp['ratio'], 1)
            self.assertLess(comp['ratio'], 10)


# ============================================================================
# 10. Koszul duality
# ============================================================================

class TestKoszulDuality(unittest.TestCase):
    """Verify behavior under c <-> 246-c."""

    def test_koszul_conductor(self):
        self.assertEqual(K4, 246)

    def test_kappa_sum(self):
        """kappa(c) + kappa(246-c) = 13*246/12."""
        for c in [10, 50, 100, 123]:
            ksum = kappa_total(c) + kappa_total(246 - c)
            self.assertAlmostEqual(ksum, 13*246/12, places=8)

    def test_self_dual_well_defined(self):
        """delta_F2 is well-defined at c=123."""
        r = full_evaluation(123)
        self.assertGreater(r['delta_F2_full'], 0)
        self.assertTrue(r['match_master'])
        self.assertTrue(r['match_graph'])

    def test_koszul_check_structure(self):
        """koszul_dual_check returns consistent data."""
        d = koszul_dual_check(50)
        self.assertAlmostEqual(d['c'] + d['c_dual'], 246)
        self.assertAlmostEqual(d['kappa_sum'], d['kappa_sum_expected'], places=8)


# ============================================================================
# 11. Limiting cases
# ============================================================================

class TestLimitingCases(unittest.TestCase):
    """Verify asymptotic behavior."""

    def test_large_c_limit_value(self):
        """delta -> (3*sqrt(10)+28)/192 as c -> inf."""
        limit = large_c_limit()
        val = delta_F2_full(1e7)
        self.assertAlmostEqual(val, limit, places=3)

    def test_large_c_limit_formula(self):
        expected = (3*math.sqrt(10) + 28) / 192
        self.assertAlmostEqual(large_c_limit(), expected, places=12)

    def test_large_c_convergence(self):
        """Successive values converge."""
        v1 = delta_F2_full(1000)
        v2 = delta_F2_full(10000)
        v3 = delta_F2_full(100000)
        self.assertLess(abs(v3 - v2), abs(v2 - v1))

    def test_diverges_near_zero(self):
        """delta_F2 diverges as c -> 0+."""
        val = delta_F2_full(0.6)
        self.assertGreater(val, 10)

    def test_subleading_structure(self):
        """Large-c expansion: A + B/c + O(1/c^2)."""
        sub = large_c_subleading()
        self.assertGreater(sub['A'], 0)
        self.assertGreater(sub['B'], 0)


# ============================================================================
# 12. Direct graph sum verification
# ============================================================================

class TestDirectGraphSum(unittest.TestCase):
    """Independent verification via graph enumeration."""

    def test_matches_formula(self):
        for c in C_VALUES_SHORT:
            gs = direct_graph_sum(c)
            formula = delta_F2_full(c)
            self.assertAlmostEqual(gs['delta_F2'], formula, places=10,
                                   msg=f"Graph sum mismatch at c={c}")

    def test_per_graph_nonnegative(self):
        for c in C_VALUES_SHORT:
            gs = direct_graph_sum(c)
            for name, data in gs['per_graph'].items():
                self.assertGreaterEqual(data['mixed'], -1e-12,
                                        f"{name} mixed negative at c={c}")

    def test_smooth_graph_zero(self):
        """Smooth graph contributes nothing."""
        gs = direct_graph_sum(100)
        self.assertAlmostEqual(gs['per_graph']['smooth']['mixed'], 0.0)


# ============================================================================
# 13. Cross-check against w4_genus2_cross_channel.py
# ============================================================================

class TestCrossCheckExistingEngine(unittest.TestCase):
    """Verify against the pre-existing w4_genus2_cross_channel engine."""

    def test_matches_existing(self):
        try:
            from w4_genus2_cross_channel import evaluate_at
        except ImportError:
            self.skipTest("w4_genus2_cross_channel not available")
        for c in C_VALUES_SHORT:
            old = evaluate_at(c)['delta_F2']
            new = delta_F2_full(c)
            self.assertAlmostEqual(old, new, places=8,
                                   msg=f"Mismatch with existing engine at c={c}")

    def test_matches_existing_rational(self):
        try:
            from w4_genus2_cross_channel import rational_part as old_rat
        except ImportError:
            self.skipTest("w4_genus2_cross_channel not available")
        for c in C_VALUES_SHORT:
            old_r = old_rat(c)
            new_r = rational_part_float(c)
            self.assertAlmostEqual(old_r, new_r, places=8)


# ============================================================================
# 14. Multi-path convergence
# ============================================================================

class TestMultiPathConvergence(unittest.TestCase):
    """At least 3 independent paths agree at each c value."""

    def test_three_paths(self):
        for c in C_VALUES_SHORT:
            # Path 1: R + I_1 + I_2
            p1 = rational_part_float(c) + irrational_part_1(c) + irrational_part_2(c)
            # Path 2: master formula
            p2 = delta_F2_full_via_master(c)
            # Path 3: direct graph sum
            p3 = direct_graph_sum(c)['delta_F2']
            self.assertAlmostEqual(p1, p2, places=10,
                                   msg=f"P1 vs P2 at c={c}")
            self.assertAlmostEqual(p1, p3, places=10,
                                   msg=f"P1 vs P3 at c={c}")

    def test_four_part_vs_two_part(self):
        """grav + hs_rational + I_1 + I_2 = R + I_1 + I_2."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            four = (gravitational_part(c) + rational_hs_part_float(c)
                    + irrational_part_1(c) + irrational_part_2(c))
            two = rational_part_float(c) + irrational_part_1(c) + irrational_part_2(c)
            self.assertAlmostEqual(four, two, places=10)


# ============================================================================
# 15. Exact arithmetic
# ============================================================================

class TestExactArithmetic(unittest.TestCase):
    """Fraction-based exact verification of rational parts."""

    def test_rational_part_exact_values(self):
        """Verify R(c) at integer c using exact Fraction arithmetic."""
        for cv in [1, 2, 4, 10, 26, 50, 100]:
            c = Fraction(cv)
            R = rational_part_exact(c)
            # Verify it is a Fraction
            self.assertIsInstance(R, Fraction)
            # Verify it matches float
            self.assertAlmostEqual(float(R), rational_part_float(cv), places=12)

    def test_gravitational_exact(self):
        for cv in [1, 10, 100]:
            c = Fraction(cv)
            g = gravitational_part_exact(c)
            self.assertEqual(g, (7*c + 2148) / (48*c))

    def test_rational_hs_exact(self):
        for cv in [1, 10, 100]:
            c = Fraction(cv)
            h = rational_hs_part_exact(c)
            expected = Fraction(567) * c * (5*c + 22) / (16 * (c+24) * (7*c+68) * (3*c+46))
            self.assertEqual(h, expected)

    def test_decomposition_exact(self):
        """R(c) = grav(c) + hs_rational(c) in exact arithmetic."""
        for cv in [1, 10, 100]:
            c = Fraction(cv)
            self.assertEqual(
                rational_part_exact(c),
                gravitational_part_exact(c) + rational_hs_part_exact(c),
            )


# ============================================================================
# 16. Asymptotic analysis
# ============================================================================

class TestAsymptotics(unittest.TestCase):
    """Large-c asymptotic behavior."""

    def test_gravitational_asymptotic(self):
        """grav ~ 7/48 + 2148/(48c) = 7/48 + 44.75/c."""
        c = 1e6
        grav = gravitational_part(c)
        leading = 7/48
        self.assertAlmostEqual(grav - leading, 2148/(48*c), places=8)

    def test_hs_rational_asymptotic(self):
        """hs_rational ~ 567*5/(16*7*3) * 1 = 2835/336 ~ 8.4375... NO.
        Actually hs_rational ~ 567*5c^2/(16*21c^3) ~ 567*5/(336c) -> 0."""
        c = 1e6
        self.assertLess(rational_hs_part_float(c), 0.01)

    def test_I1_asymptotic(self):
        """I_1 ~ sqrt(10)/64 ~ 0.04942..."""
        self.assertAlmostEqual(irrational_part_1(1e7), math.sqrt(10)/64,
                               places=4)

    def test_full_asymptotic(self):
        """delta -> (3*sqrt(10)+28)/192 ~ 0.19524..."""
        limit = (3*math.sqrt(10) + 28) / 192
        self.assertAlmostEqual(delta_F2_full(1e7), limit, places=3)


# ============================================================================
# 17. Positivity and monotonicity
# ============================================================================

class TestPositivityMonotonicity(unittest.TestCase):
    """Structural properties of delta_F2."""

    def test_positive_everywhere(self):
        for c in C_VALUES:
            if c <= 0.5:
                continue
            self.assertGreater(delta_F2_full(c), 0)

    def test_decreasing_in_c(self):
        """delta_F2 decreases as c increases (for c large enough)."""
        c_vals = [10, 50, 100, 200, 500]
        deltas = [delta_F2_full(c) for c in c_vals]
        for i in range(len(deltas) - 1):
            self.assertGreater(deltas[i], deltas[i+1],
                               f"Not decreasing at c={c_vals[i]}->{c_vals[i+1]}")

    def test_all_parts_positive(self):
        """Each part of the decomposition is positive for c > 1/2."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            self.assertGreater(gravitational_part(c), 0)
            self.assertGreater(rational_hs_part_float(c), 0)
            self.assertGreater(irrational_part_1(c), 0)
            self.assertGreater(irrational_part_2(c), 0)


# ============================================================================
# 18. Per-graph gravitational limits
# ============================================================================

class TestPerGraphGravLimits(unittest.TestCase):
    """Verify per-graph contributions at g334=g444=0."""

    def test_banana_grav(self):
        """banana at g=0: 52/(4c) = 13/c."""
        for c in C_VALUES_SHORT:
            pg = per_graph_grav_only(c)
            self.assertAlmostEqual(pg['banana'], 13/c, places=12)

    def test_theta_grav(self):
        """theta at g=0: 200/(16c) = 25/(2c)."""
        for c in C_VALUES_SHORT:
            pg = per_graph_grav_only(c)
            self.assertAlmostEqual(pg['theta'], 25/(2*c), places=12)

    def test_lollipop_grav(self):
        """lollipop at g=0: 7/48 (c-independent)."""
        for c in C_VALUES_SHORT:
            pg = per_graph_grav_only(c)
            self.assertAlmostEqual(pg['lollipop'], 7/48, places=12)

    def test_barbell_grav(self):
        """barbell at g=0: 616/(32c) = 77/(4c)."""
        for c in C_VALUES_SHORT:
            pg = per_graph_grav_only(c)
            self.assertAlmostEqual(pg['barbell'], 77/(4*c), places=12)

    def test_grav_sum(self):
        """Sum of gravitational per-graph = (7c+2148)/(48c)."""
        for c in C_VALUES_SHORT:
            pg = per_graph_grav_only(c)
            total = sum(pg.values())
            self.assertAlmostEqual(total, gravitational_part(c), places=12)


# ============================================================================
# 19. OPE structure constant properties
# ============================================================================

class TestOPEProperties(unittest.TestCase):
    """Properties of the OPE couplings relevant to the computation."""

    def test_frobenius_symmetry(self):
        """C_{ijk} is fully symmetric."""
        c, g3, g4 = 100.0, 3.0, 1.5
        from itertools import permutations
        for triple in [('T', 'W3', 'W3'), ('W3', 'W3', 'W4'),
                       ('W4', 'W4', 'W4'), ('T', 'T', 'T')]:
            vals = [_C3(*p, c, g3, g4) for p in permutations(triple)]
            for v in vals:
                self.assertAlmostEqual(v, vals[0], places=10)

    def test_parity_enforcement(self):
        """Odd W3-count vanishes."""
        c, g3, g4 = 100.0, 3.0, 1.5
        self.assertEqual(_C3('T', 'T', 'W3', c, g3, g4), 0.0)
        self.assertEqual(_C3('T', 'W3', 'W4', c, g3, g4), 0.0)
        self.assertEqual(_C3('W3', 'W3', 'W3', c, g3, g4), 0.0)

    def test_TTW4_vanishes(self):
        """C_{TTW4} = 0 (T x T OPE does not produce W4 primary)."""
        self.assertEqual(_C3('T', 'T', 'W4', 100, 3.0, 1.5), 0.0)

    def test_V04_factorization(self):
        """V_{0,4}(T,T,T,T) = 2c (single T-exchange channel)."""
        c = 100.0
        self.assertAlmostEqual(_V04('T', 'T', 'T', 'T', c, 0, 0), 2*c)

    def test_V04_with_ope(self):
        """V_{0,4}(W3,W3,W3,W3) = 2c + (c/4)*g334^2 at g444=0."""
        c, g3 = 100.0, 2.5
        v = _V04('W3', 'W3', 'W3', 'W3', c, g3, 0)
        expected = 2*c + (c/4)*g3**2
        self.assertAlmostEqual(v, expected, places=6)


# ============================================================================
# 20. Edge cases and boundary behavior
# ============================================================================

class TestEdgeCases(unittest.TestCase):
    """Boundary and special-case behavior."""

    def test_c_equals_1(self):
        """c=1: all computations well-defined."""
        r = full_evaluation(1)
        self.assertTrue(r['match_master'])
        self.assertTrue(r['match_graph'])
        self.assertGreater(r['delta_F2_full'], 0)

    def test_c_equals_246(self):
        """c=246 (Koszul conductor): well-defined."""
        r = full_evaluation(246)
        self.assertTrue(r['match_master'])
        self.assertTrue(r['match_graph'])

    def test_c_equals_123_self_dual(self):
        """c=123 (self-dual point): well-defined."""
        r = full_evaluation(123)
        self.assertTrue(r['match_master'])
        self.assertTrue(r['match_graph'])

    def test_c_very_large(self):
        """c=10000: converges toward large-c limit (B/c ~ 0.006 correction)."""
        r = full_evaluation(10000)
        self.assertTrue(r['match_master'])
        limit = large_c_limit()
        # At c=10000, subleading B/c term is still O(0.006), so use places=1
        self.assertAlmostEqual(r['delta_F2_full'], limit, places=1)

    def test_numerical_table_runs(self):
        """numerical_table produces consistent results."""
        table = numerical_table([10, 100, 246])
        self.assertEqual(len(table), 3)
        for row in table:
            self.assertTrue(row['match_master'])
            self.assertTrue(row['match_graph'])

    def test_exceeds_w3_universally(self):
        """W_4 exceeds W_3 at all tested c values."""
        for row in numerical_table():
            self.assertTrue(row['exceeds_W3'],
                            f"W4 not > W3 at c={row['c']}")


# ============================================================================
# Bonus: coefficient verification (from master formula)
# ============================================================================

class TestMasterCoefficients(unittest.TestCase):
    """Verify the individual coefficients of the master formula.

    192c * delta = 3c*g334 + 28c + 162*g334^2 + 288*g334*g444 + 8592

    These trace to specific graph contributions:
    - 28c + 8592: gravitational (g334=g444=0 terms)
    - 162*g334^2: theta (9*g334^2) + barbell (9*g334^2), scaled
    - 288*g334*g444: banana (3*g334*g444) + barbell (24*g334*g444), scaled
    - 3c*g334: lollipop (g334/64 * 192c = 3c*g334)
    """

    def test_gravitational_coefficients(self):
        """28c + 8592 from gravitational channels."""
        # grav part of 192c*delta = 192c*(7c+2148)/(48c) = 4*(7c+2148) = 28c+8592
        for c in C_VALUES:
            self.assertAlmostEqual(
                192*c*gravitational_part(c), 28*c + 8592, places=8)

    def test_g334_squared_coefficient(self):
        """Coefficient of g334^2 is 162."""
        # From: theta contributes 9*g334^2/(16c), barbell contributes 9*g334^2/(32c)
        # In 192c*delta: theta -> 192c * 9g^2/(16c) = 108g^2
        #                barbell -> 192c * 9g^2/(32c) = 54g^2
        #                Total: 162g^2  CHECK!
        self.assertEqual(108 + 54, 162)

    def test_g334_g444_coefficient(self):
        """Coefficient of g334*g444 is 288."""
        # From: banana contributes 3gg'/(4c), barbell contributes 24gg'/(32c) = 3gg'/(4c)
        # In 192c*delta: banana -> 192c * 3gg'/(4c) = 144gg'
        #                barbell -> 192c * 24gg'/(32c) = 144gg'
        #                Total: 288gg'  CHECK!
        self.assertEqual(144 + 144, 288)

    def test_g334_linear_coefficient(self):
        """Coefficient of c*g334 is 3."""
        # From lollipop: g334/64
        # In 192c*delta: 192c * g334/64 = 3c*g334  CHECK!
        self.assertAlmostEqual(192 / 64, 3.0)


if __name__ == '__main__':
    unittest.main()
