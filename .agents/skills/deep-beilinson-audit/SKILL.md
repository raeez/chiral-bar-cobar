---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

## Audit protocol

1. Fix the audit surface exactly:
   file, theorem label, formula, paragraph, compute module, or claim cluster
2. State the current claimed status:
   proved here, compute-backed, conditional, conjectural, heuristic, or open
3. Try to kill the claim:
   dependency attack
   hidden-hypothesis attack
   scope attack
   notation or object-conflation attack
   sign or grading attack
   reduced/completed or finite-stage/limit attack
   counterexample or edge-case attack
4. Recompute formulas from first principles whenever feasible. Do not verify by pattern matching against nearby text.
5. Read the cited proof steps. Check that each imported result is used with its hypotheses satisfied.
6. Check whether the same claim or formula appears elsewhere and is drifting in status or wording.
7. If the user asked for correction as well as audit, apply the minimal true fix and propagate it across duplicates.
8. Run the strongest relevant verification and end with an explicit proved/computational/conditional split.

## Severity rubric

- `CRITICAL`: false theorem surface, circular proof, or proved-here claim leaning on weaker material
- `SERIOUS`: wrong formula, wrong scope, wrong object, unstable dependency, or convention error
- `MODERATE`: misleading prose, missing qualification, stale status sync, or incomplete verification
- `MINOR`: wording, exposition, or low-risk cleanup

## Output contract

If the user asked for a review or audit, present findings first, ordered by severity, with exact file references.

If no findings survive, say so explicitly and still mention residual risks or verification gaps.

## Parallel work

Only use subagents if the user explicitly asks for parallel or delegated agent work. If that happens, split audits by independent scope, not by overlapping edits.

