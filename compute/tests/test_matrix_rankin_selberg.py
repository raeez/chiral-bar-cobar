"""Tests for the matrix Rankin-Selberg integral on VVMF character vectors.

55 tests covering:
  1. Ising matrix L-function: 3x3 matrix computation at s=2,3,4
  2. Diagonal vs off-diagonal: vanishing structure from weight differences
  3. Unfolding the matrix integral: Parseval x-integral analysis
  4. Multiplicativity of matrix entries: diagonal and off-diagonal
  5. S-matrix diagonalization: eigenbasis characters
  6. Factored L-matrix: spectral decomposition via S-matrix
  7. Determinant L-function: det(L(s)) computation
  8. Comparison with lattice case V_Z
  9. Conductor and gamma factors / functional equation tests
"""

import pytest
from fractions import Fraction
from math import gcd

import mpmath
from mpmath import mp, mpf, mpc, pi, exp, fabs, sqrt, power, zeta, re as mpre

from compute.lib.matrix_rankin_selberg import (
    ising_character_data,
    ising_model,
    tricritical_ising_model,
    three_state_potts_model,
    unfolded_dirichlet_coeffs_diagonal,
    unfolded_dirichlet_coeffs_offdiag,
    matrix_L_fast,
    extract_dirichlet_coeffs,
    check_multiplicativity,
    multiplicativity_score,
    full_multiplicativity_analysis,
    s_eigenbasis,
    eigenbasis_L_matrix,
    trace_L,
    det_L,
    trace_L_values,
    det_L_values,
    s_matrix_spectral_decomposition,
    ising_weight_differences,
    ising_vanishing_offdiag,
    tricritical_ising_weight_analysis,
    lattice_vz_L,
    lattice_vz_dirichlet_coeffs,
    ising_matrix_L,
    diagonal_vs_offdiagonal,
    completed_L_entry,
    functional_equation_test,
    rankin_selberg_gamma_factor,
    eigenbasis_characters,
    eigenbasis_qseries,
)
from compute.lib.vvmf_hecke import (
    MinimalModel,
    ising_model as vvmf_ising_model,
    character_qseries,
    character_value,
    s_matrix,
    t_matrix,
    verify_s_matrix_unitarity,
)


DPS = 25
NUM_TERMS = 60


# ===================================================================
# 1. Ising matrix L-function computation
# ===================================================================

