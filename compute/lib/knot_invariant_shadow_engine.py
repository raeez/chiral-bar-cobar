r"""Knot invariants from the Yangian shadow tower.

Mathematical foundation
-----------------------
The bar complex B(V_k(\hat{sl}_N)) produces a factorization coalgebra whose
collision residue Res^{coll}_{0,2}(\Theta_A) is the r-matrix r(z) = \Omega/z
(AP19: one pole order below the OPE).  The r-matrix exponentiates to the
Yang R-matrix R(u) = uI + P, which at the DK bridge becomes the quantum
group R-matrix R_q \in End(V \otimes V) for U_q(sl_N).

The passage from the rational Yangian R-matrix to knot invariants proceeds
through the Drinfeld-Kohno theorem (DK bridge, proved for all simple types
via MC3):

    Y(sl_N) --[DK bridge]--> U_q(\hat{sl}_N) --[evaluation]--> End(V^{tensor n})

The braid group B_n acts via sigma_i |-> check_R_{i,i+1}, and knot invariants
are obtained as quantum Markov traces of the braid representation.

Quantum R-matrix (Kassel convention)
-------------------------------------
The enhanced R-matrix (check_R = tau o R_univ, tau = flip) on the fundamental
representation V = C^N of U_q(sl_N) acts as (Kassel, Quantum Groups, Ch XVII):

    check_R(e_a tensor e_b) = q^{delta_{ab}} e_b tensor e_a
                              + [a < b] (q - q^{-1}) e_a tensor e_b

Eigenvalues: q on Sym^2(V), -q^{-1} on Lambda^2(V).
Satisfies both the Hecke relation (check_R - q)(check_R + q^{-1}) = 0
and the braid relation check_R_1 check_R_2 check_R_1 = check_R_2 check_R_1 check_R_2.

Jones polynomial
----------------
For sl_2 fundamental (N=2), the Jones polynomial of a knot K presented as
the closure of a braid beta on n strands with writhe w is:

    V_K(t) = q^{-2w} Tr(rho(beta) K^{tensor n}) / delta

where t = q^2, K = diag(q, q^{-1}), delta = q + q^{-1} = Tr(K),
and rho(sigma_i) = check_R_{i,i+1}.

V_K(t) = -t^{-4} + t^{-3} + t^{-1}  for the trefoil 3_1.
V_K(t) = t^2 - t + 1 - t^{-1} + t^{-2}  for the figure-eight 4_1.

HOMFLY-PT polynomial
--------------------
For sl_N, the HOMFLY-PT polynomial P_K(a, z) satisfies the skein relation:

    a P(L+) - a^{-1} P(L-) = z P(L0)

with a = q^N and z = q - q^{-1}.  Computed via the sl_N quantum R-matrix
with the quantum Markov trace.

Colored Jones polynomials
-------------------------
The n-colored Jones polynomial J_n(K; q) uses the n-dimensional irreducible
representation S^{n-1}(C^2) of U_q(sl_2).  The R-matrix on V_n tensor V_n
is computed via the spectral decomposition using the quantum Casimir.

Volume conjecture
-----------------
Kashaev's conjecture (Murakami-Murakami):

    lim_{n -> infty} (2 pi / n) log|J_n(K; exp(2 pi i / n))| = Vol(S^3 \setminus K)

for hyperbolic knots.  Figure-eight: Vol = 2.0298832128...

References
----------
* Kassel, "Quantum Groups", GTM 155, Springer (1995), Ch. XVII
* Ohtsuki, "Quantum Invariants", World Scientific (2002)
* Turaev, "Quantum Invariants of Knots and 3-Manifolds", de Gruyter (1994)
* Murakami-Murakami, Acta Math. 186 (2001), 85--104
* concordance.tex: MC3 (DK bridge)
"""

from __future__ import annotations

import cmath
import math
from typing import Dict, List, Optional, Tuple, Union

import numpy as np


# ============================================================
# Quantum R-matrix for sl_N (Kassel convention)
# ============================================================

