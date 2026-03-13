# MASTER PROPAGATION TASK LIST v44
# Source: raeeznotes29-36 deep synthesis (2026-03-14)
# Goal: Propagate all mathematical depth from notes into manuscript with Chriss-Ginzburg delivery

---

## AXIS 0: ARCHITECTURAL FRONT MATTER (from r32/r35)

### A0.1 — Insert formal Definition of Modular Homotopy Theory in introduction.tex
**Target**: chapters/theory/introduction.tex, after §1.4 (the four main theorems section, ~line 490)
**Content**: Insert Definition 1.X "Modular Homotopy Theory on a Smooth Curve" with:
- (i) ∞-categorical bar-cobar adjunction on D^co(Fact(X))
- (ii) Functoriality over {M̄_{g,n}} intertwined with Verdier duality
- (iii) Universal MC class Θ_A ∈ MC(Def_cyc(A) ⊗̂ RΓ(M̄_{g,•}, Q))
- (iv) Shifted-symplectic pairing with complementary Lagrangians Q_g(A), Q_g(A!)
**Cross-ref**: Forward to def:modular-koszul-homotopy in higher_genus.tex
**Verification**: Definition appears before page 30 of compiled PDF

### A0.2 — Insert "Guide to the Reader" section in introduction.tex
**Target**: chapters/theory/introduction.tex, new §1.1 or §1.2
**Content**:
- Dependency map: which chapters depend on which
- Three entry points: (a) Heisenberg frame for fastest route to main theorems, (b) Full Part 1 for complete theory, (c) Yangian chapter for braided/E1 face
- H/M/S level convention as a formal Definition (def:hms-levels)
- Table: Part 1 = Theory (foundational, read linearly), Part 2 = Examples (modular, read selectively), Part 3 = Connections (perspective, read for context)

### A0.3 — Remove project-control scaffolding from printed text
**Targets** (global grep required):
- Remove or remark-ify all "constitutional status", "control ledger", "Stratum I/II" language from chapters that are NOT concordance.tex
- Specifically: any "MC hierarchy" governance language in example chapters should be replaced with clean mathematical forward-references
- The concordance chapter (Ch 34) is the ONE place where programme/status language is appropriate
**Verification**: grep for "constitutional", "control ledger", "stratum" outside concordance.tex returns 0 hits

### A0.4 — Fix "five geometric seeds" count
**Target**: chapters/theory/introduction.tex, remark:four-pieces (~line 530)
**Content**: The remark lists FIVE ingredients but says "four pieces". Fix to say "five irreducible geometric ingredients" with explicit numbering:
1. Arnold relation (three-point collision coherence)
2. Verdier duality on Ran(X)
3. Genus-1 curvature (fiberwise d² = κ·ω_g)
4. Clutching of stable curves (modular operad)
5. Associative/E₁ structure (R-matrix, ordered configurations)
**Verification**: Printed text says "five" not "four"

---

## AXIS 1: MODULAR HOMOTOPY THEORY — Definition and Propagation (from r30/31)

### A1.1 — Three-level definition ladder in bar_cobar_construction.tex
**Target**: chapters/theory/bar_cobar_construction.tex, new subsection after bar-cobar adjunction
**Content**: Three definitions in sequence:
- **Definition (tree-level operadic homotopy theory)**: ∞-category H with homotopy-coherent P-action, operations indexed by rooted trees
- **Definition (modular homotopy theory, abstract)**: ∞-category H with homotopy-coherent M-action, operations indexed by stable graphs, compatible with separating/nonseparating gluing
- **Remark**: The formal generalization is: replace trees with stable graphs. This is "obvious" at the level of definition, not at the level of existence.
**Cross-ref**: Forward to def:modular-koszul-homotopy

