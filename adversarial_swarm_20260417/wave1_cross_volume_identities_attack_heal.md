# Wave 1 Cross-Volume Identities — Beilinson Attack and Heal

**Date.** 2026-04-17.
**Target cluster.** The five cross-volume identities healed in the 2026-04-17 Beilinson rectification: (1) ϱ_A · K(A) two-conductor identity (AP234, B93); (2) super-Yangian max(m,n) complementarity (B86); (3) Kummer-irregular prime retractions (B92); (4) W(p) tempering retraction (B91) and CY-C pentagon stratification (B89/B90); (5) BP polynomial-identity convention split.
**Posture.** Adversarial Beilinson: every claim false until independently verified; prefer a smaller true theorem.

## Attack

### F1. ϱ_A · K(A) identity (AP234 / B93).

**Stated claim.** κ(A) + κ(A^!) = ϱ_A · K(A), with ϱ_N = H_N − 1 for principal W_N, ϱ_KM = ϱ_free = 0, ϱ_BP = 1/6. K_Vir = 26, K_W3 = 100, K_BP = 196.

**Direct numerical check (Vir, W_3, BP).** Using κ_W_N(c) = c·(H_N−1) (canonical census) and the postulated K-values:
- W_2 (=Vir) self-dual c=13: κ + κ^! = 13/2 + 13/2 = 13. ϱ_2 · K = (1/2)·26 = 13. ✓
- W_3 self-dual c=50: κ + κ^! = 5·50/6 + 5·50/6 = 250/3. ϱ_3 · K = (5/6)·100 = 250/3. ✓
- BP: stated ϱ = 1/6, K = 196 → 196/6 = 98/3. Matches the cited self-dual κ+κ^! value. ✓

**F1.a — circularity probe.** The check above is consistent BUT NOT INDEPENDENT: K_Vir = 26 is fixed BY DEMANDING the Feigin–Frenkel involution c ↔ 26−c, and ϱ_2 = 1/2 is then back-derived from κ = c/2. For W_3 the formula K_W3 = 100 reflects c(W_3) + c(W_3^!) = 100 across all c ⟺ Feigin–Frenkel involution c ↔ 100−c; ϱ_3 = 5/6 is forced by κ_W3 = 5c/6. **The identity is therefore a TAUTOLOGY at the level of one-real-parameter principal W_N families: it expresses κ_W_N = c·(H_N−1) and the universality of the Feigin–Frenkel involution, no more.** It is NOT a programme-level new structural theorem; it is a consistency check between two pieces of data already in the census.

**F1.b — BP ϱ = 1/6 derivation.** The 1/6 is NOT 1/6 = (H_N − 1) for any N. It is ad hoc: K_BP = 196 (proved polynomial identity in the Arakawa convention, see §F5 below) and the cited κ + κ^! = 98/3 force ϱ_BP = (98/3)/196 = 1/6. **This is a back-derivation, not a structural derivation.** A structural derivation would identify 1/6 as a Hessian determinant, a Berezinian shift, or a coset central-charge ratio; none is given.

**F1.c — extension to W_4, W_5.** The identity predicts κ_W_4 + κ_W_4^! = (13/12)·K_W_4 and κ_W_5 + κ_W_5^! = (77/60)·K_W_5. **K_W_N for N ≥ 4 has no entry in landscape_census.tex** (verified: see CLAUDE.md "Universal celestial holography" + W_N entries; only N=2,3 K-values are inscribed). Until a primary computation of c(W_N) + c(W_N^!) at the Feigin–Frenkel-involuted level is given for N ≥ 4, the identity is UNTESTED beyond N=3.

**Verdict.** The identity is TRUE but TAUTOLOGICAL on N=2,3 and BP; UNCHECKED on N≥4. The two-K confusion (AP234) is real and the bare equation κ + κ^! = K is false except for the special families where ϱ = 1; but the heal as written promotes a definitional consistency to a "structural identity". **Beilinson surviving form is a definitional remark, not a theorem.**

### F2. Super-Yangian max(m,n) complementarity (B86).

**Stated claim.** κ(Y_ℏ(sl(m|n))) + κ(Y_ℏ(sl(n|m))^!) = max(m,n) at Sugawara-shifted dual level, "verified symbolically at small rank".

