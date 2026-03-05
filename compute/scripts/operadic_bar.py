#!/usr/bin/env python3
"""
Operadic bar complex computation for Lie algebras and W-algebras.

For a Lie algebra g of dim d, the bar complex is:
  B̄^n = g^{⊗n} ⊗ Ω^{n-1}(C_n(ℂ))
with differential d using the Lie bracket and OS form residues.

The bar cohomology H^n(B̄(g)) gives:
  - sl₂: Riordan numbers R(n+3)
  - Virasoro: Motzkin differences M(n+1)-M(n) (requires PBW extension)
  - W₃: sequence 2, 5, 16, 52, ? (the target)

Strategy:
1. Implement OS algebra and residue operations
2. Implement Lie algebra bar differential
3. Verify on sl₂ (should give Riordan numbers)
4. Extend to W₃ (including mode algebra)
"""
from fractions import Fraction as F
from itertools import product as iproduct
from functools import lru_cache
from math import gcd
from collections import defaultdict

# ============================================================
# OS ALGEBRA: Orlik-Solomon algebra of C_n(ℂ)
# ============================================================

def os_basis(n, degree):
    """
    Return a basis for Ω^degree(C_n(ℂ)) in the OS algebra.

    Convention: Ω^k is spanned by wedge products η_{i1,j1} ∧ ... ∧ η_{ik,jk}
    modulo Arnold relations. We use the "broken circuit" basis:

    For n points labeled 1,...,n, a basis of Ω^k consists of
    ordered sequences (i₁,j₁),...,(i_k,j_k) where:
    - Each (i_a, j_a) has i_a < j_a
    - The sequence forms a "no-broken-circuit" set

    Simpler: use the basis of "descending forests" with root n.
    A (k)-form basis element is a set of k edges {(a₁,b₁),...,(a_k,b_k)}
    in the complete graph K_n such that removing the largest edge from
    each cycle gives the set (no broken circuits).

    Even simpler for computation: at degree k = n-1 (top degree),
    basis has (n-1)! elements corresponding to orderings of {1,...,n-1}
    that specify the tree structure.

    We represent basis elements as tuples of pairs ((i1,j1),...,(ik,jk)).
    """
    if degree == 0:
        return [()]  # single element: the empty wedge product (scalar 1)

    if degree == n - 1:
        # Top degree: (n-1)! basis elements
        # Use increasing trees rooted at n
        # A basis: all permutations σ of [1,...,n-1], representing
        # η_{σ(1),σ(2)} ∧ η_{σ(2),σ(3)} ∧ ... ∧ η_{σ(n-2),σ(n-1)} ∧ η_{σ(n-1),n}
        # No, that's not quite right.
        #
        # Standard basis: for each permutation σ of [n-1],
        # the form ω_σ = η_{σ(1),n} ∧ η_{σ(2),n} ∧ ... ∧ η_{σ(n-1),n}
        # But these are NOT all independent (Arnold relations).
        #
        # Actually, the standard NBC basis for the top degree of C_n(ℂ):
        # Fix ordering 1 < 2 < ... < n.
        # Broken circuit: remove largest edge from each cycle.
        # NBC = no broken circuit.
        #
        # For top degree (n-1)-forms, the NBC basis has size (n-1)!.
        # These can be represented as labeled trees on [n].
        #
        # Simplest construction: use the basis
        # {η_{1,σ(1)} ∧ η_{2,σ(2)} ∧ ... ∧ η_{n-1,σ(n-1)} : σ a function ...}
        # No, this gets complicated.
        #
        # Let me use a different, explicit basis.
        # For n points, Ω^{n-1}(C_n) has basis indexed by
        # permutations of [n] up to cyclic order, or equivalently
        # by labeled rooted trees on [n].
        pass

    # General approach: enumerate NBC basis elements
    # For small n, just enumerate all possible wedge products and
    # reduce modulo Arnold relations.

    # For n ≤ 6 and degree ≤ 5, we can use explicit enumeration.
    edges = [(i, j) for i in range(1, n+1) for j in range(i+1, n+1)]

    # Generate all k-subsets of edges
    from itertools import combinations
    basis = []
    for subset in combinations(edges, degree):
        # Check NBC condition: no broken circuit
        if is_nbc(subset, n):
            basis.append(subset)

    return basis


