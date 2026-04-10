% Prompting Research Survey -- Wave 12
% Opus 4.6 on the Modular Koszul Duality manuscript
% Author: Raeez Lorgat (research notes)
% Date: 2026-04-09

# Prompting Research Survey (Wave 12)

Scope: which published and folklore prompting techniques, if institutionalised in CLAUDE.md, would reduce the specific failure modes observed over the last ~100 Opus 4.6 invocations on the three-volume Modular Koszul Duality manuscript. Each technique is evaluated against: research backing, applicability to formula-heavy mathematical work, operationalisability without bloating the instruction file, and expected reduction in anti-pattern (AP) violations.

Ground truth: anti-patterns AP1..AP141 in CLAUDE.md, the 150-commit and 300-commit empirical archaeology lists (AP116-AP141), and the cross-volume CG sweep that surfaced 42+ level-stripped r-matrix instances (AP126/AP141).

Citation discipline: I cite papers I am reasonably confident exist; otherwise I mark "folklore" (circulating in the community without a canonical paper) or "observational" (derived from local failure archaeology, not the literature). I do not fabricate authors, years, or venues.

---

## Part 1. Techniques with High Expected ROI

These five are the highest-leverage. Each targets at least three distinct AP families and can be operationalised in under 20 lines of CLAUDE.md prose.

### 1. Chain-of-Verification (CoVe)

- Source: Dhuliawala et al., "Chain-of-Verification Reduces Hallucination in Large Language Models," Meta AI, 2023 (I am reasonably confident in the title and institution; I am NOT certain of the venue).
- Mechanism: the model produces an initial answer, drafts a set of verification sub-questions tailored to that answer, answers each sub-question independently, and then revises the initial answer based on the verification pass. The crucial step is that the verification sub-questions are generated from the first-draft answer itself, so they target whatever the model is most likely to have gotten wrong.
- Applicability: maximally high for formula work. Every r-matrix formula gets a sub-question "does this vanish at k=0?" (AP126/AP141). Every summation gets "what happens at the smallest index?" (AP116). Every kappa formula gets "which family, and what does landscape_census say?" (AP1/AP39). Every harmonic-number expression gets "is H_{N-1} vs H_N - 1?" (AP136). This technique is almost exactly what the empirical AP archaeology asks for, but applied BEFORE the error is made rather than AFTER it is found.
- Integration: lightweight. A single "Verification Pass Protocol" block in CLAUDE.md that names the verification questions by AP number. See Part 5 for draft wording.
- Expected impact: I estimate this would catch the majority of AP116, AP126, AP136, AP141, and AP1 violations at authorship time. It would NOT catch conceptual errors (AP130 fiber-base, AP131 generating vs algebraic depth) because those require ontological distinctions the model may not raise as sub-questions.

### 2. Negative Few-Shot / Error Gallery

- Source: folklore, with partial backing from Wang et al. on in-context learning with negative examples (I do not remember a clean citation; mark as observational).
- Mechanism: rather than showing only correct examples, show explicit WRONG outputs alongside why they are wrong. The model learns the shape of the error as well as the shape of the solution.
- Applicability: extremely high. The AP table already encodes this: AP126 says "r(z) = Omega/z is WRONG; r(z) = k*Omega/z is correct." But the AP table is organised by category, not by visible shape of the error. An explicit "bad formula gallery" that shows the wrong formula FIRST, with a visible strikethrough or negation marker, would exploit the fact that LLMs learn from the form of the text more than from the semantic label.
- Integration: a new appendix to CLAUDE.md, "Gallery of Refuted Formulas," with 15-20 entries. Each entry: WRONG form, CORRECT form, diagnostic check. Key constraint: the WRONG form must be visibly marked (e.g., struck-through or tagged with a token like "[REFUTED]") so that an agent searching for a formula cannot accidentally paste the wrong one.
- Expected impact: AP126, AP129 (reciprocal), AP132 (augmentation ideal vs algebra), AP135 (partition sequence confusion), AP136, AP137 (bosonic/fermionic), AP140. These are all "one symbol off" errors and the negative-example format addresses them directly.

