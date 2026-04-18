# Wave-16 AP320 Re-verification — Wave-13 + Wave-14 HZ-IV κ_BKM claims

**Date:** 2026-04-18
**Prior agents:**
- Wave-13 (adbf3a47): claimed HZ-IV decoration of three κ_BKM targets
- Wave-14 (a96093d2): claimed HZ-IV decoration of five additional κ_BKM targets
- Wave-15 finals (a5cfa3f0): claimed AP320 fabrication by Wave-13/14 via grep for `@independent_verification` returning zero
- @_iv NameError fix agent (adbeada6): found that Wave-13 used alias `@_iv(...)` not long form; Wave-15 false positive

**Mission.** Run comprehensive grep across both decorator forms (long `@independent_verification`, alias `@_iv(`, suffixed `@_iv_v14_*(`, and class `TestGoldStandardDisjointPaths`) for all 10 named targets; definitively classify each.

## Verification table

| # | Target file | Wave claim | Long-form decorators | Alias `@_iv(` | Alias `@_iv_v14_*` | Import of `independent_verification` | Classification |
|---|---|---|---|---|---|---|---|
| 1 | `test_moonshine_kappa_resolution_engine.py` | W-13 | **1** @ line 923 | 0 | 0 | YES (line 920) | FULLY LANDED (long form) |
| 2 | `test_cy_bkm_algebra_engine.py` | W-13 | 0 | **1** @ line 989 | 0 | YES as `_iv` (line 986) | FULLY LANDED (alias form) |
| 3 | `test_cy_borcherds_lift_engine.py` | W-13 | 0 | **1** @ line 1337 | 0 | YES as `_iv` (line 32) | FULLY LANDED (alias form, import was subsequently fixed by agent adbeada6) |
| 4 | `test_moonshine_bar_complex.py` | W-14 | 0 | 0 | **1** @ line 1030 (`_iv_v14_mbc`) | YES as `_iv_v14_mbc` (line 1027) | FULLY LANDED (suffixed alias) |
| 5 | `test_leech_genus2_sewing_engine.py` | W-14 | 0 | 0 | **1** @ line 1065 (`_iv_v14_leech`) | YES as `_iv_v14_leech` (line 1062) | FULLY LANDED (suffixed alias) |
| 6 | `test_bc_niemeier_l_values_engine.py` | W-14 | 0 | 0 | **1** @ line 889 (`_iv_v14_nlv`) | YES as `_iv_v14_nlv` (line 886) | FULLY LANDED (suffixed alias) |
| 7 | `test_theorem_shadow_langlands_engine.py` | W-14 | 0 | 0 | **1** @ line 477 (`_iv_v14_sl`) | YES as `_iv_v14_sl` (line 474) | FULLY LANDED (suffixed alias) |
| 8 | `test_moonshine_higher_shadow_engine.py` | W-14 | 0 | 0 | **1** @ line 1290 (`_iv_v14_mhs`) | YES as `_iv_v14_mhs` (line 1287) | FULLY LANDED (suffixed alias) |
| 9 | `test_cy_siegel_shadow_engine.py` | W-13 residual (W-14 deferred) | 0 | 0 | 0 | NO | NOT LANDED (deferred, confirmed absent) |
| 10 | `test_rectification_kappa_cross_engine.py` | W-13 residual (W-14 deferred) | 0 | 0 | 0 | NO | NOT LANDED (deferred, confirmed absent) |

**`TestGoldStandardDisjointPaths` test class:** 0 matches across all 10 files. None of Wave-13/14 used that class pattern — decorators applied directly to functions, not wrapped in a class.

## Revised AP320 classification

**Wave-13 (3 targets).** All three FULLY LANDED:
- `test_moonshine_kappa_resolution_engine.py` — long form, 1 decorator.
- `test_cy_bkm_algebra_engine.py` — alias `_iv`, 1 decorator.
- `test_cy_borcherds_lift_engine.py` — alias `_iv`, 1 decorator. The NameError issue was an import at line 32 (top-of-file) — effectively present; agent adbeada6 verified/ensured the import matches the decorator site at line 1337.

**Wave-14 (5 targets).** All five FULLY LANDED with suffixed aliases (`_iv_v14_{mbc, leech, nlv, sl, mhs}`), one decorator each, import and decoration co-located correctly.

**Wave-13 residual 2 targets (W-14 deferred).** Both NOT LANDED on disk:
- `test_cy_siegel_shadow_engine.py` — zero `independent_verification` mentions.
- `test_rectification_kappa_cross_engine.py` — zero `independent_verification` mentions.
These are confirmed genuinely absent, consistent with Wave-14's explicit deferral note. This is NOT a fabrication by Wave-13 if Wave-13 merely listed them as intended-but-deferred; becomes AP320 only if Wave-13 claimed them as LANDED.

**Wave-15 finals AP320 narrative verdict.** OVERCLAIMED. Wave-15's grep used only `@independent_verification` (long form), missing 7 of 8 genuinely landed decorators (1 Wave-13 long + 2 Wave-13 alias + 5 Wave-14 suffixed-alias). The correct AP320 surface, if any, is limited to the two residual targets (#9, #10) — and only insofar as an earlier wave actually claimed them as landed.

## Session-level wave-integrity verdict

Wave-13 + Wave-14 landed 8/10 claimed targets with genuine HZ-IV decorators. The 8 landings use three alias schemes:
- Long form (1 file): `@independent_verification`
- Bare alias (2 files): `@_iv` (Wave-13 convention)
- Suffixed alias (5 files): `@_iv_v14_<tag>` (Wave-14 convention to avoid NameError under parallel imports)

Wave-15's AP320 fabrication claim is a DETECTION GAP, not a content gap: the grep pattern did not cover alias forms that the Wave-13/14 commit templates explicitly prefer.

**Meta-pattern catalog:** AP320 requires a multi-pattern detector. Propose AP320-detector-widening:

```
grep -cnE '@independent_verification|@_iv\(|@_iv_v[0-9]+_[a-zA-Z]+\(|TestGoldStandardDisjointPaths'
```

plus a separate grep against `compute/lib/independent_verification` import lines to anchor alias-definitions.

## Commit plan

**None.** Diagnostic only; no file edits. A subsequent wave can optionally:
(a) close the two residual targets (#9, #10) with genuine HZ-IV decoration (not fabrication); and
(b) extend the programme-level AP320 detector to cover alias forms per the widened grep above.
