# Adversarial-Epistemic Audit — v41 (March 13, 2026)
# Cross-repository audit of ~/chiral-bar-cobar (Vol I) and ~/ainfinity-chiral-hochschild-cohomology-3d-qft (Vol II)
# Produced by: deep read-only adversarial audit, read all theorem proofs, traced logical dependencies
# Status: COMPLETE — all four phases executed

---

## EXECUTIVE SUMMARY

This two-volume programme (Vol I: 1742pp monograph, Vol II: 111pp paper) is architecturally
sound at the frontier of mathematical physics. The four main theorems (A-D) of Vol I **earn
their ProvedHere labels** — no overclaiming detected at the theorem level. The MC hierarchy
boundary between proved and conjectural is **correctly drawn and consistently maintained**.
Vol II is genuinely a first pass: ~15 major claims need verification, compute infrastructure
is ~30% functional, and several internal inconsistencies exist. The single largest systemic
risk is the **absence of chain-level computational cross-checks** for bar cohomology dimensions.

---

## PHASE 0: GROUND TRUTH

### Vol I Census (authoritative — scripts/generate_metadata.py methodology)

| Status | Raw grep | Narrative inflation | Genuine count | State file (stale) | Delta |
|--------|----------|-------------------|---------------|-------------------|-------|
| ProvedHere | 1046 | ~19 | ~1027 | 957 | +70 |
| ProvedElsewhere | 352 | ~29 | ~323 | 323 | 0 |
| Conjectured | 168 | ~32 | ~136 | 125 | +11 |
| Heuristic | 31 | ~3 | ~28 | 28 | 0 |
| Open | 0 | 0 | 0 | 0 | 0 |
| **Total** | **1597** | **~83** | **~1514** | **1433** | **+81** |

**Census methodology note**: The SESSION_PROMPT_v23.md grep command overcounts by ~83 due
to narrative mentions of \ClaimStatus in prose. Use `scripts/generate_metadata.py` for
authoritative counts. The autonomous_state.md is stale by +81 genuine claims.

### Vol I Git State

- 29 commits visible on main (parent traversal fails at commit 30: corrupt tree object 1074f0f4)
- Working tree CLEAN — no staged or unstaged changes
- 19 commits ahead of origin/main
- Git object corruption blocks `git status`, `git log` past 29 commits

### Vol II Git State

- Single commit cfff744 ("first pass", Nov 2025)
- main.tex modified (unstaged): 5757 lines removed, 50 added (chapter \input restructure)
- All chapters/, appendices/, compute/ directories UNTRACKED
- No \ClaimStatus macros in tex source; status tracked via concordance table

### Vol II Census

~30 entries in concordance table: ~10 ProvedHere, ~5 ProvedElsewhere, ~15 Needs Verification,
~4 Conjectured, ~2 Heuristic, ~4 Open.

---

## PHASE 1: VOLUME I — THEOREM ARCHITECTURE AUDIT

### 1A. Four Main Theorems

#### Theorem A (Bar-cobar adjunction)
- **Location**: chiral_koszul_pairs.tex:936-1003
- **Verdict**: **SOLID**
- **Architecture**: Assembly of A_0 (twisting morphisms), A_1 (bar concentration), A_2 (Verdier)
- **Strongest link**: thm:fundamental-twisting-morphisms — genuine four-way equivalence with
  filtration-based proof following LV12 Thm 2.3.1
- **Weakest link**: Family statement over moduli cites proper base change
  (lem:pushforward-preserves-qi at bar_cobar_construction.tex:11365) tersely
- **Dependencies**: [LV12] (verified in bibliography), [BD04] (verified), FM compactification
  properties cited through configuration space construction
- **Assessment**: Earns ProvedHere. No overclaiming.

#### Theorem B (Higher-genus inversion)
- **Location**: higher_genus.tex:8198-8261
- **Verdict**: **SOLID** (one soft spot)
- **Architecture**: Genus induction with three lemmas
- **Strongest link**: Localization triangle argument (lem:extension-across-boundary-qi) is textbook
- **Weakest link**: lem:higher-genus-open-stratum-qi (line 8141) — 10-line proof asserting
  "fiberwise QI implies QI on U_g" without spelling out constructibility/proper-base-change.
  ALSO: E_2 collapse stated in theorem but proved in rem:e2-collapse-mechanism (line 8263),
  not in proof body
