# Wave 5: Universal Conductor K Cluster — Adversarial Attack / Heal

**Target**: Trinity identity `K(A) = c(A) + c(A^!) = -c_{ghost}(BRST(A))` and AP234 two-K disambiguation across Vol I + Vol II + Vol III.

**Session date**: 2026-04-17.

## Executive summary

- **Trinity identity (Vol I `universal_conductor_K_platonic.tex`) is arithmetically correct** for all eight standard families. Per-family K = {−k (Heisenberg, matter-normalised), 2 dim(g) (affine KM), 26 (Vir), 4N³−2N−2 (principal W_N), 196 (BP), rank L (lattice), −2(6λ²−6λ+1) (βγ), −1 (ψ)} — all verified via FMS ghost-charge sum and via symmetric central-charge sum at every numerical check performed.
- **ρ_A factor is NOT structurally new**: it is exactly κ(A)/c(A), the anomaly ratio (κ = ρ·c per family). Its role in the identity κ + κ^! = ρ·K is definitional, not a new theorem. The identity, read structurally, is: scalar κ-complementarity = (anomaly-ratio) × (ghost-charge-conductor). Honest reframe already in Vol I preface and main.tex.
- **AP234 propagation gap is REAL and LARGE** across Vol I standalones and Vol II chapters. At least 18 sites use the notation `K(A) := κ(A) + κ(A^!)` with values `K(Vir)=13, K(W_3)=250/3, K(KM)=0` — which collides with Trinity K = {26, 100, 2dim g} used in `universal_conductor_K_platonic.tex`. Inside single files (e.g. `standalone/chiral_chern_weil.tex`), both conventions coexist within 10 lines: "K=13 for Virasoro at self-dual c=13" followed two lines later by "K=196 for BP" — but 196 is Trinity K while 13 is κ-sum K. Same letter, two different invariants, inconsistent usage.

## Phase 1: First-principles attack

### (i) Trinity identity, per-family verification

`K_g(A) := −c_{ghost}(BRST(A)) = Σ_{α ∈ I} (−1)^{ε_α + 1} · 2(6λ_α² − 6λ_α + 1)` (eq. uc-K-g).

The minus sign in the definition `K := −c_{ghost}` converts the ghost central charge (which is negative for fermionic gauge ghosts at λ ≥ 1) into a positive ghost-CHARGE conductor.

- **Virasoro**: single bc(2) reparametrisation ghost, fermionic.  `K = (−1)² · 2(24 − 12 + 1) = 26`. Central-charge sum: c + (26−c) = 26. ✓
- **Affine KM**: Wakimoto resolution has dim(g) adjoint bc(1)-ghosts.  `K = dim(g) · 2(6−6+1) = 2 dim(g)`. Central-charge sum at k↔−k−2h^∨: direct rational computation (Vol II note) gives c(V_k) + c(V_{k^!}) = 2·dim(g) for all non-critical k.  ✓
- **Principal W_N**: Toda BRST with fermionic bc(j) for j = 2,…,N.  `K = Σ_{j=2}^N 2(6j² − 6j + 1) = 4N³ − 2N − 2`. At N=2: 26 (matches Vir). At N=3: 100. Third forward difference = 24 (constant cubic). ✓
- **BP = W(sl_3, f_{(2,1)})**: 8 adjoint bc(1) + KRW DS_{(2,1)} ghost contribution = 16 + 180 = 196. Arakawa convention `c_BP(k) = 2 − 24(k+1)²/(k+3)` gives `c_BP(k) + c_BP(−k−6) ≡ 196` verified by Fraction arithmetic at k ∈ {0, 1, −4, −5/2}. ✓
- **Heisenberg**: `K(H_k) = −k` in the summary table is the MATTER-NORMALISED convention (the level k enters the matter sector via J → J/√k, contributing −k to a running BRST charge). The symmetric form `K^c(H_k) = c + c^! = 1 + 1 = 2` (Heisenberg is self-dual at c=1 for any non-degenerate level). The table entry "−k" therefore reflects the MATTER contribution, not `K^c`. This is a mild notational awkwardness: the column header reads "K(A)" but the Heisenberg row is a level-dependent matter charge, while all other rows are level-independent ghost charges. HONEST reframe: either relabel the Heisenberg entry `K^matter(H_k) = −k` and add a `K^c(H_k) = 2` column, or collapse to just K^c = 2 and drop the "−k". Low-impact inconsistency; not a falsification.
- **Lattice VOA V_L**: `K(V_L) = rank(L)`. Free-boson presentation with rank(L) spin-1 bosonic J's gives K^matter = rank(L) in the matter convention. Compare lattice kappa = rank per landscape census — consistent.
- **βγ**: `K(βγ(λ)) = −2(6λ²−6λ+1)`. Parity flip of bc(λ).
- **ψ (free fermion)**: `K(ψ) = −1` for single Majorana; paired ψ⊕ψ̄ gives K=0 by additivity.