def is_nbc(edge_set, n):
    """
    Check if an edge set is NBC (No Broken Circuit) in K_n.

    A broken circuit is obtained by removing the largest edge from a cycle.
    An edge set is NBC if it contains no broken circuit.

    Equivalently: the edge set forms a forest (no cycles) when
    restricted to the condition that adding any removed edge would
    create a cycle whose maximum edge is the one removed.

    Simpler criterion: edge_set is NBC iff it forms a FOREST
    (no cycles) in K_n.

    Wait, that's not right. NBC is stronger than being a forest.
    An NBC set is a forest such that for every pair of vertices
    (i,j) not in the forest, the path from i to j in the forest
    uses only edges SMALLER than (i,j).

    Actually, the standard result: in the matroid of K_n with edges
    ordered lexicographically, the NBC bases are exactly the spanning
    forests that are "increasing" from each leaf to the root.

    For simplicity, let me use a direct cycle-detection approach.
    """
    # An edge set in K_n is NBC iff:
    # 1. It is a forest (acyclic)
    # 2. For any edge (a,b) not in the set, the path from a to b
    #    in the forest uses only edges < (a,b) in lex order.

    # Condition 1: check acyclicity using union-find
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False  # cycle!
        parent[rx] = ry
        return True

    for (i, j) in edge_set:
        if not union(i, j):
            return False  # has cycle

    # Condition 2: for each non-edge (a,b) with a<b,
    # check that the path from a to b in the forest
    # uses only edges smaller than (a,b).
    #
    # This is equivalent to: the edge set contains no "broken circuit".
    # A broken circuit for edge (a,b): a subset S ⊂ edge_set such that
    # S ∪ {(a,b)} forms a cycle and (a,b) is the LARGEST edge in the cycle.
    #
    # So: for each pair of vertices connected in the forest,
    # the maximum edge on their path should be LESS than any
    # non-forest edge that would connect the same pair.
    #
    # Equivalently: for every edge (a,b) NOT in edge_set,
    # if a,b are connected in the forest, then the max edge
    # on the a-b path is < (a,b).
    #
    # Build adjacency list for the forest
    adj = defaultdict(list)
    for (i, j) in edge_set:
        adj[i].append((j, (i, j)))
        adj[j].append((i, (i, j)))

    # Find all vertices in the forest
    vertices = set()
    for (i, j) in edge_set:
        vertices.add(i)
        vertices.add(j)

    # For each non-edge (a,b) with a,b connected, find max path edge
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (a, b) in edge_set:
                continue
            if find(a) != find(b):
                continue  # not connected, no constraint

            # Find path from a to b in forest, get max edge
            max_edge = find_max_path_edge(adj, a, b, vertices)
            if max_edge is not None and (a, b) > max_edge:
                return False  # broken circuit: (a,b) is largest in cycle

    return True


def find_max_path_edge(adj, start, end, vertices):
    """Find the maximum edge on the unique path from start to end in a forest."""
    # BFS/DFS
    visited = set()
    stack = [(start, None)]  # (current vertex, max edge so far)
    parent_map = {}

    while stack:
        v, _ = stack.pop()
        if v in visited:
            continue
        visited.add(v)

        if v == end:
            # Trace back path and find max edge
            path_edges = []
            cur = end
            while cur != start:
                prev, edge = parent_map[cur]
                path_edges.append(edge)
                cur = prev
            return max(path_edges) if path_edges else None

        for (w, edge) in adj[v]:
            if w not in visited:
                parent_map[w] = (v, edge)
                stack.append((w, None))

    return None  # not connected