**Vol I/II contradiction (already documented in `notes/of6_super_yangian_bridge_draft_2026_04_17.md`).** Vol II super_chiral_yangian.tex Step 3 shows EXPLICITLY that the bare super-trace pairing gives κ + κ^! = 0; the max(m,n) appears ONLY under the Berezinian-normalised pairing via a (1/2)·max(m,n) shift on each side. So at least two distinct pairings coexist:
  - (I) Super-trace pairing ⟨X,Y⟩^str = str(π_def(XY)) → κ + κ^! = 0.
  - (II) Berezinian pairing ⟨X,Y⟩^Ber = sBer(π_def(XY)) → κ + κ^! = max(m,n).

The OF6 draft heals this via a central-automorphism bridge (multiplication by sBer(T(u))|_{u=0}) that shifts shadow depth by exactly (1/2)·max(m,n). **The bridge is correct as a structural statement** but the existing programme inscriptions (`yangians_foundations.tex:67-71`, `programme_overview_platonic.tex:525-539`, Vol II `thm:super-complementarity-max-mn`) DISAGREE on which pairing is canonical; the OF6 draft proposes both are correct and the disagreement is the image of σ_Ber.

**F2.a — independence of the three verification paths.** The OF6 draft claims three disjoint paths: (V1) super-PBW + super-Sugawara; (V2) Nazarov 1991 quantum Berezinian centrality; (V3) Beisert 2007 psl(2|2) AdS/CFT central-extension count. (V1) and (V2) are GENUINELY DISJOINT (super-PBW does not use quasideterminants). (V3) is partially disjoint at psl(2|2) only, where it specialises to a coincidence (max(2,2)=2 matches the count of 3 central elements MINUS the centre rank — this is suspicious). **Beisert's count gives 3 central elements in psl(2|2)⊕C^3, not 2; the agreement with max=2 is via the **rank** of the centre, not the **count**. The disjoint-rationale text in the test-file decorator should be tightened.**

**F2.b — sub-Sugawara line restriction.** The identity holds only on the sub-Sugawara line k + h^v_s ≤ m+n. Above the sub-Sugawara line, super-Sugawara fails (analogous to k = −h^v in non-super case) and the claim is empty. **State this restriction in every cross-volume citation.**

**Verdict.** The bridge lemma is structurally correct; the cross-volume contradiction is healed by recognising the two pairings as σ_Ber-equivalent. The existing wave-1 inscription "verified symbolically at small rank" is too weak to be load-bearing — replace with the explicit Nazarov–Gow centrality argument from the OF6 draft. Beilinson surviving form: lem:super-trace-berezinian-bridge, ProvedHere conditional on the Nazarov–Gow centrality results (which are unconditional theorems).

### F3. Kummer-irregular prime retractions (B92).

**Stated claim.** Primes 1423, 3067, 23, 43, 419 are NOT Kummer-irregular (verified at primary source); they were mis-labelled. Bernoulli-leading first irregular is 691 (B_12); size-leading first is 37 (B_32).

**Direct Bernoulli-numerator check** (computed in this audit, `compute Akiyama–Tanigawa B_2..B_418`):
| p | irregularity window 2k ≤ p−3 | window fully checked? | first hit |
|---|---|---|---|
| 23  | ≤ 20  | YES | none — REGULAR ✓ |
| 37  | ≤ 34  | YES | 2k=32 — IRREGULAR ✓ |
| 43  | ≤ 40  | YES | none — REGULAR ✓ |
| 61  | ≤ 58  | YES | none — REGULAR (new evidence) |
| 193 | ≤ 190 | YES | none — REGULAR ✓ |
| 419 | ≤ 416 | YES | none — REGULAR ✓ |
| 691 | ≤ 688 | partial (≤418) | 2k=12 — IRREGULAR ✓ |
| 811 | ≤ 808 | partial (≤418) | none through B_418 |
| 1423 | ≤ 1420 | partial (≤418) | none through B_418 |
| 2111 | ≤ 2108 | partial (≤418) | none through B_418 |
| 3067 | ≤ 3064 | partial (≤418) | none through B_418 |
| 3617 | ≤ 3614 | partial (≤418) | 2k=16 — IRREGULAR ✓ |

