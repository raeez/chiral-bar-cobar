#!/usr/bin/env python3
"""
Bar cohomology for chiral algebras — corrected formulation.

Bar complex: B^n = g^{⊗n} ⊗ OS^{n-1}(n)
- n tensor factors from g
- (n-1)-forms from OS^{n-1}(Conf_n(C))
- dim B^n = d^n · (n-1)!

Differential: d: B^n → B^{n-1} merges pair (i,j) via Lie bracket.
"""

from fractions import Fraction
from itertools import combinations, product as iterproduct
from math import factorial
import sys, time

ZERO = Fraction(0)
ONE = Fraction(1)

# ========================================
# Lie algebra data
# ========================================

def sl2_data():
    d = 3  # e(0), f(1), h(2)
    sc = {}
    sc[(0,1,2)] = ONE; sc[(1,0,2)] = -ONE        # [e,f]=h
    sc[(2,0,0)] = Fraction(2); sc[(0,2,0)] = Fraction(-2)  # [h,e]=2e
    sc[(2,1,1)] = Fraction(-2); sc[(1,2,1)] = Fraction(2)  # [h,f]=-2f
    return d, sc

def sl3_data():
    d = 8  # H1(0),H2(1),E1(2),E2(3),E3(4),F1(5),F2(6),F3(7)
    sc = {}
    sc[(0,2,2)]=Fraction(2);  sc[(2,0,2)]=Fraction(-2)
    sc[(0,3,3)]=Fraction(-1); sc[(3,0,3)]=Fraction(1)
    sc[(1,2,2)]=Fraction(-1); sc[(2,1,2)]=Fraction(1)
    sc[(1,3,3)]=Fraction(2);  sc[(3,1,3)]=Fraction(-2)
    sc[(0,4,4)]=Fraction(1);  sc[(4,0,4)]=Fraction(-1)
    sc[(1,4,4)]=Fraction(1);  sc[(4,1,4)]=Fraction(-1)
    sc[(0,5,5)]=Fraction(-2); sc[(5,0,5)]=Fraction(2)
    sc[(0,6,6)]=Fraction(1);  sc[(6,0,6)]=Fraction(-1)
    sc[(1,5,5)]=Fraction(1);  sc[(5,1,5)]=Fraction(-1)
    sc[(1,6,6)]=Fraction(-2); sc[(6,1,6)]=Fraction(2)
    sc[(0,7,7)]=Fraction(-1); sc[(7,0,7)]=Fraction(1)
    sc[(1,7,7)]=Fraction(-1); sc[(7,1,7)]=Fraction(1)
    sc[(2,5,0)]=ONE; sc[(5,2,0)]=-ONE
    sc[(3,6,1)]=ONE; sc[(6,3,1)]=-ONE
    sc[(2,3,4)]=ONE; sc[(3,2,4)]=-ONE
    sc[(6,5,7)]=ONE; sc[(5,6,7)]=-ONE
    sc[(2,7,6)]=-ONE; sc[(7,2,6)]=ONE
    sc[(3,7,5)]=ONE; sc[(7,3,5)]=-ONE
    sc[(4,5,3)]=-ONE; sc[(5,4,3)]=ONE
    sc[(4,6,2)]=ONE; sc[(6,4,2)]=-ONE
    sc[(4,7,0)]=ONE; sc[(7,4,0)]=-ONE
    sc[(4,7,1)]=ONE; sc[(7,4,1)]=-ONE
    return d, sc

# ========================================
# NBC basis and Arnold reduction
# ========================================

def nbc_basis(n, k):
    """NBC basis for OS^k(n), vertices labeled 1..n."""
    if k == 0:
        return [()]
    if n <= 1 or k >= n:
        return [] if k > 0 else [()]
    edges = [(i,j) for i in range(1, n+1) for j in range(i+1, n+1)]
    broken_circuits = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for kk in range(j+1, n+1):
                broken_circuits.append(((i,j), (i,kk)))
    basis = []
    for subset in combinations(edges, k):
        s = set(subset)
        if all(not (bc[0] in s and bc[1] in s) for bc in broken_circuits):
            basis.append(tuple(sorted(subset)))
    return basis

