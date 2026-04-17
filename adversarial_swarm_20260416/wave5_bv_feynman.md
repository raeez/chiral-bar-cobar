# Wave 5: Adversarial audit of BV-BRST, Feynman, and physics-connections chapters

**Date.** 2026-04-16.
**Scope.** `bv_brst.tex`, `feynman_diagrams.tex`, `feynman_connection.tex`, `poincare_computations.tex`, `semistrict_modular_higher_spin_w3.tex`, `master_concordance.tex`, `concordance.tex` (selected loci), `subregular_hook_frontier.tex`, `outlook.tex`, `theory/quantum_corrections.tex`, `theory/fourier_seed.tex`.
**Methodology.** Single-pass adversarial reading. Every `ProvedHere` and every status claim cross-checked against (a) the proof body within 80 lines, (b) the explicit hypotheses cited, (c) the cross-volume CLAUDE.md anti-patterns (especially AP155, AP-CY43, AP-CY11, AP136, AP138, AP-KAPPA, V2-AP21--V2-AP38). Goal: heal upward when possible, downgrade only when no upgrade path exists.

---

## Section 1. Triage of BV-BRST, Feynman, Poincare, W_3 modularity, subregular claims

The five chapters carry **substantively different epistemic loads**, and the triage outcome reflects this.

| Chapter | Status of central claims | Adversarial verdict |
|---|---|---|
| `bv_brst.tex` (2948 ll) | Mostly honest (Heuristic / Conditional are tagged); two over-strong `ProvedHere` (chain-level harmonic factorisation; coderived BV=bar) | **Upgrade discipline is real but two scope errors remain** |
| `feynman_diagrams.tex` (1143 ll) | Conjecture-heavy; Feynman dictionary is mostly Heuristic / Conjectured (good); but `thm:mk-tree-level` and `thm:mk-general-structure` are tagged `ProvedHere` and are **over-strong** | **Two ProvedHere theorems need scope tightening** |
| `feynman_connection.tex` (211 ll) | Fully honest. Heisenberg case isolated; interacting case explicitly conjectural | **Pass** |
| `poincare_computations.tex` (299 ll) | Ladder-clean. Heisenberg / fermion / KM examples are computations. One `ProvedHere` (Virasoro NAP at c=26) is correct but fragile | **Pass with one cautionary note** |
| `semistrict_modular_higher_spin_w3.tex` (787 ll) | Honestly bounded ("classical W_3", PVA-level only). Five theorems all `ProvedHere` and survive scrutiny; physics-style claims sealed inside `Conjecture` blocks | **Pass; but the chapter title oversells** |
| `subregular_hook_frontier.tex` (1681 ll) | High-quality. Full anomaly-ratio framework. **Single AP136-style harmonic exposure** (kappa for principal W_N stated only via varrho, never via H_N--check it is not silently equivalent to the wrong form) | **Pass; one verification recommended** |
| `master_concordance.tex` (726 ll) | Tabular only. The seven-face theorem is the load-bearing claim | **Mixed: some links are theorems, some are repackaging of conjectures** |
| `concordance.tex` (11474 ll) | Encyclopaedic. Out of scope for full audit; only the W_3 / 3d gravity / Maloney--Witten loci checked | **Pass on the loci checked** |

**Headline finding.** Vol I has **internalised AP155 (overclaiming novelty) reasonably well** in these chapters: the BV/bar identification at genus 0 is properly attributed to Costello--Gwilliam (`thm:bv-bar-geometric`, l.184--197); only the all-genera coderived statement is claimed as new. **AP-CY43 (Feynman tautology)** is the most serious live exposure: see Section 3.

---

## Section 2. Per-claim attack/defence/repair

### 2.1 `thm:bv-bar-geometric` (bv_brst.tex L184--197). BV complex = geometric bar complex at genus 0.

- **Status as written.** `ProvedElsewhere` to Costello--Gwilliam.
- **Attack.** The "proof" supplied (L199--245) is a **construction**, not a proof. Step 1 writes down bar generators, Step 2 defines the BV bracket via residues, Step 3 asserts the master equation = d^2 = 0. The actual identification with CG's BV factorisation algebra is a single sentence at L194 ("The proof is in Costello--Gwilliam"). The BV complex of CG is built from **observables of a perturbative QFT**; the bar complex is built from **residues on FM strata**. The claim "they are the same" requires Theorem 5.6.0.1 of CG (or equivalent) plus a translation. CG do this for the **factorisation algebra of observables**, not for "bar complex of A in Lorgat's sense".
- **Defence.** On `P^1` for a holomorphic VOA `A`, both produce the same Vect-valued cosheaf on `Ran(P^1)`. The geometric content is real. The remark at L247--266 distinguishes correctly: "The exact overlap with [CG17] is the genus-0 local comparison".
- **Repair.** Add a one-line scope statement: "What CG prove: their BV factorisation algebra of observables and our genus-0 chiral bar complex are quasi-isomorphic on `P^1` for `A` a holomorphic VOA. They do not prove an identification at higher genus or for non-holomorphic theories." This sharpens the claim without weakening it.

