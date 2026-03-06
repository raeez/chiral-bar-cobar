#!/usr/bin/env python3
"""Pure Python chiral bar cohomology (no numpy).

Computes the chiral bar complex for finite-dim Lie algebras:
  B^n = g^{tensor n} tensor OS^{n-1}(C_n)
  d uses Lie bracket + OS residue maps.

If this gives Riordan numbers for sl_2 (3, 6, 15, 36, 91),
it validates the chiral bar complex formulation and can be
extended to vertex algebras (Virasoro, W_3).
"""
from fractions import Fraction
from itertools import combinations
from math import factorial
import sys

F = Fraction  # shorthand

# ============================================================
# OS algebra: NBC basis and residue maps
# ============================================================

def edges_Kn(n):
    """All edges (i,j) with 1 <= i < j <= n, lex ordered."""
    return [(i, j) for i in range(1, n+1) for j in range(i+1, n+1)]

def nbc_basis(n, k):
    """NBC (no-broken-circuit) basis for OS^k(C_n).
    Returns list of k-tuples of edges, sorted lexicographically.
    For k=n-1: dim = (n-1)!.
    """
    if k == 0:
        return [()]
    if n <= 1:
        return []

    all_edges = edges_Kn(n)
    bcs = broken_circuits(n)

    basis = []
    for combo in combinations(all_edges, k):
        edge_set = frozenset(combo)
        is_nbc = all(not bc.issubset(edge_set) for bc in bcs)
        if is_nbc:
            basis.append(tuple(sorted(combo)))
    return basis

def broken_circuits(n):
    """Broken circuits for K_n with lex edge ordering."""
    all_edges = edges_Kn(n)
    edge_order = {e: i for i, e in enumerate(all_edges)}

    bcs = []
    # All triangles give broken circuits
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                triangle = [(i,j), (i,k), (j,k)]
                max_e = max(triangle, key=lambda e: edge_order[e])
                bc = frozenset(triangle) - {max_e}
                bcs.append(bc)
    return bcs

def perm_sign(perm):
    """Sign of a permutation (list of indices)."""
    n = len(perm)
    inv = sum(1 for i in range(n) for j in range(i+1, n) if perm[i] > perm[j])
    return (-1) ** inv

def residue_matrices(n):
    """Compute all residue maps Res_{pq}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1}).
    Returns dict: (p,q) -> matrix (list of lists of Fraction).
    """
    if n <= 1:
        return {}

    src_basis = nbc_basis(n, n-1)
    tgt_basis = nbc_basis(n-1, n-2)
    dim_src = len(src_basis)
    dim_tgt = len(tgt_basis)
    tgt_idx = {b: i for i, b in enumerate(tgt_basis)}

    bcs_target = broken_circuits(n-1)

    result = {}
    for p in range(1, n+1):
        for q in range(p+1, n+1):
            M = [[F(0)] * dim_src for _ in range(dim_tgt)]

            # Relabeling after merging p,q -> p; remove q
            # Points: {1,...,n} \ {q}, with p representing merged point
            # Relabel to {1,...,n-1} preserving order
            old_pts = [i for i in range(1, n+1) if i != q]
            relabel = {old: new for new, old in enumerate(old_pts, 1)}

            for col, src_edges in enumerate(src_basis):
                if (p, q) not in src_edges:
                    continue

                pos = list(src_edges).index((p, q))
                sign = (-1) ** pos

                remaining = [e for e in src_edges if e != (p, q)]
                relabeled = []
                degen = False
                extra_sign = 1
                for ei, ej in remaining:
                    ni = relabel.get(ei, relabel.get(p) if ei == q else None)
                    nj = relabel.get(ej, relabel.get(p) if ej == q else None)
                    if ni is None:
                        ni = relabel[p] if ei == q else relabel[ei]
                    if nj is None:
                        nj = relabel[p] if ej == q else relabel[ej]
                    if ni == nj:
                        degen = True
                        break
                    if ni > nj:
                        ni, nj = nj, ni
                        extra_sign *= -1
                    relabeled.append((ni, nj))

                if degen:
                    continue

                total_sign = sign * extra_sign
                # Express relabeled edges in NBC basis
                coeffs = reduce_to_nbc(relabeled, n-1, tgt_basis, tgt_idx, bcs_target)
                for row, c in coeffs.items():
                    M[row][col] += F(total_sign) * c

            result[(p, q)] = M
    return result

