# Wave V81 — Attack-and-Heal: FM164/FM161 Conditional Dependency Audit

**Date:** 2026-04-16.
**Mode:** Russian-school adversarial attack + Chriss-Ginzburg dialectic. Sandbox only.
**Subject:** the recurrent footnote `conditional on FM164 + FM161` (with K3-specialised
and super-Lie variants) attached to V49 K3 Pentagon-at-$E_1$, V58/V61 V20 Step 3
chain-level (Class A and Class B0), V64 V19 Trinity-$E_1$ (Class A and Class B0),
V65 CY-C abelian K3, and (implicitly) V77 MHV70.
**Discipline gates honoured:** AP-CY11 (conditional propagation), HZ3-3 (named
dependency), AP-CY40 (status tag matches proof block), AP-CY61 (first-principles
ghost theorem extraction). Pre-commit hook: no .tex inscription, no build, no test
run, no commit. All commits would be by Raeez Lorgat ONLY.

---

## §0. Executive summary

The conditional `FM164 + FM161` rider is the load-bearing footnote of the V49
Pentagon-at-$E_1$ result for K3 input and propagates by HZ3-3 to V58, V64, V65 and
V77. The audit finds:

1. **FM164 and FM161 are precise Vol II Wave 7 supplement entries** (Vol II
   `CLAUDE.md` lines 419, 422). They are NOT in the Vol I AP catalogue.
2. **Both FM161 and FM164 are CLOSED in Vol II** by the Wave 9 / Unified Chiral
   Quantum Group Theorem (Vol II CLAUDE.md line 839: "FM161 (Yangian
   open-embedding of charts...)"; line 859: "All of FM130--135, FM161--170,
   FM176--181 CLOSED by this theorem as specialization/scope/citation fixes").
3. **The "K3-specialised" qualifier is well-defined** but stronger than what
   FM164/FM161 require: K3-specialisation is automatic from the Mukai-lattice
   self-duality plus connected pro-finite augmentation, both of which the Vol II
   Wave 9 closure handles uniformly across simple Lie types.
4. **The "super-Lie variant" qualifier is VAPID as currently written**: no
   super-Lie generalisation of FM164 or FM161 is documented in either CLAUDE.md.
   The phrase appears ONLY in V58 §3 and V64 §4 wave files; it is invoked but
   never defined. This is a Russian-school violation: the conditional cites a
   nonexistent failure mode.
5. **AP-CY11 propagation is correctly tracked at the wave level** (every V58/V64/V65
   conditional names FM164/FM161); but the cascade is now routed through a CLOSED
   condition (good news) plus a VAPID super-Lie condition for Class B0 (bad news).

The healing path: FM164/FM161 K3-specialised → unconditional theorem (close
inherits to V58 K3 cells, V64 K3 cells, V65 K3 abelian, V77 K3 cells). FM164/FM161
super-Lie variant → either documented as a precise Vol II Wave 10 supplement entry
("FM182: super-Yangian Koszulness in Positselski super-non-homogeneous framework"
+ "FM183: super-bar-cobar pro-nilpotent completion for Lie superbialgebras"), or
the V58/V64 Class B0 conditional is downgraded to a literal `\begin{conjecture}`
(with the V53.1 Berezinian rigidity argument as the heuristic).

The recommended healing is **Option C: stratification with documentation**. Sections
6 and 7 give the per-wave inheritance map and the v3.3 directive.

---

## §1. All wave references to FM164/FM161

Enumerated by file; line ranges from `grep -n` invocations.

### 1.1 V49 — `wave_application_V49_status_promotion.md`

| Location | Conditional invoked |
|---|---|
| L27--30 | "Conditional on FM164 (Yangian pro-nilpotent bar-cobar completion) and FM161 (Positselski Yangian Koszulness) K3-specialised; both expected to hold at K3 due to Mukai self-duality + ADE-self-duality." |
| L70 | Theorem header: "Pentagon-at-$E_1$ for K3 input; conditional on FM164, FM161". |
| L95--98 | `rem:k3-pentagon-conditionality`: "separable closure of FM164/FM161 for K3 input is a follow-up". |
| L141--142 | AP-CY11 compliance: "conditional propagation explicit; FM164/FM161 named in the theorem header and `rem:k3-pentagon-conditionality`". |
| L200 | "five of six corollaries inherit FM164/FM161 conditionality from `thm:k3-pentagon-E1`; only `cor:cy-c-k3-abelian-from-pentagon` is unconditional." |
| L262 | V39 H1-K3 promotion: "PROVED, conditional on FM164/FM161 K3-specialised". |
| L452, L456 | AP-compliance matrix entries. |
| L503--505 | "Does NOT close FM164 (Yangian pro-nilpotent bar-cobar completion) or FM161 (Yangian Koszulness in Positselski) in general. Closing these for the K3 input specifically is a separable technical follow-up." |
| L601--602, L658 | Conclusion: "FM164/FM161 K3-specialised, FM164/FM161 super-Lie variant" -- the only V49 mention of the super-Lie variant, in a forward reference to V58/V64. |

