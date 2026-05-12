# CLAUDE.md

> **Inherits `~/ecosystem/INVARIANTS.md`.** Canonical ecosystem rules:
> destructive-git forbidden list, multi-agent worktree concurrency,
> standalone-documents discipline, Russian-school voice,
> every-file-into-the-repo, no-LLM-attribution on commits,
> deep-semantic-merges, intelligence propagation. Read it first.
> Repo-local rules follow.

---

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge — specifically, **$E_1$–$E_1$ operadic Koszul duality in the
homotopical modular chiral realm on algebraic curves**, and what the
averaging map
$\mathrm{av}: \mathfrak{g}^{E_1} \to \mathfrak{g}^{\mathrm{mod}}$
implies about the five invariants (Theorems A, B, C, D, H) that
survive the ordered-to-symmetric chiral (co)homology projection.

Every action — read, edit, agent dispatch, inscription, retraction —
advances that understanding, one true theorem at a time. When the
choice is between mathematics and accounting, **do the mathematics**;
accounting is automated. Mathematics requires a live mind.

---

## The platonic ideal architecture (Vol I, the Open quadrant)

Vol I is the **Open quadrant** of the four-quadrant programme
$(\text{Open} \cup \text{CY}) \times (\text{Cat} \cup \text{Chain})$ —
the complete five-level **Beilinson tower** on a tangential log curve
$(X, D, \tau)$:

```
factorisation dg-category C^op on (X, D, τ)        [level 0: primitive]
        ↓  choose vacuum b ∈ C^op
chart algebra  A_b = End_C(b)                       [level 1: chart]
        ↓  Theorem A — chiral Koszul reflection K² ≃ id
bar / twisting coalgebra  B(A_b) = T^c(s^{-1} Ā_b)  [level 2: twisting]
        ↓  Theorem H — Hochschild concentration ⊂ {0,1,2}
derived chiral centre  Z^der_ch(A_b) ≃ ChirHoch^•   [level 3: BULK]
        ↓
line / brane operators                              [level 4: operator]
        ↓  modular trace + clutching on open category
modular shadow (κ-tuple, partition function, form)  [level 5: scalar]
```

Each forgetful step has a **reconstruction theorem** with named
hypothesis package: Morita (1↔0), Theorem A (1↔2), Theorem H / B
(1→3), Drinfeld-double (4→3), modular reconstruction (5→4).

**KSDual** is the $\mathbb{Z}/2$-fixed sublocus under chiral /
antichiral involution $A \mapsto A^!$. On KSDual, Theorem A is an
equivalence (not just adjunction with comparison map), Theorem H is
exact in $\{0,1,2\}$, the five-archetype dichotomy stabilises, and the
Universal Trace Identity is the equivariant signature.

**Vertical holographic equivalences** to Vols II / III at every level:

| Level | Vol I (Open) | Vol II / III companion |
|---|---|---|
| 0 | factorisation dg-cat on $(X, D, \tau)$ | Vol III: CY-cat via 6d hCS, formal locus + global descent (anomaly **quartic** $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$) |
| 1 | chart $A_b$ | Vol III: $\Phi_d^{\mathrm{FA}}$ at chosen target / vacuum |
| 2 | bar $B(A_b)$ | Vol III: $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ specialisation |
| 3 | derived chiral centre | Vol II: $\mathsf{SC}^{\mathrm{ch,top}}$-brace bulk (Vol II climax) |
| 4 | line / brane operators | Vol III: Drinfeld double $G(X) = D(Y^+(X))$ + descent |
| 5 | modular trace + clutching | Vol III: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$; Vol II: gravity-line completion |

**Master Reconstruction Theorem** (Vol I climax): the Open Beilinson
tower has five levels with reconstruction theorems and hypothesis
packages named, KSDual as $\mathbb{Z}/2$-fixed sublocus, vertical
equivalences to Vols II / III at every level. Theorems A–H are
corollaries. Inscribed in
`chapters/connections/master_reconstruction.tex` and positioned at
the structural climax of Part VI (after the seven-face dictionary,
the frontier chapters, and the cross-volume vertical-equivalence
chapters at levels 0, 2, 4; immediately before `outlook.tex` and
`master_concordance.tex`).

**Manuscript layout** (six-part platonic ideal in `main.tex`):

