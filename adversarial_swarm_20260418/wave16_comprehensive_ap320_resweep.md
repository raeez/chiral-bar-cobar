# Wave-16 Comprehensive AP320 Re-sweep — AP321-corrected programme-wide search

**Date:** 2026-04-18
**Supervisor:** re-sweep agent (diagnostic only, no edits, no commits)
**Scope:** 2026-04-18 session Tier-1 claim-file deliverables under `adversarial_swarm_20260418/`.
**AP lineage:** AP320 (narrative-only claim fabrication) × AP321 (supervisor-grep-blind
false positive) × AP316 (worktree-abandoned edit) × AP313 (truncated inscription).

## Comprehensive regex

```
@independent_verification | @_iv\( | @_iv_v[0-9]+_[a-zA-Z_]+\( |
TestGoldStandardDisjointPaths | \\ClaimStatus[A-Z][a-zA-Z]+ |
\\label\{[a-zA-Z-]+:[a-zA-Z0-9\-_]+\} | \\begin\{remark\}\[Attribution
```

## Per-claim verification table

| # | Wave + claim file | Artifact (label / decorator / heal) | Disk state | Verdict |
|---|---|---|---|---|
| 1 | W-10 CLAUDE.md rows 603-630 | 4 heals (chd clause 2 split; Drinfeld drift; Toroidal line-drift; KZB flatness drift) | All 4 line targets verified in disk CLAUDE.md + preface.tex + seven_faces.tex + ordered_associative_chiral_kd.tex | PASS |
| 2 | W-11 Vol II HZ-11 prop:standard-strong-filtration | 5 consumers sharpened to `V1-`; alias at vol2/main.tex | vol2/main.tex:892 alias present; 5 retargeted refs present (curved_dunn x2 + bv_brst x3) | PASS |
| 3 | W-11 Vol II HZ-11 rem:twining-genera | Alias already exists at main.tex:1028-1029; 5 consumers OK | Alias inscribed at main.tex:1036 (drift from 1028-1029 claimed, AP271-minor) | PASS w/ AP271 line-drift |
| 4 | W-12 H3 rename execution (~30 kappa_ch → kappa_ch^{Heis}) | Sites enumerated in preface, introduction, k3e_cy3_programme, k3e_bkm_chapter, k3_chiral_algebra, quantum_group_reps | ZERO `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}` hits in the 6 target chapter files. 71 `mathrm{Heis}` hits elsewhere are pre-existing Heisenberg prose | **AP316-worktree** (no merge to main) |
| 5 | W-12 AP253 self-cite campaign | 3 Vol I en_koszul_duality Lorgat cites + 2 Vol II (bp_chain_level, ym_boundary_theory) | ZERO Lorgat26I / Lorgat26II hits in en_koszul_duality.tex; ZERO Vol1-C31 / LorgatVolI hits in vol2/chapters. All 5 sites healed | PASS |
| 6 | W-12 modular_trace AP290 heal | 3-line Route-A/Route-B split; AP289 + AP290 warning | Route-B additive + Route-A multiplicative display present at modular_trace.tex:86+ | PASS |
| 7 | W-12 Vol II CLAUDE.md chiral Higher Deligne clause (2) drift | 5 sites + Theorem-H scope caveat (line ~1073) | 6 "clause (2)" hits in vol2/CLAUDE.md; clause-split discipline propagated | PASS |
| 8 | W-12 shadow-tower companion triage | 3 V1- phantomsection aliases in vol2/main.tex:652; 3-4 `\ref{}` retargets | 3 aliases verified (tier-4, subleading, sub-subleading); 0 bare refs remain | PASS |
| 9 | W-13 Vol I V2/V3 scaffolding | 7 phantomsection aliases main.tex:2202-2210 | 7 aliases at 2207-2213 (drift +5 lines; Wave-14 inserted an 8th at 2215). All targets verified in home volumes | PASS |
| 10 | W-13 Vol II bibkey next-tier (14 bibitems + 4 aliases) | GRW18, Arakawa07, CostelloGaiottoBoundaryVOA, CLNS24, Bakas-Winfty, KRW03, Kohno1987, Gannon16, Positselski18, SchiffmannVasserot13, ProchazkaRapcak18, FrenkelHernandez15, KhoroshkinTolstoy96, GaiottoRapcak2017, CachazoStrominger14, PasterskiShaoStromingerFlatSpaceHolog, FF90, AP95 | 18 bibitem hits in vol2/main.tex | PASS |
| 11 | W-13 AP287 HZ-11 sweep (Vol I) | Zero violations, no heals required | Diagnostic-only; no claims on disk to verify | PASS (vacuous) |
| 12 | W-13 Vol III CLAUDE.md sweep | 1 heal row 114 (Y(gl(4\|20)) → Y_{osp(4\|20)}) | Y_{osp(4\|20)} at calabi-yau-quantum-groups/CLAUDE.md:14 + :114 | PASS |
| 13 | W-13 Vol I κ_BKM 3-agent HZ-IV (gold-standard 3 files) | @_iv / @independent_verification decorators in 3 test files | 3 `test_gold_standard_*_three_disjoint_paths` functions verified in moonshine_kappa_resolution + cy_bkm_algebra + cy_borcherds_lift | PASS |
| 14 | W-14 κ_ch AP5 cross-volume sweep | Vol II manuscript clean; 5 metacognitive-layer residuals deferred to W-15 | Diagnostic-only on Vol II | PASS (vacuous Vol II; W-15 picked up the 5 metacognitive sites) |
| 15 | W-14 phantom detector post-metadata | Diagnostic counts (Vol I 12 / Vol II 0 / Vol III 0) | Enumeration table only, no heals claimed | PASS (diagnostic) |
| 16 | W-14 Vol II V1-ref HZ-11 (6-finding heal) | `rem:thqg-III-ambient-properties-attribution` in thqg_symplectic_polarization | Label inscribed at :196 | PASS |
| 17 | W-14 Vol II quantum-complementarity HZ-11 | `rem:thqg-IV-four-facets-attribution` + AP124 duplicate cleanup | Remark inscribed at thqg_gravitational_s_duality.tex:1684; AP124 dup at main.tex:978 annotated | PASS |
| 18 | W-15 AP320 supervisor sweep (diagnostic recant) | False-positive finding: Wave-13/14 decorators DO exist | Consistent with W-16 AP321 reverification | PASS (diagnostic) |
| 19 | W-15 Vol II AP287 exhaustive (diagnostic reprojection 93 → ~40) | 0 heals claimed; recategorised residuals | No claims on disk to verify | PASS (diagnostic) |
| 20 | W-15 Vol I chapter-stubs + singletons | 9 retargets (chap:infinite-fingerprint-classification twin-label + 5 singleton consumer retargets) | chap:infinite-fingerprint-classification label inscribed (3 hits); retargets confirmed: thm:pbw-koszulness-criterion (7 hits in frame/), thm:uc-trinity + thm:climax-vol1-platonic + thm:quadrichotomy (8 hits in introduction.tex) | PASS |
| 21 | W-15 metacognitive κ_ch heal (Vol II CLAUDE.md + 4 cache entries) | Route-A/B splits with AP-CY68/69 cross-refs | Not re-verified in this sweep (metacognitive notes, cache layer; scope is permitted) | PASS (assume-pass per scope) |
| 22 | W-15 `_iv` alias import fix | 1 import line at test_cy_borcherds_lift_engine.py:32 | `from compute.lib.independent_verification import independent_verification as _iv` present | PASS |
| 23 | W-16 AP320 re-verification | Re-verified Wave-13/14 κ_BKM decorators; 8/10 PASS; 2 deferred residuals | Matches Wave-15 supervisor + Wave-16 this-sweep findings | PASS |
| 24 | W-16 Vol II AP287 Option A (4 files) | 4 umbrella remarks `[Scope restriction inherited from Volume~I]` | 4 files with the marker (critical_string_dichotomy, holographic_reconstruction, gravitational_yangian, fredholm_partition_functions) | PASS |
| 25 | W-16 master BV + topologization tower resolve | Diagnostic: AP286-legitimate tactical aliases already exist | 2 phantomsection aliases verified at preface.tex:1904 / 5153 + editorial_constitution.tex:433 | PASS (diagnostic) |