def os_residue(form, collision_pair, n):
    """
    Compute the residue of an OS form at boundary divisor D_{ij}.

    form: tuple of edge pairs ((i1,j1), ..., (ik,jk))
    collision_pair: (i, j) with i < j — the two points colliding
    n: total number of points

    Returns: list of (coefficient, new_form) pairs in Ω^{k-1}(C_{n-1})
    where the new labeling merges vertex j into vertex i.
    """
    i, j = collision_pair
    k = len(form)

    if k == 0:
        return []  # residue of a 0-form is 0

    results = []

    # The residue at D_{ij} picks out the component of the form
    # that has a simple pole at z_i = z_j.
    # In the OS algebra: Res_{D_{ij}}(η_{ab} ∧ ω') =
    #   +ω'|_{z_j→z_i} if (a,b) = (i,j)
    #   0 if neither a,b is i or j  (no pole at D_{ij})
    #   more complex if a or b equals i or j but not both

    # The exact residue formula in OS algebra:
    # Res_{D_{ij}} extracts the "log pole" at D_{ij}.
    # η_{ij} has a simple log pole at D_{ij}.
    # η_{ik} for k≠j: expand at D_{ij} as η_{ik} = η_{jk} + regular
    #   (since z_i = z_j + ε, log(z_i-z_k) = log(z_j-z_k+ε) = log(z_j-z_k) + ε/...)
    #   Actually: d log(z_i - z_k) as z_i → z_j becomes d log(z_j - z_k) (regular).
    #   So η_{ik} → η_{jk} at D_{ij} (no pole).
    # η_{jk}: already expressed in terms of the remaining variables, stays as is.

    # So: the only source of a pole is η_{ij} itself.
    # Res_{D_{ij}}(η_{ij} ∧ ω') = ω'|_{relabel i→j→merged}

    # Find if η_{ij} (or η_{ji}) appears in the form
    # Since we use i<j, look for (i,j) in form

    for pos in range(k):
        edge = form[pos]
        if edge == (i, j):
            # Remove this factor, relabel remaining
            sign = (-1)**pos  # sign from pulling η_{ij} to front
            remaining = list(form[:pos]) + list(form[pos+1:])

            # Relabel: merge j into i, shift indices > j down by 1
            new_form = []
            valid = True
            for (a, b) in remaining:
                # Replace j by i
                a2 = i if a == j else a
                b2 = i if b == j else b
                if a2 == b2:
                    valid = False
                    break
                # Shift down indices > j
                if a2 > j: a2 -= 1
                if b2 > j: b2 -= 1
                # Also shift i if i > j: but i < j always
                # Normalize: ensure a2 < b2
                if a2 > b2:
                    a2, b2 = b2, a2
                    sign *= -1  # η_{b,a} = -η_{a,b}...
                    # Actually η_{ab} = d log(z_a - z_b), and
                    # η_{ba} = d log(z_b - z_a) = d log(-(z_a-z_b)) = d log(z_a-z_b) = η_{ab}
                    # So η_{ab} = η_{ba}! No sign change.
                    sign *= -1  # undo the sign flip
                new_form.append((a2, b2))

            if valid:
                results.append((F(sign), tuple(new_form)))

    # Also need to account for forms like η_{ik} that, after Arnold
    # rewriting, contain η_{ij}. But in the NBC basis, this doesn't
    # happen directly. The Arnold relations are:
    # η_{ab} ∧ η_{bc} + η_{bc} ∧ η_{ca} + η_{ca} ∧ η_{ab} = 0
    # for any triple a,b,c.

    # For the NBC basis, the forms don't contain η_{ij} unless
    # (i,j) is explicitly one of the edges. But there could be
    # implicit contributions from edges (i,k) or (j,k) that,
    # when expanded near D_{ij}, contribute to the residue.

    # The correct formula: for any form ω, the residue at D_{ij} is
    # obtained by writing ω = η_{ij} ∧ ω₁ + ω₂ where ω₂ has no
    # η_{ij} factor, and then Res_{D_{ij}}(ω) = ω₁|_{z_j→z_i}.

    # In the NBC basis, this decomposition may require Arnold relations.
    # For the current implementation, we only detect explicit η_{ij} factors.
    # This should be correct for the NBC basis if (i,j) appears explicitly.

    return results


# ============================================================
# LIE ALGEBRA BAR COMPLEX
# ============================================================

class LieAlgebra:
    """A finite-dimensional Lie algebra."""

    def __init__(self, dim, bracket_table, basis_names=None):
        """
        dim: dimension
        bracket_table: dict {(a,b): [(coeff, c), ...]} for [e_a, e_b] = Σ coeff * e_c
        basis_names: optional list of names
        """
        self.dim = dim
        self.bracket = bracket_table
        self.names = basis_names or [f"e_{i}" for i in range(dim)]

    def lie_bracket(self, a, b):
        """Compute [e_a, e_b] as list of (coefficient, index) pairs."""
        if (a, b) in self.bracket:
            return self.bracket[(a, b)]
        elif (b, a) in self.bracket:
            return [(-c, i) for c, i in self.bracket[(b, a)]]
        else:
            return []


def make_sl2():
    """Create sl₂ = {e, f, h} with standard brackets."""
    # Basis: 0=e, 1=f, 2=h
    # [e,f] = h, [h,e] = 2e, [h,f] = -2f
    bracket = {
        (0, 1): [(F(1), 2)],    # [e,f] = h
        (2, 0): [(F(2), 0)],    # [h,e] = 2e
        (2, 1): [(F(-2), 1)],   # [h,f] = -2f
    }
    return LieAlgebra(3, bracket, ['e', 'f', 'h'])


