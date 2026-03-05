# CLAUDE.md — Chiral Bar-Cobar Monograph

## Identity

Mathematical collaborator for Raeez Lorgat's research monograph:

**Chiral Duality in the Presence of Quantum Corrections: Geometric Realizations via Configuration Spaces**

Target: Annals of Mathematics / Astérisque. Every definition precise, every theorem proved, every construction functorial.

Think like a research mathematician: "is this proved? What hypotheses? Where used?" Write like Serre: concise, complete, no gaps.

---

## The Book

### Core Thesis
Classical Koszul duality (bar-cobar adjunction) lifts to chiral/vertex algebras via configuration space integrals on algebraic curves. Geometric mechanism: Verdier duality on Fulton-MacPherson compactifications, mediated by non-abelian Poincare duality (Ayala-Francis). Genus 0 recovers Beilinson-Drinfeld. Genus g >= 1: quantum corrections controlled by H*(M_g) give geometric origin to central extensions, anomalies, curved A-infinity structures.

### The Engine — Prism Principle (PROVED)
Configuration spaces decompose a chiral algebra into its operadic spectrum. Log forms on FM compactifications provide propagators; residues extract OPE data; Arnold relations ensure d^2 = 0. Verdier duality exchanges bar and cobar. Proved as operadic Koszul duality: genus-0 via HyCom <-> Grav, all genera via Feynman transform of modular operad.

### Three Main Theorems — ALL PROVED
1. **(A) Geometric Bar-Cobar Duality**: Bar and cobar functors via configuration space integrals form an adjoint pair. For Koszul chiral algebras, the adjunction is an equivalence. [PROVED: thm:bar-cobar-isomorphism-main]
2. **(B) Bar-Cobar Inversion**: For Koszul A, Omega(B(A)) -> A is a quasi-isomorphism. Spectral sequence collapses at E_2. [PROVED: thm:higher-genus-inversion]
3. **(C) Deformation-Obstruction Complementarity**: Q_g(A) + Q_g(A!) = H*(M_g, Z(A)). What one algebra sees as deformation, its dual sees as obstruction. Kodaira-Spencer map constructed for all Koszul pairs. [PROVED: thm:quantum-complementarity-main, thm:kodaira-spencer-chiral-complete]

### Architecture
- **Part 1: Theory** — Foundations, configuration spaces, bar-cobar, NAP duality, higher genus, Koszul pairs, deformation theory, E_1-chiral framework
- **Part 2: Examples** — Lattice engine, free fields, Kac-Moody, W-algebras, deformation quantization, yangians, toroidal/elliptic, genus expansions (half the book by intent)
- **Part 3: Connections** — NAP computations, Feynman diagrams, BV-BRST, holomorphic-topological, physical origins, concordance

---

## Current State (Mar 2026)

### Census (verified fresh grep, Mar 5)
| Category | Count |
|----------|-------|
| ProvedHere | **653** |
| ProvedElsewhere | **314** |
| Conjectured | **85** |
| Heuristic | **16** |
| Open | **0** |
| **Total tagged claims** | **1068** |

Note: census counts occurrences (`grep -rco --include='*.tex'`) in chapters/ and appendices/ only.

### Compilation
- **1179 pages** (converged), zero LaTeX errors, zero undefined references, zero undefined citations, zero multiply-defined labels
- 55 active .tex files + 8 stubs (+ main.tex preamble), 72.5K lines of LaTeX
- Bibliography: 272 entries (1226 lines), all citations resolved
- Reference library: 38 PDFs in references/ (64 MB)
- Cosmetic: 109 overfull hbox (0 severe >30pt, worst 12.2pt), 79 underfull hbox
- Build: up to 7-pass pdflatex with convergence detection; `scripts/build.sh` for standalone use
- **CAUTION**: A hook/watcher spawns competing pdflatex on file edits; kill before manual builds
- Subject index: 329+ entries across 37 files
- Master Table of Computed Invariants in examples_summary.tex
- TikZ concept diagrams in introduction.tex (§Dictionary, §NAP foundation)
- CONSTRAINT_MAP.md: 33-entry reference registry (22 SATISFIED, 6 FRONTIER)

