"""Hochschild-Serre E₁ computation for current algebras g[t].

Computes the E₁^{0,p} dimensions of the Strategy IV spectral sequence
for the current algebra g[t] at loop degrees p = 0,...,max_p.

From comp:current-algebra-E1 (yangians.tex): the E₁^{0,p} at root weight 0
and loop degree p equals dim H^*(g[t], k)_p, the total Lie algebra cohomology
of the polynomial current algebra at fixed loop degree.

METHOD: By the Loday-Quillen-Tsygan theorem (Feigin-Tsygan formulation for
semisimple Lie algebras), H*(g ⊗ k[t], k) is an exterior algebra on
generators at loop degrees {2e_i + 1 + 2n : i = 1,...,rank, n >= 0}
where e_1,...,e_r are the exponents of g.

Thus E₁^{0,p} = #{subsets of these generator degrees summing to p}.
This is computed via subset-sum dynamic programming.

NOTE: The naive approach of counting g-invariants in ⊗Λ^{mult}(g)
(without the CE differential) OVERCOUNTS: it gives [1,0,0,2,2,4] for
sl₂ instead of the correct [1,0,0,1,0,1]. The CE differential of
g[t] kills the excess invariants.

GROUND TRUTH (sl₂, dim=3, exponents={1}):
  E₁^{0,p} = 1, 0, 0, 1, 0, 1  at p = 0,...,5
  Generators at loop degrees: 3, 5, 7, 9, ...

sp₄ = C₂: dim=10, rank=2, h=4, h^∨=3, exponents={1,3}.
  Generators at loop degrees: {3,5,7,9,...} ∪ {7,9,11,...}
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from typing import Dict, List, Tuple

import numpy as np

from compute.lib.lie_algebra import (
    structure_constants_sl2,
    structure_constants_sl3,
)


# ---------------------------------------------------------------------------
# Lie algebra exponents
# ---------------------------------------------------------------------------

def lie_exponents(lie_type: str, rank: int) -> List[int]:
    """Return the exponents of a simple Lie algebra.

    Exponents = (fundamental degrees) - 1.
    A_n: {1,2,...,n}
    B_n: {1,3,5,...,2n-1}
    C_n: {1,3,5,...,2n-1}
    D_n: {1,3,...,2n-3,n-1}
    G_2: {1,5}
    F_4: {1,5,7,11}
    E_6: {1,4,5,7,8,11}
    E_7: {1,5,7,9,11,13,17}
    E_8: {1,7,11,13,17,19,23,29}
    """
    t = lie_type.upper()
    if t == 'A':
        return list(range(1, rank + 1))
    elif t == 'B':
        return list(range(1, 2 * rank, 2))
    elif t == 'C':
        return list(range(1, 2 * rank, 2))
    elif t == 'D':
        if rank < 3:
            raise ValueError("D_n requires n >= 3")
        return sorted(list(range(1, 2 * rank - 2, 2)) + [rank - 1])
    elif t == 'G' and rank == 2:
        return [1, 5]
    elif t == 'F' and rank == 4:
        return [1, 5, 7, 11]
    elif t == 'E':
        if rank == 6:
            return [1, 4, 5, 7, 8, 11]
        elif rank == 7:
            return [1, 5, 7, 9, 11, 13, 17]
        elif rank == 8:
            return [1, 7, 11, 13, 17, 19, 23, 29]
    raise ValueError(f"Unknown Lie type {lie_type}_{rank}")


def lie_dimension(lie_type: str, rank: int) -> int:
    """Dimension of the Lie algebra."""
    t = lie_type.upper()
    if t == 'A':
        return (rank + 1) ** 2 - 1
    elif t == 'B':
        return rank * (2 * rank + 1)
    elif t == 'C':
        return rank * (2 * rank + 1)
    elif t == 'D':
        return rank * (2 * rank - 1)
    elif t == 'G' and rank == 2:
        return 14
    elif t == 'F' and rank == 4:
        return 52
    elif t == 'E':
        return {6: 78, 7: 133, 8: 248}[rank]
    raise ValueError(f"Unknown Lie type {lie_type}_{rank}")


# ---------------------------------------------------------------------------
# E₁ computation via LQT generating function
# ---------------------------------------------------------------------------

def generator_loop_degrees(exponents: List[int], max_p: int) -> List[int]:
    """Loop degrees of all LQT generators up to max_p.

    For each exponent e, generators appear at loop degrees
    2e+1, 2e+3, 2e+5, ... (odd numbers >= 2e+1).

    Returns a sorted list (may contain repeats from different exponents).
    """
    gens = []
    for e in exponents:
        n = 0
        while True:
            d = 2 * e + 1 + 2 * n
            if d > max_p:
                break
            gens.append(d)
            n += 1
    return sorted(gens)


def e1_dims_from_generators(generators: List[int], max_p: int) -> List[int]:
    """Count subsets of generators summing to each p = 0,...,max_p.

    Standard 0-1 knapsack / subset-sum DP.
    Each generator is used at most once (exterior algebra).
    """
    dp = [0] * (max_p + 1)
    dp[0] = 1
    for g in generators:
        for p in range(max_p, g - 1, -1):
            dp[p] += dp[p - g]
    return dp


def e1_dims(lie_type: str, rank: int, max_p: int = 5) -> List[int]:
    """E₁^{0,p} for g[t] at loop degrees p = 0,...,max_p.

    Uses LQT theorem: exterior algebra on generators at
    loop degrees {2e_i+1+2n : i=1,...,rank, n>=0}.
    """
    exps = lie_exponents(lie_type, rank)
    gens = generator_loop_degrees(exps, max_p)
    return e1_dims_from_generators(gens, max_p)


def e1_generating_function_coeffs(lie_type: str, rank: int,
                                   max_p: int) -> List[int]:
    """Same as e1_dims but named to emphasize it's a GF computation."""
    return e1_dims(lie_type, rank, max_p)