def arnold_reduce(edges, sign, n, basis_index):
    """Reduce monomial to NBC basis using Arnold relations."""
    result = {}
    queue = [(sign, tuple(sorted(edges)))]
    for _ in range(5000):
        if not queue:
            break
        s, es = queue.pop()
        if s == ZERO or len(set(es)) < len(es):
            continue
        es = tuple(sorted(es))
        if es in basis_index:
            result[basis_index[es]] = result.get(basis_index[es], ZERO) + s
            continue
        done = False
        for pa in range(len(es)):
            for pb in range(pa+1, len(es)):
                if es[pa][0] == es[pb][0]:
                    i, j, kk = es[pa][0], es[pa][1], es[pb][1]
                    jk = (min(j,kk), max(j,kk))
                    rest = [es[l] for l in range(len(es)) if l != pa and l != pb]
                    move_sign = (-ONE)**(pb - pa - 1)
                    queue.append((s * move_sign, tuple([es[pa], jk] + rest)))
                    queue.append((-s * move_sign, tuple([es[pb], jk] + rest)))
                    done = True
                    break
            if done:
                break
        if not done and es not in basis_index:
            print(f"  WARNING: {es} not reducible")
    return result

# ========================================
# OS contraction
# ========================================

def os_contraction(n_pts, k_form, pq, src_basis, tgt_basis, tgt_index):
    """C_{pq}: OS^k(n) → OS^{k-1}(n-1). Returns sparse dict."""
    p, q = pq  # p < q
    entries = {}

    def relabel(v):
        """After merging p,q → p, removing q."""
        if v == q: return p
        if v > q: return v - 1
        return v

    for col, src_e in enumerate(src_basis):
        if pq not in src_e:
            continue
        pos = list(src_e).index(pq)
        sign = (-ONE)**pos
        remaining = [src_e[l] for l in range(len(src_e)) if l != pos]
        relabeled = []
        valid = True
        for e in remaining:
            a, b = relabel(e[0]), relabel(e[1])
            if a == b:
                valid = False; break
            relabeled.append((min(a,b), max(a,b)))
        if not valid:
            continue
        if not relabeled:
            if () in tgt_index:
                entries[(tgt_index[()], col)] = entries.get((tgt_index[()], col), ZERO) + sign
        else:
            coeffs = arnold_reduce(relabeled, sign, n_pts - 1, tgt_index)
            for idx, c in coeffs.items():
                if c != ZERO:
                    key = (idx, col)
                    entries[key] = entries.get(key, ZERO) + c
    return entries

# ========================================
# Bar differential with parametric signs and merge convention
# ========================================

def build_differential(dim_g, sc, n_src, sign_fn, merge_convention='lower'):
    """
    d: B^n → B^{n-1} where B^n = g^{⊗n} ⊗ OS^{n-1}(n).

    sign_fn(i, j, n): sign for pair (i,j) in B^n differential
    merge_convention:
      'lower' - result at position i, remove j
      'upper' - result at position j, remove i
    """
    n = n_src
    if n <= 1:
        return {}, dim_g**(n-1) if n > 0 else 1, dim_g**n

    # OS bases
    os_src = nbc_basis(n, n-1)        # OS^{n-1}(n)
    os_tgt = nbc_basis(n-1, n-2)      # OS^{n-2}(n-1)
    os_tgt_idx = {b: i for i, b in enumerate(os_tgt)}
    dim_os_src = len(os_src)
    dim_os_tgt = len(os_tgt)

    dim_src = dim_g**n * dim_os_src
    dim_tgt = dim_g**(n-1) * dim_os_tgt

    print(f"  d: B^{n} ({dim_src}) -> B^{n-1} ({dim_tgt})")

    # Precompute bracket: bracket[a][b] = [(c, val), ...]
    bracket = [[[] for _ in range(dim_g)] for _ in range(dim_g)]
    for a in range(dim_g):
        for b in range(dim_g):
            for c in range(dim_g):
                v = sc.get((a, b, c), ZERO)
                if v != ZERO:
                    bracket[a][b].append((c, v))

    # Precompute OS contractions
    contraction = {}
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            contraction[(i,j)] = os_contraction(n, n-1, (i,j), os_src, os_tgt, os_tgt_idx)

    # Build matrix
    mat = {}
    for src_config in iterproduct(range(dim_g), repeat=n):
        for os_s in range(dim_os_src):
            src_idx = 0
            for a in src_config:
                src_idx = src_idx * dim_g + a
            src_idx = src_idx * dim_os_src + os_s

            for i in range(1, n+1):
                for j in range(i+1, n+1):
                    a_i = src_config[i-1]
                    a_j = src_config[j-1]
                    bterms = bracket[a_i][a_j]
                    if not bterms:
                        continue

                    C = contraction[(i,j)]

                    for os_t in range(dim_os_tgt):
                        c_val = C.get((os_t, os_s), ZERO)
                        if c_val == ZERO:
                            continue

                        for bres, bcoeff in bterms:
                            # Build target config
                            tgt_list = list(src_config)
                            if merge_convention == 'lower':
                                tgt_list[i-1] = bres
                                del tgt_list[j-1]
                            else:  # 'upper'
                                tgt_list[j-1] = bres
                                del tgt_list[i-1]

                            tgt_idx = 0
                            for a in tgt_list:
                                tgt_idx = tgt_idx * dim_g + a
                            tgt_idx = tgt_idx * dim_os_tgt + os_t

                            sgn = sign_fn(i, j, n)
                            val = sgn * bcoeff * c_val
                            key = (tgt_idx, src_idx)
                            mat[key] = mat.get(key, ZERO) + val

    mat = {k: v for k, v in mat.items() if v != ZERO}
    return mat, dim_tgt, dim_src

