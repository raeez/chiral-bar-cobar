# Wave 10: Vol II Part I "Open Primitive" — Attack/Heal

**Date:** 2026-04-17
**Target:** `~/chiral-bar-cobar-vol2/` Part I (`main.tex` lines 1369-1416)
**Chapters scanned:** `foundations.tex` (3909), `locality.tex` (674), `axioms.tex` (1719), `equivalence.tex` (175), `bv-construction.tex` (309), `factorization_swiss_cheese.tex` (4128), `raviolo.tex` (737), `raviolo-restriction.tex` (512), `fm-calculus.tex` (1118), `orientations.tex` (428), `fm-proofs.tex` (557), `pva-descent-repaired.tex` (1730), `pva-expanded-repaired.tex` (377). Total ~16,393 lines.

**Skipped per directive:** `sc_chtop_heptagon.tex`, Vol II Part V, prior-wave targets, all thqg anchor chapters, `programme_climax_platonic.tex`, `logarithmic_wp_tempered_analysis_platonic.tex`, `universal_celestial_holography.tex`, `chiral_higher_deligne.tex`, `curved_dunn_higher_genus.tex`, `e_infinity_topologization.tex`, `unified_chiral_quantum_group.tex`.

## Phase 1 — Attack dimensions

### (i) CG deficiency opening

The Part I opener (`main.tex:1374-1401`) states the 3d HT primitive-datum question in
CG style: deficiency (pointwise Vol I insufficient for global HT), unique survivor
(open/closed factorization dg-category), forced machinery (SC dioperad with two
colours), and an instant-computation clause (PVA shadow from Arnold + Stokes).
`locality.tex:4-14` and `foundations.tex:43-53` likewise open with problem-first,
no result-listing. **VERDICT: PASS.**

### (ii) SC^{ch,top} as two-coloured dioperad (AP248)

`foundations.tex` §1 introduces SC^{ch,top} colloquially as "two-coloured
Swiss-cheese operad" (lines 55, 238, 242), then pins the technical axiomatic at
§1.2 (line 1969, "The two-coloured Swiss-cheese dioperad") with explicit
AP248-compliant remarks at lines 2106-2161 ("SCchtop is a dioperad, not an operad;
the bulk-boundary directionality") and at lines 2295-2320 citing Gan03 + Voronov
+ Merkulov-Vallette. `locality.tex:166-189` repeats the dioperad clause. Both
files also carry the Dunn-inapplicability clause (locality.tex:184-189,
foundations.tex:2144). **VERDICT: PASS** — the colloquial-to-technical transition
is explicit and AP248-disciplined.

### (iii) B(A) vs SC^{ch,top} (AP-SC-BAR)

`foundations.tex:2337-2365` carries an explicit remark "B̄(A) is not an
SCchtop-coalgebra" identifying B(A) as a single E_1-chiral coassociative
coalgebra over (ChirAss)^!, with the SCchtop structure placed on the derived
center pair (C^•_ch(A,A), A). `axioms.tex:1094-1103` repeats the guard for the
cogenerator coalgebra C_A. **VERDICT: PASS.**

### (iv) Dunn additivity scope

Three Dunn references; all correctly scoped. `locality.tex:184-189` denies Dunn
on SC^{ch,top}. `equivalence.tex:128-140` applies Dunn to the *topologized*
single-coloured operad E_2^hol ⊗ E_1^top ≃ E_3^top post-Sugawara (legitimate;
the directional restriction is lifted after topologization). `axioms.tex:1606`
cites "curved Dunn additivity" as the proved thm `curved-dunn-H2-vanishing-all-genera`.
**VERDICT: PASS.**

### (v) Topologization scope

`equivalence.tex:128-148` correctly states "proved chain-level for affine V_k(g) at
non-critical level", "class M chain-level in weight-completed category",
"general ... conjectural", and explicitly flags the present rectification as
*agnostic* to topologization. `foundations.tex:2310-2334` matches.
**VERDICT: PASS.**

### (vi) Slab bimodule vs SC disk (RS-9)

No conflations. The slab is never described as an SC disk. **VERDICT: PASS.**

### (vii) Physics-as-substance (RS-3)

`foundations.tex:39-64` treats 3d HT on C_z × R_t as the generating geometry;
bulk-boundary directionality is the physical constraint (not an analogy). The
Costello-Gwilliam factorization framing is the mathematical object, not scaffolding.
**VERDICT: PASS.**

## Phase 2 — Healings

Four surgical edits, all prose hygiene (HZ-10 em-dash enforcement) plus one
AI-slop substitution flagged by hook:

1. `locality.tex:172` — em-dash `---` → colon `:` in HT directionality aside.
2. `foundations.tex:2100-2101` — em-dash pair → parentheses in dioperad axiomatic.
3. `foundations.tex:2116` — em-dash pair → parentheses around
 "closed-to-open but not open-to-closed" aside.
4. `foundations.tex:391` — "A pivotal structure" → "A canonical iso V≃V**"
 (mathematical content preserved via direct description of the double-dual
 identification; hook flagged "pivotal" as slop; retained MTC technical content).
5. `factorization_swiss_cheese.tex:4037-4045` — em-dash pair bracketing
 multi-line pentagon-apparatus list → parenthetical with semicolon separators.

All em-dash pair replacements preserve semantic content. The 28 `---`
section-separator comments in `factorization_swiss_cheese.tex` are decorative
(invisible in PDF) and untouched.

## Constitutional hygiene

- **AP/HZ token grep in Part I prose:** zero hits (verified via `\b(AP\d+|HZ-\d+)\b`
 across 13 chapters, excluding `%` comments).
- **AI-slop token grep:** `moreover|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone` — zero hits.
- **Post-heal em-dash grep (prose):** zero remaining in Part I chapters
 (comment separators unchanged).

## Net diagnosis

Part I "Open Primitive" of Vol II is in CONSTITUTIONAL HEALTH on the seven audit
dimensions. Prior waves had already inscribed the AP-SC-BAR, AP-SC-NOT-SELFDUAL,
AP248 (dioperad), AP-TOPOLOGIZATION guard remarks into `foundations.tex` and
`locality.tex`; the present wave closed only prose-hygiene residue (four em-dash
sites, one AI-slop lemma). No structural violations surfaced. No theorem-status
revisions. No cross-volume propagation required.

## Not committed

Per directive: edits only, no git commit.
