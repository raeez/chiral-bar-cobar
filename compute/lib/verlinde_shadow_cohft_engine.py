r"""Verlinde formula from the shadow CohFT for all simple Lie types.

MATHEMATICAL FRAMEWORK
======================

The Verlinde formula computes dimensions of spaces of conformal blocks:

    dim V_{g,k}(G) = sum_lambda S_{0,lambda}^{2-2g}

where S is the Kac-Peterson modular S-matrix and the sum is over
integrable highest-weight representations at level k.

CRITICAL CONVENTION (AP38): The formula uses the ACTUAL S-matrix entries
S_{0,lambda}, NOT the quantum dimensions d_lambda = S_{0,lambda}/S_{0,0}.
The quantum-dimension version sum d_lambda^{2-2g} gives NON-INTEGER
results at genus >= 2.  The correct formula with S_{0,lambda} gives
integers because of the unitarity identity sum |S_{0,lambda}|^2 = 1
which ensures V_0 = 1 (genus-0 normalization).

The shadow CohFT (thm:shadow-cohft) provides a CohFT on M-bar_{g,n}
from the shadow obstruction tower.  For affine Kac-Moody algebras at
positive integer level, the SCALAR shadow partition function is:

    F_g(g_k) = kappa(g_k) * lambda_g^FP

where kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v) is the modular
characteristic and lambda_g^FP is the Faber-Pandharipande number.

KEY IDENTIFICATION (the new derivation route):
The Verlinde dimension is the FULL partition function summing over all
channels (integrable representations).  The shadow CohFT captures the
SCALAR (rank-1) projection of the modular obstruction.  They share the
same modular data (S-matrix, kappa) but compute different projections:

  - Verlinde: sum over ALL channels, giving integer partition functions
  - Shadow: scalar channel (rank 1, kappa-weighted Hodge class)

The BRIDGE: the Verlinde formula can be DERIVED from the shadow CohFT
by decomposing the MC element Theta_A into quantum-group channels.
Each channel lambda contributes S_{0,lambda}^{2-2g} to the genus-g
partition function.  The scalar shadow F_g = kappa * lambda_g^FP is
the arity-0 projection that sees only the overall kappa invariant.

At genus 1:
    V_{1,k} = number of integrable reps = |P_+^k|
    F_1 = kappa / 24

The ratio V_1 / F_1 = 24 * |P_+^k| / kappa encodes the quantum-group
rank beyond the scalar shadow.

COMPUTATION PLAN:
  1. Modular S-matrix for all simple types (Kac-Peterson / quantum Weyl)
  2. Verlinde dimensions V_{g,k}(g) for g=0,...,5 and k=1,...,5
  3. Shadow F_g = kappa * lambda_g^FP
  4. Level-rank duality: V_{g,k}(A_{N-1}) vs V_{g,N}(A_{k-1})
  5. Asymptotic growth comparison
  6. Fusion rules from the Verlinde formula

CONVENTIONS:
  - Representations labeled by Dynkin labels (a_1, ..., a_r)
    with a_i >= 0 and sum_i a_i * colabel_i <= k.
  - S_{0,0} > 0 (positive normalization)
  - For sl_2: S_{jl} = sqrt(2/(k+2)) sin(pi(j+1)(l+1)/(k+2))
  - Verlinde formula: V_g = sum_lambda S_{0,lambda}^{2-2g}

Mathematical references:
  Verlinde (1988), Nuclear Phys. B 300, 115--138
  Kac-Peterson (1984), Adv. Math. 53, 125--264
  Beauville (1996), The Verlinde formula for PGL_p
  Di Francesco-Mathieu-Senechal (1997), Conformal Field Theory
  Fuchs (1992), Affine Lie Algebras and Quantum Groups
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:modular-characteristic (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from sympy import (
    Rational,
    bernoulli,
    binomial,
    factorial,
    simplify,
    sympify,
)


# =========================================================================
# Section 0: Lie algebra data
# =========================================================================

# (type, rank) -> dict with dim, Coxeter h, dual Coxeter h^v, name,
#   rank, colabels (marks of dual affine Dynkin = coefficients of the
#   highest root in simple root basis).

_LIE_DATA = {
    ("A", 1): {"dim": 3, "h": 2, "hv": 2, "name": "sl_2",
               "rank": 1, "colabels": (1,)},
    ("A", 2): {"dim": 8, "h": 3, "hv": 3, "name": "sl_3",
               "rank": 2, "colabels": (1, 1)},
    ("A", 3): {"dim": 15, "h": 4, "hv": 4, "name": "sl_4",
               "rank": 3, "colabels": (1, 1, 1)},
    ("A", 4): {"dim": 24, "h": 5, "hv": 5, "name": "sl_5",
               "rank": 4, "colabels": (1, 1, 1, 1)},
    ("B", 2): {"dim": 10, "h": 4, "hv": 3, "name": "so_5",
               "rank": 2, "colabels": (1, 2)},
    ("B", 3): {"dim": 21, "h": 6, "hv": 5, "name": "so_7",
               "rank": 3, "colabels": (1, 2, 2)},
    ("C", 2): {"dim": 10, "h": 4, "hv": 3, "name": "sp_4",
               "rank": 2, "colabels": (2, 1)},
    ("C", 3): {"dim": 21, "h": 6, "hv": 4, "name": "sp_6",
               "rank": 3, "colabels": (2, 2, 1)},
    ("D", 4): {"dim": 28, "h": 6, "hv": 6, "name": "so_8",
               "rank": 4, "colabels": (1, 2, 1, 1)},
    ("G", 2): {"dim": 14, "h": 6, "hv": 4, "name": "G_2",
               "rank": 2, "colabels": (2, 3)},
    ("F", 4): {"dim": 52, "h": 12, "hv": 9, "name": "F_4",
               "rank": 4, "colabels": (2, 4, 3, 2)},
    ("E", 6): {"dim": 78, "h": 12, "hv": 12, "name": "E_6",
               "rank": 6, "colabels": (1, 2, 3, 2, 1, 2)},
    ("E", 7): {"dim": 133, "h": 18, "hv": 18, "name": "E_7",
               "rank": 7, "colabels": (2, 3, 4, 3, 2, 1, 2)},
    ("E", 8): {"dim": 248, "h": 30, "hv": 30, "name": "E_8",
               "rank": 8, "colabels": (2, 4, 6, 5, 4, 3, 2, 3)},
}


def _get_lie_data(lie_type: str, rank: int) -> dict:
    """Return Lie algebra data for (type, rank)."""
    key = (lie_type, rank)
    if key in _LIE_DATA:
        return _LIE_DATA[key]
    if lie_type == "A" and rank >= 1:
        N = rank + 1
        return {
            "dim": N * N - 1,
            "h": N,
            "hv": N,
            "name": f"sl_{N}",
            "rank": rank,
            "colabels": tuple([1] * rank),
        }
    raise ValueError(f"Unsupported Lie algebra ({lie_type}, {rank})")


# =========================================================================
# Section 1: Modular characteristic kappa
# =========================================================================

def kappa_affine(lie_type: str, rank: int, level: Union[int, float]) -> float:
    """Modular characteristic for affine g-hat at level k.

    kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v)

    This is the MODULAR CHARACTERISTIC, NOT c/2 in general (AP39, AP48).
    """
    data = _get_lie_data(lie_type, rank)
    return data["dim"] * (level + data["hv"]) / (2.0 * data["hv"])


def kappa_affine_exact(lie_type: str, rank: int, level: int) -> Rational:
    """Exact modular characteristic as sympy Rational."""
    data = _get_lie_data(lie_type, rank)
    return Rational(data["dim"]) * Rational(level + data["hv"], 2 * data["hv"])


def central_charge(lie_type: str, rank: int, level: Union[int, float]) -> float:
    """Sugawara central charge c = k * dim(g) / (k + h^v)."""
    data = _get_lie_data(lie_type, rank)
    return level * data["dim"] / (level + data["hv"])


# =========================================================================
# Section 2: Root system data
# =========================================================================

def cartan_matrix(lie_type: str, rank: int) -> np.ndarray:
    """Cartan matrix for simple Lie algebra (type, rank)."""
    r = rank
    if lie_type == "A":
        C = np.zeros((r, r))
        for i in range(r):
            C[i, i] = 2
            if i > 0:
                C[i, i - 1] = -1
            if i < r - 1:
                C[i, i + 1] = -1
        return C
    if lie_type == "B":
        C = np.zeros((r, r))
        for i in range(r):
            C[i, i] = 2
            if i > 0:
                C[i, i - 1] = -1
            if i < r - 1:
                C[i, i + 1] = -1
        if r >= 2:
            C[r - 1, r - 2] = -2
        return C
    if lie_type == "C":
        C = np.zeros((r, r))
        for i in range(r):
            C[i, i] = 2
            if i > 0:
                C[i, i - 1] = -1
            if i < r - 1:
                C[i, i + 1] = -1
        if r >= 2:
            C[r - 2, r - 1] = -2
        return C
    if lie_type == "D":
        if r < 3:
            raise ValueError("D type requires rank >= 3")
        C = np.zeros((r, r))
        for i in range(r):
            C[i, i] = 2
        for i in range(r - 2):
            C[i, i + 1] = -1
            C[i + 1, i] = -1
        C[r - 3, r - 1] = -1
        C[r - 1, r - 3] = -1
        return C
    if lie_type == "G" and rank == 2:
        return np.array([[2, -1], [-3, 2]], dtype=float)
    if lie_type == "F" and rank == 4:
        return np.array([
            [2, -1, 0, 0],
            [-1, 2, -2, 0],
            [0, -1, 2, -1],
            [0, 0, -1, 2],
        ], dtype=float)
    if lie_type == "E" and rank == 6:
        C = np.zeros((6, 6))
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)]
        for i in range(6):
            C[i, i] = 2
        for (i, j) in edges:
            C[i, j] = -1
            C[j, i] = -1
        return C
    if lie_type == "E" and rank == 7:
        C = np.zeros((7, 7))
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (2, 6)]
        for i in range(7):
            C[i, i] = 2
        for (i, j) in edges:
            C[i, j] = -1
            C[j, i] = -1
        return C
    if lie_type == "E" and rank == 8:
        C = np.zeros((8, 8))
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]
        for i in range(8):
            C[i, i] = 2
        for (i, j) in edges:
            C[i, j] = -1
            C[j, i] = -1
        return C
    raise ValueError(f"Cartan matrix not implemented for ({lie_type}, {rank})")


def positive_roots(lie_type: str, rank: int) -> List[np.ndarray]:
    """Positive roots in the simple root basis via BFS with full string computation.

    Uses the alpha_j-string through alpha: the string has length p+q+1 where
    p = max s such that alpha - s*alpha_j is a root, and q = p - <alpha, alpha_j^v>.
    We add alpha + alpha_j if q >= 1.
    """
    r = rank
    C = cartan_matrix(lie_type, rank)
    roots = []
    for i in range(r):
        e = np.zeros(r)
        e[i] = 1
        roots.append(e)

    seen = set()
    for rt in roots:
        seen.add(tuple(rt.astype(int)))

    queue = list(range(len(roots)))
    while queue:
        idx = queue.pop(0)
        alpha = roots[idx]
        for j in range(r):
            # Compute <alpha, alpha_j^v> = sum_k alpha_k * C_{jk}
            # NOTE: C_{jk} = 2<alpha_j, alpha_k>/<alpha_j, alpha_j>,
            # and <alpha, alpha_j^v> = sum_k alpha_k * C_{jk} = dot(C[j,:], alpha).
            # For symmetric C (simply-laced): C[j,k] = C[k,j], so both give same.
            # For non-symmetric C (non-simply-laced): MUST use row j.
            cartan_val = sum(int(alpha[k]) * C[j, k] for k in range(r))
            # Compute p: max s >= 0 such that alpha - s*alpha_j is a positive root
            p = 0
            test = alpha.copy()
            while True:
                test = test.copy()
                test[j] -= 1
                key = tuple(test.astype(int))
                if all(x >= 0 for x in test) and key in seen:
                    p += 1
                else:
                    break
            # q = p - <alpha, alpha_j^v>
            q = p - cartan_val
            if q >= 1:
                new_root = alpha.copy()
                new_root[j] += 1
                key = tuple(new_root.astype(int))
                if key not in seen:
                    seen.add(key)
                    roots.append(new_root)
                    queue.append(len(roots) - 1)
    return roots


# =========================================================================
# Section 3: Integrable representations
# =========================================================================

def integrable_weights(lie_type: str, rank: int, level: int) -> List[Tuple[int, ...]]:
    """Enumerate integrable highest weights at level k.

    Condition: a_i >= 0 and sum_i a_i * colabel_i <= k.
    Colabels are the coefficients of the highest root in the simple root basis.
    """
    data = _get_lie_data(lie_type, rank)
    r = data["rank"]
    colabels = data["colabels"]

    if r == 0:
        return [()]

    weights = []
    _enumerate_weights(colabels, level, r, 0, [], weights)
    return sorted(weights)


def _enumerate_weights(
    colabels: Tuple[int, ...], budget: int, r: int,
    idx: int, current: list, results: list,
) -> None:
    """Recursively enumerate weights with sum_i a_i * colabel_i <= budget."""
    if idx == r:
        results.append(tuple(current))
        return
    c = colabels[idx]
    max_val = budget // c
    for a in range(max_val + 1):
        current.append(a)
        _enumerate_weights(colabels, budget - a * c, r, idx + 1, current, results)
        current.pop()


def num_integrable_reps(lie_type: str, rank: int, level: int) -> int:
    """Number of integrable highest-weight representations at level k.

    For type A_r at level k: C(k + r, r).
    For other types: enumerated from colabels.
    """
    if lie_type == "A":
        return int(binomial(level + rank, rank))
    return len(integrable_weights(lie_type, rank, level))


# =========================================================================
# Section 4: Quantum Weyl dimension formula
# =========================================================================

def quantum_dim_weyl(
    dynkin_labels: Tuple[int, ...],
    lie_type: str,
    rank: int,
    level: int,
) -> float:
    """Quantum dimension via the quantum Weyl dimension formula.

    d_lambda = prod_{alpha > 0} sin(pi * (lambda+rho, alpha) / (k+h^v))
                                / sin(pi * (rho, alpha) / (k+h^v))

    where the inner product uses (omega_i, alpha_j) = delta_{ij} for
    simply-laced types, and the appropriate correction for non-simply-laced.

    For non-simply-laced types, the inner product is:
    (omega_i, alpha_j) = (d_j / 2) * delta_{ij}
    where d_j = |alpha_j|^2 is the root length squared.

    Actually: (omega_i, alpha_j) = delta_{ij} for all types when using
    the standard normalization (omega_i, alpha_j^v) = delta_{ij} and
    the pairing with ROOTS (not coroots).

    For the quantum Weyl formula, we need (lambda+rho, alpha) where
    alpha is a positive root and the pairing is the standard one.
    In the fundamental weight basis with lambda_fw and alpha in the
    simple root basis:
        (lambda_fw, alpha_sr) = sum_i lambda_i * (omega_i, alpha_sr)
    where (omega_i, alpha) = sum_j c_j * (omega_i, alpha_j) for alpha = sum c_j alpha_j.

    For simply-laced: (omega_i, alpha_j) = delta_{ij},
    so (lambda_fw, alpha_sr) = sum_i lambda_i c_i = dot(lambda_fw, alpha_sr).
    """
    data = _get_lie_data(lie_type, rank)
    hv = data["hv"]
    n = level + hv

    pos = positive_roots(lie_type, rank)
    rho = np.ones(rank)
    lam_rho = np.array([a + 1.0 for a in dynkin_labels])

    # Inner product: for simply-laced, (omega_i, alpha_j) = delta_{ij}
    # For non-simply-laced, we need the full inner product.
    # The correct formula for all types: use the NORMALIZED inner product
    # where the bilinear form is (alpha_i, alpha_j) = d_i C_{ij} / 2
    # and (omega_i, alpha_j) = d_j delta_{ij} / 2.
    # But the Kac-Peterson formula uses (,) normalized so that
    # (alpha_long, alpha_long) = 2.  For the quantum Weyl formula,
    # the argument of sin is pi * (lambda+rho, alpha^v) / (k+h^v)
    # where alpha^v = 2*alpha/(alpha, alpha) is the COROOT.
    # (lambda, alpha^v) = sum_i lambda_i (omega_i, alpha_j^v) c_j
    #                   = sum_i lambda_i * delta_{ij} * c_j = sum c_i lambda_i
    # So in terms of coroots: (lambda_fw, alpha^v) = dot(lambda_fw, coroot_coeffs).
    # The coroot of alpha = sum c_i alpha_i is alpha^v = sum c_i^v alpha_i^v
    # For simply-laced: alpha^v = alpha, so c_i^v = c_i.
    # For non-simply-laced: alpha^v = 2 alpha / |alpha|^2.

    dim = 1.0
    for alpha_sr in pos:
        # Compute <lambda+rho, alpha^v> where alpha^v = 2*alpha/(alpha,alpha)
        # is the coroot.  The quantum Weyl formula uses
        # sin(pi * <lambda+rho, alpha^v> / (k+h^v)) in numerator and denominator.
        #
        # For simply-laced: all roots have length^2 = 2, so alpha^v = alpha,
        # and <lambda, alpha^v> = <lambda, alpha> = dot(lambda_fw, alpha_sr)
        # since (omega_i, alpha_j) = delta_{ij}.
        #
        # For non-simply-laced: <lambda, alpha^v> = 2<lambda, alpha>/(alpha,alpha).
        # But (omega_i, alpha_j) = delta_{ij} still holds (this is the definition
        # of fundamental weights), so <lambda_fw, alpha_sr> = dot(lambda_fw, alpha_sr).
        # Then <lambda, alpha^v> = 2 * dot(lambda_fw, alpha_sr) / (alpha, alpha).
        # And (alpha, alpha) = sum_{i,j} c_i c_j (alpha_i, alpha_j).
        # But <lambda, alpha^v> also equals sum_i lambda_i * <omega_i, alpha^v>
        # = sum_i lambda_i * (2 (omega_i, alpha) / (alpha, alpha))
        # And (omega_i, alpha) = sum_j c_j (omega_i, alpha_j) = c_i (the coefficient).
        # So <lambda_fw, alpha^v> = sum_i lambda_i * 2 c_i / (alpha, alpha).
        #
        # ACTUALLY the simplest correct approach: the quantum Weyl formula uses
        # the inner product (lambda+rho, alpha) divided by (rho, alpha_long).
        # The argument of sin is pi * (lambda+rho, alpha) / (k+h^v) where the
        # inner product is the one making LONG roots have (alpha, alpha) = 2.
        #
        # The simplest universal formula: <lambda_fw, alpha_sr> = dot(lambda_fw, alpha_sr)
        # because (omega_i, alpha_j) = delta_{ij} for ALL types.
        # The quantum Weyl formula is:
        # d_lambda = prod_{alpha>0} sin(pi * <lambda+rho, alpha> / (k+g))
        #                          / sin(pi * <rho, alpha> / (k+g))
        # where g = h^v (dual Coxeter) and <,> is the pairing with (omega_i, alpha_j) = delta.
        # THIS IS THE CORRECT FORMULA FOR ALL TYPES.

        ip_lam = float(np.dot(lam_rho, alpha_sr))
        ip_rho = float(np.dot(rho, alpha_sr))

        num = math.sin(math.pi * ip_lam / n)
        den = math.sin(math.pi * ip_rho / n)
        if abs(den) < 1e-15:
            if abs(num) < 1e-15:
                # 0/0: both lambda+rho and rho hit the affine wall
                # Use L'Hopital: limit is ip_lam / ip_rho
                if abs(ip_rho) < 1e-15:
                    continue  # skip degenerate root
                dim *= ip_lam / ip_rho
            else:
                # 0 denominator, nonzero numerator: infinite qdim -> not integrable
                return 0.0
        elif abs(num) < 1e-15:
            return 0.0
        else:
            dim *= num / den

    return abs(dim)


def _root_lengths_squared(lie_type: str, rank: int) -> np.ndarray:
    """Squared lengths of simple roots (long roots have length^2 = 2)."""
    r = rank
    if lie_type in ("A", "D", "E"):
        return np.full(r, 2.0)
    if lie_type == "B":
        lens = np.full(r, 2.0)
        lens[r - 1] = 1.0
        return lens
    if lie_type == "C":
        lens = np.full(r, 1.0)
        lens[r - 1] = 2.0
        return lens
    if lie_type == "G" and rank == 2:
        return np.array([2.0 / 3.0, 2.0])
    if lie_type == "F" and rank == 4:
        return np.array([2.0, 2.0, 1.0, 1.0])
    raise ValueError(f"Root lengths not implemented for ({lie_type}, {rank})")


# =========================================================================
# Section 5: Modular S-matrix
# =========================================================================

@lru_cache(maxsize=64)
def S_matrix(lie_type: str, rank: int, level: int) -> np.ndarray:
    """Modular S-matrix for affine g-hat at positive integer level k.

    For type A_r (sl_{r+1}): uses the Kac-Peterson formula with
    epsilon coordinates and S_{r+1} Weyl group.

    For general type: uses the Kac-Peterson formula with the standard
    inner product and Weyl group action on shifted weights.

    Normalization: S S^dagger = I, S_{0,0} > 0.
    """
    if level < 1:
        raise ValueError(f"Level must be positive, got k={level}")

    if lie_type == "A":
        return _S_matrix_typeA(rank, level)
    else:
        return _S_matrix_general(lie_type, rank, level)


def _S_matrix_typeA(rank: int, level: int) -> np.ndarray:
    """S-matrix for type A using epsilon coordinates and S_{r+1} Weyl group.

    S_{lambda,mu} = const * sum_{w in S_{r+1}} sgn(w) *
        exp(-2*pi*i * <w(lambda+rho), mu+rho>_0 / (k+h^v))

    where <v, w>_0 is the traceless inner product on epsilon coordinates.
    """
    N = rank + 1
    n = level + N  # shifted level
    weights = integrable_weights("A", rank, level)
    n_wts = len(weights)

    from itertools import permutations

    def shifted_eps(dynkin):
        """Convert Dynkin labels to shifted epsilon coordinates."""
        eps = np.zeros(N)
        shifted = [a + 1 for a in dynkin]
        for i in range(rank):
            eps[i] = sum(shifted[j] for j in range(i, rank))
        return eps

    def ip_traceless(v, w):
        """Traceless inner product on epsilon space."""
        return float(np.dot(v, w) - np.sum(v) * np.sum(w) / N)

    # Precompute Weyl group = S_N
    weyl = []
    for perm in permutations(range(N)):
        inv = sum(1 for i in range(N) for j in range(i + 1, N)
                  if perm[i] > perm[j])
        weyl.append((perm, (-1) ** inv))

    # Shifted epsilon vectors
    eps_list = [shifted_eps(wt) for wt in weights]

    S_raw = np.zeros((n_wts, n_wts), dtype=complex)
    for i in range(n_wts):
        for j in range(n_wts):
            val = 0.0j
            for (perm, sgn) in weyl:
                w_eps = eps_list[i][list(perm)]
                ip = ip_traceless(w_eps, eps_list[j])
                val += sgn * np.exp(-2.0j * np.pi * ip / n)
            S_raw[i, j] = val

    # Normalize to unitary
    row0_norm = np.sqrt(np.sum(np.abs(S_raw[0, :]) ** 2))
    S_mat = S_raw / row0_norm

    # Phase: S_{0,0} real and positive
    phase = S_mat[0, 0] / np.abs(S_mat[0, 0])
    S_mat = S_mat / phase

    return S_mat


def _S_matrix_general(lie_type: str, rank: int, level: int) -> np.ndarray:
    """S-matrix for general type via Kac-Peterson formula.

    Uses the inner product on the weight lattice:
    For simply-laced: (lambda, alpha) = dot(lambda_fw, alpha_sr)
    For non-simply-laced: includes root length correction.
    """
    data = _get_lie_data(lie_type, rank)
    hv = data["hv"]
    n = level + hv

    weights = integrable_weights(lie_type, rank, level)
    n_wts = len(weights)

    # Shifted weights (lambda + rho) in fundamental weight basis
    shifted = [np.array([a + 1.0 for a in wt]) for wt in weights]

    # Weyl group
    weyl_elts = _generate_weyl_group(lie_type, rank)

    # Inner product matrix for simply-laced: G = C^{-1}
    # For non-simply-laced: G_{ij} = (omega_i, omega_j)
    C = cartan_matrix(lie_type, rank)
    if lie_type in ("A", "D", "E"):
        G = np.linalg.inv(C)
    else:
        d = _root_lengths_squared(lie_type, rank)
        D_half = np.diag(d / 2.0)
        B = D_half @ C  # B_{ij} = (alpha_i, alpha_j)
        C_inv = np.linalg.inv(C)
        G = C_inv.T @ B @ C_inv

    S_raw = np.zeros((n_wts, n_wts), dtype=complex)
    for i in range(n_wts):
        for j in range(n_wts):
            val = 0.0j
            for (w_mat, sgn) in weyl_elts:
                w_shifted = w_mat @ shifted[i]
                ip = float(w_shifted @ G @ shifted[j])
                val += sgn * np.exp(-2.0j * np.pi * ip / n)
            S_raw[i, j] = val

    # Normalize
    row0_norm = np.sqrt(np.sum(np.abs(S_raw[0, :]) ** 2))
    if row0_norm < 1e-15:
        raise RuntimeError(
            f"S-matrix normalization failed for ({lie_type}, {rank}) at k={level}"
        )
    S_mat = S_raw / row0_norm
    phase = S_mat[0, 0] / np.abs(S_mat[0, 0])
    S_mat = S_mat / phase

    return S_mat


@lru_cache(maxsize=32)
def _generate_weyl_group(lie_type: str, rank: int) -> Tuple[Tuple[Any, ...], ...]:
    """Generate all Weyl group elements as matrices on the weight space.

    Simple reflection s_i acts as: s_i(e_j) = e_j - C_{ji} e_i
    where C is the Cartan matrix and e_j are fundamental weight basis vectors.
    """
    r = rank
    C = cartan_matrix(lie_type, rank)

    reflections = []
    for i in range(r):
        M = np.eye(r)
        for j in range(r):
            M[i, j] -= C[j, i]
        reflections.append(M)

    identity = np.eye(r)
    elements = [(identity, 1)]
    seen = {_mat_key(identity)}
    queue = [0]

    while queue:
        idx = queue.pop(0)
        w_mat, w_sgn = elements[idx]
        for s in reflections:
            new_mat = s @ w_mat
            key = _mat_key(new_mat)
            if key not in seen:
                seen.add(key)
                elements.append((new_mat, -w_sgn))
                queue.append(len(elements) - 1)

    return tuple((m, s) for (m, s) in elements)


def _mat_key(M: np.ndarray) -> tuple:
    """Hashable key for a matrix."""
    return tuple(np.round(M.flatten(), 8))


# =========================================================================
# Section 6: Quantum dimensions
# =========================================================================

def quantum_dimensions(lie_type: str, rank: int, level: int) -> np.ndarray:
    """Quantum dimensions d_lambda = S_{0,lambda} / S_{0,0}.

    WARNING: The Verlinde formula uses S_{0,lambda}^{2-2g}, NOT
    d_lambda^{2-2g}.  Quantum dimensions are useful for fusion rules
    and quantum group data, but the Verlinde number computation
    requires the raw S-matrix entries.
    """
    S = S_matrix(lie_type, rank, level)
    s00 = S[0, 0].real
    return (S[0, :] / s00).real


def total_quantum_dim_sq(lie_type: str, rank: int, level: int) -> float:
    """Total quantum dimension squared D^2 = 1/S_{0,0}^2."""
    S = S_matrix(lie_type, rank, level)
    s00 = S[0, 0].real
    return 1.0 / (s00 * s00)


# =========================================================================
# Section 7: Verlinde formula
# =========================================================================

def verlinde_dimension(lie_type: str, rank: int, level: int, genus: int) -> float:
    """Verlinde dimension: dim of space of conformal blocks at genus g.

    V_{g,k}(g) = sum_lambda S_{0,lambda}^{2-2g}

    CRITICAL: uses RAW S-matrix entries, NOT quantum dimensions.

    Special cases:
      g=0: V_0 = sum S_{0,lambda}^2 = 1 (by unitarity of row 0).
      g=1: V_1 = sum S_{0,lambda}^0 = |P_+^k| (number of integrable reps).

    Returns floating-point value (positive integer for unitary RCFT).
    """
    if genus < 0:
        raise ValueError(f"Genus must be non-negative, got {genus}")

    S = S_matrix(lie_type, rank, level)
    n_wts = S.shape[0]
    power = 2 - 2 * genus

    total = 0.0
    for j in range(n_wts):
        s0j = S[0, j]
        mag = abs(s0j)
        if mag > 1e-15:
            total += mag ** power
    return total


def verlinde_dimension_exact(lie_type: str, rank: int, level: int, genus: int) -> int:
    """Verlinde dimension rounded to nearest integer."""
    v = verlinde_dimension(lie_type, rank, level, genus)
    result = int(round(v))
    if abs(v - result) > 0.1:
        raise RuntimeError(
            f"Verlinde dimension not close to integer: "
            f"V_{genus},{level}({lie_type}_{rank}) = {v}"
        )
    return result


# =========================================================================
# Section 8: Independent Verlinde computation via quantum Weyl dimensions
# =========================================================================

def verlinde_from_weyl_qdim(
    lie_type: str, rank: int, level: int, genus: int,
) -> float:
    """Verlinde dimension via quantum Weyl dimensions (independent path).

    V_{g,k} = (S_{0,0})^{2g-2} * sum_lambda d_lambda^{2-2g}

    where d_lambda = S_{0,lambda}/S_{0,0} is the quantum dimension
    computed from the Weyl formula, and S_{0,0} = D^{-1} where
    D^2 = sum d_lambda^2.

    This is INDEPENDENT of the S-matrix computation (verification path).
    """
    if genus == 0:
        # V_0 = sum S_{0,j}^2 = 1 by unitarity
        return 1.0

    weights = integrable_weights(lie_type, rank, level)
    # Compute quantum dimensions
    qdims = []
    for wt in weights:
        d = quantum_dim_weyl(wt, lie_type, rank, level)
        if d > 1e-15:
            qdims.append(d)

    if genus == 1:
        return float(len(qdims))

    # Compute D^2 = sum d_lambda^2
    D2 = sum(d ** 2 for d in qdims)
    D = math.sqrt(D2)
    # S_{0,0} = 1/D, so S_{0,lambda} = d_lambda / D
    # V_g = sum (d_lambda/D)^{2-2g} = D^{2g-2} * sum d_lambda^{2-2g}
    power = 2 - 2 * genus
    qdim_sum = sum(d ** power for d in qdims)
    return D ** (2 * genus - 2) * qdim_sum


# =========================================================================
# Section 9: Fusion rules
# =========================================================================

def fusion_coefficients(lie_type: str, rank: int, level: int) -> np.ndarray:
    """Fusion coefficients N_{lambda,mu}^nu via the Verlinde formula.

    N_{lambda,mu}^nu = sum_sigma S_{lambda,sigma} S_{mu,sigma}
                       conj(S_{nu,sigma}) / S_{0,sigma}
    """
    S = S_matrix(lie_type, rank, level)
    n_wts = S.shape[0]
    N = np.zeros((n_wts, n_wts, n_wts))

    for i in range(n_wts):
        for j in range(n_wts):
            for m in range(n_wts):
                total = 0.0j
                for l in range(n_wts):
                    s0l = S[0, l]
                    if abs(s0l) > 1e-15:
                        total += S[i, l] * S[j, l] * np.conj(S[m, l]) / s0l
                N[i, j, m] = total.real
    return N


def verify_fusion_integrality(lie_type: str, rank: int, level: int) -> Dict[str, Any]:
    """Verify that all fusion coefficients are non-negative integers."""
    N = fusion_coefficients(lie_type, rank, level)
    max_dev = 0.0
    all_ok = True
    for val in N.flatten():
        dev = abs(val - round(val))
        if dev > max_dev:
            max_dev = dev
        if dev > 0.01 or round(val) < -0.5:
            all_ok = False
    return {
        "all_nonneg_integer": all_ok,
        "max_deviation": max_dev,
    }


# =========================================================================
# Section 10: Shadow CohFT partition function
# =========================================================================

def lambda_fp(g: int) -> Rational:
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    numer = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    denom = 2 ** (2 * g - 1) * factorial(2 * g)
    return Rational(numer, denom)


def shadow_F_g(lie_type: str, rank: int, level: int, genus: int) -> Rational:
    """Shadow CohFT genus-g partition function.

    F_g(g_k) = kappa(g_k) * lambda_g^FP

    This is the SCALAR projection of the shadow obstruction tower.
    IMPORTANT (AP31): kappa = 0 does NOT imply Theta = 0.
    F_g captures only the kappa-weighted scalar part.
    """
    if genus < 1:
        raise ValueError(f"F_g defined for genus >= 1, got {genus}")
    kap = kappa_affine_exact(lie_type, rank, level)
    return kap * lambda_fp(genus)


# =========================================================================
# Section 11: Shadow-Verlinde comparison
# =========================================================================

def shadow_verlinde_comparison(
    lie_type: str, rank: int, level: int, genus: int,
) -> Dict[str, Any]:
    """Compare shadow CohFT partition function with Verlinde dimension.

    V_{g,k}: full partition function (sum over all channels, integer)
    F_g: scalar shadow (kappa-weighted Hodge class, real-valued)

    Their ratio encodes the quantum-group decomposition.
    """
    result = {
        "lie_type": lie_type, "rank": rank,
        "level": level, "genus": genus,
    }

    V = verlinde_dimension_exact(lie_type, rank, level, genus)
    result["verlinde_dim"] = V

    if genus >= 1:
        F = shadow_F_g(lie_type, rank, level, genus)
        result["shadow_F_g"] = float(F)
        result["shadow_F_g_exact"] = F
        if abs(float(F)) > 1e-30:
            result["ratio_V_over_F"] = V / float(F)

    result["kappa"] = kappa_affine(lie_type, rank, level)
    result["central_charge"] = central_charge(lie_type, rank, level)
    result["num_reps"] = num_integrable_reps(lie_type, rank, level)

    return result


def asymptotic_growth_comparison(
    lie_type: str, rank: int, level: int, max_genus: int = 10,
) -> Dict[str, Any]:
    """Compare asymptotic growth of Verlinde and shadow F_g.

    V_{g,k} grows as D^{2g-2} * (constant) for large g.
    F_g ~ kappa * |B_{2g}|/(2g)! (Bernoulli decay).
    """
    result = {
        "lie_type": lie_type, "rank": rank, "level": level,
    }
    D2 = total_quantum_dim_sq(lie_type, rank, level)
    result["D_squared"] = D2
    result["verlinde_log_growth_rate"] = math.log(D2) if D2 > 1 else 0.0
    result["kappa"] = kappa_affine(lie_type, rank, level)

    verlinde = []
    shadow = []
    for g in range(1, max_genus + 1):
        V = verlinde_dimension_exact(lie_type, rank, level, g)
        F = float(shadow_F_g(lie_type, rank, level, g))
        verlinde.append(V)
        shadow.append(F)

    result["verlinde_dims"] = verlinde
    result["shadow_F_g"] = shadow
    return result


# =========================================================================
# Section 12: Level-rank duality
# =========================================================================

def level_rank_check(N: int, k: int, genus: int) -> Dict[str, Any]:
    """Check level-rank duality: V_{g,k}(sl_N) vs V_{g,N}(sl_k).

    For SL(N): V_{g,k}(sl_N) is NOT in general equal to V_{g,N}(sl_k).
    The full level-rank duality is for U(N)/GL(N), not SL(N).
    We compute both sides and report.
    """
    result = {"N": N, "k": k, "genus": genus}

    if N < 2 or k < 2:
        result["note"] = "Level-rank requires N >= 2, k >= 2"
        return result

    V_A = verlinde_dimension_exact("A", N - 1, k, genus)
    V_B = verlinde_dimension_exact("A", k - 1, N, genus)
    result["V_slN_k"] = V_A
    result["V_slk_N"] = V_B
    result["equal"] = V_A == V_B

    kap_A = kappa_affine("A", N - 1, k)
    kap_B = kappa_affine("A", k - 1, N)
    result["kappa_A"] = kap_A
    result["kappa_B"] = kap_B

    return result


# =========================================================================
# Section 13: S-matrix property verification
# =========================================================================

def verify_S_matrix_properties(lie_type: str, rank: int, level: int) -> Dict[str, Any]:
    """Verify fundamental S-matrix properties."""
    S = S_matrix(lie_type, rank, level)
    n = S.shape[0]
    result = {}

    # Unitarity
    SSd = S @ np.conj(S.T)
    result["unitary_dev"] = float(np.max(np.abs(SSd - np.eye(n))))
    result["is_unitary"] = result["unitary_dev"] < 1e-6

    # S_{0,0} positive
    result["S_00"] = float(S[0, 0].real)
    result["S_00_positive"] = result["S_00"] > 0

    # Quantum dimensions
    qd = (S[0, :] / S[0, 0]).real
    result["quantum_dims"] = qd.tolist()
    result["all_qd_positive"] = bool(np.all(qd > -1e-10))

    # Symmetry (S should be symmetric or at least S = S^T up to phase)
    result["symmetry_dev"] = float(np.max(np.abs(S - S.T)))

    return result


# =========================================================================
# Section 14: Known Verlinde numbers for cross-checking
# =========================================================================

# Source: Direct computation via the Verlinde formula
# sum_{j=0}^{k} S_{0,j}^{2-2g}
# All verified independently below.

_KNOWN_VERLINDE = {
    # sl_2 (type A, rank 1):
    ("A", 1, 1, 0): 1, ("A", 1, 1, 1): 2, ("A", 1, 1, 2): 4,
    ("A", 1, 1, 3): 8, ("A", 1, 1, 4): 16,
    ("A", 1, 2, 0): 1, ("A", 1, 2, 1): 3, ("A", 1, 2, 2): 10,
    ("A", 1, 2, 3): 36, ("A", 1, 2, 4): 136,
    ("A", 1, 3, 0): 1, ("A", 1, 3, 1): 4, ("A", 1, 3, 2): 20,
    ("A", 1, 3, 3): 120, ("A", 1, 3, 4): 800,
    ("A", 1, 4, 0): 1, ("A", 1, 4, 1): 5, ("A", 1, 4, 2): 35,
    ("A", 1, 4, 3): 329, ("A", 1, 5, 0): 1, ("A", 1, 5, 1): 6,
    # sl_3 at k=1: V_g = 3^g (all S_{0,j} = 1/sqrt(3))
    ("A", 2, 1, 0): 1, ("A", 2, 1, 1): 3, ("A", 2, 1, 2): 9,
    ("A", 2, 1, 3): 27, ("A", 2, 1, 4): 81,
    # sl_4 at k=1: V_g = 4^g (all S_{0,j} = 1/2)
    ("A", 3, 1, 0): 1, ("A", 3, 1, 1): 4, ("A", 3, 1, 2): 16,
    ("A", 3, 1, 3): 64,
}


def known_verlinde(lie_type: str, rank: int, level: int, genus: int) -> Optional[int]:
    """Look up a known Verlinde number."""
    return _KNOWN_VERLINDE.get((lie_type, rank, level, genus))


# =========================================================================
# Section 15: Genus-1 comparison
# =========================================================================

def genus1_verlinde_vs_shadow(lie_type: str, rank: int, level: int) -> Dict[str, Any]:
    """Compare genus-1 Verlinde dimension with shadow F_1.

    V_{1,k} = |P_+^k| (number of integrable reps with d_lambda > 0).
    F_1 = kappa / 24.
    """
    # Count reps with nonzero quantum dimension
    weights = integrable_weights(lie_type, rank, level)
    n_nonzero = sum(
        1 for wt in weights
        if quantum_dim_weyl(wt, lie_type, rank, level) > 1e-10
    )

    n_total = len(weights)
    kap = kappa_affine(lie_type, rank, level)
    F1 = kap / 24.0

    return {
        "lie_type": lie_type, "rank": rank, "level": level,
        "V_1_nonzero_qdim": n_nonzero,
        "V_1_total_weights": n_total,
        "F_1": F1,
        "kappa": kap,
        "ratio_V1_F1": n_nonzero / F1 if abs(F1) > 1e-30 else None,
    }


# =========================================================================
# Section 16: Full diagnostic
# =========================================================================

def full_diagnostic(
    lie_type: str, rank: int, level: int, max_genus: int = 5,
) -> Dict[str, Any]:
    """Complete diagnostic for affine g-hat at level k."""
    data = _get_lie_data(lie_type, rank)
    result = {
        "algebra": data["name"],
        "lie_type": lie_type, "rank": rank, "level": level,
        "dim_g": data["dim"], "h_dual": data["hv"],
        "central_charge": central_charge(lie_type, rank, level),
        "kappa": kappa_affine(lie_type, rank, level),
        "num_integrable_reps": num_integrable_reps(lie_type, rank, level),
    }

    # S-matrix
    props = verify_S_matrix_properties(lie_type, rank, level)
    result["S_unitary"] = props["is_unitary"]
    result["S_00"] = props["S_00"]

    # Fusion
    fus = verify_fusion_integrality(lie_type, rank, level)
    result["fusion_ok"] = fus["all_nonneg_integer"]

    # Verlinde and shadow
    verlinde = {}
    shadow = {}
    for g in range(max_genus + 1):
        verlinde[g] = verlinde_dimension_exact(lie_type, rank, level, g)
        if g >= 1:
            shadow[g] = float(shadow_F_g(lie_type, rank, level, g))
    result["verlinde"] = verlinde
    result["shadow"] = shadow

    return result


# =========================================================================
# Section 17: Comprehensive multi-path verification
# =========================================================================

def comprehensive_verification(
    types_levels: Optional[List[Tuple[str, int, int]]] = None,
    max_genus: int = 5,
) -> List[Dict[str, Any]]:
    """Multi-path verification across types, levels, and genera.

    Path 1: S-matrix Verlinde formula
    Path 2: Quantum Weyl dimension formula (independent)
    Path 3: Known literature values
    Path 4: Genus-1 = integrable reps count
    Path 5: Shadow F_g = kappa * lambda_g^FP
    """
    if types_levels is None:
        types_levels = [
            ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
            ("A", 2, 1), ("A", 2, 2),
            ("A", 3, 1),
            ("B", 2, 1), ("C", 2, 1),
            ("D", 4, 1), ("G", 2, 1),
        ]

    results = []
    for (lt, r, lev) in types_levels:
        for g in range(max_genus + 1):
            rec = {"type": lt, "rank": r, "level": lev, "genus": g}

            # Path 1
            try:
                v1 = verlinde_dimension(lt, r, lev, g)
                rec["path1_Smatrix"] = v1
            except Exception as e:
                rec["path1_Smatrix"] = None
                v1 = None

            # Path 2
            try:
                v2 = verlinde_from_weyl_qdim(lt, r, lev, g)
                rec["path2_weyl"] = v2
            except Exception as e:
                rec["path2_weyl"] = None
                v2 = None

            # Path 3
            v3 = known_verlinde(lt, r, lev, g)
            rec["path3_known"] = v3

            # Path 4
            if g == 1 and v1 is not None:
                n_reps = num_integrable_reps(lt, r, lev)
                rec["path4_nreps"] = n_reps

            # Path 5
            if g >= 1:
                try:
                    F = float(shadow_F_g(lt, r, lev, g))
                    rec["path5_shadow"] = F
                except Exception:
                    rec["path5_shadow"] = None

            # Agreement
            if v1 is not None and v2 is not None:
                rec["paths_12_agree"] = abs(v1 - v2) < 0.5
            if v1 is not None and v3 is not None:
                rec["paths_13_agree"] = abs(v1 - v3) < 0.5

            results.append(rec)
    return results


# =========================================================================
# Section 18: sl_2 closed-form Verlinde (for fast verification)
# =========================================================================

def sl2_verlinde_closed_form(k: int, genus: int) -> float:
    """Closed-form Verlinde number for sl_2 at level k, genus g.

    V_{g,k} = sum_{j=0}^{k} S_{0,j}^{2-2g}

    where S_{0,j} = sqrt(2/(k+2)) * sin(pi*(j+1)/(k+2)).
    """
    n = k + 2
    power = 2 - 2 * genus
    total = 0.0
    for j in range(k + 1):
        s0j = math.sqrt(2.0 / n) * math.sin(math.pi * (j + 1) / n)
        if abs(s0j) > 1e-15:
            total += s0j ** power
    return total


# =========================================================================
# Section 19: Level-rank table
# =========================================================================

def level_rank_table(
    max_N: int = 5, max_k: int = 5, max_genus: int = 3,
) -> List[Dict[str, Any]]:
    """Build a table of level-rank duality checks."""
    results = []
    for N in range(2, max_N + 1):
        for k in range(2, max_k + 1):
            for g in range(max_genus + 1):
                results.append(level_rank_check(N, k, g))
    return results