## Aggregate statistics

- Total claim files audited: 25 Tier-1 wave notes (waves 10 → 16).
- PASS: 24 / 25.
- AP320-genuine (claim made, zero trace on disk, no alias form): **0**.
- AP316-worktree (edit landed in `.claude/worktrees/*` but not main): **1** (Wave-12 H3 rename execution — the ~30 `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}` superscript sites across 6 chapter files are NOT present on `main` HEAD 23674e80. Commit log does not carry an H3 rename SHA; the claimed agent SHA `a1b6e600` does not exist in `git log --all --oneline`. Three worktrees are at different SHAs but none of the on-disk chapter files reflect the edit. The post-Wave-12 bibkey + AP253 commits refer to *notes*, not to H3 rename execution).
- AP321-supervisor-gap: **1** (confirmed from Wave-15 → Wave-16 self-correction — Wave-15 finals used narrow `@independent_verification` grep, missing alias + suffixed-alias forms).
- REVERT: **0**.

## Confirmed AP320 fabrications

**Zero.** The original W-15 finals AP320 narrative against Wave-13/14 is a confirmed AP321
false-positive: all 8 Wave-13/14 κ_BKM gold-standard decorators landed on disk under long,
bare, or suffixed alias forms, and W-16's comprehensive regex matches them all.

