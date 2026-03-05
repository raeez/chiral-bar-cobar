#!/usr/bin/env python3
"""
Compute bar cohomology dimensions for chiral algebras.

The genus-0 chiral bar complex of V^k(g) (affine Kac-Moody at generic level) is:
  B^n = g^{tensor n} x OS_{n-1}(n)
where OS_{n-1}(n) = H^{n-1}(Conf_n(C)) has dimension (n-1)!.

The differential d: B^{n+1} -> B^n contracts a pair (i,j) by the Lie bracket
[a_i, a_j] = f^{a_i a_j}_c e_c, and takes the Poincare residue on the OS form.

At genus 0, the central extension (double pole) does NOT contribute because
the residue of dε/ε^3 vanishes (only simple poles give nonzero residues).

The bar cohomology H^n = ker(d_n)/im(d_{n+1}) gives the dimensions of the
Koszul dual algebra (A^!)_n.
"""

import numpy as np
from itertools import combinations, permutations
from collections import defaultdict
import sys
from fractions import Fraction


# =============================================================================
# 1. Lie algebra structure constants
# =============================================================================

def sl_N_structure_constants(N):
    """
    Compute structure constants for sl_N in the standard basis.

    Basis ordering for sl_N (dim = N^2 - 1):
      - E_{ij} for i != j (off-diagonal matrix units), ordered lexicographically
      - H_k = E_{kk} - E_{k+1,k+1} for k = 1,...,N-1 (traceless diagonal)

    Returns: (dim, f) where f[a][b] = dict mapping c -> f^{ab}_c
    """
    dim = N * N - 1

    # Build basis: list of (type, indices)
    # type 'E' for E_{ij}, type 'H' for H_k
    basis = []
    basis_index = {}

    # Off-diagonal E_{ij}
    for i in range(N):
        for j in range(N):
            if i != j:
                idx = len(basis)
                basis.append(('E', i, j))
                basis_index[('E', i, j)] = idx

    # Diagonal H_k = E_{kk} - E_{k+1,k+1}
    for k in range(N - 1):
        idx = len(basis)
        basis.append(('H', k))
        basis_index[('H', k)] = idx

    assert len(basis) == dim

    # Compute [basis[a], basis[b]] as a linear combination of basis elements
    # Using matrix commutator [E_{ij}, E_{kl}] = delta_{jk} E_{il} - delta_{li} E_{kj}
    # and [H_k, E_{ij}] etc.

    def matrix_unit(typ):
        """Return the N x N matrix for a basis element."""
        M = np.zeros((N, N))
        if typ[0] == 'E':
            _, i, j = typ
            M[i, j] = 1.0
        else:  # 'H'
            _, k = typ
            M[k, k] = 1.0
            M[k+1, k+1] = -1.0
        return M

    def decompose(M):
        """Decompose an N x N traceless matrix into basis coefficients."""
        coeffs = {}
        # Off-diagonal
        for i in range(N):
            for j in range(N):
                if i != j and abs(M[i, j]) > 1e-12:
                    idx = basis_index[('E', i, j)]
                    coeffs[idx] = M[i, j]

        # Diagonal: decompose traceless diagonal part into H_k basis
        diag = np.diag(M).copy()
        # H_k has diagonal (0,...,0,1,-1,0,...,0) at positions k, k+1
        # Decompose: solve for c_k where sum c_k H_k = diag
        # H_1 = (1,-1,0,...), H_2 = (0,1,-1,0,...), etc.
        # c_k = sum_{i=0}^{k} diag[i]  (cumulative sum trick)
        for k in range(N - 1):
            c_k = sum(diag[:k+1])
            if abs(c_k) > 1e-12:
                idx = basis_index[('H', k)]
                coeffs[idx] = c_k

        return coeffs

    # Build structure constant tensor
    # f[a][b] = {c: f^{ab}_c}
    f = [defaultdict(float) for _ in range(dim)]

    matrices = [matrix_unit(b) for b in basis]

    for a in range(dim):
        for b in range(dim):
            comm = matrices[a] @ matrices[b] - matrices[b] @ matrices[a]
            coeffs = decompose(comm)
            for c, val in coeffs.items():
                if abs(val) > 1e-12:
                    f[a][c] = f[a].get(c, defaultdict(float))
                    if not isinstance(f[a], defaultdict):
                        f[a] = defaultdict(float, f[a])

    # Rebuild as a cleaner structure: bracket[a][b] -> list of (c, coeff)
    bracket = [[[] for _ in range(dim)] for _ in range(dim)]
    for a in range(dim):
        Ma = matrices[a]
        for b in range(dim):
            Mb = matrices[b]
            comm = Ma @ Mb - Mb @ Ma
            coeffs = decompose(comm)
            bracket[a][b] = [(c, v) for c, v in coeffs.items()]

    return dim, bracket


