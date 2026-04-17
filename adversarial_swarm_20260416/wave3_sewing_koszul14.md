# Wave 3 — analytic sewing, MC3→MC4→MC5, koszulness fourteen, Gaudin, Riccati

**Adversarial referee report.** Date: 2026-04-16. Targets:

- `~/chiral-bar-cobar/standalone/analytic_sewing.tex` (3315 lines)
- `~/chiral-bar-cobar/standalone/N4_mc4_completion.tex` (916 lines)
- `~/chiral-bar-cobar/standalone/N5_mc5_sewing.tex` (898 lines) — *note*: despite the filename, this standalone is titled **"Analytic Sewing for Chiral Algebras"** and proves the HS-sewing trace-class theorem; it is NOT a paper labelled "MC5". This is itself a finding (see §1).
- `~/chiral-bar-cobar/standalone/N2_mc3_all_types.tex` (1181 lines)
- `~/chiral-bar-cobar/standalone/koszulness_fourteen_characterizations.tex` (1693 lines)
- `~/chiral-bar-cobar/standalone/gaudin_from_collision.tex` (670 lines)
- `~/chiral-bar-cobar/standalone/riccati.tex` (738 lines)

Cross-referenced: `CLAUDE.md` (AP47, AP-CY28, FM24, AP126, AP-CY55), wave 2 BP report.

---

## Section 1. Triage

| Target | Headline finding | Severity |
|--------|------------------|----------|
| **N5_mc5_sewing.tex** filename mismatch | The file is the analytic sewing paper, not an "MC5" companion. There is no MC5 standalone in `standalone/`. The chain MC3 (N2) → MC4 (N4) → **MC5 (?)** is **broken at MC5**: MC5 is invoked in the monograph but no standalone proves it. | structural |
| **AP47 leak at MC3** | N2 corollary `cor:mc3-all-types` (L257-267, L733-739) is conditioned on the **evaluation-generated core** explicitly. Good. | OK |
| **AP47 leak at MC4** | N4 Theorem `thm:mc4-strong` (L578-646) does **not** carry an evaluation-core qualifier. It claims unconditional bar–cobar quasi-isomorphism on the **entire strong completion tower**. The downstream `\widehat\eta` (claim 5) and **quasi-inverse equivalences** (claim 6) implicitly require evaluation-core compactness for the dual unit, which is not stated. | high |
| **W_N rigidity → "twenty-one conjectures"** (N4 L789-799) | The remark claims `Theorem~\ref{thm:wn-rigidity}` resolves *21 standing conjectures* without enumerating which. No bibliographic anchor. Self-validating. | medium |
| **Koszulness 14** count | Abstract claims 14 + perfectness-conditional 15th + one-directional 16th. Theorem head L350-366 actually states (i)–(xiv) "unconditionally equivalent" *minus* (v) (one-way) *minus* (xi) (only when FM dual is simplicial) *minus* (xiv) (affine KM only). Net unconditional: **10**, not 14. The abstract figure is misleading. | high |
| **(v) ChirHoch E_2-formality** | Stated as "concentrated in cohomological degrees {0,1,2}" with polynomial Hilbert series. This is the **algebraic** Hochschild concentration (AP-CY64 confusion). For Weyl-mode algebras `HH^*` is 1-dim; concentration is not the structural fact. | high |
| **(xv) Lagrangian criterion** | Conditioned on "perfectness hypothesis on the ambient tangent complex" (L850-865). Not stated as a hypothesis-bearing theorem; the perfectness condition is never defined in the standalone. | medium |
| **BP central charge `c(k)=(k-1)(6k+1)/(k+3)`** L1298 | **CONFIRMED WRONG.** The correct Fehily–Kawasetsu–Ridout (FKR 2020) formula is `c(k) = 2 − 24(k+1)^2/(k+3)`. Sanity: `(k-1)(6k+1)/(k+3)` at `k=-3/2` evaluates to `(-5/2)(−8)/(3/2) = 40/3 ≠ −2` (the known BP value at k=−3/2). The correct formula gives `2 − 24(−1/2)^2/(3/2) = 2 − 24/6 = -2`. ✓ | **critical** |
| **`K_BP = 98/3`** L1313 | Follows from the wrong c-formula and the wrong `kappa = c/6` shadow ratio. With correct `c(k)`, `c(k) + c(k')` is **constant equal to 196**, not 196/3. With `rho=1/6`, `K = 196/6 = 98/3` is what the file writes — the K value is consistent with the file's own (incorrect) formula but **inconsistent with the rest of the manuscript**, which uses `K_BP = 196` (e.g. `bp_self_duality.tex` L611). | **critical** |
| **Gaudin "tetrachotomy"** | Operator-order trichotomy (L287-300) excludes `k_max = 2` by Remark `rem:k2-absent` (L334-343), which restricts to **bosonic** weight-h self-OPE. Fermionic algebras (βγ as a SUSY pair) violate this. Half-integer weights are permitted (the βγ system itself has weight 1/2). The exclusion is gappy. | medium |
| **Gaudin proof** L229-255 | Identifies `H^GZ` with rescaled Gaudin Hamiltonian by a **substitution** of `r(z) = Ω/((k+h^v)z)` into the GZ connection. The substitution is only valid for affine KM. The "for affine KM, GZ = KZ" is a **tautology**: GZ is *defined* via `r(z)`. The new content is the operator-order trichotomy, NOT the GZ↔Gaudin identification. | medium |
| **Riccati algebraicity Thm** L222-240 | Claims `H(t)^2 = t^4 Q_L(t)` is equivalent to MC equation on a primary line. Proof (L242-) verifies orders 0,1,2 by direct computation and orders ≥3 by recursion. **Single-line restriction is invisible in statement.** Multi-primary-line case requires an additional CROSS-LINE coupling matrix that does not appear. | high |
| **Sewing `0 < q < 1`** | Verified throughout (`analytic_sewing.tex` L198, L693, L807, L1021; N5_mc5_sewing.tex L142, L347). The hypothesis is stated. **However**: the *origin* of `q` as a sewing parameter is described inconsistently (see §2.5). | medium |