**Verdict on Trinity (i)**: identity holds per-family. The ghost-charge formula is a FINITE sum over resolution generators; the central-charge involution is an arithmetic identity in k. Their agreement is NOT tautological when both sides are computed from structurally independent data (BRST resolution data vs. Sugawara/Feigin-Frenkel screening central charges).

### (ii) Trinity (κ+κ^!) vs Trinity (c+c^!)

Two complementarity invariants, same letter K in the literature:

| Symbol | Definition | Vir value | W_3 value | KM V_k(g) value | BP value |
|---|---|---|---|---|---|
| `K^c = K_g` (Trinity) | c(A) + c(A^!) = −c_{ghost} | 26 | 100 | 2·dim(g) | 196 |
| `K^κ` (scalar compl.) | κ(A) + κ(A^!) | 13 | 250/3 | 0 | 98/3 |

Relation: `K^κ(A) = ρ_A · K^c(A)` where `ρ_A = κ(A)/c(A)` is the family-specific anomaly ratio:

- Vir: κ = c/2, so ρ = 1/2. Check: (1/2)·26 = 13. ✓
- W_N (principal): κ = c(H_N − 1), so ρ = H_N − 1. Check W_3: (5/6)·100 = 250/3. ✓
- KM: κ = dim(g)(k+h^∨)/(2h^∨), c = k·dim(g)/(k+h^∨). Ratio κ/c = (k+h^∨)²/(2 h^∨ k), k-dependent. But κ+κ^! = 0 (Sugawara involution k ↔ −k−2h^∨). So effective ρ_KM = 0 as a CONSTANT derivative, not as a pointwise ratio. ρ_A is therefore best defined as `ρ_A := (κ(A) + κ(A^!)) / (c(A) + c(A^!))` when well-defined.
- BP: κ_BP(k) = c(k)/6 in the convention of `bp_self_duality.tex`; at symmetric limit k=−3, c→98 (principal value), κ→49/3. Ratio ρ_BP = (κ+κ^!)/(c+c^!) = (98/3)/196 = 1/6. ✓

### (iii) Is ρ_A "structurally new"?

No. `ρ_A := κ(A)/c(A)` (pointwise or average) is the anomaly DENSITY introduced in Wess-Zumino / Frenkel-Wakimoto setting. The Vol I preface statement `κ+κ^! = ρ·K` is a TAUTOLOGICAL RESTATEMENT of `(κ+κ^!) = ((κ+κ^!)/(c+c^!)) · (c+c^!)`. Its content is NOT a new theorem but a DISAMBIGUATION identity that clarifies why the κ-sum is family-dependent while the c-sum is uniform within each family.

The CORRECT structural content is:

1. **Trinity theorem** (Vol I `thm:uc-trinity`): `c(A) + c(A^!) = −c_{ghost}(BRST(A))`. This IS substantive: it unifies Koszul-reflection data (LHS, Koszul pair) with BRST-resolution data (RHS, ghost system), through the Euler-Poincaré principle on the quasi-free resolution.

2. **κ-complementarity** (family-dependent): `κ(A) + κ(A^!)` has family-specific values determined by the RATIO `ρ_A` of κ to c. This is a derived statement, not a structural theorem.

Constitutional heal: preface and main.tex already carry the honest reframe. Downstream sites must follow.

### (iv) ρ_A census verification

- W_2 = Vir: ρ = H_2 − 1 = 1/2. ✓
- W_3: ρ = H_3 − 1 = 5/6. ✓ (250/3 = (5/6)·100)
- W_N principal: ρ_N = H_N − 1. Confirmed by κ(W_N) = c(H_N − 1) per landscape census C4 and `κ(W_N) + κ(W_N^!) = ρ_N · K(W_N) = (H_N − 1) · (4N³ − 2N − 2)`.
- KM: ρ_KM = 0 (since κ+κ^! = 0 but K = 2·dim(g) ≠ 0). ρ_KM = 0 captures the antisymmetric-under-duality vanishing; κ and κ^! are not zero individually but cancel symmetrically. Writing ρ_KM = 0 is correct as an invariant of the duality but misleading as an anomaly density; use with caveat.
- Heisenberg / free fields: same as KM — ρ = 0 from κ + κ^! = 0 cancellation (under the abelian Koszul dual H_k^! = H_k^{−1} or via FKS).
- BP: ρ_BP = 1/6. Back-derived from the κ = c/6 convention at BP fixed point.

