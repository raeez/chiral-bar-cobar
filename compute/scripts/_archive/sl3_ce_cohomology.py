#!/usr/bin/env python3
"""Compute Chevalley-Eilenberg cohomology of sl_3 via explicit linear algebra.

This validates the sign convention for the bar differential by checking d²=0
on the exterior algebra model (classical CE complex).

H*(sl_3, C) = Λ(x_3, x_5) — exterior algebra on generators in degrees 3 and 5.
Dimensions: 1, 0, 0, 1, 0, 1, 0, 0, 1.
"""

import numpy as np
from itertools import combinations
from math import comb

# ================================================================
# sl_3 structure constants (same as sl3_bar_cohomology.py)
# ================================================================
DIM = 8
NAMES = ['H1', 'H2', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']

# Build structure constants [a,b] = sum_c f[a][b][c] * e_c
f = np.zeros((DIM, DIM, DIM), dtype=np.float64)

A = np.array([[2, -1], [-1, 2]])  # Cartan matrix A2

# [Hi, Ej] = A_{ij} Ej
for i in range(2):
    for j in range(2):
        f[i][2+j][2+j] = A[i][j]

# [Hi, E3]
f[0][4][4] = 1; f[1][4][4] = 1

# [Hi, Fj] = -A_{ij} Fj
for i in range(2):
    for j in range(2):
        f[i][5+j][5+j] = -A[i][j]

# [Hi, F3]
f[0][7][7] = -1; f[1][7][7] = -1

# [Ei, Fi] = Hi
f[2][5][0] = 1; f[3][6][1] = 1

# [E1, E2] = E3
f[2][3][4] = 1

# [F2, F1] = F3
f[6][5][7] = 1

# [E3, F1] = -E2
f[4][5][3] = -1

# [E3, F2] = E1
f[4][6][2] = 1

# [E3, F3] = H1 + H2
f[4][7][0] = 1; f[4][7][1] = 1

# [E1, F3] = -F2
f[2][7][6] = -1

# [E2, F3] = F1
f[3][7][5] = 1

# Antisymmetrize
for a in range(DIM):
    for b in range(a+1, DIM):
        for c in range(DIM):
            if f[a][b][c] != 0 and f[b][a][c] == 0:
                f[b][a][c] = -f[a][b][c]
            elif f[b][a][c] != 0 and f[a][b][c] == 0:
                f[a][b][c] = -f[b][a][c]

# Verify
for a in range(DIM):
    for b in range(DIM):
        for c in range(DIM):
            assert abs(f[a][b][c] + f[b][a][c]) < 1e-10, \
                f"Antisymmetry fail: [{NAMES[a]},{NAMES[b]}]->{NAMES[c]}"

# Verify Jacobi
for a in range(DIM):
    for b in range(DIM):
        for c in range(DIM):
            jac = np.zeros(DIM)
            for d in range(DIM):
                jac += f[b][c][d] * f[a][d]
                jac += f[c][a][d] * f[b][d]
                jac += f[a][b][d] * f[c][d]
            assert np.max(np.abs(jac)) < 1e-10, \
                f"Jacobi fail: ({NAMES[a]},{NAMES[b]},{NAMES[c]})"

print("Structure constants: antisymmetry OK, Jacobi OK")


# ================================================================
# CE differential on Λ^n(g) → Λ^{n-1}(g)
# ================================================================
# Basis for Λ^n(g): sorted tuples of n elements from {0,...,7}
# CE differential: d(e_{i1} ∧ ... ∧ e_{in}) =
#   Σ_{s<t} (-1)^{s+t+1} [e_{is}, e_{it}] ∧ e_{i1} ∧ ... ∧ ê_{is} ∧ ... ∧ ê_{it} ∧ ... ∧ e_{in}

def exterior_basis(n):
    """Sorted n-element subsets of {0,...,DIM-1}."""
    return list(combinations(range(DIM), n))


def wedge_insert(result_gen, remaining, n_minus_1):
    """Insert result_gen into the sorted tuple 'remaining'.
    Returns (sorted_tuple, sign) or None if result_gen is already in remaining."""
    if result_gen in remaining:
        return None  # degenerate
    lst = list(remaining) + [result_gen]
    # Bubble sort to count transpositions
    arr = lst[:]
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return tuple(arr), (-1)**swaps


def ce_differential_matrix(n):
    """Build matrix for d: Λ^n(g) → Λ^{n-1}(g)."""
    if n <= 1:
        return np.zeros((1, max(1, comb(DIM, n))))

    basis_n = exterior_basis(n)
    basis_nm1 = exterior_basis(n - 1)

    idx_map = {b: i for i, b in enumerate(basis_nm1)}

    M = np.zeros((len(basis_nm1), len(basis_n)), dtype=np.float64)

    for col, elem in enumerate(basis_n):
        # elem = (i_1, ..., i_n) sorted
        for s in range(n):
            for t in range(s+1, n):
                a, b_idx = elem[s], elem[t]
                sign_st = (-1)**(s + t + 1)

                # Remaining indices after removing positions s and t
                remaining = tuple(elem[r] for r in range(n) if r != s and r != t)

                # [e_a, e_b] = sum_c f[a][b][c] * e_c
                for c in range(DIM):
                    coeff = f[a][b_idx][c]
                    if abs(coeff) < 1e-10:
                        continue

                    result = wedge_insert(c, remaining, n - 1)
                    if result is None:
                        continue  # c already in remaining
                    sorted_tuple, wedge_sign = result

                    if sorted_tuple in idx_map:
                        row = idx_map[sorted_tuple]
                        M[row, col] += sign_st * coeff * wedge_sign

    return M


# ================================================================
# Compute and verify
# ================================================================
print("\nCE complex dimensions:")
for n in range(DIM + 1):
    print(f"  Λ^{n}(sl_3): dim = {comb(DIM, n)}")

# Build all differentials
diffs = {}
for n in range(1, DIM + 1):
    diffs[n] = ce_differential_matrix(n)
    print(f"  d_{n}: Λ^{n} -> Λ^{n-1}, matrix shape {diffs[n].shape}")

# Verify d² = 0
print("\nVerifying d² = 0:")
for n in range(2, DIM + 1):
    d_comp = diffs[n-1] @ diffs[n]
    max_err = np.max(np.abs(d_comp))
    status = "PASS" if max_err < 1e-8 else f"FAIL (max={max_err:.2e})"
    print(f"  d_{n-1} ∘ d_{n}: {status}")

# Compute cohomology
print("\nCE cohomology H^n(sl_3, C):")
expected = [1, 0, 0, 1, 0, 1, 0, 0, 1]
all_ok = True
for n in range(DIM + 1):
    if n == 0:
        # H^0 = ker(d_1)
        ker_dim = comb(DIM, 0)  # d_0 doesn't exist, so ker = all
        im_dim = 0
    else:
        chain_dim = comb(DIM, n)
        if n in diffs:
            rank_out = np.linalg.matrix_rank(diffs[n], tol=1e-8)
            ker_dim = chain_dim - rank_out
        else:
            ker_dim = chain_dim

        if n + 1 in diffs:
            rank_in = np.linalg.matrix_rank(diffs[n+1], tol=1e-8)
        else:
            rank_in = 0

        im_dim = rank_in

    h_n = ker_dim - im_dim
    exp = expected[n] if n < len(expected) else 0
    match = "OK" if h_n == exp else "MISMATCH"
    if h_n != exp:
        all_ok = False
    print(f"  H^{n} = {h_n}  (expected: {exp})  {match}")

if all_ok:
    print("\nAll CE cohomology dimensions match! Sign convention is correct.")
    print("Now applying same sign to the OS-tensor bar complex...")
else:
    print("\nSome dimensions don't match. Check structure constants or sign convention.")