### Work History
- Content extraction, notation unification, de-duplication, math corrections, compilation
- Comprehensive mathematical audits; all Open claims resolved (40 → 0)
- Structural reorganization, conjecture reduction, bibliography completion
- Subject index (329 entries), Master Table, Leitfaden
- sl₂/Vir/W₃ genus-1 pipelines, central charge complementarity theorem
- Genus universality theorem, "Three Theorems in Action" showcase
- Complete appendix audit (14/14), full codebase cross-audit (all 55 files)
- P∞ vs Coisson distinction corrected throughout
- "Three Theorems Interlock" narrative section in introduction.tex
- Proof sketch campaign (sessions 70-83); conjecture + cross-ref audits clean
- Adversarial audit (session 2): 16 findings (3 errors, 1 contradiction, 7 gaps, 5 expository), ALL FIXED
- Adversarial audit (session 3): 35 findings from 8 parallel agents. 12 priority fixes applied: W-algebra duality σK formula, FP formula, proof integral, g=0 nilpotence, free field κ≠0, Heisenberg dual, H²(M̄_g), Yangian Ext, bosonic string gloss, KL diagram, modular periodicity downgrade, conformal block rationality caveat
- Adversarial audit (session 4): 45+ findings from 7 parallel agents. 17 fixes applied: genus-1 d²=0 full proof, Leray fibration notation, propagator antisymmetry removal, obstruction degree clarification, nilpotent citation scope, fermionic coproduct sign, Koszul pair equivalence sketch, HH⁰/obstruction language, Heisenberg bar computation, W-algebra simplicity≠semisimplicity, Heisenberg dual table (CE→Sym^ch), Yangian bar description, boundary divisor H²|I|-2→H², MMM vs λ-class naming, W₃ obstruction Mumford isomorphism correction, ProvedElsewhere→ProvedHere tag, ℏ convention reconciliation

### Proof Sketches: 1 REMAINING (correctly so)
| File | Line | Context | Status |
|------|------|---------|--------|
| holomorphic_topological.tex | 77 | CL → chiral algebra conditions | Conjectured (physics) — correctly a sketch |

*7 former sketches resolved to full proofs in this session (higher_genus ×3, bar_cobar ×2, poincare_duality ×1, poincare_duality_quantum ×1).*

### What Remains — 85 Conjectured Claims

All have scope remarks. Classification:

| Category | Count | Action |
|----------|-------|--------|
| **PHYSICS** | ~30 | Correctly scoped — outside pure math |
| **BORDERLINE PROVABLE** | ~4 | Provable in principle; substantial new work |
| **GENUINELY OPEN** | ~5 | Actual open mathematical problems |
| **COMPUTATIONAL** | ~3 | Explicit calculations not yet carried out |
| **SCOPE-REMARK REFS** | ~30 | Re-references of above in scope remarks |

**Borderline provable**: chiral Kontsevich (all-orders Stokes), EO recursion (axiom verification), general m_k (all-genus propagator), affine periodicity at critical level

**Genuinely open**: Virasoro/W_infinity Koszul dual (3), reflected modular periodicity (2), derived bc-betagamma
**Recently resolved**: obs_g^2=0 for g>=3 → PROVED via Mumford's relation (thm:obstruction-nilpotent-all-genera)

**Physics conjectures (~30)**: holomorphic_topological.tex (13), bv_brst.tex (4), free_fields.tex (18), physical_origins.tex (3), koszul_pair_structure.tex (8). All with scope remarks.

**Conjectures by Part**: Theory 24, Examples 34, Connections 26, Appendices 1.

