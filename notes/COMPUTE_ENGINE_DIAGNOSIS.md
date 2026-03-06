# Compute Engine: Adversarial Audit Diagnosis

**Phase 1 Complete** — Mar 6, 2026

---

## 1A. Dead and Broken Code

### Dead Files (9 files, ~5,700 lines, 38% of lib/ codebase)

| File | Lines | Status | Reason |
|------|------:|--------|--------|
| `bar_differential.py` | 665 | BROKEN | d²≠0, produces H²=1 instead of 6 for sl₂ |
| `bar_differential_v2.py` | 511 | BROKEN | d²≠0, Arnold decomposition doesn't fix it |
| `chiral_bar_differential.py` | 1,603 | DEAD | Largest file, never tested, imports dead deps |
| `chiral_ce.py` | 377 | DEAD | No consumers anywhere |
| `w3_bar_cohomology.py` | 571 | SUPERSEDED | w3_bar.py covers same ground |
| `w3_bar_extended.py` | 824 | DEAD | PBW enumeration approach abandoned |
| `yangian_bar_compute.py` | 260 | DEAD | Wrong algebraic structure (RTT ≠ E₁-chiral) |
| `verified_formulas.py` | 74 | ORPHANED | Zero imports anywhere in codebase |
| `os_algebra.py` | 528 | STRANDED | Only consumer is dead chiral_bar_differential.py |

**Root cause for 5 of 9**: The "wrong tree" — attempting direct matrix computation of chiral bar differential when bracket-only d² ≠ 0 is a mathematical impossibility (Pole Decomposition Theorem). All numpy-based bar differential modules share this fundamental flaw.

### Partially Broken (1 file)
- `chiral_bar.py` (920 lines): CE complex works (d²=0 verified), associative bar component has d²≠0 (expected, documents curvature). Used by `htt.py`.

### Summary
- **Live code**: 29 files, ~9,100 lines (62%)
- **Dead code**: 9 files, ~5,700 lines (38%)
- **Recommendation**: Archive dead files to `compute/lib/_archive/`, keep os_algebra.py and koszul_hilbert.py accessible (correct theory, wrong wiring)

---

## 1B. Mathematical Audit: What the Engine Can vs Cannot Compute

### COMPUTES (derives results from algorithms)

| Capability | Module(s) | Method |
|-----------|-----------|--------|
| Genus expansion F_g(A) for all 11 algebras | genus_expansion.py, genus_bridge.py | κ·λ_g^FP (exact sympy Rationals) |
| Bar chain group dimensions | heisenberg_bar, virasoro_bar, etc. | OPE product enumeration |
| Koszul dual Hilbert series (classical) | koszul_hilbert.py | Quadratic dual iteration |
| Bar cohomology dims (Heis, sl₂, Vir, βγ, bc) | bar_complex.py | Closed-form recurrences |
| CE cohomology (sl₂) | chiral_bar.py, htt.py | Exact matrix rank (sympy) |
| Homotopy transfer (sl₂ formality) | htt.py | SDR construction + tree formula |
| Associahedron f-vectors | spectral_sequence.py | Narayana numbers |
| FM compactification Poincaré polynomials | fm_compactification.py | Combinatorial formula |
| GF interpolation (W₃ prediction) | bar_gf_solver.py | Rational GF fitting from 4 points |
| Complementarity κ(A)+κ(A!) | curvature_genus_bridge.py | Direct formula evaluation |
| Eisenstein series q-expansions | toroidal_bar.py | Bernoulli number formula |

### STORES (lookup tables, no derivation)

| Data | Module(s) | Source |
|------|-----------|--------|
| Bar cohomology: W₃ (deg 1-4), sl₃ (deg 1-3), Yangian | bar_complex.py KNOWN_BAR_DIMS | Manuscript/prior computation |
| Spectral sequence collapse pages | spectral_sequence.py | Hardcoded dict |
| E₂ page dimensions | spectral_sequence.py | Hardcoded dict |
| Algebra registry (11 algebras, metadata) | cross_algebra.py | String formulas |
| Koszul pair catalog | koszul_pairs.py | Hardcoded pairs |
| Cartan data (10 Lie algebras) | lie_algebra.py | Hardcoded matrices |

