#!/usr/bin/env python3
"""Find correct bar differential: try all combinations of signs and conventions."""
import sys
sys.path.insert(0, 'compute/lib')
import numpy as np
from bar_differential import (sl2_structure_constants, verify_jacobi,
                               os_top_basis, poincare_residue_matrix,
                               _express_in_nbc_basis)
from itertools import product as iter_product


def bar_diff_general(dim_g, sc, n, sign_fn, bracket_order='ij', merge_pos='i'):
    """General bar differential with configurable conventions.

    bracket_order: 'ij' for [a_i, a_j], 'ji' for [a_j, a_i]
    merge_pos: 'i' puts result at position i, 'j' puts result at position j
    """
    if n <= 2:
        src_d = dim_g ** n * max(1, len(os_top_basis(n)))
        tgt_d = dim_g ** max(n-1, 1) * max(1, len(os_top_basis(max(n-1, 1))))
        if n <= 1:
            return np.zeros((dim_g if n == 1 else 1, src_d))
        return np.zeros((tgt_d, src_d))

    source_os = os_top_basis(n)
    target_os = os_top_basis(n - 1)
    sos = len(source_os)
    tos = len(target_os)
    sdim = dim_g ** n * sos
    tdim = dim_g ** (n - 1) * tos

    res_matrices = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            res_matrices[(i, j)] = poincare_residue_matrix(n, i, j)

    M = np.zeros((tdim, sdim))

    for gen_idx in range(dim_g ** n):
        gens = []
        temp = gen_idx
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g
        gens = list(reversed(gens))

        for os_s in range(sos):
            src_idx = gen_idx * sos + os_s

            for i in range(1, n + 1):
                for j in range(i + 1, n + 1):
                    a_i = gens[i - 1]
                    a_j = gens[j - 1]

                    res_M = res_matrices[(i, j)]

                    for os_t in range(tos):
                        rc = res_M[os_t, os_s]
                        if abs(rc) < 1e-10:
                            continue

                        # Bracket
                        if bracket_order == 'ij':
                            for c in range(dim_g):
                                bc = sc[a_i, a_j, c]
                                if abs(bc) < 1e-10:
                                    continue
                                _add_term(M, dim_g, gens, n, i, j, c, os_t, tos,
                                         sign_fn(i, j, n) * bc * rc, merge_pos)
                        else:  # 'ji'
                            for c in range(dim_g):
                                bc = sc[a_j, a_i, c]
                                if abs(bc) < 1e-10:
                                    continue
                                _add_term(M, dim_g, gens, n, i, j, c, os_t, tos,
                                         sign_fn(i, j, n) * bc * rc, merge_pos)
    return M


def _add_term(M, dim_g, gens, n, i, j, c, os_t, tos, coeff, merge_pos):
    target_gens = []
    if merge_pos == 'i':
        for k in range(n):
            if k == i - 1:
                target_gens.append(c)
            elif k == j - 1:
                continue
            else:
                target_gens.append(gens[k])
    else:  # merge_pos == 'j'
        for k in range(n):
            if k == i - 1:
                continue
            elif k == j - 1:
                target_gens.append(c)
            else:
                target_gens.append(gens[k])

    tgi = 0
    for g in target_gens:
        tgi = tgi * dim_g + g
    tidx = tgi * tos + os_t
    M[tidx, M.shape[1] - 1 - (M.shape[1] - 1)] = M[tidx, M.shape[1] - 1 - (M.shape[1] - 1)]  # dummy
    # Actually need src_idx passed in. Let me fix this.


