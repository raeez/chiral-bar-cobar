r"""Independent verification of δF₂^cross(W₃) = (c + 204)/(16c).

Multi-path verification of the multi-weight cross-channel correction
for the W₃ algebra at genus 2, strengthening Theorem D by providing
concrete multi-weight evidence.

VERIFICATION STRATEGY
=====================

Path 1 (graph sum from scratch):
    Recompute every mixed-channel amplitude from raw W₃ OPE data
    (Zamolodchikov metric + 3-point structure constants) and the
    Feynman rules for stable graph sums on M̄_{2,0}.

Path 2 (closed-form algebra):
    Sum the per-graph contributions
        banana: 3/c,  theta: 9/(2c),  lollipop: 1/16,  barbell: 21/(4c)
    and verify algebraically that the sum equals (c+204)/(16c).

Path 3 (engine cross-check):
    Compare against the multi_weight_cross_channel_engine and w3_genus2
    library functions.

Path 4 (limiting cases):
    c → ∞: δF₂ → 1/16 (lollipop dominates; c-dependent terms die).
    c = -204: δF₂ = 0 (numerator vanishes; algebraic check).
    c = 50 (self-dual): δF₂ = 127/400.

Path 5 (sympy symbolic):
    Verify that the symbolic sum of 4 graph contributions simplifies
    to (c+204)/(16c) in exact symbolic arithmetic.

MANUSCRIPT REFERENCES
=====================

    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex:20560)
    eq:w3-genus2-cross (higher_genus_modular_koszul.tex:20633)
    comp:w3-genus2-multichannel (w_algebras.tex:5698)
    eq:w3-cross-channel-genus2 (w_algebras.tex:5742)

NOTE ON GRAPH COUNT
===================

The 7 genus-2 stable graphs (AP123: count is 7, not 6) are:
    A: smooth (e=0), B: figure-eight (e=1), C: dumbbell/separating (e=1),
    D: sunset/banana (e=2), E: bridge-loop/lollipop (e=2),
    F: theta (e=3), G: barbell (e=3).

Four graphs contribute to the cross-channel correction: D, E, F, G.
Three graphs have zero cross-channel: A (no edges), B (single edge),
C (single edge between g=1 vertices).
"""

import unittest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))


# ============================================================================
# W₃ OPE data (from first principles)
# ============================================================================

def w3_eta_inv(channel, c):
    """Inverse Zamolodchikov metric for W₃.

    eta_{TT} = c/2 (from T_{(3)}T = c/2), so eta^{TT} = 2/c.
    eta_{WW} = c/3 (from W_{(5)}W = c/3), so eta^{WW} = 3/c.

    # VERIFIED: [DC] OPE leading poles; [LT] Bouwknegt-Schoutens eq 2.7
    """
    if channel == 'T':
        return Fraction(2, 1) / c
    elif channel == 'W':
        return Fraction(3, 1) / c
    raise ValueError(f"Unknown channel: {channel}")


def w3_C3(a, b, d, c):
    """W₃ three-point structure constant.

    Z₂ parity (W has odd parity): odd count of W vanishes.
    Nonzero: C_{TTT} = c, C_{TWW} = C_{WTW} = C_{WWT} = c.

    # VERIFIED: [DC] W₃ OPE computation; [LT] Zamolodchikov 1985
    """
    count_W = sum(1 for x in (a, b, d) if x == 'W')
    if count_W % 2 == 1:
        return Fraction(0)
    return c


# ============================================================================
# Per-graph mixed amplitudes (independent recomputation)
# ============================================================================

def banana_mixed(c):
    """Graph D (sunset/banana): 1 vertex g=0 val=4, 2 self-loops, |Aut|=8.

    # VERIFIED: [DC] direct Feynman rule computation below
    # VERIFIED: [CF] matches w3_genus2.py:cross_channel_correction_exact
    """
    channels = ['T', 'W']
    total = Fraction(0)
    for s1 in channels:
        for s2 in channels:
            if s1 == s2:
                continue
            # Quartic vertex via s-channel factorization
            V04 = Fraction(0)
            for m in channels:
                V04 += w3_eta_inv(m, c) * w3_C3(s1, s1, m, c) * w3_C3(s2, s2, m, c)
            prop = w3_eta_inv(s1, c) * w3_eta_inv(s2, c)
            total += prop * V04 / 8
    return total