# =============================================================================
# 2. Orlik-Solomon algebra: basis and residue maps
# =============================================================================

class OSAlgebra:
    """
    Orlik-Solomon algebra for the braid arrangement of n points.

    OS_k(n) = degree-k part of H*(Conf_n(C)).
    dim OS_k(n) = |s(n, n-k)| (unsigned Stirling numbers of the first kind).
    In particular, dim OS_{n-1}(n) = (n-1)!.

    We use the "nbc" (no-broken-circuit) basis.
    Edges are pairs (i,j) with 0 <= i < j < n, ordered lexicographically.
    """

    def __init__(self, n):
        self.n = n
        self.edges = [(i, j) for i in range(n) for j in range(i+1, n)]
        self.edge_index = {e: i for i, e in enumerate(self.edges)}
        self.num_edges = len(self.edges)

        # Compute nbc basis for each degree
        self._nbc_bases = {}
        self._compute_nbc_bases()

        # Cache residue matrices
        self._residue_cache = {}

    def _compute_nbc_bases(self):
        """Compute nbc bases for all degrees."""
        # Circuits: minimal dependent sets in the graphic matroid of K_n
        # For K_n, circuits = triangles (3-cycles)
        # A broken circuit = circuit with its largest edge removed

        broken_circuits = set()
        for i in range(self.n):
            for j in range(i+1, self.n):
                for k in range(j+1, self.n):
                    # Triangle on vertices i, j, k
                    # Edges: (i,j), (i,k), (j,k) in lex order
                    # Largest edge = (j,k) (last in lex order)
                    # Broken circuit = {(i,j), (i,k)}
                    broken_circuits.add(frozenset([(i,j), (i,k)]))

        self.broken_circuits = broken_circuits

        for degree in range(self.n):
            # Enumerate all degree-subsets of edges that form independent sets
            # (forests) and contain no broken circuit
            nbc = []
            for subset in combinations(self.edges, degree):
                fset = frozenset(subset)
                # Check no broken circuit is a subset
                is_nbc = True
                for bc in broken_circuits:
                    if bc <= fset:
                        is_nbc = False
                        break
                if is_nbc:
                    # Check it's a forest (no cycles)
                    if self._is_forest(subset):
                        nbc.append(subset)

            self._nbc_bases[degree] = nbc

    def _is_forest(self, edges):
        """Check if a set of edges forms a forest (acyclic graph)."""
        if len(edges) == 0:
            return True
        # Union-find
        parent = list(range(self.n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # cycle
            parent[px] = py
            return True

        for (i, j) in edges:
            if not union(i, j):
                return False
        return True

    def basis(self, degree):
        """Return nbc basis elements for OS_degree(n)."""
        return self._nbc_bases.get(degree, [])

    def dim(self, degree):
        """Dimension of OS_degree(n)."""
        return len(self.basis(degree))

    def _reduce_to_nbc(self, degree, element_dict):
        """
        Reduce an element (given as dict: frozenset(edges) -> coeff)
        to the nbc basis. Returns list of coefficients in nbc basis order.

        Uses the Arnold relation: if a monomial contains a broken circuit
        {(i,j), (i,k)} (with j < k), replace using:
        ω_{ij} ∧ ω_{ik} = ω_{ij} ∧ ω_{jk} - ω_{ik} ∧ ω_{jk}
        (from the Arnold relation ω_{ij}∧ω_{jk} = ω_{ij}∧ω_{ik} + ω_{ik}∧ω_{jk})
        """
        nbc_basis = self.basis(degree)
        nbc_set = {frozenset(b): idx for idx, b in enumerate(nbc_basis)}

        result = np.zeros(len(nbc_basis))

        # Process each monomial
        worklist = list(element_dict.items())

        max_iterations = 10000
        iteration = 0

        while worklist and iteration < max_iterations:
            iteration += 1
            edges_fs, coeff = worklist.pop()

            if abs(coeff) < 1e-14:
                continue

            # Check if it's already in nbc basis
            if edges_fs in nbc_set:
                result[nbc_set[edges_fs]] += coeff
                continue

            # Find a broken circuit contained in this monomial
            found = False
            edges_list = sorted(edges_fs)
            for bc in self.broken_circuits:
                if bc <= edges_fs:
                    # bc = {(i,j), (i,k)} with j < k
                    bc_list = sorted(bc)
                    e1 = bc_list[0]  # (i, j)
                    e2 = bc_list[1]  # (i, k)
                    i_val = e1[0]
                    j_val = e1[1]
                    k_val = e2[1]

                    # The Arnold relation for the triple (i_val, j_val, k_val):
                    # ω_{i,j} ∧ ω_{i,k} = ω_{i,j} ∧ ω_{j,k} - ω_{i,k} ∧ ω_{j,k}
                    # where (j,k) is the largest edge (which was removed to form bc)
                    e_new = (min(j_val, k_val), max(j_val, k_val))  # (j,k)

                    # Remove e1 and e2 from the monomial, compute the remaining edges
                    remaining = edges_fs - bc

                    if e_new in remaining:
                        # The replacement edge is already present -> this monomial is zero
                        # (ω ∧ ω = 0)
                        found = True
                        break

                    # Determine signs from reordering
                    # We need to figure out the sign when replacing
                    # {e1, e2, ...rest} -> {e1, e_new, ...rest} - {e2, e_new, ...rest}

                    # Position of e1 and e2 in the sorted monomial
                    edges_sorted = sorted(edges_fs)
                    pos_e1 = edges_sorted.index(e1)
                    pos_e2 = edges_sorted.index(e2)

                    # Term 1: replace e2 with e_new -> {e1, e_new, ...rest}
                    new_edges_1 = (edges_fs - {e2}) | {e_new}
                    # Sign: moving e_new to where e2 was
                    new_sorted_1 = sorted(new_edges_1)
                    sign1 = self._permutation_sign(edges_sorted, e2, e_new, new_sorted_1)

                    # Term 2: replace e1 with e_new -> {e2, e_new, ...rest}  (with minus sign)
                    new_edges_2 = (edges_fs - {e1}) | {e_new}
                    new_sorted_2 = sorted(new_edges_2)
                    sign2 = self._permutation_sign(edges_sorted, e1, e_new, new_sorted_2)

                    worklist.append((frozenset(new_edges_1), coeff * sign1))
                    worklist.append((frozenset(new_edges_2), -coeff * sign2))

                    found = True
                    break

            if not found:
                # This shouldn't happen if our Arnold relations are complete
                # Check if the edges form a valid independent set
                edges_list = sorted(edges_fs)
                if self._is_forest(edges_list):
                    # It's a forest but not in nbc basis - shouldn't happen
                    print(f"WARNING: forest {edges_list} not in nbc basis!")
                    return None
                else:
                    # It's a cycle - should be zero
                    pass

        if iteration >= max_iterations:
            print("WARNING: exceeded max iterations in reduction")

        return result

    def _permutation_sign(self, old_sorted, old_edge, new_edge, new_sorted):
        """
        Compute the sign of replacing old_edge with new_edge in a sorted
        exterior algebra monomial.
        """
        # Remove old_edge from old_sorted, insert new_edge, count transpositions
        temp = [e for e in old_sorted if e != old_edge]
        # Insert new_edge into temp at the right position
        pos = 0
        while pos < len(temp) and temp[pos] < new_edge:
            pos += 1

        # old_edge was at position old_pos in old_sorted
        old_pos = old_sorted.index(old_edge)

        # After removing old_edge, the remaining edges shift
        # new_edge goes to position pos in the list temp
        # The sign is (-1)^(old_pos + pos) for remove-then-insert
        # Actually: removing from position old_pos costs (-1)^(old_pos)
        # (moving to front), inserting at position pos costs (-1)^pos
        # But we want to compare to the canonical sorted order...

        # Simpler: just compare the permutation between old_sorted and new_sorted
        # with the replacement
        # The sign is (-1)^(number of transpositions to go from one to the other)

        # Actually, the sign is determined by: in the original monomial
        # ω_{e1} ∧ ... ∧ ω_{old_edge} ∧ ... ∧ ω_{en}
        # we replace ω_{old_edge} with ω_{new_edge} (at the same position),
        # then reorder to canonical sorted order.

        # Step 1: position of old_edge in old_sorted
        temp_list = list(old_sorted)
        temp_list[old_pos] = new_edge
        # temp_list is now the new monomial in the wrong order
        # Sort it and count parity
        sign = 1
        # Bubble sort to count transpositions
        arr = list(temp_list)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    sign *= -1

        return sign

    def residue_matrix(self, pair, degree):
        """
        Compute the residue matrix Res_{D_{pair}}: OS_degree(n) -> OS_{degree-1}(n-1).

        pair = (i, j) with i < j.

        Returns a matrix of shape (dim OS_{degree-1}(n-1), dim OS_degree(n)).
        """
        cache_key = (pair, degree)
        if cache_key in self._residue_cache:
            return self._residue_cache[cache_key]

        i, j = pair
        n = self.n

        # Target: OS_{degree-1} for (n-1) points
        # After merging i and j, the points are relabeled
        target_os = OSAlgebra(n - 1)
        target_basis = target_os.basis(degree - 1)
        target_dim = len(target_basis)

        source_basis = self.basis(degree)
        source_dim = len(source_basis)

        if target_dim == 0 or source_dim == 0:
            mat = np.zeros((target_dim, source_dim))
            self._residue_cache[cache_key] = mat
            return mat

        # Relabeling map: after merging points i and j (j disappears),
        # point i stays, and all points > j shift down by 1.
        def relabel(v):
            """Relabel vertex v after merging i,j (j disappears)."""
            if v == j:
                return i  # j merges into i
            elif v > j:
                return v - 1
            else:
                return v

        # For the merged points, i < j, so relabel(j) = i (smaller index)
        # and relabel maps to {0, ..., n-2}
        # Need to also handle the case where relabel gives indices that
        # need re-sorting for edge representation (a, b) with a < b.

        def relabel_edge(e):
            """Relabel an edge after merging."""
            a, b = e
            ra, rb = relabel(a), relabel(b)
            if ra == rb:
                return None  # edge collapsed (was connecting i and j)
            return (min(ra, rb), max(ra, rb))

        mat = np.zeros((target_dim, source_dim))

        for src_idx, src_edges in enumerate(source_basis):
            # src_edges is a tuple of edges in OS_degree(n)
            # Check if the edge (i,j) = pair appears in src_edges
            # The residue extracts the ω_{ij} factor

            e_pair = pair
            if e_pair not in src_edges:
                # No pole at D_{ij} -> residue is 0
                continue

            # Remove the edge (i,j) from the monomial
            remaining = [e for e in src_edges if e != e_pair]

            # Sign: moving ω_{ij} to the front of the wedge product
            pos = list(src_edges).index(e_pair)
            sign = (-1) ** pos

            # Relabel the remaining edges
            relabeled = []
            valid = True
            for e in remaining:
                re = relabel_edge(e)
                if re is None:
                    valid = False
                    break
                relabeled.append(re)

            if not valid:
                continue

            # Now reduce the relabeled monomial to the target nbc basis
            # First, sort the relabeled edges and track the sign
            sorted_relabeled = sorted(relabeled)
            # Compute sign of sorting
            sort_sign = 1
            temp = list(relabeled)
            for ii in range(len(temp)):
                for jj in range(ii+1, len(temp)):
                    if temp[ii] > temp[jj]:
                        temp[ii], temp[jj] = temp[jj], temp[ii]
                        sort_sign *= -1

            total_sign = sign * sort_sign

            # Reduce to nbc basis in target OS algebra
            element = {frozenset(sorted_relabeled): total_sign}
            coeffs = target_os._reduce_to_nbc(degree - 1, element)

            if coeffs is not None:
                mat[:, src_idx] = coeffs

        self._residue_cache[cache_key] = mat
        return mat


# =============================================================================
# 3. Bar differential construction
# =============================================================================

def bar_differential_matrix(g_dim, bracket, n, verbose=False):
    """
    Construct the matrix for d: B^{n+1} -> B^n.

    B^n = g^{tensor n} x OS_{n-1}(n), dim = g_dim^n * (n-1)!
    B^{n+1} = g^{tensor (n+1)} x OS_n(n+1), dim = g_dim^{n+1} * n!

    The differential contracts pair (i,j) by the Lie bracket and
    takes the Poincare residue on the OS form.

    Returns: matrix of shape (dim B^n, dim B^{n+1})
    """
    os_source = OSAlgebra(n + 1)
    os_target = OSAlgebra(n)

    source_os_dim = os_source.dim(n)  # = n!
    target_os_dim = os_target.dim(n - 1)  # = (n-1)!

    source_dim = g_dim ** (n + 1) * source_os_dim
    target_dim = g_dim ** n * target_os_dim

    if verbose:
        print(f"  d_{n+1}: B^{n+1} ({source_dim}) -> B^{n} ({target_dim})")

    # Use sparse matrix
    from scipy.sparse import lil_matrix
    mat = lil_matrix((target_dim, source_dim), dtype=np.float64)

    # Index conventions:
    # Source element (a_0, a_1, ..., a_n, omega_idx) -> flat index
    # Target element (b_0, b_1, ..., b_{n-1}, omega_idx) -> flat index

    def source_index(algebra_indices, os_idx):
        """Flat index for a source element."""
        idx = 0
        for k, a in enumerate(algebra_indices):
            idx = idx * g_dim + a
        return idx * source_os_dim + os_idx

    def target_index(algebra_indices, os_idx):
        """Flat index for a target element."""
        idx = 0
        for k, a in enumerate(algebra_indices):
            idx = idx * g_dim + a
        return idx * target_os_dim + os_idx

    # For each collision pair (i, j) with 0 <= i < j <= n:
    pairs = [(i, j) for i in range(n + 1) for j in range(i + 1, n + 1)]

    for pi, (ci, cj) in enumerate(pairs):
        if verbose and pi % 5 == 0:
            print(f"    Processing pair ({ci},{cj}) [{pi+1}/{len(pairs)}]")

        # Residue matrix for this pair
        res_mat = os_source.residue_matrix((ci, cj), n)
        # res_mat: (target_os_dim, source_os_dim)

        # Sign from the bar complex convention
        # Standard sign: (-1)^{sum of degrees before position i}
        # For simplicity, use the sign from the residue computation
        # and a global sign (-1)^{ci} for the contraction position
        bar_sign = (-1) ** ci

        # For each source algebra index tuple (a_0, ..., a_n):
        # Contract a_{ci} and a_{cj} by bracket, get result c
        # Remaining indices form the target tuple

        # Iterate over the algebra indices efficiently
        # The contraction a_{ci}, a_{cj} -> c produces:
        # target tuple = (a_0, ..., a_{ci-1}, c, a_{ci+1}, ..., a_{cj-1}, a_{cj+1}, ..., a_n)
        # (the merged element goes to position ci, cj is removed, higher indices shift down)

        for src_os in range(source_os_dim):
            # Check which target OS elements this maps to
            res_col = res_mat[:, src_os]
            nonzero_targets = np.nonzero(res_col)[0]
            if len(nonzero_targets) == 0:
                continue

            # For each pair of algebra elements at positions ci, cj:
            for a_ci in range(g_dim):
                bracket_results = bracket[a_ci]
                for a_cj in range(g_dim):
                    br = bracket_results[a_cj]
                    if not br:
                        continue

                    # For each bracket result (c, coeff):
                    for c, coeff in br:
                        if abs(coeff) < 1e-14:
                            continue

                        # For each combination of remaining algebra indices:
                        remaining_positions = [k for k in range(n+1) if k != ci and k != cj]

                        for remaining_tuple in _iter_tuples(g_dim, len(remaining_positions)):
                            # Build source tuple
                            src_alg = [0] * (n + 1)
                            src_alg[ci] = a_ci
                            src_alg[cj] = a_cj
                            for k, pos in enumerate(remaining_positions):
                                src_alg[pos] = remaining_tuple[k]

                            # Build target tuple
                            # Merged element c goes to position min(ci, cj) = ci
                            # Elements at remaining_positions keep their relative order
                            # but are renumbered to 0, ..., n-1
                            tgt_alg = [0] * n
                            # Position ci in target gets c
                            # Other positions filled by remaining elements in order

                            # The target ordering: take the original positions
                            # 0, 1, ..., n (skipping cj), with ci getting the merged value
                            tgt_positions = [k for k in range(n+1) if k != cj]
                            for k, orig_pos in enumerate(tgt_positions):
                                if orig_pos == ci:
                                    tgt_alg[k] = c
                                else:
                                    tgt_alg[k] = src_alg[orig_pos]

                            src_idx = source_index(src_alg, src_os)

                            for tgt_os in nonzero_targets:
                                tgt_idx = target_index(tgt_alg, tgt_os)
                                mat[tgt_idx, src_idx] += bar_sign * coeff * res_col[tgt_os]

    return mat.tocsr()


def _iter_tuples(base, length):
    """Iterate over all tuples of given length with values in range(base)."""
    if length == 0:
        yield ()
        return
    for rest in _iter_tuples(base, length - 1):
        for v in range(base):
            yield rest + (v,)


# =============================================================================
# 4. Cohomology computation
# =============================================================================

def compute_bar_cohomology(g_dim, bracket, max_degree, verbose=True):
    """
    Compute bar cohomology dimensions H^n for n = 1, ..., max_degree.

    H^n = ker(d_n: B^n -> B^{n-1}) / im(d_{n+1}: B^{n+1} -> B^n)
         = dim B^n - rank(d_n) - rank(d_{n+1})

    Wait, H^n = dim ker(d_n) - dim im(d_{n+1})
             = (dim B^n - rank(d_n)) - rank(d_{n+1})
    """
    results = {}
    prev_rank = 0  # rank of d_n (from B^n to B^{n-1})

    # For H^1, we need d_1 (B^1 -> B^0) and d_2 (B^2 -> B^1)
    # d_1: B^1 -> B^0. B^1 = g (dim g_dim), B^0 = C (dim 1).
    # d_1 maps J^a to augmentation = 0, so d_1 = 0, rank = 0.

    # Pre-compute all differentials we need
    d_matrices = {}

    for n in range(1, max_degree + 2):
        if n > max_degree:
            # We need d_{max_degree+1} for im computation
            pass

        bn_dim = g_dim ** n * max(1, _factorial(n - 1))
        if verbose:
            print(f"  dim B^{n} = {g_dim}^{n} * {max(1, _factorial(n-1))} = {bn_dim}")

    # d_1: B^1 -> B^0 = 0 (augmentation is zero on generators)
    rank_d = {1: 0}

    for n in range(2, max_degree + 2):
        bn_dim = g_dim ** n * _factorial(n - 1)
        bn_minus_1_dim = g_dim ** (n - 1) * max(1, _factorial(n - 2))

        if verbose:
            print(f"\nComputing d_{n}: B^{n} ({bn_dim}) -> B^{n-1} ({bn_minus_1_dim})")

        if bn_dim > 2000000:
            if verbose:
                print(f"  Skipping: source dimension {bn_dim} too large")
            rank_d[n] = None
            continue

        mat = bar_differential_matrix(g_dim, bracket, n - 1, verbose=verbose)

        if verbose:
            print(f"  Matrix shape: {mat.shape}, nnz: {mat.nnz}")

        # Compute rank
        if mat.shape[0] * mat.shape[1] < 50000000:
            # Dense rank computation
            r = np.linalg.matrix_rank(mat.toarray(), tol=1e-8)
        else:
            # For large matrices, use sparse SVD or iterative methods
            from scipy.sparse.linalg import svds
            k = min(mat.shape) - 1
            if k > 0:
                try:
                    s = svds(mat.astype(float), k=min(k, 500), return_singular_vectors=False)
                    r = np.sum(s > 1e-8)
                    # This might undercount - fallback to dense if possible
                    if min(mat.shape) < 10000:
                        r = np.linalg.matrix_rank(mat.toarray(), tol=1e-8)
                except:
                    r = np.linalg.matrix_rank(mat.toarray(), tol=1e-8)
            else:
                r = 0

        rank_d[n] = r
        if verbose:
            print(f"  rank(d_{n}) = {r}")

    # Compute H^n
    if verbose:
        print("\n" + "=" * 50)
        print("Bar cohomology dimensions:")

    for n in range(1, max_degree + 1):
        bn_dim = g_dim ** n * max(1, _factorial(n - 1))

        if rank_d.get(n) is None or rank_d.get(n + 1) is None:
            results[n] = None
            if verbose:
                print(f"  H^{n} = ? (computation too large)")
            continue

        ker_dim = bn_dim - rank_d[n]
        im_dim = rank_d[n + 1]
        h_n = ker_dim - im_dim
        results[n] = h_n

        if verbose:
            print(f"  H^{n} = ker(d_{n})/im(d_{n+1}) = ({bn_dim} - {rank_d[n]}) - {rank_d[n+1]} = {h_n}")

    return results


def _factorial(n):
    if n <= 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# =============================================================================
# 5. Main: compute for sl_2, sl_3, and verify
# =============================================================================

def main():
    print("=" * 60)
    print("Chiral bar cohomology computation")
    print("=" * 60)

    # --- sl_2 verification ---
    print("\n--- sl_2 (dim = 3) ---")
    print("Expected (Riordan numbers R(n+3)): 3, 6, 15, 36, 91, 232, 603")

    dim2, bracket2 = sl_N_structure_constants(2)
    print(f"dim(sl_2) = {dim2}")

    results2 = compute_bar_cohomology(dim2, bracket2, max_degree=6, verbose=True)

    print("\nsl_2 results:")
    for n in sorted(results2.keys()):
        print(f"  H^{n} = {results2[n]}")

    # --- sl_3 computation ---
    print("\n\n--- sl_3 (dim = 8) ---")
    print("Known: 8, 36, 204. Need degrees 4+.")

    dim3, bracket3 = sl_N_structure_constants(3)
    print(f"dim(sl_3) = {dim3}")

    # Start with lower degrees to verify
    results3 = compute_bar_cohomology(dim3, bracket3, max_degree=5, verbose=True)

    print("\nsl_3 results:")
    for n in sorted(results3.keys()):
        print(f"  H^{n} = {results3[n]}")


if __name__ == "__main__":
    main()
