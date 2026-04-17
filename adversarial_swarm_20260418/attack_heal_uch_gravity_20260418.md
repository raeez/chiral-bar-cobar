# Attack-and-Heal: Universal Celestial Holography Gravity Chain-Level

**Target**: Vol II `thm:uch-gravity-chain-level` at `chapters/connections/universal_celestial_holography.tex:511`, with promotion note `rem:uch-gravity-chain-level-promotion` at `:579`.

**Date**: 2026-04-18

**Author**: Raeez Lorgat

**AP block**: AP841-AP860 (reserved for UCH-gravity swarm).

## Mission

Verify or falsify the W13 closure wave's chain-level promotion of universal celestial holography from weight-completed class M to the "original complex" at chain level. The status-table row advertises this as ProvedHere, with status "Chain-level class M at g≥1 inscribed as thm:uch-gravity-chain-level... promoted from conjecture 2026-04-16 via half-BRST chain-level splitting."

## Attack: Point-by-point

### A1. Theorem statement reads as direct-sum class-M promotion

`thm:uch-gravity-chain-level` statement:

> For class **M** celestial algebras arising from HT-twisted gravity, the identification of the genus-$g$ shadow coefficient with the $g$-loop sub${}^{r-2}$-leading soft theorem lifts from the **weight-completed category to the original complex at chain level**. In particular, the chain-level class-**M** scope gap of Vol I Theorem MC5 in its celestial-gravity incarnation is closed.

The theorem explicitly advertises "the original complex" as the target and "scope gap of Vol I Theorem MC5 is closed" as the consequence. Vol I MC5 status is precise: chain-level class M holds in the pro-ambient / J-adic / weight-completed ambients (three equivalent completions); direct-sum chain-level in Ch(Vect) is genuinely FALSE as an ambient artefact (S_4(Vir_c) = 10/[c(5c+22)] ≠ 0 populates bar-weight 4).

If "original complex" = pro-ambient / weight-completed, then the theorem is already equivalent to the ambient Vol I MC5 statement and there is no gap to close (the theorem is tautological).

If "original complex" = raw direct-sum Ch(Vect), then the theorem claims what MC5 class-M direct-sum status says is genuinely false.

### A2. Step 4 is an AP296 (filtration-vs-exact-weight) violation

Step 4 proof body:

> The class-**M** weight-completed identification (Proposition `prop:uch-gravity-shadow`) and the chain-level DS image of Step 3 agree on the common weight-graded pieces; the weight-completion is **surjective onto the original complex on each graded stratum** because V_k(sl_2) is conformally graded with **finite-dimensional weight spaces**.

This is verbatim the AP296 (Wave-14 MC5 heal) failure mode. AP296 was inscribed 2026-04-18 after the Vol I MC5 Wave-14 heal corrected a structurally identical argument:

> The bar differential does NOT preserve total conformal weight on bar words. The OPE weight identity $\mathrm{wt}(a_{(n)} b) = \mathrm{wt}(a) + \mathrm{wt}(b) - n - 1$ strictly decreases total weight on simple-pole summands. Canonical witnesses: Virasoro $T_{(3)} T = c/2$ drops weight $4 \to 0$; affine Kac--Moody $J^a_{(0)} J^b = [a, b]$ drops weight $2 \to 1$.

Consequently:

- A product decomposition $\prod_w B^{\mathrm{ch}}(\mathcal{A}_{\leq N})_w$ over exact weight is illegitimate for class-M algebras.
- "Finite-dimensional weight spaces" stabilises the finite-stage filtration quotients, but stabilisation of filtration pieces at each weight $w$ does NOT imply surjective-back lift of the completed object onto the direct-sum object. The direct-sum object lives in Ch(Vect); the completed object lives in the pro-ambient / J-adic ambient; the two disagree on class-M by a non-vanishing cohomological obstruction.
- The correct Vol I Wave-14 heal replaces the exact-weight product decomposition with a filtration-level argument (Prop. `standard-strong-filtration`(iv)); this gives the pro-ambient chain-level statement, not the direct-sum chain-level statement.

