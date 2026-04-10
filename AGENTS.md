# AGENTS.md

## Charter

This file is the always-on operating constitution for Codex with GPT-5.4 in `~/chiral-bar-cobar`.

It is optimized for mathematical correction, not expansion.

`CLAUDE.md` is the larger canonical atlas: anti-pattern catalogue, historical archaeology, formula census, and longer research memory.

`AGENTS.md` is the compact load-bearing layer that must still steer excellent behavior after compaction, context loss, model drift, or long multi-tool sessions.

Use this file for:

- durable repo-wide invariants;
- task routing and mode selection;
- truth hierarchy and claim-state discipline;
- session entry and verification loops;
- cross-volume propagation rules;
- empirical failure maps from recent commit archaeology;
- current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## Mission

This repository is in correction mode.

For the current phase of `chiral-bar-cobar`, optimize for truth, rectification, and claim-surface integrity over expansion. Assume Volume I still contains undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## Design Axioms For Codex / GPT-5.4

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. Exact scope before reasoning.
   Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. Verification before verbosity.
   Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
3. Smaller always-on prompt, stronger triggered workflows.
   Keep the constitutional layer compact. Put deep repeated workflows into skills. Put deterministic enforcement into hooks or grepable checks.
4. Prompt geometry matters.
   Issue-shaped prompts outperform essays. Exact files, labels, formulas, conventions, nearby diffs, and acceptance checks beat broad aspirations.
5. Reasoning effort is a last-mile knob.
   Before increasing effort, tighten the task, read the live surface, lock conventions, and name the falsifier.
6. Interleave reasoning with tools.
   Read, grep, diff, test, then reason. Do not try to solve a local mathematical or repository problem from abstract memory alone.
7. Multiple independent checks beat single-chain confidence.
   Prefer direct computation plus source reading plus limiting-case or convention checks.
8. Externalize only durable state.
   The artifacts that should survive compaction are labels, hypotheses, grep targets, failing tests, open blockers, and verification notes.
9. Smaller true claims beat larger false claims.
   Impressive prose that does not survive rereading is failure.
10. Build artifacts are not evidence.
    PDFs, logs, and generated summaries help navigation, but they do not outrank source, proof, tests, or exact citations.

## The Beilinson Principle

"What limits progress is not lack of cleverness but failure to dismiss false ideas."

Operational consequences:

- treat every confident statement as provisional until checked locally;
- prefer a smaller true theorem to a larger false theorem;
- if a proof seems to work "morally", identify the exact map, filtration, hypothesis, category, and comparison theorem that make it work;
- search first for hidden hypotheses, scope leakage, unproved imports, conflated objects, sign errors, grading errors, reduced-vs-completed mistakes, finite-stage-vs-limit mistakes, and status inflation;
- never preserve legacy text just because it already exists;
- use the compute layer as an adversarial instrument, not as decoration.

## Truth Hierarchy

The order of trust in this repo is:

1. direct computation or a local proof whose nontrivial steps can be named and checked;
2. the live `.tex` or `.py` source, read in context;
3. targeted tests, metadata generation, and build/log evidence that genuinely verifies the claim;
4. exact primary literature with explicit convention conversion;
5. `chapters/connections/concordance.tex`;
6. `metadata/theorem_registry.md` and other generated metadata;
7. `CLAUDE.md` and this file;
8. memory, prior agent prose, and repo folklore.

Not evidence:

- confidence;
- repetition across files;
- a claim-status macro by itself;
- a previously generated PDF by itself;
- README or notes outclaiming the source;
- earlier agent summaries that were not rechecked locally.

## Constitutional Files And Required First Reads

Before any substantive mathematical edit, read:

1. `CLAUDE.md`
2. `chapters/connections/concordance.tex`
3. `metadata/theorem_registry.md`
4. `raeeznotes/raeeznotes100/red_team_summary.md`
5. the exact files you will touch, plus directly cited dependencies

If the task is centered on claim status, theorem flow, frontier description, or shared formulas, also inspect the relevant metadata or sibling-volume constitutional files before editing prose.

