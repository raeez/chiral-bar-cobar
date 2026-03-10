# GPT-5.4 / Codex Operating System for the Monograph

This file is the stable cognitive scaffolding for future model-assisted
work on the monograph. It replaces ad hoc session-memory with a compact
rewrite doctrine.

## 1. Governing Aim

The present manuscript should be rewritten so that its natural subject
is unmistakable:

**modular homotopy theory for factorization algebras on curves**

The proved content already yields a substantial first volume of that
subject. The rewrite should make the proved modular Koszul core read as
Stratum I of the larger theory, not as a disconnected accumulation of
results.

### The Dual Imperative

Two principles govern all work. They amplify each other.

- **Maximalist ambition**: Always push for the most powerful, most
  general theorems. The book yearns toward the shape of theorems
  implied but not yet inked — that yearning is a research signal,
  not idle aspiration. The target is foundational work that changes
  how the subject is understood.
- **Maximal truth-seeking**: Every claim processed with equal rigor —
  TeX source, compute scripts, review notes, session state. Know
  exactly what is proved, at what level, with what hypotheses. When
  claims outrun proofs, strengthen the proof first.

The synthesis: precise knowledge of what is proved enables credible
pursuit of the most powerful theorems. Frontier discipline is not
conservatism — it is honesty that lets the frontier be pushed further.

## 2. Working Understanding of the Book

The durable understanding from the `raeeznotes*.md` sequence is:

- the theorematic spine A/B/C/D is now materially stronger;
- the former MC1 bottleneck is resolved for the standard finite-type interacting families
  (KM, Virasoro, principal finite-type `W_N`);
- the foundational live mathematical frontier is now MC2, while
  periodicity remains an orthogonal weak flank;
- the live `W` frontier is now the filtered H-level /
  coefficient-identification package for `W_\infty` and Yangian towers:
  prove the named identities
  `K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)` and
  `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)`, close the corresponding
  finite-detection packages, and separate that work from the distinct
  non-principal orbit-duality frontier, whose exact remaining packets are:
  the dual-orbit input package, the orbit-indexed level-shift package,
  and the paired DS seed-transport/globalization package;
- the main structural weakness is backward propagation of the new status
  discipline;
- Chapter 34 / concordance is the control ledger;
- the Yangian evaluation-locus Drinfeld-Kohno square now functions as a
  secondary entry atom for the braided/factorization face of the
  subject, but the extension beyond the evaluation locus and the
  dg-shifted comparison remain downstream frontier work;
- the book is strongest when split into two strata:
  proved modular Koszul core and programmatic modular homotopy theory.

## 3. Final-Form Architecture

Use the following architecture as the canonical target.

### Layer A: Frame

- Heisenberg as the smallest example carrying the whole structure.
- Secondary entry atom for the noncommutative face: the Yangian
  evaluation-locus Drinfeld-Kohno square, which isolates ordered
  factorization and braid reversal without displacing Heisenberg as the
  primary frame.
- Purpose: inevitability, not pedagogy.

### Layer B: Proved core

- Theorems A/B/C/D on the correct loci.
- Scalar and spectral characteristic packages.
- Evaluation-locus or chain-level bridges that are actually proved.

### Layer C: Complete portraits

- Major families computed as full portraits, not as decorative examples.
- Each family should reveal a new face of the general machine.

### Layer D: Synthesis and programme

- The proved bridges to representation theory, geometry, and physics.
- The resolved entry theorem on higher-genus PBW concentration together
  with the dependency-ordered frontier:
  MC2 as foundational target, MC3/MC4 as structural extensions,
  and MC5 as downstream consequence.
- The explicit next subject: modular homotopy theory for factorization
  algebras on curves.

### Layer E: Implied theorems (the yearning)

- The book wants to become something not yet stated. When proved
  theorems converge on a structural pattern that no single theorem
  captures, that pattern is a research signal.
- State implied theorems as precise conjectures with exact hypotheses.
  Test computationally. Prove or mark with honest scope remarks.
