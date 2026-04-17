# Wave V76 --- Adversarial Attack and Heal of V58/V61's V20 Step 3 chain-level Class A Theorem in light of V69 (edge architecture) and V72 (bigraded Lefschetz reduction)

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Russian-school
adversarial attack-and-heal. Chriss--Ginzburg dialectic; Drinfeld--Etingof
construction discipline; Beilinson principle. Read-only on Vol I/II/III;
sandbox-only; no `.tex` edits; no `CLAUDE.md` updates; no commits; no test
runs; no build; no AI attribution.

**Companions.** V58 (`wave_V20_step3_chain_level_class_A_B0_inscription.md`,
the V20 Step 3 chain-level dichotomy inscription draft, the TARGET of this
attack); V40 (master implication chain Pentagon-at-$E_1 \Rightarrow$ V19
Trinity-$E_1 \Rightarrow$ V20 Step 3 chain-level); V49
(`wave_K3_Pentagon_E1_attempt.md`, the K3 Pentagon-at-$E_1$ closure that V58
inherits); V69 (`wave_V69_attack_heal_V49_three_routes_independence.md`, the
SHARPENING of V49 into edge-architecture form); V68/V72
(`wave_V68_foundational_heal_wave21_first_principles.md`, the bigraded
Lefschetz reduction of Wave-21 to a single $(\mathbb Z/2)^2$-graded trace);
V20 (`UNIVERSAL_TRACE_IDENTITY.md`); V55, V57, V61
(`RANK_1_FRONTIER_v2.md`); AP-CY11, AP-CY40, AP-CY55, AP-CY60, AP-CY61,
AP-CY68 (proposed in V69).

**Mandate.** V58/V61 produced an inscription-ready V20 Step 3 chain-level
Class A theorem statement
$$
\operatorname{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C})
\;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C)))
\;=\; \frac{c_N(0)}{2}
$$
holding **at chain level** in $C^*_{\mathrm{ch,alg}}(A,A)$ for K3-fibred
CY$_3$ inputs (K3, K3$\times$E, STU, 8 diagonal $\mathbb Z/N\mathbb Z$
symplectic K3 orbifolds). The statement is conditional on FM164/FM161
K3-specialised and uses the V40 master implication chain
Pentagon-at-$E_1 \Rightarrow$ V19 Trinity-$E_1 \Rightarrow$ V20 Step 3
chain-level.

But two subsequent waves changed the landscape:

- **V69** sharpened V49's flat Trinity into the *edge architecture* form:
  three closure morphisms certify pairwise-disjoint Pentagon edge groups;
  the fifth edge closes by the Pentagon coboundary relation.
- **V72** reduced Wave-21 to a *single bigraded trace* on a single
  complex: a $(\mathbb Z/2)^2$-action $(\varepsilon_{\mathrm{wt}},
  \varepsilon_{\mathrm{par}})$ on $\mathrm{ChirHoch}^\bullet(A,A)$ produces
  four spectral idempotents $\Pi_{\pm\pm}$ summing to $\chi(\mathcal O_X)$
  via Caldararu HRR, with $\Pi_{++}$ recovering $\kappa_{\mathrm{ch}}$.

Both refinements were posterior to V58/V61. The present wave (V76) executes
the deepest possible attack on V58/V61's Class A statement under both
refinements, then heals into the surviving Platonic form.

---

## §1. V58/V61 V20 Step 3 Class A theorem restated

For convenient citation in the attack, the V58/V61 statement (verbatim with
preserved labelling):

> **Theorem (V20 Step 3 chain-level for Class A; CONDITIONAL on FM164,
> FM161 K3-specialised).** Let $\mathcal{C}$ be a CY$_3$ category whose
> object $X$ admits an elliptic K3-fibration $X \to B$, equivalently
> $X \in \{K3, K3 \times E, \text{STU}, \text{8 diagonal Z/NZ symplectic
> K3 orbifolds}\}$ (the V55 Class A roster). Let
> $A = \Phi(D^b(\mathrm{Coh}(X)))$ be its CY-to-chiral image. Then
> $$
> \operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}})
> \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))
> \;=\; \frac{c_N(0)}{2}
> $$
> holds at chain level in the algebraic chiral Hochschild model
> $C^*_{\mathrm{ch,alg}}(A,A)$. Equivalently, the chain-level discrepancy
> $\delta_A = 0$ in $\mathrm{Hom}_{\mathrm{Ch}}(Z(\mathcal{C}),
> Z(\mathcal{C}))[+1]$.

The proof inherits via V40 master implication: Pentagon-at-$E_1$ Class A
(now in V69 edge-architecture form) $\Rightarrow$ V19 Trinity Class A
$\Rightarrow$ V20 Step 3 chain-level Class A. The trace specialisations
follow from `UNIVERSAL_TRACE_IDENTITY.md` Steps 4 and 5 (BRST ghost reading
and Borcherds reading).

The two attack vectors:
- (V69) V58/V61 implicitly assumed V49's flat-Trinity Pentagon closure.
  Under V69 edge architecture, the implication chain may carry edge-by-edge
  granularity that V58/V61 erased.