# Simpler approach: just modify the existing code minimally
def build_d(dim_g, sc, n, extra_sign, merge_at_j=False):
    """Build d_n with extra_sign(i,j,n) multiplied in, optionally merging at j."""
    if n <= 2:
        if n == 2:
            return np.zeros((dim_g, dim_g**2))
        return np.zeros((1, dim_g))

    source_os = os_top_basis(n)
    target_os = os_top_basis(n - 1)
    sos = len(source_os)
    tos = len(target_os)
    sdim = dim_g ** n * sos
    tdim = dim_g ** (n - 1) * tos

    res_mats = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            res_mats[(i, j)] = poincare_residue_matrix(n, i, j)

    M = np.zeros((tdim, sdim))

    for gen_idx in range(dim_g ** n):
        gens = []
        temp = gen_idx
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g
        gens = list(reversed(gens))

        for os_s in range(sos):
            src = gen_idx * sos + os_s

            for i in range(1, n + 1):
                for j in range(i + 1, n + 1):
                    rm = res_mats[(i, j)]
                    for os_t in range(tos):
                        rc = rm[os_t, os_s]
                        if abs(rc) < 1e-10:
                            continue

                        a_i, a_j = gens[i-1], gens[j-1]
                        for c in range(dim_g):
                            bc = sc[a_i, a_j, c]
                            if abs(bc) < 1e-10:
                                continue

                            tgens = []
                            if not merge_at_j:
                                for k in range(n):
                                    if k == i-1: tgens.append(c)
                                    elif k == j-1: continue
                                    else: tgens.append(gens[k])
                            else:
                                for k in range(n):
                                    if k == i-1: continue
                                    elif k == j-1: tgens.append(c)
                                    else: tgens.append(gens[k])

                            tgi = 0
                            for g in tgens:
                                tgi = tgi * dim_g + g
                            tgt = tgi * tos + os_t

                            sgn = extra_sign(i, j, n)
                            M[tgt, src] += sgn * bc * rc

    return M


def check(dim_g, sc, sign_fn, merge_j=False, n=4):
    d_n = build_d(dim_g, sc, n, sign_fn, merge_j)
    d_nm1 = build_d(dim_g, sc, n-1, sign_fn, merge_j)
    prod = d_nm1 @ d_n
    return np.max(np.abs(prod)) < 1e-8


if __name__ == '__main__':
    names, sc = sl2_structure_constants()
    assert verify_jacobi(names, sc)
    d = len(names)
    print(f"sl₂, dim={d}")

    # Test combinations
    signs = {
        '1': lambda i,j,n: 1,
        '(-1)^(i-1)': lambda i,j,n: (-1)**(i-1),
        '(-1)^i': lambda i,j,n: (-1)**i,
        '(-1)^(j-1)': lambda i,j,n: (-1)**(j-1),
        '(-1)^j': lambda i,j,n: (-1)**j,
        '(-1)^(i+j)': lambda i,j,n: (-1)**(i+j),
        '(-1)^(i+j+1)': lambda i,j,n: (-1)**(i+j+1),
        '(-1)^(j-i-1)': lambda i,j,n: (-1)**(j-i-1),
        '(-1)^(j-i)': lambda i,j,n: (-1)**(j-i),
        '(-1)^(i*j)': lambda i,j,n: (-1)**(i*j),
        '(-1)^((i-1)*(j-1))': lambda i,j,n: (-1)**((i-1)*(j-1)),
        '(-1)^(n-j)': lambda i,j,n: (-1)**(n-j),
        '(-1)^(n-i)': lambda i,j,n: (-1)**(n-i),
        '(-1)^(i+j+n)': lambda i,j,n: (-1)**(i+j+n),
    }

    print("\nTesting d₃∘d₄ = 0:\n")
    for sname, sfn in signs.items():
        for mj in [False, True]:
            ok = check(d, sc, sfn, mj)
            if ok:
                mstr = "merge@j" if mj else "merge@i"
                print(f"  ✓ sign={sname:25s} {mstr}")

    # Also try: no extra sign, but reverse the bracket in the structure constants
    print("\n--- With reversed bracket [a_j, a_i] (=negate sc) ---\n")
    sc_neg = -sc  # [a_j, a_i] = -[a_i, a_j]
    for sname, sfn in signs.items():
        for mj in [False, True]:
            ok = check(d, sc_neg, sfn, mj)
            if ok:
                mstr = "merge@j" if mj else "merge@i"
                print(f"  ✓ sign={sname:25s} {mstr} (reversed bracket)")
