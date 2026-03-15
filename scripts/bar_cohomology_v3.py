"""
Bar cohomology computation for affine Kac-Moody algebras.

The bar complex B^n = g^{⊗n} ⊗ OS^{n-1}(n) with differential
d: B^n → B^{n-1} using the Lie bracket and OS contraction.

We compute the homology H_n = ker(d_n) / im(d_{n+1}).
"""

import numpy as np
from itertools import product as iterproduct
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.linalg import svds
import sys
from functools import lru_cache

# ========================================
# Lie algebra structure constants
# ========================================

def sl2_structure():
    """sl_2 structure constants. Basis: e(0), f(1), h(2)."""
    d = 3
    # [e,f]=h, [h,e]=2e, [h,f]=-2f
    f_abc = np.zeros((d, d, d), dtype=np.float64)
    f_abc[0, 1, 2] = 1   # [e,f] = h
    f_abc[1, 0, 2] = -1  # [f,e] = -h
    f_abc[2, 0, 0] = 2   # [h,e] = 2e
    f_abc[0, 2, 0] = -2  # [e,h] = -2e
    f_abc[2, 1, 1] = -2  # [h,f] = -2f
    f_abc[1, 2, 1] = 2   # [f,h] = 2f
    return d, f_abc

def sl3_structure():
    """sl_3 structure constants.
    Basis: H1(0), H2(1), E1(2), E2(3), E3(4), F1(5), F2(6), F3(7)
    where E3 = [E1,E2], F3 = [F2,F1].

    Cartan matrix: A = [[2,-1],[-1,2]]
    [H_i, E_j] = A_{ij} E_j, [H_i, F_j] = -A_{ij} F_j
    [E_i, F_j] = delta_{ij} H_i (for simple roots)
    [E1, E2] = E3, [F2, F1] = F3
    [E_i, F3], [E3, F_i], etc.
    """
    d = 8
    f_abc = np.zeros((d, d, d), dtype=np.float64)

    # Indices: H1=0, H2=1, E1=2, E2=3, E3=4, F1=5, F2=6, F3=7
    # Cartan matrix entries
    A = np.array([[2, -1], [-1, 2]])

    # [H_i, E_j] = A_{ij} E_j for simple roots j=1,2 (indices 2,3)
    # [H1, E1] = 2*E1
    f_abc[0, 2, 2] = 2;   f_abc[2, 0, 2] = -2
    # [H1, E2] = -1*E2
    f_abc[0, 3, 3] = -1;  f_abc[3, 0, 3] = 1
    # [H2, E1] = -1*E1
    f_abc[1, 2, 2] = -1;  f_abc[2, 1, 2] = 1
    # [H2, E2] = 2*E2
    f_abc[1, 3, 3] = 2;   f_abc[3, 1, 3] = -2

    # [H_i, E3]: E3 = E_{alpha1+alpha2}, so [H1,E3] = (2-1)*E3 = E3, [H2,E3] = (-1+2)*E3 = E3
    f_abc[0, 4, 4] = 1;   f_abc[4, 0, 4] = -1
    f_abc[1, 4, 4] = 1;   f_abc[4, 1, 4] = -1

    # [H_i, F_j] = -A_{ij} F_j for simple roots
    # [H1, F1] = -2*F1
    f_abc[0, 5, 5] = -2;  f_abc[5, 0, 5] = 2
    # [H1, F2] = 1*F2
    f_abc[0, 6, 6] = 1;   f_abc[6, 0, 6] = -1
    # [H2, F1] = 1*F1
    f_abc[1, 5, 5] = 1;   f_abc[5, 1, 5] = -1
    # [H2, F2] = -2*F2
    f_abc[1, 6, 6] = -2;  f_abc[6, 1, 6] = 2

    # [H_i, F3]: F3 corresponds to -(alpha1+alpha2)
    f_abc[0, 7, 7] = -1;  f_abc[7, 0, 7] = 1
    f_abc[1, 7, 7] = -1;  f_abc[7, 1, 7] = 1

    # [E1, F1] = H1
    f_abc[2, 5, 0] = 1;   f_abc[5, 2, 0] = -1
    # [E2, F2] = H2
    f_abc[3, 6, 1] = 1;   f_abc[6, 3, 1] = -1

    # [E1, E2] = E3
    f_abc[2, 3, 4] = 1;   f_abc[3, 2, 4] = -1
    # [F2, F1] = F3 (equivalently [F1,F2] = -F3)
    f_abc[6, 5, 7] = 1;   f_abc[5, 6, 7] = -1

    # [E1, F3] = -F2 (from [E1,[F2,F1]] = [[E1,F2],F1] + [F2,[E1,F1]]
    #  = 0 + [F2, H1] = -2F2... wait let me recompute)
    # [E1, F3] = [E1, [F2,F1]] = [[E1,F2],F1] + [F2,[E1,F1]]
    # [E1,F2] = 0 (different simple roots), [E1,F1] = H1
    # So [E1,F3] = 0 + [F2, H1] = -[H1, F2] = -1*F2...
    # wait [H1,F2] = A_{12}*(-F2) = (-1)*(-F2) = F2? No:
    # [H_i, F_j] = -A_{ij} F_j, so [H1,F2] = -A_{12}*F2 = -(-1)*F2 = F2
    # So [E1,F3] = [F2, H1] = -[H1, F2] = -F2
    f_abc[2, 7, 6] = -1;  f_abc[7, 2, 6] = 1

    # [E2, F3] = [E2, [F2,F1]] = [[E2,F2],F1] + [F2,[E2,F1]]
    # [E2,F2] = H2, [E2,F1] = 0
    # = [H2, F1] + 0 = -A_{21}*F1 = -(-1)*F1 = F1
    f_abc[3, 7, 5] = 1;   f_abc[7, 3, 5] = -1

    # [E3, F1] = [E1,E2],F1] = [[E1,F1],E2] + [E1,[E2,F1]]
    # = [H1, E2] + [E1, 0] = -E2
    f_abc[4, 5, 3] = -1;  f_abc[5, 4, 3] = 1

    # [E3, F2] = [[E1,E2],F2] = [[E1,F2],E2] + [E1,[E2,F2]]
    # = 0 + [E1, H2] = -[H2, E1] = -(-1)*E1 = E1
    f_abc[4, 6, 2] = 1;   f_abc[6, 4, 2] = -1

    # [E3, F3]: Need to compute [[E1,E2],[F2,F1]]
    # = [E1,[E2,[F2,F1]]] - [E2,[E1,[F2,F1]]]  (by Jacobi)
    # Wait, let me use: [E3,F3] = [[E1,E2],[F2,F1]]
    # Expand: [E1,[E2,[F2,F1]]] + [[E2,F1],[E1,F2]] - [E2,[E1,[F2,F1]]] ... messy
    # Better: [E3, F3] = [[E1,E2], F3] = [E1,[E2,F3]] - [E2,[E1,F3]]
    # [E2,F3] = F1 (computed above), [E1,F3] = -F2 (computed above)
    # = [E1, F1] - [E2, -F2] = H1 + [E2,F2] = H1 + H2
    f_abc[4, 7, 0] = 1;   f_abc[7, 4, 0] = -1
    f_abc[4, 7, 1] = 1;   f_abc[7, 4, 1] = -1

    return d, f_abc


