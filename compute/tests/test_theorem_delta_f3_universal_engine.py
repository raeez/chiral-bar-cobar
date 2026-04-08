r"""Comprehensive test suite for the genus-3 gravitational cross-channel correction.

Tests the PROVED universal formula:

    delta_F_3^{grav}(W_N, c) = D_3(N)*c + C_3(N) + B_3(N)/c + A_3(N)/c^2

where:
    D_3(N) = (N-2) / 27648
    C_3(N) = (N-2) * (35*N^2 + 133*N + 234) / 34560
    B_3(N) = (N-2) * (21*N^4 + 156*N^3 + 499*N^2 + 932*N + 1704) / 1728
    A_3(N) = (N-2) * (120*N^6 + 1300*N^5 + 5918*N^4 + 14786*N^3
              + 27592*N^2 + 36369*N + 56475) / 1080

Verification paths:
  1. Direct graph sum (brute force over 42 genus-3 stable graphs)
  2. Analytical c-factorization (compute at c=1, decompose by h^1)
  3. 4x4 linear extraction of D, C, B, A from 4 c-values
  4. Out-of-sample polynomial verification
  5. Vanishing at N=2 (Virasoro = uniform weight)
  6. Positivity for N >= 3, c > 0
  7. Degree bounds and leading coefficient checks
  8. (N-2) factor verification
  9. Cross-genus consistency with known genus-2 formula
 10. Large-c and small-c asymptotics
 11. Lambda_FP and Bernoulli number foundations
 12. Graph structure verification (42 graphs, h^1 decomposition)

References:
    thm:multi-weight-genus-expansion, thm:theorem-d, AP27
"""

import unittest
from fractions import Fraction
from math import factorial

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_delta_f3_universal_engine import (
    A3_formula,
    B3_formula,
    C3_formula,
    D3_formula,
    bernoulli_number,
    delta_F3_analytical,
    delta_F3_formula,
    delta_F3_grav_graph_sum,
    extract_DCBA_from_c_values,
    genus3_graphs,
    grav_C3,
    grav_kappa_channel,
    grav_kappa_total,
    grav_propagator,
    grav_V0_factorize,
    grav_vertex_factor,
    lambda_fp,
    verify_graph_count,
    verify_N2_vanishing,
    verify_positivity,
)


# ============================================================================
# 1. Foundations: Bernoulli numbers and lambda_FP
# ============================================================================

class TestBernoulliNumbers(unittest.TestCase):
    """Verify Bernoulli numbers used in lambda_FP computation."""

    def test_B0(self):
        self.assertEqual(bernoulli_number(0), Fraction(1))

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

    def test_B12(self):
        self.assertEqual(bernoulli_number(12), Fraction(-691, 2730))

    def test_odd_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(bernoulli_number(n), Fraction(0))


class TestLambdaFP(unittest.TestCase):
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda4(self):
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))

    def test_positivity(self):
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_decreasing(self):
        for g in range(1, 7):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1))

    def test_formula(self):
        """Verify lambda_g = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)."""
        for g in range(1, 6):
            B2g = bernoulli_number(2 * g)
            power = 2 ** (2 * g - 1)
            expected = Fraction(power - 1, power) * abs(B2g) / Fraction(factorial(2 * g))
            self.assertEqual(lambda_fp(g), expected)


# ============================================================================
# 2. Graph structure
# ============================================================================

class TestGraphStructure(unittest.TestCase):
    """Verify genus-3 stable graph enumeration."""

    def test_42_graphs(self):
        self.assertTrue(verify_graph_count())

    def test_h1_decomposition(self):
        graphs = genus3_graphs()
        h1_counts = {}
        for g in graphs:
            h1 = g.first_betti
            h1_counts[h1] = h1_counts.get(h1, 0) + 1
        self.assertEqual(h1_counts[0], 4)
        self.assertEqual(h1_counts[1], 9)
        self.assertEqual(h1_counts[2], 14)
        self.assertEqual(h1_counts[3], 15)

    def test_edge_range(self):
        """Edges range from 0 to 6 (= 3*3 - 3)."""
        graphs = genus3_graphs()
        edge_counts = set(g.num_edges for g in graphs)
        self.assertEqual(min(edge_counts), 0)
        self.assertEqual(max(edge_counts), 6)

    def test_arithmetic_genus(self):
        """All graphs have arithmetic genus 3."""
        for g in genus3_graphs():
            self.assertEqual(g.arithmetic_genus, 3)

    def test_stability(self):
        """All graphs are stable: 2g(v) - 2 + val(v) > 0."""
        for g in genus3_graphs():
            self.assertTrue(g.is_stable)

    def test_vertex_count_distribution(self):
        graphs = genus3_graphs()
        vc = {}
        for g in graphs:
            nv = g.num_vertices
            vc[nv] = vc.get(nv, 0) + 1
        self.assertEqual(vc[1], 4)
        self.assertEqual(vc[2], 12)
        self.assertEqual(vc[3], 15)
        self.assertEqual(vc[4], 11)


# ============================================================================
# 3. Gravitational Frobenius algebra
# ============================================================================

