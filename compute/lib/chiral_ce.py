"""Chiral Chevalley-Eilenberg complex for Kac-Moody algebras.

Computes bar cohomology of KM algebras by direct construction of the
chiral bar differential at level k=0 (pure bracket, no curvature).

Bar cohomology dims are LEVEL-INDEPENDENT (rem:bar-dims-level-independent),
so computing at k=0 gives the same answer as at any generic level.

Chain group dimensions: dim B^n = dim(g)^n * (n-1)!
  where the (n-1)! factor comes from the Orlik-Solomon algebra.

GROUND TRUTH (examples_summary.tex Table 2):
  sl2: 3, 6, 15, 36, 91, 232, 603  (Riordan R(n+3))
  sl3: 8, 36, 204, ---, ...
"""

from __future__ import annotations

from itertools import permutations, product as iproduct
from math import factorial
from typing import Dict, List, Optional, Tuple

import numpy as np


# ---------------------------------------------------------------------------
# Lie algebra structure constants
# ---------------------------------------------------------------------------

def sl2_data():
    basis = ["e", "h", "f"]
    sc = {}
    sc[("e", "f")] = {"h": 1}
    sc[("f", "e")] = {"h": -1}
    sc[("h", "e")] = {"e": 2}
    sc[("e", "h")] = {"e": -2}
    sc[("h", "f")] = {"f": -2}
    sc[("f", "h")] = {"f": 2}
    weights = {"e": (2,), "h": (0,), "f": (-2,)}
    return basis, sc, weights


def sl3_data():
    basis = ["e1", "e2", "e12", "h1", "h2", "f1", "f2", "f12"]
    sc = {}
    sc[("e1", "f1")] = {"h1": 1}; sc[("f1", "e1")] = {"h1": -1}
    sc[("e2", "f2")] = {"h2": 1}; sc[("f2", "e2")] = {"h2": -1}
    sc[("h1", "e1")] = {"e1": 2}; sc[("e1", "h1")] = {"e1": -2}
    sc[("h1", "e2")] = {"e2": -1}; sc[("e2", "h1")] = {"e2": 1}
    sc[("h2", "e1")] = {"e1": -1}; sc[("e1", "h2")] = {"e1": 1}
    sc[("h2", "e2")] = {"e2": 2}; sc[("e2", "h2")] = {"e2": -2}
    sc[("h1", "f1")] = {"f1": -2}; sc[("f1", "h1")] = {"f1": 2}
    sc[("h1", "f2")] = {"f2": 1}; sc[("f2", "h1")] = {"f2": -1}
    sc[("h2", "f1")] = {"f1": 1}; sc[("f1", "h2")] = {"f1": -1}
    sc[("h2", "f2")] = {"f2": -2}; sc[("f2", "h2")] = {"f2": 2}
    sc[("e1", "e2")] = {"e12": 1}; sc[("e2", "e1")] = {"e12": -1}
    sc[("f1", "f2")] = {"f12": -1}; sc[("f2", "f1")] = {"f12": 1}
    sc[("e12", "f1")] = {"e2": -1}; sc[("f1", "e12")] = {"e2": 1}
    sc[("e12", "f2")] = {"e1": 1}; sc[("f2", "e12")] = {"e1": -1}
    sc[("e1", "f12")] = {"f2": -1}; sc[("f12", "e1")] = {"f2": 1}
    sc[("e2", "f12")] = {"f1": 1}; sc[("f12", "e2")] = {"f1": -1}
    sc[("e12", "f12")] = {"h1": 1, "h2": 1}
    sc[("f12", "e12")] = {"h1": -1, "h2": -1}
    sc[("h1", "e12")] = {"e12": 1}; sc[("e12", "h1")] = {"e12": -1}
    sc[("h2", "e12")] = {"e12": 1}; sc[("e12", "h2")] = {"e12": -1}
    sc[("h1", "f12")] = {"f12": -1}; sc[("f12", "h1")] = {"f12": 1}
    sc[("h2", "f12")] = {"f12": -1}; sc[("f12", "h2")] = {"f12": 1}
    weights = {
        "e1": (1, 0), "e2": (0, 1), "e12": (1, 1),
        "h1": (0, 0), "h2": (0, 0),
        "f1": (-1, 0), "f2": (0, -1), "f12": (-1, -1),
    }
    return basis, sc, weights


