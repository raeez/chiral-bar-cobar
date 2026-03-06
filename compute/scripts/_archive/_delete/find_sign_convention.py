#!/usr/bin/env python3
"""Brute-force search for correct sign convention in chiral bar differential.

Try ALL 8 sign patterns for (1,2), (1,3), (2,3) with both bracket placements.
Also try different residue map sign choices.
"""

import numpy as np
from itertools import product as iproduct

# sl₂: basis {e, h, f} = {0, 1, 2}
dim = 3
sc = np.zeros((dim, dim, dim))
sc[1,0,0] = 2; sc[0,1,0] = -2   # [h,e]=2e
sc[1,2,2] = -2; sc[2,1,2] = 2   # [h,f]=-2f
sc[0,2,1] = 1; sc[2,0,1] = -1   # [e,f]=h

# d₂: B̄² → B̄¹. Just the bracket. d₂(a⊗b ⊗ η₁₂) = [a,b]
d2 = np.zeros((dim, dim*dim))
for a in range(dim):
    for b in range(dim):
        for k in range(dim):
            d2[k, a*dim+b] += sc[a,b,k]

print(f"d₂ rank: {np.linalg.matrix_rank(d2)}")
# rank 3 — so H¹ = dim B̄¹ - rank d₂ = 3 - 3 = 0
# But we want H¹ = 3! This means d₂ should be ZERO or we're indexing wrong.

# WAIT: Maybe d₂ = 0 for the CHIRAL bar complex.
# The OPE for KM: J^a(z)J^b(w) ~ k·κ^{ab}/(z-w)² + f^{ab}_c J^c(w)/(z-w)
# The residue of J^a⊗J^b ⊗ η₁₂ along D₁₂ extracts the simple pole: [J^a,J^b]
# But for the Heisenberg (example in manuscript), d_res(J⊗J⊗η₁₂) = k·1 (the double pole, not simple!)
#
# Actually re-read manuscript line 334:
# d_residue(J ⊗ J ⊗ η₁₂) = Res_{D₁₂}[J(z₁)J(z₂) ⊗ η₁₂]
# For Heisenberg: J(z)J(w) = k/(z-w)² (NO simple pole)
# Res extracts simple pole → d_res = 0 for Heisenberg in degree 2!
#
# For KM (sl₂): J^a(z)J^b(w) ~ kκ^{ab}/(z-w)² + [a,b]/(z-w)
# The form η₁₂ = dlog(z₁-z₂). Residue: ∮ f(z₁,z₂)·dlog(z₁-z₂) around z₁=z₂
# = ∮ f(z₁,z₂)·dz₁/(z₁-z₂) = (simple pole of f at z₁=z₂)
# So: Res_{D₁₂}(J^a(z₁)J^b(z₂) ⊗ η₁₂) picks out the SIMPLE pole coefficient = f^{ab}_c J^c
#
# So d₂ IS the bracket. And rank(d₂)=3 for sl₂, giving H¹=0.
# But we KNOW H¹=3 for the chiral bar cohomology!
#
# This means I'm WRONG about what B̄¹ is, or wrong about the grading, or
# the H¹=3 counts something different.

# Let me reconsider. From MEMORY.md:
# "sl₂ | Riordan R(n+3)" with H₀=R(3)=1, H₁=R(4)=3, ...
# But what does the indexing mean? H₀ might be degree 0 (constants), H₁ degree 1, etc.
#
# Maybe B̄⁰ = ground field, B̄¹ = g, B̄² = g⊗g⊗OS¹, etc.
# And d goes B̄ⁿ → B̄^{n-1}, so:
# H⁰ = ker(d₀)/0 = ker(d: B̄⁰→?) = ...
# Actually if the complex is 0 ← B̄⁰ ← B̄¹ ← B̄² ← ..., then
# H⁰ = B̄⁰/im(d₁) and H¹ = ker(d₁)/im(d₂).
#
# d₁: B̄¹ → B̄⁰ = {0→ground field}: this would be the counit/augmentation map.
# For a Lie algebra: d₁(a) = 0 (projection to degree 0 of the augmentation ideal).
# So ker(d₁) = B̄¹ = g, dim = 3.
# H¹ = ker(d₁)/im(d₂) = 3/im(d₂).
# If H¹ = 3, then im(d₂) = 0, meaning d₂ = 0!
#
# But we computed d₂ has rank 3 as the Lie bracket. So either:
# 1. The bar cohomology indexing starts at n=1 and H_1 = dim g = 3 means ker(d₁)/im(d₂)
#    and d₂ = 0 somehow, OR
# 2. I'm computing the wrong thing.

