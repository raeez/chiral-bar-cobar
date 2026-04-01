# The Four Overclaims: Reimagined from First Principles

## Overclaim 1: Z = C^•_ch(A,A) as the known bulk / MTC at integrable levels

### What was claimed
"The derived center Z = C^•_ch(V_k(g), V_k(g)) is the bulk algebra for Chern-Simons. At rational/integrable levels, its decategorified shadow is the familiar modular tensor category."

### Why it's overclaimed
Two distinct mathematical objects are being conflated:

(a) The **chiral Hochschild cochain complex** C^•_ch(A,A) — a chain-level dg algebra, defined for any A∞-chiral algebra. Its cohomology Z^der_ch(A) is the universal bulk by the Swiss-cheese theorem.

(b) The **center of the modular tensor category** of V_k(g)-modules at integrable level k — a finite-dimensional commutative algebra, the Verlinde ring.

The claim that (a) "decategorifies" to (b) requires a chain of identifications:
- C^•_ch(V_k(g), V_k(g)) → HH^*(V_k(g), V_k(g)) (take cohomology)
- HH^*(V_k(g), V_k(g)) → Z(V_k(g)-mod) (Keller's identification, requires compact generation)
- Z(V_k(g)-mod) → Verlinde ring (at integrable levels, the module category is semisimple)

Each step has hypotheses. The first is tautological. The second requires V_k(g) to be a compact generator of its module category — this fails at non-generic levels (admissible levels, critical level). The third is specific to the integrable case.

### The mathematically true form

**Theorem (Chain-level universal bulk).** Let A be a curved A∞-chiral algebra. The pair U(A) = (C^•_ch(A,A), A) is the terminal local chiral open/closed pair (thm:thqg-swiss-cheese). The chiral derived center Z^der_ch(A) = H*(C^•_ch(A,A), δ) is a Gerstenhaber algebra; on the Koszul locus it is concentrated in degrees {0,1,2} (Theorem H).

**Proposition (Boundary-linear identification).** For a logarithmic SC^{ch,top}-algebra, bulk local operators are quasi-isomorphic to chiral Hochschild cochains: O_bulk ≃ C^•_ch(A_∂, A_∂). This is proved unconditionally (thm:bulk_hochschild). The further identification bulk ≃ Z_der(C_∂) requires compact generation, which is verified in the boundary-linear exact sector.

**Conjecture (Decategorification at integrable levels).** For V_k(g) at integrable level k, the passage
Z^der_ch(V_k(g)) → Z(Rep(V_k(g))) → Verlinde ring
is the zeroth cohomology of a natural dg-to-abelian functor. This should be checkable by direct computation of HH^0(V_k(g)) = dim V_k(g)-mod.

**What the programme should do:** Compute HH^0(V_k(g), V_k(g)) explicitly for g = sl_2 at small integrable levels (k = 1, 2, 3) and verify it matches the known Verlinde algebra dimensions. This is a finite computation.

---

## Overclaim 2: MC(A)^dg = Perf(A!) as a generic local theorem

### What was claimed
"For any A∞-chiral algebra A, the open primitive is the MC coupling dg-category Line(A), equivalent to Perf(A!)."

### Why it's overclaimed
The equivalence Line(A) ≃ Perf(A!) requires:
1. A! to be well-defined — this needs A to be Koszul (or at least augmented with well-defined bar cohomology)
2. The MC coupling to produce a genuine dg-category — this needs convergence of the A∞ sums
3. The functor Line(A) → Perf(A!) given by μ_ℓ = (ρ_ℓ ⊗ 1)(μ) to be an equivalence — this is the Koszul duality comparison

For non-Koszul algebras, A! may not exist, or it may exist but not be the right object (the bar cohomology may not be concentrated). For algebras with convergence issues (non-positive-energy, or at critical level), the MC sums may diverge.

### The mathematically true form

**Definition (MC coupling category).** For any A∞-algebra A, define Line(A) as the dg-category whose objects are pairs (V, μ) with μ ∈ End(V) ⊗̂ A satisfying the A∞ MC equation, and morphisms are Hom(V,W) ⊗̂ A with the twisted differential. This is always well-defined (no hypothesis on A beyond A∞ structure and convergence of the completed tensor product).

**Theorem (Koszul comparison, proved).** If A is chirally Koszul (bar cohomology concentrated in bar degree 1), then A! = (H*(B(A)))^∨ is well-defined and the comparison functor
    Line(A) → Perf(A!)
    (V, μ) ↦ (V, ρ = (1 ⊗ π)(μ))
where π: A → A! is the canonical projection, is a quasi-equivalence.

**Proposition (Perturbative range).** For perturbative 3d HT QFT (where 1-loop exactness holds), the MC coupling category Line(A) is well-defined with objects = perturbative line operators, and the Koszul comparison holds whenever A is chirally Koszul.

**What is genuinely open:** The MC coupling category for non-Koszul algebras (e.g., simple quotient W_k(g) at admissible levels) or at the boundary of convergence (critical level k = -h∨). For these, Line(A) may exist but have no nice algebraic presentation.

**The honest statement:** Line(A) is always the correct primitive (it is defined intrinsically from the A∞ structure). The equivalence Line(A) ≃ Perf(A!) is a CONSEQUENCE OF KOSZULNESS, not a definition. The programme's 10+1+1 Koszulness characterization is exactly the characterization of when this equivalence holds.

---

## Overclaim 3: Global gluing of C_op into a factorization cosheaf

### What was claimed
"These local categories glue into a constructible dg-cosheaf C_op on Ran_∂(X,D,τ)."

### Why it's overclaimed
This is stated as a "Global theorem" but is actually a definition + a claim that the definition satisfies certain properties. The properties that need verification:

1. **Local constancy:** C restricted to a chamber of ordered disjoint points is the external tensor product of local categories. This is a definition.

2. **Weiss descent:** C satisfies descent for Weiss covers of the boundary configuration space. This requires verifying that the local-to-global comparison map is an equivalence — a genuine theorem requiring proof.

3. **Collision extension:** C extends across the compactified boundary strata (where points collide) by the meromorphic tensor product. This requires the OPE associativity to give well-defined limit objects — a convergence condition.

4. **Compatibility with interior:** The mixed open/closed structure (interior bulk points + boundary open points) satisfies the Swiss-cheese coherence conditions. This is the content of the Swiss-cheese operad acting on the cosheaf.

### The mathematically true form

**Definition (Local collar category).** For a small interval J ⊂ I_p on the real-oriented blowup, the collar category C_J is Line(A_J) — the MC coupling category of the local boundary algebra. This is always well-defined.

**Proposition (Factorization on disjoint intervals, proved).** For disjoint intervals J₁, J₂ ⊂ I_p, the external tensor product functor C_{J₁} ⊠ C_{J₂} → C_{J₁ ∪ J₂} is an equivalence. This follows from the E₁-factorization structure of the open color.

**Theorem (Extension across collisions, conditional).** The meromorphic tensor product ℓ ⊗_z ℓ' extends the factorization structure across collision strata, provided:
(a) The OPE of line operators converges (guaranteed in the perturbative 1-loop exact regime),
(b) The spectral R-matrix R(z) satisfies YBE (proved on the chirally Koszul locus).

**Programme (Weiss descent).** The Weiss descent condition on the full boundary configuration space requires the local-to-global map to be an equivalence on each stratum of the Ran space. This is the categorical analogue of the Beilinson-Drinfeld factorization axiom. For factorization ALGEBRAS (one-object case), BD prove this. For factorization CATEGORIES, the analogous result requires:
(a) The categorical Ran-space formalism (Raskin, Beraldo),
(b) The boundary/open-sector analogue on the real-oriented blowup (not yet written).

**The honest statement:** The local construction (collar categories, meromorphic tensor product, E₁-factorization on disjoint intervals) is a theorem. The global cosheaf structure (Weiss descent on the full boundary Ran space) is a well-defined programme with clear inputs from the categorical Ran-space literature, but the boundary-specific verification has not been carried out. Calling it a "theorem" is premature; calling it a "construction" with a "Weiss descent conjecture" is honest.

---

## Overclaim 4: The A∞ structure on H^{b₀,•}(S³) beyond tree level

### What was claimed
"The non-planar/higher structure [of twisted holography] is controlled by the A∞ algebra H^{b₀,•}(S³) = (H^{b₀,•}(S³), m₂, m₃, ...)"

### Why it's overclaimed
Costello-Gaiotto identify the tree-level structure of the twisted holographic duality. The tree-level OPE of single-trace operators is controlled by the A∞ structure on cohomology of the three-sphere with flat connections. At tree level, this is the classical (non-deformed) structure.

The claim that the FULL A∞ structure (all higher operations m_k for k ≥ 3, at all loop orders) controls the complete non-planar twisted holography is the programme's own construction. It would follow from:
1. The homotopy transfer theorem (HTT) applied to the 5d/3d Kaluza-Klein reduction,
2. The identification of the transferred operations with the non-planar corrections.

Step (1) is standard homological algebra. Step (2) is the conjectural part: the claim that the HTT transfer from the full 5d theory to the 3d KK-reduced theory reproduces the non-planar corrections to the OPE of single-trace operators.

### The mathematically true form

**Theorem (Tree-level A∞, standard).** The Kaluza-Klein reduction of 5d holomorphic Chern-Simons on C × S³ to 3d HT theory on C × ℝ is controlled at tree level by the A∞ structure on H^{b₀,•}(S³) obtained by homotopy transfer from the dg algebra Ω^{0,•}(S³). The transferred products m₂, m₃, ... are computed by tree-level Feynman diagrams on S³.

**Conjecture (All-loop A∞, programme).** The full non-planar structure (at all loop orders in 1/N) is controlled by a DEFORMED A∞ structure on H^{b₀,•}(S³), where the deformation parameter is 1/N (or equivalently ε₁ in the Ω-background). The deformed operations m_k^{(g)} at genus g are the g-loop corrections to the KK transfer.

**What is proved:** The tree-level structure (g = 0). The existence of the deformed A∞ structure (from the general theory of A∞ algebras in families). The identification of the deformation parameter with 1/N.

**What is not proved:** That the deformed A∞ structure reproduces the known non-planar corrections to the twisted holographic OPE at each loop order. This would require comparing the HTT output with explicit non-planar Feynman diagram computations — a substantial computation that has not been carried out.

**The honest statement:** The tree-level A∞ structure on H^{b₀,•}(S³) is standard. The claim that this A∞ structure "controls" the full non-planar twisted holography is a conjecture — a precise and plausible conjecture with a clear formulation, but not a theorem.

---

## Summary: The True Forms

| Overclaim | Mathematically true form | Status |
|-----------|------------------------|--------|
| Z = C^•_ch(A,A) as known bulk | C^•_ch(A,A) is the UNIVERSAL bulk (proved). Its identification with SPECIFIC bulk algebras (Verlinde ring, etc.) is conditional on compact generation. The checkable computation: HH^0(V_k(sl_2)) at k=1,2,3. | Theorem (abstract) + Conjecture (specific) |
| MC(A)^dg = Perf(A!) generically | MC(A)^dg = Line(A) is ALWAYS the correct primitive. The equivalence Line(A) ≃ Perf(A!) is a CONSEQUENCE OF KOSZULNESS, not a definition. | Theorem (on Koszul locus) + Open (off locus) |
| Global factorization cosheaf | Local construction is a theorem. E₁-factorization on disjoint intervals is a theorem. Global Weiss descent on boundary Ran space is a well-posed programme, not a theorem. | Theorem (local) + Programme (global) |
| A∞ on H^{b₀,•}(S³) all loops | Tree-level is standard. Full non-planar = deformed A∞ with parameter 1/N. Identification with known corrections is the conjecture. | Theorem (tree) + Conjecture (loops) |
