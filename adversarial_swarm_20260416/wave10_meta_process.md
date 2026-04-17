# Wave 10 — Meta-Process Audit (Vol I)

**Date:** 2026-04-16
**Auditor mode:** Read-only adversarial referee
**Target:** Vol I orchestration surface — `CLAUDE.md`, `AGENTS.md`, `README.md`, `Makefile`, `archive/`, `audit_campaign_*`, `elite_rescue_*`, `final_gaps_*`, `adversarial_swarm_20260416/`
**Posture:** HEAL toward strongest correct statement; downgrade only when no upgrade path exists

---

## Executive summary

Vol I has the most mature orchestration layer of the three volumes (139,568 tests; 3,726 engines; AGENTS.md exists; Makefile already exposes `verify-independence`). It is also the most bloated: `CLAUDE.md` is 1,073 lines (vs Vol III's freshly-compressed 629), `AGENTS.md` is 759 lines, and the campaign-directory landscape contains ~40 directories from prior audit/rescue cycles, of which roughly half are empty zero-byte stubs from failed agent launches. The compression and disk-hygiene opportunity is large; the more important meta-process gap is that **no machine check enforces the orchestration invariants** that AGENTS.md and CLAUDE.md spend 1,800+ lines describing. The Makefile has `verify-independence` and `verify` (an undocumented anti-pattern script), but no `claudemd-lint`, `stubs-audit`, `regression-rate`, or `concurrency-guard` target. Rules that fix repeat failure modes ("AP1: never write kappa from memory"; "FM44: batches of 3") have the same epistemic status as the rules they replaced ("always verify"): aspirational, not enforced.

The single highest-leverage upgrade is to convert the prose anti-patterns into grep-as-CI: every blacklist regex (B1-B85), every banned token, every Hot Zone trigger should be a make target that exits non-zero when violated. The infrastructure for this already exists in `scripts/verify_edit.sh --all`; it is not wired into pre-commit hooks or into a `make ci` target. Five additional Makefile targets (Section 8) would close ~70% of the regression rate documented in Section 5.

---

## Section 1 — CLAUDE.md compression candidate

**Current state:** 1,073 lines, 97 KB, 46,873 tokens (read in three slices since it exceeds Read tool's 25K-token single-call cap).

**Cross-volume duplication audit:**

| Block | Vol I lines | Duplicated where | Compression action |
|-------|-------------|------------------|-------------------|
| HZ-IV "Independent Verification Protocol" | ~100 (L191-291) | Verbatim in Vol III HZ3-11 | Move to `notes/INDEPENDENT_VERIFICATION.md`, replace with 6-line pointer |
| AP-CY62 — AP-CY67 (geometric/algebraic Hochschild) | ~70 (L1026-1070) | Identical text in Vol III AP-CY62..67 | Replace with `Read notes/cross_volume_aps.md` pointer (this file already exists per L445) |
| Vol II/III status capsule (L987-991) | ~10 | Stale snapshot of Vol III state | Compress to "see ~/calabi-yau-quantum-groups/CLAUDE.md" |
| AP186-AP233 wave-12 catalogue | ~10 (L709-715) | Pointer already says full at `compute/audit/new_antipatterns_wave12_campaign.md` | Already compressed; OK |
| Forbidden Formulas B1-B85 | ~135 (L335-444) | Mostly mirrored in AGENTS.md L213-302 (B1-B73) | Keep canonical in CLAUDE.md, in AGENTS.md replace duplicate with pointer |
| FM1-FM46 catalogue | ~75 (L467-521) | Subset (FM24, FM42-46) duplicated verbatim in Vol III CLAUDE.md L1015-1037 | Keep canonical in Vol I; Vol III pointer is fine |

**Total compression possible:** ~250 lines lossless (1,073 → ~825 = 23% reduction). This is comparable to Vol III's 859 → 629 (26.8%).

**Stale APs** (no longer fire per recent waves):
- AP146 ("expect follow-up commit for stragglers after 100+ agent campaigns") — meta-prose, not actionable. Move to FRONTIER.md or delete.
- AP43 ("Central object without `\begin{definition}` -> property list is conjecture") — has not fired in waves 1-9 of current swarm. Candidate for archival.
- AP127 ("Migrating `\input{chapter}`: add `\phantomsection\label{}` stubs") — V2-AP38 in Vol II already covers; merge.
- RS-1 through RS-20: per L962, "RS-1,2,5,6,7,8,11,16,17,18,20 merged into corresponding APs. AP16 superseded by AP27." Half this section is stale by the file's own admission. Drop the named-but-merged RS list entirely (keep only RS-3, RS-4, RS-9, RS-10, RS-12, RS-13, RS-14, RS-15, RS-19).

**NEW APs not yet captured (from waves 1-9 of current swarm):**
- **AP-NEW-1 (BP arithmetic).** P0-1 from MASTER_PUNCH_LIST: `kappa(BP_k) = c(BP_k)/6` with arithmetic `1 - 4/3 - 4/3 + 1/2 = 1/6` is wrong (`= -7/6`). The fact that this survived "verified clean" cache (per README L86 "First-principles cache, cross-programme enforcement verified clean") means the cache audited a label, not the arithmetic. Codify as "AP-CACHE-LABEL-VS-ARITHMETIC: a verified cache entry asserts a label, not the formula behind it; arithmetic must be recomputed."
- **AP-NEW-2 (Convention bridge falsity).** P0-5 from MASTER_PUNCH_LIST: `k Ω_trace = Ω/(k+h^v)` is dimensionally inconsistent. Documented in 5 files. Existing AP-RMATRIX (L449) covers level-prefix but does not flag false bridge identities. Add subitem: "When two conventions are bridged, dimensional check at k=0 AND k=-h^v MANDATORY."
- **AP-NEW-3 (Tautological internal verification).** P2-4 from MASTER_PUNCH_LIST: `mc_recursion_rational` and `sqrt_ql_rational` are algebraically identical, both restatements of `H² = t⁴ Q`. The "two independent methods" pattern in `compute/lib/shadow_tower_ope_recursion.py` is the Vol I analog of the Vol III tautological-test failure that motivated the entire HZ-IV protocol. The protocol in CLAUDE.md L191-291 is described as cross-volume but the snapshot (L286-289) shows Vol I coverage at 0/2275. **The protocol is installed but not exercised in Vol I.** Add: "AP-VERIFICATION-NOT-EXERCISED: an installed protocol with 0% coverage is a documentation artifact, not infrastructure."
- **AP-NEW-4 (Coincidental agreement masks bugs).** AP186-Opus already exists (L520-521) but only as one-line gloss. P2-3 of MASTER_PUNCH_LIST shows this: `kappa_T = c/2` and `kappa = c/6` both appear in same paper without bridge — the agreement at one specific value (κ_T = c/2 is the Virasoro normalization which equals c/6 only when... never) was not noticed because both formulas were computed in isolation. Promote AP186 to top-of-section status; current placement in middle of "Computational" subsection buries it.

**Files in CLAUDE.md path that should be retired or moved:**
- L598 reference: "Vol III default: `\begin{conjecture}` regardless." — This is the Vol III rule, not Vol I. Move to Vol III file. (Vol I default per L57-62 is `\begin{theorem}` for proven, `\begin{proposition}` for supporting; the line is misplaced.)
- L23 reference: "north star: platonic_ideal_reconstituted_2026_04_13.md" — verify this file still exists and is current; if it has been superseded, fix the pointer.

**Compression bottom line:** Yes, Vol I CLAUDE.md is bloated like Vol III's was. ~250 lines (23%) lossless reduction available; an additional ~100 lines could go if AP-CY62-67 are pointer-only and the merged-RS prose is dropped. Target: 700-750 lines.

---

## Section 2 — AGENTS.md audit

**Current state:** 759 lines, 51 KB. Identifies as "always-on operating constitution for Codex/GPT-5.4". Distinct from CLAUDE.md (described as "encyclopedic atlas").

### 2(a) — Agent invocation, prompt structure, parallelism

AGENTS.md L30-45 specifies the GPT-5.4 prompt architecture (`<task>`, `<structured_output_contract>`, `<verification_loop>`, etc.). This is reasonable and matches the Codex skill files in `.agents/skills/`. Documented anti-patterns at L45 ("vague task framing; missing output contract; asking for 'more reasoning' instead of better contract; mixing unrelated jobs into one run; unsupported certainty without grounding") are correct.

**Gap:** The XML prompt architecture is documented for *Codex* agents, but the actual swarm in this session (waves 1-9 in `adversarial_swarm_20260416/`) and the prior session (`audit_campaign_20260412_231034/AP01_bare_omega.md` STDERR) were both invoked via Codex CLI with `xhigh` reasoning, sandbox `workspace-write`. The prompts visible in the artifact STDERR sections (e.g., AP01_bare_omega.md L41 onward) DO use the documented XML tags. **Compliance is high.** No action needed.

### 2(b) — Failure modes (FM24, FM42-46)

AGENTS.md L535-541 contains "Formula drift", "Categorical confusion", "Structural" subsections that summarize FM1-FM46 by topic, ending with FM30, FM31. Then L749-759 has a separate "XXXIII. Failure Modes from 2026-04-14 CG Campaign" section listing FM42-FM46. **FM35-FM41 are missing from AGENTS.md.** These are documented in CLAUDE.md L508-518 (FM35 constitutional "never revert math to fix build", FM36 macro portability, FM37 double superscript, FM38 vertex-IRF bypass, FM39 spectral coassoc shift, FM40 naive vs derived center, FM41 Jones polynomial normalization). FM35 in particular — the constitutional rule against reverting math — is the most load-bearing operational rule and absent from the operational file.

**Recommendation:** Insert FM35-FM41 between L541 and L749 as a "Mid-campaign FMs" subsection; FM35 deserves its own elevation to a constitutional rule next to git/commit policy.

### 2(c) — Concurrency limits

AGENTS.md does not state concurrency limits. CLAUDE.md L517 (FM44) says "Counter: batches of 3, not 30+." This rule lives only in the encyclopedic atlas, not the operational layer.

### 2(d) — Concurrency rule violations in this session

The current swarm session (per `adversarial_swarm_20260416/`) shows 21 wave reports across 7 waves. Inspecting modification timestamps via the directory listing shows clusters: e.g., `MASTER_PUNCH_LIST.md` is the synthesis. The wave structure (1-3 with 9 reports = 3+3+3, then waves 4+ running concurrently) is reasonable, but the user description in the task brief mentions "24+ agents launched, often 6 concurrent — FM44 violations." If true, the violation is silent: nothing in the orchestration enforces FM44.

**Recommendation:** Promote FM44 to AGENTS.md as Section XXVII-A "Concurrency Discipline":
```
- Default batch size: 3 agents.
- Maximum concurrent: 6 (only after explicit user authorization).
- Stagger launches by ≥30s when batch > 3.
- Monitor for rate limit errors; if any agent in batch returns 429, halt batch.
```

Then: codify in `.codex/hooks.json` PreToolUse(SwarmLaunch) hook to refuse batches > 3 without authorization flag.

### 2(e) — Other AGENTS.md gaps

- L646: "git stash FORBIDDEN (use git diff > patch.diff + git apply)" — correctly stated.
- L644-647 git rules consistent with cross-volume canonical statement.
- L666-668 "Three pillars" subsection partially duplicates CLAUDE.md L924-931. Consolidate.
- Skill routing table (L575-588): comprehensive. No issues.
- Pre-Edit Verification Protocol (L367-451): templates PE-1, PE-2, PE-4, PE-5, PE-7, PE-8, PE-10, PE-11 in AGENTS.md; PE-3, PE-6, PE-9, PE-12 deferred to CLAUDE.md per L451. **Asymmetry: high-frequency violations (kappa, r-matrix, label) are operational; low-frequency (complementarity, summation boundary) are encyclopedic. Defensible split.**

---

## Section 3 — README audit

**Current state:** 142 lines. Public-facing.

### 3(a) — Overclaim audit

Comparing README L82-86 "Status" table to actual proof state:

| README claim | .tex / CLAUDE.md state | Verdict |
|--------------|------------------------|---------|
| "Master conjectures MC1-MC5: ALL PROVED" | CLAUDE.md L533: "MC5 ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL" | **MISMATCH** — README overclaims. MC5 chain-level for class M is conjectural per AP218 and per the theorem table. |
| "Main proofs adversarially verified 10/10 SOUND (732-agent campaign)" | CLAUDE.md L715 "AP225 (CRITICAL): genus-universality gap" | **MISMATCH** — Theorem D all-genera has unresolved gap per AP225 WARNING. The 732-agent verification post-dates the AP225 discovery, but `final_gaps_20260413_213946/G01_thm_D_universality_fix.md` reports the fix was made, while CLAUDE.md still carries the AP225 WARNING. **Either AP225 is closed and CLAUDE.md is stale, or AP225 is open and README is overclaiming.** Resolve before next release. |
| "First-principles cache, cross-programme enforcement verified clean" | Wave 1 (this swarm) found BP arithmetic error in 3 files (P0-1 of MASTER_PUNCH_LIST). The cache could not have caught this because the cache verifies labels not arithmetic. | **MISMATCH** — "verified clean" is not what the cache provides. Reword: "First-principles cache, label-coverage verified" or similar. |
| "Standalone papers: 16 papers, all CG-rectified" | wave 6-9 of current swarm find unrectified standalones (e.g., wave 7 W-algebra issues; standalone notes in MASTER_PUNCH_LIST P1-12 through P1-15 indicate `e1_primacy_ordered_bar.tex` standalone has ~35 V2-AP4 violations). | **MISMATCH** — "all CG-rectified" overclaims; some standalones still carry violations from before CG conventions stabilized. |

This is exactly the AP15 / V2-AP-README pattern documented in `compute/audit/new_antipatterns_wave12_campaign.md` as AP224 ("README scope inflation").

### 3(b) — Status of main theorems

README L20-26 table for theorems A-H is concordance-aligned. Theorem D row says "Proved here" without the (UNIFORM-WEIGHT) tag that AP32 mandates. Recommended: change the cell to "Proved here (uniform-weight); multi-weight g≥2 has δF_g^cross." This is the CLAUDE.md L530 phrasing transplanted to README — and the README is shorter, public-facing, so the qualifier matters more there.

### 3(c) — Other README gaps

- README L8-14 three-volume table: Vol III description says "categorical completion: CY categories as quantum chiral algebras". This is accurate but elides that Vol III's CY-A_3 is now PROVED (inf-cat) and the K3 abelian Yangian is PROVED (per Vol III CLAUDE.md). The README is silent on Vol III's actual achievements.
- README L80 "Tagged claims (Vol I registry) ~3,463" — verify against `metadata/census.json` (which `make census` regenerates). This number drifts; AP112 (stale page counts) and FM46 (stale preface counts) apply.

---

## Section 4 — archive/ audit

**Total size:** ~290 MB across 16 subdirectories. Largest:
- `archive/misc/` 204 MB
- `archive/references/` 64 MB (reference PDFs — keep)
- `archive/previews/` 15 MB (PDF previews of dropped/superseded chapters)
- `archive/raeeznotes/` 11 MB
- `archive/raeeznotes83/` 3.2 MB
- `archive/source_notes/` 3.3 MB
- `archive/source_tex/` 2.7 MB
- `archive/standalone/` 1.1 MB
- `archive/orphaned_stubs/` 104 KB (10 .tex files)

### 4(a) — Contents

`archive/orphaned_stubs/` lists: bar_cobar_quasi_isomorphism.tex, classical_to_chiral.tex, deformation_quantization_complete.tex, heisenberg_higher_genus.tex, higher_genus_full.tex, higher_genus_quasi_isomorphism.tex, kac_moody_computations.tex, koszul_across_genera.tex, obstruction_classes.tex, rosetta_stone.tex.

These are early-draft chapters superseded by current Part I/II/III content.

`archive/standalone/`: editorial_preamble.tex, editorial.pdf, editorial.tex, theorem_ledger.csv. **`theorem_ledger.csv` may have currency value** — check if it's an outdated census or if `metadata/census.json` supersedes it.

`archive/split_originals/`: bar_cobar_construction.tex (one file). The "original" of subsequently split chapters.

`archive/previews/`: 10 PDFs including `Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf`, `wave54check.pdf`, `test_oper.pdf`. **These are session detritus** — wave checks should not live in archive; they should live in build_logs/ or be deleted.

### 4(b) — Live citations to archive

`grep -rl "archive/" chapters/ standalone/ main.tex` returns ONE hit: `main.tex` itself. This is the README/CLAUDE.md/concordance reference list. **Manuscript content does NOT cite archive/ files** (correct).

### 4(c) — "Still active" content mistakenly archived

- `archive/audit/unfinished_work_audit_20260413.md` — title suggests unfinished work; if any unfinished items still apply, this audit's items may be live debt buried in archive. Sample read recommended.
- `archive/notes/` (292 KB) — sample contents not inspected; may include design memos worth preserving but not actively referenced. Low priority.
- `archive/raeeznotes_absorbed/` (168 KB) — naming suggests "already absorbed into manuscript"; should be safe to delete after a final grep verifies nothing is uniquely there.

### 4(d) — Archive recommendations

| Action | Target | Saving |
|--------|--------|--------|
| Delete | `archive/previews/wave54check.pdf, test_oper.pdf, test_snippet.pdf, codex_verify.pdf` | ~5 MB |
| Move to `.build_logs/` | `archive/previews/*.pdf` (the genuine drafts) | clarifies provenance |
| Compress to .tar.gz | `archive/raeeznotes/`, `archive/raeeznotes83/`, `archive/raeeznotes_absorbed/` | ~14 MB → ~2 MB |
| Audit and either prune or commit | `archive/audit/unfinished_work_audit_20260413.md` | clears latent debt |

`archive/misc/` at 204 MB is the largest opportunity but unsampled in this audit; recommend separate housekeeping pass.

---

## Section 5 — Audit-campaign retrospective + regression rate

**Inventory:** 11 `audit_campaign_*` directories, of which 4 are non-empty (each contains 106 AP files), 7 are empty (zero-byte stub failures).

The two non-empty campaigns are timestamped 2026-04-12 230832 and 231034 (24 minutes apart) — these are sibling/duplicate launches. The 7 empty `audit_campaign_*` directories from 2026-04-13 represent failed agent dispatches (likely FM44 rate-limiting cascade).

### 5(a) — Sample findings from `audit_campaign_20260412_231034/`

`AP01_bare_omega.md` — Wave 12 audit campaign, 524 seconds, gpt-5.4. Found:
- 5 CRITICAL bare-Omega violations across Vol I + Vol II (preface_full_survey.tex L507; log_ht_monodromy_core.tex L1905; thqg_gravitational_yangian.tex L728+L731; yangians_foundations.tex L1059)
- 6 HIGH violations (preface_section1_v2.tex L481; preface_section1_draft.tex L634; preface_sections5_9_draft.tex L542,581,582; thqg_preface_supplement.tex L224; holographic_datum_master.tex L466 + L717)
- 2 MEDIUM (frontier_modular_holography_platonic.tex L4731+L4764; rosetta_stone.tex L2795)
- 2 LOW (`.bak` files — should be deleted)

**Verdict:** 17 violations of the most-violated AP (AP126/AP141), all documented with file:line.

### 5(b) — Did findings get fixed?

Cross-checking against current swarm (wave 3 `wave3_chern_weil_levels.md`, wave 4 `wave4_holographic_3dqg.md`, MASTER_PUNCH_LIST P0-7): Wave 3 found "multiple unfixed instances in chiral_chern_weil.tex (line 429, ∂T term that should drop; bridge identity at L458) and convention clashes between three_parameter_hbar.tex, garland_lepowsky.tex, and the Vir r-matrix files."

**Conclusion:** AP126/AP141 violations from 2026-04-12 audit were NOT fully fixed by 2026-04-16. The same files appear in both audits. The audit produced a list, the fixes did not propagate.

### 5(c) — Regression rate estimate

Rough sampling against the AP01-AP20 sequence of the 2026-04-12 audit:

| AP | 2026-04-12 finding | Still present 2026-04-16? |
|----|--------------------|---------------------------|
| AP01 (bare Ω) | 17 violations | Yes — wave 3 confirms unfixed in chiral_chern_weil.tex; wave 4 in holographic; some preface variants likely unfixed |
| AP07 (env mismatch) | (sample not read) | Wave 5 chiral_hochschild_koszul.md likely confirms partial regression |
| AP08 (proof after conj) | (sample not read) | Foundation audit report shows 28+ critical "ProvedHere with no proof block" findings in arithmetic_shadows.tex alone |
| AP14 (bare kappa Vol III) | 165 baseline | Vol III CLAUDE.md HZ-7 still flags as recurrent |

**Estimated regression rate:** ≥40% of 2026-04-12 critical findings are still present 4 days later. The fix-confirm-propagate loop is leaking somewhere between (a) audit produces list, (b) elite_rescue/healing/final_gaps agents process subset, (c) follow-up audit.

### 5(d) — Recurring issues = AP candidates

The empty audit campaigns (7 of 11) are themselves a pattern: launching audits without verifying agent completion. Promote to AAP19: "Verify audit campaign produced output (non-empty directory) before declaring it run."

---

## Section 6 — elite_rescue retrospective

**Inventory:** 13 `elite_rescue_*` directories, 4 non-empty, 9 empty.

### 6(a) — What is elite_rescue?

Per H10_session_summary.md sample: "ELITE RESCUE agent. Your focus: the latest 50-100 commits across a 3-volume, 4,700-page mathematical manuscript. ... Your mission: 1. HEAL remaining wounds from the session, 2. PROVIDE alternative proof routes for REDUNDANCY, 3. CROSS-CHECK against published literature, 4. DERIVE key results via INDEPENDENT methodology, 5. UPGRADE mathematical strength wherever possible, 6. VERIFY cross-domain and cross-approach consistency."

This is the multi-path-verification programme. Output structure: H01-H10 (heal), L01-L10 (literature comparison), R01-R10 (independent rederivation).

### 6(b) — Did rescues stick?

Sample: H10_session_summary.md is essentially empty (1-second timeout — agent failed). The L01-L10 literature comparisons (BD, FG, CG, Lurie, PTVV, EF, KS, Livernet, CFG-E3, GR) and R01-R10 independent rederivations (kappa, complementarity, obs_g genus 1, sl_2 bar cohom, depth gap, SC Koszulity, Verlinde shadow, Borcherds bar Euler, E3 from 3d CS, genus 2 explicit) are the foundation of the "Alternative Proofs Secured" table in CLAUDE.md L997-1010.

**Verification chain:** Each H/L/R file should produce or amend `chapters/connections/concordance.tex` and per-theorem alternative-proof remarks in chapters. Spot check needed; not done here.

### 6(c) — elite_rescue regression

The 9 empty directories from 2026-04-13 16:34, 16:52, 16:59 (multiple times) suggest the same FM44 cascade as the audit failures. Same root cause. **The rescue infrastructure is more fragile than the audit infrastructure** because rescues require longer agent runtime and are more rate-limit sensitive.

---

## Section 7 — final_gaps verification

**Inventory:** 1 `final_gaps_20260413_213946/` directory with 30 G01-G30 files.

### 7(a) — Were the gaps fixed?

Sample G01: "AP225 closed on disk." Reports thm:genus-universality re-proven via Hodge bundle Chern-Weil, derives `obs_g(A) = κ(A)·c_g(E) = κ(A)·λ_g` directly, dropping the broken clutching-uniqueness step.

**Cross-check:** `grep -l "AP225" higher_genus_modular_koszul.tex higher_genus_foundations.tex` returns higher_genus_foundations.tex. So either:
- (a) The fix was applied but a remark or comment still mentions AP225 (acceptable archaeology),
- (b) The fix was incomplete in higher_genus_foundations.tex,
- (c) AP225 is still mentioned for context with the new clean proof.

This is the README-vs-CLAUDE.md inconsistency from Section 3(a) item 2: README says 10/10 sound, CLAUDE.md still has AP225 WARNING, final_gaps says fixed. **Single source of truth is needed.**

### 7(b) — Resurfacing in waves 1-9?

MASTER_PUNCH_LIST P1-2 says "T4 'two independent proofs' share the uniform-weight virtual class. Both Proof A (GRR/Arakelov-Faltings) and Proof B (clutching) take `[B^(g)_scalar(A)]^vir = κ·[E]` as input." This is the SAME load-bearing input the G01 fix took as a separate Hodge-bundle Chern-Weil derivation. **G01 may have passed the input through one proof but left it as an axiom in the other.** Treat as P1-priority follow-up.

---

## Section 8 — Makefile gap audit

**Existing targets (from Makefile read):**
- `make`, `make all`, `make fast`, `make release`, `make standalone`, `make working-notes`, `make icloud`
- `make watch`, `make clean`, `make veryclean`, `make clean-builds`
- `make count`, `make check`, `make integrity`, `make phase0-index`
- `make metadata`, `make census`, `make audit` (Beilinson auditor on theorem dependency DAG)
- `make verify` (anti-pattern verification via `scripts/verify_edit.sh --all`)
- `make test`, `make test-full`
- **`make verify-independence`, `make verify-independence-verbose`** — present and wired correctly per Section HZ-IV
- `make dist`, `make editorial`, `make help`

**Missing high-value targets:**

1. **`make claudemd-lint`** — checks CLAUDE.md and AGENTS.md for:
   - Stale APs (AP that hasn't appeared in any audit log for ≥30 days)
   - Duplicated content with Vol II/III CLAUDE.md (using `diff -u` against canonical)
   - Pointer rot (any `notes/X.md` reference that doesn't resolve)
   - Forbidden formulas list (B-numbers) consistency between CLAUDE.md L335-444 and AGENTS.md L213-302

2. **`make stubs-audit`** — applies AP114 (stub chapter < 50 lines, no theorems):
   - Find all chapter `.tex` files under `chapters/` with line count < 50 OR theorem count = 0
   - Fail if any are referenced by `\input{}` from `main.tex`
   - This was hand-discovered in Vol III recently; needs automation

3. **`make regression-rate`** — composite:
   - Re-run all the AP-pattern regexes from `scripts/verify_edit.sh`
   - Compare against `audit_campaign_20260412_*/` historical findings
   - Print persistence rate per AP
   - Target: `make regression-rate` returns 0 when persistence < 10% per AP, else 1

4. **`make concurrency-guard`** — hook target invoked by swarm-launching scripts:
   - Read currently-running agent count from a state file
   - If >3, refuse new launch (or, if --authorized, allow up to 6)
   - Codifies FM44

5. **`make ci`** — composite gate:
   - Equivalent to `make verify && make verify-independence && make claudemd-lint && make stubs-audit && make audit && make test`
   - This is what a pre-commit hook should call
   - Currently the closest equivalent is `make integrity`, which is undocumented in this audit but per L222 calls `scripts/integrity_gate.sh`. **Verify integrity_gate.sh covers all the above.**

6. **`make ap-blacklist-grep`** — runs all 73 forbidden-formula regexes (B1-B73) plus banned tokens against entire chapters/+standalone/+appendices/. The infrastructure to do this lives in scripts/verify_edit.sh; expose as a top-level target.

7. **`make readme-sync`** — checks README claims against:
   - `metadata/census.json` (claim counts must match)
   - `concordance.tex` theorem statuses (README status must match)
   - CLAUDE.md theorem table (must agree)
   - Fails on any mismatch (closes the AP15/AP224 README-overclaim AP).

---

## Section 9 — First-principles investigation (per AP-CY61 / AP186)

The systemic pattern across waves 1-9 of the current swarm and the audit/rescue/final-gaps history is **convention-discipline leak**: the manuscript is mathematically sound but loses correctness through (a) bare formulas without level prefix (AP126/AP141), (b) convention clashes within and across volumes (AP151/AP-CY51), (c) tautological internal verification (the same mental model on engine + test side), (d) status drift between README, CLAUDE.md, and `.tex`.

**Ghost theorem of "the regression rate is high":** It is high not because the math is wrong but because the *enforcement layer is documented, not executed*. AGENTS.md and CLAUDE.md say "do X"; nothing checks that X was done. The verify-independence target is the singular exception where a check is wired in. Every other rule sits in prose.

**The correct next theorem:** Convert prose rules to grep targets, wire grep targets into `make ci`, wire `make ci` into a `.codex/hooks.json` PreToolUse hook on Edit/Write to ANY `.tex`. This is the meta-process analog of the HZ-IV protocol that successfully shifted Vol III from "always verify" (aspirational) to "tautology fails import" (machine-checked).

**Falsifier:** If `make ci` runs in <60s on a typical edit, it is too weak (just-greps, no real check). If it runs in >5min, agents will skip it. The right granularity: `make ci-fast` (<30s) for pre-Edit, `make ci-full` (<5min) for pre-commit. The existing `make test` (fast) already follows this split; extend to verification.

---

## Section 10 — Three meta-process upgrades (concrete proposals)

### Upgrade #1: `make ap-grep` + pre-write hook

**What:** A make target that runs every blacklist regex (B1-B85) from CLAUDE.md and every banned token from AGENTS.md against a single file argument. Used as `make ap-grep FILE=chapters/theory/foo.tex`.

**Implementation:** Already mostly exists in `scripts/verify_edit.sh --all`. Promote to first-class `make ap-grep` with single-file mode. Wire into PreToolUse(Edit) hook: agent edits a `.tex` file → hook runs `make ap-grep FILE=$EDITED_FILE` → if non-zero, hook prints violations and asks the agent to confirm or revise.

**Closes:** AP126/AP141 chronic recurrence (most-violated AP per AGENTS.md L309). Closes AP29 (AI slop) chronic recurrence.

**Rough cost:** 1-2 sessions to implement the per-file mode; existing `--all` mode is already there.

### Upgrade #2: `make claim-status-sync` (cross-volume + cross-file)

**What:** Single source-of-truth check for theorem status. Reads (a) concordance.tex theorem table, (b) CLAUDE.md theorem status table, (c) README status table, (d) per-chapter `\ClaimStatusXXX` tags, (e) Vol II + Vol III inherited references. Fails if any disagree.

**Implementation:** New script `scripts/claim_status_sync.py`. Scrape all `\ClaimStatusProvedHere`, `\ClaimStatusConjectured`, `\ClaimStatusConditional` tags. Build a dict `{theorem_label: status}`. Compare against (a) (b) (c) entries by name match. Output disagreements.

**Closes:** AP15 / AP224 (README scope inflation), AP149 (resolution propagation failure), the AP225 README-vs-CLAUDE.md inconsistency identified in Sections 3(a) and 7(a).

**Rough cost:** 1 session. The hard part is the parser for the README/CLAUDE.md tables; the `.tex` scraper is trivial.

### Upgrade #3: Empty-campaign-directory cleanup + concurrency hook

**What:** (a) `make clean-empty-campaigns` deletes any `audit_campaign_*`, `elite_rescue_*`, `healing_*`, `final_gaps_*`, `fix_wave_*` directory that is zero-bytes or contains only zero-byte files. (b) Codex hook `concurrency-guard.sh` enforces FM44.

**Implementation:**
```bash
# clean-empty-campaigns
find . -maxdepth 1 -type d \( -name 'audit_campaign_*' -o -name 'elite_rescue_*' \
       -o -name 'healing_*' -o -name 'final_gaps_*' -o -name 'fix_wave_*' \) \
       -empty -exec rmdir {} \;
# also: dirs whose only content is empty .md files
```

For concurrency hook: add to `.codex/hooks.json` a PreToolUse handler on Bash(spawn agents) that increments a counter in `.agents/active_count` and refuses if >3.

**Closes:** the "empty directory cascade" pattern (7/11 audit, 9/13 elite_rescue), AAP19 (verify campaign produced output), FM44 (concurrency limit).

**Rough cost:** Half session.

---

## Section 11 — Punch list (priority-ordered, copy-paste actionable)

### P0 — Single-source-of-truth for AP225 / Theorem D status

**Files:** `chapters/theory/higher_genus_foundations.tex`, `chapters/theory/higher_genus_modular_koszul.tex`, `CLAUDE.md` L530+L552+L566+L715, `README.md` L25+L86, `concordance.tex` (need to check), `final_gaps_20260413_213946/G01_thm_D_universality_fix.md` (claim of fix)

**Issue:** `final_gaps/G01` says fix landed; `CLAUDE.md` L715 still has AP225 WARNING; README L86 says 10/10 sound. Three sources, three states.

**Action:** Verify the G01 fix in higher_genus_foundations.tex L5453 area. If solid, remove AP225 WARNING from CLAUDE.md (or reformulate as "AP225 closed by Hodge-Chern-Weil derivation"). Sync README to match. Use this as the prototype run of Upgrade #2.

### P0 — Resolve MC5 chain-level claim discrepancy

**Files:** `README.md` L86 ("MC1-MC5 ALL PROVED"), `CLAUDE.md` L533 ("MC5 chain-level CONJECTURAL"), `chapters/connections/concordance.tex`

**Action:** Single-source. The honest version is MC5 partial (analytic + coderived proved, chain-level class M conjectural). README must match.

### P1 — Convert HZ-IV protocol from documented to exercised in Vol I

**State:** Per CLAUDE.md L286-289, Vol I has 0/2275 ProvedHere claims with independent decorators.
**Action:** Seed `notes/tautology_registry.md` (Vol I) with 5-10 candidates. Apply the Vol III three-healings doctrine (find disjoint source / restrict scope / downgrade) on a sample. Make the 0% number visible in `make census` output.

### P1 — Implement `make ap-grep FILE=...` and wire into PreToolUse(Edit) hook

(Upgrade #1 above.) Closes AP126 chronic recurrence and the 17 bare-Omega violations from `audit_campaign_20260412_231034/AP01_bare_omega.md` that survived to wave 3 of the 2026-04-16 swarm.

### P1 — Implement `make claim-status-sync`

(Upgrade #2 above.) Closes the AP225 / MC5 / "10/10 sound" inconsistency triangle.

### P2 — CLAUDE.md compression (target 1073 → 750-800)

Per Section 1: pull HZ-IV body to `notes/INDEPENDENT_VERIFICATION.md`, drop AP-CY62-67 verbatim duplication (pointer suffices), drop merged-RS prose, archive AP146 / AP43 / AP127 candidates.

### P2 — AGENTS.md insertions

Per Section 2: insert FM35-FM41 (currently absent from AGENTS.md, present in CLAUDE.md), promote FM44 concurrency limit to its own subsection, codify in `.codex/hooks.json`.

### P2 — Archive cleanup

Per Section 4: delete `archive/previews/wave54check.pdf`, `test_oper.pdf`, `test_snippet.pdf`, `codex_verify.pdf` (clear session detritus). Tar+gz the three `raeeznotes*` directories. Audit `archive/audit/unfinished_work_audit_20260413.md`.

### P3 — `make clean-empty-campaigns` (Upgrade #3a)

Removes 7 empty `audit_campaign_*`, 9 empty `elite_rescue_*`, and corresponding `healing_*` / `fix_wave_*` directories. Cosmetic but reduces noise for future audit pattern-matching.

### P3 — README synchronization

Per Section 3: fix "all CG-rectified" overclaim, fix "verified clean" cache phrasing, add (UNIFORM-WEIGHT) tag to Theorem D row, refresh page/test counts via `make census`.

### P3 — Codify AAP19

"Verify audit campaign produced output (non-empty directory) before declaring it run." Add to AGENTS.md and CLAUDE.md AAP section.

---

## Steelman both sides

**Steelman of current orchestration:** The Vol I orchestration layer is the most mature in the programme. It already has Pre-Edit Verification templates (AGENTS.md PE-1 through PE-12), a 73-entry forbidden-formula blacklist with regexes, the verify-independence machinery exposed via Make, hot-zone documentation, an XML-tagged Codex prompt protocol, and a working swarm infrastructure that produced the current adversarial findings. It catches errors at multiple gates — adversarial audit, elite rescue, final gaps, healing — and the catch rate is high (60+ critical findings from the 2026-04-12 campaign, ~30 in the current 2026-04-16 swarm so far). Against that backdrop, asking for "more enforcement" is asking the gate to be a wall, which would slow research velocity. The current loose-but-documented model preserves agent flexibility while accumulating institutional memory.

**Steelman of the upgrade thesis:** A documented rule that nobody enforces is approximately equivalent to no rule. The persistence of AP126 from 2026-04-12 to 2026-04-16 across the same files (chiral_chern_weil.tex, etc.) demonstrates that prose discipline does not translate to code-state. The HZ-IV protocol was successful precisely because it converted "always verify" to "tautology fails import" — a machine check. Every other top-10 hot zone deserves the same treatment. The cost of `make ap-grep` is one session of work; the savings is the elimination of an entire wave's worth of recurrent findings per audit cycle.

**Synthesis:** Both are right. The upgrade thesis is correct mathematically (rules without enforcement decay). The current-state defense is correct operationally (the manuscript IS getting healed; the rate is what it is). The right move is to convert the highest-recurrence APs to machine checks (AP126, AP1, AP132, AP29, AP40 — these are the top 5 by violation count) without trying to mechanize the long tail of one-off APs. This preserves agent flexibility on novel material while eliminating the chronic leak.

---

## Cache write-back (per AP186 / memory protocol)

Patterns appearing 2+ times across this audit warrant cache entries. Recommended additions to `appendices/first_principles_cache.md` (Vol I) or equivalent:

1. **CACHE-AUDIT-DOCUMENTATION-VS-EXECUTION.** Documented enforcement = no enforcement when the agent reading the document is stochastic. Symptoms: rules appear, recur, accumulate prose; violations persist across audits. Counter: machine-check via grep / pytest / hook. Examples: AP126 prose discipline (failed) → `make ap-grep` (proposed); HZ-IV "always verify" prose (failed in Vol III) → `@independent_verification` decorator (succeeded). Cross-volume: same pattern in Vol II (V2-AP29 AI slop persisting), Vol III (κ subscript drift).

2. **CACHE-EMPTY-CAMPAIGN-CASCADE.** When N agents launch concurrently and most fail (rate-limit, timeout), the failed launches leave empty directories that look like successful audits to grep-based aggregators. Symptom: 7/11 audit_campaign_* dirs are empty. Counter: AAP19 — verify directory non-empty as part of "campaign succeeded" criterion.

3. **CACHE-README-AS-MATHEMATICAL-OBJECT.** README is the public-facing layer; overclaims propagate to external readers. AP15 / AP224 documented this; AP-CY15 mirrors in Vol III. Symptom: README "10/10 sound" while CLAUDE.md carries AP225 WARNING. Counter: `make claim-status-sync` (proposed). Promote README to the same status-tag discipline as `.tex`.

4. **CACHE-ORCHESTRATION-VS-CONTENT-AP-DIFFERENCE.** Content APs (AP126, AP132 etc.) attack mathematical errors. Orchestration APs (AAPs, FMs) attack process errors. They have different lifecycles: content APs decay as the manuscript stabilizes; orchestration APs grow as the swarm grows. Vol I is at the inflection: content APs are now mostly cleanup, orchestration APs are net new. AGENTS.md needs to inflate to absorb FM35-FM41 it currently lacks, while CLAUDE.md can deflate (Section 1 compression).

---

## End-of-task contract

**Claim surface audited:** Vol I CLAUDE.md (1073L), AGENTS.md (759L), README.md (142L), Makefile (470L), archive/ (16 subdirs, ~290MB), audit_campaign_*/elite_rescue_*/final_gaps_*/healing_*/fix_wave_* directories (38 total, ~half empty), adversarial_swarm_20260416/MASTER_PUNCH_LIST.md (291L), cross-references to Vol II + Vol III CLAUDE.md.

**Proved internally:** Documentation duplication exists; ~250 lines of CLAUDE.md compression available losslessly; FM35-FM41 absent from AGENTS.md; README has 4 overclaims vs CLAUDE.md / wave-1-3 findings; AP126 violations from 2026-04-12 audit persist to 2026-04-16 wave 3 in the same files; 7/11 audit_campaign_* and 9/13 elite_rescue_* dirs are empty (FM44 cascade); Makefile lacks `claudemd-lint`, `stubs-audit`, `regression-rate`, `concurrency-guard`, `ci`, `ap-grep`, `readme-sync`, `claim-status-sync`.

**Supported computationally only:** Regression rate estimate (~40% of 2026-04-12 critical findings persist) is a sample, not a complete count; full count requires re-running all 106 AP files of `audit_campaign_20260412_231034/` against current state.

**Conditional:** AP225 status (CLAUDE.md says open, final_gaps says closed). G01 fix needs verification in `higher_genus_foundations.tex` L5453 area before declaring resolved.

**Open:** Whether the existing `make integrity` / `scripts/integrity_gate.sh` already covers any of the proposed Upgrade #1-3 — needs read of `scripts/integrity_gate.sh` not done in this audit.

**Verification run:** Read tool on CLAUDE.md (3 slices), AGENTS.md (full), README.md (full), Makefile (full), MASTER_PUNCH_LIST.md (full), AP01_bare_omega.md (head), final_gaps G01 (head), elite_rescue H10 summary (head), foundation_audit_chapters_report.md (head). Bash listings of all campaign dirs with size and population counts. Grep for AP225 in fixed chapters.

**Propagation:** None — this is a meta-process audit; no edits made, no commits, per task brief.

**Written to:** `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave10_meta_process.md` per task brief.