# Actually, let me reconsider what bar cohomology means here.
# The bar complex B̄ is the REDUCED bar construction. The key point:
# In the REDUCED bar complex, we quotient out by the augmentation ideal.
#
# For a Kac-Moody algebra, the bar cohomology H^n(B̄) counts the number of
# GENERATORS needed in a minimal cofree resolution, i.e., it's related to
# Ext groups. H¹ = dim(g) = generators, H² = relations, H³ = relations among
# relations, etc.
#
# In the standard bar-cobar theory:
# B̄(A) = (T^c(s^{-1}Ā), d) where Ā = ker(ε: A→k)
# The reduced bar complex.
# For a Lie algebra (or its UEA), the bar complex of U(g):
# B̄ⁿ(U(g)) involves (s^{-1}Ū(g))^⊗n.
#
# But the CHIRAL bar complex is different. B̄ⁿ = g^⊗n ⊗ OS^{n-1}(C_n).
# This is more like the operadic bar construction.
#
# For the operadic bar: the differential involves compositions (= OPE).
# In the operadic world, d²=0 comes from the operad axioms (associativity).
#
# OK let me just try to find signs that make d²=0 AND give H¹=3, H²=6 for sl₂.
# This means: d₂ MUST be zero (so H¹=3), and rank(d₃)=3 (so H²=9-3=6... wait that's 6! ✓)
#
# So H² = dim(ker d₂) - rank(d₃) = (9-0) - rank(d₃) = 9 - rank(d₃) = 6 → rank(d₃) = 3.
# And d₂ = 0.

# REVELATION: d₂ = 0 in the chiral bar complex!
# For KM algebras, this is because the simple pole residue of the OPE
# contracted with η₁₂ gives... wait, the simple pole gives [a,b].
# So d₂ ≠ 0 if we use the Lie bracket.
#
# Unless... the chiral bar complex uses a DIFFERENT operation than the Lie bracket.
# Or unless the bar complex starts at a different degree.
#
# Let me look at this from the scripts that worked (for sl₂ H¹=3):

# From MEMORY: chiral_bar_direct.py was validated for sl₂: H = [3, 6, 15, 36, 91]
# Let me re-examine that script.

# Actually, I think the issue is that the CHIRAL bar complex is NOT:
# B̄ⁿ = g^⊗n ⊗ OS^{n-1}(C_n) with d = Lie bracket ⊗ residue
#
# Instead, it's:
# B̄ⁿ = Sym^n(g[z,z⁻¹]) ⊗ OS^{n-1}(C_n) or something involving ALL conformal weights.
#
# In other words, B̄ⁿ involves not just g but all modes J^a_m, and the
# bar cohomology counts independent modes modulo OPE relations.
#
# H¹ = dim(g) counts the NUMBER OF GENERATORS (not the modes), i.e.,
# it's the dimension of g/[g,g] in some sense. For sl₂, dim(g)=3 and H¹=3
# because all generators are independent (none can be obtained from OPE of others).
#
# But wait, for the ADJOINT representation only (weight 1 states):
# J^a_-1 |0>, there are dim(g) of them. In the bar complex at degree 1,
# B̄¹ = Span{J^a_-1 | a=1,...,dim(g)}, and d₁ = 0, so H¹ = dim(g).
# Then d₂ maps B̄² → B̄¹, and d₂ = 0 would mean... hmm.
#
# Actually, I think the CORRECT picture is:
# The FULL chiral bar complex involves ALL conformal weights.
# At conformal weight h, B̄ⁿ_h = (modes of weight h in g^⊗n) ⊗ OS^{n-1}
# The bar cohomology decomposes by weight.
# At weight 1: B̄¹_1 = g (dim=d), B̄²_1 = 0 (no weight-1 states in g⊗g⊗η₁₂),
# so H¹_1 = d.
# The values [3, 6, 15, ...] are TOTAL bar cohomology, summing over all weights.
#
# This is getting too complicated for a brute-force sign search.
# Let me instead read the working code (chiral_bar_direct.py) more carefully.

print("Need to re-examine chiral_bar_direct.py for the working implementation.")
print("The issue is not signs — it's that the FULL bar complex involves all conformal weights.")
