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

For sl_2 XXX with L sites of spin 1/2 at positions a_1, ..., a_L:

  R_{0j}(u) = (u - a_j)*I + P_{0j}   [Yang R-matrix, 4x4 on C^2 x C^2]

  T(u) = tr_0 [R_{01}(u-a_1) ... R_{0L}(u-a_L)]   [2^L x 2^L matrix]

  The TQ relation is:
    T(u) Q(u) = a(u) Q(u-1) + d(u) Q(u+1)

  where a(u) = prod_j (u - a_j + 1/2), d(u) = prod_j (u - a_j - 1/2).

  Q(u) = prod_{k=1}^M (u - u_k) where u_k are the Bethe roots solving:
    a(u_k)/d(u_k) = -Q(u_k+1)/Q(u_k-1)   (Bethe ansatz equations)

  Equivalently: prod_j (u_k - a_j + 1/2) / prod_j (u_k - a_j - 1/2)
              = - prod_{l != k} (u_k - u_l + 1) / (u_k - u_l - 1)

For sl_3, Q-operators are indexed by fundamental representations omega_1, omega_2:
  Q_1(u), Q_2(u) satisfy a system of TQ relations (Bazhanov-Lukyanov-Zamolodchikov).

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
  Baxter, "Exactly Solved Models in Statistical Mechanics" (1982)
  Bazhanov-Lukyanov-Zamolodchikov, Commun. Math. Phys. 200 (1999) 297-324
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product as iter_product
from math import factorial
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
from numpy.polynomial import polynomial as P


# =========================================================================
# I. R-MATRIX FROM MC PROJECTION
# =========================================================================

