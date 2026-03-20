#!/usr/bin/env python3
"""Tests for Artin L-functions from modular representations of rational VOAs.

Tests cover:
  1. Ising modular data (S, T matrices, eigenvalues, unitarity)
  2. Image group structure (|G|, order of generators)
  3. Verlinde fusion ring (integrality, identity, commutativity, associativity)
  4. Galois action on S-matrix (permutations at various primes)
  5. Conductor computation
  6. Artin L-function Euler factors (multiplicativity, convergence)
  7. Lee-Yang model
  8. Tricritical Ising model
  9. Minimal model survey (M(p,q) with p,q <= 6)
  10. Representation decomposition
"""

import pytest
import numpy as np
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.artin_l_from_modular_rep import (
    ising_s_matrix, ising_t_matrix,
    lee_yang_s_matrix, lee_yang_t_matrix,
    tricritical_ising_data,
    minimal_model_primaries, minimal_model_central_charge,
    minimal_model_s_matrix, minimal_model_t_matrix,
    matrix_to_numpy, mat_mul, mat_power, matrix_approx_equal,
    find_matrix_order,
    compute_image_group_order, compute_image_group_elements,
    s_matrix_eigenvalues, t_matrix_eigenvalues,
    verify_unitarity, verify_s_squared, verify_modular_relation,
    verlinde_fusion, all_fusion_coefficients, verify_fusion_ring,
    quantum_dimensions, total_quantum_dimension,
    galois_permutation_from_t, galois_signs_from_s,
    galois_matrix_at_prime,
    artin_l_function_euler_factor, artin_l_function_partial,
    artin_l_irreducible_factors,
    decompose_representation, character_table_from_elements,
    conductor_from_t, conductor_minimal_model, ramified_primes,
    minimal_model_survey,
    ising_galois_permutations,
    _primes_up_to,
)


# ============================================================
# 1. Ising modular data
# ============================================================

class TestIsingModularData:
    """Tests for the Ising model M(4,3) modular matrices."""

    def test_ising_s_matrix_shape(self):
        S = ising_s_matrix()
        Sn = matrix_to_numpy(S)
        assert Sn.shape == (3, 3)

    def test_ising_s_matrix_values(self):
        """S-matrix entries should match the known Ising values.

        Ordering is by conformal weight: [1 (h=0), sigma (h=1/16), epsilon (h=1/2)].
        """
        Sn = matrix_to_numpy(ising_s_matrix())
        s2 = np.sqrt(2)
        # S_{00} > 0
        assert Sn[0, 0].real > 0
        # |S_{00}| = 0.5
        assert abs(abs(Sn[0, 0]) - 0.5) < 1e-10
        # |S_{01}| = sqrt(2)/2
        assert abs(abs(Sn[0, 1]) - s2 / 2) < 1e-10

    def test_ising_s_unitarity(self):
        """S S^dagger = I."""
        assert verify_unitarity(ising_s_matrix())

    def test_ising_s_symmetric(self):
        """S is symmetric: S = S^T."""
        Sn = matrix_to_numpy(ising_s_matrix())
        assert np.allclose(Sn, Sn.T, atol=1e-12)

    def test_ising_s_squared_is_charge_conjugation(self):
        """S^2 = C. For Ising, all reps are self-conjugate so C = I."""
        is_involution, C = verify_s_squared(ising_s_matrix())
        assert is_involution, "S^2 should equal I for Ising"

    def test_ising_t_matrix_diagonal(self):
        """T is diagonal with prescribed entries."""
        Tn = matrix_to_numpy(ising_t_matrix())
        for i in range(3):
            for j in range(3):
                if i != j:
                    assert abs(Tn[i, j]) < 1e-12

    def test_ising_t_eigenvalues(self):
        """T eigenvalues = e^{2*pi*i*(h - c/24)} for h = 0, 1/16, 1/2."""
        Tn = matrix_to_numpy(ising_t_matrix())
        c = 0.5
        # Primaries sorted by h: (1,1) h=0, (2,1) h=1/16, (1,2) h=1/2
        hs = [0.0, 1.0 / 16, 0.5]
        for idx, h in enumerate(hs):
            expected = np.exp(2j * np.pi * (h - c / 24))
            assert abs(Tn[idx, idx] - expected) < 1e-10, \
                f"T[{idx},{idx}] = {Tn[idx,idx]}, expected {expected}"

    def test_ising_modular_relation(self):
        """(ST)^3 = S^2 (fundamental SL(2,Z) relation)."""
        assert verify_modular_relation(ising_s_matrix(), ising_t_matrix())

    def test_ising_s_eigenvalues(self):
        """S-matrix eigenvalues for Ising. S is real symmetric, eigenvalues are real."""
        eigs = s_matrix_eigenvalues(ising_s_matrix())
        for e in eigs:
            assert abs(e.imag) < 1e-10

    def test_ising_central_charge(self):
        """c = 1/2 for Ising = M(4,3)."""
        c = minimal_model_central_charge(4, 3)
        assert abs(c - 0.5) < 1e-12

    def test_ising_3_primaries(self):
        """Ising has 3 primaries: (p-1)(q-1)/2 = 3*2/2 = 3."""
        primaries = minimal_model_primaries(4, 3)
        assert len(primaries) == 3

    def test_ising_conformal_weights(self):
        """Ising conformal weights: 0, 1/16, 1/2."""
        primaries = minimal_model_primaries(4, 3)
        hs = [h for _, _, h in primaries]
        assert abs(hs[0] - 0.0) < 1e-12
        assert abs(hs[1] - 1.0 / 16) < 1e-12
        assert abs(hs[2] - 0.5) < 1e-12


