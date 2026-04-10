# CLAUDE.md Restructure Proposal (Wave 12)

**Author:** Raeez Lorgat
**Target file:** `/Users/raeez/chiral-bar-cobar/CLAUDE.md` (currently 285 lines, ~9,000 words, 141+ APs)
**Scope:** structural redesign only. No rewrite of content. Authority of current document preserved.
**Status:** proposal. Do NOT apply until Wave 12-1 through 12-10 drafts land and are cross-checked.

---

## 0. Executive Summary

The current CLAUDE.md is lived-in but not laid out for fast reference. It groups APs by "cognitive trigger" (BEFORE WRITING A FORMULA / BEFORE WRITING A SCOPE CLAIM / etc.), which is a useful mental map but a poor lookup table: a single AP can belong to three triggers, and the highest-recurrence APs (AP126 r-matrix level, AP10/AAP11 hardcoded expected values, AP132 augmentation ideal, AP1 kappa-from-memory, AP5 cross-volume grep) are buried in the same flat list as APs that have fired once in 12 months.

The proposed restructure:

1. Elevates the **top 20–30 repeat APs** to a **HOT ZONE** at the top of the file, each with an **operational template** (not prose description).
2. Adds a **True Formula Census** section that lists every canonical formula once, with sanity checks, so agents can grep a single source of truth rather than reconstructing from AP text.
3. Adds an **Opus 4.6 Quirks** section documenting model-specific failure modes observed in this codebase (pattern-matching across occurrences, confident confabulation of operadic theory, tendency to harmonize notation across contexts).
4. Keeps the full AP catalog but **reorganizes by domain** (kappa, r-matrices, grading, scope, prose, labels, arithmetic) rather than by cognitive trigger, preserving the trigger view as a cross-reference index.
5. Adds a **Hook Enforcement Map** so the author and agents can see at a glance which APs are machine-checked vs. purely cultural.
6. Adds an **AP Evolution Process** (how to add, refine, retire) so the catalog does not accrete indefinitely.
7. Adds **anchor links and a table of contents** so cross-references become one-click.

Total proposed length: ~1.4× current (~400 lines, ~12,500 words). The growth is concentrated in the HOT ZONE (operational templates) and the Formula Census (explicit formulas + sanity checks); the full AP catalog shrinks slightly through merges and dedup.

---

## 1. Proposed Table of Contents

```
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

§0  Identity                                              [unchanged, 1 paragraph]
§1  Pre-reading Checklist                                 [NEW, 10 lines]
§2  HOT ZONE -- Top Repeat APs with Operational Templates [NEW, 25 entries]
§3  The Beilinson Principle                               [unchanged]
§4  The Five Objects, Five Theorems, Key Constants        [unchanged, consolidated]
§5  True Formula Census                                   [NEW, one formula per line]
§6  Opus 4.6 Quirks and Failure Modes                     [NEW]
§7  Pre-Edit Verification Protocol                        [NEW, templates]
§8  LaTeX Pitfall Blacklist                               [NEW, integrated from AAP1/AP121/AP125]
§9  Full Anti-Pattern Catalog
    §9.1  By Domain
        §9.1.1  Kappa formulas
        §9.1.2  R-matrices, pole orders, propagators
        §9.1.3  Grading, signs, suspension
        §9.1.4  Scope, quantifiers, conditional/universal
        §9.1.5  Bar complex and augmentation
        §9.1.6  Four functors / duality
        §9.1.7  SC operad and promotion
        §9.1.8  Shadow / Hochschild
        §9.1.9  Prose hygiene
        §9.1.10 Labels, cross-refs, LaTeX
        §9.1.11 Arithmetic, special functions, combinatorics
        §9.1.12 Computation discipline
        §9.1.13 Volume III kappa-spectrum
        §9.1.14 Meta (agent anti-patterns, AAP)
    §9.2  Cognitive-Trigger Index (cross-ref view)
§10 Hook Enforcement Map                                  [NEW]
§11 AP Evolution Process                                  [NEW]
§12 Regression Safeguards (RS-1 through RS-20)            [unchanged]
§13 Structural Facts                                      [unchanged]
§14 Architecture (Vols I/II/III)                          [unchanged, consolidated]
§15 Writing Standard                                      [unchanged]
§16 Skills                                                [unchanged]
§17 Build                                                 [unchanged]
§18 Session Protocol                                      [unchanged]
§19 LaTeX / Git                                           [unchanged, consolidated]
```