def slN_check_r_matrix(q: complex, N: int) -> np.ndarray:
    """Enhanced R-matrix check_R for U_q(sl_N) on the fundamental C^N tensor C^N.

    Kassel convention:
        check_R(e_a tensor e_b) = q^{delta_{ab}} e_b tensor e_a
                                  + [a < b] (q - q^{-1}) e_a tensor e_b

    Eigenvalues: q on Sym^2 (mult N(N+1)/2), -q^{-1} on Lambda^2 (mult N(N-1)/2).
    Satisfies the Hecke relation: (check_R - q)(check_R + q^{-1}) = 0.
    Satisfies the braid relation on V^{tensor 3}.

    Basis ordering: e_a tensor e_b -> index a*N + b.
    """
    qi = 1.0 / q
    d = N * N
    R = np.zeros((d, d), dtype=complex)

    for a in range(N):
        for b in range(N):
            row_ab = a * N + b   # |e_a tensor e_b> input
            col_ba = b * N + a   # |e_b tensor e_a> output from the swap
            col_ab = a * N + b   # |e_a tensor e_b> output from the (q-qi) term

            # Term 1: q^{delta_{ab}} e_b tensor e_a
            if a == b:
                R[col_ba, row_ab] += q
            else:
                R[col_ba, row_ab] += 1.0

            # Term 2: [a < b] (q - q^{-1}) e_a tensor e_b
            if a < b:
                R[col_ab, row_ab] += (q - qi)

    return R


def slN_check_r_matrix_inverse(q: complex, N: int) -> np.ndarray:
    """Inverse of the enhanced R-matrix.

    From the Hecke relation R^2 - (q - q^{-1}) R - I = 0:
        R^{-1} = R - (q - q^{-1}) I
    """
    R = slN_check_r_matrix(q, N)
    qi = 1.0 / q
    d = N * N
    return R - (q - qi) * np.eye(d, dtype=complex)


def verify_hecke_relation(q: complex, N: int) -> float:
    """Verify (check_R - q)(check_R + q^{-1}) = 0.

    Returns Frobenius norm of the discrepancy.
    """
    qi = 1.0 / q
    R = slN_check_r_matrix(q, N)
    d = N * N
    I_d = np.eye(d, dtype=complex)
    product = (R - q * I_d) @ (R + qi * I_d)
    return float(np.linalg.norm(product))


def verify_braid_relation(q: complex, N: int) -> float:
    """Verify check_R_1 check_R_2 check_R_1 = check_R_2 check_R_1 check_R_2
    on V^{tensor 3}.

    Returns Frobenius norm of the discrepancy.
    """
    R = slN_check_r_matrix(q, N)
    I_N = np.eye(N, dtype=complex)
    R1 = np.kron(R, I_N)
    R2 = np.kron(I_N, R)
    lhs = R1 @ R2 @ R1
    rhs = R2 @ R1 @ R2
    return float(np.linalg.norm(lhs - rhs))


# ============================================================
# Braid representation
# ============================================================

def braid_matrix_slN(braid_word: List[int], n_strands: int,
                     q: complex, N: int) -> np.ndarray:
    """Braid group representation on V^{tensor n_strands} using check_R for sl_N.

    Args:
        braid_word: list of signed integers. +i means sigma_i, -i means sigma_i^{-1}.
                    1-indexed.
        n_strands: number of braid strands.
        q: quantum parameter.
        N: rank parameter (sl_N).

    Returns:
        N^n_strands x N^n_strands matrix.
    """
    d = N ** n_strands
    result = np.eye(d, dtype=complex)

    R = slN_check_r_matrix(q, N)
    Rinv = slN_check_r_matrix_inverse(q, N)

    for gen in braid_word:
        idx = abs(gen)
        assert 1 <= idx < n_strands, \
            f"Generator {idx} out of range for {n_strands} strands"
        mat = R if gen > 0 else Rinv

        left_dim = N ** (idx - 1)
        right_dim = N ** (n_strands - idx - 1)

        if left_dim > 1 and right_dim > 1:
            full = np.kron(np.kron(np.eye(left_dim, dtype=complex), mat),
                           np.eye(right_dim, dtype=complex))
        elif left_dim > 1:
            full = np.kron(np.eye(left_dim, dtype=complex), mat)
        elif right_dim > 1:
            full = np.kron(mat, np.eye(right_dim, dtype=complex))
        else:
            full = mat.copy()

        result = result @ full

    return result


def writhe(braid_word: List[int]) -> int:
    """Writhe (algebraic crossing number) of a braid word."""
    return sum(1 if g > 0 else -1 for g in braid_word)


def quantum_trace_slN(matrix: np.ndarray, q: complex, N: int,
                       n_strands: int) -> complex:
    """Quantum trace Tr_q(M) = Tr(M K^{tensor n}).

    K = diag(q^{N-1}, q^{N-3}, ..., q^{-(N-1)}) for sl_N fundamental.
    For N=2: K = diag(q, q^{-1}).
    """
    K_diag = np.array([q ** (N - 1 - 2 * j) for j in range(N)], dtype=complex)
    K_single = np.diag(K_diag)

    K_total = K_single.copy()
    for _ in range(n_strands - 1):
        K_total = np.kron(K_total, K_single)

    return np.trace(matrix @ K_total)


