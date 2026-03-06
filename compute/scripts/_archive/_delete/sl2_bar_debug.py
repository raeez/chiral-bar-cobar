#!/usr/bin/env python3
"""Debug the tensor-OS bar differential using sl_2 (dim 3).

Trace d^2 on specific elements to find the exact source of failure.
Also test whether d^2=0 on the Sn-coinvariant subspace.

sl_2 basis: H=0, E=1, F=2
[H,E]=2E, [H,F]=-2F, [E,F]=H
"""

import numpy as np
from itertools import product as iproduct

# sl_2 structure constants
DIM = 3
NAMES = ['H', 'E', 'F']
f = np.zeros((DIM, DIM, DIM))
f[0][1][1] = 2    # [H,E] = 2E
f[0][2][2] = -2   # [H,F] = -2F
f[1][2][0] = 1    # [E,F] = H
# Antisymmetrize
for a in range(DIM):
    for b in range(a+1, DIM):
        for c in range(DIM):
            if f[a][b][c] != 0:
                f[b][a][c] = -f[a][b][c]

print("sl_2 structure constants:")
for a in range(DIM):
    for b in range(a+1, DIM):
        for c in range(DIM):
            if abs(f[a][b][c]) > 1e-10:
                print(f"  [{NAMES[a]},{NAMES[b]}] has {NAMES[c]}-component = {f[a][b][c]}")

# Verify Jacobi
for a in range(DIM):
    for b in range(DIM):
        for c in range(DIM):
            jac = np.zeros(DIM)
            for d in range(DIM):
                jac += f[b][c][d] * f[a][d]
                jac += f[c][a][d] * f[b][d]
                jac += f[a][b][d] * f[c][d]
            assert np.max(np.abs(jac)) < 1e-10
print("Jacobi: OK\n")

# ================================================================
# CE complex for sl_2 (known correct)
# ================================================================
from itertools import combinations

def ce_diff(n):
    """CE differential d: Lambda^n(g) -> Lambda^{n-1}(g)."""
    if n <= 0 or n > DIM:
        return np.zeros((1, 1))
    basis_n = list(combinations(range(DIM), n))
    if n == 1:
        basis_nm1 = [()]
    else:
        basis_nm1 = list(combinations(range(DIM), n-1))

    idx = {b: i for i, b in enumerate(basis_nm1)}
    M = np.zeros((len(basis_nm1), len(basis_n)))

    for col, elem in enumerate(basis_n):
        for s in range(n):
            for t in range(s+1, n):
                sign_st = (-1)**(s + t + 1)
                remaining = tuple(elem[r] for r in range(n) if r != s and r != t)
                for c in range(DIM):
                    coeff = f[elem[s]][elem[t]][c]
                    if abs(coeff) < 1e-10:
                        continue
                    if n == 2:
                        # remaining is empty, result is just (c,)
                        target = (c,)
                    else:
                        if c in remaining:
                            continue  # degenerate
                        lst = list(remaining) + [c]
                        arr = lst[:]
                        swaps = 0
                        for i in range(len(arr)):
                            for j in range(len(arr)-1-i):
                                if arr[j] > arr[j+1]:
                                    arr[j], arr[j+1] = arr[j+1], arr[j]
                                    swaps += 1
                        target = tuple(arr)
                        sign_st *= (-1)**swaps
                    if target in idx:
                        M[idx[target], col] += sign_st * coeff
    return M

# Verify CE
d1 = ce_diff(1)  # Lambda^1 -> Lambda^0
d2 = ce_diff(2)  # Lambda^2 -> Lambda^1
d3 = ce_diff(3)  # Lambda^3 -> Lambda^2

print("CE complex for sl_2:")
print(f"  d1: {d1.shape} (Lambda^1 -> Lambda^0)")
print(f"  d2: {d2.shape} (Lambda^2 -> Lambda^1)")
print(f"  d3: {d3.shape} (Lambda^3 -> Lambda^2)")

