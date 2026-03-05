#!/usr/bin/env python3
"""
Bar cohomology computation for chiral algebras.

The chiral bar complex B̄^n has:
- n+1 factors from A = g ⊕ ℂ|0⟩ (including vacuum)
- n log-forms from OS^n(n+1) = H^n(Conf_{n+1}(ℂ))

The differential d: B̄^n → B̄^{n-1} uses the chiral bracket:
  μ^ch(a,b) = [a,b] + k·(a,b)·|0⟩

d(v₁⊗...⊗v_{n+1} ⊗ ω) = Σ_{i<j} sign · v₁⊗...⊗μ^ch(vᵢ,vⱼ)⊗...⊗v̂ⱼ⊗...⊗v_{n+1} ⊗ C_{ij}(ω)

We verify d² = 0 and compute homology H_n = ker(d_n)/im(d_{n+1}).
"""

import numpy as np
from itertools import combinations, product as iterproduct
from math import factorial, comb
import sys

# ========================================
# Lie algebra structure constants
# ========================================

def sl2_data():
    """sl₂ structure constants and Killing form. Basis: e(0), f(1), h(2)."""
    d = 3
    # [e,f]=h, [h,e]=2e, [h,f]=-2f
    f = np.zeros((d, d, d))
    f[0,1,2] = 1; f[1,0,2] = -1    # [e,f]=h
    f[2,0,0] = 2; f[0,2,0] = -2    # [h,e]=2e
    f[2,1,1] = -2; f[1,2,1] = 2    # [h,f]=-2f
    # Killing form: (e,f)=1, (h,h)=2
    kf = np.zeros((d, d))
    kf[0,1] = 1; kf[1,0] = 1; kf[2,2] = 2
    return d, f, kf

def sl3_data():
    """sl₃ structure constants. Basis: H1,H2,E1,E2,E3,F1,F2,F3."""
    d = 8
    f = np.zeros((d, d, d))
    # See bar_cohomology_v3.py for full structure constants
    # H1=0, H2=1, E1=2, E2=3, E3=4, F1=5, F2=6, F3=7
    A = np.array([[2,-1],[-1,2]])
    # [Hi, Ej] = Aij*Ej
    f[0,2,2]=2; f[2,0,2]=-2; f[0,3,3]=-1; f[3,0,3]=1
    f[1,2,2]=-1; f[2,1,2]=1; f[1,3,3]=2; f[3,1,3]=-2
    f[0,4,4]=1; f[4,0,4]=-1; f[1,4,4]=1; f[4,1,4]=-1
    # [Hi, Fj] = -Aij*Fj
    f[0,5,5]=-2; f[5,0,5]=2; f[0,6,6]=1; f[6,0,6]=-1
    f[1,5,5]=1; f[5,1,5]=-1; f[1,6,6]=-2; f[6,1,6]=2
    f[0,7,7]=-1; f[7,0,7]=1; f[1,7,7]=-1; f[7,1,7]=1
    # [Ei, Fj]
    f[2,5,0]=1; f[5,2,0]=-1    # [E1,F1]=H1
    f[3,6,1]=1; f[6,3,1]=-1    # [E2,F2]=H2
    f[2,3,4]=1; f[3,2,4]=-1    # [E1,E2]=E3
    f[6,5,7]=1; f[5,6,7]=-1    # [F2,F1]=F3
    f[2,7,6]=-1; f[7,2,6]=1    # [E1,F3]=-F2
    f[3,7,5]=1; f[7,3,5]=-1    # [E2,F3]=F1
    f[4,5,3]=-1; f[5,4,3]=1    # [E3,F1]=-E2
    f[4,6,2]=1; f[6,4,2]=-1    # [E3,F2]=E1
    f[4,7,0]=1; f[7,4,0]=-1    # [E3,F3]=H1+H2
    f[4,7,1]=1; f[7,4,1]=-1
    # Killing form: normalized so long roots have (Eα, F_α) = 1
    kf = np.zeros((d, d))
    kf[0,0] = 2; kf[0,1] = -1; kf[1,0] = -1; kf[1,1] = 2  # Cartan
    kf[2,5] = 1; kf[5,2] = 1  # (E1,F1)
    kf[3,6] = 1; kf[6,3] = 1  # (E2,F2)
    kf[4,7] = 1; kf[7,4] = 1  # (E3,F3)
    return d, f, kf

