# PLATONIC IDEAL SEQUENCING — BOTH VOLUMES

## The inner thread

The subject has one thread. It begins with a single algebraic observation
(the bar differential squares to zero because the Arnold relation holds on
configuration spaces of algebraic curves) and ends with a modular theory of
open/closed chiral homotopy type controlled by a single universal
Maurer-Cartan element. Every intermediate chapter is a projection of that
thread.

## The five conceptual strata

### STRATUM 0: THE SEED (Why d^2 = 0)

The logarithmic propagator eta_{ij} = d log(z_i - z_j) on the configuration
space of distinct points on a smooth algebraic curve satisfies the Arnold
relation:

    eta_{ij} ^ eta_{jk} + eta_{jk} ^ eta_{ki} + eta_{ki} ^ eta_{ij} = 0

This single codimension-two identity forces d^2 = 0 on the bar complex.
Everything in both volumes follows from this.

### STRATUM 1: THE CLOSED ALGEBRA (Bar-cobar on a curve)

From d^2 = 0 one builds:
  - The bar complex Bar(A) = T^c(s^{-1} bar{A}) with its differential
  - The cobar functor Omega via Verdier duality
  - Theorem A: bar-cobar adjunction as Quillen equivalence
  - Theorem B: bar-cobar inversion on the Koszul locus
  - Koszul duality, Verdier duality, the quadratic-dual coalgebra
  - Chiral Hochschild theory (closed-sector)

This is Ring 1 of the current Vol I.

### STRATUM 2: THE OPEN SECTOR (The extra dimension)

The bar coalgebra carries a second structure: deconcatenation coproduct,
which is factorization along an ordered line. This is the E_1-direction.
The pair (A, Bar(A)) is a local chiral Swiss-cheese algebra.

But the deep point is not the bar ordering. It is the center theorem:

    The universal bulk acting on any boundary algebra A
    is its chiral Hochschild cochain algebra C^bullet_ch(A,A).

This is the chiral Deligne-Tamarkin theorem. It explains WHY a 2d chiral
algebra produces 3d holomorphic-topological data: the derived center of a
codimension-one boundary algebra is the universal one-dimension-up acting
algebra.

Currently this stratum is scattered across Vol II but never named as the
principle. The rewrite makes it the conceptual heart.

### STRATUM 3: THE MODULAR COMPLETION (Trace + clutching)

At genus g >= 1, the propagator acquires curvature:

    D^2_{fib} = kappa(A) * omega_g

The shadow obstruction tower Theta_A^{<= r} consists of finite-order
projections of the bar-intrinsic MC element Theta_A := D_A - d_0.

Modularity arises from traces on the open sector composed with clutching
over log-FM compactifications of bordered stable curves. The modular MC
equation:

    d Theta + (1/2)[Theta, Theta] + Delta_{clutch}(Theta) = 0

encodes all four types of codimension-one degenerations.

Theorems C (complementarity), D (modular characteristic), H (Hochschild)
are projections of this structure.

### STRATUM 4: THE LANDSCAPE (Explicit verification)

The staircase of examples:
  Free -> Heisenberg -> beta-gamma -> KM -> Virasoro -> W_N -> Yangians
  -> lattice VOAs -> minimal models

Each example tests a different layer of the theory.

### STRATUM 5: THE FRONTIER (Open problems + physics)

MC3 beyond type A. Non-principal W-duality. Factorization envelopes.
Analytic sewing. Holographic modular Koszul datum. 3d gravity. Celestial
holography. THQG.

---

## The correct volume split

**Vol I** = Strata 0-4 (the algebraic engine + landscape)
**Vol II** = Stratum 2 in full depth (the open/closed theory) + Stratum 5 (frontiers + physics)

The key structural change: Stratum 2 must appear in BOTH volumes.
  - In Vol I: a self-contained chapter stating the center theorem and its
    consequences for the closed theory (Chapter 8 below)
  - In Vol II: the full development of the open/closed theory with all
    geometric, physical, and categorical depth

