# REWRITE STRIKE LIST v29 — Chriss-Ginzburg Forge
# Date: 2026-03-13
# Scope: All chapters, ordered by book sequence

---

## Severity Legend
| Code | Category | Rewrite Action |
|------|----------|---------------|
| G | Mathematical gap | Close or flag with `% REWRITE-GAP:` |
| L | Loose amalgamation | Fuse into one passage with governing thread |
| D | Dead prose | Cut or compress to essential content |
| M | Mechanism-blind | Prepend mechanism sentence; restructure |
| O | Orphan definition | Move/reframe to serve its theorem |
| P | Proof architecture | Restructure for transparent logic |
| R | Remark vacuum | Explain connection or delete |
| X | Cross-reference as bureaucracy | Add illuminating clause |
| S | Stale qualifier | Update to match concordance.tex |
| E | Example as drill | Rewrite as portrait |

---

## Part I — Theory (chapters/theory/)

### introduction.tex (1357 lines) — HEAVIEST SINGLE TARGET

1. introduction.tex:70-413 — **L/D** — MASSIVE: ~340 lines of session-log-grade MC4/MC5 frontier detail (stage-4 packets, stage-5 corridors, singleton coefficients, Yangian seed-and-shift). This reads like autonomous session notes pasted into a governing remark. COMPRESS TO ~20 LINES naming the frontier without listing every proposition/corollary.
2. introduction.tex:70 — **D** — "On the standard towers, the first open W∞-side packet is the exact stage-4 six-defect vanishing problem on I_4" — this level of specificity belongs in concordance.tex or yangians.tex, not the introduction.
3. introduction.tex:264-413 — **D** — DUPLICATE: Corollaries and propositions about spectral factorization seed-lines are stated ~3 times with slight variation (lines 264-302, 302-347, 349-402). These are literally repeated text blocks.
4. introduction.tex:404-413 — **D** — "the standard-tower MC5 dependency theorem is already theorematic on the realized MC4 locus" — this sentence makes sense only to someone who already knows the full MC hierarchy. An introduction should not require such context.
5. introduction.tex:415-533 — **EXEMPLARY** — "The logarithmic seed" section. Tight, mechanism-first, the Chriss-Ginzburg standard.
6. introduction.tex:536-620 — **EXEMPLARY** — "The four theorems" section. Clear, structural, each theorem in one breath.
7. introduction.tex:622-689 — **EXEMPLARY** — Central charge complementarity theorem and proof. Perfect illustration of the scalar package.
8. introduction.tex:731-758 — **L/S** — Remark "Scope" repeats MC1-5 status already given in lines 56-69, and also repeats MC4 frontier detail from lines 70-413. FUSE with lines 56-69 into a single scope paragraph.
9. introduction.tex:797-804 — **D** — "On the present theorem surface this hierarchy is not programme prose..." — defensive hedging. Cut; the theorem reference speaks for itself.
10. introduction.tex:929-990 — **EXEMPLARY** — "Five geometric ingredients" remark. Tight, structural, illuminating.
11. introduction.tex:992-1019 — **EXEMPLARY** — DK square remark. Clean.
12. introduction.tex:1021-1074 — **EXEMPLARY** — Master functorial correspondence table. Excellent.

### algebraic_foundations.tex — GOOD overall
13. algebraic_foundations.tex — **M** — Opening should name the mechanism: "operadic prerequisites exist to make the bar transform a functor, not just a construction." Currently launches into definitions without motivation.

### bar_cobar_construction.tex — EXEMPLARY opening
14. bar_cobar_construction.tex:1-80 — **EXEMPLARY** — Nilpotence-periodicity correspondence. This IS the Chriss-Ginzburg standard.
15. bar_cobar_construction.tex — **D** — Scattered "the proof is similar" or "by analogy" placeholders (systematic search needed). Each should be either expanded to a complete proof or cut.

### chiral_koszul_pairs.tex — GOOD overall
16. chiral_koszul_pairs.tex — **M** — Opening paragraph could name the governing mechanism more sharply: chiral Koszul pairs exist because configuration space residues respect the operadic quadratic structure.

### koszul_pair_structure.tex — GOOD
17. koszul_pair_structure.tex — **L** — Chapter likely has loose amalgamation in later sections where pair theory properties are listed without synthesis.

### configuration_spaces.tex — NEEDS WORK
18. configuration_spaces.tex:14 — **D** — Floating \label outside any environment. Move into the governing remark.
19. configuration_spaces.tex — **M** — FM compactification chapter should open with the geometric mechanism: "The Arnold relation is a residue theorem on the FM boundary, and it is the genus-0 reason that d²=0."

