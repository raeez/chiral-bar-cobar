---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the full target file
- the directly cited dependencies

## Rectification loop

1. Identify the organizing question of the target.
2. Identify the actual climax:
   the theorem, construction, or proof step the file is really carrying
3. Diagnose before editing:
   narrative breaks
   define-before-use failures
   cold definitions
   scope inflation
   status drift
   formula red flags
4. Rectify the structure before the line noise:
   cut dead weight
   move prerequisites earlier
   narrow overclaims
   rewrite transitions so they carry mathematics, not signposts
5. Sweep the touched surface chunk by chunk:
   audit
   repair
   re-audit
   repeat until the chunk converges or the blocker is explicit
6. After every substantive theorem-surface change, sync nearby status remarks, concordance text, duplicates, and metadata.
7. Run the strongest local verification available and close with a proved/computational/conditional split.

## Style standard

- Every definition should answer a question the reader already has.
- Every transition should say:
  where we are,
  what forces the next step,
  and what resolves it
- Delete filler, hedging, and ceremonial signposting.
- Never trade exactness for grandeur.

## Failure rule

If a strong version of the claim will not close, do not keep polishing it. Demote it, fence it, or mark it conditional.

## Parallel work

Only use subagents if the user explicitly asks for parallel or delegated agent work. If they do, split by disjoint files or disjoint write scopes.