# ---------------------------------------------------------------------------
# Convenience wrappers
# ---------------------------------------------------------------------------

def e1_dims_sl2(max_p: int = 5) -> List[int]:
    """E₁^{0,p} for sl₂[t]. Expected: [1, 0, 0, 1, 0, 1] at p=0,...,5."""
    return e1_dims('A', 1, max_p)


def e1_dims_sl3(max_p: int = 5) -> List[int]:
    """E₁^{0,p} for sl₃[t]. Exponents {1,2}, generators at {3,5,7,...}∪{5,7,...}."""
    return e1_dims('A', 2, max_p)


def e1_dims_sp4(max_p: int = 5) -> List[int]:
    """E₁^{0,p} for sp₄[t] (= C₂). Exponents {1,3}, generators at {3,5,...}∪{7,9,...}."""
    return e1_dims('C', 2, max_p)


# ---------------------------------------------------------------------------
# Growth rate analysis
# ---------------------------------------------------------------------------

def polynomial_growth_bound(dims: List[int]) -> str:
    """Analyze growth rate of E₁^{0,p} sequence.

    Returns a string describing the observed growth.
    Polynomial growth of E₁^{0,p} is the key claim for Strategy IV.
    """
    nonzero = [(p, d) for p, d in enumerate(dims) if d > 0 and p > 0]
    if len(nonzero) < 3:
        return "insufficient data"

    # Fit log(d) vs log(p) for nonzero values
    import math
    log_p = [math.log(p) for p, d in nonzero]
    log_d = [math.log(d) for p, d in nonzero]

    if len(set(log_d)) == 1:
        return "constant (all nonzero values equal)"

    # Simple linear regression
    n = len(log_p)
    sx = sum(log_p)
    sy = sum(log_d)
    sxx = sum(x * x for x in log_p)
    sxy = sum(x * y for x, y in zip(log_p, log_d))
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-10:
        return "degenerate"
    slope = (n * sxy - sx * sy) / denom
    return f"polynomial, approx degree {slope:.2f}"