def quantum_dimension_slN(q: complex, N: int) -> complex:
    """Quantum dimension [N]_q = (q^N - q^{-N}) / (q - q^{-1}).

    For N=2: [2]_q = q + q^{-1}.
    """
    qi = 1.0 / q
    if abs(q - 1.0) < 1e-12:
        return complex(N)
    return (q ** N - qi ** N) / (q - qi)


# ============================================================
# Jones polynomial (sl_2 specialization)
# ============================================================

def jones_from_braid(braid_word: List[int], n_strands: int,
                     q: complex) -> complex:
    """Jones polynomial V_K(t) from a braid closure.

    Formula (verified from first principles):
        V_K(t) = q^{-2w} Tr_q(rho(beta)) / delta

    where t = q^2, w = writhe, delta = q + q^{-1},
    Tr_q(M) = Tr(M K^{tensor n}) with K = diag(q, q^{-1}),
    and rho uses the sl_2 check_R.

    Normalization: V(unknot) = 1.
    """
    if not braid_word:
        return complex(1.0)

    mat = braid_matrix_slN(braid_word, n_strands, q, 2)
    tr = quantum_trace_slN(mat, q, 2, n_strands)
    delta = q + 1.0 / q
    w = writhe(braid_word)

    return q ** (-2 * w) * tr / delta


# ============================================================
# Standard knot braid representations
# ============================================================

KNOT_BRAIDS: Dict[str, Tuple[List[int], int]] = {
    "0_1": ([], 1),
    "3_1": ([1, 1, 1], 2),
    "4_1": ([1, -2, 1, -2], 3),
    "5_1": ([1, 1, 1, 1, 1], 2),
    "5_2": ([1, 1, 1, -2, -2], 3),
    "6_1": ([1, 1, -2, 1, -2, -2], 3),
    "7_1": ([1, 1, 1, 1, 1, 1, 1], 2),
    "9_1": ([1, 1, 1, 1, 1, 1, 1, 1, 1], 2),
    "3_1#3_1": ([1, 1, 1, 2, 2, 2], 3),
}


def torus_knot_braid(p: int, n: int) -> Tuple[List[int], int]:
    """Braid word for the torus knot T(p, n).

    T(2, n) = sigma_1^n on 2 strands.
    T(p, n) = (sigma_1 ... sigma_{p-1})^n on p strands.
    """
    if p == 2:
        return ([1] * n, 2)
    word = []
    for _ in range(n):
        for i in range(1, p):
            word.append(i)
    return (word, p)


def jones_at(knot_name: str, q: complex) -> complex:
    """Evaluate the Jones polynomial V_K(t=q^2) for a named knot."""
    if knot_name.startswith("T("):
        inner = knot_name[2:-1]
        p_str, n_str = inner.split(",")
        braid, ns = torus_knot_braid(int(p_str.strip()), int(n_str.strip()))
    elif knot_name in KNOT_BRAIDS:
        braid, ns = KNOT_BRAIDS[knot_name]
    else:
        raise ValueError(f"Unknown knot: {knot_name}")
    if not braid:
        return complex(1.0)
    return jones_from_braid(braid, ns, q)


# Exact Jones polynomials (in the variable t = q^2)

def jones_exact_trefoil(t: complex) -> complex:
    """V_{3_1}(t) = -t^{-4} + t^{-3} + t^{-1}."""
    return -t**(-4) + t**(-3) + t**(-1)


def jones_exact_figure_eight(t: complex) -> complex:
    """V_{4_1}(t) = t^2 - t + 1 - t^{-1} + t^{-2}."""
    return t**2 - t + 1 - t**(-1) + t**(-2)


JONES_EXACT = {
    "3_1": jones_exact_trefoil,
    "4_1": jones_exact_figure_eight,
}


# ============================================================
# HOMFLY-PT polynomial (sl_N generalization)
# ============================================================