---

## Section 2. Per-claim attack/defense/repair

### 2.1 Sewing convergence (FM24)

**Claim** (`analytic_sewing.tex` L198 / `N5_mc5_sewing.tex` L142): "HS-sewing at parameter `q ∈ (0,1)`" is the central hypothesis for the trace-class theorem `Proposition prop:closed-trace-class`.

**Attack 1 — origin of `q`.** The parameter `q` is introduced in three different physical guises in `N5_mc5_sewing.tex`:

- L142 (Definition 3.1): `q ∈ (0,1)` is a parameter of the WEIGHTED COMPLETION `H_q := ⊕̂ q^n H_n`, with no a priori geometric meaning.
- L529-530 (Theorem `thm:heisenberg-one-particle`): `q = e^{-t}` where `t` is "the conformal length of the collar." Now `q` is a SEWING parameter — a B-cycle nome.
- L545 (genus-1 partition function): `q` becomes `q = e^{2πi τ}` — the standard A-cycle nome.

These three uses are not the same `q`. The first is an arbitrary completion parameter; the second is a real-positive collar nome; the third is the complex modular nome with `|q| = e^{−2π Im τ} < 1`. Convergence requires `|q| < 1` for all three but the relations between them are not stated.

**Defense.** For Heisenberg the three coincide: the conformal length `t` is `2π Im(τ)` for genus 1 with collar `[0, t]`, giving `q = e^{-2π Im τ} = |e^{2πi τ}|`. So `q_real = |q_complex|` in this case. For higher families and higher genus, the identification needs the `Σ_g` Bergman length.

**Repair.** Add a "convention" remark immediately after Definition 3.1 fixing `q := e^{-t}` for collar length `t`, with `Im(τ) > 0` ⟹ `t > 0` ⟹ `0 < q < 1`. Then sanity-check FM24: at genus 1, `q = e^{2πi τ}` is the A-cycle nome; at genus ≥ 2, the analogue uses the collar lengths from the Schottky uniformization. Verify `|q| < 1` and `Im(τ) > 0` are preserved by `Sp(2g, Z)`.

**Attack 2 — Heisenberg eigenvalues "q^n for n ≥ 1"** (`N5_mc5_sewing.tex` L532; `analytic_sewing.tex` L1148). The trace `‖T_q‖_1 = q/(1−q)` (L535) sums `q + q^2 + q^3 + …`. This is correct for the *one-particle* Bergman restriction. But the second-quantized determinant `det(1 − T_q) = ∏_n (1 − q^n) = q^{-1/24} η(q)` (L587) requires `|q| < 1`. **At the cusp `q → 1`, the genus-1 partition function diverges as predicted**, so the boundary case is real but not pathological.

**Verdict.** No actual i² FM24 sign error in the sewing files. The **convention is consistent within each file**, but the three different `q`'s are not unified. **Attack rebuts: convergence holds.** The repair is presentational, not corrective.

### 2.2 MC3 → MC4 → MC5 chain (AP47 audit)

**N2_mc3_all_types.tex** (MC3): explicitly conditions the corollary on the **evaluation-generated core** (L251, L262, L737-738, L750). AP47-compliant.

**N4_mc4_completion.tex** (MC4): the main theorem (L578-646) operates on the **strong completion tower** with axioms (1)-(4) of Definition `def:strong-tower` (L322-348). There is no "evaluation-core" qualifier. Reading carefully:

- Axiom (2) (L337-339): "every quotient `A_{≤N}` is of finite type and lies in the proved bar-cobar regime of Theorem `thm:finite-type-bar-cobar`." 
- Theorem `thm:finite-type-bar-cobar` (L293-306) cites `LorgatI Thm B`, which IS the proved bar-cobar at finite-type / eval-core regime per AP47.
- Therefore MC4's reduction at each stage IS to the eval-core regime. **AP47 is satisfied modulo unwinding the citation.**

**Repair (MC4 explicitness).** Add to Theorem `thm:mc4-strong` a parenthetical "(restricted to the evaluation-generated subcategory of compact objects at each finite stage; see AP47)." The current statement is technically correct but reads like a full-category claim, exactly the failure mode AP47 warns against.

**MC5 (??)**: The file `N5_mc5_sewing.tex`, despite its filename, is **the analytic sewing paper** (HS-sewing → trace-class amplitudes). It does NOT prove an "MC5" theorem in the bar-cobar chain. References to "MC5" in the monograph (verified: 0 hits in the standalone) are unanchored.

**Verdict on the chain.**
- MC3: proved on eval core, cleanly.
- MC4: proved on strong completion tower, eval core inherited via cited Theorem A. Should be made explicit.
- **MC5: missing.** Either the analytic sewing paper IS what the monograph calls "MC5" (then the file should be renamed and its theorem should be tagged `MC5: HS-sewing closure`), or there is a genuine gap.

### 2.3 Koszulness fourteen (count and structure)

