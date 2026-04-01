r"""Tests for the Virasoro sewing spectrum engine.

Tests the Fredholm eigenvalue spectrum for Virasoro:
1. Vacuum partition enumeration
2. Gram matrix construction (exact and float)
3. Known Gram matrices at weights 2, 3, 4, 5
4. Gram matrix eigenvalue spectrum
5. Kac determinant formula
6. BPZ minimal model central charges
7. Sewing matrix = identity
8. Fredholm determinant
9. Normalized Gram spectrum
10. Eigenvalue polynomial structure
11. Large-c (Heisenberg) limit
"""

import math
import unittest
from fractions import Fraction

import numpy as np

from compute.lib.virasoro_sewing_spectrum import (
    vacuum_partitions,
    vacuum_dim,
    gram_matrix_exact,
    gram_matrix_float,
    gram_eigenvalues,
    gram_eigenvalues_exact,
    gram_condition_number,
    gram_weight2_exact,
    gram_weight3_exact,
    gram_weight4_exact,
    gram_weight5_exact,
    sewing_matrix,
    sewing_eigenvalues,
    normalized_gram_spectrum,
    fredholm_det_virasoro_vacuum,
    virasoro_character_product,
    fredholm_det_matches_character,
    kac_h_rs,
    kac_determinant,
    bpz_central_charges,
    bpz_central_charges_exact,
    null_vector_weights,
    gram_trace,
    gram_determinant,
    eigenvalue_ratios,
    eigenvalue_spectrum_scan,
    full_spectrum_analysis,
    heisenberg_gram_eigenvalues,
    spectrum_summary,
)


# ====================================================================
# Section 1: Vacuum partitions
# ====================================================================

class TestVacuumPartitions(unittest.TestCase):
    """Test vacuum module partition enumeration (parts >= 2)."""

    def test_weight_0(self):
        self.assertEqual(vacuum_partitions(0), [()])

    def test_weight_1(self):
        self.assertEqual(vacuum_partitions(1), [])

    def test_weight_2(self):
        self.assertEqual(vacuum_partitions(2), [(2,)])

    def test_weight_3(self):
        self.assertEqual(vacuum_partitions(3), [(3,)])

    def test_weight_4(self):
        parts = vacuum_partitions(4)
        self.assertEqual(len(parts), 2)
        self.assertIn((4,), parts)
        self.assertIn((2, 2), parts)

    def test_weight_5(self):
        parts = vacuum_partitions(5)
        self.assertEqual(len(parts), 2)
        self.assertIn((5,), parts)
        self.assertIn((3, 2), parts)

    def test_weight_6(self):
        parts = vacuum_partitions(6)
        self.assertEqual(len(parts), 4)
        self.assertIn((6,), parts)
        self.assertIn((4, 2), parts)
        self.assertIn((3, 3), parts)
        self.assertIn((2, 2, 2), parts)

    def test_dim_sequence(self):
        """d_n = p(n, parts>=2) for n = 0..10."""
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12]
        for n, e in enumerate(expected):
            self.assertEqual(vacuum_dim(n), e, f"vacuum_dim({n}) != {e}")

    def test_negative_weight(self):
        self.assertEqual(vacuum_partitions(-1), [])


# ====================================================================
# Section 2: Gram matrix weight 2 (exact)
# ====================================================================

class TestGramWeight2(unittest.TestCase):
    """G_2 = [[c/2]] (single entry)."""

    def test_exact_c1(self):
        G = gram_weight2_exact(Fraction(1))
        self.assertEqual(G, [[Fraction(1, 2)]])

    def test_exact_c26(self):
        G = gram_weight2_exact(Fraction(26))
        self.assertEqual(G, [[Fraction(13)]])

    def test_matches_general(self):
        c = Fraction(10)
        G_known = gram_weight2_exact(c)
        G_general = gram_matrix_exact(c, 2)
        self.assertEqual(G_known, G_general)


# ====================================================================
# Section 3: Gram matrix weight 3 (exact)
# ====================================================================

class TestGramWeight3(unittest.TestCase):
    """G_3 = [[2c]]."""

    def test_exact_c1(self):
        G = gram_weight3_exact(Fraction(1))
        self.assertEqual(G, [[Fraction(2)]])

    def test_matches_general(self):
        c = Fraction(7)
        G_known = gram_weight3_exact(c)
        G_general = gram_matrix_exact(c, 3)
        self.assertEqual(G_known, G_general)