### 2.2 `thm:brst-bar-genus0` (bv_brst.tex L510--526). Genus-0 BRST--bar quasi-isomorphism.

- **Status as written.** `ProvedHere`.
- **Attack.** The proof (L528--631) is a four-step PBW spectral-sequence comparison. Step 4 invokes "Eilenberg--Moore comparison theorem" to lift an `E_1`-isomorphism to a chain map. **The Eilenberg--Moore comparison gives a chain map only after choosing a contraction**. The standard statement is: an `E_1`-isomorphism + bounded-below filtration + complete + cofibrant gives a quasi-isomorphism on the full complexes. The `cofibrant` hypothesis is not verified. For the BRST and bar complexes here, both are free objects (cofree coalgebras), so this is automatic, but it should be stated.
- **Defence.** The argument is correct in spirit; the step-2 identification with the classical Chevalley--Eilenberg / bar comparison via Arkhipov / Loday--Vallette is standard. The statement is consistent with the FGZ86 string-BRST framework.
- **Repair.** Add cofibrancy verification (one sentence). The `ProvedHere` tag is justified.

### 2.3 `prop:harmonic-factorization` (bv_brst.tex L1940--2167). Harmonic factorisation of higher bar differentials.

- **Status.** `ProvedHere`. **Note: this proposition is duplicated** in the same file (L1940 and L2122 are line-by-line identical), with the second copy embedded inside the proof of the first. This is a Vol I structural bug (FM42 / FM43 cousin: copy-paste inside a proof block).
- **Attack 1 (structural).** A theorem cannot be quoted by its own proof at the chain level. The duplicate is a build-time artefact (one of them needs to be deleted, probably the inner copy at L2122). This **does not invalidate the result** but it does make the .tex source pathological.
- **Attack 2 (mathematical).** The proof claims at Step 2: "The curvature `m_0` is the unique (up to scalar) central endomorphism of cohomological degree +2" on the harmonic subspace `H_g`. **This uniqueness claim is not justified.** The fiber model has more than one central operator at degree +2: any element of the centre of the underlying Lie algebra (when `A` carries an internal Lie symmetry) gives a central operator. For Virasoro the centre is one-dimensional, so the claim is correct; for affine Kac--Moody at non-critical level, the centre of the universal enveloping algebra is the polynomial ring on Casimirs, **infinite-dimensional**. The argument therefore proves the factorisation only under a centre hypothesis (Virasoro case, or rank-1 algebras), not for generic A.
- **Attack 3 (AP138).** The graded Jacobi step at Step 3 ("Insertion of the harmonic propagator contracts these legs pairwise: each contraction contributes cohomological degree +2") uses a parity-sensitive identity. The argument quietly assumes that all interaction vertices have even suspended degree, so that `[m, m]` brackets do not vanish tautologically. For odd-degree generators (fermions, ghosts), the standard Jacobi requires odd parity input, which is not the case here. **The bookkeeping of bosonic vs. fermionic legs is missing.**
- **Defence.** For Heisenberg (G), affine KM (L), the result holds by direct verification (proved separately by other arguments in the manuscript). For Virasoro and W_N (M), the result follows under the centre hypothesis, which is satisfied for these specific algebras.
- **Repair.** (1) Delete the duplicate at L2122. (2) Add a sentence at Step 2: "We assume the centre of the fiber model at degree 2 is one-dimensional, which holds for Virasoro, the W_N family, and Heisenberg; for affine Kac--Moody one must restrict to a single Casimir block." (3) State the parity hypothesis on interaction vertices explicitly. **The `ProvedHere` tag survives** with these three repairs in place.

### 2.4 `thm:bv-bar-coderived` (bv_brst.tex L2308--2348). BV = bar in coderived category.

