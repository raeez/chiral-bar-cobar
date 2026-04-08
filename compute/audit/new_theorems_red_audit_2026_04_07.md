# Deep Beilinson RED Audit: New Theorems (2026-04-07)

Auditor: Claude Opus 4.6 (adversarial, falsification-maximizing)

Six theorems audited across two volumes. Findings numbered sequentially.
Severity: CRITICAL > SERIOUS > MODERATE > MINOR.

---

## Theorem 1: thm:dnp-bar-cobar-identification
**File**: `~/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex`, lines 1671--1783
**Status tag**: `\ClaimStatusProvedHere`
**Environment**: `\begin{theorem}` — matches tag (OK)

### Statement summary
Three-part identification of the DNP line-operator package with the bar-cobar twisting package:
(i) monoidal identification of meromorphic tensor product with R-twisted tensor product,
(ii) MC identification of r(z) with collision residue of Theta_A,
(iii) non-renormalization = Koszulness (E_2-collapse = one-loop exactness).

### F1 — Part (iii): Conflation of bar formality with Swiss-cheese formality (MODERATE, AP14)
**Claim**: "E_2-collapse of the bar spectral sequence means ... the bar cohomology algebra A!_line is formal: all transferred A_infinity operations m_k for k >= 3 vanish."
**Issue**: This conflates two different properties (AP14). E_2-collapse (bar formality / chiral Koszulness) means bar cohomology H*(B(A)) is concentrated in bar degree 1 — this does NOT automatically imply that the transferred A_infinity operations m_k vanish. The operations m_k on bar cohomology A^i = H*(B(A)) vanish iff the bar complex is A_infinity formal (item (iii) of thm:koszul-equivalences-meta), which IS a consequence of chiral Koszulness. The statement is technically correct because all items of the Koszulness meta-theorem are equivalent, but the PROOF step conflates the definitions. The sentence "E_2-collapse means ... m_k = 0" is misleading: E_2-collapse means bar concentration; m_k = 0 is A_infinity formality; these are different characterizations that happen to be equivalent on the Koszul locus.
**Impact**: Low — the equivalence holds, so the conclusion is correct. The proof route is sloppy but not circular.

### F2 — Part (i): Proof depends on thm:Koszul_dual_Yangian, which is scoped to affine HT gauge realizations (MODERATE)
**Claim**: Part (i) cites "Theorem thm:Koszul_dual_Yangian, Step 3" for the R-twisted coproduct.
**Issue**: The theorem thm:Koszul_dual_Yangian (in spectral-braiding-core.tex, line 1541) is scoped to "the standard affine HT gauge realization with closed colour V_k(g), satisfying the hypotheses of Theorem thm:physics-bridge." But the DNP identification theorem is stated for a general "chirally Koszul logarithmic SC^{ch,top}-algebra." The proof chain has a scope mismatch: it uses a theorem proved for the physical affine case to justify a statement about general chirally Koszul algebras. Per the linear_read_notes.md audit (lines 383-384), there is a general operadic statement (thm:yangian-recognition) that should be cited instead of thm:Koszul_dual_Yangian for the general case.
**Impact**: The proof works for affine KM algebras; for general chirally Koszul algebras, it relies on the general thm:yangian-recognition which should be cited instead.

### F3 — Part (ii): r(z) lives in A^! otimes A^!, not A otimes A (MINOR)
**Claim**: "The A_infinity Yang-Baxter MC element r(z) in A^! otimes A^! of [DNP25] is the genus-0 binary collision residue of Theta_A."
**Issue**: This is stated correctly in the theorem but the proof (line 1758) writes "the universal twisting morphism pi_A in Tw(B(A), A)" — which is a morphism FROM B(A) TO A, not an element of A^! otimes A^!. The identification of the twisting morphism with the r-matrix requires the Koszul-dual coordinate change. The proof gesture is correct but glosses over the coordinate change.
**Impact**: Low — the identification is mathematically standard.

### F4 — Hypothesis: "chirally Koszul" may be overly restrictive (MINOR)
The theorem requires chirally Koszul. The DNP framework does not require Koszulness — it works for any 3d HT theory with line operators. The Koszulness hypothesis is used in part (iii) but not in parts (i)-(ii). Parts (i)-(ii) should hold more generally.
**Impact**: Mild scope restriction.

---

