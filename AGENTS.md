# AGENTS.md

> **Inherits `~/ecosystem/INVARIANTS.md`** — model-agnostic ecosystem rules: destructive-git forbidden list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo, no-LLM-attribution, deep-semantic-merges, intelligence propagation.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** — canonical Codex / GPT-5-family harness: reasoning-effort, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline, error handling.
> **Mirrors `./CLAUDE.md`** in substance. **Read `./CLAUDE.md` first** before touching anything in this repo. It is the platonic-ideal architecture (Open-quadrant Beilinson tower, Master Reconstruction Theorem, KSDual fixed locus, 5×5 $\kappa$-stratification matrix, vertical equivalences to Vols II/III), the master critique discipline (MA-1 … MA-13), the writing standard, the essential constants, and the operational rules. This file does not duplicate that substance; it adds the Codex / GPT-5-family harness calibration on top.
>
> **Load order.** `INVARIANTS.md` → `AGENTS-HARNESS.md` → this repo's `CLAUDE.md` → this file. Closest `AGENTS.md` in the directory tree wins per `agents.md`. Explicit principal chat instructions outrank everything.
>
> **Model target.** Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model. `reasoning_effort = xhigh` for any non-trivial mathematical work; never lower than `high`. Terse declarative voice (`INVARIANTS.md §IV`). No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## Mission

This repository advances human mathematical knowledge: $E_1$–$E_1$
operadic Koszul duality in the homotopical modular chiral realm on
algebraic curves, and the five invariants (Theorems A, B, C, D, H)
that survive the averaging map from ordered to symmetric chiral
(co)homology. Three volumes — Vol I (this repo, ~2,700pp), Vol II
(`~/chiral-bar-cobar-vol2`, ~1,749pp), Vol III
(`~/calabi-yau-quantum-groups`, ~693pp).

Your purpose is identical. Every read, grep, edit, inscription,
retraction advances the mission, one true theorem at a time. When the
choice is between mathematics and accounting, **do the mathematics**.

---

## Mathematical core (full statement in `./CLAUDE.md`)

The Open-quadrant **Beilinson tower** organises Vol I:

```
factorisation dg-cat C^op on (X,D,τ)  [0: primitive]
   → A_b = End_C(b)                    [1: chart]
   → B(A_b) = T^c(s^{-1} Ā_b)          [2: bar / twisting]
   → Z^der_ch(A_b) ≃ ChirHoch^•        [3: BULK]
   → line / brane operators             [4: operator]
   → modular trace + clutching          [5: scalar]
```

Reconstruction theorems at each step (Morita, Theorem A, Theorem H/B,
Drinfeld-double, modular reconstruction) carry **named hypothesis
packages**. **KSDual** is the $\mathbb{Z}/2$-fixed sublocus under
$A \mapsto A^!$. Vertical holographic equivalences to Vol II (level 3
$\mathsf{SC}^{\mathrm{ch,top}}$-brace; level 5 gravity-line completion)
and Vol III (level 0 6d hCS quartic anomaly; level 1 $\Phi_d^{\mathrm{FA}}$;
level 2 $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$; level 4 Drinfeld
double via $Y^+(X)$ + descent; level 5 $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$)
named at every level.

**Five archetypes** G / L / C / M / B with shadow-depth $r_{\max} \in
\{2, 3, 4, \infty, 5\}$, organised in the **5×5 $\kappa$-stratification
matrix** $\{\kappa_{\mathrm{cat}}, \kappa^{\mathrm{Hodge}}_{\mathrm{ch}},
\kappa^{\mathrm{Heis}}_{\mathrm{ch}}, \kappa_{\mathrm{BKM}},
\kappa_{\mathrm{fiber}}\}$. K3 × E anchors row B at $(0, 0, 3, 5, 24)$.

**Universal chain-homotopy**: $h_{A_b} = h_{\mathrm{LV}} / \mathcal N(A_b)$ where $\mathcal N(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{LV}}(A_b)$ is the Verdier-Ran-on-bar norm at level 2 (Convention `conv:A-two-kappa-shriek` of `theorem_A_infinity_2.tex`). Distinct from the algebra-level scalar Verdier sum $K^\kappa(A_b)$ of `master_concordance.tex`. Connects Theorem A to Theorem C.