---

## VOL I: MODULAR KOSZUL DUALITY

### Overture (unchanged)
The Heisenberg atom. This works perfectly as it stands.

### Part I: The Algebraic Engine

**Chapter 1. Introduction**
  The thread from Arnold to modularity, through the center theorem.
  State all five main theorems + center theorem + modular MC equation.
  Present the dependency DAG. State the staircase.
  [CRITICAL REWRITE — see 07_PREFACES_AND_INTRODUCTIONS.md]

**Chapter 2. Algebraic foundations and bar constructions**
  Quadratic algebras, bar complex, twisting morphisms, Koszul pairs.
  Convolution dg Lie algebra. Classical Koszul duality.
  [Moderate edit: add forward reference to A_infty-chiral definition]

**Chapter 3. The geometric bar complex**
  FM compactification, log forms, Arnold relation, d^2 = 0.
  Bar factorization coalgebra on Ran(X). Three-component differential.
  Verdier duality on Ran.
  [Light edit: existing content is solid]

**Chapter 4. The geometric cobar complex**
  Verdier dual transport. Distributional kernels. Schwartz kernel theorem.
  Cobar as on-shell propagators.
  [Light edit]

**Chapter 5. Bar-cobar adjunction (Theorem A)**
  Quillen equivalence. Curved A_infty. Four-regime hierarchy.
  Strong completion-tower theorem. Reconstruction-vs-duality.
  [Light edit]

**Chapter 6. Bar-cobar inversion (Theorem B)**
  Koszul locus. Spectral sequence collapse. Categorical logarithm.
  Genus-graded convergence.
  [Light edit]

**Chapter 7. Chiral Koszul duality**
  Twisting data. PBW recognition. Non-quadratic extensions.
  Koszulness characterization programme (meta-theorem).
  [Moderate edit: align K-numbering with meta-theorem items]

**Chapter 8. THE OPEN SECTOR [NEW CHAPTER]**
  The conceptual heart of the rewrite. Contents:
  (a) A_infty-chiral algebras: the local definition (from V2-1)
  (b) The local chiral Swiss-cheese operad (from V2-2)
  (c) Chiral Hochschild cochains and the brace algebra (RL-8, RL-9)
  (d) The chiral Deligne-Tamarkin theorem (RL-10): U(A) = (C^bullet_ch(A,A), A)
      is the initial Swiss-cheese pair
  (e) Bulk = derived center (RL-11)
  (f) Why 2d chiral data produces 3d HT structure: the center theorem
  (g) Tangential log curves and the global open sector (RL-2 through RL-7)
  (h) Boundary algebra as chart; Morita invariance
  (i) The one-step Jacobi coalgebra (RL-23)
  (j) Boundary-linear LG: bulk = O(dCrit(W)) (RL-24)
  [CRITICAL NEW CHAPTER — see 08_NEW_CHAPTERS.md]

**Chapter 9. Chiral modules and factorization modules**
  [Light edit: cross-reference to open sector chapter]

**Chapter 10. Chiral Hochschild cohomology and cyclic theory**
  RESTRUCTURE into three parts:
  (a) Chiral Hochschild chains (cyclic/annulus side) — existing content
  (b) Chiral Hochschild cochains as brace algebra — import from V2-7
  (c) The center theorem — cross-reference to Chapter 8
  [HEAVY REWRITE of structure; much content already exists]

**Chapter 11. Configuration spaces and FM compactifications**
  EXPAND to include:
  (a) Classical FM on smooth curves (existing)
  (b) Real oriented blowup, tangential log curves (RL-2)
  (c) Mixed configuration spaces: interior + boundary (RL-3)
  (d) Bordered FM compactification (RL-3)
  (e) Four types of codimension-one strata
  (f) Log-FM compactifications (Mok25 dependency — flag AP11)
  [HEAVY REWRITE — new geometric foundations]

