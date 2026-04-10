# Codex Review of `true_formula_census_draft_wave12.md`

## Summary

I audited the 30-entry census independently against the local constitutional surfaces (`CLAUDE.md`, `chapters/connections/concordance.tex`, `metadata/theorem_registry.md`, `archive/raeeznotes/raeeznotes100/red_team_summary.md`), the manuscript chapters actually carrying the formulas, and a small set of targeted compute tests. The result is mixed but usable. The draft is strong on many of the scalar canonical formulas themselves: Heisenberg `\kappa = k`, Virasoro `\kappa = c/2`, affine KM `\kappa = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`, principal `W_N` `\kappa = c(H_N-1)`, the `bc/\beta\gamma` central-charge pair, the Virasoro collision residue, the augmentation-ideal bar construction, desuspension, harmonic numbers, eta normalization, and the Maurer-Cartan/QME factors are all locally corroborated. The draft is much weaker exactly where the project has historically been weak: convention-sensitive `r`-matrices, family-dependent averaging identities, conductor-vs-`\kappa`-sum conflations, and “same shape, different context” formulas where one normalization is being over-promoted into a universal one.

The seven priority entries split into three groups. C3 is sound: the affine KM `\kappa` formula is correct, and the draft correctly records the nonzero value `\kappa(V_0(\mathfrak g))=\dim(\mathfrak g)/2`. The subtlety caught in Wave 7-1 is real, but it belongs to the averaging identity, not to the `\kappa` formula itself. C4 is also sound: Drinfeld-Sokolov reduction gives generators at conformal weights `m_i+1`, so `\kappa = c \sum_i 1/(m_i+1)`, and for `\mathfrak{sl}_N` this becomes `c(H_N-1)`. The `K_N` values for `N=3,4,5` match the landscape census and the compute layer. C21 is likewise solid: the local Borcherds-lift code reconstructs `\mathrm{wt}(\Phi_{10})=10` from the K3 elliptic-genus coefficient `c_0(0)=20`, and hence `\kappa=5` via the half-weight rule.

The remaining four priority entries all require correction. C9 is not wrong in its displayed formula `k\,\Omega/z`, but it is wrong as a universal census item because the draft blacklists the KZ normalization `\Omega/((k+h^\vee)z)`, which Vol. I itself uses in the affine/KZ lane. The local evidence now supports a three-way convention split: Costello/collision-residue `k\,\Omega/z`, KZ `\Omega/((k+h^\vee)z)`, and a level-absorbed/Yangian `\Omega/z`. Those are not interchangeable, but neither are they all “wrong variants.” C16 gets the unordered set of eight `E_8` fundamental dimensions right, but two surrounding claims fail: the ordering is not Bourbaki-stable because the local engine uses a non-Bourbaki numbering for `E_8`, and the draft’s arithmetic sum is wrong. The true sum of the listed dimensions is `7054732527`, not `7056003287`. C18 is materially wrong for Bershadsky-Polyakov: if `K(A)` is defined as `\kappa(A)+\kappa(A^!)`, then the BP value is `98/3`, not `196`; `196` is the central-charge conductor `c(k)+c(-k-6)`. C20 has the correct conductor formula but both sanity checks are false: from the local BP central-charge formula one gets `c(0)=-6`, `c(-6)=202`, and the duality-fixed level `k=-3` is a pole, not a finite self-dual point. The self-dual central charge `98` occurs at the complex levels `k=-3\pm 2i`, exactly as the BP chapter states.

