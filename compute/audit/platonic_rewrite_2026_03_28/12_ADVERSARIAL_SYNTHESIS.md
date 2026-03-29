# ADVERSARIAL SYNTHESIS — 7-AGENT TEARDOWN RESULTS

## Date: 2026-03-28
## Agents: Witten, Costello, Kontsevich, Gaiotto, Polyakov, Drinfeld, Beilinson

---

## EXECUTIVE SUMMARY

7 elite adversarial agents examined every claim in the rewrite plan.

**FATAL findings: 0.** No proved theorem in the manuscript is destroyed.

**CRITICAL findings: 2.**
  1. Annulus = HH_* (M7) does not exist in the manuscript and requires careful
     excision argument with monodromy specification. (Polyakov)
  2. An estimated 20-40 ProvedHere claims should be Conditional, concentrated
     in the THQG extension (310 claims across 12 files). (Beilinson)

**SERIOUS findings: 14.**
  - Center theorem (M3): 5 serious gaps (undefined category, spectral
    substitution well-definedness, scope inflation from boundary-linear
    to universal, missing hypotheses). (Witten)
  - Open-sector definition: 3 serious gaps (tau-Morita unproved, no example
    constructed, bordered FM status contradiction). (Costello)
  - Operadic foundations: 2 serious gaps (homotopy-Koszulity proof absent
    from Vol I, brace integral formula absent). (Kontsevich)
  - Spectral consistency: 1 serious gap (Virasoro r(z) has 4 incompatible
    formulas across codebase — live AP5+AP9). (Drinfeld)
  - Physical consistency: 2 serious gaps (KZ action is classical not quantum,
    Laplace transform formula inconsistent with claimed output). (Gaiotto)
  - Modular foundations: 1 serious gap (bordered FM vs log-FM interaction
    unspecified). (Polyakov)

**MODERATE findings: 20.** (See individual reports.)
**MINOR findings: 8.** (See individual reports.)

---

## THE 5 MOST CRITICAL CORRECTIONS

### CORRECTION 1: The center theorem scope must be HONEST

The center theorem (M3), as described in the planning documents, claims
universal initiality without restriction. The actual proved content is:

  - Boundary-linear sector: PROVED (Vol II hochschild.tex)
  - Logarithmic SC algebras: PROVED (Vol II brace.tex)
  - General A_infty-chiral algebras: OPEN

The plan must state the theorem for LOGARITHMIC SC ALGEBRAS (where brace
operations are well-defined by controlled singularities), not for arbitrary
A_infty-chiral algebras.

**Specific hypothesis needed:** The A_infty-chiral algebra A must be a
logarithmic SC^{ch,top}-algebra in the sense of Vol II Def ref:def:log-SC-algebra.
This ensures:
  (a) Brace operations are well-defined (integrals converge on FM compactifications)
  (b) Spectral substitution is compatible with the iterated Laurent topology
  (c) The category of SC pairs is well-defined

Without this hypothesis, the brace operations may not exist (Witten finding 5,
Kontsevich finding 6).

### CORRECTION 2: The Virasoro r(z) inconsistency must be resolved

Drinfeld found 4 mutually incompatible formulas for r(z) of Virasoro:
  - thqg_preface_supplement.tex: r(z) = c/(2z^3) + 2T/z
  - compute/lib/e1_shadow_tower.py: r(z) = c/(2z) (scalar on primary line)
  - compute/lib/collision_residue_identification.py: r(z) = (c/2)/z^4
  - compute/tests/test_e1_tridegree_shadows.py: r(z) = (c/2)/z

Gaiotto independently found that the Laplace transform formula gives
r(z) = c/(2z^4) + 2T/z^2 + dT/z, which matches NONE of the above.

Root cause: "r(z)" is used for at least THREE different objects:
  (i)   The collision residue Res^{coll}_{0,2}(Theta_A) (a graph extraction)
  (ii)  The Laplace transform of the lambda-bracket (an integral transform)
  (iii) The scalar restriction to the primary line (a 1D projection)

These are different objects with different pole orders. The notation AP9
violation (same name, different object) must be fixed BEFORE any further
computation involving r(z).

**Action:** Introduce distinct notation:
  - r^{coll}(z) for the collision residue
  - r^{Lap}(z) for the Laplace transform
  - r^{sc}(z) for the scalar primary-line restriction