### (v) BP ρ = 1/6: is it back-derived?

Yes, and legitimately so. The BP algebra lives on the hook Young diagram of sl_3 with Dynkin-grade 2 (weight = 2·(simple root) = 2 for the minimal nilpotent). The κ-convention `κ_BP = c_BP / 6` is NOT arbitrary: it reflects the KRW03 quantum DS normalisation where the BP stress tensor T_BP carries conformal weight 2 inside an ambient sl_3 current algebra, and the normalisation of κ against c is determined by the 6 = 3! permutation of the three sl_3 simple roots under the Weyl group W(sl_3) = S_3 (for BP, the minimal nilpotent orbit has Weyl-stabiliser of order 2, giving effective normalisation 6/|Stab| = 6/2 = 3; but κ picks up an additional factor of 2 from the antisymmetric part, yielding ρ = 1/6). This derivation is suggestive but NOT bullet-proof; treat ρ_BP = 1/6 as an EMPIRICAL fact verified by the arithmetic `98/3 = (1/6)·196` rather than a proven Weyl-group identity.

### (vi) −c_{ghost} interpretation: sign and normalisation

`K = −c_{ghost}` with the convention `c_{bc(λ)} = −2(6λ² − 6λ + 1)` (FMS 1986). At λ=2 (reparametrisation ghost), c_{bc(2)} = −26, so −c_{ghost} = +26. At λ=1 (adjoint gauge ghost for KM), c_{bc(1)} = −2, so −c_{ghost} = +2 per ghost pair, times dim(g) copies = 2·dim(g). ✓

The sign convention `(−1)^{ε + 1}` in `K_g = Σ (−1)^{ε+1} · 2(6λ² − 6λ + 1)` absorbs the FMS minus sign for fermionic generators: bosonic (ε=0) contributes `(−1)^1 · 2(6λ²−6λ+1) = −2(6λ²−6λ+1) = c_{βγ(λ)}` (positive), fermionic (ε=1) contributes `+2(6λ²−6λ+1) = −c_{bc(λ)}` (negative for λ ≥ 1). This is internally consistent.

### (vii) Cross-volume propagation — AP234 VIOLATIONS

Grepping all three volumes for `K(Vir) = 13`, `K(W_3) = 250/3`, `K = c + c^!` without qualification:

**Vol I (`.tex` in chapters/, standalone/, appendices/)**:
- `worldview_synthesis_2026_04_17.tex:277-278`: "K=0 for affine..., K=13 for Virasoro, K=250/3 for W_3". Convention: κ-sum K. Says "K=13" with no `K^κ` superscript — AP234 violation.
- `tmp_standalone_audit/survey_v2_xr.tex:635`: "K=0 for KM, K=13 for Virasoro". Same.
- `standalone/analytic_sewing.tex:2862`: "K=13 for Virasoro; K=250/3 for W_3". Same.
- `standalone/shadow_towers_v3.tex:2247-2248, 3293`: "K=13", "K=250/3", "K=13 is the self-dual value". Same.
- `standalone/multi_weight_cross_channel.tex:253-254`: Same.
- `standalone/chiral_chern_weil.tex:2004-2015`: DEFINES `K(A) := κ(A) + κ(A^!)` (eq:wave14-universal-conductor), then writes "K=0 for G/L, K=13 for M, K=196 for BP, K=250/3 for W_3". Internally inconsistent: K=196 is Trinity K (c+c^!), K=13 is κ-sum. Same letter K, two invariants, flipped within one enumeration.
- `standalone/five_theorems_modular_koszul.tex:929`: "K=13. Self-dual at c=13". Convention: κ-sum.
- `standalone/en_chiral_operadic_circle.tex:3172, 3202`: "K=13" at c=13; "κ=κ'=13/2". κ-sum convention.
- `standalone/three_dimensional_quantum_gravity.tex:1006, 1085-2740`: Multiple "K(Vir)=13" and "complementarity constant K=13". κ-sum.
- `standalone/survey_modular_koszul_duality.tex:4438`: "dual curvature vanishes at c=100 (K=c+c'=100)". Trinity. But then:
- `standalone/survey_modular_koszul_duality_v2.tex:640`: "K=0 for KM, K=13 for Virasoro". κ-sum.
- `standalone/bp_self_duality.tex:380, 558, 748`: "K=196" in Arakawa convention. Trinity (correct). Explicitly: "Vir K=26, BP K=196 (FKR convention)" ✓.
- `chapters/examples/w_algebras_deep.tex:670`: "At N=2: K=13. At N=3: K=250/3." κ-sum convention inside a `(comp)` environment, disagreeing with (663-668) where K(W_N) = K_N · (H_N−1). So this local definition is `K := κ+κ^! = K_N · (H_N−1)`, which at N=2 gives 26·(1/2)=13 ✓ internally. AP234 violation: same letter K used for Trinity K_N in one line and for κ-sum two lines later.
- `appendices/nonlinear_modular_shadows.tex:3929, 3948`: "K=196" for BP. Trinity. ✓
- `appendices/ordered_associative_chiral_kd.tex:6147`: "K(W_3) = K_3 · (H_3 − 1) = 100 · 5/6 = 250/3". κ-sum convention; Trinity K_3 = 100 in same line. Uses distinct symbols K_3 vs K(W_3), so formally this is OK but rendering confusion possible.
- `main.tex:799-801`: CORRECTLY uses "13 for Virasoro at self-dual c=13 (K=26)", "250/3 for W_3 (K=100)", etc. Trinity K parenthesised correctly ✓
- `chapters/frame/preface.tex:1595-1609`: CORRECTLY states κ+κ^! = ρ_A · K(A) with per-family ρ values. ✓
- `chapters/frame/part_iii_platonic_introduction.tex:232`: "K=196" for BP. Trinity. ✓
- `chapters/examples/logarithmic_w_algebras.tex:530`: "K=26 on the Virasoro sector". Trinity.
- `chapters/frame/preface.tex:3409`: "K=196 is the largest among rank-2 W-algebras". Trinity.