**Chapter 12. Koszul pair structure and enveloping algebras**
  [Light edit]

**Chapter 13. Poincare duality**
  Verdier, NAP, homotopy Koszul dual.
  [Light edit: add remark connecting to open-sector self-intersection]

**Chapter 14. Higher genus foundations**
  Genus-g propagator, curvature, modular operads, prime form.
  [Moderate edit: integrate depth filtration V1-33, genus SS V1-34]

**Chapter 15. Higher genus complementarity (Theorem C)**
  [Light edit: cross-reference to open-sector traces]

**Chapter 16. Higher genus modular Koszul duality**
  Shadow obstruction tower, MC element, Theorems D + H.
  ADD NEW SUBSECTION: "Modular completion via open-sector traces"
  (a) Cyclic structure on open category (RL-18)
  (b) Annulus = Hochschild chains (RL-19)
  (c) Modular cooperad on bordered log-FM
  (d) MC equation with clutching (RL-16)
  (e) Modularity = trace + clutching (RL-17)
  [MODERATE REWRITE — new subsection on modular traces]

**Chapter 17. Filtered and curved Koszul duality**
  [Light edit]

**Chapter 18. The nonlinear modular shadow calculus**
  Shadow metric, connection, propagator variance, Chriss-Ginzburg
  tautological programme.
  [Moderate edit: connect shadow metric to modular tangent complex V1-35]

**Chapter 19. E_n Koszul duality**
  [Light edit]

**Chapter 20. E_1 modular Koszul duality**
  Ribbon modular operad. Feynman transform of associative modular operad.
  ADD: Connection to chiral Deligne-Tamarkin. Ribbon/'t Hooft bridge (V2-24).
  [Moderate edit]

### Part II: The Standard Landscape

**Chapter 21. Free field atoms**
  ADD: center = free polyvectors; strict base point of staircase.
  [Moderate edit]

**Chapter 22. Heisenberg-Eisenstein**
  ADD: Laplace kernel; abelian CS; complementarity kappa + kappa' = 0.
  [Moderate edit]

**Chapter 23. The beta-gamma system**
  ADD: first m_3 via degree counting; contact archetype.
  [Moderate edit]

**Chapter 24. Kac-Moody**
  ADD: nonabelian 3d action; exact complementarity under FF involution.
  [Moderate edit]

**Chapter 25. Virasoro**
  ADD: chiral Cartan formula (RL-26); wheels; infinite tower; kappa + kappa' = 13.
  [Moderate edit]

**Chapter 26. W-algebras**
  ADD: composite nonlinearity forces category beyond linear (RL-27).
  [Moderate edit]

**Chapter 27. W_3 composite fields**
  [Light edit: cross-reference brace/center perspective]

**Chapter 28. Minimal models and fusion**
  [Light edit]

**Chapter 29. Lattice foundations**
  [Light edit]

**Chapter 30. Toroidal and elliptic**
  [Light edit]

**Chapter 31. Deformation quantization**
  [Light edit]

**Chapter 32. Yangians foundations**
  ADD: E_1-chiral as open sector; spectral braiding as genus-0 shadow.
  [Moderate edit]

**Chapter 33. Yangians computations**
  ADD: Coulomb branch, CoHA (CONJECTURED, not proved).
  [Light edit — already modified]

**Chapter 34. Yangians Drinfeld-Kohno**
  [Light edit]

**Chapter 35. Bar complex tables**
  [No edit]

**Chapter 36. Landscape census**
  [Light edit: add open-sector column]

**Chapter 37. Genus expansions**
  [Light edit]

**Chapter 38. THE STAIRCASE OF EXAMPLES [NEW CHAPTER]**
  Unified narrative: each example reveals a new structural layer.
  [NEW — see 09_EXAMPLE_STAIRCASE.md]

### Part III: Bridges

**Chapter 39. Physical origins and BV-BRST**
  [Light edit: bar vs center distinction]