## Theorem 2: thm:gz26-commuting-differentials
**File**: `~/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex`, lines 1563--1658
**Status tag**: `\ClaimStatusProvedHere`
**Environment**: `\begin{theorem}` — matches tag (OK)

### Statement summary
Five-part theorem: (i) Hamiltonian decomposition + commutativity from MC flatness, (ii) collision-depth expansion, (iii) KZ recovery for affine KM, (iv) BPZ recovery for Virasoro, (v) prediction for W_N.

### F5 — Part (i): Flatness -> commutativity step assumes specific form of connection (MODERATE)
**Claim**: "The connection form depends on positions only through the differences z_{ij}, so partial_i H_j = -partial_j H_j|_{z_ij} and the flatness equation reduces to [H_i, H_j] = 0."
**Issue**: The reduction from flatness (dOmega + Omega ^ Omega = 0) to commutativity ([H_i, H_j] = 0) requires that H_i depends on z_j only through z_{ij}. This is true for the KZ connection and for shadow connections that arise from translation-invariant OPE data, but it is an additional hypothesis about the structure of the shadow representation Sh_{0,n}(Theta_A), not something that follows automatically from the MC element. The proof claims this follows because "the connection form depends on positions only through the differences z_{ij}" — this needs the fact that the OPE is translation-invariant and the shadow representation respects this.
**Impact**: The hypothesis is satisfied for all standard families; the proof is correct in practice but should note the translation-invariance assumption.

### F6 — Part (iv): Virasoro Hamiltonian formula has a sign/ordering issue (MODERATE)
**Claim**: The Virasoro Hamiltonian is H_i = sum_{j != i} (h_j/z_{ij}^2 + partial_{z_j}/z_{ij}).
**Issue**: The standard BPZ/KZ connection for Virasoro takes the form:
nabla = d - sum_i L_{-1}^{(i)} dz_i where L_{-1}^{(i)} = sum_{j!=i} (h_j/(z_i-z_j)^2 + partial_{z_j}/(z_i-z_j))
This formula is correct. However, the depth-3 term (c/2)/z_{ij}^3 in the proof (line 1712) is claimed to "act trivially on primary states." This is correct: on primary states |h>, the c/2 term contributes a scalar that, when summed over j with the cube of differences, gives zero by the global conformal Ward identity (SL(2) invariance forces the sum of 1/z_{ij}^3 terms to vanish on the conformal block space after gauge-fixing). But this is a nontrivial statement about the conformal block space, not an obvious triviality. The proof does not justify this claim.
**Impact**: The formula is correct for primary external states; the argument is incomplete for general descendant states, where the depth-3 term does not act trivially.

### F7 — Part (v): "Prediction" language for W_N (MODERATE, AP40-adjacent)
**Claim**: Part (v) is labeled as a "prediction" with ClaimStatusProvedHere.
**Issue**: The term "prediction" suggests this is a conjecture to be verified, but the theorem is tagged ProvedHere. The content of part (v) is: the collision-depth expansion PRODUCES differential operators of order 2N-2 from the W_N OPE data, and the commutativity follows from the MC equation. This IS proved (from the MC element and the OPE structure). The word "prediction" refers to the comparison with the GZ26 paper, not to the mathematical content. However, the comparison with GZ26 is NOT proved — it is stated as "a concrete prediction verifiable term by term." This is an AP40-adjacent issue: the theorem mixes proved content (existence and commutativity of the Hamiltonians) with unverified comparison (agreement with GZ26).
**Impact**: The mathematical content is proved; the comparison with GZ26 is a prediction, not a theorem.

---

## Theorem 3: thm:gaudin-yangian-identification
**File**: `~/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex`, lines 1760--1820
**Status tag**: `\ClaimStatusProvedHere`
**Environment**: `\begin{theorem}` — matches tag (OK)

### Statement summary
Three-part: (i) Gaudin = GZ26 for affine KM, (ii) higher Gaudin for general A, (iii) quantization parameter hbar = 1/(k+h^v).

### F8 — Part (i): Attribution to Feigin-Frenkel-Reshetikhin is correct (OK)
The citation FFR94 (Feigin, Frenkel, Reshetikhin, "Gaudin model, Bethe ansatz and critical level", Comm. Math. Phys. 166, 1994) is the correct original source for the connection between the Gaudin model and the critical level of affine algebras. The Gaudin Hamiltonians H_i^{Gaudin} = sum_{j!=i} Omega_{ij}/z_{ij} are standard and correctly attributed.

