# Deep Beilinson Audit: raeeznotes115.md (6787 lines)

## Summary

**Structure**: raeeznotes115 = raeeznotes114 (verbatim, lines 1-2270) + NEW material (lines 2270-6787). The first 2270 lines are an EXACT DUPLICATE of raeeznotes114 (same sections 1-7: local open object, meromorphic tensor, factorization, global, chart/center, bar vs center, scope assessment). All 12 findings from the raeeznotes114 audit apply to those lines unchanged.

**New content** (lines 2270-6787, ~4500 lines): Explicit instantiation of the open-category primitive triple (A!, Delta_z, r(z)) for three physical examples:
1. Chern-Simons with algebraic gauge group (Section 1, lines 2549-4225)
2. Doubled Chern-Simons (Section 2, lines 4226-4483)
3. 3d gravity via DS reduction (Section 3, lines 4484-6787)

**Overall verdict**: 15 findings (1 SERIOUS, 5 MODERATE, 4 MINOR, 5 DUPLICATE/STANDARD). The new content is largely correct and genuinely useful for manuscript integration, but has one formula error in the BRST computation and several scope/honesty issues.

---

## DUPLICATE CONTENT (lines 1-2270)

### Finding D1: Sections 1-7 are verbatim raeeznotes114
- Lines 1-2270
- ALL content from raeeznotes114 is duplicated with minor whitespace differences
- The raeeznotes114 audit found 3 SERIOUS, 6 MODERATE, 3 MINOR findings
- All apply unchanged: Theorem 2 associativity proof is a sketch (Finding 3), bar/center/Theta_A distinction collapsed (Finding 8), compact generator hidden hypothesis (Finding 12)
- Verdict: DUPLICATE

---

## NEW CONTENT AUDIT (lines 2270-6787)

### Finding 1 (SERIOUS): BRST closure computation has wrong coefficient
- Lines 5618-5765
- The note derives: Q_DS(W) = (1-4a) J_hat^0 c + ((kappa+2) - 2b) partial c
- Then claims a = 1/4, b = (kappa+1)/2 make this zero
- But (kappa+2) - 2*(kappa+1)/2 = (kappa+2) - (kappa+1) = 1, NOT 0
- The error is in the intermediate step Q_DS(J^-) = J_hat^0 c + (kappa+2) partial c. The correct coefficient of partial c should be (kappa+1), not (kappa+2). With (kappa+1) - 2b = (kappa+1) - (kappa+1) = 0. CORRECT.
- The FINAL formula W = J^- + (1/4):J_hat^0 J_hat^0: + ((kappa+1)/2) partial J_hat^0 is CORRECT (matches standard DS literature). Only the derivation has a coefficient error in the Q_DS(J^-) step.
- Verdict: NEW-AND-WRONG (the intermediate computation; the end formula is correct)
- Impact: If integrated into manuscript, the verification paragraph must be corrected. The formula Q_DS(J^-) = J_hat^0 c + (kappa+2) partial c should read Q_DS(J^-) = J_hat^0 c + (kappa+1) partial c.
- Class: B (formula error)
- Severity: SERIOUS (wrong coefficient in a published computation)

