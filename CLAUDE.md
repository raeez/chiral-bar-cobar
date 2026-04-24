# CLAUDE.md

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation. Read it first. Repo-local rules follow.

---

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge. Specifically, for understanding **E_1–E_1 operadic Koszul
duality in the homotopical modular chiral realm on algebraic curves** —
and what that duality implies about the five invariants (Theorems A, B,
C, D, H) that survive the averaging map
$\mathrm{av}: \mathfrak{g}^{E_1} \to \mathfrak{g}^{\mathrm{mod}}$ from
ordered to symmetric chiral (co)homology.

Every tool call, every edit, every agent decision made here has one
purpose: to advance that understanding, one true theorem at a time.

When a choice presents itself between doing mathematics and updating
accounting, **do the mathematics.** The accounting can wait. The
accounting is handled automatically by the PostToolUse hook and can
always be reconciled at session end. Mathematics requires a live mind.

## The mathematics

**One object**: the ordered bar complex
$B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ on
$\overline{M}_{g,n}$ over the relative factorisation stack.

**One relation**: the Arnold relation
$\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$
on $\mathrm{Conf}_n(X)$ with $\eta_{ij} = d\log(z_i - z_j)$.

**One equation**: the Maurer–Cartan identity
$D \cdot \Theta_A + \tfrac{1}{2}[\Theta_A, \Theta_A] = 0$
for the universal obstruction $\Theta_A$ in the ordered convolution dGLA.

**One dichotomy**: every standard chiral algebra collapses, under the
averaging map, into exactly one of four archetypes G / L / C / M with
shadow-tower depth $r_{\max} \in \{2, 3, 4, \infty\}$. The four classes
are witnessed by Heisenberg, affine Kac–Moody, $\beta\gamma$, and
Virasoro; every other algebra in the standard landscape reduces to one
of these by the averaging principle.

**Five theorems crystallise this structure**:

| | | |
|---|---|---|
| **A** | bar–cobar equivalence (backbone adjunction) | $\Omega^{\mathrm{ch}} \dashv B^{\mathrm{ch}}$ |
| **B** | chiral Positselski | $\Omega_X(B_X(C)) \xrightarrow{\sim} C$ in $D^{\mathrm{co}}_{\mathrm{ch}}(X)$ |
| **C** | derived-centre complementarity | $\kappa + \kappa^! \in \{0, 8, 13, 250/3, 98/3\}$ (family-dependent, $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ five-archetype ceiling; classical $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ subset is $\{0, 13, 250/3, 98/3\}$; the $\mathsf{B}$-row ceiling $K^\kappa = 8$ is the Vol III Mukai-enhanced K3 Heisenberg witness via Bruinier Heegner Chern-class reciprocity) |
| **D** | obstruction-tower universality | $\mathrm{obs}_g = \kappa \cdot \lambda_g$ |
| **H** | Hochschild concentration | $\mathrm{ChirHoch}^\bullet(A)$ lives in $\{0, 1, 2\}$ |

On $\mathrm{CY}_d$-categories arising from Calabi–Yau $d$-folds, the
Vol III functor $\Phi_d$ factors through holomorphic factorisation
algebras, $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ
\Phi^{\mathrm{FA}}_d$; Theorem A's bar–cobar adjunction is the
$E_1$-chiral shadow on the reference curve $C$ after Stage-2
specialisation. A single CY$_d$ category admits a family of
$E_1$-chiral shadows indexed by $(\Sigma_{d-1}, C)$; Theorem A governs
each shadow on its curve.

Everything in this repository — chapters, standalones, compute modules,
tests, diagrams — is a concentric ring around those five theorems, or
an invariant (shadow tower, Koszulness, $\mathsf{SC}^{\mathrm{ch,top}}$,
$E_n$ identification, topologisation, Yangian/RTT, CY-to-chiral
functor $\Phi$) that refines them.

Three volumes hold this structure:

- **Vol I** *Modular Koszul Duality* — this repo, ~2,700 pp. The bar-complex
  backbone, five-theorem core, standard-landscape census, physics
  bridges, seven faces of $r(z)$.