### F9 — Part (i): The prefactor 1/(k+h^v) requires justification (MODERATE)
**Claim**: H_i^{GZ} = (1/(k+h^v)) H_i^{Gaudin}
**Issue**: The collision residue for affine KM is r(z) = Omega/((k+h^v)z), which follows from the OPE J^a(z)J^b(w) ~ k*delta^{ab}/(z-w)^2 + f^{ab}_c J^c/(z-w) and the d log absorption (AP19). The d log kernel extracts the simple-pole coefficient: the OPE has poles of order 2 and 1; after d log absorption the collision residue has pole order 1 and 0. The pole-1 residue is the Casimir Omega_{ij}, and the normalization involves the Killing form normalization and level. The factor 1/(k+h^v) comes from the DUAL Coxeter normalization of the Casimir: Omega = sum_a J^a otimes J^a where the J^a are normalized so that [J^a, J^b] = f^{ab}_c J^c and the Sugawara formula gives T = (1/(2(k+h^v))) sum_a :J^a J^a:. The collision residue extraction picks up this 1/(2(k+h^v)) factor (times 2 from the Casimir in the standard normalization). The proof (line 1825) simply states the formula without deriving the prefactor; it relies on thm:shadow-connection-kz. This is acceptable as a proof-by-reference.
**Impact**: Low — the formula is standard and correctly cited.

### F10 — Part (ii): "Higher Gaudin Hamiltonians" is a new concept (MODERATE, AP43-adjacent)
**Claim**: "The terms at k >= 2 are the higher Gaudin Hamiltonians associated to the A_infinity Yangian structure."
**Issue**: The term "higher Gaudin Hamiltonians" is introduced here without a formal definition. The standard Gaudin model has Hamiltonians from the Casimir (k=1 term only). The "higher Gaudin" system from higher collision residues is a new construction in this manuscript. It is not obviously the same as any existing generalization of the Gaudin model in the literature (e.g., the higher Gaudin models of Feigin-Frenkel or the quantum Gaudin models of Feigin-Frenkel-Toledano Laredo). AP43 requires central objects to be formally defined.
**Impact**: Terminological, not mathematical. The construction is well-defined; the name is informal.

### F11 — Part (iii): hbar = 1/(k+h^v) -> 0 as k -> infinity is correct (OK)
The classical limit is standard. The verification in the compute engine confirms the convergence.

---

## Theorem 4: thm:yangian-sklyanin-quantization
**File**: `~/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex`, lines 1868--1904
**Status tag**: `\ClaimStatusProvedHere`
**Environment**: `\begin{theorem}` — matches tag (OK)

### Statement summary
Three-part: (i) Sklyanin bracket = classical limit of Yangian, (ii) coproduct quantizes Lie-Poisson, (iii) three identifications of hbar.

### F12 — The theorem is a rewording of known results with ClaimStatusProvedHere (SERIOUS, AP40)
**Claim**: Tagged ProvedHere.
**Issue**: Part (i) — that the Yangian Y_hbar(g) quantizes the Sklyanin-Poisson bracket — is Drinfeld's theorem (1985), not a new result. Part (ii) — that the Yangian coproduct quantizes the Lie-Poisson coproduct — is also classical (Drinfeld). Part (iii) — the three identifications of hbar — is the only genuinely new content, and it is essentially a normalization check.

The proof (lines 1907-1949) explicitly attributes part (i) to Semenov-Tian-Shansky and Drinfeld, and verifies numerically for sl_2. There is no new mathematical content in parts (i)-(ii); the theorem synthesizes known results from three different papers and identifies the normalization.

The correct status would be: parts (i)-(ii) are ProvedElsewhere (Drinfeld, STS), and part (iii) is ProvedHere. Tagging the entire theorem as ProvedHere is a status inflation (AP40). The theorem should either be:
- A proposition with ClaimStatusProvedElsewhere for parts (i)-(ii) and a remark for part (iii), or
- A theorem that makes clear the NOVEL content is the identification, not the individual parts.

**Impact**: Status inflation. The mathematical content is correct but not new.

