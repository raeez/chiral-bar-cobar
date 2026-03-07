# SESSION PROMPT v14 — Structural Rearchitecting

## Identity

You are rearchitecting a 1414-page mathematics monograph. The theorems are proved. The prose is secondary. What is broken is the **structural logic** — the book proves true things in incompatible dialects, uses one symbol for three mathematically different objects in some chapters while having fixed the notation in others, and presents its deepest insights (modular Koszul duality as homotopy theory on Ran(X)) at the cohomological shadow level when the homotopy-native level is already within reach.

You operate at the triple intersection of pure mathematics, mathematical physics, and physics. Every edit must be mathematically correct, physically motivated, and precisely formulated.

## The diagnosis (three documents, one verdict)

The book has three structural diseases. They are ordered by severity.

### Disease 1: Notation inconsistency across genera

Convention `conv:higher-genus-differentials` in `higher_genus.tex:64-100` correctly defines three distinct differentials:

| Symbol | Name | Square | Home |
|--------|------|--------|------|
| `\dfib` | Fiberwise curved differential | `\dfib^2 = \mcurv{g}` | Fixed curve Σ_g |
| `\Dg{g}` | Total corrected differential | `\Dg{g}^2 = 0` | Genus-g bar complex |
| `\dzero` | Genus-0 collision differential | `\dzero^2 = 0` | Arnold/P¹ |

**The problem**: This convention is used 60 times in `higher_genus.tex` but only 1 time each in `bar_cobar_construction.tex`, `introduction.tex`, and `concordance.tex`. The other ~50 .tex files still use ambiguous `d`, `d_g`, `d^2` notation. Every file that discusses higher-genus differentials must be migrated.

### Disease 2: Proved/programmatic boundary blur

The book has two strata that read as one:
- **Stratum I** (proved): Theorems A-D on the Koszul locus, scalar modular characteristic package (κ, {F_g}, Δ_A), Lagrangian complementarity, evaluation-locus DK, free-field and conditional interacting examples.
- **Stratum II** (programmatic): Full Θ_A as non-scalar MC class, coderived Ran-space formalism, full factorization-categorical DK, infinite-generator duals (Vir↔W_∞), BV/BRST/path-integral dictionary beyond genus 0, E_n higher-dimensional extension.

The introduction (lines 140-163) already distinguishes these correctly. But:
- Master tables in `examples_summary.tex` mix proved and conjectural dualities in the same rows
- `kac_moody_framework.tex` uses `Rep(U_q(g))` where the correct KL target is `C(U_q(g))` (semisimplified tilting quotient) — this was fixed in `chiral_modules.tex` but not propagated
- The concordance chapter's horizon section packages chain-level proved results alongside full categorical conjectures without visual/structural separation

### Disease 3: Cohomological where homotopy is available

The modular Koszul definition (Def 8.17.7 = `def:modular-koszul-chiral` at `higher_genus.tex:7898`) states MK4 as diagonal Ext vanishing and MK5 as a cohomology decomposition. But the book already has:
- Chain-level Lagrangian eigenspaces (Thm 8.13.26)
- Shifted symplectic structure on formal moduli (Thm `thm:shifted-symplectic-complementarity`)
- PTVV Lagrangian globalization (Prop `prop:ptvv-lagrangian`)

The homotopy objects exist. The definition hasn't caught up. This is not about adding abstraction — it's about making the definition match what the proofs already establish.

---

## Execution: Seven workstreams, dependency-ordered

### Workstream 1: Differential notation propagation [MECHANICAL, HIGH IMPACT]

**What**: Find every file that discusses higher-genus differentials and ensure it uses `\dfib`, `\Dg{g}`, `\dzero`, `\mcurv{g}` from Convention `conv:higher-genus-differentials`.

**Method**:
1. `grep -rn 'd_g\|d\^2\|d\^{2}\|d_{\mathrm{bar}}\|d_{bar}' chapters/ appendices/ --include='*.tex'` to find ambiguous differential notation in higher-genus contexts
2. For each hit: read the surrounding context (±10 lines). Determine which of the three differentials is meant. Replace with the correct macro.
3. **Do NOT touch** genus-0-only statements where `d` or `d^2 = 0` unambiguously means `\dzero`.
4. **Do NOT touch** theorem/definition environments — only prose and displayed equations outside formal environments.

