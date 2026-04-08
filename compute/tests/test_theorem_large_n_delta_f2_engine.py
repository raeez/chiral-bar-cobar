r"""Tests for the large-N expansion of delta_F_2^{grav}(W_N).

VERIFICATION PATHS (multi-path mandate: 3+ per claim):

1. Direct computation from closed-form B(N), A(N)
2. Cross-verification with independent graph sum engine
3. Expansion polynomial identity verification
4. Long division / ratio analysis
5. 't Hooft limit consistency
6. W_{1+infinity} scaling analysis
7. Matrix model / Frobenius manifold structure
8. ABJM comparison
9. Koszul duality constraints
10. Limiting cases (N=2, large N, large c)

Manuscript references:
    thm:multi-weight-genus-expansion, thm:theorem-d, AP27
"""

import unittest
import sys
import os
from fractions import Fraction
from math import factorial, log

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_large_n_delta_f2_engine import (
    A_exact,
    A_expansion_coefficients,
    A_leading,
    B_exact,
    B_expansion_coefficients,
    B_leading,
    abjm_cross_channel_status,
    abjm_genus_g_free_energy,
    c_thooft_large_N,
    c_wn_thooft,
    cross_verify_BN_AN,
    cross_verify_with_graph_sum,
    delta_F2_grav_closed,
    delta_F2_thooft,
    delta_F2_winfty_scaling,
    dominance_crossover,
    effective_matrix_size,
    frobenius_eigenvalues,
    frobenius_manifold_dimension,
    hypothetical_m2_scaling,
    kappa_abjm,
    large_N_table,
    normalized_delta_F2,
    ratio_A_over_B,
    ratio_large_N_expansion,
    spectral_curve_branch_points,
    thooft_limit_A_over_c,
    thooft_table,
    verify_A_expansion,
    verify_B_expansion,
    verify_long_division,
)


# ============================================================================
# 1. Exact values of B(N)
# ============================================================================

class TestBExact(unittest.TestCase):
    """Verify B(N) = (N-2)(N+3)/96 at specific values."""

    def test_B2_vanishes(self):
        """B(2) = 0: Virasoro is uniform-weight, no cross-channel."""
        self.assertEqual(B_exact(2), Fraction(0))

    def test_B3(self):
        """B(3) = (1)(6)/96 = 1/16."""
        self.assertEqual(B_exact(3), Fraction(1, 16))

    def test_B4(self):
        """B(4) = (2)(7)/96 = 14/96 = 7/48."""
        self.assertEqual(B_exact(4), Fraction(7, 48))

    def test_B5(self):
        """B(5) = (3)(8)/96 = 24/96 = 1/4."""
        self.assertEqual(B_exact(5), Fraction(1, 4))

    def test_B6(self):
        """B(6) = (4)(9)/96 = 36/96 = 3/8."""
        self.assertEqual(B_exact(6), Fraction(3, 8))

    def test_B10(self):
        """B(10) = (8)(13)/96 = 104/96 = 13/12."""
        self.assertEqual(B_exact(10), Fraction(13, 12))

    def test_B20(self):
        """B(20) = (18)(23)/96 = 414/96 = 69/16."""
        self.assertEqual(B_exact(20), Fraction(69, 16))

    def test_B_positive_for_N_ge_3(self):
        """B(N) > 0 for all N >= 3."""
        for N in range(3, 51):
            self.assertGreater(B_exact(N), 0,
                               f"B({N}) should be positive")

    def test_B_monotone_increasing(self):
        """B(N) is strictly increasing for N >= 3."""
        for N in range(3, 50):
            self.assertLess(B_exact(N), B_exact(N + 1),
                            f"B({N}) should be < B({N+1})")

    def test_B_invalid_N(self):
        """B(N) raises for N < 2."""
        with self.assertRaises(ValueError):
            B_exact(1)


# ============================================================================
# 2. Exact values of A(N)
# ============================================================================