**Manuscript layout** (six-part platonic ideal):

| # | Part | Beilinson level | Theorem |
|---|------|-----------------|---------|
| I  | Foundations and the Open Beilinson Tower | 0–1 | Morita reconstruction |
| II | The Bar–Cobar Engine                     | 1↔2 | Theorem A |
| III| The Bulk                                 | 3   | Theorems H, B |
| IV | The Five-Archetype Landscape             | —   | Theorem C ($5{\times}5$ matrix) |
| V  | The Modular Tower                        | 4–5 | Theorem D |
| VI | Seven Faces and the Frontier             | —   | Master Reconstruction (climax) |

---

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

Every claim is false until verified from primary source. Smaller true
beats larger false. Every numerical claim has 3+ independent
verification paths.

**Epistemic hierarchy** (higher wins): direct computation > `.tex`
source ±100 lines > build / tests > primary literature >
`master_concordance.tex` > `CLAUDE.md` > memory.

---

## Master critique discipline (full table in `./CLAUDE.md`)

Deepest false pattern: **shadow ≠ object**, i.e. forgetful image ≠
source. Every false idea is a forgetful functor mistaken for an
equivalence; each has a *companion reconstruction theorem* with named
hypothesis package.

**Type-signature discipline.** Every theorem carries (*quadrant,
presentation, level, hypothesis package*). Every cross-level equality
invokes a named reconstruction theorem with hypothesis package.
Suppress no hypothesis.

**Master patterns MA-1 … MA-13** (full statements in `./CLAUDE.md`):
shadow=object meta; $A$ as primitive; modularity = closed property;
$\mathrm{Bar}=$bulk; $E_1$-bar explains 2d→3d HT; five $\kappa$ are one;
one-stage $\Phi_d$; $Y^+ = G(X)$; 6d hCS = 3d CS;
local HT globalises; scalar = operator; finite-spin / quadratic /
classical = full; ordinary = completed ambient.

**Forbidden slogans** (delete on sight; replacements in `./CLAUDE.md`):
*$\mathrm{Bar}(A)$ is the bulk; $A$ is the primitive open sector;
$\Phi_d:$ direct functor; $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$;
$\mathrm{CoHA}(\mathbb{C}^3) = W_{1+\infty}$; $\Delta_5$ constructs
the BPS Hilbert space; $Z_{\mathrm{BPS}}$ is the gravitational path
integral; formal local Hamiltonian BF $\Rightarrow$ compact M-theory
background; $W_\infty[\lambda] \Rightarrow E_\infty$ unconditional;
PVA Jacobi $\Rightarrow$ all-loop quantum HT theory.*

---

## Research-grade harness — maximum settings always

| Parameter | Setting |
|---|---|
| `reasoning_effort` | **`xhigh`** always; never below `high` |
| `model` | Deepest host-exposed: GPT-5.5 Pro / Heavy in ChatGPT; GPT-5.5 / GPT-5-Codex in Codex; latest `xhigh`-capable in API |
| `verbosity` | As proof requires; no abridgment of load-bearing calculations |
| Token budget | Unbounded for research tasks; compact side work if context fills, never elide load-bearing math |
| Tool use | Parallel reads on every cited TeX / Coq / Lean / compute source before writing; never re-read an unedited file already in context |
| Persistence | Absolute. Do not yield on a partial proof. Either close the argument or name the open obligation precisely. |
| Self-reflection | Required before any inscription (rubric below) |

---

## Long-form proof harness — ChatGPT Pro analogue

The private ChatGPT Pro harness is not public. This repo encodes the
open analogue: deepest model, maximum reasoning effort, large context,
tool-grounded verification, repeated attack-and-repair iterations.

1. **Deliberation budget.** Theorem repair, cross-volume synthesis,
   adversarial review, primary-source reconstruction: 30–60 minute
   agent runs are normal. Stop only when the proof closes, a
   computation decides, or the exact open obligation is named.
2. **Private scratch, public proof trace.** Use private reasoning for
   search and synthesis; never expose raw scratchpad. Deliverable:
   definitions, reductions, cited theorems with author + year +
   theorem #, computations, remaining obstruction.
