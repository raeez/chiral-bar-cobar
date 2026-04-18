# Wave-14 Vol II V1-ref HZ-11 / AP287 Statistical Sweep
Date: 2026-04-18. Author: Raeez Lorgat.

## Scope and methodology

Statistical (stratified) sample of Vol II `\ref{V1-*}` consumer sites
against HZ-11 + AP287 discipline. Wave-13 (af89ec23) completed the
corresponding Vol I sweep at zero violations; the Vol II population is
larger and concentrated in `chapters/connections/thqg_*`.

Population enumeration (grep):

- `\ref{V1-*}` Vol II (.tex only): **464 sites across 40 files**
  (the earlier "1133" figure conflated `\ref` + `\label` + bare string
  occurrences of the `V1-` prefix; the genuine `\ref`-consumer count is
  464).

Stratified sample: 30 sites across the 13 highest-frequency files
(thqg_symplectic_polarization 67, thqg_critical_string_dichotomy 52,
twisted_holography_quantum_gravity 37, thqg_holographic_reconstruction
36, thqg_gravitational_yangian 34, thqg_fredholm_partition_functions
34, thqg_gravitational_complexity 24, thqg_gravitational_s_duality 22,
thqg_perturbative_finiteness 22, thqg_soft_graviton_theorems 16,
thqg_modular_bootstrap 14, bv_brst 13, dnp_identification_master 13).

## 30-site stratified classification

Type A = ProvedHere proof body silently citing V1 result → AP287
violation. Type B = chapter / section motivation with "Vol~I" prose
prefix (clean). Type C = ProvedElsewhere or Conditional with explicit
attribution (clean). Type D = definition / scope / convention recall
(clean).

| # | File | Line | Type |
|---|------|------|------|
| 1 | thqg_symplectic_polarization | 32 | B |
| 2 | thqg_symplectic_polarization | 100 | **A** |
| 3 | thqg_symplectic_polarization | 102 | **A** |
| 4 | thqg_symplectic_polarization | 138 | **A** |
| 5 | thqg_symplectic_polarization | 163 | **A** |
| 6 | thqg_symplectic_polarization | 175 | **A** |
| 7 | thqg_symplectic_polarization | 189 | **A** |
| 8 | thqg_critical_string_dichotomy | 14 | B |
| 9 | thqg_critical_string_dichotomy | 26 | D |
| 10 | thqg_critical_string_dichotomy | 59 | D |
| 11 | twisted_holography_quantum_gravity | 276 | C |
| 12 | twisted_holography_quantum_gravity | 357 | C |
| 13 | twisted_holography_quantum_gravity | 420 | C |
| 14 | twisted_holography_quantum_gravity | 511 | B |
| 15 | thqg_gravitational_yangian | 277 | D |
| 16 | thqg_gravitational_yangian | 526 | D |
| 17 | thqg_gravitational_yangian | 543 | C (borderline) |
| 18 | thqg_gravitational_yangian | 585 | C (borderline) |
| 19 | bv_brst | 794 | C (MODEL: `remark[Attribution]`) |
| 20 | bv_brst | 824 | C |
| 21 | bv_brst | 1197 | C |
| 22 | bv_brst | 2344 | C |
| 23 | bv_brst | 2364 | C (MODEL: `remark[Attribution and scope]`) |
| 24 | dnp_identification_master | 30 | C |
| 25 | dnp_identification_master | 180 | C (MODEL: `[Scope restriction inherited from Vol~I]`) |
| 26 | thqg_holographic_reconstruction | 61 | D |
| 27 | thqg_holographic_reconstruction | 304 | C (borderline) |
| 28 | thqg_fredholm_partition_functions | 53 | D |
| 29 | thqg_modular_bootstrap | 152 | C (borderline) |
| 30 | thqg_perturbative_finiteness | 463 | C (MODEL: `ProvedElsewhere{Theorem~\ref{V1-...}}`) |

Tally:

- Type A (hard AP287 violation): 6 sites (20%)
- Type B (motivation, clean): 4 (13%)
- Type C explicit attribution (clean): 10 (33%)
- Type C borderline (proof-body ref, short prose, no explicit remark): 4 (13%)
- Type D definition-recall (clean): 6 (20%)

Hard violation rate: **20%**. Borderline-inclusive rate: **33%**.

Structural observation: all six Type-A violations in the sample are
concentrated within a single proposition
(`prop:thqg-III-ambient-properties`) in `thqg_symplectic_polarization`.
The Top-10 heal below resolves all six by one compound edit.

