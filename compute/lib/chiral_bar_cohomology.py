"""Chiral bar cohomology via explicit fan-basis differential.

For a Kac-Moody algebra g-hat_k, the chiral bar complex is:
  B^n = g^{⊗n} ⊗ OS^{n-1}(Conf_n(C))
with dim = dim(g)^n × (n-1)!.

The differential d: B^n → B^{n-1} uses the OPE residues at collision
divisors D_{ij} on the FM compactification C-bar_n(C).

KEY INSIGHT: For a fan basis tree ω_T, the residue Res_{D_{ij}}(ω_T) is
NONZERO only if (i,j) is an edge of T. For non-edges, the actual form
has no pole at z_i = z_j, so the residue vanishes. This makes the
computation tractable: each tree contributes only n-1 terms to d.

The fan basis for OS^{n-1}(Conf_n) is indexed by increasing trees:
  T = (t_2, t_3, ..., t_n) with 1 ≤ t_k < k
  ω_T = ω_{t_2,2} ∧ ω_{t_3,3} ∧ ... ∧ ω_{t_n,n}
There are (n-1)! such trees.

CONVENTIONS:
- Cohomological grading, |d| = +1
- Bar differential has bar-degree -1
- Generators indexed 0, ..., dim_g - 1
- Structure constants: sc[(i,j)] = {k: c^k_{ij}} for [e_i, e_j] = c^k_{ij} e_k
"""

from __future__ import annotations

import numpy as np
from itertools import product as cartesian_product
from math import factorial
from typing import Dict, List, Optional, Tuple
from scipy import sparse
from scipy.sparse.linalg import svds


# =========================================================================
# Fan basis (increasing trees)
# =========================================================================

def fan_trees(n: int) -> List[Tuple[int, ...]]:
    """Enumerate all fan (increasing) trees on n vertices.

    Each tree is (t_2, ..., t_n) with 1 ≤ t_k < k.
    Returns list of (n-1)-tuples. Count = (n-1)!.
    """
    if n <= 1:
        return [()]

    def _gen(k: int) -> List[Tuple[int, ...]]:
        if k > n:
            return [()]
        sub = _gen(k + 1)
        result = []
        for t_k in range(1, k):
            for rest in sub:
                result.append((t_k,) + rest)
        return result

    return _gen(2)


def tree_edges(tree: Tuple[int, ...], n: int) -> List[Tuple[int, int]]:
    """Return edges of the tree as (parent, child) pairs, always parent < child."""
    return [(tree[k - 2], k) for k in range(2, n + 1)]


def contract_edge(tree: Tuple[int, ...], n: int, i: int, j: int) -> Tuple[int, ...]:
    """Contract edge (i,j) in tree T on {1,...,n}, returning a tree on {1,...,n-1}.

    Merges vertex j into vertex i (keeps i, removes j).
    All references to j become i, then relabel: shift vertices > j down by 1.

    Args:
        tree: fan tree (t_2, ..., t_n) on n vertices
        n: number of vertices
        i, j: edge to contract (must be an edge of the tree, i < j)

    Returns:
        Fan tree on n-1 vertices (after relabeling).
    """
    # Build parent list: parent[k] = tree[k-2] for k=2..n, parent[1]=0 (root)
    parent = [0] * (n + 1)
    for k in range(2, n + 1):
        parent[k] = tree[k - 2]

    # Merge j into i: replace all references to j with i
    for k in range(2, n + 1):
        if parent[k] == j:
            parent[k] = i

    # Remove vertex j from the parent list
    # New vertices: {1,...,n} \ {j}, relabeled so that v -> v if v < j, v -> v-1 if v > j
    def relabel(v):
        if v < j:
            return v
        elif v > j:
            return v - 1
        else:
            return i if i < j else i - 1  # j was merged into i

    new_tree = []
    for k in range(2, n + 1):
        if k == j:
            continue
        new_k = relabel(k)
        new_parent = relabel(parent[k])
        new_tree.append((new_k, new_parent))

    # Sort by new vertex number and extract parent sequence
    new_tree.sort(key=lambda x: x[0])
    result = tuple(p for _, p in new_tree)

    return result