# ---------------------------------------------------------------------------
# sp₄ structure constants (Chevalley basis) — for independent verification
# ---------------------------------------------------------------------------

# Indices: e₁=0, e₂=1, e₁₂=2, e₂₁₂=3, h₁=4, h₂=5, f₁=6, f₂=7, f₁₂=8, f₂₁₂=9

def structure_constants_sp4_int() -> Dict[Tuple[int, int], Dict[int, float]]:
    """Structure constants for sp₄ (= C₂) in Chevalley basis.

    C₂ Cartan: [[2,-2],[-1,2]]. Roots: α₁(short), α₂(long),
    α₁+α₂(short), 2α₁+α₂(long).

    10 generators: e₁, e₂, e₁₂=[e₁,e₂], e₂₁₂=[e₁,e₁₂],
                   h₁, h₂, f₁, f₂, f₁₂, f₂₁₂.
    """
    sc: Dict[Tuple[int, int], Dict[int, float]] = {}

    e1, e2, e12, e212, h1, h2, f1, f2, f12, f212 = range(10)

    def _add(a, b, result):
        sc[(a, b)] = result
        sc[(b, a)] = {k: -v for k, v in result.items()}

    # Cartan on simple roots: [h_i, e_j] = a_{ij} e_j
    _add(h1, e1, {e1: 2})
    _add(h1, e2, {e2: -2})
    _add(h2, e1, {e1: -1})
    _add(h2, e2, {e2: 2})

    _add(h1, f1, {f1: -2})
    _add(h1, f2, {f2: 2})
    _add(h2, f1, {f1: 1})
    _add(h2, f2, {f2: -2})

    # Cartan on composite roots
    _add(h1, e12, {e12: 0})
    _add(h2, e12, {e12: 1})
    _add(h1, e212, {e212: 2})
    _add(h2, e212, {e212: 0})

    _add(h1, f12, {f12: 0})
    _add(h2, f12, {f12: -1})
    _add(h1, f212, {f212: -2})
    _add(h2, f212, {f212: 0})

    # Positive root brackets
    _add(e1, e2, {e12: 1})
    _add(e1, e12, {e212: 2})

    # Negative root brackets
    _add(f2, f1, {f12: 1})
    _add(f12, f1, {f212: 2})

    # Simple ef brackets
    _add(e1, f1, {h1: 1})
    _add(e2, f2, {h2: 1})

    # Mixed ef brackets (derived from Jacobi)
    _add(e12, f1, {e2: -2})
    _add(e12, f2, {e1: 1})
    _add(e12, f12, {h1: 1, h2: 2})
    _add(e212, f1, {e12: -1})  # [[e1,e12],f1]=-2e12, [e1,e12]=2e212 → [e212,f1]=-e12
    _add(e212, f12, {e1: 1})   # Jacobi (e1,e12,f12): 2[e212,f12]=2e1 → [e212,f12]=e1
    _add(e212, f212, {h1: 1, h2: 1})
    _add(e1, f12, {f2: -2})
    _add(e2, f12, {f1: 1})
    _add(e1, f212, {f12: -1})
    _add(e12, f212, {f1: 1})

    return sc


# ---------------------------------------------------------------------------
# Generic Lie algebra tools (for verification)
# ---------------------------------------------------------------------------

def adjoint_matrices_from_sc(dim_g: int,
                              sc: Dict[Tuple, Dict]) -> List[np.ndarray]:
    """Build adjoint representation matrices from structure constants."""
    mats = []
    for a in range(dim_g):
        M = np.zeros((dim_g, dim_g), dtype=float)
        for b in range(dim_g):
            entry = sc.get((a, b), {})
            for c, val in entry.items():
                M[c, b] = float(val)
        mats.append(M)
    return mats


