#!/usr/bin/env python3
r"""Compute chiral bar cohomology via OS-algebra residues.

The chiral bar complex for a KM algebra g-hat_k:
  B-bar^n = g^{tensor n} tensor OS^{n-1}(C_n)

where OS^{n-1}(C_n) is the top-degree Orlik-Solomon algebra of the
configuration space of n points in C, with dim = (n-1)!.

Bar differential d: B-bar^{n+1} -> B-bar^n:
  d(a_1 tensor ... tensor a_{n+1} tensor omega)
    = sum_{p<q} sign(p,q) * bracket(a_p, a_q) * remaining * Res_{D_pq}(omega)

where Res_{D_pq}: OS^n(C_{n+1}) -> OS^{n-1}(C_n) is the Poincare residue
along the collision diagonal z_p = z_q.

After collision (p,q), the n+1 points become n points:
  - Points p and q merge
  - The merged point inherits the bracket [a_p, a_q]
  - The remaining n-1 original generators are unchanged
  - Points are relabeled 1,...,n in order (merged point at position min(p,q))

This module computes everything from first principles using numpy for speed.
"""

import numpy as np
from itertools import combinations, permutations
from math import factorial
from typing import Dict, List, Tuple, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


# ============================================================
# Orlik-Solomon algebra: NBC basis and residue maps
# ============================================================

def edges_Kn(n: int) -> List[Tuple[int, int]]:
    """All edges of K_n, lexicographically ordered. Vertices 1-indexed."""
    return [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]


def is_spanning(edge_set: frozenset, n: int) -> bool:
    """Check if an edge set spans all n vertices (is a spanning subgraph)."""
    if not edge_set:
        return n <= 1
    verts = set()
    for i, j in edge_set:
        verts.add(i)
        verts.add(j)
    if len(verts) < n:
        return False
    # Check connectivity via BFS
    adj = {v: set() for v in range(1, n + 1)}
    for i, j in edge_set:
        adj[i].add(j)
        adj[j].add(i)
    visited = set()
    stack = [1]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        for u in adj[v]:
            if u not in visited:
                stack.append(u)
    return len(visited) == n


def find_circuits(edge_list: List[Tuple[int, int]], n: int) -> List[frozenset]:
    """Find all minimal circuits (cycles) in K_n restricted to edge_list."""
    circuits = []
    # For small n, enumerate all subsets and check if they form a cycle
    for size in range(3, n + 1):
        for combo in combinations(edge_list, size):
            edge_set = frozenset(combo)
            # Check if this forms a simple cycle: every vertex has degree exactly 2
            deg = {}
            for i, j in combo:
                deg[i] = deg.get(i, 0) + 1
                deg[j] = deg.get(j, 0) + 1
            verts = set(deg.keys())
            if len(verts) == size and all(d == 2 for d in deg.values()):
                # Check minimality: no proper subset is also a cycle
                is_minimal = True
                for sub_size in range(3, size):
                    for sub_combo in combinations(combo, sub_size):
                        sub_deg = {}
                        for i, j in sub_combo:
                            sub_deg[i] = sub_deg.get(i, 0) + 1
                            sub_deg[j] = sub_deg.get(j, 0) + 1
                        sub_verts = set(sub_deg.keys())
                        if len(sub_verts) == sub_size and all(
                            d == 2 for d in sub_deg.values()
                        ):
                            is_minimal = False
                            break
                    if not is_minimal:
                        break
                if is_minimal:
                    circuits.append(edge_set)
    return circuits


def broken_circuits(n: int) -> List[frozenset]:
    """Compute all broken circuits for K_n with lex ordering on edges."""
    all_edges = edges_Kn(n)
    edge_order = {e: i for i, e in enumerate(all_edges)}

    circuits = find_circuits(all_edges, n)
    bcs = []
    for circ in circuits:
        # Find the largest edge in the circuit
        max_edge = max(circ, key=lambda e: edge_order[e])
        bc = circ - {max_edge}
        bcs.append(bc)
    return bcs


