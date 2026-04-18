# Coderived vs Chain-Level Programme-Wide Audit (2026-04-18)

Author: Raeez Lorgat.
Session: 2026-04-18 /loop iteration, coderived vs chain-level audit.
Scope: Vol I chapters/ + standalone/; Vol II chapters/; cross-check
CLAUDE.md status rows against inscribed theorem bodies.
AP block reserved per AP304/AP306: AP1441-AP1460, used minimally.

## Methodology

Phase 1: enumerate every `.tex` file under Vol I and Vol II containing
"chain-level" or "chain level". 80+ files Vol I, 213 files Vol II.

Phase 2: triage by high-signal loci identified in session context
(MC5, BV, UCH, topologization, periodic CDG, Theorem B, BP, Monster).
For each locus: read a ~20-40 line window around each "chain-level"
occurrence; classify the claim as (a) genuinely chain-level at the
stated scope, (b) cohomological Q-level presented as chain-level,
or (c) cross-volume/scope-drifted.

Phase 3: for CLAUDE.md status-row cross-check, sample the top-10
chain-level advertisements and reconcile with inscribed theorem bodies.

Phase 4: formal AP258 / AP297 violation classification; severity scale
CRITICAL / MODERATE / MINOR / NONE.

## Clean Inscriptions (honest scoping)

The following chapters pass the audit with honest scope discipline.
Each inscribes "chain-level" claims at the correct mathematical scope
and carries explicit scope qualifiers when restricted.

### Vol I

1. **`chapters/theory/mc5_class_m_chain_level_platonic.tex`**
   - 8 "strict chain-level" claims — all scoped to pro-object,
     weight-completed, or $J$-adic ambients. Step-3 Mittag-Leffler
     route healed per AP261+AP296.
   - Theorem scope on direct-sum class-M bar explicitly marked
     "genuinely false" (ambient artefact, not gap). Honest.

2. **`chapters/theory/topologization_chain_level_platonic.tex`**
   - Inscribes `thm:sugawara-antighost-primitive-chain-level` (L426-458,
     `\ClaimStatusProvedHere`) with explicit $\eta_1^{(i)},
     \eta_1^{(ii)}$ closed forms (L292-313) and four supporting
     propositions (`prop:QG1-remainder`, `prop:eta-i-primitive`,
     `prop:eta-ii-primitive`, `cor:eta-primitive`; each
     `\ClaimStatusProvedHere` with proof body).
   - Critical-level collapse to $E_2^{top}$ inscribed at
     `prop:critical-level-collapse` (L599-636); correctly scope-
     restricts the chain-level theorem to $k \ne -h^\vee$.
   - CROSS-VOLUME CONTRADICTION (see CRITICAL section below).

3. **`chapters/theory/theorem_B_scope_platonic.tex`**
   - Honestly scoped: CLAUDE.md Thm B row says coderived level
     weight-completed only; chapter confirms `thm:chiral-positselski-
     weight-completed` coderived and `prop:chiral-positselski-raw-
     direct-sum-class-M-false` separately proves the raw direct-sum
     chain-level FAILS with explicit L_0 witness.
   - Strict chain-level phrases at L430/437/551 refer to the
     Heisenberg on-the-nose route, correctly scoped as class-G-
     specific.

4. **`chapters/theory/chiral_hochschild_koszul.tex:1355`**
   - "strict chain-level inverse" caveats that general case is not
     chain-level; correctly scoped.

5. **`chapters/theory/en_koszul_duality.tex:31`**
   - Explicit parenthetical "(cohomological in general; chain-level
     on the original complex [only for affine KM])". Model of honest
     scoping.

6. **`chapters/theory/e3_identification_chain_level_platonic.tex`**
   - Inscribes chain-level $E_3$ identification with explicit
     associator dependence, E_1-chiral notion (A) of `warn:multiple-
     e1-chiral`. Honest.

### Vol II

