#!/usr/bin/env python3
"""Debug d^2 = 0 for bar differential by hand-tracing small cases.

For sl_2, trace d_3: B_4 -> B_3 and d_2: B_3 -> B_2 to find the correct sign convention.

Key insight: the bar complex for a Lie algebra IS the Chevalley-Eilenberg complex.
The CE differential is:
  d(a_1 ∧ ... ∧ a_n) = Σ_{i<j} (-1)^{i+j} [a_i, a_j] ∧ a_1 ∧ ... â_i ... â_j ... ∧ a_n

But we're NOT using exterior powers — we're using g^{⊗n} ⊗ OS^{n-1}(n).
The OS form ω encodes the wedge structure. The Poincaré residue handles the
"contraction" part. So the sign (-1)^{i+j} from CE should appear.

But wait — since generators are in degree 0 (or degree 1 after desuspension?),
the Koszul sign differs. Let me think about what the CORRECT sign is.

Plan:
1. Compute with CE sign (-1)^{i+j}
2. Compute with sign (-1)^{i+j+1}
3. Compute with sign 1 (no extra sign beyond OS)
4. Also test: what if we DON'T put a Koszul sign from the OS form extraction?
   (i.e., drop the (-1)^pos from poincare_residue_matrix)
"""
import sys
sys.path.insert(0, 'compute/lib')
import numpy as np
from bar_differential import (sl2_structure_constants, verify_jacobi,
                               os_basis, os_top_basis, poincare_residue_matrix,
                               _express_in_nbc_basis)

def print_os_basis(n):
    for d in range(n):
        b = os_basis(n, d)
        print(f"  OS^{d}({n}): {b}")

def print_residue_matrices(n):
    src = os_top_basis(n)
    tgt = os_top_basis(n-1)
    print(f"\n  Source OS^{n-1}({n}): {src}")
    print(f"  Target OS^{n-2}({n-1}): {tgt}")
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            M = poincare_residue_matrix(n, i, j)
            print(f"  Res_{{{i}{j}}}: {M.tolist()}")

def build_bar_diff(dim_g, sc, n, sign_fn, use_os_sign=True):
    """Build bar differential with configurable sign.

    sign_fn(i, j, n) = extra sign beyond OS extraction sign
    use_os_sign: if False, drop the (-1)^pos from OS extraction
    """
    if n <= 2:
        if n == 2:
            return np.zeros((dim_g, dim_g**2))
        return np.zeros((1, dim_g))

    src_os = os_top_basis(n)
    tgt_os = os_top_basis(n - 1)
    sos = len(src_os)
    tos = len(tgt_os)
    sdim = dim_g ** n * sos
    tdim = dim_g ** (n - 1) * tos

    # Rebuild residue matrices with option to drop OS sign
    res_mats = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if use_os_sign:
                res_mats[(i, j)] = poincare_residue_matrix(n, i, j)
            else:
                res_mats[(i, j)] = _poincare_residue_no_sign(n, i, j, src_os, tgt_os)

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
                            for k in range(n):
                                if k == i-1: tgens.append(c)
                                elif k == j-1: continue
                                else: tgens.append(gens[k])

                            tgi = 0
                            for g in tgens:
                                tgi = tgi * dim_g + g
                            tgt = tgi * tos + os_t

                            sgn = sign_fn(i, j, n)
                            M[tgt, src] += sgn * bc * rc

    return M


def _poincare_residue_no_sign(n, i, j, src_basis, tgt_basis):
    """Poincare residue without the (-1)^pos sign from extraction."""
    edge_ij = (min(i, j), max(i, j))
    M = np.zeros((len(tgt_basis), len(src_basis)))

    def relabel(edge, mi, mj):
        a, b = edge
        if a == mj: a = mi
        if b == mj: b = mi
        if a > mj: a -= 1
        if b > mj: b -= 1
        if a > b: a, b = b, a
        if a == b: return None
        return (a, b)

    for s_idx, mono in enumerate(src_basis):
        if edge_ij not in mono:
            continue
        pos = mono.index(edge_ij)
        # NO sign from position
        remaining = list(mono[:pos]) + list(mono[pos + 1:])
        relabeled = []
        valid = True
        for edge in remaining:
            new_edge = relabel(edge, min(i, j), max(i, j))
            if new_edge is None:
                valid = False
                break
            relabeled.append(new_edge)
        if not valid:
            continue

        relabeled_sorted = tuple(sorted(relabeled))
        perm_sign = 1
        temp = list(relabeled)
        for a in range(len(temp)):
            for b in range(a + 1, len(temp)):
                if temp[a] > temp[b]:
                    temp[a], temp[b] = temp[b], temp[a]
                    perm_sign *= -1

        if relabeled_sorted in tgt_basis:
            t_idx = tgt_basis.index(relabeled_sorted)
            M[t_idx, s_idx] = perm_sign  # no (-1)^pos
        else:
            coeff = _express_in_nbc_basis(relabeled_sorted, n - 1, len(remaining), tgt_basis)
            for t_idx, c in coeff.items():
                M[t_idx, s_idx] += perm_sign * c

    return M


