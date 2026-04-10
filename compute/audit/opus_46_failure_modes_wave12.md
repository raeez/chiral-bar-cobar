# Opus 4.6 Quirks and Failure Modes on the Modular Koszul Duality Programme (Wave 12)

**Scope.** Model-specific failure patterns observed across ~100 Opus 4.6 agent invocations on Vols I-III. These are not generic anti-patterns (AP catalogue) but recurrent behaviours of this specific model on this specific manuscript. Each entry is actionable: the counter-protocol must be something an agent can EXECUTE inside the session, not a disposition to "be careful."

**Format.** Each entry: Name / Description / Evidence / Trigger / Counter-protocol.

**Reference axis.** AP numbers cite the CLAUDE.md anti-pattern catalogue. Wave numbers cite `compute/audit/` audit reports.

---

## FM1. Generic-formula reaching (the "pretty version" attractor)

**Description.** When Opus 4.6 does not remember the exact level-prefixed form of a structural object, it falls back to the canonical textbook version. For the classical r-matrix of affine Kac-Moody, the textbook form is `Omega/z`. The level-prefixed form `k*Omega/z` is equally canonical but less prevalent in training data. Opus reaches for the "pretty" one.

**Evidence.** AP126, AP141. 12 instances in the first CG sweep, 30 more in the full-volume CG sweep. The most violated AP in the manuscript.

**Trigger.** (a) Writing an r-matrix without looking at source; (b) summarising a derivation from context window; (c) paraphrasing a cross-reference.

**Counter-protocol.** Append to every agent prompt that touches r-matrices: "After writing ANY r-matrix formula, substitute k=0 and verify r vanishes. If it does not vanish, the level prefix is missing. Do not proceed until k=0 → r=0." Encode as a literal template the agent must emit before the r-matrix formula.

---

## FM2. Level-prefix dropping on summarisation

**Description.** When Opus summarises a displayed formula from a file read earlier in the conversation, it omits scalar prefactors even if the source had them. This is distinct from FM1: the source is correct, the summary loses the prefix. The lost prefix is usually `k`, `c/2`, `kappa`, or `1/(2*pi*i)` (AP120).

**Evidence.** Wave 10-7 N1 audit L818-821 (k=0 vs k=-h^v discussion summarised without the level prefix on the r-matrix). AP120 (missing 2*pi*i in Cauchy integrals).

**Trigger.** Context-window compression; summarising earlier in the conversation; prose paraphrase of a displayed equation.

**Counter-protocol.** When reproducing a formula from earlier context, Opus must re-Read the source lines verbatim immediately before typing the formula in the response. Template: "Before I write formula X, I will Read file Y at lines [a,b] and copy the displayed equation exactly." Do not rely on the context window cache.

---

## FM3. Bosonic/fermionic conformal-anomaly conflation

**Description.** The bosonic beta-gamma central charge `c_{βγ}(λ) = 2(6λ² - 6λ + 1)` and the fermionic b-c central charge `c_{bc}(λ) = 1 - 3(2λ - 1)²` look structurally similar (both polynomial in λ, both having a centre at λ=1/2) and satisfy `c_{βγ} + c_{bc} = 0`. Opus 4.6 swaps them under pressure.

**Evidence.** AP137. At λ=2: c_{bc} = 1 - 3(3)² = -26 (the classical bosonic string ghost value); c_{βγ} = 2(24 - 12 + 1) = 26. Opus has emitted `c_{bc}(2) = 26` and `c_{βγ}(2) = -26` — sign-swapped pairs.

**Trigger.** Discussing superstring ghosts, BRST reduction, or the Feigin-Frenkel c+c'=26 duality where both ghost systems appear in the same paragraph.

**Counter-protocol.** For any ghost central charge, Opus must immediately substitute λ=2 AND λ=1 after writing the formula and verify: c_{bc}(2) = -26 (fermionic), c_{βγ}(2) = +26 (bosonic), c_{bc}+c_{βγ} = 0 pointwise. Template: "Ghost check: at λ=2, c = _____, expected _____, check _____."

