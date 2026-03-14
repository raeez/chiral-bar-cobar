# FRONTIER CARTOGRAPHY — Complete Catalogue
# Date: 2026-03-14
# Commit: 8e5ccd7 (main)
# Session: v33
# Volumes: Vol I (1803pp, 1595 claims, 6005 tests) + Vol II (173pp, 133 tests)

---

## Summary Table

| Gap Type | Code | Total | CRITICAL | HIGH | MEDIUM | LOW |
|----------|------|-------|----------|------|--------|-----|
| Untagged | G1 | 0 | 0 | 0 | 0 | 0 |
| Misstatus | G2 | 25 | 0 | 1 | 10 | 14 |
| Stale-Status | G3 | 0 | 0 | 0 | 0 | 0 |
| Prefix-Mismatch | G4 | 8 | 0 | 0 | 6 | 2 |
| Unlabeled | G5 | 12 | 0 | 0 | 12 | 0 |
| Display-Mismatch | G6 | 16 | 0 | 1 | 1 | 14 |
| Stale-Concordance | G7 | 3 | 0 | 0 | 2 | 1 |
| Missing-Concordance | G8 | 0 | 0 | 0 | 0 | 0 |
| Unpropagated | G9 | 0 | 0 | 0 | 0 | 0 |
| Phantom-Ref | G10 | 0 | 0 | 0 | 0 | 0 |
| Prose-Claim | G11 | 16 | 0 | 0 | 5 | 11 |
| Cross-Volume | G12 | 4 | 0 | 0 | 2 | 2 |
| **TOTAL** | | **84** | **0** | **2** | **38** | **44** |

**Headline**: Zero CRITICAL findings. The mathematical core (Theorems A-D, H, MC1-MC5, DK ladder) is correctly tracked at all five control-plane layers. All 1,494 theorem-class environments have ClaimStatus tags. Zero phantom references, zero undefined citations, zero multiply-defined labels. The 84 findings are control-plane hygiene issues, not mathematical errors.

---

## G1 (UNTAGGED): 0 findings

All 1,494 theorem-class environments across 70 .tex files have ClaimStatus annotations within 5 lines. Full coverage confirmed by both agent scan and direct script.

---

## G2 (MISSTATUS): 25 findings

### HIGH (1)

#### G2-H1. `thm:bg-bar-coalg` — theorem env with Heuristic status
**File**: `poincare_duality_quantum.tex:440`
**Current**: `\begin{theorem}` with `\ClaimStatusHeuristic`
**Actual**: A theorem environment cannot have Heuristic status — these are contradictory. The content is a precise mathematical claim about the beta-gamma bar complex coalgebra structure with a sketch proof.
**Resolution**: Either upgrade proof to complete (→ ProvedHere) or change environment to `\begin{conjecture}` with `conj:bg-bar-coalg` label.

### MEDIUM (10)

#### G2-M1. `thm:deformation-obstruction` — ProvedHere but proof is an outline
**File**: `bar_cobar_construction.tex:4488`
**Current**: `\ClaimStatusProvedHere`
**Actual**: Proof at line 4504 explicitly labeled "Proof (outline; full proof in §ref)". Defers to `thm:quantum-complementarity-main`.
**Resolution**: Change to `\ClaimStatusProvedElsewhere` citing the complementarity theorem.

#### G2-M2. `thm:modular-vs-quasi` — ProvedHere but proof is a heuristic
**File**: `higher_genus.tex:2811`
**Current**: `\ClaimStatusProvedHere`
**Actual**: "Proof" titled "Origin of the anomaly" gives a heuristic about Eisenstein regularization, not a derivation. The modular/quasi-modular transformation laws are classical (Serre, Zagier).
**Resolution**: Change to `\ClaimStatusProvedElsewhere` with citation.

#### G2-M3. `thm:geometric-com-lie-enhancement` — ProvedHere but proof is a sketch
**File**: `higher_genus.tex:998`
**Current**: `\ClaimStatusProvedHere`
**Actual**: 8-line "proof" asserts correspondences without verification.
**Resolution**: Complete the proof or downgrade status.

#### G2-M4. `thm:ainfty-com-lie-interchange` — ProvedHere but proof is schematic
**File**: `higher_genus.tex:1035`
**Current**: `\ClaimStatusProvedHere`
**Actual**: Single-sentence proof sketch.
**Resolution**: Complete the proof or downgrade status.

