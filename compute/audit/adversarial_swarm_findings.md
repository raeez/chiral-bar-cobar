# Adversarial Swarm Findings — Synthesis

## CRITICAL (must fix or the mathematics is incomplete)

### Costello Finding 8: PHANTOM REFERENCE
thm:e1-factorization-disjoint (foundations.tex) cites `prop:mc-homotopy-invariance` which **DOES NOT EXIST** anywhere in either volume. This is a load-bearing result: the E₁ factorization structure is the foundation of the entire open-color theory. The missing proposition — homotopy invariance of the MC coupling category — is standard (Seidel, Fukaya, Kontsevich-Soibelman) but needs to be proved or cited.

## SERIOUS (structural weaknesses)

### Dirac: The four-stage architecture is NOT minimal
- Stages 1 and 2 are the same observation (Morita theory). One definition suffices.
- Stage 3 is a conjecture, not a theorem. Cannot be a "stage" of a proved architecture.
- Stage 4 is already implicit in the definition of C (axiom (vi): clutching).
- The MINIMAL decomposition has TWO stages: (1) define C with clutching, (2) observe that the ordered bar is an E_1 coalgebra and that the genuine SC datum appears only on the derived-center pair.
- The "corrected big picture" remark has 6 points but only 1 is independent. The rest are consequences.

### Dirac: The chapter is 25-30% scaffolding
- 21 remarks outnumber theorems (8) by factor 2.6.
- Subsection "Configuration spaces and higher operations" is 82 words, zero content. DELETE.
- rem:corrected-big-picture: 6 points → 1 sentence.
- Multiple remarks restate the same insight (Steinberg analogy appears twice; "single phenomenon" restates prop:five-theorems-geometry).

### Witten: "Θ^oc IS the gravitational partition function" is a SLOGAN, not a theorem
- Perturbative, single-saddle, scalar-level only.
- Does not include non-perturbative corrections (BTZ, Farey tail, phase transitions).
- The actual CS partition function involves continuous spectrum, Plancherel measure for SL(2,R).
- The programme has produced ONE genuinely new computable invariant: Q^contact = 10/[c(5c+22)]. This has NOT been checked against any independent computation.
- F₁ = (c-26)/48 is correct (matches known one-loop CS). Beyond genus 1, nothing is checked.

### Witten: "Shadow archetypes classify gravitational dynamics" is a CATEGORY ERROR
- 3d HT gravity is topological — it has no local dynamics.
- Shadow archetypes classify boundary A∞ complexity, not bulk dynamics.
- The table labeling shadow data as "three-graviton vertex" etc. is interpretation, not derivation.

### Witten: Worked examples are CATALOGUED, not COMPUTED
- Twisted holography: no OPE coefficients computed from the framework.
- M2/M5: generators listed from literature, κ and shadow archetype both OPEN.
- A physicist cannot extract a single prediction from these sections without going back to cited papers.

### Witten: "modularity = trace + clutching" is a TAUTOLOGY at the formal level
- The MC equation is automatically satisfied (Θ defined as D_A - d_0, and D²=0 is a theorem).
- The principle becomes a genuine constraint only with analytic conditions (convergence, unitarity).
- At the formal algebraic level, it constrains nothing.

### Costello: Six categorical gaps in the foundations
1. Tensor product ⊗_α for dg-categories: WHICH tensor product? Unspecified.
2. Compatibilities between the 6 axioms of def:oc-factorization-category: NOT stated.
3. Completion ⊗̂ in def:mc-coupling-category: pronilpotent? adic? Unspecified.
4. E₁-factorization proof conflates retraction of SPACES with equivalence of CATEGORIES.
5. holim of dg-categories in conj:weiss-descent: not well-typed without ∞-categorical framework.
6. Annulus trace proof conflates E₁-algebra factorization homology with E₁-category factorization homology.

### Costello: Weiss descent "conjecture" is mislabeled
- It's not a conjecture (truth is not in doubt) and not a definition.
- It's a GAP: expected to hold, verification not written.
- The recognition theorem USES Weiss descent (lem:product-weiss-descent) and is tagged ProvedHere. Inconsistent.

## MODERATE

### Dirac: conj:weiss-descent should be "Expected" not "Conjecture"
- A conjecture suggests uncertain truth. This is routine verification not yet done.

### Dirac: Koszul comparison hypothesis could be weakened
- thm:koszul-comparison-mc requires Koszulness. The actual hypothesis is bar-cobar inversion (weaker).

### Witten: BTZ entropy derivation is standard Cardy re-labeled
- No new content from MC framework. Brown-Henneaux 1986 suffices.

### Costello: Annulus trace not in Vol II live build
- Theorem lives only in Vol I (cross-volume dependency). Vol II has no self-contained proof.

## VERIFIED/CORRECT

