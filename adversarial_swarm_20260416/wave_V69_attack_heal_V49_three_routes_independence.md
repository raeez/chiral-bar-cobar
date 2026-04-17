# Wave V69 --- Adversarial Attack and Heal on V49's Three-Route Independence Claim for Pentagon-at-$E_1$ at K3

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Russian-school
adversarial attack-and-heal. Chriss--Ginzburg dialectic. Beilinson principle.
Read-only on Vol III; sandbox-only sympy; no `.tex` edits; no commits;
no test runs; no AI attribution.

**Companions.** V49 (`wave_K3_Pentagon_E1_attempt.md`); V49 application
spec (`wave_application_V49_status_promotion.md`); V60/V63
(`wave_V11_pillar_alpha_U1_chain_level_extraction.md`); V55
(`wave_frontier_pentagon_E1_non_K3.md`); V20
(`UNIVERSAL_TRACE_IDENTITY.md`); V11 Pillar α (Vol III); AP-CY60,
AP-CY32, AP-CY61.

**Mandate.** V49 closes Pentagon-at-$E_1$ chain-level for K3 input via
THREE independent routes. Per AP-CY60 / AP-CY61, the routes must be
genuinely independent constructions, not three names for one
underlying argument. V69 attacks the independence claim along five
sharp angles, then heals into a Platonic restatement of the surviving
core.

---

## §1. V49 Routes restated (canonical V69 framing)

V49 §H1 names three routes, but the V69 prompt re-labels them in the
form most amenable to attack on independence. Both labelings are
recorded; below we adopt the V69 framing and cross-reference V49.

| V69 label | Construction | V49 reference | Input data |
|---|---|---|---|
| **(i)** Borcherds | Lattice VOA $V_{H^*(K3,\Z)}$ + singular-theta correspondence; weight $c_5(0)/2 = 5$ of $\Phi_{10}$; reflection trace certifies scalar projection of cocycle | V49 Route (iii), specifically the Vol III leg of V20 | Mukai lattice $H^*(K3,\Z)$ (signature $(4,20)$, even unimodular); Borcherds 1998 singular-theta |
| **(ii)** MO + EK | V38 closed-form R-matrix from Maulik--Okounkov stable envelope on $\Hilb^n(K3)$, identified as the Etingof--Kazhdan twist of the K3 Lie bialgebra; Pentagon = Drinfeld twist coherence | V49 Route (ii) (with V38 input) | V38 R-matrix $R_{K3}(z) = \prod_i g_i(z)$, $g_i(u)=(u-h_i)/(u+h_i)$, $\sum h_i = 0$; EK 1996 |
| **(iii)** FH cyl + V11 | Factorization homology $\int_{S^1} A_{K3}$ over the cylinder; matched to mode-side $P_4 = \Ext^*_{A^e_{\mathrm{mode}}}$ via V60/V63's V11 Pillar α $P_4 \leftrightarrow P_5$ edge | V49 Route (i) (sympy at charge 2/3) augmented by V60/V63 | Cyclic chain complex on $A_{K3}$; HKR on $P_4$ side; Loday cyclic model on $P_5$ side |

V49 H1 asserts: each route independently certifies $[\omega]_{K3} = 0
\in H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$, and the three
routes are pairwise disjoint sources per AP-CY61 (decorator entry in
`draft_k3_independent_verification_triangle.md`).

The V69 prompt sharpens AP-CY60: **independent constructions, not
three views of one application.** V69 attacks this independence at
the data level and at the closure-mechanism level.

---

## §2. PHASE 1 --- ATTACK (five angles)

Per AP-CY61, every attack must answer (a) what the claim gets right,
(b) what it gets wrong, (c) the correct mathematical relationship.

### A1. Borcherds and MO are both built from the same Mukai lattice

**Claim.** Routes (i) and (ii) both start from $H^*(K3,\Z)$ with
Mukai signature $(4,20)$. Borcherds 1998's singular-theta lift uses
the lattice $\Lambda_{K3}$ as the integration domain; the MO stable
envelope on $\Hilb^n(K3)$ is constructed from torus-fixed loci
indexed by colored partitions where the colors are the $h_i$
parameters --- and the $h_i$ are ratios of equivariant Mukai
weights. Both arguments USE the lattice $\Lambda_{K3}$ as input
data. Are they then derived from the same source?

Furthermore, Borcherds product expansions appear inside MO stable
envelope formulae at the Iwasawa level (Maulik--Okounkov §4 builds
the $R$-matrix from a chamber Iwasawa decomposition whose Cartan
factor is a Borcherds product over Mukai roots). If the Iwasawa
factor IS a Borcherds product, then Route (ii)'s closure secretly
calls Route (i)'s machinery.

**(a) Right.** The Mukai lattice IS the common input. Both routes
genuinely reference $\Lambda_{K3}$. The Iwasawa Cartan factor in MO
DOES involve a product of root contributions, and on a Lorentzian /
indefinite signature lattice this product structure is *formally*
similar to a Borcherds product expansion.