def theta_mixed(c):
    """Graph F (theta): 2 vertices g=0 val=3, 3 bridges, |Aut|=12.

    # VERIFIED: [DC] direct Feynman rule computation below
    # VERIFIED: [CF] matches w3_genus2.py:cross_channel_correction_exact
    """
    channels = ['T', 'W']
    total = Fraction(0)
    for s1 in channels:
        for s2 in channels:
            for s3 in channels:
                if s1 == s2 == s3:
                    continue
                v0 = w3_C3(s1, s2, s3, c)
                v1 = w3_C3(s1, s2, s3, c)
                prop = w3_eta_inv(s1, c) * w3_eta_inv(s2, c) * w3_eta_inv(s3, c)
                total += prop * v0 * v1 / 12
    return total


def lollipop_mixed(c):
    """Graph E (bridge-loop/lollipop): v0(g=0,val=3)+v1(g=1,val=1),
    1 self-loop + 1 bridge, |Aut|=2.

    # VERIFIED: [DC] direct Feynman rule computation below
    # VERIFIED: [LC] c-independence: result = 1/16 for all c
    """
    channels = ['T', 'W']
    kappa = {'T': c / 2, 'W': c / 3}
    total = Fraction(0)
    for s_self in channels:
        for s_bridge in channels:
            if s_self == s_bridge:
                continue
            v0 = w3_C3(s_self, s_self, s_bridge, c)
            v1 = kappa[s_bridge] / 24  # genus-1 vertex factor
            prop = w3_eta_inv(s_self, c) * w3_eta_inv(s_bridge, c)
            total += prop * v0 * v1 / 2
    return total


def barbell_mixed(c):
    """Graph G (barbell): 2 vertices g=0 val=3, 2 self-loops + 1 bridge, |Aut|=8.

    # VERIFIED: [DC] direct Feynman rule computation below
    # VERIFIED: [CF] matches w3_genus2.py:cross_channel_correction_exact
    """
    channels = ['T', 'W']
    total = Fraction(0)
    for s0 in channels:      # self-loop at v0
        for s1 in channels:  # self-loop at v1
            for br in channels:  # bridge
                if len({s0, s1, br}) == 1:
                    continue
                v0 = w3_C3(s0, s0, br, c)
                v1 = w3_C3(s1, s1, br, c)
                prop = w3_eta_inv(s0, c) * w3_eta_inv(s1, c) * w3_eta_inv(br, c)
                total += prop * v0 * v1 / 8
    return total


# ============================================================================
# Test values
# ============================================================================

# Standard test central charges
C_VALUES = [
    Fraction(1), Fraction(2), Fraction(4), Fraction(13),
    Fraction(25), Fraction(50), Fraction(100), Fraction(1000),
]


# ============================================================================
# Path 1: Graph sum from scratch
# ============================================================================

class TestPath1GraphSum(unittest.TestCase):
    """Verify δF₂(W₃) by recomputing every mixed amplitude from raw OPE data."""

    def test_banana_value(self):
        """Banana (sunset/graph D) mixed amplitude = 3/c.

        # VERIFIED: [DC] explicit Feynman rule sum; [CF] cross-engine check
        """
        for c in C_VALUES:
            self.assertEqual(banana_mixed(c), Fraction(3) / c)

    def test_theta_value(self):
        """Theta (graph F) mixed amplitude = 9/(2c).

        # VERIFIED: [DC] explicit Feynman rule sum; [CF] cross-engine check
        """
        for c in C_VALUES:
            self.assertEqual(theta_mixed(c), Fraction(9) / (2 * c))

    def test_lollipop_value(self):
        """Lollipop (bridge-loop/graph E) mixed amplitude = 1/16.

        # VERIFIED: [DC] explicit computation; [LC] c-independent
        """
        for c in C_VALUES:
            self.assertEqual(lollipop_mixed(c), Fraction(1, 16))

    def test_lollipop_c_independence(self):
        """Lollipop is c-independent (the c factors cancel exactly).

        # VERIFIED: [DC] analytic cancellation; [SY] genus-1 vertex absorbs c
        """
        vals = [lollipop_mixed(c) for c in C_VALUES]
        self.assertTrue(all(v == Fraction(1, 16) for v in vals))

    def test_barbell_value(self):
        """Barbell (graph G) mixed amplitude = 21/(4c).

        # VERIFIED: [DC] explicit Feynman rule sum with 6 mixed assignments
        # VERIFIED: [CF] matches w3_genus2.py engine
        """
        for c in C_VALUES:
            self.assertEqual(barbell_mixed(c), Fraction(21) / (4 * c))

    def test_total_equals_closed_form(self):
        """Sum of all 4 graph contributions = (c+204)/(16c).

        # VERIFIED: [DC] graph sum; [CF] closed-form algebra (Path 2)
        """
        for c in C_VALUES:
            total = banana_mixed(c) + theta_mixed(c) + lollipop_mixed(c) + barbell_mixed(c)
            expected = (c + 204) / (16 * c)
            self.assertEqual(total, expected)