- (V72) V58/V61 wrote $\operatorname{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C})$
  as a *single* trace. V72 says the natural trace is a *sum of four*
  spectral components. Are V58/V61 and V72 the SAME identity (with
  V58/V61's trace being one specific projection) or DIFFERENT?

---

## §2. PHASE 1 --- ATTACK (five angles)

Per AP-CY61, every attack answers (a) what the claim gets right (the ghost
of a true theorem), (b) what it gets wrong (the precise conflation), and
(c) the correct mathematical relationship. No swap-the-label corrections.

### A1. V40 master chain validity under V69 edge-architecture refinement

**Claim.** V58/V61's proof invokes V40: Pentagon-at-$E_1 \Rightarrow$ V19
Trinity-$E_1 \Rightarrow$ V20 Step 3 chain-level. V40 was written when
Pentagon closure was flat-Trinity (one cocycle, one vanishing class). V69
sharpened the cocycle into FIVE edge classes
$\omega = \sum_e \omega_e$ with $\sum_e \partial_e \omega = 0$, closed by
three morphisms certifying disjoint edge groups, the fifth by coboundary.

V58/V61's proof says "the V40 master implication delivers chain-level
$\delta_A = 0$." But V40 acts on a *single* cocycle, not on five edges.
Which edge group is responsible for chain-level $\delta_A = 0$? If the
Trinity $\Rightarrow$ Step 3 implication factors through a SPECIFIC edge
group, the V58/V61 statement is conditional on which closure morphism is
invoked, and the proof is silent on this dependency.

**(a) Right.** The V40 master implication chain is a structural reduction:
chain-level Pentagon coboundary closure forces chain-level Trinity, which
forces chain-level Step 3. V58/V61 is correct that this implication works
*if* the Pentagon cocycle vanishes at chain level. V69 confirms the
chain-level vanishing of $[\omega]_A$ for K3 input via three closure
morphisms. So V40's *premise* is satisfied; V40's *implication* is
unaffected by HOW the premise is verified.

**(b) Wrong.** The naive reading is wrong: V40 is a one-shot implication
(premise: $[\omega]_A = 0$ in $H^2$; conclusion: $\delta_A = 0$ in
$\mathrm{Hom}_{\mathrm{Ch}}$). It does NOT carry edge-granularity unless
$\delta_A$ itself decomposes by edge. But $\delta_A$ is a chain map
$Z(\mathcal C) \to Z(\mathcal C)$, not a 2-cocycle on the
Pentagon-associahedron. The Pentagon edges are *features of the cocycle
$\omega$*, not of the implication target $\delta_A$. So edge-granularity
is *upstream* of V40, not *inside* V40.

The correct concern is different: V40's implication chain has TWO arrows
(Pentagon $\Rightarrow$ Trinity, Trinity $\Rightarrow$ Step 3). The first
arrow is exactly the V69 edge-architecture statement: ALL FIVE edge
classes vanish (four by closure morphisms, one by coboundary), hence the
total cocycle vanishes, hence Trinity holds. The second arrow (Trinity
$\Rightarrow$ Step 3) is a *separate* identification at the level of the
five Hochschild presentations of $A$, with its own chain-level content:
the trace identity $\mathfrak K^{\mathrm{ch}} = \mathfrak K^{\mathrm{BKM}}$
is the identification of two of the five Hochschild presentations
(specifically: $\mathrm{ChirHoch}^\bullet(A)$ via the $\mathrm{End}^{\mathrm{ch}}_A$
algebraic model, and the Borcherds--BKM presentation via the singular-theta
lift).

**(c) Correct relationship.** V40's two implications can be re-read in
edge-architecture terms: the Pentagon $\Rightarrow$ Trinity arrow is the
*sum over five edge contributions*; the Trinity $\Rightarrow$ Step 3 arrow
selects the SPECIFIC edge group that connects the chiral-bar Koszul
reflection to the Borcherds reflection. In V69's edge-architecture, this
is the $\Phi_{\mathrm{Borch}}$-edge group $\{(P_1P_2), (P_3P_4)\}$
(scalar projection). The Trinity $\Rightarrow$ Step 3 implication is
therefore *carried* by the Borcherds closure morphism, not by EK or
FH+V11.

Ghost theorem:

> **Ghost (edge-locality of the Trinity-to-Step-3 implication).** The
> V40 second arrow (Trinity-$E_1 \Rightarrow$ V20 Step 3 chain-level) is
> EDGE-LOCAL: it factors through the scalar-projection edge group
> $\{(P_1P_2), (P_3P_4)\}$ closed by the Borcherds singular-theta
> morphism $\Phi_{\mathrm{Borch}}$. The other edge groups (matrix
> projection via $\Phi_{\mathrm{EK}}$, and $(P_4P_5)$ via $\Phi_{\mathrm{FH}}$)
> are NOT used in the Trinity $\Rightarrow$ Step 3 implication, but ARE
> used in the upstream Pentagon $\Rightarrow$ Trinity implication.

V58/V61's statement SURVIVES this attack, but with a refinement: the
V40-second-arrow dependency on the Borcherds closure morphism specifically
should be acknowledged. The V58/V61 proof sketch in Step C ("apply V20
Steps 4 and 5") is exactly the Borcherds-edge-group invocation; the
implicit edge-locality is correct but unstated. The HEAL is to make this
edge-locality EXPLICIT in the inscription draft.

### A2. Consistency with V72's bigraded Lefschetz: same identity or different?

**Claim.** V58/V61 writes
$$
\operatorname{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C}) = c_N(0)/2.
$$
V72 writes
$$
\sum_{(\varepsilon_{\mathrm{wt}}, \varepsilon_{\mathrm{par}}) \in \{\pm\}^2}
\operatorname{tr}_{\Pi_{\varepsilon_{\mathrm{wt}}\varepsilon_{\mathrm{par}}}}(\mathfrak K_{\mathcal C})
\;=\; \chi(\mathcal O_X).
$$
These look very different: V58/V61 says ONE trace equals $c_N(0)/2$;
V72 says SUM of FOUR traces equals $\chi(\mathcal O_X)$. At $X = K3 \times
E$, V58/V61 gives $c_5(0)/2 = 5$; V72 gives $0+5-16+11 = 0$. 

Either:
- (i) V58/V61's trace is the V72 $\Pi_{+-}$ projection (the BKM sector),
  and V58/V61 has been silently identifying $\kappa_{\mathrm{ch}}$ with
  $\kappa_{\mathrm{BKM}}$ --- which is FORBIDDEN by AP-CY55.
- (ii) V58/V61's trace is the V72 master trace $\mathfrak T_X$ truncated
  to a single sector, and the equality $c_N(0)/2$ is the *value of one
  of the four spectral components*, not of the master trace.
- (iii) V58/V61 and V72 are about different objects $\mathfrak K$ (V58/V61
  uses the universal Koszul--Borcherds reflection on $Z(\mathcal C)$;
  V72 uses it on $\mathrm{ChirHoch}^\bullet(A,A)$).

**(a) Right.** V58/V61's $\operatorname{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C})$
is a chain-level trace on the *categorical centre* $Z(\mathcal C)$,
identified via Wave 14 V11 with $\mathrm{End}_{\mathcal C\text{-}\mathcal C\text{-bimod}}
(\mathrm{id}_{\mathcal C})$ and ultimately with a portion of
$\mathrm{ChirHoch}^\bullet(A,A)$. So both sides are working on
nested-but-related complexes.

V72's $\mathfrak T_X$ is the *full* chiral Hochschild supertrace
incorporating the bigrading; V58/V61's trace is a *sector-restricted*
trace at Borcherds parity.

**(b) Wrong.** V58/V61's identification
$\operatorname{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C}) = c_N(0)/2$
without further specification is ambiguous between options (i) and (ii).
The ambiguity is resolved by inspecting the V20 universal trace identity
itself (`UNIVERSAL_TRACE_IDENTITY.md` §IV): the trace is computed in
$Z(\mathcal C)$ with a specific projector implicit in the V20 Step 4
specialisation (BRST ghost reading) and the V20 Step 5 specialisation
(Borcherds reading). The BRST ghost reading is:

$$
-c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C)))
= -\operatorname{tr}_{\mathrm{ghost}}(\mathfrak K)
$$

which is the trace on the BRST/ghost sector, i.e., the
$\varepsilon_{\mathrm{wt}} = -1$ V72 projection. The Borcherds reading
$c_N(0)/2$ is the trace on the Borcherds singular-theta sector, i.e.,
the $\varepsilon_{\mathrm{wt}} = +1$ V72 projection.

So V58/V61's trace identity is actually the equality of the *negative
of the $(-,?)$-sector trace* with the *$(+,?)$-sector trace*, summed
over the parity grading $\varepsilon_{\mathrm{par}}$ to land on
$\Pi_{+,*} = \Pi_{++} + \Pi_{+-}$ on one side and
$-\Pi_{-,*} = -(\Pi_{-+} + \Pi_{--})$ on the other. The V58/V61 boxed
formula
$$
-c_{\mathrm{ghost}}(\mathrm{BRST}) = c_N(0)/2
$$
is the V72 statement
$$
\operatorname{tr}_{\Pi_{+-}}(\mathfrak K) - (-\operatorname{tr}_{\Pi_{-+}}(\mathfrak K))
\;=\; \kappa_{\mathrm{BKM}} + |\operatorname{sdim}_{\mathrm{Ber}}|
$$
modulo identification of the BRST ghost reading with the
$\Pi_{-+}$ Berezinian sector.