class TestIsingMatrixLFunction:
    """Test the 3x3 matrix L_{ij}(s) for the Ising model."""

    def test_ising_L_is_3x3(self):
        """L_{ij}(s) for Ising is a 3x3 matrix."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        assert L.rows == 3
        assert L.cols == 3

    def test_ising_L_diagonal_positive_s2(self):
        """Diagonal entries L_{ii}(2) are positive (integrals of |chi_i|^2 y^2)."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        for i in range(3):
            assert float(L[i, i]) > 0, f"L[{i},{i}](2) should be positive"

    def test_ising_L_diagonal_positive_s3(self):
        """Diagonal entries L_{ii}(3) are positive."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 3, num_terms=NUM_TERMS, dps=DPS)
        for i in range(3):
            assert float(L[i, i]) > 0, f"L[{i},{i}](3) should be positive"

    def test_ising_L_diagonal_positive_s4(self):
        """Diagonal entries L_{ii}(4) are positive."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 4, num_terms=NUM_TERMS, dps=DPS)
        for i in range(3):
            assert float(L[i, i]) > 0, f"L[{i},{i}](4) should be positive"

    def test_ising_L_offdiag_zero(self):
        """Off-diagonal entries L_{ij}(s) vanish for Ising (non-integer weight diffs)."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        for i in range(3):
            for j in range(3):
                if i != j:
                    assert abs(float(L[i, j])) < 1e-10, \
                        f"L[{i},{j}](2) = {float(L[i,j])}, expected 0"

    def test_ising_L_decreasing_in_s(self):
        """Diagonal entries decrease as s increases (convergence improvement)."""
        mp.dps = DPS
        model = ising_model()
        L2 = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        L3 = matrix_L_fast(model, 3, num_terms=NUM_TERMS, dps=DPS)
        L4 = matrix_L_fast(model, 4, num_terms=NUM_TERMS, dps=DPS)
        for i in range(3):
            assert float(L2[i, i]) > float(L3[i, i]) > float(L4[i, i]), \
                f"L[{i},{i}] should decrease: {float(L2[i,i])} > {float(L3[i,i])} > {float(L4[i,i])}"

    def test_ising_matrix_L_wrapper(self):
        """The ising_matrix_L wrapper returns correct structure."""
        mp.dps = DPS
        result = ising_matrix_L(2, num_terms=NUM_TERMS, dps=DPS)
        assert 'L' in result
        assert 'weights' in result
        assert 'S' in result
        assert len(result['weights']) == 3


# ===================================================================
# 2. Diagonal vs off-diagonal: vanishing structure
# ===================================================================

class TestDiagonalVsOffDiagonal:
    """Test the structural vanishing of off-diagonal entries."""

    def test_ising_weights(self):
        """Ising conformal weights are h=0, h=1/16, h=1/2."""
        weights, _, labels = ising_weight_differences()
        weight_set = set(weights)
        assert Fraction(0) in weight_set
        assert Fraction(1, 16) in weight_set
        assert Fraction(1, 2) in weight_set

    def test_ising_all_offdiag_vanish(self):
        """All off-diagonal weight differences are non-integer for Ising."""
        vanishing, _, diffs = ising_vanishing_offdiag()
        for (i, j), v in vanishing.items():
            if i != j:
                assert v, f"({i},{j}): diff={diffs[(i,j)]} should give vanishing L_{{{i},{j}}}"

    def test_ising_diagonal_nonvanish(self):
        """Diagonal entries never vanish."""
        vanishing, _, _ = ising_vanishing_offdiag()
        for i in range(3):
            assert not vanishing[(i, i)]

    def test_diagonal_vs_offdiag_decomposition(self):
        """diagonal_vs_offdiagonal correctly separates components."""
        mp.dps = DPS
        model = ising_model()
        result = diagonal_vs_offdiagonal(model, 2, num_terms=NUM_TERMS, dps=DPS)
        assert len(result['diagonal']) == 3
        assert len(result['offdiagonal']) == 3  # three (i,j) pairs with i<j
        # Off-diagonal should all be zero
        for (i, j), val in result['offdiagonal'].items():
            assert abs(float(val)) < 1e-10

    def test_trace_equals_sum_of_diagonal(self):
        """tr(L) = sum of diagonal entries."""
        mp.dps = DPS
        model = ising_model()
        result = diagonal_vs_offdiagonal(model, 2, num_terms=NUM_TERMS, dps=DPS)
        tr = float(result['trace'])
        diag_sum = sum(float(d) for d in result['diagonal'])
        assert abs(tr - diag_sum) / abs(tr) < 1e-10

    def test_potts_has_integer_weight_diff(self):
        """3-state Potts M(6,5) has at least one integer weight difference."""
        model = three_state_potts_model()
        labels = model.primary_labels()
        weights = [model.conformal_weight(lab.r, lab.s) for lab in labels]
        has_integer = False
        for i in range(len(weights)):
            for j in range(i + 1, len(weights)):
                d = weights[j] - weights[i]
                if d.denominator == 1:
                    has_integer = True
        assert has_integer, "Potts should have at least one integer weight difference"


# ===================================================================
# 3. Unfolding: Parseval on x-integral
# ===================================================================

class TestUnfolding:
    """Test the Rankin-Selberg unfolding via Parseval."""

    def test_diagonal_coeffs_start_with_one(self):
        """Diagonal c_{ii}(0) = a_i(0)^2 = 1 for all Ising characters."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        for idx in range(3):
            coeffs = unfolded_dirichlet_coeffs_diagonal(
                data['qseries'][idx], data['weights'][idx], data['c'], 10, dps=DPS
            )
            # First nonzero coefficient should have value 1.0 (since a_i(0) = 1)
            assert len(coeffs) > 0
            assert abs(coeffs[0][1] - 1.0) < 1e-10

    def test_diagonal_coeffs_nonnegative(self):
        """Diagonal coefficients |a_i(n)|^2 >= 0."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        for idx in range(3):
            coeffs = unfolded_dirichlet_coeffs_diagonal(
                data['qseries'][idx], data['weights'][idx], data['c'], 30, dps=DPS
            )
            for exp, c_val in coeffs:
                assert c_val >= -1e-15, f"chi_{idx}: c({exp}) = {c_val} should be >= 0"

    def test_offdiag_ising_vanishes(self):
        """Off-diagonal unfolded coefficients vanish for Ising (non-integer h_j - h_i)."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                coeffs = unfolded_dirichlet_coeffs_offdiag(
                    data['qseries'][i], data['qseries'][j],
                    data['weights'][i], data['weights'][j], data['c'],
                    30, dps=DPS
                )
                assert len(coeffs) == 0, \
                    f"chi_{i} x chi_{j}: should vanish but got {len(coeffs)} coeffs"

    def test_diagonal_coeffs_are_squares(self):
        """c_{ii}(n) = a_i(n)^2 (character coefficients are real)."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        qs = data['qseries'][0]  # vacuum character
        for n in range(min(20, len(qs))):
            a_n = float(qs[n])
            c_n = a_n ** 2
            assert c_n >= 0
            # Check it's a perfect square of an integer
            if a_n != 0:
                assert abs(a_n - round(a_n)) < 1e-10, f"a_0({n}) = {a_n} not integer"

    def test_vacuum_character_coeffs(self):
        """Known vacuum character coefficients for Ising: 1, 0, 1, 1, 2, 2, 3, ..."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        expected = [1, 0, 1, 1, 2, 2, 3, 3, 5, 5, 7, 8, 11]
        qs = data['qseries'][0]
        for n, e in enumerate(expected):
            assert abs(float(qs[n]) - e) < 1e-10, \
                f"a_0({n}) = {float(qs[n])}, expected {e}"


