# Wave 9 — Holographic Frontier (Adversarial Audit)

**Targets**
- `chapters/connections/holographic_datum_master.tex` (PRIMARY)
- `chapters/connections/frontier_modular_holography_platonic.tex` (PRIMARY)
- `chapters/connections/entanglement_modular_koszul.tex` (gold-standard pattern)
- `chapters/connections/thqg_introduction_supplement.tex` and `_body.tex`
- `chapters/connections/thqg_entanglement_programme.tex`
- `chapters/connections/holographic_codes_koszul.tex`
- `standalone/three_dimensional_quantum_gravity.tex`

**Methodology** — adversarial audit attacking, then steelmanning, the holographic
claims; AP155, AP-CY57, AP-CY79, AP-CY81, AP-CY82, AP-CY87 propagation; first-principles
extraction of the beating mathematical core (AP-CY61).

**Disclosure**: read-only audit. No edits to manuscript. Findings fed back to
`appendices/first_principles_cache.md` (suggested entries 51–55) and
`notes/tautology_registry.md`.

---

## Section 1. `holographic_datum_master.tex` audit

### 1.1 What is the master claim?

The chapter (subtitled *The seven faces of the collision residue*) makes a single
master claim: the genus-zero binary collision residue
$r_\cA(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
admits **seven independent realizations** (F1–F7) all of which coincide as
elements of $\mathrm{End}_\cA(2)[\![z^{-1}]\!]$ after standard normalization
(Theorem `thm:hdm-seven-way-master`, ProvedHere).

The seven faces are:

| Face | Object | Source |
|------|--------|--------|
| F1 | bar–cobar twisting morphism $\pi_\cA$ | this monograph |
| F2 | DNP line-operator $r$-matrix $r^{\mathrm{DNP}}(z)$ | DNP25 |
| F3 | classical $\lambda$-bracket leading coefficient | KhanZeng25 (genus 0 only) |
| F4 | symbol of GZ commuting Hamiltonians on $\mathbb{P}^1$ | GZ26 |
| F5 | Drinfeld $r$-matrix $k\,\Omega_{\mathrm{tr}}/z$ | Drinfeld 1985 |
| F6 | Sklyanin Poisson bracket | STS83 |
| F7 | kernel of FFR Gaudin Hamiltonians | FFR94 |

### 1.2 Steelman defense

The seven-face theorem is **structurally sound** as an organizational
principle. The arrows F1↔F5↔F7 are classical: the Drinfeld $r$-matrix and the
Gaudin kernel are tautologously the simple-pole projection of the Casimir, and the
shadow/KZ comparison theorem (`thm:shadow-connection-kz`, cited as
`ProvedElsewhere`) supplies the F1↔F5 identification for $\widehat{\mathfrak g}_k$.
The classical Sklyanin bracket of F6 IS by definition the antisymmetric part of
F5 lifted to $\mathfrak g^*$, so F5⇔F6 is one definitional unwinding.

The genuine new content is **F1↔F2↔F4** and the universality claim "for every
modular Koszul $\cA$." The F1=$\pi_\cA$ identification rides on
`thm:collision-residue-twisting`, the bar-intrinsic MC theorem.

### 1.3 Adversarial attack: what's actually new?

**AP155 finding (overclaiming novelty)**. The chapter's seven-face decomposition
recovers known invariants (Drinfeld $r$-matrix; Sklyanin bracket; Gaudin kernel)
under unified labels. The headline number "seven" is misleading:
- F5, F6, F7 are not three distinct objects but three names for the affine KM
  Casimir/$z$ (this is acknowledged in the proof of F7 by the level rescaling
  $H^{\mathrm{Gaudin}}_i = (k+h^\vee)\sum_{j\neq i} r_{\widehat{\mathfrak g}_k}(z_i-z_j)$
  which says F7 is F5 with a $(k+h^\vee)$ prefactor and F6 is the antisymmetric
  part of F5 evaluated on $\mathfrak g^*$). The real distinct faces are F1, F2,
  F3, F4, F5: at most **five**, not seven.
- F2 (DNP) and F4 (GZ) are recent papers from 2025–26 whose own theorems already
  identify their constructions with bar-cobar twisting morphisms; the
  "identification" in this chapter is a citation chain, not new mathematics.
- F3 is restricted to "genus 0 only" in the current revision (good — this is
  honest scope reduction), so it does not contribute to the "all genera"
  master statement.

**Action item (not a downgrade — a *re-presentation*)**: rename the result
*Five-face master theorem* with the affine-KM specialization rolled into one
face, OR add explicitly that F5/F6/F7 are three readings of one underlying
object. The current presentation triple-counts the Casimir.

### 1.4 The $U_\cA$ thesis (lines 41–110, 790–842)

The chapter introduces a "single boundary–bulk algebra"
$U_\cA := \cA \bowtie \cA^!_\infty$ (the Drinfeld double of $\cA$ and its
Verdier-dual factorization companion) and asserts that the six-tuple
$\mathcal H(T) = (\cA, \cA^!, \cC, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$ is
the projection of $U_\cA$ under six functors
(`prop:hdm-u-a-recoverability`, `ClaimStatusHeuristic`).

**Steelman**: The Drinfeld-double assembly is a *natural language* for the
boundary–bulk dictionary; the bowtie symbol $\bowtie$ is well-defined for
matched pair Lie bialgebras, and the proposition is correctly tagged Heuristic.

**Attack — AP-CY63 / AP-CY66 propagation** (geometric vs algebraic chiral
endomorphism operad; BZFN ambient category not tunable).
1. The bowtie $\cA \bowtie \cA^!_\infty$ is an unconstructed object at the
   *chain* level for non-formal $\cA$. The matched-pair Drinfeld double makes
   sense for Lie bialgebras and finite quantum groups, but for chiral algebras /
   factorization algebras the construction is conjectural at the same depth as
   CY-A_3. Calling $U_\cA$ "the boundary–bulk algebra" without flagging this
   conditionality is a **AP-CY79 candidate** (confabulated quantum-group-style
   structure).
2. Items (R1)–(R6) of the recovery proposition are tagged "unconditional for
   modular Koszul $\cA$" except (R2). But (R5) "the bar-intrinsic differential
   on the convolution dg Lie algebra associated to $U_\cA$ produces $\Theta_\cA$"
   uses the convolution algebra of $U_\cA$, which doesn't exist independently of
   the bowtie construction. The unconditional tag is suspect.
3. The "boundary–bulk reconstructor" language imports the AdS/CFT slogan into
   pure algebra. Either (a) state which *physical* boundary–bulk pair this is
   modeling, or (b) drop "reconstructor" and call $U_\cA$ what it is: a
   *conjectured* matched-pair structure on $\cA \otimes \cA^!_\infty$.

**First-principles content (the ghost theorem)**. The TRUE result hidden in
this thesis is: when the formal universal twisting morphism
$\pi_\cA \in \mathrm{Tw}(\barB(\cA), \cA)$ admits a matched-pair refinement,
the convolution algebra carries a Drinfeld-double bracket. This is a theorem
about *coalgebra–algebra pairs with an MC element*, NOT about chiral algebras
specifically. AP-CY7 analogue: the CoHA-style assembly is associative; the
chiral twist is a *separate* assumption.

### 1.5 Falsification principle and "when two faces disagree"

The closing principle (lines 1107–1147) is methodologically sound and
explicitly documents two past errors caught by the seven-face method (the
$1/(k+h^\vee)$ normalization and DNP non-renormalization vs. $\beta\gamma$).
This is the **gold standard for falsifiability** in the chapter.

### 1.6 Verdict on `holographic_datum_master.tex`

**Mostly proved; one flag, one re-counting.**
- The collision residue identification F1↔F5 is solid for affine KM.
- F2, F4 should be tagged as *citations to recent papers* not *new
  identifications*.
- The "seven" should be honest: F5/F6/F7 are repackagings of the affine KM
  Casimir.
- The $U_\cA$ Drinfeld-double thesis is correctly Heuristic but the
  "reconstructor" prose oversells.

**Not a downgrade; a presentation reform.**

---

## Section 2. `frontier_modular_holography_platonic.tex` audit

### 2.1 What is "Platonic" here?

The word "Platonic" is **not** about Platonic solids or icosahedral symmetry.
It is a metaphor for "the eternal idea behind the visible appearances": the
holographic modular Koszul datum is the *Platonic form* whose seven shadows on
the seven faces of section 1 are the visible projections (`rem:platonic-summary`,
`rem:mature-platonic-statement`).

**Steelman**: the metaphor is consistent with the chapter's thesis (one MC
element behind many visible structures).

**Attack**: zero physical/mathematical content per se. AP106 (CG opening
violation) lite — the word "Platonic" is decorative. Recommend keeping as
informal section name only.

### 2.2 Modular holography on the proved core (Section 1)

The opening (lines 1–60) lists four ingredients from the proved core (bar–cobar,
Verdier intertwining, complementarity decomposition, scalar genus package
`obs_g = κ·λ_g`). It then declares **43 proved claims and 8 conjectured items**
(`rem:frontier-holography-census`).

The proved theorems include:
- `thm:frontier-protected-bulk-antiinvolution` (Koszul-dual involution): genuine
  consequence of bar–cobar duality + Verdier intertwining.
- `thm:frontier-transposition-cotangent` (shifted cotangent realization
  $\mathbf C_g(\cA) \simeq V_g(\cA) \oplus V_g(\cA)^\vee[-d_g]$): genuine
  consequence of complementarity + dimension count.
- `cor:frontier-spectral-reciprocity-palindromicity` (palindromicity, even-genus
  vanishing): clean cohomological corollary.
- `lem:frontier-determinant-parity`, `thm:frontier-weyl-pbw-linear-sewing`,
  `thm:frontier-gaussian-composition-schur-anomaly`,
  `thm:frontier-metaplectic-cocycle-strictification`,
  `cor:frontier-first-nonlinear-holographic-anomaly`: these are
  **finite-dimensional linear algebra over a perfect dg model**, with explicit
  Schur-complement formulas and a metaplectic 2-cocycle. These are SOLID
  (basically Weil/Shale/Segal Gaussian sewing).

**Steelman defense**: this section is the **most honest** in the chapter set
because:
1. Every proved theorem reduces to finite-rank linear algebra on perfect dg
   models;
2. The H/M/S level decoration (`framework:fwk:frontier-holography-dependencies`)
   makes the dependency tree explicit;
3. The single conjecture (`conj:frontier-bulk-enhancement-universal-mc`,
   "3d bulk factorization algebra") is correctly conjectured.

**Attack**: this is genuinely fine. The content IS proved; the "holographic"
labelling is the only place where physical-overreach risk lives, and it is
contained by the Heuristic tag on `prop:hdm-u-a-recoverability` and the
Conjectured tag on `conj:frontier-bulk-enhancement-universal-mc`.

### 2.3 Holographic modular Koszul datum (lines 1119–1199)

The 6-tuple $\mathcal H(T) = (\cA, \cA^!, \cC, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$
is defined here, and superseded later by an 8-tuple "completed Platonic datum"
$\Pi^{\mathrm{oc}}_X(\cA)$ (Definition `def:thqg-completed-platonic-datum`,
lives in `thqg_open_closed_realization.tex`), which adds chiral derived center,
annulus trace, and nonlinear resonance tower.

**Cross-file definition: VERIFIED EXISTS** at
`thqg_open_closed_realization.tex:1624`.

### 2.4 The Yangian extraction in the holographic datum

**AP-CY79 propagation check**. The chapter does NOT claim a
"gravitational Yangian Y(Vir_13)" or any other confabulated algebra. The line
$\mathcal C \simeq \cA^!\text{-}\mathsf{mod}$ is a meromorphic tensor category
(line operators of DNP), and the explicit affine identification with
Kazhdan–Lusztig
$\mathcal C(\widehat{\mathfrak g}_k) \simeq \mathcal O_{k'}(\widehat{\mathfrak g})
\simeq \mathcal C(U_q(\mathfrak g))$
is in `thqg_introduction_supplement.tex` line 142, citing
`thm:kazhdan-lusztig-equivalence` (ProvedElsewhere). This is correct for
generic $k$.

### 2.5 Verdict on `frontier_modular_holography_platonic.tex`

**STRONG GREEN.** This file is the second gold standard (after entanglement_modular_koszul.tex).
The content IS proved at the level claimed. The "Platonic" prose is
decorative-only; the underlying mathematics is finite-rank linear algebra.

---

## Section 3. THQG entanglement programme audit

### 3.1 `thqg_introduction_supplement.tex` and `_body.tex`

**Why a supplement?** The supplement provides the "from bar complex to
holographic datum" derivation in self-contained form. The main file
`thqg_introduction_supplement.tex` is 226 lines, and `\input{...}`s the body
file (3010+ lines). This split is a **mega-file containment** (cf AP-CY52);
together they exceed the 3000-line guideline.

**Live or archive?** Live: the file is included in `chapters/frame/heisenberg_frame.tex:4913`.

**Audit of theorems against AP155**:
- `thm:thqg-intro-collision-twisting` (collision residue = twisting morphism;
  ProvedElsewhere): re-statement of the proved core, OK.
- `thm:thqg-intro-arnold-cybe` (CYBE from Arnold; ProvedElsewhere): standard
  via `thm:collision-depth-2-ybe`, OK.
- `thm:thqg-intro-shadow-kz` (KZ from shadow on affine KM surface;
  ProvedElsewhere): standard via `thm:shadow-connection-kz`, OK.
- `thm:thqg-intro-quartic-linfty` (quartic obstruction = $L_\infty$ bracket;
  ProvedElsewhere): standard via `prop:shadow-massey-identification`, OK.

All four theorems are tagged ProvedElsewhere with explicit cross-references.
Honest.

**Bulk-boundary-line triangle** (lines 80–162 of body): the construction is
narrative-heavy. The "boundary algebra is $\cA$ itself", "bulk is the ambient
complex $\mathbf C_g$", "lines is $\cA^!\text{-mod}$" is a labelling, not a new
theorem. AP-CY57 mild violation: "the three vertices of the holographic
triangle assemble into a commutative triangle" needs to be a *theorem*
(commutativity of the bar functor with Verdier duality), not a description.
Actually `thm:frontier-protected-bulk-antiinvolution` proves item (iii) of the
triangle, so the architecture is solid.

### 3.2 `thqg_entanglement_programme.tex`

**Headline result, lines 100–143** (`rem:thqg-two-entanglements`). The
chapter explicitly cautions that
$\mathcal H_g(\cA) = Q_g(\cA) \oplus Q_g(\cA^!)$ is a **direct sum, not a
tensor product**, and "carries classical correlations but not quantum
entanglement." This is HONEST. It's the kind of distinction wave 4 found
missing in the 3DQG standalone.

**Theorem `thm:thqg-lagrangian-constraint`** (Lagrangian constraint;
ProvedHere): five-part proposition giving:
- (i) complementarity sum $C_g + C_g^! = \dim \mathcal H_g$
- (ii) genus-1 structure $C_1 = C_1^! = 1$
- (iii) self-dual halving
- (iv) scalar one-dim contribution
- (v) Virasoro $F_g(\mathrm{Vir}_c) + F_g(\mathrm{Vir}_{26-c}) = 13 \lambda_g^{\mathrm{FP}}$

All five parts cite proved core theorems. SOLID.

**Conjecture `conj:thqg-spatial-entanglement`** (spatial entanglement from
modules; Conjectured): explicitly tagged Conjectured. The reduced density
matrix $\rho_{\mathcal M}$ is *posited* to exist; this is the right
epistemic level.

**`conj:thqg-qes-identification`** (QES from approximant; Conjectured): the
identification of $S_{\mathrm{QES}}^{(g, \le r)}$ with the physical QES area +
bulk corrections is correctly Conjectured because it requires a gravitational
dual.

**Theorem `thm:thqg-qes-convergence`** (ProvedHere): convergence of the QES
approximant series follows from `thm:recursive-existence` and shadow growth.
LEGITIMATE — the convergence is purely about the algebraic shadow tower.

**AP-CY81 propagation check** (Cardy state vs MC element): the entanglement
programme avoids treating Cardy states as MC elements. Good.

**AP-CY82 propagation check** (algebraic identity vs physical theorem): the
chapter is *meticulous* about this. Every "algebraic Page bound" carries
"saturation by a physical entanglement entropy is conjectural" disclaimers.

### 3.3 Verdict on THQG entanglement programme

**STRONG GREEN.** The supplement and entanglement-programme files
together with `entanglement_modular_koszul.tex` form a gold-standard set
for honest physical-mathematical correspondence.

---

## Section 4. `entanglement_modular_koszul.tex` — gold standard pattern extraction

This file (Wave 4 already noted as gold standard) earns the title because:

### 4.1 What discipline does it have?

1. **Epistemic scope notice in the chapter abstract** (lines 56–77): explicitly
   states what is imported (Calabrese–Cardy via twist operator dimension), what
   is new (degree-3+ shadow corrections), what is conjectural (FLM
   identification).
2. **`ClaimStatusProvedElsewhere` for imported results** (e.g. twist operator
   dimension): no inflation.
3. **Heuristic / Conjectured tags for the holographic identifications**:
   - `conj:ent-qes` (QES from shadow): Conjectured;
   - `conj:ent-page-curve` (Page curve from Koszul complementarity): Conjectured
     with explicit "epistemic note" warning that physical identification is
     heuristic;
   - `cor:ent-page-self-dual` (self-dual Page curve): Heuristic;
   - `rem:page-curve-complementarity` (LOCAL: scope-fixed): explicitly says
     "the identification of shadow corrections with FLM bulk entropy
     corrections requires a gravitational dual and is heuristic";
   - `conj:ent-desitter` (de Sitter from Wick): Conjectured;
   - `conj:ent-jt-shadow` (JT gravity from shadow tower): Conjectured.
4. **No "gravitational Yangian" or other confabulated structure**: the
   chapter never names a quantum group/Yangian, Koszul S-duality, etc. that
   doesn't already exist.
5. **BTZ entropy theorem** (`thm:ent-btz-entropy`, ProvedHere): three parts,
   each derivation explicit. Three-route verification at genus 1
   (`rem:ent-btz-three-routes`). Multi-path verification mandate satisfied.
6. **Standard landscape census** (`thm:ent-landscape-census`, ProvedHere): six
   families, exact $\kappa$ values, exact $S_{\mathrm{EE}}^{\mathrm{sc}}$
   coefficients, shadow class, convergence status. Tested with 72 tests in
   `compute/tests/test_entanglement_shadow_engine.py`. Multi-path verified.

### 4.2 Pattern abstraction (gold standard template)

For any holographic claim:
```
1. State the algebraic content as a theorem with proof.
2. Tag the physical identification as Conjectured/Heuristic.
3. Provide an "epistemic scope" remark BEFORE the theorem block.
4. Give independent computation paths (3-route mandate).
5. Use \ClaimStatusProvedElsewhere for imported physics inputs.
6. Use \ClaimStatusConjectured/Heuristic for output identifications
   that require a gravitational dual.
```

This is the **wave 4 gold standard** that 3DQG and (less critically) the
holographic codes file should adopt.

---

## Section 5. First-principles analyses (AP-CY61)

### 5.1 The 3DQG "gravitational Yangian Y(Vir_13)" (AP-CY79 candidate, propagated)

**Wrong claim** (3DQG standalone, lines 2645–2789):
"The gravitational Yangian $\mathcal Y_{\mathrm{grav}}$ is the algebra of
conserved charges of the shadow obstruction tower at $c = 13$, acting on the
ordered bar complex $\bar B^{\mathrm{ord}}(\mathrm{Vir}_{13})$."

**First-principles analysis**:
- The shadow tower $\{S_r\}_{r \ge 2}$ at $c = 13$ is a sequence of explicit
  rationals: $S_2 = 13/2$, $S_3 = -13$, $S_4 = 10/1131$, $S_5 = -48/14703$.
  These are *numbers*, not generators of an algebra.
- Calling the closure of these numbers under "RTT relations" a "Yangian" is
  category abuse: the Yangian $Y(\mathfrak g)$ is the deformation of the
  enveloping algebra of $\mathfrak g[\![z]\!]$, requiring a Lie algebra input.
  $\mathfrak{vir}$ is a Lie algebra, but $Y(\mathfrak{vir})$ is **not a
  standard construction**; the Yangian construction works for finite Lie
  algebras and (with care) affine ones, not Virasoro.
- The "RTT" relation `eq:yangian-rtt` is written down with no specification
  of $T(z)$; this is the classic narration-vs-construction failure (AP-CY57).

**Ghost theorem (the truth at the heart)**: the shadow tower at the
Koszul-self-dual point $c = 13$ has **enhanced symmetry** — the polynomial
ring it generates is fixed by the Koszul involution $c \mapsto 26-c$. This is
real. But "enhanced symmetry of a polynomial ring" is not "Yangian."

**Confusion type**: native/derived (claim makes a derived structure
sound native), label/content (Yangian label, polynomial-ring content),
construction/narration (RTT written without $T(z)$).

**Action**: rename "gravitational Yangian" to "shadow polynomial ring at
$c = 13$ with Koszul $\mathbb Z/2$ symmetry." Downgrade the conjecture to
"the shadow algebra at $c = 13$ has enhanced symmetry; the precise quantum
group structure (if any) is open."

### 5.2 The "Koszul S-duality" mislabel (AP-CY80 candidate)

**Wrong claim** (3DQG, line 987): "Koszul duality as gravitational S-duality."

**First-principles analysis**:
- The Koszul involution on Virasoro is the additive $c \mapsto 26 - c$
  reflection, which is the Feigin–Fuchs duality of the Liouville/free-field
  realization. This is an *additive* automorphism of central charges.
- S-duality in 3d gravity (or any QFT) is a *multiplicative* SL(2, Z)
  involution on coupling constants, e.g. $\tau \mapsto -1/\tau$. The two are
  not the same operation.
- They DO coincide at $c = 13$ (the fixed point of Feigin–Fuchs) and at the
  $S$-self-dual point $\tau = i$, but coincidence at one fixed point is not
  identification.

**Ghost theorem**: $(\mathrm{Vir}_c, \mathrm{Vir}_{26-c})$ is a Koszul pair
under the bar–cobar $L_\infty$ duality, and the central charges sum to the
Virasoro Koszul conductor $K = 26$. This is a clean statement about the
chiral algebra. Calling the Feigin–Fuchs reflection "S-duality" appropriates
a specific term from physics.

**Confusion type**: label/content, specific/general (one fixed-point
coincidence does not equate two operations).

**Action**: rename "Koszul S-duality" to "Feigin–Fuchs Koszul reflection"
or "central-charge complementarity." Reserve "S-duality" for genuine
$\tau$-modular phenomena.

### 5.3 BTZ-as-MC element (AP-CY81 candidate)

**Wrong claim** (3DQG, lines 1746–1771): "The BTZ black hole of mass $M$
and angular momentum $J$ is a Maurer–Cartan element
$\alpha_{\mathrm{BTZ}} = h\,e_h + \bar h\,e_{\bar h}$ in $\mathfrak g^{\mathrm{mod}}_{\mathrm{Vir}_c}$."

**First-principles analysis**:
- The BTZ black hole IS a flat $SL(2, \mathbb R)$ connection on the solid
  torus with prescribed holonomy. In the boundary CFT, it IS a state
  $|h, \bar h\rangle$ in the Hilbert space — i.e., a **module element**, not
  an algebra element.
- A Maurer–Cartan element of $\mathfrak g^{\mathrm{mod}}_{\mathrm{Vir}_c}$
  is a degree-1 element of the *deformation complex* satisfying $D\alpha +
  \frac12[\alpha, \alpha] = 0$. Its meaning is "an infinitesimal deformation
  of the chiral algebra structure," not "a state in some module."
- The "proof" claims that $|h, \bar h\rangle$ satisfies the conformal Ward
  identities, which "are exactly the components of the MC equation projected
  to the boundary." This is **wrong category**. Conformal Ward identities are
  conditions on a state (a vector in a module), not on an algebra element.

**Ghost theorem**: BTZ has a clean algebraic shadow:
- The character of the highest-weight Virasoro module $V_{h, \bar h}$ at
  $c = 3\ell/(2G)$ encodes the BTZ partition function via Cardy.
- The corresponding *automorphism* of $\mathrm{Vir}_c$ (the spectral flow by
  $h$) is an algebra element, but it's an automorphism, not an MC element.

**Confusion type**: object/structure (state vs algebra element); algebra/coalgebra
(state ∈ comodule, MC ∈ algebra). The misnaming changes which equation BTZ
must satisfy.

**Action**: replace "BTZ is an MC element" with "BTZ corresponds to a Virasoro
highest-weight state $|h, \bar h\rangle$ in the module category"; "the modular
characteristic class $\Theta_\cA$ governs the gravitational corrections to the
BTZ saddle through its evaluation on the BTZ background." This preserves the
algebraic content without category error.

### 5.4 Holographic codes K4 ⇔ K4 tautology (AP-CY87 propagation)

**Claim** (`thm:hc-koszulness-exact-qec`, ProvedHere):
(i) $\cA$ is chirally Koszul ⇔ (ii) $\Omega(B(\cA)) \xrightarrow{\sim} \cA$
⇔ (iii) every bulk operator in $C^\bullet_{\mathrm{ch}}(\cA, \cA)$ is recoverable.

**Honest in proof**: the proof of (i) ⇔ (ii) explicitly says "this is
condition K4; the equivalence is **tautological**" (line 353). Good — the
chapter declares the tautology.

**The non-tautological content** is (ii) ⇒ (iii) and (iii) ⇒ (i), the
extension to the chiral Hochschild complex via functoriality. This is genuine.

**Code distance d = 2** (`rem:hc-universal-parameters`, lines 676–688):
"the minimum weight of a detectable error is the bar degree shift, which
equals 2 (the desuspension $s^{-1}$ has degree $-1$, so the first nontrivial
bar element has degree 2)."

**Adversarial attack**: this conflates the bar augmentation degree with the
QECC code distance. In quantum error correction:
- Code distance $d$ = minimum Hamming weight of an undetectable Pauli error
- Bar degree shift = the homological degree of the first nontrivial cycle in
  $B(\cA)$

These are **different** concepts. The bar degree is an internal grading on
the algebraic encoding; QECC distance is a metric on the physical space
of operators with respect to a tensor product structure.

The claim "$d = 2$ universal" follows from "bar degree starts at 2" under
the *assumption* that bar degree = QECC distance, which is unproven and
likely false (the chapter's own remark line 661 admits "the symplectic
code is not orthogonal", which already breaks the standard QECC framework).

**Action**: tag the claim "d = 2" as *structural analogy*, not theorem.
The chapter already tags row K11 as "$\star$" with footnote "conditional on
perfectness/nondegeneracy" — extend the same caveat to the universal d = 2
statement.

### 5.5 The $U_\cA$ Drinfeld double (AP-CY79 candidate, second instance)

Already discussed in §1.4. The "boundary–bulk reconstructor" $U_\cA = \cA
\bowtie \cA^!_\infty$ is conjectural at the chain level for non-formal
chiral algebras. Its tag (`prop:hdm-u-a-recoverability`,
`ClaimStatusHeuristic`) is correct, but the surrounding prose in
`sec:hdm-thesis` reads as if $U_\cA$ exists. Recommend prefacing
`sec:hdm-thesis` with an explicit existence caveat: "the construction of
$U_\cA$ as an honest matched-pair structure is conjectural and parallels
the CY-A_3 saga; the proposition is heuristic accordingly."

---

## Section 6. Three upgrade paths

The user requested upgrade paths, not downgrades. Each downgrade above can be
turned into a clean upgrade by *narrowing scope*.

### 6.1 Upgrade Path A — *Universal Koszul–Holographic theorem with explicit dictionary*

**Claim**: For every modular Koszul chiral algebra $\cA$ on a smooth
projective curve $X$, there is a **canonical functor**
$\Phi^{\mathrm{hol}}_X : \mathrm{ModKoszul}(X) \to \mathrm{HoloDatum}_6$
sending $\cA \mapsto (\cA, \cA^!, \cC, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$,
where $\mathrm{HoloDatum}_6$ is the 1-category whose objects are 6-tuples
satisfying the four consistency conditions C1–C4 of
`rem:hdm-four-consistency-conditions` (modulo the tagged conditional content).

**Status**: provable as a theorem if we replace "every modular Koszul" with
"every modular Koszul $\cA$ for which the bar–cobar inversion holds at the
chain level." The functor exists at the homotopy-categorical level on the
Koszul locus.

**This is genuinely new**: it converts the prose-level "the holographic datum
is a functor of $\cA$" into a precise categorical statement, and exposes the
two non-trivial datapoints (the conditionality of $\cA^!_\infty \to \cA^!$
and of the bulk factorization algebra) as two clean conditions on the target
category.

### 6.2 Upgrade Path B — *Holographic codes from Koszul pairs: explicit construction*

**Claim**: For every chirally Koszul pair $(\cA, \cA^!)$, there is an
**explicit symplectic stabilizer code** $[[n, k, d]]_{\cA}$ where:
- $n = \dim_\C \mathbf C_g(\cA)$ (physical Hilbert space)
- $k = \dim_\C \mathbf Q_g(\cA) = n/2$ (logical, Lagrangian)
- $d$ is the **Verdier-pairing distance**: the minimum dimension of a
  subspace $E \subset \mathbf C_g(\cA)$ such that $E$ has nontrivial Verdier
  pairing with both $\mathbf Q_g(\cA)$ and $\mathbf Q_g(\cA^!)$.

**Status**: this $d$ is finite-rank linear algebra at each genus, computable
on perfect dg models. The current chapter's "$d = 2$ universal" claim
collapses to this *Verdier-pairing distance*, which is genus-dependent and
can be computed for the standard landscape.

**Genus-1 instance**: $d_1 = 1$ (since $\dim \mathbf Q_1(\cA) = 1$ for
all standard families, every nonzero error is detectable). For $g = 2$ and
above, $d_g$ depends on the family.

This is the kind of *concrete invariant* that replaces the over-broad
"$d = 2$" claim.

### 6.3 Upgrade Path C — *AdS3/CFT2 entanglement-modular dictionary as
chain-level equivalence*

**Claim** (the gold-standard analogue for entanglement_modular_koszul.tex):
For every modular Koszul Virasoro algebra at central charge $c$, there is a
**chain-level equivalence**
$\mathrm{Mod}_{\mathrm{Vir}_c} \simeq^{\mathrm{ch}} \mathrm{Mod}_{\mathrm{Vir}_{26-c}}^{\mathrm{Koszul-dual}}$
between the module category of $\mathrm{Vir}_c$ and the Koszul-dual module
category, intertwining the **shadow Hamiltonian** (= modular Hamiltonian
at chain level) with the Verdier involution.

**Status**: provable at the cohomological level via the proved
complementarity theorem. The chain-level version requires the bar-cobar
inversion at the chain level (Theorem B), which IS proved on the Koszul
locus.

**This is genuinely new** because it gives a precise mathematical
counterpart to the modular flow ↔ Tomita–Takesaki dictionary that
entanglement_modular_koszul.tex calls "structural" — and upgrades it to a
chain-level statement on the Koszul locus.

---

## Section 7. Punch list (prioritized)

### Tier 1 (presentation reform, no math change)

1. **`holographic_datum_master.tex`**: rename "seven-face" to either
   "five-face master theorem" with the affine KM specialization rolled into one
   face, OR add a remark explicitly noting that F5/F6/F7 are three readings of
   one underlying object.
2. **`holographic_datum_master.tex`** (lines 30–110): preface
   `sec:hdm-thesis` with: "the construction of $U_\cA$ as an honest matched-pair
   structure is conjectural at the chain level for non-formal $\cA$; the
   `ClaimStatusHeuristic` tag on `prop:hdm-u-a-recoverability` propagates
   accordingly."
3. **`holographic_codes_koszul.tex`** (lines 676–688): add caveat to
   "$d = 2$ universal" — tag as structural analogy, not theorem;
   alternative: replace with the *Verdier-pairing distance* of Upgrade Path B.

### Tier 2 (rename to remove confabulation)

4. **3DQG standalone** (lines 2645–2789): rename "gravitational Yangian" to
   "shadow polynomial ring at $c = 13$." Specifically retract:
   - "The gravitational Yangian $\mathcal Y_{\mathrm{grav}}$ is the algebra
     of conserved charges of the shadow obstruction tower at $c = 13$"
     → "The shadow polynomial ring $\mathcal P_{c=13}$ generated by
     $\{S_r(\mathrm{Vir}_{13})\}_{r \ge 2}$ is fixed by the Koszul $\mathbb
     Z/2$ involution $c \mapsto 26-c$."
   - "The shadow connection $\nabla^{\mathrm{hol}}$ is the generating function
     of the Yangian generators" → drop "Yangian generators"; just call it the
     generating function of shadow projections.
   - `def:gravitational-yangian` → restate without "Yangian" claim;
     `thm:gravitational-yangian` parts (i)–(iv) are valid as-is *if* the word
     "Yangian" is replaced by "shadow algebra"; part (v) on the
     "self-dual braiding" needs additional caveat.
5. **3DQG standalone** (line 987): rename `sec:koszul-s-duality` →
   `sec:koszul-feigin-fuchs`. Retract "S-duality" terminology;
   replace with "Feigin–Fuchs Koszul reflection" or "central-charge
   complementarity."
6. **3DQG standalone** (lines 1746–1771): retract `thm:btz-mc`. Replace with:
   "BTZ corresponds to a highest-weight state $|h, \bar h\rangle$ in the
   Virasoro module $V_{h, \bar h}$. The shadow MC element $\Theta_\cA$
   evaluated on this state produces the genus expansion of the BTZ partition
   function." This preserves the algebraic content; removes the category
   error.

### Tier 3 (status correction)

7. **3DQG standalone** all `\begin{theorem}` blocks downstream of
   "BTZ is an MC element": review whether the theorem still holds after the
   restatement. In particular `thm:vir-koszul-mc` and the algebraic Page
   curve theorem. Most should survive (the algebra is clean; only the
   physical interpretation needs care), but tagging review is needed.

### Tier 4 (cache write-back, AP propagation)

8. **`appendices/first_principles_cache.md`**: append entries 51–55 from
   §5 of this report:
   - 51: "Gravitational Yangian Y(Vir_13)" confabulation (AP-CY79)
   - 52: "Koszul S-duality" mislabel of additive Feigin–Fuchs reflection (AP-CY80)
   - 53: BTZ-as-MC algebra/coalgebra category error (AP-CY81)
   - 54: Algebraic Page curve identity vs physical Page curve theorem (AP-CY82)
   - 55: Bar-degree-2 ≠ QECC code distance (AP-CY87)
9. **`notes/tautology_registry.md`**: add `thm:hc-koszulness-exact-qec`
   parts (i) ⇔ (ii) as a documented tautology (the chapter already says so).
10. **CLAUDE.md** AP-CY catalogue: integrate AP-CY79–82, AP-CY87 if not
    already present (cross-check with the AP-CY catalogue).

### Tier 5 (upgrade paths, new content)

11. Implement **Upgrade Path A** (universal Koszul–holographic functor as
    1-category statement): natural target for a future proposition in
    `frontier_modular_holography_platonic.tex` Section 1.
12. Implement **Upgrade Path B** (Verdier-pairing distance for symplectic
    holographic codes): replace `rem:hc-universal-parameters` line 676–688.
13. Implement **Upgrade Path C** (chain-level chiral entanglement-modular
    dictionary): natural target for a new proposition in
    `entanglement_modular_koszul.tex` after `thm:entanglement-complementarity`.

---

## Coda: gold-standard ranking

From this audit, the holographic frontier files rank as follows on
*epistemic discipline*:

| Rank | File | Reason |
|------|------|--------|
| 1 | `entanglement_modular_koszul.tex` | Explicit epistemic scope, Conjectured/Heuristic tags throughout, no confabulated structures, multi-path verification |
| 2 | `frontier_modular_holography_platonic.tex` | Finite-rank linear algebra throughout, single Conjectured tag, H/M/S level decoration, honest 43/8 census |
| 3 | `thqg_entanglement_programme.tex` | Direct-sum vs tensor-product caveat is exemplary; QES correctly Conjectured |
| 4 | `thqg_introduction_supplement(_body).tex` | Most theorems ProvedElsewhere; mild AP-CY57 narration risk in triangle assembly |
| 5 | `holographic_datum_master.tex` | Seven-face is a five-face triple-counted; $U_\cA$ thesis oversells Heuristic content |
| 6 | `holographic_codes_koszul.tex` | "d = 2 universal" overreach; otherwise solid; symplectic-vs-orthogonal caveat is well-handled |
| 7 | `standalone/three_dimensional_quantum_gravity.tex` | Most prone to AP-CY79/80/81/82 confabulations; needs the systematic renames of Tier 2 |

All seven files are *fixable* by presentation reform plus the targeted
renames and tag additions of Tiers 1–3. None require retraction of the
underlying algebraic content; the issues are uniformly at the
interpretation layer.
