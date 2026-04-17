# Wave V84 --- Adversarial attack and heal on V69's fifth-edge coboundary closure

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.**
Russian-school adversarial attack-and-heal. Stasheff--Mac Lane operadic
rigor; Lurie HA discipline. Read-only on Vol III; sandbox-only sympy;
no `.tex` edits; no commits; no test runs; no build; no AI attribution.

**Companions.** V69
(`wave_V69_attack_heal_V49_three_routes_independence.md`); V49
application spec (`wave_application_V49_status_promotion.md`); V49
(`wave_K3_Pentagon_E1_attempt.md`); V60/V63 (`wave_V11_pillar_alpha_
U1_chain_level_extraction.md`); V20 (`UNIVERSAL_TRACE_IDENTITY.md`);
AP-CY55, AP-CY57, AP-CY60, AP-CY61, AP-CY32, AP-CY30 (factored vs.
solved at higher coherence), AP-CY39 (incompatibility, cross-arity).

**Mandate.** V69 produced V49\* edge architecture: three closure
morphisms $\Phi_{\mathrm{Borch}}, \Phi_{\mathrm{EK}}, \Phi_{\mathrm{FH}}$
certify pairwise-disjoint Pentagon edge groups for K3 input; the
**fifth edge $(P_5, P_1)$ is asserted to close by the Pentagon
coboundary relation $\sum_{e \in E(\Pi)} \partial_e \omega = 0$.**
V84 attacks the fifth-edge coboundary closure along five sharp angles,
applying AP-CY57 (no narration without construction), AP-CY60
(constructions are not corollaries of one functor), AP-CY61
(every wrong claim contains the ghost of a true theorem), and the
Stasheff $K_n$-coherence framework. Phase 2 heals into a Platonic
restatement separating the *four-edge cocycle ledger* from the
*$K_5$-coherence cell*.

---

## §1. Setup and the precise V69 fifth-edge claim

V69's V49\* assigns Pentagon edges as follows:

| Edge | Closure morphism | Cohomology theory |
|---|---|---|
| $(P_1, P_2)$ | $\Phi_{\mathrm{Borch}}$ | Automorphic forms on $\Sp_4(\Z)$ |
| $(P_3, P_4)$ | $\Phi_{\mathrm{Borch}}$ | (idem) |
| $(P_2, P_3)$ | $\Phi_{\mathrm{EK}}$ | Drinfeld twist deformation cohomology |
| $(P_4, P_5)$ | $\Phi_{\mathrm{FH}}$ | Cyclic homology $\mathrm{HC}_*$ |
| $(P_5, P_1)$ | (by Pentagon coboundary) | --- |

The asserted closure of $(P_5, P_1)$:

> *Given that the four other edges close as cocycles via three
> morphisms, the fifth edge $\partial_{P_5 P_1} \omega$ is forced to
> vanish by the relation $\sum_e \partial_e \omega = 0$.*

The slogan: **"closing four edges automatically closes the fifth."**

This is a Mac Lane–style coherence step at the cocycle level: if a
2-cocycle decomposes by edge, and four edge components are cocycles,
the sum-relation forces the fifth. V84 asks: under what hypotheses is
this automatic, and what hypotheses does V69 implicitly assume?

---

## §2. PHASE 1 --- ATTACK (five angles)

Per AP-CY61, every angle answers (a) what is right, (b) what is
wrong, (c) what is the correct mathematical relationship.

### A1. Cocycle vs. chain-homotopy: is the closure of the four edges *strict* or *up to coherent homotopy*?

**Claim.** V69 invokes Pentagon coboundary $\sum_e \partial_e \omega = 0$
as if it were a strict identity in a 2-cocycle group $Z^2$. But the
closure mechanisms supplied by V49\* are NOT strict-equality
certifications:

- **Route (i) Borcherds** certifies vanishing of the *scalar
  projection* $\tr_{Z(\mathcal C)} \omega_e$ for the two
  scalar-projecting edges; this is vanishing in $\Z$, not vanishing of
  $\omega_e$ as a chain.
- **Route (ii) EK** certifies vanishing of the *Drinfeld twist class*
  $[\omega_{P_2 P_3}]_{\mathrm{tw}}$; this is vanishing in
  $H^2_{\mathrm{tw}}$, i.e., vanishing modulo a Drinfeld-twist
  coboundary.
- **Route (iii) FH + V11** certifies vanishing *up to a coherent
  cyclic-Hochschild homotopy*; V60/V63's V11 Pillar α explicitly says
  the chain map $\eta_{45}$ commutes with differentials *up to a
  coherent (co-)homotopy*, not strictly.

If the four edges close only "up to homotopy", the Pentagon
coboundary relation $\sum_e \partial_e \omega = 0$ at the strict
chain level need not force the fifth edge to vanish; instead, it
forces $\partial_{P_5 P_1} \omega$ to equal a chain whose class is
a sum of three coherent-homotopy correction terms. This is a
**higher-arity correction**, not vanishing.

**(a) Right.** The Pentagon coboundary relation $\sum_e \partial_e
\omega = 0$ DOES hold strictly in the chain complex
$C^*_{\mathrm{ch,alg}}(V_{\Lambda_{K3}}, V_{\Lambda_{K3}})$ at the
defining-cocycle level: this is just $d^2 = 0$ for the chiral
Hochschild differential, expanded by edge. So formally the
five-fold sum vanishes as a chain identity.