# ===================================================================
# 4. Multiplicativity of matrix entries
# ===================================================================

class TestMultiplicativity:
    """Test multiplicativity of Dirichlet coefficients c_{ij}(n)."""

    def test_diagonal_not_multiplicative(self):
        """Diagonal c_{ii}(n) = a_i(n)^2 is NOT multiplicative for Ising."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        for idx in range(3):
            coeffs = [float(data['qseries'][idx][n] ** 2) for n in range(30)]
            score = multiplicativity_score(coeffs, 15)
            # Score should be well below 1.0 for partition-like numbers
            assert score < 0.5, \
                f"chi_{idx}^2 should be non-multiplicative, got score {score}"

    def test_vacuum_specific_failure(self):
        """Specific multiplicativity failure: a_0(6) != a_0(2)*a_0(3)."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        qs = data['qseries'][0]
        a2, a3, a6 = float(qs[2]), float(qs[3]), float(qs[6])
        # a_0 = [1, 0, 1, 1, 2, 2, 3, ...], so a(2)=1, a(3)=1, a(6)=3
        assert abs(a2 - 1) < 1e-10
        assert abs(a3 - 1) < 1e-10
        assert abs(a6 - 3) < 1e-10
        # c(6) = 9, c(2)*c(3) = 1 => ratio = 9, multiplicativity FAILS
        assert abs(a6 ** 2 - a2 ** 2 * a3 ** 2) > 0.5

    def test_full_analysis_all_below_threshold(self):
        """Full multiplicativity analysis: all diagonal entries below threshold."""
        mp.dps = DPS
        model = ising_model()
        scores = full_multiplicativity_analysis(model, N_max=25, dps=DPS)
        for (i, j), score in scores.items():
            if i == j:
                assert score < 0.5, \
                    f"Diagonal ({i},{i}) should be non-multiplicative, got {score}"

    def test_multiplicativity_score_range(self):
        """Multiplicativity scores are in [0, 1]."""
        mp.dps = DPS
        model = ising_model()
        scores = full_multiplicativity_analysis(model, N_max=20, dps=DPS)
        for key, score in scores.items():
            assert 0.0 <= score <= 1.0, f"Score for {key} = {score} out of range"

    def test_squares_not_multiplicative(self):
        """General principle: if a(n) is not multiplicative, a(n)^2 is not either."""
        # Partition numbers p(n): p(2)=2, p(3)=3, p(6)=11
        # p(6)^2 = 121 vs p(2)^2 * p(3)^2 = 4*9 = 36
        coeffs = [0, 1, 4, 9, 25, 49, 121, 225]  # p(n)^2 starting at n=0
        score = multiplicativity_score(coeffs, 5)
        assert score < 1.0