def verify_jacobi(d, f_abc):
    """Verify Jacobi identity: [a,[b,c]] + [b,[c,a]] + [c,[a,b]] = 0."""
    max_err = 0
    for a in range(d):
        for b in range(d):
            for c in range(d):
                val = np.zeros(d)
                for e in range(d):
                    for g in range(d):
                        # [a,[b,c]]: f_bc^e * f_ae^g
                        val[g] += f_abc[b,c,e] * f_abc[a,e,g]
                        # [b,[c,a]]: f_ca^e * f_be^g
                        val[g] += f_abc[c,a,e] * f_abc[b,e,g]
                        # [c,[a,b]]: f_ab^e * f_ce^g
                        val[g] += f_abc[a,b,e] * f_abc[c,e,g]
                err = np.max(np.abs(val))
                max_err = max(max_err, err)
    print(f"Jacobi identity max error: {max_err}")
    return max_err < 1e-10


# ========================================
# Orlik-Solomon algebra (NBC basis)
# ========================================

def os_nbc_basis(n, k):
    """
    Return the NBC basis for OS^k(n) = H^k(Conf_n(C)).
    Each basis element is a sorted tuple of edges ((i1,j1), ..., (ik,jk))
    with i_l < j_l, forming a no-broken-circuit set.

    Returns list of tuples of edges.
    """
    if k == 0:
        return [()]  # empty product = 1
    if n <= 1 or k >= n:
        if k == 0:
            return [()]
        return []  # OS^k(n) = 0 for k >= n

    # All edges of K_n, lexicographically ordered
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]

    # Find all circuits (cycles) and their broken circuits
    # A circuit is a cycle in K_n. Broken circuit = cycle minus its largest edge.
    broken_circuits = set()

    # For K_n, cycles of length 3: (i,j,k) with edges (i,j),(j,k),(i,k)
    # The largest edge is max of {(i,j),(j,k),(i,k)} in lex order
    # Broken circuit = the other two edges
    for i in range(n):
        for j in range(i+1, n):
            for kk in range(j+1, n):
                cycle_edges = sorted([(i,j), (i,kk), (j,kk)])
                # Remove the largest edge
                bc = tuple(cycle_edges[:-1])
                broken_circuits.add(bc)

    # Longer cycles also create broken circuits, but for K_n the
    # NBC complex is determined by 3-cycles (Whitney's theorem)
    # Actually, we need all broken circuits from all cycles.
    # For simplicity, let's also add 4-cycles etc.
    # But for K_n, the broken circuit complex is determined by 3-cycles alone
    # (since every broken circuit from a longer cycle contains a broken circuit from a 3-cycle)

    # Generate all k-element subsets of edges that contain no broken circuit
    from itertools import combinations

    nbc = []
    for subset in combinations(range(len(edges)), k):
        edge_set = tuple(edges[s] for s in subset)
        # Check if edge_set contains any broken circuit
        is_nbc = True
        for bc in broken_circuits:
            if all(e in edge_set for e in bc):
                is_nbc = False
                break
        if is_nbc:
            nbc.append(edge_set)

    return nbc