**(b) Wrong.** What V69 conflates is *vanishing of the cocycle class*
with *vanishing of the cocycle chain*. The four edge closures
certify class-vanishing in their respective target cohomology
theories; pulling that back to chain-level vanishing requires
choosing explicit coboundary-witness chains $h_e$ such that
$\omega_e = \partial h_e$ at the chain level. The pulled-back chain
identity is

$$
\partial_{P_5 P_1} \omega \;=\; -\sum_{e \neq (P_5 P_1)} \partial_e \omega
\;=\; -\sum_{e \neq (P_5 P_1)} \partial(\partial h_e) \;=\; 0
$$

where the second equality uses $\omega_e = \partial h_e$ (chain
witness) and the third uses $\partial^2 = 0$. So strictly, IF chain
witnesses $h_e$ are chosen, the fifth edge IS forced to be a
boundary of $-\sum h_e$.

But the three closure morphisms produce target-side witnesses, not
source-side witnesses. To pull back, we need each $\Phi_*$ to be a
chain map admitting a *section* (or at least a quasi-inverse) that
returns a source-side $h_e$. None of $\Phi_{\mathrm{Borch}},
\Phi_{\mathrm{EK}}, \Phi_{\mathrm{FH}}$ is invertible; they are
projections / lifts to disjoint cohomology theories. So the
pullback is at best a *zigzag of quasi-isomorphisms*, with each
zigzag step contributing its own coherent homotopy.

**(c) Correct relationship.** The fifth-edge closure is **not
automatic at the strict-chain level**; it is automatic only at the
cohomology-class level *provided the three target cohomology
theories jointly detect the chain-level cocycle*. The precise
statement is:

> **Fifth-edge closure (refined).** $[\omega_{P_5 P_1}] = 0 \in H^2$
> iff $[\omega_e] = 0 \in H^2$ for $e \in \{(P_1 P_2), (P_3 P_4),
> (P_2 P_3), (P_4 P_5)\}$ AND the three closure morphisms
> $\Phi_{\mathrm{Borch}}, \Phi_{\mathrm{EK}}, \Phi_{\mathrm{FH}}$
> jointly form a *detecting family* for $H^2(\mathrm{SC}^{\mathrm{ch,top}};
> \mathfrak{aut})$ at K3 input, i.e., the joint kernel of
> $(\Phi_{\mathrm{Borch}})_*, (\Phi_{\mathrm{EK}})_*, (\Phi_{\mathrm{FH}})_*$
> on $H^2$ is zero.

The detecting-family hypothesis is NOT free: it is a non-trivial
property of the triple of morphisms. V69 invokes the coboundary
relation as if it were a free Mac Lane theorem, but the actual
content is the *joint detection* of $H^2$ by the three projections.

**Ghost theorem (extracted per AP-CY61):**

> **Ghost (joint-detection coboundary).** Let $A = V_{\Lambda_{K3}}$
> and let $\omega \in Z^2(C^*_{\mathrm{ch,alg}}(A,A))$ be the
> Pentagon cocycle decomposed by edge. Suppose the three morphisms
> $\Phi_{\mathrm{Borch}}, \Phi_{\mathrm{EK}}, \Phi_{\mathrm{FH}}$
> form a $H^2$-detecting family at K3 input. Then closure of four
> edges in their respective targets implies closure of the fifth
> edge in $H^2$ via the Pentagon coboundary relation. The hypothesis
> "detecting family" is a separate input, NOT a consequence of the
> three morphisms existing.

### A2. Pentagon vs. higher polygons: $A_5$ vs. $A_6, A_7, \ldots$

**Claim.** At $E_1$ chain level, only the Pentagon ($A_5$) relation is
needed for associativity coherence at the *binary-product* level. But
chain-level $A_\infty$ algebras (Stasheff) have an $A_n$-relation for
every $n \geq 2$, parameterized by the Stasheff associahedron $K_n$.
$K_5$ has dimension 3; the Pentagon is the boundary of $K_4$ (which
is a pentagon, i.e., a 2-cell). So "Pentagon" is the *2-dimensional*
$A_4$-coherence, not the $A_5$-coherence. V49\* covers Mac Lane's
Pentagon ($K_4$); what about $K_5, K_6, \ldots$?

**(a) Right.** Stasheff's $K_n$ associahedron parametrises the
$n$-fold associativity coherences. At $E_1$ chain level, the full
$A_\infty$-structure requires a coherent system of $K_n$-cells for
all $n$. Mac Lane's Pentagon is the 2-cell $K_4$ (a pentagon-shaped
polytope). Closure of $K_4$ does NOT imply closure of $K_5$ (a
3-dimensional polytope with 14 vertices, 21 edges, 9 faces). At each
$n$, a new coherence cocycle could appear.

**(b) Wrong.** V49\* and V69 are statements about the **lowest
non-trivial coherence cocycle**, namely the Pentagon $K_4$. The
$A_4$-cocycle $\omega \in H^2$ is the Mac Lane–Stasheff obstruction
to strict associativity. Higher Stasheff cocycles $\omega^{(n)} \in
H^{n-2}$ for $n \geq 5$ live in higher cohomology degrees and are
*not* what Pentagon-at-$E_1$ is about.

V69's statement is correctly scoped to $K_4$. It does NOT claim
closure of $K_5, K_6, \ldots$. The fifth-edge coboundary closure is
purely about the $K_4$-cocycle $\omega$, decomposed into its five
edge contributions ($K_4$ has 5 edges as a pentagon-shaped 2-cell).