def nbc_basis(n: int, k: int) -> List[Tuple[Tuple[int, int], ...]]:
    """NBC basis for OS^k(C_n).

    Returns list of k-element edge sets (as sorted tuples) that:
    1. Are k-element subsets of edges of K_n
    2. Contain no broken circuit as a subset

    For k = n-1: these are NBC spanning trees, count = (n-1)!.
    """
    if n <= 1:
        if k == 0:
            return [()]
        return []
    if k == 0:
        return [()]

    all_edges = edges_Kn(n)
    bcs = broken_circuits(n)

    basis = []
    for combo in combinations(all_edges, k):
        edge_set = frozenset(combo)
        # Check: no broken circuit is a subset
        is_nbc = True
        for bc in bcs:
            if bc.issubset(edge_set):
                is_nbc = False
                break
        if is_nbc:
            basis.append(tuple(sorted(combo)))
    return basis


def _edge_sign(edges_tuple: tuple, full_edges: tuple) -> int:
    """Sign of the wedge product: product of signs from ordering edges."""
    # The sign comes from reordering the edges to match the canonical order
    # For a tuple of edges, the sign is the parity of the permutation
    # that sorts the edges into the canonical (lex) order.
    # Since we always store edges in sorted order, the sign is +1.
    return 1


def relabel_after_collision(
    pq: Tuple[int, int], n: int
) -> Dict[int, int]:
    """After colliding points p and q (merging q into p), relabel to 1..n-1.

    Convention: the merged point goes to position min(p,q) in the new labeling.
    Other points shift down to fill the gap left by max(p,q).

    Returns: dict mapping old vertex labels to new labels.
    """
    p, q = pq
    # After collision: point q disappears, point p becomes the merged point.
    # New labels: 1, ..., n-1.
    # Old points: 1, ..., n with q removed.
    # The merged point (originally p) keeps its relative position.

    old_points = [i for i in range(1, n + 1) if i != q]
    # old_points has n-1 elements, in order. Map them to 1..n-1.
    relabel = {}
    for new_label, old_label in enumerate(old_points, start=1):
        relabel[old_label] = new_label
    return relabel


def residue_matrix(n: int) -> Dict[Tuple[int, int], np.ndarray]:
    """Compute residue maps Res_{D_pq}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1}).

    Returns dict mapping (p,q) to a matrix of shape (dim_target, dim_source).

    The residue of omega = eta_{e1} ^ ... ^ eta_{e_{n-1}} along D_{pq}:
    1. If edge (p,q) is not among {e1,...,e_{n-1}}: residue is 0.
    2. If edge (p,q) = e_k: remove that factor (with sign (-1)^k),
       relabel remaining edges using the collision relabeling,
       and express in the target NBC basis.
    """
    if n <= 1:
        return {}

    source_basis = nbc_basis(n, n - 1)
    target_basis = nbc_basis(n - 1, n - 2)
    dim_source = len(source_basis)
    dim_target = len(target_basis)

    # Build target lookup
    target_idx = {b: i for i, b in enumerate(target_basis)}

    result = {}
    for p in range(1, n + 1):
        for q in range(p + 1, n + 1):
            M = np.zeros((dim_target, dim_source), dtype=np.float64)
            relabel = relabel_after_collision((p, q), n)

            for col, src_edges in enumerate(source_basis):
                # src_edges is a tuple of (n-1) edges, sorted
                # Check if (p,q) is among them
                if (p, q) not in src_edges:
                    continue

                # Find position of (p,q) in the wedge product
                pos = src_edges.index((p, q))
                sign = (-1) ** pos

                # Remaining edges after removing (p,q)
                remaining = [e for e in src_edges if e != (p, q)]

                # Relabel remaining edges
                relabeled = []
                for i, j in remaining:
                    ni = relabel.get(i)
                    nj = relabel.get(j)
                    if ni is None or nj is None:
                        # One endpoint was q; it merges into p
                        if i == q:
                            ni = relabel[p]
                        if j == q:
                            nj = relabel[p]
                        if ni is None:
                            ni = relabel[i]
                        if nj is None:
                            nj = relabel[j]
                    # Normalize edge orientation: smaller index first
                    if ni > nj:
                        ni, nj = nj, ni
                        sign *= -1
                    if ni == nj:
                        # Degenerate: both endpoints merged
                        sign = 0
                        break
                    relabeled.append((ni, nj))

                if sign == 0:
                    continue

                # Express relabeled edges as an element of OS^{n-2}(C_{n-1})
                # The relabeled edges form a (n-2)-form in the target space.
                # Need to express in the NBC basis using Arnold relations.
                relabeled_sorted = tuple(sorted(relabeled))

                if relabeled_sorted in target_idx:
                    # It's already a basis element
                    row = target_idx[relabeled_sorted]
                    M[row, col] += sign
                else:
                    # Need to reduce using Arnold relations
                    # For now, use the full reduction algorithm
                    coeffs = _reduce_to_nbc(
                        relabeled, n - 1, target_basis, target_idx
                    )
                    for row, c in coeffs.items():
                        M[row, col] += sign * c

            result[(p, q)] = M

    return result