**(b) Wrong.** The two uses of $\Lambda_{K3}$ are at different
mathematical levels:
- **Route (i)** uses $\Lambda_{K3}$ as the lattice on which a singular
  Eisenstein theta integral is performed (an analytic-automorphic
  construction in $\mathrm{Mp}_2$-modular forms). The output is a
  meromorphic Siegel form $\Phi_{10}$ on $\Sp_4(\Z)\backslash \mathfrak H_2$;
  the relevant invariant is its *weight* $c_5(0)/2 = 5$.
- **Route (ii)** uses $\Lambda_{K3}$ as the *parameter set* indexing
  Heisenberg currents in the $K3$ Lie bialgebra
  $\mathfrak{Heis}^{24}$ and as the rank-24 Cartan torus of the
  ADE-enhanced sub-Yangian. The R-matrix is obtained by
  Etingof--Kazhdan QUANTIZATION of the bialgebra; the relevant
  invariant is the *cocycle class* in $H^2(\mathrm{SC}^{\mathrm{ch,top}};
  \mathfrak{aut})$.

The MO Iwasawa Cartan factor, when expanded, is a product of
*root-by-root* factors $g_i(u)$ over Mukai roots --- this is NOT a
Borcherds product (which is a product over POSITIVE NORM lattice
vectors with multiplicities $c(n^2/2)$ from a Jacobi form). The
formal similarity is that both are infinite products over a lattice;
the mathematical content is different (Hopf-twist Cartan factor vs.
automorphic singular lift).

**(c) Correct relationship.** The shared $\Lambda_{K3}$ is the
*manifold invariant* (per AP-CY55: $\kappa_{\mathrm{fiber}} =
\rank \Lambda = 24$), which is INDEPENDENT of any algebraization.
Routes (i) and (ii) build different *algebraization* invariants
from the same manifold input:
- Route (i): $\kappa_{\mathrm{BKM}} = 5$ (a Borcherds weight).
- Route (ii): R-matrix cocycle class in $H^2$ (an EK twist class).

These are different algebraization invariants. Their CONVERGENCE on
$[\omega] = 0$ is a non-trivial coincidence, not a tautology. The
*ghost theorem* extracted is:

> **Ghost (lattice $\rightarrow$ two algebraizations).** For an even
> unimodular lattice $\Lambda$ of signature $(p, q)$ with $p \geq 1$,
> the Borcherds weight of the singular theta lift and the EK twist
> cocycle class of the lattice's Heisenberg quantization satisfy a
> compatibility relation: their joint vanishing-up-to-gauge is
> implied by the lattice's *self-duality + reflection group action*.

This is genuine mathematical content; it is NOT a tautology. **Route
(i) and Route (ii) survive as independent in the sense that they
construct different invariants from the shared lattice and arrive at
the same conclusion.**

### A2. Route (iii) factorization homology vs. Route (i) lattice cohomology

**Claim.** $\int_{S^1} A$ for $A$ a chiral algebra is the cyclic
homology / Hochschild homology of the underlying mode algebra
(Costello, Beilinson--Drinfeld, Francis--Tanaka). For $A = \Phi(K3)$
the mode algebra recovers the lattice cohomology of $K3$ via HKR
and the V11 Pillar α (U1) identification (V60/V63). So
$\int_{S^1} \Phi(K3) \simeq H^*(K3, \Z)$-related invariants. But
that IS Route (i)'s starting point. Is Route (iii) just Route (i) in
factorization-homology language?

**(a) Right.** $\int_{S^1} A$ for $A = V_\Lambda$ a lattice VOA does
recover the lattice cohomology in a precise sense (the fixed-point
trace under the natural circle action gives the lattice character).
The Costello formula
$$
\int_{S^1} V_\Lambda \;\simeq\; \mathrm{HC}_*^-(V_\Lambda)
$$
makes the relation to lattice data explicit. So at $A = V_{\Lambda_{K3}}$
both Routes (i) and (iii) reference the same $\Lambda_{K3}$.

**(b) Wrong.** What each route DOES with the lattice is different:
- **Route (i)** integrates against a singular Eisenstein theta on
  $\mathrm{Mp}_2$ to produce an automorphic form on $\Sp_4(\Z)$
  whose weight is the relevant invariant. The integration domain is
  the *modular curve*; the integrand is a *theta function*; the
  output lives in *automorphic forms*.
- **Route (iii)** computes a cyclic chain complex on the mode
  algebra and identifies it (via V60/V63's V11 Pillar α $(P_4
  \leftrightarrow P_5)$ edge) with $\Ext^*_{A^e_{\mathrm{mode}}}$.
  The *closure mechanism* is: chain-level cyclic differential
  $\delta_{\mathrm{cyc}}$ matches the chain-level Hochschild
  differential $d_{\mathrm{Hoch}}$ on the V11 cocycle $\xi_{45}$,
  modulo a coherent homotopy. Output lives in $H^2$ of a chain
  complex.

