r"""Tests for quantum groups at roots of unity: shadow obstruction tower
and 3-manifold invariants.

Multi-path verification structure:
  Path 1: Direct quantum group computation (R-matrix, Casimir, quantum integers)
  Path 2: Kazhdan-Lusztig correspondence with WZW (kappa, central charge)
  Path 3: Verlinde fusion rule comparison (S-matrix, fusion coefficients)
  Path 4: 3-manifold invariant numerical values (D^2, lens spaces)
  Path 5: Generic-q limit (p -> infinity recovery of classical data)
  Path 6: Resonance rank prediction from shadow framework (R-matrix truncation)

Target: 100+ tests.
"""

from __future__ import annotations

import cmath
import math

import numpy as np
import pytest

from compute.lib.quantum_group_root_of_unity_engine import (
    quantum_integer,
    quantum_factorial,
    quantum_binomial,
    root_of_unity,
    quantum_dimension,
    modular_quantum_dim,
    frobenius_center_generators,
    quantum_casimir_eigenvalue,
    center_dimension_at_root,
    universal_r_matrix_terms,
    truncated_r_matrix_sl2,
    verlinde_fusion_coefficient,
    verlinde_fusion_matrix,
    verlinde_s_matrix,
    verify_verlinde_formula,
    fusion_ring_dimensions,
    resonance_rank_root_of_unity,
    r_matrix_term_count,
    mc_element_arity_bound,
    kl_level,
    kappa_wzw_sl2,
    kappa_quantum_group,
    central_charge_wzw_sl2,
    kl_data,
    rt_normalization,
    rt_normalization_exact,
    gauss_sum,
    rt_s3,
    rt_lens_space,
    rt_poincare_sphere,
    projective_cover_dimension,
    indecomposable_count,
    log_shadow_data,
    sl3_type1_irreps,
    sl3_quantum_dim,
    sl3_resonance_rank,
    sl3_kl_data,
    generic_q_limit_check,
    shadow_data_comparison,
    ribbon_eigenvalues,
    t_matrix,
    verify_modular_relation,
    casimir_spectrum,
    full_verification_suite,
)


# ============================================================
# PATH 1: Direct quantum group computation
# ============================================================

class TestQuantumIntegers:
    """Test quantum integers and combinatorics at roots of unity."""

    def test_quantum_integer_generic(self):
        """[n]_q at generic q is well-defined."""
        q = cmath.exp(0.3j)
        for n in range(1, 8):
            val = quantum_integer(n, q)
            # [n]_q should be nonzero for generic q
            assert abs(val) > 1e-10, f"[{n}]_q vanished at generic q"

    def test_quantum_integer_classical_limit(self):
        """As q -> 1, [n]_q -> n."""
        q = 1.0 + 1e-12j  # near 1
        for n in range(1, 8):
            val = quantum_integer(n, q)
            assert abs(val - n) < 1e-6, f"[{n}]_q = {val}, expected {n}"

    @pytest.mark.parametrize("p", [3, 4, 5, 7, 11])
    def test_quantum_integer_vanishes_at_p(self, p):
        """[p]_q = 0 at q = exp(2*pi*i/p)."""
        q = root_of_unity(p)
        val = quantum_integer(p, q)
        assert abs(val) < 1e-10, f"[{p}]_q = {val}, expected 0"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_quantum_integer_nonzero_below_p_odd(self, p):
        """[n]_q != 0 for 1 <= n < p when p is ODD.

        For odd p, [n]_q = 0 iff p | n, so [n] != 0 for 1 <= n < p.
        For even p (e.g. p=4), [n]_q = 0 when p | 2n, so [2]_q = 0
        at p=4 because q^4 = 1 implies q^2 = -1.
        """
        q = root_of_unity(p)
        for n in range(1, p):
            val = quantum_integer(n, q)
            assert abs(val) > 1e-10, f"[{n}]_q vanished at p={p}"

    def test_quantum_integer_vanishing_even_root(self):
        """At p=4 (even), [2]_q = 0 because q^4=1 implies q^{2*2}=1."""
        q = root_of_unity(4)
        val = quantum_integer(2, q)
        assert abs(val) < 1e-10, f"[2]_q = {val} at p=4, expected 0"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_quantum_integer_periodicity(self, p):
        """[n+p]_q = [n]_q at q^p = 1 (periodicity mod p)."""
        q = root_of_unity(p)
        # Actually [n+p] = -[n] due to q^p = 1 and the sign structure.
        # q^{n+p} = q^n * q^p = q^n * 1 = q^n, so
        # [n+p] = (q^{n+p} - q^{-(n+p)})/(q-q^{-1})
        #        = (q^n - q^{-n})/(q-q^{-1}) = [n].
        # Actually q^{-p} = q^{-p} = (q^p)^{-1} = 1, so q^{-(n+p)} = q^{-n}.
        # Hence [n+p] = [n]. CORRECT.
        for n in range(1, p):
            val_n = quantum_integer(n, q)
            val_np = quantum_integer(n + p, q)
            assert abs(val_n - val_np) < 1e-8, \
                f"Periodicity failed: [{n}] = {val_n}, [{n+p}] = {val_np}"

    @pytest.mark.parametrize("p", [3, 4, 5, 7])
    def test_quantum_factorial_vanishes_at_p(self, p):
        """[p]! = 0 at q^p = 1 (since [p]_q = 0)."""
        q = root_of_unity(p)
        val = quantum_factorial(p, q)
        assert abs(val) < 1e-10, f"[{p}]! = {val}, expected 0"

    def test_quantum_factorial_zero(self):
        """[0]! = 1."""
        q = root_of_unity(5)
        assert abs(quantum_factorial(0, q) - 1.0) < 1e-14

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_quantum_factorial_nonzero_below_p(self, p):
        """[n]! != 0 for 0 <= n < p."""
        q = root_of_unity(p)
        for n in range(p):
            val = quantum_factorial(n, q)
            assert abs(val) > 1e-10, f"[{n}]! vanished at p={p}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_quantum_binomial_pascal(self, p):
        """Quantum Pascal identity: [n choose k] = q^k [n-1 choose k] + q^{-(n-k)} [n-1 choose k-1]."""
        q = root_of_unity(p)
        for n in range(2, p):
            for k in range(1, n):
                lhs = quantum_binomial(n, k, q)
                rhs = (q ** k * quantum_binomial(n - 1, k, q)
                       + q ** (-(n - k)) * quantum_binomial(n - 1, k - 1, q))
                assert abs(lhs - rhs) < 1e-8, \
                    f"Pascal failed at n={n}, k={k}: {lhs} vs {rhs}"

    def test_quantum_binomial_boundary(self):
        """[n choose 0] = [n choose n] = 1."""
        q = root_of_unity(5)
        for n in range(6):
            assert abs(quantum_binomial(n, 0, q) - 1.0) < 1e-12
            assert abs(quantum_binomial(n, n, q) - 1.0) < 1e-12