def _reduce_to_nbc(
    edges: List[Tuple[int, int]],
    n: int,
    basis: List[Tuple[Tuple[int, int], ...]],
    basis_idx: Dict,
) -> Dict[int, float]:
    """Reduce a wedge product of edges to the NBC basis using Arnold relations.

    Arnold relation: eta_{ij} ^ eta_{jk} = eta_{ij} ^ eta_{ik} - eta_{ik} ^ eta_{jk}
    (for any three distinct i,j,k -- this is the 3-term relation)

    Returns dict mapping basis index to coefficient.
    """
    # Strategy: repeatedly apply Arnold relations to eliminate broken circuits.
    # This is a finite process since each application reduces the lex-order of the edge set.

    bcs = broken_circuits(n)
    all_edges_order = {e: i for i, e in enumerate(edges_Kn(n))}

    # Represent the form as a linear combination of sorted edge tuples
    # Each entry: (coeff, sorted_edge_tuple)
    edge_tuple = tuple(sorted(edges))

    # Check sign: the original ordering of edges matters
    # We need the sign of the permutation that sorts `edges` into `edge_tuple`
    perm_sign = _permutation_sign(edges, list(edge_tuple))
    if perm_sign == 0:
        return {}  # degenerate (repeated edge)

    forms = {edge_tuple: float(perm_sign)}

    # Iteratively reduce
    changed = True
    max_iter = 100
    iteration = 0
    while changed and iteration < max_iter:
        changed = False
        iteration += 1
        new_forms = {}
        for edge_t, coeff in forms.items():
            if abs(coeff) < 1e-15:
                continue
            edge_set = frozenset(edge_t)

            # Check if this contains any broken circuit
            found_bc = None
            for bc in bcs:
                if bc.issubset(edge_set):
                    found_bc = bc
                    break

            if found_bc is None:
                # Already NBC
                new_forms[edge_t] = new_forms.get(edge_t, 0) + coeff
            else:
                changed = True
                # Apply Arnold relation to eliminate this broken circuit
                # The broken circuit came from a circuit C with largest edge e_max removed.
                # Arnold: sum over cyclic permutations of the triangle gives 0.
                # For a triangle {ij, jk, ik}: eta_ij ^ eta_jk + eta_jk ^ eta_ik + eta_ik ^ eta_ij = 0
                # The broken circuit is {ij, jk} (assuming ik is the largest).
                # So: eta_ij ^ eta_jk = eta_ij ^ eta_ik - eta_ik ^ eta_jk
                # (replace the BC {ij, jk} with two terms involving ik)

                # Find the full circuit
                e_max = _find_circuit_max(found_bc, n, all_edges_order)
                if e_max is None:
                    # Can't find the circuit -- just keep the form
                    new_forms[edge_t] = new_forms.get(edge_t, 0) + coeff
                    continue

                # The Arnold relation for the circuit {bc edges} ∪ {e_max}:
                # We need to express the form that contains the BC in terms of
                # forms that contain e_max instead of one of the BC edges.

                bc_edges = sorted(found_bc, key=lambda e: all_edges_order[e])
                # For a 2-edge BC (from a triangle):
                if len(bc_edges) == 2:
                    e1, e2 = bc_edges[0], bc_edges[1]  # sorted by lex
                    # Arnold: eta_{e1} ^ eta_{e2} = eta_{e1} ^ eta_{emax} - eta_{emax} ^ eta_{e2}
                    #        = eta_{e1} ^ eta_{emax} + eta_{e2} ^ eta_{emax}
                    # Wait, Arnold relation: for edges forming a triangle {e1, e2, e_max}:
                    # eta_{e1} ^ eta_{e2} - eta_{e1} ^ eta_{e_max} + eta_{e2} ^ eta_{e_max} = 0
                    # (with appropriate signs depending on vertex ordering)

                    # Actually, Arnold relation for vertices {i,j,k} with i<j<k:
                    # eta_{ij} ^ eta_{jk} - eta_{ij} ^ eta_{ik} + eta_{ik} ^ eta_{jk} = 0
                    # => eta_{ij} ^ eta_{jk} = eta_{ij} ^ eta_{ik} - eta_{ik} ^ eta_{jk}

                    # Find the three vertices of the triangle
                    triangle_verts = set()
                    for e in list(found_bc) + [e_max]:
                        triangle_verts.update(e)
                    i, j, k = sorted(triangle_verts)

                    # The triangle edges are (i,j), (i,k), (j,k)
                    # The broken circuit is the triangle minus the largest edge
                    # Largest edge = (j,k) or (i,k) depending on lex order
                    # In our ordering: (i,j) < (i,k) < (j,k) when i<j<k
                    # So largest = (j,k), BC = {(i,j), (i,k)}

                    # Arnold: eta_{ij} ^ eta_{ik} = eta_{ij} ^ eta_{jk} - eta_{jk} ^ eta_{ik}
                    #                              = eta_{ij} ^ eta_{jk} + eta_{ik} ^ eta_{jk}

                    # But we want to ELIMINATE the BC. The BC is {e1, e2} which
                    # doesn't contain e_max. We want to replace it with terms
                    # containing e_max.

                    # Find which edges are e1, e2, e_max in terms of (i,j,k)
                    e_ij = (i, j)
                    e_ik = (i, k)
                    e_jk = (j, k)

                    # The BC = triangle - {largest} = {e_ij, e_ik} (if e_jk is largest)
                    # or {e_ij, e_jk} (if e_ik is largest), etc.

                    # Arnold: eta_{ij} ^ eta_{jk} - eta_{ij} ^ eta_{ik} + eta_{ik} ^ eta_{jk} = 0
                    # => the 2-form eta_{e_a} ^ eta_{e_b} where {e_a, e_b} is the BC
                    # can be expressed in terms of the other two pairings.

                    # We need: which pair in {e1,e2} corresponds to which edges of the triangle?
                    bc_set = frozenset(bc_edges)

                    if bc_set == frozenset([e_ij, e_ik]):
                        # BC = {(i,j), (i,k)}, missing edge = (j,k)
                        # Arnold: eta_ij ^ eta_ik = eta_ij ^ eta_jk + eta_ik ^ eta_jk
                        # (from: -eta_ij^eta_ik + eta_ij^eta_jk + ... wait)
                        # Arnold: eta_ij^eta_jk - eta_ij^eta_ik + eta_ik^eta_jk = 0
                        # => eta_ij^eta_ik = eta_ij^eta_jk + eta_ik^eta_jk
                        replacement_pairs = [(e_ij, e_jk, 1), (e_ik, e_jk, 1)]
                    elif bc_set == frozenset([e_ij, e_jk]):
                        # BC = {(i,j), (j,k)}, missing = (i,k)
                        # Arnold: eta_ij^eta_jk = eta_ij^eta_ik - eta_ik^eta_jk
                        replacement_pairs = [(e_ij, e_ik, 1), (e_ik, e_jk, -1)]
                    elif bc_set == frozenset([e_ik, e_jk]):
                        # BC = {(i,k), (j,k)}, missing = (i,j)
                        # Arnold: eta_ik^eta_jk = -eta_ij^eta_jk + eta_ij^eta_ik
                        # = eta_ij^eta_ik - eta_ij^eta_jk
                        replacement_pairs = [(e_ij, e_ik, 1), (e_ij, e_jk, -1)]
                    else:
                        raise ValueError(f"Unexpected BC {bc_set} for triangle {i},{j},{k}")

                    # Now apply the replacement in the full edge tuple
                    # Find positions of e1 and e2 in edge_t
                    pos1 = list(edge_t).index(bc_edges[0])
                    pos2 = list(edge_t).index(bc_edges[1])

                    # The sign of eta_{e1}^eta_{e2} in the wedge product at positions pos1, pos2
                    # depends on the ordering: positive if pos1 < pos2.
                    bc_sign = 1 if pos1 < pos2 else -1

                    other_edges = [e for e in edge_t if e not in bc_set]

                    for new_e1, new_e2, rel_sign in replacement_pairs:
                        new_edges = list(other_edges) + [new_e1, new_e2]
                        new_sorted = tuple(sorted(new_edges))

                        # Compute the sign: the replacement introduces a sign
                        # from the Arnold relation, plus the sign from reordering.
                        psign = _permutation_sign(
                            [new_e1, new_e2] + other_edges,
                            list(new_sorted)
                        )
                        if psign == 0:
                            continue
                        total_sign = coeff * bc_sign * rel_sign * psign
                        new_forms[new_sorted] = new_forms.get(new_sorted, 0) + total_sign
                else:
                    # Higher-order broken circuit -- more complex reduction
                    # For small n (<=5), triangles suffice
                    new_forms[edge_t] = new_forms.get(edge_t, 0) + coeff

        forms = {k: v for k, v in new_forms.items() if abs(v) > 1e-15}

    # Convert to basis indices
    result = {}
    for edge_t, coeff in forms.items():
        if abs(coeff) < 1e-15:
            continue
        if edge_t in basis_idx:
            result[basis_idx[edge_t]] = result.get(basis_idx[edge_t], 0) + coeff
        else:
            # This shouldn't happen if the reduction is correct
            print(f"WARNING: form {edge_t} not in NBC basis (n={n})")
    return result