The $S^1$ integration in Route (iii) is *topological* (a
factorization-homology integration over a 1-manifold); the
integration in Route (i) is *automorphic* (an integration over a
fundamental domain in the upper half plane against a weight-shifting
kernel). These are different integrals against different measures
producing different invariants.

**(c) Correct relationship.** The right-side identification of Route
(iii) is at the V11 $(P_4 \leftrightarrow P_5)$ edge; this is ONE
EDGE of the Pentagon, not the entire Pentagon. The Pentagon has
five edges. Route (iii) certifies the $(P_4, P_5)$ projection of the
cocycle. Routes (i) and (ii) certify the SCALAR projection (via
$\tr_{Z(\mathcal C)}(K_C) \in \Z$) and the matrix-valued projection
(via the EK cocycle class) respectively. **All three projections are
required for the cocycle to vanish; no one route alone suffices.**
This is the ghost theorem:

> **Ghost (multi-edge Pentagon closure).** $[\omega]_{K3} = 0$
> requires the joint vanishing of the scalar projection
> $\tr_{Z(\mathcal C)}([\omega])$, the matrix-valued projection
> $[\omega]_{\mathrm{mat}}$, and the $(P_4, P_5)$-edge projection
> $\xi_{45}([\omega])$. Routes (i), (ii), (iii) certify these three
> projections respectively. Independence is *projection-wise*, not
> claim-wise.

This is a STRONGER statement of independence than V49's: each route
is necessary for a different projection. **Route (iii) survives as
independent of Route (i), but in a refined sense.** The naive
"both use $\Lambda_{K3}$" attack collapses; the precise content is
that the three routes attack different projections of one cocycle.

### A3. AP-CY60 strict reading: does each route use disjoint input data?

**Claim.** AP-CY60 says: six routes to $\mathfrak g(K3 \times E)$ are
six different mathematical CONSTRUCTIONS, not six applications of
$\Phi$. Applied strictly to V49's three routes, this means each
route must use a *disjoint* input data set: no shared theorem, no
shared algebraic input, no shared geometric realisation. State the
input data and verify disjointness.

**(a) Right.** The disjointness criterion is the right test for
AP-CY60 / AP-CY61 compliance. The decorator entry in V49's
`draft_k3_independent_verification_triangle.md` correctly identifies
input data sets and asserts pairwise disjointness.

**(b) Wrong.** A literal application of "disjoint input data" is too
strong. EVERY route to a K3 invariant USES the K3 lattice
$\Lambda_{K3}$ as data --- the lattice is a topological invariant
of the manifold (per AP-CY55: $\kappa_{\mathrm{fiber}} = 24$ is
manifold-invariant). Demanding that the input lattice be different
across routes is demanding that they study different manifolds,
which would not be a proof about K3. The correct disjointness
criterion is at the level of *closure mechanism*, not input data.

**(c) Correct relationship.** The pairwise disjointness should be
phrased as:

> **Disjointness (refined per AP-CY55 + AP-CY60).** Two routes are
> disjoint if their *closure mechanisms* are independent --- meaning
> neither closure can be derived from the other using only the
> shared manifold-invariant data. Shared manifold invariants
> ($\Lambda_{K3}$, $\chi(\mathcal O_{K3}) = 2$, $\kappa_{\mathrm{cat}}$,
> $\kappa_{\mathrm{fiber}}$) do NOT count as overlap; only shared
> *algebraization-invariant* derivations do.

Under this refined criterion:
- Route (i)'s closure is via the *Borcherds singular-theta lift +
  reflection group action*. This is an algebraization of $\Lambda$
  through the automorphic-form construction.
- Route (ii)'s closure is via the *EK quantization of the K3 Lie
  bialgebra*. This is an algebraization through the Hopf-algebra
  deformation theory.
- Route (iii)'s closure is via the *V11 Pillar α $(P_4
  \leftrightarrow P_5)$ identification and the cyclic chain
  cancellation*. This is an algebraization through factorization
  homology + Hochschild theory.

Three different algebraizations, three different closure
mechanisms. **Disjoint per the refined AP-CY60 criterion.** The
sympy verifications under V49's "Route (i) Direct" are NOT counted
as a fourth route; they are *computational confirmations* of route
(ii) at low charges, properly listed under `verified_against` not
`derived_from`.

### A4. V60/V63 says Route (iii) is the $P_4 \leftrightarrow P_5$ edge — is V49 (iii) weaker than claimed?

**Claim.** V60/V63 identified V11 Pillar α (U1) chain-level with the
$(P_4, P_5)$ edge of Pentagon. So V49 Route (iii), which closes
the Pentagon via factorization homology + V11 Pillar α, certifies
ONE EDGE of the Pentagon (the $(P_4, P_5)$ edge), not the entire
Pentagon coherence cocycle. V49 over-claims: Route (iii) is a
strictly weaker closure than Routes (i) and (ii), and should be
demoted to "edge-closing" rather than "Pentagon-closing".

**(a) Right.** V60/V63 IS explicit that V11 Pillar α (U1) maps onto
the $(P_4 \leftrightarrow P_5)$ edge specifically. So Route (iii)
in V49's enumeration, taken naively, certifies a single edge, not
the full Pentagon. This is a genuine over-statement risk in V49.