- **Vol II** *$A_\infty$ Chiral Algebras and 3D HT QFT* —
  `~/chiral-bar-cobar-vol2`, ~1,749 pp. SC^{ch,top} bar differential as
  holomorphic factorisation, coproduct as topological factorisation,
  seven parts culminating in 3D quantum gravity.
- **Vol III** *CY Categories, Quantum Groups, and BPS Algebras* —
  `~/calabi-yau-quantum-groups`, ~693 pp. The CY-to-chiral two-stage
  factorisation $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}
  \circ \Phi^{\mathrm{FA}}_d$ (stage 1: canonical $E_d$-holomorphic
  factorisation algebra on a CY$_d$ variety, pinned by
  Kontsevich–Tamarkin $E_d$-formality + Costello–Gwilliam–Li
  locality; stage 2: factorisation homology over a $(d-1)$-cycle
  $\Sigma_{d-1}$ followed by restriction to a reference curve $C$),
  K3 Yangian, CY landscape, Borcherds/Monster BKM algebras. A single
  CY$_d$ category admits a FAMILY of $E_1$-chiral shadows indexed by
  $(\Sigma_{d-1}, C)$.

## What counts as progress

- A new theorem stated precisely, proved rigorously, inscribed with a
  proof body a reader can verify against primary literature.
- A new example: compute $\kappa$, the shadow tower, bar cohomology,
  derived centre, for an algebra not yet tabulated.
- A falsified claim repaired by a corrected statement, construction, or
  proof obligation.
- A healed statement: the natural hypothesis and proof on which the
  intended theorem actually holds.
- A concrete first-principles computation that replaces a
  citation-only black box (e.g. the in-place derivation of
  $\langle \Lambda | \Lambda \rangle = c(5c+22)/10$ from the Virasoro
  algebra, replacing the Zamolodchikov / BPZ attribution).

**Progress is *not*** updating a status-table row, renaming a label,
counting equivalences in a meta-theorem, propagating a scope qualifier
across ten files, retracting advertising in `FRONTIER.md`, or editing
`AGENTS.md` to match `CLAUDE.md`. Those are bookkeeping. The hook
catches them after every inscription; you do not have to.

## Beilinson's dictum (the working epistemology)

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

Every claim is false until independently verified from primary source.
Prefer a smaller true theorem to a larger false one. Every numerical
claim should have 3+ genuinely independent verification paths (direct
computation, alternative formula, limiting case, symmetry/duality,
cross-family, literature + convention, dimensional analysis, numerical
evaluation).

**Epistemic hierarchy** (higher wins):
1. Direct computation.
2. `.tex` source ±100 lines of the claim.
3. Build system / test suite.
4. Published literature (primary).
5. `chapters/connections/concordance.tex`.
6. This file.
7. Memory.

Before every assertion: *"How do I know this? Read the source, computed
it, or assumed it?"* If assumed, stop and verify.

## The manuscript is self-complete, self-coherent, self-consistent

The current version stands for itself and only itself. All LaTeX
mathematical writing is standalone, up-to-date, consistent, coherent.
The manuscript does not reference its own previous versions. There is
no place in this research programme for references to previous
versions, intermediate ansätze, earlier drafts, retracted values,
superseded formulas, or any other drafting-history commentary. If a
formula used to be $X$ and now it is $Y$, the manuscript says $Y$;
it does not say "$Y$ (previously $X$, now retracted)", does not say
"$Y$ supersedes the earlier $X$", does not explain how the author
arrived at $Y$.  The mathematical argument proves $Y$; the drafting
trajectory is not part of the mathematics.

When a mathematical retraction is genuinely informative --- a proof
that was attempted and failed, whose failure illuminates why the
successful proof is forced --- state the failed argument and its
flaw as mathematics: "the identity $[m_k, B^{(2)}] = 0$ fails
per-$k$ because cyclic invariance controls adjacent contractions
but not non-adjacent terms (Proposition~X)". Do not frame it as
"the author initially attempted $X$ but retracted in favour of $Y$".
The mathematics is the Gap/Flaw, not the drafting record.