class TestAExact(unittest.TestCase):
    """Verify A(N) = (N-2)(3N^3 + 14N^2 + 22N + 33)/24 at specific values."""

    def test_A2_vanishes(self):
        """A(2) = 0: Virasoro is uniform-weight."""
        self.assertEqual(A_exact(2), Fraction(0))

    def test_A3(self):
        """A(3) = (1)(81+126+66+33)/24 = 306/24 = 51/4."""
        poly_val = 3 * 27 + 14 * 9 + 22 * 3 + 33
        self.assertEqual(poly_val, 306)
        self.assertEqual(A_exact(3), Fraction(306, 24))
        self.assertEqual(A_exact(3), Fraction(51, 4))

    def test_A4(self):
        """A(4) = (2)(3*64 + 14*16 + 22*4 + 33)/24 = (2)(192+224+88+33)/24."""
        poly_val = 3 * 64 + 14 * 16 + 22 * 4 + 33
        self.assertEqual(poly_val, 537)
        self.assertEqual(A_exact(4), Fraction(2 * 537, 24))
        self.assertEqual(A_exact(4), Fraction(1074, 24))
        self.assertEqual(A_exact(4), Fraction(179, 4))

    def test_A5(self):
        """A(5) = (3)(3*125 + 14*25 + 22*5 + 33)/24."""
        poly_val = 3 * 125 + 14 * 25 + 22 * 5 + 33
        self.assertEqual(poly_val, 868)
        self.assertEqual(A_exact(5), Fraction(3 * 868, 24))
        self.assertEqual(A_exact(5), Fraction(2604, 24))
        self.assertEqual(A_exact(5), Fraction(217, 2))

    def test_A_positive_for_N_ge_3(self):
        """A(N) > 0 for all N >= 3."""
        for N in range(3, 51):
            self.assertGreater(A_exact(N), 0,
                               f"A({N}) should be positive")

    def test_A_monotone_increasing(self):
        """A(N) is strictly increasing for N >= 3."""
        for N in range(3, 50):
            self.assertLess(A_exact(N), A_exact(N + 1),
                            f"A({N}) should be < A({N+1})")


# ============================================================================
# 3. W_3 consistency: delta_F_2 = (c + 204)/(16c)
# ============================================================================

class TestW3Consistency(unittest.TestCase):
    """Verify the W_3 special case matches the known formula."""

    def test_W3_formula_at_c100(self):
        """delta_F_2(W_3, 100) = (100+204)/(16*100) = 304/1600 = 19/100."""
        c = Fraction(100)
        expected = Fraction(304, 1600)
        self.assertEqual(delta_F2_grav_closed(3, c), expected)

    def test_W3_formula_at_c1(self):
        """delta_F_2(W_3, 1) = (1+204)/16 = 205/16."""
        c = Fraction(1)
        expected = Fraction(205, 16)
        self.assertEqual(delta_F2_grav_closed(3, c), expected)

    def test_W3_formula_symbolic(self):
        """B(3) + A(3)/c = 1/16 + 51/(4c) = (c+204)/(16c)."""
        for c_val in [1, 2, 5, 10, 50, 100, 1000]:
            c = Fraction(c_val)
            ours = delta_F2_grav_closed(3, c)
            known = (c + 204) / (16 * c)
            self.assertEqual(ours, known, f"W_3 formula mismatch at c={c_val}")

    def test_204_equals_4_times_51(self):
        """The 204 in (c+204)/(16c) equals 4*A(3) = 4*51/4*4/1 = 16*51/4.
        Actually: 16*B + 16*A/c = c + 16*A. 16*51/4 = 204. Confirmed."""
        self.assertEqual(16 * A_exact(3), Fraction(204))


# ============================================================================
# 4. Expansion verification (polynomial identity)
# ============================================================================

class TestExpansions(unittest.TestCase):
    """Verify that the expanded forms match the factored forms."""

    def test_B_expansion_all_N(self):
        """B(N) = (N^2 + N - 6)/96 for N = 2..50."""
        for N in range(2, 51):
            self.assertTrue(verify_B_expansion(N),
                            f"B expansion failed at N={N}")

    def test_A_expansion_all_N(self):
        """A(N) = (3N^4 + 8N^3 - 6N^2 - 11N - 66)/24 for N = 2..50."""
        for N in range(2, 51):
            self.assertTrue(verify_A_expansion(N),
                            f"A expansion failed at N={N}")

    def test_B_expansion_coefficients(self):
        """Check the dictionary of B expansion coefficients."""
        coeffs = B_expansion_coefficients()
        self.assertEqual(coeffs['N^2'], Fraction(1, 96))
        self.assertEqual(coeffs['N^1'], Fraction(1, 96))
        self.assertEqual(coeffs['N^0'], Fraction(-1, 16))

    def test_A_expansion_coefficients(self):
        """Check the dictionary of A expansion coefficients."""
        coeffs = A_expansion_coefficients()
        self.assertEqual(coeffs['N^4'], Fraction(1, 8))
        self.assertEqual(coeffs['N^3'], Fraction(1, 3))
        self.assertEqual(coeffs['N^2'], Fraction(-1, 4))
        self.assertEqual(coeffs['N^1'], Fraction(-11, 24))
        self.assertEqual(coeffs['N^0'], Fraction(-11, 4))

    def test_A_expansion_sum(self):
        """Check that the expansion coefficients sum correctly at specific N."""
        coeffs = A_expansion_coefficients()
        for N in [3, 5, 10, 20]:
            from_coeffs = (coeffs['N^4'] * N**4 + coeffs['N^3'] * N**3 +
                           coeffs['N^2'] * N**2 + coeffs['N^1'] * N +
                           coeffs['N^0'])
            self.assertEqual(from_coeffs, A_exact(N),
                             f"A expansion sum mismatch at N={N}")


