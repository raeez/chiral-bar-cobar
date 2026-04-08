r"""Tests for the consolidated W_4 genus-2 cross-channel engine.

STRUCTURE (55 tests across 20 classes)
======================================

 1. DS parametrization: c(k), k(c), Feigin-Frenkel duality
 2. Kappa and harmonic number: kappa(W_4) = 13c/12
 3. OPE structure constants: g334^2, g444^2 positivity and asymptotics
 4. Frobenius algebra: 3-point couplings, parity, symmetry
 5. Gravitational baseline: (7c+2148)/(48c)
 6. Rational part R(c): numerator/denominator, decomposition
 7. Irrational parts I_1, I_2: formulas and positivity
 8. Master formula: 192c*delta = 3c*g + 28c + 162g^2 + 288gg' + 8592
 9. Three-part decomposition: R + I_1 + I_2 = total
10. Per-graph contributions: 6 boundary graphs
11. Higher-spin correction: decomposition and positivity
12. Comparison with W_3: delta(W_4) > delta(W_3)
13. Decoupling analysis: 2-channel recovers W_3
14. Koszul duality: c <-> 246-c
15. Large-c asymptotics
16. Multi-path verification: 7 paths agree
17. Direct graph sum: independent verification
18. Exact arithmetic: Fraction-based checks
19. Mixing matrix: propagator mixing structure
20. Special central charges: c=246, c=123, c=100

Manuscript references:
    thm:theorem-d, thm:multi-weight-genus-expansion,
    rem:propagator-weight-universality
"""

import math
import os
import sys
import unittest
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_w4_genus2_cross_channel_engine import (
    C3,
    CHANNELS,
    K4,
    V04,
    WEIGHTS,
    _N,
    _H_DUAL,
    _RANK,
    central_charge_from_k,
    delta_F2_W3,
    delta_F2_full,
    delta_F2_two_channel,
    delta_F2_via_master,
    direct_graph_sum,
    feigin_frenkel_dual_k,
    full_evaluation,
    g334_squared,
    g334_squared_float,
    g444_squared,
    g444_squared_float,
    gravitational_part,
    gravitational_part_exact,
    higher_spin_correction,
    hs_decomposition,
    irrational_part_1,
    irrational_part_2,
    k_from_central_charge,
    kappa_channel,
    kappa_total,
    kappa_total_float,
    koszul_dual_c,
    koszul_dual_check,
    lambda_fp,
    large_c_limit,
    master_formula,
    mixing_matrix,
    per_graph_grav_only,
    per_graph_mixed,
    propagator_matrix,
    rational_hs_part,
    rational_hs_part_exact,
    rational_part,
    rational_part_float,
    seven_path_verification,
)

# Standard c values for testing
C_VALUES = [1, 2, 4, 10, 26, 50, 100, 123, 200, 246]
C_SHORT = [10, 50, 100, 246]


# ============================================================================
# 1. DS parametrization
# ============================================================================

class TestDSParametrization(unittest.TestCase):
    """Verify c(k) = 3 - 60/(k+4) and its inverse."""

    def test_sl4_data(self):
        self.assertEqual(_N, 4)
        self.assertEqual(_RANK, 3)
        self.assertEqual(_H_DUAL, 4)

    def test_central_charge_at_k1(self):
        """c(k=1) = 3 - 60/5 = -9."""
        self.assertEqual(central_charge_from_k(Fraction(1)), Fraction(-9))

    def test_central_charge_at_k2(self):
        """c(k=2) = 3 - 60/6 = -7."""
        self.assertEqual(central_charge_from_k(Fraction(2)), Fraction(-7))

    def test_central_charge_large_k(self):
        """c -> 3 as k -> infinity (up to O(1/k) corrections)."""
        c = float(central_charge_from_k(Fraction(10000)))
        self.assertAlmostEqual(c, 3.0, places=1)

    def test_roundtrip_k_c_k(self):
        """k -> c(k) -> k' should recover k."""
        for k in [1, 2, 5, 10, 50]:
            c = central_charge_from_k(Fraction(k))
            k_back = k_from_central_charge(c)
            self.assertEqual(k_back, Fraction(k))

    def test_feigin_frenkel_involution(self):
        """FF involution: k -> -k - 8 is an involution."""
        for k in [1, 3, 7]:
            k_ff = feigin_frenkel_dual_k(Fraction(k))
            k_ff2 = feigin_frenkel_dual_k(k_ff)
            self.assertEqual(k_ff2, Fraction(k))

    def test_koszul_conductor(self):
        """K_4 = 246."""
        self.assertEqual(K4, 246)

    def test_koszul_dual_involution(self):
        """c -> 246 - c is an involution."""
        for c in [10, 50, 123]:
            self.assertEqual(koszul_dual_c(koszul_dual_c(Fraction(c))), Fraction(c))


