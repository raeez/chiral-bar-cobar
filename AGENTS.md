# AGENTS.md

## Mission

This repository is not a generic TeX project. It is a long-form
mathematical rewrite project whose immediate objective is:

- make the present manuscript read as Volume I of a larger subject,
  namely **modular homotopy theory for factorization algebras on
  curves**;
- preserve the proved modular Koszul core while separating it cleanly
  from the still-programmatic outer theory;
- rewrite for inevitability, not accumulation.

## North Star

The monograph's mature shape is:

1. a frame example that reveals the whole structure in miniature
   (Heisenberg);
2. a proved modular Koszul core (Theorems A/B/C/D on the correct loci);
3. complete portraits of the major families;
4. a synthesis/programme layer pointing toward modular homotopy theory
   for factorization algebras on curves.

Do not treat the book as "theory plus examples plus applications."
Treat it as one subject seen from several mathematically precise
vantage points.

## Canonical Documents

When working in this repo, consult these in order:

1. [notes/GPT54_CODEX_OPERATING_SYSTEM.md](/Users/raeez/chiral-bar-cobar/notes/GPT54_CODEX_OPERATING_SYSTEM.md)
2. [notes/VISION.md](/Users/raeez/chiral-bar-cobar/notes/VISION.md)
3. [notes/REWRITE_QUEUE.md](/Users/raeez/chiral-bar-cobar/notes/REWRITE_QUEUE.md)
4. [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex)
5. [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex)
6. [main.tex](/Users/raeez/chiral-bar-cobar/main.tex)
7. [CLAUDE.md](/Users/raeez/chiral-bar-cobar/CLAUDE.md)

If two documents disagree, prefer the more recent rewrite doctrine over
older session prompts or legacy agent notes.

## Non-Negotiable Mathematical Discipline

Every substantial edit must preserve these distinctions:

- H/M/S semantics:
  H-level = homotopy-native statement;
  M-level = explicit dg/bar-complex model;
  S-level = cohomological or numerical shadow.
- Construction versus resolution:
  bar/cobar objects may exist beyond the locus where inversion is proved.
- Scalar versus spectral versus full package:
  `kappa` is not `Theta_A`.
- Fiberwise curved differential versus strict total differential:
  do not reuse notation as if they were the same object.
- Status tags:
  every important claim should read as proved, conditional,
  conjectural, or programme.

## Chriss-Ginzburg Rewrite Rules

Use these as operational rules, not as literary aspirations:

1. Open chapters with a mathematical question or tension, not a file
   summary.
2. Use the Heisenberg chapter as the frame example whenever a general
   mechanism needs concrete intuition.
3. State bridges between fields as theorems or precise conjectures, not
   as analogies.
4. After a theorem, add at most one shadow sentence pointing to the
   larger programme.
5. Prefer exact mathematical nouns and verbs over evaluative prose.

## Rewrite Workflow

For each file or chapter:

1. Identify its role in the whole-book mosaic.
2. State the question the chapter answers.
3. Check whether its semantic level and status discipline are explicit.
4. Remove catalogue prose and empty transition language.
5. Add cross-references that carry mathematical content.
6. Compile with `make fast` after the edit batch.

## GPT-5.4 / Codex High-Reasoning Protocol

Use the following as the execution contract for ChatGPT 5.4 in Codex
with extra-high reasoning. The objective is not merely to "improve
prose" but to route work through the correct control surface, preserve
the theorem graph, and exploit the repo's large surface area without
creating status drift.

### Session Startup

Before editing, determine all six items:

1. What is the governing question of the target file?
2. Is the target in Stratum I (proved core) or Stratum II (programme)?
3. Which semantic levels are being touched: H, M, S?
4. Which status vocabulary is legal here: proved, conditional,
   conjectural, programme?
5. Which control document governs the truth conditions for this edit:
   `introduction.tex`, `concordance.tex`, `main.tex`, or a local theorem
   chapter?
6. Is this task upstream doctrine, theorem hardening, portrait
   synchronization, frontier reset, or compute-supported evidence?

If any of these are unclear, read upward in the control stack before
changing downstream files.

### Default Internal Brief

At session start, silently adopt this brief:

- I am maintaining Volume I of modular homotopy theory for
  factorization algebras on curves, not polishing isolated TeX.
- The proved modular Koszul core is the load-bearing object; the outer
  programme must remain explicit and correctly fenced.
- Chapter 34 is constitutional when status language drifts elsewhere.
- I must distinguish construction from resolution, scalar from
  spectral from full package, and fiberwise curvature from strict total
  differential before I touch exposition.
- I widen first by locating the controlling surface, then narrow to the
  smallest edit that propagates the correct doctrine.

### Task Routing Across the Repo

Route each task to the right surface before editing.

1. Control-layer task:
   use when a claim's status, theorem scope, part architecture, or
   chapter role changes. Edit `introduction.tex`,
   `concordance.tex`, and `main.tex` before local chapters.
2. Theorem-hardening task:
   use when a definition, theorem statement, proof dependency, or
   semantic-level distinction is unstable. Prefer theory chapters and
   local dependency digests before examples.
