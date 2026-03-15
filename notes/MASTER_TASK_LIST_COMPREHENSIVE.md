# COMPREHENSIVE MASTER TASK LIST
## Modular Homotopy Theory for Factorization Algebras on Curves (Volumes I & II)

**Generated**: 2026-03-15
**Scope**: Everything stated, unstated, hinted, conjectured, and implied across both volumes.
**Sources**: CLAUDE.md, MEMORY.md, concordance.tex (both volumes), PROGRAMMES.md, NEW_MACHINERY.md, conclusion.tex (Vol II), session context.

**Priority key**: P0 = do now, P1 = do soon, P2 = do when ready, P3 = research frontier
**Complexity key**: S = small (<1hr), M = medium (1-4hr), L = large (4hr+), XL = multi-session
**Dependencies**: listed by task ID

---

## CATEGORY A: Vol I Exposition (Strike List Remnants)

### A1. Structural Splits

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| A1.1 | Split `bar_cobar_construction.tex` (12,906 lines) into 2-3 chapters: (a) bar construction + Arnold, (b) cobar construction + twisting morphisms, (c) bar-cobar adjunction + Verdier intertwining | P1 | XL | -- |
| A1.2 | Reorganize `free_fields.tex` (3,821 lines): deduplicate Virasoro (appears 3x), consolidate WZW, separate bc/betagamma into clean family structure | P1 | L | -- |
| A1.3 | Compress `yangians.tex` lines 837-1927: ~1100 lines of repetitive propositions, target 60% compression while preserving all proved content | P1 | L | -- |
| A1.4 | Compress abstract from ~1900 words to 400-500 words (Annals/Asterisque standard) | P0 | M | -- |
| A1.5 | Merge `sign_conventions.tex` fully into `signs_and_shifts.tex` (3 appendices -> 1 unified appendix) | P1 | M | -- |

### A2. Notation Standardization (Cross-File)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| A2.1 | Standardize bar differential naming: unify `d_bar`, `d_B`, `d_{bar}` across all chapters | P1 | M | -- |
| A2.2 | Standardize bar complex notation: unify `B(A)`, `\bar{B}(A)`, `\barB(\cA)` across all chapters | P1 | M | -- |
| A2.3 | Standardize Hochschild notation: unify `HH^*`, `ChirHoch^*`, `HC^*` across theory and examples | P1 | M | -- |
| A2.4 | Standardize propagator notation: resolve `eta` vs `omega` for the FM propagator | P1 | S | -- |
| A2.5 | Standardize differential notation: ensure `\dfib`, `\Dg{g}`, `\dzero` used consistently per CLAUDE.md | P1 | M | -- |
| A2.6 | Standardize H/M/S level annotations: ensure every theorem/conjecture identifies its semantic level | P2 | L | -- |

### A3. Incomplete Proofs (~18 remaining)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| A3.1 | Audit all "sketch" proofs and replace with complete arguments | P1 | XL | -- |
| A3.2 | Audit all "the proof is similar" instances and provide explicit proofs | P1 | L | -- |
| A3.3 | Audit all placeholder proofs (marked or implied) and complete | P1 | XL | -- |
| A3.4 | Verify all ClaimStatus annotations match actual proof density | P2 | L | -- |

### A4. Redundancy Elimination (~12 items)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| A4.1 | Deduplicate Virasoro content: 3 independent treatments in `free_fields.tex` | P1 | L | A1.2 |
| A4.2 | Deduplicate bc/betagamma content: appears in 3 places | P1 | M | A1.2 |
| A4.3 | Deduplicate KM level-shifting: appears in `kac_moody_framework.tex` and `concordance.tex` | P2 | S | -- |
| A4.4 | Consolidate DS reduction exposition: scattered across `w_algebras_framework.tex`, `w_algebras_deep.tex`, `w3_composite_fields.tex` | P2 | M | -- |

### A5. Bibliography

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| A5.1 | Fix 10 pre-existing undefined bibliography entries (Ahlfors, Mumford, Rudin, etc.) | P0 | S | -- |
| A5.2 | Verify all ~270 bibliography entries have correct journal/year/page data | P2 | L | -- |
| A5.3 | Add missing bibliography entries identified in recent sessions | P1 | S | -- |

