# CLAUDE.md — Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves

## What This Is

Two-volume research monograph by Raeez Lorgat. Vol I (~2,174pp, 80+ active files, ~2,920 claims) is the algebraic engine: bar-cobar duality for chiral algebras on curves, with the five main theorems proved, a nonlinear shadow calculus with full Θ_A proved (bar-intrinsic, thm:mc2-bar-intrinsic) and finite-order engine through arity 4, and a comprehensive physics landscape (20+ worked examples from Gaiotto et al.). Vol II (~500pp, at ~/chiral-bar-cobar-vol2, 41+ files, ~500+ claims with 100% tag coverage) applies the engine to 3d holomorphic-topological QFT, PVA quantization, and holography.

**Vol I structure**: Overture (Heisenberg atom) + Part I (The Algebraic Engine: Thms A-D+H, HTT, nonlinear shadow tower, branch-line reductions) + Part II (The Standard Landscape: all example families + combinatorial frontier) + Part III (Bridges: Feynman, BV/BRST, YM boundary theory, E_n, Langlands) + Part IV (The Frontier, concordance) + Appendices (4 clusters: A-Foundations, B-Nonlinear Calculus, C-Extended Families, D-Physics+Reference).

**Vol I title**: *Modular Koszul Duality*
**Vol II title**: *A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT*

## The Dual Imperative

Maximalist ambition synergizes with maximal truth-seeking. Precision enables ambition. When claims outrun proofs, strengthen the proof first.

## The Beilinson Principle

**"What limits forward progress is not the lack of genius but the inability to dismiss false ideas."**

This is a permanent operating directive. Every agent session in this repository acts as a frontier research mathematician whose primary cognitive move is **falsification, not confirmation**. A claim is false until you have independently verified it from primary source. This applies to:

- Claims in the manuscript (theorems, propositions, remarks, formulas)
- Claims in this file (CLAUDE.md), in concordance.tex, and in memory files
- Your own reasoning, corrections, and proposed edits
- Status tags (`\ClaimStatusProvedHere` is a LaTeX macro, not a proof)

Prefer a smaller true theorem to a larger false one. Downgrading, narrowing, or fencing a claim is progress. Treat compute as an adversarial verification layer. Never change a formula just because a narrative wants it. Use the red-team materials, theorem registry, and concordance as active audit instruments, not decorative metadata.

### Epistemic Hierarchy

Trust these sources in this order. When they conflict, the higher-ranked source wins:

1. **Direct computation** — symbolic verification via compute/ modules, dimensional analysis, limiting cases
2. **The .tex source itself** — the actual theorem statement and proof text, read in full with ±100 lines of context
3. **The build system** — compiler errors, undefined references, test failures
4. **Published literature** — original papers with verified arXiv/DOI identifiers
5. **concordance.tex** — the constitution, but verify its claims against 1–4
6. **This file (CLAUDE.md)** — operational instructions; mathematical claims may lag behind source
7. **Memory files** — historical context; may be stale; always verify before acting on

**CLAUDE.md and memory files describe what we *believe* is true. The .tex source is what we *have written*. The compute/ modules test what we *can verify*. These three can disagree. When they do, investigate — do not assume any layer is authoritative.**

### The Verification Reflex

Before every assertion, edit, or claim about the codebase:

> **"How do I know this? Did I read the source, compute it, or assume it?"**

If "assume" — stop and verify. If "read it in CLAUDE.md or memory" — go read the actual .tex. If "compute" — can you reproduce the computation independently?

### Cognitive Anti-Patterns — Observed From This Repository's Own Error History

These are not hypothetical. Each has occurred multiple times, documented across 94 correction commits in 300 recent commits. Actively resist every one.

**AP1 — Copy-paste without recomputation.** κ(KM) = dim(g)·(k+h∨)/(2h∨). κ(Vir) = c/2. κ(W_N) = c·(H_N - 1). These are three *distinct* formulas. This repository has 7+ commits correcting κ formulas copied between families without recomputation (c28bd2e, c0f0e4c, eb1b70d, 43e5ac2, 6526706, 05d6eb2, 5629ee7). One such error propagated to 47 files. **Rule: before writing any formula, check `landscape_census.tex`. Never copy a formula between algebra families without recomputing from first principles.**

**AP2 — Anchoring on descriptions over source.** CLAUDE.md says "MC4 PROVED." The .tex file may say something different, or the proof may have a gap. D²=0 was simultaneously tagged ProvedHere and Conjectured in different files of the same manuscript. **Rule: read the actual theorem and proof in .tex. Descriptions are claims *about* source, not source itself.**

**AP3 — Pattern completion over verification.** You see a formula in three places and a variant in a fourth. You "correct" the fourth to match the three. But the fourth was correct (applying to a different family) and the three were wrong. **Rule: compute independently. Never correct by majority vote across occurrences.**

**AP4 — Status tag as ground truth.** `\ClaimStatusProvedHere` means someone typed those characters. Prior audits found 4–20 status boundary violations per cycle — claims tagged as proved whose proofs cite conjectural inputs, prove something weaker than stated, or contain gaps. **Rule: verify that the proof actually proves the stated claim. Check that all cited results have their hypotheses satisfied.**

**AP5 — Local fix, global neglect.** You correct a formula in one file. The same formula appears in 10+ other files across both volumes. You've created an inconsistency. This is the #1 systematic failure mode (3–4 commits required per full correction). **Rule: after EVERY correction, grep for all variant forms across `~/chiral-bar-cobar` AND `~/chiral-bar-cobar-vol2`. Fix all instances in the same session.**

**AP6 — Omitting boundary qualifications.** "D²=0 is proved" — at which level? Convolution? Ambient? "κ is computed" — genus-0 curvature m₀ or genus-1 obstruction κ? "Θ_A is proved" — truncated Θ_A^{≤r} or full? Four audit findings trace directly to this conflation. **Rule: every use of shadow tower, bar curvature, D²=0, or obstruction coefficient MUST specify genus, arity, and level (convolution vs ambient).**

**AP7 — Scope inflation.** Universal claim, special-case proof. "Koszulness holds for all..." when proved only for type A. Prior audits found 3+ instances (MC3 was the canonical example before its all-types resolution). **Rule: before writing a universal quantifier, verify the proof has no implicit type/genus/level restriction.**

**AP8 — Virasoro self-duality ambiguity.** One root error ("Virasoro is self-dual") propagated to 6 corrections because it conflates uncurved quadratic self-dual (c=0) and FF-involution self-dual (c=13). **Rule: NEVER write "self-dual" for Virasoro unqualified. Always specify which duality and which central charge.**

**AP9 — Same name, different object.** κ means different things for different families. m₀ (genus-0 curvature) ≠ κ (genus-1 obstruction). The dg Lie algebra ≠ the L∞ algebra. Conv_str ≠ Conv_∞. Confusing these passes tests if the tests encode the same confusion. **Rule: use explicit qualifiers (κ^{KM}, κ^{Vir}, κ^{W_N}) or fully qualify in prose. Use \Convstr and \Convinf macros.**

**AP10 — Tests with hardcoded wrong expected values.** If a formula is wrong in both code AND test, the test passes. This happened with κ formulas across 47 files. **Rule: cross-family consistency checks (additivity, complementarity, anti-symmetry) are the real verification. Single-family hardcoded tests are necessary but NOT sufficient.**

**AP11 — Single-point external dependency without flag.** `thm:ambient-d-squared-zero` depends entirely on [Mok25, Thm 3.3.1], a 2025 preprint. **Rule: any theorem resting on a single external source gets flagged in concordance.tex with source, publication status, and fallback status.**

**AP12 — Proof status inflation by accretion.** As the manuscript grew through raeeznotes75–97 (6+ months), new proofs upgraded old conjectures but didn't consistently update all legacy ProvedElsewhere/Conjectured tags. Each audit cycle finds 8–12 stale tags. **Rule: when proving a claim, search the entire manuscript for all variants. Update all instances in the same commit. Use `git log` to find all commits that touched the claim.**

**AP13 — Forward references hiding gaps.** A claim in the introduction is tagged ProvedHere, but the proof at genus g ≥ 1 assumes the very thing it claims to prove. The Beilinson audit flagged Theorem B's spectral sequence collapse as circular at higher genus. **Rule: forward references must be transparent about genus/level/type restrictions. If proved at genus 0 and conjectured at g ≥ 1, say so at every cross-reference site.**

**AP14 — Conflating chiral Koszulness with Swiss-cheese formality.** Chirally Koszul (def:chiral-koszul-geometric) = bar cohomology H*(B(A)) concentrated in bar degree 1. Swiss-cheese formal = the SC^{ch,top} operations m_k^{SC} on A vanish for k ≥ 3. These are DIFFERENT PROPERTIES of DIFFERENT OBJECTS. The dodecahedron m_k (condition (iii)) are transferred operations on H*(B(A)); the Swiss-cheese m_k^{SC} are operadic compositions on A itself. ALL standard families (G/L/C/M) are chirally Koszul (cor:universal-koszul: freely strongly generated ⟹ PBW collapse ⟹ bar concentrated). Only classes G/L/C are Swiss-cheese formal. Class M (Virasoro, W_N) is Koszul but NOT Swiss-cheese formal: m_k^{SC} ≠ 0 for all k ≥ 3. Shadow depth classifies complexity WITHIN the Koszul world, not Koszulness status. NEVER write "Virasoro is not Koszul" or "DS reduction breaks Koszulness." The correct statements are "Virasoro has non-formal Swiss-cheese structure" and "DS reduction introduces Swiss-cheese non-formality." Theorem thm:ds-koszul-obstruction proves that DS introduces higher SC operations, NOT that it destroys bar concentration. This error propagated through 20+ files in Vol II across multiple agent sessions before being identified. **Rule: when writing about Koszulness, always specify: (a) which object's operations you mean (bar-transferred or Swiss-cheese), and (b) which property you mean (bar concentration or SC formality).**