class TestQuantumCasimir:
    """Test quantum Casimir eigenvalues."""

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_casimir_trivial_rep(self, p):
        """Casimir on V_1 (trivial): c_1 = (q + q^{-1}) / (q - q^{-1})^2."""
        q = root_of_unity(p)
        c1 = quantum_casimir_eigenvalue(1, q)
        expected = (q + 1.0 / q) / (q - 1.0 / q) ** 2
        assert abs(c1 - expected) < 1e-10

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_casimir_spectrum_weyl_symmetry(self, p):
        """Casimir eigenvalues satisfy c_n = c_{p-n} (Weyl symmetry at root of unity).

        At q^p = 1: q^{p-n} = q^{-n}, so
        c_{p-n} = (q^{p-n} + q^{-(p-n)})/(q-q^{-1})^2 = (q^{-n} + q^n)/(q-q^{-1})^2 = c_n.
        Hence eigenvalues are NOT all distinct; they come in pairs (n, p-n).
        """
        spectrum = casimir_spectrum(p)
        eigenvalues = {n: c for n, c in spectrum}
        for n in range(1, p):
            c_n = eigenvalues[n]
            c_pn = eigenvalues[p - n]
            assert abs(c_n - c_pn) < 1e-8, \
                f"Weyl symmetry failed at p={p}: c_{n} = {c_n}, c_{p-n} = {c_pn}"

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_casimir_distinct_modulo_weyl(self, p):
        """Casimir eigenvalues are distinct up to the Weyl reflection n <-> p-n."""
        spectrum = casimir_spectrum(p)
        eigenvalues = {n: c for n, c in spectrum}
        # Only check n <= p//2 for distinctness
        reduced = []
        for n in range(1, p // 2 + 1):
            reduced.append((n, eigenvalues[n]))
        for i in range(len(reduced)):
            for j in range(i + 1, len(reduced)):
                ni, ci = reduced[i]
                nj, cj = reduced[j]
                assert abs(ci - cj) > 1e-8, \
                    f"Casimir collision at p={p}: V_{ni} and V_{nj} (unexpected)"


class TestRMatrix:
    """Test R-matrix at roots of unity."""

    @pytest.mark.parametrize("p", [3, 5, 7, 11])
    def test_r_matrix_truncation_odd(self, p):
        """R-matrix has exactly p terms (n=0,...,p-1) at odd root q^p=1.

        For ODD p: [n]_q = 0 iff p|n, so first vanishing factorial is [p]! = 0.
        The sum runs n = 0, 1, ..., p-1 giving p terms.
        For EVEN p: [p/2]_q = 0, so truncation happens at n = p/2.
        """
        q = root_of_unity(p)
        n_terms = r_matrix_term_count(p, q)
        assert n_terms == p, f"Expected {p} terms, got {n_terms}"

    def test_r_matrix_truncation_even(self):
        """At p=4 (even root), [2]_q = 0 so R-matrix truncates at n=2."""
        q = root_of_unity(4)
        n_terms = r_matrix_term_count(4, q)
        # [2]_q = 0 at q=i, so [2]! = 0, truncation at n=2.
        assert n_terms == 2, f"Expected 2 terms, got {n_terms}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_universal_r_terms_count(self, p):
        """Universal R-matrix term list has p entries."""
        q = root_of_unity(p)
        terms = universal_r_matrix_terms(p, q)
        assert len(terms) == p, f"Expected {p} terms, got {len(terms)}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_universal_r_first_term(self, p):
        """First term (n=0) of the R-matrix is 1."""
        q = root_of_unity(p)
        terms = universal_r_matrix_terms(p, q)
        assert terms[0][0] == 0
        assert abs(terms[0][1] - 1.0) < 1e-12

    @pytest.mark.parametrize("p", [3, 4, 5, 7])
    def test_hecke_relation_root_of_unity(self, p):
        """(check_R - q)(check_R + q^{-1}) = 0 at root of unity."""
        q = root_of_unity(p)
        R = truncated_r_matrix_sl2(p, 2)
        qi = 1.0 / q
        I4 = np.eye(4, dtype=complex)
        product = (R - q * I4) @ (R + qi * I4)
        assert np.linalg.norm(product) < 1e-8, \
            f"Hecke relation failed at p={p}, norm={np.linalg.norm(product)}"

    @pytest.mark.parametrize("p", [3, 4, 5, 7])
    def test_braid_relation_root_of_unity(self, p):
        """R1 R2 R1 = R2 R1 R2 on V_2^{tensor 3} at root of unity."""
        q = root_of_unity(p)
        R = truncated_r_matrix_sl2(p, 2)
        I2 = np.eye(2, dtype=complex)
        R1 = np.kron(R, I2)
        R2 = np.kron(I2, R)
        disc = np.linalg.norm(R1 @ R2 @ R1 - R2 @ R1 @ R2)
        assert disc < 1e-8, f"Braid relation failed at p={p}, disc={disc}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_r_matrix_eigenvalues_fundamental(self, p):
        """Eigenvalues of check_R on V_2 tensor V_2 are q (mult 3) and -q^{-1} (mult 1)."""
        q = root_of_unity(p)
        R = truncated_r_matrix_sl2(p, 2)
        eigvals = list(np.linalg.eigvals(R))

        qi = 1.0 / q
        expected = [q, q, q, -qi]

        # Match eigenvalues as multisets (greedy matching)
        unmatched = list(expected)
        for ev in eigvals:
            matched = False
            for i, ex in enumerate(unmatched):
                if abs(ev - ex) < 1e-6:
                    unmatched.pop(i)
                    matched = True
                    break
            assert matched, \
                f"Eigenvalue {ev} has no match in expected set at p={p}"
        assert len(unmatched) == 0, f"Unmatched expected: {unmatched}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_r_matrix_higher_rep(self, p):
        """R-matrix on V_3 tensor V_3 satisfies braid relation."""
        R = truncated_r_matrix_sl2(p, 3)
        d = 9
        I3 = np.eye(3, dtype=complex)
        R1 = np.kron(R, I3)
        R2 = np.kron(I3, R)
        disc = np.linalg.norm(R1 @ R2 @ R1 - R2 @ R1 @ R2)
        assert disc < 1e-6, f"Braid relation on V_3 failed at p={p}, disc={disc}"


# ============================================================
# PATH 2: Kazhdan-Lusztig correspondence
# ============================================================

class TestKazhdanLusztig:
    """Test Kazhdan-Lusztig correspondence with WZW."""

    @pytest.mark.parametrize("p,expected_k", [(3, 1), (4, 2), (5, 3), (7, 5)])
    def test_kl_level(self, p, expected_k):
        """Level k = p - 2."""
        assert kl_level(p) == expected_k

    @pytest.mark.parametrize("p", [3, 4, 5, 7, 11])
    def test_kappa_kl_match(self, p):
        """kappa(U_q) = kappa(sl_2^(1)_k) = 3p/4 via KL."""
        kappa = kappa_quantum_group(p)
        expected = 3.0 * p / 4.0
        assert abs(kappa - expected) < 1e-12, \
            f"kappa mismatch at p={p}: {kappa} vs {expected}"

    @pytest.mark.parametrize("p", [3, 4, 5, 7])
    def test_kappa_from_wzw_formula(self, p):
        """kappa = dim(g)(k+h^vee)/(2*h^vee) = 3(k+2)/4 for sl_2."""
        k = kl_level(p)
        kappa_wzw = kappa_wzw_sl2(k)
        kappa_qg = kappa_quantum_group(p)
        assert abs(kappa_wzw - kappa_qg) < 1e-12

    @pytest.mark.parametrize("k,expected_c", [
        (1, 1.0), (2, 1.5), (3, 9.0 / 5.0), (5, 15.0 / 7.0)
    ])
    def test_central_charge_wzw(self, k, expected_c):
        """c = 3k/(k+2) for sl_2^(1)_k."""
        c = central_charge_wzw_sl2(k)
        assert abs(c - expected_c) < 1e-12, \
            f"c(k={k}) = {c}, expected {expected_c}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_kappa_not_c_over_2(self, p):
        """AP39: kappa != c/2 in general (they coincide only for Virasoro)."""
        kl = kl_data(p)
        assert kl["kappa_neq_c_over_2"], \
            f"kappa = c/2 at p={p}, but they should differ for affine sl_2"

    @pytest.mark.parametrize("p", [3, 4, 5, 7])
    def test_n_integrable_reps(self, p):
        """Number of integrable reps = p - 1 = k + 1."""
        k = kl_level(p)
        kl = kl_data(p)
        assert kl["n_integrable_reps"] == p - 1 == k + 1

    @pytest.mark.parametrize("p", [3, 5, 7, 11])
    def test_kl_data_self_consistent(self, p):
        """All KL data fields are mutually consistent."""
        kl = kl_data(p)
        assert abs(kl["kappa"] - kl["kappa_check"]) < 1e-12
        assert kl["level_k"] == p - 2
        assert abs(kl["central_charge"] - 3.0 * kl["level_k"] / (kl["level_k"] + 2)) < 1e-12


# ============================================================
# PATH 3: Verlinde fusion rules
# ============================================================

class TestVerlindeRules:
    """Test Verlinde fusion rules at roots of unity."""

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_verlinde_formula_verified(self, p):
        """Verlinde formula: N_{ij}^k = sum_s S_{is} S_{js} S_{ks}^* / S_{1s}."""
        disc = verify_verlinde_formula(p)
        assert disc < 1e-8, f"Verlinde formula discrepancy {disc} at p={p}"

    def test_fusion_fundamental_p5(self):
        """V_2 tensor V_2 = V_1 + V_3 at level 3 (p=5)."""
        assert verlinde_fusion_coefficient(2, 2, 1, 5) == 1
        assert verlinde_fusion_coefficient(2, 2, 3, 5) == 1
        assert verlinde_fusion_coefficient(2, 2, 2, 5) == 0  # parity
        assert verlinde_fusion_coefficient(2, 2, 4, 5) == 0  # truncation check

    def test_fusion_truncation_p3(self):
        """At p=3 (level 1): V_2 tensor V_2 = V_1 only (V_3 truncated)."""
        # At p=3: type-1 reps are V_1, V_2.
        # V_2 tensor V_2: classically = V_1 + V_3, but V_3 doesn't exist at p=3.
        # Verlinde: N_{22}^1 = 1, N_{22}^3 impossible (3 >= p).
        assert verlinde_fusion_coefficient(2, 2, 1, 3) == 1
        # k=3 is out of range for p=3
        assert verlinde_fusion_coefficient(2, 2, 3, 3) == 0

    def test_fusion_symmetry(self):
        """N_{ij}^k is symmetric in i,j."""
        p = 7
        for i in range(1, p):
            for j in range(1, p):
                for k in range(1, p):
                    assert verlinde_fusion_coefficient(i, j, k, p) == \
                           verlinde_fusion_coefficient(j, i, k, p)

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_fusion_identity(self, p):
        """V_1 is the identity: V_1 tensor V_j = V_j."""
        for j in range(1, p):
            for k in range(1, p):
                expected = 1 if k == j else 0
                assert verlinde_fusion_coefficient(1, j, k, p) == expected, \
                    f"Identity failed: N_{{1,{j}}}^{k} = {verlinde_fusion_coefficient(1, j, k, p)}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_fusion_associativity(self, p):
        """Fusion is associative: sum_m N_{ij}^m N_{mk}^l = sum_m N_{jk}^m N_{im}^l."""
        n = p - 1
        for i in range(1, p):
            for j in range(1, p):
                for k in range(1, p):
                    for l_val in range(1, p):
                        lhs = sum(verlinde_fusion_coefficient(i, j, m, p) *
                                  verlinde_fusion_coefficient(m, k, l_val, p)
                                  for m in range(1, p))
                        rhs = sum(verlinde_fusion_coefficient(j, k, m, p) *
                                  verlinde_fusion_coefficient(i, m, l_val, p)
                                  for m in range(1, p))
                        assert lhs == rhs, \
                            f"Associativity failed: ({i},{j},{k},{l_val})"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_s_matrix_unitarity(self, p):
        """S-matrix is unitary: S S^T = I."""
        S = verlinde_s_matrix(p)
        product = S @ S.T
        disc = np.linalg.norm(product - np.eye(p - 1))
        assert disc < 1e-10, f"S-matrix not unitary at p={p}, disc={disc}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_s_matrix_symmetry(self, p):
        """S-matrix is symmetric: S_{ab} = S_{ba}."""
        S = verlinde_s_matrix(p)
        disc = np.linalg.norm(S - S.T)
        assert disc < 1e-14, f"S-matrix not symmetric at p={p}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_s_matrix_positivity_first_row(self, p):
        """S_{1,j} > 0 for all j (quantum dimensions positive)."""
        S = verlinde_s_matrix(p)
        for j in range(p - 1):
            assert S[0, j] > 0, f"S_{{1,{j+1}}} = {S[0, j]} <= 0"

    def test_quantum_dimensions_from_s_matrix(self):
        """dim_q(V_j) from S-matrix: S_{j,1}/S_{1,1} = sin(pi*j/p)/sin(pi/p).

        The S-matrix uses the HALF-quantum parameter: dim_q^{S}(V_j) = sin(pi*j/p)/sin(pi/p).
        The quantum integer [j]_q uses q=exp(2*pi*i/p): [j]_q = sin(2*pi*j/p)/sin(2*pi/p).
        These differ by a factor: sin(pi*j/p)/sin(pi/p) vs sin(2*pi*j/p)/sin(2*pi/p).

        Relation: S_{j,1}/S_{1,1} = [j]_{q^{1/2}} where q^{1/2} = exp(pi*i/p).
        """
        p = 5
        q_half = cmath.exp(1.0j * cmath.pi / p)
        S = verlinde_s_matrix(p)
        for j in range(1, p):
            qdim_from_s = S[j - 1, 0] / S[0, 0]
            qdim_half = quantum_integer(j, q_half)
            assert abs(qdim_from_s - abs(qdim_half)) < 1e-8, \
                f"dim_q mismatch for V_{j}: S gives {qdim_from_s}, [j]_{{q^{{1/2}}}} = {abs(qdim_half)}"


# ============================================================
# PATH 4: 3-manifold invariants
# ============================================================

class TestThreeManifoldInvariants:
    """Test Reshetikhin-Turaev 3-manifold invariants."""

    @pytest.mark.parametrize("p", [3, 5, 7, 11])
    def test_d2_two_computations(self, p):
        """D^2 computed two ways: sum vs closed form p/(2 sin^2(pi/p))."""
        D2_sum = rt_normalization(p)
        D2_exact = rt_normalization_exact(p)
        rel_err = abs(D2_sum - D2_exact) / D2_exact
        assert rel_err < 1e-10, \
            f"D^2 mismatch at p={p}: sum={D2_sum}, exact={D2_exact}, rel_err={rel_err}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_d2_positive(self, p):
        """D^2 > 0."""
        D2 = rt_normalization(p)
        assert D2 > 0, f"D^2 = {D2} at p={p}"

    def test_d2_p3(self):
        """D^2 at p=3 = 3/(2 sin^2(pi/3)) = 3/(2 * 3/4) = 2."""
        D2 = rt_normalization_exact(3)
        assert abs(D2 - 2.0) < 1e-12

    def test_d2_p4(self):
        """D^2 at p=4 = 4/(2 sin^2(pi/4)) = 4/(2 * 1/2) = 4."""
        D2 = rt_normalization_exact(4)
        assert abs(D2 - 4.0) < 1e-12

    def test_rt_s3_normalization(self):
        """RT(S^3) = 1 (normalization convention)."""
        for p in [3, 5, 7]:
            assert abs(rt_s3(p) - 1.0) < 1e-14

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_rt_lens_space_l1_1_is_s3(self, p):
        """L(1,1) = S^3, so RT(L(1,1)) should be the Kirby normalization."""
        # L(1,1) = +1 surgery on unknot.
        # RT(L(1,1)) = (1/D^2) sum_j [j]^2 theta_j
        # This should be tau_+ / D^2 where tau_+ is the positive Gauss sum.
        val = rt_lens_space(p, 1, 1)
        tau_plus = gauss_sum(p, +1)
        D2 = rt_normalization(p)
        expected = tau_plus / D2
        assert abs(val - expected) < 1e-8, \
            f"L(1,1) mismatch at p={p}: got {val}, expected {expected}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_rt_lens_space_absolute_value(self, p):
        """RT invariants of lens spaces have bounded absolute value."""
        for n in range(1, 6):
            val = rt_lens_space(p, n, 1)
            assert abs(val) < 100, f"|RT(L({n},1))| = {abs(val)} too large at p={p}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_gauss_sum_modulus(self, p):
        """|tau_+|^2 = D^2."""
        tau_p = gauss_sum(p, +1)
        D2 = rt_normalization(p)
        assert abs(abs(tau_p) ** 2 - D2) < 1e-6, \
            f"|tau_+|^2 = {abs(tau_p)**2}, D^2 = {D2} at p={p}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_gauss_sum_conjugation(self, p):
        """tau_- = conjugate(tau_+)."""
        tau_p = gauss_sum(p, +1)
        tau_m = gauss_sum(p, -1)
        assert abs(tau_m - tau_p.conjugate()) < 1e-8, \
            f"tau_- != conj(tau_+) at p={p}"


class TestRibbonAndModular:
    """Test ribbon structure and modular category relations."""

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_ribbon_trivial_rep(self, p):
        """Twist on V_1 is 1 (trivial)."""
        thetas = ribbon_eigenvalues(p)
        # theta_1 = q^{(1-1)/4} = q^0 = 1
        assert abs(thetas[0] - 1.0) < 1e-12

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_ribbon_eigenvalues_count(self, p):
        """p-1 ribbon eigenvalues."""
        thetas = ribbon_eigenvalues(p)
        assert len(thetas) == p - 1

    @pytest.mark.parametrize("p", [5, 7])
    def test_s2_is_charge_conjugation(self, p):
        """S^2 = C (charge conjugation matrix)."""
        mod = verify_modular_relation(p)
        assert mod["S2_equals_C_discrepancy"] < 1e-8, \
            f"S^2 != C at p={p}, disc={mod['S2_equals_C_discrepancy']}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_s4_is_identity(self, p):
        """S^4 = I."""
        mod = verify_modular_relation(p)
        assert mod["S4_equals_I_discrepancy"] < 1e-8, \
            f"S^4 != I at p={p}, disc={mod['S4_equals_I_discrepancy']}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_st3_proportional_s2(self, p):
        """(ST)^3 proportional to S^2."""
        mod = verify_modular_relation(p)
        assert mod["ST3_proportional_to_S2_discrepancy"] < 1e-6, \
            f"(ST)^3 not proportional to S^2 at p={p}"


# ============================================================
# PATH 5: Generic-q limit
# ============================================================

class TestGenericQLimit:
    """Test that root-of-unity data recovers generic quantum group as p -> infinity."""

    def test_quantum_dim_convergence(self):
        """|[2]_q| -> 2 as p -> infinity."""
        for p in [50, 100, 500]:
            q = root_of_unity(p)
            qdim = quantum_dimension(2, q)
            # [2]_q = q + q^{-1} = 2 cos(2*pi/p) -> 2 as p -> infinity
            expected = 2.0 * math.cos(2.0 * math.pi / p)
            assert abs(qdim - expected) < 1e-10

    def test_r_matrix_terms_grow(self):
        """Number of R-matrix terms = p (grows with p)."""
        for p in [5, 11, 17, 29]:
            q = root_of_unity(p)
            n = r_matrix_term_count(p, q)
            assert n == p

    def test_fusion_approaches_classical(self):
        """Verlinde fusion V_2 x V_2 = V_1 + V_3 holds for p >= 4."""
        for p in [4, 5, 7, 11, 29]:
            assert verlinde_fusion_coefficient(2, 2, 1, p) == 1
            assert verlinde_fusion_coefficient(2, 2, 3, p) == 1

    def test_kappa_grows_linearly(self):
        """kappa = 3p/4 grows linearly with p."""
        for p in [5, 11, 23, 101]:
            kappa = kappa_quantum_group(p)
            assert abs(kappa - 3.0 * p / 4.0) < 1e-12

    def test_central_charge_approaches_3(self):
        """c = 3k/(k+2) -> 3 as k -> infinity. Error = 6/(k+2)."""
        for k in [10, 50, 200]:
            c = central_charge_wzw_sl2(k)
            expected_error = 6.0 / (k + 2.0)
            assert abs(c - 3.0) < expected_error + 1e-10, \
                f"c(k={k}) = {c}, |c-3| = {abs(c-3)}, bound = {expected_error}"

    def test_generic_limit_data(self):
        """Comprehensive generic-q limit check."""
        results = generic_q_limit_check([5, 11, 29, 101])
        for r in results:
            assert r["n_r_matrix_terms"] == r["p"]
            # Quantum dim of V_2 approaches 2
            expected_qdm = 2.0 * math.cos(2 * math.pi / r["p"])
            assert abs(r["quantum_dim_V2"] - expected_qdm) < 1e-8


# ============================================================
# PATH 6: Resonance rank from shadow framework
# ============================================================

class TestResonance:
    """Test resonance rank predictions from the shadow framework."""

    @pytest.mark.parametrize("p", [3, 4, 5, 7, 11])
    def test_resonance_rank_equals_p_minus_1(self, p):
        """Resonance rank = p - 1 (R-matrix truncation order)."""
        rho = resonance_rank_root_of_unity(p)
        assert rho == p - 1

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_resonance_matches_r_matrix_odd(self, p):
        """Resonance rank = (number of R-matrix terms) - 1 for odd p."""
        q = root_of_unity(p)
        n_terms = r_matrix_term_count(p, q)
        rho = resonance_rank_root_of_unity(p)
        assert rho == n_terms - 1

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_mc_arity_bound(self, p):
        """MC element arity bound = p - 1 at roots of unity."""
        data = mc_element_arity_bound(p)
        assert data["mc_arity_bound"] == p - 1
        assert data["resonance_rank"] == p - 1
        assert data["level"] == p - 2

    def test_mc4_automatic_finite(self):
        """MC4 completion is automatic at roots of unity (finite truncation)."""
        for p in [3, 5, 7]:
            data = mc_element_arity_bound(p)
            assert "automatic" in data["mc4_status"]


# ============================================================
# Cross-path comparisons
# ============================================================

class TestCrossPathVerification:
    """Cross-path verification: multiple independent computations agree."""

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_shadow_data_all_paths(self, p):
        """All verification paths agree at each odd root of unity.

        Note: R-matrix truncation at n_terms = p holds only for ODD p.
        For even p, truncation happens earlier at p/2.
        """
        data = shadow_data_comparison(p)
        assert data["kappa_match"], f"kappa mismatch at p={p}"
        # R-matrix truncation: p terms for odd p
        assert data["r_matrix_truncation_match"], f"R-matrix truncation mismatch at p={p}"
        assert data["verlinde_verified"], f"Verlinde not verified at p={p}"
        assert data["D2_match"], f"D^2 mismatch at p={p}"
        assert data["resonance_match"], f"Resonance rank mismatch at p={p}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_full_verification_suite(self, p):
        """Full verification suite passes."""
        results = full_verification_suite(p)
        assert results["verlinde_discrepancy"] < 1e-8
        assert results["D2_relative_error"] < 1e-8
        assert results["resonance_matches_truncation"]
        assert results["hecke_discrepancy"] < 1e-8
        assert results["braid_discrepancy"] < 1e-8

    @pytest.mark.parametrize("p", [5, 7])
    def test_kappa_three_paths(self, p):
        """kappa verified via 3 independent paths:
        Path 1: direct formula 3p/4
        Path 2: KL correspondence dim(g)(k+h^vee)/(2h^vee)
        Path 3: central charge relation (distinct from kappa)
        """
        kappa_1 = 3.0 * p / 4.0
        kappa_2 = kappa_wzw_sl2(kl_level(p))
        kappa_3 = kappa_quantum_group(p)

        assert abs(kappa_1 - kappa_2) < 1e-12
        assert abs(kappa_2 - kappa_3) < 1e-12

        # AP39: kappa != c/2
        c = central_charge_wzw_sl2(kl_level(p))
        assert abs(kappa_1 - c / 2.0) > 0.01, \
            "kappa should NOT equal c/2 for affine sl_2"


# ============================================================
# Center and type-2 representations
# ============================================================

class TestCenterAndReps:
    """Test the enlarged center and representation theory."""

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_frobenius_center_has_four_generators(self, p):
        """Frobenius center has generators E^p, F^p, K^p, K^{-p}."""
        gen = frobenius_center_generators(p)
        assert gen["Frobenius_E"] == f"E^{p}"
        assert gen["Frobenius_F"] == f"F^{p}"
        assert gen["Frobenius_K_plus"] == f"K^{p}"

    @pytest.mark.parametrize("p", [3, 5, 7, 11])
    def test_type1_irreps_count(self, p):
        """p - 1 type-1 irreducible representations."""
        data = center_dimension_at_root(p)
        assert data["n_type1_irreps"] == p - 1
        assert data["type1_dims"] == list(range(1, p))

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_type2_dimension(self, p):
        """Type-2 irreps are p-dimensional."""
        data = center_dimension_at_root(p)
        assert data["type2_dim"] == p


# ============================================================
# Logarithmic (non-semisimple) extensions
# ============================================================

class TestLogarithmic:
    """Test logarithmic/non-semisimple structure at roots of unity."""

    @pytest.mark.parametrize("p", [5, 7])
    def test_projective_cover_generic(self, p):
        """dim P(n) = 2p for 1 < n < p-1."""
        for n in range(2, p - 1):
            dim_P = projective_cover_dimension(n, p)
            assert dim_P == 2 * p, f"dim P({n}) = {dim_P}, expected {2*p}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_projective_cover_boundary(self, p):
        """dim P(1) = dim P(p-1) = p."""
        assert projective_cover_dimension(1, p) == p
        assert projective_cover_dimension(p - 1, p) == p

    @pytest.mark.parametrize("p", [5, 7])
    def test_projective_cover_out_of_range(self, p):
        """dim P(n) = 0 for n >= p or n < 1."""
        assert projective_cover_dimension(0, p) == 0
        assert projective_cover_dimension(p, p) == 0

    @pytest.mark.parametrize("p", [5, 7])
    def test_indecomposable_counts(self, p):
        """Indecomposable module counts are consistent."""
        data = indecomposable_count(p)
        assert data["n_simple"] == p - 1
        assert data["n_projective"] == p - 1
        assert data["n_projective_simple"] == 2
        assert data["n_non_simple_projective"] == p - 3

    @pytest.mark.parametrize("p", [5, 7])
    def test_log_shadow_depth(self, p):
        """Shadow depth in the log category matches resonance rank."""
        data = log_shadow_data(p)
        assert data["shadow_depth"] == p - 1
        assert data["shadow_depth"] == resonance_rank_root_of_unity(p)

    @pytest.mark.parametrize("p", [5, 7])
    def test_log_grothendieck_relations(self, p):
        """Grothendieck ring: [P(n)] = [V(n)] + [V(p-n)]."""
        data = log_shadow_data(p)
        for n in range(2, p - 1):
            key = f"P({n})"
            assert key in data["grothendieck_relations"]
            expected = f"V({n}) + V({p - n})"
            assert data["grothendieck_relations"][key] == expected

    def test_log_irregular_singularity(self):
        """Non-semisimple category has irregular singularity for p > 3."""
        for p in [5, 7, 11]:
            data = log_shadow_data(p)
            assert data["irregular_singularity"] is True
        data_3 = log_shadow_data(3)
        assert data_3["irregular_singularity"] is False  # p=3 is too small


# ============================================================
# Higher rank: sl_3
# ============================================================

class TestSl3:
    """Test U_q(sl_3) at roots of unity."""

    def test_sl3_type1_irreps_p5(self):
        """sl_3 at q^5 = 1: type-1 irreps labeled by (a,b) with a+b <= 2."""
        # Level k = p - 3 = 2, so a + b <= k = 2.
        reps = sl3_type1_irreps(5)
        labels = [(a, b) for a, b, _ in reps]
        expected = [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0)]
        assert set(labels) == set(expected), f"Got {labels}, expected {expected}"

    def test_sl3_dimensions_p5(self):
        """Dimensions of sl_3 type-1 irreps at p=5."""
        reps = sl3_type1_irreps(5)
        dims = {(a, b): d for a, b, d in reps}
        assert dims[(0, 0)] == 1   # trivial
        assert dims[(1, 0)] == 3   # fundamental
        assert dims[(0, 1)] == 3   # anti-fundamental
        assert dims[(2, 0)] == 6   # symmetric square
        assert dims[(1, 1)] == 8   # adjoint
        assert dims[(0, 2)] == 6

    def test_sl3_quantum_dim_trivial(self):
        """dim_q(V(0,0)) = 1 for sl_3."""
        q = root_of_unity(5)
        qdim = sl3_quantum_dim(0, 0, q)
        assert abs(qdim - 1.0) < 1e-10

    @pytest.mark.parametrize("p", [5, 7])
    def test_sl3_quantum_dim_fundamental(self, p):
        """dim_q(V(1,0)) = [3]_q for sl_3 fundamental."""
        q = root_of_unity(p)
        qdim = sl3_quantum_dim(1, 0, q)
        expected = quantum_integer(3, q)
        # Actually dim_q(fund) = [3]_q for sl_3... let me verify.
        # dim_q = [2][1][3] / ([1][1][2]) = [3] for (a,b) = (1,0).
        assert abs(qdim - expected) < 1e-8, \
            f"dim_q(fund) = {qdim}, expected [3] = {expected}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_sl3_resonance_rank(self, p):
        """Resonance rank for sl_3 = p - 1."""
        assert sl3_resonance_rank(p) == p - 1

    def test_sl3_kl_data_p5(self):
        """KL data for sl_3 at p=5: level k=2, kappa=20/3."""
        data = sl3_kl_data(5)
        assert data["level_k"] == 2
        assert abs(data["kappa"] - 20.0 / 3.0) < 1e-12
        assert data["h_vee"] == 3
        assert data["dim_g"] == 8

    @pytest.mark.parametrize("p", [5, 7])
    def test_sl3_kappa_formula(self, p):
        """kappa(sl_3^(1)_k) = 8(k+3)/6 = 4(k+3)/3 = 4p/3."""
        data = sl3_kl_data(p)
        assert abs(data["kappa"] - 4.0 * p / 3.0) < 1e-12

    def test_sl3_central_charge(self):
        """c(sl_3^(1)_k) = 8k/(k+3)."""
        for p in [5, 7]:
            data = sl3_kl_data(p)
            k = data["level_k"]
            expected_c = 8.0 * k / (k + 3.0)
            assert abs(data["central_charge"] - expected_c) < 1e-12