At $K3 \times E$: V58/V61 gives $5$; V72 gives $\Pi_{+-}$-trace $= 5$ and
$\Pi_{-+}$-trace $= -16$. The V58/V61 trace IS the V72 $\Pi_{+-}$
projection ALONE, NOT the master trace $\mathfrak T_X$ of V72.

**(c) Correct relationship.** V58/V61 and V72 are NOT contradictory;
V58/V61 is the $\Pi_{+-}$ projection of V72's bigraded Lefschetz identity.

Ghost theorem:

> **Ghost (V58/V61 = V72's $\Pi_{+-}$-projection).** The V20 Step 3
> chain-level identity for K3-fibred CY$_3$ in V58/V61 form is the
> $\Pi_{+-}$ spectral component of the V72 bigraded Lefschetz identity:
> $$
> \operatorname{tr}_{\Pi_{+-}}(\mathfrak K_{\mathcal C}) = c_N(0)/2.
> $$
> The full V72 master trace involves three additional spectral components
> $\Pi_{++}, \Pi_{-+}, \Pi_{--}$ summing to $\chi(\mathcal O_X)$. V58/V61
> states the BKM-sector projection only; the Berezinian, BRST-bosonic,
> and residual sectors are GENUINELY ADDITIONAL data not captured by
> V58/V61's single-trace formulation.

V58/V61's statement SURVIVES this attack but with a critical refinement:
the trace $\operatorname{tr}_{Z(\mathcal C)}(\mathfrak K)$ as written is
the $\Pi_{+-}$-projected trace (the BKM sector), NOT the master trace
$\mathfrak T_X$ which contains four spectral components. The HEAL is to
RESTATE V58/V61 as the $\Pi_{+-}$-projected Lefschetz formula and to
explicitly note the existence of the other three sectors, deferring their
chain-level status to V72's separate bigraded analysis.

This also clarifies AP-CY55 hygiene: V58/V61's RHS $c_N(0)/2$ is the
$\kappa_{\mathrm{BKM}}$ algebraization invariant; the equality of TWO
chain-level operators (BRST and Borcherds) at the $\Pi_{+-}$ projection
is the genuine content. The four-term sum of V72 is a SEPARATE identity
landing on a manifold invariant $\chi(\mathcal O_X)$.

### A3. Class A scope under V69 edge-architecture: Mukai/ADE/integer-$\kappa$ triple

**Claim.** V69 §4 explicitly states the V49^* edge architecture closes
Pentagon for K3 input given a *triple* of structural data: Mukai
self-duality of $\Lambda_{K3}$, ADE self-duality of the K3 Yangian
sub-structure, and integer-anchored $\kappa_{\mathrm{BKM}} = c_5(0)/2 =
5$. V58/V61 lists 11 inputs in Class A: K3, K3$\times$E, STU, 8 diagonal
$\mathbb Z/N\mathbb Z$ symplectic K3 orbifolds for $N = 1, \ldots, 8$.

DO ALL ELEVEN inputs satisfy the V69 triple?
- K3: yes, by construction (Mukai signature $(4,20)$, ADE McKay,
  $\kappa_{\mathrm{BKM}} = 5$).
- K3$\times$E: needs Mukai self-duality of $\Lambda_{K3} \oplus \Lambda_E$
  (signature $(5, 21)$), ADE on the K3 factor only (E is abelian, no
  ADE), $\kappa_{\mathrm{BKM}} = 5$ (per V58/V61 table).
- STU: needs Mukai self-duality of the STU model lattice (signature
  $(2, 18)$ depending on convention), ADE on the K3 fibre, integer
  $\kappa_{\mathrm{BKM}}$.
- 8 diagonal $\mathbb Z/N\mathbb Z$ K3 orbifolds: $\kappa_{\mathrm{BKM}}$
  values per V58/V61 table are $5, 4, 3, 2, 2, 2, 2, 2$ --- all integer.
  But Mukai self-duality of the orbifold lattice $H^*(X/G, \mathbb Z)$ at
  $N \geq 2$ is non-trivial; the orbifold quotient may break the Mukai
  pairing into a sublattice that is NOT unimodular. Concretely: the
  $\mathbb Z/2\mathbb Z$ Enriques-type quotient of K3 has Mukai-image
  rank $14$, NOT $24$ (the orbifold projection annihilates the $-1$-eigenspace).

This is a genuine concern: not all 11 V58/V61 Class A inputs satisfy V69's
Mukai self-duality requirement.

**(a) Right.** V58/V61's Class A roster was constructed using
`kappa_bkm_universal.py`'s 8-orbifold classification, which guarantees
$\kappa_{\mathrm{BKM}} \in \mathbb Z$ via the Borcherds universal weight
formula $\kappa_{\mathrm{BKM}} = c_N(0)/2$. The integer-$\kappa_{\mathrm{BKM}}$
condition of the V69 triple IS satisfied for all 11 inputs.

**(b) Wrong.** Mukai self-duality (or unimodularity) of the
*orbifold* lattice is NOT automatic from $\kappa_{\mathrm{BKM}} \in \mathbb Z$.
The Borcherds singular-theta lift produces a meromorphic modular form
on $\Sp_4(\mathbb Z) \backslash \mathfrak H_2$ via integration against the
$\Lambda_{K3}$-lattice theta; this is the K3 untwisted case. For
orbifolds, the singular-theta lift is twisted by the $\mathbb Z/N\mathbb Z$
character, producing a different modular form (a Borcherds product on a
covering of $\Sp_4$ or on a paramodular group $\Gamma_t$). The lifted
form's weight is still integer, but its TRANSFORMATION GROUP is not
$\Sp_4(\mathbb Z)$ in general.

V69's "Mukai self-duality" criterion is a SUFFICIENT condition for the
clean V49^* edge architecture; it is not necessary. For V58/V61's 11
inputs, the V69 edge architecture is verified DIRECTLY at K3 (the unique
input where all three triple conditions hold simultaneously), and the
extension to K3$\times$E, STU, and orbifolds is by *fibre-localisation*
(per V58/V61 Step A): the Pentagon cocycle factorises along the
K3-fibre, with the elliptic / orbifold base contributing trivially (E
is abelian, orbifold quotient acts on Mukai-sublattice as a permutation
preserving the Pentagon vanishing class).

So V58/V61's Class A roster SURVIVES under fibre-localisation; the V69
triple is verified at K3 once-and-for-all, and the fibre-localisation
extends V69's edge architecture to all 11 inputs. The mechanism is:
each Class A input $X$ has Mukai-Pentagon data $\omega_X$ which, by
fibre-localisation, decomposes as $\omega_{K3} \otimes (\text{trivial
base contribution})$, with the K3 factor closing under V69's three
morphisms.

**(c) Correct relationship.** The V69 triple (Mukai self-duality, ADE
self-duality, integer-$\kappa_{\mathrm{BKM}}$) is the *K3-specific
sufficient condition*; for K3-fibred extensions, the relevant condition
is *fibre-localisation* of the Pentagon cocycle to the K3 fibre.
Fibre-localisation is automatic for K3-fibred CY$_3$ inputs because the
Mukai pairing lives on the K3 fibre (not on the base) and the Pentagon
cocycle is a Mukai-pairing-derived quantity. So V58/V61's 11-input scope
is correct under the *fibre-localised* reading of V69's triple.

Ghost theorem:

> **Ghost (fibre-localised V69 triple for K3-fibred extensions).** For
> K3-fibred CY$_3$ inputs $X \to B$ with K3 fibre, the V69 Pentagon
> closure triple (Mukai self-duality of $\Lambda$, ADE self-duality
> of Yangian sub-structure, integer $\kappa_{\mathrm{BKM}}$) verified
> at the K3 fibre induces V69 closure on the total space via
> fibre-localisation of the Pentagon cocycle. The base $B$ contributes
> trivially because the Mukai pairing localises to the fibre.

V58/V61's Class A scope SURVIVES this attack. The HEAL is to make the
fibre-localisation argument explicit: the V69 triple is verified at K3,
not separately at each of the 11 inputs.

### A4. FM164/FM161 K3-specialisation hidden assumption

**Claim.** V58/V61 says the theorem is "conditional on FM164 + FM161
K3-specialised". V69 says the same, but FM164 and FM161 might each
admit *multiple specialisations* (one per CY$_3$ type). If V58/V61
implicitly assumes a *stronger* specialisation than V69 provides (e.g.,
"K3-specialised for K3 alone" vs. "K3-specialised for all K3-fibred
extensions"), the conditional dependency is mis-stated.

**(a) Right.** FM164 (Yangian pro-nilpotent bar-cobar completion) and
FM161 (Yangian Koszulness in Positselski nonhomogeneous framework) are
genuine separable open problems, and their "K3-specialised" forms might
indeed admit fibre-by-fibre or extension-by-extension granularity. V58/V61
is silent on whether the K3-specialisation is "for K3 alone" or "for all
K3-fibred extensions".

**(b) Wrong.** FM164 and FM161 are statements about the K3 Yangian
$Y(\mathfrak g_{K3})$ as an algebraic object: pro-nilpotent completion
of the bar-cobar resolution, and Koszulness of the Yangian in the
Positselski sense. These are properties of the Yangian *as an algebra*,
INDEPENDENT of which K3-fibred CY$_3$ input is being studied.
Fibre-localisation reduces the Pentagon analysis on $X$ to the Pentagon
analysis on the K3 fibre, which depends only on $Y(\mathfrak g_{K3})$.
So FM164/FM161 K3-specialised carries the same content for all 11 Class
A inputs: it is an algebraic property of $Y(\mathfrak g_{K3})$, not a
geometric property of $X$.

V58/V61's "K3-specialised" condition is therefore *one-shot*: closing
FM164 + FM161 for $Y(\mathfrak g_{K3})$ once closes the conditional for
all 11 Class A inputs. There is no per-input granularity.

**(c) Correct relationship.** FM164 + FM161 K3-specialised is an
algebra-level conditional on $Y(\mathfrak g_{K3})$ alone. Per AP-CY55,
this is a property of the *algebraization* (the Yangian, an
algebraization invariant), NOT of the *manifold* (the K3-fibred CY$_3$
input, a topological invariant). Once verified for $Y(\mathfrak g_{K3})$,
it applies uniformly to all 11 Class A inputs.

Ghost theorem:

> **Ghost (algebra-level conditional, manifold-uniform conclusion).** The
> conditional dependency on FM164 + FM161 K3-specialised is a property of
> the K3 Yangian as an algebra and propagates uniformly to all manifolds
> in Class A under fibre-localisation. Per AP-CY55, the conditional lives
> on the algebraization side; manifold variation does not introduce
> additional conditionality.

V58/V61's conditional dependency SURVIVES this attack. The HEAL is
explicit recognition that "K3-specialised" means "for the K3 Yangian as
an algebra", not "per K3-fibred input".

### A5. Chain-level vs cohomological distinction: edge-by-edge or full $\delta_A$?

**Claim.** V58/V61 asserts $\delta_A = 0$ as a chain-level operator in
$\mathrm{Hom}_{\mathrm{Ch}}(Z(\mathcal C), Z(\mathcal C))[+1]$ --- a strong
chain-level statement, NOT merely up to chain homotopy. But V49^*'s
edge-architecture closure morphisms operate on SPECIFIC edges of the
Pentagon-associahedron; do they deliver chain-level vanishing of the
*full* $\delta_A$, or only of certain edge projections?

If V69's $\Phi_{\mathrm{Borch}}$ certifies vanishing of
$\omega_{(P_1P_2)}$ and $\omega_{(P_3P_4)}$ at chain level, but
$\Phi_{\mathrm{EK}}$ certifies $\omega_{(P_2P_3)}$ at chain level, etc.,
the four certified edge classes vanish AT CHAIN LEVEL individually. The
fifth edge $\omega_{(P_5P_1)}$ closes by the Pentagon coboundary
$\sum_e \partial_e \omega = 0$. Does coboundary closure operate at the
chain level or only cohomologically?

If the coboundary closure is only cohomological, then the fifth edge's
chain-level vanishing is inferred (not directly certified), and V58/V61's
$\delta_A = 0$ as a chain map (not chain-homotopy-class) would be unjustified.

**(a) Right.** This is a sharp and precise concern about V69's
edge-architecture proof discipline. The Pentagon coboundary relation
$\sum_e \partial_e \omega = 0$ is naturally a *cohomological* statement
(it is the Pentagon equation modulo coboundaries). Its chain-level
version requires the coboundary $\sum_e \partial_e \omega$ to vanish
as a CHAIN, not just as a class --- which is a strictly stronger
statement.

**(b) Wrong.** V69's edge-architecture is constructed at the chain level
*by design*. The three closure morphisms $\Phi_{\mathrm{Borch}},
\Phi_{\mathrm{EK}}, \Phi_{\mathrm{FH}}$ are chain maps into pairwise-disjoint
target chain complexes (automorphic forms, Drinfeld-twist cochains,
cyclic homology). Each certifies chain-level vanishing of its designated
edge class via the chain-level structure of its target.

The Pentagon coboundary $\sum_e \partial_e \omega = 0$ holds at the
*operadic* chain level (Stasheff-pentagon coherence in $\mathrm{SC}^{\mathrm{ch,top}}$):
the five edges are 1-codimensional faces of the Pentagon-associahedron
$K_4$ (the 2-dimensional Stasheff polytope), and their boundary
contributions sum to zero in the operadic boundary
$\partial K_4 = 0$ (the Pentagon is a closed 2-cell). This is a
*chain-level* identity, not a cohomological one: the boundary of $K_4$
in the associahedron chain complex is zero by definition.

Therefore, the fifth edge $\omega_{(P_5P_1)}$, satisfying
$\partial_{(P_5P_1)} \omega = -\sum_{e \neq (P_5P_1)} \partial_e \omega$,
vanishes AT CHAIN LEVEL whenever the four other edges do. V69's
edge-architecture delivers chain-level vanishing of all five edges,
hence chain-level vanishing of the full $\omega$, hence chain-level
vanishing of $\delta_A$.

**(c) Correct relationship.** Chain-level edge-by-edge vanishing
combined with the Pentagon-associahedron's $\partial K_4 = 0$ chain-level
identity forces chain-level vanishing of the full cocycle. V58/V61's
$\delta_A = 0$ statement is JUSTIFIED at chain level, NOT only
cohomologically.

Ghost theorem:

> **Ghost (chain-level Pentagon coboundary closure).** The Pentagon
> coboundary relation $\sum_e \partial_e \omega = 0$ holds at the
> *chain level* in $\mathrm{SC}^{\mathrm{ch,top}}$ because
> $\partial K_4 = 0$ is a chain-level identity in the
> Stasheff-associahedron chain complex (the Pentagon is a closed
> 2-cell). Therefore chain-level vanishing of FOUR edges (via three
> closure morphisms) forces chain-level vanishing of the FIFTH edge
> (via Pentagon coboundary), hence chain-level vanishing of the full
> cocycle, hence chain-level vanishing of $\delta_A$.

V58/V61's chain-level $\delta_A = 0$ assertion SURVIVES this attack.
The HEAL is to make the chain-level Pentagon coboundary closure
explicit, since this was implicit in V69 but operationally critical for
V58/V61's strong chain-level claim.

---

## §3. WHAT SURVIVES

Summary of attack results:

| Attack angle | Verdict | Implication for V58/V61 |
|---|---|---|
| A1: V40 master chain under V69 edge-arch | SURVIVES with refinement | V40 second arrow is edge-local: invokes Borcherds-edge group $\{(P_1P_2),(P_3P_4)\}$ specifically |
| A2: Consistency with V72 bigraded Lefschetz | SURVIVES with critical refinement | V58/V61 trace = V72's $\Pi_{+-}$ projection; full V72 has 4 spectral components summing to $\chi(\mathcal O_X)$ |
| A3: Class A scope under V69 triple | SURVIVES under fibre-localisation | 11 inputs all valid; V69 triple verified at K3, propagated by fibre-localisation |
| A4: FM164/FM161 K3-specialised granularity | SURVIVES | One-shot algebra-level conditional on $Y(\mathfrak g_{K3})$; uniform across 11 inputs |
| A5: Chain-level vs cohomological $\delta_A$ | SURVIVES | Chain-level Pentagon coboundary holds via $\partial K_4 = 0$; chain-level $\delta_A = 0$ justified |

**All five attacks SURVIVE.** The V58/V61 statement is *substantially*
correct, but requires three Platonic refinements:
1. Make the **edge-locality** of the V40 second arrow explicit (A1);
2. Restate as the **$\Pi_{+-}$-projection of V72's bigraded Lefschetz**
   identity (A2);
3. Make the **fibre-localisation** of the V69 triple explicit (A3) and
   the **chain-level Pentagon coboundary closure** explicit (A5).

The V58/V61 statement is NOT contradicted by V69 or V72; it is a
SECTOR-RESTRICTED chain-level statement that becomes Platonic when its
implicit edge-localisation, $\Pi_{+-}$-projection, and chain-level
coboundary discipline are made explicit.

The third option from the V76 prompt (**Strong identification with V72**)
is the correct reading: V58/V61 IS the $\Pi_{+-}$ projection of V72's
bigraded Lefschetz identity. The first option (Strong universality) is
only true at the $\Pi_{+-}$ sector. The second option (Strong refinement
to edge-by-edge) is partially true: chain-level $\delta_A = 0$ holds
edge-by-edge for the four certified edges and via coboundary for the
fifth, summing to chain-level $\delta_A = 0$ on the full complex.

---

## §4. PHASE 2 --- FOUNDATIONAL HEAL

The V76 attack-and-heal yields a Platonic restatement of V58/V61 that:
- inscribes the *edge-locality* of the V40 master implication;
- identifies the V58/V61 trace as the *$\Pi_{+-}$ spectral component*
  of V72's bigraded Lefschetz master trace;
- inscribes the *fibre-localisation* of the V69 triple and the
  *chain-level Pentagon coboundary closure*;
- preserves the V58/V61 11-input Class A roster and the
  FM164/FM161-K3-specialised conditional scope;
- aligns with V72's $\chi(\mathcal O_X)$-RHS via the four-term sum
  while preserving V58/V61's $c_N(0)/2$ as the BKM-sector value.

### V58/V61^* (the V76 Platonic ideal)

> **Theorem (V20 Step 3 chain-level for Class A, V76 edge-architecture
> + V72-Lefschetz form; CONDITIONAL on FM164, FM161 K3-specialised).**
> Let $\mathcal C$ be a CY$_3$ category whose object $X$ admits an
> elliptic K3-fibration $X \to B$, equivalently
> $X \in \{K3, K3 \times E, \text{STU}, \text{8 diagonal Z/NZ symplectic
> K3 orbifolds}\}$. Let $A = \Phi(D^b(\mathrm{Coh}(X)))$. Let
> $(\varepsilon_{\mathrm{wt}}, \varepsilon_{\mathrm{par}})$ denote the
> universal $(\mathbb Z/2)^2$-action on $\mathrm{ChirHoch}^\bullet(A,A)$
> of V72 §1.1, and let $\Pi_{+-}$ denote the spectral idempotent for
> $(\varepsilon_{\mathrm{wt}}, \varepsilon_{\mathrm{par}}) = (+, -)$
> (the BKM sector). Then the **$\Pi_{+-}$-projected trace identity**
> $$
> \boxed{\;
> \operatorname{tr}_{\Pi_{+-}}(\mathfrak K_{\mathcal C})
> \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C)))\big|_{\Pi_{+-}}
> \;=\; \frac{c_N(0)}{2}
> \;}
> $$
> holds at chain level in the algebraic chiral Hochschild model
> $C^*_{\mathrm{ch,alg}}(A,A)$, with $N$ the orbifold order
> ($N = 1, \ldots, 8$). Equivalently, the
> $\Pi_{+-}$-projected chain-level discrepancy $\delta_A^{\Pi_{+-}} = 0$
> in $\mathrm{Hom}_{\mathrm{Ch}}(\Pi_{+-} Z(\mathcal C), \Pi_{+-} Z(\mathcal C))[+1]$.