#### G2-M5. `thm:elliptic-compactification` — ProvedHere but proof incomplete
**File**: `configuration_spaces.tex:1488`
**Current**: `\ClaimStatusProvedHere`
**Actual**: "Proof" labeled "[Construction]" — introduces coordinates but does not verify claimed properties (2) and (3).
**Resolution**: Complete the proof or downgrade status.

#### G2-M6. `thm:period-integrals-bar` — ProvedElsewhere but decomposition may be original
**File**: `configuration_spaces.tex:1555`
**Current**: `\ClaimStatusProvedElsewhere` citing BD04
**Actual**: The three-part decomposition appears to be a reformulation original to this monograph; proof labeled "[Sketch]".
**Resolution**: Cite precise BD04 theorem or change to ProvedHere with complete proof.

#### G2-M7. `thm:completion-necessity` — ProvedHere but proof covers only 1 of 3 conditions
**File**: `bar_cobar_construction.tex:4940`
**Current**: `\ClaimStatusProvedHere`
**Actual**: "Proof by Example: Virasoro" covers only condition (1).
**Resolution**: Downgrade to example/remark or prove all three conditions.

#### G2-M8. `prop:classification-table` — ProvedElsewhere but contains original content
**File**: `existence_criteria.tex:475`
**Current**: `\ClaimStatusProvedElsewhere` citing FBZ04, BD04
**Actual**: Table includes "W_infty: NO" and "W_N: Sometimes" which are assessments from this monograph.
**Resolution**: Change status to mixed or split into PE and PH parts.

#### G2-M9. Yangian prose: "conjectured to be self-dual (Theorem~\ref{...})"
**File**: `yangians.tex:3966`
**Current**: Prose says "conjectured" while citing a proved theorem
**Actual**: The R-matrix inversion is proved; the spectral-shift self-duality claim is a separate assertion. Contradictory wording.
**Resolution**: Distinguish what is proved (R-matrix inversion) from what is speculated (spectral-shift self-duality).

#### G2-M10. 6 Heuristic items listed as "Conjecture" in concordance index
**File**: `concordance.tex:5935-6047` (index) vs various source files
**Current**: Concordance open conjectures index says "Conjecture~\ref{conj:...}" for 6 items
**Actual**: All 6 have `\ClaimStatusHeuristic` in source, not Conjectured:
- `conj:anomaly-cancellation` (bar_cobar_construction.tex:4362)
- `conj:brst-cohomology` (bar_cobar_construction.tex:4295)
- `conj:cobar-physical` (bar_cobar_construction.tex:2905)
- `conj:bv-equals-bar-cobar` (bv_brst.tex:1633)
- `conj:quantum-master-complete` (bv_brst.tex:1615)
- `conj:bphz-recursion` (feynman_diagrams.tex:1071)
**Resolution**: Either upgrade source to Conjectured, or add a Heuristic sub-section to the concordance index.

### LOW (14)

#### G2-L1 through G2-L9. Definitions with ClaimStatus tags (9 instances)
Definitions are stipulative and should not carry ClaimStatus. Found in:
- `higher_genus.tex:195` — `def:scalar-curvature-shadow` (ProvedHere on definition)
- `bar_cobar_construction.tex:5864` — `def:winfty-principal-stage-compatible` (Conjectured on definition)
- `bar_cobar_construction.tex:5886` — `def:winfty-quotient-system` (Conjectured on definition)
- `bar_cobar_construction.tex:8010` — `def:winfty-stage4-ward-normalized` (Conjectured on definition)
- `yangians.tex:8192` — `def:ordered-e1-factorization` (Conjectured on definition)
- `yangians.tex:8206` — `def:spectral-quantum-group` (Conjectured on definition)
- `yangians.tex:8218` — `def:dg-shifted-yangian` (Conjectured on definition)
- `yangians.tex:8230` — `def:rtt-adapted-filtration` (Conjectured on definition)
- `coderived_models.tex:317` — `def:completed-chiral-ambient` (Conjectured on definition)
**Resolution**: Remove ClaimStatus from definitions; if existence is conjectural, add a separate conjecture.

#### G2-L10. `coderived_models.tex:85` — ProvedElsewhere on a definition
#### G2-L11. `existence_criteria.tex:689` — ProvedElsewhere on a remark
#### G2-L12. `nilpotent_completion.tex:133` — ProvedHere with acknowledged proof gap (rem at line 172)
#### G2-L13. Inline ClaimStatusConjectured in remark prose (yangians.tex:694, 813)
#### G2-L14. `poincare_duality_quantum.tex:240` — remark calls a conjecture "This theorem"

---

## G3 (STALE-STATUS): 0 findings

