# Wave 6 -- Index and Cross-Reference Audit

**Author:** adversarial referee, 2026-04-16
**Scope:** standalone/theorem_index.tex, standalone/notation_index.tex, chapters/theory/chiral_center_theorem.tex, chapters/theory/algebraic_foundations.tex, chapters/theory/coderived_models.tex, standalone/sc_chtop_pva_descent.tex, main.tex.
**Posture:** heal toward the strongest accurate claim; downgrade only when no upgrade path exists.

---

## Section 1. Theorem index audit

### 1.1 Headline summary inconsistencies (internal to theorem_index.tex)

The summary tables on standalone/theorem_index.tex L23-L51 do not match the entry rows below them. The "Total entries" line says 2262, but the sum of the part counts (Frame 19 + Theory 1125 + Examples 713 + Connections 405) is 2262 — consistent. However, the status table (L43-L51) is inconsistent with the actual row counts:

| Status | Summary table claim | Actual row count | Delta |
|---|---|---|---|
| ProvedHere | 1670 | 1671 | +1 |
| ProvedElsewhere | 328 | 329 | +1 |
| Conjectured | 257 | 258 | +1 |
| Conditional | 5 | 6 | +1 |
| Heuristic | 1 | 2 | +1 |
| Unknown | 1 | 4 | +3 |
| **Sum** | **2262** | **2270** | **+8** |

Status row count (2270) exceeds total-entries claim (2262) by 8. Either the rows include 8 detokenize artefacts that were not counted as entries, or 8 tags are double-counted. Either way the summary table is unreliable; an automated regenerator would have caught this.

### 1.2 Part labelling drift (CRITICAL)

The Part summary table (theorem_index.tex L36-L42) records:

```
Frame                     19
Part I: Theory          1125
Part II: Examples        713
Part III: Connections    405
```

But main.tex actually defines six parts (L899, L1088, L1182, L1390, L1511, L1544):

```
Part I  : The Bar Complex                         (label: part:bar-complex)
Part II : The Characteristic Datum                (label: part:characteristic-datum)
Part III: The Standard Landscape                  (label: part:standard-landscape)
Part IV : Physics Bridges                         (label: part:physics-bridges)
Part V  : The Seven Faces of the Collision Residue (label: part:seven-faces)
Part VI : The Frontier                            (label: part:v1-frontier)
```

The index aggregates by source directory (chapters/theory, chapters/examples, chapters/connections) and labels these aggregates as "Part I/II/III." This was true under an older 3-part architecture but is **wrong now**. Any reader who trusts the index and goes to "Part II" expecting a list of examples will instead find "The Characteristic Datum" — which spans theory chapters such as e1_modular_koszul, ordered_associative_chiral_kd, en_koszul_duality. The map between source directory and part is now many-to-many: chapters/theory feeds Parts I, II, IV, VI; chapters/examples feeds Part III; chapters/connections feeds Parts IV, V, VI.

This is V2-AP26 / AP-CY13 (cross-volume Part number staleness) firing inside Vol I's own metadata.

### 1.3 Line-number staleness (uniform)

The index is dated 2026-04-13. Spot checks against current chapter files (mtime 2026-04-16) show uniform line-number drift:

| Label | Index says | Actual line | Drift |
|---|---|---|---|
| thm:chiral-deligne-tamarkin | chiral_center_theorem.tex:1312 | :1422 | +110 |
| thm:hochschild-polynomial-growth | chiral_hochschild_koszul.tex:800 | :1042 | +242 |
| thm:main-koszul-hoch | chiral_hochschild_koszul.tex:691 | :929 | +238 |
| thm:e1-primacy | chapters/theory/introduction.tex:1303 | :1311 | +8 |
| thm:e1-chiral-koszul-duality | chiral_koszul_pairs.tex:5428 | :5643 | +215 |