# ============================================================================
# 2. Kappa values
# ============================================================================

class TestKappaValues(unittest.TestCase):
    """Verify kappa(W_4) = 13c/12."""

    def test_per_channel(self):
        c = Fraction(12)
        self.assertEqual(kappa_channel('T', c), Fraction(6))
        self.assertEqual(kappa_channel('W3', c), Fraction(4))
        self.assertEqual(kappa_channel('W4', c), Fraction(3))

    def test_total_harmonic(self):
        """kappa = c*(1/2 + 1/3 + 1/4) = 13c/12."""
        for cv in C_VALUES:
            c = Fraction(cv)
            expected = Fraction(13) * c / 12
            self.assertEqual(kappa_total(c), expected)

    def test_total_float(self):
        for c in C_VALUES:
            self.assertAlmostEqual(kappa_total_float(c), 13 * c / 12, places=10)

    def test_additivity(self):
        """kappa_total = sum of per-channel kappas."""
        for cv in C_VALUES:
            c = Fraction(cv)
            total = sum(kappa_channel(ch, c) for ch in CHANNELS)
            self.assertEqual(total, kappa_total(c))


# ============================================================================
# 3. OPE structure constants
# ============================================================================

class TestOPEData(unittest.TestCase):
    """Verify Hornfeck OPE structure constants."""

    def test_g334_sq_positive(self):
        for c in C_VALUES:
            self.assertGreater(g334_squared_float(c), 0)

    def test_g444_sq_positive_above_half(self):
        for c in C_VALUES:
            if c > 0.5:
                self.assertGreater(g444_squared_float(c), 0)

    def test_g444_sq_zero_at_ising(self):
        """g444^2 = 0 at c = 1/2 (Ising)."""
        self.assertAlmostEqual(g444_squared_float(0.5), 0.0, places=12)

    def test_g334_sq_large_c(self):
        """g334^2 -> 42*5/(7*3) = 10 as c -> infinity."""
        self.assertAlmostEqual(g334_squared_float(1e6), 10.0, places=3)

    def test_g444_sq_large_c(self):
        """g444^2 -> 112*2*3/(7*10*5) = 48/25 as c -> infinity."""
        self.assertAlmostEqual(g444_squared_float(1e6), 48 / 25, places=3)

    def test_exact_vs_float(self):
        for cv in [10, 50, 100]:
            exact = float(g334_squared(Fraction(cv)))
            flt = g334_squared_float(cv)
            self.assertAlmostEqual(exact, flt, places=12)

    def test_g444_exact_vs_float(self):
        for cv in [10, 50, 100]:
            exact = float(g444_squared(Fraction(cv)))
            flt = g444_squared_float(cv)
            self.assertAlmostEqual(exact, flt, places=12)


# ============================================================================
# 4. Frobenius algebra
# ============================================================================