**AP15 — Holomorphic/quasi-modular conflation.** E_2*(τ) is quasi-modular (transforms with additive anomaly 3τ/(πi)), NOT a holomorphic modular form for SL(2,Z). The shadow multiplicativity theorem falsely claimed graph amplitudes are "polynomials in E_4, E_6" — but the genus-1 propagator IS E_2*, and products of E_2* are quasi-modular polynomials in {E_2*, E_4, E_6}, NOT in {E_4, E_6}. The "dim S_k = 0 for k < 12" argument applies ONLY to holomorphic M_k(SL(2,Z)); the space of quasi-modular forms is larger. Three false claims in one session were built on this conflation. **Rule: when working with genus-1 amplitudes, ALWAYS specify holomorphic vs quasi-modular vs almost-holomorphic. NEVER apply holomorphic dimension formulas to quasi-modular objects. The genus-1 propagator is E_2*; any graph sum involving it produces quasi-modular forms.**

**AP16 — Integrated identity ≠ class identity (level confusion).** The multi-generator theorem proved F_g = κ · λ_g^FP (an integrated number) but claimed λ_g^{(h_i)} = λ_g (class equality in cohomology). The Hodge bundle ℰ_h = R^0π_*ω^{⊗h} has rank (2h-1)(g-1); for different h, c_g(ℰ_h) lives in H^{2(2h-1)(g-1)}(M̄_g) — DIFFERENT cohomological degrees. Classes in different degrees CANNOT be equal. **Rule: NEVER promote an equality of numbers to an equality of cohomology classes without verifying both sides live in the same degree. State integrated results as integrated identities.**

**AP17 — Narrative velocity overriding verification (cascade error).** In one session, three false theorems were written into the manuscript: shadow multiplicativity (AP15), multi-generator universality (AP16), MK3 scope inflation (AP18). Each built on the previous one's unchecked success. **Rule: after writing ANY new theorem, IMMEDIATELY deploy an adversarial audit on it BEFORE building the next result. NEVER chain new claims without auditing each link. \ClaimStatusProvedHere should be the LAST thing added, after audit, not the first.**

**AP18 — "Entire standard landscape" without exception analysis.** PBW propagation was claimed for "every standard family" but: βγ has weight-0 generator γ (violating positive grading); admissible-level quotients have null vectors (breaking L_0 invertibility); minimal models are quotients where universal PBW fails. Also: "reduces to a single axiom MK1" hid that MK2 (Verdier) is also needed. **Rule: before ANY universal quantifier over families, explicitly list every family and check each against the hypotheses. State exceptions in the theorem statement.**

**AP19 — Label prefix mismatch.** A `\begin{remark}` labeled `\label{thm:...}`, or a `\begin{conjecture}` labeled `\label{thm:...}`. Found in bv_brst.tex (2 instances), propagated to 2 cross-reference sites. **Rule: label prefix MUST match environment type. thm: → theorem/proposition/lemma. def: → definition. rem: → remark. conj: → conjecture. cor: → corollary. After ANY label change, grep the entire manuscript for all \ref{old-label} sites (AP5).**

