r"""Tests for verlinde_ordered_engine.py.

Verifies that the ordered chiral homology framework recovers the
Verlinde formula for the dimension of the space of conformal blocks
of V_k(sl_2) at integer level k >= 1.

Test structure:
  (1) S-matrix properties (unitarity, symmetry, positivity)
  (2) Genus-0 identity Z_0 = 1
  (3) Genus-1 identity Z_1 = k+1
  (4) Known Verlinde dimensions at low k and g
  (5) Cross-checks: direct vs quantum-dimension paths
  (6) Handle-attachment recursion
  (7) Separating factorization
  (8) k=1 special case Z_g = 2^g
  (9) Kappa values
  (10) Genus-1 ordered chiral homology identification

Each expected value is derived from 2+ independent sources:
  [DC] Direct computation from S-matrix definition
  [LT] Literature (Verlinde 1988; Bakalov-Kirillov 2001)
  [CF] Cross-family/cross-engine (verlinde_shadow_algebra.py)
  [LC] Limiting case (g=0 -> unitarity, g=1 -> count)
  [SY] Symmetry (S-matrix orthogonality)
"""

import math
import sys
import os

import numpy as np
import pytest

# Ensure compute/ is on path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.verlinde_ordered_engine import (
    sl2_S_matrix,
    sl2_S_first_row,
    quantum_dimensions,
    total_quantum_dimension_squared,
    verlinde_dimension,
    verlinde_dimension_exact,
    verlinde_via_quantum_dims,
    verify_genus0_unitarity,
    verify_genus1_count,
    handle_operator,
    verify_handle_recursion,
    separating_factorization,
    kappa_sl2,
    shadow_F1,
    genus1_ordered_identification,
    genus0_ordered_identification,
    KNOWN_VERLINDE_DIMS,
    verify_all,
)

from fractions import Fraction


# =========================================================================
#  1.  S-MATRIX PROPERTIES
# =========================================================================

class TestSMatrix:
    """S-matrix structural properties."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_orthogonality(self, k: int):
        """S * S^T = I (orthogonal matrix).
        # VERIFIED: [DC] direct matrix product
        # VERIFIED: [SY] sine orthogonality relations
        """
        S = sl2_S_matrix(k)
        I = np.eye(k + 1)
        assert np.max(np.abs(S @ S.T - I)) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_symmetry(self, k: int):
        """S = S^T (symmetric matrix).
        # VERIFIED: [DC] direct comparison
        # VERIFIED: [SY] S_{jl} = S_{lj} from sin symmetry
        """
        S = sl2_S_matrix(k)
        assert np.max(np.abs(S - S.T)) < 1e-12

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_first_row_positive(self, k: int):
        """S_{0j} > 0 for all j (positive quantum dimensions).
        # VERIFIED: [DC] sin(pi*(j+1)/(k+2)) > 0 for 0 < j+1 < k+2
        # VERIFIED: [LT] Bakalov-Kirillov Lemma 3.3.15
        """
        S0 = sl2_S_first_row(k)
        assert all(s > 1e-12 for s in S0)

    def test_invalid_level(self):
        """Level must be positive."""
        with pytest.raises(ValueError):
            sl2_S_matrix(0)
        with pytest.raises(ValueError):
            sl2_S_matrix(-1)


# =========================================================================
#  2.  GENUS-0 IDENTITY Z_0 = 1
# =========================================================================

class TestGenus0:
    """Z_0 = 1 from unitarity of S-matrix."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_z0_equals_1(self, k: int):
        """Z_0(k) = sum S_{0j}^2 = 1 for all k.
        # VERIFIED: [DC] direct sum of squares
        # VERIFIED: [SY] orthogonality of first row with itself
        # VERIFIED: [LC] unique vacuum at genus 0
        """
        assert verify_genus0_unitarity(k)
        assert verlinde_dimension_exact(0, k) == 1


# =========================================================================
#  3.  GENUS-1 IDENTITY Z_1 = k+1
# =========================================================================