| # | Part | Beilinson level | Theorem |
|---|------|-----------------|---------|
| I  | Foundations and the Open Beilinson Tower | 0–1 | Morita reconstruction |
| II | The Bar–Cobar Engine                     | 1↔2 | **Theorem A** |
| III| The Bulk                                 | 3   | **Theorems H, B** |
| IV | The Five-Archetype Landscape             | —   | **Theorem C** $5{\times}5$ matrix |
| V  | The Modular Tower                        | 4–5 | **Theorem D** |
| VI | Seven Faces and the Frontier             | —   | **Master Reconstruction** (climax) |

---

## The mathematics

**One object**: the ordered bar complex
$B^{\mathrm{ord}}(A_b) = T^c(s^{-1}\bar A_b)$ on $\overline{M}_{g,n}$
over the relative factorisation stack.

**One relation**: the Arnold relation
$\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki}
+ \eta_{ki} \wedge \eta_{ij} = 0$
on $\mathrm{Conf}_n(X)$ with $\eta_{ij} = d\log(z_i - z_j)$.

**One equation**: the Maurer–Cartan identity
$D \cdot \Theta_{A_b} + \tfrac{1}{2}[\Theta_{A_b}, \Theta_{A_b}] = 0$
in the ordered convolution dGLA.

**One dichotomy**: at chart level, every standard chiral algebra
collapses under averaging into one of five archetypes
**G / L / C / M / B** with shadow-depth
$r_{\max} \in \{2, 3, 4, \infty, 5\}$, and admits a row in the
**5 × 5 $\kappa$-stratification matrix** with measurements
$\{\kappa_{\mathrm{cat}},\ \kappa^{\mathrm{Hodge}}_{\mathrm{ch}},\
\kappa^{\mathrm{Heis}}_{\mathrm{ch}},\ \kappa_{\mathrm{BKM}},\
\kappa_{\mathrm{fiber}}\}$. K3 × E anchors row B at $(0, 0, 3, 5, 24)$.

**Five theorems**, restratified by Beilinson-tower level:

| | Statement | Level | Hypothesis package |
|---|---|---|---|
| **A** | $K^2 \simeq \mathrm{id}$ on $\mathrm{Kosz}(X)$ | 1 ↔ 2 | augmented + complete + finite-dim graded |
| **B** | $\Omega_X(B_X(C)) \xrightarrow{\sim} C$ in $D^{\mathrm{co}}_{\mathrm{ch}}(X)$ | 1 → 3 | Koszul locus |
| **C** | $K^\kappa(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{alg}}(A_b)$ in family-stratum ceiling | 5 (per stratum) | five $\kappa$-measurements per family; collapse pattern; algebra-level Verdier sum, distinct from $\mathcal N(A_b)$ |
| **D** | $\mathrm{obs}_g = \kappa \cdot \lambda_g$ | 4 (on $\overline{M}_{g,n}$) | $H^*(\overline{M}_{g,n})$ class |
| **H** | $\mathrm{ChirHoch}^\bullet \subset \{0,1,2\}$ | 3 | finiteness + completion (Class M needs completed/pro/$J$-adic) |