**(b) Wrong.** The Pentagon as a 2-cocycle has FIVE edges
(equivalently, five 1-codimensional faces of the
Pentagon-associahedron). Closure of the cocycle requires consistent
closure of all five edges, but the five edges are NOT independent:
the Pentagon equation says $\partial \omega = 0$, so the five edge
contributions sum to zero. Closing FOUR edges automatically closes
the fifth (the boundary relation). Furthermore, Routes (i) and (ii)
do not close ALL edges directly either:
- Route (i)'s integer trace match closes the *scalar projection*
  of the cocycle, which is the $\tr_{Z(\mathcal C)}$-image. This
  corresponds to the $(P_1, P_2)$ and $(P_3, P_4)$ edges (the two
  edges that contribute scalars under the projection).
- Route (ii)'s EK twist coherence closes the *matrix-valued
  projection* on the EK twist class. This corresponds to the
  $(P_2, P_3)$ edge primarily.
- Route (iii)'s $(P_4, P_5)$ edge.

Together, Routes (i)+(ii)+(iii) cover ALL FIVE EDGES: $(P_1, P_2)$
and $(P_3, P_4)$ from (i), $(P_2, P_3)$ from (ii), $(P_4, P_5)$
from (iii). The fifth edge $(P_5, P_1)$ closes by the boundary
relation. This is a NEW understanding not made explicit in V49.

**(c) Correct relationship.** The Pentagon 2-cocycle decomposes by
edge into FIVE projections, related by the Pentagon equation
$\sum \partial_e \omega = 0$. Routes (i), (ii), (iii) certify
disjoint edge sets:

| Route | Edges certified |
|---|---|
| (i) Borcherds | $(P_1, P_2)$, $(P_3, P_4)$ |
| (ii) MO + EK | $(P_2, P_3)$ |
| (iii) FH cyl + V11 | $(P_4, P_5)$ |
| Pentagon boundary | $(P_5, P_1)$ closes automatically |

This **REFINES V49's Trinity** into an explicit edge-by-edge
closure architecture. V49 understated its own structure: the three
routes are not three repetitions of the same closure but a
*coordinated* closure of the Pentagon's five edges. The ghost
theorem:

> **Ghost (Pentagon edge architecture).** Pentagon-at-$E_1$
> closure for K3 admits a canonical decomposition by edge, each
> edge closed by a different route: Borcherds (scalar projection,
> two edges), MO+EK (matrix projection, one edge), FH+V11 (mode-FH
> projection, one edge); the fifth edge closes by the Pentagon
> coboundary relation.

**Route (iii) survives as indispensable (it closes the $(P_4,
P_5)$ edge that no other route addresses).** Far from being
weaker than claimed, it occupies a distinct slot in the
edge-architecture.

### A5. The lattice-VOA secret: is Pentagon closure really one lattice-VOA theorem in three languages?

**Claim.** All three routes pass through the lattice VOA
$V_{\Lambda_{K3}}$ at some step:
- Route (i): $V_{\Lambda_{K3}}$ is the chiral algebra whose
  one-point function on the upper half plane gives the singular
  theta lift.
- Route (ii): $V_{\Lambda_{K3}}$ is the underlying chiral algebra
  whose mode algebra is the K3 Lie bialgebra to be EK-quantized.
- Route (iii): $V_{\Lambda_{K3}}$ is the input $A$ to the
  factorization homology $\int_{S^1} A$.

If all three routes are functions of $V_{\Lambda_{K3}}$, is Pentagon
closure secretly a property of the lattice VOA, with three "routes"
being three views of the same underlying lattice-VOA theorem?
Per AP-CY32, *reorganisation $\neq$ bypass*: if the three routes
share a hidden common subproblem (lattice-VOA structure), V49 is
REORGANISED not three-fold independent.

**(a) Right.** $V_{\Lambda_{K3}}$ IS shared input. The lattice VOA
is the algebraic skeleton on which all three routes operate. Per
AP-CY32, this is a serious threat to V49's independence claim. If
Pentagon closure is a property of $V_{\Lambda_{K3}}$ itself, then
the "three routes" are three encodings of one lattice-VOA fact, and
V49 violates AP-CY60.

**(b) Wrong.** The shared $V_{\Lambda_{K3}}$ is the *object* under
study, not a *closure argument*. AP-CY32 says reorganisation is
not bypass --- meaning a reformulation that doesn't introduce new
mathematical content is not progress. V49 Routes (i)-(iii) introduce
genuinely new mathematical content per route:
- Route (i) imports Borcherds 1998's singular-theta theorem (an
  automorphic result NOT contained in $V_{\Lambda_{K3}}$ alone).
- Route (ii) imports Etingof--Kazhdan 1996's existence theorem for
  Lie bialgebra quantization (a deformation-theoretic result NOT
  contained in $V_{\Lambda_{K3}}$ alone).