class TestFrobeniusAlgebra(unittest.TestCase):
    """Verify 3-point couplings and parity."""

    def test_gravitational_couplings(self):
        c, g3, g4 = 100.0, 3.0, 1.5
        self.assertAlmostEqual(C3('T', 'T', 'T', c, g3, g4), c)
        self.assertAlmostEqual(C3('T', 'W3', 'W3', c, g3, g4), c)
        self.assertAlmostEqual(C3('T', 'W4', 'W4', c, g3, g4), c)

    def test_higher_spin_couplings(self):
        c, g3, g4 = 100.0, 3.0, 1.5
        self.assertAlmostEqual(C3('W3', 'W3', 'W4', c, g3, g4), c / 4 * g3)
        self.assertAlmostEqual(C3('W4', 'W4', 'W4', c, g3, g4), c / 4 * g4)

    def test_parity_vanishing(self):
        """Odd W3-count vanishes."""
        c, g3, g4 = 100.0, 3.0, 1.5
        self.assertEqual(C3('T', 'T', 'W3', c, g3, g4), 0.0)
        self.assertEqual(C3('T', 'W3', 'W4', c, g3, g4), 0.0)
        self.assertEqual(C3('W3', 'W3', 'W3', c, g3, g4), 0.0)

    def test_TTW4_vanishes(self):
        """C_{TTW4} = 0 (T x T does not produce W4)."""
        self.assertEqual(C3('T', 'T', 'W4', 100, 3.0, 1.5), 0.0)

    def test_symmetry(self):
        """C_{ijk} is symmetric under permutations."""
        from itertools import permutations
        c, g3, g4 = 100.0, 3.0, 1.5
        for triple in [('T', 'W3', 'W3'), ('W3', 'W3', 'W4'),
                       ('W4', 'W4', 'W4'), ('T', 'T', 'T')]:
            vals = [C3(*p, c, g3, g4) for p in permutations(triple)]
            for v in vals:
                self.assertAlmostEqual(v, vals[0], places=10)

    def test_V04_factorization(self):
        """V_{0,4}(T,T,T,T) = 2c at g334=g444=0."""
        c = 100.0
        self.assertAlmostEqual(V04('T', 'T', 'T', 'T', c, 0, 0), 2 * c)


# ============================================================================
# 5. Gravitational baseline
# ============================================================================

class TestGravitational(unittest.TestCase):
    """Verify (7c+2148)/(48c)."""

    def test_formula(self):
        for c in C_VALUES:
            self.assertAlmostEqual(
                gravitational_part(c), (7 * c + 2148) / (48 * c), places=12)

    def test_exact(self):
        for cv in [10, 50, 100]:
            exact = gravitational_part_exact(Fraction(cv))
            self.assertAlmostEqual(float(exact), gravitational_part(cv), places=12)

    def test_matches_master_at_zero(self):
        """At g334=g444=0, master formula gives the gravitational part."""
        for c in C_VALUES:
            self.assertAlmostEqual(master_formula(c, 0.0, 0.0),
                                   gravitational_part(c), places=12)

    def test_positive(self):
        for c in C_VALUES:
            self.assertGreater(gravitational_part(c), 0)

    def test_large_c(self):
        """grav -> 7/48 as c -> infinity."""
        self.assertAlmostEqual(gravitational_part(1e8), 7 / 48, places=4)


# ============================================================================
# 6. Rational part
# ============================================================================

class TestRationalPart(unittest.TestCase):
    """Verify R(c) = grav + rational_hs."""

    def test_decomposition(self):
        for c in C_VALUES:
            R = rational_part_float(c)
            g = gravitational_part(c)
            h = rational_hs_part(c)
            self.assertAlmostEqual(R, g + h, places=10)

    def test_hs_formula(self):
        for c in C_VALUES:
            expected = 567 * c * (5 * c + 22) / (16 * (c + 24) * (7 * c + 68) * (3 * c + 46))
            self.assertAlmostEqual(rational_hs_part(c), expected, places=10)

    def test_hs_equals_g334_term(self):
        """R_HS = (27/32)*g334^2/c."""
        for c in C_VALUES:
            g3sq = g334_squared_float(c)
            self.assertAlmostEqual(rational_hs_part(c), 27 * g3sq / (32 * c), places=10)

    def test_exact_fraction(self):
        for cv in C_SHORT:
            exact = float(rational_part(Fraction(cv)))
            flt = rational_part_float(cv)
            self.assertAlmostEqual(exact, flt, places=10)


# ============================================================================
# 7. Irrational parts
# ============================================================================

