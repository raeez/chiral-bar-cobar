"""Chiral bar complex: full differential with OS forms on configuration spaces.

The chiral bar complex for a Kac-Moody algebra g-hat_k at genus 0 is:

  B-bar^n = g^{tensor n} ⊗ OS^{n-1}(Conf_n(C))

where OS^{n-1} is the top-degree part of the Orlik-Solomon algebra.
The chain group has dimension dim(g)^n × (n-1)!.

DIFFERENTIAL STRUCTURE:

The bar differential d: B-bar^n → B-bar^{n-1} is:

  d = Σ_{1≤i<j≤n} bracket_{ij} ⊗ Res_{ij}

where:
  - bracket_{ij}: g^{⊗n} → g^{⊗(n-1)} applies Lie bracket [e_{a_i}, e_{a_j}],
    placing the result at position i and removing position j.
  - Res_{ij}: OS^{n-1}(n) → OS^{n-2}(n-1) is the Poincaré residue
    map that extracts the coefficient of dlog(z_i - z_j).

d^2 = 0 follows from the Borcherds identity: the Jacobi identity for the
bracket is supplemented by the Arnold relations in the OS algebra to give
complete cancellation of all iterated-residue terms (Cases (i)-(iii) of
Theorem thm:bar-nilpotency-complete).

IMPORTANT NOTES:
  - On g^{⊗n} ALONE (without OS forms), bracket^2 ≠ 0 (proved, all 2048 signs)
  - On g^{⊗n} ⊗ OS^{n-1}(n), the combined bracket ⊗ Res DOES give d^2 = 0
  - For weight-1 generators, the double-pole (curvature) OPE coefficient
    kappa(a,b)|0> maps to the vacuum, which is quotiented out in A-bar.
    However, the curvature enters implicitly through the OS form structure:
    the Arnold relations encode the triple-collision contributions that
    compensate d_bracket^2 ≠ 0 on bare tensors.

SIGN CONVENTION:
  The sign is built into two places:
  1. The antisymmetry of the Lie bracket: [a,b] = -[b,a]
  2. The OS residue sign: Res_{ij}(... ∧ η_{ij} ∧ ...) picks up (-1)^{position}

  We allow a global sign parameter for each pair (i,j) to systematically
  search for the correct convention if needed.

CONVENTIONS:
  - Cohomological grading: |d| = +1
  - Points 1-indexed: {1, ..., n}
  - Tensor indices 0-indexed: {0, ..., dim_g-1}
  - Basis ordering: flat = tensor_flat * os_dim + os_idx
"""

from __future__ import annotations

import numpy as np
from typing import Dict, List, Optional, Tuple
from itertools import combinations
from math import factorial

from .os_algebra import os_dimension, os_basis, residue_map


# ===========================================================================
# Lie algebra data
# ===========================================================================

def sl2_data() -> Tuple[int, Dict, Dict]:
    """Structure constants and Killing form for sl_2.

    Basis: e=0, h=1, f=2.
    Brackets: [e,f]=h, [h,e]=2e, [h,f]=-2f.
    Killing form (normalized): kappa(e,f) = kappa(f,e) = 1, kappa(h,h) = 2.
    """
    sc = {
        (0, 2): {1: 1},   # [e,f] = h
        (2, 0): {1: -1},  # [f,e] = -h
        (1, 0): {0: 2},   # [h,e] = 2e
        (0, 1): {0: -2},  # [e,h] = -2e
        (1, 2): {2: -2},  # [h,f] = -2f
        (2, 1): {2: 2},   # [f,h] = 2f
    }
    kf = {
        (0, 2): 1, (2, 0): 1,
        (1, 1): 2,
    }
    return 3, sc, kf