### F13 — Part (ii): Coproduct formula has wrong structure (MODERATE)
**Claim**: "Delta(x) = x otimes 1 + 1 otimes x + hbar[r^cl, x otimes 1] + O(hbar^2)" (line 1924-1925).
**Issue**: The standard Yangian coproduct in evaluation representations is NOT of this form. The correct Drinfeld coproduct of the Yangian Y(g) is:
  Delta(J^a) = J^a otimes 1 + 1 otimes J^a (the primitive part)
  Delta(T^a) = T^a otimes 1 + 1 otimes T^a + (hbar/2) f^a_{bc} J^b otimes J^c
where T^a are the level-1 generators. In evaluation representation at z:
  Delta_z(J^a) = J^a otimes 1 + 1 otimes J^a
  Delta_z(T^a) = T^a otimes 1 + 1 otimes T^a + z*(J^a otimes 1) + hbar * [r, J^a otimes 1]
The formula in the manuscript writes "hbar[r^cl, x otimes 1]" as the correction, which is a schematic expression. The "x" on the left should be a generator, not a general element (the coproduct is defined on generators and extended by algebra structure). This is not wrong per se but is imprecise.
**Impact**: The formula is schematic/heuristic, not a precise mathematical identity.

---

## Theorem 5: thm:kz-classical-quantum-bridge
**File**: `~/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex`, lines 2223--2287
**Status tag**: `\ClaimStatusProvedHere`
**Environment**: `\begin{theorem}` — matches tag (OK)

### Statement summary
Four-part: (i) genus-0 seed from PVA lambda-bracket, (ii) genus-1 obstruction via BV operator, (iii) all-genera completion via bar-intrinsic MC, (iv) gauge invariance = Jacobi.

### F14 — Parts (i)-(iii) are summary theorems referencing established results (MODERATE)
**Claim**: Tagged ProvedHere.
**Issue**: The four parts each reference an already-proved theorem: part (i) cites thm:collision-residue-twisting and thm:collision-depth-2-ybe; part (ii) cites thm:w3-genus1-curvature; part (iii) cites thm:mc2-bar-intrinsic; part (iv) cites thm:bar-nilpotency-complete. The "theorem" is really a SYNTHESIS — it packages known results into a narrative about the deformation-quantization bridge. This is legitimate as a theorem statement (a theorem can combine established facts into a new statement), and the proof correctly references the established results.
**Impact**: Low — the synthesis is a valid theorem.

### F15 — Part (iv): "Gauge invariance = Jacobi" conflates two levels (MODERATE, AP42)
**Claim**: "The gauge invariance condition of the KZ25 Poisson sigma model is the lambda-Jacobi identity."
**Issue**: The KZ25 sigma-model gauge invariance is a GEOMETRIC condition (invariance of a path integral under gauge transformations). The lambda-Jacobi identity is an ALGEBRAIC condition (an identity among lambda-bracket coefficients). The claim that these are "the same" is a sophisticated identification that holds at the level of formal algebraic structures (the Maurer-Cartan equation in both frameworks gives d^2 = 0), but the two conditions are formulated in different categories. The proof sketch (lines 2307-2319) gives a reasonable argument linking them via the Arnold relation, but the step from "geometric gauge invariance" to "algebraic Jacobi" requires the full comparison between the BV path integral and the bar complex, which is only proved at genus 0.
**Impact**: The identification is correct at genus 0; at higher genus it is conjectural (conj:master-bv-brst).

---

## Theorem 6: thm:shadow-depth-operator-order
**File**: `~/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex`, lines 1952--2005
**Status tag**: `\ClaimStatusProvedHere`
**Environment**: `\begin{theorem}` — matches tag (OK)

### Statement summary
Three-part: (i) finite depth => multiplication operators (k_max = 1), (ii) infinite depth => differential operators, (iii) non-formality detection.

### F16 — CRITICAL ERROR: beta-gamma p_max is 1, not 2 (CRITICAL)
**Claim**: The table at lines 1985-1991 assigns p_max = 2, k_max = 1 to beta-gamma. The proof (lines 2009-2016) says: "beta(z)gamma(w) ~ 1/(z-w), which is a simple pole, but the Sugawara energy-momentum tensor introduces a double pole."
**Issue**: This is a CRITICAL mathematical error. The theorem itself at lines 1958-1960 defines: "Write p_max for the maximal OPE pole order among **generating fields**." The generating fields of the beta-gamma system are beta and gamma. Their OPE is:
  beta(z)gamma(w) ~ 1/(z-w)   (simple pole, p = 1)
  beta(z)beta(w) ~ regular     (p = 0)
  gamma(z)gamma(w) ~ regular   (p = 0)