# ---------------------------------------------------------------------------
# Orlik-Solomon top-degree basis and restriction
# ---------------------------------------------------------------------------
# OS^{n-1}(C_n) has dim (n-1)!.
# Basis: orderings of {1,...,n-1} (point 0 is the root).
# Form for ordering sigma = (s_1,...,s_{n-1}):
#   omega_sigma = eta_{0,s_1} ^ eta_{s_1,s_2} ^ ... ^ eta_{s_{n-2},s_{n-1}}
#
# Restriction iota_{ij}: merge point i into point j.
# If the path visits i, the edge entering i and exiting i get merged:
#   ...-> k -> i -> l ->... becomes ...-> k -> j -> l ->...
# (with j replacing i throughout, then relabeling).
#
# If the form contains eta_{i,j} as a factor, the restriction is ZERO.

def os_basis(n: int) -> List[Tuple[int, ...]]:
    """Basis for OS^{n-1}(C_n). Orderings of {1,...,n-1}."""
    if n <= 1:
        return [()]
    return list(permutations(range(1, n)))


def os_form_edges(n: int, sigma: Tuple[int, ...]) -> List[Tuple[int, int]]:
    """Convert ordering sigma to list of directed edges (path from 0)."""
    if not sigma:
        return []
    edges = [(0, sigma[0])]
    for k in range(len(sigma) - 1):
        edges.append((sigma[k], sigma[k + 1]))
    return edges


def os_restrict_bracket(
    n: int,
    sigma: Tuple[int, ...],
    i: int, j: int,
) -> List[Tuple[Tuple[int, ...], int]]:
    """Restrict OS form by merging point i into point j (bracket contraction).

    Returns list of (target_ordering, sign) in the (n-1)-point OS basis.
    Points relabeled: remove i, shift indices > i down by 1.

    The bracket contraction uses the simple pole residue, which
    integrates eta_{ij} against the residue. The result is obtained
    by removing the edge involving i,j and connecting the remaining path.
    """
    edges = os_form_edges(n, sigma)

    # Check if any edge IS (i,j) or (j,i) -- if so, the residue
    # extracts a coefficient and removes this edge from the form.
    # If no edge touches both i and j, the restriction is zero
    # (no eta_{ij} factor to extract residue from).

    # For the chiral bar differential, the residue at z_i = z_j
    # extracts the coefficient of eta_{ij} in the form.
    # The path form omega_sigma contains eta_{a,b} for consecutive
    # pairs in the path 0 -> s_1 -> s_2 -> ... -> s_{n-1}.

    # Find the edge(s) involving i and j
    ij_edge_idx = None
    for idx, (a, b) in enumerate(edges):
        if (a == i and b == j) or (a == j and b == i):
            ij_edge_idx = idx
            break

    if ij_edge_idx is None:
        # No direct i-j edge: need to check if the form has an
        # eta_{ij} component when expanded in the wedge product basis.
        # For path forms, if i and j are not adjacent in the path,
        # the form does NOT contain eta_{ij}, so the restriction is zero.
        return []

    # The edge (a, b) at position ij_edge_idx is either (i,j) or (j,i).
    a, b = edges[ij_edge_idx]

    # Remove this edge: merge the two path segments.
    # Before: ...-> prev -> a -> b -> next ->...
    # After:  ...-> prev -> (merged point) -> next ->...
    # The merged point keeps label j (we remove i).

    # Build new path: replace i with j, remove the edge
    new_path = list(sigma)
    # Find i in the path
    if i in new_path:
        i_pos = new_path.index(i)
        new_path[i_pos] = j  # Replace i with j
        # But now we have j appearing twice (or the path structure changes).
        # Actually, the restriction REMOVES the edge (a,b) and connects
        # the path through the merged point j.

    # Simpler approach: rebuild the path after merging i into j.
    # The full path is: 0 -> sigma[0] -> sigma[1] -> ... -> sigma[n-2]
    full_path = [0] + list(sigma)

    # Replace all occurrences of i with j
    merged_path = [j if x == i else x for x in full_path]

    # Remove consecutive duplicates (the merged edge)
    cleaned = [merged_path[0]]
    for x in merged_path[1:]:
        if x != cleaned[-1]:
            cleaned.append(x)

    # Relabel: remove point i from index set
    # k -> k if k < i, k -> k-1 if k > i
    def relabel(x):
        return x if x < i else x - 1

    relabeled = [relabel(x) for x in cleaned]

    # The new ordering is relabeled[1:] (skip the root 0)
    new_sigma = tuple(relabeled[1:])

    # Check it's a valid (n-1)-point ordering
    if len(new_sigma) != n - 2:
        return []

    # Sign: the original edge was at position ij_edge_idx in the wedge.
    # Removing it from position ij_edge_idx gives sign (-1)^{ij_edge_idx}.
    # Also need sign from eta_{ij} vs eta_{ji}: eta_{j,i} = -eta_{i,j}.
    edge_sign = 1 if a == i else -1  # eta_{i,j} vs eta_{j,i}
    position_sign = (-1) ** ij_edge_idx

    return [(new_sigma, edge_sign * position_sign)]


