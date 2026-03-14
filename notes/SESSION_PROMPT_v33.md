# SESSION PROMPT v33 — Frontier Cartography: Control-Plane Audit and Unstable-Frontier Catalogue
# For: Claude Opus 4.6 (1M context) in Claude Code, extra high reasoning mode
# Date: 2026-03-14
# Supersedes: none (orthogonal to v32; v32 = correctness audit, v33 = control-plane audit)
# Prerequisite: v32 Forge Audit batches 1-11 complete (8 errors, 8 conventions fixed)

---

## 0. ROLE AND POSTURE

You are a control-plane cartographer. Your predecessors audited *correctness* — whether proofs are complete, whether formulas have right signs, whether ClaimStatus matches reality. You audit *visibility* — whether every mathematical claim that exists in the source is properly registered in the tracking infrastructure, correctly labeled, consistently propagated across all files that reference it, and faithfully reflected in the constitutional document (concordance.tex).

**The fundamental assumption**: Nothing is correctly tracked until independently verified. A `\ClaimStatusProvedHere` tag may be present while the concordance still calls the result conjectural. A proved theorem may carry a `conj:` label from when it was first stated. A conjecture may have been upgraded in one file but its display text still reads "Conjecture~\ref{thm:...}" in three others. A formula may be numerically verified in `compute/tests/` but the corresponding theorem environment lacks a `\ClaimStatus` tag entirely. These are the cracks. Your job is to find every one.

**Epistemic posture**: Treat each mathematical claim as an expression yearning toward what it is meant to be. A `\begin{theorem}` aspires to theoremhood; a `\ClaimStatusProvedHere` aspires to truth. Do not assume any aspiration is realized. Your catalogue records the gap between aspiration and verification — but does so without cynicism: the purpose is to enable the propagation pass that closes every gap.

**Your output is a catalogue, not surgery.** You do not edit the manuscript. You do not fix findings. You produce a structured inventory of every control-plane gap, with enough precision that each can be resolved by a single targeted edit in a subsequent session. The catalogue is the deliverable.

**Scope**: Two repositories, one programme.
- **Volume I** (primary): `~/chiral-bar-cobar` — 1,811pp monograph, ~132K source lines, ~1,700 ClaimStatus tags, 5,984 tests
- **Volume II** (secondary): `~/ainfinity-chiral-hochschild-cohomology-3d-qft` — 173pp paper, ~9K source lines, ~45 major claims, 133 tests
- **Cross-volume**: 5 conjectural bridges. Both manuscripts must agree on what is proved and what is open.

---

## 1. WHAT THE CONTROL PLANE IS

The control plane has five layers. A claim is "fully tracked" when it is registered at all five. A gap at any layer is a finding.

| Layer | Infrastructure | What It Tracks | Authoritative Source |
|-------|---------------|----------------|---------------------|
| **L1: Tag** | `\ClaimStatus{ProvedHere,ProvedElsewhere,Conjectured,Heuristic,Open}` | Whether each theorem-env has an epistemic status | Inline in .tex files |
| **L2: Label** | `\label{thm:,prop:,lem:,cor:,conj:,def:,rem:}` + environment type | Whether label prefix matches environment type | Inline in .tex files |
| **L3: Metadata** | `metadata/claims.jsonl`, `census.json`, `label_index.json` | Machine-readable claim registry | `scripts/generate_metadata.py` |
| **L4: Constitution** | `concordance.tex` (Ch. 34) + MC hierarchy + DK ladder | Strategic status of all main results | concordance.tex (the constitution) |
| **L5: Compute** | `compute/tests/` (5,984 tests) | Numerical verification of explicit formulas | Test files in compute/ |

**A fully tracked claim** has: correct ClaimStatus (L1), matching label prefix (L2), appears in metadata (L3), is reflected in concordance if it's a main/MC result (L4), and its formulas are computationally verified if numerically checkable (L5).

---

## 2. THE TWELVE GAP TYPES

Every finding belongs to exactly one type. Mutually exclusive, collectively exhaustive.

### Tag-Layer Gaps (L1)