So p_max = 1, NOT 2. The Sugawara energy-momentum tensor T = :partial(beta)gamma: is a COMPOSITE field, not a generator. Its OPE T(z)T(w) has a quartic pole, but T is not among the "generating fields."

The proof acknowledges the problem ("which is a simple pole") but then claims the Sugawara tensor "introduces" a double pole. This is wrong by the theorem's own definition: p_max is among generators. The Sugawara tensor is not a generator.

**Consequence**: If p_max(betagamma) = 1, then k_max = p_max - 1 = 0. This means the collision-depth expansion has NO terms (k_max = 0), and the GZ26 Hamiltonians are... identically zero? This seems wrong too.

**Root cause analysis**: The confusion arises because there are TWO natural choices for p_max:
(a) p_max among generators (as stated in the theorem): for betagamma, this gives p_max = 1.
(b) p_max among ALL fields including composites: for betagamma, this gives p_max = 4 (from the T-T OPE with quartic pole).

Neither choice gives the claimed p_max = 2. The value p_max = 2 would be correct if one includes the SUGAWARA TENSOR as a quasi-generator (it appears in the T-beta and T-gamma OPEs with double poles: T(z)beta(w) ~ lambda*beta/(z-w)^2 + ..., T(z)gamma(w) ~ (1-lambda)*gamma/(z-w)^2 + ...). But T is not an independent generator — it is determined by beta and gamma.

The deeper issue: the SHADOW DEPTH of betagamma is 4 (class C, r_max = 4), which is NOT equal to k_max + 1. The theorem tries to relate shadow depth class to operator order, but for betagamma, the shadow depth comes from the quartic contact invariant (which involves normal-ordered composites at arity 4), NOT from higher OPE poles of generators.

The correct resolution: the beta-gamma system should NOT appear in the "finite depth => k_max = 1" part of the table with p_max = 2. Instead:
- If p_max is defined among generators: betagamma has p_max = 1, k_max = 0, and the Hamiltonians vanish (the shadow connection has no poles in z_{ij}, so correlators are constant — consistent with the VANISHING r-matrix noted in beta_gamma.tex line 96-100).
- If p_max is defined among all fields: betagamma has p_max = 4, k_max = 3, and it would be class M — contradicting the assignment to class C.

**The table is WRONG for beta-gamma.** The claimed correspondence "classes G/L/C have p_max = 2 and k_max = 1" fails for class C (betagamma).

### F17 — The dichotomy "finite depth <=> multiplication operators" fails for betagamma (CRITICAL)
**Claim**: Part (i) claims that ALL finite-depth classes (G, L, C) have k_max = 1 and Hamiltonians are multiplication operators.
**Issue**: As shown in F16, betagamma (class C, shadow depth 4) has p_max = 1 among generators, giving k_max = 0. So betagamma does NOT have k_max = 1 — it has k_max = 0. The dichotomy should be:
- Classes G (Heisenberg) and L (affine KM): p_max = 2 among generators, k_max = 1, Hamiltonians are multiplication operators.
- Class C (betagamma): p_max = 1 among generators, k_max = 0, Hamiltonians are zero (trivial).
- Class M (Virasoro, W_N): p_max >= 4, k_max >= 3, Hamiltonians are genuine differential operators.

The corrected dichotomy has THREE tiers (trivial / multiplication / differential), not two (multiplication / differential).

### F18 — Part (iii): Conflation of bar formality with Swiss-cheese formality (MODERATE, AP14)
**Claim**: "classes G/L/C have m_k^{SC} = 0 for k >= 3 on the standard comparison surfaces (Swiss-cheese formality)"
**Issue**: The proof (lines 2042-2058) correctly distinguishes bar formality from Swiss-cheese formality: "this controls the bar formality, not the Swiss-cheese formality." However, it then claims "For classes G/L/C, the OPE pole structure limits the Swiss-cheese operations to depth 1." This is only true for classes G and L. For class C (betagamma), the Swiss-cheese operations m_k^{SC} for k >= 3 are the collision residues at depth >= 2 — but depth >= 2 collision residues require OPE poles of order >= 3 among generators, which betagamma does not have. So betagamma has m_k^{SC} = 0 for k >= 3 by trivial vanishing (no higher poles), not by bar E_2-collapse. The conclusion is correct but the reasoning conflates two mechanisms.

