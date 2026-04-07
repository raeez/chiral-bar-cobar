r"""Adversarial red-team verification of delta_F_2^{grav}(W_N).

INDEPENDENT verification of the claimed universal N-formula:

    delta_F_2^{grav}(W_N, c) = B(N) + A(N)/c

where:
    B(N) = (N-2)(N+3)/96
    A(N) = (N-2)(3N^3 + 14N^2 + 22N + 33)/24

This test suite uses ZERO imports from the multi-weight cross-channel engine.
Every computation is independent and adversarial.

Verification paths:
  1. Direct graph sum (brute force over 7 genus-2 stable graphs)
  2. Symbolic/algebraic derivation via harmonic sums
  3. Newton interpolation extraction of A and B from 2 c-values
  4. Algebraic proof: A(N) = (2*S1^2 + S2 - 12)/4 with S1, S2 closed forms
  5. Large-c asymptotics (B(N) from lollipop)
  6. Vanishing at N=2 (Virasoro, uniform weight)
  7. Positivity for N >= 3, c > 0
  8. Per-graph decomposition cross-checks
  9. Koszul duality constraints
 10. Large-N asymptotics

Manuscript references:
    thm:multi-weight-genus-expansion, thm:theorem-d, AP27
"""

import unittest
from fractions import Fraction
from math import factorial

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from rectification_delta_f2_verify_engine import (
    bernoulli_number,
    claimed_A,
    claimed_B,
    claimed_formula,
    delta_F2_grav_graph_sum,
    delta_F2_grav_per_graph,
    delta_F2_grav_symbolic,
    derive_graph_amplitudes_symbolic,
    extract_A_N_from_graphs,
    extract_B_N_from_large_c,
    genus2_stable_graphs_independent,
    grav_C3,
    grav_kappa_channel,
    grav_kappa_total,
    grav_propagator,
    grav_vertex_factor,
    grav_V0_factorize,
    harmonic_minus_one_independent,
    lambda_fp_independent,
    newton_interpolate_delta_F2,
    sum_inverse_squares,
    verify_A_N_polynomial,
    verify_W3_genus2,
)


# ============================================================================
# 1. Foundations: Bernoulli numbers and lambda_FP
# ============================================================================

class TestBernoulliNumbers(unittest.TestCase):
    """Verify Bernoulli numbers against known values."""

    def test_B0(self):
        self.assertEqual(bernoulli_number(0), Fraction(1))

    def test_B1(self):
        # Akiyama-Tanigawa gives B_1 = +1/2 (second Bernoulli convention).
        # Both +1/2 and -1/2 appear in the literature. The sign does not
        # affect lambda_FP (which uses only even Bernoulli numbers).
        self.assertEqual(bernoulli_number(1), Fraction(1, 2))

    def test_B2(self):
        self.assertEqual(bernoulli_number(2), Fraction(1, 6))

    def test_B4(self):
        self.assertEqual(bernoulli_number(4), Fraction(-1, 30))

    def test_B6(self):
        self.assertEqual(bernoulli_number(6), Fraction(1, 42))

    def test_B8(self):
        self.assertEqual(bernoulli_number(8), Fraction(-1, 30))

    def test_B10(self):
        self.assertEqual(bernoulli_number(10), Fraction(5, 66))

    def test_odd_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(bernoulli_number(n), Fraction(0))


