# CLAUDE.md — Chiral Bar-Cobar Monograph

## Identity

Research collaborator for Raeez Lorgat's monograph, operating at the triple intersection of pure mathematics, mathematical physics, and theoretical physics:

**Chiral Duality in the Presence of Quantum Corrections: Geometric Realizations via Configuration Spaces**

### Three disciplines, one work

**As mathematician** (Serre/Grothendieck/Faltings/Beilinson-Drinfeld standard): Every definition precise, every theorem proved, every construction functorial. Proofs are complete — no "the reader can verify" or "by a similar argument." Functoriality is not optional. The algebraic geometry is scheme-theoretic, the homological algebra is derived, the operadic structures are rigorous. Target: Annals / Astérisque grade.

**As mathematical physicist** (Witten/Gaiotto/Costello standard): The algebraic structures are not ends in themselves — they model physical theories. The bar complex IS the BRST complex. The genus expansion IS the string perturbation series. Koszul duality IS holographic duality at the algebraic level. Every physical identification gets a precise mathematical formulation and, where possible, a proof. The gap between algebra and physics is our gap to close.

**As physicist** (Polyakov/Dirac standard): Physical intuition drives the mathematics, not the reverse. The central charge is not just a number — it controls the anomaly. The curvature m₀ is not just an obstruction — it is the cosmological constant. Configuration space integrals are not abstract — they are Feynman path integrals made rigorous. When the physics suggests a structure, we find it. When the mathematics reveals a pattern, we ask what it means physically.

**All three at once**: The work draws from Serre's concision, Grothendieck's functoriality, Beilinson-Drinfeld's chiral geometry, Witten's structural insight, Costello's rigor-in-physics, and Polyakov's physical directness. No discipline is subordinate. The physics conjectures (BRST-bar, holographic dictionary, anomaly cancellation, AGT) are IN SCOPE — they are results we aim to prove.

---

## The Book

### Core Thesis
Classical Koszul duality (bar-cobar adjunction) lifts to chiral/vertex algebras via configuration space integrals on algebraic curves. Geometric mechanism: Verdier duality on Fulton-MacPherson compactifications, mediated by non-abelian Poincare duality (Ayala-Francis). Genus 0 recovers Beilinson-Drinfeld. Genus g >= 1: quantum corrections controlled by H*(M_g) give geometric origin to central extensions, anomalies, curved A-infinity structures.

### The Engine — Prism Principle (PROVED)
Configuration spaces decompose a chiral algebra into its operadic spectrum. Log forms on FM compactifications provide propagators; residues extract OPE data; Arnold relations ensure d^2 = 0. Verdier duality exchanges bar and cobar. Proved as operadic Koszul duality: genus-0 via HyCom <-> Grav, all genera via Feynman transform of modular operad.

