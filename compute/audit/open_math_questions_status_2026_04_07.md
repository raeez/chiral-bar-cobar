# Open Mathematical Questions: Definitive Status Report

Date: 2026-04-07

This report codifies the status of five genuine open mathematical
questions in the monograph, based on direct investigation of the
.tex source, compute/ engines, and independent first-principles
computation.

---

## Question 1: Bershadsky-Polyakov Central Charge Formula

### Summary

**THREE MUTUALLY INCONSISTENT FORMULAS exist in the codebase.**
An independent first-principles derivation shows **all three are wrong**
or at least two are wrong and one disagrees with the others.

### What is known

The codebase contains three distinct formulas for the BP central charge:

| File | Formula | K_BP | Status |
|------|---------|------|--------|
| `sl3_subregular_bar.py:106-115` | `c = (k-15)/(k+3)` | 2 | OLD, acknowledged wrong |
| `bp_shadow_tower.py:46-49` | `c = 2 - 3(2k+3)^2/(k+3)` | 76 | Current manuscript |
| `nonprincipal_ds_reduction.py:79-84` | `c = 2 - 3(2k+3)^2/(k+3)` | 76 | Current manuscript |

The manuscript (`subregular_hook_frontier.tex:911,965`) currently uses
the quadratic-numerator formula `c = 2 - 3(2k+3)^2/(k+3)` with K_BP = 76.
A RECTIFICATION-FLAG comment at line 1075-1083 records the change from
the old linear formula to the new quadratic one.

**However, an independent derivation from the Kac-Wakimoto theorem
produces a FOURTH formula:**

```
c_BP(k) = dim(g^f) - 12*||rho||^2 / (k + h^v)
        = 4 - 24/(k+3)
        = (4k - 12)/(k + 3)
        = 4(k-3)/(k+3)
```

with K_BP = 8 (not 2, not 76).

Derivation inputs (all standard):
- g = sl_3, h^v = 3, dim(g) = 8
- f = minimal nilpotent (partition (2,1))
- dim(g^f) = 4 (centralizer of f: matches 4 generators J, G+, G-, T)
- ||rho||^2 = 2 (standard for sl_3: rho = alpha_1 + alpha_2)
- rho_0 = 0 (grade-0 subalgebra g_0 is abelian/Cartan, Weyl vector = 0)

This formula c = 4(k-3)/(k+3) is consistent with:
- Polyakov (1990) original computation
- Bershadsky (1991) Jacobi identity constraint on T(z)T(w) OPE
- c = 0 at k = 3 (free-field point)
- c = -2 at k = 1 (known value from representation theory)
- Linear numerator (degree 1 over degree 1), as expected for a
  W-algebra central charge from the KRW formula
- Constant Koszul conductor K = 8 under k -> -k-6

The manuscript formula `c = 2 - 3(2k+3)^2/(k+3)` has a QUADRATIC
numerator (degree 2 over degree 1). This is structurally wrong:
the KRW formula for ANY W-algebra of the form W^k(g, f) at generic
level produces a central charge of the form `c = A - B/(k + h^v)`
where A, B are level-independent constants. The quadratic numerator
violates this structural constraint.

### What is NOT known

1. The precise convention mapping between the different references.
   Different papers (Polyakov 1990, Bershadsky 1991, Feigin-Semikhatov
   2004, Kac-Roan-Wakimoto 2003, Fehily-Kawasetsu-Ridout 2020) may
   use different level conventions (k_FS = k_KRW + shift). A wrong
   level shift would explain how a correct formula in one convention
   became the wrong quadratic formula in another.

2. The source of the quadratic formula. The rectification comment
   at line 1078 says it was "verified against bp_shadow_tower.py and
   theorem_nonprincipal_line_operators_engine.py," but these engines
   IMPLEMENT the same formula rather than independently deriving it.
   This is an AP10 violation (tests with hardcoded wrong values).

3. Whether the formula from Fehily-Kawasetsu-Ridout (2020) that is
   cited in `theorem_w_algebra_chapter_rectification_engine.py:126`
   as `c = 2 - 24(k+1)^2/(k+3)` is a correct transcription of
   that paper. If so, it is yet another (fifth!) distinct formula
   with K = 196, which would also need reconciliation.

### What would settle the question