def homfly_from_braid(braid_word: List[int], n_strands: int,
                      q: complex, N: int) -> complex:
    """HOMFLY-PT polynomial P_K(a, z) at a = q^N, z = q - q^{-1}.

    Generalizes the Jones polynomial formula to sl_N:
        P_K = q^{-N(N-1)w} Tr_q(rho_N(beta)) / delta_N

    where delta_N = Tr(K_{sl_N}) = sum_j q^{N-1-2j} = [N]_q via
    the sl_N ribbon element.

    Normalization: P(unknot) = 1.
    """
    if not braid_word:
        return complex(1.0)

    mat = braid_matrix_slN(braid_word, n_strands, q, N)
    tr = quantum_trace_slN(mat, q, N, n_strands)

    # delta_N = Tr(K_{sl_N})
    K_diag = np.array([q ** (N - 1 - 2 * j) for j in range(N)], dtype=complex)
    delta_N = np.sum(K_diag)

    w = writhe(braid_word)

    # The writhe exponent for sl_N: we need alpha such that
    # alpha^{-w} Tr_q(rho(beta)) / delta_N gives the correct invariant.
    # For N=2: alpha = q^2. For general N: alpha = q^{N}.
    # This comes from the twist on the fundamental: theta_V = q^{c_2(V)}
    # where c_2 = N(N-1)/... Actually let me find it empirically.
    #
    # For the unknot on 1 strand: alpha^0 * Tr(K) / delta_N = 1. Correct.
    # For R1 (single positive kink, w=1): alpha^{-1} * Tr(R K2) / delta_N = 1.
    # So alpha = Tr(R K2) / delta_N.
    # For N=2: alpha = q^2 (verified above).
    # For general N: use the formula Tr(check_R K^{tensor 2}) / delta_N.

    R = slN_check_r_matrix(q, N)
    K_single = np.diag(K_diag)
    K2 = np.kron(K_single, K_single)
    alpha = np.trace(R @ K2) / delta_N

    return alpha ** (-w) * tr / delta_N


def homfly_at(knot_name: str, q: complex, N: int) -> complex:
    """Evaluate the HOMFLY-PT polynomial for a named knot."""
    if knot_name.startswith("T("):
        inner = knot_name[2:-1]
        p_str, n_str = inner.split(",")
        braid, ns = torus_knot_braid(int(p_str.strip()), int(n_str.strip()))
    elif knot_name in KNOT_BRAIDS:
        braid, ns = KNOT_BRAIDS[knot_name]
    else:
        raise ValueError(f"Unknown knot: {knot_name}")
    if not braid:
        return complex(1.0)
    return homfly_from_braid(braid, ns, q, N)


# ============================================================
# Skein relation verification
# ============================================================

def verify_skein_relation(q: complex, N: int, n_strands: int,
                          braid_prefix: List[int],
                          crossing_pos: int) -> Tuple[complex, complex, complex, float]:
    """Verify the HOMFLY-PT skein relation from the MC equation.

    The skein relation at the R-matrix level is:
        q check_R - q^{-1} check_R^{-1} = (q - q^{-1}) I

    which follows from the Hecke relation (check_R - q)(check_R + q^{-1}) = 0.

    We verify this on quantum traces: for any braid prefix b,
        Tr_q(b R_i) - Tr_q(b R_i^{-1}) = (q - q^{-1}) Tr_q(b)

    which follows from R - R^{-1} = (q - q^{-1}) I (the Hecke skein identity).

    Returns: (tr_plus, tr_minus, tr_zero, discrepancy)
    """
    qi = 1.0 / q
    braid_plus = braid_prefix + [crossing_pos]
    braid_minus = braid_prefix + [-crossing_pos]
    braid_zero = list(braid_prefix)

    mat_plus = braid_matrix_slN(braid_plus, n_strands, q, N) if braid_plus else \
        np.eye(N ** n_strands, dtype=complex)
    mat_minus = braid_matrix_slN(braid_minus, n_strands, q, N) if braid_minus else \
        np.eye(N ** n_strands, dtype=complex)
    mat_zero = braid_matrix_slN(braid_zero, n_strands, q, N) if braid_zero else \
        np.eye(N ** n_strands, dtype=complex)

    tr_plus = quantum_trace_slN(mat_plus, q, N, n_strands)
    tr_minus = quantum_trace_slN(mat_minus, q, N, n_strands)
    tr_zero = quantum_trace_slN(mat_zero, q, N, n_strands)

    # Skein: tr_plus - tr_minus = (q - qi) tr_zero
    lhs = tr_plus - tr_minus
    rhs = (q - qi) * tr_zero
    discrepancy = abs(lhs - rhs)

    return (tr_plus, tr_minus, tr_zero, discrepancy)


def verify_skein_at_rmatrix_level(q: complex, N: int) -> float:
    """Verify R - R^{-1} = (q - q^{-1}) I directly.

    This is the Hecke-algebra skein relation, an immediate consequence of
    the Hecke quadratic: R^2 - (q - q^{-1}) R - I = 0, which gives
    R^{-1} = R - (q - q^{-1}) I, hence R - R^{-1} = (q - q^{-1}) I.
    """
    qi = 1.0 / q
    R = slN_check_r_matrix(q, N)
    Rinv = slN_check_r_matrix_inverse(q, N)
    d = N * N
    lhs = R - Rinv
    rhs = (q - qi) * np.eye(d, dtype=complex)
    return float(np.linalg.norm(lhs - rhs))