---

## FM4. "k=0 vs k=-h^v" semantic confusion at Kac-Moody

**Description.** Opus conflates two semantically distinct limits of affine Kac-Moody: the abelian limit `k=0` (where `r(z) = 0`, the algebra becomes classically trivial as a chiral object, but remains Koszul) and the critical level `k = -h^v` (where the algebra becomes non-Koszul and the centre jumps). Both "destroy the r-matrix" in a vague sense, so Opus treats them as interchangeable.

**Evidence.** Wave 10-7 N1 audit, L818-821. Opus wrote "at the critical level the r-matrix vanishes" when it meant "at k=0 the r-matrix vanishes; at the critical level k=-h^v the centre jumps."

**Trigger.** Discussing any limit of affine KM; Feigin-Frenkel duality; Sugawara construction.

**Counter-protocol.** For any statement about Kac-Moody limits, Opus must emit a two-row table before prose: `k=0 → r(z)=0, algebra abelian, still Koszul` and `k=-h^v → centre jumps, not Koszul, Feigin-Frenkel dual appears`. The table is the proof of non-conflation.

---

## FM5. Wrong fundamental Lie-algebra dimensions (E_8 and exceptionals)

**Description.** For exceptional Lie algebras, Opus 4.6 generates plausible-looking dimensions that are not in the actual fundamental representation list. For E_8 the correct fundamentals are `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`; Opus has emitted `779247`, which is not any E_8 irreducible.

**Evidence.** Wave 10-8 N2 audit. The number `779247` appears nowhere in the LiE tables or in compute/lib/ canonical data.

**Trigger.** Writing about exceptional holonomy, E-series W-algebras, exceptional coset VOAs.

**Counter-protocol.** For any finite-dimensional Lie algebra fundamental, Opus must Grep `compute/lib/` for the canonical dimension BEFORE writing it in prose. Template: "Before writing dim(rep) = N for [exceptional algebra], I will grep compute/lib/ for the canonical value." If no match, write the symbolic name (`V_{ω_1}(E_8)`) and refuse the numerical value.

---

## FM6. Undefined macros in standalone paper extraction

**Description.** The monograph main.tex defines many custom macros (`\cW`, `\hol`, `\Ran`, `\FM`, `\chHoch`, `\ChirHoch`). When Opus extracts a standalone paper by copying a subset of chapters, it preserves these macros in the body but omits them from the new standalone preamble. The resulting standalone fails to compile or compiles with `??` placeholders.

**Evidence.** Wave 11-4 N6 audit. Opus delivered a standalone extraction of the shadow tower chapter with `\cW`, `\FM`, and `\chHoch` undefined in the new preamble.

**Trigger.** Any task that uses the word "standalone," "extract," "arXiv submission," or "split into separate tex."

**Counter-protocol.** After producing any standalone `.tex`, Opus must run Grep for `\\[a-zA-Z]+` control sequences in the new file and cross-check each against `\newcommand`/`\providecommand`/`\DeclareMathOperator` in the new preamble. Template: `Grep "\\\\[a-zA-Z]+" standalone.tex | sort -u`; for each, verify it is either standard LaTeX, defined in the new preamble, or listed as missing. Do not mark the extraction complete until this list is empty.

---

## FM7. LaTeX structural typo `\end{definition>`

**Description.** Opus 4.6 occasionally produces structural typos where `}` is replaced by `>`. This is specific to LaTeX environments (`\end{foo>` instead of `\end{foo}`). The typo passes visual inspection in small diffs and only surfaces at compile time, often several commits later.

**Evidence.** Wave 10-8 N2 audit: `\end{definition>` found in Vol I overture.

**Trigger.** Edit tool calls where `}` immediately precedes a newline inside a large Edit; dense LaTeX environment nesting.

**Counter-protocol.** After every Edit to a `.tex` file, run Grep with pattern `\\end\{[^}]*>` (and the symmetric `\\begin\{[^}]*>`) on that file. If any match, fix immediately before proceeding. This is cheap enough to embed in a post-Edit hook.