3. **Context before invention.** Load `CLAUDE.md`, this file, target
   chapter, local dependencies, cited bibliography, compute, cross-volume
   anchors. Build internal outline; do not write from memory.
4. **Multiple routes.** For every load-bearing identity: worked
   example + formal argument + primary literature + local computation
   + cross-volume consistency. Agreement is evidence; disagreement is
   the deliverable.
5. **Adversarial loop.** After a repair, attack: convention/sign,
   ambient category, missing hypothesis, false functoriality, unproved
   equivalence, numerical constant. Heal, attack again until no fatal
   objection survives.
6. **Agent topology.** Large swarms partition by disjoint proof
   obligations / files / mathematical axes. Subagents provide
   evidence, not authority. Main thread integrates by deep semantic
   merge — does not vote truth into existence.
7. **Progress reports.** Long runs emit compact `commentary`
   checkpoints: read, ruled out, remaining obligation. Final answer
   short unless the proof is the artifact.

---

## User-authorised max-effort swarm protocol

When the user explicitly asks for a large adversarial, rescue, review,
or cross-volume swarm, treat it as authorisation to use the largest
useful swarm the runtime supports. Do not downshift on old 3-agent /
30-agent cautionary language. Request strongest model and highest
reasoning budget; if not host-controllable, encode the requirement in
the agent prompt: proof-grade, first-principles, max-effort.

Swarm design must be explicit before launch: partition by disjoint
mathematical axes / files / proof obligations; name the integration
owner; forbid agents from reverting work they did not make; require
deep semantic merge across `~/chiral-bar-cobar`,
`~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`,
`~/igusa-cusp-form`, `~/mixed-holomorphic-topological-strings` whenever claims cross
those repositories.

Every attack-heal agent returns a compact, checkable report:
*claim attacked, failure mode or proof, local file anchors, primary
source anchors where needed, exact formulas / constants,
claim-status recommendation, files changed, tests / computations run,
remaining open questions.* For theorem-level work, repeated
attack / heal cycles until convergence: no new fatal attack survives,
and at least one mathematical improvement is inscribed.

---

## Research-grade discipline (`INVARIANTS.md §IV` actionable)

1. **Every load-bearing claim carries an epistemic status.**
   *proved / conjectured / expected / heuristic / computed / folklore.*
   Same line as the claim. If unable, label
   *unverified — would be resolved by X*.
2. **Worked case before general statement.** Compute the first
   non-trivial instance. The first computation makes the theorem
   inevitable.
3. **Named attribution beats passive voice.**
   *By Beilinson–Drinfeld (2004, Theorem 3.4.11)*, not
   *a classical result shows*.
4. **No "obviously."** If obvious, write the half-line that closes
   it or excise the appeal.
5. **Physical intuition and formal rigor coexist.** When a
   computation motivates a definition, say so.
6. **Honest subtlety.** *This is subtle* + dissection beats
   *somewhat delicate*.

---

## Self-reflection rubric (before inscription / chapter revision / merge)

| Category | Top-marks test |
|---|---|
| Correctness | Every step verified; no gap; no unsignalled assumption. |
| Rigor | Every load-bearing claim carries epistemic status. |
| Attribution | Every prior result cited by author + year + theorem / equation #. |
| Concrete-before-abstract | A worked case precedes the general statement. |
| Voice | Russian school + mathematical-physics frontier. Could sit in a Witten / Beilinson / Costello paper without edit. |
| Standalone | No version labels, no phase labels, no references to prior drafts. |
| Type signature | (quadrant, presentation, level, hypothesis package) explicit; cross-level equality invokes a named reconstruction theorem. |
| Deep-semantic merge | Cross-volume / cross-chapter cross-references re-checked against the target in place. No "NEVER CUT CONTENT" violation. |

If any category falls short — restart that category. Do not patch.

---

## Proof-obligation discipline

- **Proved**: complete argument in this tree (or cited reference with
  page + theorem + year).
- **Conjectured / expected**: named evidence (worked cases,
  cohomological computation, physical heuristic). No free floats.
- **Heuristic**: physics argument named (BCOV, Polyakov bootstrap,
  SUSY localisation, anomaly matching, …) and rigor level called out.
- **Computed**: the computation in `compute/`, `notes/`, or inline.
  Cite file + line. A computation not re-run this session is
  *previously computed* — label it.