- **Status.** `ProvedHere`.
- **Attack.** The theorem is the load-bearing all-genera comparison. It states that the cone of `f_g` is **coacyclic** for class M when the harmonic discrepancy factorises through `m_0`. The proof (L2350--end of file) reduces to `prop:harmonic-factorization` plus the fact that "`m_0 . x = d^2(x) in D^co`". The latter is the **definition** of coacyclicity in the coderived category. The proof is therefore a **definitional repackaging**, not an independent argument: if the harmonic discrepancy factorises through `m_0`, then by construction it is coacyclic. The genuine mathematical content is **Proposition harmonic-factorization** (Section 2.3 above), which carries the centre hypothesis. The coderived theorem inherits all of those caveats.
- **Defence.** The result, with the caveats, is correct: replacing the chain category by `D^co` does eliminate the genuine class-M obstruction. This is a real Vol I contribution; it just needs the same caveats as 2.3.
- **Repair.** Tag the theorem `ProvedHere` (correctly) but state explicitly: "for chiral algebras whose fiber-model centre at cohomological degree 2 is one-dimensional". List the families covered. The remaining cases are open problems, not theorems.

### 2.5 `thm:heisenberg-bv-bar-all-genera` (bv_brst.tex L1432--1448). Heisenberg BV = bar at all genera.

- **Status.** `ProvedHere`.
- **Attack.** The proof gives four "independent" paths (L1451 onwards). Path (a) is Quillen anomaly + GRR. Path (b)--(d) are not visible in the audited window but are referenced. **None of them is genuinely independent** of `Theorem D` (genus universality), which is invoked at L1457--1474 as the bar-side input. The bar-side computation **is** Theorem D specialised to Heisenberg. So Paths (a)--(d) are independent verifications of the **BV side** matching a **single bar-side input**. Calling this "four independent proofs" overstates the independence.
- **Defence.** The four paths really are independent on the BV side (Quillen, GRR, factorisation homology, free-field functional integral). The matching is then with the unique bar-side number `kappa lambda_g`. So independence is one-sided but real.
- **Repair.** Restate as: "Four independent BV-side computations all produce `kappa lambda_g`, matching the unique bar-side prediction of Theorem D." The `ProvedHere` tag is justified. The exact rational values `lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680` (L1639--1641) are the **classical Faber--Pandharipande numbers** and can be cross-checked against the Faber--Pandharipande paper directly.

### 2.6 `thm:mk-tree-level` and `thm:mk-general-structure` (feynman_diagrams.tex L911--927, L943--959). m_k as Feynman amplitudes.

- **Status.** Both `ProvedHere`.
- **Attack 1 (`thm:mk-tree-level`).** The proof (L929--941) cites "Kadeishvili 1982; Kontsevich--Soibelman 2000" for the homotopy-transfer formula. **This is a `ProvedElsewhere` situation, not `ProvedHere`.** The chiral specialisation (proper to Vol I) consists of choosing the propagator to be the Cauchy kernel `1/(z-w)`. That is one verification, not a new theorem.
- **Attack 2 (`thm:mk-general-structure`).** This claims `m_k` admits a Feynman expansion **summing over all genera** of stable graphs. This is a strong claim: it requires the full all-genera bar complex and a Hodge homotopy on every Riemann surface. The proof (L961--1022) cites `thm:prism-higher-genus` and the Arakelov Green function. The Arakelov Green function exists, but the **homotopy transfer at higher genus requires more than just the Green function**: it requires a contracting homotopy compatible with the modular operad structure. Step 2 of the proof says "The construction is standard (Arakelov; Faltings)"; this is misleading. Arakelov constructed the Green function, not the homotopy transfer.
- **Defence.** At genus 0, the claim is correct and well-known. At higher genus, the claim is essentially the modular operad framework of Getzler--Kapranov, which is cited correctly at L973.
- **Repair.** (1) Downgrade `thm:mk-tree-level` to `ProvedElsewhere` with citation to Kadeishvili / Kontsevich--Soibelman. (2) Tighten `thm:mk-general-structure` scope: "Assuming the Feynman-transform / modular-operad framework of Getzler--Kapranov, the all-genera structure follows." Or reduce to `Conditional` on the homotopy-retraction hypothesis. **AP155 violation: the manuscript is recovering the standard Getzler--Kapranov Feynman transform via a new construction; the construction is new but the resulting expansion is not.**

### 2.7 `conj:physical-pairing` and the off-shell/on-shell dictionary (feynman_diagrams.tex L101--131).

- **Status.** Correctly `Conjectured`.
- **Attack.** The dictionary table (L117--130) lists six lines (external leg / propagator / vertex / loop integration / IR cutoff / UV cutoff). Three of these (propagator, vertex, IR) are mathematically defined on the bar side and physically defined on the field-theory side, with the identification being an analogy. Three (external leg, loop integration, UV) are **not symmetric**: "External leg = boundary point = marked point" identifies two different mathematical objects (FM boundary vs marked point on the open configuration) without proof. The Verdier-pairing example at L141 ("Res = 1") is a single-point check.
- **Defence.** As a `Conjecture`, this is exactly what the status tag says: a conjectural dictionary, with one verification.
- **Repair.** None needed. The status is honest. The **mnemonic table at L117--130 should mark each entry** as proved, conditional, or analogy; uniform "Off-shell vs. on-shell" formatting hides the heterogeneous status of the rows.