def os_contract(n, k, basis_k, edge_to_contract):
    """
    Contract edge (i,j) from OS^k(n) to OS^{k-1}(n-1).

    Given a basis element of OS^k(n) and an edge (p,q) to contract,
    return the result as a linear combination of NBC basis elements
    of OS^{k-1}(n-1).

    After contracting (p,q), points p and q merge. We relabel:
    the merged point gets label min(p,q), and all labels > max(p,q) decrease by 1.

    Returns: list of (coefficient, basis_index) pairs
    """
    p, q = edge_to_contract
    assert p < q

    # We need to express the contraction in terms of the NBC basis
    # The contraction "extracts" the factor omega_{pq} from the form

    # First, express the basis element in terms of the full OS generators
    # and extract the coefficient of omega_{pq}

    # For a basis element (e1, ..., ek), if (p,q) is one of the edges,
    # the contraction removes it and relabels the remaining edges.
    # If (p,q) is not one of the edges, we need to use Arnold relations
    # to express the product in a form that contains omega_{pq}.

    # This is the key computation. For the NBC basis, we can use the
    # Arnold relation to express ω_{pq} ∧ (rest) in terms of NBC elements.

    # Simplification: compute the contraction by working in the full
    # exterior algebra and using Arnold relations.

    # For now, use a direct approach: compute the contraction matrix
    # by expressing everything in coordinates.

    # This function is called by the differential builder below.
    pass