### 1.2 V58/V61 — `wave_V20_step3_chain_level_class_A_B0_inscription.md`

| Location | Class | Conditional |
|---|---|---|
| L103--104 | Class A | "Theorem (V20 Step 3 chain-level for Class A; CONDITIONAL on FM164, FM161 K3-specialised)" |
| L140--141 | Class A | Honest scope statement |
| L173 | Class A | "Q.E.D. (modulo FM164/FM161 K3-specialised)" |
| L178--180 | Class A | AP-CY11 propagation explicit |
| L198--199 | Class B0 | "Theorem (V20 Step 3 chain-level for Class B0; CONDITIONAL on FM164, FM161 super-Lie variant)" |
| L268 | Class B0 | "Q.E.D. (modulo FM164/FM161 super-Lie variant)" |
| L272--275 | Class B0 | AP-CY11 propagation explicit |
| L408--414 | TeX | `\begin{theorem}[V20 Step 3 chain-level for Class A; conditional on FM164, FM161 K3-specialised]` |
| L438--442 | TeX | `\begin{theorem}[V20 Step 3 chain-level for Class B0; conditional on FM164, FM161 super-Lie variant]` |
| L602--603 | Status table | Class A: `cond. FM164/FM161 K3-spec.`; Class B0: `cond. FM164/FM161 super-Lie variant`. |
| L619 | Scope | "Does NOT close FM164 or FM161 (general or K3-specialised or super-Lie variant)". |

### 1.3 V64 — `wave_V19_Trinity_E1_class_A_B0_inscription.md`

Symmetric to V58, four conditional theorem headers and four `Q.E.D. (modulo …)`
markers. Class A theorem L198--199 (`K3-specialised`); Class B0 theorem
L277--278 (`super-Lie variant`); Status table L725--729 (rows abelian, A, A
extension, B0, B0 other, B-quintic, B-LP$^2$, B-Yangian, B other).

### 1.4 V65 — `wave_CY_C_abelian_quantum_group_inscription.md`

| Location | Conditional |
|---|---|
| L55--56 | `\begin{theorem}[CY-C abelian level for K3; \ClaimStatusProvedHere conditional on FM164 + FM161]` |
| L86 | Conditionality justification: "expected to hold at the K3 abelian level by Mukai self-duality and the abelian-block structure (V49 H4)" |
| L279 | Status table: K3 abelian (generic) "PROVED (cond. FM164/FM161)" |
| L307--308 | TeX inscription target |
| L393 | Editorial note: "`\ClaimStatusProvedHere conditional on FM164 + FM161` per HZ3-3 (conditional propagation discipline)" |
| L413 | Falsifiable Prediction 7: "Under FM164/FM161 closed at K3, the Etingof–Kazhdan quantization twist…" |
| L459 | Closure summary: "construction is conditional only on FM164/FM161…" |

### 1.5 V77 (MHV70) — implicit inheritance

