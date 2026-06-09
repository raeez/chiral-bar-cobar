# MANUSCRIPT RECONSTITUTION KICKSTART

> Self-contained launch protocol. Pastes into a clean Claude Code or
> Codex session at the repository root and orchestrates a max-parallel
> swarm to reconstitute Vol I into its platonic-ideal form. All agents
> respect the writing and voice standards documented on disk.

---

## Role of the receiving thread

You are the **integration owner** for the Vol I reconstitution
swarm. Your job is to (a) verify the load context is current,
(b) dispatch the Wave-1 cluster of agents in maximum parallelism,
(c) integrate their reports by deep semantic merge into the
manuscript, (d) launch Wave-2 follow-up agents on the items Wave-1
opens.

You do not decide truth alone. Subagents provide evidence; the
manuscript decides. When a subagent's report disagrees with primary
literature or `chapters/examples/landscape_census.tex`, the source
wins and the disagreement is itself the deliverable.

---

## Load order (read in full, in this order, before dispatching agents)

1. `~/ecosystem/INVARIANTS.md` — voice and ecosystem invariants.
2. `./CLAUDE.md` — platonic-ideal architecture, master critique
   discipline (MA-1 … MA-13), writing standard, essential constants,
   operational rules.
3. `./AGENTS.md` — research-grade harness (`reasoning_effort=xhigh`,
   long-form proof harness, self-reflection rubric).
4. `./FRONTIER.md` — proved core, open frontiers F1 … F12, vertical
   equivalences, the 5×5 $\kappa$-stratification matrix, the seven
   faces of $r(z)$.
5. `./README.md` — programme orientation, structure, build commands.
6. `chapters/connections/master_concordance.tex` — repo constitution.
7. `chapters/examples/landscape_census.tex` — canonical formulas
   per family (the source of truth for every $\kappa$, every $r(z)$,
   every shadow-tower entry).
8. `notes/antipatterns_catalogue.md` — AP register, hook-checked
   signatures, and (after Cluster A3 lands) MA-1 … MA-13.

Do not re-read files already in context. Use parallel `Read` /
`Grep` calls for the seven files above before any agent is dispatched.

---

## Target — Vol I platonic ideal

Vol I is the **Open quadrant** of the four-quadrant programme: the
complete five-level **Beilinson tower** on a tangential log curve
$(X, D, \tau)$,
$\mathcal{C}^{\mathrm{op}} \rightsquigarrow A_b \rightsquigarrow B(A_b)
\rightsquigarrow Z^{\mathrm{der}}_{\mathrm{ch}}(A_b) \rightsquigarrow
\text{ops} \rightsquigarrow \text{scalar}$,
with reconstruction theorems and named hypothesis packages at every
level. **KSDual** is the $\mathbb{Z}/2$-fixed sublocus under chiral /
antichiral involution $A \mapsto A^!$. **Vertical holographic
equivalences** to Vols II / III at every level. The **Master
Reconstruction Theorem** is the structural climax; Theorems A, B, C,
D, H are corollaries restratified by tower level. The five archetypes
G / L / C / M / B sit in a **5×5 $\kappa$-stratification matrix**
with K3 × E anchoring row B at $(0, 0, 3, 5, 24)$.

The reconstitution is a *type-signature pass + master-critique
discipline pass + matrix construction + vertical-equivalence
inscription*, executed in parallel across the manuscript with the
seven structural elements
$(X, D, \tau;\ \mathcal{C}^{\mathrm{op}},\ b,\ A_b,\
Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{C}),\ \Theta_\mathcal{C},\
\mathrm{Tr}_\mathcal{C})$
replacing the prior "$A$ as primitive" framing.

---

## Disciplines (apply to every agent, every inscription)

1. **Type signature on every theorem.** Every theorem statement
   carries (*quadrant, presentation, level, hypothesis package*).
   Every cross-level equality invokes a named reconstruction theorem
   with hypothesis package. Suppress no hypothesis.