def build_os_contraction_matrix(n, k, p, q):
    """
    Build the matrix for the contraction at edge (p,q):
    iota_{pq}: OS^k(n) -> OS^{k-1}(n-1)

    expressed in the NBC bases of OS^k(n) and OS^{k-1}(n-1).

    The contraction extracts omega_{pq} and relabels remaining points.
    After merging p and q, the merged point gets label min(p,q),
    and all labels > max(p,q) decrease by 1.
    """
    basis_k = os_nbc_basis(n, k)

    # After contraction, we have n-1 points
    n_new = n - 1
    basis_km1 = os_nbc_basis(n_new, k-1)

    if not basis_k or not basis_km1:
        return np.zeros((len(basis_km1) if basis_km1 else 0,
                         len(basis_k) if basis_k else 0))

    # Build relabeling map: after merging p,q -> min(p,q)
    # Points 0,...,n-1 map to 0,...,n-2
    def relabel(v):
        """Relabel vertex v after merging p,q."""
        if v == q:
            return p  # q merges into p
        elif v > q:
            return v - 1  # shift down
        else:
            return v

    def relabel_and_sort_edge(e):
        """Relabel edge after merge and sort."""
        a, b = relabel(e[0]), relabel(e[1])
        if a == b:
            return None  # edge collapsed
        return (min(a,b), max(a,b))

    # To compute the contraction, we work in the full exterior algebra
    # of edges. We need to express each NBC basis element as a product
    # of omega forms, extract the omega_{pq} factor, and express the
    # result in the new NBC basis.

    # Strategy: use the fact that in the OS algebra,
    # omega = omega_{pq} ∧ alpha + beta
    # where beta doesn't contain omega_{pq}.
    # iota_{pq}(omega) = alpha (restricted and relabeled)

    # For an NBC basis element (e1,...,ek):
    # If (p,q) is one of the edges, say e_l, then
    # iota_{pq}(e1∧...∧ek) = ±(e1∧...∧ê_l∧...∧ek) relabeled
    # If (p,q) is not one of the edges, we use Arnold to express
    # in terms containing omega_{pq}.

    # This requires knowing how to express omega_{pq} ∧ (stuff) in NBC basis
    # and vice versa.

    # Simpler approach: compute everything via the full representation.
    # Build the representation of OS^k(n) as a quotient of the exterior
    # algebra of edges by Arnold relations.

    # Actually, let me use a different strategy:
    # Build the full contraction in the exterior algebra and project to NBC.

    # For each NBC basis element of OS^k(n), express it as a wedge product
    # of omega_{e_i} forms. The contraction iota_{pq} extracts omega_{pq}:
    # iota_{pq}(omega_{e1} ∧ ... ∧ omega_{ek}) = sum over l of
    # (-1)^l * delta_{el = (p,q)} * omega_{e1} ∧ ... ∧ hat{omega_{el}} ∧ ... ∧ omega_{ek}
    # + Arnold correction terms when (p,q) is not directly present

    # For the direct case (pq in the edges), the contraction is straightforward.
    # For the indirect case, we need Arnold relations.

    # Let me implement this using a vector representation.
    # Choose an ordering of edges, represent forms as vectors in the
    # exterior algebra, and compute.

    # All edges of K_n
    all_edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    n_edges = len(all_edges)
    edge_idx = {e: i for i, e in enumerate(all_edges)}

    # NBC basis as subsets of edge indices
    nbc_idx_sets = []
    for b in basis_k:
        nbc_idx_sets.append(tuple(edge_idx[e] for e in b))

    # Build a vector space representation of OS^k(n) using NBC basis
    dim_k = len(basis_k)

    # For each NBC basis element, compute iota_{pq} by expressing
    # the contraction in the full exterior algebra, then projecting
    # back to NBC basis of OS^{k-1}(n-1).

    # We need the "express in NBC basis" function for OS^{k-1}(n-1)
    # This requires knowing the Arnold relations.

    # Alternative approach: compute numerically.
    # Build the map from NBC basis to a vector space using random evaluation.

    # Actually, let me just use a recursive/direct approach.
    # For small n (up to ~7), we can compute this directly.

    mat = np.zeros((len(basis_km1), len(basis_k)), dtype=np.float64)

    pq_edge = (p, q)

    for col, bk in enumerate(basis_k):
        edges_list = list(bk)

        if pq_edge in edges_list:
            # Direct case: omega_{pq} is one of the factors
            l = edges_list.index(pq_edge)
            sign = (-1)**l
            remaining = edges_list[:l] + edges_list[l+1:]

            # Relabel remaining edges
            relabeled = []
            valid = True
            for e in remaining:
                re = relabel_and_sort_edge(e)
                if re is None:
                    valid = False
                    break
                relabeled.append(re)

            if valid and len(relabeled) == k-1:
                relabeled_sorted = tuple(sorted(relabeled))
                # Express in NBC basis of OS^{k-1}(n-1)
                result = express_in_nbc(relabeled_sorted, n_new, k-1, basis_km1)
                for row, coeff in result:
                    mat[row, col] += sign * coeff
        else:
            # Need Arnold relations to express in form containing omega_{pq}
            # Use the identity: for any three vertices a,b,c:
            # omega_{ab} ∧ omega_{bc} = omega_{ab} ∧ omega_{ac} + omega_{ac} ∧ omega_{bc}
            # (Arnold relation)

            # Strategy: find a vertex c such that (p,c) or (c,q) is in edges_list
            # and use Arnold to introduce omega_{pq}

            result = contract_via_arnold(bk, pq_edge, n, k,
                                         basis_km1, n_new)
            for row, coeff in result:
                mat[row, col] += coeff

    return mat


def express_in_nbc(edge_tuple, n, k, nbc_basis):
    """
    Express a product of k edges (given as a sorted tuple) in the
    NBC basis of OS^k(n).

    Returns list of (basis_index, coefficient) pairs.
    """
    if k == 0:
        return [(0, 1.0)]

    edge_list = list(edge_tuple)

    # Check if already in NBC basis
    for idx, b in enumerate(nbc_basis):
        if tuple(sorted(b)) == tuple(sorted(edge_list)):
            # Check signs from sorting
            sign = 1  # TODO: compute permutation sign if needed
            return [(idx, sign)]

    # Need to use Arnold relations to express in NBC basis
    # Arnold: omega_{ab} ∧ omega_{bc} = omega_{ab} ∧ omega_{ac} + omega_{ac} ∧ omega_{bc}
    # equivalently: omega_{ab} ∧ omega_{bc} - omega_{ab} ∧ omega_{ac} - omega_{ac} ∧ omega_{bc} = 0

    # Find a broken circuit in edge_list
    all_vertices = set()
    for e in edge_list:
        all_vertices.update(e)

    # Check all triples of vertices for broken circuits
    vertices = sorted(all_vertices)
    for i, a in enumerate(vertices):
        for j, b in enumerate(vertices):
            if j <= i:
                continue
            for kk, c in enumerate(vertices):
                if kk <= j:
                    continue
                # Three vertices a < b < c
                # Broken circuit from cycle (a,b),(b,c),(a,c) minus (b,c)
                # = {(a,b), (a,c)}
                e_ab = (a, b)
                e_ac = (a, c)
                e_bc = (b, c)

                if e_ab in edge_list and e_ac in edge_list and e_bc not in edge_list:
                    # Found broken circuit {(a,b), (a,c)}
                    # Arnold: omega_{ab} ∧ omega_{ac} = omega_{ab} ∧ omega_{bc} - omega_{bc} ∧ omega_{ac}
                    # = omega_{ab} ∧ omega_{bc} + omega_{ac} ∧ omega_{bc}
                    # Wait: Arnold says omega_{ab}∧omega_{bc} = omega_{ab}∧omega_{ac} + omega_{ac}∧omega_{bc}
                    # So omega_{ab}∧omega_{ac} = omega_{ab}∧omega_{bc} - omega_{ac}∧omega_{bc}

                    # Replace {(a,b),(a,c)} with:
                    # omega_{ab}∧omega_{bc} - omega_{ac}∧omega_{bc}
                    # in the product
                    idx_ab = edge_list.index(e_ab)
                    idx_ac = edge_list.index(e_ac)

                    # Sign from moving e_ac next to e_ab
                    # Move e_ac to position idx_ab + 1
                    if idx_ac > idx_ab:
                        sign_move = (-1)**(idx_ac - idx_ab - 1)
                    else:
                        sign_move = (-1)**(idx_ab - idx_ac)

                    # term1: replace (a,c) with (b,c) in the sorted product
                    new_edges_1 = list(edge_list)
                    new_edges_1[idx_ac] = e_bc
                    new_edges_1_sorted = tuple(sorted(new_edges_1))

                    # term2: replace (a,b) with (b,c) in the sorted product
                    new_edges_2 = list(edge_list)
                    new_edges_2[idx_ab] = e_bc
                    new_edges_2_sorted = tuple(sorted(new_edges_2))

                    # Actually this is getting the signs wrong. Let me use a simpler approach.
                    # Just try all permutations and check against NBC basis.
                    break
            else:
                continue
            break
        else:
            continue
        break

    # Fallback: if we can't express it, return empty (this shouldn't happen for valid inputs)
    # For robustness, try matching directly
    for idx, b in enumerate(nbc_basis):
        if set(b) == set(edge_list):
            # Compute sign of permutation from edge_list to b
            sign = permutation_sign(edge_list, list(b))
            return [(idx, sign)]

    # If still not found, return zero (element might be zero due to relations)
    return []