**AP20 — Theorem environment with non-proved status.** `\begin{theorem}[...; \ClaimStatusConjectured]` is a logical contradiction: a "theorem" is by definition proved. Found 3 instances in twisted_holography_quantum_gravity.tex (G12', G13, G16). The LLM generates `\begin{theorem}` by pattern-matching surrounding text, without checking that the environment type matches the claim status. **Rule: \begin{theorem} requires \ClaimStatusProvedHere or \ClaimStatusProvedElsewhere. If the claim is Conjectured, use \begin{conjecture}. If Heuristic, use \begin{conjecture} or \begin{remark}. NEVER write \begin{theorem} with a non-proved status tag.**

**AP21 — Status tag on wrong environment type.** `\ClaimStatusProvedHere` on a `\begin{definition}` (definitions have no proof status) or on an incomplete proof (a heuristic discussion labeled as a proof). Found in frontier_modular_holography_platonic.tex (definition) and configuration_spaces.tex (heuristic discussion). **Rule: definitions NEVER carry claim status tags. Proofs must actually prove the stated claim (AP4). If a "proof" is really a discussion, rename it `\begin{proof}[Discussion]` and downgrade the claim status. \ClaimStatusProvedHere should be the LAST thing added to a theorem, after the proof is verified complete.**

**AP22 — OPE confused with collision residue (pole order error).** The OPE T(z)T(w) ~ (c/2)/(z-w)⁴ + 2T/(z-w)² + ∂T/(z-w) has pole orders 4, 2, 1. The collision residue r(z) = Res^{coll}_{0,2}(Θ_A) extracts one fewer power: r(z) = (c/2)/z³ + 2T/z (pole orders 3, 1). The extraction involves d log(z-w), which absorbs one power. Similarly for KM: the OPE has poles z⁻² and z⁻¹, but the r-matrix is Ω/z (pole order 1 only). Found in working_notes.tex (2 instances), e1_modular_koszul.tex, and the gravity chapter. **Rule: when writing an r-matrix formula, the pole orders are ONE LESS than the OPE pole orders. r(z) = Res^{coll}(Θ_A) extracts the coefficient of d log(z-w), not dz/(z-w). NEVER copy an OPE formula as an r-matrix formula.**

**AP23 — κ vs κ_eff vs m₀ conflation.** Three distinct objects: κ(A) = modular characteristic (intrinsic scalar of one algebra), κ_eff = ghost-subtracted curvature of a composite system (κ_matter + κ_ghost), m₀ = κ·ω_g (the curved A∞ curvature, a class not a scalar). The genus tower uses κ: F_g = κ·λ_g^FP. The anomaly cancellation uses κ_eff: κ_eff = 0 at c=26. The transgression algebra uses κ(B) where B is the Koszul dual: u = η² = κ(B)·ω_g (LINEAR in κ, not κ²). Found systematically in working_notes.tex (6 instances) and the gravity chapter. **Rule: (1) F_g formula always uses κ(A), never κ_eff. (2) u = η² is κ·ω_g (first power, a class), not κ² (a scalar). (3) When writing κ_eff, always state "(after ghost subtraction)" or "(matter + ghost)". (4) NEVER square κ in the transgression algebra — the Clifford relation is η² = λ (linear), not η² = λ² (quadratic).**

### Rectification Dynamics (Active)

This repository is in a sustained correction-and-rectification phase. Assume both volumes still contain many undiscovered errors. At even a 2% error rate across ~2,920 tagged claims: ~58 errors. At 5%: ~146. The job is falsification.

**Upstream-first ordering.** Verify claims in dependency-DAG order. The DAG has 1,297 theorem nodes and 1,669 edges. 522 root nodes have zero upstream dependencies — these are safe to verify in any order and should be verified first. Then Layer 1 (direct dependents of roots), then Layer 2, etc. Critical bottleneck: `thm:mc2:bar:intrinsic` (37 downstream citations). Most complex cone: Thm C (25 upstream deps).

**Verification windows (upstream-first):**
1. **Roots** (522 nodes): definitions, basic lemmas, frame examples — no upstream deps
2. **Thm A** (adjunction) — root theorem, no upstream deps, verify first among main theorems
3. **Thm B** (inversion, 11 upstream) — depends on genus-graded convergence, Barr-Beck-Lurie, log convergence
4. **Thm C** (complementarity, 25 upstream) — depends on anomaly duality, concrete modular datum
5. **Thm D** (modular characteristic, 13 upstream) — depends on generating function, closed forms
6. **MC2 bar-intrinsic** (37 downstream) — the single biggest bottleneck; verify after Thms A–D
7. **MC4 completion** (15 upstream) — depends on resonance-filtered bar-cobar
8. **MC5 sewing** (14 downstream) — depends on general HS-sewing
9. **All remaining claims** in topological order through the DAG

**The correction loop.** For each suspected error:
1. **Locate**: exact file, line, ±100 lines of context
2. **Classify**: A (logical/circular), B (formula), C (structural/label), D (status), E (editorial)
3. **Verify the diagnosis**: confirm this is wrong, not a convention difference or your misunderstanding
4. **Compute the correction** independently — not by pattern, not by majority vote
5. **Grep all variants** across both volumes: `~/chiral-bar-cobar` and `~/chiral-bar-cobar-vol2`
6. **Apply** with minimal blast radius
7. **Build + test**: `make fast` and `make test` must pass
8. **Propagate** to all instances found in step 5
9. **Document**: what was found, what class, what was corrected

**The double-edged Beilinson.** The principle applies to your corrections too:
> **"Am I certain this correction is right, or am I merely confident?"**
Certainty requires independent verification. If you cannot independently verify a correction, mark it `% RECTIFICATION-FLAG: [reason]` rather than silently applying. A wrong correction is worse than no correction.

## Deep Beilinson Audit — Procedure

When instructed to "perform a deep Beilinson audit," execute the following protocol on every page of the manuscript, proceeding linearly from page 1. Deployable on Vol I, Vol II, or both at will.

### Core Principle

**"What holds back forward progress is not the lack of genius but the inability to dismiss false ideas."** Every claim is false until independently verified. The audit's purpose is FALSIFICATION, not confirmation.

### Per-Page Protocol

For each page of the PDF:

1. **Read the page** via PDF extraction. Simultaneously read the corresponding .tex source to catch PDF-vs-source discrepancies.
2. **Enumerate every mathematical claim** on the page: formulas, theorem statements, proof steps, definitions, examples, table entries, sign conventions, scope qualifications.
3. **For each claim, independently verify:**
   - **Formulas**: Recompute from first principles. Do NOT pattern-match against other occurrences — compute independently (AP1, AP3).
   - **Proof steps**: Check logical validity. Does the hypothesis of each cited result match how it's used? Are there unstated assumptions? (AP4, AP7)
   - **Conventions**: Verify sign/shift conventions (s vs s⁻¹, cohomological vs homological, ℏ normalization) against the signs appendix (appendices/signs_and_shifts.tex) which is AUTHORITATIVE.
   - **Scope**: Check universal claims against known counterexamples. "For all" means ALL — verify edge cases (critical level, admissible, self-dual points). (AP7)
   - **Cross-references**: Verify cited theorem numbers resolve. Read the cited result to confirm hypotheses match.
   - **Status tags**: For any claim tagged ProvedHere, verify the proof actually proves the stated claim, not something weaker.
4. **Cross-check against the compute layer**: For any numerical formula (κ values, F_g, Q^contact, discriminants, growth rates), verify against compute/tests/ and compute/lib/. Run targeted tests if needed.
5. **Cross-check against the literature**: For standard results (Arnold relations, Faber-Pandharipande, Koszul duality Com^!=Lie, Feigin-Frenkel involution), verify the manuscript's statement matches the published version.
6. **Propagation check (AP5)**: After finding ANY error, immediately grep the entire codebase (both volumes, all .tex files, CLAUDE.md, memory files) for ALL other occurrences of the same formula/claim. Fix all instances in the same pass.
7. **Record findings**: Update `compute/audit/linear_read_notes.md` with:
   - Finding number, page, severity (CRITICAL/SERIOUS/MODERATE/MINOR)
   - Exact claim, exact issue, exact fix
   - Status (FIXED/OPEN/RETRACTED)
8. **Fix immediately**: Apply fixes to source files as they are found. Build after each fix to verify compilation. Do not accumulate unfixed findings.

### The Six Hostile Examiners

Deploy the following adversarial perspectives on formula-dense or conceptually novel pages:

- **Beilinson** (falsification-first): Is every "proved" claim actually proved? Are there circular dependencies? Is the scope honest?
- **Witten** (mathematical physics): Does the mathematics reproduce known physics? Are physical claims rigorous or heuristic? Are they correctly qualified?
- **Costello** (factorization algebras): Is the categorical framework correct? Are Ran space constructions well-defined? Is "factorization coalgebra" used correctly?
- **Gaiotto** (vertex algebras/W-algebras): Are κ formulas correct? Are Koszul duals correctly identified? Do shadow tower computations match the VOA literature?
- **Drinfeld** (Yangians/quantum groups): Are Yangian structures correctly defined? Is the DK bridge correctly stated? Are prefundamental modules correctly characterized?
- **Kontsevich** (operads/formality): Is the operadic framework correct? Are formality claims properly proved? Is the L∞ structure correctly defined? Is terminology precise?

### Known Error Patterns (from audit history)

The manuscript has specific recurring failure modes. Watch for:

- **AP1**: κ(W_N) formula copied incorrectly between sections (7+ correction commits historically)
- **AP3**: Pattern-completing a formula from adjacent families without recomputing
- **AP5**: Fixing a formula in one location but not propagating to all other occurrences
- **AP8**: Writing "self-dual" for Virasoro without specifying which duality and which c
- **AP9**: Confusing κ (modular characteristic) with c (central charge) or with κ_c (Hessian eigenvalue)
- **Shift confusion**: s vs s⁻¹ in bar (desuspension) and cobar (also desuspension in this manuscript's convention per signs appendix line 1316)
- **Bernoulli signs**: Â(x) has alternating signs, Â(ix) = (x/2)/sin(x/2) has all positive coefficients. F_g values are POSITIVE.
- **Heisenberg non-self-duality**: H_k^! = Sym^ch(V*) ≠ H_{-k}. This is a critical pitfall.

### Pace and Depth

- **Pages with no math** (TOC, blank, part titles): Note structural consistency, move on immediately.
- **Expository pages** (preface, introduction): Full verification of every formula. Error rate ~1 per 2-3 pages historically.
- **Formal proof pages** (body chapters 3-11): Verify theorem statements, check proof logic, verify key sign computations. Error rate ~0 historically but verify anyway.
- **Formula tables**: Verify EVERY entry independently. Tables are the #1 error source (copied formulas).

### Build Discipline

- After every fix: rebuild (`make fast` or `pdflatex`). Verify 0 undefined references.
- After every 10 pages: run compute tests (`python3 -m pytest compute/tests/ -x --tb=short -q`).
- Never accumulate more than 3 unfixed findings before building.

### Completion Criteria

The audit is complete when:
- Every page of the target volume(s) has been read and verified
- Every finding has been fixed, retracted, or documented as OPEN with justification
- The build is clean (0 undefined references, 0 undefined citations)
- All compute tests pass (22,000+)
- The findings register is complete with running totals

## Beilinson Rectification Loop — Chapter-Level Protocol

When instructed to "run the Beilinson loop on [TARGET]" (where TARGET is a chapter .tex path), execute the following **convergent iterative loop**. The loop has three stages per iteration and repeats until convergence (Stage 3 audit returns zero actionable findings). This protocol uses Claude Code's tool primitives directly: parallel Agent dispatch, background execution, worktree isolation, and TaskCreate/TaskUpdate for persistent state.

**The loop may run for hours. That is expected and correct.** Each iteration tightens the chapter. Convergence is the only exit condition.

### Initialization: TASK SETUP

Use TaskCreate to register the chapter as a tracked unit of work:
```
TaskCreate(description="Beilinson loop: [TARGET]", status="in_progress")
```

Record iteration count N=0.

---

### ITERATION N (repeat until convergence)

Increment N. Update task: `TaskUpdate(note="Iteration N starting")`

---

### Stage 1: DEEP BEILINSON AUDIT (read-only, adversarial, parallel, falsification-maximizing)

The goal is **maximal falsification from first principles**. Every claim is false until independently verified. Deploy the Six Hostile Examiners (Beilinson, Witten, Costello, Gaiotto, Drinfeld, Kontsevich) on every formula-dense or conceptually novel passage.

Launch THREE Agent tool calls in a SINGLE message (parallel dispatch):

```
Agent(subagent_type="general-purpose", run_in_background=true,
  description="RED audit [chapter] iter N",
  prompt="DEEP FALSIFICATION AUDIT of [TARGET], iteration N.
  Read the ENTIRE file. For every mathematical claim — theorem statements,
  proof steps, formulas, definitions, examples, table entries, sign
  conventions, scope qualifiers — INDEPENDENTLY VERIFY from first principles:
  - Recompute every formula (AP1, AP3). Do NOT pattern-match.
  - Check every proof step for logical validity (AP4, AP7, AP13).
  - Verify sign/shift conventions against the signs appendix.
  - Check universal claims against ALL edge cases (AP7, AP18).
  - Verify every cross-reference resolves and hypotheses match.
  - Check status tags against what the proof actually proves (AP4, AP12).
  - Deploy the Six Hostile Examiners on dense passages.
  - Cross-check numerical formulas against compute/tests/ and compute/lib/.
  Output: numbered findings (line, severity, class, claim, issue, proposed fix).
  Be MAXIMALLY adversarial. A finding you miss now propagates forever.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="BLUE audit [chapter] iter N",
  prompt="STALENESS + CONSISTENCY AUDIT of [TARGET], iteration N.
  Read TARGET + concordance.tex + CLAUDE.md + landscape_census.tex.
  - Flag every claim whose status changed (conjecture->theorem, restricted->general).
  - Flag every formula that differs from landscape_census.tex or the compute layer.
  - Flag duplicate subsection numbers, broken label references, AP12 violations.
  - Flag AP5 violations: formulas that appear in other files with different values.
  - Flag AP8/AP9 violations: ambiguous terminology, same-name-different-object.
  - Flag AP14 violations: Koszulness/formality conflation.
  - Flag AP15 violations: holomorphic/quasi-modular conflation.
  - Grep BOTH ~/chiral-bar-cobar AND ~/chiral-bar-cobar-vol2 for variant forms.
  Output: numbered findings with exact file:line locations across both volumes.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="GREEN audit [chapter] iter N",
  prompt="COMPLETENESS + FRONTIER AUDIT of [TARGET], iteration N.
  Read TARGET + git log -50 + concordance.tex + memory files.
  - Identify proved results that SHOULD appear in this chapter but are missing.
  - Identify structural gaps: missing definitions, unproved lemmas cited, dangling
    forward references, proof chains with unstated hypotheses.
  - Rank every gap by mathematical importance (load-bearing vs cosmetic).
  - For each gap, assess: can it be CLOSED with existing tools, or is it genuinely open?
  - Check against the full MC1-5 status, Koszulness programme, shadow tower status,
    three-pillar architecture, platonic completion theorem, entanglement programme,
    open/closed realization, shadow-formality all-arity.
  - Identify opportunities to STRENGTHEN: conjectures that are now theorems,
    conditional results whose conditions can be removed, scope restrictions that
    can be lifted.
  Output: numbered findings ranked by mathematical priority, with concrete proposals.")
```

All three run in background. When all three report back, merge findings into a single **FINDINGS REGISTER** with deduplication. Classify each: (A) logical/circular, (B) formula, (C) structural, (D) status, (E) editorial. Severity: CRITICAL > SERIOUS > MODERATE > MINOR. This register is the input to Stage 2.

Update task: `TaskUpdate(note="Iteration N Stage 1 complete: F findings (C critical, S serious, M moderate)")`

---

### Stage 2: ADVANCE (rewrite, rescaffold, close gaps, advance frontier)

**The north star**: Chriss-Ginzburg. The standard: Kac, Etingof, Bezrukavnikov, Gelfand, and the entire elite Russian school. Every object earns its place by solving a specific problem. Every paragraph forces the next. Scope is honest at every claim boundary. The mathematics is CORRECT, COMPLETE, and BEAUTIFUL.

This stage has two sub-phases executed sequentially:

#### Stage 2a: SURGICAL FIXES (build-gated)

For each finding from Stage 1 with severity >= MODERATE, in dependency order:

1. Read the exact location (±50 lines context)
2. Compute the correction independently — NOT by pattern (AP3)
3. Apply the minimal fix with Edit tool
4. Grep BOTH `~/chiral-bar-cobar` AND `~/chiral-bar-cobar-vol2` for all variant forms (AP5)
5. Fix all instances in the same pass

**Build gate**: After every 3 fixes, run `make fast`. Never accumulate > 3 unfixed findings before building. If a fix breaks the build, revert immediately.

Update task: `TaskUpdate(note="Iteration N Stage 2a: J/F findings fixed")`

#### Stage 2b: RECONSTITUTE + ADVANCE (architectural, isolated)

With all audit errors fixed, launch the reconstitution in a worktree for safety:

```
Agent(subagent_type="general-purpose", isolation="worktree",
  description="Reconstitute+advance [chapter] iter N",
  prompt="ARCHITECTURAL RECONSTITUTION AND FRONTIER ADVANCE of [TARGET],
  iteration N. All Stage 1 audit errors are fixed. Now the task is twofold:

  PART I — RECONSTITUTION. Assess against the Chriss-Ginzburg standard:
  (1) Does every object earn its place by solving a specific problem?
  (2) Does every paragraph force the next?
  (3) Is Theta_A the single organizing thread?
  (4) Is scope honest at every claim boundary?
  (5) Would Beilinson, Kac, Etingof, Bezrukavnikov, Gelfand find this satisfactory?

  Propose and execute structural changes: reordering, merging, splitting,
  new material blocks, deleted redundancy, tightened prose. The standard is
  the elite Russian school — no hedging, no filler, no AI slop, every
  sentence carries mathematical weight.

  PART II — FRONTIER ADVANCE. From the GREEN audit's gap analysis:
  (1) Close every gap that can be closed with existing tools.
  (2) Prove every lemma that is cited but unproved, if the proof is within reach.
  (3) Upgrade conjectures to theorems where the proof now exists.
  (4) Remove unnecessary conditions from conditional results.
  (5) Add missing definitions, constructions, or examples that the chapter needs.
  (6) Write new compute tests for any new or modified mathematical claims.
  (7) Strengthen the narrative arc — every chapter should tell a single story
      with Theta_A as protagonist.

  Build after each edit. Report all changes made, gaps closed, and build status.
  If any edit breaks the build, revert that edit and continue.
  Run `make test` after all edits to verify no regressions.")
```

Review the worktree diff. Apply successful changes to main. Discard failed changes.

Update task: `TaskUpdate(note="Iteration N Stage 2b complete: G gaps closed, R rewrites applied")`

---

### Stage 3: RE-AUDIT (adversarial verification of what was just written)

**Critical**: This is NOT a rubber stamp. This is a FRESH adversarial audit of everything written in Stage 2, with the same intensity as Stage 1. The purpose is to catch errors introduced by the rewrite — new formulas that are wrong, new proofs with gaps, new scope claims that are too broad, prose that hedges or bloats.

Launch THREE Agent tool calls in a SINGLE message (parallel dispatch):

```
Agent(subagent_type="general-purpose", run_in_background=true,
  description="RED re-audit [chapter] iter N",
  prompt="ADVERSARIAL RE-AUDIT of [TARGET], iteration N Stage 3.
  Stage 2 just rewrote and advanced this chapter. Your job: FALSIFY
  everything that was just written. Focus especially on:
  - NEW formulas: recompute each one from first principles (AP1, AP3, AP17).
  - NEW proofs: check every logical step. Are hypotheses satisfied? Is scope honest?
  - NEW definitions: are they well-formed? Do they conflict with existing ones?
  - UPGRADED claims: was the upgrade justified? Did the proof actually prove this?
  - REMOVED material: was anything load-bearing deleted?
  - AP17 cascade check: did the rewrite chain multiple unchecked claims?
  Read the FULL file. Output: numbered findings. If you find ZERO actionable
  findings, explicitly state 'CONVERGED: no actionable findings.'")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="BLUE re-audit [chapter] iter N",
  prompt="CONSISTENCY RE-AUDIT of [TARGET], iteration N Stage 3.
  Stage 2 just modified this chapter. Check:
  - Do all new/modified formulas match landscape_census.tex and compute/?
  - Do all new/modified cross-references resolve?
  - Are there new AP5 violations (formula changed here but not elsewhere)?
  - Are there new AP8/AP9/AP14/AP15 violations introduced by the rewrite?
  - Does the chapter still compile? Are there new undefined references?
  - Grep both volumes for any inconsistencies introduced.
  Output: numbered findings. State 'CONVERGED' if zero actionable findings.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="GREEN re-audit [chapter] iter N",
  prompt="QUALITY RE-AUDIT of [TARGET], iteration N Stage 3.
  Stage 2 just rewrote this chapter. Assess against the Chriss-Ginzburg +
  Kac/Etingof/Bezrukavnikov/Gelfand standard:
  - Does the prose meet the standard? No AI slop, no hedging, no dashes where
    a colon or period suffices, no 'notably', 'crucially', 'remarkably'.
  - Does every object earn its place?
  - Are there still structural gaps that Stage 2 missed or introduced?
  - Is there redundancy that should be eliminated?
  - Would a hostile referee at Inventiones accept this chapter as-is?
  Output: numbered findings. State 'CONVERGED' if zero actionable findings.")
```

When all three report back, merge into a FINDINGS REGISTER.

**Convergence test**: If ALL THREE re-audit agents report CONVERGED (zero actionable findings at severity >= MODERATE), proceed to FINALIZE. Otherwise, the findings become the input to the NEXT iteration: return to Stage 1 with N+1, using the Stage 3 findings as the starting register (skip re-auditing claims already verified in this iteration; focus on new/modified material).

Update task: `TaskUpdate(note="Iteration N Stage 3: [CONVERGED | NOT CONVERGED, K new findings]")`

---

### FINALIZE (after convergence)

1. Build both volumes: `pkill -9 -f pdflatex; sleep 2; make fast` and `cd ~/chiral-bar-cobar-vol2 && make`
2. Run full tests: `make test`
3. Grep for any new AP1-AP18 violations introduced by this session
4. Update task: `TaskUpdate(status="completed", note="CONVERGED after N iterations. Npp, M undef refs, K tests passed, J total findings fixed, G gaps closed")`
5. If any theorem status changed, update concordance.tex
6. Report to user: iteration count, total findings fixed, gaps closed, frontier advances, final build status

### Loop State

The TaskCreate/TaskUpdate system persists across context compression and session boundaries. To see loop progress: `TaskList`. To resume after interruption: read the task list, find the latest iteration, and continue from the current stage.

**Chapter ordering** follows the upstream-first dependency DAG: foundations and definitions first, then the five main theorems in order (A, B, C, D, H), then examples, then connections, then appendices.

### Execution Rules (inherited from Beilinson Principle)

- Never edit without reading first
- Never write a formula without computing it
- Never change a correct formula to match a wrong narrative
- After every correction, grep BOTH volumes (AP5)
- The .tex source is ground truth; CLAUDE.md and memory describe beliefs
- A smaller true chapter beats a larger false one
- When agents disagree, trust computation > source > description
- A wrong correction is worse than no correction — mark uncertain fixes with `% RECTIFICATION-FLAG`
- **AP17 applies to your own rewrites**: after writing ANY new theorem in Stage 2, audit it in Stage 3 before building on it in the next iteration
- **The loop runs until convergence, not until fatigue.** If iteration 5 finds errors, iteration 6 runs. Hours-long execution is expected and correct.

## Five Main Theorems (all proved)

- **(A)** Bar-cobar adjunction + Verdier intertwining on Ran(X)
- **(B)** Bar-cobar inversion: Omega(B(A)) -> A quasi-iso on Koszul locus
- **(C)** Complementarity: Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)); upgraded to shifted-symplectic Lagrangian geometry
- **(D)** Modular characteristic: kappa(A) universal, additive, duality-constrained (kappa+kappa'=0 for KM/free fields; kappa+kappa'=rho*K for W-algebras), A-hat GF
- **(H)** Hochschild: ChirHoch*(A) polynomial, Koszul-functorial