- **Kunneth step**: Correct. "Tensor products of QIs are QIs by algebraic Kunneth over a field"
  — no Tor corrections needed. Sound.
- **Dependencies**: thm:bar-nilpotency-complete (bar_cobar_construction.tex:567),
  thm:chiral-koszul-duality (chiral_koszul_pairs.tex:1534), prop:gluing-at-nodes (7491),
  lem:boundary-compatible (7519). All exist with ProvedHere.
- **Assessment**: Earns ProvedHere. Soft spot is compression, not omission.

#### Theorem C (Quantum complementarity)
- **Location**: higher_genus.tex:5035-6231 (~1000-line proof, 10 steps in 3 parts)
- **Verdict**: **SOLID** (two soft spots)
- **Architecture**: Part I (SS construction, Steps 1-4), Part II (Verdier duality, Steps 5-6),
  Part III (decomposition, Steps 7-10)
- **Strongest link**: Anti-commutativity in Step 7 (thm:kodaira-spencer-chiral-complete, line 5753).
  Clean algebraic computation using Lie derivative contravariance + Verdier intertwining +
  Koszul involutivity. Steps 9-10 (eigenspace decomposition of involution) are airtight.
- **Weakest link #1**: Step 4.3 (lem:fiber-cohomology-center, line 5419) — center constancy
  over moduli. Argument: "OPE data are local on the curve and do not depend on global
  complex structure." Physically intuitive but should cite a rigidity theorem for vertex
  algebra centers, or note D_X-module flatness.
- **Weakest link #2**: Step 8 (lem:eigenspace-decomposition-complete, line 6028) — sign
  argument at lines 6067-6070 connecting "q=0 row" to "eigenvalue +1 under sigma" is
  compressed. Correct but conflates Poincare duality sign with Verdier involution eigenvalue.
- **Dependencies**: [BD04, Thm 4.6.1] Gauss-Manin (verified), thm:bar-concentration,
  thm:geometric-equals-operadic-bar, thm:e1-module-koszul-duality (all in text with ProvedHere),
  lem:involution-splitting (line 4795, proved same file).
- **Assessment**: Earns ProvedHere. Most original and elaborate proof in the monograph.

#### Theorem D_scal (Scalar modular characteristic)
- **Location**: higher_genus.tex:10601-10658
- **Verdict**: **SOLID** (one soft spot)
- **Architecture**: Pure assembly of four sub-results
- **Strongest link**: Additivity (cor:kappa-additivity, line 4262) — clean standard property.
  A-hat generating function — PROVED via Faber-Pandharipande, not pattern-matched.
- **Weakest link**: thm:genus-universality (line 4080) — passage from Heisenberg to general
  single-generator algebras via "propagator structure is universal." The mechanism
  (genus-g obstruction = kappa * lambda_g because lambda_g is the only topological invariant
  of the B-cycle integration, and kappa is the only algebra-specific scalar) is correct but
  stated as assertion rather than demonstrated step-by-step.
- **Dependencies**: thm:heisenberg-obs (3560), thm:mumford-formula (3392),
  Faber-Pandharipande formula (classical), [BD04].
- **Assessment**: Earns ProvedHere. The A-hat GF is independently verifiable.

### 1B. Master Conjecture Hierarchy

#### MC1 (PBW concentration) — SOUND

Three family proofs:
- **KM** (thm:pbw-allgenera-km, higher_genus.tex:9676): 3-step proof. Step 1: E_1 factorization
  via H^{1,0}(Sigma_g). Step 2: Whitehead acyclicity on non-trivial modules. Step 3: Killing
  contraction killed by d_2 at level k. Minor: "same argument applies at each weight h"
  (line 9840) for higher Casimirs is brief but correct (L_0 = h*id at weight h).
- **Vir** (thm:pbw-allgenera-virasoro, higher_genus.tex:9921): Clean scalar h*id argument
  on single weight-2 generator. Invertible for h >= 2. No issues.
- **W_N** (thm:pbw-allgenera-principal-w, higher_genus.tex:9214): Triangularity argument with
  unique weight-2 generator T on diagonal. Upper triangular matrix with invertible diagonal.
  Correct: every simple g has exponent 1 with multiplicity 1 (standard Lie theory).

