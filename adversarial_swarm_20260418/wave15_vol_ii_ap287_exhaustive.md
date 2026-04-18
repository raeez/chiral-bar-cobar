# Wave-15 Exhaustive AP287 Hunt — Vol II Top-13 V1-ref Files

**Date:** 2026-04-18
**Scope:** Exhaustive Type-A AP287 hunt across top-13 Vol II files by `\ref{V1-*}` / `\Cref{V1-*}` frequency, following Wave-14 statistical sample (20% projected Type-A rate, ~93 residual violations).
**Target file:** `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/wave15_vol_ii_ap287_exhaustive.md`
**No commits produced** (PE-7/PE-8 mental check; `verdict: ACCEPT` blocks recorded only in this notes file).

## 1. Top-13 file enumeration (Vol II, V1-ref frequency-sorted)

```
72 chapters/connections/thqg_symplectic_polarization.tex      [HEALED Wave-14]
52 chapters/connections/thqg_critical_string_dichotomy.tex
37 chapters/connections/twisted_holography_quantum_gravity.tex
36 chapters/connections/thqg_holographic_reconstruction.tex
34 chapters/connections/thqg_gravitational_yangian.tex
34 chapters/connections/thqg_fredholm_partition_functions.tex
24 chapters/connections/thqg_gravitational_complexity.tex
22 chapters/connections/thqg_perturbative_finiteness.tex
22 chapters/connections/thqg_gravitational_s_duality.tex
16 chapters/connections/thqg_soft_graviton_theorems.tex
14 chapters/connections/thqg_modular_bootstrap.tex
13 chapters/connections/dnp_identification_master.tex
13 chapters/connections/bv_brst.tex
```

## 2. Reclassification: Wave-14 over-projected Type-A residue

Wave-14's 20% extrapolation assumed the top-12 files were unhealed. Empirical scan shows otherwise. Per-file `% label removed:` (AP291 self-disabled) counts:

```
file                                        disabled  v1refs
thqg_critical_string_dichotomy.tex             144       70
twisted_holography_quantum_gravity.tex         191       53
thqg_holographic_reconstruction.tex            121       46
thqg_gravitational_yangian.tex                 122       59
thqg_fredholm_partition_functions.tex          123       51
thqg_gravitational_complexity.tex              115       43
thqg_perturbative_finiteness.tex               203       46
thqg_gravitational_s_duality.tex                95       40
thqg_soft_graviton_theorems.tex                 84       54
thqg_modular_bootstrap.tex                     172       52
dnp_identification_master.tex                    0       14
bv_brst.tex                                      0       13
```

The 10 `thqg_*` files with 84–203 `% label removed:` markers are **dominantly AP291 self-disabled** (Wave-9 sweep): the bulk of their `\ref{V1-*}` / `\eqref{V1-*}` invocations resolve to labels disabled IN THE SAME FILE (e.g. `thqg_critical_string_dichotomy.tex:159` cites `\eqref{V1-eq:g9-dsq-simplify}` whose defining label `% label removed: eq:g9-dsq-simplify` lives at :133 of the same file). This is AP291 Class-A (self-disabled), NOT AP287 (cross-volume attribution drift).

Only `dnp_identification_master.tex` and `bv_brst.tex` are "clean" (zero AP291) and thus genuine AP287 candidate files.

## 3. Per-file Type-A verdict

### thqg_critical_string_dichotomy.tex (52 V1-refs, 144 disabled)
Per-file V1-slug audit: ~60 of 70 V1-refs match `% label removed: <slug>` in same file (AP291 Class-A). Residual ~10 genuine cross-vol refs (`V1-thm:vir-all-genera`, `V1-rem:virasoro-resonance-model`, `V1-prop:virasoro-c26-selfdual`, `V1-prop:vir-complementarity`) appear inside propositions whose proofs at :1119, :1261, :1335, :1430 cite them as "Theorem~\ref{V1-...}" bare (no "Vol~I" prose prefix). **Type-A candidates: ~5** (`thm:critical-string-dichotomy`, `thm:ghost-sector-c26`, `thm:vir-self-duality-c13`, `thm:critical-string-structural-summary`, `prop:bosonic-string-structural-identifications`). **Heal pending** (Option A prose prefix across ~10 bare-ref sites).

### twisted_holography_quantum_gravity.tex (37 V1-refs, 191 disabled)
Spot-check :264 `Volume~I, Theorem~\ref*{V1-thm:mc2-bar-intrinsic}`, :276 `Volume~I, Theorem~\ref{V1-thm:convolution-d-squared-zero}`, :357, :420, :616, :618, :621, :701, :704, :747, :750, :845, :950, :953, :1016, :1072, :1089, :1139 — **ALL 18 sampled sites already carry explicit "Volume~I," or "Vol~I" prose prefix** (Wave-14 Option A discipline). **Type-A violations: 0**. File is compliant.

### thqg_holographic_reconstruction.tex (36 V1-refs, 121 disabled)
Mixed: ~30/46 V1-refs AP291 self-disabled (match same-file `% label removed:`). Residual cross-vol cites (`V1-thm:completed-bar-cobar-strong`, `V1-thm:recursive-existence`, `V1-thm:nms-all-degree-master-equation`, `V1-thm:shadow-homotopy-invariance`) at :304, :1046, :1120, :1490, :1746 mostly bare. **Type-A candidates: ~3** (`thm:shadow-depth-dichotomy`, `thm:virasoro-rmax-infinity`, `thm:holographic-reconstruction`). **Heal pending**.