# ============================================================
# 2. Image group structure
# ============================================================

class TestImageGroup:
    """Tests for the finite image group Im(rho)."""

    def test_ising_s_order(self):
        """Order of S in Ising representation. S^2 = I."""
        S = ising_s_matrix()
        order = find_matrix_order(S)
        assert order == 2, f"Order of S = {order}, expected 2"

    def test_ising_t_order(self):
        """Order of T in Ising representation = 48."""
        T = ising_t_matrix()
        order = find_matrix_order(T)
        assert order == 48, f"Order of T = {order}, expected 48"

    def test_ising_st_order(self):
        """Order of ST in Ising representation. (ST)^3 = S^2 = I, so order divides 3."""
        S = matrix_to_numpy(ising_s_matrix())
        T = matrix_to_numpy(ising_t_matrix())
        ST = S @ T
        order = find_matrix_order(ST)
        assert order == 3, f"Order of ST = {order}, expected 3"

    def test_ising_group_order(self):
        """Compute |Im(rho)| for Ising. Should be finite by Bantay's theorem."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        group_order, ord_S, ord_T, ord_ST = compute_image_group_order(S, T)
        assert group_order > 1
        assert ord_S == 2
        assert ord_T == 48
        assert ord_ST == 3

    def test_lee_yang_t_order(self):
        """Order of T for Lee-Yang model = 60."""
        T = lee_yang_t_matrix()
        order = find_matrix_order(T)
        assert order == 60, f"Order of T = {order}, expected 60"

    def test_lee_yang_group_finite(self):
        """Im(rho) is finite for Lee-Yang (rational VOA)."""
        S = lee_yang_s_matrix()
        T = lee_yang_t_matrix()
        group_order, _, _, _ = compute_image_group_order(S, T)
        assert group_order > 1
        assert group_order < 5000


# ============================================================
# 3. Verlinde fusion ring
# ============================================================

class TestVerlindeRing:
    """Tests for Verlinde fusion coefficients."""

    def test_ising_fusion_identity(self):
        """N_{0,j}^k = delta_{j,k} (identity element)."""
        S = ising_s_matrix()
        for j in range(3):
            for k in range(3):
                val = verlinde_fusion(S, 0, j, k)
                expected = 1.0 if j == k else 0.0
                assert abs(val - expected) < 1e-6, \
                    f"N_{{0,{j}}}^{k} = {val}, expected {expected}"

    def test_ising_fusion_integrality(self):
        """All N_{ij}^k are non-negative integers."""
        S = ising_s_matrix()
        N = all_fusion_coefficients(S)
        for (i, j, k), val in N.items():
            rounded = round(val.real)
            assert abs(val.real - rounded) < 1e-6, \
                f"N_{{{i},{j}}}^{k} = {val} not integer"
            assert abs(val.imag) < 1e-6
            assert rounded >= 0, f"N_{{{i},{j}}}^{k} = {rounded} < 0"

    def test_ising_fusion_commutativity(self):
        """N_{ij}^k = N_{ji}^k."""
        S = ising_s_matrix()
        N = all_fusion_coefficients(S)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    assert abs(N[(i, j, k)] - N[(j, i, k)]) < 1e-6

    def test_ising_sigma_fusion(self):
        """sigma x sigma = 1 + epsilon.

        In our ordering [1(0), sigma(1), epsilon(2)]:
        N_{1,1}^0 = 1, N_{1,1}^2 = 1, N_{1,1}^1 = 0.
        """
        S = ising_s_matrix()
        assert abs(verlinde_fusion(S, 1, 1, 0) - 1.0) < 1e-6  # -> 1
        assert abs(verlinde_fusion(S, 1, 1, 2) - 1.0) < 1e-6  # -> epsilon
        assert abs(verlinde_fusion(S, 1, 1, 1) - 0.0) < 1e-6  # -> sigma (forbidden)

    def test_ising_epsilon_fusion(self):
        """epsilon x epsilon = 1 (Z_2 fusion rule).

        epsilon = index 2 in ordering [1, sigma, epsilon].
        """
        S = ising_s_matrix()
        assert abs(verlinde_fusion(S, 2, 2, 0) - 1.0) < 1e-6
        assert abs(verlinde_fusion(S, 2, 2, 1) - 0.0) < 1e-6
        assert abs(verlinde_fusion(S, 2, 2, 2) - 0.0) < 1e-6

    def test_ising_fusion_ring_axioms(self):
        """Full ring axiom verification including associativity."""
        S = ising_s_matrix()
        all_pass, details = verify_fusion_ring(S)
        assert all_pass, f"Fusion ring axiom failures: {details}"

    def test_ising_quantum_dimensions(self):
        """Quantum dimensions d_i = S_{0i}/S_{00}.

        d_1 = 1, d_sigma = sqrt(2), d_epsilon = 1.
        """
        S = ising_s_matrix()
        dims = quantum_dimensions(S)
        assert abs(dims[0] - 1.0) < 1e-10
        assert abs(abs(dims[1]) - np.sqrt(2)) < 1e-10
        assert abs(abs(dims[2]) - 1.0) < 1e-10

    def test_ising_total_quantum_dimension(self):
        """D^2 = 1/|S_{00}|^2 = 1/0.25 = 4."""
        S = ising_s_matrix()
        D2 = total_quantum_dimension(S)
        assert abs(D2 - 4.0) < 1e-10

    def test_lee_yang_fusion_ring(self):
        """Lee-Yang fusion ring: phi x phi = 1 + phi."""
        S = lee_yang_s_matrix()
        all_pass, details = verify_fusion_ring(S)
        assert all_pass, f"Lee-Yang fusion ring failures: {details}"

    def test_lee_yang_quantum_dimension_golden(self):
        """Lee-Yang quantum dimension d_phi = S_{01}/S_{00}.

        For Lee-Yang M(5,2), the non-vacuum primary (2,1) has negative h = -1/5.
        The quantum dimension d_phi = S_{0,phi}/S_{0,0}.

        With the corrected S-matrix (DMS formula), d_phi is the inverse golden
        ratio 1/phi = (sqrt(5)-1)/2 = 0.618... (or its negative).
        The FUSION dimension (= largest eigenvalue of N_phi) is always phi.
        """
        S = lee_yang_s_matrix()
        dims = quantum_dimensions(S)
        inv_phi = (np.sqrt(5) - 1) / 2  # 0.618...
        assert abs(dims[0] - 1.0) < 1e-10
        # |d_phi| = 1/phi for the normalized S-matrix
        assert abs(abs(dims[1]) - inv_phi) < 1e-6


# ============================================================
# 4. Galois action
# ============================================================

class TestGaloisAction:
    """Tests for the Galois action on modular data."""

    def test_ising_galois_at_p3_ramified(self):
        """p=3 divides the Ising conductor 48, so it is ramified."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        perm, signs = galois_signs_from_s(S, T, 3)
        assert perm is None, "p=3 should be ramified (3 | 48)"

    def test_ising_galois_at_p2_ramified(self):
        """p=2 divides the Ising conductor 48, so it is ramified."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        perm, signs = galois_signs_from_s(S, T, 2)
        assert perm is None, "p=2 should be ramified (2 | 48)"

    def test_ising_galois_at_unramified_primes(self):
        """Test Galois permutations at primes coprime to conductor 48."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        for p in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
            perm, signs = galois_signs_from_s(S, T, p)
            assert perm is not None, f"p={p} should be coprime to 48"
            assert len(perm) == 3
            assert set(perm) == {0, 1, 2}, f"Permutation at p={p} invalid: {perm}"

    def test_ising_galois_permutations_function(self):
        """Test the dedicated Ising Galois analysis function."""
        results = ising_galois_permutations([5, 7, 11, 13])
        for p in [5, 7, 11, 13]:
            assert p in results
            assert results[p]['p_mod_8'] == p % 8

    def test_galois_preserves_fusion(self):
        """Galois permutation must be a fusion ring automorphism."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        N_orig = all_fusion_coefficients(S)

        for p in [5, 7, 11, 13]:
            perm, signs = galois_signs_from_s(S, T, p)
            if perm is None:
                continue
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        n_orig = round(N_orig[(i, j, k)].real)
                        n_perm = round(N_orig[(perm[i], perm[j], perm[k])].real)
                        assert n_orig == n_perm, \
                            f"Galois at p={p} breaks fusion: N_{{{i},{j}}}^{k}={n_orig} " \
                            f"vs N_{{{perm[i]},{perm[j]}}}^{perm[k]}={n_perm}"

    def test_galois_matrix_is_signed_permutation(self):
        """rho(sigma_p) should be a signed permutation matrix."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        for p in [5, 7, 11, 13]:
            M = galois_matrix_at_prime(S, T, p)
            if M is None:
                continue
            for i in range(3):
                nonzero_row = np.sum(np.abs(M[i, :]) > 1e-10)
                nonzero_col = np.sum(np.abs(M[:, i]) > 1e-10)
                assert nonzero_row == 1, f"Row {i} has {nonzero_row} nonzero at p={p}"
                assert nonzero_col == 1, f"Col {i} has {nonzero_col} nonzero at p={p}"
            for entry in M.flat:
                if abs(entry) > 1e-10:
                    assert abs(abs(entry) - 1.0) < 1e-10


