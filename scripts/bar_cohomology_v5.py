#!/usr/bin/env python3
"""
Bar cohomology computation for chiral algebras — pure Python (no numpy).

Uses exact rational arithmetic (fractions.Fraction) to avoid numerical issues.
"""

from fractions import Fraction
from itertools import combinations, product as iterproduct
from math import factorial
import sys
import time

ZERO = Fraction(0)
ONE = Fraction(1)

# ========================================
# Lie algebra data
# ========================================

def sl2_data():
    """sl2: basis e(0), f(1), h(2). [e,f]=h, [h,e]=2e, [h,f]=-2f."""
    d = 3
    f = {}
    f[(0,1,2)] = ONE; f[(1,0,2)] = -ONE
    f[(2,0,0)] = Fraction(2); f[(0,2,0)] = Fraction(-2)
    f[(2,1,1)] = Fraction(-2); f[(1,2,1)] = Fraction(2)
    kf = {}
    kf[(0,1)] = ONE; kf[(1,0)] = ONE; kf[(2,2)] = Fraction(2)
    return d, f, kf

def sl3_data():
    """sl3: basis H1(0),H2(1),E1(2),E2(3),E3(4),F1(5),F2(6),F3(7)."""
    d = 8
    f = {}
    # [Hi, Ej] = A_ij * Ej
    f[(0,2,2)]=Fraction(2);  f[(2,0,2)]=Fraction(-2)
    f[(0,3,3)]=Fraction(-1); f[(3,0,3)]=Fraction(1)
    f[(1,2,2)]=Fraction(-1); f[(2,1,2)]=Fraction(1)
    f[(1,3,3)]=Fraction(2);  f[(3,1,3)]=Fraction(-2)
    f[(0,4,4)]=Fraction(1);  f[(4,0,4)]=Fraction(-1)
    f[(1,4,4)]=Fraction(1);  f[(4,1,4)]=Fraction(-1)
    # [Hi, Fj] = -A_ij * Fj
    f[(0,5,5)]=Fraction(-2); f[(5,0,5)]=Fraction(2)
    f[(0,6,6)]=Fraction(1);  f[(6,0,6)]=Fraction(-1)
    f[(1,5,5)]=Fraction(1);  f[(5,1,5)]=Fraction(-1)
    f[(1,6,6)]=Fraction(-2); f[(6,1,6)]=Fraction(2)
    f[(0,7,7)]=Fraction(-1); f[(7,0,7)]=Fraction(1)
    f[(1,7,7)]=Fraction(-1); f[(7,1,7)]=Fraction(1)
    # [Ei, Fj] and [Ei, Ej]
    f[(2,5,0)]=ONE; f[(5,2,0)]=-ONE    # [E1,F1]=H1
    f[(3,6,1)]=ONE; f[(6,3,1)]=-ONE    # [E2,F2]=H2
    f[(2,3,4)]=ONE; f[(3,2,4)]=-ONE    # [E1,E2]=E3
    f[(6,5,7)]=ONE; f[(5,6,7)]=-ONE    # [F2,F1]=F3  (note: [F2,F1], not [F1,F2])
    f[(2,7,6)]=-ONE; f[(7,2,6)]=ONE    # [E1,F3]=-F2
    f[(3,7,5)]=ONE; f[(7,3,5)]=-ONE    # [E2,F3]=F1
    f[(4,5,3)]=-ONE; f[(5,4,3)]=ONE    # [E3,F1]=-E2
    f[(4,6,2)]=ONE; f[(6,4,2)]=-ONE    # [E3,F2]=E1
    f[(4,7,0)]=ONE; f[(7,4,0)]=-ONE    # [E3,F3]=H1+H2
    f[(4,7,1)]=ONE; f[(7,4,1)]=-ONE
    # Killing form
    kf = {}
    kf[(0,0)]=Fraction(2); kf[(0,1)]=Fraction(-1)
    kf[(1,0)]=Fraction(-1); kf[(1,1)]=Fraction(2)
    kf[(2,5)]=ONE; kf[(5,2)]=ONE
    kf[(3,6)]=ONE; kf[(6,3)]=ONE
    kf[(4,7)]=ONE; kf[(7,4)]=ONE
    return d, f, kf