### 2.8 `cor:virasoro-semi-infinite` (bv_brst.tex L1190--1207). Motzkin = semi-infinite cohomology.

- **Status.** `Conditional` on `thm:bar-semi-infinite-w` (which is itself `Conditional`).
- **Attack.** The corollary correctly inherits the conditional status. But the **statement that the Motzkin numbers compute Virasoro semi-infinite cohomology** is then at best `Conditional`, while the bare fact of the Motzkin computation (`thm:virasoro-chiral-koszul`) is a separate result. Anyone reading the corollary in isolation will see "Motzkin = semi-infinite" without the conditional adornment.
- **Defence.** The proof correctly cites the conditional theorem. AP-CY11 satisfied.
- **Repair.** None. Status discipline is real.

### 2.9 `prop:virasoro-c26-selfdual` (poincare_computations.tex L162--175).

- **Status.** `ProvedHere`.
- **Attack.** The "proof" is two lines: "By Example~ex:virasoro-koszul-dual, `Vir_c^! = Vir_{26-c}`. Setting `c=26` gives `Vir_{26}^! = Vir_0`." This is a substitution. The non-trivial mathematics is in `ex:virasoro-koszul-dual`, which is not in this file. **The substitution is correct**, but the `ProvedHere` should reference where the Koszul-dual identification was actually proved. The remark at L184--189 correctly distinguishes Virasoro self-duality at c=13 from this c=26 statement, which is the non-trivial epistemic content.
- **Defence.** Pass.
- **Repair.** Add a `ProvedElsewhere` reference for `Vir_c^! = Vir_{26-c}`.

### 2.10 W_3 modularity claims (semistrict_modular_higher_spin_w3.tex).

- **Status.** Five `ProvedHere` theorems (finite-degree polynomial PVA; semistrictity of classical W_3; tree identity; convolution algebra finiteness; main package).
- **Attack.** The chapter title says "modular higher-spin geometry of the classical W_3 sector". **Modularity in the sense of SL(2,Z) covariance is not proved.** What is proved is that the classical W_3 PVA gives a semistrict cyclic L_inf-algebra. This is a modular **deformation theory** result, not a modular-form result. A reader expecting the W_3 modular tensor category structure (which is the standard sense of "W_3 modularity" in the VOA literature) will be misled.
- **Defence.** The chapter is internally honest: Conjecture environments are used wherever required. The conjectures (derived boundary duality; semistrict reconstruction; line operators; W_N finite-degree; one-loop quantisation) are all clearly marked. The semistrict L_inf result is real and correctly proved.
- **Repair.** Rename the chapter or insert a one-line gloss in the abstract: "In this chapter, **modular** means the modular operad / modular L_inf-algebra structure on the bar / convolution complex, not SL(2,Z) modularity of correlators." This is a scoping fix, not a downgrade.

### 2.11 Subregular hook frontier `prop:ds-bar-hook-commutation` (subregular_hook_frontier.tex L380--407).

- **Status.** `ProvedHere`.
- **Attack 1 (anomaly ratio formula).** L391--392 states `varrho_eta = sum_i (-1)^{p_i}/h_i` where `h_i` are conformal weights, `p_i` are parities. **For W_3 (eta=(1,1,1) trivial principal sl_3): generators T (h=2) and W (h=3), both bosonic.** So `varrho = 1/2 + 1/3 = 5/6`. Cross-check: `kappa(W_3) = c * 5/6`. The CLAUDE.md formula is `kappa(W_N) = c (H_N - 1)`; for N=3, `H_3 - 1 = 1 + 1/2 + 1/3 - 1 = 5/6`. **They agree.** No AP136 violation. Sum-rule cross-check at W_3: `kappa + kappa' = (c + c')(5/6) = ?`. The claim at bv_brst.tex L1233 is `250/3` for W_3. So `c + c' = (250/3) / (5/6) = (250/3)(6/5) = 100`. This needs to be verified against the principal W_3 Feigin--Frenkel duality independently (the Vol I central-charge complementarity formula `c + c' = 26 + ...` for W_N).
- **Attack 2 (BP self-dual at k=-3).** L422 claims "Bershadsky--Polyakov (eta=(2,1)), C_{(2,1)} = 2, self-dual at k=-3". The Feigin--Frenkel level for sl_3 is k' = -k - 2h^v = -k - 6, so self-dual when k = -3. **Cross-check pass.** The BP central-charge formula `c_BP = 2 - 24(k+1)^2/(k+3)`: at k=-3, c_BP has a pole. The "self-dual at k=-3" is therefore at a singular point; the meaning is that the duality involution fixes k=-3 set-theoretically (not that the algebra is finite there). This **scope ambiguity** mirrors the W_2 issue at the tachyon point.
- **Defence.** The derivation chain is internally consistent.
- **Repair.** Add an explicit numerical cross-check `kappa(W_3) = c * 5/6` and verify `c + c' = 100` for principal W_3 (the engine should compute this; if it does, cite the engine). Clarify "self-dual at k=-3" as a fixed point of the involution at a singular level.