**(c) Correct relationship.** Pentagon-at-$E_1$ at K3 input closes
the $K_4$-cocycle. **The $K_5, K_6, \ldots$ Stasheff cells are a
separate frontier.** Stasheff's theorem (1963): if the $K_n$-cocycles
are killed for all $n \geq 4$, the $A_\infty$-structure is
quasi-equivalent to a strict associative one. Killing only $K_4$
gives an $A_4$-algebra (associative up to homotopy with explicit
pentagon-witness $h$). Higher $K_n$ remains.

**Ghost theorem:**

> **Ghost (Stasheff tower scope).** Pentagon-at-$E_1$ V49\* closes
> $K_4$; Stasheff $K_5, K_6, \ldots$ are independent obstructions
> living in higher cohomology degrees. The fifth-edge coboundary
> closure of V69 is about the five 1-cells of $K_4$, NOT about
> $K_5$. Honest scope: $K_4$-coherence at K3 input. Open: $K_5$ and
> higher.

This **clarifies** V49\*'s scope without weakening it: V49\* is
exactly an $A_4$-coherence statement at K3, not an $A_\infty$
coherence statement. The fifth-edge closure operates within the
$K_4$ cell; nothing in V69 propagates to $K_5$.

### A3. Strict vs. lax Pentagon: do the four edge closures produce a non-trivial 3-cell?

**Claim.** V49\* assumes the four edge-group certifiers give STRICT
Pentagon edges (closure of $\omega_e$ as a strict 0-class). But each
of the three closure morphisms is *lax* in a precise sense:
- $\Phi_{\mathrm{Borch}}$ is a lift through automorphic forms; the
  trace-match $c_5(0)/2 = 5$ is a numerical identity but the
  scalar-projection of $\omega_e$ to $\Z$ collapses higher data.
- $\Phi_{\mathrm{EK}}$ is a lax functor (Drinfeld 1989: twist
  coherence holds up to gauge equivalence, not strictly).
- $\Phi_{\mathrm{FH}}$ is a chain map up to coherent homotopy
  (V60/V63 explicit).

If any closure is lax, the fifth-edge coboundary closure does not
produce strict vanishing; it produces a 3-cell $\eta_{P_5 P_1}^{(3)}$
that may be non-trivial. This 3-cell IS a Stasheff $K_5$-component.
So V69's implicit promotion of "lax four-edge closure" to "strict
fifth-edge vanishing" is precisely the same conflation as AP-CY30
(*factored $\neq$ solved for higher coherence*).

**(a) Right.** AP-CY30 is the right precedent: the Zamolodchikov
tetrahedron equation does NOT follow from pairwise YBE for the
2-particle R-matrix; the three-particle S-operator obstructs. The
analogue here: closure of four Pentagon edges does NOT automatically
imply closure of the fifth at the strict chain level if the four
closures are lax. The 3-cell that emerges is the Stasheff
$K_5$-component, which is independent.

**(b) Wrong.** The 3-cell that emerges from a lax four-edge closure
is NOT a $K_4$-edge contribution; it lives in $H^3$, NOT $H^2$. The
Pentagon cocycle $\omega \in H^2$ is the $K_4$-coherence. The 3-cell
$\eta^{(3)}$ lives in $H^3$ and is the $K_5$-coherence. So the
fifth-edge coboundary closure within $H^2$ may STILL succeed, with
the price being a non-trivial 3-cell in $H^3$ that obstructs
$K_5$-coherence.

**(c) Correct relationship.** Lax closure of four Pentagon edges in
$H^2$ implies closure of the fifth edge in $H^2$ MODULO a
$K_5$-cocycle $\eta^{(3)} \in H^3$. The cohomological precise
statement:

> **Fifth-edge closure (lax-corrected).** With four edges closed
> laxly via $\Phi_{\mathrm{Borch}}, \Phi_{\mathrm{EK}},
> \Phi_{\mathrm{FH}}$, the fifth-edge class
> $[\omega_{P_5 P_1}] \in H^2$ vanishes iff the induced
> $K_5$-cocycle $[\eta^{(3)}] \in H^3$ also vanishes. The
> $K_5$-cocycle is the Stasheff associahedron's first higher
> coherence; its vanishing is a SEPARATE check beyond the four-edge
> $K_4$ ledger.

**Ghost theorem:**

> **Ghost (lax-Pentagon $\rightarrow$ Stasheff $K_5$).** Lax closure
> of $K_4$-edges produces a $K_5$-cocycle $\eta^{(3)} \in H^3$ as
> an obstruction. V69's fifth-edge coboundary closure within $H^2$
> is a TRUE statement; the residual $K_5$-cocycle is a SEPARATE,
> higher-degree obstruction. V49\* should be supplemented with an
> explicit $K_5$-cocycle audit.

This is consistent with A2: the Stasheff tower is the proper home
for higher coherences, and V49\*'s natural extension is to track the
$K_5$-cocycle.

### A4. Mac Lane coherence: is Pentagon $\Rightarrow$ all higher polygons valid at chain level?

**Claim.** Mac Lane's pentagon coherence theorem (1963) says:
**for a monoidal category, the Pentagon implies all higher polygon
coherences.** This is the foundational result that justifies stopping
at $K_4$. But Mac Lane's theorem is for STRICT-OBJECT monoidal
categories; for chain-level $E_1$ algebras (where the underlying
object is a chain complex with a non-strict differential), Mac Lane's
theorem requires an *$A_\infty$-refinement* (Stasheff 1963: pentagon
$K_4$ alone is the $A_4$-relation, NOT all higher $A_n$). So V69's
implicit appeal to "Mac Lane coherence forces the fifth edge" is
**misapplied**: Mac Lane gives strict coherence for monoidal
categories, not chain-level $E_1$ algebras.

