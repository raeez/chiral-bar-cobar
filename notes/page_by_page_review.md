# Page-by-Page Review Log

**Goal**: Annals-grade uniformity, harmony, and beauty.
**Method**: Linear pass through the PDF, 3-5 fixes per page, logged here.
**Session**: 2026-03-12

---

## Page 1 (Title + Abstract)

1. **Removed extra `\medskip`** before first abstract paragraph — was creating unnecessary vertical gap after "Abstract" heading. (`main.tex:636`)
2. **Normalized em-dash spacing** in abstract: `---the Heisenberg algebra` → `--- the Heisenberg algebra` (matching body convention of spaced em-dashes). Two instances fixed. (`main.tex:654,683-684`)
3. Abstract otherwise clean: title formatting, MSC codes, keyword list all correct.

## Pages 2-44 (Table of Contents)

ToC is auto-generated. Issues found reflect section titles in source files:

1. **Chapter 15 "HH" short title fixed**: `\chapter[HH]{Chiral Hochschild cohomology...}` → `\chapter{Chiral Hochschild cohomology...}` — the abbreviated `[HH]` was producing "HH" in ToC and running headers, which is too terse for a monograph. Now displays the full chapter title. (`hochschild_cohomology.tex:5`)

## Page 45 (Chapter 1 opening)

1. **Normalized em-dash spacing** in opening list: ` --- Heisenberg...Yangians --- is` confirmed consistent with body convention. (`heisenberg_frame.tex:14-16`)
2. **Reduced `\bigskip` to `\medskip`** before "We begin with the Heisenberg algebra" — excessive vertical space between the itemized overview and the transition paragraph. (`heisenberg_frame.tex:88`)
3. **Removed unnecessary `\medskip`** before "Let $X$ be a smooth algebraic curve" — standard paragraph break suffices. (`heisenberg_frame.tex:93`)

## Pages 46-47 (§1.1 Bar complex at degree 1)

1. Content is clean — grading/desuspension accounting, Borcherds identity extraction, all precise.
2. Notation consistent: $d_{\mathrm{res}}$, $\bar{B}^{\mathrm{ch}}_n$, $\eta_{ij}$.
3. No fixes needed on these pages.

## Page 48 (General degree-1 element, start of §1.2)

1. **Replaced informal "Wait ---"**: `Wait --- this is not quite right.` → `This requires care.` — "Wait" is too conversational for Annals-grade. The pedagogical intent (showing a subtle error) is preserved. (`heisenberg_frame.tex:718`)
2. Cross-references and equation numbering consistent.
3. Section title "The bar complex at degree 2 — Arnold enters" — en-dash in PDF is correct (auto-converted from ` --- `).

## Pages 49-50 (Degree 2 computation, Arnold relation)

1. **Added missing period** after alternating sign sequence `$+1, -1, +1, -1, \ldots$` (end of paragraph before "For a general basis element"). (`heisenberg_frame.tex:877`)
2. Proposition 1.2.1 (Arnold relation) correctly formatted with `[proved here]`.
3. Remark 1.2.2 on Arnold as factorization coherence — clean.

## Pages 51-55 (Degree 3 computation, §1.3)

1. Content clean — the six boundary strata computed explicitly, Types I/II cancellation clear.
2. Boxed equations \eqref{eq:frame-dres-deg3-full} and \eqref{eq:frame-dsquared-deg3} for emphasis — appropriate for key results in introductory chapter.
3. **Replaced ALL-CAPS emphasis**: `IS the genus tower` → `\emph{is} the genus tower` — ALL-CAPS not appropriate for formal mathematical writing. (`heisenberg_frame.tex:1383`)

## Pages 56-57 (§1.4 Koszul dual, §1.5 Bar-cobar inversion)

1. Table comparing $\mathcal{H}_k$ and its Koszul dual — formatting clean, column alignment good.
2. Remark on "Three different dualities" — well-structured enumeration.
3. No fixes needed.

## Pages 58-60 (§1.6 Genus 1 curvature, §1.7 Holomorphic anomaly)

