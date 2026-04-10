# Exhaustive Gap Analysis -- All Three Volumes
## 2026-04-08, Post-Session Diagnostic

**Scope**: Vol I (~2,522pp, 122 active .tex, 1,178 compute engines, 2,898 ProvedHere tags, 261 Conjectured tags, 228 conjecture environments), Vol II (~1,516pp, 102 active .tex, 3,120 test defs), Vol III (48 active .tex, 16,551 test defs). Total test definitions across all three volumes: **118,826**.

---

## SCALE 1: LOCAL (Line-Level)

### 1.1 RECTIFICATION-FLAG Comments Still Open

**Vol I** (12 flags, 4 OPEN):

| # | File | Status | Severity | Issue |
|---|------|--------|----------|-------|
| 1 | `subregular_hook_frontier.tex:1075` | **OPEN, CRITICAL** | CRITICAL | Unresolved flag about hook-type scope |
| 2 | `quantum_corrections.tex:373` | **OPEN** | SERIOUS | m_3 coefficient for beta-gamma unverified |
| 3 | `frontier_modular_holography_platonic.tex:4776` | **OPEN** | SERIOUS | BRST reduction shift claim unverified |
| 4 | `computational_methods.tex:1100` | **OPEN** | MODERATE | Individual coset pieces unverified |
| 5 | `computational_methods.tex:1526` | **OPEN** | MODERATE | Table conformal weight dims unverified |
| 6 | `chiral_koszul_pairs.tex:1028` | **OPEN** | MINOR | Notation A_2^! ambiguity |
| 7 | `en_koszul_duality.tex:1053` | **OPEN** | MODERATE | L_infty formality higher components |
| 8 | `cobar_construction.tex:2169` | **OPEN** | MODERATE | AP25/AP33 Verdier duality statement |
| 9 | `chiral_hochschild_koszul.tex:5452` | **OPEN** | SERIOUS | AP1 supertrace formula unverified |
| 10 | `chiral_hochschild_koszul.tex:5648` | **OPEN** | MODERATE | Kontsevich formality dependency |
| 11 | `arithmetic_shadows.tex:2990` | **OPEN, CRITICAL** | CRITICAL | AP74: Bernoulli-Dirichlet identity numerically FALSE |
| 12 | `w_algebras.tex:231` | Resolved | -- | Per-channel eigenvalues |

**Vol II** (4 flags):

| # | File | Status | Severity |
|---|------|--------|----------|
| 1 | `w-algebras-stable.tex:503` | **OPEN** | SERIOUS | Laplace kernel vs collision residue confusion |
| 2 | `introduction.tex:1516` | **OPEN** | SERIOUS | AP22 hbar^{2g-2} vs hbar^{2g} unverified |
| 3 | `ht_bulk_boundary_line_frontier.tex:2590` | **OPEN** | MODERATE | Theta_{M2} conjectural definition |
| 4 | `thqg_gravitational_yangian.tex:713` | **OPEN** | MINOR | "Therefore" logic unverified |

**Vol III** (6 flags):

| # | File | Status | Severity |
|---|------|--------|----------|
| 1 | `working_notes.tex:261` | **OPEN** | SERIOUS | AP40/AP-CY6/AP42 scope issues |
| 2 | `working_notes.tex:438` | **OPEN** | MODERATE | Class C betagamma kappa claim |
| 3 | `working_notes.tex:689` | **OPEN** | SERIOUS | AP48: kappa(V^natural) undetermined |
| 4 | `working_notes.tex:2690` | **OPEN** | SERIOUS | kappa_ch = 3 asserted without derivation |
| 5 | `physics_bv_brst_cy.tex:475` | **OPEN** | SERIOUS | kappa(G(X)) = chi^CY(X) unproved |
| 6 | `cy_to_chiral.tex:1306` | **OPEN** | MODERATE | K3 kappa_{CY2} formula unverified |

**Priority**: Items 1.1.1 (subregular hook) and 1.1.11 (Bernoulli-Dirichlet, AP74) in Vol I are CRITICAL and must be resolved before any submission.

### 1.2 Compute Test Failures