### A1.2 — Modular bar construction as Feynman transform
**Target**: chapters/theory/bar_cobar_construction.tex AND chapters/theory/higher_genus.tex
**Content**: Make explicit that:
- B^mod(A)(g,n) = ⊕_{Γ ∈ G^st_{g,n}} (⊗_{v ∈ V(Γ)} A(g_v, val(v))) ⊗ or(E(Γ))
- Sum over stable graphs with Σ_v g_v + b_1(Γ) = g
- This IS the Feynman transform FT_M(A)
- Vertices carry local operations, internal edges are propagators, loops encode genus
**Locations**: Wherever the genus-g bar complex is currently defined, add this graph-sum description

### A1.3 — Three-part differential: d_mod = d_int + d_sep + d_nonsep
**Target**: chapters/theory/higher_genus.tex, near definition of higher-genus differential
**Content**: Make explicit the three geometric pieces:
- d_int = internal differential of coefficient object
- d_sep = contractions of separating edges (ordinary gluing of two components)
- d_nonsep = contractions of loops/self-gluings (genus-raising operations)
- d² = 0 follows from boundary-of-boundary = 0 in modular operad axioms
**Verification**: These three terms are named and labeled in the compiled text

### A1.4 — Genus filtration as fundamental parameter
**Target**: chapters/theory/higher_genus.tex
**Content**: Make explicit:
- F_{≤G} B^mod(A) := ⊕_{g≤G} B^mod_{(g)}(A)
- g=0: tree level (ordinary operadic bar)
- g=1: one-loop (curvature, central extension, Sugawara)
- g≥2: higher loops (Mirzakhani volumes, intersection theory)
- "Modular homotopy theory is not a metaphor: it is the homotopy theory whose fundamental filtration parameter is genus"

### A1.5 — Deformation complex as modular convolution dg Lie algebra
**Target**: chapters/theory/deformation_theory.tex, and forward-ref from higher_genus.tex
**Content**: Insert or strengthen:
- Def^mod(A) := ∏_{g,n} Hom_{Σ_n}(C_*(M̄_{g,n}), End_A(g,n)) with bracket from graph gluing
- MC element Θ ∈ MC(Def^mod(A)) IS equivalent to modular structure on the underlying graded object
- This is the direct higher-genus upgrade of "homotopy algebraic structures = MC elements in convolution dg Lie algebra"
- The new feature: coefficients are chains on M̄_{g,n}, so stable-graph geometry enters the governing dg Lie algebra itself

### A1.6 — Quantum L∞ vs cyclic L∞ distinction
**Target**: chapters/theory/deformation_theory.tex, new remark after cyclic L∞ definition
**Content**: Insert remark:quantum-vs-cyclic-linf:
- Tree level = cyclic L∞ algebra
- All genus = quantum L∞ algebra (Braun-Maunder: loop homotopy algebra)
- m(ℏ) = m_0 + ℏm_1 + ⋯ solving quantum master equation
- Lifting cyclic L∞ to quantum/modular is OBSTRUCTED: first obstruction is Δ(m_0), lift exists iff unimodular
- Our Koszul chiral algebras DO give full modular homotopy types — this is SPECIAL
- Globalized on curves/factorization algebras = full modular homotopy type (richer than bare quantum L∞)
**Slogan**: "tree level = cyclic L∞; all genus = quantum L∞; globalized on curves = modular homotopy type"

### A1.7 — Surface observables via factorization homology
**Target**: chapters/theory/poincare_duality.tex or poincare_duality_quantum.tex
**Content**: Add remark connecting to Ayala-Francis:
- H_{Σ_g}(A) := ∫_{Σ_g} A (factorization homology over genus-g surface)
- Poincaré/Koszul duality: factorization homology with A ↔ factorization cohomology with A!
- This is the topological shadow of the modular bar-cobar story
**Cross-ref**: Ayala-Francis in bibliography

---

## AXIS 2: TWO-ATOM ARCHITECTURE (from r29/r33)