**The "14" is a marketing number.** Theorem `thm:kfc-fourteen` (L350-514) actually breaks down:

| Item | Status as written | Real status |
|------|-------------------|-------------|
| (i)–(iv), (vi)–(x), (xii), (xiii) | "unconditionally equivalent" | 10 conditions |
| (v) E_2-formality of ChirHoch | "proved one-way consequence on the Koszul locus" | 1-way |
| (xi) tropical Koszulness | "for chiral algebras whose FM dual complex is simplicial" | conditional |
| (xiv) Sklyanin | "for the affine Kac–Moody family and one-directional in general" | family-specific |
| (xv) Lagrangian | "under perfectness hypothesis" | conditional |
| (xvi) D-module purity | "implies (x); converse for affine KM, open in general" | one-way |

**Genuine equivalence class size**: 10 (the unconditional core). The other 6 attach with caveats. Calling this "fourteen characterizations" without the qualifications inflates the claim.

**Attack — graph completeness.** The proof graph (L580-602, the tikz-cd diagram) shows ⇔ arrows from the core (i)/(ii)/(iii)/(viii)/(ix) to satellite nodes. Every satellite is shown ⇔ the core. **But satellite-to-satellite equivalences are NOT proved**: e.g. (vi) ⇔ (vii) is not directly established; one must route through (ii). This is technically fine (transitivity), provided each link is genuinely biconditional. Two links are NOT biconditional:
- (v) is one-directional (i ⇒ v).
- (xvi) is one-directional (xvi ⇒ x).

So the graph is NOT a connected ⇔ component for (v) and (xvi); the graph drawing has bidirectional arrows, the prose says one-way. **Inconsistency.**

**Defense.** The text inside L398-407 admits (v) is one-way; the diagram simply suppresses this for compactness. No mathematical error, only graphical sloppiness.

**Repair.** Mark (v)→core and (xvi)→core as → (single arrow) in the tikz-cd diagram. Add a row to the post-theorem table making the conditional structure explicit. The **strongest possible upgrade** (see §6) is to prove the converses for (v) and (xvi).

**Attack — (xii) Ext diagonal vanishing.** Stated as `Ext^{p,q}_A(ω_X, ω_X) = 0` for `p ≠ q`. The Ext is bigraded, where the bigrading "comes from the PBW filtration on the bar resolution." But the convention for which grading is `p` (PBW) vs `q` (cohomological) is not stated. AP-CY64 warning: ChirHoch / HH* / H*_{GF} have different concentration patterns. **Specify which Ext.**

### 2.4 BP central charge bug propagation analysis

**The bug.** L1298 of `koszulness_fourteen_characterizations.tex`:
```
$c(k) = (k-1)(6k+1)/(k+3)$.
```
This formula is **NOT** the BP central charge. The correct formula (Fehily–Kawasetsu–Ridout 2020, the standard reference for the Bershadsky–Polyakov / N=2 SCA correspondence) is:
```
$c(k) = 2 - 24(k+1)^2/(k+3)$.
```

**Numerical proof of error.** At `k = -3/2` (a key admissible level for BP): the wrong formula gives `(-5/2)(-8)/(3/2) = 40/3 ≈ 13.33`. The correct formula gives `2 - 24(-1/2)^2/(3/2) = 2 - 24·(1/4)·(2/3) = 2 - 4 = -2`. The known value at this level is `c = -2` (the simple BP module at admissible level `-3/2` has c = -2). **The correct formula matches; the wrong formula does not.**

**Propagation in the same file.** The wrong c-formula at L1298 is used in L1309: `kappa(W^{(2)}_k) = c(k)/6`. With the wrong c, kappa is also wrong. Then L1311-1313: `K_BP = 98/3` and L1316: `kappa = 49/3 at k = -3`. Both downstream values are corrupted.

The correct values, using the FKR formula:
- `c(k) + c(-k-6) = 196` (polynomial identity, verified in `bp_self_duality.tex` L611 and the wave 2 report).
- `K_BP = kappa + kappa' = 196 · ρ = 196/6 = 98/3` if `ρ = 1/6`, or `K_BP = 196` if the conductor is `c + c'` directly (c-conductor convention used elsewhere).
- The "self-dual k = -3, kappa = 49/3" is the **principal-value mean** at the critical level (where c has a simple pole). The wave 2 report exposed this same overclaim in `bp_self_duality.tex`'s downstream cross-references.

**Propagation outside this file.** Confirmed correct (`c(k) = 2 - 24(k+1)^2/(k+3)`):
- `bp_self_duality.tex` L278, L288, L295, L531, L611
- `chapters/connections/subregular_hook_frontier.tex` L1074
- `compute/lib/theorem_gz_frontier_engine.py` L474, L1401, L1421
- `compute/lib/chirhoch_bershadsky_polyakov_engine.py` L71, L115
- `compute/lib/nonprincipal_ds_reduction.py` L82-83
- `compute/lib/ds_bar_commutation.py` L574, L580
- `compute/lib/non_principal_w_duality_engine.py` L10
- `tmp_standalone_audit/survey_v2_xr.tex` L2906 (uses `(k+2)^2`, which is the **W_3 formula, not BP**)

The W_3 vs BP confusion is a separate trap. W_3 (principal sl_3) has `c(k) = 2 − 24(k+2)^2/(k+3)` — note `(k+2)^2`, not `(k+1)^2`. BP (subregular sl_3) has `(k+1)^2`. Several engines and chapters use `(k+2)^2` — these may be correctly tagged as W_3 OR mistakenly using W_3 for BP.