print(f"\n  d1 matrix:\n{d1}")
print(f"  d2 matrix:\n{d2}")
print(f"  d3 matrix:\n{d3}")

comp12 = d1 @ d2
comp23 = d2 @ d3
print(f"\n  d1 o d2: max|err| = {np.max(np.abs(comp12)):.1e}")
print(f"  d2 o d3: max|err| = {np.max(np.abs(comp23)):.1e}")

# CE cohomology
r1 = np.linalg.matrix_rank(d1)
r2 = np.linalg.matrix_rank(d2)
r3 = np.linalg.matrix_rank(d3)
print(f"\n  Ranks: r(d1)={r1}, r(d2)={r2}, r(d3)={r3}")
print(f"  H^0 = ker(d1) = {DIM - r1 - 0}")  # no d0
print(f"  H^1 = ker(d2)/im(d1) ... wait, CE goes the other direction")
# Actually for sl_2: H^*(sl_2, C) = Lambda(x_3) where x_3 is in degree 3.
# Dims: H^0=1, H^1=0, H^2=0, H^3=1.

# ================================================================
# Tensor-OS bar complex for n=2,3
# ================================================================
# n=2: B^2 = g^{otimes 2} tensor OS^1(C_2) = g^{otimes 2} (dim 9)
# OS^1(C_2) = span{w_{01}} (dim 1)
# d: B^2 -> B^1 = g (dim 3)
# d(a_0, a_1; w_{01}) = sum_c f[a_0,a_1,c] * e_c
#   (Res_{01}(w_{01}) = 1, merged point at 0)
#   Result: [a_0, a_1] at the single remaining point

# n=3: B^3 = g^{otimes 3} tensor OS^2(C_3) = g^{otimes 3} tensor C^2 (dim 27*2=54)
# OS^2(C_3) NBC basis: w_0 = (0,1)(1,2), w_1 = (0,2)(1,2) (dim 2)
# d: B^3 -> B^2 = g^{otimes 2} tensor OS^1(C_2) = g^{otimes 2} (dim 9)

# Residue maps for n=3 (verified earlier):
# Res_{01}(w_0) = +1, Res_{01}(w_1) = 0
# Res_{02}(w_0) = 0,  Res_{02}(w_1) = +1
# Res_{12}(w_0) = -1, Res_{12}(w_1) = -1

# The differential d: B^3 -> B^2:
# For element (a_0, a_1, a_2) tensor w_k:
#   d = sum_{i<j} [a_i, a_j]_c * (contraction of tensor) tensor Res_{ij}(w_k)
#
# After Res_{ij}, points merge: i,j -> i (=min(i,j)), higher points shift.
# The Lie tensor: [a_i, a_j]_c goes to the merged point (position i), position j removed.

# Let me be very explicit. For (i,j) = (0,1):
# Merge: 0,1->0; 2->1. Bracket at pos 0, a_2 at pos 1.
# Result tensor: ([a_0,a_1]_c, a_2) at positions (0,1) in the target.
# Res_{01}(w_k): see above.

# For (i,j) = (0,2):
# Merge: 0,2->0; 1->1. Bracket at pos 0, a_1 at pos 1.
# Result tensor: ([a_0,a_2]_c, a_1) at positions (0,1).
# Res_{02}(w_k): see above.

# For (i,j) = (1,2):
# Merge: 1,2->1; 0->0. Bracket at pos 1, a_0 at pos 0.
# Result tensor: (a_0, [a_1,a_2]_c) at positions (0,1).
# Res_{12}(w_k): see above.

# Sign convention: I'll try sign = +1 first and compute d^2 explicitly.