### A2.1 — Strengthen "two atoms" language in introduction.tex
**Target**: chapters/theory/introduction.tex, §1.4 or wherever atoms are introduced
**Content**: Make crystal clear:
- **Heisenberg = E∞ atom**: symmetric configurations, commutative chiral, genus/curvature/complementarity/scalar invariants
- **Yangian = E₁ atom**: ordered configurations, associative/braided chiral, ordering/braiding reversal/evaluation locus/RTT/DK ladder
- These are not "two examples among many" — they are the two irreducible entry points of the entire subject
- All other families (KM, Virasoro, W-algebras, lattice VOAs) are intermediate between these poles

### A2.2 — Propagate atom language to Part 2 introduction
**Target**: chapters/examples/examples_summary.tex (or wherever Part 2 begins)
**Content**: Part 2 should open with explicit statement:
- "The examples in this part are organized along the axis from the E∞-commutative atom (Heisenberg) to the E₁-associative atom (Yangian)"
- Table showing each example family's position on this axis
- Kac-Moody: E∞-chiral, single simple pole → Lie-Com exchange under duality
- W-algebras: E∞-chiral, double poles from composites → richer bar cohomology
- Lattice VOAs: E∞-chiral with E₁ sublattice structure
- Yangian: pure E₁-chiral, R-matrix braiding, no type exchange

### A2.3 — Heisenberg frame: add genus-0/genus-1/genus-2 explicit modular bar terms
**Target**: chapters/frame/heisenberg_frame.tex
**Content**: Following r30/31, write the first explicit terms of B^mod(H_k):
- g=0: ordinary bar complex (Arnold differential, already present)
- g=1: one-loop term with Sugawara/curvature correction d² = κ·ω₁
- g=2: two-loop term with M̄_{2,n} coefficient, explicit propagator pairing
- This makes "modular homotopy theory" concrete at the FIRST example

### A2.4 — Yangian as entry point: add explicit ordered-configuration bar description
**Target**: chapters/examples/yangians.tex, early section
**Content**: Parallel to Heisenberg frame, but for E₁:
- Bar complex uses ORDERED configuration spaces Conf^ord_n(X)
- Spectral parameter u = z_1 - z_2 is the coordinate difference
- R-matrix R(u) = 1 + ℏΩ/u appears as the local fusion kernel
- Duality inverts R-matrix: R(u) ↦ R(u)^{-1} (NOT type exchange)
- This is E₁-factorization, not E∞-factorization

---

## AXIS 3: YANGIAN ONTOLOGY — E₁ Precision (from r29)

### A3.1 — Three-level Yangian hierarchy (insert in yangians.tex)
**Target**: chapters/examples/yangians.tex, new subsection ~§22.1 or early
**Content**: Definition/Remark with precise three-level distinction:
- **(A) Algebraic Yangian Y(g)**: RTT presentation, formal spectral parameter u, quadratic-LINEAR (not quadratic), gr Y(g) ≅ U(g[z]) is quadratic
- **(B) E₁-chiral Yangian**: Y(g) equipped with E₁-factorization structure on curve X, spectral parameter = coordinate difference z₁-z₂
- **(C) QFT realization**: 4d Chern-Simons (Costello-Witten-Yamazaki), boundary operators = chiral algebra, line operators = monoidal category controlled by Yangian
**Cross-ref**: These three levels MUST be distinguished wherever Yangians appear

### A3.2 — Fix "Yangian is quadratic" confusion (global)
**Target**: Global grep for "Yangian" + "quadratic" across all .tex files
**Content**: Every instance must be corrected:
- Yangian is NOT quadratic in Koszul sense
- Yangian IS quadratic-linear (filtered quadratic via RTT)
- Associated graded gr Y(g) ≅ U(g[z]) IS quadratic
- PBW spectral sequence connects filtered to graded
**Verification**: No statement says "Yangian is quadratic" without "filtered" or "associated graded" qualifier

### A3.3 — Spectral parameter as geometric, not formal
**Target**: chapters/examples/yangians.tex, wherever spectral parameter appears
**Content**: Every mention of spectral parameter should clarify:
- u is NOT an external formal variable
- u = z₁ - z₂ is the coordinate difference on the curve
- This geometrization is WHY Yangians are naturally factorization objects
- OPEs depend on this difference: A(z)B(w) ~ [A,B]/(z-w) + ⋯