Outside the priority set, the most important corrections are C13, C28, C29, and C30. C13 is simply false as written: `\mathrm{av}(r)=\kappa` is true for Heisenberg/abelian lanes, but the non-abelian affine identity is `\mathrm{av}(r)+\dim(\mathfrak g)/2=\kappa`. C28 is also false: the manuscript writes the KZ connection both as `\Omega\,dz_{ij}/z_{ij}` and as `\Omega\,d\log(z_i-z_j)`, so blacklisting `d\log` is an error, not a safeguard. C29 has the right warning about matrix collapse at genus one, but its Hodge-class formula is not mathematically well-formed at general genus: `\lambda_1=c_1(\mathbb E)` at genus one, while `\lambda_g=c_g(\mathbb E)` at genus `g`, and one should not write `c_1(\lambda_g)`. C30 keeps the correct discriminant formula `\Delta=8\kappa S_4` but then overstates it into a global finite-depth criterion. Local class-C files explicitly record finite depth `r_{\max}=4` with nonzero quartic contact and termination by stratum separation, so “finite depth iff `\Delta=0`” is not globally true.

The draft’s overall reliability is therefore not catastrophic, but it is not yet a constitutional source. I count a proved core of correct formulas, several entries that become acceptable after narrow contextual repair, and a smaller but important set of entries where the draft currently teaches the wrong reflex: universalizing the affine `r`-matrix normalization, universalizing `\mathrm{av}(r)=\kappa`, identifying the BP central-charge conductor with the BP `\kappa`-sum, or forbidding `d\log` in the KZ connection. Those are exactly the error modes the anti-pattern infrastructure exists to stop. The numerics are mostly good; the claim-surface discipline is not yet stable. My trust grade is therefore **C**: useful as a checked worksheet, unsafe as a “must never be written from memory” authority until the convention-sensitive entries are repaired and the misleading sanity checks are removed.

Targeted compute checks run during this audit:

- `pytest -q compute/tests/test_bc_exceptional_categorical_zeta_engine.py -k 'fundamental_dimensions_match_known'` -> `5 passed`
- `pytest -q compute/tests/test_landscape_census_verification.py -k 'complementarity or w4_kappa or w3_central_charge_formula'` -> `13 passed`
- `pytest -q compute/tests/test_bp_shadow_tower.py -k '196 or koszul'` -> `2 passed`
- `pytest -q compute/tests/test_cy_borcherds_lift_engine.py -k 'weight_10 or phi_10 or borcherds_weight'` -> `3 passed`
- `pytest -q compute/tests/test_theorem_pva_classical_r_matrix_engine.py -k 'heisenberg or sl2 or dlog'` -> `31 passed`
- `pytest -q compute/tests/test_mzv_bar_complex.py -k 'KZ and connection'` -> `7 passed`

## Per-entry Verdict Table