def build_d2(sign_func=None):
    """d: g^{otimes 2} -> g^{otimes 1} = g. Shape: (3, 9)."""
    if sign_func is None:
        sign_func = lambda i,j: 1

    M = np.zeros((DIM, DIM**2))
    for a0 in range(DIM):
        for a1 in range(DIM):
            col = a0 * DIM + a1
            # Only pair: (i,j)=(0,1)
            sign = sign_func(0, 1)
            for c in range(DIM):
                coeff = f[a0][a1][c]
                if abs(coeff) < 1e-10:
                    continue
                # Result: c at position 0
                M[c, col] += sign * coeff
    return M

def build_d3(sign_func=None):
    """d: g^{otimes 3} tensor OS^2(C_3) -> g^{otimes 2} tensor OS^1(C_2).
    Source dim: 27*2=54. Target dim: 9*1=9. Shape: (9, 54)."""
    if sign_func is None:
        sign_func = lambda i,j: 1

    # Residues for n=3
    # w_0 = (0,1)(1,2), w_1 = (0,2)(1,2)
    res = {
        (0,1): [1, 0],
        (0,2): [0, 1],
        (1,2): [-1, -1],
    }

    M = np.zeros((DIM**2, DIM**3 * 2))
    for a0 in range(DIM):
        for a1 in range(DIM):
            for a2 in range(DIM):
                lie_col = a0 * DIM**2 + a1 * DIM + a2
                for wk in range(2):  # OS basis index
                    col = lie_col * 2 + wk

                    # Pair (0,1): merge 0,1->0; 2->1
                    # Result: ([a0,a1]_c, a2) at (0,1)
                    r01 = res[(0,1)][wk]
                    if abs(r01) > 1e-10:
                        sign = sign_func(0, 1)
                        for c in range(DIM):
                            coeff = f[a0][a1][c]
                            if abs(coeff) < 1e-10:
                                continue
                            row = c * DIM + a2
                            M[row, col] += sign * coeff * r01

                    # Pair (0,2): merge 0,2->0; 1->1
                    # Result: ([a0,a2]_c, a1) at (0,1)
                    r02 = res[(0,2)][wk]
                    if abs(r02) > 1e-10:
                        sign = sign_func(0, 2)
                        for c in range(DIM):
                            coeff = f[a0][a2][c]
                            if abs(coeff) < 1e-10:
                                continue
                            row = c * DIM + a1
                            M[row, col] += sign * coeff * r02

                    # Pair (1,2): merge 1,2->1; 0->0
                    # Result: (a0, [a1,a2]_c) at (0,1)
                    r12 = res[(1,2)][wk]
                    if abs(r12) > 1e-10:
                        sign = sign_func(1, 2)
                        for c in range(DIM):
                            coeff = f[a1][a2][c]
                            if abs(coeff) < 1e-10:
                                continue
                            row = a0 * DIM + c
                            M[row, col] += sign * coeff * r12

    return M


print("\n" + "="*60)
print("Tensor-OS bar complex for sl_2")
print("="*60)

# Test many sign conventions
sign_options = {
    "+1":           lambda i,j: 1,
    "-1":           lambda i,j: -1,
    "(-1)^i":       lambda i,j: (-1)**i,
    "(-1)^j":       lambda i,j: (-1)**j,
    "(-1)^{i+j}":   lambda i,j: (-1)**(i+j),
    "(-1)^{i+j+1}": lambda i,j: (-1)**(i+j+1),
    "(-1)^{i+1}":   lambda i,j: (-1)**(i+1),
    "(-1)^{j+1}":   lambda i,j: (-1)**(j+1),
}

for sname, sfunc in sign_options.items():
    d2_mat = build_d2(sfunc)
    d3_mat = build_d3(sfunc)
    comp = d2_mat @ d3_mat
    err = np.max(np.abs(comp))
    r2 = np.linalg.matrix_rank(d2_mat)
    r3 = np.linalg.matrix_rank(d3_mat)
    status = "d^2=0" if err < 1e-8 else f"d^2!=0 ({err:.1e})"
    print(f"  sign={sname:15s}: rk(d2)={r2}, rk(d3)={r3}, {status}")

