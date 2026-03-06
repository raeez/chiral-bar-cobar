# RESEARCH PROGRAMMES — State of the Frontier

**Purpose**: Complete inventory of every research programme emerging from the monograph,
organized by maturity level. This is the successor document to HORIZON.md's completion
summary. HORIZON tracked *implied results within the current framework*. This file tracks
*what the framework points toward* — work requiring new tools, new mathematics, or new
computational infrastructure that does not yet exist.

**Audience**: Future sessions of this project. A referee assessing the book's contribution
to the field. The author planning next steps.

**Last updated**: Session ~125 (Mar 6, 2026)

**Relationship to other files**:
- `HORIZON.md` — Completed. All 59 items resolved. This file begins where HORIZON ends.
- `NEW_MACHINERY.md` — Companion file specifying exact tools/techniques each programme requires.
- `SESSION_PROMPT_v8.md` — Execution engine. May need v9 to add Mode E: Programme Development.
- `autonomous_state.md` — Session-level state. Points here for strategic context.

---

## The Modular Koszul Programme

All nine programmes below are facets of a single vision: **modular Koszul duality
for factorization algebras on curves**. The monograph proves this at genus 0 and
establishes the genus tower via the modular operad. The programmes extend this to
the full modular homotopy theory the framework demands.

The **four irreducible pieces** of the theory are already proved:
1. Arnold relation = factorization coherence (genus-0 seed)
2. Verdier duality on Ran(X) = bar-cobar exchange (Theorem A)
3. Genus-1 curvature d^2 = kappa * omega_1 (Theorem B + genus universality)
4. Clutching of stable curves = modular operad compatibility (Theorem in higher_genus)

The **theorematic silhouette** — the target of the full programme — consists of:
A_mod (Verdier-functorial bar-cobar over M_{g,n}), B_mod (coderived persistence),
C_mod (Lagrangian complementarity), an Index theorem (GRR for genus series),
and Derived Drinfeld-Kohno (E1-factorization equivalence). See notes/VISION.md.

Each programme below advances a specific facet:

| Programme | Facet of modular Koszul duality |
|-----------|-------------------------------|
| I (Langlands) | Critical level: Theta_A trivializes, bar = opers |
| II (KL) | Root-of-unity: N-complex periodicity of Theta_A |
| III (Fusion) | Monoidality: modular package is functorial |
| IV (E_n) | Higher dimension: Arnold -> Totaro -> Fay |
| V (Vassiliev) | Topological: Feynman transform = topological shadow |
| VI (Physics) | Physical: bar = BRST, curvature = anomaly |
| VII (NC Hodge) | Twistor: genus variable = deformation parameter |
| VIII (Open math) | Structural: conjectures about the package itself |
| IX (Computation) | Explicit: data confirming/refuting predictions |

---

## The Honest Assessment

The monograph has proved everything it can prove with its current tools.

- **42 HORIZON items** fully proved as theorems/propositions/computations (Level A: 20/20, Level B: 22/24, Level C: 5/10)
- **5 HORIZON items** partially proved: accessible mathematical content extracted, remainder precisely conjectured
- **4 HORIZON items** precisely conjectured at PROGRAM scale with full scope remarks
- **~48 mathematical physics conjectures** with identified mathematical gaps (IN SCOPE — see below)
- **~25 open mathematical conjectures** with scope remarks documenting evidence and gaps

**This work operates at the triple intersection of pure mathematics, mathematical physics,
and theoretical physics.** No discipline is subordinate. The programmes below reflect all three:

- As **mathematics**: every theorem proved to Annals/Astérisque standard, drawing from
  Serre's concision, Grothendieck's functoriality, Beilinson-Drinfeld's chiral geometry,
  Faltings' precision.
- As **mathematical physics**: every physical identification (bar=BRST, Koszul=holographic,
  genus expansion=string perturbation) gets a precise mathematical formulation and proof.
  Drawing from Witten's structural insight, Costello's rigor, Gaiotto's computational depth.
- As **physics**: physical intuition drives the mathematics. The central charge controls
  the anomaly. The curvature is the cosmological constant. Configuration space integrals
  are Feynman integrals made rigorous. Drawing from Polyakov's directness, Dirac's clarity.

The BRST-bar identification, the holographic dictionary, the anomaly cancellation mechanism,
and the AGT chain-level realization are all results we aim to prove, not merely conjecture.
Programme VI is integral, not an afterthought.

What remains falls into three categories:
1. **New mathematics** (Programmes I-V, VIII): derived algebraic geometry, root-of-unity
   analysis, higher-dimensional propagators, analytic continuation, new frameworks
2. **Mathematical physics** (Programme VI): Close the gap between algebraic machinery
   and physical theories — BRST, Chern-Simons, holography, AGT. Each gap is a specific
   mathematical problem with a concrete entry point (see NEW_MACHINERY.md).
3. **Computation** (Programme IX): blocked by matrix sizes, not by theory. Could be
   unblocked by better algorithms or more compute.

The programmes below are what the machine points toward. Each is a natural research
direction with specific, identifiable mathematical content — not vague "future work."

