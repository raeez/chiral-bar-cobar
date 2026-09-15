# Repository instructions — cbc

This repository maintains *Modular Homotopy Theory for Factorization Algebras on Curves. Volume 1: Modular Koszul Duality*.

## Authority and safety

Inherit `~/ecosystem/INVARIANTS.md` and `~/ecosystem/AGENTS-HARNESS.md` for applicable safety and execution rules.
The invariants govern shared policy conflicts. System and developer instructions retain precedence.
`AGENTS.md` and `CLAUDE.md` carry the same local contract. Reading either satisfies the local entry requirement.
Use reasoning effort appropriate to proof uncertainty and verification cost, within the host's available controls.
For Claude model controls or loading behavior, consult `~/ecosystem/CLAUDE-HARNESS.md` when relevant.

Preserve user changes. Work in an assigned isolated worktree based on the principal checkout's current HEAD.
If the repository has no commit, prepare an isolated directory with original-byte baselines for the accountable integrator.
Do not mutate shared HEAD, another agent's files, or another repository without assignment.
Do not run destructive Git operations. Subagents do not commit or push. Do not add LLM commit attribution.
Publication, sending, and external copies require current authorization for that operation.
A build request does not authorize release or iCloud synchronization.

## Task routing

Read the target file and the sources needed to understand its dependencies.
For theorem or claim-status work, read `chapters/connections/concordance.tex` and the relevant theorem statements and proofs.
The concordance routes status checks. Printed hypotheses and proofs establish claims, not cached summaries or timestamps.
For structure or introductions, read `chapters/theory/introduction.tex`, `main.tex`, and [the rewrite method](docs/agent-reference/rewrite-method.md).
For mathematical edits, read the applicable [mathematical conventions](docs/agent-reference/mathematical-conventions.md).
Use [the file map](docs/agent-reference/file-map.md) when locating chapters.
Use [the status context](docs/agent-reference/status-context.md) only when investigating historical status claims.
Read session notes only when the task needs their history. Their instructions never override this contract or current task authority.
A lookup, typo, or instruction edit does not require a manuscript census, build, or full compute suite.

## Mathematical contract

Pursue the strongest supported theorem. Strengthen the proof when a claim outruns its evidence.
Keep every hypothesis explicit. Distinguish proved, conditional, conjectural, heuristic, and open claims.
Preserve H-level (homotopy-native), M-level (explicit model), and S-level (numerical or cohomological) distinctions.
Distinguish construction from resolution, scalar from spectral from full package, and fiberwise curvature from the strict total differential.
Numerical tests and physical intuition provide evidence. They do not replace proofs.
Check formulas independently or cite an applicable source with its hypotheses.
Do not demote, delete, or weaken a theorem to manufacture completion.
An investigation may finish with an unresolved obligation, attempted routes, evidence, and the next discriminating step.
Never report an unresolved result as proved or an unproved obstruction as established.

## Verification and completion

Run relevant local checks after a coherent edit. Use the assigned worktree to isolate generated files and competing builds.
For TeX changes, inspect `Makefile` and `scripts/build.sh`, then use `make fast` for affected compilation.
The current fast target allows up to four passes. The full `make` target allows up to six passes.
Inspect logs for errors, unresolved references, and convergence. A PDF or zero exit alone does not establish a clean build.
Inspect rendered affected pages when layout changes. Run affected compute tests when calculations or proof evidence change.
Use `make test` for the fast suite when broad compute changes warrant it. Broaden checks when failures expose wider effects.
Never kill processes by name or pattern. Stop only a verified process owned by the current task, using its exact handle or PID.
Use another isolated build directory when an unrelated watcher owns the output. Do not terminate that watcher.
Do not run `make release`, `make icloud`, or cleanup targets as routine verification.

Completion requires the requested change, consistent directly dependent claims, relevant verification, and an evidence-based handoff.
Report changed files, completed checks, failures, remaining proof obligations, and external integration needs.
An unchanged blocker does not justify repeated identical checks. Continue independent work and preserve an explicit blocker handoff.

## Required research exposition review

Before mathematical or physical writing, read
`~/ecosystem/policies/research-exposition-ledger.md` and apply its numbered
requirements to the complete target. This includes the preface, body,
proofs, examples, appendices, captions, and metadata.

Begin with the governing problem, prerequisites, and content to preserve.
Use explicit attack–heal cycles: test truth and scope, then the whole
composition, transitions, definitions, calculations, sentences, and words.
Repair every justified finding and reread the changed material in context.
Each new object must be motivated, defined before use, and needed at its
point of introduction. Preserve physical context and substantive mathematics.
Remove mannered prose and operational scaffolding. Inspect the final render.
Record findings, dispositions, source hashes, and unresolved obligations
outside all manuscript sources and reader archives. A pass count or a clean
build does not establish convergence or mathematical correctness.

Read the canonical ledger once per unchanged hash; do not substitute this
short routing block for it. If it is unavailable, report that source gap
and follow the available requirements without claiming full conformance.