## Projection to 464-site population

Naive: 20% × 464 = **~93 projected Type-A violations** programme-wide.
This overstates because the violating sample is clustered in one
proposition. Cluster-corrected: 3-6 propositions × 4-7 V1-refs each,
plus a long tail of borderline proof-body refs (~155 sites)
missing explicit `[Attribution]` remarks but otherwise scoped.

Models to propagate (Vol II internal): `bv_brst.tex`,
`dnp_identification_master.tex`, `thqg_perturbative_finiteness.tex` —
these files already carry the correct HZ-11 patterns (explicit
Attribution remarks; "Volume~I" prose prefixes; ProvedElsewhere with
in-tag V1-ref).

## Top-10 heal applied (Wave-14, this session)

Single compound heal on
`chapters/connections/thqg_symplectic_polarization.tex:121-153,192`:

1. `\ClaimStatusProvedHere` → `\ClaimStatusConditional` on
   `prop:thqg-III-ambient-properties` (captures the Koszul-locus +
   perfectness external dependency).
2. Appended `\begin{remark}[Attribution: Vol~I dependencies for
   Proposition~\ref{prop:thqg-III-ambient-properties}]` enumerating
   all five Vol I inputs (`V1-lem:perfectness-criterion`,
   `V1-lem:quantum-ss-convergence`,
   `V1-sublem:center-isomorphism`,
   `V1-cor:duality-bar-complexes-complete`,
   `V1-thm:geometric-equals-operadic-bar`) with scope inheritance
   note (Koszul locus, finite-dim fiber cohomology) and HZ-11 + AP287
   citation.
3. Label `rem:thqg-III-ambient-properties-attribution` added.

This single heal resolves sites 2-7 (the six Type-A violations).
Nine additional "Top-10" candidate heals are deferred as LOW-priority
borderline sites (Type C without explicit attribution remark);
enumeration preserved for Wave-15 continuation:

- `thqg_gravitational_yangian.tex:543,585`
- `thqg_holographic_reconstruction.tex:304`
- `thqg_modular_bootstrap.tex:152`
- `thqg_fredholm_partition_functions.tex` proof-body refs (sample-2)
- `thqg_soft_graviton_theorems.tex` proof-body refs (sample-2)
- `thqg_gravitational_complexity.tex` proof-body refs (sample-2)

## Residual long-tail plan

Full sweep of the 464-site population is roughly 5-6x the sample
cost. Prioritised approach:

1. **Wave-15 (immediate)**: exhaustive Type-A hunt in the top-13
   files — enumerate every `\ref{V1-*}` inside a `\ClaimStatusProvedHere`
   proof body. Expected yield: ~10-20 additional heals, each following
   the `prop:thqg-III-ambient-properties` template.
2. **Wave-16**: long-tail 27 files (1-12 V1-refs each). Likely
   yield: 5-10 additional heals plus ~50 borderline sites requiring
   prose-prefix ("Volume~I, Theorem~\ref{...}") or attribution-remark
   augmentation.
3. **Wave-17+**: tune `compute/audit/ap287_sweep.py` (not yet
   written; see Wave-13 af89ec23 for Vol I rubric) to auto-flag
   ProvedHere theorem/prop blocks whose proof bodies contain
   `\ref{V1-*}` or `\ref{V3-*}` without sibling `\ClaimStatusConditional`
   tag or `\begin{remark}[Attribution]` within 10 lines of `\end{proof}`.

## Commit plan

One commit for the single Wave-14 heal:

```
Vol II Wave-14 AP287/HZ-11 heal: thqg_symplectic_polarization
prop:thqg-III-ambient-properties downgraded ProvedHere -> Conditional
with Attribution remark enumerating five Vol I dependencies; sample
sweep note inscribed under adversarial_swarm_20260418/
```

No build or test run required for this edit (prose-level downgrade
+ attribution remark; zero mathematical content changed). Author:
Raeez Lorgat.

## Sample-external flags (noted, not healed)

The PostToolUse hook surfaced pre-existing AP24/AP8 cluster
violations in `thqg_symplectic_polarization.tex` at lines 1916/1940
("$\kappa + \kappa^! = 0$" without family qualifier — Virasoro is 13,
not 0) and 2017/2041 ("Vir$_{13}$ (self-dual)" should be qualified
c=13). These are distinct from HZ-11/AP287 scope; recorded here for
a separate Wave-15 heal pass (template: append family qualifier or
route through `landscape_census.tex` complementarity table).