All recently changed claims have current ClaimStatus tags. No evidence of outdated tags from prior sessions.

---

## G4 (PREFIX-MISMATCH): 8 findings

### MEDIUM (6)

#### G4-M1. `thm:betagamma-bc-koszul-detailed` on `\begin{proposition}`
**File**: `beta_gamma.tex:337`
**Resolution**: Rename to `prop:betagamma-bc-koszul-detailed`, update 2 refs.
**Propagation**: beta_gamma.tex:940, kac_moody_framework.tex:426

#### G4-M2 through G4-M5. Orphaned backward-compatible `rem:` labels on lemma/proposition envs (4)
- `rem:bar-deg2-symmetric-square` on lemma (examples_summary.tex:1856) — 0 refs, safe to delete
- `rem:bar-dims-partitions` on lemma (free_fields.tex:3733) — 0 refs, safe to delete
- `rem:bar-dims-level-independent` on lemma (kac_moody_framework.tex:499) — 0 refs, safe to delete
- `rem:ext-koszul-dual-level` on proposition (chiral_modules.tex:3026) — 0 refs, safe to delete

#### G4-M6. Orphaned `prop:pbw-universal-conformal` on `\begin{theorem}`
**File**: `higher_genus.tex:10267` — 0 refs, safe to delete

### LOW (2)

#### G4-L1 and G4-L2. `thm:bar-differential` and `thm:bar-differential-structure` on `\begin{definition}`
**File**: `bar_cobar_construction.tex:339`
**Note**: 14 refs across 10 files all say "Theorem~\ref{...}". See G6 findings below.
**Resolution**: Either promote env to `\begin{theorem}` (recommended — content is assertive) or migrate all refs to `def:bar-differential-complete`.

---

## G5 (UNLABELED): 12 findings — all conjectures

All 12 are conjecture environments with ClaimStatus but without `\label{}`.

| # | File | Line | Title | Status |
|---|------|------|-------|--------|
| 1 | feynman_diagrams.tex | 128 | Loop expansion = A-infinity operations | Heuristic |
| 2 | feynman_diagrams.tex | 240 | Bar complex and graph complex | Heuristic |
| 3 | genus_complete.tex | 625 | Holographic duality via bar-cobar | Conjectured |
| 4 | holomorphic_topological.tex | 406 | Chiral operad from HCS | Conjectured |
| 5 | holomorphic_topological.tex | 627 | W-algebra from Hitchin | Conjectured |
| 6 | free_fields.tex | 2285 | W-algebra A-infinity and quantum cohomology | Conjectured |
| 7 | free_fields.tex | 3989 | String amplitude, g >= 1 | Conjectured |
| 8 | free_fields.tex | 4019 | Bulk-boundary correspondence | Conjectured |
| 9 | free_fields.tex | 4071 | Bulk package from boundary shadow | Conjectured |
| 10 | free_fields.tex | 4089 | Holographic dictionary | Conjectured |
| 11 | free_fields.tex | 4162 | Loop corrections as string coupling | Conjectured |
| 12 | koszul_pair_structure.tex | 1852 | AdS/CFT as CS/Koszul duality | Conjectured |

**Resolution**: Add `\label{conj:...}` to each. All are physics-horizon Tier 3 conjectures.

---

## G6 (DISPLAY-MISMATCH): 16 instances from 2 root causes

### HIGH (1 root cause, 14 instances)

#### G6-H1. "Theorem~\ref{thm:bar-differential-structure}" on a `\begin{definition}` (12 refs) + "Theorem~\ref{thm:bar-differential}" (2 refs)
14 references across 10 files say "Theorem" but the target is `\begin{definition}` at bar_cobar_construction.tex:337.
**Propagation surface**:
- bar_cobar_construction.tex:2017 — "Theorem~\ref{thm:bar-differential}"
- bar_cobar_construction.tex:12002 — "Theorem~\ref{def:geometric-bar}"
- bar_cobar_construction.tex:14179,14313 — "Theorem~\ref{thm:bar-differential-structure}"
- deformation_theory.tex:316
- koszul_pair_structure.tex:1699
- beta_gamma.tex:153
- w_algebras_framework.tex:764
- free_fields.tex:2275
- holomorphic_topological.tex:961
- kontsevich_integral.tex:133,271
- genus_complete.tex:476
- concordance.tex:2884,3043
**Resolution**: Promote env to `\begin{theorem}` (the bar differential structure is assertive, not stipulative). Then all 14 "Theorem~\ref{}" become correct.

### MEDIUM (1 root cause, 2 instances)