---

## 2. Section Count, Sizes, Total Length

| Section | Current lines | Proposed lines | Delta |
|---|---|---|---|
| §0 Identity | 3 | 3 | 0 |
| §1 Pre-reading Checklist | 0 | 10 | +10 |
| §2 HOT ZONE | 0 | 80 | +80 |
| §3 Beilinson Principle | 5 | 5 | 0 |
| §4 Five Objects / Theorems / Constants | 18 | 18 | 0 |
| §5 True Formula Census | 0 (scattered) | 50 | +50 (net, after dedup) |
| §6 Opus 4.6 Quirks | 0 | 25 | +25 |
| §7 Pre-Edit Verification | 0 | 20 | +20 |
| §8 LaTeX Pitfall Blacklist | scattered | 15 | +15 |
| §9 Full AP Catalog (domain-reorganized) | 130 | 115 | −15 (dedup) |
| §10 Hook Enforcement Map | 0 | 25 | +25 |
| §11 AP Evolution Process | 0 | 15 | +15 |
| §12 Regression Safeguards | 11 | 11 | 0 |
| §13 Structural Facts | 8 | 8 | 0 |
| §14 Architecture | 9 | 9 | 0 |
| §15–§19 Writing/Skills/Build/Session/LaTeX/Git | 45 | 45 | 0 |
| **Total** | **~285** | **~454** | **+169 (~1.6×)** |

Word count: current ~9,000 → proposed ~14,000. The 1.6× growth is entirely front-loaded: everything new lives in §1–§8, so the "if you only read the first 200 lines" experience is strictly denser and more actionable.

---

## 3. Opening Paragraphs for NEW Sections

### §1 Pre-reading Checklist -- ALWAYS read before first Edit

> Before any edit in any of the three volumes, verify: (1) you have run `make fast` within the last 30 minutes, (2) you have read the actual `.tex` source and not a CLAUDE.md description of it, (3) you have grepped all three volumes for the pattern you are about to change, (4) the HOT ZONE below contains no entry matching the class of edit you are about to make. If any of these is false, STOP and fix it first. This checklist is not aspirational; it is the minimum viable discipline that keeps the three-volume programme consistent.

### §2 HOT ZONE -- Top Repeat APs with Operational Templates

> The 25 entries below are the APs that have fired most often in the last 300 commits, weighted by "cost to recover" (cross-volume grep-and-fix ≫ single-file typo). Each entry has an **operational template**: the literal keystrokes or grep invocation you run BEFORE writing, not a description of a philosophy. If you only read 80 lines of CLAUDE.md, read these. An AP earns a HOT ZONE slot by (a) appearing in 3+ commits as the proximate cause of a rectification, or (b) surviving visual inspection in peer review. Entries are demoted out of HOT ZONE after 60 commits without recurrence; see §11.

### §5 True Formula Census

> Every canonical formula in the three volumes appears ONCE in this section, with a source (canonical `.tex` file), a convention qualifier (Vol I OPE / Vol II lambda-bracket / Vol III motivic), and at least two sanity checks (limiting case, symmetry, or cross-family). All other occurrences in CLAUDE.md, in chapter prose, in compute engines, and in tests MUST cite this census by anchor, not restate the formula. Discrepancies between this census and source files are resolved by direct computation, never by harmonizing to whichever appears more frequently (AP128, V2-AP28). The census exists because reconstruction from memory (AP1 for kappa, AP126 for r-matrices, AP135 for partition numbers) accounts for the single largest class of rectification commits in the 300-commit archaeology.

### §6 Opus 4.6 Quirks and Failure Modes