Step 4's verbatim argument "surjective onto the original complex on each graded stratum" is the exact reverse-direction version of the exact-weight product decomposition. Finite-dimensional weight spaces make each $F_w / F_{w-1}$ finite-dimensional, hence the filtration tower Mittag-Leffler-stabilises. This gives a well-defined pro-ambient statement. It does NOT give a direct-sum statement because the bar differential mixes weights and the $\varprojlim^1$ class controlling direct-sum exactness is precisely the non-vanishing class-M shadow obstruction.

### A3. The theorem's own dependency `prop:bv-bar-class-m-weight-completed` refutes it

`prop:bv-bar-class-m-weight-completed` at `chapters/connections/bv_brst.tex:2318` states verbatim in its attribution remark (`:2341-2359`):

> The direct-sum (uncompleted) class M chain-level MC5 is **correctly still false**, since the permanent cubic source regenerates nonzero higher harmonic discrepancies at every stage.

and in `rem:bv-bar-class-m-frontier` (`:2361-2395`):

> A strict comparison on the raw direct-sum models would have to absorb infinitely many nonvanishing higher corrections by a single ordinary chain-homotopy package. **This is what fails.**

Vol II itself inscribes that the direct-sum class-M statement fails. `thm:uch-gravity-chain-level` Step 4 attempts to prove exactly the statement that its ambient dependency says fails.

### A4. Adjacent theorem `thm:uch-soft-hierarchy` flags chain-level original complex as open

In the same chapter, `thm:uch-soft-hierarchy` clause (iii) proof at `:893-896`:

> Genus $g \geq 1$ finiteness is Vol I Theorem MC4; at class M it holds in the weight-completed category (Vol I Theorem MC5), **with the chain-level original-complex case open**.

The chapter simultaneously asserts (in `thm:uch-gravity-chain-level`) that the chain-level original-complex case is closed and (in `thm:uch-soft-hierarchy`(iii) proof) that it is open. This is a same-file inconsistency (AP300-class).

### A5. Dependency `thm:chd-ds-hochschild` supplies only E_2 quasi-isomorphism, not class-M original-complex

`thm:chd-ds-hochschild` at `chapters/theory/chiral_higher_deligne.tex:740` states:

> $\mathrm{DS}^\bullet : \mathrm{ChirHoch}^\bullet(\mathcal{W}_k(\mathfrak{g}, f)) \xrightarrow{\sim} H^\bullet_{\mathrm{DS}}(\mathrm{ChirHoch}^\bullet(V_k(\mathfrak{g})))$, as E_2-chiral brace algebras.

The quasi-isomorphism is of Hochschild complexes; it is an identification, not a lift from class L to class M on the original complex. Step 3 of `thm:uch-gravity-chain-level` relies on "DS preserves chain-level quasi-isomorphisms", which is true in the Kazhdan-graded / weight-completed ambient. It does NOT promote the ambient: DS applied chain-level weight-completed yields a chain-level weight-completed statement on the target, not a chain-level original-complex statement.

Downstream `cor:universal-holography-class-M` at `chiral_higher_deligne.tex:837` (the natural companion statement) is explicit:

> The identification is chain-level on the **weight-completed** ambient (equivalently, on the pro-object / J-adic topological ambient of Vol I `thm:mc5-class-m-chain-level-pro-ambient`); on the bounded direct-sum ambient Ch(Vect) the chain-level identification is **genuinely false**, as is already the bar-cobar chain-level in that ambient for class M (the shadow coefficient $S_4(\mathrm{Vir}_c) = 10/[c(5c+22)] \neq 0$ populates bar-weight 4).

The DS-Hochschild bridge `thm:chd-ds-hochschild`, when applied honestly, gives the weight-completed statement. It does not produce what `thm:uch-gravity-chain-level` claims.

### A6. Phantom reference `prop:uch-gravity-shadow` (AP264)