| Code | Name | Definition | Severity | Detection |
|------|------|------------|----------|-----------|
| **G1** | UNTAGGED | Theorem/proposition/lemma/corollary/conjecture environment without any `\ClaimStatus*` | HIGH | Automated: find env without ClaimStatus within 5 lines |
| **G2** | MISSTATUS | ClaimStatus contradicts actual mathematical content (e.g., ProvedHere on a sketch, Conjectured on a result proved in the same file) | CRITICAL | Manual: read proof, judge completeness |
| **G3** | STALE-STATUS | ClaimStatus was correct when written but is now outdated due to work in a later session (e.g., conjecture proved in v31 but tag not updated) | HIGH | Cross-ref: check session notes, concordance |

### Label-Layer Gaps (L2)

| Code | Name | Definition | Severity | Detection |
|------|------|------------|----------|-----------|
| **G4** | PREFIX-MISMATCH | Label prefix doesn't match environment type (`conj:` on theorem, `thm:` on conjecture, etc.) | HIGH | Automated: regex cross-check env type vs label prefix |
| **G5** | UNLABELED | Theorem-class environment (thm/prop/lem/cor/conj) without any `\label{}` | MEDIUM | Automated: find env without \label within 5 lines |
| **G6** | DISPLAY-MISMATCH | Reference display text contradicts label or env type ("Conjecture~\ref{thm:X}", "Theorem~\ref{conj:Y}") | LOW | Automated: grep for "Conjecture.*\\ref\{thm:" etc. |

### Constitution-Layer Gaps (L4)

| Code | Name | Definition | Severity | Detection |
|------|------|------------|----------|-----------|
| **G7** | STALE-CONCORDANCE | Concordance entry inconsistent with current manuscript (status changed, theorem promoted/demoted, scope refined, but concordance not updated) | HIGH | Manual: compare concordance claims vs actual source |
| **G8** | MISSING-CONCORDANCE | Main result or MC-related claim not mentioned in concordance at all | MEDIUM | Manual: check each main theorem/MC claim has concordance entry |

### Propagation Gaps (Cross-File)

| Code | Name | Definition | Severity | Detection |
|------|------|------------|----------|-----------|
| **G9** | UNPROPAGATED | Status change in one file not reflected in all files that reference the claim (e.g., conjecture promoted to theorem in source file but still called "Conjecture" in 3 other files) | HIGH | Automated: for each upgraded label, grep all \ref{} sites |
| **G10** | PHANTOM-REF | Proof cites \ref{X} but X doesn't exist, or X doesn't say what the proof claims, or X's hypotheses aren't satisfied | HIGH | Semi-automated: cross-reference labels |

### Boundary Gaps (Control Plane Edge)

| Code | Name | Definition | Severity | Detection |
|------|------|------------|----------|-----------|
| **G11** | PROSE-CLAIM | Mathematical claim stated in prose, remark, or proof body that is substantive enough to deserve its own theorem-class environment but doesn't have one | MEDIUM | Manual: read prose for "it follows that", "this shows", "we conclude", "one can show" |
| **G12** | CROSS-VOLUME | Claim status inconsistent between Vol I and Vol II (e.g., bridge claim called "conjectural" in Vol II but "proved" in Vol I, or vice versa) | MEDIUM | Manual: check all 5 bridges |

### Exclusion Criteria (NOT gaps)

These are intentional and should NOT be flagged:
- **Remarks without ClaimStatus**: Remarks are editorial/expository. ~1,000 remarks lack tags by design.
- **Definitions without ClaimStatus**: Definitions are stipulative, not claims.
- **Computations without ClaimStatus** (if inside a proof): Intermediate calculations are part of the proof, not standalone claims.
- **`eq:` labels on display math inside theorem envs**: The equation is the reference target, not the theorem. Intentional.
- **Results absent from concordance**: Only main theorems (A/B/C/D/H), MC results, and DK ladder entries belong in concordance. Not every lemma.

---

## 3. EXECUTION PROTOCOL

### Phase 0: Orientation and Baseline Census

**Do this FIRST. Do not skip. The census numbers anchor everything that follows.**