> This section documents failure modes observed specifically under Claude Opus 4.6 (1M context) in this codebase. These are not anti-patterns for the mathematics; they are anti-patterns for the model, and they must be counter-engineered at the prompt level. Examples: (a) pattern-matching a formula across nearby occurrences and propagating a wrong variant (AP3, AP10, V2-AP28, AP128); (b) confabulating operadic references without citation (AAP18); (c) harmonizing subscripts across contexts (AP-CY16); (d) writing "iff" when only one direction is proved (AP36); (e) optimizing README prose for impressiveness beyond ground truth (AP-CY15); (f) batch-propagating corrections before verifying the first instance (V2-AP19); (g) silently omitting the level k from r-matrices because $\Omega/z$ and $k\Omega/z$ both look valid (AP126/AP141). Each quirk is paired with a prompt-level mitigation.

### §7 Pre-Edit Verification Protocol (Templates)

> This section contains copy-pasteable templates for common edit classes: "changing a kappa formula", "adding a theorem", "migrating a chapter between volumes", "updating a test expected value", "writing a conjecture vs. theorem environment". Each template enumerates the grep invocations, the sanity-check evaluations, and the minimum number of independent derivation paths (AAP11). Templates are terse (5–10 lines each) and terminate in a "ready to write" checkpoint. An edit made without running the applicable template is an AP17 violation.

### §8 LaTeX Pitfall Blacklist

> Patterns that LaTeX compiles silently but that produce the wrong document. This list is grep-ready. Run each grep before every commit: `antml`, `</invoke>`, backtick numerals, Markdown `**bold**`, bare `s^` without `^{-1}`, `\newcommand` in chapter files, `\title{}` or `\begin{abstract}` or `\tableofcontents` in \input'd chapter files, `Part~[IVXL]` hardcoded numerals, duplicate `\label{}`, stale `thm:` prefix on a `\begin{conjecture}`. The blacklist is NOT a substitute for reading the source; it is the last-mile filter.

### §10 Hook Enforcement Map

> For each AP in §9, this table records whether a pre-commit hook, CI test, or grep-on-save currently enforces it. Columns: AP number, enforcement status (HOOK / TEST / GREP / CULTURE), location of the enforcing script, and failure mode if the hook is bypassed. An AP with status CULTURE is only as strong as the current session's discipline; these are the candidates for future mechanization. When adding a new AP, §11 requires specifying its initial enforcement column.

### §11 Process for AP Evolution

> APs are not immortal. The catalog accretes because adding an AP costs nothing and retiring one feels like tempting fate. This section defines the lifecycle: **propose** (in a commit message citing the triggering failure, with a proposed cognitive trigger and enforcement column), **activate** (after 1 independent confirmation), **promote** (to HOT ZONE after 3 recurrences), **refine** (split into child APs when the entry exceeds 3 paragraphs), **merge** (when two APs are found to describe the same failure), **retire** (after 60 commits without recurrence AND with a mechanical enforcement in place). Retired APs are moved to `compute/audit/retired_anti_patterns.md`, not deleted. The lifecycle runs at every Wave boundary.

---

## 4. HOT ZONE Content (Proposed 25 Entries)

Each entry has the operational template format:

```
H1. AP126/AP141 — r-matrix level k must not vanish
    OPERATIONAL TEMPLATE: before writing any r-matrix,
    (1) grep -rn 'r(z)\s*=\s*\\Omega' chapters/    # expect 0 hits
    (2) grep -rn 'r(z)\s*=\s*k\s*\\Omega' chapters/ # inspect all
    (3) evaluate at k=0: verify r -> 0 symbolically
    (4) cross-reference §5.2 (r-matrix census)
    TRIGGER FREQUENCY: 42+ instances (12 + 30 in full-volume sweep).
    HOOK: GREP (partial). Upgrade to pre-commit check.
```

Proposed HOT ZONE slate (numbered H1–H25):

