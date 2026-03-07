# SESSION PROMPT v15 — RESCULPTING

## Identity
You are the research collaborator specified in CLAUDE.md (triple-intersection: Serre/Grothendieck + Witten/Costello + Polyakov/Dirac). Read CLAUDE.md fully before proceeding.

## Mission
Execute the **immediate resculpting** of the monograph's proof architecture. The notes (raeeznotes2-7) converge on one diagnosis: the theorematic core is real but the proof graph has dependency cycles, contradictions, and status drift that are fatal at referee level. This session fixes the architecture, not the ambition.

## Pre-flight
1. Read CLAUDE.md, MEMORY.md, CONSTRAINT_MAP.md
2. Fresh census: `grep -rc 'ClaimStatus' chapters/ appendices/ --include='*.tex'`
3. Read all files before editing them

## The Eight Strikes — ordered by priority and dependency

### STRIKE 1: Kill the definition-theorem circularity [CRITICAL]
**Problem**: `def:chiral-koszul-pair` already requires bar/cobar quasi-isomorphisms that Theorem A then "proves." `def:modular-koszul-chiral` includes MK3 (inversion) and MK5 (complementarity) as axioms, then Theorems B/C prove those same statements, and the example propositions cite Theorems B/C to verify the definition. This is a dependency cycle.

**Files**: `chiral_koszul_pairs.tex` (def lines 65-97), `higher_genus.tex` (def lines 7924-7999, thm lines 1535-1595, 7706-7733, props 8005-8068)

**Action**:
1. Read `chiral_koszul_pairs.tex` fully. Find `def:chiral-koszul-pair`.
2. Replace it with a **recognition criterion** definition (call it "chiral Koszul datum" or "pre-Koszul pair"):
   - Candidate dual coalgebra C_i
   - Universal twisting morphism τ
   - Acyclicity of twisted Koszul complexes K_τ(A,C)
   - PBW/diagonal-Ext concentration for associated graded
   - Verdier compatibility on bar complex
3. Read `higher_genus.tex` fully. Find `def:modular-koszul-chiral`.
4. Replace with **modular pre-Koszul chiral algebra** whose axioms are genuinely antecedent:
   - MK1: genus-0 Koszulity (recognition criterion from above)
   - MK2: Verdier/factorization compatibility
   - MK4: higher-genus PBW / filtered modular control (central curvature, genus tower)
   - DELETE MK3 (inversion) and MK5 (complementarity) from the definition
5. Theorem A now PROVES bar/cobar identification from the recognition criterion
6. Theorem B now PROVES inversion from modular pre-Koszul hypotheses
7. Theorem C now PROVES complementarity from modular pre-Koszul hypotheses
8. Example propositions verify ONLY the antecedent hypotheses, never cite A/B/C for verification
9. Optionally define "modular Koszul chiral algebra" as one satisfying the conclusions — but this is a theorem about pre-Koszul objects, not a definition used by the theorems

**Constraint**: Do not change the mathematical content of the proofs. Only reorganize the logical dependency: hypotheses → theorems → consequences.

### STRIKE 2: Fix the false citation in Theorem A's proof [HIGH]
**Problem**: The proof of `thm:bar-cobar-isomorphism-main` cites `thm:bar-nilpotency-complete` (which proves d²=0) and claims it establishes bar concentration in degree 0. It does not.

**Files**: `higher_genus.tex` (proof lines 1627-1636), `bar_cobar_construction.tex` (thm lines 562-597), `chiral_koszul_pairs.tex`

**Action**:
1. Add a genuine **bar concentration theorem** in `chiral_koszul_pairs.tex`:
   - Statement: Under the recognition criterion, H^i(B̄_ch(A₁)) = 0 for i≠0, H^0 ≅ A₂!
   - Proof sketch: Filter bar complex by conformal weight/bar length → associated graded = classical Koszul complex → invoke classical diagonal concentration (BGS/Priddy) → lift by spectral sequence comparison
2. Fix the proof of Theorem A to cite this new theorem instead of `thm:bar-nilpotency-complete`

### STRIKE 3: Eliminate the bar-cobar "for any algebra" contradiction [CRITICAL]
**Problem**: One place states Ω(B̄(A)) ≃ A "always true for any algebra A." Another states it only on the Koszul/completed locus. Direct contradiction.

**Files**: `bar_cobar_construction.tex` (rem:fundamental-distinction lines 4624-4633), `deformation_theory.tex` (thm:bar-cobar-resolution lines 1362-1383, "Hochschild via bar-cobar" lines 247-253)

**Action**:
1. Read both files. Locate all "for any chiral algebra" bar-cobar inversion statements.
2. Rewrite `rem:fundamental-distinction`:
   - "Always true: bar and cobar constructions exist and d²=0"
   - "On the Koszul/completed locus only: the counit is a quasi-isomorphism"
3. Scope `thm:bar-cobar-resolution` to require Koszul hypothesis (or coderived completed sense off it)
4. Fix the Hochschild computation theorem to use the scoped version

### STRIKE 4: Repair Theorem C's fiber-cohomology lemma [HIGH]
**Problem**: `lem:fiber-cohomology-center` proves vanishing only "when restricted to the degree-0 bar component," but Theorem C needs the full fiber cohomology sheaf concentrated in degree 0.

**Files**: `higher_genus.tex` (lemma lines 4982-5067, theorem `thm:quantum-complementarity-main`)

**Action**:
1. Read the lemma and its proof carefully.
2. Strengthen Step 4 to prove total fiber-cohomology concentration:
   - Filter the full fiber bar complex by bar degree
   - Identify associated graded with Koszul/Ext complex
   - Show spectral sequence collapses: only total degree 0 survives
   - Conclude full local system is Z(A) ⊗ C̄