# ================================================================
# Detailed trace: compute d^2 on a specific element
# ================================================================
print("\n" + "="*60)
print("Trace d^2 on specific elements (sign=+1)")
print("="*60)

d2_mat = build_d2()
d3_mat = build_d3()

# Let's trace d^2(E tensor E tensor E tensor w_0)
# E=1, so (1,1,1) tensor w_0
# Index: lie_col = 1*9 + 1*3 + 1 = 13; col = 13*2 + 0 = 26

col_idx = (1 * DIM**2 + 1 * DIM + 1) * 2 + 0  # (E,E,E) tensor w_0
d3_col = d3_mat[:, col_idx]
print(f"\nd3(E⊗E⊗E⊗w_0):")
for row in range(DIM**2):
    if abs(d3_col[row]) > 1e-10:
        a = row // DIM
        b = row % DIM
        print(f"  ({NAMES[a]}⊗{NAMES[b]}) * {d3_col[row]}")

# [E,E]=0 for all pairs, so d should be 0
print("Expected: 0 (since [E,E]=0)")

# Try (H,E,F) tensor w_0
col_idx = (0 * DIM**2 + 1 * DIM + 2) * 2 + 0  # (H,E,F) tensor w_0
d3_col = d3_mat[:, col_idx]
print(f"\nd3(H⊗E⊗F⊗w_0):")
for row in range(DIM**2):
    if abs(d3_col[row]) > 1e-10:
        a = row // DIM
        b = row % DIM
        print(f"  ({NAMES[a]}⊗{NAMES[b]}) * {d3_col[row]}")

# Let's compute manually:
# Pair (0,1): [H,E]=2E. Res_{01}(w_0)=1. Result: (2E, F) = 2*(1,2)
# Pair (0,2): [H,F]=-2F. Res_{02}(w_0)=0. -> 0
# Pair (1,2): [E,F]=H. Res_{12}(w_0)=-1. Result: (H, -H) = -1*(0,0)
print("Manual: (0,1) gives 2(E⊗F); (0,2) gives 0; (1,2) gives -(H⊗H)")

# Now apply d2 to this result
d3_result = d3_col
d2d3 = d2_mat @ d3_result
print(f"\nd2(d3(H⊗E⊗F⊗w_0)):")
for c in range(DIM):
    if abs(d2d3[c]) > 1e-10:
        print(f"  {NAMES[c]} * {d2d3[c]}")

# Manual: d2(2 E⊗F - H⊗H) = 2[E,F] - [H,H] = 2H - 0 = 2H
print("Manual d2: d(2 E⊗F) = 2[E,F] = 2H; d(-H⊗H) = -[H,H] = 0; total = 2H")

# So d^2(H⊗E⊗F⊗w_0) = 2H ≠ 0!

# Now let's also check (H,E,F) tensor w_1
col_idx = (0 * DIM**2 + 1 * DIM + 2) * 2 + 1  # (H,E,F) tensor w_1
d3_col = d3_mat[:, col_idx]
print(f"\nd3(H⊗E⊗F⊗w_1):")
for row in range(DIM**2):
    if abs(d3_col[row]) > 1e-10:
        a = row // DIM
        b = row % DIM
        print(f"  ({NAMES[a]}⊗{NAMES[b]}) * {d3_col[row]}")

# Manual:
# Pair (0,1): [H,E]=2E. Res_{01}(w_1)=0. -> 0
# Pair (0,2): [H,F]=-2F. Res_{02}(w_1)=1. Result: (-2F, E) = -2*(2,1)
# Pair (1,2): [E,F]=H. Res_{12}(w_1)=-1. Result: (H, -H) = -1*(0,0)
print("Manual: (0,1) gives 0; (0,2) gives -2(F⊗E); (1,2) gives -(H⊗H)")

