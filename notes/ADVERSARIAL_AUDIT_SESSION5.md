# Adversarial Audit — Session 5 (March 6, 2026)

## Methodology
- **Phase 1**: 10 parallel agents covering all 55+ .tex files across Theory, Examples, Connections, Appendices
- Cross-reference integrity audit (labels, claim statuses, notation, census drift)
- Each agent read every proof, checked formulas, verified sign conventions
- **Phase 2**: 8 parallel agents covering compute engine, build system, proof chains, bibliography, macros, formula cross-verification, physics conjectures, deep spot-checks

## Census (Fresh)
| Status | CLAUDE.md | Actual | Drift |
|--------|-----------|--------|-------|
| ProvedHere | 669 | 696 | +27 |
| ProvedElsewhere | 314 | 328 | +14 |
| Conjectured | 100 | 114 | +14 |
| Heuristic | 18 | 18 | 0 |
| **Total** | **1101** | **1156** | **+55** |

Three new files not in CLAUDE.md file map: `en_koszul_duality.tex`, `derived_langlands.tex`, `kontsevich_integral.tex`.

---

## FINDINGS SUMMARY

| Severity | Count |
|----------|-------|
| CRITICAL | 4 |
| MAJOR / HIGH | 34 |
| MEDIUM | 17 |
| MINOR / LOW | ~78 |
| **Total** | **~133** |

---

## CRITICAL FINDINGS (4)

### C1. Chiral Hochschild d^2=0 proof uses false associativity
- **File**: `hochschild_cohomology.tex:380-391`
- **Issue**: Proof of `thm:hochschild-chain-complex` asserts strict associativity `mu(mu(a,b),c) = mu(a,mu(b,c))` for chiral products. **Chiral algebras are NOT strictly associative** — they satisfy OPE associativity (Borcherds identity), not strict associativity.
- **Impact**: The d^2=0 proof is invalid. All Hochschild cohomology results downstream depend on this.
- **Fix**: Rewrite proof using factorization algebra axioms or Borcherds identity at the cochain level.

### C2. Virasoro Koszulness table contradicts its own theorem
- **File**: `chiral_koszul_pairs.tex:2307`
- **Issue**: Summary table lists Virasoro as "No" (not Koszul), directly contradicting `thm:virasoro-chiral-koszul` at line 346 in the same file, which PROVES Virasoro IS chiral Koszul (via PBW spectral sequence + I-adic completion).
- **Impact**: Readers of the summary get the opposite conclusion from the theorem.
- **Fix**: Correct table entry; rename "Non-example 1" subsection heading.

### C3. Sign error in Kac table duality formula (eq:kac-table-koszul)
- **File**: `chiral_modules.tex:3553-3554`
- **Issue**: The substitution q -> -q in h_{r,s} = ((pr-qs)^2 - (p-q)^2)/(4pq) should flip the denominator sign: 4p(-q) = -4pq. The formula is missing this sign. Propagates into wrong numerical values for Ising dual weights ({0, 33/16, 5/2} claimed; correct is {0, 17/16, 3/2}) and free boson duals.
- **Impact**: Three explicit numerical examples are wrong.
- **Fix**: Correct the formula and recompute all examples in lines 3553-3570.

### C4. Heisenberg bar complex identified as both coLie AND coSym (contradiction)
- **File**: `free_fields.tex:784` vs `free_fields.tex:2486`
- **Issue**: Line 784 says B(H_k) = coLie(V*[-1]). Line 2486 says B(H_k) = Sym^ch(V*). These are mutually exclusive — coLie is the Koszul dual of Com, while Sym is the Koszul dual of Lie.
- **Impact**: Fundamental algebraic identification of the most basic example is contradictory.
- **Fix**: The correct answer is H! = Sym^ch(V*) (CLAUDE.md verified fact). Fix line 784.

---

## HIGH / MAJOR FINDINGS (28)

### Theory

**H1. False identification kappa=k=c=d for Heisenberg**
- `free_fields.tex:1241`
- For general Heisenberg of dimension d at level k, central charge c = d (not k). The blanket identification kappa=k=c=d is wrong when d != k.

**H2. HH duality shift accounting: 2+1+1=4, not 2**
- `deformation_theory.tex:402-406`
- Proof of thm:main-koszul-hoch claims Verdier shift (2) + desuspension (1) + Serre (1) = total shift 2. But 2+1+1=4. The shift accounting is confused.

**H3. Wrong formula for d_int in deformation complex**
- `deformation_theory.tex:135`
- d_int uses alternating signed sum with hat (simplicial face map pattern), but is labeled "internal differential." Conflates d_int and d_fact.