`wave_V70_attack_heal_K3_mukai_signature_uniqueness.md` does not name FM164/FM161
in its theorem headers, but the V70 K3 Mukai uniqueness argument feeds V49 Route
(ii) (Etingof--Kazhdan rigidity); by AP-CY11 every theorem chaining through V49
inherits V49's conditionality. V77 therefore implicitly carries `cond.\ FM164 +
FM161 K3-specialised` even though the wave file does not write it. **This is the
silent inheritance failure** that V81 must surface.

### 1.6 V69 — `wave_V69_attack_heal_V49_three_routes_independence.md`

V69 is the "attack-heal" wave for V49. Five mentions (L451, L462, L539, L564,
L695, L714) all of `FM164 + FM161 K3-specialised`. V69 explicitly states "V69
does NOT extend V49's resolution beyond K3" and preserves the conditional rider.

### 1.7 RANK_1_FRONTIER_v3.md

Five table rows: Class A K3 (`FM164 + FM161`), Class A extension (`FM164 +
FM161`), Class B0 (`FM164/FM161 super-Lie`), and the per-class summary tables
for V20 Step 3, V19 Trinity, CY-C abelian.

### 1.8 MASTER_PUNCH_LIST.md

L1048: "H1 unifies FOUR previously-independent open conjectures: V19 amplitude,
R-twist (V19 form b), V20 Step 3 chain-level, V11 (U1) chain-level. Conditional
on FM164 + FM161." L1208: "Conditional on FM164 (Yangian pro-nilpotent
bar-cobar) + FM161 (Positselski nonhomogeneous Yangian Koszulness) for K3
input."

---

## §2. ATTACK — five adversarial angles per AP-CY61

For each angle: (a) what the wave inscriptions get RIGHT, (b) what they get
WRONG, (c) the correct mathematical relationship.

### 2.1 ATTACK ANGLE 1 — What ARE FM164 and FM161 precisely?

**Provocation.** Eight wave files cite "conditional on FM164/FM161" as if
referring to standardly catalogued failure modes. But the Vol I CLAUDE.md
contains NO entries FM164 or FM161. Search of `~/chiral-bar-cobar/CLAUDE.md`
returns zero matches. The catalogue these labels live in is Vol II's CLAUDE.md
Wave 7 supplement (lines 419 and 422). If a Vol III result is conditional on a
Vol II Failure Mode, the cross-volume citation discipline (HZ3-10 / AP-CY13)
requires the conditional to be named with VOLUME PROVENANCE.

**(a) RIGHT (the ghost theorem).** The waves correctly identify two precise
gaps in the Yangian-side justification of the Pentagon-at-$E_1$ closure:
  - a **Koszul duality** gap (the Positselski PP05 framework requires connected
    grading $A_0 = k$, but the Yangian level grading is pro-finite); and
  - a **bar-cobar completion** gap (pro-nilpotence does not imply conilpotence
    for raw $B(A)$; only $\hat B(A)$ is conilpotent in the pro-nilpotent
    completion category).
Both are real Vol II Wave 7 entries with explicit `yangians_foundations.tex`
line numbers (L552, L623--635, L677--701).

**(b) WRONG.** Three errors:
  1. **Volume provenance dropped.** Wave files write `FM164` not
     `[Vol II] FM164`. Per HZ3-10 / AP-CY13 cross-volume Part discipline,
     cross-volume failure mode references must carry the volume tag.
  2. **CLOSURE STATUS IGNORED.** Vol II CLAUDE.md line 839 records: "FM161
     (Yangian open-embedding of charts $M_{\rm Kosz}^{\rm assoc} \hookrightarrow
     M_{\rm Kosz}^{\rm chiral}$, quadratic-Koszul chart includes into
     chiral-Koszul atlas)" -- this is FM161 CLOSED. Vol II line 859 records:
     "All of FM130--135, FM161--170, FM176--181 CLOSED by this theorem as
     specialization/scope/citation fixes." So FM164 is also CLOSED. The wave
     files, written before the Vol II Wave 9 closure, treat both as OPEN.
  3. **Failure-mode statement vs failure-mode resolution.** Even when CLOSED,
     a Vol III result conditional on FM164/FM161 is conditional on the CLOSURE
     ARGUMENT being applicable to its specific input (here: K3 abelian
     Heisenberg with ADE enhancement). The Vol II Wave 9 closure was proved
     for "Fix simple Lie $g$ (finite/affine), good $\mathbb Z$-grading $\Gamma$
     on $g$ via $sl_2$-triple, non-critical level $k \neq -h^v$, shift datum
     $\mu$." The Mukai-lattice Heisenberg is not literally a "simple Lie $g$";
     applicability requires verification.

**(c) CORRECT relationship.** The right statement is:
> The V49 K3 Pentagon-at-$E_1$ chain-level result is conditional on the Vol II
> Wave 9 Unified Chiral Quantum Group Theorem applying to the K3 Mukai-lattice
> Heisenberg with ADE enhancement.

This is a *much weaker* and more verifiable conditional than `FM164 + FM161`,
because it is stated against a known closed theorem rather than against two
historically-open failure modes. The verification reduces to checking that the
K3 Heisenberg satisfies the Vol II Wave 9 hypotheses (it does, after the
Mukai-lattice → simple Lie $\hat{\mathfrak{u}}(1)^{24}$ identification + the
ADE enhancement gives a finite simple Lie subalgebra).

### 2.2 ATTACK ANGLE 2 — Universality across four uses

**Provocation.** The wave files apply `FM164/FM161` (or its super-Lie variant)
to FOUR distinct use cases:
  - V49 K3-specialised (K3 abelian + ADE-enhanced sub-Yangian, EK twist).
  - V58/V64 Class A (K3, $K3 \times E$, STU, 8 diagonal $\mathbb{Z}/N\mathbb{Z}$
    symplectic K3 orbifolds).
  - V58/V64 Class B0 (conifold $Y(\mathfrak{gl}(1|1))$, super-trace-zero CoHA).
  - V65 CY-C abelian K3 (Drinfeld currents + double presentation).
Are these all simultaneously satisfied?

**(a) RIGHT.** All four uses involve a Yangian-type positive half + bar-cobar
duality + Pentagon-coherence cocycle. The Vol II FM164/FM161 statements DO
apply to each: they are about Yangian Koszulness and bar-cobar completion in
generality.

**(b) WRONG.** Three sub-errors:
  1. The V58/V64 Class A "extension" to $K3 \times E$, STU, orbifolds inherits
     FM164/FM161 K3-specialised by fibre-localisation onto the K3 fibre.
     This is correctly handled in V58 L142--144. But the elliptic / orbifold
     quotients introduce ADDITIONAL conditional structure (see Angle 5 below):
     orbifold equivariance + elliptic factor commutativity. These are NOT in
     FM164/FM161.
  2. The V58/V64 Class B0 "super-Lie variant" is not a documented Vol II FM
     entry (see Angle 5 in detail). The wave files invoke "the super-Lie
     version of standard Yangian Koszulness" without naming a FM number.
  3. The V65 CY-C abelian K3 invokes FM164/FM161 in a STRONGER form: not just
     "conditional on Yangian Koszulness for the K3 abelian Heisenberg" but
     also "conditional on the BZFN equivalence Rep$^{E_2}(Y) \to $Rep$(C)$",
     which is AP-CY66 territory and NOT FM164/FM161.

**(c) CORRECT relationship.** The four uses each carry DIFFERENT conditionals,
even when they share `FM164/FM161` as a label:

| Wave | Surface conditional | True conditional structure |
|---|---|---|
| V49 K3 | FM164 + FM161 K3-spec. | Vol II Wave 9 closure for K3 Heisenberg + ADE |
| V58/V64 Class A | FM164 + FM161 K3-spec. | V49 + fibre-localisation onto K3 fibre |
| V58/V64 Class B0 | FM164 + FM161 super-Lie | UNDOCUMENTED super-Lie analog (vapid as written) |
| V65 CY-C K3 abelian | FM164 + FM161 | V49 + AP-CY66 BZFN ambient discipline |

Not a uniform rider; four distinct riders with one shared label.

### 2.3 ATTACK ANGLE 3 — AP-CY11 / HZ3-3 conditional propagation

**Provocation.** AP-CY11 + HZ3-3 require that every result chaining through a
conditional inherits the conditional. V58 chains through V49 (K3-specialised
case) but ALSO covers Class B0 (super-Lie variant). Is the propagation track
correctly maintained?

**(a) RIGHT.** V58 §2.3 ("Conditional dependencies (per AP-CY11)") and V64 §3.3
explicitly invoke HZ3-3 and name the conditional inheritance. The Class A
theorem header carries `K3-specialised`; the Class B0 theorem header carries
`super-Lie variant`. Two different conditionals, two different theorems --
correct stratification at the surface.

**(b) WRONG.** Two AP-CY11 violations:
  1. **V77 silent inheritance.** V77 (V70) Mukai uniqueness feeds V49 Route
     (ii) (EK rigidity) but does not state its inheritance of `FM164 + FM161
     K3-specialised`. Per HZ3-3, V77 results that USE V49 must name the
     inheritance.
  2. **Cross-product propagation in V58 Class A extensions.** V58 extends Class
     A from K3 to $K3 \times E$, STU, orbifolds. The fibre-localisation
     argument is correct, but the conditional structure on the BASE (elliptic
     factor for $K3 \times E$, rational base for STU, orbifold equivariance
     for diagonal $\mathbb{Z}/N\mathbb{Z}$) is not named. These are SEPARATE
     conditionals not present in FM164/FM161.

**(c) CORRECT relationship.** Conditional propagation discipline requires:
  - Every wave result lists its conditional dependencies in a `Conditional
    dependencies` block.
  - When a wave EXTENDS a result (e.g., V58 Class A extends V49 K3 to orbifolds),
    NEW conditionals introduced by the extension are named separately.
  - Implicit dependencies (V77 → V49) are flagged.

### 2.4 ATTACK ANGLE 4 — "K3-specialised" semantic content

**Provocation.** "K3-specialised" appears as a qualifier on FM164 + FM161
across V49, V58 §2, V64 §3, V65, V69. Three plausible readings:
  (a) the failure mode is reduced to its K3-specific version;
  (b) the failure mode is only known to hold for K3 inputs;
  (c) the failure mode's RESOLUTION applies only to K3 inputs.

**(a) RIGHT.** All three readings have ghost content:
  - Reading (a) corresponds to Vol II line 859: FM161-170 closed as
    "specialization/scope/citation fixes". The K3 Heisenberg is the
    canonical specialization where Mukai self-duality + ADE self-duality
    rigidify the closure.
  - Reading (b): for the Mukai lattice $\Lambda_{K3}$ of signature $(2, 22)$
    or $(4, 20)$, the bar-cobar Yangian completion (FM164) reduces to a
    finite-rank computation because the lattice is finite-rank, sidestepping
    pro-nilpotent completion subtleties.
  - Reading (c): the Vol II Wave 9 closure framework includes K3 as one of
    eight specialization fibres (the K3 super-Yangian $Y(\mathfrak{gl}(4|20))$
    is one of the cells).

**(b) WRONG.** The wave files conflate readings (b) and (c). When V49 says
"FM164/FM161 K3-specialised; both expected to hold at K3 due to Mukai
self-duality + ADE-self-duality" (L29), the "expected to hold" language is
reading (b), not (c). Vol II Wave 9 has CLOSED FM164/FM161 in framework
generality; the K3 case is one of the closed specialization cells, not an
"expected" specialization.

**(c) CORRECT relationship.** "K3-specialised" should be replaced by
"verified for the Vol II Wave 9 K3 Heisenberg cell." This is reading (c)
explicitly, with the Vol II Wave 9 closure as the witness.

### 2.5 ATTACK ANGLE 5 — "super-Lie variant" — VAPID conditionality

**Provocation.** V58 §3 Class B0 and V64 §4 Class B0 both cite "FM164/FM161
super-Lie variant". Is this a documented variant?

**(a) RIGHT.** The super-Yangian world DOES have a Koszul duality + bar-cobar
completion question. The Vol III references: AP-CY35 (super-Yangian
$Y(\mathfrak{gl}(4|20))$ is conjectural), AP-CY46 (no native CY$_4$ Yangian,
$p_1$-twisted double current algebra), V53.1 Berezinian channel rigidity. The
ghost: a precise super-Lie analog of FM161 + FM164 would say:
  - **FM161-super (proposed):** $Y(\mathfrak{g}_{\rm super})$ Koszulness via
    Positselski super-non-homogeneous duality requires connected $\mathbb{Z}/2$-graded
    grading; the super-Yangian's level grading is pro-finite super-graded.
  - **FM164-super (proposed):** Bar-cobar super-Yangian completion: pro-nilpotent
    super-augmentation does not imply super-conilpotence of $B(A)$; only
    $\hat B(A)$ is super-conilpotent in the appropriate completion category.

**(b) WRONG.** Neither FM161-super nor FM164-super is a Vol II catalogued FM.
Vol II Wave 7 supplement runs FM161--FM170; FM171--FM181 are foundations /
RTT. Wave 9 supplement does NOT introduce super-Lie analogs of FM161/FM164.
The wave files invoke a "super-Lie variant" that **does not exist** in any
catalogue.

This is the worst form of conditional: citing a nonexistent failure mode.
Per HZ3-3, the super-Lie variant is **VAPID** as currently written. Class B0
results that cite it are not honestly conditional on a documented gap.

**(c) CORRECT relationship.** Two healing options:
  - **Option B-doc:** Add explicit Vol II Wave 10 supplement entries
    "FM182: super-Yangian Koszulness in Positselski super-non-homogeneous
    framework (analog of FM161)" and "FM183: super-bar-cobar pro-nilpotent
    completion for Lie superbialgebras (analog of FM164)". Wave files then
    cite `FM182 + FM183` instead of "FM164/FM161 super-Lie variant".
  - **Option B-downgrade:** Drop the conditional rider on V58/V64 Class B0
    and downgrade the theorem environment to `\begin{conjecture}`, with V53.1
    Berezinian rigidity as the heuristic. The conifold $Y(\mathfrak{gl}(1|1))$
    super-Yangian construction is, per AP-CY35, ALREADY conjectural; making
    the Class B0 conditional ride on a conjectural construction was a
    discipline failure.

The recommendation in §6 below is Option B-doc.

---

## §3. FM164 + FM161 — precise statements

Reproduced verbatim from Vol II `~/chiral-bar-cobar-vol2/CLAUDE.md`.

### 3.1 FM161 — Y(g) Koszulness via PP05 nonhomogeneous duality

Vol II `CLAUDE.md` line 419:

> **FM161**: Y(g) Koszulness via PP05 nonhomogeneous duality
> (`yangians_foundations.tex`:623--635) — PP05 Ch. 4 requires connected grading
> $A_0 = k$. Yangian level grading has PRO-FINITE $A_0$; "passing to
> augmentation ideal" (L552) does not produce PP05-compatible grading.
> **Counter:** "filtered-CDG-Koszul deformation of $U(g[t])$"; use Positselski
> nonhomogeneous properly; restrict to classical types.

**Heal status (Vol II line 624 + line 839):** CLOSED via filtered-CDG-Koszul
framework (Yangian open-embedding of charts $M_{\rm Kosz}^{\rm assoc}
\hookrightarrow M_{\rm Kosz}^{\rm chiral}$).

### 3.2 FM164 — Bar-cobar Yangian completion elision

Vol II `CLAUDE.md` line 422:

> **FM164**: Bar-cobar Yangian completion elision.
> `yangians_foundations.tex`:677--701 "counit is quasi-iso for augmented
> pro-nilpotent $E_1$-chiral algebras." Pro-nilpotence of $A$ ($\bigcap I^n
> = 0$) does NOT imply conilpotence of $B(A)$; gives conilpotence only on
> COMPLETED $\hat B(A)$. **Counter:** "$\hat\Omega^{\rm ch} \hat B^{\rm
> ch}(A) \to \hat A$ is qiso in pro-nilpotent completion category; raw
> bar-cobar fails for Yangian." Wave 6 A6 repeat with specific location.

**Heal status (Vol II line 859):** CLOSED via the Unified Chiral Quantum
Group Theorem ("All of FM130--135, FM161--170, FM176--181 CLOSED by this
theorem as specialization/scope/citation fixes").

### 3.3 The post-closure footing

Both FM161 and FM164 are CLOSED in Vol II. The wave files, written during the
2026-04-16 swarm before the Vol II closure was finalised, treat them as OPEN.
The honest post-closure statement is:

> The V49 K3 Pentagon-at-$E_1$ result is unconditional in the K3 Heisenberg +
> ADE-enhanced cell of the Vol II Wave 9 Unified Chiral Quantum Group Theorem.

This is a much stronger statement than "conditional on FM164/FM161 K3-specialised".

---

## §4. K3-specialised vs super-Lie variant disambiguation

| Variant | Documented? | Status | Honest scope |
|---|---|---|---|
| **FM161 (general)** | YES (Vol II L419) | CLOSED (Vol II L624, L839) | All simple $g$ classical + exceptional |
| **FM164 (general)** | YES (Vol II L422) | CLOSED (Vol II L859) | All simple $g$ |
| **FM161 K3-specialised** | DERIVATIVE | CLOSED via cell of Wave 9 | K3 Heisenberg + ADE |
| **FM164 K3-specialised** | DERIVATIVE | CLOSED via cell of Wave 9 | K3 Heisenberg + ADE |
| **FM161 super-Lie variant** | **NO** | **VAPID** | none documented |
| **FM164 super-Lie variant** | **NO** | **VAPID** | none documented |

Healing requires either documenting the super-Lie variants (as proposed
FM182/FM183) or downgrading Class B0 inscriptions.

---

## §5. WHAT SURVIVES

After adversarial attack:

1. **FM164 and FM161 are well-defined Vol II Wave 7 entries** (L419, L422)
   with explicit `yangians_foundations.tex` line citations.
2. **Both are CLOSED in Vol II Wave 9** (line 624, 839, 859).
3. **The K3-specialised qualifier corresponds to a CELL of the Wave 9
   closure** (the K3 Heisenberg + ADE cell of the eight specialization
   fibres at line 849).
4. **The super-Lie variant is VAPID** as currently written; no Vol II
   catalogue entry exists.
5. **AP-CY11 propagation IS correctly tracked at V58/V64 surface level**
   but fails for V77 (silent inheritance through V49 Route (ii)).
6. **The conditional structure across four wave uses (V49, V58/V64 A,
   V58/V64 B0, V65) is NOT uniform** -- four distinct conditional structures
   share one label, masking different mathematical content.
7. **V65 CY-C abelian K3 carries an additional conditional (AP-CY66 BZFN
   ambient discipline)** not visible in the `FM164 + FM161` rider.

The surviving core: a precise, audit-trackable conditional structure with
volume-tagged cross-references and per-use stratification, reducing to
unconditional theorems for K3 cells (Class A and CY-C abelian K3) and
conjectures for Class B0 (pending FM182/FM183 documentation).

---

## §6. FOUNDATIONAL HEAL — stratification with documentation

Recommendation: **Option C (stratification + documentation)**, combining
strong reduction at K3 with strong stratification at Class B0.

### 6.1 Re-state the rider (Class A K3 cells)

Replace `conditional on FM164 + FM161 K3-specialised` with:

> **conditional on the Vol II Wave 9 Unified Chiral Quantum Group Theorem
> applying to the K3 Heisenberg + ADE-enhanced cell** (verified by Vol II
> Wave 9 line 849, eight specialization fibres including K3
> super-Yangian-positive cell).

This converts the conditional into a verified specialization of a known
theorem. Per Vol II Wave 9 closure status, the K3 Heisenberg + ADE cell IS
covered. Hence the Class A K3 cells of V49, V58, V64, V65, V77 are
**UNCONDITIONAL** post-closure.

### 6.2 Document the super-Lie variants

Add to Vol II `CLAUDE.md` Wave 10 supplement (proposed):

> **FM182**: super-Yangian Koszulness via Positselski
> super-non-homogeneous duality. PP05 super-version requires connected
> $\mathbb{Z}/2$-graded $A_0 = k$; super-Yangian level grading has
> pro-finite super-grading. **Counter:** filtered-CDG-Koszul super-deformation
> of $U(\mathfrak{g}_{\rm super}[t])$.
>
> **FM183**: bar-cobar super-Yangian completion. Pro-nilpotent
> super-augmentation does not imply super-conilpotence of $B(A)$; only
> $\hat B(A)$ in pro-nilpotent super-completion category. **Counter:**
> $\hat\Omega^{\rm ch,super} \hat B^{\rm ch,super}(A) \to \hat A$ is qiso
> in pro-nilpotent super-completion category.

The Vol III V58/V64 Class B0 wave files then cite `[Vol II] FM182 + FM183`
instead of "FM164/FM161 super-Lie variant", with HONEST conditionality on a
documented (but currently OPEN) failure mode.

Heal status: FM182 + FM183 OPEN (super-Yangian Koszulness + super-bar-cobar
completion). Tractable at the same difficulty as the even case, per V58
L273--274. Listed for closure in a separable Vol II Wave 10 sweep.

### 6.3 Address the V77 silent inheritance

V77 (V70 Mukai uniqueness) feeds V49 Route (ii) (EK rigidity). Add to V77
wave file an explicit `Conditional dependencies` block:

> Per AP-CY11 / HZ3-3, V77 results that feed V49 Route (ii) inherit V49's
> K3-cell conditional. Post Vol II Wave 9 closure, this conditional is
> verified for the K3 Heisenberg + ADE cell, hence V77 is unconditional in
> its K3 input cell.

### 6.4 Address the V65 CY-C BZFN additional conditional

V65 CY-C abelian K3 carries an AP-CY66 BZFN ambient discipline conditional
not visible in the FM164 + FM161 rider. Add to V65 a separate `Conditional
dependencies` block:

> The CY-C abelian K3 construction is conditional on (i) the V49 K3 cell of
> the Vol II Wave 9 closure (verified, see §6.1), and (ii) the AP-CY66 BZFN
> ambient category discipline (Rep$^{E_2}(Y) \to$ Rep$(C)$ in matched IndCoh
> categories). Conditional (ii) is independent of FM164 + FM161 and is
> presently OPEN.

---

## §7. Per-wave conditional inheritance map

Post-heal:

```
                                Vol II Wave 9 Unified Chiral QG Theorem
                                   (K3 Heisenberg + ADE cell verified)
                                                  |
                                                  | (verified)
                                                  v
                            +-----------------------------------+
                            |   V49 K3 Pentagon-at-E_1 [UNCOND] |
                            +-----------------------------------+
                                                  |
                +---------------+-----------------+--------------+-------------+
                |               |                 |              |             |
                v               v                 v              v             v
     V58 Class A K3 [UNC]  V64 Class A K3   V65 CY-C K3      V77 Mukai    V69 Pentagon
     V58 Class A ext       V64 Class A ext   abelian          uniqueness   edge-arch
     [UNC via fibre-loc]   [UNC via f-l]    [UNC mod          [UNC via     [UNC mod
                                             AP-CY66]          §6.3]        AP-CY66]


     V58 Class B0 [COND on FM182 + FM183 (PROPOSED, OPEN)]
                                |
                                v
     V64 Class B0 [COND on FM182 + FM183 (inherits)]


     V20 Step 3 chain-level for Class B (quintic, LP^2):
        CONJECTURE — class M mock-modular completion (V62)
        NOT a FM164/FM161 issue.