**Verdict.** The retractions of 23, 43, 419 are CORRECT and confirmed at primary source by exhaustive Bernoulli-numerator factorisation through their full Kummer window. 1423 and 3067: the retraction is consistent with all evidence through B_418; full confirmation requires Bernoulli tables to 2k ≈ 3064 (Buhler–Harvey 2011 "Irregular primes to 163 million" exhausts these — primary-source citation should be added). **The "Riccati-arithmetic characteristic primes" relabel is a real invariant** insofar as the S_r numerator denominators of the Virasoro shadow tower do contain these primes (compute_lib structure constants confirm 691 and 3617 enter via shadow_tower_higher_coefficients.tex routes); but the relabelling carries **no independent computational test** distinguishing "Riccati-arithmetic" from "shadow-numerator coincidence". Beilinson surviving form: state the primes as "characteristic primes of the Virasoro Riccati recurrence", drop the Kummer label, cite Buhler–Harvey for the regularity facts.

### F4. W(p) tempering retraction (B91) and CY-C pentagon stratification (B89/B90).

**W(p) sub-claim.** Vol II commit `a5640de` had inscribed thm:tempered-stratum-contains-wp at ProvedHere; audit retracted to Conjectured. The chain "C_2-cofiniteness ⟹ bounded Massey ⟹ tempered" fails because Gurarie 1993 (hep-th/9303160) and Flohr 1996 (hep-th/9605151) construct logarithmic-CFT amplitudes with unbounded Massey products despite finite-dimensional Zhu algebra A(W(p)) of dim 2p (Adamović–Milas).

**F4.a — but the chapter `logarithmic_wp_tempered_analysis_platonic.tex` (read in audit) explicitly heals to TEMPERING via three-channel decomposition.** The chapter chairs (A) attack, (B) heal via Vir + TW + WW channel split each polynomially bounded by Stirling r!^{1/r} ≈ r/e, (C) heal-mode conclusion W(p) IS tempered. Status of `conj:tempered-stratum-contains-wp` in the chapter is CONJECTURAL; status of the `thm:` form retracted by the rectification audit. **There is internal inconsistency between the chapter heal and the audit retraction.** The chapter uses bounded Zhu matrix elements as its load-bearing input; the Gurarie/Flohr counterexamples concern UNBOUNDED Massey products inside CORRELATION FUNCTIONS, not inside Zhu structure constants. **The two arguments are about different objects; the implication "C_2-cofin ⟹ bounded Massey in correlation functions" is not the same as "bounded Massey in shadow-tower structure constants".** The retraction is overcautious. Heal: re-open the question whether shadow-tower-Massey is bounded for W(p), independently of correlation-function Massey.

**CY-C pentagon sub-claim.** The pentagon of five intertwiners R_1..R_5 for G(K3 × E) was claimed to give "six routes converge isomorphically" with κ_ch stratification {3, 12, 24}. Healed: pentagon real, but stratification is generator-rank ρ^{R_i} (rank of intertwiner image inside MMF lattice), not κ_ch.

**F4.b — Hodge-supertrace argument for κ_ch = 0 route-independent.** Direct check: K3 × E has h^{0,0}=1, h^{0,1}=1, h^{0,2}=1, h^{0,3}=1 (Künneth: K3 has h^{0,0}=h^{0,2}=1; E has h^{0,0}=h^{0,1}=1). κ_ch = Σ (-1)^q h^{0,q} = 1 - 1 + 1 - 1 = 0. ✓ Hodge supertrace is route-independent (a classical invariant of the underlying CY); there is no way for any pentagon route to assign nonzero κ_ch. The retraction is unconditional.

**F4.c — is ρ^{R_i} a well-defined invariant or a route-dependent count?** ρ^{R_i} := rank of the intertwiner R_i as a map between two MMF (modular Mathieu form) lattices. Each R_i has a well-defined source/target lattice (per pentagon edge); the rank is therefore canonically attached to the EDGE, not to a route. The stratification {3, 12, 24} is the cardinality of {ranks across the five edges} — this is route-independent. ✓

**Verdict.** W(p) tempering: the rectification's retraction conflates two different Massey objects; chapter's heal is plausible but not verified by primary source. **Open Frontier.** CY-C pentagon healing is correct; κ_ch = 0 confirmed by Hodge supertrace.

### F5. BP Koszul-conductor polynomial identity (theorem-status table).

