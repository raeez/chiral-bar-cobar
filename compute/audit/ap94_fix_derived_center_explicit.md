# AP94 Fix: derived_center_explicit.py

Scope: compute layer only. Manuscript side handled by parallel agents.

## Summary

The file `compute/lib/derived_center_explicit.py` carried an AP94/AP95
violation: it modelled `ChirHoch*(Vir_c)` as the unbounded polynomial
ring `C[Theta]` with `|Theta|=2`, and `ChirHoch*(W_3)` as the bigraded
polynomial ring `C[Theta_1, Theta_2]`. Both models give infinite total
dimension and contradict Theorem H
(`thm:hochschild-polynomial-growth`), which forces cohomological
amplitude `[0,2]` with `dim ChirHoch^2(A) = dim Z(A^!)`. At generic
central charge, `Z(Vir_c) = Z(W_3) = 1`, so Theorem H pins the
Hochschild profile to `(1,1,1)` for both families.

The violation was partly docstring-level, partly logic-level, and
partly test-level. The test layer was synchronised against the
wrong engine values (AP128 pattern), so the tests "verified" outputs
that directly contradicted Theorem H.

## Decision rationale: Option A (replace)

Option A (replace with Theorem-H-consistent bounded model) was chosen
over:

- Option B (flag as a different object). Rejected because the function
  is named `chiral_hkr_dimension`, the docstring explicitly invokes
  the chiral HKR prediction, and the master package
  `full_derived_center_package` already uses the bounded model
  `{0:1, 1:1, 2:1}` for Virasoro and W3. A flag-only fix would leave
  two different conventions inside the same module.
- Option C (delete). Rejected because `chiral_hkr_dimension` is
  imported and tested and its Heisenberg/affine branches are correct.
  Deletion would lose load-bearing coverage.

Option A is the only fix that (a) agrees with Theorem H, (b) agrees
with the module's own `full_derived_center_package`, and (c) preserves
the function's signature for the existing test file.

## Before/after diff summary

### `compute/lib/derived_center_explicit.py`

1. `HochschildCocycleEnumerator` class docstring (line ~164):
   replaced "polynomial-ring structure for the W-algebra regime"
   with explicit statement that Theorem H concentration in `{0,1,2}`
   applies uniformly across the standard landscape.

2. `virasoro_hh2_weight_graded` docstring (lines ~293-330):
   removed the literal assertion `ChirHoch*(Vir_c) = C[Theta]`, the
   `Gelfand-Fuchs` attribution, the "polynomial ring model" language,
   and the false prose claim `dim ChirHoch^n = 1 if n even, else 0`.
   Replaced with Theorem H's bounded profile and a prohibitive note
   naming AP94/AP95. Logic unchanged (the implementation already
   returned `{0:1, 1:0, ..., max_weight:0}`, which is consistent with
   Theorem H once interpreted as dim HH^2 at each weight; only the
   docstring misrepresented what it was computing).

3. `chiral_hkr_dimension` docstring and logic (lines ~1110-1170):
   completely rewrote the docstring (the old one rambled through
   three contradictory "resolutions" and landed on C[Theta]); changed
   the Virasoro branch from `1 if degree % 2 == 0 else 0` to the
   Theorem-H profile `(1,1,1)`; changed the W3 branch from a partition
   count over generator weights `{2,3}` to the Theorem-H profile
   `(1,1,1)`; added an early return `0` for `degree < 0 or degree > 2`
   that applies uniformly. Heisenberg and affine sl_2 branches
   unchanged (they were already Theorem-H-consistent).

4. Affine sl_2 branch refactored so the `degree == 1` case returns
   `3` (dim(sl_2)) and all other in-range cases return `1`, matching
   the existing `affine_sl2_hh_dimensions` helper.

### `compute/tests/test_derived_center_explicit.py`

1. `test_virasoro_hkr_polynomial_ring` renamed to
   `test_virasoro_hkr_theorem_h_bounded`. Assertions changed:
   - `HH^1 == 0` -> `HH^1 == 1` (Theorem H gives 1, not 0)
   - `HH^4 == 1` -> `HH^4 == 0` (Theorem H vanishes beyond degree 2)
   - Added explicit vanishing checks at degrees 3, 5, 6.
   The test docstring now cites Theorem H and names the AP94 anti-
   pattern that was previously being verified.

2. `test_w3_hkr_polynomial_ring` renamed to
   `test_w3_hkr_theorem_h_bounded`. Assertions changed:
   - `HH^1 == 0` -> `HH^1 == 1`
   - `HH^3 == 1` -> `HH^3 == 0`
   - `HH^4 == 1` -> `HH^4 == 0`
   - `HH^5 == 1` -> `HH^5 == 0`
   - `HH^6 == 2` -> `HH^6 == 0`
   The old assertions were the clearest smoking gun of the AP128
   pattern: the engine returned partition counts from the generating
   function `1/((1-t^2)(1-t^3))` and the test hard-coded the same
   values.

## Importing modules

Grep for `derived_center_explicit` in `compute/`:

| file | imports | status |
|------|---------|--------|
| `compute/lib/rectification_kappa_cross_engine.py` | `kappa` only | UNAFFECTED |
| `compute/tests/test_derived_center_explicit.py` | many (infected) | UPDATED |
| `compute/tests/test_rectification_kappa_cross_engine.py` | `kappa` only | UNAFFECTED |

Only the direct test file was affected by the fix. No cross-engine
test used the infected `chiral_hkr_dimension` or
`virasoro_hh2_weight_graded` outputs.

## Newly-discovered contradictions

### CRITICAL FINDING 1: AP128 test-engine synchronization

The Virasoro and W3 branches of `chiral_hkr_dimension` returned values
directly contradicting Theorem H, and `test_virasoro_hkr_polynomial_ring`
and `test_w3_hkr_polynomial_ring` asserted exactly those wrong values.
The test suite was therefore "passing" while verifying output that
contradicts a Proved-Here theorem in the same manuscript. This is the
textbook AP128 pattern.

### CRITICAL FINDING 2: Module-internal contradiction

Within the same file, `full_derived_center_package` at line 1302 used
`hh = {0:1, 1:1, 2:1}` for Virasoro (consistent with Theorem H) while
`chiral_hkr_dimension` returned `1 if degree even else 0` for Virasoro
(contradicting Theorem H). Two sibling functions in the same module
disagreed on the shape of `ChirHoch*(Vir_c)`. The `full_derived_center_package`
path happened to be the one cited in the Euler-characteristic test
(`test_euler_characteristic_values`), which is why that test passed
with `chi = 1` while `test_virasoro_hkr_polynomial_ring` passed with
an unbounded model.

### CRITICAL FINDING 3: Sibling-module infection (OUT OF SCOPE)

The same `C[Theta]` / Gelfand-Fuchs violation appears in TWO other
compute modules that are OUT OF SCOPE for this agent:

- `compute/lib/theorem_h_hochschild_polynomial.py` lines 144, 832,
  966, 969. This is the module nominally responsible for Theorem H;
  it currently encodes the wrong model of Theorem H in its own
  docstrings. This is the most dangerous occurrence: the engine
  named after Theorem H contradicts Theorem H.
- `compute/lib/theorem_thm_h_e3_rectification_engine.py` line 290.
- `compute/tests/test_theorem_h_hochschild_polynomial.py` lines
  344, 463, 469, 822. Infected test expectations.

A parallel agent should be dispatched to those files. Without that
dispatch, `theorem_h_hochschild_polynomial.py` remains the load-
bearing false "verification" of Theorem H.

### FINDING 4: Manuscript-side audit trail

The audit notes in `compute/audit/exhaustive_gap_analysis_2026_04_08.md`
(line 112 ff.) and `compute/audit/complete_frontier_status_2026_04_08.md`
(line 290 ff.) already flagged the C[Theta] pattern as an AP94 violation
and noted that the continuous cohomology `H^*_cont(L_1) = C[Theta]`
statement is a fact about the Witt Lie algebra, NOT about chiral
Hochschild cohomology. These audit notes were correct; the compute
layer simply had not been updated to match them.

## Recommended manuscript-side follow-up

1. Verify that `chiral_hochschild_koszul.tex` never claims Vir has
   HH classes beyond degree 2. The statement at lines 649-736 of
   `chiral_hochschild_koszul.tex` is correct (amplitude [0,2], Hilbert
   polynomial of degree at most 2). No manuscript-side change needed
   in this chapter.

2. Audit any other chapter that mentions `C[Theta]` or "Gelfand-Fuchs"
   in the context of chiral Hochschild. The correct usage is that
   `H^*_cont(Witt) = C[Theta]` (Gelfand-Fuchs) is a DIFFERENT functor
   from `ChirHoch*`; any passage that conflates them is AP95.

3. Dispatch a parallel agent to `theorem_h_hochschild_polynomial.py`
   and its test file. These encode the wrong Theorem H.

4. Consider whether CLAUDE.md's AP94 should be strengthened from
   "dim <= 4" to an explicit amplitude statement "`ChirHoch^n = 0`
   for `n > 2`". The current wording allows future agents to
   misread "dim <= 4" as a bound on some other grading while still
   permitting unbounded polynomial towers.

## Residual inconsistencies (flagged, not fixed)

- `theorem_h_hochschild_polynomial.py` and its test file remain
  infected. Out of scope for this agent.
- The docstring of `virasoro_hh2_weight_graded` claimed to compute
  the weight-graded dimension of HH^2, but the implementation simply
  returns `{0:1, else:0}` without doing any actual bar-complex
  computation. The output is Theorem-H-consistent but trivially so;
  the function does not verify Theorem H, it merely asserts its
  conclusion. Any future test that claimed this function verifies
  Theorem H would be circular. The fix preserved the trivial
  implementation (because rewriting the bar-complex enumeration is
  out of scope) and the updated docstring no longer claims that the
  function verifies anything.
- `HochschildCocycleEnumerator` (lines ~155-220) is an independent
  enumeration class over cochain weights; its output is not currently
  tested against Theorem H's cohomological amplitude, so it cannot
  serve as a verification of Theorem H. This is a structural gap:
  the compute layer lacks a genuinely independent verification of
  the `n > 2` vanishing.