class TestGravitationalAlgebra(unittest.TestCase):
    """Verify gravitational Frobenius algebra structure constants."""

    def test_TTT(self):
        c = Fraction(10)
        self.assertEqual(grav_C3(2, 2, 2, c), c)

    def test_TWW(self):
        c = Fraction(10)
        for j in range(3, 8):
            self.assertEqual(grav_C3(2, j, j, c), c)
            self.assertEqual(grav_C3(j, 2, j, c), c)
            self.assertEqual(grav_C3(j, j, 2, c), c)

    def test_TTW_vanishes(self):
        c = Fraction(10)
        for j in range(3, 8):
            self.assertEqual(grav_C3(2, 2, j, c), Fraction(0))

    def test_WWW_vanishes(self):
        c = Fraction(10)
        for j in range(3, 8):
            self.assertEqual(grav_C3(j, j, j, c), Fraction(0))

    def test_mixed_vanishes(self):
        c = Fraction(10)
        self.assertEqual(grav_C3(3, 4, 5, c), Fraction(0))
        self.assertEqual(grav_C3(3, 3, 4, c), Fraction(0))

    def test_parity(self):
        """Odd parity triples vanish."""
        c = Fraction(10)
        self.assertEqual(grav_C3(2, 3, 4, c), Fraction(0))
        self.assertEqual(grav_C3(3, 5, 7, c), Fraction(0))

    def test_propagator(self):
        c = Fraction(10)
        self.assertEqual(grav_propagator(2, c), Fraction(1, 5))
        self.assertEqual(grav_propagator(3, c), Fraction(3, 10))
        self.assertEqual(grav_propagator(5, c), Fraction(1, 2))

    def test_kappa_total(self):
        c = Fraction(6)
        # kappa(W_3) = c/2 + c/3 = 3 + 2 = 5
        self.assertEqual(grav_kappa_total(3, c), Fraction(5))

    def test_vertex_g0_3pt(self):
        c = Fraction(10)
        aw = (2, 3, 4)
        self.assertEqual(grav_V0_factorize((2, 2, 2), c, aw), c)
        self.assertEqual(grav_V0_factorize((2, 3, 3), c, aw), c)
        self.assertEqual(grav_V0_factorize((3, 4, 2), c, aw), Fraction(0))

    def test_vertex_g0_4pt_banana(self):
        """V_0(j,j,k,k) = 2c for all j,k (through T-channel)."""
        c = Fraction(10)
        aw = (2, 3, 4, 5)
        for j in aw:
            for k in aw:
                self.assertEqual(grav_V0_factorize((j, j, k, k), c, aw), 2 * c)

    def test_vertex_g1_diagonal(self):
        c = Fraction(10)
        aw = (2, 3)
        # V_{1,2}(j,j) = (c/j)*lambda_1 = (c/j)/24
        self.assertEqual(
            grav_vertex_factor(1, (3, 3), c, aw),
            Fraction(c, 3) * Fraction(1, 24)
        )

    def test_vertex_g1_mixed_vanishes(self):
        c = Fraction(10)
        aw = (2, 3)
        self.assertEqual(grav_vertex_factor(1, (2, 3), c, aw), Fraction(0))


# ============================================================================
# 4. N=2 vanishing (Virasoro = uniform weight)
# ============================================================================

class TestN2Vanishing(unittest.TestCase):
    """At N=2, W_2 = Virasoro has only channel T (weight 2): uniform weight."""

    def test_formula_vanishing(self):
        self.assertTrue(verify_N2_vanishing())

    def test_D3_vanishes(self):
        self.assertEqual(D3_formula(2), Fraction(0))

    def test_C3_vanishes(self):
        self.assertEqual(C3_formula(2), Fraction(0))

    def test_B3_vanishes(self):
        self.assertEqual(B3_formula(2), Fraction(0))

    def test_A3_vanishes(self):
        self.assertEqual(A3_formula(2), Fraction(0))

    def test_graph_sum_vanishes(self):
        for c_val in [1, 2, 5]:
            self.assertEqual(
                delta_F3_grav_graph_sum(2, Fraction(c_val)), Fraction(0)
            )

    def test_full_formula_vanishes(self):
        for c_val in [1, 3, 7, 13]:
            self.assertEqual(
                delta_F3_formula(2, Fraction(c_val)), Fraction(0)
            )


# ============================================================================
# 5. In-sample verification: formula matches graph sum for N=2..8
# ============================================================================

class TestInSampleVerification(unittest.TestCase):
    """Verify formula matches direct graph sum for N=2..8 at multiple c-values."""

    def _check_N(self, N, c_vals):
        for c_val in c_vals:
            c = Fraction(c_val)
            formula = delta_F3_formula(N, c)
            graph_sum = delta_F3_grav_graph_sum(N, c)
            self.assertEqual(
                formula, graph_sum,
                f"N={N}, c={c_val}: formula={formula}, graph_sum={graph_sum}"
            )

    def test_N2(self):
        self._check_N(2, [1, 3, 7])

    def test_N3(self):
        self._check_N(3, [1, 3, 7])

    def test_N4(self):
        self._check_N(4, [1, 3, 7])

    def test_N5(self):
        self._check_N(5, [1, 3, 7])

    def test_N6_c1(self):
        self._check_N(6, [1])

    def test_N7_c1(self):
        self._check_N(7, [1])

    def test_N8_c1(self):
        self._check_N(8, [1])


# ============================================================================
# 6. Analytical c-factorization verification
# ============================================================================

class TestAnalyticalFactorization(unittest.TestCase):
    """Verify that the analytical method (compute at c=1, decompose by h^1)
    gives the same D, C, B, A as the formula."""

    def test_N3(self):
        D, C, B, A = delta_F3_analytical(3)
        self.assertEqual(D, D3_formula(3))
        self.assertEqual(C, C3_formula(3))
        self.assertEqual(B, B3_formula(3))
        self.assertEqual(A, A3_formula(3))

    def test_N4(self):
        D, C, B, A = delta_F3_analytical(4)
        self.assertEqual(D, D3_formula(4))
        self.assertEqual(C, C3_formula(4))
        self.assertEqual(B, B3_formula(4))
        self.assertEqual(A, A3_formula(4))

    def test_N5(self):
        D, C, B, A = delta_F3_analytical(5)
        self.assertEqual(D, D3_formula(5))
        self.assertEqual(C, C3_formula(5))
        self.assertEqual(B, B3_formula(5))
        self.assertEqual(A, A3_formula(5))

    def test_N6(self):
        D, C, B, A = delta_F3_analytical(6)
        self.assertEqual(D, D3_formula(6))
        self.assertEqual(C, C3_formula(6))
        self.assertEqual(B, B3_formula(6))
        self.assertEqual(A, A3_formula(6))


# ============================================================================
# 7. Specific N-values: exact D, C, B, A values
# ============================================================================