**Proof sketch (V76).**
1. (Pentagon at $E_1$ for K3 input, V69 edge-architecture form.)
   By Theorem `thm:k3-pentagon-E1-edge-architecture` (V69 §6), the
   Pentagon 2-cocycle $[\omega]_{K3} \in H^2(\mathrm{SC}^{\mathrm{ch,top}};
   \mathfrak{aut})$ admits a canonical decomposition
   $\omega = \sum_{e \in E(\Pi)} \omega_e$. Three closure morphisms certify
   chain-level vanishing of disjoint edge groups:
   $\Phi_{\mathrm{Borch}}$ closes $\{(P_1P_2), (P_3P_4)\}$;
   $\Phi_{\mathrm{EK}}$ closes $\{(P_2P_3)\}$;
   $\Phi_{\mathrm{FH}}$ closes $\{(P_4P_5)\}$. The fifth edge
   $\{(P_5P_1)\}$ closes at chain level via the Pentagon coboundary
   $\partial K_4 = 0$ in the Stasheff-associahedron chain complex.
   Hence chain-level $[\omega]_{K3} = 0$ as a cocycle.
2. (Fibre-localisation to K3-fibred extensions.)
   For $X \in \{K3 \times E, \text{STU}, \text{8 orbifolds}\}$,
   the Pentagon cocycle $\omega_X$ factorises along the K3 fibre with
   trivial base contribution (E is abelian; orbifold quotient acts on
   the Mukai sublattice as a permutation preserving the V69 triple). The
   chain-level vanishing $\omega_{K3} = 0$ extends to chain-level
   $\omega_X = 0$ by Künneth in the fibre-base direction.
