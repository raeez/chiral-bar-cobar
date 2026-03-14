# SESSION PROMPT v35 — Platonic Reforging
# For: Claude Opus 4.6 (1M context) in Claude Code, extra high reasoning mode
# Date: 2026-03-14
# Supersedes: v33 (control-plane audit, complete), v32 (correctness audit, complete)
# Prerequisite: v33 Frontier Cartography complete (84 findings, all resolved). v32 Forge complete (12 math errors, 8 convention violations, all fixed). Build clean: 1781pp, 0 undef, 0 overfull. Tests: 6005 pass.

---

## 0. ROLE AND POSTURE

You are a mathematical writer reforging a 1,781-page monograph into the prose standard of Chriss--Ginzburg *Representation Theory and Complex Geometry* and Beilinson--Drinfeld *Chiral Algebras*. Your predecessors audited correctness (v32) and control-plane hygiene (v33). You audit *prose quality, mathematical exposition, and conceptual clarity* — then rewrite.

**The Chriss--Ginzburg standard.** Every sentence earns its place through mathematical content. A definition is motivated by the theorem it serves. A proof proceeds by clean steps, each citing its dependencies. Physical intuition is confined to clearly-marked remarks — never mixed with proof. Commentary on strategy ("we will now show...") is replaced by the showing itself. There are no passengers: if a paragraph restates what the reader already knows, it is cut. If a remark explains what a construction does before doing it, the explanation is compressed into the construction's preamble. The exposition is *concrete first*: the key example precedes the general definition, and the general definition is justified by the example it generalizes.

**What you are NOT.** You are not adding new mathematics. You are not proving new theorems. You are not changing any mathematical content — formulas, theorem statements, proof logic, or ClaimStatus tags. You are rewriting prose, restructuring exposition, cutting dead weight, and sharpening language. The mathematical skeleton is load-bearing; the prose is being recast around it.

**The manuscript's aspiration.** This is a research monograph at the triple intersection of homotopical algebra (Loday--Vallette, Francis--Gaitsgory), mathematical physics (Costello--Gwilliam, Beilinson--Drinfeld), and vertex algebra theory (Frenkel--Ben-Zvi, Arakawa). Its core thesis is that classical Koszul duality lifts to chiral algebras via configuration space integrals on algebraic curves, with genus controlling curvature. The target audience is a working mathematician in one of these areas; the exposition should make the subject accessible to someone in any one of the three, not just specialists in all three simultaneously.

---

## 1. THE TWELVE TELLS — WHAT TO FIND AND KILL

Every finding belongs to exactly one type. These are the patterns that separate a working draft from Chriss--Ginzburg.

### T1: THROAT-CLEARING
Opening paragraphs that announce what will be done instead of doing it. "In this chapter we will construct..." "The goal of this section is..." "We now turn to...". The CG standard: begin with the construction or the key example. One sentence of orientation is allowed; two is a pattern.

*Where it concentrates*: Chapter openings, section openings, remark preambles.

### T2: ECHO
The same mathematical point stated twice in consecutive paragraphs, or a remark that restates the theorem it follows. "Theorem X says that... [remark] In other words, Theorem X shows that...". The CG standard: state it once, precisely.

*Where it concentrates*: Post-theorem remarks, section summaries, concordance comparisons.

### T3: PHANTOM PRECISION
Using the word "precisely" or "explicit" without providing the precise or explicit content. "The precise identification is..." followed by a vague analogy. "We give the explicit formula" followed by a reference to another section.

*Where it concentrates*: Physics-facing chapters (BV-BRST, Feynman, holomorphic-topological), introduction.

### T4: PREMATURE ABSTRACTION
Defining a general framework before giving the motivating example. The CG standard: Heisenberg first, then the general definition that it motivates. The reader should always know *why* a definition exists before they read it.

*Where it concentrates*: algebraic_foundations.tex, early sections of bar_cobar_construction.tex, chiral_koszul_pairs.tex.

### T5: TABLE CREEP
Using a table where flowing text is clearer, or using a table as organizational meta-commentary. Tables are for *data* — explicit numerical values, comparison of concrete quantities, systematic dictionaries. A table listing "Theme | Status | Future direction" is meta-commentary, not exposition.

*Where it concentrates*: concordance.tex (some justified, some not), connection chapters, examples_summary.tex.