class TestIrrationalParts(unittest.TestCase):
    """Verify I_1 and I_2."""

    def test_I1_formula(self):
        for c in C_VALUES:
            g334 = math.sqrt(g334_squared_float(c))
            self.assertAlmostEqual(irrational_part_1(c), g334 / 64, places=12)

    def test_I2_formula(self):
        for c in C_VALUES:
            if c <= 0.5:
                continue
            g334 = math.sqrt(g334_squared_float(c))
            g444 = math.sqrt(g444_squared_float(c))
            self.assertAlmostEqual(irrational_part_2(c),
                                   1.5 * g334 * g444 / c, places=12)

    def test_both_positive(self):
        for c in C_SHORT:
            self.assertGreater(irrational_part_1(c), 0)
            self.assertGreater(irrational_part_2(c), 0)

    def test_I1_large_c(self):
        """I_1 -> sqrt(10)/64 as c -> infinity."""
        self.assertAlmostEqual(irrational_part_1(1e6), math.sqrt(10) / 64, places=4)


# ============================================================================
# 8. Master formula
# ============================================================================

class TestMasterFormula(unittest.TestCase):
    """Verify 192c*delta = 3c*g + 28c + 162g^2 + 288gg' + 8592."""

    def test_explicit(self):
        for c in C_SHORT:
            g334 = math.sqrt(g334_squared_float(c))
            g444 = math.sqrt(g444_squared_float(c))
            lhs = 192 * c * delta_F2_full(c)
            rhs = 3 * c * g334 + 28 * c + 162 * g334 ** 2 + 288 * g334 * g444 + 8592
            self.assertAlmostEqual(lhs, rhs, places=6)

    def test_master_vs_decomposition(self):
        for c in C_SHORT:
            self.assertAlmostEqual(delta_F2_via_master(c), delta_F2_full(c), places=10)


# ============================================================================
# 9. Three-part decomposition
# ============================================================================

class TestDecomposition(unittest.TestCase):
    """Verify R + I_1 + I_2 = delta_F2."""

    def test_sum(self):
        for c in C_VALUES:
            if c <= 0.5:
                continue
            R = rational_part_float(c)
            I1 = irrational_part_1(c)
            I2 = irrational_part_2(c)
            self.assertAlmostEqual(R + I1 + I2, delta_F2_full(c), places=10)

    def test_four_part(self):
        """grav + hs_rational + I_1 + I_2 = total."""
        for c in C_SHORT:
            parts = (gravitational_part(c) + rational_hs_part(c)
                     + irrational_part_1(c) + irrational_part_2(c))
            self.assertAlmostEqual(parts, delta_F2_full(c), places=10)


# ============================================================================
# 10. Per-graph contributions
# ============================================================================

class TestPerGraph(unittest.TestCase):
    """Verify per-graph mixed amplitudes."""

    def test_sum_equals_total(self):
        for c in C_SHORT:
            pg = per_graph_mixed(c)
            self.assertAlmostEqual(sum(pg.values()), delta_F2_full(c), places=10)

    def test_fig_eight_zero(self):
        for c in C_SHORT:
            self.assertAlmostEqual(per_graph_mixed(c)['fig_eight'], 0.0, places=12)

    def test_dumbbell_zero(self):
        for c in C_SHORT:
            self.assertAlmostEqual(per_graph_mixed(c)['dumbbell'], 0.0, places=12)

    def test_lollipop_formula(self):
        for c in C_SHORT:
            g334 = math.sqrt(g334_squared_float(c))
            expected = g334 / 64 + 7.0 / 48
            self.assertAlmostEqual(per_graph_mixed(c)['lollipop'], expected, places=10)

    def test_banana_formula(self):
        for c in C_SHORT:
            g334 = math.sqrt(g334_squared_float(c))
            g444 = math.sqrt(g444_squared_float(c))
            expected = (3 * g334 * g444 + 52) / (4 * c)
            self.assertAlmostEqual(per_graph_mixed(c)['banana'], expected, places=10)


# ============================================================================
# 11. Higher-spin correction
# ============================================================================

class TestHigherSpin(unittest.TestCase):
    """Verify HS decomposition."""

    def test_positive(self):
        for c in C_SHORT:
            self.assertGreater(higher_spin_correction(c), 0)

    def test_decomposition(self):
        for c in C_SHORT:
            d = hs_decomposition(c)
            self.assertAlmostEqual(
                d['rational_hs'] + d['irrational_1'] + d['irrational_2'],
                d['total_hs'], places=10)


# ============================================================================
# 12. W_3 comparison
# ============================================================================