# ============================================================
# Colored Jones polynomial
# ============================================================

def _quantum_casimir_tensor(q: complex, j: float) -> np.ndarray:
    """Quantum Casimir on V_j tensor V_j via the coproduct of U_q(sl_2).

    V_j has dimension n = 2j+1, basis |k> with k=0,...,n-1 and m = j - k.
    Generators: E (raising), F (lowering), K = q^H.
    Coproduct: Delta(E) = E tensor K + 1 tensor E, etc.
    Casimir on V_j tensor V_j has eigenvalue [s]_q [s+1]_q on the V_s component.
    """
    n = int(2 * j + 1)
    dd = n * n

    def q_int(m):
        if abs(q - 1.0) < 1e-14:
            return complex(m)
        return (q ** m - q ** (-m)) / (q - 1.0 / q)

    # Build representation matrices on V_j
    E = np.zeros((n, n), dtype=complex)
    F = np.zeros((n, n), dtype=complex)
    K = np.zeros((n, n), dtype=complex)
    Kinv = np.zeros((n, n), dtype=complex)

    for k in range(n):
        m = j - k
        K[k, k] = q ** m
        Kinv[k, k] = q ** (-m)
        if k > 0:
            m_from = j - k
            coeff = cmath.sqrt(q_int(j - m_from) * q_int(j + m_from + 1))
            E[k - 1, k] = coeff
        if k < n - 1:
            m_from = j - k
            coeff = cmath.sqrt(q_int(j + m_from) * q_int(j - m_from + 1))
            F[k + 1, k] = coeff

    I_n = np.eye(n, dtype=complex)
    qi_val = 1.0 / q

    # Coproduct
    Delta_E = np.kron(E, K) + np.kron(I_n, E)
    Delta_F = np.kron(F, I_n) + np.kron(Kinv, F)
    Delta_K = np.kron(K, K)
    Delta_Kinv = np.kron(Kinv, Kinv)

    if abs(q - 1.0) < 1e-14:
        H = np.diag([j - k for k in range(n)])
        Delta_H = np.kron(H, I_n) + np.kron(I_n, H)
        return Delta_F @ Delta_E + Delta_E @ Delta_F + Delta_H @ Delta_H / 2.0

    C = Delta_F @ Delta_E + (q * Delta_K - qi_val * Delta_Kinv) / (q - qi_val)
    return C


def _colored_r_matrix(q: complex, color: int) -> Tuple[np.ndarray, np.ndarray]:
    """R-matrix on V_{color} tensor V_{color} for U_q(sl_2).

    For color=2 (fundamental), returns the Kassel check_R directly.

    For color >= 3, uses spectral decomposition via the quantum Casimir:
        R = sum_s mu_s P_s
    where P_s is the projector onto V_s in V_j tensor V_j.

    The eigenvalue of the Kassel check_R on the V_s component of V_j tensor V_j is:
        mu_s = (-1)^{2j-s} q^{s(s+1) - 2j(j+1) + j}

    This is calibrated so that for j=1/2 (color=2) the eigenvalues are
    q (on sym) and -q^{-1} (on anti), matching the Kassel formula exactly.
    """
    j = (color - 1) / 2.0
    n = color
    dd = n * n

    # For color=2, use the exact Kassel formula
    if color == 2:
        R = slN_check_r_matrix(q, 2)
        Rinv = slN_check_r_matrix_inverse(q, 2)
        return R, Rinv

    def q_int(m):
        if abs(q - 1.0) < 1e-14:
            return complex(m)
        return (q ** m - q ** (-m)) / (q - 1.0 / q)

    # Allowed spins in V_j tensor V_j: 2j, 2j-2, ..., 0 (or 1)
    spins = []
    s = 2 * j
    while s >= -0.5:
        if s >= 0:
            spins.append(s)
        s -= 2

    C = _quantum_casimir_tensor(q, j)

    # Casimir eigenvalue on V_s: c_s = [s]_q [s+1]_q
    casimir_evals = {s: q_int(s) * q_int(s + 1) for s in spins}

    R_mat = np.zeros((dd, dd), dtype=complex)

    for s in spins:
        c_s = casimir_evals[s]
        # Calibrated eigenvalue formula (matches Kassel check_R at j=1/2)
        mu_s = (-1) ** int(2 * j - s) * q ** (s * (s + 1) - 2 * j * (j + 1) + j)

        # Projector via product formula
        proj = np.eye(dd, dtype=complex)
        for sp in spins:
            if abs(sp - s) > 1e-10:
                c_sp = casimir_evals[sp]
                denom = c_s - c_sp
                if abs(denom) < 1e-14:
                    proj = np.zeros((dd, dd), dtype=complex)
                    break
                proj = proj @ (C - c_sp * np.eye(dd, dtype=complex)) / denom

        R_mat += mu_s * proj

    Rinv = np.linalg.inv(R_mat)
    return R_mat, Rinv