#### G6-M1. `thm:betagamma-bc-koszul-detailed` — inconsistent display text
- beta_gamma.tex:940: "Theorem~\ref{thm:...}" — wrong (env is proposition)
- kac_moody_framework.tex:426: "Proposition~\ref{thm:...}" — display correct but prefix wrong
**Resolution**: Fix with G4-M1 above.

---

## G7 (STALE-CONCORDANCE): 3 findings

#### G7-M1. `conj:physical-pairing` — description mismatch
**File**: concordance.tex:6033
**Current**: "Physical pairing from Verdier duality"
**Actual**: Source (feynman_diagrams.tex:79) header is "Feynman rules dictionary"; content is about bar-cobar modeling Feynman rules.
**Resolution**: Update concordance description.

#### G7-M2. Open conjectures index includes 3 proved theorems
**File**: concordance.tex:5924-6086
**Current**: Section titled "The following conjectures remain open" includes `thm:modular-anomaly` (ProvedElsewhere), `thm:w-integrability` (ProvedHere), `thm:en-koszul-duality` (ProvedElsewhere)
**Resolution**: Rename section to "Index of conjectures and related results" or move proved items to a separate list.

#### G7-L1. 6 Heuristic items indexed as "Conjecture" (see G2-M10)
**Resolution**: Same as G2-M10.

---

## G8 (MISSING-CONCORDANCE): 0 findings

All main theorems (A-D, H), MC hierarchy (MC1-MC5), DK ladder (DK-0 through DK-5), and nine-futures entries are present in concordance. No omissions.

---

## G9 (UNPROPAGATED): 0 findings

All v40 label upgrades (12 conj:→thm: promotions, 4 thm:→conj: demotions, 6 rem: prefix fixes, 2 prop: fixes) are fully propagated. Zero stale display text at any reference site.

---

## G10 (PHANTOM-REF): 0 findings

All 1,960 unique `\ref{}` and `\eqref{}` targets resolve. Build log: 0 undefined references, 0 undefined citations, 0 multiply-defined labels.

---

## G11 (PROSE-CLAIM): 16 findings

### MEDIUM (5)

#### G11-M1. Koszul implies strict associativity — in remark prose
**File**: `higher_genus.tex:463-466`
**Claim**: "If A is Koszul, then bar(A) has m_k = 0 for k >= 3 (strictly associative)."
**Resolution**: Extract as a corollary or add forward reference to where this is proved.

#### G11-M2. Level-independence of bar cohomology — in remark prose
**File**: `combinatorial_frontier.tex:101-106`
**Claim**: "Bar cohomology dimensions are independent of the level k at generic values."
**Resolution**: Extract as a proposition with ClaimStatus.

#### G11-M3. VOAs have central curvature — in remark prose
**File**: `bar_cobar_construction.tex:11967-11969`
**Claim**: "Vertex operator algebras (with the standard vacuum axiom) and chiral algebras arising from unitary CFT have central curvature."
**Resolution**: Extract as a lemma (ProvedElsewhere).

#### G11-M4. Quasi-isomorphism conjecture in prose (Yangian)
**File**: `yangians.tex:813-819`
**Claim**: QI between E1-chiral Yangian and dg-shifted Yangian of DNP25, stated only in remark with inline ClaimStatus.
**Resolution**: Extract as a `\begin{conjecture}` with label.

#### G11-M5. Spectral-shift self-duality claim in computation prose
**File**: `yangians.tex:3965-3972`
**Claim**: Y(g)^! = Y(g) after spectral parameter shift u -> u+1, stated in a computation environment.
**Resolution**: Extract as a conjecture or corollary depending on proof status.

### LOW (11)

#### G11-L1. `higher_genus.tex:1688-1689` — star-product = quantization of OPE Poisson
#### G11-L2. `higher_genus.tex:1692-1693` — "All structures determined by genus-0 data" (Witten)
#### G11-L3. `higher_genus.tex:7241-7270` — explicit genus-1 complementarity computations in prose
#### G11-L4. `higher_genus.tex:4420-4424` — K_0(KCA)→Q surjective
#### G11-L5. `higher_genus.tex:6914-6916` — c=13 self-dual parenthetical
#### G11-L6. `bar_cobar_construction.tex:11955-11970` — strict vs homotopy nilpotence claims
#### G11-L7. `configuration_spaces.tex:1139-1143` — genus-stratified bar differential
#### G11-L8. `configuration_spaces.tex:1207-1227` — higher-genus Siegel Arnold relations
#### G11-L9. `en_koszul_duality.tex:776-781` — U_2(g) = topological shadow identification
#### G11-L10. `hochschild_cohomology.tex:120` — Coxeter element action claim
#### G11-L11. `chiral_koszul_pairs.tex:2876-2884` — W_k(sl_3) H^4 obstruction

