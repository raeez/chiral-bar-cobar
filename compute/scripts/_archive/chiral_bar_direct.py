#!/usr/bin/env python3
r"""Direct computation of chiral bar cohomology via OS residue maps.

The chiral bar complex B^n(A) = V^{\otimes n} \otimes OS^{n-1}(C_n)
with differential d = \sum_{i<j} [,]_{ij} \otimes Res_{ij}.

For KM algebras at level k=0 (bracket only, no Killing form):
  d_{ij}(a_1 ... a_n \otimes \omega) =
    ([a_i, a_j] at position min(i,j), delete max) \otimes \iota_{\eta_{ij}}(\omega)|_{relabel}

Key: \iota_{\eta_{ij}} is contraction (interior product) on OS forms.
The Arnold relations ensure d^2 = 0 (together with Jacobi identity).

At nonzero level k, there's an additional Killing form term (double pole),
but bar cohomology dims are conjectured level-independent for KM.
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import svds
from itertools import permutations, combinations
from math import factorial
from fractions import Fraction
import sys


# ---------------------------------------------------------------------------
# Lie algebra structure constants
# ---------------------------------------------------------------------------

def sl2_structure_constants():
    """sl_2 structure constants f^{ab}_c. Basis: e=0, h=1, f=2."""
    d = 3
    f = {}
    # [e, h] = -2e, [h, e] = 2e
    f[(0, 1, 0)] = -2; f[(1, 0, 0)] = 2
    # [e, f] = h, [f, e] = -h
    f[(0, 2, 1)] = 1; f[(2, 0, 1)] = -1
    # [h, f] = -2f, [f, h] = 2f
    f[(1, 2, 2)] = -2; f[(2, 1, 2)] = 2
    return d, f


def sl3_structure_constants():
    """sl_3 structure constants. Basis: H1=0,H2=1,E1=2,E2=3,E3=4,F1=5,F2=6,F3=7."""
    d = 8
    f = {}
    H1, H2, E1, E2, E3, F1, F2, F3 = range(8)
    CARTAN = [[2, -1], [-1, 2]]

    def sb(a, b, c, v):
        f[(a, b, c)] = f.get((a, b, c), 0) + v
        f[(b, a, c)] = f.get((b, a, c), 0) - v

    # [H_i, E_j] = A_{ij} E_j
    for i, hi in enumerate([H1, H2]):
        for j, ej in enumerate([E1, E2]):
            if CARTAN[i][j] != 0:
                sb(hi, ej, ej, CARTAN[i][j])
    # [H_i, F_j] = -A_{ij} F_j
    for i, hi in enumerate([H1, H2]):
        for j, fj in enumerate([F1, F2]):
            if CARTAN[i][j] != 0:
                sb(hi, fj, fj, -CARTAN[i][j])
    # [E_i, F_j] = delta_{ij} H_i
    sb(E1, F1, H1, 1)
    sb(E2, F2, H2, 1)
    # [E1, E2] = E3, [F2, F1] = F3
    sb(E1, E2, E3, 1)
    sb(F2, F1, F3, 1)
    # [H_i, E3] = (A_{i1}+A_{i2}) E3
    sb(H1, E3, E3, CARTAN[0][0] + CARTAN[0][1])  # 2-1=1
    sb(H2, E3, E3, CARTAN[1][0] + CARTAN[1][1])  # -1+2=1
    # [H_i, F3] = -(A_{i1}+A_{i2}) F3
    sb(H1, F3, F3, -(CARTAN[0][0] + CARTAN[0][1]))
    sb(H2, F3, F3, -(CARTAN[1][0] + CARTAN[1][1]))
    # [E3, F1] = -E2 (from [E1E2, F1] = [E1,F1]E2 = H1 E2... actually need to be careful)
    # Actually: [E3, F1] = [[E1,E2], F1] = [E1,[E2,F1]] + [[E1,F1],E2] = 0 + [H1,E2] = -E2
    sb(E3, F1, E2, -1)
    # [E3, F2] = [[E1,E2], F2] = [E1,[E2,F2]] + [[E1,F2],E2] = [E1,H2] + 0 = -(-1)E1 = E1
    sb(E3, F2, E1, 1)
    # [E3, F3] = [[E1,E2], [F2,F1]]
    # = [E1,[E2,[F2,F1]]] + [[E1,[F2,F1]],E2] (using nested Jacobi)
    # [E2, F3] = [E2, [F2,F1]] = [[E2,F2],F1] + [F2,[E2,F1]] = [H2,F1] + 0 = -(-1)F1 = F1
    # wait let me just use: [E3,F3] = H1 + H2
    sb(E3, F3, H1, 1)
    sb(E3, F3, H2, 1)
    # [E1, F3] = [E1, [F2,F1]] = [[E1,F2],F1] + [F2,[E1,F1]] = 0 + [F2,H1] = -(-2)F2...
    # Actually [F2,H1] = -[H1,F2] = -(-(-1))F2 = -F2... hmm
    # [H1,F2] = -A_{12} F2 = -(-1)F2 = F2, so [F2,H1] = -F2
    # [E1, F3] = 0 + [F2, H1] = -F2
    sb(E1, F3, F2, -1)
    # [E2, F3] = [E2, [F2,F1]] = [[E2,F2],F1] + [F2,[E2,F1]]
    # = [H2,F1] + 0 = -A_{21}F1... hmm
    # [H2,F1] = -A_{21}F1 = -(-1)F1 = F1
    sb(E2, F3, F1, 1)

    # Clean up zero entries
    f = {k: v for k, v in f.items() if v != 0}
    return d, f


# ---------------------------------------------------------------------------
# Orlik-Solomon algebra: NBC basis and residue maps
# ---------------------------------------------------------------------------

def nbc_basis_forms(n):
    """NBC basis for OS^{n-1}(C_n) (top degree).

    Returns list of frozensets of edges, each edge = (i,j) with i<j.
    These are the (n-1)-element subsets of edges of K_n that contain
    no broken circuit (where circuits are broken by removing the largest edge).

    For top degree (n-1 forms from n(n-1)/2 edges), the NBC basis has (n-1)! elements.
    """
    if n == 1:
        return [frozenset()]
    if n == 2:
        return [frozenset([(1, 2)])]

    # All edges of K_n
    edges = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]

    # Circuits of K_n: triangles {(i,j),(j,k),(i,k)} for i<j<k
    # Broken circuit: remove max edge from each circuit
    broken_circuits = set()
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                # Triangle (i,j), (i,k), (j,k). Max edge = (j,k)
                bc = frozenset([(i, j), (i, k)])
                broken_circuits.add(bc)

    # NBC basis: (n-1)-element subsets of edges containing no broken circuit
    basis = []
    for subset in combinations(edges, n - 1):
        fs = frozenset(subset)
        is_nbc = True
        for bc in broken_circuits:
            if bc.issubset(fs):
                is_nbc = False
                break
        if is_nbc:
            basis.append(fs)

    return basis


def nbc_basis_ordered(n):
    """NBC basis as ordered tuples of edges (for sign tracking).

    Returns list of tuples of edges in a canonical order.
    """
    basis_sets = nbc_basis_forms(n)
    # Order edges lexicographically within each basis element
    return [tuple(sorted(b)) for b in basis_sets]


def reduce_to_nbc(edges_tuple, n):
    """Reduce a product of OS forms to the NBC basis using Arnold relations.

    Arnold relation: eta_{ij} ^ eta_{jk} = eta_{ij} ^ eta_{ik} - eta_{ik} ^ eta_{jk}
    (for any triple i,j,k — this means eta_{jk} ^ eta_{ij} can be replaced)

    Returns: dict mapping NBC basis index -> coefficient (Fraction).
    Uses the canonical NBC basis from nbc_basis_ordered(n).
    """
    nbc = nbc_basis_ordered(n)
    nbc_sets = [frozenset(b) for b in nbc]

    edges = list(edges_tuple)
    edge_set = frozenset(edges)

    # Check if already NBC
    if edge_set in nbc_sets:
        idx = nbc_sets.index(edge_set)
        # Compute sign: parity to go from edges_tuple to nbc[idx]
        target = list(nbc[idx])
        sign = _permutation_sign(edges, target)
        return {idx: Fraction(sign)}

    # Need Arnold reduction. Use recursive approach.
    # Find the broken circuit contained in edge_set
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                bc = frozenset([(i, j), (i, k)])
                if bc.issubset(edge_set):
                    # We have edges (i,j) and (i,k) but NOT (j,k)
                    # Arnold: eta_{ij} ^ eta_{ik} = eta_{ij} ^ eta_{jk} - eta_{jk} ^ eta_{ik}
                    # Wait, the standard Arnold is:
                    # eta_{ij} ^ eta_{jk} + eta_{jk} ^ eta_{ki} + eta_{ki} ^ eta_{ij} = 0
                    # i.e. d(eta_{ij} eta_{jk}) relation
                    # Rewrite: eta_{ij} ^ eta_{ik} = eta_{ij} ^ eta_{jk} - eta_{ik} ^ eta_{jk}
                    # So if we have {..., (i,j), (i,k), ...} and (j,k) not present:
                    # We need to express eta_{(i,j)} ^ eta_{(i,k)} in terms with (j,k)

                    # Actually for NBC: edges NOT in any broken circuit.
                    # broken circuit = circuit minus max edge
                    # For triangle (i,j,k): circuit = {(i,j),(i,k),(j,k)}, max = (j,k)
                    # broken circuit = {(i,j),(i,k)}
                    # So having both (i,j) and (i,k) is bad (broken circuit).
                    # Arnold relation: eta_{(i,j)} ^ eta_{(i,k)} = eta_{(i,j)} ^ eta_{(j,k)} - eta_{(i,k)} ^ eta_{(j,k)}
                    # This replaces {(i,j),(i,k)} with {(i,j),(j,k)} and {(i,k),(j,k)}

                    other = [e for e in edges if e != (i, j) and e != (i, k)]
                    pos_ij = edges.index((i, j))
                    pos_ik = edges.index((i, k))

                    # sign from moving (i,j) and (i,k) to adjacent positions
                    # edges = [..., (i,j)@pos_ij, ..., (i,k)@pos_ik, ...]
                    # Rewrite: (-1)^parity * eta_{(i,j)} ^ eta_{(i,k)} ^ (other)

                    # Let's build the two replacement terms
                    # Term 1: {(i,j), (j,k)} ∪ other  with sign +
                    # Term 2: {(i,k), (j,k)} ∪ other  with sign -

                    # Be careful with signs from permutation
                    # Original: put (i,j) at front, (i,k) second, then other
                    perm_edges = [(i, j), (i, k)] + other
                    sign_orig = _permutation_sign(edges, perm_edges)

                    term1_edges = [(i, j), (j, k)] + other
                    term2_edges = [(i, k), (j, k)] + other

                    result = {}
                    r1 = reduce_to_nbc(tuple(term1_edges), n)
                    for idx, coeff in r1.items():
                        result[idx] = result.get(idx, Fraction(0)) + sign_orig * coeff
                    r2 = reduce_to_nbc(tuple(term2_edges), n)
                    for idx, coeff in r2.items():
                        result[idx] = result.get(idx, Fraction(0)) - sign_orig * coeff

                    return {k: v for k, v in result.items() if v != 0}

    # Should not reach here for valid OS forms
    return {}


def _permutation_sign(perm_from, perm_to):
    """Sign of the permutation taking perm_from to perm_to."""
    if sorted(perm_from) != sorted(perm_to):
        return 0
    n = len(perm_from)
    # Build permutation
    idx_map = {v: i for i, v in enumerate(perm_to)}
    perm = [idx_map[v] for v in perm_from]
    # Count inversions
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inv += 1
    return 1 if inv % 2 == 0 else -1


def os_contraction(edges_tuple, edge_ij, n):
    """Contract (interior product) of OS form with eta_{ij}.

    iota_{eta_{ij}}(eta_{a1b1} ^ ... ^ eta_{ak bk})
    = sum_l (-1)^{l-1} delta(a_l b_l, ij) * (product without l-th)

    Then relabel: merge j into i (z_j = z_i), renumber remaining
    particles 1,...,n-1.

    Returns: list of (coefficient, new_edges_tuple) after relabeling.
    """
    edges = list(edges_tuple)
    results = []

    for l, e in enumerate(edges):
        if e == edge_ij:
            sign = (-1) ** l
            remaining = edges[:l] + edges[l + 1:]
            # Relabel: merge j into i, particles > j get decremented
            i_merge, j_merge = edge_ij  # i < j
            new_edges = []
            for (a, b) in remaining:
                # Replace j with i
                a2 = i_merge if a == j_merge else a
                b2 = i_merge if b == j_merge else b
                # Decrement indices > j
                if a2 > j_merge:
                    a2 -= 1
                if b2 > j_merge:
                    b2 -= 1
                # Normalize to (min, max)
                if a2 > b2:
                    a2, b2 = b2, a2
                    sign *= -1  # swapping edge orientation = sign
                if a2 == b2:
                    return []  # degenerate, shouldn't happen
                new_edges.append((a2, b2))
            results.append((Fraction(sign), tuple(new_edges)))

    return results


# ---------------------------------------------------------------------------
# Bar differential: exact rational computation
# ---------------------------------------------------------------------------

def build_bar_differential(dim_g, structure_consts, n):
    """Build the bar differential d: B^n -> B^{n-1} as a sparse matrix.

    B^n = g^{⊗n} ⊗ OS^{n-1}(C_n)
    d = sum_{i<j} [,]_{ij} ⊗ Res_{ij}

    Returns: sparse matrix (rational entries stored as float64).
    """
    if n <= 1:
        return None

    d = dim_g

    # Source: B^n
    src_nbc = nbc_basis_ordered(n)
    dim_src_os = len(src_nbc)
    dim_src = d ** n * dim_src_os

    # Target: B^{n-1}
    tgt_nbc = nbc_basis_ordered(n - 1)
    dim_tgt_os = len(tgt_nbc)
    dim_tgt = d ** (n - 1) * dim_tgt_os

    if n == 2:
        dim_tgt_os = 1  # OS^0 = C
        dim_tgt = d

    print(f"  Building d: B^{n} ({dim_src}) -> B^{n-1} ({dim_tgt})")

    # Build sparse matrix entries
    rows, cols, vals = [], [], []

    # Precompute OS contractions for each (edge, basis element) pair
    os_contractions = {}
    for s_idx, src_form in enumerate(src_nbc):
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                edge = (i, j)
                contr = os_contraction(src_form, edge, n)
                if contr:
                    os_contractions[(s_idx, edge)] = contr

    # Precompute target NBC index map
    if n - 1 >= 2:
        tgt_nbc_map = {frozenset(b): idx for idx, b in enumerate(tgt_nbc)}

    # For each source basis element
    for src_tensor_idx in range(d ** n):
        # Decode tensor index to generator tuple
        gens = []
        temp = src_tensor_idx
        for _ in range(n):
            gens.append(temp % d)
            temp //= d

        for s_os_idx, src_form in enumerate(src_nbc):
            src_col = src_tensor_idx * dim_src_os + s_os_idx

            # Sum over pairs (i,j)
            for i in range(1, n + 1):
                for j in range(i + 1, n + 1):
                    edge = (i, j)

                    # OS contraction
                    key = (s_os_idx, edge)
                    if key not in os_contractions:
                        continue

                    # Lie bracket [a_i, a_j]
                    a_i = gens[i - 1]
                    a_j = gens[j - 1]

                    for c in range(d):
                        f_val = structure_consts.get((a_i, a_j, c), 0)
                        if f_val == 0:
                            continue

                        # Build target generator tuple:
                        # merged point at position min(i,j)=i gets bracket result c
                        # other generators shift
                        tgt_gens = []
                        for pos in range(1, n + 1):
                            if pos == j:
                                continue  # deleted
                            elif pos == i:
                                tgt_gens.append(c)
                            else:
                                tgt_gens.append(gens[pos - 1])

                        # Target tensor index
                        tgt_tensor_idx = 0
                        for k in range(len(tgt_gens) - 1, -1, -1):
                            tgt_tensor_idx = tgt_tensor_idx * d + tgt_gens[k]

                        # OS form contribution
                        for (os_coeff, new_form) in os_contractions[key]:
                            if n - 1 == 1:
                                # B^1: OS^0 = C, single basis element
                                tgt_os_idx = 0
                                tgt_row = tgt_tensor_idx
                            else:
                                # Need to express new_form in NBC basis
                                if len(new_form) == 0:
                                    tgt_os_idx = 0
                                    tgt_row = tgt_tensor_idx * dim_tgt_os + tgt_os_idx
                                else:
                                    new_form_set = frozenset(new_form)
                                    if new_form_set in tgt_nbc_map:
                                        tgt_os_idx = tgt_nbc_map[new_form_set]
                                        # Sign from reordering
                                        sign = _permutation_sign(
                                            list(new_form), list(tgt_nbc[tgt_os_idx])
                                        )
                                        tgt_row = tgt_tensor_idx * dim_tgt_os + tgt_os_idx
                                        os_coeff *= sign
                                    else:
                                        # Need Arnold reduction
                                        reduced = reduce_to_nbc(new_form, n - 1)
                                        for t_idx, r_coeff in reduced.items():
                                            tgt_row2 = tgt_tensor_idx * dim_tgt_os + t_idx
                                            val = float(f_val * os_coeff * r_coeff)
                                            if abs(val) > 1e-15:
                                                rows.append(tgt_row2)
                                                cols.append(src_col)
                                                vals.append(val)
                                        continue

                            val = float(f_val * os_coeff)
                            if abs(val) > 1e-15:
                                rows.append(tgt_row)
                                cols.append(src_col)
                                vals.append(val)

    M = sparse.csr_matrix(
        (vals, (rows, cols)), shape=(dim_tgt, dim_src)
    )
    return M


def compute_bar_cohomology(dim_g, structure_consts, name, max_deg=5, expected=None):
    """Compute chiral bar cohomology H^n = ker(d_n) / im(d_{n+1})."""
    d = dim_g

    print(f"\n{'=' * 60}")
    print(f"CHIRAL BAR COHOMOLOGY: {name}")
    print(f"dim g = {d}")
    print(f"{'=' * 60}")

    # Build differentials
    diffs = {}
    for deg in range(2, max_deg + 2):
        nbc = nbc_basis_ordered(deg)
        dim_chain = d ** deg * len(nbc)
        if dim_chain > 2_000_000:
            print(f"  Degree {deg}: {dim_chain} dims, skipping (too large)")
            break
        diffs[deg] = build_bar_differential(dim_g, structure_consts, deg)

    # Check d^2 = 0
    for deg in range(3, max_deg + 2):
        if deg in diffs and deg - 1 in diffs and diffs[deg] is not None and diffs[deg - 1] is not None:
            dd = diffs[deg - 1] @ diffs[deg]
            max_err = abs(dd).max() if dd.nnz > 0 else 0
            print(f"  |d_{deg-1} d_{deg}| = {max_err:.2e}")

    print()

    # Compute cohomology
    for deg in range(1, max_deg + 1):
        nbc_deg = nbc_basis_ordered(deg)
        dim_chain = d ** deg * len(nbc_deg)

        # ker(d_deg)
        if deg in diffs and diffs[deg] is not None:
            D = diffs[deg]
            ker_dim = dim_chain - matrix_rank_sparse(D)
        else:
            ker_dim = dim_chain  # d = 0 means everything is in kernel

        # im(d_{deg+1})
        if deg + 1 in diffs and diffs[deg + 1] is not None:
            im_dim = matrix_rank_sparse(diffs[deg + 1])
        else:
            im_dim = 0

        h_n = ker_dim - im_dim

        exp_str = ""
        if expected and deg <= len(expected):
            match = "OK" if h_n == expected[deg - 1] else "MISMATCH"
            exp_str = f"  (expected {expected[deg - 1]}: {match})"

        print(f"  H^{deg} = ker({ker_dim}) - im({im_dim}) = {h_n}{exp_str}")


def matrix_rank_sparse(M):
    """Compute rank of a sparse matrix."""
    if M is None:
        return 0
    M_dense = M.toarray()
    return np.linalg.matrix_rank(M_dense, tol=1e-8)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # sl_2: expected Riordan numbers R(n+3): 3, 6, 15, 36, 91
    d2, sc2 = sl2_structure_constants()
    compute_bar_cohomology(
        d2, sc2, "sl_2", max_deg=5,
        expected=[3, 6, 15, 36, 91]
    )

    # sl_3: expected 8, 36, 204, ?, ?
    d3, sc3 = sl3_structure_constants()
    compute_bar_cohomology(
        d3, sc3, "sl_3", max_deg=4,
        expected=[8, 36, 204]
    )