### A6. Formatting

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| A6.1 | Fix 7 remaining overfull boxes (minor, 1-3pt) | P0 | S | -- |
| A6.2 | Final pass on index entries for completeness | P2 | L | -- |
| A6.3 | Verify all cross-references resolve (0 undefined refs target) | P0 | S | -- |

---

## CATEGORY B: Vol II Exposition (Deep Read Findings)

### B1. Structural Bridges and Theorems

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| B1.1 | State the Volume I bridge as a theorem: bar complex + coproduct = SC^{ch,top}-algebra (currently only implicit) | P0 | M | -- |
| B1.2 | Develop the Steinberg analogy: convolution on FM(C) x Conf(R) paralleling Steinberg variety / Hecke algebra | P1 | M | -- |
| B1.3 | State curved A-infinity bridge as theorem/conjecture: curved bar at genus g = curved A-infinity with m_0 = kappa * omega_g | P0 | M | -- |
| B1.4 | State main PVA theorem first in Section 6 (reorg: conclusion before proof) | P1 | M | -- |

### B2. Missing Computations

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| B2.1 | Work out concrete bar element B_ch(H_k) in degrees 1, 2, 3 for Heisenberg | P0 | L | -- |
| B2.2 | Evaluate LG m_3 integral explicitly (Landau-Ginzburg cubic) | P1 | L | -- |
| B2.3 | Work out d_Q + d_res + d_{A-infinity} on a concrete 3-term bar element | P1 | M | -- |
| B2.4 | Verify Virasoro r-matrix against CYBE | P1 | M | -- |
| B2.5 | Compute W_3 spectral R-matrix | P2 | L | -- |

### B3. Missing Transitions and Remarks

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| B3.1 | Add physical remark on contractibility and d'=1 (after Prop 7.8) | P1 | S | -- |
| B3.2 | Add three missing transitions: BV->FM, PVA->Hochschild, bar-cobar->line operators | P1 | M | -- |
| B3.3 | Add early roadmap of conditional vs unconditional results | P0 | M | -- |
| B3.4 | Flesh out lines-as-modules proof (essential surjectivity) | P1 | L | -- |
| B3.5 | Add Laplace transform = spectral duality remark | P2 | S | -- |
| B3.6 | Add "why this product structure is forced" argument in `foundations.tex` | P1 | M | -- |

### B4. Reorganization

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| B4.1 | Move Recognition Conjecture after BV construction (better logical flow) | P1 | M | -- |
| B4.2 | Move ambient complementarity to concordance or standalone section | P2 | M | -- |
| B4.3 | Make conclusion concrete (specific connections, not generic future directions) | P1 | M | -- |
| B4.4 | Add Vol II claim status tags throughout (currently absent) | P0 | L | -- |

---