```
STEP 0.1 — Build both volumes.
  Vol I:  pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; cd ~/chiral-bar-cobar && make fast
  Vol II: cd ~/ainfinity-chiral-hochschild-cohomology-3d-qft && make fast

STEP 0.2 — Regenerate Vol I metadata (authoritative census).
  cd ~/chiral-bar-cobar && python scripts/generate_metadata.py
  Read metadata/census.json → record PH, PE, CJ, HE, OP counts.

STEP 0.3 — Fresh grep census (cross-check).
  For each ClaimStatus type, grep -rc across chapters/ appendices/ --include='*.tex'.
  Compare with metadata counts. If they differ by more than 5%, investigate.

STEP 0.4 — Read the constitution.
  Read concordance.tex in full. Note: MC hierarchy status, DK ladder status, theorem architecture,
  nine-futures assessment. This is your reference for G7/G8 detection.

STEP 0.5 — Read session history.
  Read notes/GLOBAL_TASKLIST.md, notes/FORGE_AUDIT_all_batches.md, notes/autonomous_state.md.
  These tell you what changed recently and where stale-status gaps (G3) are likely.

STEP 0.6 — Record baseline.
  Write the orientation summary to notes/FRONTIER_CARTOGRAPHY_baseline.md:
    - Vol I: page count, claim counts by status, test count, build status
    - Vol II: page count, claim counts, test count, build status
    - Date, commit hash, branch
```

### Phase 1: Automated Detection (use tools, not eyeballs)

**Run these searches BEFORE reading any files.** They catch G1, G4, G5, G6, G9, G10 mechanically.

```
SEARCH 1.1 — G1 (UNTAGGED): Find theorem-class envs without ClaimStatus.
  Strategy: For each env type in {theorem, proposition, lemma, corollary, conjecture},
  find \begin{TYPE} that is NOT followed by ClaimStatus within the next 5 lines.
  Use multiline grep or a Python script against the .tex sources.
  Record: file, line number, environment type, title (if any).

SEARCH 1.2 — G4 (PREFIX-MISMATCH): Find label/env-type mismatches.
  Strategy: For each \label{PREFIX:...} inside a \begin{TYPE}...\end{TYPE},
  check that PREFIX matches TYPE (thm↔theorem, prop↔proposition, lem↔lemma,
  cor↔corollary, conj↔conjecture, def↔definition, rem↔remark).
  IMPORTANT: a conj: label inside a theorem env is HIGH severity (overclaiming).
  A thm: label inside a conjecture env is also HIGH (underclaiming or stale upgrade).

SEARCH 1.3 — G5 (UNLABELED): Find theorem-class envs without labels.
  Strategy: Find \begin{TYPE} not followed by \label within 5 lines.
  Exclude: definitions, remarks (intentionally unlabeled sometimes).

SEARCH 1.4 — G6 (DISPLAY-MISMATCH): Find reference display text contradictions.
  Search patterns:
    "Conjecture[~\s]*\\\\ref\\{thm:"     → claims theorem is conjecture
    "Theorem[~\s]*\\\\ref\\{conj:"        → claims conjecture is theorem
    "Lemma[~\s]*\\\\ref\\{thm:"           → wrong env type in display
    "Proposition[~\s]*\\\\ref\\{conj:"     → wrong env type in display
    (and all other cross-type patterns)

SEARCH 1.5 — G9 (UNPROPAGATED): Find stale references to upgraded claims.
  From MEMORY.md and session notes, identify all claims that changed status
  (promoted conj→thm, demoted thm→conj, scope-qualified, etc.).
  For each, grep all \ref{LABEL} sites and check display text consistency.

SEARCH 1.6 — G10 (PHANTOM-REF): Find broken cross-references.
  grep for \ref{...} where the label doesn't exist in label_index.json.
  Also: grep the build log (main.log) for "Reference .* undefined".
```

**Record all automated findings in notes/FRONTIER_CARTOGRAPHY_auto.md.** Structured format per finding (see §5).

### Phase 2: Manual Deep Read (where automation can't reach)

G2, G3, G7, G8, G11, G12 require reading comprehension. Process files in priority order.

**Priority order** (where gaps concentrate):