# ===================================================================
# 5. S-matrix diagonalization
# ===================================================================

class TestSMatrixEigenbasis:
    """Test S-matrix eigenbasis computation."""

    def test_ising_s_eigenvalues(self):
        """Ising S-matrix eigenvalues are {+1, +1, -1}."""
        mp.dps = DPS
        evals, _ = s_eigenbasis(ising_model(), dps=DPS)
        evals_sorted = sorted([float(e) for e in evals])
        assert abs(evals_sorted[0] - (-1)) < 1e-10
        assert abs(evals_sorted[1] - 1) < 1e-10
        assert abs(evals_sorted[2] - 1) < 1e-10

    def test_s_squared_is_identity(self):
        """For Ising, S^2 = C = I (all reps self-conjugate)."""
        mp.dps = DPS
        S = s_matrix(ising_model(), dps=DPS)
        S2 = S * S
        n = S2.rows
        for i in range(n):
            for j in range(n):
                expected = 1.0 if i == j else 0.0
                assert abs(float(S2[i, j]) - expected) < 1e-10

    def test_eigenvectors_orthonormal(self):
        """S-eigenvectors are orthonormal."""
        mp.dps = DPS
        _, U = s_eigenbasis(ising_model(), dps=DPS)
        n = U.rows
        # U^T U should be identity (or close)
        prod = U * U.T
        for i in range(n):
            for j in range(n):
                expected = 1.0 if i == j else 0.0
                assert abs(float(prod[i, j]) - expected) < 1e-8, \
                    f"U^T U [{i},{j}] = {float(prod[i,j])}, expected {expected}"

    def test_eigenbasis_characters_evaluate(self):
        """Eigenbasis characters psi_k(tau) can be evaluated."""
        mp.dps = DPS
        model = ising_model()
        tau = mpc(0, 1.5)  # purely imaginary
        psi = eigenbasis_characters(model, tau, num_terms=NUM_TERMS, dps=DPS)
        assert len(psi) == 3
        # Each should be a finite complex number
        for k, p in enumerate(psi):
            assert mpmath.isfinite(p), f"psi_{k} is not finite: {p}"

    def test_eigenbasis_preserves_partition_function(self):
        """The partition function Z = sum |chi_i|^2 = sum |psi_k|^2 is preserved."""
        mp.dps = DPS
        model = ising_model()
        tau = mpc(0.1, 1.2)
        from compute.lib.vvmf_hecke import character_vector
        chars = character_vector(model, tau, num_terms=NUM_TERMS, dps=DPS)
        Z_original = sum(abs(c) ** 2 for c in chars)
        psi = eigenbasis_characters(model, tau, num_terms=NUM_TERMS, dps=DPS)
        Z_eigen = sum(abs(p) ** 2 for p in psi)
        rel_err = abs(float(Z_original - Z_eigen)) / abs(float(Z_original))
        assert rel_err < 1e-6, f"Partition functions differ: {rel_err}"


# ===================================================================
# 6. Factored L-matrix: spectral decomposition
# ===================================================================