## Writing standard: Chriss–Ginzburg north star

The manuscript prose is written in the Chriss–Ginzburg voice,
channelling simultaneously the Russian elite mathematical school ---
Gelfand, Manin, Drinfeld, Arnold, Beilinson, Bernstein, Kapranov,
Etingof, Kazhdan, Kontsevich, Soibelman, Bezrukavnikov --- and the
mathematical physics elite --- Polyakov, Nekrasov, Witten, Costello,
Gaiotto, Moore, Segal. **Show don't tell.** Do not narrate. Construct
the mathematics directly and let the synthesis of disparate technical
domains (algebra + geometry, physics + mathematics, operads +
representation theory, Hodge theory + automorphic forms) bring out
the inner music of the subject.

**Forbidden in manuscript prose** (reader-facing `.tex` in `chapters/`,
`frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`):

- Bookkeeping vocabulary of any kind. No "Wave N", no "round M",
  no "batch K", no "DNA strand S$x$", no "AP$n$", no "antipattern $n$",
  no "Pattern $n$", no "cache entry $n$", no "CG-rectify pass $k$",
  no "$\mathsf{HZ}$-$n$ inscription". These belong in `notes/`,
  `FRONTIER.md`, commit messages, and the local `memory/` --- never
  in the manuscript.
- Meta-narration of the author's intent: "we now turn to",
  "having established", "let us now", "this brings us to",
  "it is worth noting", "notably", "crucially", "remarkably",
  "furthermore", "moreover", "in the present work", "this preface's
  role is to". Delete every instance; replace with direct mathematical
  statements.
- Hedging the mathematics does not earn. If the identification
  $X = Y$ is proved, write "$X = Y$"; do not write "$X$ is closely
  related to $Y$". Courage, after Drinfeld and Polyakov and Nekrasov:
  the equals sign is a theorem, not a suggestion.

**Required** (the CG standard):

- Every section and subsection title names a mathematical object,
  construction, theorem, or question --- never a process, wave,
  round, or meta-organising device.
- Every definition is preceded within ten lines by the question
  or obstruction it answers. The reader feels "of course" before
  the definition arrives.
- Every symbol is defined at or before first use, with a
  parenthetical first-principles definition for standard concepts
  (D-module, Ran space, FM compactification, Hodge bundle,
  $L_\infty$-algebra, Kuga--Satake, Humbert divisor).
- Every physical claim is labelled: theorem, heuristic, or
  metaphor. When a physical identification can be stated as a
  theorem, state it as a theorem; do not hide the content as an
  "analogy".
- **Economy.** Every word carries weight. A paragraph that can be
  one sentence is one sentence.
- At every section boundary, three sentences: (1) what was just
  established; (2) the question or obstruction the next section
  resolves; (3) the construction or theorem that resolves it.
  These sentences are *mathematics*, not signposts.

The reader is an equal who sees the force of the argument when it
is stated with sufficient precision. The prose does not explain
mathematics; it *is* mathematics, carrying the same logical force
as the displayed equations.

This rule is retroactive and forward-looking. Existing manuscript
prose containing bookkeeping vocabulary is to be rectified chapter
by chapter through the `chriss-ginzburg-rectify` skill; new prose
is to be written in the CG voice from the first keystroke.

## How to work

**Formulas come from `chapters/examples/landscape_census.tex` or a
primary paper** — never from memory. $\kappa$ per family, $r(z)$ per
family, central charges per family: `landscape_census.tex` is the
canonical source. If the formula is not there, write it there first
(with primary-literature citation), then use it.

**Proofs are inscribed in the chapter, not in notes.** A proof that
lives only in `notes/` or a swarm log is not a proof. It is a draft.
Move it into `chapters/**.tex` with a `\label{thm:...}` and a
`\begin{proof}...\end{proof}` body.

**After every inscription** (theorem, proposition, lemma, corollary,
definition, proof, remark), the PostToolUse hook
(`.claude/hooks/beilinson-gate.sh`) sweeps the edited file for known
anti-pattern signatures and cached confusion patterns. Read its
advisory output; address what it flags; return to the mathematics.