---

## G12 (CROSS-VOLUME): 4 findings

### MEDIUM (2)

#### G12-M1. Bridge 3 (DK/YBE): Stale monograph frontier
**File**: Vol II concordance.tex:131
**Current**: Frontier column says "MC3 (DK extension)"
**Actual**: Bridge targets DK-0, which is proved. MC3 is about extensions beyond evaluation-generated core.
**Resolution**: Update to "DK-0 proved; MC3 extension open"

#### G12-M2. Bridge 4 (W-algebras): Stale monograph frontier
**File**: Vol II concordance.tex:132
**Current**: Frontier column says "MC5 (BRST=bar)"
**Actual**: MC5 genus 0 is proved; only higher genus is conjectural.
**Resolution**: Update to "MC5 genus 0 proved; higher genus conjectural"

### LOW (2)

#### G12-L1. Bridge 2 (Hochschild): Imprecise reference
**File**: Vol I concordance.tex:3537-3538
**Current**: Bridge references `thm:w-algebra-hochschild` (W-algebra computation)
**Better**: Should reference `thm:main-koszul-hoch` (Theorem H proper)

#### G12-L2. Vol II structural: Zero ClaimStatus macros in .tex files
**File**: All Vol II .tex files
**Current**: Vol II defines ClaimStatus macros but no .tex file uses them; status tracking is plain text in concordance only.
**Resolution**: Install ClaimStatus annotations in Vol II theorem environments (systematic, ~45 claims).

---

## Propagation Queue

Ordered by impact (most downstream references first):

| Priority | G-Code | Label/Location | Resolution | Propagation Sites | Effort |
|----------|--------|----------------|------------|-------------------|--------|
| 1 | G6-H1 | `thm:bar-differential-structure` on definition | Promote env to theorem | 14 refs across 10 files (become correct) | S |
| 2 | G4-M1 | `thm:betagamma-bc-koszul-detailed` on proposition | Rename to prop: | 2 refs in 2 files | S |
| 3 | G5 (all) | 12 unlabeled conjectures | Add labels | 12 edits, no refs to update | S |
| 4 | G4-M2-M6 | 5 orphaned backward-compatible labels | Delete aliases | 5 edits, 0 refs | S |
| 5 | G2-M10 | 6 Heuristic items in concordance index | Update concordance or source | concordance.tex + 4 source files | S |
| 6 | G2-H1 | `thm:bg-bar-coalg` theorem/Heuristic contradiction | Change env or upgrade proof | 1 file | S |
| 7 | G2-M1 | `thm:deformation-obstruction` outline proof | Change to ProvedElsewhere | 1 file | S |
| 8 | G2-M2 | `thm:modular-vs-quasi` heuristic proof | Change to ProvedElsewhere | 1 file | S |
| 9 | G2-M3,M4 | Two sketch proofs in higher_genus | Complete or downgrade | 1 file | M |
| 10 | G2-M5,M6 | Two sketch proofs in configuration_spaces | Complete or downgrade | 1 file | M |
| 11 | G2-L1-L9 | 9 definitions with ClaimStatus | Remove tags | 6 files | S |
| 12 | G12-M1,M2 | Stale Vol II concordance frontiers | Update 2 entries | 1 file (Vol II) | S |
| 13 | G7-M1,M2 | Concordance index framing | Edit section title + description | 1 file | S |
| 14 | G11-M1-M5 | 5 medium prose claims | Extract to theorem envs | 5 files | M |
| 15 | G12-L2 | Vol II ClaimStatus installation | Add ~45 tags | ~10 files (Vol II) | L |

---

## Completion Statement

> Every theorem-class environment across both manuscripts has been checked for G1-G6.
> Every concordance entry has been checked for G7-G8. Every recently-changed claim has
> been checked for G3 and G9. All 5 cross-volume bridges have been checked for G12.
> The structured catalogue contains 84 findings with zero TBD entries. The propagation
> queue is actionable — each item can be resolved by a single targeted edit without
> further research.

**Main theorems verified clean**: Theorems A, B, C, D_scal, H — all have complete proofs matching ProvedHere status. MC1 (proved), MC2 (proved), MC3-MC5 (correctly conjectured). DK-0 through DK-2/3 (proved, correctly scoped), DK-4/5 (correctly conjectured). Zero misstatuses in any main theorem or MC/DK entry.