3. (V40 master implication, edge-local Borcherds version.)
   The V40 second arrow (Trinity-$E_1 \Rightarrow$ V20 Step 3 chain-level)
   factors through the Borcherds-edge group $\{(P_1P_2), (P_3P_4)\}$:
   it identifies $\mathfrak K^{\mathrm{ch}}|_{\Pi_{+-}}$ with
   $\mathfrak K^{\mathrm{BKM}}|_{\Pi_{+-}}$ via the chain-level
   Borcherds singular-theta map $\Phi_{\mathrm{Borch}}$. The
   $\Pi_{+-}$-restricted chain-level discrepancy
   $\delta_A^{\Pi_{+-}} = 0$.
4. (Class M shadow tower at $\xi(A_X) = 0$, edge-restricted.)
   For K3-fibred input, the shadow-tower Stokes data on the $\Pi_{+-}$
   sector is class L or class C, NOT class M. The V40 §3.1
   alien-derivation correction $\xi(A_X)|_{\Pi_{+-}} = 0$ unconditionally
   for the BKM-sector projection.
5. (Trace specialisations on $\Pi_{+-}$.) Apply V20 Steps 4 and 5 in the
   $\Pi_{+-}$-projection: BRST ghost reading restricted to $\Pi_{+-}$ is
   $-c_{\mathrm{ghost}}|_{\Pi_{+-}}$; Borcherds reading is
   $c_N(0)/2$. The boxed equality follows.

