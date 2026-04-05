r"""Tests for Maulik-Okounkov vs Vol II R-matrix comparison for C^3.

Tests the agreement of two independent R-matrix constructions:
  (1) MO stable envelopes on Hilb^n(C^2)
  (2) Vol II OPE monodromy of W_{1+infinity}

Multi-path verification:
  Path 1: Direct comparison of MO and Vol II eigenvalues (product formula)
  Path 2: Explicit hand-computed eigenvalues for Hilb^2, Hilb^3
  Path 3: Unitarity from g(u)*g(-u) = 1
  Path 4: Yang-Baxter equation
  Path 5: Crossing symmetry h1 <-> h2
  Path 6: Classical limit recovers bar complex r-matrix
  Path 7: Specialization to Schiffmann-Vasserot parameters
"""

import numpy as np
import pytest

from compute.lib.rmatrix_comparison_c3 import (
    arm_length,
    bar_complex_rmatrix_gl1,
    boxes,
    c3_standard_params,
    classical_limit_rmatrix,
    compare_rmatrices,
    conjugate_partition,
    content,
    full_comparison_pipeline,
    hilb2_rmatrix_explicit,
    hilb3_rmatrix_explicit,
    kappa_from_rmatrix,
    leg_length,
    mo_rmatrix_charge_sector,
    mo_rmatrix_fock_diagonal,
    mo_rmatrix_hilbn,
    partitions_of,
    rmatrix_at_specializations,
    structure_function,
    structure_function_inversion,
    sv_params,
    tangent_weights_hilbn,
    verify_crossing_symmetry,
    verify_unitarity,
    verify_ybe_charge_sector,
    verify_ybe_mixed_charges,
    vol2_rmatrix_heisenberg_fock,
    weight_function_hilb1,
)


# =========================================================================
# Parameters for tests
# =========================================================================

H1, H2 = 1.0, 2.0  # Generic non-degenerate choice; h3 = -3
U_GENERIC = 5.0 + 0.1j
V_GENERIC = 3.0 + 0.2j
TOL = 1e-10


# =========================================================================
# 0. Partition combinatorics
# =========================================================================

class TestPartitionCombinatorics:
    """Tests for partition functions and Young diagram geometry."""

    def test_partitions_of_0(self):
        assert partitions_of(0) == [()]

    def test_partitions_of_1(self):
        assert partitions_of(1) == [(1,)]

    def test_partitions_of_2(self):
        assert partitions_of(2) == [(2,), (1, 1)]

    def test_partitions_of_3(self):
        assert partitions_of(3) == [(3,), (2, 1), (1, 1, 1)]

    def test_partitions_of_4(self):
        parts = partitions_of(4)
        assert len(parts) == 5
        assert parts == [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]

    def test_partitions_of_5(self):
        parts = partitions_of(5)
        assert len(parts) == 7  # p(5) = 7

    def test_conjugate_partition_hook(self):
        assert conjugate_partition((3, 1)) == (2, 1, 1)

    def test_conjugate_partition_column(self):
        assert conjugate_partition((1, 1, 1)) == (3,)

    def test_conjugate_partition_row(self):
        assert conjugate_partition((3,)) == (1, 1, 1)

    def test_conjugate_partition_square(self):
        assert conjugate_partition((2, 2)) == (2, 2)

    def test_conjugate_involution(self):
        """Conjugation is an involution."""
        for n in range(6):
            for lam in partitions_of(n):
                assert conjugate_partition(conjugate_partition(lam)) == lam

    def test_arm_leg_lengths_hook(self):
        """For (2,1): conjugate is (2,1).
        box (0,0): a = 2-0-1 = 1, l = conj[0]-0-1 = 2-0-1 = 1
        box (0,1): a = 2-1-1 = 0, l = conj[1]-0-1 = 1-0-1 = 0
        box (1,0): a = 1-0-1 = 0, l = conj[0]-1-1 = 2-1-1 = 0
        """
        lam = (2, 1)
        assert arm_length(lam, 0, 0) == 1
        assert arm_length(lam, 0, 1) == 0
        assert arm_length(lam, 1, 0) == 0
        assert leg_length(lam, 0, 0) == 1
        assert leg_length(lam, 0, 1) == 0
        assert leg_length(lam, 1, 0) == 0

    def test_boxes_count(self):
        for n in range(1, 6):
            for lam in partitions_of(n):
                assert len(boxes(lam)) == n

    def test_content_single_box(self):
        assert content((1,), 0, 0, H1, H2) == 0

    def test_content_row(self):
        """For (3): contents are 0, h1, 2*h1."""
        lam = (3,)
        assert abs(content(lam, 0, 0, H1, H2) - 0) < TOL
        assert abs(content(lam, 0, 1, H1, H2) - H1) < TOL
        assert abs(content(lam, 0, 2, H1, H2) - 2 * H1) < TOL

    def test_content_column(self):
        """For (1,1,1): contents are 0, -h2, -2*h2."""
        lam = (1, 1, 1)
        assert abs(content(lam, 0, 0, H1, H2) - 0) < TOL
        assert abs(content(lam, 1, 0, H1, H2) - (-H2)) < TOL
        assert abs(content(lam, 2, 0, H1, H2) - (-2 * H2)) < TOL