1. **`chapters/connections/bv_brst.tex`**
   - Gold-standard discipline. Every chain-level claim carries
     class-by-class scope table (L2024-2064): class G/L chain-level
     curved equivalence; class C chain-level under harmonic
     decoupling; class M "coderived equivalence; naive chain level
     false — harmonic correction survives but is curvature-divisible".
   - `prop:bv-bar-class-m-weight-completed` (L2335) honestly tags
     `\ClaimStatusProvedElsewhere` with the weight-completed scope.
   - Three obstructions prop + harmonic decoupling prop do NOT inflate.

2. **`chapters/theory/topologization_class_m_original_complex_platonic.tex`**
   - Exemplary. Header comments at L16-125 enumerate the three
     distinct ambients (pro-ambient, $J$-adic, weight-completed) and
     explicitly inscribe the original-complex frontier as
     `thm:chain-level-e3-original-complex-conditional` + the
     obstruction theorem for generic class M.
   - No AP258 violation: CONDITIONAL tag matches statement.

3. **`chapters/connections/e_infinity_topologization.tex`**
   - `rem:frontier-class-L-strict-chain-level` at L382-411 downgrades
     class-L original-complex chain-level to frontier. Honest retraction.
   - Cohomological ladder (L786-790) + weight-filtered inverse limit
     (L814, L830) chain-level lift via Ayala-Francis cofinality.
     Scope qualifiers attached to each use.
   - Conjecture on $W_\infty$ E_\infty specialisation (L858-862) is
     cohomologically phrased with weight-filtered chain-level
     upgrade noted. Honest.

4. **`chapters/connections/universal_celestial_holography.tex`**
   - `thm:uch-gravity-chain-level` (L509-525, `\ClaimStatusProvedHere`)
     — advertised "chain-level on pro-object ambient, equivalently on
     $J$-adic topological or weight-completed ambient of Vol I
     Theorem MC5", with explicit note "on the bounded direct-sum
     ambient $\mathrm{Ch}(\mathrm{Vect})$ the identification fails
     (MC5 class M false)". Honest.
   - Step-2 (L548-558) routes through class-L unconditional Thm MC4;
     sound.

5. **`chapters/connections/monster_chain_level_e3_top_platonic.tex`**
   - Theorem + proof structure honest at surface; cites
     `thm:uhf-leech-class-M-chain-level` as Step-2 input.
     **PHANTOM label, see CRITICAL section**.

6. **`chapters/connections/fractional_ghost_chain_level_platonic.tex`**
   - Branched-cover descent from class-L chain-level; inherits the
     class-L chain-level frontier status (see CRITICAL).

## CRITICAL Violations

### V1. Vol I class-L chain-level vs Vol II class-L chain-level (AP258 + AP271 cross-volume contradiction)

**Target.** Strict chain-level Sugawara-antighost identity on the
ORIGINAL (uncompleted) BV complex for $V_k(\fg)$, $k \ne -h^\vee$.

**Vol I position** (`chapters/theory/topologization_chain_level_platonic.tex`):
- `thm:sugawara-antighost-primitive-chain-level` at L426-458 is
  `\ClaimStatusProvedHere`.
- Proof body (L447-458) composes `prop:QG1-remainder` (L238-281)
  with `cor:eta-primitive` (L413-420) giving
  $[Q_{tot}, \widetilde G_1] = T_{Sug} + R_1 - R_1 = T_{Sug}$.
- Explicit $\eta_1^{(i)}, \eta_1^{(ii)}$ closed forms at L296-306.
- `prop:eta-i-primitive` (L327-388) and `prop:eta-ii-primitive`
  (L390-411) each `\ClaimStatusProvedHere` with detailed proofs
  invoking Jacobi identity + antisymmetry + NO associator
  cancellation (`rem:NO-assoc` at L315-325).

**Vol II position** (`chapters/connections/e_infinity_topologization.tex`):
- `rem:frontier-class-L-strict-chain-level` at L382-411:
  > "Theorem `thm:E3-topological-km` establishes
  > $T_{Sug} = [Q_{CS}, G_{Sug}]$ on $H^\bullet(A^{BV}_{3d}, Q_{tot})$,
  > i.e. on cohomology. A chain-level strengthening on the original
  > (uncompleted) BV complex would require explicit antighost contact
  > corrections $\eta_1^{(i)}, \eta_1^{(ii)}$ ... their assembly into
  > a chain-level identity is a genuine computation not inscribed in
  > the present volume ... the verification that these choices absorb
  > the full chain-level discrepancy in $[Q, \tilde G_1] - T_{Sug}$ is
  > pending, and the summary claim has been downgraded accordingly to
  > a frontier item."