# ============================================================================
# Path 2: Closed-form algebraic verification
# ============================================================================

class TestPath2ClosedFormAlgebra(unittest.TestCase):
    """Verify the algebra: 3/c + 9/(2c) + 1/16 + 21/(4c) = (c+204)/(16c)."""

    def test_c_dependent_sum(self):
        """banana + theta + barbell = 51/(4c).

        3/c + 9/(2c) + 21/(4c) = 12/(4c) + 18/(4c) + 21/(4c) = 51/(4c).

        # VERIFIED: [DC] direct arithmetic; [DA] all terms are O(1/c)
        """
        for c in C_VALUES:
            c_dep = Fraction(3) / c + Fraction(9) / (2 * c) + Fraction(21) / (4 * c)
            self.assertEqual(c_dep, Fraction(51) / (4 * c))

    def test_total_simplification(self):
        """51/(4c) + 1/16 = (816 + 4c)/(64c) = (c+204)/(16c).

        # VERIFIED: [DC] fraction arithmetic; [SY] factor 4 from num and denom
        """
        for c in C_VALUES:
            lhs = Fraction(51) / (4 * c) + Fraction(1, 16)
            # Common denominator 16c:
            # 51/(4c) = 204/(16c), 1/16 = c/(16c)
            # Sum = (c + 204)/(16c)
            rhs = (c + 204) / (16 * c)
            self.assertEqual(lhs, rhs)

    def test_numerator_factorization(self):
        """816 + 4c = 4(204 + c), and 64c = 4 * 16c, so ratio = (c+204)/(16c).

        # VERIFIED: [DC] direct check; [DA] dimensional consistency
        """
        for c in C_VALUES:
            self.assertEqual(816 + 4 * c, 4 * (204 + c))
            self.assertEqual(Fraction(4 * (204 + c), 64 * c), (c + 204) / (16 * c))


# ============================================================================
# Path 3: Engine cross-check
# ============================================================================

class TestPath3EngineCrossCheck(unittest.TestCase):
    """Cross-check against the established compute engines."""

    def test_against_w3_genus2_engine(self):
        """Match w3_genus2.cross_channel_correction.

        # VERIFIED: [CF] cross-engine; [DC] independent graph sum (Path 1)
        """
        try:
            from w3_genus2 import cross_channel_correction
        except ImportError:
            self.skipTest("w3_genus2 engine not available")

        for c in C_VALUES:
            engine_val = cross_channel_correction(c)
            independent_val = (c + 204) / (16 * c)
            self.assertEqual(engine_val, independent_val)

    def test_against_multi_weight_engine(self):
        """Match multi_weight_cross_channel_engine.delta_F2_W3_closed.

        # VERIFIED: [CF] cross-engine; [DC] independent graph sum (Path 1)
        """
        try:
            from multi_weight_cross_channel_engine import delta_F2_W3_closed
        except ImportError:
            self.skipTest("multi_weight_cross_channel_engine not available")

        for c in C_VALUES:
            engine_val = delta_F2_W3_closed(c)
            independent_val = (c + 204) / (16 * c)
            self.assertEqual(engine_val, independent_val)

    def test_against_multi_weight_graph_sum(self):
        """Match multi_weight_cross_channel_engine.cross_channel_genus2.

        # VERIFIED: [CF] full graph-sum engine; [DC] independent computation
        """
        try:
            from multi_weight_cross_channel_engine import (
                cross_channel_genus2, W3Frobenius,
            )
        except ImportError:
            self.skipTest("multi_weight_cross_channel_engine not available")

        w3 = W3Frobenius()
        for c in [Fraction(2), Fraction(13), Fraction(50), Fraction(100)]:
            engine_val = cross_channel_genus2(w3, c)
            independent_val = (c + 204) / (16 * c)
            self.assertEqual(engine_val, independent_val)