| Entry | Verdict | Evidence and notes |
|---|---|---|
| C1 | CORRECT | `chapters/examples/free_fields.tex:1375,5428-5449` and `chapters/frame/heisenberg_frame.tex:1987,4015` support `\kappa(\cH_k)=k` and `\operatorname{av}(k/z)=k`. |
| C2 | NEEDS REFINEMENT | `\kappa(\mathrm{Vir}_c)=c/2` is correct (`chapters/examples/genus_expansions.tex:1302`), but the entry falsely says Virasoro is the unique standard family with `\kappa=c/2`; `\beta\gamma` also has `\kappa=c/2` (`chapters/examples/beta_gamma.tex:1212-1218`). The sanity check “`c=0` implies abelian” is false; the central term vanishes but the Witt bracket remains. |
| C3 | CORRECT | `chapters/examples/landscape_census.tex:76-79` and `chapters/frame/preface.tex:616-624` support the shifted affine formula and the nonzero `k=0` value. |
| C4 | CORRECT | `chapters/examples/w_algebras.tex:2317-2319` derives `\kappa=c\sum_i 1/(m_i+1)` from DS reduction; `chapters/examples/landscape_census.tex:134-137,688-692,1219-1223,1380-1382` give the `\mathfrak{sl}_N` specialization and `K_N` values. |
| C5 | CORRECT | `chapters/examples/beta_gamma.tex:322-330` gives `c_{bc}=1-3(2\lambda-1)^2`, `c_{bc}(1/2)=1`, `c_{bc}(2)=-26`. |
| C6 | NEEDS REFINEMENT | `chapters/examples/beta_gamma.tex:313-330` supports the canonical formula, but blacklist item (a) is not wrong: `12\lambda^2-12\lambda+2` is algebraically identical to `2(6\lambda^2-6\lambda+1)`. It should be marked “equivalent but noncanonical,” not blacklisted. |
| C7 | CORRECT | `chapters/examples/beta_gamma.tex:627-638` proves `c_{\beta\gamma}+c_{bc}=0`. |
| C8 | CORRECT | Directly follows from C2 by arithmetic; `chapters/examples/landscape_census.tex:688-691` records the Virasoro conductor `26` and self-dual point `13`. |
| C9 | NEEDS REFINEMENT | `CLAUDE.md:15-27` canonizes `k\Omega/z` only for the collision-residue lane, while `chapters/examples/landscape_census.tex:213-216` and `compute/audit/cg_rectify_kac_moody_wave13.md:50-54` record a legitimate KZ normalization `\Omega/((k+h^\vee)z)`. The draft’s averaging sanity check is also wrong in the non-abelian case; see C13. |
| C10 | CORRECT | `chapters/frame/heisenberg_frame.tex:1942,2049,2102,4015` records `r(z)=k/z`, the `k=0` vanishing, and the exact averaging identity. |
| C11 | CORRECT | `chapters/examples/w_algebras.tex:1474-1490` and `chapters/examples/w3_holographic_datum.tex:337` record `r^{\mathrm{Vir}}(z)=(c/2)/z^3+2T/z`; the quartic-to-cubic shift is standard AP19 pole absorption. |
| C12 | CORRECT | Supported by the Heisenberg and Virasoro examples in C10/C11 and by the general `d\log` absorption discussion in `chapters/theory/ordered_associative_chiral_kd.tex:438-440`. |
| C13 | INCORRECT | `chapters/frame/preface.tex:616-624` and `compute/audit/opus_46_failure_modes_wave12.md:131-139` explicitly state the non-abelian affine correction `\operatorname{av}(r)+\dim(\mathfrak g)/2=\kappa`. Blacklist item (a) is therefore actually the correct affine non-abelian formula. |
| C14 | CORRECT | `chapters/theory/introduction.tex:2021-2024` gives `\barB_X(\cA)=T^c(s^{-1}\bar\cA)` with the augmentation ideal; standard bar-construction references agree. |
| C15 | CORRECT | `compute/tests/test_theorem_cross_volume_ap49_engine.py:395-399` verifies the local convention `|s^{-1}v|=|v|-1`; this matches standard bar-complex grading. |
| C16 | NEEDS REFINEMENT | The unordered dimension set is correct by independent Weyl-dimension computation (`compute/lib/bc_exceptional_categorical_zeta_engine.py:244-274,952-987`) and literature-table comparison (`compute/tests/test_bc_exceptional_categorical_zeta_engine.py:158-168`). But the order is not Bourbaki-stable because the local engine uses non-Bourbaki numbering (`compute/lib/bc_exceptional_categorical_zeta_engine.py:48-50`), and the draft’s sum is wrong: the listed numbers add to `7054732527`, not `7056003287`. |
| C17 | CORRECT | `chapters/examples/w_algebras_deep.tex:1195-1198,2331-2332` and `chapters/examples/w_algebras.tex:2190,2317-2319` give strong generators at weights `2,3,\dots,N`. |
| C18 | INCORRECT | `chapters/examples/landscape_census.tex:134-145,688-692` and `compute/lib/wn_central_charge_canonical.py:76-82` show `\kappa+\kappa'=(H_N-1)K_N` for principal `W_N`; `chapters/connections/subregular_hook_frontier.tex:939-949` shows BP has `\kappa+\kappa'=196/6=98/3`, not `196`. |
| C19 | CORRECT | `chapters/examples/w_algebras_deep.tex:611,904,3968` and direct arithmetic confirm `H_N=\sum_{j=1}^N 1/j`. |
| C20 | NEEDS REFINEMENT | `chapters/examples/bershadsky_polyakov.tex:63-67,199-217` proves `K_{\mathrm{BP}}=c(k)+c(-k-6)=196`, but both census sanity checks are false: from the local formula `c(0)=-6`, `c(-6)=202`, and `k=-3` is a pole, not a finite self-dual point. |
| C21 | CORRECT | `compute/lib/cy_borcherds_lift_engine.py:543-547` derives `\mathrm{wt}(\Phi_{10})=10` from the K3 elliptic genus, and `compute/lib/cy_second_quantization_engine.py:1471-1492` gives `\kappa=5`; `compute/lib/bps_entropy_shadow.py:1155-1163` supplies the `\Delta_5^2` half-weight relation. |
| C22 | CORRECT | `chapters/examples/minimal_model_examples.tex:477-478` gives the standard eta expansion with the `q^{1/24}` prefactor. |
| C23 | CORRECT | Independent expansion of `\prod_{n\ge1}(1-q^n)^{-2}` gives coefficients `(1,2,5,10,20,36,\dots)`, matching the draft’s first five terms. |
| C24 | CORRECT | Standard complex analysis gives `[z^{n-1}]f(z)=\frac1{2\pi i}\oint f(z)\,dz/z^n`; `compute/lib/theorem_stokes_mc_engine.py:316-317` uses the same normalization. |
| C25 | CORRECT | `chapters/examples/w_algebras.tex:3884-3886` gives the MC equation with `1/2`, and `chapters/examples/w_algebras.tex:4090-4092` gives the QME with the same `1/2` factor. |
| C26 | CORRECT | `chapters/theory/three_invariants.tex:340-347` records `r_{\max}=2,3,4,\infty` for Heisenberg, affine KM, `\beta\gamma`, and Virasoro respectively. |
| C27 | NEEDS REFINEMENT | The census statement is a true upper bound, but the proved local theorem is sharper: `\ChirHoch^0=\mathbb C`, `\ChirHoch^1=0`, `\ChirHoch^2=\mathbb C`, and zero above (`chapters/theory/hochschild_cohomology.tex:104-114`), so the exact support is `{0,2}`, not “possibly `{0,1,2}`.” |
| C28 | INCORRECT | `chapters/examples/kac_moody.tex:2262-2272` writes KZ as `\Omega\,dz_{ij}/z_{ij}`, while `chapters/theory/ordered_associative_chiral_kd.tex:5093-5101` writes the same connection as `\Omega\,d\log(z_i-z_j)`. The draft’s blacklist therefore forbids an equivalent local notation. |
| C29 | NEEDS REFINEMENT | The matrix-collapse warning is right (`chapters/examples/heisenberg_eisenstein.tex:576-580`), but the Hodge-class formula is not: `\lambda_1=c_1(\mathbb E)` and `\lambda_2=c_2(\mathbb E)` are the local conventions (`chapters/examples/heisenberg_eisenstein.tex:565-567,621-623`), so one should not write `c_1(\lambda_g)`. |
| C30 | INCORRECT | `chapters/connections/concordance.tex:133-141` gives the discriminant formula `\Delta=8\kappa S_4` but also states that class C escapes the single-line dichotomy by stratum separation. This is reinforced by `compute/lib/linf_bracket_engine.py:1069-1072` and `compute/lib/shadow_depth_cross_verification.py:549-554`, where class C has `S_4\neq0`, `\Delta\neq0`, and finite depth `4`. |