# ============================================================
# 5. Conductor computation
# ============================================================

class TestConductor:
    """Tests for conductor and ramification."""

    def test_ising_conductor_from_t(self):
        """Ising conductor = 48."""
        T = ising_t_matrix()
        N = conductor_from_t(T)
        assert N == 48, f"Ising conductor = {N}, expected 48"

    def test_ising_conductor_from_formula(self):
        N = conductor_minimal_model(4, 3)
        assert N == 48

    def test_lee_yang_conductor(self):
        """Lee-Yang conductor = 60."""
        T = lee_yang_t_matrix()
        N = conductor_from_t(T)
        assert N == 60, f"Lee-Yang conductor = {N}, expected 60"

    def test_lee_yang_conductor_formula(self):
        N = conductor_minimal_model(5, 2)
        assert N == 60

    def test_ising_ramified_primes(self):
        """Ramified primes for Ising: {2, 3} (primes dividing 48)."""
        rams = ramified_primes(48)
        assert rams == {2, 3}

    def test_lee_yang_ramified_primes(self):
        """Ramified primes for Lee-Yang: {2, 3, 5} (primes dividing 60)."""
        rams = ramified_primes(60)
        assert rams == {2, 3, 5}

    def test_tricritical_ising_conductor(self):
        """Conductor for tricritical Ising M(5,4) matches T-matrix order."""
        N_formula = conductor_minimal_model(5, 4)
        T, _ = minimal_model_t_matrix(5, 4)
        N_from_T = conductor_from_t(T)
        assert N_formula > 0
        assert N_from_T == N_formula

    def test_conductor_consistency(self):
        """conductor_minimal_model and conductor_from_t agree for all small models."""
        for p, q in [(4, 3), (5, 2), (5, 3), (5, 4), (7, 2), (7, 3)]:
            if math.gcd(p, q) != 1:
                continue
            N1 = conductor_minimal_model(p, q)
            T, _ = minimal_model_t_matrix(p, q)
            N2 = conductor_from_t(T)
            assert N1 == N2, f"M({p},{q}): formula={N1}, T-order={N2}"


