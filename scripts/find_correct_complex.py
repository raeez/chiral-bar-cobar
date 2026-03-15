#!/usr/bin/env python3
"""Find the correct bar complex that gives Riordan numbers for sl₂.

The expected sl₂ bar cohomology is H^n = R(n+3) = 3, 6, 15, 36, 91, ...
(shifted Riordan numbers, OEIS A005043).

Expected ranks of the differential d_n: B_n → B_{n-1}:
  rank d₁ = 0
  rank d₂ = 0
  rank d₃ = 3   (so H² = 9 - 0 - 3 = 6)
  rank d₄ = 36  (so H³ = 54 - 3 - 36 = 15)

We test several possible complexes:
1. g^{⊗n} ⊗ OS^{n-1}(n) with bracket + Poincaré residue (chiral bar)
2. g^{⊗n} with associative bar (consecutive pairs only)
3. g^{⊗n} ⊗ OS^{n-1}(n) with various signs
4. The CORRECT operadic bar using the Lie operad (= CE complex on Λ^n(g))
"""
import sys
sys.path.insert(0, 'compute/lib')
import numpy as np
from bar_differential import (sl2_structure_constants, verify_jacobi,
                               os_top_basis, poincare_residue_matrix,
                               _express_in_nbc_basis)


def build_chiral_d(dim_g, sc, n, sign_fn=None):
    """Build chiral bar differential: d_n: B_n → B_{n-1}.

    B_n = g^{⊗n} ⊗ OS^{n-1}(C_n)
    Uses ALL pairs (i,j), bracket + Poincaré residue.
    """
    if sign_fn is None:
        sign_fn = lambda i, j, n: 1

    if n <= 2:
        src_os = os_top_basis(n) if n >= 1 else [()]
        tgt_os = os_top_basis(n-1) if n >= 2 else [()]
        sos = len(src_os) if n >= 1 else 1
        tos = len(tgt_os) if n >= 2 else 1
        sdim = dim_g ** n * sos if n >= 1 else 1
        tdim = dim_g ** max(n-1, 0) * tos if n >= 1 else 1
        return np.zeros((tdim, sdim))

    src_os = os_top_basis(n)
    tgt_os = os_top_basis(n-1)
    sos = len(src_os)
    tos = len(tgt_os)
    sdim = dim_g ** n * sos
    tdim = dim_g ** (n-1) * tos

    res_mats = {}
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            res_mats[(i,j)] = poincare_residue_matrix(n, i, j)

    M = np.zeros((tdim, sdim))

    for gi in range(dim_g ** n):
        gens = []
        t = gi
        for _ in range(n):
            gens.append(t % dim_g)
            t //= dim_g
        gens = list(reversed(gens))

        for os_s in range(sos):
            src = gi * sos + os_s

            for i in range(1, n+1):
                for j in range(i+1, n+1):
                    rm = res_mats[(i,j)]
                    for os_t in range(tos):
                        rc = rm[os_t, os_s]
                        if abs(rc) < 1e-10:
                            continue

                        ai, aj = gens[i-1], gens[j-1]
                        for c in range(dim_g):
                            bc = sc[ai, aj, c]
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


def build_assoc_d(dim_g, sc, n):
    """Build ASSOCIATIVE bar differential: d_n: g^{⊗n} → g^{⊗(n-1)}.

    d[a₁|...|aₙ] = Σᵢ₌₁^{n-1} (-1)^{i-1} a₁|...|[aᵢ,aᵢ₊₁]|...|aₙ

    Uses CONSECUTIVE pairs only, NO OS forms.
    """
    if n <= 1:
        return np.zeros((1, dim_g))

    sdim = dim_g ** n
    tdim = dim_g ** (n-1)
    M = np.zeros((tdim, sdim))

    for gi in range(sdim):
        gens = []
        t = gi
        for _ in range(n):
            gens.append(t % dim_g)
            t //= dim_g
        gens = list(reversed(gens))

        for i in range(n-1):  # consecutive pairs (i, i+1), 0-indexed
            ai, ai1 = gens[i], gens[i+1]
            sign = (-1) ** i

            for c in range(dim_g):
                bc = sc[ai, ai1, c]
                if abs(bc) < 1e-10:
                    continue

                tgens = gens[:i] + [c] + gens[i+2:]
                tgi = 0
                for g in tgens:
                    tgi = tgi * dim_g + g

                M[tgi, gi] += sign * bc

    return M