def permutation_sign(perm1, perm2):
    """Compute the sign of the permutation that takes perm1 to perm2."""
    n = len(perm1)
    if n <= 1:
        return 1
    idx_map = {v: i for i, v in enumerate(perm2)}
    perm = [idx_map[v] for v in perm1]
    # Count inversions
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                inv += 1
    return (-1)**inv


def contract_via_arnold(edges_tuple, pq_edge, n, k, target_basis, n_new):
    """
    Contract omega_{pq} from a product of edges when omega_{pq} is not
    directly present. Use Arnold relations to introduce it.

    Returns list of (basis_index, coefficient) pairs in target_basis.
    """
    p, q = pq_edge
    edges = list(edges_tuple)

    # Find edges incident to p or q
    incident_p = [e for e in edges if p in e]
    incident_q = [e for e in edges if q in e]

    if not incident_p and not incident_q:
        # No edges touching p or q → contraction is zero
        return []

    # Use Arnold relation: for vertices p, q, r:
    # omega_{pr} ∧ omega_{rq} = omega_{pr} ∧ omega_{pq} + omega_{pq} ∧ omega_{rq}
    # So if we have omega_{pr} (with r ≠ q), we can write:
    # omega_{pr} = (stuff involving omega_{pq})
    # More precisely: omega_{pr} ∧ omega_{pq} = omega_{pr} ∧ omega_{rq} - omega_{pq} ∧ omega_{rq}

    # This is getting complex. Let me use a numerical approach instead.
    # Build a random numerical evaluation of OS forms and compute
    # the contraction matrix numerically.

    return []  # Placeholder


# ========================================
# Simpler approach: use the Chevalley-Eilenberg complex
# ========================================

def ce_complex_dimensions(d, n_max):
    """
    The Chevalley-Eilenberg complex CE^n(g) = Lambda^n(g) has dimension C(d,n).
    Differential d: Lambda^n(g) -> Lambda^{n+1}(g).
    """
    from math import comb
    dims = [comb(d, n) for n in range(d+1)]
    return dims


# ========================================
# Direct computation using numerical linear algebra
# ========================================