If `raeeznotes/raeeznotes100/red_team_summary.md` is absent, say so explicitly and use the archived repo copy at `archive/raeeznotes/raeeznotes100/red_team_summary.md` or the newest relevant audit notes under `compute/audit/` instead. Do not pretend the file was read.

`chapters/connections/concordance.tex` is the constitution of the monograph. When files disagree, repair the chapter, theorem statement, or status tag so they match the concordance, or update the concordance deliberately if the project has genuinely moved.

## Cross-Volume Scope

This repo is Volume I of a three-volume programme:

- Vol I: `~/chiral-bar-cobar`
- Vol II: `~/chiral-bar-cobar-vol2`
- Vol III: `~/calabi-yau-quantum-groups`

When a task touches shared formulas, theorem statuses, definitions, notation, bridge claims, chapter references, or hardcoded expected values, the live surface includes all three volumes.

Cross-volume rule:

- grep before editing;
- grep after editing;
- update all genuine duplicates in the same session, or leave an explicit pending note naming the untouched collision surface.

## E1-First Prose Architecture

Every chapter constructs the E1 ordered bar story first, then derives the symmetric story by Sigma_n-averaging.

Pattern for every structural passage:
1. Construct the E1 object (B^ord, r(z), Theta_A in g^{E1}).
2. Show the E1 structure (deconcatenation, R-matrix, matrix curvature).
3. Apply av: g^{E1} -> g^mod (lossy coinvariant projection).
4. Derive the symmetric result (kappa, obs_g, shadow tower).

Never state a symmetric result without the E1 object it projects from. The five theorems extract Sigma_n-invariant content of B^ord. The convolution algebra has two levels: g^{E1} (primitive) and g^mod (shadow). Theta_A lives in g^{E1}; everything else is its projection.

## All Anti-Pattern Catalogues Are Binding

All anti-patterns in the three `CLAUDE.md` files are binding law:

- Vol I: `AP1` through `AP149`
- Vol II: `V2-AP1` through `V2-AP39`
- Vol III: `AP-CY1` through `AP-CY19`

`AGENTS.md` compresses them into an always-on steering surface. It does not supersede them. When a task touches one of the domains below, open the relevant `CLAUDE.md` slice before editing.

## Live Cross-Volume Hot Zones

These are the failure families that recur across the three volumes and the last-100-commit archaeology. Treat them as hot before any nontrivial edit.

### Hot Zone 1: Formula Drift

- `AP1`: never write `\kappa` from memory; read the census source first;
- `AP19`, `AP117`, `AP120`, `AP126`, `AP136`, `AP137`, `AP141`;
- `AP143`: DS ghost charge background shift omission (W_N for N>=3);
- `AP144`: convention coexistence without bridge (r-matrix trace-form vs KZ);
- `AP148`: r-matrix normalization is convention-dependent (C9 corrected);
- `V2-AP34`: divided-power `\lambda`-bracket normalization;
- `AP113`: bare `\kappa` forbidden in Vol III;
- `AP-CY17`, `AP-CY19`: CY dimension and genus-normalization drift.

### Hot Zone 2: Status / Environment / Label Drift

- `AP40`: environment must match epistemic status;
- `AP125`, `AP124`: label prefix and uniqueness across all three volumes;
- `AP4` and `V2-AP31`: no proof after conjecture;
- `AP-CY6`, `AP-CY11`, `AP-CY14`: conditionality and theorem-environment overreach in Vol III.

### Hot Zone 3: Object And Convention Conflation

- `AP25`, `AP34`, `AP50`: `A`, `B(A)`, `A^i`, `A^!`, `Z^{der}_{ch}` are distinct;
- `AP33`, `AP131`, `AP132`;
- `AP142`: local-global conflation on curves. "Koszul duality over a point is Koszul duality over P^1" is FALSE. (a) Retract is DATA; (b) formal disk D carries thickening data; (c) A^1 already has Arnold relations and FM compactifications absent over a point; (d) P^1 adds compactness. Always specify WHICH space and WHAT comparison data;
- `V2-AP1` through `V2-AP24`: `E_1` versus `E_\infty`, ordered versus symmetric bar, open/closed directionality, PVA versus `P_\infty`;
- `AP-CY3`, `AP-CY4`, `AP-CY7`, `AP-CY10`, `AP-CY12`: `E_2`, Drinfeld center, derived center, CoHA, flop/Koszul, shadow-depth misclassification.