# ---------------------------------------------------------------------------
# Bar differential construction
# ---------------------------------------------------------------------------

def build_bar_diff(basis, sc, n, verbose=False):
    """Build bar differential d_n: B^n -> B^{n-1} as numpy matrix.

    B^n = g^{otimes n} tensor OS^{n-1}(C_n).
    d_n sums over pairs (i,j) with 0 <= i < j < n.

    At k=0: d is purely the Lie bracket contraction.
    """
    d = len(basis)
    b2i = {b: idx for idx, b in enumerate(basis)}

    os_src = os_basis(n)
    os_tgt = os_basis(n - 1)
    os_src_dim = len(os_src)
    os_tgt_dim = len(os_tgt)

    src_dim = d**n * os_src_dim
    tgt_dim = d**(n-1) * os_tgt_dim

    if verbose:
        print(f"  d_{n}: B^{n} ({src_dim}) -> B^{n-1} ({tgt_dim})")

    # Index maps
    os_tgt_lookup = {sigma: idx for idx, sigma in enumerate(os_tgt)}

    def src_idx(gens, os_i):
        idx = 0
        for g in gens:
            idx = idx * d + g
        return idx * os_src_dim + os_i

    def tgt_idx(gens, os_i):
        idx = 0
        for g in gens:
            idx = idx * d + g
        return idx * os_tgt_dim + os_i

    mat = np.zeros((tgt_dim, src_dim), dtype=np.int64)

    for gen_tuple in iproduct(range(d), repeat=n):
        for os_s_i, os_s_sigma in enumerate(os_src):
            s = src_idx(gen_tuple, os_s_i)

            for i in range(n):
                for j in range(i + 1, n):
                    a_i = basis[gen_tuple[i]]
                    a_j = basis[gen_tuple[j]]
                    bracket = sc.get((a_i, a_j), {})
                    if not bracket:
                        continue

                    # OS restriction
                    restricted = os_restrict_bracket(n, os_s_sigma, i, j)
                    if not restricted:
                        continue

                    for new_sigma, os_sign in restricted:
                        if new_sigma not in os_tgt_lookup:
                            continue
                        os_t_i = os_tgt_lookup[new_sigma]

                        for c_name, coeff in bracket.items():
                            c_idx = b2i[c_name]
                            # Build target generator tuple
                            new_gens = list(gen_tuple)
                            new_gens[i] = c_idx
                            del new_gens[j]

                            t = tgt_idx(tuple(new_gens), os_t_i)
                            mat[t, s] += os_sign * coeff

    return mat, src_dim, tgt_dim