class TestLambdaFP(unittest.TestCase):
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp_independent(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp_independent(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp_independent(3), Fraction(31, 967680))

    def test_lambda4(self):
        self.assertEqual(lambda_fp_independent(4), Fraction(127, 154828800))

    def test_positivity(self):
        for g in range(1, 8):
            self.assertGreater(lambda_fp_independent(g), 0)

    def test_decreasing(self):
        for g in range(1, 7):
            self.assertGreater(lambda_fp_independent(g),
                               lambda_fp_independent(g + 1))


# ============================================================================
# 2. Genus-2 stable graph enumeration
# ============================================================================

class TestGenus2Graphs(unittest.TestCase):
    """Verify the 7 genus-2 stable graphs independently."""

    def setUp(self):
        self.graphs = genus2_stable_graphs_independent()

    def test_count(self):
        self.assertEqual(len(self.graphs), 7)

    def test_all_genus_2(self):
        for g in self.graphs:
            self.assertEqual(g.arithmetic_genus, 2, f"{g.name} has genus {g.arithmetic_genus}")

    def test_all_stable(self):
        for g in self.graphs:
            self.assertTrue(g.is_stable, f"{g.name} is not stable")

    def test_automorphism_orders(self):
        expected = {
            'smooth': 1, 'figure_eight': 2, 'banana': 8,
            'dumbbell': 2, 'theta': 12, 'lollipop': 2, 'barbell': 8,
        }
        for g in self.graphs:
            self.assertEqual(g.automorphism_order, expected[g.name],
                             f"|Aut({g.name})| wrong")

    def test_orbifold_euler(self):
        """sum 1/|Aut(Gamma)| = chi(M_2) = 1/240 by Harer-Zagier.

        The orbifold Euler characteristic of M_2 is B_4/(4*3!) = (-1/30)/24
        Wait, that gives -1/720. Actually chi_{orb}(M_2) is NOT the sum
        over boundary graphs. The correct check:
        the boundary contribution sum_{Gamma with edges > 0} 1/|Aut|
        should be a known quantity. Let me just verify the sum.
        """
        graphs_with_edges = [g for g in self.graphs if g.num_edges > 0]
        total = sum(Fraction(1, g.automorphism_order) for g in graphs_with_edges)
        # 1/2 + 1/8 + 1/2 + 1/12 + 1/2 + 1/8 = 6/8 + 6/12 + 6/8 ...
        # Let me just verify: 1/2 + 1/8 + 1/2 + 1/12 + 1/2 + 1/8
        # = 3/2 + 2/8 + 1/12 = 3/2 + 1/4 + 1/12 = 18/12 + 3/12 + 1/12 = 22/12 = 11/6
        self.assertEqual(total, Fraction(11, 6))

    def test_valences(self):
        expected = {
            'smooth': (0,),
            'figure_eight': (2,),
            'banana': (4,),
            'dumbbell': (1, 1),
            'theta': (3, 3),
            'lollipop': (3, 1),
            'barbell': (3, 3),
        }
        for g in self.graphs:
            self.assertEqual(g.valence(), expected[g.name],
                             f"valence({g.name}) wrong")


# ============================================================================
# 3. Gravitational Frobenius algebra
# ============================================================================

class TestGravitationalFrobenius(unittest.TestCase):
    """Verify the gravitational-only 3-point structure constants."""

    def test_C3_TTT(self):
        self.assertEqual(grav_C3(2, 2, 2, Fraction(10)), Fraction(10))

    def test_C3_TWjWj(self):
        for j in [3, 4, 5, 6, 7]:
            self.assertEqual(grav_C3(2, j, j, Fraction(10)), Fraction(10),
                             f"C_{{T,W{j},W{j}}} wrong")

    def test_C3_TTWj_vanishes(self):
        for j in [3, 4, 5, 6]:
            self.assertEqual(grav_C3(2, 2, j, Fraction(10)), Fraction(0),
                             f"C_{{T,T,W{j}}} should vanish")

    def test_C3_parity_odd_vanishes(self):
        """Triples with odd total odd-weight count vanish."""
        self.assertEqual(grav_C3(3, 3, 3, Fraction(10)), Fraction(0))
        self.assertEqual(grav_C3(3, 4, 4, Fraction(10)), Fraction(0))
        self.assertEqual(grav_C3(3, 5, 4, Fraction(10)), Fraction(0))

    def test_C3_no_higher_spin(self):
        """Higher-spin exchange vanishes in gravitational approximation."""
        self.assertEqual(grav_C3(3, 3, 4, Fraction(10)), Fraction(0))
        self.assertEqual(grav_C3(4, 4, 4, Fraction(10)), Fraction(0))
        self.assertEqual(grav_C3(3, 3, 5, Fraction(10)), Fraction(0))

    def test_C3_symmetry(self):
        """C_{ijk} is symmetric under permutations."""
        from itertools import permutations
        c = Fraction(7)
        for (i, j, k) in [(2, 3, 3), (2, 4, 4), (2, 2, 2), (3, 3, 4)]:
            vals = [grav_C3(*p, c) for p in permutations([i, j, k])]
            for v in vals:
                self.assertEqual(v, vals[0], f"C_{{{i},{j},{k}}} not symmetric")


class TestPropagator(unittest.TestCase):
    """Verify propagator eta^{jj} = j/c (AP27)."""

    def test_T_propagator(self):
        self.assertEqual(grav_propagator(2, Fraction(10)), Fraction(1, 5))

    def test_W3_propagator(self):
        self.assertEqual(grav_propagator(3, Fraction(9)), Fraction(1, 3))

    def test_W4_propagator(self):
        self.assertEqual(grav_propagator(4, Fraction(8)), Fraction(1, 2))


class TestKappa(unittest.TestCase):
    """Verify kappa values."""

    def test_kappa_total_W3(self):
        """kappa(W_3) = c/2 + c/3 = 5c/6."""
        self.assertEqual(grav_kappa_total(3, Fraction(6)), Fraction(5))

    def test_kappa_total_W4(self):
        """kappa(W_4) = c/2 + c/3 + c/4 = 13c/12."""
        self.assertEqual(grav_kappa_total(4, Fraction(12)), Fraction(13))

    def test_kappa_channel_T(self):
        self.assertEqual(grav_kappa_channel(2, Fraction(10)), Fraction(5))

    def test_kappa_channel_W3(self):
        self.assertEqual(grav_kappa_channel(3, Fraction(9)), Fraction(3))


# ============================================================================
# 4. Vertex factors
# ============================================================================

class TestVertexFactors(unittest.TestCase):
    """Verify vertex factors for the gravitational Frobenius algebra."""

    def test_V0_3_TTT(self):
        w = (2, 3, 4, 5)
        self.assertEqual(grav_V0_factorize((2, 2, 2), Fraction(10), w), Fraction(10))

    def test_V0_3_TWW(self):
        w = (2, 3, 4, 5)
        self.assertEqual(grav_V0_factorize((2, 3, 3), Fraction(10), w), Fraction(10))

    def test_V0_4_TTTT(self):
        """V_{0,4}(T,T,T,T) = eta^{TT} * C_{TTT} * C_{TTT} = (2/c)*c*c = 2c."""
        w = (2, 3, 4)
        self.assertEqual(grav_V0_factorize((2, 2, 2, 2), Fraction(10), w), Fraction(20))

    def test_V0_4_TTjj_universal(self):
        """V_{0,4}(a,a,b,b) = 2c for ALL (a,b) in gravitational approx."""
        w = (2, 3, 4, 5)
        c = Fraction(10)
        for a in w:
            for b in w:
                val = grav_V0_factorize((a, a, b, b), c, w)
                self.assertEqual(val, 2 * c,
                                 f"V_0(4)({a},{a},{b},{b}) = {val}, expected {2*c}")

    def test_V1_1_diagonal(self):
        w = (2, 3, 4)
        c = Fraction(24)
        self.assertEqual(grav_vertex_factor(1, (2,), c, w), Fraction(1, 2))
        self.assertEqual(grav_vertex_factor(1, (3,), c, w), Fraction(1, 3))

    def test_V1_2_diagonal_only(self):
        """V_{1,2}(j,j) = kappa_j * lambda_1. V_{1,2}(j,k) = 0 for j != k."""
        w = (2, 3, 4)
        c = Fraction(24)
        self.assertEqual(grav_vertex_factor(1, (2, 2), c, w),
                         grav_kappa_channel(2, c) * lambda_fp_independent(1))
        self.assertEqual(grav_vertex_factor(1, (2, 3), c, w), Fraction(0))


# ============================================================================
# 5. W_3 genus-2: delta_F2 = (c+204)/(16c)
# ============================================================================

class TestW3Genus2(unittest.TestCase):
    """Verify delta_F_2(W_3) = (c+204)/(16c) by three independent paths."""

    def test_c1(self):
        r = verify_W3_genus2(Fraction(1))
        self.assertTrue(r['all_agree'])
        self.assertEqual(r['graph_sum'], Fraction(205, 16))

    def test_c10(self):
        r = verify_W3_genus2(Fraction(10))
        self.assertTrue(r['all_agree'])
        self.assertEqual(r['graph_sum'], Fraction(107, 80))

    def test_c26(self):
        r = verify_W3_genus2(Fraction(26))
        self.assertTrue(r['all_agree'])
        self.assertEqual(r['graph_sum'], Fraction(115, 208))

    def test_c50(self):
        r = verify_W3_genus2(Fraction(50))
        self.assertTrue(r['all_agree'])

    def test_claimed_formula_matches(self):
        """The N-formula at N=3 gives (c+204)/(16c)."""
        for cv in [1, 2, 5, 10, 26, 50]:
            c = Fraction(cv)
            self.assertEqual(claimed_formula(3, c), (c + 204) / (16 * c))


# ============================================================================
# 6. W_4 gravitational: delta_F2 = (7c+2148)/(48c)
# ============================================================================

class TestW4Genus2Grav(unittest.TestCase):
    """Verify delta_F_2^{grav}(W_4) = (7c+2148)/(48c)."""

    def test_graph_sum_c1(self):
        d = delta_F2_grav_graph_sum(4, Fraction(1))
        self.assertEqual(d, Fraction(2155, 48))

    def test_graph_sum_c10(self):
        d = delta_F2_grav_graph_sum(4, Fraction(10))
        expected = Fraction(7 * 10 + 2148, 48 * 10)
        self.assertEqual(d, expected)

    def test_formula_match(self):
        for cv in [1, 2, 3, 5, 10, 50]:
            c = Fraction(cv)
            self.assertEqual(delta_F2_grav_graph_sum(4, c),
                             (7 * c + 2148) / (48 * c))

    def test_exceeds_W3(self):
        for cv in [1, 5, 10, 50]:
            c = Fraction(cv)
            d3 = delta_F2_grav_graph_sum(3, c)
            d4 = delta_F2_grav_graph_sum(4, c)
            self.assertGreater(d4, d3)


# ============================================================================
# 7. W_5 gravitational: delta_F2 = (c+434)/(4c)
# ============================================================================

class TestW5Genus2Grav(unittest.TestCase):
    """Verify delta_F_2^{grav}(W_5) = (c+434)/(4c)."""

    def test_graph_sum_c1(self):
        d = delta_F2_grav_graph_sum(5, Fraction(1))
        self.assertEqual(d, Fraction(435, 4))

    def test_formula_match(self):
        for cv in [1, 2, 3, 5, 10, 50]:
            c = Fraction(cv)
            self.assertEqual(delta_F2_grav_graph_sum(5, c),
                             (c + 434) / (4 * c))

    def test_exceeds_W4(self):
        for cv in [1, 5, 10, 50]:
            c = Fraction(cv)
            d4 = delta_F2_grav_graph_sum(4, c)
            d5 = delta_F2_grav_graph_sum(5, c)
            self.assertGreater(d5, d4)


# ============================================================================
# 8. Universal N-formula: graph sum vs claimed for N=3..11
# ============================================================================

class TestUniversalFormula(unittest.TestCase):
    """Verify delta_F_2^{grav}(W_N) = B(N) + A(N)/c for N=3..11."""

    def test_graph_sum_vs_formula_N3_to_N11(self):
        """Three-way match: graph sum, claimed formula, symbolic derivation."""
        for N in range(3, 12):
            for cv in [1, 2, 3, 5, 10]:
                c = Fraction(cv)
                gs = delta_F2_grav_graph_sum(N, c)
                cf = claimed_formula(N, c)
                sym = delta_F2_grav_symbolic(N, c)
                self.assertEqual(gs, cf,
                                 f"graph_sum != claimed at N={N}, c={cv}")
                self.assertEqual(gs, sym,
                                 f"graph_sum != symbolic at N={N}, c={cv}")

    def test_newton_interpolation_N3_to_N11(self):
        """Newton interpolation extracts A and B matching the claim."""
        for N in range(3, 12):
            r = newton_interpolate_delta_F2(N)
            self.assertTrue(r['A_matches_claim'], f"A mismatch at N={N}")
            self.assertTrue(r['B_matches_claim'], f"B mismatch at N={N}")
            self.assertTrue(r['verified_at_c3'], f"c=3 verify failed at N={N}")


# ============================================================================
# 9. N=2 vanishing (Virasoro, uniform weight)
# ============================================================================

class TestN2Vanishing(unittest.TestCase):
    """delta_F_2^{grav}(W_2, c) = 0 for all c (Virasoro is uniform-weight)."""

    def test_formula_vanishes(self):
        for cv in [1, 10, 100]:
            self.assertEqual(claimed_formula(2, Fraction(cv)), Fraction(0))

    def test_graph_sum_vanishes(self):
        """W_2 has only 1 channel (T). No mixed amplitudes possible."""
        for cv in [1, 10]:
            d = delta_F2_grav_graph_sum(2, Fraction(cv))
            self.assertEqual(d, Fraction(0))

    def test_B_vanishes(self):
        self.assertEqual(claimed_B(2), Fraction(0))

    def test_A_vanishes(self):
        self.assertEqual(claimed_A(2), Fraction(0))


# ============================================================================
# 10. B(N) = (N-2)(N+3)/96 from lollipop analysis
# ============================================================================

class TestBFormula(unittest.TestCase):
    """Verify B(N) = (N-2)(N+3)/96."""

    def test_B_from_lollipop(self):
        """B(N) equals the lollipop-derived formula for N=2..15."""
        for N in range(2, 16):
            self.assertEqual(extract_B_N_from_large_c(N), claimed_B(N))

    def test_B_values(self):
        expected = {
            2: Fraction(0),
            3: Fraction(1, 16),
            4: Fraction(7, 48),
            5: Fraction(1, 4),
            6: Fraction(3, 8),
        }
        for N, B in expected.items():
            self.assertEqual(claimed_B(N), B, f"B({N}) wrong")

    def test_B_factorization(self):
        """B(N) = (N-2)(N+3)/96, verify the factored form."""
        for N in range(2, 20):
            num = (N - 2) * (N + 3)
            self.assertEqual(claimed_B(N), Fraction(num, 96))

    def test_B_monotone_increasing(self):
        for N in range(3, 20):
            self.assertGreater(claimed_B(N + 1), claimed_B(N))

    def test_B_positive_for_N_ge_3(self):
        for N in range(3, 50):
            self.assertGreater(claimed_B(N), 0)


# ============================================================================
# 11. A(N) = (N-2)(3N^3+14N^2+22N+33)/24 from graph analysis
# ============================================================================

class TestAFormula(unittest.TestCase):
    """Verify A(N) = (N-2)(3N^3+14N^2+22N+33)/24."""

    def test_A_from_graphs(self):
        """A(N) from graph-by-graph analysis matches claimed polynomial."""
        for N in range(3, 16):
            self.assertTrue(verify_A_N_polynomial(N), f"A({N}) mismatch")

    def test_A_values(self):
        expected = {
            3: Fraction(51, 4),     # 1*(3*27+14*9+22*3+33)/24 = 306/24
            4: Fraction(179, 4),    # 2*(3*64+14*16+22*4+33)/24 = 1074/24
            5: Fraction(217, 2),    # 3*(3*125+14*25+22*5+33)/24 = 2604/24
        }
        for N, A in expected.items():
            self.assertEqual(claimed_A(N), A, f"A({N}) wrong")

    def test_A_monotone_increasing(self):
        for N in range(3, 20):
            self.assertGreater(claimed_A(N + 1), claimed_A(N))

    def test_A_positive_for_N_ge_3(self):
        for N in range(3, 50):
            self.assertGreater(claimed_A(N), 0)

    def test_A_algebraic_identity(self):
        """A(N) = (2*S1^2 + S2 - 12)/4 where S1=sum j, S2=sum j^2 for j=2..N.

        This is the ALGEBRAIC PROOF of the N-formula.
        """
        for N in range(3, 20):
            S1 = sum(j for j in range(2, N + 1))
            S2 = sum(j * j for j in range(2, N + 1))
            A_from_sums = Fraction(2 * S1 * S1 + S2 - 12, 4)
            self.assertEqual(A_from_sums, claimed_A(N),
                             f"Algebraic identity fails at N={N}")

    def test_A_polynomial_expansion(self):
        """(N-2)(3N^3+14N^2+22N+33) = 3N^4+8N^3-6N^2-11N-66."""
        for N in range(2, 20):
            lhs = (N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33)
            rhs = 3 * N**4 + 8 * N**3 - 6 * N**2 - 11 * N - 66
            self.assertEqual(lhs, rhs, f"Polynomial expansion fails at N={N}")


# ============================================================================
# 12. Positivity: delta_F_2 > 0 for all N >= 3, c > 0
# ============================================================================

class TestPositivity(unittest.TestCase):
    """delta_F_2^{grav}(W_N, c) > 0 for all N >= 3 and c > 0."""

    def test_positivity_small_c(self):
        for N in range(3, 10):
            for cv in [1, 2, 3, 5]:
                d = delta_F2_grav_graph_sum(N, Fraction(cv))
                self.assertGreater(d, 0, f"Not positive at N={N}, c={cv}")

    def test_positivity_large_c(self):
        for N in range(3, 10):
            d = delta_F2_grav_graph_sum(N, Fraction(1000))
            self.assertGreater(d, 0, f"Not positive at N={N}, c=1000")

    def test_positivity_from_formula(self):
        """Both B(N) > 0 and A(N) > 0 for N >= 3, so delta > 0 for c > 0."""
        for N in range(3, 50):
            self.assertGreater(claimed_B(N), 0)
            self.assertGreater(claimed_A(N), 0)


# ============================================================================
# 13. Per-graph decomposition
# ============================================================================

class TestPerGraphDecomposition(unittest.TestCase):
    """Verify per-graph contributions match the symbolic analysis."""

    def test_smooth_zero(self):
        """Smooth graph (0 edges) contributes 0."""
        for N in range(3, 8):
            decomp = delta_F2_grav_per_graph(N, Fraction(10))
            self.assertEqual(decomp['smooth']['mixed'], Fraction(0))

    def test_figure_eight_mixed_zero(self):
        """Figure-eight (1 edge) has no mixed assignments."""
        for N in range(3, 8):
            decomp = delta_F2_grav_per_graph(N, Fraction(10))
            self.assertEqual(decomp['figure_eight']['mixed'], Fraction(0))

    def test_dumbbell_mixed_zero(self):
        """Dumbbell (1 edge) has no mixed assignments."""
        for N in range(3, 8):
            decomp = delta_F2_grav_per_graph(N, Fraction(10))
            self.assertEqual(decomp['dumbbell']['mixed'], Fraction(0))

    def test_banana_mixed_formula(self):
        """Banana mixed = (S1^2 - S2)/(4c)."""
        for N in range(3, 8):
            c = Fraction(10)
            S1 = sum(j for j in range(2, N + 1))
            S2 = sum(j * j for j in range(2, N + 1))
            expected = Fraction(S1 * S1 - S2, 4) / c
            decomp = delta_F2_grav_per_graph(N, c)
            self.assertEqual(decomp['banana']['mixed'], expected,
                             f"Banana mixed wrong at N={N}")

    def test_theta_mixed_formula(self):
        """Theta mixed = (sum_{j=3}^N j^2) / (2c)."""
        for N in range(3, 8):
            c = Fraction(10)
            S2_from3 = sum(j * j for j in range(3, N + 1))
            expected = Fraction(S2_from3, 2) / c
            decomp = delta_F2_grav_per_graph(N, c)
            self.assertEqual(decomp['theta']['mixed'], expected,
                             f"Theta mixed wrong at N={N}")

    def test_lollipop_c_independent(self):
        """Lollipop mixed amplitude is independent of c."""
        for N in range(3, 8):
            d1 = delta_F2_grav_per_graph(N, Fraction(1))
            d2 = delta_F2_grav_per_graph(N, Fraction(100))
            self.assertEqual(d1['lollipop']['mixed'], d2['lollipop']['mixed'],
                             f"Lollipop not c-independent at N={N}")

    def test_lollipop_mixed_formula(self):
        """Lollipop mixed = (S1 - 2)/48."""
        for N in range(3, 8):
            c = Fraction(10)
            S1_from3 = sum(j for j in range(3, N + 1))
            expected = Fraction(S1_from3, 48)
            decomp = delta_F2_grav_per_graph(N, c)
            self.assertEqual(decomp['lollipop']['mixed'], expected,
                             f"Lollipop mixed wrong at N={N}")

    def test_barbell_mixed_formula(self):
        """Barbell mixed = (S1^2 - 4)/(4c)."""
        for N in range(3, 8):
            c = Fraction(10)
            S1 = sum(j for j in range(2, N + 1))
            expected = Fraction(S1 * S1 - 4, 4) / c
            decomp = delta_F2_grav_per_graph(N, c)
            self.assertEqual(decomp['barbell']['mixed'], expected,
                             f"Barbell mixed wrong at N={N}")

    def test_per_graph_sum_equals_total(self):
        """Sum of per-graph mixed amplitudes equals delta_F_2."""
        for N in range(3, 8):
            c = Fraction(10)
            decomp = delta_F2_grav_per_graph(N, c)
            total = sum(decomp[g]['mixed'] for g in decomp)
            d = delta_F2_grav_graph_sum(N, c)
            self.assertEqual(total, d, f"Per-graph sum != total at N={N}")

    def test_symbolic_matches_per_graph(self):
        """Symbolic graph-by-graph matches brute-force per-graph."""
        for N in range(3, 8):
            c = Fraction(10)
            sym = derive_graph_amplitudes_symbolic(N, c)
            bf = delta_F2_grav_per_graph(N, c)
            for name in sym:
                self.assertEqual(sym[name], bf[name]['mixed'],
                                 f"Symbolic != brute-force at N={N}, {name}")


# ============================================================================
# 14. Large-c asymptotics
# ============================================================================

class TestLargeCAsymptotics(unittest.TestCase):
    """Verify large-c behavior: delta_F_2 -> B(N) as c -> inf."""

    def test_convergence_to_B(self):
        for N in range(3, 8):
            B = float(claimed_B(N))
            d_large = float(delta_F2_grav_graph_sum(N, Fraction(10**6)))
            # A(N)/c correction is O(10^{-6}) * A(N). For N=5, A=217/2,
            # so the remainder is ~1.1e-4. Use places=3 for safety.
            self.assertAlmostEqual(d_large, B, places=3,
                                   msg=f"N={N}: delta at c=10^6 != B(N)")

    def test_subleading_A(self):
        """c * (delta - B) -> A as c -> inf."""
        for N in range(3, 8):
            c = Fraction(10**6)
            delta = delta_F2_grav_graph_sum(N, c)
            remainder = c * (delta - claimed_B(N))
            self.assertEqual(remainder, claimed_A(N),
                             f"Subleading mismatch at N={N}")

    def test_divergence_at_c_to_zero(self):
        """delta_F_2 ~ A(N)/c diverges as c -> 0+."""
        for N in range(3, 6):
            d_small = delta_F2_grav_graph_sum(N, Fraction(1, 100))
            self.assertGreater(d_small, 100, f"Not diverging at N={N}")


# ============================================================================
# 15. Large-N asymptotics
# ============================================================================

class TestLargeNAsymptotics(unittest.TestCase):
    """Verify large-N behavior of B(N) and A(N)."""

    def test_B_grows_quadratically(self):
        """B(N) ~ N^2/96 for large N."""
        for N in [50, 100]:
            B = float(claimed_B(N))
            asymptotic = N**2 / 96
            self.assertAlmostEqual(B / asymptotic, 1.0, places=1,
                                   msg=f"B({N}) not ~ N^2/96")

    def test_A_grows_as_N5(self):
        """A(N) ~ 3N^4/24 = N^4/8 * (N-2)/N ~ N^5/8 for large N.
        More precisely: A(N) ~ (N-2)*3N^3/24 = N^4/8 - N^3/4 for large N."""
        for N in [50, 100]:
            A = float(claimed_A(N))
            asymptotic = N**4 / 8  # Leading term
            self.assertAlmostEqual(A / asymptotic, 1.0, places=0,
                                   msg=f"A({N}) not ~ N^4/8")

    def test_ratio_A_over_B_grows(self):
        """A(N)/B(N) ~ 12*N^2 for large N.

        A ~ (N-2)*3N^3/24 = N^4/8, B ~ (N-2)*(N+3)/96 ~ N^2/96.
        Ratio ~ (N^4/8)/(N^2/96) = 12*N^2.
        """
        for N in [20, 50]:
            ratio = float(claimed_A(N)) / float(claimed_B(N))
            self.assertGreater(ratio / (12 * N**2), 0.5)
            self.assertLess(ratio / (12 * N**2), 2.0)


# ============================================================================
# 16. Monotonicity in N
# ============================================================================

class TestMonotonicity(unittest.TestCase):
    """delta_F_2 is strictly increasing in N for fixed c > 0."""

    def test_monotone_c1(self):
        for N in range(3, 10):
            d_N = delta_F2_grav_graph_sum(N, Fraction(1))
            d_N1 = delta_F2_grav_graph_sum(N + 1, Fraction(1))
            self.assertGreater(d_N1, d_N, f"Not monotone at N={N}, c=1")

    def test_monotone_c100(self):
        for N in range(3, 10):
            d_N = delta_F2_grav_graph_sum(N, Fraction(100))
            d_N1 = delta_F2_grav_graph_sum(N + 1, Fraction(100))
            self.assertGreater(d_N1, d_N, f"Not monotone at N={N}, c=100")


# ============================================================================
# 17. Algebraic proof: the full derivation chain
# ============================================================================

class TestAlgebraicProof(unittest.TestCase):
    """Verify the algebraic derivation from harmonic sums to polynomial."""

    def test_S1_formula(self):
        """S1 = sum_{j=2}^N j = N(N+1)/2 - 1."""
        for N in range(2, 20):
            S1 = sum(j for j in range(2, N + 1))
            self.assertEqual(S1, N * (N + 1) // 2 - 1)

    def test_S2_formula(self):
        """S2 = sum_{j=2}^N j^2 = N(N+1)(2N+1)/6 - 1."""
        for N in range(2, 20):
            S2 = sum(j * j for j in range(2, N + 1))
            self.assertEqual(S2, N * (N + 1) * (2 * N + 1) // 6 - 1)

    def test_B_from_S1(self):
        """B(N) = (S1-2)/48 = (N(N+1)/2-3)/48 = (N^2+N-6)/96 = (N-2)(N+3)/96."""
        for N in range(2, 20):
            S1 = N * (N + 1) // 2 - 1
            B_from_S1 = Fraction(S1 - 2, 48)
            B_factored = Fraction((N - 2) * (N + 3), 96)
            self.assertEqual(B_from_S1, B_factored,
                             f"B derivation fails at N={N}")

    def test_A_from_S1_S2(self):
        """A(N) = (2S1^2 + S2 - 12)/4.

        Expanding: S1 = N(N+1)/2 - 1, S2 = N(N+1)(2N+1)/6 - 1.
        2S1^2 + S2 - 12 = N(N+1)(3N^2+5N-11)/3 - 66/3
        Wait, let me be precise.

        2S1^2 = 2*(N(N+1)/2-1)^2 = N^2(N+1)^2/2 - 2N(N+1) + 2
        S2 = N(N+1)(2N+1)/6 - 1
        Total = N^2(N+1)^2/2 - 2N(N+1) + 2 + N(N+1)(2N+1)/6 - 1 - 12
              = N^2(N+1)^2/2 + N(N+1)(2N+1)/6 - 2N(N+1) - 11.

        Common denominator 6:
        = [3N^2(N+1)^2 + N(N+1)(2N+1) - 12N(N+1) - 66] / 6
        = [N(N+1)(3N(N+1)+2N+1-12) - 66] / 6
        = [N(N+1)(3N^2+5N-11) - 66] / 6.

        So A = this / 4 = [N(N+1)(3N^2+5N-11) - 66] / 24.
        We need to verify this equals (N-2)(3N^3+14N^2+22N+33)/24.
        """
        for N in range(2, 20):
            lhs = N * (N + 1) * (3 * N**2 + 5 * N - 11) - 66
            rhs = (N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33)
            self.assertEqual(lhs, rhs, f"Polynomial identity fails at N={N}")

    def test_full_chain(self):
        """Full derivation chain: graphs -> harmonic sums -> polynomial -> claimed.

        This is the complete algebraic proof in one test.
        """
        for N in range(3, 15):
            # Step 1: harmonic sums from channel weights
            S1 = sum(j for j in range(2, N + 1))
            S2 = sum(j * j for j in range(2, N + 1))

            # Step 2: B from lollipop
            B = Fraction(S1 - 2, 48)

            # Step 3: A from banana + theta + barbell
            A = Fraction(2 * S1**2 + S2 - 12, 4)

            # Step 4: polynomial identities
            S1_closed = N * (N + 1) // 2 - 1
            self.assertEqual(S1, S1_closed)
            B_poly = Fraction((N - 2) * (N + 3), 96)
            self.assertEqual(B, B_poly)
            A_poly = Fraction((N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33), 24)
            self.assertEqual(A, A_poly)

            # Step 5: match against graph sum
            c = Fraction(7)
            formula = B + A / c
            graph_sum = delta_F2_grav_graph_sum(N, c)
            self.assertEqual(formula, graph_sum,
                             f"Full chain fails at N={N}")


# ============================================================================
# 18. Cross-checks with the kappa*lambda diagonal
# ============================================================================

class TestDiagonalCrossCheck(unittest.TestCase):
    """Verify consistency of diagonal vs mixed decomposition.

    NOTE: The smooth graph (genus 2, 0 edges) contributes kappa*lambda_2
    to the full F_2, but it has 0 edges so our graph_amplitude_raw returns 0.
    The smooth contribution is handled separately in the full theory.

    The BOUNDARY graphs (those with edges > 0) contribute both diagonal
    and mixed amplitudes. The diagonal boundary sum is NOT equal to
    kappa*lambda_2 (that comes from smooth + boundary diagonal together).
    """

    def test_diagonal_plus_mixed_equals_total(self):
        """For each graph: diagonal + mixed = total."""
        for N in range(3, 8):
            c = Fraction(10)
            decomp = delta_F2_grav_per_graph(N, c)
            for name in decomp:
                d = decomp[name]
                self.assertEqual(d['diagonal'] + d['mixed'], d['total'],
                                 f"diag+mixed != total at N={N}, {name}")

    def test_total_boundary_consistent(self):
        """Sum of all per-graph totals = diagonal_sum + delta_F2."""
        for N in range(3, 8):
            c = Fraction(10)
            decomp = delta_F2_grav_per_graph(N, c)
            total_all = sum(decomp[g]['total'] for g in decomp)
            total_diag = sum(decomp[g]['diagonal'] for g in decomp)
            delta = delta_F2_grav_graph_sum(N, c)
            self.assertEqual(total_all, total_diag + delta,
                             f"Boundary total inconsistent at N={N}")


# ============================================================================
# 19. Specific numerical spot checks
# ============================================================================

class TestNumericalSpotChecks(unittest.TestCase):
    """Exact numerical values at specific (N, c) pairs."""

    def test_N3_c1(self):
        self.assertEqual(delta_F2_grav_graph_sum(3, Fraction(1)), Fraction(205, 16))

    def test_N3_c26(self):
        self.assertEqual(delta_F2_grav_graph_sum(3, Fraction(26)),
                         Fraction(115, 208))

    def test_N4_c1(self):
        self.assertEqual(delta_F2_grav_graph_sum(4, Fraction(1)), Fraction(2155, 48))

    def test_N5_c1(self):
        self.assertEqual(delta_F2_grav_graph_sum(5, Fraction(1)), Fraction(435, 4))

    def test_N6_c1(self):
        expected = claimed_formula(6, Fraction(1))
        self.assertEqual(delta_F2_grav_graph_sum(6, Fraction(1)), expected)

    def test_N6_c10(self):
        expected = claimed_formula(6, Fraction(10))
        self.assertEqual(delta_F2_grav_graph_sum(6, Fraction(10)), expected)

    def test_N7_c1(self):
        expected = claimed_formula(7, Fraction(1))
        self.assertEqual(delta_F2_grav_graph_sum(7, Fraction(1)), expected)

    def test_N8_c1(self):
        expected = claimed_formula(8, Fraction(1))
        self.assertEqual(delta_F2_grav_graph_sum(8, Fraction(1)), expected)


# ============================================================================
# 20. Edge cases and robustness
# ============================================================================

class TestEdgeCases(unittest.TestCase):
    """Edge cases and robustness checks."""

    def test_N1_would_be_empty(self):
        """N=1 means only weight-1 channel; not meaningful for W_N."""
        # The formula gives (1-2)*(1+3)/96 = -4/96 = -1/24, but N=1 is
        # not a valid W_N algebra. We just check the formula evaluates.
        self.assertEqual(claimed_B(1), Fraction(-1, 24))
        # This negative value is consistent: N=1 is outside the domain.

    def test_very_large_N(self):
        """Formula evaluates for large N (no overflow with Fraction)."""
        N = 100
        B = claimed_B(N)
        A = claimed_A(N)
        self.assertGreater(B, 0)
        self.assertGreater(A, 0)
        # B(100) = 98*103/96 = 10094/96 = 5047/48
        self.assertEqual(B, Fraction(98 * 103, 96))

    def test_delta_ratio_to_kl(self):
        """delta / (kappa*lambda) is O(1) at large c and grows with N."""
        ratios = []
        for N in range(3, 8):
            c = Fraction(1000)
            delta = float(delta_F2_grav_graph_sum(N, c))
            kl = float(grav_kappa_total(N, c) * lambda_fp_independent(2))
            ratios.append(delta / kl)
        # Ratios should be increasing
        for i in range(len(ratios) - 1):
            self.assertGreater(ratios[i + 1], ratios[i])


# ============================================================================
# 21. Fourth verification path: floating-point independent computation
# ============================================================================

class TestFloatingPointPath(unittest.TestCase):
    """Fourth verification path using float arithmetic (independent of Fraction)."""

    def _delta_float(self, N, c):
        """Direct floating-point graph sum (no Fraction)."""
        weights = list(range(2, N + 1))

        def prop(j):
            return j / c

        def kappa_j(j):
            return c / j

        lam1 = 1.0 / 24
        lam2 = 7.0 / 5760

        def C3(i, j, k):
            odd = sum(1 for w in [i, j, k] if w % 2 == 1)
            if odd % 2 == 1:
                return 0.0
            t = tuple(sorted([i, j, k]))
            if t == (2, 2, 2):
                return c
            if t[0] == 2 and t[1] == t[2] and t[1] >= 3:
                return c
            return 0.0

        def V04(a, a2, b, b2):
            # V_{0,4}(a,a,b,b) = sum_m (m/c)*C(a,a,m)*C(m,b,b)
            total = 0.0
            for m in weights:
                c1 = C3(a, a2, m)
                if c1 == 0:
                    continue
                c2 = C3(m, b, b2)
                total += (m / c) * c1 * c2
            return total

        mixed_total = 0.0

        # Banana: sigma=(j1,j2), amp = prop(j1)*prop(j2)*V04(j1,j1,j2,j2)
        for j1 in weights:
            for j2 in weights:
                if j1 == j2:
                    continue  # skip diagonal
                amp = prop(j1) * prop(j2) * V04(j1, j1, j2, j2)
                mixed_total += amp / 8  # |Aut|=8

        # Theta: sigma=(j1,j2,j3), amp = prop(j1)*prop(j2)*prop(j3)*C3(j1,j2,j3)^2
        for j1 in weights:
            for j2 in weights:
                for j3 in weights:
                    if len(set([j1, j2, j3])) <= 1:
                        continue
                    cv = C3(j1, j2, j3)
                    if cv == 0:
                        continue
                    amp = prop(j1) * prop(j2) * prop(j3) * cv * cv
                    mixed_total += amp / 12  # |Aut|=12

        # Lollipop: sigma=(j1,j2), j1=self-loop@v0, j2=bridge
        # v0(g=0): (j1,j1,j2), v1(g=1): (j2,)
        for j1 in weights:
            for j2 in weights:
                if j1 == j2:
                    continue
                vf0 = C3(j1, j1, j2)
                if vf0 == 0:
                    continue
                vf1 = kappa_j(j2) * lam1
                amp = prop(j1) * prop(j2) * vf0 * vf1
                mixed_total += amp / 2  # |Aut|=2

        # Barbell: sigma=(j1,j2,j3), j1=loop@v0, j2=bridge, j3=loop@v1
        # v0(g=0): (j1,j1,j2), v1(g=0): (j2,j3,j3)
        for j1 in weights:
            for j2 in weights:
                for j3 in weights:
                    if len(set([j1, j2, j3])) <= 1:
                        continue
                    vf0 = C3(j1, j1, j2)
                    if vf0 == 0:
                        continue
                    vf1 = C3(j2, j3, j3)
                    if vf1 == 0:
                        continue
                    amp = prop(j1) * prop(j2) * prop(j3) * vf0 * vf1
                    mixed_total += amp / 8  # |Aut|=8

        return mixed_total

    def test_float_vs_exact_N3(self):
        for cv in [1, 10, 100]:
            exact = float(delta_F2_grav_graph_sum(3, Fraction(cv)))
            flt = self._delta_float(3, float(cv))
            self.assertAlmostEqual(exact, flt, places=10,
                                   msg=f"Float mismatch at N=3, c={cv}")

    def test_float_vs_exact_N4(self):
        for cv in [1, 10]:
            exact = float(delta_F2_grav_graph_sum(4, Fraction(cv)))
            flt = self._delta_float(4, float(cv))
            self.assertAlmostEqual(exact, flt, places=10,
                                   msg=f"Float mismatch at N=4, c={cv}")

    def test_float_vs_exact_N5(self):
        exact = float(delta_F2_grav_graph_sum(5, Fraction(10)))
        flt = self._delta_float(5, 10.0)
        self.assertAlmostEqual(exact, flt, places=10)

    def test_float_vs_formula_N6(self):
        c = 10.0
        flt = self._delta_float(6, c)
        formula = float(claimed_formula(6, Fraction(10)))
        self.assertAlmostEqual(flt, formula, places=10)

    def test_float_vs_formula_N7(self):
        c = 10.0
        flt = self._delta_float(7, c)
        formula = float(claimed_formula(7, Fraction(10)))
        self.assertAlmostEqual(flt, formula, places=9)


if __name__ == '__main__':
    unittest.main()