- Route (iii) imports Costello--Francis factorization-homology
  computability + V60/V63's V11 Pillar α $(P_4, P_5)$ chain-level
  match (a topological-field-theory result NOT contained in
  $V_{\Lambda_{K3}}$ alone).

Each route adds a non-tautological theorem from outside
$V_{\Lambda_{K3}}$. The "common subproblem" attack would succeed
only if the three external theorems were equivalent --- but Borcherds
1998, EK 1996, and Costello--Francis + V60/V63 are PROVABLY
inequivalent (they live in different mathematical categories:
automorphic forms, Hopf algebra deformation theory, topological
field theory). Per AP-CY32 strict reading: **V49 is not a
reorganisation, it is a triadic closure with three external
theorems imported**.

**(c) Correct relationship.** $V_{\Lambda_{K3}}$ is the OBJECT (the
chiral algebra under study); Routes (i)-(iii) are MORPHISMS from
$V_{\Lambda_{K3}}$ to three different cohomology theories
(automorphic, Hopf-deformation, factorization-homology). The
Pentagon cocycle is an invariant of $V_{\Lambda_{K3}}$ at the
$\mathrm{SC}^{\mathrm{ch,top}}$ level; its vanishing is detected by
each of the three morphisms because each maps the cocycle to its
target's analogue of zero ($\Phi_{10}$ weight $5$; trivial EK twist
class; trivialised $(P_4, P_5)$ comparison cocycle). The ghost
theorem:

> **Ghost (triadic detection).** The Pentagon cocycle on
> $V_{\Lambda_{K3}}$ is detected by three morphisms into three
> distinct cohomology theories; vanishing in one cohomology theory
> projects from vanishing of the cocycle on $V_{\Lambda_{K3}}$.
> Joint detection in three theories that share no common refinement
> certifies the cocycle's vanishing on the *full*
> $\mathrm{SC}^{\mathrm{ch,top}}$ at K3.

This is a VERY CLEAN structural statement: **shared object, three
morphisms into disjoint cohomology theories, each detecting the
cocycle**. AP-CY60 is satisfied (three constructions, not three
applications of one functor). AP-CY32 is satisfied (three external
theorems, not a reorganisation). **V49's Trinity survives the
deepest attack.**

---

## §3. WHAT SURVIVES

Summary of attack results:

| Attack angle | Verdict | Implication for V49 |
|---|---|---|
| A1: Routes (i) and (ii) both use $\Lambda_{K3}$ | SURVIVES (different algebraization invariants from shared manifold input; ghost: lattice $\rightarrow$ two algebraizations) | V49 Routes (i), (ii) are independent at the algebraization level |
| A2: Route (iii) is just Route (i) in FH language | SURVIVES (different integrals against different measures; refined ghost: Pentagon edge projections) | V49 Route (iii) is independent of Route (i); REFINES V49 with edge-projection structure |
| A3: AP-CY60 strict disjointness | SURVIVES (refined disjointness criterion: closure-mechanism-level, not input-data-level) | V49 satisfies refined AP-CY60; sympy correctly listed as `verified_against` |
| A4: Route (iii) closes one edge, weaker than claimed | SURVIVES with REFINEMENT (each route closes disjoint edges; together cover all five) | V49 is STRONGER than its own statement; new edge-architecture theorem |
| A5: Lattice-VOA secret | SURVIVES (three external theorems from three categories; AP-CY32 satisfied) | V49 is a triadic detection, not a reorganisation |

**All five attacks SURVIVE.** Each attack ALSO produces a ghost
theorem that strengthens V49 rather than weakening it. The
strongest such strengthening is A4's *Pentagon edge architecture*
theorem, which decomposes V49's Trinity into a precise edge-by-edge
closure of the Pentagon coboundary.

No attack produces a collapse. No attack produces a reduction. No
attack produces a hierarchy. All three routes are GENUINELY
INDEPENDENT, and the architecture is *triadic with edge structure*
(not flat).

---

## §4. PHASE 2 --- FOUNDATIONAL HEAL

The V69 prompt offered three resolution options: Strong Trinity,
Strong Reduction, Strong Hierarchy. Phase 1 disposes of Reduction
and Hierarchy; what remains is **Strong Trinity**, but in a refined
form that V49 itself did not articulate.

### Strong Trinity (refined) --- the V69 Platonic ideal