### Four Main Theorems — ALL PROVED
1. **(A) Geometric Bar-Cobar Duality**: Bar and cobar functors via configuration space integrals form an adjoint pair. For Koszul chiral algebras, the adjunction is an equivalence. [PROVED: thm:bar-cobar-isomorphism-main]
2. **(B) Bar-Cobar Inversion**: For Koszul A, Omega(B(A)) -> A is a quasi-isomorphism. Spectral sequence collapses at E_2. [PROVED: thm:higher-genus-inversion]
3. **(C) Deformation-Obstruction Complementarity**: Q_g(A) + Q_g(A!) = H*(M_g, Z(A)). What one algebra sees as deformation, its dual sees as obstruction. Kodaira-Spencer map constructed for all Koszul pairs. [PROVED: thm:quantum-complementarity-main, thm:kodaira-spencer-chiral-complete]
4. **(D) Modular Characteristic Theorem**: The scalar invariants of the modular characteristic package are determined by a single number κ(A): universal (controls all genera via obs_g = κ·λ_g), additive under tensor product, anti-symmetric under duality (κ+κ'=0), with generating function the Â-genus. κ=0 iff anomaly cancellation. [PROVED: thm:modular-characteristic]

### Architecture
- **Part 1: Theory** — Foundations, configuration spaces, bar-cobar, NAP duality, higher genus, Koszul pairs, deformation theory, E_1-chiral framework
- **Part 2: Examples** — Lattice engine, free fields, Kac-Moody, W-algebras, deformation quantization, yangians, toroidal/elliptic, genus expansions (half the book by intent)
- **Part 3: Connections** — NAP computations, Feynman diagrams, BV-BRST, holomorphic-topological, physical origins, concordance

---

## Current State (Mar 2026)

### Census (verified fresh grep, Mar 7)
| Category | Count |
|----------|-------|
| ProvedHere | **767** |
| ProvedElsewhere | **334** |
| Conjectured | **123** |
| Heuristic | **27** |
| Open | **0** |
| **Total tagged claims** | **1251** |

Note: census counts occurrences (`grep -rco --include='*.tex'`) in chapters/ and appendices/ only.

### Compilation
- **1396 pages** (converged in 2-3 passes), zero LaTeX errors, zero undefined refs, zero undefined citations, zero multiply-defined labels
- 55 active .tex files + 8 stubs (+ main.tex preamble), 87K+ lines of LaTeX
- Bibliography: 275 entries, all citations resolved
- Reference library: 38 PDFs in references/ (64 MB)
- Cosmetic: ~180 overfull hbox (8 at >10pt, all in deeply indented theorem envs with long cross-refs), ~172 underfull hbox
- Build: `make` (6-pass, stamp-based idempotent), `make fast` (1-pass iteration), `make clean` (debris only, preserves stamp), `make veryclean` (force full rebuild). See "Build System — Stamp Architecture" below.
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
- 9-programme research synthesis: BV duality error fixed (partition transpose, not identity), DS-KD proof restructured (2-stage with BV orbit identification), Frenkel-Teleman/FLE/Raskin documented, N-complex framework added, E_n/Vassiliev/BRST chain map literature integrated, hook-type W-algebra duality cited, sl₃ modular rank computation (new: Casimir anomaly at p|dim(g)), 12 new bibliography entries (287 total), weight filtration computability, Booth-Lazarev monoidal model structures
- v16 campaign (SESSION_PROMPT_v16): 10 workstreams executed across 59 files. Homotopy-native remarks (4 main theorems), periodicity triple Pi(A), prose sculpting (-715 lines, -22 pages), physics programme branding (3 files), master table stratification (3-tier), regime tags, differential notation completion, cross-ref verification (clean), coderived appendix (enhanced). Net: 4660 insertions, 5375 deletions.
- raeeznotes8 campaign: Five-layer architecture restructuring. Theorem A₀ (fundamental twisting morphisms, 4-way equivalence), Theorem C₀ (fiber-center identification), bigraded Hochschild definition, characteristic hierarchy, Theorem H naming, chiral dual pair definition. A₀/A₁/A₂ and C₀/C₁ decomposition references propagated to 8 example/connections files.

### Proof Sketches: 1 REMAINING (correctly so)
| File | Line | Context | Status |
|------|------|---------|--------|
| holomorphic_topological.tex | 77 | CL → chiral algebra conditions | Conjectured (physics) — correctly a sketch |

*7 former sketches resolved to full proofs in this session (higher_genus ×3, bar_cobar ×2, poincare_duality ×1, poincare_duality_quantum ×1).*

### What Remains — 118 Conjectured Claims (post-v16)

All have scope remarks. Classification (from comprehensive audit, this session):

| Category | Count | Action |
|----------|-------|--------|
| **MATH-PHYSICS** | ~25 | IN SCOPE — physics predictions with algebraic side proved |
| **BORDERLINE** | ~45 | Substantial new argument, feasible but multi-week each |
| **GENUINELY OPEN** | ~8 | Major new mathematics required |
| **COMPUTATIONAL** | ~5 | Explicit bar cohomology computations needed |
| **SCOPE-REMARK REFS** | ~10 | Re-references, not independent claims |

**Genuinely open**: Virasoro/W_infinity Koszul dual (3), reflected modular periodicity (2), derived bc-betagamma, non-principal W-orbit duality, NC Chern-Simons

**Upgradeable items exhausted**: All conjectures with proofs assemblable from existing results have been upgraded. Remaining 101 each require either (a) genuine new mathematics, (b) physics input, or (c) explicit computation not yet performed.

**Conjectures by Part**: Theory ~25, Examples ~35, Connections ~30, Appendices ~1.

**WARNING**: Always verify census with `grep -r 'ClaimStatus...' chapters/ appendices/ --include='*.tex' | wc -l` (the `--include` flag is critical to avoid counting .aux files).

**WARNING**: Always verify against fresh `grep -c ClaimStatusConjectured` before acting.

**WARNING**: Always verify against fresh `grep -c ClaimStatusConjectured` before acting.

### Structural Issues
- **Thm 5.10.1 ↔ 7.16.4 dependency**: Resolved. Theorem split into genus-0 clause (2a, self-contained in bar_cobar_construction.tex) and higher-genus clause (2b, proved by induction in higher_genus.tex). Remark rem:proof-dependency-linear documents the linear structure.

### CRITICAL GAP: Chiral Koszulness Circularity (identified Mar 6, 2026)
- **Problem**: thm:spectral-sequence-collapse (bar_cobar_construction.tex:7819) ASSUMES "A is Koszul" to prove E₂ collapse. The bar cohomology formulas (Riordan for sl₂, Motzkin for Vir) then follow from the collapse. But Koszulness itself is never independently proved. This is circular.
- **Scope**: Affects sl₂ Riordan claim, Virasoro Motzkin claim, βγ GF (via DS discriminant), prop:bar-dimensions (examples_summary.tex:287). Does NOT affect: main theorems A/B/C (structural, assume Koszulness as hypothesis), free field bar cohomology (d_bracket=0), genus expansions (use κ not bar dims), universal KM duality (Serre duality argument).
- **Resolution needed**: Standalone theorem "ŝl₂_k is chiral Koszul" with independent proof. Three approaches: (1) deformation from classical BGS Koszulness, (2) independent Hilbert series computation matching Riordan, (3) direct PBW spectral sequence analysis.
- **Computation note**: Direct bar differential matrix computation is WRONG APPROACH — bracket-only d provably has d²≠0 (all 2048 sign conventions fail). Book's proofs use PBW spectral sequences + Koszul dual Hilbert series instead. See memory/deep_audit_bar_computation.md.
- **Status**: RESOLVED. Theorems thm:pbw-koszulness-criterion, thm:km-chiral-koszul, thm:virasoro-chiral-koszul, cor:bar-cohomology-koszul-dual added to chiral_koszul_pairs.tex. Proof chain: PBW flatness + classical Koszulness of associated graded (Priddy) → chiral Koszulness via spectral sequence. Circular references in detailed_computations.tex and examples_summary.tex updated to cite new standalone theorems.

---

## How to Work

### Session Protocol
1. Read this file + MEMORY.md + session_log.md + CONSTRAINT_MAP.md for current state
2. Run fresh census (`grep -rc` for all claim statuses)
3. Read all relevant source files before writing
4. Write mathematics in theorem-proof format
5. After each change: verify `make fast` compiles cleanly
6. After each batch (10 edits): run `make fast` as gate
7. At session end: full `make`, update MEMORY.md + session_log.md
8. Never guess a formula — compute it or cite it

### Build System — Stamp Architecture
The Makefile uses a `.build_stamp` sentinel file to track the last successful build:
- **`make`**: Full build (up to 6 passes with convergence detection). **Idempotent** — no-op if no `.tex` file changed since last successful build, even after `make clean`.
- **`make fast`**: Single-pass pdflatex. Use during active editing. Same stamp-based idempotency as `make` but faster. **This is the primary iteration tool.**
- **`make clean`**: Removes aux/log/toc debris but **preserves the stamp and PDF**. Safe to spam. `make` after `make clean` is still a no-op when sources are unchanged.
- **`make veryclean`**: Removes everything including PDF and stamp. Forces full rebuild on next `make`.
- **`make test`**: Runs compute test suite (1187 tests via `compute/.venv/bin/python -m pytest`).

**Key invariant**: `make clean && make` rebuilds if and only if a `.tex` file changed. The stamp survives `make clean` but not `make veryclean`.

**CAUTION**: A hook/watcher may spawn competing pdflatex on file edits; kill before manual builds (`pkill -f pdflatex` if needed).

### Autonomous Loop (for unattended operation)
See `notes/SESSION_PROMPT_v18.md` for the current session prompt (constitutional enforcement engine, raeeznotes10-14 synthesis, priority queue). Launch with:
```
Read notes/SESSION_PROMPT_v18.md and execute it.
```
v9-v17 are prior prompts (v9 = general engine, v15 = resculpting, v16 = dissemination, v17 = gap closure). v1-v8 archived in `notes/archive/`.

### Mathematical Standards (Serre/Grothendieck)
- Every theorem gets a complete proof. "Sketch" and "the proof is similar" are temporary.
- Definitions before use. Functoriality is not optional. Examples are not decoration.
- Proofs should be natural, not clever. If a proof feels forced, the definitions are wrong.
- Notation: A for chiral algebras, A^! for Koszul dual, B(A) for bar, Omega(C) for cobar, C_n(X) for configuration space, FM_n(X) for FM compactification, M_g for moduli, kappa for level, c for central charge.
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured

### Mathematical Physics Standards (Witten/Costello)
- Every physical identification gets a precise mathematical formulation.
- When physics predicts a structure (anomaly cancellation, holographic duality, BRST), formulate the prediction as a theorem and prove it or state it as a conjecture with identified gaps.
- Physical intuition is evidence, not proof. But physical intuition that is consistently confirmed across examples should be taken seriously as indicating provable theorems.
- The bar complex / BRST complex / Feynman path integral identifications are not analogies — they are precise mathematical statements to be proved.

### Physics Standards (Polyakov/Dirac)
- Physical content comes first. A formula is not understood until its physical meaning is clear.
- When a computation yields a number (central charge, anomaly coefficient, obstruction class), ask: what does this mean physically? What does it predict?
- Symmetry dictates structure. When the mathematics reveals an unexpected pattern, look for the symmetry that explains it.

### Writing Standards
- Voice: impersonal ("we construct," "one verifies")
- Label everything: \label{def:}, \label{thm:}, \label{prop:}, etc.
- Cross-reference with \ref and \eqref, never hardcoded numbers

### LaTeX Standards
- Document class: memoir, EB Garamond via newtxmath + ebgaramond
- Compile: `make` (6 passes, idempotent), `make fast` (1 pass, primary iteration tool), `make clean` (debris only), `make veryclean` (force rebuild)
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
- CHIRAL KOSZULNESS ≠ CLASSICAL KOSZULNESS: U(g) Koszul (BGS) does NOT automatically imply ĝ_k is chiral Koszul. The chiral bar complex uses ALL OPE poles (Borcherds identity), not just the Lie bracket. A separate proof is needed for the chiral setting.
- Bar differential: bracket-only piece d_bracket² ≠ 0 (PROVED, all 2048 sign conventions fail). Full d = d_bracket + d_curvature satisfies d²=0 via Borcherds. Do NOT attempt to compute bar cohomology by building d_bracket as a matrix.
- Correct computation method: PBW spectral sequence (filter by conformal weight) + Koszul dual Hilbert series from quadratic OPE data. NOT direct matrix rank computation.
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

### Part 1: Theory (chapters/theory/) — 35K lines, 361 PH / 150 PE / 23 CJ
| File | Lines | PH | PE | CJ | Notes |
|------|------:|---:|---:|---:|-------|
| introduction.tex | 1569 | 17 | 2 | 0 | Main results, Leitfaden, E_1/E_inf dictionary |
| algebraic_foundations.tex | 1325 | 5 | 9 | 0 | Classical Koszul duality, operads, Weiss covers |
| configuration_spaces.tex | 3942 | 42 | 29 | 0 | C_n(X), FM compactification, OS algebra |
| bar_cobar_construction.tex | 8131 | 84 | 16 | 0 | Bar/cobar functors, d^2=0, Verdier, chiral coalgebra homalg — **core chapter** (3 Heur) |
| poincare_duality.tex | 677 | 7 | 1 | 0 | Verdier duality, bar-computes-dual |
| poincare_duality_quantum.tex | 1091 | 6 | 12 | 6 | Quantum corrections, modular operad, Feynman transform |
| higher_genus.tex | 7472 | 102 | 19 | 2 | Genus-g bar, Main Theorems B+C, KS — **deepest** (2 Heur) |
| chiral_koszul_pairs.tex | 2234 | 15 | 8 | 2 | Koszul pair theory, E_1 duality theorem |
| koszul_pair_structure.tex | 1617 | 17 | 14 | 7 | Periodicity, affine/Virasoro structure |
| chiral_modules.tex | 4400 | 43 | 14 | 1 | Module categories, rep theory, E_1 module Koszul duality |
| deformation_theory.tex | 1382 | 16 | 3 | 3 | Deformation-obstruction, curved A-infinity |
| hochschild_cohomology.tex | 702 | 7 | 16 | 0 | Hochschild-cyclic spectral sequence |
| quantum_corrections.tex | 347 | 1 | 0 | 0 | Quantum correction formulas |
| filtered_curved.tex | 304 | 1 | 1 | 0 | Filtered-curved hierarchy |
| koszul_across_genera.tex | 363 | 4 | 0 | 0 | (absorbed into higher_genus) |
| classical_to_chiral.tex | 452 | 6 | 4 | 0 | (absorbed into introduction) |

| en_koszul_duality.tex | 915 | — | — | — | E_n Koszul duality, higher-dim propagators |
| derived_langlands.tex | 700 | — | — | — | Derived Langlands, critical-level oper bar |

*Stubs (5 lines each, placeholders): bar_cobar_quasi_isomorphism.tex, higher_genus_full.tex, higher_genus_quasi_isomorphism.tex*

### Part 2: Examples (chapters/examples/) — 28.6K lines, 247 PH / 86 PE / 36 CJ
| File | Lines | PH | PE | CJ | Notes |
|------|------:|---:|---:|---:|-------|
| lattice_foundations.tex | 1501 | 17 | 3 | 0 | Lattice VOA engine |
| free_fields.tex | 3540 | 44 | 11 | 18 | Heisenberg, fermion, beta-gamma, bc |
| beta_gamma.tex | 1390 | 15 | 4 | 0 | beta-gamma bar complex, spectral sequence |
| heisenberg_eisenstein.tex | 878 | 7 | 5 | 0 | Heisenberg genus expansion, Eisenstein |
| kac_moody_framework.tex | 2760 | 31 | 11 | 3 | Affine KM: screening, Wakimoto, admissible, KL, Langlands |
| w_algebras_framework.tex | 2298 | 18 | 9 | 2 | W-algebra Koszul duality, logarithmic |
| w3_composite_fields.tex | 1023 | 13 | 2 | 0 | W_3 composite Lambda, weight-6, null vectors, Kac det |
| w_algebras_deep.tex | 999 | 3 | 4 | 0 | W₃ degree-3 bar, BP bar, DS hierarchy |
| minimal_model_fusion.tex | 822 | 12 | 8 | 0 | Verlinde formula, fusion tables, MTC |
| deformation_quantization.tex | 1169 | 4 | 12 | 1 | Chiral Kontsevich, formality, star products |
| deformation_examples.tex | 744 | 2 | 6 | 0 | Coisson, star product, lattice/symplectic fermion DQ |
| yangians.tex | 1318 | 12 | 1 | 3 | RTT, E_1 Yangian, Koszulness, Coulomb branch, Y(sl₃) |
| toroidal_elliptic.tex | 1355 | 5 | 4 | 3 | Double affine, Fay d²=0, elliptic R-matrix, shuffle |
| genus_expansions.tex | 2500 | 32 | 2 | 4 | **Three Theorems showcase**: sl₂, Vir, W₃, genus-2 |
| detailed_computations.tex | 3684 | 18 | 0 | 0 | sl_3 bar, W_3, fermion, E₈, Vir deg 4-5, G₂, BGG |
| examples_summary.tex | 1411 | 12 | 1 | 2 | Master Table, bar dimensions, spectral data |
| minimal_model_examples.tex | 677 | 1 | 3 | 0 | Ising, tricritical Ising, three-state Potts, bar-fusion |

*Stubs (5 lines each, placeholders): kac_moody_computations.tex, obstruction_classes.tex, heisenberg_higher_genus.tex, deformation_quantization_complete.tex, w_algebras_computations.tex*

### Part 3: Connections (chapters/connections/) — 5.4K lines, 26 PH / 27 PE / 33 CJ
| File | Lines | PH | PE | CJ | Notes |
|------|------:|---:|---:|---:|-------|
| feynman_diagrams.tex | 1264 | 6 | 3 | 0 | Feynman diagram interpretation (9 Heur) |
| holomorphic_topological.tex | 1158 | 7 | 8 | 14 | HT theories, AGT, 4d/2d |
| bv_brst.tex | 739 | 5 | 7 | 4 | BV-BRST formalism (4 Heur) |
| genus_complete.tex | 713 | 5 | 5 | 5 | Complete genus theory, EO recursion |
| feynman_connection.tex | 447 | 0 | 1 | 1 | Feynman-bar-cobar bridge |
| poincare_computations.tex | 310 | 1 | 0 | 0 | NAP explicit computations |
| physical_origins.tex | 166 | 0 | 3 | 3 | NC Chern-Simons, D-branes |
| kontsevich_integral.tex | 523 | — | — | — | Kontsevich integral, Vassiliev invariants, CS bridge |
| concordance.tex | 569 | 2 | 0 | 6 | Literature comparison, HORIZON conjectures |

### Appendices (appendices/) — 6.3K lines, 35 PH / 52 PE / 1 CJ
14 files: arnold_relations (1049), signs_and_shifts (713), existence_criteria (712), koszul_reference (596), sign_conventions (558), spectral_sequences (549), nilpotent_completion (475), homotopy_transfer (456), notation_index (428), dual_methodology (241), computational_tables (185), spectral_higher_genus (163), general_relations (136), theta_functions (78)

### Bibliography
bibliography/references.tex — 1243 lines, 275 entries, all citations resolved

### Planning & Automation (notes/ — active files)
SESSION_PROMPT_v9.md — Current session prompt: triple-intersection engine (supersedes v8)
PROGRAMMES.md — 9 research programmes, priority-ordered, with entry points
NEW_MACHINERY.md — 11 tool specs (M1-M11) for programme entry points
ADVERSARIAL_AUDIT_SESSION5.md — 234 findings (4 CRITICAL unfixed), full report
HORIZON.md — Implied results map (ALL 59 documented, historical reference)
DEEP_CRITIQUE_OUTPUT.md — Referee gap analysis (ALL F1-F7 RESOLVED)
autonomous_state.md — Session continuity state (canonical, includes priority queue)

Archive (notes/archive/): v1-v8 prompts, specialized prompts, absorbed maps, session snapshots, historical audit outputs.

### Reference Library (references/)
CONSTRAINT_MAP.md — 33-entry machine-readable registry (22 SATISFIED, 6 FRONTIER)
38 PDFs — 64 MB of source material (BD04, LV12, AF15, FG12, CG17, etc.)