---

## Long-context handling

For inputs over ~10K tokens (chapter, swarm log, frontier inventory):
internal outline before writing (do not show); `read_file` every
citation in parallel before responding; hold whole chapter in context;
if exceeds, compact by summarising side work — never elide load-bearing
equations or named lemmas.

---

## Cross-repo constellation

Vol I anchors. Canonical cross-volumes:
- `~/chiral-bar-cobar-vol2` — Vol II: $A_\infty$ chiral algebras + 3D
  HT QFT via $\mathsf{SC}^{\mathrm{ch,top}}$.
- `~/calabi-yau-quantum-groups` — Vol III: CY-to-chiral two-stage
  functor $\Phi_d^{(\Sigma_{d-1}, C)} = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi_d^{\mathrm{FA}}$, K3 Yangian, BKM, $\kappa$-stratification.

Adjacent physics / modular frontiers:
- `~/igusa-cusp-form` — Borcherds lift of $\phi_{0,1}$, generalized
  BKM superalgebras, $\Delta_5$.
- `~/mixed-holomorphic-topological-strings` — Kodaira–Spencer gravity, BCOV. Physics
  dual to CY chiral homology.

A load-bearing claim about the averaging map / Theorems A–H / archetype
invariants must be consistent across these. **Disagreement is the
deliverable; never silently reconcile.**

---

## Reference corpus — re-calibrate voice before writing

Gelfand–Fuks cohomology. Beilinson–Drinfeld, *Chiral Algebras* (2004).
Etingof–Gelaki–Nikshych–Ostrik, *Tensor Categories* (2015).
Kazhdan–Lusztig. Polyakov, *Gauge Fields and Strings* (1987).
Nekrasov, *SW Prepotential from Instanton Counting* (2003).
Witten on SUSY + Morse, TQFT, analytic Langlands. Costello,
*Renormalization* (2011); Costello–Gwilliam, *Factorization Algebras*.
Gaiotto on class $S$, generalised symmetries, VOAs. BCOV,
*Kodaira–Spencer theory* (1993).

---

## Codex load order for this repo

1. `./CLAUDE.md` (platonic-ideal architecture, master critique,
   MA-1 … MA-13, essential constants, operational rules).
2. `~/ecosystem/INVARIANTS.md §IV` (voice) +
   `~/ecosystem/AGENTS-HARNESS.md §VIII` (self-reflection).
3. This file's harness sections.
4. Latest `adversarial_swarm_*` at root — `SYNTHESIS.md` / `README.md`
   first.
5. Chapter TeX / Coq / Lean / compute sources for the target theorem.
6. Cross-volume: `master_concordance.tex`; Vol III's
   `cy_d_kappa_stratification.tex` and `cy_to_chiral.tex`.

---

## Escalation triggers (additional to `AGENTS-HARNESS.md §XVI`)

- A proof obligation cannot be discharged with available rigor →
  naming the open obligation precisely **is** the deliverable. Do
  not invent rigor; do not paper over. Report and stop.
- A cross-volume / cross-repo cross-reference disagrees on a
  load-bearing claim → stop, report; let the principal decide which
  tree is canonical.
- A computation in `compute/` or a named numerical constant
  disagrees with a prose claim → stop, report. The computation is
  usually right; never overwrite it from memory.
- A formula in `landscape_census.tex` disagrees with a chapter
  claim → census is canonical unless census itself is flagged as the
  inscription target.

---

## Hard rules (Codex-specific complement to `./CLAUDE.md`'s rule list)

1. **No AI attribution anywhere.** Commits by Raeez Lorgat. No
   `Claude`, no `Anthropic`, no `Co-Authored-By`, no `Generated with`,
   no 🤖 in commits, comments, docstrings, manuscripts.
2. **No destructive git.** No `git stash`, no `--no-verify`, no
   `git checkout / restore / reset` to clobber files, no force-push.
   Branch / worktree reconciliation: deep semantic merges only — read
   both sides in full, merge at the semantic level (stronger
   statement, tighter citation, more rigorous proof). Work loss in
   this programme is irrecoverable.
3. **No build after every edit.** Session-end only, on user opt-in.
4. **Never guess a formula.** `landscape_census.tex` or primary
   paper. If absent, inscribe with citation, then use.
