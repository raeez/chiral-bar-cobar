# BLUEPRINTS FOR PREFACES AND INTRODUCTIONS

Detailed map-and-territory of both prefaces and both introductions:
the logical, ontological, and spiritual development across the full arc.

---

## VOL I PREFACE: "From a point to a curve to a moduli space"

### Current state
510 lines modified. Heisenberg atom as anchor. Generating function refined.
Complementarity formula corrected. Multi-generator W-algebra patterns added.
Missing: the open-sector thread.

### The four-act structure

**Act 1: The seed** (~10 pages)
  The Heisenberg current J(z) on P^1. The logarithmic propagator:

      eta_{12} = d log(z_1 - z_2)

  The Arnold relation on three points:

      eta_{12} ^ eta_{23} + eta_{23} ^ eta_{31} + eta_{31} ^ eta_{12} = 0

  Therefore d^2 = 0 on the bar complex Bar(H_k) = T^c(s^{-1} J).

  SHOW: the explicit bar differential, the explicit d^2 computation, the
  explicit cancellation via Arnold. Do not just state it — compute it in
  front of the reader for the Heisenberg case.

  The MC element: Theta_{H_k} = kappa * eta tensor Lambda. The parity
  argument: why transferred m_n = 0 for n >= 3 on the Heisenberg.

  The generating function:

      sum_{g >= 1} F_g(H_k) hbar^{2g-2} = k * (hat{A}(i hbar) - 1)

  with explicit Taylor coefficients F_1 = k/24, F_2 = 7k/5760, F_3 = 31k/967680.

  **Emotional arc:** From a single 1-form on a configuration space, an entire
  modular theory emerges. The reader should feel: "this is inevitable."

**Act 2: The duality** (~5 pages)
  The bar complex is a coalgebra. Its Verdier dual is the Koszul dual:

      H_k^! = Sym^{ch}(V*) (NOT H_{-k})

  Bar-cobar inversion: Omega(Bar(H_k)) ~ H_k on the Koszul locus.
  Complementarity: what H_k sees as obstruction, H_k^! sees as deformation.

  The complementarity ladder (first appearance):
  - Heisenberg: kappa + kappa' = 0
  - KM: kappa + kappa' = 0 (under FF involution k -> -k - 2h^vee)
  - Virasoro: kappa + kappa' = 13 (under c -> 26-c)
  - W_3: kappa + kappa' = 250/3 (under c -> 100-c)

  **Emotional arc:** Duality is not decoration — it is the engine.

**Act 3: The open sector** (~5 pages, NEW)
  The bar coalgebra carries a second structure: the deconcatenation coproduct

      Delta[a_1 | ... | a_n] = sum_{i=0}^n [a_1|...|a_i] tensor [a_{i+1}|...|a_n]

  This is factorization along an ordered line. The pair (A, Bar(A)) is a
  local chiral Swiss-cheese algebra on D x R.

  But the deep point is not the bar ordering. It is the CENTER THEOREM:

  > The universal bulk acting on any boundary algebra A is its chiral
  > Hochschild cochain algebra C^bullet_ch(A,A).

  This is why a 2d chiral algebra produces 3d holomorphic-topological data:
  the derived center of a codimension-one boundary algebra is the universal
  one-dimension-up acting algebra.

  On a curve with punctures, the open sector lives on the real-oriented
  blowup. The boundary algebra is the endomorphism algebra of a chosen
  vacuum. Different vacua give Morita-equivalent presentations.

  **Emotional arc:** The extra dimension was always there, hiding in the
  deconcatenation coproduct and the center theorem. We did not add it —
  we uncovered it.

**Act 4: The modular completion** (~5 pages)
  At genus g >= 1, the propagator acquires curvature:

      D^2_{fib} = kappa(A) * omega_g

  The shadow obstruction tower Theta_A^{<= r} projects the single bar-intrinsic
  MC element Theta_A := D_A - d_0. Traces on the open sector, composed with
  clutching over log-FM compactifications, produce the full modular theory.

  The five main theorems (A through H) are projections of this structure.
  The staircase of examples (free -> Heisenberg -> ... -> W_3) tests each
  layer.

  **Emotional arc:** The modular theory is not added by hand — it is forced
  by traces and clutching on the open sector.