Drifts of 200+ lines are likely caused by a single chapter expansion. Every line number in the index that points to a chapter file modified after 2026-04-13 should be treated as advisory only. The label resolves; the line does not.

### 1.4 Triage table for sample entries

| Label | Status in index | Status in source | Verdict |
|---|---|---|---|
| thm:chiral-deligne-tamarkin | ProvedHere | ProvedHere (chapter L1461) | ACCURATE on status; SCOPE-DRIFT on line |
| thm:hochschild-polynomial-growth | ProvedHere | ProvedHere (chapter L1041) | ACCURATE on status; SCOPE-DRIFT on line |
| thm:main-koszul-hoch | ProvedHere | not checked here, label resolves | ACCURATE on resolution; SCOPE-DRIFT on line |
| thm:bar-cobar-isomorphism-main | ProvedHere | resolves to chiral_koszul_pairs.tex:4071 (per index) | not re-verified; assume SCOPE-DRIFT on line |
| thm:bar-cobar-inversion-qi | ProvedHere | resolves to bar_cobar_adjunction_inversion.tex:1606 | not re-verified; SCOPE-DRIFT likely |
| thm:positselski-chiral-proved | ProvedHere | resolves | not re-verified |
| thm:e1-primacy | ProvedHere | ProvedHere | ACCURATE on status; SCOPE-DRIFT on line |
| thm:e1-chiral-koszul-duality | ProvedHere | resolves | ACCURATE on status; SCOPE-DRIFT on line |

No WRONG or MISSING entries surfaced in the spot-check sample, but the line drift means the index is currently a label resolver, not a navigator. The Audit-Notes block at L57-L62 documents 4 known issues (1 missing-tag entry, 4 duplicate labels) and these are ACCURATE.

### 1.5 Duplicate labels (acknowledged in audit notes, but worth re-flagging)

Index L60-L62 lists four duplicate labels:

- prop:fermion-complementarity (free_fields.tex L467 vs genus_expansions.tex L2454)
- prop:finite-jet-rigidity (concordance.tex L842 vs higher_genus_modular_koszul.tex L28581)
- prop:gaussian-collapse-abelian (concordance.tex L903 vs higher_genus_modular_koszul.tex L28640)
- prop:polynomial-level-dependence (concordance.tex L866 vs higher_genus_modular_koszul.tex L28604)

LaTeX will emit "Label `prop:foo' multiply defined" warnings for each. The pattern is consistent: each duplicate is between concordance.tex and higher_genus_modular_koszul.tex (3 of 4) — suggesting that concordance.tex copy-pasted blocks from higher_genus_modular_koszul (or vice versa) in violation of V2-AP27 ("duplicated mathematical content across files FORBIDDEN"). The free_fields/genus_expansions case is independent.

---

## Section 2. Notation index audit

### 2.1 Coverage

notation_index.tex declares 27 symbol entries plus 9 macros in the preamble. This is far below the actual notation footprint of Vol I (which routinely uses Theta_A, kappa, av, r(z), B^ord, B^Sigma, B^FG, etc., plus all the Hodge-class series). The standalone presents itself as an index "scoped to the notation introduced in main.tex and chapters/theory/" — but a reader trying to look up Sigma-vs-ord vs FG bar variants (V2-AP3, three bars), or hbar conventions, will not find them.

Scope is minimal but at least non-fraudulent: every entry checked resolves to a real definition.

### 2.2 kappa subscript convention

The notation index uses bare kappa(A), kappa(a,b) on L117, L141. AP113 (Vol III only, "kappa without subscripts FORBIDDEN") does not apply to Vol I — kappa here is the unique scalar modular characteristic, not the Vol III kappa-spectrum. The L141 entry explicitly notes: "the affine non-abelian Sugawara shift is handled later in the text." So bare kappa is intended in Vol I.

This is consistent with the Vol I convention: kappa(Heis_k) = k, kappa(Vir_c) = c/2, etc., and the symbol lives at the av-collapsed (centre-symmetric) level. Vol III's kappa-spectrum disambiguation does not apply backwards.