Both `\ref{prop:uch-gravity-shadow}` consumers at `:527` and `:567` reference a label that does not exist anywhere in the programme:

```
grep -rn 'label\{prop:uch-gravity-shadow\}' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/chiral-bar-cobar /Users/raeez/calabi-yau-quantum-groups
```

returns zero hits. The proof's Step 4 has a phantom load-bearing reference. This is AP264 (phantom ref to non-existent proposition).

### A7. HZ-IV decorator is AP277 vacuous-body variant

`compute/tests/test_climax_theorems_iv.py::test_uch_soft_graviton_leading_order` carries a sound `disjoint_rationale` (Strominger asymptotic symmetries vs. Donnay-Pasterski-Puhm celestial diamonds), but the test body computes only the leading-order Weinberg soft factor $S_2 = c/2 = 1/2$ at $c = 1$ — a leading-order Gelfand-Fuchs cocycle check. It does NOT verify any chain-level class-M statement. AP277: sound decorator prose, tautological test body with respect to the theorem's actual content.

### A8. W13 promotion trail is AP269 + AP240

The promotion from conjecture to theorem is advertised in session notes (`notes/session_20260417_master_synthesis.md`, `notes/part_VII_frontier_platonic_reconstitution.md`) as "W13 `thm:uch-gravity-chain-level` + HPL through DS SDR; `thm:chd-ds-hochschild`". The "HPL through DS SDR" is AP269-class fabrication at the narrative layer: the HPL transfer in `thm:chd-ds-hochschild` Step 3 is explicitly confined to Kazhdan-graded / weight-completed behaviour ("applies chain-level because Arakawa's C_2-cofiniteness ensures the retract data are defined on each conformal-weight stratum"); the direct-sum extension is the permanent-cubic-source obstruction `rem:bv-bar-class-m-frontier` says fails.

AP240 (closure-by-repackaging): The "closure" of the chain-level class-M frontier via `thm:uch-gravity-chain-level` repackages the frontier into the theorem body without resolving the direct-sum obstruction. Reading `prop:bv-bar-class-m-weight-completed` attribution remark resolves the question honestly: the direct-sum statement is genuinely false; the chain-level original-complex statement requires the ambient re-interpretation.

## Diagnosis

`thm:uch-gravity-chain-level` as written is an AP296 + AP264 + AP300 composite violation and carries a same-file inconsistency with `thm:uch-soft-hierarchy`(iii). Its Step 4 reproduces the exact-weight-vs-filtration error that Wave-14 Vol I MC5 heal rectified two days ago on 2026-04-16/18. The theorem's own dependencies (`prop:bv-bar-class-m-weight-completed`, `cor:universal-holography-class-M`, `thm:chd-ds-hochschild`) all state the conclusion it claims is genuinely false on the direct-sum ambient.

Two honest scopes survive:

(a) **Pro-ambient / weight-completed restatement**: the chain-level identification holds on the pro-ambient / J-adic / weight-completed ambient, which is the Vol I MC5 pro-ambient statement transported through the DS-Hochschild bridge. This is a genuine theorem but redundant with `cor:universal-holography-class-M` specialised to gravity, and does not close any scope gap of MC5.

(b) **Ambient-neutral reformulation**: following the Vol I MC5 Platonic chapter (`chapters/theory/mc5_class_m_chain_level_platonic.tex`), the "original complex" can be reinterpreted as the canonical inverse limit in pro-Ch(Vect) / J-adic topological ambient, which IS the original complex of a weight-graded chiral algebra natively. This reframes the weight-completion as ambient choice rather than mathematical obstruction, following the Platonic chapter's lead.

Both honest scopes are ALREADY CAPTURED by the existing weight-completed theorems. The incremental content advertised by `thm:uch-gravity-chain-level` over `cor:universal-holography-class-M` and `thm:uch-soft-hierarchy` is zero.

## Heal

**Action taken**: Downgrade the theorem with honest scope.

