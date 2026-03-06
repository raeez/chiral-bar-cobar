#!/usr/bin/env python3
"""Build the correct tensor-OS bar differential for sl_3 by using
the isomorphism Lambda^n(g) ~= (g^{otimes n} tensor OS^{n-1}(C_n))_{S_n}
to transport the known-correct CE differential.

Plan:
1. Build the CE differential (verified d^2=0)
2. Build the embedding Lambda^n(g) -> g^{otimes n} tensor OS^{n-1}(C_n)
3. Read off what the differential looks like on the tensor-OS side
4. Verify d^2=0 on the full (non-antisymmetrized) tensor-OS complex

Key fact from Arnold/OS theory:
  Lambda^n(C^N) ~= OS^n(C_N) as graded vector spaces
  (more precisely, H^n(M(A_N)) where A_N is the braid arrangement)

For our purposes: the NBC basis of OS^{n-1}(C_n) provides (n-1)! elements,
and g^{otimes n} provides dim(g)^n elements. The total dimension
dim(g)^n * (n-1)! should match C(dim(g), n) * n! / ... no, that's wrong.

Actually: Lambda^n(g) has dim C(8,n), while g^{otimes n} tensor OS^{n-1}(C_n)
has dim 8^n * (n-1)!. These are NOT the same (64*1=64 vs C(8,2)=28 at n=2).
The tensor-OS space is LARGER. The CE complex sits inside as the S_n-invariant
(with signs) subspace.

So the tensor-OS bar complex is genuinely different from CE — it's a larger
complex. The differential must use the interaction between the tensor ordering
and the OS forms. Let me reconsider.

Actually, let me reconsider the whole setup. The CHIRAL bar complex at genus 0
for a Kac-Moody algebra V_k(g) at level k is NOT the CE complex of g.
It's a bigger complex where:
- Bar degree n has chain groups labeled by n-tuples of generators
  (with conformal weights) tensored with OS forms
- The bar differential uses OPE residues, not just Lie brackets

For the MINIMUM WEIGHT sector (all generators at weight 1, i.e., the
currents J^a of the affine Lie algebra), the chain space at bar degree n is
g^{otimes n} tensor OS^{n-1}(C_n), and the differential involves the
simple-pole OPE J^a(z) J^b(w) ~ [a,b]/(z-w) + k(a,b)/(z-w)^2.

The simple pole gives the Lie bracket term, and the double pole gives
the "curvature" (level) term. At level k=0 (just the Lie algebra),
only the simple pole contributes.

For d^2=0, we need:
- d_bracket^2 + {d_bracket, d_curvature} + d_curvature^2 = 0
- d_curvature^2 = 0 automatically (curvature produces scalars)
- The remaining condition is the BORCHERDS identity on OS forms

This means d^2=0 does NOT follow from just Jacobi + Arnold. It requires
the full OPE/Borcherds identity, which mixes the Lie bracket and OS structure.

Let me try to build the differential correctly by being more careful about
what Res_{ij} does and how it interacts with the tensor factor.
"""

import numpy as np
from itertools import product as iproduct
import sys
sys.path.insert(0, '/Users/raeez/chiral-bar-cobar/compute/scripts')
from sl3_bar_sign_test import os_basis, compute_residue_matrices, _relabel_edge, _sort_with_sign, _express_in_nbc, f, DIM

# ================================================================
# Approach: Direct verification via small examples
# ================================================================

# For n=2: B^2 = g^{otimes 2} tensor OS^1(C_2)
# OS^1(C_2) = span{w_{01}} (1-dimensional)
# So B^2 = g^{otimes 2} (dim 64)
#
# d: B^2 -> B^1 = g^{otimes 1} tensor OS^0(C_1) = g (dim 8)
#
# d(a tensor b tensor w_{01}) = [a,b] tensor Res_{01}(w_{01})
#                              = [a,b] tensor 1 (in OS^0(C_1))
#
# This is just the Lie bracket. d: g^2 -> g, d(a,b) = [a,b].
# This is correct and obviously has d^2 NOT defined (need d: g -> k).