def sl3_data() -> Tuple[int, Dict, Dict]:
    """Structure constants and Killing form for sl_3.

    Basis (8 generators): Chevalley basis
    e1=0, e2=1, e12=2, f1=3, f2=4, f12=5, h1=6, h2=7
    where e12 = [e1,e2], f12 = [f2,f1].
    """
    # Cartan matrix of sl_3: [[2,-1],[-1,2]]
    sc = {}

    # [e1, f1] = h1
    sc[(0, 3)] = {6: 1}
    sc[(3, 0)] = {6: -1}
    # [e2, f2] = h2
    sc[(1, 4)] = {7: 1}
    sc[(4, 1)] = {7: -1}
    # [e1, e2] = e12
    sc[(0, 1)] = {2: 1}
    sc[(1, 0)] = {2: -1}
    # [f2, f1] = f12
    sc[(4, 3)] = {5: 1}
    sc[(3, 4)] = {5: -1}
    # [e12, f1] = -e2 (from Serre relations)
    # Actually: [e12, f1] = [[e1,e2],f1] = [e1,[e2,f1]] + [[e1,f1],e2]
    # [e2,f1] = 0 (different simple roots), [e1,f1] = h1
    # So [e12, f1] = 0 + [h1, e2] = -e2
    sc[(2, 3)] = {1: -1}
    sc[(3, 2)] = {1: 1}
    # [e12, f2] = e1 (similarly)
    # [e12, f2] = [[e1,e2],f2] = [e1,[e2,f2]] + [[e1,f2],e2]
    # [e2,f2] = h2, [e1,f2] = 0
    # So [e12, f2] = [e1, h2] = -(-1)*e1 = e1
    sc[(2, 4)] = {0: 1}
    sc[(4, 2)] = {0: -1}
    # [e1, f12] = -f2
    # [e1, f12] = [e1,[f2,f1]] = [[e1,f2],f1] + [f2,[e1,f1]]
    # [e1,f2] = 0, [e1,f1] = h1
    # = 0 + [f2, h1] = -[h1,f2] = -(-(-1)f2) ... need Cartan: [h1,f2] = f2 (since a_{12}=-1)
    # Actually [h1, f2] = -a_{12} f2 = -(-1)f2 = f2
    # So [e1, f12] = [f2, h1] = -[h1, f2] = -f2
    sc[(0, 5)] = {4: -1}
    sc[(5, 0)] = {4: 1}
    # [e2, f12] = f1
    # [e2, f12] = [e2,[f2,f1]] = [[e2,f2],f1] + [f2,[e2,f1]]
    # [e2,f2] = h2, [e2,f1] = 0
    # = [h2, f1] + 0 = -a_{21} * (-f1) ... [h2,f1] = -a_{21}f1 = f1
    # Wait: [h2, f1] = -a_{21} f1. For sl_3: a_{21} = -1. So [h2,f1] = f1.
    sc[(1, 5)] = {3: 1}
    sc[(5, 1)] = {3: -1}
    # [e12, f12] = h1 + h2
    # [e12, f12] = [[e1,e2],[f2,f1]] ... by Jacobi and previous:
    # = [e1, [e2, f12]] + [e2, [e12, f1]] ... hmm, need to be careful
    # Actually: [e12, f12] = h1 + h2 (standard result for sl_3)
    sc[(2, 5)] = {6: 1, 7: 1}
    sc[(5, 2)] = {6: -1, 7: -1}

    # Cartan-generator brackets
    # [h1, e1] = 2e1, [h1, e2] = -e2, [h1, e12] = e12
    sc[(6, 0)] = {0: 2}
    sc[(0, 6)] = {0: -2}
    sc[(6, 1)] = {1: -1}
    sc[(1, 6)] = {1: 1}
    sc[(6, 2)] = {2: 1}
    sc[(2, 6)] = {2: -1}
    # [h1, f1] = -2f1, [h1, f2] = f2, [h1, f12] = -f12
    sc[(6, 3)] = {3: -2}
    sc[(3, 6)] = {3: 2}
    sc[(6, 4)] = {4: 1}
    sc[(4, 6)] = {4: -1}
    sc[(6, 5)] = {5: -1}
    sc[(5, 6)] = {5: 1}

    # [h2, e1] = -e1, [h2, e2] = 2e2, [h2, e12] = e12
    sc[(7, 0)] = {0: -1}
    sc[(0, 7)] = {0: 1}
    sc[(7, 1)] = {1: 2}
    sc[(1, 7)] = {1: -2}
    sc[(7, 2)] = {2: 1}
    sc[(2, 7)] = {2: -1}
    # [h2, f1] = f1, [h2, f2] = -2f2, [h2, f12] = -f12
    sc[(7, 3)] = {3: 1}
    sc[(3, 7)] = {3: -1}
    sc[(7, 4)] = {4: -2}
    sc[(4, 7)] = {4: 2}
    sc[(7, 5)] = {5: -1}
    sc[(5, 7)] = {5: 1}

    # [h1, h2] = 0 (Cartan is abelian)
    # No entry needed

    # Killing form: kappa = trace form / (2 * h_dual) where h_dual = 3
    # For sl_3 with Chevalley basis:
    # kappa(e_alpha, f_alpha) = 1 for each root
    # kappa(h_i, h_j) = A_{ij} (Cartan matrix entries... actually need inverse)
    # The normalized Killing form: kappa(e_i, f_i) for simple roots = 1
    kf = {
        (0, 3): 1, (3, 0): 1,  # (e1, f1)
        (1, 4): 1, (4, 1): 1,  # (e2, f2)
        (2, 5): 1, (5, 2): 1,  # (e12, f12)
        (6, 6): 2, (7, 7): 2,  # (h1, h1), (h2, h2)
        (6, 7): -1, (7, 6): -1,  # (h1, h2)
    }

    return 8, sc, kf