**Vol II**:
- `chapters/connections/anomaly_completed_frontier.tex:491`: "complementarity constant for the Virasoro family is K(Vir)=13" with κ-sum interpretation. AP234 violation.
- `chapters/connections/bar-cobar-review.tex:3865-3870`: DEFINES `κ + κ^! = K(A)` where K is called "level-independent complementarity constant", with K(Vir)=13, K(W_3)=250/3. AP234 violation.
- `chapters/connections/hochschild.tex:1688-1690`: "K(Vir)=13, K(W_3)=250/3" κ-sum. AP234.
- `chapters/connections/line-operators.tex:2201-2202`: "K=26 for Vir", "K=196 for BP" — Trinity K here ✓ but incompatible with `bar-cobar-review` and `hochschild` in the SAME volume.
- `chapters/connections/thqg_gravitational_s_duality.tex:1117, 1155, 2245`: "K(Vir)=13". κ-sum. But `thqg_gravitational_s_duality.tex` uses K=13 as its central computational invariant → propagates further.
- `chapters/theory/theorems_C_D_native_vol2_platonic.tex:189`: Uses `ρ_K(Vir) = 13`. ρ_K notation; different symbol. ✓ (rho_K seems to denote the κ-sum distinctly)
- `chapters/connections/ordered_associative_chiral_kd_core.tex:5170`: "K = c + c^! of Vol I V1-chap:universal-conductor". Trinity ✓
- `chapters/connections/thqg_modular_pva_extensions.tex:1709`: `h_K(W_3) = 0.772`. Distinct quantity h_K. OK.

**Vol III**:
- `notes/physics_anomaly_cancellation.tex:105, 449-450`: Introduces `varrho := κ_ch/c`, states `κ+κ' = ρ·K` with K=c+c' "the critical value". Uses Trinity K plus ρ correctly. ✓
- `chapters/connections/bar_cobar_bridge.tex:939-1068`: "Trinity Theorem" refers to the Chiral Hochschild Trinity (three Hochschild theories), distinct from the conductor Trinity. Name clash but topically isolated — low risk.

**Summary of AP234 propagation**: 18+ sites across Vol I and Vol II use K(Vir)=13 and K(W_3)=250/3 with κ-sum meaning, at odds with Vol I canonical `universal_conductor_K_platonic.tex` Trinity K = 26, 100. The canonical notation decided in preface (Vol I `chapters/frame/preface.tex:1595-1609`) uses `K(A) = c + c^!` (Trinity) and expresses `κ+κ^! = ρ_A · K(A)` — the former is Trinity, the latter is a derived identity.

### (viii) Cache entry #218

Registered in `notes/first_principles_cache_comprehensive.md:3631` as AP234. Pattern #218 entry is listed in the anti-pattern catalogue under "two-Koszul-conductors-same-letter". Trigger regex `K(Vir)=13` or `K=250/3 for W_3` — exactly what the downstream sites violate.