---

## FM8. Universal-quantifier drift on uniform-weight theorems

**Description.** Theorem D holds unconditionally at genus 1 but scales to all genera only under the uniform-weight hypothesis; at g ≥ 2 with multi-weight, there is a cross-channel correction δF_g^cross. Opus writes "for all genera" or "at every g" without the scope tag, silently widening the theorem.

**Evidence.** AP32 ("every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Untagged = violation."). Wave 11 overture audit F1-C1: panel at lines 176-179 displayed the generating function without UNIFORM-WEIGHT tag.

**Trigger.** Writing Theorem D, F_g generating functions, anything involving obs_g.

**Counter-protocol.** Mandate a three-line template before any displayed obs_g or F_g equation: (1) "Scope: g = ___, weight = ___"; (2) "Tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, +δF_g^cross)"; (3) the equation. Untagged equations refuse to build in a pre-commit hook: Grep for `obs_g\|F_g\|lambda_g` and verify every match has UNIFORM-WEIGHT or ALL-WEIGHT within 3 lines.

---

## FM9. Harmonic-number off-by-one `H_{N-1}` vs `H_N - 1`

**Description.** Opus 4.6 confuses `H_{N-1} = sum_{j=1}^{N-1} 1/j` with `H_N - 1 = sum_{j=2}^{N} 1/j`. The two expressions differ for all N ≥ 2 (at N=2, H_1 = 1 but H_2 - 1 = 1/2). The error is invisible in symbolic form and only surfaces when evaluating at N=2.

**Evidence.** AP136. CLAUDE.md itself contained this error: κ(W_N) was written as `c*H_{N-1}` when the correct formula is `c*(H_N - 1)`.

**Trigger.** Writing W_N central-charge formulas, any harmonic-number-shifted expression.

**Counter-protocol.** After writing any formula containing H_N with a shift, Opus must evaluate the formula at N=2 AND at N=3 and compare the two numerical values. Template: "H_{N-1}: N=2 gives 1, N=3 gives 3/2. H_N - 1: N=2 gives 1/2, N=3 gives 5/6. The formula in my text gives: ___." The comparison forces disambiguation.

---

## FM10. Hardcoded part number drift (`Part~IV` vs `\ref{part:…}`)

**Description.** Opus writes cross-volume references as hardcoded roman numerals (`Part~IV`, `Chapter~12`) instead of symbolic `\ref{part:...}`. When a part is inserted, moved, or renamed, the hardcoded references become silently wrong. Caught across all three volumes.

**Evidence.** V2-AP26. The issue became acute in Vol II Part VI (3D HT QFT) reorganisation, where Part IV references to the landscape shifted to Part V without being updated.

**Trigger.** Writing cross-references during prose; meta-discussion of manuscript structure.

**Counter-protocol.** After any Edit to a `.tex` file, Grep for the regex `Part~[IVX]+\|Chapter~[0-9]+` in the file. For every match, replace with `\ref{part:...}` or `\ref{chap:...}`. Encode as a post-Edit hook on chapter files.

---

## FM11. Sugawara shift missing: `av(r(z)) = κ` without the dim(g)/2 correction

**Description.** For abelian chiral algebras (Heisenberg), `av(r(z)) = κ` holds cleanly. For non-abelian Kac-Moody, the Sugawara construction contributes an additional `dim(g)/2` shift: `av(r(z)) + dim(g)/2 = κ(V_k(g))`. Opus writes the abelian form universally, dropping the shift.

**Evidence.** Wave 7-1 preface audit. The abelian case is so central (Heisenberg as CG opening, AP108) that Opus generalises it unconditionally.

**Trigger.** Stating the κ = av(r(z)) correspondence in generality; cross-referencing the Heisenberg opening to KM families.

**Counter-protocol.** Before writing `av(r(z)) = κ`, Opus must first state the family (abelian vs non-abelian). Template: "Family: [Heisenberg | abelian KM | non-abelian KM | Vir | W_N]. For abelian: av(r) = κ directly. For non-abelian KM: av(r) + dim(g)/2 = κ(V_k(g))." The template forces the Sugawara shift into view.