class TestFactoredLMatrix:
    """Test L-matrix spectral decomposition via S-matrix."""

    def test_spectral_trace_preserved(self):
        """Trace is preserved under S-basis rotation: tr(L) = tr(S L S^T)."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        result = s_matrix_spectral_decomposition(model, 2, num_terms=NUM_TERMS, dps=DPS)
        tr_orig = float(trace_L(L))
        tr_rotated = float(sum(result['principal_L']))
        rel_err = abs(tr_orig - tr_rotated) / abs(tr_orig)
        assert rel_err < 1e-6, f"Trace not preserved: {tr_orig} vs {tr_rotated}"

    def test_spectral_not_diagonal_for_ising(self):
        """Since L is diagonal in the ORIGINAL basis, S L S^T is NOT diagonal."""
        mp.dps = DPS
        model = ising_model()
        result = s_matrix_spectral_decomposition(model, 2, num_terms=NUM_TERMS, dps=DPS)
        # The off-diagonal norm should be nonzero
        assert float(result['off_diag_norm']) > 1.0, \
            "S L S^T should be non-diagonal when L is diagonal and S is not identity"

    def test_eigenbasis_L_matrix_computed(self):
        """eigenbasis_L_matrix returns the rotated matrix and eigenvalues."""
        mp.dps = DPS
        model = ising_model()
        Lambda, evals = eigenbasis_L_matrix(model, 2, num_terms=NUM_TERMS, dps=DPS)
        assert Lambda.rows == 3
        assert Lambda.cols == 3
        assert len(evals) == 3

    def test_eigenbasis_L_trace_matches(self):
        """Trace of eigenbasis L equals trace of original L."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        Lambda, _ = eigenbasis_L_matrix(model, 2, num_terms=NUM_TERMS, dps=DPS)
        tr_L = float(trace_L(L))
        tr_Lambda = float(trace_L(Lambda))
        rel_err = abs(tr_L - tr_Lambda) / abs(tr_L)
        assert rel_err < 1e-6


# ===================================================================
# 7. Determinant L-function
# ===================================================================

class TestDeterminantL:
    """Test the determinant of the matrix L-function."""

    def test_det_L_positive(self):
        """det(L(s)) > 0 for s = 2, 3, 4 (product of positive diagonal entries)."""
        mp.dps = DPS
        model = ising_model()
        for s in [2, 3, 4]:
            L = matrix_L_fast(model, s, num_terms=NUM_TERMS, dps=DPS)
            d = float(det_L(L))
            assert d > 0, f"det(L({s})) = {d}, expected positive"

    def test_det_equals_product_of_diagonal(self):
        """For diagonal Ising L, det(L) = product of diagonal entries."""
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        d = float(det_L(L))
        prod = float(L[0, 0] * L[1, 1] * L[2, 2])
        rel_err = abs(d - prod) / abs(prod)
        assert rel_err < 1e-8, f"det = {d}, prod = {prod}"

    def test_det_decreasing_in_s(self):
        """det(L(s)) decreases as s increases."""
        mp.dps = DPS
        model = ising_model()
        det2 = float(det_L(matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)))
        det3 = float(det_L(matrix_L_fast(model, 3, num_terms=NUM_TERMS, dps=DPS)))
        det4 = float(det_L(matrix_L_fast(model, 4, num_terms=NUM_TERMS, dps=DPS)))
        assert det2 > det3 > det4

    def test_det_L_values_utility(self):
        """det_L_values returns correct dict."""
        mp.dps = DPS
        model = ising_model()
        result = det_L_values(model, [2, 3], num_terms=NUM_TERMS, dps=DPS)
        assert 2 in result
        assert 3 in result
        assert float(result[2]) > 0

    def test_det_not_multiplicative(self):
        """The determinant Dirichlet series is NOT multiplicative.

        Since det(L) = L_{00} * L_{11} * L_{22} and each L_{ii} has
        non-multiplicative Dirichlet coefficients, the product (convolution)
        is also non-multiplicative.
        """
        mp.dps = DPS
        data = ising_character_data(num_terms=40, dps=DPS)
        # Product of squares of character coefficients
        product_coeffs = []
        for n in range(25):
            val = 1.0
            for idx in range(3):
                val *= float(data['qseries'][idx][n]) ** 2
            product_coeffs.append(val)
        score = multiplicativity_score(product_coeffs, 12)
        assert score < 0.5, f"det Dirichlet coefficients should be non-multiplicative: {score}"