# For n=3: B^3 = g^{otimes 3} tensor OS^2(C_3)
# OS^2(C_3) has NBC basis: {(0,1)(1,2), (0,2)(1,2)} (dim 2)
# So dim B^3 = 8^3 * 2 = 1024
#
# d: B^3 -> B^2 = g^{otimes 2} tensor OS^1(C_2) = g^{otimes 2} (dim 64)
#
# For a basis element (a,b,c) tensor omega where omega in OS^2(C_3):
# d = sum_{0<=i<j<=2} bracket_{ij} tensor Res_{ij}
#
# After Res_{ij}, points {0,1,2} -> {0,1} (merged pair becomes min(i,j),
# higher indices shift down).
#
# Let's trace through:
# For (i,j) = (0,1): merge 0,1 -> 0, point 2 -> 1
#   Lie: (a,b,c) -> ([a,b], c) at positions (0,1)
#   Form: Res_{01}(omega)
#
# For (i,j) = (0,2): merge 0,2 -> 0, point 1 stays 1
#   Lie: (a,b,c) -> ([a,c], b) at positions (0,1)
#   Form: Res_{02}(omega)
#
# For (i,j) = (1,2): merge 1,2 -> 1, point 0 stays 0
#   Lie: (a,b,c) -> (a, [b,c]) at positions (0,1)
#   Form: Res_{12}(omega)
#
# What sign? The sign must come from something. In the operad picture,
# the sign comes from the operadic composition. For the Lie operad
# (identified with commutative cooperad), the composition signs are
# the Koszul signs.
#
# The Lie cooperad: Lie^i(n) = sgn_n (the sign representation of S_n).
# The decomposition map delta: Lie^i(n) -> Lie^i(k) tensor Lie^i(n-k+1)
# involves the sign from the shuffle.
#
# For our tensor-OS model: OS^{n-1}(C_n) ~= Lie^i(n) tensor sgn_n
# (the Lie cooperad tensored with the sign representation).
# Actually, OS^{n-1}(C_n) ~= H^{n-1}(M(A_n)) which is the
# top-dimensional cohomology of the complement, which is the
# SIGN representation of S_n (as a vector space of dimension (n-1)!).
#
# Wait, H^{n-1}(M(A_{n-1})) = H^{n-1}(Conf_n(C)) and it is NOT
# just the sign representation. It's the regular representation
# decomposed via NBC. Let me just work with explicit matrices.

# ================================================================
# Build d: g^{otimes 3} tensor OS^2(C_3) -> g^{otimes 2} tensor OS^1(C_2)
# and d: g^{otimes 2} tensor OS^1(C_2) -> g^{otimes 1} tensor OS^0(C_1)
# with sign = (-1)^{s+t+1} (CE convention) applied BEFORE the Res.
# ================================================================

# The key question: do we apply the CE sign (-1)^{s+t+1} to the
# tensor-OS differential, or does the OS residue already account for it?
#
# Hypothesis: the correct differential is
#   d = sum_{i<j} (-1)^{i+j+1} * bracket_{ij} tensor Res_{ij}
# where bracket_{ij} replaces position i with [a_i,a_j] and deletes j,
# AND Res_{ij} acts on the OS factor.
#
# We already tested (-1)^{i+j+1} in sl3_bar_sign_test.py, and it failed.
# But wait — in that test, the sign was applied to the COMBINED contribution.
# Let me re-examine: the differential in that test was
#   M[row,col] += sign * coeff * res_mat[row_f, col_f]
# where sign = sign_func(i,j,n), coeff = f[a_i][a_j][c],
# and res_mat is the OS residue matrix.
#
# So sign_func = (-1)^{i+j+1} was already tested and FAILED.
# But the contraction (i,j) in my test was:
#   "Replace j with c, remove i" — i.e. the bracket output goes to position j.
#
# In CE, the convention is that [a_s, a_t] goes to a NEW position that
# inherits from the wedge. In the tensor model, placing [a_i,a_j] at
# position j and removing position i is different from placing it at
# position i and removing position j.
#
# Let me systematically test ALL combinations:
# - Placement: [a_i,a_j] at pos i (remove j) vs at pos j (remove i)
# - Sign: various functions of i,j