**(a) Right.** Mac Lane 1963 (the monoidal-category coherence theorem)
shows that for a monoidal category, the pentagon $K_4$ + triangle
($K_3$, the unit coherence) imply all higher $K_n$ coherences at the
*categorical level*. This is correct for strict-object monoidal
categories.

**(b) Wrong.** Mac Lane's theorem is at the *categorical* (1-cell /
2-cell) level, not at the chain-complex level. For a chain-level
$E_1$ algebra (= an $A_\infty$ algebra), Stasheff's 1963 theorem
gives a different picture: the $A_n$-relations for all $n$ are
*independent generators*, and only after passing to the homotopy
category does Mac Lane's coherence apply. The chain-level fifth-edge
coboundary closure invokes Pentagon $K_4$ at the chain level, where
Mac Lane's argument requires an explicit $A_\infty$-extension.

**(c) Correct relationship.** Mac Lane's coherence theorem applies
to V49\* at the *cohomology-class* level (where $A_\infty \to
A$-strict equivalence holds). At the *chain* level, V49\* must
either (1) supply explicit $h_e$ chain witnesses for each closure
morphism, or (2) work explicitly in the homotopy category
$\mathrm{Ho}(C^*_{\mathrm{ch,alg}})$ where Mac Lane applies. Both
options require declaration; V69 leaves it implicit.

**Ghost theorem:**

> **Ghost (Mac Lane $\rightarrow$ Stasheff bridge).** At cohomology
> level, Mac Lane's pentagon coherence justifies the fifth-edge
> coboundary closure. At chain level, the bridge requires either
> explicit $h_e$ chain witnesses or passage to
> $\mathrm{Ho}(C^*_{\mathrm{ch,alg}})$. V69's fifth-edge closure
> implicitly works at the cohomology level; the chain-level lift
> requires the Stasheff $A_\infty$-machinery.

This supports the refined statement: V49\* is valid at the
*cohomology-class* level. Chain-level upgrade requires a separate
construction (either $h_e$ witnesses or homotopy-category passage).

### A5. Edge-group disjointness vs. non-overlap: count check

**Claim.** V69 claims the three closure morphisms certify *pairwise-
disjoint* edge groups. But the Pentagon has 5 edges and three groups
means at least one group has $\geq 2$ edges (by pigeonhole). V69's
table assigns:
- Borcherds: 2 edges $\{(P_1 P_2), (P_3 P_4)\}$;
- EK: 1 edge $\{(P_2 P_3)\}$;
- FH+V11: 1 edge $\{(P_4 P_5)\}$;
- coboundary: 1 edge $\{(P_5 P_1)\}$.

Disjointness is satisfied numerically (no edge appears in two
groups). But: the Borcherds group has TWO edges $\{(P_1 P_2),
(P_3 P_4)\}$. Why these two? Are they jointly closed by the same
mechanism (one trace-match), or are they two independent closures by
the same morphism? If the latter, V69's three-route count might be
under-counting (Borcherds = 2 closures, not 1).

**(a) Right.** Pigeonhole forces at least one group to have $\geq 2$
edges. V69's assignment puts both scalar-projecting edges in the
Borcherds group. The two edges $\{(P_1 P_2), (P_3 P_4)\}$ are
EQUIVALENT under the scalar-projection $\tr_{Z(\mathcal C)}$: both
project to the same $\Z$-valued integer. So the trace-match
$c_5(0)/2 = 5$ closes BOTH simultaneously via a single equation.
This is one closure, two edges.

**(b) Wrong.** The two edges are distinct as 1-cells in $K_4$; they
are equivalent only under the projection $\tr_{Z(\mathcal C)}$.
Strict edge-by-edge closure would require closing each edge as a
separate cocycle. V69's collapsing of the two scalar-projecting
edges into one Borcherds closure is mathematically correct *only at
the projected level* (in the image of $\tr_{Z(\mathcal C)}$). At the
chain level, the two edges $\omega_{P_1 P_2}$ and $\omega_{P_3 P_4}$
are different chains; their projections coincide but the chains
themselves do not.

**(c) Correct relationship.** V69's edge-architecture table is
correct *modulo the scalar projection*. At the chain level, the
table should read:

| Edge | Closure level | Witness |
|---|---|---|
| $(P_1 P_2)$ | scalar projection $\Z$ | $c_5(0)/2 = 5$ |
| $(P_3 P_4)$ | scalar projection $\Z$ | $c_5(0)/2 = 5$ (same equation) |
| $(P_2 P_3)$ | matrix class $H^2_{\mathrm{tw}}$ | EK twist coherence |
| $(P_4 P_5)$ | cyclic class $\mathrm{HC}_*$ | V11 Pillar α $\eta_{45}$ |
| $(P_5 P_1)$ | (forced by coboundary $H^2$) | --- |

Pairwise disjointness holds at the *projection-target* level: scalar,
matrix, cyclic, coboundary-forced. But edge-by-edge chain-level
disjointness is an OVER-CLAIM. The honest statement: each closure
morphism certifies vanishing of a *projection* of one or two edges,
NOT vanishing of the chains themselves.

**Ghost theorem:**

