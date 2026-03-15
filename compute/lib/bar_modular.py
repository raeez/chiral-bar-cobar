"""Modular arithmetic computations for sl_3 bar complex infrastructure.

WARNING: The CHIRAL bar differential d = d_bracket + d_curvature requires the
full Borcherds identity (all OPE poles). The bracket-only piece d_bracket
provably has d_bracket^2 != 0 (verified for all 2048 sign conventions).
Do NOT attempt to compute chiral bar cohomology by building d_bracket as a matrix.

Correct approach: PBW spectral sequence + Koszul dual Hilbert series.
See chiral_koszul_pairs.tex: thm:pbw-koszulness-criterion.

This module provides:
  1. Orlik-Solomon (NBC basis) dimension tables
  2. Chevalley-Eilenberg cohomology of sl_3 over F_p (d_CE^2 = 0)
  3. Bar complex dimension tables (without differential)
  4. sl_3 structure constants and Killing form over F_p

References: PROGRAMMES.md Programme IX, CLAUDE.md "Bar Differential" section.
"""

from __future__ import annotations

import numpy as np
from typing import Dict, List, Optional, Tuple
from itertools import combinations, product as cartprod


# ==========================================================================
# sl_3 data (hardcoded for speed — no sympy)
# ==========================================================================

DIM_G = 8
# Generator indices: H1=0, H2=1, E1=2, E2=3, E3=4, F1=5, F2=6, F3=7
H1, H2, E1, E2, E3, F1, F2, F3 = range(8)

# Structure constants [a, b] = sum_c f^c_{ab} * gen_c
# Stored as dict: (a, b) -> list of (c, f^c_{ab})
_BRACKET: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}


def _init_bracket():
    """Initialize sl_3 structure constants (integer coefficients)."""
    global _BRACKET
    if _BRACKET:
        return

    b = {}
    CARTAN = [[2, -1], [-1, 2]]

    # [H_i, E_j] = A_{ij} * E_j
    for i, hi in enumerate([H1, H2]):
        for j, ej in enumerate([E1, E2]):
            a_ij = CARTAN[i][j]
            if a_ij != 0:
                b[(hi, ej)] = [(ej, a_ij)]
                b[(ej, hi)] = [(ej, -a_ij)]

    # [H_i, F_j] = -A_{ij} * F_j
    for i, hi in enumerate([H1, H2]):
        for j, fj in enumerate([F1, F2]):
            a_ij = CARTAN[i][j]
            if a_ij != 0:
                b[(hi, fj)] = [(fj, -a_ij)]
                b[(fj, hi)] = [(fj, a_ij)]

    # [H_i, E_3], [H_i, F_3]: root alpha_1 + alpha_2
    b[(H1, E3)] = [(E3, 1)]; b[(E3, H1)] = [(E3, -1)]
    b[(H2, E3)] = [(E3, 1)]; b[(E3, H2)] = [(E3, -1)]
    b[(H1, F3)] = [(F3, -1)]; b[(F3, H1)] = [(F3, 1)]
    b[(H2, F3)] = [(F3, -1)]; b[(F3, H2)] = [(F3, 1)]

    # [E_i, F_j]
    b[(E1, F1)] = [(H1, 1)]; b[(F1, E1)] = [(H1, -1)]
    b[(E2, F2)] = [(H2, 1)]; b[(F2, E2)] = [(H2, -1)]
    b[(E1, E2)] = [(E3, 1)]; b[(E2, E1)] = [(E3, -1)]
    b[(F2, F1)] = [(F3, 1)]; b[(F1, F2)] = [(F3, -1)]

    # E_3 with F_i
    b[(E3, F1)] = [(E2, -1)]; b[(F1, E3)] = [(E2, 1)]
    b[(E3, F2)] = [(E1, 1)]; b[(F2, E3)] = [(E1, -1)]
    b[(E3, F3)] = [(H1, 1), (H2, 1)]; b[(F3, E3)] = [(H1, -1), (H2, -1)]

    # E_i with F_3
    b[(E1, F3)] = [(F2, -1)]; b[(F3, E1)] = [(F2, 1)]
    b[(E2, F3)] = [(F1, 1)]; b[(F3, E2)] = [(F1, -1)]

    _BRACKET = b