def form_extraction_sign(tree: Tuple[int, ...], n: int, j: int) -> int:
    """Sign from extracting the form factor ω_{t_j, j} from the wedge product.

    The wedge product is ω_{t_2,2} ∧ ω_{t_3,3} ∧ ... ∧ ω_{t_n,n}.
    The factor for vertex j is at position (j-2) in the wedge (0-indexed).
    Extracting it gives sign (-1)^{j-2}.
    """
    return (-1) ** (j - 2)


# =========================================================================
# Bar differential matrix construction
# =========================================================================

def bar_differential_matrix(dim_g: int, structure_constants: Dict,
                            bar_degree: int,
                            dtype=np.float64) -> sparse.csr_matrix:
    """Build the bar differential d: B^n → B^{n-1} as a sparse matrix.

    B^n = g^{⊗n} ⊗ OS^{n-1}(Conf_n)
    Basis: (a_1, ..., a_n, T) where a_i ∈ {0,...,d-1}, T is a fan tree.

    The differential acts by:
    d(v ⊗ ω_T) = Σ_{(i,j) ∈ edges(T)} sign × [v with a_i,a_j bracketed] ⊗ ω_{T/(i,j)}

    Args:
        dim_g: dimension of g
        structure_constants: bracket data (i,j) -> {k: c^k_{ij}}
        bar_degree: n (the source bar degree)

    Returns:
        Sparse matrix with rows = B^{n-1} basis, cols = B^n basis.
    """
    n = bar_degree
    d = dim_g

    if n < 2:
        # d: B^1 → B^0 is zero (no way to reduce a single generator)
        src_dim = d * max(1, factorial(n - 1)) if n >= 1 else 1
        return sparse.csr_matrix((1, src_dim), dtype=dtype)

    # Source: B^n = g^{⊗n} × trees_n
    trees_n = fan_trees(n)
    n_trees_n = len(trees_n)  # = (n-1)!
    tree_n_idx = {t: i for i, t in enumerate(trees_n)}
    src_dim = d ** n * n_trees_n

    # Target: B^{n-1} = g^{⊗(n-1)} × trees_{n-1}
    trees_nm1 = fan_trees(n - 1)
    n_trees_nm1 = len(trees_nm1)  # = (n-2)!
    tree_nm1_idx = {t: i for i, t in enumerate(trees_nm1)}
    tgt_dim = d ** (n - 1) * n_trees_nm1

    # Build sparse matrix entries
    rows = []
    cols = []
    vals = []

    for t_idx, tree in enumerate(trees_n):
        edges = tree_edges(tree, n)
        for (parent, child) in edges:
            i, j = parent, child  # i < j always for fan trees
            # Sign from extracting form factor
            ext_sign = form_extraction_sign(tree, n, j)

            # Contract tree
            contracted = contract_edge(tree, n, i, j)
            ct_idx = tree_nm1_idx.get(contracted)
            if ct_idx is None:
                continue  # shouldn't happen

            # Iterate over all tensor basis elements
            for tensor_flat in range(d ** n):
                # Decode tensor indices
                indices = []
                tmp = tensor_flat
                for _ in range(n):
                    indices.append(tmp % d)
                    tmp //= d
                indices.reverse()  # indices[0] = first tensor factor

                a_i = indices[i - 1]  # 0-indexed: position i-1
                a_j = indices[j - 1]

                # Bracket [a_i, a_j]
                bracket = structure_constants.get((a_i, a_j), {})
                if not bracket:
                    continue

                # Koszul sign: moving a_j past elements between positions i and j
                # In the bar construction with suspension, each element has degree 1
                # Moving a_j past (j-i-1) elements: sign = (-1)^{j-i-1}
                koszul_sign = (-1) ** (j - i - 1)

                total_sign = ext_sign * koszul_sign

                for c, coeff in bracket.items():
                    if coeff == 0:
                        continue
                    # Build target tensor: replace a_i with c, remove a_j
                    new_indices = list(indices)
                    new_indices[i - 1] = c
                    del new_indices[j - 1]

                    # Encode target tensor
                    target_flat = 0
                    for idx_val in new_indices:
                        target_flat = target_flat * d + idx_val

                    # Target index in B^{n-1}
                    row = target_flat * n_trees_nm1 + ct_idx
                    # Source index in B^n
                    col = tensor_flat * n_trees_n + t_idx

                    rows.append(row)
                    cols.append(col)
                    vals.append(total_sign * coeff)

    mat = sparse.coo_matrix((vals, (rows, cols)),
                            shape=(tgt_dim, src_dim), dtype=dtype)
    return mat.tocsr()


