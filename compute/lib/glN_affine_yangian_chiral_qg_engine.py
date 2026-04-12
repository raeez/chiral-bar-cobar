r"""Chiral quantum group structure on Y(gl_N-hat) for N >= 2.

MATHEMATICAL FRAMEWORK
======================

The affine Yangian Y(gl_N-hat) is the quantisation of gl_N[t] with
generators t_{ij}^{(r)} (1 <= i,j <= N, r >= 0) assembled into an
N x N transfer matrix

    T(u) = I_N + sum_{r >= 1} T^{(r)} u^{-r},

where (T^{(r)})_{ij} = t_{ij}^{(r)}.

R-MATRIX (Yang's rational R-matrix for gl_N):
    R(u) = u(u + Psi)^{-1} P + Psi(u + Psi)^{-1} I
         = (u P + Psi I) / (u + Psi)
         = I + Psi(P - I)/u + O(1/u^2)

where P is the permutation on C^N tensor C^N and Psi is the level.

Equivalently in the additive convention (no denominator):
    R^{add}(u) = u I + Psi P

The classical r-matrix (first order in Psi):
    r(z) = Psi P / z       (trace-form, AP126: Psi=0 -> r=0)

This is Yang's rational R-matrix with level prefix Psi (AP126 mandatory).
At N=1: R(u) = 1 (scalar), r(z) = Psi/z, recovering the W_{1+inf} case.

RTT RELATION (non-trivial for N >= 2):
    R_{12}(u - v) T_1(u) T_2(v) = T_2(v) T_1(u) R_{12}(u - v)

where T_1(u) = T(u) tensor I_N, T_2(v) = I_N tensor T(v), and
R_{12}(u-v) acts on C^N tensor C^N.

For N=1 the RTT is trivially satisfied (scalar R-matrix).
For N >= 2 the RTT is the defining relation of Y(gl_N).

DRINFELD COPRODUCT:
    Delta_z(T(u)) = T(u) . T(u - z)    (matrix multiplication in aux space)

Component form:
    Delta_z(t_{ij}(u)) = sum_k t_{ik}(u) tensor t_{kj}(u - z)

where t_{ij}(u) = delta_{ij} + sum_{r >= 1} t_{ij}^{(r)} u^{-r}.

TRUNCATION: W_N = W_{1+inf} / I_N has generators of spins 1, 2, ..., N
and is the chiral algebra associated to Y(gl_N-hat).

YANG-BAXTER EQUATION:
    R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)

This is verified numerically for the Yang R-matrix at each N.

OPE COMPATIBILITY (Theorem): The Drinfeld coproduct satisfies OPE
compatibility at all spins by two arguments:
  (A) Coderivation on Koszul-locus bar complex (generic Psi).
  (B) JKL vertex bialgebra theorem on the CoHA of the Jordan quiver
      at rank N (JKL26 Theorem C for general quivers).

QUANTUM DETERMINANT:
    qdet T(u) = sum_{sigma in S_N} sgn(sigma) prod_{i=1}^{N}
                T_{i,sigma(i)}(u - (i-1) Psi)
This is central in Y(gl_N).

Conventions
-----------
* R^{add}(u) = u I + Psi P  (additive Yang R-matrix with level Psi).
* R^{mult}(u) = I + Psi P/u  (multiplicative, for RTT with T(u) = I + ...).
* T(u) = I + T^{(1)} u^{-1} + T^{(2)} u^{-2} + ...
* AP126: level prefix Psi mandatory; Psi=0 -> r(z)=0.
* Cohomological grading (|d| = +1).

References
----------
* Molev, "Yangians and Classical Lie Algebras", AMS 2007.
* Chari-Pressley, "A Guide to Quantum Groups", Cambridge 1994.
* Maulik-Okounkov, arXiv:1211.1287 (stable envelopes).
* Schiffmann-Vasserot, arXiv:1202.2756 (SV isomorphism).
* Prochazka-Rapcak, arXiv:1711.11582 (W_{1+inf} and gl_N).
* Jindal-Kaubrys-Latyntsev, arXiv:2603.21707 (vertex bialgebra).
* Yang-Zhao, arXiv:1401.3979 (CoHA and Yangian).
"""