2. **Master critique discipline (MA-1 … MA-13).** Halt the inscription
   on any forbidden form (shadow=object, $A$ as primitive, $\mathrm{Bar}=$bulk,
   modularity = closed property, five $\kappa$ are one, one-stage
   $\Phi_d$, $Y^+ = G(X)$, 6d hCS = 3d CS, local HT globalises,
   scalar = operator, finite-spin = full theorem, ordinary = completed
   ambient). Replace per the table in `CLAUDE.md`.
3. **Chriss–Ginzburg voice.** No bookkeeping vocabulary in manuscript
   prose ("Wave N", "Pattern n", "AP$n$", "HZ-$n$"). No meta-narration
   ("we now turn to", "having established", "notably", "remarkably").
   No hedging ("$X$ is closely related to $Y$"; if proved, write
   $X = Y$). Every section title names a mathematical object.
   Every definition preceded by the question it answers.
4. **Self-completeness.** No references to previous versions, retracted
   values, drafting-history commentary. Mathematics is the Gap / Flaw,
   not the drafting record.
5. **No destructive git.** No `git stash`, `git reset --hard`,
   `git checkout / restore`, `--no-verify`, `--amend` without explicit
   instruction, no force-push. Branch / worktree reconciliation: deep
   semantic merge only.
6. **Three-path verification.** Every numerical claim verified by 3+
   independent paths (direct computation, alternative formula, limiting
   case, symmetry / duality, cross-family, primary literature,
   dimensional analysis, numerical evaluation).
7. **No AI attribution.** Commits by Raeez Lorgat. No `Claude`,
   `Anthropic`, `Co-Authored-By`, `Generated with`, 🤖 anywhere.
8. **Subagents provide evidence, not authority.** Main thread
   integrates by deep semantic merge.

---

## Wave 1 — dispatch all clusters in parallel

In a single message, dispatch the five clusters below using the Agent
tool with multiple concurrent calls. Use `subagent_type=general-purpose`
unless otherwise specified. Each agent receives the per-cluster prompt
template, with variables filled per agent's slot.

### Cluster A — Constitutional (4 agents, parallel)

Inscribes the Vol 0 / constitution layer. Each agent writes a single
new file or updates a single existing file.

- **A1 — Master Reconstruction Theorem chapter.**
  Write `chapters/connections/master_reconstruction.tex` (~15pp).
  Inscribe: the five-level Beilinson tower with the seven structural
  elements; reconstruction theorems Morita / Theorem A / Theorem H /
  Drinfeld-double / modular-trace at each step, each with named
  hypothesis package; KSDual as $\mathbb{Z}/2$-fixed sublocus under
  chiral / antichiral involution; vertical equivalences to Vols II /
  III at every level; Theorems A, B, C, D, H as corollaries. State
  Master Reconstruction as a structural meta-theorem (Bourbaki-structure
  level), not a scalar identity. Register in `main.tex` immediately
  before Part VI. Cite `CLAUDE.md` §"The platonic ideal architecture"
  for the spec.

- **A2 — Type System Appendix.**
  Write `appendices/type_system.tex` (~7pp). Define formally: levels
  0–5 (primitive, chart, twisting, bulk, operator, scalar); quadrant
  tags (Open / CY); presentation tags (Cat / Chain); hypothesis-package
  primitives; composition rules. Provide the Hypothesis-Package
  Lattice as a labelled figure: nodes are reconstruction theorems,
  edges are package containment. Register in `main.tex` appendix
  block.

- **A3 — Master patterns inscription.**
  Update `notes/antipatterns_catalogue.md` with **MA-1 through MA-13**
  plus the meta pattern AP-META-shadow-equals-object. Each MA entry:
  forbidden form, *Why* (the false-equality structure), *How to
  apply* (detection signature for the hook), companion reconstruction
  theorem, hypothesis package. Append at the end of the existing AP
  register (do not overwrite). Provide a brief detection regex per MA
  for the `beilinson-gate.sh` hook to consume.

