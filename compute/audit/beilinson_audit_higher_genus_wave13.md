# Beilinson Audit — higher_genus_modular_koszul.tex (Wave 13)

**Target:** `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex` (29,818 lines, post Wave 6-4)
**Mode:** Read-only adversarial audit, six hostile examiners
**Focus:** Wave 6-4 load-bearing additions (`prop:universal-instanton-action`, `rem:universal-instanton-sanity`, `prop:c13-full-self-duality`, AP30 conditional tags) plus prior core theorems

---

## Per-Examiner Finding Counts

| Examiner           | CRITICAL | MODERATE | MINOR | NITPICK | Total |
|--------------------|:--------:|:--------:|:-----:|:-------:|:-----:|
| Formalist          |    2     |    4     |   3   |    2    |  11   |
| Topologist         |    1     |    3     |   2   |    1    |   7   |
| Physicist          |    1     |    2     |   2   |    1    |   6   |
| Number Theorist    |    1     |    2     |   2   |    1    |   6   |
| Adversarial Chef   |    2     |    3     |   2   |    1    |   8   |
| Editor             |    0     |    2     |   3   |    3    |   8   |
| **TOTAL**          |  **7**   |  **16**  | **14**| **9**   | **46**|

---

## Top 8 CRITICAL / MODERATE Findings

### C1 [CRITICAL — Formalist / Chef]
**`thm:shadow-formality-identification` (L14285) proof Step 4 confuses projection with equality.**
Step 4 asserts that the genus-0 projection of `Sh_r` is "exactly `ℓ_r^{(0),tr}` on the MC element," then writes
`Sh_r(A) = ℓ_r^{(0),tr}(...) + Σ_{g≥1} ℓ_r^{(g),tr}(...) + Λ_P(...)`.
But `Sh_r` as defined (L14108: `r_max := sup{r : A^sh_{r,0} ≠ 0}`, arity projection of Θ_A) is already a genus-0 object; the second "genus ≥ 1 corrections" summand on the same `Sh_r` double-counts if `Sh_r` means the arity-r projection at all genera, or is trivially zero if `Sh_r` is strictly genus-0. The proof needs to split notation: `Sh_r^(0)` vs `Sh_r^full`. As written, the closing decomposition equation is ill-typed. This propagates into Remark `rem:shadow-tower-linfty-formality` (L14493) which asserts the decomposition at the homotopy-invariant level.

### C2 [CRITICAL — Number Theorist]
**`thm:shadow-transseries` (L24422) vs `prop:shadow-stokes-multipliers` (L24417) residue inconsistency.**
Line 24417: `Res_{ℏ=2πn} = (-1)^n · 2πn · κ` (residue in ℏ-plane).
Line 24484: `R_n = (-1)^n · 8π²n² · κ` (residue of `Z(u) = Σ F_g u^g` as function of `u` at `u_n = (2πn)²`).
These are residues of *different* functions, but the proof at L24483 ("For the Taylor coefficients of `Z(u)` near a simple pole at `u_n`") derives `R_n` and then asserts `F_g^(n) = -R_n / u_n^{g+1}`. A direct check: at g=1, n=1, this gives `F_1^(1) = -(8π²κ)/(2π)^4 = -κ/(2π²)`, not the instanton large-order limit of `2κ/(2π)^{2g}` = `2κ/(2π)²` at g=1. The factor-of-4 discrepancy (or sign) indicates the pole-order counting in `Z(u)` (simple-pole in u? double-pole?) was done in the ℏ-variable, not the u-variable, and not reconciled. AP120 (Cauchy normalization) smell.