def _find_circuit_max(
    bc: frozenset, n: int, edge_order: Dict
) -> Optional[Tuple[int, int]]:
    """Find the edge e_max such that bc ∪ {e_max} is a circuit."""
    all_edges = edges_Kn(n)
    for e in all_edges:
        if e in bc:
            continue
        candidate = bc | {e}
        # Check if candidate is a circuit (simple cycle)
        deg = {}
        for i, j in candidate:
            deg[i] = deg.get(i, 0) + 1
            deg[j] = deg.get(j, 0) + 1
        if all(d == 2 for d in deg.values()) and len(deg) == len(candidate):
            # Also check that e is indeed the max
            if all(edge_order[e] >= edge_order[f] for f in candidate):
                return e
    return None


def _permutation_sign(src: list, dst: list) -> int:
    """Sign of the permutation that maps src to dst. Returns 0 if not a permutation."""
    if len(src) != len(dst) or set(map(tuple, src)) != set(map(tuple, dst)):
        return 0
    n = len(src)
    src_idx = {tuple(v): i for i, v in enumerate(src)}
    perm = [src_idx[tuple(v)] for v in dst]
    # Count inversions
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inv += 1
    return (-1) ** inv


# ============================================================
# Lie algebra structure constants
# ============================================================

def sl2_structure_tensor():
    """Structure constants for sl_2 as a 3x3x3 tensor.

    Basis: e=0, h=1, f=2.
    [e,f] = h, [h,e] = 2e, [h,f] = -2f.
    """
    f = np.zeros((3, 3, 3))
    # [e, f] = h
    f[0, 2, 1] = 1
    f[2, 0, 1] = -1
    # [h, e] = 2e
    f[1, 0, 0] = 2
    f[0, 1, 0] = -2
    # [h, f] = -2f
    f[1, 2, 2] = -2
    f[2, 1, 2] = 2
    return f


