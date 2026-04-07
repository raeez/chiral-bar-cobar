r"""Tests for the W_4 genus-2 cross-channel correction.

Verifies delta_F2(W_4) -- the first 3-channel genus-2 computation.

Test structure:
    1. Foundational data: kappa, lambda_FP, OPE structure constants
    2. Frobenius algebra: structure constants, 4-point vertices, parity
    3. Graph topology: genus, stability, automorphism groups
    4. Per-graph amplitudes: each of the 7 genus-2 stable graphs
    5. Cross-channel correction: the total delta_F2
    6. Rational/irrational decomposition
    7. Comparison with W_3 result
    8. Koszul duality: constraints at c <-> 246-c
    9. Limiting cases: large c, self-dual point
   10. Multi-path verification: independent floating-point cross-checks

Manuscript references:
    thm:theorem-d, op:multi-generator-universality,
    thm:multi-weight-genus-expansion, w4_ds_ope_extraction.py
"""

import math
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from w4_genus2_cross_channel import (
    CHANNELS,
    GENUS2_GRAPHS,
    WEIGHTS,
    K4,
    C3_generic,
    V04_generic,
    _half_edge_channels,
    delta_F2_w3,
    evaluate_at,
    g334_g444_product_squared,
    g334_squared,
    g444_squared,
    graph_amplitude_generic,
    graph_decomposition_generic,
    irrational_part_numerical,
    kappa_channel,
    kappa_total_val,
    lambda_fp,
    numerical_table,
    rational_part,
)


# ============================================================================
# 1. Foundational data
# ============================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify lambda_g^FP values."""

    def test_lambda1(self):
        from fractions import Fraction
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        from fractions import Fraction
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))


class TestKappaValues(unittest.TestCase):
    """Verify per-channel and total kappa for W_4."""

    def test_kappa_T(self):
        self.assertAlmostEqual(kappa_channel('T', 12), 6.0)

    def test_kappa_W3(self):
        self.assertAlmostEqual(kappa_channel('W3', 12), 4.0)

    def test_kappa_W4(self):
        self.assertAlmostEqual(kappa_channel('W4', 12), 3.0)

    def test_kappa_total(self):
        self.assertAlmostEqual(kappa_total_val(12), 13.0)

    def test_kappa_harmonic(self):
        """kappa(W_4) = c*(H_4 - 1) = c*(1/2 + 1/3 + 1/4) = 13c/12."""
        for c in [1, 2, 4, 10, 100]:
            expected = 13 * c / 12
            self.assertAlmostEqual(kappa_total_val(c), expected, places=10)

    def test_kappa_additivity(self):
        """kappa_total = kappa_T + kappa_W3 + kappa_W4."""
        for c in [1, 5, 50, 246]:
            total = sum(kappa_channel(ch, c) for ch in CHANNELS)
            self.assertAlmostEqual(total, kappa_total_val(c), places=10)


class TestOPEData(unittest.TestCase):
    """Verify OPE structure constants from Hornfeck 1993."""

    def test_g334_sq_positive_unitary(self):
        """g334^2 > 0 for c > 0 (unitary regime)."""
        for c in [1, 2, 10, 50, 100, 246]:
            self.assertGreater(float(g334_squared(c)), 0)

    def test_g444_sq_positive_above_half(self):
        """g444^2 > 0 for c > 1/2."""
        for c in [1, 2, 10, 50, 100, 246]:
            self.assertGreater(float(g444_squared(c)), 0)

    def test_g444_sq_zero_at_ising(self):
        """g444^2 = 0 at c = 1/2 (Ising point)."""
        val = float(g444_squared(0.5))
        self.assertAlmostEqual(val, 0.0, places=10)

    def test_g334_sq_classical_limit(self):
        """g334^2 -> 10 as c -> infinity."""
        val = float(g334_squared(100000))
        self.assertAlmostEqual(val, 10.0, places=2)

    def test_g444_sq_classical_limit(self):
        """g444^2 -> 48/25 = 1.92 as c -> infinity."""
        val = float(g444_squared(100000))
        self.assertAlmostEqual(val, 48 / 25, places=2)

    def test_product_squared_rational(self):
        """g334^2 * g444^2 is a rational function of c."""
        from sympy import Symbol, cancel
        c = Symbol('c', positive=True)
        p = g334_g444_product_squared(c)
        # Check it evaluates to a consistent float
        for cv in [1, 10, 100]:
            v1 = float(p.subs(c, cv))
            v2 = float(g334_squared(cv)) * float(g444_squared(cv))
            self.assertAlmostEqual(v1, v2, places=8)