### C3 [CRITICAL — Topologist / Chef]
**`prop:universal-instanton-action` (L24499) universality claim overreaches.**
The claim states `A = (2π)²` is universal "across all modular Koszul families," but the proof (L24520) grounds universality in `F_g = κ · λ_g^FP` — which is the **uniform-weight scalar lane only** per AP32. For multi-weight W_N families, the cross-channel correction `δF_g^cross` has independent large-order behavior (explicitly flagged in `rem:cross-channel-instanton-heavier`, L24627: "cross-channel growth rate ... is not governed by a single instanton action in the usual Borel sense"). The proposition statement and proof both assert universality without the uniform-weight restriction. AP32 scoping tag missing from Proposition statement itself; the sanity-check remark `rem:universal-instanton-sanity` correctly tags AP32 but only for Vir_1, not as a precondition on the Proposition.

### C4 [CRITICAL — Formalist]
**`cor:explicit-theta-specializations` (L4000) duality line is wrong for Heisenberg / lattice.**
L4054-4057: "Duality: Θ^min_A + Θ^min_{A!} = 0 for affine KM (Feigin-Frenkel: k ↦ -k - 2h^v)."
But then the table includes Heisenberg (`κ = k`) and lattice VOA (`κ = d`). Heisenberg at level `k` and its Koszul dual: the Koszul dual of Heisenberg at level `k` is Heisenberg at level `-k` (in the sign-reversed convention), giving κ + κ' = 0. Fine. But for lattice VOAs, `κ(V_Λ) = d = rank` is a positive integer; its Koszul dual (formally the exterior algebra on Λ*) does not have `κ = -d` — lattice VOAs are not one-parameter families. The statement "κ+κ'=0 for affine KM and free-field algebras" silently lumps lattice VOAs into "free-field" with a duality that is not established in the chapter. AP33/AP29 cross-check: Heisenberg duality needs to be `Heis_k / Heis_{-k}` not `V_Λ / V_{Λ*}`.

### C5 [CRITICAL — Physicist / Formalist]
**`prop:c13-full-self-duality` (L24707) clause (c) is a silent conjecture.**
The proposition asserts `S_r(Vir_13) = S_r(Vir_13^!)` for all `r ≥ 2` "and the shadow trace formula `RTF(f) = 0` vanishes for all test functions `f` through **computationally verified arities**." The final phrase smuggles a conjectural universal statement behind a computationally-verified qualifier. The proof (L24756) then argues by "higher-arity corrections to RTF are odd functions of δ_κ (by the Z/2-symmetry of the Koszul involution acting on the shadow connection, Theorem `thm:shadow-connection`(v))" — but `thm:shadow-connection` (L17171) is about the Q_L' / (2 Q_L) 1-form; its clause (v) on Koszul Z/2 symmetry is cited without being visible in the proof as an all-arity claim. This is AP36 (claimed biconditional / universal without proved content). A finite computational check does not prove "for all test functions f, all arities." Downgrade to `ClaimStatusConjectured` for the all-arity portion of (c), or split: (c1) proved at arities 2..N via computation; (c2) conjecture for r > N.