# ---------------------------------------------------------------------------
# Cohomology computation
# ---------------------------------------------------------------------------

def compute_bar_cohomology(basis, sc, max_degree, verbose=False):
    """Compute bar cohomology H^n for n = 1, ..., max_degree."""
    d = len(basis)
    results = {}

    # We need d_n and d_{n+1} for each degree n.
    # Cache differentials.
    diff_cache = {}

    def get_diff(n):
        if n not in diff_cache:
            if n <= 0:
                # d_0 doesn't exist, d_1: B^1 -> B^0 = 0
                return np.zeros((1, d), dtype=np.int64), d, 1
            diff_cache[n] = build_bar_diff(basis, sc, n, verbose)
        return diff_cache[n]

    for deg in range(1, max_degree + 1):
        mat_n, src_n, tgt_n = get_diff(deg)
        mat_np1, src_np1, tgt_np1 = get_diff(deg + 1)

        # H^deg = ker(d_deg) / im(d_{deg+1})
        # Since d^2 = 0: im(d_{deg+1}) subset ker(d_deg)
        # So H^deg = dim ker(d_deg) - rank(d_{deg+1})

        # Use numpy rank (float, but for integer matrices should be exact
        # for reasonably sized matrices)
        ker_n = src_n - np.linalg.matrix_rank(mat_n.astype(float))
        rank_np1 = np.linalg.matrix_rank(mat_np1.astype(float))

        results[deg] = ker_n - rank_np1
        if verbose:
            print(f"  H^{deg} = ker(d_{deg})={ker_n} - rank(d_{deg+1})={rank_np1} = {results[deg]}")

    return results


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_d_squared(basis, sc, n, verbose=False):
    """Check d_{n-1} ∘ d_n = 0."""
    mat_n, _, _ = build_bar_diff(basis, sc, n, verbose)
    mat_nm1, _, _ = build_bar_diff(basis, sc, n - 1, verbose)
    product = mat_nm1 @ mat_n
    is_zero = np.all(product == 0)
    if verbose:
        print(f"  d_{n-1} ∘ d_{n} = 0: {is_zero}")
        if not is_zero:
            print(f"    max entry: {np.max(np.abs(product))}")
    return is_zero


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("CHIRAL BAR COHOMOLOGY: DIRECT COMPUTATION")
    print("=" * 60)

    # --- sl2 ---
    print("\n--- sl2 verification ---")
    basis, sc, _ = sl2_data()

    print("Checking d^2 = 0:")
    for n in [2, 3]:
        verify_d_squared(basis, sc, n, verbose=True)

    results_sl2 = compute_bar_cohomology(basis, sc, max_degree=4, verbose=True)
    expected_sl2 = {1: 3, 2: 6, 3: 15, 4: 36}
    print("\nsl2 results:")
    for deg in sorted(results_sl2):
        exp = expected_sl2.get(deg, "?")
        ok = results_sl2[deg] == exp
        print(f"  [{'PASS' if ok else 'FAIL'}] H^{deg} = {results_sl2[deg]} (expected {exp})")

    # --- sl3 ---
    print("\n--- sl3 computation ---")
    basis, sc, _ = sl3_data()

    print("Checking d^2 = 0:")
    for n in [2, 3]:
        verify_d_squared(basis, sc, n, verbose=True)

    results_sl3 = compute_bar_cohomology(basis, sc, max_degree=3, verbose=True)
    expected_sl3 = {1: 8, 2: 36, 3: 204}
    print("\nsl3 results:")
    for deg in sorted(results_sl3):
        exp = expected_sl3.get(deg, "?")
        ok = results_sl3[deg] == exp
        print(f"  [{'PASS' if ok else 'FAIL'}] H^{deg} = {results_sl3[deg]} (expected {exp})")