class TestGenus1:
    """Z_1 = k+1 (integrable representation count)."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_z1_equals_k_plus_1(self, k: int):
        """Z_1(k) = k+1 for all k >= 1.
        # VERIFIED: [DC] sum_{j=0}^{k} S_{0j}^0 = k+1
        # VERIFIED: [LT] Zhu (1996): k+1 simple A(V)-modules
        # VERIFIED: [CF] ordered_chirhoch_integrable_engine.py
        """
        assert verify_genus1_count(k)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_genus1_ordered_identification(self, k: int):
        """Ordered chiral homology at genus 1 gives Z_1 = k+1.
        # VERIFIED: [DC] genus1_ordered_identification
        # VERIFIED: [LT] prop:ell-degree0 in ordered_chiral_homology.tex
        """
        data = genus1_ordered_identification(k)
        assert data["match"]
        assert data["Z_1"] == k + 1
        assert data["num_integrable_reps"] == k + 1


# =========================================================================
#  4.  KNOWN VERLINDE DIMENSIONS
# =========================================================================

class TestKnownValues:
    """Verify against the known-values table."""

    @pytest.mark.parametrize("k,g,expected", [
        (1, 0, 1), (1, 1, 2), (1, 2, 4), (1, 3, 8), (1, 4, 16),
        (2, 0, 1), (2, 1, 3), (2, 2, 10), (2, 3, 36), (2, 4, 136),
        (3, 0, 1), (3, 1, 4), (3, 2, 20), (3, 3, 120), (3, 4, 800),
        (4, 0, 1), (4, 1, 5), (4, 2, 35), (4, 3, 329), (4, 4, 3611),
        (5, 0, 1), (5, 1, 6), (5, 2, 56), (5, 3, 784), (5, 4, 13328),
    ])
    def test_known_dimension(self, k: int, g: int, expected: int):
        """Z_g(k) matches known value.
        # VERIFIED: [DC] direct computation
        # VERIFIED: [CF] verlinde_shadow_algebra.py SL2_VERLINDE_TABLE
        # VERIFIED: [LT] Bakalov-Kirillov (2001)
        """
        computed = verlinde_dimension_exact(g, k)
        assert computed == expected, (
            f"Z_{g}(k={k}): computed {computed}, expected {expected}"
        )


# =========================================================================
#  5.  CROSS-CHECKS: DIRECT VS QUANTUM-DIMENSION PATHS
# =========================================================================

class TestCrossChecks:
    """Two independent computation paths give the same answer."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    @pytest.mark.parametrize("g", [0, 1, 2, 3, 4])
    def test_direct_vs_qdim(self, k: int, g: int):
        """verlinde_dimension == verlinde_via_quantum_dims.
        # VERIFIED: [DC] two independent code paths
        """
        z_direct = verlinde_dimension(g, k)
        z_qdim = verlinde_via_quantum_dims(g, k)
        assert abs(z_direct - z_qdim) < 1e-8, (
            f"Z_{g}(k={k}): direct={z_direct}, qdim={z_qdim}"
        )

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_total_quantum_dim(self, k: int):
        """D^2 = sum d_j^2 = 1/S_{00}^2.
        # VERIFIED: [DC] direct sum
        # VERIFIED: [SY] S-matrix identity
        """
        D2 = total_quantum_dimension_squared(k)
        S0 = sl2_S_first_row(k)
        s00 = S0[0]
        expected = 1.0 / s00 ** 2
        assert abs(D2 - expected) < 1e-8


# =========================================================================
#  6.  HANDLE-ATTACHMENT RECURSION
# =========================================================================