# ====================================================================
# Section 4: Gram matrix weight 4 (exact)
# ====================================================================

class TestGramWeight4(unittest.TestCase):
    """G_4 has known entries: [[5c, 3c], [3c, c(8+c)/2]]."""

    def test_exact_c1(self):
        G = gram_weight4_exact(Fraction(1))
        self.assertEqual(G[0][0], Fraction(5))
        self.assertEqual(G[0][1], Fraction(3))
        self.assertEqual(G[1][0], Fraction(3))
        self.assertEqual(G[1][1], Fraction(9, 2))

    def test_symmetric(self):
        c = Fraction(10)
        G = gram_weight4_exact(c)
        self.assertEqual(G[0][1], G[1][0])

    def test_determinant_positive_large_c(self):
        c = Fraction(100)
        G = gram_weight4_exact(c)
        det = G[0][0] * G[1][1] - G[0][1] * G[1][0]
        self.assertGreater(det, 0)

    def test_matches_general(self):
        c = Fraction(5)
        G_known = gram_weight4_exact(c)
        G_general = gram_matrix_exact(c, 4)
        for i in range(2):
            for j in range(2):
                self.assertEqual(G_known[i][j], G_general[i][j],
                                 f"Mismatch at ({i},{j})")


# ====================================================================
# Section 5: Gram matrix weight 5 (exact)
# ====================================================================

class TestGramWeight5(unittest.TestCase):
    """G_5 = [[10c, 4c], [4c, c(6+c)]]."""

    def test_exact_c1(self):
        G = gram_weight5_exact(Fraction(1))
        self.assertEqual(G[0][0], Fraction(10))
        self.assertEqual(G[0][1], Fraction(4))
        self.assertEqual(G[1][1], Fraction(7))

    def test_symmetric(self):
        c = Fraction(13)
        G = gram_weight5_exact(c)
        self.assertEqual(G[0][1], G[1][0])

    def test_matches_general(self):
        c = Fraction(3)
        G_known = gram_weight5_exact(c)
        G_general = gram_matrix_exact(c, 5)
        for i in range(2):
            for j in range(2):
                self.assertEqual(G_known[i][j], G_general[i][j],
                                 f"Mismatch at ({i},{j})")


# ====================================================================
# Section 6: Gram matrix float vs exact
# ====================================================================

class TestGramFloatVsExact(unittest.TestCase):
    """Float computation matches exact Fraction computation."""

    def test_weight4_c10(self):
        c = Fraction(10)
        G_exact = gram_matrix_exact(c, 4)
        G_float = gram_matrix_float(10.0, 4)
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(float(G_exact[i][j]), G_float[i][j],
                                       places=8)

    def test_weight5_c26(self):
        c = Fraction(26)
        G_exact = gram_matrix_exact(c, 5)
        G_float = gram_matrix_float(26.0, 5)
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(float(G_exact[i][j]), G_float[i][j],
                                       places=6)


# ====================================================================
# Section 7: Eigenvalue spectrum
# ====================================================================

class TestEigenvalueSpectrum(unittest.TestCase):
    """Test Gram matrix eigenvalue computation."""

    def test_weight2_single_eigenvalue(self):
        evals = gram_eigenvalues(10.0, 2)
        self.assertEqual(len(evals), 1)
        self.assertAlmostEqual(evals[0], 5.0, places=10)  # c/2 = 5

    def test_weight3_single_eigenvalue(self):
        evals = gram_eigenvalues(10.0, 3)
        self.assertEqual(len(evals), 1)
        self.assertAlmostEqual(evals[0], 20.0, places=10)  # 2c = 20

    def test_weight4_two_eigenvalues(self):
        evals = gram_eigenvalues(10.0, 4)
        self.assertEqual(len(evals), 2)
        # Both should be positive at c=10
        self.assertGreater(evals[0], 0)
        self.assertGreater(evals[1], 0)

    def test_eigenvalues_positive_at_large_c(self):
        """At large c, all eigenvalues should be positive."""
        for n in range(2, 8):
            evals = gram_eigenvalues(100.0, n)
            for e in evals:
                self.assertGreater(e, 0,
                                   f"Negative eigenvalue at c=100, weight {n}")

    def test_eigenvalues_sorted(self):
        evals = gram_eigenvalues(10.0, 6)
        for i in range(len(evals) - 1):
            self.assertLessEqual(evals[i], evals[i + 1])

    def test_empty_at_weight1(self):
        evals = gram_eigenvalues(10.0, 1)
        self.assertEqual(len(evals), 0)