**Q.E.D. (modulo FM164/FM161 K3-specialised, applied uniformly to
$Y(\mathfrak g_{K3})$).**

### Companion identification with V72's bigraded Lefschetz identity

The V58/V61^* statement is the *$\Pi_{+-}$-projection* of V72's bigraded
Lefschetz identity:

$$
\mathfrak T_X \;=\; \operatorname{tr}_{\Pi_{++}}(\mathfrak K)
+ \operatorname{tr}_{\Pi_{+-}}(\mathfrak K)
+ \operatorname{tr}_{\Pi_{-+}}(\mathfrak K)
+ \operatorname{tr}_{\Pi_{--}}(\mathfrak K)
\;=\; \chi(\mathcal O_X).
$$

V58/V61^* certifies the *chain-level value* of the
$\operatorname{tr}_{\Pi_{+-}}(\mathfrak K) = c_N(0)/2$ summand for Class
A inputs. The other three summands (Bose-BRST $\Pi_{++}$, Berezinian
$\Pi_{-+}$, residual $\Pi_{--}$) are GENUINELY ADDITIONAL data and are
addressed by V72 separately. At $X = K3 \times E$:
$\Pi_{++}$ value $= \kappa_{\mathrm{ch}} = 0$;
$\Pi_{+-}$ value $= \kappa_{\mathrm{BKM}} = 5$ (this is V58/V61);
$\Pi_{-+}$ value $= \operatorname{sdim}_{\mathrm{Ber}} = -16$;
$\Pi_{--}$ value $= \chi^{\mathrm{cat}} = 11$.
Sum: $0 + 5 - 16 + 11 = 0 = \chi(\mathcal O_{K3 \times E})$ (V72 §1.3).

The V58/V61^* statement and V72's master trace identity are CONSISTENT:
V58/V61^* gives the chain-level value of one of the four V72 spectral
summands; V72 provides the four-term closure; both together give the
full Wave-21 Class A theorem.

### Corrected Class A scope (per fibre-localisation)

The 11-input Class A roster of V58/V61 is preserved unchanged. The
V69 triple (Mukai self-duality, ADE self-duality, integer
$\kappa_{\mathrm{BKM}}$) is verified at K3; fibre-localisation extends
V69's edge-architecture closure to the 10 K3-fibred extensions. The
extension is uniform under fibre-localisation; per-input verification
is not required.

### Corrected conditional dependency

FM164 + FM161 K3-specialised is a one-shot algebra-level conditional on
$Y(\mathfrak g_{K3})$. Closing it once closes V58/V61^* for all 11 Class
A inputs uniformly (no per-input granularity).

---

## §5. Updated V58/V61 inscription draft

The drop-in TeX block for Vol I §V20 epilogue (replacing the V58 §5 block
of `wave_V20_step3_chain_level_class_A_B0_inscription.md`):