**Files to check** (priority order):
- `poincare_duality_quantum.tex` — quantum corrections, likely uses ambiguous d_g
- `genus_expansions.tex` — genus showcase, must use correct notation
- `free_fields.tex` — higher-genus sections
- `kac_moody_framework.tex` — higher-genus KM
- `w_algebras_framework.tex` — higher-genus W
- `deformation_theory.tex` — curved A∞
- `bv_brst.tex` — BRST differential vs bar differential
- `genus_complete.tex` — genus theory
- `feynman_diagrams.tex` — Feynman interpretation
- All appendices mentioning higher genus

**Verification**: After all edits, `grep -rn '\\dfib\|\\Dg\|\\dzero\|\\mcurv' chapters/ appendices/ --include='*.tex' | wc -l` should be substantially larger than the current 63.

**Compile gate**: `make fast` after every 3 files.

### Workstream 2: KL target category propagation [MECHANICAL, MEDIUM IMPACT]

**What**: Every occurrence of `Rep(U_q(\mathfrak{g}))` in the Kazhdan-Lusztig context must become `\mathcal{C}(U_q(\mathfrak{g}))` (semisimplified tilting quotient) or carry an explicit qualifier.

**Affected files** (from grep):
- `kac_moody_framework.tex` (4 hits)
- `derived_langlands.tex` (3 hits)
- `yangians.tex` (3 hits)
- `chiral_modules.tex` (2 hits — may already be correct)
- `chiral_koszul_pairs.tex` (1 hit)
- `deformation_theory.tex` (1 hit)

**Method**: Read each hit in context. If the statement is about the KL equivalence or its target, replace `\mathrm{Rep}(U_q(\fg))` with `\mathcal{C}(U_q(\fg))` and add a parenthetical "(semisimplified tilting quotient)" on first use per chapter. If the statement is about general representations (not KL-specific), leave it.

**Verification**: Reread `chiral_modules.tex` (the canonical version) to confirm the convention matches.

### Workstream 3: Master table stratification [STRUCTURAL, HIGH IMPACT]

**What**: Split every master table that mixes proved and conjectural dualities into two clearly separated sections.

**Files**:
- `examples_summary.tex` — The Master Table of Computed Invariants (~line 287+). Split into "Proved dualities" and "Conjectural/programmatic dualities" sub-tables.
- `concordance.tex` — The horizon section. Ensure every horizon item is explicitly marked as Stratum II.
- `introduction.tex` — The functorial correspondence table. Check that each row is correctly labeled.

**Method**: Read the full table. For each row, check: is the Koszul dual identification proved (ProvedHere/ProvedElsewhere) or conjectural? Move conjectural rows to a separate sub-table with a header like "Programmatic identifications (see Part III for status)."

**Verification**: Every row in the "Proved" sub-table should reference a theorem with `\ClaimStatusProvedHere` or `\ClaimStatusProvedElsewhere`. Every row in the "Programmatic" sub-table should reference a conjecture.

### Workstream 4: Homotopy-first MK definition [MATHEMATICAL, HIGH IMPACT]

**What**: Add a homotopy-native version of the modular Koszul definition alongside the existing one.

**Location**: `higher_genus.tex`, immediately before the current Definition 7898.

**Content**: A new definition `def:modular-koszul-homotopy` stating MK axioms in homotopy language:
- MK1∞: weight filtration makes B_X(A) Koszul on associated graded
- MK2∞: D_Ran B_X(A) ≃ B_X(A!) (equivalence in homotopy category of factorization coalgebras)
- MK3∞: Ω_X B_X(A) ≃ A on Koszul locus in Alg_aug(Fact(X))
- MK4∞: genus tower from filtered MC deformation of B_X(A)
- MK5∞: complementarity complex C_g(A) := RΓ(M̄_g, Z_A) splits as Q_g(A) ⊕ Q_g(A!) with each summand Lagrangian (homotopy eigenspaces of σ, not cohomological kernels)

Then relabel the existing definition as "Concrete dg model of Definition `def:modular-koszul-homotopy`" with a remark explaining that MK1-MK5 are the shadow (S-level) of MK1∞-MK5∞.

**Guard rail**: Do NOT change any existing theorem statements. Do NOT change any existing proofs. Add the homotopy definition as a NEW definition that the existing one models. The existing proofs then become "model presentations" of the homotopy statements — no proof needs rewriting.

**Verification**: Existing `\ref{def:modular-koszul-chiral}` references remain valid. New definition is referenced from introduction.tex.

### Workstream 5: Parameter-source diagram [MATHEMATICAL, MEDIUM IMPACT]

**What**: Add one commutative diagram that resolves the recurring confusion between "parameters from the curve" and "classes on moduli."

**Location**: `higher_genus.tex`, in or near Convention `conv:higher-genus-differentials` (line 64-100).