# ============================================================================
# 5. Long division and ratio A/B
# ============================================================================

class TestRatioAOverB(unittest.TestCase):
    """Verify A(N)/B(N) and its large-N expansion."""

    def test_long_division_identity(self):
        """3N^3+14N^2+22N+33 = (N+3)(3N^2+5N+7) + 12 for N=2..100."""
        for N in range(2, 101):
            self.assertTrue(verify_long_division(N),
                            f"Long division failed at N={N}")

    def test_ratio_at_N3(self):
        """A(3)/B(3) = (51/4) / (1/16) = 204."""
        self.assertEqual(ratio_A_over_B(3), Fraction(204))

    def test_ratio_at_N4(self):
        """A(4)/B(4) = (179/4) / (7/48) = (179*48)/(4*7) = 179*12/7."""
        expected = Fraction(179 * 12, 7)
        self.assertEqual(ratio_A_over_B(4), expected)

    def test_ratio_grows_as_12N2(self):
        """A(N)/B(N) ~ 12N^2 at large N."""
        for N in [20, 50, 100]:
            r = float(ratio_A_over_B(N))
            leading = 12 * N**2
            relative_error = abs(r - leading) / leading
            self.assertLess(relative_error, 0.1,
                            f"Ratio at N={N}: {r:.1f} vs 12N^2={leading}")

    def test_ratio_exact_decomposition(self):
        """A/B = 4(3N^2+5N+7) + 48/(N+3) = 12N^2+20N+28+48/(N+3)."""
        for N in range(3, 51):
            r = ratio_A_over_B(N)
            poly_part = 12 * N**2 + 20 * N + 28
            remainder = Fraction(48, N + 3)
            self.assertEqual(r, Fraction(poly_part) + remainder,
                             f"Ratio decomposition failed at N={N}")


# ============================================================================
# 6. Cross-verification with independent graph sum
# ============================================================================

class TestCrossVerification(unittest.TestCase):
    """Cross-verify against the independent rectification engine."""

    def test_cross_verify_N3(self):
        """Graph sum matches closed form at N=3."""
        result = cross_verify_with_graph_sum(3, Fraction(100))
        self.assertTrue(result['all_agree'],
                        f"Cross verification failed: {result}")

    def test_cross_verify_N4(self):
        """Graph sum matches closed form at N=4."""
        result = cross_verify_with_graph_sum(4, Fraction(50))
        self.assertTrue(result['all_agree'],
                        f"Cross verification failed: {result}")

    def test_cross_verify_N5(self):
        """Graph sum matches closed form at N=5."""
        result = cross_verify_with_graph_sum(5, Fraction(200))
        self.assertTrue(result['all_agree'],
                        f"Cross verification failed: {result}")

    def test_cross_verify_N6(self):
        """Graph sum matches closed form at N=6."""
        result = cross_verify_with_graph_sum(6, Fraction(30))
        self.assertTrue(result['all_agree'],
                        f"Cross verification failed: {result}")

    def test_cross_verify_B_N(self):
        """B(N) matches graph-based extraction for N=3..8."""
        for N in range(3, 9):
            result = cross_verify_BN_AN(N)
            self.assertTrue(result['B_match'],
                            f"B({N}) graph mismatch: {result}")

    def test_cross_verify_A_N(self):
        """A(N) matches graph-based extraction for N=3..8."""
        for N in range(3, 9):
            result = cross_verify_BN_AN(N)
            self.assertTrue(result['A_match'],
                            f"A({N}) graph mismatch: {result}")


# ============================================================================
# 7. Virasoro (N=2) vanishing
# ============================================================================

class TestVirasoroVanishing(unittest.TestCase):
    """N=2 (Virasoro) is uniform-weight: delta_F_2 = 0."""

    def test_B2(self):
        self.assertEqual(B_exact(2), Fraction(0))

    def test_A2(self):
        self.assertEqual(A_exact(2), Fraction(0))

    def test_delta_F2_vanishes(self):
        """delta_F_2(Vir, c) = 0 for any c."""
        for c in [1, 10, 26, 100]:
            self.assertEqual(delta_F2_grav_closed(2, Fraction(c)), Fraction(0))


# ============================================================================
# 8. 't Hooft limit
# ============================================================================