#### MC2 (cyclic L-infinity + Theta_A) — SOUND (one caveat)

- **MC2-1 (graph complex)**: thm:cyclic-linf-graph, deformation_theory.tex:1669. Homotopy Jacobi
  via Stokes on FM compactifications + Fay trisecant. CAVEAT: sign verification is structural
  (appeals to Kontsevich graph complex conventions), not explicit computation. Given the
  monograph's own 2048-sign precedent for d_bracket^2 != 0, this is a potential attack surface.
- **MC2-2 (modular-operadic)**: prop:geometric-modular-operadic-mc, higher_genus.tex:11767.
  Formal algebra on complete filtered objects. Sound.
- **MC2-3 (tautological line)**: thm:tautological-line-support, higher_genus.tex:15982.
  Period-matrix identification omega_g -> lambda_g is correct (Hodge bundle theory).
  Independent verification via Pixton's relations is a genuine consistency check.
- **Assembly**: thm:mc2-full-resolution (line 14423). Mechanical — cites three resolved
  hypotheses, applies conditional completion. Clean.
- **Scalar saturation**: cor:scalar-saturation (line 14519). Depends on dim H^2_cyc = 1.
  Proved on standard landscape (cor:effective-quadruple). Conjectured universally
  (conj:scalar-saturation-universality). Text is explicit about this boundary.

#### MC3 (factorization DK/KL) — CORRECTLY MARKED

- "Evaluation-generated core" IS precisely defined: thm:eval-core-identification (yangians.tex:5833).
  In type A: D^b(Rep_fd(Y_hbar(sl_N))) exactly.
- Molev PBW dependency disclosed throughout: rem:dk23-unconditional-scope (yangians.tex:6867),
  concordance status table (line 3024).
- Two independent proofs for DK-2/3: (a) thick generation type-A, (b) sectorwise convergence
  all types.
- Gap to full O: explicitly characterized by four extension conjectures (yangians.tex:5894-5958).
- No overclaiming detected.

#### MC4 (W-infinity/Yangian towers) — CORRECTLY MARKED

- thm:rtt-mittag-leffler (yangians.tex:7742): ML argument complete. 4 steps: PBW filtration,
  E_1 degeneration (Koszulness forces diagonal), projection surjectivity, filtered => actual.
  Each step is elementary given the inputs.
- cor:completed-bar-cobar-yangian (line 7840): Standard "inverse limit of QIs under ML".
- Algebraic identification: conj:dk4-inverse-limit (line 7898). Correctly marked conjectural.

#### MC5 (BV/BRST = bar) — CORRECTLY MARKED

- thm:algebraic-string-dictionary (free_fields.tex:3756): Assembly of four separately proved
  results. Genus 0 is genuine. Higher genus honestly conjectural.

### 1C. DK Ladder

| Rung | Claimed | Audit | External Inputs | Conditional On |
|------|---------|-------|-----------------|---------------|
| DK-0 | Proved | SOUND | Molev PBW, PP05, Lurie DAG X | — |
| DK-1 | Proved | SOUND | Drinfeld polynomial classification | DK-0 |
| DK-1.5 | Proved | SOUND | — (independent lattice bypass) | — |
| DK-2/3 | Proved (eval-gen core) | SOUND | Molev PBW (disclosed) | DK-0, DK-1 |
| DK-4 analytic | Proved | SOUND | — | DK-2/3 |
| DK-4 algebraic | Conjectural | CORRECTLY MARKED | — | — |
| DK-5 | Conjectural | CORRECTLY MARKED | — | DK-4 |