**H4. HH^1 derivation argument: [alpha_0, alpha(z)] != k*1**
- `deformation_theory.tex:1206`
- Claims ad_{alpha_0} produces the derivation D(alpha) = c*1. But alpha_0 is central in Heisenberg ([alpha_0, alpha_n] = 0 for all n). Conclusion HH^1=0 is correct but the explicit argument is wrong.

**H5. bc/beta-gamma HH verification is circular**
- `deformation_theory.tex:1303-1312`
- Uses HH*(Heisenberg) in place of HH*(bc), justified by "coincides in these degrees." The bc system has 2 generators vs Heisenberg's 1 — unjustified identification.

**H6. N=4 SYM claim is wrong**
- `deformation_theory.tex:996`
- Claims "HH^2 = C^{3(g-1)} gives gauge coupling and theta angles." N=4 SYM is 4d, not a 2d chiral algebra; conformal manifold is 1-dimensional (tau). Formula involves unspecified genus g.

**H7. Degree-2 Hochschild-W factor-of-2 discrepancy**
- `hochschild_cohomology.tex:92` vs `koszul_pair_structure.tex:597`
- W-algebra Hochschild: deg(Theta_i) = h_i = m_i+1 in one file, deg(Theta_i) = 2(m_i+1) in the other. Different contexts (generic vs critical level), but the notation conflates them.

**H8. Cyclic homology notation: HC vs HP**
- `hochschild_cohomology.tex:672`
- cor:cyclic-homology-duality uses HC_* but states it's "periodic cyclic homology" — should be HP_* (2-periodic). Inconsistent with definitions in the same file.

**H9. Chiral Yangian proof proves wrong thing**
- `koszul_pair_structure.tex:1016-1023`
- thm:chiral-yangian claims Yangian arises from KL equivalence (deep Feigin-Frenkel result), but proof only verifies basic chiral algebra axioms. Should be ProvedElsewhere for the KL part.

**H10. BV structure proof gap (linearized QME != full QME)**
- `koszul_pair_structure.tex:1538-1567`
- Proof says d^2=0 "is the linearized QME" — but the full QME has {S,S} interaction term. Defers to Part III but is tagged ProvedHere.

**H11. Yangian theorem computes quadratic dual, doesn't prove Koszulness**
- `chiral_koszul_pairs.tex:490-521`
- thm:yangian-self-dual tagged ProvedHere computes R^perp but never proves the Koszul complex is acyclic (i.e., that the bar spectral sequence degenerates at E_2).

**H12. Completion convergence lemma proof gap**
- `chiral_koszul_pairs.tex:919-950`
- Claims polynomial growth + formal smoothness => Mittag-Leffler condition, but doesn't verify ML (requires eventually stable images of transition maps).

**H13. Tor-independence assertion in monoidal module Koszul duality**
- `chiral_modules.tex:315-325`
- Jump from "concentrated on the diagonal" to "flat over A!" is not justified. Non-trivial homological claim.

**H14. Kac table dual weight numerical errors**
- `chiral_modules.tex:3564-3568`
- Ising dual weights stated as {0, 33/16, 5/2} — correct values are {0, 17/16, 3/2}. Free boson dual values also wrong (sign error from C3).

**H15. PBW spectral sequence misquoted (Whitehead on infinite-dim module)**
- `derived_langlands.tex:183-188`
- Whitehead lemma applied to S*(g[t^-1]t^-1), which is infinite-dimensional. Requires pro-finite-dimensional or weight decomposition argument.

**H16. Propagator symmetry error in E_n chapter**
- `en_koszul_duality.tex:237-242`
- Claims sigma*G = G + i*pi. But d(log(-1)) = 0 (differential of a constant). The correct statement is sigma*G = G.

**H17. B(H_k) bar complex vanishing claim contradicts explicit chain groups**
- `free_fields.tex:3006-3012`
- Claims B^n = 0 for n >= 3, contradicting explicit nonzero chain groups (dim g)^n * (n-1)!.

**H18. E_1 vs E_2 collapse contradiction in KM intro**
- `kac_moody_framework.tex:25`
- Introduction says spectral sequence "collapses at E_1" but body computes nontrivial E_1 differentials (correct collapse is at E_2).

**H19. beta-gamma differential table: 4 entries wrong**
- `beta_gamma.tex:739-756`
- Missing divisor types in the nonzero-differential table.

**H20. W-algebra complementarity formula unproved**
- `w_algebras_framework.tex:2083-2085`
- Formula Q(A) + Q(A!) = 2*rank + 4h^vee*dim stated without proof for general W-algebras.