| Slot | Source AP(s) | Title | Trigger frequency |
|---|---|---|---|
| H1  | AP126, AP141 | r-matrix level k vanishing check | 42+ |
| H2  | AP1 | kappa from memory is FORBIDDEN; read landscape_census.tex | 30+ |
| H3  | AP10, AAP11, AP128, V2-AP28 | Hardcoded expected values need 2+ derivation paths | 25+ |
| H4  | AP132 | B(A) uses augmentation ideal Ā, not A | repeated |
| H5  | AP5, AAP6 | Grep ALL THREE volumes after correction | always |
| H6  | AP22, AP44, AP45 | Desuspension sign: `s^{-1}`, NEVER bare `s` | 20+ |
| H7  | AP32 | Uniform-weight vs all-weight tag on F_g, obs_g, lambda_g | always |
| H8  | AP36 | "implies" vs "iff" — write "implies" until converse proved | repeated |
| H9  | AP124, AP125 | Duplicate labels; label prefix must match environment | 15+ |
| H10 | AP6, AP7 | Scope: specify genus, arity, level | always |
| H11 | AP17 | Audit every new theorem before building next result | always |
| H12 | AP121 | No Markdown inside LaTeX (backticks, bold, italic) | repeated |
| H13 | AAP1 | Grep for `antml`, `</invoke>` in every write | always |
| H14 | AP2, AP115 | Read actual .tex, not CLAUDE.md description | always |
| H15 | AP3, AP128 | Never pattern-match across occurrences | 15+ |
| H16 | AP116, AP136 | Summation boundary verification (smallest index) | repeated |
| H17 | AP117 | Connection is r(z)dz, not r(z) d log(z) | repeated |
| H18 | AP118 | Genus-1 scalar collapse: write in full matrix form | repeated |
| H19 | AP120 | Cauchy normalization 1/(2πi), never 1/(2π) | 3+ |
| H20 | AP40, AAP4 | Environment must match tag (conjecture/theorem) | repeated |
| H21 | AP-CY14, AP-CY11 | Vol III default is \begin{conjecture} | repeated |
| H22 | AP113 | Vol III: bare kappa FORBIDDEN, always subscript | always (Vol III) |
| H23 | AP129 | Reciprocal a/b vs b/a — substitute numerical value | 5+ |
| H24 | V2-AP34 | Divided-power lambda-bracket in Vol II (c/12 not c/2) | repeated |
| H25 | AP127 | Migrated-chapter \label stubs and \ref audits | 7+ |

Each of these gets the operational-template block above, ~3 lines per entry, ~80 total lines for HOT ZONE.

---

## 5. Wave 12 Draft Integration Map

This restructure is a receiver for multiple forthcoming Wave 12 drafts. Integration mapping:

| Wave 12 draft | Feeds into new section | Notes |
|---|---|---|
| 12-1 (pre-reading checklist) | §1 | One-page compact form. |
| 12-2 (formula census) | §5 True Formula Census | Canonical formula list with sanity checks; replaces scattered formulas in current §"Key Constants" and per-AP mentions. |
| 12-3 (Opus 4.6 failure-mode doc) | §6 Opus 4.6 Quirks | Verbatim the model-specific failure modes with prompt-level mitigations. |
| 12-4 (LaTeX blacklist) | §8 LaTeX Pitfall Blacklist | Grep-ready commands. |
| 12-5 (pre-edit verification templates) | §7 Pre-Edit Verification Protocol | One template per edit class. |
| 12-6 (hook enforcement audit) | §10 Hook Enforcement Map | Column-by-column AP enforcement status. |
| 12-7 (AP evolution process) | §11 AP Evolution Process | Lifecycle definitions. |
| 12-9 (HOT ZONE slate) | §2 HOT ZONE | The 25 entries above; Wave 12-9 finalizes the operational templates. |
| 12-10 (AP dedup / merge table) | §9 Full AP Catalog reorganization | Drives the §9.1 domain reorganization and the merges in §6 below. |

Wave 12-8 is reserved for cross-volume propagation of the restructure (Vol II and Vol III CLAUDE.md add pointers to the new §5, §6, §8 of Vol I).

---

## 6. AP Consolidation and Dedup Analysis

### 6.1 Duplicates / near-duplicates (merge candidates)

Direct overlaps found in the current 141-AP catalog:

| Merge target | APs merged | Justification |
|---|---|---|
| **M1: r-matrix level** | AP126 + AP141 | AP141 is explicitly "AP126 is systemic"; same failure class, same operational check. |
| **M2: Hardcoded expected values** | AP10 + AAP11 + AP128 + V2-AP28 | All four say "two independent derivation paths or the test and engine share the same wrong mental model". Collapse into one domain entry with four historical examples. |
| **M3: Cross-volume grep after correction** | AP5 + AAP6 + AP12 | All three prescribe "search all three volumes after correction"; AP12 is AP5 scoped to proving a claim. |
| **M4: Kappa-from-memory** | AP1 + AP9 + AP20 + AP24 + AP39 + AP48 + AP136 | Current CLAUDE.md already groups these under "kappa" in the cognitive-trigger view; formalize the merge in the domain view with one master entry and six historical specializations. |
| **M5: Scope / genus / arity** | AP6 + AP7 + AP18 + AP32 | Four APs all saying "specify scope; do not write universal quantifier without verification". |
| **M6: Biconditional caution** | AP36 + (part of) AP138 | AP36 is "implies vs iff". AP138's even-degree Jacobi case is a specific instance of "biconditional that is actually one-directional". |
| **M7: Prose hygiene (AI slop)** | AP106 + AP109 + AP111 + V2-AP29 | Four APs all prohibiting "this chapter constructs", results-before-proof, "what this chapter proves" blocks, and AI-slop vocabulary. Merge into single prose-hygiene block with one grep list. |
| **M8: Environment matches tag** | AP4 + AP40 + AP60 + AAP4 + V2-AP31 + AP-CY11 + AP-CY14 | Seven APs all saying "conjecture environment for unproved; theorem environment only with ProvedHere and matching tag". Merge. |
| **M9: Summation boundary + harmonic** | AP116 + AP136 | Both about summation index boundary checking; AP136 is the specialization to harmonic numbers. |
| **M10: Label hygiene** | AP124 + AP125 + AP127 | Duplicate labels, stale prefixes, migrated-chapter stubs all belong to one "label hygiene" domain entry. |
| **M11: E_inf / E_1 hierarchy (Vol II)** | V2-AP1–V2-AP16 | Sixteen APs all belong to the three-tier picture. Keep the individual entries for historical/archaeological reasons but put them behind one master "E_1/E_inf Hierarchy" anchor that states the three-tier picture once. |
| **M12: Markdown-in-LaTeX** | AP121 + V2-AP26 (Part numerals) + V2-AP32 (standalone artifact leak) | All three are "LaTeX-invisible errors": Markdown syntax, hardcoded Part numerals, standalone artifacts leaking into inputs. Merge into the LaTeX Pitfall Blacklist (§8). |

**Total merge count: 12 merges, consolidating 43 APs into 12 master entries.** Historical APs are preserved as citations under their master entry; the flat-count reduction is from 141+ to ~110 master entries plus historical footnotes.

### 6.2 Candidates for splitting (entries that grew too large)

APs currently exceeding 3 sentences / multi-paragraph entries:

| AP | Current size | Split proposal |
|---|---|---|
| AP1 (kappa operational mandate) | 5 sentences + bold mandate | Split into AP1 (operational mandate, one line) + AP1.a (kappa_eff distinction) + AP1.b (cross-check protocol). |
| AP32 (genus-1 != all-genera) | 4 sentences + bold tag requirement | Split into AP32 (genus scope) + AP32.a (uniform-weight/all-weight tag requirement as a §7 template, not a prose AP). |
| AP126 (level-stripped r-matrix) | 6 sentences | Split into AP126 (the rule) + AP126.a (enforcement via k=0 check) + historical note on 42-instance archaeology. |
| AP136 (harmonic number notation) | 4 sentences | Move the worked example (H_1=1 vs H_2-1=1/2) into §5 formula census; keep AP136 as a one-line "evaluate at smallest N" rule. |
| V2-AP34 (divided power in Vol II) | 4 sentences + explicit examples | Move examples to §5 formula census (Vol II convention row); keep V2-AP34 as a one-line rule. |
| AP-CY14 (unconstructed object) | 4 sentences + bold clause | Split into AP-CY14 (rule) + reference to §9.1.13 kappa-spectrum master entry. |

### 6.3 Dead or near-dead APs (consolidation candidates, not deletion)

Current APs that have fired zero or one times since introduction:

| AP | Reason for dead status | Disposition |
|---|---|---|
| AP28 (undefined qualifier in 3+ locations) | Fired once, at introduction. | Merge into §9.1.10 (LaTeX/labels) as a footnote. |
| AP41 (prose mechanism != math mechanism) | Fired twice. | Merge into §9.1.9 (prose hygiene) as a footnote. |
| AP42 (state level of validity) | Fired once. | Merge into §9.1.4 (scope). |
| AP43 (central object without \begin{definition}) | Fired once, covered by M8. | Subsume into M8. |
| AP78 (never conjecture from number-theoretic coincidences) | Fired once. | Keep as footnote in §9.1.11 (arithmetic). |
| AP101 (qi not merely iso on cohomology is tautological) | Fired twice. | Keep as footnote. |
| AP114 (stub chapters) | Mechanized: now enforced by the stub-chapter grep. | Move to §10 Hook Enforcement Map as an enforced item, not a cultural AP. |

**Retirement count: 7 APs moved from active catalog to footnotes or to §10 enforcement map.** None deleted; all remain searchable.

### 6.4 Net effect on AP count

- Current: 141 numbered APs (AP1–AP141) + 18 AAPs + 35 V2-APs + 19 AP-CYs = **213 total**.
- Proposed after merges and retirements: 213 − 43 (merged under 12 masters) − 7 (retired to footnotes) + 12 (new master entries) = **175 active**, with all 213 preserved as historical references under master entries.

The count reduction is modest but the cognitive load reduction is significant: the agent sees 12 master domain entries in §9.1 instead of 43 scattered entries.

---

## 7. Anchor-Link Strategy

Markdown anchor links in GitHub-flavored / pandoc-flavored markdown:

- Every section heading gets an explicit anchor: `## §2 HOT ZONE {#hot-zone}`.
- Every HOT ZONE slot gets a short anchor: `### H1 r-matrix level {#h1}`, `### H2 kappa memory {#h2}`, etc.
- Every domain section in §9.1 gets an anchor matching the domain name: `#kappa-formulas`, `#r-matrices`, `#grading-signs`, `#scope`, `#bar-complex`, `#four-functors`, `#sc-operad`, `#shadow-hochschild`, `#prose-hygiene`, `#labels-latex`, `#arithmetic`, `#computation-discipline`, `#vol3-kappa-spectrum`, `#aap-meta`.
- Every AP retains a stable anchor `#ap-126`, `#ap-141`, etc. Master entries use `#m1-r-matrix-level`, `#m2-hardcoded-values`, etc.
- Cross-references use the compact form `[AP126](#ap-126)` in prose, and the §9.2 cognitive-trigger index lives as a flat list of `[AP126](#ap-126) -- formula trigger`.
- The §5 Formula Census uses formula-specific anchors: `#census-kappa-km`, `#census-kappa-vir`, `#census-r-matrix-km`, `#census-theta-a`, etc. Chapter prose, compute engines, and tests reference these by anchor in a Census comment.
- Hook Enforcement Map (§10) entries link back to the AP anchor they enforce: `AP126 → pre-commit/check_r_matrix_level.sh → [ap-126](#ap-126)`.

This gives ~300 anchors total. The editor/viewer experience: click any AP number in prose and jump to the master entry; click a formula reference in a chapter and jump to the census.

---

## 8. What Is Preserved Unchanged

To respect the Beilinson principle and the authority of the lived-in document:

- The **Identity** paragraph (§0) stays verbatim.
- The **Beilinson Principle** (§3), including the epistemic hierarchy, stays verbatim.
- **Key Constants** (§4) stays; §5 census is additive, not a replacement. (The census has more formulas, with sanity checks; §4 remains the tight one-paragraph summary.)
- **Theorem Status table** stays verbatim.
- **Regression Safeguards** RS-1 through RS-20 stay verbatim.
- **Writing Standard** (the twelve-voice channel) stays verbatim.
- All AP text is preserved. Merges produce new master entries but historical entries remain searchable under the master.
- The Skills list, Build commands, Session Protocol, LaTeX, and Git sections stay verbatim.
- No AP is deleted. Dead APs are demoted to footnotes under their domain master entry.