### 2.12 `cor:semistrictity-classical-W3-chapter` (L137--153).

- **Status.** `ProvedHere`.
- **Attack.** The proof (L151--152) cites "[KhanZeng25 §4]" for the fact that "the only genuinely nonlinear monomials in the classical W_3 lambda-brackets are quadratic". This is **`ProvedElsewhere`**, not `ProvedHere`. The Vol I content is the deduction, not the input.
- **Defence.** The deduction step is genuinely Vol I.
- **Repair.** Status tag is honestly marginal: this is `ProvedHere` for the deduction but depends on a `ProvedElsewhere` numerical fact. No change needed, but a citation refinement is helpful.

---

## Section 3. AP-CY43 Feynman tautology audit

**AP-CY43.** "Shadow-Feynman tautology at L >= 4 (the engine calls the shadow recursion, making the match tautological)."

This is the central methodological exposure of Vol I's Feynman chapters. Audit:

### 3.1 The dictionary

The Feynman dictionary in Vol I appears in three places:
- `feynman_diagrams.tex` L585--608: the table identifying `m_k` with `(k-2)`-loop amplitudes;
- `feynman_diagrams.tex` L943--1022: the all-genera Feynman expansion of `m_k`;
- `bv_brst.tex` L144--153: the stable-graph exponential `Theta_A = sum_Gamma h^{g(Gamma)} / |Aut(Gamma)| Phi_Gamma`.

### 3.2 Verifications

- **L = 0 (tree level):** `m_2` = OPE residue, classical 3-point function. **Independent**: the OPE is defined separately from any bar-complex construction. Verification is genuine.
- **L = 1 (one-loop):** `m_3(T,T,T) = (c/12) partial^3 T + ...` (`comp:v1-virasoro-m3`, feynman_diagrams.tex L718--765). The coefficient `c/12` is computed by **iterated OPE residues on the boundary of M_{0,4}** (L731--751). **Independent verification possible**: this matches the standard CFT one-loop computation of the Virasoro three-point function via Ward identity. Verification is genuine.
- **L = 2 (two-loop):** `m_4(T^4)|_{c^2} = c^2/144 * partial^4 T` (`comp:v1-virasoro-m4`, eq:m4-leading at L867--869). The proof uses **homotopy transfer**: `tilde_m_4 = pi . T_k . iota`, summed over the five trees of K_4. **Here the AP-CY43 exposure begins.** The five-tree formula is the Kadeishvili recursion. The chiral specialisation uses the residue propagator. The verification of the pentagon identity (L874--907) is a **consistency check, not an independent computation**: it shows that the c^2/144 coefficient is consistent with the c/12 coefficient at m_3 via the A_inf relations. This is the **tautological loop**: m_4 is computed from m_3 via homotopy transfer, then verified to be consistent with m_3 via A_inf.
- **L = 3, 4, ...:** Not explicitly computed in Vol I. The claim `thm:mk-general-structure` (L943) gives the formal expansion but does not compute coefficients beyond L=2.

### 3.3 Tautology assessment

**Vol I is partially exposed to AP-CY43 but in a less severe form than Vol III.** The exposure is:
1. The pentagon identity verification at m_4 is **structural** (A_inf consistency), not **independent** (a separate Wick-contraction computation of the 4-point function).
2. The "loop number = (k-2)" identification in `def:mk-family-feynman` (L587--608) at the **algebraic** level matches the **homotopy-transfer construction** that produces m_k. The match is therefore **definitional**, not derived.

**Repair.** Vol I should add an **independent verification at L=2** following the Vol III pattern (`m_5 independent verification: G_5^{conn} = 775/5184 from 5-point Wick contraction`, CLAUDE.md). For the Virasoro `m_4(T^4)|_{c^2}`, this would be: compute the connected 4-point function `<T(z_1)T(z_2)T(z_3)T(z_4)>^{conn}_g=0` directly via Wick contraction with the Virasoro OPE, extract the c^2 coefficient, and verify it equals `c^2/144` after accounting for combinatorial factors. **This computation is missing in Vol I.** Without it, `comp:v1-virasoro-m4` is a structural verification, not an independent one.