# Killing form: (H_i, H_j) = A_{ij}, (E_i, F_i) = 1
_KILLING: Dict[Tuple[int, int], int] = {
    (H1, H1): 2, (H1, H2): -1, (H2, H1): -1, (H2, H2): 2,
    (E1, F1): 1, (F1, E1): 1,
    (E2, F2): 1, (F2, E2): 1,
    (E3, F3): 1, (F3, E3): 1,
}


def bracket_mod_p(a: int, b: int, p: int) -> List[Tuple[int, int]]:
    """[a, b] mod p. Returns list of (gen_index, coefficient mod p)."""
    _init_bracket()
    terms = _BRACKET.get((a, b), [])
    return [(c, coeff % p) for c, coeff in terms]


def killing_mod_p(a: int, b: int, p: int) -> int:
    """(a, b) mod p."""
    return _KILLING.get((a, b), 0) % p


# ==========================================================================
# Orlik-Solomon algebra (NBC basis) over integers
# ==========================================================================

def nbc_basis(n: int, k: int) -> List[Tuple[Tuple[int, int], ...]]:
    """No-Broken-Circuit basis for OS^k(n) of the braid arrangement.

    Points labeled 0, ..., n-1. Circuit-breaking order: lex on (i,j).
    A broken circuit: remove the lex-smallest edge from each 3-cycle.
    NBC = k-element edge sets containing no broken circuit.
    """
    if k == 0:
        return [()]
    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]

    # Broken circuits: for each 3-cycle, the broken circuit is
    # {(i,m), (j,m)} (remove smallest edge (i,j) from triangle)
    broken_circuits = set()
    for i in range(n):
        for j in range(i + 1, n):
            for m in range(j + 1, n):
                broken_circuits.add(frozenset({(i, m), (j, m)}))

    result = []
    for combo in combinations(all_edges, k):
        combo_set = frozenset(combo)
        is_nbc = True
        for bc in broken_circuits:
            if bc.issubset(combo_set):
                is_nbc = False
                break
        if is_nbc:
            result.append(combo)

    return result


def os_dimension(n: int, k: int) -> int:
    """Dimension of OS^k(n) = |s(n, n-k)| (unsigned Stirling 1st kind)."""
    return len(nbc_basis(n, k))


# ==========================================================================
# Bar complex dimension tables (NO differential — see module docstring)
# ==========================================================================

def bar_dimension(degree: int, dim_g: int = DIM_G) -> int:
    """Dimension of B^degree = dim_g^degree * |NBC^{degree-1}(degree)|.

    This is the dimension of the chain space, NOT the cohomology.
    Computing the cohomology requires the full chiral differential
    (PBW spectral sequence), not just the bracket piece.
    """
    return dim_g ** degree * os_dimension(degree, degree - 1)


def bar_dimension_table(max_degree: int = 6, dim_g: int = DIM_G) -> Dict[int, int]:
    """Table of bar complex chain space dimensions."""
    return {n: bar_dimension(n, dim_g) for n in range(1, max_degree + 1)}


# ==========================================================================
# Chevalley-Eilenberg cohomology over F_p
# ==========================================================================