## Koszulness Characterization Programme

Major structural component. Two overlapping numbering schemes exist:

**Meta-theorem (thm:koszul-equivalences-meta in chiral_koszul_pairs.tex)**: items (i)-(xii). **10 unconditional equivalences + 1 conditional + 1 one-directional (D-module purity)**. Item (xii) = D-module purity (forward proved, converse open). Concordance section: sec:concordance-koszulness-programme.

**Preface K-numbering (K1-K12)**: a different list of 12 where K12 = bifunctor decomposition (proved). D-module purity is a 13th item outside this list.

**The meta-theorem items (authoritative):**
- (i) PBW degeneration at all genera — unconditional
- (ii) A∞ formality of bar cohomology — unconditional
- (iii) Ext diagonal vanishing — unconditional
- (iv) Bar-cobar counit is quasi-iso — unconditional
- (v) Barr-Beck-Lurie comparison is equivalence — unconditional
- (vi) FH concentrated in degree 0 — unconditional
- (vii) ChirHoch vanishes outside {0,1,2} — unconditional
- (viii) Kac-Shapovalov det nonzero in bar-relevant range — unconditional
- (ix) FM boundary acyclicity — unconditional
- (x) Shadow-formality at arities 2,3,4 — unconditional
- (xi) Lagrangian criterion — **CONDITIONAL** on perfectness/nondegeneracy
- (xii) D-module purity — **ONE-DIRECTIONAL** ((x)⟹(xii) proved, converse open)