## Detailed Derivations for Priority Entries

### C3. Affine KM `\kappa = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`

**Claim.** For the affine VOA `V_k(\mathfrak g)`, the modular characteristic is
`\kappa(V_k(\mathfrak g))=\dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`.

**Independent derivation.**

- The landscape census records the affine line with central charge `kd/(k+h^\vee)` and `\kappa = td/(2h^\vee)` where `t=k+h^\vee` and `d=\dim(\mathfrak g)` (`chapters/examples/landscape_census.tex:76-79`).
- The preface then gives the more structural identity
  `\operatorname{av}(r(z)) + \dim(\mathfrak g)/2 = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee) = \kappa`
  (`chapters/frame/preface.tex:616-624`).
- At `k=0`, this gives `\kappa=\dim(\mathfrak g)/2`.
- At `k=-h^\vee`, it gives `\kappa=0`.

**Comparison to census.** The displayed formula and both boundary checks are correct. The draft correctly resists the old false reflex “`k=0` should force `\kappa=0`.”

**Wave 7-1 nuance.** The census entry itself is fine. The missing nuance is that the identity `\operatorname{av}(r)=\kappa` is not universal for non-abelian affine algebras; the correct local statement is `\operatorname{av}(r)+\dim(\mathfrak g)/2=\kappa`. That issue belongs to C13, not C3.

