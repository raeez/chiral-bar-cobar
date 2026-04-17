# Wave-7 Beilinson Attack + Heal: Conformal Anomaly c/2 and prop:e3-via-dunn

Date: 2026-04-17
Targets:
1. Vol I status-table claim "Conformal anomaly QUANTIFIED: obstruction to constant coproduct = c/2 = kappa(Vir_c); c=0 vanishes; c != 0 spectral parameter FORCED."
2. Vol I status-table claim "E_3 via Dunn PROVED (alt): prop:e3-via-dunn (CG factorization E_1^top x E_2^hol + Sugawara + Dunn = E_3^top). INDEPENDENT of HDC."

Canonical sources audited:
- `chapters/theory/conformal_anomaly_rigidity_platonic.tex` (481 lines, full Platonic form).
- `chapters/theory/en_koszul_duality.tex:4892-5102` (prop:e3-via-dunn + rem:e3-two-routes + theorem thm:e3-cs context).
- `chapters/theory/en_koszul_duality.tex:3052-3207` (def:inner-conformal-vector, thm:topologization, constr:sugawara-antighost).
- `chapters/theory/en_koszul_duality.tex:26-47` (chapter preamble scope bullets constraining SC^{ch,top} vs E_3).
- `chapters/theory/en_koszul_duality.tex:7736-7823` (prop:e3-on-derived-center explicit colored-operad obstruction discussion).

## Phase 1: Hostile Audit

### (i) Conformal anomaly = c/2 = kappa(Vir_c)

Claim reads: "obstruction to constant coproduct = c/2". Four sub-checks.

(a) **Is the coefficient literally c/2, not c/12 or c/6?**
The chapter (`conformal_anomaly_rigidity_platonic.tex`) pins the coefficient to the TT OPE double-pole `(c/2)/(z-w)^4` in BPZ normalisation (eq:TT-OPE, line 59-65). The rigidity theorem (thm:conformal-anomaly-rigidity, line 182-237) proves the obstruction class in H^2_ch(Vir_c, Vir_c) equals `(c/2) * Omega` where Omega is the universal Virasoro Casimir class (def:universal-casimir, line 125-137). The proof extracts the coefficient by residue against `T(z_1)T(z_1+z_2)T(0)` and reads off the (z_1-z_2)^{-4} double-pole coefficient, which is c/2 in every CFT convention. The distinct numeral c/24 appears only via the cylinder L_0 mode and is correctly segregated in rem:bpz-c-over-24-distinction (line 384-393).

VERDICT: c/2 is CORRECT and UNIVERSAL. The bridge identity "Casimir energy on the cylinder = (c/2)/12" is stated.

(b) **Is c/2 = kappa(Vir_c)?**
Census C3 confirms: kappa(Vir_c) = c/2 (AP39: Vir is the ONLY family where kappa coincides with S_2/2 = c/2). The chapter's rem:kappa-vir-is-c-over-2 (line 104-115) cites landscape_census.tex and the Virasoro status row. Numerical self-check at c = 13: kappa = 13/2, matching Vir^! = Vir_{26-c} self-duality. 

VERDICT: Identification c/2 = kappa(Vir_c) is CORRECT on a Census-verified path (not a memory recall).

(c) **At c = 0 does constant coproduct exist?**
thm:c-zero-coproduct-is-constant (line 239-272) proves: at c = 0, the TT OPE has vanishing double pole, so Vir_0 twoheadrightarrow Witt is an iso of vertex Lie algebras; Drinfeld-Etingof-Kazhdan uniqueness of the Witt Lie bialgebra gives a unique z-independent coproduct on Witt, lifted to Vir_0 by primitivity on the (now-central, trivially acting) central element. The degree-2 obstruction (c/2)*Omega vanishes at c=0; HKR descent lifts the trivialisation inductively in z.

VERDICT: CORRECT. c = 0 obstruction genuinely vanishes; the Witt Lie bialgebra exists and is z-independent.