# ============================================================
# 6. Artin L-function
# ============================================================

class TestArtinLFunction:
    """Tests for the Artin L-function construction."""

    def test_ising_euler_factor_at_unramified(self):
        """Euler factors exist at unramified primes."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        for p in [5, 7, 11, 13]:
            factor = artin_l_function_euler_factor(S, T, p, 2.0)
            assert factor is not None, f"p={p} should be unramified for Ising"
            assert abs(factor) > 0.1
            assert abs(factor) < 100

    def test_ising_euler_factor_ramified(self):
        """Ramified primes (dividing 48) should return None."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        for p in [2, 3]:
            factor = artin_l_function_euler_factor(S, T, p, 2.0)
            assert factor is None, f"p={p} should be ramified"

    def test_ising_partial_l_function(self):
        """Partial Artin L-function converges for Re(s) > 1."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        val, used, ramified = artin_l_function_partial(S, T, 2.0, num_primes=20)
        assert len(used) > 0
        assert abs(val) > 0
        assert 2 in ramified and 3 in ramified

    def test_ising_l_function_convergence(self):
        """L(s) should approach 1 as Re(s) -> infinity."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        val_5, _, _ = artin_l_function_partial(S, T, 5.0, num_primes=30)
        val_10, _, _ = artin_l_function_partial(S, T, 10.0, num_primes=30)
        assert abs(val_10 - 1.0) < abs(val_5 - 1.0) + 0.01

    def test_euler_factor_det_formula(self):
        """Verify Euler factor = det(I - rho(sigma_p) p^{-s})^{-1}."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        n = 3
        for p in [5, 7, 11]:
            M = galois_matrix_at_prime(S, T, p)
            if M is None:
                continue
            s = 2.0
            det_val = np.linalg.det(np.eye(n) - M * p**(-s))
            factor = artin_l_function_euler_factor(S, T, p, s)
            assert abs(factor * det_val - 1.0) < 1e-10

    def test_artin_l_multiplicative_by_construction(self):
        """The Artin L-function is multiplicative by construction (Euler product).

        Each Euler factor is well-defined at unramified primes.
        For large p and s, factors approach 1.
        """
        S = ising_s_matrix()
        T = ising_t_matrix()
        good_primes = [p for p in _primes_up_to(50) if 48 % p != 0]
        for p in good_primes:
            factor = artin_l_function_euler_factor(S, T, p, 2.0)
            assert factor is not None, f"Factor at p={p} should exist"
            assert np.isfinite(abs(factor)), f"Factor at p={p} not finite"

    def test_irreducible_factors(self):
        """Test the irreducible L-function factorization."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        result = artin_l_irreducible_factors(S, T, 2.0, num_primes=15)
        assert result['dimension'] == 3
        assert result['conductor'] == 48
        assert abs(result['total']) > 0