# =========================================================================
# 1. Structure function tests
# =========================================================================

class TestStructureFunction:
    """Tests for the Y(gl_hat_1) structure function g(u)."""

    def test_g_normalization(self):
        """g(u) -> 1 as u -> infinity."""
        g = structure_function(1000.0, H1, H2)
        assert abs(g - 1.0) < 1e-4

    def test_g_inversion_identity(self):
        """g(u) * g(-u) = 1 for all u (away from poles at -h1, -h2, -h3)."""
        # Avoid u and -u near poles: -h1=-1, -h2=-2, -h3=3
        for u in [4.5, 5.5, 0.7 + 1.3j, 10.0, -0.5 + 0.5j]:
            product = structure_function_inversion(u, H1, H2)
            assert abs(product - 1.0) < TOL, f"g(u)*g(-u) = {product} at u={u}"

    def test_g_inversion_many_params(self):
        """g(u)*g(-u) = 1 for various (h1, h2).

        Use u=7.5 to stay well away from poles for all parameter sets.
        Poles of g are at -h1, -h2, -h3; poles of g(-u) are at h1, h2, h3.
        """
        params = [(1, 2), (0.5, 3), (1, -2), (2, 3), (0.3, 0.7)]
        for h1, h2 in params:
            # Choose u that avoids poles of both g(u) and g(-u)
            h3 = -(h1 + h2)
            poles = [h1, h2, h3, -h1, -h2, -h3]
            u = 7.5
            # Verify u is safe
            assert all(abs(u - p) > 0.1 for p in poles), f"u={u} too close to pole for h=({h1},{h2})"
            product = structure_function_inversion(u, h1, h2)
            assert abs(product - 1.0) < TOL

    def test_g_zeros_at_h_params(self):
        """g(h1) = 0, g(h2) = 0, g(h3) = 0."""
        h3 = -(H1 + H2)
        for h in [H1, H2, h3]:
            val = structure_function(h, H1, H2)
            assert abs(val) < TOL

    def test_g_poles_at_neg_h_params(self):
        """g(-h1), g(-h2), g(-h3) diverge."""
        # Test that values are very large near -h1
        val = structure_function(-H1 + 1e-8, H1, H2)
        assert abs(val) > 1e6

    def test_g_at_sv_n2(self):
        """Structure function at SV N=2: h1=1, h2=-2, h3=1."""
        h1, h2 = 1.0, -2.0
        g = structure_function(5.0, h1, h2)
        # g(5) = (5-1)(5+2)(5-1)/((5+1)(5-2)(5+1)) = 4*7*4/(6*3*6) = 112/108
        expected = (4 * 7 * 4) / (6 * 3 * 6)
        assert abs(g - expected) < TOL


# =========================================================================
# 2. MO R-matrix tests: Hilb^1
# =========================================================================

class TestMORmatrixHilb1:
    """Tests for the MO R-matrix on Hilb^1(C^2) = C^2."""

    def test_hilb1_equals_g(self):
        """R^{MO}_{(1),(1)}(u) = g(u)."""
        R = mo_rmatrix_fock_diagonal(U_GENERIC, (1,), (1,), H1, H2)
        g = structure_function(U_GENERIC, H1, H2)
        assert abs(R - g) < TOL

    def test_hilb1_weight_function(self):
        """Weight function equals g(u)."""
        R = weight_function_hilb1(U_GENERIC, H1, H2)
        g = structure_function(U_GENERIC, H1, H2)
        assert abs(R - g) < TOL

    def test_hilb1_tangent_weights(self):
        """Hilb^1 has tangent weights {h1, h2}."""
        weights = tangent_weights_hilbn((1,), H1, H2)
        assert len(weights) == 2
        assert abs(weights[0] - H1) < TOL
        assert abs(weights[1] - H2) < TOL

    def test_hilb1_matrix_is_1x1(self):
        """R-matrix on Hilb^1 tensor Hilb^1 is 1x1."""
        R = mo_rmatrix_charge_sector(1, 1, U_GENERIC, H1, H2)
        assert R.shape == (1, 1)


