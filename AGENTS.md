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

## Current Priority

The active frontier wave is post-MC1 synchronization:

- propagate the resolved higher-genus PBW theorem state through control
  notes and frontier ledgers;
- keep principal finite-type `W_N` in the proved core;
- push the next `W` work onto completed infinite-generator bar theory
  (`W_\infty` / Yangian towers) and non-principal orbit duality.

The control layer is stable; the task now is to keep the repo's
scaffolding and frontier artefacts aligned with that stability.

## Safety

- Do not revert user changes unless explicitly asked.
- Prefer editing the control documents before touching downstream
  chapters.
- Use `make fast` for iteration and `make` for a fuller pass.
- If a theorem is still programmatic, say so exactly; do not blur the
  boundary for rhetorical smoothness.