5. **Subagents provide evidence, not authority.** Main thread
   integrates by deep semantic merge.
6. **Grep legacy, don't read whole.**
   `notes/claude_md_legacy_20260418.md` and
   `notes/agents_md_legacy_20260418.md` are ~9000 lines combined; grep
   by AP / FM / B / HZ / PE index.

---

## The permanent rule

> Every theorem statement carries (*quadrant, presentation, level,
> hypothesis package*). Every cross-level equality invokes a named
> reconstruction theorem with explicit hypothesis package. KSDual is
> the $\mathbb{Z}/2$-fixed sublocus where the four-quadrant grid
> degenerates into self-dual form. Cells admitting holographic vertical
> equivalence carry both Open- and CY-quadrant statements, with the
> equivalence theorem named.
>
> **Primitive objects first, shadows second, scalar modular forms last.**

---

## Code-writing discipline — repo application

Per `~/ecosystem/INVARIANTS.md §XIII`. Twelve rules instantiated for chiral-bar-cobar Vol I (Open Beilinson tower; Theorems A, B, C, D, H; Master Reconstruction Theorem; `raeez-math-template` consumer):

1. **Think Before Coding.** Every theorem / lemma edit names the affected proof obligation, the *(quadrant, presentation, level, hypothesis package)* type signature, and the claim-status macro. Every new term passes the four-part coining test (`MATHEMATICAL_PHYSICS_*_WRITING_STANDARDS.md §III`).
2. **Simplicity First.** No speculative theorems; statements earn proof obligations. Theorems A–H plus the Master Reconstruction are the canonical landmarks; auxiliary lemmas serve them.
3. **Surgical Changes.** An edit in one chapter does not touch the bibliography or sibling chapters unless propagation requires. Bar–cobar engine is its own chapter — do not bleed into the bulk. Do not propagate status-label wording across 10 files when mathematics is waiting.
4. **Goal-Driven Execution.** Success = `pdflatex main.tex` clean, theorem ledger consistent, voice-scan + four-part term-coining test pass, claim-status macros honest, `raeez-math-template.sty` symlink intact (`make check` in `~/latex-template`), Beilinson gate clean. Build at session-end only.
5. **Use the model only for judgment calls.** Cross-reference resolution is deterministic per `\label`/`\ref`; theorem-numbering is deterministic per LaTeX. Codex drafts proofs and chooses examples; it does not invent term names without the four-part test or coefficients without `landscape_census.tex` / primary literature.
6. **Token budgets are not advisory.** Monograph-scale; checkpoint between chapters and between Beilinson-tower levels (0–5). For long-form proof harness sessions, load context first, build internal outline, do not paginate.
7. **Surface conflicts, don't average them.** Canonical theorem statement wins over inline commentary. Master Reconstruction Theorem (climax) wins over earlier formulations. A computation in `compute/` or `landscape_census.tex` wins over prose claims — never overwrite from memory.
8. **Read before you write.** Read the affected theorem and its hypothesis package. Read the cross-volume companion section (Vol II / III) before editing a vertical-equivalence chapter. Grep legacy `notes/claude_md_legacy_*.md` and `notes/first_principles_cache_comprehensive.md` — never read whole.
9. **Tests verify intent.** Claim-status macros (`\ClaimStatusProvedHere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusRetracted`) are the load-bearing test. A theorem labelled `proved` with a proof gap is broken. Four-part term-coining test is non-vacuous.
10. **Checkpoint after every significant step.** Between chapters, summarize theorem-ledger delta and cross-volume equivalence impact. Between Beilinson-tower levels, restate reconstruction-theorem status. Subagents return evidence, not authority; main thread integrates via deep semantic merge.
11. **Match the codebase's conventions, even if you disagree.** `raeez-math-template.sty` symlinked at repo root, loaded immediately after `\documentclass`, `\mainpreambleonly` guard preserved (`INVARIANTS.md §XII`). Theorem environments per template. No local typography forks.
12. **Fail loud.** Announce every broken cross-ref, dangling theorem, unhealed conjecture label (`INVARIANTS.md §XI`). Never demote Theorem A to motivation; heal it. Never silently overwrite a computation from memory. Cross-volume / compute-vs-prose disagreements stop and report.