# ============================================================================
# 2. Frobenius algebra
# ============================================================================

class TestFrobeniusAlgebra(unittest.TestCase):
    """Verify the W_4 Frobenius algebra structure constants."""

    def test_C3_universal_T_exchange(self):
        """C_{TTT} = C_{TW3W3} = C_{TW4W4} = c (universal T-exchange)."""
        c = 100
        self.assertEqual(C3_generic('T', 'T', 'T', c, 0, 0), c)
        self.assertEqual(C3_generic('T', 'W3', 'W3', c, 0, 0), c)
        self.assertEqual(C3_generic('T', 'W4', 'W4', c, 0, 0), c)

    def test_C3_parity_vanishing(self):
        """Odd W3-count vanishes."""
        c, g3, g4 = 100, 3.16, 1.39
        self.assertEqual(C3_generic('T', 'T', 'W3', c, g3, g4), 0)
        self.assertEqual(C3_generic('T', 'W3', 'W4', c, g3, g4), 0)
        self.assertEqual(C3_generic('W3', 'W3', 'W3', c, g3, g4), 0)
        self.assertEqual(C3_generic('W3', 'W4', 'W4', c, g3, g4), 0)

    def test_C3_W3W3W4(self):
        """C_{W3W3W4} = (c/4)*g334."""
        c, g3, g4 = 100, 3.16, 1.39
        expected = (c / 4) * g3
        self.assertAlmostEqual(
            C3_generic('W3', 'W3', 'W4', c, g3, g4), expected, places=8)

    def test_C3_W4W4W4(self):
        """C_{W4W4W4} = (c/4)*g444."""
        c, g3, g4 = 100, 3.16, 1.39
        expected = (c / 4) * g4
        self.assertAlmostEqual(
            C3_generic('W4', 'W4', 'W4', c, g3, g4), expected, places=8)

    def test_C3_symmetry(self):
        """C_{ijk} is symmetric under permutations."""
        c, g3, g4 = 50, 2.5, 1.2
        from itertools import permutations
        for i, j, k in [('T', 'W3', 'W3'), ('W3', 'W3', 'W4'), ('W4', 'W4', 'W4')]:
            vals = [C3_generic(*p, c, g3, g4) for p in permutations([i, j, k])]
            for v in vals:
                self.assertAlmostEqual(v, vals[0], places=10)

    def test_V04_universal_T_exchange(self):
        """V_{0,4}(i,i|j,j) = 2c when g334 = g444 = 0 (T-exchange only)."""
        c = 100
        for i in CHANNELS:
            for j in CHANNELS:
                v = V04_generic(i, i, j, j, c, 0, 0)
                self.assertAlmostEqual(v, 2 * c, places=8,
                                       msg=f"V04({i},{i}|{j},{j})")

    def test_V04_W4_correction(self):
        """V_{0,4}(W3,W3|W3,W3) = 2c + (c/4)*g334^2."""
        c, g3 = 100.0, 2.579
        v = V04_generic('W3', 'W3', 'W3', 'W3', c, g3, 0)
        expected = 2 * c + (c / 4) * g3**2
        self.assertAlmostEqual(v, expected, places=4)

    def test_V04_cross_term(self):
        """V_{0,4}(W3,W3|W4,W4) = 2c + (c/4)*g334*g444."""
        c, g3, g4 = 100.0, 2.579, 1.160
        v = V04_generic('W3', 'W3', 'W4', 'W4', c, g3, g4)
        expected = 2 * c + (c / 4) * g3 * g4
        self.assertAlmostEqual(v, expected, places=3)


# ============================================================================
# 3. Graph topology
# ============================================================================