def build_ce_d(dim_g, sc, n):
    """Build CE differential: d_n: Λ^n(g) → Λ^{n-1}(g).

    d(x₁∧...∧xₙ) = Σ_{i<j} (-1)^{i+j} [xᵢ,xⱼ] ∧ x₁ ∧ ... x̂ᵢ ... x̂ⱼ ... ∧ xₙ

    Uses ALL pairs, EXTERIOR algebra (no OS, no repeats).
    """
    from itertools import combinations

    src_basis = list(combinations(range(dim_g), n))
    tgt_basis = list(combinations(range(dim_g), n-1))

    if not src_basis:
        return np.zeros((len(tgt_basis) if tgt_basis else 1, 0))
    if not tgt_basis:
        return np.zeros((1 if n == 1 else 0, len(src_basis)))

    tgt_map = {b: i for i, b in enumerate(tgt_basis)}
    M = np.zeros((len(tgt_basis), len(src_basis)))

    for si, mono in enumerate(src_basis):
        for ii in range(n):
            for jj in range(ii+1, n):
                ai, aj = mono[ii], mono[jj]
                ce_sign = (-1) ** (ii + jj)

                for c in range(dim_g):
                    fc = sc[ai, aj, c]
                    if abs(fc) < 1e-10:
                        continue

                    remaining = [mono[k] for k in range(n) if k != ii and k != jj]
                    combined = sorted([c] + remaining)

                    if len(set(combined)) < len(combined):
                        continue

                    target = tuple(combined)
                    if target not in tgt_map:
                        continue

                    ti = tgt_map[target]

                    # Compute sign from inserting c into remaining
                    insert_list = [c] + remaining
                    sort_sign = 1
                    temp = list(insert_list)
                    for a in range(len(temp)):
                        for b in range(a+1, len(temp)):
                            if temp[a] > temp[b]:
                                temp[a], temp[b] = temp[b], temp[a]
                                sort_sign *= -1

                    M[ti, si] += ce_sign * sort_sign * fc

    return M


def build_all_pairs_tensor_d(dim_g, sc, n, sign_fn):
    """Bar differential on g^{⊗n} (no OS forms), using ALL pairs.

    d[a₁|...|aₙ] = Σ_{i<j} sign_fn(i,j) [aᵢ,aⱼ] (at pos i, remove j) ⊗ rest
    """
    if n <= 1:
        return np.zeros((1, dim_g))

    sdim = dim_g ** n
    tdim = dim_g ** (n-1)
    M = np.zeros((tdim, sdim))

    for gi in range(sdim):
        gens = []
        t = gi
        for _ in range(n):
            gens.append(t % dim_g)
            t //= dim_g
        gens = list(reversed(gens))

        for i in range(n):
            for j in range(i+1, n):
                ai, aj = gens[i], gens[j]

                for c in range(dim_g):
                    bc = sc[ai, aj, c]
                    if abs(bc) < 1e-10:
                        continue

                    tgens = []
                    for k in range(n):
                        if k == i: tgens.append(c)
                        elif k == j: continue
                        else: tgens.append(gens[k])

                    tgi = 0
                    for g in tgens:
                        tgi = tgi * dim_g + g

                    sgn = sign_fn(i+1, j+1, n)  # convert to 1-indexed
                    M[tgi, gi] += sgn * bc

    return M