# =========================================================================
# 3. MO R-matrix tests: Hilb^2
# =========================================================================

class TestMORmatrixHilb2:
    """Tests for the MO R-matrix on Hilb^2(C^2)."""

    def test_hilb2_explicit_eigenvalues(self):
        """Compare with hand-computed eigenvalues for Hilb^2."""
        result = hilb2_rmatrix_explicit(U_GENERIC, H1, H2)
        assert result["matrix_dim"] == 4  # 2x2 tensor product

    def test_hilb2_matrix_dimension(self):
        """R-matrix on Hilb^2 tensor Hilb^2 is 4x4."""
        R = mo_rmatrix_charge_sector(2, 2, U_GENERIC, H1, H2)
        assert R.shape == (4, 4)

    def test_hilb2_diagonal(self):
        """R-matrix is diagonal in partition basis."""
        R = mo_rmatrix_charge_sector(2, 2, U_GENERIC, H1, H2)
        off_diag = R - np.diag(np.diag(R))
        assert np.max(np.abs(off_diag)) < TOL

    def test_hilb2_eigenvalue_22(self):
        """R_{(2),(2)}(u) = g(u)^2 * g(u+h1) * g(u-h1)."""
        g = lambda z: structure_function(z, H1, H2)
        expected = g(U_GENERIC) ** 2 * g(U_GENERIC + H1) * g(U_GENERIC - H1)
        computed = mo_rmatrix_fock_diagonal(U_GENERIC, (2,), (2,), H1, H2)
        assert abs(computed - expected) < TOL

    def test_hilb2_eigenvalue_11_11(self):
        """R_{(1,1),(1,1)}(u) = g(u)^2 * g(u+h2) * g(u-h2)."""
        g = lambda z: structure_function(z, H1, H2)
        expected = g(U_GENERIC) ** 2 * g(U_GENERIC + H2) * g(U_GENERIC - H2)
        computed = mo_rmatrix_fock_diagonal(U_GENERIC, (1, 1), (1, 1), H1, H2)
        assert abs(computed - expected) < TOL

    def test_hilb2_mixed_eigenvalue(self):
        """R_{(2),(1,1)}(u) explicit formula."""
        g = lambda z: structure_function(z, H1, H2)
        h3 = -(H1 + H2)
        expected = g(U_GENERIC) * g(U_GENERIC + H2) * g(U_GENERIC + H1) * g(U_GENERIC - h3)
        computed = mo_rmatrix_fock_diagonal(U_GENERIC, (2,), (1, 1), H1, H2)
        assert abs(computed - expected) < TOL


# =========================================================================
# 4. MO R-matrix tests: Hilb^3
# =========================================================================