from __future__ import annotations

from itertools import permutations
from math import factorial
from typing import Dict, List, Optional, Tuple

import numpy as np


# ============================================================
# 1. Fundamental operators
# ============================================================

def permutation_operator(N: int) -> np.ndarray:
    """Permutation operator P on C^N tensor C^N.

    P(e_i tensor e_j) = e_j tensor e_i.
    P^2 = I.  Tr P = N.
    """
    dim = N * N
    P = np.zeros((dim, dim), dtype=complex)
    for i in range(N):
        for j in range(N):
            P[i * N + j, j * N + i] = 1.0
    return P


def identity_tensor(N: int) -> np.ndarray:
    """Identity on C^N tensor C^N."""
    return np.eye(N * N, dtype=complex)


# ============================================================
# 2. Yang R-matrix with level prefix Psi (AP126)
# ============================================================

def yang_r_matrix_additive(N: int, Psi: complex, u: complex) -> np.ndarray:
    r"""Additive Yang R-matrix for gl_N.

    R^{add}(u) = u I_{N^2} + Psi P

    where P is the permutation and Psi is the level parameter.

    AP126 check: at Psi=0, R^{add}(u) = u I (trivial, no interaction).
    The classical r-matrix is r(z) = Psi P / z (level prefix Psi).

    Args:
        N: rank (fundamental dimension).
        Psi: level parameter.
        u: spectral parameter.

    Returns:
        N^2 x N^2 complex matrix.
    """
    I = identity_tensor(N)
    P = permutation_operator(N)
    return u * I + Psi * P


def yang_r_matrix_multiplicative(N: int, Psi: complex, u: complex) -> np.ndarray:
    r"""Multiplicative Yang R-matrix for gl_N.

    R^{mult}(u) = I + Psi P / u

    Used in the RTT relation with T(u) = I + sum T^{(r)} u^{-r}.

    AP126 check: at Psi=0, R^{mult}(u) = I (no braiding).
    """
    I = identity_tensor(N)
    P = permutation_operator(N)
    return I + (Psi / u) * P


def classical_r_matrix(N: int, Psi: complex, z: complex) -> np.ndarray:
    r"""Classical r-matrix for gl_N at level Psi.

    r(z) = Psi P / z

    AP126: level prefix Psi mandatory; Psi=0 -> r=0.
    """
    P = permutation_operator(N)
    return (Psi / z) * P


# ============================================================
# 3. Yang-Baxter equation verification
# ============================================================

def _embed_12(R: np.ndarray, N: int) -> np.ndarray:
    """Embed N^2 x N^2 matrix R_{12} into N^3 x N^3 as R_{12} tensor I_N."""
    return np.kron(R, np.eye(N, dtype=complex))


def _embed_23(R: np.ndarray, N: int) -> np.ndarray:
    """Embed N^2 x N^2 matrix R_{23} into N^3 x N^3 as I_N tensor R_{23}."""
    return np.kron(np.eye(N, dtype=complex), R)


def _embed_13(R: np.ndarray, N: int) -> np.ndarray:
    """Embed R_{13} into N^3 x N^3.

    (R_{13})_{(ijk),(lmn)} = R_{(ik),(ln)} * delta_{jm}.
    """
    dim3 = N ** 3
    result = np.zeros((dim3, dim3), dtype=complex)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                row = i * N * N + j * N + k
                for l in range(N):
                    for nn in range(N):
                        col = l * N * N + j * N + nn
                        result[row, col] += R[i * N + k, l * N + nn]
    return result


def verify_yang_baxter(N: int, Psi: complex, u: complex, v: complex,
                       tol: float = 1e-8) -> Dict:
    """Verify the Yang-Baxter equation for the additive Yang R-matrix.

    R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)

    Args:
        N: fundamental dimension.
        Psi: level parameter.
        u, v: spectral parameters.
        tol: numerical tolerance.

    Returns:
        Dictionary with verification results.
    """
    R12 = _embed_12(yang_r_matrix_additive(N, Psi, u - v), N)
    R13 = _embed_13(yang_r_matrix_additive(N, Psi, u), N)
    R23 = _embed_23(yang_r_matrix_additive(N, Psi, v), N)

    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12

    diff = float(np.max(np.abs(lhs - rhs)))
    return {
        'N': N,
        'Psi': Psi,
        'u': u,
        'v': v,
        'max_diff': diff,
        'passes': diff < tol,
    }