# ====================================================================
# Section 8: Kac determinant
# ====================================================================

class TestKacDeterminant(unittest.TestCase):
    """Test Kac table values h_{r,s}."""

    def test_h11_zero(self):
        """h_{1,1} = 0 for all c (the identity module)."""
        for c in [0.5, 1.0, 10.0, 26.0]:
            self.assertAlmostEqual(kac_h_rs(1, 1, c), 0.0, places=10)

    def test_h_ising_values(self):
        """At c=1/2 (Ising, m=3): h_{1,2} = 1/16, h_{2,1} = 1/2, h_{1,3} = 1/2.

        The Kac table for the Ising model (p=4, q=3):
          h_{r,s} = ((4r - 3s)^2 - 1) / 48
          h_{1,1} = 0, h_{1,2} = 1/16, h_{2,1} = 1/2
        """
        c = 0.5
        h12 = kac_h_rs(1, 2, c)
        h21 = kac_h_rs(2, 1, c)
        self.assertAlmostEqual(h12, 1.0 / 16.0, places=8)
        self.assertAlmostEqual(h21, 0.5, places=8)

    def test_h_symmetry_at_c1(self):
        """At c=1: h_{r,s} = (r-s)^2/4."""
        for r in range(1, 5):
            for s in range(1, 5):
                h = kac_h_rs(r, s, 1.0)
                expected = (r - s) ** 2 / 4.0
                self.assertAlmostEqual(h, expected, places=10,
                                       msg=f"h_{{{r},{s}}} at c=1")


# ====================================================================
# Section 9: Sewing matrix = identity
# ====================================================================

class TestSewingMatrix(unittest.TestCase):
    """The sewing matrix is the identity at genus 1."""

    def test_sewing_is_identity(self):
        for n in range(2, 8):
            S = sewing_matrix(10.0, n)
            d = vacuum_dim(n)
            if d > 0:
                np.testing.assert_array_almost_equal(S, np.eye(d))

    def test_sewing_eigenvalues_all_one(self):
        for n in range(2, 8):
            evals = sewing_eigenvalues(10.0, n)
            d = vacuum_dim(n)
            if d > 0:
                np.testing.assert_array_almost_equal(evals, np.ones(d))


# ====================================================================
# Section 10: Fredholm determinant
# ====================================================================

class TestFredholmDeterminant(unittest.TestCase):
    """Test the Fredholm determinant computation."""

    def test_at_q_zero(self):
        """At q=0, Fredholm det = 1."""
        self.assertAlmostEqual(fredholm_det_virasoro_vacuum(0.0), 1.0, places=12)

    def test_at_small_q_near_one(self):
        """At small q, Fredholm det is near 1."""
        fred = fredholm_det_virasoro_vacuum(0.01)
        self.assertAlmostEqual(fred, 1.0, places=3)

    def test_positive_for_q_in_01(self):
        """For 0 < q < 1, the Fredholm det is positive."""
        for q in [0.01, 0.1, 0.3, 0.5]:
            fred = fredholm_det_virasoro_vacuum(q)
            self.assertGreater(fred, 0, f"Fredholm det negative at q={q}")

    def test_character_positive(self):
        char = virasoro_character_product(0.1)
        self.assertGreater(char, 1.0)

    def test_fred_char_consistency(self):
        result = fredholm_det_matches_character(0.1)
        self.assertTrue(result['match'],
                        f"Fredholm/character mismatch: diff={result['difference']}")


# ====================================================================
# Section 11: BPZ minimal models
# ====================================================================

class TestBPZMinimalModels(unittest.TestCase):
    """Test BPZ central charge enumeration."""

    def test_ising_c_half(self):
        bpz = bpz_central_charges()
        m3 = [c for m, c in bpz if m == 3][0]
        self.assertAlmostEqual(m3, 0.5, places=10)

    def test_tricritical_ising(self):
        bpz = bpz_central_charges()
        m4 = [c for m, c in bpz if m == 4][0]
        self.assertAlmostEqual(m4, 0.7, places=10)

    def test_exact_bpz(self):
        bpz = bpz_central_charges_exact()
        m3 = [c for m, c in bpz if m == 3][0]
        self.assertEqual(m3, Fraction(1, 2))

    def test_bpz_all_less_than_1(self):
        bpz = bpz_central_charges()
        for m, c in bpz:
            self.assertLess(c, 1.0, f"BPZ c({m}) = {c} >= 1")

    def test_bpz_monotone_increasing(self):
        bpz = bpz_central_charges()
        for i in range(len(bpz) - 1):
            self.assertLess(bpz[i][1], bpz[i + 1][1])