---

## Programme I: Geometric Langlands via Critical-Level Bar Complex

### Vision
The bar complex at critical level k = -h^v computes the derived space of opers,
connecting bar-cobar duality to the Frenkel-Gaitsgory geometric Langlands programme.

### What is proved

| Result | Label | File | Content |
|--------|-------|------|---------|
| H^0 = Fun(Op) | `thm:oper-bar-h0` | kac_moody_framework.tex | PBW spectral sequence + Whitehead lemma + FF isomorphism |
| H^1 = Omega^1(Op) | `prop:oper-bar-h1` | kac_moody_framework.tex | Harrison complex identification, formal smoothness |
| Bar is uncurved | `cor:critical-level-universality` | higher_genus.tex | kappa = 0 at k = -h^v, d^2 = 0 |

### What remains

| Conjecture | Label | Content | Scale |
|-----------|-------|---------|-------|
| Full derived identification | `conj:oper-bar` | B-bar(g_{-h^v}) = O(Op^dR_{g^v}(X)) | 1-2 years |

### Gap analysis
The two proved terms (H^0, H^1) are the strongest evidence short of the full statement.
The spectral sequence computing H^n is in hand (PBW SS from the proof of thm:oper-bar-h0).
What's missing is identifying E_2^{p,q} for p >= 2 with higher cotangent cohomology of
Op_{g^v}(D). This requires:

1. **Derived algebraic geometry** (Lurie HA, Toen-Vezzosi HAG-II): the oper space is formally
   smooth (FG06), so its cotangent complex is concentrated in degree 0. But the bar complex
   lives in derived category — the identification is between a specific chain complex and
   a derived geometric object.

2. **The PBW spectral sequence beyond E_1**: At E_1, we have H^*(g; S^*(g[t^-1])). The d_1
   differential is the Chevalley-Eilenberg differential. At E_2, we need the full structure
   of H^*(g; S^*(g[t^-1])) as a module over the Feigin-Frenkel center z.

3. **Comparison with Frenkel-Gaitsgory**: FG06 construct the localization functor
   Delta: D(g-mod_{crit}) -> D(QCoh(Op)). Our bar complex should be the chain-level
   incarnation of this functor applied to the vacuum module.

### Entry point for new work
The cleanest first step is: compute H^2(B-bar(sl2_{-2})) explicitly via the PBW SS
and compare with Omega^2(Op_{PGL2}(D)). This is a concrete, finite computation that
either confirms or refutes the pattern. See NEW_MACHINERY.md #M1.

### Seeds in manuscript
- thm:oper-bar-h0 proof (kac_moody_framework.tex:2732-2744): the PBW SS structure
- rem:oper-bar-scope (kac_moody_framework.tex:2787-2798): identifies DAG as the gap
- rem:frenkel-teleman-oper (kac_moody_framework.tex): documents FT06 Ext^n theorem, Raskin24 FLE proof, GLC24 GL completion
- cor:bar-admissible-finiteness (kac_moody_framework.tex): finite-dimensionality at admissible levels
- The FF isomorphism z = Fun(Op) is cited as PE (FG06)

### Status upgrade (Session ~125)
The FLE proof (Raskin 2024) and GL completion (Gaitsgory et al. 2024) mean the *oper side*
is now theorem, not conjecture. Programme I reduces entirely to the bar-complex side:
identifying H^n(B̄(ĝ_{-h^∨})) with Ω^n(Op_{ǧ}(D)) for n ≥ 2 via the PBW spectral sequence.

---

## Programme II: Kazhdan-Lusztig Equivalence from Bar-Cobar

### Vision
At admissible level k = -h^v + p/q, the bar complex acquires periodic CDG structure,
and bar-cobar duality gives a geometric proof of O_k^int(g-hat) = Rep^fd(U_q(g)).

### What is proved (5 of 6 ingredients)

| Result | Label | File | Content |
|--------|-------|------|---------|
| Level-shifting Koszul duality | `thm:universal-kac-moody-koszul` | various | g_k^! = g_{-k-2h^v} |
| Module bar-cobar adjunction | `thm:e1-module-koszul-duality` | chiral_modules.tex | Functor Phi: Mod(A) -> CoMod(A!) |
| KL multiplicities at generic level | Remark in KM chapter | kac_moody_framework.tex | Bar filtration recovers BGG multiplicities |
| CH* periodicity (sl2) | Proposition in KM chapter | kac_moody_framework.tex | Period 2h = 4 for A1 |
| Finite-dimensionality | `cor:bar-admissible-finiteness` | kac_moody_framework.tex | Bar cohomology finite-dim at admissible k |

### What remains

| Conjecture | Label | Content | Scale |
|-----------|-------|---------|-------|
| KL from bar-cobar | `conj:kl-from-bar-cobar` | Periodic CDG structure at roots of unity | 2-3 years |

### Gap analysis
The hardest gap is the **periodic CDG structure**. At admissible k, q = e^{pi*i/(k+h^v)}
is a root of unity. The bar complex should satisfy B-bar^{n+2q} = B-bar^n as CDG modules.