# ============================================================
# 4. RTT relation verification
# ============================================================

def _T_matrix_eval(N: int, Psi: complex, u: complex, a: complex) -> np.ndarray:
    """Evaluation representation T_a(u) for Y(gl_N).

    T_a(u) = (u - a) I_N + Psi sum_{i,j} E_{ij} tensor E_{ji}
    divided by (u - a + Psi), as an N x N matrix.

    In the standard convention:
        T_a(u)_{ij} = (u - a) delta_{ij} / (u - a + Psi)
                    + Psi E_{ji}(a) / (u - a + Psi)

    where the evaluation map sends t_{ij}^{(1)} -> Psi * E_{ji}.

    For simplicity, the evaluation T-matrix in the fundamental rep is:
        T_a(u) = R^{mult}(u - a)  restricted to the first tensor factor.

    Actually, the evaluation L-operator is:
        L_a(u) = I + Psi * sum E_{ij} tensor E_{ji} / (u - a)
               = I + Psi * P / (u - a)  (acting on C^N tensor C^N)

    which means T(u) in the fundamental auxiliary space is
        T_a(u)_{ij} = delta_{ij} + Psi * delta_{ij...wait}

    Let's be precise. The RTT T-matrix in auxiliary space C^N:
        T_a(u) = I_N + Psi/(u - a) * E   (N x N matrix over the algebra)

    where E_{ij} acts as the matrix unit on C^N_quantum.

    For a NUMERICAL evaluation in the fundamental of the quantum space:
        L_{a}(u) = I_{N^2} + Psi * P / (u - a)

    This is the L-operator: an N^2 x N^2 matrix that satisfies RTT.
    """
    return yang_r_matrix_multiplicative(N, Psi, u - a)


def verify_rtt_relation(N: int, Psi: complex, u: complex, v: complex,
                        a: complex = 1.0, tol: float = 1e-8) -> Dict:
    """Verify the RTT relation for the evaluation L-operator.

    R_{12}(u - v) L_1(u) L_2(v) = L_2(v) L_1(u) R_{12}(u - v)

    where L(u) = I + Psi P / (u - a) is the evaluation L-operator.

    For N=1: trivially satisfied (everything commutes).
    For N>=2: non-trivial matrix identity.

    The verification uses the L-operator as an N^2 x N^2 matrix
    in both spaces, with embedding into N^4 = (N^2)^2.
    """
    # R_{12}(u-v) in C^N tensor C^N
    R12 = yang_r_matrix_additive(N, Psi, u - v)

    # L-operators as N^2 x N^2 matrices
    L_u = yang_r_matrix_multiplicative(N, Psi, u - a)
    L_v = yang_r_matrix_multiplicative(N, Psi, v - a)

    # For the RTT in the evaluation representation, the YBE gives:
    # R_{12}(u-v) R_{13}(u-a) R_{23}(v-a) = R_{23}(v-a) R_{13}(u-a) R_{12}(u-v)
    #
    # In additive convention:
    # R_{12}(u-v) R_{13}(u-a) R_{23}(v-a) = R_{23}(v-a) R_{13}(u-a) R_{12}(u-v)
    #
    # This IS the YBE.  The RTT is a CONSEQUENCE of the YBE
    # (evaluate one space in the fundamental).
    #
    # More directly: T_1(u) T_2(v) in the evaluation rep means
    # L_{a,12}(u) L_{a,23}(v) in a triple space, but the RTT relation
    # in the standard form uses two auxiliary spaces and one quantum space.
    #
    # For a clean numerical test: the RTT relation in the additive convention
    # with L_a(u) = R(u-a) is EQUIVALENT to the YBE.
    # Let's verify the RTT directly using the multiplicative convention.

    # Multiplicative convention:
    # R^{mult}(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R^{mult}(u-v)
    # where T_1(u) = T(u) tensor I, T_2(v) = I tensor T(v).

    # In N^2 x N^2 = (C^N_aux1 tensor C^N_aux2) tensor (C^N_aux1 tensor C^N_aux2):
    # We work in C^N tensor C^N tensor C^N where:
    #   space 1 = auxiliary 1, space 2 = auxiliary 2, space 3 = quantum (fundamental eval)

    # R_{12}(u-v): acts on aux1 tensor aux2
    R12_triple = _embed_12(yang_r_matrix_additive(N, Psi, u - v), N)

    # T_1(u): the L-operator for auxiliary space 1 and quantum space 3
    # L_{13}(u-a) = R_{13}^{add}(u-a)
    L13_u = _embed_13(yang_r_matrix_additive(N, Psi, u - a), N)

    # T_2(v): the L-operator for auxiliary space 2 and quantum space 3
    # L_{23}(v-a) = R_{23}^{add}(v-a)
    L23_v = _embed_23(yang_r_matrix_additive(N, Psi, v - a), N)

    # RTT: R_{12}(u-v) L_{13}(u-a) L_{23}(v-a) = L_{23}(v-a) L_{13}(u-a) R_{12}(u-v)
    # This is exactly the YBE! So the RTT for the evaluation L-operator IS the YBE.
    lhs = R12_triple @ L13_u @ L23_v
    rhs = L23_v @ L13_u @ R12_triple

    diff = float(np.max(np.abs(lhs - rhs)))

    # Also verify that for N=1 the relation is trivially satisfied
    trivial_at_N1 = (N == 1)

    return {
        'N': N,
        'Psi': Psi,
        'u': u,
        'v': v,
        'a': a,
        'max_diff': diff,
        'passes': diff < tol,
        'trivial_at_N1': trivial_at_N1,
    }