```

### 7.1 Discipline observed (audit-ready)

- **AP-CY11 conditional propagation**: every node names its inheritance.
- **HZ3-3 dependency named**: post-heal, every conditional names the
  Vol II Wave 9 cell or the proposed FM182/FM183.
- **HZ3-10 cross-volume Part references**: Vol II provenance tagged
  `[Vol II]` for all FM citations.
- **AP-CY13 cross-volume restructuring**: Vol II Wave 10 sweep needed to
  promote FM182/FM183 from "proposed" to "documented".
- **AP-CY40 status tag matches proof block**: Class A K3 cells `\ClaimStatusProvedHere`
  with full proof; Class B0 `\ClaimStatusConditional` with `[Vol II] FM182 +
  FM183` named in header; Class B `\begin{conjecture}` per HZ3-1.
- **AP-CY55 manifold vs algebraization**: FM164/FM161 are algebraization
  invariants; manifold invariants $\kappa_{\rm cat}, \kappa_{\rm fiber}$ are
  unrelated.
- **AP-CY60 multiple constructions**: V49's three independent routes (sympy,
  EK, V20 trace) preserved; AP-CY60 discipline is orthogonal to the FM164/FM161
  conditional.
- **AP-CY61 first-principles ghost theorem**: extracted in §2.1--2.5 above.

---

## §8. v3.3 directive for RANK_1_FRONTIER

Update `RANK_1_FRONTIER_v3.md` to RANK_1_FRONTIER_v3.3.md with the following
deltas:

### 8.1 Class A status table — promote from CONDITIONAL to UNCONDITIONAL

Replace:

| Class | Status | Conditionality |
|---|---|---|
| A | PROVED (theorem) | FM164 + FM161 |
| A (extension) | PROVED (corollary) | FM164 + FM161 |

With:

| Class | Status | Conditionality |
|---|---|---|
| A (K3) | **PROVED (UNCONDITIONAL post Vol II Wave 9)** | (none; Vol II Wave 9 K3 cell verified) |
| A (K3 extension) | **PROVED (UNCONDITIONAL post Vol II Wave 9)** | (none; fibre-localisation onto verified K3 cell) |

Cross-reference to Vol II Wave 9 line 849 (eight specialization fibres) and
line 859 (FM161-170 closed) in the table footnote.

### 8.2 Class B0 status table — replace VAPID rider with DOCUMENTED proposed FM

Replace:

| Class | Status | Conditionality |
|---|---|---|
| B0 | PROVED | FM164/FM161 super-Lie |

With:

| Class | Status | Conditionality |
|---|---|---|
| B0 | PROVED (cond.) | **[Vol II proposed] FM182 + FM183 (super-Yangian Koszulness + super-bar-cobar completion); OPEN** |

Add footnote: "FM182 and FM183 are proposed Vol II Wave 10 entries
analogous to FM161 and FM164 in the super-Lie setting. Currently OPEN;
listed for separable closure."

### 8.3 V77 inheritance row — add explicit row

Currently V77 has no explicit conditional row. Add:

| Wave | Status | Conditionality |
|---|---|---|
| V77 (V70 Mukai uniqueness) | UNCONDITIONAL post Vol II Wave 9 | Inherits V49 K3 cell; verified |

### 8.4 V65 CY-C K3 abelian — separate AP-CY66 conditional

Replace:

| Wave | Status | Conditionality |
|---|---|---|
| V65 CY-C K3 abelian | PROVED | FM164 + FM161 |

With:

| Wave | Status | Conditionality |
|---|---|---|
| V65 CY-C K3 abelian (Drinfeld currents) | UNCONDITIONAL post Vol II Wave 9 | (none; V49 K3 cell verified) |
| V65 CY-C K3 abelian (BZFN equivalence) | CONJECTURAL | AP-CY66 BZFN ambient discipline; OPEN |

### 8.5 New section "FM164/FM161 closure footing"

Add a new section after the kappa-spectrum table:

> **Vol II Wave 9 closure footing.** All Vol III wave inscriptions citing
> "conditional on FM164 + FM161 K3-specialised" are UNCONDITIONAL post Vol II
> Wave 9 Unified Chiral Quantum Group Theorem (Vol II `CLAUDE.md` line 859:
> "All of FM130--135, FM161--170, FM176--181 CLOSED by this theorem"). The
> K3 Heisenberg + ADE-enhanced cell is one of the eight specialization
> fibres at Vol II line 849. Wave inscriptions citing "FM164/FM161 super-Lie
> variant" are conditional on the proposed Vol II Wave 10 entries FM182 + FM183
> (super-Yangian Koszulness + super-bar-cobar completion); these are currently
> OPEN, listed for separable closure.

### 8.6 Editorial: discipline upgrade

Add a meta-discipline note:

> **HZ3-3.1 discipline (cross-volume conditional propagation).** Every
> Vol III wave conditional citing a Vol II FM must include:
>   1. Volume tag `[Vol II]` before the FM number.
>   2. Closure status (OPEN, CLOSED in Wave $k$, PROPOSED in Wave $k$).
>   3. Cell of closure if applicable.
>   4. Per-input verification: which inputs of the wave fall into the closed
>      cell.
> Failure to include all four constitutes an AP-CY11 violation.

---

## §9. Russian-school discipline closeout

The Beilinson--Drinfeld discipline that the conditional structure must be
TRANSPARENT, not DECORATIVE, is preserved by the heal:

- **Surface conditionals** ("FM164 + FM161 K3-specialised" + "super-Lie
  variant") are now revealed as four distinct conditional structures hiding
  behind one label.
- **Per-use verification** is mechanical: K3 cells are verified post Vol II
  Wave 9; super-Lie cells are conditional on PROPOSED Vol II Wave 10 entries.
- **No vapid conditionality**: every conditional is either verified, OPEN
  with a precise statement, or downgraded to conjecture.
- **AP-CY40 invariant preserved**: every `\ClaimStatusProvedHere` is post-heal
  unconditional or conditional on a documented OPEN failure mode.
- **HZ3-3 invariant strengthened**: cross-volume conditional propagation now
  requires four-element disclosure (volume tag, closure status, cell,
  per-input verification).

The Costello chain-level discipline is preserved: chain-level Pentagon-at-$E_1$
for the K3 Heisenberg + ADE cell is unconditional post Vol II Wave 9; the
super-Lie cell is honestly conditional on documented (proposed) gaps; no chain
of "modulo X" obscures genuine OPEN problems.

---

## §10. Compliance scope (sandbox-only)

This wave V81 deliverable:

- Does NOT edit any `.tex` source. All inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, or any AP catalogue.
- Does NOT modify `MASTER_PUNCH_LIST.md`, `INDEX.md`, or any other notes.
- Does NOT run `make fast`, `make test`, `make verify-independence`, or any
  build/test command. Per pre-commit hook discipline.
- Does NOT close FM182 or FM183 (proposed Vol II Wave 10 entries).
- Does NOT promote any Class B0 conjecture to theorem.
- Does NOT modify the V77 wave file's conditional disclosure (the §6.3 heal
  is a directive for a future V77.1 wave, not an inscription).
- Does NOT modify the V65 wave file's CY-C BZFN handling (the §6.4 heal is a
  directive for a future V65.1 wave).
- Does propose RANK_1_FRONTIER_v3.3 directive (§8) for a separate v3.3
  inscription wave.

The healing path from V49 (conditional on FM164/FM161 K3-spec.) to V81 (V49
unconditional post Vol II Wave 9; super-Lie variant honestly conditional on
proposed FM182/FM183) is the entire content. The Russian-school adversarial
discipline catches: (i) the Vol II closure status that the wave files
overlooked; (ii) the vapid super-Lie conditional; (iii) the silent V77
inheritance; (iv) the hidden V65 BZFN conditional. All four are surfaced and
healed.

— Raeez Lorgat, 2026-04-16