def bar_complex_dim(g, n):
    """Dimension of B̄^n = g^⊗n ⊗ Ω^{n-1}(C_n)."""
    os_dim = 1
    for k in range(1, n):
        os_dim *= k  # (n-1)!
    return g.dim**n * os_dim


def bar_differential_matrix(g, n, os_b_n=None, os_b_nm1=None):
    """
    Build the matrix of d: B̄^n → B̄^{n-1}.

    B̄^n has basis: (a₁,...,aₙ) ⊗ ω where aᵢ ∈ {0,...,dim-1} and ω ∈ OS basis.
    B̄^{n-1} has basis: (b₁,...,b_{n-1}) ⊗ ω' where ω' ∈ OS basis of C_{n-1}.

    The differential:
    d([a₁|...|aₙ] ⊗ ω) = Σ_{i<j} ±[a₁|...|[aᵢ,aⱼ]|...|âⱼ|...|aₙ] ⊗ Res_{D_{ij}}(ω)

    Returns matrix M where M[row][col] = coefficient.
    """
    d = g.dim

    # Get OS bases
    if os_b_n is None:
        os_b_n = os_basis(n, n - 1)
    if os_b_nm1 is None:
        os_b_nm1 = os_basis(n - 1, n - 2) if n >= 2 else [()]

    # Index the basis elements
    # B̄^n basis: (tensor_indices, form_index)
    # tensor_indices: tuple of length n, each in {0,...,d-1}
    # form_index: index into os_b_n

    source_tensors = list(iproduct(range(d), repeat=n))
    target_tensors = list(iproduct(range(d), repeat=n-1)) if n >= 2 else [()]

    source_size = len(source_tensors) * len(os_b_n)
    target_size = len(target_tensors) * len(os_b_nm1)

    # Build index maps
    source_tensor_idx = {t: i for i, t in enumerate(source_tensors)}
    target_tensor_idx = {t: i for i, t in enumerate(target_tensors)}
    target_form_idx = {f: i for i, f in enumerate(os_b_nm1)}

    # Build matrix (sparse)
    matrix = defaultdict(F)

    for s_tidx, s_tensor in enumerate(source_tensors):
        for s_fidx, s_form in enumerate(os_b_n):
            s_idx = s_tidx * len(os_b_n) + s_fidx

            # For each collision pair (i,j) with i < j (1-indexed in the OS algebra)
            for i in range(n):
                for j in range(i + 1, n):
                    # Lie bracket [a_i, a_j]
                    bracket_results = g.lie_bracket(s_tensor[i], s_tensor[j])
                    if not bracket_results:
                        continue

                    # OS form residue at D_{i+1, j+1} (OS uses 1-indexed)
                    form_residues = os_residue(s_form, (i + 1, j + 1), n)
                    if not form_residues:
                        continue

                    # Sign: (-1)^(position_of_j_relative_to_i)
                    # For the bar complex, removing element j from position j
                    # and replacing a_i by [a_i, a_j]:
                    # Sign = (-1)^(j-i-1) from moving a_j past the intervening elements
                    # (This is a simplification; the exact sign depends on convention)
                    koszul_sign = (-1)**(j - i - 1)

                    for br_coeff, br_idx in bracket_results:
                        # New tensor: replace a_i by br_idx, remove a_j
                        new_tensor = list(s_tensor)
                        new_tensor[i] = br_idx
                        del new_tensor[j]
                        new_tensor = tuple(new_tensor)

                        if new_tensor not in target_tensor_idx:
                            continue
                        t_tidx = target_tensor_idx[new_tensor]

                        for form_coeff, new_form in form_residues:
                            if new_form not in target_form_idx:
                                # Need to express in NBC basis
                                # For now, skip (this is a limitation)
                                continue
                            t_fidx = target_form_idx[new_form]

                            t_idx = t_tidx * len(os_b_nm1) + t_fidx

                            total_coeff = F(koszul_sign) * br_coeff * form_coeff
                            matrix[(t_idx, s_idx)] += total_coeff

    # Convert to dense matrix
    M = [[F(0)] * source_size for _ in range(target_size)]
    for (r, c), v in matrix.items():
        M[r][c] += v

    return M, source_size, target_size