def verify_rtt_nontrivial_at_N_ge_2(N: int, Psi: complex = 1.0,
                                      u: complex = 3.7, v: complex = 1.3,
                                      tol: float = 1e-8) -> Dict:
    """Verify that the RTT relation is NON-TRIVIAL for N >= 2.

    For N=1: R(u) is scalar, so LHS and RHS are trivially equal.
    For N >= 2: R(u) is a non-scalar matrix, so the RTT imposes
    genuine quadratic relations on the generators.

    We check non-triviality by verifying that [R_{12}, L_{13}] != 0
    (i.e., the R-matrix does NOT commute with the L-operator in general).
    """
    R12 = _embed_12(yang_r_matrix_additive(N, Psi, u - v), N)
    L13 = _embed_13(yang_r_matrix_additive(N, Psi, u), N)

    commutator = R12 @ L13 - L13 @ R12
    comm_norm = float(np.max(np.abs(commutator)))

    # For N=1: commutator should be 0 (scalar R)
    # For N>=2: commutator should be nonzero
    is_nontrivial = comm_norm > tol

    return {
        'N': N,
        'Psi': Psi,
        'commutator_norm': comm_norm,
        'is_nontrivial': is_nontrivial,
        'expected_nontrivial': N >= 2,
        'consistent': is_nontrivial == (N >= 2),
    }


# ============================================================
# 5. Drinfeld coproduct
# ============================================================

def drinfeld_coproduct_transfer(N: int, u: complex, z: complex,
                                 T_coeffs_left: List[np.ndarray],
                                 T_coeffs_right: List[np.ndarray],
                                 max_order: int = 4) -> np.ndarray:
    """Compute Delta_z(T(u)) = T(u) . T(u-z) as N x N matrix over A tensor A.

    T(u) = I_N + sum_{r>=1} T^{(r)} u^{-r}
    T(u-z) = I_N + sum_{r>=1} T^{(r)} (u-z)^{-r}

    The result is an N x N matrix whose (i,j) entry is
        sum_k T_{ik}(u) tensor T_{kj}(u-z).

    For evaluation: T_coeffs_left and T_coeffs_right are the T^{(r)} matrices.
    max_order controls the truncation in u^{-1}.

    Returns the product as an N x N matrix of complex numbers (for numerical eval).
    """
    # Build T(u) = I + sum T^{(r)} u^{-r}
    T_u = np.eye(N, dtype=complex)
    for r in range(1, min(len(T_coeffs_left), max_order + 1)):
        T_u = T_u + T_coeffs_left[r] * u**(-r)

    # Build T(u-z) = I + sum T^{(r)} (u-z)^{-r}
    T_uz = np.eye(N, dtype=complex)
    for r in range(1, min(len(T_coeffs_right), max_order + 1)):
        T_uz = T_uz + T_coeffs_right[r] * (u - z)**(-r)

    # Matrix multiplication: Delta_z(T(u)) = T(u) . T(u-z)
    return T_u @ T_uz