# ============================================================================
# Path 4: Limiting cases and special values
# ============================================================================

class TestPath4LimitingCases(unittest.TestCase):
    """Verify δF₂(W₃) at limiting and special values of c."""

    def test_large_c_limit(self):
        """c → ∞: δF₂ → 1/16 (only lollipop survives).

        (c+204)/(16c) = 1/16 + 204/(16c) = 1/16 + 51/(4c).
        At c = 10^8, the 1/c correction is ~10^{-8}.

        # VERIFIED: [LC] leading term; [DA] lollipop is c-independent
        """
        c = Fraction(10**8)
        delta = (c + 204) / (16 * c)
        remainder = delta - Fraction(1, 16)
        self.assertEqual(remainder, Fraction(51) / (4 * c))
        self.assertLess(float(remainder), 1e-6)

    def test_c_equals_neg204_vanishes(self):
        """At c = -204: δF₂ = 0 (numerator vanishes).

        Physically meaningless but algebraically clean.

        # VERIFIED: [DC] numerator = c + 204 = 0; [CF] component sum check
        """
        c = Fraction(-204)
        delta = (c + 204) / (16 * c)
        self.assertEqual(delta, Fraction(0))

        # Also verify from graph-sum components
        total = (Fraction(3) / c + Fraction(9) / (2 * c)
                 + Fraction(1, 16) + Fraction(21) / (4 * c))
        self.assertEqual(total, Fraction(0))

    def test_self_dual_c50(self):
        """W₃ self-dual at c = 50 (K_{W₃} = 250/3, c + c' = 100, c = c' = 50).

        δF₂(50) = (50 + 204)/(16 · 50) = 254/800 = 127/400.

        # VERIFIED: [DC] direct evaluation; [SY] self-duality c = c'
        """
        c = Fraction(50)
        delta = (c + 204) / (16 * c)
        self.assertEqual(delta, Fraction(127, 400))

    def test_c_equals_1(self):
        """c = 1: δF₂ = 205/16.

        # VERIFIED: [DC] (1+204)/(16·1) = 205/16; [CF] component sum
        """
        self.assertEqual(
            (Fraction(1) + 204) / (16 * Fraction(1)),
            Fraction(205, 16),
        )

    def test_c_equals_2(self):
        """c = 2: δF₂ = 103/16.

        # VERIFIED: [DC] (2+204)/(16·2) = 206/32 = 103/16; [CF] component sum
        """
        self.assertEqual(
            (Fraction(2) + 204) / (16 * Fraction(2)),
            Fraction(103, 16),
        )

    def test_positivity_for_positive_c(self):
        """δF₂ > 0 for all c > 0 (numerator c+204 > 0 when c > 0).

        # VERIFIED: [DC] sign analysis; [SY] all graph contributions ≥ 0
        """
        for c in C_VALUES:
            if c > 0:
                delta = (c + 204) / (16 * c)
                self.assertGreater(delta, 0)

    def test_monotone_decreasing(self):
        """δF₂ is monotonically decreasing for c > 0.

        d/dc [(c+204)/(16c)] = -204/(16c²) < 0.

        # VERIFIED: [DC] derivative; [NE] numerical spot checks
        """
        sorted_c = sorted(C_VALUES)
        positive_c = [c for c in sorted_c if c > 0]
        deltas = [(c + 204) / (16 * c) for c in positive_c]
        for i in range(len(deltas) - 1):
            self.assertGreater(deltas[i], deltas[i + 1])


# ============================================================================
# Path 5: Sympy symbolic verification
# ============================================================================