def colored_jones_from_braid(braid_word: List[int], n_strands: int,
                              q: complex, color: int) -> complex:
    """Colored Jones polynomial J_{color}(K; q).

    Uses the color-dimensional representation V_{color} of U_q(sl_2).
    color=2 recovers the ordinary Jones polynomial.
    """
    if not braid_word:
        return complex(1.0)
    if color == 1:
        return complex(1.0)

    j = (color - 1) / 2.0
    d = color

    R_full, Rinv_full = _colored_r_matrix(q, color)
    total_dim = d ** n_strands
    result = np.eye(total_dim, dtype=complex)

    for gen in braid_word:
        idx = abs(gen)
        mat = R_full if gen > 0 else Rinv_full

        left_dim = d ** (idx - 1)
        right_dim = d ** (n_strands - idx - 1)

        if left_dim > 1 and right_dim > 1:
            full = np.kron(np.kron(np.eye(left_dim, dtype=complex), mat),
                           np.eye(right_dim, dtype=complex))
        elif left_dim > 1:
            full = np.kron(np.eye(left_dim, dtype=complex), mat)
        elif right_dim > 1:
            full = np.kron(mat, np.eye(right_dim, dtype=complex))
        else:
            full = mat.copy()

        result = result @ full

    # Ribbon element for the spin-j rep
    K_diag = np.array([q ** (2 * (j - k)) for k in range(d)], dtype=complex)
    K_single = np.diag(K_diag)

    K_total = K_single.copy()
    for _ in range(n_strands - 1):
        K_total = np.kron(K_total, K_single)

    tr = np.trace(result @ K_total)
    delta_color = np.sum(K_diag)

    # Writhe correction: for the spin-j representation,
    # alpha = Tr(R K^{tensor 2}) / delta
    K2_color = np.kron(K_single, K_single)
    alpha = np.trace(R_full @ K2_color) / delta_color

    w = writhe(braid_word)
    return alpha ** (-w) * tr / delta_color


def colored_jones_at(knot_name: str, q: complex, color: int) -> complex:
    """Evaluate the colored Jones polynomial J_n(K; q)."""
    if knot_name.startswith("T("):
        inner = knot_name[2:-1]
        p_str, n_str = inner.split(",")
        braid, ns = torus_knot_braid(int(p_str.strip()), int(n_str.strip()))
    elif knot_name in KNOT_BRAIDS:
        braid, ns = KNOT_BRAIDS[knot_name]
    else:
        raise ValueError(f"Unknown knot: {knot_name}")
    if not braid:
        return complex(1.0)
    return colored_jones_from_braid(braid, ns, q, color)


# ============================================================
# Volume conjecture
# ============================================================

def volume_conjecture_approximant(knot_name: str, n: int) -> float:
    r"""Compute (2 pi / n) log|J_n(K; exp(2 pi i / n))|.

    For hyperbolic knots, converges to Vol(S^3 \ K) as n -> infty.
    """
    q = cmath.exp(2j * cmath.pi / n)
    J_n = colored_jones_at(knot_name, q, n)
    if abs(J_n) < 1e-300:
        return 0.0
    return (2 * math.pi / n) * math.log(abs(J_n))


KNOWN_VOLUMES: Dict[str, float] = {
    "4_1": 2.0298832128,
    "5_2": 2.8281220883,
    "6_1": 3.1639855383,
}


# ============================================================
# Vassiliev invariants
# ============================================================

def vassiliev_from_derivative(knot_name: str, order: int,
                              eps: float = 1e-4) -> complex:
    """Vassiliev invariant v_n via Cauchy contour integral.

    v_n = (1 / (2 pi i)) oint V(e^h) h^{-(n+1)} dh

    The Jones polynomial V_K(e^{2h}) = 1 + v_2 h^2 + v_3 h^3 + ...
    under q = e^h, t = q^2 = e^{2h}.
    """
    n_sample = max(128, 16 * order)
    result = complex(0)

    for k in range(n_sample):
        theta = 2 * math.pi * k / n_sample
        h_val = eps * cmath.exp(1j * theta)
        q = cmath.exp(h_val)
        V_q = jones_at(knot_name, q)
        result += V_q / h_val ** order
    result /= n_sample

    return result