def sl3_structure_tensor():
    """Structure constants for sl_3 as an 8x8x8 tensor.

    Basis: H1=0, H2=1, E1=2, E2=3, E3=4, F1=5, F2=6, F3=7.
    """
    d = 8
    f = np.zeros((d, d, d))
    H1, H2, E1, E2, E3, F1, F2, F3 = range(8)
    CARTAN = np.array([[2, -1], [-1, 2]])

    def set_bracket(a, b, c, val):
        f[a, b, c] += val
        f[b, a, c] -= val

    # [H_i, E_j] = A_{ij} E_j
    for i, hi in enumerate([H1, H2]):
        for j, ej in enumerate([E1, E2]):
            if CARTAN[i, j] != 0:
                set_bracket(hi, ej, ej, CARTAN[i, j])

    # [H_i, F_j] = -A_{ij} F_j
    for i, hi in enumerate([H1, H2]):
        for j, fj in enumerate([F1, F2]):
            if CARTAN[i, j] != 0:
                set_bracket(hi, fj, fj, -CARTAN[i, j])

    # [E_i, F_j] = delta_{ij} H_i
    set_bracket(E1, F1, H1, 1)
    set_bracket(E2, F2, H2, 1)

    # [E_1, E_2] = E_3
    set_bracket(E1, E2, E3, 1)
    # [F_2, F_1] = F_3
    set_bracket(F2, F1, F3, 1)

    # [H_i, E_3]: root alpha_1+alpha_2
    set_bracket(H1, E3, E3, 1)  # A11+A12 = 2-1 = 1
    set_bracket(H2, E3, E3, 1)  # A21+A22 = -1+2 = 1

    # [H_i, F_3]
    set_bracket(H1, F3, F3, -1)
    set_bracket(H2, F3, F3, -1)

    # [E_3, F_1] = -E_2
    set_bracket(E3, F1, E2, -1)
    # [E_3, F_2] = E_1
    set_bracket(E3, F2, E1, 1)
    # [E_3, F_3] = H_1 + H_2
    set_bracket(E3, F3, H1, 1)
    set_bracket(E3, F3, H2, 1)

    # [E_1, F_3] = -F_2
    set_bracket(E1, F3, F2, -1)
    # [E_2, F_3] = F_1
    set_bracket(E2, F3, F1, 1)

    return f