---

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| HOT ZONE operational templates drift out of sync with source APs | §11 AP Evolution Process requires updating HOT ZONE whenever the source AP is edited. |
| Formula census becomes yet another source-of-truth in addition to landscape_census.tex | §5 explicitly cites landscape_census.tex as upstream; §5 is a CLAUDE.md-embedded view, not a replacement. |
| Anchor links rot under future renames | Anchors derive mechanically from AP numbers, which are immortal once assigned. Domain anchors are stable. |
| 1.6× length growth pushes CLAUDE.md past the agent's fast-read budget | HOT ZONE is front-loaded; §1 Pre-reading Checklist is 10 lines. The "first 200 lines" experience is strictly denser, not longer. |
| Merges erase AP provenance | Merges preserve original AP numbers as citations under master entries; nothing is forgotten. |
| Retired APs come back | Retirement requires 60 commits without recurrence AND a mechanical enforcement. A retired AP that recurs is un-retired and re-promoted. |
| Cross-volume drift: Vol II and Vol III CLAUDE.md do not mirror the restructure | Wave 12-8 handles cross-volume propagation as a single atomic commit. |

---

## 10. What This Proposal Does NOT Do

- Does not rewrite any AP text.
- Does not change any mathematical statement.
- Does not modify any `.tex` file.
- Does not modify CLAUDE.md. This document lives in `compute/audit/` only.
- Does not introduce new APs. It only reorganizes, merges, and front-loads existing ones.
- Does not add AI attribution anywhere.
- Does not propose retiring any AP to deletion. All APs remain searchable.

---

## 11. Implementation Order (Post-Approval)

If the user approves this proposal, the implementation order is:

1. Wave 12-2 draft (Formula Census) lands in `compute/audit/formula_census_wave12.md`.
2. Wave 12-3 (Opus 4.6 quirks) lands in `compute/audit/opus_quirks_wave12.md`.
3. Wave 12-4 (LaTeX blacklist) lands in `compute/audit/latex_blacklist_wave12.md`.
4. Wave 12-5 (verification templates) lands in `compute/audit/preedit_templates_wave12.md`.
5. Wave 12-6 (hook enforcement audit) lands in `compute/audit/hook_enforcement_wave12.md`.
6. Wave 12-9 (HOT ZONE slate with operational templates) lands in `compute/audit/hot_zone_wave12.md`.
7. Wave 12-10 (AP dedup table with final merges) lands in `compute/audit/ap_dedup_wave12.md`.
8. All seven drafts cross-checked against the current CLAUDE.md (Beilinson loop).
9. A single atomic commit restructures `/Users/raeez/chiral-bar-cobar/CLAUDE.md` using the merged Wave 12 drafts.
10. Wave 12-8 propagates pointers to Vol II and Vol III CLAUDE.md in the same commit.

Builds are NOT run by this proposal. The restructure commit runs `make fast` and `make test` as normal Session Protocol steps.

---

## 12. Summary

- **Proposed section count:** 19 top-level sections (current: 15), with 14 sub-sections in §9 domain reorganization.
- **Proposed length:** ~454 lines, ~14,000 words (current: 285 lines, ~9,000 words). Growth ratio 1.6×.
- **Structural improvements (top 3):**
  1. HOT ZONE with 25 operational-template entries at the top of the file.
  2. True Formula Census as the single source of truth, cited by anchor from everywhere else.
  3. Domain reorganization of the AP catalog, with the cognitive-trigger view preserved as a cross-reference index.
- **Merge candidates identified:** 12 merges consolidating 43 APs into 12 master entries. 7 dead APs demoted to footnotes. Net active count 213 → 175, with all 213 preserved as historical citations.
- **Anchor strategy:** ~300 anchors; every section, every HOT ZONE slot, every AP, every domain, every census formula gets a stable anchor derived mechanically from its immortal identifier.
- **Wave 12 integration:** 12-1 → §1, 12-2 → §5, 12-3 → §6, 12-4 → §8, 12-5 → §7, 12-6 → §10, 12-7 → §11, 12-9 → §2, 12-10 → §9, 12-8 → Vol II/III cross-volume propagation.

This is a structural redesign, not a rewrite. The spirit of the current document — adversarial falsification, epistemic hierarchy, three-volume discipline — is preserved and amplified.