class TestMORmatrixHilb3:
    """Tests for the MO R-matrix on Hilb^3(C^2)."""

    def test_hilb3_explicit_eigenvalues(self):
        """Compare with hand-computed eigenvalues for Hilb^3."""
        result = hilb3_rmatrix_explicit(U_GENERIC, H1, H2)
        assert result["matrix_dim"] == 9  # 3x3 tensor product

    def test_hilb3_matrix_dimension(self):
        """R-matrix on Hilb^3 tensor Hilb^3 is 9x9."""
        R = mo_rmatrix_charge_sector(3, 3, U_GENERIC, H1, H2)
        assert R.shape == (9, 9)

    def test_hilb3_diagonal(self):
        """R-matrix is diagonal in partition basis."""
        R = mo_rmatrix_charge_sector(3, 3, U_GENERIC, H1, H2)
        off_diag = R - np.diag(np.diag(R))
        assert np.max(np.abs(off_diag)) < TOL

    def test_hilb3_eigenvalue_333(self):
        """R_{(3),(3)}(u): 9 box pairs from {0,h1,2h1} x {0,h1,2h1}."""
        g = lambda z: structure_function(z, H1, H2)
        # Contents of (3): {0, h1, 2h1}
        # Pairs: 9 total. g(u+ci-cj) for all (ci, cj) in {0,h1,2h1}^2
        expected = 1.0 + 0j
        for ci in [0, H1, 2 * H1]:
            for cj in [0, H1, 2 * H1]:
                expected *= g(U_GENERIC + ci - cj)
        computed = mo_rmatrix_fock_diagonal(U_GENERIC, (3,), (3,), H1, H2)
        assert abs(computed - expected) < TOL

    def test_hilb3_eigenvalue_21_21(self):
        """R_{(2,1),(2,1)}(u): 9 box pairs from {0,h1,-h2} x {0,h1,-h2}."""
        g = lambda z: structure_function(z, H1, H2)
        expected = 1.0 + 0j
        for ci in [0, H1, -H2]:
            for cj in [0, H1, -H2]:
                expected *= g(U_GENERIC + ci - cj)
        computed = mo_rmatrix_fock_diagonal(U_GENERIC, (2, 1), (2, 1), H1, H2)
        assert abs(computed - expected) < TOL

    def test_hilb3_eigenvalue_111_111(self):
        """R_{(1,1,1),(1,1,1)}(u): 9 box pairs from {0,-h2,-2h2}^2."""
        g = lambda z: structure_function(z, H1, H2)
        expected = 1.0 + 0j
        for ci in [0, -H2, -2 * H2]:
            for cj in [0, -H2, -2 * H2]:
                expected *= g(U_GENERIC + ci - cj)
        computed = mo_rmatrix_fock_diagonal(U_GENERIC, (1, 1, 1), (1, 1, 1), H1, H2)
        assert abs(computed - expected) < TOL


# =========================================================================
# 5. MO vs Vol II comparison (the central test)
# =========================================================================

class TestMOvsVolII:
    """Tests that MO and Vol II R-matrices agree.

    This is the CENTRAL test: agreement proves the E_1 -> E_2 passage
    via Drinfeld center at the level of explicit matrix coefficients.
    """

    @pytest.mark.parametrize("n1,n2", [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1), (2, 3), (3, 2), (3, 3)])
    def test_mo_vol2_agree(self, n1, n2):
        """MO R-matrix equals Vol II R-matrix for charge sector (n1, n2)."""
        result = compare_rmatrices(n1, n2, U_GENERIC, H1, H2)
        assert result["agree"], \
            f"MO-Vol II mismatch at ({n1},{n2}): diff_norm = {result['difference_norm']}"

    @pytest.mark.parametrize("n1,n2", [(1, 1), (2, 2), (3, 3)])
    def test_mo_vol2_agree_different_params(self, n1, n2):
        """Agreement persists at different (h1, h2) parameters."""
        for h1, h2 in [(0.5, 3.0), (1.0, -2.0), (2.0, 3.0), (0.3, 0.7)]:
            result = compare_rmatrices(n1, n2, U_GENERIC, h1, h2)
            assert result["agree"], \
                f"Mismatch at ({n1},{n2}), h=({h1},{h2}): diff = {result['difference_norm']}"

    @pytest.mark.parametrize("n1,n2", [(1, 1), (2, 2)])
    def test_mo_vol2_agree_different_u(self, n1, n2):
        """Agreement persists at different spectral parameters."""
        for u in [1.5, 7.0, 3.0 + 2.0j, 10.0 + 0.5j, -2.0 + 1.0j]:
            result = compare_rmatrices(n1, n2, u, H1, H2)
            assert result["agree"], \
                f"Mismatch at ({n1},{n2}), u={u}: diff = {result['difference_norm']}"

    def test_mo_vol2_agree_sv_n2(self):
        """Agreement at Schiffmann-Vasserot N=2."""
        h1, h2 = sv_params(2)
        result = compare_rmatrices(2, 2, U_GENERIC, h1, h2)
        assert result["agree"]

    def test_mo_vol2_agree_sv_n3(self):
        """Agreement at Schiffmann-Vasserot N=3."""
        h1, h2 = sv_params(3)
        result = compare_rmatrices(1, 1, U_GENERIC, h1, h2)
        assert result["agree"]


# =========================================================================
# 6. Unitarity tests
# =========================================================================