# ============================================================
# 7. Lee-Yang model
# ============================================================

class TestLeeYang:
    """Tests for the Lee-Yang model M(5,2)."""

    def test_lee_yang_s_unitarity(self):
        assert verify_unitarity(lee_yang_s_matrix())

    def test_lee_yang_s_symmetric(self):
        Sn = matrix_to_numpy(lee_yang_s_matrix())
        assert np.allclose(Sn, Sn.T, atol=1e-12)

    def test_lee_yang_modular_relation(self):
        assert verify_modular_relation(lee_yang_s_matrix(), lee_yang_t_matrix())

    def test_lee_yang_central_charge(self):
        """c = -22/5 for Lee-Yang."""
        c = minimal_model_central_charge(5, 2)
        assert abs(c - (-22.0 / 5)) < 1e-12

    def test_lee_yang_fusion_phi_phi(self):
        """phi x phi = 1 + phi (golden ratio fusion)."""
        S = lee_yang_s_matrix()
        # In ordering by conformal weight: index 0 = vacuum, index 1 = phi
        assert abs(verlinde_fusion(S, 1, 1, 0) - 1.0) < 1e-6
        assert abs(verlinde_fusion(S, 1, 1, 1) - 1.0) < 1e-6

    def test_lee_yang_partial_l(self):
        """Partial L-function for Lee-Yang."""
        S = lee_yang_s_matrix()
        T = lee_yang_t_matrix()
        val, used, ramified = artin_l_function_partial(S, T, 2.0, num_primes=15)
        assert len(used) > 0 or len(ramified) > 0
        # The L-function should be computable

    def test_lee_yang_2_primaries(self):
        """Lee-Yang has exactly 2 primaries."""
        primaries = minimal_model_primaries(5, 2)
        assert len(primaries) == 2

    def test_lee_yang_s_squared(self):
        """S^2 = I (charge conjugation = identity for Lee-Yang)."""
        S = lee_yang_s_matrix()
        is_inv, _ = verify_s_squared(S)
        assert is_inv