### CANNOT COMPUTE (fundamental blockers)

| Gap | Blocker | Impact |
|-----|---------|--------|
| **Chiral bar differential** | d²≠0 for bracket-only (math impossibility) | Cannot compute bar cohomology from first principles for interacting algebras |
| **Bar cohomology sl₃ deg ≥4** | Chain group dim 24,576 at deg 4; needs sparse modular LA | Programme IX frontier |
| **Bar cohomology W₃ deg ≥5** | Composite fields break PBW enumeration | H⁵=171 is interpolation, not computation |
| **PBW spectral sequence** | spectral_sequence.py is 100% lookup — no actual E_r computation | Cannot verify E₂ collapse computationally |
| **Chiral Koszul dual Hilbert series** | koszul_hilbert.py does classical only; chiral needs full OS algebra | Gap between classical BGS and chiral Koszulness |

### Verdict
The engine is a **verification and regression framework** (~75% of 924 tests check hardcoded constants against manuscript). It excels at genus expansions, complementarity checking, and cross-algebra consistency. It cannot independently discover bar cohomology for interacting algebras.

---

## 1C. Engineering Audit

### Top 5 Engineering Problems

**E1. No public API** — `__init__.py` is empty. Every import is `from compute.lib.specific_module import specific_function`. No discoverability, no stable interface.

**E2. 38% dead code** — 5,700 lines of broken/dead code in lib/. Creates confusion about which approach is current. The dead files are the largest files (chiral_bar_differential.py at 1,603 lines).

**E3. numpy/sympy split** — 10 files use numpy (floating point), 27 use sympy (exact). All numpy files are dead/broken. The live engine is 100% sympy. Mixed arithmetic is a false promise.

**E4. Near-zero coupling** — Only 3 internal import relationships. Each algebra module is a standalone island. No shared OPE engine, no shared bar complex construction, no shared differential builder. Code duplication across ~15 algebra-specific bar modules.

**E5. Test suite is 65% regression, 8% identity, 1% computation** — 588/901 tests check hardcoded values. Only 11 tests perform actual matrix computation. Only 72 tests verify mathematical identities (d²=0, Jacobi, etc.). The suite catches regressions but doesn't validate mathematics.

### Top 3 Mathematical Bottlenecks

**M1. No working chiral bar differential** — The engine's raison d'être is bar complex computation, but the core object (the differential d: B^n → B^{n-1}) cannot be built. The PBW spectral sequence approach is documented but not implemented computationally.

**M2. PBW spectral sequence is a stub** — spectral_sequence.py contains zero spectral sequence computation. It stores known E₂ dimensions as lookup tables. An actual implementation would: (a) build gr_PBW(B(A)), (b) compute E₁ = CE(g, Sym(g[t⁻¹])), (c) compute d₁ differentials, (d) take cohomology to get E₂.

**M3. Classical-to-chiral Koszul gap** — koszul_hilbert.py computes classical quadratic dual Hilbert series correctly. But chiral Koszulness requires the full chiral OPE structure (all poles, Borcherds identity), not just the classical quadratic data. The bridge from thm:pbw-koszulness-criterion to actual computation is unbuilt.

---

## Phase 1 Exit Criteria — Satisfied

| Criterion | Answer |
|-----------|--------|
| **(a)** Dead/broken lib files | **9 of 39** (38% of lines) |
| **(b)** Compute vs store | **11 genuine compute capabilities** vs **6 pure storage modules** vs **5 impossible gaps** |
| **(c)** Top 5 engineering problems | E1-E5 above |
| **(d)** Top 3 mathematical bottlenecks | M1-M3 above |