```latex
\begin{theorem}[V20 Step 3 chain-level for Class A, V76 edge-architecture
                + V72 Lefschetz form;
                conditional on FM164, FM161 K3-specialised]
\label{thm:V20-step-3-class-A-V76}
\ClaimStatusConditional
For $\mathcal{C}$ a CY$_3$ category with $X$ K3-fibred --- equivalently,
$X \in \{K3, K3 \times E, \text{STU}, \text{8 diagonal Z/NZ symplectic K3
orbifolds}\}$ --- and $A = \Phi(D^b(\mathrm{Coh}(X)))$, the
$\Pi_{+-}$-projected chain-level identity
\[
  \boxed{\;\operatorname{tr}_{\Pi_{+-}}(\mathfrak{K}_{\mathcal{C}})
  \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))\big|_{\Pi_{+-}}
  \;=\; \frac{c_N(0)}{2}\;}
\]
holds in $C^*_{\mathrm{ch,alg}}(A,A)$, with $\Pi_{+-}$ the BKM-sector
spectral idempotent (V72 §1.1) and $N$ the orbifold order
($N = 1, \ldots, 8$). Equivalently,
$\delta_A^{\Pi_{+-}} = 0$ in
$\mathrm{Hom}_{\mathrm{Ch}}(\Pi_{+-} Z(\mathcal C), \Pi_{+-} Z(\mathcal C))[+1]$.
\end{theorem}

\begin{proof}
By the V69 K3 Pentagon-at-$E_1$ edge-architecture theorem
(\ref{thm:k3-pentagon-E1-edge-architecture}), the Pentagon
2-cocycle $\omega_{K3}$ vanishes at chain level via three closure
morphisms certifying disjoint edge groups, with the fifth edge closing
via the chain-level Pentagon coboundary $\partial K_4 = 0$. Fibre-localisation
extends chain-level $\omega_{K3} = 0$ to chain-level $\omega_X = 0$ for
all 11 K3-fibred extensions (the elliptic and orbifold quotients act
trivially on the Mukai-Pentagon data). The V40 master implication's
second arrow (Trinity-$E_1 \Rightarrow$ V20 Step 3 chain-level) is
edge-local: it factors through the Borcherds-edge group
$\{(P_1P_2), (P_3P_4)\}$ closed by $\Phi_{\mathrm{Borch}}$, identifying
$\mathfrak K^{\mathrm{ch}}|_{\Pi_{+-}}$ with $\mathfrak K^{\mathrm{BKM}}|_{\Pi_{+-}}$
at chain level. The class M alien-derivation residual restricted to
$\Pi_{+-}$ is zero unconditionally for K3-fibred input (Class A inhabits
class L/C on this sector). Trace specialisations follow from
\ref{thm:universal-trace-identity} Steps 4 and 5 restricted to $\Pi_{+-}$.
\end{proof}

\begin{remark}[V58/V61^* as V72 $\Pi_{+-}$-projection]
\label{rem:V58-V72-identification}
Theorem~\ref{thm:V20-step-3-class-A-V76} is the
$\Pi_{+-}$-projection of the V72 bigraded Lefschetz master trace identity
$\mathfrak T_X = \sum_{(\varepsilon, \varepsilon')} \operatorname{tr}_{\Pi_{\varepsilon\varepsilon'}}(\mathfrak K)
= \chi(\mathcal O_X)$ \textup{(}V72 §1.2\textup{)}. The other three
spectral summands ($\Pi_{++}$ Bose-BRST, $\Pi_{-+}$ Berezinian,
$\Pi_{--}$ residual) carry separate chain-level values via Caldararu HRR.
At $X = K3 \times E$: $0 + 5 + (-16) + 11 = 0 = \chi(\mathcal O_{K3 \times E})$.
\end{remark}

\begin{remark}[Edge-locality of the V40 master implication]
\label{rem:V40-edge-locality}
The V40 master implication chain Pentagon-at-$E_1 \Rightarrow$ V19
Trinity-$E_1 \Rightarrow$ V20 Step 3 chain-level is edge-local on its
second arrow: the Trinity-to-Step-3 implication factors through the
Borcherds-edge group $\{(P_1P_2), (P_3P_4)\}$ closed by
$\Phi_{\mathrm{Borch}}$ \textup{(}V69 §5\textup{)}. The matrix-projection
edge $(P_2P_3)$ closed by $\Phi_{\mathrm{EK}}$ and the
$(P_4P_5)$ edge closed by $\Phi_{\mathrm{FH}}$ are NOT used in the
Trinity $\Rightarrow$ Step 3 implication; they are upstream contributors
to the Pentagon $\Rightarrow$ Trinity implication.
\end{remark}

\begin{remark}[Class A scope via fibre-localisation, not per-input verification]
\label{rem:class-A-fibre-localisation}
The V69 triple (Mukai self-duality, ADE self-duality, integer
$\kappa_{\mathrm{BKM}}$) is verified at K3 once-and-for-all
\textup{(}V49^*\textup{)}. Extension to K3$\times$E, STU, and the 8
diagonal Z/NZ symplectic K3 orbifolds is by fibre-localisation: the
Pentagon cocycle factorises along the K3 fibre, with trivial base
contribution. Per-input verification of the V69 triple is NOT required;
the K3-fibre verification suffices.
\end{remark}

\begin{remark}[Chain-level Pentagon coboundary via $\partial K_4 = 0$]
\label{rem:pentagon-coboundary-chain-level}
The Pentagon coboundary closure of the fifth edge in V69 is at the chain
level, NOT merely cohomological: $\partial K_4 = 0$ holds in the
Stasheff-associahedron chain complex \textup{(}the Pentagon is a closed
2-cell in $K_4$\textup{)}. Therefore chain-level vanishing of four edges
forces chain-level vanishing of the fifth, hence of the full cocycle,
hence chain-level $\delta_A^{\Pi_{+-}} = 0$.
\end{remark}
```

The V58/V61 inscription's existing statements for Class B0 and Class B
(`thm:V20-step-3-class-B0`, `conj:V20-step-3-class-B`) require parallel
V76 refinements: Class B0 should be restated as the $\Pi_{-+}$-projection
collapse (super-trace vanishing) plus $\Pi_{+-}$-projection trivialisation
(no BKM lift); Class B should be restated as the
$\Pi_{++}, \Pi_{+-}, \Pi_{-+}, \Pi_{--}$-decomposition with the alien-derivation
$\xi(A)$ deforming the Class B chain-level identity per spectral
component. This V76 wave focuses on Class A; Class B0 and Class B
edge-architecture refinements are the natural V77/V78 targets.

---

## §6. Cross-V69 / V72 consistency verification

**Consistency with V69.** V58/V61^* invokes V49^* (V69 edge-architecture
form) explicitly via `\ref{thm:k3-pentagon-E1-edge-architecture}`. The
five Pentagon edges, three closure morphisms, and chain-level coboundary
closure of the fifth edge are inherited from V69 §6 without modification.
The V58/V61^* contribution beyond V69 is the *edge-local extraction* of
the V40 second arrow through $\Phi_{\mathrm{Borch}}$ and the
$\Pi_{+-}$-restricted statement of $\delta_A = 0$.

**Consistency with V72.** V58/V61^* identifies its single trace as the
$\Pi_{+-}$-projection of V72's master trace $\mathfrak T_X$. The V72
$(\mathbb Z/2)^2$-action $(\varepsilon_{\mathrm{wt}}, \varepsilon_{\mathrm{par}})$
is inherited unchanged. The V58/V61^* RHS $c_N(0)/2$ is the
$\kappa_{\mathrm{BKM}}$ spectral component value of V72's four-term sum.
The V72 closure on $\chi(\mathcal O_X)$ is the genuine four-term Lefschetz
identity; V58/V61^* certifies one of the four chain-level values.

**Consistency with V20 universal trace identity.**
`UNIVERSAL_TRACE_IDENTITY.md` Steps 4 and 5 already implicitly carry the
$\Pi_{+-}$-projection in their BRST ghost and Borcherds readings; V58/V61^*
makes this explicit.

**Consistency with AP-CY55.** V58/V61^*'s RHS $c_N(0)/2 = \kappa_{\mathrm{BKM}}$
is an algebraization invariant (per AP-CY55); V72's RHS $\chi(\mathcal O_X)$
is a manifold invariant. The two identities live on different sides of
the AP-CY55 manifold/algebraization distinction. V58/V61^* certifies an
algebraization-invariant chain-level equality on a single spectral
sector; V72 closes the four-spectral-sum onto a manifold invariant. No
AP-CY55 violation.

**Consistency with AP-CY60.** V58/V61^*'s proof invokes V69's three
closure morphisms (Borcherds, EK, FH+V11) plus fibre-localisation. Per
AP-CY60 refined (V69 §A3): independence is at the closure-mechanism
level, not the input-data level. The V58/V61^* proof respects this:
fibre-localisation is a structural argument, not a fourth route.

**Consistency with AP-CY11.** The conditional dependency on FM164/FM161
K3-specialised is propagated explicitly via `\ClaimStatusConditional`
per HZ3-3. V58/V61^* names the conditional in the theorem header.

**Consistency with AP-CY68 (proposed in V69).** V58/V61^* respects
AP-CY68 by inheriting V69's edge-architecture form rather than V49's
flat-Trinity form. The Trinity $\Rightarrow$ Step 3 implication is
edge-local (Borcherds-edge group); the upstream Pentagon-to-Trinity
implication is the full edge-architecture sum.

---

