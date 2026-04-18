# HZ-IV Programme-Wide Disjointness Audit -- Wave 7 (2026-04-18)

Adversarial auditor: Etingof / Polyakov / Kazhdan / Gelfand / Nekrasov /
Kapranov / Bezrukavnikov / Costello / Gaiotto / Witten. AP277 / AP287 /
AP288 / AP310 discipline. Diagnostic only; no edits, no commits.

## 1. Programme-wide enumeration

Raw grep (`@independent_verification|@assert_sources_disjoint|verified_against|derived_from`):

| Volume | total grep hits | files touching an HZ-IV keyword |
|---|---|---|
| Vol I (`/Users/raeez/chiral-bar-cobar`) | 806 | 57 |
| Vol II (`/Users/raeez/chiral-bar-cobar-vol2`) | 948 | 60 |
| Vol III (`/Users/raeez/calabi-yau-quantum-groups`) | 675 | 82 |
| **Programme total** | **2429** | **199** |

These counts include `derived_from` and `verified_against` keyword
occurrences inside each decorator block; a single decorator typically
produces ~5 hits. Conservative decorator-level estimate: ~400-500 HZ-IV
decorators programme-wide.

Notable concentrations:
- Vol II `test_climax_theorems_wave*_iv.py` (waves 3-18): ~20 decorators
  per file, 15 wave files, every one pre-flagged `HZ-IV-W8-B` by the
  Wave-10 scan (primitive tautology, `assert True` bodies).
- Vol I `test_hz_iv_decorators_wave{1,2}.py`, `test_mc3_five_family.py`,
  `test_shadow_tower_higher.py` (56 hits): load-bearing, numerical.
- Vol III `test_hyperkahler_anchored_fixed_point.py` (159 hits): the
  heaviest single file in the programme.

## 2. Twenty-decorator sample (compact table)

Columns: path / claim / P1-P2-P3 bibkeys (compact) / test-body computation
signatures / shared intermediate / verdict.