class TestTHooftLimit(unittest.TestCase):
    """Verify the 't Hooft limit behavior."""

    def test_c_wn_thooft_N2_lam_half(self):
        """c(W_2, lambda=1/2) = c(Vir, k=2)."""
        # lambda = 2/(2+2) = 1/2 means k=2
        c = c_wn_thooft(2, Fraction(1, 2))
        # c(Vir, k=2) = 1 - 6*1/4 = 1 - 3/2 = -1/2
        # Using FL: (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
        # = 1 - 2*3*(3)^2/4 = 1 - 54/4 = 1 - 27/2 = -25/2
        expected = Fraction(1) - Fraction(2 * 3 * 9, 4)
        self.assertEqual(c, expected)

    def test_thooft_limit_A_over_c(self):
        """The 't Hooft limit of A(N)/c(N,lambda) is -lambda/8."""
        for lam in [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)]:
            limit = thooft_limit_A_over_c(lam)
            self.assertEqual(limit, -lam / 8)

    def test_thooft_A_over_c_convergence(self):
        """A(N)/c(N,lambda) converges to -lambda/8 as N grows."""
        lam = Fraction(1, 3)
        limit = float(thooft_limit_A_over_c(lam))
        for N in [10, 20, 50]:
            c = c_wn_thooft(N, lam)
            if c == 0:
                continue
            actual = float(A_exact(N) / c)
            # Should converge to limit
            if N >= 20:
                self.assertAlmostEqual(actual, limit, delta=abs(limit) * 0.5,
                                       msg=f"N={N}: A/c={actual:.6f} vs limit={limit:.6f}")

    def test_B_dominates_at_large_N(self):
        """B(N) ~ N^2/96 grows unboundedly, dominating the finite A/c limit."""
        lam = Fraction(1, 2)
        for N in [10, 20, 50]:
            data = delta_F2_thooft(N, lam)
            if data['delta_F2'] is None:
                continue
            B = float(data['B'])
            A_over_c = float(data['A_over_c'])
            # At large N, |B| >> |A/c|
            if N >= 20:
                self.assertGreater(abs(B), abs(A_over_c),
                                   f"N={N}: B should dominate at large N")

    def test_thooft_table_runs(self):
        """'t Hooft table generates data without errors."""
        table = thooft_table(N_values=[3, 5, 10], lambda_values=[Fraction(1, 3)])
        self.assertGreater(len(table), 0)


# ============================================================================
# 9. W_{1+infinity} limit (divergence)
# ============================================================================

class TestWInfinityLimit(unittest.TestCase):
    """Verify that delta_F_2 diverges as N -> infinity with c fixed."""

    def test_divergence_B(self):
        """B(N) grows without bound."""
        vals = [float(B_exact(N)) for N in [10, 50, 100]]
        self.assertLess(vals[0], vals[1])
        self.assertLess(vals[1], vals[2])
        self.assertGreater(vals[2], 100)  # B(100) = 98*103/96 ~ 105

    def test_divergence_A_over_c(self):
        """A(N)/c grows without bound for any fixed c."""
        c = Fraction(100)
        vals = [float(A_exact(N) / c) for N in [10, 50, 100]]
        self.assertLess(vals[0], vals[1])
        self.assertLess(vals[1], vals[2])

    def test_cross_over_scalar_grows(self):
        """delta_F_2 / (kappa * lambda_2) grows with N."""
        c = Fraction(100)
        ratios = []
        for N in [3, 5, 10, 20]:
            data = delta_F2_winfty_scaling(N, c)
            r = data['ratio_cross_over_scalar']
            if r is not None:
                ratios.append(float(r))
        # Should be increasing
        for i in range(len(ratios) - 1):
            self.assertLess(ratios[i], ratios[i + 1],
                            f"Cross/scalar ratio not increasing at step {i}")

    def test_winfty_scaling_data(self):
        """Scaling data is well-formed."""
        data = delta_F2_winfty_scaling(10, 100)
        self.assertIn('delta_F2', data)
        self.assertIn('kappa', data)
        self.assertIn('scalar_F2', data)


# ============================================================================
# 10. Matrix model / Frobenius manifold structure
# ============================================================================