### A3.4 — Insert "chiral Yangian" precise definition
**Target**: chapters/examples/yangians.tex
**Content**: Definition:
> An E₁-chiral Yangian on a curve X is an E₁-factorization algebra on X whose local operator algebra reproduces the Yangian R(u)-matrix relations, with the spectral parameter identified with the coordinate difference of ordered insertion points.
**Cross-ref**: This aligns with Costello-Gaiotto-Witten factorization quantum groups

### A3.5 — Operadic table: E∞/P∞/E₁ chiral hierarchy
**Target**: chapters/theory/introduction.tex or chapters/theory/en_koszul_duality.tex
**Content**: Insert clean table:

| Algebra | Geometry | Operad | Configuration space |
|---------|----------|--------|---------------------|
| Heisenberg / comm VA | Symmetric collision | E∞ | Conf_n(X) unordered |
| KM / Virasoro / W | Symmetric with poles | E∞ | Conf_n(X) unordered |
| Yangian | Ordered collision + braid | E₁ | Conf^ord_n(X) ordered |
| Affine Yangian | Ordered + loops | E₁ + loop ext | Conf^ord with loop direction |
| Elliptic quantum group | Torus geometry | Modular deformation | Conf on elliptic curve |

### A3.6 — Rational → trigonometric → elliptic = curve geometry
**Target**: chapters/examples/yangians.tex, and chapters/examples/toroidal_elliptic.tex
**Content**: Insert remark connecting the quantum group hierarchy to curve geometry:
- Rational R-matrix → Yangian → rational spectral parameter u = z₁-z₂ on ℙ¹
- Trigonometric R-matrix → quantum loop algebra → multiplicative parameter on ℂ*
- Elliptic R-matrix → elliptic quantum group → torus coordinate on E_τ
- This is NOT three unrelated algebraic families — it IS the geometry of the curve

---

## AXIS 4: E₁-E₂-GT LADDER (from r29 — LARGELY NEW CONTENT)

### A4.1 — Insert E₁-E₂ obstruction remark
**Target**: chapters/theory/en_koszul_duality.tex, new remark after E_n Koszul duality section
**Content**: Remark:e1-e2-obstruction:
- E₁: ordered binary fusion with braid monodromy (Yangian level)
- E₂: coherent 2D interchange (little 2-disks operad)
- The gap is NOT "more commutativity" — it is coherent many-point transport
- The missing coherence data = Drinfeld associator
- Drinfeld-Kohno IS the genus-0 E₁-factorization comparison theorem
- Full E₂ coherence requires associator input

### A4.2 — Grothendieck-Teichmüller group remark
**Target**: chapters/theory/en_koszul_duality.tex or chapters/connections/concordance.tex
**Content**: Remark:grothendieck-teichmuller:
- E₂ operad is formal (Tamarkin), but formality is NOT canonical
- Non-canonicity governed by Drinfeld associators
- Symmetry group of this non-canonicity = GT
- Slogan: "GT is the hidden symmetry of the passage from braid-level data to full E₂-coherent data"
- For the Yangian: R-matrix = local two-point transport; associator = coherent many-point transport; GT = symmetry of coherent E₂-formality package

### A4.3 — Three-step ontology for Yangian/DK
**Target**: chapters/examples/yangians.tex, remark in DK ladder section
**Content**: The correct ladder is NOT E₁ → E₂ as if E₂ = "more commutative Yangian". Rather:
1. **E₁-chiral Yangian**: ordered fusion, R-matrix, DK monodromy
2. **Associator/GT layer**: coherence upgrade problem (Drinfeld associator)
3. **E₂-topological factorization**: genuine two-dimensional little-disks structure
4. **Modular layer**: genus and periods deform the whole package further