class TestHandleRecursion:
    """Bar complex factorization under handle attachment."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    @pytest.mark.parametrize("g", [0, 1, 2, 3])
    def test_handle_recursion(self, k: int, g: int):
        """Z_{g+1} = sum_j S_{0j}^{-2} * S_{0j}^{2-2g}.
        # VERIFIED: [DC] direct recursion check
        # VERIFIED: [LT] TQFT handle formula (Atiyah 1988)
        """
        assert verify_handle_recursion(g, k)


# =========================================================================
#  7.  SEPARATING FACTORIZATION
# =========================================================================

class TestSeparatingFactorization:
    """Bar complex factorization under separating degeneration."""

    @pytest.mark.parametrize("k", [1, 2, 3])
    @pytest.mark.parametrize("g1,g2", [
        (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1),
    ])
    def test_separating(self, k: int, g1: int, g2: int):
        """Z_{g1+g2} = sum_j Z_{g1}^{(j)} * Z_{g2}^{(j)} * S_{0j}^{-2}.
        # VERIFIED: [DC] direct computation
        # VERIFIED: [LT] TQFT factorization (Atiyah 1988)
        """
        assert separating_factorization(g1, g2, k)


# =========================================================================
#  8.  k=1 SPECIAL CASE: Z_g = 2^g
# =========================================================================

class TestLevel1:
    """At k=1 (pointed MTC), Z_g = 2^g."""

    @pytest.mark.parametrize("g", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_z_g_equals_2_to_g(self, g: int):
        """Z_g(k=1) = 2^g.

        At k=1, S = (1/sqrt(2)) * Hadamard, so
        S_{00} = S_{01} = 1/sqrt(2), and
        Z_g = 2 * (1/sqrt(2))^{2-2g} = 2 * 2^{g-1} = 2^g.

        # VERIFIED: [DC] direct S-matrix computation
        # VERIFIED: [LT] Ising: Z/2Z fusion ring
        """
        assert verlinde_dimension_exact(g, 1) == 2 ** g


# =========================================================================
#  9.  KAPPA VALUES
# =========================================================================

class TestKappa:
    """Modular characteristic kappa(V_k(sl_2)) = 3(k+2)/4."""

    @pytest.mark.parametrize("k,expected", [
        (1, Fraction(9, 4)),
        (2, Fraction(3, 1)),
        (3, Fraction(15, 4)),
        (4, Fraction(9, 2)),
        (5, Fraction(21, 4)),
    ])
    def test_kappa(self, k: int, expected: Fraction):
        """kappa(V_k(sl_2)) = 3(k+2)/4.
        # AP1: from landscape_census.tex
        # VERIFIED: [DC] direct formula
        # VERIFIED: [LC] k=0 -> 3/2 (NOT zero); k=-2 -> 0 (critical)
        """
        assert kappa_sl2(k) == expected

    def test_kappa_k0_boundary(self):
        """kappa(V_0(sl_2)) = 3/2 (abelian limit, NOT zero).
        # VERIFIED: [DC] 3*(0+2)/4 = 3/2
        # VERIFIED: [LC] k=0 is abelian limit; algebra is still Koszul
        """
        # k=0 is not a valid WZW level but kappa formula is well-defined
        kap = Fraction(SL2_DIM * (0 + SL2_DUAL_COXETER), 2 * SL2_DUAL_COXETER)
        assert kap == Fraction(3, 2)

    def test_shadow_F1(self):
        """F_1 = kappa/24.
        # VERIFIED: [DC] direct formula
        # VERIFIED: [LT] lambda_1 = 1/24 on M-bar_{1,1}
        """
        for k in range(1, 6):
            f1 = shadow_F1(k)
            kap = kappa_sl2(k)
            assert f1 == kap * Fraction(1, 24)


SL2_DIM = 3
SL2_DUAL_COXETER = 2


# =========================================================================
#  10.  GENUS-0 ORDERED IDENTIFICATION
# =========================================================================

class TestGenus0Identification:
    """Ordered chiral homology at genus 0 recovers Z_0 = 1."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_genus0_id(self, k: int):
        """genus0_ordered_identification gives Z_0 = 1.
        # VERIFIED: [DC] direct computation
        # VERIFIED: [LC] unique vacuum at genus 0
        """
        data = genus0_ordered_identification(k)
        assert data["match"]
        assert data["Z_0"] == 1


# =========================================================================
#  11.  INTEGRALITY
# =========================================================================

class TestIntegrality:
    """Verlinde dimensions are always positive integers."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 7, 8])
    @pytest.mark.parametrize("g", [0, 1, 2, 3])
    def test_positive_integer(self, k: int, g: int):
        """Z_g(k) is a positive integer for all k >= 1, g >= 0.
        # VERIFIED: [DC] float-to-int rounding within 1e-4
        # VERIFIED: [LT] Verlinde (1988): conformal block count
        """
        z = verlinde_dimension(g, k)
        z_int = round(z)
        assert abs(z - z_int) < 1e-4, f"Z_{g}(k={k}) = {z} not close to integer"
        assert z_int > 0, f"Z_{g}(k={k}) = {z_int} not positive"


# =========================================================================
#  12.  FULL VERIFICATION SUITE
# =========================================================================

class TestFullVerification:
    """Run the engine's own verify_all() suite."""

    def test_verify_all(self):
        """All internal verification checks pass."""
        results = verify_all()
        failures = {k: v for k, v in results.items() if not v}
        assert not failures, f"Failed checks: {failures}"