def verify_jacobi(d, f):
    """Verify Jacobi identity."""
    max_err = 0
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for g in range(d):
                    val = 0
                    for e in range(d):
                        val += f[b,c,e]*f[a,e,g] + f[c,a,e]*f[b,e,g] + f[a,b,e]*f[c,e,g]
                    max_err = max(max_err, abs(val))
    return max_err < 1e-10

# ========================================
# NBC basis for OS algebra
# ========================================

def nbc_basis(n, k):
    """
    NBC basis for OS^k(n) = H^k(Conf_n(ℂ)).
    Returns list of sorted edge tuples.
    n: number of points (1-indexed: 1,...,n)
    k: form degree
    """
    if k == 0:
        return [()]
    if n <= 1 or k >= n:
        return [] if k > 0 else [()]

    # All edges of K_n
    edges = [(i,j) for i in range(1, n+1) for j in range(i+1, n+1)]

    # Broken circuits from 3-cycles (Whitney: these generate all BCs)
    broken_circuits = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for kk in range(j+1, n+1):
                # Cycle: (i,j), (j,kk), (i,kk). Largest edge = (j,kk) or (i,kk)?
                # Lex order: (i,j) < (i,kk) < (j,kk) since i<j<kk
                # Largest = (j,kk). BC = {(i,j), (i,kk)}
                broken_circuits.append(frozenset([(i,j), (i,kk)]))

    # NBC: k-subsets of edges containing no broken circuit
    basis = []
    for subset in combinations(edges, k):
        subset_set = frozenset(subset)
        is_nbc = True
        for bc in broken_circuits:
            if bc.issubset(subset_set):
                is_nbc = False
                break
        if is_nbc:
            basis.append(tuple(sorted(subset)))

    return basis

# ========================================
# Arnold reduction: express a monomial in NBC basis
# ========================================

def arnold_reduce(edges_with_sign, n, k, target_basis):
    """
    Express a signed monomial (sign, sorted_edges) as a linear combination
    of NBC basis elements using Arnold relations.

    Returns dict: {basis_index: coefficient}
    """
    # edges_with_sign: list of (sign, sorted_edge_tuple)
    # Process iteratively until all monomials are in NBC form

    result = {}
    queue = list(edges_with_sign)  # [(sign, edge_tuple), ...]

    max_iterations = 1000
    iteration = 0

    while queue and iteration < max_iterations:
        iteration += 1
        sign, edges = queue.pop()

        if abs(sign) < 1e-15:
            continue

        edges = tuple(sorted(edges))

        # Check if it's an NBC element
        bc_found = False
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for kk in range(j+1, n+1):
                    # BC = {(i,j), (i,kk)}
                    if (i,j) in edges and (i,kk) in edges:
                        # Found broken circuit. Apply Arnold relation.
                        # Arnold: ω_{ij}∧ω_{ik} = ω_{ij}∧ω_{jk} - ω_{ik}∧ω_{jk}
                        # Replace {(i,j),(i,kk)} with:
                        # Term 1: replace (i,kk) with (j,kk)
                        # Term 2: -(replace (i,j) with (j,kk))

                        edge_list = list(edges)
                        pos_ij = edge_list.index((i,j))
                        pos_ik = edge_list.index((i,kk))

                        # Need to compute sign from moving edges to adjacent positions
                        # and applying the Arnold relation.
                        #
                        # The monomial is: ...∧ω_{ij}∧...∧ω_{ik}∧...
                        # We need: ω_{ij}∧ω_{ik} = ω_{ij}∧ω_{jk} - ω_{ik}∧ω_{jk}
                        #
                        # Move ω_{ik} from pos_ik to pos_ij+1:
                        if pos_ij < pos_ik:
                            move_sign = (-1)**(pos_ik - pos_ij - 1)
                        else:
                            move_sign = (-1)**(pos_ij - pos_ik)
                            # Swap so ij is first
                            pos_ij, pos_ik = pos_ik, pos_ij

                        # After moving, we have: ...ω_{ij}∧ω_{ik}...
                        # Arnold: ω_{ij}∧ω_{ik} → ω_{ij}∧ω_{jk} - ω_{ik}∧ω_{jk}

                        jk = (min(j,kk), max(j,kk))

                        # Term 1: replace (i,kk) with (j,kk), keep (i,j)
                        new_edges_1 = list(edges)
                        idx_ik = new_edges_1.index((i,kk))
                        new_edges_1[idx_ik] = jk
                        # Sort and compute sign
                        new_edges_1_sorted = tuple(sorted(new_edges_1))
                        perm_sign_1 = _permutation_sign(
                            [new_edges_1[l] for l in range(len(new_edges_1))],
                            list(new_edges_1_sorted))
                        queue.append((sign * move_sign * perm_sign_1, new_edges_1_sorted))

                        # Term 2: replace (i,j) with (j,kk), keep (i,kk), with minus
                        new_edges_2 = list(edges)
                        idx_ij = new_edges_2.index((i,j))
                        new_edges_2[idx_ij] = jk
                        new_edges_2_sorted = tuple(sorted(new_edges_2))
                        perm_sign_2 = _permutation_sign(
                            [new_edges_2[l] for l in range(len(new_edges_2))],
                            list(new_edges_2_sorted))
                        queue.append((-sign * move_sign * perm_sign_2, new_edges_2_sorted))

                        bc_found = True
                        break
                if bc_found:
                    break
            if bc_found:
                break

        if not bc_found:
            # It's NBC. Find it in the basis.
            found = False
            for idx, b in enumerate(target_basis):
                if b == edges:
                    result[idx] = result.get(idx, 0) + sign
                    found = True
                    break
            if not found:
                # Check with edges that might have duplicates (= 0)
                if len(set(edges)) < len(edges):
                    pass  # Zero (duplicate edges)
                else:
                    print(f"  WARNING: NBC element {edges} not found in basis!")

    if iteration >= max_iterations:
        print(f"  WARNING: Arnold reduction did not converge!")

    return result