### A4.4 — DK as genus-0 E₁-factorization theorem
**Target**: chapters/examples/yangians.tex, DK section
**Content**: Sharpen the narrative:
- DK compares geometric braid monodromy (from KZ/configuration space) with algebraic braid data (from R-matrix/quantum group)
- In factorization language: both are realizations of the same local system/factorization transport on ordered configurations
- DK is the genus-0 face; modular homotopy theory asks what happens when the curve acquires genuine moduli
- ordered configurations → E₁-factorization → braid transport/R-matrix → Drinfeld-Kohno

---

## AXIS 5: NON-SCALAR THETA_A (from r34 — LARGELY NEW CONTENT)

### A5.1 — Insert non-scalar Θ_A construction in deformation_theory.tex
**Target**: chapters/theory/deformation_theory.tex, after scalar saturation discussion
**Content**: New subsection "Non-scalar universal classes":
- Requires dim H²_cyc(A,A) ≥ 2 with nontrivial mixed transferred cyclic brackets
- Choose basis η₁,...,η_r ∈ H²_cyc, modular coefficients U₁,...,U_r ∈ m_{R_mod}
- Universal recursive construction (HPT):
  - Θ^(1) = i(Σ_i η_i ⊗ U_i)
  - Θ^(N) = -h(Σ_{n≥2} (1/n!) Σ_{N₁+...+N_n=N} ℓ_n(Θ^(N₁),...,Θ^(N_n)))
- Projected obstruction equations: p(Σ_{n≥2} (1/n!) ℓ_n(Θ,...,Θ)) = 0
- These cut out the non-scalar modular deformation locus

### A5.2 — Insert explicit two-channel formula
**Target**: chapters/theory/deformation_theory.tex, continuation of A5.1
**Content**: Two-channel prototype (r=2, basis η₁, η₂):
- Θ_A = η₁⊗U₁ + η₂⊗U₂ - (1/2)hℓ₂(η₁,η₂)⊗U₁U₂ - (1/6)hℓ₃(η₁,η₁,η₂)⊗U₁²U₂ - (1/6)hℓ₃(η₁,η₂,η₂)⊗U₁U₂² + O(4)
- Non-scalar iff some mixed coefficient U_iU_j survives in gauge-normal form
- Scalar saturation is exactly the degenerate case where all mixed coefficients can be gauged away

### A5.3 — Universal HTT tree formula
**Target**: chapters/theory/deformation_theory.tex
**Content**: The closed-form non-scalar universal class:
- Θ_A^{ns} := Σ_T (1/|Aut(T)|) HTT_T(η_{i₁},...,η_{i_k}) ⊗ U_{i₁}⋯U_{i_k}
- Sum over rooted homotopy-transfer trees T
- HTT_T = standard homotopy-transfer operation from (i,p,h,ℓ_n)
- Universal, coordinate-free, automatically records every mixed non-scalar coupling

### A5.4 — Non-scalar criterion
**Target**: chapters/theory/deformation_theory.tex
**Content**: Proposition:non-scalar-criterion:
- Θ_A is genuinely non-scalar iff, in minimal cyclic model form, some mixed transferred bracket ℓ_n(η_{i₁},...,η_{i_n}) produces a nontrivial homotopy correction not removable by gauge
- Equivalently: after gauge-normal form, some mixed coefficient u_iu_j, u_iu_ju_k, etc. survives

### A5.5 — Modular version with clutching compatibility
**Target**: chapters/theory/deformation_theory.tex, and chapters/theory/higher_genus.tex
**Content**: The modular version:
- U_i = Σ_{g≥1} U_{i,g} with U_{i,g} ∈ R_•(M̄_{g,•})
- MC equation: Σ_{n≥1} (1/n!) ℓ_n(Θ_A,...,Θ_A) = 0
- Clutching compatibility: gl*(Θ_A) = Θ_A ⊛ Θ_A under modular operadic clutching maps
- This is the clean universal formula. Its scalar trace is only the shadow: tr(Θ^{ns}) = κ₁(A)U₁ + κ₂(A)U₂ + mixed trace corrections