# ===========================================================================
# Core index arithmetic
# ===========================================================================

def _multi_to_flat(indices: Tuple[int, ...], dim_g: int) -> int:
    """Convert multi-index to flat tensor index."""
    flat = 0
    for idx in indices:
        flat = flat * dim_g + idx
    return flat


def _flat_to_multi(flat: int, n: int, dim_g: int) -> Tuple[int, ...]:
    """Convert flat tensor index to multi-index of length n."""
    indices = []
    for _ in range(n):
        indices.append(flat % dim_g)
        flat //= dim_g
    return tuple(reversed(indices))


# ===========================================================================
# Bracket matrix for a single pair
# ===========================================================================

def bracket_matrix(dim_g: int, sc: Dict, n: int, i: int, j: int) -> np.ndarray:
    """Bracket matrix for contracting pair (i,j) at bar degree n.

    Maps g^{⊗n} → g^{⊗(n-1)} by:
      (a_1,...,a_n) ↦ Σ_c f^c_{a_i,a_j} (a_1,...,c_at_i,...,â_j,...,a_n)

    Args:
        i, j: 1-indexed positions with i < j
    """
    src_dim = dim_g ** n
    tgt_dim = dim_g ** (n - 1)
    mat = np.zeros((tgt_dim, src_dim))

    for flat_src in range(src_dim):
        multi_src = _flat_to_multi(flat_src, n, dim_g)
        a_i, a_j = multi_src[i - 1], multi_src[j - 1]
        bracket = sc.get((a_i, a_j), {})
        for c, coeff in bracket.items():
            new_indices = list(multi_src)
            new_indices[i - 1] = c
            del new_indices[j - 1]
            flat_tgt = _multi_to_flat(tuple(new_indices), dim_g)
            mat[flat_tgt, flat_src] += coeff

    return mat


# ===========================================================================
# Full chiral bar differential
# ===========================================================================

def chiral_bar_diff(dim_g: int, sc: Dict, n: int,
                    sign_func=None) -> np.ndarray:
    """Full chiral bar differential d: B-bar^n → B-bar^{n-1}.

    D = Σ_{1≤i<j≤n} sign(i,j) * bracket_{ij} ⊗ Res_{ij}

    Args:
        dim_g: dimension of the Lie algebra
        sc: structure constants {(a,b): {c: f^c_ab}}
        n: bar degree (number of tensor factors)
        sign_func: optional function (i, j, n) → ±1 for the sign convention.
                   If None, uses sign = 1 (no additional sign).

    Returns:
        Matrix of shape (tgt_total_dim, src_total_dim)
    """
    if n < 2:
        src_os = os_dimension(1, 0) if n == 1 else 1
        return np.zeros((1, dim_g * max(src_os, 1)))

    src_tensor = dim_g ** n
    tgt_tensor = dim_g ** (n - 1)

    src_os = os_dimension(n, n - 1)
    tgt_os = os_dimension(n - 1, n - 2) if n >= 3 else 1

    if src_os == 0 or tgt_os == 0:
        return np.zeros((tgt_tensor * max(tgt_os, 1),
                         src_tensor * max(src_os, 1)))

    src_total = src_tensor * src_os
    tgt_total = tgt_tensor * tgt_os

    D = np.zeros((tgt_total, src_total))

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            B = bracket_matrix(dim_g, sc, n, i, j)
            R = residue_map(n, n - 1, i, j)

            sign = sign_func(i, j, n) if sign_func else 1

            D += sign * np.kron(B, R)

    return D


def chain_dims(dim_g: int, max_n: int) -> Dict[int, int]:
    """Chain space dimensions for bar degrees 1, ..., max_n."""
    result = {}
    for n in range(1, max_n + 1):
        os_dim = os_dimension(n, n - 1) if n >= 1 else 1
        result[n] = dim_g ** n * max(os_dim, 1)
    return result


# ===========================================================================
# d^2 verification
# ===========================================================================