- **Vol I**: At least 1 known failure: `test_theorem_bethe_mc_engine.py::TestPath2YangYang::test_yang_yang_gradient_matches_mc_gradient` (asserts pi/2 < 1e-6, obviously wrong). This is a broken test expectation (AP10 pattern).
- **Vol II/III**: Test runs timed out or produced empty output during this session; full suite status unknown. Requires a clean `make test-full` run.

**Priority**: SERIOUS. A failing test in the staged files means the test was written with wrong expectations. Must audit test_theorem_bethe_mc_engine.py line 224.

### 1.3 K_BP = 76 vs 196 Inconsistency (CRITICAL)

The Bershadsky-Polyakov Koszul conductor appears in TWO CONFLICTING VALUES:
- `appendices/nonlinear_modular_shadows.tex:3882`: "Koszul conductor K = 76" (WRONG)
- `standalone/bp_self_duality.tex:77`: "Koszul conductor K_B = 196" (CORRECT, per authoritative Fehily-Kawasetsu-Ridout convention)
- Compute layer: SPLIT -- `ds_shadow_higher_arity.py` has K=76; `bershadsky_polyakov_bar.py` has K=196; tests assert BOTH values in different files.

The root cause: two different central charge formulas for BP. The principal W_3 formula c = 2 - 3(2k+3)^2/(k+3) gives K=76 (WRONG for BP); the non-principal BP formula c = -(12k^2 + 34k + 21)/(k+3) gives K=196 (CORRECT for BP). The engines document this distinction but the appendix .tex still has the wrong value.

**Priority**: CRITICAL. This is a live AP1 violation affecting at least 3 files.

### 1.4 Undefined References

- **Vol I**: 3,330 unique undefined references (8,131 total warnings). This is an ENORMOUS number but most appear to be cross-reference targets for labels defined in chapters that are included conditionally or that rely on multi-pass compilation. A 2-pass rebuild should resolve most.
- **Vol II**: 994 unique undefined references (1,978 total). Many are V1-prefixed cross-volume references that require the Vol I aux file.

**Priority**: SERIOUS for any submission-blocking refs. Most are benign (multi-pass artifacts) but must be verified with a clean 2-pass build.

### 1.5 TODO/FIXME/XXX Comments

- **Vol I**: 16 across 3 files (lattice_foundations, yangians_drinfeld_kohno, yangians_computations)
- **Vol II**: 3 in w-algebras-w3.tex
- **Vol III**: 1 in bar_cobar_bridge.tex

**Priority**: MODERATE. These should be resolved before submission.

---

## SCALE 2: CHAPTER (Structural)

### 2.1 Three-Bar-Complex Distinction

The ordered/unordered/Lie bar distinction (AP82, AP85, AP102, AP104) is explicitly installed in:
- **Vol I**: 22 files mention "ordered bar" or "B^ord" etc.
- **Vol II**: 29 files
- **Vol III**: 5 files

**Files likely MISSING the distinction** (chapters that discuss bar complexes without specifying which):
- Vol I appendices: `signs_and_shifts.tex`, `homotopy_transfer.tex`, `koszul_reference.tex` -- these are reference appendices that should specify which bar.
- Vol I theory: `filtered_curved.tex`, `algebraic_foundations.tex` -- foundational chapters that set up the bar differential without the tripartite language.
- Vol II: 73 untouched files (102 total - 29 touched = 73) have NOT been swept for the three-bar distinction.

**Priority**: SERIOUS. The 73 untouched Vol II files are the biggest gap. The Vol I theory chapters that define the bar complex should be the first to install the distinction.

### 2.2 E_1 Primacy (AP104)

`princ:e1-primacy` is referenced in exactly 1 Vol I file (introduction.tex) and 0 Vol II files. The label is defined somewhere in Vol I but the principle is not cross-referenced.

Files explicitly discussing E_1 primacy: 7 in Vol I, 0 in Vol II (from the grep for "E_1.*primitive" etc.). Vol III CLAUDE.md has the thesis installed but the .tex files have not been audited for it.

**Priority**: SERIOUS. The E_1 primacy thesis needs to be installed as cross-references in Vol II (especially in the Swiss-cheese chapters, the ordered bar chapters, and the PVA descent chapters) and Vol III (the E_1/E_2 hierarchy chapters).

### 2.3 AP75 (Virasoro HH Polynomial-Ring Error)