### A5.6 — Current landscape: dim H²_cyc = 1 limitation
**Target**: chapters/theory/deformation_theory.tex, remark after non-scalar construction
**Content**: Remark:non-scalar-landscape:
- Currently accessible families (KM at generic level, Virasoro, principal W_N) have dim H²_cyc = 1
- Scalar saturation holds on this landscape (cor:scalar-saturation, prop:saturation-equivalence)
- The obstruction to non-scalar Θ_A is NOT the formalism — it is finding/building chiral algebras with dim H²_cyc ≥ 2 and nontrivial mixed brackets
- Candidates: admissible-level KM (H²_cyc,prim open), products of chiral algebras, extended algebras with multiple central extensions
- This is the TRUE frontier of MC2: not the existence theorem (proved) but the concrete realization beyond scalar

---

## AXIS 6: TOTAL MODULAR CHARACTERISTIC PACKAGE (from r36)

### A6.1 — Promote V_A K-theoretic hierarchy from remark to proposition
**Target**: chapters/theory/higher_genus.tex, rem:structural-saturation → prop:k-theoretic-extraction
**Content**: Promote to Proposition:k-theoretic-extraction:
- Let V_A := [Rπ_{g*} B̄^{(g)}(A)] ∈ K₀(M̄_g) be the virtual bar family. Then:
  - (L1) c₁(det V_A) = κ(A)·λ (first Chern class → scalar modular characteristic)
  - (L2) c_*(V_A) → Δ_A(x) (total Chern class → spectral discriminant)
  - (L3) Hol(V_A) → Π_A (holonomy representation → periodicity profile)
- These three levels are NOT the same information: L1 is trace, L2 is determinant, L3 is eigenvalue
- Each level is extractable functorially from V_A and compatible with clutching and Verdier duality

### A6.2 — Θ_A vs V_A bridge
**Target**: chapters/theory/higher_genus.tex, new remark after prop:k-theoretic-extraction
**Content**: Remark:theta-vs-VA:
- Θ_A → (B̄^{(•)}(A), d̄^Θ) → Rπ_{g*} B̄^{(g)}(A) → V_A ∈ K₀(M̄_g)
- Θ_A is UPSTREAM (chain-level flatness/integrability of genus tower)
- V_A is DOWNSTREAM (K-theoretic virtual bundle after derived pushforward)
- Θ_A tells you HOW the tower is assembled; V_A tells you WHAT virtual geometric object remains after assembly
- In scalar-saturated case: Θ_A^{min} = κ(A)·η⊗Λ, so V_A is rank-1 and c₁ carries all info
- Beyond scalar: V_A is higher-rank, c₁ no longer determines c_*, Hol

### A6.3 — Clutching decomposition of Θ_A
**Target**: chapters/theory/higher_genus.tex, wherever clutching is discussed
**Content**: Make explicit:
- ξ_sep*(Θ^{(g)}) = Σ_{g₁+g₂=g} Θ^{(g₁)} ⋆ Θ^{(g₂)} (separating degeneration)
- ξ_ns*(Θ^{(g+1)}) = Δ_ns(Θ^{(g)}) (nonseparating degeneration raises genus by 1)
- These are the GLUING LAWS of the modular bar family
- After pushforward, same laws make V_A coherent over moduli

### A6.4 — Four irreducible geometric seeds: propagate to all main chapters
**Target**: chapters/theory/introduction.tex, chapters/frame/heisenberg_frame.tex, chapters/theory/higher_genus.tex, chapters/connections/concordance.tex
**Content**: The total package is generated by four (five with E₁) irreducible inputs:
1. Arnold relation (d² = 0 at genus 0)
2. Verdier duality (D_Ran B̄(A) ≃ B̄(A!))
3. Genus-1 curvature (d_fib² = κ·ω_g, central extension)
4. Clutching (modular operadic sewing)
5. (E₁ face) Associative/R-matrix structure
- κ, Δ, Π, Θ are the OUTPUTS of this machine, not the inputs
**Verification**: Each of the four target chapters mentions these seeds

---

## AXIS 7: YANGIAN FRONTIER REPAIR (from r33)