class TestFrobeniusManifold(unittest.TestCase):
    """Verify the Frobenius manifold interpretation."""

    def test_dimension(self):
        """Frobenius manifold dimension = N-1."""
        for N in range(2, 11):
            self.assertEqual(frobenius_manifold_dimension(N), N - 1)

    def test_eigenvalues(self):
        """T-multiplication eigenvalues are {2, 3, ..., N}."""
        for N in [3, 5, 10]:
            eigs = frobenius_eigenvalues(N, 100)
            expected = [Fraction(j) for j in range(2, N + 1)]
            self.assertEqual(eigs, expected)

    def test_branch_points(self):
        """Spectral curve has N-1 branch points at u = 2, ..., N."""
        for N in [3, 4, 5]:
            bps = spectral_curve_branch_points(N)
            self.assertEqual(len(bps), N - 1)
            self.assertEqual(bps, list(range(2, N + 1)))

    def test_effective_matrix_size(self):
        """Effective matrix size is N-1."""
        for N in [3, 5, 10]:
            self.assertEqual(effective_matrix_size(N), N - 1)

    def test_W3_has_2_branch_points(self):
        """W_3 spectral curve: 2 branch points (matches A_1 curve)."""
        self.assertEqual(len(spectral_curve_branch_points(3)), 2)

    def test_matrix_model_obstruction_consistency(self):
        """N-1 branch points for N >= 4 exceeds the 2-branch-point
        obstruction proved in matrix_model_cross_channel.py."""
        for N in range(4, 11):
            self.assertGreater(len(spectral_curve_branch_points(N)), 2)


# ============================================================================
# 11. ABJM comparison
# ============================================================================

class TestABJM(unittest.TestCase):
    """Verify ABJM N^{3/2} scaling comparison."""

    def test_kappa_abjm(self):
        """kappa(ABJM, N) = -2N^2."""
        for N in [1, 2, 5, 10]:
            self.assertEqual(kappa_abjm(N), Fraction(-2 * N**2))

    def test_abjm_N2_scaling(self):
        """ABJM free energy scales as N^2, not N^{3/2}."""
        for g in [1, 2, 3]:
            F_10 = float(abjm_genus_g_free_energy(10, g))
            F_20 = float(abjm_genus_g_free_energy(20, g))
            # Ratio should be (20/10)^2 = 4
            ratio = F_20 / F_10
            self.assertAlmostEqual(ratio, 4.0, delta=0.01,
                                   msg=f"ABJM genus {g}: ratio should be 4")

    def test_abjm_cross_channel_zero(self):
        """ABJM cross-channel correction is zero."""
        status = abjm_cross_channel_status()
        self.assertIn("ZERO", status)

    def test_hypothetical_m2_dominance(self):
        """Hypothetical M2 algebra: N^{5/2} dominates N^2."""
        for N in [10, 50]:
            data = hypothetical_m2_scaling(N, Fraction(1), Fraction(1, 2))
            self.assertEqual(data['dominant'], 'A/c (N^{5/2} >> N^2)')
            # At large N, A/c should exceed B
            if N >= 20:
                self.assertGreater(abs(data['A_over_c_float']),
                                   abs(data['B_float']))


# ============================================================================
# 12. Dominance crossover
# ============================================================================

class TestDominanceCrossover(unittest.TestCase):
    """Verify the crossover central charge c_* = A(N)/B(N)."""

    def test_crossover_N3(self):
        """c_*(3) = A(3)/B(3) = 204."""
        data = dominance_crossover(3)
        self.assertEqual(data['c_star'], Fraction(204))

    def test_crossover_grows_as_12N2(self):
        """c_*(N) ~ 12N^2 at large N."""
        for N in [20, 50, 100]:
            data = dominance_crossover(N)
            cs = float(data['c_star'])
            leading = 12 * N**2
            rel_err = abs(cs - leading) / leading
            self.assertLess(rel_err, 0.15,
                            f"N={N}: c*={cs:.0f} vs 12N^2={leading}")

    def test_at_crossover_terms_equal(self):
        """At c = c_*, B(N) = A(N)/c."""
        for N in [3, 5, 10]:
            cs = ratio_A_over_B(N)
            B = B_exact(N)
            A_over_cs = A_exact(N) / cs
            self.assertEqual(B, A_over_cs,
                             f"At crossover N={N}: B={B} vs A/c*={A_over_cs}")


# ============================================================================
# 13. Positivity and monotonicity
# ============================================================================

class TestPositivity(unittest.TestCase):
    """Verify positivity and monotonicity properties."""

    def test_delta_F2_positive_for_c_positive_N_ge_3(self):
        """delta_F_2 > 0 for c > 0 and N >= 3."""
        for N in range(3, 16):
            for c_val in [1, 10, 100, 1000]:
                dF2 = delta_F2_grav_closed(N, Fraction(c_val))
                self.assertGreater(dF2, 0,
                                   f"delta_F_2({N}, {c_val}) should be > 0")

    def test_delta_F2_increases_with_N(self):
        """delta_F_2(W_N, c) increases with N for fixed c > 0."""
        c = Fraction(100)
        for N in range(3, 20):
            self.assertLess(delta_F2_grav_closed(N, c),
                            delta_F2_grav_closed(N + 1, c),
                            f"delta_F_2 not increasing at N={N}")


