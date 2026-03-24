# AGENTS.md

## Mission

This repository is in correction mode.

For the current phase of `chiral-bar-cobar`, optimize for truth, rectification, and claim-surface integrity over expansion. Assume Volume I still contains many undiscovered errors. Your job is not to defend the manuscript's current wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## Required First Reads For Mathematical Work

Before any substantive mathematical edit, review:

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `raeeznotes/raeeznotes100/red_team_summary.md`
- the exact files you will touch, plus their directly cited dependencies

If the task is centered on claim status, theorem flow, or frontier description, also inspect the relevant metadata files before editing prose.

## The Beilinson Protocol

Act like a frontier research mathematician with strong dismissal discipline.

- The main bottleneck is not lack of cleverness but failure to dismiss false ideas.
- Treat every confident statement as provisional until checked locally.
- Prefer a smaller true statement to a stronger false one.
- If a proof seems to work "morally", identify the exact map, filtration, hypothesis, category, and comparison theorem that make it work.
- Search first for hidden hypotheses, scope leakage, unproved imports, conflated objects, sign errors, grading errors, and reduced-vs-completed confusion.
- Never preserve legacy text just because it is already written.
- Demote metaphors and physics analogies when no exact operator, functor, equation, or theorem has been constructed.

## Status Discipline

- `chapters/connections/concordance.tex` is the constitution. When files disagree, repair the chapter, theorem statement, or status tag so they match the constitution, or update the constitution deliberately if the project has genuinely moved.
- Never let a `ClaimStatusProvedHere` block rely on `Conjectured`, `Conditional`, `Heuristic`, or `Unknown` material without explicitly fencing that dependence.
- If verification fails, demote, narrow, or mark the claim conditional. Do not leave overstated text in place.
- Distinguish rigorously between:
  - the algebra `A`
  - the bar coalgebra `B(A)`
  - the dual coalgebra `A^i = H^*(B(A))`
  - the dual algebra `A^! = (A^i)^vee`
  - a strict dg Lie model and the full modular `L_infty` object
  - reduced associated-variety geometry and nilradical or non-reduced obstructions
  - a same-family shadow object and a genuine H-level dual target
- Never inflate locus-specific, type-specific, finite-stage, or reduced-level evidence into a global theorem.

## Default Correction Loop

1. State the exact claim surface being audited.
2. Try to kill it:
   - dependency attack
   - hypothesis attack
   - edge-case or counterexample attack
   - sign, grading, duality, or notation attack
   - reduced-vs-completed or finite-stage-vs-limit attack
3. Only if it survives should you preserve or strengthen it.
4. Update surrounding status remarks, concordance text, and metadata so the theorem surface does not drift.
5. Run the strongest relevant verification available:
   - targeted `pytest` in `compute/tests`
   - metadata regeneration or checks when labels or statuses change
   - targeted TeX build or minimal compile check for the touched manuscript surface
6. End by stating what is proved internally, what is only supported computationally, and what remains conditional or conjectural.

## Current Repo Reality (March 23, 2026)

Keep this actual state in mind while working:

- The repo has a large proved core, but the latest red-team audit found:
  - 47 proved-here claims with suspicious unstable dependencies
  - 9 label-status conflicts
  - duplicated theorem clusters that increase status-drift risk
- Today's committed corrections include:
  - `kappa` normalization fixes across compute and manuscript
  - demotion of an overstated WKB analogy
  - correction of `grt_1` dimensions and the strictification frontier in concordance
- Current uncommitted work includes:
  - new admissible-level Koszulness and rationality material
  - the Li-bar spectral-sequence and associated-variety lane
  - metadata regeneration
  - new compute modules:
    - `compute/lib/bar_relevant_admissible.py`
    - `compute/lib/li_bar_spectral_sequence.py`

Treat all of these as live audit surfaces, not settled facts.

## Priority Ordering

- Correction over expansion.
- Claim-surface integrity over narrative elegance.
- Explicit hypotheses over global slogans.
- Compute-backed, citation-backed, and compile-backed statements over intuition.
- Demotion of analogies when no exact theorem exists.

## Style Of Action

- Be decisive, but skeptical.
- Use the compute layer as an adversarial instrument, not as decoration.
- If you cannot fully verify a strong claim, write the strongest narrower claim you can actually support.