**Builds happen at session end**, only when the user asks:

```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast     # Vol I
cd ~/chiral-bar-cobar-vol2 && make                        # Vol II
cd ~/calabi-yau-quantum-groups && make fast               # Vol III
```

Do not run `make fast` after every edit. The hook does not nag about
builds. Compilation errors surface on the session-end build.

**Tests** — prefer running only the test file for the module you have
edited. `make test` (fast, ~1 min) or `make test-full` (~119K tests,
~minutes) are last resorts.

**Compute engine** — `compute/` holds the numerical-verification surface
(per-family $\kappa$, shadow-tower entries, bar cohomology, landscape
identities). When a new $\kappa$ or shadow-tower entry is inscribed, add
the verification test alongside it: direct computation sits at the top
of the epistemic hierarchy. Venv auto-detected at `compute/.venv/`.

**Validation gates** (automations of Beilinson's dictum — run when
sharpening scope or auditing a cascade, not on every edit):
`make integrity` (strict rebuild + claim-tag coverage),
`make audit` (Beilinson proof-chain audit on the theorem DAG),
`make verify-independence` (ProvedHere tautology / orphan check),
`make verify` (anti-pattern scan across all `.tex`),
`make census` (claim-tag accounting).

**Standalone papers** — `standalone/` holds extraction papers (A--P
plus surveys), built with `make standalone`. They pull from the
chapters; they are not independent drafts and never fork a formula.

## Essential constants (for quick cross-reference)

- $\kappa(V_k(\mathfrak{g})) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$
  (affine Kac–Moody, trace-form).
- $\kappa(\mathrm{Vir}_c) = c/2$.
- $\kappa(\mathcal{H}_k) = k$ (Heisenberg).
- $\kappa(\mathcal{W}_N) = c(H_N - 1)$ with $H_N = \sum_{j=1}^N 1/j$.
- Virasoro shadow: $S_2 = c/2$, $S_3 = 2$,
  $S_4 = 10/[c(5c+22)]$, $S_5 = -48/[c^2(5c+22)]$.
- Zamolodchikov norm $\langle\Lambda|\Lambda\rangle = c(5c+22)/10$ with
  $\Lambda = {:}TT{:} - (3/10)\partial^2 T$.
- $r$-matrix, trace form (level prefix MANDATORY):
  $r^{KM}(z) = k\,\Omega/z$, $r^{\mathrm{Heis}}(z) = k/z$,
  $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$.
- Desuspension: $|s^{-1}v| = |v| - 1$; cohomological grading $|d| = +1$.
- Bar: $B(A) = T^c(s^{-1}\bar A)$, $\bar A = \ker \epsilon$.

**Five objects, never conflate**:
$A$ (algebra) — $B(A)$ (bar coalgebra) — $A^i = H^\star B(A)$
(dual coalgebra) — $A^! = ((A^i)^\vee)$ (dual algebra) —
$Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ (derived centre = bulk).
$\Omega(B(A)) = A$ is **inversion**, not Koszul duality. $A^!$ via
**Verdier**. Bulk via **Hochschild** cochains.

## Chain-level and $(\infty,1)$-categorical: equal status

Both **chain-level** mathematics (explicit complexes, named
differentials, witnessed homotopies, $L_\infty$-formalism,
Mittag–Leffler towers, ambient-qualified statements like
`mc5_class_m_chain_level_platonic.tex:229`) and **$(\infty,1)$-categorical**
mathematics (derived/$\infty$-stable categories, Lurie's $\mathrm{HA}$
formalism, factorisation $\infty$-categories, $\infty$-operadic
constructions a la Costello–Gwilliam, Francis–Gaitsgory) are **equally
load-bearing** in this programme. Neither is "the better lane"; neither
"replaces" or "subsumes" the other.