### Witten: F₁ = (c-26)/48 matches known one-loop CS ✓
### Witten: Q^contact = 10/[c(5c+22)] is a genuine new computation ✓
### Witten: κ + κ' = 13 for Virasoro is correct ✓
### Costello: Swiss-cheese theorem (thm:thqg-swiss-cheese) has genuine proof with valid deferred target ✓
### Costello: Weiss descent honestly labeled as conjecture ✓

## CRITICAL: Beilinson — The reconception has overclaimed

### "Every object is a projection of Θ^oc" is LITERALLY FALSE
The curve X, the Ran space, FM compactification, Arnold relations, D-module structure — none are projections. The honest version: "Every algebraic invariant of the genus expansion is a projection of Θ_A."

### "Every theorem is a consequence of the MC equation" is FALSE
Theorem B (bar-cobar inversion) uses PBW concentration + Barr-Beck-Lurie comparison — logically independent of the MC equation. The MC element exists because D²=0; but existence of MC ≠ the five theorems.

### The reconception DEMOTES proved math for programmatic math
The bar complex has 1400pp of proofs. The open factorization category has definitions and one theorem. Calling the proved object a "shadow" and the defined object the "primitive" inverts the proved-to-conjectural hierarchy. The reconception is a PARTIALLY correct idea treated as FULLY correct.

### N4 (modularity = trace+clutching) at genus ≥ 2 is a CONJECTURE presented as a PRINCIPLE
Theorem D gives the explicit formula κ·λ_g. N4 says this should also come from clutching — but this computation has not been done. The principle replaces a proved formula with an unproved mechanism.

### The four-stage architecture creates an illusion of 75% completion
Stage 1 carries the entire mathematical weight. Stages 2-4 add progressively less proved content and more programmatic assertion.

### Three errors of the reconception:
1. **Scope inflation** (AP7/AP28): universal quantifiers that are false
2. **Status inversion**: demoting proved objects, promoting defined ones
3. **Premature retrospective coherence**: rewriting history as if platonic order were logical order

### The correct Beilinsonian verdict:
Keep: bar≠bulk (proved), derived center = universal bulk (proved at Stage 1), Morita invariance (proved). Dismiss: "every object is a projection," "every theorem is a consequence," universal scope of N4.

## SOUND: Kontsevich — Operadic foundations are solid

### Homotopy-Koszulity proof: COMPLETE AND CORRECT
Three-step argument (classical Koszulity + Kontsevich formality + transfer) is fully verified with explicit two-colored operad map checking.

### "Partially modular" operad: PRECISELY DEFINED, ORIGINAL, HONEST
15 axioms, comparison with Getzler-Kapranov and Vallette explicitly stated. The manuscript does not overclaim novelty.

### Relative Feynman transform: ORIGINAL, COMPLETE WITH SIGNS
Signs specified in full Koszul convention. Bicomplex condition proved. Two worked examples verify identities.

### Moderate gaps:
- Quillen equivalence: model structures on coalgebra categories cited but not fully specified
- "Quasi-isomorphism in coderived category": used but not defined
- "Shadow Postnikov tower": deformation-theoretic analogy, not genuine Postnikov; should be qualified

### Overall: the operadic machinery is the STRONGEST part of the programme

## Polyakov: The programme is purely perturbative

### Honest scope: rigorous perturbative machine, not a theory of quantum gravity
- Programme computes genus-by-genus coefficients F_g with algebraic precision
- Does NOT reproduce BTZ entropy (correctly tagged Conjectured)
- Does NOT see non-perturbative effects (no saddle points, no phase transitions, no sum over geometries)
- Resurgent structure is conjectural beyond Virasoro

### Two claims that must be corrected:
1. "MC replaces the sum over topologies" (preface line 1872) — OVERSCOPED. MC replaces ambiguity within the perturbative expansion, not the gravitational sum over three-manifold topologies.
2. The gap between SL(2,R) (physical gauge group) and the complex algebraic framework is NEVER ACKNOWLEDGED. The manuscript works over C throughout but the physics needs R.

### Never discussed:
- Quantum corrections to Brown-Henneaux c = 3ℓ/(2G)
- Hawking-Page phase transition
- The Maloney-Witten problem (negative Fourier coefficients in Poincaré series)
- Real vs complex Chern-Simons (Giombi-Maloney-Yin analytic continuation)

### What the actual gravitational partition function is vs what the programme computes:
- Actual: Z(τ) = |q^{-c/24} ∏(1-q^n)^{-1}|² × (sum over geometries)
- Programme: the Taylor coefficients F_g of the asymptotic expansion of log|η(τ)|^{-2c}
- The programme does not compute the eta function itself, let alone the sum over geometries

## Gaiotto: Two formula errors found and FIXED

### SERIOUS: S_6 and S_7 WRONG in Vol II rosetta_stone.tex (AP1/AP5 violation)
- S_6 was (460c+1768)/[c³(5c+22)²], correct is 80(45c+193)/[3c³(5c+22)²]
- S_7 was -48(115c+396)/[c⁴(5c+22)²], correct is -2880(15c+61)/[7c⁴(5c+22)²]
- Correct values confirmed in Vol I at 4+ locations + compute layer
- **FIXED** in rosetta_stone.tex