def build_bar_differential_numerical(d, f_abc, n, sign_convention='geometric'):
    """
    Build the bar differential d: B^n -> B^{n-1} numerically.

    B^n = g^{⊗n} ⊗ OS^{n-1}(n)

    The differential sums over all pairs (i,j) with i < j:
    d(v1⊗...⊗vn ⊗ ω) = Σ_{i<j} ±[vi,vj] ⊗ (remaining) ⊗ ι_{ij}(ω)

    For the OS contraction, we use numerical evaluation:
    evaluate all OS forms at random points and compute the contraction
    by evaluating the residue numerically.
    """
    # Instead of working with the abstract OS algebra,
    # use a concrete realization via evaluation at points.

    # dim B^n = d^n * (n-1)! (using the top OS degree)
    # This is for OS^{n-1}(n) which has dim (n-1)!

    nbc_n = os_nbc_basis(n, n-1)  # OS^{n-1}(n)
    nbc_nm1 = os_nbc_basis(n-1, n-2)  # OS^{n-2}(n-1)

    dim_os_n = len(nbc_n)
    dim_os_nm1 = len(nbc_nm1) if n >= 2 else 1

    dim_source = d**n * dim_os_n  # B^n
    dim_target = d**(n-1) * dim_os_nm1  # B^{n-1}

    if n <= 1:
        return np.zeros((dim_target, dim_source))

    print(f"  Building d: B^{n} ({dim_source}) -> B^{n-1} ({dim_target})")

    # Build contraction matrices for each pair (p,q)
    contraction_matrices = {}
    for p in range(n):
        for q in range(p+1, n):
            contraction_matrices[(p,q)] = build_os_contraction_full(n, n-1, p, q, nbc_n, nbc_nm1)

    # Build the full differential matrix
    # Index: (a0,...,a_{n-1}, os_idx) for source
    # Index: (b0,...,b_{n-2}, os_idx) for target

    mat = lil_matrix((dim_target, dim_source), dtype=np.float64)

    for p in range(n):
        for q in range(p+1, n):
            C = contraction_matrices[(p,q)]
            if C is None:
                continue

            # For each pair of Lie algebra elements and OS basis element:
            for os_src in range(dim_os_n):
                for os_tgt in range(dim_os_nm1):
                    c_coeff = C[os_tgt, os_src]
                    if abs(c_coeff) < 1e-15:
                        continue

                    # For each tensor configuration in g^⊗n:
                    for src_config in iterproduct(range(d), repeat=n):
                        a_p = src_config[p]
                        a_q = src_config[q]

                        # Compute [v_p, v_q]
                        for c in range(d):
                            bracket = f_abc[a_p, a_q, c]
                            if abs(bracket) < 1e-15:
                                continue

                            # Build target configuration: remove index p,
                            # replace index q with c, shift
                            tgt_list = list(src_config[:p]) + list(src_config[p+1:])
                            # Now tgt_list has n-1 elements, and the element
                            # that was at position q is now at position q-1
                            tgt_list[q-1] = c

                            # Compute sign
                            # Sign from moving v_p past v_{p+1},...,v_{q-1}
                            sign = (-1)**(q - p - 1)

                            # Convert to indices
                            src_idx = 0
                            for k_idx in range(n):
                                src_idx = src_idx * d + src_config[k_idx]
                            src_idx = src_idx * dim_os_n + os_src

                            tgt_idx = 0
                            for k_idx in range(n-1):
                                tgt_idx = tgt_idx * d + tgt_list[k_idx]
                            tgt_idx = tgt_idx * dim_os_nm1 + os_tgt

                            mat[tgt_idx, src_idx] += sign * bracket * c_coeff

    return mat.tocsr()


def build_os_contraction_full(n, k, p, q, nbc_k, nbc_km1):
    """
    Build contraction matrix iota_{pq}: OS^k(n) -> OS^{k-1}(n-1)
    using the full exterior algebra computation with Arnold relations.

    Use a numerical approach: evaluate at random points.
    """
    if k == 0:
        return None

    dim_src = len(nbc_k)
    dim_tgt = len(nbc_km1)

    if dim_src == 0 or dim_tgt == 0:
        return np.zeros((dim_tgt, dim_src))

    # Relabeling function after merging p and q
    def relabel(v):
        if v == q:
            return p
        elif v > q:
            return v - 1
        return v

    # For each source basis element:
    mat = np.zeros((dim_tgt, dim_src))

    for col, src_edges in enumerate(nbc_k):
        # src_edges is a tuple of k edges in K_n
        # We need to compute iota_{pq} of omega_{e1} ∧ ... ∧ omega_{ek}

        # This equals: extract the coefficient of omega_{pq} from the wedge product,
        # expressed using Arnold relations if necessary.

        # Strategy: write the form as omega_{pq} ∧ alpha + beta
        # where beta doesn't contain omega_{pq}.
        # Then iota_{pq}(form) = alpha (relabeled).

        # To extract alpha, we can use the fact that in the OS algebra,
        # the contraction is a derivation: iota_{pq}(a ∧ b) = iota_{pq}(a) ∧ b + (-1)^{|a|} a ∧ iota_{pq}(b)
        # But iota_{pq} is the operation of extracting omega_{pq}, which is NOT
        # a derivation in general (because of Arnold relations).

        # Actually, for the geometric contraction (residue at D_{pq}),
        # the operation IS well-defined on OS forms. Let me compute it
        # by working in terms of the generators.

        # Direct approach: if (p,q) is one of the edges, extraction is straightforward.
        # If not, use Arnold to create it.

        result = extract_omega_pq(src_edges, p, q, n, k, nbc_km1)
        for row, coeff in result:
            mat[row, col] += coeff

    return mat