> **Ghost (projection vs. chain disjointness).** V49\*'s pairwise-
> disjoint edge groups are at the PROJECTION level
> (scalar/matrix/cyclic), NOT at the chain level. The Pentagon
> coboundary closes the fifth edge IN COHOMOLOGY $H^2$ at K3, given
> that the four other edge classes vanish in their respective target
> cohomology theories AND the three projections jointly detect $H^2$.
> Chain-level closure requires explicit chain witnesses, not supplied
> by V69.

This SHARPENS V49\*'s independence claim: independence is at the
projection level (three different cohomology theories), NOT at the
edge level (some projections cover multiple edges).

---

## §3. WHAT SURVIVES

| Attack | Verdict | Implication for V49\* |
|---|---|---|
| A1: cocycle vs. chain-homotopy | SURVIVES with **detecting-family hypothesis** added | Fifth-edge closure requires explicit joint-detection assumption |
| A2: Pentagon vs. $K_5, K_6, \ldots$ | SURVIVES; scope is correctly $K_4$-coherence | V49\* is an $A_4$-statement; $K_5$ remains open |
| A3: strict vs. lax Pentagon | SURVIVES with **$K_5$-cocycle audit** added | Lax closure produces a $K_5$-cocycle $\eta^{(3)} \in H^3$ as a SEPARATE check |
| A4: Mac Lane vs. Stasheff bridge | SURVIVES at cohomology level; chain-level requires Stasheff witnesses | V49\* is correct in $H^2$; chain-level lift needs $h_e$ |
| A5: edge-group disjointness | SURVIVES at **projection** level, NOT at chain level | Disjointness is in the projection targets, not in the edges themselves |

**No attack collapses V69.** The fifth-edge coboundary closure is
SOUND at the cohomology-class level $H^2$, **conditional on**:
1. The three morphisms $\Phi_{\mathrm{Borch}}, \Phi_{\mathrm{EK}},
   \Phi_{\mathrm{FH}}$ form a *detecting family* for $H^2$ at K3 input.
2. The closure scope is restricted to the $K_4$-coherence cocycle
   $\omega \in H^2$; the $K_5$-coherence cocycle $\eta^{(3)} \in H^3$
   is a separate audit.
3. Disjointness of the three closure morphisms is at the
   projection-target level (scalar, matrix, cyclic), not at the
   chain-level edge level.
4. Chain-level closure (vs. cohomology-level closure) requires
   explicit Stasheff $h_e$ chain witnesses or passage to
   $\mathrm{Ho}(C^*_{\mathrm{ch,alg}})$ where Mac Lane applies.

The four conditions are NOT free; each is a substantive hypothesis
that V69 leaves implicit. They are the seeds of true theorems (the
ghosts of A1-A5).

---

## §4. PHASE 2 --- FOUNDATIONAL HEAL

### V49\*\* (Pentagon-at-$E_1$ for K3 input, V84-refined edge-architecture)