class TestGraphTopology(unittest.TestCase):
    """Verify genus-2 stable graph data."""

    def test_genus_2(self):
        """All graphs have arithmetic genus 2."""
        for G in GENUS2_GRAPHS:
            n_v = len(G['vertices'])
            n_e = len(G['edges'])
            g_sum = sum(gv for gv, _ in G['vertices'])
            h1 = n_e - n_v + 1
            g_total = h1 + g_sum
            self.assertEqual(g_total, 2, f"{G['name']}: genus = {g_total}")

    def test_stability(self):
        """All vertices are stable: 2g_v + val_v >= 3."""
        for G in GENUS2_GRAPHS:
            for gv, nv in G['vertices']:
                self.assertGreaterEqual(2 * gv + nv, 3,
                                        f"{G['name']}: unstable ({gv},{nv})")

    def test_seven_graphs(self):
        """There are exactly 7 stable graphs at (g=2, n=0)."""
        self.assertEqual(len(GENUS2_GRAPHS), 7)

    def test_automorphism_groups(self):
        """Verify automorphism group orders."""
        expected = {'smooth': 1, 'fig_eight': 2, 'banana': 8,
                    'dumbbell': 2, 'theta': 12, 'lollipop': 2, 'barbell': 8}
        for G in GENUS2_GRAPHS:
            self.assertEqual(G['aut'], expected[G['name']])


# ============================================================================
# 4. Per-graph amplitudes
# ============================================================================