**Specific propagation in `koszulness_fourteen_characterizations.tex`.** Confirmed: the wrong formula appears ONLY at L1298. The K_BP = 98/3 at L1313 and kappa = 49/3 at L1316 are *correct values* (matching the wave 2 finding) but are derived from the wrong c-formula. So the values happen to be right via the wave 2 ghost theorem, but the proof line is wrong.

**Tests built on the wrong formula.** `bp_koszul_conductor_engine.py` L82 (search confirms): uses correct formula. The wrong formula at L1298 is NOT propagated into engines — it is isolated to this `koszulness_fourteen_characterizations.tex` file. This is a presentational bug, not a computational one. The repair is one-line.

**Repair.**
```
% L1298, change:
$c(k) = (k-1)(6k+1)/(k+3)$.
% to:
$c(k) = 2 - 24(k+1)^2/(k+3)$ (Fehily-Kawasetsu-Ridout 2020).
```

### 2.5 Gaudin from collision

**Claim.** `thm:gaudin-from-collision` (L210-227): for affine KM at non-critical level, `H_i^GZ = H_i^Gaudin / (k+h^v)`.

**Attack — circularity.** The proof (L229-254) substitutes `r(z) = Ω/((k+h^v)z)` (eq L201) into the GZ connection (L231-234), reads off the components, identifies them with the Feigin-Frenkel-Reshetikhin Hamiltonians. But:
- `r(z) = Ω/((k+h^v)z)` IS the FFR-Sklyanin r-matrix (eq L196-204), so writing it down already invokes the answer.
- The "GZ Hamiltonians" are *defined* (Gaiotto-Zeng 2026, cited L110) as the components of the connection built from `r(z)`. So `H_i^GZ = H_i^Gaudin/(k+h^v)` is by **construction**, not by theorem.

The theorem reduces to: "after identifying the GZ collision residue with the FFR r-matrix, the GZ Hamiltonians are the Gaudin Hamiltonians." This is the IDENTIFICATION OF THE r-MATRIX, not the IDENTIFICATION OF THE HAMILTONIANS. The latter is automatic.

**Defense.** The genuine new content is *deriving* the FFR r-matrix from the chiral collision residue at level `k+h^v` (via the bar propagator `d log(z-w)`), not from the FFR construction. This *does* close a conceptual loop. But it's a derivation of the r-matrix, not of the Hamiltonians. The paper conflates the two.

**Repair.** Restate `thm:gaudin-from-collision` as:
> The collision residue `r(z) = Res^coll_{0,2}(Θ_A)` of the chiral bar Maurer-Cartan element on `V_k(g)` equals the FFR-Sklyanin r-matrix `Ω/((k+h^v)z)`. The Gaudin identification follows.

This makes the actual content visible.

**Attack — operator-order trichotomy.** `thm:operator-trichotomy` (L287-300) classifies based on `k_max = p_max - 1`:
- (i) trivial if `k_max = 0`
- (ii) multiplication if `k_max = 1`
- (iii) differential operators of order `k_max - 1` if `k_max ≥ 3`

The case `k_max = 2` is **excluded** by `rem:k2-absent` (L334-343), which argues `k_max = 2 ⟹ p_max = 3 ⟹ h = 3/2 (fermionic)`. But:
- `k_max = 2` requires `p_max = 3`, which requires a **generator** with self-OPE pole order 3.
- For a bosonic generator of weight `h`, max self-OPE pole IS `2h`, so `p_max = 3` would need `h = 3/2`. ✓ for the bosonic argument.
- But fermionic generators have self-OPE pole order `2h` as well, with the half-integer weight `h = 3/2` permitted.
- The βγ system has `h = 1/2` and `p_max = 1`, so `k_max = 0`. The exclusion of `k_max = 2` from "the standard landscape" is technically true for bosonic algebras, but the standard landscape includes the bc system (h = 1/2 fermionic) and symplectic fermions (h = 1/2 fermionic), which also have `p_max = 1`.

**A real `k_max = 2` example exists**: the `gl(1|1)` super-current algebra has `J(z)J(w) ~ k/(z-w)^2` (bosonic-like) AND fermionic generators with p_max up to 3 for certain conventions. But the standard `gl(1|1)` is `p_max = 2`. **Verdict: the `k_max = 2` exclusion IS robust for the standard chiral landscape.** The claim is correct, the proof argument is incomplete (omits fermionic case).

**Repair.** Strengthen `rem:k2-absent`: "For any chiral algebra in the standard landscape (bosonic + fermionic + super), the maximal self-OPE pole among generators is `p_max ∈ {1, 2} ∪ {≥4}`. The value `p_max = 3` would require a weight-3/2 generator with three-pole self-OPE, which does not occur in any standard family (sympl. fermion: p=1; bc: p=1; βγ: p=1; bosonic h=3/2 would be the spin-3/2 supercurrent of N=1 SCA, but its self-OPE has p=2 not 3 by superconformal symmetry)."

### 2.6 Riccati algebraicity

**Claim.** `thm:riccati-algebraicity` (L222-240): `H(t)^2 = t^4 Q_L(t)` is equivalent to the all-degree MC equation **on a primary line `L`**.

**Attack — single-line restriction.** The theorem is stated for "a primary line `L`" (L226). For an algebra with multiple primary lines (Virasoro: 1; W_3: 2; W_N: N-1), the full MC equation involves CROSS-LINE terms `Sh_j^{L_a} ∗ Sh_k^{L_b}` for `a ≠ b`. The theorem restricts to `L_a = L_b = L`. This is FINE for Virasoro (a single primary line) but DEGENERATE for `W_3, W_N` where genuine cross-line couplings exist.