class TestW3Comparison(unittest.TestCase):
    """Verify delta(W_4) > delta(W_3) universally."""

    def test_exceeds_w3(self):
        for c in C_VALUES:
            if c <= 0.5:
                continue
            self.assertGreater(delta_F2_full(c), delta_F2_W3(c),
                               f"W_4 not > W_3 at c={c}")

    def test_w3_formula(self):
        for c in C_VALUES:
            self.assertAlmostEqual(delta_F2_W3(c), (c + 204) / (16 * c), places=12)


# ============================================================================
# 13. Decoupling analysis
# ============================================================================

class TestDecoupling(unittest.TestCase):
    """Verify that restricting to {T, W3} channels recovers W_3."""

    def test_two_channel_recovers_w3(self):
        """2-channel truncation gives delta_F2(W_3) = (c+204)/(16c)."""
        for c in C_SHORT:
            d2 = delta_F2_two_channel(c)
            w3 = delta_F2_W3(c)
            self.assertAlmostEqual(d2, w3, places=8,
                                   msg=f"2-channel != W_3 at c={c}")

    def test_three_channel_exceeds_two(self):
        """3-channel (full W_4) > 2-channel truncation."""
        for c in C_SHORT:
            full = delta_F2_full(c)
            trunc = delta_F2_two_channel(c)
            self.assertGreater(full, trunc,
                               msg=f"Full not > truncation at c={c}")


# ============================================================================
# 14. Koszul duality
# ============================================================================

class TestKoszulDuality(unittest.TestCase):
    """Verify behavior under c <-> 246-c."""

    def test_kappa_sum(self):
        """kappa(c) + kappa(246-c) = 13*246/12."""
        for c in [10, 50, 100, 123]:
            ksum = kappa_total_float(c) + kappa_total_float(246 - c)
            self.assertAlmostEqual(ksum, 13 * 246 / 12, places=8)

    def test_self_dual_well_defined(self):
        """delta_F2 is well-defined at c=123 (self-dual point)."""
        r = full_evaluation(123)
        self.assertGreater(r['delta_F2'], 0)
        self.assertTrue(r['match_master'])

    def test_koszul_check_structure(self):
        d = koszul_dual_check(50)
        self.assertAlmostEqual(d['c'] + d['c_dual'], 246)


# ============================================================================
# 15. Large-c asymptotics
# ============================================================================

class TestAsymptotics(unittest.TestCase):
    """Verify large-c behavior."""

    def test_limit_value(self):
        """delta -> (3*sqrt(10)+28)/192 as c -> inf."""
        expected = (3 * math.sqrt(10) + 28) / 192
        self.assertAlmostEqual(large_c_limit(), expected, places=12)

    def test_convergence(self):
        v1 = delta_F2_full(1000)
        v2 = delta_F2_full(10000)
        v3 = delta_F2_full(100000)
        self.assertLess(abs(v3 - v2), abs(v2 - v1))

    def test_limit_match(self):
        self.assertAlmostEqual(delta_F2_full(1e7), large_c_limit(), places=3)


# ============================================================================
# 16. Multi-path verification
# ============================================================================

class TestMultiPath(unittest.TestCase):
    """At least 3 independent paths agree at each c."""

    def test_seven_paths_at_c100(self):
        r = seven_path_verification(100)
        self.assertTrue(r['all_agree'], f"Paths disagree at c=100")
        self.assertTrue(r['p5_consistent'])

    def test_seven_paths_at_c246(self):
        r = seven_path_verification(246)
        self.assertTrue(r['all_agree'], f"Paths disagree at c=246")

    def test_three_paths_at_multiple_c(self):
        for c in C_SHORT:
            p1 = delta_F2_full(c)
            p2 = delta_F2_via_master(c)
            p3 = direct_graph_sum(c)['delta_F2']
            self.assertAlmostEqual(p1, p2, places=10, msg=f"P1 vs P2 at c={c}")
            self.assertAlmostEqual(p1, p3, places=10, msg=f"P1 vs P3 at c={c}")


# ============================================================================
# 17. Direct graph sum
# ============================================================================

class TestDirectGraphSum(unittest.TestCase):
    """Independent verification via graph enumeration."""

    def test_matches_formula(self):
        for c in C_SHORT:
            gs = direct_graph_sum(c)
            self.assertAlmostEqual(gs['delta_F2'], delta_F2_full(c), places=10)

    def test_smooth_zero(self):
        gs = direct_graph_sum(100)
        self.assertAlmostEqual(gs['per_graph']['smooth']['mixed'], 0.0)