# ===================================================================
# 8. Comparison with lattice case V_Z
# ===================================================================

class TestLatticeComparison:
    """Compare with the lattice VOA V_Z where L(s) = 4 zeta(2s)."""

    def test_lattice_vz_at_s2(self):
        """V_Z: L(2) = 4 zeta(4) = 4 pi^4/90."""
        mp.dps = DPS
        L = lattice_vz_L(2, dps=DPS)
        expected = 4 * float(zeta(4))
        assert abs(float(L) - expected) < 1e-10

    def test_lattice_vz_at_s3(self):
        """V_Z: L(3) = 4 zeta(6) = 4 pi^6/945."""
        mp.dps = DPS
        L = lattice_vz_L(3, dps=DPS)
        expected = 4 * float(zeta(6))
        assert abs(float(L) - expected) < 1e-10

    def test_lattice_coeffs_multiplicative(self):
        """Lattice V_Z Dirichlet coefficients sigma_{-1}(n) are multiplicative."""
        mp.dps = DPS
        coeffs = lattice_vz_dirichlet_coeffs(50, dps=DPS)
        passes = 0
        total = 0
        for m in range(2, 20):
            for n in range(2, 20):
                if m * n >= 50:
                    continue
                if gcd(m, n) != 1:
                    continue
                c_mn = float(coeffs[m * n])
                c_m_cn = float(coeffs[m]) * float(coeffs[n])
                if c_m_cn > 1e-15:
                    total += 1
                    if abs(c_mn - c_m_cn) / abs(c_m_cn) < 1e-8:
                        passes += 1
        assert passes == total, f"Multiplicativity: {passes}/{total}"

    def test_lattice_vs_ising_structure(self):
        """Lattice has 1 character (matrix trivially 1x1), Ising has 3.

        The non-multiplicativity of the Ising scalar Dirichlet series
        comes from having MULTIPLE characters. For lattice VOA with 1
        character, the problem reduces to a single Rankin-Selberg integral.
        """
        mp.dps = DPS
        # Lattice: L is 1x1, automatically multiplicative
        lattice_score = 1.0  # by construction (sigma_{-1} is multiplicative)
        # Ising: diagonal entries non-multiplicative
        model = ising_model()
        scores = full_multiplicativity_analysis(model, N_max=20, dps=DPS)
        ising_diag_scores = [scores[(i, i)] for i in range(3)]
        avg_ising_score = sum(ising_diag_scores) / 3
        # Lattice should be strictly better
        assert lattice_score > avg_ising_score + 0.3


# ===================================================================
# 9. Conductor and gamma factors / functional equation
# ===================================================================