def verify_jacobi(d, sc):
    """Verify Jacobi identity for structure constants."""
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for g in range(d):
                    val = ZERO
                    for e in range(d):
                        val += sc.get((b,c,e), ZERO)*sc.get((a,e,g), ZERO)
                        val += sc.get((c,a,e), ZERO)*sc.get((b,e,g), ZERO)
                        val += sc.get((a,b,e), ZERO)*sc.get((c,e,g), ZERO)
                    if val != ZERO:
                        return False
    return True

# ========================================
# NBC basis for OS algebra
# ========================================

def nbc_basis(n, k):
    """NBC basis for OS^k(n). n points labeled 1..n, k = form degree."""
    if k == 0:
        return [()]
    if n <= 1 or k >= n:
        return [] if k > 0 else [()]
    edges = [(i,j) for i in range(1, n+1) for j in range(i+1, n+1)]
    # Broken circuits: for each 3-cycle {(i,j),(i,k),(j,k)} with i<j<k,
    # largest edge in lex = (j,k), so BC = {(i,j),(i,k)}
    broken_circuits = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for kk in range(j+1, n+1):
                broken_circuits.append(((i,j), (i,kk)))
    basis = []
    for subset in combinations(edges, k):
        subset_set = set(subset)
        is_nbc = all(not (bc[0] in subset_set and bc[1] in subset_set)
                      for bc in broken_circuits)
        if is_nbc:
            basis.append(tuple(sorted(subset)))
    return basis

# ========================================
# Arnold reduction
# ========================================

def arnold_reduce(edges_list, sign, n, k, target_basis, basis_index):
    """
    Express sign * ω_{e1}∧...∧ω_{ek} as NBC combination.
    Returns dict {basis_idx: Fraction coefficient}.
    """
    result = {}
    queue = [(sign, tuple(sorted(edges_list)))]
    max_iter = 2000
    it = 0
    while queue and it < max_iter:
        it += 1
        s, edges = queue.pop()
        if s == ZERO:
            continue
        # Check for duplicate edges (= 0 by antisymmetry)
        if len(set(edges)) < len(edges):
            continue
        edges = tuple(sorted(edges))
        # Check if in NBC basis
        if edges in basis_index:
            idx = basis_index[edges]
            result[idx] = result.get(idx, ZERO) + s
            continue
        # Find a broken circuit and apply Arnold relation
        bc_found = False
        for pos_a in range(len(edges)):
            ea = edges[pos_a]
            for pos_b in range(pos_a+1, len(edges)):
                eb = edges[pos_b]
                # Check if (ea, eb) is a broken circuit
                # BC = {(i,j),(i,kk)} where i<j<kk
                i_a, j_a = ea
                i_b, j_b = eb
                if i_a == i_b:
                    # This is a broken circuit {(i,j),(i,kk)} with j<kk
                    i, j, kk = i_a, j_a, j_b
                    jk = (min(j,kk), max(j,kk))
                    # Arnold: ω_{ij}∧ω_{ik} = ω_{ij}∧ω_{jk} - ω_{ik}∧ω_{jk}
                    # In our monomial, ω_{ij} is at pos_a, ω_{ik} at pos_b
                    # Move them adjacent: sign from transpositions
                    # They're already ordered (pos_a < pos_b), so:
                    # Bring pos_b to pos_a+1: sign (-1)^(pos_b - pos_a - 1)
                    move_sign = (-ONE)**(pos_b - pos_a - 1)
                    # Now have: ...ω_{ij}∧ω_{ik}∧...rest
                    rest = list(edges[:pos_a]) + list(edges[pos_a+1:pos_b]) + list(edges[pos_b+1:])
                    # Term 1: ω_{ij}∧ω_{jk}∧rest
                    t1 = [ea, jk] + rest
                    queue.append((s * move_sign, tuple(t1)))
                    # Term 2: -ω_{ik}∧ω_{jk}∧rest
                    t2 = [eb, jk] + rest
                    queue.append((-s * move_sign, tuple(t2)))
                    bc_found = True
                    break
            if bc_found:
                break
        if not bc_found:
            # Should be NBC but wasn't found in index - error
            print(f"  WARNING: {edges} not found in basis and no BC detected!")
    if it >= max_iter:
        print(f"  WARNING: Arnold reduction did not converge after {max_iter} iterations")
    return result