The C[Theta] notation appears in:
- `koszul_pair_structure.tex:542,571` -- H*_cont(L_1) = C[Theta]
- `introduction.tex:1158` -- ChirHoch*(A) as "polynomial ring"
- `hochschild_cohomology.tex:141,249,790` -- multiple occurrences

AP94 established that ChirHoch*(Vir_c) has total dim at most 4, so calling it a "polynomial ring" is misleading. The H*_cont(L_1) = C[Theta] is a CONTINUOUS cohomology statement about the Witt algebra (correct), NOT about chiral Hochschild cohomology. The introduction.tex line conflates the two.

Vol II and Vol III: zero occurrences. Contained to Vol I.

**Priority**: SERIOUS. The introduction line 1158 must be corrected; the continuous cohomology statements in koszul_pair_structure and hochschild_cohomology are correct but should have a remark distinguishing them from ChirHoch.

### 2.4 AP91 (Scalar Coderivation Overclaim)

Only 2 occurrences remain:
- `en_koszul_duality.tex:1354`: correctly says the scalar coderivation picture "does not extend" (this is the FIX, not the bug)
- `thqg_critical_string_dichotomy.tex:1904`: says curvature "is a scalar coderivation" -- needs AP91 qualification that this fails at g >= 1.

**Priority**: MODERATE. One remaining instance needs qualification.

### 2.5 Proof-After-Conjecture (AAP4)

Multiline grep found 20+ files in Vol I and 20+ in Vol II with `\begin{conjecture}...\begin{proof}` patterns. However, the AP40 check for `\begin{theorem}` with `ClaimStatusConjectured` returns ZERO -- so the environment/tag mismatch is fully resolved. The proof-after-conjecture issue is separate: many conjectures have "evidence" blocks presented as proofs.

**Priority**: MODERATE. These should use `\begin{remark}[Evidence]` per AAP4, but this is editorial, not mathematical.

### 2.6 Em Dashes (Prose Standard)

- **Vol I**: 164 uncommented `---` occurrences across 40 files. Mechanical cleanup was declared COMPLETE, but 164 remain. Many are in `landscape_census.tex` (21), `higher_genus_complementarity.tex` (9), `ordered_associative_chiral_kd.tex` (7).
- **Vol II**: 94 across 32 files.
- **Vol III**: 233 across 30 files (many in notes/ directory).

**Priority**: MODERATE for Vols I-II (submission standard); MINOR for Vol III (notes are working documents).

---

## SCALE 3: VOLUME (Architectural)

### 3.1 Cross-Volume Reference Integrity

Vol II has 994 unique undefined references, many V1-prefixed. This means the cross-volume reference mechanism is fragile. Any label rename in Vol I silently breaks Vol II references.

**Priority**: SERIOUS. Need a systematic audit: extract all V1-* labels referenced in Vol II, verify each exists in Vol I. Same for V2-* references in Vol I.

### 3.2 Untouched Files

- **Vol I**: ~60 non-archive, non-standalone files were NOT modified in the last 10 commits. Most are appendices and archived material. The 15 appendix files have not been swept by the rectification programme.
- **Vol II**: 102 of 102 active files are untouched in the last 5 commits (only chapter and connection files were modified). This means the ENTIRE Vol II source is stale relative to the current session's architectural changes.
- **Vol III**: All 48 active .tex files are untouched in the last 5 commits (only the rectification of AP40/AP4 in the most recent commit).

**Priority**: CRITICAL for Vol II (the entire volume has not absorbed the three-bar-complex or E_1 primacy changes). SERIOUS for Vol III.

### 3.3 Vol II SC^{ch,top} Description

The Vol II preface and introduction were recently modified (in the last 5 commits), but the 73 untouched connection and theory chapters still describe SC^{ch,top} without the updated understanding from the 22-agent swarm. In particular:
- The distinction between the three coproducts on the bar (Lie^c vs Sym^c vs T^c) is installed in 29 Vol II files but absent from 73.
- The E_1/ordered bar as primitive is not cross-referenced anywhere in Vol II.

**Priority**: SERIOUS.

### 3.4 Vol III Positioning

Vol III CLAUDE.md has the E_1 primacy thesis installed correctly (the section "E_1/Ordered as Primitive" was added 2026-04-08). However:
- The .tex theory chapters (cy_to_chiral.tex, e1_chiral_algebras.tex, e2_chiral_algebras.tex) were modified in the last 3 commits but the specific E_1 primacy content was installed only in CLAUDE.md, not in the .tex prose.
- The 30 notes/ files have 233 em dashes and no E_1 primacy language.

