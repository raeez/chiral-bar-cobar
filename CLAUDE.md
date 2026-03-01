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

## Current State (Mar 1, 2026 — Post Session 40)

### Census (verified fresh via grep -rF on .tex files)
| Category | Count |
|----------|-------|
| ProvedHere | **460** |
| ProvedElsewhere | **258** |
| Conjectured | **75** (59 distinct claims) |
| Open | **0** |

### Compilation
- **945 pages**, zero LaTeX errors, zero undefined references, zero undefined citations
- 16 cosmetic hyperref warnings ("Token not allowed in PDF string")
- ~51K lines across 55 active .tex files (+ main.tex preamble)
- Bibliography complete (all citations resolved)

### Phases Complete (40 sessions, ~1440 fixes)
- Phase 0-4: Content extraction, notation, de-duplication, math fixes, compilation
- Phase 5-6: Comprehensive mathematical audits
- Sessions 16-18: Open -> ProvedHere campaign (40 -> 0)
- Sessions 19-23: Five Transformative Moves (all executed), structural reorganization
- Sessions 24-39: Deep audit marathon, conjecture reduction (97 -> 75), bibliography completion
- Session 40: Comprehensive assessment, documentation overhaul, conjecture attack

### What Remains — The 59 Distinct Conjectured Claims

75 uses of \ClaimStatusConjectured in .tex files correspond to 59 distinct mathematical claims (some tags appear in scope remarks). All have scope remarks. Classification:

| Category | Count | Action |
|----------|-------|--------|
| **PHYSICS** | 28 | Correctly scoped — outside pure math |
| **PROVABLE** | 21 | Can be proved with existing infrastructure |
| **GENUINELY OPEN** | 7 | Actual open mathematical problems |
| **COMPUTATIONAL** | 3 | Explicit calculations not yet carried out |

**Provable conjectures by priority** (see notes/CONJECTURE_REGISTRY.md for full details):
- Tier 1 (high impact): Periodicity cluster (5 in deformation_theory.tex), chiral Kontsevich, P-infinity formality, deformation acyclicity
- Tier 2 (moderate): EO recursion, Virasoro Hochschild, QME = bar-cobar, bar = BRST, general m_k, spectral sequence genus, master identity, elliptic vs rational
- Tier 3 (partial): W-algebra bar-cobar items, affine periodicity at critical level, BV on chiral Hochschild

**Physics conjectures (28)**: Concentrated in holomorphic_topological.tex (10), bv_brst.tex (6), free_fields.tex (8), physical_origins.tex (3), koszul_pair_structure.tex (3). All appropriately labeled with scope remarks.

**Genuinely open (7)**: Virasoro/W_infinity Koszul dual (3), reflected modular periodicity (2), obs_g^2=0 for g>=3, derived bc-betagamma.

---

## How to Work

### Session Protocol
1. Read this file + MEMORY.md for current state
2. Read all relevant source files before writing
3. Write mathematics in theorem-proof format
4. After each change: verify `make` compiles cleanly (`make fast` for single pass)
5. Update MEMORY.md with what was accomplished
6. Never guess a formula — compute it or cite it

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
- Compile: `make` (3 pdflatex passes), `make fast` (1 pass), `make clean`
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

These errors have been made and corrected. DO NOT reintroduce them.

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

### Central Charges and Levels
- Sugawara: T = (1/2(k+h-dual))Sum :J^a J^a:, c = k*dim(g)/(k+h-dual)
- Sugawara UNDEFINED at critical level k=-h-dual (not "c diverges")
- Feigin-Frenkel: k <-> -k-2h-dual (NOT -k-h-dual)
- Level shift: -kappa-2h-dual is correct for vertex algebra convention
- Virasoro DS: c = 1 - 6(k+1)^2/(k+2); W_3 DS: c = 2 - 24(k+2)^2/(k+3)
- DS formula != minimal model formula (different parametrizations)
- KM periodicity: 2h (Coxeter), NOT 2h-dual (dual Coxeter) — differ for non-simply-laced
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