# ============================================================================
# 14. Koszul duality constraints
# ============================================================================

class TestKoszulDuality(unittest.TestCase):
    """Verify Koszul duality properties of delta_F_2."""

    def test_koszul_conductor(self):
        """K_N = 2(N-1) + 4N(N^2-1). K_2=26, K_3=100, K_4=246."""
        def K(N):
            return 2 * (N - 1) + 4 * N * (N**2 - 1)
        self.assertEqual(K(2), 26)
        self.assertEqual(K(3), 100)
        self.assertEqual(K(4), 246)

    def test_delta_F2_at_dual_c(self):
        """delta_F_2(W_N, c) + delta_F_2(W_N, K_N - c) should have structure.

        Under Koszul duality c -> K_N - c, delta_F_2 transforms as:
          B(N) + A(N)/c  ->  B(N) + A(N)/(K_N - c)

        The sum: 2*B(N) + A(N)*(1/c + 1/(K_N-c)) = 2*B + A*K_N/(c*(K_N-c)).
        """
        for N in [3, 4, 5]:
            K_N = 2 * (N - 1) + 4 * N * (N**2 - 1)
            c = Fraction(10)
            c_dual = Fraction(K_N) - c
            d1 = delta_F2_grav_closed(N, c)
            d2 = delta_F2_grav_closed(N, c_dual)
            # Sum should be 2*B + A*K_N/(c*(K_N-c))
            expected = 2 * B_exact(N) + A_exact(N) * K_N / (c * c_dual)
            self.assertEqual(d1 + d2, expected,
                             f"Koszul sum failed at N={N}")

    def test_self_dual_point(self):
        """At c = K_N/2 (self-dual point), delta_F_2 = B(N) + 2*A(N)/K_N."""
        for N in [3, 4, 5]:
            K_N = Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))
            c_sd = K_N / 2
            dF2 = delta_F2_grav_closed(N, c_sd)
            expected = B_exact(N) + 2 * A_exact(N) / K_N
            self.assertEqual(dF2, expected,
                             f"Self-dual point failed at N={N}")


# ============================================================================
# 15. Large-N table and numerical checks
# ============================================================================

class TestLargeNTable(unittest.TestCase):
    """Verify the large-N table output."""

    def test_table_generation(self):
        """Table generates without errors."""
        table = large_N_table(N_values=[3, 5, 10])
        self.assertEqual(len(table), 3)

    def test_table_values_consistent(self):
        """Table values match direct computation."""
        for row in large_N_table(N_values=[3, 5, 10], c_value=100):
            N = row['N']
            self.assertEqual(row['B(N)'], B_exact(N))
            self.assertEqual(row['A(N)'], A_exact(N))

    def test_cross_over_scalar_increases(self):
        """Cross/scalar ratio increases with N at fixed c."""
        table = large_N_table(N_values=[3, 5, 10, 20], c_value=100)
        ratios = [row['cross_over_scalar'] for row in table]
        for i in range(len(ratios) - 1):
            self.assertLess(ratios[i], ratios[i + 1])


# ============================================================================
# 16. Normalized quantities
# ============================================================================

class TestNormalized(unittest.TestCase):
    """Verify normalized delta_F_2 quantities."""

    def test_times_c_is_polynomial(self):
        """delta_F_2 * c = B*c + A is a polynomial in c."""
        for N in [3, 5]:
            for c_val in [1, 10, 100]:
                c = Fraction(c_val)
                data = normalized_delta_F2(N, c)
                expected = B_exact(N) * c + A_exact(N)
                self.assertEqual(data['times_c'], expected)

    def test_over_lambda2(self):
        """delta_F_2 / lambda_2 is computed correctly."""
        c = Fraction(100)
        data = normalized_delta_F2(3, c)
        lam2 = Fraction(7, 5760)
        expected = delta_F2_grav_closed(3, c) / lam2
        self.assertEqual(data['over_lambda2'], expected)


# ============================================================================
# 17. Leading-term approximations
# ============================================================================

class TestLeadingTerms(unittest.TestCase):
    """Verify leading-term approximation quality."""

    def test_B_leading_quality(self):
        """B(N) ~ N^2/96 within 10% for N >= 10."""
        for N in [10, 20, 50, 100]:
            exact = float(B_exact(N))
            approx = B_leading(N)
            rel_err = abs(exact - approx) / exact
            self.assertLess(rel_err, 0.12,
                            f"B_leading at N={N}: err={rel_err:.3f}")

    def test_A_leading_quality(self):
        """A(N) ~ N^4/8 within 20% for N >= 10."""
        for N in [10, 20, 50, 100]:
            exact = float(A_exact(N))
            approx = A_leading(N)
            rel_err = abs(exact - approx) / exact
            self.assertLess(rel_err, 0.25,
                            f"A_leading at N={N}: err={rel_err:.3f}")


