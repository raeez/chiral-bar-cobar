"""Verify d_bracket² = 0 on the chiral bar complex for sl₂.

The chiral bar differential uses only the Lie bracket (zeroth product)
and the Poincaré residue on OS forms. The Jacobi identity should give d²=0.

If d² ≠ 0, there's a sign error in the differential construction.
This script computes everything manually to find the correct signs.
"""

import sys, os
# Scripts are run standalone (not via pytest); add compute/ root for lib.* imports.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from lib.os_algebra import os_basis, os_dimension, residue_map, make_pair


def sl2_bracket(a, b):
    """[a,b] for sl₂. Basis: e=0, h=1, f=2."""
    # Returns list of (coeff, index) pairs
    if (a, b) == (0, 2): return [(1, 1)]    # [e,f] = h
    if (a, b) == (2, 0): return [(-1, 1)]   # [f,e] = -h
    if (a, b) == (1, 0): return [(2, 0)]    # [h,e] = 2e
    if (a, b) == (0, 1): return [(-2, 0)]   # [e,h] = -2e
    if (a, b) == (1, 2): return [(-2, 2)]   # [h,f] = -2f
    if (a, b) == (2, 1): return [(2, 2)]    # [f,h] = 2f
    return []


def print_residue_maps():
    """Print all OS residue maps for small n."""
    print("=== OS Residue Maps ===")
    for n in [2, 3]:
        k = n - 1
        dim_src = os_dimension(n, k)
        dim_tgt = os_dimension(n - 1, k - 1)
        _, src_basis = os_basis(n, k)
        _, tgt_basis = os_basis(n - 1, k - 1)
        print(f"\nOS^{k}({n}): dim = {dim_src}")
        print(f"  Source basis shape: {src_basis.shape}")

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                res = residue_map(n, k, i, j)
                print(f"  Res_D{i}{j}: {res.tolist()}")


def build_d_bracket_manual_n2():
    """Build d_bracket: B̄^2 → B̄^1 manually for sl₂.

    B̄^2 = sl₂^{⊗2} ⊗ OS^1(2).  dim = 9 × 1 = 9.
    B̄^1 = sl₂ ⊗ OS^0(1).  dim = 3 × 1 = 3.

    Only one pair (1,2). Res_{D_{12}}(η_{12}) = 1.
    d(a⊗b⊗η) = [a,b] ⊗ 1.  (No sign factor since j-i-1 = 0.)
    """
    dim_g = 3
    # Source: (a,b) pairs, indexed as a*3 + b
    # Target: c, indexed as c
    mat = np.zeros((3, 9))
    for a in range(3):
        for b in range(3):
            src = a * 3 + b
            for coeff, c in sl2_bracket(a, b):
                mat[c, src] += coeff
    return mat


def build_d_bracket_manual_n3():
    """Build d_bracket: B̄^3 → B̄^2 manually for sl₂.

    B̄^3 = sl₂^{⊗3} ⊗ OS^2(3).  dim = 27 × 2 = 54.
    B̄^2 = sl₂^{⊗2} ⊗ OS^1(2).  dim = 9 × 1 = 9.

    Three pairs (1,2), (1,3), (2,3).

    For each pair (i,j):
    - Sign: (-1)^{j-i-1}
    - OS residue: Res_{D_{ij}}: OS^2(3) → OS^1(2)
    - Tensor: replace positions i,j with [a_i, a_j] at min(i,j), remove max(i,j)

    The sign convention for the CE differential is:
    d(x₁⊗x₂⊗x₃ ⊗ ω) = Σ_{i<j} (-1)^{i+j} [xᵢ,xⱼ] ⊗ x_k ⊗ Res_{D_{ij}}(ω)
    where k is the remaining index.

    Wait, the standard sign for the CE complex is (-1)^{i+j-1}. Let me use that.
    """
    dim_g = 3
    os_src_dim = os_dimension(3, 2)  # should be 2
    os_tgt_dim = os_dimension(2, 1)  # should be 1

    print(f"  OS^2(3) dim = {os_src_dim}")
    print(f"  OS^1(2) dim = {os_tgt_dim}")

    # Get residue maps
    res_12 = residue_map(3, 2, 1, 2)  # OS^2(3) → OS^1(2)
    res_13 = residue_map(3, 2, 1, 3)
    res_23 = residue_map(3, 2, 2, 3)

    print(f"  Res_D12 = {res_12.tolist()}")
    print(f"  Res_D13 = {res_13.tolist()}")
    print(f"  Res_D23 = {res_23.tolist()}")

    # Source indexing: (a,b,c,s) → a*3*3*2 + b*3*2 + c*2 + s
    # where a,b,c ∈ {0,1,2} are sl₂ indices, s ∈ {0,1} is OS index
    src_dim = 27 * os_src_dim
    tgt_dim = 9 * os_tgt_dim

    mat = np.zeros((tgt_dim, src_dim))

    for a in range(3):
        for b in range(3):
            for c in range(3):
                for s in range(os_src_dim):
                    src_idx = ((a * 3 + b) * 3 + c) * os_src_dim + s

                    # Pair (1,2): merge a,b into [a,b], keep c
                    # Sign: (-1)^{1+2-1} = 1  (CE convention)
                    # My code used (-1)^{j-i-1} = (-1)^0 = 1
                    for coeff, d_ab in sl2_bracket(a, b):
                        for t in range(os_tgt_dim):
                            os_c = res_12[t, s]
                            if abs(os_c) < 1e-15:
                                continue
                            # Target: (d_ab, c, t) → d_ab*3 + c (for os_tgt_dim=1)
                            tgt_idx = (d_ab * 3 + c) * os_tgt_dim + t
                            sign = 1  # (-1)^{1+2-1} = 1
                            mat[tgt_idx, src_idx] += sign * coeff * os_c

                    # Pair (1,3): merge a,c into [a,c], keep b
                    # Sign: (-1)^{1+3-1} = -1
                    # Merged goes to position min(1,3)=1, removed is max=3
                    # Target tensor: ([a,c], b) at positions (1,2)
                    for coeff, d_ac in sl2_bracket(a, c):
                        for t in range(os_tgt_dim):
                            os_c = res_13[t, s]
                            if abs(os_c) < 1e-15:
                                continue
                            # After merge: position 1 = [a,c], position 2 = b
                            tgt_idx = (d_ac * 3 + b) * os_tgt_dim + t
                            sign = -1  # (-1)^{1+3-1} = -1
                            mat[tgt_idx, src_idx] += sign * coeff * os_c

                    # Pair (2,3): merge b,c into [b,c], keep a
                    # Sign: (-1)^{2+3-1} = 1
                    # Merged goes to position min(2,3)=2, removed is max=3
                    # Target tensor: (a, [b,c]) at positions (1,2)
                    for coeff, d_bc in sl2_bracket(b, c):
                        for t in range(os_tgt_dim):
                            os_c = res_23[t, s]
                            if abs(os_c) < 1e-15:
                                continue
                            # After merge: position 1 = a, position 2 = [b,c]
                            tgt_idx = (a * 3 + d_bc) * os_tgt_dim + t
                            sign = 1  # (-1)^{2+3-1} = 1
                            mat[tgt_idx, src_idx] += sign * coeff * os_c

    return mat