# ========================================
# OS contraction
# ========================================

def os_contraction_matrix(n, k, pq, source_basis, target_basis, target_index):
    """
    Contraction C_{pq}: OS^k(n) -> OS^{k-1}(n-1).
    Returns sparse dict: {(tgt_idx, src_idx): Fraction}.
    """
    p, q = pq
    n_new = n - 1

    def relabel(v):
        if v == q: return p
        if v > q: return v - 1
        return v

    def relabel_edge(e):
        a, b = relabel(e[0]), relabel(e[1])
        if a == b: return None
        return (min(a,b), max(a,b))

    entries = {}
    for col, src_edges in enumerate(source_basis):
        if pq not in src_edges:
            continue
        pos = list(src_edges).index(pq)
        sign = (-ONE)**pos
        remaining = list(src_edges[:pos]) + list(src_edges[pos+1:])
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
        if len(relabeled) == 0:
            # k=1: result is scalar
            if () in target_index:
                idx = target_index[()]
                entries[(idx, col)] = entries.get((idx, col), ZERO) + sign
        else:
            coeffs = arnold_reduce(relabeled, sign, n_new, k-1,
                                   target_basis, target_index)
            for idx, coeff in coeffs.items():
                if coeff != ZERO:
                    entries[(idx, col)] = entries.get((idx, col), ZERO) + coeff
    return entries

# ========================================
# Sparse matrix operations
# ========================================

def sparse_mat_mul(A, B, rows_A, cols_A, cols_B):
    """Multiply sparse matrices A (rows_A x cols_A) * B (cols_A x cols_B)."""
    # A, B are dicts {(i,j): val}
    # Build column lookup for A
    result = {}
    # Group B by row
    B_by_row = {}
    for (r, c), v in B.items():
        if v == ZERO: continue
        if r not in B_by_row:
            B_by_row[r] = []
        B_by_row[r].append((c, v))
    # For each entry in A, multiply with B entries in that column
    for (i, k), a_val in A.items():
        if a_val == ZERO: continue
        if k in B_by_row:
            for (j, b_val) in B_by_row[k]:
                key = (i, j)
                result[key] = result.get(key, ZERO) + a_val * b_val
    return result

def sparse_rank(mat_dict, nrows, ncols):
    """Compute rank of sparse matrix using exact Gaussian elimination."""
    # Convert to dense-ish row format
    rows = {}
    for (i, j), v in mat_dict.items():
        if v != ZERO:
            if i not in rows:
                rows[i] = {}
            rows[i][j] = v

    rank = 0
    pivot_cols = set()
    row_list = sorted(rows.keys())

    # For each column, find a pivot row
    col_order = sorted(set(j for r in rows.values() for j in r.keys()))

    for col in col_order:
        # Find a row with nonzero entry in this column
        pivot_row = None
        for r in row_list:
            if r in rows and col in rows[r] and rows[r][col] != ZERO:
                if col not in pivot_cols:
                    pivot_row = r
                    break
        if pivot_row is None:
            continue

        pivot_cols.add(col)
        rank += 1
        pivot_val = rows[pivot_row][col]

        # Eliminate this column from all other rows
        for r in row_list:
            if r == pivot_row:
                continue
            if r in rows and col in rows[r] and rows[r][col] != ZERO:
                factor = rows[r][col] / pivot_val
                for c, v in rows[pivot_row].items():
                    if c not in rows[r]:
                        rows[r][c] = ZERO
                    rows[r][c] -= factor * v
                # Clean up zeros
                rows[r] = {c: v for c, v in rows[r].items() if v != ZERO}
                if not rows[r]:
                    del rows[r]

    return rank

