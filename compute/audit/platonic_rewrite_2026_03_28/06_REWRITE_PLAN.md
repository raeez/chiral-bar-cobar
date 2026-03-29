# THE FULL EXECUTION PLAN

## Waves, dependencies, and directives

The rewrite is organized into 5 waves, each completing a layer that the
next wave depends on. Within each wave, tasks are parallelizable.

---

## WAVE 1: FOUNDATIONS (no downstream dependencies)

**Goal:** Establish the geometric and definitional foundations that all
subsequent rewrites depend on.

### Task 1.1: Configuration spaces chapter expansion
**File:** chapters/theory/configuration_spaces.tex (Vol I)
**Cluster:** C
**What to do:**
  - Add Section: "Tangential log curves and real-oriented blowup"
    Define (X, D, tau). Construct X~_D. Show boundary circles S^1_p.
    Cut to intervals I_p via tangential basepoint.
  - Add Section: "Mixed configuration spaces"
    Define Conf^{oc}_{I,m}(X,D,tau). Interior x boundary.
    State factorization properties.
  - Add Section: "Bordered Fulton-MacPherson compactification"
    Define FM^{oc,log}_{I,m}. Enumerate four types of codimension-one strata.
    Flag Mok25 dependency with AP11 notation.
  - Add Section: "Depth filtration"
    Tridegree (g,n,d) from log boundary depth.
**Dependencies:** None.
**Estimated size:** ~15 pages new content.
**Beilinson check:** Every statement about log-FM that depends on Mok25 must
have an explicit "[Mok25, Thm X.Y.Z]" citation and a fallback clause.

### Task 1.2: Vol II preface and introduction rewrite
**Files:** preface.tex, introduction.tex (Vol II)
**Cluster:** A
**What to do:**
  - Preface: "The open sector as primary object"
    Open with the claim. Motivate via Costello-Dimofte-Gaiotto expectations.
    State the center theorem as the organizing principle.
    Present the volume outline through the open-sector lens.
  - Introduction: "From Swiss-cheese to center to modularity"
    State Theorem 0 (center theorem) of Vol II.
    Present: local -> global -> modular.
**Dependencies:** None (these are expository).
**Estimated size:** ~10 pages rewritten.
**Directive:** Do NOT write detailed proofs here. State theorems, give
motivation, forward-reference to body chapters.

---

## WAVE 2: CORE NEW CONTENT

**Goal:** Write the new chapters that contain the heart of the rewrite.

### Task 2.1: Vol I Chapter 8 — "The open sector"
**File:** NEW chapters/theory/open_sector.tex (Vol I)
**Clusters:** A, B
**What to do:**
  Write the chapter from scratch. Contents:

  Section 8.1: A_infty-chiral algebras
    Import the definition from V2-1. Sesquilinearity, unitality, spectral
    A_infty identities. Notation: m_k, s, Lambda_i. Match Vol I conventions.
    Relate to strict chiral algebras as m_k = 0 for k >= 3.

  Section 8.2: The local chiral Swiss-cheese operad
    Import from V2-2. SC^{ch,top} with operation spaces FM_k(C) x E_1(m).
    No open-to-closed. State recognition theorem. Reference F4/F5 in Vol II.

  Section 8.3: Chiral Hochschild cochains
    Define C^n_ch(A,A). Define partial composition o_i with spectral
    substitution Lambda_i. Define brace operations. Define Gerstenhaber bracket.

  Section 8.4: The chiral brace algebra theorem
    State and prove: (C^bullet_ch(A,A), delta, {-}) is a brace dg algebra.
    Proof: operadic associativity of block substitution. delta^2 = 0 from
    [m,m] = 0.

  Section 8.5: The chiral Deligne-Tamarkin theorem
    State and prove: U(A) = (C^bullet_ch(A,A), A) is a local chiral
    Swiss-cheese pair, initial among all such pairs with open color A.
    Proof: define Phi_{(B,A)}(b)_n := mu_{1;n}(b; a_1,...,a_n). Show it is
    a brace morphism. Show uniqueness.

  Section 8.6: Bulk = derived center
    Z_ch(C_op) ~ C^bullet_ch(A_b, A_b) independent of generator.
    Morita invariance proof.

  Section 8.7: Why 2d chiral data produces 3d HT structure
    The center theorem as the conceptual explanation. Not bar ordering.
    But bar coalgebra remains the open-sector coalgebra model.
    The bar/center distinction (RL-14).

  Section 8.8: Tangential log curves and the global open sector
    Summary of the global construction (referencing Chapter 11 for details).
    Open/closed factorization dg-category as a definition.
    Boundary algebra as endomorphism chart.

  Section 8.9: The one-step Jacobi coalgebra
    J_{F,p} = (S^c(sU + R), b_F). Cobar = pointed line algebra.
    Explicit A_infty model from Taylor coefficients.
    Three subexamples: free, quadratic, cubic.

  Section 8.10: Boundary-linear Landau-Ginzburg
    W(x,y) = <y, F(x)>. Boundary algebra A_F. By dg HKR:
    Z^ch_der(A_F) ~ O(dCrit(W)). Bulk = functions on derived critical locus.

