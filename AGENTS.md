# AGENTS.md

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge. Specifically, for understanding **E_1–E_1 operadic Koszul
duality in the homotopical modular chiral realm on algebraic curves**
and the five invariants (Theorems A, B, C, D, H) that survive the
averaging map from ordered to symmetric chiral (co)homology.

If you are an agent operating in this repository, your purpose is
identical to that mission. Every action you take — read, grep, edit,
inscribe, refactor, retract — is in service of advancing that
understanding, one true theorem at a time.

When a choice presents itself between doing mathematics and updating
accounting, **do the mathematics.** Accounting is automated by the
PostToolUse hook and can always be reconciled at session end.
Mathematics requires a live mind.

## The mathematics you are working on

**One object**: the ordered bar complex
$B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$.

**One relation**: the Arnold relation on $\mathrm{Conf}_n(X)$.

**One equation**: $D\cdot\Theta_A + \tfrac{1}{2}[\Theta_A,\Theta_A] = 0$
in the ordered convolution dGLA.

**One dichotomy**: every standard chiral algebra collapses under
averaging into G / L / C / M (shadow-depth 2 / 3 / 4 / $\infty$).

**Five theorems** (Theorem A bar–cobar, Theorem B chiral Positselski,
Theorem C derived-centre complementarity, Theorem D obstruction-tower
universality, Theorem H Hochschild concentration in $\{0,1,2\}$).

Three volumes hold the structure: Vol I (this repo), Vol II
(`~/chiral-bar-cobar-vol2`), Vol III
(`~/calabi-yau-quantum-groups`).

## What counts as progress

- A new theorem, precisely stated, rigorously proved, inscribed with
  a proof body verifiable against primary literature.
- A new example: $\kappa$, shadow tower, bar cohomology, derived
  centre for an algebra not yet tabulated.
- A falsified claim: asserted identity fails at a specific parameter.
- A sharpened scope: narrowest hypothesis on which a proof actually
  holds.
- A first-principles computation replacing a citation black box.

## What does NOT count as progress

Updating a status-table row. Renaming a label. Counting equivalences
in a meta-theorem. Propagating a scope qualifier across ten files.
Retracting advertising in `FRONTIER.md`. Editing `AGENTS.md` to
match `CLAUDE.md`. These are bookkeeping. The hook catches them.
You do not have to.

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

Every claim is false until independently verified from primary
source. Prefer a smaller true theorem to a larger false one. Every
numerical claim should have 3+ independent verification paths.

Epistemic hierarchy (higher wins): direct computation > `.tex`
source ±100 lines > build system > published literature (primary) >
`concordance.tex` > `CLAUDE.md` > memory.

## How to work

Formulas come from `chapters/examples/landscape_census.tex` or a
primary paper — never from memory.

Proofs live in `chapters/**.tex` with a `\label{thm:...}` and a
`\begin{proof}...\end{proof}` body — not in notes.

After every inscription (theorem, proposition, lemma, corollary,
definition, proof, remark), the PostToolUse hook
(`.claude/hooks/beilinson-gate.sh`) sweeps the edited file for
anti-pattern signatures and cached confusion patterns. Read its
output; address what it flags; return to the mathematics.

Builds happen at session end only, by user opt-in. Never run
`make fast` after every edit.

Tests — run only the module you have edited, not the full suite.

## Agent rules (hard)

1. **No AI attribution anywhere.** Ever. Commits by Raeez Lorgat
   only. No `Claude`, no `Anthropic`, no `Co-Authored-By`, no
   `Generated with`, no 🤖 in commits, comments, docstrings, or
   manuscripts. Pre-commit hook nudges on this.
2. **No `git stash`.** Use `git diff > patch.diff && git apply`.
3. **Do not amend commits** without explicit instruction.
4. **Do not build after every edit.** Session end only, on user
   opt-in.
5. **Never guess a formula.** `landscape_census.tex` or primary
   paper; if absent, inscribe it first with citation.
6. **Do not spawn 30 parallel Codex agents for an adversarial audit.**
   Empirical throughput: ~1 substantive deliverable per session
   window (codex-companion serialises and silently budget-cuts).
   Direct main-thread edits are higher throughput.
7. **Grep the legacy, don't read it whole.** The legacy files
   `notes/claude_md_legacy_20260418.md` and
   `notes/agents_md_legacy_20260418.md` are ~9,000 lines combined;
   grep by AP/FM/HZ/PE index.
8. **Claim-status tags** (`\ClaimStatusProvedHere`,
   `\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`,
   `\ClaimStatusHeuristic`) default to `\ClaimStatusConjectured` when
   uncertain. Downgrading is cheaper than overclaiming.

## Essential constants

- $\kappa(V_k(\mathfrak{g})) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$.
- $\kappa(\mathrm{Vir}_c) = c/2$; $\kappa(\mathcal{H}_k) = k$.
- $\kappa(\mathcal{W}_N) = c(H_N - 1)$, $H_N = \sum_{j=1}^N 1/j$.
- Virasoro shadow: $S_2=c/2$, $S_3=2$, $S_4=10/[c(5c+22)]$,
  $S_5=-48/[c^2(5c+22)]$.
- $\langle\Lambda|\Lambda\rangle = c(5c+22)/10$ for
  $\Lambda = {:}TT{:} - (3/10)\partial^2 T$.
- Five objects never conflated: $A$, $B(A)$, $A^i$, $A^!$,
  $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$. $\Omega(B(A))=A$ is
  **inversion** not Koszul duality; $A^!$ via **Verdier**; bulk via
  **Hochschild** cochains.
- r-matrix (trace form, level prefix MANDATORY):
  $r^{KM}(z) = k\Omega/z$, $r^{\mathrm{Heis}}(z) = k/z$,
  $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$.

## Build (session-end only)

```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast     # Vol I
cd ~/chiral-bar-cobar-vol2 && make                        # Vol II
cd ~/calabi-yau-quantum-groups && make fast               # Vol III
```

## Where the bookkeeping lives

- `notes/claude_md_legacy_20260418.md` — full prior CLAUDE.md,
  lossless (1408 lines). Grep for AP/FM/B/HZ/PE indices.
- `notes/agents_md_legacy_20260418.md` — full prior AGENTS.md,
  lossless.
- `notes/first_principles_cache_comprehensive.md` — ~250-entry
  confusion-pattern registry.
- `appendices/first_principles_cache.md` — cache tip in the manuscript.
- `chapters/examples/landscape_census.tex` — canonical formulas.
- `chapters/connections/concordance.tex` — repo constitution.
- `scripts/hooks/beilinson-gate.sh` — version-controlled hook source
  (copy into `.claude/hooks/` locally for Claude Code to invoke).

## Do not

1. Propagate status-label wording across 10 files when mathematics is
   waiting.
2. Invent formulas from memory.
3. Run `make fast` after every edit.
4. Add AI attribution anywhere.
5. `git stash` or amend commits.
6. Read `notes/claude_md_legacy_20260418.md` or
   `notes/first_principles_cache_comprehensive.md` whole — grep.
7. Confuse this file with a configuration manual. This is a
   mathematician's working manifesto.