- This is not speculative decoration — it is the maximalist ambition
  made operational by the discipline of maximal truth-seeking.

## 4. Chriss-Ginzburg Lessons to Enforce

The relevant lesson is not style mimicry. It is structural discipline.

1. Governing question:
   every chapter should answer a mathematical question the previous
   chapter made unavoidable.
2. Frame example:
   one example should make the whole theory visible before the abstract
   machinery is unfolded.
3. Inevitability through failure:
   generalization should arise because the previous level breaks.
4. Synthesis as theorem:
   disparate subjects are connected by functors, equivalences, or named
   conjectures, not by analogy language.
5. Delayed payoff:
   earlier constructions should later reappear as the solution to a
   problem the reader now genuinely has.
6. Vocabulary discipline:
   every sentence must do mathematical work.

## 5. Semantic and Status Matrix

Every major object or claim should be placeable in this matrix.

### Semantic level

- H-level: stable/coderived/factorization/formal-moduli statement.
- M-level: explicit dg, filtered, curved, or bar-cobar model.
- S-level: cohomology, dimensions, generating series, tables.

### Status

- proved
- conditional
- conjectural
- programme

### Stratum

- Stratum I: proved modular Koszul core
- Stratum II: modular homotopy theory programme

If an edit obscures any of these three coordinates, it is a bad edit.

## 6. Core Boundaries That Must Stay Sharp

- `kappa(A)` is the scalar shadow, not the full package.
- `Theta_A` is the principal open homotopy object.
- bar/cobar existence is broader than inversion.
- fiberwise curved differential and strict total differential are not
  interchangeable notation.
- periodicity claims must not outrun the argument.

## 7. Control Documents

The repo has three text-control layers:

1. [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex)
   Front door: tells the reader what subject the book is.
2. [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex)
   Status ledger: authoritative boundary between theorem and programme.
3. [main.tex](/Users/raeez/chiral-bar-cobar/main.tex)
   Part architecture: controls the reader's large-scale map.

Any whole-book rewrite should start here.

## 8. Model Workflow

When ChatGPT 5.4 or Codex works on the book:

1. Read the relevant control docs first.
2. Identify the chapter's governing question.
3. Identify its stratum, semantic level, and status mix.
4. Rewrite the opening so the chapter enters through a question or
   tension, not a summary.
5. Add one retrospective link and one forward shadow where appropriate.
6. Remove empty catalogue prose.
7. Compile after the batch.

## 9. Rewrite Priorities

Priority order for the active rewrite campaign:

1. Propagate the resolved MC1 status through control notes, examples,
   frontier ledgers, and any remaining local summaries.
2. Keep finite-type principal `W_N` in Stratum I and isolate
   `W_\infty` / Yangian H-level comparison problems and non-principal
   orbit duality in Stratum II, with the latter decomposed into
   dual-orbit input, orbit-indexed level-shift, and paired DS
   seed-transport packets.
3. Advance MC2 first: the theorem surface now reduces the cyclic
   deformation / universal `Theta_A` frontier to three exact packages,
   namely the intrinsic cyclic `\Defcyc(\cA)` model, the geometric
   completed tensor / clutching package, and the one-channel
   genus-by-genus normalization problem in the simple-Lie case.
4. Treat MC3 and MC4 as the next structural comparison layer after the
   standard M-level completions, not as missing finite-type PBW input.
5. Treat periodicity as an auxiliary weak flank: contain, clarify, and
   never let it outrun the proved core or the MC2 -> MC3/MC4 -> MC5
   dependency order.
6. Repair any local theorem statements whose status still drifts from
   Chapter 34.

## 10. Definition of Success

Success is not "the book sounds grander." Success is:

- the reader can tell, from the opening and the concordance alone, what
  is proved and what is programme;
- the Heisenberg frame makes the abstract machinery feel necessary;
- the examples read as complete portraits of one subject;
- the final target is explicit:
  modular homotopy theory for factorization algebras on curves.