### Directives for the preface
- SHOW, don't tell. Every formula must be computed, not just stated.
- The Heisenberg atom remains the anchor. Acts 3 and 4 grow FROM it.
- Do not make Act 3 longer than Act 1. The open sector is a revelation,
  not a second book.
- Reference the staircase but do not develop it (that is Part II).
- End with a one-paragraph statement of what the five main theorems say
  and how they relate to each other.

---

## VOL I INTRODUCTION: "From Arnold to modularity"

### Current state
200+ lines modified. Framework axiomatization, universality statement,
Theorem H projection. Missing: center theorem, staircase, dependency DAG.

### The structure

**Section 1: The thread** (~3 pages)
  State the five conceptual strata:
  0. The seed: Arnold relation forces d^2 = 0
  1. The closed algebra: bar-cobar adjunction and inversion
  2. The open sector: center theorem gives 3d from 2d
  3. The modular completion: traces + clutching
  4. The landscape: examples verify the machine

  State the dependency DAG (ASCII art or tikz):

      Arnold
        |
      d^2 = 0
        |
      Thm A (adjunction) --> Thm B (inversion)
        |                         |
      Center thm            Thm C (complementarity)
      (bulk = HH)                 |
        |                   Thm D (modular char kappa)
      3d HT                       |
        |                   Thm H (Hochschild)
      Modular MC                  |
      (Theta: trace+clutch) Shadow obstruction tower Theta^{<=r}

**Section 2: The five main theorems** (~5 pages)
  State each theorem with its precise hypotheses and conclusion.
  For each, say what it is a projection OF (the modular twisting morphism).
  Cross-reference to the body chapter where it is proved.

  Theorem A: Bar-cobar adjunction. B^ch -| Omega^ch on Ran(X).
  Theorem B: Bar-cobar inversion. Omega(Bar(A)) ~ A on Koszul locus.
  Theorem C: Complementarity. Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)).
  Theorem D: Modular characteristic. kappa(A) universal, additive.
  Theorem H: Chiral Hochschild. ChirHoch*(A) polynomial, Koszul-functorial.

**Section 3: The center theorem** (~3 pages)
  State: for every A_infty-chiral algebra A,
    U(A) = (C^bullet_ch(A,A), A)
  is the universal local chiral Swiss-cheese pair.

  Consequence: bulk = C^bullet_ch(A,A). This explains the 2d -> 3d jump.

  On a tangential log curve (X,D,tau), the open sector is a cyclic
  factorization dg-category. Its derived center is the bulk.

  Modularity is trace + clutching on the open category.

**Section 4: The staircase** (~3 pages)
  State the six examples and what each reveals:
  Free: strict base point; center = free polyvectors
  Heisenberg: first spectral layer; abelian CS
  beta-gamma: first m_3; contact archetype; degree counting
  KM: nonabelian; exact complementarity; 3d CS
  Virasoro: infinite tower; wheel combinatorics; Cartan formula
  W_3: composite nonlinearity; quartic resonance

**Section 5: The three concentric rings** (~2 pages)
  Ring 1: proved core (Thms A-H, MC1,2,4,5, MC3 type A)
  Ring 2: nonlinear characteristic (shadow obstruction tower, ring structure)
  Ring 3: physics frontier (W-duality, Yangians, holography)

**Section 6: Guide to reading** (~2 pages)
  Which chapters to read for which purpose.
  Dependencies between chapters.
  What requires what.

### Directives for the introduction
- State theorems precisely. Do not just gesture at them.
- Every claim must be qualified by genus, level, type restrictions (AP6, AP7).
- The introduction is a MAP. It tells you what is in each room, not what
  each room looks like inside.
- Do not prove anything in the introduction. Forward-reference only.
- End with a paragraph on what is NOT in the manuscript: the open problems,
  the frontier, the remaining conjectures.

---

## VOL II PREFACE: "The open sector as primary object"

### Current state
Motivates holomorphic x topological; bar complex as unified structure.
Missing: the categorical/center perspective.

### The structure

**Opening paragraph:**
  "The primitive object of chiral homotopy theory is not a single algebra
  but a cyclic factorization dg-category on the real-oriented blowup of a
  punctured curve."

  Do NOT soften this. State it as the thesis of Vol II.