**Additional proved characterizations (outside meta-theorem):**
- Tropical Koszulness (thm:tropical-koszulness) — unconditional
- Bifunctor decomposition (thm:bifunctor-obstruction-decomposition) — one consequence of Koszulness (not an equivalence)
- Curve independence (prop:genus0-curve-independence) — proved
- PBW universality (prop:pbw-universality) — proved (sufficient condition)

## Three Concentric Rings (the architecture)

**Ring 1** — Proved core: Theorems A-H, **all five MC1-5 proved (MC3 all simple types)**, DK-0 through DK-3, MC3 thick generation (all simple types), MC4 strong completion towers (thm:completed-bar-cobar-strong, W_N rigidity, 21 conjectures resolved), MC5 all-genera sewing (thm:general-hs-sewing, thm:heisenberg-sewing), Koszulness 10 unconditional + 1 conditional + 1 one-directional (thm:koszul-equivalences-meta); D-module purity partially proved (13th characterization).
**Ring 2** — Nonlinear characteristic layer (the shadow Postnikov tower), FULLY INTEGRATED across Parts I-III. The primary mathematical object is the filtered finite-order engine: Theta_A^{<=2} (kappa), Theta_A^{<=3} (cubic shadow), Theta_A^{<=4} (quartic shadow), ... with obstruction classes o_{r+1}(A) in the cyclic deformation complex. Proved at finite order: kappa for all families, cubic shadows, quartic resonance class with clutching law (via Mok's log FM degeneration). Q^contact_Vir = 10/[c(5c+22)]. Genus-1 Hessian correction delta_H^(1)_Vir = 120/[c^2(5c+22)]x^2. Shadow archetypes computed in every example chapter: Heisenberg=Gaussian/terminates@2, affine=Lie/tree/terminates@3, betagamma=contact/quartic/terminates@4, Virasoro/W_N=mixed (infinite tower, quintic forced). Shadow depth classification into four classes: G (Gaussian, r_max=2), L (Lie/tree, r_max=3), C (contact/quartic, r_max=4), M (mixed, r_max=infinity). Operadic complexity conjecture (conj:operadic-complexity): r_max(A) = A∞-depth = L∞-formality level. The shadow tower = L∞ formality obstruction tower identification is PROVED at arities 2,3,4 (prop:shadow-formality-low-arity). Ambient complementarity = shifted-symplectic Lagrangian geometry, CONDITIONAL on perfectness/nondegeneracy hypotheses. The full Theta_A (all arities, all genera) is PROVED by the bar-intrinsic construction (thm:mc2-bar-intrinsic): Theta_A := D_A - d_0 is MC because D_A^2 = 0. The shadow tower consists of its finite-order projections.
**Ring 3** — Physics-facing frontier: W-algebra axis (MC4 W_infty closed unconditionally), Yangian/RTT axis (**MC3 fully proved all types**, DK-5 accessible), holographic/celestial axis (anomaly-completed Koszul duality, M2 example in Vol II, holographic modular Koszul datum H(T) = (A, A!, C, r(z), Θ_A, ∇^hol) packaging the full HT holographic system into a single modular MC problem with five theorem targets). **MC4 splitting**: MC4⁺ (positive towers: W_{1+∞}, affine Yangians, RTT — SOLVED by weight stabilization, thm:stabilized-completion-positive) vs MC4⁰ (resonant towers: Virasoro, non-quadratic W_N — reduced to finite resonance problem by thm:resonance-filtered-bar-cobar). Resonance rank ρ(A) (def:resonance-rank) classifies completion difficulty. Platonic completion conjecture (conj:platonic-completion): every positive-energy chiral algebra has ρ < ∞. Vir_{26-c} reinterpreted as depth-zero resonance shadow. **Analytic completion programme** (raeeznotes90): sewing envelope A^sew (Hausdorff completion for sewing-amplitude seminorms), analytic bar coalgebra B^an(A) (graph-norm closure), analytic Koszul pairs, HS-sewing condition (Hilbert-Schmidt multiplication → trace-class amplitudes), coderived analytic shadows Q_g^an(A), shadow partition function. Platonic chain: A_alg ⊂ A^sew ⇝ F_A ∈ IndHilb ⇝ Q•^an(A). Four target theorems/conjectures: (A_an) Heisenberg sewing theorem (thm:heisenberg-sewing, PROVED: one-particle Bergman reduction, Fredholm determinant, thm:heisenberg-one-particle-sewing), (B_an) lattice sewing envelope (thm:lattice-sewing, PROVED), (C_an) analytic realization criterion (conj:analytic-realization, conjectural), (D_an) boundary bar duality (conj:boundary-bar-duality, conjectural). HS-sewing PROVED for entire standard landscape (thm:general-hs-sewing: polynomial OPE growth + subexponential sector growth ⟹ convergence). References: Moriwaki 2026 (conformally flat FH in IndHilb, Heisenberg/Bergman), Adamo-Moriwaki-Tanimoto 2024 (conformal OS for unitary full VOAs).

**Unifying principle**: The modular L∞ convolution algebra g^mod_A is the single organizing structure. It carries a natural modular L∞ structure (from the Feynman transform of the modular operad); the dg Lie algebra (def:modular-convolution-dg-lie) is its strict model. The shadow Postnikov tower is the finite-order projection of the universal MC element Θ_A. The shadow Postnikov tower — κ (arity 2), cubic shadow C (arity 3), quartic resonance class Q (arity 4) — consists of finite-order projections of the universal MC element Θ_A (thm:mc2-bar-intrinsic). Theorems A-D+H and the genus expansion are proved projections of the scalar level κ. The full MC element Θ_A ∈ MC(g^mod_A) satisfying D·Θ + ½[Θ,Θ] = 0 is PROVED: Θ_A := D_A - d_0 is MC because D_A² = 0 (thm:convolution-d-squared-zero). The weight filtration on g^mod controls the extension tower; each finite truncation Θ_A^{<=r} is constructive and does not require the full all-genera modular envelope.

## Three-Pillar Foundational Architecture (NEW)

Three preprints force upgrades at three levels. Recorded in concordance.tex sec:concordance-three-pillars.

**Pillar A** (MS24): Primitive local object = homotopy chiral algebra (Ch∞), not strict. Strict chiral algebra appears after rectification. Ch∞ → strict on H^• → PVA/coisson shadow.
**Pillar B** (RNW19+Val16): Universal deformation machine = filtered convolution sL∞-algebra hom_α(C,A). Deformation space = MC ∞-groupoid. dg Lie algebra = strict model. **Key constraint**: hom_α extends to ∞-morphisms in either slot separately but NOT both simultaneously (no-bifunctor obstruction). MC3 categorical lift must proceed one slot at a time.
**Pillar C** (Mok25): Global collision geometry = log FM compactification FM_n(X|D) on snc pairs. Tropicalization = planted forests (G_pf = Trop(FM_n(C|D))). Semistable degeneration formula → clutching laws.

**Eleven identification theorems** (9 proved, 2 structural):
1. g^mod_A = hom_α(C^!_ch, P^ch) (thm:convolution-master-identification)
2. Θ_A ∈ MC(hom_α) ≅ Tw_α (cor:theta-twisting-morphism)
3. G_pf = Trop(FM_n(C|D)) (thm:planted-forest-tropicalization)
4. B(A) is Ch∞-algebra (thm:cech-hca)
5. B_κ ⊣ Ω_κ is Quillen equivalence (thm:quillen-equivalence-chiral)
6. A^sh is homotopy invariant (thm:shadow-homotopy-invariance)
7. One-slot obstruction constrains MC3 (RNW19 Theorem 6.1)
8. F_n = o_n: secondary Borcherds operations = shadow tower obstruction classes (prop:borcherds-shadow-identification)
9. Quartic clutching law via Mok's degeneration formula [Mok25, Cor 5.3.4] (constr:arity4-degeneration)
10. Log clutching conjecture proved via [Mok25, Cor 5.3.4] (conj:log-clutching-degeneration → proved)
11. Ambient D²=0 proved via Mok's log FM normal-crossings [Mok25, Thm 3.3.1] (thm:ambient-d-squared-zero)

## The Chriss-Ginzburg Principle (the architecture)

Every algebraic structure in the monograph is a Maurer-Cartan element in a convolution dg Lie algebra. The key objects:

1. **Modular cyclic deformation complex** `Def_cyc^mod(A)` (def:modular-cyclic-deformation-complex in chiral_hochschild_koszul.tex): the ambient home. Differential from graph composition, bracket from stable-curve gluing.
2. **Stable-graph and planted-forest coefficient algebras** `G_st`, `G_pf` (def:stable-graph-coefficient-algebra, def:planted-forest-coefficient-algebra in higher_genus_modular_koszul.tex): the explicit combinatorial heart of g^amb_A.
3. **Shadow Postnikov tower** Θ_A^{<=r}: the proved finite-order truncations. Each level is a graph sum through arity r with obstruction class o_{r+1}(A) in the cyclic deformation complex.
4. **Bar complex as modular operad algebra** (thm:bar-modular-operad in bar_cobar_adjunction_curved.tex): {B^(g,n)(A)} is an algebra over FCom (Feynman transform of commutative modular operad). ∂²=0 at all genera is a formal consequence.
5. **Modular dg-shifted Yangian as pro-MC** (def:modular-yangian-pro in yangians_drinfeld_kohno.tex): Y_T^mod = pronilpotent completion of convolution dg Lie algebra. R_T^mod(z;ℏ) is an MC element.
6. **Shadow algebra** `A^sh` (def:shadow-algebra in higher_genus_modular_koszul.tex): H_•(Def_cyc^mod(A)) as graded commutative ring. Shadows (κ, Δ, C, Q, Sh_r) are graded projections at finite order. The all-arity master equation is the MC equation projected to arity r. The full tower convergence Θ_A = varprojlim Θ_A^{<=r} is PROVED (thm:recursive-existence).
7. **Koszulness characterization programme** (sec:concordance-koszulness-programme in concordance.tex, thm:koszul-equivalences-meta in chiral_koszul_pairs.tex): 12 equivalent characterizations of chiral Koszulness (K1-K12, **10 unconditionally proved equivalent + 1 conditional + 1 one-directional**; D-module purity = 13th, partially proved). K1-K12: PBW degeneration, A∞ formality, shadow-formality, E₂-formality, curve independence, PBW universality, Barr-Beck-Lurie, FH concentration, FM boundary acyclicity, tropical Koszulness, Lagrangian criterion (conditional on perfectness/nondegeneracy), bifunctor decomposition.

8. **Platonic package** Π_X(L) (constr:platonic-package in concordance.tex): six-fold datum (Fact_X(L), B̄_X(L), Θ_L, L_L, (V^br_L, T^br_L), R_4^mod(L)) from cyclically admissible Lie conformal algebra L (def:cyclically-admissible). Target: modular factorization envelope U^mod_X as left adjoint of primitive-current functor Prim^mod (conj:platonic-adjunction). Envelope + bar coalgebra + universal MC class = platonic form. **UPGRADED** to eight-fold **completed platonic datum** Π^oc_X(A) (def:thqg-completed-platonic-datum in thqg_open_closed_realization.tex): adds chiral derived center Z^der_ch(A) (universal bulk), annulus trace Tr_A ≃ HH_*(A) (first modular shadow of open sector), and nonlinear resonance tower R^oc_•(A) (quartic and higher obstructions in Z^2). **KEY DISTINCTION**: bar/cobar classifies TWISTING MORPHISMS (universal couplings between A and A!); the derived center classifies BULK OPERATORS acting on the boundary. The open/closed MC element Θ^oc = Θ_A + Σ μ^{M_j} packages both (constr:thqg-oc-mc-element).
9. **Cubic gauge triviality** (thm:cubic-gauge-triviality in higher_genus_modular_koszul.tex): If H^1(F^3g/F^4g, d_2) = 0, then cubic MC term is gauge-trivial and the quartic class [Θ'_4] ∈ H^2(F^4g/F^5g, d_2) is canonical. Abstract reason first nonlinear shadow is quartic.
10. **Independent sum factorization** (prop:independent-sum-factorization in higher_genus_modular_koszul.tex): For L = L₁ ⊕ L₂ with vanishing mixed OPE, all shadows separate: κ additive, T^br direct sum, Δ multiplicative, R_4^mod additive.
11. **Graphwise cocomposition** (const:vol1-graphwise-log-fm-cocomposition): Δ^log_Γ := (ν_Γ)_* ∘ Res_{D^log_Γ}, Γ-amplitude ℓ_Γ, Taylor coefficients ℓ_k^(g) = Σ_Γ |Aut(Γ)|^{-1} ℓ_Γ.
12. **Boundary operators as residue correspondences** (const:vol1-boundary-operators-residue): d_sew, d_pf, ℏΔ as residue/pushforward on log-FM strata. D²=0 = codimension-2 face cancellation.
13. **Depth filtration and tridegree** (def:vol1-rigid-planted-forest-depth-filtration): Tridegree (g,n,d) = (loop genus, arity, log boundary depth) from Mok's stratification.
14. **Genus spectral sequence** (const:vol1-genus-spectral-sequence): E_1 page isolates tree (p=0), one-loop (p=1), genus-2 shell (p=2) data. Differentials = obstruction maps Ob_g. DISTINCT from PBW spectral sequence.
15. **Modular tangent complex** (const:vol1-modular-tangent-complex): L∞ twisted differential d_{Θ_A}(x) = Σ (ℏ^g/n!) ℓ_{n+1}^(g)(Θ_A^⊗n, x); strict chart = d + [Θ_A, -]. Characteristic projections: κ, Δ_A, R^mod_4.
16. **Θ_A as universal twisting morphism** (cor:vol1-theta-log-fm-twisting-data): MC_•(Def∞^mod_log) ≃ Tw_α^mod.

17. **Shadow metric** `Q_L` (def:shadow-metric in higher_genus_modular_koszul.tex): quadratic form on each primary line L. The MC equation on L is equivalent to H² = t⁴Q (thm:riccati-algebraicity): shadow tower is algebraic of degree 2. Gaussian decomposition Q = (2κ+3αt)² + 2Δt². Critical discriminant Δ = 8κS₄ classifies shadow depth: Δ = 0 ⟺ tower terminates.
18. **Shadow connection** ∇^sh = d - Q'/(2Q) dt (thm:shadow-connection): logarithmic connection of Q_L. Residue 1/2 at zeros of Q. Monodromy = -1 (Koszul sign). Complementarity of discriminants: Δ(A) + Δ(A!) = 6960/[(5c+22)(152-5c)] (constant numerator). Self-dual at c=13.
19. **Propagator variance** δ_mix = Σf_i²/κ_i - (Σf_i)²/Σκ_i (thm:propagator-variance): multi-channel non-autonomy on the diagonal. Non-negative by Cauchy-Schwarz. Vanishes iff quartic gradient curvature-proportional (enhanced symmetry). Mixing polynomial P(W₃) = 25c²+100c-428. Computable from arity 2+4 alone.
20. **Arithmetic packet connection** ∇^arith_A (def:arithmetic-packet-connection in arithmetic_shadows.tex): flat meromorphic connection on the arithmetic packet module M_A = ⊕_χ M_χ over the spectral s-line. Singular divisor D_A = ∪_χ div(Λ_χ) is independent of nilpotent parts (thm:packet-connection-flatness). Arithmetic skeleton Ask(A) = M_A^ss controls divisor; algebraic defect Def_alg(A) = ⊕ N_χ M_χ contributes only unipotent monodromy. Principle: **arithmetic is semisimple; homotopy defect is unipotent**. Frontier defect form Ω_A = d log Λ_Eis - d log φ measures discrepancy between activated L-packets and automorphic scattering (def:frontier-defect-form). Gauge criterion (prop:gauge-criterion-scattering): Eisenstein block matches scattering connection iff Ω_A exact. Miura splitting for W_N (prop:miura-packet-splitting): Heisenberg core arithmetically inert; all obstructions in finite defect sector. Arithmetic comparison conjecture (conj:arithmetic-comparison): Θ_A canonically determines ∇^arith, higher-genus MC data accesses frontier defect residues.

The proved core descends from finite-order truncations of the shadow tower. The full equation **D_A Θ_A + ½[Θ_A, Θ_A] = 0** is PROVED at all levels: D²=0 at the convolution level is a THEOREM (from ∂²=0 on M̄_{g,n}), and at the ambient level D²=0 is also PROVED (thm:ambient-d-squared-zero, via Mok's log FM normal-crossings result). The all-arity inverse limit Θ_A = varprojlim Θ_A^{≤r} exists (thm:recursive-existence). Scalar saturation universality is proved for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape at all non-critical levels (for affine Kac-Moody, this includes admissible levels; for W-algebras, the UNIVERSAL algebra W^k(g) is Koszul at ALL levels by Feigin-Frenkel free generation; the SIMPLE QUOTIENT W_k(g) at admissible levels has Koszulness OPEN (bar-Ext vs ordinary-Ext gap)).

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
make test                                                         # Fast tests (~8.1K)
make test-full                                                    # All tests (~8.8K)
python3 scripts/generate_metadata.py                              # Census (authoritative)
```

**CAUTION**: Watcher spawns competing pdflatex; always kill before builds.

## Session Entry

1. Read this file — especially the Beilinson Principle and anti-patterns AP1–AP13
2. Build: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast`
3. Run tests: `make test`
4. `git log --oneline -10` for recent context
5. Identify which rectification tier/task to continue (upstream-first in the dependency DAG)
6. Read relevant .tex source before any edit — never write from memory or description
7. After each change: build + test. After each correction: grep both volumes for all variants (AP5)
8. Never guess a formula — compute it or cite it. Check `landscape_census.tex` (AP1)
9. At session end: build both volumes, run tests, summarize errors found by class

## Critical Pitfalls — MEMORIZE THESE

**Five objects that must never be conflated:**
- A: the algebra. B(A): the bar coalgebra. A^i = H*(B(A)): the dual coalgebra. A^! = (A^i)^v: the dual algebra.
- Omega(B(A)) = A (bar-cobar INVERSION, not duality). A^! is obtained by VERDIER/LINEAR duality, not cobar.
- Z^der_ch(A) = H*(C^•_ch(A,A), δ): the chiral derived center (UNIVERSAL BULK). This is NOT the bar complex. Bar/cobar = twisting morphisms (couplings). Derived center = bulk operators acting on boundary. The open/closed MC element Θ^oc = Θ_A + Σμ^M packages both (thm:thqg-swiss-cheese, thm:thqg-oc-mc-equation).

**Grading**: COHOMOLOGICAL (|d|=+1). Bar uses DESUSPENSION.
**Koszul duality**: Com^! = Lie (NOT coLie). Heisenberg NOT self-dual. Chiral Koszulness != classical Koszulness.
**Curved A-infinity**: m_1^2(a) = [m_0, a] (COMMUTATOR, MINUS sign). Bar d^2=0 always; curvature shows as m_1^2 != 0.
**Sugawara**: UNDEFINED at critical level k=-h^v (not "c diverges"). Feigin-Frenkel: k <-> -k-2h^v.
**Virasoro**: Self-dual at c=13, NOT c=26. Vir_c^! = Vir_{26-c}. The same-family shadow Vir_{26-c} is the DEPTH-ZERO RESONANCE SHADOW (rem:virasoro-resonance-model): it is the image of the finite-dimensional resonance truncation R_Vir, not the final dual. The genuine W_∞-type dual requires the full resonance-filtered completion (conj:platonic-completion).
**FM compactification**: Blowup along diagonals, NOT complement of diagonal.
**Prime form**: Section of K^{-1/2} boxtimes K^{-1/2} (NOT K^{+1/2}).
**QME**: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2).
**d_bracket^2 != 0**: PROVED (all 2048 signs). Full Borcherds d gives d^2=0.
**sl_2 bar H^2 = 5** (not 6; Riordan WRONG at n=2).
**Convolution algebra**: The dg Lie algebra Conv_str(C,P) is a STRICT MODEL of the underlying modular L∞ algebra Conv_∞(C,P). MC moduli coincide; full L∞ needed for transfer, formality, gauge equivalence. Bar-cobar preserves quasi-isos BECAUSE it is a quantum L∞ functor.
**Shadow tower (the primary object)**: The shadow Postnikov tower Θ_A^{<=r} consists of finite-order projections of the bar-intrinsic MC element Θ_A := D_A - d_0 (thm:mc2-bar-intrinsic). κ, C, Q are successive projections. The full Θ_A is PROVED by the bar-intrinsic construction. All-arity convergence Θ_A = varprojlim Θ_A^{<=r} is PROVED (thm:recursive-existence). Scalar saturation universality is PROVED for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape. The residual conjecture is restricted to non-algebraic-family constructions (no known modular Koszul example with simple Lie symmetry).
**D²=0**: At the convolution level, D²=0 is a THEOREM (from ∂²=0 on M̄_{g,n}). At the ambient level (with planted-forest corrections), D²=0 is now PROVED (thm:ambient-d-squared-zero, via Mok's log FM normal-crossings, [Mok25, Thm 3.3.1]).
**Shadow depth vs Koszulness**: Shadow depth r_max does NOT characterize Koszulness. Both finite (Heis@2, aff@3, βγ@4) and infinite (Vir@∞) shadow depth algebras are Koszul. Shadow depth classifies COMPLEXITY of Koszul algebras (G/L/C/M classes), not Koszulness itself.
**Single-line dichotomy** (thm:single-line-dichotomy): On any 1D primary slice of Def_cyc^mod, the shadow metric Q_L(t) = (2κ + αt)² + 2Δt² with critical discriminant Δ = 8κS₄ forces r_max ∈ {2, 3, ∞}. The four-class partition G/L/C/M is structural: Δ = 0 ↔ perfect square Q_L ↔ finite tower (G or L); Δ ≠ 0 ↔ irreducible Q_L ↔ infinite tower (M). The contact class C (r_max = 4) escapes via STRATUM SEPARATION: the quartic contact invariant lives on a charged stratum whose self-bracket exits the complex by rank-one rigidity. Total depth d = 1 + d_arith + d_alg (thm:depth-decomposition). Algebraic depth d_alg ∈ {0, 1, 2, ∞}. Depths ≥ 5 are purely arithmetic (cusp forms).
**Universal vs simple quotient**: V_k(g) is Koszul for ALL k (prop:pbw-universality). L_k(g) may fail at admissible levels. The PBW criterion applies to the UNIVERSAL algebra; failure for simple quotients comes from vacuum null vectors.
**Three-pillar constraints**: (1) The convolution sL∞-algebra hom_α(C,A) is NOT a strict Lie algebra — it is shifted homotopy Lie with higher brackets ℓ_k (k≥3). The dg Lie is a strict MODEL only. (2) hom_α is functorial in either slot separately but FAILS as a bifunctor in both slots simultaneously (RNW19 §6). MC3 categorical lift must proceed one slot at a time. (3) Log FM compactification FM_n(X|D) ≠ classical FM; requires snc pair (X,D). Ordinary FM is the D=∅ special case.
**Non-principal W-duality**: DS reduction for arbitrary nilpotent f EXISTS (Kac-Roan-Wakimoto). The obstruction is NOT defining W_k(g,f); it is proving bar-cobar/Koszul COMMUTES with non-principal reduction. Hook-type in type A is PROVED corridor. Full arbitrary-nilpotent BV duality is CONJECTURAL. Proposition 21.19.29 in current global form COLLAPSES theorem/conjecture boundary — must be restricted to proved cases (principal, sl₃ subregular/minimal, hook-type).
**Factorization envelopes**: Nishinaka's construction starts from Lie conformal algebras, NOT arbitrary vertex algebras. The factorization envelope gives the ENVELOPING vertex algebra, not an arbitrary one. Vicedo's construction is the full/non-chiral analogue. Neither constructs the MODULAR completion — that is the frontier.
**Analytic vs algebraic**: The bare VOA/chiral algebra is a dense algebraic skeleton. The actual object for partition functions and sewing is the sewing envelope A^sew (Hausdorff completion). Curvature at genus g ≥ 1 forces coderived/contraderived categories, NOT ordinary derived categories. IndHilb-valued factorization homology (Moriwaki 2026) is 1-categorical, metric-dependent, conformally flat only — NOT yet the full analytic story.
**Planted-forest correction**: δ_pf^{(g,0)} is the d_pf component of D acting on Mok's rigid codimension-≥2 log-FM strata. Genus-2 formula EXACT: S_3(10S_3−κ)/48. Genus-3: 8-term polynomial in κ,S_3,S_4,S_5 (eq:delta-pf-genus3-explicit, genus-1+ vertex weights approximate). Self-loop parity vanishing (prop:self-loop-vanishing): single-vertex (0,2k) with k self-loops has I=0 for ALL k≥2 (odd-dimensional parity obstruction). Shadow visibility genus: g_min(S_r) = floor(r/2)+1 (cor:shadow-visibility-genus). Pixton conjecture (conj:pixton-from-shadows): class-M algebras generate Pixton ideal via infinite MC tower — computationally supported at genus 2-3, formal ideal membership OPEN (requires strata algebra/admcycles). Compute module: pixton_shadow_bridge.py (75 tests).

## LaTeX Rules

- All macros in main.tex preamble — NEVER \newcommand in chapter files (use \providecommand for compatibility)
- Document class: memoir; fonts: EB Garamond via newtxmath + ebgaramond
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic
- Label everything: \label{def:}, \label{thm:}, etc. Cross-reference with \ref, never hardcode.

## What NOT To Do

- Do not add packages without checking preamble compatibility
- Do not change verified formulas without checking Critical Pitfalls
- Do not create new .tex files when content belongs in existing chapter
- Do not duplicate definitions — reference from Part I
- Do not guess file locations — use Glob/Grep to find them

## Key File Renames (from platonic cleanup)

| Old name | New name |
|----------|----------|
| kac_moody_framework.tex | kac_moody.tex |
| w_algebras_framework.tex | w_algebras.tex |
| detailed_computations.tex | bar_complex_tables.tex |
| examples_summary.tex | landscape_census.tex |
| deformation_theory.tex | chiral_hochschild_koszul.tex |
| deformation_examples.tex | deformation_quantization_examples.tex |

## Titan Splits (dispatchers → parts)

| Original | Split into |
|----------|-----------|
| higher_genus.tex | higher_genus_foundations + higher_genus_complementarity + higher_genus_modular_koszul |
| yangians.tex | yangians_foundations + yangians_computations + yangians_drinfeld_kohno |
| bar_cobar_adjunction.tex | bar_cobar_adjunction_curved + bar_cobar_adjunction_inversion |

## Git — HARD RULE

All commits authored by Raeez Lorgat. **Never credit an LLM.** No "co-authored-by", no "generated by", no AI attribution anywhere.

## Constitution

**Single source of truth**: concordance.tex (the constitution). When chapters disagree, the constitution is right.

**MC frontier** (all five MC1-5 proved; MC3 all simple types via multiplicity-free ℓ-weights):
- MC1: **PROVED** (PBW concentration, all standard families)
- MC2: **PROVED** (bar-intrinsic construction, thm:mc2-bar-intrinsic): Θ_A := D_A - d_0 is automatically MC because D_A² = 0. No restriction to simple Lie symmetry needed. Scalar saturation (Θ = κ·η⊗Λ) proved for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape at all non-critical levels (for affine Kac-Moody, this includes admissible levels; for W-algebras, the UNIVERSAL algebra W^k(g) is Koszul at ALL levels by Feigin-Frenkel free generation; the SIMPLE QUOTIENT W_k(g) at admissible levels has Koszulness OPEN (bar-Ext vs ordinary-Ext gap)). Residual universality conjecture restricted to non-algebraic-family constructions.
- MC3: **PROVED FOR ALL SIMPLE TYPES** (thm:categorical-cg-all-types, cor:mc3-all-types): chromatic filtration + categorical prefundamental CG closure via multiplicity-free ℓ-weights (Chari-Moura) + Francis-Gaitsgory pro-nilpotent completion + DK on compacts. The type A proof (thm:mc3-type-a-resolution) was the original template; the all-types generalization replaces the minuscule hypothesis with the strictly weaker multiplicity-free ℓ-weight property. DK-5 now accessible for all simple types.
- MC4: **PROVED** — Strong completion-tower theorem (thm:completed-bar-cobar-strong): finite-stage bar-cobar passes to inverse limits automatically via strong filtration axiom μ_r(F^{i_1},...,F^{i_r}) ⊂ F^{i_1+...+i_r}, yielding arity cutoff (lem:arity-cutoff) that makes continuity + ML automatic. CompCl(F_ft) carries quasi-inverse bar-cobar homotopy equivalence (cor:completion-closure-equivalence), stable under MC twisting (thm:mc-twisting-closure), with completed twisting representability (thm:completed-twisting-representability). Coefficient-stability criterion (thm:coefficient-stability-criterion) reduces convergence to finite matrix stabilization. Uniform PBW bridge (thm:uniform-pbw-bridge) connects MC1→MC4. **MC4 SPLITTING**: MC4⁺ (positive towers: W_{1+∞}, affine Yangians, RTT — SOLVED by weight stabilization) vs MC4⁰ (resonant towers: Virasoro, non-quadratic W_N — reduced to finite resonance problem by thm:resonance-filtered-bar-cobar). W_N rigidity (thm:winfty-all-stages-rigidity-closure, 21 conjectures resolved). Remaining example-specific task: coefficient stabilization on finite windows + H-level target identification.
- MC5: **PROVED** — Inductive genus determination + 2D convergence (no UV renormalization needed) + analytic-algebraic comparison + general HS-sewing criterion (thm:general-hs-sewing: polynomial OPE growth + subexponential sector growth implies convergence at all genera). Heisenberg sewing theorem proved (thm:heisenberg-sewing, thm:heisenberg-one-particle-sewing: one-particle Bergman reduction, Fredholm determinant).
- Theta_A: **PROVED** by bar-intrinsic construction (thm:mc2-bar-intrinsic): Θ_A := D_A - d_0 ∈ MC(Def_cyc(A) ⊗̂ G_mod). Shadow algebra A^sh = H_•(Def_cyc^mod). Named shadows (κ, Δ, C, Q) are projections of this single element (cor:shadow-extraction). All-arity master equation = MC equation projected to arity r. Q^contact_Vir = 10/[c(5c+22)]. Scalar saturation proved for all algebraic families (thm:algebraic-family-rigidity) via Whitehead reduction + algebraic semicontinuity; residual conjecture restricted to non-algebraic-family constructions.
- Koszulness characterization programme: recorded in concordance.tex sec:concordance-koszulness-programme. 12 equivalent characterizations K1-K12 of chiral Koszulness (**10 unconditionally proved equivalent + 1 conditional + 1 one-directional**, thm:koszul-equivalences-meta in chiral_koszul_pairs.tex). 10 unconditional: PBW degeneration, A∞ formality, shadow-formality, E₂-formality, curve independence, PBW universality, Barr-Beck-Lurie, FH concentration, FM boundary acyclicity, tropical Koszulness. 1 conditional: Lagrangian criterion (K11, thm:lagrangian-koszulness, pending perfectness/nondegeneracy). 1 one-directional: bifunctor decomposition (K12, one implication proved). D-module purity is a 13th characterization, partially proved (forward direction established, converse open).

## Six Frontier Research Directions (raeeznotes85-91)

**Direction 1: Platonic Holographic Programme** (raeeznotes86). Every HT holographic system T should be controlled by a holographic modular Koszul datum H(T) = (A, A!, C, r(z), Θ_A, ∇^hol). Central claim: the dg-shifted Yangian r(z) is the binary genus-0 shadow of Θ_A, i.e. r(z) = Res^coll_{0,2}(Θ_A). Five theorem targets: boundary-defect realization, Yangian-shadow, sphere reconstruction (2026 GZ commuting differentials = scalar shadow of Sh_{0,n}(Θ_A)), quartic resonance obstruction, singular-fiber descent. Modular shadow connection ∇^hol_{g,n} = d − Sh_{g,n}(Θ_A). Deformation-quantization bridge Q_HT: classical coisson → quantum Koszul (Khan-Zeng 3d PVA sigma model).

**Direction 2: Analytic Sewing Programme** (raeeznotes89). The platonic ideal: formal OPE data ⊂ sewing envelope ⇝ Hilbert factorization theory ⇝ coderived shadow invariants. Sewing envelope A^sew = Hausdorff completion for all-amplitude seminorm topology. HS-sewing condition: Σ q^{a+b+c} ‖m^c_{a,b}‖²_HS < ∞ implies trace-class closed amplitudes. Analytic bar coalgebra. Analytic Koszul pair. Heisenberg sewing theorem PROVED (thm:heisenberg-sewing: one-particle Bergman reduction, Fredholm determinant). HS-sewing PROVED for entire standard landscape (thm:general-hs-sewing). Curvature forces coderived passage at genus g ≥ 1. IndHilb-valued conformally flat factorization homology (Moriwaki 2026).

**Direction 3: Factorization-Envelope Technology** (raeeznotes90/91). Pipeline: Lie conformal algebra → factorization envelope → factorization algebra → vertex algebra ≅ enveloping VA (Nishinaka 2025/26, generalizing KM + Virasoro; Vicedo 2025, full/non-chiral). Platonic target: universal modular factorization envelope U^mod_X(L) as left adjoint of modular primitive-current functor Prim_mod. Six-fold package Π_X(L) = (F_X, B̄_X, Θ_L, L_L, (V^br, T^br), R^mod_4). Envelope-shadow functor Θ^env_{≤r}(R). DS reduction as functor on platonic packages: Θ_{W_N} = DS(Θ_{ĝ}).

**Direction 4: Non-Principal W-Algebra Duality** (raeeznotes88). Hook-type in type A is the first genuine proved non-principal corridor (Fehily, Creutzig-Linshaw-Nakatsuka-Sato, 2023-2025). Transport propagation lemma: hook-type seeds + edge-compatibility → transport-closure duality. Type-A transport-to-transpose conjecture: (W_k(sl_N, f_λ))! ≃ W_{k^∨_λ}(sl_N, f_{λ^t}). KEY CORRECTION: arbitrary DS reduction EXISTS (Kac-Roan-Wakimoto); what remains is proving bar-cobar/Koszul commutes with non-principal reduction.

**Direction 5: MC4 Completion Programme** (raeeznotes87). MC4 PROVED. MC4 splits into MC4⁺ (positive towers: solved by stabilization) and MC4⁰ (resonant towers: finite resonance). Resonance rank ρ(A) classifies completion difficulty. Platonic completion conjecture: every positive-energy chiral algebra has ρ < ∞. Virasoro: Vir_{26-c} = depth-zero resonance shadow, not final dual. MC5 now also PROVED (all-genera HS-sewing).

**Direction 6: Strategic Bottleneck** (raeeznotes85). All five MC1-5 proved. The MC3 extension to all simple types is now complete (cor:mc3-all-types). The completed inverse-limit bar/cobar problem for non-quadratic, infinite-generator chiral algebras is resolved by the strong completion-tower theorem (MC4). Non-principal W-duality and factorization-envelope technology are the active growth directions.

## Vol II (~/chiral-bar-cobar-vol2)

Five parts: I (Bar Complex -> Swiss-Cheese), II (Descent Calculus), III (Dualities and Bulk-Boundary-Line), IV (Standard Landscape), V (Quantization and Holography).

The bar complex's differential = C-direction factorization. Its coproduct = R-direction factorization. Together: Swiss-cheese algebra on FM_k(C) x Conf_k(R). At genus g >= 1: curved Swiss-cheese with curvature kappa * omega_g.

**Vol II status**: ALL foundational items PROVED. Recognition theorem PROVED (Weiss cosheaf descent, lem:product-weiss-descent). Homotopy-Koszulity of SC^{ch,top} PROVED (via Kontsevich formality + transfer from classical Swiss-cheese). PVA descent D2-D6 ALL PROVED: D2-D5 via repaired geometric proofs (exchange cylinder + three-face Stokes on FM_3(C)); D6 via H3(a) factorization + topological contractibility (no extra hypothesis beyond (H1)-(H4)). Operad⟹axioms (F4) PROVED. Axioms⟹operad (F5, rectification) PROVED via homotopy-Koszulity. Stokes⟹A∞ (FM1) PROVED. Zero conjectural algebraic inputs remain beyond the standing physical axioms (H1)-(H4) and standard published results (Kontsevich formality, GK94, BM03, CG17, AF15). Cross-volume bridges catalogued in concordance.