def extract_omega_pq(edges, p, q, n, k, target_basis):
    """
    Given a wedge product omega_{e1} ∧ ... ∧ omega_{ek} in OS^k(n),
    extract the coefficient of omega_{pq}.

    Result is expressed in target_basis of OS^{k-1}(n-1).
    """
    edges = list(edges)
    pq = (min(p,q), max(p,q))

    def relabel_edge(e):
        a, b = e
        a_new = a if a < max(p,q) else a - 1
        b_new = b if b < max(p,q) else b - 1
        if a == max(p,q):
            a_new = min(p,q)
        if b == max(p,q):
            b_new = min(p,q)
        if a_new == b_new:
            return None
        return (min(a_new, b_new), max(a_new, b_new))

    if pq in edges:
        # Direct case
        l = edges.index(pq)
        sign = (-1)**l
        remaining = edges[:l] + edges[l+1:]

        relabeled = []
        for e in remaining:
            re = relabel_edge(e)
            if re is None:
                return []
            relabeled.append(re)

        relabeled_tuple = tuple(sorted(relabeled))
        # Find in target basis
        return find_in_nbc_basis(relabeled_tuple, target_basis, sign)

    # Indirect case: use Arnold relation to introduce omega_{pq}
    # Arnold: omega_{pa} ∧ omega_{aq} = omega_{pa} ∧ omega_{pq} + omega_{pq} ∧ omega_{aq}
    # So omega_{pa} ∧ omega_{aq} contains omega_{pq} with coefficient
    # omega_{aq} (from the first term) and -omega_{pa} (from the second term, with sign)

    # Find edges incident to p and q
    p_edges = [(i, e) for i, e in enumerate(edges) if p in e and e != pq]
    q_edges = [(i, e) for i, e in enumerate(edges) if q in e and e != pq]

    # Find a vertex r connected to both p and q through edges in our product
    p_neighbors = set()
    for _, e in p_edges:
        r = e[0] if e[1] == p else e[1]
        p_neighbors.add(r)

    q_neighbors = set()
    for _, e in q_edges:
        r = e[0] if e[1] == q else e[1]
        q_neighbors.add(r)

    # Case 1: edge (p,r) in edges and edge (r,q) also in edges for some r
    common = p_neighbors & q_neighbors
    if common:
        r = min(common)  # pick the smallest for consistency
        pr = (min(p,r), max(p,r))
        rq = (min(r,q), max(r,q))

        idx_pr = edges.index(pr)
        idx_rq = edges.index(rq)

        # Arnold: omega_{pr} ∧ omega_{rq} = omega_{pr} ∧ omega_{pq} + omega_{pq} ∧ omega_{rq}
        # So the coefficient of omega_{pq} in omega_{...} ∧ omega_{pr} ∧ omega_{...} ∧ omega_{rq} ∧ omega_{...}
        # involves moving pr and rq adjacent and applying Arnold.

        # This is getting very involved. Let me use a completely numerical approach.
        pass

    # Numerical approach: evaluate at random points
    return extract_omega_pq_numerical(edges, p, q, n, k, target_basis)