**Section 1: Why a second volume?** (~2 pages)
  Vol I proves the algebraic engine: bar-cobar, Koszul, shadow obstruction tower.
  Vol II develops the categorical and geometric depth of the open sector
  and its applications to 3d holomorphic-topological physics.

  The key theorem that bridges the volumes: the chiral center theorem.
  Vol I states it algebraically. Vol II develops its full geometric,
  physical, and categorical consequences.

**Section 2: The open sector** (~3 pages)
  On a tangential log curve (X, D, tau):
  - The real oriented blowup produces boundary intervals
  - Interior insertions are holomorphic; boundary insertions are ordered
  - The mixed configuration space is the natural domain
  - A factorization cosheaf on the mixed Ran space is the correct object

  A chosen boundary vacuum b produces an A_infty-chiral algebra A_b.
  Different choices give Morita-equivalent presentations.
  The intrinsic object is the Morita class.

**Section 3: Bulk = center; modularity = traces** (~3 pages)
  The derived center Z_ch(C_op) = C^bullet_ch(A_b, A_b) is the universal
  local bulk. This is why 2d chiral data produces 3d HT structure.

  Modularity is not an adjective on the closed algebra. It is the statement
  that traces on the open category survive clutching across nodal degenerations.

**Section 4: The examples** (~2 pages)
  The staircase: free -> Heisenberg -> LG -> KM -> Virasoro -> W_3.
  Each computed in full in Vol II Part IV.

**Section 5: Guide to Vol II** (~1 page)
  Part I: the open/closed theory (definitions, theorems, constructions)
  Part II: descent to coarser objects (PVA, raviolo)
  Part III: the bulk-boundary-line triangle
  Part IV: examples
  Part V: physics (quantization, holography, gravity)

### Directives for the Vol II preface
- Assertive tone. This is not "another perspective on chiral algebras."
  It is the correct categorical framing.
- Reference Vol I explicitly for the algebraic engine.
- Do not repeat Vol I proofs. Cross-reference.
- Keep it short. The preface should be <15 pages.

---

## VOL II INTRODUCTION: "From Swiss-cheese to center to modularity"

### The structure

**Section 1: Theorem 0 of Vol II** (~3 pages)
  State the chiral center theorem:
  For every A_infty-chiral algebra A, U(A) = (C^bullet_ch(A,A), A) is the
  universal local chiral Swiss-cheese pair.

  This is the single theorem that organizes the entire volume.

**Section 2: Local -> global -> modular** (~3 pages)
  Local: the Swiss-cheese operad SC^{ch,top}. Recognition theorem.
  Global: tangential log curves, mixed Ran space, factorization category.
  Modular: traces, clutching, modular twisting morphism.

**Section 3: The examples** (~2 pages)
  Brief preview of the six worked examples.

**Section 4: Relation to Vol I** (~2 pages)
  Vol I Thm A = adjunction of bar-cobar = one aspect of the center theorem.
  Vol I Thm B = inversion = the center theorem restricted to the Koszul locus.
  Vol I Thms C, D, H = projections of the modular twisting morphism.
  Vol I shadow obstruction tower = Taylor expansion of Theta_C.

**Section 5: Relation to the literature** (~2 pages)
  Francis-Gaitsgory: Com-Lie on Ran, NOT E_1-E_1. We do E_1-E_1.
  Gui-Li-Zeng: quadratic chiral duality, different from FG and from ours.
  Costello-Dimofte-Gaiotto: predicted the center theorem and line-category picture.
  Khan-Zeng: PVA -> 3d HT gauge theory; Virasoro -> topological enhancement.
  Dimofte-Niu-Py: line operators as A^!-modules, dg-shifted Yangian.
  Mok: log-FM compactifications for the bordered/nodal geometry.
  Malikov-Schechtman: Ch_infty algebras, homotopy chiral.

  **IMPORTANT:** State precisely what each reference does and does NOT do.
  Do not overclaim influence. Do not underclaim. Beilinson pass on every
  attribution.

### Directives for the Vol II introduction
- Begin with the center theorem. Everything flows from it.
- Do not re-derive the bar-cobar theory. Vol I did that.
- State what is NEW in Vol II: the categorical framework, the global
  construction, the physical realizations, the examples.
- End with a paragraph on what remains open.