## CATEGORY C: Cross-Volume Bridges

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| C1 | Prove or precisely conjecture: chiral bar complex = SC^{ch,top}-algebra. Vol II concordance lists this as "Conjectured" bridge. | P1 | XL | -- |
| C2 | Prove: curved bar at genus g = curved A-infinity with m_0 = kappa * omega_g. Connect Vol II's BV-derived A-infinity to Vol I's genus tower. | P1 | L | -- |
| C3 | Prove: Vol II's Hochschild complex -> Vol I's polynomial Hochschild (Theorem H). The bulk-Hochschild identification (Thm 7.11 in Vol II) should specialize. | P1 | L | -- |
| C4 | State and prove: bar-cobar adjunction commutes with DS reduction. Would connect Vol II's W-algebra examples to Vol I's DS-Koszul intertwining. | P2 | XL | -- |
| C5 | State: spectral R-matrix from Vol II specializes to Vol I's DK ladder at evaluation locus. Bridge between spectral braiding (Vol II Sec 9) and DK-0/1 (Vol I). | P2 | L | -- |
| C6 | State: PVA descent (Vol II) recovers Coisson structure (Vol I) when X = point. Bridge between PVA (Vol II Sec 6) and Coisson/P-infinity-chiral (Vol I). | P2 | M | -- |
| C7 | State: formality obstruction (d'=1 failure) connects to genus-1 curvature d^2 = kappa * omega_1. Vol II concordance research signal (1). | P2 | L | -- |
| C8 | State: (H1)-(H4) + BV-BRST should imply chiral Koszulness. Vol II concordance research signal (2). | P3 | XL | -- |
| C9 | State: higher-genus A-infinity structure with spectral parameters. Vol II concordance research signal (3). | P3 | XL | -- |
| C10 | State: spectral braiding beyond evaluation promotes R(z) to full factorization category. Vol II concordance research signal (4). Advances MC3. | P3 | XL | -- |

---

## CATEGORY D: Mathematical Frontier (MC Hierarchy)

### D1. MC3 — Factorization DK Beyond Evaluation-Generated Core

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| D1.1 | Resolve Baxter exact triangles (conj:baxter-exact-triangles): categorical lift from K_0-level TQ to natural transformations of exact functors. 498 tests verify K_0 level. | P2 | XL | -- |
| D1.2 | Resolve shifted-prefundamental generation (conj:shifted-prefundamental-generation): prove thick generation of O^{sh}_{<=0} by evaluation + prefundamental modules. 186 tests on L^-_a. | P2 | XL | D1.1 |
| D1.3 | Resolve pro-Weyl recovery (conj:pro-weyl-recovery): construct A-infinity or dg model for pro-Weyl limit M(Psi). 344 tests on ML conditions. | P2 | XL | D1.2 |
| D1.4 | Resolve DK on compacts (conj:dk-compacts-completion): Feigin-Gainutdinov completion gap. 101 tests. | P3 | XL | D1.1, D1.2, D1.3 |
| D1.5 | Extend sectorwise finiteness and factorization descent to completed/coderived enlargement beyond eval-gen core | P3 | XL | D1.1-D1.4 |
| D1.6 | Resolve conj:mc3-sectorwise-all-types: extend sectorwise convergence from evaluation-generated core to full module categories | P3 | XL | D1.5 |

### D2. MC4 — W-infinity and Yangian Infinite Towers

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| D2.1 | W-infinity: resolve stage-4 six-defect vanishing (C^{res} = C^{DS} on I_4). 121 tests on DS side. | P2 | L | -- |
| D2.2 | W-infinity: promote I_4 to I_N via incremental packets J_{M+1}. Reduction chain is explicit. | P2 | XL | D2.1 |
| D2.3 | W-infinity: construct filtered H-level target W^{ht} with finite quotients W_N | P3 | XL | D2.1, D2.2 |
| D2.4 | W-infinity: large-N coupling identification lambda -> 1-lambda (conj:w-infty-bar) | P3 | XL | D2.3 |
| D2.5 | Yangian: resolve DK-4 algebraic identification (MC element, translation, coproduct for g_A = Y^{dg}). Analytic part done (ML + completed bar-cobar). | P2 | XL | -- |
| D2.6 | Yangian: RTT-adapted realization of canonical dg model U^{comp}(g_A). Proposition criteria in place. | P3 | XL | D2.5 |
| D2.7 | Yangian: prove C^{res} = C^{DS} on I_N and K^{line} = K^{RTT} on Delta_{a,0}(N). 219 tests verify low N. | P2 | L | D2.5 |
| D2.8 | Yangian: single degree-2 identity r_a^{fund}(z)(e_1 x e_2) = -hbar(e_2 x e_1) on ordered fundamental line. Factorization side carries this coefficient. | P2 | L | D2.7 |
| D2.9 | Resolve conj:winfty-stage4-ward-inheritance: visible weight-4 normalization conjecture C^{res}_{4,4;2;0,6}(4) = 2 | P2 | M | D2.1 |
| D2.10 | Resolve conj:winfty-stage5-higher-spin-identities: next finite bar-vs-DS identity list | P2 | L | D2.1, D2.9 |

### D3. MC5 — BV/BRST = Bar at Higher Genus

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| D3.1 | Resolve disk-local packet (conj:disk-local-perturbative-fm): identify local perturbative BRST brackets with bar residue operations on C_2 and C_3 strata | P2 | L | -- |
| D3.2 | Resolve compactified ternary comparison on M_{0,4}: two-coefficient packet a_{pert}=a_{bar}, b_{pert}=b_{bar} | P2 | L | D3.1 |
| D3.3 | Extend holomorphic-to-real propagator from genus 0 to genus g >= 1 (Costello renormalization data required) | P3 | XL | D3.2, D1.*, D2.* |
| D3.4 | Prove conj:anomaly-physical: BV-BRST identification extends to all genera | P3 | XL | D3.3 |

### D4. DK Ladder (Beyond Proved Core)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| D4.1 | DK-4: complete algebraic identification. ML proved; remaining is algebraic ID (MC element, translation, coproduct). | P2 | XL | D2.5 |
| D4.2 | DK-5: resolve 3 unproved assumptions (conjectural) | P3 | XL | D4.1 |

### D5. Independent Frontier Problems

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| D5.1 | Periodicity sync: reconcile lcm/profile shadow with sharp geometric factors. Orthogonal weak flank. | P3 | L | -- |
| D5.2 | Coderived Ran space theory: off-Koszul bar-cobar inversion (conj:off-koszul-ran-inversion). H1 structural gap. | P3 | XL | -- |
| D5.3 | Reflected modular periodicity (conj:reflected-modular-periodicity): independent of MC chain | P3 | L | -- |
| D5.4 | Derived bc-betagamma (conj:derived-bc-betagamma): Koszul check verified at 57 tests | P2 | L | -- |
| D5.5 | W-orbit duality (conj:w-orbit-duality): W^k(g,f)^! = W^{k'}(g,f^D). Principal proved; subregular partial. Frontier now at sl_{20} hook family. | P2 | XL | -- |
| D5.6 | DS transport of T_br (spectral branch): full T_br is NOT DS-invariant for rank >= 2. Refined formulation needed. | P2 | L | -- |
| D5.7 | Completion frontier (H3 hypothesis): finite-stage bar-cobar compatibility for infinite-type algebras | P3 | XL | -- |

---

## CATEGORY E: Computational Frontier

### E1. Bar Cohomology Verification

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| E1.1 | W_4 DS OPE extraction of 4 free coefficients (stage-4 structural analysis). 72 tests done. | P1 | L | -- |
| E1.2 | Verify W_3 H^5 = 171 (conjectured): confirm/deny algebraicity of W_3 bar GF | P2 | L | -- |
| E1.3 | Verify Y(sl_2) H^4 = 82 (conjectured): feasible 37M-entry matrix | P2 | L | -- |
| E1.4 | Verify H^4(B(sl_3)) = 1352 (conjectured): requires chiral-bar-specific methods (786K chain groups) | P3 | XL | -- |
| E1.5 | Understand sl_3 Koszul dual dims going negative at deg 8 (mechanism; sl_2 also negative at deg 12) | P2 | M | -- |

### E2. KL/Root-of-Unity Computations

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| E2.1 | Determine categorical meaning of exact 66-dimensional N=4 packet (palindromic staircase 1,4,8,12,16,12,8,4,1) | P2 | XL | -- |
| E2.2 | Determine whether one flavor or paired packet controls semisimplified KL target from N=3 packet dim H^{1,2}_2 = 3 | P2 | L | -- |
| E2.3 | Compute N=5 q-bar cohomology: next discriminant beyond N=4 | P3 | XL | E2.1 |
| E2.4 | Determine if Dirichlet Schrodinger operator with sextic potential lifts to H/M-level KL mechanism | P3 | L | E2.1 |

### E3. MC2/Theta_A Computations

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| E3.1 | Compute H^2(B-bar(sl2_{-2})) and compare with Omega^2(Op_{PGL2}(D)) (Programme I entry) | P2 | L | -- |
| E3.2 | Extend MC2 cyclic L-infinity scaffold to higher arities (beyond l_3) | P2 | L | -- |

### E4. Open Conjectures (~34 from G1-G34)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| E4.1 | Resolve ~34 open conjectures catalogued as G1-G34 in master task list v27 (all labeled, research-grade) | P3 | XL | various |

### E5. Structural Gaps (~8 from H1-H8)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| E5.1 | H1: Coderived Ran formalism — off-Koszul bar-cobar inversion | P3 | XL | -- |
| E5.2 | H2: W-infinity H-level realization — RESOLVED by thm:winfty-factorization-kd; remaining is large-N coupling | P2 | L | D2.4 |
| E5.3 | H3: Thick generation beyond Rep_fd — extension to non-polynomial infinite-dimensional modules | P3 | XL | D1.2 |
| E5.4 | H4: Baxter derived lift — categorical lift from SES to natural transformations | P3 | XL | D1.1 |
| E5.5 | H5: Prefundamental generation — finite resolution by evaluation + prefundamental summands | P3 | XL | D1.2 |
| E5.6 | H6: Pro-Weyl M-level lift — A-infinity model for pro-Weyl limit | P3 | XL | D1.3 |
| E5.7 | H7: Holomorphic-to-real propagator extension — Costello renormalization data | P3 | XL | D3.3 |
| E5.8 | H8: DS transport of T_br — full transfer operator NOT DS-invariant at rank >= 2 | P2 | L | D5.6 |

---

## CATEGORY F: Infrastructure

### F1. Vol I Infrastructure

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| F1.1 | Fix corrupt git tree object 1074f0f4 (blocks git log past 29 commits) | P1 | M | -- |
| F1.2 | Push 19 commits ahead of origin | P0 | S | F1.1 |
| F1.3 | Run full census via `scripts/generate_metadata.py` and verify totals | P0 | S | -- |

### F2. Vol II Infrastructure

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| F2.1 | Upgrade Vol II Makefile to match Vol I: multi-pass, stamp-based idempotent, metadata integration, integrity gates | P1 | M | -- |
| F2.2 | Expand Vol II test suite from 5 modules (~133 tests) to match Vol I density (~40+ modules, ~6K tests) | P2 | XL | -- |
| F2.3 | Add claim status tags throughout Vol II (currently absent; Vol II concordance uses text-based status) | P0 | L | -- |
| F2.4 | Create Vol II metadata generation: census script, dependency graph, claim counter | P2 | M | -- |
| F2.5 | Add Vol II index entries for all theorem-class environments | P2 | L | -- |

---

## CATEGORY G: Research Programmes (from PROGRAMMES.md)

### G1. Programme I: Geometric Langlands via Critical-Level Bar Complex

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G1.1 | Prove full derived identification: B-bar(g_{-h^v}) = O(Op^{dR}_{g^v}(X)) for all n | P3 | XL | E3.1 |
| G1.2 | Compute H^2(B-bar(sl2_{-2})) explicitly via PBW SS (entry computation) | P2 | L | -- |
| G1.3 | Build derived algebraic geometry interface for bar complexes (Tool 1.1 from NEW_MACHINERY) | P3 | XL | -- |
| G1.4 | Compute PBW SS beyond E_1 for sl_2 (Tool 1.2 from NEW_MACHINERY) | P2 | L | G1.2 |

### G2. Programme II: Kazhdan-Lusztig from Bar-Cobar

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G2.1 | Promote admissible-level N-complex certificate to periodic/coderived KL object (conj:kl-periodic-cdg -> conj:kl-coderived -> conj:kl-braided) | P3 | XL | E2.1, E2.2 |
| G2.2 | Determine categorical meaning of first computed sl_2 packet dim H^{1,2}_2 = 3 | P2 | L | -- |
| G2.3 | N-complex homological algebra: determine which flavor/paired packet controls KL categories | P3 | XL | G2.2 |
| G2.4 | Tensor structure: prove monoidality via Programme III (fusion preservation) | P3 | XL | G3.1 |

### G3. Programme III: Fusion Product Preservation

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G3.1 | Prove conj:fusion-bar-cobar: module bar-cobar functor Phi is monoidal | P3 | XL | -- |
| G3.2 | Verify monoidality for Heisenberg Fock modules (entry computation) | P2 | L | -- |
| G3.3 | Show bar coalgebra coproduct intertwines with fusion tensor product | P3 | XL | G3.2 |

### G4. Programme IV: Higher-Dimensional E_n Koszul Duality

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G4.1 | Write explicit bar differential formulas in Totaro generators at n >= 3 (computational refinement) | P3 | L | -- |
| G4.2 | Define E_2-bar complex using Brieskorn algebra elements, compute for Chains(Omega^2 S^3) | P3 | XL | -- |
| G4.3 | Compare n=3 E_3-bar complex with perturbative Chern-Simons (connects to Programme V) | P3 | XL | G4.1 |

### G5. Programme V: Vassiliev Invariants from Feynman Transform

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G5.1 | Restrict genus-0 bar complex of sl_2 to configuration spaces of S^1, compare with Kontsevich integral | P3 | L | -- |
| G5.2 | Resolve conj:vassiliev-bar: higher-genus loop expansion of Kontsevich integral | P3 | XL | G5.1 |
| G5.3 | Prove holomorphic -> topological Feynman transform comparison theorem | P3 | XL | G5.2 |

### G6. Programme VI: Mathematical Physics

#### G6a. BRST-Bar Identification

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G6a.1 | Extend genus-0 BRST-bar chain map to genus g >= 1 (requires Costello renormalization) | P3 | XL | D3.3 |
| G6a.2 | Construct explicit isomorphism for bosonic string (A = H^26 tensor bc) at genus 0 (entry computation, already done for KM/W) | P2 | L | -- |

#### G6b. Holographic Dictionary (AdS3/CFT2)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G6b.1 | Identify bulk observables with Costello-Li twisted SUGRA on AdS_3 | P3 | XL | -- |
| G6b.2 | Verify for sl2_k that H^0(B-bar) matches CS observable algebra on solid torus (dim = k+1) | P2 | L | -- |
| G6b.3 | Resolve conj:ads-cft-bar: curved bar complex provides algebraic model for bulk theory | P3 | XL | G6b.1 |

#### G6c. AGT Chain-Level Realization

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G6c.1 | Verify B-bar(Vir_c) computes equivariant chains on Hilb_n(C^2) for small n (G = SU(2) entry) | P3 | XL | -- |
| G6c.2 | Resolve conj:agt-bar-cobar: bar complex computes instanton partition function | P3 | XL | G6c.1 |

#### G6d. HCS/CL/4d-2d Functor

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G6d.1 | Compare CL factorization algebra for N=4 SYM with B-bar(g_{-h^v}) as factorization algebra | P3 | XL | G1.1 |
| G6d.2 | Resolve conj:CL-produces-chiral: CL construction produces chiral algebra | P3 | XL | G6d.1 |

#### G6e. Infinite-Generator Duality

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G6e.1 | W-infinity side: construct principal-stage compatible factorization target | P3 | XL | D2.3 |
| G6e.2 | Yangian side: construct RTT-adapted filtration on dg-shifted/factorization target | P3 | XL | D2.6 |
| G6e.3 | Prove stagewise coefficient identities on both towers | P3 | XL | D2.7, D2.1 |

#### G6f. 3d Mirror Symmetry

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G6f.1 | Identify Coulomb branch ring with specific E1-chiral bar complex | P3 | XL | -- |
| G6f.2 | Show symplectic duality corresponds to bar-cobar inversion | P3 | XL | G6f.1 |
| G6f.3 | Relate mass/FI deformations to curvature of bar complex | P3 | XL | G6f.2 |

#### G6g. Remaining Physics Conjectures (~26 items)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G6g.1 | NC Chern-Simons (conj:nc-cs) | P3 | XL | G6a.1 |
| G6g.2 | D-brane E1 (conj:dbrane-e1) | P3 | XL | -- |
| G6g.3 | q-AGT (thm:q-agt): 5d Nekrasov partition function | P3 | XL | G6c.2 |
| G6g.4 | GW S-duality | P3 | XL | -- |
| G6g.5 | WRT (thm:wrt-conjecture): Witten CS path integral | P3 | XL | G5.2 |
| G6g.6 | String amplitude correspondence | P3 | XL | G6a.1 |
| G6g.7 | Modular anomaly BRST (thm:modular-anomaly-brst) | P3 | XL | D3.4 |
| G6g.8 | Path integral = bar-cobar (conj:bar-cobar-path-integral) | P3 | XL | D3.4 |
| G6g.9 | Holographic Koszul (conj:holographic-koszul) | P3 | XL | G6b.3 |
| G6g.10 | CS factorization (conj:cs-factorization) | P3 | XL | G5.2 |

### G7. Programme VII: Noncommutative Hodge Theory

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G7.1 | Formulate notion of "twistor structure" on genus-graded object | P3 | XL | -- |
| G7.2 | Identify genus variable g_s with deformation parameter lambda | P3 | XL | G7.1 |
| G7.3 | Construct C*-action on de Rham complex of genus tower | P3 | XL | G7.2 |
| G7.4 | Resolve conj:nc-hodge: twistor interpretation of genus expansion | P3 | XL | G7.3 |

### G8. Programme VIII: Open Mathematical Conjectures

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G8.1 | W-orbit duality for general nilpotent data (conj:w-orbit-duality). Principal proved; hook family now at sl_{20}. Three exact packets (A,B,C) identified. | P2 | XL | -- |
| G8.2 | Scalar saturation universality (conj:scalar-saturation-universality): prove dim H^2_{cyc,prim}(A) = 0 at admissible levels | P2 | L | -- |
| G8.3 | Generating function conjectures (conj:w3-bar-gf, conj:sl3-bar-gf, conj:yangian-bar-gf, conj:non-simply-laced-discriminant): 82 self-consistency tests | P2 | L | E1.2, E1.3, E1.4 |
| G8.4 | Non-simply-laced discriminant conjecture | P3 | L | -- |

### G9. Programme IX: Computation

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| G9.1 | Extend n=7 PBW computation to n=8 (Casimir eigenspace extraction at scale) | P2 | L | -- |
| G9.2 | Complete W_4 DS OPE extraction: 4 remaining higher-spin coefficients | P1 | L | -- |
| G9.3 | KL N-complex: extend beyond N=4 degree-2 (next discriminant) | P2 | XL | E2.1 |
| G9.4 | Hook-pair DS: extend corrected semidirect check beyond sl_{20} | P2 | L | -- |
| G9.5 | MC4 boundary strip: extend Delta_{a,0}(N) verification beyond rank 4 | P2 | M | -- |

---

## CATEGORY H: Theta_A and Nonlinear Characteristic Layer

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| H1 | Resolve the nonlinear shadow tower: kappa -> Delta_A -> [C_A], o^(4), [Q_A] -> Theta_A (Ring 2 from CLAUDE.md) | P2 | XL | -- |
| H2 | Construct ambient complementarity as (-1)-shifted symplectic formal moduli with Lagrangian maps | P3 | XL | -- |
| H3 | Compute complementarity potential S_A for standard families | P2 | L | -- |
| H4 | Compute quartic resonance class R^{mod}_{4,g,n} for first nontrivial cases | P3 | L | -- |
| H5 | Compute branch-line reductions with universal genus-3 constant 7 | P2 | M | -- |
| H6 | Spectral characteristic Delta_A: identify structure beyond scalar kappa | P3 | XL | -- |

---

## CATEGORY I: Vol II Research Directions (from Conclusion)

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| I1 | Complete quantization: all-loop quantum corrections, convergence/finiteness under H1-H4, anomaly cancellations in d'=1 formality gap | P3 | XL | -- |
| I2 | Non-perturbative effects: instanton contributions, non-perturbative line operators, S-duality | P3 | XL | -- |
| I3 | Higher-dimensional generalizations: L-infinity chiral algebras for d' >= 2, polysimplicial chiral operads | P3 | XL | -- |
| I4 | Geometric Langlands connections via 3d HT theories | P3 | XL | G1.1 |
| I5 | Applications to knot invariants: categorical lifts of Jones/HOMFLY/Khovanov via A^!-modules | P3 | XL | G5.2 |
| I6 | Vol II homotopy-Koszulity conjecture (conj:homotopy-Koszul): SC^{ch,top} is homotopy-Koszul | P3 | XL | -- |
| I7 | Prove recognition conjecture (conj:recognition): A-infinity chiral algebras = SC^{ch,top}-algebras | P2 | XL | I6 |
| I8 | Prove filtered Koszul duality beyond quadratic locus (thm:filtered-koszul, conditional on conj:homotopy-Koszul) | P3 | XL | I6 |

---

## CATEGORY J: Ring 3 — Physics-Facing Frontier

### J1. W-Algebra Axis

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| J1.1 | Prove completed Koszulity is ubiquitous for affine W-algebras at generic level | P2 | L | -- |
| J1.2 | Characterize strict Koszulity as exceptional: subregular W_n^{(2)} has unbounded canonical arity | P2 | L | -- |
| J1.3 | Develop semistrict W_3 as first finite-arity modular higher-spin package (concordance appendix) | P2 | L | -- |

### J2. Yangian/RTT Axis

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| J2.1 | Local quadratic kernel + weightwise stabilized envelope + boundary quotient for RTT tower | P2 | XL | D2.6 |
| J2.2 | Orthogonal coideal descent | P3 | XL | -- |
| J2.3 | Rank-one Kleinian test case | P2 | L | -- |

### J3. Holographic/Celestial Axis

| ID | Task | Priority | Complexity | Deps |
|----|------|----------|------------|------|
| J3.1 | Protected bulk reconstruction | P3 | XL | G6b.3 |
| J3.2 | Cotangent reciprocity | P3 | L | -- |
| J3.3 | Weyl sewing and metaplectic anomaly | P3 | L | -- |
| J3.4 | Bulk/boundary/line Koszul triangle (Vol II) | P3 | XL | C1 |

---

## SUMMARY

| Category | Count | P0 | P1 | P2 | P3 |
|----------|-------|----|----|----|-----|
| A: Vol I Exposition | 24 | 4 | 15 | 5 | 0 |
| B: Vol II Exposition | 17 | 4 | 8 | 3 | 2 |
| C: Cross-Volume Bridges | 10 | 0 | 2 | 4 | 4 |
| D: Mathematical Frontier | 27 | 0 | 0 | 14 | 13 |
| E: Computational Frontier | 12 | 0 | 1 | 7 | 4 |
| F: Infrastructure | 8 | 3 | 3 | 2 | 0 |
| G: Research Programmes | 42 | 0 | 0 | 11 | 31 |
| H: Theta_A / Nonlinear | 6 | 0 | 0 | 3 | 3 |
| I: Vol II Research | 8 | 0 | 0 | 1 | 7 |
| J: Ring 3 Physics | 9 | 0 | 0 | 5 | 4 |
| **TOTAL** | **163** | **11** | **29** | **55** | **68** |

### Critical Path

The critical path for the monograph's mathematical frontier is:
```
Evaluation-generated core (PROVED)
  => MC3 enlargement (D1.1 -> D1.2 -> D1.3 -> D1.4 -> D1.5)
    => MC4 H-level comparison (D2.1 -> D2.2 -> D2.3 + D2.5 -> D2.6)
      => MC5 physics completion (D3.1 -> D3.2 -> D3.3 -> D3.4)
```

The critical path for publication readiness is:
```
A5.1 (bibliography) + A6.1 (overfull) + A6.3 (xrefs)  -- immediate
A1.4 (abstract)                                         -- immediate
B4.4 (Vol II claim tags) + B1.1/B1.3 (bridge theorems) -- urgent
A1.1 (split bar_cobar) + A1.2 (reorg free_fields)      -- near-term
A3.1-A3.3 (complete all proofs)                         -- essential
```

### Periodicity Note

Periodicity (D5.1, D5.3) is an **orthogonal weak flank**, not a bottleneck for any MC resolution. It should be worked on opportunistically, not at the expense of the MC3 -> MC4 -> MC5 chain.