**Key reframing (Session ~125)**: Kapranov's N-complex framework (1996) provides the right
replacement. At q = e^{2πi/N}, the bar differential satisfies d^N = 0 (not d² = curvature).
Khovanov-Qi (2020) develop the homological algebra of N-complexes. This replaces the CDG
approach entirely — see rem:n-complex-framework in kac_moody_framework.tex.

Specific obstacles:
1. **Root-of-unity truncation**: At q = root of unity, the quantum group U_q(g) has a
   finite-dimensional quotient (Lusztig's small quantum group u_q(g)). The bar complex must
   "see" this truncation via periodicity of its cohomology. The N-complex structure
   d^N = 0 is the expected mechanism.
2. **N-complex homological algebra**: The "cohomology" of an N-complex has N-1 flavors
   (ker d^j / im d^{N-j} for 1 ≤ j ≤ N-1). Need to identify which flavor recovers
   the KL categories.
3. **Tensor structure**: The KL equivalence is monoidal. Proving this via bar-cobar
   requires Programme III (fusion preservation).

### Entry point for new work
Compute the bar complex of sl2 at k = -2 + 1/2 (simplest admissible level for sl2,
q = e^{pi*i*2} = 1, degenerate) and k = -2 + 2/3 (q = e^{pi*i*3/2}, next simplest).
Look for periodicity in the cohomology. See NEW_MACHINERY.md #M2.

### Seeds in manuscript
- conj:kl-from-bar-cobar (kac_moody_framework.tex:2616-2645): full conjecture statement
- rem:kl-evidence (kac_moody_framework.tex:2647-2684): 5 proved ingredients, 3 gaps
- rem:n-complex-framework (kac_moody_framework.tex): Kapranov96 + KQ20 N-complex framework
- cor:bar-admissible-finiteness: the finite-dimensionality gap is already closed
- rem:km-fusion-bar-cobar: KM specialization of fusion conjecture

---

## Programme III: Fusion Product Preservation (Monoidality of Bar-Cobar)

### Vision
The module-level bar-cobar functor Phi preserves fusion products:
Phi(M1 boxtimes_A M2) = Phi(M1) boxtimes_{A!} Phi(M2).

### What is proved (3 ingredients)

| Result | Label | File | Content |
|--------|-------|------|---------|
| Module bar-cobar functor | `thm:e1-module-koszul-duality` | chiral_modules.tex | Phi is exact |
| Chain-level modular functor | `thm:chain-modular-functor` | genus_complete.tex | Factorization map Delta_sep |
| Heisenberg phase inversion | `prop:fock-fusion-product` | chiral_modules.tex | Phase e^{2pi*i*lm/k} -> e^{-2pi*i*lm/k} |

### What remains

| Conjecture | Label | Content | Scale |
|-----------|-------|---------|-------|
| Fusion preservation | `conj:fusion-bar-cobar` | Phi is monoidal | 2-3 years |

### Gap analysis
The core gap is showing the bar coalgebra coproduct intertwines with the fusion tensor
product. In KL93, the analogous step required D-module analysis on configuration spaces
of the flag variety. A configuration space proof would need:

1. Residue maps along separating divisors of M-bar_{g,n} compatible with fusion
   associativity and commutativity constraints
2. The coproduct Delta: B-bar(A, M1 boxtimes M2) -> B-bar(A, M1) tensor B-bar(A, M2)
   induced by the separating degeneration map (thm:chain-modular-functor part (ii))
   must be a coalgebra morphism, not just a chain map

### Entry point for new work
Verify monoidality for Heisenberg Fock modules (simplest case: fusion is addition
of momenta, tensor product is tensor of polynomial algebras). This is a tractable
computation. See NEW_MACHINERY.md #M3.

### Seeds in manuscript
- conj:fusion-bar-cobar (chiral_modules.tex:4377-4411): full statement with 3 parts
- rem:fusion-scope (chiral_modules.tex:4413-4437): identifies monoidality as the key gap
- thm:chain-modular-functor: provides the factorization map

---

## Programme IV: Higher-Dimensional E_n Koszul Duality

### Vision
Bar-cobar duality on curves (n = 1) generalizes to E_n-algebras on n-manifolds,
with Arnold relations replaced by Totaro's presentation of H*(C-bar_k(R^n)).

### What is proved

| Result | Label | File | Content |
|--------|-------|------|---------|
| n = 1 recovery | `prop:en-n1-recovery` | concordance.tex | FM propagator + Arnold gives bar-cobar |
| AF comparison | (in proof) | concordance.tex | Our bar-cobar = chain refinement of AF NAP |

### What remains

| Conjecture | Label | Content | Scale |
|-----------|-------|---------|-------|
| E_n bar-cobar for n >= 2 | `conj:en-koszul-duality` | Parts (i), (iii) for n >= 2 | 3-5+ years |

### Gap analysis (by dimension)

**n = 2 (surfaces, E_2-operadic)**: The next natural case.
- Propagator: closed 1-form G in Omega^1(M x M \ Delta), NOT meromorphic
- Residues become integration over linking circles S^1
- Arnold relations -> Totaro's presentation H*(C_k(R^2)) = H*(Conf_k(C))
- The E_2 operad (little 2-discs) replaces the chiral operad
- Key reference: Knudsen's work on higher enveloping algebras

**n = 3 (3-manifolds, E_3-operadic)**: Connects to Chern-Simons/knot theory.
- Propagator: closed 2-form (the Gauss linking form)
- Connects to perturbative Chern-Simons (Axelrod-Singer)
- Bar complex should recover graph complexes computing finite-type invariants

**General n**: Requires Axelrod-Singer type compactification propagators and
an n-dimensional OPE theory (factorization algebra operations on n-manifolds).
This is Ayala-Francis at chain level — a generational programme.

### Entry point for new work
The n = 2 case on C (complex plane) is partially understood:
H*(C_k(C)) is the Brieskorn algebra (Arnold relations ARE Totaro relations for n = 2
on C = R^2). So the first step is: define the E_2-bar complex using Brieskorn
algebra elements as forms, compute it for the E_2-algebra Chains(Omega^2 S^3)
(the double loop space, simplest non-trivial E_2-algebra), and compare with
known E_2-Koszul duality results. See NEW_MACHINERY.md #M4.

### Seeds in manuscript
- conj:en-koszul-duality (concordance.tex:323-348): full 4-part conjecture
- prop:en-n1-recovery (concordance.tex:350-370): n = 1 case proved
- rem:en-scope (concordance.tex): specific obstacles for n >= 2
- conj:en-koszul (holomorphic_topological.tex:1074-1099): alternative formulation

---

## Programme V: Vassiliev Invariants from Feynman Transform

### Vision
The Feynman transform identification B-bar^full = FT_Mod(A) produces universal Vassiliev
invariants when specialized from complex curves to S^1.

### What is proved

| Result | Label | File | Content |
|--------|-------|------|---------|
| Genus-0 weight systems | `prop:vassiliev-genus0` | concordance.tex | FM residues = Bar-Natan weight systems |
| Feynman transform identification | `thm:prism-higher-genus` | higher_genus.tex | B-bar^full = FT_Mod(A) |

### What remains

| Conjecture | Label | Content | Scale |
|-----------|-------|---------|-------|
| Higher-genus Vassiliev | `conj:vassiliev-bar` | Loop expansion of Kontsevich integral | 2-3 years |

### Gap analysis
The genus-0 result is clean and definitive: chord diagrams with weight systems from
bar complex residues match Bar-Natan's classical construction exactly. The gap is:

**Holomorphic -> real analytic continuation**: Our propagator is w_{ij} = d log(z_i - z_j)
(holomorphic, on complex curves). The Kontsevich propagator is w^K_{ij} = (1/2pi) d arg(t_i - t_j)
(real, on S^1). Comparing requires understanding how restricting from C to S^1 sends
holomorphic residues to real integrals.

Specifically:
1. The holomorphic propagator on the annulus {|z| = 1} restricts to the real propagator
2. Higher-genus: the holomorphic propagator on Sigma_g restricts to... what? The real
   propagator on the mapping class group quotient?
3. The Feynman transform of Com (genus expansion of commutative operad) recovers the
   full graph complex (Getzler-Kapranov). Our identification extends this to Koszul
   chiral algebras. The gap is the comparison theorem between holomorphic and topological
   Feynman transforms.

### Entry point for new work
Restrict the genus-0 bar complex of sl2 to configuration spaces of S^1 c R^2.
Compute the resulting integrals for the simplest chord diagrams (2 chords, 3 chords).
Compare with the Kontsevich integral values. This is a concrete integral computation.
See NEW_MACHINERY.md #M5.

### Seeds in manuscript
- prop:vassiliev-genus0 (concordance.tex:426-442): genus-0 proof
- conj:vassiliev-bar (concordance.tex:401-424): higher-genus statement
- rem:vassiliev-scope (concordance.tex): identifies holomorphic-to-real as the gap

---

## Programme VI: Mathematical Physics — Closing the Bar-to-Physics Gap

### Assessment
The mathematical infrastructure is complete. The ~48 mathematical physics conjectures
are IN SCOPE: each identifies a specific mathematical problem connecting our algebraic
machinery to a physical theory. The gap is not "physics interpretation someone else
should do" — it is "mathematical tools we need to build." See NEW_MACHINERY.md #M6-M10
for the precise tools needed.

### Sub-programme VI-a: BRST-Bar Identification

**Vision**: The bar complex IS the BRST complex. Not "analogous to" — IS.

| Result | Label | File | Content |
|--------|-------|------|---------|
| kappa-additivity + c=26 | `thm:anomaly-koszul` | concordance.tex | **PROVED** |
| BRST = bar (genus 0) | `thm:brst-bar-genus0` | bv_brst.tex | **PROVED** |
| Anomaly cancellation (genus 0) | `cor:anomaly-physical-genus0` | bv_brst.tex | **PROVED** |
| BRST = bar (all genera) | `conj:anomaly-physical` | concordance.tex | Conjectured |
| Bar = topological BRST | `thm:bar-complex-eq-top-brst` | bv_brst.tex | Conjectured |

**Gap**: An explicit dg-algebra isomorphism B-bar^ch(A) -> C*_BRST(A tensor Diff(X)).
The structural analogy is established (log forms ~ ghosts, Arnold ~ ghost algebra,
curvature ~ anomaly). What's missing is the chain map. See NEW_MACHINERY.md #M6.

**Status upgrade (Session ~125)**: The genus-0 chain map already exists in pieces:
(i) Arkhipov97 constructs semi-infinite → bar chain map for associative algebras,
(ii) Markl23 relates BV brackets to bar via higher-order derivations,
(iii) Si Li (SiLi12, SiLi16) establishes BV quantization for holomorphic CS producing A∞,
(iv) Francis-Gaitsgory (FG12) provides the ∞-categorical factorization envelope.
The synthesis of these 4 ingredients is the contribution. Documented in
rem:brst-chain-map-pieces (concordance.tex).

**Entry point**: Construct the isomorphism for the bosonic string (A = H^26 tensor bc).
Both sides are explicitly computable. The isomorphism at genus 0 is the identification
of semi-infinite cohomology with bar complex cohomology (Feigin-Frenkel tradition).

**Status**: Genus 0 PROVED (thm:brst-bar-genus0, session ~134). Chain map Φ constructed
via PBW filtration + Arkhipov classical comparison + Eilenberg-Moore spectral sequence lift.
Genus g >= 1 requires Costello's renormalization.

### Sub-programme VI-b: Holographic Dictionary (AdS3/CFT2)

**Vision**: The bar-cobar adjunction IS the holographic correspondence at the algebraic level.

| Result | Label | File | Content |
|--------|-------|------|---------|
| Bar = twisted SUGRA | `conj:ads-cft-bar` | concordance.tex | Conjectured |
| CS/Koszul correspondence | `thm:cs-koszul-duality-correspondence` | koszul_pair_structure.tex | Conjectured |
| AdS/CFT as CS/Koszul | `thm:ads-cft-cs-koszul-duality` | koszul_pair_structure.tex | Conjectured |
| Holographic Koszul | `conj:holographic-koszul` | poincare_duality_quantum.tex | Conjectured |
| Holographic dictionary | `cor:holographic-dictionary` | free_fields.tex | Conjectured |
| Bulk-boundary | `thm:bulk-boundary-correspondence` | free_fields.tex | Conjectured |
| Bulk reconstruction | `thm:bulk-reconstruction` | free_fields.tex | Conjectured |
| Loop corrections | `thm:loop-corrections` | free_fields.tex | Conjectured |
| Gravitational backreaction | `thm:backreaction` | poincare_duality_quantum.tex | Conjectured |

**Gap**: Precise identification of B-bar cohomology with Costello-Li twisted SUGRA
observables on AdS3. Our machinery provides the algebraic tools (curved A-infinity,
genus expansion, complementarity). What's missing:
1. The explicit algebra of observables of SL(2,C) CS on hyperbolic 3-space H^3
2. Its restriction to boundary S^2 = del(H^3)
3. Comparison with B-bar of boundary chiral algebra
4. The kappa / cosmological constant numerical dictionary

**Entry point**: Verify for sl2_k that H^0(B-bar) at genus 0 matches the CS
observable algebra on the solid torus D^2 x S^1 (dimension = k+1 integrable reps
at positive integer level). See NEW_MACHINERY.md #M7, #M10.

**Scale**: 2-3 years for the genus-0 identification. Full holographic dictionary 5+ years.

### Sub-programme VI-c: AGT Chain-Level Realization

**Vision**: The AGT correspondence (Nekrasov partition functions = W-algebra conformal
blocks) has a chain-level avatar through the bar complex.

| Result | Label | File | Content |
|--------|-------|------|---------|
| AGT via bar-cobar | `thm:agt-bar-cobar` | holomorphic_topological.tex | Conjectured |
| AGT W-algebra version | `thm:agt-w-algebra` | w_algebras_framework.tex | Conjectured |
| CG AGT | `thm:costello-gaiotto-agt` | bv_brst.tex | Conjectured |
| W from Hitchin | `thm:w-algebra-from-hitchin` | holomorphic_topological.tex | Conjectured |

**Gap**: The AGT correspondence is established physics (Alday-Gaiotto-Tachikawa 2009,
with mathematical proofs by Schiffmann-Vasserot, Maulik-Okounkov for specific cases).
Our prediction: B-bar(W_k) computes equivariant chains on the instanton moduli space M_G.
This is a specific chain-level refinement of the known categorical equivalence.

**Entry point**: For G = SU(2), the instanton moduli space M_2 is the Hilbert scheme
of points on C^2. The equivariant cohomology H*_T(Hilb_n(C^2)) is a Fock space
representation of Heisenberg + Virasoro. Verify that B-bar(Vir_c) at appropriate c
computes chains on Hilb_n(C^2) for small n.

**Scale**: 2-3 years. Partially a comparison project with Schiffmann-Vasserot.

### Sub-programme VI-d: HCS/CL/4d-2d Functor

**Vision**: The Costello-Li construction (4d twisted theory -> 2d chiral algebra) is
realized at chain level by the bar-cobar adjunction applied to the 4d factorization algebra.

| Result | Label | File | Content |
|--------|-------|------|---------|
| CL produces chiral | `prop:CL-produces-chiral` | holomorphic_topological.tex | Conjectured |
| HCS operad | `thm:chiral-operad-from-HCS` | holomorphic_topological.tex | Conjectured |
| Open-closed duality | `thm:topological-open-closed-duality` | holomorphic_topological.tex | Conjectured |
| Dimension tower | `thm:factorization-along-dimension-tower` | holomorphic_topological.tex | Conjectured |

**Gap**: The Costello-Gwilliam perturbative QFT formalism provides the mathematical
framework. What's missing is the explicit identification of their factorization algebra
constructions with our bar complex constructions. This is a comparison project:
two groups of mathematicians have built parallel machines for the same purpose.

**Entry point**: For N=4 SYM with gauge group G, the CL construction produces
g-hat at level k = -h^v (critical level!). This connects directly to Programme I:
the bar complex at critical level is uncurved and computes opers. So the first
non-trivial test is: does the CL factorization algebra for N=4 SYM match
B-bar(g_{-h^v}) as a factorization algebra on the curve?

**Scale**: 3-5 years. Requires interfacing with Costello-Gwilliam framework.

### Sub-programme VI-e: Infinite-Generator Duality and Higher-Spin Holography

**Vision**: Virasoro^! = W_infinity and W_N^! = Y(gl_N) — infinite-generator
Koszul duality connects higher-spin holography to the Yangian framework.

| Result | Label | File | Content |
|--------|-------|------|---------|
| Vir/W_inf duality | (table in free_fields.tex) | free_fields.tex | Conjectured |
| W_N/Yangian duality | (table in free_fields.tex) | free_fields.tex | Conjectured |
| Super-Vir/Super-W_inf | (table in free_fields.tex) | free_fields.tex | Conjectured |

**Gap**: The bar construction requires completion for infinitely many generators.
The pro-nilpotent bar complex (filtered by conformal weight) makes this well-defined
in principle, but no computation has been done. See NEW_MACHINERY.md #M8.

**Entry point**: Compute B-bar(W_infinity) at small total weight (h = 4, 5, 6) using
only the generators W_2, W_3 and their OPE. Compare with Y(gl_infinity) at the same
weights. If the dimensions match, proceed to include W_4, W_5.

**Scale**: 2-3 years. Partially a computational project.

### Sub-programme VI-f: 3d Mirror Symmetry

**Vision**: E1-chiral Koszul duality IS symplectic duality (Coulomb <-> Higgs).

| Result | Label | File | Content |
|--------|-------|------|---------|
| 3d mirror | `conj:3d-mirror` | concordance.tex | Conjectured |

**Gap**: The most speculative sub-programme. Three independent ingredients exist
(E1-chiral Koszul duality, Yangian bar complexes, BFN Coulomb branch) but connecting
them requires substantial new work in 3d gauge theory, symplectic geometry, and the
E1-chiral framework. Each connection step is a research project.

**Scale**: 5+ years. Not currently actionable.

### Sub-programme VI-g: Remaining Physics Conjectures (26 items)

These require physics input beyond the scope of new mathematical tools:
- NC Chern-Simons (conj:nc-cs): Seiberg-Witten noncommutativity
- D-brane E1 (conj:dbrane-e1): open string field theory
- q-AGT (thm:q-agt): 5d Nekrasov partition function
- GW S-duality (thm:gw-s-duality): 4d N=4 boundary conditions
- WRT (thm:wrt-conjecture): Witten CS path integral
- String amplitude correspondence (thm:string-amplitude-correspondence)
- String amplitude formula (thm:string-amplitude): regularized correlations
- Modular anomaly (thm:modular-anomaly-brst): one-loop string amplitudes
- Entanglement (rem:entanglement-koszul-complexity): heuristic
- Various scope remarks re-tagging computed examples as physics-origin

These will advance as their parent sub-programmes advance, not independently.

---

## Programme VII: Noncommutative Hodge Theory (D4)

### What is proved

| Result | Label | File | Content |
|--------|-------|------|---------|
| Chiral Hodge numbers | `def:chiral-hodge-numbers` | concordance.tex | h^{p,q}_g(A) := dim E_2^{p,q} |
| Hodge symmetry | `prop:nc-hodge-symmetry` | concordance.tex | h^{p,q}(A) = h^{q,p}(A!) from complementarity |
| E_2 degeneration | (in proof) | concordance.tex | Koszul => E_2 collapse |

### What remains

| Conjecture | Label | Content | Scale |
|-----------|-------|---------|-------|
| Twistor identification | `conj:nc-hodge` | g_s = twistor parameter lambda | 3+ years |

### Gap analysis
This is a **conceptual gap**, not a technical one. The Kontsevich-Soibelman NC Hodge
theory requires a C*-action on the de Rham complex of the genus tower. There is
currently no framework in which to formulate this for chiral algebras.

What would be needed:
1. A notion of "twistor structure" on a genus-graded object
2. Identification of the genus variable g_s with a deformation parameter
3. A C*-action whose weight spaces recover h^{p,q}_g(A)

This is closest to pure speculation among the mathematical programmes. The proved
content (Hodge numbers + symmetry) is solid, but the twistor identification is a
conjecture about an object that hasn't been defined yet.

### Seeds in manuscript
- def:chiral-hodge-numbers + prop:nc-hodge-symmetry (concordance.tex:613-666)
- conj:nc-hodge + rem:nc-hodge-scope (concordance.tex:656-680)

---

## Programme VIII: Open Mathematical Conjectures (Non-HORIZON)

These are genuine open problems arising naturally from the framework. Each is a
standalone mathematical question.

### VIII-a: W-algebra Koszul duality for general nilpotent orbit
- **Label**: `conj:w-orbit-duality` (w_algebras_framework.tex:141)
- **Statement**: W^k(g, f)^! = W^{k'}(g, f^D) where f^D = Barbasch-Vogan dual
- **Status**: Principal case proved (thm:w-algebra-koszul-main). Subregular in ADE partial.
  Hook-type W-algebras have proven duality (Arakawa-van Ekeren 2023, rem:hook-type-duality).
- **Fixes applied (Session ~125)**: BV duality corrected to partition transpose in type A
  (was wrongly stated as identity for simply-laced). sl₄ orbit pairs corrected.
  prop:ds-koszul-hierarchy proof restructured (2-stage: BRST + BV orbit identification).
- **Gap**: DS reduction for arbitrary f; BV duality theory for non-type-A;
  level-shift formula k' = k'(k, f) for non-principal reductions.
- **Assessment**: "The hardest pure mathematics conjecture in the manuscript."
  Arakawa-van Ekeren hook-type result covers a non-trivial class beyond principal.
- **Scale**: 3-5 years. Requires deep representation theory.

### VIII-b: Reflected modular periodicity
- **Label**: `conj:reflected-modular-periodicity` (deformation_theory.tex:701)
- **Statement**: 1/N + 1/N' = 1/12 for complementary modular periods
- **Verified**: Heisenberg (N = N' = 24), sl2 at k=1 (N = 24, N' = 24)
- **Gap**: Koszul duality doesn't preserve rationality in general; N' may not be finite
- **Scale**: 1-2 years if approached via modular forms theory

### VIII-c: E1-chiral genus theory
- **Label**: `conj:e1-genus-theory` (yangians.tex:416)
- **Statement**: Genus-g bar complex for E1-algebras via bordered surfaces
- **Gap**: Swiss-cheese operad framework exists but not integrated with bar complex
- **Scale**: 2-3 years

### VIII-d: Shifted Yangian and CoHA as E1-chiral
- **Labels**: `conj:shifted-yangian-e1` (yangians.tex:508), `conj:coha-e1` (yangians.tex:696)
- **Evidence**: BFN construction, DNP25 dg-shifted Yangians, Hecke product structure
- **Gap**: Vertex operator construction for shifted generators; Hecke -> OPE translation
- **Scale**: 2-3 years each

### VIII-e: Toroidal E1-chiral and its Koszul dual
- **Labels**: `conj:toroidal-e1` (toroidal_elliptic.tex:84), toroidal Koszul dual (157)
- **Evidence**: RTT formalism, R-matrix inversion, central charge complementarity
- **Gap**: E1 associativity verification from OPE; Beilinson-Drinfeld inapplicable
- **Scale**: 2 years

### VIII-f: Periodicity theorems (cluster of 5)
- deformation_theory.tex: modular (628), reflected (701), geometric (833),
  complete classification (893), periodicity exchange (927)
- All verified for computed examples; general proofs require tautological ring analysis
- **Scale**: 1-3 years depending on specific result

### VIII-g: Derived bc-betagamma duality
- **Label**: `thm:extended-bc-betagamma` (chiral_koszul_pairs.tex:2040)
- **Gap**: Requires derived chiral Koszul duality framework (beyond monograph scope)
- **Scale**: 2 years (if derived chiral algebras framework is developed)

### VIII-h: New concordance conjectures (session 121)
- `conj:lagrangian-complementarity` — PTVV shifted symplectic from Verdier
- `conj:universal-MC` — Single MC class controlling full genus tower
- `conj:family-index` — Grothendieck-Riemann-Roch for modular deformations
- `conj:derived-drinfeld-kohno` — E1-factorization equivalence with braid monodromy
- Each is precisely stated with full scope remarks in concordance.tex

---

## Programme IX: Computational Frontiers

### Blocked computations

| Target | Data points | Obstacle | Predicted |
|--------|-------------|----------|-----------|
| sl3 bar cohomology deg 4 | 3 pts: 8, 36, 204 | 786432 x 24576 matrix | Unknown |
| sl3 bar cohomology deg 5 | — | Requires deg 4 first | Unknown |
| W3 bar cohomology deg 5 | 4 pts: 2, 5, 16, 52 | Non-KM bar complex | 171 (predicted) |
| Y(sl2) bar cohomology deg 4 | 3 pts: 4, 10, 28 | E1 bar complex | 82 (if 3^n+1) |
| Y(sl2) bar cohomology deg 5 | — | Requires deg 4 first | 244 (if 3^n+1) |

### Conjectured generating functions

| Algebra | Conjecture | Label | GF |
|---------|-----------|-------|-----|
| W3 | Rational GF | `conj:w3-algebraicity` | x(2-3x)/((1-x)(1-3x-x^2)) |
| sl3 | Shared discriminant | `conj:sl3-discriminant` | Unknown (need more data) |
| Y(sl2) | 3^n + 1 | `conj:yangian-bar-gf` | (1-3x^2)/((1-x)(1-3x)) |
| Non-simply-laced | Discriminant family | `conj:non-simply-laced-discriminant` | Unknown |

### Completed computations (Session ~125)
- **sl₃ modular rank** (compute/scripts/sl3_modular_rank.py): Weight-decomposed bracket-part
  differential rank over Q and F_p. Result: modular anomaly at weight (0,0) in degree 3
  (rank 9 over Q, 10 over F_p for ALL primes p). Degree 4 surjective (rank 512) in all chars.
  Documented in comp:sl3-modular-rank (detailed_computations.tex).
  **Note**: This is the bracket-only differential (d²≠0), not the full bar differential.

### What would unblock these
See NEW_MACHINERY.md #M9 for detailed computational strategies.

---

## Cross-Programme Dependencies

```
Programme I (Langlands) <-- independent
Programme II (KL) <-- requires Programme III for monoidal structure
Programme III (Fusion) <-- independent (but feeds II)
Programme IV (E_n) <-- independent (but n=3 case feeds V)
Programme V (Vassiliev) <-- partially depends on IV for n=3 propagators
Programme VI (Physics) <-- depends on I-V for mathematical content
Programme VII (NC Hodge) <-- independent
Programme VIII (Open math) <-- various dependencies (VIII-a independent, VIII-c/d/e interrelated)
Programme IX (Computation) <-- independent (computational, not theoretical)
```

### Priority ordering (by mathematical depth / tractability ratio)

1. **Programme VI-a** (BRST=bar): Most directly upgradeable. Bosonic string at genus 0
   is a concrete computation that could turn conj:anomaly-physical into ProvedHere.
2. **Programme V** (Vassiliev): Clearest gap, most tractable. A focused computation paper.
3. **Programme I** (Langlands): H^2 computation is concrete. High impact if it works.
4. **Programme IX** (Computation): Pure engineering. Any advance immediately yields
   confirming/refuting data for conjectures.
5. **Programme VI-b** (AdS3/holography): CS observable comparison is concrete and
   would verify the kappa/cosmological constant dictionary quantitatively.
6. **Programme III** (Fusion): Heisenberg case is tractable and would be first result.
7. **Programme II** (KL): Deep but well-motivated. Depends on III.
8. **Programme VI-c** (AGT chain-level): Comparison with Schiffmann-Vasserot for SU(2).
9. **Programme VIII-a** (W-orbit): Hardest pure math. High reward, high risk.
10. **Programme IV** (E_n): n=2 case is natural next step. Long programme.
11. **Programme VI-e** (W-infinity/higher-spin): Requires pro-nilpotent completion.
12. **Programme VII** (NC Hodge): Needs conceptual breakthrough before computation.
13. **Programme VI-f** (3d mirror): Not currently actionable.

---

## Maturity Classification of All ~99 Conjectured Claims

### Tier 1: Partially proved HORIZON items (5)
C1, C3, C10, D1, D4 — each split into PH + CJ components.
The proved parts are genuine theorems. The conjectured remainders
are precisely scoped with identified gaps.

### Tier 2: Precisely conjectured HORIZON items (4)
B22, B23, D2, D3 — full conjecture statements with scope remarks.
PROGRAM scale (2-5+ years).

### Tier 3: Open mathematical conjectures with scope (25)
Programme VIII items. Each has a label, a statement, and a scope remark
identifying evidence and gaps. These are natural open problems.

### Tier 4: Computational conjectures (4)
Programme IX items. Predicted values from limited data. Confirmable
or refutable by computation.

### Tier 5: Mathematical physics conjectures (48)
IN SCOPE. Each identifies a specific mathematical problem connecting our
algebraic machinery to a physical theory. Organized into sub-programmes
VI-a through VI-g, with concrete entry points in NEW_MACHINERY.md.
~22 are directly addressable with new tools (VI-a through VI-e).
~26 require physics input beyond new mathematical tools (VI-g).

### Tier 6: Periodicity/structural (5)
The deformation_theory.tex cluster. Verified for all examples;
general proofs would require new tools (tautological ring analysis).