def _permutation_sign(perm_from, perm_to):
    """Sign of permutation taking perm_from to perm_to."""
    n = len(perm_from)
    if n <= 1:
        return 1
    idx_map = {v: i for i, v in enumerate(perm_to)}
    perm = [idx_map[v] for v in perm_from]
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                inv += 1
    return (-1)**inv

# ========================================
# OS contraction
# ========================================

def os_contraction(n, k, pq, source_basis, target_basis):
    """
    Compute contraction matrix C_{pq}: OS^k(n) → OS^{k-1}(n-1).

    The contraction at divisor D_{pq} extracts ω_{pq} from the form
    (if present) and relabels vertices.

    Returns: (dim_target × dim_source) numpy matrix.
    """
    p, q = pq
    assert p < q

    dim_src = len(source_basis)
    dim_tgt = len(target_basis)

    if dim_src == 0 or dim_tgt == 0:
        return np.zeros((dim_tgt, dim_src))

    mat = np.zeros((dim_tgt, dim_src))

    n_new = n - 1  # After merging p,q

    def relabel_vertex(v):
        if v == q:
            return p
        elif v > q:
            return v - 1
        return v

    def relabel_edge(e):
        a, b = e
        a_new = relabel_vertex(a)
        b_new = relabel_vertex(b)
        if a_new == b_new:
            return None  # Collapsed
        return (min(a_new, b_new), max(a_new, b_new))

    for col, src_edges in enumerate(source_basis):
        pq_edge = (p, q)

        if pq_edge not in src_edges:
            # ω_{pq} not present → residue is 0
            continue

        # Extract ω_{pq}
        pos = list(src_edges).index(pq_edge)
        sign = (-1)**pos

        # Remaining edges (with pq removed)
        remaining = list(src_edges[:pos]) + list(src_edges[pos+1:])

        # Relabel
        relabeled = []
        valid = True
        for e in remaining:
            re = relabel_edge(e)
            if re is None:
                valid = False
                break
            relabeled.append(re)

        if not valid:
            continue

        # Express relabeled edges in target NBC basis via Arnold reduction
        relabeled_sorted = tuple(sorted(relabeled))
        if len(relabeled) == 0:
            # k=1 case: result is empty tuple (scalar)
            for idx, b in enumerate(target_basis):
                if b == ():
                    mat[idx, col] += sign
        else:
            # Arnold reduce
            coeffs = arnold_reduce(
                [(sign, relabeled_sorted)], n_new, k-1, target_basis)
            for idx, coeff in coeffs.items():
                mat[idx, col] += coeff

    return mat