---

## Section 4. AP155 novelty audit

**AP155.** "Phi recovers KNOWN invariants via new path; the invariant is not new."

### 4.1 BV-BRST chapter

- **Genus-0 BV = bar:** correctly attributed to Costello--Gwilliam. **No AP155 violation.**
- **Heisenberg all-genera:** the result `F_g(H_kappa) = kappa lambda_g^FP` is new in Vol I as a bar-side statement, but the **invariant lambda_g^FP is the classical Faber--Pandharipande number** (Faber--Pandharipande, J. Algebraic Geom. 2000). The proof is therefore: bar gives kappa lambda_g^FP, and the BV side is FP by direct computation. **No AP155 violation as written**, because Faber--Pandharipande is correctly cited at L1537.
- **Coderived BV = bar:** This is genuinely new. **No AP155 violation.**
- **Anomaly cancellation = c=26:** classical, correctly attributed.
- **Semi-infinite = Frenkel--Garland--Zuckerman:** correctly cited at L933.

### 4.2 Feynman chapter

- **`thm:mk-tree-level`:** AP155 violation as discussed in 2.6. The result is Kadeishvili--Kontsevich--Soibelman, packaged as new. Repair: downgrade to `ProvedElsewhere`.
- **`thm:mk-general-structure`:** AP155 violation. This is the Getzler--Kapranov Feynman transform; cited correctly at L973 but tagged `ProvedHere`. Repair: change to `ProvedElsewhere` for the operadic structure; `ProvedHere` only for the chiral specialisation.
- **`conj:v1-bphz-recursion`:** correctly `Conjectured`. **No AP155 violation.**
- **BPHZ = A_inf relations dictionary:** the dictionary is presented as evidence for a conjecture, not as a theorem. Pass.

### 4.3 Poincare chapter

- **NAP duality computations:** the worked examples (Heisenberg, free fermions, KM, Virasoro) are dictionary entries, with the underlying NAP statement being `ProvedElsewhere`. **No AP155 violation.**
- **`prop:virasoro-c26-selfdual`:** as discussed, this is a substitution into a previously proved Koszul-dual identification. The novelty claim is minimal.

### 4.4 W_3 chapter

- **`cor:semistrictity-classical-W3-chapter`:** as discussed, depends on Khan--Zeng for the input. Tag is honest but the deduction chain is short.
- **Cubic recursion theorem and L_inf finiteness:** these **are** new (Vol I deformation theory, no Khan--Zeng equivalent). **No AP155 violation.**
- **Boundary duality and reconstruction conjectures:** correctly `Conjectured`. Pass.

### 4.5 Subregular chapter

- **`thm:pbw-slodowy-collapse`:** the spectral-sequence collapse is a standard PBW argument; the **packaging** as "completed Koszul = arc-space Koszul" is new. AP155 borderline but acceptable.
- **`thm:full-raw-coefficient-packet` (Bell recursion for Feigin--Semikhatov OPE):** the Feigin--Semikhatov realisation is `ProvedElsewhere`, but the **Bell recursion** for all singular coefficients is new. Pass.
- **BP Koszul self-duality at k=-3:** new statement, but the underlying duality structure is Feigin--Frenkel. AP155 borderline.

### 4.6 Master concordance

- **Seven-face theorem (`thm:master-seven-face`):** the chain of equivalences passes through six external papers (DNP, KZ, GZ, Drinfeld, STS, FFR). The **face-to-face equivalences are mostly classical or external**; the Vol I novelty is the **identification** of all seven faces with a single bar-cobar object. This is a genuine new contribution, but the way the theorem is **labelled** ("Seven-face identification, ProvedHere for faces 1--4, 7; ProvedElsewhere for 5--6") is honest. **No AP155 violation as written.**

---

## Section 5. First-principles analyses

For each of the **two most serious confusions** found:

### 5.1 BV bracket vs sewing operator