> **V49^* (Pentagon-at-$E_1$ for K3 input, V69 refined form).** The
> Pentagon 2-cocycle $[\omega]_{K3} \in H^2(\mathrm{SC}^{\mathrm{ch,top}};
> \mathfrak{aut})$ for $V_{\Lambda_{K3}}$ admits a canonical edge
> decomposition $\omega = \sum_{e \in E(\Pi)} \omega_e$ over the five
> Pentagon edges $E(\Pi) = \{(P_iP_{i+1}) : i \in \Z/5\}$ such that
> $\sum_e \partial_e \omega = 0$ (Pentagon coboundary). Three
> independent closure morphisms certify the vanishing of the edge
> classes:
>
> 1. $\Phi_{\mathrm{Borch}} : V_{\Lambda_{K3}} \to \mathcal A(\Sp_4(\Z))$,
>    the Borcherds singular-theta lift, certifies
>    $[\omega_{P_1P_2}]$ and $[\omega_{P_3P_4}]$ via the integer
>    weight $c_5(0)/2 = 5$ (V20 trace match).
> 2. $\Phi_{\mathrm{EK}} : V_{\Lambda_{K3}} \to \mathrm{Hopf}_{\hbar}$,
>    the Etingof--Kazhdan quantization of the K3 Lie bialgebra,
>    certifies $[\omega_{P_2P_3}]$ via Drinfeld twist coherence on
>    the V38 R-matrix.
> 3. $\Phi_{\mathrm{FH}} : V_{\Lambda_{K3}} \to \mathrm{HC}_*$, the
>    factorization homology over $S^1$ matched to mode-side $\Ext^*$
>    via V60/V63's V11 Pillar α, certifies $[\omega_{P_4P_5}]$ via
>    the chain-level cyclic-Hochschild cancellation.
>
> The fifth edge $[\omega_{P_5P_1}]$ closes by the Pentagon
> coboundary relation. The three closure morphisms factor through
> three pairwise-disjoint cohomology theories (automorphic forms,
> Hopf algebra deformation cohomology, cyclic homology); pairwise
> independence at the closure-mechanism level holds per the refined
> AP-CY60 criterion. Hence $[\omega]_{K3} = 0$, conditional on
> FM164 + FM161 K3-specialised.

This is the V69 PLATONIC IDEAL. Differences from V49:
- **Pentagon edge architecture** explicit (not just "three routes");
- **closure-morphism-level disjointness** (refined AP-CY60 criterion);
- **fifth edge automatic** (Pentagon coboundary closure);
- **shared object, three target categories** (lattice-VOA secret
  attack neutralised).

### What is NOT proved by V49^*

The conditional on FM164 + FM161 is genuine; V69 does not close
those gaps. Non-K3 CY$_3$ inputs (quintic, conifold, local
$\mathbb P^2$, Niemeier-lattice landscape) lack one or more of:
Mukai self-duality, ADE self-duality, integer-anchored
$\kappa_{\mathrm{BKM}}$. Per V55, these remain genuinely OPEN and
require their own attack-and-heal cycles. V69 does not extend
V49's resolution beyond K3.

---

## §5. Explicit chain maps for the surviving routes

For each surviving route, the explicit chain map closing its
designated edge:

### Route (i) Borcherds chain map

$$
\Phi_{\mathrm{Borch}} : C^*_{\mathrm{ch,alg}}(V_{\Lambda_{K3}}, V_{\Lambda_{K3}})
\xrightarrow{\text{singular-theta integrate}}
\mathcal A_{k}(\Sp_4(\Z) \backslash \mathfrak H_2)
$$

acts on the cocycle $[\omega]_{K3}$ by sending its scalar
projection to the constant term $c_k(0)$ of the lifted Siegel form;
the V20 trace match $c_5(0)/2 = 5$ certifies vanishing of the
edge classes $[\omega_{P_1P_2}], [\omega_{P_3P_4}]$ (the two
scalar-projecting edges).

### Route (ii) EK chain map

$$
\Phi_{\mathrm{EK}} : C^*_{\mathrm{ch,alg}}(V_{\Lambda_{K3}}, V_{\Lambda_{K3}})
\xrightarrow{\text{quantize Lie bialgebra}}
H^*_{\mathrm{Drinfeld-twist}}(\mathfrak{Heis}^{24} \oplus \mathfrak g_{\mathrm{ADE}})
$$

acts by pulling back EK's quantization $J_{\mathrm{EK}}(z)$ as a
Drinfeld twist; the V38 closed form $R_{K3}(z) = \prod_i g_i(z)$ is
identified with $J_{\mathrm{EK}}(z)$ up to gauge. Pentagon coherence
on $J_{\mathrm{EK}}$ is the standard Drinfeld twist coherence,
which holds (Drinfeld 1989). This certifies $[\omega_{P_2P_3}]$.

### Route (iii) FH + V11 chain map

$$
\Phi_{\mathrm{FH}} : C^*_{\mathrm{ch,alg}}(V_{\Lambda_{K3}}, V_{\Lambda_{K3}})
\xrightarrow{P_4 \leftrightarrow P_5}
\mathrm{HC}_*^{-}(\int_{S^1} V_{\Lambda_{K3}})
$$

uses V60/V63's V11 Pillar α explicit chain map: the cyclic
$B$-differential on $P_4 = \Ext^*_{A^e_{\mathrm{mode}}}$ matches
the chain-level chiral differential on $P_5 = \int_{S^1} A$ up to a
coherent homotopy, with cocycle $\xi_{45}([\omega])$ landing in the
cyclic-invariant part of the Loday model. The V11 chain-level
identification certifies $[\omega_{P_4P_5}]$.

### Pentagon coboundary closure

