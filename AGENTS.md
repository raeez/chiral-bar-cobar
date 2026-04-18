# AGENTS.md -- Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,700pp, 139,568 tests, 3,726 engines). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,749pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~693pp, ~34,000 tests, ~460 engines). Total ~5,142pp, ~177K tests, ~4,186 engines, 3,500+ tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

Today's date: 2026-04-17. This file reflects the Wave 14 reconstitution (2026-04-16) and the Beilinson-rectified audit (2026-04-17).

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
3. **Smaller always-on prompt, stronger triggered workflows.** Keep the constitutional layer compact. Put deep repeated workflows into skills. Put deterministic enforcement into hooks or grepable checks.
4. **Prompt geometry matters.** Issue-shaped prompts outperform essays. Exact files, labels, formulas, conventions, nearby diffs, and acceptance checks beat broad aspirations.
5. **Reasoning effort is a last-mile knob.** Before increasing effort, tighten the task, read the live surface, lock conventions, and name the falsifier.
6. **Interleave reasoning with tools.** Read, grep, diff, test, then reason. Do not try to solve a local mathematical or repository problem from abstract memory alone.
7. **Multiple independent checks beat single-chain confidence.** Prefer direct computation plus source reading plus limiting-case or convention checks.
8. **Externalize only durable state.** The artifacts that should survive compaction are labels, hypotheses, grep targets, failing tests, open blockers, and verification notes.
9. **Smaller true claims beat larger false claims.** Impressive prose that does not survive rereading is failure.
10. **Build artifacts are not evidence.** PDFs, logs, and generated summaries help navigation, but they do not outrank source, proof, tests, or exact citations.

### GPT-5.4 Prompt Architecture (composing task prompts)

Use XML-tagged blocks for structural clarity:

- `<task>`: concrete job and repository context
- `<structured_output_contract>`: exact shape, ordering, brevity
- `<default_follow_through_policy>`: act without asking routine questions; stop only when a missing detail changes correctness or safety
- `<verification_loop>`: verify result against task requirements before finalizing
- `<grounding_rules>`: ground every claim in evidence; label hypotheses
- `<missing_context_gating>`: do not guess missing repository facts; retrieve with tools or state unknowns
- `<completeness_contract>`: resolve fully; check for follow-on fixes and edge cases
- `<dig_deeper_nudge>`: after first finding, check for second-order failures, empty-state behavior, stale state
- `<action_safety>`: keep changes scoped; avoid unrelated refactors; call out risky actions
- `<tool_persistence_rules>`: keep using tools until evidence suffices; do not abandon after partial read

**Anti-patterns**: vague task framing; missing output contract; asking for "more reasoning" instead of better contract; mixing unrelated jobs into one run; unsupported certainty without grounding.

## III. `/chriss-ginzburg-rectify` -- READ THE WHOLE FILE, CHUNK BY CHUNK, LINEARLY (CONSTITUTIONAL)

When `/chriss-ginzburg-rectify` (or the skill) is invoked on a target file, Phase 1 (Global Diagnostic) is NOT OPTIONAL and is NOT ABBREVIATED. Analyse the **whole file**, **chunk by chunk**, **linearly**, from start to finish, with **small chunk size**. Every line must pass under your eyes.

**Binding rules:**
- The skill's wording "For files >3000 lines: sample strategically" is OVERRIDDEN. Do NOT sample. Do NOT jump. Do NOT read section heads via Grep and call it Phase 1. Do NOT read only opening + closing + dense midsection.
- **Chunk size: ~250-500 lines per Read call, at most.** Large chunks (1000+) that approach the 25000-token cap compress context and invite skimming. Prefer many small Reads to few large ones. Within the `chriss-ginzburg-rectify` skill itself, the default is ~50 lines per chunk.
- **Linear progression:** start at line 1. Each subsequent Read starts where the previous one ended. No skips; no revisits unless a Phase 3 edit requires it.
- **Coverage is a proof obligation.** Sum of `limit` across all Phase 1 Reads equals the file line count. Starting offsets form a contiguous cover of [1, EOF]. If you cannot state this, Phase 1 is incomplete.
- Grep does NOT substitute for Phase 1. Grep is Phase 3 cross-file propagation.
- If a Read fails at 25000 tokens, cut `limit` in half and retry. Never skip the oversized region.
- If the skill is invoked without a file argument or on a non-existent path, STOP and ask. Do not silently rectify something else.

A 5000-line chapter takes ~10-20 small Reads. That is the cost; it is not negotiable. Prior "CONVERGED (0 edits)" declarations based on lightweight `rg` screens missed formula bugs, define-before-use violations, unmotivated definitions, operadic conflations, scope inflations, and circular-proof routings. Linear whole-file coverage is the only reliable protection.

## IV. Programme Identity (Crystallized 2026-04-12; Wave 14 panoramic 2026-04-17)

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0).