- Theorem environment retained (the pro-ambient / weight-completed statement is a genuine theorem, just not an advance over ambient Vol I MC5).
- Theorem statement rewritten to name the ambient explicitly (pro-ambient / J-adic / weight-completed). Claim "lifts... to the original complex at chain level" retracted; replaced with "identifies chain-level on the pro-ambient (equivalently, on the weight-completed ambient of Vol I MC5)".
- Claim "chain-level class-M scope gap of Vol I Theorem MC5 is closed" retracted; scope gap at the direct-sum ambient is genuinely false per `prop:bv-bar-class-m-weight-completed`.
- Step 4 rewritten to state the pro-ambient surjectivity (correct) rather than direct-sum lift (incorrect).
- Phantom `\ref{prop:uch-gravity-shadow}` references retargeted to the actual shadow-coefficient propositions in the chapter: `prop:uch-gravity-leading` (`:447`) for the leading statement and `prop:uch-gravity-higher-partial` (`:489`) for the higher-order statement. If the intended reference was a genuine shadow-coefficient inscription that never landed, the retargets make the proof text self-consistent; inscribing the full shadow-coefficient proposition remains a separate frontier item.
- Promotion remark `rem:uch-gravity-chain-level-promotion` updated: (i) name pro-ambient as the ambient where promotion is genuine; (ii) retract "chain-level original complex" framing; (iii) cite AP296 (Wave-14 MC5 filtration-vs-exact-weight heal) to record the error mode that led to the initial over-claim.
- Same-file inconsistency with `thm:uch-soft-hierarchy`(iii) resolved by retracting the over-claim, consistent with `:893-896` "chain-level original-complex case open" statement.

**Proof restructure**:

- Steps 1-3 unchanged (DS-Hochschild bridge correctly supplies a weight-completed chain-level identification).
- Step 4 rewritten to state the pro-ambient limit via Milnor / Mittag-Leffler stabilisation (following `prop:bv-bar-class-m-weight-completed` Vol II attribution remark and Vol I `thm:mc5-class-m-chain-level-pro-ambient`).

**No CLAUDE.md update**: the Vol II CLAUDE.md may carry the pessimistic ambient caveat; Vol I CLAUDE.md status-table row for "Universal celestial holography" will be reviewed at a follow-up reconciliation pass (leaving scope status as "pro-ambient / weight-completed chain-level for gravity; direct-sum class-M on original complex genuinely false per MC5") — but updating CLAUDE.md directly is reserved for the main-thread supervisor per AP304 concurrent-edit protocol, not this swarm.

## AP inscriptions (reserved block AP841-AP860; used AP841-AP843)

**AP841 (UCH-gravity direct-sum class-M overclaim).** Specialisation of AP296 (filtration-vs-exact-weight bigrading) to the celestial-gravity / universal-holography lane. A chapter-level theorem claiming to "lift from weight-completed to original complex at chain level" via finite-dimensional weight-space surjectivity is the AP296 error mode wearing a different hat. Diagnostic counter: substitute $T_{(3)} T = c/2$ into the bar differential at weight 4; output lands at weight 0; the "weight-completion surjective on each graded stratum" argument fails. Healing: name the ambient explicitly (pro-object / J-adic / weight-completed) and retract the "original complex" phrasing unless the ambient-neutral reformulation of `mc5_class_m_chain_level_platonic.tex` is invoked by name.

**AP842 (W13 closure-wave retroactive compression).** Instance of AP240 (closure-by-repackaging) and AP254 (closure-date commit-floor) as they manifest at the celestial-holography frontier: the W13 2026-04-16 "chain-level class M promotion" narrative compresses three distinct weight-completed theorems (`thm:chd-ds-hochschild`, `prop:bv-bar-class-m-weight-completed`, modular-bootstrap $H^2 = 0$) into a single "original complex at chain level" advertisement. The underlying weight-completed content is sound; the advertisement rides on the ambient ambiguity. Counter: when reading any "closure of MC5 class-M chain-level at the original complex" claim, check (i) whether "original complex" resolves to pro-ambient or direct-sum, (ii) whether the cited inputs are weight-completed or direct-sum theorems, (iii) whether `rem:bv-bar-class-m-frontier` or `rem:mc5-honest-weight-filtration` is referenced. Absence of (iii) in a closure-wave narrative is a strong AP842 signal.