---

## FM12. Mid-response truncation on long audit tasks

**Description.** Opus 4.6 occasionally truncates mid-response when an audit task requires producing both a fix and a summary report in the same turn. The truncation happens between the end of the fix and the start of the report, so the fix lands but the report is lost.

**Evidence.** Wave 11-1 and Wave 11-3 audit sessions.

**Trigger.** Long Edit sequences followed by requested report; "do X and then summarise" prompts exceeding ~8k tokens of output.

**Counter-protocol.** Separate fix execution from report writing across two tool calls. In the first, Opus produces ONLY the Edits and a one-line "fixes complete" marker. In the second, it reads the diff and writes the report. Prompt-level enforcement: "Phase 1: fixes only. Phase 2: report only. Do not combine."

---

## FM13. Auto-completion to the majority-variant

**Description.** When typing a formula that appears in many forms across the literature, Opus 4.6 auto-completes to the most common training-data variant even when the manuscript uses a different convention. Example: `eta(q) = prod(1-q^n)` (missing the `q^{1/24}` prefix that the manuscript consistently uses, AP22). Example: `|s^{-1}v| = |v| + 1` instead of `|v| - 1` (suspension vs desuspension, AP22/AP45).

**Evidence.** AP22, AP44-AP46, AP132. Discovered repeatedly across CG sweeps.

**Trigger.** Typing a formula in prose (not copied from source); formulas that have a "textbook default" and a "manuscript convention"; auto-completing operator-product expansions.

**Counter-protocol.** For any formula in {eta(q), s^{-1}, bar-complex augmentation Ā vs A, OPE vs lambda-bracket}, Opus must break the formula across multiple lines and annotate each term's convention. Template: "eta(q) = q^{1/24} * prod(1-q^n) // q^{1/24} is Vol I convention; NEVER omit." The explicit comment forces conscious writing.

---

## FM14. AP125 label/environment mismatch on tag changes

**Description.** When an agent downgrades a theorem to a conjecture (or upgrades a lemma to a theorem), it changes `\begin{theorem}` to `\begin{conjecture}` but forgets to rename the label from `thm:foo` to `conj:foo`. Agents that later grep for `conj:` miss the conjecture; agents that grep for `thm:` find a non-theorem.

**Evidence.** AP125. Surfaced during the rectify-all sweep when multiple agents produced inconsistent `\ref{thm:...}` targeting conjecture environments.

**Trigger.** Any status-tag change (ProvedHere ↔ Conjectured); theorem ↔ conjecture environment swaps; downgrade following a Beilinson audit.

**Counter-protocol.** Environment-tag changes must be executed as atomic 3-step edits: (1) rename `\begin{X}` and `\end{X}`; (2) rename `\label{Y:foo}` to `\label{Y':foo}`; (3) Grep and replace ALL `\ref{Y:foo}` → `\ref{Y':foo}` across three volumes. No intermediate commit. Template refuses to proceed after (1) until (2) and (3) are done in the same tool call batch.

---

## FM15. Duplicate labels across volumes

**Description.** Parallel agents in different volumes independently create labels with the same natural name (e.g. `conj:kappa-bps-universality` in both Vol I and Vol III). LaTeX compiles each volume independently and silently uses the local definition, but cross-volume references and census scripts break.

**Evidence.** AP124. The case `conj:kappa-bps-universality` surfaced in both Vol I Part V and Vol III Part II.

**Trigger.** Parallel agent swarms that create labels independently; natural-name labels that match a universal concept.

**Counter-protocol.** Before creating any new `\label{foo}`, Opus must Grep for that label across ALL THREE volumes: `grep -rn '\\label{foo}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups`. If any match outside the current file, prefix the new label with a volume tag (`v1-`, `v2-`, `v3-`) or abort and reuse the existing label with a cross-volume reference.

---

## FM16. Silent κ-family conflation when the family is inferred from context

