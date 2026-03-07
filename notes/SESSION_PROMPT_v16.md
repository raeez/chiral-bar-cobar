# SESSION PROMPT v16 — DEEP PERVASIVE DISSEMINATION

## Identity
You are the research collaborator specified in CLAUDE.md. Triple-intersection: Serre/Grothendieck + Witten/Costello + Polyakov/Dirac. Read CLAUDE.md and MEMORY.md fully before proceeding.

## Mission
Execute deep pervasive dissemination of the material consequences of raeeznotes2-9 across the ENTIRE manuscript (55+ .tex files, 75K+ lines). Touch every file. The v15 resculpting campaign fixed the critical proof architecture (circularity, false citations, fiber-cohomology, Hochschild duality, Theorem D split, conjecture stratification). This session propagates the REMAINING consequences — homotopy-native formulations, periodicity profiles, prose quality, parameter-source precision, coderived ambient, and Programme branding — into every chapter, example, connection, and appendix.

## Pre-flight
1. Read CLAUDE.md, MEMORY.md
2. Fresh census: `grep -rco 'ClaimStatus...' chapters/ appendices/ --include='*.tex'`
3. Read all files before editing them
4. Kill watcher: `pkill -9 -f pdflatex; sleep 2`

## COMPLETED (v15 + prior sessions — DO NOT REDO)
- Definition-theorem circularity killed (Strike 1)
- Bar concentration theorem added, false citation fixed (Strike 2)
- "For any algebra" contradiction fixed (Strike 3)
- Fiber-cohomology lemma strengthened (Strike 4)
- Hochschild duality unified (Strike 5)
- Theorem D split: scalar proved, Theta conjectural (Strike 6)
- Global claim-status audit (Strike 7)
- Conjecture stratification in concordance.tex (Strike 8)
- Differential notation campaign: \dfib, \Dg{g}, \dzero deployed in 11 files
- KL target: Rep(U_q(g)) -> C(U_q(g)) fixed everywhere
- Parameter source: H^1(Sigma_g) not H^1(M_g) fixed
- MK4 split: unconditional (free fields) vs conditional (interacting)
- CG restructuring phases 1-3 complete
- Frame chapter (heisenberg_frame.tex) written

## WORK STREAMS — ordered by depth-of-impact

### WS-1: Homotopy-Native Reformulations [HIGH — 15+ files]
**Source**: raeeznotes3 edits 1-12, raeeznotes7 §§1-8, raeeznotes8 formal replacements

**What**: Every major theorem and definition should present the homotopy-native (derived/infinity-categorical) formulation FIRST, with the cohomological shadow as a corollary. The manuscript currently does the reverse in most places.

**Specific edits**:
1. **Complementarity as fiber sequence** (higher_genus.tex): After thm:quantum-complementarity-main, add a Remark stating the H/M/S hierarchy:
   - H-level: fiber sequence Def(A) -> H -> Def(A!) in DGCat
   - M-level: chain-level complementarity complex with explicit maps
   - S-level (current): Q_g(A) + Q_g(A!) = H*(M_g, Z(A)) [the shadow]
   Mark the S-level as "the cohomological shadow of Theorem C."

2. **Bar-cobar as derived adjunction** (bar_cobar_construction.tex): After thm:bar-cobar-isomorphism-main, add Remark on derived-categorical formulation:
   - B_ch and Omega_ch are adjoint functors between infinity-categories
   - The quasi-isomorphism is a unit/counit in the derived sense
   - Current theorem is the shadow on homotopy categories

3. **Deformation complex as cyclic L-infinity** (deformation_theory.tex): After the deformation-obstruction section, add Remark identifying Def(A) as underlying a cyclic L-infinity algebra (Kontsevich-Soibelman, Costello-Li).

4. **Modular characteristic as Maurer-Cartan** (higher_genus.tex): Near thm:modular-characteristic, add Remark that the full (conjectural) Theta_A is a universal MC element in Def_cyc(A) hat-tensor R\Gamma(M-bar, Q).

5. **Inversion as coderived equivalence** (higher_genus.tex): Near thm:higher-genus-inversion, add Remark that off the Koszul locus, bar-cobar still gives a coderived equivalence (coderived = Positselski sense).

**Protocol**: Add Remarks only — do NOT rewrite theorem statements. Each Remark is 8-15 lines of LaTeX. Label: rem:homotopy-native-X.