# ========================================
# Bar differential — sparse
# ========================================

def build_bar_differential_sparse(dim_g, struct_const, killing_form, level, n_source):
    """
    Build d: B^n -> B^{n-1} as sparse dict.
    B^n = A^{tensor (n+1)} tensor OS^n(n+1), dim A = dim_g + 1.
    """
    d = dim_g
    dim_A = d + 1
    n = n_source
    n_target = n - 1
    pts_src = n + 1
    pts_tgt = n

    os_src = nbc_basis(pts_src, n)
    os_tgt = nbc_basis(pts_tgt, n_target) if n_target >= 0 else [()]
    os_tgt_index = {b: i for i, b in enumerate(os_tgt)}

    dim_os_src = len(os_src)
    dim_os_tgt = len(os_tgt)
    dim_source = dim_A**pts_src * dim_os_src
    dim_target = dim_A**pts_tgt * dim_os_tgt if n_target >= 0 else dim_A

    if n <= 0 or dim_source == 0 or dim_target == 0:
        return {}, dim_target, dim_source

    print(f"  d: B^{n} ({dim_source}) -> B^{n-1} ({dim_target})")

    # Precompute chiral bracket: mu_ch[a][b] = [(c, coeff), ...]
    mu_ch = [[[] for _ in range(dim_A)] for _ in range(dim_A)]
    lev = Fraction(level)
    for a in range(1, dim_A):
        for b in range(1, dim_A):
            terms = []
            for c in range(d):
                val = struct_const.get((a-1, b-1, c), ZERO)
                if val != ZERO:
                    terms.append((c+1, val))
            kf_val = lev * killing_form.get((a-1, b-1), ZERO)
            if kf_val != ZERO:
                terms.append((0, kf_val))
            mu_ch[a][b] = terms

    # Precompute OS contraction matrices
    print(f"  Computing OS contractions...")
    contraction = {}
    for i in range(1, pts_src+1):
        for j in range(i+1, pts_src+1):
            contraction[(i,j)] = os_contraction_matrix(
                pts_src, n, (i,j), os_src, os_tgt, os_tgt_index)

    # Build differential
    print(f"  Building differential entries...")
    mat = {}
    count = 0

    for src_config in iterproduct(range(dim_A), repeat=pts_src):
        for os_src_idx in range(dim_os_src):
            # Source index
            src_flat = 0
            for a in src_config:
                src_flat = src_flat * dim_A + a
            src_idx = src_flat * dim_os_src + os_src_idx

            for i in range(1, pts_src+1):
                for j in range(i+1, pts_src+1):
                    a_i = src_config[i-1]
                    a_j = src_config[j-1]
                    bracket_terms = mu_ch[a_i][a_j]
                    if not bracket_terms:
                        continue

                    C_ij = contraction[(i,j)]

                    for os_tgt_idx in range(dim_os_tgt):
                        c_coeff = C_ij.get((os_tgt_idx, os_src_idx), ZERO)
                        if c_coeff == ZERO:
                            continue

                        for bracket_result, bracket_coeff in bracket_terms:
                            tgt_list = list(src_config)
                            tgt_list[i-1] = bracket_result
                            del tgt_list[j-1]
                            tgt_flat = 0
                            for a in tgt_list:
                                tgt_flat = tgt_flat * dim_A + a
                            tgt_idx = tgt_flat * dim_os_tgt + os_tgt_idx

                            sign = (-ONE)**(j - i - 1)
                            val = sign * bracket_coeff * c_coeff
                            key = (tgt_idx, src_idx)
                            mat[key] = mat.get(key, ZERO) + val
                            count += 1

    # Clean zeros
    mat = {k: v for k, v in mat.items() if v != ZERO}
    print(f"  {len(mat)} nonzero entries (from {count} accumulations)")
    return mat, dim_target, dim_source