```
TIER 1 — Constitution and cross-volume (G7, G8, G12):
  1. concordance.tex (6,086 lines — the constitution, G7/G8 ground zero)
  2. Vol II concordance.tex (147 lines — check 5 bridges, G12)

TIER 2 — Most technical files (G2, G3, G11 concentrate here):
  3. bar_cobar_construction.tex (15,078 lines — sub-batch by 2K-line chunks)
  4. higher_genus.tex (~16K lines — Theorems B/C/D, sub-batch)
  5. yangians.tex (12,632 lines — most recent, sub-batch)

TIER 3 — Example families (G2, G11):
  6. w_algebras_framework.tex + w_algebras_deep.tex
  7. kac_moody_framework.tex
  8. free_fields.tex
  9. toroidal_elliptic.tex

TIER 4 — Theory structure (G2, G11):
  10. chiral_koszul_pairs.tex + koszul_pair_structure.tex
  11. configuration_spaces.tex
  12. deformation_theory.tex + quantum_corrections.tex
  13. en_koszul_duality.tex
  14. poincare_duality_quantum.tex + hochschild_cohomology.tex

TIER 5 — Connections and appendices (G2, G11):
  15. bv_brst.tex + feynman_diagrams.tex + feynman_connection.tex
  16. holomorphic_topological.tex + physical_origins.tex
  17. All appendices (16 files)

TIER 6 — Frame and showcase:
  18. heisenberg_frame.tex
  19. examples_summary.tex + detailed_computations.tex + genus_expansions.tex
  20. minimal_model_fusion.tex + minimal_model_examples.tex
```

**For each file, the manual protocol**:

```
M.1  Read the file in 2000-line chunks. Do not skip interior sections.

M.2  For each theorem-class environment:
     - Does the ClaimStatus match the actual content? (G2)
     - Was this claim's status recently changed? Check session notes. (G3)
     - Are there substantive mathematical claims in the proof body that should
       be extracted as their own lemma/proposition? (G11)

M.3  For concordance.tex specifically (G7, G8):
     - For EACH entry in the MC hierarchy: read the cited theorem,
       verify the concordance description matches the actual statement.
     - For EACH entry in the DK ladder: same.
     - For EACH entry in the nine-futures table: same.
     - For EACH theorem in the "principal contributions" section: same.
     - Flag any discrepancy as G7. Flag any missing entry as G8.

M.4  For Vol II (G12):
     - Read all 5 bridge descriptions in Vol II concordance.tex.
     - For each: find the corresponding Vol I claim. Compare status.
     - Flag any inconsistency as G12.
```

### Phase 3: Propagation Surface Analysis

**For each finding of severity HIGH or CRITICAL**, compute its propagation surface:

```
P.1  Grep for every \ref{LABEL} across all .tex files.
P.2  For each reference site: record file:line and the display text used.
P.3  Identify which reference sites would need to change if this finding is resolved.
P.4  Record the propagation surface as part of the finding (see §5).
```

This is what makes the catalogue *actionable* — the subsequent propagation pass knows exactly which files to touch for each fix.

### Phase 4: Synthesis and Output

```
S.1  Merge automated findings (Phase 1) and manual findings (Phase 2).
S.2  Deduplicate: a single gap may be caught by both automated and manual passes.
S.3  Compute propagation surfaces (Phase 3) for all HIGH/CRITICAL findings.
S.4  Write the complete catalogue to notes/FRONTIER_CARTOGRAPHY_catalogue.md (§5 format).
S.5  Write the summary table and propagation queue (§6 format).
```

---

## 4. ANTI-FAILURE-MODE PROTOCOL

### F1: Over-Flagging
**Symptom**: Flagging 500+ "gaps" that are mostly intentional (remarks without ClaimStatus, definitions without labels).
**Antidote**: Re-read §2 Exclusion Criteria before recording ANY finding. Ask: "Is this intentional?" Remarks, definitions, and intermediate computations are excluded by design. If your finding count exceeds 300 for Vol I, you are almost certainly over-flagging. The true gap count for theorem-class environments is likely ~150-250.

### F2: Under-Reading
**Symptom**: Relying entirely on automated grep and never reading the actual mathematical content. Misses G2 (misstatus), G3 (stale-status), G7 (stale-concordance), G11 (prose-claims) entirely.
**Antidote**: Phase 1 (automated) catches ~40% of gaps. Phase 2 (manual) catches the remaining ~60%. Do NOT skip Phase 2. The most consequential gaps — where a "theorem" is actually a sketch, or where concordance is stale — are invisible to grep.

### F3: Concordance Fetishism
**Symptom**: Expecting every lemma and remark to appear in concordance. Flagging hundreds of G8 (missing-concordance) for minor results.
**Antidote**: Concordance tracks: the 5 main theorems (A/B/C/D/H), the MC hierarchy (MC1-MC5), the DK ladder (DK-0 through DK-5), the nine-futures assessment, and the principal contributions. That's ~50-80 entries. A lemma in Chapter 7 does NOT need a concordance entry unless it is part of a main theorem's proof chain.

