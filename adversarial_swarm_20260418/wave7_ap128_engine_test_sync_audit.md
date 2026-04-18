# Wave-7 AP128 Engine-Test Synchronization Audit — Vol I Programme-Wide

Date: 2026-04-18. Scope: Vol I (`/Users/raeez/chiral-bar-cobar/compute/`).
Diagnostic only. No edits. No commits. Author: Raeez Lorgat.

APs invoked: AP10 (two-source `# VERIFIED` discipline), AP128 (engine-test
synchronized to same wrong value / shared data table), AP277 (vacuous HZ-IV
body behind sound prose), AP288 (decorator-label vs test-body computation
disjointness), AP287 (structural-impossibility primitive tautology), AP310
(shared intermediate step across decorator paths — newly surfaced here).

Inventory: 1481 test files, 1356 engine modules. 339 `# VERIFIED` comment
hits across 30 sampled files; 40+ test files carry `derived_from` /
`verified_against` HZ-IV decorators.

## 1. Classification scheme

| Class | Meaning |
|-------|---------|
| CLEAN | Test body computes expected from a genuinely disjoint secondary source; AP10 two-source citation honored. |
| AP10-SINGLE-SOURCE | Hardcoded expected has one `# VERIFIED` citation or none; lacks two-category cross-check. |
| AP128-DATA-TABLE | Engine holds a hardcoded dict/list; test consults the same engine (or same module's dict) as ground truth. |
| AP310-SHARED-INTERMEDIATE | Two declared-disjoint HZ-IV paths both pass through a common helper/engine/literal table. |
| AP277-VACUOUS-BODY | Decorator prose sound; body is structural booleans, no numerical cross-check. |
| AP288-RHS-IDENTITY | Three paths declared; body computes all three as same RHS expression with renamed variables. |

## 2. 30-sample table (compact; file:first-line-evidence)

| # | Test file | Engine / source | Category | Notes |
|---|-----------|-----------------|----------|-------|
| 1 | test_chirhoch_dimension_engine.py | chirhoch_dimension_engine.LIE_ALGEBRA_DIMS | AP128-DATA-TABLE | Engine has hardcoded `LIE_ALGEBRA_DIMS` + `DUAL_COXETER_NUMBERS` dicts; test asserts against dict values. Mitigated by Humphreys [LT] + [DC] comments. |
| 2 | test_theorem_H_hochschild_koszul.py | chirhoch_dimension_engine | AP128-DATA-TABLE + AP288 | Decorator cites Feigin-Fuchs/Wang/Whitehead; body pulls `heis.hilbert_triple == (1,1,1)` etc. directly from the same engine. Three "disjoint paths" collapse to one table read. |
| 3 | test_z_g_s_r_arithmetic_duality.py | inline OEIS A000928 + sympy.bernoulli | CLEAN | Verbatim OEIS table + independent `sympy.bernoulli` factorisation + `sympy.factorint` on `N_r` polys. Genuinely three disjoint paths. |
| 4 | test_kappa_conductor.py | inline arithmetic on `K_ghost` formula | CLEAN | FMS tabulated c_ghost {-26, +11, -2} re-derived via explicit formula in test body; no engine delegation. |
| 5 | test_s5_vir_wick.py | s5_vir_wick + Riccati closed form | CLEAN | Wick derivation vs closed-form `-48/(c^2(5c+22))`; two genuinely distinct machineries; boundary c=1 hand-checked. |
| 6 | test_shadow_tower_higher.py | shadow_tower_higher_vir + shadow_tower_ope_recursion | CLEAN | MC recursion vs Riccati sqrt(Q_L) across c ∈ {1, 1/2, 13, 25}; two engines, same answer forced by theorem. |
| 7 | test_virasoro_motivic_purity.py | inline `_s4_vir_shapovalov` Shapovalov path | CLEAN | Three derivation lanes per chapter; verification uses BPZ/Shapovalov/Brown period map, no recursion. |
| 8 | test_ftm_seven_fold_tfae.py | no engine; structural booleans | AP277-VACUOUS-BODY | Sound Priddy/LV12/GK94 prose; body: `assert witness_family in {...}`. Zero numerical content. |
| 9 | test_mc3_five_family.py | no engine; structural booleans | AP277-VACUOUS-BODY | Eight HZ-IV decorators; bodies: `assert len(set(witnesses.values())) == 5` and similar. Prose disjoint; body not exercised. |
| 10 | test_mc5_class_m_chain_level_platonic.py | sympy symbolic identities | AP277-VACUOUS-BODY (partial) | Self-admitted "symbolic/structural" — `_harmonic_discrepancy` is a re-statement, not a cross-check. |
| 11 | test_bp_koszul_conductor_engine.py | bp_koszul_conductor_engine.c_BP | CLEAN | Every expected value derived inline by [DC] `2 - 24(k+1)²/(k+3)`; [SY] / [LC] cross-checks noted. |
| 12 | test_hz_iv_decorators_wave1.py | miura_coproduct_universal_engine + depth_classification + chirhoch + verlinde_ordered | Mixed: CLEAN (Miura Ψ=1 limit) + AP128-DATA-TABLE (chirhoch delegation) | Miura boundary limits {0,1} forced externally (Feigin-Frenkel / classical); chirhoch asserts engine output. |
| 13 | test_ds_coproduct_intertwining_engine.py | ds_coproduct_intertwining_engine | AP10-SINGLE-SOURCE | File-header `# VERIFIED` lists five categories; body defers to engine; engine docstring admits degree-1 tautology (AP257 precedent, Wave-5 #51). |
| 14 | test_periodic_cdg_admissible.py | inline `2**rank` thrice | AP288-RHS-IDENTITY | Wave-9 #61 documented: "ckl_screening_dim with ALL THREE RHS computed as 2**rank in-line." Decorator prose names three paths; body computes one. |
| 15 | test_koszulness_moduli.py | derived_from/verified_against present | Not inspected in depth; likely HZ-IV-W8-B candidate per Wave-11 #75. |
| 16 | test_clutching_uniqueness.py | derived_from/verified_against present | Not inspected; primitive-at-g=1 candidate. |
| 17 | test_topologization_chain_level.py | derived_from/verified_against present | Not inspected; class-L chain-level claim (known retraction zone, AP271). |
| 18 | test_theorem_A_infinity_2.py | derived_from/verified_against present | Not inspected; Theorem A^{∞,2} modular-family scope. |
| 19 | test_theorem_D_modular_characteristic.py | derived_from/verified_against present | Not inspected; AP225 genus-universality zone. |
| 20 | test_theorem_B_scope.py | derived_from/verified_against present | Not inspected. |
| 21 | test_theorem_C_fiber_center.py | derived_from/verified_against present | Not inspected. |
| 22 | test_theorem_A_bar_cobar_isomorphism.py | derived_from/verified_against present | Not inspected. |
| 23 | test_sub_subleading_asymptotic.py | derived_from/verified_against present | Not inspected. |
| 24 | test_virasoro_motivic_rationality.py | derived_from/verified_against | Not inspected. |
| 25 | test_virasoro_motivic_purity_all_r.py | derived_from/verified_against | Not inspected; likely paired with #7 (CLEAN). |
| 26 | test_higher_kummer_arithmetic_duality.py | OEIS + sympy | Likely CLEAN (pattern matches #3). |
| 27 | test_four_tier_kummer_database.py | Kummer tables | Likely CLEAN (OEIS primary). |
| 28 | test_exceptional_yangian_koszul_duality.py | derived_from/verified_against | Not inspected; exceptional Lie dims have FM-LIE-NUMERICS precedent. |
| 29 | test_super_complementarity_sl21.py | derived_from/verified_against | Not inspected; super-Yangian rename AP279. |
| 30 | test_shadow_exponential_base.py | derived_from/verified_against | Not inspected. |

Inspected in depth: 14/30. Not inspected in depth: 16/30 (skeleton shape
captured from grep hits only; finer classification deferred).

## 3. Violation-class breakdown (sample of 14)

| Category | Count | Fraction |
|----------|-------|----------|
| CLEAN | 6 | 43% |
| AP128-DATA-TABLE | 2 | 14% |
| AP277-VACUOUS-BODY | 3 | 21% |
| AP288-RHS-IDENTITY | 1 | 7% |
| AP10-SINGLE-SOURCE | 1 | 7% |
| Mixed / partial | 1 | 7% |

Cleanness ratio 6/14 ≈ 43% is a notable improvement over Wave-7's 1:19
HZ-IV disjointness finding; it suggests the OEIS+sympy+closed-form
triangulation pattern (tests #3, #5-#7) is the HONEST template and
scales. The failures cluster around Theorem H + structural-TFAE proofs
where the claim itself is essentially definitional, and numerical
cross-checks are hard to construct.

## 4. Spot-check of four named engines

### (a) `kappa_bkm_universal.py` (Vol III)

**Verdict: AP310-SHARED-INTERMEDIATE at structural level.**

All six "disjoint paths" in `cross_validate_all_engines()` (paths A–F)
route through `diagonal_siegel_cy_orbifolds.FRAME_SHAPE_DATA`, a
hardcoded dict with literal `borcherds_weight=5, c_disc_0=10, ...`
lines. Paths B/C/D/E/F each `_import_module` and read from the same
table. The formula `kappa_BKM = c(0)/2` is verified against itself.

The `BorcherdsWeightVerification.formula_matches` field is literally
`weight_formula == weight_lit` where both come from the same
`FRAME_SHAPE_DATA[N]` record. `depends_on_CY_A=False` is correct as an
ontological claim but ≠ disjoint verification.

Mitigation: the numerical values {10, 8, 6, 4, 4, 2, 2, 2} for c_N(0)
at N=1..8 trace to Gaberdiel-Hohenegger-Volpato 2010 Frame-shape
tabulation (mentioned in docstring at lines 130-131). If a test
cross-checked at least one value via independent Borcherds-product
convergence OR ran `borcherds_lift.phi01_c_table` as a PARALLEL
computation (not an import of the same table), the decoration would be
honest.

**AP239 (naming after physical source) note**: the κ_BKM(Φ_1)=5
inscription (healed 2026-04-17 via Gritsenko Δ_5) is now correct; but
the disjoint verification that the healed value is 5 (not 10 or 0)
must come from outside FRAME_SHAPE_DATA.

### (b) `chirhoch_dimension_engine.py` (Vol I)

**Verdict: AP128-DATA-TABLE (Wave-6 agent was right).**

Every `chirhoch_<family>()` function returns a hardcoded
`ChirHochData(dim0=1, dim1=dim(g), dim2=1)` triple with inline
`# VERIFIED` comments pointing to chapter lines. The test asserts
`h.dim0 == 1, h.dim1 == 1, h.dim2 == 1` — identical to engine.

Status: mitigated by two-source `# VERIFIED` comments (`[LT]` chapter
citation + `[DC]` Koszul-resolution reasoning + `[SY]` palindrome).
But these are PROSE mitigations in the engine body, not SEPARATE
computational paths in the test.

The test file (`test_chirhoch_dimension_engine.py`) has NO
`derived_from`/`verified_against` decorator — it is a pure engine
regression test. That is appropriate for a data-table engine, PROVIDED
the decorator-style use (in `test_theorem_H_hochschild_koszul.py`,
sample #2) does not pretend three disjoint paths when it just reads
the same engine. Theorem H's `test_theorem_H_chirhoch_concentration_structure`
is the AP128 violation: three HZ-IV paths declared (Feigin-Fuchs,
Wang, Whitehead) but body pulls three triples from one dict.

### (c) `classify_glcm` in `depth_classification.py` (Vol I)

**Verdict: AP277-VACUOUS-BODY (Wave-7 flagged correctly).**

```python
def classify_glcm(alpha, delta):
    if D_zero and a_zero: return ('G', 2, 0)
    elif D_zero and not a_zero: return ('L', 3, 1)
    elif not D_zero and a_zero: return ('C', 4, 2)
    else: return ('M', None, None)
```

A 2×2 Boolean truth table returning hardcoded tuples. Used dual-role:
(1) as the canonical classifier for bar chapters; (2) as the
verification target for `prop:depth-gap-trichotomy` HZ-IV test (sample
#12). The depth-gap theorem states d_alg ∈ {0,1,2,∞} with gap at 3;
the engine returns {0,1,2,None(=∞)} by construction. Verifying the
theorem by asking the engine "what are your output values?" is
precisely AP277.

Mitigation: the test file inspected pairs `classify_glcm` with
`DepthClassification.verify_delta()` which computes
`8*kappa*S_4 - delta` symbolically — that IS a genuine cross-check
against the engine's own output (AP128-adjacent but forward-oriented).
The gap-at-3 assertion should be forced by a MATHEMATICAL argument
(shadow Lie Jacobi, MC relation at degree 4) invoked at the test level,
not by counting outputs of the classifier.

### (d) Z_g Kummer engine

**Not found as a named module.** There is no `z_g_kummer.py` in
`compute/lib/`. The test `test_z_g_s_r_arithmetic_duality.py` (sample
#3) is a STANDALONE test that inlines the OEIS A000928 table and
computes N_r via `sympy.bernoulli` + `sympy.factorint` directly. This
is the gold-standard AP128-CLEAN template: no engine to share source
of truth with, three independent computations in-test.

Related engine candidates reviewed: none matched the description.
`shadow_tower_higher_vir.py` holds S_r closed forms; they are
cross-checked against `shadow_tower_ope_recursion.py` (MC recursion)
at test level — CLEAN.

## 5. Heal recommendations by category

### AP128-DATA-TABLE (chirhoch, FRAME_SHAPE_DATA)

1. DUAL-PATH wiring in HZ-IV decorated tests. For Theorem H: replace
the body's engine read with at minimum ONE independent re-derivation
(e.g., for Heisenberg, invoke the Feigin-Fuchs BRST spectral sequence
engine if it exists, or compute `dim H^i(Vir_c via Fock complex)` via
`fock_resolution.py`; for affine sl_2, use Whitehead+Künneth directly
via `whitehead_kunneth_engine.py` if it exists, else inline).
2. For FRAME_SHAPE_DATA: wire ONE of the paths (say path C,
`borcherds_lift.phi01_c_table`) to RUN the Fourier expansion of
φ_{0,1} in-test; compare path C's numerical output against path A's
table. Path F remains a sanity check, not an independent verification.

### AP277-VACUOUS-BODY (FTM TFAE, MC3 five-family, MC5 class M)

Follow the Wave-11 #75 template: audit each decorator to determine
whether primitive-structural claims are (a) genuinely non-numerical
(flag as HZ-IV-W8-B = STRUCTURAL PRIMITIVE, do not count toward
coverage); or (b) admit a numerical witness at some family (inscribe
the witness). Sample #11 `test_bp_koszul_conductor_engine.py` is the
inscribed-witness template.

### AP288-RHS-IDENTITY (periodic_cdg_admissible)

Already healed (Wave-8 #51 / Wave-9 #61). Extend the Wave-9 lint to
Vol I via `compute/scripts/audit_independent_verification.py`: AST-walk
each `@independent_verification` target; emit warning when all three
declared paths compute on the same RHS expression.

### AP10-SINGLE-SOURCE (ds_coproduct_intertwining)

Engine docstring self-admits "tautology at degree 1" (Wave-5 #51).
Current status sample shows five `[DC]/[LT]/[LC]/[CF]/[NE]` categories
cited at file-header level but body delegates. Healing: re-inscribe
one numerical cross-check at degree ≥ 2 where the intertwining is
non-trivial (AP256 aspirational-heal precedent).

## 6. Systemic observations

1. **"Disjoint at decorator, identical at body" is the modal failure.**
The Wave-7 HZ-IV disjointness audit saw 1/19 CLEAN. This sample of 14
deep-inspected tests sees 6/14 CLEAN, biased by including
test_z_g_s_r / test_kappa_conductor / test_s5_vir_wick / test_shadow_tower_higher
/ test_virasoro_motivic_purity / test_bp_koszul_conductor (all genuinely
good). The improvement is real but concentrated in
recursion-vs-closed-form families (Virasoro shadow, Kummer/Bernoulli).

2. **Structural-TFAE proofs are inherently AP277-prone.** FTM
seven-fold, MC3 five-family, MC5 three-ambient, Koszul 10+1+1 — each
has N decorators with body `assert witness in {...}`. The honest cost
accounting: these are sound at the PROSE level, not at the COMPUTATION
level; they should carry the HZ-IV-W8-B flag and NOT count toward the
Vol I coverage target.

3. **Engine-as-ground-truth pattern (AP128).** Whenever a test imports
from `compute.lib.X_engine` and asserts against X_engine's output,
the test is an engine REGRESSION test, not an independent verification.
These should be renamed `test_X_engine_regression.py` or similar to
distinguish from HZ-IV decorator tests; the HZ-IV `derived_from`/
`verified_against` decorator should be refused on regression tests at
`independent_verification.py` level (new infrastructure).

4. **Infrastructure recommendation.** Extend
`compute/lib/independent_verification.py` with an AST-based check:
(a) walk the decorated function body; (b) collect every `==` RHS; (c)
if any two RHS expressions are AST-identical (after variable
α-renaming), raise `NonDisjointComputationError`. Paired with an
import-time registry to detect shared engine imports across the three
`derived_from` paths.

## 7. Commit plan

**None.** This is a diagnostic audit per the wave brief ("Do NOT apply
heals — this is diagnostic"). Recommended next-wave actions:

- Wave-8: wire FRAME_SHAPE_DATA verification path C to run Fourier
expansion in-test.
- Wave-9: AST-based disjointness lint at import time in
`independent_verification.py`.
- Wave-10: audit the 16 uninspected tests from the 30-sample against
the categories here; inscribe HZ-IV-W8-B flag on all structural-TFAE
tests that survive.
- Wave-11: full Vol I Theorem H HZ-IV re-decoration using disjoint
engines (or mark primitive and do not count).

All work attributed to Raeez Lorgat. No AI attribution.