A theorem stated and proved at chain level (with explicit chain
homotopy $h$ satisfying $[d, h] = \mathrm{id} - p$, witnessed at a
file:line) is just as valid as the same theorem stated and proved at
$(\infty,1)$-categorical level (with the homotopy-coherent adjunction
exhibited via Lurie's $\mathrm{HA}.5.5$ machinery). The two lanes
**inform each other**:

- Chain-level lets you **compute** with named generators, named
  differentials, named pole-orders. It exposes the arithmetic that an
  $(\infty,1)$-statement abstracts away. Use chain-level for $\kappa$
  computations, shadow-tower entries $S_k$, OPE pole orders, explicit
  bar–cobar contractions on a finite generating set, and any concrete
  numerical claim that has to be verified against a primary source.
- $(\infty,1)$-categorical lets you **state** the universal property
  cleanly: bar–cobar as the adjunction of $(\infty,1)$-categories
  (Pattern 269), $\mathrm{ChirAlg}^{\mathrm{ch}}_X$ as a presentable
  $\infty$-category, factorisation as an $\infty$-operadic structure,
  Hochschild cochains as the derived endomorphism object in an
  $\infty$-stable category. Use $(\infty,1)$-categorical for stating
  universal properties, for working with derived categories of
  $D$-modules / sheaves, and for any theorem whose statement requires
  passing to the homotopy category to even be true on the nose.

**Operating rule**: state every theorem in the lane in which its proof
actually works. If chain-level: name the chain homotopy / Mittag–Leffler
witness / explicit MC element / explicit OPE pole. If
$(\infty,1)$-categorical: name the $(\infty,1)$-functor / adjunction /
limit-colimit construction. If both: state both, label which lane each
status applies to (Pattern 236 ambient-qualifier discipline). **Never**
write "this is just the chain-level / $(\infty,1)$-categorical
shadow of the real theorem": both shadows are real, both are the
theorem, viewed through different lenses.

Pattern 269 (adjunction-strictness conflation: chain-level adjunctions
need explicit splitting witnesses; $(\infty,1)$-categorical
adjunctions are the natural home for chiral bar–cobar) is a *scope
declaration*, not a hierarchy. The chain-level statement at
`mc5_class_m_chain_level_platonic.tex:229` (pro-object /
weight-completed ambient) and the $(\infty,1)$-statement (derived
category of factorisation $D$-modules) are **two different theorems**
about two different mathematical objects, both proved, both load-bearing.

## Where the bookkeeping lives

The following files hold the accounting and disciplinary content that
used to clutter this file. Grep them when you need a specific index;
do not let them occupy cognitive space.

- **`notes/antipatterns_catalogue.md`** — the live Vol I AP catalogue
  (AP register plus cross-volume additions through AP936, including
  the 2026-04-22 Vol III two-stage factorisation wave: AP929--AP936
  covering single-stage $\Phi_d$ framing, six-routes-as-$\Phi_3$,
  Fake-Monster dimension discipline, Super-Yangian envelope
  trichotomy, $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ manifesto
  reinforcement, $\mathrm{CoHA}(\C^3) = Y^+$ reinforcement, warning
  environment prohibition, discipline-token leakage). Every
  `/chriss-ginzburg-rectify` invocation consults this at Gate 0
  alongside the cache. Append new APs here; do not add to the legacy
  file.
- **`notes/cross_volume_aps.md`** — cross-volume AP reference
  (AP-CY* from Vol III, V2-AP* from Vol II) consulted when editing
  material that spans volumes.
- **`notes/claude_md_legacy_20260418.md`** — the full prior CLAUDE.md
  (1408 lines, lossless). Historical snapshot; the AP catalogue has
  moved to `notes/antipatterns_catalogue.md`. Still contains the
  theorem-status table, the constitutional trust warning, the
  metadata hygiene protocol, Opus quirks, prose-hygiene rules, and
  the pre-edit verification protocol templates. Grep by index for
  historical context. Do not read whole.
- **`notes/agents_md_legacy_20260418.md`** — the full prior
  AGENTS.md, lossless.
- **`notes/first_principles_cache_comprehensive.md`** — ~250-entry
  confusion-pattern registry with regex triggers. The hook auto-checks
  the top-15 patterns on every inscription; grep the full registry
  when planning a proof that touches a delicate conflation zone (CY vs
  chiral, algebra vs coalgebra, averaging vs derived centre, chain vs
  cohomological, specific vs general).
- **`appendices/first_principles_cache.md`** — the cache tip as
  inscribed in the manuscript (top entries; see end of file for latest).
- **`chapters/examples/landscape_census.tex`** — canonical formulas
  per family. The source of truth for every $\kappa$ and every $r(z)$.
- **`chapters/connections/concordance.tex`** — the repo's constitution
  and authoritative convention document.
- **Volume-specific** `CLAUDE.md` in `~/chiral-bar-cobar-vol2` and
  `~/calabi-yau-quantum-groups`. Vol III carries the canonical
  CY$_d$ $\kappa_\bullet$ table
  (`~/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex`)
  and the two-stage factorisation
  $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ
  \Phi^{\mathrm{FA}}_d$
  (`~/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`).
- **`README.md`** — public-facing programme status: the five-theorem
  table, shadow-depth table, 16-paper standalone map, page counts.
  Canonical for the headline shape; lags the live chapters by days.
  Read it when orienting a new agent to the programme.
- **`FRONTIER.md`**, **`AGENTS.md`**, theorem-status tables,
  adversarial-swarm logs in `adversarial_swarm_*/`, session memorials
  in `memory/` — *working notebooks*, not canonical references. They
  drift. When they conflict with `landscape_census.tex` or a primary
  paper, the primary wins.

## Git and authorship

All commits are authored by **Raeez Lorgat**. Never any AI attribution
anywhere: no `Claude`, no `Anthropic`, no `Co-Authored-By`, no
`Generated with`, no 🤖, in commits, comments, docstrings, or
manuscripts. The pre-commit hook nudges on this; if it fires, remove
the offending content — do not paper over.

`git stash` is forbidden (use `git diff > patch.diff && git apply`
when you need to pause work). Do not amend commits without explicit
instruction. The repository constitution is
`chapters/connections/concordance.tex`.

## LaTeX hygiene

Macros live in `main.tex`'s preamble. Inside chapters, use
`\providecommand`, never `\newcommand`. The programme compiles with
`memoir` + EB Garamond (`newtxmath + ebgaramond`).

Claim-status tags (`\ClaimStatusProvedHere`,
`\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`,
`\ClaimStatusHeuristic`) are reader-facing bookkeeping, not repairs. When
uncertain, name the exact proof obligation and heal the proof, statement,
or construction; do not downgrade the manuscript to close. Do not spend
cognitive cycles tuning labels; the hook and session review catch drift.

## Ambient hooks (automatic)

- **`PreToolUse(Agent)`** → `cache-injection.sh` prepends the
  first-principles-protocol preamble to every Agent call.
- **`PreToolUse(Bash, git commit)`** → pre-commit reminder: no AI
  attribution, Raeez Lorgat only.
- **`PostToolUse(Edit|Write)`** → `beilinson-gate.sh` scans the
  edited `.tex` / `.py` file for:
  (a) the canonical anti-pattern signatures
  (AP7/8/14/19/24/25/27/33/34/40/44/45/106/113/117/121/124/134/186/AP-CY61,
  PROSE slop, AAP1 tool-markup leak);
  (b) when the edit introduces a theorem / proposition / lemma /
  corollary / definition / proof / remark block, the top-15 cache
  confusion patterns (specific/general, bare κ, native/derived $E_n$,
  construction/narration, algebra/coalgebra, CoHA vs vertex algebra,
  Drinfeld centre vs averaging, two-$\hbar$ without bridge, chain vs
  cohomological, part/whole for $\{b_k, B^{(2)}\}$,
  $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$
  coincidence, Künneth-multiplicative $\kappa_{\mathrm{cat}}$ on
  products);
  (c) cross-volume formula propagation awareness (AP5).
  Output appears as `additionalContext` in the next tool result.
- **`Stop`** → `convergence-gate.sh` session-end summary.

The hook is advisory. When it flags a false positive (e.g., a
legitimate Heisenberg or affine-KM $\kappa + \kappa^\vee = 0$), note
the scope in the inscription and move on — do not argue with the hook.

## Long-form proof harness

For Claude Code, Codex CLI, and any GPT-5.5 / GPT-5-Codex-class agent,
frontier mathematics runs in maximum-effort mode. Use the deepest
host-exposed model and reasoning budget. If the host offers a
GPT-5.5 Pro / Heavy or `xhigh` setting, use it for theorem repair,
cross-volume synthesis, adversarial review, and primary-source
reconstruction. The private ChatGPT Pro harness is not public; this is
the open local analogue.

Long runs are normal. A 30-60 minute agent run is acceptable when a
proof obligation requires it. The agent first loads the relevant
context (`CLAUDE.md`, `AGENTS.md`, target chapter, dependencies,
bibliography, compute files, cross-volume anchors), builds an internal
outline, then works through independent proof routes: worked example,
formal argument, primary source, computation, and cross-volume
consistency. Private scratch stays private; the deliverable is the
checked proof trace and the exact remaining obstruction.

After every proposed repair, run an attack-heal loop: strongest
counterexample, sign/convention check, ambient-category check, missing
hypothesis, false functoriality, unproved equivalence, numerical
constant. Heal and attack again until the theorem closes or the exact
obstruction is named for the next repair cycle. Do not downgrade the
manuscript to close the loop. Subagents provide evidence, not authority;
the main thread integrates by deep semantic merge.

## What not to do

1. Do not treat old throughput cautions as a prohibition on swarms.
   When the user explicitly asks for a large adversarial or
   cross-volume swarm, it is allowed. Partition work by disjoint files
   or mathematical axes, require short verifiable reports, and merge by
   deep semantic review across Vol I/II/III.
2. Do not propagate status-label wording across 10 files when
   mathematics is waiting.
3. Do not invent formulas from memory. Consult
   `landscape_census.tex` or primary literature.
4. Do not run `make fast` after every edit.
5. Do not add AI attribution anywhere.
6. Do not `git stash` or amend commits.
7. Do not read `notes/claude_md_legacy_20260418.md` or
   `notes/first_principles_cache_comprehensive.md` whole — grep them
   by the specific anchor you need.
8. Do not build on a new theorem without auditing its proof first.
   When you sharpen one theorem, re-check every theorem that cites
   it — the Beilinson cascade is a real failure mode. Prefer a
   smaller audited theorem to a larger unaudited one.
9. Do not defend prior output by sampling files and citing AP
   discipline. When the user says content is wrong, believe the user
   and ask what to fix. Self-audit of one's own mathematics is
   negative yield; it rationalises rather than corrects.
10. Do not confuse this file with a configuration manual. This file is
    a mathematician's working manifesto. If it ever grows again to the
    shape of a config manual, shrink it back.

## 2026-04-22 cross-volume sharpenings

Four load-bearing markers from the Vol III programme now anchor Vol I
material. These are not decorative cross-references; the Vol I
landscape examples, the $\mathsf{B}$-row of derived-centre
complementarity, and the BRST ghost identity each refactor through
them.

**Eight-form spread.** The $\mathsf{B}$-row ceiling $K^\kappa = 8$ in
Theorem C sits at the $N = 1$ vertex of a universal eight-form
Gritsenko--Cl\'ery spread. Weights
$w(N) \in \{5, 2, 1, 1, 1/2, 1, 1/4, 0\}$ and Fourier zero-coefficients
$c_N(0) \in \{10, 4, 2, 2, 1, 2, 1/2, 0\}$ give
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2 \in \{5, 2, 1, 1, 1/2, 1, 1/4, 0\}$
for $N \in \{1, 2, 3, 4, 6\}$ and the half-integer / quarter-integer
continuations. Cover assignment: integer weight rides
$\mathrm{Sp}_4(\Z)$, half-integer weight rides $\mathrm{Mp}_4$,
quarter-integer weight rides the double cover
$\widetilde{\mathrm{Mp}}_4$; the weight-zero form is the degenerate
terminal fibre. Vol I's $\kappa_{\mathrm{BKM}} = 5$ is the $N = 1$
anchor; the remaining five $N$-rows are witnessed in Vol III.

**Universal Borcherds weight identity.** The formula
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is the canonical form for
every $N \in \{1, 2, 3, 4, 6\}$. Primary sources: Borcherds 1995
(singular-theta lift and denominator-formula weight), Gritsenko 1999
(explicit $\Delta_5$, $\Delta_2$, $\Delta_1$ series and their Fourier
expansions). Vol I's lattice examples --- the Monster $V^\natural$
denominator, the fake-Monster lattice $\mathrm{II}_{25,1}$, the
Niemeier family --- cite this universal form rather than any additive
split $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} +
\chi(\mathcal{O}_{\mathrm{fiber}})$, which fails at every $N$ (at
$N = 1$ the left side is $5$, the right side is $0 + 0 = 0$).

