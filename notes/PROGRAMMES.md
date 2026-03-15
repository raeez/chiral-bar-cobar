# RESEARCH PROGRAMMES — State of the Frontier

**Purpose**: Complete inventory of every research programme emerging from the monograph,
organized by maturity level. This is the successor document to HORIZON.md's completion
summary. HORIZON tracked *implied results within the current framework*. This file tracks
*what the framework points toward* — work requiring new tools, new mathematics, or new
computational infrastructure that does not yet exist.

**Audience**: Future sessions of this project. A referee assessing the book's contribution
to the field. The author planning next steps.

**Governing principle (Dual Imperative)**: Every programme below is driven by
maximalist ambition — the most powerful, general theorems the subject admits.
The discipline of maximal truth-seeking (precise status at every level) is
what makes the ambition credible. Programmes are ordered by dependency, not
difficulty, so the frontier advances honestly.

**Last updated**: Mar 9, 2026

**Relationship to other files**:
- `HORIZON.md` — Completed. All 59 items resolved. This file begins where HORIZON ends.
- `NEW_MACHINERY.md` — Companion file specifying exact tools/techniques each programme requires.
- `SESSION_PROMPT_v8.md` — Execution engine. May need v9 to add Mode E: Programme Development.
- `autonomous_state.md` — Session-level state. Points here for strategic context.

---

## The Modular Koszul Programme

All nine programmes below are facets of a single subject: **modular homotopy theory
for factorization algebras on curves**. The present monograph is Volume I of that
subject: it proves the modular Koszul core, establishes the genus tower on the
theorematic loci, and isolates the remaining homotopy-native packages.

The **four irreducible pieces** of the theory are already proved:
1. Arnold relation = factorization coherence (genus-0 seed)
2. Verdier duality on Ran(X) = bar-cobar exchange (Theorem A)
3. Genus-1 curvature d^2 = kappa * omega_1 (Theorem B + genus universality)
4. Clutching of stable curves = modular operad compatibility (Theorem in higher_genus)

For entry, the mature subject now has two atoms, not one generic
examples layer.  Heisenberg remains the primary commutative/modular
frame.  The Yangian evaluation-locus Drinfeld-Kohno square is the
secondary braided/factorization atom: it isolates ordered
configurations, braid monodromy, and reversal of braiding without
pretending that the full category-`O` / dg-shifted comparison is
already proved.

The **theorematic silhouette** — the target of the full programme — consists of:
A_mod (Verdier-functorial bar-cobar over M_{g,n}), B_mod (coderived persistence),
C_mod (Lagrangian complementarity), an Index theorem (GRR for genus series),
and Derived Drinfeld-Kohno (E1-factorization equivalence). See notes/VISION.md.

Status discipline for the frontier:
when Parts I-II exhibit a same-family partner
(for example the Virasoro involution `c <-> 26-c`), that partner should be read as the
proved M/S-level shadow controlling curvature, complementarity, and
semi-infinite growth.  The stronger H-level realization by a completed
infinite-generator dual object (for example `W_\\infty`) remains frontier mathematics and belongs to the
MC4 / infinite-generator programme.

Current frontier dependency order:
1. **Resolved entry theorem**: MC1 is closed for the standard finite-type
   interacting families (affine Kac-Moody, Virasoro, principal finite-type
   `W_N`).
2. **Resolved foundational target**: MC2 is now PROVED
   (`thm:mc2-full-resolution` in `higher_genus.tex`). All three packages
   — cyclic L-infinity graph complex, geometric modular-operadic MC
   framework, tautological-line support — are resolved. The universal
   MC element `Theta_A` exists.
3. **Live frontier**: MC3 and MC4, now interpreted as the full
   factorization-categorical lift and the H-level comparison problem for
   infinite-generator targets after the standard M-level completions.
   MC3 has new DK-1½ result for lattice VOAs (bypassing thick generation).
4. **Physics completion**: MC5, downstream of the previous layers.

Derived Drinfeld-Kohno should be read as a staged ladder, not one
opaque conjectural block:
1. `DK-0`: chain-level evaluation-locus `q \mapsto q^{-1}` /
   `R \mapsto R^{-1}` shadow on the standard evaluation objects;
2. `DK-1`: intrinsic ordered factorization category on the evaluation
   locus;
3. `DK-2`: factorization Kazhdan functor `KZ_fact` on that ordered
   category;
4. `DK-3`: extension beyond evaluation modules via Koszul, generation,
   and monadicity input;
5. `DK-4`: full ordered `E1`-factorization equivalence;
6. `DK-5`: dg-shifted Yangian / line-operator comparison at the
   intended H-level target.

Periodicity is not part of that master-conjecture chain.  It is an
orthogonal weak flank: the lcm/profile shadow and quantum periodicity
inputs are theorematic, while modular bar-cohomology periodicity and
sharp geometric factors remain conjectural.

Each programme below advances a specific facet of that larger subject:

| Programme | Facet of modular homotopy theory |
|-----------|-------------------------------|
| I (Langlands) | Critical level: bar = opers; the proved MC2 hierarchy is expected to degenerate there |
| II (KL) | Root-of-unity: quantum-group / periodic / CDG shadow feeding the modular characteristic hierarchy |
| III (Fusion) | Monoidality: the modular characteristic hierarchy should be functorial |
| IV (E_n) | Higher dimension: Arnold -> Totaro -> Fay |
| V (Vassiliev) | Topological: Feynman transform = topological shadow |
| VI (Physics) | Physical: BRST/bar comparison, curvature = anomaly |
| VII (NC Hodge) | Twistor: genus variable = deformation parameter |
| VIII (Open math) | Structural: conjectures about the hierarchy itself |
| IX (Computation) | Explicit: data testing scalar/spectral laws and the MC3/MC4 frontier |

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
  genus expansion=string perturbation) is routed to a precise mathematical formulation
  with an explicit status tag and dependency order. When the boundary algebraic package
  is already theorematic, the open work is the comparison problem itself; when
  infinite-generator targets are required, their filtered H-level realization sits
  upstream in MC4. Drawing from Witten's structural insight, Costello's rigor,
  Gaiotto's computational depth.
- As **physics**: physical intuition drives the mathematics. The central charge controls
  the anomaly. The curvature is the cosmological constant. Configuration space integrals
  are Feynman integrals made rigorous. Drawing from Polyakov's directness, Dirac's clarity.

Programme VI is therefore organized, not flattened: theorematic boundary algebraic
packages first; then any MC4 target-construction and coefficient-identification step
for infinite-generator objects; only then the downstream MC5 physical dictionary or
comparison. Programme VI is integral, not an afterthought.

The sharpest current boundary is therefore not ``proved versus conjectural'' in
the abstract, but ``proved shadow versus realized object.''  The book now has a
stable proved modular Koszul core; what remains is to upgrade its shadows to the
homotopy-native objects that would constitute modular homotopy theory for
factorization algebras on curves.

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
and bar-cobar duality should give a geometric proof of the
semisimplified Kazhdan--Lusztig target
$\mathcal{O}_k^{\mathrm{int}}(\widehat{\mathfrak{g}})
\simeq \mathcal{C}(U_q(\mathfrak{g}))$.  Any non-semisimple lift to
$\mathrm{Rep}^{\mathrm{fd}}(U_q(\mathfrak{g}))$ or larger
completed/coderived enlargement is a separate outer MC3 problem.

### What is proved (6 of 6 preparatory ingredients)

| Result | Label | File | Content |
|--------|-------|------|---------|
| Level-shifting Koszul duality | `thm:universal-kac-moody-koszul` | various | g_k^! = g_{-k-2h^v} |
| Module bar-cobar adjunction | `thm:e1-module-koszul-duality` | chiral_modules.tex | Functor Phi: Mod(A) -> CoMod(A!) |
| KL multiplicities at generic level | Remark in KM chapter | kac_moody_framework.tex | Bar filtration recovers BGG multiplicities |
| CH* periodicity (sl2) | Proposition in KM chapter | kac_moody_framework.tex | Period 2h = 4 for A1 |
| Finite-dimensionality | `cor:bar-admissible-finiteness` | kac_moody_framework.tex | Bar cohomology finite-dim at admissible k |
| Root-of-unity q-bar certificate | compute KL lane | `compute/lib/kl_ncomplex_sl2.py`, `compute/tests/test_kl_ncomplex_sl2.py` | `d_q^N = 0` computed directly at `N=2,3` and structurally certified at `N=4,5`; reduced degree-2 vanishing split from the genuine `d_q^2 \neq 0` check |

### What remains

| Conjecture | Label | Content | Scale |
|-----------|-------|---------|-------|
| KL semisimplified target from bar-cobar | `conj:kl-periodic-cdg` -> `conj:kl-coderived` -> `conj:kl-braided` | Periodic CDG, coderived lift to the semisimplified target, braided upgrade | 2-3 years |