**Priority**: MODERATE. The notes are working documents, but the theory chapters should have the architectural principle.

---

## SCALE 4: PROGRAMME (Mathematical Frontier)

### 4.1 Genuine Open Problems from This Session

1. **Mixed-sector control**: The swarm established that delta_F_g^cross lives in the CLOSED sector (AP93), not the mixed sector. The open question: what does the mixed sector (open-closed channels in the Swiss-cheese sense) actually control? The annulus trace provides the first open-to-closed map at genus 1; the full modular cooperad structure is the programme. **Status**: No theorem formulated yet. This is a genuine research direction.

2. **E_1 primacy as theorem**: The thesis "E_1/ordered is primitive, modular/symmetric is derived" is installed as ARCHITECTURE but lacks a single clean theorem statement. Candidate: "The averaging map av: g^{E_1} -> g^{mod} is a surjective quasi-isomorphism of dg Lie algebras, and the kernel ker(av) carries exactly the quantum group / R-matrix data." This would make E_1 primacy load-bearing. **Status**: Not formulated. Requires proof that av is a qi (or at least surjective on cohomology).

3. **Deformation quantization gaps** (from agent 20 of the swarm): Three gaps identified:
   - Gap A: The chain-level S^3-framing for CY3 categories (blocks CY-A at d=3). Closable? No -- requires new geometric input (Costello-Li level).
   - Gap B: The evaluation-to-full extension (DK-4/5, downstream of MC3). Closable? Partially -- Francis-Gaitsgory pro-nilpotent completion handles compacts.
   - Gap C: The modular factorization envelope as left adjoint. Closable? This is conj:platonic-adjunction, still open. Referenced in 9 Vol I files and 4 Vol II files.

4. **Lie bracket on Hom(Sym^c, A) vs MC elements**: The three-bar-complex picture raises the question: the Lie bracket on the convolution algebra is determined by the Lie^c restriction of the bar coproduct, but the MC elements (which encode the full modular structure) live in higher Eulerian weights. What is the precise relationship? This is a question about the Eulerian weight decomposition of the convolution algebra and has not been formulated as a theorem.

5. **K11 perfectness**: The Lagrangian Koszulness criterion (K11) is conditional on perfectness and nondegeneracy. This was proved unconditional for the standard landscape (prop:lagrangian-perfectness) but the general statement remains conditional. Whether perfectness holds for all positive-energy chiral algebras is open.

### 4.2 Theorems That Could Be Proved

1. **av surjectivity on cohomology**: The averaging map av: g^{E_1}_A -> g^{mod}_A should be surjective on H^* for Koszul algebras (the ordered bar sees everything the symmetric bar does). This would be a clean theorem making E_1 primacy precise.

2. **Euler-weight decomposition of MC space**: The MC elements in the convolution algebra decompose by Eulerian weight. The weight-1 (Harrison) component controls the Lie bracket; the weight-2 component controls the commutative (symmetric) structure. A theorem relating these to the three bar complexes would close the architectural gap.

3. **delta_F_g^cross computation at genus 3**: The genus-2 cross-channel correction for W_3 is computed (delta_F_2 = (c+204)/(16c)). The genus-3 analogue would test universality of the cross-channel pattern. The planted-forest engine exists but the W_3-specific genus-3 computation has not been done.

### 4.3 Concordance Currency

The concordance (chapters/connections/concordance.tex) was modified in the last 5 commits, but:
- The three-bar-complex picture is NOT reflected in concordance (no section on ordered vs unordered vs Lie bar).
- The E_1 primacy principle is NOT reflected in concordance.
- The AP81-AP104 anti-patterns are referenced only in CLAUDE.md, not in the concordance or editorial constitution.

**Priority**: SERIOUS. The concordance is "the constitution" but lags behind the current session's architectural discoveries.

---

## SCALE 5: EPISTEMIC (Verification)

### 5.1 Compute Coverage