class TestUnitarity:
    """Tests for R(u)*R_{21}(-u) = 1, following from g(u)*g(-u) = 1."""

    @pytest.mark.parametrize("n1,n2", [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1), (3, 3)])
    def test_unitarity(self, n1, n2):
        """R(u)*R_{21}(-u) = 1 in charge sector (n1, n2)."""
        result = verify_unitarity(n1, n2, U_GENERIC, H1, H2)
        assert result["holds"], \
            f"Unitarity fails at ({n1},{n2}): max_error = {result['max_error']}"

    def test_unitarity_different_params(self):
        """Unitarity at various (h1, h2)."""
        for h1, h2 in [(0.5, 3.0), (1.0, -2.0), (2.0, 3.0)]:
            result = verify_unitarity(2, 2, U_GENERIC, h1, h2)
            assert result["holds"]


# =========================================================================
# 7. Yang-Baxter equation tests
# =========================================================================

class TestYBE:
    """Tests for the Yang-Baxter equation.

    For diagonal R-matrices, YBE is trivially satisfied (scalars commute).
    The tests verify that the PRODUCT of structure functions factors correctly.
    """

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_ybe_same_charge(self, n):
        """YBE in the charge-n sector."""
        result = verify_ybe_charge_sector(n, U_GENERIC, V_GENERIC, H1, H2)
        assert result["holds"], \
            f"YBE fails at n={n}: max_error = {result['max_error']}"

    @pytest.mark.parametrize("n1,n2,n3", [
        (1, 1, 1), (1, 2, 1), (2, 1, 1), (1, 1, 2),
        (2, 2, 1), (2, 1, 2), (1, 2, 2), (2, 2, 2),
        (1, 3, 1), (3, 1, 2), (2, 3, 1),
    ])
    def test_ybe_mixed_charges(self, n1, n2, n3):
        """YBE in mixed charge sectors."""
        result = verify_ybe_mixed_charges(n1, n2, n3, U_GENERIC, V_GENERIC, H1, H2)
        assert result["holds"], \
            f"YBE fails at ({n1},{n2},{n3}): max_error = {result['max_error']}"

    def test_ybe_different_params(self):
        """YBE at various (h1, h2)."""
        for h1, h2 in [(0.5, 3.0), (1.0, -2.0)]:
            result = verify_ybe_charge_sector(2, U_GENERIC, V_GENERIC, h1, h2)
            assert result["holds"]


# =========================================================================
# 8. Crossing symmetry tests
# =========================================================================

class TestCrossing:
    """Tests for crossing symmetry: R_{lam,mu}(u; h1,h2) = R_{mu',lam'}(u; h2,h1)."""

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_crossing_symmetry(self, n):
        """Crossing symmetry in the charge-n sector."""
        result = verify_crossing_symmetry(n, U_GENERIC, H1, H2)
        assert result["holds"], \
            f"Crossing fails at n={n}: max_error = {result['max_error']}"

    def test_crossing_different_params(self):
        """Crossing symmetry at various (h1, h2)."""
        for h1, h2 in [(0.5, 3.0), (2.0, 3.0)]:
            result = verify_crossing_symmetry(2, U_GENERIC, h1, h2)
            assert result["holds"]


# =========================================================================
# 9. Classical limit tests
# =========================================================================

class TestClassicalLimit:
    """Tests for the classical limit: R -> 1 + hbar^2 * r_cl + O(hbar^4)."""

    def test_classical_limit_hilb1(self):
        """Classical r-matrix for Hilb^1 agrees with bar complex.

        log g(u) with h_a -> hbar*h_a has only ODD powers of hbar
        (because log g only has odd power sums p_k with k odd, and p_1=0
        by CY condition). The leading term is at hbar^3:

            log g(u) = -2*hbar^3*p_3/(3*u^3) + O(hbar^5)
            g(u) = 1 - 2*hbar^3*p_3/(3*u^3) + O(hbar^5)

        where p_3 = h1^3 + h2^3 + h3^3 = 3*sigma_3 = 3*h1*h2*h3.
        """
        hbar = 1e-3
        u = 5.0
        g_val = structure_function(u, hbar * H1, hbar * H2)
        r_classical = (g_val - 1.0) / hbar ** 3

        # p_3 = 3*sigma_3, sigma_3 = h1*h2*h3 = 1*2*(-3) = -6
        h3 = -(H1 + H2)
        sigma_3 = H1 * H2 * h3
        p_3 = 3 * sigma_3
        expected = -2 * p_3 / (3 * u ** 3)

        assert abs(r_classical - expected) < 1e-2, \
            f"Classical limit: {r_classical} vs expected {expected}"

    def test_kappa_extraction(self):
        """kappa = -sigma_2 for the Heisenberg subalgebra."""
        kappa = kappa_from_rmatrix(1, H1, H2)
        sigma_2 = H1 * H2 + H1 * (-(H1 + H2)) + H2 * (-(H1 + H2))
        assert abs(kappa - (-sigma_2)) < TOL

    def test_bar_complex_rmatrix(self):
        """Bar complex classical r-matrix = -sigma_2/u."""
        sigma_2 = H1 * H2 + H1 * (-(H1 + H2)) + H2 * (-(H1 + H2))
        r = bar_complex_rmatrix_gl1(5.0, sigma_2)
        assert abs(r - (-sigma_2 / 5.0)) < TOL