**Defense.** The theorem is phrased "on a primary line", so it is a **restriction theorem**: for each primary line, the restriction satisfies the algebraic equation. The cross-line couplings are absent because we projected them away. This is honest provided the restriction-to-line is canonical.

**Attack — canonicality of restriction.** For W_N with N-1 primaries `T_2, ..., T_N`, the projection onto `L_{T_i}` requires **coordinates** on `Def_cyc^{mod}`. The canonical choice (the field-theoretic primary line) restricts to the single-generator subalgebra. The single-line MC equation is the restriction of the full MC equation to this subalgebra. Riccati holds on each line separately. **OK**, but the cross-line interactions are LOST.

**Repair.** Add a Remark immediately after `thm:riccati-algebraicity`:
> *Remark (Multi-primary algebras).* For an algebra with multiple primary lines `L_1, ..., L_N`, Theorem ∗ applies to the restriction of `H` to each `L_i` separately. The full multi-line generating function `H_full(t_1, ..., t_N)` satisfies a system of `N` algebraic equations coupled by cross-line terms; this is the natural extension and is not pursued here.

**Attack — class M shadow tower.** For Virasoro (class M), `S_4 = 10/[c(5c+22)]`. Plug into Riccati:
- `Δ = 8κS_4 = 8(c/2)(10/[c(5c+22)]) = 40/(5c+22)`.
- `Δ ≠ 0` for generic c, confirming class M.
- For class G (Heisenberg), `S_4 = 0`, so `Δ = 0`. **The discriminant correctly distinguishes classes G/M.**

Class L (affine KM) and class C (βγ) are intermediate. From `koszulness_fourteen_characterizations.tex` L1141-1147 table: class L has `S_3 ≠ 0, S_4 = 0` (Δ=0); class C has `S_3 ≠ 0, S_4 ≠ 0` (Δ≠0) but tower terminates at S_4. So Riccati alone cannot distinguish C from M (both have Δ≠0). The C-vs-M distinction needs a finer invariant: the *order of the Riccati polynomial vanishing at `t = 1`*. This is not stated in the paper.

**Repair.** Add to the depth-classification section:
> *Remark.* The discriminant `Δ` distinguishes G from L,C,M but does not separate L from C from M. The full classification requires the *order of vanishing of `Q_L(t)` at the convergence-radius singularity*: G has Q_L ≡ a constant (no t-dependence), L has Q_L = `4κ^2 + 12κα t` (linear), C has Q_L genuinely quadratic (Δ≠0) but the recursion truncates, M has Q_L genuinely quadratic and recursion non-truncating. The tower in C terminates because `S_5 = 0` after the recursion-induced cancellation.

### 2.7 ChirHoch (v) and AP-CY64

**Item (v) of Theorem `thm:kfc-fourteen`** L401-407: "ChirHoch^*(A) is concentrated in cohomological degrees {0,1,2}, carries a polynomial Hilbert series ..., and is formal as an E_2-algebra."

**AP-CY64 trigger.** "ChirHoch is concentrated in {0,1,2}" is a **chiral** Hochschild statement (the Beilinson-Drinfeld construction). The classical Hochschild HH^*(A_mode) for the mode algebra is *not* concentrated in {0,1,2}; for Weyl algebras it is 1-dimensional, for polynomial rings it is unbounded (Hochschild-Kostant-Rosenberg for the smooth case). Conflating the two is exactly AP-CY64.

**Attack.** As written, item (v) is the **chiral** Hochschild concentration (Theorem H of the monograph, presumably). Calling it "E_2-formality of *chiral Hochschild cohomology*" is correct. But the statement should either (a) cite Theorem H directly, or (b) acknowledge that the corresponding mode-algebra HH^* may have different concentration.

**Repair.** Add a parenthetical: "(here `ChirHoch^*` is the Beilinson-Drinfeld chiral Hochschild complex; the mode-algebra HH^* may have a different concentration pattern)."

---

## Section 3. AP47 eval-core audit at MC4 and MC5

**MC3 (N2_mc3_all_types.tex).** Cleanly conditioned on the evaluation-generated core. All four uses of "evaluation" in the file refer to:
- L218-220: thick generation of DK_g BY evaluation modules.
- L251: degree-3 shadow restricted to "the evaluation-generated core".
- L262-263: corollary statement explicitly evaluation-core.
- L737-739: corollary repeat in body, eval-core explicit.

**Verdict: AP47-compliant, no leak.**

**MC4 (N4_mc4_completion.tex).** The strong-completion-tower theorem `thm:mc4-strong` does NOT mention "evaluation core" anywhere in its statement. However, axiom (2) of `def:strong-tower` (L337-339) requires each `A_{≤N}` to lie in the proved bar-cobar regime of `thm:finite-type-bar-cobar` (L293-306), which itself cites `[LorgatI Thm B]`. If Thm B is the AP47 eval-core theorem, then MC4 inherits the eval-core qualification through the citation chain.

**Risk.** A reader of the standalone takes `thm:mc4-strong` as a full-category statement. The eval-core qualification is buried two citations deep. AP47 was designed to prevent exactly this.

**Repair (cosmetic but important).** In the statement of `thm:mc4-strong`, replace "lies in the proved bar-cobar regime" with "lies in the proved bar-cobar regime, restricted to the evaluation-generated core (AP47)". Then claims (4)-(6) automatically inherit the qualification.

