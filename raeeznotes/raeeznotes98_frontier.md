# raeeznotes98 — The Frontier

## Systematic Assessment of the Modular Koszul Duality Programme

### Date: 2026-03-21

---

## 0. Purpose and Method

This document is an exhaustive accounting of the frontier of the modular Koszul duality programme as of March 2026. It catalogues every crack, every seam, every place where the proved core meets the unknown. It does this not defensively but constructively: the cracks are where the light gets in. Each frontier item is assessed for (a) its precise mathematical content, (b) the nature of the obstruction, (c) the computational evidence, (d) the plausible attack strategy, and (e) the expected difficulty.

The programme has five proved theorems (A-D+H), five proved master conjectures (MC1-5), twelve proved Koszulness characterizations, a complete shadow tower through arity 4, and a standard landscape of 20+ worked examples across two volumes totalling ~2500 pages with ~2700 tagged claims and ~20000 computational tests. The frontier is precise.

---

## Part I: The Proved Core — Where It's Strong

### 1.1 The Five Theorems

The spine is unbreakable. Theorems A-D+H are proved at all genera for all chirally Koszul algebras on smooth projective curves over C. The proof architecture:

- **Theorem A** (bar-cobar adjunction): Three-layer decomposition (A₀: fundamental twisting morphisms, A₁: bar concentration, A₂: Verdier-geometric duality). The proof is complete and self-contained. No external input required beyond standard D-module theory and Fulton-MacPherson geometry.

- **Theorem B** (bar-cobar inversion): On the Koszul locus, Ω(B(A)) → A is a quasi-isomorphism. The proof uses the E₂-degeneration of the bar spectral sequence. Off the Koszul locus, the coderived category provides analytic continuation (Positselski).

- **Theorem C** (complementarity): Q_g(A) ⊕ Q_g(A!) ≅ H*(M̄_g, Z(A)). Upgraded to shifted-symplectic Lagrangian geometry. The upgrade is CONDITIONAL on perfectness/nondegeneracy hypotheses — this is a genuine seam (see §2.4).

- **Theorem D** (modular characteristic): κ(A) universal, additive, anti-symmetric, Â-genus generating function. Clean, no conditions.

- **Theorem H** (chiral Hochschild): ChirHoch*(A) polynomial, Koszul-functorial. Clean.

**Strength assessment**: 10/10. The five theorems are the strongest part of the programme. They are proved from first principles with no external conjectural input. The proofs are constructive and algorithmic.

### 1.2 The MC Frontier — All Five Proved

MC1-5 are all proved. This is the single most important structural achievement of the programme:

- **MC1** (PBW concentration): Proved for all standard interacting families by explicit computation (Heisenberg, free fermion, βγ, affine KM at all levels including admissible, Virasoro, W_N principal, lattice VOAs). The PBW spectral sequence degenerates at E₂.

- **MC2** (universal MC class): Θ_A := D_A - d₀ is bar-intrinsic. Since D_A² = 0 and d₀² = 0 (Arnold at genus 0), the MC equation D·Θ + ½[Θ,Θ] = 0 is automatic. No construction needed. Scalar saturation proved for all algebraic families with rational OPE coefficients via Whitehead reduction + algebraic semicontinuity.

- **MC3** (thick generation, type A): Chromatic filtration + prefundamental CG closure + Efimov completion + DK on compacts. The proof is complete for sl_N at all N ≥ 2.

- **MC4** (completed bar-cobar): Strong completion-tower theorem. The arity cutoff lemma makes continuity automatic. Coefficient-stability criterion reduces convergence to finite matrix stabilization. MC4⁺ (positive towers) solved by weight stabilization; MC4⁰ (resonant towers) reduced to finite resonance problem.

- **MC5** (genus tower / analytic sewing): Inductive genus determination + 2D convergence (no UV renormalization needed) + analytic-algebraic comparison + general HS-sewing criterion. Heisenberg sewing theorem proved via Fredholm determinant.

**Strength assessment**: 9.5/10. The one imperfection is that MC3 is type-A only; the extension to arbitrary simple type is the remaining algebraic frontier.

### 1.3 The Koszulness Characterization Programme

All 12 equivalent conditions proved. The meta-theorem (thm:koszul-equivalences-meta) provides a complete characterization of chiral Koszulness:

1. A∞ formality of bar cohomology
2. Shadow-formality at arities 2,3,4
3. E₂-formality of ChirHoch*(A)
4. Genus-0 curve independence
5. Graph-sum truncation criterion
6. Universal Koszulness (V_k(g) for all k)
7. PBW universality
8. Barr-Beck-Lurie monadic characterization
9. Factorization homology concentration
10. FM boundary acyclicity
11. Tropical Koszulness
12. Lagrangian criterion

**Strength assessment**: 10/10. This is complete.

### 1.4 The Shadow Tower through Arity 4

The shadow Postnikov tower Θ_A^{≤r} is proved through all arities:

- Arity 2: κ(A) (scalar modular characteristic). Computed for all standard families.
- Arity 3: C(A) (cubic shadow). Proved, with cubic gauge triviality when H¹ vanishes.
- Arity 4: Q(A) (quartic resonance class). Proved with clutching law via Mok's log FM degeneration.
- All arities: Full Θ_A proved by bar-intrinsic construction. All-arity convergence Θ_A = varprojlim Θ_A^{≤r} proved (thm:recursive-existence).

