# REWRITE CONTINUATION PROMPT — Chriss-Ginzburg Forge, Phase 2+

**Date**: 2026-03-13 (updated after session 4)
**Baseline**: 1800pp, 0 build errors, 0 undef refs, 0 overfull boxes, 5984 tests passing
**Session 4 work**: Completed ALL remaining items. Mathematical audit closed (19/19 facts verified, 1 exposition gap noted: prime form K^{-1/2} bundle). T1-5 concordance constitutional audit complete (zero discrepancies). T4-6 w_algebras_deep.tex cross-ref fix (sectorwise finiteness dedup at line 1127). T4-1 scope riders audited (16 instances, all mathematically necessary). T4-2 prop chains audited (yangians.tex cascading results are mathematical backbone). T4-6 yangians.tex E₁-factorization verified distinct. All Tier 5/6 verified. **All items now ✅.**
**Session 3 work**: introduction.tex scope dedup (T1-2, merged rem:two-strata into governing remark), feynman_diagrams.tex full restructuring (T1-4: fused chiral-field-theory definition with bar connection, compressed loop number conjecture to remark, fused three off-shell/on-shell/pairing sections into one, merged duplicate Kontsevich remarks, removed triplicate formality remark — net ~6 pages compression), Tier 3 mechanism sentences (T3-1 chiral_modules, T3-4 configuration_spaces, T3-5 chiral_koszul_pairs, T3-6 w_algebras_framework, T3-7 deformation_examples, T3-11 free_fields chapter title rename), Tier 4 patterns (T4-4 constitutional notes 8 files compressed, T4-5 verified hypotheses correctly inside theorem environments), mathematical audit (12 CLAUDE.md critical facts verified correct across manuscript)
**Session 2 work**: beta_gamma.tex portrait complete (BG-1/2/3/4/5), kac_moody_framework.tex sl₂ portrait + floating labels (KM-1/2), detailed_computations.tex mechanism framing (DC-1/2), introduction.tex frontier compression (T1-1) + 10 floating labels removed, ~50 dead HMS/boilerplate labels batch-removed across all chapters, w_algebras_deep.tex bridge remark, yangians.tex MC3 cluster preamble, scope qualifier audit documented, loose amalgamation audit documented
**Prior work (session 1)**: Governing questions rewritten (5 files), HMS boilerplate compressed (50 files), `$`→`\[...\]` (41 files, 1616 pairs), floating labels fixed (6 files), frontier deduplication (4 files), beta_gamma.tex governing question + mechanism framing (2 edits)

---

## ORIENTATION FOR THE EXECUTOR

You are rewriting a 1806-page mathematics monograph into its Platonic ideal form. The standard is Chriss-Ginzburg's *Representation Theory and Complex Geometry*: every sentence carries structural weight, definitions serve theorems, proofs reveal geometric mechanism before algebraic verification, examples are portraits not drills.

### The Epistemic Stance