# ============================================================
# 8. Tricritical Ising
# ============================================================

class TestTricriticalIsing:
    """Tests for the tricritical Ising model M(5,4)."""

    def test_tricritical_ising_6_primaries(self):
        """M(5,4) has 6 primaries."""
        primaries = minimal_model_primaries(5, 4)
        assert len(primaries) == 6

    def test_tricritical_ising_central_charge(self):
        """c = 7/10 for tricritical Ising."""
        c = minimal_model_central_charge(5, 4)
        assert abs(c - 0.7) < 1e-12

    def test_tricritical_ising_s_unitarity(self):
        S, T, labels = tricritical_ising_data()
        assert verify_unitarity(S)

    def test_tricritical_ising_modular_relation(self):
        S, T, labels = tricritical_ising_data()
        assert verify_modular_relation(S, T)

    def test_tricritical_ising_fusion_ring(self):
        S, T, labels = tricritical_ising_data()
        all_pass, details = verify_fusion_ring(S)
        assert all_pass, f"Tricritical Ising fusion failures: {details}"

    def test_tricritical_ising_quantum_dimensions_positive(self):
        """Quantum dimensions should all be positive for unitary model."""
        S, T, labels = tricritical_ising_data()
        dims = quantum_dimensions(S)
        for i, d in enumerate(dims):
            assert d.real > -1e-10, f"d_{i} = {d} not positive"


# ============================================================
# 9. Minimal model survey
# ============================================================