**Description.** When the family (Heis, KM, Vir, W_N) is not stated in the immediately preceding sentence, Opus 4.6 picks κ from the most recently-mentioned family even if the current context has shifted. The shift is usually in a "meanwhile, for Virasoro..." transition paragraph.

**Evidence.** AP1, AP9, AP39. Wave 6 and 8 CG sweeps found multiple instances where κ^{KM} was used in a Vir context and vice versa.

**Trigger.** Transition paragraphs that switch families; prose discussing "all standard families" in the same sentence as a κ formula; retrospective discussion of complementarity.

**Counter-protocol.** Every κ formula must carry an explicit family superscript. Refuse to write bare `κ` or `kappa` in any mathematical context. Template enforced by pre-commit Grep: `\kappa[^_^]` or `\kappa$` (bare κ) should return zero matches in Vols I-III excluding allowed contexts. Vol III already enforces this (AP113); extend to Vols I-II.

---

## FM17. Amplitude/dimension conflation for ChirHoch

**Description.** Theorem H states that `ChirHoch*(A)` is concentrated in cohomological degrees `{0, 1, 2}` with total dimension ≤ 4. Opus 4.6 conflates "cohomological amplitude [0, 2]" (a topological invariant of the complex) with "virtual dimension 2" (an arithmetic invariant computed via Euler characteristic or index), writing `vdim(ChirHoch) = 2` in prose.

**Evidence.** AP134. Discovered in the shadow-tower chapter during rectification.

**Trigger.** Discussing Theorem H in prose; cross-referencing H to virtual dimension statements in Vol III (CY moduli).

**Counter-protocol.** Any sentence mentioning ChirHoch* and a numerical invariant must choose explicitly between "cohomological amplitude = [0, d]" and "virtual dimension = d" and state which is meant. Template: "amplitude [0, 2] ≠ vdim 2; the former is topological, the latter arithmetic." The negation forces disambiguation.

---

## FM18. Generating-depth vs algebraic-depth conflation

**Description.** `d_gen` (the arity at which all higher operations are determined by lower ones) and `d_alg` (whether the tower terminates) are distinct invariants. For Virasoro, `d_gen = 3` (m_3 generates all m_k recursively) but `d_alg = ∞` (class M, non-terminating). Opus writes `d(Vir) = 3` without specifying which depth, or concludes `d_alg(Vir) = 3` because "m_3 generates everything."

**Evidence.** AP131. Discovered in the G/L/C/M classification discussion.

**Trigger.** Discussing the depth classification; writing about class-M algebras; distinguishing Vir from finite-depth families.

**Counter-protocol.** Every depth statement must carry the subscript `gen` or `alg`. Template before any `d(...)` expression: "Depth type: generating (d_gen) or algebraic (d_alg)? For Vir: d_gen = 3, d_alg = ∞." Refuse bare `d(...)` or `depth(...)` in any G/L/C/M context.

---

## FM19. Fiber-base confusion: forms on Σ vs classes on M̄_g

**Description.** `dτ` is a holomorphic form on an elliptic curve E_τ (the fibre of the universal curve over the j-line). `ω_g = c_1(λ)` is a cohomology class on the moduli space M̄_g (the base). These live on different spaces and cannot be equated. Opus 4.6 writes `ω_g = dτ` or similar base-fibre conflations when summarising higher-genus curvature.

**Evidence.** AP130. Caught in the genus-1 curvature discussion (Wave 11 F1-M3: "the phase and the Hodge class live on DIFFERENT spaces").

**Trigger.** Discussing d_fib² = κ · ω_g; any cross-reference from genus-1 OPE to the Hodge bundle.

**Counter-protocol.** Before writing `ω_g = [expression]`, Opus must state the space each side lives on. Template: "LHS lives on M̄_g. RHS lives on ___. For equality, ___ must be a class on moduli; if it is a form on the curve, the correct relation is [integrate over fibre] or [pull back along period map]." Refuses to equate pointwise forms with moduli classes.

---