**Verdict.** CORRECT.

**Confidence.** High.

### C4. Principal `W_N` `\kappa = c(H_N-1)`

**Claim.** For the principal algebra `\mathcal W^k(\mathfrak{sl}_N,f_{\mathrm{prin}})`,
`\kappa = c(H_N-1)`.

**Independent derivation.**

- The general DS formula in the manuscript is
  `\kappa = c\sum_{i=1}^r 1/(m_i+1)`,
  where `m_i` are the exponents of `\mathfrak g`
  (`chapters/examples/w_algebras.tex:2317-2319`).
- For `\mathfrak{sl}_N`, the exponents are `1,2,\dots,N-1`.
- Therefore
  `\kappa = c\sum_{j=2}^N 1/j = c(H_N-1)`.
- The landscape census records exactly this specialization (`chapters/examples/landscape_census.tex:134-137,1380-1382`) and the anomaly-ratio identity `\varrho(\mathfrak{sl}_N)=H_N-1` (`chapters/examples/landscape_census.tex:1219-1223`).

**Boundary checks.**

- `N=2`: `H_2-1=1/2`, hence `\kappa=c/2`, i.e. Virasoro.
- `N=3`: `H_3-1=5/6`, hence `\kappa=5c/6`.

**`K_N` verification.**

- The local census gives `K_N=4N^3-2N-2` with values `K_3=100`, `K_4=246`, `K_5=488` (`chapters/examples/landscape_census.tex:688-692`).
- The compute layer independently gives
  `\kappa+\kappa'=(H_N-1)K_N` and evaluates this to
  `250/3`, `533/2`, and `9394/15` for `N=3,4,5`
  (`compute/lib/wn_central_charge_canonical.py:76-82`).

**Blacklist review.**

- `cH_{N-1}` is genuinely wrong (AP136).
- `c(H_N-1)` and `c\sum_{j=2}^N 1/j` are equivalent; both should be accepted.

**Verdict.** CORRECT.

**Confidence.** High.

### C9. Affine KM classical `r`-matrix

**Claim.** The draft states the canonical affine KM formula is
`r^{\mathrm{KM}}(z)=k\,\Omega/z`,
and blacklists both `\Omega/z` and `\Omega/((k+h^\vee)z)`.

**Independent derivation.**

- `CLAUDE.md` gives `r^{\mathrm{KM}}(z)=k\Omega/z` as the required AP126/AP141 collision-residue form, with the mandatory `k=0` vanishing check (`CLAUDE.md:15-27`).
- But Vol. I also records the affine/KZ triple as
  `(\widehat{\mathfrak g}_k,\widehat{\mathfrak g}_{-k-2h^\vee},\Omega/((k+h^\vee)z))`
  (`chapters/examples/landscape_census.tex:213-216`).
- The rectification note makes the distinction explicit:
  Vol. II uses Costello collision-residue `k\Omega/z`, while Vol. I affine/KZ passages use `\Omega/((k+h^\vee)z)`; both are legitimate but distinct (`compute/audit/cg_rectify_kac_moody_wave13.md:50-54`).