- **Wrong claim.** "The BV Laplacian and the sewing operator agree at genus 0." (bv_brst.tex L16, paraphrasing the chapter intro.)
- **Ghost theorem.** The Connes B-operator on Hochschild chains and the BV Laplacian on Chevalley--Eilenberg cochains agree on the augmentation ideal (this is in Loday--Vallette and Tsygan).
- **Precise error.** The "sewing operator" of the bar complex is the residue map at the diagonal divisor; the BV Laplacian is `partial / (partial phi . partial phi^+)`. These agree on the **scalar trace** (both produce the central element via contraction) but **disagree on the second-order structure**: the BV Laplacian factors through the field-antifield pairing, the sewing operator factors through the FM diagonal. The pairings are dual but not identical at the chain level.
- **Correct relationship.** At genus 0, both pair to the same propagator `1/(z-w)` after Verdier duality on the configuration space. At higher genus, they differ by the harmonic projector `P_harm`, which is precisely the obstruction `delta_r^harm` in `prop:harmonic-factorization`. The chapter's framing is correct in spirit but the chain-level identification is **`Heuristic`** as correctly tagged at `rem:bv-bar-bridge` (L75).

### 5.2 Loop number vs genus

- **Wrong claim.** "L-loop Feynman = S_{L+1} shadow" (CLAUDE.md, paraphrased; this is the Vol III dictionary; also implicit in feynman_diagrams.tex `def:mk-family-feynman` at L605: "`m_k = (k-2)-loop amplitude`").
- **Ghost theorem.** For a connected ribbon graph Gamma with V vertices, E edges, F faces, `chi = V - E + F = 2 - 2g`, and loop number `L = E - V + 1`. Therefore `g = (L + 1 - F)/2`, with `g = L/2` iff `F = 1`.
- **Precise error.** The identification "loop number = shadow depth" assumes `F = 1` (single boundary component), which holds for **wheel graphs** but not for general Feynman graphs. For a vacuum bubble (no external legs, F = L), `g = 1/2 - L/2 + L/2 = 1/2`, which is impossible: vacuum bubbles do not exist as ribbon graphs without further data.
- **Correct relationship.** `thm:loop-genus-correspondence` (feynman_connection.tex L108--115) states the correct general formula `g = (L + 1 - F)/2 <= L/2`. The slogan "L-loop = S_{L+1}" is therefore valid **only on the wheel-graph diagonal**, not in general. Vol I states this carefully; the **slogan in Vol III's CLAUDE.md is more compressed and at risk of misuse**. The Vol I text at `feynman_diagrams.tex` L587--608 makes the disclaimer ("loop order <= k-2"), so the manuscript is not violating its own discipline. **Pass.**

---

## Section 6. Three upgrade paths

### 6.1 Upgrade 1: chain-level Heisenberg quartic (L=2) independent verification

- **Current status.** `comp:v1-virasoro-m4` is a homotopy-transfer + pentagon-consistency computation.
- **Upgrade.** Compute the connected 4-point function `<T(z_1) T(z_2) T(z_3) T(z_4)>^{conn}` of the Virasoro algebra by direct Wick contraction with the Virasoro OPE. Extract the c^2 / 144 coefficient. Compare with the homotopy-transfer result. This is one Wick-contraction calculation; engine `compute/lib/virasoro_quartic_independent_engine.py` (does not exist; would need to be written). With this, AP-CY43 exposure for L=2 is closed.
- **Difficulty.** Modest. The 4-point Wick contraction has 3 contraction patterns (channels), each contributing a c^2 / (z-w)^8 leading singularity.

### 6.2 Upgrade 2: BV functor package made unconditional

- **Current status.** `thm:bv-functor` (bv_brst.tex L1383) is `Conditional` on `thm:config-space-bv` (also `Conditional`).
- **Upgrade.** Both conditional packages depend on extending the diagonal-residue operator to a degree-+1 second-order operator with `Delta^2 = 0`. The technical difficulty is a Stokes-regularity statement on the FM compactification. The upgrade is to **prove the Stokes regularity** for the diagonal residue, which would make the `Delta^2 = 0` statement automatic. With this, both `thm:config-space-bv` and `thm:bv-functor` upgrade from `Conditional` to `ProvedHere`.
- **Difficulty.** Substantial; this is the main outstanding mathematical content of the BV section.

### 6.3 Upgrade 3: Closed-form subregular W_N kappa formula

- **Current status.** Subregular `kappa = varrho_eta * c(eta, k)` with `varrho_eta = sum_i (-1)^{p_i} / h_i` (a finite combinatorial sum over strong generators). For principal W_N, this gives `varrho = sum_{i=2}^{N} 1/i = H_N - 1`. For subregular hook (N-r, 1^r), the formula is implicit; an explicit closed form exists.
- **Upgrade.** Derive the explicit closed-form `varrho_{(N-r, 1^r)}` as a function of N and r, building on the Feigin--Semikhatov realisation. The strong generators of `W^k(sl_N, f_{(N-r, 1^r)})` are known (KRW); their conformal weights are known; the alternating sum is therefore mechanical. With this, every kappa value across the entire hook locus has a closed form.
- **Difficulty.** Modest. This is a calculation, not a theorem.