### 2.3 ChirHoch entry vs chapter usage

notation_index.tex L153-L155:

```
$\ChirHoch^*(\cA)$
& chiral Hochschild cohomology; in the introduction it is defined
  as the cohomology of coderivations of the bar coalgebra
& \path{chapters/theory/introduction.tex:694} \\
```

Chapter usage in chiral_center_theorem.tex defines ChirHoch via the chiral Hochschild cochain complex C^bullet_ch(A,A) (L33-L37) and the brace dg algebra (Thm 3.6 / brace-dg-algebra). Two routes converge to the same object: coderivations of the bar coalgebra (introduction L694) vs. cochain complex (chiral_center_theorem L33). The relation between the two is Theorem H + bar-cobar inversion. Both are used as "ChirHoch^*(A)" without disambiguation. This is not wrong (the two are quasi-isomorphic on the Koszul locus) but the notation index does not flag the dual realisation.

### 2.4 Z^der_ch notation index entry

notation_index.tex L157-L159 says:

```
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \operatorname{HH}^*(\cA,\cA)$
& derived chiral center; the bulk object computed by Hochschild cochains
& \path{main.tex:787}
```

But chapters/theory/chiral_center_theorem.tex L31-L33 defines Z^der_ch = C^bullet_ch(A,A), the Hochschild *cochain complex*, equipped with brace dg algebra structure. The notation index entry says HH^*(A,A) — i.e., already-cohomology. The chain-vs-cohomology distinction matters: the brace dg algebra structure lives at the chain level; HH^* is the cohomology. The index entry should read "HH-bullet" (chain) or note that the chain-level model is what carries the brace structure.

This is a chain/cohomology conflation (cache type "chain/cohomology", listed in CLAUDE.md). Heal: rewrite the index entry as

```
Z^der_ch(A) = (C^bullet_ch(A,A), brace dg algebra),
   with cohomology HH^*(A,A) = ChirHoch^*(A).
```

---

## Section 3. The chiral center theorem -- resolving the wave 4 contradiction

### 3.1 Wave 4 finding restated

Wave 4 flagged: chiral_center_theorem.tex L2025-L2041 says ChirHoch^*(Vir_c) "is concentrated in degrees {0,2}" with H^1=0; en_chiral_operadic_circle.tex Thm 3.6 + Prop 10.4 says ChirHoch^*(A) for A = Vir_c is "concentrated in {0,1,2}." These look contradictory.

### 3.2 Resolution: occupation vs amplitude (NEW PATTERN)

Both statements are correct under the right reading:

- **Amplitude bound** (the universal statement): for any modular Koszul algebra A, ChirHoch^n(A) = 0 for n outside {0,1,2}. This is Theorem H (chiral_hochschild_koszul.tex L1040 thm:hochschild-polynomial-growth, and en_chiral_operadic_circle.tex L996 thm:e-theorem-H). The cohomological amplitude is bounded by 2.

- **Occupation pattern** (algebra-dependent): for a specific A, the set {n : H^n(A) != 0} can be a strict subset of {0,1,2}. For Vir_c specifically, ChirHoch^1(Vir_c) = 0 (no first-order deformations of the chiral product as a Vir_c-action; only the central charge deformation in degree 2). For affine sl_2 at generic level, ChirHoch^1 = sl_2 (3-dimensional), so the occupation is the full {0,1,2}.

The wave 4 reading was: "{0,1,2}" from en_chiral_operadic_circle is an *amplitude bound* mistated as if it were the *occupation set* for Vir specifically. That is not quite the right diagnosis. The {0,1,2} statement in en_chiral_operadic_circle Theorem H (L1000) is universal — it applies to any Koszul chiral A, not specifically Vir. There is no claim "ChirHoch^*(Vir_c) is occupied in all of {0,1,2}." The Theorem H statement is consistent with the Vir occupation {0,2}: {0,2} is a subset of {0,1,2}.

