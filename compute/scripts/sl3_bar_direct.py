#!/usr/bin/env python3
"""Direct computation of sl₃ bar cohomology at minimum weight.

At minimum weight (w=n), B̄^n = g^⊗n ⊗ OS^{n-1}(C_n).
d: B̄^{n+1} → B̄^n via Poincaré residue of OPE along collision divisors.

Goal: check if minimum-weight cohomology matches known [8, 36, 204].
"""

import numpy as np
import time
from math import factorial

# sl₃ structure constants
dim_g = 8
labels = ['H1', 'H2', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']
H1, H2, E1, E2, E3, F1, F2, F3 = range(8)

sc = np.zeros((dim_g, dim_g, dim_g))

# Cartan-Root
sc[H1,E1,E1]=2;  sc[E1,H1,E1]=-2
sc[H1,E2,E2]=-1; sc[E2,H1,E2]=1
sc[H1,E3,E3]=1;  sc[E3,H1,E3]=-1
sc[H1,F1,F1]=-2; sc[F1,H1,F1]=2
sc[H1,F2,F2]=1;  sc[F2,H1,F2]=-1
sc[H1,F3,F3]=-1; sc[F3,H1,F3]=1
sc[H2,E1,E1]=-1; sc[E1,H2,E1]=1
sc[H2,E2,E2]=2;  sc[E2,H2,E2]=-2
sc[H2,E3,E3]=1;  sc[E3,H2,E3]=-1
sc[H2,F1,F1]=1;  sc[F1,H2,F1]=-1
sc[H2,F2,F2]=-2; sc[F2,H2,F2]=2
sc[H2,F3,F3]=-1; sc[F3,H2,F3]=1

# Root-Root
sc[E1,F1,H1]=1;  sc[F1,E1,H1]=-1
sc[E2,F2,H2]=1;  sc[F2,E2,H2]=-1
sc[E1,E2,E3]=1;  sc[E2,E1,E3]=-1
sc[F1,F2,F3]=-1; sc[F2,F1,F3]=1
sc[E3,F3,H1]=1;  sc[E3,F3,H2]=1; sc[F3,E3,H1]=-1; sc[F3,E3,H2]=-1
sc[E1,F3,F2]=-1; sc[F3,E1,F2]=1
sc[E2,F3,F1]=1;  sc[F3,E2,F1]=-1
sc[E3,F1,E2]=-1; sc[F1,E3,E2]=1
sc[E3,F2,E1]=1;  sc[F2,E3,E1]=-1

# Verify Jacobi
print("Verifying Jacobi identity...")
max_err = 0
for a in range(dim_g):
    for b in range(dim_g):
        for c in range(dim_g):
            for d in range(dim_g):
                val = sum(sc[a,b,e]*sc[e,c,d] + sc[b,c,e]*sc[e,a,d] + sc[c,a,e]*sc[e,b,d]
                          for e in range(dim_g))
                max_err = max(max_err, abs(val))
print(f"  Max Jacobi error: {max_err}")
assert max_err == 0, "Jacobi identity violated!"

# d₂: B̄² → B̄¹ (bracket map)
# B̄² = g⊗g (dim 64), B̄¹ = g (dim 8)
# d₂(a⊗b) = [a,b]
print("\n--- d₂: g⊗g → g ---")
d2 = np.zeros((dim_g, dim_g**2))
for a in range(dim_g):
    for b in range(dim_g):
        for c in range(dim_g):
            d2[c, a*dim_g+b] += sc[a,b,c]

rank_d2 = np.linalg.matrix_rank(d2)
print(f"  rank(d₂) = {rank_d2}")
print(f"  dim ker(d₂) = {dim_g**2 - rank_d2}")

# d₃: B̄³ → B̄² at minimum weight
# B̄³ = g⊗³ ⊗ OS²(C₃), dim = 512 * 2 = 1024
# B̄² = g⊗² ⊗ OS¹(C₂), dim = 64 * 1 = 64
#
# OS²(C₃) basis: {ω₀ = η₀₁∧η₀₂, ω₁ = η₀₂∧η₁₂}
# Arnold: η₀₁∧η₁₂ = ω₀ + ω₁
#
# Contraction maps (OS² → OS¹, with OS¹ = span{η₀₁}):
# ι₀₁: ω₀ → +1, ω₁ → 0
# ι₀₂: ω₀ → -1, ω₁ → +1
# ι₁₂: ω₀ → 0,  ω₁ → -1
#
# After collision D_{ij}: merge vertices i,j, apply bracket [e_i, e_j].

print("\n--- d₃: g⊗³⊗OS²(C₃) → g⊗²⊗OS¹(C₂) ---")
t0 = time.time()

# Contraction coefficients: iota[pair_idx][os_idx] = coefficient
# pair indices: 0=(0,1), 1=(0,2), 2=(1,2)
iota3 = {
    0: [1, 0],    # ι₀₁
    1: [-1, 1],   # ι₀₂
    2: [0, -1],   # ι₁₂
}

d3 = np.zeros((64, 1024))
for a in range(dim_g):
    for b in range(dim_g):
        for c in range(dim_g):
            for omega in range(2):
                src = a*dim_g*dim_g*2 + b*dim_g*2 + c*2 + omega

                # Res_{D₀₁}: [a,b]⊗c, ι₀₁(ω)
                coeff = iota3[0][omega]
                if coeff != 0:
                    for d in range(dim_g):
                        if sc[a,b,d] != 0:
                            d3[d*dim_g+c, src] += sc[a,b,d] * coeff

                # Res_{D₀₂}: [a,c]⊗b, ι₀₂(ω)
                coeff = iota3[1][omega]
                if coeff != 0:
                    for d in range(dim_g):
                        if sc[a,c,d] != 0:
                            d3[d*dim_g+b, src] += sc[a,c,d] * coeff

                # Res_{D₁₂}: a⊗[b,c], ι₁₂(ω)
                coeff = iota3[2][omega]
                if coeff != 0:
                    for d in range(dim_g):
                        if sc[b,c,d] != 0:
                            d3[a*dim_g+d, src] += sc[b,c,d] * coeff

print(f"  Built in {time.time()-t0:.2f}s, shape {d3.shape}")
rank_d3 = np.linalg.matrix_rank(d3)
ker_d3 = 1024 - rank_d3
print(f"  rank(d₃) = {rank_d3}")
print(f"  dim ker(d₃) = {ker_d3}")

# Check d₂ ∘ d₃ = 0
comp23 = d2 @ d3
print(f"  ||d₂∘d₃|| = {np.max(np.abs(comp23))}")

# Minimum-weight cohomology
# H¹ = B̄¹/im(d₂) = 8 - rank(d₂)
H1 = dim_g - rank_d2
# H² = ker(d₂)/im(d₃) = (64 - rank_d2) - rank_d3
H2 = (dim_g**2 - rank_d2) - rank_d3
print(f"\nMinimum-weight cohomology:")
print(f"  H¹ = {dim_g} - {rank_d2} = {H1} (expected 8)")
print(f"  H² = {dim_g**2-rank_d2} - {rank_d3} = {H2} (expected 36)")

if H1 != 8:
    print(f"\n  *** H¹ ≠ 8: minimum weight doesn't capture full bar cohomology ***")
    print(f"  The bar complex involves all conformal weights.")
    print(f"  Cannot compute H⁴ from minimum weight alone.")
else:
    print(f"\n  H¹ matches! Checking H²...")
    if H2 == 36:
        print(f"  H² matches! Minimum weight captures bar cohomology.")
        print(f"  Now building d₄ to compute H³...")
    else:
        print(f"  H² = {H2} ≠ 36. Higher weights contribute.")

# d₄: B̄⁴ → B̄³
# B̄⁴ = g⊗⁴ ⊗ OS³(C₄), dim = 4096 * 6 = 24576
# B̄³ = g⊗³ ⊗ OS²(C₃), dim = 512 * 2 = 1024
#
# OS³(C₄) has dim 6. We need an explicit basis and contraction maps.
#
# Using NBC basis. Edges of K₄ (0-indexed):
# e₀=(0,1), e₁=(0,2), e₂=(0,3), e₃=(1,2), e₄=(1,3), e₅=(2,3)
#
# NBC 3-sets (verified by hand):
# Must avoid broken circuits from triangles:
#   {e₀,e₁}, {e₀,e₂}, {e₁,e₂}, {e₃,e₄}
# and from 4-cycles:
#   {e₀,e₂,e₃}, {e₀,e₁,e₄}, {e₁,e₂,e₃}
#
# Valid 3-sets:
nbc4 = []
from itertools import combinations as comb
bc_2sets = [{0,1}, {0,2}, {1,2}, {3,4}]
bc_3sets = [{0,2,3}, {0,1,4}, {1,2,3}]
for s in comb(range(6), 3):
    s_set = set(s)
    if any(bc.issubset(s_set) for bc in bc_2sets):
        continue
    if s_set in bc_3sets:
        continue
    nbc4.append(s)

edges4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
print(f"\nNBC basis for OS³(C₄): {len(nbc4)} elements")
for i, s in enumerate(nbc4):
    print(f"  ω_{i} = η_{edges4[s[0]]} ∧ η_{edges4[s[1]]} ∧ η_{edges4[s[2]]}")

if H1 == 8 and H2 == 36 and len(nbc4) == 6:
    print(f"\n--- d₄: g⊗⁴⊗OS³(C₄) → g⊗³⊗OS²(C₃) ---")
    print(f"  Source dim: {4096*6} = 24576")
    print(f"  Target dim: {512*2} = 1024")

    # For each pair (i,j) in {0,1,2,3}, we need:
    # 1. The bracket of factors at positions i,j
    # 2. The OS contraction ι_{ij}: OS³(C₄) → OS²(C₃)
    #
    # The OS contraction: ι_{ij}(η_S) where S is a 3-subset of edges.
    # ι_{ij} extracts η_{ij} from the form and substitutes z_i=z_j in the rest.
    #
    # After collision of vertices i,j → new vertex min(i,j):
    # relabel: vertices are {0,...,3}\{max(i,j)}, renumbered to {0,1,2}.
    # The target OS²(C₃) has basis {ω₀=η₀₁∧η₀₂, ω₁=η₀₂∧η₁₂} (0-indexed).

    # For each pair (i,j) and each NBC 3-set s:
    # ι_{ij}(η_{s[0]}∧η_{s[1]}∧η_{s[2]}) = ?
    # Case 1: (i,j) is one of the edges in s. Then extract it, get a 2-form.
    #         The remaining 2 edges are relabeled after merging i,j.
    #         Express in terms of the OS²(C₃) basis.
    # Case 2: (i,j) is not in s. Then ι_{ij} = 0.

    pairs4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    edge_to_idx = {e: i for i, e in enumerate(edges4)}

    def relabel_edge(e, i, j):
        """Relabel edge e after merging vertices i,j → min(i,j).
        Vertices > max(i,j) shift down by 1."""
        a, b = e
        merged = min(i, j)
        removed = max(i, j)
        # Replace i or j with merged
        if a == i or a == j:
            a = merged
        if b == i or b == j:
            b = merged
        # Shift down vertices > removed
        if a > removed:
            a -= 1
        if b > removed:
            b -= 1
        if a == b:
            return None  # degenerate
        return (min(a,b), max(a,b))

    # Target OS²(C₃) basis: ω₀=η₀₁∧η₀₂, ω₁=η₀₂∧η₁₂
    # (0-indexed vertices for C₃: {0,1,2})
    target_edges = [(0,1),(0,2),(1,2)]
    target_os_basis = [(0,1), (1,2)]  # indices into target_edges: η₀₁∧η₀₂ = (0,1), η₀₂∧η₁₂ = (1,2)
    # Arnold: η₀₁∧η₁₂ = η₀₁∧η₀₂ + η₀₂∧η₁₂, i.e. target_edge_pair (0,2) = ω₀ + ω₁

    def express_2form_in_os_basis(e1_idx, e2_idx):
        """Express η_{e1}∧η_{e2} in OS²(C₃) basis.
        e1_idx, e2_idx are indices into target_edges = [(0,1),(0,2),(1,2)].
        Returns (coeff_ω₀, coeff_ω₁)."""
        pair = (min(e1_idx, e2_idx), max(e1_idx, e2_idx))
        sign = 1 if e1_idx < e2_idx else -1

        # Basis: ω₀ = η₀∧η₁ (edges 0,1), ω₁ = η₁∧η₂ (edges 1,2)
        # Arnold: η₀∧η₂ (edges 0,2) = ω₀ + ω₁
        if pair == (0, 1):
            return (sign, 0)
        elif pair == (1, 2):
            return (0, sign)
        elif pair == (0, 2):
            return (sign, sign)  # η₀∧η₂ = ω₀ + ω₁
        else:
            return (0, 0)

    # Compute contraction table: iota4[pair_idx][source_os_idx] = (coeff_ω₀, coeff_ω₁)
    iota4 = {}
    for pi, (vi, vj) in enumerate(pairs4):
        eij_idx = edge_to_idx[(vi, vj)]
        iota4[pi] = {}
        for si, s in enumerate(nbc4):
            if eij_idx not in s:
                iota4[pi][si] = (0, 0)
                continue

            # Extract η_{ij} from the wedge product
            remaining = [e for e in s if e != eij_idx]
            # Position of eij in s determines sign
            pos = list(s).index(eij_idx)
            sign = (-1)**pos

            # Relabel remaining edges after merging vi, vj
            relabeled = []
            for e_idx in remaining:
                orig_edge = edges4[e_idx]
                new_edge = relabel_edge(orig_edge, vi, vj)
                if new_edge is None:
                    sign = 0
                    break
                relabeled.append(new_edge)

            if sign == 0 or len(relabeled) != 2:
                iota4[pi][si] = (0, 0)
                continue

            # Convert relabeled edges to target_edges indices
            te_indices = []
            for re in relabeled:
                if re in target_edges:
                    te_indices.append(target_edges.index(re))
                else:
                    sign = 0
                    break

            if sign == 0:
                iota4[pi][si] = (0, 0)
                continue

            # Express in OS² basis
            c0, c1 = express_2form_in_os_basis(te_indices[0], te_indices[1])
            iota4[pi][si] = (sign * c0, sign * c1)

    # Print contraction table
    print(f"\n  Contraction table ι: OS³(C₄) → OS²(C₃):")
    for pi, (vi,vj) in enumerate(pairs4):
        print(f"    D_{{{vi}{vj}}}:", end="")
        for si in range(len(nbc4)):
            c0, c1 = iota4[pi][si]
            print(f" ω{si}→({c0},{c1})", end="")
        print()

    # Now build d₄ matrix (24576 × 1024)
    # Source: (a₀,a₁,a₂,a₃,ω_s) → a₀*8³*6 + a₁*8²*6 + a₂*8*6 + a₃*6 + ω_s
    # Target: (b₀,b₁,b₂,ω_t) → b₀*8²*2 + b₁*8*2 + b₂*2 + ω_t

    t0 = time.time()
    # Use sparse matrix for d₄
    from scipy.sparse import lil_matrix

    n_os_s = len(nbc4)  # 6
    n_os_t = 2
    dim_src = dim_g**4 * n_os_s  # 24576
    dim_tgt = dim_g**3 * n_os_t  # 1024

    d4 = lil_matrix((dim_tgt, dim_src))

    for a0 in range(dim_g):
        for a1 in range(dim_g):
            for a2 in range(dim_g):
                for a3 in range(dim_g):
                    for ws in range(n_os_s):
                        src = a0*dim_g**3*n_os_s + a1*dim_g**2*n_os_s + a2*dim_g*n_os_s + a3*n_os_s + ws
                        factors = [a0, a1, a2, a3]

                        for pi, (vi, vj) in enumerate(pairs4):
                            c0, c1 = iota4[pi][ws]
                            if c0 == 0 and c1 == 0:
                                continue

                            # Bracket [factors[vi], factors[vj]]
                            bracket_results = []
                            for d in range(dim_g):
                                if sc[factors[vi], factors[vj], d] != 0:
                                    bracket_results.append((d, sc[factors[vi], factors[vj], d]))

                            if not bracket_results:
                                continue

                            # Remaining factors: all except vi, vj, with merged result at min(vi,vj)
                            remaining = [k for k in range(4) if k != vi and k != vj]
                            # Target tensor: (bracket_result, factors[remaining[0]], factors[remaining[1]])
                            # Order: merged position first, then remaining in order
                            merged_pos = min(vi, vj)
                            # Build target factor list: insert bracket at merged_pos
                            # remaining is sorted, and we need to figure out the order
                            # in the target g⊗³.

                            # After merging vi,vj → position min(vi,vj):
                            # The 3 remaining positions are sorted.
                            target_positions = sorted([merged_pos] + remaining)
                            # Map: merged_pos → bracket, remaining[k] → factors[remaining[k]]

                            for d, bracket_val in bracket_results:
                                # Build target tensor index
                                target_factors = [0, 0, 0]
                                for tp_idx, tp in enumerate(target_positions):
                                    if tp == merged_pos:
                                        target_factors[tp_idx] = d
                                    elif tp in remaining:
                                        target_factors[tp_idx] = factors[tp]

                                for wt, coeff in [(0, c0), (1, c1)]:
                                    if coeff == 0:
                                        continue
                                    tgt = (target_factors[0]*dim_g**2*n_os_t +
                                           target_factors[1]*dim_g*n_os_t +
                                           target_factors[2]*n_os_t + wt)
                                    d4[tgt, src] += bracket_val * coeff

    d4_csr = d4.tocsr()
    print(f"  Built d₄ in {time.time()-t0:.2f}s, shape {d4_csr.shape}, nnz={d4_csr.nnz}")

    # Check d₃ ∘ d₄ = 0
    d3_sparse = lil_matrix(d3).tocsr()
    comp34 = d3_sparse @ d4_csr
    print(f"  ||d₃∘d₄|| = {abs(comp34).max()}")

    # Compute rank of d₄ using dense SVD (1024 × 24576 is manageable)
    t0 = time.time()
    d4_dense = d4_csr.toarray()
    rank_d4 = np.linalg.matrix_rank(d4_dense)
    print(f"  rank(d₄) = {rank_d4} (computed in {time.time()-t0:.2f}s)")
    ker_d4 = dim_src - rank_d4
    print(f"  dim ker(d₄) = {ker_d4}")

    # H³ = ker(d₃)/im(d₄) = (1024-rank_d3) - rank_d4
    H3 = ker_d3 - rank_d4
    print(f"\n  H³_min = {ker_d3} - {rank_d4} = {H3} (expected 204)")

    print(f"\nSUMMARY:")
    print(f"  H¹ = {H1} (expected 8)")
    print(f"  H² = {H2} (expected 36)")
    print(f"  H³ = {H3} (expected 204)")

    if H3 == 204:
        print(f"\n  ALL THREE MATCH! Minimum weight captures bar cohomology.")
        print(f"  Need d₅ ({dim_g**5*24} × {dim_src}) for H⁴ — likely too large.")
        print(f"  H⁴ would require computing rank of a {dim_g**5*24} × {dim_src} matrix.")
    else:
        print(f"\n  H³ = {H3} ≠ 204. Minimum weight may not suffice, or construction has an error.")