3. If this full theorem cannot be proved, weaken Theorem C accordingly and add a scope remark

### STRIKE 5: Unify Hochschild duality [HIGH]
**Problem**: Two inequivalent formulations exist: CH_n(A₁) ≅ CH_n(A₂)^∨ ⊗ ω_X[2] vs HH^n_chiral(A) ≅ HH^{2-n}_chiral(A!)^∨ ⊗ ω_X. One preserves degree with [2]-shift; the other reflects degree. Both cannot be correct as stated.

**Files**: `higher_genus.tex` (cor:hochschild-duality lines 1717ff), `deformation_theory.tex` (thm:main-koszul-hoch lines 452-505), `hochschild_cohomology.tex` (lines 694-704)

**Action**:
1. Read all three files at the relevant locations.
2. Pick ONE definitive object-level theorem:
   ```
   RHH_chiral(A) ≃ RHom(RHH_chiral(A!), ω_X[2])
   ```
3. Derive whichever group-level formulas are intended by taking cohomology with ONE fixed bigrading convention
4. Delete/replace the competing formulation
5. Ensure downstream citations (cyclic homology chapters) use the canonical version

### STRIKE 6: Split Theorem D — scalar proved vs full conjectural [MEDIUM-HIGH]
**Problem**: Theorem D mixes proved scalar package (κ(A), {F_g(A)}) with separately proved but non-scalar Δ_A and conjectural Θ_A. The introduction overstates.

**Files**: `higher_genus.tex` (def:modular-characteristic-package lines 8089-8116, thm:modular-characteristic lines 8127-8177), `introduction.tex`

**Action**:
1. Split Definition def:modular-characteristic-package into:
   - **Scalar modular characteristic system** (κ(A), {F_g(A)}): \ClaimStatusProvedHere
   - **Spectral discriminant** Δ_A: separate theorem/corollary
   - **Full modular homotopy package** (κ, {F_g}, Δ, Θ_A): \ClaimStatusConjectured for the non-scalar completion
2. Restate Theorem D as: "The scalar modular characteristic system is determined by κ(A), with universal genus formula (Â-genus), additivity, and duality law κ+κ'=0."
3. Present Θ_A as a programme-level conjectural enhancement, not part of the proved theorem
4. Update introduction.tex framing accordingly

### STRIKE 7: Global claim-status propagation [MEDIUM]
**Problem**: Chapter 34 (concordance) has the honest status logic; earlier chapters have not caught up. Status tags, theorem/conjecture boundaries, and census numbers drift.

**Action**:
1. After completing Strikes 1-6, do a full source audit:
   - Every `\ClaimStatusProvedHere` item must have a complete proof and not contain conjectural ingredients
   - Every definition containing conjectural data must not be tagged ProvedHere
   - Every example proposition must verify hypotheses, not conclusions
2. Fix any remaining `Rep(U_q(g))` → `C(U_q(g))` in KL contexts (propagate from chiral_modules.tex canonical version)
3. Fix any remaining "for any chiral algebra" bar-cobar statements (from Strike 3)
4. Run fresh census and update CLAUDE.md

### STRIKE 8: Conjecture stratification [MEDIUM]
**Problem**: ~94 conjectures sit in one flat list. Foundational missing pieces, reachable extensions, and physics horizons are not peers.

**Action**:
1. In `concordance.tex` or a new front-matter section, add a conjecture stratification:
   - **Tier 1 — Foundational**: full Θ_A, one flagship PBW degeneration, coderived Ran formalism
   - **Tier 2 — Consequence**: full DK, KL-from-bar-cobar stages, shifted-symplectic enhancement
   - **Tier 3 — Physics horizon**: BV=bar, path integral, holographic, E_n extension
2. Add a brief remark to each CJ claim indicating its tier (can be done as scope remarks)

---

## Execution Protocol

### Order of operations
Strikes 1-4 are interdependent and form the core repair. Execute in order:
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

### Per-strike protocol
1. Read ALL relevant files completely before writing
2. Draft changes mentally, checking for downstream breakage
3. Make edits
4. After each strike: `pkill -9 -f pdflatex; sleep 2; make fast` to verify compilation
5. If compilation fails, fix immediately before proceeding

### After all strikes
1. Full build: `pkill -9 -f pdflatex; sleep 2; make`
2. Fresh census
3. Update CLAUDE.md census numbers and status
4. Update MEMORY.md with session results
5. Git commit with descriptive message

### What NOT to do
- Do not change mathematical content of proofs (only reorganize logical dependencies)
- Do not add new theorems beyond what is needed (bar concentration theorem in Strike 2 is the exception)
- Do not touch notation/macros in the preamble unless required
- Do not rewrite proofs that are currently correct
- Do not add packages or change document class
- Do not expand conjectures or add new programme material
- Do not change the frame chapter or introduction beyond status-alignment fixes
- Keep edits minimal and surgical — the goal is architectural repair, not rewriting

### Estimated scope
- Strike 1: ~200 lines changed across 2 files
- Strike 2: ~80 lines added to 1 file, ~10 lines fixed in 1 file
- Strike 3: ~40 lines changed across 2 files
- Strike 4: ~60 lines changed in 1 file
- Strike 5: ~100 lines changed across 3 files
- Strike 6: ~80 lines changed across 2 files
- Strike 7: grep-driven audit, ~50 scattered fixes
- Strike 8: ~60 lines added to 1 file

Total: ~700 lines of surgical edits across ~10 files. This is a 1-session task.