The contradiction is therefore a misreading of Theorem H, not a defect in the manuscript. **But** the prose around Theorem H invites this misreading because the immediately following paragraphs (L1006-L1013) interpret the three nonvanishing degrees:

```
(i) ChirHoch^0(A) = Z(A): the naive centre.
(ii) ChirHoch^1(A): first-order deformations of A as a chiral algebra.
(iii) ChirHoch^2(A): obstructions to extending deformations.
```

This presents (i)-(iii) as if all three degrees are present for every A. They are not. For Vir, (ii) vanishes; for the Heisenberg, (i)-(iii) are each 1-dimensional; for affine sl_N, (ii) is dim(sl_N)-dimensional. The Theorem H prose should explicitly say: "the *amplitude* is bounded by {0,1,2}; occupation is algebra-dependent."

The Remark at en_chiral_operadic_circle L1016-L1026 (rem:e-amplitude) does exactly this for the broader confusion against virtual dimension and Gel'fand-Fuchs, but does NOT distinguish amplitude vs occupation within {0,1,2} itself. Add one sentence to that remark.

### 3.3 Cross-reference inside chiral_center_theorem.tex

Chapter L2103 says: "the chiral Hochschild cohomology of a modular Koszul algebra has polynomial Hilbert series and is concentrated in degrees {0, 1, 2}." This is the amplitude bound applied to Vir; the chapter then narrows to {0,2} for Vir specifically two paragraphs later (L2105-L2108). The chapter is internally correct. The standalone is internally correct. The contradiction was in the reader's combined parse, not in either source.

### 3.4 Healing actions (no manuscript edit; recommendations only)

1. en_chiral_operadic_circle.tex Thm 3.6 (L996, thm:e-theorem-H): in the universal-quantifier statement, amend "concentrated in cohomological degrees {0,1,2}" to "**bounded** in cohomological degrees {0,1,2} (cohomological amplitude)." Push the (i)-(iii) interpretation paragraph behind the words "Occupied degrees are algebra-dependent; when the corresponding group is non-zero, it has the following meaning."

2. Add to rem:e-amplitude (L1016) the sentence: "Within the amplitude {0,1,2}, the occupation set {n : ChirHoch^n(A) != 0} is algebra-dependent. For Vir_c, the occupation is {0,2}; for affine sl_2, the occupation is {0,1,2}; for Heisenberg, the occupation is {0,1,2}."

3. In chiral_center_theorem.tex L2025: replace "ChirHoch^n(Vir_c) = 0 for n > 2" with "By Theorem H (amplitude bound), ChirHoch^n(Vir_c) = 0 for n outside {0,1,2}; the Virasoro-specific occupation is {0,2}." This makes the universal-vs-specific distinction explicit at the use site.

This is not a downgrade; the strongest accurate statement is exactly amplitude-vs-occupation.

### 3.5 The {0,1,2} vs {0,2} pattern (cache write-back: NEW PATTERN)

Wave 4 noted the "occupation vs amplitude" pattern. This audit confirms it is a generic confusion site whenever a universal cohomological-bound theorem is followed by a specific-algebra computation:

| Universal (amplitude) | Specific algebra (occupation) | File |
|---|---|---|
| {0,1,2} for any Koszul chiral A | {0,2} for Vir_c | chiral_center_theorem.tex L2103 vs L2107 |
| {0,1,2} for any Koszul chiral A | {0,1,2} for affine sl_2 (occupation full) | chiral_center_theorem.tex L1996-L2007 |
| {0,1,2} for any Koszul chiral A | {0,1,2} for Heisenberg | chiral_center_theorem.tex L1976-L1994 |