- The KZ connection itself is written locally as
  `d-(1/(k+2))\sum \Omega_{ij}\,dz_{ij}/z_{ij}`
  (`chapters/examples/kac_moody.tex:2262-2272`).

**Comparison to census.**

- The displayed formula is correct only if the entry is explicitly scoped to the Costello/collision-residue normalization.
- The census is wrong to blacklist `\Omega/((k+h^\vee)z)` as a wrong variant; it is a legitimate KZ normalization used in the manuscript.
- The bare `\Omega/z` form is wrong if the affine level `k` is still an explicit variable, but it is not universally “wrong” across all nearby literatures because Yangian/Drinfeld conventions absorb the level.
- The averaging sanity check in the draft is also wrong for non-abelian affine KM; see C13.

**Correct replacement.**

- Collision-residue/Costello normalization: `r(z)=k\Omega/z` with `k=0` vanishing (AP126/AP141).
- KZ normalization: `r(z)=\Omega/((k+h^\vee)z)`.
- Level-absorbed/Yangian normalization: `r(z)=\Omega/z`.

**Verdict.** NEEDS REFINEMENT.

**Confidence.** High.

**Error class.** AP126/AP141 convention conflation.

### C16. `E_8` fundamental dimensions

**Claim.** The eight fundamental `E_8` dimensions are
`{248,3875,30380,147250,2450240,6696000,146325270,6899079264}`.

**Independent derivation.**

- The local exceptional-engine computes representation dimensions by the Weyl dimension formula from positive coroot data (`compute/lib/bc_exceptional_categorical_zeta_engine.py:244-274`).
- The summary routine constructs the eight fundamental highest weights and computes their dimensions directly (`compute/lib/bc_exceptional_categorical_zeta_engine.py:952-987`).
- The test suite independently checks that these computed dimensions match the literature table `_KNOWN_FUND_DIMS['E8']` (`compute/tests/test_bc_exceptional_categorical_zeta_engine.py:158-168`), and the targeted test run passed.

**Comparison to census.**

- The unordered set of eight dimensions is correct.
- The order claim is not stable unless a numbering convention is stated. The local engine explicitly warns that its `E_8` numbering differs from standard Bourbaki (`compute/lib/bc_exceptional_categorical_zeta_engine.py:48-50`).
- The draft’s sum check is wrong. Direct arithmetic gives
  `248+3875+30380+147250+2450240+6696000+146325270+6899079264 = 7054732527`,
  not `7056003287`.

**Verdict.** NEEDS REFINEMENT.

**Confidence.** High.

**Correct form.** Keep the set; drop the unqualified `\omega_1,\dots,\omega_8` ordering unless the numbering convention is named, and correct the total sum to `7054732527`.

### C18. Complementarity sum

**Claim.** The draft defines `K(A)=\kappa(A)+\kappa(A^!)` and then lists the family values, including Bershadsky-Polyakov value `196`.

**Independent derivation.**

- For principal `W_N`, the compute layer gives
  `\kappa+\kappa'=(H_N-1)K_N`
  with `K_N = 2(N-1)(2N^2+2N+1)` (`compute/lib/complementarity_cross_verification.py:128-141`, `compute/lib/wn_central_charge_canonical.py:76-82`).
- Hence:
  `N=3`: `(5/6)\cdot 100 = 250/3`;
  `N=4`: `(13/12)\cdot 246 = 533/2`;
  `N=5`: `(77/60)\cdot 488 = 9394/15`.
- For Bershadsky-Polyakov, the manuscript distinguishes the two constants:
  `K_{\mathrm{BP}}=c(k)+c(-k-6)=196`,
  but
  `\kappa+\kappa' = c/6 + c'/6 = 196/6 = 98/3`
  (`chapters/connections/subregular_hook_frontier.tex:939-949`).

**Comparison to census.**

- KM/free `0` is correct.
- Virasoro `13` is correct.
- `W_3` row `250/3` is correct.
- General `W_N` row `K_N(H_N-1)` is correct.
- BP row `196` is wrong if the quantity being tabulated is `\kappa+\kappa'`.