> **Theorem (V84-refined; \ClaimStatusConjectured, cond.\ on
> FM164, FM161, detecting-family at K3, $K_5$-cocycle vanishing).**
> Let $A = V_{\Lambda_{K3}}$ and let $[\omega]_{K3} \in H^2(\mathrm{SC}^{\mathrm{ch,top}};
> \mathfrak{aut})$ be the $K_4$-coherence Pentagon cocycle. Suppose:
>
> **(H1) Four-edge ledger.** Three closure morphisms certify
> vanishing of four edge classes at the projection-target level:
> - $\Phi_{\mathrm{Borch}}$ certifies $\tr_{Z(\mathcal C)}
>   [\omega_{P_1 P_2}] = \tr_{Z(\mathcal C)} [\omega_{P_3 P_4}] = 0
>   \in \Z$ via $c_5(0)/2 = 5$;
> - $\Phi_{\mathrm{EK}}$ certifies $[\omega_{P_2 P_3}]_{\mathrm{tw}}
>   = 0 \in H^2_{\mathrm{Drinfeld-tw}}$ via Drinfeld twist coherence
>   on the V38 R-matrix;
> - $\Phi_{\mathrm{FH}}$ certifies $\xi_{45}([\omega_{P_4 P_5}]) = 0
>   \in \mathrm{HC}_*^-$ via V11 Pillar α $\eta_{45}$ chain map.
>
> **(H2) Detecting family.** The three induced maps
> $(\Phi_{\mathrm{Borch}})_*, (\Phi_{\mathrm{EK}})_*,
> (\Phi_{\mathrm{FH}})_*$ on $H^2(C^*_{\mathrm{ch,alg}}(A,A))$ are
> jointly injective; equivalently, their joint kernel on $H^2$ is
> zero.
>
> **(H3) $K_5$-cocycle vanishing.** The Stasheff $K_5$-cocycle
> $[\eta^{(3)}] \in H^3(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$
> vanishes (separate audit; not contained in the four-edge ledger).
>
> Then the fifth edge $[\omega_{P_5 P_1}] = 0$ in $H^2$ via the
> Pentagon coboundary relation $\sum_e \partial_e \omega = 0$, and
> hence $[\omega]_{K3} = 0$ in $H^2$.

This is the V84 PLATONIC IDEAL. Differences from V49\* (V69):
- **(H2) detecting family** made explicit (was implicit in V69).
- **(H3) $K_5$-cocycle audit** added (V69 was silent on Stasheff
  $K_5$).
- **Disjointness restated** as projection-target-level, not
  edge-level.
- **Cohomology-class closure** vs. chain-level closure separated;
  V49\*\* lives in $H^2$, chain-level statement requires Stasheff
  witnesses (open).

### What is NOT proved by V49\*\*

- The detecting-family hypothesis (H2) is plausible but unverified;
  it is a non-trivial property of the triple $(\Phi_{\mathrm{Borch}},
  \Phi_{\mathrm{EK}}, \Phi_{\mathrm{FH}})$ that requires its own
  argument.
- The $K_5$-cocycle (H3) is a separate frontier; existing K3 results
  do not address it.
- Chain-level closure (vs. cohomology-class closure) requires
  explicit Stasheff $h_e$ witnesses, also open.

---

## §5. Strict-vs-lax verdict and $K_5$-coherence verification

**Strict vs. lax verdict.** All three closure morphisms are LAX:
- Borcherds: lax in the sense that scalar projection collapses
  matrix/cyclic data.
- EK: lax in the sense that Drinfeld twist coherence is up to gauge.
- FH+V11: lax in the sense that V11 Pillar α $\eta_{45}$ is a chain
  map up to coherent (co-)homotopy.

Hence V49\*\* operates at the **cohomology-class** level, not the
strict-chain level. The Pentagon coboundary fifth-edge closure is
valid in $H^2$ provided (H1) + (H2) hold; chain-level closure
requires Stasheff $h_e$ witnesses (open).

**$K_5$-coherence verification.** The Stasheff $K_5$ associahedron
has dimension 3, with 14 vertices (= Catalan $C_4 = 14$), 21 edges,
9 2-faces. Its cocycle $\eta^{(3)} \in H^3(\mathrm{SC}^{\mathrm{ch,top}};
\mathfrak{aut})$ is the obstruction to extending an $A_4$-coherent
structure to an $A_5$-coherent structure. For K3 input, the
$K_5$-cocycle has not been audited; V49\*\* assumes (H3) as a
separate hypothesis.

The minimal extension to verify (H3): compute $[\eta^{(3)}]$ at K3
input and check vanishing. The obvious approach is via three
sub-routes paralleling V49\*'s edge-architecture:
- $\Phi_{\mathrm{Borch}}$ sends $[\eta^{(3)}]$ to a degree-3 class
  in $H^3(\mathcal A_*(\Sp_4(\Z))) = 0$ (automorphic forms have
  no degree-3 cohomology in this range; V20-style argument).
- $\Phi_{\mathrm{EK}}$ sends $[\eta^{(3)}]$ to $H^3_{\mathrm{tw}}$,
  which is computable via the Drinfeld associator (KZ equation
  monodromy at higher orders).
- $\Phi_{\mathrm{FH}}$ sends $[\eta^{(3)}]$ to $\mathrm{HC}_*^-$ at
  degree 3, which is computable via V11 Pillar α at higher
  Hochschild degrees (the $(P_4, P_5)$ chain map extends to a
  $(P_4, P_5)$-cube that controls $H^3$).

This is the V84 conjectural pathway for closing (H3); it is not
verified in V84 and remains open for a future wave (V85-V90 frontier).

---

## §6. Per-route certification with explicit chain map (cohomology level)

Restating V69's per-route chain maps with the V84 refinements
(detecting-family + lax-projection clarifications):

### Route (i) Borcherds (scalar projection)

$$
(\Phi_{\mathrm{Borch}})_* : H^2(C^*_{\mathrm{ch,alg}}(V_{\Lambda_{K3}},
V_{\Lambda_{K3}})) \;\xrightarrow{\tr_{Z(\mathcal C)}}\;
\Z \;\hookrightarrow\; \mathcal A_5(\Sp_4(\Z) \backslash \mathfrak H_2)
$$

certifies $\tr_{Z(\mathcal C)}[\omega_{P_1 P_2}] =
\tr_{Z(\mathcal C)}[\omega_{P_3 P_4}] = 0$ via $c_5(0)/2 = 5$ (V20).
**Lax.** Two edges collapse to one scalar identity.

### Route (ii) EK (Drinfeld-twist projection)

$$
(\Phi_{\mathrm{EK}})_* : H^2(C^*_{\mathrm{ch,alg}}(V_{\Lambda_{K3}},
V_{\Lambda_{K3}})) \;\xrightarrow{J_{\mathrm{EK}}\text{-twist class}}\;
H^2_{\mathrm{Drinfeld-tw}}(\mathfrak{Heis}^{24} \oplus \mathfrak g_{\mathrm{ADE}})
$$

certifies $[\omega_{P_2 P_3}]_{\mathrm{tw}} = 0$ via the standard
Drinfeld twist coherence (Drinfeld 1989). **Lax.** Up to gauge.

### Route (iii) FH + V11 (cyclic projection)

$$
(\Phi_{\mathrm{FH}})_* : H^2(C^*_{\mathrm{ch,alg}}(V_{\Lambda_{K3}},
V_{\Lambda_{K3}})) \;\xrightarrow{\xi_{45}\text{ via } \eta_{45}}\;
\mathrm{HC}_*^-(\int_{S^1} V_{\Lambda_{K3}})
$$

with $\eta_{45}$ the V11 Pillar α cyclic-averaging chain map
$\eta_{45}([a_0 | \cdots | a_n]) = \frac{1}{(n+1)!} \sum_{\sigma \in C_{n+1}}
\mathrm{sgn}(\sigma) a_{\sigma(0)} \otimes \cdots \otimes a_{\sigma(n)}$;
certifies $\xi_{45}([\omega_{P_4 P_5}]) = 0$. **Lax.** Up to coherent
(co-)homotopy.

### Pentagon coboundary fifth-edge closure (V84-refined)

Given (H1) four-edge closures in three target cohomology theories
and (H2) detecting family for $H^2$, the Pentagon coboundary relation

$$
\partial_{P_5 P_1}[\omega] \;=\; -\sum_{e \neq (P_5 P_1)} \partial_e [\omega]
\;\in\; H^2
$$

forces $[\omega_{P_5 P_1}] = 0 \in H^2$. **Cohomology-class level
only**; chain-level lift requires Stasheff $h_e$ witnesses (open).
Subject to (H3) $K_5$-cocycle vanishing for full $A_5$-coherence.

---

## §7. v3.4 directive

V69 produced v3 directive (frontier rearchitecture at non-K3 inputs).
V84 sharpens it:

> **v3.4 directive.** Pentagon-at-$E_1$ at K3 closes in the
> V84-refined edge-architecture form V49\*\*: four edges via three
> closure morphisms into pairwise-disjoint cohomology theories, fifth
> edge by Pentagon coboundary in $H^2$. Closure is at the
> COHOMOLOGY-CLASS level, conditional on (H1) four-edge ledger
> (V49\*); (H2) detecting family for $H^2$ at K3 (open audit); (H3)
> Stasheff $K_5$-cocycle vanishing at K3 (open audit). For non-K3
> $\mathrm{CY}_3$ inputs (Class B per V55), each input requires its
> own (H1) + (H2) + (H3) audit; the Class B challenge is to
> identify three pairwise-disjoint closure morphisms forming a
> detecting family AND verify the $K_5$-cocycle separately.
>
> Honest scope: V49\*\* is an $A_4$-coherence statement at K3 input
> at the cohomology-class level. Chain-level $A_4$-coherence (with
> explicit Stasheff $h_e$ witnesses) and $A_5$-coherence (with
> $K_5$-cocycle vanishing) are SEPARATE frontiers requiring their
> own attack-and-heal cycles (V85, V86, V87 candidate waves).

### v3.4 inscription targets

**T1.** Augment `MASTER_PUNCH_LIST.md` V49 section:
*"V49\*\*: Pentagon-at-$E_1$ for K3, V84 edge-architecture. Refines
V49\* by separating the four-edge cocycle ledger (cohomology-class
closures via three projection-target morphisms) from the
detecting-family hypothesis (H2: joint injectivity of three
projections on $H^2$) and the Stasheff $K_5$-cocycle audit (H3:
separate frontier in $H^3$). Disjointness is at the projection-target
level (scalar/matrix/cyclic), not at the edge level. Closure is at
the cohomology-class level; chain-level lift requires Stasheff
$h_e$ witnesses (open)."*

**T2.** Add new AP entry to the Vol III AP catalogue:

> **AP-CY69. Lax-Pentagon vs. strict-Pentagon edge closure.** When
> certifying closure of Pentagon-edge classes via lax morphisms
> (projection to scalar/matrix/cyclic targets, twist-coherence,
> chain-up-to-homotopy), the resulting fifth-edge closure is valid
> only at the COHOMOLOGY-CLASS level $H^2$, not at the strict-chain
> level. Chain-level fifth-edge closure requires explicit Stasheff
> $h_e$ chain witnesses; lax closures generate a Stasheff
> $K_5$-cocycle in $H^3$ as a separate higher-coherence
> obstruction. Counter: before claiming fifth-edge coboundary
> closure, identify whether each four-edge closure is strict
> (chain-level) or lax (cohomology-level), state the level of the
> fifth-edge closure accordingly, and audit the $K_5$-cocycle
> separately.

**T3.** Add new AP entry:

> **AP-CY70. Detecting-family hypothesis for joint
> projection-closure.** When closing a cohomology cocycle by joint
> vanishing of multiple projections to disjoint cohomology
> theories, the joint projection family must be a DETECTING family
> (jointly injective on the relevant $H^*$). The detecting-family
> property is a non-trivial hypothesis, NOT a consequence of the
> projections existing or being pairwise disjoint. Counter: before
> any joint-projection cohomology-closure argument, explicitly
> formulate the detecting-family hypothesis and either prove it or
> declare it open.

**T4.** Update `notes/INDEPENDENT_VERIFICATION.md` with the V84
edge-architecture as the model entry: independent verification of a
cocycle's vanishing via three projections requires a *detecting
family* certification, not just three pairwise-disjoint
projection-target morphisms. The decorator's `disjoint_rationale`
should include a sentence: *"the three projections form a detecting
family for $H^2$ at K3 input, certified by [argument]."*

**T5.** Cross-volume sweep. The V84 refinements do NOT change Vol I
or Vol II dependencies beyond V49\*'s; the V20 Universal Trace
Identity remains the load-bearing cross-volume citation, now used
to certify the *scalar projection* of two Pentagon edges
($\{(P_1 P_2), (P_3 P_4)\}$) as a single $\Z$-valued identity. The
V11 Pillar α (Vol II Pentagon) certifies the *cyclic projection* of
one edge ($(P_4 P_5)$). Detecting-family hypothesis (H2) and
Stasheff $K_5$-cocycle (H3) are NEW cross-volume targets requiring
audits in Vol III at K3 input.

**T6.** New candidate wave queue:
- **V85**: detecting-family hypothesis (H2) audit at K3 input. Show
  $(\Phi_{\mathrm{Borch}})_*, (\Phi_{\mathrm{EK}})_*,
  (\Phi_{\mathrm{FH}})_*$ are jointly injective on $H^2$.
- **V86**: Stasheff $K_5$-cocycle (H3) audit at K3 input. Compute
  $[\eta^{(3)}] \in H^3$ at $V_{\Lambda_{K3}}$ and verify vanishing.
- **V87**: chain-level lift of V49\*\* via explicit Stasheff $h_e$
  witnesses for each closure morphism.

---

## §8. Coda

V69 produced V49\*'s edge architecture, with the fifth edge $(P_5,
P_1)$ closing by Pentagon coboundary. V84 attacked the fifth-edge
closure along five sharp angles per AP-CY61 (cocycle vs.
chain-homotopy; Pentagon vs. higher Stasheff; strict vs. lax;
Mac Lane vs. Stasheff; edge-group vs. projection disjointness). All
five attacks SURVIVED, each producing a ghost theorem that REFINES
rather than rejects V49\*.