Then verify which formula is correct for each notion. Fix all ~4 tex files
and ~3 compute modules.

### CORRECTION 3: The MC equation proof mechanism description must be corrected

Polyakov found that the planning document (M6) incorrectly describes the
proof as "Stokes on compactified 1-dimensional families." The actual
manuscript proof is codimension-2 face cancellation on the full moduli space
(d^2 = 0 on chains of M-bar_{g,n}). The MC equation follows from D_A^2 = 0,
which is the algebraic transport of boundary-of-boundary = 0.

**Action:** Correct M6 description. The MC equation at general (g,n) is NOT
derived from Stokes on 1-parameter families. It is a formal consequence of
D_A^2 = 0 (convolution-level) or D^2 = 0 (ambient-level, Mok25-dependent).

### CORRECTION 4: The Laplace transform formula is wrong

Gaiotto found an internal inconsistency: the staircase document computes
r(z) = k/z^2 from the Laplace transform of {J_lambda J} = k*lambda, but
then claims r(z) = hbar*q_1*q_2/z. These have DIFFERENT z-dependence.

The root issue: there are two different "r(z)" objects:
  (a) The Laplace transform of the lambda-bracket: gives k/z^2
  (b) The classical r-matrix in the Yangian sense: gives k/z

These are related by the fact that the OPE J(z)J(w) ~ k/(z-w)^2 has
SECOND-order pole, and the r-matrix extracts the RESIDUE of the pole
(which is k/z, not k/z^2).

**Action:** Fix the Laplace transform formula in the staircase. The correct
statement is: the r-matrix r(z) = Omega/z is the Laplace transform of the
SINGULAR part of the OPE (the coefficient of 1/(z-w)), not of the
lambda-bracket itself. The lambda-bracket and the r-matrix are related by
r(z) = sum_{n>=0} c_n/z^{n+1} where c_n = res_{lambda=0} lambda^n {a_lambda b}/n!.

### CORRECTION 5: Bordered FM compactification status must be clarified

Costello found that the bordered FM compactification is marked CONJECTURAL
in one frontier chapter (ordered_associative_chiral_kd_frontier.tex) but
the strata proposition using it is marked PROVED in another
(modular_pva_quantization_core.tex). These cannot both be correct.

**Action:** Determine the true status. Either:
  (a) The bordered FM compactification exists (prove it or cite it), and
      upgrade the conjectural tag. OR:
  (b) It is genuinely open, and downgrade the ProvedHere tag on all results
      that use it.

This affects M5 and M6 in the plan.

---

## THE 14 SERIOUS FINDINGS IN DETAIL

### From Witten (Center Theorem):

W1. Theorem does not exist in source — blueprint only. [SERIOUS]
W2. "Local chiral SC pair" is undefined. [SERIOUS]
W3. Initiality claim conflates two different categories. [SERIOUS]
W5. Spectral substitution well-definedness non-trivial. [SERIOUS]
W11. Boundary-linear scope not propagated (AP7). [SERIOUS]

### From Costello (Open Sector):

C1. "Constructible dg-cosheaf" undefined on mixed Ran space. [SERIOUS]
C2. Tau-Morita invariance unproved. [SERIOUS]
C6. No explicit example constructed. [SERIOUS]

### From Kontsevich (Operadic):

K2. Homotopy-Koszulity of SC^{ch,top}: proof absent from Vol I. [SERIOUS]
K3. Brace operations: geometric integral formula not written. [SERIOUS]
K6. Spectral substitution: iterated Laurent expansion order. [SERIOUS]

### From Drinfeld (Spectral):

D1. Virasoro r(z) has 4 incompatible formulas. [SERIOUS]

### From Gaiotto (Physical):

G2. KZ action for affine sl_2 is CLASSICAL, not quantum. [SERIOUS]
G7. Laplace transform inconsistency (k/z^2 vs k/z). [SERIOUS]

### From Polyakov (Modular):

P3. Bordered FM vs log-FM interaction unspecified. [SERIOUS]

---

## FORTIFIED M1-M12 LIST (with adversarial corrections incorporated)

### M1. Chiral brace operations
**Original:** Explicit formula with spectral substitution.
**Correction (K3, K6):** The integral formula must be written GEOMETRICALLY
(over FM compactifications), not just algebraically. The iterated Laurent
expansion order must be specified (BD convention: expand in lambda_{k-1}
first, then lambda_{k-2}, etc.). The logarithmic hypothesis
(Def ref:def:log-SC-algebra) is REQUIRED for well-definedness.