### Hot Zone 3b: Structural Reorganization Debt

- `AP145`: restructuring propagation debt — Part renumbering, chapter migration, label renaming create O(N) cross-reference fixes;
- `AP146`: mega-campaign straggler commits — after 100+ agent campaigns, expect follow-up commits for late-arriving results;
- `AP147`: circular proof routing — when theorems cross-reference each other, insert routing remarks citing the primitive non-circular anchor;
- `V2-AP26` through `V2-AP30`: stale Part references after restructuring.

### Hot Zone 4: Propagation And Oracle Drift

- `AP10`, `AP128`: tests and engines can share the same wrong model;
- `V2-AP26` through `V2-AP30`: stale Part references and cross-volume propagation failures;
- `V2-AP32` through `V2-AP35`: standalone artifact leaks, permanent rectification flags, connective drift after corrections;
- `AP-CY13`, `AP-CY15`, `AP-CY16`, `AP-CY18`: stale references, README scope inflation, rank mismatches, and coefficient-table drift.

### Hot Zone 5: Prose Slop And Structural Noise

- `AP29`, `V2-AP29`: banned filler vocabulary and em dashes;
- `AP121`: no Markdown in LaTeX;
- artifact cleanup is mandatory after generation;
- connective words like "therefore" and "hence" must be re-audited after formula correction.

## Empirical Risk Map From Last-100-Commit Archaeology

This dated section exists because the recent error distribution changes how the model should behave. Refresh it when it becomes stale.

### Volume I: dominant repeat failures

- repeated rectification waves, not isolated typo cleanup;
- persistent `AP126/AP141` level-prefix failures;
- label/status/concordance drift: `AP125`, `AP124`, `AP40`;
- formula drift around `\kappa`, harmonic numbers, desuspension, and central-charge conventions;
- compute/test synchronization failures and stale hardcoded oracles;
- DS ghost charge cascade: W6/W7 ghost central charges wrong by orders of magnitude (AP143);
- r-matrix normalization convention mixing: trace-form vs KZ (AP144/AP148; C9/C13 corrected);
- local-global conflation on curves (AP142; 17 fixes across 14 files);
- standalone drift and build-artifact noise repeatedly obscuring the live source;
- prose fortification and slop cleanup recurring often enough to require explicit post-write grep;
- mega-campaign straggler commits after 100+ agent campaigns (AP146).

### Volume II: dominant repeat failures

- `AP40` environment/status drift (~50 instances in 7 commits; frontier chapters default to theorem when should default to conjecture);
- `V2-AP34` divided-power convention drift (15+ corrupted lambda-brackets; grep `c/2.*lambda.*3` to catch);
- `AP32` uniform-weight tag drift (20+ scope tightenings);
- `AP126` propagation into the 3D / ordered-bar bridge (34+ bare Omega/z instances in 5 commits);
- `V2-AP37` Arakelov form normalisation (same sign error fixed THREE times across THREE commits);
- stale hardcoded Part references after restructuring (`V2-AP26`: 24+ fixes after 10→8);
- proof-after-conjecture and connective drift after local fixes (`V2-AP31`/`V2-AP35`: 27 instances);
- cross-volume propagation failures where Vol II continued to advertise stale Vol I claims;
- phantom label debt from chapter migration (`V2-AP38`: 366 phantoms across 2 commits);
- undefined macros after migration (`V2-AP39`: 7 macros across 2 commits);
- terminology rename cascades (`V2-AP36`: shadow tower rename took 5 commits).

### Volume III: dominant repeat failures

- `AP113` bare-`\kappa` recurrence;
- overclaiming d=3 CY existence or theorem status;
- conditionality not propagating far enough downstream;
- bar-Euler / Borcherds / CY3 frontier statements outrunning what the manuscript actually proves;
- stub and thin-chapter fragility;
- compute/test and build-artifact churn masking the real status boundary.

## Current Dirty Collision Surface Snapshot (April 10, 2026)

This snapshot is a prior, not permission to skip `git status --short`.

### Volume I

Current dirty surface is broad and collision-heavy:

- `AGENTS.md`, `CLAUDE.md`, `chapters/connections/concordance.tex`, and `metadata/theorem_registry.md` are dirty;
- large swaths of frame, theory, examples, appendices, and connections are dirty;
- many compute libraries and tests are dirty;
- build outputs, PDFs, logs, and new audit notes are present.

Treat any Vol I change as potentially interacting with an active rectification wave.

### Volume II

Current dirty surface is smaller but load-bearing:

- `AGENTS.md`, `CLAUDE.md`, and `compute/audit/linear_read_notes.md` are dirty;
- multiple frontier and connections chapters are dirty, especially `chapters/connections/thqg_perturbative_finiteness.tex`;
- preface, introduction, and the compiled PDF are dirty.

Any claim about genus-2 stable graphs, perturbative finiteness, frontier status, or cross-volume bridge wording must be rechecked live.

### Volume III

Current dirty surface is bridge-heavy:

- `AGENTS.md` is dirty;
- `chapters/theory/cy_to_chiral.tex`, `chapters/theory/introduction.tex`, `chapters/theory/e1_chiral_algebras.tex`, `chapters/connections/cy_holographic_datum_master.tex`, and several examples are dirty;
- seven compute libraries and their tests are dirty;
- notes, logs, and compiled PDFs are dirty.

Any Vol III bridge statement about `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{BKM}}`, CY3 existence, or CY `r`-matrices must be treated as live and collision-prone.

Rule: rerun `git status --short` in every touched repo before trusting this summary.

## Codex / GPT-5.4 Task Intake

Before any nontrivial work, lock these eight items:

1. the exact target file, theorem, formula, bridge, engine, or live surface;
2. the task type: audit, rectification, formula verification, status sync, compute/test repair, build triage, or frontier synthesis;
3. the active convention bridge: grading, shifts, OPE versus `\lambda`-brackets, genus and arity scope, ordered versus symmetric bar, Vol I versus Vol II versus Vol III normalization;
4. the live evidence surface: source, nearby context, diff, logs, tests, and citations if any;
5. the narrowest falsifier that could kill the current claim;
6. the propagation surface across the three volumes;
7. the dirty collision surface in every repo involved;
8. the matching skill, if a repo skill applies.

If the user prompt is underspecified, infer the smallest defensible scope only after reading the live surface. Ask only when theorem status, convention choice, or irreversible architecture would change.

## Skills And Mode Routing

Use progressive disclosure. Do not reconstruct a deep workflow from scratch when a repo skill already exists.

Trigger map:

- `beilinson-rectify`: use for rectifying, fortifying, rewriting, or structurally repairing a mathematical chapter, proof, or claim surface;
- `chriss-ginzburg-rectify`: use for chapter-scale structural fortification, especially introductions, prefaces, chapter openings, and arguments that need full rewrite-level convergence;
- `claim-surface-sync`: use when theorem labels, status tags, concordance text, registry entries, or duplicated theorem surfaces may drift out of sync;
- `deep-beilinson-audit`: use for adversarial audits, red-teaming, pressure-testing, and frontier verification;
- `multi-path-verify`: use for one formula, invariant, theorem status, or computational claim where independent verification paths matter;
- `cross-volume-propagation`: use after any formula, status, terminology, or theorem-surface correction that may recur across Volumes I, II, and III;
- `build-surface`: use when builds, test output, or warning classification decide whether a change is actually verified;
- `compute-engine-scaffold`: use when the task is to add or repair a compute engine together with independent multi-path tests;
- `frontier-research`: use for frontier synthesis or research architecture, local by default and delegation-enabled only with explicit user authorization.

Default reasoning effort is `medium`.

Escalate to `high` or `xhigh` only for proof surgery, chapter-scale structural repair, or stalled frontier synthesis after the task definition and falsifier are already sharp.

## Codex Local Infrastructure

Repo-local Codex playbooks live in `.agents/skills/`:

- `beilinson-rectify`
- `chriss-ginzburg-rectify`
- `deep-beilinson-audit`
- `multi-path-verify`
- `claim-surface-sync`
- `cross-volume-propagation`
- `build-surface`
- `compute-engine-scaffold`
- `frontier-research`