def matrix_rank(M, nrows, ncols):
    """Compute rank of a matrix over Q (using Fraction)."""
    A = [row[:] for row in M]
    rank = 0
    for col in range(ncols):
        # Find pivot
        piv = None
        for row in range(rank, nrows):
            if A[row][col] != F(0):
                piv = row
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        pv = A[rank][col]
        for row in range(nrows):
            if row != rank and A[row][col] != F(0):
                fac = A[row][col] / pv
                for c in range(ncols):
                    A[row][c] -= fac * A[rank][c]
        rank += 1
    return rank


# ============================================================
# MAIN: Verify on sl₂
# ============================================================

if __name__ == "__main__":
    import sys

    g = make_sl2()
    print("sl₂ bar complex computation")
    print("=" * 60)
    print(f"Lie algebra: dim = {g.dim}, generators: {g.names}")

    riordan = [1, 0, 1, 1, 3, 6, 15, 36, 91, 232]

    # Compute at each bar degree
    prev_rank_d = 0  # rank of d_{n+1→n}

    for n in range(1, 6):
        print(f"\nBar degree n = {n}:")

        os_bn = os_basis(n, n - 1)
        print(f"  OS basis dim Ω^{n-1}(C_{n}): {len(os_bn)}")
        print(f"  Expected: {max(1, 1) if n==1 else 'factorial(n-1)='}{1 if n==1 else __import__('math').factorial(n-1)}")

        dim_bn = g.dim**n * len(os_bn)
        print(f"  dim B̄^{n} = {g.dim}^{n} × {len(os_bn)} = {dim_bn}")

        if n == 1:
            # H^1 = B̄^1 (no differential from B̄^2 reaches B̄^1...
            # actually d: B̄^2 → B̄^1 exists)
            # We need to compute d: B̄^2 → B̄^1
            os_b2 = os_basis(2, 1)
            M, src, tgt = bar_differential_matrix(g, 2, os_b2, os_bn)
            rank_d2 = matrix_rank(M, tgt, src)
            print(f"  d: B̄^2 → B̄^1: matrix {tgt}×{src}, rank = {rank_d2}")

            # H^1 = dim B̄^1 - rank(d: B̄^2 → B̄^1) - rank(d: B̄^1 → B̄^0)
            # d: B̄^1 → B̄^0 is the augmentation, which is 0 for elements of g (augmentation ideal)
            h1 = dim_bn - rank_d2
            print(f"  H^1 = {dim_bn} - {rank_d2} = {h1}")
            print(f"  Expected R({n+3}) = {riordan[n+3]}")
            prev_rank_d = rank_d2
        else:
            # Compute d: B̄^{n+1} → B̄^n and d: B̄^n → B̄^{n-1}
            # H^n = ker(d: B̄^n → B̄^{n-1}) / im(d: B̄^{n+1} → B̄^n)
            # = (dim B̄^n - rank(d_n)) - rank(d_{n+1})
            # where rank(d_n) = rank of d: B̄^n → B̄^{n-1}
            # and rank(d_{n+1}) = rank of d: B̄^{n+1} → B̄^n

            # We already have rank(d_n) from previous step: prev_rank_d
            # Now compute d: B̄^{n+1} → B̄^n
            if n < 5:  # limit computation size
                os_bnp1 = os_basis(n + 1, n)
                dim_bnp1 = g.dim**(n+1) * len(os_bnp1)
                print(f"  dim B̄^{n+1} = {dim_bnp1}")

                if dim_bnp1 <= 5000 and dim_bn <= 5000:
                    M_next, src_next, tgt_next = bar_differential_matrix(g, n + 1, os_bnp1, os_bn)
                    rank_dnp1 = matrix_rank(M_next, tgt_next, src_next)
                    print(f"  d: B̄^{n+1} → B̄^{n}: rank = {rank_dnp1}")

                    # Also compute d: B̄^n → B̄^{n-1}
                    os_bnm1 = os_basis(n - 1, n - 2)
                    M_cur, src_cur, tgt_cur = bar_differential_matrix(g, n, os_bn, os_bnm1)
                    rank_dn = matrix_rank(M_cur, tgt_cur, src_cur)
                    print(f"  d: B̄^{n} → B̄^{n-1}: rank = {rank_dn}")

                    hn = dim_bn - rank_dn - rank_dnp1
                    print(f"  H^{n} = {dim_bn} - {rank_dn} - {rank_dnp1} = {hn}")
                    print(f"  Expected R({n+3}) = {riordan[n+3]}")
                    prev_rank_d = rank_dnp1
                else:
                    print(f"  Skipping (matrix too large: {dim_bnp1} × {dim_bn})")
            else:
                print(f"  Skipping degree {n+1}")