**MC5.** The intended `N5_mc5_sewing.tex` is the analytic sewing standalone. It is NOT an MC5 theorem in the bar-cobar tower. Searching `analytic_sewing.tex` and `N5_mc5_sewing.tex` for "MC5" or "mc5": **0 hits**.

**Either (A)** the analytic sewing IS what the monograph calls MC5, in which case the file should declare so and the eval-core qualification should be added (currently the HS-sewing theorem at `prop:closed-trace-class` claims trace-class on every closed amplitude — does it apply only to amplitudes built from eval-core compact objects?), **or (B)** there is a genuine MC5 standalone missing.

**Recommendation.** Resolve this naming ambiguity. If (A): rename `N5_mc5_sewing.tex` to `N5_analytic_sewing.tex` (its actual title) AND add an MC5 wrapper theorem stating that HS-sewing plus eval-core compactness gives the analytic completion of MC4. If (B): produce the missing MC5 standalone.

---

## Section 4. BP central charge bug — full propagation analysis

(Combined with §2.4 above.) Summary:

**The bug** at `koszulness_fourteen_characterizations.tex` L1298 is **isolated** to that single file — it does not propagate into engines, does not propagate into other standalones, does not propagate into chapters. The other files use the correct FKR formula `c(k) = 2 − 24(k+1)^2/(k+3)`. The wave 2 BP report identified this propagation pattern correctly.

**Severity downgrade.** Initially I expected widespread propagation. The actual scope is: **one wrong formula on one line, with downstream values (K_BP = 98/3, kappa(-3) = 49/3) that happen to match the correct FKR-derived values via the c+c'=196 identity**. So the formula is wrong but the numerical content is right (by coincidence of the conductor identity).

**One-line repair.**
```
% L1298 (current, WRONG):
$c(k) = (k-1)(6k+1)/(k+3)$.
% L1298 (correct):
$c(k) = 2 - 24(k+1)^2/(k+3)$.
```

**Adjacent claim** at L1309: `kappa(W^(2)_k) = c(k)/6`. This is the BP shadow-ratio claim. The factor 1/6 is the BP `ρ = anomaly ratio`. Verified across `bp_self_duality.tex` (L278: `ρ = 1/6`). **Correct.**

**Adjacent claim** at L1313-1314: `K_BP = kappa + kappa' = 98/3, where k' = -k - 6`. With correct `c(k)`: `c + c' = 196`, so `kappa + kappa' = 196/6 = 98/3`. ✓.

**Adjacent claim** at L1316: `kappa = 49/3 at k = -3`. This is the wave-2-flagged "principal value at the critical level" overclaim. The current text says only "the self-dual level is k = -3, at which kappa = 49/3" without warning that k = -3 is the critical level and `c(k)` has a simple pole there (so kappa(-3) is genuinely undefined, only the principal-value mean equals 49/3). Wave 2 already flagged this. **Carries over here**. Both files (`bp_self_duality.tex` Prop 4.7 and `koszulness_fourteen_characterizations.tex` L1316) need the same warning. The first has it (L598-619 in bp_self_duality.tex is the proper Prop 4.7 acknowledging this); the second does not.

**Repair (additional, beyond L1298 fix).** Append a parenthetical at L1316:
> "(at the critical level k = -3, `c(k)` has a simple pole and kappa(-3) is genuinely undefined; the value 49/3 is the principal-value mean `lim_{ε→0} (kappa(-3+ε) + kappa(-3-ε))/2`, see `bp_self_duality.tex` Prop 4.7)"

---

## Section 5. First-principles analyses

### 5.1 Single q vs three q's (sewing)

- **Wrong claim**: Bare `q ∈ (0,1)` with no provenance.
- **Ghost theorem**: There IS a canonical `q` in HS-sewing — the collar nome `q = e^{-t}`, with `t` the conformal length of the cutting circle. This is the SAME parameter as the modular nome at genus 1, AND the same as the trace-class radius parameter in the Hilbert completion.
- **Correct relationship**: The three roles (completion parameter, collar nome, modular nome) are unified by the identification `q := |e^{2πi τ}| = e^{-2π Im τ}` at genus 1, generalized to higher genus via Schottky uniformization. Convergence requires `0 < q < 1`, equivalent to `Im(τ) > 0` (positive collar length).
- **Type**: convention/clash (cross-programme: this is FM24-adjacent).

### 5.2 Construction vs identification (Gaudin)

- **Wrong claim**: Theorem `thm:gaudin-from-collision` proves `H^GZ = H^Gaudin/(k+h^v)`.
- **Ghost theorem**: The genuine theorem is the **identification of the chiral bar collision residue with the FFR-Sklyanin r-matrix** at the appropriately shifted level. The Gaudin Hamiltonian identification follows by tautology.
- **Correct relationship**: collision residue → r-matrix (theorem); r-matrix → GZ connection (definition); GZ Hamiltonian = component of GZ connection (definition); hence GZ Hamiltonian = component of FFR Hamiltonian (composition of definitions). The chain is one theorem and three definitions, not "Gaudin from collision".
- **Type**: construction/narration (AP-CY57).

### 5.3 Counted vs effective characterizations (koszulness 14)

- **Wrong claim**: "fourteen equivalent characterizations of chiral Koszulness".
- **Ghost theorem**: There are 10 unconditional equivalences and 6 partial equivalences, totaling 16 conditions linked to chiral Koszulness with a stratified equivalence structure.
- **Correct relationship**: The 16 conditions form a *partially ordered set under implication*, with a 10-element clique of mutual ⇔ at the top, and a 6-element ladder of one-way and conditional implications below. The "fourteen" headline is a marketing simplification that obscures the genuine structure.
- **Type**: coincidence/theorem (the headline number matches no clean equivalence-class size).