# ========================================
# Main
# ========================================

def compute_bar_cohomology(algebra='sl2', level=1, max_degree=4):
    if algebra == 'sl2':
        d, sc, kf = sl2_data()
    elif algebra == 'sl3':
        d, sc, kf = sl3_data()
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    print(f"Algebra: {algebra}, dim g = {d}, level k = {level}")
    print(f"Verifying Jacobi...", end=" ")
    t0 = time.time()
    assert verify_jacobi(d, sc), "FAILED!"
    print(f"OK ({time.time()-t0:.1f}s)")

    dim_A = d + 1
    print(f"\nBar complex dimensions (A = g + C|0>, dim A = {dim_A}):")
    dims = {}
    for n in range(max_degree + 1):
        pts = n + 1
        dim_os = factorial(n) if n > 0 else 1
        dim_bn = dim_A**pts * dim_os
        dims[n] = dim_bn
        print(f"  B^{n} = {dim_A}^{pts} x {dim_os} = {dim_bn}")

    print(f"\nBuilding differentials...")
    diffs = {}
    diff_dims = {}
    for n in range(1, max_degree + 1):
        print(f"\n--- Degree {n} ---")
        t0 = time.time()
        mat, dim_tgt, dim_src = build_bar_differential_sparse(d, sc, kf, level, n)
        diffs[n] = mat
        diff_dims[n] = (dim_tgt, dim_src)
        print(f"  Time: {time.time()-t0:.1f}s")

    # Verify d^2 = 0
    print(f"\nVerifying d^2 = 0...")
    for n in range(2, max_degree + 1):
        if n in diffs and (n-1) in diffs:
            t0 = time.time()
            d2 = sparse_mat_mul(diffs[n-1], diffs[n],
                                diff_dims[n-1][0], diff_dims[n-1][1],
                                diff_dims[n][1])
            max_val = max((abs(v) for v in d2.values()), default=ZERO)
            status = "OK" if max_val == ZERO else f"FAILED (max = {max_val})"
            print(f"  d_{n-1} o d_{n}: {status} ({time.time()-t0:.1f}s)")

    # Compute ranks and homology
    print(f"\nComputing ranks...")
    ranks = {}
    for n in range(1, max_degree + 1):
        t0 = time.time()
        r = sparse_rank(diffs[n], diff_dims[n][0], diff_dims[n][1])
        ranks[n] = r
        print(f"  rank(d_{n}) = {r} ({time.time()-t0:.1f}s)")

    print(f"\nHomology dimensions:")
    for n in range(max_degree):
        ker = dims[n] - ranks.get(n, 0)
        im = ranks.get(n+1, 0)
        h_n = ker - im
        print(f"  H^{n} = {dims[n]} - {ranks.get(n,0)} - {ranks.get(n+1,0)} = {h_n}")

    # Expected for sl2: Riordan numbers R(n+3) = 1, 3, 6, 15, 36, 91, ...
    if algebra == 'sl2':
        riordan = [1, 0, 1, 1, 3, 6, 15, 36, 91, 239, 628]
        print(f"\nExpected (Riordan R(n+3)): {[riordan[n+3] for n in range(min(max_degree, len(riordan)-3))]}")

if __name__ == '__main__':
    algebra = sys.argv[1] if len(sys.argv) > 1 else 'sl2'
    level = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    max_deg = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    compute_bar_cohomology(algebra, level, max_deg)