**Chapter 40. Holomorphic-topological boundary conditions**
  REWRITE "why 2d+1" using center theorem, not bar ordering.
  [MODERATE REWRITE]

**Chapter 41. Yang-Mills boundary theory**
  [Light edit]

**Chapter 42. Yang-Mills instanton screening**
  [Light edit]

**Chapter 43. Kontsevich integral**
  [Light edit]

**Chapter 44. Derived Langlands and opers**
  [Light edit]

**Chapter 45. Arithmetic shadows**
  REFINE: separate proved depth decomposition from speculative motivic claims.
  Move arithmetic packet connection to frontier appendix.
  [Moderate edit]

### Part IV: The Frontier

**Chapter 46. Concordance (constitution)**
  ADD sections on:
  (a) Open-sector architecture
  (b) Center theorem as proved result
  (c) Modular-completion-from-traces framework
  (d) Updated three-pillar integration with center perspective
  (e) Aligned K-numbering / meta-theorem items
  [MODERATE REWRITE]

**Chapter 47. Outlook and open problems**
  [Light edit]

**Chapters 48-51. Frontier chapters**
  Non-principal W-duality, analytic sewing, factorization envelopes,
  MC3 beyond type A.
  [Light edit: connect to open-sector perspective where appropriate]

### Appendices (4 clusters — as now)

---

## VOL II: A-INFINITY CHIRAL ALGEBRAS AND 3D HOLOMORPHIC-TOPOLOGICAL QFT

### Preface
  The open sector as primary object. The center theorem as the 2d->3d bridge.
  [CRITICAL REWRITE — see 07_PREFACES_AND_INTRODUCTIONS.md]

### Introduction
  From Swiss-cheese to center to modularity.
  [CRITICAL REWRITE — see 07_PREFACES_AND_INTRODUCTIONS.md]

### Part I: The Open/Closed Theory

**Chapter 1. Bar complex as Swiss-cheese correspondence**
  foundations.tex content. Bar differential = holomorphic factorization.
  Bar coproduct = topological factorization.
  [Moderate edit: clean up framing]

**Chapter 2. A_infty-chiral algebras: axioms**
  axioms.tex content. Sesquilinearity, unitality, spectral A_infty.
  [Light edit: ensure Vol I consistency]

**Chapter 3. The local chiral Swiss-cheese operad**
  locality.tex + equivalence.tex content. SC^{ch,top} definition.
  Recognition theorem. Homotopy-Koszulity.
  [Light edit]

**Chapter 4. FM calculus and Stokes proof of A_infty relations**
  fm_calculus.tex content. A_infty from Stokes on FM.
  [Light edit]

**Chapter 5. THE CHIRAL CENTER THEOREM [EXPANDED/REFRAMED]**
  brace.tex + hochschild.tex content, PLUS:
  (a) Brace algebra on C^bullet_ch(A,A) — full proof
  (b) Chiral Deligne-Tamarkin: U(A) is initial Swiss-cheese pair
  (c) Bulk reconstruction: bulk = Z_der(C_op) = C^bullet_ch(A_b, A_b)
  (d) Universal property: Phi_{(B,A)}: B -> C^bullet_ch(A,A)
  (e) Independence of generator (Morita invariance)
  [CRITICAL REWRITE — promoted from HT-specific to universal]

**Chapter 6. TANGENTIAL LOG CURVES AND THE GLOBAL OPEN SECTOR [NEW]**
  (a) Tangential log curves (X, D, tau)
  (b) Real oriented blowup, boundary intervals
  (c) Mixed configuration spaces
  (d) Mixed Ran space
  (e) Open/closed factorization dg-category (definition)
  (f) Boundary algebra as endomorphism chart
  (g) Morita invariance
  (h) Global center: bulk on the curve
  [NEW CHAPTER — see 08_NEW_CHAPTERS.md]