def check_d2(dim_g, sc, sign_fn, use_os_sign=True, max_n=5):
    """Check d^2 = 0 for all pairs."""
    results = {}
    for n in range(3, max_n + 1):
        d_n = build_bar_diff(dim_g, sc, n, sign_fn, use_os_sign)
        d_nm1 = build_bar_diff(dim_g, sc, n - 1, sign_fn, use_os_sign)
        prod = d_nm1 @ d_n
        err = np.max(np.abs(prod))
        results[n] = err < 1e-8
    return results


if __name__ == '__main__':
    names, sc = sl2_structure_constants()
    assert verify_jacobi(names, sc)
    d = len(names)

    print("OS bases:")
    for n in range(2, 6):
        print_os_basis(n)

    print("\nResidue matrices:")
    for n in range(3, 6):
        print(f"\nn = {n}:")
        print_residue_matrices(n)

    # Try many sign conventions
    signs = {
        '1': lambda i,j,n: 1,
        '(-1)^{i+j}': lambda i,j,n: (-1)**(i+j),
        '(-1)^{i+j+1}': lambda i,j,n: (-1)**(i+j+1),
        '(-1)^{i-1}': lambda i,j,n: (-1)**(i-1),
        '(-1)^{j-1}': lambda i,j,n: (-1)**(j-1),
        '(-1)^{j-i-1}': lambda i,j,n: (-1)**(j-i-1),
        '(-1)^{j-i}': lambda i,j,n: (-1)**(j-i),
    }

    print("\n\n=== Testing with OS extraction sign (original) ===")
    for sname, sfn in signs.items():
        res = check_d2(d, sc, sfn, use_os_sign=True)
        ok = all(res.values())
        detail = ", ".join(f"d_{n-1}d_{n}={'ok' if v else 'FAIL'}" for n, v in res.items())
        print(f"  {sname:20s}: {detail}  {'PASS' if ok else ''}")

    print("\n=== Testing WITHOUT OS extraction sign ===")
    for sname, sfn in signs.items():
        res = check_d2(d, sc, sfn, use_os_sign=False)
        ok = all(res.values())
        detail = ", ".join(f"d_{n-1}d_{n}={'ok' if v else 'FAIL'}" for n, v in res.items())
        print(f"  {sname:20s}: {detail}  {'PASS' if ok else ''}")

    # Also try: use CE convention directly (no OS, just antisymmetrize)
    # The CE differential on Λ^n(g) is:
    # d(x_1∧...∧x_n) = Σ_{i<j} (-1)^{i+j} [x_i,x_j] ∧ x_1 ∧ ... x̂_i ... x̂_j ... ∧ x_n
    # Let's build this DIRECTLY to verify our expected cohomology
    print("\n\n=== Direct CE computation (no OS) ===")
    from itertools import combinations

    def ce_differential(dim_g, sc, n):
        """Build CE differential d: Λ^n(g) → Λ^{n-1}(g)."""
        if n <= 1:
            return np.zeros((1, dim_g))

        src_basis = list(combinations(range(dim_g), n))
        tgt_basis = list(combinations(range(dim_g), n - 1))

        src_map = {b: i for i, b in enumerate(src_basis)}
        tgt_map = {b: i for i, b in enumerate(tgt_basis)}

        M = np.zeros((len(tgt_basis), len(src_basis)))

        for s_idx, mono in enumerate(src_basis):
            for ii in range(n):
                for jj in range(ii + 1, n):
                    a_i = mono[ii]
                    a_j = mono[jj]

                    ce_sign = (-1) ** (ii + jj)

                    # [a_i, a_j] = Σ_c f^{ij}_c · c
                    for c in range(dim_g):
                        fc = sc[a_i, a_j, c]
                        if abs(fc) < 1e-10:
                            continue

                        # Build target: c ∧ x_1 ∧ ... x̂_i ... x̂_j ... ∧ x_n
                        remaining = [mono[k] for k in range(n) if k != ii and k != jj]
                        target = sorted([c] + remaining)

                        # Check for repeats
                        if len(set(target)) < len(target):
                            continue

                        target_tuple = tuple(target)
                        if target_tuple not in tgt_map:
                            continue

                        # Sign from sorting c into position
                        # c is inserted among the remaining elements
                        combined = [c] + remaining
                        # Count inversions to sort
                        sort_sign = 1
                        temp = list(combined)
                        for a in range(len(temp)):
                            for b in range(a + 1, len(temp)):
                                if temp[a] > temp[b]:
                                    temp[a], temp[b] = temp[b], temp[a]
                                    sort_sign *= -1

                        t_idx = tgt_map[target_tuple]
                        M[t_idx, s_idx] += ce_sign * sort_sign * fc

        return M

    # Compute CE cohomology for sl2
    print(f"dim sl2 = {d}")
    ce_dims = {}
    for n in range(1, d + 1):
        from math import comb
        print(f"  Λ^{n}(sl₂): dim = {comb(d, n)}")

    # Check d^2 = 0
    for n in range(2, d + 1):
        dn = ce_differential(d, sc, n)
        dnm1 = ce_differential(d, sc, n - 1)
        prod = dnm1 @ dn
        print(f"  d_{n-1}∘d_{n}: max|prod| = {np.max(np.abs(prod)):.2e}")

    # Compute CE cohomology
    d_mats = {}
    for n in range(1, d + 2):
        d_mats[n] = ce_differential(d, sc, n)

    print("\nCE cohomology of sl₂:")
    for n in range(1, d + 1):
        d_out = d_mats[n]
        d_in = d_mats[n + 1] if n + 1 in d_mats else np.zeros((d_mats[n].shape[1], 1))

        rank_out = np.linalg.matrix_rank(d_out)
        rank_in = np.linalg.matrix_rank(d_in)
        chain_dim = d_out.shape[1]
        h = chain_dim - rank_out - rank_in
        print(f"  H^{n}_CE = {h}  (chain={chain_dim}, ker={chain_dim-rank_out}, im={rank_in})")

    # NOW: the bar complex for a Lie algebra g is NOT the CE complex.
    # It's the TENSOR algebra (not exterior algebra) with OS forms.
    # B_n = g^{⊗n} ⊗ OS^{n-1}(n), d uses bracket + Poincaré residue.
    # This should give bar cohomology = Ext^*_{Ug}(k, k), which for sl2 is:
    # H^1 = 3, H^2 = 6, H^3 = 15, H^4 = 36, ...
    # (These are NOT the CE cohomology dimensions 0, 0, 1)

    print("\n\n=== Detailed d_3 trace for sl₂ ===")
    # d_3: B_3 → B_2
    # B_3 = g^{⊗3} ⊗ OS^2(3), dim = 3^3 × 2 = 54
    # B_2 = g^{⊗2} ⊗ OS^1(2), dim = 3^2 × 1 = 9

    os3 = os_top_basis(3)
    os2 = os_top_basis(2)
    print(f"OS^2(3) basis: {os3}")
    print(f"OS^1(2) basis: {os2}")

    # Residue matrices for n=3
    print("\nResidue matrices for n=3:")
    for i in range(1, 4):
        for j in range(i + 1, 4):
            rm = poincare_residue_matrix(3, i, j)
            print(f"  Res_{{{i}{j}}}: {rm.tolist()}")

    # Let's trace through a specific element:
    # e.g., e_0 ⊗ e_0 ⊗ e_0 ⊗ ω_s where ω_s is an OS basis element
    # With sl2 structure: [e,h] = -2e, [e,f] = h, [h,f] = -2f
    # names = ['e', 'f', 'h'] typically? Let me check
    print(f"\nGenerator names: {names}")
    print(f"Structure constants (nonzero):")
    for a in range(d):
        for b in range(d):
            for c in range(d):
                if abs(sc[a,b,c]) > 1e-10:
                    print(f"  [{names[a]}, {names[b]}] -> {sc[a,b,c]:.0f} * {names[c]}")