**WARNING**: Always verify census with `grep -r 'ClaimStatus...' chapters/ appendices/ --include='*.tex' | wc -l` (the `--include` flag is critical to avoid counting .aux files).

**WARNING**: Always verify against fresh `grep -c ClaimStatusConjectured` before acting.

**WARNING**: Always verify against fresh `grep -c ClaimStatusConjectured` before acting.

### Structural Issues
- **Thm 5.10.1 ↔ 7.16.4 dependency**: Resolved. Theorem split into genus-0 clause (2a, self-contained in bar_cobar_construction.tex) and higher-genus clause (2b, proved by induction in higher_genus.tex). Remark rem:proof-dependency-linear documents the linear structure.

---

## How to Work

### Session Protocol
1. Read this file + MEMORY.md + session_log.md + CONSTRAINT_MAP.md for current state
2. Run fresh census (`grep -rc` for all claim statuses)
3. Read all relevant source files before writing
4. Write mathematics in theorem-proof format
5. After each change: verify `make fast` compiles cleanly
6. After each batch (10 edits): run `make fast` as gate
7. At session end: full `make` (3-pass), update MEMORY.md + session_log.md
8. Never guess a formula — compute it or cite it

### Autonomous Loop (for unattended operation)
See `notes/SESSION_PROMPT_v8.md` for the current unified session prompt (state-driven mode selection, subsumes v1-v7 + specialized prompts). Launch with:
```
Read notes/SESSION_PROMPT_v8.md and execute it.
```
All prior prompts (v1-v7) and specialized prompts archived in `notes/archive/`.

### Mathematical Standards
- Every theorem gets a complete proof. "Sketch" and "the proof is similar" are temporary.
- Definitions before use. Functoriality is not optional. Examples are not decoration.
- Notation: A for chiral algebras, A^! for Koszul dual, B(A) for bar, Omega(C) for cobar, C_n(X) for configuration space, FM_n(X) for FM compactification, M_g for moduli, kappa for level, c for central charge.
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured

### Writing Standards
- Voice: impersonal ("we construct," "one verifies")
- Label everything: \label{def:}, \label{thm:}, \label{prop:}, etc.
- Cross-reference with \ref and \eqref, never hardcoded numbers

### LaTeX Standards
- Document class: memoir, EB Garamond via newtxmath + ebgaramond
- Compile: `make` (6 pdflatex passes), `make fast` (1 pass), `make clean`
- Chapter files: \include from main.tex; sub-files: \input
- All macros in main.tex preamble — NEVER \newcommand in chapter files
- Key macros: \chirAss, \chirCom, \chirLie, \Eone, \Einf, \Pinf, \B (bar), \cA (chiral algebra)

### What NOT to Do
- Do not add packages without checking preamble compatibility
- Do not change document class or font setup
- Do not create new .tex files when content belongs in existing chapter
- Do not duplicate definitions — reference from Part 1
- Do not use \newcommand in chapter files
- Do not add TODO comments — track externally
- Do not change verified formulas (see next section)

---

## Critical Pitfalls — VERIFIED FACTS

Reference facts. Verify against source before editing.

### Grading and Conventions
- Manuscript uses COHOMOLOGICAL grading: |d| = +1 (Loday-Vallette uses homological)
- Bar construction uses DESUSPENSION: B(A) = T^c(s^{-1}A-bar, d) in cohomological convention
- Suspension: sV = V[-1] under V[n]^k = V^{k+n}
- Terminology: "strict" not "on-nose" for d^2=0

### Koszul Duality
- Com^! = Lie (NOT coLie)
- Sym^! = Lambda (exterior), NOT commutative again
- Koszul dual coalgebra: SUB-coalgebra of cofree (cogenerated by R-perp), NOT quotient
- Heisenberg is NOT self-dual: H^! = Sym^ch(V*) (commutative chiral), NOT H_{-k}
- Free fermion dual: F^! = beta-gamma (Lie<->Com duality), NOT Heisenberg
- bc-betagamma is a 2-generator duality (dim V=2)
- Bosonization != Koszul duality (bc has 2 generators, Heisenberg has 1)