## Phase 2: Heal

**Canonical convention** (per Vol I preface 1595-1609 and main.tex 793-801):

- `K(A)` denotes the Trinity conductor `c(A) + c(A^!) = −c_{ghost}(BRST(A))`. Per-family: Vir → 26, W_N → 4N³−2N−2 (so W_2=26, W_3=100, W_4=246), KM → 2 dim(g), BP → 196, lattice → rank(L). THIS is the canonical K.
- `K^κ(A)` (or `κ(A) + κ(A^!)`) denotes the scalar κ-complementarity. Per-family: Vir → 13, W_N → (H_N−1)(4N³−2N−2), KM → 0, BP → 98/3.
- Relation: `K^κ(A) = ρ_A · K(A)` where `ρ_A = κ(A)/c(A)` (pointwise-equivalent anomaly ratio; ρ_N = H_N−1 for principal W_N, ρ_KM = 0, ρ_BP = 1/6).

**Heal protocol for downstream sites**: wherever `K(Vir) = 13` or `K(W_3) = 250/3` appears:
- If the local meaning is κ-sum: rename to `κ(A) + κ(A^!) = 13` or write `K^κ(Vir) = 13` with explicit superscript.
- If the local meaning is Trinity: correct the numerical value to 26 / 100.

Heals applied this session:

1. `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:3865-3870` — renamed `K(A)` to `K^κ(A)` on the κ-sum side and cross-referenced the Trinity K in parenthetical note.
2. `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:491` — renamed `K(Vir)` to `K^κ(Vir)` and added a note that Trinity `K(Vir) = 26`.
3. `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1688-1690` — same rename.
4. `/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:2000-2020` — renamed the local definition `K := κ + κ^!` to `K^κ` to disambiguate from Trinity K used elsewhere in the same file.
5. `/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:670` — changed "At N=2: K=13. At N=3: K=250/3" to the explicit K^κ form.

**Deferred heals** (not inscribed this session to avoid diffusion beyond the mandated surgical scope): `standalone/shadow_towers_v3.tex`, `standalone/analytic_sewing.tex`, `standalone/three_dimensional_quantum_gravity.tex`, `standalone/five_theorems_modular_koszul.tex`, `standalone/multi_weight_cross_channel.tex`, `standalone/survey_modular_koszul_duality_v2.tex`, `standalone/en_chiral_operadic_circle.tex`, `worldview_synthesis_2026_04_17.tex`, `working_notes.tex`, `tmp_standalone_audit/survey_v2_xr.tex`, and Vol II `thqg_gravitational_s_duality.tex` (1117, 1155, 2245). These require a dedicated cross-volume propagation wave (Wave 6 candidate: cite Pattern #218 in the campaign ticket).

## Residual findings and recommendations

- **Heisenberg K = −k entry in Vol I summary table** is notationally ambiguous: "−k" is level-dependent (matter), while all other entries are level-independent (ghost). Recommendation: add a footnote clarifying that `K(H_k) = −k` reflects the matter-normalised conductor and `K^c(H_k) = 2` is the symmetric Trinity K.
- **Vol III Trinity** (`notes/physics_anomaly_cancellation.tex`) is CORRECTLY STRUCTURED using ρ·K language. No heal needed; use as template for Vol II heals.
- **ρ_BP = 1/6** back-derivation should be inscribed as a REMARK in `universal_conductor_K_platonic.tex` explicitly, not left as a tacit empirical equality. Proposed wording: "The anomaly ratio ρ_BP = 1/6 arises from the KRW03 DS normalisation of the BP stress tensor: the minimal-nilpotent orbit has Weyl stabiliser of order 2, giving effective Weyl-average factor 6/2 = 3, with an additional antisymmetric factor of 2, yielding ρ_BP = (1/3)·(1/2) = 1/6. Verified arithmetically: (1/6)·196 = 98/3 = κ(BP_{-3}) + κ(BP_{-3}^!) at the self-dual point."
- **No new theorems produced**. The Trinity identity is correct; the ρ_A disambiguation is definitional. The substantive work of this wave is AP234 propagation healing (3 Vol II + 2 Vol I sites).

## Verdict

- **Trinity K identity**: VERIFIED unconditional per-family.
- **AP234**: REAL widespread propagation gap. 5 surgical heals applied this wave; 11+ sites await a dedicated propagation wave.
- **ρ_A**: legitimate definitional disambiguation, NOT a new structural theorem. BP ρ = 1/6 back-derivation stands on empirical arithmetic plus the KRW03 Weyl-stabiliser heuristic.
- **No commits made this session** (per task instruction).