### higher_genus.tex — GOOD opening
20. higher_genus.tex — **L** — Later sections (genus tower, period corrections) likely accumulate sequential exposition without synthesis. Audit interior.

### chiral_modules.tex — NEEDS WORK
21. chiral_modules.tex:1-10 — **D** — Governing question remark is boilerplate ("which part of the modular bar-cobar construction..."). Replace with a chapter-specific mechanism statement.
22. chiral_modules.tex — **D** — Floating label `rem:chiral-modules-hms` outside any environment.

### deformation_theory.tex — GOOD
23. deformation_theory.tex — **R** — Check whether later remarks connecting to BV/BRST explain the connection or just name it.

### poincare_duality.tex — GOOD
24. poincare_duality.tex — **EXEMPLARY** — Circularity problem framing.

### poincare_duality_quantum.tex — NEEDS WORK
25. poincare_duality_quantum.tex:1-10 — **D** — No \chapter{} command visible; governing question is boilerplate copy-paste. This may be a \section within poincare_duality.tex that got separated.

### hochschild_cohomology.tex — GOOD
26. hochschild_cohomology.tex — **M** — Check that the SBI sequence explanation names the geometric reason (clutching + trace) rather than just the algebraic formalism.

### en_koszul_duality.tex — GOOD
27. en_koszul_duality.tex — **R** — Check that the "two axes" (chiral vs. topological) remark explains WHY they're separate, not just THAT they are.

### derived_langlands.tex — GOOD
28. derived_langlands.tex — **S** — Verify that KL conjecture scope matches concordance.tex current status (DK-2/3 proved on eval-gen core).

---

## Part II — Examples (chapters/examples/) — HEAVIEST REWRITE TERRITORY

### lattice_foundations.tex — GOOD
29. lattice_foundations.tex:1-100 — **EXEMPLARY** — Clean definitions, good table, functorial structure announced.

### free_fields.tex — NEEDS WORK
30. free_fields.tex:14-18 — **D** — Four consecutive floating \label commands outside any environment.
31. free_fields.tex — **D** — Chapter title "Examples" is too generic; should be "Free field atoms" or similar.

### beta_gamma.tex — NEEDS WORK
32. beta_gamma.tex:48-60 — **G/P** — Degree-2 bar complex decomposition writes tensor-product components with no indices or grading data; differential matrix entries truncated mid-proof.
33. beta_gamma.tex — **E** — The beta-gamma computation should be a PORTRAIT showing what Lie-Com duality looks like in practice, not just a coefficient calculation.

### heisenberg_eisenstein.tex — GOOD content, structural issue
34. heisenberg_eisenstein.tex — **D** — No visible \chapter{} heading. Verify this is intentional (may be \input within another chapter).

### kac_moody_framework.tex — GOOD
35. kac_moody_framework.tex — **M** — Verify that the level-shift k → -k-2h∨ is named as the Feigin-Frenkel involution (the MECHANISM) before the formula appears.
36. kac_moody_framework.tex — **E** — sl₂ at level k should be a PORTRAIT: show what the bar complex looks like, what the Koszul dual is, and why the critical level is special—all in one coherent narrative.

### w_algebras_framework.tex — GOOD
37. w_algebras_framework.tex — **M** — DS reduction should be named as "quantum gauge-fixing" up front, then the formalism unpacks it.

### w3_composite_fields.tex — GOOD
38. w3_composite_fields.tex — **EXEMPLARY** — The Lambda = :TT: - (3/10)∂²T derivation is a model computation.

### w_algebras_deep.tex — NEEDS WORK
39. w_algebras_deep.tex:1-10 — **D** — Opens directly with \subsection{} and no \chapter{} or introductory paragraph. Needs a mechanism sentence.
40. w_algebras_deep.tex — **L** — Likely heavy loose amalgamation: this is the "deep W-algebra theory" chapter built incrementally across many sessions.

### yangians.tex — GOOD opening, likely interior issues
41. yangians.tex — **L** — The §25.9 (∞-categorical factorization KD) was added in a single large session. Check for internal repetition and loose amalgamation.
42. yangians.tex — **D** — Check for repeated formulations of "on the evaluation-generated core" scope qualifiers added post-hoc.

### toroidal_elliptic.tex — GOOD
43. toroidal_elliptic.tex — **R** — Programme tracks should explain WHY they are separate, not just that they are.

### deformation_quantization.tex — GOOD
44. deformation_quantization.tex — **X** — Kontsevich theorem citation should say what it gives (formality + star product), not just reference the theorem number.