# ============================================================
# Chiral bar differential
# ============================================================

def chiral_bar_differential(f_abc: np.ndarray, n: int) -> np.ndarray:
    """Build bar differential d: B-bar^n -> B-bar^{n-1}.

    B-bar^n = g^{tensor n} tensor OS^{n-1}(C_n)
    dim B-bar^n = dim_g^n * (n-1)!

    B-bar^{n-1} = g^{tensor (n-1)} tensor OS^{n-2}(C_{n-1})
    dim B-bar^{n-1} = dim_g^{n-1} * (n-2)!

    Returns matrix of shape (dim_target, dim_source).
    """
    dim_g = f_abc.shape[0]

    if n <= 1:
        return np.zeros((0, dim_g))

    # OS bases
    source_os = nbc_basis(n, n - 1)  # OS^{n-1}(C_n)
    target_os = nbc_basis(n - 1, n - 2)  # OS^{n-2}(C_{n-1})
    dim_os_source = len(source_os)
    dim_os_target = len(target_os)

    # Total dimensions
    source_dim = dim_g ** n * dim_os_source
    target_dim = dim_g ** (n - 1) * dim_os_target

    # Column indexing: (gen_tuple, os_idx) -> col
    # col = tensor_idx * dim_os_source + os_idx
    # tensor_idx encodes (a_1, ..., a_n) in mixed-radix

    # Row indexing: (gen_tuple, os_idx) -> row
    # row = tensor_idx * dim_os_target + os_idx

    # Residue maps
    res_maps = residue_matrix(n)

    # Build matrix using sparse construction
    rows = []
    cols = []
    vals = []

    def tensor_to_idx(gen_tuple, dim):
        """Convert generator tuple to linear index (little-endian)."""
        idx = 0
        for k in range(len(gen_tuple) - 1, -1, -1):
            idx = idx * dim + gen_tuple[k]
        return idx

    for src_tensor_idx in range(dim_g ** n):
        # Decode tensor index to generator tuple
        gens = []
        temp = src_tensor_idx
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g

        for os_src_idx in range(dim_os_source):
            col = src_tensor_idx * dim_os_source + os_src_idx

            # Sum over all collision pairs (p, q)
            for p in range(1, n + 1):
                for q in range(p + 1, n + 1):
                    # OS residue: source os_src_idx -> target os
                    res = res_maps.get((p, q))
                    if res is None:
                        continue

                    # Nonzero residue entries
                    for os_tgt_idx in range(dim_os_target):
                        res_coeff = res[os_tgt_idx, os_src_idx]
                        if abs(res_coeff) < 1e-15:
                            continue

                        # Bracket at positions p, q (1-indexed)
                        a_p = gens[p - 1]
                        a_q = gens[q - 1]

                        for c in range(dim_g):
                            bracket_coeff = f_abc[a_p, a_q, c]
                            if abs(bracket_coeff) < 1e-15:
                                continue

                            # Build target generator tuple:
                            # Replace p,q with bracket result c at position min(p,q)
                            # Remove position max(p,q)
                            tgt_gens = list(gens)
                            tgt_gens[p - 1] = c  # put bracket at position p
                            del tgt_gens[q - 1]  # remove position q

                            # Sign: from moving a_q past generators between p and q
                            # In the wedge product, removing position q introduces
                            # a sign (-1)^{q-p-1} from commuting past intermediate elements
                            sign = (-1) ** (q - p - 1)

                            tgt_tensor_idx = tensor_to_idx(tgt_gens, dim_g)
                            row = tgt_tensor_idx * dim_os_target + os_tgt_idx

                            rows.append(row)
                            cols.append(col)
                            vals.append(sign * bracket_coeff * res_coeff)

    # Build dense matrix
    M = np.zeros((target_dim, source_dim))
    for r, c, v in zip(rows, cols, vals):
        M[r, c] += v

    return M