## FM20. Iff-drift: writing "iff" when only one direction is proved

**Description.** Opus 4.6 has a slight bias toward writing "iff" or the biconditional `⇔` when the converse is obvious-looking but not actually proved in the same theorem. The forward direction is real; the reverse direction is a conjecture that has drifted into a theorem statement.

**Evidence.** AP36 ("Before writing 'iff' or biconditional arrow, STOP: is the converse proved in the same theorem? If not, write 'implies.'"). Discovered in the Koszul 10+1+1 list where one of the equivalences was silently upgraded to a biconditional.

**Trigger.** Writing theorem statements that look symmetric; summarising the Koszulness equivalents; stating complementarity theorems.

**Counter-protocol.** Before writing any `⇔` or "iff," Opus must emit a two-line template: "Forward: [hypothesis] ⇒ [conclusion]. Proved in ___. Reverse: [conclusion] ⇒ [hypothesis]. Proved in ___ OR CONJECTURED." If the reverse is conjectured or unproved, replace `⇔` with `⇒` and add a remark.

---

## FM21. Opus "recovers" a formula by dimensional analysis and gets the prefactor wrong

**Description.** When Opus cannot remember the exact coefficient of a formula, it reconstructs from dimensional analysis. The reconstruction typically gets the powers right but the numerical prefactor (1/2, 1/24, 1/(2πi), 7/5760) wrong. The most common victims are F_g generating-function coefficients and partition-function normalisations.

**Evidence.** AP120, AP128. The Wave 11 audit confirmed F_2 = 7/5760 is in the chapter; earlier drafts had emitted 1/5760 and 7/2880.

**Trigger.** Writing F_g values without a source in the immediate context; summarising Faber-Pandharipande values; reconstructing from "I remember this involves Bernoulli numbers."

**Counter-protocol.** For any numerical coefficient in {F_g, lambda_g, 1/(2πi), Bernoulli numbers, Faber-Pandharipande values}, Opus must Read the canonical source file in compute/lib/ before writing the number. Template: "Before writing F_g = ___, I will Read compute/lib/faber_pandharipande.py at the relevant line and quote the value." No reconstruction from memory.

---

## FM22. "Koszul conductor" numerical substitution errors

**Description.** The Koszul conductor `K = c + c'` is a global duality invariant (e.g. K_BP = 196 for the Bershadsky-Polyakov pair). Local constants (ghost numbers, grading shifts, normalisation factors, C_{(2,1)} = 2) are different numbers that appear in the same paragraph as the conductor. Opus conflates them, writing K_BP = 2 (copying the local ghost constant) instead of K_BP = 196.

**Evidence.** AP140. Discovered in the extremal W-algebra chapter.

**Trigger.** Any paragraph that mentions both the Koszul conductor and a local constant from the same derivation; BP-algebra central charge discussion.

**Counter-protocol.** For any Koszul conductor value, Opus must first write `K = c + c'`, then substitute the two central charges, then evaluate. Template: "K = c + c' = ___ + ___ = ___. Local constants from this derivation are: ___, which are NOT K." The substitution forces the correct value.

---

## Summary statistics

**Total failure modes documented.** 22.

**Covered APs.** AP1, AP7, AP9, AP22, AP32, AP36, AP39, AP44-46, AP113, AP120, AP124-126, AP128, AP130-132, AP134, AP136, AP137, AP140, AP141, V2-AP26.

**Coverage gaps.** FM entries do not exhaust all APs; they document only patterns that Opus 4.6 specifically tends to fall into (as distinct from hypothetically-possible errors). Notably missing: AP5 propagation (Opus handles this well when prompted), AP113 κ-subscripts in Vol III (already enforced at the file level).

**Enforcement model.** Each FM's counter-protocol is designed to be expressible as either (a) a pre-Edit template the agent must emit, (b) a post-Edit Grep hook, or (c) an atomic multi-step template. The three classes are not equally feasible: templates (a) are self-enforcing; hooks (b) require harness support; atomic multi-steps (c) require the agent to resist partial execution.