**Stated claim.** In Arakawa convention c(BP_k) = 2 − 24(k+1)²/(k+3), the Koszul-conductor function K_BP(k) := c(BP_k) + c(BP_{−k−6}) ≡ 196 in Q(k). In FL convention c^{FL}(k) = −(2k+3)(3k+1)/(k+3), K_BP^{FL}(k) is meromorphic with pole at k=−3.

**Direct verification of Arakawa polynomial identity** (computed inline in this audit by reading `bp_self_duality.tex:309-329`):
- (k+5)² − (k+1)² = 8(k+3); the (k+3) factor cancels EXACTLY against the denominator.
- K_BP(k) = 4 + 24·8(k+3)/(k+3) + … = 4 + 192 = 196. ✓ Polynomial identity in Q(k).

**F5.a — k = −3 critical fiber.** The fixed point k = −3 of k ↦ −k−6 coincides with the critical level −h^v(sl_3) = −3. The "principal-value symmetric limit" κ(BP_{−3}) = 49/3 is well-defined as
  lim_{ε→0} (1/2)[κ(BP_{−3+ε}) + κ(BP_{−3−ε})]
because the simple pole 24(k+1)²/(k+3) is odd around k=−3 in the relevant variable. **Verify directly:** at k = −3 + ε, c = 2 − 24·(−2+ε)²/ε = 2 − 24(4 − 4ε + ε²)/ε = 2 − 96/ε + 96 − 24ε. The leading singularity is −96/ε; symmetrising in ε ↦ −ε gives (−96/ε + 96/ε)/2 = 0, leaving 2 + 96 = 98 → κ = 49. **But the cited value is 49/3, not 49.** Either the symmetrisation must be applied to κ = c/something, or the symmetrisation involves a different odd part. Re-read `bp_self_duality.tex:301-307`: the cited value κ(BP_{-3}) = 49/3 is described as the "principal-value symmetric limit" without explicit derivation. **This is an ANOMALY — the symmetric limit of c gives 98, hence c/2 = 49, not 49/3.** Possible source of factor 1/3: BP-specific convention κ_BP = c/6 (not c/2). **Open frontier:** verify the κ_BP = c/6 normalisation by direct PBW computation.

**F5.b — convention coexistence.** Arakawa and Fateev–Lukyanov conventions parametrise the SAME BP algebra via a level reparametrisation k_FL = α k_Arakawa + β. Both must give the same κ + κ^!; the Arakawa-polynomial / FL-meromorphic split is a chart-dependent statement, not a structural one. **Beilinson surviving form: state the identity in BOTH conventions, exhibit the level reparametrisation explicitly, and verify the meromorphic-vs-polynomial difference is the image of the reparametrisation jacobian.**

**Verdict.** Arakawa polynomial identity K_BP ≡ 196 unconditional in Q(k). κ(BP_{−3}) = 49/3 has anomaly: arithmetic from `c(BP_k) − 98 odd in (k+3)` gives c → 98 hence κ = c/2 = 49, not 49/3. **Audit finding: verify BP κ-normalisation; if κ_BP ≠ c/2, the cited 49/3 needs explicit normalisation statement.**

## Survivors

After the attack, the surviving load-bearing claims are:

- **S1.** ϱ_A · K(A) consistency check holds for Vir, W_3, BP (TAUTOLOGICAL but correct).
- **S2.** Super-Yangian: σ_Ber central automorphism bridges super-trace (κ + κ^! = 0) and Berezinian (κ + κ^! = max(m,n)) on sub-Sugawara line. Lemma form ProvedHere via Nazarov–Gow.
- **S3.** Primes 23, 43, 419 are Bernoulli-regular (audit-verified). Primes 1423, 3067 are Bernoulli-regular through B_418; full confirmation via Buhler–Harvey table to 163M.
- **S4.** Hodge supertrace gives κ_ch(K3 × E) = 0 route-independent. ρ^{R_i} is edge-canonical, hence the {3, 12, 24} pentagon stratification is route-independent.
- **S5.** Arakawa-convention K_BP(k) ≡ 196 polynomial identity in Q(k), proved by direct (k+3) cancellation.

Retracted or restricted:

- **R1.** "K(A) = κ(A) + κ(A^!)" bare (without ϱ_A) is FALSE for every standard family. Always carry ϱ_A.
- **R2.** "W(p) is analytically tempered" — chapter's heal is plausible but not primary-source verified; current status conjectural.
- **R3.** "κ_ch stratification {3, 12, 24}" — replace by ρ^{R_i} stratification; κ_ch = 0 universally.
- **R4.** Kummer-irregular labels for {23, 43, 419, 1423, 3067} — replace by "Riccati-arithmetic characteristic primes of the Virasoro shadow tower" (relabel only; retains computational content as primes appearing in S_r numerators).
- **R5.** κ(BP_{−3}) = 49/3 needs explicit BP κ-normalisation derivation; anomaly with κ = c/2 ⟹ 49 unresolved in this audit.

## Platonic Reconstitution — Five Healed Identity Statements

**(I) Two-K conductor consistency (replaces AP234 / B93 as a structural identity).**

> *Definition.* For a chiral Koszul pair (A, A^!) in the standard landscape, the **central-charge conductor** is K(A) := c(A) + c(A^!) (a function of the Koszul-locus level parameter, identically constant on each one-parameter principal family by the Feigin–Frenkel involution). The **shadow conductor** is κ(A) + κ(A^!).
>
> *Proposition* (consistency of the two conductors on principal W_N). On principal W_N, with κ_W_N(c) = c·(H_N − 1) (Vol I C4) and the Feigin–Frenkel involution c ↔ K(W_N) − c (with K(W_2) = 26, K(W_3) = 100; K(W_N) for N ≥ 4 not yet inscribed in the census),
>
>     κ(W_N) + κ(W_N^!) = (H_N − 1) · K(W_N).
>
> The factor (H_N − 1) is the W_N κ-coefficient; the identity is an arithmetic consequence of κ-linearity in c plus the Feigin–Frenkel involution, NOT a separate theorem.
>
> *Remark.* On BP (with the Arakawa convention K_BP = 196 of Theorem `thm:bp-koszul-conductor-polynomial`), κ + κ^! = (1/6) · K_BP = 98/3, where 1/6 is back-derived; a structural derivation of the BP coefficient 1/6 (e.g., as a Hessian determinant or coset central-charge ratio) is an open question.
>
> *Scope.* Verified for W_2, W_3, BP. Untested for N ≥ 4. The bare equation K = κ + κ^! holds iff ϱ = 1; this never occurs on the standard landscape.

**(II) Super-Yangian complementarity bridge (heals B86 + OF6).**

> *Lemma* (super-trace–Berezinian bridge, after Nazarov 1991, Gow 2006). Let A = Y_ℏ(sl(m|n)) on the sub-Sugawara line k + h^v_s ≤ m+n, h^v_s = m−n. Write κ^str (resp. κ^Ber) for the shadow depth with respect to the super-trace (resp. quantum-Berezinian) pairing. Then:
>
>     κ^str(A) + κ^str(A^!) = 0,        κ^Ber(A) + κ^Ber(A^!) = max(m, n),
>     κ^Ber − κ^str = (1/2)·max(m, n)   on each of A and A^!.
>
> *Bridge.* Multiplication by sBer(T(u))|_{u=0} is an algebra automorphism of Z(A) (Nazarov 1991 Thm 1; Molev 3.9.1 + Gow 2006 Thm 5.1) and acts on shadow depth by the additive shift (1/2)·max(m, n). Both pairings are correct; they parametrise the same complementarity datum.
>
> *Scope.* sub-Sugawara line k + h^v_s ≤ m+n. Supertraceless type-A: super-trace = Verdier pairing; Sugawara pairing = Berezinian.

**(III) Kummer-irregular prime retraction.**

> *Definition.* The **characteristic primes of the Virasoro shadow tower** are the primes appearing in the numerators (or in the prime decomposition of denominators) of S_r(Vir_c) ∈ Q(c) for r ≥ 2.
>
> *Fact.* The set of Virasoro characteristic primes through r = 11 includes {37, 61, 193, 691, 811, 3617, 16657} (computed from `chapters/theory/shadow_tower_higher_coefficients.tex`). The intersection with Bernoulli-irregular primes is {37, 691, 3617}. The primes 23, 43, 61, 193, 419, 811, 1423, 2111, 3067, 16657 appear in the shadow data but are **Bernoulli-regular** (verified for 23, 43, 61, 193, 419 by exhaustion through their Kummer window; for 1423, 3067 via Buhler–Harvey 2011 "Irregular primes to 163 million"; 811, 2111, 16657 verified through B_418 in this audit).
>
> *Conclusion.* The label "Kummer-irregular" attached to {1423, 3067, 23, 43, 419} in earlier inscriptions was incorrect. They remain genuine **Riccati-arithmetic characteristic primes** of the shadow recurrence; the relabelling preserves their computational role.