### A7.1 — Replace all "low-stage Yangian problem" phrasing
**Target**: chapters/examples/examples_summary.tex, chapters/examples/yangians.tex, notes/PROGRAMMES.md
**Content**: Replace any residual "low-stage Yangian problem" or "first unresolved issue is low-level RTT mismatch" with:
> "The proved Yangian content is the E₁-bar-cobar duality and the evaluation-locus DK core. The first visible boundary-strip packets are computationally closed. The live frontier is the construction of the filtered H-level dg target with RTT-adapted finite quotients, together with the extension from the evaluation-generated core to the completed/coderived enlargement."

### A7.2 — Three-layer Yangian triage (insert in yangians.tex)
**Target**: chapters/examples/yangians.tex, at the start of the DK section
**Content**: Force the following separation everywhere:
- **Layer A (proved)**: chain-level E₁ bar-cobar, evaluation-locus factorization comparison, DK-2/3 on eval-gen core, finite-stage packet reductions
- **Layer B (conjectural but well-posed)**: filtered H-level dg target, RTT-adapted finite-quotient package, coefficientwise RTT completion comparison, compact-generator packet
- **Layer C (downstream physics)**: dg-shifted Yangian realization, full DK-4/5 bridge, module-category enhancement

### A7.3 — Promote conj:dg-shifted-yangian-rtt-package as organizing conjecture
**Target**: chapters/examples/yangians.tex
**Content**: Make this the single Yangian frontier theorem-object. Everything else becomes:
- Evidence for it (computational packet verifications)
- Reductions to it (H-level comparison criterion)
- Consequences of it (DK-4/5 as comparison built on the target)

---

## AXIS 8: CROSS-VOLUME BRIDGES (from Vol II audit)

### A8.1 — Insert labeled cross-volume bridge theorems
**Target**: chapters/connections/concordance.tex, new subsection "Bridges to Volume II"
**Content**: Five bridges formalized as conjectural theorem-objects:
1. **conj:vol2-bar-cobar-bridge**: SC^{ch,top} bar-cobar adjunction recovers Vol I Theorem A for boundary operators
2. **conj:vol2-hochschild-bridge**: Bulk = chiral Hochschild cochains recovers Vol I Theorem H
3. **conj:vol2-dk-ybe-bridge**: Spectral braiding r(z) = Laplace of λ-bracket recovers DK-0
4. **conj:vol2-w-algebra-bridge**: Feynman m_k matches bar differential for W-algebra examples
5. **conj:vol2-bv-functor-bridge**: Analytic hypotheses (H1)-(H4) define the physics-to-algebra functor for MC5

---

## AXIS 9: SPECIFIC FORMULA INSTALLATIONS

### A9.1 — Install modular deformation complex formula
**Target**: chapters/theory/deformation_theory.tex
**Content**: Explicit display equation:
  Def^{mod}(\cA) := \prod_{g,n} \Hom_{\Sigma_n}(C_*(\overline{\mathcal{M}}_{g,n}), \End_\cA(g,n))

### A9.2 — Install stable-graph bar sum formula
**Target**: chapters/theory/bar_cobar_construction.tex or higher_genus.tex
**Content**: Explicit display equation:
  \bar{B}^{(g)}(\cA) = \bigoplus_{\Gamma \in \mathcal{G}^{\mathrm{st}}_{g,n}} \left(\bigotimes_{v \in V(\Gamma)} \cA(g_v, \mathrm{val}(v))\right) \otimes \mathrm{or}(E(\Gamma))

### A9.3 — Install HPT non-scalar MC recursion
**Target**: chapters/theory/deformation_theory.tex
**Content**: Display equations from r34:
  Θ^{(1)} = i\!\left(\sum_i \eta_i \otimes U_i\right), \quad
  Θ^{(N)} = -h\!\left(\sum_{n \geq 2} \frac{1}{n!} \sum_{N_1+\cdots+N_n=N} \ell_n(\Theta^{(N_1)}, \ldots, \Theta^{(N_n)})\right)

