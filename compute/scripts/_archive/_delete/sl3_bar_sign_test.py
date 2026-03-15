#!/usr/bin/env python3
"""Test different sign conventions for the tensor-OS bar differential.

Try all reasonable sign candidates for ε_{ij} and check d²=0.
"""

import numpy as np
from itertools import product as iproduct, combinations
from collections import defaultdict

# ================================================================
# sl_3 structure constants (verified)
# ================================================================
DIM = 8
f = np.zeros((DIM, DIM, DIM), dtype=np.float64)
A = np.array([[2, -1], [-1, 2]])

for i in range(2):
    for j in range(2):
        f[i][2+j][2+j] = A[i][j]
f[0][4][4] = 1; f[1][4][4] = 1
for i in range(2):
    for j in range(2):
        f[i][5+j][5+j] = -A[i][j]
f[0][7][7] = -1; f[1][7][7] = -1
f[2][5][0] = 1; f[3][6][1] = 1
f[2][3][4] = 1; f[6][5][7] = 1
f[4][5][3] = -1; f[4][6][2] = 1
f[4][7][0] = 1; f[4][7][1] = 1
f[2][7][6] = -1; f[3][7][5] = 1

for a in range(DIM):
    for b in range(a+1, DIM):
        for c in range(DIM):
            if f[a][b][c] != 0 and f[b][a][c] == 0:
                f[b][a][c] = -f[a][b][c]
            elif f[b][a][c] != 0 and f[a][b][c] == 0:
                f[a][b][c] = -f[b][a][c]

# ================================================================
# Minimal OS algebra and residue (for small n)
# ================================================================
def os_basis(n):
    if n <= 1:
        return [()]
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    broken_circuits = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                broken_circuits.append(frozenset({(i,j), (i,k)}))
    basis = []
    for subset in combinations(edges, n-1):
        subset_set = frozenset(subset)
        if not any(bc.issubset(subset_set) for bc in broken_circuits):
            basis.append(tuple(sorted(subset)))
    return basis

def _relabel_edge(e, i, j):
    hi, lo = max(i, j), min(i, j)
    a, b = e
    def remap(p):
        if p == i or p == j: return lo
        elif p > hi: return p - 1
        else: return p
    a2, b2 = remap(a), remap(b)
    if a2 == b2: return None
    return (min(a2, b2), max(a2, b2))

def _sort_with_sign(edges):
    arr = list(edges)
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return tuple(arr), (-1)**swaps

def _express_in_nbc(form_edges, n, basis, depth=0):
    if depth > 20: return {}
    if form_edges in basis: return {basis.index(form_edges): 1.0}
    if len(set(form_edges)) < len(form_edges): return {}
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                bc = ((i,j), (i,k))
                if bc[0] in form_edges and bc[1] in form_edges:
                    pos_ij = form_edges.index(bc[0])
                    pos_ik = form_edges.index(bc[1])
                    missing = (j, k)
                    new1 = list(form_edges); new1[pos_ik] = missing
                    s1, sign1 = _sort_with_sign(new1)
                    new2 = list(form_edges); new2[pos_ij] = missing
                    s2, sign2 = _sort_with_sign(new2)
                    result = {}
                    for idx, v in _express_in_nbc(s1, n, basis, depth+1).items():
                        result[idx] = result.get(idx, 0) + sign1 * v
                    for idx, v in _express_in_nbc(s2, n, basis, depth+1).items():
                        result[idx] = result.get(idx, 0) - sign2 * v
                    return {k: v for k, v in result.items() if abs(v) > 1e-10}
    return {}

def compute_residue_matrices(n):
    basis_n = os_basis(n)
    basis_nm1 = os_basis(n - 1)
    matrices = {}
    for i in range(n):
        for j in range(i+1, n):
            M = np.zeros((len(basis_nm1), len(basis_n)), dtype=np.float64)
            for col, form in enumerate(basis_n):
                if (i,j) not in form: continue
                pos = form.index((i,j))
                sign = (-1) ** pos
                remaining = list(form[:pos]) + list(form[pos+1:])
                relabeled = []
                ok = True
                for e in remaining:
                    e2 = _relabel_edge(e, i, j)
                    if e2 is None: ok = False; break
                    relabeled.append(e2)
                if not ok: continue
                sorted_rel, sort_sign = _sort_with_sign(relabeled)
                coeffs = _express_in_nbc(sorted_rel, n - 1, basis_nm1)
                for row, v in coeffs.items():
                    M[row, col] += sign * sort_sign * v
            matrices[(i, j)] = M
    return matrices