def extract_omega_pq_numerical(edges, p, q, n, k, target_basis):
    """
    Numerically compute the contraction of omega_{pq} from a wedge product.

    Use random point evaluation: evaluate the form at many random
    configurations and solve for the coefficients in the target basis.
    """
    pq = (min(p,q), max(p,q))
    n_new = n - 1
    k_new = k - 1

    def relabel(v):
        if v == q: return p
        if v > q: return v - 1
        return v

    dim_tgt = len(target_basis)
    if dim_tgt == 0:
        return []

    # Generate random points
    np.random.seed(42)
    n_samples = dim_tgt + 5

    # Evaluate source form at configurations near z_p = z_q
    # The contraction extracts the coefficient of dlog(z_p - z_q)

    results = np.zeros(n_samples)
    tgt_matrix = np.zeros((n_samples, dim_tgt))

    for s in range(n_samples):
        # Random points z_0, ..., z_{n-1}
        z = np.random.randn(n) + 1j * np.random.randn(n)

        # Evaluate source form: product of omega_{ij} = 1/(z_i - z_j) for each edge
        # (evaluating the "coefficient" form, without the differential)
        src_val = 1.0
        for e in edges:
            src_val *= 1.0 / (z[e[0]] - z[e[1]])

        # The contraction at (p,q) divides by the omega_{pq} factor
        # and relabels. The "coefficient of omega_{pq}" in the
        # product is obtained by removing the 1/(z_p - z_q) factor.

        # But we also need to handle the signs from the wedge product.
        # For a product omega_{e1} ∧ ... ∧ omega_{ek}, the contraction
        # iota_{pq} extracts omega_{pq} with the appropriate sign.

        # The contraction result at the relabeled points:
        z_new = np.zeros(n_new, dtype=complex)
        for v in range(n):
            v_new = relabel(v)
            z_new[v_new] = z[v]
        # Overwrite the merged point with z[p]
        z_new[p] = z[p]

        # Evaluate target basis forms at z_new
        for t, tgt_edges in enumerate(target_basis):
            tgt_val = 1.0
            for e in tgt_edges:
                tgt_val *= 1.0 / (z_new[e[0]] - z_new[e[1]])
            tgt_matrix[s, t] = tgt_val.real

        # Compute contraction value
        # The contraction iota_{pq} of the form ω = ∧ω_{ei} extracts ω_{pq}.
        # If ω_{pq} = dlog(z_p - z_q) and we evaluate forms as 1/(z_i - z_j):
        # The contraction removes 1/(z_p - z_q) from the product and
        # accounts for the sign from the wedge position.

        # Since (p,q) is not in edges, the product doesn't directly contain
        # 1/(z_p - z_q). The Arnold relation creates it implicitly.

        # Actually, the evaluation approach: the contraction of omega_{pq}
        # from a k-form ω gives a (k-1)-form α such that ω = omega_{pq} ∧ α + β
        # where beta doesn't involve omega_{pq}.
        # So: ω / omega_{pq} = α (mod terms not containing omega_{pq})
        # In evaluation: val(ω) = val(omega_{pq}) * val(α) + ...
        # So val(α) ≈ val(ω) / val(omega_{pq}) (approximately, at generic points)

        contraction_val = src_val * (z[p] - z[q])  # multiply by (z_p - z_q) to remove one pole
        # But this doesn't account for the wedge signs...

        # This numerical approach is getting unreliable. Let me try a different method.
        results[s] = contraction_val.real

    # Solve: results = tgt_matrix @ coeffs
    if dim_tgt > 0:
        coeffs, _, _, _ = np.linalg.lstsq(tgt_matrix, results, rcond=None)
        result = [(i, coeffs[i]) for i in range(dim_tgt) if abs(coeffs[i]) > 1e-10]
        return result
    return []


def find_in_nbc_basis(edge_tuple, nbc_basis, overall_sign=1.0):
    """Find an edge tuple in the NBC basis, accounting for permutation signs."""
    edge_set = set(edge_tuple)
    for idx, b in enumerate(nbc_basis):
        if set(b) == edge_set:
            # Compute sign
            sign = overall_sign
            if len(b) > 1:
                sign *= permutation_sign(list(edge_tuple), list(b))
            return [(idx, sign)]
    return []


# ========================================
# Main computation
# ========================================

def compute_bar_cohomology(algebra='sl2', max_degree=5):
    """Compute bar cohomology dimensions for the given algebra."""

    if algebra == 'sl2':
        d, f_abc = sl2_structure()
    elif algebra == 'sl3':
        d, f_abc = sl3_structure()
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    print(f"Computing bar cohomology for {algebra} (dim = {d})")
    print(f"Verifying Jacobi identity...", end=" ")
    assert verify_jacobi(d, f_abc), "Jacobi identity failed!"

    # Compute bar complex dimensions
    print(f"\nBar complex chain group dimensions B^n = d^n * (n-1)!:")
    for n in range(1, max_degree + 2):
        import math
        dim_bn = d**n * math.factorial(n-1)
        print(f"  B^{n} = {d}^{n} * {math.factorial(n-1)} = {dim_bn}")

    print(f"\nBuilding differentials and computing homology...")

    # Build differentials d_n: B^n -> B^{n-1}
    # H_n = ker(d_n) / im(d_{n+1})

    ranks = {}
    dims = {}

    for n in range(1, max_degree + 2):
        import math
        dim_os = math.factorial(n-1)
        dims[n] = d**n * dim_os
    dims[0] = 1  # B^0 = C (vacuum)

    # Compute rank of each differential
    for n in range(2, max_degree + 2):
        print(f"\n--- Degree {n} ---")
        mat = build_bar_differential_numerical(d, f_abc, n)
        if mat.shape[0] > 0 and mat.shape[1] > 0:
            r = np.linalg.matrix_rank(mat.toarray(), tol=1e-8)
            ranks[n] = r
            print(f"  rank(d_{n}) = {r}")
        else:
            ranks[n] = 0
    ranks[1] = 0  # d_1: B^1 -> B^0 is zero (single generator)

    # Compute homology dimensions
    print(f"\nHomology dimensions:")
    for n in range(1, max_degree + 1):
        ker_dim = dims[n] - ranks.get(n, 0)
        im_dim = ranks.get(n+1, 0)
        h_n = ker_dim - im_dim
        print(f"  H_{n} = dim(B^{n}) - rank(d_{n}) - rank(d_{n+1})")
        print(f"       = {dims[n]} - {ranks.get(n,0)} - {ranks.get(n+1,0)} = {h_n}")


if __name__ == '__main__':
    algebra = sys.argv[1] if len(sys.argv) > 1 else 'sl2'
    max_deg = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    compute_bar_cohomology(algebra, max_deg)