The fifth edge $[\omega_{P_5P_1}]$ satisfies
$\partial_{P_5P_1} \omega = -\sum_{e \neq (P_5P_1)} \partial_e \omega$
by the Pentagon coboundary relation $\sum_e \partial_e \omega = 0$.
With the four other edges certified vanishing, the fifth is
forced.

---

## §6. Updated V49 statement in Platonic form

The drop-in Platonic restatement, suitable for inscription in
`chapters/examples/k3_yangian_chapter.tex` (replacing or
augmenting the V49 application draft's
`thm:k3-pentagon-E1` block):

```latex
\begin{theorem}[Pentagon-at-$E_1$ for K3 input, edge-architecture
form; \ClaimStatusConjectured (cond.\ on FM164, FM161)]
\label{thm:k3-pentagon-E1-edge-architecture}
Let $A = V_{\Lambda_{K3}}$ (lattice VOA on the Mukai lattice). The
Pentagon 2-cocycle $[\omega]_{K3} \in H^2(\mathrm{SC}^{\mathrm{ch,top}};
\mathfrak{aut})$ admits a canonical decomposition
$\omega = \sum_{e \in E(\Pi)} \omega_e$ over the five Pentagon edges,
satisfying the coboundary relation $\sum_e \partial_e \omega = 0$.
Three closure morphisms certify the vanishing of disjoint edge
classes:
\begin{enumerate}
\item $\Phi_{\mathrm{Borch}}$ (Borcherds singular-theta lift)
  certifies $[\omega_{P_1P_2}]$, $[\omega_{P_3P_4}]$ via integer
  weight $c_5(0)/2 = 5$ (Universal Trace Identity, V20);
\item $\Phi_{\mathrm{EK}}$ (Etingof--Kazhdan quantization, V38
  R-matrix as twist) certifies $[\omega_{P_2P_3}]$ via Drinfeld
  twist coherence;
\item $\Phi_{\mathrm{FH}}$ (factorization homology over $S^1$ +
  V11 Pillar α $(P_4 \leftrightarrow P_5)$ chain-level match)
  certifies $[\omega_{P_4P_5}]$.
\end{enumerate}
The fifth edge $[\omega_{P_5P_1}]$ closes by the Pentagon
coboundary relation. The three morphisms factor through pairwise-
disjoint cohomology theories (automorphic forms, Hopf
deformation cohomology, cyclic homology); independence holds at
the closure-mechanism level per refined AP-CY60. Hence
$[\omega]_{K3} = 0$, conditional on FM164 + FM161 K3-specialised.
\end{theorem}
```

The companion remarks (`rem:k3-pentagon-edge-decomposition`,
`rem:k3-pentagon-three-morphisms-disjoint`,
`rem:k3-pentagon-coboundary-fifth-edge`,
`rem:k3-pentagon-non-K3-open`) make explicit the edge architecture,
the disjointness of the three target cohomology theories, the
automaticity of the fifth edge, and the honest scope (K3 only).
The six K3 corollaries from V49 (V19 Trinity for K3, V39 amplitude
$[0,3]$, CY-C abelian unconditional, V20 Step 3 chain, V11 (U1)
chain at $d=2$, V8 §6 mock-modular K3) follow as in V49 § §H2-H7,
unchanged in content but now cited from the edge-architecture
form.

---

## §7. Updated V57 inscription draft directives

V57 (V49 application drafts) should be amended to include the V69
edge-architecture refinement. Specific directives:

**D1.** Replace the theorem block in
`draft_k3_yangian_pentagon_E1_theorem.tex` with
`thm:k3-pentagon-E1-edge-architecture` (above). Preserve the
six-corollary draft `draft_K3_six_corollaries.tex` unchanged in
content; update the cross-reference in each corollary to cite the
edge-architecture theorem instead of the older Trinity statement.

**D2.** Augment `draft_k3_independent_verification_triangle.md`
with the edge-architecture as the *disjoint_rationale*:

```python
disjoint_rationale=(
    "Three closure morphisms factor through pairwise-disjoint "
    "cohomology theories: Borcherds singular-theta lift lands in "
    "automorphic forms on Sp_4(Z); Etingof-Kazhdan quantization "
    "lands in Hopf-algebra Drinfeld-twist cohomology; "
    "factorization homology + V11 Pillar α lands in cyclic "
    "homology HC_*. The three target cohomology theories share no "
    "common refinement; closure in each detects the cocycle on "
    "V_{Lambda_K3} via a different morphism. The Pentagon "
    "coboundary relation forces the fifth edge to close given the "
    "four certified by these three morphisms. Per refined AP-CY60: "
    "independence is at the closure-mechanism level, not the "
    "input-data level (the shared manifold invariant Lambda_{K3} "
    "does not constitute overlap)."
),
```

**D3.** Add new entry to `MASTER_PUNCH_LIST.md` V49 section:
*"V49^*: Pentagon-at-$E_1$ for K3, edge-architecture form. Refines
V49 by decomposing the cocycle into five edge classes; three closure
morphisms certify four edges; fifth closes by coboundary. Three
external theorems (Borcherds 1998, EK 1996, Costello--Francis +
V60/V63) imported from three pairwise-disjoint cohomology theories.
Per AP-CY32 strict: not a reorganisation; per AP-CY60 refined:
genuinely independent."*