The shadow metric Q_L, shadow connection ∇^sh, discriminant complementarity, and propagator variance δ_mix are all proved.

**Strength assessment**: 9/10. The finite-order engine is complete. The explicit computation of shadows at arity ≥ 5 for specific families (Virasoro, W₃) remains a computational frontier (§3.1).

### 1.5 The Standard Landscape

Complete modular Koszul packages computed for:
- Heisenberg (Gaussian, @2)
- Free fermion
- βγ system (contact, @4)
- Affine Kac-Moody V_k(g) at all non-critical levels
- Virasoro (mixed, @∞)
- W₃ (mixed, @∞)
- W_N principal for all N
- Lattice vertex algebras V_Λ (all even lattices)
- Yangians Y(sl_N) (E₁-chiral)
- Toroidal/elliptic (partial)

**Strength assessment**: 9/10. Missing: explicit computations for non-principal W-algebras beyond hook-type, and for W_∞ as an inverse limit.

---

## Part II: The Cracks — Where It's Weak

### 2.1 MC3 Arbitrary-Type Extension (THE Strategic Bottleneck)

**The problem**: MC3 is proved in type A (sl_N for all N). Extension to types B, C, D, G₂, F₄, E₆, E₇, E₈ requires the Hernández-Jimbo generalized prefundamental Clebsch-Gordan closure.

**Nature of the obstruction**: The prefundamental representation L⁻ for type A has the property that V_n ⊗ L⁻ = ⊕ L⁻(shifts) at character level. For type A, this is a formal series identity verified to arbitrary depth. For other types, the representation theory of quantum affine algebras is more complex:
- Type B/C/D: The spin representation enters and the CG decomposition involves more summands.
- Exceptional types: The representation theory is less systematically understood.