**H21. Drinfeld associator theorem: propagator identification gap**
- `kontsevich_integral.tex:390-430`
- ProvedHere claim doesn't verify that chiral bar complex propagator agrees with Kontsevich propagator. Key step stated but not proved.

**H22. Growth rate formula: log n instead of n**
- `examples_summary.tex:1109-1111`
- lim (log dim / log n) = dim g should be lim (log dim / n) = log(dim g) for exponential growth. Wrong denominator.

**H23. Degree-2 bar differential "vanishes identically" — false**
- `examples_summary.tex:1093-1101`
- Claims d_2: B^2 -> B^1 vanishes identically. The explicit 3x9 matrix in detailed_computations.tex has rank 3. Dimension H^2 = binom(dim g + 1, 2) is correct, but not because d_2 vanishes.

**H24. Curvature sign error**
- `algebraic_foundations.tex:200`
- States m_0 = k*c (positive k), contradicting m_0 = -k*c at lines 168 and 182 of the same file.

**H25. P_infinity-chiral / Coisson conflation in comparison table**
- `introduction.tex:553`
- Table labels Coisson as "standard analog" of P_infinity-chiral. Per CLAUDE.md critical distinction, these are at different quantization levels. Actively misleading.

**H26. Existence criterion iff proof gap**
- `introduction.tex:1129-1165`
- thm:existence-koszul claimed as "if and only if" but the sufficiency direction (4 conditions => Koszul dual exists) is hand-wavy. Condition (3) (Poincare duality for CH) is non-standard and its role unclear.

**H27. Two \chapter commands in one file**
- `algebraic_foundations.tex:540`
- File produces two chapters from one \include — structural issue.

**H28. Green function G_tau defined inconsistently (simple vs double pole)**
- `heisenberg_eisenstein.tex:101` vs `:641`
- Line 101: G_tau = zeta_tau + ... (simple pole). Line 641: G_tau = wp_tau + ... (double pole). Different functions sharing the same symbol.

---

## MEDIUM FINDINGS (17)

### Structural Issues

**M1. 31 label/environment prefix mismatches**
- 31 `thm:` or `cor:` labels on `\begin{conjecture}` environments (LaTeX renders correctly, but labels are misleading). Full list in cross-ref audit.

**M2. 26 conjectures followed by \begin{proof} blocks**
- Logical contradiction. Most in feynman_diagrams.tex (8), bv_brst.tex (4), free_fields.tex (5), deformation_theory.tex (1). Proof blocks should be replaced with Discussion/Evidence environments.

**M3. 176 ProvedElsewhere claims without \cite{} within 15 lines**
- Many are well-known results, but ~50 lack even an author name.

**M4. 8 duplicate definitions of "Koszul pair"**
- In algebraic_foundations (4 versions), koszul_pair_structure, bar_cobar, chiral_koszul_pairs, poincare_duality. Risk of definitional drift.

**M5. 5 PH-tagged sketch lemmas in bar_cobar_construction**
- Lines 4793-4876: lemmas tagged ProvedHere but explicitly labeled "proof sketch." Full proofs exist in higher_genus.tex but the PH tag here is misleading.

### Formula/Convention Issues

**M6. Modular anomaly "proof" doesn't prove the theorem**
- `free_fields.tex:3322-3340`
- Tagged ProvedHere but the argument doesn't establish the stated result.

**M7. Two incompatible kappa conventions in W-algebra chapter**
- `w_algebras_framework.tex:1564ff`
- Both level and kappa-class meanings coexist without reconciliation.

**M8. Arnold/Totaro confusion in E_n chapter**
- `en_koszul_duality.tex:111-116`
- Theorem says "Arnold presentation, n=1" but writes H*(Conf_k(C;Q)), which is n=2 (real dimension).

**M9. Kontsevich weight table lacks context**
- `computational_tables.tex:9-23`
- Graph types listed without specifying Kontsevich formality context (boundary vs aerial vertices, dimension).

**M10. Lambda convention (quasi-primary vs non-quasi-primary) confusion**
- `computational_tables.tex:137-138`
- W_3 commutator uses non-quasi-primary Lambda but standard references use quasi-primary.

**M11. Cross-reference to appendix that's actually a chapter remark**
- `sign_conventions.tex:340`
- "Start with Appendix \ref{rem:LV-signs}" — but rem:LV-signs is in bar_cobar_construction.tex (a chapter).

**M12. Incomplete classification table (W_{1+inf} missing)**
- `existence_criteria.tex:481` vs `koszul_reference.tex:232`
- existence_criteria.tex omits W_{1+infinity} entirely.