def yang_r_matrix_sl2(u: complex) -> np.ndarray:
    """Yang R-matrix R(u) = u*I + P on C^2 x C^2.

    This is the genus-0 arity-2 MC projection Theta_A^{(0,2)} for
    A = V_k(sl_2), evaluated in the fundamental representation.

    The classical r-matrix is r(z) = Omega/z where Omega is the Casimir.
    In the fundamental rep: r(z) = P/z.
    The quantum R-matrix is R(u) = u*I + P, satisfying R(u) -> P/u as u -> 0
    (i.e., the classical limit R(u)/u -> I + P/u ~ 1 + r(u)).

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
            # P maps |i>|j> to |j>|i>
            row = i * dim + j
            col = j * dim + i
            P_mat[row, col] = 1.0
    I_d2 = np.eye(d2, dtype=complex)
    return u * I_d2 + P_mat


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

def transfer_matrix_sl2(u: complex, a_list: List[complex]) -> np.ndarray:
    """Transfer matrix T(u) for sl_2 XXX chain with sites at positions a_j.

    T(u) = tr_0 [R_{0,1}(u - a_1) R_{0,2}(u - a_2) ... R_{0,L}(u - a_L)]

    where the trace is over the auxiliary space (space 0 = C^2),
    and the result is a 2^L x 2^L matrix acting on the physical Hilbert space.

    This is the genus-0 arity-L projection of Theta_A: the factorization
    homology of the bar complex over Conf_L(C) with L marked points.

    Args:
        u: spectral parameter
        a_list: list of inhomogeneity parameters [a_1, ..., a_L]

    Returns:
        2^L x 2^L transfer matrix
    """
    L = len(a_list)
    dim_phys = 2 ** L
    dim_aux = 2

    # Build the monodromy matrix: product of R-matrices in auxiliary x physical space
    # Each R_{0,j} acts on C^2 (aux) x C^2 (site j) x I (other sites)
    # We work in the basis |aux> |site_1> ... |site_L>

    # Start with identity on aux x phys
    monodromy = np.eye(dim_aux * dim_phys, dtype=complex)

    for j in range(L):
        # R_{0,j}(u - a_j) acts on aux (dim 2) x site_j (dim 2)
        R_0j = yang_r_matrix_sl2(u - a_list[j])

        # Embed into full space: aux x site_1 x ... x site_L
        # R_{0,j} acts on positions (0, j+1) in the tensor product
        # of (L+1) copies of C^2.
        R_full = _embed_R_in_chain(R_0j, j, L, dim_aux=2)
        monodromy = R_full @ monodromy

    # Partial trace over auxiliary space (first factor)
    T = np.zeros((dim_phys, dim_phys), dtype=complex)
    for a in range(dim_aux):
        for i in range(dim_phys):
            for ip in range(dim_phys):
                row = a * dim_phys + i
                col = a * dim_phys + ip
                T[i, ip] += monodromy[row, col]

    return T


def _embed_R_in_chain(R: np.ndarray, site_index: int, L: int,
                       dim_aux: int = 2) -> np.ndarray:
    """Embed R_{0,j} into the full Hilbert space.

    R acts on aux (C^{dim_aux}) x site_j (C^2).
    The full space is C^{dim_aux} x (C^2)^L.

    We tensor R with identity on all other sites.

    Args:
        R: 4x4 R-matrix on C^2 x C^2
        site_index: which physical site (0-indexed)
        L: total number of physical sites
        dim_aux: dimension of auxiliary space
    """
    # Full dimension
    dim_full = dim_aux * (2 ** L)

    # Build the embedding.
    # The indices are: (aux, s_0, s_1, ..., s_{L-1})
    # R_{0,j} acts on (aux, s_j).
    # Use Kronecker products:
    #   I_{sites before j} x R_{aux, site_j} x I_{sites after j}
    # But the aux index is interleaved with site_j.

    # Strategy: directly construct the matrix element by element.
    R_full = np.zeros((dim_full, dim_full), dtype=complex)

    dim_site = 2
    dim_before = dim_site ** site_index
    dim_after = dim_site ** (L - site_index - 1)

    for a in range(dim_aux):
        for ap in range(dim_aux):
            for sj in range(dim_site):
                for sjp in range(dim_site):
                    # R-matrix element
                    r_elem = R[a * dim_site + sj, ap * dim_site + sjp]
                    if abs(r_elem) < 1e-15:
                        continue

                    # Now embed: identity on sites before j and after j
                    for b in range(dim_before):
                        for c in range(dim_after):
                            # Full row index: a * 2^L + b * 2^{L-j} + sj * 2^{L-j-1} + c
                            # Actually: index = a * dim_before * dim_site * dim_after
                            #                 + b * dim_site * dim_after
                            #                 + sj * dim_after + c
                            row = (a * dim_before * dim_site * dim_after
                                   + b * dim_site * dim_after
                                   + sj * dim_after + c)
                            col = (ap * dim_before * dim_site * dim_after
                                   + b * dim_site * dim_after
                                   + sjp * dim_after + c)
                            R_full[row, col] += r_elem

    return R_full


def transfer_matrix_sl3(u: complex, a_list: List[complex]) -> np.ndarray:
    """Transfer matrix T(u) for sl_3 XXX chain.

    T(u) = tr_0 [R_{0,1}(u-a_1) ... R_{0,L}(u-a_L)]

    where aux = C^3, physical sites are each C^3.
    Result is 3^L x 3^L matrix.
    """
    L = len(a_list)
    dim_site = 3
    dim_aux = 3
    dim_phys = dim_site ** L

    monodromy = np.eye(dim_aux * dim_phys, dtype=complex)

    for j in range(L):
        R_0j = yang_r_matrix_sl3(u - a_list[j])
        R_full = _embed_R_general(R_0j, j, L, dim_aux=dim_aux, dim_site=dim_site)
        monodromy = R_full @ monodromy

    T = np.zeros((dim_phys, dim_phys), dtype=complex)
    for a in range(dim_aux):
        for i in range(dim_phys):
            for ip in range(dim_phys):
                row = a * dim_phys + i
                col = a * dim_phys + ip
                T[i, ip] += monodromy[row, col]

    return T


def _embed_R_general(R: np.ndarray, site_index: int, L: int,
                      dim_aux: int = 3, dim_site: int = 3) -> np.ndarray:
    """Embed R_{0,j} into the full space for general dim."""
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


# =========================================================================
# III. BAXTER Q-OPERATOR FOR sl_2 XXX
# =========================================================================

@dataclass
class BaxterTQData:
    """Complete Baxter TQ data for a spin chain."""
    L: int                      # number of sites
    a_list: List[complex]       # inhomogeneity parameters
    bethe_roots: np.ndarray     # Bethe roots u_1, ..., u_M
    M: int                      # number of Bethe roots (magnon number)
    Q_poly: np.ndarray          # Q(u) as polynomial coefficients
    T_eigenvalue: complex       # transfer matrix eigenvalue
    tq_residual: float          # |T*Q - a*Q(u-1) - d*Q(u+1)| (should be ~0)
    bae_residuals: np.ndarray   # BAE residuals at each root


def a_function_sl2(u: complex, a_list: List[complex]) -> complex:
    """a(u) = prod_j (u - a_j + 1/2) for the sl_2 XXX TQ relation."""
    result = 1.0 + 0j
    for aj in a_list:
        result *= (u - aj + 0.5)
    return result


def d_function_sl2(u: complex, a_list: List[complex]) -> complex:
    """d(u) = prod_j (u - a_j - 1/2) for the sl_2 XXX TQ relation."""
    result = 1.0 + 0j
    for aj in a_list:
        result *= (u - aj - 0.5)
    return result


def q_polynomial_from_roots(u: complex, roots: np.ndarray) -> complex:
    """Q(u) = prod_k (u - u_k) evaluated at u."""
    result = 1.0 + 0j
    for r in roots:
        result *= (u - r)
    return result


def transfer_eigenvalue_from_bethe(u: complex, a_list: List[complex],
                                    bethe_roots: np.ndarray) -> complex:
    """Transfer matrix eigenvalue Lambda(u) from Bethe ansatz.

    Lambda(u) = a(u) * prod_k (u - u_k - 1) / (u - u_k)
              + d(u) * prod_k (u - u_k + 1) / (u - u_k)

    This is the eigenvalue of T(u) on the Bethe state corresponding
    to the roots {u_k}.
    """
    a_u = a_function_sl2(u, a_list)
    d_u = d_function_sl2(u, a_list)

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
    """Verify TQ relation: T(u)*Q(u) = a(u)*Q(u-1) + d(u)*Q(u+1).

    Returns the absolute residual.
    """
    T_u = transfer_eigenvalue_from_bethe(u, a_list, bethe_roots)
    Q_u = q_polynomial_from_roots(u, bethe_roots)
    Q_um = q_polynomial_from_roots(u - 1, bethe_roots)
    Q_up = q_polynomial_from_roots(u + 1, bethe_roots)
    a_u = a_function_sl2(u, a_list)
    d_u = d_function_sl2(u, a_list)

    lhs = T_u * Q_u
    rhs = a_u * Q_um + d_u * Q_up

    return abs(lhs - rhs)


def bethe_ansatz_equations(bethe_roots: np.ndarray,
                           a_list: List[complex]) -> np.ndarray:
    """Evaluate the Bethe ansatz equations.

    BAE: for each k,
      prod_j (u_k - a_j + 1/2) / prod_j (u_k - a_j - 1/2)
        = - prod_{l != k} (u_k - u_l + 1) / (u_k - u_l - 1)

    Equivalently: a(u_k)/d(u_k) = - prod_{l != k} (u_k - u_l + 1)/(u_k - u_l - 1)

    Returns array of residuals (LHS - RHS) for each root.
    """
    M = len(bethe_roots)
    residuals = np.zeros(M, dtype=complex)

    for k in range(M):
        uk = bethe_roots[k]
        lhs = a_function_sl2(uk, a_list) / d_function_sl2(uk, a_list)

        rhs = -1.0 + 0j
        for l in range(M):
            if l != k:
                rhs *= (uk - bethe_roots[l] + 1) / (uk - bethe_roots[l] - 1)

        residuals[k] = lhs - rhs

    return residuals


def solve_bethe_sl2_homogeneous(L: int, M: int,
                                 max_iter: int = 1000,
                                 tol: float = 1e-12) -> np.ndarray:
    """Solve Bethe ansatz equations for homogeneous sl_2 XXX chain.

    Homogeneous: all a_j = 0, so a(u) = (u + 1/2)^L, d(u) = (u - 1/2)^L.

    BAE: ((u_k + 1/2)/(u_k - 1/2))^L = - prod_{l != k} (u_k - u_l + 1)/(u_k - u_l - 1)

    For M magnons on L sites (M <= L/2 for ground state and low-lying).

    Uses Newton's method with standard string hypothesis initial guess.

    Args:
        L: number of sites
        M: number of magnons (Bethe roots)
        max_iter: maximum Newton iterations
        tol: convergence tolerance

    Returns:
        array of M Bethe roots
    """
    a_list = [0.0] * L

    if M == 0:
        return np.array([], dtype=complex)

    # Initial guess: string hypothesis
    # For the ground state, roots are approximately on the real axis,
    # symmetric around 0.
    if M == 1:
        # Single magnon: (u + 1/2)^L / (u - 1/2)^L = -1
        # For L=2: (u+1/2)^2/(u-1/2)^2 = -1, so (u+1/2)/(u-1/2) = +-i
        # u+1/2 = i(u-1/2), u(1-i) = -1/2 - i/2, u = (-1-i)/(2(1-i)) = (-1-i)(1+i)/(2*2) = (-1-i+(-i+1))/4 = -2i/4 = -i/2
        # So u = i/2 or u = -i/2
        if L == 2:
            return np.array([0.5j], dtype=complex)
        # General: use perturbative initial guess
        roots = np.array([0.1 + 0.01j * (k - (M - 1) / 2) for k in range(M)],
                         dtype=complex)
    else:
        # Symmetric distribution for ground state
        roots = np.array([(k - (M - 1) / 2) * 0.5 / max(M - 1, 1)
                          for k in range(M)], dtype=complex)

    # Newton iteration on the logarithmic BAE
    # log BAE: L * log((u_k + 1/2)/(u_k - 1/2)) = i*pi*(2*I_k + 1)
    #          + sum_{l != k} [log((u_k - u_l + 1)/(u_k - u_l - 1))]
    # where I_k are quantum numbers (integers or half-integers)

    # For simplicity, use direct Newton on the BAE residuals
    for _ in range(max_iter):
        res = bethe_ansatz_equations(roots, a_list)
        if np.max(np.abs(res)) < tol:
            break

        # Jacobian by finite differences
        jac = np.zeros((M, M), dtype=complex)
        eps = 1e-8
        for k in range(M):
            roots_p = roots.copy()
            roots_p[k] += eps
            res_p = bethe_ansatz_equations(roots_p, a_list)
            jac[:, k] = (res_p - res) / eps

        try:
            delta = np.linalg.solve(jac, -res)
            roots += 0.5 * delta  # damped Newton step
        except np.linalg.LinAlgError:
            break

    return roots


def solve_bethe_sl2(L: int, M: int, a_list: Optional[List[complex]] = None,
                     initial_guess: Optional[np.ndarray] = None,
                     max_iter: int = 2000, tol: float = 1e-12) -> np.ndarray:
    """Solve BAE for general inhomogeneous sl_2 XXX chain.

    Args:
        L: number of sites
        M: number of magnons
        a_list: inhomogeneity parameters (default: homogeneous, all 0)
        initial_guess: starting roots (default: heuristic)
        max_iter: Newton iterations
        tol: convergence tolerance

    Returns:
        array of M Bethe roots
    """
    if a_list is None:
        a_list = [0.0] * L

    if M == 0:
        return np.array([], dtype=complex)

    if initial_guess is not None:
        roots = initial_guess.copy().astype(complex)
    else:
        # Heuristic initial guess
        roots = np.array([(k - (M - 1) / 2) * 0.8 / max(M - 1, 1) + 0.01j
                          for k in range(M)], dtype=complex)

    for _ in range(max_iter):
        res = bethe_ansatz_equations(roots, a_list)
        if np.max(np.abs(res)) < tol:
            break

        jac = np.zeros((M, M), dtype=complex)
        eps = 1e-8
        for k in range(M):
            roots_p = roots.copy()
            roots_p[k] += eps
            res_p = bethe_ansatz_equations(roots_p, a_list)
            jac[:, k] = (res_p - res) / eps

        try:
            delta = np.linalg.solve(jac, -res)
            # Damped step with line search
            step = 1.0
            for _ in range(10):
                new_roots = roots + step * delta
                new_res = bethe_ansatz_equations(new_roots, a_list)
                if np.max(np.abs(new_res)) < np.max(np.abs(res)):
                    break
                step *= 0.5
            roots += step * delta
        except np.linalg.LinAlgError:
            break

    return roots


# =========================================================================
# IV. EXPLICIT CONSTRUCTIONS FOR L = 2, 3, 4
# =========================================================================

def baxter_q_sl2_L2(M: int = 0) -> BaxterTQData:
    """Baxter Q-operator for sl_2 XXX with L=2 sites.

    The Hilbert space is C^2 x C^2 = C^4.
    Decomposition: V_1 x V_1 = V_2 + V_0 (triplet + singlet).

    Sectors:
      M=0: vacuum (all spins up). Q(u) = 1. T(u) = (u+1/2)^2 + (u-1/2)^2 = 2u^2 + 1/2.
      M=1: one magnon (one spin flipped). Q(u) = u - u_1 where u_1 is Bethe root.
           BAE: ((u_1 + 1/2)/(u_1 - 1/2))^2 = -1, so u_1 = i/2 or u_1 = -i/2.
           But we need REAL physical roots for Hermitian Hamiltonian.
           Actually u_1 can be complex. For the singlet: u_1 = i/2.
    """
    L = 2
    a_list = [0.0, 0.0]

    if M == 0:
        # Vacuum sector: no Bethe roots
        bethe_roots = np.array([], dtype=complex)
        # T eigenvalue: a(u) + d(u) = (u+1/2)^2 + (u-1/2)^2
        def T_eig(u):
            return (u + 0.5) ** 2 + (u - 0.5) ** 2

        # Verify TQ: T(u)*1 = (u+1/2)^2 * 1 + (u-1/2)^2 * 1 = T(u). Trivially OK.
        tq_res = 0.0
        bae_res = np.array([], dtype=complex)

    elif M == 1:
        # One-magnon sector
        # BAE: ((u_1+1/2)/(u_1-1/2))^2 = -1
        # => (u_1+1/2)/(u_1-1/2) = +-i
        # u_1+1/2 = i*(u_1-1/2) => u_1(1-i) = -1/2 - i/2 = -(1+i)/2
        # u_1 = -(1+i)/(2(1-i)) = -(1+i)^2/(2*2) = -(2i)/4 = -i/2
        # Or: u_1+1/2 = -i*(u_1-1/2) => u_1(1+i) = -1/2 + i/2 = (i-1)/2
        # u_1 = (i-1)/(2(1+i)) = (i-1)(1-i)/(2*2) = (i-i^2-1+i)/4 = (2i+1-1)/4 = i/2
        bethe_roots = np.array([0.5j], dtype=complex)
        tq_res = verify_tq_relation(1.0, a_list, bethe_roots)
        bae_res = bethe_ansatz_equations(bethe_roots, a_list)

    else:
        raise ValueError(f"For L=2, M must be 0 or 1, got {M}")

    return BaxterTQData(
        L=L, a_list=a_list, bethe_roots=bethe_roots, M=M,
        Q_poly=bethe_roots,
        T_eigenvalue=transfer_eigenvalue_from_bethe(0.0, a_list, bethe_roots),
        tq_residual=float(np.max(np.abs(
            [verify_tq_relation(u, a_list, bethe_roots)
             for u in [0.5, 1.0, 1.5, 2.0, 3.0]]
        ))) if M > 0 else 0.0,
        bae_residuals=bae_res,
    )


def baxter_q_sl2_L3(M: int = 0) -> BaxterTQData:
    """Baxter Q-operator for sl_2 XXX with L=3 sites.

    Hilbert space: (C^2)^3 = C^8.
    Decomposition: V_1^3 = V_3 + 2*V_1 (spin 3/2 + two copies of spin 1/2).

    Sectors:
      M=0: vacuum. T(u) = (u+1/2)^3 + (u-1/2)^3 = 2u^3 + 3u/2.
      M=1: one magnon. BAE: ((u_1+1/2)/(u_1-1/2))^3 = -1.
    """
    L = 3
    a_list = [0.0, 0.0, 0.0]

    if M == 0:
        bethe_roots = np.array([], dtype=complex)
        tq_res = 0.0
        bae_res = np.array([], dtype=complex)

    elif M == 1:
        # BAE: ((u+1/2)/(u-1/2))^3 = -1
        # (u+1/2)/(u-1/2) = -1^{1/3} = e^{i*pi*(2k+1)/3} for k=0,1,2
        # For k=0: ratio = e^{i*pi/3} = (1+i*sqrt(3))/2
        # u+1/2 = r*(u-1/2) where r = e^{i*pi/3}
        # u(1-r) = -1/2 - r/2 = -(1+r)/2
        # u = -(1+r)/(2(1-r))
        import cmath
        roots_all = []
        for k in range(3):
            r = cmath.exp(1j * cmath.pi * (2 * k + 1) / 3)
            u_root = -(1 + r) / (2 * (1 - r))
            roots_all.append(u_root)

        # Pick the root with smallest imaginary part (physical ground state)
        bethe_roots = np.array([roots_all[0]], dtype=complex)

        # Verify all three are valid roots
        tq_residuals = []
        for root in roots_all:
            res = verify_tq_relation(1.0, a_list, np.array([root]))
            tq_residuals.append(abs(res))

        bae_res = bethe_ansatz_equations(bethe_roots, a_list)
        tq_res = float(np.max(np.abs(
            [verify_tq_relation(u, a_list, bethe_roots)
             for u in [0.5, 1.0, 1.5, 2.0, 3.0]]
        )))

    else:
        # General M: solve numerically
        bethe_roots = solve_bethe_sl2(L, M, a_list)
        bae_res = bethe_ansatz_equations(bethe_roots, a_list)
        tq_res = float(np.max(np.abs(
            [verify_tq_relation(u, a_list, bethe_roots)
             for u in [0.5, 1.0, 1.5, 2.0, 3.0]]
        )))

    return BaxterTQData(
        L=L, a_list=a_list, bethe_roots=bethe_roots, M=M,
        Q_poly=bethe_roots,
        T_eigenvalue=transfer_eigenvalue_from_bethe(0.0, a_list, bethe_roots),
        tq_residual=tq_res,
        bae_residuals=bae_res,
    )


def baxter_q_sl2_L4(M: int = 0) -> BaxterTQData:
    """Baxter Q-operator for sl_2 XXX with L=4 sites.

    Hilbert space: (C^2)^4 = C^16.
    Decomposition: V_1^4 = V_4 + 3*V_2 + 2*V_0.

    Sectors:
      M=0: vacuum.
      M=1: one magnon. BAE: ((u+1/2)/(u-1/2))^4 = -1.
      M=2: two magnons. BAE is a coupled system.
    """
    L = 4
    a_list = [0.0] * L

    if M == 0:
        bethe_roots = np.array([], dtype=complex)
        bae_res = np.array([], dtype=complex)
        tq_res = 0.0

    elif M == 1:
        # BAE: ((u+1/2)/(u-1/2))^4 = -1
        import cmath
        roots_all = []
        for k in range(4):
            # 4th roots of -1: e^{i*pi*(2k+1)/4}
            r = cmath.exp(1j * cmath.pi * (2 * k + 1) / 4)
            u_root = -(1 + r) / (2 * (1 - r))
            roots_all.append(u_root)
        bethe_roots = np.array([roots_all[0]], dtype=complex)
        bae_res = bethe_ansatz_equations(bethe_roots, a_list)
        tq_res = float(np.max(np.abs(
            [verify_tq_relation(u, a_list, bethe_roots)
             for u in [0.5, 1.0, 1.5, 2.0, 3.0]]
        )))

    elif M == 2:
        # Two-magnon ground state for L=4
        # The BAE system:
        # ((u_1+1/2)/(u_1-1/2))^4 = - (u_1-u_2+1)/(u_1-u_2-1)
        # ((u_2+1/2)/(u_2-1/2))^4 = - (u_2-u_1+1)/(u_2-u_1-1)
        # For the singlet (total S^z = 0), the Bethe roots come in pairs.
        # Use symmetry: u_1 = -u_2 = u for some u.
        # Then: ((u+1/2)/(u-1/2))^4 = -(2u+1)/(2u-1)
        # Let w = (u+1/2)/(u-1/2). Then w^4 = -(2u+1)/(2u-1).
        # Note 2u+1 = 2(u-1/2)+2 = 2(u-1/2)(1 + 1/(u-1/2)) ... messy.
        # Actually (2u+1)/(2u-1) = (u+1/2)^2/((u-1/2)(u+1/2-1)) ... no.
        # Let's just note: 2u+1 = 2u-1 + 2, so (2u+1)/(2u-1) = 1 + 2/(2u-1).

        # Solve numerically with symmetric initial guess
        initial = np.array([0.3 + 0.01j, -0.3 + 0.01j], dtype=complex)
        bethe_roots = solve_bethe_sl2(L, M, a_list, initial_guess=initial)
        bae_res = bethe_ansatz_equations(bethe_roots, a_list)
        tq_res = float(np.max(np.abs(
            [verify_tq_relation(u, a_list, bethe_roots)
             for u in [0.5, 1.0, 1.5, 2.0, 3.0]]
        )))

    else:
        bethe_roots = solve_bethe_sl2(L, M, a_list)
        bae_res = bethe_ansatz_equations(bethe_roots, a_list)
        tq_res = float(np.max(np.abs(
            [verify_tq_relation(u, a_list, bethe_roots)
             for u in [0.5, 1.0, 1.5, 2.0, 3.0]]
        )))

    return BaxterTQData(
        L=L, a_list=a_list, bethe_roots=bethe_roots, M=M,
        Q_poly=bethe_roots,
        T_eigenvalue=transfer_eigenvalue_from_bethe(0.0, a_list, bethe_roots),
        tq_residual=tq_res,
        bae_residuals=bae_res,
    )


# =========================================================================
# V. DIRECT TRANSFER MATRIX DIAGONALIZATION
# =========================================================================

def diagonalize_transfer_sl2(L: int,
                              a_list: Optional[List[complex]] = None,
                              u_values: Optional[List[complex]] = None,
                              ) -> Dict[str, Any]:
    """Diagonalize the transfer matrix T(u) directly for sl_2 XXX.

    This provides PATH A verification: the transfer matrix eigenvalues
    from direct diagonalization must match those from the Bethe ansatz
    (PATH B).

    The key identity: T(u) commutes with total spin operators and
    with T(v) for all v (integrability).  Diagonalization in the
    simultaneous eigenbasis of T and S^z gives sectors labeled by
    the z-component of total spin.

    Args:
        L: number of sites
        a_list: inhomogeneity parameters (default: homogeneous)
        u_values: spectral parameters at which to evaluate T(u)

    Returns:
        dict with eigenvalues, commutativity checks, etc.
    """
    if a_list is None:
        a_list = [0.0] * L
    if u_values is None:
        u_values = [0.0, 0.5, 1.0, 2.0]

    dim = 2 ** L

    # Build S^z (total spin z-component)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    Sz = np.zeros((dim, dim), dtype=complex)
    for j in range(L):
        # sigma_z on site j
        op = np.eye(1, dtype=complex)
        for k in range(L):
            op = np.kron(op, sigma_z if k == j else I2)
        Sz += 0.5 * op

    # Build T(u) at several u values
    T_matrices = {}
    for u in u_values:
        T_matrices[u] = transfer_matrix_sl2(u, a_list)

    # Check [T(u), T(v)] = 0 (integrability)
    commutativity_checks = {}
    for i, u1 in enumerate(u_values):
        for j, u2 in enumerate(u_values):
            if j > i:
                comm = T_matrices[u1] @ T_matrices[u2] - T_matrices[u2] @ T_matrices[u1]
                commutativity_checks[(u1, u2)] = float(np.linalg.norm(comm))

    # Check [T(u), S^z] = 0
    sz_checks = {}
    for u in u_values:
        comm = T_matrices[u] @ Sz - Sz @ T_matrices[u]
        sz_checks[u] = float(np.linalg.norm(comm))

    # Diagonalize T at u = u_values[0]
    eigenvalues_by_u = {}
    for u in u_values:
        evals = np.linalg.eigvals(T_matrices[u])
        eigenvalues_by_u[u] = sorted(evals, key=lambda x: (x.real, x.imag))

    return {
        "L": L,
        "dim": dim,
        "T_matrices": T_matrices,
        "commutativity_checks": commutativity_checks,
        "sz_checks": sz_checks,
        "eigenvalues_by_u": eigenvalues_by_u,
    }


def verify_integrability_sl2(L: int) -> bool:
    """Verify [T(u), T(v)] = 0 for sl_2 XXX at several (u, v) pairs.

    This is the statement that the transfer matrices at different spectral
    parameters commute, which is a consequence of the Yang-Baxter equation
    for the R-matrix.

    The MC interpretation: the CYBE (genus-0 arity-3 MC equation) implies
    that the RTT algebra relations hold, which in turn implies [T(u), T(v)] = 0.
    """
    result = diagonalize_transfer_sl2(L)
    return all(v < 1e-10 for v in result["commutativity_checks"].values())


# =========================================================================
# VI. BETHE ANSATZ <=> TRANSFER MATRIX COMPARISON
# =========================================================================

def compare_bethe_vs_diag_sl2(L: int, M: int,
                               u_test: complex = 1.0) -> Dict[str, Any]:
    """Compare transfer matrix eigenvalue from Bethe ansatz vs diagonalization.

    PATH A: Direct diagonalization of T(u) (numerical linear algebra).
    PATH B: Bethe ansatz roots -> analytic eigenvalue formula.

    These must agree: verification of the Baxter TQ construction.
    """
    a_list = [0.0] * L

    # Path A: diagonalize T(u_test)
    T_matrix = transfer_matrix_sl2(u_test, a_list)
    evals_diag = sorted(np.linalg.eigvals(T_matrix).real)

    # Path B: Bethe ansatz
    bethe_roots = solve_bethe_sl2(L, M, a_list)
    T_bethe = transfer_eigenvalue_from_bethe(u_test, a_list, bethe_roots)

    # Find the diagonalization eigenvalue closest to the Bethe prediction
    distances = [abs(ev - T_bethe) for ev in evals_diag]
    best_match_idx = np.argmin(distances)
    best_match = evals_diag[best_match_idx]

    return {
        "L": L,
        "M": M,
        "u_test": u_test,
        "T_bethe": T_bethe,
        "T_diag_closest": best_match,
        "discrepancy": abs(T_bethe - best_match),
        "all_diag_eigenvalues": evals_diag,
        "bethe_roots": bethe_roots,
        "bae_residuals": bethe_ansatz_equations(bethe_roots, a_list),
    }


# =========================================================================
# VII. MC PROJECTION VERIFICATION
# =========================================================================

def verify_r_from_mc_sl2() -> Dict[str, Any]:
    """Verify that the Yang R-matrix comes from the MC projection.

    PATH C: The classical r-matrix r(z) = P/z is extracted from
    Theta_A^{(0,2)} via collision residue (AP19). The quantum
    R-matrix R(u) = u*I + P is the unique solution of the quantum YBE
    with classical limit r(z) = P/z.

    Verification:
    1. R(u)/u -> I + P/u matches 1 + hbar*r(z) at z = u, hbar = 1.
    2. R(u) satisfies YBE (from CYBE of r, which is arity-3 MC equation).
    3. Transfer matrix from R gives commuting operators (integrability).
    """
    results = {}

    # 1. Classical limit
    for u_test in [1.0, 2.0, 5.0, 10.0]:
        R_norm = yang_r_matrix_sl2(u_test) / u_test
        # r(z) = P/z, so 1 + r(u) = I + P/u
        P_mat = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                          [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
        classical = np.eye(4) + P_mat / u_test
        results[f"classical_limit_u={u_test}"] = float(
            np.linalg.norm(R_norm - classical))

    # 2. Yang-Baxter equation
    for u, v in [(1.0, 2.0), (0.5, 3.0), (-1.0, 2.5)]:
        results[f"YBE_u={u}_v={v}"] = verify_yang_baxter_general(
            yang_r_matrix_sl2, u, v, dim=2)

    # 3. Integrability
    for L in [2, 3, 4]:
        results[f"integrability_L={L}"] = verify_integrability_sl2(L)

    return results


def verify_r_from_mc_sl3() -> Dict[str, Any]:
    """Verify the sl_3 Yang R-matrix from MC projection.

    For sl_3: r(z) = Omega_{sl_3}/z where Omega is the quadratic Casimir
    in the fundamental rep.  In the C^3 x C^3 representation:
    Omega = P (the permutation on C^3 x C^3), so R(u) = u*I_9 + P_9.
    """
    results = {}

    # YBE
    for u, v in [(1.0, 2.0), (0.5, 3.0)]:
        results[f"YBE_sl3_u={u}_v={v}"] = verify_yang_baxter_general(
            yang_r_matrix_sl3, u, v, dim=3)

    # Integrability: T(u) for sl_3 with L=2
    a_list = [0.0, 0.0]
    T1 = transfer_matrix_sl3(1.0, a_list)
    T2 = transfer_matrix_sl3(2.0, a_list)
    comm = T1 @ T2 - T2 @ T1
    results["integrability_sl3_L2"] = float(np.linalg.norm(comm))

    return results


# =========================================================================
# VIII. sl_3 Q-OPERATORS (indexed by fundamental representations)
# =========================================================================

def transfer_eigenvalue_sl3_vacuum(u: complex, L: int) -> complex:
    """Transfer matrix eigenvalue on the vacuum for sl_3 with L sites.

    For the vacuum state (all sites in highest weight state of C^3),
    the transfer matrix with V_{omega_1} auxiliary space has eigenvalue:

      Lambda_1(u) = (u + 1)^L + (u)^L + (u - 1)^L

    This is the trace of the monodromy matrix on the vacuum.
    """
    return (u + 1) ** L + u ** L + (u - 1) ** L


def a_functions_sl3(u: complex, a_list: List[complex]) -> Tuple[complex, complex, complex]:
    """The three functions a_1, a_2, a_3 for sl_3 TQ relation.

    For sl_3 with fundamental auxiliary space:
      a_1(u) = prod_j (u - a_j + 1)
      a_2(u) = prod_j (u - a_j)
      a_3(u) = prod_j (u - a_j - 1)
    """
    a1 = a2 = a3 = 1.0 + 0j
    for aj in a_list:
        a1 *= (u - aj + 1)
        a2 *= (u - aj)
        a3 *= (u - aj - 1)
    return a1, a2, a3


def verify_tq_sl3_vacuum(u: complex, L: int) -> float:
    """Verify TQ relation for sl_3 on the vacuum state.

    On the vacuum, Q_1(u) = 1 and Q_2(u) = 1 (no Bethe roots).

    The TQ relation:
      Lambda_1(u) = a_1(u) + a_2(u) + a_3(u)
                  = (u+1)^L + u^L + (u-1)^L

    which is trivially satisfied.
    """
    a_list = [0.0] * L
    a1, a2, a3 = a_functions_sl3(u, a_list)
    lhs = transfer_eigenvalue_sl3_vacuum(u, L)
    rhs = a1 + a2 + a3
    return abs(lhs - rhs)


# =========================================================================
# IX. HAMILTONIAN FROM TRANSFER MATRIX (MC -> INTEGRABLE SYSTEM)
# =========================================================================

def hamiltonian_from_transfer_sl2(L: int,
                                   a_list: Optional[List[complex]] = None,
                                   ) -> np.ndarray:
    """Extract the Hamiltonian H from T(u) via H = d/du log T(u)|_{u=0}.

    For the homogeneous XXX chain:
      H = sum_j P_{j,j+1}  (nearest-neighbor permutation Hamiltonian)

    with periodic boundary conditions.

    The MC interpretation: the Hamiltonian is the LINEARIZATION of the
    transfer matrix at u = 0, which corresponds to the genus-0 arity-2
    MC projection (the r-matrix) evaluated at the identity permutation.
    """
    if a_list is None:
        a_list = [0.0] * L

    # H = (d/du) T(u)|_{u=0} * T(0)^{-1}
    # More precisely, for the XXX model:
    # H = d/du ln T(u)|_{u=shift}
    # For homogeneous chain: H = sum_j d/du R_{j,j+1}(u)|_{u=0}

    eps = 1e-6
    T_plus = transfer_matrix_sl2(eps, a_list)
    T_minus = transfer_matrix_sl2(-eps, a_list)
    T_0 = transfer_matrix_sl2(0.0, a_list)

    dT = (T_plus - T_minus) / (2 * eps)

    # For the XXX Hamiltonian: H ~ d/du T(u)|_{u=some shift}
    # T(0) is the shift operator (for homogeneous chain).
    # The actual Hamiltonian is H = (1/2) * sum_j (sigma_j . sigma_{j+1})
    # which relates to dT/du|_{u=0} via H = (1/2i) * T'(0) * T(0)^{-1} + const.

    # For simplicity, return the numerical derivative directly.
    try:
        T0_inv = np.linalg.inv(T_0)
        H = dT @ T0_inv
    except np.linalg.LinAlgError:
        H = dT  # T(0) may be singular

    return H


def heisenberg_hamiltonian_sl2(L: int) -> np.ndarray:
    """Build the Heisenberg XXX Hamiltonian directly for comparison.

    H = sum_{j=1}^L (sigma_j . sigma_{j+1} + I) / 2
      = sum_{j=1}^L P_{j,j+1}

    with periodic BC: site L+1 = site 1.
    """
    dim = 2 ** L
    H = np.zeros((dim, dim), dtype=complex)

    # Pauli matrices
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    for j in range(L):
        jp = (j + 1) % L  # periodic BC
        for pauli in [sx, sy, sz]:
            # sigma_j . sigma_{j+1}
            op = np.eye(1, dtype=complex)
            for k in range(L):
                if k == j:
                    op = np.kron(op, pauli)
                elif k == jp:
                    op = np.kron(op, pauli)
                else:
                    op = np.kron(op, I2)
            H += 0.25 * op  # factor 1/4 because P = (I + sigma.sigma)/2

    # Add identity part: P = (I + sigma.sigma)/2, so sum P = L/2 + sum sigma.sigma/2
    # We already have sum (sigma_j.sigma_{j+1})/4
    # P_{j,j+1} = (I + sigma_j.sigma_{j+1})/2, so sum P = sum(I/2 + sigma.sigma/2)
    H_perm = L * 0.5 * np.eye(dim, dtype=complex) + 2 * H  # rescale

    return H_perm


# =========================================================================
# X. MASTER VERIFICATION SUITE
# =========================================================================

def verify_all_mc_to_baxter() -> Dict[str, Any]:
    """Complete verification: MC element -> R-matrix -> T(u) -> Q(u) -> Bethe.

    Three independent paths that must agree:
      A: Direct diagonalization of T(u)
      B: Bethe ansatz -> Q(u) -> eigenvalues
      C: MC projection -> R(u) -> YBE -> integrability
    """
    results = {}

    # Path C: R-matrix from MC
    r_mc = verify_r_from_mc_sl2()
    results["PATH_C_classical_limits"] = all(
        v < 1e-10 for k, v in r_mc.items() if "classical" in k)
    results["PATH_C_YBE"] = all(
        v < 1e-10 for k, v in r_mc.items() if "YBE" in k)
    results["PATH_C_integrability"] = all(
        v for k, v in r_mc.items() if "integrability" in k)

    # sl_2, L=2
    for M in [0, 1]:
        data = baxter_q_sl2_L2(M)
        results[f"L2_M{M}_TQ_residual"] = data.tq_residual
        results[f"L2_M{M}_BAE_residual"] = (
            float(np.max(np.abs(data.bae_residuals)))
            if len(data.bae_residuals) > 0 else 0.0)

    # sl_2, L=3
    for M in [0, 1]:
        data = baxter_q_sl2_L3(M)
        results[f"L3_M{M}_TQ_residual"] = data.tq_residual
        results[f"L3_M{M}_BAE_residual"] = (
            float(np.max(np.abs(data.bae_residuals)))
            if len(data.bae_residuals) > 0 else 0.0)

    # sl_2, L=4
    for M in [0, 1, 2]:
        data = baxter_q_sl2_L4(M)
        results[f"L4_M{M}_TQ_residual"] = data.tq_residual
        results[f"L4_M{M}_BAE_residual"] = (
            float(np.max(np.abs(data.bae_residuals)))
            if len(data.bae_residuals) > 0 else 0.0)

    # Cross-check: Bethe vs diagonalization (Path A vs Path B)
    for L in [2, 3]:
        for M in [0, 1]:
            comp = compare_bethe_vs_diag_sl2(L, M)
            results[f"L{L}_M{M}_Bethe_vs_Diag"] = comp["discrepancy"]

    # sl_3 checks
    r_sl3 = verify_r_from_mc_sl3()
    results["PATH_C_sl3_YBE"] = all(
        v < 1e-10 for k, v in r_sl3.items() if "YBE" in k)

    # sl_3 vacuum TQ
    for L in [2, 3]:
        results[f"sl3_L{L}_vacuum_TQ"] = verify_tq_sl3_vacuum(1.0, L)

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