### P∞-Chiral vs Coisson — CRITICAL DISTINCTION
- **Coisson algebra** (BD) = Poisson vertex algebra (PVA) = commutative D_X-algebra + Lie* bracket (λ-bracket). It is NOT a chiral algebra. Has no OPE, no chiral operations. Only a single λ-bracket on a commutative algebra.
- **P∞-chiral algebra** = TWO compatible chiral-operad structures: chirCom (commutative chiral product) + chirLie (chiral Lie bracket), with Leibniz. Since chirCom^! = chirLie, the two structures are presented across Koszul dual frames. It IS a chiral algebra (already an E∞-chiral algebra with extra L∞ structure).
- **Deformation quantization levels**:
  - Coisson (classical, no OPE) → quantize → E∞-chiral (vertex algebra, "singly quantum")
  - P∞-chiral (E∞ + L∞, already has OPE) → quantize → E₁-chiral (nonlocal VA, "doubly quantum")
- P∞-chiral and Coisson live at different levels of quantization.

### Central Charges and Levels
- Sugawara: T = (1/2(k+h-dual))Sum :J^a J^a:, c = k*dim(g)/(k+h-dual)
- Sugawara UNDEFINED at critical level k=-h-dual (not "c diverges")
- Feigin-Frenkel: k <-> -k-2h-dual (NOT -k-h-dual)
- Level shift: -kappa-2h-dual is correct for vertex algebra convention
- Virasoro DS: c = 1 - 6(k+1)^2/(k+2); W_3 DS: c = 2 - 24(k+2)^2/(k+3)
- DS formula != minimal model formula (different parametrizations)
- KM periodicity: 2h (Coxeter), NOT 2h-dual (dual Coxeter) — differ for non-simply-laced
- KM periodicity rank>1: "period 2h for all g" is WRONG — sl_2 is 4-periodic but sl_3 is NOT 6-periodic (dim CH^12 != dim CH^6). Rank-1 periodicity + higher-rank polynomial-exterior structure.
- h-dual(g-dual) = h-dual(g) ONLY for simply-laced; B_n: h-dual=2n-1, C_n: h-dual=n+1

### Curved and A-infinity
- A-infinity: Sum_{r+s+t=n} (-1)^{rs+t} m_{r+1+t}(id^r tensor m_s tensor id^t) = 0
- Curved A-infinity: m_1^2(a) = m_2(m_0,a) - m_2(a,m_0) = [m_0,a] (COMMUTATOR, MINUS sign)
- Bar differential always d^2=0; curvature shows as m_1^2 != 0

### Geometry
- FM compactification: C-bar_n(X) = Bl (blowup along diagonals), NOT X^n \ Delta
- M-bar_{0,5} = Bl_4(P^2) (del Pezzo degree 5), dim H^2 = 5 (NOT P^2)
- P^n != S^{2n} for n >= 2 (different cohomology)
- Prime form E(z,w) is section of K^{-1/2} boxtimes K^{-1/2} (NOT K^{+1/2})
- Normal bundle N_{Delta_S/X^n} = direct-sum T_X (tangent), NOT T_X*
- Vol(M-bar_g) ~ (2g)! (Mirzakhani), NOT e^{Cg}

### Physics Formulas
- QME: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2)
- HCS action: Tr(A-bar wedge dbar A + (2/3)A-bar wedge [A-bar,A-bar]) — coefficient 2/3
- W_3 composite: Lambda = :TT: - (3/10)partial^2 T (MINUS sign)
- Virasoro central extension is Lie algebra 2-COCYCLE (not 3-cocycle)

See MEMORY.md "Known Verified Formulas" for the complete list (~100 entries).

---

## File Map