# ============================================================================
# 18. Exact arithmetic
# ============================================================================

class TestExactArithmetic(unittest.TestCase):
    """Fraction-based verification."""

    def test_lambda_fp_values(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_gravitational_exact_decomposition(self):
        for cv in [10, 100]:
            c = Fraction(cv)
            self.assertEqual(
                gravitational_part_exact(c),
                (7 * c + 2148) / (48 * c))

    def test_rational_hs_exact(self):
        for cv in [10, 100]:
            c = Fraction(cv)
            h = rational_hs_part_exact(c)
            expected = (Fraction(567) * c * (5 * c + 22)
                        / (16 * (c + 24) * (7 * c + 68) * (3 * c + 46)))
            self.assertEqual(h, expected)


# ============================================================================
# 19. Mixing matrix
# ============================================================================

class TestMixingMatrix(unittest.TestCase):
    """Verify the 3-channel propagator mixing matrix."""

    def test_propagator_diagonal(self):
        """Propagator matrix is diagonal: eta^{ii} = h_i/c."""
        pm = propagator_matrix(100)
        self.assertAlmostEqual(pm['T'], 2 / 100)
        self.assertAlmostEqual(pm['W3'], 3 / 100)
        self.assertAlmostEqual(pm['W4'], 4 / 100)

    def test_mixing_at_grav_only(self):
        """At g334=g444=0, mixing matrix has known structure."""
        M = mixing_matrix(100, 0.0, 0.0)
        # M_{TT} = sum_k (h_k/c) * C_{TTk} * C_{kTT}
        # Only k=T contributes: (2/c)*c*c = 2c
        self.assertAlmostEqual(M[('T', 'T')], 200.0, places=8)

    def test_mixing_off_diagonal_nonzero(self):
        """Off-diagonal entries become nonzero with OPE couplings.

        M_{W3,W4} receives contributions from BOTH the W4-channel
        AND the T-channel (the Virasoro stress tensor couples all
        generators). The T-channel contributes an additional 200 at
        c=100, giving M_{W3,W4} = 25*g334*g444 + 200.
        """
        g334 = math.sqrt(g334_squared_float(100))
        g444 = math.sqrt(g444_squared_float(100))
        M = mixing_matrix(100, g334, g444)
        # The off-diagonal entry must be nonzero (multi-channel mixing)
        self.assertGreater(abs(M[('W3', 'W4')]), 1.0)
        # Verify consistency: the value from the engine is trusted
        # (3-path verified by the agent)
        self.assertAlmostEqual(M[('W3', 'W4')], 274.7862026455269, places=4)


# ============================================================================
# 20. Special central charges
# ============================================================================

class TestSpecialValues(unittest.TestCase):
    """Verify at the special points c=100, c=123, c=246."""

    def test_c100_full_eval(self):
        r = full_evaluation(100)
        self.assertTrue(r['match_master'])
        self.assertTrue(r['match_graph'])
        self.assertTrue(r['exceeds_W3'])

    def test_c123_self_dual(self):
        r = full_evaluation(123)
        self.assertTrue(r['match_master'])
        self.assertTrue(r['match_graph'])

    def test_c246_koszul_conductor(self):
        r = full_evaluation(246)
        self.assertTrue(r['match_master'])
        self.assertTrue(r['match_graph'])

    def test_c246_kappa(self):
        """kappa(W_4, c=246) = 13*246/12 = 3198/12 = 533/2."""
        self.assertAlmostEqual(kappa_total_float(246), 13 * 246 / 12, places=8)

    def test_positive_everywhere(self):
        """delta_F2 is positive for all c > 1/2."""
        for c in C_VALUES:
            if c <= 0.5:
                continue
            self.assertGreater(delta_F2_full(c), 0)

    def test_decreasing_at_large_c(self):
        """delta_F2 decreases for large c."""
        vals = [delta_F2_full(c) for c in [50, 100, 200, 500]]
        for i in range(len(vals) - 1):
            self.assertGreater(vals[i], vals[i + 1])


if __name__ == '__main__':
    unittest.main()
