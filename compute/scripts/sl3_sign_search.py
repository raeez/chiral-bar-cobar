#!/usr/bin/env python3
"""Search for correct signs in sl₃ bar differential.

The bar differential d = sum_{i<j} σ_{ij} · Res_{D_{ij}}
where σ_{ij} is a sign that includes Koszul, geometric, and operadic contributions.

At minimum weight with all generators in the same degree,
the sign reduces to a simple ±1 per pair.

We search over all sign assignments to find d²=0.
"""

import numpy as np
from itertools import product as iprod

dim_g = 8
H1, H2, E1, E2, E3, F1, F2, F3 = range(8)

# sl₃ structure constants
sc = np.zeros((dim_g, dim_g, dim_g))
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
sc[E1,F1,H1]=1;  sc[F1,E1,H1]=-1
sc[E2,F2,H2]=1;  sc[F2,E2,H2]=-1
sc[E1,E2,E3]=1;  sc[E2,E1,E3]=-1
sc[F1,F2,F3]=-1; sc[F2,F1,F3]=1
sc[E3,F3,H1]=1;  sc[E3,F3,H2]=1; sc[F3,E3,H1]=-1; sc[F3,E3,H2]=-1
sc[E1,F3,F2]=-1; sc[F3,E1,F2]=1
sc[E2,F3,F1]=1;  sc[F3,E2,F1]=-1
sc[E3,F1,E2]=-1; sc[F1,E3,E2]=1
sc[E3,F2,E1]=1;  sc[F2,E3,E1]=-1

# Build d₂: B̄² → B̄¹ (just the bracket, no sign freedom)
d2 = np.zeros((dim_g, dim_g**2))
for a in range(dim_g):
    for b in range(dim_g):
        for c in range(dim_g):
            d2[c, a*dim_g+b] += sc[a,b,c]

# For d₃, we have OS²(C₃) basis {ω₀, ω₁} and 3 pairs.
# The contraction structure is fixed by the OS algebra:
# ι₀₁: ω₀→α, ω₁→0
# ι₀₂: ω₀→β, ω₁→γ
# ι₁₂: ω₀→0, ω₁→δ
#
# where α, β, γ, δ ∈ {±1} encode the signs.
#
# Arnold relation: η₀₁∧η₁₂ = η₀₁∧η₀₂ + η₀₂∧η₁₂ = ω₀ + ω₁
# Alternatively, the signs depend on orientation choices.
#
# Physical constraint: the signs are determined by geometry.
# But let me search over (α,β,γ,δ) ∈ {±1}⁴ and also over
# the tensor ordering convention (whether we put bracket result first or last).

# The bracket part also has sign choices:
# Res_{D₀₁}: factors (0,1) → [a₀,a₁], remaining a₂ → position ?
# Option A: output = [a₀,a₁] ⊗ a₂ (bracket first)
# Option B: output = a₂ ⊗ [a₀,a₁] (bracket last)
# For pairs other than (0,1), the ordering matters.

# Let me parametrize more carefully.
# For each pair (i,j) in {(0,1),(0,2),(1,2)}, the output is:
# (result of merging i,j) ⊗ (remaining factor)
# with positions determined by min/max.

# After merging (0,1): merged→pos 0, remaining 2→pos 1. Output: [a₀,a₁]⊗a₂
# After merging (0,2): merged→pos 0, remaining 1→pos 1. Output: [a₀,a₂]⊗a₁
# After merging (1,2): merged→pos 0 is a₀, merged→pos 1. Output: a₀⊗[a₁,a₂]

# So the tensor ordering IS determined by the vertex ordering.
# The only freedom is in the OS contraction signs.

# Let me try: global sign σ_{ij} for each pair, PLUS the OS contraction sign.
# Total sign for pair (i,j) on OS element ω_k = σ_{ij} * ι_{ij}(ω_k)

# There are also operadic signs: (-1)^{sum of degrees of elements to the left}
# In the bar complex, elements have degree |sā| = |ā| - 1 = 0 (if |ā|=1, weight 1).
# So all Koszul signs are (-1)^0 = 1. No operadic signs at minimum weight.

# Search over all sign combinations
print("Searching for d²=0 signs...")
print(f"d₂ shape: {d2.shape}")

best = (1e10, None, None)