**Chapter 7. ONE-STEP JACOBI COALGEBRA AND EXACT MODELS [NEW]**
  (a) One-step Jacobi coalgebra J_{F,p}
  (b) Cobar = exact pointed line algebra
  (c) Explicit A_infty model from Taylor coefficients
  (d) Free / quadratic / cubic subexamples
  (e) Boundary-linear LG: bulk = O(dCrit(W))
  (f) Koszul duality in the exact sector
  [NEW CHAPTER — see 08_NEW_CHAPTERS.md]

### Part II: Descent and Coarse Objects

**Chapter 8. PVA descent**
  [Light edit]

**Chapter 9. Raviolo vertex algebras**
  [Light edit]

**Chapter 10. Rosetta stone**
  [Light edit: add center-theorem column]

### Part III: The Bulk-Boundary-Line Triangle

**Chapter 11. BULK = DERIVED CENTER [PROMOTED]**
  ht_bulk_boundary_line_core.tex content, REFRAMED:
  (a) Universal theorem: A_bulk ~ Z_der(C_op) ~ HH^bullet(A^!)
  (b) Three principles: intrinsic before complement-dependent, derived before
      cohomology, local exact before global
  (c) Morita-categorical formulation
  (d) Line operators as A^!-modules
  [CRITICAL REWRITE — from HT-specific to universal]

**Chapter 12. Spectral braiding and the Yangian shadow**
  spectral-braiding-core.tex content, PLUS Laplace transform dictionary.
  [Moderate edit]

**Chapter 13. Line operators**
  line-operators.tex content. Frame: lines are objects of C_op; A^!-module
  structure is a presentation.
  [Moderate edit]

**Chapter 14. MODULAR COMPLETION FROM OPEN-SECTOR TRACES [NEW]**
  (a) Cyclic structure on open factorization category
  (b) Annulus = Hochschild chains (excision proof)
  (c) Modular cooperad on bordered log-FM
  (d) Modular twisting morphism
  (e) MC equation with clutching
  (f) Modularity = trace + clutching (not an axiom on closed algebra)
  (g) Ribbon/'t Hooft bridge: 't Hooft expansion = open-sector trace
  [NEW CHAPTER — see 08_NEW_CHAPTERS.md]

### Part IV: Examples

**Chapter 15. Free multiplet**
  Explicit center computation. Strict base point.

**Chapter 16. Abelian Chern-Simons / Heisenberg**
  Spectral kernel r(z) = hbar q_1 q_2 / z. 3d action. Complementarity.

**Chapter 17. Cubic Landau-Ginzburg**
  First m_3. Degree counting on FM. Quartic vanishing.

**Chapter 18. Affine sl_2**
  Nonabelian 3d action. Sugawara. Complementarity under FF involution.

**Chapter 19. Virasoro**
  Chiral Cartan formula. Topological enhancement. Wheel combinatorics.

**Chapter 20. W_3**
  Composite nonlinearity. Quartic resonance. Category beyond linear.

[These example chapters may need significant NEW WRITING depending on how
much is already in the Vol II examples files. Cross-reference with V2-18.]

### Part V: Quantization and Holography

**Chapter 21. Modular PVA quantization**
  [Moderate edit: connect to modular completion framework]

**Chapter 22. Affine half-space BV**
  [Light edit]

**Chapter 23. Holomorphic-topological field theories**
  [Light edit]

**Chapter 24. 3D gravity from E_1-chiral Koszul duality**
  REFRAME: ground in center theorem.
  [Moderate edit]

**Chapter 25. Celestial boundary transfer**
  [Light edit: mark Conditional where appropriate]

**Chapter 26. Log HT monodromy**
  [Light edit]

**Chapter 27. Anomaly-completed structures**
  [Light edit: mark Conditional]

**Chapter 28. Conclusion and open problems**
  [Light edit]

### Appendices
Brace signs, FM proofs, orientations, PVA expanded.
[Light edit: consistency check with Vol I signs appendix]