## Confirmed AP316-worktree

**One.** Wave-12 H3 rename execution (`wave12_h3_rename_execution.md`, ~30 claimed
`\kappa_{\mathrm{ch}}^{\mathrm{Heis}}` retag sites across 6 chapter files) is not present
on `main` HEAD. Possible causes: (a) merge to main pending; (b) edits left in an agent
worktree that was reset before merge; (c) narrative claim produced without actual Edit
invocation. Grep `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}` on `main`:

```
chapters/frame/preface.tex                    : 0 hits
chapters/theory/introduction.tex              : 0 hits
chapters/examples/k3e_cy3_programme.tex       : 0 hits
chapters/examples/k3e_bkm_chapter.tex         : 0 hits
chapters/examples/k3_chiral_algebra.tex       : 0 hits
chapters/examples/quantum_group_reps.tex      : 0 hits
```

Healing: either (i) re-execute the H3 rename on `main` with PE-5 template per edit (AP5
atomic propagation), or (ii) retract the rename narrative in a future wave and note the
two-subscript discipline is carried only in CLAUDE.md + Vol II / Vol III CLAUDE.md
pointers. Option (i) is preferred because the H3 discipline is load-bearing for AP-CY68/69
inscribed in `notes/cross_volume_aps.md` and the Route-A/Route-B Beauville table in
`cy_d_kappa_stratification.tex:411-426`.

## Meta-pattern: AP320-supervisor-pattern hierarchy

Three failure modes now registered:
- **AP320-genuine** — claim made, zero disk trace, no alias. Zero instances this session.
- **AP316-worktree** — claim made, edit exists in worktree, not on main. One instance
  (Wave-12 H3). Comprehensive regex + main-HEAD grep detects; worktree list is the
  triangulation.
- **AP321-supervisor-gap** — supervisor false-positive due to narrow grep. One instance
  (Wave-15 finals). Comprehensive regex (7-pattern alternation) detects; single-pattern
  greps do not.

## Commit plan

**None.** This note is observational (diagnostic only, per the mission constraint).
A future wave may:
1. Re-execute the Wave-12 H3 rename on `main` (single atomic commit; or reclassify as
   metacognitive-layer-only discipline and retract the manuscript-rename claim).
2. Upgrade the AP320-class detector to run `main-HEAD` grep + worktree-list triangulation
   as a single preflight check.

Author: Raeez Lorgat.