# =========================================================================
# Bar cohomology computation
# =========================================================================

def bar_cohomology_dim(dim_g: int, structure_constants: Dict,
                       bar_degree: int, max_degree: int = None,
                       verbose: bool = False) -> int:
    """Compute dim H^n(B-bar) at bar degree n.

    H^n = ker(d_n: B^n → B^{n-1}) / im(d_{n+1}: B^{n+1} → B^n)
    dim H^n = dim B^n - rank(d_n) - rank(d_{n+1})

    Args:
        dim_g: dimension of g
        structure_constants: bracket data
        bar_degree: n
        max_degree: not used (for API compatibility)
        verbose: print progress

    Returns:
        Dimension of H^n.
    """
    n = bar_degree
    d = dim_g

    if n < 1:
        return 1  # H^0 = k

    # Build d_n: B^n → B^{n-1}
    if verbose:
        src_n = d ** n * factorial(n - 1) if n >= 1 else 1
        tgt_n = d ** (n - 1) * factorial(n - 2) if n >= 2 else 1
        print(f"Building d_{n}: B^{n} ({src_n}) → B^{n-1} ({tgt_n})")
    d_n = bar_differential_matrix(dim_g, structure_constants, n)
    rank_dn = matrix_rank_sparse(d_n, verbose=verbose)

    # Build d_{n+1}: B^{n+1} → B^n
    src_np1 = d ** (n + 1) * factorial(n)
    if verbose:
        print(f"Building d_{n+1}: B^{n+1} ({src_np1}) → B^{n} ({d_n.shape[1]})")
    d_np1 = bar_differential_matrix(dim_g, structure_constants, n + 1)
    rank_dnp1 = matrix_rank_sparse(d_np1, verbose=verbose)

    dim_Bn = d_n.shape[1]
    h_n = dim_Bn - rank_dn - rank_dnp1

    if verbose:
        print(f"H^{n} = dim B^{n} - rank(d_{n}) - rank(d_{n+1})")
        print(f"     = {dim_Bn} - {rank_dn} - {rank_dnp1} = {h_n}")

    return h_n


def matrix_rank_sparse(mat: sparse.spmatrix, verbose: bool = False) -> int:
    """Compute rank of a sparse matrix over Q (using float64 with tolerance)."""
    if mat.nnz == 0:
        return 0

    m, n = mat.shape
    if m == 0 or n == 0:
        return 0

    # For small matrices, use dense SVD
    if m * n < 10_000_000:
        dense = mat.toarray()
        rank = np.linalg.matrix_rank(dense)
        if verbose:
            print(f"  Dense rank computation: {m}×{n}, rank={rank}")
        return rank

    # For larger matrices, use sparse rank via QR or SVD
    if verbose:
        print(f"  Sparse rank computation: {m}×{n}, nnz={mat.nnz}")

    # Use scipy sparse QR for rank
    try:
        from scipy.sparse.linalg import splu
        # LU decomposition can give rank for square matrices
        # For rectangular, we can use QR
    except ImportError:
        pass

    # Fallback: convert to dense if feasible
    if m * n < 500_000_000:
        dense = mat.toarray()
        rank = np.linalg.matrix_rank(dense, tol=1e-8)
        if verbose:
            print(f"  Dense rank: {rank}")
        return rank

    # For very large matrices, use modular arithmetic
    return matrix_rank_modular(mat, verbose=verbose)