# ========================================
# Sparse matrix tools
# ========================================

def sparse_mul(A, B):
    """Multiply sparse matrices."""
    result = {}
    B_by_row = {}
    for (r, c), v in B.items():
        if v != ZERO:
            B_by_row.setdefault(r, []).append((c, v))
    for (i, k), a_val in A.items():
        if a_val == ZERO or k not in B_by_row:
            continue
        for (j, b_val) in B_by_row[k]:
            key = (i, j)
            result[key] = result.get(key, ZERO) + a_val * b_val
    return {k: v for k, v in result.items() if v != ZERO}

def sparse_rank(mat, nrows, ncols):
    """Exact rank via Gaussian elimination."""
    rows = {}
    for (i, j), v in mat.items():
        if v != ZERO:
            rows.setdefault(i, {})[j] = v
    rank = 0
    pivot_cols = {}
    for col in sorted(set(j for r in rows.values() for j in r)):
        pivot_row = None
        for r in sorted(rows.keys()):
            if col in rows.get(r, {}) and rows[r][col] != ZERO and r not in pivot_cols.values():
                pivot_row = r
                break
        if pivot_row is None:
            continue
        pivot_cols[col] = pivot_row
        rank += 1
        pv = rows[pivot_row][col]
        for r in list(rows.keys()):
            if r == pivot_row:
                continue
            if col in rows.get(r, {}) and rows[r][col] != ZERO:
                f = rows[r][col] / pv
                for c, v in rows[pivot_row].items():
                    rows[r][c] = rows[r].get(c, ZERO) - f * v
                rows[r] = {c: v for c, v in rows[r].items() if v != ZERO}
                if not rows[r]:
                    del rows[r]
    return rank

# ========================================
# Sign conventions to try
# ========================================

SIGN_CONVENTIONS = {
    'none':     lambda i, j, n: ONE,
    'ij':       lambda i, j, n: (-ONE)**(i+j),
    'ij1':      lambda i, j, n: (-ONE)**(i+j+1),
    'ji1':      lambda i, j, n: (-ONE)**(j-i-1),
    'ji':       lambda i, j, n: (-ONE)**(j-i),
    'i1':       lambda i, j, n: (-ONE)**(i-1),
    'j':        lambda i, j, n: (-ONE)**(j),
    'i':        lambda i, j, n: (-ONE)**(i),
}

# ========================================
# Main
# ========================================