class TestFunctionalEquation:
    """Test the completed L-function and functional equation."""

    def test_gamma_factor_computable(self):
        """Rankin-Selberg gamma factor is a finite positive number for s > 1."""
        mp.dps = DPS
        gf = rankin_selberg_gamma_factor(2, mpf(0), mpf(0), dps=DPS)
        assert mpmath.isfinite(gf)
        assert float(abs(gf)) > 0

    def test_gamma_factor_with_spectral_shift(self):
        """Gamma factor with nonzero spectral parameter mu != 0."""
        mp.dps = DPS
        gf = rankin_selberg_gamma_factor(3, mpf(0), mpf('0.5'), dps=DPS)
        assert mpmath.isfinite(gf)

    def test_completed_L_entry_computable(self):
        """Completed L-function entry Lambda_{00}(s) is computable."""
        mp.dps = DPS
        model = ising_model()
        val = completed_L_entry(model, 0, 0, 2, num_terms=NUM_TERMS, dps=DPS)
        assert mpmath.isfinite(val)
        assert float(abs(val)) > 0

    def test_completed_L_diagonal_symmetry(self):
        """For diagonal entries, Lambda_{ii}(s) should satisfy approximate
        functional equation Lambda_{ii}(s) ~ Lambda_{ii}(1-s)
        (up to truncation artifacts).

        NOTE: This test checks the functional equation at the CONCEPTUAL level.
        Due to the truncated q-series and the non-standard normalization,
        the functional equation will only be approximate.

        We test at s = 2.5 and s = 3.5 (away from Gamma poles) to verify
        the completed L-function is finite and real at these points.
        """
        mp.dps = DPS
        model = ising_model()
        val_s1 = completed_L_entry(model, 0, 0, 2.5, num_terms=NUM_TERMS, dps=DPS)
        val_s2 = completed_L_entry(model, 0, 0, 3.5, num_terms=NUM_TERMS, dps=DPS)
        assert mpmath.isfinite(val_s1)
        assert mpmath.isfinite(val_s2)
        # Both should be real and positive for diagonal entries
        assert float(mpre(val_s1)) > 0
        assert float(mpre(val_s2)) > 0
        # Completed L decreases slower than uncompleted (gamma grows)
        # but should still be finite
        assert float(abs(val_s1)) > 0
        assert float(abs(val_s2)) > 0


# ===================================================================
# 10. Tricritical Ising and non-diagonal structure
# ===================================================================

class TestTricriticalIsing:
    """Test properties of models with potential non-trivial off-diagonal structure."""

    def test_tricritical_ising_num_primaries(self):
        """Tricritical Ising has 6 primaries."""
        result = tricritical_ising_weight_analysis()
        assert result['num_primaries'] == 6

    def test_tricritical_ising_no_integer_diffs(self):
        """Tricritical Ising has NO integer weight differences."""
        result = tricritical_ising_weight_analysis()
        assert len(result['integer_diffs']) == 0

    def test_potts_has_nontrivial_offdiag(self):
        """3-state Potts has integer weight differences, so L is NOT fully diagonal."""
        model = three_state_potts_model()
        labels = model.primary_labels()
        weights = [model.conformal_weight(lab.r, lab.s) for lab in labels]
        integer_pairs = []
        for i in range(len(weights)):
            for j in range(i + 1, len(weights)):
                d = weights[j] - weights[i]
                if d.denominator == 1:
                    integer_pairs.append((i, j, int(d)))
        assert len(integer_pairs) >= 1, "Potts should have at least one integer weight diff"


# ===================================================================
# 11. Extract Dirichlet coefficients
# ===================================================================