def reduce_to_nbc(edges, n, basis, basis_idx, bcs):
    """Reduce a wedge product of edges to NBC basis using Arnold relations."""
    edge_order = {e: i for i, e in enumerate(edges_Kn(n))}

    # Check for repeated edges
    if len(set(edges)) < len(edges):
        return {}

    sorted_edges = tuple(sorted(edges))
    # Compute sign of sorting
    idx_map = {e: i for i, e in enumerate(edges)}
    perm = [idx_map[e] for e in sorted_edges]
    sort_sign = perm_sign(perm)

    forms = {sorted_edges: F(sort_sign)}

    for _iter in range(50):
        new_forms = {}
        changed = False
        for edge_t, coeff in forms.items():
            if coeff == 0:
                continue
            edge_set = frozenset(edge_t)

            found_bc = None
            for bc in bcs:
                if bc.issubset(edge_set):
                    found_bc = bc
                    break

            if found_bc is None:
                new_forms[edge_t] = new_forms.get(edge_t, F(0)) + coeff
                continue

            changed = True
            bc_edges = sorted(found_bc, key=lambda e: edge_order[e])

            # Find the triangle
            verts = set()
            for e in bc_edges:
                verts.update(e)
            # Find missing edge to complete triangle
            missing = None
            for e in edges_Kn(n):
                if e not in found_bc and set(e).issubset(verts):
                    missing = e
                    break
            if missing is None:
                new_forms[edge_t] = new_forms.get(edge_t, F(0)) + coeff
                continue

            i, j, k = sorted(verts)
            e_ij, e_ik, e_jk = (i,j), (i,k), (j,k)
            bc_set = frozenset(bc_edges)

            # Arnold: eta_ij^eta_jk - eta_ij^eta_ik + eta_ik^eta_jk = 0
            if bc_set == frozenset([e_ij, e_ik]):
                # eta_ij^eta_ik = eta_ij^eta_jk + eta_ik^eta_jk
                replacements = [(e_ij, e_jk, 1), (e_ik, e_jk, 1)]
            elif bc_set == frozenset([e_ij, e_jk]):
                # eta_ij^eta_jk = eta_ij^eta_ik - eta_ik^eta_jk
                replacements = [(e_ij, e_ik, 1), (e_ik, e_jk, -1)]
            elif bc_set == frozenset([e_ik, e_jk]):
                # eta_ik^eta_jk = eta_ij^eta_ik - eta_ij^eta_jk
                replacements = [(e_ij, e_ik, 1), (e_ij, e_jk, -1)]
            else:
                new_forms[edge_t] = new_forms.get(edge_t, F(0)) + coeff
                continue

            # Find positions of BC edges in edge_t
            edge_list = list(edge_t)
            pos_bc = [edge_list.index(e) for e in bc_edges]
            bc_sign = 1 if pos_bc[0] < pos_bc[1] else -1

            other = [e for e in edge_t if e not in bc_set]

            for new_e1, new_e2, rel_sign in replacements:
                new_list = other + [new_e1, new_e2]
                if len(set(new_list)) < len(new_list):
                    continue  # degenerate
                new_sorted = tuple(sorted(new_list))
                # Sign from reordering
                temp_list = [new_e1, new_e2] + list(other)
                if len(set(temp_list)) < len(temp_list):
                    continue
                idx_map2 = {e: i for i, e in enumerate(temp_list)}
                p2 = [idx_map2[e] for e in new_sorted]
                psign = perm_sign(p2)
                if psign == 0:
                    continue
                total = coeff * F(bc_sign * rel_sign * psign)
                new_forms[new_sorted] = new_forms.get(new_sorted, F(0)) + total

        forms = {k: v for k, v in new_forms.items() if v != 0}
        if not changed:
            break

    result = {}
    for edge_t, coeff in forms.items():
        if coeff == 0:
            continue
        if edge_t in basis_idx:
            idx = basis_idx[edge_t]
            result[idx] = result.get(idx, F(0)) + coeff
    return result

# ============================================================
# Lie algebra bar complex
# ============================================================