### Finding 2 (MODERATE): r_Vir written as OPE, not collision residue
- Lines 5880-5998
- The note writes r_Vir(z-w) = c/2 / (z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
- This is the T(z)T(w) OPE itself, with the same pole orders
- In the DNP25 dg-shifted Yangian context, r(z) IS the spectral kernel / shifted lambda-bracket, which has the SAME pole structure as the OPE. This is correct within that framework.
- However, this is a DIFFERENT object from the bar r-matrix / collision residue (AP19), which absorbs one pole order via d log
- The note does not explicitly distinguish these two r-matrices
- Verdict: NEW-AND-CORRECT (in the DNP context), but potential AP19 confusion if integrated without qualification
- Class: C (structural)
- Severity: MODERATE
- If absorbed into manuscript: MUST add a remark distinguishing r(z)^{DNP} (spectral kernel, same poles as OPE) from r(z)^{bar} (collision residue, one lower pole order)

### Finding 3 (MODERATE): h_IJ sign discrepancy between mode and generating function forms
- Lines 3035-3395
- Mode form: Q(B_n^I) = n(k_IJ - h_IJ) c_{n-1}^J + f_{JK}^I sum B_s^K c_r^J
- Generating function form: QB^I(z)^- = -(k_IJ + h_IJ) partial c^J(z)^- + f_{JK}^I c^J(z)^- B^K(z)^-
- The mode form has (k - h) while the generating function has -(k + h). These should be consistent: the mode sum n*k*c_{n-1} becomes -k*partial(c) in generating function form (the n factor and z^{-n-1} combine). So (k-h) in modes becomes -(k-h) in generating function, NOT -(k+h).
- This is either a sign error or a convention shift from the normal-ordering correction
- Verdict: NEW-AND-SUSPICIOUS (needs independent verification of the normal-ordering correction between modes and fields)
- Class: B (formula)
- Severity: MODERATE

### Finding 4 (MODERATE): "Q-exact translation" claim for pure CS needs qualification
- Lines 4098-4225
- The note claims that when V=0 and k is nondegenerate, translations are Q-exact: [Q, L] = T. Therefore the meromorphic z-dependence of the tensor product is "homotopically trivialized."
- This is a STANDARD result in the HT literature (Costello-Li, and before them, the observation that topological theories have Q-exact energy-momentum tensors)
- The conclusion (C, otimes_z) ~ g-hat_{k-h^v}-mod is CORRECT
- But the claim requires k != h^v (else the level k-h^v = 0 is degenerate/critical). This condition is not stated.
- Verdict: NEW-AND-CORRECT but missing critical-level exception (AP18/AP7)
- Class: D (scope)
- Severity: MODERATE

### Finding 5 (MODERATE): r_grav formula conflates OPE and r-matrix
- Lines 6209-6560
- The note writes r_grav(z, z-bar) = c_L/2 / z^4 + 2T_L/z^2 + ... + c_R/2 / z-bar^4 + ...
- Same issue as Finding 2: this is the Virasoro OPE, presented as the "reduced shifted r-kernel"
- In the DNP dg-shifted Yangian framework, this IS r(z) (the spectral kernel)
- But writing it as r_grav without qualification risks AP19 confusion with the bar r-matrix
- Additionally, writing r_grav(z, z-bar) with BOTH z and z-bar dependence is unusual for a chiral object; the left and right sectors should be separately holomorphic/antiholomorphic
- Verdict: NEW-AND-CORRECT (in DNP framework) but needs clearer labeling
- Class: C (structural)
- Severity: MODERATE

### Finding 6 (MINOR): Khan-Zeng PVA identification is standard
- Lines 2695-2773
- The lambda-bracket {B_lambda^a B^b} = f^{ab}_c B^c + k kappa^{ab} lambda and field redefinition to HT CS is correctly stated
- This is a known result from Khan-Zeng (2023), already cited extensively in Vol II
- Verdict: STANDARD (not new)
- Class: E (editorial)
- Severity: MINOR

### Finding 7 (MINOR): Doubled CS construction is immediate
- Lines 4226-4483
- A!_dbl = A!_L hat-tensor A!_R, r_dbl = r_L + r_R, Delta_dbl = Delta_L hat-tensor Delta_R
- This is the obvious product construction and internal consistency follows from sectorwise separation
- Correct but mathematically trivial (product of independent sectors)
- Verdict: NEW-AND-CORRECT (but trivial)
- Class: E (editorial)
- Severity: MINOR

### Finding 8 (MINOR): Central charge formula c(kappa) verified correct
- Lines 5590-5614
- c(kappa) = 13 - 6(kappa+2) - 6/(kappa+2)
- Verified: this equals the standard 1 - 6(kappa+1)^2/(kappa+2). CORRECT.
- Verdict: STANDARD
- Class: N/A
- Severity: N/A

### Finding 9 (MINOR): h_IJ = h^v delta_IJ for simple g verified correct
- Lines 3118-3188
- h_IJ := (1/2) f_{IL}^K f_{JK}^L = h^v delta_IJ in Killing-orthonormal basis
- This is the adjoint Casimir identity. CORRECT for simple g.
- Verdict: STANDARD
- Class: N/A
- Severity: N/A

### Finding 10 (MINOR): Explicit mode expansion of r(z) is new
- Lines 2426-2507 (general formula), 3500-3585 (CS specialization)
- r(z) = sum_I sum_{n,m>=0} (-1)^n C(n+m, n) [c_n^I tensor B_{I,m} - B_n^I tensor c_{I,m}] / z^{n+m+1}
- This binomial-coefficient expansion is NOT in the manuscript
- It is a straightforward mode expansion of the contour integral, correct by construction
- Verdict: NEW-AND-CORRECT
- Where to absorb: Vol II, spectral-braiding-core.tex or line-operators.tex, as an explicit mode formula for the free-field r-matrix

### Finding 11: DS reduction produces gravity primitive only at BRST cohomology level
- Lines 6740-6787
- The note honestly states: the reduced r_grav is canonical at BRST cohomology level, but a chain-level element inside A!_grav requires choosing a homotopy transfer; different choices differ by Q_DS-exact terms
- This is a genuinely important caveat, correctly stated
- The note correctly identifies the next frontier step: explicit homological perturbation to write Delta_z^grav on the Virasoro side
- Verdict: NEW-AND-CORRECT (honesty clause)
- Where to absorb: Vol II, 3d_gravity.tex subsection on the primitive package, as a remark on the chain-level vs cohomology-level distinction

### Finding 12: Scope assessment (Section 7, inherited from rn114) is honest and correct
- Lines 2204-2257
- Correctly separates: (a) proved local open primitive, (b) proved meromorphic tensor + factorization equivalence, (c) open global tangential-log-curve programme, (d) open modular completion
- The new sections do NOT violate this scope: the CS/gravity content is local and perturbative
- Verdict: DUPLICATE (from rn114 audit)

---

## CONTENT NOT IN THE MANUSCRIPT (integration candidates)

### Priority 1 (should absorb):
1. **Explicit mode expansion of r(z)** (Finding 10, lines 2426-3585): The free-field r-matrix formula with binomial coefficients. Target: spectral-braiding-core.tex or line-operators.tex.
2. **Chain-level vs cohomology-level caveat for DS-reduced Yangian** (Finding 11, lines 6740-6787): Important honesty clause. Target: 3d_gravity.tex, subsec:3d-gravity-primitive-package.

### Priority 2 (could absorb if extended):
3. **Explicit A! generators and relations for CS** (Section 1.1, lines 2775-3410): The B_n, c_n mode algebra with explicit differential. Already partially in Vol I yangians_foundations.tex (prop on shifted cotangent loop algebra). Target: rosetta_stone.tex, subsec:cs-nonabelian-primitive-package (extend existing content).
4. **Explicit Delta_z for CS** (Section 1.3, lines 3608-3945): The free-field translation-coproduct in mode form. Standard but explicit. Target: spectral-braiding-core.tex.

### Priority 3 (already covered in manuscript):
5. The doubled CS construction (Section 2) is already implicit in the manuscript's product structure.
6. The gravity DS reduction to Virasoro (Section 3) is already covered in 3d_gravity.tex at the chart level.
7. The Sugawara/BRST-cohomology generator W (Section 3) is standard DS material, already cited.

---

## RELATIONSHIP TO RAEEZNOTES114 AUDIT

The raeeznotes114 audit identified two genuinely new pieces needing integration:
- S2: Meromorphic tensor product on modules (fills Costello Finding 6)
- S3: Theorem 3 equivalence of presentations (fills Costello Findings 2+6)

raeeznotes115 adds:
- S4: Explicit mode expansion of the free-field r-matrix (new, not in rn114)
- S5: Chain-level vs cohomology-level caveat for DS-reduced gravity Yangian (new)
- S6: Explicit A! mode algebra for CS gauge theory (extends existing manuscript content)

Items S2 and S3 from the rn114 audit are still pending integration.

---

## ERROR SUMMARY

| # | Lines | Type | Severity | Description |
|---|-------|------|----------|-------------|
| 1 | 5618-5765 | B (formula) | SERIOUS | Q_DS(J^-) has kappa+2 instead of kappa+1 (intermediate step; final formula correct) |
| 2 | 5880-5998 | C (structural) | MODERATE | r_Vir written as OPE without distinguishing from bar r-matrix (AP19 risk) |
| 3 | 3035-3395 | B (formula) | MODERATE | Mode (k-h) vs field -(k+h) sign discrepancy needs resolution |
| 4 | 4098-4225 | D (scope) | MODERATE | Q-exact translation claim missing critical-level exception |
| 5 | 6209-6560 | C (structural) | MODERATE | r_grav labeled without DNP vs bar qualification |