**(IV) CY-C pentagon stratification (heals B89/B90).**

> *Theorem.* For G(K3 × E), the five-edge pentagon of MMF intertwiners R_1, ..., R_5 satisfies:
>
>     (a) κ_ch is route-independent and equal to the Hodge supertrace
>         κ_ch(K3 × E) = Σ (−1)^q h^{0,q}(K3 × E) = 0.
>     (b) The pentagon is stratified by the EDGE-CANONICAL invariant
>         ρ^{R_i} := rank of R_i as MMF-lattice intertwiner,
>         taking values in {3, 12, 24}.
>     (c) ρ^{R_i} and κ_ch are orthogonal invariants.
>
> *Retraction.* The earlier "κ_ch stratification {3, 12, 24}" was a category error: κ_ch is a route-independent supertrace (necessarily 0 for K3 × E); ρ^{R_i} is an algebraic invariant of each pentagon edge.

**(V) BP polynomial identity (Arakawa) and meromorphic identity (FL).**

> *Theorem* (Arakawa convention, after `bp_self_duality.tex:279-329`). With c(BP_k) = 2 − 24(k+1)²/(k+3), the Koszul conductor K_BP(k) := c(BP_k) + c(BP_{−k−6}) is identically 196 in Q(k). Equivalently c(BP_k) − 98 is an odd function of (k+3). The fixed point k = −3 is the critical level −h^v(sl_3); the symmetric limit κ_BP(−3) = (TBD) requires explicit BP κ-normalisation (open: see §F5.a).
>
> *Theorem* (FL convention). In the Fateev–Lukyanov screening convention c^{FL}(k) = −(2k+3)(3k+1)/(k+3), K_BP^{FL}(k) = −12(k+3) − 48/(k+3) is meromorphic with pole at k = −3. The two conventions parametrise the same BP algebra via the level reparametrisation k_FL ↔ k_Arakawa explicitly given by the central-charge equation; the polynomial-vs-meromorphic difference is the image of the reparametrisation jacobian.
>
> *Scope.* Both conventions valid; choose explicitly per chapter. Cross-volume references must state the convention.

## Open Frontier (post-audit)

1. **W(p) tempering.** Chapter `logarithmic_wp_tempered_analysis_platonic.tex` heals to tempering via three-channel Stirling argument, but the rectification audit retracted the corresponding theorem. The Gurarie/Flohr unbounded-Massey counterexamples concern correlation-function Massey, not shadow-tower-Massey; **the implication chain "C_2-cofin ⟹ bounded shadow Massey" remains open** as a precise question, distinct from the falsified "C_2-cofin ⟹ bounded correlation Massey".
2. **W_N (N ≥ 4) Koszul-conductor K(W_N).** Census carries no entry. Required for ϱ-identity testing at N ≥ 4. Predict: K(W_N) = c_self-dual(W_N) · 2, where c_self-dual(W_N) is the fixed point of the Feigin–Frenkel involution on principal W_N central charges.
3. **BP κ-normalisation.** κ(BP_{−3}) = 49/3 vs c(BP_{−3})|_{symm} → 98 ⟹ c/2 = 49. Resolve by reading the BP κ-coefficient (likely κ_BP = c/6, not c/2) directly from PBW.
4. **BP ϱ = 1/6 structural derivation.** Currently back-derived. Find Hessian / coset / Berezinian-shift origin.
5. **Buhler–Harvey citation in B92 retraction.** Add explicit primary-source citation for 1423, 3067 regularity.
6. **Beisert 2007 disjointness rationale (V3 in OF6).** Tighten — psl(2|2) gives 3 central elements, max(2,2) = 2; the agreement is via centre rank, not central-element count.

---

*Author.* Raeez Lorgat. *Audit posture.* Adversarial Beilinson. *Output.* This file only; no .tex inscription.