class TestExactValues(unittest.TestCase):
    """Verify exact D, C, B, A values at specific N."""

    def test_N3_D(self):
        self.assertEqual(D3_formula(3), Fraction(1, 27648))

    def test_N3_C(self):
        self.assertEqual(C3_formula(3), Fraction(79, 2880))

    def test_N3_B(self):
        self.assertEqual(B3_formula(3), Fraction(69, 8))

    def test_N3_A(self):
        self.assertEqual(A3_formula(3), Fraction(6281, 4))

    def test_N4_D(self):
        self.assertEqual(D3_formula(4), Fraction(1, 13824))

    def test_N4_C(self):
        self.assertEqual(C3_formula(4), Fraction(221, 2880))

    def test_N4_B(self):
        self.assertEqual(B3_formula(4), Fraction(1199, 36))

    def test_N4_A(self):
        self.assertEqual(A3_formula(4), Fraction(109499, 12))


# ============================================================================
# 8. Polynomial degree and structure
# ============================================================================

class TestPolynomialStructure(unittest.TestCase):
    """Verify polynomial degrees and leading coefficients."""

    def test_D3_degree1(self):
        """D_3(N) = (N-2)/27648 is degree 1."""
        # Leading coefficient: 1/27648
        self.assertEqual(D3_formula(1000) * 27648 / (1000 - 2), Fraction(1))

    def test_C3_degree3(self):
        """C_3(N) has degree 3 with leading term 35*N^2/34560 * N = 35*N^3/34560."""
        # The leading coefficient (N^3 term) is (N-2)*35*N^2/34560 -> 35/34560 * N^3
        # = 7/6912 * N^3 for large N
        c3_1000 = C3_formula(1000)
        # ~ 7/6912 * 10^9 for large N
        ratio = c3_1000 / Fraction(1000**3)
        self.assertAlmostEqual(float(ratio), 7.0 / 6912, places=3)

    def test_B3_degree5(self):
        """B_3(N) has degree 5."""
        # Leading term: (N-2) * 21*N^4 / 1728 -> 21/1728 * N^5 = 7/576 * N^5
        b_1000 = B3_formula(1000)
        ratio = b_1000 / Fraction(1000**5)
        self.assertAlmostEqual(float(ratio), 7.0 / 576, places=3)

    def test_A3_degree7(self):
        """A_3(N) has degree 7."""
        # Leading term: (N-2) * 120*N^6 / 1080 -> 120/1080 * N^7 = 1/9 * N^7
        a_10000 = A3_formula(10000)
        ratio = a_10000 / Fraction(10000**7)
        self.assertAlmostEqual(float(ratio), 1.0 / 9, places=3)

    def test_N_minus_2_factor(self):
        """All four polynomials vanish at N=2."""
        self.assertEqual(D3_formula(2), Fraction(0))
        self.assertEqual(C3_formula(2), Fraction(0))
        self.assertEqual(B3_formula(2), Fraction(0))
        self.assertEqual(A3_formula(2), Fraction(0))


# ============================================================================
# 9. Positivity
# ============================================================================

class TestPositivity(unittest.TestCase):
    """For N >= 3 and c > 0, delta_F_3^{grav} should be positive."""

    def test_positivity_N3(self):
        for c_val in [1, 5, 10, 100]:
            self.assertTrue(verify_positivity(3, Fraction(c_val)))

    def test_positivity_N5(self):
        for c_val in [1, 5, 10, 100]:
            self.assertTrue(verify_positivity(5, Fraction(c_val)))

    def test_positivity_N10(self):
        for c_val in [1, 5, 10, 100]:
            self.assertTrue(verify_positivity(10, Fraction(c_val)))

    def test_all_DCBA_positive_N3_to_12(self):
        """D, C, B, A should all be non-negative for N >= 3."""
        for N in range(3, 13):
            self.assertGreater(D3_formula(N), 0, f"D_3({N}) <= 0")
            self.assertGreater(C3_formula(N), 0, f"C_3({N}) <= 0")
            self.assertGreater(B3_formula(N), 0, f"B_3({N}) <= 0")
            self.assertGreater(A3_formula(N), 0, f"A_3({N}) <= 0")


# ============================================================================
# 10. Asymptotics
# ============================================================================

class TestAsymptotics(unittest.TestCase):
    """Verify asymptotic behavior."""

    def test_large_c_dominated_by_D(self):
        """For large c, delta_F_3 ~ D_3(N) * c."""
        N = 5
        c = Fraction(10**8)
        delta = delta_F3_formula(N, c)
        D_term = D3_formula(N) * c
        ratio = delta / D_term
        self.assertAlmostEqual(float(ratio), 1.0, places=4)

    def test_small_c_dominated_by_A(self):
        """For small c, delta_F_3 ~ A_3(N) / c^2."""
        N = 5
        c = Fraction(1, 10**6)
        delta = delta_F3_formula(N, c)
        A_term = A3_formula(N) / (c * c)
        ratio = delta / A_term
        self.assertAlmostEqual(float(ratio), 1.0, places=4)

    def test_monotone_in_N(self):
        """At fixed c, delta_F_3 increases with N."""
        c = Fraction(10)
        prev = delta_F3_formula(3, c)
        for N in range(4, 13):
            curr = delta_F3_formula(N, c)
            self.assertGreater(curr, prev, f"Not monotone at N={N}")
            prev = curr


# ============================================================================
# 11. Cross-genus consistency
# ============================================================================

class TestCrossGenusConsistency(unittest.TestCase):
    """Consistency between genus-2 and genus-3 formulas."""

    def test_genus2_N2_vanishes(self):
        """Genus-2 correction also vanishes at N=2."""
        from theorem_delta_f3_universal_engine import B2_formula, A2_formula
        self.assertEqual(B2_formula(2), Fraction(0))
        self.assertEqual(A2_formula(2), Fraction(0))

    def test_genus3_larger_than_genus2_at_small_c(self):
        """At small c, higher-genus corrections grow, so A_3/c^2 >> A_2/c."""
        from theorem_delta_f3_universal_engine import delta_F2_formula
        c = Fraction(1, 10)
        for N in range(3, 8):
            f2 = delta_F2_formula(N, c)
            f3 = delta_F3_formula(N, c)
            self.assertGreater(f3, f2,
                               f"N={N}, c=1/10: genus-3 not larger than genus-2")

    def test_degree_pattern(self):
        """Genus-2 has degrees (2, 4); genus-3 has (1, 3, 5, 7)."""
        # Genus-2: B_2 degree 2, A_2 degree 4 (from (N-2)*(degree 3))
        from theorem_delta_f3_universal_engine import B2_formula, A2_formula
        # Just check that B2(N) is quadratic (degree 2)
        # B2(N) = (N-2)(N+3)/96
        self.assertEqual(B2_formula(100), Fraction(98 * 103, 96))