- **A4 — Concordance update.**
  Update `chapters/connections/master_concordance.tex` with the
  type-signature discipline as constitution-level rule:
  *"every theorem statement carries (quadrant, presentation, level,
  hypothesis package); every cross-level equality invokes a named
  reconstruction theorem; KSDual is the $\mathbb{Z}/2$-fixed sublocus."*
  Plus: pin the seven structural elements as primitive datum.
  Insert near the existing constitutional rules block, do not move
  the existing constitution.

### Cluster B — Vol I chapter sweep (13 agents, parallel)

Each agent owns one chapter file. Action per file: type-signature
pass + master-critique discipline pass + replace forbidden slogans
per MA-1 … MA-13 + restratify cross-volume references with explicit
$(\Sigma_{d-1}, C)$ indices where Vol III content is invoked.

| Agent | Target file | Primary work |
|---|---|---|
| B1 | `chapters/connections/holographic_datum_master.tex` | Replace "$A$ as primitive open sector" with $(\mathcal{C}^{\mathrm{op}}, b, A_b)$; install seven structural elements |
| B2 | `chapters/connections/holographic_codes_koszul.tex` | "bar = bulk" → "bar = twisting; $Z^{\mathrm{der}}_{\mathrm{ch}}$ = bulk" everywhere |
| B3 | `chapters/connections/entanglement_modular_koszul.tex` | Same MA-4 sweep + entanglement-from-$\kappa$ scope |
| B4 | `chapters/connections/feynman_connection.tex` + `feynman_diagrams.tex` | bar-only uplift explanation → chiral Deligne–Tamarkin / Swiss-cheese (MA-5) |
| B5 | `chapters/connections/genus1_seven_faces.tex` + `genus_complete.tex` + `poincare_computations.tex` | Modularity = trace + clutching (MA-3) |
| B6 | `chapters/connections/frontier_modular_holography_platonic.tex` + `subregular_hook_frontier.tex` + `semistrict_modular_higher_spin_w3.tex` | Modularity reframing + KSDual scope |
| B7 | `chapters/examples/landscape_census.tex` | 5×5 $\kappa$-matrix table per family; explicit $(\Sigma_{d-1}, C)$ indexing on every CY-derived shadow; delete additive $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ |
| B8 | `chapters/examples/chiral_moonshine_unified.tex` + `exceptional_yangian_koszul_duality_platonic.tex` + `bershadsky_polyakov.tex` | Five-stratum $\kappa$ tagging; Vol III shadow with $(\Sigma_{d-1}, C)$ |
| B9 | `chapters/examples/kac_moody.tex` + `heisenberg_eisenstein.tex` + `beta_gamma.tex` + `free_fields.tex` | Archetype-specific chart-class enumeration; Theorem A four-lane discipline |
| B10 | `chapters/connections/bv_brst.tex` | Ghost-trace UTI as scope-alignment; quartic 6d hCS obstruction (MA-9) |
| B11 | `chapters/connections/thqg_*.tex` (intro_supplement + open_closed + entanglement_programme) | Replace "Universal Holography constructs 3d gravity" with algebraic-sector identification (MA-11); BTZ / Cardy hypotheses inscribed inline |
| B12 | `chapters/theory/theorem_A_infinity_2.tex` | Theorem A in parametric strength: weak (always-adjunction) / strong (Koszul-locus equivalence) / strongest (rejected, replaced by Theorem H); Priddy / Positselski lane split |
| B13 | `appendices/_sl2_yangian_insert.tex` + `appendices/ordered_associative_chiral_kd.tex` + `appendices/koszul_reference.tex` + `appendices/dual_methodology.tex` | Gui–Li–Zeng quadratic duality scoped to "candidate dual + MC comparison map"; full Koszulness named as separate theorem |

### Cluster C — 5×5 $\kappa$-matrix (5 agents, parallel)

Each agent owns one row of the matrix and computes five $\kappa$
measurements with three independent verification paths each.