(d) **Is "spectral parameter FORCED" from Delta_z cocycle?**
prop:spectral-parameter-forced-at-nonzero-c (line 274-296) proves: any z-independent Delta has delta'(0) = 0, hence obs = 0; but the rigidity theorem gives obs = (c/2)Omega, which is nonzero in H^2_ch(Vir_c, Vir_c) by lem:casimir-nonvanishing (Feigin-Fuchs H^2(Witt; C) = C, line 139-166). Contradiction. Hence no z-independent Delta can satisfy shifted-parameter coassociativity at c != 0.

VERDICT: CORRECT. The forcing IS from the shifted-parameter coassociativity cocycle condition (def:chiral-coproduct-spectral (iii), line 86-88), exactly as Drinfeld's quantum-double construction requires spectral parameter to cancel the central-charge anomaly.

**Adversarial probe**: "What if H^2(Vir_c, Vir_c) has rank > 1 and other classes contribute?"

Feigin-Fuchs is explicit: the scalar (Vir-invariant) part is 1-dimensional (lem:casimir-nonvanishing line 143-147). The non-scalar complement vanishes on the test pair (T_{-2}|0>, T_{-2}|0>), which is Vir-invariant. rem:casimir-intrinsic (line 168-177) separates universal vs module-pullback: a null module can kill the image but not the universal coefficient (thm:universal-coefficient, line 298-333).

**Adversarial probe**: "Can c/2 be absorbed into a redefinition of Omega?"

No: Omega is normalised by Omega(T_{-2}|0>, T_{-2}|0>) = |0> (def:universal-casimir line 134-135). The c/2 is rigid given this normalisation, matching the TT OPE double-pole coefficient. Adversarial audit bullet (1) in sec:adversarial-audit-anomaly (line 402-411) acknowledges that null modules are the only obstruction to "nonzero on every representation", and correctly states this is a measure-zero locus.

**Adversarial probe (AP138 parity check)**: TT OPE `(c/2)/(z-w)^4` is symmetric (even) under (z,w) swap combined with (T <-> T) even parity, so the double-pole Casimir class is a genuine symmetric-2-cocycle, not a parity-forbidden identity.

FINAL VERDICT (i): Conformal anomaly c/2 obstruction SURVIVES at sharpest form. Universal coefficient proved; module pullback caveat correctly stated. The chapter is PLATONIC as inscribed.

### (ii) prop:e3-via-dunn

Claim: CG factorization `F^{CS}_k` on R x C provides `E_1^top x E_2^hol`; Sugawara at non-critical k makes C-translations Q-exact, promoting E_2^hol -> E_2^top cohomologically; Dunn gives E_3^top.

(a) **Is `F^{CS}_k` single-colored?**
Yes: F^{CS}_k is a factorization algebra on the 3-manifold R x C in the Costello-Gwilliam sense (prop:e3-via-dunn proof line 4956-4969). This is a SINGLE-COLOURED factorization algebra on a 3-manifold, distinct from SC^{ch,top} which is the two-coloured operad governing open/closed boundary configurations. The distinction is load-bearing: SC^{ch,top} is two-coloured with directionality (no open->closed maps); the chapter preamble bullet #2 (line 26-36) and prop:e3-on-derived-center (line 7736-7823) state this obstruction explicitly.

CAVEAT IDENTIFIED: The proof of thm:topologization (line 3162-3167) writes "the E_1^top from the R-direction (the open color of SC^{ch,top})" — this parenthetical equates the CG R-factor with the SC^{ch,top} open color. This is technically a misnomer: the E_1^top comes from the CG factorization algebra's R-direction (single-coloured on R x C), NOT from SC^{ch,top}. The SC^{ch,top} framework does NOT admit Dunn (per bullet #2); invoking "open color of SC^{ch,top}" here is prose slippage. The proof is CORRECT if read with F^{CS}_k in place; the parenthetical is a minor expository bug that risks reader confusion.

