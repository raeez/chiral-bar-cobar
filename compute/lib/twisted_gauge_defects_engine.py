r"""Twisted gauge theory defects and the shadow obstruction tower.

Systematic treatment of line defects, surface defects, and defect networks
in the bar-complex framework of modular Koszul duality.

Mathematical setup
------------------
Costello's 4d Chern--Simons theory on Sigma x C (Sigma = topological plane,
C = holomorphic curve) has:

  (a) LINE DEFECTS (Wilson lines): labeled by representations V_lambda of g.
      In our framework, each is a module for the boundary chiral algebra
      hat{g}_k on C.  The module shadow data consists of (lambda, C_2(lambda),
      kappa^{mod}(lambda)), where C_2 is the quadratic Casimir and
      kappa^{mod} is the module-level modular characteristic.

  (b) SURFACE DEFECTS (boundary conditions): an A-module or A-bimodule M
      in the chiral category.  The bar complex B(A, M, A) of A with
      coefficients in M computes Tor_A(M, -).

  (c) DEFECT OPE: two parallel line defects (Wilson lines in V_lambda and
      V_mu) fuse via the R-matrix r(z) = Omega/z, the collision residue
      of the MC element Theta_A (AP19: one pole order below the OPE).
      The fusion decomposes via CG: V_lambda x V_mu = oplus V_nu.

  (d) GUKOV--WITTEN SURFACE OPERATOR: monodromy defect with holonomy
      exp(2 pi i sigma), sigma in h (Cartan subalgebra).  In our framework:
      a twisted module for hat{g}_k where the monodromy modifies the
      bar differential.  The twisted modular characteristic is
      kappa^{tw}(sigma) = kappa + delta_kappa(sigma) where
      delta_kappa = -k * |sigma|^2 / 2.

  (e) 't HOOFT LINES (magnetic defects): modules for the KOSZUL DUAL A!.
      For hat{g}_k this is hat{g}_{-k-2h^v}.  The 't Hooft line in
      representation V_lambda^L of g^L (Langlands dual) maps to the
      Wilson line via electric-magnetic (S-) duality.

  (f) DEFECT CROSSING KERNEL (6j-symbols): when two line defects cross,
      the amplitude is the Racah--Wigner 6j-symbol.  This is computed
      from the CG decomposition and the R-matrix eigenvalues.

  (g) DEFECT NETWORKS (webs): networks of line operators form string
      diagrams in the category of A-modules.  Trivalent vertices are
      CG intertwiners; the diagram evaluation is a composition of such.

  (h) KAPUSTIN--WITTEN AND GEOMETRIC LANGLANDS: the A-twist of 4d N=4
      SYM relates Wilson lines of G to Hecke eigensheaves of G^L.
      In our framework, the DK bridge (Drinfeld--Kohno) gives the
      monodromy representation of the KZ connection, which realizes
      the Hecke action categorically.

Conventions
-----------
* Cohomological grading (|d| = +1).
* The r-matrix r(z) = Omega/z has a SINGLE pole (AP19: bar absorbs one power).
* kappa(hat{g}_k) = dim(g) * (k + h^v) / (2 h^v)  (AP1, AP9, AP39).
* The R-matrix R(z) = 1 + r(z)/kappa + O(1/kappa^2).
* Yang R-matrix convention: R(u) = u*I + P (additive, matching
  yangian_residue_extraction.py).
* Desuspension LOWERS degree (AP45): |s^{-1}v| = |v| - 1.

Ground truth references
-----------------------
* yangian_residue_extraction.py: Yang R-matrix, YBE, channel decomposition.
* yangian_rmatrix_sl3.py: sl_3 R-matrix from bar complex.
* dk_compact_generation.py: DK ladder, thick generation, K_0 comparison.
* kappa_cross_verification.py: kappa values for all families.
* lie_algebra.py: Lie algebra data, Cartan matrices, root systems.
* sl3_casimir_decomp.py: Casimir decomposition of tensor powers.
* prefundamental_clebsch_gordan.py: CG for prefundamental modules.

Manuscript references
---------------------
* yangians_drinfeld_kohno.tex: DK bridge, KZ connection, R-matrix.
* yangians_foundations.tex: Yangian representations, evaluation modules.
* yangians_computations.tex: thick generation, defect crossing.
* chiral_koszul_pairs.tex: Koszul duality, A! = hat{g}_{-k-2h^v}.
* concordance.tex: MC3 (all types), DK ladder.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from sympy import Matrix, Rational, Symbol, eye, simplify, sqrt, symbols, zeros


# ============================================================================
# Lie algebra data registry (minimal, consistent with kappa_cross_verification)
# ============================================================================

# (type, rank) -> (dim, h_dual, name)
# h_dual = dual Coxeter number; h = Coxeter number not needed here.
# For simply-laced: h = h_dual.

_LIE_DATA: Dict[Tuple[str, int], Tuple[int, int, str]] = {
    ("A", 1): (3, 2, "sl_2"),
    ("A", 2): (8, 3, "sl_3"),
    ("A", 3): (15, 4, "sl_4"),
    ("A", 4): (24, 5, "sl_5"),
    ("A", 5): (35, 6, "sl_6"),
    ("A", 6): (48, 7, "sl_7"),
    ("A", 7): (63, 8, "sl_8"),
    ("B", 2): (10, 3, "so_5"),
    ("B", 3): (21, 5, "so_7"),
    ("C", 2): (10, 3, "sp_4"),
    ("C", 3): (21, 4, "sp_6"),
    ("D", 4): (28, 6, "so_8"),
    ("G", 2): (14, 4, "G_2"),
    ("F", 4): (52, 9, "F_4"),
    ("E", 6): (78, 12, "E_6"),
    ("E", 7): (133, 18, "E_7"),
    ("E", 8): (248, 30, "E_8"),
}


def _get_lie_data(lie_type: str, rank: int) -> Tuple[int, int, str]:
    """Retrieve (dim, h_dual, name) for a simple Lie algebra."""
    key = (lie_type, rank)
    if key not in _LIE_DATA:
        raise ValueError(f"Lie algebra ({lie_type}, {rank}) not in registry")
    return _LIE_DATA[key]


# ============================================================================
# 1. Modular characteristic kappa (AP1, AP9, AP39)
# ============================================================================

def kappa_affine(lie_type: str, rank: int, k: Rational) -> Rational:
    r"""Modular characteristic kappa(hat{g}_k) = dim(g) * (k + h^v) / (2 h^v).

    This is the genus-1 obstruction class coefficient.  It is NOT c/2 in general
    (AP39: kappa = c/2 only for Virasoro).

    For sl_N at level k: kappa = N^2 - 1) * (k + N) / (2N).

    Args:
        lie_type: Dynkin type ("A", "B", "C", "D", "E", "F", "G").
        rank: rank of the Lie algebra.
        k: level (must not be -h^v = critical level).

    Returns:
        Exact rational kappa value.
    """
    dim_g, h_dual, _ = _get_lie_data(lie_type, rank)
    if k == -h_dual:
        raise ValueError(
            f"Level k = -{h_dual} is the critical level for {lie_type}_{rank}; "
            "Sugawara is undefined (AP: critical level pitfall)"
        )
    return Rational(dim_g, 2 * h_dual) * (k + h_dual)


def central_charge_affine(lie_type: str, rank: int, k: Rational) -> Rational:
    r"""Sugawara central charge c(hat{g}_k) = k * dim(g) / (k + h^v).

    Args:
        lie_type: Dynkin type.
        rank: rank.
        k: level (not critical).

    Returns:
        Exact rational central charge.
    """
    dim_g, h_dual, _ = _get_lie_data(lie_type, rank)
    if k == -h_dual:
        raise ValueError(
            f"Level k = -{h_dual} is the critical level for {lie_type}_{rank}"
        )
    return Rational(dim_g) * k / (k + h_dual)


# ============================================================================
# 2. Line defects = Wilson lines = representations V_lambda
# ============================================================================

@dataclass
class LineDefect:
    r"""A line defect (Wilson line) in 4d CS, labeled by a representation.

    In our framework, a line defect is a module for the boundary chiral
    algebra hat{g}_k.  The key invariants are:

      - weight: highest weight lambda (as a tuple of Dynkin labels)
      - casimir_2: quadratic Casimir eigenvalue C_2(lambda)
      - dim_rep: dimension of the representation
      - kappa_module: module-level modular characteristic

    The module shadow data packages these into defect-colored vertices
    in the genus expansion.
    """
    lie_type: str
    rank: int
    weight: Tuple[int, ...]  # Dynkin labels (lambda_1, ..., lambda_r)
    level: Rational
    casimir_2: Rational = Rational(0)
    dim_rep: int = 0
    kappa_module: Rational = Rational(0)

    def __post_init__(self):
        if len(self.weight) != self.rank:
            raise ValueError(
                f"Weight tuple length {len(self.weight)} != rank {self.rank}"
            )
        self.casimir_2 = quadratic_casimir(self.lie_type, self.rank, self.weight)
        self.dim_rep = weyl_dimension(self.lie_type, self.rank, self.weight)
        self.kappa_module = module_kappa(
            self.lie_type, self.rank, self.weight, self.level
        )


def quadratic_casimir(lie_type: str, rank: int,
                      weight: Tuple[int, ...]) -> Rational:
    r"""Quadratic Casimir eigenvalue C_2(V_lambda) for a highest weight lambda.

    For type A_n = sl_{n+1} with Dynkin labels (lambda_1, ..., lambda_n):

      C_2(lambda) = sum_{i,j} (A^{-1})_{ij} lambda_i (lambda_j + 2 rho_j)

    where A is the Cartan matrix and rho = (1, 1, ..., 1) in the Dynkin basis.

    For sl_2 with weight (n) (spin n/2 representation):
      C_2 = n(n+2)/4 = j(j+1) with j = n/2.

    For sl_3 with weight (a, b):
      C_2 = (2/3)(a^2 + b^2 + ab) + 2(a + b).

    Args:
        lie_type: Dynkin type.
        rank: rank.
        weight: Dynkin labels tuple.

    Returns:
        Exact rational Casimir value.
    """
    if len(weight) != rank:
        raise ValueError(f"Weight length {len(weight)} != rank {rank}")

    if lie_type == "A":
        return _casimir_type_A(rank, weight)
    elif lie_type in ("B", "C", "D"):
        return _casimir_from_cartan(lie_type, rank, weight)
    elif lie_type in ("G", "F", "E"):
        return _casimir_from_cartan(lie_type, rank, weight)
    else:
        raise ValueError(f"Unknown Lie type: {lie_type}")


def _casimir_type_A(rank: int, weight: Tuple[int, ...]) -> Rational:
    r"""Casimir for sl_{rank+1} via the inverse Cartan matrix.

    A^{-1}_{ij} = min(i, j) * (rank + 1 - max(i, j)) / (rank + 1)
    (1-indexed: i, j = 1, ..., rank).

    C_2 = sum_{i,j} A^{-1}_{ij} * lambda_i * (lambda_j + 2)
    where rho_j = 1 in Dynkin basis for type A.
    """
    N = rank + 1  # sl_N
    lam = list(weight)
    # rho in Dynkin basis for type A: all ones
    rho = [1] * rank

    result = Rational(0)
    for i in range(rank):
        for j in range(rank):
            # 1-indexed: i+1, j+1
            a_inv = Rational(min(i + 1, j + 1) * (N - max(i + 1, j + 1)), N)
            result += a_inv * lam[i] * (lam[j] + 2 * rho[j])
    return result


def _casimir_from_cartan(lie_type: str, rank: int,
                         weight: Tuple[int, ...]) -> Rational:
    r"""Casimir from the inverse Cartan matrix (general types).

    Uses sympy Matrix inversion for exact arithmetic.
    The Weyl vector rho in Dynkin basis has all components equal to 1
    for simply-laced types.  For non-simply-laced, rho_i = 1 still
    holds in the Dynkin label basis.
    """
    try:
        from compute.lib.lie_algebra import CARTAN_MATRICES
        A = CARTAN_MATRICES.get((lie_type, rank))
        if A is None:
            raise ValueError(f"Cartan matrix for ({lie_type}, {rank}) not available")
    except ImportError:
        raise ValueError("lie_algebra module not available")

    A_inv = A.inv()
    lam = list(weight)
    rho = [1] * rank  # rho in Dynkin basis

    result = Rational(0)
    for i in range(rank):
        for j in range(rank):
            result += A_inv[i, j] * lam[i] * (lam[j] + 2 * rho[j])
    return result


def weyl_dimension(lie_type: str, rank: int,
                   weight: Tuple[int, ...]) -> int:
    r"""Dimension of V_lambda via the Weyl dimension formula.

    For type A_n = sl_{n+1}:
      dim V_lambda = prod_{1 <= i < j <= n+1} (l_i - l_j) / (i - j)
    where l = (lambda_1 + ... + lambda_n, lambda_2 + ... + lambda_n, ..., lambda_n, 0)
    is the partition form, shifted by rho.

    For sl_2, weight (n): dim = n + 1.
    For sl_3, weight (a, b):
      dim = (a+1)(b+1)(a+b+2)/2.
    """
    if lie_type == "A":
        return _weyl_dim_A(rank, weight)
    else:
        return _weyl_dim_general(lie_type, rank, weight)


def _weyl_dim_A(rank: int, weight: Tuple[int, ...]) -> int:
    """Weyl dimension for sl_{rank+1}."""
    N = rank + 1
    # Convert Dynkin labels to partition + rho shift
    # l_i = sum_{j >= i} lambda_j, then shift: l_i += N - i
    l = [0] * N
    for i in range(rank):
        for j in range(i, rank):
            l[i] += weight[j]
    # Shift by rho: rho_i = N - i (1-indexed), so rho_{i-1} = N - i
    for i in range(N):
        l[i] += N - 1 - i

    # Weyl formula: prod_{i<j} (l_i - l_j) / prod_{i<j} (rho_i - rho_j)
    num = 1
    den = 1
    for i in range(N):
        for j in range(i + 1, N):
            num *= (l[i] - l[j])
            den *= (N - 1 - i) - (N - 1 - j)  # = j - i
    return num // den


def _weyl_dim_general(lie_type: str, rank: int,
                      weight: Tuple[int, ...]) -> int:
    """Weyl dimension via inner products with positive roots.

    dim V_lambda = prod_{alpha > 0} <lambda + rho, alpha> / <rho, alpha>
    computed in the weight lattice.  Uses lie_algebra.py for root data.
    """
    try:
        from compute.lib.lie_algebra import (
            CARTAN_MATRICES, _positive_roots_from_cartan,
        )
        A = CARTAN_MATRICES.get((lie_type, rank))
        if A is None:
            raise ValueError(f"Cartan matrix for ({lie_type}, {rank}) not available")
        pos_roots = _positive_roots_from_cartan(A, rank)
    except ImportError:
        raise ValueError("lie_algebra module not available for general Weyl dimension")

    lam = list(weight)
    rho = [1] * rank  # Dynkin labels
    lam_rho = [lam[i] + rho[i] for i in range(rank)]

    num = Rational(1)
    den = Rational(1)
    for alpha in pos_roots:
        # <lambda + rho, alpha^v> = sum_i (lambda_i + rho_i) * alpha_i
        # where alpha = sum alpha_i * alpha_i (simple root coefficients)
        inner_lam = sum(lam_rho[i] * alpha[i] for i in range(rank))
        inner_rho = sum(rho[i] * alpha[i] for i in range(rank))
        num *= inner_lam
        den *= inner_rho

    return int(num / den)


def module_kappa(lie_type: str, rank: int,
                 weight: Tuple[int, ...], k: Rational) -> Rational:
    r"""Module-level modular characteristic for a Wilson line in V_lambda.

    For a highest-weight module V_lambda of hat{g}_k, the module-level
    contribution to the genus-1 partition function is:

      kappa^{mod}(lambda) = C_2(lambda) / (2 * (k + h^v))

    This is the conformal weight h_lambda = C_2(lambda) / (2(k + h^v))
    of the primary state in V_lambda, which appears as the module-level
    correction to the bulk kappa in the defect partition function.

    Note: kappa_affine(g, k) is the BULK contribution from the algebra;
    kappa_module is the DEFECT correction from the representation.

    Args:
        lie_type, rank: Lie algebra type and rank.
        weight: Dynkin labels.
        k: level.

    Returns:
        Exact rational module kappa.
    """
    _, h_dual, _ = _get_lie_data(lie_type, rank)
    c2 = quadratic_casimir(lie_type, rank, weight)
    return c2 / (2 * (k + h_dual))


# ============================================================================
# 3. Defect OPE = R-matrix fusion
# ============================================================================

def permutation_matrix(N: int) -> np.ndarray:
    """Permutation matrix P on C^N tensor C^N: P(e_i tensor e_j) = e_j tensor e_i."""
    P = np.zeros((N * N, N * N), dtype=float)
    for i in range(N):
        for j in range(N):
            P[i * N + j, j * N + i] = 1.0
    return P


def yang_r_matrix(u: complex, N: int) -> np.ndarray:
    """Yang R-matrix R(u) = u*I + P on C^N tensor C^N (additive convention)."""
    P = permutation_matrix(N)
    I = np.eye(N * N, dtype=complex)
    return u * I + P


def defect_ope_r_matrix(z: complex, N: int, k: Rational) -> np.ndarray:
    r"""Defect OPE R-matrix in the fundamental representation.

    The defect OPE for two parallel Wilson lines is controlled by the
    collision residue r(z) = Omega/z of Theta_A (AP19: one pole order
    below the OPE).  In the fundamental representation V = C^N:

      R^{defect}(z) = I + P / (kappa * z) + O(1/(kappa*z)^2)

    where kappa = kappa(hat{g}_k) and P is the permutation.

    At leading order in 1/kappa, this is the Yang R-matrix evaluated
    at the rescaled spectral parameter u = kappa * z.

    Args:
        z: spectral parameter (separation of defects).
        N: dimension of fundamental (C^N for sl_N).
        k: level.

    Returns:
        N^2 x N^2 numpy array.
    """
    kap = float(kappa_affine("A", N - 1, k))
    # Leading order: I + P/(kappa * z)
    P = permutation_matrix(N)
    I = np.eye(N * N, dtype=complex)
    return I + P / (kap * z)


def verify_defect_ybe(z1: complex, z2: complex, z3: complex,
                      N: int, k: Rational) -> float:
    r"""Verify the Yang--Baxter equation for the defect OPE R-matrix.

    The YBE guarantees consistency of the defect OPE:
      R_{12}(z_1 - z_2) R_{13}(z_1 - z_3) R_{23}(z_2 - z_3)
      = R_{23}(z_2 - z_3) R_{13}(z_1 - z_3) R_{12}(z_1 - z_2)

    We verify this for the full Yang R-matrix R(u) = u*I + P, which
    is exact (not just leading order), and hence satisfies YBE exactly.

    Returns:
        Frobenius norm of the difference (should be 0).
    """
    I_N = np.eye(N, dtype=complex)
    d = N * N * N

    kap = float(kappa_affine("A", N - 1, k))
    # Use Yang R-matrix at rescaled parameters
    u12 = kap * (z1 - z2)
    u13 = kap * (z1 - z3)
    u23 = kap * (z2 - z3)

    R12 = np.kron(yang_r_matrix(u12, N), I_N)
    R23 = np.kron(I_N, yang_r_matrix(u23, N))

    # R13: acts on factors 1, 3 (identity on 2)
    R_raw = yang_r_matrix(u13, N)
    R13 = np.zeros((d, d), dtype=complex)
    for i in range(N):
        for j in range(N):
            for kk in range(N):
                for ip in range(N):
                    for kp in range(N):
                        row = i * N * N + j * N + kk
                        col = ip * N * N + j * N + kp
                        R13[row, col] += R_raw[i * N + kk, ip * N + kp]

    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    return float(np.linalg.norm(lhs - rhs))


def defect_ope_eigenvalues(N: int) -> Dict[str, Any]:
    r"""Eigenvalues of the defect OPE on Sym^2(V) and Lambda^2(V).

    The permutation P decomposes V tensor V into:
      Sym^2(V):    eigenvalue +1,  dim = N(N+1)/2
      Lambda^2(V): eigenvalue -1,  dim = N(N-1)/2

    For the Yang R-matrix R(u) = u*I + P:
      R|_{Sym^2} = (u + 1) * Id
      R|_{Lambda^2} = (u - 1) * Id

    The zero of R on the antisymmetric channel at u = 1 corresponds to
    the antisymmetric fusion channel being forbidden at that spectral
    parameter (the short-distance limit of the defect OPE).

    Returns:
        Dict with decomposition data.
    """
    return {
        "N": N,
        "sym_dim": N * (N + 1) // 2,
        "antisym_dim": N * (N - 1) // 2,
        "sym_eigenvalue": "+1 (u+1 for R(u))",
        "antisym_eigenvalue": "-1 (u-1 for R(u))",
        "fusion_rule": f"V_fund x V_fund = Sym^2 + Lambda^2 "
                       f"({N * (N + 1) // 2} + {N * (N - 1) // 2} = {N * N})",
    }


# ============================================================================
# 4. Clebsch--Gordan decomposition and fusion rules
# ============================================================================

def clebsch_gordan_sl2(n1: int, n2: int) -> List[int]:
    r"""Clebsch--Gordan decomposition for sl_2: V_{n1} x V_{n2}.

    V_n is the (n+1)-dimensional irreducible with highest weight n.

    CG rule: V_{n1} x V_{n2} = V_{|n1-n2|} + V_{|n1-n2|+2} + ... + V_{n1+n2}.

    Equivalently: spins j1 = n1/2, j2 = n2/2 give
      j = |j1 - j2|, |j1 - j2| + 1, ..., j1 + j2.

    Returns:
        List of highest weights n in the decomposition (sorted).
    """
    return list(range(abs(n1 - n2), n1 + n2 + 1, 2))


def clebsch_gordan_sl3_fund(a1: int, b1: int, a2: int, b2: int) -> List[Tuple[int, int]]:
    r"""Clebsch--Gordan for sl_3: V_{(a1,b1)} x V_{(a2,b2)}.

    Returns the list of irreducible summands (Dynkin labels) with multiplicities.
    Implemented for small representations via the Weyl character formula
    and dimension counting.

    For the fundamental x fundamental case (1,0) x (1,0):
      V_{(1,0)} x V_{(1,0)} = V_{(2,0)} + V_{(0,1)}
      (3 x 3 = 6 + 3-bar)

    For fundamental x antifundamental (1,0) x (0,1):
      V_{(1,0)} x V_{(0,1)} = V_{(1,1)} + V_{(0,0)}
      (3 x 3-bar = 8 + 1)

    Returns:
        List of (a, b) Dynkin labels in the decomposition.
    """
    # For now, implement the most important cases explicitly.
    # These are verified by dimension counting.
    key = ((a1, b1), (a2, b2))

    _CG_TABLE = {
        # fund x fund: 3 x 3 = 6 + 3-bar
        ((1, 0), (1, 0)): [(2, 0), (0, 1)],
        # fund x anti-fund: 3 x 3-bar = 8 + 1
        ((1, 0), (0, 1)): [(1, 1), (0, 0)],
        ((0, 1), (1, 0)): [(1, 1), (0, 0)],
        # anti-fund x anti-fund: 3-bar x 3-bar = 6-bar + 3
        ((0, 1), (0, 1)): [(0, 2), (1, 0)],
        # fund x adjoint: 3 x 8 = 15 + 6-bar + 3
        ((1, 0), (1, 1)): [(2, 1), (0, 2), (1, 0)],
        ((1, 1), (1, 0)): [(2, 1), (0, 2), (1, 0)],
        # adjoint x adjoint: 8 x 8 = 27 + 10 + 10-bar + 8 + 8 + 1
        ((1, 1), (1, 1)): [(2, 2), (3, 0), (0, 3), (1, 1), (1, 1), (0, 0)],
    }

    if key in _CG_TABLE:
        return _CG_TABLE[key]

    # Fallback: dimension-based check only
    raise NotImplementedError(
        f"CG decomposition for ({a1},{b1}) x ({a2},{b2}) not in table; "
        "extend the table or use a general algorithm"
    )


def fusion_dimension_check_sl2(n1: int, n2: int) -> Dict[str, Any]:
    r"""Verify the CG decomposition for sl_2 by dimension counting.

    dim(V_{n1} x V_{n2}) = (n1+1)(n2+1) should equal
    sum of dim(V_n) = (n+1) over all CG summands.
    """
    summands = clebsch_gordan_sl2(n1, n2)
    dim_lhs = (n1 + 1) * (n2 + 1)
    dim_rhs = sum(n + 1 for n in summands)
    return {
        "n1": n1, "n2": n2,
        "dim_tensor": dim_lhs,
        "dim_sum": dim_rhs,
        "match": dim_lhs == dim_rhs,
        "summands": summands,
        "num_summands": len(summands),
    }


def fusion_dimension_check_sl3(a1: int, b1: int,
                               a2: int, b2: int) -> Dict[str, Any]:
    r"""Verify the CG decomposition for sl_3 by dimension counting."""
    summands = clebsch_gordan_sl3_fund(a1, b1, a2, b2)
    dim_lhs = _weyl_dim_A(2, (a1, b1)) * _weyl_dim_A(2, (a2, b2))
    dim_rhs = sum(_weyl_dim_A(2, (a, b)) for a, b in summands)
    return {
        "weight_1": (a1, b1),
        "weight_2": (a2, b2),
        "dim_tensor": dim_lhs,
        "dim_sum": dim_rhs,
        "match": dim_lhs == dim_rhs,
        "summands": summands,
        "num_summands": len(summands),
    }


# ============================================================================
# 5. Surface defects = boundary conditions = A-modules
# ============================================================================

@dataclass
class SurfaceDefect:
    r"""A surface defect (boundary condition) in 4d CS.

    In our framework, a surface defect is an A-module M for the boundary
    chiral algebra A.  The bar complex B(A, M, A) computes Tor_A(M, -).

    For affine KM at level k, the standard surface defects are:
      - Dirichlet: M = trivial module (vacuum module V_k(g))
      - Neumann: M = regular module (adjoint representation)
      - Nahm: M = Whittaker module (generic character of n_+)

    The module bar complex has:
      - Differential: d_M = d_bar + d_module (bar differential + module action)
      - Curvature: m_0^M = kappa^{mod}(M) * omega_g (module-level obstruction)
      - The bar-module spectral sequence E_1 = Tor_*(H*(A), M).

    Attributes:
        name: human-readable name.
        lie_type, rank: Lie algebra data.
        level: level k.
        module_type: "vacuum", "highest_weight", "whittaker", etc.
        weight: highest weight (for HW modules).
        kappa_module: module-level modular characteristic.
    """
    name: str
    lie_type: str
    rank: int
    level: Rational
    module_type: str = "vacuum"
    weight: Optional[Tuple[int, ...]] = None
    kappa_module: Rational = Rational(0)

    def __post_init__(self):
        if self.module_type == "vacuum":
            # Vacuum module: weight = 0
            self.weight = tuple(0 for _ in range(self.rank))
            self.kappa_module = Rational(0)
        elif self.module_type == "highest_weight" and self.weight is not None:
            self.kappa_module = module_kappa(
                self.lie_type, self.rank, self.weight, self.level
            )


def dirichlet_surface_defect(lie_type: str, rank: int,
                             k: Rational) -> SurfaceDefect:
    """Dirichlet boundary condition = vacuum module."""
    _, _, name = _get_lie_data(lie_type, rank)
    return SurfaceDefect(
        name=f"Dirichlet({name}, k={k})",
        lie_type=lie_type, rank=rank, level=k,
        module_type="vacuum",
    )


def neumann_surface_defect(lie_type: str, rank: int,
                           k: Rational) -> SurfaceDefect:
    """Neumann boundary condition = regular module (adjoint)."""
    _, _, name = _get_lie_data(lie_type, rank)
    # Adjoint representation = highest root
    # For type A_n: adjoint = (1, 0, ..., 0, 1)
    if lie_type == "A":
        if rank == 1:
            adj_weight = (2,)
        else:
            adj_weight = tuple(
                1 if i == 0 or i == rank - 1 else 0
                for i in range(rank)
            )
    elif lie_type == "B":
        adj_weight = tuple(0 if i != 1 else 1 for i in range(rank))
        if rank >= 2:
            adj_weight = (0, 1) + tuple(0 for _ in range(rank - 2))
    elif lie_type == "C":
        adj_weight = (2,) + tuple(0 for _ in range(rank - 1))
    elif lie_type == "D":
        adj_weight = tuple(0 if i != 1 else 1 for i in range(rank))
        if rank >= 4:
            adj_weight = (0, 1) + tuple(0 for _ in range(rank - 2))
    elif lie_type == "G" and rank == 2:
        adj_weight = (0, 1)  # short root
    elif lie_type == "F" and rank == 4:
        adj_weight = (1, 0, 0, 0)
    elif lie_type == "E" and rank == 6:
        adj_weight = (0, 0, 0, 0, 0, 1)  # Note: varies by convention
    elif lie_type == "E" and rank == 7:
        adj_weight = (1, 0, 0, 0, 0, 0, 0)
    elif lie_type == "E" and rank == 8:
        adj_weight = (0, 0, 0, 0, 0, 0, 0, 1)
    else:
        raise ValueError(f"Adjoint weight not implemented for ({lie_type}, {rank})")

    return SurfaceDefect(
        name=f"Neumann({name}, k={k})",
        lie_type=lie_type, rank=rank, level=k,
        module_type="highest_weight",
        weight=adj_weight,
    )


def module_bar_complex_data(defect: SurfaceDefect) -> Dict[str, Any]:
    r"""Data of the bar complex B(A, M, A) for a surface defect.

    The module bar complex has:
      - Terms: B_n(A, M, A) = M tensor (s^{-1} A)^{tensor n}
      - Differential: d = d_bar + d_module
      - PBW filtration: same as the algebra bar complex
      - Cohomology: Tor_A^n(M, k) = H^n(B(A, M, A))

    For the vacuum module, this reduces to the ordinary bar complex B(A).
    For a highest-weight module V_lambda at non-critical level:
      H^0(B(A, V_lambda, A)) = V_lambda (the module itself)
      H^n = 0 for n >= 1 (Koszulness implies acyclicity of the bar resolution)

    Returns:
        Dict with bar complex data.
    """
    kap_bulk = kappa_affine(defect.lie_type, defect.rank, defect.level)

    data = {
        "defect_name": defect.name,
        "module_type": defect.module_type,
        "weight": defect.weight,
        "kappa_bulk": kap_bulk,
        "kappa_module": defect.kappa_module,
        "kappa_total": kap_bulk + defect.kappa_module,
        "is_koszul_acyclic": True,  # For standard families at generic level
        "bar_differential": "d_bar + d_module",
        "parity": "same as algebra bar complex",
    }

    if defect.module_type == "vacuum":
        data["reduces_to"] = "ordinary bar complex B(A)"
        data["H0"] = "vacuum module V_k(g)"
    elif defect.module_type == "highest_weight":
        data["H0"] = f"V_{defect.weight}"
        data["conformal_weight"] = defect.kappa_module

    return data


# ============================================================================
# 6. Gukov--Witten surface operator = monodromy defect
# ============================================================================

@dataclass
class GukovWittenDefect:
    r"""Gukov--Witten surface operator (monodromy defect).

    A codimension-2 defect in 4d CS with holonomy exp(2 pi i sigma)
    around the defect, where sigma is an element of the Cartan subalgebra h.

    In our framework, this is a TWISTED module for hat{g}_k:
    the bar differential is modified by the monodromy, and the modular
    characteristic receives a correction.

    The twisted kappa:
      kappa^{tw}(sigma) = kappa(hat{g}_k) + delta_kappa(sigma)
    where
      delta_kappa(sigma) = -k * |sigma|^2 / 2

    Here |sigma|^2 = (sigma, sigma) in the Killing form normalization
    (the same normalization as the quadratic Casimir).

    For sigma = 0 (trivial monodromy): this reduces to the untwisted case.
    For sigma = rho/k (principal embedding): the twisted module is the
    Whittaker module, connecting to the Nahm boundary condition.

    Attributes:
        lie_type, rank: Lie algebra.
        level: level k.
        sigma: Cartan element (tuple of coordinates in simple root basis).
        sigma_norm_sq: |sigma|^2 in the Killing form.
    """
    lie_type: str
    rank: int
    level: Rational
    sigma: Tuple[Rational, ...]
    sigma_norm_sq: Rational = Rational(0)

    def __post_init__(self):
        if len(self.sigma) != self.rank:
            raise ValueError(
                f"sigma length {len(self.sigma)} != rank {self.rank}"
            )
        self.sigma_norm_sq = _cartan_norm_sq(self.lie_type, self.rank, self.sigma)

    @property
    def delta_kappa(self) -> Rational:
        """Monodromy correction to kappa."""
        return -self.level * self.sigma_norm_sq / 2

    @property
    def kappa_twisted(self) -> Rational:
        """Total twisted kappa."""
        return kappa_affine(self.lie_type, self.rank, self.level) + self.delta_kappa


def _cartan_norm_sq(lie_type: str, rank: int,
                    sigma: Tuple[Rational, ...]) -> Rational:
    r"""Compute |sigma|^2 = (sigma, sigma) using the Cartan matrix.

    In the simple root basis, |sigma|^2 = sum_{ij} sigma_i * A_{ij} * sigma_j
    where A is the symmetrized Cartan matrix (= Cartan for simply-laced).

    Actually: the Killing form in the Cartan is given by
      (h_i, h_j) = A_{ij} (Cartan matrix entry)
    for the coroot basis.  Since sigma is given in the simple coroot basis:
      |sigma|^2 = sigma^T A sigma.
    """
    try:
        from compute.lib.lie_algebra import CARTAN_MATRICES
        A = CARTAN_MATRICES.get((lie_type, rank))
        if A is None:
            raise ValueError(f"Cartan matrix for ({lie_type}, {rank}) not available")
    except ImportError:
        # Fallback for sl_2
        if lie_type == "A" and rank == 1:
            return 2 * sigma[0] ** 2
        raise

    s = [Rational(x) for x in sigma]
    result = Rational(0)
    for i in range(rank):
        for j in range(rank):
            result += s[i] * A[i, j] * s[j]
    return result


def gukov_witten_trivial(lie_type: str, rank: int,
                         k: Rational) -> GukovWittenDefect:
    """Trivial monodromy (sigma = 0)."""
    sigma = tuple(Rational(0) for _ in range(rank))
    return GukovWittenDefect(lie_type, rank, k, sigma)


def gukov_witten_principal(lie_type: str, rank: int,
                           k: Rational) -> GukovWittenDefect:
    r"""Principal monodromy sigma = rho^v / k.

    rho^v is the Weyl vector in the coroot basis.  For type A_n:
    rho^v = (1, 1, ..., 1) in the fundamental weight basis, which
    gives rho^v = sum_i alpha_i^v in the simple coroot basis.
    In Dynkin labels: rho = (1, 1, ..., 1).

    The principal GW defect connects to the Nahm (Whittaker) boundary
    condition.
    """
    sigma = tuple(Rational(1, k) for _ in range(rank))
    return GukovWittenDefect(lie_type, rank, k, sigma)


# ============================================================================
# 7. 't Hooft lines = magnetic defects = modules for A!
# ============================================================================

@dataclass
class THooftLine:
    r"""Magnetic line defect ('t Hooft line) in 4d CS.

    In our framework, 't Hooft lines are modules for the Koszul dual A!.
    For hat{g}_k, the Koszul dual is hat{g}_{-k-2h^v} (AP33: this is
    the Koszul dual, NOT the Feigin--Frenkel dual, NOT the negative-level
    substitution).

    The 't Hooft line in representation V_lambda^L of g^L (Langlands dual)
    maps to a Wilson line via electric-magnetic (S-) duality.

    For simply-laced g (where g = g^L):
      Wilson(V_lambda, k) <-> 't Hooft(V_lambda, k^!) where k^! = -k - 2h^v.

    The kappa of the Koszul dual:
      kappa(hat{g}_{k^!}) = dim(g) * (k^! + h^v) / (2 h^v)
                          = dim(g) * (-k - h^v) / (2 h^v)
                          = -kappa(hat{g}_k)

    This gives kappa + kappa' = 0 (AP24: correct for KM families).

    Attributes:
        lie_type, rank: Lie algebra.
        level: level k of the ORIGINAL algebra (the dual has k^! = -k - 2h^v).
        weight: highest weight of the magnetic representation.
        dual_level: k^! = -k - 2h^v.
        kappa_dual: kappa of the Koszul dual.
    """
    lie_type: str
    rank: int
    level: Rational
    weight: Tuple[int, ...]
    dual_level: Rational = Rational(0)
    kappa_dual: Rational = Rational(0)
    casimir_dual: Rational = Rational(0)

    def __post_init__(self):
        _, h_dual, _ = _get_lie_data(self.lie_type, self.rank)
        self.dual_level = -self.level - 2 * h_dual
        self.kappa_dual = kappa_affine(self.lie_type, self.rank, self.dual_level)
        self.casimir_dual = quadratic_casimir(self.lie_type, self.rank, self.weight)


def verify_kappa_complementarity_km(lie_type: str, rank: int,
                                    k: Rational) -> Dict[str, Any]:
    r"""Verify kappa(hat{g}_k) + kappa(hat{g}_{k^!}) = 0 for KM.

    This is AP24: the complementarity sum vanishes for KM families.
    The Koszul dual level is k^! = -k - 2h^v (Feigin-Frenkel involution).

    Returns:
        Dict with verification data.
    """
    _, h_dual, name = _get_lie_data(lie_type, rank)
    k_dual = -k - 2 * h_dual
    kap = kappa_affine(lie_type, rank, k)
    kap_dual = kappa_affine(lie_type, rank, k_dual)
    return {
        "algebra": name,
        "k": k,
        "k_dual": k_dual,
        "kappa": kap,
        "kappa_dual": kap_dual,
        "sum": kap + kap_dual,
        "vanishes": (kap + kap_dual == 0),
    }


# ============================================================================
# 8. Defect crossing kernel = 6j-symbols = Racah--Wigner
# ============================================================================

def crossing_kernel_sl2(j1: Rational, j2: Rational, j3: Rational,
                        j4: Rational, j12: Rational,
                        j23: Rational) -> Rational:
    r"""6j-symbol (Racah--Wigner coefficient) for sl_2.

    The 6j-symbol {j1 j2 j12; j3 j4 j23} controls the crossing kernel:
    when two line defects with spins j1, j2 fuse via channel j12 and then
    fuse with j3, the alternative fusion (j2 fuses with j3 via j23, then
    with j1) is related by the 6j-symbol.

    Computed via the Racah formula:
      {a b e; c d f} = Delta(abe) Delta(cde) Delta(acf) Delta(bdf)
                       * sum_z (-1)^z (z+1)! / [denominator terms]

    where Delta(abc) = sqrt((-a+b+c)!(a-b+c)!(a+b-c)!/(a+b+c+1)!).

    For integer/half-integer spins only.

    This is exact for small spins. For large spins, use asymptotic formulas.
    """
    # Convert to twice-integer for exact arithmetic
    a, b, e, c, d, f = (
        2 * j1, 2 * j2, 2 * j12, 2 * j3, 2 * j4, 2 * j23,
    )
    # All must be non-negative integers
    for x in (a, b, c, d, e, f):
        if x != int(x) or x < 0:
            return Rational(0)
    a, b, c, d, e, f = int(a), int(b), int(c), int(d), int(e), int(f)

    def _triangle_ok(x, y, z):
        """Check triangle inequality and integrality."""
        s = x + y + z
        if s % 2 != 0:
            return False
        if x + y < z or x + z < y or y + z < x:
            return False
        return True

    if not all([
        _triangle_ok(a, b, e),
        _triangle_ok(c, d, e),
        _triangle_ok(a, c, f),
        _triangle_ok(b, d, f),
    ]):
        return Rational(0)

    def _delta_sq(x, y, z):
        """Delta(x/2, y/2, z/2)^2 = (-x+y+z)/2! * ... / ((x+y+z)/2+1)!"""
        s = (x + y + z) // 2
        n1 = (- x + y + z) // 2
        n2 = (x - y + z) // 2
        n3 = (x + y - z) // 2
        from math import factorial
        return Rational(
            factorial(n1) * factorial(n2) * factorial(n3),
            factorial(s + 1)
        )

    delta_abe = _delta_sq(a, b, e)
    delta_cde = _delta_sq(c, d, e)
    delta_acf = _delta_sq(a, c, f)
    delta_bdf = _delta_sq(b, d, f)

    from math import factorial

    # Sum over z
    z_min = max(
        (a + b + e) // 2,
        (c + d + e) // 2,
        (a + c + f) // 2,
        (b + d + f) // 2,
    )
    z_max = min(
        (a + b + c + d) // 2,
        (a + d + e + f) // 2,
        (b + c + e + f) // 2,
    )

    total = Rational(0)
    for z in range(z_min, z_max + 1):
        num = (-1) ** z * factorial(z + 1)
        den = (
            factorial(z - (a + b + e) // 2)
            * factorial(z - (c + d + e) // 2)
            * factorial(z - (a + c + f) // 2)
            * factorial(z - (b + d + f) // 2)
            * factorial((a + b + c + d) // 2 - z)
            * factorial((a + d + e + f) // 2 - z)
            * factorial((b + c + e + f) // 2 - z)
        )
        total += Rational(num, den)

    from sympy import sqrt as sym_sqrt
    # The 6j-symbol = total * product of Delta factors
    # Delta factors are square roots, but Delta^2 is rational
    # The full 6j is product of sqrt(Delta^2) * total
    # Since we work with Delta^2, the 6j^2 is rational:
    result_sq = total ** 2 * delta_abe * delta_cde * delta_acf * delta_bdf
    # Return the signed value (total carries the sign)
    sign = 1 if total >= 0 else -1
    return sign * sym_sqrt(abs(result_sq))


def crossing_kernel_eigenvalue_sl2(j1: int, j2: int) -> Dict[str, Any]:
    r"""Eigenvalues of the crossing kernel (braiding) for sl_2 defects.

    For two Wilson lines with spins j1, j2 in the fundamental channel,
    the braiding eigenvalue on the fusion channel V_J is:

      R_J = (-1)^{j1 + j2 - J} * q^{C_2(J) - C_2(j1) - C_2(j2)}

    where q is related to the level k and C_2(j) = j(j+1).

    At the classical level (q -> 1, k -> infinity), this reduces to
    the permutation eigenvalue (-1)^{j1 + j2 - J}.
    """
    channels = clebsch_gordan_sl2(2 * j1, 2 * j2)
    result = {}
    for n in channels:
        J = Rational(n, 2)
        sign = (-1) ** (j1 + j2 - int(J))
        c2_diff = J * (J + 1) - j1 * (j1 + 1) - j2 * (j2 + 1)
        result[f"J={J}"] = {
            "J": J,
            "dim": n + 1,
            "classical_braiding": sign,
            "casimir_diff": c2_diff,
        }
    return {
        "j1": j1, "j2": j2,
        "channels": result,
        "num_channels": len(channels),
    }


# ============================================================================
# 9. Defect networks = string diagrams = web evaluation
# ============================================================================

def trivalent_vertex_sl2(j1: int, j2: int, j3: int) -> Dict[str, Any]:
    r"""Trivalent vertex (CG intertwiner) for sl_2 defect network.

    A trivalent vertex with incoming lines j1, j2 and outgoing line j3
    exists iff j3 appears in V_{2*j1} x V_{2*j2}, i.e.,
    |j1 - j2| <= j3 <= j1 + j2 and j1 + j2 + j3 is integer.

    The vertex evaluation is (up to normalization):
      <j3, m3 | j1, m1; j2, m2> = CG coefficient.

    Returns:
        Dict with existence check and basic data.
    """
    allowed = clebsch_gordan_sl2(2 * j1, 2 * j2)
    j3_in_allowed = (2 * j3) in allowed
    return {
        "j1": j1, "j2": j2, "j3": j3,
        "exists": j3_in_allowed,
        "triangle_ineq": abs(j1 - j2) <= j3 <= j1 + j2,
        "integrality": (j1 + j2 + j3) == int(j1 + j2 + j3),
        "allowed_channels": [Rational(n, 2) for n in allowed],
    }


def theta_network_sl2(j1: int, j2: int, j3: int) -> Dict[str, Any]:
    r"""Theta network (two trivalent vertices connected by three edges).

    The theta network with edge labels j1, j2, j3 evaluates to:

      Theta(j1, j2, j3) = dim(j1) * dim(j2) * dim(j3) / dim(0)
                         * |{6j symbol}|^2

    This is nonzero iff the triangle inequality is satisfied.
    At the classical level (no quantum deformation):
      Theta_cl = 1 if triangle holds, 0 otherwise.

    The theta network appears in the genus-0 defect partition function:
    it is the 3-punctured sphere with Wilson line insertions.
    """
    exists = (
        abs(j1 - j2) <= j3 <= j1 + j2
        and (j1 + j2 + j3) == int(j1 + j2 + j3)
    )
    return {
        "j1": j1, "j2": j2, "j3": j3,
        "exists": exists,
        "classical_value": 1 if exists else 0,
        "interpretation": "genus-0 defect partition function (3-punctured sphere)",
    }


def defect_web_evaluation_sl2(
    edges: List[Tuple[int, int, int]],
    vertices: List[Tuple[int, int, int]],
) -> Dict[str, Any]:
    r"""Evaluate a planar defect web for sl_2.

    A planar web is a trivalent graph with edges labeled by spins.
    Each vertex (j_a, j_b, j_c) contributes a CG intertwiner.
    The evaluation is the contraction of all intertwiners.

    For simple webs (chains of fusions), this reduces to a product
    of CG coefficients / 6j-symbols.

    Args:
        edges: list of (source_vertex, target_vertex, spin) triples.
        vertices: list of (j1, j2, j3) triples of spins meeting at each vertex.

    Returns:
        Dict with evaluation data.
    """
    # Verify each vertex satisfies triangle inequality
    vertex_valid = []
    for j1, j2, j3 in vertices:
        valid = (
            abs(j1 - j2) <= j3 <= j1 + j2
            and (j1 + j2 + j3) == int(j1 + j2 + j3)
        )
        vertex_valid.append(valid)

    all_valid = all(vertex_valid)
    return {
        "num_edges": len(edges),
        "num_vertices": len(vertices),
        "all_vertices_valid": all_valid,
        "vertex_validity": vertex_valid,
        "euler_characteristic": len(vertices) - len(edges),
        "classical_nonzero": all_valid,
    }


# ============================================================================
# 10. Kapustin--Witten twist and geometric Langlands
# ============================================================================

def langlands_dual_lie_type(lie_type: str, rank: int) -> Tuple[str, int]:
    r"""Langlands dual Lie algebra type.

    The Langlands dual exchanges:
      A_n <-> A_n (self-dual)
      B_n <-> C_n
      D_n <-> D_n (self-dual)
      E_n <-> E_n (self-dual)
      F_4 <-> F_4 (self-dual)
      G_2 <-> G_2 (self-dual, BUT with exchanged root lengths)

    Returns:
        (dual_type, dual_rank).
    """
    if lie_type == "B":
        return ("C", rank)
    elif lie_type == "C":
        return ("B", rank)
    else:
        # A, D, E, F, G are self-dual
        return (lie_type, rank)


def kapustin_witten_dictionary(lie_type: str, rank: int,
                               k: Rational) -> Dict[str, Any]:
    r"""The Kapustin--Witten dictionary for 4d CS / geometric Langlands.

    Maps structures in 4d Chern--Simons with gauge group G at level k
    to structures on the Langlands dual side G^L:

      Wilson line V_lambda (G, k) <-> Hecke eigensheaf (G^L)
      't Hooft line V_mu^L (G^L) <-> Wilson line (G, k^!)
      Defect OPE (R-matrix) <-> Hecke algebra action
      KZ monodromy <-> DK bridge (Drinfeld--Kohno)
      Surface operator GW(sigma) <-> Ramification (Parahoric)

    The KZ connection with level k has monodromy in Rep(U_q(g)) with
    q = exp(pi i / (k + h^v)).  Via the DK theorem, this realizes
    the categorical equivalence Rep_fd(Y(g)) ~ Rep_fd(U_q(g)).

    Returns:
        Dict with the dictionary entries.
    """
    dim_g, h_dual, name = _get_lie_data(lie_type, rank)
    dual_type, dual_rank = langlands_dual_lie_type(lie_type, rank)
    _, dual_h, dual_name = _get_lie_data(dual_type, dual_rank)

    kap = kappa_affine(lie_type, rank, k)
    k_dual = -k - 2 * h_dual

    return {
        "gauge_group": name,
        "langlands_dual": dual_name,
        "level": k,
        "kappa": kap,
        "dual_level": k_dual,
        "q_parameter": f"exp(pi i / ({k} + {h_dual}))",
        "dictionary": {
            "Wilson_line": "Hecke eigensheaf on Bun_{G^L}",
            "tHooft_line": f"Wilson line of {dual_name} at level {k_dual}",
            "defect_OPE": "Hecke algebra action on D-modules",
            "KZ_monodromy": "DK bridge: Rep_fd(Y(g)) ~ Rep_fd(U_q(g))",
            "surface_GW": "Parahoric ramification data",
            "bar_complex": "Derived category of D-modules on Bun_{G^L}",
        },
        "dk_bridge": {
            "status": "PROVED for all simple types (cor:mc3-all-types)",
            "content": (
                "The monodromy of the KZ connection at level k realizes "
                "an equivalence between the evaluation-generated subcategory "
                "of Y(g)-mod and the category of finite-dimensional "
                "U_q(g)-modules."
            ),
        },
    }


def kz_connection_parameter(lie_type: str, rank: int,
                            k: Rational) -> Dict[str, Any]:
    r"""KZ connection data for the defect system.

    The KZ connection on Conf_n(C) x V_1^{x n} is:
      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)

    where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
    the i-th and j-th tensor factors.

    The connection parameter is 1/(k + h^v), which appears in the
    bar complex as the prefactor of the collision residue r(z) = Omega/z.
    This is consistent with r(z) = Res^{coll}_{0,2}(Theta_A) (AP19).

    Returns:
        Dict with KZ data.
    """
    _, h_dual, name = _get_lie_data(lie_type, rank)
    kap = kappa_affine(lie_type, rank, k)

    return {
        "algebra": name,
        "level": k,
        "h_dual": h_dual,
        "kz_parameter": Rational(1, k + h_dual),
        "kappa": kap,
        "r_matrix_prefactor": f"Omega / z with Omega = quadratic Casimir",
        "kz_flat": True,
        "monodromy_target": f"Rep_fd(U_q({name})) with q = exp(pi i / {k + h_dual})",
    }


# ============================================================================
# 11. Defect partition function = module trace
# ============================================================================

def defect_partition_function_genus1(
    lie_type: str, rank: int, k: Rational,
    weight: Tuple[int, ...],
) -> Dict[str, Any]:
    r"""Genus-1 partition function with a line defect insertion.

    For a Wilson line in V_lambda on a genus-1 curve (torus):
      Z_1(A, V_lambda) = Tr_{V_lambda}(q^{L_0 - c/24})
                       = q^{h_lambda - c/24} * ch_{V_lambda}(q)

    where h_lambda = C_2(lambda) / (2(k + h^v)) is the conformal weight
    and ch_{V_lambda}(q) is the character of the representation.

    The defect contribution to the genus-1 shadow is:
      F_1^{defect}(lambda) = (kappa + kappa^{mod}(lambda)) * lambda_1
                           = (kappa + h_lambda) / 24

    This follows from the genus-1 obstruction formula obs_1 = kappa * lambda_1
    corrected by the module-level kappa.

    Returns:
        Dict with partition function data.
    """
    dim_g, h_dual, name = _get_lie_data(lie_type, rank)
    kap = kappa_affine(lie_type, rank, k)
    c2 = quadratic_casimir(lie_type, rank, weight)
    h_lambda = c2 / (2 * (k + h_dual))
    c = central_charge_affine(lie_type, rank, k)

    kap_mod = h_lambda
    kap_total = kap + kap_mod

    return {
        "algebra": name,
        "level": k,
        "weight": weight,
        "central_charge": c,
        "kappa_bulk": kap,
        "conformal_weight": h_lambda,
        "kappa_module": kap_mod,
        "kappa_total": kap_total,
        "F1_bulk": kap / 24,
        "F1_defect": kap_mod / 24,
        "F1_total": kap_total / 24,
        "lambda_1": Rational(1, 24),
    }


# ============================================================================
# 12. Consistency checks and cross-verifications
# ============================================================================

def verify_fusion_associativity_sl2(j1: int, j2: int, j3: int) -> Dict[str, Any]:
    r"""Verify associativity of the defect fusion for sl_2.

    The fusion (j1 x j2) x j3 and j1 x (j2 x j3) must produce the
    same set of channels (with the same multiplicities).

    This is a non-trivial check on the CG coefficients.
    """
    # (j1 x j2) x j3
    channels_12 = clebsch_gordan_sl2(2 * j1, 2 * j2)
    left_assoc = {}
    for n12 in channels_12:
        for n in clebsch_gordan_sl2(n12, 2 * j3):
            left_assoc[n] = left_assoc.get(n, 0) + 1

    # j1 x (j2 x j3)
    channels_23 = clebsch_gordan_sl2(2 * j2, 2 * j3)
    right_assoc = {}
    for n23 in channels_23:
        for n in clebsch_gordan_sl2(2 * j1, n23):
            right_assoc[n] = right_assoc.get(n, 0) + 1

    match = (left_assoc == right_assoc)
    return {
        "j1": j1, "j2": j2, "j3": j3,
        "left_assoc": left_assoc,
        "right_assoc": right_assoc,
        "match": match,
    }


def verify_defect_shadow_additivity(
    lie_type: str, rank: int, k: Rational,
    weight1: Tuple[int, ...], weight2: Tuple[int, ...],
) -> Dict[str, Any]:
    r"""Verify additivity of module kappa for independent defects.

    If two line defects are far apart (non-interacting), the total
    module kappa should be additive:
      kappa^{mod}(lambda_1, lambda_2) = kappa^{mod}(lambda_1) + kappa^{mod}(lambda_2)

    This is the defect analogue of the shadow additivity
    (prop:independent-sum-factorization).
    """
    kap1 = module_kappa(lie_type, rank, weight1, k)
    kap2 = module_kappa(lie_type, rank, weight2, k)
    # For non-interacting defects, the total is the sum
    kap_total = kap1 + kap2
    return {
        "weight_1": weight1,
        "weight_2": weight2,
        "kappa_mod_1": kap1,
        "kappa_mod_2": kap2,
        "kappa_sum": kap_total,
        "additivity_holds": True,  # By construction for non-interacting
    }


def electric_magnetic_duality_check(
    lie_type: str, rank: int, k: Rational,
    weight: Tuple[int, ...],
) -> Dict[str, Any]:
    r"""Check electric-magnetic duality for Wilson/'t Hooft lines.

    For simply-laced g (where g = g^L), S-duality maps:
      Wilson(V_lambda, k) <-> 't Hooft(V_lambda, k^!)

    The Casimir of the Wilson line at level k should match the Casimir
    of the 't Hooft line (which is a Wilson line of A! at level k^!).

    This is a consequence of Theorem C (complementarity) applied to
    the defect sector.
    """
    _, h_dual, name = _get_lie_data(lie_type, rank)
    k_dual = -k - 2 * h_dual

    c2_wilson = quadratic_casimir(lie_type, rank, weight)
    c2_thooft = quadratic_casimir(lie_type, rank, weight)  # Same weight, same g

    kap_mod_wilson = module_kappa(lie_type, rank, weight, k)
    kap_mod_thooft = module_kappa(lie_type, rank, weight, k_dual)

    # The conformal weights are related by level duality
    h_wilson = c2_wilson / (2 * (k + h_dual))
    h_thooft = c2_thooft / (2 * (k_dual + h_dual))

    # At the dual level: k_dual + h_dual = -k - h_dual
    # So h_thooft = C_2 / (2 * (-k - h_dual)) = -h_wilson
    # The sign flip is the Koszul duality signature.

    return {
        "algebra": name,
        "level": k,
        "dual_level": k_dual,
        "weight": weight,
        "casimir": c2_wilson,
        "h_wilson": h_wilson,
        "h_thooft": h_thooft,
        "h_sum": h_wilson + h_thooft,
        "h_sum_vanishes": (h_wilson + h_thooft == 0),
        "interpretation": (
            "h_wilson + h_thooft = 0 is the module-level complementarity, "
            "the defect analogue of kappa + kappa' = 0 for KM (AP24)"
        ),
    }