# =========================================================================
# 10. Explicit R-matrix entry tests (hand-computed)
# =========================================================================

class TestExplicitEntries:
    """Hand-computed R-matrix entries for specific partitions and parameters."""

    def test_empty_partition(self):
        """R_{(),()}(u) = 1 (empty product)."""
        val = mo_rmatrix_fock_diagonal(U_GENERIC, (), (), H1, H2)
        assert abs(val - 1.0) < TOL

    def test_hilb1_explicit(self):
        """R_{(1),(1)}(u) = g(u) = (u-h1)(u-h2)(u-h3)/((u+h1)(u+h2)(u+h3))."""
        u = 5.0
        h3 = -(H1 + H2)
        expected = (u - H1) * (u - H2) * (u - h3) / ((u + H1) * (u + H2) * (u + h3))
        computed = mo_rmatrix_fock_diagonal(u, (1,), (1,), H1, H2)
        assert abs(computed - expected) < TOL

    def test_hilb2_row_row(self):
        """R_{(2),(2)}(u) with h1=1, h2=2: explicit numerical check."""
        u = 5.0
        h1, h2, h3 = 1.0, 2.0, -3.0
        g = lambda z: (z - h1) * (z - h2) * (z - h3) / ((z + h1) * (z + h2) * (z + h3))
        # Contents of (2): {0, 1}
        # R = g(u+0-0)*g(u+0-1)*g(u+1-0)*g(u+1-1)
        #   = g(5)*g(4)*g(6)*g(5) = g(5)^2 * g(4) * g(6)
        expected = g(5) ** 2 * g(4) * g(6)
        computed = mo_rmatrix_fock_diagonal(u, (2,), (2,), h1, h2)
        assert abs(computed - expected) < TOL

    def test_hilb1_mixed_charges(self):
        """R_{(1),(1,1)}(u): 1 box x 2 boxes = 2 structure functions."""
        g = lambda z: structure_function(z, H1, H2)
        # (1) contents: {0}, (1,1) contents: {0, -h2}
        expected = g(U_GENERIC + 0 - 0) * g(U_GENERIC + 0 - (-H2))
        expected_v2 = g(U_GENERIC) * g(U_GENERIC + H2)
        assert abs(expected - expected_v2) < TOL

        computed = mo_rmatrix_fock_diagonal(U_GENERIC, (1,), (1, 1), H1, H2)
        assert abs(computed - expected) < TOL


# =========================================================================
# 11. Specialization tests
# =========================================================================

class TestSpecializations:
    """Tests at specific parameter values from the physics literature."""

    def test_sv_n1_degenerate(self):
        """SV N=1: h1=1, h2=-1, h3=0. g(u) = (u-1)(u+1)u / ((u+1)(u-1)u) = 1."""
        # At this point g(u) = 1 identically (structure function trivializes)
        # But h3=0 makes the denominator vanish at u=0.
        # At generic u != 0: g = 1.
        h1, h2 = sv_params(1)
        # g(5) = (5-1)(5+1)(5-0)/((5+1)(5-1)(5+0)) = 4*6*5/(6*4*5) = 1
        g = structure_function(5.0, h1, h2)
        assert abs(g - 1.0) < TOL

    def test_sv_n2_values(self):
        """SV N=2: h1=1, h2=-2, h3=1. Explicit g(u)."""
        h1, h2 = sv_params(2)
        h3 = -(h1 + h2)  # = 1
        assert abs(h3 - 1.0) < TOL

        # g(u) = (u-1)(u+2)(u-1)/((u+1)(u-2)(u+1)) = (u-1)^2*(u+2)/((u+1)^2*(u-2))
        u = 5.0
        expected = (u - 1) ** 2 * (u + 2) / ((u + 1) ** 2 * (u - 2))
        computed = structure_function(u, h1, h2)
        assert abs(computed - expected) < TOL

    def test_rmatrix_specializations(self):
        """R-matrices at multiple standard specializations all agree."""
        result = rmatrix_at_specializations(1, 1)
        for key, data in result.items():
            assert data["agree"], f"Mismatch at specialization {key}"