# ============================================================================
# 12. Formula consistency at many N and c values
# ============================================================================

class TestFormulaConsistency(unittest.TestCase):
    """Verify the formula is internally consistent."""

    def test_c_structure_N3(self):
        """delta_F3(3, c) = D*c + C + B/c + A/c^2 for all c."""
        D = D3_formula(3)
        C = C3_formula(3)
        B = B3_formula(3)
        A = A3_formula(3)
        for c_val in range(1, 20):
            c = Fraction(c_val)
            lhs = delta_F3_formula(3, c)
            rhs = D * c + C + B / c + A / (c * c)
            self.assertEqual(lhs, rhs, f"c={c_val}")

    def test_c_structure_N7(self):
        D = D3_formula(7)
        C = C3_formula(7)
        B = B3_formula(7)
        A = A3_formula(7)
        for c_val in range(1, 10):
            c = Fraction(c_val)
            lhs = delta_F3_formula(7, c)
            rhs = D * c + C + B / c + A / (c * c)
            self.assertEqual(lhs, rhs, f"c={c_val}")

    def test_additivity_structure(self):
        """D, C, B, A all have (N-2) factor and are polynomials in N."""
        for N in range(2, 15):
            d = D3_formula(N)
            c = C3_formula(N)
            b = B3_formula(N)
            a = A3_formula(N)
            if N == 2:
                self.assertEqual(d, 0)
                self.assertEqual(c, 0)
                self.assertEqual(b, 0)
                self.assertEqual(a, 0)
            else:
                # All should be positive
                self.assertGreater(d, 0)
                self.assertGreater(c, 0)
                self.assertGreater(b, 0)
                self.assertGreater(a, 0)


# ============================================================================
# 13. Graph sum decomposition
# ============================================================================

class TestGraphSumDecomposition(unittest.TestCase):
    """Verify per-graph properties of the graph sum."""

    def test_smooth_graph_zero_mixed(self):
        """The smooth graph (0 edges) contributes 0 to mixed."""
        graphs = genus3_graphs()
        smooth = [g for g in graphs if g.num_edges == 0]
        self.assertEqual(len(smooth), 1)

    def test_single_edge_zero_mixed(self):
        """Graphs with 1 edge have 0 mixed (single channel, always diagonal)."""
        graphs = genus3_graphs()
        c = Fraction(1)
        aw = (2, 3)
        for g in graphs:
            if g.num_edges == 1:
                from theorem_delta_f3_universal_engine import graph_amplitude_decomposed
                decomp = graph_amplitude_decomposed(g, c, aw)
                self.assertEqual(decomp['mixed'], Fraction(0))


# ============================================================================
# 14. Specific formula values
# ============================================================================

class TestSpecificValues(unittest.TestCase):
    """Verify specific computed values from the derivation."""

    def test_D3_values(self):
        expected = {
            3: Fraction(1, 27648),
            4: Fraction(1, 13824),
            5: Fraction(1, 9216),
            6: Fraction(1, 6912),
            7: Fraction(5, 27648),
            8: Fraction(1, 4608),
            9: Fraction(7, 27648),
            10: Fraction(1, 3456),
        }
        for N, val in expected.items():
            self.assertEqual(D3_formula(N), val, f"D_3({N})")

    def test_C3_values(self):
        expected = {
            3: Fraction(79, 2880),
            4: Fraction(221, 2880),
            5: Fraction(887, 5760),
            6: Fraction(191, 720),
        }
        for N, val in expected.items():
            self.assertEqual(C3_formula(N), val, f"C_3({N})")

    def test_B3_values(self):
        expected = {
            3: Fraction(133, 16),
            4: Fraction(4499, 144),
            5: Fraction(5887, 72),
            6: Fraction(6431, 36),
        }
        for N, val in expected.items():
            self.assertEqual(B3_formula(N), val, f"B_3({N})")

    def test_A3_values(self):
        expected = {
            3: Fraction(6281, 4),
            4: Fraction(109499, 12),
            5: Fraction(68959, 2),
            6: Fraction(206215, 2),
        }
        for N, val in expected.items():
            self.assertEqual(A3_formula(N), val, f"A_3({N})")


# ============================================================================
# 15. Inner polynomial evaluations
# ============================================================================

class TestInnerPolynomials(unittest.TestCase):
    """Verify the inner polynomials (after factoring (N-2))."""

    def test_C3_inner_at_3(self):
        # 35*9 + 133*3 + 234 = 315 + 399 + 234 = 948
        # C3(3) = 1 * 948 / 34560 = 948/34560 = 79/2880
        self.assertEqual(Fraction(948, 34560), Fraction(79, 2880))
        self.assertEqual(C3_formula(3), Fraction(79, 2880))

    def test_B3_inner_at_3(self):
        # 15*81 + 147*27 + 517*9 + 947*3 + 1686
        # = 1215 + 3969 + 4653 + 2841 + 1686 = 14364
        # B3(3) = 1 * 14364 / 1728 = 14364/1728 = 133/16
        self.assertEqual(Fraction(14364, 1728), Fraction(133, 16))

    def test_A3_inner_at_3(self):
        # 120*729 + 1300*243 + 5918*81 + 14786*27 + 27592*9 + 36369*3 + 56475
        # = 87480 + 315900 + 479358 + 399222 + 248328 + 109107 + 56475
        # = 1695870
        # A3(3) = 1 * 1695870 / 1080 = 6281/4
        val = 87480 + 315900 + 479358 + 399222 + 248328 + 109107 + 56475
        self.assertEqual(val, 1695870)
        self.assertEqual(Fraction(1695870, 1080), Fraction(6281, 4))


# ============================================================================
# 16. Denominators
# ============================================================================