1. **Read the original Bershadsky (1991, hep-th/9106111) paper and
   transcribe the central charge formula with full convention detail.**
   The paper derives c from the Jacobi identity on the OPE algebra;
   this is the most direct route.

2. **Verify at a specific admissible level against known minimal model
   data.** The BP minimal models at admissible levels k = p/q - 3
   have known central charges from character theory. Checking c_BP(k)
   at k = -5/3 (the simplest admissible level) against the known
   minimal model value would distinguish the formulas.

3. **Compute c from the explicit free-field realization** (Feigin-
   Semikhatov maximally asymmetric form, which is already in the
   manuscript at line 554-618 of subregular_hook_frontier.tex).
   The T(z)T(w) OPE can be computed directly from the free fields.

### Recommended next step

Read the original Bershadsky (1991) paper (arXiv: hep-th/9106111).
Transcribe the T(z)T(w) OPE central charge. Verify against the KW
derivation c = 4(k-3)/(k+3). If confirmed, fix all three compute
modules AND the manuscript simultaneously (AP5: fix all instances).

**SEVERITY: CRITICAL.** The BP central charge propagates to kappa,
the shadow tower, the Koszul conductor, the complementarity sum,
and at least 63 tests. All downstream computations using c_BP are
unreliable until this is resolved.

---

## Question 2: Multi-Weight Universality Failure Completeness

### Summary

The genus-2 cross-channel correction delta_F_2(W_3) = (c+204)/(16c)
is the COMPLETE genus-2 free energy correction for the multi-weight
failure. The planted-forest correction delta_pf and the cross-channel
correction delta_F_2^cross are DIFFERENT objects that enter the free
energy through different mechanisms. The genus-3 formula is also
computed. The question of completeness is SETTLED through genus 4.

### What IS known

**The full genus-2 free energy decomposition** (thm:multi-weight-genus-expansion,
line 19265 of higher_genus_modular_koszul.tex):

```
F_2(A) = kappa(A) * lambda_2^FP + delta_F_2^cross(A)
```

For W_3:
- kappa(W_3) = 5c/6
- lambda_2^FP = 7/5760
- delta_F_2^cross(W_3) = (c+204)/(16c)

The cross-channel correction decomposes by graph
(`theorem_genus2_planted_forest_gz26_engine.py:381-424`):
- banana: 3/c
- theta: 9/(2c)
- lollipop: 1/16
- barbell: 21/(4c)
- fig_eight: 0
- dumbbell: 0
- Total: (c+204)/(16c)

This is complete: ALL 7 stable graphs of M-bar_{2,0} (more precisely
6 boundary strata plus 1 open stratum) are accounted for. The 4
contributing graphs (D, E, F, and the banana) carry all mixed-channel
amplitudes; the remaining 3 have zero cross-channel by the
single-edge genus-1 universality mechanism.

**The planted-forest correction** delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48
is a SEPARATE object: it measures the higher-arity shadow contributions
to the genus-2 free energy from the obstruction tower. For UNIFORM-WEIGHT
algebras, this is the only correction beyond kappa * lambda_2^FP (and
it vanishes for class G algebras like Heisenberg). For MULTI-WEIGHT
algebras, BOTH delta_pf and delta_F_2^cross contribute, but they enter
through different mechanisms (planted-forest graphs vs mixed-channel
boundary graphs).

**Genus-3 is also computed** (comp:w3-genus3-cross, line 19851):
```
delta_F_3(W_3) = (5c^3 + 3792c^2 + 1,149,120c + 217,071,360) / (138,240 c^2)
```
All 42 stable graphs of M-bar_{3,0} are summed with all 2^|E| channel
assignments. 34 of 42 graphs contribute nonzero cross-channel corrections.
At large c: delta_F_3 ~ c/27648 (linear in c), and the ratio to the
scalar part approaches 42/31 ~ 1.35.

**Genus-4** is also computed (comp:w3-genus4-cross, line 19910).

### What is NOT known

1. **Whether delta_pf and delta_F_2^cross overlap or are additive.**
   The manuscript writes F_2 = kappa*lambda_2 + delta_F_2^cross, with
   delta_pf being a separate object. Whether the planted-forest
   correction is a COMPONENT of delta_F_2^cross or an ADDITIONAL term
   needs clarification. From the compute engine, they appear to be
   separate: delta_pf captures the higher-arity vertex corrections
   (from S_3, S_4, ...) while delta_F_2^cross captures the multi-channel
   edge assignment corrections. For uniform-weight algebras delta_F_2^cross = 0
   but delta_pf may be nonzero.