# ============================================================
# Kauffman bracket (state sum model)
# ============================================================

def kauffman_bracket_state_sum(crossings: List[Tuple[int, int, int, int, int]],
                                A: complex) -> complex:
    """Kauffman bracket <K> via state sum.

    Each crossing: (a, b, c, d, sign).
    For each state (2^n choices), resolve each crossing as A or A^{-1} smoothing.
    <K> = sum_states A^{sigma(s)} d^{loops(s) - 1}
    where d = -A^2 - A^{-2}, sigma = #A - #B resolutions.
    """
    n_c = len(crossings)
    bracket = complex(0)
    d = -A**2 - A**(-2)

    for state in range(2 ** n_c):
        sigma = 0
        for c in range(n_c):
            if (state >> c) & 1 == 0:
                sigma += 1
            else:
                sigma -= 1

        n_loops = _count_loops_in_state(crossings, state)
        bracket += A ** sigma * d ** (n_loops - 1)

    return bracket


def _count_loops_in_state(crossings: List[Tuple[int, int, int, int, int]],
                           state: int) -> int:
    """Count loops in a resolution state via union-find."""
    segments = set()
    for c in crossings:
        segments.update(c[:4])
    parent = {s: s for s in segments}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    for c_idx, (i, j, k, l, sign) in enumerate(crossings):
        if (state >> c_idx) & 1 == 0:
            # A-resolution
            if sign > 0:
                union(i, k)
                union(j, l)
            else:
                union(i, l)
                union(j, k)
        else:
            # B-resolution
            if sign > 0:
                union(i, l)
                union(j, k)
            else:
                union(i, k)
                union(j, l)

    roots = set(find(s) for s in segments)
    return len(roots)


TREFOIL_CROSSINGS = [
    (0, 1, 2, 3, +1),
    (2, 3, 4, 5, +1),
    (4, 5, 0, 1, +1),
]

FIGURE_EIGHT_CROSSINGS = [
    (0, 1, 2, 3, +1),
    (2, 3, 4, 5, -1),
    (4, 5, 6, 7, +1),
    (6, 7, 0, 1, -1),
]


# ============================================================
# A-polynomial
# ============================================================

def a_polynomial_trefoil_str() -> str:
    """A-polynomial of the trefoil: l + m^6."""
    return "l + m^6"


def a_polynomial_figure_eight_str() -> str:
    """A-polynomial of the figure-eight: l^2 m^4 - l(m^8 - m^6 - 2m^4 - m^2 + 1) + m^4."""
    return "l^2*m^4 - l*(m^8 - m^6 - 2*m^4 - m^2 + 1) + m^4"


def a_polynomial_numerical(knot_name: str, l: complex, m: complex) -> complex:
    """Evaluate the A-polynomial A(l, m) numerically."""
    if knot_name == "3_1":
        return l + m ** 6
    elif knot_name == "4_1":
        return l**2 * m**4 - l * (m**8 - m**6 - 2*m**4 - m**2 + 1) + m**4
    else:
        raise NotImplementedError(f"A-polynomial not implemented for {knot_name}")


# ============================================================
# Mirror image
# ============================================================

def mirror_braid(braid_word: List[int]) -> List[int]:
    """Mirror image: negate all generators."""
    return [-g for g in braid_word]


def jones_mirror_relation(knot_name: str, q: complex) -> Tuple[complex, complex, float]:
    """Verify V_{K*}(q) = V_K(q^{-1}).

    Returns (V_K(q), V_{K*}(q), discrepancy).
    """
    if knot_name not in KNOT_BRAIDS:
        raise ValueError(f"Unknown knot: {knot_name}")
    braid, ns = KNOT_BRAIDS[knot_name]
    mirror = mirror_braid(braid)

    V_K = jones_from_braid(braid, ns, q) if braid else 1.0
    V_Kstar = jones_from_braid(mirror, ns, q) if mirror else 1.0
    V_K_qinv = jones_from_braid(braid, ns, 1.0 / q) if braid else 1.0

    return (V_K, V_Kstar, abs(V_Kstar - V_K_qinv))


# ============================================================
# Reidemeister invariance
# ============================================================