**Dependencies:** Task 1.1 (for the global construction reference).
**Estimated size:** ~40 pages.
**This is the most important single task in the entire rewrite.**

### Task 2.2: Vol II Chapter 5 — "The chiral center theorem" (expanded)
**File:** brace.tex + hochschild.tex (Vol II, restructured)
**Cluster:** A
**What to do:**
  Restructure existing content + add:
  (a) Full proof of brace algebra theorem (from RL-9)
  (b) Statement and proof of Deligne-Tamarkin theorem (from RL-10)
  (c) Bulk reconstruction as universal property
  (d) Morita invariance of center
**Dependencies:** Task 2.1 (for consistency of notation and definitions).
**Estimated size:** ~25 pages (much existing content, ~10 pages new).

### Task 2.3: Vol II Chapter 6 — "Tangential log curves and the global open sector"
**File:** NEW (Vol II)
**Cluster:** A
**What to do:**
  Write from scratch. Contents:
  (a) Tangential log curves (X, D, tau) — full definition
  (b) Real oriented blowup X~_D, boundary circles, intervals
  (c) Mixed configuration spaces — formal definition
  (d) Mixed Ran space — formal definition
  (e) Open/closed factorization dg-category — definition (not theorem)
  (f) Boundary algebra from compact generator — theorem with proof
  (g) Morita invariance — theorem with proof
  (h) Global center: Z_ch(C_op) on the curve
**Dependencies:** Task 1.1 (geometric foundations).
**Estimated size:** ~20 pages.

### Task 2.4: Vol II Chapter 7 — "One-step Jacobi coalgebra and exact models"
**File:** NEW (Vol II)
**Cluster:** F
**What to do:**
  Write from scratch. Contents:
  (a) One-step Jacobi coalgebra J_{F,p} — construction
  (b) Cobar algebra Omega(J_{F,p}) — exact pointed line algebra
  (c) Explicit A_infty model K^{gr}_{F,p} = k[c_alpha] tensor Lambda(lambda_i)
  (d) Higher products m_n from Taylor coefficients of F
  (e) Three subexamples: F=0 (free), F=x^2 (quadratic), F=x^3 (cubic)
  (f) Boundary-linear LG: bulk = O(dCrit(W))
  (g) Koszul duality in the exact sector
**Dependencies:** Task 2.1 (definitions).
**Estimated size:** ~15 pages.

---

## WAVE 3: MODULAR COMPLETION + EXAMPLES

**Goal:** Integrate the modular-traces perspective and write the example chapters.

### Task 3.1: Vol I higher-genus modular Koszul — traces subsection
**File:** chapters/theory/higher_genus_modular_koszul.tex (Vol I)
**Cluster:** E
**What to do:**
  Add new section: "Modular completion via open-sector traces"
  (a) Cyclic structure on open factorization category
  (b) Annulus = Hochschild chains (excision proof)
  (c) Modular cooperad on bordered log-FM (definition)
  (d) Modular twisting morphism Theta_C
  (e) MC equation d Theta + (1/2)[Theta,Theta] + Delta_clutch(Theta) = 0
  (f) Modularity = trace + clutching (the punchline)
  Cross-reference to shadow tower: Theta_A^{<=r} are finite-order projections
  of the modular twisting morphism.
**Dependencies:** Tasks 2.1 (open sector), 1.1 (bordered FM).
**Estimated size:** ~10 pages new.

### Task 3.2: Vol II Chapter 14 — "Modular completion from open-sector traces"
**File:** NEW (Vol II)
**Cluster:** E
**What to do:**
  Write from scratch. Full development of:
  (a) Cyclic structure on open factorization category
  (b) Annulus = Hochschild chains (excision proof, detailed)
  (c) Modular cooperad on bordered log-FM
  (d) Modular twisting morphism — construction
  (e) MC equation with clutching — proof from Stokes
  (f) Modularity = trace + clutching
  (g) Ribbon/'t Hooft bridge: 't Hooft expansion = open-sector trace on
      ribbon modular operad