**M13. Convention switch without marker in signs_and_shifts**
- `signs_and_shifts.tex:510-636`
- Switches between unsuspended and desuspended bar complex conventions without clear transition.

**M14. Verlinde formula discrepancy (N_sigma,epsilon^sigma = 2)**
- `minimal_model_examples.tex:208-233`
- Computes wrong answer, acknowledges it, but resolution is incomplete — never identifies root cause.

**M15. W_3 deformation coefficient cross-reference mismatch**
- `deformation_examples.tex:377-384`
- Claims c/(110+2c) with cross-ref to comp:w3-nthproducts, which gives 16/(22+5c). Different quantities.

**M16. Curvature formula ambiguity**
- `derived_langlands.tex:330`
- Curvature m_0 identified with Sugawara central charge c/2, but the curvature comes from the central extension, not directly from Sugawara.

**M17. Admissible level under FF involution: sign issue**
- `koszul_pair_structure.tex:775`
- k' = -k-2h^vee gives k'+h^vee = -(k+h^vee) which is NEGATIVE. Kac-Wakimoto definition requires k+h^vee > 0. Proof glosses over sign by taking absolute values.

---

## MINOR / LOW FINDINGS (~65)

### Selected highlights (full list omitted for brevity):

1. `deformation_theory.tex:1301` — \label inside \ref (harmless but incorrect)
2. `deformation_theory.tex:518` — Boson-fermion correspondence tagged PH, should be PE (Frenkel-Kac-Segal)
3. `physical_origins.tex:58,139` — `thm:` label prefix on conjectures, running text says "Theorem"
4. `existence_criteria.tex:443` — Step 5 referenced but algorithm only defines Steps 1-4
5. `spectral_sequences.tex:45-337` — Grading convention switches (homological -> cohomological, increasing -> decreasing filtration) without explicit transition markers
6. `notation_index.tex:240` — Symbol delta overloaded (3 meanings)
7. `theta_functions.tex:77` — Elliptic bar differential formula without reference or derivation
8. `genus_expansions.tex:73` — x/(2sin(x/2)) called "A-hat genus" — actually Todd genus
9. `examples_summary.tex:518` — Algebraicity corollary statement imprecise (would include transcendental Heisenberg GF)
10. `detailed_computations.tex:19-23` — Arnold relation eta_{31}=eta_{13} justification imprecise
11. `deformation_examples.tex:595-603` — Self-contradictory text: computes c+c'=-4 then c+c'=0 inline
12. `free_fields.tex:3400` — "Modular invariance requires c = 0 mod 24" is wrong
13. `free_fields.tex:2882` — Heisenberg residue formula contradicts triple-pole-zero-residue analysis
14. `w_algebras_deep.tex:913-914` — Claims "irrational levels" for c=0 solutions; actual solutions k=-9/4, -5/3 are rational
15. `sign_conventions.tex:342` — Hardcoded section number "11.3"

---

## RECOMMENDED ACTIONS (Priority Order)

### Immediate (4 critical fixes)
1. **Fix C1**: Rewrite chiral Hochschild d^2=0 proof using Borcherds identity
2. **Fix C2**: Correct Virasoro entry in Koszulness summary table
3. **Fix C3**: Correct sign in eq:kac-table-koszul, recompute all dual weight examples
4. **Fix C4**: Resolve coLie vs coSym contradiction for Heisenberg bar complex

### High Priority (top 10 of 28)
5. Fix shift accounting in HH duality proof (H2)
6. Fix d_int formula (H3)
7. Fix curvature sign (H24)
8. Fix growth rate denominator (H22)
9. Fix degree-2 bar differential vanishing claim (H23)
10. Fix E_1/E_2 collapse statement (H18)
11. Fix Green function symbol overload (H28)
12. Fix kappa=k=c=d identification (H1)
13. Downgrade Yangian "Koszul duality" to "quadratic dual computation" or supply Koszulness proof (H11)
14. Fix propagator symmetry error (H16)

### Structural (batch fixes)
15. Rename 31 `thm:` labels on conjectures to `conj:` prefixes
16. Replace 26 proof blocks on conjectures with Discussion/Evidence
17. Add citations to ~50 PE claims lacking any attribution
18. Consolidate 8 Koszul pair definitions
19. Update CLAUDE.md census and file map

---

## COMPARISON WITH PRIOR AUDITS