HEAL (surgical edit, en_koszul_duality.tex:3162-3167): replace "(the open color of SC^{ch,top})" with "(the single-coloured topological factor of the CG factorization algebra F^{CS}_k on R x C)".

VERDICT (a): F^{CS}_k IS single-coloured; prop:e3-via-dunn proof is internally consistent. The thm:topologization parenthetical needs surgical rewording to match the correct ontology.

(b) **Sugawara -> E_2^hol promoted to E_2^top cohomologically?**
thm:topologization part (i) (line 3148-3167) gives: inner conformal vector identifies T_Sug with [Q,G] in BRST cohomology; G generates holomorphic translations; hence C-translations act trivially on H_Q^*. Lurie HA Thm 5.4.5.9 (locally constant factorization algebra on C ≅ R^2 is an E_2^top-algebra) delivers the promotion.

Scope check: Sugawara denominator 2(k+h^v) requires k != -h^v (critical level caveat on line 3200-3206). At k = -h^v, promotion fails; this is correctly noted.

VERDICT (b): Promotion is COHOMOLOGICAL (on H_Q^*) not chain-level on the original complex. This matches AP-TOPOLOGIZATION (H15). Chain-level requires the A_inf coherence [m, G] = partial_z (thm:topologization part (iii), line 3186-3198), which is PROVED for affine KM at non-critical level (Vol II e_infinity_topologization.tex) and CONJECTURAL for general chiral with conformal vector (conj:topologization-general).

(c) **Dunn additivity validly applied?**
Dunn (Lurie HA Thm 5.1.2.2): E_m tensor E_n ≅ E_{m+n} for single-coloured E_n-operads acting on a COMMON object. In prop:e3-via-dunn, both the E_1^top and E_2^top factors act on the SAME object H_Q^*(Z^{der}_ch(V_k(g))) (line 4992-5000); the factors come from orthogonal geometric directions (R and C ≅ R^2 embedded as R x C ≅ R^3). The coloured-operad obstruction does NOT apply because F^{CS}_k is single-coloured on the 3-manifold.