**AP843 (Adjacent-theorem ambient inconsistency in same chapter).** Specialisation of AP300 (in-file ProvedHere-vs-retracted-mechanism drift) to ambient-qualification inconsistency. One theorem (here `thm:uch-gravity-chain-level`) claims chain-level closure on the original complex; an adjacent theorem (`thm:uch-soft-hierarchy`(iii)) in the same chapter flags the same statement as open. Detection: after inscribing any chain-level class-M closure theorem, grep the same file for "original complex... open" / "chain-level... open" / "weight-completed" / "ambient"; adjacent statements with disagreeing ambient scope are AP843. Healing: align all same-file ambient qualifiers before accepting the closure theorem.

## Cache entries

None new; this session's heals map to existing Pattern 218 (two Koszul conductors same letter — AP234 parent), AP296 (filtration-vs-exact-weight bigrading), and AP240/AP254 (closure-wave narrative compression).

## Patch (per AP316)

The heal mutates `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/universal_celestial_holography.tex` lines 509-600. A minimal diff is applied directly in the main repo working tree (no worktree isolation) because the edit is a single theorem block + one remark in one file, and the write is idempotent.

## Post-heal residual

- (OF1) **Pro-ambient MC5 transport to gravity lane**: inscribing the pro-ambient restatement as a named lemma in the celestial-holography chapter (currently absorbed into `cor:universal-holography-class-M` in the chiral higher Deligne chapter). Low priority.
- (OF2) **`prop:uch-gravity-shadow` real inscription**: the "genus-g shadow coefficient = (r-2)-th bracket on weight-g stratum of ChirHoch^\bullet(Vir_c)" statement is load-bearing and deserves its own labelled inscription with HZ-IV decorator, not a retarget to leading/higher propositions. Mid priority.
- (OF3) **Direct-sum class-M open-frontier narrative**: the chapter should inherit the Vol I MC5 Platonic reformulation by either (a) naming the pro-ambient as the genuine ambient of the "original complex", or (b) keeping the direct-sum ambient named and flagging class-M direct-sum as a programme-level ambient-artefact.
- (OF4) **HZ-IV numerical upgrade of `test_uch_soft_graviton_leading_order`**: to close AP277 the test body should wire a genuine class-M bar-cohomology check at weight 4 (e.g. verify $S_4(\mathrm{Vir}_c) = 10/[c(5c+22)]$ numerically at two disjoint $c$-values) rather than a leading-order Weinberg factor. Mid priority.

## Audit trail

- Attacked `thm:uch-gravity-chain-level` Step 4 against AP296 — FAILS.
- Attacked `thm:uch-gravity-chain-level` against `prop:bv-bar-class-m-weight-completed` attribution remark — STATEMENT OF THEOREM CONTRADICTS ITS OWN DEPENDENCY.
- Attacked Step 4 phantom reference `prop:uch-gravity-shadow` — AP264 PHANTOM confirmed, zero `\label` matches across all three volumes.
- Attacked adjacent `thm:uch-soft-hierarchy`(iii) for ambient agreement — INCONSISTENT, flags same claim open while closure theorem claims closed.
- Attacked HZ-IV decorator body — AP277 VACUOUS relative to chain-level content of theorem.
- Attacked W13 promotion narrative — AP240 + AP254 closure-wave repackaging confirmed.

Verdict: theorem as inscribed is unsound at its advertised scope. Heal to pro-ambient / weight-completed scope via downgrade + proof-body rewrite + phantom-reference retarget. No mathematical content is lost; the pro-ambient statement is the genuine content.