| Audit | Session | Findings | Critical | Fixed |
|-------|---------|----------|----------|-------|
| Session 2 | ~95 | 16 | 3 errors | ALL |
| Session 3 | ~100 | 35 | 12 priority | ALL |
| Session 4 | ~105 | 45+ | 17 fixes | ALL |
| **Session 5** | **~130** | **~114** | **4 critical** | **PENDING** |

New findings cluster in: deformation_theory.tex (12), chiral_modules.tex (8), free_fields.tex (7), hochschild_cohomology.tex (5), chiral_koszul_pairs.tex (6). Many are in newer content added since Session 4.

---

---

## THEORY CORE FINDINGS (bar_cobar_construction + higher_genus + configuration_spaces)

### MAJOR (6)

**T1. E_2 collapse proof conflates bar with bar-cobar complex**
- `bar_cobar_construction.tex:~8036-8043`
- E_1^{p,q} vanishing asserted from Koszul property of bar complex, but not explained why this implies vanishing in bar-COBAR spectral sequence. Different objects.

**T2. Fiberwise QI does not imply pushforward QI**
- `bar_cobar_construction.tex:~8117-8118`
- Claims fiberwise QI over M_g implies R*pi_* is QI. Needs proper base change theorem (properness + bounded complexes).

**T3. Mixed term d_0*d_k + d_k*d_0 = 0: OPE pole analysis incomplete**
- `higher_genus.tex:~6693-6699`
- Argument handles simple poles only. Full OPE has higher-order poles; interaction not addressed.

**T4. A-cycle disjointness: geometric vs algebraic**
- `higher_genus.tex:~6707-6710`
- Proof requires gamma_k ∩ gamma_l = emptyset geometrically, but A-cycles with zero algebraic intersection can still intersect geometrically. Must declare geometric disjointness of chosen basis.

**T5. NBC basis recurrence f(n) = n*f(n-1) unjustified**
- `configuration_spaces.tex:~1997-2006`
- Final count |NBC(n)| = n! is correct (Stanley), but the recurrence used in the proof is not established.

**T6. Presentation independence theorem has no proof**
- `configuration_spaces.tex:~2053-2065`
- thm:presentation-independence tagged ProvedHere, but "proof" merely restates the claim.

### MINOR (13)

- B1 (`bar_cobar:~581`): Sign compatibility argument is circular (signs defined to work, then said to work)
- B2 (`bar_cobar:~608`): Residues commute for disjoint divisors (not anticommute); cancellation from signed sum
- B3 (`bar_cobar:~3831`): C_c^infty is LF-space (not Frechet); dual completeness via Montel, not as stated
- B4 (`bar_cobar:~7834`): psi_g target notation: maps to A, not to A_g — genus grading unclear
- B5 (`bar_cobar:~7964`): Associated graded lemma confuses which differentials survive on E_0
- B7 (`bar_cobar:~8096`): Redundant integral + pushforward notation for genus-g bar complex
- C1 (`config_spaces:~1337`): eta_{ji} = eta_{ij} explanation calls antisymmetric log a "symmetry"
- C3 (`config_spaces:~2010`): O(n^3) sparsity bound unclear (per-row? total?)
- C5 (`config_spaces:~2075`): Arnold boundary extension: mixed case (2 in cluster, 1 outside) not handled
- H1 (`higher_genus:~2514`): E_2 quasi-modular transformation sign needs verification
- H7 (`higher_genus:~6741`): C[tau] called "ring of modular forms" — should be C[E_4, E_6]
- H8 (`higher_genus:~6769`): Lemma stated for n>=1 but nonzero case is n=0
- H9 (`higher_genus:~7263`): "Every vertex genus < g" false in separating case (genus-0 vertices allowed)

---

## FULL STATISTICS BY FILE