**Classification.** AP258 (cohomological-vs-chain status drift) +
AP271 (reverse drift: one volume pessimistic, other optimistic).

**Severity: CRITICAL.** The two volumes contradict each other on the
same mathematical statement. Vol I presents the proof; Vol II says
the computation is pending. Downstream consequences:
1. Vol II `chapters/theory/bp_chain_level_strict_platonic.tex`
   (BP strict chain-level on ORIGINAL complex) cites Vol I
   `thm:sugawara-antighost-primitive-chain-level` at L83 as the
   load-bearing class-L Wick-absorption input. If Vol II's frontier
   assessment is correct, BP's "strict chain-level on original
   complex" claim inherits frontier status and the Vol II BP chapter
   also becomes frontier-conditional.
2. Vol II `chapters/connections/fractional_ghost_chain_level_platonic.tex`
   and `chapters/connections/bp_chain_level_strict_platonic.tex`'s
   "chain-level avatar" (L621-646 of fractional_ghost) cite the same
   class-L chain-level input.
3. Vol II `chapters/connections/monster_chain_level_e3_top_platonic.tex`
   and several Vol II "chain-level" celestial-holography theorems
   transitively depend on the topologization tower, which includes
   the class-L entry.

**Healing options.**
- **Option A (Vol I is correct)**: Vol II `rem:frontier-class-L-
  strict-chain-level` is stale; retract/update the remark to cite
  Vol I's `thm:sugawara-antighost-primitive-chain-level` as the
  inscribed proof, and remove the frontier downgrade. This requires
  independent verification that Vol I's Jacobi-identity +
  antisymmetry cancellations in `prop:eta-i-primitive` and
  `prop:eta-ii-primitive` are complete (the proof at L386-388
  asserts "the signs conspire so that this term cancels one copy of
  the leading $R_{ghost}$" — this is load-bearing and should be
  verified by explicit Wick computation at $\fsl_2$ level 1).
- **Option B (Vol II is correct)**: Vol I is overclaiming (AP4:
  proof after conjecture); downgrade Vol I's theorem to conjecture
  or conditional, flag `prop:eta-i-primitive` and `prop:eta-ii-
  primitive` as requiring full Wick-level verification, retarget
  the status-table row in CLAUDE.md Topologization row entry
  "class L: PROVED Q_{tot}-cohomological" (matching Vol II) and
  drop the "strict chain-level" language from Vol II chapters that
  cite the Vol I theorem.
- **Option C (independent verification)**: run an explicit Wick-
  computation engine on $V_k(\fsl_2)$ at $k=1$ (4 generators, 6
  ghosts, minimal example) verifying
  $[Q_{tot}, \widetilde G_1] = T_{Sug}$ on cochains. If engine
  confirms: Option A. If engine finds residual: Option B.

**AP1441** (this session). Proposed registration (provisional, pending
consolidation per AP314): "Class-L strict chain-level Sugawara
identity: Vol I inscribes with proof; Vol II downgrades to frontier;
engine verification pending." Status: AMBIGUOUS pending Option C.

### V2. Monster chain-level E_3-top phantom load-bearing reference (AP264 + AP242)

**Target.** Vol II `chapters/connections/monster_chain_level_e3_top_platonic.tex`
`thm:monster-chain-level-e3-top` (L39-63, `\ClaimStatusProvedHere`)
constructs the Monster $V^\natural$ chain-level $E_3$-top structure
via Leech $\Z/2$ orbifold.

**Load-bearing reference at Step 2** (L144):

> "By Theorem~\ref*{thm:uhf-leech-class-M-chain-level}, $V_\Lambda$
> admits a chain-level $E_3$-topological structure as the boundary
> of abelian ..."