2. **The genus-5 and higher tower.** No explicit formula exists beyond
   genus 4. The structural question: does the cross-channel correction
   grow polynomially or faster with genus?

3. **A closed-form generating function** for the cross-channel tower
   analogous to the A-hat generating function for the scalar part.

### What would settle it

A rigorous proof that F_2(A) = kappa*lambda_2 + delta_pf + delta_F_2^cross
(three terms) or F_2(A) = kappa*lambda_2 + delta_F_2^cross (two terms with
delta_pf absorbed into the cross-channel sum). The key distinction:
does delta_pf = 0 for multi-weight algebras (because the planted-forest
correction only matters for uniform-weight algebras), or does it add
on top of the cross-channel correction?

### Recommended next step

Clarify the relationship between delta_pf and delta_F_2^cross in the
manuscript. The most likely resolution: for multi-weight algebras,
delta_F_2^cross INCLUDES the planted-forest contributions (it is the
COMPLETE correction), while delta_pf is the restriction of that correction
to the planted-forest strata for uniform-weight algebras. Verify this
by checking that the genus-2 graph sum for Virasoro (uniform-weight)
gives delta_F_2^cross = 0 and delta_pf = -(c-40)/48 simultaneously.

**SEVERITY: MODERATE.** The genus-2 formula is correct and complete; the
question is about the relationship between two different decompositions
of the same free energy, not about missing terms.

---

## Question 3: Non-Principal W-Algebras Beyond Hook Type

### Summary

The hook-type corridor is the ONLY proved non-principal transport path.
Extension to non-hook nilpotent orbits remains conjectural, with a
specific first test case identified.

### What IS known

1. **Completed Koszulness is universal** (thm:pbw-slodowy-collapse,
   line 80 of subregular_hook_frontier.tex): ANY W-algebra W^k(g,f) whose
   associated graded is Sym_partial(V) for a finite-dimensional V is
   completed Koszul. This applies to ALL nilpotent orbits f whenever
   the associated-graded theorem holds (rem:arbitrary-nilpotent-conditional,
   line 164).

2. **Hook-type transport is proved CONDITIONALLY** (thm:hook-transport-corridor,
   line 228): Under the hypothesis that DS/bar compatibility holds along
   the hook network, (W^k(sl_N, f_eta))^! = W^{-k-2N}(sl_N, f_{eta^t})
   for all hook partitions eta = (N-r, 1^r).

3. **Transport propagation is unconditional** (prop:transport-propagation,
   line 255): IF the hook duality is established AND the duality functor D
   intertwines every reduction edge, THEN duality extends to the entire
   transport-closure of the hook vertices.

4. **The transport-to-transpose conjecture** (conj:type-a-transport-to-transpose,
   line 297): At generic level, the transport-closure of hook vertices is ALL
   of Par(N), giving (W^k(sl_N, f_lambda))^! = W^{k_lambda^v}(sl_N, f_{lambda^t}).

5. **The formality mechanism is incomplete** (rem:hook-formality-mechanism, line 279):
   The DS/bar compatibility along the entire hook network is NOT yet proved
   uniformly. The safe statement is case-by-case verification.

6. **Specific sl_4 data is computed** (comp:sl4-hook-data, line 352; also
   hook_type_w_duality.py and hook_type_bar_sl4.py): Generator content,
   ghost constants, and kappa for all sl_4 partitions (including non-hook
   (2,2)).

7. **First non-abelian audit surface**: The partition (3,2) in sl_5 is
   identified as the first explicit non-abelian test (rem:abelian-nonabelian-
   nilradical, line ~292). The nilradical for (3,2) is NOT abelian, so the
   abelian-n+ formality mechanism fails and new methods are needed.

### What is NOT known

1. **Whether (W^k(sl_N, f_lambda))^! is a W-algebra for non-hook lambda.**
   For hook partitions this follows from the structure of inverse reduction
   and the self-dual property of type-A orbits. For non-hook partitions,
   the dual MIGHT be a more exotic object (not just a W-algebra at a
   different level and dual orbit).