# ============================================================
# Specific known values
# ============================================================

class TestKnownValues:
    """Test against specific known values from the literature."""

    def test_p3_level1_data(self):
        """p=3, level 1: Ising model data."""
        # sl_2^(1) at level 1: c = 1 (free boson compactification)
        c = central_charge_wzw_sl2(1)
        assert abs(c - 1.0) < 1e-12

        # kappa = 3*3/4 = 9/4
        kappa = kappa_quantum_group(3)
        assert abs(kappa - 9.0 / 4.0) < 1e-12

        # 2 type-1 irreps (dims 1, 2)
        data = center_dimension_at_root(3)
        assert data["n_type1_irreps"] == 2

    def test_p5_level3_s_matrix(self):
        """p=5, level 3: S-matrix entries."""
        S = verlinde_s_matrix(5)
        prefactor = math.sqrt(2.0 / 5.0)

        # S_{11} = sqrt(2/5) sin(pi/5)
        assert abs(S[0, 0] - prefactor * math.sin(math.pi / 5)) < 1e-12

        # S_{12} = sqrt(2/5) sin(2*pi/5)
        assert abs(S[0, 1] - prefactor * math.sin(2 * math.pi / 5)) < 1e-12

    def test_p5_level3_fusion_counts(self):
        """At level 3 (p=5), verify specific fusion products."""
        # V_2 x V_2 = V_1 + V_3
        assert verlinde_fusion_coefficient(2, 2, 1, 5) == 1
        assert verlinde_fusion_coefficient(2, 2, 3, 5) == 1

        # V_2 x V_3 = V_2 + V_4
        assert verlinde_fusion_coefficient(2, 3, 2, 5) == 1
        assert verlinde_fusion_coefficient(2, 3, 4, 5) == 1

        # V_3 x V_3 = V_1 + V_3 (truncated from classical V_1+V_3+V_5)
        assert verlinde_fusion_coefficient(3, 3, 1, 5) == 1
        assert verlinde_fusion_coefficient(3, 3, 3, 5) == 1
        assert verlinde_fusion_coefficient(3, 3, 5, 5) == 0  # truncated!

        # V_4 x V_4: classically V_1+V_3+V_5+V_7.
        # Truncation: V_5, V_7 forbidden (>= p). V_3: 4+4+3=11 > 2p-1=9, FORBIDDEN.
        # Only V_1 survives: N_{44}^1 = 1.
        assert verlinde_fusion_coefficient(4, 4, 1, 5) == 1
        assert verlinde_fusion_coefficient(4, 4, 3, 5) == 0  # killed by Verlinde truncation

    def test_d2_known_values(self):
        """D^2 at small p: known exact values."""
        # p=3: D^2 = 2
        assert abs(rt_normalization_exact(3) - 2.0) < 1e-12
        # p=4: D^2 = 4
        assert abs(rt_normalization_exact(4) - 4.0) < 1e-12
        # p=5: D^2 = 5/(2 sin^2(pi/5)) = 5/(2 * (5-sqrt(5))/8) = 20/(5-sqrt(5))
        val = 5.0 / (2.0 * math.sin(math.pi / 5.0) ** 2)
        assert abs(rt_normalization_exact(5) - val) < 1e-12

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_quantum_dim_steinberg(self, p):
        """Quantum dimension of the Steinberg rep V_{p-1} at q^p = 1.

        In the q-integer convention: [p-1]_q = -1 (since q^{p-1} = q^{-1}).
        In the modular convention: d_{p-1} = sin(pi*(p-1)/p)/sin(pi/p) = 1.
        The Steinberg rep has modular dimension 1.
        """
        # q-integer: [p-1] = -1
        q = root_of_unity(p)
        qdim = quantum_dimension(p - 1, q)
        assert abs(qdim - (-1.0)) < 1e-8, f"[{p-1}]_q = {qdim}, expected -1"

        # Modular: d_{p-1} = sin(pi*(p-1)/p)/sin(pi/p) = sin(pi/p)/sin(pi/p) = 1
        d_steinberg = modular_quantum_dim(p - 1, p)
        assert abs(d_steinberg - 1.0) < 1e-10, \
            f"d_{{p-1}} = {d_steinberg}, expected 1"


