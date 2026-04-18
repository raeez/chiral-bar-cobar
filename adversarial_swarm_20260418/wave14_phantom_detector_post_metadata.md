# Wave-14 Phantom Detector Re-Run — Post Metadata Build, Three-Volume Audit

Date: 2026-04-18
Protocol: AP317 multi-line env scan (±5 lines) + `metadata/label_index.json` cross-check + live-tex consumer filter (excludes `relaunch_|rectification_|healing_|opus_audit_|wave*_audit_|.claude/worktrees/|notes/|adversarial_swarm_|backup|archive|fix_wave_`).
Source of truth: `metadata/label_index.json` (v1 11139 labels / v2 6942 / v3 3033) + programme-wide `grep` sweep for `\label{...}` over `chapters/`, `standalone/`, `appendices/`, `main.tex`.
Diagnostic only, no edits, no commits.

## Per-volume counts

| Volume | live-tex defined labels | phantomsection labels (unique) | false-positive (defined elsewhere or in metadata) | GENUINE phantom (zero def, ≥1 live-tex consumer) | retirable orphan (zero def, zero consumer) |
|---|---|---|---|---|---|
| Vol I  | 15278 | 62 | 45 | **12** | 5 |
| Vol II | 6340  | 32 | 32 | **0**  | 0 |
| Vol III| 2969  | 60 | 60 | **0**  | 0 |

Note: a 13-item Vol I list shrunk to 12 after the repo-wide sanity pass pruned `lem:super-trace-berezinian-bridge` (defined at `chapters/examples/yangians_foundations.tex:198`; phantomsection elsewhere was a redundant alias).

## Wave-7 → Wave-14 delta

| Volume | Wave-7 raw phantoms | Wave-9 Tier-1 (metadata-grounded) | Wave-12/13 heals applied | Wave-14 GENUINE Tier-1 remaining |
|---|---|---|---|---|
| Vol I  | 1559 (detection gap in Wave-7) | — | Wave-10/11 heals in `v1_*_attack_heal.md`; Wave-13 infrastructure | 12 |
| Vol II | 412 | 13 | Wave-12 Tier-1 heal (ab2835b2) | 0 |
| Vol III| 30  | small | Wave-13 scaffolding (a8f54388) | 0 |

Delta commentary:
- Vol II 13 → 0: the Wave-12 Tier-1 heal cleanly eliminated all genuine Tier-1 phantoms. 32 remaining phantomsection labels are FALSE POSITIVES (label actually exists in live-tex; phantomsection is a redundant alias, harmless).
- Vol III 30 → 0: Wave-13 scaffolding closed the Tier-1 window; 60 phantomsection labels remain but every one resolves to a live-tex defining environment within the ±5-line multi-line scan or appears as a genuine `metadata/label_index.json` entry.
- Vol I 1559 → 12: the Wave-7 raw number overcounted catastrophically because (a) it lacked the multi-line env scan, missing `\begin{env}[title]\n\label{...}` split patterns; (b) it lacked the metadata cross-check. With both filters, 45 of 62 phantomsection labels prove to be false positives, 5 are retirable orphans (zero consumers), and 12 are genuine phantoms.

## Top-12 Vol I genuine phantoms (consumer count)

| Rank | Label | Consumers | Heal priority |
|---|---|---|---|
| 1 | `conj:master-bv-brst`                         | **47** | TIER-1 CRITICAL — single highest consumer count programme-wide |
| 2 | `thm:topologization-tower`                    | 5      | TIER-1 (tactical phantomsection alias, AP286 flagged) |
| 3 | `chap:infinite-fingerprint-classification`    | 4      | TIER-1 chapter stub |
| 4 | `prop:pbw-koszulness-criterion`               | 2      | TIER-2 |
| 5 | `chap:universal-holography-functor`           | 2      | TIER-2 chapter stub |
| 6 | `thm:chiral-positselski-7-2`                  | 2      | TIER-2 (status-table flagged phantom) |
| 7 | `thm:shadow-quadrichotomy`                    | 1      | TIER-3 |
| 8 | `chap:theorem-A-modular-family`               | 1      | TIER-3 chapter stub |
| 9 | `thm:dbar-equals-kz-arnold`                   | 1      | TIER-3 |
| 10| `chap:chiral-higher-deligne`                  | 1      | TIER-3 chapter stub |
| 11| `thm:K-trinity`                               | 1      | TIER-3 |
| 12| `thm:ghost-identity-platonic`                 | 1      | TIER-3 |