### Part 1: Theory (chapters/theory/)
| File | Lines | PH | PE | C | Notes |
|------|------:|---:|---:|--:|-------|
| introduction.tex | 1240 | 16 | 2 | 0 | Main results, E_1/E_inf dictionary, standing assumptions |
| algebraic_foundations.tex | 1340 | 5 | 9 | 0 | Classical Koszul duality, operads, Weiss covers |
| configuration_spaces.tex | 3880 | 40 | 29 | 0 | C_n(X), FM compactification, OS algebra |
| bar_cobar_construction.tex | 7201 | 80 | 14 | 0 | Bar/cobar functors, d^2=0, Verdier pairing — **core chapter** |
| poincare_duality.tex | 643 | 7 | 1 | 0 | Verdier duality, bar-computes-dual |
| poincare_duality_quantum.tex | 1059 | 6 | 11 | 6 | Quantum corrections, modular operad, Feynman transform |
| higher_genus.tex | 6356 | 83 | 17 | 7 | Genus-g bar complex, Main Theorem C, KS map — **deepest chapter** |
| chiral_koszul_pairs.tex | 2114 | 13 | 8 | 2 | Koszul pair theory, E_1 duality theorem |
| koszul_pair_structure.tex | 1300 | 11 | 11 | 8 | Periodicity, affine/Virasoro structure |
| chiral_modules.tex | 717 | 14 | 1 | 1 | Module categories, E_1 module Koszul duality |
| deformation_theory.tex | 1330 | 10 | 3 | 8 | Deformation-obstruction, curved A-infinity |
| hochschild_cohomology.tex | 644 | 5 | 16 | 1 | Hochschild-cyclic spectral sequence |
| quantum_corrections.tex | 381 | 1 | 0 | 0 | Quantum correction formulas |
| filtered_curved.tex | 314 | 1 | 1 | 0 | Filtered-curved hierarchy |
| koszul_across_genera.tex | 362 | 4 | 0 | 0 | Genus-graded Koszul duality (absorbed into higher_genus) |
| classical_to_chiral.tex | 462 | 6 | 4 | 0 | Three-level hierarchy (absorbed into introduction) |

Stubs (content merged elsewhere): bar_cobar_quasi_isomorphism, higher_genus_full, higher_genus_quasi_isomorphism

### Part 2: Examples (chapters/examples/)
| File | Lines | PH | PE | C | Notes |
|------|------:|---:|---:|--:|-------|
| lattice_foundations.tex | 1261 | 16 | 3 | 0 | Lattice VOA engine |
| free_fields.tex | 2790 | 39 | 12 | 14 | Heisenberg, fermion, beta-gamma, bc |
| beta_gamma.tex | 515 | 9 | 4 | 0 | beta-gamma system detail |
| heisenberg_eisenstein.tex | 530 | 5 | 2 | 1 | Heisenberg genus expansion, Eisenstein |
| kac_moody_framework.tex | 942 | 13 | 6 | 1 | Affine KM: screening, Wakimoto, A-infinity |
| w_algebras_framework.tex | 1207 | 9 | 6 | 1 | W-algebra Koszul duality |
| w3_composite_fields.tex | 421 | 4 | 1 | 0 | W_3 composite Lambda |
| w_algebras_deep.tex | 170 | 1 | 4 | 0 | Flag varieties, jet geometry |
| minimal_model_fusion.tex | 350 | 2 | 5 | 0 | Verlinde formula, fusion tables |
| deformation_quantization.tex | 828 | 3 | 10 | 4 | Chiral Kontsevich, formality |
| deformation_examples.tex | 178 | 0 | 4 | 1 | Coisson, star product |
| yangians.tex | 290 | 3 | 1 | 1 | RTT, E_1 Yangian, Coulomb branch |
| toroidal_elliptic.tex | 271 | 1 | 2 | 2 | Double affine, elliptic R-matrix |
| genus_expansions.tex | 226 | — | — | — | Multi-genus computations |
| detailed_computations.tex | 494 | — | — | — | sl_3 bar, W_3, Yangian |
| examples_summary.tex | 60 | — | — | — | Catalogue summary |
| minimal_model_examples.tex | 43 | — | — | — | W_3(3,4), W_3(5,6) |

Stubs: heisenberg_higher_genus, obstruction_classes, kac_moody_computations, w_algebras_computations, deformation_quantization_complete

### Part 3: Connections (chapters/connections/)
| File | Lines | PH | PE | C | Notes |
|------|------:|---:|---:|--:|-------|
| feynman_diagrams.tex | 1128 | 3 | 2 | 1 | Feynman diagram interpretation |
| holomorphic_topological.tex | 1114 | 0 | 7 | 10 | HT theories, AGT, 4d/2d |
| bv_brst.tex | 719 | 2 | 6 | 6 | BV-BRST formalism |
| genus_complete.tex | 491 | 2 | 3 | 4 | Complete genus theory, EO recursion |
| feynman_connection.tex | 455 | 0 | 1 | 0 | Feynman-bar-cobar bridge |
| poincare_computations.tex | 362 | 1 | 0 | 0 | NAP explicit computations |
| physical_origins.tex | 167 | 0 | 3 | 3 | NC Chern-Simons, D-branes |
| concordance.tex | 112 | 2 | 0 | 0 | Literature comparison (BD, FG, GLZ, LV) |

### Appendices (appendices/) — 14 files, ~6.6K lines
arnold_relations, signs_and_shifts, sign_conventions, existence_criteria, koszul_reference, spectral_sequences, spectral_higher_genus, homotopy_transfer, nilpotent_completion, notation_index, dual_methodology, computational_tables, theta_functions, general_relations

### Bibliography
bibliography/references.tex — 944 lines, all citations resolved

### Planning (notes/)
EXECUTION_PLAN.md, CONJECTURE_REGISTRY.md, SESSION_LAUNCHER.md, ENDGAME_PROMPT.md, ENDGAME_PROMPT_v2.md
