# Wave 10 HZ-IV-W8-B Primitive-Tautology Programme-Wide Scan (2026-04-17)

## Mandate

Surface every independent-verification decorator whose three declared
"disjoint verification paths" collapse to a structural boolean predicate
(`_pred(bool, ...) -> bool`) or `assert True`, and therefore verifies
nothing at the numerical level. This is the W8-B failure mode: "degree-1
primitive tautology" generalised to the symptom "both sides are
definitionally true, so disjoint verification is STRUCTURALLY IMPOSSIBLE".

Wave-8 #51 and Wave-9 #61 flagged the symptom. Wave-9 #61 explicitly
noted the Vol II `test_climax_theorems_wave*_iv.py` family as the
deferred target. This scan closes that deferral.

## Per-volume scan statistics

### Vol I (`~/chiral-bar-cobar`)

- IV decorator files scanned: 55.
- `_pred(bool) -> bool` hits: 0.
- `assert True` hits: 0.
- Explicit "structural/boolean" self-description: 0 files.
- **W8-B FLAG COUNT: 0.** Vol I decorators (e.g. `test_hz_iv_decorators_wave1.py`,
  `test_ds_koszul_intertwine_iv.py`, `test_ftm_seven_fold_tfae.py`) invoke
  actual engine outputs (`primary_cross_coefficient`, `ker_av_dim`,
  `chirhoch_affine_km`, `verlinde_dimension_exact`) and compare against
  multi-path numerical witnesses. These are genuine decorations.

### Vol II (`~/chiral-bar-cobar-vol2`)

- IV decorator files scanned: 59.
- `_pred(bool) -> bool` definitions: **57** across **13** files
  (all under `test_climax_theorems_wave{3,4,5,6,7,8,9,10,11,12,13,14}_iv.py`
  plus `test_universal_holography_functor_fm_iv.py`).
- `assert True` hits: **37** across **5** files
  (waves 15, 16, 17, 18 and `test_climax_theorems_iv.py`).
- Combined scope: **17 files** exhibit the W8-B primitive-tautology
  pattern either as boolean-predicate oracles or as degenerate
  `assert True` sealing-wax tests.
- **W8-B FLAG COUNT: 17 files, approximately 94 claims.**

Representative instance (wave 3, `test_e3_topological_ds`):

```python
def _w_algebra_E3_topological(non_critical: bool, principal_nilpotent: bool) -> bool:
    return non_critical and principal_nilpotent

@independent_verification(claim="thm:E3-topological-DS", ...)
def test_e3_topological_ds():
    assert _w_algebra_E3_topological(True, True)
```

The predicate returns `True` by construction on the hypothesis
arguments. The decorator records Arakawa 2015 and Witten 1989 as
"verified against", but the test itself verifies nothing beyond
`True and True == True`. This is textbook W8-B: the claim the
decorator advertises as verified has not been cross-checked by any
numerical computation; the external sources are bibliographic
scaffolding, not active cross-verification.

The `assert True` form (waves 15-18 + master `test_climax_theorems_iv`)
is even starker: the test body is `assert True`; the decorator payload
is metadata only.

### Vol III (`~/calabi-yau-quantum-groups`)

- IV decorator files scanned: 82.
- `_pred(bool) -> bool` hits: 0.
- `assert True` hits: 0.
- **W8-B FLAG COUNT: 0.** Vol III adherence to the HZ-IV discipline
  is the installation standard (coverage 2/283 reported in
  `notes/INDEPENDENT_VERIFICATION.md`).

## Per-instance verdict (Vol II)

Three-healings menu from Wave 9:

1. **Scope-restrict** (rename test to admit tautology, move decorator
   to non-primitive sector).
2. **Downgrade** (Conjectured or Partial).
3. **Honest omission with flag** (annotate at module level; defer real
   IV to a follow-up campaign).

**Applied verdict for all 17 Vol II files: (3) honest omission with
flag.**

Rationale: the claims are genuine programme theorems with existing
`.tex` proofs; the decorators themselves are correctly authored at
the *bibliographic* level (external sources ARE genuinely disjoint).
The gap is that the Python-level predicate does not perform a
numerical cross-check. Downgrading to `Conjectured` would be a
category error (the theorems are proved in prose); scope-restricting
would require re-authoring each test against an engine output that
does not yet exist. The correct intermediate action is to **flag the
pattern in-module** so future HZ-IV campaigns can replace each
tautological predicate with a numerical engine call.

Per-instance table (Vol II, 17 files, ~94 claims): **all flagged with
in-module `# HZ-IV-W8-B` marker comment citing this scan.** Test
bodies unchanged; no commit planned this wave.

### File-by-file flag inventory

| File | Pattern | Claims | Verdict |
|------|---------|--------|---------|
| `test_climax_theorems_iv.py` | `assert True` (2) + bookkeeping | 7 | Flag |
| `test_climax_theorems_wave3_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave4_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave5_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave6_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave7_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave8_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave9_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave10_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave11_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave12_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave13_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave14_iv.py` | `_pred(bool) -> bool` | 7 | Flag |
| `test_climax_theorems_wave15_iv.py` | `assert True` | 7 | Flag |
| `test_climax_theorems_wave16_iv.py` | `assert True` | ~3 | Flag |
| `test_climax_theorems_wave17_iv.py` | `assert True` | ~20 | Flag |
| `test_climax_theorems_wave18_iv.py` | `assert True` | ~20 | Flag |
| `test_universal_holography_functor_fm_iv.py` | `_pred(bool) -> bool` | 7 | Flag |

## Follow-up queue (future wave)

For each flagged file, the genuine heal is one of:

- identify a numerical observable (dimension count, structure constant,
  central charge, Chern character) whose value is NOT predetermined
  by the hypothesis booleans;
- import an existing compute engine from `compute/lib/` that produces
  the observable;
- replace the boolean predicate with an `assert engine_output ==
  expected_value` call, anchored to at least one `verified_against`
  citation that independently predicts the same value.

Where no such observable exists (e.g. `thm:master` is a purely
structural master-equation statement admitting no numerical content),
the honest downgrade is to route the claim through a
`\ClaimStatusProvedElsewhere` tag with a Remark attributing the
external source, and remove the decorator from the test suite.

## Scan completeness

All 196 decorator files across three volumes scanned via
`rg '^def _[a-z_]+\([a-z_]+:\s*bool.*\)\s*->\s*bool:'` and
`rg 'assert\s+True\s*$'`. The 19 Vol I `assert True` hits are in
compute engines (`test_gap_closure.py` etc.) used as reachability
probes, NOT inside `@independent_verification` decorators; spot-checked
and confirmed out of scope.

No further false negatives expected: the W8-B signature is narrow
(boolean tautology inside a decorated test), and the ripgrep patterns
cover both canonical forms. Any future W8-B entry will be caught by
`scripts/audit_independent_verification.py` once that audit is
extended to classify tautological predicates (a concrete follow-up
item).

## Coverage impact

Pre-scan Vol II coverage: 0/1134 per HZ-IV Protocol installation
snapshot (CLAUDE.md HZ-IV). The 94 flagged Vol II claims should NOT
count toward genuine HZ-IV coverage and should be removed from any
coverage-upgrade announcement until healed.