def build_bar_diff(n, placement, sign_func):
    """Build d: g^{otimes n} tensor OS^{n-1}(C_n) -> g^{otimes(n-1)} tensor OS^{n-2}(C_{n-1}).

    placement='at_i': [a_i,a_j] replaces pos i, delete pos j
    placement='at_j': [a_i,a_j] replaces pos j, delete pos i
    """
    os_n = os_basis(n)
    os_nm1 = os_basis(n-1)
    res_mats = compute_residue_matrices(n)

    lie_dim_n = DIM ** n
    lie_dim_nm1 = DIM ** (n-1)
    total_n = lie_dim_n * len(os_n)
    total_nm1 = lie_dim_nm1 * len(os_nm1)

    def lie_idx(tup):
        idx = 0
        for t in tup:
            idx = idx * DIM + t
        return idx

    M = np.zeros((total_nm1, total_n))

    for lie_tup in iproduct(range(DIM), repeat=n):
        col_lie = lie_idx(lie_tup)

        for i in range(n):
            for j in range(i+1, n):
                sign = sign_func(i, j, n)
                res_mat = res_mats[(i,j)]

                for c in range(DIM):
                    coeff = f[lie_tup[i]][lie_tup[j]][c]
                    if abs(coeff) < 1e-10:
                        continue

                    if placement == 'at_i':
                        # [a_i,a_j] at pos i, delete pos j
                        new = list(lie_tup)
                        new[i] = c
                        new = tuple(new[:j] + new[j+1:])
                    else:
                        # [a_i,a_j] at pos j, delete pos i
                        new = list(lie_tup)
                        new[j] = c
                        new = tuple(new[:i] + new[i+1:])

                    row_lie = lie_idx(new)

                    for cf in range(len(os_n)):
                        for rf in range(len(os_nm1)):
                            rv = res_mat[rf, cf]
                            if abs(rv) < 1e-10:
                                continue
                            col = col_lie * len(os_n) + cf
                            row = row_lie * len(os_nm1) + rf
                            M[row, col] += sign * coeff * rv

    return M

# Test all sign/placement combinations
print("Systematic search: d^2=0 on g^{otimes n} tensor OS^{n-1}(C_n)")
print("=" * 70)

sign_options = {
    "1":           lambda i,j,n: 1,
    "-1":          lambda i,j,n: -1,
    "(-1)^i":      lambda i,j,n: (-1)**i,
    "(-1)^j":      lambda i,j,n: (-1)**j,
    "(-1)^{i+1}":  lambda i,j,n: (-1)**(i+1),
    "(-1)^{j+1}":  lambda i,j,n: (-1)**(j+1),
    "(-1)^{i+j}":  lambda i,j,n: (-1)**(i+j),
    "(-1)^{i+j+1}":lambda i,j,n: (-1)**(i+j+1),
    "(-1)^{j-i}":  lambda i,j,n: (-1)**(j-i),
    "(-1)^{j-i+1}":lambda i,j,n: (-1)**(j-i+1),
}

found = False
for placement in ['at_i', 'at_j']:
    for sname, sfunc in sign_options.items():
        try:
            d2 = build_bar_diff(2, placement, sfunc)
            d3 = build_bar_diff(3, placement, sfunc)
            comp = d2 @ d3
            err = np.max(np.abs(comp))
            if err < 1e-8:
                r2 = np.linalg.matrix_rank(d2, tol=1e-8)
                r3 = np.linalg.matrix_rank(d3, tol=1e-8)
                print(f"  *** d^2=0 FOUND: placement={placement}, sign={sname}")
                print(f"      rank(d2)={r2}, rank(d3)={r3}")

                # Compute bar cohomology
                k2 = d2.shape[1] - r2
                k3 = d3.shape[1] - r3
                h2 = k2 - r3  # ker(d2)/im(d3)
                print(f"      dim B^2={d2.shape[1]}, dim B^3={d3.shape[1]}")
                print(f"      ker(d2)={k2}, H^2={h2}")
                found = True
        except Exception as e:
            print(f"  ERROR: {placement}/{sname}: {e}")