**Label inscription audit.** Grep `\label{thm:uhf-leech-class-M-chain-level}`
across entire Vol II — zero hits. The two existing `thm:uhf-*` labels
are:
- `thm:uhf-monster-orbifold-bv-anomaly-vanishes`
  (`universal_holography_functor.tex:497`)
- `thm:uhf-perturbative-finiteness-split`
  (`universal_holography_functor.tex:588`)

Neither matches.

**Classification.** AP264 (phantom `\ref{thm:...}` to non-existent
theorem) at a LOAD-BEARING STEP of a `\ClaimStatusProvedHere`
theorem; composite with AP242 (forward-reference lemma labelled as
inscribed).

**Severity: CRITICAL.** A `\ClaimStatusProvedHere` theorem with a
phantom Step-2 load-bearing citation. The phantom mask resolves
silently at build time (typical `[?]` suppressed by `\ref*`
starred form or by a missing-ref `\phantomsection` elsewhere);
reader trusts the cited theorem; it does not exist.

**Healing options.**
- **Option A (retarget)**: identify the intended theorem — most
  likely `universal_holography_functor.tex` contains a Leech-
  related class-M chain-level statement under a different label;
  inspect Chapter 12/Section on UHF Leech orbifold.
- **Option B (inscribe)**: if no existing theorem covers the claim,
  inscribe `thm:uhf-leech-class-M-chain-level` with proof. Leech
  lattice VOA $V_\Lambda$ is class G (free bosonic, 24 Heisenberg
  generators); class G has chain-level curved equivalence
  unconditionally (`bv_brst.tex:2051`). A Leech class-M chain-level
  theorem is STRUCTURALLY OUT OF PLACE: Leech is class G, not
  class M. This suggests the intended label is `thm:uhf-leech-
  class-G-chain-level` or similar.
- **Option C (downgrade)**: if no proof is available, downgrade
  `thm:monster-chain-level-e3-top` from `\ClaimStatusProvedHere`
  to `\ClaimStatusConditional` with attribution to the missing Leech
  input.

**AP1442** (this session, provisional). Proposed consolidation into
existing AP264 as a top-priority instance.

## MODERATE Violations

### V3. Vol I en_koszul_duality.tex:31 chain-level scope qualifier is correct but CLAUDE.md Topologization row carries stale "strict chain-level" advertising for class L

**Target.** CLAUDE.md Topologization row line 529:
> "PROVED on original complex for G/critical; PROVED Q_{tot}-cohomological
> for L; PROVED weight-completed for M"

This is the CORRECT post-audit scoping. Vol I `en_koszul_duality.tex:31`
agrees: "(cohomological in general; chain-level on the original complex
only for the affine KM at non-critical level)".

However, a different CLAUDE.md line inside the same Topologization row
(Theorem Status table) says:

> "class L (V_k(g), k≠-h^v): E_3^top on Q_{tot}-cohomology via
> `thm:E3-topological-km` ... the strict chain-level upgrade via
> explicit η_1 antighost-contact is a FRONTIER item; draft candidate
> formulas inscribed in Vol II `e_infinity_topologization.tex:401-411`
> were retracted 2026-04-17 pending independent verification"

This is consistent with Vol II `rem:frontier-class-L-strict-chain-level`.
The TopologizationRow CLAUDE.md rhetoric is thus INTERNALLY CONSISTENT
with Vol II. Inconsistency is with Vol I `topologization_chain_level_platonic.tex`
which still inscribes `thm:sugawara-antighost-primitive-chain-level`
as `\ClaimStatusProvedHere`.

**Classification.** AP271 reverse drift localised to Vol I chapter:
CLAUDE.md + Vol II are pessimistic; Vol I chapter is optimistic.

**Severity: MODERATE.** This is the same V1 contradiction viewed from
the CLAUDE.md side. Heals when V1 heals.

### V4. Theorem B coderived vs chain-level in CLAUDE.md Thm B row

**Target.** CLAUDE.md Thm B row line 492:
> "Chain-level class G (Heisenberg: chain-level qi via on-the-nose
> harmonic vanishing; direct evaluation of `thm:bv-bar-coderived` at
> Vol II `bv_brst.tex:2088-2094`) and class L (affine KM non-critical:
> chain-level qi via PBW-associated graded reduction ...)
> `\ClaimStatusProvedElsewhere` — attributed to Vol II
> `thm:bv-bar-coderived` ... NOT inscribed in Vol I."