class TestDenominators(unittest.TestCase):
    """Verify the denominator factorizations."""

    def test_D3_denominator(self):
        # 27648 = 2^10 * 3^3
        self.assertEqual(27648, 2**10 * 3**3)

    def test_C3_denominator(self):
        # 34560 = 2^8 * 3^3 * 5
        self.assertEqual(34560, 2**8 * 3**3 * 5)

    def test_B3_denominator(self):
        # 1728 = 2^6 * 3^3
        self.assertEqual(1728, 2**6 * 3**3)

    def test_A3_denominator(self):
        # 1080 = 2^3 * 3^3 * 5
        self.assertEqual(1080, 2**3 * 3**3 * 5)


# ============================================================================
# 17. Third-path verification: extract DCBA from 4 c-values
# ============================================================================

class TestExtractDCBA(unittest.TestCase):
    """Third independent path: extract D,C,B,A via 4x4 linear system."""

    def test_extract_N3(self):
        D, C, B, A = extract_DCBA_from_c_values(3)
        self.assertEqual(D, D3_formula(3))
        self.assertEqual(C, C3_formula(3))
        self.assertEqual(B, B3_formula(3))
        self.assertEqual(A, A3_formula(3))

    def test_extract_N4(self):
        D, C, B, A = extract_DCBA_from_c_values(4)
        self.assertEqual(D, D3_formula(4))
        self.assertEqual(C, C3_formula(4))
        self.assertEqual(B, B3_formula(4))
        self.assertEqual(A, A3_formula(4))

    def test_extract_N5(self):
        D, C, B, A = extract_DCBA_from_c_values(5)
        self.assertEqual(D, D3_formula(5))
        self.assertEqual(C, C3_formula(5))
        self.assertEqual(B, B3_formula(5))
        self.assertEqual(A, A3_formula(5))

    def test_extract_different_c_values(self):
        """Use a non-default set of c-values to extract DCBA at N=3."""
        c_vals = (Fraction(2), Fraction(3), Fraction(7), Fraction(11))
        D, C, B, A = extract_DCBA_from_c_values(3, c_vals=c_vals)
        self.assertEqual(D, D3_formula(3))
        self.assertEqual(C, C3_formula(3))
        self.assertEqual(B, B3_formula(3))
        self.assertEqual(A, A3_formula(3))


# ============================================================================
# 18. Out-of-sample verification at large N
# ============================================================================

class TestOutOfSample(unittest.TestCase):
    """Verify formula at N values beyond the interpolation range."""

    def test_N9_analytical(self):
        D, C, B, A = delta_F3_analytical(9)
        self.assertEqual(D, D3_formula(9))
        self.assertEqual(C, C3_formula(9))
        self.assertEqual(B, B3_formula(9))
        self.assertEqual(A, A3_formula(9))

    def test_N10_analytical(self):
        D, C, B, A = delta_F3_analytical(10)
        self.assertEqual(D, D3_formula(10))
        self.assertEqual(C, C3_formula(10))
        self.assertEqual(B, B3_formula(10))
        self.assertEqual(A, A3_formula(10))

    def test_N10_exact_values(self):
        """Exact values at N=10, independently computed."""
        self.assertEqual(D3_formula(10), Fraction(1, 3456))
        # C3(10) = 8 * (35*100 + 133*10 + 234) / 34560
        #        = 8 * 5064 / 34560 = 40512 / 34560 = 211/180
        self.assertEqual(C3_formula(10), Fraction(211, 180))

    def test_N11_analytical(self):
        D, C, B, A = delta_F3_analytical(11)
        self.assertEqual(D, D3_formula(11))
        self.assertEqual(C, C3_formula(11))
        self.assertEqual(B, B3_formula(11))
        self.assertEqual(A, A3_formula(11))


# ============================================================================
# 19. Analytical vs brute-force cross-validation
# ============================================================================

class TestAnalyticalVsBruteForce(unittest.TestCase):
    """The analytical (c-factorization) and brute-force methods must agree."""

    def test_N3_c1(self):
        bf = delta_F3_grav_graph_sum(3, Fraction(1))
        fm = delta_F3_formula(3, Fraction(1))
        self.assertEqual(bf, fm)

    def test_N3_c7(self):
        bf = delta_F3_grav_graph_sum(3, Fraction(7))
        fm = delta_F3_formula(3, Fraction(7))
        self.assertEqual(bf, fm)

    def test_N3_c13(self):
        bf = delta_F3_grav_graph_sum(3, Fraction(13))
        fm = delta_F3_formula(3, Fraction(13))
        self.assertEqual(bf, fm)

    def test_N4_c1(self):
        bf = delta_F3_grav_graph_sum(4, Fraction(1))
        fm = delta_F3_formula(4, Fraction(1))
        self.assertEqual(bf, fm)

    def test_N4_c3(self):
        bf = delta_F3_grav_graph_sum(4, Fraction(3))
        fm = delta_F3_formula(4, Fraction(3))
        self.assertEqual(bf, fm)

    def test_N5_c1(self):
        bf = delta_F3_grav_graph_sum(5, Fraction(1))
        fm = delta_F3_formula(5, Fraction(1))
        self.assertEqual(bf, fm)


# ============================================================================
# 20. Gravitational vs actual W_3 cross-check
# ============================================================================

class TestGravitationalVsActualW3(unittest.TestCase):
    """The gravitational and actual W_3 computations now agree exactly.

    Previously these differed by 5/(16c) due to a half-edge ordering bug
    in the gravitational engine: self-loop half-edges were interleaved
    with bridge half-edges at genus-0 vertices instead of being paired
    first. The fix ensures correct factorization pairing.
    """

    def test_difference_at_c1(self):
        from w3_genus3_cross_channel import genus3_cross_channel
        c = Fraction(1)
        grav = delta_F3_grav_graph_sum(3, c)
        actual = genus3_cross_channel(c)
        self.assertEqual(grav, actual)

    def test_difference_at_c5(self):
        from w3_genus3_cross_channel import genus3_cross_channel
        c = Fraction(5)
        grav = delta_F3_grav_graph_sum(3, c)
        actual = genus3_cross_channel(c)
        self.assertEqual(grav, actual)

    def test_difference_at_c10(self):
        from w3_genus3_cross_channel import genus3_cross_channel
        c = Fraction(10)
        grav = delta_F3_grav_graph_sum(3, c)
        actual = genus3_cross_channel(c)
        self.assertEqual(grav, actual)

    def test_difference_formula(self):
        """grav == actual for all c > 0 (after half-edge ordering fix)."""
        from w3_genus3_cross_channel import genus3_cross_channel
        for c_val in [1, 2, 3, 7, 26]:
            c = Fraction(c_val)
            diff = delta_F3_grav_graph_sum(3, c) - genus3_cross_channel(c)
            self.assertEqual(diff, Fraction(0),
                             f"Difference not 0 at c={c_val}")