**Universal chain-homotopy** (load-bearing, connects Theorem A to
Theorem C): $h_{A_b} = h_{\mathrm{LV}} / \mathcal N(A_b)$ where
$\mathcal N(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{LV}}(A_b)$ is the
Verdier-Ran-on-bar norm at level 2 (Convention
`conv:A-two-kappa-shriek` in `theorem_A_infinity_2.tex`). This is
distinct from the algebra-level scalar Verdier sum $K^\kappa(A_b)$
of `master_concordance.tex`; the two coincide only on class B (Mukai
conductor = 8).
Archetype witnesses: $h_G$ trivial; $h_L$ Sugawara $1/(2(k+h^\vee))$
(diverges at critical level); $h_C$ free-field OPE; $h_M$
weight-completed Felder BRST (Zamolodchikov norm $c(5c+22)/10$,
which vanishes — and so $h_M$ diverges — at $c=0$ and $c=-22/5$
Yang–Lee). The Borel-Riccati pole at $c=-218/45$ is a *separate*
singularity (the secondary Borel-resummation pole of the shadow
tower's radius $|\omega|^2 = c^2(5c+22)/[4(45c+218)]$); the
Zamolodchikov norm at $c=-218/45$ evaluates to the finite value
$436/405$, so the chain homotopy is finite there.
$h_B$ Mukai-K3 Heisenberg via Bruinier–Heegner Chern-class reciprocity.

Three volumes: Vol I (this repo, ~2,700pp), Vol II
(`~/chiral-bar-cobar-vol2`, ~1,749pp), Vol III
(`~/calabi-yau-quantum-groups`, ~693pp).

---

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

Every claim is false until verified from primary source. Smaller true
beats larger false. Every numerical claim has **3+ independent
verification paths** (direct computation, alternative formula,
limiting case, symmetry / duality, cross-family, primary literature,
dimensional analysis, numerical evaluation).

**Epistemic hierarchy** (higher wins): direct computation in `compute/`
> `.tex` source ±100 lines > build / tests > primary literature >
`chapters/connections/master_concordance.tex` > this file > memory.

Before every assertion: *"How do I know this — read, computed, or
assumed?"* If assumed, stop and verify.

---

## The master critique discipline

The deepest false pattern is **shadow ≠ object**. Equivalently:
forgetful image ≠ source. Every false idea is a forgetful functor
mistaken for an equivalence; each has a *companion reconstruction
theorem* with named hypothesis package. Never suppress that hypothesis
package.

**Type-signature discipline.** Every theorem carries
(*quadrant, presentation, level, hypothesis package*). Every cross-level
equality invokes a named reconstruction theorem with hypothesis
package. Suppress no hypothesis.

**Master patterns to detect (MA-1 … MA-13).** When any forbidden form
appears, halt the inscription and either replace or quarantine:

| # | Forbidden | Required |
|---|---|---|
| 1 | shadow = object (meta) | every cross-level equality names a reconstruction theorem |
| 2 | $A$ as primitive open object | $A_b = \mathrm{End}_\mathcal{C}(b)$ at chosen vacuum on factorisation dg-cat $\mathcal{C}^{\mathrm{op}}$ |
| 3 | modularity = closed-algebra property | trace + clutching on open category; closed shadow has modular consequences |
| 4 | $\mathrm{Bar}(A) = $ bulk | bar = twisting coalgebra; $Z^{\mathrm{der}}_{\mathrm{ch}}(A) = $ bulk |
| 5 | $E_1$-bar direction explains 2d→3d HT | chiral Deligne–Tamarkin / Swiss-cheese; bar = computational model |
| 6 | five $\kappa$ are one invariant | five $\kappa$-measurements per family; collapse pattern is the classification axis |
| 7 | one-stage $\Phi_d$ | $\Phi_d^{(\Sigma_{d-1}, C)} = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi_d^{\mathrm{FA}}$ |
| 8 | $Y^+(X) = G(X)$ | Drinfeld double after Hall pairing + completion + integral form + descent |
| 9 | 6d hCS = 3d CS in disguise | quartic obstruction $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$, not cubic Casimir |
| 10 | local HT globalises automatically | descent + QME + anomaly + locality required |
| 11 | scalar shadow = operator algebra | $\Delta_5$ = Borcherds denominator; operator-level Pfaffian missing problem |
| 12 | finite-spin / quadratic / classical = full theorem | endpoint hypotheses (Prochazka, CKL, PRS, Yamada, KZ analytic SDR) explicit |
| 13 | ordinary = completed ambient | Class M chain-level requires completed / pro / $J$-adic ambient |

**Forbidden slogans** (a sample; full list with replacements in
`notes/antipatterns_catalogue.md` under MA-1 … MA-13):
*$\mathrm{Bar}(A)$ is the bulk*; *$A$ is the primitive open sector*;
*$\Phi_d: \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ is direct*;
*$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$*;
*$\mathrm{CoHA}(\mathbb{C}^3) = W_{1+\infty}$* (truth:
$= Y^+(\mathfrak{gl}_1)$);
*$\Delta_5$ constructs the BPS Hilbert space*;
*$Z_{\mathrm{BPS}}$ is the gravitational path integral*;
*formal local Hamiltonian BF $\Rightarrow$ compact twisted M-theory background*;
*$W_\infty[\lambda] \Rightarrow E_\infty$ unconditional*;
*PVA Jacobi $\Rightarrow$ all-loop quantum HT theory*.

---

## What counts as progress

A new theorem precisely stated, rigorously proved, with primary-literature-verifiable
proof body. A new $\kappa$-matrix entry by 3+ paths. A falsified claim
repaired. A healed statement with the natural hypothesis named. A
first-principles computation replacing a citation black box (e.g. the
in-place derivation of
$\langle \Lambda | \Lambda \rangle = c(5c+22)/10$
from Virasoro). A reconstruction theorem named with its hypothesis
package. A vertical Open ↔ CY equivalence stated at a previously
unstated level.

**Not progress**: status-table updates, label renames, scope-qualifier
propagation, `FRONTIER.md` retraction sweeps, syncing `AGENTS.md` to
`CLAUDE.md`. Bookkeeping. The hook catches it.

---

## Writing standard: Chriss–Ginzburg north star

Manuscript prose channels the Russian elite school (Gelfand, Manin,
Drinfeld, Arnold, Beilinson, Bernstein, Kapranov, Etingof, Kazhdan,
Kontsevich, Soibelman, Bezrukavnikov) and the mathematical-physics
elite (Polyakov, Nekrasov, Witten, Costello, Gaiotto, Moore, Segal).
**Show don't tell.** Construct mathematics directly; the synthesis of
disparate technical domains brings out the unified structure.

**Forbidden in manuscript prose** (`chapters/`, `frame/`, `examples/`,
`theory/`, `connections/`, `bibliography/`, `appendices/`):

- *Bookkeeping vocabulary* — "Wave N", "round M", "batch K", "DNA
  strand", "AP$n$", "Pattern $n$", "cache entry $n$",
  "CG-rectify pass $k$", "$\mathsf{HZ}$-$n$ inscription". These
  belong in `notes/`, `FRONTIER.md`, commit messages, local
  `memory/` — never in the manuscript.
- *Meta-narration* — "we now turn to", "having established", "let us
  now", "this brings us to", "it is worth noting", "notably",
  "crucially", "remarkably", "furthermore", "moreover", "in the
  present work". Delete every instance; replace with direct
  mathematical statement.
- *Hedging the mathematics earns.* If $X = Y$ is proved, write
  $X = Y$; never "$X$ is closely related to $Y$". Courage, after
  Drinfeld and Polyakov: the equals sign is a theorem.

**Required**:

- Every section title names a mathematical object, construction,
  theorem, or question — never a process or meta-organising device.
- Every definition is preceded within ten lines by the question it
  answers; the reader feels "of course" before the definition arrives.
- Every symbol defined at or before first use, with parenthetical
  first-principles for standard concepts.
- Every physical claim labelled: theorem, heuristic, or metaphor.
  When a physical identification can be a theorem, state it as one;
  do not hide content as an "analogy".
- Economy. A paragraph that can be one sentence is one sentence.
- At every section boundary, three sentences of mathematics: what was
  just established, the question the next section resolves, the
  construction that resolves it.

The reader is an equal who sees the force of the argument when stated
with sufficient precision. The prose **is** mathematics, not
commentary on mathematics. Existing prose with bookkeeping vocabulary
is rectified through `/chriss-ginzburg-rectify`; new prose is in the
CG voice from the first keystroke.

---

## The manuscript is self-complete, self-coherent, self-consistent

Current version stands for itself. No references to previous versions,
intermediate ansätze, retracted values, superseded formulas, or
drafting-history commentary. If a formula was $X$ and is now $Y$, the
manuscript says $Y$; not "$Y$ (previously $X$)".

When a retraction is genuinely informative — a proof attempt whose
failure illuminates why the successful proof is forced — state the
failed argument and its flaw as mathematics: *"$[m_k, B^{(2)}] = 0$
fails per-$k$ because cyclic invariance controls adjacent contractions
but not non-adjacent terms (Proposition X)"*. Not "the author
initially attempted X". The mathematics is the Gap / Flaw, not the
drafting record.

---

## Chain-level and $(\infty,1)$-categorical: equal status

Both **chain-level** mathematics (explicit complexes, named
differentials, witnessed homotopies, $L_\infty$, Mittag–Leffler
towers, ambient-qualified statements) and **$(\infty,1)$-categorical**
mathematics (derived $\infty$-stable categories, Lurie HA,
factorisation $\infty$-categories, $\infty$-operads à la
Costello–Gwilliam, Francis–Gaitsgory) are **equally load-bearing**.
Neither replaces the other.

State each theorem in the lane its proof works. Chain-level: name the
chain homotopy / Mittag–Leffler tower / explicit MC element / OPE
pole. $(\infty,1)$-categorical: name the $(\infty,1)$-functor /
adjunction / colimit. If both lanes needed, state both,
ambient-qualified. Never write "this is just the chain-level /
$(\infty,1)$-shadow of the real theorem": both shadows are real, both
are the theorem viewed through different lenses.

---

## How to work

**Formulas come from `chapters/examples/landscape_census.tex` or a
primary paper** — never from memory. If absent there, write it there
first with primary-literature citation, then use it.

**Proofs are inscribed in chapters, not notes.** A proof in `notes/` or
a swarm log is a draft. Move it into `chapters/**.tex` with
`\label{thm:...}` and a `\begin{proof}...\end{proof}` body.

**After every inscription**, the PostToolUse hook
(`.claude/hooks/beilinson-gate.sh`) sweeps for anti-pattern signatures
and cached confusion patterns. Read its output; address what it flags;
return to the mathematics. False positive — note scope inline and
move on.

**Builds happen at session end only**, when the user asks:

```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast     # Vol I
cd ~/chiral-bar-cobar-vol2 && make                        # Vol II
cd ~/calabi-yau-quantum-groups && make fast               # Vol III
```

**Tests** — the test file for the module edited. `make test` (~1 min)
or `make test-full` (~119K tests) are last resorts.

**Compute engine** — `compute/` is the immune system. New $\kappa$ /
shadow-tower / 5×5 matrix entry inscribed → 3-path verification test
alongside.

**Validation gates** (sharpening scope, not every edit):
`make integrity`, `make audit`, `make verify-independence`,
`make verify`, `make census`.

---

## Operational discipline

**Autonomy.** Operate fully autonomously. No permission prompts during
research-grade work. Destructive git is forbidden; everything else
proceeds.

**Git and authorship.** All commits authored by **Raeez Lorgat**.
**Never** any AI attribution — no `Claude`, no `Anthropic`, no
`Co-Authored-By`, no `Generated with`, no 🤖 in commits, comments,
docstrings, or manuscripts. Pre-commit hook nudges; if it fires,
remove offending content, do not paper over. **No `git stash`**
(use `git diff > patch.diff && git apply`). **No amend without
explicit instruction.** **No `git checkout / restore / reset` to
clobber files. No force-push.**

**Branch / worktree reconciliation — DEEP SEMANTIC MERGES ONLY.**
Read both sides in full; merge at the semantic level — pick the
stronger statement, the tighter citation, the more rigorous proof.
Work loss here is irrecoverable.

**LaTeX hygiene.** Macros in `main.tex` preamble. In chapters, use
`\providecommand`, never `\newcommand`. Compiles with `memoir` + EB
Garamond. Claim-status tags
(`\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`,
`\ClaimStatusConjectured`, `\ClaimStatusHeuristic`) are bookkeeping,
not repairs. When uncertain, name the proof obligation and heal — do
not downgrade.

**Multi-tool concurrency.** Independent tool calls go in parallel.

**Long-form proof harness.** A 30–60 minute agent run is acceptable
when a proof obligation requires it. Load context first; build
internal outline; work through independent proof routes (worked
example, formal argument, primary source, computation, cross-volume
consistency). Attack-heal loop: strongest counterexample, sign /
convention, ambient category, missing hypothesis, false functoriality,
unproved equivalence, numerical constant. Heal and attack until the
theorem closes or the exact obstruction is named. Do not downgrade to
close. **Subagents provide evidence, not authority.**

---

## Memory system

Persistent file-based memory at
`/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/`.
Types: **user** (role, knowledge), **feedback** (corrections +
confirmations with *Why* and *How to apply*), **project**
(in-progress decisions; absolute dates), **reference** (external
pointers). Index in `MEMORY.md` (one-line entries ≤150 chars).

**Memory is point-in-time.** Verify against current state before
acting; if memory and current state disagree, trust the current state
and update / remove the stale memory. For implementation alignment
within a conversation, use a *plan*; for step tracking, use *tasks*.
Memory is for cross-conversation context only.

---

## Essential constants

- $\kappa(V_k(\mathfrak{g})) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$ (affine KM, trace form).
- $\kappa(\mathrm{Vir}_c) = c/2$. $\kappa(\mathcal{H}_k) = k$. $\kappa(\mathcal{W}_N) = c(H_N - 1)$, $H_N = \sum_{j=1}^N 1/j$.
- Virasoro shadow: $S_2 = c/2$, $S_3 = 2$, $S_4 = 10/[c(5c+22)]$, $S_5 = -48/[c^2(5c+22)]$, $S_6 = 80(45c+193)/[3c^3(5c+22)^2]$. Borel radius $|\omega|^2(c) = c^2(5c+22) / [4(45c+218)]$, Stokes pole $c_S = -218/45$.
- Zamolodchikov norm: $\langle\Lambda|\Lambda\rangle = c(5c+22)/10$ for $\Lambda = {:}TT{:} - (3/10)\partial^2 T$.
- $r$-matrix (level prefix MANDATORY): $r^{KM}(z) = k\,\Omega/z$; $r^{\mathrm{Heis}}(z) = k/z$; $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$.
- Universal Borcherds-weight identity: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for $N \in \{1, 2, 3, 4, 6\}$ + half / quarter-integer continuations.
- Universal chain-homotopy: $h_{A_b} = h_{\mathrm{LV}} / \mathcal N(A_b)$ where $\mathcal N(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{LV}}(A_b)$ is the Verdier-Ran-on-bar norm (level 2). Witness values: $\mathcal N(\mathsf G)=1$, $\mathcal N(\mathsf L)=2(k+h^\vee)$, $\mathcal N(\mathsf C)=1$, $\mathcal N(\mathsf M)=c(5c+22)/10$, $\mathcal N(\mathsf B)=8$. Distinct from the algebra-level scalar Verdier sum $K^\kappa(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{alg}}(A_b)$ of `master_concordance.tex` (which gives $0$ for $\mathsf G,\mathsf L,\mathsf C$ and $13$ for $\mathsf M$).
- Desuspension: $|s^{-1}v| = |v| - 1$; cohomological grading $|d| = +1$.
- Bar: $B(A_b) = T^c(s^{-1}\bar A_b)$, $\bar A_b = \ker \epsilon$.

**Five objects, never conflate**:
$A_b$ (chart algebra) — $B(A_b)$ (bar coalgebra) —
$A_b^{i} = H^\star B(A_b)$ (cohomology coalgebra) —
$A_b^{!}$ (Verdier dual) —
$Z^{\mathrm{der}}_{\mathrm{ch}}(A_b)$ (derived centre = bulk).
$\Omega(B(A_b)) = A_b$ is **inversion**, not Koszul duality.
$A_b^{!}$ via **Verdier**. Bulk via **Hochschild** cochains.

---

## Where the bookkeeping lives

- `chapters/connections/master_concordance.tex` — repo constitution.
- `chapters/examples/landscape_census.tex` — canonical formulas.
- `notes/antipatterns_catalogue.md` — AP register + MA-1 … MA-13.
- `notes/cross_volume_aps.md` — cross-volume AP reference.
- `notes/first_principles_cache_comprehensive.md` — confusion-pattern
  registry; hook auto-checks top-15, grep the rest.
- `appendices/first_principles_cache.md` — cache tip in manuscript.
- Volume-specific `CLAUDE.md` in `~/chiral-bar-cobar-vol2`,
  `~/calabi-yau-quantum-groups`. Vol III carries the canonical CY$_d$
  $\kappa$-table (`cy_d_kappa_stratification.tex`) and the two-stage
  functor chapter (`cy_to_chiral.tex`).
- `FRONTIER.md`, `AGENTS.md`, `adversarial_swarm_*/`, `memory/` —
  *working notebooks*. Primary wins on conflict.

---

## Ambient hooks (automatic)

- `PreToolUse(Agent)` → `cache-injection.sh` prepends the
  first-principles preamble to every Agent call.
- `PreToolUse(Bash, git commit)` → pre-commit reminder: no AI
  attribution, Raeez Lorgat only.
- `PostToolUse(Edit|Write)` → `beilinson-gate.sh` scans for AP
  signatures, master patterns MA-1 … MA-13, top-15 cache patterns,
  cross-volume formula propagation. Output as `additionalContext` in
  next tool result.
- `Stop` → `convergence-gate.sh` session-end summary.

The hook is advisory. False positives — scope inline, move on.

---

## What not to do

1. Do not invent formulas from memory — consult
   `landscape_census.tex` or primary literature.
2. Do not propagate status-label wording across 10 files when
   mathematics is waiting.
3. Do not run `make fast` after every edit.
4. Do not read `notes/claude_md_legacy_*.md` or
   `notes/first_principles_cache_comprehensive.md` whole — grep them.
5. Do not build on a new theorem without auditing its proof.
   The Beilinson cascade is a real failure mode.
6. Do not defend prior output by sampling files and citing AP
   discipline. When the user says content is wrong, believe the user.
   Self-audit of one's own mathematics is negative yield.
7. Do not treat old throughput cautions as a prohibition on swarms.
   User-authorised large swarms are allowed.
8. Do not confuse this file with a configuration manual. This is a
   mathematician's working manifesto.

---

## The permanent rule

> Every theorem statement carries a type signature
> (*quadrant, presentation, level, hypothesis package*).
> Every cross-level equality invokes a named reconstruction theorem
> with explicit hypothesis package.
> KSDual is the $\mathbb{Z}/2$-fixed sublocus where the four-quadrant
> grid degenerates into self-dual form.
> Cells admitting holographic vertical equivalence carry both Open- and
> CY-quadrant statements, with the equivalence theorem named.
>
> **Primitive objects first, shadows second, scalar modular forms last.**

---

## Code-writing discipline — repo application

Per `~/ecosystem/INVARIANTS.md §XIII`. Twelve rules instantiated for chiral-bar-cobar Vol I (Open Beilinson tower; Theorems A, B, C, D, H; Master Reconstruction Theorem; `raeez-math-template` consumer):

1. **Think Before Coding.** Every theorem / lemma edit names the affected proof obligation, the *(quadrant, presentation, level, hypothesis package)* type signature, and the claim-status macro. Every new term passes the four-part coining test (`MATHEMATICAL_PHYSICS_*_WRITING_STANDARDS.md §III`).
2. **Simplicity First.** No speculative theorems; statements earn proof obligations. Theorems A–H plus the Master Reconstruction are the canonical landmarks; auxiliary lemmas serve them.
3. **Surgical Changes.** An edit in one chapter does not touch the bibliography or sibling chapters unless propagation requires. Bar–cobar engine is its own chapter — do not bleed into the bulk. Do not propagate status-label wording across 10 files when mathematics is waiting.
4. **Goal-Driven Execution.** Success = `pdflatex main.tex` clean, theorem ledger consistent, voice-scan + four-part term-coining test pass, claim-status macros honest, `raeez-math-template.sty` symlink intact (`make check` in `~/latex-template`), Beilinson gate clean. Build at session-end only.
5. **Use the model only for judgment calls.** Cross-reference resolution is deterministic per `\label`/`\ref`; theorem-numbering is deterministic per LaTeX. The model drafts proofs and chooses examples; it does not invent term names without the four-part test or coefficients without `landscape_census.tex` / primary literature.
6. **Token budgets are not advisory.** Monograph-scale; checkpoint between chapters and between Beilinson-tower levels (0–5). For long-form proof harness sessions, load context first, build internal outline, do not paginate.
7. **Surface conflicts, don't average them.** Canonical theorem statement wins over inline commentary. Master Reconstruction Theorem (climax) wins over earlier formulations. A computation in `compute/` or `landscape_census.tex` wins over prose claims — never overwrite from memory.
8. **Read before you write.** Read the affected theorem and its hypothesis package. Read the cross-volume companion section (Vol II / III) before editing a vertical-equivalence chapter. Grep legacy `notes/claude_md_legacy_*.md` and `notes/first_principles_cache_comprehensive.md` — never read whole.
9. **Tests verify intent.** Claim-status macros (`\ClaimStatusProvedHere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusRetracted`) are the load-bearing test. A theorem labelled `proved` with a proof gap is broken. Four-part term-coining test is non-vacuous.
10. **Checkpoint after every significant step.** Between chapters, summarize theorem-ledger delta and cross-volume equivalence impact. Between Beilinson-tower levels, restate reconstruction-theorem status. Subagents return evidence, not authority; main thread integrates via deep semantic merge.
11. **Match the codebase's conventions, even if you disagree.** `raeez-math-template.sty` symlinked at repo root, loaded immediately after `\documentclass`, `\mainpreambleonly` guard preserved (`INVARIANTS.md §XII`). Theorem environments per template. No local typography forks.
12. **Fail loud.** Announce every broken cross-ref, dangling theorem, unhealed conjecture label (`INVARIANTS.md §XI`). Never demote Theorem A to motivation; heal it. Never silently overwrite a computation from memory. Cross-volume / compute-vs-prose disagreements stop and report.