class TestFigEight(unittest.TestCase):
    """Figure-eight graph: 1 vertex (g=1, val=2), 1 self-loop, |Aut|=2."""

    def test_no_mixed(self):
        """Single edge: no mixed assignments possible."""
        for c in [10, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            decomp = graph_decomposition_generic(1, c, g3, g4)
            self.assertAlmostEqual(decomp['mixed'], 0.0, places=10)

    def test_total_3_over_48(self):
        """Total = 3/(48) = 1/16 (independent of c, g334, g444)."""
        for c in [1, 10, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            decomp = graph_decomposition_generic(1, c, g3, g4)
            self.assertAlmostEqual(decomp['total'], 1 / 16, places=10)


class TestDumbbell(unittest.TestCase):
    """Dumbbell: 2 vertices (g=1)+(g=1), 1 bridge, |Aut|=2."""

    def test_no_mixed(self):
        """Single edge: no mixed assignments possible."""
        for c in [10, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            decomp = graph_decomposition_generic(3, c, g3, g4)
            self.assertAlmostEqual(decomp['mixed'], 0.0, places=10)

    def test_total_c_proportional(self):
        """Dumbbell total = c/1536 for W₄ with physical OPE couplings."""
        for c in [12, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            decomp = graph_decomposition_generic(3, c, g3, g4)
            self.assertAlmostEqual(decomp['total'], c / 1536, places=10)


class TestBanana(unittest.TestCase):
    """Banana: 1 vertex (g=0, val=4), 2 self-loops, |Aut|=8."""

    def test_mixed_at_g334_g444_zero(self):
        """At g334=g444=0 (T-exchange only): mixed = 13/c."""
        for c in [10, 100]:
            decomp = graph_decomposition_generic(2, c, 0, 0)
            expected = 13.0 / c
            self.assertAlmostEqual(decomp['mixed'], expected, places=10)

    def test_mixed_positive(self):
        """Mixed amplitude is positive for c > 1/2."""
        for c in [1, 10, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            decomp = graph_decomposition_generic(2, c, g3, g4)
            self.assertGreater(decomp['mixed'], 0)


class TestTheta(unittest.TestCase):
    """Theta graph: 2 vertices (g=0,val=3)+(g=0,val=3), 3 bridges, |Aut|=12."""

    def test_rational_in_c(self):
        """Theta mixed amplitude is rational in c (no g444 dependence)."""
        for c in [10, 100]:
            # Theta involves only C_{ijk} at trivalent vertices.
            # The only non-universal C with even W3-count is C_{W3W3W4}.
            # The W3 parity at each trivalent vertex constrains the assignments.
            # g444 never appears (no W4W4W4 vertex in the theta graph).
            g3 = math.sqrt(float(g334_squared(c)))
            decomp1 = graph_decomposition_generic(4, c, g3, 0)
            decomp2 = graph_decomposition_generic(4, c, g3, 999)  # g444 irrelevant
            self.assertAlmostEqual(decomp1['mixed'], decomp2['mixed'], places=10)

    def test_mixed_at_g334_zero(self):
        """At g334=0: theta mixed = 25/(2c)."""
        for c in [10, 50, 100]:
            decomp = graph_decomposition_generic(4, c, 0, 0)
            expected = 25.0 / (2 * c)
            self.assertAlmostEqual(decomp['mixed'], expected, places=10)


class TestLollipop(unittest.TestCase):
    """Lollipop: vertex 0 (g=0,val=3) + vertex 1 (g=1,val=1), |Aut|=2."""

    def test_mixed_at_g334_zero(self):
        """At g334=0: lollipop mixed = 7/48."""
        for c in [10, 100]:
            decomp = graph_decomposition_generic(5, c, 0, 0)
            expected = 7.0 / 48
            self.assertAlmostEqual(decomp['mixed'], expected, places=10)

    def test_c_independent_rational_part(self):
        """Rational part 7/48 is independent of c."""
        val1 = 7.0 / 48
        for c in [1, 100, 1000]:
            decomp = graph_decomposition_generic(5, c, 0, 0)
            self.assertAlmostEqual(decomp['mixed'], val1, places=10)

    def test_irrational_term(self):
        """Mixed = 7/48 + g334/64 (the g334 term is irrational in c)."""
        for c in [10, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            decomp = graph_decomposition_generic(5, c, g3, 0)
            expected = 7.0 / 48 + g3 / 64
            self.assertAlmostEqual(decomp['mixed'], expected, places=8)


class TestBarbell(unittest.TestCase):
    """Barbell: 2 vertices (g=0,val=3), 2 self-loops + 1 bridge, |Aut|=8."""

    def test_mixed_at_g334_zero(self):
        """At g334=g444=0: barbell mixed = 77/(4c)."""
        for c in [10, 100]:
            decomp = graph_decomposition_generic(6, c, 0, 0)
            expected = 77.0 / (4 * c)
            self.assertAlmostEqual(decomp['mixed'], expected, places=10)

    def test_mixed_positive(self):
        """Mixed amplitude is positive for c > 1/2."""
        for c in [1, 10, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            decomp = graph_decomposition_generic(6, c, g3, g4)
            self.assertGreater(decomp['mixed'], 0)


# ============================================================================
# 5. Cross-channel correction: the total delta_F2
# ============================================================================

class TestDeltaF2Total(unittest.TestCase):
    """Verify the total cross-channel correction delta_F2(W_4)."""

    def test_positive_for_unitary(self):
        """delta_F2 > 0 for all c > 1/2."""
        for c in [1, 2, 4, 10, 26, 50, 100, 246]:
            r = evaluate_at(c)
            self.assertGreater(r['delta_F2'], 0,
                               f"delta_F2 not positive at c={c}")

    def test_formula_consistency(self):
        """delta_F2 = sum of per-graph mixed amplitudes."""
        for c in [10, 100]:
            r = evaluate_at(c)
            total = sum(r['per_graph'][G['name']]['mixed']
                        for G in GENUS2_GRAPHS)
            self.assertAlmostEqual(r['delta_F2'], total, places=10)

    def test_T_exchange_only(self):
        """At g334=g444=0: delta = (7c+2148)/(48c)."""
        for c in [10, 100, 246]:
            decomp_total = 0
            for idx in range(len(GENUS2_GRAPHS)):
                d = graph_decomposition_generic(idx, c, 0, 0)
                decomp_total += d['mixed']
            expected = (7 * c + 2148) / (48 * c)
            self.assertAlmostEqual(decomp_total, expected, places=10)

    def test_symbolic_formula(self):
        r"""The symbolic formula: 192c * delta = 3cg334 + 28c + 162g334^2 + 288g334g444 + 8592."""
        for c in [10, 50, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            r = evaluate_at(c)
            formula = (3 * c * g3 + 28 * c + 162 * g3**2 + 288 * g3 * g4 + 8592) / (192 * c)
            self.assertAlmostEqual(r['delta_F2'], formula, places=8)


# ============================================================================
# 6. Rational/irrational decomposition
# ============================================================================

class TestRationalIrrational(unittest.TestCase):
    """Verify the R(c) + I(c) decomposition of delta_F2."""

    def test_rational_part_formula(self):
        """R(c) = (147c^4 + 60823c^3 + ...)/[48c(c+24)(3c+46)(7c+68)]."""
        for c in [10, 100]:
            r_val = rational_part(c)
            num = 147*c**4 + 60823*c**3 + 2360126*c**2 + 34360800*c + 161254656
            den = 48*c*(c+24)*(3*c+46)*(7*c+68)
            expected = num / den
            self.assertAlmostEqual(r_val, expected, places=8)

    def test_irrational_part_formula(self):
        """I(c) = sqrt(g334^2)/64 + (3/2)*sqrt(g334^2*g444^2)/c."""
        for c in [10, 100]:
            irr = irrational_part_numerical(c)
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            expected = g3 / 64 + 1.5 * g3 * g4 / c
            self.assertAlmostEqual(irr, expected, places=10)

    def test_sum_equals_total(self):
        """R(c) + I(c) = delta_F2."""
        for c in [4, 26, 100, 246]:
            r = evaluate_at(c)
            sum_parts = rational_part(c) + irrational_part_numerical(c)
            self.assertAlmostEqual(r['delta_F2'], sum_parts, places=8)

    def test_irrational_positive(self):
        """I(c) > 0 for c > 1/2."""
        for c in [1, 10, 100]:
            irr = irrational_part_numerical(c)
            self.assertGreater(irr, 0)


# ============================================================================
# 7. Comparison with W_3
# ============================================================================

class TestW3Comparison(unittest.TestCase):
    """Compare delta_F2(W_4) with delta_F2(W_3) = (c+204)/(16c)."""

    def test_w4_exceeds_w3(self):
        """delta_F2(W_4) > delta_F2(W_3) for all c > 1/2.

        W_4 has more channels (3 vs 2), so more cross-channel mixing.
        """
        for c in [1, 10, 100, 246]:
            w4 = evaluate_at(c)['delta_F2']
            w3 = delta_F2_w3(c)
            self.assertGreater(w4, w3, f"W4 <= W3 at c={c}")

    def test_ratio_bounded_and_positive(self):
        """delta_W4/delta_W3 is positive and bounded for all c > 0."""
        for c in [10, 50, 100, 1000]:
            w4 = evaluate_at(c)['delta_F2']
            w3 = delta_F2_w3(c)
            ratio = w4 / w3
            self.assertGreater(ratio, 0, f"Ratio negative at c={c}")
            self.assertLess(ratio, 100, f"Ratio unbounded at c={c}")


# ============================================================================
# 8. Koszul duality
# ============================================================================

class TestKoszulDuality(unittest.TestCase):
    """Verify behavior under Koszul duality c <-> 246 - c."""

    def test_complementarity_sum(self):
        """K_4 = 246 (sl_4 complementarity sum)."""
        self.assertEqual(K4, 246)

    def test_kappa_complementarity(self):
        """kappa(c) + kappa(246-c) = 13*246/12 = 533/2."""
        for c in [10, 50, 123]:
            ksum = kappa_total_val(c) + kappa_total_val(246 - c)
            self.assertAlmostEqual(ksum, 13 * 246 / 12, places=8)

    def test_self_dual_point(self):
        """Self-dual point: c = 123."""
        r = evaluate_at(123)
        self.assertAlmostEqual(r['c'], 123)
        # delta_F2 should be well-defined at the self-dual point
        self.assertGreater(r['delta_F2'], 0)


# ============================================================================
# 9. Limiting cases
# ============================================================================

class TestLimits(unittest.TestCase):
    """Verify asymptotic behavior."""

    def test_large_c_convergence(self):
        """delta_F2 converges to a finite limit as c -> inf."""
        v1 = evaluate_at(1000)['delta_F2']
        v2 = evaluate_at(10000)['delta_F2']
        v3 = evaluate_at(100000)['delta_F2']
        # Convergent: successive differences decrease
        self.assertLess(abs(v3 - v2), abs(v2 - v1))
        # Finite and positive
        self.assertGreater(v3, 0)
        self.assertLess(v3, 1)

    def test_large_c_rational_part_finite(self):
        """Rational part is finite and positive at large c."""
        v = rational_part(10000)
        self.assertGreater(v, 0)
        self.assertLess(v, 1)

    def test_large_c_irrational_limit(self):
        """Irrational part -> sqrt(10)/64 as c -> inf."""
        expected = math.sqrt(10) / 64
        val = irrational_part_numerical(10000)
        self.assertAlmostEqual(val, expected, places=2)

    def test_diverges_as_c_to_zero(self):
        """delta_F2 diverges as c -> 0+."""
        val = evaluate_at(0.6)['delta_F2']
        self.assertGreater(val, 50)  # Diverges but at c=0.6 is ~75


# ============================================================================
# 10. Multi-path verification
# ============================================================================

class TestMultiPath(unittest.TestCase):
    """Independent cross-checks (multi-path verification mandate)."""

    def test_path1_direct_float_vs_evaluate(self):
        """Path 1: direct floating-point graph sum vs evaluate_at."""
        c = 100
        g3 = math.sqrt(float(g334_squared(c)))
        g4 = math.sqrt(float(g444_squared(c)))

        total_mixed = 0
        for idx in range(len(GENUS2_GRAPHS)):
            d = graph_decomposition_generic(idx, c, g3, g4)
            total_mixed += d['mixed']

        r = evaluate_at(c)
        self.assertAlmostEqual(total_mixed, r['delta_F2'], places=10)

    def test_path2_symbolic_formula(self):
        """Path 2: symbolic 192c*delta = 3cg+28c+162g^2+288gg'+8592."""
        for c in [4, 26, 100]:
            g3 = math.sqrt(float(g334_squared(c)))
            g4 = math.sqrt(float(g444_squared(c)))
            formula = (3*c*g3 + 28*c + 162*g3**2 + 288*g3*g4 + 8592) / (192*c)
            r = evaluate_at(c)
            self.assertAlmostEqual(r['delta_F2'], formula, places=8)

    def test_path3_rational_plus_irrational(self):
        """Path 3: R(c) + I(c) = delta_F2."""
        for c in [10, 100]:
            r = evaluate_at(c)
            rpi = rational_part(c) + irrational_part_numerical(c)
            self.assertAlmostEqual(r['delta_F2'], rpi, places=8)

    def test_consistency_at_c_equals_4(self):
        """Cross-check at c=4 (free boson pair central charge)."""
        r = evaluate_at(4)
        self.assertGreater(r['delta_F2'], 0)
        self.assertGreater(r['delta_F2'], delta_F2_w3(4))

    def test_fig_eight_universal(self):
        """Figure-eight total = 1/16, independent of OPE data (universal)."""
        for c in [1, 10, 100]:
            for g3, g4 in [(0, 0), (1, 1), (5, 3)]:
                decomp = graph_decomposition_generic(1, c, g3, g4)
                self.assertAlmostEqual(decomp['total'], 1 / 16, places=10)

    def test_dumbbell_universal_structure(self):
        """Dumbbell total is proportional to c, independent of OPE data."""
        for c in [10, 100]:
            decomp_a = graph_decomposition_generic(3, c, 0, 0)
            decomp_b = graph_decomposition_generic(3, c, 1, 1)
            self.assertAlmostEqual(decomp_a['total'] / c, decomp_b['total'] / c, places=10)

    def test_per_graph_sum_consistency(self):
        """Sum of per-graph contributions matches total at multiple c values."""
        for c in [2, 26, 123]:
            r = evaluate_at(c)
            graph_sum = sum(r['per_graph'][G['name']]['mixed']
                           for G in GENUS2_GRAPHS)
            self.assertAlmostEqual(graph_sum, r['delta_F2'], places=10,
                                   msg=f"Graph sum mismatch at c={c}")


if __name__ == '__main__':
    unittest.main()