1. Elliptic propagator, Weierstrass zeta, $E_2$ anomaly — all formulas match Critical Pitfalls section.
2. Theorem formatting consistent (genus-1 partition function, genus-1 curvature).
3. No fixes needed.

## Pages 61-63 (§1.8 Coderived category, §1.9 Genus 2, §1.10 Genus tower)

1. Free energy table (Table 1.1) — formatting clean, decimal approximations helpful.
2. $\hat{A}$-genus derivation via Faber-Pandharipande and GRR — complete.
3. No fixes needed.

## Pages 64-73 (§1.11 Complementarity through §1.17 Synthesis)

1. **Fixed `$\mathcal{W}$-algebra` notation**: One instance of plain "W-algebras" in introduction.tex changed to `$\mathcal{W}$-algebras` for consistency with the frame chapter and introduction conventions. (`introduction.tex:346`)
2. Noted: 320 instances of plain "W-algebra" vs 140 of `$\mathcal{W}$-algebra` across document — larger consistency issue flagged for future pass.

## Cross-cutting: Non-breaking spaces before `\ref` (ALL PAGES)

**82 instances fixed** across 15 files. This is the single most impactful typographic fix — prevents line breaks between "Theorem" and its number throughout the entire document.

Files fixed:
- `algebraic_foundations.tex` (3)
- `bar_cobar_construction.tex` (13)
- `higher_genus.tex` (39)
- `chiral_koszul_pairs.tex` (7)
- `configuration_spaces.tex` (2)
- `feynman_diagrams.tex` (1)
- `free_fields.tex` (2)
- `heisenberg_eisenstein.tex` (1)
- `minimal_model_fusion.tex` (1)
- `w3_composite_fields.tex` (1)
- `deformation_quantization.tex` (1)
- `general_relations.tex` (1)
- `arnold_relations.tex` (2)
- `existence_criteria.tex` (1)
- `koszul_reference.tex` (7)

Pattern: `Theorem \ref` → `Theorem~\ref` (and similarly for Proposition, Lemma, Corollary, Definition, Remark, Example, Section, Chapter, Appendix).

---

## Summary of fixes (pages 1-73)

| Category | Count | Impact |
|----------|-------|--------|
| Non-breaking spaces before `\ref` | 82 | High — prevents all bad line breaks at cross-references |
| Chapter 15 ToC title | 1 | High — visible throughout document |
| Abstract formatting | 3 | Medium — first impression of the paper |
| Em-dash consistency | 2 | Medium — visual uniformity |
| Informal language | 1 | Medium — tone for Annals grade |
| Notation consistency | 1 | Low — $\mathcal{W}$ vs W |
| Vertical spacing | 3 | Low — page aesthetics |
| Missing punctuation | 1 | Low — completeness |
| ALL-CAPS emphasis | 1 | Low — tone |
| **Total** | **95** | |

---

## Session 2: Cross-Manuscript Mathematical Consistency (2026-03-12)

**Focus**: Stale claims, cross-chapter inconsistencies, notation uniformity.
**Method**: Systematic grep-and-verify across all chapters, not page-by-page.

### A. Stale MC2 References (MC2 fully resolved → Theorem)

| File | Line | Fix |
|------|------|-----|
| introduction.tex | 542 | `Conjecture~\ref{conj:master-theta}` → `Theorem~\ref{conj:master-theta} (originally MC2)` |
| introduction.tex | 707 | `resolving Conjecture~\ref{conj:universal-MC}` → `resolving Theorem~\ref{conj:universal-MC}` |
| higher_genus.tex | 10137 | Removed stale "resolving Conjecture~\ref{conj:master-theta}" |
| higher_genus.tex | 10326 | Updated to `This is Theorem~\ref{conj:master-theta} (MC2).` |
| higher_genus.tex | 11747 | Updated "three open MC2 hypotheses reduce to two" → both resolved |
| higher_genus.tex | 14155 | Added missing "[Resolved]" annotation to mc2-hyp:tautological |
| deformation_theory.tex | 1334 | "two MC2 hypotheses remain open" → all three resolved |
| concordance.tex | 38-43 | Updated opening to state MC2 is proved |
| concordance.tex | 557-560 | Split "Conjectures" range to separate Theorem from Conjectures |
| concordance.tex | 2598 | `resolving Conjecture` → `Theorem` |
| concordance.tex | 4042 | Removed "conjectural" describing Θ_A (now proved) |
| fourier_seed.tex | 679 | Updated to `(Theorem~\ref{conj:master-theta}).` |