The deepest finding is the separation of the **four-edge cocycle
ledger** (V49\*'s achievement) from the **$K_5$-coherence cell**
(V84's identified frontier). V49\*\* is a *cohomology-class* level
statement in $H^2$, conditional on:

- **(H1)** four-edge closures in three target cohomology theories
  (V49\*'s achievement);
- **(H2)** detecting-family hypothesis: three projections jointly
  injective on $H^2$ at K3 (NEW, open);
- **(H3)** Stasheff $K_5$-cocycle vanishing in $H^3$ at K3 (NEW,
  open).

The fifth-edge coboundary closure is **VALID** in $H^2$ given
(H1)+(H2); it is **NOT AUTOMATIC** as Mac Lane–style coherence
would suggest. The Mac Lane theorem applies at the categorical
level; the chain-level / cohomology-level statement requires the
Stasheff $A_\infty$-machinery and the detecting-family hypothesis.

V84 produces three v3.4 directives (T1-T3 inscription targets, with
T2 = AP-CY69 lax-Pentagon edge closure and T3 = AP-CY70 detecting-
family hypothesis as new AP entries). It identifies three new
candidate waves (V85, V86, V87) for the detecting-family audit, the
$K_5$-cocycle audit, and the chain-level Stasheff $h_e$ lift.

V49\*\* survives the V84 attack as a refined, honestly-scoped
$A_4$-cohomology-class theorem. It is strictly stronger than V49\*
in transparency (explicit hypotheses) and strictly weaker in
implicit-claim scope (no chain-level closure, no $K_5$-coherence).
This is the Beilinson principle in action: each attack-and-heal
cycle sharpens the ledger of what is genuinely proved vs. what is
genuinely assumed.

The single-line memorable form:

> Pentagon-at-$E_1$ at K3 fifth-edge coboundary closes in $H^2$
> conditional on (H1) four-edge ledger via three projection-target
> morphisms, (H2) detecting-family hypothesis (joint injectivity on
> $H^2$), (H3) Stasheff $K_5$-cocycle vanishing in $H^3$. Lax
> closures generate the $K_5$-cocycle as a separate higher-coherence
> obstruction; Mac Lane coherence applies at the cohomology-class
> level only. Per AP-CY69 and AP-CY70.

---

## §9. Final report (for caller)

**Fifth-edge coboundary closure status.** SURVIVES at the
cohomology-class level $H^2$, conditional on (H1) four-edge ledger
(V49\* achievement) + (H2) detecting-family hypothesis (NEW,
explicit, open audit) + (H3) Stasheff $K_5$-cocycle vanishing in
$H^3$ (NEW, explicit, open audit). NOT automatic via Mac Lane
coherence; requires Stasheff $A_\infty$-machinery for chain-level
lift.

**Strict vs. lax verdict.** All three closure morphisms
($\Phi_{\mathrm{Borch}}, \Phi_{\mathrm{EK}}, \Phi_{\mathrm{FH}}$) are
LAX:
- Borcherds: scalar projection collapses higher data;
- EK: Drinfeld twist coherence up to gauge;
- FH+V11: chain map up to coherent (co-)homotopy.

Hence V49\*\* operates at the cohomology-class level only;
chain-level closure requires explicit Stasheff $h_e$ chain witnesses
(open frontier V87).

**$K_5$-coherence verification.** NOT performed in V84. The Stasheff
$K_5$-cocycle $[\eta^{(3)}] \in H^3$ is a separate higher-coherence
obstruction generated by lax closures; its vanishing at K3 input is
declared as hypothesis (H3) and queued as candidate wave V86. A
conjectural pathway via the three sub-projections (Borcherds:
$H^3(\mathcal A_*(\Sp_4(\Z))) = 0$; EK: KZ associator monodromy at
higher orders; FH: V11 Pillar α $(P_4, P_5)$-cube extending to $H^3$)
is sketched in §5.

**v3.4 directive.** V49\*\* (V84-refined) is the canonical Pentagon-
at-$E_1$ K3-input closure form. New AP entries: AP-CY69 (lax-Pentagon
vs. strict-Pentagon edge closure) and AP-CY70 (detecting-family
hypothesis for joint projection-closure). Three new candidate waves
queued: V85 (detecting-family audit), V86 ($K_5$-cocycle audit), V87
(chain-level Stasheff $h_e$ lift). Honest scope: $A_4$-cohomology-
class level at K3 input; chain-level / $A_5$-coherence are explicit
open frontiers.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution. No commits. No `.tex`
edits. No test runs. No build. Sandbox sympy verifications inherited
from V49 / V69, not re-run. Read-only on Vol III. Delivered to
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_V84_attack_heal_V69_fifth_edge_coboundary.md`
per V84 mandate (deepest attack on V69's fifth-edge coboundary
closure for K3 input).