d2d3 = d2_mat @ d3_col
print(f"\nd2(d3(H⊗E⊗F⊗w_1)):")
for c in range(DIM):
    if abs(d2d3[c]) > 1e-10:
        print(f"  {NAMES[c]} * {d2d3[c]}")

# d2(-2 F⊗E - H⊗H) = -2[F,E] - [H,H] = -2(-H) = 2H
print("Manual d2: d(-2 F⊗E) = -2[F,E] = 2H; d(-H⊗H) = 0; total = 2H")

print("\n" + "="*60)
print("Key observation: d^2 ≠ 0 on individual tensor-OS elements,")
print("but maybe d^2 = 0 on certain LINEAR COMBINATIONS.")
print("="*60)

# The sum (H,E,F)⊗w_0 + alpha*(H,E,F)⊗w_1 might have d^2=0
# d^2(w_0 part) = 2H, d^2(w_1 part) = 2H
# So d^2((H,E,F)⊗(w_0+alpha*w_1)) = 2(1+alpha)H
# For d^2=0 need alpha = -1.
# (H,E,F)⊗(w_0-w_1) should have d^2=0.

# What is w_0 - w_1 as a form?
# w_0 = (0,1)(1,2), w_1 = (0,2)(1,2)
# w_0 - w_1 = w_{01}w_{12} - w_{02}w_{12} = (w_{01}-w_{02})w_{12}
# By Arnold: w_{01}w_{12} + w_{12}w_{20} + w_{20}w_{01} = 0
# i.e., w_{01}w_{12} - w_{12}w_{02} - w_{02}w_{01} = 0
# So w_{01}w_{12} = w_{12}w_{02} + w_{02}w_{01}
# And w_0 - w_1 = w_{01}w_{12} - w_{02}w_{12}
#   = (w_{12}w_{02} + w_{02}w_{01}) - w_{02}w_{12}
#   = w_{02}w_{12} + w_{02}w_{01} - w_{02}w_{12} (wait, ext alg is anti-comm)
# In the ext algebra: w_{12}w_{02} = -w_{02}w_{12}
# So w_0 - w_1 = -w_{02}w_{12} + w_{02}w_{01} - w_{02}w_{12}
#   = -2w_{02}w_{12} + w_{02}w_{01}
# Hmm, this doesn't simplify nicely.

# Let me try the FULL antisymmetrization:
# Alt(H⊗E⊗F) = H⊗E⊗F - H⊗F⊗E + E⊗F⊗H - E⊗H⊗F + F⊗H⊗E - F⊗E⊗H
# The image of e_H ∧ e_E ∧ e_F in g^{⊗3} tensor OS^2(C_3)
# under the isomorphism Lambda^3(g) -> (g^{⊗3} tensor OS^2(C_3))_{S_3}
# involves the S_3 action on BOTH factors.

# S_3 acts on g^{⊗3} by permuting tensor factors
# S_3 acts on OS^2(C_3) by permuting variables
# The diagonal action on the tensor product gives coinvariants

# The S_3 orbits on points:
# sigma = (01): swaps points 0,1
#   On g^{⊗3}: (a0,a1,a2) -> (a1,a0,a2)
#   On OS: w_{ij} -> w_{sigma(i),sigma(j)}
#     w_{01} -> w_{10} = -w_{01}
#     w_{02} -> w_{12}
#     w_{12} -> w_{02}
#   On NBC basis:
#     w_0 = w_{01}w_{12} -> (-w_{01})(w_{02}) = -w_{01}w_{02}
#       = -(Arnold: w_{01}w_{02} = -w_{01}w_{12} - w_{02}w_{12}) Hmm.

# This is getting complicated. Let me just do it numerically.

# ================================================================
# Build S_3 action and project to coinvariants
# ================================================================
from itertools import permutations

def parity(sigma):
    """Parity of permutation sigma (as a list)."""
    n = len(sigma)
    visited = [False]*n
    sign = 0
    for i in range(n):
        if not visited[i]:
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = sigma[j]
                cycle_len += 1
            sign += cycle_len - 1
    return (-1)**sign