**Three-factor Universal Trace Identity.** On the Koszul-self-dual
subcategory whose objects admit a BRST resolution and a Calabi--Yau
target supporting a Borcherds product,
$$
\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2)
= \mathrm{tr}_{\mathrm{Pentagon}}
= \omega_{\mathrm{Borcherds}}
= c_N(0)/2.
$$
Vol I supplies the ghost-scope reading: $Q_{\mathrm{BRST}}^2 = 0$ is
the nilpotency that forces the trace to land in the Euler-characteristic
class of the $\Sigma_{d-1}$-cycle. Vol II supplies the Pentagon-scope
reading on the $\mathsf{SC}^{\mathrm{ch,top}}$ boundary. Vol III
supplies the Borcherds-scope reading as the singular-theta weight. The
three scopes agree where they all apply; they do not compete.

**Universal positive-geometry grammar.** Every standard-landscape
example in Vol I --- Heisenberg $\mathcal{H}_k$, free fermion,
$bc(\lambda)$, $\beta\gamma(\lambda)$, affine Kac--Moody
$V_k(\mathfrak{g})$, Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$,
Bershadsky--Polyakov $BP$ --- fits the template
$Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$
for some Calabi--Yau target $X$ via Stage-1 $\Phi^{\mathrm{FA}}_d$,
with Drinfeld double $G(X) = D(Y^+(X))$. Four equivariance strata
discriminate the examples: toric $T^d$ (local surfaces), reduced
$\C^\times + \mathrm{Aut}(X)$ (K3, K3 $\times$ E, abelian surfaces),
orbifold inertia $I(X/G)$ (Mathieu / McKay lattices), and
lattice-polarised period domain (Borcherds / Gritsenko lifts). The
shadow tower on a given example is the specialisation of $Y^+(X)$ to
$C = \mathbb{P}^1$ with the stratum-appropriate equivariance.