**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center.** B^ord(A) is an E_1-chiral coassociative COALGEBRA over (ChirAss)^!. It carries a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. SC^{ch,top} (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_ch(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output.

**The E_n operadic circle:** E_3-TOPOLOGICAL(bulk) -> E_2(boundary chiral) -> E_1(bar/QG) -> E_2(Drinfeld center) -> E_3-TOPOLOGICAL(derived center). Each arrow: restriction to codim-2 defect, ordered bar complex, categorified averaging, higher Deligne. The circle closes for 3d HT with conformal vector. Without conformal vector: stuck at SC^{ch,top}.

**SC^{ch,top} != E_3.** Swiss-cheese is two-coloured with directionality. Dunn additivity does NOT apply. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. `thm:topologization` PROVED for affine KM V_k(g) at k != -h^v. General: CONJECTURAL. Proof is cohomological (Q-cohomology); for class M chain-level E_3 may fail on the direct-sum ambient.

**Five notions of E_1-chiral algebra:** (A) strict ChirAss, (B) A_inf in End^ch_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)<->(C) via Drinfeld associator on Koszul locus.

**Three Hochschild theories:** (i) Topological HH: E_1 -> E_2 (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral -> E_inf, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category -> E_2 w/ CY shifted Poisson. NEVER conflate. Geometry determines which: curve X -> chiral; R -> topological; CY category -> categorical.

**Architecture (2026-04-13):** E_n chiral algebra theory stays in Vol I (algebraic-geometric objects on curves and configuration spaces: factorisation algebras, FM compactifications, Mok's logarithmic spaces, bar complexes at all E_n levels, derived chiral centres -- inherently geometric, never "pure algebra"). Derived centres are constructed and their E_n properties proved in Vol I; Vol II interprets them physically as 3d HT gauge theories. Vol III constructs concrete CY quantum groups as examples of Vol I's abstract E_1-chiral quantum groups, via 6d hCS, 4d/5d HT CS, little string theory, M5 branes.

**Wave 14 panoramic synthesis (2026-04-16/17).** ONE atomic phenomenon (chiral Koszul reflection), THREE lenses (operadic / holographic / geometric), FOUR generating identities (G1-G4 = MC for Theta_A, d_bar = KZ^*(nabla_Arnold), kappa = -c_ghost(BRST), shadow obstruction tower obs_g = kappa*lambda_g + delta_F_g^cross), ONE universal trace identity bridging Vol I <-> Vol III via Phi. The universal conductor K = c + c^! = -c_ghost(BRST) unifies `{-k, 2dim(g), 26, 100, 196}` across the programme; the scalar complementarity kappa + kappa^! = rho_A * K produces the family-dependent `{0, 13, 250/3, 98/3}`. Wave 14 reconstitution drafts live in `adversarial_swarm_20260416/wave14_*.md` (Theorem A Koszul Reflection, kappa conductor, climax theorem, shadow tower quadrichotomy, BRST ghost identity, MC5 theorem, q-convention bridge, S_5 Wick, Phi functor Vol III).

**What we study.** Holomorphic chiral (factorisation) (co)homology via bar and cobar chain constructions at various geometric locations, hence the different (modular) operads at play. Geometry determines the operad; the operad determines the bar complex; the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**North star:** `memory/platonic_ideal_reconstituted_2026_04_17.md`. Supersedes 2026-04-13 and 2026-04-12 reconstitutions. Wave 14 panoramic synthesis across three volumes.

## V. The Beilinson Principle

"What limits forward progress is not the lack of genius but the inability to dismiss false ideas." Every claim is false until independently verified from primary source. Prefer a smaller true theorem to a larger false one. Every numerical claim requires 3+ genuinely independent verification paths (direct computation, alternative formula, limiting case, symmetry/duality, cross-family, literature+convention, dimensional analysis, numerical evaluation).

Operational consequences: treat every confident statement as provisional until checked locally; if a proof seems to work "morally", identify the exact map, filtration, hypothesis, category, and comparison theorem; search first for hidden hypotheses, scope leakage, conflated objects, sign/grading errors, reduced-vs-completed mistakes, status inflation; never preserve legacy text just because it exists; use the compute layer as an adversarial instrument.

**Epistemic hierarchy** (higher wins): (1) Direct computation > (2) .tex source +/-100 lines > (3) Build system > (4) Published literature > (5) concordance.tex > (6) This file > (7) Memory. Before every assertion: "How do I know this? Read the source, computed it, or assumed it?" If assumed, stop and verify.

## VI. Truth Hierarchy

1. Direct computation or a local proof whose nontrivial steps can be named and checked
2. The live `.tex` or `.py` source, read in context
3. Targeted tests, metadata generation, and build/log evidence that genuinely verifies the claim
4. Exact primary literature with explicit convention conversion
5. `chapters/connections/concordance.tex`
6. `metadata/theorem_registry.md` and other generated metadata
7. `CLAUDE.md` and this file
8. Memory, prior agent prose, and repo folklore

**Not evidence:** confidence; repetition across files; a claim-status macro by itself; a previously generated PDF; README or notes outclaiming source; earlier agent summaries not rechecked locally.

## VII. Constitutional Files And Required First Reads

Before any substantive mathematical edit, read:

1. `CLAUDE.md`
2. `chapters/connections/concordance.tex`
3. `metadata/theorem_registry.md`
4. `raeeznotes/raeeznotes100/red_team_summary.md` (or `archive/raeeznotes/raeeznotes100/red_team_summary.md`)
5. The exact files you will touch, plus directly cited dependencies

`chapters/connections/concordance.tex` is the constitution of the monograph. When files disagree, repair the chapter/theorem/status to match the concordance, or update the concordance deliberately.

**Reference files (load on demand):**
- `notes/cross_volume_aps.md` -- Vol II V2-AP1..39 + Vol III AP-CY1..67. Read before any cross-volume edit.
- `notes/true_formula_census.md` -- Full C1-C31 census (externalized 2026-04-16).
- `notes/first_principles_cache_comprehensive.md` -- 210+ confusion-pattern registry with regex triggers.
- `chapters/examples/landscape_census.tex` -- Canonical kappa / r(z) / central charges per family. MANDATORY Read before any formula.

## VIII. Manuscript Metadata Hygiene (CONSTITUTIONAL, ZERO TOLERANCE)

The anti-pattern catalogue, the confusion-pattern cache, and all metacognitive accounting stay OUT of the manuscript and OUT of the standalone papers. They live only in `CLAUDE.md`, `AGENTS.md`, `notes/first_principles_cache_comprehensive.md`, `MEMORY.md`, `notes/`, and the `memory/` directory. The manuscript and standalones are the mathematics; the metacognitive architecture is scaffolding the reader must never see.

**FORBIDDEN tokens in any typeset line** of `chapters/**/*.tex`, `standalone/**/*.tex`, `main.tex` (outside `%` comments), or any `.tex` file that compiles into the monograph or a standalone paper:

- `AP\d+` (e.g. `AP1`, `AP113`, `AP234`), including in prose, remark/theorem titles, and section headers.
- `V\d-AP\d+` (e.g. `V2-AP39`), `AP-CY\d+`, `FM\d+`, `B\d+` when used as blacklist identifiers.
- `HZ-\d+`, `HZ-[IVX]+` (e.g. `HZ-4`, `HZ-IV`): hot-zone labels.
- `Pattern \d+`, `Cache #\d+`: first-principles-cache entry identifiers.
- `first_principles_cache` or `first principles cache` referenced by name in typeset prose.
- "cache entry", "anti-pattern catalogue", "catalogue of anti-patterns", "the AP catalogue", or any variant.
- Titles like `\section{Universal APxxx healing}`, `\begin{remark}[..., AP\d+]`, `\label{...-ap\d+}`.
- Commit-message style metadata: `RECTIFICATION-FLAG`, "(per AP...)", "(per cache...)".

**ALLOWED:**

- LaTeX comments starting with `%` (invisible in the PDF). `% AP126 check: k=0 gives r=0.` is fine as scaffolding.
- References in `CLAUDE.md`, `AGENTS.md`, `MEMORY.md`, `notes/first_principles_cache_comprehensive.md`, `notes/`, `memory/`, `adversarial_swarm_*/`, `compute/` Python, test files.
- Referring to a mathematical pattern by its mathematical content (e.g. "level-prefix convention", "trace-form r-matrix at k=0", "family-dependent anomaly ratio"). Rename and describe in substance, not by catalogue index.

**Healing protocol** when an AP reference is found in typeset prose:

1. Parenthetical tag (`, AP1 / AP39` in a remark title; `(AP77)` in prose): remove entirely. The mathematical substance already conveys the point.
2. Section header (`\section{Universal AP126 healing}`): rename to describe the mathematics. Update `\ref{sec:...}` targets.
3. Load-bearing prose sentence (`By AP77, the series is Pade-summable`): rephrase as mathematical content (`The series is convergent and therefore Pade-summable rather than Borel-summable`).
4. Label (`\label{rem:foo-ap42}`): rename to `\label{rem:foo}` and grep the whole Vol for `\ref{rem:foo-ap42}` to update. Labels stay unique.

**Enforcement.** Before every commit whose diff touches `.tex` files under `chapters/`, `standalone/`, or the abstract of `main.tex`:

```bash
# Vol I:
grep -rn '\bAP[0-9]\+\b\|\bHZ-[0-9IVX]\+\b\|V[0-9]-AP[0-9]\+\|AP-CY[0-9]\+\|\bPattern [0-9]\+\b\|Cache #[0-9]\+\|first_principles_cache' \
  /Users/raeez/chiral-bar-cobar/chapters/ \
  /Users/raeez/chiral-bar-cobar/standalone/ \
  2>/dev/null | grep -v ':[0-9]*:\s*%'
# Vol II: same under /Users/raeez/chiral-bar-cobar-vol2/
# Vol III: same under /Users/raeez/calabi-yau-quantum-groups/
```

Zero hits is the commit-gate. If any hit appears: stop, heal, re-grep until zero.

**AP236 companion check (2026-04-17):** blacklist-slug leakage into typeset parentheticals. Agents occasionally leak `/B\d+` identifiers into `\textup{(}...\textup{)}` annotations. Grep `\\textup\{\(\}\s*\/B\d+|(\s*\/B\d+;` and `\\textup\{\(\}\\textup\{\)\}` (orphan empty parentheticals) before every commit.

**Why.** The manuscript is the object of study for the reader; the catalogue is the author's working notebook. A reader who opens the PDF and encounters `(AP225)` in a theorem statement sees scaffolding, not mathematics. Catalogue indices rot; prose coupled to them breaks.

## IX. E1-First Prose Architecture (MANDATORY)

The ordered bar B^ord(A) is the primitive object. Every chapter, section, theorem presentation MUST construct the E1 ordered story first, then derive the symmetric story by averaging:

1. CONSTRUCT the E1 object (B^ord, r(z), Theta_A in g^{E1}, the matrix-valued curvature)
2. EXHIBIT the E1 structure (deconcatenation coproduct, R-matrix, Yangian)
3. APPLY the averaging map av: g^{E1} -> g^mod (lossy Sigma_n-coinvariant projection)
4. DERIVE the symmetric result (kappa from av(r(z)); for non-abelian affine KM, av(r(z)) + dim(g)/2 = kappa; obs_g = kappa*lambda_g, the shadow tower)

NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" -- they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.

The convolution algebra has two levels: g^{E1}_A (primitive, carrying the R-matrix) and g^mod_A (coinvariant shadow, carrying only kappa). Theta_A lives in g^{E1}_A; everything in the monograph is its Sigma_n-coinvariant projection.

## X. The Five Objects (NEVER CONFLATE)

- **A**: algebra
- **B(A) = T^c(s^{-1} Abar)**: bar coalgebra (Abar = ker(epsilon), augmentation ideal)
- **A^i = H*(B(A))**: dual coalgebra (Koszul cohomology of bar)
- **A^! = ((A^i)^v)**: dual algebra (linear or Verdier dual)
- **Z^{der}_{ch}(A)**: derived chiral center = bulk (Hochschild cochains)

Omega(B(A)) = A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.

**FORBIDDEN conflations:**
- "bar-cobar produces bulk" (WRONG: bar-cobar inverts to A; bulk is Hochschild)
- "Omega(B(A)) is the Koszul dual" (WRONG: that is INVERSION)
- "the Koszul dual equals the bar complex" (WRONG: bar is coalgebra, dual is algebra)
- "D_Ran(B(A)) is the cobar complex" (WRONG: D_Ran is Verdier; cobar is Omega)

**SC^{ch,top} is NOT on B(A).** B(A) is E_1 coassociative coalgebra. SC^{ch,top} lives on the pair (C^bullet_ch(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."

**SC^{ch,top} is NOT Koszul self-dual.** SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!. SC = (Com, Ass) with closed dim = 1. The duality FUNCTOR is involutive; the OPERAD is not self-dual.

**A^! is an SC^!-algebra** = (Lie, Ass)-algebra (closed = Sklyanin bracket, open = Yangian product). NOT an SC-algebra.

## XI. The Four Shadow Classes (quadrichotomy)

The canonical term is **quadrichotomy** (NOT "quaternitomy"). Matches `thm:quadrichotomy` in `shadow_tower_quadrichotomy_platonic.tex`. Grep `quaternitomy` after any write naming the G/L/C/M partition.

- **G**: r=2, Heisenberg. Delta=0, d_alg=0. SC-formal.
- **L**: r=3, affine KM. Delta!=0, d_alg=1.
- **C**: r=4, betagamma. Delta!=0, d_alg=2.
- **M**: r=inf, Vir/W_N. Delta!=0, d_alg=inf.

Delta = 8*kappa*S_4. Delta=0 <-> finite tower. SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.

## XII. Cross-Volume Scope

- Vol I: `~/chiral-bar-cobar`
- Vol II: `~/chiral-bar-cobar-vol2`
- Vol III: `~/calabi-yau-quantum-groups`

When a task touches shared formulas, theorem statuses, definitions, notation, bridge claims, chapter references, or hardcoded expected values, the live surface includes all three volumes.

Cross-volume rule: grep before editing; grep after editing; update all genuine duplicates in the same session, or leave an explicit pending note.

## XIII. HOT ZONE -- Top 10 Repeat Offenders + Independent Verification Protocol

Read BEFORE any edit. These are the APs that fire repeatedly across waves despite being catalogued. Each entry is operational, not prose. Covers ~80% of real-world violation patterns. Full AP catalogue: §XVIII onward.

### HZ-1. AP126/AP141 (r-matrix level prefix) -- 6 waves, 90+ instances

Template, fill BEFORE writing any r-matrix:

```
family:               [Heis / affine KM / Vir / W_N / Yang rational / Calogero-Moser]
r(z) written:         [formula with level prefix visible]
level parameter:      [k / k+h^v / hbar / c]
k=0 check:            r(z)|_{level=0} = [value]    required: 0 (trace-form convention)
match?                [Y/N]   <-- must be Y for trace-form; KZ convention at k=0 gives
                                  Omega/(h^v*z) != 0 for non-abelian g (correct: Lie bracket persists)
source:               landscape_census.tex line [N] OR compute engine
FORBIDDEN bare forms: Omega/z (no level), k*Omega/z^2 (double pole)
```

Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix write: grep for bare `\Omega/z` without level prefix; any match = STOP.

### HZ-2. AP40 (environment matches tag) -- 5 waves, 70+ instances

Decision tree, answer BEFORE writing `\begin{...}`:

```
Q1: Complete proof here or in cited literature?
    NO  -> \begin{conjecture} + \ClaimStatusConjectured. STOP.
    YES -> Q2
Q2: Backbone main / supporting / auxiliary?
    main       -> \begin{theorem}
    supporting -> \begin{proposition}
    auxiliary  -> \begin{lemma}
Q3: Self-contained or cited?
    self-contained -> \ClaimStatusProvedHere + \begin{proof}
    cited          -> \ClaimStatusProvedElsewhere + Remark[Attribution]
UNCERTAIN -> default \begin{conjecture}. Downgrade is cheaper than rename.
```

Vol III default: `\begin{conjecture}` regardless. Label prefix follows environment.

### HZ-3. AP32 (uniform-weight tag on F_g) -- 4 waves, 30+ instances

Every formula of the form `F_g = ... lambda_g ...` or `obs_g = ...` MUST be followed in the same sentence by ONE of:

```
(a) (UNIFORM-WEIGHT)
(b) (ALL-WEIGHT, with cross-channel correction delta F_g^cross)
(c) (g=1 only; ALL-WEIGHT at g=1 is unconditional)
(d) (LOCAL: scope defined in surrounding paragraph, see ref:...)
```

No "in a theorem" loophole. Tag required in prose, remarks, and definitions.

### HZ-4. AP1 (kappa from memory) -- 4 waves, 15+ instances

Writing kappa from memory is FORBIDDEN. Before ANY kappa:

```
Step 1: Identify family (Heis / Vir / KM / W_N / free / coset / SVir / BP / betagamma)
Step 2: Open landscape_census.tex, copy formula WITH citation comment
Step 3: Paste with comment: % formula from landscape_census.tex:LINE; k=0 -> VALUE verified
Step 4: Evaluate at two boundary values and write results in comment
```

Quick reference (cross-check census before use):
- KM: `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`; k=0 -> dim(g)/2; k=-h^v -> 0 (critical)
- Vir: `kappa(Vir_c) = c/2`; c=13 -> 13/2 (self-dual)
- Heis: `kappa(H_k) = k`; k=0 -> 0
- W_N: `kappa(W_N) = c*(H_N - 1)`, `H_N = 1 + 1/2 + ... + 1/N`. NOT `H_{N-1}`. At N=2: H_2=3/2, H_2-1=1/2, kappa(W_2)=c/2=Vir.

### HZ-5. AP125/AP124 (label prefix and uniqueness) -- 3 waves, 25+ instances

Before writing `\label{foo}`:

```
(i)  Prefix matches environment: thm/prop/lem/conj/rem/def/eq
(ii) Uniqueness across all three volumes:
     grep -rn '\\label{foo}' ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups
     0 -> safe. >=1 -> rename with volume suffix (v1-, v2-, v3-).
```

Downgrade atomicity: when downgrading theorem -> conjecture, rename `thm:foo -> conj:foo` AND update every `\ref{thm:foo}` across three volumes in the SAME tool-call batch. No intermediate commit.

### HZ-6. AP10/AP128 (hardcoded expected values) -- 3 waves, 12+ engines

Every hardcoded expected value requires `# VERIFIED` citing 2+ independent sources from different categories:

```
[DC] direct computation     [LT] literature (paper + eq #)
[LC] limiting case          [SY] symmetry
[CF] cross-family           [NE] numerical (>=10 digits)
[DA] dimensional analysis
```

When correcting an engine, derive the new expected value from an INDEPENDENT source, NOT from the corrected engine output. Engine and test sharing the same wrong mental model is the most dangerous AP10 variant.

### HZ-7. AP113 (bare kappa in Vol III) -- 3 waves, 165 baseline instances

Bare `\kappa` in Vol III is permitted IFF the section opens with a local definition. Approved subscripts (closed set): `{ch, cat, BKM, fiber}`. FORBIDDEN: `{global, BPS, eff, total, naive}`.

Decision tree:
- chiral algebra -> `kappa_ch`
- BKM algebra -> `kappa_BKM`
- Euler characteristic -> `kappa_cat`
- lattice/fiber -> `kappa_fiber`

### HZ-8. AP4 (proof after conjecture) -- 3 waves, 40+ instances

Before `\begin{proof}`:

```
Step 1: Nearest preceding \begin{...} within 30 lines
Step 2: theorem/prop/lemma -> proof may follow
        conjecture/heuristic/remark/definition -> STOP, use \begin{remark}[Evidence]
Step 3: ClaimStatus tag check
        ProvedHere -> self-contained proof body
        ProvedElsewhere -> paragraph attributing, NOT re-proof
        Conjectured -> AP40 upstream violation
```

### HZ-9. AP25/AP34/AP50 (four-functor discipline) -- 3 waves, 15+ instances

Write this list before any paragraph mentioning "bar", "cobar", "Koszul dual", or "derived center":

```
% FOUR OBJECTS:
% 1. B(A) = bar coalgebra = T^c(s^{-1} A-bar) with deconcatenation + twist
% 2. A^i = H^*(B(A)) = dual coalgebra (Koszul cohomology of bar)
% 3. A^! = ((A^i)^v) = dual ALGEBRA (linear or Verdier dual)
% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk
```

### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances, 3 zero-tolerance commits

PRE-WRITE check: does the sentence start with one of the banned tokens? If yes, REWRITE before typing.

POST-WRITE grep (mandatory):

```
Banned (case-insensitive): moreover, additionally, notably, crucially, remarkably,
interestingly, furthermore, "we now", "it is worth noting", "worth mentioning",
"it should be noted", "it is important to note", delve, leverage, tapestry,
cornerstone, landscape (as metaphor), journey, navigate (non-geometric).

Em-dash (---, U+2014) FORBIDDEN. Use colons, semicolons, separate sentences.

Hedging ban in math: arguably, perhaps, seems to, appears to. State or mark as conjecture.
```

Three cleanup commits in Vol II prove aspirational instructions insufficient. Post-write grep is the only reliable enforcement.

### HZ-IV. Independent Verification Protocol (cross-volume, installed 2026-04-16)

**Canonical (verbatim) location:** Vol III `CLAUDE.md` "Independent Verification Protocol". Identical machinery lives at `compute/lib/independent_verification.py`, `compute/scripts/audit_independent_verification.py`, `compute/tests/test_independent_verification_infra.py`, `notes/INDEPENDENT_VERIFICATION.md`.

**Operational summary (sufficient without loading Vol III):** every `\ClaimStatusProvedHere` test must declare `derived_from`, `verified_against`, `disjoint_rationale`. Disjointness checked at import time. Three healings when honest decoration fails:
1. find a disjoint source
2. restrict scope (`\begin{proposition}` for partial)
3. downgrade to `\ClaimStatusConjectured`

**Coverage snapshot at installation (2026-04-16):** Vol I 0/2275, Vol II 0/1134, Vol III 2/283. The gap closes only through GENUINE verification or explicit status downgrade, never tautological decoration. Vol I working queue: to be seeded as adversarial audits identify candidates.

## XIV. Canonical Formulas

Verify against these AND `landscape_census.tex` before writing. NEVER write kappa from memory.

```text
# Kappa (C1-C4)
kappa(H_k) = k                                       # Heisenberg; k=0->0, k=1->1
kappa(Vir_c) = c/2                                    # Virasoro ONLY; c=0->0, c=13->13/2
kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)                 # Affine KM; k=0->dim(g)/2 (NOT 0), k=-h^v->0
kappa(W_N) = c*(H_N - 1), H_N = sum_{j=1}^N 1/j      # W_N; N=2: H_2-1=1/2 so kappa=c/2=Vir

# r-matrix (C9-C11) -- level prefix k MANDATORY (THE MOST VIOLATED PATTERN)
r^KM(z) = k*Omega/z           [trace-form]            # k=0->0; k=-h^v->finite
r^KM(z) = Omega/((k+h^v)*z)   [KZ]                    # k=0->Omega/(h^v*z)!=0; k=-h^v->diverges
r^Heis(z) = k/z                                       # k=0->0
r^Vir(z) = (c/2)/z^3 + 2T/z                           # cubic+simple, NOT quartic. d-log absorbs one

# Bridge: k*Omega_tr = Omega/(k+h^v) at generic k
# Averaging (C13): av(r(z)) = kappa for abelian; av(r(z)) + dim(g)/2 = kappa for non-abelian KM

# Central charges (C5-C7)
c_bc(lambda) = 1 - 3(2*lambda-1)^2                    # fermionic; lambda=1/2->1, lambda=2->-26
c_bg(lambda) = 2(6*lambda^2-6*lambda+1)               # bosonic; lambda=1/2->-1, lambda=2->+26
c_bc + c_bg = 0                                        # pointwise; verify at lambda=1: 2+(-2)=0

# Bar complex (C14-C15)
B(A) = T^c(s^{-1} A-bar), A-bar = ker(epsilon)        # augmentation ideal, NOT bare A
|s^{-1}v| = |v| - 1                                    # desuspension LOWERS; mnemonic: bar=down=s^{-1}
d_bar^2 = 0 ALWAYS; d_fib^2 = kappa*omega_g            # fiberwise only, at g>=1

# Structural constants
MC: d*Theta + (1/2)[Theta,Theta] = 0
QME: hbar*Delta*S + (1/2){S,S} = 0
F_1 = kappa/24                                         # sanity check for Cauchy normalization
F_2 = 7*kappa/5760                                     # NOT 7/2880, NOT 1/5760
eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)              # q^{1/24} ESSENTIAL for modular weight 1/2
Cauchy: [z^{n-1}]f(z) = 1/(2*pi*i) * oint f(z)dz/z^n  # NOT 1/(2*pi) -- missing i
Delta = 8*kappa*S_4                                    # LINEAR in kappa, NOT quadratic
S_2 = kappa for ALL families                           # S_2=c/12 is WRONG (divided-power confusion)

# Complementarity (two K's with same letter; NEVER CONFLATE)
# (a) Scalar complementarity: kappa(A) + kappa(A^!) (family-dependent)
kappa(KM) + kappa(KM^!)    = 0
kappa(Heis) + kappa(Heis^!)= 0
kappa(free) + kappa(free^!)= 0
kappa(Vir) + kappa(Vir^!)  = 13       # self-dual c=13; NOT 26
kappa(W_3) + kappa(W_3^!)  = 250/3
kappa(BP) + kappa(BP^!)    = 98/3     # NOT 1/3; self-dual k=-3
# (b) Trinity ghost conductor: K(A) = c(A) + c(A^!) = -c_ghost(BRST)
K(KM)   = 2*dim(g)      K(Heis) = -k       K(Vir) = 26       K(W_3) = 100      K(BP) = 196
# Relation: kappa + kappa^! = rho_A * K(A)
#   rho_N = H_N - 1 for principal W_N (rho_2 = 1/2, rho_3 = 5/6)
#   rho_KM = rho_free = 0
#   rho_BP = 1/6
# At c=13 Vir self-dual: K=26, kappa+kappa^!=13; cross-check: rho_Vir * K = (1/2) * 26 = 13. OK.

# Combinatorial / numerical
sl_2 bar H^2 = 5 (NOT 6)
genus-2 stable graphs = 7 (NOT 6)
E_8 adjoint = 248 (NOT 779247 -- not any E_8 irreducible)
1/eta^2 coefficients: (1,2,5,10,20,...) bicoloured partitions (NOT triangular 1,3,6,10,...)
K_g^{FdV} = 2*rank + 4*dim*h^v (Freudenthal-de Vries Koszul conductor, Hilbert-series growth; name alpha_g reserved for Gaussian sewing 2-cocycle det(1-CB)^{-1/2} in higher_genus_complementarity.tex:6082)
d_alg in {0,1,2,inf} (depth gap: 3 impossible, prop:depth-gap-trichotomy)

# Shadow exponential base
C_A = limsup |A_{r+1}/A_r| = 6 uniformly on non-logarithmic class M T-line with Virasoro subalgebra
Closed form: Sigma_Vir(z) = 4z^3/9 - z^2/9 + z/27 - log(1+6z)/162
Pole-doubling all k:      Sigma_Vir^{(k)}(z) = [P_k + Q_k*log(1+6z)]/(1+6z)^{2k}
Decomposition: 6 = r_0 * S_{r_0} = 3 * 2
Cross-volume: beta_A (Vol II tempering rate) = C_A at leading 1/c

# W_3 W-line (iter 58)
a_n = 2*3^{n-2}*C(2n-4,n-2)/[n*(n-1)];  a_{n+1}/a_n = 12-30/(n+1);  C_{W_3}^{W-line} = 12 = 2*6
Stirling: a_n ~ 12^n/(72*sqrt(pi)*n^{5/2}).  K_3 = 4 (Koszul-dual invariant under c->4-c)
Conjectural spin-stratified lattice: C_{W^{(s)}} = s(s+1)  (s=2: 6; s=3: 12; s=4: 20)

# Super-Yangian complementarity (Beilinson-rectified 2026-04-17)
kappa(Y(sl(m|n))) + kappa(Y(sl(n|m))^!) = max(m, n)   # at Sugawara-shifted dual level;
                                                       # prior "= 0" Virasoro analogy RETRACTED

# beta_N exact closed form (Vol II thm:beta-N-closed-form-proved-all-N)
beta_N = 12*(H_N - 1) = sum_{s=2}^{N} 12/s            # rational for N>=5; beta_5=77/5, beta_6=87/5
```

Full census C1-C31 with wrong variants and derivations: `notes/true_formula_census.md`; top-5 (C3, C4, C9, C14, C19) inline in CLAUDE.md.

## XV. Wrong Formulas Blacklist (grep after every .tex write)

Concrete forbidden forms repeatedly emitted. Match = fix immediately. Format: `BAD -> CORRECT`.

```text
# r-matrix / level (MOST VIOLATED; see AP-RMATRIX)
B1.  r(z) = \Omega/z                         -> MUST be k*\Omega/z (bare level-stripped)
B2.  r^Vir(z) = (c/2)/z^4                    -> (c/2)/z^3 + 2T/z (cubic + simple, NOT quartic)
B3.  r^Vir(z) = (c/2)/z^2                    -> cubic + simple
B4.  \Omega\,d\log z  (no k)                 -> k\Omega\,d\log z

# central charges / kappa
B5.  c_{bc} = 2(6L^2-6L+1)                   -> that is c_bg (swapped)
B6.  c_{bg} = 1-3(2L-1)^2                    -> that is c_bc (swapped)
B7.  kappa(W_N) = c*H_{N-1}                  -> c*(H_N - 1)
B8.  kappa = c/2 unqualified                 -> Virasoro ONLY
B9.  kappa+kappa' = 0 unscoped               -> family-specific: 0 KM/free, 13 Vir, 250/3 W_3, 98/3 BP
B10. kappa = S_2/2                           -> S_2 = kappa (no factor 2); only Vir has kappa=c/2
B11. av(r(z))=kappa for non-abelian KM       -> missing Sugawara shift dim(g)/2
B12. bare kappa in Vol III                   -> kappa_{ch|cat|BKM|fiber}
B13. kappa_{global|BPS|eff|total|naive}      -> only approved subscripts in Vol III

# bar complex / suspension (see AP-DESUSP)
B14. T^c(s^{-1} A)                           -> T^c(s^{-1} A-bar) (augmentation ideal)
B15-B16. T^c(s A) or |s^{-1}v|=|v|+1         -> s^{-1} direction, |v|-1 lowers
B17. eta = prod(1-q^n) (bare)                -> eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)

# boundaries / combinatorics / numerical
B18. W_N weights {2,...,N+1}                 -> {2,...,N}  (N-1 generators)
B19. H_N = sum_{j=1}^{N-1} 1/j               -> upper limit N, not N-1
B20. C_n = binary trees w/ n leaves          -> n+1 leaves (n internal nodes)
B21. E_8 fundamental = 779247                -> NOT any E_8 irreducible
B22. dim H^2(B(sl_2)) = 6                    -> 5
B23. genus-2 stable graphs = 6               -> 7
B24. 1/eta^2 coefficients (1,3,6,10,...)     -> bicoloured (1,2,5,10,20,...)
B25. K_BP = 2                                -> 196

# scope / quantifier
B26. obs_g = kappa*lambda_g untagged         -> tag (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta)
B27. A <-> B where only -> proved            -> -> + Remark on converse
B28. "k=0 fails Koszulness" for KM           -> k=0 abelian, still Koszul; k=-h^v is critical
B29. Thm C^{E1} with n free on RHS           -> quantify with 2g-2+n > 0

# macros / labels / LaTeX
B30-B31. \end{definition>, \begin{theorem>   -> > instead of } (grep \\end\{[^}]*>)
B32. \cW in standalone w/o \providecommand   -> add macro to preamble
B33. Part~IV, Chapter~12 hardcoded           -> \ref{part:...}
B34. duplicate label across volumes          -> suffix v1-/v2-/v3-
B35. \begin{conjecture}\label{thm:foo}       -> prefix MUST match environment
B36. \cite{GeK98} without bibitem            -> emits [?]

# numerical coefficients
B37. F_2 = 1/5760 or 7/2880                  -> 7/5760
B38. 1/(2*pi) integral (missing i)           -> 1/(2*pi*i)
B39. KM r-matrix not vanishing at k=0        -> level-prefix violation (see AP-RMATRIX)

# prose
B40. Markdown in LaTeX (backticks, **bold**) -> $...$, \textbf, \emph
B41. Em-dash (--- or U+2014)                 -> colon, semicolon, separate sentence
B42. AI slop (notably, crucially, etc.)      -> banned vocabulary

# depth / dimension / fiber-base
B43. d_alg(Vir) = 3                          -> d_gen=3, d_alg=inf
B44. bare d(Vir) without gen/alg             -> always subscript
B45. vdim ChirHoch*(A) = 2                   -> amplitude [0,2], NOT vdim
B46. omega_g = dtau                          -> dtau on curve, omega_g = c_1(lambda) on moduli

# grading / curved
B47. [m,[m,f]]=1/2[[m,m],f] at even ||m||    -> tautological at even; identity requires odd
B48. m_1^2 = 0 in curved A-inf               -> m_1^2(a) = [m_0, a]
B49. d^2=kappa*omega_g as bar diff           -> d^2_bar=0 always; d^2_fib fiberwise

# promotion / SC / sector
B50. dim SC^mix_{k,m} = (k-1)!*m!            -> (k-1)!*C(k+m,m)
B51. B_{SC}(A) for one-colour input          -> SC two-coloured; use promotion A->(A,A)
B52. kappa(BP)+kappa(BP^!)=1/3               -> 98/3
B53. "over a point is over P^1"              -> FALSE: retract is DATA; disk!=point; A^1 has Arnold
B54-B56. B(A) SC coalgebra / bar = colors    -> FALSE: B(A) single E_1 coalgebra; SC in derived center pair
B57. SC^{ch,top} is Koszul self-dual         -> FALSE: SC^!=(Lie,Ass,shuffle)
B58. chiral label for topologized center     -> E_3-TOPOLOGICAL
B59. "Topologization proved for all"         -> ONLY affine KM at non-critical level
B60. "A^! is an SC-algebra"                  -> SC^!-algebra = (Lie,Ass)
B61. "chiral QG for all four families"       -> ONLY sl_2 Yangian + affine KM concrete
B62. Delta_z(T) = T + T + (1/Psi)(J.J)       -> (Psi-1)/Psi on cross-term
B63. nabla=d+A with dPhi=+A*Phi              -> inconsistent; nabla=d-A gives dPhi=+A*Phi

# (B64-B67 RETRACTED. B68 merged into S_2=c/2 correction.)

B68-B73 (2026-04: recent corrections): S_2=c/12 for Vir WRONG, MUST S_2=kappa=c/2 (B68); pi_3(BU)=Z WRONG, =0 (Bott, pi_odd(BU)=0) (B69); kappa_ch=h^{1,1} WRONG for h^{0,2}!=0 (K3: h^{1,1}=20, chi/2=12) (B70); McKay(Z_3)=K_{3,3} WRONG -- 3 oriented 3-cycles (9 directed arrows) (B71); "excision gives B(A) (x) B(A)" WRONG -- excision gives B_L (x)_A B_R one copy over A (B72); "pi_4(BU)=Z provides E_2" WRONG -- obstruction group, not guarantee (B73).

B74-B85 (Vol II 2026-04-12/13 cross-volume): Cauchy on formal power series -- formal needs flatness+homotopy-invariance, Cauchy needs convergent (B74); non-holomorphic maps (|z|) on holomorphic complexes introduce dz-bar (B75); chain-level decomp != cohomological decomp (B76); abstract machine theorem != input verification (B77); "Proof sketch" + ClaimStatusProvedHere ambiguous (B78); conj->theorem upgrade requires exhaustive \ref{conj:X} sweep all volumes (B79); two obstruction complexes for one obstruction -- specify which (B80); level-by-level rationality != convergence (gap is eigenvalue not determinant bounds) (B81); cohomological compatibility != chain-level (B82); stale classification lists (update when new theorems expand proved scope) (B83); Khan-Zeng: 3d Poisson sigma model covers ALL freely-generated PVAs w/ conformal vector (B84); orbifold route Z/n-invariants preserves E_n (B85).

B86-B94 (Session 2026-04-17 Beilinson-rectified):
B86. kappa(Y(sl(m|n))) + kappa(Y(sl(n|m))^!) = 0    # CORRECT: = max(m, n) at Sugawara-shifted dual level
B87. "Tempered stratum obstruction kappa^(inf)_orig = 1/e"  # RETRACTED: Stirling factor dropped; correct limsup = 0 generically
B88. "First Kummer-irregular prime 691" (unqualified) # imprecise: 691 is BERNOULLI-LEADING first (B_12); SIZE-LEADING first is 37 (B_32)
B89. "Six routes to G(K3xE) converge isomorphically" # FALSIFIED: pentagon of five intertwiners, R_2 source branch
B90. "CY-C pentagon kappa_ch stratification {3,12,24}"  # CATEGORY ERROR: kappa_ch = 0 route-independent; stratification is rho^{R_i} (generator-lattice rank)
B91. "C_2-cofiniteness => bounded Massey => tempered" (W(p)) # FAILS: Gurarie 1993 + Flohr 1996 exhibit unbounded Massey
B92. Primes 1423, 3067, 23, 43, 419 labelled Kummer-irregular # VERIFIED REGULAR at primary source; they are Riccati-arithmetic, NOT Kummer-arithmetic
B93. kappa(A)+kappa(A^!)=K(A) (bare)   # MUST be kappa + kappa^! = rho_A * K(A); see Canonical Formulas
B94. "quaternitomy"                    # MUST be "quadrichotomy" (canonical per thm:quadrichotomy)
```

Full blacklist and regex triggers: CLAUDE.md §Wrong Formulas Blacklist and `notes/first_principles_cache_comprehensive.md`.

## XVI. Consolidated / Merged Anti-Patterns

Collapsing redundant APs into single operational rules. These replace scattered catalog entries.

**AP-RMATRIX (= AP126 + AP141 + AP148).** Every r-matrix carries level prefix; verify k=0 in the chosen convention. Counter: (a) substitute k=0 and verify r vanishes (trace-form) or gives Omega/(h^v*z) (KZ non-abelian); (b) state convention; (c) grep bare `\Omega/z`. Two conventions for affine KM: trace-form `r(z)=k*Omega/z` (k=0 -> 0; av(r)=kappa_dp; Sugawara shift dim(g)/2 for full kappa); KZ `r(z)=Omega/((k+h^v)*z)` (k=0 nonzero for non-abelian). Bridge: `k*Omega_tr = Omega/(k+h^v)` at generic k. 42+ instances; the most violated pattern.

**AP-KAPPA (= AP1 + AP9 + AP20 + AP24 + AP48 + AP136).** Kappa DISTINCT per family. Always qualify (`kappa^{KM}`, `kappa^{Vir}`). Read landscape_census.tex; evaluate at k=0, k=-h^v (KM), c=13 (Vir); cross-check compute/. Memory writing FORBIDDEN. Values: KM=dim(g)(k+h^v)/(2h^v); Vir=c/2; W_N=c*(H_N-1), H_N=sum_{j=1}^{N} 1/j (at N=2, H_1=1 but H_2-1=1/2); Heis=k. Scalar complementarity: 0 (KM/free), 13 (Vir), 250/3 (W_3), 98/3 (BP). State WHICH algebra: intrinsic vs kappa_eff=kappa(matter)+kappa(ghost) vs kappa(B=A^!).

**AP-DESUSP (= AP22 + AP45 + B15 + B16).** `|s^{-1}v|=|v|-1`. `T^c(s^{-1} A-bar)`, NOT `T^c(s A-bar)`; bar=down=desuspension=s^{-1}.

**AP-SC-BAR (= AP165 + FM25 + B54-B56).** B(A) = T^c(s^{-1} A-bar) is a SINGLE E_1 chiral coassociative coalgebra. SC^{ch,top} lives on the derived center pair (C^bullet_ch(A,A), A), NOT on B(A). The 6-step chain of errors: (1) "bar differential is closed color" WRONG -- d_B is single degree-1 map over (ChirAss)^!. (2) "deconcat = open color" WRONG -- cofree coassociative T^c(V); single-colored E_1. (3) "d_B + Delta = SC-coalgebra" WRONG -- two structures != two colors. (4) "SC on B(A) dual to SC on (Z^{der}(A), A)" WRONG -- B(A) is INPUT; SC emerges in OUTPUT via Hom(B(A),A). (5) "E_1-chiral = E_1-topological" WRONG -- chiral is on CURVE; topological is Conf_k(R); bar is over (ChirAss)^!, not (Ass)^!. (6) Steinberg analogy RETIRED. FORBIDDEN: "B(A) is SC-coalgebra", "bar presents Swiss-cheese", "curved SC^{ch,top}-algebra" for g>=1 (bar is curved A_infinity-chiral). After any paragraph with both B(A) and SC^{ch,top}, verify SC attributed to the derived center pair. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`.

**AP-TOPOLOGIZATION (= AP158 + AP167 + AP168 + B58 + B59).** Topologization (SC^{ch,top} -> E_3-TOPOLOGICAL via Sugawara) PROVED for affine KM V_k(g) at k != -h^v; CONJECTURAL for general chiral algebras with conformal vector. Proof COHOMOLOGICAL (Q-cohomology), not chain-level; for class M chain-level E_3 may fail on direct-sum ambient (PROVED weight-completed; see MC5 table entry). Every reference must carry "(proved affine KM non-critical; conjectural general; cohomological, not chain-level on direct-sum)." SC is two-coloured with directionality; Dunn does NOT apply to coloured operads. Without conformal vector: stuck at SC^{ch,top}. At k=-h^v: Sugawara undefined. "Chiral" label FORBIDDEN for topologized bulk; write E_3-topological. **Wave 14 upgrade (2026-04-16):** iterated Sugawara tower gives E_{k+2}-top for depth-k stress tensors; W_N -> E_{N+1}-top; W_infty -> E_infty-top (Vol II `e_infinity_topologization.tex`).

**AP-SC-NOT-SELFDUAL (= AP166 + FM26 + B57).** `(SC^{ch,top})^! != SC^{ch,top}`. SC^! = (Lie^c, Ass^c, shuffle-mixed), closed dim (n-1)!. SC = (Com, Ass, product-mixed), closed dim 1. Confusion: "duality FUNCTOR is involution" != "OPERAD is self-dual". (P^!)^! ~ P does NOT mean P^! ~ P. Livernet proves Koszulity NOT self-duality. Verify dim P(n) = dim P^!(n) at all degrees before claiming self-dual. CORRECT: "SC Koszul duality exchanges Com <-> Lie while preserving Ass; duality functor is involution."

**AP-UNIFORM-WEIGHT-TAG (= AP32 + B26).** Every obs_g, F_g, lambda_g in theorem/remark/definition MUST carry explicit scope tag: (UNIFORM-WEIGHT), (ALL-WEIGHT + cross-channel correction delta F_g^cross), (g=1 only), (LOCAL: scope in surrounding paragraph). Untagged = violation.

**AP-LABEL-DISCIPLINE (= AP124 + AP125 + B34 + B35 + FM14 + FM15).** (i) prefix matches env (thm/prop/lem/conj/rem/def); (ii) uniqueness across all three volumes. Before any `\label{foo}`, grep all three volumes; if duplicate, prefix v1/v2/v3. When upgrading/downgrading environment: atomic rename (env + label + all `\ref` instances) in SAME tool-call batch, NO intermediate commit.

**FM-LIE-NUMERICS (= FM5 + FM21 + C16).** Never generate exceptional Lie dimensions from memory. Plausible fabrications (779247 for E_8 is not any irreducible); prefactors (1/2, 1/24, 1/(2*pi*i), 7/5760) frequently wrong. Grep `compute/lib/` before writing; if no match, use symbolic name `V_{omega_1}(E_8)`. E_8 fundamentals: `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.

## XVII. Theorem Status Table (Rectified 2026-04-17, post-Wave 14 + Beilinson audit)

**2026-04-17 Beilinson-rectified addendum.** The status table reflects the 2026-04-16 closure wave inscriptions. Audit findings (`notes/rectification_map_beilinson_audit.md`) refined: (i) programme climax `thm:programme-climax` (Vol II) is SCOPE-QUALIFIED to non-logarithmic C_2-cofinite standard landscape + irrational cosets; log W(p) excluded pending Adamovic-Milas character-amplitude bound. (ii) CY-C pentagon (Vol III) stratifies generator rank rho^{R_i}, NOT kappa_ch (Hodge-supertrace invariant = 0 route-independent). (iii) Kummer-irregular prime labels 1423, 3067, 23, 43, 419 retracted at primary-source verification. (iv) Super-Yangian max(m, n) complementarity replaces naive sum=0. (v) Topologization class M original-complex carries retraction notice; the 1/e obstruction is a Stirling cancellation error. Theorems A-D+H remain PROVED at stated scopes; only scope qualifiers and cross-reference labels changed.

| Thm | Status | Key result (summary; CLAUDE.md has full detail) |
|-----|--------|-------------------------------------------------|
| A | **PROVED unconditional** (fixed curve + Mbar_{g,n} incl. boundary, standard landscape) | Genus-0: seven-fold hub-and-spoke TFAE (`ftm_seven_fold_tfae_platonic.tex`, 2026-04-16). Six spokes (Koszul morphism, counit qi, unit weak eq, twisted tensor acyclic, bar weight-1, SC-formality) bidirected to PBW E_2-collapse HUB. Spoke 4 (twisted tensor <-> PBW) load-bearing, witnessed by V_k(sl_2). Spoke 7 class-G scoped. Spoke 5 extends g>=1 only class G. **Modular-family PROVED (2026-04-16):** base-change via BD holonomic + GR17 six-functor; nodal sewing via Mok25 log FM + Francis-Gaitsgory + HS-sewing; Mbar_{g,n} assembly via K-theoretic filtration + lambda_{-1}(E). H01 (PTVV/factorization-homology) upgraded to proposition. E_1-ordered variant PROVED via Shelton-Yuzvinsky. Residual: non-finitely-generated MC4-completion. |
| B | **PROVED unconditional** at coderived; chain-level G/L via MacLane-splitting | `thm:chiral-positselski-7-2` (2026-04-16): counit Omega_X(B_X(C)) -> C iso in D^co_chi(X) for conilpotent chiral CDG-coalgebra with finite-dim graded pieces. 6-step proof. Off-locus UNCONDITIONAL. `thm:chiral-positselski-5-3`: co-contra correspondence. Class G: sigma_Heis via MacLane on Sym(V_{[1]}). Class L (KM non-critical): sigma_KM via PBW + E_2-collapse. Class M chain-level: GENUINELY FALSE direct-sum (S_4 != 0 forces weight-4 bar cohomology); weight-completed PROVED. |
| C | C0 / C1 unconditional on Koszul locus restricted to Heisenberg, affine KM at positive-integer level (TUY) + at boundary admissible level (Arakawa); C1 reflexivity unconditional; C2 Lagrangian CONDITIONAL on BV + Verdier + bar-chart lift + Mok25-log-FM sewing | Post-audit scoped status (2026-04-17 + F07 2026-04-18): (T1) `conj:derived-center-koszul-equivalence` CONJECTURAL (Deligne-Tamarkin); only H^0 naive-centre unconditional (`lem:naive-center-koszul-identification`). Hinich 2001 + GR17 bypasses inscribed as failing (`rem:derived-center-sharpened-scope`). (T2) `prop:perfectness-standard-landscape` UNCONDITIONAL only on the Heis + KM-integer + KM-admissible-boundary lane; generic non-critical KM = `conj:perfectness-boundary-km-generic`; class-M boundary = `conj:perfectness-boundary-class-M`. Weightwise-finiteness → total-finiteness bridge via `prop:conformal-blocks-bar` is IN-PROGRESS (F07 heal). (T3) C1 reflexivity unconditional on Koszul locus. (T4) `rem:plus-three-shift-nonissue` retracts the +3 shift concern; no Verdier pairing at g=0. (T5) C2 hypotheses: BV + Verdier + bar-chart lift + BV-bracket + nondegeneracy + Kontsevich-Pridham transport. (T6) C0 unconditional on Koszul locus. (T7) class-M C2(iii) weight-completed via MC5 pro-ambient. (T8) δ_F_2^cross(W_3) = (c+204)/(16c). (T9) `thm:C-PTVV-alternative` clauses (i)-(ii) genuinely independent via PTVV+HAG-II; Lagrangian clause (iii) CONDITIONAL on Mok25 log-FM chain-level sewing at g≥3. |
| D | **PROVED unconditionally** (uniform-weight, Koszul locus, all g>=1) | obs_g=kappa*lambda_g; multi-weight: +delta_F_g^cross; delta_F_2(W_3) = (c+204)/(16c). 3 prior gaps CLOSED (2026-04-16): (i) virtual-class globalization via K-theory + lambda_{-1}(E) + splitting `ch_g(lambda_{-1}(E)) = c_g(E)`; (ii) Faltings retargeted to Arakelov 1974 + Faltings 1984 s2 + Soule 1992 Ch.III; (iii) BGS c_1(det E) -> c_g(E) via splitting + scalar-channel linearity. **AP225 resolved**: clutching-uniqueness proposition pins obs_g/kappa = lambda_g uniquely (Graber-Vakil socle). H04 upgraded GENUINELY DISJOINT. |
| H | **PROVED** sharp Hilbert series on Koszul locus; E_1-variant PROVABLE | ChirHoch*(A) concentrated in {0,1,2}; `P(t,q) = HS_{Z(A)}(q) + HS_{ChirHoch^1(A)}(q)*t + HS_{Z(A^!)}(q)*t^2`. Critical k=-h^v excluded. **Step 3 circularity RESOLVED (2026-04-16)** via `thm:pbw-koszulness-criterion` + Shelton-Yuzvinsky + chiral quadratic-Koszul. Three disjoint verifications: Heis (Feigin-Frenkel CE), Vir (Wang BRST/Feigin-Fuks), affine sl_2 (Whitehead+Kunneth). E_1-variant `thm:hochschild-concentration-E1` provable via FM^ord + pure braid OS + ordered Koszul dual. |
| MC1-4 | **PROVED UNCONDITIONAL** at generic parameters (principal class M); MC3 five-family (Baxter RETRACTED) | MC1 universal via Whitehead; MC1 Virasoro g>=2 UNCONDITIONAL via L_0-diagonalization. Feigin-Fuks independent verification. MC2 bar-intrinsic PROVED. **MC3 PROVED five-family on evaluation-generated core** (`mc3_five_family_platonic.tex`, 2026-04-16): asymptotic prefundamentals (type A); reflection-equation Shapovalov (B/C/D); Chari-Moura multiplicity-free l-weights; theta-divisor complement (elliptic); parity-balance (super-Yangian). Baxter retracted as type-A rational artifact. Silent non-coverage (log W, N=2 SCA, cosets, non-rational lattice, roots of unity) in `thm:mc3-full-DK-conjectural`. MC4+ UNCONDITIONAL. MC4^0 UNCONDITIONAL (2026-04-16): SDR via Wakimoto (Vir) / Feigin-Frenkel (W_N). Non-principal hook-type (r<=N-3) PROVED (KRW03, Arakawa07). |
| MC5 | **PROVED on THREE equivalent ambients of original complex** (pro-object / J-adic / weight-completed); direct-sum `Ch(Vect)` genuinely FALSE (ambient artefact) | HS-sewing unconditional. **Chain-level class M PROVED in THREE AMBIENTS (2026-04-17)**: (i) `thm:mc5-class-m-chain-level-pro-ambient` pro-Ch(Vect), strict chain-level qi every g>=0, 4-step (h_N = sum h*m_0^{j-1} -> Mittag-Leffler -> pro-qi); (ii) `thm:mc5-class-m-topological-chain-level-j-adic`; (iii) weight-completed via `thm:completed-bar-cobar-strong`. **Direct-sum falsity is ambient-choice artefact**: S_4(Vir_c) = 10/[c(5c+22)] forces weight-4 cohomology ONLY in bounded-direct-sum; inverse limit IS the original bar complex. 2026-04-17 adversarial Wave 1 closed "chain-level class M original." AP203 HEALED. `c_r = S_r` PROVED. H07 UPGRADED: direct SC^{ch,top} homotopy-Koszulity via Ginzburg-Kapranov + Ass self-duality + Deligne-purity. |
| Koszul | 10+1+1 | 10 unconditional + Lagrangian (conditional) + D-mod purity (one-direction). Equiv (vii) uniform-weight all-genera / multi-weight genus-0 only. Equiv (viii) concentration proved; freeness conditional on Massey vanishing. ALT: proof web (H09). |
| D^2=0 | PROVED | Convolution on universal family over Mbar_{g,n}; ambient Mok25 log FM. |
| Theta_A | PROVED | Bar-intrinsic; all-degree inverse limit (`thm:recursive-existence`). |
| SC-formal | PROVED | SC-formal iff class G. Forward: operadic tower truncation (Delta=0). Converse: shadow tower controls SC ops. ALT: operadic both directions (H11). |
| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3. Betagamma d_alg=2 witness on standard conformal-weight line. Impossibility of 3 via MC relation + shadow Lie Jacobi. ALT: representation-theoretic (H10). |
| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g))=g; total dim=dim(g)+2 (`prop:chirhoch1-affine-km`). |
| Topologization | **PROVED on original complex for G/critical; PROVED Q_{tot}-cohomological for L; PROVED weight-completed for M** (`thm:topologization-tower`; post-Wave-1 Beilinson audit 2026-04-17 identifies THREE open directions, not one) | (1) G (Heis): E_3^top on original complex unconditional (Dunn on F^{H_k}); (2) L (V_k(g), k!=-h^v): E_3^top ON Q_{tot}-COHOMOLOGY via `thm:E3-topological-km` + `thm:iterated-sugawara-construction` (Sugawara identity T_Sug=[Q_tot,G_Sug] proved in H^•(A^{BV}_{3d},Q_tot); STRICT CHAIN-LEVEL UPGRADE via explicit η_1 antighost-contact is a FRONTIER item; draft candidate formulas in Vol II e_infinity_topologization.tex:401-411 RETRACTED 2026-04-17 pending independent verification); (3) C: E_3^top via FMS bosonization to Heis; (4) M: weight-completed chain-level E_3^top via half-BRST + MC5 pattern; (5) critical k=-h^v: E_2^top (not E_3; Sugawara collapse is a dimension drop). THREE OPEN DIRECTIONS: (I) class M original complex in Ch(Vect); (II) class L strict chain-level (requires [Q,tilde G_1]−T_Sug identically zero in bulk BV chain, not merely Q-exact); (III) antighost BRST-commutativity [G^(n),G^(m)]=Q-exact at spin n,m≥3 (postulated as axiom T5 of def:higher-spin-stress-tower, not derived). ALT H08 no longer conjectural for G/C and M-weight-completed. |
| E_3 identification | **PROVED simple g, affine KM V_k(g) at generic non-critical level** via `thm:e3-identification` in `en_koszul_duality.tex:5346`; gl_N noted at remark level in `rem:e3-non-simple-gl-N`:5584 (2-parameter B_tr + B_ab from Sym^2(gl_N^*)^{gl_N}); general non-simple case `rem:e3-non-simple`:5549 only addresses Sym^2(g^*)^g biderivation count (N = r + C(dim z+1, 2)); semisimple / reductive / nilpotent (Heisenberg) / solvable cases UNINSCRIBED as theorems — previously-advertised labels `prop:e3-gl-N`, `thm:e3-identification-semisimple`, `thm:e3-identification-reductive`, `prop:e3-heisenberg`, `thm:e3-identification-solvable` are AP255 phantoms (grep all three volumes, zero hits). Chain-level qi-model via Fresse Vol II cited at citation level only; comparison diagram between E_3-algebraic and E_3-topological not inscribed. CY_4 p_1-twisted cross-references a PROVED-NEGATIVE row (pi_4(BU)=Z is obstruction group, not positive structure). | Z^der_ch(V_k(g)) ~= A^lambda as E_3-deformation family over lambda H^3(g)[[lambda]]. Honest strengthening count: 1 inscribed theorem (simple g base) + 2 remark-level (gl_N + general non-simple biderivation count). |
| Elliptic chiral QG | PROVED leading-order hbar for sl_2 via Felder R + KZB + Fay trisecant | theta_1'/theta_1 propagator (NOT Weierstrass zeta). Heat prefactor 1/(4*pi*i) diag, 1/(2*pi*i) off-diag. |
| CY_4 p_1-twisted | **CONSTRUCTED + CONJECTURED** (Vol III `cy_to_chiral.tex:4502-4700`, construction of p_1-twisted family + `conj:cy4-p1-family-associator-sextic` verified only at the sextic); **PROVED NEGATIVE**: "no native CY_4 Yangian exists" (Vol III `en_factorization.tex:289-299`) since π_4(BU)=Z is a Pontryagin BLOCK-obstruction, not a positive structure | Cocycle candidate c(x,y) = <x ∪ y ∪ p_1(T_X),[X]>/24. K3×K3 N(X)=0 claim UNINSCRIBED (generically false since p_1(K3) != 0). 7d hCS realization CITED (Costello-Gaiotto), not inscribed. Previously-advertised "PROVED as Y_{p_1}(X)" row is RETRACTED: inherits conjectural status of associator-sextic conjecture; the proved-negative row stands separately. |
| Toroidal chiral QG | PROVED formal-disk via DIM + SV CoHA; global P^1xP^1 conditional on class-M chain-level | 2-param RTT; Miki S_3 = Weyl of Omega-background. |
| Chiral QG equiv | **ORDERED base: PROVED on Koszul locus** via `thm:chiral-qg-equiv` at `ordered_associative_chiral_kd.tex:8404` (`\ClaimStatusProvedHere`, title "Chiral bialgebra equivalence on the Koszul locus"; in build via `main.tex:1394`). AP263 Hopf-antipode caveat at `rem:chiral-bialgebra-not-hopf`:8496; GRT_1 torsor content at `rem:chiral-qg-grt1-torsor`:8522. Triangle (I) R-matrix ↔ (II) chiral $A_\infty$ in $\End^{\ch}_\cA$ ↔ (III) chiral coproduct coassociative up to $\Phi$; canonical at $H^0$, non-canonical up to $\GRT_1(\Q)$ at cochain level. LOAD-BEARING on JKL26 at $N \geq 3$ via `prop:ff-screening-coproduct-obstruction` (FF is NOT a drop-in replacement; $(\Psi-1)/\Psi$ obstruction explicit). gl_N extension via `thm:glN-chiral-qg`:10324 (`\ClaimStatusProvedHere`). ELLIPTIC + TOROIDAL formal-disk: standalone-only at `seven_faces.tex:1006,1020`; `seven_faces.tex` NOT `\input`-ed into `main.tex`, so chapter-level inscription is FRONTIER. | Of 8 formerly-advertised strengthening labels: 1 inscribed theorem (`thm:glN-chiral-qg`), 1 inscribed remark absorbing intended content (`rem:chiral-qg-grt1-torsor`), 6 AP241 phantoms with ZERO live consumer `\ref` after 2026-04-18 retarget (`def:ordered-koszul-chiral-algebra`, `prop:yangian-ordered-koszul`, `thm:chiral-qg-equiv-ordered`, `prop:sl2-yangian-triangle-concrete`, `thm:w-infty-chiral-qg-completed`, chapter-level elliptic/toroidal). `\phantomsection\label{thm:grt1-rigidity}` stub at preface retired 2026-04-18. Concrete verification of triangle BEYOND sl_2 Yangian + affine KM + gl_N is OPEN. |
| Non-principal W | **Koszulness at generic level PROVED for every nilpotent** via Arakawa Kazhdan filtration (Inventiones 2007); **hook-type $r \leq N-3$ is the MC1 semisimple-Levi window, NOT a Koszulness window** — prior conflation healed 2026-04-17. Hook-type parabolic screening CONDITIONAL at theorem level — `thm:n4-non-principal-hook` in `standalone/N4_mc4_completion.tex` has proof sketch only, no `\ClaimStatus` tag; downgrade to `\ClaimStatusConjectured` or full proof inscription pending. Subregular/minimal/screening-kernel preservation UNINSCRIBED at theorem level for general N. BP = W^k(sl_3, f_{(2,1)}) is OUTSIDE hook corridor (r ≤ 0 for sl_3) and analysed directly via `thm:w-bp-strict` + `thm:bp-koszul-conductor-polynomial`. | Log W(p) Massey <Omega,Omega,Omega> EXPLICIT CLAIM RETRACTED: keyword "Massey" absent from `logarithmic_w_algebras.tex`; Gurarie 1993 + Flohr 1996 give UNBOUNDED Massey in H^•_log — falsifies naive "C_2-cofinite ⟹ bounded Massey ⟹ tempered" implication (B91) in logarithmic sector. Open problem: shadow-tower triple Massey in H^•_reg(B(W(p))) (distinct from logarithmic sector, unboundedness there already known); sharpest target p = 3. |
| gl_N chiral QG | **UNCONDITIONAL at N=2 via sl_2 Yangian + affine sl_2 RTT + SV CoHA; N ≥ 3 CONDITIONAL on JKL26 vertex bialgebra on Jordan quiver CoHA (Argument B)**, with Feigin-Frenkel screening descent **PROVED OBSTRUCTED** at explicit $(\Psi-1)/\Psi$ cocycle (`prop:ff-screening-coproduct-obstruction` at `ordered_associative_chiral_kd.tex:10177`). Bialgebra level only; full Hopf lift is PROVED NEGATIVE per AP263 (`rem:chiral-bialgebra-not-hopf`:8497). Inscribed at `thm:glN-chiral-qg`:10324 (`\ClaimStatusProvedHere`). | Prior row "UNCONDITIONAL all N≥2 via Feigin-Frenkel screening (JKL26 phantom eliminated)" RETRACTED per AP256+AP271+AP305 healing 2026-04-18. Argument B theorem body explicitly names JKL26 as external input at N ≥ 3 (`:10517-10519`). FF-obstruction cocycle $[Q_{\alpha_i},\Delta_z^{\mathfrak h}]$ has coefficient $(\Psi-1)/\Psi$ matching `thm:miura-cross-universality`; vanishes only at $\Psi=1$ (free-boson). Lemma `qdet-central-all-N`:10675 carries `\ClaimStatusProvedElsewhere` — centrality inherited from Molev (Thm 1.6.4 + 1.11.2) via antisymmetriser-image argument. Decreasing-column ordering load-bearing at N ≥ 3 (`rem:qdet-decreasing-ordering`:10727); increasing fails at Ψ^2. Two-param gl_N RTT matches `rem:e3-non-simple-gl-N` with $\dim\Sym^2(\mathfrak{gl}_N^*)^{\mathfrak{gl}_N} = 2$ (trace + trace-of-trace). $\Psi=0$ (identity QG) and $\Psi=1$ (free boson) inscribed as degenerate/coincidence points. |
| Verlinde recovery | PROVED | Z_g = sum S_{0j}^{2-2g} from ordered chiral homology at integer level. |
| ker(av) formula | PROVED (all simple g) | dim(ker(av_n)) = d^n - C(n+d-1,d-1) for d-dim rep. |
| Genus-2 construction | CONSTRUCTED | KZB 2x2 Siegel period matrix, chi=-12 at degree 2, doubly-dynamical (`conj:g2-ddybe`). |
| Miura coefficient | PROVED (`thm:miura-cross-universality`) | (Psi-1)/Psi on J(x)W_{s-1}+W_{s-1}(x)J ALL spins s>=2. Three-step; spins 2-6 verified, 142 tests. |
| Z_g closed forms | DISCOVERED g=0..9; PROVED all g via Hurwitz-Bernoulli; arithmetic duality at {691, 3617} through r=11 | P_g(n) = n^{g-1}(n^2-1)*R_{g-2}(n^2), n=k+2. Leading = B_{2g-2}/(g-1). Kummer-congruence predictions (691 at Z_7, 3617 at Z_9) falsification tests. `thm:z-g-s-r-arithmetic-duality`: leading Kummer-irregular primes {691, 3617} present on Z_g AND absent on S_r(Vir_c) through r=11. Characteristic S_r primes {61, 193, 2111, 16657, 3988097}. **2026-04-17 retraction**: primes 1423, 3067, 23, 43, 419 NOT Kummer-irregular (regular at primary source); they are Riccati-arithmetic in S_r numerators. Corrected Tier-3: {37, 691, 811}. |
| W_N Stokes count | DISCOVERED | Stokes rays for W_N KZ = 4N-4 (linear in N). W_2: 4. W_3: 8. Poincare rank = 2N-2. |
| Shadow = GW(C^3) | IDENTIFIED | Shadow tower at kappa=Psi produces perturbative constant-map GW free energies F_g^{GW,const}(C^3). MacMahon M(q) on DT side via MNOP. |
| Conformal anomaly | QUANTIFIED | Obstruction to constant coproduct = c/2 = kappa(Vir_c). At c=0: obstruction vanishes. At c!=0: spectral parameter FORCED. |
| Chiral Higher Deligne | **PROVED (Vol II `chiral_higher_deligne.tex`, 2026-04-16)** | `thm:chiral-higher-deligne`: Z^{der}_ch(A) universal E_3-chiral acted on by SC^{ch,top} via heptagon (3)<->(4)<->(5). `thm:H-concentration-via-E3-rigidity`: Thm H concentration CONSEQUENCE of E_3-rigidity + PBW. `thm:chd-ds-hochschild`: ChirHoch^bullet(W_k(g)) ~= H^bullet_DS(ChirHoch^bullet(V_k(g))) chain-level E_2-chiral Gerstenhaber. `cor:universal-holography-class-M`. |
| Curved-Dunn H^2=0 at g>=2 | **PROVED (Vol II `curved_dunn_higher_genus.tex`, 2026-04-16)** | `prop:modular-bootstrap-to-curved-dunn-bridge`; `prop:genus1-twisted-tensor-product` Gauss-Manin + Arakelov; `thm:curved-dunn-H2-vanishing-all-genera`; `thm:irregular-singular-kzb-regularity`: Jimbo-Miwa replaces KZ Stokes. |
| SC^{ch,top} heptagon | **PROVED (Vol II `sc_chtop_heptagon.tex`, 2026-04-16)** | Five classical faces + face (6) Drinfeld-centre `Z(Rep_fact(A)) ~= Rep_fact(Z^der_ch(A))^{E_2}` via half-braiding + face (7) derived-AG via PTVV on `Map(X x R_{>=0}, B SC-Alg)`. Seven edge theorems close heptagon. SC^{ch,top} is GENERIC; topologization at affine KM non-critical proved; general conjectural. |
| Universal celestial holography | **PROVED chain-level (Vol II `universal_celestial_holography.tex`, 2026-04-16)** | `thm:uch-main`: SC^{ch,top} on `(A^cel, Z^der_ch(A^cel))` + celestial OPE = chiral factorization homology on `P^1_cel` + shadow-tower = soft-factor hierarchy. Coverage: self-dual gauge (KM), gauge+matter (DS), gravity (Vir + w_{1+inf}), YM (Beem-Rastelli). Chain-level class M at g>=1 open `conj:uch-gravity-chain-level`. |
| Periodic CDG admissible KL | **PROVED (Vol I `periodic_cdg_admissible.tex`, 2026-04-16)** | `thm:periodic-cdg-is-koszul-compatible`: `F^n = ker(Q^n_{adm})` on `KL_k^{adm}` at `k+h^v = p/q` compatible w/ chiral Koszul. `thm:admissible-kl-bar-cobar-adjunction`: `Omega^ch |- B^ch` descends unconditionally. `cor:class-M-admissible-minimal-model`: `KL^{adm}_{Vir}(c_{p,q})` has `(p-1)(q-1)/2` simples, all finite-length. Closes sole remaining irreducible-open frontier. |
| E_infty-Topologization | **PROVED (Vol II `e_infinity_topologization.tex`, 2026-04-16)** | `thm:iterated-sugawara-construction`: tower `{T^{(n)}}_{2 <= n <= N+1}` each inner w/ BRST primitive G^{(n)}. `thm:e-infinity-topologization-ladder`: k inner stress tensors => E_{k+2}-top via Dunn. Vir -> E_3-top; W_N -> E_{N+1}-top; W_infty -> E_infty-top (Platonic endpoint). `thm:operadic-spiral`: infinite bidirectional spiral. **Climax restatement:** 3d quantum gravity Vol II Part VI is N=2 shadow of 3d+infty topological. |
| Theorem A^{infty,2} | **PROVED (Vol I `theorem_A_infinity_2.tex`, 2026-04-16)** | `thm:A-infinity-2`: Francis-Gaitsgory bar-cobar (infty,2)-equivalence at properad level. `B-bar^ch_X : Fact^{aug}(X) <-> CoFact^{conil,comp}(X) : Omega^ch_X` (infty,2)-adjoint on conilpotent-complete. Three clauses: (i) properad lift via Hackney-Robertson; (ii) pole-free restriction recovers LV12 (Ass, Ass^!); (iii) R-twisted Sigma_n-descent relates B^{ord}(A) to B^Sigma(A). 14+ corollaries. `cor:chiral-KK-formal-smoothness`. |
| CY-D dimension stratification | **PROVED (Vol III `cy_d_kappa_stratification.tex`, 2026-04-16)** | `thm:kappa-hodge-supertrace-identification`: `kappa_ch(A_X) = sum_q (-1)^q h^{0,q}(X)` unconditional compact CY_d via HKR + Mukai + HC^-_d trace. `thm:kappa-stratification-by-d` d in {1,...,5}: E(0), K3(2), abelian/bielliptic(0), quintic/K3xE/E^3(0), local P^2(3/2), CY_4 sextic(2), CY_5 generic(0). `cor:conifold-non-local-surface`: conifold NOT local surface; kappa_ch=1 via McKay. `thm:borcherds-weight-kappa-BKM-universal`: kappa_BKM(Phi_N) = c_N(0)/2 universal N in {1,2,3,4,6}. |
| BP Koszul-conductor polynomial identity | **PROVED IN ARAKAWA CONVENTION** (Vol I `standalone/bp_self_duality.tex`, 2026-04-16) | `thm:bp-koszul-conductor-polynomial`: Arakawa `c(BP_k) = 2 - 24(k+1)^2/(k+3)`, `K_BP(k) := c(BP_k) + c(BP_{-k-6}) ≡ 196 ∈ Q(k)`. Fixed k=-3 coincides with critical -h^v(sl_3); `kappa(BP_{-3}) = 49/3` principal-value limit. 73+7 tests + 2 disjoint decorators. **Vol II cross-check (2026-04-17)**: FL convention `c^{FL}(k) = -(2k+3)(3k+1)/(k+3)` gives meromorphic `K^{FL}_BP(k) = -12(k+3) - 48/(k+3)` w/ pole at k=-3 -- NOT polynomial. Both parametrize SAME BP via level reparametrization; polynomial-identity is Arakawa-specific. |
| Critical level jump | PROVED | At k=-h^v: kappa=0, monodromy trivial, H^1 doubles (4->8), Koszulness fails, bar H* = Omega*(Op_g^v(D)). 72 tests. |
| Genus-2 degree decomp | PROVED | CB_{2,2}(k) = 2k(k+1)(k+2)/3 (cubic). k=1: 4. Singlet+triplet channels (`prop:g2-conformal-block-degree`). |
| Antipode non-lifting | PROVED (negative) | S(T(u))=T(u)^{-1} does NOT lift to vertex-algebraic antipode. Two obstructions (OPE and Hopf axiom). |
| DS intertwining | VERIFIED | (pi_3 x pi_3) circ Delta_z^{sl_3} = Delta_z^{W_3} circ pi_3 verified 57 tests. Spectral coassociativity uses shifted parameters. |
| bar H^2 sl_2 | FIXED | Correct chiral bar h_2=5 (prior 6 was CE/Riordan). Orlik-Solomon form factor. |
| Quantum det ordering | FOUND | Central qdet uses DECREASING column index. At N=3, increasing-index NOT central. 74 tests. |
| E_3 via Dunn | PROVED (alt) | `prop:e3-via-dunn`: CG factorization E_1^top x E_2^hol + Sugawara + Dunn = E_3^top. Independent of HDC. |
| E_3 for gl_N | EXTENDED | Two independent bilinear forms B_tr, B_ab. |
| 6d hCS defect | PROVED | Codim-2 defect on C sub C^3: boundary algebra = W_{1+inf} with Psi=-sigma_2. c=1 (Sugawara). N_{C/Y}=C^2 gives spectral params. 48 tests. |
| DDYBE face model | **NUMERICAL EVIDENCE + CONJECTURED at generic Omega** (Vol I `genus_2_ddybe_platonic.tex`, 2026-04-16) | Face-model bypasses vertex-IRF. Tolerance ladder T1(10^{-12})/T2(10^{-10})/T3(10^{-6})/T4(10^{-4}). Generic-Omega DDYBE: 5 tests at T4; diagonal-Omega factorization exact via two genus-1 DYBE copies (T3); separating degeneration AP157-empty. 29 face-model tests. `conj:g2-ddybe` remains ClaimStatusConjectured -- finite-hbar commutativity of doubly-dynamical Casimirs is residual conjecture. Szego three-term identity (Fay 1973 Cor. 2.5) holds all g>=0. |
| Drinfeld center Heis | VERIFIED | `conj:drinfeld-center-equals-bulk` for H_k: 5 invariants at 6 levels. Naive dim 1 vs derived dim 3. 72 tests. |
| Toroidal coproduct | CONJECTURED | `conj:toroidal-two-param-coprod`: Delta_{z,w}(T(u,v)) = T(u,v) (x) T(u-z, v-w). Miki equivariance. 5-step. |
| Coderived E_3 | PARTIAL | Steps 1-2 proved (D^co stable infty-cat; obstruction coacyclic). Step 3 open. |
| KZB flatness | VERIFIED | d_tau(wp_1) = (1/(4*pi*i)) d_w(wp + wp^2) at machine precision. Prefactor 1/(4*pi*i) diagonal vs 1/(2*pi*i) off-diagonal. |

## XVIII. Anti-Patterns by Topic

### Epistemic
- **AP2/AP4/AP17:** Read actual .tex proof; ClaimStatus tag != ground truth; audit every new theorem IMMEDIATELY before building next result.
- **AP11/AP13/AP28/AP38:** Single-point external dependency -> flag in concordance; forward references transparent about genus/level/type; no undefined terminological qualifier in 3+ locations; literature values carry source paper AND convention (DVV != Eichler-Zagier).
- **AP15:** E_2* is quasi-modular. Genus-1 propagator IS E_2*. Graph sums produce {E_2*, E_4, E_6}.
- **AP26/AP37:** Fock != BPZ for weight>=4, rank>=3 W-algebras. SS page from FULL differential, not pole-order heuristics. Lie homology != Hochschild homology.
- **AP35/AP41/AP42/AP43:** False proof + true conclusion -> two cancelling errors, fix BOTH. Prose mechanism != mathematical mechanism. State level of validity explicitly. Central object without `\begin{definition}` -> property list is conjecture.
- **AP39:** kappa != S_2 for non-Vir. Coincide only rank-1. Heis kappa=k; Vir kappa=c/2; KM kappa=dim(g)(k+h^v)/(2h^v).
- **AP47/AP60:** Evaluation-generated core != full category (MC3 proved on eval core, DK-4/5 downstream). Tag only genuinely new content ProvedHere; classical parts ProvedElsewhere.
- **AP147/AP149/AP150:** Circular proof routing -> insert ROUTING REMARK citing primitive anchor. Resolution propagation atomic (concordance, preface, intro, standalones, theorem status, label prefixes, other volumes). Agent confabulation: every claimed arrow needs independent theorem reference.
- **AP155/AP157:** "New invariant" overclaim: architectural novelty != computational novelty; check Bernard/Felder/Etingof-Varchenko/Calaque-Enriquez-Etingof. Degeneration-dependent "invariants" require degeneration-independence proof; separating degeneration of g=2 has ZERO genuinely g=2 info.

### Computational
- **AP3/AP10/AP61:** Compute independently. NEVER pattern-match. Every hardcoded expected value requires comment citing 2+ independent derivation paths.
- **AP6/AP7/AP8/AP14/AP18:** Specify genus/degree/level (convolution vs ambient) for D^2=0, kappa, Theta_A. Before universal quantifier verify no implicit restriction. NEVER "self-dual" unqualified (Vir self-dual c=13). Koszulness != SC formality; Koszul = bar H* in degree 1; SC formal = m_k^{SC}=0 k>=3; all standard families Koszul, only class G SC-formal. "Entire standard landscape" -> list every family.
- **AP29/AP31/AP33:** H_k^! = Sym^ch(V*) != H_{-k} (same kappa, different algebras). delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree independent. F_1=0 does NOT imply F_g=0.
- **AP30/AP36:** CohFT flat identity requires vacuum in V. "implies" proved vs "iff" claimed -> write "implies" until converse has independent proof.
- **AP59/AP62/AP63/AP64:** Three invariants: p_max(OPE pole) != k_max(collision depth=p-1) != r_max(shadow depth); betagamma: p=1, k=0, r=4. "Depends only on dim(g)" = Euler char only. CE(g_-) != chiral bar for multi-gen; Orlik-Solomon form factor; sl_3 chiral H^2=36 vs CE H^2=20. CE weight vs PBW degree different sequences; specify grading.
- AP66-80 (specialized computational): free-field GFs NOT D-finite, interacting ARE (AP66); strong gen != FREE strong gen, W(p) has 4, FREE strong gen OPEN (AP67); PVA slab ghost c != kappa; SVir kappa=(3c-2)/4; Sigma_0=13>Sigma_1=41/4>Sigma_2=1>Sigma_4=0 (AP68); tau_shadow = kappa-deformed KdV, standard KdV only kappa=1 (AP69); shadow L^sh has POLES s=1,2; F_g <-> L^sh(1-2g) FAILS (AP70); shadow kappa != Dyson beta; c=13 kappa=6.5 (AP71); W-algebra NOP bar d^2 != 0 (AP72); BV=bar PROVED G/L, CONDITIONAL C/M (AP73); false Bernoulli-Dirichlet identity (AP74); Koszulness = PBW degree concentration NOT conformal weight (AP75); Y_{1,1,1} c=0, kappa=Psi NOT c=3 (AP76); Stokes ratio on convergent spurious; use direct Pade (AP77); never conjecture from number-theoretic coincidences (AP78); W(p) has 4 generators T + sl_2 triplet, not 2 (AP79); engine without test file -> verify BOTH exist (AP80).
- AP133: Catalan index shift. C_n counts binary trees with n+1 leaves (n internal nodes).
- AP135: q-expansion coefficients. 1/eta(tau)^r has r-coloured partition numbers p_{-r}(n). r=2: (1,2,5,10,20,...). OEIS lookup before hardcoding.
- AP140: Koszul conductor vs local constant. K=c+c' is GLOBAL invariant. K_BP=196, not 2.
- AP143: DS ghost charge background shift omission. c_ghost(N,f,k) = c(sl_N,k) - c(W_{N,f},k); simplified N*(N-1) OMITS background charge. At N=7: 1722 vs 42. Compute c(sl_N,k) - c(W_{N,f},k) directly from Fateev-Lukyanov.
- AP178: S_4 large-c asymptotic. 10/[c(5c+22)] ~ 2/c^2 at large c, NOT 2/(5c^2).

### Empirical (AP116-AP187)
- **AP116-123 (numerics & LaTeX hygiene):** sum_{j=a}^{b} substitute smallest index (AP116); connection 1-form = r(z)dz NOT d log, Arnold d log(z_i-z_j) is bar coefficient (AP117); (Im Omega)^{-1} scalar g=1, matrix g>=2 (AP118); before Borel verify Gevrey-1; Gevrey-0 => direct Pade (AP119); Cauchy = 1/(2*pi*i), F_1=kappa/24 (AP120); NO Markdown in LaTeX (AP121); test tolerance RELATIVE (AP122); combinatorial counts verified BEFORE hardcoding; genus-2 stable graphs=7 (AP123).
- **AP129-139 (object/grading hygiene):** ratio a/b transcription error b/a (AP129); fiber dtau in H^{1,0}(E_tau) != base c_1(lambda) in H^2(M-bar_g) (AP130); d_gen (finite) != d_alg (inf for Vir) (AP131); B(A)=T^c(s^{-1} A-bar) (AP132); amplitude [0,2] != vdim (AP134); c_{bg}(lambda)=2(6*lambda^2-6*lambda+1) vs c_{bc}(lambda)=1-3(2*lambda-1)^2, c_total=0 at each lambda (AP137); [m,[m,f]]=(1/2)[[m,m],f] requires ||m|| ODD (AP138); every variable in displayed eqn quantified, LHS superset RHS (AP139).
- **AP144-156 (convention & scope):** multiple conventions -> BRIDGE IDENTITY at every site (AP144); restructuring = O(N) debt; grep all three volumes (AP145); after 100+ agent campaigns expect straggler commit (AP146); convention clash in single file (hbar with/without pi*i); grep definitions (AP151); "ordered" on curve = LABELED non-coinvariant, NOT totally ordered (AP152); E_3 scope inflation: HDC needs B^Sigma(A) E_2-coalgebra; E_inf input -> E_3; E_1 input -> only E_2 (AP153); two E_3 structures (algebraic HDC vs topological Sugawara); topological PROVED affine KM, CONJECTURAL general (AP154); wp_1 conventions (theta_1'/theta_1 vs Weierstrass zeta_tau) DIFFERENT monodromy (AP156).
- **AP177-187 (Beilinson-era):** S_2=c/12 lambda-bracket confusion; shadow invariant S_2=kappa=c/2 (AP177); cross-volume shadow bridge S_2^{VolI}=6*S_2^{lambda-bracket} (AP180); pi_3(BU)=0 (Bott), NOT Z (AP181); kappa_ch=chi(S)/2 only for Tot(K_S->S); conifold NOT local surface (AP182); McKay quiver Z_3 = 3 oriented 3-cycles NOT K_{3,3} (AP183); excision=gluing (B_L (x)_A B_R), coproduct=splitting (plain (x)) (AP184); pi_4(BU)=Z is obstruction GROUP NOT guarantee (AP185); coincidental agreement masks bugs ((Psi-1)/Psi=1/Psi at Psi=2; verify at 3+ parameters) (AP186); Miura from T(u)=prod(u+Lambda_i) -> psi_s=e_s; coefficient :J*W_{s-1}: is 1/Psi all s>=2 (AP187).

### Operadic-Structural
- **AP25/AP34/AP50 (four functors):** B(A)=coalgebra; D_Ran(B(A))=B(A!)=algebra; Omega(B(A))=A (INVERSION); Z^der_ch(A)=bulk. D_Ran=VERDIER; bulk=HOCHSCHILD. A^!_inf (Verdier, chain) != A^! (linear, strict). NEVER "bar-cobar produces bulk."
- **AP65/AP81-85/AP88/AP103/AP104 (operadic):** B_P(A)=P^!-coalgebra != BP=cooperad. Three coalgebras: Lie^c (Harrison/coLie), Sym^c (coshuffle, 2^n terms), T^c (deconcatenation, n+1 terms). Factorization coproduct (Sym^c on Ran) != deconcatenation (T^c on ordered); R-matrix descent relates. B_{Com}(A) is coLie, not cocommutative. P^i=cooperad != P^!=(P^i)^v=operad. Cotriple bar != operadic bar.
- **AP86/AP87/AP89-93 (SC/promotion):** B_{SC}(A) for one-colour ill-formed; SC two-coloured; promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A) + mixed sector. SC mixed-sector dim=(k-1)!*C(k+m,m). FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation. Two curvatures: mu_0 (algebra, g=0) vs d_fib^2=kappa*omega_g (fiberwise, g>=1).
- **AP94-98/AP100/AP102 (shadow/Hochschild):** ChirHoch*(Vir_c) degrees {0,1,2}. ChirHoch != Gelfand-Fuchs. Shadow algebra has graded Lie bracket NOT ring. av g^{E_1}->g^mod LOSSY; deg 2 recovers kappa abelian/scalar; non-abelian KM gives kappa_dp + dim(g)/2 Sugawara shift. C0 fiber-center; C1 Lagrangian eigenspace; C2 shifted symplectic/BV conditional. Scalar kappa+kappa'=rho*K from C1 + Theorem D.
- **AP99/AP101/AP127/AP128:** K11 Lagrangian CONDITIONAL (perfectness + bar-cobar normal-complex). "qi not merely iso on cohomology" tautological. Migrating `\input{chapter}`: add `\phantomsection\label{}` stubs for EVERY label. Engine-test sync to wrong value -- NEVER update tests from engine output; derive INDEPENDENTLY.
- **AP142:** Local-global conflation on curves. "Koszul duality over point = over P^1" FALSE. Three errors: (a) HOMOTOPY RETRACT IS DATA; (b) DISK != POINT; (c) A^1 ALREADY HAS ARNOLD RELATIONS. Specify WHICH space, COMPARISON DATA, on-the-nose vs extra-structure.
- **AP159-164 (Yangian / Hochschild / E_1-chiral / E_3 scopes):** Four Yangian types (classical E_1-top R; dg-shifted point/disk; chiral E_1-chiral on X D-mod; spectral on A^1_u) -- use ^{ch}/^{dg} superscripts (AP159). Three Hochschild by geometry: Top HH E_1->E_2 Deligne; Chiral ChirHoch E_inf-chiral->{0,1,2} Thm H; Categorical dg cat -> E_2 w/ CY shifted Poisson (AP160). Five E_1-chiral notions NOT interchangeable; each own derived center; (B)<->(C) Koszul locus only (AP161). E_3 requires (a) conformal vector, (b) non-critical level, (c) T(z) Q-exact; PROVED affine KM, CONJECTURAL general (AP162). "Lives on R x C" unjustified for E_1-chiral (AP163). Chiral Gerstenhaber != topological: OPE residues on FM_k(C) vs little 2-disks (AP164).
- **AP169-175 (SC/associator/Yangian/QG):** SC^{ch,top} is GENERIC case; E_3 is special; most chiral algebras lack conformal vector (AP169). Two Yangian definitions (weaker E_1-factorization+RTT vs stronger (A, S(z), Delta^{ch}, {m_k}) + modular MC tower); equivalence OPEN (AP170). Associator dichotomy: cohomological derived center ASSOCIATOR-INDEPENDENT; cochain-level ASSOCIATOR-DEPENDENT. Bar-side (kappa, shadow) associator-FREE; cobar/coproduct depend on Phi (AP171). A^! is SC^!-algebra = (Lie Sklyanin, Ass), NOT SC-algebra (AP172). Z^{der}_{ch}(Y(g)^{ch}) NOT computed; predicted infinite-dim; E_1 input only E_2 (AP173). Chiral QG equiv: abstractly on Koszul locus; concrete only sl_2 Yangian + affine KM (AP174). Pentagon of equivalences is a STAR; five SC presentations through operadic hub (AP175).
- **AP176 (CONSTITUTIONAL):** "arity" BANNED. "Degree" universal for bar grading, operadic input count, tree vertex valence, Stasheff identity level, SC mixed sector params. NEVER reintroduce. Grep `grep -rn '\barity\b' chapters/ appendices/ standalone/` must return ZERO.
- **AP179:** Graph vertex valence context-dependent. Graph: "degree"; operad: "valence" (NOT "arity").

### Label / Prose / Scope
- AP5: Grep ALL THREE volumes for variants after EVERY correction.
- AP12: When proving a claim, grep entire manuscript for variants. Update same commit.
- AP40: Environment matches tag. Conjectured -> `\begin{conjecture}`. ProvedElsewhere -> theorem + Remark attribution.
- AP105: Heis = abelian KM = abelian CS boundary. SAME OPE J(z)J(w)~k/(z-w)^2. Simple-pole needs ODD generator (symplectic fermion).
- AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
- AP108: Heis = CG opening, NOT atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
- AP106/AP109/AP111: NEVER "This chapter constructs..."; NEVER list results before proving; no "What this chapter proves" blocks. Open with deficiency.
- AP110: Each volume's preface tells its OWN story; cross-volume in delineated subsections.
- AP112: Never trust stale page counts. Verify against fresh builds.
- AP113: Vol III bare kappa. See HZ-7.
- AP114: Stub chapters (<50 lines, no theorems) -> develop or comment out.
- AP115: Architectural CLAUDE.md claims must be enacted in .tex. Metadata-source gap is most dangerous AP.

**Prose laws**: no AI slop; no hedging where math clear; no em dashes; no passive-voice hedging; every paragraph forces next; state/prove once; scope always explicit; prior work = one sentence per paper.

### 732-Agent Adversarial Campaign (AP186-AP236)

Full catalogue: `compute/audit/new_antipatterns_wave12_campaign.md`.

**AP186-210 (specialized):** ProvedHere-no-proof-block; orphaned chapters; empty sections; dead labels; hidden imports (119 findings); circular proof chains; scope inflation statement-vs-proof; biconditional forward-only; curved complex with flat tools (45); five-object conflation (47); SC misattribution non-formula; bare Hochschild (89); Whitehead lemma semisimple-only; strong filtration inequality direction; transfer theorem gap; Baxter not vacuous at lambda=0; coderived element-wise invalid; class-M harmonic unproved; genus-0 boundary contradiction; reflexivity hidden in duality; object switch mid-proof (Verdier != cobar); Theorem A Verdier algebra/coalgebra flip; missing lemma cited; topologization chain-level vs cohomological.

**AP211-224:** test file absent (219); TODO/FIXME unresolved; stub chapter false coverage; cross-volume bridge outdated; preface advertising stronger than proved; Koszul (vii) genus-0 scope; Koszul (viii) ChirHoch freeness overclaim; SC-formality restricted to metric families; depth-gap d_alg=2 wrong line; D^2=0 wrong geometric space; Gerstenhaber single insertion; Theorem H config-space collapse unjustified; Theorem H bar-coalgebra/Koszul-dual conflation; README scope inflation.

**AP225-233 (deep structural):** AP225 (CRITICAL) genus-universality gap (NOW RESOLVED via clutching-uniqueness proposition, see Theorem D row); AP226 K_0-class vs scalar (use Chern character); AP227 ProvedHere forwarding ("By Theorem X" is ProvedElsewhere); AP228 anomaly-Koszul dependency inversion; AP229 SC-formality propagation debt (Vol III stale); AP230 genus-1 sufficient claimed all-genera; AP231 draft artifacts in theorem statements; AP232 duality clause overclaiming family scope; AP233 compact/completed comparison gap MC3.

**AP234-235 (preface rectification 2026-04-17):**
- **AP234: Two-Koszul-conductors-same-letter.** kappa(A)+kappa(A^!) (scalar complementarity, family-dependent: 0/13/250/3/98/3) is DISTINCT from the Trinity K(A)=c+c^!=-c_ghost(BRST) (-k/2*dim(g)/26/100/196). Relation: kappa+kappa^!=rho_A*K with rho_N=H_N-1 for principal W_N, rho_KM=rho_free=0, rho_BP=1/6. The equation kappa+kappa^!=K (bare, no rho) is FALSE for every standard family. Canonical K-values in `universal_conductor_K_platonic.tex:795-821` and `higher_genus_complementarity.tex:3015-3120`. Grep trigger: any `K(Vir)=13` or `K=250/3 for W_3`. Cross-check K at self-dual c=13 -- correct is K=26, not 13.
- **AP235: quaternitomy/quadrichotomy drift.** "Quadrichotomy" is canonical (matches `thm:quadrichotomy`, `chap:shadow-quadrichotomy-platonic`); "quaternitomy" is an invented hybrid that drifts across preface, working_notes, part-introductions. Grep `quaternitomy` after any write naming the G/L/C/M partition.

**AP236 (bar_construction.tex rectification 2026-04-17):** Blacklist-slug leakage into typeset parenthetical. `/B\d+` identifiers from the Wrong-Formulas Blacklist leak into manuscript `\textup{(}...\textup{)}` annotations (e.g. `\textup{(}/B49; treated in Chapter~X\textup{)}`). Reader sees non-existent citation; slug rots with every renumbering. Constitutional hygiene violation. Grep `\\textup\{\(\}\s*\/B\d+|(\s*\/B\d+;` before every commit touching `.tex`. Healing: delete the slug; keep only the mathematical cross-reference. Companion: orphaned `\textup{(}\textup{)}` empty parentheticals left behind when a macro-resolved reference is deleted between the delimiters -- grep `\\textup\{\(\}\\textup\{\)\}`.

## XIX. Failure Mode Awareness (GPT-5.4 / Opus 4.6)

Model-specific recurrent patterns from ~100+ agent invocations across three volumes.

**Formula drift.** FM1 (generic-formula reach: bare Omega/z; counter: substitute k=0 first). FM2 (level-prefix dropping on summarisation; counter: re-Read verbatim). FM3 (c_bg vs c_bc swap; counter: substitute lambda=2 AND lambda=1). FM9 (H_{N-1} vs H_N-1 at N=2: H_1=1 vs H_2-1=1/2). FM11 (Sugawara shift missing; non-abelian KM: av(r)+dim(g)/2=kappa). FM13 (auto-complete Dedekind eta to bare `prod(1-q^n)`; annotate `q^{1/24}`). FM16 (silent kappa-family conflation). FM31 (Miura (Psi-1)/Psi universal across spins). FM31a (10/(5c^2)=2/c^2, NOT 2/(5c^2); substitute c=100).

**Categorical confusion.** FM4 (k=0 abelian vs k=-h^v critical at KM). FM5/FM21 (see FM-LIE-NUMERICS). FM17 (amplitude [0,2] != vdim 2). FM18 (d_gen=3 vs d_alg=inf for Vir). FM19 (dtau on curve vs omega_g on moduli). FM23 (local-global on curves; name space/comparison-data/extra-structure). FM24 (B-cycle i^2 error: q=exp(2*pi*i*hbar) becomes real). FM25 (see AP-SC-BAR). FM26 (see AP-SC-NOT-SELFDUAL). FM27 (scope inflation in metadata). FM28 (see AP-TOPOLOGIZATION). FM32 (pi_3(BU)=0; fiber sequence pi_k(BX)=pi_{k-1}(X)). FM33 (formula outside hypothesis domain: kappa_ch=chi(S)/2 only for Tot(K_S->S)). FM40 (naive center != derived: Z(Drin(H_k)) dim 1 vs Z^{der}_{ch}(H_k) dim 3).

**Sign/convention.** FM29 (nabla=d-A gives dPhi=+A*Phi; verify nabla(Phi)=0). FM30 (Belavin: Pauli decomposition NOT Weierstrass zeta; two-step degeneration). FM32a (RTT sign: additive R=uI+Psi*P vs Molev 1-P/u opposite). FM33a (qdet ordering DECREASING, j=N-1 leftmost; left-to-right NOT central N>=3). FM34 (excision=gluing, B_L (x)_A B_R; coproduct=splitting, plain (x)). FM34a (heat prefactor 1/(4*pi*i) diag, 1/(2*pi*i) off-diag). FM39 (spectral coassociativity uses SHIFTED params, not Delta_z with itself).

**Structural.** FM5 (wrong Lie dims; see FM-LIE-NUMERICS). FM6 (undefined macros in standalone extraction: `\cW`, `\hol`, `\Ran`, `\FM`, `\chHoch`; grep `\\[a-zA-Z]+` vs preamble). FM7 (LaTeX typo `\end{definition>`; grep `\\end\{[^}]*>`). FM8 (universal-quantifier drift on uniform-weight). FM10 (hardcoded Part~IV/Chapter~12; grep `Part~[IVX]+|Chapter~[0-9]+`). FM12 (mid-response truncation; separate fix from report). FM14/15 (see AP-LABEL-DISCIPLINE). FM20 (iff-drift; "Forward:... Reverse:... proved/CONJECTURED" template). FM22 (K_BP=2 wrong; 196). FM37 (double superscript on `\SCchtop`; use explicit `\mathsf{SC}^{ch,top,an}`). FM38 (vertex-IRF not automatic; face-model bypass for genus-2 DDYBE). FM41 (Jones = Markov + writhe + quantum dim; raw KZ trace != Jones).

**Agent / campaign infrastructure.**
- **FM35 (CONSTITUTIONAL).** NEVER REVERT MATHEMATICAL CONTENT TO FIX BUILD ERRORS. Build errors are LaTeX; math is never at fault. 100 macro errors = add 100 `\providecommand` lines. NEVER DROP MATHEMATICS.
- **FM36.** Macro portability on cross-volume insertion. Grep undefined control sequences after insertion; add `\providecommand`.
- **FM42.** Bulk substring replacement corruption (CRITICAL). `replace_all` "arity"->"degree" corrupts singularity->singuldegree, parity->pdegree, etc. (45 corruptions in one Vol III campaign). NEVER bulk-replace short strings inside common words. After any bulk replace, grep `ldegree|ndegree|rdegree|pdegree|tdegree`. Checklist: {singularity, complementarity, unitarity, regularity, modularity, parity, familiarity, similarity, polarity, disparity, linearity, popularity, circularity, hilarity}.
- **FM43.** E_n output scope of CY-to-chiral Phi: E_2-chiral at d<=2, E_1-chiral at d>=3. Always state scope `(n=2 for d<=2; n=1 for d>=3)`.
- **FM44.** Agent rate limiting. Batches of 3, not 30+. Expect 5-13 min per agent on 1000-3000 line files.
- **FM45.** Agent skill fidelity gap (200-word brief vs 15,000-word skill). For full rectification, invoke skill in main conversation.
- **FM46.** Stale preface line counts. After campaign, update with `wc -l` comparison.

## XX. Regression Safeguards

- **RS-3.** Physics IS the homotopy type, not a "bridge." Costello-Gaiotto-Dimofte are substance.
- **RS-4.** Costello/Dimofte/Gaiotto content in mathematical core, not "connections" chapters.
- **RS-9.** The slab is a bimodule, NOT a Swiss-cheese disk. Two boundary components.
- **RS-10.** Single-pass agent work without audit FORBIDDEN. Beilinson loop mandatory.
- **RS-12.** The programme is THREE volumes.
- **RS-13.** In Vol II, gravity is the CLIMAX (Part VI).
- **RS-14.** Introduction orients, Overture instantiates.
- **RS-15.** Koszul programme before higher_genus in dependency DAG.
- **RS-19.** Preface is complete survey. Save before compressing.

## XXI. Agent Anti-Patterns

- **AAP1.** Grep `antml` or `</invoke>` in .tex after every write.
- **AAP2.** Terminology rename ATOMIC across all three volumes in single session.
- **AAP3.** Formula implemented ONCE in canonical module, import everywhere.
- **AAP4.** `\begin{proof}` only after theorem/prop/lemma with ProvedHere. Use Remark[Evidence] for conjectures.
- **AAP5.** Build-artifact commits batched with content. Never standalone artifact commits.
- **AAP6.** Search ALL THREE volumes before downgrading a status tag.
- **AAP7.** Grep current file before writing a formula that appears elsewhere in same file.
- **AAP8.** README claims independently verifiable by test suite.
- **AAP9.** Wait for ALL agents to finish before launching new batch.
- **AAP10.** After agent completion, verify BOTH engine AND test files exist.
- **AAP11.** Every hardcoded expected value derivable by 2+ independent paths.
- **AAP12.** Asymptotic tolerance proportional to 1/log(N) or verified by two methods.
- **AAP13.** NEVER downgrade model without user permission. Wait and retry on rate limit.
- **AAP14.** Unique branch name per agent.
- **AAP15.** Serialize builds or use isolated worktrees. Parallel pdflatex kills.
- **AAP16.** git stash FORBIDDEN. Use `git diff > patch.diff` + `git apply`.
- **AAP17.** Verify edits via `git diff`, not agent narrative.
- **AAP18.** Confabulating operadic theory -> compute or cite (Loday-Vallette, Vallette, Livernet). NEVER analogize.

## XXII. Pre-Edit Verification Protocol

Fill-in-the-blank templates MANDATORY before writing listed formula classes. Filling a template IS the verification.

**Invocation protocol.** Before every Edit touching a trigger pattern, write the relevant template as a fenced block in the reply text (NOT in .tex), fill it in, end with `verdict: ACCEPT`, THEN invoke Edit. If any `match?` is `N` or required source blank, `verdict: REJECT` and re-draft.

**PE-1. r-matrix write** (AP-RMATRIX; trigger: `r(z)`, `r_{ij}`, classical r-matrix)

```
## PRE-EDIT: r-matrix
family:                    [Heis / affine KM / Vir / W_N / lattice / Yangian / other]
r(z) written:              [full formula with level prefix]
level parameter symbol:    [k / k+h^v / hbar / c / Psi]
OPE pole order p:          [_]
r-matrix pole order p-1:   [_]              # d log absorbs one pole
convention:                [trace-form k*Omega/z / KZ Omega/((k+h^v)*z)]
k=0 check (trace-form):    r(z)|_{k=0} = [_]    expected: 0
  (KZ convention: k=0 gives Omega/(h^v*z) != 0 for non-abelian g; this is correct)
match?                     [Y/N]            # must be Y for trace-form; N/A for KZ non-abelian
grep check:                bare \Omega/z instances in edit scope: [N]
bare \Omega/z allowed?     N
critical-level (KM):       r(z)|_{k=-h^v} = [_]    (trace-form: finite; KZ: diverges)
source:                    [landscape_census.tex:LINE / compute/module.py]
verdict:                   [ACCEPT / REJECT]
```

**PE-2. kappa formula write** (AP-KAPPA; trigger: kappa or variant)

```
## PRE-EDIT: kappa
family:                    [Heis / Vir / KM / W_N / bc / betagamma / svir / other]
kappa formula written:     [_]
census citation:           landscape_census.tex:LINE, kappa^{family} = [_]
match?                     [Y/N]            # STOP if N
AP39 uniqueness: is kappa = S_2?  [Y/N]
  if Y, is family Vir?     [Y/N]            # only Vir has kappa = S_2/2 = c/2
evaluation paths:
  at k=0:                  [_]  expected [_]
  at k=-h^v (KM):          [_]  expected 0
  at c=13 (Vir):           [_]  expected 13/2
AP136 boundary (W_N):      formula uses [H_N / H_{N-1} / H_N - 1]
  substitute N=2:          [_]  expected c/2 (W_2 = Vir)
wrong variants avoided:
  NOT kappa(Vir) = c       NOT kappa(W_N) = c*H_{N-1}
  NOT kappa(Heis) = k/2    NOT kappa(KM) = (k+h^v)/(2h^v) (missing dim(g))
verdict:                   [ACCEPT / REJECT]
```

**PE-4. bar complex formula** (AP132, AP22, AP23, AP44; trigger: `B(A)`, `T^c(...)`, any desuspension)

```
## PRE-EDIT: bar complex
object written:            B(A) = [_]
T^c argument:              [s^{-1} \bar A / s^{-1} A / s \bar A / bare A]
AP132 augmentation:        \bar A = ker(epsilon) present?  [Y/N]   # must be Y
AP22 desuspension:         |s^{-1} v| = |v| [-1 / +1]              # must be -1
s^{-1} (NOT bare s) used?  [Y/N]                                   # must be Y
coproduct type:            [deconcatenation T^c / coshuffle Sym^c / coLie]
match to intended bar?     [B^ord -> deconc / B^Sigma -> coshuffle / B^Lie -> coLie]
grading:                   cohomological |d|=+1?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

**PE-5. Vol III kappa write** (AP113; trigger: ANY kappa in `~/calabi-yau-quantum-groups/**/*.tex`, zero tolerance)

```
## PRE-EDIT: Vol III kappa
subscript written:         [kappa_ch / kappa_cat / kappa_BKM / kappa_fiber / OTHER]
subscript present?         [Y/N]   # must be Y; bare kappa FORBIDDEN
subscript justification:   [chiral shadow / categorified / BKM / fiber correction]
census citation:           Vol III landscape_census_cy.tex:LINE
grep BEFORE write:         bare `\kappa[^_]` hits: [N]
grep AFTER write:          bare `\kappa[^_]` hits: [N]
delta = 0?                 [Y/N]   # must be Y
verdict:                   [ACCEPT / REJECT]
```

**PE-7. Label creation** (AP-LABEL-DISCIPLINE; trigger: any `\label{...}` write)

```
## PRE-EDIT: label
environment:               [theorem / proposition / conjecture / definition / remark / lemma]
label written:             \label{prefix:name}
prefix match:              theorem->thm, prop->prop, conj->conj, def->def, rem->rem, lem->lem
match?                     [Y/N]   # must be Y
duplicate check (grep all three volumes):
  Vol I matches:           [N]
  Vol II matches:          [N]
  Vol III matches:         [N]
  total BEFORE:            [N]
  total AFTER:             [N]
  delta = 1?               [Y/N]   # must be Y
if duplicate, rename with volume suffix and update all \ref
verdict:                   [ACCEPT / REJECT]
```

**PE-8. Cross-volume formula** (AP5, AP3; trigger: formula shared across volumes)

```
## PRE-EDIT: cross-volume formula
formula:                   [_]
Vol I grep:                [hits, canonical form]
Vol II grep:               [hits, canonical form]
Vol III grep:              [hits, canonical form]
consistent across volumes? [Y/N]
if inconsistent:
  canonical volume:        [Vol I / II / III]
  other volumes updated same session?  [Y/N]  # must be Y
convention conversion?     [OPE(I) -> lambda(II) / motivic(III) / NA]
conversion applied?        [Y/N/NA]
verdict:                   [ACCEPT / REJECT]
```

**PE-10. Scope quantifier** (AP6, AP7, AP32, AP139; trigger: theorem statement, obs_g / F_g / lambda_g, universal quantifier)

```
## PRE-EDIT: scope quantifier
statement:                 [_]
genus:                     [g=0 / g=1 / g>=2 / all g / UNSPECIFIED -> REJECT]
degree:                     [n=_ / all n / UNSPECIFIED -> REJECT]
level:                     [convolution M-bar_{g,n} / ambient Mok25 log FM / both / NA]
weight tag:                [(UNIFORM-WEIGHT) / (ALL-WEIGHT + delta F_g^cross) / NA]
tagged in statement?       [Y/N]  # must be Y for any g>=2 claim
free-variable audit:
  variables on LHS:        {_}
  variables on RHS:        {_}
  LHS superset RHS?        [Y/N]  # if N, bind the free variable
implies vs iff:            [implies / iff]
  if iff, converse proved in same theorem?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

**PE-11. Differential form type** (AP117, AP27, AP130; trigger: connection 1-form, KZ, Arnold, bar propagator)

```
## PRE-EDIT: differential form
what:                      [connection 1-form / bar propagator / Arnold form / KZ / other]
form written:              [_]
expected type:
  connection 1-form: r(z) dz  (NOT d log)
  KZ:                sum r_{ij} dz_{ij}
  Arnold form:       d log(z_i - z_j)  (bar coefficient, NOT connection)
  bar propagator:    d log E(z,w)  (weight 1 ALWAYS)
match?                     [Y/N]
propagator weight:         1?  [Y/N]
d log check:               if d log appears, Arnold-form context? [Y/N]
space the form lives on:   [fiber Sigma_g / base M-bar_{g,n} / FM_n(X) / Ran(X)]
fiber-base:                object on fiber vs class on base correctly distinguished? [Y/N]
verdict:                   [ACCEPT / REJECT]
```

**Refusal criteria.** Reject own edit if any `match?` = N, any blank source, any `FORBIDDEN` ticked, grep delta mismatch. On reject: re-draft, re-fill, proceed only when `verdict: ACCEPT`.

Remaining templates PE-3 (complementarity), PE-6 (exceptional dimensions), PE-9 (summation boundary), PE-12 (prose hygiene) in `compute/audit/pre_edit_verification_protocol_wave12.md`.

## XXIII. The Resonance Loop

For any nontrivial task, run this loop until CONVERGED or BLOCKED.

### 0. Scope Lock
State the exact claim surface. Lock: file, theorem label, formula, convention, family, status.

### 1. Invariant Lock
Before trusting any local argument, lock: grading and shifts; object identity among A, B(A), A^i, A^!, Z^{der}_{ch}; genus, degree, family, filtration, and completion scope; theorem status and environment; Vol I/II/III convention bridges.

### 2. RED Pass -- Attack Logic
Dependency attack; hypothesis attack; edge-case or counterexample; sign, grading, duality, notation; reduced-vs-completed or finite-stage-vs-limit; object-conflation; status-inflation.

### 3. BLUE Pass -- Attack Consistency
Theorem/proof/status mismatch; label prefix/uniqueness drift; stale Part references; compute/manuscript disagreement; README or notes outclaiming .tex; cross-volume inconsistencies.

### 4. GREEN Pass -- Attack Gaps
Missing definitions; hidden imported lemmas; unsupported converses; dangling references; true statement weaker than advertised.

### 5. Patch in Dependency Order
CRITICAL and SERIOUS first, then MODERATE. For each: (a) re-read local context, (b) re-derive or recompute independently, (c) smallest truthful edit, (d) immediately search for downstream advertisements.

### 6. Propagate
After any mathematical change: grep Vol I; grep Vol II; grep Vol III. Update genuine duplicates or leave explicit pending note.

### 7. Verify
Narrowest check that can falsify: targeted pytest; grep for forbidden formulas/stale labels/banned prose; targeted TeX build; metadata check.

### 8. Hostile Re-Read
Reread your own rewrite as an adversary. Try to break it.

### 9. Stop Condition
- **CONVERGED**: no known actionable MODERATE+ issue on modified surface; narrowest verification passes.
- **BLOCKED**: exact blocker named precisely with strongest truthful narrower statement.

Do not stop between those states.

## XXIV. Convergent Writing Loop

For introductions, prefaces, chapter openings, and load-bearing prose:

`WRITE -> REIMAGINE -> REWRITE -> BEILINSON AUDIT -> REIMAGINE AGAIN -> REWRITE AGAIN -> CONVERGE`

Minimum: preface/introduction 3+ iterations; chapter openings 2+.

Reimagination channels: Gelfand (inevitability), Beilinson (falsification), Drinfeld (unifying principle), Kazhdan (compression), Etingof (clarity), Polyakov (physics=theorem), Nekrasov (seamless passage), Kapranov (higher structure IS math), Ginzburg (every object solves a problem), Costello (factorization), Gaiotto (dualities compute), Witten (physical insight precedes proof).

CG structural moves: deficiency opening; unique survivor; instant computation; forced transition; decomposition table; dichotomy; sentence-as-theorem.

## XXV. Claim-Status Discipline

Every serious statement: exactly one of `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConditional`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusOpen`.

Rules:
- ProvedHere = verify proof proves stated claim; status tag != ground truth
- Conjectured -> `\begin{conjecture}`; ProvedElsewhere -> theorem + Remark[Attribution]
- When downgrading theorem -> conjecture: rename `thm:foo -> conj:foo` AND update every `\ref` atomically
- README may not outclaim live manuscript
- Tag only genuinely new content ProvedHere; classical parts ProvedElsewhere with attribution

## XXVI. Structural Facts

**Shadow tower.** Theta_A := D_A - d_0 is MC (`thm:mc2-bar-intrinsic`). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M quadrichotomy. Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (`prop:sc-formal-iff-class-g`). Depth gap: d_alg in {0,1,2,inf} (`prop:depth-gap-trichotomy`). ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (`prop:chirhoch1-affine-km`).

**Convolution.** dg Lie `Conv_str` is strict model of L-inf `Conv_inf`. MC moduli coincide. Full L-inf needed for transfer/formality/gauge equivalence.

**E_1 primacy.** B^ord is the primitive (Stasheff). av: g^{E_1} -> g^mod lossy Sigma_n-coinvariant projection. At degree 2, av(r(z)) recovers kappa in the abelian and scalar families; for non-abelian affine KM gives kappa_dp and the full kappa adds dim(g)/2. All standard chiral algebras are E_inf (local); E_1 = nonlocal (Yangian, EK quantum VA). NEVER "E_inf means no OPE poles."

**Three-pillar constraints.** (1) Convolution sL-inf `hom_alpha(C,A)` is NOT strict Lie. (2) `hom_alpha` fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X, D).

## XXVII. Alternative Proofs Secured (2026-04-13)

Every main theorem has >=2 independent proof paths.

| Theorem | Primary | Alternative |
|---------|---------|-------------|
| A | Twisting morphisms + filtered comparison | Lurie inf-cat nerve-realization (H01); PTVV/factorization-homology (upgraded to proposition) |
| B | Bar filtration spectral sequence | Keller deformation + Kontsevich formality (H02) |
| C | Fiber bar + eigenspace decomp | PTVV shifted symplectic (H03) |
| D | Shadow tower + genus universality | GRR on universal curve (H04, upgraded to genuinely disjoint factorization-homology) |
| H | Bar-Hochschild comparison | Deformation-theoretic dimensional analysis (H05) |
| MC2 | Recursive inverse limit | KS scattering diagram (H06) |
| MC5 | Harmonic mechanism + coacyclic | Operadic Koszul duality (H07); direct SC^{ch,top} homotopy-Koszulity via Ginzburg-Kapranov |
| Topologization | Sugawara [Q,G]=T | CFG factorization homology (H08, no longer conjectural) |
| SC-formal | Shadow tower truncation | Operadic tower truncation (H11) |
| Depth gap | MC relation at degree 4 | Shadow Lie Jacobi (H10) |
| Compl K | Fiber-center + Theorem D | Index theory / Euler characteristic (H12) |

Condition removal: uniform-weight (H13), Koszul locus (H14), chain-level topologization (H15), perfectness C1 (H17, now a theorem `prop:perfectness-standard-landscape`).

## XXVIII. Platonic Ideal Roadmap (Beilinson-rectified 2026-04-17)

**Unconditional (high confidence).** Thms A (fixed-curve, modular-family PROVED), B (on-locus, off-locus after Chiral-Positselski 7.2), C0 (D^co), C1 (g>=1, perfectness a theorem), D (all-genera via clutching-uniqueness), H (circularity resolved via PBW), MC1, MC2, MC4^+ and MC4^0, SC-formality, depth gap, D^2=0, Theta_A, ChirHoch^1, 10 Koszul equivs, Verlinde recovery, ker(av), Miura coefficient, critical level jump, E_3 identification (simple / gl_N / semisimple / reductive / nilpotent / solvable), chiral QG equiv (ordered Koszul locus, E_1-chiral input included; elliptic; toroidal formal-disk), gl_N chiral QG all N, Theorem A^{infty,2}, CY-D dimension stratification, periodic CDG admissible KL, E_infty-Topologization (iterated Sugawara), chiral higher Deligne, curved-Dunn H^2=0 all g>=2, SC^{ch,top} heptagon, universal celestial holography (chain-level).

**Conditional (genuine mathematical restrictions).** C2 Lagrangian (uniform-weight + BV package), MC3 full DK beyond type-A (modulo `conj:dk-compacts-completion`; CONJECTURAL for logarithmic W / N=2 SCA / cosets / non-rational lattice / roots of unity), MC5 direct-sum `Ch(Vect)` chain-level class M (genuinely FALSE; PROVED on pro-object / J-adic / weight-completed ambients), Koszul (vii) multi-weight (genus-0), Koszul (viii) freeness (Massey vanishing), universal celestial holography at g>=1 class M (`conj:uch-gravity-chain-level`), toroidal chiral QG global P^1 x P^1 (class-M chain-level dependence), topologization chain-level on direct-sum class-M original complex.

**Conjectural.** Topologization general chiral with conformal vector beyond iterated-Sugawara scope; Theorem A modular-family for non-finitely-generated MC4-completion regime.

**Open frontier (post-Wave 14 reconstitution, 2026-04-16).** Five previously-deepest frontiers CLOSED or substantially REDUCED: (1) chain-level E_3 on original complex (Vol II `e_infinity_topologization.tex`, `chiral_higher_deligne.tex`); (2) MC5 chain-level class M (CLOSED pro / J-adic / weight-completed; direct-sum genuinely false, correct scope); (3) modular-family Theorem A over M-bar_{g,n} (Vol I `theorem_A_infinity_2.tex`); (4) topologization general with conformal vector (Vol II `e_infinity_topologization.tex`); (5) chiral coproduct for non-gauge-theoretic families (Vol II `unified_chiral_quantum_group.tex`). Sole remaining genuine frontier `conj:periodic-cdg` for admissible KL (FM251): CLOSED by Vol I `periodic_cdg_admissible.tex`.

**Beilinson-rectified open frontiers (2026-04-17 audit, surfaced AFTER 2026-04-16 wave).**
- **W(p) triplet tempering.** Vol II commit `a5640de` inscription RETRACTED `thm:tempered-stratum-contains-wp` from ProvedHere to Conjectured. The Zhu-bounded-Massey proof chain fails: Gurarie 1993 (arXiv:hep-th/9303160) and Flohr 1996 (arXiv:hep-th/9605151) construct logarithmic-CFT amplitudes with unbounded Massey despite finite-dim Zhu. Correct tempered scope: principal + non-logarithmic + non-minimal standard landscape; W(p) open pending Adamovic-Milas character-amplitude bound.
- **Non-tempered stratum OVERCLAIM.** Climax statement "non-tempered stratum is EMPTY on C_2-cofinite standard landscape" is SCOPE-QUALIFIED: emptiness holds on the non-logarithmic subset (Vir, W_N, all Schellekens, Monster, irrational cosets). Logarithmic W(p) remains open.
- **CY-C pentagon invariant.** Vol III commit `cade61c` healed pentagon stratification `{3, 12, 24}` from `kappa_ch^{R_i}` to `rho^{R_i}` (generator-lattice rank). Category error: kappa_ch is route-independent = 0 for K3xE by Hodge supertrace; stratification is algebraic invariant orthogonal to kappa_ch.
- **Kummer-irregular prime labelling.** Vol I commit `9668336` retracted primes 1423, 3067, 23, 43, 419 from Kummer-irregular label. They appear in S_r numerators as Riccati-arithmetic characteristic primes. Corrected Tier-3 emergence: {37, 691, 811}; 3067 dropped.
- **beta_N exact closed form.** RESOLVED (Vol II `beta_N_closed_form_all_platonic.tex`, `thm:beta-N-closed-form-proved-all-N`): beta_N = 12*(H_N - 1) = sum_{s=2}^{N} 12/s. Both prior candidates RULED OUT at N=4. Rational (not integer) for N>=5; beta_5 = 77/5, beta_6 = 87/5.
- **Super-complementarity canonical pairing.** `kappa + kappa^! = max(m, n)` for super-Yangians scopes to sub-Sugawara line; two pairings (super-trace vs Berezinian) coexist without programme-level canonicalisation. Verdier pairing inscription pending.

The Beilinson audit inscribed `notes/rectification_map_beilinson_audit.md` (926 lines) with full verdicts and heal paths; post-audit priority order places climax-rewrite and preface-refresh LAST to prevent propagation of unverified closures.

**Recovery infrastructure:** `scripts/resume_failed.py`, `scripts/campaign_dashboard.py`, 9 campaign scripts.

## XXIX. Vol III 6d hCS Cross-Awareness (2026-04-12/13)

Feeds back into Vol I. Detail in `notes/cross_volume_aps.md`.

**Capsule of AP-CY23-34:** E_1-chiral bialgebra is correct Hopf home (B^ord preserves R-matrix; B^Sigma kills Hopf) (AP-CY23); docstring confabulation (AP-CY24); R = (id(x)S)Delta(1) WRONG, use half-braiding (AP-CY25); sigma_2 even under h_i->-h_i, k^!=-k from Shapovalov (AP-CY26); sandbox non-persistence, verify with `ls` (AP-CY27); pole-unsafe test points (avoid z=+/-h_i) (AP-CY28); wrong-repo writes (AP-CY29); factored != solved (YBE does NOT imply ZTE) (AP-CY30); spectral z != worldsheet z (AP-CY31); reorganisation != bypass (AP-CY32); chain-level != rational (E_3 collapses under formality) (AP-CY33); total {b,B^{(2)}}=0 via Costello TCFT but individual {b_k,B^{(2)}} != 0 (AP-CY34).

**Geometric vs Algebraic Model Conflations (AP-CY62-67, migrated 2026-04-16 to `notes/cross_volume_aps.md`).** Specify "geometric (FM)" vs "algebraic (bar/operadic)" for any chain-level C^*_ch(A,A) (CY62); "chiral endomorphism operad on FM_k(C)" FIRES -- End^ch is algebraic (CY63); HH*(Weyl)=1-dim, "Theorem H has no THH analogue" FALSE; unbounded object is Gel'fand-Fuchs not THH (CY64); Yangian Y(g) has spectral parameters in Drinfeld centre via evaluation modules (CY65); BZFN uses SAME S; two centres come from DIFFERENT algebras (chiral A vs A_mode) (CY66); spectral parameters are formal algebraic variables in End^ch_A; FM_k(C) enters via comparison, not definition (CY67).

**Key Vol I infrastructure results:** Shadow tower S_k = A_inf coproduct correction delta^{(k)} PROVED; shadow-Feynman L-loop = S_{L+1}. ZTE fails for Yang R-matrix at O(kappa^2); E_3 nontrivial beyond E_2. E_3 bar cohomology: class L=(1+t)^{3g}=2^{3g}; class C=2^{3g}; class M = 6^g (Kunneth, chain-level P(q)^{6g}). Universal coproduct Delta_z(e_s)=sum C(N_R-b, k) z^k e_a^L * e_b^R (all spins). Conductors: G/L rho_K=0; M(Vir) 13; K3xE 0. Chiral CE: B(U^ch(L)) = CE_*(L) PROVED. kappa_BKM = c_N(0)/2 universal. CY-A_3 PROVED in inf-cat; chain-level [m_3, B^{(2)}] != 0 is NOT obstruction; Obs_Ainf=0 UNIVERSALLY via Costello TCFT.

## XXX. Architecture

**Vol I** (~2,700pp). Introduction + Overture (Heisenberg CG opening, unnumbered) + Part I (Bar Complex: Thms A-D+H, 12 Koszul equivs) + Part II (Characteristic Datum: shadow tower, G/L/C/M/M*/W, higher-genus, E_1 modular) + Part III (Standard Landscape: all families, census) + Part IV (Physics Bridges: E_n, factorization envelopes, derived Langlands) + Part V (Seven Faces of r(z): F1 bar-cobar twisting, F2 DNP25 line-operator, F3 Khan-Zeng PVA, F4 Gaiotto-Zeng sphere Hamiltonians, F5 Drinfeld Yangian, F6 Sklyanin/STS83, F7 FFR94 Gaudin) + Part VI (Frontier) + Appendices.

**Vol II** (~1,749pp). SC^{ch,top} bar differential = holomorphic factorization on C, coproduct = topological factorization on R. Seven parts: I (Open Primitive), II (E_1 Core), III (Seven Faces), IV (Char Datum), V (HT Landscape), VI (3D Quantum Gravity = CLIMAX), VII (Frontier). Vol II CLAUDE.md + `notes/cross_volume_aps.md` for V2-AP*.

**Vol III** (~693pp). CY -> chiral functor Phi. ~34,000 tests, ~460 engines. 10 proofs at publication standard. Seven parts: I (Foundations), II (CY-to-Chiral Functor), III (E_n Hierarchy), IV (K3 Yangian), V (CY Landscape), VI (Seven Faces r_CY), VII (Frontiers). kappa subscripts MANDATORY. CY-A_3 PROVED (inf-cat). K3 abelian Yangian PROVED. ZTE T COMPUTED. kappa_BKM = c_N(0)/2 universal. Class M E_3 bar dim = 6^g. Shadow tower through m_8. Mock modular K3: THEOREM at d=2. CY-D dimension-stratified.

## XXXI. Build & Test

```bash
# Vol I
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
make test          # fast tests
make test-full     # all tests (~119K)

# Vol II
cd ~/chiral-bar-cobar-vol2 && make

# Vol III
cd ~/calabi-yau-quantum-groups && make fast

# Census
python3 scripts/generate_metadata.py
```

CAUTION: Watcher spawns competing pdflatex; always kill before builds.

## XXXII. Session Protocol

1. Read CLAUDE.md + AGENTS.md.
2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`.
3. Tests: `make test`.
4. `git log --oneline -10`.
5. Read .tex source before any edit (never from memory).
6. After each change: build + test. After each correction: grep ALL THREE volumes.
7. Never guess a formula: compute or cite `landscape_census.tex`.
8. Apply convergent writing loop to all prose.
9. Session end: build all three volumes, run tests, summarize errors by class.
10. Before first Edit: run HOT ZONE check (§XIII) and Pre-Edit Verification (§XXII). If pending edit touches r-matrix / kappa / bar complex / label / Vol III kappa / cross-volume formula / scope quantifier / differential form, fill the corresponding PE-1..PE-11 template as a fenced block BEFORE invoking Edit, ending with `verdict: ACCEPT`.

## XXXIII. Skill Routing (Claude <-> Codex)

Every Claude skill has a Codex home. No durable workflow is Claude-only.

| Claude Skill | Codex Skill (.agents/skills/) | Trigger |
|-------------|-------------------------------|---------|
| `/build` | `build-surface` | build, test, compile, verify |
| `/audit [target]` | `deep-beilinson-audit` | audit, falsify, red-team, pressure-test, verify |
| `/rectify [file]` | `beilinson-rectify` | rectify, fortify, tighten, repair |
| `/beilinson-rectify [file]` | `beilinson-rectify` | same as /rectify (heavier variant) |
| `/chriss-ginzburg-rectify [file]` | `chriss-ginzburg-rectify` | chapter-scale structural rewrite, CG convergence, introductions, prefaces |
| `/verify [claim]` | `multi-path-verify` | verify formula, invariant, computational claim |
| `/propagate [pattern]` | `cross-volume-propagation` | cross-volume formula/status fix |
| `/compute-engine [name]` | `compute-engine-scaffold` | new engine with multi-path tests |
| `/rectify-all` | swarm of `beilinson-rectify` | full-volume parallel (user-authorized) |
| `/beilinson-swarm` | swarm of `beilinson-rectify` | parallel chapter rectification (user-authorized) |
| `/research-swarm [topic]` | `frontier-research` | frontier synthesis, research architecture |
| -- | `claim-surface-sync` | theorem/status/concordance/label drift |

Both `/rectify` and `/chriss-ginzburg-rectify` are available in BOTH Claude (via CLAUDE.md skill definitions) and Codex (via `.agents/skills/beilinson-rectify/SKILL.md` and `.agents/skills/chriss-ginzburg-rectify/SKILL.md`). Use `beilinson-rectify` for targeted chapter/proof repair; use `chriss-ginzburg-rectify` for chapter-scale structural rewriting with convergent loop (subject to §III constitutional injunction).

Codex skill invocation: when a task matches a skill trigger, use the skill instead of reconstructing the workflow. Swarm delegation: only with explicit user authorization. Split by independent scope, not overlapping edits.

Default reasoning effort: `medium`. Escalate to `high`/`xhigh` only for proof surgery, chapter-scale structural repair, or stalled frontier synthesis after task definition and falsifier are already sharp.

## XXXIV. Hook Architecture

Codex hooks in `.codex/hooks.json` provide deterministic guardrails:

- **SessionStart**: injects live-surface reminder and skill map
- **UserPromptSubmit**: routes prompts toward matching Codex skills
- **PreToolUse (Bash)**: blocks destructive shell habits, warns on commit/source-edit paths
- **PostToolUse (Bash)**: refuses to let failing build/test output count as verification
- **Stop**: forces rectification-style work to close as CONVERGED or BLOCKED

Hook rule: hooks are deterministic guardrails, not substitutes for judgment. If a workflow repeats and does not belong in always-on context, move it to a skill instead of bloating AGENTS.md.

## XXXV. Codex / GPT-5.4 Task Intake

Before any nontrivial work, lock these eight items:

1. The exact target file, theorem, formula, bridge, engine, or live surface.
2. Task type: audit, rectification, formula verification, status sync, compute/test repair, build triage, or frontier synthesis.
3. Active convention bridge: grading, shifts, OPE vs lambda-brackets, genus/degree scope, ordered vs symmetric bar, Vol I vs Vol II vs Vol III normalization.
4. Live evidence surface: source, nearby context, diff, logs, tests, citations.
5. Narrowest falsifier that could kill the current claim.
6. Propagation surface across three volumes.
7. Dirty collision surface in every repo involved.
8. Matching skill, if a repo skill applies.

If the user prompt is underspecified, infer the smallest defensible scope only after reading the live surface.

## XXXVI. Cross-Volume Propagation Discipline

- Never assume a fix is local if the claim is formula-level, status-level, or bridge-level.
- Before changing shared formula/theorem: grep all three volumes.
- After changing: grep again for stale copies.
- Never hardcode Part numbers: use `\ref{part:...}`.
- When correcting engine formula: derive new expected independently before changing tests.
- Convention conversion required between volumes (OPE -> lambda-bracket -> motivic).
- Build artifacts and release PDFs are downstream, not authoritative.

## XXXVII. Prose and Formatting Discipline

Banned (case-insensitive): moreover, additionally, notably, crucially, remarkably, interestingly, furthermore, "we now", "it is worth noting", "worth mentioning", "it should be noted", "it is important to note", delve, leverage, tapestry, cornerstone, landscape (metaphor), journey, navigate (non-geometric).

Em-dash (---, U+2014) FORBIDDEN. Use colons, semicolons, separate sentences.

Hedging ban in math: arguably, perhaps, seems to, appears to. State or mark conjecture.

No Markdown in LaTeX: no backtick numerals, no **bold**, no _italic_. Use `$...$`, `\textbf`, `\emph`.

Post-write grep MANDATORY on touched .tex files.

## XXXVIII. LaTeX Conventions

All macros in `main.tex` preamble. NEVER `\newcommand` in chapters (use `\providecommand`). Memoir class, EB Garamond (newtxmath + ebgaramond). Tags: `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`. Label everything with `\label{def:}`, `\label{thm:}`. Cross-reference with `\ref`. Do not add packages without checking compatibility. Do not create new .tex files when content belongs in existing chapters.

## XXXIX. Git Rules

All commits authored by Raeez Lorgat. NEVER credit an LLM. No co-authored-by, no generated-by, no AI attribution anywhere.

git stash FORBIDDEN (AAP16; use `git diff > patch.diff` + `git apply`). Constitution: concordance.tex.

Before every commit:
1. Build passes.
2. Tests pass.
3. Manuscript Metadata Hygiene grep returns zero hits (§VIII).
4. No AI attribution anywhere in the diff.

## XL. End-of-Task Output Contract

For every substantial mathematical task, end with:

1. The exact claim surface audited.
2. What was proved internally vs only supported computationally.
3. What remains conditional, conjectural, heuristic, or open.
4. What verification was run.
5. What propagation was completed or explicitly left pending.

If blocked: name the exact blocker and the strongest truthful narrower statement.

## XLI. Style of Action

Be decisive, but skeptical. Read before editing. Verify before advertising. Prefer the live source over inherited narrative. Prefer the narrowest falsifier over broad "confidence." Prefer one true local theorem over one false grand synthesis.
