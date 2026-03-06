#!/usr/bin/env python3
"""Derive the tensor-OS bar differential from the CE differential.

Strategy: The CE complex Lambda^n(g) with basis {sorted n-subsets} and differential
  d(e_{i1}^...^e_{in}) = sum_{s<t} (-1)^{s+t+1} [e_{is},e_{it}] ^ e_{i1}^...^hat{is}^...^hat{it}^...

is isomorphic to g^{otimes n} tensor OS^{n-1}(C_n) modulo the OS relations.
We verify d^2=0 on the tensor-OS model by translating the CE sign convention.

The key insight: in the CE complex, the sign (-1)^{s+t+1} comes from removing
two elements at positions s and t from a wedge product. In the tensor-OS model,
we need to account for:
1. The OS residue Res_{ij}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1})
2. The contraction g^{otimes n} -> g^{otimes (n-1)} via [e_i, e_j]

The OS residue already handles the "form" part. The Lie contraction sign should
match so that the total differential agrees with CE on the image.
"""

import numpy as np
from itertools import combinations, product as iproduct
from math import comb

# ================================================================
# sl_3 structure constants
# ================================================================
DIM = 8
NAMES = ['H1', 'H2', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']

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

print("Structure constants verified (antisymmetry + Jacobi)")

# ================================================================
# CE differential (known correct)
# ================================================================
def exterior_basis(n):
    return list(combinations(range(DIM), n))

def wedge_insert(gen, remaining):
    if gen in remaining:
        return None
    lst = list(remaining) + [gen]
    arr = lst[:]
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return tuple(arr), (-1)**swaps

def ce_diff(n):
    if n <= 1:
        return np.zeros((1, max(1, comb(DIM, n))))
    basis_n = exterior_basis(n)
    basis_nm1 = exterior_basis(n-1)
    idx = {b: i for i, b in enumerate(basis_nm1)}
    M = np.zeros((len(basis_nm1), len(basis_n)))
    for col, elem in enumerate(basis_n):
        for s in range(n):
            for t in range(s+1, n):
                a, b_idx = elem[s], elem[t]
                sign_st = (-1)**(s + t + 1)
                remaining = tuple(elem[r] for r in range(n) if r != s and r != t)
                for c in range(DIM):
                    coeff = f[a][b_idx][c]
                    if abs(coeff) < 1e-10:
                        continue
                    result = wedge_insert(c, remaining)
                    if result is None:
                        continue
                    sorted_tuple, wsign = result
                    if sorted_tuple in idx:
                        M[idx[sorted_tuple], col] += sign_st * coeff * wsign
    return M

# Verify CE d^2=0
print("\nCE verification:")
for n in range(2, 6):
    d_n = ce_diff(n)
    d_nm1 = ce_diff(n-1)
    err = np.max(np.abs(d_nm1 @ d_n))
    print(f"  d_{n-1} o d_{n}: max|d^2| = {err:.1e}")

# ================================================================
# Now build the SAME differential on g^{otimes n} (unsymmetrized)
# ================================================================
# Key: g^{otimes n} has basis {(a_1,...,a_n) : a_i in {0,...,7}}
# The CE differential on Lambda^n embeds into the one on g^{otimes n}
# via antisymmetrization.
#
# On g^{otimes n}, the differential is:
#   d(e_{a_1} otimes ... otimes e_{a_n}) =
#     sum_{s<t} (-1)^{s+t+1} sum_c f[a_s,a_t,c] *
#       e_{a_1} otimes ... otimes hat{a_s} otimes ... otimes e_c(at pos t) otimes ... otimes e_{a_n}
#       (with relabeling: remove pos s, put c at pos t)
#
# Wait — that's not right either. In the CE complex, removing positions s,t
# and inserting [e_s,e_t] gives an (n-1)-form. The positions get relabeled.
#
# Let's just directly build d on g^{otimes n} -> g^{otimes (n-1)} using
# the CE sign convention:
#
# d(e_{a_1} ... e_{a_n}) = sum_{s<t} (-1)^{s+t+1} [e_{a_s}, e_{a_t}]
#   tensor (remove positions s and t, insert bracket result)
#
# There's a choice: where does the bracket result go? In CE, it just goes
# into the wedge. In the tensor product, we must choose. Standard: replace
# position s with [a_s,a_t], delete position t. Or: delete position s,
# replace position t with [a_s,a_t]. These differ by sign.
#
# Actually, the standard bar differential does:
# d(a_1|...|a_n) = sum_{i<j} eps_{ij} [a_i, a_j] inserted, others kept
# where the result is an (n-1)-tuple.

# Let's try BOTH placements and ALL signs:

def tensor_diff(n, placement='replace_first', extra_sign_func=None):
    """Build d: g^{otimes n} -> g^{otimes (n-1)}.

    placement='replace_first': replace pos s with [a_s,a_t], delete pos t
    placement='replace_second': delete pos s, replace pos t with [a_s,a_t]
    """
    dim_n = DIM ** n
    dim_nm1 = DIM ** (n-1)

    def to_index(tup):
        idx = 0
        for t in tup:
            idx = idx * DIM + t
        return idx

    M = np.zeros((dim_nm1, dim_n))

    for tup in iproduct(range(DIM), repeat=n):
        col = to_index(tup)
        for s in range(n):
            for t in range(s+1, n):
                sign = (-1)**(s + t + 1)
                if extra_sign_func:
                    sign *= extra_sign_func(s, t, n)

                for c in range(DIM):
                    coeff = f[tup[s]][tup[t]][c]
                    if abs(coeff) < 1e-10:
                        continue

                    if placement == 'replace_first':
                        # Replace s with c, delete t
                        new = list(tup)
                        new[s] = c
                        new = tuple(new[:t] + new[t+1:])
                    else:
                        # Delete s, replace t with c
                        new = list(tup)
                        new[t] = c
                        new = tuple(new[:s] + new[s+1:])

                    M[to_index(new), col] += sign * coeff

    return M

print("\n" + "="*60)
print("Testing tensor differential d^2=0 (no OS, just g^{otimes n})")
print("="*60)

for placement in ['replace_first', 'replace_second']:
    for name, sfunc in [("none", None),
                         ("(-1)^{s+t}", lambda s,t,n: (-1)**(s+t)),
                         ("(-1)", lambda s,t,n: -1)]:
        d2 = tensor_diff(2, placement)
        d3 = tensor_diff(3, placement, sfunc)

        # For d2, also apply extra sign
        d2_s = tensor_diff(2, placement, sfunc)

        comp = d2_s @ d3
        err = np.max(np.abs(comp))
        r2 = np.linalg.matrix_rank(d2_s, tol=1e-8)
        r3 = np.linalg.matrix_rank(d3, tol=1e-8)
        status = "d^2=0" if err < 1e-8 else f"d^2!=0 ({err:.1e})"
        print(f"  {placement:15s} extra={name:15s}: rk(d2)={r2:3d} rk(d3)={r3:4d} {status}")

# ================================================================
# Now the CE approach on g^{otimes n} with antisymmetrizer
# ================================================================
# The CE differential on Lambda^n(g) CAN be computed via:
# d_CE = Alt_{n-1} o d_tensor o incl_n
# where Alt is the antisymmetrizer and d_tensor acts on g^{otimes n}.
#
# But actually, the tensor differential d_tensor should satisfy d^2=0
# BY ITSELF if the formula is correct (since it's just the bar differential
# of the Lie algebra viewed as an associative algebra, sort of).
#
# Actually NO. The bar differential of a Lie algebra uses the BAR complex
# which is different. The CE differential uses the WEDGE product structure.
# On g^{otimes n} without antisymmetrization, d^2 != 0 in general; it's
# only d^2=0 on Lambda^n(g).
#
# For the OS model, the point is that OS^{n-1}(C_n) provides the
# "combinatorial" analog of the exterior algebra.

# ================================================================
# Direct approach: CE on Lambda^n(g) = g^{otimes n} / S_n(signs)
# The bar complex of a Lie algebra: B(g) = T^c(s^{-1}g)
# Bar differential uses the Lie bracket.
# This is the ASSOCIATIVE bar construction applied to U(g).
#
# Actually, the Chevalley-Eilenberg complex IS the bar construction
# for the Lie operad. The associative bar construction is different.
#
# For CHIRAL algebras, the bar construction uses the OS/configuration
# space model. For the LIE algebra case (genus 0, affine Kac-Moody at
# level 0), the chiral bar complex reduces to a model using OS algebras.
#
# The tensor-OS model: B^n = g^{otimes n} tensor OS^{n-1}(C_n)
# The OS algebra OS^*(C_n) has an NBC basis, and the residue maps
# Res_{ij}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1}) contract (merge) points.
#
# The differential: for each pair (i,j), 1 <= i < j <= n, we take
# the bracket [a_i, a_j] and apply Res_{ij} to the form.
# After Res_{ij}, the n points become n-1 points (i and j merge).
# The Lie tensor changes: position i gets [a_i,a_j], position j is removed.
#
# But what sign? The OS residue carries sign from the Arnold relations.
# The additional sign should come from the operad structure.
#
# For the COM! = LIE case, the bar construction of a commutative algebra
# gives the Harrison complex. For LIE algebras, the "bar construction"
# in the operadic sense gives the CE complex.
#
# Key reference: Loday-Vallette, Section 10.1.7:
# C(g) = (Lie^i(g), d) where Lie^i is the Lie cooperad applied to g.
# The differential uses the cooperad decomposition.
#
# In our tensor-OS model, Lie^i(n) = OS^{n-1}(C_n) (the top form part).
# The cooperad decomposition maps are the residue maps.
#
# The CE sign (-1)^{s+t+1} already accounts for everything when
# the basis elements are ordered. The question is how this translates
# to the tensor-OS model where Lie tensors and OS forms are SEPARATE.

# ================================================================
# CORRECT APPROACH: Build CE on g^{otimes n} tensor Lambda^{n-1}(n)
# where Lambda^{n-1}(n) = top exterior power of the OS algebra.
# ================================================================
# Actually, OS^{n-1}(C_n) IS Lambda^{n-1}(arrangement complement).
# The NBC basis gives a canonical basis.
# The residue map Res_{ij} is the "contraction" map.
#
# In the combined complex, a basis element is:
#   (a_1,...,a_n) tensor omega
# where omega is an NBC basis element of OS^{n-1}(C_n).
#
# The differential should be:
#   d((a_1,...,a_n) tensor omega) = sum_{(i,j)} [a_i,a_j]_c *
#     (a_1,...,a_c@j,...,hat{a_i},...,a_n) tensor Res_{ij}(omega)
#
# with sign = (-1)^{i} (for removing position i from the tensor).
# The OS residue Res_{ij} already carries its own sign from the
# position of (i,j) in omega.
#
# But we showed this doesn't work with (-1)^i. Let me think again...
#
# Actually, maybe the sign should be (-1)^{s+t+1} just like CE,
# and the OS residue should NOT carry an additional position-dependent sign.

# Let me try: just use the CE sign (-1)^{s+t+1} and the OS residue
# (which includes the position-of-edge sign from Arnold/NBC decomposition).

# We already tested this in the sign_test script with (-1)^{i+j+1}.
# It didn't work. So there must be something else going on.

# The problem might be in the residue computation itself.
# Let me verify the residue maps independently.

# ================================================================
# Verify: does the OS residue satisfy the right compatibility?
# ================================================================
# For n=3, OS^2(C_3) has basis {w_{12}w_{23}} (single NBC element).
# (Using edges (0,1), (0,2), (1,2); NBC basis for n=3, degree 2
#  avoids broken circuit {(0,1),(0,2)}, so basis = {(0,1)(1,2)} and {(0,2)(1,2)}.)
# Wait — let me just compute it.

from sl3_bar_sign_test import os_basis, compute_residue_matrices

for n in range(2, 5):
    basis = os_basis(n)
    print(f"\nOS^{n-1}(C_{n}) NBC basis (dim={len(basis)}):")
    for i, b in enumerate(basis):
        print(f"  {i}: {b}")

print("\nResidue matrices for n=3:")
res3 = compute_residue_matrices(3)
for (i,j), M in sorted(res3.items()):
    if np.any(np.abs(M) > 1e-10):
        print(f"  Res_({i},{j}): {M.flatten()}")

print("\nResidue matrices for n=4:")
res4 = compute_residue_matrices(4)
basis4 = os_basis(4)
basis3 = os_basis(3)
print(f"  OS^3(C_4) dim={len(basis4)}, OS^2(C_3) dim={len(basis3)}")
for (i,j), M in sorted(res4.items()):
    if np.any(np.abs(M) > 1e-10):
        print(f"  Res_({i},{j}):")
        print(f"    {M}")