**Dependencies:** Tasks 2.3 (global open sector), 1.1 (bordered FM).
**Estimated size:** ~25 pages.

### Task 3.3: Vol II bulk-boundary-line restructure
**File:** ht_bulk_boundary_line_core.tex (Vol II)
**Cluster:** A
**What to do:**
  Restructure to separate universal theorem from HT realization:
  Part A (universal): bulk = Z_der(C_op) = HH^bullet(A^!) for any A_infty-chiral.
    Three principles. Morita-categorical formulation. Line operators as A^!-modules.
  Part B (HT realization): specialize to 3d HT theories. Holographic datum.
    Physical examples.
**Dependencies:** Task 2.2 (center theorem in Vol II).
**Estimated size:** ~5 pages new, ~15 pages restructured.

### Task 3.4: Vol II example chapters (6 chapters)
**Files:** NEW chapters 15-20 (Vol II)
**Cluster:** F
**What to do:**
  Write 6 new example chapters, each computing:
  - The A_infty-chiral structure
  - The chiral Hochschild cochains / center
  - The 3d HT action (where applicable)
  - The genus-1 data (kappa, F_1)
  - The complementarity sum

  Ch 15: Free multiplet. m_2(a,b) = ab, rest zero. Center = free polyvectors.
  Ch 16: Heisenberg. {J_lambda J} = k lambda. r(z) = hbar/z. kappa = k/2.
  Ch 17: Cubic LG. m_3(a,b,c) = 2g abc. m_4 = 0 by degree counting on FM.
  Ch 18: Affine sl_2. 27 Jacobi triples. Sugawara. kappa = 3(k+2)/4.
  Ch 19: Virasoro. Chiral Cartan. Wheels. kappa = c/2. kappa + kappa' = 13.
  Ch 20: W_3. Composite Lambda. All coefficients. kappa = 5c/6. kappa + kappa' = 250/3.

**Dependencies:** Tasks 2.1 (definitions), 2.4 (Jacobi coalgebra for LG).
**Estimated size:** ~60 pages total (~10 per example).

---

## WAVE 4: LANDSCAPE + BRIDGES

**Goal:** Integrate the open-sector perspective into the existing landscape
and harmonize cross-volume bridges.

### Task 4.1: Vol I example chapter open-sector subsections
**Files:** 7 example chapters (Vol I)
**Cluster:** F
**What to do:**
  Each example chapter gets a new subsection: "Open-sector perspective"
  (1-2 pages each, ~10 pages total). Content:
  - Free fields: center = free polyvectors
  - Heisenberg: Laplace kernel, abelian CS
  - beta-gamma: first m_3, contact archetype
  - Kac-Moody: nonabelian 3d action
  - Virasoro: chiral Cartan, topological enhancement
  - W-algebras: composite nonlinearity
  - Yangians: E_1-chiral as open sector
**Dependencies:** Task 2.1 (open sector chapter).
**Estimated size:** ~10 pages total.

### Task 4.2: Vol I Chapter 38 — "The staircase of examples"
**File:** NEW (Vol I, Part II)
**Cluster:** F
**What to do:**
  Write unified narrative showing how each example reveals a new layer:
  (a) The complexity hierarchy: strict -> spectral -> first m_3 -> nonabelian
      -> wheels/infinite -> composite nonlinear
  (b) Shadow depth classification: G/L/C/M
  (c) The complementarity ladder: kappa + kappa' = 0, 0, 13, 250/3, ...
  (d) The convergence staircase: terminating at 2, 3, 4, infinity
  (e) The center staircase: free polyvectors -> Koszul -> dCrit -> ...
**Dependencies:** Task 4.1 (open-sector subsections in example chapters).
**Estimated size:** ~15 pages.

### Task 4.3: Cross-volume bridge harmonization
**Files:** Multiple (both volumes)
**Cluster:** (all)
**What to do:**
  - Bar-cobar bridge: add center-theorem cross-reference
  - Hochschild bridge: UPGRADE from conjectural to consequence of center theorem
  - DK-YBE bridge: connect Laplace transform to Yangian spectral kernel
  - W-algebra bridge: connect composite nonlinearity to categorical necessity
  - Ribbon/'t Hooft bridge: connect to cyclic trace on open category
  - BV functor bridge: keep conditional, flag (H1)-(H4)
  - NEW center bridge: Vol I center theorem = Vol II center theorem