### Gap analysis
For the semisimplified KL target, the hardest gap is no longer whether a
root-of-unity bar differential exists, but how to interpret the
admissible-level q-bar object categorically. At admissible k,
q = e^{pi*i/(k+h^v)} is a root of unity. The M-level q-bar certificate
is now explicit: for `u_q(sl_2)` the Kapranov differential satisfies
`d_q^N = 0`, computed directly at `N=2,3` and discharged by the
quantum-binomial structural route at `N=4,5` once the reduced bar
spaces are too large to materialize densely; the reduced degree-2
vanishing `d_q^2 = 0` is separated from the genuinely non-classical
check `d_q^2 != 0`, which is directly witnessed at bar degree `>= 3` in
the tractable `N=3` case. The theorematic KL gap is therefore the
passage from this M-level `N`-complex certificate to the periodic or
coderived KL object, and then to the semisimplified target
$\mathcal{C}(U_q(\mathfrak{g}))`.
The first degree-4 admissible `sl_2` packet is now also resolved:
`dim H^{1,2}_2 = dim H^{2,1}_3 = 3` by sparse `q`-bar elimination.
The live KL question is therefore no longer the existence of the
`N`-complex, but the categorical meaning of this first symmetric packet.
The first sparse `N=4` degree-1 window already vanishes in the resolved
channels `H^{3,1}_1 = H^{2,2}_1 = 0`, and the remaining degree-1
channel now vanishes as well: `H^{1,3}_1 = 0`. So the whole first
`N=4` degree-1 packet is zero, and the next discriminant is a
higher-degree `N=4` continuation. The first tractable degree-2 channels
now vanish as well: `H^{3,1}_2 = H^{2,2}_2 = 0`, so the next
discriminant is the unresolved `H^{1,3}_2` channel. The split-form
sparse `d_q^3 : B_5 -> B_2` certificate already gives
`rank(im d_q^3) >= 3903`, hence `dim H^{1,3}_2 <= 66`, and the residual
cokernel is supported only on the left factors `F`, `E`, and `K-1`.
So the live gap is now this residual `66`-dimensional packet, not the
whole `B_5 -> B_2` map. Even the full generator-prefix cube
`{F,E,K-1}^3 x I^2` adds no new residual rank beyond that certificate,
and the later split-form precursor stages with
`ab`, `abc`, or `abcd` in `span{F,E,K-1}` are also quotient-zero. The
surviving first-term sector compresses from `42,718,284` raw tuples to
only `1493` distinct right-product states, and its standalone tensor
span adds just `57` directions beyond the `3903`-rank seed span
(`43` from `F`, `14` from `E`, `0` from `K-1`). So the live KL gap is
now the cancellation/annihilator problem between that first-term
`57`-plane and the remaining nonresidual split terms. The new quotient
comparison shows that the combined non-first split sector already spans
that same `57`-plane, so the next attack is an internal cancellation
operator on a common quotient plane rather than a hunt for extra
directions. That exhaustive compressed verification is now complete:
all `354,668` surviving prefix signatures, covering the full
`42,718,284` raw surviving columns, vanish in the seed quotient. So the
seed rank `3903` is exact and
`dim H^{1,3}_2 = 66`. The live KL question is now no longer a
`B_5 -> B_2` elimination problem, but the categorical meaning of this
exact `66`-dimensional `N=4` packet. That packet already carries a
rigid support fingerprint: it splits as `F⊗48 ⊕ E⊗15 ⊕ (K-1)⊗3`, and
its total root-weight profile is palindromic
`1,4,8,12,16,12,8,4,1` across weights `-4,...,4`. Equivalently, at the
S-level it is an exact unit-step interval staircase with multiplicities
`1,3,4,4,4` on supports `[-4,4],[-3,3],[-2,2],[-1,1],{0}`. The next
shadow comparison should now target this exact fingerprint, not just
the raw dimension. More sharply: this staircase is not the image of the
first admissible `N=3` packet under any exact symmetric convolution
transport at all, because support forces every radius-`R>=2` outer
kernel coefficient to vanish and reduces any exact transport to the
radius-`1` case, while the exact radius-`0` / radius-`1` systems are
already inconsistent for both one flavor and the paired packet.
The first structured non-convolutional finite-window candidate is now
visible too: on `[-4,4]`, the paired `N=3` profile is recovered exactly
from the `N=4` staircase by a Dirichlet discrete Laplacian plus even
sextic potential, while pure multiplication needs degree `8`.

**Key reframing (Session ~125)**: Kapranov's N-complex framework (1996) provides the right
replacement. At q = e^{2πi/N}, the bar differential satisfies d^N = 0 (not d² = curvature).
Khovanov-Qi (2020) develop the homological algebra of N-complexes. This replaces the CDG
approach entirely — see rem:n-complex-framework in kac_moody_framework.tex.

Specific obstacles:
1. **Periodic shadow extraction**: At q = root of unity, the quantum group U_q(g) has a
   finite-dimensional quotient (Lusztig's small quantum group u_q(g)). The q-bar complex now
   certifies `d^N = 0`, and the first admissible `sl_2` packet is
   explicitly `dim H^{1,2}_2 = dim H^{2,1}_3 = 3`; what remains is to
   extract the periodic or coderived shadow seen by the KL target from
   that packet. At the S-level, each flavor is the same sparse
   three-point profile on weights `-3,0,3` with class-support sizes
   `1,6,1`, whereas the first exact `N=4` packet is already the
   `66`-dimensional interval staircase above.
2. **N-complex homological algebra**: The "cohomology" of an N-complex has N-1 flavors
   (ker d^j / im d^{N-j} for 1 ≤ j ≤ N-1). The first admissible `sl_2`
   packet is symmetric rather than single-flavor, so the next step is to
   determine whether one flavor, the paired packet, or some further
   categorical operation on that sparse `N=3` profile recovers the KL
   categories and explains the staircase-rigid `N=4` packet.
3. **Tensor structure**: The KL equivalence is monoidal. Proving this via bar-cobar
   requires Programme III (fusion preservation).

### Entry point for new work
Hold the q-bar certificate fixed and move to the next KL question:
identify the categorical meaning of the first computed `sl_2` packet
`dim H^{1,2}_2 = dim H^{2,1}_3 = 3`, deciding whether one flavor or the
paired packet controls the semisimplified KL target. The immediate task
is no longer to re-prove `d_q^N = 0`, but to detect the
periodic/coderived shadow of this packet and then extend the same
diagnostic beyond the first admissible level. The whole first sparse
`N=4` degree-1 packet now vanishes,
`H^{3,1}_1 = H^{2,2}_1 = H^{1,3}_1 = 0`, so the next compute target is
the first degree-2 packet. Its tractable channels now also vanish,
`H^{3,1}_2 = H^{2,2}_2 = 0`, and the split-form sparse image
certificate already gives `rank(im d_q^3) >= 3903`, hence
`dim H^{1,3}_2 <= 66`. The next compute target is therefore the
residual `66`-dimensional `H^{1,3}_2` packet supported on left factors
`F`, `E`, and `K-1`, rather than the full `B_5 -> B_2` continuation.
The whole generator-prefix cube `{F,E,K-1}^3 x I^2` already lies inside
the existing seed span, so the remaining packet is genuinely beyond the
first generator-level probe. The later split-form precursor stages
`ab`, `abc`, and `abcd` landing in that span are also quotient-zero, so
the only live split term is the first one. That first-term sector now
compresses to `1493` distinct right-product states and its standalone
tensor span adds only `57` directions beyond the `3903`-rank seed span,
so the next compute attack is no longer another raw tuple sweep. The
combined non-first split sector already spans the same `57`-plane, and
the exhaustive compressed verification of the full surviving packet now
shows that every weighted surviving column vanishes in the seed
quotient. Thus the `3903`-rank seed image is exact and
`dim H^{1,3}_2 = 66`. The remaining work is to determine the
periodic/coderived shadow and categorical meaning of this exact
`66`-dimensional packet. The exact packet is already structurally rigid:
`F⊗48 ⊕ E⊗15 ⊕ (K-1)⊗3` with palindromic total root-weight profile
`1,4,8,12,16,12,8,4,1`, equivalently the interval staircase
`[-4,4] + 3[-3,3] + 4[-2,2] + 4[-1,1] + 4{0}` at the S-level. By
contrast, the first exact `N=3` packet is only the sparse three-point
profile `{-3:1, 0:1, 3:1}` in each flavor, so the next categorical test
is to explain that contrast rather than merely match dimensions. The
simple convolutional route is now ruled out exactly: support forces any
exact symmetric transport to the radius-`1` case, but those exact
systems are inconsistent for both the single and paired `N=3` sources.
Signed radius-`4` kernels exist only as window-matching artifacts on
`[-4,4]`; they spill outside the target support and are not genuine
transports. The first surviving structured route is instead the
finite-window operator `aΔ+V_6(w)` on `[-4,4]`, so the next question is
whether that operator is the S-level shadow of a real H/M-level KL
mechanism or only a numerical organizer.
See NEW_MACHINERY.md #M2.

### Seeds in manuscript
- conj:kl-periodic-cdg / conj:kl-coderived / conj:kl-braided
  (kac_moody_framework.tex:2692-2744): staged KL conjecture package
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
The curve-level chiral bar-cobar story has its topological little-disks
shadow at `n = 2`, because a complex curve is a real oriented surface.
Programme IV asks what survives when one leaves the holomorphic
Beilinson--Drinfeld setting and passes to genuine `E_n`-algebras on
real `n`-manifolds, with Arnold relations replaced by Totaro's
presentation of `H^*(C-bar_k(R^n))`.

### What is proved

| Result | Label | File | Content |
|--------|-------|------|---------|
| n = 2 topological recovery | `prop:en-n2-recovery` | concordance.tex | On a complex curve viewed as a real oriented surface, the FM propagator admits the holomorphic representative `d log(z_i-z_j)` and recovers the topological shadow of the chiral bar-cobar adjunction |
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
- prop:en-n2-recovery (concordance.tex:350-370): n = 2 topological recovery proved on a complex curve viewed as a real oriented surface
- rem:en-scope (concordance.tex): specific obstacles for n >= 2
- thm:en-koszul (holomorphic_topological.tex:1358): $E_n$ Koszul duality on $n$-manifolds (ProvedElsewhere)

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

**Vision**: At genus `0` the bar complex is identified with the BRST
complex; the live programme is to lift that comparison to the
all-genera holomorphic/BV setting without flattening the status
boundary.

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

**Vision**: The bar-cobar adjunction should supply the algebraic template for holographic
correspondence.

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
observables on AdS3. The finite-type boundary algebraic package is already theorematic
in the core. What remains is the physical comparison itself, and whenever a higher-spin
or infinite-generator bulk target is required its filtered H-level realization belongs
upstream to MC4 rather than to the holographic dictionary step. Our machinery provides
the algebraic tools (curved A-infinity, genus expansion, complementarity). What's missing:
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
blocks) should admit a chain-level avatar through the bar complex.

| Result | Label | File | Content |
|--------|-------|------|---------|
| AGT via bar-cobar | `thm:agt-bar-cobar` | holomorphic_topological.tex | Conjectured |
| AGT W-algebra version | `thm:agt-w-algebra` | w_algebras_framework.tex | Conjectured |
| CG AGT | `thm:costello-gaiotto-agt` | bv_brst.tex | Conjectured |
| W from Hitchin | `thm:w-algebra-from-hitchin` | holomorphic_topological.tex | Conjectured |

**Gap**: The AGT correspondence is established physics (Alday-Gaiotto-Tachikawa 2009,
with mathematical proofs by Schiffmann-Vasserot, Maulik-Okounkov for specific cases).
Within the repo's actual dependency order, principal finite-type `W_N` already lies in
the proved core, so the AGT comparison is not a substitute for missing finite-type bar
theory. If one asks for filtered `W_\\infty` / Yangian targets or coefficient-level
identifications beyond the finite stages, those are upstream MC4 tasks; the physical or
gauge-theoretic comparison itself is downstream. Our prediction is that, once the needed
targets are in place, B-bar(W_k) computes equivariant chains on the instanton moduli
space M_G. This is a specific chain-level refinement of the known categorical
equivalence.

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

**Vision**: Virasoro^! = W_infinity and W_N^! = Y(gl_N) at the H-level.  The
finite-type principal `W_N` stages already belong to the proved modular Koszul
core; the live problem is the infinite-generator / Yangian comparison beyond
that theorematic M-level package.

| Result | Label | File | Content |
|--------|-------|------|---------|
| Vir/W_inf duality | (table in free_fields.tex) | free_fields.tex | Conjectured |
| W_N/Yangian duality | (table in free_fields.tex) | free_fields.tex | Conjectured |
| Super-Vir/Super-W_inf | (table in free_fields.tex) | free_fields.tex | Conjectured |

**Gap**: The live gap is no longer principal finite-type `W_N`; the
standard-tower completed M-level packages for the principal
`W_\infty` and RTT Yangian towers are already theorematic.  What
remains is the H-level target and exact coefficient-identification
package beyond those standard towers.

On the `W_infinity` side this now means:
construct a principal-stage compatible factorization target, extract
the local coefficients, and prove the stagewise identities
`C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)`.
Those identities are no longer a vague comparison slogan; they are
detected on the finitely many generator-level primary coefficients,
after which translation propagates them to all descendants.

Foundationally, one should not first search for a closed
infinite-generator presentation of `W_\infty^!`.  The standard
principal tower already determines the completed M-level candidate
`\varprojlim_N \bar B(W_N)`.  The open work is to realize a compatible
H-level/factorization target with quotients `W_N`, prove the finite
packet identities on `\mathcal I_N`, and then apply the inverse-limit
comparison theorem.  In other words: the missing step is promotion of
the standard completed bar candidate to an H-level dual object, not a
new completion theorem on the bar side itself.

On the Yangian side the parallel task is:
construct an RTT-adapted filtration on the dg-shifted/factorization
target and prove the stagewise identities
`K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)`.
For the standard type-`A` tower, this is no longer a fresh local
residue computation: the factorization target already carries the
standard normalized residue, and any dg-shifted realization presented by
the same ordered bar seed inherits that local closure. What remains
there is the compact-generator comparison. Beyond that theorematic
standard packet, the Yangian identities are reduced further to vanishing
of the defect family on a faithful subcategory generated by tensor
products of fundamental evaluation modules.

So the open MC4 ledger is now exact:
1. build the filtered H-level targets with the correct finite quotients;
2. prove the named mode identities on those finite quotients; and
3. close the finite-detection steps, namely the Yangian boundary strip
   `\Delta_{a,0}(N)` and the `W_\infty` primary seed set
   `\mathcal{I}_N`.
At the current theorem surface this is no longer an amorphous
comparison problem.  The Yangian strip is detected on generic tensor
powers of the fundamental evaluation module of lengths at most `N+1`,
and with standard twisted-coproduct propagation the higher tensor
lengths become formal once the fundamental `L`-operator is controlled;
the remaining Yangian check is the pairwise auxiliary-space kernel
identity `L_a(u)=R_{0a}(u-a)`.  For the standard type-A RTT tower this
is now theorematically reduced to transport of the standard normalized
residue to the dg-shifted target, equivalently the ordered tensor-line
coefficient `e_1\otimes e_2 \mapsto -\hbar\,e_2\otimes e_1`, followed by
the compact-generator comparison.  On the `W_\infty` side, the first
genuinely new packet beyond the Virasoro block is the explicit stage-3
list of fifteen primary coefficients, but the theorematic `W_3` OPE
already reduces that to three nonzero numbers and twelve forced
vanishings.  Stage `N=4` is now compressed as well: after removing the
exact stress-tensor sector and the theorematic `(3,3)` `W_3` sector,
the residual packet has exactly `29` primary coefficients.  Primaryity
first reduces that residual packet to `7` top-pole coefficients and
`22` forced zeros.  Skew-symmetry then removes the odd self-OPE entry
`(4,4,3,5)`, leaving the exact six-entry stage-`4` packet on
`\mathcal{I}_4` and `23` forced zeros, organized as three explicit
local OPE blocks.  Among those six entries, the only
genuinely mixed higher-spin data are the three coefficients in the
mixed `(3,4)` block.  Within that mixed block, the `W^{(3)}` target
channel is swap-even under reversing the mixed OPE order, while the
`W^{(2)}` and `W^{(4)}` target channels are swap-odd.  On the
principal Drinfeld--Sokolov side, the mixed `W^{(2)}` target then
vanishes by mixed-weight orthogonality plus the Virasoro Ward identity,
while the principal `W^{(4)}`-`W^{(4)}\to T` coefficient is fixed to
`2`.  The live stage-`4` comparison is therefore the exact six-entry
identity packet on `\mathcal{I}_4`,
`\mathsf{C}^{\mathrm{res}}_{s,t;u;m,n}(4)=\mathsf{C}^{\mathrm{DS}}_{s,t;u;m,n}(4)`,
in the channels `(3,3;4;0,2)`, `(4,4;4;0,4)`, `(3,4;3;0,4)`,
`(3,4;4;0,3)`, `(4,4;2;0,6)`, `(3,4;2;0,5)`, split as
`4` residual higher-spin channels plus `2` theorematic
Virasoro-target identities.
From there the promotion `\mathcal{I}_4 \to \mathcal{I}_N` is no
longer a black box: Proposition
`prop:winfty-ds-stage-growth-packet` linearizes it as repeated closure
of the incremental packets `\mathcal{J}_{M+1}`, and Corollary
`cor:winfty-ds-stage-growth-top-parity` reduces those further to the
top-pole/parity packets `\mathcal{J}_{M+1}^{\mathrm{red}}`.
`prop:winfty-stage-growth-virasoro-target-contraction` then gives the
uniform reduced-packet contraction under the normalized residue
package by removing exactly the target-`2` Virasoro channels.  The
first next downstream reduced stage is already explicit, and it should
now be read as a transport problem rather than as a fresh coefficient
block: `cor:winfty-ds-stage5-reduced-packet` identifies
`\mathcal{J}_5^{\mathrm{red}}` as an `11`-entry packet,
`cor:winfty-stage5-residue-eight-channel` and
`cor:winfty-stage5-higher-spin-packet` identify the contracted
`8`-channel higher-spin packet `\mathcal{J}_5^{\mathrm{hs}}`, and
`prop:winfty-stage5-local-attack-order` packages the local order there
as entry packet first, then the target-`5` corridor, then the
remaining transport ladders in targets `5`, `4`, `3`.
`prop:winfty-stage5-higher-spin-subblocks` breaks that packet into the
source-pair ladder `1+3+3+1`, and
`cor:winfty-stage5-entry-transport` isolates the first two-channel
entry packet from the six-channel mixed transport packet.
`prop:winfty-stage5-entry-mixed-self` then resolves that entry packet
into the mixed-entry singleton `(3,4;5;0,2)` and the self-return
singleton `(5,5;4;0,6)`.  `prop:winfty-stage5-higher-spin-target-blocks`
also regroups the packet by target spin, and
`cor:winfty-stage5-target5-corridor` identifies the first local
three-channel strip as the target-`5` corridor
`(3,4;5;0,2)`, `(3,5;5;0,3)`, `(4,5;5;0,4)`.
`prop:winfty-stage5-reduced-tail-singleton` identifies
`(3,4;5;0,2)` as the entire reduced tail input at stage `5`;
`prop:winfty-stage5-tail-mechanism` identifies the exact missing
comparison mechanism there as the `W^{(5)}`-projection in the top pole
of `W^{(3)}(z)W^{(4)}(w)`; and
`cor:winfty-stage5-target5-residual` identifies the residual
continuation after that tail input as the two-channel ladder
`\mathcal{J}_5^{\mathrm{tr},5}`;
`prop:winfty-stage5-target5-transport-mechanism` identifies that
residual continuation as the comparison of the `W^{(5)}`-projection in
`W^{(3)}(z)W^{(5)}(w)` and `W^{(4)}(z)W^{(5)}(w)`;
`prop:winfty-stage5-target5-transport-singletons` then splits that
residual target-`5` continuation into the pole-`3` singleton
`(3,5;5;0,3)` and the pole-`4` singleton `(4,5;5;0,4)`.
`prop:winfty-stage5-visible-w5-normalization` makes the visible
`W^{(5)}` normalization theorematic under the stage-`5` Virasoro
package.  On the visible pairing loci of
`prop:winfty-stage5-target5-pole3-pairing-vanishing` through
`cor:winfty-stage5-tail-cross-target-reduction`, the same target-`5`
staircase becomes partially rigid: the pole-`3` singleton vanishes, the
pole-`4` singleton is tied to the self-return singleton, and the tail
singleton is tied to neighboring target-`4` / target-`3` channels.
`cor:winfty-stage5-target5-corridor-to-tail` then kills the transport
part on the visible `W^{(4)}` / `W^{(5)}` pairing locus, and
`cor:winfty-stage5-target5-no-new-independent-data` shows that on the
full visible `W^{(3)}` / `W^{(4)}` / `W^{(5)}` pairing locus the whole
target-`5` corridor carries no new independent coefficient.
`prop:winfty-stage5-target4-pole5-w4-vanishing`,
`prop:winfty-stage5-target3-pole5-w3-vanishing`, and
`prop:winfty-stage5-transport-cross-target-reduction` then collapse the
remaining target-`4` / target-`3` transport front to one effective
coefficient, and `cor:winfty-stage5-effective-independent-frontier`
shows that on that full visible pairing locus the whole stage-`5`
higher-spin packet carries one effective independent coefficient,
represented by the target-`4` singleton `(3,5;4;0,4)`.
`conj:winfty-stage5-principal-target5-no-new-independent-data` and
`conj:winfty-stage5-principal-residual-front-one-coefficient` then
split the remaining principal-side structural input into the target-`5`
corridor and the residual front;
`conj:winfty-stage5-principal-target5-transport-vanishing` plus
`conj:winfty-stage5-principal-tail-cross-target-reduction` form the
target-`5` staircase, while
`conj:winfty-stage5-principal-residual-front-vanishings` plus
`conj:winfty-stage5-principal-residual-cross-target-reduction` form the
residual-front staircase, and
`prop:winfty-stage5-principal-one-coefficient-factorization` packages
their conjunction as
`conj:winfty-stage5-principal-one-coefficient-normal-form`.
`prop:winfty-stage5-one-coefficient-reduction` reduces the full visible
stage-`5` higher-spin comparison to the single identity
`C^{res}_{3,5;4;0,4}(5)=C^{DS}_{3,5;4;0,4}(5)`.
`cor:winfty-stage5-visible-conjecture-network-collapse` then shows that,
once those four principal structural steps are granted, every
downstream local stage-`5` conjectural surface is either automatic or
equivalent to that same singleton comparison.
`cor:winfty-stage5-exact-remaining-input` packages the exact remaining
local input there as the four-step principal staircase consisting of
target-`5` transport vanishings, tail cross-target reduction, residual
vanishings, and residual cross-target reduction, together with the
single target-`4` singleton match. `cor:winfty-stage5-one-defect-family`
then rewrites the same frontier defect-theoretically: the full
visible-pairing stage-`5` higher-spin defect family collapses to one
representative defect at `(3,5;4;0,4)`.
`cor:winfty-stage5-visible-defect-classes` sharpens the same local
picture further: every nonautomatic downstream stage-`5`
visible-pairing surface lies in one of the three exact defect classes
`-5/4 D_5`, `D_5`, or `-3/4 D_5`, while the target-`5` corridor and the
self block are automatic.
`prop:winfty-stage5-transport-target-ladders` splits the mixed packet
into three fixed-target two-channel ladders,
and `prop:winfty-stage5-transport-pole-profiles` identifies the
target-`5` ladder as the lowest-pole transport lane and therefore the
softest next local proof surface.
`conj:winfty-stage5-higher-spin-identities` is the next finite
bar-vs-DS identity list.  The exact missing lemma for making the
stage-`4` four-channel contraction unconditional is now named
explicitly as `conj:winfty-stage4-ward-inheritance`, whose open
content is reduced by `prop:winfty-stage4-visible-pairing-gap` to the
single visible weight-`4` normalization conjecture, equivalently
`C^{res}_{4,4;2;0,6}(4)=2`, once the visible Virasoro Ward action is
fixed; `cor:winfty-stage4-single-scalar-equivalent` packages that
scalar as the exact theorematic form of the stage-`4` refinement.  On
the additional visible pairing locus, the higher-spin comparison is now
reduced further by
`cor:winfty-stage4-primitive-transport-square-triple` to the signless
square-class triple `(3,3;4;0,2)`, `(4,4;4;0,4)`, `(3,4;4;0,3)`, with
the swap-even square channel automatic from `(3,3;4;0,2)`.  The exact
next local stage-`4` gap after that reduction is the visible top-pole
Borcherds transport relation isolated in
`rem:winfty-stage4-primitive-transport-gap`: forcing the swap-odd
`W^{(4)}` transport square from the `(3,3)` square would bring the
residue packet down to the same two primitive self-coupling square
classes as on the principal DS side, and
`cor:winfty-stage4-visible-borcherds-two-primitive` now packages this
as an exact equivalence: on the visible pairing locus, that single
transport relation is precisely the remaining input for collapsing the
primitive-plus-transport triple to the principal two-primitive
square-class profile.
See NEW_MACHINERY.md #M8.

**Entry point**: Attack the first nontrivial finite-detection lanes.
On the Yangian side, extract the coefficients `K^{line}_{a,b}(N)` for
the first visible stages and compare them with the truncated RTT
coefficients on tensor products of fundamental evaluation modules.  On
the `W_\infty` side, extract the first generator-level residue
coefficients in the seed set `\mathcal{I}_N`, compare them with the
principal Drinfeld--Sokolov coefficients, and propagate by translation
closure.

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

### VIII-a: W-algebra Koszul duality for general nilpotent data / orbit-indexed frontier
- **Label**: `conj:w-orbit-duality` (w_algebras_framework.tex:141)
- **Statement**: W^k(g, f)^! = W^{k'}(g, f^D) where f^D = Barbasch-Vogan dual
- **Status**: Principal case proved (thm:w-algebra-koszul-main). Subregular in ADE partial.
  Hook-type W-algebras have proven duality (Arakawa-van Ekeren 2023, rem:hook-type-duality).
- **Fixes applied (Session ~125)**: BV duality corrected to partition transpose in type A
  (was wrongly stated as identity for simply-laced). sl₄ orbit pairs corrected.
  prop:ds-koszul-hierarchy proof restructured (2-stage: BRST + BV orbit identification).
- **Gap**: DS reduction for arbitrary f; BV duality theory for non-type-A;
  level-shift formula k' = k'(k, f) for non-principal reductions.
  This is a distinct orbit-indexed transport frontier, not the standard
  MC4 residue/kernel identification packet for `W_\infty` / Yangian
  towers.
- **Exact packet A**: determine the dual-orbit input
  `f \leftrightarrow f^D` needed by the conjecture beyond the current
  seeded type-A catalog, including the relevant component-group
  compatibilities.
- **Exact packet B**: determine the orbit-indexed level-shift rule
  `k' = k'(k,f)` extending the current seeded correction table.
- **Exact packet C**: construct and globalize paired non-principal DS
  seed transports whose survivor brackets, cohomology profiles, and
  normalization data match on dual orbit pairs beyond the present
  hook/subregular theorematic seeds.
- **Current scaffold**: `compute/lib/nonprincipal_ds_orbits.py` now gives a clean
  type-A frontier catalog with transpose BV duality, orbit-dimension
  identities, and an orbit-indexed non-principal level-shift data API
  (`nonprincipal_orbit_level_shift_type_a`) in place of a single hook-only
  ansatz callsite; seeded non-hook entries now include nonzero per-orbit
  corrections, and the seeded `general_nonprincipal` partition catalog is now
  part of that orbit verification layer too.
- **Compute expansion (Mar 7, 2026)**:
  `compute/lib/bv_duality.py` now isolates type-A BV pair logic
  (including first non-self-dual hook seed `A_3: (3,1) \leftrightarrow (2,1,1)`),
  and `compute/lib/nonprincipal_ds_reduction.py` adds the `sl_3` subregular BP
  seed + hook-pair DS seed records for the paired DS seed transport
  packet of the non-principal frontier.
- **Non-hook extension (Mar 8, 2026, twelfth pass)**:
  the orbit and DS-seed layers now include type-A two-row non-hook cases
  (`(n-s,s), s\ge 2`) with catalog/verifier coverage and propagated
  non-principal seed records, so frontier bookkeeping is no longer
  hook/subregular-only.
- **Broader non-hook extension (Mar 8, 2026, fourteenth pass)**:
  the same orbit/seed bookkeeping now reaches the seeded general type-A
  non-principal catalog (`general_nonprincipal` partitions such as `(2,2,1)`
  and `(3,2,1)`), with propagated orbit-corrected level shifts and dedicated
  seed verifiers.
- **Chain/normalization scaffolds (Mar 7, 2026, follow-on)**:
  `compute/lib/nonprincipal_ds_normalization.py` now exposes explicit
  convention bridges for BP central-charge sums, and
  `compute/lib/ds_reduction.py` records the first chain-level non-principal DS
  inputs (subregular `sl_3` triple, grading profile, BRST ghost weights).
- **BRST-input refinement (Mar 8, 2026)**:
  `compute/lib/ds_reduction.py` now also includes the full subregular
  good-grading basis, linear DS constraints, and the abelian positive-nilpotent
  check forcing the quadratic ghost term to vanish in the `sl_3` seed.
- **Truncated BRST layer (Mar 8, 2026, second pass)**:
  `compute/lib/ds_reduction.py` now includes an explicit truncated seed
  differential `d = \chi \wedge -` with symbolic `d^2=0` verification for the
  subregular `sl_3` seed, and paired seed complexes for the first non-self-dual
  hook case (`A_3`: `(3,1) \leftrightarrow (2,1,1)`).
- **Truncated cohomology layer (Mar 8, 2026, third pass)**:
  the DS scaffold now computes truncated cohomology dimensions explicitly;
  the subregular specialization and both first-hook-pair specializations are
  acyclic at this seed level.
- **Hook-family systematization (Mar 8, 2026, fourth pass)**:
  `compute/lib/nonprincipal_ds_reduction.py` now exposes a family API
  (`nonprincipal_hook_seed`, `nonprincipal_hook_seed_catalog`) with
  status/level-shift propagation checks across hook/subregular type-A cases,
  and `compute/lib/ds_reduction.py` now mirrors this with
  `hook_pair_ds_seed(_catalog)` plus family-level nilpotence/acyclicity checks
  for the truncated symbolic BRST sectors. The two catalogs are now explicitly
  cross-aligned by partition and level-shift checks.
- **Constraint-count ansatz layer (Mar 8, 2026, seventh pass)**:
  generic hook/subregular DS sectors now default to an explicit type-A sizing
  ansatz extracted from canonical hook `sl_2` triples (positive simple-root
  grade count, with the proved `sl_3` subregular case fixed at `2`) with
  verification checks, and this ansatz now propagates automatically through the
  DS pair catalogs and linear-constraint block builders.
  The orbit module now also provides explicit hook-pair profile records
  (`hook_orbit_pair_profile`, catalog + verifier) that package source/dual
  partitions, orbit/centralizer dimensions, positive basis labels, and the
  same simple-root count data used in the DS sizing layer.
- **Subregular survivor identification (Mar 8, 2026, fifth pass)**:
  `compute/lib/ds_reduction.py` now identifies the explicit `sl_3` subregular
  `g^f` survivor sector in matrix form and verifies that its DS weight profile
  matches the Bershadsky--Polyakov strong generators
  `(J, G^+, G^-, T)` with weights `(1, 3/2, 3/2, 2)`.
  The same scaffold now also exposes the canonical splitting
  `\mathfrak{sl}_3 = [e,\mathfrak{sl}_3] \oplus \mathfrak{g}^f` and the
  induced projection onto those surviving strong fields. The projected
  survivor-sector bracket is also now explicit at the linear seed level:
  `[J,G^\pm] = \pm \frac{3}{2} G^\pm`, `[G^+,G^-]=T`, with `T` central.
- **Hook-matrix representatives (Mar 8, 2026, sixth pass)**:
  `compute/lib/nonprincipal_ds_orbits.py` now supplies explicit standard
  nilpotent matrices for type-A hook partitions, including the first genuine
  non-self-dual pair `A_3: (3,1) \leftrightarrow (2,1,1)`, together with
  matrix-level recovery of the partition and direct centralizer-dimension
  checks against the closed partition formula. The same orbit scaffold now also
  produces explicit traceless centralizer bases for that first pair, with
  dimensions `5` and `9`, and standard `sl_2` triples with full `ad(h)`
  grading multiplicities on `\mathfrak{sl}_4`. The positive graded basis labels
  are now explicit as well, so the future DS ghost directions for that pair are
  concrete rather than just counted. Those actual five positive directions are
  now wired into the first hook-pair linear Koszul blocks in
  `compute/lib/ds_reduction.py`, and the corresponding ghost conformal weights
  are explicit on both source and target sides. The first hook-pair truncated
  wedge seed now uses the same five directions, so the pair's linear models are
  no longer mixed placeholder/real data.
- **Hook survivor algebra (Mar 8, 2026, seventh pass)**:
  the first non-self-dual hook pair now has an explicit homogeneous
  `\mathfrak{g}^f` survivor basis and closed reduced bracket. The source
  survivor DS weights are `(1,2,2,2,3)`, while the target survivor DS weights
  are `(1,1,1,1,3/2,3/2,3/2,3/2,2)`. Its positive sectors are now also known
  to be non-abelian on both sides, so the quadratic ghost term must appear in
  the genuine hook-pair BRST differential. The compute layer now packages this
  as explicit BRST blueprints with `quadratic_ghost_term_present = True` on
  both sides, and the nonzero `c c b` support entries are now explicit.
- **Hook ghost BRST realization (Mar 8, 2026, eighth pass)**:
  the first non-self-dual hook pair now has the actual finite ghost-sector
  BRST complexes in compute, with differentials including both the character
  term and the explicit quadratic `c c b` support. Both source and target
  complexes satisfy `d^2=0` and are acyclic in every ghost degree. Moreover,
  they match under an explicit canonical relabeling of the five positive
  directions. The same code now also builds mixed fixed constraint-degree
  blocks on shifted currents `u_i`, `c`-ghosts, and `b`-ghosts, and verifies
  `d^2=0` plus vanishing cohomology through constraint degree `2` on both
  sides. Those mixed blocks also match under the same canonical relabeling.
  The same mixed formalism now also covers the self-dual `sl_3` subregular
  control case through constraint degree `3`, with vanishing quadratic term and
  acyclic tested blocks.
- **Hook nonlinear current term (Mar 8, 2026, ninth pass)**:
  the mixed `u-c-b` truncation for the first non-self-dual hook pair now also
  includes the first nonlinear current/OPE correction, namely the `c \cdot \rho`
  action of the positive sector on shifted currents and `b`-ghosts derived from
  the explicit positive-sector brackets. This term is nontrivial on the first
  positive constraint-degree block, but the resulting nonlinear mixed blocks
  still satisfy `d^2=0`, remain acyclic through constraint degree `2`, and
  continue to match source-to-target under the canonical relabeling. In the
  self-dual `sl_3` subregular control case the same nonlinear term vanishes,
  exactly because the constrained positive sector is abelian.
- **Survivor-coupled truncation (Mar 8, 2026, tenth pass)**:
  the nonlinear mixed blocks now also carry linear survivor degree, with the
  positive sector acting on survivor variables through the induced quotient
  action `\mathfrak{g}/[e,\mathfrak{g}] \cong \mathfrak{g}^f`. For the first
  non-self-dual hook pair this survivor-feedback term is genuinely nonzero
  (`6` source terms, `14` target terms), but the first tested truncation
  (constraint degree `\le 1`, survivor degree `1`) is still square-zero and
  acyclic on both sides. In the self-dual `sl_3` subregular control case the
  survivor action is also explicit (`G^- \mapsto J`, `T \mapsto -G^+` under
  `c_{\alpha_1+\alpha_2}`), and the corresponding survivor-coupled truncation
  remains square-zero and acyclic through constraint degree `2`.
- **Higher survivor degree and internal CE layer (Mar 8, 2026, twelfth pass)**:
  the accelerated exact-rank path now checks the first hook-pair
  survivor-coupled truncation at survivor degree `2` as well, and it still
  collapses through constraint degree `1`. The first genuinely non-collapsing
  survivor layer is instead the internal reduced `g^f` current/ghost sector:
  `compute/lib/ds_reduction.py` now builds finite CE blocks on survivor
  polynomials plus survivor ghosts, using the reduced survivor bracket table to
  generate both quadratic ghost terms and adjoint-action terms. These blocks
  are square-zero and already have nonzero cohomology at survivor polynomial
  degree `1` in both the subregular `sl_3` control case and the first
  non-self-dual hook pair.
- **Semidirect obstruction identified (Mar 8, 2026, thirteenth pass)**:
  the next attempted coupling, namely the naive semidirect product of the
  positive-sector BRST layer with the internal reduced-survivor CE sector, is
  now also in compute. It fails `d^2=0` for a structural reason: the projected
  positive action on the reduced survivor sector is not a derivation of the
  reduced survivor bracket. Compute now records the derivation-defect tensors
  explicitly for the subregular `sl_3` control case and for the first
  non-self-dual hook pair. So the next missing ingredient is not “more
  truncation”; it is the higher correction term or homotopy-transfer datum that
  repairs this derivation defect.
- **First transferred correction on the control case (Mar 8, 2026, fourteenth pass)**:
  the subregular `sl_3` control case now has explicit `[e,\mathfrak{g}]`
  witness lifts for the survivor action and explicit unreduced witness formulas
  for every derivation defect. Because the active positive generator
  `E_{13}` is itself `ad_e`-exact, the first transferred cubic BRST
  correction is computable and cancels the naive reduced survivor action on the
  control case. The corrected semidirect survivor block is now verified to
  satisfy `d^2=0`; the next live step is to transport this witness/correction
  mechanism to the first genuinely non-self-dual hook pair rather than working
  only with quotient-level defect tensors.
- **First transferred correction on the first hook pair (Mar 8, 2026, fifteenth pass)**:
  that transport step now works at first order. For the first genuinely
  non-self-dual hook pair, the derivation-coboundary equation is solvable for
  every active positive ghost on both source and target survivor sectors. The
  resulting correction terms cancel the naive reduced survivor action
  completely on both sides, and the corrected semidirect survivor blocks
  restore `d^2=0` at the same low truncation where the naive quotient-level
  semidirect coupling failed.
- **Hook witness layer extracted (Mar 8, 2026, sixteenth pass)**:
  that explicit witness upgrade has now started on the first hook pair itself.
  Compute now records hook-pair survivor-action lifts as projected terms plus
  chosen `[e,\mathfrak{g}]` witness preimages, and the hook-pair derivation
  defects are recovered from the same unreduced witness identity as in the
  subregular control case.
- **Witness-driven first transfer on hooks (Mar 8, 2026, seventeenth pass)**:
  the remaining quotient-level step is now gone. The first hook-pair
  correction is packaged as explicit witness data: each correction term carries
  the exact constrained-current preimage in `[e,\mathfrak{g}]` together with
  the survivor-action lift whose projected part it cancels. The same
  witness-driven first-transfer mechanism is also checked on a low-rank hook
  catalog through `\mathfrak{sl}_7`, where every constrained current is
  `ad_e`-exact and the first transfer kills the reduced survivor action on both
  sides.
- The next family layer is now partially secured as well: at the first tested
  semidirect truncation
  `(constraint\ degree, survivor\ degree, internal\ CE\ degree)=(0,1,1)`,
  the corrected semidirect hook blocks are square-zero for every hook
  orientation through `\mathfrak{sl}_6`, and those corrected semidirect blocks
  now satisfy the expected dual-swap symmetry through the same range.
- The first step beyond that checked semidirect range is now sharper too:
  `\mathfrak{sl}_7` has all-orientation first-transfer cancellation, and the
  corrected semidirect truncation at `(0,1,1)` is now verified for the full
  hook family by direct half-catalog square-zero checks (`r=1,2,3`) together
  with the nontrivial transpose-dual comparisons (`r=1,2`).
- The next rank is no longer blocked by the old exact-projection solve either:
  compute now caches hook/partition survivor projections in traceless-basis
  coordinates, which makes the next family step tractable. On that optimized
  pipeline, `\mathfrak{sl}_8` now has all-orientation first-transfer
  cancellation, and the corrected semidirect truncation at `(0,1,1)` is
  verified for the full hook family by half-catalog square-zero checks
  (`r=1,2,3`) plus the matching transpose-dual checks on those same pairs.
- The same optimized semidirect pipeline now reaches one more full hook rank:
  `\mathfrak{sl}_9` is verified at `(0,1,1)` by square-zero checks on the
  half-catalog `r=1,2,3,4` together with the nontrivial dual-swap checks
  `r=1,2,3`. The first-transfer frontier is therefore already open one step
  past that family statement as well.
- That boundary has now moved again: `\mathfrak{sl}_{10}` satisfies the same
  symmetry-reduced semidirect check at `(0,1,1)`, with half-catalog
  square-zero on `r=1,2,3,4` and dual-swap on the nontrivial pairs `r=1,2,3`,
  while the first-transfer cancellation holds on every hook orientation
  `r=1,\dots,8`.
- The next family step is now settled too: after fixing a high-rank standard
  basis-label alias in the orbit layer, `\mathfrak{sl}_{11}` satisfies the
  same symmetry-reduced semidirect check at `(0,1,1)`, with half-catalog
  square-zero on `r=1,2,3,4,5` and dual-swap on the nontrivial pairs
  `r=1,2,3,4`, while the first-transfer cancellation holds on every hook
  orientation `r=1,\dots,9`. The new scaling bottleneck is dual-swap
  comparison cost, not survivor projection.
- The next rank is not closed, but it is now open at the extreme hook:
  `\mathfrak{sl}_{12}, r=1` already satisfies first-transfer cancellation,
  corrected semidirect square-zero at `(0,1,1)`, and the transpose-dual
  comparison, and `r=2` already satisfies first-transfer cancellation plus
  corrected semidirect square-zero at the same truncation. The live
  computational gap is therefore the rest of the `\mathfrak{sl}_{12}`
  half-catalog, not the existence of a next-rank sample.
- That gap is now gone. After replacing semidirect dual-swap comparison by a
  relabeled block-spec check instead of full BRST-block reconstruction,
  `\mathfrak{sl}_{12}` satisfies the corrected semidirect check at `(0,1,1)`
  for the full hook family, via half-catalog square-zero on `r=1,2,3,4,5`
  together with dual-swap on the nontrivial pairs `r=1,2,3,4,5`, and every
  hook orientation has first-transfer cancellation as well. The live boundary
  is now `\mathfrak{sl}_{13}`.
- That boundary has moved again. After replacing three remaining projector-path
  bottlenecks by direct standard-basis coordinates, one-pass `[e,g]` pivot
  extraction, and sparse basis-column assembly, `\mathfrak{sl}_{13}`
  satisfies the same corrected semidirect check at `(0,1,1)` for the full
  hook half-catalog: square-zero on `r=1,2,3,4,5,6`, dual-swap on the
  nontrivial pairs `r=1,2,3,4,5`, and first-transfer cancellation on every
  half-catalog orientation `r=1,\dots,6`. The live boundary is now
  `\mathfrak{sl}_{14}`.
- One step past that written family boundary is already open on the same
  compute track: `\mathfrak{sl}_{14}` now satisfies the same corrected
  semidirect check at `(0,1,1)` on the full hook half-catalog
  `r=1,\dots,6`, with dual-swap verified on the nontrivial pairs and
  first-transfer cancellation on the full half-catalog. The live boundary is
  now `\mathfrak{sl}_{15}`.
- The next rank is already open at low depth on the same pipeline:
  `\mathfrak{sl}_{15}` now satisfies the same corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog `r=1,\dots,7`, with dual-swap
  verified on the nontrivial pairs and first-transfer cancellation on the full
  half-catalog. The live boundary is now `\mathfrak{sl}_{16}`.
- One step past that written boundary is already open at low depth too:
  `\mathfrak{sl}_{16}` now satisfies the same corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog `r=1,\dots,7`, with dual-swap
  verified on the nontrivial pairs and first-transfer cancellation on the full
  half-catalog. The live boundary is now `\mathfrak{sl}_{17}`.
- The next rank is already open at low depth on the same pipeline:
  `\mathfrak{sl}_{17}` now satisfies the same corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog `r=1,\dots,8`, with dual-swap
  verified on the nontrivial pairs and first-transfer cancellation on the full
  half-catalog. The next target is now `\mathfrak{sl}_{18}`.
- That target is now fully closed at the same truncation:
  `\mathfrak{sl}_{18}` satisfies the corrected semidirect check at `(0,1,1)`
  on the full hook half-catalog `r=1,\dots,8`, with dual-swap verified on the
  nontrivial pairs and first-transfer cancellation on the full half-catalog.
  The next target is therefore `\mathfrak{sl}_{19}`.
- One step beyond that written boundary is now fully closed too:
  `\mathfrak{sl}_{19}` satisfies the corrected semidirect check at `(0,1,1)`
  on the full hook half-catalog `r=1,\dots,9`, with dual-swap verified on the
  nontrivial pairs and first-transfer cancellation on the full half-catalog.
  The next target is therefore `\mathfrak{sl}_{20}`.
- One step beyond that new written boundary is already open at the extreme
  hook: `\mathfrak{sl}_{20}, r=1` satisfies first-transfer cancellation and
  corrected semidirect square-zero at `(0,1,1)`.
- **Family nonlinear extension (Mar 8, 2026, eleventh pass)**:
  the hook mixed/nonlinear BRST scaffold is now family-level, not first-pair
  only: `compute/lib/ds_reduction.py` now exposes generic hook-pair APIs for
  constraints, positive-sector brackets, quadratic `c c b` support, and
  current-action terms, with mixed/nonlinear block builders for general
  type-A `(n,r)` hooks under explicit truncation controls.
- **Family dual-swap verification (Mar 8, 2026, eleventh pass)**:
  mixed and nonlinear hook-pair blocks are now compared against the
  transpose-dual case (`r \leftrightarrow n-r-1`) under canonical side
  relabeling, and catalog verifiers check this symmetry across the seeded
  type-A range. The survivor scaffold is now generalized as well through
  `hook_pair_surviving_field_candidates`, `hook_pair_reduced_brackets`,
  family survivor-action terms, and family survivor-coupled blocks; the same
  dual-swap catalog check now runs for survivor-coupled blocks on a tractable
  seeded range.
- **Non-hook chain lift (Mar 8, 2026, thirteenth pass)**:
  the same chain-level DS machinery now covers type-A two-row non-hook
  families: mixed/nonlinear/survivor-coupled block builders plus canonical
  relabel and dual-swap catalog verifiers are now in place on the seeded
  non-hook range.
- **General non-hook chain lift (Mar 8, 2026, fourteenth pass)**:
  the partition-pair DS machinery now also covers seeded general
  `general_nonprincipal` type-A families, so mixed/nonlinear/survivor-coupled
  block builders and dual-swap catalog verifiers are no longer restricted to
  the two-row non-hook subcatalog.
- **Mixed/nonlinear non-hook verification expansion (Mar 8, 2026, seventeenth pass)**:
  the cheaper non-hook block layers now run further than the initial
  seed: two-row mixed/nonlinear dual-swap checks reach `\mathfrak{sl}_9`,
  while the general non-principal mixed/nonlinear families are reduced by
  transpose symmetry and verified on the symmetry-reduced seeded range through
  size `9`. The same general survivor-coupled family-via-duality layer now
  also remains positive through size `12` in survivor degree `1` and through
  size `11` in survivor degree `2`.
- **Corrected semidirect non-hook lift (Mar 8, 2026, fifteenth pass)**:
  the same generic partition-pair machinery now carries witness-level
  first-transfer survivor corrections on the seeded non-hook range as well:
  internal survivor CE blocks plus corrected semidirect survivor blocks are now
  implemented for seeded two-row and `general_nonprincipal` type-A families,
  and the seeded `(0,1,1)` corrected semidirect catalog is wired into the same
  dual-swap verification layer.
- **Corrected semidirect non-hook verification expansion (Mar 8, 2026, sixteenth pass)**:
  the seeded two-row corrected semidirect layer now runs as a bundled check
  through `\mathfrak{sl}_8` at truncation `(0,1,1)`; the same two-row
  family-via-duality check also stays positive in survivor degree `2`
  through `\mathfrak{sl}_8`, and the seeded
  `general_nonprincipal` corrected
  semidirect family now reaches size `14` as a stable seeded bundle at the
  first corrected semidirect truncation `(0,1,1)`; the size-14 lift uses a
  fixed row-minor solver for the reduced survivor-bracket layer in place of
  repeated tall exact solves and prunes semidirect branches that cannot
  contribute at internal CE cutoff `1`. The same general
  family-via-duality check remains positive in survivor degree `2` through
  size `11`.
- **Assessment**: the frontier is now decomposed into the three exact
  packets above. Arakawa-van Ekeren hook-type duality and the
  `sl_3` subregular seed settle only the first theorematic seeds of
  that larger transport problem.
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
- Frontier placement:
  this cluster is an orthogonal weak flank, not part of the
  resolved-MC2 / live-MC3-MC4 / downstream-MC5 dependency chain.
- Status discipline:
  the structural lcm/profile shadow is theorematic, the $T$-matrix and
  quantum periodicity inputs are proved in their stated regimes, but
  modular bar-cohomology periodicity and the sharp geometric factors
  remain conjectural even for the flagship rational families.
- Evidence:
  computed examples, theta-function control, and rank-1 periodic
  shadows support the conjectural bar-periodicity statements, but do
  not upgrade them to theorem status.
- **Scale**: 1-3 years depending on specific result

### VIII-g: Derived bc-betagamma duality
- **Label**: `thm:extended-bc-betagamma` (chiral_koszul_pairs.tex:2040)
- **Gap**: Requires derived chiral Koszul duality framework (beyond monograph scope)
- **Scale**: 2 years (if derived chiral algebras framework is developed)

### VIII-h: Concordance frontier labels (session 121; one now theorematic)
- `conj:lagrangian-complementarity` — now a proved concordance theorem
  giving the PTVV shifted-symplectic / Lagrangian refinement
- `conj:universal-MC` — Single MC class controlling full genus tower
- `conj:family-index` — Grothendieck-Riemann-Roch for modular deformations
- `conj:derived-drinfeld-kohno` — E1-factorization equivalence with braid monodromy
- These labels are precisely stated with full scope remarks in
  concordance.tex; only the first has moved into the proved core.

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
| sl3 | Shared discriminant | `conj:sl3-bar-gf` | Unknown (need more data) |
| Y(sl2) | 3^n + 1 | `conj:yangian-bar-gf` | (1-3x^2)/((1-x)(1-3x)) |
| Non-simply-laced | Discriminant family | `conj:non-simply-laced-discriminant` | Unknown |

### Completed computations (Session ~125)
- **sl₃ modular rank** (compute/scripts/sl3_modular_rank.py): Weight-decomposed bracket-part
  differential rank over Q and F_p. Result: modular anomaly at weight (0,0) in degree 3
  (rank 9 over Q, 10 over F_p for ALL primes p). Degree 4 surjective (rank 512) in all chars.
  Documented in comp:sl3-modular-rank (detailed_computations.tex).
  **Note**: This is the bracket-only differential (d²≠0), not the full bar differential.
- **MC1 genus-1 `sl_2` PBW diagnostics generalized** (compute/lib/genus1_pbw_sl2.py):
  tensor-power Casimir and PBW `d_1` diagnostics are now reusable beyond the hard-coded
  tensor-square/triple cases; tests now verify the weight-2 and weight-3 elimination
  mechanism through a shared API (compute/tests/test_genus1_pbw_sl2.py).
  The same surface now includes explicit `sl_2`-equivariance and Casimir-commutation
  gates for `d_1` through tensor power `n=6`.
  These computed tensor-power diagnostics are now reflected directly in the proof text
  of `thm:pbw-genus1-km` (Step 4, `higher_genus.tex`) with explicit `n=3,4,5,6` spectra and
  rank/equivariance gates, keeping theorem narrative and executable evidence synchronized.
  This closes duplication in the MC1 compute surface and provides the direct launch point
  for higher-weight genus-1 checks.
- **MC1 scaling profiler added** (`compute/scripts/profile_genus1_pbw_sl2_scaling.py`):
  per-power timing confirms current practical default frontier at `n=6`, with Casimir
  eigenspace computation as the dominant cost (`~5.2s` of `~7.4s` total at `n=6`).
  The modular/sparse `n=7` path is now executable end-to-end:
  full eigenspaces recover as
  `{0:36, 4:273, 12:525, 24:588, 40:441, 60:231, 84:78, 112:15}`
  in ~`30.3s` total (`~19.3s` Casimir phase) for one prime and
  ~`53.2s` total (`~42.0s` Casimir phase) for a two-prime consistency run.
  The profiler and library now expose explicit Casimir modes
  (`auto`/`exact`/`exact_sparse`/`modular`/`theory`) with default policy `auto` = exact through `n<=6`
  and modular eigenspace extraction from `n>=7`, so default diagnostics
  stay full-strength on the stable window while keeping frontier checks executable.
  The modular lane now also has explicit backend strategies:
  `global` (full matrix rank over `GF(p)`) and
  `weight_block` (rank by ad(h)-weight blocks), with policy
  `CASIMIR_MODULAR_STRATEGY = auto` selecting `global` through `n<=6`
  and `weight_block` at `n>=7`.
  The frontier backend now also prunes impossible weight/eigenvalue
  pairs in modular block solves (`|w|>j` contributes zero for
  `\lambda_j=2j(j+1)`), reducing finite-field rank tasks on `n=7`.
  The default modular-prime lane is now tuned to the smallest
  non-colliding frontier prime (`CASIMIR_MODULAR_PRIMES=(127,)`), and
  the default `n=7` auto run (`auto` + `weight_block`) remains fully
  exact at the eigenspace level while reducing practical frontier time
  relative to the older large-prime baseline.
  A `QQ`-exact sparse nullity probe (`exact_sparse`) was benchmarked and does
  not improve the frontier (`n=5`: ~`26.7s` vs exact ~`1.85s`; `n=6`: >`240s`),
  so it remains a research-only backend.
- **MC2 Step-1/2/3/4(+cyclic-completed) compute scaffold advanced** (`compute/lib/mc2_cyclic_linf.py`):
  a finite-dimensional coderivation dg-Lie model and low-arity cyclic
  `L_\infty` model are now executable, including an initial symbolic
  Maurer-Cartan solver pass with nontrivial solutions `{0,1}` and regression tests
  in `compute/tests/test_mc2_cyclic_linf.py`.
  The same module now includes a first non-toy `sl_2` seed extracted from
  bar/OPE data (simple-pole bracket + normalized double-pole pairing),
  with dg-Lie/Jacobi/Leibniz and ad-invariant pairing checks.
  Step-3 now includes a first nontrivial cyclic higher bracket:
  an `eta`-valued `l_3` channel from the Killing 3-cocycle together with
  a mixed three-parameter residual probe `l_3(xe,yh,zf)` and CE-closure checks.
  Step-4 now includes a first completion/clutching surrogate:
  genus-indexed completed tensor convolution (`\widehat{\otimes}` proxy),
  a boundary clutching map induced by `l_2`, and an explicit factorized
  compatibility check (`6\omega + 22q\omega + 20q^2\omega` in the toy model),
  plus truncated completed-series MC residual checks.
  The same completion lane now verifies completed cyclicity identities
  for `l_2` and `l_3` genus-by-genus and includes a first symbolic
  truncated completed-MC solver branch (`a_0=1` implies `a_1=a_2=0`
  in the toy ansatz).
  The same lane now also supports genus-stratified obstruction extraction
  in the strict positive-genus regime and recursive branchwise solving,
  with explicit inconsistent-branch detection (`a_0=2` has no branch).
  It now also supports multi-basis completed-MC solving (truncated and
  recursive): in the toy `(\theta,\omega)` basis, fixing `\theta_0=1`
  forces higher `\theta_g` coefficients to vanish while retaining
  unconstrained `\omega_g` completed directions explicitly.
  A suspension-shifted symmetric `sl_2` `l_3` representative is now
  executable as well, with a nontrivial mixed residual
  (`\eta=-2xyz` on `(e,h,f)`) and explicit nonzero genus-2/genus-3
  obstruction channels on the strict positive-genus ansatz
  `\alpha_1=e+h+f`.
  The same shifted-seed nontrivial lane now extends to `sl_3`,
  `sp_4`, and `g_2`: on `(e1,e2,f12)` the mixed residual channel is
  `\eta=xyz` for `sl_3`, `\eta=2xyz` for `sp_4`, and `\eta=3xyz`
  for `g_2`, with genus-3 obstruction channels `\eta`, `2\eta`,
  and `3\eta`.
  The extracted one-channel normalization profile is now uniform:
  in all four lanes (`sl_2`, `sl_3`, `sp_4`, `g_2`), the genus-3
  `\eta` obstruction equals the mixed residual value at `(1,1,1)`,
  giving normalization ratio `1`.
  The same shifted lane now verifies the symbolic scaling law:
  genus-2 obstruction is quadratic in the genus-1 seed scale, and
  `O_3^\eta(t)=t^3\,\eta(1,1,1)` exactly across all four type/rank lanes.
  On the shared root-string channel `(e1,e2,f12)` for
  `sl_3/sp_4/g_2`, it now also satisfies the explicit signature law
  `O_2=t^2(e12+f1-m f2)` and `O_3^\eta=m t^3\eta=-t\,O_2^{f2}`
  with `m=1,2,3`.
  The same law is now lifted to a symbolic one-parameter root-string
  family (`m` formal): the shifted obstruction identities are verified
  as polynomial identities in `(m,t)`, and the sampled specializations
  `m=1,2,3` match the concrete `sl_3/sp_4/g_2` lanes exactly.
  The same channel now has a symbolic seed-packet lift
  (`a,b,m` formal):
  `[e1,e2]=a e12`, `[e2,f12]=b f1`, `[e1,f12]=-m f2`,
  `\langle e12,f12\rangle=m`.
  Its shifted profile is
  `O_2=t^2(a\,e12+b\,f1-m\,f2)`, `O_3^\eta=a m t^3\eta=-a t\,O_2^{f2}`;
  the genus-3 `\eta` channel is independent of the free `f1` packet
  coefficient `b`.
  The same packet is now executable as a projection law on shifted
  root-string lanes (`sl_3/sp_4/g_2` plus family samples `m=1,2,3`):
  extracting the visible low-arity packet
  (simple-pole `l_2` channel scales + root-string pairing scale)
  and rebuilding the packet seed reproduces the same
  `\eta(1,1,1)`, genus-2 channel, and genus-3 channel exactly.
  The same lane now has an inverse identifiability law:
  from obstruction data alone on that channel
  (`O_2^{e12}`, `O_2^{f1}`, `O_2^{f2}`, `O_3^\eta`) one recovers
  the packet coefficients `(a,b,m)` and
  `\eta(1,1,1)=a m`, with `\eta` still independent of `b`.
  The same packet now has a canonical transfer round-trip law:
  seed-side packet extraction, obstruction-side packet inference, and
  packet-profile reconstruction are mutually consistent and recover the
  same `(O_2,O_3^\eta)` data on
  `sl_3/sp_4/g_2` and root-string family samples `m=1,2,3`.
  The same transfer package now also recovers the first mixed
  higher-bracket channel itself: the reconstructed shifted seed has
  exactly the same `l_3(xe1,ye2,zf12)` residual as the source seed, and
  this residual is exactly
  `\eta(1,1,1)\,x y z` with
  `\eta(1,1,1)=a m` inferred from obstruction data.
  From that same obstruction profile, the shifted root-string seed
  profile is now recovered at channel level as well: reconstructed `l_2`, pairing,
  and mixed `l_3` coefficients on
  `(e1,e2,f12)\to(e12,f1,f2,\eta)` match the source seed exactly.
  On those same visible channels, the ordered seed triple is now
  permutation-rigid in compute: among seed-line permutations, only
  `(e1,e2,f12)` preserves the full
  `(e12,f1,f2,\eta)` support incidence, and this rigidity is preserved
  by obstruction-side chart recovery.
  The same root-string lane now makes the incidence-orbit criterion
  executable as well: the visible root-string permutation group
  extracted from the simple-pole/pairing/support packet realizes the
  same universal three-case orbit table on the tested lanes `m=1,2,3`,
  and the induced support orbits are singleton exactly on
  `(e12,f1,f2,\eta)`, with `e12` the unique normalization-nonzero
  genus-2 singleton.
  The same lane now also extracts a normalized invariant signature
  directly from those visible packets:
  normalized incidence `(1,1,-1,1)` on
  `(e12,f1,f2,\eta)` and normalized pairing profile
  `(e12,f12)/m=1`, `(f1,f12)/m=(f2,f12)/m=0`,
  uniformly across `sl_3/sp_4/g_2` and family `m=1,2,3`.
  Equivalently, the signed seed-character now computes as one canonical
  tuple `(1,1,-1,1)` with the same normalization/support indicators on
  every tested lane.
  The same lane now verifies full symbolic polynomial identities:
  `O_2(\alpha_1)=\frac12\,l_2(\alpha_1,\alpha_1)` and
  `O_3^\eta(\alpha_1)=\eta(x,y,z)=\frac16\,l_3^\eta(\alpha_1,\alpha_1,\alpha_1)`
  on the tested triples.
  This `\eta` channel is now checked to coincide with the unique cyclic
  deformation direction (`H^2_{cyc}=\mathbb{C}`) in each of the same
  `sl_2/sl_3/sp_4/g_2` lanes, and `\eta(1,1,1)` is now checked to
  match the seed Killing 3-cocycle normalization in each lane.
  For the same genus-1-only ansatz and arity-`<=3` shifted seeds, the
  obstruction support now truncates exactly at genus `3`
  (`O_g=0` for all `g>=4`).
  The same evidence is now available as one executable shifted
  one-channel criterion package combining normalization, scaling,
  root-string signature identities, polynomial identities, CE
  uniqueness alignment, and support truncation.
  On the theorem surface this now has a precise job description rather
  than a generic universality slogan: construct the intrinsic cyclic
  `\Defcyc(\cA)` model, realize the geometric completed tensor /
  clutching package, and normalize the single surviving genus channel in
  the simple-Lie case.
  That last package is now reduced again on the theorem surface:
  prove a joint clutching/trace isolation statement identifying the
  obstruction with the tautological line, construct the opposite
  one-channel Verdier/Lagrangian line so the pair spans a
  `\sigma`-stable plane, lift that plane to perfect one-channel
  projector subcomplexes with the PTVV / anti-involution
  quasi-isomorphism, then realize that lift by explicit one-channel
  coderivation subcomplexes in `\Defcyc(\cA)` and a geometric
  coefficient complex, then reduce those subcomplexes to finite
  low-bar-length seed data in
  `\operatorname{CoDer}^{\mathrm{cyc}}(\widehat{\barB}_X(\cA))[1]`,
  then compress that seed data to one distinguished degree-`2`
  cocycle plus finite bar-length-`<=3` correction packets and one
  finite pairing matrix from the minimal seed-packet criterion, then
  identify that packet with the visible low-arity simple-pole bracket
  sector, normalized double-pole pairing matrix, and Killing
  `l_3^\eta` sector, then reduce that visible packet further to a
  canonical transfer package on the one-channel seed spaces consisting
  of one cyclic seed, one shared generator-seed lift producing the
  Killing `l_3^\eta` sector, and one functorial normalization splitting
  off the one-channel cocycle line, then reduce that package further to
  the explicit root-string transfer law
  `O_2=t^2(a e12+b f1-m f2)`, `O_3^\eta=a m t^3\eta`,
  with obstruction-side recovery of `(a,b,m)` and the same
  coefficient-extraction normalization, then reduce that law further to
  a root-string chart forced on the one-channel seed spaces up to
  rescaling of the three seed lines, then reduce that chart statement
  further to intrinsic line detection by
  `l_{2,sp}`, `\beta^{dp}`, `\nu^{sp}`, and the support of
  `(O_2,O_3^\eta)`, then reduce that further to automorphism-rigidity
  of the one-channel support graph, then reduce that further to a
  finite stabilizer computation on the one-channel support graph, then
  reduce that further to a bounded incidence-matrix / orbit-count
  computation on the visible one-channel graph, then reduce that
  further to a universal three-case orbit table for
  `m=1,2,3` / `sl_3, sp_4, g_2`, then collapse that to direct
  lookup/identification against one canonical universal table, then
  collapse that further to the minimal invariant signature packet that
  forces that table, then collapse that further to the universal
  signed seed-character law recovering that packet, then collapse that
  further to the universal two-sign plus normalization-scalar law
  recovering that character, then collapse that further to the
  root-string parity sign plus normalization scalar, then collapse
  that further to the chart-normalized seed scalar, and
  finally one normalized scalar comparison with the proved coefficient
  `\kappa(\cA)` fixes the genus-$g$ normalization.

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
11. **Programme VI-e** (W-infinity/higher-spin): Requires filtered H-level targets plus exact coefficient-identification / finite-detection packages.
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
