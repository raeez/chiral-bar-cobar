# Attack-and-heal: Drinfeld-Sokolov reduction BRST cohomology + DS coproduct intertwining (Vol I)

**Target.** CLAUDE.md theorem-status row "DS intertwining: VERIFIED at degree >= 2 (non-trivial); degree 1 tautological | (pi_3 x pi_3) o Delta_z^{sl_3} = Delta_z^{W_3} o pi_3 verified 57 tests. Spectral coassociativity uses shifted parameters. Engine docstring `compute/lib/ds_coproduct_intertwining_engine.py:103-104` records degree-1 as tautological (pi_3 acts as identity on the W_3 generators at leading order); the content is the degree->=2 sl_3 RTT computation (AP256/AP257 discipline)."

**Mission.** Audit (i) theorem inscription locus, (ii) AP143 DS ghost charge full-vs-naive arithmetic at N=3, (iii) 57-test multi-k coverage, (iv) cross-consistency of the degree-1 tautological / degree->=2 non-tautological framing across Vol I + tests.

**Verdict.** No heal needed. The programme state is CONSISTENT with the CLAUDE.md status row; four previously-known healings (AP143 retraction of N(N-1) naive formula; AP256/AP257 engine-docstring correction; Wave-9 AP288 gold-standard disjoint paths; AP149 propagation to `rem:ds-intertwining-w3`) are all in effect. One minor docstring phrasing drift flagged as LOW-severity advisory.

---

## 1. Theorem inscription

Primary inscribed locus: Vol I `chapters/theory/ordered_associative_chiral_kd.tex:12249-12275`, `rem:ds-intertwining-w3` (`\begin{remark}` environment -- NOT a theorem; no `\ClaimStatus` tag needed per AP40). The remark inscribes:

1. Pi_3 reduction map V_k(sl_3) -> W_3.
2. Intertwining diagram (pi_3 x pi_3) o Delta_z^{sl_3} = Delta_z^{W_3} o pi_3.
3. Degree-1 Cartan sector: tautological -- 57 compute tests verify self-consistent specialisation.
4. Degree-≥2 non-tautological content -- equivalent to sl_3 RTT commutator cross-verification on gl_3 81 RTT components (rem:gl3-explicit, 53 compute tests at Psi in {1, 0.5, 2}).
5. Spin-3 gravitational HPL_3 sector as sharpest non-tautological witness.
6. Spectral coassociativity with shifted parameters.

The presentation is a remark (not a theorem) because the primary mathematical content is the sl_3 RTT commutator identity (a separate theorem, cross-referenced) and the Miura cross-universality (separate theorem thm:miura-cross-universality); the DS intertwining is a consistency-check summary, not an independent theorem claim. Status-tag discipline honest.

## 2. AP143 ghost-charge arithmetic: FULL Fateev-Lukyanov, NAIVE N(N-1) retracted

First-principles computation at N=3:

| k  | c_Sug(sl_3) | c_W3(k) (F-L) | c_ghost = c_Sug - c_W3 | naive N(N-1)=6 |
|----|-------------|---------------|------------------------|----------------|
|  0 |  0          | -30           | 30                     | 6              |
|  1 |  2          | -52           | 54                     | 6              |
|  2 | 16/5        | -374/5        | 78                     | 6              |
|  5 |  5          | -145          | 150                    | 6              |
| 10 | 80/13       | -3430/13      | 270                    | 6              |

The naive N(N-1)=6 is level-independent and wildly wrong at every integer k. The FULL F-L formula c_ghost = c_Sug(sl_N) - c_W_N(k) produces strongly level-dependent values. The `compute/lib/ds_coproduct_intertwining_engine.py::central_charge_consistency` function (lines 1160-1203) implements the full F-L subtraction correctly; the test `test_central_charge_consistency` at `compute/tests/test_ds_coproduct_intertwining_engine.py:178-183` asserts c_ghost_k0 = 30 and c_ghost_k1 = 54.

Manuscript audit: grep for `N(N-1)|N\*(N-1)` across `chapters/theory/*.tex` + `standalone/*.tex` returns ONE hit at `chapters/theory/computational_methods.tex:628` as a LaTeX comment: `% OLD WRONG: claimed kappa_ghost = N(N-1)/2, k-independent.` This is AP143 historical retraction marker, not an active claim. No active manuscript-layer AP143 violation detected.

AP143 discipline: UPHELD.

## 3. 57-test multi-k coverage audit

Total pytest collection on `compute/tests/test_ds_coproduct_intertwining_engine.py` returns 57 tests (matches CLAUDE.md row).

Multi-k coverage:
- `TestSpecificLevels::test_intertwining_at_level` parametrized at `k_val in [0, 1, 2, 5, 10]` (5 distinct levels via `@pytest.mark.parametrize`).
- `TestSpecificLevels::test_k0_data` -- explicit k=0 checks on Psi, c_W3, kappa_sl3, kappa_W3.
- `TestSpecificLevels::test_k1_data` -- explicit k=1 checks.
- `TestSpecificLevels::test_negative_level` -- explicit k=-1 (Psi=2) check.
- `TestCriticalLevel` -- three tests at k=-3 (critical level k = -h^vee boundary).
- `TestGoldStandardDisjointPathsDSIntertwining::path_C_per_level_numerical` -- five-level numerical uniformity check at k in {0,1,2,5,10}.