However, the SHADOW DEPTH of betagamma is 4 (class C), and the shadow obstruction tower has nonzero quartic contact invariant. This means there ARE nontrivial A_infinity operations — but they come from NORMAL-ORDERED composites at arity 4, not from higher OPE poles. The Swiss-cheese operations m_k^{SC} in the full sense (including normal-ordered composites, not just OPE poles) may be nonzero for betagamma at k = 3 or k = 4. The proof conflates "OPE pole-driven SC operations" with "all SC operations."

### F19 — Part (i) proof: "all have p_max = 2" is false for Heisenberg (MODERATE)
**Claim**: "Classes G, L, C all have maximal OPE pole order p_max = 2 (Heisenberg: J(z)J(w) ~ k/(z-w)^2; ...)"
**Issue**: Heisenberg has generators J^1, ..., J^n. Their OPE is J^i(z)J^j(w) ~ k*delta^{ij}/(z-w)^2. The maximal pole order among generators is indeed 2. Affine KM also has maximal pole order 2 among generators. But betagamma has maximal pole order 1 among generators (as analyzed in F16). So the claim "all have p_max = 2" is false for betagamma.

### F20 — Compute engine inconsistency with theorem (MODERATE, AP10)
**Claim**: The compute engine theorem_three_paper_intersection_engine.py (line 488) assigns betagamma max_ope_pole = 2.
**Issue**: This hardcodes the same error as the theorem. The engine should have max_ope_pole = 1 for betagamma (among generators). But the engine has max_ope_pole = 2, which is the T-beta/T-gamma pole order, not the beta-gamma generator pole order. This is an AP10 violation: the test encodes the same wrong value as the theorem.

---

## Summary Table

| # | Theorem | Finding | Severity | Class |
|---|---------|---------|----------|-------|
| F1 | DNP (Vol II) | Bar formality / SC formality conflation in proof | MODERATE | AP14 |
| F2 | DNP (Vol II) | Scope mismatch: proof cites affine-scoped theorem for general statement | MODERATE | AP7 |
| F3 | DNP (Vol II) | Twisting morphism vs r-matrix coordinate change glossed | MINOR | editorial |
| F4 | DNP (Vol II) | Koszulness hypothesis may be overly restrictive | MINOR | AP7 |
| F5 | GZ26 | Translation-invariance assumption unstated | MODERATE | hidden hypothesis |
| F6 | GZ26 | Depth-3 Virasoro term "acts trivially" unjustified | MODERATE | proof gap |
| F7 | GZ26 | Part (v) mixes proved content with unverified comparison | MODERATE | AP40-adj |
| F8 | Gaudin-Yangian | FFR94 attribution correct | OK | — |
| F9 | Gaudin-Yangian | 1/(k+h^v) prefactor relies on reference | MODERATE | proof-by-ref |
| F10 | Gaudin-Yangian | "Higher Gaudin" not formally defined | MODERATE | AP43-adj |
| F11 | Gaudin-Yangian | Classical limit correct | OK | — |
| F12 | Sklyanin | Parts (i)-(ii) are known results tagged ProvedHere | SERIOUS | AP40 |
| F13 | Sklyanin | Coproduct formula schematic, not precise | MODERATE | imprecision |
| F14 | KZ bridge | Synthesis theorem of established results | MODERATE | legitimate |
| F15 | KZ bridge | Gauge invariance = Jacobi conflates geometric/algebraic | MODERATE | AP42 |
| F16 | Depth/order | **betagamma p_max is 1, not 2: TABLE WRONG** | **CRITICAL** | AP3/AP9 |
| F17 | Depth/order | **Dichotomy fails for class C: three tiers, not two** | **CRITICAL** | AP7 |
| F18 | Depth/order | SC formality mechanism confused for class C | MODERATE | AP14 |
| F19 | Depth/order | "All have p_max = 2" false for betagamma | MODERATE | AP3 |
| F20 | Depth/order | Compute engine hardcodes same wrong value | MODERATE | AP10 |

---

## Totals

- **CRITICAL**: 2 (F16, F17 — both in thm:shadow-depth-operator-order)
- **SERIOUS**: 1 (F12 — status inflation in thm:yangian-sklyanin-quantization)
- **MODERATE**: 13
- **MINOR**: 2
- **OK**: 2

---

## Detailed Analysis: The beta-gamma p_max Error (F16-F17)

### The mathematical situation