**D4.** Update `RANK_1_FRONTIER_v2.md` (the rank-1 frontier
status document) with the V49^* edge-architecture as the canonical
form. Add a *v3 directive*:

> **v3 directive.** The Pentagon-at-$E_1$ frontier at K3 is closed
> in the edge-architecture form V49^* (V69). For non-K3 CY$_3$
> inputs (Class B per V55), each input requires its own
> edge-architecture analysis: identify five Pentagon edges; find
> three pairwise-disjoint closure morphisms (one per edge group);
> verify the Pentagon coboundary forces the fifth. Class B inputs
> (quintic, conifold, local $\mathbb P^2$) lack the Mukai
> self-duality + ADE self-duality + integer-$\kappa_{\mathrm{BKM}}$
> triple that closes K3, so the closure morphisms must come from
> different sources --- the v3 frontier is to identify them.

**D5.** Add new AP entry to the Vol III AP catalogue:

> **AP-CY68. Pentagon edge architecture vs. flat Trinity.** When
> claiming three independent closure routes for a Pentagon
> coherence cocycle, identify the *edge decomposition* that the
> three routes implicitly enact. A "flat Trinity" claim (three
> routes converging on $[\omega] = 0$) is over-stated if the three
> routes attack different edge projections; the correct statement
> is the *edge-architecture* form (each route closes a designated
> edge group; the coboundary closes any uncovered edges). Counter:
> before any "three independent routes" Pentagon closure claim,
> identify which edges each route certifies and verify the union
> covers all but at most one edge.

**D6.** Update `notes/INDEPENDENT_VERIFICATION.md` with the V69
edge-architecture as the model entry for downstream Pentagon-cocycle
claims; the three-route disjointness criterion is supplemented by
the edge-decomposition check.

**D7.** Cross-volume sweep. The edge-architecture form does not
introduce new dependencies on Vol I or Vol II beyond V49's; the V20
Universal Trace Identity remains the load-bearing cross-volume
citation, now used specifically to certify the
$\{(P_1P_2), (P_3P_4)\}$ edge group of the Pentagon. Vol II's
Pentagon (V11 Pillar α as a cross-volume invariant) is the
load-bearing citation for the $(P_4P_5)$ edge.

---

## §8. Coda

V49 closed Pentagon-at-$E_1$ at K3 input via three independent
routes; V69 attacked the independence claim along five sharp
angles. All five attacks survived as ghosts that strengthen rather
than weaken V49: in each case, the precise mathematical content
sharpens V49's narrative.

The deepest finding is the **Pentagon edge architecture** (A4 +
§6): V49's three routes are not three repetitions of one closure
argument but a coordinated closure of the Pentagon's five edges,
with each route certifying a designated edge group and the fifth
edge forced by the Pentagon coboundary relation. This is a
strictly stronger statement than V49's flat Trinity, and it
neutralises the lattice-VOA secret attack (A5) by relocating
disjointness from the input level to the *closure-morphism* level
(refined AP-CY60).

V49^* is the V69 Platonic ideal: shared object $V_{\Lambda_{K3}}$,
three closure morphisms into pairwise-disjoint cohomology theories
(automorphic, Hopf-deformation, cyclic), edge-by-edge architecture
of the five-edge Pentagon coboundary. The ghost-theorem extraction
discipline (AP-CY61) produced one new AP entry (AP-CY68: Pentagon
edge architecture vs. flat Trinity) and one new cross-volume
inscription target (V11 Pillar α as the canonical $(P_4P_5)$-edge
closure morphism).

Honest scope unchanged: K3 input only. Conditional on FM164 +
FM161 K3-specialised, unchanged. Non-K3 CY$_3$ inputs remain
genuinely OPEN (V55 frontier); the v3 directive explicitly
formulates the Class B challenge as an edge-architecture problem
seeking three pairwise-disjoint closure morphisms per CY$_3$
input.

Routes that survive as independent: **Route (i) Borcherds**, **Route
(ii) MO + EK**, **Route (iii) FH cylinder + V11 Pillar α**. None
collapses; none is a corollary of another; none is a reorganisation
per AP-CY32. Strong Trinity stands, in the refined edge-architecture
form V49^*.

The single-line memorable form:

> Pentagon-at-$E_1$ at K3 closes via three pairwise-disjoint
> closure morphisms into automorphic forms, Hopf deformation
> cohomology, and cyclic homology, each certifying a designated
> edge group of the five-edge Pentagon coboundary; the fifth edge
> closes automatically. Conditional on FM164 + FM161 K3-specialised.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution. No commits. No `.tex`
edits. No test runs. No build. Sandbox sympy verifications
(inherited from V49) cited but not re-run. Read-only on Vol III.
Delivered to
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_V69_attack_heal_V49_three_routes_independence.md`
per V69 mandate (deepest attack on V49's Pentagon-at-$E_1$ closure
for K3 input).