def matrix_rank_modular(mat: sparse.spmatrix, primes: List[int] = None,
                        verbose: bool = False) -> int:
    """Compute rank of an integer matrix using modular arithmetic.

    Compute rank mod p for several primes and take the maximum.
    For integer matrices, rank over Q = max rank over F_p (for large enough p).
    """
    if primes is None:
        primes = [65521, 65519, 65497]  # large primes < 2^16

    max_rank = 0
    for p in primes:
        mat_mod = mat.copy()
        mat_mod.data = mat_mod.data.astype(np.int64) % p
        # Remove zeros
        mat_mod.eliminate_zeros()

        # Gaussian elimination mod p
        rank = gaussian_elim_rank_mod(mat_mod, p, verbose=verbose)
        if verbose:
            print(f"  Rank mod {p}: {rank}")
        max_rank = max(max_rank, rank)

    return max_rank


def gaussian_elim_rank_mod(mat: sparse.spmatrix, p: int,
                           verbose: bool = False) -> int:
    """Gaussian elimination rank over F_p for a sparse matrix."""
    # Convert to dense array mod p for smaller matrices
    m, n = mat.shape
    if m * n < 200_000_000:
        A = mat.toarray().astype(np.int64) % p
        return _dense_rank_mod(A, p)

    # For very large matrices, use row-by-row elimination
    return _sparse_rank_mod(mat, p, verbose=verbose)


def _dense_rank_mod(A: np.ndarray, p: int) -> int:
    """Rank of dense matrix over F_p via Gaussian elimination."""
    m, n = A.shape
    A = A.copy() % p
    rank = 0
    pivot_cols = []

    for col in range(n):
        # Find pivot in column col, rows rank..m-1
        pivot_row = None
        for row in range(rank, m):
            if A[row, col] % p != 0:
                pivot_row = row
                break

        if pivot_row is None:
            continue

        # Swap rows
        if pivot_row != rank:
            A[[rank, pivot_row]] = A[[pivot_row, rank]]

        # Scale pivot row
        inv_pivot = pow(int(A[rank, col]), p - 2, p)  # Fermat's little theorem
        A[rank] = (A[rank] * inv_pivot) % p

        # Eliminate column
        for row in range(m):
            if row == rank:
                continue
            if A[row, col] % p != 0:
                factor = A[row, col]
                A[row] = (A[row] - factor * A[rank]) % p

        pivot_cols.append(col)
        rank += 1

        if rank == m:
            break

    return rank


def _sparse_rank_mod(mat: sparse.spmatrix, p: int,
                     verbose: bool = False) -> int:
    """Sparse rank computation mod p using row reduction."""
    # Convert to lil_matrix for efficient row operations
    m, n = mat.shape
    A = mat.tolil()

    rank = 0
    used_rows = set()

    for col in range(n):
        if rank >= m:
            break

        # Find pivot
        pivot_row = None
        for row in range(m):
            if row in used_rows:
                continue
            val = int(A[row, col]) % p
            if val != 0:
                pivot_row = row
                break

        if pivot_row is None:
            continue

        used_rows.add(pivot_row)
        inv_pivot = pow(int(A[pivot_row, col]) % p, p - 2, p)

        # Scale pivot row
        pivot_data = A.getrow(pivot_row).toarray().flatten()
        pivot_data = (pivot_data * inv_pivot) % p

        # Eliminate
        for row in range(m):
            if row == pivot_row:
                continue
            val = int(A[row, col]) % p
            if val != 0:
                row_data = A.getrow(row).toarray().flatten()
                row_data = (row_data - val * pivot_data) % p
                A[row] = sparse.lil_matrix(row_data.reshape(1, -1))

        rank += 1
        if verbose and rank % 100 == 0:
            print(f"    Rank progress: {rank}/{min(m,n)}")

    return rank