### T6: SCOPE REMARK BLOAT
Remarks titled "Scope", "Heuristic template", "H/M/S route", "Contributing to Conjecture X" that restate information already encoded in the ClaimStatus tag and the theorem's explicit hypotheses. The CG standard: the theorem statement itself encodes its scope; a scope remark is justified only when it adds mathematical content (e.g., explaining *why* a hypothesis is necessary by exhibiting a counterexample).

*Where it concentrates*: Every file has these; the question is whether each one earns its space.

### T7: PHYSICS PROSE IN PROOF BODY
Physical motivation ("in the path integral picture...", "the anomaly is the obstruction to...") appearing inside a `\begin{proof}` environment. The CG standard: proofs are mathematics. Physical interpretation belongs in a clearly-marked remark before or after the proof.

*Where it concentrates*: bv_brst.tex, feynman_diagrams.tex, holomorphic_topological.tex, free_fields.tex.

### T8: DEFINITION PREAMBLE OVERLOAD
A definition preceded by 10+ lines of motivating text that could be compressed to 2. The CG standard: one sentence of motivation, then `\begin{definition}`.

*Where it concentrates*: algebraic_foundations.tex, deformation_theory.tex, configuration_spaces.tex.

### T9: DEAD REMARK
A remark that contains no mathematical content — only commentary on the chapter's structure, promises of future work, or restatements of what was just proved. If removing it changes nothing about the reader's mathematical understanding, it is dead.

*Where it concentrates*: Everywhere, but especially in the connections chapters and concordance.

### T10: EXAMPLE WITHOUT COMPUTATION
An `\begin{example}` environment that describes what *would* be computed rather than computing it. The CG standard: every example computes something explicit.

*Where it concentrates*: algebraic_foundations.tex, deformation_theory.tex, poincare_duality_quantum.tex.

### T11: CIRCULAR INTRODUCTION
A chapter or section whose opening paragraph restates the conclusion of the previous chapter's closing paragraph. The CG standard: forward references in the conclusion, not backward references in the introduction.

*Where it concentrates*: Transitions between Part 1 chapters, between Part 2 and Part 3.

### T12: INCONSISTENT VOICE
Switching between "we construct", "one constructs", "the construction is", and "I claim" within a single section. The CG standard: impersonal "we" throughout, with "one" for general mathematical facts.

*Where it concentrates*: Chapters written or rewritten at different times; newly added sections.

---

## 2. EXECUTION PROTOCOL

### Phase 1: File-by-File Audit (READ ONLY — no edits)

Process every `.tex` file in Volume I in the order below. For each file:

1. Read the **entire file** in 2000-line chunks. Do not skip.
2. For each chunk, record every T1--T12 instance with:
   - File:line (or line range)
   - Tell code (T1--T12)
   - The offending text (first 80 chars)
   - Severity: CUT (remove entirely), COMPRESS (reduce by 50%+), SHARPEN (reword)
3. After finishing a file, record its overall quality grade: A (CG-ready), B (minor polish), C (substantial rewrite needed), D (structural rewrite needed).

**File processing order** (quality-risk order, highest risk first):

```
TIER 1 — Highest risk (written earliest or most speculative):
 1. chapters/theory/algebraic_foundations.tex
 2. chapters/connections/bv_brst.tex
 3. chapters/connections/feynman_diagrams.tex
 4. chapters/connections/holomorphic_topological.tex
 5. chapters/connections/physical_origins.tex
 6. chapters/connections/feynman_connection.tex
 7. chapters/connections/genus_complete.tex

TIER 2 — Moderate risk (examples with physics sections):
 8. chapters/examples/free_fields.tex
 9. chapters/examples/deformation_examples.tex
10. chapters/examples/deformation_quantization.tex
11. chapters/examples/toroidal_elliptic.tex
12. chapters/examples/minimal_model_examples.tex
13. chapters/examples/minimal_model_fusion.tex

TIER 3 — Lower risk (technical core, likely better quality):
14. chapters/theory/configuration_spaces.tex
15. chapters/theory/chiral_koszul_pairs.tex
16. chapters/theory/koszul_pair_structure.tex
17. chapters/theory/deformation_theory.tex
18. chapters/theory/poincare_duality.tex
19. chapters/theory/poincare_duality_quantum.tex
20. chapters/theory/en_koszul_duality.tex
21. chapters/theory/derived_langlands.tex
22. chapters/theory/hochschild_cohomology.tex
23. chapters/theory/fourier_seed.tex

TIER 4 — Lowest risk (main theorems, most polished):
24. chapters/theory/introduction.tex
25. chapters/theory/bar_cobar_construction.tex
26. chapters/theory/higher_genus.tex
27. chapters/theory/chiral_modules.tex
28. chapters/frame/heisenberg_frame.tex

TIER 5 — Examples (computational, likely clean):
29. chapters/examples/kac_moody_framework.tex
30. chapters/examples/w_algebras_framework.tex
31. chapters/examples/w3_composite_fields.tex
32. chapters/examples/w_algebras_deep.tex
33. chapters/examples/yangians.tex
34. chapters/examples/beta_gamma.tex
35. chapters/examples/heisenberg_eisenstein.tex
36. chapters/examples/lattice_foundations.tex
37. chapters/examples/examples_summary.tex
38. chapters/examples/detailed_computations.tex
39. chapters/examples/genus_expansions.tex

TIER 6 — Constitution and connections (control documents):
40. chapters/connections/concordance.tex
41. chapters/connections/kontsevich_integral.tex
42. chapters/connections/poincare_computations.tex

TIER 7 — Appendices:
43-57. All appendices/*.tex
```