### F4: Attention Decay
**Symptom**: After 50+ findings, quality of manual assessment drops. Mechanical "PASS" stamps in later files.
**Antidote**: After every 5 files in Phase 2, insert a checkpoint. Re-read the G-code definitions. Ask: "Am I still distinguishing G2 from G3? Am I catching G11 (prose-claims)?" The densest gaps live in the longest files (bar_cobar 15K, higher_genus 16K, yangians 12K) — do not rush these.

### F5: Catalogue-Fix Conflation
**Symptom**: Starting to edit .tex files during the catalogue phase. "I'll just fix this one..."
**Antidote**: This session produces ONE artifact: the catalogue. No .tex edits. No label changes. No ClaimStatus additions. The catalogue is the input to a SEPARATE propagation session. Mixing catalogue and fix causes state corruption: you change a file, then later in the same pass you read a file that references it, and your earlier change is invisible.

### F6: Cross-Volume Neglect
**Symptom**: Spending 95% of effort on Vol I and giving Vol II a cursory scan.
**Antidote**: Vol II has only ~45 claims and 9K lines — it takes 30 minutes to read thoroughly. But it has ~18 NeedsVerification claims and 4 conjectured results whose status relative to Vol I may have drifted. The 5 bridges are the most important cross-file findings in the entire catalogue.

### F7: Propagation Surface Laziness
**Symptom**: Recording a finding without its propagation surface. "Just fix the label" without noting the 7 other files that reference it.
**Antidote**: For HIGH/CRITICAL findings, the propagation surface IS the finding. A label change without display-text updates creates 7 new G6 findings. Run the grep. List every reference site. This is what makes the catalogue actionable.

---

## 5. OUTPUT FORMAT: PER-FINDING

```markdown
### [G-CODE] [Severity] [Vol] [File:Line] [Label or description]

**Current state**: [What the manuscript/control-plane currently says]
**Actual state**: [What independent analysis reveals the true state to be]
**Evidence**: [How you know — grep output, file read, cross-reference, compute test, session note]
**Resolution**: [Single sentence: what edit resolves this gap]
**Propagation surface** (HIGH/CRITICAL only):
  - [file1:line] — [what needs to change there]
  - [file2:line] — [what needs to change there]
  - ...
```

---

## 6. OUTPUT FORMAT: SUMMARY AND QUEUE

### Summary Table

```markdown
| Gap Type | Code | Total | CRITICAL | HIGH | MEDIUM | LOW |
|----------|------|-------|----------|------|--------|-----|
| Untagged | G1   |       |          |      |        |     |
| Misstatus | G2  |       |          |      |        |     |
| Stale-Status | G3 |     |          |      |        |     |
| Prefix-Mismatch | G4 | |          |      |        |     |
| Unlabeled | G5  |       |          |      |        |     |
| Display-Mismatch | G6 | |         |      |        |     |
| Stale-Concordance | G7 | |        |      |        |     |
| Missing-Concordance | G8 | |      |      |        |     |
| Unpropagated | G9 |    |          |      |        |     |
| Phantom-Ref | G10 |    |          |      |        |     |
| Prose-Claim | G11 |    |          |      |        |     |
| Cross-Volume | G12 |   |          |      |        |     |
| **TOTAL** |      |      |          |      |        |     |
```

### Propagation Queue

Ordered by impact (most downstream references first):

```markdown
| Priority | G-Code | Label/Location | Resolution | Propagation Sites | Effort |
|----------|--------|----------------|------------|-------------------|--------|
| 1        |        |                |            | N files           | S/M/L  |
| 2        |        |                |            |                   |        |
| ...      |        |                |            |                   |        |
```

### Completion Criterion

The catalogue is COMPLETE when you can state:

> "Every theorem-class environment across both manuscripts has been checked for G1-G6.
> Every concordance entry has been checked for G7-G8. Every recently-changed claim has
> been checked for G3 and G9. All 5 cross-volume bridges have been checked for G12.
> The structured catalogue exists with zero TBD entries. The propagation queue is
> actionable — each item can be resolved by a single targeted edit without further research."

---

## 7. GROUND TRUTH HIERARCHY

When in doubt about a claim's true status, resolve using:

| Priority | Source | Authority |
|----------|--------|-----------|
| 1 | CLAUDE.md Critical Pitfalls | Sacred. Computation-verified. Manuscript bends to these. |
| 2 | concordance.tex (Ch. 34) | Constitutional. When chapters disagree, concordance wins. |
| 3 | compute/tests/ (5,984 tests) | Computational ground truth. Specific numerical values. |
| 4 | Session notes (FORGE_AUDIT, GLOBAL_TASKLIST) | Recent history. What changed and when. |
| 5 | The proof text itself | Check completeness, signs, hypotheses, circularity. |
| 6 | Prose claims outside theorem envs | Lowest trust. Stale language concentrates here. |

---

## 8. WHAT THE CATALOGUE ENABLES

The catalogue is not an end — it is the input to a **doctrinal propagation pass** that brings every claim into full control-plane registration. That pass will:

1. Add missing ClaimStatus tags (resolves all G1)
2. Correct misstatus tags (resolves all G2, G3)
3. Fix label prefixes (resolves all G4)
4. Add missing labels (resolves all G5)
5. Update display text at all reference sites (resolves all G6, G9)
6. Update concordance entries (resolves all G7, G8)
7. Fix phantom references (resolves all G10)
8. Extract prose claims into theorem environments (resolves all G11)
9. Synchronize cross-volume status (resolves all G12)

After propagation, the manuscript achieves **doctrinal consistency**: every mathematical claim is visible to the control plane, correctly classified, consistently referenced, and faithfully reflected in the constitution.

---

## 9. THE ELEVEN CRITICAL PITFALLS (re-read at each batch boundary)

1. COHOMOLOGICAL grading: |d| = +1. Bar uses DESUSPENSION s^{-1}. V[n]^k = V^{k+n}.
2. Koszul duals: Com^! = Lie (NOT coLie). Heisenberg NOT self-dual. bc^! = betagamma.
3. Bar differential: d_bracket^2 != 0. Full d = d_bracket + d_curvature has d^2 = 0.
4. Curved A-infinity: m_1^2(a) = [m_0,a] (COMMUTATOR, MINUS sign).
5. Central charges: Sugawara c = k*dim(g)/(k+h^vee), UNDEFINED at k=-h^vee.
6. Periodicity: 2h Coxeter (NOT 2h^vee). Wrong for rank > 1.
7. Geometry: FM = blowup (NOT X^n \ Delta). Normal bundle = tangent, NOT cotangent.
8. Physics: QME factor 1/2. HCS coefficient 2/3. Lambda = :TT: - (3/10)d^2 T (MINUS).
9. P-infinity vs Coisson: Different objects, different quantization levels.
10. Differentials: dfib^2 = kappa * omega_g (NOT zero). Dg^2 = 0.
11. Cyclic CE: H^n_cyc(g,g) = H^{n+1}(g). H^2_cyc = C for all simple g.

---

## 10. KEY INFRASTRUCTURE REFERENCE

```
Vol I:
  ~/chiral-bar-cobar/
  ├── scripts/generate_metadata.py    → regenerate census/claims/labels
  ├── metadata/census.json            → claim counts by status/part/file
  ├── metadata/claims.jsonl           → one JSON line per claim
  ├── metadata/label_index.json       → all labels with file:line
  ├── metadata/dependency_graph.dot   → theorem DAG
  ├── chapters/connections/concordance.tex → CONSTITUTION (Ch. 34)
  ├── compute/tests/                  → 5,984 ground-truth tests
  ├── notes/GLOBAL_TASKLIST.md        → live task tracker
  ├── notes/FORGE_AUDIT_all_batches.md → v32 audit findings
  └── Makefile                        → make fast, make test, make metadata

Vol II:
  ~/ainfinity-chiral-hochschild-cohomology-3d-qft/
  ├── chapters/connections/concordance.tex → status ledger (§22)
  ├── compute/tests/                  → 133 tests
  ├── notes/autonomous_state.md       → session state
  └── Makefile                        → make fast, make test

Cross-Volume Bridges (check ALL for G12):
  1. Bar-cobar:    Vol II bar-cobar-review.tex  ↔  Vol I Thm A
  2. Hochschild:   Vol II hochschild.tex        ↔  Vol I Thm H
  3. DK/Yang-Baxter: Vol II spectral-braiding.tex ↔ Vol I DK-0
  4. W-algebras:   Vol II w-algebras.tex        ↔  Vol I MC5
  5. Physics functor: Vol II bv-construction.tex ↔ Vol I framework
```