# For n=3: S_3 acts on g^{otimes 3} tensor OS^2(C_3)
# We need the action on the OS basis.

# The OS^2(C_3) basis: w_0=(0,1)(1,2), w_1=(0,2)(1,2)
# For sigma in S_3, sigma acts on w_{ij} = d log(z_i - z_j) by:
# sigma(w_{ij}) = w_{sigma(i),sigma(j)} (= -w_{sigma(j),sigma(i)} if sigma(i)>sigma(j))

# First, compute the S_3 action on OS^2(C_3) in the NBC basis.
# For each sigma, compute sigma(w_0) and sigma(w_1) as NBC coords.

def apply_sigma_to_os_basis(sigma, basis_elem):
    """Apply permutation sigma to an OS basis element.
    basis_elem is a tuple of edges ((i1,j1), (i2,j2), ...).
    Returns (new_edges, sign) where sign accounts for reordering.
    """
    new_edges = []
    sign = 1
    for (i, j) in basis_elem:
        si, sj = sigma[i], sigma[j]
        if si < sj:
            new_edges.append((si, sj))
        else:
            new_edges.append((sj, si))
            sign *= -1  # w_{ji} = -w_{ij}
    # Sort edges and track sign
    arr = list(new_edges)
    for p in range(len(arr)):
        for q in range(len(arr)-1-p):
            if arr[q] > arr[q+1]:
                arr[q], arr[q+1] = arr[q+1], arr[q]
                sign *= -1
    return tuple(arr), sign

# Express in NBC basis
from sl3_bar_sign_test import os_basis, _express_in_nbc

os3_basis = os_basis(3)
print("\nOS^2(C_3) NBC basis:", os3_basis)

print("\nS_3 action on OS^2(C_3):")
perms_3 = list(permutations(range(3)))
os_action_matrices = {}
for sigma in perms_3:
    mat = np.zeros((2, 2))
    for k, b in enumerate(os3_basis):
        new_edges, sign = apply_sigma_to_os_basis(list(sigma), b)
        # Express new_edges in NBC basis
        coeffs = _express_in_nbc(new_edges, 3, os3_basis)
        if not coeffs and new_edges in os3_basis:
            coeffs = {os3_basis.index(new_edges): 1.0}
        for idx, v in coeffs.items():
            mat[idx, k] = sign * v
    os_action_matrices[sigma] = mat
    par = parity(list(sigma))
    print(f"  sigma={sigma} (par={par:+d}): matrix = {mat.tolist()}")

# ================================================================
# Build the antisymmetrizer projector on g^{otimes 3} tensor OS^2(C_3)
# ================================================================
# The antisymmetrizer (for the sign representation):
# P_anti = (1/n!) sum_sigma sgn(sigma) * sigma
# where sigma acts DIAGONALLY: sigma(v tensor w) = sigma(v) tensor sigma(w)
# and the sign comes from the representation we want.

# Actually, for the CE complex, the isomorphism is:
# Lambda^n(g) ~= (g^{otimes n} tensor sgn_n)_{S_n}
# where sgn_n is the sign representation.
# This is the same as (g^{otimes n})^{S_n,anti} = antisymmetric tensors.

# In the tensor-OS model, the analog is:
# Lambda^n(g) ~= (g^{otimes n} tensor OS^{n-1}(C_n))_{S_n}
# where S_n acts diagonally, and the coinvariants use the TRIVIAL character
# (because the OS top form already carries the sign representation).

# Actually: OS^{n-1}(C_n) = H^{n-1}(Conf_n(C), C) as S_n-rep.
# For n=3: this is the standard representation of S_3 minus trivial, i.e.,
# it's 2-dimensional... but which rep?