def verify_jacobi_generic(dim_g: int, sc: Dict) -> bool:
    """Verify Jacobi identity for structure constants."""
    mats = adjoint_matrices_from_sc(dim_g, sc)
    for a in range(dim_g):
        for b in range(dim_g):
            comm = mats[a] @ mats[b] - mats[b] @ mats[a]
            ad_ab = np.zeros((dim_g, dim_g), dtype=float)
            for c, val in sc.get((a, b), {}).items():
                ad_ab += val * mats[c]
            if not np.allclose(comm, ad_ab, atol=1e-10):
                return False
    return True


def killing_form(dim_g: int, ad_mats: List[np.ndarray]) -> np.ndarray:
    """Killing form κ(a,b) = Tr(ad(a)·ad(b))."""
    K = np.zeros((dim_g, dim_g))
    for a in range(dim_g):
        for b in range(a, dim_g):
            K[a, b] = np.trace(ad_mats[a] @ ad_mats[b])
            K[b, a] = K[a, b]
    return K


def sp4_ad_mats() -> List[np.ndarray]:
    """Adjoint matrices for sp₄."""
    return adjoint_matrices_from_sc(10, structure_constants_sp4_int())


def _perm_sign(perm: List[int], target: List[int]) -> int:
    """Sign of permutation taking perm to target."""
    pos = {v: i for i, v in enumerate(target)}
    p = [pos[v] for v in perm]
    inv = sum(1 for i in range(len(p))
              for j in range(i + 1, len(p)) if p[i] > p[j])
    return (-1) ** inv


def exterior_power_action(k: int,
                           ad_mats: List[np.ndarray]) -> List[np.ndarray]:
    """Action of each generator on Λ^k(g)."""
    dim_g = len(ad_mats)
    if k > dim_g or k < 0:
        return [np.zeros((0, 0)) for _ in range(dim_g)]
    basis = list(combinations(range(dim_g), k))
    basis_idx = {b: i for i, b in enumerate(basis)}
    n = len(basis)

    result = []
    for a in range(dim_g):
        M = np.zeros((n, n), dtype=float)
        ad_a = ad_mats[a]
        for col, indices in enumerate(basis):
            for j in range(k):
                for c in range(dim_g):
                    coeff = ad_a[indices[j], c]
                    if abs(coeff) < 1e-15:
                        continue
                    new_list = list(indices)
                    new_list[j] = c
                    if len(set(new_list)) < k:
                        continue
                    sorted_new = sorted(new_list)
                    sign = _perm_sign(new_list, sorted_new)
                    tgt = tuple(sorted_new)
                    if tgt in basis_idx:
                        M[basis_idx[tgt], col] += coeff * sign
        result.append(M)
    return result


def ce_cohomology_dims(dim_g: int, ad_mats: List[np.ndarray]) -> List[int]:
    """Compute H^n(g) = dim of g-invariant n-forms (for semisimple g)."""
    dims = []
    for p in range(dim_g + 1):
        ext_mats = exterior_power_action(p, ad_mats)
        if not ext_mats or ext_mats[0].shape[0] == 0:
            dims.append(1 if p == dim_g else 0)
            continue
        big = np.vstack(ext_mats)
        rank = np.linalg.matrix_rank(big, tol=1e-8)
        inv_dim = ext_mats[0].shape[0] - rank
        dims.append(inv_dim)
    return dims


# ---------------------------------------------------------------------------
# sl₂ / sl₃ structure constants (integer-indexed)
# ---------------------------------------------------------------------------

def structure_constants_sl2_int() -> Dict[Tuple[int, int], Dict[int, float]]:
    """sl₂ structure constants with integer indices: e=0, h=1, f=2."""
    sc_str = structure_constants_sl2()
    idx = {"e": 0, "h": 1, "f": 2}
    sc = {}
    for (a, b), coeffs in sc_str.items():
        sc[(idx[a], idx[b])] = {idx[c]: float(v) for c, v in coeffs.items()}
    return sc


def sl2_ad_mats() -> List[np.ndarray]:
    """Adjoint matrices for sl₂."""
    return adjoint_matrices_from_sc(3, structure_constants_sl2_int())