def sl2_bracket():
    """sl_2 structure constants. Basis: e=0, h=1, f=2.
    [e,f]=h, [h,e]=2e, [h,f]=-2f."""
    f = {}
    f[(0,2,1)] = F(1); f[(2,0,1)] = F(-1)
    f[(1,0,0)] = F(2); f[(0,1,0)] = F(-2)
    f[(1,2,2)] = F(-2); f[(2,1,2)] = F(2)
    return f, 3

def sl3_bracket():
    """sl_3 structure constants. dim=8."""
    f = {}
    H1,H2,E1,E2,E3,F1,F2,F3 = range(8)
    A = [[2,-1],[-1,2]]

    def sb(a,b,c,v):
        f[(a,b,c)] = f.get((a,b,c),F(0)) + F(v)
        f[(b,a,c)] = f.get((b,a,c),F(0)) - F(v)

    for i,hi in enumerate([H1,H2]):
        for j,ej in enumerate([E1,E2]):
            if A[i][j] != 0: sb(hi,ej,ej,A[i][j])
        for j,fj in enumerate([F1,F2]):
            if A[i][j] != 0: sb(hi,fj,fj,-A[i][j])

    sb(E1,F1,H1,1); sb(E2,F2,H2,1)
    sb(E1,E2,E3,1); sb(F2,F1,F3,1)
    sb(H1,E3,E3,1); sb(H2,E3,E3,1)
    sb(H1,F3,F3,-1); sb(H2,F3,F3,-1)
    sb(E3,F1,E2,-1); sb(E3,F2,E1,1)
    sb(E3,F3,H1,1); sb(E3,F3,H2,1)
    sb(E1,F3,F2,-1); sb(E2,F3,F1,1)
    return f, 8

def chiral_bar_differential(bracket, dim_g, n):
    """Build d: B^n -> B^{n-1} for the chiral bar complex.

    B^n = g^{tensor n} tensor OS^{n-1}(C_n)
    Differential contracts pairs (p,q) using Lie bracket + OS residue.
    """
    if n <= 1:
        return [], 0, 0

    src_os = nbc_basis(n, n-1)
    tgt_os = nbc_basis(n-1, n-2)
    dim_os_src = len(src_os)
    dim_os_tgt = len(tgt_os)

    src_dim = dim_g**n * dim_os_src
    tgt_dim = dim_g**(n-1) * dim_os_tgt

    # Get residue maps
    res = residue_matrices(n)

    # Build matrix
    M = [[F(0)] * src_dim for _ in range(tgt_dim)]

    def encode_tensor(gens, os_idx, dim_g_val, os_dim):
        """Encode (generator tuple, OS index) as single integer."""
        t = 0
        for k in range(len(gens)-1, -1, -1):
            t = t * dim_g_val + gens[k]
        return t * os_dim + os_idx

    # Iterate over source basis elements
    for src_t in range(dim_g**n):
        gens = []
        temp = src_t
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g

        for os_src in range(dim_os_src):
            col = src_t * dim_os_src + os_src

            for p in range(1, n+1):
                for q in range(p+1, n+1):
                    res_M = res.get((p,q))
                    if res_M is None:
                        continue

                    for os_tgt in range(dim_os_tgt):
                        res_coeff = res_M[os_tgt][os_src]
                        if res_coeff == 0:
                            continue

                        a_p = gens[p-1]
                        a_q = gens[q-1]

                        for c in range(dim_g):
                            bc = bracket.get((a_p, a_q, c), F(0))
                            if bc == 0:
                                continue

                            # Build target: replace p with bracket, remove q
                            tgt_gens = list(gens)
                            tgt_gens[p-1] = c
                            del tgt_gens[q-1]

                            # Sign: (-1)^{q-p-1}
                            sign = F((-1)**(q-p-1))

                            tgt_t = 0
                            for k in range(len(tgt_gens)-1, -1, -1):
                                tgt_t = tgt_t * dim_g + tgt_gens[k]
                            row = tgt_t * dim_os_tgt + os_tgt

                            M[row][col] += sign * bc * res_coeff

    return M, src_dim, tgt_dim

