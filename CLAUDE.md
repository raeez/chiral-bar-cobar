# CLAUDE.md

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
| **C** | derived-centre complementarity | $\kappa + \kappa^! \in \{0, 13, 250/3, 98/3\}$ (family-dependent) |
| **D** | obstruction-tower universality | $\mathrm{obs}_g = \kappa \cdot \lambda_g$ |
| **H** | Hochschild concentration | $\mathrm{ChirHoch}^\bullet(A)$ lives in $\{0, 1, 2\}$ |

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
  `~/calabi-yau-quantum-groups`, ~693 pp. The CY-to-chiral functor
  $\Phi$, K3 Yangian, CY landscape, Borcherds/Monster BKM algebras.

## What counts as progress

- A new theorem stated precisely, proved rigorously, inscribed with a
  proof body a reader can verify against primary literature.
- A new example: compute $\kappa$, the shadow tower, bar cohomology,
  derived centre, for an algebra not yet tabulated.
- A falsified claim: demonstrating an asserted identity fails at a
  specific parameter point.
- A sharpened scope: restricting a theorem to the narrowest hypothesis
  on which its proof actually holds.
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

## Where the bookkeeping lives

The following files hold the accounting and disciplinary content that
used to clutter this file. Grep them when you need a specific index;
do not let them occupy cognitive space.

- **`notes/claude_md_legacy_20260418.md`** — the full prior CLAUDE.md
  (1408 lines, lossless). Contains the complete AP/FM/B/HZ/PE
  catalogues, the theorem-status table, the constitutional trust
  warning, the metadata hygiene protocol, Opus quirks, prose-hygiene
  rules, and the pre-edit verification protocol templates. Grep by
  index (`AP126`, `FM30`, `PE-5`, `HZ-4`, `B28`). Do not read whole.
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
  `~/calabi-yau-quantum-groups`.
- **`FRONTIER.md`**, **`AGENTS.md`**, **`README.md`**, theorem-status
  tables, adversarial-swarm logs in `adversarial_swarm_*/`, session
  memorials in `memory/` — *working notebooks*, not canonical
  references. They drift. When they conflict with
  `landscape_census.tex` or a primary paper, the primary wins.

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
`\ClaimStatusHeuristic`) are reader-facing bookkeeping. Default to
`\ClaimStatusConjectured` when uncertain — downgrading is cheaper than
overclaiming. Do not spend cognitive cycles tuning them; the hook and
session review catch drift.

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

## What not to do

1. Do not spawn 30 parallel Codex agents for an adversarial audit.
   The codex-companion serializes and silently budget-cuts;
   empirical throughput is ~1 substantive deliverable per session
   window. Direct edits in the main thread are higher throughput for
   virtually any bookkeeping-style target.
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
8. Do not confuse this file with a configuration manual. This file is
   a mathematician's working manifesto. If it ever grows again to the
   shape of a config manual, shrink it back.