### A9.4 — Install two-channel explicit formula
**Target**: chapters/theory/deformation_theory.tex
**Content**: Display equation from r34:
  \Theta_\cA^{\mathrm{ns}} = \eta_1 \otimes U_1 + \eta_2 \otimes U_2 - \tfrac{1}{2}\,h\ell_2(\eta_1,\eta_2) \otimes U_1 U_2 - \tfrac{1}{6}\,h\ell_3(\eta_1,\eta_1,\eta_2) \otimes U_1^2 U_2 - \tfrac{1}{6}\,h\ell_3(\eta_1,\eta_2,\eta_2) \otimes U_1 U_2^2 + O(4)

### A9.5 — Install clutching decomposition formula
**Target**: chapters/theory/higher_genus.tex
**Content**: Display equations:
  \xi_{\mathrm{sep}}^*(\Theta^{(g)}) = \sum_{g_1+g_2=g} \Theta^{(g_1)} \star \Theta^{(g_2)}, \quad
  \xi_{\mathrm{ns}}^*(\Theta^{(g+1)}) = \Delta_{\mathrm{ns}}(\Theta^{(g)})

### A9.6 — Install K-theoretic extraction display
**Target**: chapters/theory/higher_genus.tex
**Content**: Display equation:
  c_1(\det \mathcal{V}_\cA) \leadsto \kappa(\cA), \quad
  c_*(\mathcal{V}_\cA) \leadsto \Delta_\cA(x), \quad
  \mathrm{Hol}(\mathcal{V}_\cA) \leadsto \Pi_\cA

---

## AXIS 10: CONCORDANCE UPDATES

### A10.1 — Update nine-futures table for modular homotopy theory definition
**Target**: chapters/connections/concordance.tex, Future 3
**Content**: Future 3 should now reference the formal Definition 1.X (from A0.1) and the three-level ladder (from A1.1)

### A10.2 — Update MC4 narrative for non-scalar Θ_A
**Target**: chapters/connections/concordance.tex, MC4 section
**Content**: MC4 narrative should mention that the non-scalar Θ_A construction (A5.1-A5.5) provides the formal framework; the concrete realization beyond scalar is the live frontier

### A10.3 — Update DK narrative for E₁-E₂-GT ladder
**Target**: chapters/connections/concordance.tex, DK ladder section
**Content**: Add remark that DK is naturally an E₁-factorization theorem and the step to E₂ coherence requires associator/GT data (from A4.1-A4.4)

---

## EXECUTION ORDER (recommended)

**Phase 1 — Structural/Definitional** (highest leverage):
A0.1, A0.2, A0.4, A1.1, A1.6, A2.1, A3.1, A3.4, A3.5

**Phase 2 — Deep Formula Installation**:
A1.2, A1.3, A1.4, A1.5, A5.1, A5.2, A5.3, A5.4, A5.5, A9.1-A9.6

**Phase 3 — Propagation Across Manuscript**:
A2.2, A2.3, A2.4, A3.2, A3.3, A3.6, A6.1, A6.2, A6.3, A6.4, A7.1, A7.2, A7.3

**Phase 4 — New Content (E₁-E₂-GT, Cross-Volume)**:
A4.1, A4.2, A4.3, A4.4, A8.1

**Phase 5 — Editorial Cleanup**:
A0.3, A1.7, A5.6, A10.1, A10.2, A10.3

---

## TOTAL: 58 tasks across 10 axes
- Axis 0 (Architecture): 4 tasks
- Axis 1 (Modular Homotopy Theory): 7 tasks
- Axis 2 (Two Atoms): 4 tasks
- Axis 3 (Yangian Ontology): 6 tasks
- Axis 4 (E₁-E₂-GT): 4 tasks
- Axis 5 (Non-Scalar Θ): 6 tasks
- Axis 6 (Total Package): 4 tasks
- Axis 7 (Yangian Frontier): 3 tasks
- Axis 8 (Cross-Volume): 1 task
- Axis 9 (Formula Installation): 6 tasks
- Axis 10 (Concordance Updates): 3 tasks