if __name__ == '__main__':
    names, sc = sl2_structure_constants()
    assert verify_jacobi(names, sc)
    d = len(names)
    print(f"sl₂, dim={d}, generators: {names}")

    print("\n" + "="*60)
    print("Expected bar cohomology (Riordan): H = 3, 6, 15, 36, 91")
    print("Expected ranks: d₂=0, d₃=3, d₄=36, d₅=414")
    print("Chain dims: B₁=3, B₂=9, B₃=54, B₄=486, B₅=5760")
    print("="*60)

    # 1. Chiral bar with various signs
    print("\n--- Chiral bar (g^n ⊗ OS^{n-1}) ---")
    signs = {
        '1': lambda i,j,n: 1,
        '(-1)^{i+j}': lambda i,j,n: (-1)**(i+j),
        '(-1)^{i+j+1}': lambda i,j,n: (-1)**(i+j+1),
        '(-1)^{i-1}': lambda i,j,n: (-1)**(i-1),
    }

    for sname, sfn in signs.items():
        d3 = build_chiral_d(d, sc, 3, sfn)
        r3 = np.linalg.matrix_rank(d3)

        d4 = build_chiral_d(d, sc, 4, sfn)
        r4 = np.linalg.matrix_rank(d4)

        # Check d²
        d3d4 = d3 @ d4
        d2_ok = np.max(np.abs(d3d4)) < 1e-8

        print(f"  sign={sname:20s}: rank(d₃)={r3}, rank(d₄)={r4}, d₃∘d₄=0: {d2_ok}")

    # 2. Associative bar (consecutive pairs, no OS)
    print("\n--- Associative bar (consecutive pairs, no OS) ---")
    for n in range(2, 6):
        dn = build_assoc_d(d, sc, n)
        rn = np.linalg.matrix_rank(dn)
        print(f"  d_{n}: {dn.shape}, rank={rn}")

    # Check d² for associative
    d2a = build_assoc_d(d, sc, 2)
    d3a = build_assoc_d(d, sc, 3)
    d4a = build_assoc_d(d, sc, 4)
    print(f"  d₂∘d₃=0: {np.max(np.abs(d2a @ d3a)) < 1e-8}")
    print(f"  d₃∘d₄=0: {np.max(np.abs(d3a @ d4a)) < 1e-8}")

    # Compute associative bar cohomology
    print("\n  Associative bar cohomology:")
    d_mats = {n: build_assoc_d(d, sc, n) for n in range(1, 6)}
    for n in range(1, 5):
        d_out = d_mats[n]
        d_in = d_mats[n+1]
        r_out = np.linalg.matrix_rank(d_out)
        r_in = np.linalg.matrix_rank(d_in)
        chain_dim = d_out.shape[1]
        h = chain_dim - r_out - r_in
        print(f"    H^{n} = {chain_dim} - {r_out} - {r_in} = {h}")

    # 3. CE complex
    print("\n--- CE complex (Λ^n, all pairs, antisymmetric) ---")
    for n in range(1, d+1):
        dn = build_ce_d(d, sc, n)
        rn = np.linalg.matrix_rank(dn)
        print(f"  d_{n}: {dn.shape}, rank={rn}")

    # 4. All-pairs on g^{⊗n} (no OS, no antisymmetry) with various signs
    print("\n--- All-pairs on g^⊗n (no OS, no antisymmetry) ---")
    for sname, sfn in signs.items():
        d3 = build_all_pairs_tensor_d(d, sc, 3, sfn)
        r3 = np.linalg.matrix_rank(d3)
        d4 = build_all_pairs_tensor_d(d, sc, 4, sfn)
        r4 = np.linalg.matrix_rank(d4)
        d2_ok = np.max(np.abs(d3 @ d4)) < 1e-8
        print(f"  sign={sname:20s}: rank(d₃)={r3}, rank(d₄)={r4}, d₃∘d₄=0: {d2_ok}")

    # Compute all-pairs cohomology with CE sign
    print("\n  All-pairs cohomology with (-1)^{i+j} sign:")
    sfn = lambda i,j,n: (-1)**(i+j)
    d_mats = {n: build_all_pairs_tensor_d(d, sc, n, sfn) for n in range(1, 6)}
    for n in range(1, 5):
        d_out = d_mats[n]
        d_in = d_mats[n+1]
        r_out = np.linalg.matrix_rank(d_out)
        r_in = np.linalg.matrix_rank(d_in)
        chain_dim = d_out.shape[1]
        h = chain_dim - r_out - r_in
        print(f"    H^{n} = {chain_dim} - {r_out} - {r_in} = {h}")