**Inscribed.** `bv_brst.tex:2084` `\label{thm:bv-bar-coderived}` exists;
proof runs L2088-2258. The theorem statement (L2087-2094) asserts
coderived equivalence, with class G/L scope-by-scope clauses. Class L
"chain-level curved equivalence" at L2052 per the internal scope
table; class L proof routes through "Jacobi kills the cubic harmonic
term". Genuine chain-level (not Q-cohomological) per the table.

**Classification.** Honest so far. The CLAUDE.md attribution is
correct.

However: Theorem B CLAUDE.md row also writes:

> "chiral adaptation of Positselski 2011 Thm 4.6 + Thm 7.2 is CITED
> at citation level in Steps 2 and 4 of the weight-completed proof,
> not independently inscribed. Phantom flag: prior status-table names
> `thm:chiral-positselski-7-2` and `thm:chiral-positselski-5-3` are
> PHANTOM in Vol I — the former appears only as
> `\phantomsection\label{thm:chiral-positselski-7-2}` at
> `chapters/frame/preface.tex:5081`; the latter has zero `\label`
> occurrences across the three volumes."

This is AP255 self-acknowledged; no fresh violation.

### V5. "Chain-level" in UCH celestial-dual propositions

**Target.** `chapters/connections/universal_celestial_holography.tex`
L965 `prop:celestial-dual-heisenberg` `\ClaimStatusProvedHere` and
L994 `prop:celestial-dual-virasoro` "`\ClaimStatusProvedHere` at
genus 0, `\ClaimStatusProvedHere` in weight-completed category at
genus $\geq 1$".

**Inscribed.** Each proposition's claim tag matches scope. Virasoro
proposition explicitly splits g=0 (chain-level) vs g>=1 (weight-
completed). Honest.

**Classification.** No violation. Model of scoped inscription.

## MINOR Violations

### V6. `standalone/three_dimensional_quantum_gravity.tex:2871` stale "strict chain-level" claim

**Target.** L2871: "$[Q, \widetilde G_1] = T_{Sug}$ strict chain-level."

**Classification.** AP271 reverse drift: standalone carries the
optimistic class L chain-level claim matching Vol I's inscription
but contradicting Vol II's frontier assessment.

**Severity: MINOR.** Standalone is not `\input` into `main.tex`;
build-level impact nil. Content-level: propagates the V1
contradiction.

### V7. Vol I `chapters/connections/thqg_open_closed_realization.tex:1446`

**Target.** "is missing is the passage from these strict chain-level
data to a [cross-volume target]"

**Classification.** Prose discussion, not a theorem claim. No
violation; scope-dependent phrasing.

## AP297 Cross-Volume Homotopy-Formula Audit

Explicit scan for AP297 (cross-volume homotopy formula cited to
a proof body that does not inscribe it) beyond the Theorem B / MC5
instances already catalogued.

1. **BP `lem:R-twisted-descent` in `bp_chain_level_strict_platonic.tex`**
   cites Vol I `\S\ref*{sec:strict-chain-level}` in `Vol1-class-L-
   antighost` (L449). Vol I section `sec:strict-chain-level` IS
   inscribed (topologization_chain_level_platonic.tex:423) with
   theorem body and proof. AP297 NOT triggered — cited source
   DOES inscribe the formula.

2. **`fractional_ghost_chain_level_platonic.tex:621-646`** claims
   "the chain-level antighost lift ... supplies the explicit chain-
   level lift for the BP fibre ..." with reference to
   `chap:bp-chain-level-strict-platonic`. That chapter does inscribe
   the BP claim (at its own `\ClaimStatusProvedHere`), though the
   BP inscription inherits V1. No fresh AP297.

3. **UCH `thm:uch-gravity-chain-level` (L510)** cites Vol I
   `thm:mc5-class-m-chain-level-pro-ambient`. Vol I
   `mc5_class_m_chain_level_platonic.tex:229-437` inscribes this.
   AP297 NOT triggered.