| Agent | Archetype | Row | Deliverable |
|---|---|---|---|
| C-G | Heisenberg $\mathcal{H}_k$ | row G | $\{\kappa_{\mathrm{cat}}, \kappa^{\mathrm{Hodge}}_{\mathrm{ch}}, \kappa^{\mathrm{Heis}}_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\}$ for $\mathcal{H}_k$; collapse pattern; chart-class enumeration |
| C-L | $V_k(\mathfrak{g})$ | row L | Same five entries; Sugawara / Freudenthal-shift discipline (CLAUDE.md essential constants) |
| C-C | $\beta\gamma(\lambda)$ | row C | Same; $\lambda$-family stratification |
| C-M | $\mathrm{Vir}_c$, $\mathcal{W}_N$ | row M | Same; $|\omega|^2(c)$ Borel-radius closed form $c^2(5c+22)/[4(45c+218)]$; Stokes pole $c_S = -218/45$ |
| C-B | Mukai-K3 Heisenberg | row B | $(0, 0, 3, 5, 24)$ at K3 × E; universal Borcherds-weight $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for $N \in \{1,2,3,4,6\}$ + half / quarter-integer continuations |

Each agent:
- Computes the five entries from `compute/` engines or first principles.
- Verifies each entry by 3+ paths (direct computation, primary
  literature, limiting case, symmetry, cross-family).
- Writes `compute/tests/test_kappa_stratification_<ROW>.py`.
- Reports the row entries plus collapse pattern (which entries
  coincide), plus three independent verification paths per entry.

### Cluster D — Standalone papers (4 agents, parallel)

The standalone papers most affected by the master critique:

- **D-A — Paper A (Five Theorems).** Update theorem statements to
  type-signature form (level, hypothesis package). Restate Theorem C
  as 5×5 matrix with K3 × E row B = $(0, 0, 3, 5, 24)$. Restate
  Theorem A in parametric strength.
- **D-C — Paper C ($E_1$ primacy).** Reframe bar direction as
  computational model, not 2d→3d HT explanation; chiral Deligne–Tamarkin
  / Swiss-cheese as the explanatory mechanism (MA-5).
- **D-M — Paper M.** Retitle to "Algebraic Holographic HT Sector with
  Virasoro Boundary and Derived Chiral Centre Bulk". Abstract and
  introduction rewritten to identify the algebraic sector, not
  "construct 3d quantum gravity"; BTZ / Cardy hypotheses listed
  inline.
- **D-N — Paper N (Igusa cusp / $\Delta_5$).** Frame deliverable as
  virtual $K_0$-determinant + Borcherds denominator; operator-level
  Pfaffian construction explicitly listed as F11 open frontier.

### Cluster E — Vertical equivalences (3 agents, parallel)

New theorem statements pinning the cross-volume vertical equivalences.

- **E-V0 — Vertical-0 (level-0 holographic equivalence).** Inscribe
  the level-0 vertical: factorisation dg-cat $\mathcal{C}^{\mathrm{op}}$
  ↔ CY-cat via 6d hCS, formal locus + global descent; quartic anomaly
  $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$ explicit. Target file:
  new section in `chapters/connections/frontier_modular_holography_platonic.tex`
  (Vol I cross-volume statement); cross-reference to Vol III's
  `chapters/theory/cy_to_chiral.tex` for the CY-side.
- **E-V2 — Vertical-2 (bar / specialisation comparison).** Inscribe
  the level-2 vertical: $B(A_b)$ ↔ $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$
  specialisation. Target: new appendix
  `appendices/vertical_equivalence_level_2.tex` or new section in
  `appendices/ordered_associative_chiral_kd.tex`.
- **E-V4 — Vertical-4 (Drinfeld double via $Y^+(X)$ + descent).**
  Inscribe the level-4 vertical: line operators ↔ Drinfeld double
  $G(X) = D(Y^+(X))$ with Hall pairing + completion + integral form +
  stable-envelope transport + descent (MA-8). Target: new section in
  `chapters/connections/holographic_datum_master.tex`; cross-reference
  to Vol III's CoHA / quantum group chapter.