### All other formulas VERIFIED CORRECT:
- κ(V_k(g)) = dim(g)(k+h∨)/(2h∨): verified for sl_2 at k=1 and k=-2
- Q^contact = 10/[c(5c+22)]: correct, poles at c=0 and c=-22/5
- W_3 composite Λ = :TT: - 3/10 ∂²T: correct Zamolodchikov normalization
- BRST charge Q_BRST = ∮ Tr(cZ₁Z₂ + cIJ + ½bc²): correct
- DDCA relation sign (mp-nq): matches Guay convention
- Verlinde S-matrix: correct standard convention, charge conjugation C=I for sl_2

## Drinfeld: Yangian identification correct for finite Y(g)

### Three naming/structural issues:
1. "dg-shifted Yangian" is a new structure (A∞ bialgebra with spectral parameter), NOT Drinfeld Y(g)
2. No antipode defined — the definition is a bialgebra, not Hopf
3. "Affine Yangian specialization" title misleading — constructs finite Y(g), not affine Y(ĝ)

### Verified correct:
- RTT presentation matches for Y(g) at ℏ = 1/(k+h∨)
- Full quantum YBE R₁₂R₁₃R₂₃ = R₂₃R₁₃R₁₂ proved (not just classical)
- DDCA epsilon constraint ε₃ = -Kε₁ - ε₂ correct for K M2 branes
- DK status levels accurately stated in manuscript

## Segal: Modularity framework architecturally sound, comparison missing

### SERIOUS: "modularity" means different things
- Segal: Z invariant under MCG (constraint)
- Manuscript: Z produced by clutching (construction)
- The equivalence is never stated as a theorem

### SERIOUS: MCG-equivariance rests on 3-line remark
- rem:modular-invariance-tower is the ONLY place in 3000+ pages where this is stated
- No proof beyond "follows from equivariance of the Feynman transform"

### SERIOUS: Z_g DEFINED by clutching, never COMPARED with external notion

### Missing: Segal-type modular functor from the categorical data

## Lurie: ∞-categorical framework is SOUND

### The manuscript handles strict/∞-categorical interface with more care than most
- Convention conv:vol2-strict-models is principled
- Strict/L∞ comparison for modular convolution algebra praised as "handled with the care I would require"
- All ∞-categorical claims invoked by citation to published sources (CG17, FG12, HA, AF15, BD04)

### Three moderate presentation gaps (not mathematical errors):
- "equivalence" in factorization axioms = quasi-equivalence, but not stated
- Cosheaf descent condition not explicitly stated for DgCat-valued cosheaves
- Model structures invoked but not written down for bar-cobar Quillen equivalence

## Feynman: ZERO first-principles verification at genus ≥ 1

### The programme's computational verification is almost entirely tautological above genus 0

**What EXISTS (genuine first-principles computation):**
- d²=0 at genus 0 from bar differential matrices built from structure constants + OS residue (sl_2, sl_3, low degrees)
- Bar cohomology dimensions from kernel/image (match Motzkin increments for Virasoro, partition numbers for Heisenberg)
- Shadow obstruction tower recursion from the Riccati equation (genuine algebraic computation)
- Complementarity kappa + kappa' cross-family consistency checks

**What is HARDCODED (takes the answer as input):**
- κ = c/2 for Virasoro — `genus1_curvature()` literally returns the input parameter
- F_1 = κ/24 — never derived from the genus-1 bar complex
- F_g = κ · λ_g — computed from Bernoulli formula, never from stable graph sum
- The "bar_d_squared_genus1" function checks κ == κ (tautological)

**What has NEVER been computed:**
- r(z) = Res^coll_{0,2}(Θ_A) for ANY specific algebra (the R-matrix identification)
- The derived center from bar complex data (the Verlinde module tests S-matrix, not bar complex)
- Θ_A constructed explicitly as D_A - d_0 (existence proved abstractly, never instantiated)
- F_2 from the stable graph sum (6 graph types at genus 2)

### Three computations that would give the programme teeth:
1. **Compute κ from d² on the torus**: Build the genus-1 bar differential using Weierstrass zeta propagator, compute d², extract coefficient of Arnold defect, verify = c/2 · E_2(τ)
2. **Compute R-matrix from Res^coll**: Construct Θ_A at genus 0 arity 2 from bar-intrinsic definition, take collision residue, verify = Ω/z for sl_2
3. **Compute F_2 from graph sum**: Enumerate 6 genus-2 stable graphs, compute amplitudes from shadow data, sum, verify = κ · 7/5760

### The honest assessment:
"The programme has teeth at genus 0. At genus ≥ 1, it has only formulas that verify formulas."