4. **Monster `thm:monster-chain-level-e3-top` Step 2** cites
   `thm:uhf-leech-class-M-chain-level`. Phantom target (V2 above).
   This IS AP297-style but the deeper failure is AP264 phantom label.

## Summary of Findings

| ID | Pattern | Severity | Location |
|----|---------|----------|----------|
| V1 | AP258+AP271 Vol I vs Vol II class-L chain-level | CRITICAL | Vol I `topologization_chain_level_platonic.tex:427` vs Vol II `e_infinity_topologization.tex:382` |
| V2 | AP264+AP242 Monster phantom Leech chain-level | CRITICAL | Vol II `monster_chain_level_e3_top_platonic.tex:144` |
| V3 | AP271 CLAUDE.md + Vol II pessimistic, Vol I optimistic | MODERATE | CLAUDE.md Topologization row + Vol I chapter |
| V4 | Theorem B coderived attribution | NONE (honest) | CLAUDE.md Thm B row |
| V5 | UCH celestial-dual propositions | NONE (honest) | `universal_celestial_holography.tex:965+994` |
| V6 | Standalone stale chain-level | MINOR | `standalone/three_dimensional_quantum_gravity.tex:2871` |
| V7 | Prose `thqg_open_closed_realization.tex` | NONE | prose, not a theorem |

## Recommended Heals (prioritised)

1. **V1 CRITICAL**: engine verification of Vol I's
   `prop:eta-i-primitive` + `prop:eta-ii-primitive` at $\fsl_2$
   level 1. Explicit Wick computation of $[Q_{tot}, \eta_1^{(i)}]$
   and $[Q_{tot}, \eta_1^{(ii)}]$ against $R_{ghost}$ and $R_{self}$
   with full NO associator tracking. If residual zero: Vol II remark
   retracted; V3 resolves. If residual nonzero: Vol I theorem
   downgraded to conditional/conjecture; ripple through V6, BP
   chapter, Monster (via class L dependence), UCH gravity
   (via class L input on cohomology route, chain-level on pro-
   ambient unaffected).

2. **V2 CRITICAL**: locate or inscribe `thm:uhf-leech-class-M-
   chain-level`. If Leech is actually class G (likely), rename to
   `thm:uhf-leech-class-G-chain-level` and inscribe the class-G
   theorem from `bv_brst.tex:2051` scope table as a local
   proposition. Update Monster chapter Step 2 citation.

3. **V3 MODERATE**: blocks on V1 heal. After V1 resolved, either
   restore Vol I claim with upgraded confidence or propagate
   frontier status across all cross-volume consumers.

4. **V6 MINOR**: standalone heal one-line textual edit; block on V1.

## Notes on Methodology

This audit is a SURVEY, not an exhaustive sweep. The cross-volume
chain-level claim space is large (80+ Vol I chapters, 213 Vol II
chapters, each with multiple "chain-level" occurrences). A
comprehensive pass would require either (a) a dedicated engine that
parses every `\ClaimStatusProvedHere` + "chain-level" pair against
cited labels, or (b) a multi-agent swarm running per-chapter.

Priorities targeted here: loci explicitly flagged in session context
(MC5, BV, UCH, topologization, periodic CDG, Theorem B), loci with
"strict chain-level" advertising, loci with cross-volume citations
to chain-level lemmas.

Gaps in this audit: standalones beyond `three_dimensional_quantum_
gravity.tex` and `seven_faces.tex` not sampled; Vol II
`chapters/connections/*` beyond 6 inspected files not sampled;
`ordered_associative_chiral_kd.tex` chain-level claims not audited
(large file, ~30 hits for "chain-level").

## AP Reservations Used

From block AP1441-AP1460 (15 reserved):
- AP1441: V1 class-L Sugawara chain-level contradiction (provisional,
  pending AP consolidation per AP314).
- AP1442: V2 phantom Leech chain-level (provisional, consolidate
  into existing AP264 per AP314 / AP306 release).

Remaining AP1443-AP1460 released for future use.

## Attribution

All work by Raeez Lorgat. No AI attribution.