---

## Per-agent prompt template

Every agent receives:

```
You are agent <ID> in the Vol I reconstitution swarm. Your scope is
<TARGET>. Your deliverable is <DELIVERABLE>.

REQUIRED CONTEXT (read in full before any inscription):
1. /Users/raeez/chiral-bar-cobar/CLAUDE.md
2. /Users/raeez/chiral-bar-cobar/AGENTS.md
3. /Users/raeez/chiral-bar-cobar/FRONTIER.md
4. /Users/raeez/chiral-bar-cobar/chapters/connections/master_concordance.tex
5. /Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex
6. The TARGET file(s) listed in your scope.
7. Any cross-volume anchors named in CLAUDE.md vertical-equivalences
   table that touch your scope.

DISCIPLINE:
- Type signature on every theorem (quadrant, presentation, level,
  hypothesis package).
- Master critique master patterns MA-1 … MA-13 (CLAUDE.md table).
- Chriss–Ginzburg voice (no bookkeeping vocabulary, no meta-narration,
  no hedging the mathematics).
- Self-completeness (no references to previous versions, retractions,
  drafting history).
- No destructive git.
- 3+ independent verification paths on every numerical claim.
- No AI attribution.

DELIVERABLE FORMAT:
- Files changed (path + brief summary per file).
- Theorems / propositions / lemmas / definitions inscribed (label +
  one-line statement + level signature + hypothesis package).
- Numerical claims verified (claim + 3 paths).
- Open obligations named (precise statement of what would close them).
- Cross-volume references made explicit.
- Compact report under 800 words.

FORBIDDEN:
- Inventing formulas from memory; consult landscape_census.tex or
  primary literature.
- Inscribing without naming hypothesis package.
- Using bookkeeping vocabulary in manuscript prose.
- Reverting work you did not make.
- Voting truth into existence; if uncertain, name the obligation
  precisely.

ATTACK-HEAL DISCIPLINE:
After every proposed inscription, attack the strongest failure mode:
convention/sign, ambient category, missing hypothesis, false
functoriality, unproved equivalence, numerical constant. Heal and
attack again until the inscription closes or the exact obstruction is
named.
```

---

## Convergence criteria per cluster

- **Cluster A** converges when all four constitutional artifacts are
  inscribed and `make integrity` passes on the new chapter / appendix
  / catalogue entries.
- **Cluster B** converges when each chapter file passes the
  `beilinson-gate.sh` master-pattern detection (no MA-1 … MA-13
  signatures triggered) and every theorem in the file carries a type
  signature.
- **Cluster C** converges when the 5×5 matrix is fully populated, every
  entry has 3 verification paths logged in `compute/tests/`, and the
  collapse pattern per row is named.
- **Cluster D** converges when each paper's abstract, introduction,
  and theorem statements are restratified per the master critique;
  Paper M is retitled.
- **Cluster E** converges when each new vertical-equivalence section
  is inscribed with its hypothesis package and the cross-volume
  reference resolves.

---

## Reporting (every agent, on completion)

```
AGENT <ID> REPORT
=================
Scope: <one-line>
Files changed: <list>
Inscriptions: <theorems / propositions / lemmas with labels>
Numerical claims verified: <claim + 3 paths each>
Open obligations: <precise statements>
Cross-volume references: <made explicit>
Discipline check: PASS / FAIL on each of (type signature, MA-1..MA-13,
   CG voice, self-completeness, no destructive git, 3-path verification)
Time: <elapsed>
```

The integration owner reads every report; integrates into the
manuscript by deep semantic merge; flags conflicts for Wave-2
follow-up.

---

## Integration owner (main thread) workflow

After dispatching Wave 1 with all 29 agents in parallel
(4 + 13 + 5 + 4 + 3):