Minor: In thm:h-level-factorization-kd Part (i), cosheaf descent ("QI on every basis open =>
global QI") is stated without proof. Correct by standard sheaf theory.

### 1D. Compute Verification Layer

**Test suite stratification** (~5,858 tests):

| Tier | Est. Count | Quality | Examples |
|------|-----------|---------|---------|
| Structural identities (d^2=0, Jacobi) | 800-1000 | Excellent | mc2_cyclic_ce:54-98, bar_cohomology_verification:34-55 |
| Published numerical values | 500-700 | Strong | Partition numbers (OEIS A000041), Riordan (A005043), Sugawara |
| Cross-checks | 200-300 | Good | CE vs Riordan agreement at degree 1 |
| Regression tests | 300-500 | Weak | W_3 H^4=52 "UNKNOWN -- no documented derivation" |
| Smoke/API | 1000-1500 | None | Only tests code runs |

**CRITICAL GAPS**:
1. No test connects bar_cohomology_dim() output to KNOWN_BAR_DIMS (chain-level cross-check missing)
2. sl_3 bar dims (8, 36, 204) are hardcoded lookups with no active computational derivation
3. W_3 H^4=52 explicitly flagged in test_conjectural.py as undocumented
4. Koszul dual Hilbert series uses numpy SVD (floating-point rank detection, fine for d=3, risky for d=8+)

**Highest-value missing test**: CE cohomology of sl_3 loop algebra at weight 1 = 8 (extends
validated sl_2 infrastructure to sl_3; independently verifies first entry in sl_3 bar table).

### 1E. The 19-Commit Arc

| Category | Count | Description |
|----------|-------|-------------|
| Substantive (new theorems, frontier) | 7 | DK-5 spectral sharpening, stage-5 packets, KL compression |
| Structural (notation, labels) | 4 | Bookmark-safe headings, notation normalization |
| Computational (tests, perf) | 5 | Rank-10 smoke coverage, DS caching, lattice budgets |
| Doctrinal (control sync) | 3 | Concordance/intro sync, state recording |

Arc: focused sprint on DK-5/MC4 Yangian frontier. No claim status upgrades in this batch.

---

## PHASE 2: VOLUME II — FIRST-PASS ASSESSMENT

### 2A. Structural Audit

**Restructuring status**: INCOMPLETE.
- main.tex gutted (5757 lines -> \input calls) but:
  - Broken cross-references: \eqref{eq:sesqui_1}, \eqref{eq:sesqui_i} — labels don't exist
  - Two empty appendix stubs (brace-signs.tex, orientations.tex)
  - SC operad defined in two places with different labels
  - PVA descent proved three times with slightly different notation
  - Worked examples spread across three overlapping files
- **CRITICAL**: Contradictory free multiplet cohomology: examples-computing.tex:140 says H^0=C;
  examples-complete.tex:95 says H^0=C[F_n]. Cannot both be correct.

### 2B. Standing Hypotheses (H1)-(H4)

- (H1)-(H3): Clearly stated (BV data, propagator regularity, FM logarithmic forms)
- **(H4)**: Vaguely stated. "Tameness hypotheses" for rectification never defined.
  Never checked for ANY example.
- Three example verifications (free, LG, CS): NON-CIRCULAR for (H1)-(H3) but (H4) unchecked.
- LG cubic: ALL compute operations are stubs (pass). Truncation claim m_4=0 is heuristic.

### 2C. Cross-Volume Bridges

| Bridge | Precision | Evidence | Verdict |
|--------|-----------|----------|---------|
| Bar-cobar (SC -> Thm A) | Imprecise — analogy, not conjecture | Structural parallel | Not a mathematical statement |
| Hochschild (§13 -> Thm H) | Moderate — dimensional descent sketch | Reduction principle | Needs formalization |
| Yang-Baxter (r(z) -> DK-0) | Moderate — Laplace formula given | Formula match | Stokes+AOS verification needed |
| W-algebras (Feynman -> bar d) | Imprecise — expectation | Genus-0 dictionary (Vol I) | Higher-order comparison needed |
| Physics-algebra ((H1-4) -> Vol I) | Programme-level | — | General proof of (H1-4) needed |

**None stated as formal conjectures.** All are research signals.

### 2D. Test Infrastructure

Vol II: 38 tests, all passing. ~30% genuine (Koszul signs, arity-4 A_inf consistency,
Laurent arithmetic, OPE coefficients). ~70% scaffolding/degenerate (free multiplet =
trivial, abelian CS = degenerate, Virasoro Jacobi = hardcoded return S.Zero).
ALL LG cubic operations are stubs.

---

## PHASE 3: CROSS-VOLUME COHERENCE

### 3A. Convention Consistency

| Convention | Vol I Location | Vol II Location | Verdict |
|-----------|---------------|-----------------|---------|
| Grading |d|=+1 | introduction.tex:1112 | axioms.tex:6, CLAUDE.md:62 | CONSISTENT |
| Bar desuspension | algebraic_foundations.tex:435 | CLAUDE.md:63 | CONSISTENT |
| A-inf signs | LV (-1)^{rs+t} | Koszul (-1)^{(j-1)(|a_1|+...)} | CONSISTENT (equiv.) |
| Com^!=Lie | algebraic_foundations.tex:535 | CLAUDE.md:97 | CONSISTENT |
| Sugawara/FF | kac_moody_framework.tex:163 | CLAUDE.md:100-101 | CONSISTENT |
| FM compactification | configuration_spaces.tex:2787 | fm-calculus.tex:10 | CONSISTENT |
| Curved A-inf sign | fourier_seed.tex:504 | CLAUDE.md:110 | CONSISTENT |
| Spectral parameters | Not used (geometric) | axioms.tex:19 (lambda_i) | Not comparable |

**Vol II internal**: Sesquilinearity inconsistency within axioms.tex (axiom line 35 vs proof
lemma line 219 give different formulas). Flagged in Vol II's own concordance.

### 3B. Strongest/Weakest/Missing

- **Strongest achievement**: Theorem C (quantum complementarity) — 10-step proof, most original
- **Most vulnerable**: MC2 graph complex sign verification (structural not explicit)
- **Conspicuously missing**: Chain-level computational cross-check for bar cohomology
- **Largest aspiration gap**: Vol II (first pass → journal quality)

---

## PHASE 4: PLATONIC AUDIT

### Gap Map

| Component | Rating | Note |
|-----------|--------|------|
| Theorem A | ★★★★☆ | Complete; one terse family step |
| Theorem B | ★★★★☆ | Complete; E_2 collapse in remark not proof |
| Theorem C | ★★★★☆ | Complete; center-constancy compressed |
| Theorem D_scal | ★★★★☆ | Complete; universality generalization by analogy |
| MC1 | ★★★★☆ | Sound for all three families |
| MC2 | ★★★★☆ | Sound; sign verification structural |
| MC3 (eval core) | ★★★★☆ | Two independent proofs |
| MC3 (full O) | ★★☆☆☆ | Four conjectures, no proof strategy |
| MC4 (ML) | ★★★★☆ | Complete |
| MC4 (algebraic id) | ★☆☆☆☆ | Programme-level |
| MC5 (genus 0) | ★★★★☆ | Assembly of proved results |
| MC5 (higher genus) | ★☆☆☆☆ | Downstream, no independent content |
| DK ladder (0-2/3) | ★★★★☆ | Sound |
| DK ladder (4-5) | ★★☆☆☆ | Analytic done; algebraic open |
| Examples (KM,Vir,W) | ★★★★☆ | Proved with computational support |
| Examples (Yangian) | ★★★☆☆ | DK core proved; infinite-rank conjectural |
| Compute tests | ★★★☆☆ | Strong structural; missing chain-level |
| Vol II (paper) | ★★☆☆☆ | Genuine ideas; proofs incomplete |
| Cross-volume bridges | ★☆☆☆☆ | Research signals, not conjectures |

### Recommendations (prioritized)

**Critical (status-relevant):**
1. Fix census protocol (use generate_metadata.py, update autonomous_state.md)
2. Repair git (corrupt tree object 1074f0f4)
3. Add chain-level bar cohomology test (bar_cohomology_dim vs KNOWN_BAR_DIMS for sl_2)

**Important (proof-strengthening):**
4. Expand Theorem B lem:higher-genus-open-stratum-qi (constructibility + proper base change)
5. Move E_2 collapse into Theorem B proof body
6. Strengthen Theorem C center constancy (D_X-module rigidity citation)
7. Make MC2 graph complex sign check explicit (low-arity computational verification)

**Strategic (highest leverage):**
8. Compute sl_3 bar H^1=8 from chain-level CE (extend LoopAlgebraCE to sl_3)
9. Formalize five cross-volume bridges as labeled conjectures
10. Implement LG cubic operations + test m_4=0 computationally

**Aspirational (programme-transforming):**
11. Prove dim H^2_cyc = 1 universally
12. Construct RTT-adapted dg model of g_A (closes DK-4)
13. Prove thick generation of D^b(O) by evaluation modules (closes MC3)