### 3. External Grounding with Mandatory Citation

- Source: folklore, but related to retrieval-augmented generation (Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," 2020) and to what the Claude Code community calls "cite-or-compute."
- Mechanism: every numerical or formulaic claim must be tagged with its source: either a file:line reference (to .tex source or compute/ engine output) or a cited paper with edition and page. The agent is FORBIDDEN from writing a formula from memory without a source tag.
- Applicability: maximal for this manuscript, because the manuscript already has a canonical source (landscape_census.tex) for every kappa formula, and the compute/ layer is the canonical source for every numerical invariant. The failure mode is not that the source is missing; it is that Opus 4.6 does not always consult it.
- Integration: strengthen AP1 from "read landscape_census.tex for that family" to "writing any kappa formula without a cite tag is forbidden, and the cite tag must take the form [landscape_census.tex:FAMILY:LINE] or [compute/MODULE.py:FUNCTION]." Apply the same rule to every numerical constant, not just kappa.
- Expected impact: AP1, AP10 (hardcoded expected values), AP39 (kappa != S_2), AP59 (p_max vs k_max vs r_max), AP62 (dim(g) vs bracket structure). Also AP38 (literature conventions). External grounding is what the Beilinson principle asks for; it just needs to be mechanised.

### 4. Constitutional Critique (operationalised, not aspirational)

- Source: Bai et al., "Constitutional AI: Harmlessness from AI Feedback," Anthropic, 2022. The technique was developed for safety/harmlessness but generalises to any rubric-driven critique.
- Mechanism: after generating a draft, the model critiques it against a written constitution and revises. The key word is "written": the constitution must be a concrete checklist the model can walk through, not a vague principle.
- Applicability: CLAUDE.md's Beilinson principle is the CONSTITUTION. The problem is that the critique step is not operationally enforced: an agent can produce a draft and commit it without self-critique. What is missing is the forcing function.
- Integration: introduce a "Critique Protocol" that the agent MUST execute before committing any prose or formula. The critique is a literal walk through a numbered checklist (a rubric) that is short enough to fit in context but long enough to catch the common errors. See Part 5 for the draft rubric.
- Expected impact: catches everything already in the AP list, but only if the rubric is actually walked. The mechanism that makes this work is the forcing-function: the agent must produce a rubric-scored output BEFORE the edit is accepted. Expected reduction in AP violations: high for AP4 (claim status), AP6 (scope specification), AP32 (uniform-weight tagging), AP36 (iff vs implies), AP40 (environment matches tag), AP139 (unbound variable).

### 5. Plan-and-Solve (Wang et al., 2023)

- Source: Wang et al., "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models," ACL 2023 (I am confident in the title and approximate year; mark the venue as uncertain).
- Mechanism: split the response into a PLAN phase (what steps to take, what to verify) and a SOLVE phase (execute the plan). The plan is produced FIRST and is typically shorter than the eventual answer. The separation reduces the rate at which the model "reaches for the generic formula" without first checking whether the problem's context makes the generic formula wrong.
- Applicability: extremely high for rectification and audit tasks. The observed failure is that the agent, when asked to rewrite a paragraph, starts editing without first planning what it is about to change. Plan-and-solve would force a one-paragraph plan before the edit, which creates an opportunity for a CoVe pass on the plan itself.
- Integration: reshape the skills (/audit, /rectify, /chriss-ginzburg-rectify) so that each one has an explicit PLAN phase before any Edit call. The plan phase outputs a list of (a) files to touch, (b) claims to verify, (c) APs to check. The solve phase executes, and only the solve phase calls Edit.
- Expected impact: AP2 (read the actual .tex, not CLAUDE.md's description of it), AP12 (search entire manuscript for variants before editing), AP17 (audit new theorems before building on them), AP105 and AP108 (structural prose errors), and all the writing-law violations that come from starting to type without a plan.

---

## Part 2. Techniques to Try (Medium Expected ROI)

### 6. Reflexion / Retrospective Critique

- Source: Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," 2023 (I am reasonably confident in authors and year).
- Mechanism: after a task fails, the agent writes a verbal lesson into persistent memory; subsequent tasks consult the memory.
- Applicability: THIS IS WHAT CLAUDE.MD ALREADY DOES. Every new AP is a verbal reinforcement lesson. The question is whether the process can be tightened: can new APs be added mid-session rather than only after the session? And can they be surfaced to agents at the relevant moment rather than always at session start?
- Integration: add a "Session-Local AP Extension" block to CLAUDE.md so that when a new failure is observed, it can be added as a temporary AP (AP-session-NN) for the rest of the session, then folded into the permanent list if it recurs.
- Expected impact: moderate. Reflexion is long-run medicine. The short-run impact depends on whether the added APs are consulted.

### 7. Adversarial Self-Prompting (Devil's Advocate)

- Source: folklore; related to self-consistency literature and to the "red-team your own answer" family of techniques.
- Mechanism: after producing an answer, the model produces a paragraph arguing that the answer is wrong. It then either defends or revises.
- Applicability: useful for audit-heavy tasks; the /audit skill already does a version of this with six hostile examiners. Extending it to every Edit call would be overkill but extending it to every THEOREM statement is plausible.
- Integration: add a "Devil's Advocate" step to the theorem-writing protocol: after writing a theorem, produce three counterexample attempts. If any lands, revise; if none land, record "counterexamples attempted, none succeeded" in the commit message.
- Expected impact: targets AP7 (universal quantifier scope), AP8 (self-dual unqualified), AP32 (untagged weight), AP36 (iff vs implies), AP139 (unbound variable). Adds overhead; recommend for theorem work only, not prose.

### 8. Confidence Calibration / Uncertainty Flagging

- Source: folklore; formalised in various LLM calibration papers (Kadavath et al., "Language Models (Mostly) Know What They Know," 2022 — I am reasonably confident this exists).
- Mechanism: every claim gets a tag such as "certain / likely / uncertain / guess." Uncertain claims are flagged rather than hidden inside confident prose.
- Applicability: the manuscript's ClaimStatus tags already encode this, but only at the granularity of theorems. What is missing is sentence-level calibration inside proofs and prose.
- Integration: lightweight. Introduce an inline marker \claimcert{...} or, less invasively, require agents to begin any speculative remark with "Heuristic:" or "Expected:" and any guess with "Conjecture:". This already exists via \ClaimStatusHeuristic and \ClaimStatusConjectured but is under-used mid-proof.
- Expected impact: moderate. AP36 (iff vs implies), AP41 (prose mechanism vs math mechanism), AP42 (state level of validity), AP43 (central object without definition).

### 9. Template-Filler Prompts

- Source: observational, already in use in Wave 12-5 and earlier waves.
- Mechanism: force a fixed output structure (e.g., "Verdict / Evidence / Recommendation"). The model cannot leave fields blank or reorder.
- Applicability: high for audit reports and AP5 propagation sweeps; less valuable for freeform chapter rectification where rigid structure would constrain prose quality.
- Integration: continue current practice; extend to (a) chriss-ginzburg-rectify output format, (b) verify output format, (c) propagate output format. Each skill should have a template at the top of its prompt.
- Expected impact: low for manuscript quality, high for cross-session consistency and auditability. Worth institutionalising because it costs nothing.

### 10. Rubric-Based Scoring

- Source: folklore; related to LLM-as-judge literature (Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," 2023 — I am reasonably confident this exists).
- Mechanism: the agent scores its own output against a numeric rubric before delivery. Scores below threshold trigger a revision pass.
- Applicability: this is Constitutional Critique (Technique 4) with a numeric layer on top. The numeric layer adds little for formula work but has value for prose: a "CG-score" for chapter openings, a "Beilinson-score" for proof prose.
- Integration: pair with Constitutional Critique. Not a standalone.
- Expected impact: modest standalone; useful as a reinforcement of Technique 4.

---

## Part 3. Techniques That Do Not Apply (Or Are Overhyped for This Manuscript)

### 11. Self-Consistency (Wang et al., 2022)

- Source: Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models," 2022 (reasonably confident).
- Mechanism: sample N reasoning paths, take the majority vote.
- Why it does NOT apply well here: in mathematical manuscript work, the majority answer is often the WRONG answer. AP126 is a case in point: the naive "r(z) = Omega/z" was the majority answer across 42+ instances, all of them wrong. Majority vote would have ratified the error. The correct answer requires grounding, not voting.
- Verdict: low ROI for formulas; potentially useful for ambiguous convention questions (Drinfeld rational vs level-k normalisation) but even there, the better tool is external grounding with citation.

### 12. Tree-of-Thoughts (Yao et al., 2023)

- Source: Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models," NeurIPS 2023 (reasonably confident).
- Mechanism: explore multiple reasoning branches and backtrack.
- Why it does NOT apply well here: overkill for formula verification; the formulas are local and do not require branching search. For higher-level architectural decisions (Drinfeld double sketches, slab bimodule structure) it might help but those are rare events and typically happen in collaboration with advisors, not inside an agent invocation.
- Verdict: narrow applicability. Not worth institutionalising.

### 13. Multi-Agent Debate

- Source: Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate," 2023 (reasonably confident).
- Mechanism: two or more agents argue about a claim before resolving.
- Assessment: the /audit skill with six hostile examiners is already a multi-agent debate. It works. The question is not "add this technique" but "when do we invoke the existing skill?" The answer is: more often, on smaller targets, with tighter rubrics.
- Verdict: already institutionalised; no new integration needed, but the invocation frequency should increase.

### 14. Chain-of-Thought with Explicit Rigor Level

- Source: folklore.
- Mechanism: instruct the agent to compute step-by-step at "Bourbaki standard" vs "physics intuition" depending on context.
- Assessment: sounds useful but in practice the correct rigor level for this manuscript is ALWAYS Bourbaki, except in certain prose passages where Polyakov-Witten voice is required. This is already in the voice-channel list at the bottom of CLAUDE.md. The technique would not add anything new.
- Verdict: redundant with the existing voice channel.

### 15. Extended Thinking / Scratchpad Separation

- Source: folklore, closely related to what Claude Code already exposes via the model's internal reasoning.
- Mechanism: separate a visible scratchpad from the final answer.
- Assessment: Opus 4.6 already has extended thinking available. The question is whether the scratchpad is being USED, not whether it exists. This is a harness-configuration question, not a prompting-technique question.
- Verdict: out of scope for CLAUDE.md; belongs in the harness configuration.

---

## Part 4. Assessment of Claude Code Infrastructure Leverage

Which techniques benefit most from the specific infrastructure of Claude Code with Opus 4.6?

- **Hooks** (PreToolUse, PostToolUse, Stop): the BIGGEST leverage point. A PreToolUse hook on the Edit tool can enforce a Constitutional Critique step before every Edit: if the Edit's new_string contains a kappa formula, the hook requires a citation tag. If it contains a summation, the hook requires a boundary check comment. This makes Techniques 1, 3, and 4 enforceable rather than aspirational.
- **Sub-agents** (spawned via Task or Skill): the second-biggest leverage point. Each sub-agent starts with a clean context and cannot "drift" as far as a long-running main session. Techniques 4 (Constitutional Critique) and 7 (Devil's Advocate) are naturally implemented as spawned sub-agents that score or critique the main agent's work.
- **Skills**: the existing skill library (/audit, /chriss-ginzburg-rectify, /verify, /propagate) is already a Plan-and-Solve implementation at the session level. Each skill is a plan; the model executes. Extending the skills to include explicit PLAN-phase outputs (before any Edit) would add another layer of Plan-and-Solve.
- **Grep, Read, Edit tools**: these make external grounding (Technique 3) cheap. Every citation tag can be verified by grepping the cited file. The cost of verification is near-zero; the cost of a fabricated citation is catastrophic. This asymmetry argues for strict enforcement.
- **Bash tool with build/test integration**: Reflexion (Technique 6) is naturally implemented by running tests after each edit and feeding failures back. The test suite is the external reinforcement signal. This is already partly in place; the question is whether test failures trigger AP-extension writes into a session-local file.

Specific recommendation: the highest-leverage infrastructure move is a PreToolUse hook on Edit that rejects the call unless the new_string has passed a three-question CoVe check (level prefix, boundary index, scope tag). This is Technique 1 + Technique 3 + Technique 4 enforced by the harness, not by the model's willingness to self-discipline.

---

## Part 5. Top Five Draft CLAUDE.md Wordings

These are the exact strings I would add to CLAUDE.md. Each is short enough to fit alongside the existing AP list without doubling the file length.

### Wording 1 (Chain-of-Verification, target: AP116, AP126, AP136, AP141)

> **Verification Pass Protocol (CoVe).** Before writing any formula in .tex or compute/, execute a three-question verification pass. The questions are generated from the formula itself and answered inline in a comment block (LaTeX) or docstring (Python). The three questions:
>
> 1. **Boundary.** If the formula contains a summation, a harmonic number, or an index, substitute the smallest legal value of the index and state the result. (AP116, AP136.)
> 2. **Limit.** If the formula contains a parameter (k, c, lambda, q), evaluate at the natural limiting value (k=0, c=13, lambda=1, q=1) and state whether the result is the expected limit. (AP126, AP141.)
> 3. **Cite.** State the source: landscape_census.tex:FAMILY:LINE, or compute/MODULE.py:FUNCTION, or [AuthorYear, Theorem X]. If none of these can be supplied, the formula is a guess and must be marked \ClaimStatusHeuristic or deleted. (AP1, AP38.)
>
> Verification pass output is persisted as a LaTeX comment or Python docstring. Agents must produce the pass BEFORE the Edit call; the pass is part of the new_string payload, not a separate message.

### Wording 2 (Negative Few-Shot / Error Gallery, target: AP126, AP129, AP132, AP135, AP136, AP137)

> **Gallery of Refuted Formulas.** The following formulas are WRONG. Do not paste them. If you find yourself writing any of them, STOP and consult the corrected form.
>
> [REFUTED] r(z) = Omega / z  -- missing level prefix; correct: r(z) = k * Omega / z. (AP126/AP141.)
>
> [REFUTED] S_4(Vir) = -(5c+22)/(10c)  -- reciprocal error; correct: S_4(Vir) = 10 / [c(5c+22)]. (AP129.)
>
> [REFUTED] B(A) = T^c(s^{-1} A)  -- missing augmentation; correct: B(A) = T^c(s^{-1} Abar). (AP132.)
>
> [REFUTED] 1/eta^2 expansion starts (1, 3, 6, 10, ...)  -- those are triangular numbers; correct: (1, 2, 5, 10, 20, ...) bicoloured partitions. (AP135.)
>
> [REFUTED] kappa(W_N) = c * H_{N-1}  -- wrong by one harmonic-number term; correct: kappa(W_N) = c * (H_N - 1). (AP136.)
>
> [REFUTED] c_{bc}(lambda) = 2(6 lambda^2 - 6 lambda + 1)  -- that is c_{betagamma}; correct c_{bc} = 1 - 3(2 lambda - 1)^2. (AP137.)
>
> [REFUTED] Koszul conductor K_BP = 2  -- that is a ghost constant; correct K_BP = 196. (AP140.)
>
> Grep this gallery before writing any formula that resembles one of these shapes. If your draft matches a refuted form verbatim, you have regressed; revert.

### Wording 3 (External Grounding with Mandatory Citation, target: AP1, AP10, AP38, AP39, AP59, AP62)

> **Citation Mandate.** Every numerical constant and every closed-form formula in the manuscript must carry a cite tag at the point of use, of one of the following forms:
>
> - `% source: landscape_census.tex:line N` (for kappa and related invariants)
> - `% source: compute/MODULE.py::FUNCTION` (for values computed by the engine layer)
> - `% source: [Author, Year, Theorem/Page]` (for literature values; record the convention)
> - `% derived: [one-sentence derivation from first principles]` (only when the above are not available)
>
> Agents are FORBIDDEN from writing a formula without a cite tag. An uncited formula is a guess. The tag must be verifiable: a PostToolUse hook should grep the cited file to confirm the line or function exists. If verification fails, the edit is invalid and must be revised.

### Wording 4 (Constitutional Critique / Rubric Protocol, target: AP4, AP6, AP32, AP36, AP40, AP139)

> **Critique Protocol.** Before any chapter-level Edit is committed, execute the following rubric walkthrough inline in the agent response. Each item gets a yes/no verdict with a one-sentence justification.
>
> 1. **Scope tagged.** Every theorem carries explicit tags for genus, arity, weight (UNIFORM-WEIGHT vs ALL-WEIGHT), and duality side. (AP6, AP32.)
> 2. **Quantifiers closed.** Every variable in a displayed equation is universally quantified or bound by context. No free variables. (AP139.)
> 3. **Implication direction.** "iff" is written only when the converse is proved in the same theorem; otherwise "implies". (AP36.)
> 4. **Claim status matches environment.** \ClaimStatusProvedHere lives inside \begin{theorem}; \ClaimStatusConjectured inside \begin{conjecture}; labels are prefixed thm:/conj:/prop: to match. (AP40, AP125.)
> 5. **Source cited.** Every formula has a cite tag (see Citation Mandate). (AP1, AP38.)
>
> If any item is "no", the edit is not acceptable. Revise and walk the rubric again. The rubric walkthrough is part of the response to the user; it is not suppressed.

### Wording 5 (Plan-and-Solve, target: AP2, AP12, AP17, AP105, AP108)

> **Plan Phase Before Edit.** No Edit call may be issued until the agent has produced a PLAN block in the response. The plan block has three fields:
>
> - **Files to touch.** Absolute paths only. If the list is empty, the plan is to Read, not Edit.
> - **Claims to verify.** Every claim the edit assumes or proves, stated in one sentence each. Each claim carries a verification source (landscape_census, compute/, literature, or derived-here).
> - **APs to check.** The subset of AP1..AP141 that apply to this edit, listed by number. Agents must grep CLAUDE.md for the listed APs before proceeding.
>
> The plan phase output is required. Agents that attempt to Edit without a plan block are operating outside the protocol; the harness should reject such calls via a PreToolUse hook on Edit.

---

## Part 6. Integration Priority and Overhead Estimate

Ranked by (expected AP-reduction impact) / (CLAUDE.md lines added + harness complexity).

| Rank | Technique | Lines added | Harness change | Expected AP reductions |
|------|-----------|-------------|----------------|-------------------------|
| 1 | CoVe Verification Pass (Wording 1) | ~15 | Optional PreToolUse hook | AP1, AP38, AP116, AP126, AP136, AP141 |
| 2 | Error Gallery (Wording 2) | ~20 | None | AP126, AP129, AP132, AP135, AP136, AP137, AP140 |
| 3 | Citation Mandate (Wording 3) | ~12 | Optional PostToolUse grep verify | AP1, AP10, AP38, AP39, AP59, AP62 |
| 4 | Critique Protocol (Wording 4) | ~15 | None (self-discipline) | AP4, AP6, AP32, AP36, AP40, AP125, AP139 |
| 5 | Plan-and-Solve (Wording 5) | ~12 | PreToolUse hook on Edit | AP2, AP12, AP17, AP105, AP108 |
| 6 | Reflexion session-local APs | ~8 | Append-only session file | Long-run reinforcement of new APs |
| 7 | Devil's Advocate on theorems | ~10 | None | AP7, AP8, AP32, AP36, AP139 |
| 8 | Confidence inline markers | ~6 | None | AP36, AP41, AP42, AP43 |

The first five are the recommended immediate integration set. Combined overhead: ~74 lines added to CLAUDE.md plus two hooks (one PreToolUse on Edit, one PostToolUse grep verification). Expected coverage: ~40 of the 141 APs receive an additional enforcement mechanism, and the 13 most common empirical APs (AP116, AP126, AP129, AP132, AP135, AP136, AP137, AP140, AP141, AP1, AP38, AP39, AP40) are covered by at least two independent techniques each.

---

## Part 7. Key Considerations and Risks

1. **Overhead vs compliance.** If the verification pass produces a three-paragraph preamble before every formula, agents will shortcut it. The verification pass must be SHORT enough that shortcutting is not tempting. Target: three one-line questions, three one-line answers.

2. **Rubric fatigue.** A long rubric is a rubric that is skipped. The Critique Protocol in Wording 4 is five items, which is near the upper limit of what an agent will actually walk.

3. **Citation verifiability.** Requiring cite tags without a verification hook creates a new failure mode: fabricated cite tags that look plausible but do not point to real lines. The PostToolUse grep verification is essential.

4. **Harness coupling.** Hooks make the enforcement robust but couple the workflow to the specific Claude Code harness. If the manuscript is opened in a different harness, the hooks are gone. The prose wordings in CLAUDE.md must stand alone, with the hooks as enforcement on top.

5. **Recency bias in APs.** AP126, AP136, and AP141 are the most recent empirical APs and dominate recent attention. This may be unrepresentative of the long-run failure distribution. The verification pass should be structured by the general classes (boundary, limit, cite) rather than hardcoded to specific APs, so that new empirical APs in the same class are automatically covered.

6. **False confidence from rubric passes.** An agent that walks a rubric and passes every item may acquire false confidence. The Beilinson principle says "the rubric is necessary, not sufficient." The critique protocol should end with "If this rubric passed on first try, something is wrong; re-examine the hardest claim."

---

## Appendix A. Citation Honesty Declaration

Citations I am reasonably confident in:
- Dhuliawala et al., Chain-of-Verification, 2023, Meta AI (title and institution confident, venue uncertain)
- Wang et al., Plan-and-Solve, ACL 2023 (title and year confident)
- Wang et al., Self-Consistency CoT, 2022 (confident)
- Yao et al., Tree of Thoughts, NeurIPS 2023 (confident)
- Shinn et al., Reflexion, 2023 (confident)
- Du et al., Multi-agent Debate, 2023 (confident)
- Lewis et al., RAG, 2020 (confident)
- Bai et al., Constitutional AI, 2022, Anthropic (confident)
- Kadavath et al., Language Models (Mostly) Know What They Know, 2022 (reasonably confident)
- Zheng et al., MT-Bench LLM-as-a-judge, 2023 (reasonably confident)

Items I explicitly did NOT cite because I was not confident:
- any negative-example / negative-few-shot paper (marked "folklore/observational")
- any specific adversarial-self-prompting paper (marked "folklore")
- any paper for explicit-rigor-level CoT (marked "folklore")
- any paper for confidence-tagged inline markers (marked "folklore")

I have not fabricated any author, year, or title. Where I was uncertain I have said so.

---

## Appendix B. What This Survey Does NOT Address

- The harness-configuration side (hook registration, skill registration, settings.json edits). These belong in a separate harness-configuration document.
- The prose-quality side (voice channels, Gelfand/Beilinson/Drinfeld). Those are already encoded in CLAUDE.md under the Writing Standard section and are not prompting techniques in the research sense.
- Techniques for improving tool-call efficiency (parallel tool calls, background processes). These belong in a Claude Code best-practices document.
- Long-horizon memory across sessions beyond what is already in MEMORY.md. That is a separate project.

End of survey.