# ========================================
# Bar differential
# ========================================

def build_bar_differential(dim_g, struct_const, killing_form, level,
                           n_source, sign_convention='standard'):
    """
    Build the bar differential d: B̄^n → B̄^{n-1}.

    B̄^n = A^{⊗(n+1)} ⊗ OS^n(n+1), where A = g ⊕ ℂ|0⟩.
    dim(A) = dim_g + 1.

    The differential merges pairs (i,j) using the chiral bracket:
    μ^ch(e_a, e_b) = [e_a, e_b] + level*(e_a, e_b)*|0⟩
    μ^ch(e_a, |0⟩) = 0
    μ^ch(|0⟩, e_b) = 0
    μ^ch(|0⟩, |0⟩) = 0

    Convention: basis of A is |0⟩ (index 0), e_1,...,e_d (indices 1..d).

    Returns: sparse-like matrix (dense for now).
    """
    d = dim_g
    dim_A = d + 1  # Including vacuum |0⟩ at index 0

    n = n_source  # Source bar degree
    n_target = n - 1

    # Number of points (= tensor factors)
    pts_src = n + 1   # B̄^n has n+1 factors
    pts_tgt = n       # B̄^{n-1} has n factors

    # OS bases
    os_src_basis = nbc_basis(pts_src, n)      # OS^n(n+1)
    os_tgt_basis = nbc_basis(pts_tgt, n_target) if n_target >= 0 else [()]  # OS^{n-1}(n)

    dim_os_src = len(os_src_basis)
    dim_os_tgt = len(os_tgt_basis)

    dim_source = dim_A**pts_src * dim_os_src
    dim_target = dim_A**pts_tgt * dim_os_tgt if n_target >= 0 else dim_A

    if n <= 0 or dim_source == 0 or dim_target == 0:
        return np.zeros((dim_target, dim_source))

    print(f"  d: B̄^{n} ({dim_source}) → B̄^{n-1} ({dim_target})")

    # Precompute chiral bracket
    # mu_ch[a][b] = list of (c, coeff) where μ^ch(e_a, e_b) = Σ coeff * e_c
    # Index 0 = |0⟩, indices 1..d = generators
    mu_ch = [[[] for _ in range(dim_A)] for _ in range(dim_A)]
    for a in range(1, dim_A):
        for b in range(1, dim_A):
            # Lie bracket: [e_a, e_b] = Σ_c f^{a-1,b-1}_c * e_{c+1}
            for c in range(d):
                val = struct_const[a-1, b-1, c]
                if abs(val) > 1e-15:
                    mu_ch[a][b].append((c+1, val))
            # Killing form: level * (e_a, e_b) * |0⟩
            kf_val = level * killing_form[a-1, b-1]
            if abs(kf_val) > 1e-15:
                mu_ch[a][b].append((0, kf_val))

    # Precompute OS contraction matrices for each pair
    contraction = {}
    for i in range(1, pts_src+1):
        for j in range(i+1, pts_src+1):
            contraction[(i,j)] = os_contraction(
                pts_src, n, (i,j), os_src_basis, os_tgt_basis)

    # Build differential matrix
    mat = np.zeros((dim_target, dim_source))

    # Index encoding for tensor: (a_1, ..., a_m) → flat index
    # flat = Σ a_i * dim_A^(m-1-i) * dim_os + os_idx

    def encode_src(config, os_idx):
        """Encode source index: config is tuple of length pts_src, os_idx in [0, dim_os_src)."""
        idx = 0
        for a in config:
            idx = idx * dim_A + a
        return idx * dim_os_src + os_idx

    def encode_tgt(config, os_idx):
        """Encode target index."""
        idx = 0
        for a in config:
            idx = idx * dim_A + a
        return idx * dim_os_tgt + os_idx

    # Iterate over all source configurations
    for src_config in iterproduct(range(dim_A), repeat=pts_src):
        for os_src_idx in range(dim_os_src):
            src_idx = encode_src(src_config, os_src_idx)

            # Sum over all pairs (i,j) with 1-indexed
            for i in range(1, pts_src+1):
                for j in range(i+1, pts_src+1):
                    a_i = src_config[i-1]  # 0-indexed in config
                    a_j = src_config[j-1]

                    # Chiral bracket
                    bracket_terms = mu_ch[a_i][a_j]
                    if not bracket_terms:
                        continue

                    # OS contraction
                    C = contraction[(i,j)]

                    for os_tgt_idx in range(dim_os_tgt):
                        c_coeff = C[os_tgt_idx, os_src_idx]
                        if abs(c_coeff) < 1e-15:
                            continue

                        for bracket_result, bracket_coeff in bracket_terms:
                            # Build target configuration:
                            # Position i gets bracket_result
                            # Position j is removed
                            # Remaining positions shift
                            tgt_list = list(src_config)
                            tgt_list[i-1] = bracket_result
                            del tgt_list[j-1]  # Remove position j
                            tgt_config = tuple(tgt_list)

                            # Sign: (-1)^{j-i-1} for moving v_j past intermediate elements
                            sign = (-1)**(j - i - 1)

                            tgt_idx = encode_tgt(tgt_config, os_tgt_idx)

                            mat[tgt_idx, src_idx] += sign * bracket_coeff * c_coeff

    return mat