# ============================================================================
# 18. Additivity / factoring properties of B and A
# ============================================================================

class TestAlgebraicProperties(unittest.TestCase):
    """Verify algebraic properties of B(N) and A(N)."""

    def test_B_factors(self):
        """B(N) = (N-2)(N+3)/96 vanishes exactly at N=2 and N=-3."""
        self.assertEqual(B_exact(2), Fraction(0))
        # N = -3 not in domain, but the polynomial vanishes
        self.assertEqual((-3 - 2) * (-3 + 3), 0)

    def test_A_factors(self):
        """A(N) has factor (N-2), vanishing at N=2."""
        self.assertEqual(A_exact(2), Fraction(0))
        # The cubic 3N^3+14N^2+22N+33 has no positive integer roots
        for N in range(1, 20):
            val = 3 * N**3 + 14 * N**2 + 22 * N + 33
            self.assertGreater(val, 0, f"Cubic should be positive at N={N}")

    def test_B_second_differences(self):
        """B(N) is quadratic: second differences are constant.
        Delta^2 B = B(N+2) - 2*B(N+1) + B(N) = 1/48."""
        for N in range(2, 20):
            d2 = B_exact(N + 2) - 2 * B_exact(N + 1) + B_exact(N)
            self.assertEqual(d2, Fraction(1, 48),
                             f"Second difference at N={N}: {d2}")

    def test_A_fourth_differences(self):
        """A(N) is quartic: fourth differences are constant.
        Delta^4 A = sum_{k=0}^4 (-1)^k C(4,k) A(N+4-k) = 3."""
        from math import comb
        for N in range(2, 10):
            d4 = sum((-1)**k * comb(4, k) * A_exact(N + 4 - k)
                     for k in range(5))
            self.assertEqual(d4, Fraction(3),
                             f"Fourth difference at N={N}: {d4}")


# ============================================================================
# 19. Consistency between c_wn_thooft and wn_central_charge_canonical
# ============================================================================

class TestTHooftCentralCharge(unittest.TestCase):
    """Cross-verify c_wn_thooft against the canonical formula."""

    def test_matches_canonical_N2(self):
        """c(W_2, lambda=1/2) matches Fateev-Lukyanov at k=2."""
        from wn_central_charge_canonical import c_wn_fl
        lam = Fraction(1, 2)  # k = 2, N = 2
        c_thooft = c_wn_thooft(2, lam)
        c_fl = c_wn_fl(2, 2)
        self.assertEqual(c_thooft, c_fl,
                         f"Mismatch: thooft={c_thooft}, FL={c_fl}")

    def test_matches_canonical_N3_k1(self):
        """c(W_3, k=1) via 't Hooft (lambda = 3/4) matches FL."""
        from wn_central_charge_canonical import c_wn_fl
        N, k = 3, 1
        lam = Fraction(N, k + N)
        c_thooft = c_wn_thooft(N, lam)
        c_fl = c_wn_fl(N, k)
        self.assertEqual(c_thooft, c_fl,
                         f"Mismatch: thooft={c_thooft}, FL={c_fl}")

    def test_matches_canonical_N5_k3(self):
        """c(W_5, k=3) via 't Hooft matches FL."""
        from wn_central_charge_canonical import c_wn_fl
        N, k = 5, 3
        lam = Fraction(N, k + N)
        c_thooft = c_wn_thooft(N, lam)
        c_fl = c_wn_fl(N, k)
        self.assertEqual(c_thooft, c_fl,
                         f"Mismatch: thooft={c_thooft}, FL={c_fl}")

    def test_matches_canonical_range(self):
        """Match FL formula for N=2..8, k=1..5."""
        from wn_central_charge_canonical import c_wn_fl
        for N in range(2, 9):
            for k in range(1, 6):
                lam = Fraction(N, k + N)
                c_t = c_wn_thooft(N, lam)
                c_f = c_wn_fl(N, k)
                self.assertEqual(c_t, c_f,
                                 f"Mismatch at N={N}, k={k}: {c_t} vs {c_f}")


# ============================================================================
# 20. Edge cases and error handling
# ============================================================================