### deformation_examples.tex — GOOD
45. deformation_examples.tex — **M** — Pinf vs. coisson distinction is stated but the REASON (different quantization levels) should be the governing sentence.

### genus_expansions.tex — GOOD
46. genus_expansions.tex:1-80 — **EXEMPLARY** — Heisenberg free energy theorem. Clean theorem-proof-remark structure.
47. genus_expansions.tex — **E** — Later family computations (KM, Virasoro, W₃) should each be a PORTRAIT showing what's family-specific vs. what's universal.

### detailed_computations.tex — GOOD
48. detailed_computations.tex — **E** — Arnold relation computation is explicit and correct but should be framed as "the genus-0 reason that d²=0" (portrait, not drill).

### examples_summary.tex — GOOD
49. examples_summary.tex — **EXEMPLARY** — Master table of invariants. Clean, informative.

### minimal_model_fusion.tex — NEEDS WORK
50. minimal_model_fusion.tex:1-5 — **D** — No \chapter{} command. Opens directly with \section.

### minimal_model_examples.tex — NEEDS WORK
51. minimal_model_examples.tex:1-5 — **D** — No \chapter{} command. Opens directly with \section. First remark unlabeled.

---

## Part III — Connections (chapters/connections/)

### concordance.tex — REWRITE WITH EXTREME CARE
52. concordance.tex:1-76 — **EXEMPLARY** — Constitutional apparatus: governing question, present ledger, two minimal objects. Tight.
53. concordance.tex:197-230 — **D** — BD/FG/GLZ comparison tables are factual but could use governing sentences (WHY this comparison matters, not just WHAT the terminology mapping is).
54. concordance.tex — **S** — Systematic audit: every MC status, DK status, and theorem status marker must match the current proved/conjectural boundary. This is the constitution; it must be pristine.

### feynman_diagrams.tex — NEEDS HEAVY WORK
55. feynman_diagrams.tex:23-41 — **M** — "Chiral field theory data" definition is physics-first but doesn't name the bar complex connection until a separate remark. Fuse.
56. feynman_diagrams.tex:36 — **D** — Extremely long single line (~400 chars) for the propagator description. Break into structured definition.
57. feynman_diagrams.tex:84-93 — **G** — "Configuration space interpretation" conjecture is marked ClaimStatusHeuristic but the content is standard (loop number = free integration variable). Either prove it or cite it.
58. feynman_diagrams.tex:95-105 — **P** — "Evidence" environment: the argument is not a proof but not quite heuristic either. Clarify what is being asserted.
59. feynman_diagrams.tex:107-110 — **R** — "Scope" remark says "Type VII (physics-dictionary)" but doesn't explain what that means for the reader.
60. feynman_diagrams.tex:112-150 — **L** — "Bar complex as off-shell amplitudes" section: three consecutive conjecture/evidence/remark triples with the same structure. Fuse into one coherent discussion.
61. feynman_diagrams.tex:120-125 — **D** — Double-dollar display math ($$...$$) should use \[...\] throughout.
62. feynman_diagrams.tex:158-199 — **L** — "Cobar complex and on-shell propagator templates" repeats the same conjecture/evidence/remark pattern. The bar/cobar duality (off-shell/on-shell) should be ONE structural remark, not two parallel copies.
63. feynman_diagrams.tex:162-168 — **G** — Cobar/on-shell propagator conjecture uses momentum-space language ("momenta²") for a position-space construction. The claim needs reformulation.
64. feynman_diagrams.tex — **D** — Throughout: $$ display math instead of \[...\]. Systematic.

### holomorphic_topological.tex — GOOD
65. holomorphic_topological.tex — **S** — Status split declaration must match concordance.tex.

### bv_brst.tex — GOOD
66. bv_brst.tex — **M** — "BV=bar" should be named as the mechanism (antibracket is the bar differential on the antifield complex) before the formal statement.

### physical_origins.tex — GOOD
67. physical_origins.tex — **R** — BLLPRR construction connection to bar-cobar: explain HOW, not just THAT.

### kontsevich_integral.tex — GOOD
68. kontsevich_integral.tex — **X** — Bar-propagator connection should name what the Kontsevich integral gives (universal Vassiliev invariant via configuration space integrals with the same log form kernel).

---

## Frame (chapters/frame/)

### heisenberg_frame.tex — EXEMPLARY
69. heisenberg_frame.tex:1-80 — **EXEMPLARY** — This IS the standard. Mechanism-first, tight, every sentence carries structural weight.

---

## Systematic Patterns (apply across all chapters)