def ce_differential_mod_p(
    degree: int,
    p: int,
    dim_g: int = DIM_G,
) -> np.ndarray:
    """Build CE differential d: C^degree(sl_3) -> C^{degree+1}(sl_3) over F_p.

    C^k(g) = Lambda^k(g*), with basis = k-element subsets of {0,...,dim_g-1}.
    The CE differential is:
      (df)(x_0,...,x_k) = sum_{i<j} (-1)^{i+j} f([x_i,x_j], x_0,...,hat_i,...,hat_j,...,x_k)

    This DOES satisfy d^2 = 0 (standard Lie algebra cohomology).
    """
    source_basis = list(combinations(range(dim_g), degree))
    target_basis = list(combinations(range(dim_g), degree + 1))
    n_source = len(source_basis)
    n_target = len(target_basis)

    source_idx = {s: i for i, s in enumerate(source_basis)}
    target_idx = {t: i for i, t in enumerate(target_basis)}

    D = np.zeros((n_target, n_source), dtype=np.int64)

    _init_bracket()

    # For each target basis element (a_0, ..., a_k) in Lambda^{k+1},
    # and each pair (i, j) with i < j:
    #   bracket [a_i, a_j] = sum_c f^c_{a_i, a_j} * c
    #   replace a_i, a_j with c in the remaining tuple
    #   find the resulting element in source basis
    for col, src in enumerate(source_basis):
        # Apply d to src = (a_0, ..., a_{k-1}) in Lambda^k
        # d(src)(x_0, ..., x_k) involves all (k+1)-tuples
        # Better: use the dual formula.
        # d(e^{i_1} ^ ... ^ e^{i_k}) = sum_{a<b} f^{i_?}_{ab} * ...
        # Actually, let's use the direct formula on the exterior algebra:
        #
        # For omega in Lambda^k(g*), d(omega) in Lambda^{k+1}(g*) is:
        # d(omega)(g_0,...,g_k) = sum_{i<j} (-1)^{i+j} omega([g_i,g_j], g_0,...,^i,...,^j,...,g_k)
        #
        # In terms of basis: if omega = e^{a_1} ^ ... ^ e^{a_k},
        # then d(omega) = -sum_{c < d, m} f^{a_m}_{cd} * e^{a_1}^...^e^{c}^...^e^{a_k} ^ e^{d}
        # where we replace a_m by c and wedge in d.
        #
        # Equivalently, using structure constants directly:
        pass

    # Simpler approach: build the matrix by evaluating on basis elements.
    # d: Lambda^k -> Lambda^{k+1} via the transpose of the Lie bracket.
    #
    # For f^c_{ab} (structure constants), the CE differential on Lambda^*(g*) is:
    # d(e^c) = -1/2 sum_{a,b} f^c_{ab} e^a ^ e^b
    # d extends to Lambda^k by the Leibniz rule.
    #
    # So for degree 1 -> 2:
    # d(e^c) = -1/2 sum_{a<b} (f^c_{ab} - f^c_{ba}) e^a ^ e^b
    #        = -sum_{a<b} f^c_{ab} e^a ^ e^b  (since f^c_{ba} = -f^c_{ab})
    #
    # For general degree k -> k+1, use:
    # d(e^{i_1} ^ ... ^ e^{i_k}) = sum_m (-1)^{m-1} d(e^{i_m}) ^ e^{i_1} ^ ... ^ ^{i_m} ^ ... ^ e^{i_k}

    D = np.zeros((n_target, n_source), dtype=np.int64)

    # Precompute d on degree 1: d(e^c) = -sum_{a<b} f^c_{ab} e^a ^ e^b
    d1 = {}  # c -> list of ((a, b), coeff) with a < b
    for c in range(dim_g):
        terms = []
        for a in range(dim_g):
            for b in range(a + 1, dim_g):
                # f^c_{ab}
                fc = 0
                for gen, coeff in _BRACKET.get((a, b), []):
                    if gen == c:
                        fc = coeff
                if fc != 0:
                    terms.append(((a, b), -fc))
        d1[c] = terms

    for col, src in enumerate(source_basis):
        src_list = list(src)
        k = len(src_list)

        for m in range(k):
            # Apply d to e^{src[m]}, wedge with the rest
            sign_m = (-1) ** m
            c = src_list[m]
            rest = src_list[:m] + src_list[m + 1:]

            for (a, b), coeff in d1[c]:
                # Result: e^a ^ e^b wedged with rest (excluding position m)
                # Need to sort into canonical order and track sign
                new_elements = [a, b] + rest
                # Check for duplicates
                if len(set(new_elements)) < len(new_elements):
                    continue
                # Sort and compute sign of permutation
                target_sorted = tuple(sorted(new_elements))
                perm_sign = _perm_sign(new_elements, target_sorted)
                if perm_sign == 0:
                    continue

                if target_sorted in target_idx:
                    row = target_idx[target_sorted]
                    total_coeff = sign_m * coeff * perm_sign
                    D[row, col] = (D[row, col] + total_coeff) % p

    return D


def _perm_sign(perm: list, target: tuple) -> int:
    """Sign of the permutation that sorts perm into target.

    Returns +1 or -1, or 0 if there are duplicates.
    """
    n = len(perm)
    if len(set(perm)) < n:
        return 0

    # Map target positions
    pos = {v: i for i, v in enumerate(target)}
    arr = [pos[v] for v in perm]

    # Count inversions
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return (-1) ** inv