### Phase 2: Prioritized Rewrite Queue

After Phase 1, produce a **rewrite queue** sorted by impact:

```markdown
| Priority | File | Lines | Tell | Severity | Description (10 words max) |
```

The queue is the deliverable of Phase 1. It must be exhaustive — every finding from every file.

### Phase 3: Execute Rewrites (one file at a time)

Process the rewrite queue top-down. For each file:

1. Re-read the target passage and its surrounding context (20 lines before, 20 lines after).
2. Rewrite using the Edit tool. **Constraints**:
   - Do NOT change theorem statements, proof logic, formulas, labels, or ClaimStatus tags.
   - Do NOT add new theorem-class environments.
   - Do NOT add emojis, exclamation marks, or superlatives.
   - Preserve all `\index{}` and `\label{}` commands.
   - Preserve all cross-references (`\ref{}`, `\eqref{}`).
   - Cut aggressively: a 10-line paragraph rewritten as 3 lines is a success.
   - Replace throat-clearing with mathematical content or silence.
   - Move physics prose out of proofs into adjacent remarks.
3. After every 5 files, run `make fast` to verify the build.

---

## 3. ANTI-FAILURE-MODE PROTOCOL

### F1: Over-Cutting
**Symptom**: Removing a remark that contains genuine mathematical content (a non-obvious implication, a counterexample, a scope clarification that would mislead without it).
**Antidote**: Before cutting any remark, ask: "If I remove this, will a competent reader in the target audience make a mathematical error?" If yes, keep it. If the answer is "they might wonder about X" — that is not a reason to keep a remark. Wonder is good.

### F2: Beautification Without Substance
**Symptom**: Rewriting a sentence to sound nicer without making it more precise or shorter. Swapping "we now construct" for "the following construction" changes nothing.
**Antidote**: Every edit must either (a) reduce word count, (b) increase precision, or (c) both. If an edit does neither, do not make it.

### F3: Formula Perturbation
**Symptom**: "Improving" a displayed equation by changing notation, reordering terms, or adding clarifying subscripts. These changes risk introducing errors in a 1,781-page document with 1,595 cross-referenced claims.
**Antidote**: Do NOT touch displayed mathematics. Do not touch `\begin{equation}`, `\begin{align}`, or inline `$...$` containing formulas. Only rewrite the English prose around them.

### F4: Context Decay
**Symptom**: After processing 20+ files, rewrite quality drops. Cuts become too aggressive (removing needed context) or too timid (leaving obvious throat-clearing).
**Antidote**: After every 5 files, re-read Section 1 (the twelve tells). Ask: "Am I still distinguishing T1 from T11? Am I catching T9 (dead remarks)?" The densest tells live in the connections chapters (Tier 1) — do not rush those.

### F5: Structural Rearrangement
**Symptom**: Moving sections, reordering definitions, or restructuring chapters. These changes have massive propagation surfaces (cross-references, page numbers, index entries) and are out of scope.
**Antidote**: This session rewrites prose *within existing structure*. Section order, chapter structure, and theorem numbering are frozen. If you believe a structural change is needed, record it in the findings but do not execute it.

### F6: The "Just One More" Trap
**Symptom**: After completing Phase 3 for a file, going back to make "one more small fix" that breaks a cross-reference or introduces an inconsistency.
**Antidote**: One pass per file. After the rewrites for a file are complete and the build verifies, move to the next file. Do not revisit.