def verify_d_squared(dim_g: int, sc: Dict, n: int,
                     sign_func=None, tol: float = 1e-8) -> Dict:
    """Verify d^2 = 0 at bar degree n.

    Computes D_{n-1} ∘ D_n and checks if the result is zero.
    """
    if n < 3:
        return {"n": n, "d_squared_zero": True, "trivial": True}

    D_n = chiral_bar_diff(dim_g, sc, n, sign_func)
    D_nm1 = chiral_bar_diff(dim_g, sc, n - 1, sign_func)

    d_sq = D_nm1 @ D_n
    max_entry = np.max(np.abs(d_sq))
    is_zero = max_entry < tol

    return {
        "n": n,
        "d_squared_zero": is_zero,
        "max_entry": float(max_entry),
        "D_n_shape": D_n.shape,
        "D_nm1_shape": D_nm1.shape,
        "d_sq_shape": d_sq.shape,
    }


def search_sign_convention(dim_g: int, sc: Dict, n: int,
                           tol: float = 1e-8) -> List[Dict]:
    """Search over sign conventions to find one where d^2 = 0.

    Tests all 2^(C(n,2)) sign choices for pairs at degree n.
    For n=3: 8 choices. For n=4: 64 choices.
    """
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    num_pairs = len(pairs)
    results = []

    for sign_bits in range(2 ** num_pairs):
        signs = {}
        for idx, (i, j) in enumerate(pairs):
            signs[(i, j)] = 1 if (sign_bits >> idx) & 1 == 0 else -1

        def sign_func(i, j, n_):
            return signs.get((i, j), 1)

        result = verify_d_squared(dim_g, sc, n, sign_func, tol)
        result["signs"] = dict(signs)
        results.append(result)

        if result["d_squared_zero"]:
            break

    return results


def search_parametric_signs(dim_g: int, sc: Dict, n: int,
                            tol: float = 1e-8) -> List[Dict]:
    """Search parametric sign families: ε(i,j) = (-1)^{f(i,j)}.

    Tests common sign conventions from the literature:
    0: ε = 1 (no sign)
    1: ε = (-1)^{i+j}
    2: ε = (-1)^{i+j-1}
    3: ε = (-1)^{j-1}
    4: ε = (-1)^{i}
    5: ε = (-1)^{j}
    6: ε = (-1)^{i-1}
    7: ε = (-1)^{i+j+1}
    """
    conventions = {
        "none": lambda i, j, n_: 1,
        "(-1)^{i+j}": lambda i, j, n_: (-1) ** (i + j),
        "(-1)^{i+j-1}": lambda i, j, n_: (-1) ** (i + j - 1),
        "(-1)^{j-1}": lambda i, j, n_: (-1) ** (j - 1),
        "(-1)^{i}": lambda i, j, n_: (-1) ** i,
        "(-1)^{j}": lambda i, j, n_: (-1) ** j,
        "(-1)^{i-1}": lambda i, j, n_: (-1) ** (i - 1),
        "(-1)^{i+j+1}": lambda i, j, n_: (-1) ** (i + j + 1),
    }

    results = []
    for name, sign_func in conventions.items():
        result = verify_d_squared(dim_g, sc, n, sign_func, tol)
        result["convention"] = name
        results.append(result)

    return results


# ===========================================================================
# Bar cohomology computation
# ===========================================================================

def bar_cohomology(dim_g: int, sc: Dict, max_n: int,
                   sign_func=None, tol: float = 1e-8) -> Dict[int, int]:
    """Compute bar cohomology dimensions H^n for n = 1, ..., max_n.

    H^n = ker(d_n: B-bar^n → B-bar^{n-1}) / im(d_{n+1}: B-bar^{n+1} → B-bar^n)

    The differential d: B-bar^n → B-bar^{n-1} DECREASES bar degree.
    """
    # Build all differentials
    diffs = {}
    for n in range(2, max_n + 2):
        diffs[n] = chiral_bar_diff(dim_g, sc, n, sign_func)

    result = {}
    for n in range(1, max_n + 1):
        # Chain space dimension
        os_dim = os_dimension(n, n - 1) if n >= 1 else 1
        space_dim = dim_g ** n * max(os_dim, 1)

        # Kernel of d_n (differential OUT of degree n)
        if n >= 2 and n in diffs:
            D_n = diffs[n]
            rank_out = np.linalg.matrix_rank(D_n, tol=tol)
            ker_dim = space_dim - rank_out
        else:
            # No outgoing differential at degree 1
            ker_dim = space_dim

        # Image of d_{n+1} (differential INTO degree n)
        if n + 1 in diffs:
            D_np1 = diffs[n + 1]
            rank_in = np.linalg.matrix_rank(D_np1, tol=tol)
        else:
            rank_in = 0

        result[n] = ker_dim - rank_in

    return result