### B. DK-2/3 Scope (now proved unconditionally for ALL simple types)

| File | Line | Fix |
|------|------|-----|
| yangians.tex | 4819-4833 | Rewrote DK-2/3 item: "type A proved / other types conjectural" → "All types proved" by two mechanisms (thick gen + sectorwise) |
| yangians.tex | 4846-4856 | Tightened summary: leads with unconditional all-types result |
| lattice_foundations.tex | 3656-3657 | Table: "Type A only" → "All types" for DK-2/DK-3 |

### C. E_n Koszul Duality (now proved → Theorem)

| File | Line | Fix |
|------|------|-----|
| concordance.tex | 1431-1432 | `Conjecture~\ref{conj:en-koszul}` → `Theorem~\ref{conj:en-koszul-duality}` |
| concordance.tex | 4097-4098 | Same update + noted as proved |
| concordance.tex | 4398-4399 | Same update |
| holomorphic_topological.tex | 1356 | ClaimStatusConjectured → ClaimStatusProvedElsewhere |
| holomorphic_topological.tex | 1390 | Added resolution note citing Theorem |

### D. Mathematical Exposition Improvements

| File | Line | Fix |
|------|------|-----|
| w_algebras_deep.tex | 228 | Filled missing formula: `m_0^{(G)} = 2k'/3` (was blank) |
| kontsevich_integral.tex | 272 | Added critical-level note: Sugawara undefined at k=-h^∨ |
| chiral_koszul_pairs.tex | 30-36 | Clarified why non-quadratic algebras can be chiral Koszul (PBW filtration) |
| deformation_theory.tex | 1318-1327 | Strengthened l_4^tr=0 proof: explicit transfer formula argument |
| beta_gamma.tex | 114-117 | Clarified two-generator duality (bc, not single free fermion) |
| yangians.tex | 1979-1980 | "Heisenberg self-duality" → correctly notes H is NOT self-dual |

### E. $\mathcal{W}$-algebra Notation Uniformity

Fixed plain "W-algebra" → `$\mathcal{W}$-algebra` in **34 theorem/definition/section headings** across:
- w_algebras_framework.tex (6 environments)
- kac_moody_framework.tex (2 environments + 1 section)
- bv_brst.tex (2 environments + 1 section)
- concordance.tex (1 environment)
- w_algebras_deep.tex (3 environments)
- free_fields.tex (7 environments)
- holomorphic_topological.tex (3 environments)
- hochschild_cohomology.tex (1 environment)
- koszul_pair_structure.tex (1 environment)
- chiral_koszul_pairs.tex (1 environment)
- chiral_modules.tex (1 environment)
- existence_criteria.tex (1 environment)

### F. Formula Verification (all correct)

Spot-checked 5 critical formula families across 40+ instances:
- ✓ Virasoro DS: c = 1 - 6(k+1)²/(k+2) — 7 instances
- ✓ W₃ DS: c = 2 - 24(k+2)²/(k+3) — 9 instances
- ✓ W₃ Λ = :TT: - (3/10)∂²T — 10+ instances (minus sign correct)
- ✓ Feigin-Frenkel: k ↔ -k-2h^∨ — 131 instances (2h^∨ correct)
- ✓ Sugawara: T = (1/2(k+h^∨))Σ:J^a J^a: — all correct + undefined at critical

### Session 2 Summary

| Category | Count |
|----------|-------|
| Stale MC2 references fixed | 12 |
| DK scope corrections | 3 |
| E_n theorem upgrades | 5 |
| Exposition improvements | 6 |
| W-algebra notation fixes | 34 |
| Formula verifications | 40+ |
| **Total mathematical fixes** | **60** |

Build: 1646pp, 0 undefined refs, 0 overfull boxes.

---

## Continuing from page 74...