# Let me check: trace of each element
for sigma in perms_3:
    tr = np.trace(os_action_matrices[sigma])
    par = parity(list(sigma))
    print(f"  Tr(sigma={sigma}) = {tr:.0f}, parity={par:+d}")

# If OS^2(C_3) is the sign representation, then Tr(sigma) = sgn(sigma)*2.
# If it's the standard rep, Tr(id)=2, Tr(transposition)=0, Tr(3-cycle)=-1.

print("\n" + "="*60)
print("Building coinvariant projection and checking d^2=0")
print("="*60)

# The coinvariant space (g^{otimes n} tensor OS^{n-1})_{S_n}:
# For the CORRECT isomorphism Lambda^n(g) ~= coinvariants,
# we need to use: sigma acts on g^{otimes n} by permuting factors,
# and on OS by the above matrices.
# The coinvariant for the SIGN character:
# P = (1/6) sum_sigma sgn(sigma) * sigma
# This projects onto the subspace where sigma*v = sgn(sigma)*v.

# Total dim at n=3: 27*2 = 54
total_dim_3 = DIM**3 * 2

# Build sigma action on the total space
def sigma_action_matrix(sigma, n=3):
    """Build matrix for sigma acting on g^{otimes n} tensor OS^{n-1}(C_n)."""
    if n != 3:
        raise NotImplementedError

    os_mat = os_action_matrices[sigma]
    total = DIM**n * 2
    M = np.zeros((total, total))

    for tup in iproduct(range(DIM), repeat=n):
        # sigma permutes tensor factors
        new_tup = tuple(tup[sigma[k]] for k in range(n))
        col_lie = tup[0]*DIM**2 + tup[1]*DIM + tup[2]
        row_lie = new_tup[0]*DIM**2 + new_tup[1]*DIM + new_tup[2]

        for wk in range(2):
            col = col_lie*2 + wk
            for wl in range(2):
                row = row_lie*2 + wl
                M[row, col] += os_mat[wl, wk]

    return M

# Build sign-character projector
P_sign = np.zeros((total_dim_3, total_dim_3))
for sigma in perms_3:
    par = parity(list(sigma))
    M = sigma_action_matrix(sigma)
    P_sign += par * M
P_sign /= 6.0  # |S_3| = 6

# Also try trivial character
P_triv = np.zeros((total_dim_3, total_dim_3))
for sigma in perms_3:
    M = sigma_action_matrix(sigma)
    P_triv += M
P_triv /= 6.0

rk_sign = np.linalg.matrix_rank(P_sign, tol=1e-8)
rk_triv = np.linalg.matrix_rank(P_triv, tol=1e-8)
print(f"  Sign-character coinvariants: rank(P) = {rk_sign}")
print(f"  Trivial-character coinvariants: rank(P) = {rk_triv}")
print(f"  (Expected: Lambda^3(sl_2) = C(3,3) = 1)")

# Check d^2=0 on each subspace
d3_mat = build_d3()
d2_mat = build_d2()
comp = d2_mat @ d3_mat

# Restrict d3 to the sign-coinvariant subspace
# If P*v = v for v in the subspace, then d^2*P should be 0 on the image
comp_sign = comp @ P_sign
comp_triv = comp @ P_triv
print(f"\n  d2 o d3 o P_sign: max|err| = {np.max(np.abs(comp_sign)):.1e}")
print(f"  d2 o d3 o P_triv: max|err| = {np.max(np.abs(comp_triv)):.1e}")

# Also check for n=2
total_dim_2 = DIM**2 * 1  # OS^1(C_2) is 1-dim
P_sign_2 = np.zeros((total_dim_2, total_dim_2))
P_triv_2 = np.zeros((total_dim_2, total_dim_2))
for sigma in permutations(range(2)):
    sigma = list(sigma)
    par = parity(sigma)
    M = np.zeros((total_dim_2, total_dim_2))
    for tup in iproduct(range(DIM), repeat=2):
        new_tup = tuple(tup[sigma[k]] for k in range(2))
        col = tup[0]*DIM + tup[1]
        row = new_tup[0]*DIM + new_tup[1]
        # OS^1(C_2) action: sigma swaps 0,1; w_{01} -> w_{10} = -w_{01}
        os_sign = 1 if sigma == [0,1] else -1
        M[row, col] = os_sign
    P_sign_2 += par * M
    P_triv_2 += M