**Do not assume the mathematics is correct.** Every `\ClaimStatusProvedHere` is an aspiration in the process of being born, not a settled fact. Every "proof" is a candidate proof. When you rewrite a passage, you are simultaneously:
1. Improving its prose quality (mechanism-first, no dead weight)
2. Stress-testing its mathematical content (does the proof actually prove what it claims? does the theorem statement match what's established in the proof? are the hypotheses sufficient?)
3. Checking it against the CLAUDE.md Critical Pitfalls (the 11 verified fact families that, if violated, corrupt the manuscript)

When you find a mathematical issue during rewriting: **do not silently fix it**. Flag it explicitly with `% REWRITE-AUDIT: [description]` so it can be tracked. If the fix is clear, apply it AND flag it. If the fix requires research, flag only.

### Ground Truth Hierarchy

1. **CLAUDE.md Critical Pitfalls** — Sacred. Verified facts. If the manuscript contradicts these, the manuscript is wrong.
2. **concordance.tex** (Chapter 34) — The constitution. When earlier chapters disagree, concordance is right.
3. **compute/tests/** — Computational ground truth. 5984 tests encode specific numerical values.
4. **The proofs themselves** — Each proof must be checked for: (a) all hypotheses used, (b) correct sign conventions, (c) no circular reasoning, (d) complete (not "the proof is similar").

### Build Discipline

After every batch of 5-10 edits:
```bash
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; scripts/build.sh 1
```
Check: 0 errors, 0 undef refs, 0 undef cits, 0 overfull. If any appear, fix before proceeding.

### Anti-Patterns (from prior sessions — these actually happened)

| Trap | Description | Antidote |
|------|-------------|---------|
| **Cosmetic** | Rearranging words without changing substance | Ask: "Does the reader's understanding change?" If no, don't touch it. |
| **Expansion** | Adding 3 sentences to "explain" what 1 sentence said | The goal is compression. Net line count should decrease or hold. |
| **Deference** | Treating `ProvedHere` as gospel | Read the proof. Does it actually establish the claim? |
| **Hallucination** | Inventing a formula that "should" be there | Never guess. Compute or cite. Every formula in CLAUDE.md Critical Pitfalls was verified. |
| **Context drain** | Trying to rewrite 50 files in one conversation | Work in batches of 3-5 files. Build-test between batches. |
| **Uniformity** | Making every chapter sound the same | Each chapter has a different mechanism. The governing question should name THAT chapter's mechanism. |
| **Scope creep** | Adding new theorems/definitions during rewrite | REWRITE not ADD. If a theorem is missing, flag it with `% REWRITE-AUDIT: missing theorem`. |

### Quality Test

After rewriting a section, ask: Would a reader who has never seen this material feel the *inevitability* of the result? Could they reconstruct the geometric mechanism from the prose alone, before reading the proof? If not, the rewrite has not succeeded.

### Exemplary Sections (the standard to match)

Read these before rewriting anything — they ARE the Platonic form:
- `chapters/frame/heisenberg_frame.tex:1-80` — Entry atom. Mechanism-first.
- `chapters/theory/bar_cobar_construction.tex:1-80` — Nilpotence-periodicity. THIS is the standard.
- `chapters/examples/genus_expansions.tex:1-80` — Free energy theorem. Clean theorem-proof-remark.
- Introduction: "The logarithmic seed" (lines 415-533), "The four theorems" (lines 536-620), "Five geometric ingredients" (lines 929-990), "DK square" (lines 992-1019), "Master functorial correspondence" (lines 1021-1074)

---

## THE WORK — ORGANIZED BY TIER

Items marked ✅ are completed. All others are open.

---

### TIER 0 — IN PROGRESS (beta_gamma portrait rewrite)

These were actively being executed when context ran out.

#### BG-2: Remove PATCH 041 duplicate in beta_gamma.tex ✅

**File**: `chapters/examples/beta_gamma.tex`
**Lines**: 402-543 (§5 "Beta-gamma systems")
**Problem**: Lines 402-543 are a PATCH 041 block that duplicates content from §1-§4. The section header "Beta-gamma systems" creates a confusing duplicate TOC entry. Inside the patch:
- Lines 411-413: Physical motivation remark — unique sentence about λ=2 BRST ghosts
- Lines 415-434: `const:geometric-beta-gamma` (K_X^λ ⊗ L bundle formulas + special cases) — UNIQUE, not in §4
- Lines 437-448: `def:beta-gamma-ope-complete` — PURE DUPLICATE of lines 23-27
- Lines 450-464: `prop:beta-gamma-modes` (mode expansions) — UNIQUE, not in §1
- Lines 466-477: `thm:beta-gamma-stress` (stress tensor + central charge formula) — EXPANDS lines 29-32
- Lines 479-496: `comp:beta-gamma-central-charges` (central charge table) — UNIQUE
- Lines 498-519: `thm:beta-gamma-bar` (geometric bar construction) — UNIQUE formulation (FM version)
- Lines 521-529: Wakimoto remark — UNIQUE
- Lines 531-543: `thm:beta-gamma-universal` (universal property) — UNIQUE

**Action**:
1. Migrate `const:geometric-beta-gamma` (lines 415-434) to §4 (Geometric realization, before line 387)
2. Migrate `prop:beta-gamma-modes` (lines 450-464) to §1 (after the OPE at line 27)
3. Replace the thin stress tensor at lines 29-32 with `thm:beta-gamma-stress` content (lines 466-477)
4. Migrate `comp:beta-gamma-central-charges` (lines 479-496) to §1 after stress tensor
5. Migrate `thm:beta-gamma-bar` (lines 498-519) to §2 (before thm:betagamma-complete-bar at line 40)
6. Migrate Wakimoto remark (lines 521-529) and `thm:beta-gamma-universal` (lines 531-543) to §4
7. Remove the PATCH 041 section shell (lines 402-413, 436-448, and the `%===` banner comments)
8. Update the §6 reference at line 553 ("extends the computation of \S\ref{sec:beta-gamma-complete-analysis}") to point to §2

**Cross-refs to preserve**: `def:beta-gamma-ope-complete` (→ notation_index.tex:390), `const:geometric-beta-gamma` (→ same file line 845), `thm:beta-gamma-stress` (→ same file line 898), `comp:beta-gamma-central-charges` (→ genus_expansions.tex:2028)

**Mathematical audit during rewrite**:
- Verify stress tensor formula T = (1-λ)(β∂γ) - λ(∂β·γ) matches CLAUDE.md conventions
- Verify central charge c_βγ = +2(6λ²-6λ+1) matches thm:beta-gamma-stress AND comp:beta-gamma-central-charges
- Verify c_bc = -c_βγ (sign reversal for Koszul dual)
- Check: is the universal property (thm:beta-gamma-universal) correctly stated? "Free vertex algebra generated by two fields with single relation" — is this FBZ04's actual statement?

#### BG-3: Deduplicate Koszul dual proof ✅

Compressed thm:betagamma-bc-koszul-detailed from 60-line re-proof to proposition (central charge complementarity only). References thm:betagamma-fermion-koszul. Cross-ref to rem:km-central-charge-sum for KM contrast.

#### BG-5: Geometric interpretation enrichment ✅

Added rem:bundle-bar-mechanism connecting Serre duality pairing K_X^λ ⊗ K_X^{1-λ} → K_X to bar differential. Updated configuration space picture with FM compactification + bundle notation. Removed stale sec:beta-gamma-complete-analysis label. Fixed §6 cross-ref → subsec:bar-cobar-verification.

---

### TIER 1 — Heavy Structural Rewrites (highest impact)

#### T1-1: introduction.tex lines 70-413 — Compress frontier detail ✅

Compressed 22 lines → 7 lines (session 2). Lines 264-402 are now clean mathematical structure (theorem + proof + remark + diagram). No duplication remains.

#### T1-2: introduction.tex — Deduplicate scope remarks ✅

Merged rem:two-strata (Scope remark, formerly at line 369) into governing remark (lines 55-64). The label rem:two-strata is preserved (4 external cross-refs from concordance.tex, coderived_models.tex, introduction.tex). The standalone Scope remark removed.

#### T1-3: introduction.tex — Cut defensive hedging ✅

Already removed in a prior session — the text "On the present theorem surface this hierarchy is not programme prose..." no longer exists in any .tex file.

#### T1-4: feynman_diagrams.tex — Full restructuring ✅

**Net compression**: ~6 pages (1806→1800pp). Major structural edits:
1. Fused "Chiral field theory data" definition with "Connection to bar complex" remark into one compressed definition (def:worldline-intro preserved). Cut ~40 lines of verbose physics framing.
2. Compressed "Configuration space interpretation" from conjecture+evidence (25 lines) to remark (7 lines). Loop number = Betti number is standard; codimension interpretation kept as informal.
3. Fused three sections (Bar=off-shell, Cobar=on-shell, Pairing=S-matrix) into ONE section "Off-shell/on-shell duality" with combined Feynman rules dictionary table (conj:physical-pairing preserved). Cut ~120 lines down to ~40.
4. Merged two duplicate Kontsevich formality remarks (rem:kontsevich-graphs preserved). Removed triplicate formality remark (rem:kontsevich-worldline, 0 external refs).
5. Removed graph complex evidence block (restated dictionary from conjecture) and verbose scope remark.
**Mathematical audit**: All Heuristic claims correctly marked. MC5 local packet chain (lines 428-733) preserved intact (heavily cross-referenced from concordance.tex).

#### T1-5: concordance.tex — Constitutional status audit ✅

**Status verified** (sessions 3-4):
- MC1 proved (standard finite-type interacting families) ✓
- MC2 fully resolved (all 3 packages) ✓
- MC3 eval-gen core proved (DK-0/1/1½/2/3, all simple types); extension conjectural ✓
- MC4 M-level done, H-level frontier ✓
- MC5 downstream of MC3/MC4 ✓
- DK ladder: 0✓ 1✓ 1½✓ 2/3✓(eval-gen core) 4(ML proved, alg id open) 5(conj) ✓
- Theorem status table (A_mod, B_mod, C_mod, Index, DK, H): all match CLAUDE.md ✓
- Nine-futures table: correctly annotated ✓
- "Three of four" stale text: already fixed (prior session) ✓
- Prose quality: appropriate for constitutional chapter (precise, authoritative) ✓
- **Zero discrepancies found.** No `% REWRITE-AUDIT` flags needed.

---

### TIER 2 — Portrait Rewrites (moderate effort, high prose impact)

#### T2-1: kac_moody_framework.tex — sl₂ portrait synthesis ✅

Added rem:sl2-portrait with 3-item enumeration: (1) level shift as curvature mechanism, (2) critical level as curvature-free locus, (3) central charge non-cancellation contrast with βγ/bc. Cross-refs thm:betagamma-bc-koszul-detailed.

#### T2-2: kac_moody_framework.tex — Fix floating labels ✅

Replaced 4 stale rem: labels (km-atom, km-status, km-hms, km-route) with single sec:km-bar-complex. All 4 had 0 references.

#### T2-3: detailed_computations.tex — Arnold relation mechanism ✅

Added mechanism paragraph after comp:heisenberg-deg3-full: pole-order argument (d_bracket = 0 because no simple pole), Arnold relation constrains form-space dimension but does not participate in the differential. Also removed floating label rem:detailed-hms.

#### T2-4: detailed_computations.tex — Harrison subcomplex ✅

Already portrait-quality. Lines 125-136 correctly identify: Harrison shuffle antisymmetry turns convolution into commutator; [a_{-m}, a_m] = κm IS the curvature m₀. No edit needed.

---

### TIER 3 — Mechanism Sentences (15-30 min each, systematic)

Each item below requires: (1) Read the chapter opening, (2) Write a 1-3 sentence mechanism statement, (3) Verify it doesn't contradict CLAUDE.md.

| Item | File | Status | Action taken |
|------|------|--------|--------------|
| T3-1 | chiral_modules.tex | ✅ | Governing Q: added "bar differential on modules detects extensions via collision residues" |
| T3-2 | chiral_modules.tex | ✅ | Floating label fixed (session 2) |
| T3-3 | configuration_spaces.tex | ✅ | Floating label fixed (session 2) |
| T3-4 | configuration_spaces.tex | ✅ | Governing Q: "FM encodes all collision patterns; Arnold relation is a residue theorem on that boundary and is the genus-0 reason d²=0" |
| T3-5 | chiral_koszul_pairs.tex | ✅ | Governing Q: "Chiral Koszul pairs exist because configuration space residues respect operadic quadratic structure" |
| T3-6 | w_algebras_framework.tex | ✅ | Governing Q: "DS reduction is quantum gauge-fixing: the BRST complex of a constrained WZW model at nilpotent f" |
| T3-7 | deformation_examples.tex | ✅ | Governing Q: P∞/coisson distinction per CLAUDE.md. Coisson → E∞ (singly quantum), P∞ → E₁ (doubly quantum). |
| T3-8 | hochschild_cohomology.tex | ✅ | Verified: SBI sequence presented algebraically (correct for this algebraic chapter); geometric interpretation (clutching+trace) lives in higher-genus chapters. No edit needed. |
| T3-9 | en_koszul_duality.tex | ✅ | Already mechanism-first: names propagator dimension shift, Totaro relations, different operadic structures. No edit needed. |
| T3-10 | bv_brst.tex | ✅ | Already mechanism-first: "bar complex is the BRST complex, BV antibracket is Verdier duality on configuration spaces." No edit needed. |
| T3-11 | free_fields.tex | ✅ | Chapter title: "Examples" → "Free field atoms". Labels fixed (session 2). |

---

### TIER 4 — Systematic Patterns (batch-processable)

#### T4-1: Pattern E — Post-hoc scope qualifiers (strike #96-100) ✅

**Audit result** (session 4): Grepped all 4 search patterns across all .tex files. Found 16 instances total (14 "evaluation-generated core", 2 "theorematic domain", 0 others). All are mathematically necessary — they appear in theorem statements specifying the domain of validity, proof explanations referencing which locus a result holds on, or status assessments in concordance.tex. None are editorial padding. No removals warranted.

#### T4-2: Pattern F — Repeated proposition references (strike #101-110) ✅

**Audit result** (session 4): In introduction.tex, lines 264-402 are clean theorem-proof-remark-diagram structure (no duplication after T1-1 compression). In yangians.tex, the proposition/corollary chains (lines 769-2958) are cascading mathematical results: each proposition narrows scope and adds new input toward MC4 resolution. These are the mathematical backbone of the DK-4 argument, not duplicated prose. No changes warranted.

#### T4-3: Pattern G — "This is new" claims ✅

**Audit result**: All 6 instances are inside proper attribution remarks (itemizing which ingredients are from literature vs. original). This is standard mathematical writing. No changes needed.

#### T4-5: Post-hoc scope qualifiers (from agent audit) ✅

**Verified** (session 3): All cited hypotheses are correctly formulated inside their theorem environments. The "Assume..." phrasing appears within theorem/proposition statement bodies (standard mathematical writing), not as external prose.

#### T4-6: Loose amalgamation bridges (from agent audit) ✅

**w_algebras_deep.tex** ✅ (bridge at line 465 added): finite-type → W∞ transition
**yangians.tex** ✅ (bridge at line 8033 added): preamble before 4-definition MC3 cluster

**Remaining** ✅ (session 4):
- `w_algebras_deep.tex:1122-1142`: Replaced re-description of sectorwise finiteness setup with cross-reference to Step 1 (Computation~\ref{comp:w-bar-dims}). Build verified.
- `yangians.tex:6425 vs 8037`: Two distinct definitions — `def:e1-factorization-category` (concrete, enumerated) vs. `def:ordered-e1-factorization` (abstract ∞-categorical wrapper that explicitly references the first). No duplication.

#### T4-4: Pattern I — Constitutional notes (strike #126-130) ✅

**Problem**: "Constitutional note: Chapter 34 (concordance.tex) is the normative status ledger..." appears as LaTeX comments at file tops, but inconsistently.
**Action**: The `% Status and semantic-level disputes...` line at the top of each file already handles this. Remove any separate "Constitutional note" comments that duplicate it.

---

### TIER 5 — Remaining Part II ✅ (all verified session 3-4)

| Item | Status | Result |
|------|--------|--------|
| T5-1 | ✅ | genus_expansions: governing Q + opening paragraph already portrait-oriented |
| T5-2 | ✅ | toroidal_elliptic: lines 16-24 already explain WHY directions are separate |
| T5-3 | ✅ | deformation_quantization: line 14 already says what Kontsevich gives |
| T5-4 | ✅ | minimal_model_fusion: intentional \input (continues W-algebra chapter) |
| T5-5 | ✅ | minimal_model_examples: intentional \input (continues W-algebra chapter) |

---

### TIER 6 — Part III Remaining ✅ (all verified session 3-4)

| Item | Status | Result |
|------|--------|--------|
| T6-1 | ✅ | physical_origins: governing Q names the translation mechanism |
| T6-2 | ✅ | kontsevich_integral: governing Q already names universal Vassiliev + config space + log form |
| T6-3 | ✅ | derived_langlands: DK scope matches concordance (no DK-2/3 refs in this chapter) |

---

### TIER 7 — Already Completed ✅

| Item | Description | Status |
|------|-------------|--------|
| ✅ | HMS boilerplate compression (50 files) | Done — all chapters + appendices |
| ✅ | `$` → `\[...\]` replacement (41 files, 1616 pairs) | Done — 0 `$` remaining |
| ✅ | Floating label fixes (configuration_spaces, chiral_modules, poincare_duality, free_fields, deformation_examples, lattice_foundations) | Done |
| ✅ | Frontier deduplication (physical_origins, holomorphic_topological, genus_complete, bv_brst) | Done — MC4/MC5 reprints → concordance cross-refs |
| ✅ | Governing question rewrites: algebraic_foundations, w_algebras_deep | Done |
| ✅ | BG-1: beta_gamma.tex governing question mechanism | Done |
| ✅ | BG-2: beta_gamma.tex PATCH 041 removal | Done — unique content migrated to §1/§4 |
| ✅ | BG-3: beta_gamma.tex Koszul dual proof dedup | Done — compressed to central charge proposition |
| ✅ | BG-4: beta_gamma.tex bar complex mechanism framing | Done |
| ✅ | BG-5: beta_gamma.tex geometric enrichment | Done — bundle-bar mechanism + FM notation |
| ✅ | KM-1/2: kac_moody_framework sl₂ portrait + floating labels | Done |
| ✅ | DC-1/2: detailed_computations Arnold + Harrison mechanism | Done |
| ✅ | Introduction floating labels cleanup (10 unreferenced labels removed) | Done |
| ✅ | Introduction frontier compression (T1-1): 22 lines → 7 lines | Done |
| ✅ | ~50 dead HMS/boilerplate labels batch-removed (all chapters) | Done |
| ✅ | w_algebras_deep.tex bridge remark (finite-type → W∞ transition) | Done |
| ✅ | yangians.tex MC3 cluster preamble (4-definition bridge) | Done |
| ✅ | Scope qualifier audit (T4-5): 15 instances documented | Done (documentation) |
| ✅ | Loose amalgamation audit (w_algebras_deep + yangians §25.9) | Done (documentation + fixes) |
| ✅ | Pattern G "This is new" audit (T4-3): all 6 instances appropriate | Done |
| ✅ | KM governing question (kac_moody_framework) | Done — Feigin-Frenkel involution named |
| ✅ | DC governing question (detailed_computations) | Done |
| ✅ | T1-2: introduction.tex scope dedup (rem:two-strata merged into governing remark) | Done (session 3) |
| ✅ | T1-3: introduction.tex defensive hedging (already removed) | Done |
| ✅ | T1-4: feynman_diagrams.tex full restructuring (~6pp compression) | Done (session 3) |
| ✅ | T3-1/4/5/6/7/11: Mechanism sentences (6 chapters edited) | Done (session 3) |
| ✅ | T3-8/9/10: Mechanism sentences (3 chapters verified already good) | Done (session 3) |
| ✅ | T4-4: Constitutional notes compressed (8 files, 4-line→1-line) | Done (session 3) |
| ✅ | T4-5: Post-hoc scope qualifiers verified (hypotheses inside theorem envs) | Done (session 3) |
| ✅ | T5-1/2/3: Tier 5 portraits verified | Done (session 3) |
| ✅ | T5-4/5: minimal_model files — intentional \input, no \chapter needed | Done (session 3) |
| ✅ | T6-1/2/3: Tier 6 chapters — governing Qs already mechanism-first | Done (session 3) |
| ✅ | Mathematical audit: all 12 critical facts verified correct | Done (session 3) |
| ✅ | T4-1: Scope riders audited (16 instances, all mathematically necessary) | Done (session 4) |
| ✅ | T4-2: Proposition chains audited (yangians cascading results = math backbone) | Done (session 4) |
| ✅ | T4-6: w_algebras_deep.tex sectorwise finiteness cross-ref (line 1127) | Done (session 4) |
| ✅ | T4-6: yangians.tex E₁-factorization verified distinct (def vs ordered def) | Done (session 4) |
| ✅ | T1-5: Concordance constitutional audit — all MC/DK/theorem status verified | Done (session 4) |
| ✅ | Mathematical audit: remaining 7 facts verified correct (session 4 batch) | Done (session 4) |

---

## MATHEMATICAL AUDIT CHECKLIST ✅ (ALL 19 FACTS VERIFIED)

All 19 critical mathematical facts verified correct across the entire manuscript. Zero errors. One minor exposition gap (prime form K^{-1/2} bundle exponent not explicitly stated).

### Koszul Duality Facts (CLAUDE.md §Koszul Duality)
- [x] Com^! = Lie (NOT coLie) — verified: 6 locations, all correct
- [x] Heisenberg NOT self-dual: H^! = Sym^ch(V*), NOT H_{-k} — verified: 6 locations, all correct
- [x] Free fermion: F^! = beta-gamma (Lie↔Com duality), NOT Heisenberg — verified: 3 locations, all correct
- [x] bc-betagamma is 2-generator duality (dim V=2) — verified correct
- [x] CHIRAL KOSZULNESS ≠ CLASSICAL — verified: lem:operadic-koszul-transfer properly documents transfer hypotheses
- [x] Bar differential: d_bracket² ≠ 0 on the nose; full d satisfies d²=0 — verified: bar_cobar_construction.tex:634 (d_bracket²≠0 explicit), thm:bar-nilpotency-complete (d²=0 proved). No false claims.
- [x] PBW SS does NOT automatically degenerate at E₃ for "quadratic OPE" — verified: heisenberg_frame.tex:2076-2087 rem:frame-pbw-warning explicitly warns "the claim 'quadratic OPE implies E₂ collapse' is FALSE for W-algebras"

### Central Charges (CLAUDE.md §Central Charges)
- [x] Sugawara: c = k·dim(g)/(k+h∨) — verified: 4 locations, all correct
- [x] Sugawara UNDEFINED at critical level — verified: 5 locations, all say "undefined" not "diverges"
- [x] Feigin-Frenkel: k ↔ -k-2h∨ (NOT -k-h∨) — verified: 6 locations, all correct
- [x] Virasoro DS: c = 1 - 6(k+1)²/(k+2) — verified: 9 locations, all correct
- [x] W₃ DS: c = 2 - 24(k+2)²/(k+3) — verified: 8 locations, all correct
- [x] KM periodicity: 2h (Coxeter), NOT 2h∨ (dual Coxeter) — verified: derived_langlands.tex, combinatorial_frontier.tex
- [x] h∨(g∨) = h∨(g) ONLY for simply-laced — verified: existence_criteria.tex, detailed_computations.tex properly qualify

### Curved A∞ (CLAUDE.md §Curved A-infinity)
- [x] m₁²(a) = [m₀,a] (COMMUTATOR) — verified: 3 locations, all correct
- [x] Bar differential always d²=0; curvature shows as m₁² ≠ 0 — verified: thm:bar-nilpotency-complete, homotopy_transfer.tex:744

### Geometry (CLAUDE.md §Geometry)
- [x] FM = Bl (blowup along diagonals), NOT X^n\Δ — verified: configuration_spaces.tex, homotopy_transfer.tex, signs_and_shifts.tex
- [x] Prime form E(z,w) is section of K^{-1/2} ⊠ K^{-1/2} — ⚠ K exponent not explicitly stated (exposition gap, no contradiction)
- [x] Normal bundle N_{Δ_S/X^n} = ⊕ T_X (tangent), NOT T_X* — verified: configuration_spaces.tex:3125, signs_and_shifts.tex:672

### Physics (CLAUDE.md §Physics Formulas)
- [x] QME: ℏΔS + (1/2){S,S} = 0 (factor 1/2) — verified: 5 locations in bv_brst.tex + concordance.tex
- [x] W₃ composite: Λ = :TT: - (3/10)∂²T (MINUS sign) — verified: 15+ locations, all correct
- [x] Virasoro central extension is Lie algebra 2-COCYCLE — verified: 4 locations, all correct

---

## EXECUTION ORDER (recommended)

1. ~~**Finish beta_gamma.tex**~~ ✅ All BG items complete
2. ~~**kac_moody_framework.tex**~~ ✅ T2-1, T2-2 complete
3. ~~**detailed_computations.tex**~~ ✅ T2-3, T2-4 complete
4. ~~**introduction.tex**~~ ✅ T1-1 done (session 2), T1-2 done (session 3), T1-3 already removed
5. ~~**feynman_diagrams.tex**~~ ✅ T1-4 done (session 3, ~6pp compression)
6. ~~**Tier 3 mechanism sentences**~~ ✅ 6 of 11 edited, 3 already good, 2 floating-label-only (done in session 2)
7. ~~**Tier 4 systematic patterns**~~ ✅ T4-1 scope riders verified, T4-4 constitutional notes compressed, T4-5 hypotheses verified
8. ~~**concordance.tex audit**~~ ✅ T1-5 complete: MC1-5, DK ladder, theorem table all verified correct vs CLAUDE.md; prose appropriate for constitutional chapter
9. ~~**Tiers 5-6**~~ ✅ All items verified (T5-1/2/3 already good, T5-4/5 intentional \input, T6-1/2/3 already good)
10. ~~**Mathematical audit checklist**~~ ✅ All 19 critical facts verified correct (sessions 3-4). One exposition gap: prime form K^{-1/2} bundle exponent not explicitly stated.

---

## GIT PROTOCOL

All commits authored by Raeez Lorgat. No AI attribution anywhere. No "co-authored-by", no "generated by". This is a HARD RULE from CLAUDE.md.

When committing after a batch:
```
git add [specific files]
git commit -m "rewrite(chriss-ginzburg): [description of batch]"
```

---

## SESSION MANAGEMENT

Each conversation should:
1. Start by reading this file + CLAUDE.md + concordance.tex
2. Pick up from where the last session left off (use the ✅ markers)
3. Work through 3-5 files per session
4. Build-test after each batch
5. Update this file: mark completed items ✅, add any new findings
6. Save session state to `notes/autonomous_state.md`

If context runs out mid-rewrite: the most recent work is tracked by the ✅ markers in this file and by git status.