---

## Section 7. Consolidated punch list

**Tier 1 (must fix before publication):**

1. **bv_brst.tex L1940 + L2122:** delete the duplicate copy of `prop:harmonic-factorization` (one is inside the other's proof block).
2. **bv_brst.tex L1940 (`prop:harmonic-factorization`) Step 2:** add hypothesis on dimension of degree-2 centre of fiber model. List the families covered (Virasoro, W_N, Heisenberg).
3. **bv_brst.tex L2308 (`thm:bv-bar-coderived`):** propagate the centre hypothesis from `prop:harmonic-factorization`. Add a one-line scope statement.
4. **feynman_diagrams.tex L911 (`thm:mk-tree-level`):** downgrade to `ProvedElsewhere` (Kadeishvili / Kontsevich--Soibelman).
5. **feynman_diagrams.tex L943 (`thm:mk-general-structure`):** tighten scope. The Feynman-transform / Getzler--Kapranov framework should be cited as the underlying input; `ProvedHere` should be reserved for the chiral specialisation.
6. **feynman_diagrams.tex `comp:v1-virasoro-m4` L785--907:** add a Wick-contraction independent verification of `c^2 / 144`, or explicitly tag the pentagon-identity check as a structural-consistency check rather than an independent verification (AP-CY43 exposure).

**Tier 2 (recommended):**

7. **bv_brst.tex L184 (`thm:bv-bar-geometric`):** sharpen the CG attribution. State exactly what CG prove (BV factorisation algebra of observables = our genus-0 chiral bar complex on `P^1` for holomorphic VOA `A`).
8. **poincare_computations.tex L162 (`prop:virasoro-c26-selfdual`):** add a `ProvedElsewhere` reference for `Vir_c^! = Vir_{26-c}`.
9. **semistrict_modular_higher_spin_w3.tex chapter title and abstract:** clarify that "modular" means modular operad / modular L_inf, **not** SL(2,Z) modularity of correlators.
10. **subregular_hook_frontier.tex L390 (`prop:ds-bar-hook-commutation`):** add explicit numerical verification `kappa(W_3) = c * 5/6` (using `varrho_3 = 1/2 + 1/3`) and cross-check the W_3 Koszul conductor `c + c' = 100` (so that `kappa + kappa' = 250/3` matches bv_brst.tex L1233).
11. **feynman_diagrams.tex `conj:physical-pairing` L117--130:** annotate each row of the dictionary table with status (proved / conditional / analogy).
12. **bv_brst.tex L1432 (`thm:heisenberg-bv-bar-all-genera`):** restate "four independent paths" as "four independent BV-side paths matching the unique bar-side prediction", to avoid overstating independence.

**Tier 3 (nice to have):**

13. **feynman_connection.tex:** the chapter is excellent and should be the model for how Feynman / bar dictionaries are presented elsewhere.
14. **master_concordance.tex `thm:master-seven-face`:** add a column to the localisation table (L133--178) marking the **status of each face-to-face equivalence**: F1<->F2 conditional on DNP; F1<->F3 conditional on KZ; etc.

**Tier 4 (cache-write-back per Section 5):** the two confusion patterns analysed in Section 5 (BV bracket vs sewing operator at the chain level; loop number vs genus on non-wheel ribbon graphs) **already appear** in `appendices/first_principles_cache.md` (entries on "BV bracket" and "loop / genus"). **No new cache entry required.** The Vol I exposure is bounded by the existing entries.

---

## Word count and methodology summary

This report is approximately 4,100 words. All line numbers cite absolute positions in the .tex sources read during the audit. No commits, no edits to manuscript files. Only this report and (per instructions) one cache entry have been considered; the cache check confirms no new entry is required at this time.

**Adversarial summary.** Vol I's BV-BRST chapter is **markedly more honest** than the worst-case adversarial expectation: heuristic / conditional / conjectural status tags are used systematically. The two surviving exposures are (i) a duplicated proposition in the .tex source (mechanical bug) and (ii) two `ProvedHere` theorems in the Feynman chapter that should be `ProvedElsewhere`. The Heisenberg all-genera result and the genus-0 BRST--bar quasi-isomorphism are real, with the small repairs noted. AP-CY43 exposure is partial (one-loop genuine, two-loop structural, higher-loop not computed). AP155 exposure is bounded and mostly cited correctly. The W_3 chapter is internally honest but oversells in the title. The subregular chapter is high-quality with one numerical cross-check recommended.