## Branch and worktree reconciliation -- DEEP SEMANTIC MERGES ONLY

When branches or worktrees differ, ALWAYS perform a **deep semantic
merge** to reconcile them. **NO EXCEPTIONS.**

- Never discard one side of a divergence without reading it.
- Never `git reset --hard`, `git checkout --`, or `git restore` to
  clobber work as a shortcut to resolve conflict.
- Never force-push to obliterate upstream divergence.
- Read both sides in full, understand what each side uniquely
  contributes, and construct a merged result that preserves the
  mathematical content, prose improvements, and structural refinements
  from **both** sides. When a line-level conflict is semantic
  (e.g., a theorem statement reworded), merge at the semantic level --
  pick the stronger statement, the tighter citation, the more rigorous
  proof -- not at the diff-hunk level.
- When unclear which side is stronger on a given hunk, read both in
  context. Do not guess.

Applies to: `git pull`, `git merge`, worktree reconciliation, cherry-picks
across branches, rebase conflicts, and any divergence between local and
upstream (including push rejections where upstream has new commits).

**Rationale:** work loss in this programme is irrecoverable -- chapters
represent weeks of adversarial-swarm output, elite-voice synthesis, and
primary-literature audit. A shallow "accept theirs" / "accept ours" is
never the right answer. Deep semantic merges take longer but are the
only operation consistent with Beilinson's dictum and the golden rule
"NEVER CUT CONTENT".