Multi-k coverage: at least 6 distinct integer levels (k in {-3, -1, 0, 1, 2, 5, 10}) plus symbolic-k checks. Levels are not restricted to k=1 in isolation.

Caveat (low severity): the intertwining identity at degree 2 is formally level-independent (Drinfeld binomials do not involve Psi). The multi-level checks verify the surrounding data (Psi substitution, central charges, kappa values) across levels, not a level-dependent intertwining content. This is consistent with the mathematical content and the `path_C_per_level_numerical` explicit uniformity assertion.

57-test discipline: UPHELD.

## 4. AP256/AP257 engine-docstring / manuscript consistency

The CLAUDE.md row cites engine docstring at `compute/lib/ds_coproduct_intertwining_engine.py:103-104`. Verbatim:

```
AT DEGREE 1, the intertwining is a TAUTOLOGY for the Cartan sector
(both sides use the same Drinfeld formula) but a NONTRIVIAL CONSISTENCY
CHECK for:
  (a) The Miura-inverted W_3 coproduct Delta_z(T_{W_3}) ...
  (b) The spectral parameter structure (z-dependence) ...
  (c) The level identification Psi = k + h^vee = k + 3.
  (d) The Sugawara construction: T_{W_3} = T_{Sug}^{sl_3} + ghost correction.
```

The test `test_psi1_intertwines_tautological` at `test_ds_coproduct_intertwining_engine.py:234-256` inscribes the degree-1 tautological status as a Wave-7 HZ-IV FLAG: primitive-by-construction on both sides, AP287 structural-impossibility, UNDECORATED (no `@independent_verification`). The decorated HZ-IV at `test_ds_coproduct_intertwining_degree_ge_2_hz_iv` (line 605) explicitly binds to degree 2.

Manuscript remark `rem:ds-intertwining-w3` inscribes the identical split: "At degree 1 the intertwining is _tautological_ on the Cartan sector ... At degree >= 2 the intertwining is non-tautological". Three documents agree (engine docstring / test docstring / manuscript remark).

AP256/AP257 discipline: UPHELD.

### 4.1 Minor phrasing advisory (LOW severity, no heal required)

Engine docstring line 103-111 reads "degree 1 is a TAUTOLOGY for the Cartan sector (both sides use the same Drinfeld formula) but a NONTRIVIAL CONSISTENCY CHECK for (a) Miura-inverted W_3 coproduct Delta_z(T_{W_3}) ..." This conflates two scopes:

- The _Cartan-eigenvalue_ intertwining at degree 1 is tautological (both sides defined primitive by fiat).
- The _spin-2 Miura_ consistency at degree 1 (item (a)) is a nontrivial check AT DEGREE 1 -- but it is _not_ the CLAUDE.md row's "degree >= 2 sl_3 RTT computation". Items (a)-(d) in the engine docstring enumerate WITHIN-DEGREE-1 nontrivial consistency conditions; the CLAUDE.md row's "degree >= 2 content" refers to the RTT commutator matching at sl_3 arity 2 (rem:gl3-explicit).

These are two different senses of "nontrivial at degree 1" vs "nontrivial at degree >= 2". The docstring phrasing is technically correct but the contrast "tautology ... but ... consistency check" at lines 103-105 could be read as self-contradictory by a naive reader. The manuscript remark rem:ds-intertwining-w3 at line 12249-12275 draws the cleaner distinction (degree 1 Cartan tautological; degree >= 2 RTT cross-verification; spin-3 HPL_3 as sharpest non-tautological witness). Rectification optional; preferred form in future passes would be docstring lines 103-111 rewritten to mirror the manuscript remark's three-tier structure (degree-1 Cartan / degree-1 Miura consistency / degree->=2 RTT).

No AP registration required; this is within-wave drift from the Wave-9 AP288 gold-standard propagation, not a new failure mode.

## 5. Summary table

| Check                                             | Status     |
|---------------------------------------------------|------------|
| Theorem inscription present                       | Yes (rem:ds-intertwining-w3, ordered_associative_chiral_kd.tex:12249) |
| AP143 ghost charge full F-L (not N(N-1)=6)        | Yes (engine central_charge_consistency + test_central_charge_consistency)  |
| 57 tests (CLAUDE.md claim)                        | Yes (pytest --collect-only reports 57)                                     |
| Multi-k coverage (not just k=1)                   | Yes (k in {-3, -1, 0, 1, 2, 5, 10} + symbolic)                             |
| AP256/AP257 engine docstring matches manuscript   | Yes (three documents agree on degree-1 tautological / degree->=2 RTT)      |
| AP288 HZ-IV disjoint paths implemented            | Yes (Wave-9 gold-standard at test_ds_coproduct_intertwining_engine.py:658) |
| Manuscript hygiene (no AP143 N(N-1) active)       | Yes (historical retraction marker only at computational_methods.tex:628)   |

## 6. No new APs registered

Per AP314 (inscription-rate discipline) + AP306 (block under-utilisation), this audit inscribes ZERO new APs. All observed patterns are covered by AP143, AP256, AP257, AP287, AP288. The Minor phrasing advisory in Section 4.1 does not meet the threshold of a new failure mode.

## 7. No commits

Per the PRE-COMMIT hook discipline reiterated during this audit: no `git commit` issued. All findings recorded here as a mission report; manuscript and engine state unchanged.

-- Raeez Lorgat, 2026-04-18