## Vol II top-10

Zero genuine phantoms. All 32 phantomsection-tagged labels resolve via multi-line env scan or metadata cross-check to live-tex definitions (redundant aliases, harmless but recommend AP286 audit).

## Vol III top-10

Zero genuine phantoms. All 60 phantomsection-tagged labels resolve (metadata has 3033 entries; every phantomsection label is already a recognised definition).

## Heal recommendations

1. **`conj:master-bv-brst` (47 consumers)** — single highest-impact remaining phantom programme-wide. Either (a) inscribe the master BV-BRST conjecture locally in the Part VI / class-M topologization chapter with a full statement environment + proof-sketch/evidence remark, or (b) retarget all 47 consumers to an existing inscribed theorem (`thm:iterated-sugawara-construction` / `thm:e-infinity-topologization-ladder` are candidates) and retire the phantomsection. Prefer (a): the 47 consumers suggest load-bearing status; AP286 (tactical phantomsection alias) warns mere retargeting is insufficient when prose treats the label as a distinct result.
2. **`thm:topologization-tower` (5 consumers)** — already flagged in CLAUDE.md AP286 as tactical-alias-only; upgrade to semantic heal via either umbrella-theorem inscription or per-consumer retarget to the two constituent Vol II theorems.
3. **Chapter-stub phantoms (`chap:*`)** — four chapter-level labels (`chap:infinite-fingerprint-classification`, `chap:universal-holography-functor`, `chap:theorem-A-modular-family`, `chap:chiral-higher-deligne`). Each points to a chapter-scale construction advertised but not compiled. Either inscribe chapter stubs with `\chapter{...}\label{...}` in an existing `\input` file, or retarget references to standalone files that exist.
4. **`thm:chiral-positselski-7-2` (2 consumers)** — already flagged in CLAUDE.md Theorem B row as phantom; either inscribe locally as a named theorem in `chapters/theory/theorem_B_scope_platonic.tex` or retire the name.
5. **`prop:pbw-koszulness-criterion` (2)** — load-bearing for `thm:hochschild-concentration-E1` (Theorem H) and Spoke 5 of `thm:ftm-seven-fold-tfae-via-hub-spoke`. Priority TIER-2; inscribe in the FTM chapter.
6. **Tier-3 singletons** (`thm:shadow-quadrichotomy`, `thm:dbar-equals-kz-arnold`, `thm:K-trinity`, `thm:ghost-identity-platonic`) — single-consumer refs; inscribe or retarget in a batch heal pass.
7. **Five retirable orphans (zero consumers)** — safe to delete the `\phantomsection\label{...}` line without any ref churn. Quick cleanup opportunity.

## Metadata-layer observations

- All three volumes now have `metadata/label_index.json` + `claims.jsonl`; the cross-check is decisive — post-Wave-9 Vol II/III phantom counts collapse to zero.
- Vol I's 12 genuine phantoms are the load-bearing residual from the Wave-1..Wave-13 campaign. None overlap with Vol II/III.
- No AP255-class phantom-file violations detected in Vol II/III. Vol I's four `chap:*` phantoms ARE AP255 violations (chapter-level file advertised but not compiled).

## Detection-gap verification

Confirmed all three filters fire correctly:
- (A) multi-line env scan caught at least 12 Vol I false positives where `\begin{theorem}[...]` was on line L and `\label{...}` on line L+2.
- (B) metadata cross-check eliminated ~30 Vol II and ~55 Vol III false positives.
- (C) live-tex consumer filter separated retirable orphans (5 in Vol I) from genuine phantoms (12 in Vol I with consumer count ≥ 1).