### Pattern A: Boilerplate governing questions
70-80. MULTIPLE FILES — **D** — Several chapters have copy-paste governing question remarks: "The governing question of this chapter is which part of the modular bar-cobar construction..." These should each be chapter-specific mechanism statements. Files: chiral_modules.tex, poincare_duality_quantum.tex, and others (systematic grep for boilerplate needed).

### Pattern B: Floating labels
81-85. MULTIPLE FILES — **D** — Floating \label{} commands outside any \begin{remark}/\begin{theorem} environment. These create invisible anchors. Files: configuration_spaces.tex, free_fields.tex, chiral_modules.tex, and others.

### Pattern C: Missing \chapter{} commands
86-90. MULTIPLE FILES — **D** — Some files that should be standalone chapters open with \section or \subsection instead of \chapter{}. Files: poincare_duality_quantum.tex, w_algebras_deep.tex, minimal_model_fusion.tex, minimal_model_examples.tex.

### Pattern D: Double-dollar display math
91-95. feynman_diagrams.tex + potentially others — **D** — $$...$$ instead of \[...\]. Systematic replacement needed.

### Pattern E: Post-hoc scope qualifiers
96-100. MULTIPLE FILES — **S** — Phrases like "on the evaluation-generated core" or "on the printed simple-Lie-symmetry locus" inserted repeatedly as scope riders. These should be stated ONCE at the governing remark and then assumed.

### Pattern F: Repeated proposition references
101-110. introduction.tex + yangians.tex — **D** — Proposition/Corollary chains stated with slight variation across multiple paragraphs. Deduplicate.

### Pattern G: "This is new" claims
111-115. MULTIPLE FILES — **D** — Several sections end with "This result is new" or "These explicit results are new." This is appropriate in the concordance but reads as self-congratulation elsewhere. Cut or fold into the remark connecting to prior literature.

### Pattern H: HMS route remarks
116-125. ALL CHAPTERS — **D/L** — Every chapter has an HMS route remark (H/M/S route; Convention~\ref{conv:hms-levels}). These are useful in theory but many are boilerplate ("This chapter is primarily M-level..."). Those that say nothing chapter-specific should be compressed to a single-line label or cut.

### Pattern I: Constitutional notes
126-130. MULTIPLE FILES — **D** — "Constitutional note: Chapter 34 (concordance.tex) is the normative status ledger..." LaTeX comments at file top. These are fine as internal documentation but should be consistent (some files have them, some don't).

---

## Summary Statistics

| Category | Count | Distribution |
|----------|-------|-------------|
| D (Dead prose) | ~55 | Heaviest; especially introduction.tex lines 70-413 |
| L (Loose amalgamation) | ~20 | Concentrated in feynman_diagrams.tex, introduction.tex, w_algebras_deep.tex |
| M (Mechanism-blind) | ~12 | Scattered across Part I and Part II openings |
| S (Stale qualifier) | ~10 | Post-hoc scope qualifiers, status mismatches |
| E (Example as drill) | ~8 | Part II computations that should be portraits |
| R (Remark vacuum) | ~7 | Connections named without explanation |
| G (Mathematical gap) | ~5 | feynman_diagrams.tex conjectures, beta_gamma.tex truncation |
| P (Proof architecture) | ~3 | feynman_diagrams.tex evidence environments |
| X (Cross-ref bureaucracy) | ~4 | Missing illuminating clauses |
| O (Orphan definition) | ~2 | Minor |
| EXEMPLARY | ~15 | bar_cobar opening, heisenberg_frame, genus_expansions, master table, logarithmic seed, four theorems, five ingredients, DK square |

**Total sites**: ~210+
**Heaviest single target**: introduction.tex:70-413 (~340 lines of session-log frontier detail)
**Heaviest chapter group**: Part III feynman_diagrams.tex (lowest prose quality per line)
**Best chapters**: heisenberg_frame.tex, bar_cobar_construction.tex opening, concordance.tex opening

---

## Phase 2 Attack Order

1. **introduction.tex** — Compress lines 70-413 to ~20 lines. Deduplicate scope remarks.
2. **feynman_diagrams.tex** — Restructure conjecture/evidence/remark triples. Fix display math.
3. **w_algebras_deep.tex** — Add chapter opening. Audit for loose amalgamation.
4. **chiral_modules.tex** — Replace boilerplate governing question. Fix floating labels.
5. **beta_gamma.tex** — Complete truncated proof. Reframe as portrait.
6. **Systematic patterns** (boilerplate HMS, floating labels, missing \chapter{}, $$)
7. **Remaining Part II chapters** — Mechanism sentences, portrait rewrites.
8. **concordance.tex** — Careful status audit vs. current state.
9. **Part I remaining** — Light touch (mostly GOOD/EXEMPLARY).