def test_signs(algebra='sl2', max_deg=3):
    if algebra == 'sl2':
        d, sc = sl2_data()
    else:
        d, sc = sl3_data()

    print(f"=== Testing sign conventions for {algebra} (dim={d}) ===\n")

    for merge_conv in ['lower', 'upper']:
        for sign_name, sign_fn in SIGN_CONVENTIONS.items():
            print(f"merge={merge_conv}, sign={sign_name}:")

            diffs = {}
            dims = {}
            ok = True

            for n in range(2, max_deg + 1):
                mat, dt, ds = build_differential(d, sc, n, sign_fn, merge_conv)
                diffs[n] = mat
                dims[n] = (dt, ds)

            mat1, dt1, ds1 = build_differential(d, sc, 1, sign_fn, merge_conv)
            # d1 is trivial: B^1 = g → B^0 = ? (but B^0 = 1 for bar construction)
            # Actually d1: B^1 → B^0. B^0 = g^0 · OS^{-1}(0) which doesn't make sense.
            # Let me skip d1 for now and check d2∘d3 = 0.

            for n in range(3, max_deg + 1):
                if n in diffs and (n-1) in diffs:
                    d2 = sparse_mul(diffs[n-1], diffs[n])
                    max_val = max((abs(v) for v in d2.values()), default=ZERO)
                    if max_val != ZERO:
                        print(f"  d_{n-1}∘d_{n}: FAILED (max={max_val})")
                        ok = False
                    else:
                        print(f"  d_{n-1}∘d_{n}: OK")

            if ok:
                print(f"  >>> ALL d²=0 checks passed! <<<")
            print()

def compute_cohomology(algebra='sl2', max_deg=5, sign_name='ij', merge_conv='lower'):
    if algebra == 'sl2':
        d, sc = sl2_data()
    elif algebra == 'sl3':
        d, sc = sl3_data()

    sign_fn = SIGN_CONVENTIONS[sign_name]

    print(f"Algebra: {algebra}, dim={d}, sign={sign_name}, merge={merge_conv}")
    print(f"Bar complex dimensions (B^n = g^n · (n-1)!):")

    b_dims = {}
    for n in range(1, max_deg + 1):
        dim_os = factorial(n-1) if n >= 1 else 1
        b_dims[n] = d**n * dim_os
        print(f"  B^{n} = {d}^{n} · {dim_os} = {b_dims[n]}")

    print(f"\nBuilding differentials...")
    diffs = {}
    diff_dims = {}
    for n in range(2, max_deg + 1):
        t0 = time.time()
        mat, dt, ds = build_differential(d, sc, n, sign_fn, merge_conv)
        diffs[n] = mat
        diff_dims[n] = (dt, ds)
        print(f"  d_{n}: {len(mat)} nonzero entries ({time.time()-t0:.1f}s)")

    # Check d²=0
    print(f"\nVerifying d²=0...")
    for n in range(3, max_deg + 1):
        t0 = time.time()
        d2 = sparse_mul(diffs[n-1], diffs[n])
        mx = max((abs(v) for v in d2.values()), default=ZERO)
        print(f"  d_{n-1}∘d_{n}: {'OK' if mx==ZERO else f'FAIL (max={mx})'} ({time.time()-t0:.1f}s)")

    # Compute ranks
    print(f"\nComputing ranks...")
    ranks = {}
    for n in range(2, max_deg + 1):
        t0 = time.time()
        r = sparse_rank(diffs[n], diff_dims[n][0], diff_dims[n][1])
        ranks[n] = r
        print(f"  rank(d_{n}) = {r} ({time.time()-t0:.1f}s)")

    # Homology: H^n = dim(B^n) - rank(d_n) - rank(d_{n+1})
    # Note: d_n: B^n → B^{n-1}, so ker(d_n) = dim(B^n) - rank(d_n)
    # and im(d_{n+1}) ⊆ ker(d_n) has rank = rank(d_{n+1}).
    print(f"\nBar cohomology dimensions:")
    for n in range(2, max_deg):
        ker = b_dims[n] - ranks.get(n, 0)
        im = ranks.get(n+1, 0)
        h_n = ker - im
        print(f"  H^{n} = {b_dims[n]} - {ranks.get(n,0)} - {ranks.get(n+1,0)} = {h_n}")

    if algebra == 'sl2':
        riordan = [1, 0, 1, 1, 3, 6, 15, 36, 91, 239, 628]
        print(f"\nExpected (Riordan R(n+3)): {[riordan[n+3] for n in range(2, min(max_deg, len(riordan)-3))]}")

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'

    if mode == 'test':
        test_signs('sl2', 3)
    elif mode == 'compute':
        alg = sys.argv[2] if len(sys.argv) > 2 else 'sl2'
        deg = int(sys.argv[3]) if len(sys.argv) > 3 else 5
        sign = sys.argv[4] if len(sys.argv) > 4 else 'ij'
        merge = sys.argv[5] if len(sys.argv) > 5 else 'lower'
        compute_cohomology(alg, deg, sign, merge)