### Part 1: Theory (chapters/theory/) — 34K lines, 355 PH / 150 PE / 24 CJ
| File | Lines | PH | PE | CJ | Notes |
|------|------:|---:|---:|---:|-------|
| introduction.tex | 1444 | 17 | 2 | 0 | Main results, Leitfaden, E_1/E_inf dictionary |
| algebraic_foundations.tex | 1325 | 5 | 9 | 0 | Classical Koszul duality, operads, Weiss covers |
| configuration_spaces.tex | 3942 | 42 | 29 | 0 | C_n(X), FM compactification, OS algebra |
| bar_cobar_construction.tex | 7146 | 78 | 16 | 2 | Bar/cobar functors, d^2=0, Verdier — **core chapter** (1 Heur) |
| poincare_duality.tex | 677 | 7 | 1 | 0 | Verdier duality, bar-computes-dual |
| poincare_duality_quantum.tex | 1091 | 6 | 12 | 6 | Quantum corrections, modular operad, Feynman transform |
| higher_genus.tex | 6824 | 93 | 21 | 6 | Genus-g bar, Main Theorems B+C, KS — **deepest** |
| chiral_koszul_pairs.tex | 2234 | 15 | 8 | 2 | Koszul pair theory, E_1 duality theorem |
| koszul_pair_structure.tex | 1602 | 15 | 14 | 8 | Periodicity, affine/Virasoro structure |
| chiral_modules.tex | 4160 | 41 | 14 | 0 | Module categories, rep theory, E_1 module Koszul duality |
| deformation_theory.tex | 1382 | 16 | 3 | 3 | Deformation-obstruction, curved A-infinity |
| hochschild_cohomology.tex | 699 | 7 | 16 | 0 | Hochschild-cyclic spectral sequence |
| quantum_corrections.tex | 347 | 1 | 0 | 0 | Quantum correction formulas |
| filtered_curved.tex | 304 | 1 | 1 | 0 | Filtered-curved hierarchy |
| koszul_across_genera.tex | 363 | 4 | 0 | 0 | (absorbed into higher_genus) |
| classical_to_chiral.tex | 452 | 6 | 4 | 0 | (absorbed into introduction) |

*Stubs (5 lines each, placeholders): bar_cobar_quasi_isomorphism.tex, higher_genus_full.tex, higher_genus_quasi_isomorphism.tex*

### Part 2: Examples (chapters/examples/) — 27.2K lines, 237 PH / 85 PE / 34 CJ
| File | Lines | PH | PE | CJ | Notes |
|------|------:|---:|---:|---:|-------|
| lattice_foundations.tex | 1501 | 17 | 3 | 0 | Lattice VOA engine |
| free_fields.tex | 3540 | 44 | 11 | 18 | Heisenberg, fermion, beta-gamma, bc |
| beta_gamma.tex | 1390 | 15 | 4 | 0 | beta-gamma bar complex, spectral sequence |
| heisenberg_eisenstein.tex | 877 | 7 | 5 | 0 | Heisenberg genus expansion, Eisenstein |
| kac_moody_framework.tex | 2404 | 28 | 10 | 1 | Affine KM: screening, Wakimoto, admissible, Whittaker |
| w_algebras_framework.tex | 2298 | 18 | 9 | 2 | W-algebra Koszul duality, logarithmic |
| w3_composite_fields.tex | 1023 | 13 | 2 | 0 | W_3 composite Lambda, weight-6, null vectors, Kac det |
| w_algebras_deep.tex | 997 | 3 | 4 | 0 | W₃ degree-3 bar, BP bar, DS hierarchy |
| minimal_model_fusion.tex | 822 | 12 | 8 | 0 | Verlinde formula, fusion tables, MTC |
| deformation_quantization.tex | 1169 | 4 | 12 | 1 | Chiral Kontsevich, formality, star products |
| deformation_examples.tex | 744 | 2 | 6 | 0 | Coisson, star product, lattice/symplectic fermion DQ |
| yangians.tex | 1243 | 12 | 1 | 3 | RTT, E_1 Yangian, Koszulness, Coulomb branch, Y(sl₃) |
| toroidal_elliptic.tex | 1355 | 5 | 4 | 3 | Double affine, Fay d²=0, elliptic R-matrix, shuffle |
| genus_expansions.tex | 2344 | 30 | 2 | 4 | **Three Theorems showcase**: sl₂, Vir, W₃, genus-2 |
| detailed_computations.tex | 3684 | 18 | 0 | 0 | sl_3 bar, W_3, fermion, E₈, Vir deg 4-5, G₂, BGG |
| examples_summary.tex | 1073 | 8 | 1 | 2 | Master Table, bar dimensions, spectral data |
| minimal_model_examples.tex | 677 | 1 | 3 | 0 | Ising, tricritical Ising, three-state Potts, bar-fusion |