def drinfeld_coproduct_component(N: int, n: int, z: complex) -> Dict:
    """The Drinfeld coproduct Delta_z(T^{(n)}) for the gl_N Yangian.

    From Delta_z(T(u)) = T(u) . T(u-z), expanding in u^{-n}:

        Delta_z(T^{(n)})_{ij} = sum_k sum_{a+b=n, b>=0}
            binom(b + ...) * T^{(a)}_{ik} tensor T^{(b)}_{kj} * (polynomial in z)

    For n=0: Delta_z(I) = I tensor I.
    For n=1: Delta_z(T^{(1)}) = T^{(1)} tensor I + I tensor T^{(1)}
             + z (I tensor T^{(1)}) ... wait, need careful expansion.

    Actually the expansion of T(u) . T(u-z):
    [u^{-n}] T(u) T(u-z) = sum_{a=0}^{n} T^{(a)} . [u^{-a} * (u-z)^{-(n-a)}]
    with expansion (u-z)^{-m} = u^{-m} sum_{j>=0} binom(m+j-1,j) (z/u)^j.

    So [u^{-n}] T(u) T(u-z)
    = sum_{a+b=n, a,b>=0} sum_{j>=0} binom(b+j-1,j) z^j
      T^{(a)} . T^{(b)} u^{-(a+b+j)}

    Wait, we want the total coefficient of u^{-n}, so a + b + j = n,
    i.e., j = n - a - b >= 0.

    Delta_z(T^{(n)})_{ij} = sum_{a,b>=0, a+b<=n}
        binom(b + (n-a-b) - 1, n-a-b) z^{n-a-b}
        sum_k T^{(a)}_{ik} tensor T^{(b)}_{kj}

    Let c = n - a - b >= 0, so the coefficient is binom(b+c-1, c) z^c.

    For a Numerical evaluation, we just compute T(u) . T(u-z) directly.

    Returns description dict (symbolic form for documentation).
    """
    result = {
        'N': N,
        'n': n,
        'description': f'Delta_z(T^{{({n})}}) for gl_{N}',
        'formula': 'sum_{a+b+c=n} binom(b+c-1,c) z^c T^(a) . T^(b)',
    }
    return result


# ============================================================
# 6. Quantum determinant
# ============================================================

def quantum_determinant_eval(N: int, Psi: complex, u: complex,
                              a: complex = 0.0) -> complex:
    """Quantum determinant qdet T(u) in the evaluation representation.

    qdet T(u) = sum_{sigma in S_N} sgn(sigma)
                prod_{i=1}^{N} T_{i,sigma(i)}(u - (i-1)*Psi)

    The L-operator in the evaluation representation at point a is:

        L_a(u) = I_{N^2} + Psi P / (u-a)

    as an N^2 x N^2 matrix on C^N_aux tensor C^N_quant.

    Block extraction: T_{ij}(u) is the N x N block acting on C^N_quant:

        T_{ij}(u)_{ab} = L_{(ia),(jb)} = delta_{ij} delta_{ab}
                         + (Psi/(u-a)) delta_{ib} delta_{ja}

    The quantum determinant is the antisymmetrised ordered product of these
    blocks with Psi-shifted spectral parameters. It is CENTRAL in Y(gl_N),
    meaning it evaluates to a scalar (proportional to I_N on C^N_quant).
    """
    # Build T(u - s*Psi)_{ij} as N x N matrices on C^N_quant, for s = 0,...,N-1
    T_shifted = []
    for s in range(N):
        u_s = u - s * Psi
        coeff = Psi / (u_s - a)
        # T_s[i,j] is an N x N matrix on C^N_quant
        # T_{ij}(u_s)_{ab} = delta_{ij} delta_{ab} + coeff * delta_{ib} delta_{ja}
        T_s = np.zeros((N, N, N, N), dtype=complex)
        for i in range(N):
            for j in range(N):
                # delta_{ij} * delta_{ab}: add I_N to diagonal blocks only
                if i == j:
                    for aa in range(N):
                        T_s[i, j, aa, aa] += 1.0
                # coeff * delta_{ib} delta_{ja}: matrix with 1 at (a,b) = (j,i)
                T_s[i, j, j, i] += coeff
        T_shifted.append(T_s)

    # qdet = sum_sigma sgn(sigma) prod_{i} T_{i,sigma(i)}(u - (i-1)*Psi)
    qdet = np.zeros((N, N), dtype=complex)  # operator on C^N
    for perm in permutations(range(N)):
        sgn = _perm_sign(list(perm))
        # Ordered product T_{1,sigma(1)}(u) . T_{2,sigma(2)}(u-Psi) . ...
        product = np.eye(N, dtype=complex)
        for i in range(N):
            product = product @ T_shifted[i][i, perm[i]]
        qdet += sgn * product

    return qdet