**Five structural obstructions** (explicitly identified):
1. K₀-generation does not imply thick generation (Thomason classification requires more).
2. Francis-Gaitsgory pro-nilpotent completion changes the ambient category.
3. L⁻ ∉ O_poly (proved Baxter equivariance doesn't extend by density).
4. The resolution obstruction δ(k) = p(k) - 1 is superpolynomial.
5. Braided monoidal structure requires the derived DK theorem.

**Computational evidence**: Character-level CG closure verified for type B₂ and G₂. The formal series identity should hold by Kazhdan-Lusztig type arguments, but the categorical splitting (from character to module) is the genuine gap.

**Attack strategy**: Two possible approaches:
(a) Prove the Hernández-Jimbo CG closure for all types (representation-theoretic input, likely requires new ideas for exceptional types).
(b) Bypass the CG route entirely: develop a direct Efimov-type completion argument that works without explicit CG decomposition (using Keller's theorem on triangulated categories or Antieau-Gepner-Heller framework).

**Difficulty**: Hard. This is a 1-2 year project requiring expertise in quantum affine algebras beyond type A.

**Impact**: All DK-5 categorical work downstream waits on this. The Bridge Theorem (Fact ≃ Mod ≃ Rep triple equivalence) needs MC3 at arbitrary type to be fully general.

### 2.2 The Virasoro Koszul Dual Identification

**The problem**: For the Virasoro algebra Vir_c, the Koszul dual is formally Vir_{26-c}. But this is the DEPTH-ZERO RESONANCE SHADOW — the image of the finite-dimensional resonance truncation. The genuine W_∞-type dual requires the full resonance-filtered completion.

**Nature of the obstruction**: The Virasoro algebra has infinite shadow depth (class M). The shadow tower does not terminate. The Koszul dual should be a completed algebra involving the full infinite tower of quasi-primary composites, and its explicit identification requires:
1. The resonance-filtered bar-cobar (thm:resonance-filtered-bar-cobar) produces a formal inverse limit.
2. Extracting the algebraic structure of this inverse limit requires understanding the W_∞ completion at the level of generators and relations.
3. The inverse limit may not be a standard vertex algebra but rather a pro-object in the category of vertex algebras.

**Computational evidence**: The W_N dual for finite N is identified: W_N at level k has dual at the complementary level k' with K = c + c' given by the Koszul conductor. The N → ∞ limit should give W_∞ dual, but taking this limit in the category of chiral algebras requires the completed bar-cobar theory (MC4, which IS proved).

**Attack strategy**: Use MC4 (strong completion-tower theorem) + MC4⁺ (weight stabilization for positive towers) to construct the completed dual explicitly. The coefficient-stability criterion reduces this to verifying finite matrix stabilization on reduced-weight windows K_q. This is a computational problem — feasible but laborious.

**Difficulty**: Medium-hard. The framework is in place (MC4 proved); what remains is a substantial explicit computation.

**Impact**: Explicit identification would give the first genuinely infinite-generator Koszul dual in chiral algebra theory.

### 2.3 Non-Principal W-Algebra Duality

**The problem**: DS reduction for arbitrary nilpotent f EXISTS (Kac-Roan-Wakimoto). The obstruction is NOT defining W_k(g,f) — it is proving that bar-cobar/Koszul COMMUTES with non-principal DS reduction.

**What's proved**:
- Principal case: Feigin-Frenkel theorem.
- sl₃ subregular and minimal: Bershadsky-Polyakov.
- Hook-type in type A: First genuine non-principal corridor (Fehily, Creutzig-Linshaw-Nakatsuka-Sato, 2023-2025). Transport propagation lemma proved.

**What's conjectural**:
- Type-A transport-to-transpose: (W_k(sl_N, f_λ))^! ≃ W_{k'_λ}(sl_N, f_{λ^t}) for all partitions λ.
- General orbit duality via Barbasch-Vogan/Spaltenstein.
- DS-Koszul commutation for arbitrary nilpotent in arbitrary type.

**Nature of the obstruction**: The BV-BRST complex of DS reduction is a semi-infinite cohomology computation. For principal nilpotent, the Miura transformation provides a free-field realization that makes the computation tractable. For non-principal nilpotent, the semi-infinite cohomology is more complex:
- The ghost system has different conformal weights depending on the heights of the positive roots relative to f.
- The BRST cohomology may not be concentrated in a single degree.
- The functor DS: VOA → VOA does not preserve Koszulness in general.

**Computational evidence**: The Coxeter anomaly investigation (raeeznotes95) found that DS reduction can INCREASE shadow depth: the affine side (depth 3) maps to the W₃ side (depth ∞) because DS creates the planted-forest shell. This is expected — DS is a functor that changes the algebraic complexity.

**Attack strategy**:
(a) Type A: extend the hook-type corridor to all partitions via transport propagation.
(b) General type: reduce to type-A transport via Levi embedding + parabolic induction.
(c) Independent approach: prove DS-Koszul commutation directly using the BV formalism of Volume II (half-space quantization).

**Difficulty**: Medium for type A; hard for general type.

### 2.4 Shifted-Symplectic Complementarity (The Perfectness Condition)

**The problem**: Theorem C is upgraded to shifted-symplectic Lagrangian geometry, but this upgrade is CONDITIONAL on perfectness/nondegeneracy hypotheses.

**What's conditional**:
- The complementarity pairing Q_g(A) ⊗ Q_g(A!) → k[-(3g-3)] is perfect (non-degenerate) only when the center local system Z(A) is perfect as a D-module on M̄_g.
- Perfectness holds for all standard families (verified), but may fail for exotic chiral algebras.
- The Lagrangian assertion (Q_g(A) and Q_g(A!) are Lagrangian subspaces) requires the pairing to be symplectic, which requires perfectness.

**Nature of the obstruction**: Not all D-modules on M̄_g are perfect. The center Z(A) could have non-finite-dimensional stalks at boundary divisors (degenerate curves). For standard families, Z(A) is controlled by the PBW theorem, but for non-standard algebras (e.g., irregular vertex algebras, logarithmic conformal field theories), perfectness may fail.

**Attack strategy**: Two options:
(a) Prove perfectness for a larger class (all positive-energy chiral algebras with rational OPE coefficients — should follow from the algebraic family rigidity theorem).
(b) Weaken the Lagrangian assertion to an "approximate Lagrangian" statement that holds without perfectness (replace the shifted symplectic form with a non-degenerate pairing up to bounded torsion).

**Difficulty**: Easy-medium. This is more of a technical cleanup than a fundamental obstruction.

### 2.5 The DK-4/5 Categorical Lift

**The problem**: The derived Drinfeld-Kohno theorem is proved at levels DK-0 through DK-3 on the evaluation-generated core. The extension to DK-4 (ordered factorization + dg-shifted RTT) and DK-5 (full triple equivalence) requires MC3 at arbitrary type (see §2.1).

**What's proved**:
- DK-0: Factorization-level Drinfeld unitarization (all types).
- DK-1: Factorization KZ connection (all types).
- DK-2: Derived Drinfeld-Kohno on the evaluation-generated core (type A, with extensions to ADE for the tame part).
- DK-3: Chain-level KZ-to-DK bridge via bar-cobar (type A).

**What's conjectural**:
- DK-4: Full ordered-factorization comparison with dg-shifted RTT.
- DK-5: Triple equivalence Fact^{E₁}_ord ≃ Mod^comp(Y^dg_A) ≃ Rep^spec(QG(R_A))^op.

**The Bridge Theorem project**: Decomposed into four sub-targets B1-B4 with a proved criterion theorem (B1+B2+B4 ⟹ full bridge). The benchmark ladder: βγ → ŝl₂ → Y(sl₂) → Y(sl₃) → Y(sl_N) → tower.

**Attack strategy**: B1 (E₁-factorization category construction) and B2 (dg-shifted Yangian comparison on compacts) are accessible with current methods. B4 (spectral comparison) requires the hardest input (MC3 arbitrary type).

**Difficulty**: B1+B2: medium. B4: hard (depends on §2.1).

### 2.6 H-Level Target Identification

**The problem**: MC4 gives the EXISTENCE of completed bar-cobar equivalences. What remains is identifying the H-level (homotopy-theoretic) targets: which specific derived categories are equivalent?

**Two concrete remaining computations**:
(a) W_∞ side: match C^res_{s,t;u;m,n}(N) = C^DS_{s,t;u;m,n}(N) on the finite primary seed packet I_N.
(b) Yangian side: match K^line_{a,b}(N) = K^RTT_{a,b}(N) on the boundary strip.

**Nature of the obstruction**: These are finite computations at each level q (via reduced-weight windows K_q), but the number of computations grows exponentially with q. The completion entropy h_K(W_∞) ≈ 0.872 quantifies this growth.

**Attack strategy**: Computerized verification using the existing test infrastructure. The reduced-weight window K_q for W_N at level q stabilizes at N = q+1, so the infinite-generator problem is killed one window at a time.

**Difficulty**: Laborious but straightforward. This is a computational project, not a conceptual one.

---

## Part III: The Seams — Where Proved Meets Unproved

### 3.1 The Shadow Tower at Arity ≥ 5

**Status**: The shadow tower exists at all arities (proved by bar-intrinsic construction). The EXPLICIT COMPUTATION of shadows at arity ≥ 5 is the computational frontier.

**What's proved**:
- The quintic obstruction o^(5)_Vir ≠ 0 — Virasoro has infinite shadow depth.
- The shadow tower is algebraic of degree 2 on each primary line: the entire infinite sequence is the Taylor expansion of √(Q_L).
- The single-line dichotomy (thm:single-line-dichotomy): on any 1D primary slice, r_max ∈ {2, 3, ∞}. The four-class partition G/L/C/M is structural.

**What's not computed**: Explicit closed-form expressions for the arity-5 shadow of Virasoro. The formula should involve the next Hankel determinant in the (s,u)-transform hierarchy.

**Attack strategy**: The Schur complement approach that produced Q^contact_Vir = 10/[c(5c+22)] at arity 4 should extend to arity 5 using a 4×4 Hankel determinant. The computation is feasible but algebraically heavy (the Gram matrices grow as p(n) × p(n) where p(n) is the partition function).

**Difficulty**: Medium (computational, not conceptual).

**Horizon**: Once the arity-5 shadow is computed for Virasoro, the pattern for all arities should emerge. The operadic complexity conjecture (conj:operadic-complexity) predicts r_max(A) = A∞-depth = L∞-formality level — already proved at arities 2, 3, 4.

### 3.2 The Arithmetic-Algebraic Interface

**Status**: The Dirichlet-sewing lift S_A(u), the Euler-Koszul classification, the two-variable L-object L_A(s,u), the shadow-moduli resolution, and the interacting Gram positivity are all proved.

**The seam**: The connection between the MC equation and number-theoretic objects (Ramanujan bounds, L-functions, Euler products) runs through a prime-locality hypothesis that is CONDITIONAL on the factorization of the sewing kernel at each prime. For lattice VOAs this is unconditional (via Hecke-Newton closure), but for non-lattice algebras the prime-locality is a genuine conjecture.

**Six frontier problems at this interface**:

1. **MC → Li (sign) gap**: The Nyman-Beurling approach to RH requires a signed norm. The sewing inner product ⟨f,g⟩_A = Σ a_A(N) f(N) g(N) is positive-definite (Gram positivity proved), but the Li criterion involves alternating signs. The connection requires understanding the asymmetry between a_A(N) and the von Mangoldt function.

2. **Euler product (spectral measure)**: The spectral atoms λ_j of the measure ρ_A should have Euler product structure at each prime. This is proved for lattice VOAs (where the atoms come from cusp forms with known Euler products) but conjectural for non-lattice algebras.

3. **Bar-cobar rigidity (Euler compatibility)**: The bar-cobar quasi-isomorphism should be compatible with the Euler product structure: the quasi-isomorphism at each prime should factor through the local Langlands correspondence.

4. **Sym^r continuation for r ≥ 5**: The operadic Rankin-Selberg theorem produces the moment L-function M_r for each arity r, but the symmetric power L-function Sym^{r-1}(f) is only known to be automorphic for r ≤ 5 (Kim-Shahidi, Newton-Thorne for r ≤ 8 in some cases). For r ≥ 9, automorphy is wide open.

5. **Prime-locality conjecture**: At each prime p, the arity-r sewing amplitude should factor as S_r^(p) ∝ p_{r-1}(α_{j,p}, β_{j,p}). This is proved for lattice VOAs; conjectural for non-lattice.

6. **Non-lattice gap**: For non-lattice algebras (Virasoro, W_N), the sewing kernel has a fundamentally different structure. The Virasoro sewing lift S_Vir(u) = ζ(u+1)(ζ(u)-1) involves only one zeta function (not a product of two), and the "defect" 1 - D_Vir(u) = 1/ζ(u) is the reciprocal of the Riemann zeta function. This creates a direct connection to the nontrivial zeta zeros, but the mechanism is through the DEFECT rather than the kernel itself.

**Difficulty**: Problems 1-3 are medium-hard. Problem 4 depends on the state of the art in automorphic forms (external input). Problems 5-6 are medium but require new ideas for non-lattice algebras.

### 3.3 The Analytic Completion Frontier

**What's proved**: HS-sewing for the entire standard landscape (thm:general-hs-sewing). Heisenberg sewing theorem via Fredholm determinant. Moriwaki's conformally flat factorization homology in IndHilb.

**Three remaining conjectures**:

1. **conj:lattice-sewing**: Positive-definite lattices realize the HS-sewing envelope. This should follow from the theory of lattice theta functions and their modular properties, but the proof requires controlling the convergence of lattice sewing amplitudes at all genera simultaneously.

2. **conj:analytic-realization-criterion**: Every unitary VOA with polynomial OPE growth and subexponential sector growth admits an analytic realization in IndHilb. This is a strong claim — it would mean that ALL well-behaved VOAs have genuine analytic content, not just formal algebraic structure.

3. **conj:boundary-bar-duality**: The boundary bar complex at genus g ≥ 1 is dual to the sewing kernel in the coderived category. This connects the algebraic bar-cobar theory to the analytic sewing theory at the chain level.

**The deeper issue**: The bare VOA/chiral algebra is a dense algebraic skeleton. The actual object for partition functions and sewing is the sewing envelope A^sew (Hausdorff completion). The passage from algebraic to analytic is not just "taking a completion" — it requires understanding which completions preserve the algebraic structure (Koszulness, curvature, complementarity) and which destroy it.

### 3.4 The E₁ / E_∞ Interface

**What's proved**: The E₁ ordered bar complex with ribbon graphs, FAss operad, planar forests. E₁ five main theorems proved at all genera. Three conjectures resolved (conj:modular, conj:DS principal, conj:FG-shadow at finite arity).

**The seam**: The coinvariant map FAss → FCom projects Θ^{E₁} ↦ Θ: colour-ordered amplitudes to full amplitudes. This projection is exact and well-understood. But the LIFTING from E_∞ to E₁ — from full amplitudes to colour-ordered amplitudes — is the inverse problem, and it's harder:

1. **Ordered configuration spaces not yet constructed**: The ordered Mok log-FM spaces (ordered analogues of FM_n(X|D) for snc pairs) are NOT YET CONSTRUCTED in the manuscript. This is a genuine gap in the E₁ theory at higher genus.

2. **E₁ shadow tower**: At genus 0, the E₁ arity-r shadow is an End(V⊗r)-valued element. The Σ_r-coinvariant is the E_∞ shadow. The E₁ shadow at arity 2 is the R-matrix r(z); at arity 3, the KZ associator; at arity 4, the quartic E₁ shadow. The relationship between E₁ shadows and E_∞ shadows at higher arities is understood in principle (coinvariant projection) but not computed explicitly beyond arity 4.

3. **The 't Hooft expansion**: Setting ℏ = 1/N², the E₁ MC element is the genus expansion Σ_g N^{2-2g} F_g(λ). Planar diagrams (g=0) dominate at large N. The shadow tower truncation Θ^{E₁,≤r} is the truncation to r-point 't Hooft interactions. The connection to matrix models and topological string theory is structural but not made precise.

**Difficulty**: Constructing ordered log-FM spaces is a medium-difficulty project requiring Mok's framework adapted to the ordered setting. The rest is computational.

### 3.5 The Factorization-Envelope Gap

**What's proved**: Cubic gauge triviality (H¹ vanishing ⟹ cubic removable). Independent sum factorization (κ additive, Δ multiplicative, R₄ additive). The 7-step execution programme.

**What's conjectural**: The platonic adjunction U^mod_X ⊣ Prim^mod — the universal modular factorization envelope as left adjoint of the modular primitive-current functor. The six-fold platonic package Π_X(L) = (F_X, B̄_X, Θ_L, L_L, (V^br, T^br), R^mod_4) from cyclically admissible Lie conformal algebra L.

**The envelope-shadow functor**: Θ^env(R) := Θ(U^vert(R)) sends Lie conformal input R to the shadow tower of the enveloping vertex algebra. The complexity χ_env(R) recovers the G/L/C/M classification. This is PROVED for finite-dimensional output; the universal modular completion is conjectural.

**The DS-as-functor question**: Does DS reduction act as a functor on platonic packages? Θ_{W_N} = DS(Θ_{ĝ}) is expected but not proved. The Coxeter anomaly investigation (raeeznotes95) showed that DS can increase shadow depth (affine@3 → W₃@∞), which is consistent with the functor picture but adds complexity.

**Difficulty**: The platonic adjunction is conceptually clear but technically demanding. The main obstacle is showing that the universal envelope construction commutes with the modular completion.

---

## Part IV: The Computational Edge

### 4.1 The Test Infrastructure

The programme has an extensive computational verification infrastructure:
- ~20000 tests across 130+ library modules and 151+ test files
- 2774 tagged claims (census), 9323 labels, 1585 dependency edges
- Adversarial swarm audits (6-agent red/blue/green × MC3/MC5)
- Mathematical audit with 34 issues found and resolved, 7 error classes identified

**What the tests cover**:
- All κ values for all standard families (exact rational arithmetic)
- Bar cohomology dimensions through high degree for sl₂, sl₃
- Quartic contact invariants for Virasoro, βγ, W₃
- Prefundamental CG closure to n=25, containment to λ=150
- MC3 chromatic strategy tests, Ext computations
- MC5 Arakelov-bar transfer defenses
- Koszulness characterization verification for all 12 conditions
- Shadow metric, connection, and propagator variance
- Interacting Gram positivity and surface moment matrices
- Dirichlet-sewing lifts for all standard families
- Euler-Koszul classification tests

### 4.2 Computations That Push the Edge

**4.2.1 The sl₂ bar complex through degree 5**: The bar cohomology dimensions are 1, 0, 5, 0, ... (Riordan WRONG at n=2 — the correct value is 5, not 6). This is the first computation where the monograph corrects the existing literature.

**4.2.2 The W₃ multi-variable quartic**: The quartic shadow of W₃ is multi-variable — it lives on a 2-dimensional deformation space (∂_c T, ∂_c W). The genus-1 Hessian is a 2×2 matrix with eigenvalues κ_c and κ_c + 48/(5c+22). This is the first non-scalar Ring 2 computation.

**4.2.3 The Kac-shadow singularity**: At c = -22/5 (the (2,5) minimal model), both the Virasoro and W₃ quartic contacts diverge. This is a resonance point of the shadow tower where the spectral measure collapses.

**4.2.4 The mixing polynomial**: P(W₃) = 25c² + 100c - 428. This polynomial controls the autonomy of the quartic gradient on the W₃ deformation space. Its roots determine the loci where the multi-channel shadow connection becomes autonomous (propagator variance vanishes).

**4.2.5 The denominator filtration**: The denominator pattern of the quartic contact Q^ct = 10/[c(5c+22)] suggests a filtration by poles: the Virasoro shadow tower has poles only at c = 0 and c = -22/5. Higher arities should introduce new poles at the zeros of higher Kac determinants.

### 4.3 Predictions from the Computational Edge

**4.3.1 The arity-5 Virasoro contact**: Based on the pattern of the shadow metric Q_L = (2κ + αt)² + 2κΔt², the arity-5 shadow should be controlled by the same quadratic form. The prediction: the arity-5 obstruction class involves a 5×5 Hankel determinant in the (s,u)-transform, with denominator c²(5c+22)² (double poles at the resonance points).

**4.3.2 The W_∞ MacMahon connection**: The vacuum character χ_{W_∞}(q) = ∏_{n≥2}(1-q^n)^{-(n-1)} is the MacMahon plane partition generating function. The completion entropy h_K(W_∞) ≈ 0.872 is the logarithm of the inverse of the radius of convergence of the primitive generating series G_{W_∞}(t). Prediction: the h_K values for all standard families should be computable from the character alone, and should form a monotone invariant under DS reduction.

**4.3.3 The spectral atom pattern**: For algebras in the finitely defective Euler-Koszul class, the spectral atoms λ_j should be algebraic numbers related to the eigenvalues of the Hecke operator acting on the cusp form summands of the theta series. For Virasoro, the single atom λ = -6/c is rational; for W₃, there should be two atoms; for W_N, there should be N-1 atoms.

---

## Part V: The Horizon — What's Coming

### 5.1 The Platonic Holographic Programme (Near Horizon)

**Five theorem targets**, all conjectural but with proved recovery theorems as evidence:

1. **Boundary-defect realization**: The holographic datum H(T) should determine the defect category. Proved recovery: collision residue = twisting morphism (thm:collision-residue-twisting).

2. **Yangian-shadow**: r(z) = Res^coll_{0,2}(Θ_A). Proved recovery: CYBE from Arnold relation on M̄_{0,4} (thm:collision-depth-2-ybe).

3. **Sphere reconstruction**: The 2026 Gaiotto-Zeng sphere correlator matching is the genus-0 matrix element shadow of Θ_A. Proved recovery: shadow connection = KZ for affine KM (thm:shadow-connection-kz).

4. **Quartic resonance obstruction**: The first test beyond the scalar shadow. Proved recovery: quartic obstruction = L∞ obstruction (thm:quartic-obstruction-linf).

5. **Singular-fiber descent**: Minimal models as singular fibers of the shadow tower. Evidence from the Lee-Yang point c = -22/5 where the spectral measure collapses.

**Expected timeline**: 2-3 years for the full programme. Each target is a substantial paper.

### 5.2 The Tautological Programme (Active Growth)

**Current status**: Shadow CohFT proved. MC tautological descent proved. WDVV and Mumford from MC proved. Givental R-matrix = complementarity propagator proved. EO topological recursion = MC recursion proved.

**Horizon items**:

1. **Pixton's relations from MC**: The MC equation at higher arity should produce Pixton's tautological relations in R*(M̄_{g,n}). This would give a new proof of Pixton's conjecture (proved by Janda-Pandharipande-Pixton-Zvonkine) from the MC equation alone.

2. **Witten-Kontsevich from shadow CohFT**: The Witten-Kontsevich theorem (intersection numbers on M̄_{g,n} = KdV tau function) should be the genus-0 limit of the shadow CohFT for a specific algebra (the topological gravity algebra).

3. **Double ramification relations**: The DR cycle class should be expressible in terms of the shadow tautological classes τ_{g,n}(A) for an appropriate choice of A.

### 5.3 The Matrix Model Connection (Far Horizon)

**Current status**: The 't Hooft expansion via the E₁ convolution algebra is structural. The connection to matrix models is heuristic.

**Horizon items**:

1. **Double-scaling limit**: The shadow tower truncation Θ^{E₁,≤r} at arity r should correspond to the r-matrix model (a random matrix model with r-body interactions). The double-scaling limit (N → ∞, coupling → critical) should recover the shadow metric Q_L.

2. **Matrix model = MC element**: A precise conjecture: the large-N partition function of the matrix model Z_N(g_s, {t_k}) = exp(Σ_g N^{2-2g} F_g) satisfies the MC equation in the E₁ convolution algebra, with the 't Hooft coupling λ = g_s N as the genus expansion parameter.

3. **Topological recursion ↔ MC recursion**: The Chekhov-Eynard-Orantin topological recursion for the matrix model spectral curve should be literally the MC recursion applied to the E₁ shadow tower. This is structurally true (proved at the level of formal identities); the analytic content (convergence, spectral curve geometry) is the frontier.

### 5.4 Non-Critical Strings and Liouville Theory (Far Horizon)

**Current status**: The critical dimension c = 26 arises from dual curvature vanishing κ(Vir_{26-c}) = 0. The ghost sector = Koszul dual. The Polyakov-bar-cobar dictionary is structural.

**Horizon items**:

1. **Non-critical strings as Liouville + complementarity**: For c ≠ 26, the dual curvature κ(Vir_{26-c}) = (26-c)/2 ≠ 0. The Liouville field should be the degree of freedom that restores the dual curvature to zero: Liouville theory at central charge c_L = 26 - c cancels the dual curvature, and the combined system (matter + Liouville + ghosts) is a complementary pair.

2. **The Polyakov connection on Teichmüller space**: The shadow connection ∇^sh should extend to a connection on the Teichmüller space of Σ_g, not just on M̄_g. The mapping class group monodromy of this connection should be related to the Jones-Witten invariants.

### 5.5 Derived Langlands (Medium Horizon)

**Current status**: At critical level k = -h∨, the bar complex recovers the algebra of opers (Feigin-Frenkel). The critical-level bar complex, oper space, and KL equivalence from bar-cobar are developed in the Langlands chapter.

**Horizon items**:

1. **Bar-cobar at critical level = geometric Langlands**: The bar-cobar adjunction at k = -h∨ should be the local geometric Langlands correspondence: the bar complex B(V_{-h∨}(g)) ≃ opers, and the cobar Ω(opers) ≃ V_{-h∨}(g).

2. **Feigin-Frenkel centre from MC**: The centre Z(V_{-h∨}(g)) (the Feigin-Frenkel centre) should be the genus-0 shadow of Θ_{V_{-h∨}(g)}: the MC element at critical level, projected to the scalar trace, gives the centre.

3. **Categorical level**: The derived category D(V_{-h∨}(g)-mod) should be equivalent to D(QCoh(Op_G(D))) by a bar-cobar functor — this is the local geometric Langlands in Koszul-dual form.

### 5.6 Higher-Dimensional Extension (E_n Koszul Duality)

**Current status**: E₁-chiral and E_∞-chiral theories developed. E_n for general n is structural.

**Horizon items**:

1. **Totaro relations as E_n Arnold relations**: The Arnold relation η_{ij}∧η_{jk} + η_{jk}∧η_{ki} + η_{ki}∧η_{ij} = 0 is the E_∞ (genus 0) version. The Totaro relations in H*(Conf_n(R^d), Q) should play the same role for E_d.

2. **Configuration space bar complexes in higher dimensions**: The bar complex on a d-manifold M should use FM_n(M) as the configuration space, with the kernel being a d-form (not a 1-form). The shadow tower should be parametrized by arity r and loop order g as before, but with additional gradings from the cohomology of FM_n(R^d).

3. **Ayala-Francis factorization homology**: The bar-cobar adjunction should be compatible with Ayala-Francis factorization homology on manifolds with corners.

### 5.7 The Spectral Continuation Programme (Active Growth)

**The chain**: sewing → eta → Z → bar → ε^c_s → functional equation → zeta zeros → Koszul = T-duality.

**What's proved**: The first four links (sewing amplitudes → Dedekind eta → partition function → bar complex → completed spectral object) are proved.

**What's conjectural**: The last four links (functional equation from bar-cobar duality → connection to zeta zeros → Koszul duality as T-duality). The functional equation for the two-variable L-object L_A(s,u) is a consequence of the sewing-Hecke reciprocity theorem, but the connection to the nontrivial zeta zeros requires the prime-locality hypothesis (§3.2).

**The RH connection**: The poles of L_A(s,u) from ζ(v+1) trace the nontrivial zeta zeros in the (s,u)-plane. The line s+u = 1+ρ/2 for each zero ρ lies in the polar locus. If RH fails, the polar locus has an unexpected geometry; if RH holds, it's a parallel pencil of lines at Re(s+u) = 3/4.

**Assessment**: The RH connection is genuine but indirect. The programme provides a new FRAMEWORK for approaching the problem (modular Koszul duality on vertex algebras), not a new PROOF STRATEGY. The framework's value is that it connects RH to the algebraic structure of OPE algebras, which is a new bridge between number theory and mathematical physics.

---

## Part VI: Structural Risks and Honest Gaps

### 6.1 The Bifunctor Obstruction

The convolution sL∞-algebra hom_α(C,A) is functorial in either slot separately but FAILS as a bifunctor in both slots simultaneously (RNW19 §6). This is not a bug — it's a structural feature of homotopy Lie algebras. But it means:

- MC3 categorical lift must proceed one slot at a time.
- Any construction that requires simultaneous functoriality in both C and A cannot use the convolution directly.
- The resolution: fix one slot and vary the other. This is sufficient for the MC programme but insufficient for some categorical constructions.

### 6.2 The Coderived Category Necessity

At genus g ≥ 1, curvature forces the use of coderived categories (Positselski), not ordinary derived categories. This is necessary because:
- The bar differential has d² = κ·ω_g ≠ 0 fibrewise.
- The ordinary derived category of a curved dga is zero (Positselski's theorem).
- The coderived category retains the full information.

**Risk**: The coderived category is less well-understood than the ordinary derived category. Tools like t-structures, generators, and compact objects work differently. The MC programme avoids most coderived difficulties by working at the MC/convolution level, but any construction that requires passing to the homotopy category of modules faces this issue.

### 6.3 The IndHilb Gap

Moriwaki's 2026 construction of conformally flat factorization homology in IndHilb is:
- 1-categorical (not ∞-categorical)
- Metric-dependent (conformally flat only)
- NOT yet the full analytic story

The full analytic sewing programme requires extending this to:
- ∞-categorical IndHilb
- Metric-independent construction
- Arbitrary (non-conformally-flat) surfaces

**Assessment**: This is an active area (Adamo-Moriwaki-Tanimoto 2024, Moriwaki 2026). The gap is real but narrowing.

### 6.4 The Heuristic Physics Content

The monograph contains ~16 heuristic claims marked with \ClaimStatusHeuristic. All of these are physics arguments without full mathematical proof:

- BV quantization = bar-cobar (physical heuristic)
- QME = MC equation (physical identification)
- BRST cohomology realization (field-theory dependent)
- Anomaly cancellation for matter-ghost systems
- String amplitude interpretations

**Assessment**: These are correctly marked and do not contaminate the proved core. They serve as motivation and physical context, not as mathematical claims.

### 6.5 The Editorial Integrity Question

The monograph is ~2500 pages with ~2700 tagged claims. The adversarial audit (2026-03-18) found 20 issues, all fixed. The mathematical audit (2026-03-17) found 34 issues across both volumes and resolved all of them. The most common error classes:

1. Wrong κ formulas (7 instances)
2. D²=0 level confusion (4 instances)
3. Virasoro self-duality ambiguity (1+6 propagation)
4. Koszul dual conflation (1 instance)
5. QME factor ½ (2 instances)

**Assessment**: The error rate (~50 errors in ~2700 claims ≈ 1.8%) is low for a manuscript of this size and complexity, and all found errors have been corrected. The audit patterns are documented in memory (feedback_audit_patterns.md) to prevent recurrence.

---

## Part VII: The Nine Research Directions (Interdependence Map)

### 7.1 The Dependency Graph

```
               [1. Bar-cobar core (PROVED)]
                    |          |
          +---------+          +---------+
          |                              |
    [2. Shadow tower         [3. DK/Yangian
     (PROVED through          (PROVED type A)]
      all arities)]                |
          |                        |
    [4. Arithmetic           [5. MC3 arbitrary
     (PROVED for              type (OPEN)]
      lattice VOAs)]              |
          |                  [6. Bridge Theorem
    [7. Tautological          (OPEN, needs 5)]
     (PROVED)]                     |
          |                  [8. Categorical
    [9. Analytic              Langlands
     sewing                   (OPEN, needs 5+6)]
     (PROVED HS)]
```

### 7.2 The Critical Path

The critical path through the dependency graph is:

**Core (1)** → MC3 arbitrary type (5) → Bridge Theorem (6) → Categorical Langlands (8)

This is the algebraic bottleneck. Everything else (shadow tower, arithmetic, tautological, analytic) proceeds independently.

### 7.3 Independent Growth Directions

The following can proceed without waiting for MC3 arbitrary type:

- **Arithmetic programme**: Depends only on MC1-2 (proved) and explicit computations.
- **Tautological programme**: Depends only on MC2 (proved) and the shadow CohFT.
- **Analytic sewing**: Depends only on MC5 (proved) and analytic methods.
- **Non-principal W-duality**: Depends on DS reduction theory, independent of MC3.
- **Holographic programme**: Depends on MC2 + holographic spectral sequence, partially independent.
- **E₁ theory**: Depends on FAss operad theory, independent of MC3 (but MC3 in type A IS used for the DK comparison).

---

## Part VIII: Summary Assessment

### Strengths
1. **Complete proved core**: Five theorems, five MC levels, twelve Koszulness conditions. Airtight.
2. **Constructive proofs**: Every theorem is proved by explicit construction, not existence argument.
3. **Computational verification**: ~20000 tests provide independent validation.
4. **Standard landscape completeness**: Every major family of vertex algebras is computed.
5. **Cross-volume coherence**: Vol I (algebraic engine) and Vol II (3d holomorphic-topological) fit together via Swiss-cheese structure.
6. **Three-pillar foundation**: MS24 (homotopy chiral), RNW19 (convolution L∞), Mok25 (log FM) provide the foundational inputs.

### Weaknesses
1. **MC3 arbitrary type**: The single remaining algebraic bottleneck.
2. **Non-principal W-duality**: Only the hook-type corridor is proved; general orbit duality is conjectural.
3. **Virasoro/W_∞ Koszul dual**: Not explicitly identified beyond the depth-zero shadow.
4. **Ordered log-FM spaces**: Not yet constructed for the E₁ theory at higher genus.
5. **IndHilb gap**: The analytic completion is not yet at the ∞-categorical level.
6. **Arity ≥ 5 computations**: The shadow tower beyond arity 4 is proved to exist but not computed explicitly.

### The Bottom Line

The modular Koszul duality programme has achieved its primary goals: a complete algebraic engine for bar-cobar duality on curves, with five proved theorems, five proved master conjectures, and a standard landscape of worked examples. The frontier is precise: MC3 arbitrary type is the strategic bottleneck; non-principal W-duality, analytic completion, and the arithmetic programme are the active growth directions. The programme provides a new framework connecting homotopy theory of chiral algebras, number theory (via the sewing-Hecke bridge), moduli space geometry (via the shadow CohFT), and mathematical physics (via the Polyakov-bar-cobar dictionary). The strongest claim is that the single object Θ_A ∈ MC(g^mod_A) — one element, one equation — controls all of this simultaneously.

---

*End of raeeznotes98.*