| File | CRIT | HIGH | MED | LOW | Total |
|------|------|------|-----|-----|-------|
| bar_cobar_construction.tex | 0 | 2 | 0 | 5 | 7 |
| higher_genus.tex | 0 | 4 | 0 | 6 | 10 |
| configuration_spaces.tex | 0 | 2 | 0 | 6 | 8 |
| hochschild_cohomology.tex | 1 | 3 | 0 | 1 | 5 |
| deformation_theory.tex | 0 | 6 | 0 | 6 | 12 |
| chiral_koszul_pairs.tex | 1 | 2 | 0 | 3 | 6 |
| chiral_modules.tex | 1 | 4 | 0 | 4 | 9 |
| algebraic_foundations.tex | 0 | 2 | 0 | 3 | 5 |
| introduction.tex | 0 | 2 | 0 | 4 | 6 |
| free_fields.tex | 1 | 3 | 2 | 3 | 9 |
| kac_moody_framework.tex | 0 | 1 | 0 | 0 | 1 |
| w_algebras_framework.tex | 0 | 1 | 1 | 1 | 3 |
| beta_gamma.tex | 0 | 1 | 0 | 1 | 2 |
| koszul_pair_structure.tex | 0 | 2 | 1 | 1 | 4 |
| poincare_duality_quantum.tex | 0 | 1 | 0 | 2 | 3 |
| en_koszul_duality.tex | 0 | 1 | 1 | 1 | 3 |
| derived_langlands.tex | 0 | 1 | 1 | 1 | 3 |
| kontsevich_integral.tex | 0 | 1 | 0 | 0 | 1 |
| examples_summary.tex | 0 | 2 | 0 | 2 | 4 |
| heisenberg_eisenstein.tex | 0 | 0 | 1 | 0 | 1 |
| detailed_computations.tex | 0 | 0 | 1 | 3 | 4 |
| minimal_model_examples.tex | 0 | 0 | 1 | 0 | 1 |
| deformation_examples.tex | 0 | 0 | 1 | 1 | 2 |
| genus_expansions.tex | 0 | 0 | 0 | 1 | 1 |
| feynman_diagrams.tex | 0 | 1 | 0 | 1 | 2 |
| bv_brst.tex | 0 | 1 | 0 | 1 | 2 |
| physical_origins.tex | 0 | 0 | 1 | 0 | 1 |
| concordance.tex | 0 | 0 | 0 | 0 | 0 |
| Appendices (14 files) | 0 | 0 | 5 | 12 | 17 |
| Cross-ref/structural | 0 | 0 | 6 | 2 | 8 |
| **TOTAL** | **4** | **34** | **17** | **78** | **133** |

---

---
---

# PHASE 2: Infrastructure, Code, Proof Chains, Bibliography, Physics

## COMPUTE ENGINE (17 findings)

### CRITICAL (3)

**CE1. Heisenberg kappa = k/2 (should be k)**
- `compute/lib/genus_bridge.py:63`, `compute/lib/cross_algebra.py:40`
- Two modules define kappa(Heisenberg) = k/2. Correct value is k (the level itself). F_1(H_k) = k/24 requires kappa=k; k/2 gives wrong F_1 = k/48. Tests pass tautologically.

**CE2. OS algebra intermediate dimensions wrong**
- `compute/lib/bar_comparison.py:71-78`
- `os_dim(n, degree)` uses falling factorial instead of elementary symmetric polynomials in {1,...,n-1}. os_dim(4,1)=3 (wrong, should be 6), os_dim(4,2)=6 (wrong, should be 11). Top-degree and degree-0 are correct, so tests don't catch it.

