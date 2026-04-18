# Wave-12 Vol I HZ-IV Gold-Standard Propagation (continued)

Date: 2026-04-18
Agent: continuation of Wave-10 `aee61065` broaden agent.

## Scope

Three Vol I HZ-IV tests upgraded to gold-standard disjoint-path decoration.
All upgrades are ADDITIVE (new test functions appended); no existing test was
renamed or deleted. No commits per mission constraints.

## Targets & before/after structure

### 1. `compute/tests/test_shadow_exponential_base.py` — `thm:universal-class-M-C-is-6`, `thm:shadow-series-closed-form-Virasoro`

**Before.** Docstring-level claims "Path 1 / Path 2 / Path 3" with ZERO
`@independent_verification` decorator. 15 existing tests all use the same
`leading_asymptotic(r)` engine call for the "three paths", violating
AP277/AP288 (label-disjointness without computational-disjointness).

**After.** Added two new `@independent_verification` functions:

- `test_gold_standard_C_A_equals_6_three_paths`:
  - Path A: Riccati closed-form ratio `|A_{r+1}/A_r| = 6r/(r+1)` at r=19
    via direct arithmetic on `8(-6)^{r-4}/r` (no engine call).
  - Path B: log-branch-point radius via `sp.solve(1+6z, z)` and
    Cauchy-Hadamard, disjoint from Riccati.
  - Path C: cross-family `s3_w3_tline`, `s3_bp_tline` both give `S_3 = 2`,
    yielding `C = r_0 * S_{r_0} = 6` independently of Virasoro.

- `test_gold_standard_log_branch_point_three_paths`:
  - Path A: direct Taylor match against `-(-1)^{r+1} 6^r/(162 r)`.
  - Path B: solve linear system `a b^4/4 = -a_4`, `a b^5/5 = a_5`, pinning
    `(a, b) = (-1/162, 6)` without assuming the closed form.
  - Path C: ratio-test singularity-type diagnosis (log vs pole vs essential)
    via ratio = `6 r/(r+1)` ≠ 6 rules out pole.

### 2. `compute/tests/test_shadow_tower_asymptotics.py` — `thm:leading-asymptote-virasoro`

**Before.** 15 tests all chain through `leading_coefficient(r)` engine call,
including tests claiming "the mechanism" (recursion) but actually just
evaluating the engine's closed form. Zero HZ-IV decorators.

**After.** Added `test_gold_standard_leading_asymptote_three_paths`:

- Path A: iterate Riccati recursion `S_r = -3(r-1)/r * S_{r-1}` from seed
  `S_4 = 1/2` step by step (no engine call).
- Path B: telescoping product with explicit verification of the identity
  `prod_{k=5}^r (k-1)/k = 4/r` by direct multiplication.
- Path C: generating-function coefficient extraction from `log(1+6z)`.

Engine call demoted to Path Z sanity anchor, not in `verified_against`.

### 3. `compute/tests/test_shadow_tower_recursive.py` — `thm:riccati-algebraicity` (S_4 anchor)

**Before.** 742 lines, zero `@independent_verification` decorators. Tests
route through the `shadow_tower_recursive` engine exclusively.

**After.** Added `TestGoldStandardDisjointPathsRiccati` class with
`test_S4_virasoro_three_disjoint_paths`:

- Path A: leading-c asymptote `c^2 S_4 -> 2` from the closed-form shadow
  generating function `Sigma_Vir`. (Self-consistency of the Riccati H^2 = Q_L
  equation is tautological at leading order — honest scope statement.)
- Path B: shadow discriminant `Delta = 40/(5c+22)` (inscribed at
  `higher_genus_modular_koszul.tex:16701` as Riccati-algebraicity primitive)
  combined with `Delta = 8 kappa S_4` pins the full closed form.
- Path C: Zamolodchikov 1985 BPZ null-state level-4 Kac matrix
  `(L_{-4}, L_{-2}^2)` mixing.

## Manual arithmetic verification

Each target verified by hand:

| Target | Path A at c=1 | Path B at c=1 | Path C at c=1 | Agree? |
|---|---|---|---|---|
| C_A=6 at r=19 | `\|A_{20}/A_{19}\| = 57/10` | `1/\|-1/6\| = 6` | `3·2 = 6` | ✓ |
| log-branch r=4 | `leading_asymptotic(4)=2` | `(a,b)=(-1/162,6)` ✓ | ratio 6·4/5=24/5 ≠ 6 (log) | ✓ |
| leading-asymp r=5 | `-6/5` (recursion) | `-6/5` (telescope) | `-6/5` (closed form) | ✓ |
| S_4 leading c | `lim c^2·10/[c(5c+22)] = 2` | `40/(5c+22)/(4c) = 10/[c(5c+22)]` | `10/[c(5c+22)]` | ✓ |
| S_4 at c=1 | N/A (leading only) | `10/27` | `10/27` | ✓ |
| S_4 at c=26 | N/A (leading only) | `10/3952` | `10/3952` | ✓ |

All three targets pass AST parse (`python3 -c "import ast; ast.parse(...)"`).
Runtime pytest execution deferred: sandbox lacks the compute venv's pytest
binary. Test bodies are syntactically valid and numerically verified by
hand arithmetic.

## HZ-IV discipline notes

- Engine calls (`leading_asymptotic`, `leading_coefficient`,
  `compute_shadow_tower`) demoted to Path Z sanity anchors ONLY; not in
  `verified_against` per Wave-10 adjudication.
- `assert_sources_disjoint` at import time guards against label-disjoint-but-
  computation-identical (AP288) — the disjointness rationale for each
  decorator names DISTINCT mathematical objects (log GF, discriminant
  invariant, Kac determinant; Riccati recursion, telescoping identity,
  log-series coefficient; ratio test, Cauchy-Hadamard, cross-family seed).
- AP277 heal: no `assert True` hardcodes; every path performs a concrete
  algebraic or numerical evaluation at test time.
- AP287 honest scoping: the Riccati S_4 test labels Path A as leading-c
  asymptote ONLY — full-value agreement requires Paths B and C because the
  Riccati self-consistency is tautological at leading order (honest
  admission; not a failure mode).

## Residuals

- Path A of the Riccati S_4 test could be strengthened to a genuinely
  independent FULL derivation if the Zhu/Kazhdan-Lusztig level-4 Kac
  determinant is computed from scratch (rather than cited as Path C).
  Engine for this: to be scaffolded as `compute/lib/kac_determinant_level4.py`.
- Cross-volume κ_BKM HZ-IV decorators (Wave-9/10 carryover) remain pending;
  out of scope for this continuation.
- Wave-10 self-flagged residual `test_riccati_recursion_engine.py` does NOT
  exist at that name; content lives in `test_shadow_tower_recursive.py`
  which is now upgraded.

## Commit plan

No commits per mission constraints. Recommended when user approves:

```
git add compute/tests/test_shadow_exponential_base.py \
        compute/tests/test_shadow_tower_asymptotics.py \
        compute/tests/test_shadow_tower_recursive.py \
        adversarial_swarm_20260418/wave12_vol_i_hz_iv_broaden_continued.md
git commit -m "Vol I HZ-IV gold-standard broaden: 3 Vol I tests upgraded (AP277/AP287/AP288)"
```

Pre-commit: run `compute/.venv/bin/python -m pytest <three files> -v` to
confirm all three new functions green.