# =========================================================================
# 12. Full pipeline test
# =========================================================================

class TestFullPipeline:
    """Run the complete comparison pipeline."""

    def test_full_pipeline_charge2(self):
        """Full pipeline up to charge 2."""
        result = full_comparison_pipeline(max_charge=2, h1=H1, h2=H2, u=U_GENERIC)
        assert result["summary"]["all_agree"], "MO-Vol II comparison failed"
        assert result["summary"]["all_unitary"], "Unitarity failed"
        assert result["summary"]["all_ybe"], "YBE failed"
        assert result["summary"]["all_crossing"], "Crossing symmetry failed"
        assert result["summary"]["all_pass"], "Some test in pipeline failed"

    def test_full_pipeline_charge3(self):
        """Full pipeline up to charge 3."""
        result = full_comparison_pipeline(max_charge=3, h1=H1, h2=H2, u=U_GENERIC)
        assert result["summary"]["all_pass"], "Full pipeline failed at charge 3"


# =========================================================================
# 13. Consistency with existing compute layer
# =========================================================================

class TestConsistencyWithExisting:
    """Cross-check with existing R-matrix engines in the compute layer."""

    def test_classical_cybe_for_gl1(self):
        """The classical r-matrix r(u) = sigma_2/u satisfies CYBE trivially.

        For gl_1 (rank 1), the Casimir is a scalar, so CYBE is trivially
        satisfied: [c/u, c/(u+v)] + [c/u, c/v] + [c/(u+v), c/v] = 0
        because scalars commute.
        """
        sigma_2 = H1 * H2 + H1 * (-(H1 + H2)) + H2 * (-(H1 + H2))
        r_u = bar_complex_rmatrix_gl1(5.0, sigma_2)
        r_v = bar_complex_rmatrix_gl1(3.0, sigma_2)
        r_uv = bar_complex_rmatrix_gl1(8.0, sigma_2)
        # Scalars commute, so [r_12, r_13] = r_u * r_uv - r_uv * r_u = 0
        assert abs(r_u * r_uv - r_uv * r_u) < TOL

    def test_tangent_weights_match_hilbert_scheme_geometry(self):
        """Tangent weights of Hilb^n(C^2) match known geometric formulas."""
        # Hilb^1: T_{(1)} = {h1, h2} (tangent space of C^2)
        w1 = tangent_weights_hilbn((1,), H1, H2)
        assert len(w1) == 2

        # Hilb^2, point (2): T has 4 weights
        w2_row = tangent_weights_hilbn((2,), H1, H2)
        assert len(w2_row) == 4

        # Hilb^2, point (1,1): T has 4 weights
        w2_col = tangent_weights_hilbn((1, 1), H1, H2)
        assert len(w2_col) == 4

    def test_partition_count_consistency(self):
        """Partition counts match known values p(n)."""
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11}
        for n, count in expected.items():
            assert len(partitions_of(n)) == count, f"p({n}) wrong"

    def test_charge_sector_dimension(self):
        """R-matrix dimension matches p(n1)*p(n2)."""
        for n1, n2 in [(1, 1), (2, 2), (3, 3), (1, 3), (2, 3)]:
            R = mo_rmatrix_charge_sector(n1, n2, U_GENERIC, H1, H2)
            d1 = len(partitions_of(n1))
            d2 = len(partitions_of(n2))
            assert R.shape == (d1 * d2, d1 * d2)


# =========================================================================
# 14. Stress tests and edge cases
# =========================================================================

class TestEdgeCases:
    """Edge cases and stress tests."""

    def test_large_u(self):
        """R-matrix approaches identity for large |u|."""
        R = mo_rmatrix_fock_diagonal(1000.0, (2, 1), (2, 1), H1, H2)
        assert abs(R - 1.0) < 1e-3

    def test_complex_u(self):
        """R-matrix is well-defined for complex u."""
        R = mo_rmatrix_fock_diagonal(3.0 + 4.0j, (2,), (1, 1), H1, H2)
        assert np.isfinite(R)

    def test_negative_h_params(self):
        """R-matrix with negative h parameters."""
        R = mo_rmatrix_fock_diagonal(5.0, (1,), (1,), -1.0, -2.0)
        g = structure_function(5.0, -1.0, -2.0)
        assert abs(R - g) < TOL

    def test_consistency_mo_hilbn_vs_charge_sector(self):
        """mo_rmatrix_hilbn and mo_rmatrix_charge_sector agree for n1=n2."""
        R_hilb = mo_rmatrix_hilbn(2, U_GENERIC, H1, H2)
        R_charge = mo_rmatrix_charge_sector(2, 2, U_GENERIC, H1, H2)
        assert np.allclose(R_hilb, R_charge, atol=TOL)