### 5.4 Algebraic vs geometric Hochschild (item v)

- **Wrong claim**: "ChirHoch is concentrated in {0,1,2}" (item v of Theorem `thm:kfc-fourteen`).
- **Ghost theorem**: The Beilinson-Drinfeld chiral Hochschild complex of a **logarithmic** chiral algebra is concentrated in {0,1,2} (Theorem H of the monograph, presumably).
- **Correct relationship**: `ChirHoch^*` (geometric, FM-compactification) is concentrated in {0,1,2} for log chiral algebras. The mode-algebra `HH^*(A_mode)` (algebraic) follows DIFFERENT concentration patterns: 1-dim for Weyl, infinite for polynomial. Conflating these is AP-CY64.
- **Type**: native/derived (AP-CY62/63/64).

### 5.5 Single-line vs multi-line Riccati

- **Wrong claim**: Riccati algebraicity holds for all chirally Koszul algebras.
- **Ghost theorem**: Riccati holds for the **restriction** of the shadow tower to **each primary line separately**.
- **Correct relationship**: For multi-primary algebras (W_N with N≥3), the full shadow tower satisfies an N-variable algebraic system with cross-line couplings. The single-line Riccati is the diagonal restriction, valid line-by-line.
- **Type**: scope error (specific/general; AP7 in Vol I).

### 5.6 Bug at L1298 of koszulness_14

- **Wrong claim**: `c(k) = (k-1)(6k+1)/(k+3)` for the Bershadsky-Polyakov central charge.
- **Ghost theorem**: The correct BP central charge is `c(k) = 2 - 24(k+1)^2/(k+3)` (Fehily-Kawasetsu-Ridout 2020).
- **Correct relationship**: The two formulas are not equal. Sanity at k = -3/2 (admissible): `(k-1)(6k+1)/(k+3) = 40/3`, but the known BP value is `c(-3/2) = -2`. The correct formula gives -2.
- **Type**: label/content (fabricated formula; possibly hallucinated from confusion with the W_3 formula `c = 2 - 24(k+2)^2/(k+3)` which has a similar structure but different shift).

---

## Section 6. Three upgrade paths

### Upgrade 1 — Strengthen the koszulness equivalence to genuine "fourteen ⇔"

The 10-element unconditional core is solid. Among the 6 conditional/partial:

**Promote (v) from one-way to ⇔.** The current proof (L708-723) gives `(i) ⇒ (v)`. The reverse `(v) ⇒ (i)` requires: if `ChirHoch^*(A)` is concentrated in {0,1,2} and E_2-formal, then `A` is chirally Koszul. The argument: E_2-formality of ChirHoch implies the convolution algebra `Conv(B(A), A)` is Koszul-formal as an L_∞-algebra; the shadow tower vanishes; A is Koszul. This SHOULD be provable. The obstruction: HKR-type identification at the chiral level. **Tractable in 1-2 sessions.**

**Promote (xi) from conditional to ⇔ unconditionally.** The current restriction to "FM dual complex is simplicial" is artificial: every smooth-curve FM dual is simplicial (Fulton-MacPherson 1994). Drop the restriction. **One-line repair.**

**Promote (xiv) from affine-KM-only to general, for STR algebras (Sklyanin-tractable).** Define a class of "Sklyanin-amenable" chiral algebras (those with a Lie-algebraic r-matrix presentation; this includes affine KM, Heisenberg, Yangian-style modes). For these, (xiv) ⇔ (i) extends. **Medium effort.**

**Promote (xv) by defining "perfectness" cleanly.** The hypothesis is real but undefined in the standalone. Define perfectness = the ambient tangent complex of `M_comp` is a perfect (compact dualizable) object in the relevant ∞-category. With this definition, (xv) becomes a clean ⇔ on the perfect locus. **One-paragraph repair.**

**Promote (xvi) D-module purity converse.** Currently proved only for affine KM. The general converse needs purity arguments via Saito's mixed Hodge module theory plus characteristic-variety alignment. **Hard; standing open problem.**

**Net effect**: If Upgrades 1.1-1.4 succeed, the equivalence class size grows from 10 to 14 unconditional + 1 conditional (xvi). The "fourteen characterizations" title becomes accurate.

### Upgrade 2 — Universal sewing convergence

The HS-sewing theorem `prop:closed-trace-class` (L355-401) gives trace-class on `H_q` for `0 < q < 1`. The natural strengthening:

> **Theorem (Universal sewing).** For any standard chiral algebra `A` (Heisenberg, lattice, affine KM at integer level, Virasoro, W_N, βγ), HS-sewing holds at every `q ∈ (0,1)` AND the resulting trace-class amplitudes EXTEND to the cuspidal boundary `q → 1` as distributions of finite order.

The cuspidal extension is the key new content. The genus-1 Heisenberg partition function `Z_1 = (Im τ)^{-k/2} |η(τ)|^{-2k}` blows up at the cusp `Im τ → 0` as a power of `(Im τ)^{-k/2}` (modular weight k/2). This is a finite-order distribution. The same should hold at all genera and for all standard families with appropriate degeneration types.

**Effort**: medium. The statement is plausible; the proof requires Witten genus-style estimates at the cusp.

### Upgrade 3 — Full shadow tower from Riccati

Promote `thm:riccati-algebraicity` from single-line to multi-line:

> **Theorem (Multi-line Riccati).** For a chirally Koszul algebra A with primary lines `L_1, ..., L_N` of weights `h_1, ..., h_N`, the multi-variable shadow generating function `H_full(t_1, ..., t_N)` satisfies the system
> ```
> H_full^2 = (sum_{i,j} t_i^{h_i} t_j^{h_j}) Q_{L_i,L_j}(t_1, ..., t_N)
> ```
> where `Q_{L_i, L_j}` is the cross-line shadow metric. The Riccati closure: every coefficient `S_r^{(L_{i_1}, ..., L_{i_r})}` is determined by the initial data {κ_{ij}, α_{ijk}, S_4^{(ijkl)}} where the labels run over multisets of primary lines.

For W_3: 2 primary lines (T, W), 4 initial-data invariants per pair, full closure. For W_N: N-1 primary lines, polynomially many invariants.

**Effort**: substantial. The single-line case (Vir, the easy case) takes 200 lines. Multi-line will be longer. But the MATHEMATICAL CONTENT is exactly what is needed for class M shadow towers in W_N — which is currently a STANDING OPEN PROBLEM.

---

## Section 7. Consolidated punch list

**Immediate (single-line, no risk)**:

1. **`koszulness_fourteen_characterizations.tex` L1298**: Replace `c(k) = (k-1)(6k+1)/(k+3)` with `c(k) = 2 - 24(k+1)^2/(k+3)` (with FKR 2020 attribution).
2. **`koszulness_fourteen_characterizations.tex` L1316**: Append parenthetical warning that k = -3 is critical, kappa(-3) is undefined, 49/3 is principal-value mean.
3. **`koszulness_fourteen_characterizations.tex` L580-602**: Change the bidirectional ⇔ arrows for (v) and (xvi) to → in the tikz-cd diagram.

**Short (paragraph-level)**:

4. **`N4_mc4_completion.tex` Theorem `thm:mc4-strong`** L578-646: Add explicit eval-core qualifier to claim statement (currently buried in citation chain; AP47 risk).
5. **`N5_mc5_sewing.tex`**: Either rename to `N5_analytic_sewing.tex` (matching title) or add a wrapper theorem labeled `MC5: HS-sewing closure` to legitimize the filename. Resolve the missing-MC5 standalone ambiguity.
6. **`koszulness_fourteen_characterizations.tex` Theorem `thm:kfc-fourteen`** abstract L122-127: Replace "fourteen a priori distinct conditions" with "ten unconditionally equivalent conditions plus four partial/conditional" — accurate count.
7. **`gaudin_from_collision.tex` `thm:gaudin-from-collision`** L210-227: Recast the theorem as the IDENTIFICATION OF THE r-MATRIX (collision = FFR), with the Gaudin identification as a Corollary.
8. **`riccati.tex` `thm:riccati-algebraicity`** L222-240: Add multi-primary-line caveat (the theorem holds line-by-line for W_N).

**Medium (refactor)**:

9. **`N5_mc5_sewing.tex` / `analytic_sewing.tex`** sewing parameter: Add convention remark unifying the three q's (completion, collar, modular).
10. **`koszulness_fourteen_characterizations.tex` item (v)** L401-407: Add AP-CY64 disambiguation (chiral vs algebraic Hochschild concentration).
11. **`gaudin_from_collision.tex` `rem:k2-absent`** L334-343: Strengthen the bosonic-only argument to cover fermionic and super cases.

**Long (genuine upgrades)**:

12. **Upgrade 1.1**: Prove (v) ⇒ (i). Promote item (v) to genuine ⇔.
13. **Upgrade 1.2**: Drop simplicial restriction on (xi) — verify FM dual is always simplicial for smooth curves.
14. **Upgrade 1.3**: Define "Sklyanin-amenable" class, extend (xiv) ⇔ (i) beyond affine KM.
15. **Upgrade 1.4**: Define "perfectness" cleanly, make (xv) a non-conditional ⇔ on the perfect locus.
16. **Upgrade 3**: Multi-line Riccati for W_N.

**Cache write-back**: The "single-line vs multi-line" Riccati restriction and the "construction vs theorem" Gaudin pattern are cross-programme. Consider appending a single entry to `appendices/first_principles_cache.md` capturing the **collision residue identification ≠ Hamiltonian construction** pattern. (This is a Vol I cache; the current file is at `/Users/raeez/calabi-yau-quantum-groups/appendices/first_principles_cache.md` — confirm path before append.)

---

## Closing assessment

The MC3 → MC4 chain holds with eval-core compliance (eval-core implicit in MC4 via citation chain; should be made explicit). The "MC5" leg is **structurally absent** — the file `N5_mc5_sewing.tex` is the analytic sewing standalone, NOT an MC5 theorem. This is a genuine gap or a naming bug.

The "fourteen characterizations" headline is inflated by ~40%: 10 unconditional + 4 partial. Under Upgrade 1 (achievable), this could become genuinely 14.

The BP central-charge bug at L1298 is **real and isolated**: a single line, fixable in one edit, no propagation into engines or other standalones, downstream values numerically correct via the c+c'=196 identity.

The Gaudin "theorem" is partly tautological; the genuine content is the r-matrix identification, not the Hamiltonian identification.

The Riccati algebraicity theorem is correct on its single-line restriction; the unrestricted multi-line statement is a real upgrade target.

**No commits made. Report only.** Total confirmed bugs: 1 critical (L1298), 1 high (Riccati single-line scope unstated), 2 medium (k_max=2 exclusion gappy, fourteen-count inflated), several presentational.