*Stubs (5 lines each, placeholders): kac_moody_computations.tex, obstruction_classes.tex, heisenberg_higher_genus.tex, deformation_quantization_complete.tex, w_algebras_computations.tex*

### Part 3: Connections (chapters/connections/) — 4.9K lines, 24 PH / 27 PE / 26 CJ
| File | Lines | PH | PE | CJ | Notes |
|------|------:|---:|---:|---:|-------|
| feynman_diagrams.tex | 1264 | 6 | 3 | 0 | Feynman diagram interpretation (9 Heur) |
| holomorphic_topological.tex | 1123 | 6 | 8 | 13 | HT theories, AGT, 4d/2d |
| bv_brst.tex | 739 | 5 | 7 | 4 | BV-BRST formalism (4 Heur) |
| genus_complete.tex | 576 | 3 | 5 | 5 | Complete genus theory, EO recursion |
| feynman_connection.tex | 447 | 0 | 1 | 1 | Feynman-bar-cobar bridge |
| poincare_computations.tex | 310 | 1 | 0 | 0 | NAP explicit computations |
| physical_origins.tex | 166 | 0 | 3 | 3 | NC Chern-Simons, D-branes |
| concordance.tex | 312 | 2 | 0 | 0 | Literature comparison (BD, FG, AF, CG, LV) |

### Appendices (appendices/) — 6.3K lines, 35 PH / 52 PE / 1 CJ
14 files: arnold_relations (1049), signs_and_shifts (713), sign_conventions (558), spectral_sequences (549), koszul_reference (596), existence_criteria (712), homotopy_transfer (456), nilpotent_completion (475), dual_methodology (241), notation_index (428), computational_tables (185), theta_functions (78), spectral_higher_genus (163), general_relations (136)

### Bibliography
bibliography/references.tex — 1226 lines, 272 entries, all citations resolved

### Planning & Automation (notes/ — 4 active files)
SESSION_PROMPT_v8.md — Current unified session prompt: state-driven mode selection, subsumes v1-v7
HORIZON.md — Implied results map (20/20 Level A done, 22/24 Level B done)
DEEP_CRITIQUE_OUTPUT.md — Referee gap analysis (ALL F1-F7 RESOLVED)
autonomous_state.md — Session continuity state (canonical)

Archive (notes/archive/): 21 superseded files including all prior prompts (v1-v7), specialized prompts (DEEP_CRITIQUE, ADVERSARIAL_AUDIT, STRATEGIC_SYNTHESIS, EXPLORATION_ENGINE, COMPUTE_ENGINE), absorbed maps (IMPLIED_RESULTS_MAP, RESTRUCTURING_PROPOSAL), session snapshots, and historical audit outputs.

### Reference Library (references/)
CONSTRAINT_MAP.md — 33-entry machine-readable registry (22 SATISFIED, 6 FRONTIER)
38 PDFs — 64 MB of source material (BD04, LV12, AF15, FG12, CG17, etc.)