**Dependencies:** Tasks 2.1, 2.2, 3.2.
**Estimated size:** ~5 pages of new cross-references.

### Task 4.4: Vol I holomorphic-topological chapter rewrite
**File:** chapters/connections/holomorphic_topological.tex (Vol I)
**Cluster:** A
**What to do:**
  Rewrite "why 2d+1" section using center theorem.
  Old: "the bar complex has an E_1 direction"
  New: "the derived center of a codimension-one boundary algebra is the
  universal one-dimension-up acting algebra"
**Dependencies:** Task 2.1.
**Estimated size:** ~3 pages rewritten.

---

## WAVE 5: EDITORIAL + PROPAGATION

**Goal:** Finalize introductions, preface, concordance, metadata.

### Task 5.1: Vol I introduction rewrite
**File:** chapters/theory/introduction.tex (Vol I)
**Clusters:** A, B, G
**What to do:**
  Full rewrite. The introduction should:
  (a) State the thread: Arnold -> bar -> open sector -> center -> modularity
  (b) Present the dependency DAG (5 main theorems + center theorem + MC eq)
  (c) State the staircase
  (d) State the five conceptual strata
  (e) Qualify all universal claims (AP7)
  (f) Forward-reference to body chapters
**Dependencies:** ALL previous waves.
**Directive:** Write this LAST. The introduction is a map; the territory
must exist first.

### Task 5.2: Vol I preface rewrite
**File:** chapters/frame/preface.tex (Vol I)
**Clusters:** A, G
**What to do:**
  Add the four-act structure:
  Act 1: The seed (Arnold, d^2=0, Heisenberg atom — existing, refine)
  Act 2: The duality (bar-cobar, Koszul, Verdier — existing, tighten)
  Act 3: The open sector (NEW — deconcatenation -> center -> 3d)
  Act 4: Modularity (curvature, traces, clutching — existing, reframe)
**Dependencies:** Task 5.1 (introduction tells us what the preface must foreshadow).

### Task 5.3: Vol I concordance update
**File:** chapters/connections/concordance.tex (Vol I)
**Clusters:** A, E, G
**What to do:**
  Add new sections:
  (a) sec:concordance-open-sector — open-sector architecture
  (b) sec:concordance-center-theorem — center theorem as proved result
  (c) sec:concordance-modular-traces — modular-completion-from-traces
  (d) Update three-pillar integration with center perspective
  (e) Align K-numbering with meta-theorem items
  (f) Update MC frontier with unified narrative
**Dependencies:** Task 2.1.

### Task 5.4: Metadata regeneration
**Files:** metadata/*.{json,jsonl,md,dot}
**What to do:**
  - python3 scripts/generate_metadata.py
  - Verify new labels, new claims, new dependency edges
  - Run beilinson_auditor.py on all modified files
  - Build both volumes: make fast, cd ~/chiral-bar-cobar-vol2 && make
  - Run tests: make test, make test-full
**Dependencies:** ALL previous tasks.

### Task 5.5: Scope narrowing propagation check
**Files:** All modified files in both volumes
**What to do:**
  - Grep both volumes for "standard examples" -> verify scope
  - Grep for "12 equivalent" / "12/12" -> verify Koszulness count
  - Grep for "self-dual" near Virasoro -> verify qualification
  - Grep for kappa formulas -> verify family-specific (AP1)
  - Run make test to verify all compute tests pass
**Dependencies:** ALL previous tasks.

---

## TIMELINE ESTIMATE

Not providing time estimates per CLAUDE.md instructions. But the dependency
structure implies:

Wave 1 must complete before Wave 2 can start.
Wave 2 must complete before Wave 3 can start.
Waves 3 and 4 can partially overlap.
Wave 5 must come last.

Within each wave, all tasks are parallelizable.

---

## SUCCESS CRITERIA

The rewrite is complete when:

1. Vol I builds clean (0 undefined refs, 0 undefined citations)
2. Vol II builds clean
3. All compute tests pass (22,000+)
4. The center theorem appears in Vol I Chapter 8 with full proof
5. The introduction tells the five-stratum story
6. Every "why 2d+1" discussion uses the center theorem
7. Every main theorem is connected to the modular twisting morphism
8. The staircase of examples is a standalone chapter
9. Cross-volume bridges are harmonized
10. Concordance reflects the open-sector architecture
11. No claim tagged ProvedHere that is actually Conditional (AP4)
12. No scope inflation (AP7): every universal claim is verified