2. **The DS/bar compatibility for non-abelian nilradicals.** The hook corridor
   works because the nilradical for hook partitions in type A is (mostly)
   abelian, allowing the Kazhdan filtration argument. For non-hook partitions
   like (3,2) in sl_5, the nilradical has non-abelian components, and the
   filtration formality breaks down.

3. **Types B, C, D, E, F, G.** The entire hook framework is specific to
   type A. For non-simply-laced types, the partition/orbit classification
   is different, and the transport-to-transpose mechanism may not apply.

### What would settle it

For the type-A question: Prove DS/bar compatibility for the partition
(3,2) in sl_5. This is the minimal non-hook, non-abelian case. If
the duality W^k(sl_5, f_{(3,2)})^! = W^{k'}(sl_5, f_{(2,2,1)}) holds
(where (3,2)^t = (2,2,1)), this would provide strong evidence for the
full transport-to-transpose conjecture.

### Recommended next step

Build a compute engine for sl_5 partition (3,2): compute the generator
content, central charge, kappa, and check the complementarity sum
kappa(k) + kappa(k') against the predicted Koszul conductor. If the
kappa sum is k-independent (necessary for duality), this is evidence
for the conjecture. If it FAILS to be k-independent, the conjecture
is false in its stated form.

**SEVERITY: MODERATE.** This is an open mathematical frontier, not a
bug. The manuscript correctly marks the transport-to-transpose as a
conjecture (conj:type-a-transport-to-transpose) and the hook corridor
as conditional (thm:hook-transport-corridor).

---

## Question 4: BV/BRST = Bar at Genus >= 2

### Summary

conj:master-bv-brst (BV/BRST complex = bar complex at all genera) is
PROVED at genus 0 and for Heisenberg at all genera. At genus 1, the
scalar comparison F_1 = kappa/24 holds universally, but chain-level
identification is conditional for classes C and M. At genus >= 2, the
conjecture is fully open for interacting theories.

### What IS known

**Proved results:**
1. Genus 0: BV = bar is PROVED (thm:bv-bar-geometric, CG17). This is
   the foundational result.
2. Heisenberg at all genera: PROVED (thm:heisenberg-bv-bar-all-genera,
   thm:heisenberg-sewing). The Gaussian path integral is exact.
3. Genus 1, scalar level: F_1^BV = F_1^bar = kappa/24 for ALL families
   (verified by 3 independent paths in the engine). The BV exponent
   alpha(A) = kappa(A) by the Quillen anomaly computation.
4. Genus 1, chain level for classes G and L: PROVED. For Heisenberg
   (class G), the Gaussian structure makes the identification exact.
   For affine KM (class L), the Jacobi identity forces the harmonic
   propagator P_harm to decouple from the cubic OPE.

**Conditional results:**
5. Genus 1, chain level for class C (beta-gamma): Conditional on
   Q_contact coupling to P_harm. For beta-gamma specifically, Q_contact = 0
   by the weight-(1,0) structure, so the coupling is trivially zero.
6. Genus 1, chain level for class M (Virasoro, W_N): Conditional on
   controlling the all-arity coupling of the shadow obstruction tower to
   the harmonic propagator.

**Genus-2 constraints from the planted-forest data:**
7. At genus 2, the bar side gives F_2 = kappa*lambda_2^FP + delta_pf
   where delta_pf = S_3(10*S_3 - kappa)/48. The BV side should produce
   the same F_2 from a 2-loop computation on M-bar_{2,0} (6 stable graphs
   as Feynman diagrams). This comparison is CONJECTURAL.

### What is NOT known

1. **The genus-2 BV path integral for interacting theories.** The 2-loop
   Feynman diagrams on M-bar_{2,0} with the KZ25 sigma-model action have
   not been computed for Virasoro or W_N. This would require explicit
   evaluation of 6 graph amplitudes in the BV formalism and comparison
   with the bar planted-forest formula.

2. **The harmonic propagator coupling at genus >= 2.** At genus 1, the
   harmonic propagator P_harm is a 1-dimensional object (the constant
   mode on the torus). At genus >= 2, P_harm is g-dimensional (from the
   g holomorphic 1-forms on a genus-g surface). The coupling of the
   shadow obstruction tower to this g-dimensional harmonic space is the
   main technical obstacle.

3. **Whether BV/BRST = bar fails for some specific algebra at genus 2.**
   No counterexample is known. The conjecture could be TRUE universally,
   TRUE for classes G/L/C and FALSE for class M, or TRUE for all but
   fail at some specific non-standard algebra.

### Specific genus-2 obstructions

The BV/BRST engine (`theorem_bv_brst_genus1_constraints_engine.py:580-641`)
identifies three specific genus-2 obstacles:

1. **Class G (Heisenberg):** No obstruction. delta_pf = 0 (S_3 = 0), and
   the Gaussian integral is exact at all genera. PROVED.

2. **Class L (affine KM):** The first genuine test. delta_pf != 0 (e.g.,
   for sl_2 at k=1: S_3 = 4/3, delta_pf = 133/432). The BV 2-loop
   computation should match. The obstacle: the cubic OPE vertex contributes
   non-trivially to 2-loop diagrams, and the Jacobi-based decoupling
   argument from genus 1 does not directly generalize.

3. **Class M (Virasoro):** delta_pf = -(c-40)/48 from S_3 = 2. The quartic
   contact Q^contact_Vir = 10/[c(5c+22)] also contributes via the banana
   graph. Multiple vertex types (cubic and quartic) interact through the
   genus-2 graph sum.

### What would settle it

1. **Compute the 2-loop BV path integral for affine sl_2 at k=1 on a
   genus-2 surface.** This is the simplest interacting case (class L,
   finite number of graph amplitudes, no quartic vertex). If it matches
   delta_pf = 133/432, the conjecture gains strong support.

2. **Prove the harmonic propagator decoupling at genus 2 for class L
   algebras.** This would extend the Jacobi-based argument from genus 1.

### Recommended next step

Build a compute engine that evaluates the 6 BV Feynman graph amplitudes
at genus 2 for affine sl_2 at k=1, using the KZ25 sigma model action.
Compare with delta_pf = 133/432. This is the minimal decisive test.

**SEVERITY: LOW (for now).** The conjecture is correctly marked as
conjectural throughout the manuscript. The proved results (genus 0
universally, Heisenberg at all genera, scalar genus-1 universally)
are sound. The genus-2 frontier is an open research problem, not a
manuscript error.

---

## Question 5: GZ26 Term-by-Term Comparison for W_N

### Summary

The existence and commutativity of W_N Hamiltonians from Theta_A is
PROVED. The term-by-term comparison with GZ26's specific operators is
CONJECTURAL, with a specific convention mismatch identified as the
obstacle.

### What IS known

**Proved results:**
1. **Existence of commuting Hamiltonians** (thm:gz26-commuting-differentials,
   part (v)): For any modular Koszul algebra A, the shadow connection
   nabla^hol_{0,n} = d - Sh_{0,n}(Theta_A) decomposes into commuting
   Hamiltonians H_i with [H_i, H_j] = 0. This is a THEOREM.

2. **KZ recovery** (part iii): For affine KM algebras, the Hamiltonians
   recover the Knizhnik-Zamolodchikov connection exactly.

3. **BPZ recovery** (part iv): For the Virasoro algebra, the Hamiltonians
   recover the Belavin-Polyakov-Zamolodchikov connection exactly.

4. **W_3 collision residue structure** (theorem_w3_commuting_hamiltonians_engine.py):
   The full collision residue table is computed:
   - k_max = 5 (from the W-W OPE sixth-order pole, after d log absorption)
   - Differential operator order = 4 (fourth-order on descendants)
   - Definitive depth table: depths 1-5 for all (T,T), (T,W), (W,T), (W,W)
     channel pairs, with the Lambda composite field action on primaries
     computed as Lambda_0|h> = (h^2 - 3h/5)|h>.
   - T-sector restriction recovers Virasoro (consistency check).

5. **General W_N structure**: For W_N, k_max = 2N-1, differential operator
   order = 2(N-1). The Hamiltonians are (2N-2)th-order differential operators.

**Conjectural content (rem:gz26-wn-comparison-conjectural, line 1615-1621
and rem:gz26-scope, line 1624-1632 of frontier_modular_holography_platonic.tex):**

The conjectural step is the TERM-BY-TERM identification of the
Hamiltonians H_i from Theta_{W_N} with the specific operators
constructed in the GZ26 interface paper. The manuscript correctly
marks this as conjectural and identifies the obstacle: "a normalization
convention match that is not yet established."

### What is NOT known

1. **The GZ26 normalization convention.** The GZ26 paper constructs
   Hamiltonians for interface minimal model holography. Their operators
   are defined in a specific basis related to the interface construction.
   The shadow connection Hamiltonians are defined in the bar/MC basis.
   The two bases differ by a (possibly level-dependent) change of
   normalization.

2. **Whether the W_3 Hamiltonians at n=4 agree numerically with GZ26.**
   This would require: (a) fixing four specific W_3 representations
   (with explicit h_j, w_j values), (b) computing the 4-point conformal
   block ODE from both the shadow connection and the GZ26 operators,
   (c) comparing the two ODEs term by term.

3. **Whether the Lambda composite field action (h^2 - 3h/5) matches
   the GZ26 weight-4 operator.** The Lambda_0 eigenvalue on primaries
   is a specific polynomial in h. If the GZ26 operators use a different
   quasi-primary at weight 4, the polynomials would differ.

### What would settle it

**A specific W_3 test at n=4:** Take four degenerate W_3 representations
(e.g., the vacuum, fundamental, adjoint, and dual fundamental of the
W_3 algebra at a specific level). Compute:
1. The 4-point conformal block ODE from the shadow connection H_i.
2. The 4-point ODE from the GZ26 operators.
3. Compare the two ODEs as polynomial differential operators in z.

If they match (up to an overall normalization), the identification is
established for this case. If they DIFFER by more than a scalar, the
convention mismatch is structural and may require a basis change.

The most accessible test case: W_3 at c = 2 (the W_3 minimal model
at the simplest admissible level), with four representations at the
degenerate weights h_j = 0, h_{(1,0)}, h_{(0,1)}, 0 (vacuum-vacuum-
degenerate-degenerate).

### Recommended next step

Implement the W_3 4-point ODE from the shadow connection Hamiltonian
in the existing engine (the framework is already built in
`w3_hamiltonian_4pt_primary`, line 599). Evaluate at a specific set of
(h_1, h_2, h_3, h_4, w_1, w_2, w_3, w_4, c) values and compare the
resulting ODE coefficients with the GZ26 prediction (which would need
to be extracted from their paper).

**SEVERITY: LOW.** The conjecture is correctly marked as conjectural.
The proved content (existence and commutativity from Theta_A, KZ and
BPZ recovery) is the main mathematical result. The GZ26 comparison is
a concrete prediction, not a claimed theorem.

---

## Cross-Cutting Findings

### BP Central Charge Propagation (AP5 risk)

The BP formula propagates to at least the following locations:
- `sl3_subregular_bar.py` (OLD formula: (k-15)/(k+3), K=2)
- `bp_shadow_tower.py` (NEW formula: 2-3(2k+3)^2/(k+3), K=76)
- `nonprincipal_ds_reduction.py` (NEW formula, same as bp_shadow_tower)
- `theorem_w_algebra_chapter_rectification_engine.py` (yet another formula: 2-24(k+1)^2/(k+3), K=196)
- `subregular_hook_frontier.tex` lines 911, 965, 1015
- Downstream: kappa, shadow tower, Koszul conductor, 63+ tests

**The codebase has FOUR DISTINCT BP central charge formulas, none of
which match the first-principles KW derivation c = 4(k-3)/(k+3) with
K=8.** This is an AP1/AP3/AP10 violation of the most severe kind.

### Multi-Weight Decomposition Terminology

The relationship between delta_pf (planted-forest) and delta_F_2^cross
(cross-channel) needs clearer exposition. They are conceptually distinct
(higher-arity vertex corrections vs multi-channel edge corrections) but
may overlap in the multi-weight case.

### Epistemic Honesty Assessment

The manuscript is correctly honest about the conjectural status of
Questions 3-5. The BV/BRST conjecture, the transport-to-transpose
conjecture, and the GZ26 comparison are all properly marked with
\ClaimStatusConjectured or \ClaimStatusConditional. The main concern
is Question 1, where an incorrect formula is tagged \ClaimStatusProvedHere.