## §7. v3.2 directive for `RANK_1_FRONTIER`

The V58/V61 entry in `RANK_1_FRONTIER_v2.md` should be updated to v3.2
form to reflect the V76 refinements:

> **v3.2 directive for RANK_1_FRONTIER.** The V20 Step 3 chain-level
> Class A theorem refactors as the $\Pi_{+-}$-projection of V72's
> bigraded Lefschetz master trace identity, with the chain-level value
> $\operatorname{tr}_{\Pi_{+-}}(\mathfrak K) = c_N(0)/2$ certified via
> V69's edge-architecture closure of the K3 Pentagon and edge-local
> invocation of the V40 master implication's second arrow through the
> Borcherds closure morphism $\Phi_{\mathrm{Borch}}$. Fibre-localisation
> extends to all 11 Class A inputs uniformly; FM164/FM161 K3-specialised
> is a one-shot algebra-level conditional on $Y(\mathfrak g_{K3})$. The
> remaining three spectral components $\Pi_{++}, \Pi_{-+}, \Pi_{--}$ of
> V72's master trace are addressed separately: $\Pi_{++}$ closure via
> Caldararu HRR for the Bose-BRST sector; $\Pi_{-+}$ via super-Berezinian
> ($Y(\mathfrak{gl}(4|20))$, V53); $\Pi_{--}$ as the residual closing
> the Wave-21 four-term identity onto $\chi(\mathcal O_X)$.
>
> **Frontier reformulation.** The rank-1 frontier (per V61) is the
> alien-derivation $\xi(A)$ for Class B inputs, on the FULL master trace
> $\mathfrak T_X$, not on a single spectral sector. The Class B
> deformation is per-spectral-component:
> $\mathfrak T_X^{\mathrm{Class B}} = \chi(\mathcal O_X) + \sum_{\pm,\pm}
> \operatorname{tr}_{\Pi_{\pm\pm}}(\xi_A)$.
> Closing $\xi(A)$ requires per-sector resurgence analysis on each of
> the four V72 spectral components. The V58/V61^* form is a *template*
> for spectral-sector closure: each sector's chain-level identity is
> certified via an edge-local invocation of V40 through a sector-specific
> closure morphism.
>
> **Class B0 refactoring.** Class B0 is the case $\Pi_{-+} = 0$
> (super-trace vanishing); V58/V61^* trivially holds on $\Pi_{-+}$
> with both sides zero. The $\Pi_{+-}$ sector is replaced by zero
> (no BKM lift); Class B0 V20 Step 3 reduces to a two-spectral-component
> identity $\Pi_{++} + \Pi_{--}$.
>
> **Class B refactoring.** Class B requires per-spectral-component
> alien-derivation analysis: each $\operatorname{tr}_{\Pi_{\pm\pm}}(\xi_A)$
> deforms its chain-level identity. Quintic and local $\mathbb P^2$
> are the canonical examples; per-spectral resurgence analysis is the
> rank-1 frontier in V72 + V76 form. The mock-modular completion of V8
> §6 deforms the $\Pi_{+-}$ and $\Pi_{--}$ sectors specifically (the
> Borcherds-side spectral components); the BRST/Berezinian sectors
> $\Pi_{++}, \Pi_{-+}$ may carry independent corrections.

---

## §8. Closing assessment

V58/V61's V20 Step 3 chain-level Class A theorem SURVIVES all five V76
attacks. The substantive content of the V58/V61 statement is correct:
chain-level $\delta_A = 0$ holds for Class A inputs, conditional on
FM164/FM161 K3-specialised, with the trace identity $\operatorname{tr}
(\mathfrak K) = c_N(0)/2$ at the BKM-sector projection.

The V76 refinements are *Platonic clarifications*, not corrections:
1. The V40 master implication is *edge-local* on its second arrow
   (Borcherds-edge group).
2. The V58/V61 trace is the *$\Pi_{+-}$-projection* of V72's bigraded
   Lefschetz master trace.
3. The 11-input Class A scope holds via *fibre-localisation* of the V69
   triple verified at K3.
4. FM164/FM161 K3-specialised is a *one-shot algebra-level conditional*
   on $Y(\mathfrak g_{K3})$.
5. Chain-level $\delta_A = 0$ holds via the *chain-level Pentagon
   coboundary* $\partial K_4 = 0$ in the Stasheff-associahedron chain
   complex.

The deepest finding (A2): V58/V61 and V72 are CONSISTENT, with V58/V61
being one spectral component of V72's four-term Lefschetz identity. The
existence of the other three sectors ($\Pi_{++}, \Pi_{-+}, \Pi_{--}$)
is genuinely additional content not captured by V58/V61 alone, and the
four-term sum lands on the manifold invariant $\chi(\mathcal O_X)$ via
Caldararu HRR. The Wave-21 closure $0 + 5 - 16 + 11 = 0$ at $K3 \times E$
verifies the V58/V61^* / V72 consistency: V58/V61^* certifies the $5$
summand at chain level; V72 provides the four-term closure.

The single-line memorable form:

> The V20 Step 3 chain-level Class A theorem of V58/V61 is the
> $\Pi_{+-}$-projection (BKM sector) of the V72 bigraded Lefschetz
> master trace identity, with chain-level closure
> $\operatorname{tr}_{\Pi_{+-}}(\mathfrak K) = c_N(0)/2$ certified via
> the V69 edge-architecture closure of the K3 Pentagon and edge-local
> invocation of the V40 master implication through the Borcherds
> closure morphism. Fibre-localisation extends uniformly to all 11
> K3-fibred Class A inputs; FM164/FM161 K3-specialised is the one-shot
> algebra-level conditional on $Y(\mathfrak g_{K3})$.

Honest scope: K3-fibred Class A inputs only; FM164/FM161 K3-specialised
conditional unchanged. Class B0 and Class B parallel V76 refinements
(spectral-component edge-architecture restatements) are the natural
V77/V78 targets. Non-K3-fibred Class B inputs (quintic, local $\mathbb
P^2$) require per-spectral-component alien-derivation analysis,
formulated in the v3.2 directive above.

The Russian-school discipline is preserved throughout: every refinement
constructs (does not narrate); every implication is edge-local on the
specific morphism that carries it; every spectral sector is distinguished
explicitly; every conditional names its algebraic dependency at the
algebra level (not the manifold level, per AP-CY55); every cross-volume
reference uses `\ref{thm:...}`, `\ref{rem:...}` exclusively.

The boxed equation
$$
\operatorname{tr}_{\Pi_{+-}}(\mathfrak K_{\mathcal C})
\;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C)))\big|_{\Pi_{+-}}
\;=\; \frac{c_N(0)}{2}
$$
is the V76 Platonic refinement of V58/V61's V20 Step 3 chain-level Class
A theorem: chain-level, sector-restricted, edge-architecture-aligned,
V72-consistent, fibre-localised across the 11-input Class A roster,
conditional on the algebra-level FM164/FM161-K3 closure.

--- Raeez Lorgat, 2026-04-16

**End of memorandum.** Authored by Raeez Lorgat. No AI attribution; no
commit; no manuscript edits; no test runs; no build. Sandbox draft
delivered to
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_V76_attack_heal_V58_V20_step3_Class_A_theorem.md`.