- **Total engines**: 1,178 in Vol I (non-archive)
- **Engines without tests**: 62 (5.3% untested)
- **Notable untested engines**:
  - `cohft_*.py` (5 engines): CohFT-related computations with no verification
  - `dmod_*.py` (5 engines): D-module purity computations with no verification
  - `mg_*.py` (5 engines): Moduli space graph computations with no verification
  - `mc4_*.py` (2 engines), `mc5_*.py` (1 engine): frontier MC programme engines untested
  - `mumford_chiodo_multiweight_engine.py`: the multi-weight genus expansion engine has NO test file (but contains the key formula delta_F_2(W_3) = (c+204)/(16c))

**Priority**: CRITICAL for mumford_chiodo_multiweight_engine.py (load-bearing formula, no test). SERIOUS for the 62 untested engines generally.

### 5.2 Multi-Path Verification Gaps

The mandate requires 3+ independent verification paths per numerical claim. Key claims lacking this:
1. **delta_F_2(W_3) = (c+204)/(16c)**: Computed in mumford_chiodo_multiweight_engine.py but NO test file exists. At most 1 verification path.
2. **Q^contact_Vir = 10/[c(5c+22)]**: Verified in multiple engines but should be cross-checked against the quartic shadow engine.
3. **BP Koszul conductor K=196**: Verified in bershadsky_polyakov_bar.py and theorem_gz_frontier_engine.py but CONTRADICTED by ds_shadow_higher_arity.py (K=76) and appendix .tex (K=76). Fails multi-path: two paths give 196, two give 76.
4. **Genus-3 planted-forest correction**: The 11-term polynomial (eq:delta-pf-genus3-explicit) is computed in pixton_shadow_bridge.py but the "genus-1+ vertex weights approximate" caveat means this is not fully verified.

### 5.3 Theorems Tagged ProvedHere Without Audit

Total ProvedHere tags: 2,898 in Vol I. This session's swarm audited the five main theorems (A-D+H) and confirmed them sound. The rectification programme swept ~63 chapters. But:
- The 15 appendix files were NOT swept by the rectification programme.
- The 59 remaining active non-archive files (122 total - 63 swept) were not individually audited.
- The 228 conjecture environments have not been systematically checked against the proved core to see if any can be upgraded.

**Priority**: MODERATE. The unswept files are mostly examples and connections chapters; the load-bearing theory chapters were swept.

### 5.4 Stale Conjectured Tags

228 conjecture environments in Vol I, 261 ClaimStatusConjectured tags across 51 files. Several conjectures have been proved since being tagged:
- conj:platonic-completion -> thm:platonic-completion (PROVED, but need to verify all 9 reference sites are updated)
- conj:log-clutching-degeneration -> proved (via Mok25)
- conj:operadic-complexity (still OPEN -- shadow depth = A_infty depth identification is PROVED by thm:shadow-formality-identification, but the L_infty formality level equivalence is conjectural)

**Priority**: MODERATE. A systematic grep for conj: labels that have corresponding thm: labels would catch stale downgrades.

---

## SCALE 6: PUBLICATION (Presentation)

### 6.1 Hostile Referee Issues

A hostile Inventiones/Annals referee would flag:

1. **3,330 undefined references in Vol I**: Even if most resolve with multi-pass compilation, ANY undefined reference in a submitted manuscript is unacceptable. This must be reduced to ZERO.

2. **K_BP = 76 vs 196 contradiction within the same volume**: An internal inconsistency between the appendix and the standalone paper would destroy credibility.

3. **AP74 flag: numerically false Bernoulli-Dirichlet identity** (arithmetic_shadows.tex:2990): A formula flagged as numerically false that is still in the manuscript is a fatal error.

4. **62 untested compute engines**: A referee checking the "computationally verified" claims would find 5.3% of engines have no tests at all.

5. **Proof-after-conjecture** in 20+ files: Evidence blocks formatted as proofs of conjectural statements would raise scope-honesty concerns.

6. **164 em dashes in Vol I, 94 in Vol II**: Minor prose issue but signals inconsistent editorial standards.

### 6.2 AI Slop

Zero occurrences of "notably", "crucially", "remarkably", "intriguingly", "importantly" across all three volumes. This is excellent -- the prose fortification campaign was thorough.

### 6.3 Bibliography