# ============================================================
# Poincare sphere (complicated computation)
# ============================================================

class TestPoincareSphere:
    """Test RT invariant of the Poincare homology sphere."""

    @pytest.mark.parametrize("p", [5, 7])
    def test_rt_poincare_finite(self, p):
        """RT(Poincare sphere) is finite at roots of unity."""
        val = rt_poincare_sphere(p)
        assert np.isfinite(abs(val)), f"RT(Poincare) not finite at p={p}"
        assert abs(val) < 1000, f"|RT(Poincare)| = {abs(val)} too large at p={p}"

    def test_rt_poincare_p5_nonzero(self):
        """RT(Poincare sphere) at p=5 is nonzero."""
        val = rt_poincare_sphere(5)
        # The Poincare sphere is a non-trivial 3-manifold; RT should detect it.
        # At p=5 (level 3), there are 4 type-1 reps, and the RT invariant
        # is a nontrivial sum.
        # We don't hardcode the exact value (to avoid AP38 convention issues),
        # but verify it's nonzero and finite.
        assert abs(val) > 1e-10, f"RT(Poincare) = {val} at p=5, expected nonzero"


# ============================================================
# Additional cross-checks
# ============================================================

class TestAdditionalCrossChecks:
    """Additional consistency checks across different computations."""

    @pytest.mark.parametrize("p", [5, 7])
    def test_fusion_dimensions_match(self, p):
        """Fusion with V_2: d_i * d_2 = sum_k N_{i,2}^k * d_k.

        Uses modular quantum dimensions d_n = sin(pi*n/p)/sin(pi/p).
        """
        for i in range(1, p):
            d_i = modular_quantum_dim(i, p)
            d_2 = modular_quantum_dim(2, p)
            product_qdim = d_i * d_2

            sum_fusion = sum(
                verlinde_fusion_coefficient(i, 2, k, p) * modular_quantum_dim(k, p)
                for k in range(1, p)
            )

            assert abs(product_qdim - sum_fusion) < 1e-6, \
                f"Fusion dimension mismatch for V_{i} x V_2 at p={p}: " \
                f"product={product_qdim}, sum={sum_fusion}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_total_quantum_dimension_from_s(self, p):
        """D^2 = 1/S_{11}^2 from S-matrix.

        S_{11} = sqrt(2/p) sin(pi/p), so 1/S_{11}^2 = p/(2 sin^2(pi/p)) = D^2.
        """
        S = verlinde_s_matrix(p)
        D2_from_s = 1.0 / S[0, 0] ** 2
        D2_direct = rt_normalization(p)
        assert abs(D2_from_s - D2_direct) < 1e-6, \
            f"D^2 mismatch: S-matrix gives {D2_from_s}, direct gives {D2_direct}"

    def test_r_matrix_determinant_fundamental(self):
        """det(check_R) = q^{eigenvalue_sum} on V_2 tensor V_2."""
        for p in [5, 7]:
            R = truncated_r_matrix_sl2(p, 2)
            det_R = np.linalg.det(R)
            # Eigenvalues: q (mult 3), -q^{-1} (mult 1)
            # det = q^3 * (-q^{-1}) = -q^2
            q = root_of_unity(p)
            expected_det = -q ** 2
            assert abs(det_R - expected_det) < 1e-8, \
                f"det(R) = {det_R}, expected {expected_det} at p={p}"

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_verlinde_s_rows_orthonormal(self, p):
        """S-matrix rows are orthonormal (real orthogonal)."""
        S = verlinde_s_matrix(p)
        n = p - 1
        for i in range(n):
            for j in range(n):
                dot = np.dot(S[i], S[j])
                expected = 1.0 if i == j else 0.0
                assert abs(dot - expected) < 1e-10, \
                    f"S row orthogonality failed: ({i},{j}) dot = {dot}"

    @pytest.mark.parametrize("p", [5, 7])
    def test_casimir_sum_rule(self, p):
        """Sum rule: sum_j d_j^2 = D^2 (total quantum dimension squared).

        Uses modular quantum dimensions d_j = sin(pi*j/p)/sin(pi/p).
        """
        sum_qdim2 = sum(modular_quantum_dim(j, p) ** 2 for j in range(1, p))
        D2 = rt_normalization(p)
        assert abs(sum_qdim2 - D2) < 1e-8, \
            f"Sum d_j^2 = {sum_qdim2}, D^2 = {D2}"

    def test_resonance_rank_monotone(self):
        """Resonance rank increases with p."""
        prev = 0
        for p in [3, 4, 5, 7, 11, 13]:
            rho = resonance_rank_root_of_unity(p)
            assert rho > prev, f"Resonance rank not monotone at p={p}"
            prev = rho

    @pytest.mark.parametrize("p", [5, 7])
    def test_kl_c_bounded_by_3(self, p):
        """Central charge c = 3k/(k+2) < 3 for all finite levels."""
        c = central_charge_wzw_sl2(kl_level(p))
        assert c < 3.0, f"c = {c} >= 3 at p={p}"
        assert c > 0, f"c = {c} <= 0 at p={p}"