# =========================================================================
# Standard Lie algebra data
# =========================================================================

def sl2_structure_constants() -> Dict:
    """sl_2 structure constants. Basis: 0=e, 1=h, 2=f."""
    return {
        (0, 2): {1: 1},     # [e,f] = h
        (2, 0): {1: -1},    # [f,e] = -h
        (1, 0): {0: 2},     # [h,e] = 2e
        (0, 1): {0: -2},    # [e,h] = -2e
        (1, 2): {2: -2},    # [h,f] = -2f
        (2, 1): {2: 2},     # [f,h] = 2f
    }


def sl3_structure_constants() -> Dict:
    """sl_3 structure constants.

    Basis: 0=H1, 1=H2, 2=E1, 3=E2, 4=E3, 5=F1, 6=F2, 7=F3
    Cartan matrix: A = [[2,-1],[-1,2]]

    Roots: alpha1 = (2,-1), alpha2 = (-1,2), alpha3 = alpha1+alpha2 = (1,1)
    [H1,E1]=2E1, [H1,E2]=-E2, [H1,E3]=E3
    [H2,E1]=-E1, [H2,E2]=2E2, [H2,E3]=E3
    [E1,F1]=H1, [E2,F2]=H2, [E3,F3]=H1+H2
    [E1,E2]=E3, [F1,F2]=-F3
    [E1,F3]=-F2, [E2,F3]=F1  (cross terms)
    [E3,F1]=-E2, [E3,F2]=E1  (CORRECTED signs: verified by matrix units)
    """
    sc = {}

    # [H1, roots]
    sc[(0, 2)] = {2: 2};   sc[(2, 0)] = {2: -2}   # [H1,E1]=2E1
    sc[(0, 3)] = {3: -1};  sc[(3, 0)] = {3: 1}     # [H1,E2]=-E2
    sc[(0, 4)] = {4: 1};   sc[(4, 0)] = {4: -1}    # [H1,E3]=E3
    sc[(0, 5)] = {5: -2};  sc[(5, 0)] = {5: 2}     # [H1,F1]=-2F1
    sc[(0, 6)] = {6: 1};   sc[(6, 0)] = {6: -1}    # [H1,F2]=F2
    sc[(0, 7)] = {7: -1};  sc[(7, 0)] = {7: 1}     # [H1,F3]=-F3

    # [H2, roots]
    sc[(1, 2)] = {2: -1};  sc[(2, 1)] = {2: 1}     # [H2,E1]=-E1
    sc[(1, 3)] = {3: 2};   sc[(3, 1)] = {3: -2}    # [H2,E2]=2E2
    sc[(1, 4)] = {4: 1};   sc[(4, 1)] = {4: -1}    # [H2,E3]=E3
    sc[(1, 5)] = {5: 1};   sc[(5, 1)] = {5: -1}    # [H2,F1]=F1
    sc[(1, 6)] = {6: -2};  sc[(6, 1)] = {6: 2}     # [H2,F2]=-2F2
    sc[(1, 7)] = {7: -1};  sc[(7, 1)] = {7: 1}     # [H2,F3]=-F3

    # [E,F] Cartan elements
    sc[(2, 5)] = {0: 1};   sc[(5, 2)] = {0: -1}    # [E1,F1]=H1
    sc[(3, 6)] = {1: 1};   sc[(6, 3)] = {1: -1}    # [E2,F2]=H2
    sc[(4, 7)] = {0: 1, 1: 1}; sc[(7, 4)] = {0: -1, 1: -1}  # [E3,F3]=H1+H2

    # [E,E] and [F,F] (root addition)
    sc[(2, 3)] = {4: 1};   sc[(3, 2)] = {4: -1}    # [E1,E2]=E3
    sc[(5, 6)] = {7: -1};  sc[(6, 5)] = {7: 1}     # [F1,F2]=-F3

    # Cross terms (CORRECTED by matrix unit verification)
    sc[(2, 7)] = {6: -1};  sc[(7, 2)] = {6: 1}     # [E1,F3]=-F2
    sc[(3, 7)] = {5: 1};   sc[(7, 3)] = {5: -1}    # [E2,F3]=F1
    sc[(4, 5)] = {3: -1};  sc[(5, 4)] = {3: 1}     # [E3,F1]=-E2
    sc[(4, 6)] = {2: 1};   sc[(6, 4)] = {2: -1}    # [E3,F2]=E1

    return sc