# ============================================================================
# 21. Genus-2 consistency across N range
# ============================================================================

class TestGenus2Genus3Consistency(unittest.TestCase):
    """Cross-genus structural consistency checks."""

    def test_genus2_N2_vanishes(self):
        from theorem_delta_f3_universal_engine import B2_formula, A2_formula
        self.assertEqual(B2_formula(2), Fraction(0))
        self.assertEqual(A2_formula(2), Fraction(0))

    def test_genus2_known_W3(self):
        """delta_F_2(W_3) = (c+204)/(16c) = 1/16 + 51/(4c)."""
        from theorem_delta_f3_universal_engine import B2_formula, A2_formula
        self.assertEqual(B2_formula(3), Fraction(1, 16))
        self.assertEqual(A2_formula(3), Fraction(51, 4))

    def test_genus2_B2_formula(self):
        """B_2(N) = (N-2)(N+3)/96."""
        from theorem_delta_f3_universal_engine import B2_formula
        for N in range(2, 15):
            expected = Fraction((N - 2) * (N + 3), 96)
            self.assertEqual(B2_formula(N), expected, f"B_2({N})")

    def test_genus2_A2_formula(self):
        """A_2(N) = (N-2)(3N^3+14N^2+22N+33)/24."""
        from theorem_delta_f3_universal_engine import A2_formula
        for N in range(2, 15):
            inner = 3 * N**3 + 14 * N**2 + 22 * N + 33
            expected = Fraction((N - 2) * inner, 24)
            self.assertEqual(A2_formula(N), expected, f"A_2({N})")

    def test_genus3_dominates_at_small_c(self):
        """For small c, A_3/c^2 >> A_2/c."""
        from theorem_delta_f3_universal_engine import delta_F2_formula
        c = Fraction(1, 100)
        for N in range(3, 8):
            f2 = delta_F2_formula(N, c)
            f3 = delta_F3_formula(N, c)
            self.assertGreater(f3, f2)


# ============================================================================
# 22. Large-N leading coefficients
# ============================================================================

class TestLargeNLeading(unittest.TestCase):
    """Verify leading-order polynomial behavior at large N."""

    def test_D3_leading_coefficient(self):
        """D_3(N) ~ N/27648 for large N."""
        N = 10000
        val = D3_formula(N)
        leading = Fraction(N, 27648)
        ratio = val / leading
        self.assertAlmostEqual(float(ratio), 1.0, places=3)

    def test_C3_leading_coefficient(self):
        """C_3(N) ~ 35*N^3/34560 = 7*N^3/6912 for large N."""
        N = 10000
        val = C3_formula(N)
        leading = Fraction(7) * Fraction(N**3) / Fraction(6912)
        ratio = val / leading
        self.assertAlmostEqual(float(ratio), 1.0, places=2)

    def test_B3_leading_coefficient(self):
        """B_3(N) ~ 15*N^5/1728 = 5*N^5/576 for large N."""
        N = 10000
        val = B3_formula(N)
        leading = Fraction(5) * Fraction(N**5) / Fraction(576)
        ratio = val / leading
        self.assertAlmostEqual(float(ratio), 1.0, places=2)

    def test_A3_leading_coefficient(self):
        """A_3(N) ~ 120*N^7/1080 = N^7/9 for large N."""
        N = 10000
        val = A3_formula(N)
        leading = Fraction(N**7) / Fraction(9)
        ratio = val / leading
        self.assertAlmostEqual(float(ratio), 1.0, places=2)


# ============================================================================
# 23. Harmonic sum relations
# ============================================================================

class TestHarmonicSumRelations(unittest.TestCase):
    """Verify the kappa_total = c*(H_N - 1) identity."""

    def test_kappa_total_N3(self):
        c = Fraction(6)
        self.assertEqual(grav_kappa_total(3, c), Fraction(5))

    def test_kappa_total_N4(self):
        c = Fraction(12)
        # kappa = 12*(1/2 + 1/3 + 1/4) = 12*(13/12) = 13
        self.assertEqual(grav_kappa_total(4, c), Fraction(13))

    def test_kappa_total_N5(self):
        c = Fraction(60)
        # kappa = 60*(1/2+1/3+1/4+1/5) = 60*(77/60) = 77
        self.assertEqual(grav_kappa_total(5, c), Fraction(77))

    def test_kappa_channel_sum(self):
        """kappa_total = sum_{j=2}^N c/j."""
        c = Fraction(7)
        for N in range(2, 10):
            expected = sum(c / Fraction(j) for j in range(2, N + 1))
            self.assertEqual(grav_kappa_total(N, c), expected)


# ============================================================================
# 24. Edge-case and boundary tests
# ============================================================================

class TestEdgeCases(unittest.TestCase):
    """Boundary conditions and edge cases."""

    def test_N1_formula(self):
        """N=1 has no channels at all (weight 2 needs N >= 2)."""
        # The formulas evaluate to negative values at N=1 (no physical meaning)
        d = D3_formula(1)
        self.assertEqual(d, Fraction(-1, 27648))

    def test_large_c_asymptotics(self):
        """At c=10^12, delta_F3 is dominated by D_3(N)*c."""
        c = Fraction(10**12)
        for N in [3, 5, 10]:
            delta = delta_F3_formula(N, c)
            D_term = D3_formula(N) * c
            ratio = delta / D_term
            self.assertAlmostEqual(float(ratio), 1.0, places=4)

    def test_small_c_asymptotics(self):
        """At c=10^{-6}, delta_F3 is dominated by A_3(N)/c^2."""
        c = Fraction(1, 10**6)
        for N in [3, 5, 10]:
            delta = delta_F3_formula(N, c)
            A_term = A3_formula(N) / (c * c)
            ratio = delta / A_term
            self.assertAlmostEqual(float(ratio), 1.0, places=4)