# ============================================================
# Main computation
# ============================================================

def compute_bar_cohomology(f_abc: np.ndarray, name: str, max_degree: int = 5):
    """Compute bar cohomology for a Lie algebra with structure tensor f_abc."""
    dim_g = f_abc.shape[0]

    print(f"\n{'=' * 60}")
    print(f"CHIRAL BAR COHOMOLOGY FOR {name} (dim g = {dim_g})")
    print(f"{'=' * 60}")

    # First verify Jacobi identity
    jacobi_err = 0
    for a in range(dim_g):
        for b in range(dim_g):
            for c in range(dim_g):
                total = np.zeros(dim_g)
                for d in range(dim_g):
                    total += f_abc[a, b, d] * f_abc[d, c, :]
                    total += f_abc[b, c, d] * f_abc[d, a, :]
                    total += f_abc[c, a, d] * f_abc[d, b, :]
                jacobi_err = max(jacobi_err, np.max(np.abs(total)))
    print(f"Jacobi identity error: {jacobi_err:.2e}")

    # Compute chain dimensions and differentials
    ranks = {}
    chain_dims = {}

    for deg in range(1, max_degree + 2):
        os_dim = factorial(deg - 1) if deg >= 1 else 1
        chain_dims[deg] = dim_g ** deg * os_dim
        print(f"\nB-bar^{deg}: dim = {dim_g}^{deg} * {os_dim} = {chain_dims[deg]}")

    for deg in range(2, max_degree + 2):
        if chain_dims[deg] > 200000:
            print(f"  d_{deg}: SKIPPED (source dim {chain_dims[deg]} too large)")
            continue

        print(f"  Building d_{deg}: B-bar^{deg}({chain_dims[deg]}) -> B-bar^{deg-1}({chain_dims[deg-1]})")
        D = chiral_bar_differential(f_abc, deg)
        r = np.linalg.matrix_rank(D, tol=1e-8)
        ranks[deg] = r
        print(f"  rank(d_{deg}) = {r}")

        # Verify d^2 = 0 (check with previous differential)
        if deg - 1 in ranks and deg - 1 >= 2:
            D_prev = chiral_bar_differential(f_abc, deg - 1)
            prod = D_prev @ D
            d2_err = np.max(np.abs(prod)) if prod.size > 0 else 0
            print(f"  d^2 check: |d_{deg-1} * d_{deg}| = {d2_err:.2e}",
                  "OK" if d2_err < 1e-8 else "FAIL!")

    # Compute cohomology
    print(f"\nBar cohomology:")
    for deg in range(1, max_degree + 1):
        dim_n = chain_dims[deg]
        r_out = ranks.get(deg, 0)  # rank of d_n (outgoing)
        r_in = ranks.get(deg + 1, 0)  # rank of d_{n+1} (incoming)
        H_n = dim_n - r_out - r_in
        print(f"  H^{deg} = {dim_n} - {r_out} - {r_in} = {H_n}")


def verify_os_basis():
    """Verify OS algebra dimensions and residue maps."""
    print("OS algebra verification:")
    for n in range(2, 6):
        basis = nbc_basis(n, n - 1)
        expected = factorial(n - 1)
        ok = "OK" if len(basis) == expected else "FAIL"
        print(f"  OS^{n-1}(C_{n}): dim = {len(basis)} (expected {expected}) {ok}")

    # Verify residue maps for n=3 (should match existing code)
    print("\nResidue maps for n=3:")
    res3 = residue_matrix(3)
    for (p, q), M in sorted(res3.items()):
        print(f"  Res_{{D_{{{p}{q}}}}}: {M.flatten()}")


if __name__ == "__main__":
    verify_os_basis()

    # Test on sl_2
    f_sl2 = sl2_structure_tensor()
    compute_bar_cohomology(f_sl2, "sl_2", max_degree=5)