### M2. Chiral brace identities
**Original:** Statement + proof from tree enumeration.
**Correction (K1):** The product FM_k(C) x E_1(m) must be treated
chain-level, not topologically. Use the Eilenberg-Zilber/Alexander-Whitney
maps for the Kunneth quasi-isomorphism, or work with the total complex of
the bicomplex. State the Kunneth hypothesis explicitly.

### M3. Center theorem
**Original:** U(A) is initial SC pair, universal.
**Correction (W2, W3, W5, W11):** RESTRICT to logarithmic SC-algebras.
Define the category of SC pairs precisely. State the spectral substitution
convention. The scope is: logarithmic SC-algebras at genus 0, non-critical
level. The boundary-linear case is PROVED; the general logarithmic case
requires the brace identities (M2) to be established first.

### M4. Derived center = Hochschild cochains
**Original:** Morita argument.
**Correction (W12):** Requires compact generation hypothesis. State:
"Let C be a compactly generated dg-category with compact generator b."

### M5. Bordered FM compactification
**Original:** Construction of mixed config spaces + compactification.
**Correction (C4, P3, C11):** The compactification is NOT a product of
FM_k(C) x Stasheff. It requires blowing up mixed diagonals (holomorphic
and topological singularities entangled). Must specify the relationship to
Mok's log-FM: is bordered FM the real-oriented blowup of log-FM?
Must resolve the conjectural/proved status contradiction.

### M6. Modular MC equation with clutching
**Original:** Stokes on 1-dimensional families.
**Correction (P1):** NOT Stokes on 1-dimensional families. The proof is
codimension-2 face cancellation on the full moduli space: D_A^2 = 0 is
automatic from boundary-of-boundary = 0 on chains. The clutching term
Delta_clutch is the non-separating node contribution within the full
modular operad bracket (K7 clarification: in Getzler-Kapranov's formalism,
clutching IS part of the bracket, separated only by separating vs
non-separating nodes).

### M7. Annulus = Hochschild chains
**Original:** Excision proof.
**Correction (P2):** Must specify: (i) E_1 structure from tangential
linearization, (ii) Ayala-Francis collar-gluing theorem, (iii) monodromy
around the puncture. The naive excision argument cuts S^1 into two arcs;
the factorization cosheaf must satisfy Mayer-Vietoris on these arcs.
For non-trivial monodromy (e.g., twisted modules), the Hochschild chains
are TWISTED Hochschild chains.

### M8. One-step Jacobi coalgebra
**Original:** Construction from Taylor coefficients.
**No significant corrections.** Beilinson confirmed this is genuinely missing.
The construction is algebraically clean.

### M9. Boundary-linear LG theorem
**Original:** bulk = O(dCrit(W)).
**Correction (Beilinson):** PARTIALLY present in
deformation_quantization_examples.tex. The specific formulation as a named
theorem may be missing, but the dCrit material exists. Check before writing
duplicate content.

### M10. Chiral Cartan formula
**Original:** [T, f] = df + delta(iota_T f).
**Correction (G5):** Specify: holds for the UNIVERSAL Virasoro VOA V_c at
ALL c. For the simple quotient L_c at rational c (minimal models),
additional analysis needed. The notation iota_T is non-standard in VOA
literature — define it explicitly.

### M11. Degree counting for cubic LG
**Original:** m_4 = 0 by FM dimension deficit.
**Correction (G1):** Clarify that the degree counting is on the holomorphic
FM slice FM_k(C), not on the full 3d HT configuration space. The
t-direction contributes degree 0 (step functions, not differential forms).
The deficit is 4 real dimensions, independent of k.

### M12. Complementarity verification
**Correction (Beilinson):** This is a FALSE ALARM. Complementarity
verifications ALREADY EXIST in landscape_census.tex and example chapters.
Do not duplicate. Instead, consolidate existing verifications into a
single table with the staircase presentation.

---

## FORTIFIED SCOPE STATEMENT

The center theorem, in its HONEST form, says:

**Theorem (Chiral Center Theorem — logarithmic case).**
Let A be a logarithmic SC^{ch,top}-algebra on a disk D in C. Then:

(a) The chiral Hochschild cochain complex C^bullet_ch(A,A), equipped with
    brace operations defined by integration over FM compactifications
    with logarithmic weight forms, is a brace dg algebra.

(b) The pair U(A) = (C^bullet_ch(A,A), A) is a local chiral Swiss-cheese
    pair in the sense of the SC^{ch,top}-operad.

(c) U(A) is initial among all logarithmic SC pairs with fixed open color A:
    for any logarithmic SC pair (B, A), there is a unique morphism
    Phi: B -> C^bullet_ch(A,A) in the category of SC^{ch,top}-algebras
    compatible with the action on A.

**Hypothesis required:** A is logarithmic (Def ref:def:log-SC-algebra),
meaning the OPE kernels extend to logarithmic forms on FM compactifications
with controlled singularities. This holds for ALL standard families
(Heisenberg, KM, Virasoro, W_N, lattice VOAs) at generic (non-critical)
level.

**NOT claimed:** Initiality for arbitrary A_infty-chiral algebras with
distributional or non-convergent spectral substitutions.

---

## FORTIFIED PLAN CORRECTIONS

### Correction to 09_EXAMPLE_STAIRCASE.md:

1. Fix the Laplace transform formula (Correction 4).
   r(z) for Heisenberg is k/z (the r-MATRIX), not k/z^2 (the Laplace of
   the lambda-bracket). The r-matrix extracts the singular part of the OPE,
   not the lambda-bracket.

2. Qualify KZ action as CLASSICAL (Correction from Gaiotto finding 2).
   The 3d HT action from Khan-Zeng is the classical limit. The identification
   with Chern-Simons is at the classical level. Quantum corrections
   (deformation quantization of PVA to VOA) are the open problem.

3. Add Virasoro r(z) disambiguation (Correction 2).

### Correction to 08_NEW_CHAPTERS.md:

1. Restrict the center theorem to logarithmic SC algebras (Correction 1).
2. Fix M6 proof mechanism (Correction 3).
3. Resolve bordered FM status (Correction 5) before writing M5.

### Correction to 11_REASSESSMENT.md:

1. M12 is a false alarm — complementarity already exists.
2. M9 is partially present — check before duplicating.
3. The density claim of "4 formal environments per 200 lines" for chiral
   Hochschild chapter is inflated; actual is 2.67. Correct the diagnostic.
4. Add: the THQG extension has an estimated 20-40 ProvedHere claims that
   should be Conditional. This is the manuscript's largest systematic
   vulnerability and must be addressed in the rewrite.

### New item: r(z) disambiguation (added to M-list as M0)

**M0. r(z) notation disambiguation.**
Introduce three distinct notations:
  r^{coll}(z) = collision residue of Theta_A
  r^{Lap}(z) = Laplace transform of lambda-bracket
  r^{sc}(z) = scalar primary-line restriction
Fix all 4 tex files and 3 compute modules. Verify pole orders.

---

## WHAT THE ADVERSARIAL PASS CONFIRMS

Despite 14 serious findings, the CORE is sound:

1. **The five main theorems (A-D+H) are PROVED and CLEAN.** No adversarial
   agent found a gap in any proved theorem. (Beilinson explicitly verified.)

2. **The MC2 bar-intrinsic construction is CLEAN.** Zero preprint risk.

3. **The shadow Postnikov tower convergence is CORRECT.** Weight-completed
   pro-nilpotent topology with explicit Mittag-Leffler. (Polyakov verified.)

4. **The modular MC equation mechanism is CORRECT in the manuscript.** The
   codimension-2 face cancellation proof is clean. (Only the PLANNING
   DOCUMENT described it incorrectly.)

5. **The Koszulness characterization programme is CORRECT.** 10 unconditional
   + 1 conditional + 1 one-directional, consistently tracked.

6. **The center theorem is PLAUSIBLE and the basic idea is SOUND.** The
   topological analogue is true. The boundary-linear case is proved. The
   extension to logarithmic SC algebras is a well-posed theorem with a
   clear proof strategy.

The serious findings are concentrated in:
  (a) Planning documents that overclaim or misdescribe (not the manuscript)
  (b) Notational inconsistencies (r(z) disambiguation, AP9)
  (c) Missing hypotheses (logarithmic, compact generation)
  (d) Status tag debt (THQG ProvedHere vs Conditional)

These are all fixable. None threatens the proved core.