**Verdict.** INCORRECT.

**Confidence.** High.

**Correct form.**

- If the quantity is `\kappa+\kappa'`, BP should read `98/3`.
- If the quantity is the central-charge conductor `c+c'`, then the header must change, because that is a different invariant.

**Error class.** AP24/AP140-type conductor-vs-`\kappa` conflation.

### C20. `K_{\mathrm{BP}}=196`

**Claim.** The BP conductor is `K_{\mathrm{BP}}=c(k)+c(-k-6)=196`.

**Independent derivation.**

- The local BP central charge is
  `c(k)=2-24(k+1)^2/(k+3)` (`chapters/examples/bershadsky_polyakov.tex:63-64`).
- The dual level is `k'=-k-6`, so
  `c(k')=2-24(-k-5)^2/(-k-3)`.
- The BP chapter expands the sum explicitly and gets `196`
  (`chapters/examples/bershadsky_polyakov.tex:199-217`).
- The targeted BP test suite passed.

**Boundary checks.**

- At `k=0`,
  `c(0)=2-24/3=-6`,
  and at the dual level `k'=-6`,
  `c(-6)=2-24\cdot 25/(-3)=202`.
  Sum: `196`.
- The duality-fixed level is `k=-3`, but `c(k)` has a pole there, so one cannot use `c(-3)=98`.
- The BP chapter instead records the self-dual central charge `c=98` at the complex levels `k=-3\pm 2i` (`chapters/examples/bershadsky_polyakov.tex:65-67`).

**Comparison to census.**

- The canonical formula `K_{\mathrm{BP}}=196` is correct.
- Sanity check 1 is wrong (`c(0)` is `-6`, not `-23/3`).
- Sanity check 2 is wrong (`k=-3` is not a finite self-dual point of the central charge).

**Verdict.** NEEDS REFINEMENT.

**Confidence.** High.

**Correct form.**

- Keep `K_{\mathrm{BP}}=196`.
- Replace the sanity checks with `(k,k')=(0,-6)` giving `(-6,202)`, and with the manuscript’s actual self-dual central-charge statement `c=98` at `k=-3\pm 2i`.

**Error class.** Fixed-point/critical-pole conflation; nearest family resemblance is AP24-style duality-fixed-point confusion.

### C21. Igusa cusp form weight and BKM `\kappa`

**Claim.** `\mathrm{wt}(\Phi_{10})=10=2\kappa`, hence `\kappa=5`.

**Independent derivation.**

- The Borcherds-lift engine states that the Gritsenko-Nikulin lift uses the K3 elliptic genus coefficient `c_0(0)=20`, producing `\Phi_{10}` of weight `c_0(0)/2=10` (`compute/lib/cy_borcherds_lift_engine.py:543-547`).
- The second-quantization engine records the equivalent arithmetic identity
  `\kappa_{\mathrm{BPS}}=\chi(K3)/4-1=5` and `\mathrm{wt}(\Phi_{10})=\chi(K3)/2-2=10`
  (`compute/lib/cy_second_quantization_engine.py:1471-1492`).
- The entropy/shadow engine states the square-root relation explicitly:
  `\Delta_5` has weight `5`, `\Phi_{10}` has weight `10`, and therefore `\mathrm{wt}(\Phi_{10})=2\kappa` (`compute/lib/bps_entropy_shadow.py:1155-1163`).

**Comparison to census.** The factor-of-two explanation is correct, and the blacklisted variants `\kappa=10` and `\mathrm{wt}(\Phi_{10})=5` are genuinely wrong.

**Verdict.** CORRECT.

**Confidence.** High.

## Top 5 Entries Needing Refinement