Repo-local Codex hooks live in `.codex/hooks.json`:

- `SessionStart`: injects the Vol I live-surface reminder and skill map;
- `UserPromptSubmit`: routes prompts toward the matching Codex playbooks;
- `PreToolUse`: blocks destructive shell habits and warns on commit/source-edit paths;
- `PostToolUse`: refuses to let failing build/test output count as verification;
- `Stop`: forces rectification-style work to close as `CONVERGED` or `BLOCKED`.

Hook rule:

- hooks are deterministic guardrails, not substitutes for judgment;
- if a workflow repeats and does not belong in always-on context, move it to a skill instead of bloating `AGENTS.md`.

## Claude-To-Codex Parity Map

Any operational workflow defined in `CLAUDE.md` is also binding for Codex. The Codex-native equivalents are:

- `/build` -> `build-surface` plus the build commands in this file;
- `/audit [target]` -> `deep-beilinson-audit`;
- `/chriss-ginzburg-rectify [file]` -> `chriss-ginzburg-rectify`;
- `/rectify [file]` and `/beilinson-rectify [file]` -> `beilinson-rectify`;
- `/verify [claim]` -> `multi-path-verify`;
- `/propagate [pattern]` -> `cross-volume-propagation`;
- `/compute-engine [name]` -> `compute-engine-scaffold`;
- `/rectify-all` and `/beilinson-swarm` -> user-authorized multi-agent expansion of `beilinson-rectify`;
- `/research-swarm [topic]` -> `frontier-research`, with delegation or swarm behavior only if the user explicitly asks.

Rule:

- Claude slash-command workflows are not Claude-only privileges.
- If `CLAUDE.md` defines a reusable loop, routine, or meta workflow, Codex must either:
  use the matching skill,
  follow the corresponding routine in this file,
  or state the blocker explicitly.

## Pre-Edit Verification Protocol

The Pre-Edit Verification Protocol from `CLAUDE.md` is part of the Codex contract too.

Before editing a surface that touches one of the following families, load the matching PE template from `CLAUDE.md` or `compute/audit/pre_edit_verification_protocol_wave12.md` and fill it mentally or explicitly before editing:

- `PE-1`: `r`-matrix write
- `PE-2`: `kappa` formula write
- `PE-3`: complementarity write
- `PE-4`: bar complex formula
- `PE-5`: Vol III `kappa` write
- `PE-6`: exceptional dimensions
- `PE-7`: label creation
- `PE-8`: cross-volume formula
- `PE-9`: summation boundary
- `PE-10`: scope quantifier
- `PE-11`: differential form type
- `PE-12`: prose hygiene

Mandatory trigger cases:

- `r`-matrices or OPE-to-`r` conversions;
- any `\kappa` formula or conductor statement;
- bar/cobar formulas, desuspension, augmentation ideals, or differential identities;
- label creation, environment changes, or status changes;
- cross-volume formulas or mirrored theorem advertisements;
- scope-quantifier or uniform-weight statements;
- differential-form statements like `dz` versus `d log z`.

If the edit is in one of those hot families, do not patch by pattern alone.

## Convergent Writing Loop

The convergent writing loop from `CLAUDE.md` is also binding for Codex on prose-heavy mathematical work:

`WRITE -> REIMAGINE -> REWRITE -> BEILINSON AUDIT -> REIMAGINE AGAIN -> REWRITE AGAIN -> CONVERGE`

Use it for:

- prefaces and introductions: at least 3 iterations;
- chapter openings and theorem lead-ins: at least 2 iterations;
- any exposition whose job is structural mathematical orientation, not just local copy.

Reimagination channels:

- Gelfand: inevitability
- Beilinson: falsification
- Drinfeld: unifying principle
- Kazhdan: compression
- Etingof: clarity
- Polyakov: physics equals theorem
- Kapranov / Costello / Gaiotto / Witten: higher-structure and factorization pressure where relevant

Chriss-Ginzburg structural moves remain available to Codex:

- deficiency opening;
- unique survivor;
- instant computation;
- forced transition;
- decomposition table;
- dichotomy;
- sentence-as-theorem.

## Session Protocol

For substantial sessions, Codex should follow the same routine shape that `CLAUDE.md` requires:

1. Read `CLAUDE.md`, `AGENTS.md`, and the live target surface.
2. Run the narrowest relevant build/test prelude for the task:
   `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2`
3. Inspect `git log --oneline -10` and `git status --short` in every touched repo.
4. Read `.tex` or source files before editing. Never edit from memory.
5. After each correction, grep all three volumes if the claim may propagate.
6. After each substantive change, run the narrowest build/test/metadata check that can falsify it.
7. Apply the convergent writing loop to prose-heavy mathematical exposition.
8. End with a proved/computational/conditional split and explicit convergence or blocker language.

## The Resonance Loop

For any nontrivial task, run this loop until `CONVERGED` or `BLOCKED`.

### 0. Scope Lock

State the exact claim surface being audited.

### 1. Invariant Lock

Before trusting any local argument, lock:

- grading and shifts;
- object identity among `A`, `B(A)`, `A^i`, `A^!`, `Z^{der}_{ch}`;
- genus, arity, family, filtration, and completion scope;
- theorem status and environment;
- Vol I / II / III convention bridges.

### 2. RED Pass

Try to kill the claim:

- dependency attack;
- hypothesis attack;
- edge-case or counterexample attack;
- sign, grading, duality, or notation attack;
- reduced-vs-completed or finite-stage-vs-limit attack;
- object-conflation attack;
- status-inflation attack.

### 3. BLUE Pass

Attack consistency:

- theorem / proof / status mismatch;
- label prefix or uniqueness drift;
- stale Part or chapter references;
- compute/manuscript disagreement;
- README or notes outclaiming the `.tex`;
- cross-volume inconsistencies.

### 4. GREEN Pass

Attack structural gaps:

- missing definitions;
- hidden imported lemmas;
- unsupported converses;
- dangling references;
- places where the true statement is weaker than the advertised one.

### 5. Patch In Dependency Order

Fix `CRITICAL` and `SERIOUS` findings first, then `MODERATE`.

For each fix:

1. reread the local context;
2. re-derive or recompute independently;
3. make the smallest truthful edit;
4. immediately search for downstream advertisements of the old claim.

### 6. Propagate

After any mathematical change:

- grep Volume I;
- grep Volume II;
- grep Volume III;
- update genuine duplicates or leave an explicit pending note.

### 7. Verify

Run the narrowest check that can actually falsify the change:

- targeted `pytest` in `compute/tests`;
- metadata regeneration or checks when labels or statuses change;
- targeted grep for forbidden formulas, stale labels, or banned prose;
- targeted TeX build or minimal compile check for the touched manuscript surface.

### 8. Hostile Re-Read

Reread your own rewrite as an adversary. Try to break it.

### 9. Stop Condition

- `CONVERGED`: no known actionable `MODERATE+` issue remains on the modified surface, and the narrowest relevant verification passes.
- `BLOCKED`: exact blocker named precisely, with the strongest truthful narrower statement identified.

Do not stop between those states.

## Status Discipline

- Never let a `\ClaimStatusProvedHere` block rely on `Conjectured`, `Conditional`, `Heuristic`, or `Open` material without explicit fencing.
- If verification fails, demote, narrow, or mark conditional. Do not leave overstated text in place.
- Theorem/proposition/lemma/corollary environments are for proof-bearing claims only.
- Conjectural or heuristic material belongs in matching environments, not theorem-like ones.
- When downgrading or renaming a claim, update the environment, label prefix, claim-status tag, local proof or evidence remark, and downstream references in the same session.
- README files, notes, and summaries may not outclaim the live manuscript.

## Cross-Volume Propagation Discipline

- Never assume a fix is local if the claim is formula-level, status-level, or bridge-level.
- Before changing a shared formula or theorem advertisement, grep all three volumes.
- After changing a shared formula or theorem advertisement, grep all three volumes again for stale copies.
- Never hardcode Part numbers in prose. Use `\ref{part:...}`.
- When correcting an engine formula, derive new expected values independently before changing tests.
- Build artifacts and release PDFs are downstream surfaces, not authoritative sources.

## Canonical Formulas

Verify against these and the live census source before writing:

```text
kappa(H_k) = k                                     # Heisenberg
kappa(Vir_c) = c/2                                # Virasoro ONLY
kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)             # Affine KM
kappa(W_N) = c*(H_N - 1), H_N = sum_{j=1}^N 1/j  # Principal W_N

r^KM(z) = k*Omega/z           # Level prefix k MANDATORY
r^Heis(z) = k/z               # Level prefix k MANDATORY
r^Vir(z) = (c/2)/z^3 + 2T/z   # Cubic + simple, NOT quartic

c_bc(lambda) = 1 - 3(2*lambda-1)^2
c_bg(lambda) = 2(6*lambda^2-6*lambda+1)
c_bc + c_bg = 0

K(KM) = 0, K(Vir) = 13, K(W_3) = 250/3, K(BP) = 196
sl_2 bar H^2 = 5
Genus-2 stable graphs = 7       # Total connected stable strata at g=2, n=0
E_8 adjoint = 248

B(A) = T^c(s^{-1} A-bar), A-bar = ker(epsilon)
|s^{-1}v| = |v| - 1
d_bar^2 = 0 ALWAYS; d_fib^2 = kappa*omega_g  # Fiberwise only
MC: d*Theta + (1/2)[Theta,Theta] = 0
QME: hbar*Delta*S + (1/2){S,S} = 0
F_1 = kappa/24, F_2 = 7*kappa/5760
eta(tau) = q^{1/24} * prod(1-q^n)
Cauchy: 1/(2*pi*i), NOT 1/(2*pi)
Delta = 8*kappa*S_4
```

## Forbidden Formulas

Grep these after every relevant check:

```text
B1.  r(z) = Omega/z               -> MUST be k*Omega/z
B2.  r^Vir(z) = (c/2)/z^4         -> cubic z^3, NOT quartic
B5.  c_bc = 2(6L^2-6L+1)          -> that's c_bg
B7.  kappa(W_N) = c*H_{N-1}       -> MUST be c*(H_N - 1)
B9.  kappa+kappa' = 0 unscoped    -> family-specific only
B14. T^c(s^{-1} A)                -> MUST be T^c(s^{-1} A-bar)
B16. |s^{-1}v| = |v|+1            -> MUST be |v|-1
B17. eta = prod(1-q^n)            -> missing q^{1/24}
B21. E_8 = 779247                 -> false
B22. dim H^2(B(sl_2)) = 6         -> MUST be 5
B25. K_BP = 2                     -> MUST be 196
B37. F_2 = 1/5760 or 7/2880       -> MUST be 7/5760
B38. 1/(2*pi) integral            -> MUST be 1/(2*pi*i)
B43. d_alg(Vir) = 3               -> d_gen=3, d_alg=infinity
```

## Five Objects: Never Conflate

- `A`: algebra
- `B(A)`: bar coalgebra
- `A^i = H^*(B(A))`: dual coalgebra
- `A^! = (A^i)^vee`: dual algebra
- `Z^{der}_{ch}`: bulk / derived chiral center

## Four Classes

- `G`: `r = 2`, Heisenberg
- `L`: `r = 3`, affine KM
- `C`: `r = 4`, betagamma
- `M`: `r = infinity`, Virasoro / `W_N`

## Prose And Formatting Discipline

- Banned filler vocabulary from `AP29` and `V2-AP29` remains banned.
- Em dashes are forbidden.
- No Markdown syntax inside LaTeX.
- After correcting a formula or theorem sentence, reread all nearby "therefore", "hence", and "it follows" connectors for stale logic.
- Post-write grep is mandatory on touched `.tex` files when the edit is nontrivial.

## End-Of-Task Output Contract

For every substantial mathematical task, end with a compact report that states:

1. the exact claim surface audited;
2. what was proved internally versus only supported computationally;
3. what remains conditional, conjectural, heuristic, or open;
4. what verification was run;
5. what propagation was completed or explicitly left pending.

If blocked, name the exact blocker and the strongest truthful narrower statement.

## Style Of Action

- Be decisive, but skeptical.
- Read before editing.
- Verify before advertising.
- Prefer the live source over inherited narrative.
- Prefer the narrowest falsifier over broad "confidence."
- Prefer one true local theorem over one false grand synthesis.