for s01, s02, s12 in iprod([1, -1], repeat=3):
    for alpha, beta, gamma, delta in iprod([1, -1], repeat=4):
        # Build d₃ with these signs
        # ι₀₁: ω₀→s01*alpha, ω₁→0
        # ι₀₂: ω₀→s02*beta, ω₁→s02*gamma
        # ι₁₂: ω₀→0, ω₁→s12*delta
        iota = {
            0: [s01*alpha, 0],
            1: [s02*beta, s02*gamma],
            2: [0, s12*delta],
        }

        d3 = np.zeros((64, 1024))
        for a in range(dim_g):
            for b in range(dim_g):
                for c in range(dim_g):
                    for omega in range(2):
                        src = a*dim_g*dim_g*2 + b*dim_g*2 + c*2 + omega
                        factors = [a, b, c]

                        # Res_{D₀₁}: [a,b]⊗c, ι₀₁(ω)
                        coeff = iota[0][omega]
                        if coeff != 0:
                            for d in range(dim_g):
                                if sc[a,b,d] != 0:
                                    d3[d*dim_g+c, src] += sc[a,b,d] * coeff

                        # Res_{D₀₂}: [a,c]⊗b, ι₀₂(ω)
                        coeff = iota[1][omega]
                        if coeff != 0:
                            for d in range(dim_g):
                                if sc[a,c,d] != 0:
                                    d3[d*dim_g+b, src] += sc[a,c,d] * coeff

                        # Res_{D₁₂}: a⊗[b,c], ι₁₂(ω)
                        coeff = iota[2][omega]
                        if coeff != 0:
                            for d in range(dim_g):
                                if sc[b,c,d] != 0:
                                    d3[a*dim_g+d, src] += sc[b,c,d] * coeff

        comp = d2 @ d3
        err = np.max(np.abs(comp))

        if err < best[0]:
            best = (err, (s01,s02,s12), (alpha,beta,gamma,delta))
            if err == 0:
                print(f"  FOUND d²=0: σ=({s01},{s02},{s12}), ι=({alpha},{beta},{gamma},{delta})")
                rank_d2_val = np.linalg.matrix_rank(d2)
                rank_d3_val = np.linalg.matrix_rank(d3)
                H1 = dim_g - rank_d2_val
                H2 = (dim_g**2 - rank_d2_val) - rank_d3_val
                print(f"    rank(d₂)={rank_d2_val}, rank(d₃)={rank_d3_val}")
                print(f"    H¹={H1}, H²={H2}")

print(f"\nBest: err={best[0]}, σ={best[1]}, ι={best[2]}")