3. Portrait-synchronization task:
   use when example chapters, summary tables, or family narratives lag
   behind the proved core. Keep each family a portrait of one subject,
   not an isolated calculation dump.
4. Frontier-reset task:
   use when a formerly open frontier has moved. Propagate the new state
   through concordance, metadata, notes, and examples in one batch.
5. Compute-surface task:
   use when theorem-level claims depend on explicit evidence,
   diagnostics, or test scaffolding. Keep compute outputs at M/S-level
   unless a theorem already promotes them.

### Current Routing Facts

These are the non-negotiable current facts inherited from the
`raeeznotes*.md` corpus and already reflected in the control layer:

- MC1 is resolved for the standard finite-type interacting families:
  affine Kac-Moody, Virasoro, and principal finite-type `W_N`.
- Principal finite-type `W_N` belongs in the proved core.
- `W_infty`, Yangian towers, and non-principal orbit duality do not
  belong to that resolved finite-type PBW story.
- The principal open foundational target is MC2: cyclic deformation
  theory and the universal `Theta_A`.
- Periodicity remains the weakest status flank and must be stated with
  extra caution.

### Pass Types

When a task is broad, choose one pass type explicitly and complete it
end-to-end instead of mixing several half-passes.

1. Doctrinal propagation pass:
   synchronize local chapters with the current control doctrine.
2. Theorem linearization pass:
   remove circularity, sharpen hypotheses, and make the dependency
   graph acyclic on the page.
3. Entry-point pass:
   rewrite chapter openings around a mathematical tension, governing
   question, and chapter role.
4. Portrait pass:
   make examples reveal distinct faces of the same theory and inherit
   the correct status language.
5. Frontier pass:
   move stale "live conjectures" into the right resolved/open buckets
   across concordance, metadata, examples, and notes.
6. Periodicity containment pass:
   downgrade any periodicity language that outruns the printed proof and
   restate the chapter around the periodicity profile, structural lcm
   bound, and explicit conjectural scope.

### High-Leverage Execution Loop

For nontrivial work, follow this loop:

1. Read the control node and the target file together.
2. Write down the governing question, stratum, semantic levels, and
   legal status language.
3. Identify the smallest authoritative file set that must move
   together.
4. Make the theorem-status boundaries explicit before polishing prose.
5. Rewrite the opening, theorem statements, and bridge sentences so the
   mathematical route is visible.
6. Propagate the new doctrine forward to obvious summaries, tables,
   examples, and frontier ledgers.
7. Compile with `make fast`.

### Failure Modes To Prevent

These are recurring Codex and manuscript failure modes. Guard against
them explicitly.

- Local patching before reading the control layer.
- Treating Chapter 34 as commentary instead of constitutional status
  ledger.
- Allowing S-level evidence or tables to leak into H-level claims.
- Writing "full package" when only scalar or spectral data are proved.
- Reusing one differential notation for `d_fib` and `D_tot`.
- Treating bar/cobar existence as if it automatically implies
  inversion.
- Using Heisenberg as proof of the full package rather than as the atom
  of the scalar/spectral story.
- Letting periodicity claims outrun the argument.
- Forgetting that principal finite-type `W_N` is resolved while
  `W_infty` and non-principal orbit questions remain frontier.
- Editing downstream portraits without updating upstream doctrine.
- Producing elegant local prose that leaves the theorem graph or status
  ledger inconsistent.

### Prompting Style For Codex

When reasoning, prefer instructions of the following form:

- classify before rewriting;
- determine the controlling stratum and semantic level;
- state the exact theorem/conjecture boundary;
- identify the parent master conjecture, if any;
- propagate status changes through every dependent summary surface;
- prefer one decisive doctrinal batch over many local cosmetic edits.

Avoid vague prompts such as "improve this chapter" or "make this more
compelling" unless they are immediately grounded by governing question,
semantic level, and status target.

### Definition of Done

A pass is complete only if all relevant items are true:

- the chapter or file now states its governing question;
- the stratum and status language are correct;
- H/M/S drift has been reduced, not increased;
- scalar, spectral, and full-package language are separated;
- `d_fib` and `D_tot` are not conflated;
- MC1/MC2/MC3/MC4/MC5 status is current;
- control documents and downstream summaries agree;
- `make fast` has been run after the edit batch.

## Current Priority

The active frontier wave is post-MC1 synchronization:

- propagate the resolved higher-genus PBW theorem state through control
  notes and frontier ledgers;
- keep principal finite-type `W_N` in the proved core;
- push the next `W` work onto the filtered H-level comparison /
  realization packages for `W_\infty` / Yangian towers, with the
  theorematic completed M-level principal-stage package treated as
  already in hand, and onto non-principal orbit duality.

The control layer is stable; the task now is to keep the repo's
scaffolding and frontier artefacts aligned with that stability.

## Safety

- Do not revert user changes unless explicitly asked.
- Prefer editing the control documents before touching downstream
  chapters.
- Use `make fast` for iteration and `make` for a fuller pass.
- If a theorem is still programmatic, say so exactly; do not blur the
  boundary for rhetorical smoothness.