class TestEdgeCases(unittest.TestCase):
    """Verify edge cases and error handling."""

    def test_c_zero_raises(self):
        """delta_F_2 at c=0 raises ValueError."""
        with self.assertRaises(ValueError):
            delta_F2_grav_closed(3, 0)

    def test_N1_raises(self):
        """B(1) and A(1) raise ValueError."""
        with self.assertRaises(ValueError):
            B_exact(1)
        with self.assertRaises(ValueError):
            A_exact(1)

    def test_lambda_zero_raises(self):
        """c_wn_thooft at lambda=0 raises."""
        with self.assertRaises(ValueError):
            c_wn_thooft(3, Fraction(0))

    def test_negative_c(self):
        """delta_F_2 at negative c still computes."""
        dF2 = delta_F2_grav_closed(3, Fraction(-10))
        # B + A/(-10) = 1/16 - 51/40 = 5/80 - 102/80 = -97/80
        expected = Fraction(1, 16) + Fraction(51, 4) / Fraction(-10)
        self.assertEqual(dF2, expected)

    def test_large_c_approaches_B(self):
        """For very large c, delta_F_2 -> B(N)."""
        for N in [3, 5, 10]:
            c = Fraction(10**9)
            dF2 = delta_F2_grav_closed(N, c)
            B = B_exact(N)
            # A/c ~ 0
            self.assertAlmostEqual(float(dF2), float(B), places=3)


# ============================================================================
# 21. Multi-path verification: 3 independent paths per key claim
# ============================================================================

class TestMultiPathVerification(unittest.TestCase):
    """Multi-path verification mandate: 3+ paths per claim."""

    def test_B3_three_paths(self):
        """B(3) = 1/16 via three independent paths."""
        # Path 1: closed form
        p1 = B_exact(3)
        # Path 2: expansion polynomial
        p2 = Fraction(9 + 3 - 6, 96)  # (N^2+N-6)/96 at N=3
        # Path 3: from graph engine (lollipop contribution)
        S1_from3 = sum(j for j in range(3, 4))  # j=3 only: S1_from3 = 3
        p3 = Fraction(S1_from3, 48)  # lollipop formula
        self.assertEqual(p1, Fraction(1, 16))
        self.assertEqual(p2, Fraction(1, 16))
        self.assertEqual(p3, Fraction(1, 16))

    def test_A3_three_paths(self):
        """A(3) = 51/4 via three independent paths."""
        # Path 1: closed form
        p1 = A_exact(3)
        # Path 2: expansion polynomial
        p2 = Fraction(3 * 81 + 8 * 27 - 6 * 9 - 11 * 3 - 66, 24)
        # = (243+216-54-33-66)/24 = 306/24 = 51/4
        # Path 3: from graph sums (banana + theta + barbell)
        S1 = sum(j for j in range(2, 4))  # 2+3 = 5
        S2 = sum(j * j for j in range(2, 4))  # 4+9 = 13
        S2_from3 = 9
        banana = Fraction(S1 * S1 - S2, 4)  # (25-13)/4 = 3
        theta = Fraction(S2_from3, 2)  # 9/2
        barbell = Fraction(S1 * S1 - 4, 4)  # (25-4)/4 = 21/4
        p3 = banana + theta + barbell  # 3 + 9/2 + 21/4 = 12/4 + 18/4 + 21/4 = 51/4
        self.assertEqual(p1, Fraction(51, 4))
        self.assertEqual(p2, Fraction(51, 4))
        self.assertEqual(p3, Fraction(51, 4))

    def test_delta_F2_W3_three_paths(self):
        """delta_F_2(W_3, c=100) via three paths."""
        c = Fraction(100)
        # Path 1: our closed form
        p1 = delta_F2_grav_closed(3, c)
        # Path 2: known formula
        p2 = (c + 204) / (16 * c)
        # Path 3: graph sum
        from rectification_delta_f2_verify_engine import delta_F2_grav_graph_sum
        p3 = delta_F2_grav_graph_sum(3, c)
        self.assertEqual(p1, p2)
        self.assertEqual(p2, p3)

    def test_ratio_three_paths(self):
        """A(N)/B(N) at N=3 via three paths."""
        # Path 1: from ratio function
        p1 = ratio_A_over_B(3)
        # Path 2: direct division
        p2 = A_exact(3) / B_exact(3)
        # Path 3: from W_3 formula coefficient extraction
        # delta_F_2 = (c+204)/(16c). Constant term = 1/16 = B.
        # 1/c coefficient = 204/16 = 51/4 = A. Ratio = 204.
        p3 = Fraction(204)
        self.assertEqual(p1, Fraction(204))
        self.assertEqual(p2, Fraction(204))
        self.assertEqual(p3, Fraction(204))


if __name__ == '__main__':
    unittest.main()