# ================================================================
# Build bar differential with parameterized sign
# ================================================================
def bar_diff_matrix(n, sign_func):
    """Build the full bar differential d: g^n ⊗ OS^{n-1} → g^{n-1} ⊗ OS^{n-2}.

    sign_func(i, j, n) returns the sign for the (i,j) pair.
    Only uses weight (0,0) block for speed (Cartan subalgebra tensors).
    """
    # Use a small subset: just sl_2 subalgebra (H1, E1, F1) = indices 0, 2, 5
    # Actually, use full sl_3 but restrict to low degree for speed

    os_n = os_basis(n)
    os_nm1 = os_basis(n - 1)
    res_mats = compute_residue_matrices(n)

    dim_lie_n = DIM ** n
    dim_lie_nm1 = DIM ** (n - 1)
    dim_total_n = dim_lie_n * len(os_n)
    dim_total_nm1 = dim_lie_nm1 * len(os_nm1)

    # Index a lie tuple by its multi-index
    def lie_index(tup):
        idx = 0
        for k, t in enumerate(tup):
            idx = idx * DIM + t
        return idx

    M = np.zeros((dim_total_nm1, dim_total_n), dtype=np.float64)

    for lie_tuple in iproduct(range(DIM), repeat=n):
        col_lie = lie_index(lie_tuple)

        for i in range(n):
            for j in range(i+1, n):
                a_i, a_j = lie_tuple[i], lie_tuple[j]
                res_mat = res_mats[(i, j)]
                sign = sign_func(i, j, n)

                for c in range(DIM):
                    coeff = f[a_i][a_j][c]
                    if abs(coeff) < 1e-10: continue

                    # Replace j with c, remove i
                    new_list = list(lie_tuple)
                    new_list[j] = c
                    new_tuple = tuple(new_list[:i] + new_list[i+1:])
                    row_lie = lie_index(new_tuple)

                    for col_f in range(len(os_n)):
                        for row_f in range(len(os_nm1)):
                            if abs(res_mat[row_f, col_f]) < 1e-10: continue
                            col = col_lie * len(os_n) + col_f
                            row = row_lie * len(os_nm1) + row_f
                            M[row, col] += sign * coeff * res_mat[row_f, col_f]

    return M


# ================================================================
# Test sign conventions
# ================================================================
print("Testing sign conventions for d²=0 on tensor-OS bar complex")
print(f"(Using full sl_3, degrees 2 and 3)\n")

sign_candidates = {
    "(-1)^i":          lambda i, j, n: (-1)**i,
    "(-1)^j":          lambda i, j, n: (-1)**j,
    "(-1)^{i+j}":     lambda i, j, n: (-1)**(i+j),
    "(-1)^{i+j+1}":   lambda i, j, n: (-1)**(i+j+1),
    "(-1)^{i+1}":     lambda i, j, n: (-1)**(i+1),
    "(-1)^{j+1}":     lambda i, j, n: (-1)**(j+1),
    "+1":              lambda i, j, n: 1,
    "-1":              lambda i, j, n: -1,
}

for name, sign_func in sign_candidates.items():
    # Build d_2 and d_3
    d2 = bar_diff_matrix(2, sign_func)
    d3 = bar_diff_matrix(3, sign_func)

    # Check d_1 ∘ d_2 (d_1 maps to vacuum, trivially 0 at nonzero weight)
    # Check d_2 ∘ d_3
    comp = d2 @ d3
    max_err = np.max(np.abs(comp))

    r2 = np.linalg.matrix_rank(d2, tol=1e-8)
    r3 = np.linalg.matrix_rank(d3, tol=1e-8)

    status = "d²=0 ✓" if max_err < 1e-8 else f"d²≠0 (max={max_err:.1e})"
    print(f"  {name:20s}: rank(d2)={r2:4d}, rank(d3)={r3:4d}, {status}")
