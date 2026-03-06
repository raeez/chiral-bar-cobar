# CG Restructuring Log

## Overview
Chriss-Ginzburg restructuring: Example-first architecture with the Heisenberg algebra as frame example.

## Phase 0: Architectural Design (COMPLETED, prior session)
- Created `notes/CG_RESTRUCTURING_PLAN.md` with 5-phase plan

## Phase 1: Write Heisenberg Frame Chapter (COMPLETED)
- **Created**: `chapters/frame/heisenberg_frame.tex` (~1200 lines, 16 sections)
- CG-style: computation first, definitions after
- Cold open with OPE, bar complex built by hand, Arnold relation demonstrated
- Koszul dual read off, genus-1 curvature, genus tower, A-hat genus
- Previews: sl2, Yangians, modular programme
- All cross-references verified against manuscript label conventions

## Phase 2: Update main.tex (COMPLETED)
- **Part 0** added: `\part{The Heisenberg algebra}` with preamble (lines 623-635)
- **Part I** preamble: back-references frame chapter (lines 652-666)
- **Part II** preamble: rewritten to reference frame chapter and discriminant structure (lines 767-792)
- **Part III** preamble: rewritten with BV=bar, Kontsevich, Costello-Li connections (lines 918-943)
- Frame chapter included via `\include{chapters/frame/heisenberg_frame}`

## Phase 3: Shorten introduction.tex (COMPLETED)
- **Before**: ~1569 lines
- **After**: 1230 lines (reduction: 339 lines, ~22%)

### Removed (redundant with frame chapter or Part I chapters):
| Section | Lines | Reason |
|---------|-------|--------|
| Geometric bar construction theorem | ~35 | Now in Chapter bar_cobar |
| Verdier duality remark (rem:NAP-foundation) | ~20 | Now in bar_cobar |
| Geometric cobar construction theorem | ~25 | Now in bar_cobar |
| Full genus bar complex theorem | ~30 | Now in higher_genus |
| maintheorem bar-cobar-complete + proof | ~50 | Redundant with Part I |
| maintheorem curved-complete + proof | ~30 | Redundant with Part I |
| Strict nilpotence subsection | ~45 | Now in frame ch §3 + bar_cobar |
| maintheorem NAP-complete + proof | ~20 | Redundant with Part I |
| Explicit Koszul pairs corollary | ~15 | Summary paragraph replaces |
| Hochschild computation corollary | ~10 | Summary paragraph replaces |
| Arnold relations section (§8) | ~22 | Fully in frame ch §3 |
| Wider landscape subsection | ~50 | Covered by frame ch §14-16 |
| How structures correspond subsection | ~17 | Covered by frame ch + bar_cobar |
| Computations section (verbose) | ~50 | Compressed to 15 lines |

### Kept (essential, not in frame chapter):
- §1 The problem (lines 3-72)
- §2 Three theorems (lines 74-127)
- §3 Central thesis + four irreducible pieces (lines 129-274)
- §4 Relationship to foundational work (lines 276-337)
- §5 Dictionary: E∞/E₁/P∞ definitions (lines 340-705) — externally referenced
- §7 Central charge complementarity theorem (23 external refs)
- §9 Chiral Hochschild cohomology (not in frame chapter)
- §10 Criteria for existence of Koszul duals (not in frame chapter)
- §11 Computations (compressed)
- §12 Standing assumptions and conventions

### New forward references added:
- §6 opening paragraph → Chapter frame, Chapters bar_cobar--higher_genus
- §7 opening paragraph → sec:central-thesis, Chapter frame
- §11 → Chapter frame, Part II, Master Table

## Phase 4: Update Chapter Openings (COMPLETED)
24 chapter files now back-reference the frame chapter:

### Theory chapters (9 files):
- algebraic_foundations.tex, configuration_spaces.tex, bar_cobar_construction.tex
- higher_genus.tex, chiral_koszul_pairs.tex, deformation_theory.tex
- poincare_duality.tex, poincare_duality_quantum.tex, chiral_modules.tex

### Example chapters (8 files):
- free_fields.tex, kac_moody_framework.tex, w_algebras_framework.tex
- genus_expansions.tex, yangians.tex, lattice_foundations.tex
- detailed_computations.tex, examples_summary.tex

### Connection chapters (5 files):
- feynman_diagrams.tex, bv_brst.tex, concordance.tex
- holomorphic_topological.tex, physical_origins.tex

### Additional (2 files):
- beta_gamma.tex, deformation_quantization.tex

## Phase 5: Verification (COMPLETED)
- **Compilation**: Zero LaTeX errors, PDF produced (1340 pages)
- **Census**: PH 697, PE 332, CJ 115, HE 19 (total 1163)
  - PH -1, PE -2 vs prior: all removed claims are redundant restatements
  - No actual proofs removed; all live in their canonical chapters
- **Undefined refs**: Only pre-existing appendix forward refs (need 3+ passes)
- **No new undefined refs** introduced by restructuring

## Files Modified
| File | Change |
|------|--------|
| chapters/frame/heisenberg_frame.tex | CREATED (frame chapter) |
| main.tex | Part 0 + preamble updates |
| chapters/theory/introduction.tex | Shortened 1569→1230 lines |
| 24 chapter .tex files | Back-reference paragraphs added |

## Census Delta
| Status | Before | After | Delta | Notes |
|--------|--------|-------|-------|-------|
| ProvedHere | 698 | 697 | -1 | Redundant maintheorem restatements |
| ProvedElsewhere | 334 | 332 | -2 | Redundant theorem restatements |
| Conjectured | 115 | 115 | 0 | |
| Heuristic | 19 | 19 | 0 | |
| **Total** | **1166** | **1163** | **-3** | All removals are redundant |