P_sign_2 /= 2.0
P_triv_2 /= 2.0

rk_sign_2 = np.linalg.matrix_rank(P_sign_2, tol=1e-8)
rk_triv_2 = np.linalg.matrix_rank(P_triv_2, tol=1e-8)
print(f"\n  n=2: Sign-character coinvariants: rank = {rk_sign_2}")
print(f"  n=2: Trivial-character coinvariants: rank = {rk_triv_2}")
print(f"  (Expected: Lambda^2(sl_2) = C(3,2) = 3)")

# Check if d3 maps sign-coinvariants to sign-coinvariants
d3_P = d3_mat @ P_sign
P_d3 = P_sign_2 @ d3_mat
print(f"\n  d3 maps sign-coinvariants to target:")
print(f"  max|P_sign_2 @ d3 - P_sign_2 @ d3 @ P_sign| = {np.max(np.abs(P_d3 - P_sign_2 @ d3_mat @ P_sign)):.1e}")

# Also check trivial
d3_Pt = d3_mat @ P_triv
Pt_d3 = P_triv_2 @ d3_mat
print(f"  max|P_triv_2 @ d3 - P_triv_2 @ d3 @ P_triv| = {np.max(np.abs(Pt_d3 - P_triv_2 @ d3_mat @ P_triv)):.1e}")

print("\n" + "="*60)
print("Checking d^2=0 restricted to coinvariant subspaces")
print("="*60)

# Get basis for the sign-coinvariant subspace of B^3
U, S, Vt = np.linalg.svd(P_sign)
tol = 1e-8
# Columns of U corresponding to singular values near 1
# Actually P is a projector, so eigenvalues are 0 or 1
eigvals = np.abs(S)
basis_idx = eigvals > 0.5  # eigenvalue ~1
basis_sign_3 = U[:, basis_idx]  # columns form basis of sign-coinvariant subspace
print(f"  Sign-coinvariant subspace of B^3: dim = {basis_sign_3.shape[1]}")

# Similarly for B^2
U2, S2, _ = np.linalg.svd(P_sign_2)
basis_sign_2 = U2[:, np.abs(S2) > 0.5]
print(f"  Sign-coinvariant subspace of B^2: dim = {basis_sign_2.shape[1]}")

# Restrict d3 and d2 to these subspaces
d3_restricted = basis_sign_2.T @ d3_mat @ basis_sign_3
d2_restricted_target = d2_mat @ basis_sign_2
print(f"  d3 restricted: shape {d3_restricted.shape}")

comp_restricted = d2_restricted_target @ d3_restricted
print(f"  d2 o d3 restricted: max|err| = {np.max(np.abs(comp_restricted)):.1e}")

# Try trivial character
U2t, S2t, _ = np.linalg.svd(P_triv_2)
basis_triv_2 = U2t[:, np.abs(S2t) > 0.5]
Ut, St, _ = np.linalg.svd(P_triv)
basis_triv_3 = Ut[:, np.abs(St) > 0.5]
print(f"\n  Trivial-coinvariant subspace of B^3: dim = {basis_triv_3.shape[1]}")
print(f"  Trivial-coinvariant subspace of B^2: dim = {basis_triv_2.shape[1]}")

d3_triv = basis_triv_2.T @ d3_mat @ basis_triv_3
d2_triv_target = d2_mat @ basis_triv_2
comp_triv = d2_triv_target @ d3_triv
print(f"  d2 o d3 restricted (triv): max|err| = {np.max(np.abs(comp_triv)):.1e}")