### WS-2: Periodicity Profile Pi(A) [MEDIUM-HIGH — 8+ files]
**Source**: raeeznotes4 §7, raeeznotes7 §7

**What**: Replace any remaining references to a scalar "Period(A)" with the periodicity profile Pi(A) = (M_A, Q_A, G_A) triple (module M_A of polynomial growth, exterior algebra Q_A of periodicity generators, Galois group G_A of splitting field).

**Specific edits**:
1. In koszul_pair_structure.tex: Ensure the periodicity discussion uses Pi(A) not a scalar period. Add Remark rem:periodicity-profile if not present.
2. In examples that compute periodicity (detailed_computations.tex, examples_summary.tex): State profile components, not just a single number.
3. In concordance.tex: Any periodicity conjectures should reference Pi(A).
4. In introduction.tex: If "Period(A)" appears in the dictionary, replace with Pi(A) or add clarification.

**Protocol**: Search `grep -rn 'Period(A\|period.*scalar' chapters/ --include='*.tex'` first. Only edit where scalar period language exists.

### WS-3: Prose Sculpting — Chriss-Ginzburg Standard [HIGH — all files]
**Source**: SESSION_PROMPT_v13, raeeznotes2 §exposition

**The 10 failure modes to eliminate** (from v13):
- F1: ANNOUNCEMENT — "We will now prove..." / "In this section we..." → CUT
- F2: REDUNDANT RE-DERIVATION — re-proving what was proved in an earlier chapter → compress to citation
- F3: PREAMBLE BLOAT — multi-paragraph motivation before a definition → move after or inline
- F4: BULLET-LIST SYNDROME — lists where flowing prose would be better → RESEQUENCE
- F5: HISTORICAL DIGRESSION — "Historically, Koszul (1950)..." → CUT or footnote
- F6: CONVENTION SCATTER — re-stating conventions from the preamble → CUT (reference Convention X)
- F7: DEAD TRANSITIONS — "Having established X, we now turn to Y" → CUT
- F8: PASSIVE HEDGING — "It might be noted that..." → direct assertion or CUT
- F9: EXPLAIN-THEN-STATE — explaining the theorem before stating it → STATE first, explain after
- F10: COMPUTATION WITHOUT NARRATIVE — pages of formulas with no guiding text → add 1-line bridges

**Protocol**: For each file, scan for F1-F10 patterns. Apply CUT/COMPRESS/BRIDGE/PUNCH operations. Target: 5-10% reduction per file in non-mathematical text. Do NOT touch proofs or theorem statements.

**Priority order**: Theory core (bar_cobar, higher_genus, chiral_koszul_pairs, deformation_theory) → Examples (free_fields, kac_moody, w_algebras) → Connections → Appendices.

### WS-4: Parameter-Source Diagram [MEDIUM — 2 files]
**Source**: raeeznotes3 edit 9, v14 W5

**What**: Add a commutative diagram (TikZ or display math) showing the parameter source chain:
```
H^1(Sigma_g, Z(A)) --pushforward--> H^0(M_g, R^1 pi_* Z(A)) --period--> H^1(M_g, Z_A^flat)
```
with annotations explaining which parameters are geometric (from the curve) vs modular (from the moduli space).

**Location**: higher_genus.tex, near Convention conv:higher-genus-differentials.

**Protocol**: One diagram, ~15 lines of LaTeX. Add after the convention block.

### WS-5: Coderived Model Appendix Stub [MEDIUM — 1 new file + main.tex]
**Source**: raeeznotes3 edit 7, raeeznotes7 §2

**What**: The manuscript references coderived/contraderived categories in several places but has no self-contained appendix. Create appendices/coderived_models.tex (~100 lines) with:
- Definition of coderived category D^co(A) (Positselski)
- Definition of contraderived category D^ctr(A)
- Key property: bar-cobar adjunction extends to D^co <-> D^ctr
- Reference: Positselski "Two kinds of derived categories"
- ClaimStatusProvedElsewhere for all claims (these are known results)

**Note**: appendices/coderived_models.tex already exists as untracked file. Read it first, extend if needed.

### WS-6: Physics Programme Branding [MEDIUM — 3 files]
**Source**: raeeznotes2 §branding

**What**: Chapters 29-31 (bv_brst.tex, holomorphic_topological.tex, physical_origins.tex) should be explicitly branded as "Programme" material — they describe research directions, not proved results. Add a brief Remark at the start of each chapter:

```latex
\begin{remark}[Programme status]
This chapter develops the physical interpretation of bar-cobar duality
as [BRST/holomorphic-topological/...] theory. The identifications in
\S\ref{...} are proved; the extensions in \S\ref{...} are conjectural
programme material (Tier 2--3 in the conjecture stratification of
Chapter~\ref{chap:concordance}).
\end{remark}
```

### WS-7: Master Table Stratification [MEDIUM — 1 file]
**Source**: v14 W3, raeeznotes4 §4

**What**: The Master Table of Computed Invariants in examples_summary.tex should be stratified by proof status:
- Tier A: Fully proved (kappa, central charge, bar dimensions for free fields)
- Tier B: Proved conditional on chiral Koszulness (bar dimensions for interacting)
- Tier C: Conjectural (spectral discriminant predictions, Yangian bar GF)

Add a column or footnote system indicating tier.

### WS-8: Regime Tags on Theorem Environments [LOW — scanning pass]
**Source**: raeeznotes2

**What**: Each major theorem should indicate its "regime" — genus-0, all genera, Koszul locus, completed/coderived. Not as formal metadata but as parenthetical in the theorem name:

```latex
\begin{theorem}[Bar-cobar inversion --- Koszul locus, all genera]
```

**Protocol**: Only add where the regime is not already clear from context. Skip if the theorem statement makes the hypotheses explicit.

### WS-9: Cross-Reference Tightening [LOW — scanning pass]
**Source**: raeeznotes3, general quality

**What**: Ensure every forward reference to a theorem has the correct label. Grep for `\\ref{thm:` and verify each target exists and is correctly scoped after the v15 changes (some labels may have changed).

**Protocol**: `grep -rn '\\ref{thm:' chapters/ --include='*.tex'` → verify each.

### WS-10: Differential Notation Completion [LOW — scanning pass]
**Source**: raeeznotes2, MEMORY.md

**What**: The differential notation campaign deployed \dfib, \Dg{g}, \dzero in 11 files. Verify ALL files that discuss higher-genus differentials use the correct macro. Grep for bare `d_g` or `d^2 = \kappa` or `d_{\mathrm{fib}}` that should be macro-ified.

**Protocol**: `grep -rn 'd_g\|d_{g}\|d_\\mathrm{fib}' chapters/ --include='*.tex'` → fix any non-macro occurrences.

## Execution Protocol

### Order of operations
WS-1 → WS-2 → WS-3 → WS-4 → WS-5 → WS-6 → WS-7 → WS-8 → WS-9 → WS-10

### Per-workstream protocol
1. Read ALL relevant files completely before writing
2. Draft changes mentally, check for downstream breakage
3. Make edits (prefer Edit tool, never Write for existing files)
4. After each workstream: `pkill -9 -f pdflatex; sleep 2; make fast` to verify compilation
5. If compilation fails, fix immediately before proceeding

### For WS-3 (prose sculpting) — execute as parallel agents per file group:
- Group A: Theory core (8 files)
- Group B: Examples (17 files)
- Group C: Connections + Appendices (22 files)

### After all workstreams
1. Full build: `pkill -9 -f pdflatex; sleep 2; make`
2. Fresh census
3. Update CLAUDE.md census numbers
4. Update MEMORY.md with session results
5. Git commit with descriptive message

### What NOT to do
- Do not change mathematical content of proofs
- Do not rewrite theorem statements (add Remarks instead)
- Do not add new theorems or conjectures
- Do not touch notation/macros in the preamble unless required
- Do not add packages or change document class
- Do not delete proved content
- Do not create new chapter files (appendix stub is the exception)
- Keep Remarks to 8-15 lines each — concise, not essays

### Estimated scope
- WS-1: ~120 lines added across 4 files (Remarks)
- WS-2: ~40 lines changed across 4-8 files
- WS-3: net -500 to -1000 lines across all files (cuts > additions)
- WS-4: ~15 lines added to 1 file
- WS-5: ~100 lines (new appendix or extend existing stub)
- WS-6: ~30 lines added across 3 files
- WS-7: ~30 lines changed in 1 file
- WS-8: ~30 one-line edits across 15 files
- WS-9: grep-driven verification, ~10 fixes
- WS-10: grep-driven verification, ~5 fixes

Total: ~400 lines added, ~700 lines cut. Net reduction. 18-24 hour autonomous session.