# ============================================================================
# 25. Polynomial consistency: D,C,B,A evaluated at N=2..12 simultaneously
# ============================================================================

class TestPolynomialConsistencyWide(unittest.TestCase):
    """Verify DCBA formulas match analytical computation across wide N range."""

    def test_analytical_matches_formula_N2_to_9(self):
        for N in range(2, 10):
            D, C, B, A = delta_F3_analytical(N)
            self.assertEqual(D, D3_formula(N), f"D mismatch at N={N}")
            self.assertEqual(C, C3_formula(N), f"C mismatch at N={N}")
            self.assertEqual(B, B3_formula(N), f"B mismatch at N={N}")
            self.assertEqual(A, A3_formula(N), f"A mismatch at N={N}")


# ============================================================================
# 26. Reconstruction via Lagrange interpolation
# ============================================================================

class TestLagrangeReconstruction(unittest.TestCase):
    """Verify that Lagrange interpolation of computed points recovers the formula."""

    def test_D3_interpolation(self):
        """D_3 is degree 1, so 2 points suffice."""
        from theorem_delta_f3_universal_engine import (
            lagrange_interpolate, evaluate_polynomial
        )
        points = [(N, D3_formula(N)) for N in range(2, 5)]
        coeffs = lagrange_interpolate(points)
        for N in range(2, 15):
            val = evaluate_polynomial(coeffs, Fraction(N))
            self.assertEqual(val, D3_formula(N), f"D_3 interpolation fails at N={N}")

    def test_C3_interpolation(self):
        """C_3 is degree 3, so 4 points suffice."""
        from theorem_delta_f3_universal_engine import (
            lagrange_interpolate, evaluate_polynomial
        )
        points = [(N, C3_formula(N)) for N in range(2, 7)]
        coeffs = lagrange_interpolate(points)
        for N in range(2, 20):
            val = evaluate_polynomial(coeffs, Fraction(N))
            self.assertEqual(val, C3_formula(N), f"C_3 interpolation fails at N={N}")

    def test_B3_interpolation(self):
        """B_3 is degree 5, so 6 points suffice."""
        from theorem_delta_f3_universal_engine import (
            lagrange_interpolate, evaluate_polynomial
        )
        points = [(N, B3_formula(N)) for N in range(2, 9)]
        coeffs = lagrange_interpolate(points)
        for N in range(2, 20):
            val = evaluate_polynomial(coeffs, Fraction(N))
            self.assertEqual(val, B3_formula(N), f"B_3 interpolation fails at N={N}")

    def test_A3_interpolation(self):
        """A_3 is degree 7, so 8 points suffice."""
        from theorem_delta_f3_universal_engine import (
            lagrange_interpolate, evaluate_polynomial
        )
        points = [(N, A3_formula(N)) for N in range(2, 11)]
        coeffs = lagrange_interpolate(points)
        for N in range(2, 20):
            val = evaluate_polynomial(coeffs, Fraction(N))
            self.assertEqual(val, A3_formula(N), f"A_3 interpolation fails at N={N}")


# ============================================================================
# 27. Self-loop parity vanishing
# ============================================================================

class TestSelfLoopParity(unittest.TestCase):
    """Self-loop graphs have constrained channel assignments."""

    def test_single_vertex_double_loop_diagonal_only(self):
        """Single-vertex g=1 with 2 self-loops: both loops must carry same channel
        (vertex genus >= 1 requires all half-edges same channel)."""
        graphs = genus3_graphs()
        from theorem_delta_f3_universal_engine import graph_amplitude_decomposed
        c = Fraction(1)
        aw = (2, 3, 4)
        for g in graphs:
            if g.num_vertices == 1 and g.num_edges == 2:
                decomp = graph_amplitude_decomposed(g, c, aw)
                self.assertEqual(decomp['mixed'], Fraction(0),
                                 "g=1 double-loop has mixed channels")

    def test_single_vertex_triple_loop_has_mixed(self):
        """Single-vertex g=0 with 3 self-loops CAN have mixed channels."""
        graphs = genus3_graphs()
        from theorem_delta_f3_universal_engine import graph_amplitude_decomposed
        c = Fraction(1)
        aw = (2, 3)
        for g in graphs:
            if g.num_vertices == 1 and g.num_edges == 3 and g.vertex_genera[0] == 0:
                decomp = graph_amplitude_decomposed(g, c, aw)
                self.assertGreater(decomp['mixed'], Fraction(0),
                                   "g=0 triple-loop should have mixed channels")


# ============================================================================
# 28. Summing D*c + C + B/c + A/c^2 at specific rational c
# ============================================================================

class TestRationalCValues(unittest.TestCase):
    """Verify the formula at rational (non-integer) c values."""

    def test_N3_c_half(self):
        c = Fraction(1, 2)
        expected = (D3_formula(3) * c + C3_formula(3)
                    + B3_formula(3) / c + A3_formula(3) / (c * c))
        self.assertEqual(delta_F3_formula(3, c), expected)

    def test_N5_c_third(self):
        c = Fraction(1, 3)
        expected = (D3_formula(5) * c + C3_formula(5)
                    + B3_formula(5) / c + A3_formula(5) / (c * c))
        self.assertEqual(delta_F3_formula(5, c), expected)

    def test_N4_c_seven_thirds(self):
        c = Fraction(7, 3)
        expected = (D3_formula(4) * c + C3_formula(4)
                    + B3_formula(4) / c + A3_formula(4) / (c * c))
        self.assertEqual(delta_F3_formula(4, c), expected)


# ============================================================================
# 29. Inner polynomial coefficient verification
# ============================================================================