def test_ce_signs():
    """Test with Chevalley-Eilenberg signs to verify Jacobi gives d²=0."""
    print("\n=== Testing d² = 0 with CE signs ===")
    d2 = build_d_bracket_manual_n2()
    print(f"d_bracket(2→1): shape {d2.shape}")

    d3 = build_d_bracket_manual_n3()
    print(f"d_bracket(3→2): shape {d3.shape}")

    d2_sq = d2 @ d3
    max_val = np.max(np.abs(d2_sq))
    print(f"\nd² = d_bracket(2→1) ∘ d_bracket(3→2): shape {d2_sq.shape}")
    print(f"  max |entry| = {max_val:.6e}")
    if max_val < 1e-10:
        print("  ✓ d² = 0")
    else:
        print("  ✗ d² ≠ 0")
        # Show nonzero entries
        nz = np.argwhere(np.abs(d2_sq) > 1e-10)
        for r, c in nz[:10]:
            print(f"    d²[{r},{c}] = {d2_sq[r,c]:.4f}")

    return d2, d3


def try_alternative_signs():
    """Try different sign conventions to find d²=0."""
    print("\n=== Trying alternative sign conventions ===")
    dim_g = 3
    os_src_dim = os_dimension(3, 2)
    os_tgt_dim = os_dimension(2, 1)

    res_12 = residue_map(3, 2, 1, 2)
    res_13 = residue_map(3, 2, 1, 3)
    res_23 = residue_map(3, 2, 2, 3)

    d2 = build_d_bracket_manual_n2()

    # Try all 8 sign choices for the three pairs
    for s12 in [1, -1]:
        for s13 in [1, -1]:
            for s23 in [1, -1]:
                mat = np.zeros((9, 54))
                for a in range(3):
                    for b in range(3):
                        for c in range(3):
                            for s in range(os_src_dim):
                                src_idx = ((a*3+b)*3+c)*os_src_dim + s

                                # (1,2)
                                for coeff, d_ab in sl2_bracket(a,b):
                                    for t in range(os_tgt_dim):
                                        os_c = res_12[t,s]
                                        if abs(os_c) < 1e-15: continue
                                        tgt_idx = (d_ab*3+c)*os_tgt_dim+t
                                        mat[tgt_idx, src_idx] += s12 * coeff * os_c

                                # (1,3)
                                for coeff, d_ac in sl2_bracket(a,c):
                                    for t in range(os_tgt_dim):
                                        os_c = res_13[t,s]
                                        if abs(os_c) < 1e-15: continue
                                        tgt_idx = (d_ac*3+b)*os_tgt_dim+t
                                        mat[tgt_idx, src_idx] += s13 * coeff * os_c

                                # (2,3)
                                for coeff, d_bc in sl2_bracket(b,c):
                                    for t in range(os_tgt_dim):
                                        os_c = res_23[t,s]
                                        if abs(os_c) < 1e-15: continue
                                        tgt_idx = (a*3+d_bc)*os_tgt_dim+t
                                        mat[tgt_idx, src_idx] += s23 * coeff * os_c

                d2_sq = d2 @ mat
                max_val = np.max(np.abs(d2_sq))
                if max_val < 1e-10:
                    print(f"  ✓ d²=0 with signs ({s12:+d}, {s13:+d}, {s23:+d})")
                else:
                    pass  # don't print failures


if __name__ == '__main__':
    print_residue_maps()
    d2, d3 = test_ce_signs()
    try_alternative_signs()