# ===========================================================================
# Riordan numbers (ground truth for sl_2)
# ===========================================================================

def riordan(n: int) -> int:
    """n-th Riordan number (OEIS A005043).

    R(0)=1, R(1)=0, R(n) = ((n-1)*(2*R(n-1)+3*R(n-2))) / (n+1)
    """
    if n == 0:
        return 1
    if n == 1:
        return 0
    R = [0] * (n + 1)
    R[0] = 1
    R[1] = 0
    for i in range(2, n + 1):
        R[i] = ((i - 1) * (2 * R[i - 1] + 3 * R[i - 2])) // (i + 1)
    return R[n]


def sl2_expected_bar_coh(max_n: int) -> Dict[int, int]:
    """Expected bar cohomology for sl_2: H^n = R(n+3)."""
    return {n: riordan(n + 3) for n in range(1, max_n + 1)}


# ===========================================================================
# Main verification
# ===========================================================================

if __name__ == "__main__":
    import sys

    dim_g, sc, kf = sl2_data()

    print("=" * 70)
    print("CHIRAL BAR COMPLEX: DIFFERENTIAL VERIFICATION FOR sl_2")
    print("=" * 70)

    # Chain space dimensions
    print("\nChain space dimensions (sl_2):")
    for n in range(1, 6):
        os_dim = os_dimension(n, n - 1) if n >= 1 else 1
        print(f"  B-bar^{n} = {dim_g}^{n} × {max(os_dim,1)} = {dim_g**n * max(os_dim,1)}")

    # Check d^2 = 0 with different sign conventions
    print("\n--- d^2 verification at degree 3 (parametric signs) ---")
    results3 = search_parametric_signs(dim_g, sc, 3)
    for r in results3:
        status = "✓ d²=0" if r["d_squared_zero"] else f"✗ max|d²|={r['max_entry']:.2e}"
        print(f"  {r['convention']:20s}: {status}")

    # Find working convention
    working = [r for r in results3 if r["d_squared_zero"]]
    if working:
        conv_name = working[0]["convention"]
        print(f"\n>>> FOUND WORKING CONVENTION: {conv_name}")
    else:
        print("\n>>> No parametric convention works. Trying exhaustive search...")
        results_exhaust = search_sign_convention(dim_g, sc, 3)
        working_exhaust = [r for r in results_exhaust if r["d_squared_zero"]]
        if working_exhaust:
            print(f"  Found {len(working_exhaust)} working sign assignments")
            for r in working_exhaust[:3]:
                print(f"    Signs: {r['signs']}")
        else:
            print("  NO WORKING SIGN CONVENTION AT DEGREE 3!")
            print("  This means bracket ⊗ Res is insufficient;")
            print("  the curvature differential is needed.")
            sys.exit(0)

    # If a convention works, verify at higher degrees and compute cohomology
    if working:
        sign_name = working[0]["convention"]

        # Map name to function
        sign_funcs = {
            "none": lambda i, j, n_: 1,
            "(-1)^{i+j}": lambda i, j, n_: (-1) ** (i + j),
            "(-1)^{i+j-1}": lambda i, j, n_: (-1) ** (i + j - 1),
            "(-1)^{j-1}": lambda i, j, n_: (-1) ** (j - 1),
            "(-1)^{i}": lambda i, j, n_: (-1) ** i,
            "(-1)^{j}": lambda i, j, n_: (-1) ** j,
            "(-1)^{i-1}": lambda i, j, n_: (-1) ** (i - 1),
            "(-1)^{i+j+1}": lambda i, j, n_: (-1) ** (i + j + 1),
        }
        sign_func = sign_funcs[sign_name]

        print(f"\n--- d^2 verification at degrees 4-5 with {sign_name} ---")
        for deg in [4, 5]:
            r = verify_d_squared(dim_g, sc, deg, sign_func)
            status = "✓ d²=0" if r["d_squared_zero"] else f"✗ max|d²|={r['max_entry']:.2e}"
            print(f"  degree {deg}: {status}  shapes: {r['D_n_shape']} -> {r['D_nm1_shape']}")

        print(f"\n--- Bar cohomology (sl_2) with {sign_name} ---")
        coh = bar_cohomology(dim_g, sc, 5, sign_func)
        expected = sl2_expected_bar_coh(5)
        for n in range(1, 6):
            exp = expected[n]
            got = coh[n]
            status = "✓" if got == exp else "✗"
            print(f"  H^{n} = {got:6d}  (expected {exp:6d})  {status}")