The bibliography was modified in the last 5 commits. Missing references from the swarm findings:
- The swarm identified AP104 (E_1 primacy) as connected to Fresse (2009, operadic bar), Vallette (2020, operadic Koszul duality), Loday-Vallette (2012, algebraic operads). These should be in the bibliography if not already.
- The three-bar-complex picture cites Harrison (1962), Barr (1968), Gerstenhaber-Schack (1987), Fresse (2004). Verify these are present.

**Priority**: MODERATE.

### 6.4 Index Entries

New concepts from this session that need index entries:
- "Ordered bar complex" / "E_1-bar complex"
- "Eulerian weight decomposition"
- "Three-bar-complex picture"
- "Averaging map (convolution to modular)"
- AP104 principle

**Priority**: MINOR for submission; important for usability.

---

## SUMMARY: TOP 15 PRIORITIES

| Rank | Scale | Item | Severity |
|------|-------|------|----------|
| 1 | LOCAL | K_BP = 76 vs 196 contradiction (appendix + compute) | CRITICAL |
| 2 | LOCAL | AP74: numerically false Bernoulli-Dirichlet identity | CRITICAL |
| 3 | LOCAL | subregular_hook_frontier.tex:1075 OPEN CRITICAL flag | CRITICAL |
| 4 | VERIFY | mumford_chiodo_multiweight_engine.py has NO test file | CRITICAL |
| 5 | LOCAL | Failing test: test_theorem_bethe_mc_engine (pi/2 < 1e-6) | SERIOUS |
| 6 | VOLUME | Vol II: 73/102 files untouched by three-bar/E_1 rectification | SERIOUS |
| 7 | CHAPTER | E_1 primacy not cross-referenced in Vol II (0 refs) | SERIOUS |
| 8 | LOCAL | 8 OPEN RECTIFICATION-FLAGs in Vol I (4 SERIOUS) | SERIOUS |
| 9 | VOLUME | Cross-volume reference integrity (994 undefined in Vol II) | SERIOUS |
| 10 | PROGRAMME | Concordance does not reflect three-bar or E_1 primacy | SERIOUS |
| 11 | CHAPTER | 20+ files with proof-after-conjecture (AAP4) in each volume | MODERATE |
| 12 | VERIFY | 62 compute engines without test files (5.3%) | MODERATE |
| 13 | LOCAL | 164 em dashes in Vol I, 94 in Vol II | MODERATE |
| 14 | CHAPTER | AP91 scalar coderivation: 1 remaining instance | MODERATE |
| 15 | CHAPTER | introduction.tex:1158 "polynomial ring" for ChirHoch | MODERATE |

---

## WHAT IS GENUINELY DONE

To be maximally honest:

1. **AP40 (env/tag mismatch)**: ZERO theorem environments with Conjectured tags across all 3 volumes. Fully resolved.
2. **AI slop**: ZERO occurrences across all 3 volumes. Fully resolved.
3. **Five main theorems (A-D+H)**: Confirmed sound by multiple swarm audits.
4. **MC1-MC4**: All proved, status consistent across volumes. **MC5**: Analytic HS-sewing lane proved at all genera; genuswise BV/BRST/bar identification conjectural (genus-0 algebraic BRST/bar comparison proved, tree-level amplitude pairing conditional).
5. **AP104 in CLAUDE.md**: Installed in all three volumes.
6. **Three-bar-complex in Vol I**: Installed in 22 files including all load-bearing theory chapters.
7. **Test suite**: 118,826 test definitions across 3 volumes -- an extraordinary verification layer.
8. **Koszulness programme**: 10 unconditional + 1 conditional + 1 one-directional, consistent everywhere.

## WHAT WAS SWEPT BUT NOT DEEPLY VERIFIED

1. **Vol I rectification programme**: 63 chapters swept with ~96 fixes, but the 15 appendices and ~20 remaining active files were not individually audited.
2. **Vol II**: Only 30 files touched in last 5 commits; 72 files have received NO attention from the current session.
3. **Vol III**: Only AP40/AP4 rectification (47 tags, 2 proof-after-conjecture fixes). No structural or mathematical audit.
4. **Cross-volume consistency**: The Vol I changes (three-bar, E_1 primacy, AP81-AP104) have NOT been propagated to Vol II or Vol III .tex files.
5. **Build cleanliness**: The 3,330 undefined references in Vol I suggest the build is not in a clean state (likely needs 2-pass rebuild or conditional includes adjustment).