if best[0] > 0:
    print("\nNo sign combination gives d²=0 with 2-element OS basis.")
    print("Trying alternative OS basis...")

    # Alternative: maybe the OS basis should be
    # {η₀₁∧η₁₂, η₀₁∧η₀₂} or {η₀₁∧η₀₂, η₀₁∧η₁₂}
    # Or maybe the issue is the ordering within the tensor product
    # after merging vertices.

    # Let me try a completely different approach:
    # For Res_{D₀₂}: the output ordering might be a₁⊗[a₀,a₂] instead of [a₀,a₂]⊗a₁
    # (i.e., the remaining factor keeps its position, bracket goes to merged position)

    print("\nTrying with alternative tensor orderings...")

    # For each pair, try both orderings of (bracket, remaining)
    for t01, t02, t12 in iprod([0, 1], repeat=3):
        for s01, s02, s12 in iprod([1, -1], repeat=3):
            # Fixed ι (from geometry):
            iota = {
                0: [s01, 0],
                1: [-s02, s02],
                2: [0, -s12],
            }

            d3 = np.zeros((64, 1024))
            for a in range(dim_g):
                for b in range(dim_g):
                    for c in range(dim_g):
                        for omega in range(2):
                            src = a*dim_g*dim_g*2 + b*dim_g*2 + c*2 + omega

                            # Res_{D₀₁}: merge 0,1. bracket=[a,b], remaining=c
                            coeff = iota[0][omega]
                            if coeff != 0:
                                for d in range(dim_g):
                                    if sc[a,b,d] != 0:
                                        if t01 == 0:
                                            d3[d*dim_g+c, src] += sc[a,b,d]*coeff
                                        else:
                                            d3[c*dim_g+d, src] += sc[a,b,d]*coeff

                            # Res_{D₀₂}: merge 0,2. bracket=[a,c], remaining=b
                            coeff = iota[1][omega]
                            if coeff != 0:
                                for d in range(dim_g):
                                    if sc[a,c,d] != 0:
                                        if t02 == 0:
                                            d3[d*dim_g+b, src] += sc[a,c,d]*coeff
                                        else:
                                            d3[b*dim_g+d, src] += sc[a,c,d]*coeff

                            # Res_{D₁₂}: merge 1,2. bracket=[b,c], remaining=a
                            coeff = iota[2][omega]
                            if coeff != 0:
                                for d in range(dim_g):
                                    if sc[b,c,d] != 0:
                                        if t12 == 0:
                                            d3[a*dim_g+d, src] += sc[b,c,d]*coeff
                                        else:
                                            d3[d*dim_g+a, src] += sc[b,c,d]*coeff

            comp = d2 @ d3
            err = np.max(np.abs(comp))
            if err == 0:
                rank_d3_val = np.linalg.matrix_rank(d3)
                H1 = dim_g - 8  # rank d2 = 8 always
                H2 = 56 - rank_d3_val
                print(f"  d²=0: σ=({s01},{s02},{s12}), t=({t01},{t02},{t12}), rank(d₃)={rank_d3_val}, H¹={H1}, H²={H2}")

    # If still nothing, the issue is deeper: maybe the bar complex uses the
    # COMMUTATOR bracket [a,b] = ab - ba in the associative algebra,
    # not the Lie bracket. Or maybe there's a curvature correction.
    # Or maybe the d₂ map itself should include the Killing form.

    print("\nTrying: d₂ includes Killing form (k-dependent double pole)...")
    # d₂(a⊗b ⊗ η₁₂) = [a,b] + k·κ(a,b)·|0⟩
    # The |0⟩ maps to B̄⁰ = ground field (degree 0).
    # So d₂ has TWO components:
    # d₂^{(1)}: B̄² → B̄¹ (bracket)
    # d₂^{(0)}: B̄² → B̄⁰ (Killing form)
    # Similarly d₃ has:
    # d₃^{(1)}: B̄³ → B̄² (bracket on one pair)
    # d₃^{(0)}: B̄³ → B̄¹ (double pole + remaining factor)
    #
    # For d²=0 at degree 3: d₂^{(1)} ∘ d₃^{(1)} + d₂^{(0)} ∘ d₃^{(2)} = 0
    # where d₃^{(2)}: B̄³ → B̄¹ involves double-pole contraction.
    # But d₂^{(0)}: B̄² → B̄⁰ (scalars), so d₂^{(0)} ∘ d₃^{(1)}: B̄³ → B̄⁰
    # and d₂^{(1)} ∘ d₃^{(1)}: B̄³ → B̄¹.
    # These map to DIFFERENT targets, so each must vanish separately.
    # So d₂^{(1)} ∘ d₃^{(1)} = 0 must hold on its own.
    # Which means our computation should have d²=0 for the bracket part alone.

    # Unless the bar complex is NOT simply B̄^n → B̄^{n-1},
    # but rather the TOTAL bar differential maps B̄ → B̄ and
    # d² = 0 on the TOTAL complex, with cancellation between
    # different degree components.

    # In the bar construction of an A∞-algebra:
    # d_bar = sum_n d_n where d_n: B̄^k → B̄^{k-n+1}
    # d²_bar = 0 encodes the A∞ relations.

    # For KM: m₂ = OPE (simple pole), m₁ = 0, m₀ = curvature (double pole)
    # The bar differential is:
    # d(a₁|...|aₙ) = sum_{i<j} ±m₂(aᵢ,aⱼ)⊗rest + sum_i ±m₁(aᵢ)⊗rest + m₀⊗...
    # d²=0 requires: m₂ satisfies Jacobi (homotopically) and m₁²=[m₀, -]

    # For the minimum weight, m₁=0, m₀=0 (the curvature/double pole
    # doesn't appear in the minimum weight sector).
    # So d = sum m₂ and d²=0 requires Jacobi for the Lie bracket.
    # But Jacobi IS satisfied (we verified it!).
    # So d²=0 MUST hold with the right signs.

    # The issue must be in my construction of the map.
    # Let me go back to first principles.

    print("\n" + "="*60)
    print("FIRST PRINCIPLES: Bar differential from operadic bar")
    print("="*60)

    # In the operadic bar construction (Loday-Vallette Ch. 6):
    # For a binary operad P and P-algebra A:
    # B(A) = (T^c(sA), d) where d(sa₁⊗...⊗saₙ) = sum ±sa₁⊗...⊗sμ(aᵢ,a_{i+1})⊗...⊗saₙ
    # This is for the ASSOCIATIVE operad (only adjacent compositions).

    # For the COMMUTATIVE (chiral) operad:
    # d(sa₁⊗...⊗saₙ) = sum_{i<j} ±sa₁⊗...⊗sμ(aᵢ,aⱼ)⊗...⊗saₙ
    # ALL pairs, not just adjacent.

    # The suspension shift: |sa| = |a| - 1. For a in degree 0 (Lie algebra elements),
    # |sa| = -1. The Koszul sign rule gives:
    # d(sa₁⊗sa₂⊗sa₃) = sum_{i<j} (-1)^{|sa₁|+...+|sa_{i-1}|} sμ(aᵢ,aⱼ) ⊗ rest

    # For degree-0 elements, all |sa_k| = -1, so:
    # d(sa₁⊗sa₂⊗sa₃) = (-1)^0 sμ(a₁,a₂)⊗sa₃ (pair 1,2)
    #                   + (-1)^{|sa₁|} sμ(a₁,a₃)⊗sa₂ (pair 1,3)... hmm

    # Actually the sign depends on the exact convention.
    # In the Chevalley-Eilenberg complex for Lie algebras:
    # d(x₁∧...∧xₙ) = sum_{i<j} (-1)^{i+j+1} [xᵢ,xⱼ]∧x₁∧...∧x̂ᵢ∧...∧x̂ⱼ∧...∧xₙ

    # The CE complex uses ANTISYMMETRIC tensor products (exterior algebra).
    # But the bar complex uses SYMMETRIC tensor products (or rather, the cofree coalgebra).

    # For the COMMUTATIVE operad bar:
    # B(A) = (Sym^c(sĀ), d) (cofree COCOMMUTATIVE coalgebra)
    # and d uses the Lie bracket with signs from the commutative operad.

    # For the CHIRAL operad bar:
    # B(A) = (cofree coalgebra over chiral cooperad, d)
    # The cofree structure is indexed by configuration spaces.
    # B̄^n = A^⊗n ⊗ OS^{n-1} (NOT symmetric in the factors).

    # The bar differential in the chiral case:
    # d(a₁⊗...⊗aₙ ⊗ ω) = sum_{i<j} [aᵢ,aⱼ] ⊗ (rest) ⊗ ι_{ij}(ω)
    # where the remaining factors are in positions {1,...,n}\{i,j} ∪ {ij}
    # relabeled to {1,...,n-1}.

    # The sign comes from:
    # 1. Moving aᵢ and aⱼ adjacent (Koszul sign)
    # 2. The operadic composition sign
    # 3. The OS contraction sign

    # For elements of degree 0 (weight-1 modes), Koszul signs are trivial.
    # The OS contraction sign is determined by geometry.
    # The operadic sign... let me check.

    # Actually, in the REDUCED bar complex, the elements are in the desuspended
    # augmentation ideal: s⁻¹Ā. For KM algebra generators J^a (of conformal weight 1,
    # which has cohomological degree... what?).

    # In the manuscript's convention: |d| = +1 (cohomological).
    # J^a has conformal weight 1, but what is its cohomological degree?
    # In the bar complex, the suspension gives |s⁻¹J^a| = |J^a| + 1.
    # If J^a is in degree 0, then |s⁻¹J^a| = 1.
    # If J^a is in degree 1, then |s⁻¹J^a| = 2.

    # The sign issue comes from the degree of the bar elements.
    # Let me try both: elements in degree 0 and degree 1.

    # Actually the simplest thing: try the CE differential sign convention
    # and see if it works.

    print("\nTrying CE-type signs: d(a∧b∧c) = [a,b]∧c - [a,c]∧b + [b,c]∧a")

    # CE differential on ∧³(g) → ∧²(g):
    # d(a∧b∧c) = [a,b]∧c - [a,c]∧b + [b,c]∧a
    # Signs: (+1, -1, +1) for pairs (01, 02, 12)

    # But in the bar complex, we have g⊗³ ⊗ OS² (NOT ∧³(g)).
    # The OS² piece plays the role of the "form factor".

    # In the CE complex: ∧ⁿ(g*) with d induced by [,].
    # d(f)(x₁,...,xₙ) = sum_{i<j} (-1)^{i+j} f([xᵢ,xⱼ], x₁,...,x̂ᵢ,...,x̂ⱼ,...,xₙ)
    #                 + sum_i (-1)^{i+1} xᵢ · f(x₁,...,x̂ᵢ,...,xₙ)
    # (second part is zero for adjoint action on trivial coefficients)

    # The sign (-1)^{i+j} for pairs:
    # (0,1): (-1)^{0+1} = -1
    # (0,2): (-1)^{0+2} = +1
    # (1,2): (-1)^{1+2} = -1

    # With OS contraction signs from before:
    for ce_signs in [(-1,1,-1), (1,-1,1)]:
        d3 = np.zeros((64, 1024))
        for a in range(dim_g):
            for b in range(dim_g):
                for c in range(dim_g):
                    for omega in range(2):
                        src = a*dim_g*dim_g*2 + b*dim_g*2 + c*2 + omega

                        # ι values from geometry
                        iota_vals = {
                            0: [1, 0],
                            1: [-1, 1],
                            2: [0, -1],
                        }

                        for pair_idx, (vi, vj) in enumerate([(0,1),(0,2),(1,2)]):
                            coeff = iota_vals[pair_idx][omega] * ce_signs[pair_idx]
                            if coeff == 0:
                                continue

                            remaining = [k for k in range(3) if k != vi and k != vj][0]
                            fa = [a,b,c]

                            for d in range(dim_g):
                                if sc[fa[vi], fa[vj], d] != 0:
                                    # Output: bracket at merged pos, remaining at other pos
                                    merged = min(vi, vj)
                                    if merged < remaining:
                                        tgt = d*dim_g + fa[remaining]
                                    else:
                                        tgt = fa[remaining]*dim_g + d
                                    d3[tgt, src] += sc[fa[vi],fa[vj],d] * coeff

        comp = d2 @ d3
        err = np.max(np.abs(comp))
        if err == 0:
            rank_d3_val = np.linalg.matrix_rank(d3)
            H2 = 56 - rank_d3_val
            print(f"  d²=0 with CE signs {ce_signs}! rank(d₃)={rank_d3_val}, H²={H2}")
        else:
            print(f"  CE signs {ce_signs}: ||d²||={err}")

    # Full brute force: 3 pairs × 2 OS elements = 6 entries in iota table
    # with values ±1 or 0. But the 0 positions are fixed by which pairs
    # appear in which OS basis element.
    # Really the freedom is: for ι₀₁(ω₀), ι₀₂(ω₀), ι₀₂(ω₁), ι₁₂(ω₁)
    # each ∈ {+1, -1}, giving 2⁴ = 16 combinations.
    # Plus tensor ordering: 2³ = 8 for (bracket,remaining) vs (remaining,bracket).
    # Total: 16 × 8 = 128 combinations.

    print("\nFull brute force: 128 combinations...")
    found_any = False
    for signs in iprod([1,-1], repeat=4):
        iota_vals = {
            0: [signs[0], 0],
            1: [signs[1], signs[2]],
            2: [0, signs[3]],
        }
        for orderings in iprod([0,1], repeat=3):
            d3 = np.zeros((64, 1024))
            for a in range(dim_g):
                for b in range(dim_g):
                    for c in range(dim_g):
                        for omega in range(2):
                            src = a*dim_g*dim_g*2 + b*dim_g*2 + c*2 + omega
                            fa = [a,b,c]

                            for pair_idx, (vi,vj) in enumerate([(0,1),(0,2),(1,2)]):
                                coeff = iota_vals[pair_idx][omega]
                                if coeff == 0:
                                    continue
                                remaining = [k for k in range(3) if k != vi and k != vj][0]

                                for d in range(dim_g):
                                    if sc[fa[vi],fa[vj],d] != 0:
                                        if orderings[pair_idx] == 0:
                                            tgt = d*dim_g + fa[remaining]
                                        else:
                                            tgt = fa[remaining]*dim_g + d
                                        d3[tgt, src] += sc[fa[vi],fa[vj],d] * coeff

            comp = d2 @ d3
            err = np.max(np.abs(comp))
            if err == 0:
                rank_d3_val = np.linalg.matrix_rank(d3)
                H1 = dim_g - 8
                H2 = 56 - rank_d3_val
                if H2 > 0:
                    found_any = True
                    print(f"  d²=0: signs={signs}, order={orderings}, rank(d₃)={rank_d3_val}, H¹={H1}, H²={H2}")

    if not found_any:
        print("  No combination gives d²=0 with positive H².")
        print("  The issue may be deeper — perhaps the bar complex is NOT")
        print("  just the bracket differential on g⊗n ⊗ OS^{n-1}.")