**CE3. sl3 complementarity sum = 48 (should be 16)**
- `compute/lib/bar_comparison.py:149`
- c(k) + c(k') = 2*dim(sl3) = 16, not 48. The 48 matches no known formula. genus_bridge.py has the correct value.

### HIGH (3)

**CE4. Free fermion generator count inconsistency**
- `cross_algebra.py:47` (2 generators) vs `bar_complex.py:172` (1 generator)
- Describe different mathematical objects. Bar dimensions use the 1-generator version.

**CE5. Free fermion Koszul dual wrong in registry**
- `cross_algebra.py:54`: lists F! = Sym^ch(V*). Correct: F! = beta-gamma.

**CE6. sympy.Rational shadowed by float division**
- `w3_bar_extended.py:754`: `def Rational(a, b): return a / b` shadows sympy.Rational.

### MEDIUM (6)

- CE7: Lee-Yang docstring says M(5,3) c=-3/5, correct is M(5,2) c=-22/5
- CE8: G2 root length docstring uses different normalization than code
- CE9: Floating-point SVD for exact integer rank computation (koszul_hilbert, os_algebra)
- CE10: Tautological verify_*() functions check hardcoded values against themselves
- CE11: kappa_heisenberg() crashes on symbolic input
- CE12: Heisenberg curvature m_0 = k/2 (should be k) in cross_algebra.py

### LOW (5)

- CE13: Dead code in km_complementarity_sum()
- CE14: W3 Borcherds mode offsets hardcoded
- CE15: sys.path manipulation in all scripts
- CE16: Virasoro OPE table omits quartic pole (intentional but inconsistent with cross_algebra.py)
- CE17: os_total_dim(n) = n! (actually correct despite os_dim being wrong)

---

## MAIN.TEX PREAMBLE & MACROS (13 findings)

### HIGH (2)

**PM1. Geometry options silently dead**
- `main.tex:429-435`: Second `\usepackage{geometry}[...]` has options AFTER closing brace — LaTeX ignores them. Intended margins (1.2in top/bottom, 1.25in sides) are NOT applied. Document uses only `margin=1in` from line 96.
- Fix: Use `\geometry{top=1.2in, bottom=1.2in, left=1.25in, right=1.25in, footskip=0.5in}`

**PM2. Missing xy package causes compilation error**
- `chapters/theory/derived_langlands.tex:633` uses `\xymatrix` but `xy` is never loaded.
- Fix: Rewrite diagram using tikz-cd (already loaded) or add `\usepackage[all]{xy}`

### MEDIUM (4)

- PM3: 4 duplicate macro pairs (chirbar/barBch, chircobar/Omegach, MC/MCeq)
- PM4: 17 unused macros defined but never used in any chapter
- PM5: \C, \Z, \R override built-in accent commands
- PM6: Macros defined after \begin{document} (fragile, non-standard)

### LOW (4)

- PM7: Hardcoded chapter numbers in 4 locations (should be \ref)
- PM8: \coAlg (roman) vs \CoAlg (sans-serif) — ambiguous
- PM9: \oti and \otim both expand to \otimes
- PM10: No \newcommand violations in chapters (CLEAN)

---

## PROOF CHAIN INTEGRITY — ALL CLEAN

All three main theorems have complete, self-contained proof chains:

| Theorem | Label | Depth | Gaps | Circles | Conjectured deps |
|---------|-------|-------|------|---------|-----------------|
| A (Bar-Cobar Duality) | thm:bar-cobar-isomorphism-main | 4 | 0 | 0 | 0 |
| B (Inversion) | thm:higher-genus-inversion | 5 | 0 | 0 | 0 |
| C (Complementarity) | thm:quantum-complementarity-main | 6 | 0 | 0 | 0 |

Dependency structure: B depends on A; C is independent of both A and B. No physics results contaminate pure math proofs. Cross-reference between thm:bar-cobar-inversion-qi and thm:higher-genus-inversion is informational, not circular.

---

## BIBLIOGRAPHY (95+ findings)

### CRITICAL (2)

**BIB1. Broken citation: BLPW16**
- `yangians.tex:753` cites BLPW16 (Braden-Licata-Proudfoot-Webster). No bib entry exists.

**BIB2. Broken citation: GG11**
- `w_algebras_deep.tex:498` cites GG11. Entry exists as `Gaberdiel-Gopakumar` but not as `GG11`.

### HIGH (21+)

**BIB3. 15+ full duplicate entry sets**
- Kontsevich DQ: 4 copies (Kon03, kontsevich-deformation, Kontsevich99, Kontsevich-formality)
- Arnold: 3 copies. BPZ: 3 copies. GLZ: 3 copies. CG: 3 copies.
- Feigin-Frenkel, Lurie HA, Lurie HTT, FBZ, Costello-Li, FM94: 2 copies each.

**BIB4. 6 key-name date mismatches**
- BW93 → paper from 1983. GLZ21 → published 2024. Lur17 → book from 2009.

### MEDIUM (26)

**BIB5. 26 alias stubs render "Alias key for X" as visible bibliography text**
- e.g., `\bibitem{LV12} Alias key for LV.` renders literally in PDF.

### LOW (80+)

- 74 uncited bibliography entries (26% of total)
- 6 author name inconsistencies (Feigin, E. Frenkel, I. Frenkel, Kontsevich, Arnold, Lurie)
- costello-factorization key points to Renormalization book (wrong title)

---

## TEX-CODE FORMULA CONSISTENCY — ALL CLEAN

**Zero discrepancies** across all five categories:
- Bar cohomology dimensions (10 algebras): ALL MATCH
- Generating functions (6 GFs): ALL MATCH
- Central charge formulas (7 formulas): ALL MATCH
- Genus expansion coefficients (12 values): ALL MATCH
- Lie algebra data (10 algebras): ALL MATCH

---

## DEEP FORMULA SPOT-CHECKS (16 formulas)

| Formula | Verdict |
|---------|---------|
| Lambda = :TT: - (3/10) d^2 T | CORRECT |
| W(z)W(w) leading c/3 | CORRECT |
| Lambda coefficient 16/(22+5c) | CORRECT |
| Verlinde formula | CORRECT |
| Ising S-matrix | CORRECT |
| N_{sigma,sigma}^I = 1 | CORRECT |
| FP g=1: 1/24 | CORRECT |
| FP g=2: 7/5760 | CORRECT (manuscript correct) |
| Riordan values 1,0,1,1,3,6,15,36 | CORRECT |
| Riordan GF (manuscript) | CORRECT |
| **Riordan GF (CLAUDE.md)** | **WRONG** — denominator 2x should be 2x(1+x) |
| A-infinity sign (-1)^{rs+t} | CORRECT |
| Cohomological |d|=+1 | CORRECT |
| lambda_{g-1}^2 = 2 lambda_g lambda_{g-2} | CORRECT |
| Mumford from c(E)*c(E^v)=1 | CORRECT |

**One error in CLAUDE.md**: Riordan GF stated as `(1+x-sqrt((1-3x)(1+x)))/(2x)` — missing `(1+x)` in denominator. This generates Motzkin numbers, not Riordan. Correct: `(1+x-sqrt(1-2x-3x^2))/(2x(1+x))`.

---

## PHYSICS CONJECTURES ASSESSMENT (35 distinct claims)

### Upgradeable (3)
1. **Gaiotto-Witten S-duality (principal, simply-laced)**: IS Feigin-Frenkel duality → ProvedElsewhere
2. **Gaiotto-Witten (hook-type)**: IS Arakawa-van Ekeren → ProvedElsewhere
3. **W-algebra integrability (classical)**: IS Drinfeld-Sokolov → ProvedElsewhere (quantum A-inf remains Conjectured)

### Should Split (3)
- Gaiotto-Witten: principal proved, general conjectured
- W-algebra bar complex (HT): item (1) proved, items (2-3) conjectured
- Topological open-closed: math proved, physics interpretation conjectured

### Mislabeled as "Physics" (5 are pure math)
- W-algebra Koszulness at admissible levels
- E_n Koszul duality on n-manifolds
- Virasoro ↔ W_infinity, W_N ↔ Y(gl_N), Super-Vir ↔ Super-W_infinity

### Imprecisely Stated (3 severe)
- Modular anomaly formula: dim H*_BRST is infinite, formula meaningless without regularization
- Bulk reconstruction: Omega^n(B(O_CFT)) is a vector space, not a function of (z,z-bar)
- Entanglement/Koszul complexity: "no precise mathematical formulation known" → downgrade to Heuristic

### Physics in Math Proofs: NONE FOUND

---

## REPO STRUCTURE & BUILD (14 findings)

### HIGH (1)
- CLAUDE.md census stale by +55 claims

### MEDIUM (7)
- 3 compiled .tex files untracked in git
- No requirements.txt for compute venv
- 15 untracked notes files (stale prompts)
- build.sh missing buf_size=1000000
- Convergence check misses "Label(s) may have changed"
- 11 dead scratch scripts tracked
- 16 untracked compute files

### LOW (6)
- geometry package loaded twice, pass count mismatch, pkill guard missing, etc.

---

# GRAND TOTAL (Phase 1 + Phase 2)

| Category | Phase 1 | Phase 2 | Total |
|----------|---------|---------|-------|
| CRITICAL | 4 | 8 | **12** |
| HIGH/MAJOR | 34 | 29 | **63** |
| MEDIUM | 17 | 43 | **60** |
| LOW/MINOR | 78 | 21 | **99** |
| **Findings** | **133** | **101** | **234** |

### Top 12 Critical Fixes Required

| # | Finding | Location |
|---|---------|----------|
| 1 | Hochschild d^2=0 uses false strict associativity | hochschild_cohomology.tex:380 |
| 2 | Virasoro "No" in Koszul table contradicts own theorem | chiral_koszul_pairs.tex:2307 |
| 3 | Sign error in Kac table duality formula | chiral_modules.tex:3553 |
| 4 | Heisenberg bar = coLie AND coSym contradiction | free_fields.tex:784 vs 2486 |
| 5 | Heisenberg kappa = k/2 (should be k) in code | genus_bridge.py:63, cross_algebra.py:40 |
| 6 | OS algebra dimensions wrong (falling factorial) | bar_comparison.py:71 |
| 7 | sl3 complementarity = 48 (should be 16) | bar_comparison.py:149 |
| 8 | Broken citation BLPW16 | yangians.tex:753 |
| 9 | Broken citation GG11 | w_algebras_deep.tex:498 |
| 10 | Geometry options silently dead | main.tex:429 |
| 11 | Missing xy package (compilation error) | derived_langlands.tex:633 |
| 12 | CLAUDE.md Riordan GF wrong denominator | CLAUDE.md |

*Generated by 18-agent parallel adversarial audit (Phase 1: 10 agents, Phase 2: 8 agents), March 6, 2026.*
*All agents completed. Full findings catalogued above.*