def _perm_sign(perm: List[int]) -> int:
    """Sign of a permutation given as a list."""
    n = len(perm)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        j = i
        cycle_len = 0
        while not visited[j]:
            visited[j] = True
            j = perm[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign *= -1
    return sign


def verify_qdet_scalar(N: int, Psi: complex, u: complex,
                        a: complex = 0.0, tol: float = 1e-8) -> Dict:
    """Verify that qdet T(u) is a scalar (proportional to identity).

    In the evaluation representation, qdet should be a scalar operator
    (proportional to I_N), since it is central in Y(gl_N).
    """
    qdet = quantum_determinant_eval(N, Psi, u, a)
    # Check if qdet is proportional to identity
    trace = np.trace(qdet)
    expected_scalar = trace / N
    deviation = np.max(np.abs(qdet - expected_scalar * np.eye(N, dtype=complex)))
    return {
        'N': N,
        'Psi': Psi,
        'u': u,
        'qdet_trace': trace,
        'scalar_value': expected_scalar,
        'deviation_from_scalar': float(deviation),
        'is_scalar': float(deviation) < tol,
    }


# ============================================================
# 7. R-matrix properties specific to gl_N
# ============================================================

def verify_r_matrix_properties(N: int, Psi: complex, u: complex,
                                tol: float = 1e-8) -> Dict:
    """Verify algebraic properties of the Yang R-matrix.

    Properties:
    (1) P^2 = I (permutation involution).
    (2) R(u) R(-u) = (Psi^2 - u^2) I  (unitarity, additive convention).
    (3) R(0) = Psi P (symmetry at u=0).
    (4) Psi=0 gives R(u) = u I (trivial, AP126).
    (5) Classical limit: R(u) = u I + Psi P + O(Psi^2) gives r(z) = Psi P / z.
    """
    I = identity_tensor(N)
    P = permutation_operator(N)

    R_u = yang_r_matrix_additive(N, Psi, u)
    R_minus_u = yang_r_matrix_additive(N, Psi, -u)

    # (1) P^2 = I
    p_squared = np.allclose(P @ P, I)

    # (2) Unitarity: R(u) R(-u) = (Psi^2 - u^2) I
    #     Proof: (uI + Psi P)(-uI + Psi P) = -u^2 I + Psi^2 P^2 = (Psi^2 - u^2) I.
    product = R_u @ R_minus_u
    expected = (Psi**2 - u**2) * I
    unitarity = float(np.max(np.abs(product - expected)))

    # (3) R(0) = Psi P
    R_0 = yang_r_matrix_additive(N, Psi, 0.0)
    at_zero = float(np.max(np.abs(R_0 - Psi * P)))

    # (4) AP126: Psi=0 -> R = u I
    R_trivial = yang_r_matrix_additive(N, 0.0, u)
    ap126 = float(np.max(np.abs(R_trivial - u * I)))

    # (5) Classical r-matrix: r = Psi P / z
    r = classical_r_matrix(N, Psi, 1.0)
    r_expected = Psi * P
    classical = float(np.max(np.abs(r - r_expected)))

    # (6) AP126 classical: Psi=0 -> r=0
    r_trivial = classical_r_matrix(N, 0.0, 1.0)
    ap126_classical = float(np.max(np.abs(r_trivial)))

    return {
        'N': N,
        'Psi': Psi,
        'P_squared_is_I': p_squared,
        'unitarity_deviation': unitarity,
        'unitarity_passes': unitarity < tol,
        'R_at_zero_deviation': at_zero,
        'R_at_zero_passes': at_zero < tol,
        'AP126_R_deviation': ap126,
        'AP126_R_passes': ap126 < tol,
        'classical_r_deviation': classical,
        'classical_r_passes': classical < tol,
        'AP126_classical_deviation': ap126_classical,
        'AP126_classical_passes': ap126_classical < tol,
    }


# ============================================================
# 8. N=1 reduction to W_{1+infinity}
# ============================================================

def verify_N1_reduction(Psi: complex = 1.0, tol: float = 1e-8) -> Dict:
    """Verify that at N=1, the R-matrix is scalar and RTT is trivial.

    For N=1:
      - R(u) = u + Psi (scalar).
      - P = 1 (permutation on C^1 tensor C^1 = C).
      - RTT is trivially satisfied.
      - Classical r-matrix: r(z) = Psi/z (scalar).
    """
    N = 1
    u = 3.0 + 1.0j

    R = yang_r_matrix_additive(N, Psi, u)
    # Should be a 1x1 matrix = [[u + Psi]]
    expected = np.array([[u + Psi]], dtype=complex)
    r_scalar = float(np.max(np.abs(R - expected)))

    # Classical r-matrix at z=1: Psi/1 = Psi
    r = classical_r_matrix(N, Psi, 1.0)
    r_expected = np.array([[Psi]], dtype=complex)
    r_classical = float(np.max(np.abs(r - r_expected)))

    # AP126: Psi=0 -> r=0
    r0 = classical_r_matrix(N, 0.0, 1.0)
    ap126 = float(np.max(np.abs(r0)))

    return {
        'N': N,
        'R_is_scalar': r_scalar < tol,
        'R_value': complex(R[0, 0]),
        'R_expected': u + Psi,
        'r_classical_ok': r_classical < tol,
        'AP126_passes': ap126 < tol,
    }


# ============================================================
# 9. Full verification suite
# ============================================================

def full_verification(N: int, Psi: complex = 1.0,
                      u: complex = 3.7 + 0.3j,
                      v: complex = 1.3 + 0.7j,
                      tol: float = 1e-8) -> Dict:
    """Run the complete verification suite for gl_N at level Psi.

    Checks:
    1. R-matrix properties (unitarity, P^2=I, AP126).
    2. Yang-Baxter equation.
    3. RTT relation (evaluation rep).
    4. RTT non-triviality for N >= 2.
    5. Quantum determinant scalarity.
    """
    results = {
        'N': N,
        'Psi': Psi,
    }

    # R-matrix properties
    r_props = verify_r_matrix_properties(N, Psi, u, tol)
    results['r_matrix'] = r_props

    # YBE
    ybe = verify_yang_baxter(N, Psi, u, v, tol)
    results['ybe'] = ybe

    # RTT
    rtt = verify_rtt_relation(N, Psi, u, v, tol=tol)
    results['rtt'] = rtt

    # RTT non-triviality
    rtt_nt = verify_rtt_nontrivial_at_N_ge_2(N, Psi, u=u.real, v=v.real, tol=tol)
    results['rtt_nontrivial'] = rtt_nt

    # Quantum determinant
    qdet = verify_qdet_scalar(N, Psi, u, tol=tol)
    results['qdet'] = qdet

    # Summary
    all_pass = (
        r_props['unitarity_passes']
        and r_props['AP126_R_passes']
        and r_props['AP126_classical_passes']
        and ybe['passes']
        and rtt['passes']
        and rtt_nt['consistent']
        and qdet['is_scalar']
    )
    results['all_pass'] = all_pass

    return results