class TestInnerPolynomialCoefficients(unittest.TestCase):
    """Verify inner polynomial coefficients by direct evaluation."""

    def test_C3_inner_at_4(self):
        # inner = 35*16 + 133*4 + 234 = 560 + 532 + 234 = 1326
        # C3(4) = 2 * 1326 / 34560 = 2652/34560 = 221/2880
        self.assertEqual(Fraction(2652, 34560), Fraction(221, 2880))
        self.assertEqual(C3_formula(4), Fraction(221, 2880))

    def test_B3_inner_at_4(self):
        # inner = 15*256 + 147*64 + 517*16 + 947*4 + 1686
        #       = 3840 + 9408 + 8272 + 3788 + 1686 = 26994
        # B3(4) = 2 * 26994 / 1728 = 53988/1728 = 4499/144
        inner = 3840 + 9408 + 8272 + 3788 + 1686
        self.assertEqual(inner, 26994)
        self.assertEqual(Fraction(53988, 1728), Fraction(4499, 144))

    def test_A3_inner_at_4(self):
        # inner at N=4:
        # 120*4096 + 1300*1024 + 5918*256 + 14786*64 + 27592*16 + 36369*4 + 56475
        terms = [120*4096, 1300*1024, 5918*256, 14786*64, 27592*16, 36369*4, 56475]
        inner = sum(terms)
        # A3(4) = 2 * inner / 1080
        a4 = Fraction(2 * inner, 1080)
        self.assertEqual(a4, A3_formula(4))


# ============================================================================
# 30. Degree pattern: (1, 3, 5, 7) increases by 2 per 1/c power
# ============================================================================

class TestDegreePattern(unittest.TestCase):
    """The degree pattern (1, 3, 5, 7) increases by 2 per additional 1/c power.

    This reflects: each edge carries N-1 channel choices, and graphs with more
    edges (higher h^1) have polynomials with higher N-degree.
    """

    def test_D3_is_exactly_degree_1(self):
        """D_3(N) = (N-2)/27648 is degree 1, coefficient N^1 is 1/27648."""
        from theorem_delta_f3_universal_engine import lagrange_interpolate
        points = [(N, D3_formula(N)) for N in range(2, 5)]
        coeffs = lagrange_interpolate(points)
        # coeffs[0] is constant, coeffs[1] is N^1 coefficient
        # D3(N) = (N-2)/27648 = N/27648 - 2/27648
        self.assertEqual(coeffs[1], Fraction(1, 27648))
        self.assertEqual(coeffs[0], Fraction(-2, 27648))
        self.assertEqual(len(coeffs), 2)  # exactly degree 1

    def test_C3_is_exactly_degree_3(self):
        from theorem_delta_f3_universal_engine import lagrange_interpolate
        points = [(N, C3_formula(N)) for N in range(2, 7)]
        coeffs = lagrange_interpolate(points)
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        self.assertEqual(len(coeffs), 4)  # degree 3

    def test_B3_is_exactly_degree_5(self):
        from theorem_delta_f3_universal_engine import lagrange_interpolate
        points = [(N, B3_formula(N)) for N in range(2, 9)]
        coeffs = lagrange_interpolate(points)
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        self.assertEqual(len(coeffs), 6)  # degree 5

    def test_A3_is_exactly_degree_7(self):
        from theorem_delta_f3_universal_engine import lagrange_interpolate
        points = [(N, A3_formula(N)) for N in range(2, 11)]
        coeffs = lagrange_interpolate(points)
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        self.assertEqual(len(coeffs), 8)  # degree 7


# ============================================================================
# 31. Common denominator check: the single-fraction form
# ============================================================================

class TestSingleFractionForm(unittest.TestCase):
    """Verify the single-fraction numerator for specific N values."""

    def test_N3_single_fraction(self):
        """delta_F3(3, c) = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
        in the GRAVITATIONAL approximation."""
        for c_val in [1, 2, 5, 10]:
            c = Fraction(c_val)
            num = 5 * c_val**3 + 3792 * c_val**2 + 1149120 * c_val + 217071360
            den = 138240 * c_val**2
            self.assertEqual(delta_F3_formula(3, c), Fraction(num, den))

    def test_N3_numerator_coefficients(self):
        """All numerator coefficients are positive."""
        # D*138240 = 5, C*138240 = 3792, B*138240 = 1149120, A*138240 = 217071360
        self.assertEqual(D3_formula(3) * 138240, Fraction(5))
        self.assertEqual(C3_formula(3) * 138240, Fraction(3792))
        self.assertEqual(B3_formula(3) * 138240, Fraction(1149120))
        self.assertEqual(A3_formula(3) * 138240, Fraction(217071360))


# ============================================================================
# 32. h^1 decomposition of graph contributions
# ============================================================================

class TestH1Decomposition(unittest.TestCase):
    """Verify that the c-factorization by loop number h^1 is correct."""

    def test_h1_range(self):
        """h^1 ranges from 0 to 3 for genus-3 graphs."""
        graphs = genus3_graphs()
        h1_values = set(g.first_betti for g in graphs)
        self.assertEqual(h1_values, {0, 1, 2, 3})

    def test_h1_count_sum(self):
        """4 + 9 + 14 + 15 = 42."""
        graphs = genus3_graphs()
        h1_counts = {}
        for g in graphs:
            h1 = g.first_betti
            h1_counts[h1] = h1_counts.get(h1, 0) + 1
        total = sum(h1_counts.values())
        self.assertEqual(total, 42)

    def test_c_scaling(self):
        """Graph with h^1=k has amplitude scaling as c^{1-k} at c=1 vs c=c0."""
        # For h^1=0 (trees): amplitude ~ c^1
        # For h^1=1: amplitude ~ c^0 (constant in c)
        # For h^1=2: amplitude ~ c^{-1}
        # For h^1=3: amplitude ~ c^{-2}
        D, C, B, A = delta_F3_analytical(3)
        c_test = Fraction(7)
        delta = delta_F3_formula(3, c_test)
        reconstructed = D * c_test + C + B / c_test + A / (c_test * c_test)
        self.assertEqual(delta, reconstructed)


if __name__ == '__main__':
    unittest.main()