1. **C13.** Replace the universal statement `\operatorname{av}(r)=\kappa` with a family split: Heisenberg/abelian lanes satisfy it directly; non-abelian affine KM requires `\operatorname{av}(r)+\dim(\mathfrak g)/2=\kappa`.
2. **C18.** Separate the BP central-charge conductor from the BP `\kappa`-sum. If the table is about `\kappa+\kappa'`, the BP entry must be `98/3`, not `196`.
3. **C9.** Scope the affine `r`-matrix by normalization. Mark `k\Omega/z` as the Costello/collision-residue form, `\Omega/((k+h^\vee)z)` as the KZ form, and stop blacklisting the KZ normalization.
4. **C20.** Keep `K_{\mathrm{BP}}=196`, but rewrite both sanity checks. The current `k=0` value and `k=-3` self-dual statement are false.
5. **C30.** Keep `\Delta=8\kappa S_4`, but narrow the criterion to the single-line theorem and explicitly fence the class-C escape by stratum separation. The present global biconditional is false.

## New Wrong Variants Not Already Blacklisted

- **C2:** “Virasoro at `c=0` is abelian.” False; only the central extension vanishes. The Witt bracket remains.
- **C2:** “Virasoro is the unique standard family with `\kappa=c/2`.” False; locally `\beta\gamma` also satisfies `\kappa=c/2` (`chapters/examples/beta_gamma.tex:1212-1218`).
- **C9/C13:** “`\Omega/((k+h^\vee)z)` is a wrong affine KM formula.” False; it is a legitimate KZ normalization in Vol. I.
- **C16:** “The listed `E_8` dimensions sum to `7056003287`.” False; the correct sum is `7054732527`.
- **C20:** “`k=-3` is a self-dual BP level with `c(-3)=98`.” False; `k=-3` is a pole, and `c=98` occurs at `k=-3\pm 2i`.
- **C29:** “`\omega_g = c_1(\lambda_g)`.” False/not well-formed for general `g`; use `\lambda_1=c_1(\mathbb E)` and `\lambda_g=c_g(\mathbb E)`.
- **C30:** “Finite depth iff `\Delta=0`.” False globally; class C gives finite depth by stratum separation with nonzero quartic contact data.

## E8 Dimension Verification

Independent verification path:

- Root/coroot data in `compute/lib/bc_exceptional_categorical_zeta_engine.py`.
- Weyl dimension formula implementation in `compute/lib/bc_exceptional_categorical_zeta_engine.py:244-274`.
- Fundamental highest-weight scan in `compute/lib/bc_exceptional_categorical_zeta_engine.py:952-987`.
- Literature-table comparison in `compute/tests/test_bc_exceptional_categorical_zeta_engine.py:158-168`.

Conclusion:

- The unordered eight-dimensional census set is correct.
- The draft must not claim Bourbaki-ordered `\omega_1,\dots,\omega_8` without specifying numbering.
- The draft’s sum check must be corrected to `7054732527`.

## `K_{\mathrm{BP}} = 196` Verification

Independent verification path:

- Local BP formula `c(k)=2-24(k+1)^2/(k+3)` in `chapters/examples/bershadsky_polyakov.tex:63-64`.
- Duality `k'=-k-6` and explicit computation of `c(k)+c(k')=196` in `chapters/examples/bershadsky_polyakov.tex:199-217`.
- Landscape table confirmation in `chapters/examples/landscape_census.tex:142-145`.
- Passing targeted pytest check on `compute/tests/test_bp_shadow_tower.py`.

Conclusion:

- The conductor value `196` is correct.
- The draft’s supporting sanity checks are not.
- The BP complementarity sum on the `\kappa` side is `98/3`, not `196`.

## Overall Trustworthiness Grade

**Grade: C**

Justification:

- The draft gets most of the basic scalar formulas right.
- It fails on several convention-heavy or family-sensitive entries that are exactly the places where a census must be strict.
- The most serious defects are not random slips; they are structural conflations between normalization, averaging, and which invariant is actually being tabulated.
- After repairing C9, C13, C18, C20, C28, and C30, the draft could plausibly rise to a B-grade authority. In its current form, it is useful only with active cross-checking.