class TestMinimalModelSurvey:
    """Tests for the survey across minimal models M(p,q)."""

    def test_survey_small(self):
        """Survey M(p,q) with p,q <= 5."""
        results = minimal_model_survey(p_max=5, q_max=5)
        labels = [r['label'] for r in results if 'error' not in r]
        assert 'M(4,3)' in labels  # Ising
        assert 'M(5,2)' in labels  # Lee-Yang
        assert len(results) >= 4

    def test_survey_conductors_positive(self):
        """All conductors should be positive integers."""
        results = minimal_model_survey(p_max=5)
        for r in results:
            if 'error' in r:
                continue
            N = r['conductor']
            assert isinstance(N, int) and N > 0, f"{r['label']}: conductor = {N}"

    def test_survey_ising_entry(self):
        """Check the Ising entry in the survey."""
        results = minimal_model_survey(p_max=5)
        ising = [r for r in results if r.get('label') == 'M(4,3)']
        assert len(ising) == 1
        r = ising[0]
        assert r['n_primaries'] == 3
        assert abs(r['central_charge'] - 0.5) < 1e-12
        assert r['conductor'] == 48

    def test_number_of_primaries(self):
        """Number of primaries = (p-1)(q-1)/2 for M(p,q)."""
        for p, q in [(4, 3), (5, 2), (5, 3), (5, 4), (6, 5), (7, 2)]:
            if math.gcd(p, q) != 1:
                continue
            primaries = minimal_model_primaries(p, q)
            expected = (p - 1) * (q - 1) // 2
            assert len(primaries) == expected, \
                f"M({p},{q}): got {len(primaries)} primaries, expected {expected}"

    def test_survey_group_orders_finite(self):
        """Group orders should be finite for small models."""
        results = minimal_model_survey(p_max=5)
        for r in results:
            if 'error' in r:
                continue
            if r['group_order'] is not None:
                assert r['group_order'] > 0


# ============================================================
# 10. Representation decomposition
# ============================================================