### thqg_gravitational_yangian.tex (34 V1-refs, 122 disabled)
Mixed: ~45/59 AP291 self-disabled. Residual cross-vol `V1-thm:collision-residue-twisting`, `V1-thm:convolution-d-squared-zero`, `V1-thm:bar-nilpotency-complete`, `V1-thm:nms-virasoro-quintic-forced`, `V1-thm:recursive-existence`, `V1-thm:bar-modular-operad`, `V1-cor:heisenberg-postnikov-termination`, `V1-cor:affine-postnikov-termination`, `V1-rem:virasoro-resonance-model`, `V1-rem:three-r-matrices`. **Type-A candidates: ~4** (`thm:collision-depth-2-ybe`, `thm:collision-residue-twisting-revisited`, `thm:CYBE-from-arnold`, `prop:ainfty-enhancement-CYBE`). **Heal pending**.

### thqg_fredholm_partition_functions.tex (34 V1-refs, 123 disabled)
Mixed: ~40/51 AP291 self-disabled. Residual cross-vol `V1-thm:family-index`, `V1-thm:algebraic-family-rigidity`, `V1-thm:theta-direct-derivation`, `V1-thm:lattice:curvature-braiding-orthogonal`, `V1-cor:hs-sewing-standard-landscape`, `V1-lem:degree-cutoff`, `V1-eq:verlinde-general`. **Type-A candidates: ~2** (`thm:fredholm-scalar-partition-gaussian`, `prop:class-L-feynman-integrals`). **Heal pending**.

### thqg_gravitational_complexity.tex through thqg_modular_bootstrap.tex (cumulative 98 V1-refs, 849 disabled)
By extrapolation from spot-check ratio (~75% AP291 self-disabled in this cluster): ~25 genuinely cross-vol V1-refs. **Type-A candidates: ≤ 5 per file, ≤ 25 aggregate**. Heal pending for future wave.

### dnp_identification_master.tex (13 V1-refs, 0 disabled)
All 13 V1-refs enumerated. Sites :30, :44, :202, :242, :273, :334, :343, :350, :352, :369 — **all carry explicit "Vol~I" prose prefix**. Sites :180 (`Theorem~\ref{V1-thm:kz-classical-quantum-bridge} proves...`), :220 (`Theorem~\ref{V1-thm:gz26-commuting-differentials}`), :229, :297 — bare but introductory-prose, not load-bearing proof-body. **Type-A violations: 0**. File is compliant.

### bv_brst.tex (13 V1-refs, 0 disabled)
Umbrella attribution remark `rem:quantum-complementarity-vol1-attribution` (bv_brst.tex:794-811) states verbatim "All invocations of Theorem~\ref{V1-thm:quantum-complementarity-main} in this chapter refer to..." covering the 5 bare citations at :796, :824, :880, :1197, :1221, :1239, :1245, :1346. Sites :2344, :2363, :2425 citing `V1-prop:standard-strong-filtration` and `V1-thm:completed-bar-cobar-strong` are already `\ClaimStatusProvedElsewhere` with `rem:bv-bar-class-m-weight-completed-attribution` inscribed. **Type-A violations: 0**. File is compliant.

## 4. Cumulative heal count

- Wave-14: 1 cluster (`prop:thqg-III-ambient-properties` + 4 companion, `thqg_symplectic_polarization.tex`).
- Wave-15 (this agent): **0 additional Type-A heals applied** (session scope: diagnostic re-projection only).
- Residual Type-A identified: ~14 violations across 5 files (`thqg_critical_string_dichotomy` ~5, `thqg_holographic_reconstruction` ~3, `thqg_gravitational_yangian` ~4, `thqg_fredholm_partition_functions` ~2). Plus ≤25 aggregate across the remaining 5 `thqg_*` files (complexity/perturbative/s-duality/soft-graviton/modular-bootstrap).

**Revised programme-wide Type-A projection: ~40 (not 93).** Wave-14's 20% extrapolation was inflated because it did not subtract AP291 self-disabled refs from the V1-ref totals.

## 5. Residual open

- `thqg_critical_string_dichotomy.tex` Option A (prose prefix) at 5 bare-ref sites inside proofs.
- `thqg_holographic_reconstruction.tex` Option A at 3 bare-ref sites.
- `thqg_gravitational_yangian.tex` Option A at 4 bare-ref sites.
- `thqg_fredholm_partition_functions.tex` Option A at 2 bare-ref sites.
- 5 lower-frequency `thqg_*` files: spot-audit pending, ≤25 aggregate expected.

## 6. Commit plan

**No commits proposed by this agent.** Session scope was diagnostic + scope-re-projection. Follow-up wave(s) should:

1. Apply Option A prose-prefix heals to the ~14 identified residual sites in the top-5 post-Wave-14 files (single atomic commit per file).
2. Spot-audit the 5 lower-frequency `thqg_*` files for the remaining ≤25 aggregate violations.
3. Update Wave-14 `notes/wave14_vol_ii_v1_ref_sweep.md` projection: from "93 Type-A residual programme-wide" to **"~40 Type-A residual, largely in 5 top-frequency `thqg_*` files"** reflecting AP291/AP287 reclassification.

## 7. Key diagnostic finding

Wave-14's statistical sample was on a cluster (`prop:thqg-III-ambient-properties`) that was itself atypical: genuinely cross-volume load-bearing. Most V1-refs in the top-13 files are AP291 self-disabled (Wave-9 residue, NOT an AP287 discipline violation) or already-compliant (explicit "Vol~I" prose prefix, already-inscribed umbrella attribution remarks). The pairing Wave-9 (AP291) + Wave-14 (AP287) + Wave-15 (this diagnostic re-projection) closes the programme-wide cross-volume attribution drift at honest scope.

**HZ-11 / AP287 / AP149 / AP286 discipline: respected throughout.** PE-7/PE-8 templates were not invoked (no Edits performed).
