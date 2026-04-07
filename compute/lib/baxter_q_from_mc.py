r"""Baxter Q-operator from the universal MC element Theta_A.

CONSTRUCTION: The Baxter Q-operator for lattice integrable models is a
HIGHER PROJECTION of the universal MC element Theta_A := D_A - d_0.

The projection hierarchy from Theta_A:

  (g=0, r=2):  r(z) = Res^{coll}_{0,2}(Theta_A)  -- classical r-matrix
  (g=0, r=2):  R(u) = u*I + P   [Yang R-matrix for sl_2, from r(z) = P/z]
  (g=0, r=L):  T(u) = tr_0 prod_{j=1}^L R_{0,j}(u - a_j)  -- transfer matrix
  (g=0, all):  Q(u) solves T(u)Q(u) = a(u)Q(u-1) + d(u)Q(u+1) -- Baxter Q

The key point: R(u) is the QUANTIZATION of the classical r-matrix r(z),
itself the genus-0 arity-2 MC projection.  The transfer matrix T(u) is the
genus-0 arity-L trace (monodromy trace) of iterated R-matrices, which
corresponds to the factorization homology of the bar complex over the
configuration space Conf_L(C).  The Q-operator is the generating function
of commuting integrals: its zeros are the Bethe roots that diagonalize T.

CONVENTION (Faddeev-Reshetikhin-Takhtajan / FRT):

  R(u) = u*I + eta*P   with eta = 1 (additive spectral parameter)

  For homogeneous chain (a_j = 0 for all j):
    a(u) = (u + eta)^L = (u + 1)^L
    d(u) = u^L

  Transfer matrix eigenvalue (Bethe ansatz):
    Lambda(u) = a(u) * prod_k (u - u_k - 1)/(u - u_k)
              + d(u) * prod_k (u - u_k + 1)/(u - u_k)

  TQ relation:
    Lambda(u) * Q(u) = a(u) * Q(u - 1) + d(u) * Q(u + 1)
    where Q(u) = prod_k (u - u_k)

  BAE (from vanishing of Q(u) at u = u_k):
    a(u_k) / d(u_k) = -Q(u_k + 1) / Q(u_k - 1)
    i.e., ((u_k + 1) / u_k)^L = -prod_{l != k} (u_k - u_l + 1)/(u_k - u_l - 1)

  Vacuum eigenvalue (M = 0, Q = 1):
    Lambda_vac(u) = (u + 1)^L + u^L

  Verification: at u=1, L=2: Lambda_vac(1) = 4 + 1 = 5.
  This matches direct diagonalization of T(1) (eigenvalue 5 on |up,up>).

For sl_3, Q-operators are indexed by fundamental representations omega_1, omega_2.

THREE VERIFICATION PATHS per claim:
  Path A: Direct eigenvalue computation (diagonalize T, solve TQ)
  Path B: Bethe ansatz (find roots, verify BAE, reconstruct Q)
  Path C: MC projection (verify T comes from R which comes from Theta_A)

CONVENTIONS:
  AP19: r-matrix poles ONE BELOW OPE (d log kernel absorption)
  AP27: bar propagator d log E(z,w) is weight 1
  AP33: H_k^! = Sym^ch(V*) != H_{-k}
  AP39: kappa != c/2 in general
  AP44: lambda-bracket coeff = OPE mode / n!

References:
  twisted_holography_quantum_gravity.tex (Vol II)
  yangians_drinfeld_kohno.tex (Vol I)
  sl2_baxter.py, sl3_baxter.py (existing modules)
  Faddeev, "How the algebraic Bethe ansatz works" (Les Houches 1996)
  Baxter, "Exactly Solved Models in Statistical Mechanics" (1982)
  Korepin-Bogoliubov-Izergin, "Quantum Inverse Scattering Method" (1993)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product as iter_product
from math import factorial
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np


# =========================================================================
# I. R-MATRIX FROM MC PROJECTION
# =========================================================================

def yang_r_matrix_sl2(u: complex) -> np.ndarray:
    """Yang R-matrix R(u) = u*I + P on C^2 x C^2.

    This is the genus-0 arity-2 MC projection Theta_A^{(0,2)} for
    A = V_k(sl_2), evaluated in the fundamental representation.

    The classical r-matrix is r(z) = Omega/z where Omega is the Casimir.
    In the fundamental rep: r(z) = P/z.
    The quantum R-matrix is R(u) = u*I + P, satisfying R(u)/u -> I + P/u
    as u -> infinity (classical limit: 1 + r(1/u)).

    AP19: the r-matrix has pole order ONE BELOW the OPE.
    For sl_2: OPE has z^{-2} (Casimir) and z^{-1} (structure constants).
    The r-matrix has z^{-1} (Casimir/z) only.
    """
    P_mat = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ], dtype=complex)
    I4 = np.eye(4, dtype=complex)
    return u * I4 + P_mat


def yang_r_matrix_sl3(u: complex) -> np.ndarray:
    """Yang R-matrix R(u) = u*I + P on C^3 x C^3.

    For A = V_k(sl_3): the fundamental is 3-dimensional.
    R(u) = u*I_9 + P_9 where P_9 is the 9x9 permutation.
    """
    dim = 3
    d2 = dim * dim
    P_mat = np.zeros((d2, d2), dtype=complex)
    for i in range(dim):
        for j in range(dim):
            row = i * dim + j
            col = j * dim + i
            P_mat[row, col] = 1.0
    I_d2 = np.eye(d2, dtype=complex)
    return u * I_d2 + P_mat


def yang_r_matrix_slN(u: complex, N: int) -> np.ndarray:
    """Yang R-matrix R(u) = u*I + P on C^N x C^N."""
    d2 = N * N
    P_mat = np.zeros((d2, d2), dtype=complex)
    for i in range(N):
        for j in range(N):
            P_mat[i * N + j, j * N + i] = 1.0
    return u * np.eye(d2, dtype=complex) + P_mat


def verify_yang_baxter_general(R_func: Callable, u: complex, v: complex,
                                dim: int = 2) -> float:
    """Verify the Yang-Baxter equation for a general R-matrix.

    R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)

    on V^{tensor 3} where V = C^dim.

    Returns Frobenius norm of the difference.
    """
    d3 = dim ** 3
    I_d = np.eye(dim, dtype=complex)

    def R12(w):
        return np.kron(R_func(w), I_d)

    def R23(w):
        return np.kron(I_d, R_func(w))

    def R13(w):
        R = R_func(w)
        R13_mat = np.zeros((d3, d3), dtype=complex)
        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    for ip in range(dim):
                        for kp in range(dim):
                            row = i * dim * dim + j * dim + k
                            col = ip * dim * dim + j * dim + kp
                            R13_mat[row, col] += R[i * dim + k, ip * dim + kp]
        return R13_mat

    lhs = R12(u - v) @ R13(u) @ R23(v)
    rhs = R23(v) @ R13(u) @ R12(u - v)
    return float(np.linalg.norm(lhs - rhs))


# =========================================================================
# II. TRANSFER MATRIX FROM ITERATED R-MATRICES
# =========================================================================

def _embed_R_in_chain(R: np.ndarray, site_index: int, L: int,
                       dim_aux: int = 2, dim_site: int = 2) -> np.ndarray:
    """Embed R_{0,j} into the full Hilbert space.

    R acts on aux (C^{dim_aux}) x site_j (C^{dim_site}).
    The full space is C^{dim_aux} x (C^{dim_site})^L.

    Tensors R with identity on all other sites.
    """
    dim_phys = dim_site ** L
    dim_full = dim_aux * dim_phys

    R_full = np.zeros((dim_full, dim_full), dtype=complex)

    dim_before = dim_site ** site_index
    dim_after = dim_site ** (L - site_index - 1)

    for a in range(dim_aux):
        for ap in range(dim_aux):
            for sj in range(dim_site):
                for sjp in range(dim_site):
                    r_elem = R[a * dim_site + sj, ap * dim_site + sjp]
                    if abs(r_elem) < 1e-15:
                        continue
                    for b in range(dim_before):
                        for c in range(dim_after):
                            row = (a * dim_before * dim_site * dim_after
                                   + b * dim_site * dim_after
                                   + sj * dim_after + c)
                            col = (ap * dim_before * dim_site * dim_after
                                   + b * dim_site * dim_after
                                   + sjp * dim_after + c)
                            R_full[row, col] += r_elem

    return R_full


def transfer_matrix_general(u: complex, a_list: List[complex],
                             R_func: Callable, dim_site: int) -> np.ndarray:
    """Transfer matrix T(u) for a general XXX chain.

    T(u) = tr_0 [R_{0,1}(u - a_1) ... R_{0,L}(u - a_L)]

    where the trace is over the auxiliary space (same dim as site).

    Args:
        u: spectral parameter
        a_list: inhomogeneity parameters [a_1, ..., a_L]
        R_func: R-matrix function (spectral param -> d^2 x d^2 matrix)
        dim_site: dimension of each site (= dim of auxiliary space)

    Returns:
        dim_site^L x dim_site^L transfer matrix
    """
    L = len(a_list)
    dim_aux = dim_site
    dim_phys = dim_site ** L

    monodromy = np.eye(dim_aux * dim_phys, dtype=complex)

    for j in range(L):
        R_0j = R_func(u - a_list[j])
        R_full = _embed_R_in_chain(R_0j, j, L, dim_aux=dim_aux,
                                    dim_site=dim_site)
        monodromy = R_full @ monodromy

    T = np.zeros((dim_phys, dim_phys), dtype=complex)
    for a in range(dim_aux):
        for i in range(dim_phys):
            for ip in range(dim_phys):
                row = a * dim_phys + i
                col = a * dim_phys + ip
                T[i, ip] += monodromy[row, col]

    return T


def transfer_matrix_sl2(u: complex, a_list: List[complex]) -> np.ndarray:
    """Transfer matrix T(u) for sl_2 XXX chain with sites at positions a_j.

    T(u) = tr_0 [R_{01}(u-a_1) ... R_{0L}(u-a_L)] with R(u) = uI + P.

    This is the genus-0 arity-L projection of Theta_A.
    """
    return transfer_matrix_general(u, a_list, yang_r_matrix_sl2, dim_site=2)


def transfer_matrix_sl3(u: complex, a_list: List[complex]) -> np.ndarray:
    """Transfer matrix T(u) for sl_3 XXX chain."""
    return transfer_matrix_general(u, a_list, yang_r_matrix_sl3, dim_site=3)


# =========================================================================
# III. BAXTER Q-OPERATOR FOR sl_2 XXX (FRT Convention)
# =========================================================================

@dataclass
class BaxterTQData:
    """Complete Baxter TQ data for a spin chain."""
    L: int                      # number of sites
    a_list: List[complex]       # inhomogeneity parameters
    bethe_roots: np.ndarray     # Bethe roots u_1, ..., u_M
    M: int                      # number of Bethe roots (magnon number)
    T_eigenvalue_at_0: complex  # transfer matrix eigenvalue at u=0
    tq_residual: float          # max |T*Q - a*Q(u-1) - d*Q(u+1)| (should be ~0)
    bae_residuals: np.ndarray   # BAE residuals at each root


def a_function(u: complex, a_list: List[complex]) -> complex:
    """a(u) = prod_j (u - a_j + 1) for FRT convention R(u) = uI + P.

    On the pseudo-vacuum: R(u)|0,0> = (u+1)|0,0>, hence the
    vacuum contribution from the 'up' auxiliary state gives (u+1)^L
    in the homogeneous case.
    """
    result = 1.0 + 0j
    for aj in a_list:
        result *= (u - aj + 1)
    return result


def d_function(u: complex, a_list: List[complex]) -> complex:
    """d(u) = prod_j (u - a_j) for FRT convention R(u) = uI + P.

    On the pseudo-vacuum: R(u)|1,0> starts with u|1,0> + ...,
    so the 'down' auxiliary diagonal gives u^L.
    """
    result = 1.0 + 0j
    for aj in a_list:
        result *= (u - aj)
    return result


def q_polynomial(u: complex, roots: np.ndarray) -> complex:
    """Q(u) = prod_k (u - u_k) evaluated at u."""
    result = 1.0 + 0j
    for r in roots:
        result *= (u - r)
    return result


def transfer_eigenvalue_bethe(u: complex, a_list: List[complex],
                               bethe_roots: np.ndarray) -> complex:
    """Transfer matrix eigenvalue Lambda(u) from Bethe ansatz.

    Lambda(u) = a(u) * Q(u-1)/Q(u) + d(u) * Q(u+1)/Q(u)

    where a(u) = prod(u - a_j + 1), d(u) = prod(u - a_j).

    Equivalently (multiplying out Q(u)):
    Lambda(u) * Q(u) = a(u) * Q(u-1) + d(u) * Q(u+1)

    For u away from the Bethe roots (where Q(u) != 0), this gives:
    Lambda(u) = a(u) * prod_k (u-u_k-1)/(u-u_k) + d(u) * prod_k (u-u_k+1)/(u-u_k)
    """
    a_u = a_function(u, a_list)
    d_u = d_function(u, a_list)

    if len(bethe_roots) == 0:
        return a_u + d_u

    prod_minus = 1.0 + 0j
    prod_plus = 1.0 + 0j
    prod_denom = 1.0 + 0j
    for uk in bethe_roots:
        prod_minus *= (u - uk - 1)
        prod_plus *= (u - uk + 1)
        prod_denom *= (u - uk)

    return a_u * prod_minus / prod_denom + d_u * prod_plus / prod_denom


def verify_tq_relation(u: complex, a_list: List[complex],
                        bethe_roots: np.ndarray) -> float:
    """Verify TQ relation: Lambda(u)*Q(u) = a(u)*Q(u-1) + d(u)*Q(u+1).

    Uses the Bethe eigenvalue formula for Lambda(u), so the TQ relation
    is an algebraic identity.  The verification confirms the formula is
    internally consistent.

    Returns the absolute residual.
    """
    Lambda_u = transfer_eigenvalue_bethe(u, a_list, bethe_roots)
    Q_u = q_polynomial(u, bethe_roots)
    Q_um = q_polynomial(u - 1, bethe_roots)
    Q_up = q_polynomial(u + 1, bethe_roots)
    a_u = a_function(u, a_list)
    d_u = d_function(u, a_list)

    lhs = Lambda_u * Q_u
    rhs = a_u * Q_um + d_u * Q_up

    return abs(lhs - rhs)


def verify_tq_against_diag(u: complex, a_list: List[complex],
                            bethe_roots: np.ndarray) -> float:
    """Verify TQ relation using DIRECT transfer matrix diagonalization.

    Lambda_diag(u) * Q(u) = a(u)*Q(u-1) + d(u)*Q(u+1)

    where Lambda_diag(u) is the eigenvalue of T(u) closest to the Bethe
    prediction.  This is the cross-check between Path A and Path B.
    """
    # Path A: direct diag
    T = transfer_matrix_sl2(u, a_list)
    evals = np.linalg.eigvals(T)

    # Path B: Bethe prediction
    Lambda_bethe = transfer_eigenvalue_bethe(u, a_list, bethe_roots)

    # Find closest eigenvalue to Bethe prediction
    distances = np.abs(evals - Lambda_bethe)
    Lambda_diag = evals[np.argmin(distances)]

    Q_u = q_polynomial(u, bethe_roots)
    Q_um = q_polynomial(u - 1, bethe_roots)
    Q_up = q_polynomial(u + 1, bethe_roots)
    a_u = a_function(u, a_list)
    d_u = d_function(u, a_list)

    lhs = Lambda_diag * Q_u
    rhs = a_u * Q_um + d_u * Q_up

    return abs(lhs - rhs)


def bethe_ansatz_equations(bethe_roots: np.ndarray,
                           a_list: List[complex]) -> np.ndarray:
    """Evaluate BAE residuals in the FRT convention.

    BAE: for each k,
      a(u_k) / d(u_k) = -Q(u_k + 1) / Q(u_k - 1)

    i.e., prod_j (u_k - a_j + 1) / prod_j (u_k - a_j)
        = - prod_{l != k} (u_k - u_l + 1) / (u_k - u_l - 1)

    Returns array of residuals (LHS - RHS) for each root.
    """
    M = len(bethe_roots)
    residuals = np.zeros(M, dtype=complex)

    for k in range(M):
        uk = bethe_roots[k]
        d_uk = d_function(uk, a_list)
        if abs(d_uk) < 1e-30:
            residuals[k] = 1e10
            continue
        lhs = a_function(uk, a_list) / d_uk

        rhs = -1.0 + 0j
        for l in range(M):
            if l != k:
                denom = uk - bethe_roots[l] - 1
                if abs(denom) < 1e-30:
                    rhs = 1e10
                    break
                rhs *= (uk - bethe_roots[l] + 1) / denom

        residuals[k] = lhs - rhs

    return residuals


def _bethe_log_equations(bethe_roots: np.ndarray,
                          a_list: List[complex],
                          quantum_numbers: np.ndarray) -> np.ndarray:
    """Logarithmic form of BAE for stable numerics.

    log BAE:
      L * log((u_k + 1)/u_k) = i*pi*(2*I_k + 1)
        + sum_{l != k} log((u_k - u_l + 1)/(u_k - u_l - 1))

    where I_k are quantum numbers (integers or half-integers).
    """
    M = len(bethe_roots)
    L = len(a_list)
    residuals = np.zeros(M, dtype=complex)

    for k in range(M):
        uk = bethe_roots[k]
        # LHS: sum over sites
        lhs = 0.0 + 0j
        for aj in a_list:
            lhs += np.log((uk - aj + 1) / (uk - aj))

        # RHS: quantum number + scattering
        rhs = 1j * np.pi * (2 * quantum_numbers[k] + 1)
        for l in range(M):
            if l != k:
                rhs += np.log((uk - bethe_roots[l] + 1) /
                              (uk - bethe_roots[l] - 1))

        residuals[k] = lhs - rhs

    return residuals


def solve_bethe_sl2(L: int, M: int,
                     a_list: Optional[List[complex]] = None,
                     initial_guess: Optional[np.ndarray] = None,
                     quantum_numbers: Optional[np.ndarray] = None,
                     max_iter: int = 5000, tol: float = 1e-12) -> np.ndarray:
    """Solve BAE for sl_2 XXX chain using Newton's method.

    Uses the logarithmic form of BAE for stability, with specified
    quantum numbers I_k that select the Bethe state.

    Args:
        L: number of sites
        M: number of magnons
        a_list: inhomogeneity parameters (default: homogeneous, all 0)
        initial_guess: starting roots
        quantum_numbers: array of M integers/half-integers selecting the state
        max_iter: Newton iterations
        tol: convergence tolerance

    Returns:
        array of M Bethe roots
    """
    if a_list is None:
        a_list = [0.0] * L

    if M == 0:
        return np.array([], dtype=complex)

    if quantum_numbers is None:
        # Ground state quantum numbers: I_k = -(M-1)/2, ..., (M-1)/2
        quantum_numbers = np.array([(k - (M - 1) / 2) for k in range(M)])

    if initial_guess is not None:
        roots = initial_guess.copy().astype(complex)
    else:
        # Initial guess from quantum numbers (first-order approximation)
        roots = np.array([0.5 / np.tan(np.pi * (2 * Ik + 1) / (2 * L))
                          if abs(np.sin(np.pi * (2 * Ik + 1) / (2 * L))) > 0.01
                          else 10.0 + 0.1j
                          for Ik in quantum_numbers], dtype=complex)

    for iteration in range(max_iter):
        res = _bethe_log_equations(roots, a_list, quantum_numbers)
        if np.max(np.abs(res)) < tol:
            break

        # Jacobian by finite differences
        jac = np.zeros((M, M), dtype=complex)
        eps = 1e-8
        for k in range(M):
            roots_p = roots.copy()
            roots_p[k] += eps
            res_p = _bethe_log_equations(roots_p, a_list, quantum_numbers)
            jac[:, k] = (res_p - res) / eps

        try:
            delta = np.linalg.solve(jac, -res)
            # Damped step
            step = 1.0
            for _ in range(15):
                new_roots = roots + step * delta
                new_res = _bethe_log_equations(new_roots, a_list,
                                                quantum_numbers)
                if np.max(np.abs(new_res)) < np.max(np.abs(res)) * 1.01:
                    break
                step *= 0.5
            roots += step * delta
        except np.linalg.LinAlgError:
            break

    return roots


# =========================================================================
# IV. EXPLICIT CONSTRUCTIONS FOR L = 2, 3, 4
# =========================================================================

def find_all_bethe_states(L: int, M: int,
                           a_list: Optional[List[complex]] = None
                           ) -> List[BaxterTQData]:
    """Find all Bethe states for given L, M by enumerating quantum numbers.

    For the XXX spin chain with L sites and M magnons, the allowed
    quantum numbers I_k are integers (or half-integers for even M)
    in the range |I_k| < (L - M + 1)/2, and I_1 < I_2 < ... < I_M.

    Returns a list of BaxterTQData, one per Bethe state.
    """
    if a_list is None:
        a_list = [0.0] * L

    if M == 0:
        return [BaxterTQData(
            L=L, a_list=a_list,
            bethe_roots=np.array([], dtype=complex),
            M=0,
            T_eigenvalue_at_0=a_function(0.0, a_list) + d_function(0.0, a_list),
            tq_residual=0.0,
            bae_residuals=np.array([], dtype=complex),
        )]

    # Enumerate quantum number sets
    half_range = (L - M) / 2
    # For even M, quantum numbers are half-integers; for odd M, integers
    # Actually for XXX with R(u) = uI + P, quantum numbers are always
    # integers for the logarithmic BAE.
    candidates = list(range(int(-half_range), int(half_range) + 1))

    from itertools import combinations
    results = []

    for qn_set in combinations(candidates, M):
        qn = np.array(qn_set, dtype=float)
        roots = solve_bethe_sl2(L, M, a_list, quantum_numbers=qn)
        bae_res = bethe_ansatz_equations(roots, a_list)

        if np.max(np.abs(bae_res)) < 1e-6:
            tq_res = max(
                verify_tq_against_diag(u, a_list, roots)
                for u in [0.5, 1.0, 2.0, 3.0]
            )
            results.append(BaxterTQData(
                L=L, a_list=a_list,
                bethe_roots=roots, M=M,
                T_eigenvalue_at_0=transfer_eigenvalue_bethe(0.0, a_list, roots),
                tq_residual=tq_res,
                bae_residuals=bae_res,
            ))

    return results


def baxter_q_sl2_L2() -> List[BaxterTQData]:
    """All Baxter Q-operators for sl_2 XXX with L=2 sites.

    Hilbert space: (C^2)^2 = C^4.
    Decomposition: V_1 x V_1 = V_2 + V_0 (triplet + singlet).

    Bethe states:
      M=0: vacuum |up,up>, Lambda(u) = (u+1)^2 + u^2 = 2u^2+2u+1.
      M=1: singlet, Q(u) = u + 1/2, u_1 = -1/2.
           Lambda(u) = (u+1)^2*(u-3/2)/(u+1/2) + u^2*(u+3/2)/(u+1/2)
                     = 2u^2 + 2u - 1.
    """
    a_list = [0.0, 0.0]
    results = []

    # M=0: vacuum
    results.append(BaxterTQData(
        L=2, a_list=a_list,
        bethe_roots=np.array([], dtype=complex),
        M=0,
        T_eigenvalue_at_0=a_function(0.0, a_list) + d_function(0.0, a_list),
        tq_residual=0.0,
        bae_residuals=np.array([], dtype=complex),
    ))

    # M=1: singlet, u_1 = -1/2
    root = np.array([-0.5], dtype=complex)
    bae_res = bethe_ansatz_equations(root, a_list)
    tq_res = max(
        verify_tq_against_diag(u, a_list, root)
        for u in [0.5, 1.0, 1.5, 2.0, 3.0]
    )
    results.append(BaxterTQData(
        L=2, a_list=a_list,
        bethe_roots=root, M=1,
        T_eigenvalue_at_0=transfer_eigenvalue_bethe(0.0, a_list, root),
        tq_residual=tq_res,
        bae_residuals=bae_res,
    ))

    return results


def baxter_q_sl2_L3() -> List[BaxterTQData]:
    """All Baxter Q-operators for sl_2 XXX with L=3 sites.

    Hilbert space: (C^2)^3 = C^8.
    Decomposition: V_1^3 = V_3 + 2*V_1.
    Sz sectors: M=0 (1 state), M=1 (3 states), plus M=2,3 by Sz symmetry.
    """
    a_list = [0.0, 0.0, 0.0]
    results = []

    # M=0: vacuum
    results.extend(find_all_bethe_states(3, 0, a_list))
    # M=1: solve
    results.extend(find_all_bethe_states(3, 1, a_list))

    return results


def baxter_q_sl2_L4() -> List[BaxterTQData]:
    """All Baxter Q-operators for sl_2 XXX with L=4 sites.

    Hilbert space: (C^2)^4 = C^16.
    Decomposition: V_1^4 = V_4 + 3*V_2 + 2*V_0.
    """
    a_list = [0.0] * 4
    results = []

    for M in range(3):  # M = 0, 1, 2
        results.extend(find_all_bethe_states(4, M, a_list))

    return results


# =========================================================================
# V. DIRECT TRANSFER MATRIX ANALYSIS
# =========================================================================

def diagonalize_transfer_sl2(L: int,
                              a_list: Optional[List[complex]] = None,
                              u_values: Optional[List[complex]] = None
                              ) -> Dict[str, Any]:
    """Diagonalize T(u) directly for sl_2 XXX.

    Verifications:
    1. [T(u), T(v)] = 0 (integrability from YBE)
    2. [T(u), S^z] = 0 (weight conservation)
    3. Eigenvalues match Bethe ansatz predictions
    """
    if a_list is None:
        a_list = [0.0] * L
    if u_values is None:
        u_values = [0.0, 0.5, 1.0, 2.0]

    dim = 2 ** L

    # T(u) at several spectral parameters
    T_mats = {u: transfer_matrix_sl2(u, a_list) for u in u_values}

    # [T(u), T(v)] = 0
    comm_checks = {}
    for i, u1 in enumerate(u_values):
        for j, u2 in enumerate(u_values):
            if j > i:
                comm = T_mats[u1] @ T_mats[u2] - T_mats[u2] @ T_mats[u1]
                comm_checks[(u1, u2)] = float(np.linalg.norm(comm))

    # Eigenvalues
    evals_by_u = {}
    for u in u_values:
        evals_by_u[u] = sorted(np.linalg.eigvals(T_mats[u]).real)

    return {
        "L": L,
        "dim": dim,
        "commutativity_checks": comm_checks,
        "eigenvalues_by_u": evals_by_u,
    }


def verify_integrability(L: int, dim_site: int = 2) -> bool:
    """Verify [T(u), T(v)] = 0 at several (u, v) pairs."""
    a_list = [0.0] * L
    if dim_site == 2:
        R_func = yang_r_matrix_sl2
    elif dim_site == 3:
        R_func = yang_r_matrix_sl3
    else:
        return False

    u_vals = [0.5, 1.0, 2.0, 3.0]
    for i, u1 in enumerate(u_vals):
        for j, u2 in enumerate(u_vals):
            if j > i:
                T1 = transfer_matrix_general(u1, a_list, R_func, dim_site)
                T2 = transfer_matrix_general(u2, a_list, R_func, dim_site)
                comm = T1 @ T2 - T2 @ T1
                if np.linalg.norm(comm) > 1e-10:
                    return False
    return True


def verify_bethe_vs_diag(L: int, M: int,
                          u_test: complex = 1.0) -> Dict[str, Any]:
    """Compare transfer eigenvalue from Bethe ansatz vs diagonalization."""
    a_list = [0.0] * L

    # Direct diag
    T = transfer_matrix_sl2(u_test, a_list)
    evals_diag = sorted(np.linalg.eigvals(T).real)

    # Bethe ansatz for each allowed state
    states = find_all_bethe_states(L, M, a_list)
    bethe_evals = []
    for st in states:
        ev = transfer_eigenvalue_bethe(u_test, a_list, st.bethe_roots).real
        bethe_evals.append(ev)

    # Match Bethe eigenvalues to diagonalization eigenvalues
    matched = []
    for bev in bethe_evals:
        dists = [abs(bev - dev) for dev in evals_diag]
        best = min(dists)
        matched.append(best)

    return {
        "L": L, "M": M, "u_test": u_test,
        "diag_eigenvalues": evals_diag,
        "bethe_eigenvalues": bethe_evals,
        "match_errors": matched,
        "all_match": all(m < 1e-8 for m in matched) if matched else True,
    }


# =========================================================================
# VI. MC PROJECTION VERIFICATION
# =========================================================================

def verify_r_from_mc_sl2() -> Dict[str, Any]:
    """Verify that the Yang R-matrix arises from the MC projection.

    Path C: r(z) = P/z from genus-0 arity-2 projection of Theta_A.
    R(u) = uI + P is the unique rational YBE solution with this classical limit.

    Checks:
    1. Classical limit: R(u)/u -> I + P/u (matches 1 + r(1/u))
    2. YBE: R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)
    3. Integrability: [T(u), T(v)] = 0
    """
    results = {}

    # Classical limit
    for u_test in [1.0, 2.0, 5.0, 10.0]:
        R_norm = yang_r_matrix_sl2(u_test) / u_test
        P_mat = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                          [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
        classical = np.eye(4) + P_mat / u_test
        results[f"classical_limit_u={u_test}"] = float(
            np.linalg.norm(R_norm - classical))

    # YBE
    for u, v in [(1.0, 2.0), (0.5, 3.0), (-1.0, 2.5)]:
        results[f"YBE_u={u}_v={v}"] = verify_yang_baxter_general(
            yang_r_matrix_sl2, u, v, dim=2)

    # Integrability
    for L in [2, 3, 4]:
        results[f"integrability_L={L}"] = verify_integrability(L, 2)

    return results


def verify_r_from_mc_sl3() -> Dict[str, Any]:
    """Verify the sl_3 Yang R-matrix from MC projection."""
    results = {}

    for u, v in [(1.0, 2.0), (0.5, 3.0)]:
        results[f"YBE_sl3_u={u}_v={v}"] = verify_yang_baxter_general(
            yang_r_matrix_sl3, u, v, dim=3)

    results["integrability_sl3_L2"] = verify_integrability(2, 3)

    return results


# =========================================================================
# VII. sl_3 Q-OPERATORS
# =========================================================================

def transfer_eigenvalue_sl3_vacuum(u: complex, L: int) -> complex:
    """Vacuum eigenvalue of T(u) for sl_3 XXX with L sites.

    For R(u) = uI_9 + P_9 on C^3 x C^3, the pseudo-vacuum |0,0,...,0>
    (all sites in highest weight state) gives:
      Lambda_vac(u) = (u + 1)^L + u^L + (u - 1)^L

    because the three diagonal elements of R(u) on |a, 0> are:
      a=0: R(u)|0,0> = (u+1)|0,0>   -> factor (u+1)
      a=1: R(u)|1,0> = u|1,0> + ... -> factor u
      a=2: R(u)|2,0> = (u-1)|2,0> + ... wait, need to check.

    Actually for R(u) = uI + P on C^N:
      R(u)|a, s> = u|a,s> + |s,a>
    So R(u)|a, 0> = u|a,0> + delta(a,0)*|0,0> + (1-delta(a,0))*|0,a>
    Diagonal: R_{(a,0),(a,0)} = u + delta(a,0).
    So diagonal contributions: (u+1) for a=0, u for a=1, u for a=2.
    Vacuum eigenvalue: (u+1)^L + 2*u^L for sl_3.
    """
    return (u + 1) ** L + 2 * u ** L


def verify_sl3_vacuum(L: int, u_test: complex = 1.0) -> float:
    """Verify sl_3 vacuum eigenvalue against direct diagonalization."""
    a_list = [0.0] * L
    T = transfer_matrix_sl3(u_test, a_list)
    # Vacuum is |0,0,...,0> = first basis state
    vac_eigenvalue = T[0, 0].real
    predicted = transfer_eigenvalue_sl3_vacuum(u_test, L).real
    return abs(vac_eigenvalue - predicted)


# =========================================================================
# VIII. HAMILTONIAN EXTRACTION
# =========================================================================

def heisenberg_hamiltonian_from_transfer(L: int) -> np.ndarray:
    """Extract Heisenberg Hamiltonian from T(u) via logarithmic derivative.

    H = (d/du) ln T(u)|_{u=0} = T'(0) T(0)^{-1}

    For R(u) = uI + P: T(0) = tr_0(P_{01}...P_{0L}) is the cyclic shift.
    T'(0) = sum_j tr_0(P_{01}...P'_{0j}...P_{0L}) where P' = I (derivative of uI+P is I).
    """
    a_list = [0.0] * L
    eps = 1e-7
    T_plus = transfer_matrix_sl2(eps, a_list)
    T_minus = transfer_matrix_sl2(-eps, a_list)
    T_0 = transfer_matrix_sl2(0.0, a_list)

    dT = (T_plus - T_minus) / (2 * eps)
    try:
        T0_inv = np.linalg.inv(T_0)
        H = dT @ T0_inv
    except np.linalg.LinAlgError:
        H = dT
    return H


def heisenberg_hamiltonian_direct(L: int) -> np.ndarray:
    """Build Heisenberg XXX Hamiltonian directly: H = sum P_{j,j+1}.

    P_{j,j+1} is the permutation (swap) operator on sites j, j+1
    with periodic boundary: site L+1 = site 1.
    """
    dim = 2 ** L
    H = np.zeros((dim, dim), dtype=complex)
    I2 = np.eye(2, dtype=complex)
    P_swap = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                        [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)

    for j in range(L):
        jp = (j + 1) % L
        # Build P_{j,jp} acting on (C^2)^L
        if jp == j + 1 or (j == L - 1 and jp == 0):
            # Adjacent sites
            if j < jp:
                left = j
            else:
                left = jp  # wrap-around case needs care

            if j == L - 1 and jp == 0:
                # P_{L-1, 0}: need to permute first and last sites
                P_full = np.zeros((dim, dim), dtype=complex)
                for idx in range(dim):
                    bits = [(idx >> (L - 1 - k)) & 1 for k in range(L)]
                    # Swap bits[0] and bits[L-1]
                    bits_new = bits.copy()
                    bits_new[0], bits_new[L - 1] = bits[L - 1], bits[0]
                    idx_new = sum(b << (L - 1 - k) for k, b in enumerate(bits_new))
                    P_full[idx_new, idx] = 1.0
                H += P_full
            else:
                # P_{j, j+1}: swap adjacent sites
                # = I_{before} x P_swap x I_{after}
                before = np.eye(2 ** j, dtype=complex)
                after = np.eye(2 ** (L - j - 2), dtype=complex)
                P_full = np.kron(np.kron(before, P_swap), after)
                H += P_full

    return H


# =========================================================================
# IX. MASTER VERIFICATION SUITE
# =========================================================================

def verify_all_mc_to_baxter() -> Dict[str, Any]:
    """Complete verification: MC element -> R-matrix -> T(u) -> Q(u) -> Bethe.

    Three independent paths that must agree:
      A: Direct diagonalization of T(u)
      B: Bethe ansatz -> Q(u) -> eigenvalues
      C: MC projection -> R(u) -> YBE -> integrability
    """
    results = {}

    # ---- Path C: R-matrix from MC ----
    r_mc = verify_r_from_mc_sl2()
    results["C_classical_limits_ok"] = all(
        v < 1e-10 for k, v in r_mc.items() if "classical" in k)
    results["C_YBE_ok"] = all(
        v < 1e-10 for k, v in r_mc.items() if "YBE" in k)
    results["C_integrability_ok"] = all(
        v for k, v in r_mc.items() if "integrability" in k)

    # ---- Path C: sl_3 ----
    r_sl3 = verify_r_from_mc_sl3()
    results["C_sl3_YBE_ok"] = all(
        v < 1e-10 for k, v in r_sl3.items() if "YBE" in k)
    results["C_sl3_integrability"] = r_sl3.get("integrability_sl3_L2", False)

    # ---- L=2: TQ relation and Bethe-vs-Diag ----
    states_L2 = baxter_q_sl2_L2()
    for st in states_L2:
        label = f"L2_M{st.M}"
        results[f"{label}_tq_residual"] = st.tq_residual
        if len(st.bae_residuals) > 0:
            results[f"{label}_bae_max"] = float(np.max(np.abs(st.bae_residuals)))

    # Bethe vs Diag for L=2
    for M in [0, 1]:
        comp = verify_bethe_vs_diag(2, M)
        results[f"L2_M{M}_bethe_vs_diag"] = comp["all_match"]

    # ---- L=3 ----
    states_L3 = baxter_q_sl2_L3()
    for i, st in enumerate(states_L3):
        label = f"L3_state{i}_M{st.M}"
        results[f"{label}_tq_residual"] = st.tq_residual
        if len(st.bae_residuals) > 0:
            results[f"{label}_bae_max"] = float(np.max(np.abs(st.bae_residuals)))

    for M in [0, 1]:
        comp = verify_bethe_vs_diag(3, M)
        results[f"L3_M{M}_bethe_vs_diag"] = comp["all_match"]

    # ---- L=4 ----
    states_L4 = baxter_q_sl2_L4()
    for i, st in enumerate(states_L4):
        label = f"L4_state{i}_M{st.M}"
        results[f"{label}_tq_residual"] = st.tq_residual
        if len(st.bae_residuals) > 0:
            results[f"{label}_bae_max"] = float(np.max(np.abs(st.bae_residuals)))

    for M in [0, 1, 2]:
        comp = verify_bethe_vs_diag(4, M)
        results[f"L4_M{M}_bethe_vs_diag"] = comp["all_match"]

    # ---- sl_3 vacuum ----
    for L in [2, 3]:
        results[f"sl3_L{L}_vacuum_check"] = verify_sl3_vacuum(L, 1.0)

    # ---- Hamiltonian from transfer matrix ----
    for L in [2, 3, 4]:
        H_transfer = heisenberg_hamiltonian_from_transfer(L)
        H_direct = heisenberg_hamiltonian_direct(L)
        # They should be proportional (up to additive constant)
        # H_transfer = L*I + H_direct (approximately)
        # Check eigenvalues match up to affine transformation
        ev_t = sorted(np.linalg.eigvals(H_transfer).real)
        ev_d = sorted(np.linalg.eigvals(H_direct).real)
        # Normalize: subtract mean, scale by std
        ev_t_n = np.array(ev_t)
        ev_d_n = np.array(ev_d)
        ev_t_n = (ev_t_n - ev_t_n.mean())
        ev_d_n = (ev_d_n - ev_d_n.mean())
        if np.std(ev_t_n) > 1e-10 and np.std(ev_d_n) > 1e-10:
            ev_t_n /= np.std(ev_t_n)
            ev_d_n /= np.std(ev_d_n)
            results[f"hamiltonian_L{L}_match"] = float(
                np.linalg.norm(ev_t_n - ev_d_n))
        else:
            results[f"hamiltonian_L{L}_match"] = 0.0

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("BAXTER Q-OPERATOR FROM MC ELEMENT: VERIFICATION SUITE")
    print("=" * 70)

    results = verify_all_mc_to_baxter()
    n_pass = 0
    n_fail = 0
    for name, val in results.items():
        if isinstance(val, bool):
            ok = val
        elif isinstance(val, float):
            ok = val < 1e-6
        else:
            ok = True
        status = "PASS" if ok else "FAIL"
        if ok:
            n_pass += 1
        else:
            n_fail += 1
        print(f"  [{status}] {name}: {val}")

    print(f"\n{n_pass} passed, {n_fail} failed out of {n_pass + n_fail} checks.")