This is exactly two appearances of the pattern with both readings co-existing. Recording for cross-volume cache: the **amplitude vs occupation** confusion type is distinct from chain-vs-cohomology (which is the dimensional difference within a fixed degree) and from specific-vs-general (which is about scope of formulae). It is a *set-theoretic* confusion: bounded-set vs nonempty-set within the bound.

---

## Section 4. Standalone-vs-chapter consistency

### 4.1 chiral_center_theorem chapter vs en_chiral_operadic_circle standalone

The chapter (chiral_center_theorem.tex) and the standalone (en_chiral_operadic_circle.tex) cover overlapping material:

| Object | Chapter (line) | Standalone (line) | Status |
|---|---|---|---|
| Brace dg algebra theorem | thm:brace-dg-algebra (L717), ProvedHere | thm:brace-dg-algebra-standalone? not located | UNPAIRED |
| Chiral Deligne-Tamarkin | thm:chiral-deligne-tamarkin (L1421), ProvedHere | thm:e-deligne-tamarkin-chiral? not located | UNPAIRED |
| Theorem H | thm:hochschild-polynomial-growth in chiral_hochschild_koszul.tex L1042 (ProvedHere) | thm:e-theorem-H L996 (no explicit ClaimStatus tag) | STATUS DRIFT (chapter ProvedHere; standalone untagged) |
| Vir ChirHoch | prop:derived-center-explicit L1965 (chapter), ProvedHere | prop:e-vir-complete L3033 (standalone) | DUPLICATE COMPUTATION |

The standalone en_chiral_operadic_circle.tex has its own labels (thm:e-theorem-H, prop:e-vir-complete, etc.) parallel to chapter labels (thm:hochschild-polynomial-growth, prop:derived-center-explicit). It is a *self-contained* preprint that re-proves results also stated in the integrated manuscript. This is intentional but creates a fork: edits to one are not propagated to the other automatically.

V2-AP27 ("duplicated mathematical content across files FORBIDDEN") would say to use \input or \ref. The standalone-as-preprint defense is reasonable, but the standalone should at minimum carry an opening header pointing readers to the canonical integrated location of each claim. None of the standalone theorems carry a \ClaimStatusProvedElsewhere{thm:hochschild-polynomial-growth in chapters/theory/chiral_hochschild_koszul.tex} marker.

### 4.2 sc_chtop_pva_descent standalone

This is a self-contained article with its own preamble (\title, \author, \maketitle, \tableofcontents). It is **not** included by main.tex (verified: grep returns no \input{sc_chtop_pva_descent}). So this is purely a preprint. V2-AP32 ("standalone-document artifact leak") does not fire because the file is not \input by main.tex.

The standalone proves:
- thm:scchtop-koszulity (L531, ProvedHere) — homotopy-Koszulity of SC^{ch,top}
- thm:scchtop-koszul-dual (L608, ProvedHere) — Koszul dual is (Lie^c, Ass^c)
- thm:pva-descent (L906, ProvedHere) — PVA descent
- prop:resolvent-principle (L1123, ProvedHere)
- 3 worked-example propositions (Heis L1201, KM L1287, W_3 L1385)