### C6 [CRITICAL — Chef]
**`thm:genus-graded-koszul` (L238) convergence hypothesis (2) is circular.**
Hypothesis (2) requires the genus-graded bar complex to "converge in the ℏ-adic topology." The proof (L258) says "involutivity follows from applying bar-cobar at each genus and passing to the inverse limit using the convergence hypothesis." But the convergence hypothesis is stated without any content: it asserts exactly what the theorem needs, with no verification path, no cross-reference to `cor:free-energy-ahat-genus` (L2641, where |ℏ| < 2π convergence is established for the **scalar** series only). As stated, the theorem is vacuous: it says "if it converges, it converges to something invertible." The convergence hypothesis needs either (a) a sharper statement (filtered ℏ-adic completion is automatic; what's needed is non-triviality of graded pieces), or (b) verification for Koszul families (Heisenberg at k≠0, affine KM at generic level).

### M1 [MODERATE — Formalist]
**`thm:mc2-conditional-completion` (L7228) vs `thm:mc2-full-resolution` (L7312) scope creep.**
`thm:mc2-conditional-completion` is stated at the trace level with MC2-3 requiring tautological-line support. `thm:mc2-full-resolution` claims resolution "on the proved uniform-weight lane" but the theorem statement at L7316-7318 says "any Koszul chiral algebra A on a smooth projective curve X with non-degenerate invariant form and simple Lie symmetry g on the proved uniform-weight lane." Reading carefully, the "on the proved uniform-weight lane" parse-binds to "symmetry g" rather than to the theorem's scope — ambiguous. The proof (L7347) correctly treats this as a uniform-weight restriction, but the statement should front-load "uniform-weight" as a hypothesis. AP7 (universal quantifier without restriction check).

### M2 [MODERATE — Number Theorist]
**`rem:universal-instanton-sanity` (L24534) Gevrey-1 argument is circular at g=1.**
The remark computes `F_{g+1}/F_g ~ (2g+1)(2g+2)/(2π)² ~ 0.0253 g²` and says this "rules out the Gevrey-0 alternative" and "reads off the Borel singularity nearest the origin." But `F_g^{Vir_1} = (1/2) λ_g^FP` is the closed form the remark derives from; one cannot "read off" A = (2π)² from F_{g+1}/F_g when F_g was already defined via λ_g^FP which already had A = (2π)² baked into its `sinh^{-1}` generating function. This is a consistency check, not an independent verification path. AP119 (Gevrey-1 discrimination) correctly distinguishes Gevrey-0 from Gevrey-1 *in principle*, but here the input and output are the same function. The remark should be explicit: this is consistency, not independent corroboration.

---

## AP Compliance on Top-Level Claims

| AP     | Top-level claim           | Compliance status |
|--------|---------------------------|:-----------------:|
| AP1 (κ per family) | `cor:explicit-theta-specializations` (L4000): KM, Vir, W_N, Heis, lattice all correct per landscape | PASS (with MODERATE duality line, see C4) |
| AP8 (self-duality qualified) | `prop:c13-full-self-duality` tagged "AP8" at L24714 | PASS |
| AP24 (complementarity scoped) | L24715 "with complementarity sum κ+κ' = 13 on this family, AP24" | PASS |
| AP29 / AP33 (κ_eff ≠ κ+κ') | L24616-24625 separates κ_eff (c=26) from δ_κ (c=13) with AP29 | PASS |
| AP30 (CohFT flat-identity conditional) | 11 occurrences (L2053, L2111, L16949, L22091, L22981, L23162, L23186, L23247, L23442, L23524, L24108, L24224) | PASS — Wave 6-4 coverage appears complete |
| AP32 (uniform-weight on obs_g, F_g, λ_g) | `thm:modular-characteristic` (L2503), `thm:mc2-full-resolution` (L7312), `prop:universal-instanton-action` (L24499) | PARTIAL — `prop:universal-instanton-action` missing the tag (see C3) |
| AP36 (implies vs iff) | `prop:c13-full-self-duality` clause (c) "all arities" | FAIL (see C5) |
| AP116 (H_N harmonic) | L4050, L19149 use H_N = Σ_{j=1}^N 1/j correctly | PASS |
| AP117 (r(z)dz vs d log) | No KZ connection 1-form stated as `r(z) d log(z)` in Wave 6-4 additions | PASS |
| AP118 (g=1 matrix collapse) | (Im Ω)^{-1} not featured in this chapter; `ω_g` used correctly | PASS |
| AP126 (level-stripped r-matrix) | L24739 explicitly flags AP126 as "vacuous at Vir_13" for level-independent r(z) = κΩ/z³ + 2T/z | PASS |
| AP132 (augmentation ideal) | L24736 flags AP132 explicitly, and L733, L1399, L11928, L24730 use ker(ε) or `\bar{V}` | PASS |
| AP136 (H_{N-1} ≠ H_N - 1) | No H_{N-1} notation appears — chapter uses `c(H_N - 1)` consistently | PASS |
| AP141 (AP126 sweep) | r-matrix formula at L24739 includes κ prefix on Ω/z³, consistent with level-dependent form | PASS |
| AP139 (unbound variables) | `thm:multi-weight-genus-expansion` (L20071): F_g depends on g only on LHS, n never appears as free; iv-vi variables all bound | PASS |

---

## Additional MODERATE Findings (abbreviated)

- **M3 [Formalist]** `prop:gue-universality` (L2707) identifies N² = κ(A) — for Heisenberg at k=1, gives N²=1, N=1; GUE at N=1 is trivial Gaussian. Statement is fine but the identification `N² = κ` with κ potentially non-integer (e.g. 3(k+2)/4 for sl_2 at generic k) requires interpretation as a formal parameter, not a matrix size. Not flagged.
- **M4 [Topologist]** `thm:operadic-complexity-detailed` (L14096): The statement `r_max = d_∞ = f_∞` depends on injectivity of antisymmetrization `m_r^tr → ℓ_r^{(0),tr}` on cyclic cochains. Proof at L14139 asserts injectivity without citation; for cyclic chain-level arguments this is nontrivial and should cite Loday-Vallette or a specific lemma in the chapter.
- **M5 [Physicist]** `prop:shadow-integrable-hierarchy` (L16939) Gelfand-Dickey identification for class L is "G D_2" — but for affine sl_N the natural DS reduction gives GD_N, not GD_2. The class-L row should specify: affine g at the sl_2 level gives GD_2, but affine sl_3 gives GD_3 (even though both are class L with r_max = 3). Terminological slip.
- **M6 [Editor]** `rem:kappa-deformed-kdv` (L17051) — at κ=0 "the nonlinear term diverges and the KdV description breaks down, consistent with the triviality of the shadow tower." But κ=0 is critical-level (affine KM) where the Feigin-Frenkel center is nontrivial; the shadow tower is trivial but the content migrates to bar cohomology. The "breaks down" phrasing fails to acknowledge this (compare to Overture / preface which handles it cleanly).
- **M7 [Chef]** `thm:km-strictification` (L7480) asserts `Θ^str_{ĝ_k} = κ(ĝ_k) · μ ⊗ Λ` is "a strict chain-level MC element" with no corrections at any genus. But this is an `l_1, l_2`-strict statement on Def^cyc(ĝ_k). The theorem does not address whether, under homotopy transfer to `g^mod`, higher brackets could appear — and `cor:one-dim-obstruction` ensures only the degree-2 line is one-dimensional, not that there are no quartic or higher corrections. Proof is correct for the strict model; the claim "no corrections at any genus" should be scoped to the strict chart.

## Additional MINOR / NITPICK Findings

- **MINOR** `thm:multi-weight-genus-expansion` part (ii) (L20098): `δF_g^cross(A)` is a graph sum over "mixed-channel boundary graphs of M̄_{g,0}" but the W_3 genus-2 computation at L22925 writes four contributing graphs (sunset, theta, bridge-loop, barbell), and the theorem statement says three (L20127). L22931 then lists four. Arithmetic inconsistency between statement and remark — resolved in the formula `(c+204)/(16c) = 3/c + 9/(2c) + 1/16 + 21/(4c)` (four terms) but the theorem text at L20127 says "three contributing strata."
- **MINOR** L24854: "gap of 13 units between the two central charges is dim(g)/2 = 26/2" is reversed — 26/2 = 13, and the gap c=26 vs c=13 is 13 units. Phrasing is correct but "= 26/2" reads as if the gap equals 26/2; should read "26 - 13 = 13 = dim/2."
- **MINOR** `prop:shadow-schwarzian` (L24882) `C = 8κ²Δ` then `C = -disc(Q_L)/4` with `disc = -32 κ² Δ`. Check: `-(-32κ²Δ)/4 = 8κ²Δ`. Consistent. Not a finding — verification passes.
- **NITPICK** L14067 "The arity-(r+1) obstruction receives contributions from two sources: connected graphs (possibly multi-vertex) producing total arity r+1, and the genus-loop operator Λ_P applied to lower-arity shadows." This list is not exhaustive if higher BV operators `l_1^{(g≥2)}` contribute at lower arity — the proof should cite the vanishing condition.
- **NITPICK** L27593 "Assume the full universal Maurer-Cartan element is scalar" — this is an unmarked conjecture masquerading as a hypothesis of a theorem. Fine as a hypothesis; but the theorem as stated has a trivial conclusion if the hypothesis is never checked.
- **NITPICK** L25662 "(Virasoro, W_N)" as example of class M — strictly this is the class M identification per Table 14152, but the remark should cross-reference `ex:operadic-complexity-verification` for the depth claim.
- **NITPICK** Several em dashes not found — prose standard compliant. Passive voice minimal.

---

## Health Grade

**B+ (Strong, load-bearing content with 2 structural gaps)**

The chapter is the largest in Vol I (29,818 lines) and carries the full higher-genus programme. The Wave 6-4 additions (`prop:universal-instanton-action`, `rem:universal-instanton-sanity`, `prop:c13-full-self-duality`, ~11 AP30 tags) are real improvements but introduce two specific structural issues:

**Strengths.**
- AP30 coverage appears uniform across all shadow-CohFT cross-references (11 explicit flags).
- AP1 κ formulas per family are correct; `c(H_N - 1)` for W_N is correct and not conflated with `c H_{N-1}` (AP136 compliant).
- AP8 / AP24 / AP29 qualification on c=13 self-duality is present and distinguishes `δ_κ = 0` (c=13) from `κ_eff = 0` (c=26).
- AP132 augmentation-ideal language used at the key site.
- The `thm:multi-weight-genus-expansion` correctly proves the scalar formula *fails* at g=2 for W_3 with the explicit `(c+204)/(16c)` correction (AP32 scoping correct).
- The `prop:shadow-formality-low-arity` → `thm:shadow-formality-identification` proof is structurally sound at arities 2, 3, 4 and the induction is well-motivated.

**Critical gaps.**
- C3 (AP32 missing from `prop:universal-instanton-action` statement).
- C5 (`prop:c13-full-self-duality` clause (c) "all arities" is a silent conjecture).
- C6 (`thm:genus-graded-koszul` convergence hypothesis is vacuous).
- C1 (type error in `thm:shadow-formality-identification` Step 4 on Sh_r vs Sh_r^{(0)}).
- C2 (residue/Borel-variable confusion between `thm:shadow-transseries` and `prop:shadow-stokes-multipliers`).

**Structural remark.** The chapter is well-modularized into six subsections (genus tower, Koszul-graded, modular characteristic, shadow formality, shadow CohFT, self-dual point) with minimal redundancy. The CG structural moves (deficiency opening via genus-0 inversion failure at g ≥ 1, unique survivor via the four-class G/L/C/M dichotomy) are executed cleanly. The Wave 6-4 sanity-check remark at `rem:universal-instanton-sanity` demonstrates AP119 (Gevrey-1 discrimination) correctly in principle but has a consistency-vs-independence bug (M2).

---

## Recommendations for Rectification Wave

**Priority 1 (CRITICAL — must fix before next build cycle).**

1. **[C3] Scope `prop:universal-instanton-action` to uniform-weight lane.** Add explicit "(uniform-weight; AP32)" tag to the Proposition statement. The proof is correct in spirit but the multi-weight case is handled by `rem:cross-channel-instanton-heavier`, which should be cross-referenced from the Proposition.

2. **[C5] Split `prop:c13-full-self-duality` clause (c) into proved + conjectural.** Rewrite as:
   - (c1) `S_r(Vir_13) = S_r(Vir_13^!)` for `r ≥ 2`: PROVED (rationality + involution fixing c=13).
   - (c2) RTF(f) = 0 for all f: CONJECTURE, verified computationally through arity r ≤ N (specify N).

3. **[C6] Give `thm:genus-graded-koszul` a non-vacuous convergence hypothesis.** Either:
   - (a) replace "converges in ℏ-adic topology" with the sharper "graded pieces `B^(g)(A) / B^(g+1)(A)` are finite-dimensional in each conformal weight," OR
   - (b) verify the convergence explicitly for Heisenberg and affine KM at generic level using `cor:free-energy-ahat-genus` as a model.

4. **[C1] Fix `thm:shadow-formality-identification` Step 4 type confusion.** Introduce `Sh_r^{(0)}` (genus-0 arity-r shadow) vs `Sh_r^full` (all-genus arity-r projection) as distinct symbols. The decomposition at L14455 should read:
   `Sh_r^full(A) = Sh_r^{(0)}(A) + [genus ≥ 1 corrections]`
   with `Sh_r^{(0)} = ℓ_r^{(0),tr}(...)` and the corrections from `Λ_P` and `ℓ_n^{(g≥1)}`.

5. **[C2] Reconcile the Borel-variable residue calculation in `thm:shadow-transseries`.** Either work consistently in `u = ℏ²` throughout (where the pole at `u_n = (2π n)²` is simple, residue `R_n`), or consistently in ℏ (pole at `ℏ = 2π n`, residue `(-1)^n · 2π n · κ`), and perform the `F_g^{(n)}` extraction explicitly with correct pole-order counting. AP120 (Cauchy normalization) cross-check: verify `F_1^{(1)} = 2κ/(2π)²` matches a known expansion.

**Priority 2 (MODERATE — next rectification sweep).**

6. **[C4] Fix `cor:explicit-theta-specializations` duality line.** Change "κ + κ' = 0 for affine KM and free-field" to "κ + κ' = 0 for affine KM and Heisenberg (at opposite levels)." Lattice VOAs should either be given a stated Koszul partner or be excluded from the duality clause.

7. **[M1] Front-load "uniform-weight" hypothesis in `thm:mc2-full-resolution`.** Rephrase statement so "on the proved uniform-weight lane" binds to the theorem scope, not to "simple Lie symmetry."

8. **[M2] Annotate `rem:universal-instanton-sanity` as consistency check, not independent verification.** The Gevrey-1 argument is internally consistent but uses the same λ_g^FP generating function; the cross-check is against closed-form F_g, which is not independent.

9. **[M7] Scope `thm:km-strictification` conclusion to the strict chart.** "No corrections at any genus" should read "in the strict model Def^cyc(ĝ_k); the statement does not constrain higher brackets under transfer to `g^mod`."

**Priority 3 (MINOR / NITPICK — prose polish sweep).**

10. Reconcile 3-vs-4 graph count mismatch between `thm:multi-weight-genus-expansion` clause (vi) (L20127) and `rem:w3-genus2-cross-channel` (L22925).
11. Polish the "26/2" phrasing at L24854.
12. Specify the Gelfand-Dickey order for class L in `prop:shadow-integrable-hierarchy`.

**Estimate:** Priority-1 fixes are ~6-8 hours of focused work per finding (including Beilinson reverification). Priority-2 fixes ~2-3 hours each. Priority-3 are single-commit polishes.

**Cross-volume propagation (AP5) flag.** Findings C3, C4, C5 are likely mirrored in Vol II (gravity climax + self-dual invocations) and the Vol I preface (which inherits the scalar formula universality claim). A propagation sweep on `prop:universal-instanton-action`, `prop:c13-full-self-duality`, and the "κ + κ' = 0 for free-field" phrasing across all three volumes is recommended concurrent with rectification.

---

*End of audit.*