1. Wait for reports. Each agent runs 30–60 minutes typically.
2. As reports arrive, integrate by deep semantic merge:
   - Verify the agent's discipline-check claims.
   - Run `make verify` (anti-pattern scan) on the modified files.
   - Run `make audit` on the relevant chapters if theorem-level work.
   - Run targeted tests for `compute/` changes.
   - Resolve any conflicts between cluster outputs (e.g., Cluster A's
     concordance update vs Cluster B's chapter-level changes that
     reference the new constitution).
3. Surface any open obligations to the user as candidates for Wave 2.
4. After all Wave 1 agents return, run a session-end build of Vol I
   with `make fast` (only when asked) and post a synthesis report.

---

## Wave 2 — dispatched after Wave 1 reports integrate

Wave 2 is conditional on Wave 1 outputs and is dispatched by the
integration owner. Likely Wave 2 clusters:

- **F — Compute-engine extension.** Build
  `compute/lib/kappa_stratification.py` with verified entries from
  Cluster C; build `compute/tests/test_master_reconstruction.py`
  exercising the Master Reconstruction Theorem corollaries.
- **G — Cross-repo bridge sweeps.** Update Vol II's `CLAUDE.md` and
  Vol III's `CLAUDE.md` to mirror the platonic-ideal architecture;
  inscribe vertical-equivalence cross-references in the companion
  volumes.
- **H — Standalone-paper second wave.** Update Papers B, E, F, K, L
  for the master critique implications; build the dependency DAG
  inscription.
- **I — Open-frontier sharpening.** For each F1 … F12, inscribe the
  hypothesis package and heal path explicitly in `FRONTIER.md` if not
  already there; for F8 (chart-class enumeration), launch the
  archetype-by-archetype enumeration sweep.

Wave 3+ is dispatched as Wave 2 surfaces further obligations.

---

## Launch sequence (one tool message)

In a single message, dispatch all 29 Wave-1 agents using the Agent
tool with concurrent tool calls. The dispatch message should contain:

- 4 calls for Cluster A (one per A1–A4),
- 13 calls for Cluster B (one per B1–B13),
- 5 calls for Cluster C (one per archetype),
- 4 calls for Cluster D (one per priority paper),
- 3 calls for Cluster E (one per vertical level).

Each call's `prompt` field is the per-agent template above with
`<ID>`, `<TARGET>`, `<DELIVERABLE>` filled in from the cluster
specifications. `description` is 3–5 words.
`subagent_type=general-purpose` for all (or `Explore` for any
read-only diagnostic agents added later).

The integration owner does not write to the manuscript directly while
agents are running; it only integrates after reports arrive.

---

## Safety net

- If any agent reports a discipline-check FAIL, do not integrate that
  agent's output. Re-dispatch with sharpened scope.
- If two agents' outputs conflict on the same file, deep-semantic-merge
  by selecting the stronger statement / tighter citation / more
  rigorous proof — never `git reset --hard` or `git checkout --` to
  resolve.
- If the user interrupts mid-swarm, the integration owner reports
  which agents have returned and which are still running; integration
  proceeds on returned agents only.
- If a Wave-1 agent surfaces a load-bearing retraction (a previously
  proved theorem now falsified by the master critique), the
  integration owner halts dispatch on dependent agents until the
  retraction is integrated and a healed statement is inscribed.

---

## End state of Wave 1 (target)

- The Master Reconstruction Theorem chapter is inscribed.
- The Type System Appendix is inscribed.
- MA-1 … MA-13 are in `notes/antipatterns_catalogue.md` and consumed
  by the hook.
- 13 chapter files have type-signature passes complete.
- The 5×5 $\kappa$-stratification matrix is populated and verified.
- Papers A, C, M, N have updated abstracts and theorem statements.
- Three new vertical-equivalence sections are inscribed.
- The manuscript compiles cleanly (`make fast`).
- A Wave-2 dispatch list is queued.

The platonic ideal is asymptotic; Wave 1 closes the largest gap. The
quiet music begins when Vol I's prose and theorem statements first
stop disagreeing with their own architecture.