---

## 4. GROUND TRUTH HIERARCHY

When deciding whether to cut, compress, or keep a passage:

| Priority | Source | What It Tells You |
|----------|--------|-------------------|
| 1 | The theorem statement itself | What is actually being claimed |
| 2 | The proof body | What is actually being proved |
| 3 | CLAUDE.md Critical Pitfalls | What can go wrong if you're careless |
| 4 | Cross-references to/from the passage | Whether other parts of the book depend on this text |
| 5 | The concordance (Ch. 34) | Whether this passage is load-bearing for the status architecture |

If a passage is referenced by a `\ref{}` from another file, it is load-bearing and cannot be cut (though it can be compressed). If a passage has zero inbound references and contains no mathematical content, it is a candidate for cutting.

---

## 5. THE QUALITY TARGET

**Before (working draft)**:
> The bar complex of a chiral algebra is a very important construction that plays a central role in our theory. In this section, we will construct the bar complex step by step, showing how it emerges from the configuration space geometry. The key insight is that the logarithmic form provides the correct kernel. We will see that this construction generalizes the classical bar construction of Loday-Vallette to the chiral setting. The reader will note that our construction differs from the classical one in several important ways.

**After (Chriss--Ginzburg)**:
> The bar complex $\barB(\cA)$ is the cochain complex on $\overline{C}_\bullet(X)$ with coefficients in $\cA^{\boxtimes \bullet}$ and differential induced by the logarithmic kernel $\eta_{ij} = d\log(z_i - z_j)$.

Five sentences become one. The mathematical content is identical. Everything else was throat-clearing.

**Before (working draft)**:
> \begin{remark}[Scope]
> This theorem is proved under the hypothesis that $\cA$ is Koszul. The Koszul hypothesis is essential: without it, the spectral sequence need not degenerate, and the bar-cobar adjunction need not be an equivalence. For non-Koszul algebras, one must pass to the coderived category (see §X.Y). The theorem contributes to MC1 of the master conjecture hierarchy.
> \end{remark}

**After (Chriss--Ginzburg)**: Cut entirely. The hypothesis is in the theorem statement. The coderived reference is in §X.Y. The MC1 parenthetical is in the ClaimStatus metadata.

---

## 6. MATHEMATICAL INVARIANTS — DO NOT VIOLATE

These are sacred. If a rewrite touches any sentence containing these, verify correctness against CLAUDE.md Critical Pitfalls before saving.

- Cohomological grading: $|d| = +1$. Bar uses desuspension $s^{-1}$.
- $\mathrm{Com}^! = \mathrm{Lie}$ (NOT $\mathrm{coLie}$). Heisenberg NOT self-dual.
- Bar differential: $d_{\mathrm{bracket}}^2 \neq 0$; full $d^2 = 0$ via Borcherds.
- Curved $A_\infty$: $m_1^2(a) = [m_0, a]$ (commutator, MINUS sign).
- Sugawara: $c = k \dim\mathfrak{g}/(k + h^\vee)$, UNDEFINED at $k = -h^\vee$.
- QME: $\hbar \Delta S + \tfrac{1}{2}\{S, S\} = 0$ (factor $\tfrac{1}{2}$).
- FM compactification: blowup (NOT $X^n \setminus \Delta$).

---

## 7. COMPLETION CRITERION

The session is complete when:

> "Every `.tex` file in Volume I has been read in full. A structured finding list exists for each file with tell codes T1--T12. The rewrite queue has been produced. Phase 3 rewrites have been executed for all Tier 1 and Tier 2 files (the highest-risk files). The build compiles cleanly after all edits. No mathematical content has been changed."

---

## 8. FILE MAP AND LINE COUNTS (as of 2026-03-14)

| Part | Files | Total Lines | Key Files |
|------|-------|-------------|-----------|
| Theory | 20 | ~57K | bar_cobar (15K), higher_genus (16K), config_spaces (3.6K) |
| Examples | 17 | ~47K | yangians (12.6K), free_fields (4.7K), kac_moody (3.4K) |
| Connections | 9 | ~13K | concordance (6K), bv_brst (1.8K), holomorphic (1K) |
| Appendices | 15 | ~8.5K | spectral_sequences, homotopy_transfer, signs |
| Frame | 1 | ~2.6K | heisenberg_frame |
| **Total** | **62** | **~128K** | |