| # | file:line | claim | P1 | P2 | P3 | body | shared intermediate | verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | vol1 `test_theorem_H_hochschild_koszul.py:51` | thm:main-koszul-hoch | bar+PBW+OS / FM-formality / -- | FeiginFuchs1984 | Wang1998+Whitehead+Kunneth | three `chirhoch_*` engine calls | `chirhoch_dimension_engine` is the single source of truth; Feigin-Fuchs and Wang are BIBLIOGRAPHIC, not executed | **AP288** (three paths collapse to one engine; prior audit flagged) |
| 2 | vol1 `test_ds_coproduct_intertwining_engine.py:605` | thm:ds-intertwining (deg >= 2) | Tsymbaliuk R-matrix | Miura cross-engine | level-by-level integer k | `verify_psi2_intertwining()` + `delta_psi_sl3 - delta_psi_w1inf` | all three paths re-call the same `verify_psi2_intertwining` closure | **AP310** (shared intermediate; session ledger flagged) |
| 3 | vol3 `test_cy_c_six_routes_generator_level.py:~160` | thm:cy-c-six-routes | MO stable envelope | Huybrechts Chow motive | Kummer MV | hard-coded `RHO_PENTAGON` dict + structural checks | `{3,12,24}` hardcoded; no engine call to any of the three paths | **AP277** + **test-encoded-tautology** (AP290 type-swap already healed at variable-name level) |
| 4 | vol2 `test_climax_theorems_wave18_iv.py:14` | prop:pants-product-HH | Costello2007 | KS2009 | -- | `assert True` | n/a | **AP287** (primitive tautology; HZ-IV-W8-B flag present) |
| 5 | vol2 `test_climax_theorems_wave18_iv.py:33` | prop:punctured-disk-S1-qiso | Lurie HA 5.5.3.8 | AyalaFrancis2015 | -- | `assert True` | n/a | **AP287** (HZ-IV-W8-B flag present) |
| 6 | vol2 `test_climax_theorems_wave17_iv.py:39` | thm:homotopy-Koszul | Hoefel | Hoefel-Livernet | Fresse-Vallette | `is_homotopy_koszul(bool, bool) -> bool` returning `and` of inputs | `and` of two booleans; no computational content | **AP287** (HZ-IV-W8-B flag present; docstring claims "not a tautology" but body is) |
| 7 | vol2 `test_universal_holography_functor_fm_iv.py:42` | prop:uhf-fm125-koszul-triangle-projection | VolI ThmH | E3-chiral formal def | UHF chain-level | `_chirhoch_virasoro_structure(c_generic)` returns hard-coded dict | `{HH0:1, HH2:1}` hardcoded | **test-encoded-tautology** (Gel'fand-Fuchs and Feigin verify the hardcoded value; not executed) |
| 8 | vol2 `test_universal_holography_functor_fm_iv.py:84` | prop:uhf-fm126-global-triangle | UHF Dunn / CostelloGwilliam / DS-Hoch bridge | BZFN | Lurie HA 5.3.1.30 | `_global_triangle_chain_level_supplied(bool, bool)` returning `not(class_m and not bridge)` | structural predicate; all three paths verify the same boolean branch | **AP287** + **AP288** (boolean predicate encodes the claim) |
| 9 | vol1 `test_hz_iv_decorators_wave1.py:47` (miura cross-univ) | thm:miura-cross-universality | Miura inversion | Psi=1 free-boson limit | Psi->inf classical | `primary_cross_coefficient(s)` + two boundary `Psi=1,2` evals | the boundary evaluations re-call the same engine; the "two" verification paths are same-engine at different parameter values | **AP310** (Psi=1 and Psi=2 are same-engine evaluations, not disjoint) |
| 10 | vol1 `test_hz_iv_decorators_wave1.py:94` | prop:chirhoch1-affine-km | Koszul res + chirhoch engine | Whitehead current-algebra | Bourbaki Lie IV-VI | hardcoded Bourbaki dims `{sl2:3, sl3:8, G2:14}` checked against `chirhoch_affine_km` | dims hardcoded, engine re-derived; Whitehead source cited but not called | **AP277** on Whitehead path (bibliographic only); P2+P3 distinct |
| 11 | vol1 `test_hz_iv_decorators_wave1.py:139` | prop:depth-gap-trichotomy | shadow-tower alpha/Delta | classify_glcm engine | Kac 1990 character tables | 4 witness dicts hardcoded (alpha,Delta) + `classify_glcm` re-verifies | Kac citations are bibliographic; no call | **AP288** (P1+P2 are same engine's input/output; P3 bibliographic) |
| 12 | vol1 `test_hz_iv_decorators_wave1.py:206` | prop:sc-formal-iff-class-g | shadow-tower trunc | classify_glcm | FF free-field + OS | re-uses `classify_glcm` on witness dict | P1+P2 collapse to same engine | **AP288** |
| 13 | vol1 `test_hz_iv_decorators_wave1.py:263` | prop:ker-av-schur-weyl | `ker_av_dim` engine | Schur-Weyl Fulton-Harris | Young-tableaux hook-content | engine vs `d**n - comb(n+d-1, d-1)` | P2 (Schur-Weyl) IS the closed form; this is genuinely two disjoint computations | **CLEAN** (engine code-path vs `math.comb`) |
| 14 | vol1 `test_hz_iv_decorators_wave1.py:316` | prop:verlinde-from-ordered | ordered chiral hom S-matrix | Moore-Seiberg Z_0=1 | Gepner-Witten Z_1=k+1 / Beauville-Laszlo | `verify_genus0_unitarity(k)` + `verify_genus1_count(k)` + `verlinde_dimension_exact(g,k)` | three engine functions inside same `verlinde_ordered_engine` module | **AP310** (same engine module; boundary predicates could share intermediate) |
| 15 | vol1 `test_mc3_five_family.py:51` | thm:mc3-eval-core-5-family | 5-family synthesis | KR dim recursion + Molev sdet + FM algorithm + EV elliptic + GM super | GTL 2017 overlap | `witnesses` dict + `assert len(set(values)) == 5` | no external engine; bookkeeping only | **AP277** (verifies distinctness of strings, not mathematics) |
| 16 | vol1 `test_mc3_five_family.py:155` | prop:mc3-BCD-reflection-shap | LK coideal + MR twisted Y | Sklyanin 1988 boundary QISM | Molev 2007 sym-antisym RTT | `sdet_central = True; assert sdet_central` | hardcoded boolean | **AP277** (literal `True` assignment) |
| 17 | vol2 `test_super_chiral_yangian.py:87` | thm:super-yangian-e1-chiral | EK super-quantisation | Nazarov 1991 RTT | Gow-Molev 2010 PBW | `super_permutation_eigenvalue(p_i,p_j)` + `eig*eig == 1` | the assertion `(-1)^{2pipj} == 1` is TAUTOLOGICAL (parity ints squared) | **AP287** (mathematical tautology `x^2 >= 0`) |
| 18 | vol2 `test_super_chiral_yangian.py:135` | thm:super-yangian-e1-chiral (second decorator, same claim) | ordered bar T^c | Manin-Penkov-Skryabin Thm 3.2 | -- | `assert (sig_k + sig_l) % 2 == (sig_l + sig_k) % 2` | test explicitly tautological (`a+b == b+a`) — noted in test's OWN docstring | **AP287** (self-admitted tautology) |
| 19 | vol2 `test_wn_tempered_closure.py:90` | prop:beta-N-closed-form | FL structure + Riccati | N=2/3 direct | triangular-number identity | `beta_N_candidate_A/B(N)` + hardcoded `BETA_2=6, BETA_3=10` | HZ-IV test documents the candidate is RETRACTED (FP-all theorem gives 13 at N=4, not 15 or 16); keeps decorator despite decoration referencing a falsified form | **AP256/AP310** (decorator stale; "closed form" healed at `beta_N_closed_form_all_platonic.tex` to `12(H_N-1)`; decorator not updated) |
| 20 | vol3 `test_cy_d_kappa_stratification.py:136` | thm:kappa-hodge-supertrace-ident | HKR D^b(Coh) + shadow tower + Caldararu | Yau 1977 Calabi | Huybrechts K3 + GHJ | `hodge_supertrace_column(k3_hodge())` returns hardcoded Hodge diamond | the Hodge diamonds are hardcoded from Huybrechts / GHJ; supertrace is sum with `(-1)^q` | **AP310** (Yau/Huybrechts/GHJ all produce the SAME hardcoded Hodge diamond input; verification is `sum((-1)^q * h_{0,q})` evaluated once) |

## 3. Violation-class breakdown (n = 20)

| verdict | count | ratio |
|---|---|---|
| CLEAN | 1 | 5% |
| AP277 (vacuous body / bookkeeping) | 4 | 20% |
| AP287 (structural primitive tautology) | 6 | 30% |
| AP288 (label-disjoint-body-identical) | 3 | 15% |
| AP310 (shared intermediate step) | 5 | 25% |
| TEST-ENCODED-TAUTOLOGY | 2 | 10% |
| Stale decorator (AP256 / AP310) | 1 | 5% |

Reading: 1/20 CLEAN. 19/20 exhibit AP277/AP287/AP288/AP310 or a hybrid.
The Wave-10 HZ-IV-W8-B flag is already PRESENT on 3 of the AP287 sample
members (Vol II climax waves) -- these are correctly self-noted as not
counting toward HZ-IV coverage. The remaining violations are NOT flagged
and need either heal or HZ-IV-W8-B annotation.

## 4. Heal recommendations

Per-sample recommendations (no edits applied):

- **# 1 (ThmH):** wire `chirhoch_dimension_engine` for path 1, but for
  paths 2 and 3 invoke GENUINELY DIFFERENT engines -- e.g. for Feigin-
  Fuchs, compute Virasoro BRST via `compute/lib/feigin_fuchs_brst.py`
  (needs creation) returning (1,0,1) from Fock-complex resolution; for
  Wang 1998 affine sl_2, compute via Whitehead-Kunneth in a disjoint
  module. Only then are the three paths numerically disjoint.
- **# 2 (DS intertwining):** inscribe Miura-cross separate engine; the
  current `verify_psi2_intertwining` is the single source, three paths
  must factor through distinct implementations.
- **# 3 (CY-C six routes):** replace hardcoded `RHO_PENTAGON` with THREE
  independent computations (torus-localisation vs Chow-motive vs
  Mayer-Vietoris), each returning the triple independently.
- **# 4-8, 17-18 (AP287 / HZ-IV-W8-B):** either
  (a) add the `HZ-IV-W8-B FLAG` comment to the files that lack it, OR
  (b) downgrade the corresponding `\ClaimStatusProvedHere` tags to
  `\ClaimStatusConditional` in the manuscript. Do not carry uncaveated
  coverage.
- **# 9 (miura cross):** treat `Psi=1` and `Psi=2` evaluations as ONE
  engine path (symbolic boundary check); add a TRULY disjoint source
  (e.g. Feigin-Frenkel free-field realization coefficient computed from
  an independent screening-operator engine).
- **# 11-12, 14, 20 (AP288/AP310):** for each decorator, ensure at least
  two of the three paths live in DIFFERENT Python modules and do not
  ingest the same input data; `classify_glcm` cannot be both derivation
  and verification.
- **# 15-16:** promote from structural-string-distinctness to actual
  numerical thick-generation check via Nakajima/Hernandez engines; or
  flag HZ-IV-W8-B.
- **# 19 (beta_N):** update decorator to cite `beta_N_closed_form` and
  drop `candidate_A/B` references; the closed form is now
  `12(H_N - 1)`, not `(N+1)(N+2)/2`.

## 5. Residual open

- **Programme-wide AP288/AP310 sweep beyond 20 samples**: the sample
  ratio (19/20 with violations) strongly suggests the Vol I/II/III
  HZ-IV coverage numbers (Vol I 0/2275, Vol II 0/1134, Vol III 2/283
  per CLAUDE.md) understate the problem by failing to distinguish
  CLEAN from AP287/AP310. The sole CLEAN exemplar (ker_av_schur_weyl)
  is the template -- two genuinely disjoint computations, no shared
  engine, no shared hardcoded data.
- **Infrastructure recommendation**: extend
  `compute/lib/independent_verification.py::assert_sources_disjoint`
  to AST-walk the test body and reject any decorator where the three
  (`derived_from`, `verified_against` path 1, path 2) claims reduce to
  a single engine function-call AST. Current assertion checks label
  strings only; this is the AP288 surface layer, not the body-identity
  check.
- **Decorator stale-drift (AP256) audit**: case # 19 shows a decorator
  surviving a theorem retraction. Programme-wide sweep for decorators
  whose `derived_from` or `verified_against` cites a retracted form.
- **Vol III `test_hyperkahler_anchored_fixed_point.py` (159 grep hits)**:
  unsampled; high priority for dedicated audit given concentration.
- **Three remaining HZ-IV-W8-B unflagged wave files**: Vol II
  `wave{4,5,6}_iv.py` per grep were not individually verified for the
  flag comment in this audit; needs same-session sweep.

## Summary

Enumeration: Vol I 806 / Vol II 948 / Vol III 675 grep hits across 199
files (~400-500 decorators). Sample 20: 1 CLEAN, 6 AP287, 5 AP310, 4
AP277, 3 AP288, 2 test-encoded-tautology, 1 stale (AP256). Ratio
CLEAN:violation = 1:19. The HZ-IV discipline is broadly non-disjoint at
the test-body layer despite sound bibliographic labels. Heal: wire
genuinely disjoint engines per path, extend `assert_sources_disjoint`
to AST-check body identity, complete HZ-IV-W8-B annotation sweep on
unflagged wave files, audit decorators against retracted theorem forms.

No edits applied. No commits. All work attributed to Raeez Lorgat.