The beta-gamma system has two generating fields beta (weight lambda) and gamma (weight 1-lambda). Their OPEs among themselves:
- beta(z)gamma(w) ~ 1/(z-w): simple pole (p = 1)
- beta(z)beta(w) ~ 0: no pole (p = 0)
- gamma(z)gamma(w) ~ 0: no pole (p = 0)

The Sugawara energy-momentum tensor T = :(1-lambda)*beta*partial(gamma) - lambda*partial(beta)*gamma: is a COMPOSITE (weight 2, not a generator). Its OPE with generators:
- T(z)beta(w) ~ lambda*beta/(z-w)^2 + partial(beta)/(z-w): double pole (p = 2)
- T(z)gamma(w) ~ (1-lambda)*gamma/(z-w)^2 + partial(gamma)/(z-w): double pole (p = 2)
- T(z)T(w) ~ (c/2)/(z-w)^4 + 2T/(z-w)^2 + partial(T)/(z-w): quartic pole (p = 4)
where c = -2(6*lambda^2 - 6*lambda + 1).

### What p_max should be

The theorem defines p_max "among generating fields." By this definition:
- p_max(betagamma) = 1

The bar complex is built from GENERATORS. The collision residues in the bar differential come from the OPEs of generators. For betagamma, the only nonzero collision residue is from the simple-pole beta-gamma OPE, and d log absorption makes this a zero-order (constant) collision residue. This means:
- k_max(betagamma) = 0
- The collision residue r(z) = 0 (confirmed in beta_gamma.tex, line 96-100: "The collision-residue r-matrix vanishes")

### Resolution

The theorem should either:
1. Redefine p_max to include composite fields (in which case betagamma gets p_max = 4 and moves to class M), or
2. Remove betagamma from the "classes G/L/C all have p_max = 2" claim and note it as a special case, or
3. Introduce a more refined notion that accounts for the fact that betagamma's shadow depth comes from normal-ordered composites, not from generator OPE poles.

The most honest resolution is option (2) or (3). The shadow depth classification (G/L/C/M) is NOT controlled by the generator OPE pole order alone. The betagamma system proves this: it has shadow depth 4 (class C) but generator p_max = 1. The quartic contact shadow comes from arity-4 graph sums involving normal-ordered composites, not from quartic OPE poles.

### Cross-check with the manuscript's own statements

beta_gamma.tex, lines 96-100: "The collision-residue r-matrix vanishes: the betagamma OPE beta(z)gamma(w) ~ 1/(z-w) has only a simple pole, which is absorbed by d log extraction. The leading nontrivial interaction datum is the quartic contact shadow, not the r-matrix."

This CONFIRMS that k_max = 0 for betagamma. The existing manuscript text contradicts the new theorem's table.

thqg_holographic_reconstruction.tex, lines 762-764: "The betagamma system has OPE beta(z)gamma(w) ~ 1/(z-w)."

The compute engine (line 488) hardcodes max_ope_pole = 2 for betagamma, propagating the error (AP10).

---

## Recommendations

1. **F16/F17 (CRITICAL)**: Correct the betagamma row in the table. The corrected table should be:

   | Family | Class | p_max | k_max | Operator order |
   |--------|-------|-------|-------|----------------|
   | Heisenberg | G | 2 | 1 | 0 |
   | affine KM | L | 2 | 1 | 0 |
   | betagamma | C | 1 | 0 | trivial (no Hamiltonians) |
   | Virasoro | M | 4 | 3 | 1 |
   | W_3 | M | 6 | 5 | 4 |
   | W_N | M | 2N | 2N-1 | 2N-2 |

   The dichotomy should be restated as a TRICHOTOMY: (a) trivial (k_max = 0, no collision residues, class C/betagamma), (b) multiplication operators (k_max = 1, classes G/L), (c) differential operators (k_max >= 3, class M). Or alternatively, if the theorem wants a clean dichotomy, restrict to algebras with nontrivial collision residue r-matrix (r(z) != 0), which excludes betagamma.

2. **F12 (SERIOUS)**: Downgrade parts (i)-(ii) of thm:yangian-sklyanin-quantization from ProvedHere to ProvedElsewhere, or restructure as: "Proposition (Drinfeld, STS) + Remark (normalization identification)."

3. **F20**: Fix the compute engine to have max_ope_pole = 1 for betagamma.

4. **All other findings**: Address at next editorial pass.