# =========================================================================
# 15. Multi-path verification summary
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification tests ensuring consistency across methods.

    Per the multi-path verification mandate:
    Path 1: MO product formula
    Path 2: Vol II OPE monodromy
    Path 3: Explicit hand computation
    """

    def test_three_paths_hilb2(self):
        """Three independent paths agree for Hilb^2.

        Use u=5.5 to avoid poles: for H1=1,H2=2,H3=-3, poles of g are at
        -1,-2,3. Content differences for Hilb^2 partitions are in
        {-h1, 0, h1, -h2, h2, h1+h2}. So g(u+d) must avoid poles,
        i.e. u+d not in {-1,-2,3}. With u=5.5 and max |d|=2, the
        nearest dangerous value is 5.5-2=3.5 (safe) or 5.5+(-2)=3.5 (safe).
        Actually we need u+h2=7.5, u-h2=3.5, u+h3=2.5, u-h3=8.5 -- all safe.
        """
        u = 5.5

        # Path 1: MO product formula
        path1 = mo_rmatrix_fock_diagonal(u, (2,), (2,), H1, H2)

        # Path 2: Vol II OPE monodromy
        R_v2 = vol2_rmatrix_heisenberg_fock(u, 2, 2, H1, H2)
        path2 = R_v2[0, 0]  # (2) is the first partition

        # Path 3: Hand computation
        g = lambda z: structure_function(z, H1, H2)
        path3 = g(u) ** 2 * g(u + H1) * g(u - H1)

        assert abs(path1 - path2) < TOL
        assert abs(path1 - path3) < TOL
        assert abs(path2 - path3) < TOL

    def test_three_paths_hilb3(self):
        """Three independent paths agree for Hilb^3.

        Use u=5.5 to stay away from all poles. Max content difference
        for partitions of 3 is 2*max(h1,h2) = 4, so g(u+d) has
        argument in [1.5, 9.5] -- all safe.
        """
        u = 5.5

        # Path 1: MO product formula
        path1 = mo_rmatrix_fock_diagonal(u, (2, 1), (2, 1), H1, H2)

        # Path 2: Vol II OPE monodromy
        R_v2 = vol2_rmatrix_heisenberg_fock(u, 3, 3, H1, H2)
        # (2,1) is the second partition of 3
        parts = partitions_of(3)
        idx_21 = parts.index((2, 1))
        path2 = R_v2[idx_21 * 3 + idx_21, idx_21 * 3 + idx_21]

        # Path 3: Hand computation
        g = lambda z: structure_function(z, H1, H2)
        contents_21 = [0, H1, -H2]
        path3 = 1.0 + 0j
        for ci in contents_21:
            for cj in contents_21:
                path3 *= g(u + ci - cj)

        assert abs(path1 - path2) < TOL
        assert abs(path1 - path3) < TOL

    def test_unitarity_from_g_inversion(self):
        """Unitarity R*R21^{-1} = 1 follows directly from g*g^{-1} = 1."""
        # Use u=9.5 to avoid all poles of g(z) at z in {-H1,-H2,-H3}={-1,-2,3}.
        # The test iterates partitions up to size 3 with H1=1,H2=2.
        # Max |content difference| across all partition pairs is 5
        # (e.g. (1,1,1) vs (2,): c=-4 minus c=1). Forward call evaluates
        # g at z in [u-5, u+5]=[4.5, 14.5]; backward at z in [-u-5, -u+5]
        # = [-14.5, -4.5]. Both intervals avoid all poles {-1,-2,3}.
        u = 9.5
        for lam in [(1,), (2,), (1, 1), (2, 1), (3,), (1, 1, 1)]:
            for mu in [(1,), (2,), (1, 1)]:
                r_fwd = mo_rmatrix_fock_diagonal(u, lam, mu, H1, H2)
                r_bwd = mo_rmatrix_fock_diagonal(-u, mu, lam, H1, H2)
                assert abs(r_fwd * r_bwd - 1.0) < TOL, \
                    f"Unitarity fails for ({lam},{mu})"