def matrix_rank_mod_p(M: np.ndarray, p: int) -> int:
    """Compute rank of integer matrix M modulo prime p using Gaussian elimination."""
    M = M.copy() % p
    rows, cols = M.shape
    pivot_row = 0

    for col in range(cols):
        if pivot_row >= rows:
            break

        # Find pivot
        found = False
        for row in range(pivot_row, rows):
            if M[row, col] % p != 0:
                found = True
                M[[pivot_row, row]] = M[[row, pivot_row]]
                break

        if not found:
            continue

        # Eliminate
        inv = pow(int(M[pivot_row, col]), p - 2, p)  # Fermat's little theorem
        M[pivot_row] = (M[pivot_row] * inv) % p

        for row in range(rows):
            if row != pivot_row and M[row, col] % p != 0:
                factor = M[row, col] % p
                M[row] = (M[row] - factor * M[pivot_row]) % p

        pivot_row += 1

    return pivot_row


def ce_cohomology_dims_mod_p(
    p: int,
    dim_g: int = DIM_G,
    max_degree: int = None,
) -> Dict[int, int]:
    """Compute all CE cohomology dimensions H^k(sl_3) mod p.

    Returns dict: degree -> dimension.
    Known answer: H*(sl_3) = Lambda(x_3, x_5), so
      H^0=1, H^3=1, H^5=1, H^8=1, all others=0.
    """
    if max_degree is None:
        max_degree = dim_g

    ranks = {}
    for k in range(max_degree + 1):
        if k == 0:
            D = ce_differential_mod_p(0, p, dim_g)
            ranks[0] = matrix_rank_mod_p(D, p)
        elif k <= dim_g:
            D = ce_differential_mod_p(k, p, dim_g)
            ranks[k] = matrix_rank_mod_p(D, p)

    dims = {}
    from math import comb
    for k in range(max_degree + 1):
        chain_dim = comb(dim_g, k)
        rank_dk = ranks.get(k, 0) if k <= dim_g else 0
        rank_dk_minus_1 = ranks.get(k - 1, 0) if k >= 1 else 0
        dims[k] = chain_dim - rank_dk - rank_dk_minus_1

    return dims


def verify_ce_cohomology(primes: List[int] = None) -> Dict[str, bool]:
    """Verify CE cohomology of sl_3 against known values.

    H*(sl_3, C) = Lambda(x_3, x_5):
      H^0=1, H^3=1, H^5=1, H^8=1, all others=0.
    """
    if primes is None:
        primes = [5, 7, 11]

    known = {0: 1, 1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 0, 8: 1}
    results = {}

    for p in primes:
        dims = ce_cohomology_dims_mod_p(p, max_degree=8)
        for k, expected in known.items():
            key = f"H^{k}(sl_3) mod {p}: expected {expected}, got {dims.get(k, '?')}"
            results[key] = (dims.get(k, -1) == expected)

    return results


def verify_d_squared_ce(degree: int, p: int, dim_g: int = DIM_G) -> bool:
    """Verify d^2 = 0 for the CE differential at given degree mod p."""
    if degree + 1 > dim_g:
        return True  # d_{degree+1} is zero
    D_k = ce_differential_mod_p(degree, p, dim_g)
    D_kp1 = ce_differential_mod_p(degree + 1, p, dim_g)
    product = (D_kp1 @ D_k) % p
    return np.all(product == 0)


# ==========================================================================
# Dimension tables and summary
# ==========================================================================

def print_dimension_table(max_degree: int = 6):
    """Print bar complex chain space dimensions and OS dimensions."""
    print("Bar complex chain space dimensions for sl_3 (dim g = 8):")
    print(f"{'degree':>8} {'OS dim':>10} {'B^n dim':>12}")
    print("-" * 32)
    for n in range(1, max_degree + 1):
        os_dim = os_dimension(n, n - 1)
        b_dim = bar_dimension(n)
        print(f"{n:>8} {os_dim:>10} {b_dim:>12}")
    print()
    print("NOTE: These are chain space dimensions, NOT cohomology.")
    print("Cohomology requires the full chiral differential (PBW spectral sequence).")