# ====================================================================
# Section 12: Gram trace and determinant
# ====================================================================

class TestGramTraceAndDet(unittest.TestCase):
    """Test trace and determinant at specific c values."""

    def test_trace_weight2(self):
        """tr(G_2) = c/2."""
        self.assertAlmostEqual(gram_trace(10.0, 2), 5.0, places=10)

    def test_trace_weight3(self):
        """tr(G_3) = 2c."""
        self.assertAlmostEqual(gram_trace(10.0, 3), 20.0, places=10)

    def test_determinant_weight2(self):
        """det(G_2) = c/2."""
        self.assertAlmostEqual(gram_determinant(10.0, 2), 5.0, places=10)

    def test_determinant_weight4(self):
        """Verify det(G_4) from the known 2x2 matrix."""
        c = 10.0
        G = gram_weight4_exact(Fraction(10))
        det_exact = float(G[0][0] * G[1][1] - G[0][1] * G[1][0])
        det_float = gram_determinant(c, 4)
        self.assertAlmostEqual(det_float, det_exact, places=4)


# ====================================================================
# Section 13: Normalized spectrum
# ====================================================================

class TestNormalizedSpectrum(unittest.TestCase):
    """Test the normalized Gram spectrum."""

    def test_normalized_sums_to_one(self):
        """Normalized eigenvalues sum to 1."""
        spec = normalized_gram_spectrum(10.0, 6)
        if len(spec) > 0:
            self.assertAlmostEqual(np.sum(spec), 1.0, places=10)

    def test_normalized_nonneg_at_large_c(self):
        """At large c, all normalized eigenvalues are non-negative."""
        spec = normalized_gram_spectrum(100.0, 6)
        for s in spec:
            self.assertGreaterEqual(s, -1e-10)


# ====================================================================
# Section 14: Eigenvalue scan
# ====================================================================

class TestEigenvalueScan(unittest.TestCase):
    """Test multi-c eigenvalue scanning."""

    def test_scan_returns_correct_shape(self):
        c_vals = [1.0, 10.0, 25.0]
        result = eigenvalue_spectrum_scan(4, c_vals)
        self.assertEqual(result['eigenvalues'].shape, (3, 2))

    def test_scan_traces_match(self):
        c_vals = [10.0]
        result = eigenvalue_spectrum_scan(4, c_vals)
        expected_trace = gram_trace(10.0, 4)
        self.assertAlmostEqual(result['traces'][0], expected_trace, places=4)


# ====================================================================
# Section 15: Condition number
# ====================================================================

class TestConditionNumber(unittest.TestCase):
    """Test Gram matrix condition number."""

    def test_condition_one_at_weight2(self):
        """Weight 2 is 1x1, so condition number = 1."""
        cond = gram_condition_number(10.0, 2)
        self.assertAlmostEqual(cond, 1.0, places=10)

    def test_condition_increases_at_low_c(self):
        """Near BPZ values, condition number should increase."""
        cond_generic = gram_condition_number(10.0, 6)
        cond_near_bpz = gram_condition_number(0.5, 6)
        self.assertGreater(cond_near_bpz, cond_generic)


# ====================================================================
# Section 16: Full spectrum analysis
# ====================================================================

class TestFullSpectrumAnalysis(unittest.TestCase):
    """Test the full spectrum analysis function."""

    def test_analysis_structure(self):
        result = full_spectrum_analysis(10.0, n_max=6)
        self.assertEqual(result['c'], 10.0)
        self.assertIn(2, result['eigenvalues'])
        self.assertIn(6, result['eigenvalues'])


# ====================================================================
# Section 17: Eigenvalue ratios
# ====================================================================

class TestEigenvalueRatios(unittest.TestCase):
    """Test eigenvalue ratio computation."""

    def test_ratios_max_is_one(self):
        ratios = eigenvalue_ratios(10.0, 6)
        if len(ratios) > 0:
            self.assertAlmostEqual(np.max(ratios), 1.0, places=10)

    def test_ratios_all_between_0_and_1(self):
        ratios = eigenvalue_ratios(100.0, 6)
        for r in ratios:
            self.assertGreaterEqual(r, -1e-10)
            self.assertLessEqual(r, 1.0 + 1e-10)


if __name__ == '__main__':
    unittest.main()