# ========================================
# Main computation
# ========================================

def compute_bar_cohomology(algebra='sl2', level=1, max_degree=4):
    """Compute bar cohomology dimensions."""

    if algebra == 'sl2':
        d, f, kf = sl2_data()
    elif algebra == 'sl3':
        d, f, kf = sl3_data()
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    print(f"Algebra: {algebra}, dim g = {d}, level k = {level}")
    print(f"Verifying Jacobi identity...", end=" ")
    assert verify_jacobi(d, f), "Jacobi FAILED!"
    print("OK")

    dim_A = d + 1

    # Compute dimensions
    print(f"\nBar complex dimensions (unreduced, A = g ⊕ ℂ|0⟩, dim A = {dim_A}):")
    for n in range(max_degree + 1):
        pts = n + 1
        dim_os = factorial(n) if n > 0 else 1  # dim OS^n(n+1) = n!
        dim_bn = dim_A**pts * dim_os
        print(f"  B̄^{n} = {dim_A}^{pts} × {dim_os} = {dim_bn}")

    # Build differentials
    print(f"\nBuilding differentials...")
    diffs = {}
    for n in range(1, max_degree + 1):
        print(f"\n--- Degree {n} ---")
        diffs[n] = build_bar_differential(d, f, kf, level, n)

    # Verify d² = 0
    print(f"\nVerifying d² = 0...")
    for n in range(2, max_degree + 1):
        if n in diffs and (n-1) in diffs:
            d2 = diffs[n-1] @ diffs[n]
            err = np.max(np.abs(d2))
            status = "OK" if err < 1e-10 else f"FAILED (max err = {err:.2e})"
            print(f"  d_{n-1} ∘ d_{n}: {status}")

    # Compute homology
    print(f"\nComputing homology...")
    dims = {}
    ranks = {}

    for n in range(max_degree + 1):
        pts = n + 1
        dim_os = factorial(n) if n > 0 else 1
        dims[n] = dim_A**pts * dim_os

    for n in range(1, max_degree + 1):
        r = np.linalg.matrix_rank(diffs[n], tol=1e-8)
        ranks[n] = r
        print(f"  rank(d_{n}: B̄^{n} → B̄^{n-1}) = {r}")

    print(f"\nHomology dimensions:")
    for n in range(max_degree):
        ker = dims[n] - ranks.get(n, 0)  # d_n outgoing
        im = ranks.get(n+1, 0)  # d_{n+1} incoming
        h_n = ker - im
        print(f"  H_{n} = dim(B̄^{n}) - rank(d_{n}) - rank(d_{n+1}) = {dims[n]} - {ranks.get(n,0)} - {ranks.get(n+1,0)} = {h_n}")

    return


if __name__ == '__main__':
    algebra = sys.argv[1] if len(sys.argv) > 1 else 'sl2'
    level = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    max_deg = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    compute_bar_cohomology(algebra, level, max_deg)