if not found:
    print("\n  No simple sign convention gives d^2=0.")
    print("  Testing with additional Koszul signs from tensor permutation...")

    # Maybe we need a sign that depends on the Lie algebra elements (grading).
    # In the super/graded setting, permuting elements gives Koszul signs.
    # Since all generators are in degree 1 (odd after desuspension s^{-1}),
    # permuting two desuspended elements gives (-1)^{1*1} = -1.
    # The desuspension shifts the degree: |s^{-1}a| = |a| - 1.
    # For Lie algebra elements in degree 0 (concentrated in degree 0),
    # s^{-1}a is in degree -1 (odd in cohomological convention).

    # In the bar complex B(A) = T^c(s^{-1}A_+), the elements s^{-1}a
    # are in degree -1. The bar differential involves removing one
    # factor and applying mu, so there's a sign from commuting s^{-1}
    # past previous factors.

    # For the classical bar complex of an associative algebra:
    # d[a_1|...|a_n] = sum_{i=1}^{n-1} (-1)^i [a_1|...|a_i*a_{i+1}|...|a_n]
    # (with desuspension signs already absorbed).

    # For a Lie algebra, the bar = CE complex uses:
    # d = sum_{i<j} (-1)^{i+j} f^c_{ij} (with various conventions)

    # The issue: in the tensor-OS model the sign might depend on
    # which OS basis element we're using (i.e., on the topology
    # of the form, not just the positions i,j).

    # Alternative: the sign might need to account for the position
    # of the edge (i,j) within the OS form omega.
    # Specifically, if omega = w_{e_1} ... w_{e_{n-1}} and (i,j)=e_k,
    # then the sign should include (-1)^{k-1} from the position of
    # the edge being "contracted" in the form.

    # But wait — the residue map already accounts for the position
    # sign via (-1)^pos in the _compute_residue_matrices function!
    # Let me check...

    # In compute_residue_matrices, line 114: sign = (-1)**pos
    # This is the sign from removing the edge at position pos
    # from the NBC monomial.

    # So the residue map ALREADY includes (-1)^{position in form}.
    # The remaining sign should just be from the Lie contraction.

    # Let me try: NO additional sign (sign=1) but with the
    # (-1)^pos removed from the residue, replaced by (-1)^{i+j+1}:

    print("\n  Testing: CE sign on Lie, clean residue (no position sign)...")

    def compute_residue_no_pos_sign(n):
        """Residue matrices WITHOUT the (-1)^pos sign."""
        from sl3_bar_sign_test import os_basis, _relabel_edge, _sort_with_sign, _express_in_nbc
        basis_n = os_basis(n)
        basis_nm1 = os_basis(n - 1)
        matrices = {}
        for i in range(n):
            for j in range(i+1, n):
                M = np.zeros((len(basis_nm1), len(basis_n)), dtype=np.float64)
                for col, form in enumerate(basis_n):
                    if (i,j) not in form: continue
                    pos = form.index((i,j))
                    # NO (-1)^pos sign here
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
                        M[row, col] += sort_sign * v  # no (-1)^pos
                matrices[(i, j)] = M
        return matrices

    def build_bar_diff_v2(n, placement, sign_func, use_clean_res=False):
        os_n = os_basis(n)
        os_nm1 = os_basis(n-1)
        if use_clean_res:
            res_mats = compute_residue_no_pos_sign(n)
        else:
            res_mats = compute_residue_matrices(n)

        lie_dim_n = DIM ** n
        lie_dim_nm1 = DIM ** (n-1)
        total_n = lie_dim_n * len(os_n)
        total_nm1 = lie_dim_nm1 * len(os_nm1)

        def lie_idx(tup):
            idx = 0
            for t in tup:
                idx = idx * DIM + t
            return idx

        M = np.zeros((total_nm1, total_n))

        for lie_tup in iproduct(range(DIM), repeat=n):
            col_lie = lie_idx(lie_tup)
            for i in range(n):
                for j in range(i+1, n):
                    sign = sign_func(i, j, n)
                    res_mat = res_mats[(i,j)]
                    for c in range(DIM):
                        coeff = f[lie_tup[i]][lie_tup[j]][c]
                        if abs(coeff) < 1e-10:
                            continue
                        if placement == 'at_i':
                            new = list(lie_tup)
                            new[i] = c
                            new = tuple(new[:j] + new[j+1:])
                        else:
                            new = list(lie_tup)
                            new[j] = c
                            new = tuple(new[:i] + new[i+1:])
                        row_lie = lie_idx(new)
                        for cf in range(len(os_n)):
                            for rf in range(len(os_nm1)):
                                rv = res_mat[rf, cf]
                                if abs(rv) < 1e-10:
                                    continue
                                col = col_lie * len(os_n) + cf
                                row = row_lie * len(os_nm1) + rf
                                M[row, col] += sign * coeff * rv
        return M

    for placement in ['at_i', 'at_j']:
        for sname, sfunc in sign_options.items():
            d2 = build_bar_diff_v2(2, placement, sfunc, use_clean_res=True)
            d3 = build_bar_diff_v2(3, placement, sfunc, use_clean_res=True)
            comp = d2 @ d3
            err = np.max(np.abs(comp))
            if err < 1e-8:
                print(f"  *** d^2=0 FOUND (clean res): placement={placement}, sign={sname}")
                found = True

    if not found:
        print("  Still no d^2=0. The issue is deeper.")

        # Final attempt: use (-1)^{i+j+1} on the CE sign COMBINED with
        # (-1)^pos from the residue, but also include (-1)^i for the
        # Koszul sign from desuspension.
        print("\n  Brute-forcing 3-parameter sign: (-1)^{a*i + b*j + c*pos + d}...")

        res3_full = compute_residue_matrices(3)
        os3 = os_basis(3)
        os2 = os_basis(2)

        # For each basis form in OS^2(C_3), find which (i,j) it contains
        # and at what position
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        # sign = (-1)^{a*i + b*j + c*pos + d}
                        # where pos is the position of edge (i,j) in the OS basis element
                        def make_sign(a,b,c,d):
                            def sf(i,j,n):
                                return (-1)**(a*i + b*j + d)
                            return sf

                        for placement in ['at_i', 'at_j']:
                            # Need to encode pos-dependent sign into residue
                            def compute_res_with_pos_sign(n, a_exp, b_exp, c_exp, d_exp):
                                from sl3_bar_sign_test import os_basis, _relabel_edge, _sort_with_sign, _express_in_nbc
                                basis_n = os_basis(n)
                                basis_nm1 = os_basis(n - 1)
                                matrices = {}
                                for ii in range(n):
                                    for jj in range(ii+1, n):
                                        M = np.zeros((len(basis_nm1), len(basis_n)))
                                        for col, form in enumerate(basis_n):
                                            if (ii,jj) not in form: continue
                                            pos = form.index((ii,jj))
                                            sign_total = (-1)**(a_exp*ii + b_exp*jj + c_exp*pos + d_exp)
                                            remaining = list(form[:pos]) + list(form[pos+1:])
                                            relabeled = []
                                            ok = True
                                            for e in remaining:
                                                e2 = _relabel_edge(e, ii, jj)
                                                if e2 is None: ok = False; break
                                                relabeled.append(e2)
                                            if not ok: continue
                                            sorted_rel, sort_sign = _sort_with_sign(relabeled)
                                            coeffs = _express_in_nbc(sorted_rel, n - 1, basis_nm1)
                                            for row, v in coeffs.items():
                                                M[row, col] += sign_total * sort_sign * v
                                        matrices[(ii, jj)] = M
                                return matrices

                            def build_bar_v3(n, plc, res_func):
                                os_n_l = os_basis(n)
                                os_nm1_l = os_basis(n-1)
                                res_mats_l = res_func(n)
                                total_n_l = DIM**n * len(os_n_l)
                                total_nm1_l = DIM**(n-1) * len(os_nm1_l)

                                def lie_idx(tup):
                                    idx = 0
                                    for t in tup:
                                        idx = idx * DIM + t
                                    return idx

                                M = np.zeros((total_nm1_l, total_n_l))
                                for lie_tup in iproduct(range(DIM), repeat=n):
                                    col_lie = lie_idx(lie_tup)
                                    for ii in range(n):
                                        for jj in range(ii+1, n):
                                            res_mat = res_mats_l[(ii,jj)]
                                            for cc in range(DIM):
                                                coeff = f[lie_tup[ii]][lie_tup[jj]][cc]
                                                if abs(coeff) < 1e-10: continue
                                                if plc == 'at_i':
                                                    nl = list(lie_tup); nl[ii]=cc
                                                    nl = tuple(nl[:jj]+nl[jj+1:])
                                                else:
                                                    nl = list(lie_tup); nl[jj]=cc
                                                    nl = tuple(nl[:ii]+nl[ii+1:])
                                                rl = lie_idx(nl)
                                                for cf in range(len(os_n_l)):
                                                    for rf in range(len(os_nm1_l)):
                                                        rv = res_mat[rf,cf]
                                                        if abs(rv)<1e-10: continue
                                                        M[rl*len(os_nm1_l)+rf, col_lie*len(os_n_l)+cf] += coeff*rv
                                return M

                            rf = lambda n, a=a,b=b,c=c,d=d: compute_res_with_pos_sign(n,a,b,c,d)
                            d2m = build_bar_v3(2, placement, rf)
                            d3m = build_bar_v3(3, placement, rf)
                            comp = d2m @ d3m
                            err = np.max(np.abs(comp))
                            if err < 1e-8:
                                print(f"  *** d^2=0 FOUND: a={a} b={b} c={c} d={d} placement={placement}")
                                found = True

        if not found:
            print("  No 4-parameter sign convention works either.")
            print("  The issue may be in the relabeling/residue computation itself.")
