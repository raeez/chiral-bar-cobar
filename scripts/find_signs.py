#!/usr/bin/env python3
"""Find the correct sign convention for the bar differential by brute force.

Test all reasonable sign functions σ(i,j) for d: B_n → B_{n-1}
and check d² = 0 for sl₂ at small degrees.
"""
import sys
sys.path.insert(0, 'compute/lib')

import numpy as np
from bar_differential import (sl2_structure_constants, sl3_structure_constants,
                               verify_jacobi, os_top_basis, poincare_residue_matrix)
from itertools import product as iter_product


def bar_diff_with_sign(dim_g, sc, n, sign_fn):
    """Build d: B_n → B_{n-1} with custom sign function.

    sign_fn(i, j, n) returns the sign for pair (i,j) in the n-factor complex.
    Points labeled 1..n.
    """
    if n <= 2:
        source_os = os_top_basis(n) if n >= 1 else [()]
        target_os = os_top_basis(n - 1) if n >= 2 else [()]
        source_dim = dim_g ** n * len(source_os) if n >= 1 else 1
        target_dim = dim_g ** (n - 1) * len(target_os) if n >= 1 else 1
        return np.zeros((target_dim, source_dim))

    source_os = os_top_basis(n)
    target_os = os_top_basis(n - 1)
    source_os_dim = len(source_os)
    target_os_dim = len(target_os)
    source_dim = dim_g ** n * source_os_dim
    target_dim = dim_g ** (n - 1) * target_os_dim

    # Precompute residue matrices
    res_matrices = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            res_matrices[(i, j)] = poincare_residue_matrix(n, i, j)

    M = np.zeros((target_dim, source_dim))

    for gen_idx in range(dim_g ** n):
        gens = []
        temp = gen_idx
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g
        gens = list(reversed(gens))

        for os_s_idx in range(source_os_dim):
            source_idx = gen_idx * source_os_dim + os_s_idx

            for i in range(1, n + 1):
                for j in range(i + 1, n + 1):
                    a_i = gens[i - 1]
                    a_j = gens[j - 1]

                    res_M = res_matrices[(i, j)]

                    for os_t_idx in range(target_os_dim):
                        res_coeff = res_M[os_t_idx, os_s_idx]
                        if abs(res_coeff) < 1e-10:
                            continue

                        for c in range(dim_g):
                            bracket_coeff = sc[a_i, a_j, c]
                            if abs(bracket_coeff) < 1e-10:
                                continue

                            target_gens = []
                            for k in range(n):
                                if k == i - 1:
                                    target_gens.append(c)
                                elif k == j - 1:
                                    continue
                                else:
                                    target_gens.append(gens[k])

                            target_gen_idx = 0
                            for g in target_gens:
                                target_gen_idx = target_gen_idx * dim_g + g

                            target_idx = target_gen_idx * target_os_dim + os_t_idx

                            sgn = sign_fn(i, j, n)
                            coeff = sgn * bracket_coeff * res_coeff
                            M[target_idx, source_idx] += coeff

    return M


def check_d_squared(dim_g, sc, n, sign_fn):
    """Check if d_{n-1} ∘ d_n = 0."""
    d_n = bar_diff_with_sign(dim_g, sc, n, sign_fn)
    d_nm1 = bar_diff_with_sign(dim_g, sc, n - 1, sign_fn)
    prod = d_nm1 @ d_n
    return np.max(np.abs(prod)) < 1e-8


def compute_cohomology(dim_g, sc, max_deg, sign_fn):
    """Compute bar cohomology with given sign convention."""
    result = {1: dim_g}
    d_matrices = {}
    for deg in range(2, max_deg + 2):
        d_matrices[deg] = bar_diff_with_sign(dim_g, sc, deg, sign_fn)

    for deg in range(2, max_deg + 1):
        d_out = d_matrices[deg]
        d_in = d_matrices[deg + 1]
        rank_out = np.linalg.matrix_rank(d_out)
        rank_in = np.linalg.matrix_rank(d_in)
        chain_dim = d_out.shape[1]
        h = chain_dim - rank_out - rank_in
        result[deg] = h
    return result


# Sign conventions to test
sign_fns = {
    'none': lambda i, j, n: 1,
    '(-1)^(i-1)': lambda i, j, n: (-1) ** (i - 1),
    '(-1)^(j-1)': lambda i, j, n: (-1) ** (j - 1),
    '(-1)^(i+j)': lambda i, j, n: (-1) ** (i + j),
    '(-1)^(i+j+1)': lambda i, j, n: (-1) ** (i + j + 1),
    '(-1)^(j-i-1)': lambda i, j, n: (-1) ** (j - i - 1),
    '(-1)^(j-i)': lambda i, j, n: (-1) ** (j - i),
    '(-1)^i': lambda i, j, n: (-1) ** i,
    '(-1)^j': lambda i, j, n: (-1) ** j,
    '(-1)^(i*(j-1))': lambda i, j, n: (-1) ** (i * (j - 1)),
}


if __name__ == '__main__':
    print("Loading sl₂...")
    names, sc = sl2_structure_constants()
    assert verify_jacobi(names, sc)
    dim_g = len(names)

    print("\n=== Testing sign conventions: d₃∘d₄ = 0 for sl₂ ===\n")

    working = []
    for name, sign_fn in sign_fns.items():
        ok34 = check_d_squared(dim_g, sc, 4, sign_fn)
        ok45 = check_d_squared(dim_g, sc, 5, sign_fn)
        status = "✓" if (ok34 and ok45) else "✗"
        print(f"  {name:25s}: d₃∘d₄={ok34}, d₄∘d₅={ok45}  {status}")
        if ok34 and ok45:
            working.append((name, sign_fn))

    print(f"\n{len(working)} working conventions found.\n")

    # Compute cohomology with working conventions
    expected = {1: 3, 2: 6, 3: 15, 4: 36}

    for name, sign_fn in working:
        coh = compute_cohomology(dim_g, sc, 4, sign_fn)
        match = all(coh.get(k) == expected.get(k) for k in expected)
        print(f"  {name:25s}: H = {coh}  {'✓ MATCH' if match else '✗'}")