These do not appear in theorem_index.tex (the index scans chapters/**, not standalone/**). So the index is missing this body of theorems entirely. A reader using theorem_index.tex as a navigator will not find any SC^{ch,top}-Koszulity or PVA-descent results.

### 4.3 V2-AP21 compliance check (PVA != P_inf-chiral)

V2-AP21 says: PVA = classical shadow (descend to cohomology); P_inf = homotopy intermediate. The standalone (sc_chtop_pva_descent.tex) defines \Pinf in the macro block (L79) but does not appear to use it in the body (grep returns only the macro definition). The body uses "PVA" exclusively, in correct sense (descent on cohomology). The opening abstract L156 says: "operations $m_k$ descend to a commutative product and a $\lambda$-bracket." This is the descent direction: m_k chain-level → PVA cohomology.

V2-AP22 hierarchy: Comm assoc < PVA < E_inf-chiral < P_inf-chiral < E_1-chiral. The standalone's "PVA descent" is the rightmost-to-leftmost arrow in this hierarchy via cohomology truncation. Correct.

No V2-AP21 violation.

### 4.4 chiral_center_theorem chapter status discrepancies

All theorem-environment occurrences in chiral_center_theorem.tex carry ProvedHere or ProvedElsewhere tags. No bare theorems detected.

---

## Section 5. Cross-reference breakage report

### 5.1 Missing or mistyped labels in the index

- thm:hochschild-polynomial-growth: indexed at line 800 of chiral_hochschild_koszul.tex; actual label at line 1042. Index will resolve via label, but the line is misleading. Drift = 242 lines.
- thm:main-koszul-hoch: indexed at line 691; actual at line 929. Drift = 238 lines.
- thm:chiral-deligne-tamarkin: indexed at line 1312; actual at line 1422. Drift = 110 lines.
- thm:e1-chiral-koszul-duality: indexed at line 5428; actual at line 5643. Drift = 215 lines.
- thm:e1-primacy: indexed at line 1303; actual at line 1311. Drift = 8 lines.

Pattern: chapters that were edited 2026-04-14 through 2026-04-16 have line drifts of 100-240 lines. Index dated 2026-04-13. Regenerate the index whenever any indexed chapter is touched.

### 5.2 Standalone files not indexed

- standalone/en_chiral_operadic_circle.tex (~3000+ lines, ~30 theorem environments) — no entries in theorem_index.tex
- standalone/sc_chtop_pva_descent.tex (1594 lines, ~10 theorem environments) — no entries
- standalone/cy_to_chiral_functor.tex — no entries
- standalone/drinfeld_kohno_bridge.tex — no entries
- All other standalone preprints — no entries

The index scope is "chapters/**/*.tex" only. This is consistent with the index's stated scope ("auto-generated from chapters/**/*.tex"), but means readers searching for SC^{ch,top}-Koszulity, PVA descent, the Vir derived centre, the chiral Deligne-Tamarkin standalone formulation, etc., will not find them. Mention this scope limitation prominently in the index header (currently buried at L20).

### 5.3 Index Part-aggregation maps to source directory, not Part labels

Already covered in Sec 1.2. The "Part I/II/III" labels in the summary table are aliases for "chapters/theory / chapters/examples / chapters/connections" directories. They do not correspond to the six \part{} declarations in main.tex. Either rename to "Theory chapters / Example chapters / Connections chapters" (honest), or regenerate the index with proper part-label awareness using main.tex's \part{} declarations as the ground truth.

### 5.4 Notation index missing key symbols

Glossary inadequacies in notation_index.tex:

- No entry for B^Sigma_X(A) (only B_X = symmetric and B^ord). The three-bar distinction (V2-AP3) is invisible.
- No entry for B^FG (zeroth-pole bar, V2-AP3).
- No entry for av (the averaging map mentioned at L133).
- No entry for the shadow tower S_k.
- No entry for the discriminant Delta (only "Delta = 8 kappa S_4" without standalone Delta entry).
- No entry for hbar — and Vol I has multiple hbar conventions floating around (cf. AP151 in CLAUDE.md). A central hbar entry would be load-bearing.

Recommend extending the notation index to ~50-60 entries to match the actual symbol footprint.

---

## Section 6. First-principles analyses

### 6.1 Why the index has stale Part labels

The index is auto-generated from chapters/**/*.tex by a scraper. Its output was correct under a 3-part architecture (Theory / Examples / Connections). When main.tex was restructured to a 6-part layout (Bar Complex / Characteristic Datum / Standard Landscape / Physics Bridges / Seven Faces / Frontier), the scraper was not updated. The scraper still computes part counts by file directory, which has stayed (chapters/theory, chapters/examples, chapters/connections), but the part *labels* (Part I "Theory", Part II "Examples", Part III "Connections") are now misnomers because main.tex's actual Part I is "The Bar Complex," etc.

**Ghost theorem:** The "directory == part" identification was true under the old architecture. The mathematical content of the index — labels, statuses, line numbers — is correct relative to chapters/**. The defect is in the **interpretation** layer that maps directories to part names.

**Heal:** the scraper should read main.tex \part{...} \label{...} declarations and assign each chapter to a part by its position in the input order. A correct mapping is:

| File directory | Old label | Actual part assignments (main.tex) |
|---|---|---|
| chapters/theory/* | Part I: Theory | Spread across Parts I, II, IV, VI |
| chapters/examples/* | Part II: Examples | All in Part III: The Standard Landscape |
| chapters/connections/* | Part III: Connections | Spread across Parts IV, V, VI |

### 6.2 Why the wave 4 ChirHoch contradiction looked like a contradiction

The {0,1,2} amplitude bound and the {0,2} Vir occupation were both stated as "concentrated in" without distinguishing the universal claim from the specific computation. A reader sliding from one to the other reads a contradiction. The defect is in the prose, not the math: the universal Theorem H is correct, the specific Vir computation is correct, and they are consistent (one is a subset bound, the other is a specific subset).

**Ghost theorem:** Both readings of "concentrated in S" — (a) H^n = 0 for n outside S, (b) H^n != 0 for all n in S — are common in the literature. (a) is the amplitude reading; (b) is the occupation reading. They coincide when the cohomology is "generic" but diverge for specific algebras.

**Heal:** standardise on (a) for universal statements ("amplitude bounded by S = {0,1,2}") and reserve "concentrated in S" for (b) (occupation, specific computation). This is a pure prose discipline.

### 6.3 Why the index status counts disagree by 8

The summary status table (L43-L51) totals 2262, but row scrape counts 2270. A delta of 8 is small enough that it could be the audit-notes block (1 missing tag, 4 duplicate-label entries, plus possibly the 4 Unknown rows where the summary said 1). The summary table appears to have been hand-edited or generated by a different scraper pass than the row table. Auto-regenerate to remove the discrepancy.

---

## Section 7. Three upgrade paths

### 7.1 Theorem index regeneration (LOW EFFORT, HIGH PAYOFF)

Run a fresh index regeneration with these requirements:
1. Scan chapters/** AND standalone/** (currently only chapters/**).
2. Read main.tex \part{...} \label{...} declarations to assign each chapter to its current part.
3. Cross-check status tags: every theorem must have an explicit ClaimStatus*, no "Unknown" tolerated.
4. Auto-regenerate on every commit that touches an indexed file (pre-commit hook).
5. Emit warnings for: duplicate labels, status drift across standalone-vs-chapter, line drift since last regen.

This is purely tooling, no manuscript change required.

### 7.2 Notation index expansion (MEDIUM EFFORT, MEDIUM PAYOFF)

Extend notation_index.tex to ~60 entries covering: three-bar variants (V2-AP3), shadow tower symbols, hbar conventions (with explicit AP151 cross-reference), av, kappa-sites, Delta. Group by section (Bar variants / Shadow tower / Modular data / Convolution algebra). Cross-reference each entry to its first formal definition. Estimated 3-4 hours of work.

### 7.3 Standalone-vs-chapter ProvedElsewhere harmonization (LOW EFFORT, HIGH RIGOR)

Every theorem in standalone/en_chiral_operadic_circle.tex that re-proves a chapter result should carry \ClaimStatusProvedElsewhere{} pointing to the chapter label. This is the canonical V2-AP-style discipline for cross-source consistency. Estimated 1 hour.

The strengthened version: add a header table to each standalone preprint mapping its theorem labels to the corresponding chapter labels:

```
| Standalone label             | Chapter label                        |
|------------------------------|--------------------------------------|
| thm:e-theorem-H              | thm:hochschild-polynomial-growth     |
| prop:e-vir-complete          | prop:derived-center-explicit (Part iii) |
```

Then any future edit to either side is at minimum locatable.

---

## Section 8. Punch list

In priority order:

### CRITICAL
1. theorem_index.tex Part labels are stale (3-part old architecture). Regenerate against main.tex's 6-part structure.
2. Status counts in summary table (1670/328/257/5/1/1) disagree with actual row counts (1671/329/258/6/2/4) by 8 entries total. Auto-regenerate to resolve.
3. theorem_index.tex line numbers drifted by 100-240 lines for chapters edited after 2026-04-13. Regenerate.

### HIGH
4. Theorem H universal statement (en_chiral_operadic_circle.tex L996-L1013, chiral_hochschild_koszul.tex L1040-L1090) should explicitly distinguish "amplitude bounded by {0,1,2}" from "occupation is the full {0,1,2}" to prevent the wave 4 misreading.
5. notation_index.tex Z^der_ch entry says HH^*(A,A) (cohomology) but chapter defines it as C^bullet_ch (chain). Fix to chain-with-derived-cohomology.
6. Add amplitude-vs-occupation sentence to rem:e-amplitude (en_chiral_operadic_circle.tex L1016) listing Vir occupation = {0,2}, sl_2 = {0,1,2}, Heis = {0,1,2}.
7. Standalone preprints (en_chiral_operadic_circle, sc_chtop_pva_descent, etc.) should carry \ClaimStatusProvedElsewhere markers for theorems that duplicate chapter results.

### MEDIUM
8. Notation index is too small (27 entries). Expand to ~60 covering three-bar variants, hbar, av, shadow tower, etc.
9. Index is missing all standalone/* theorems. Either widen scraper scope or document the limitation in the index header.
10. Four duplicate labels in index (audit notes L60-L62) need de-duplication: prop:fermion-complementarity, prop:finite-jet-rigidity, prop:gaussian-collapse-abelian, prop:polynomial-level-dependence.

### LOW
11. notation_index.tex L141 entry for kappa(A) notes "the affine non-abelian Sugawara shift is handled later in the text" — this could be promoted to a formal cross-reference \S\ref{...} rather than prose.
12. Add bridging remark in notation_index.tex documenting the chain-vs-cohomology relationship of Z^der_ch and ChirHoch.

### FOR THE CACHE WRITE-BACK
13. **NEW PATTERN: "amplitude-vs-occupation conflation."** Universal cohomological-bound theorems ("H^n = 0 for n outside S") are routinely confused with specific-algebra occupation claims ("H^n != 0 for all n in S"). Two appearances in this audit (Vir vs Theorem H, sl_2 vs Theorem H), confirming wave 4's instinct that this is a generic pattern, not a one-off. Cache as cross-volume confusion type "set-theoretic / amplitude-vs-occupation."

Counter-template: every universal cohomological concentration theorem should state "**amplitude** {bounded by} S" rather than "concentrated in S," and reserve "occupation" wording for specific-algebra computations. Where the index uses {0,1,2}, cross-check against the universal Theorem H proof and the specific-algebra examples in the same section.

---

## Appendix A. Files inspected (absolute paths)

- /Users/raeez/chiral-bar-cobar/standalone/theorem_index.tex
- /Users/raeez/chiral-bar-cobar/standalone/notation_index.tex
- /Users/raeez/chiral-bar-cobar/standalone/en_chiral_operadic_circle.tex
- /Users/raeez/chiral-bar-cobar/standalone/sc_chtop_pva_descent.tex
- /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex
- /Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex
- /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex
- /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex
- /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
- /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
- /Users/raeez/chiral-bar-cobar/main.tex

## Appendix B. Methodology

Read/Grep/Glob/Bash only. No edits to manuscript. No commits. Spot-checked status tags and line numbers; full audit would require re-running the index scraper. Identified contradictions by cross-querying labels between standalone preprints and chapter source.