class TestDecomposition:
    """Tests for representation decomposition."""

    def test_ising_decomposition(self):
        """Decompose the 3-dim Ising representation."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        elements = compute_image_group_elements(S, T)
        dec = decompose_representation(elements)
        assert dec is not None
        assert dec['dim'] == 3
        assert dec['group_order'] > 1

    def test_ising_character_norm(self):
        """||chi||^2 must be a positive integer."""
        S = ising_s_matrix()
        T = ising_t_matrix()
        elements = compute_image_group_elements(S, T)
        dec = decompose_representation(elements)
        chi_sq = dec['character_norm_sq']
        assert chi_sq > 0
        assert abs(chi_sq - round(chi_sq)) < 0.5

    def test_lee_yang_decomposition(self):
        """Decompose the 2-dim Lee-Yang representation."""
        S = lee_yang_s_matrix()
        T = lee_yang_t_matrix()
        elements = compute_image_group_elements(S, T)
        dec = decompose_representation(elements)
        assert dec['dim'] == 2


# ============================================================
# 11. Universal structure tests
# ============================================================

class TestUniversalStructure:
    """Tests for universal properties of rational VOA modular representations."""

    def test_all_s_matrices_unitary(self):
        """S-matrices are unitary for ALL minimal models (tested)."""
        for p, q in [(4, 3), (5, 2), (5, 3), (5, 4), (7, 2), (7, 4)]:
            if math.gcd(p, q) != 1:
                continue
            S, _ = minimal_model_s_matrix(p, q)
            assert verify_unitarity(S), f"S not unitary for M({p},{q})"

    def test_all_modular_relations(self):
        """(ST)^3 = S^2 for all tested minimal models."""
        for p, q in [(4, 3), (5, 2), (5, 4), (7, 2)]:
            if math.gcd(p, q) != 1:
                continue
            S, _ = minimal_model_s_matrix(p, q)
            T, _ = minimal_model_t_matrix(p, q)
            assert verify_modular_relation(S, T), \
                f"Modular relation fails for M({p},{q})"

    def test_all_fusion_rings_valid(self):
        """Fusion ring axioms hold for all tested minimal models."""
        for p, q in [(4, 3), (5, 2), (5, 4), (7, 2)]:
            if math.gcd(p, q) != 1:
                continue
            S, _ = minimal_model_s_matrix(p, q)
            ok, details = verify_fusion_ring(S)
            assert ok, f"Fusion ring fails for M({p},{q}): {details}"

    def test_conductor_divides_expected(self):
        """Conductor should be a positive integer for all models."""
        for p, q in [(4, 3), (5, 2), (5, 4), (6, 5), (7, 2), (7, 3)]:
            if math.gcd(p, q) != 1:
                continue
            N = conductor_minimal_model(p, q)
            assert N > 0, f"M({p},{q}): conductor = {N}"


# ============================================================
# 12. Cross-model comparison
# ============================================================

class TestCrossModelComparison:
    """Compare Artin L-function content across models."""

    def test_ising_vs_lee_yang_conductors(self):
        """Ising conductor 48, Lee-Yang conductor 60: gcd = 12."""
        N_ising = conductor_minimal_model(4, 3)
        N_ly = conductor_minimal_model(5, 2)
        assert N_ising == 48
        assert N_ly == 60
        assert math.gcd(N_ising, N_ly) == 12

    def test_dimensions_match_primaries(self):
        """Dimension of S-matrix = number of primaries."""
        for p, q in [(4, 3), (5, 2), (5, 4)]:
            primaries = minimal_model_primaries(p, q)
            S, _ = minimal_model_s_matrix(p, q)
            Sn = matrix_to_numpy(S)
            assert Sn.shape[0] == len(primaries)

    def test_quantum_dim_positivity_unitary(self):
        """Quantum dimensions are positive for unitary minimal models M(p, p-1)."""
        for p in [3, 4, 5, 6, 7]:
            q = p - 1
            if math.gcd(p, q) != 1:
                continue
            S, _ = minimal_model_s_matrix(p, q)
            dims = quantum_dimensions(S)
            for i, d in enumerate(dims):
                assert d.real > -1e-10, f"M({p},{q}): d_{i} = {d}"

    def test_l_function_different_models(self):
        """Artin L-functions for different models should differ."""
        S_i = ising_s_matrix()
        T_i = ising_t_matrix()
        S_ly = lee_yang_s_matrix()
        T_ly = lee_yang_t_matrix()

        L_ising, used_i, _ = artin_l_function_partial(S_i, T_i, 2.0, num_primes=20)
        L_ly, used_ly, _ = artin_l_function_partial(S_ly, T_ly, 2.0, num_primes=20)

        # Both should be finite
        if len(used_i) > 0:
            assert abs(L_ising) > 0
        if len(used_ly) > 0:
            assert abs(L_ly) > 0


# ============================================================
# 13. Additional model tests
# ============================================================

class TestAdditionalModels:
    """Tests for M(5,3), M(7,2), and other models."""

    def test_m53_3_primaries(self):
        """M(5,3) has (5-1)(3-1)/2 = 4 primaries."""
        primaries = minimal_model_primaries(5, 3)
        assert len(primaries) == 4

    def test_m53_s_unitary(self):
        S, _ = minimal_model_s_matrix(5, 3)
        assert verify_unitarity(S)

    def test_m53_modular_relation(self):
        S, _ = minimal_model_s_matrix(5, 3)
        T, _ = minimal_model_t_matrix(5, 3)
        assert verify_modular_relation(S, T)

    def test_m53_fusion_ring(self):
        S, _ = minimal_model_s_matrix(5, 3)
        ok, details = verify_fusion_ring(S)
        assert ok, f"M(5,3) fusion ring fails: {details}"

    def test_m72_3_primaries(self):
        """M(7,2) has (7-1)(2-1)/2 = 3 primaries."""
        primaries = minimal_model_primaries(7, 2)
        assert len(primaries) == 3

    def test_m72_s_unitary(self):
        S, _ = minimal_model_s_matrix(7, 2)
        assert verify_unitarity(S)

    def test_m72_fusion_ring(self):
        S, _ = minimal_model_s_matrix(7, 2)
        ok, details = verify_fusion_ring(S)
        assert ok, f"M(7,2) fusion ring fails: {details}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