def matrix_rank_exact(M):
    """Exact rank using Fraction arithmetic and Gaussian elimination."""
    if not M or not M[0]:
        return 0
    m = len(M)
    n = len(M[0])
    A = [row[:] for row in M]
    rank = 0
    for col in range(n):
        pivot = None
        for row in range(rank, m):
            if A[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        pv = A[rank][col]
        for row in range(m):
            if row != rank and A[row][col] != 0:
                factor = A[row][col] / pv
                for c2 in range(n):
                    A[row][c2] -= factor * A[rank][c2]
        rank += 1
    return rank

def verify_d_squared(bracket, dim_g, n):
    """Check d^2 = 0 for the chiral bar differential."""
    M1, _, _ = chiral_bar_differential(bracket, dim_g, n)
    M2, _, _ = chiral_bar_differential(bracket, dim_g, n-1)
    if not M1 or not M2:
        return True
    # Compute M2 * M1
    rows2 = len(M2)
    cols1 = len(M1[0])
    inner = len(M1)
    assert inner == len(M2[0]), f"Dimension mismatch: {inner} vs {len(M2[0])}"

    max_err = F(0)
    for i in range(rows2):
        for j in range(cols1):
            val = sum(M2[i][k] * M1[k][j] for k in range(inner))
            if abs(val) > max_err:
                max_err = abs(val)
    return max_err == 0

def compute_cohomology(bracket, dim_g, name, max_deg=5):
    """Compute chiral bar cohomology of a Lie algebra."""
    print(f"\n{'='*60}")
    print(f"CHIRAL BAR COHOMOLOGY: {name} (dim={dim_g})")
    print(f"{'='*60}")

    # OS basis dims
    print("OS dims:", {n: factorial(n-1) for n in range(1, max_deg+2)})

    ranks = {}
    chain_dims = {}
    for deg in range(1, max_deg+2):
        os_dim = factorial(deg-1)
        chain_dims[deg] = dim_g**deg * os_dim
    print("Chain dims:", {k:v for k,v in chain_dims.items() if k <= max_deg+1})

    for deg in range(2, max_deg+2):
        sd = chain_dims[deg]
        td = chain_dims[deg-1]
        if sd > 50000:
            print(f"  d_{deg}: SKIP (dim={sd} too large)")
            continue
        print(f"  Building d_{deg}: {sd} -> {td} ...", end="", flush=True)
        M, _, _ = chiral_bar_differential(bracket, dim_g, deg)
        r = matrix_rank_exact(M)
        ranks[deg] = r
        print(f" rank={r}")

    # Verify d^2=0
    for deg in range(3, max_deg+2):
        if deg in ranks and deg-1 in ranks:
            ok = verify_d_squared(bracket, dim_g, deg)
            print(f"  d^2=0 check (d_{deg-1}*d_{deg}): {'OK' if ok else 'FAIL!'}")

    # Cohomology
    print(f"\nBar cohomology:")
    cohom = {}
    for deg in range(1, max_deg+1):
        dim_n = chain_dims[deg]
        r_out = ranks.get(deg, 0)
        r_in = ranks.get(deg+1, 0)
        H = dim_n - r_out - r_in
        cohom[deg] = H
        print(f"  H^{deg} = {dim_n} - {r_out} - {r_in} = {H}")

    return cohom


# ============================================================
# Quick OS verification
# ============================================================

def verify_os():
    print("OS algebra verification:")
    for n in range(2, 6):
        b = nbc_basis(n, n-1)
        expected = factorial(n-1)
        print(f"  OS^{n-1}(C_{n}): dim={len(b)} (expected {expected}) {'OK' if len(b)==expected else 'FAIL'}")

    # Residue maps for n=3
    print("\nResidue maps for n=3:")
    res3 = residue_matrices(3)
    for (p,q), M in sorted(res3.items()):
        flat = [M[r][c] for r in range(len(M)) for c in range(len(M[0]))]
        print(f"  Res_D{p}{q}: {flat}")

    # Check d^2 = 0 for sl_2 at degree 3
    br, dim = sl2_bracket()
    print(f"\nd^2=0 check for sl_2, deg 3:", verify_d_squared(br, dim, 3))


if __name__ == "__main__":
    verify_os()

    # sl_2: expected Riordan numbers R(n+3) = 3, 6, 15, 36, 91
    br2, d2 = sl2_bracket()
    cohom2 = compute_cohomology(br2, d2, "sl_2", max_deg=5)

    print("\nExpected (Riordan R(n+3)): 3, 6, 15, 36, 91")
    print("Got:", [cohom2.get(i,0) for i in range(1,6)])

    # sl_3: if feasible
    br3, d3 = sl3_bracket()
    cohom3 = compute_cohomology(br3, d3, "sl_3", max_deg=4)
