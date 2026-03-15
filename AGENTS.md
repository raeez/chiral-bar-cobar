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
2. a proved modular Koszul core (Theorems A/B/C/D/H on the correct loci);
3. complete portraits of the major families;
4. a synthesis/programme layer pointing toward modular homotopy theory
   for factorization algebras on curves.

Do not treat the book as "theory plus examples plus applications."
Treat it as one subject seen from several mathematically precise
vantage points.

## Chriss-Ginzburg Method

The operational model is the introduction and preface of
Chriss--Ginzburg's *Representation Theory and Complex Geometry*.
Interpret that inheritance structurally, not cosmetically.

- **Synthesis before accumulation**:
  this book belongs to the synthesis side of mathematics.  Treat
  representation theory, geometry, physics, and computation as
  coordinated faces of one subject governed by a common theorem graph.
- **Heart before scaffolding**:
  route the reader to the governing mechanism early.  Bring in
  background only when the mechanism demands it; do not front-load an
  encyclopedia of preliminaries.
- **Geometry before bureaucracy**:
  when several proofs are available, prefer the one that exposes the
  controlling geometry or functorial mechanism and lowers conceptual
  overhead, even if another proof is formally more elementary.
- **Mosaic architecture**:
  chapters are tiles in one picture.  Each chapter should answer a
  question inherited from its neighbors and leave behind the next
  unavoidable question.
- **Failure forces generalization**:
  new machinery should appear because the previous level breaks:
  point to curve, genus~0 to higher genus, unordered to ordered,
  scalar to spectral to full package.
- **Accessible local texture**:
  keep the local exposition direct and cognitively light without
  weakening theorem-status precision.  Definitions are earned by the
  computations or tensions that require them.

## Canonical Documents

When working in this repo, consult these in order:

1. [CLAUDE.md](/Users/raeez/chiral-bar-cobar/CLAUDE.md) (conventions, invariants, file map)
2. [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex) (constitution)
3. [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex) (front door)
4. [notes/SESSION_PROMPT_v36.md](/Users/raeez/chiral-bar-cobar/notes/SESSION_PROMPT_v36.md) (live execution prompt)
6. [notes/autonomous_state.md](/Users/raeez/chiral-bar-cobar/notes/autonomous_state.md) (session state)
7. [notes/VISION.md](/Users/raeez/chiral-bar-cobar/notes/VISION.md) (north star)
8. [notes/PROGRAMMES.md](/Users/raeez/chiral-bar-cobar/notes/PROGRAMMES.md) (research programmes)

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

## The Dual Imperative

Two principles govern all work. They are synergistic.

- **Maximalist ambition**: Always push for the most powerful, most
  general theorems. The book yearns toward the shape of theorems
  implied but not yet inked. That yearning is a research signal.
  The target is foundational work, not a survey.
- **Maximal truth-seeking**: Every claim — in TeX, compute scripts,
  review notes, session prompts — is processed with equal rigor.
  Know exactly what is proved, at what level, with what hypotheses.
  This is not conservatism; it is what makes the ambition credible.

The synthesis: precise knowledge of what is proved enables credible
pursuit of the most powerful theorems. Frontier overreach guardrails
exist not to be conservative but to be honest — so the frontier can
be pushed credibly further.

## Chriss-Ginzburg Rewrite Rules

Use these as operational rules, not as literary aspirations:

1. Open chapters with a mathematical question or tension, not a file
   summary; make that question arise from the previous chapter if at
   all possible.
2. Surface the governing mechanism early and import background on
   demand, not as a prerequisite wall.
3. Use the Heisenberg chapter as the frame example whenever a general
   commutative/modular mechanism needs concrete intuition, and Yangian
   when the braided/factorization face is the real entry atom.
4. Introduce new machinery only when a precise obstruction forces it.
5. State bridges between fields as theorems or precise conjectures, not
   as analogies.
6. After a theorem, add at most one shadow sentence pointing to the
   larger programme.
7. Treat examples as generative portraits of the theory, not as
   decoration or verification dumps.
8. Prefer exact mathematical nouns and verbs over evaluative prose.

## Rewrite Workflow

For each file or chapter:

1. Identify its role in the whole-book mosaic.
2. State the question the chapter answers.
3. Check whether its semantic level and status discipline are explicit.
4. Remove catalogue prose and empty transition language.
5. Add cross-references that carry mathematical content.
6. Compile with `make fast` after the edit batch.

## Claude Opus 4.6 / Claude Code High-Reasoning Protocol

Use the following as the execution contract for Claude Opus 4.6 in Claude Code
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
- I am working in a Chriss--Ginzburg synthesis mode: direct route to
  the heart of the subject, background on demand, one governing
  mechanism carried across many surfaces.
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
6. Implied-theorem task:
   use when a structural pattern across proved cases suggests a theorem
   that has not been stated. The book's yearning — theorems implied but
   not yet inked — is a research signal. State the implied theorem as a
   precise conjecture with exact hypotheses. Verify computationally in
   known cases. Prove or mark as conjectural with honest scope remarks.

### Current Routing Facts

These are the non-negotiable current facts inherited from the
`raeeznotes*.md` corpus and already reflected in the control layer:

- MC1 is resolved for the standard finite-type interacting families:
  affine Kac-Moody, Virasoro, and principal finite-type `W_N`.
- Principal finite-type `W_N` belongs in the proved core.
- `W_infty` and Yangian towers do not belong to that resolved
  finite-type PBW story, and the distinct non-principal orbit frontier
  now decomposes into three exact packets: dual-orbit input,
  orbit-indexed level shift, and paired DS seed transport/globalization.
- MC2 is proved: cyclic deformation theory and the universal `Theta_A`
  belong to the proved core. The live frontier now begins with MC3 and
  MC4, with MC5 downstream.
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

These are recurring failure modes. Guard against them explicitly.

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

### Prompting Style

When reasoning, prefer instructions of the following form:

- classify before rewriting;
- identify the breakage that forces the next construction;
- determine the controlling stratum and semantic level;
- ask which uniform mechanism governs the surfaces being connected;
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

The active frontier wave is post-MC1/MC2, with five main theorems
(A/B/C/D/H) and DK-0 through DK-3 proved:

- MC1 and MC2 are proved; the live frontier is MC3/MC4;
- keep principal finite-type `W_N` in the proved core;
- push the next work onto the exact MC4 package for
  `W_\infty` / Yangian towers:
  build the filtered H-level targets, prove the named identities
  `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)` and
  `K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)`, close the finite-detection
  packages `\mathcal{I}_N` and `\Delta_{a,0}(N)`, and keep the distinct
  non-principal orbit frontier separate as its own three exact packets:
  dual-orbit input, orbit-indexed level shift, and paired DS seed
  transport/globalization;
- MC3: coderived/completed enlargement beyond the evaluation-generated
  core remains the principal categorical frontier.

The control layer is stable; the task now is to keep the repo's
scaffolding and frontier artefacts aligned with that stability.

## Safety

- Do not revert user changes unless explicitly asked.
- Prefer editing the control documents before touching downstream
  chapters.
- Use `make fast` for iteration and `make` for a fuller pass.
- If a theorem is still programmatic, say so exactly; do not blur the
  boundary for rhetorical smoothness.