def verify_jacobi(dim_g: int, sc: Dict) -> int:
    """Verify Jacobi identity for all triples. Returns number of violations."""
    violations = 0
    for a in range(dim_g):
        for b in range(dim_g):
            for c in range(dim_g):
                # [[a,b],c] + [[b,c],a] + [[c,a],b] = 0
                total = {}
                for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
                    bracket_xy = sc.get((x, y), {})
                    for k, coeff_k in bracket_xy.items():
                        bracket_kz = sc.get((k, z), {})
                        for m, coeff_m in bracket_kz.items():
                            total[m] = total.get(m, 0) + coeff_k * coeff_m
                for m, val in total.items():
                    if abs(val) > 1e-12:
                        violations += 1
    return violations


# =========================================================================
# Verification and testing
# =========================================================================

def verify_d_squared(dim_g: int, sc: Dict, bar_degree: int,
                     verbose: bool = False) -> bool:
    """Verify d² = 0 for the bar differential at given degree.

    d_{n-1} ∘ d_n should be the zero matrix.
    """
    n = bar_degree
    if n < 3:
        return True  # d_1 ∘ d_2 is trivially zero (d_1 = 0)

    d_n = bar_differential_matrix(dim_g, sc, n)
    d_nm1 = bar_differential_matrix(dim_g, sc, n - 1)

    # d_{n-1} ∘ d_n
    d_sq = d_nm1 @ d_n

    max_val = np.max(np.abs(d_sq.toarray())) if d_sq.nnz > 0 else 0
    is_zero = max_val < 1e-10

    if verbose:
        print(f"d²=0 check at degree {n}: max|d²| = {max_val:.2e}, {'PASS' if is_zero else 'FAIL'}")

    return is_zero


def run_sl2_verification(max_degree: int = 4, verbose: bool = True):
    """Verify bar cohomology for sl_2 against Riordan numbers."""
    sc = sl2_structure_constants()
    d = 3

    if verbose:
        jv = verify_jacobi(d, sc)
        print(f"sl_2 Jacobi violations: {jv}")

    # Proved bar cohomology dims (PBW/CE); NOT the Riordan numbers
    expected_dims = [None, 3, 5, 15, 36, 91, 232, 603]

    results = {}
    for n in range(1, max_degree + 1):
        if verbose:
            print(f"\n--- Bar degree {n} ---")

        # Verify d² = 0
        if n >= 3:
            d2_ok = verify_d_squared(d, sc, n, verbose=verbose)
            if not d2_ok:
                print(f"WARNING: d² ≠ 0 at degree {n}!")

        h_n = bar_cohomology_dim(d, sc, n, verbose=verbose)
        expected = expected_dims[n] if n < len(expected_dims) else None
        match = h_n == expected if expected is not None else None
        results[n] = (h_n, expected, match)

        if verbose:
            status = "✓" if match else ("✗" if match is False else "?")
            print(f"H^{n}(B-bar(sl_2)) = {h_n} (expected {expected}) {status}")

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("CHIRAL BAR COHOMOLOGY: VERIFICATION")
    print("=" * 60)
    run_sl2_verification(max_degree=4, verbose=True)
