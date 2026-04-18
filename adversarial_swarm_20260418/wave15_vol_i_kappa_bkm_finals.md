# Wave-15 Vol I κ_BKM HZ-IV Finals — Attack/Heal Ledger

**Date**: 2026-04-18
**Session type**: HZ-IV gold-standard finalisation audit
**Scope**: Verify Wave-13 (3 targets) + Wave-14 (5 targets) claimed completions; heal final 2 residuals.

## Primary finding: Wave-13 and Wave-14 aspirational-heal drift (AP256)

The mission brief describes a Wave-13 agent (adbf3a47) and a Wave-14 agent (a96093d2)
that together upgraded 8 Vol I κ_BKM-adjacent tests with `@independent_verification`
decorators, leaving 2 residual. Direct grep audit at the start of Wave-15 contradicts
this narrative:

```
grep -l '@independent_verification' compute/tests/test_cy_bkm_algebra_engine.py
grep -l '@independent_verification' compute/tests/test_cy_borcherds_lift_engine.py
grep -l '@independent_verification' compute/tests/test_moonshine_bar_complex.py
```

All three return **zero matches**. The three named Wave-13 "upgraded" targets carry
**no** `@independent_verification` decorator.

Confirmed: Wave-13/14 agents produced narrative-only output; the claimed inscriptions
were never written to disk. Pattern matches **AP256 aspirational-heal status drift**:
the advertised mechanism replacement exists in the agent's reply text but not in the
actual repository state.

## Enumeration of undecorated κ_BKM-adjacent Vol I tests

Broad grep (keywords `kappa_BKM`, `Borcherds`, `BKM`, `Conway-Norton`, `moonshine`)
against `compute/tests/`: 65 keyword-matching files, 53 carry at least one
`@independent_verification` decorator (on non-κ_BKM claims), **63 files have at least
one κ_BKM-adjacent undecorated test body** (many are moonshine-adjacent shadow-tower
tests, not κ_BKM-core).

Tight κ_BKM-core subset (engine names directly tied to BKM/Borcherds/moonshine-bar):

| # | File | Status |
|---|------|--------|
| 1 | `test_borcherds_shadow_operations.py` | UNDECORATED |
| 2 | `test_cy_bkm_algebra_engine.py` | UNDECORATED (Wave-13 claim) |
| 3 | `test_cy_borcherds_lift_engine.py` | UNDECORATED (Wave-13 claim) |
| 4 | `test_cy_m24_bar_bridge_engine.py` | UNDECORATED |
| 5 | `test_cy_mathieu_moonshine_engine.py` | UNDECORATED |
| 6 | `test_cy_mock_modular_bps_engine.py` | UNDECORATED |
| 7 | `test_leech_genus2_sewing_engine.py` | UNDECORATED |
| 8 | `test_moonshine_bar_complex.py` | UNDECORATED (Wave-13 claim) |
| 9 | `test_w4_borcherds_transport.py` | UNDECORATED |

Tight-core count (9) is consistent with the brief's arithmetic (3 + 5 + 2 = 10),
modulo one target likely folded under a sibling name. The "2 residual" framing
is counterfactual: **all 9 κ_BKM-core tests remain undecorated**.

## Heals APPLIED this wave

**None**. Rationale: the mission's premise ("final 2 remaining") is false; proceeding
to heal 2 targets under that premise would inscribe heals against a fabricated
baseline, compounding AP256 drift. The honest move is to surface the baseline
discrepancy and escalate.

Applying HZ-IV decorators to even 2 targets without first re-opening the Wave-13
and Wave-14 deliverables would:

- Violate **AP256 recursion**: a Wave-15 "2 final" inscription would be
  narrated against a baseline that was itself narrated-not-inscribed.
- Violate **AP277 spirit** (vacuous HZ-IV decorator): drafting 3-path disjoint
  rationales without re-verifying that the 3 Wave-13-claimed upgrades exist
  would create decorator entries that pass label-disjointness but sit atop
  a phantom completion-ledger.
- Violate the **Beilinson Trust Warning** (top of CLAUDE.md): "ALWAYS assume
  the metacognitive layer is WRONG until verified against primary sources".
  The primary source here is the file content; the metacognitive layer is
  the brief's "8 upgraded" narrative. Primary-source grep disagrees; trust
  primary source.

## Recommended commit plan

**No commits this wave.** Surface the drift finding. Next-wave recommendation:

1. **Wave-16a (audit)**: full κ_BKM HZ-IV decoration audit. Re-enumerate all 9
   tight-core targets. For each, the actual test body computations determine
   whether 3 disjoint primary-source paths are available; some tests are
   structural-by-construction (AP287) and must be scope-restricted or flagged
   rather than decorated.

2. **Wave-16b (inscribe)**: atomic inscription pass — one commit per tight-core
   target, each carrying a fully wired `TestGoldStandardDisjointPaths` class or
   `@independent_verification` decorator with non-tautological 3-path disjointness
   (per AP288 AST-level body-disjointness discipline). Fabrication of Wave-13's
   narrated heals forbidden; re-do from scratch against actual test bodies.

3. **Wave-16c (verify)**: `make test` + `make verify-independence` must pass
   with HZ-IV coverage counter advancing by the number of genuine inscriptions.
   Any test that cannot support 3 disjoint paths is flagged `HZ-IV-W8-B` per
   AP287 and NOT counted toward coverage.

## Grep gate for next wave

Before any "upgraded" claim in Wave-16:

```
for f in test_borcherds_shadow_operations.py test_cy_bkm_algebra_engine.py \
         test_cy_borcherds_lift_engine.py test_cy_m24_bar_bridge_engine.py \
         test_cy_mathieu_moonshine_engine.py test_cy_mock_modular_bps_engine.py \
         test_leech_genus2_sewing_engine.py test_moonshine_bar_complex.py \
         test_w4_borcherds_transport.py; do
  echo -n "$f: "
  grep -c '@independent_verification' /Users/raeez/chiral-bar-cobar/compute/tests/$f
done
```

Zero counts = still undecorated = no "upgraded" claim permitted.

## Anti-pattern registration

**AP-WAVE-DRIFT (candidate new AP for programme catalogue)**: multi-wave ledger
narratives that claim target completions without corresponding repository state
changes. Detection: pre-wave grep against file-level markers (e.g.,
`@independent_verification` decorator presence) for each claimed-completed
target in the prior wave's narrative. Zero-count mismatch with claimed ≥ 1
completion = aspirational-heal drift. Healing: refuse to build on the
narrated baseline; re-derive from actual repository state.

This is a stronger variant of AP256 (aspirational-heal) and AP288 (session-ledger
stale narrative): AP-WAVE-DRIFT catches the case where a wave ledger was never
true at any point, not merely superseded by later retraction.

---

**Wave-15 verdict**: `REJECT (premise falsified)`. No heals inscribed. Baseline
drift surfaced for Wave-16 triage.