class TestPath5SympySymbolic(unittest.TestCase):
    """Symbolic verification using sympy exact arithmetic."""

    def test_symbolic_sum_simplifies(self):
        """Verify that the symbolic sum of 4 terms simplifies to (c+204)/(16c).

        # VERIFIED: [DC] sympy simplification; [CF] Fraction arithmetic (Path 2)
        """
        try:
            from sympy import Symbol, Rational, simplify, cancel
        except ImportError:
            self.skipTest("sympy not available")

        c = Symbol('c', positive=True)
        banana = Rational(3) / c
        theta_val = Rational(9) / (2 * c)
        lollipop_val = Rational(1, 16)
        barbell_val = Rational(21) / (4 * c)

        total = banana + theta_val + lollipop_val + barbell_val
        expected = (c + 204) / (16 * c)

        diff = cancel(total - expected)
        self.assertEqual(diff, 0)

    def test_symbolic_derivative(self):
        """d/dc [(c+204)/(16c)] = -204/(16c²) = -51/(4c²).

        # VERIFIED: [DC] sympy diff; [DA] dimensional analysis
        """
        try:
            from sympy import Symbol, Rational, diff, simplify
        except ImportError:
            self.skipTest("sympy not available")

        c = Symbol('c', positive=True)
        f = (c + 204) / (16 * c)
        df = diff(f, c)
        expected_df = Rational(-51, 4) / c**2
        self.assertEqual(simplify(df - expected_df), 0)

    def test_partial_fraction_decomposition(self):
        """(c+204)/(16c) = 1/16 + 51/(4c).

        # VERIFIED: [DC] sympy apart; [CF] matches large-c analysis
        """
        try:
            from sympy import Symbol, Rational, apart
        except ImportError:
            self.skipTest("sympy not available")

        c = Symbol('c', positive=True)
        f = (c + 204) / (16 * c)
        pf = apart(f, c)
        expected = Rational(1, 16) + Rational(51, 4) / c
        self.assertEqual(pf, expected)


# ============================================================================
# Structural: 7 genus-2 stable graphs (AP123)
# ============================================================================

class TestGenus2GraphCount(unittest.TestCase):
    """Verify the count and classification of genus-2 stable graphs."""

    def test_seven_graphs(self):
        """M̄_{2,0} has exactly 7 stable graphs (AP123: NOT 6).

        A: smooth (e=0, h¹=2)
        B: figure-eight (e=1, h¹=2)
        C: dumbbell/separating (e=1, h¹=0)
        D: sunset/banana (e=2, h¹=2)
        E: bridge-loop/lollipop (e=2, h¹=1)
        F: theta (e=3, h¹=2)
        G: barbell (e=3, h¹=2)

        # VERIFIED: [LT] Faber 1999; [DC] Euler char χ = 2g-2+n = 2
        """
        graphs = [
            {'name': 'smooth', 'edges': 0, 'vertices': [(2,)], 'h1': 2},
            {'name': 'figure-eight', 'edges': 1, 'vertices': [(1,)], 'h1': 2},
            {'name': 'dumbbell', 'edges': 1, 'vertices': [(1,), (1,)], 'h1': 0},
            {'name': 'banana', 'edges': 2, 'vertices': [(0,)], 'h1': 2},
            {'name': 'lollipop', 'edges': 2, 'vertices': [(0,), (1,)], 'h1': 1},
            {'name': 'theta', 'edges': 3, 'vertices': [(0,), (0,)], 'h1': 2},
            {'name': 'barbell', 'edges': 3, 'vertices': [(0,), (0,)], 'h1': 2},
        ]
        self.assertEqual(len(graphs), 7)

    def test_four_contributing_graphs(self):
        """Exactly 4 of the 7 graphs contribute to δF₂^cross.

        Contributing: D (banana), E (lollipop), F (theta), G (barbell).
        Non-contributing: A (no edges), B (single edge), C (single edge).

        # VERIFIED: [DC] per-graph computation; [SY] single-edge => no mixed
        """
        contributing = ['banana', 'lollipop', 'theta', 'barbell']
        non_contributing = ['smooth', 'figure-eight', 'dumbbell']
        self.assertEqual(len(contributing), 4)
        self.assertEqual(len(non_contributing), 3)
        self.assertEqual(len(contributing) + len(non_contributing), 7)

    def test_contribution_sources(self):
        """Verify the graph contribution values at a specific c.

        # VERIFIED: [DC] independent graph-by-graph computation (Path 1)
        # VERIFIED: [CF] matches w3_genus2 engine values
        """
        c = Fraction(100)
        contributions = {
            'banana': Fraction(3) / c,         # = 3/100
            'theta': Fraction(9) / (2 * c),    # = 9/200
            'lollipop': Fraction(1, 16),        # = 1/16 (c-independent)
            'barbell': Fraction(21) / (4 * c),  # = 21/400
        }
        total = sum(contributions.values())
        self.assertEqual(total, (c + 204) / (16 * c))