**Content**:
```latex
\begin{equation}\label{eq:parameter-source-diagram}
H^1(\Sigma_g, \C) \xrightarrow{\text{period}}
Z^1(\mathrm{Def}_{\mathrm{cyc}}(\cA)_{\mathrm{model}}) \xrightarrow{\text{obstruction}}
R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_\cA) \xrightarrow{\mathrm{tr}}
R\Gamma(\overline{\mathcal{M}}_g, \Q)
\end{equation}
```

With a 3-line remark: fiber-period parameters (t_k from A-cycles of Σ_g) live at the left. Moduli obstruction classes (obs_g) live in the middle. Scalar tautological shadows (κ·λ_g) live at the right. The quantum-corrected differential D_g uses the LEFT data; the complementarity theorem uses the MIDDLE data; the modular characteristic theorem uses the RIGHT data.

### Workstream 6: Scalar vs. full package — introduction tightening [EDITORIAL, MEDIUM IMPACT]

**What**: Make the introduction's treatment of Theorem D surgically precise about what is proved vs. what is programmatic.

**Location**: `introduction.tex`, the Theorem D paragraph (~line 196-230).

**Edit**: Ensure Theorem D is stated as "the scalar modular characteristic system is determined by κ(A)" and that the non-scalar Θ_A is explicitly labeled as the "principal open problem of the modular programme" (which it already is at line 157 — verify and sharpen if needed).

Also check: does the introduction ever say "the modular characteristic package is established" without the scalar qualifier? If so, add "scalar" before "package."

### Workstream 7: Proved/conditional split for interacting MK [MATHEMATICAL, LOW RISK]

**What**: Verify the current Prop 8006 (`prop:conditional-modular-koszul`) is correctly stated and that no other location in the book claims unconditional modular Koszulity for Virasoro/W_N.

**Method**: `grep -rn 'modular Koszul' chapters/ appendices/ --include='*.tex'` and check each hit. If any claim says "Virasoro is modular Koszul" without the PBW degeneration hypothesis, add the qualifier.

---

## Execution protocol

### Priority and dependency
```
W1 (differential notation) — independent, do first (highest mechanical impact)
W2 (KL target) — independent, can parallel with W1
W3 (table split) — independent, can parallel
W4 (homotopy MK def) — after W1 (needs stable notation), highest mathematical impact
W5 (parameter diagram) — after W1 (lives in same file)
W6 (intro tightening) — after W4 (references new definition)
W7 (MK verification) — after W4 (checks propagation)
```

### Per-workstream protocol
1. **Read all affected files** before editing any.
2. **Edit surgically**: change the minimum needed. Do not rewrite surrounding prose.
3. **Compile gate**: `pkill -9 -f pdflatex; sleep 2; make fast` after every 3 file edits. Zero errors required.
4. **Report**: After each workstream, state files edited, lines changed, and verification result.

### Context management for large files
`higher_genus.tex` (7472 lines) and `bar_cobar_construction.tex` (8131 lines) are too large to read in full. Strategy:
- Use targeted grep to find relevant sections
- Read only the ±30 line window around each hit
- Make surgical edits to those windows
- Never attempt to read > 500 contiguous lines of these files

### What you must NOT do
1. **Do NOT rewrite theorem statements inside `\begin{theorem}...\end{theorem}`.**
2. **Do NOT change proofs.** The mathematics is done. You are changing definitions, conventions, notation in prose, and table organization.
3. **Do NOT add new theorems or conjectures** (except the homotopy MK definition in W4, which is a reformulation, not new mathematics).
4. **Do NOT touch `chapters/frame/heisenberg_frame.tex`** — it is the gold standard.
5. **Do NOT touch `main.tex` preamble** unless adding a new macro for W2 (`\tiltcat` or similar for the tilting category).
6. **Do NOT add motivational paragraphs.** You are tightening, not expanding.
7. **Do NOT change `\ClaimStatus` tags.** The census is stable.
8. **Do NOT change bibliography.** It is complete.
9. **Do NOT plan.** Open the first file and edit it. The plan is this prompt.

### Compile and verify at session end
```bash
pkill -9 -f pdflatex; sleep 2; make fast  # zero errors
grep -rc '\\dfib\|\\Dg\|\\dzero\|\\mcurv' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "New notation uses:",s}'  # should be >> 63
grep -rc 'ClaimStatusProvedHere\|ClaimStatusProvedElsewhere\|ClaimStatusConjectured' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "Total claims:",s}'  # should be unchanged (~1186)
```

## Begin

Start with Workstream 1. Grep for ambiguous differential notation in `poincare_duality_quantum.tex`. Read the hits. Edit them. Move to the next file.