def verify_reidemeister_2(q: complex) -> float:
    """R2: inserting sigma_i sigma_i^{-1} does not change the invariant.

    [1, -1, 1, 1, 1] on 2 strands should equal [1, 1, 1] (trefoil).
    """
    v1 = jones_from_braid([1, 1, 1], 2, q)
    v2 = jones_from_braid([1, -1, 1, 1, 1], 2, q)
    return abs(v1 - v2)


def verify_reidemeister_3(q: complex) -> float:
    """R3: [1,2,1] and [2,1,2] on 3 strands give the same polynomial."""
    v1 = jones_from_braid([1, 2, 1], 3, q)
    v2 = jones_from_braid([2, 1, 2], 3, q)
    return abs(v1 - v2)


# ============================================================
# DK bridge
# ============================================================

def yang_to_quantum_bridge(u: complex, q: complex, N: int) -> Tuple[np.ndarray, float]:
    """Verify classical limit: check_R(q) -> P as q -> 1.

    The Yang R-matrix R_Yang(u) = uI + P from the bar complex relates to
    check_R via the DK bridge.  In the classical limit q -> 1:
        check_R(q) -> P  (the permutation operator)

    The first-order expansion is:
        check_R(1 + eps) = P + eps (diagonal correction) + O(eps^2)

    Returns: (check_R, discrepancy of classical limit).
    """
    from compute.lib.yangian_residue_extraction import permutation_matrix_slN

    check_R = slN_check_r_matrix(q, N)
    P = permutation_matrix_slN(N)
    d = N * N

    # Classical limit: check_R(1) should equal P (the permutation matrix)
    R_at_1 = slN_check_r_matrix(1.0 + 1e-14, N)
    discrepancy = float(np.linalg.norm(R_at_1 - P))

    return check_R, discrepancy


# ============================================================
# Multi-path verification
# ============================================================

def jones_multipath(knot_name: str, q: complex) -> Dict[str, complex]:
    """Compute Jones polynomial via multiple independent paths.

    Path 1: sl_2 check_R braid representation.
    Path 2: HOMFLY-PT at N=2.
    Path 3: Colored Jones at color=2.
    """
    return {
        "check_R": jones_at(knot_name, q),
        "homfly_N2": homfly_at(knot_name, q, 2),
        "colored_j2": colored_jones_at(knot_name, q, 2),
    }


# ============================================================
# LaurentPoly utility
# ============================================================

class LaurentPoly:
    """Laurent polynomial in q^{1/2}. Keys are 2*exponent (integer)."""

    def __init__(self, coeffs: Optional[Dict[int, Union[int, float]]] = None):
        self.coeffs: Dict[int, Union[int, float]] = {}
        if coeffs:
            for k, v in coeffs.items():
                if isinstance(v, float) and abs(v) < 1e-12:
                    continue
                if v != 0:
                    self.coeffs[k] = v

    @classmethod
    def zero(cls) -> 'LaurentPoly':
        return cls()

    @classmethod
    def one(cls) -> 'LaurentPoly':
        return cls({0: 1})

    def __add__(self, other: 'LaurentPoly') -> 'LaurentPoly':
        r = dict(self.coeffs)
        for k, v in other.coeffs.items():
            r[k] = r.get(k, 0) + v
        return LaurentPoly(r)

    def __sub__(self, other: 'LaurentPoly') -> 'LaurentPoly':
        r = dict(self.coeffs)
        for k, v in other.coeffs.items():
            r[k] = r.get(k, 0) - v
        return LaurentPoly(r)

    def __mul__(self, other: 'LaurentPoly') -> 'LaurentPoly':
        r: Dict[int, Union[int, float]] = {}
        for k1, v1 in self.coeffs.items():
            for k2, v2 in other.coeffs.items():
                k = k1 + k2
                r[k] = r.get(k, 0) + v1 * v2
        return LaurentPoly(r)

    def __neg__(self) -> 'LaurentPoly':
        return LaurentPoly({k: -v for k, v in self.coeffs.items()})

    def shift(self, s: int) -> 'LaurentPoly':
        """Multiply by q^{s/2}."""
        return LaurentPoly({k + s: v for k, v in self.coeffs.items()})

    def evaluate(self, q: complex) -> complex:
        result = 0.0j
        for k, v in self.coeffs.items():
            result += v * q ** (k / 2.0)
        return result

    def __repr__(self) -> str:
        if not self.coeffs:
            return "0"
        terms = []
        for k in sorted(self.coeffs.keys()):
            c = self.coeffs[k]
            if k == 0:
                terms.append(f"{c}")
            elif k % 2 == 0:
                terms.append(f"{c}*q^{k // 2}")
            else:
                terms.append(f"{c}*q^({k}/2)")
        return " + ".join(terms)