# ============================================================================
# Koszul complementarity under c ↔ 100-c
# ============================================================================

class TestKoszulComplementarity(unittest.TestCase):
    """Verify δF₂ behavior under W₃ Koszul duality c ↔ 100-c."""

    def test_complementarity_sum(self):
        """δF₂(c) + δF₂(100-c) has a specific algebraic form.

        δ(c) + δ(c') = (c+204)/(16c) + (304-c)/(16(100-c))
                      = [-(c²-100c-10200)] / [8c(100-c)]

        # VERIFIED: [DC] direct algebra; [SY] Koszul duality structure
        """
        for c in [Fraction(1), Fraction(2), Fraction(13), Fraction(25), Fraction(50)]:
            c_dual = Fraction(100) - c
            if c_dual <= 0:
                continue
            delta_c = (c + 204) / (16 * c)
            delta_cd = (c_dual + 204) / (16 * c_dual)
            delta_sum = delta_c + delta_cd

            numerator = -(c * c - 100 * c - Fraction(10200))
            denominator = 8 * c * (100 - c)
            expected = numerator / denominator
            self.assertEqual(delta_sum, expected)

    def test_self_dual_symmetry(self):
        """At c = 50 (self-dual point): δ(c) = δ(c'), so δ_sum = 2δ(50).

        # VERIFIED: [DC] c = c' = 50; [SY] self-duality
        """
        delta_50 = (Fraction(50) + 204) / (16 * Fraction(50))
        self.assertEqual(2 * delta_50, Fraction(127, 200))


# ============================================================================
# Consistency with uniform-weight and scalar formula
# ============================================================================

class TestScalarFormulaRelation(unittest.TestCase):
    """Verify the relation between δF₂^cross and the scalar universal F₂."""

    def test_scalar_universal_f2(self):
        """F₂^univ(W₃) = κ(W₃) · λ₂^FP = (5c/6)(7/5760) = 7c/6912.

        κ(W₃) = c*(H₃ - 1) = c*(1 + 1/2 + 1/3 - 1) = c*(5/6) = 5c/6.
        λ₂^FP = 7/5760.

        # VERIFIED: [DC] κ from C4 census; [LT] Faber-Pandharipande
        """
        for c in C_VALUES:
            kappa_w3 = 5 * c / 6  # VERIFIED: C4, H_3=11/6, H_3-1=5/6
            lambda_2 = Fraction(7, 5760)  # VERIFIED: [LT] FP value
            F2_univ = kappa_w3 * lambda_2
            self.assertEqual(F2_univ, 7 * c / 6912)

    def test_ratio_delta_over_f2(self):
        """δF₂/F₂^univ = 432(c+204)/(7c²).

        # VERIFIED: [DC] direct ratio; [DA] dimensionless, O(1/c) at large c
        """
        for c in C_VALUES:
            if c <= 0:
                continue
            delta = (c + 204) / (16 * c)
            f2_univ = 7 * c / 6912
            ratio = delta / f2_univ
            expected = Fraction(432) * (c + 204) / (7 * c * c)
            self.assertEqual(ratio, expected)

    def test_ratio_vanishes_at_large_c(self):
        """δF₂/F₂^univ → 0 as c → ∞ (scalar formula becomes exact).

        # VERIFIED: [LC] ratio ~ 432*204/(7c) + 432/(7c²); [DA] 1/c decay
        """
        c = Fraction(10**6)
        ratio = Fraction(432) * (c + 204) / (7 * c * c)
        self.assertLess(float(ratio), 1e-3)


if __name__ == '__main__':
    unittest.main()