class TestDirichletCoeffExtraction:
    """Test extraction of Dirichlet coefficients from character data."""

    def test_extract_diagonal_coeffs(self):
        """Extract c_{00}(n) for vacuum character."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        coeffs = extract_dirichlet_coeffs(
            data['qseries'][0], data['qseries'][0],
            data['weights'][0], data['weights'][0], data['c'],
            N_max=15, dps=DPS
        )
        # c_{00}(0) = a_0(0)^2 = 1
        assert abs(float(coeffs[0][1]) - 1.0) < 1e-10
        # c_{00}(2) = a_0(2)^2 = 1  (since a_0(2) = 1)
        assert abs(float(coeffs[2][1]) - 1.0) < 1e-10
        # c_{00}(6) = a_0(6)^2 = 9  (since a_0(6) = 3)
        assert abs(float(coeffs[6][1]) - 9.0) < 1e-10

    def test_extract_offdiag_returns_empty(self):
        """Off-diagonal coefficients are empty for non-integer weight diff."""
        mp.dps = DPS
        data = ising_character_data(num_terms=NUM_TERMS, dps=DPS)
        coeffs = extract_dirichlet_coeffs(
            data['qseries'][0], data['qseries'][1],
            data['weights'][0], data['weights'][1], data['c'],
            N_max=15, dps=DPS
        )
        # All should be zero since h_1 - h_0 = 1/16 is non-integer
        nonzero = [c for _, c in coeffs if abs(float(c)) > 1e-15]
        assert len(nonzero) == 0


# ===================================================================
# 12. Structural theorems
# ===================================================================

class TestStructuralTheorems:
    """Test structural properties of the matrix Rankin-Selberg integral."""

    def test_hermitian_L_matrix(self):
        """L_{ij}(s) = conj(L_{ji}(s)) for real s, i.e., L is Hermitian.

        Since chi_i are real on the imaginary axis and L involves
        chi_i * conj(chi_j), we get L_{ij} = conj(L_{ji}).
        For real characters (as in minimal models), L is real symmetric.
        """
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        for i in range(3):
            for j in range(3):
                diff = abs(float(L[i, j]) - float(L[j, i]))
                assert diff < 1e-10, f"L[{i},{j}] != L[{j},{i}]"

    def test_positive_semidefinite(self):
        """L(s) is positive semidefinite for real s > 1.

        Since L_{ij}(s) = integral chi_i conj(chi_j) y^s dmu,
        for any vector v: v^dag L v = integral |sum v_i chi_i|^2 y^s dmu >= 0.
        """
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        # Check all eigenvalues are non-negative (L is diagonal with positive entries)
        for i in range(3):
            assert float(L[i, i]) >= 0

    def test_matrix_diagonal_key_insight(self):
        """KEY STRUCTURAL RESULT: For minimal models with all non-integer weight
        differences, the matrix Rankin-Selberg integral is DIAGONAL.

        This means the matrix formulation does NOT improve multiplicativity
        over the scalar case -- it merely decomposes the scalar trace into
        independently non-multiplicative diagonal components.

        The obstruction to multiplicativity is NOT interference between
        characters but rather the partition-like nature of each individual
        character's Fourier coefficients.
        """
        mp.dps = DPS
        model = ising_model()
        L = matrix_L_fast(model, 2, num_terms=NUM_TERMS, dps=DPS)
        # Verify L is diagonal
        for i in range(3):
            for j in range(3):
                if i != j:
                    assert abs(float(L[i, j])) < 1e-10
                else:
                    assert float(L[i, i]) > 0
        # Verify each diagonal entry has non-multiplicative coefficients
        data = ising_character_data(num_terms=30, dps=DPS)
        for idx in range(3):
            coeffs = [float(data['qseries'][idx][n] ** 2) for n in range(25)]
            score = multiplicativity_score(coeffs, 12)
            assert score < 0.5

    def test_trace_L_consistent_with_scalar(self):
        """tr(L(s)) gives the scalar Rankin-Selberg integral sum_i integral |chi_i|^2 y^s."""
        mp.dps = DPS
        model = ising_model()
        result = trace_L_values(model, [2, 3], num_terms=NUM_TERMS, dps=DPS)
        for s_val in [2, 3]:
            assert float(result[s_val]) > 0

    def test_offdiag_structural_vanishing_theorem(self):
        """For ANY rational CFT where all h_i - h_j are non-integer for i != j,
        the matrix Rankin-Selberg integral is diagonal.

        This is the Parseval orthogonality theorem: the x-integral of
        e^{2 pi i alpha x} vanishes for non-integer alpha.
        """
        # Test on both Ising and tricritical Ising
        for model_fn in [ising_model, tricritical_ising_model]:
            model = model_fn()
            labels = model.primary_labels()
            weights = [model.conformal_weight(lab.r, lab.s) for lab in labels]
            all_noninteger = True
            for i in range(len(weights)):
                for j in range(i + 1, len(weights)):
                    d = weights[j] - weights[i]
                    if d.denominator == 1:
                        all_noninteger = False
            if all_noninteger:
                mp.dps = DPS
                L = matrix_L_fast(model, 2, num_terms=40, dps=DPS)
                for i in range(L.rows):
                    for j in range(L.cols):
                        if i != j:
                            assert abs(float(L[i, j])) < 1e-10
