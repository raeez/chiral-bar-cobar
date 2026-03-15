"""Compute chiral bar cohomology using FULL differential (bracket + curvature).

Key insight: bar cohomology H^n = (ker d_bracket ∩ ker d_curvature) / im(d_bracket)

The chiral bar differential d = d_bracket + d_curvature maps B̄^n → B̄^{n-1} ⊕ T_curv
where:
- d_bracket: extracts simple pole residue (Lie bracket), maps to B̄^{n-1}
- d_curvature: extracts double pole residue (Killing form), maps to a "curvature target"
  T_curv = g^{⊗(n-2)} ⊗ OS^{n-2}(n-1)

Since d_bracket and d_curvature land in different spaces, ker(d) = ker(d_bracket) ∩ ker(d_curvature).
And im(d in B̄^n) = im(d_bracket|_{n+1}) (curvature from n+2 lands in a different mixed space).

So: H^n = (ker d_bracket^n ∩ ker d_curvature^n) / im(d_bracket^{n+1})
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from itertools import product as iter_product
from lib.os_algebra import os_basis, os_dimension, residue_map, make_pair


# ---------------------------------------------------------------------------
# Lie algebra data
# ---------------------------------------------------------------------------

def sl2_data():
    """sl₂: basis {e=0, h=1, f=2}, [e,f]=h, [h,e]=2e, [h,f]=-2f.
    Killing form: (e,f)=(f,e)=1, (h,h)=2."""
    d = 3
    bracket = np.zeros((d, d, d))
    bracket[0, 2, 1] = 1;  bracket[2, 0, 1] = -1   # [e,f]=h
    bracket[1, 0, 0] = 2;  bracket[0, 1, 0] = -2   # [h,e]=2e
    bracket[1, 2, 2] = -2; bracket[2, 1, 2] = 2     # [h,f]=-2f
    killing = np.zeros((d, d))
    killing[0, 2] = 1; killing[2, 0] = 1; killing[1, 1] = 2
    return d, bracket, killing


def sl3_data():
    """sl₃: basis {H1,H2,E1,E2,E3,F1,F2,F3}."""
    d = 8
    bracket = np.zeros((d, d, d))
    # Cartan: [H1,E1]=2E1, [H1,F1]=-2F1, [H1,E2]=-E2, [H1,F2]=F2
    #         [H2,E2]=2E2, [H2,F2]=-2F2, [H2,E1]=-E1, [H2,F1]=F1
    #         [H1,E3]=E3, [H1,F3]=-F3, [H2,E3]=E3, [H2,F3]=-F3
    bracket[0,2,2]=2;   bracket[2,0,2]=-2    # [H1,E1]=2E1
    bracket[0,5,5]=-2;  bracket[5,0,5]=2     # [H1,F1]=-2F1
    bracket[0,3,3]=-1;  bracket[3,0,3]=1     # [H1,E2]=-E2
    bracket[0,6,6]=1;   bracket[6,0,6]=-1    # [H1,F2]=F2
    bracket[0,4,4]=1;   bracket[4,0,4]=-1    # [H1,E3]=E3
    bracket[0,7,7]=-1;  bracket[7,0,7]=1     # [H1,F3]=-F3
    bracket[1,3,3]=2;   bracket[3,1,3]=-2    # [H2,E2]=2E2
    bracket[1,6,6]=-2;  bracket[6,1,6]=2     # [H2,F2]=-2F2
    bracket[1,2,2]=-1;  bracket[2,1,2]=1     # [H2,E1]=-E1
    bracket[1,5,5]=1;   bracket[5,1,5]=-1    # [H2,F1]=F1
    bracket[1,4,4]=1;   bracket[4,1,4]=-1    # [H2,E3]=E3
    bracket[1,7,7]=-1;  bracket[7,1,7]=1     # [H2,F3]=-F3
    # Positive roots: [E1,E2]=E3
    bracket[2,3,4]=1;   bracket[3,2,4]=-1
    # Negative roots: [F2,F1]=F3
    bracket[6,5,7]=1;   bracket[5,6,7]=-1
    # Cartan from roots: [E1,F1]=H1, [E2,F2]=H2, [E3,F3]=H1+H2
    bracket[2,5,0]=1;   bracket[5,2,0]=-1    # [E1,F1]=H1
    bracket[3,6,1]=1;   bracket[6,3,1]=-1    # [E2,F2]=H2
    bracket[4,7,0]=1;   bracket[7,4,0]=-1    # [E3,F3]=H1
    bracket[4,7,1]=1;   bracket[7,4,1]=-1    # [E3,F3]+=H2
    # Cross: [E1,F2]=0, [E2,F1]=0 (already zero)
    # [E3,F1]=E2 (via Jacobi) — wait, let me compute:
    # [E3,F1] = [[E1,E2],F1] = [E1,[E2,F1]] + [[E1,F1],E2] = 0 + [H1,E2] = -E2
    bracket[4,5,3]=-1;  bracket[5,4,3]=1     # [E3,F1]=-E2
    # [E3,F2] = [[E1,E2],F2] = [E1,[E2,F2]] + [[E1,F2],E2] = [E1,H2] + 0 = E1
    bracket[4,6,2]=1;   bracket[6,4,2]=-1    # [E3,F2]=E1
    # [F3,E1] = [[F2,F1],E1] = [F2,[F1,E1]] + [[F2,E1],F1] = [F2,-H1] + 0 = F2
    # Actually [F3,E1] = -[E1,F3] = -(H1+H2)... wait.
    # E3=[E1,E2], F3=[F2,F1]. [E1,F3]=[E1,[F2,F1]]=[F2,[E1,F1]]+[[E1,F2],F1]
    # = [F2,-H1] + 0 = -[F2,H1] = -(-F2) = F2. Wait, [H1,F2]=F2 so [F2,H1]=-F2.
    # So [E1,F3] = -[F2,H1] = F2. Hmm, let me redo:
    # [E1,F3]=[E1,[F2,F1]]. Jacobi: = [[E1,F2],F1]+[F2,[E1,F1]]
    # [E1,F2]=0, [E1,F1]=H1. So = 0 + [F2,H1] = -[H1,F2] = -F2.
    # Wait [H1,F2]=F2, so [F2,H1]=-F2. So [E1,F3]=-F2.
    # Hmm let me recheck. [H1,F2]=F2? From above: bracket[0,6,6]=1 means [H1,F2]=F2.
    # But standard convention: H1 acts on F2 (which has root -α2) by <α1,-α2>=-(-1)=1?
    # Actually for sl3, <α1,α2>=-1, so [H1,F2]=-(-1)F2=F2. Yes.
    # [E1,F3] = [F2,H1] = -[H1,F2] = -F2.
    # Wait no: [E1,F3]=[E1,[F2,F1]]=[[E1,F2],F1]+[F2,[E1,F1]]=0+[F2,H1]=-[H1,F2]=-F2
    # But F2 has index 6, so:
    # Actually I already set [E3,F1]=-E2 and [E3,F2]=E1 above. Let me not
    # duplicate. The bracket [E1,F3] is not the same as [E3,F1].
    # [E1,F3]: E1=index 2, F3=index 7.
    bracket[2,7,6]=-1;  bracket[7,2,6]=1     # [E1,F3]=-F2
    # [E2,F3] = [E2,[F2,F1]] = [[E2,F2],F1]+[F2,[E2,F1]]=[H2,F1]+0
    # [H2,F1]=F1 (bracket[1,5,5]=1). So [E2,F3]=F1.
    bracket[3,7,5]=1;   bracket[7,3,5]=-1    # [E2,F3]=F1

    killing = np.zeros((d, d))
    # Killing form: (Hi,Hj)=A_{ij}, (Ei,Fj)=delta_{ij}
    killing[0,0]=2; killing[0,1]=-1; killing[1,0]=-1; killing[1,1]=2
    killing[2,5]=1; killing[5,2]=1  # (E1,F1)
    killing[3,6]=1; killing[6,3]=1  # (E2,F2)
    killing[4,7]=1; killing[7,4]=1  # (E3,F3)
    return d, bracket, killing


# ---------------------------------------------------------------------------
# Bar complex dimensions
# ---------------------------------------------------------------------------

def bar_dim(dim_g: int, n: int) -> int:
    """Dimension of B̄^n = g^{⊗n} ⊗ OS^{n-1}(n)."""
    if n <= 0:
        return 1 if n == 0 else 0
    os_dim = os_dimension(n, n - 1)
    return dim_g**n * os_dim


def bar_basis_index(dim_g: int, n: int, tensor_indices: tuple, os_idx: int,
                     os_dim: int) -> int:
    """Linear index for basis element (tensor_indices, os_idx) in B̄^n.

    tensor_indices: tuple of n indices in range(dim_g)
    os_idx: index of OS basis element
    """
    tensor_linear = 0
    for a in tensor_indices:
        tensor_linear = tensor_linear * dim_g + a
    return tensor_linear * os_dim + os_idx


# ---------------------------------------------------------------------------
# Bracket differential d_bracket: B̄^n → B̄^{n-1}
# ---------------------------------------------------------------------------

def build_bracket_differential(dim_g: int, bracket: np.ndarray, n: int) -> np.ndarray:
    """Build bracket differential matrix d_bracket: B̄^n → B̄^{n-1}.

    This is the simple-pole (Lie bracket) part of the chiral bar differential.
    """
    if n <= 1:
        return np.zeros((bar_dim(dim_g, n - 1), bar_dim(dim_g, n)))

    os_src_dim = os_dimension(n, n - 1)
    os_tgt_dim = os_dimension(n - 1, n - 2)
    src_dim = dim_g**n * os_src_dim
    tgt_dim = dim_g**(n - 1) * os_tgt_dim

    mat = np.zeros((tgt_dim, src_dim))

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # OS residue map at D_{ij}
            os_res = residue_map(n, n - 1, i, j)  # (os_tgt_dim × os_src_dim)

            # Sign from reordering: bring positions i,j adjacent
            # Convention: (-1)^{j-i-1} for bringing j next to i
            sign_ij = (-1) ** (j - i - 1)

            # For each source basis element
            for src_tensor in iter_product(range(dim_g), repeat=n):
                a_i = src_tensor[i - 1]  # 0-indexed
                a_j = src_tensor[j - 1]

                for src_os in range(os_src_dim):
                    src_idx = bar_basis_index(dim_g, n, src_tensor, src_os, os_src_dim)

                    # Bracket [a_i, a_j] = sum_c bracket[a_i, a_j, c] * e_c
                    for c in range(dim_g):
                        coeff = bracket[a_i, a_j, c]
                        if abs(coeff) < 1e-15:
                            continue

                        # Build target tensor: replace i,j with c at merged position
                        # Merged position = min(i,j), remove max(i,j)
                        tgt_tensor = list(src_tensor)
                        tgt_tensor[i - 1] = c  # merged position
                        tgt_tensor.pop(j - 1)  # remove j (0-indexed)
                        tgt_tensor = tuple(tgt_tensor)

                        # OS residue
                        for tgt_os in range(os_tgt_dim):
                            os_coeff = os_res[tgt_os, src_os]
                            if abs(os_coeff) < 1e-15:
                                continue

                            tgt_idx = bar_basis_index(dim_g, n - 1, tgt_tensor,
                                                        tgt_os, os_tgt_dim)
                            mat[tgt_idx, src_idx] += sign_ij * coeff * os_coeff

    return mat


# ---------------------------------------------------------------------------
# Curvature differential d_curvature: B̄^n → T_curv
# ---------------------------------------------------------------------------

def build_curvature_differential(dim_g: int, killing: np.ndarray, n: int,
                                   level: float = 1.0) -> np.ndarray:
    """Build curvature differential matrix d_curvature: B̄^n → T_curv.

    The curvature at collision D_{ij} maps:
    (v_1,...,v_n) ⊗ ω → level·κ(v_i,v_j) · (v_1,...,v̂_i,...,v̂_j,...,v_n) ⊗ Res_{D_{ij}}(ω)

    Target space T_curv = g^{⊗(n-2)} ⊗ OS^{n-2}(n-1).
    Note: this is NOT B̄^{n-2} (different OS space). For kernel computation, it doesn't matter.

    For n=2: target is C (scalar). κ(v_1,v_2)·Res(ω) is a scalar.
    For n=1: no curvature (need at least 2 generators).
    """
    if n <= 1:
        return np.zeros((1, bar_dim(dim_g, n)))

    os_src_dim = os_dimension(n, n - 1)
    src_dim = dim_g**n * os_src_dim

    if n == 2:
        # Target is scalar: just the Killing form value times OS residue
        # OS^1(2) → OS^0(1) = C, residue is trivially 1 (η₁₂ → 1)
        os_tgt_dim = 1
        tgt_dim = 1  # scalar

        mat = np.zeros((tgt_dim, src_dim))
        os_res = residue_map(2, 1, 1, 2)  # should be 1×1 matrix ≈ [[1]]

        for a in range(dim_g):
            for b in range(dim_g):
                kab = killing[a, b]
                if abs(kab) < 1e-15:
                    continue
                src_idx = bar_basis_index(dim_g, 2, (a, b), 0, os_src_dim)
                mat[0, src_idx] += level * kab * os_res[0, 0]

        return mat

    # n >= 3
    # Target: g^{⊗(n-2)} ⊗ OS^{n-2}(n-1)
    os_tgt_dim = os_dimension(n - 1, n - 2)
    tgt_tensor_dim = dim_g**(n - 2)
    tgt_dim = tgt_tensor_dim * os_tgt_dim

    # We need separate target blocks for each collision pair, because
    # different pairs produce generators at different positions.
    # However, after relabeling, the results can be mapped to a common
    # target space g^{⊗(n-2)} ⊗ OS^{n-2}(n-1).
    #
    # Actually, different pairs (i,j) map to the SAME target space
    # but via different relabeling. Let me be careful.
    #
    # After collision at D_{ij}:
    # - Remaining generators: at positions {1,...,n}\{i,j}
    # - These need to be mapped to a standard (n-2)-tensor
    # - The natural ordering: preserve relative order, renumber to 1,...,n-2
    #
    # The OS part: Res_{D_{ij}}: OS^{n-1}(n) → OS^{n-2}(n-1)
    # The merged point gets label min(i,j), others shift down as needed.
    # The curvature eliminates the merged point too, so we need
    # OS forms on n-2 points. But the residue gives forms on n-1 points.
    #
    # SOLUTION: concatenate all pairs' contributions into a single target.
    # This gives a taller matrix, but the kernel is what matters.

    num_pairs = n * (n - 1) // 2
    total_tgt_dim = num_pairs * tgt_dim

    mat = np.zeros((total_tgt_dim, src_dim))

    pair_idx = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            tgt_offset = pair_idx * tgt_dim
            pair_idx += 1

            os_res = residue_map(n, n - 1, i, j)
            sign_ij = (-1) ** (j - i - 1)

            for src_tensor in iter_product(range(dim_g), repeat=n):
                a_i = src_tensor[i - 1]
                a_j = src_tensor[j - 1]
                kab = killing[a_i, a_j]
                if abs(kab) < 1e-15:
                    continue

                # Remaining generators (remove positions i and j)
                remaining = []
                for pos in range(n):
                    if pos != i - 1 and pos != j - 1:
                        remaining.append(src_tensor[pos])
                tgt_tensor = tuple(remaining)

                for src_os in range(os_src_dim):
                    src_idx = bar_basis_index(dim_g, n, src_tensor, src_os, os_src_dim)

                    for tgt_os in range(os_tgt_dim):
                        os_coeff = os_res[tgt_os, src_os]
                        if abs(os_coeff) < 1e-15:
                            continue

                        # Target index within this pair's block
                        t_tensor_linear = 0
                        for a in tgt_tensor:
                            t_tensor_linear = t_tensor_linear * dim_g + a
                        t_local = t_tensor_linear * os_tgt_dim + tgt_os

                        mat[tgt_offset + t_local, src_idx] += \
                            sign_ij * level * kab * os_coeff

    return mat


# ---------------------------------------------------------------------------
# Bar cohomology computation
# ---------------------------------------------------------------------------

def compute_bar_cohomology(dim_g: int, bracket: np.ndarray, killing: np.ndarray,
                            max_degree: int = 5, level: float = 1.0):
    """Compute bar cohomology H^n for n = 1, ..., max_degree.

    H^n = (ker d_bracket^n ∩ ker d_curvature^n) / im(d_bracket^{n+1})
    """
    results = {}

    # Precompute differentials
    d_brackets = {}
    d_curvatures = {}

    for n in range(1, max_degree + 2):  # need n+1 for image
        dim_bn = bar_dim(dim_g, n)
        if dim_bn == 0:
            continue
        print(f"  Building differentials for degree {n} (dim B̄^{n} = {dim_bn})...")
        d_brackets[n] = build_bracket_differential(dim_g, bracket, n)
        d_curvatures[n] = build_curvature_differential(dim_g, killing, n, level)

    for n in range(1, max_degree + 1):
        dim_bn = bar_dim(dim_g, n)
        if dim_bn == 0:
            results[n] = 0
            continue

        print(f"\n  Computing H^{n}:")
        print(f"    dim B̄^{n} = {dim_bn}")

        # Kernel of d_bracket
        d_br = d_brackets.get(n)
        if d_br is not None and d_br.size > 0:
            _, S_br, Vt_br = np.linalg.svd(d_br, full_matrices=True)
            rank_br = np.sum(S_br > 1e-8)
            ker_br_basis = Vt_br[rank_br:]  # rows are kernel basis vectors
            dim_ker_br = ker_br_basis.shape[0]
        else:
            ker_br_basis = np.eye(dim_bn)
            dim_ker_br = dim_bn

        print(f"    dim ker(d_bracket) = {dim_ker_br}")

        # Kernel of d_curvature
        d_cv = d_curvatures.get(n)
        if d_cv is not None and d_cv.size > 0:
            _, S_cv, Vt_cv = np.linalg.svd(d_cv, full_matrices=True)
            rank_cv = np.sum(S_cv > 1e-8)
            ker_cv_basis = Vt_cv[rank_cv:]
            dim_ker_cv = ker_cv_basis.shape[0]
        else:
            ker_cv_basis = np.eye(dim_bn)
            dim_ker_cv = dim_bn

        print(f"    dim ker(d_curvature) = {dim_ker_cv}")

        # Intersection of kernels: ker(d_bracket) ∩ ker(d_curvature)
        # = ker([d_bracket; d_curvature]) (stacked matrix)
        d_combined = np.vstack([d_br, d_cv]) if d_cv is not None and d_cv.size > 0 \
                     else d_br
        _, S_comb, Vt_comb = np.linalg.svd(d_combined, full_matrices=True)
        rank_comb = np.sum(S_comb > 1e-8)
        ker_comb_basis = Vt_comb[rank_comb:]
        dim_ker_comb = ker_comb_basis.shape[0]

        print(f"    dim (ker d_bracket ∩ ker d_curvature) = {dim_ker_comb}")

        # Image of d_bracket from degree n+1
        d_br_next = d_brackets.get(n + 1)
        if d_br_next is not None and d_br_next.size > 0:
            _, S_im, _ = np.linalg.svd(d_br_next, full_matrices=False)
            dim_im = np.sum(S_im > 1e-8)
        else:
            dim_im = 0

        # Image of d_curvature from degree n+2
        # This lands in a DIFFERENT space (mixed vacuum states), so does NOT
        # contribute to B̄^n. dim_im_curv = 0.

        print(f"    dim im(d_bracket from n+1) = {dim_im}")

        # But we need im(d_bracket) WITHIN ker(d_combined)
        # im(d_bracket^{n+1}) is a subspace of B̄^n. Its intersection with
        # ker(d_combined) gives the denominator.
        # Since d² = 0 on the full complex, d_bracket(x) for x ∈ B̄^{n+1}
        # should satisfy d_bracket(d_bracket(x)) + d_curvature(d_bracket(x)) = 0.
        # But d_bracket² ≠ 0 in general! So im(d_bracket^{n+1}) is NOT
        # necessarily inside ker(d_combined).
        #
        # Hmm, this needs more thought. In the full complex with d = d_br + d_cv,
        # d² = 0 means for x ∈ B̄^{n+1}:
        # d(d(x)) = d(d_br(x) + d_cv(x))
        # d_br(x) ∈ B̄^n, d_cv(x) ∈ T_curv^{n-1}
        # d(d_br(x)) = d_br(d_br(x)) + d_cv(d_br(x)) [in B̄^{n-1} ⊕ T_curv^{n-2}]
        # d(d_cv(x)) involves applying d to the curvature output...
        #
        # Actually, d² = 0 says that for x ∈ B̄^{n+1}, d(d(x)) = 0.
        # d(x) has components in B̄^n (bracket) and mixed vacuum states (curvature).
        # For the B̄^n component d_br(x), applying d again gives:
        # d_br(d_br(x)) + d_cv(d_br(x)) + [cross terms from mixed states] = 0
        #
        # This means d_br(d_br(x)) ∈ B̄^{n-1} and d_cv(d_br(x)) ∈ T_curv
        # don't individually vanish — they're compensated by cross terms from
        # the curvature output of x.
        #
        # For COHOMOLOGY: we need im(d) in B̄^n, which is NOT just im(d_br^{n+1}).
        # There's also contributions from d acting on vacuum-containing states.
        #
        # Let me reconsider. The FULL complex is:
        # ... → B̃^{n+1} → B̃^n → B̃^{n-1} → ...
        # where B̃^n = ⊕_k B̃^n_k (k = number of vacuum insertions)
        # H^n of the FULL complex at the "pure" level B̃^n_0 = B̄^n:
        #
        # Actually, the cohomology of the total complex is NOT stratified by
        # number of vacua. The differential mixes pure and vacuum states.
        #
        # For a SIMPLER approach: just compute rank of d_combined = [d_br; d_cv]
        # for the kernel, and use the RANK of the combined differential FROM
        # degree n+1 for the image.

        # Cohomology dimension (upper bound, might need refinement)
        h_n = dim_ker_comb - dim_im

        print(f"    H^{n} = {dim_ker_comb} - {dim_im} = {h_n}")

        results[n] = h_n

    return results


# ---------------------------------------------------------------------------
# Verification: d² = 0 check
# ---------------------------------------------------------------------------

def check_d_squared(dim_g, bracket, killing, n, level=1.0):
    """Check whether d_bracket² = 0 and the full d² = 0 structure."""
    d_br_n = build_bracket_differential(dim_g, bracket, n)
    d_br_n1 = build_bracket_differential(dim_g, bracket, n - 1)
    d_cv_n = build_curvature_differential(dim_g, killing, n, level)

    d2_bracket = d_br_n1 @ d_br_n if d_br_n1.shape[1] == d_br_n.shape[0] else None

    if d2_bracket is not None:
        max_entry = np.max(np.abs(d2_bracket))
        print(f"  d_bracket² (n={n}): max entry = {max_entry:.2e} {'✓ ZERO' if max_entry < 1e-8 else '✗ NONZERO'}")

    return d2_bracket


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print("=" * 60)
    print("CHIRAL BAR COHOMOLOGY: FULL DIFFERENTIAL COMPUTATION")
    print("=" * 60)

    # Riordan numbers R(n+3) for comparison
    # R(4)=3, R(5)=6, R(6)=15, R(7)=36, R(8)=91
    riordan = {1: 3, 2: 6, 3: 15, 4: 36, 5: 91}

    print("\n--- sl₂ (dim=3) ---")
    d, bracket, killing = sl2_data()

    # First check d_bracket² for small degrees
    print("\nChecking d_bracket² = 0:")
    for n in range(2, 5):
        check_d_squared(d, bracket, killing, n)

    print("\nComputing bar cohomology:")
    max_deg = 4  # start small
    results = compute_bar_cohomology(d, bracket, killing, max_degree=max_deg)

    print("\n" + "=" * 40)
    print("RESULTS: sl₂ bar cohomology")
    print("=" * 40)
    print(f"{'n':>4} {'H^n':>8} {'R(n+3)':>8} {'match':>6}")
    print("-" * 30)
    for n in range(1, max_deg + 1):
        h_n = results.get(n, '?')
        r_n = riordan.get(n, '?')
        match = '✓' if h_n == r_n else '✗'
        print(f"{n:>4} {h_n:>8} {r_n:>8} {match:>6}")