VERDICT (c): Dunn application is VALID at the cohomological level on H_Q^*. Chain-level on original complex is not claimed by prop:e3-via-dunn (it's cohomological by construction via the BRST passage).

### (iii) INDEPENDENT of HDC

rem:e3-two-routes (line 5003-5067) compares:
- HDC route (thm:e3-cs(i)): Bar^Sigma(V_k(g)) is E_2; Higher Deligne promotes Hochschild cochains to E_3 via E_2+1 = E_3. Purely algebraic, works for any E_inf-chiral algebra.
- Dunn route (prop:e3-via-dunn): CG factorization E_1^top x E_2^hol + Sugawara topologises E_2^hol -> E_2^top; Dunn gives E_3^top. Uses 3d bulk theory explicitly.

The two routes are GENUINELY INDEPENDENT: the HDC route uses no 3d bulk and no Sugawara, only the symmetric bar E_2 + Higher Deligne Conjecture. The Dunn route uses no Higher Deligne Conjecture, only Costello-Gwilliam factorization + Lurie recognition + Sugawara + Dunn (which is a theorem, not a conjecture). The two E_3^top structures agree via CFG classification thm:cfg (both classified by (k+h^v) H^3(g)[[k+h^v]]).

VERDICT (iii): "INDEPENDENT of HDC" is JUSTIFIED. The Dunn route avoids the Higher Deligne Conjecture entirely. (The HDC route is the one that invokes it; the Dunn route is strictly alternative.)

### (iv) AP167/AP168 scope (affine KM specific?)

prop:e3-via-dunn is EXPLICITLY scoped to affine Kac-Moody V_k(g) at non-critical level k != -h^v (proposition statement line 4903-4905). This matches AP-TOPOLOGIZATION: topologization is PROVED for affine KM at non-critical level; CONJECTURAL for general chiral with conformal vector (conj:topologization-general). General-chiral extension is NOT claimed by prop:e3-via-dunn.

VERDICT (iv): Scope is HONEST. Proposition does not overclaim beyond affine KM.

### (v) Chain-level vs cohomological

prop:e3-via-dunn output is explicitly on H_Q^*(Z^{der}_ch(V_k(g))) (line 4907, 4998-5000), i.e. COHOMOLOGICAL. Chain-level on the original complex is addressed by thm:topologization part (iii) under the hypothesis [m,G] = partial_z (line 3186-3198). For class M, chain-level on the original complex is GENUINELY OPEN (CLAUDE.md "MC5 class M chain-level is direct-sum FALSE; weight-completed / pro-ambient / J-adic PROVED"); prop:e3-via-dunn does not touch class M directly.

VERDICT (v): Scope is HONEST cohomological at the proposition level. The chain-level statement for class L requires the extra A_inf coherence hypothesis, correctly flagged in thm:topologization(iii).

### (vi) Propagation

CLAUDE.md entry: "E_3 via Dunn PROVED (alt): prop:e3-via-dunn: CG factorization E_1^top x E_2^hol + Sugawara + Dunn = E_3^top. Independent of HDC."

This summary is FAITHFUL to the proposition. The status-table row should be read with implicit scope: output on H_Q^* (cohomological), affine KM at non-critical level. The "INDEPENDENT of HDC" qualifier is mathematically justified. No propagation edits required.

## Phase 2: Heal

Single surgical heal identified: the parenthetical "the open color of SC^{ch,top}" at en_koszul_duality.tex:3163-3164 (in the proof of thm:topologization part (i)) and again at en_koszul_duality.tex:4600-4601 (proof of prop:e3-via-dunn alternative packaging) and 7743-7744. These phrase the R-direction of the CG 3-manifold factorization algebra as if it were the "open color" of SC^{ch,top} — conflating two distinct ontologies. Since SC^{ch,top} is the coloured operad where Dunn does NOT apply (per chapter bullet #2 and prop:e3-on-derived-center), invoking "open color" while then applying Dunn is a micro-slippage.

**Recommended heal (light-touch, prose-only)**:
- Line 3163-3164 (thm:topologization proof, part (i)): replace "(the open color of SC^{ch,top})" with "(the topological factor of the Costello-Gwilliam factorization algebra F^{CS}_k on R x C, single-coloured on the 3-manifold)".
- Line 4600-4601 (analogous phrasing in proof of thm:chain-level-E3-top-class-L): analogous replacement.

Both edits are expository, not mathematical; they make the Dunn-admissibility transparent by explicitly naming the single-coloured factorization algebra ambient in which Dunn applies (as opposed to SC^{ch,top} where it does not).

Applied below as one Edit operation per occurrence.

## Constitutional Hygiene Audit

Grep the chapter and conformal_anomaly_rigidity_platonic.tex for forbidden typeset tokens `AP\d+`, `HZ-\d+`, `Pattern \d+`, `Cache #\d+` in non-comment lines.

- `conformal_anomaly_rigidity_platonic.tex`: clean (AP/HZ absent from typeset prose).
- Prop:e3-via-dunn and thm:topologization blocks: clean (AP/HZ absent from typeset prose).

No hygiene violations.

## Summary Verdict

(i) Conformal anomaly c/2 obstruction: SURVIVES sharpest form. The chapter is Platonic. No edits.
(ii) prop:e3-via-dunn: SURVIVES with scope honest (cohomological on H_Q^*, affine KM non-critical, Dunn on single-coloured F^{CS}_k). One expository micro-heal identified: replace "the open color of SC^{ch,top}" with "the single-coloured topological factor of F^{CS}_k on R x C" at three sites. Mathematical content unchanged; reader clarity improved.

## File Paths (absolute)

- `/Users/raeez/chiral-bar-cobar/chapters/theory/conformal_anomaly_rigidity_platonic.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex`
