# Wave-17 AP316 Re-Execution Audit: H3 Two-Subscript Rename in Vol III

**Date**: 2026-04-18
**Mission**: Verify the Wave-12 H3 rename (κ_ch → κ_ch^{Heis}) is actually
landed on main HEAD of `~/calabi-yau-quantum-groups`, or re-execute if not.
**Trigger**: Wave-16 AP320 re-sweep reported zero hits on main for the ~30
renames claimed by Wave-12 agent `a1b6e600` across 6 Vol III chapter files,
suggesting worktree-isolated work abandoned at delivery (AP316 class).

## Verdict

**NO RE-EXECUTION REQUIRED.** The Wave-12 H3 rename IS fully landed on main
HEAD. The Wave-16 audit "zero hits" finding was a query-mismatch artefact,
not evidence of AP316 worktree isolation. All ~30 Route-B sites across the
six target files already carry `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}`.

Git log on main shows the landing commit set: Wave-20 (`4af2b3e`) "CY-D κ
stratification + K3 chiral/quantum toroidal/BKM chapters + modular trace +
preface/intro + derived categories CY + quantum group reps + CY-to-chiral +
quantum chiral algebras refinements" — date-ordered before Wave-16. Most
likely the rename was swept into one of Waves 18/20/21/22 propagation
commits under the broader CY-D / Part-VII heading rather than under an
isolated "Wave-12 H3 rename" commit. Consistent with the Wave-13 residual
sweep (`aa885c0d`) recorded in the mission brief as REAL.

## Per-site evidence (grep on main HEAD)

### 1. `chapters/frame/preface.tex` — 5 κ_ch^{Heis} occurrences present

```
489: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E)
490:  = \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) + \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1 = 3$
493: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ (constant across pentagon)
1046: \emph{K3-1}: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3 = \dim_\C$
1050: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) = 2$, $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 1$
```

Wave-11 patch file listed 3 sites at L489-490, L1046, L1050. All renamed. ✓

### 2. `chapters/theory/introduction.tex` — 8 κ_ch^{Heis} occurrences present

```
319-322: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ remains nonzero by additivity
         ($\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 1$,
          $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$)
707-708: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3 = \dim_\C$
         $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) + \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1$
1041: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$
1186: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3 = \dim_\C$
1190: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) = 2$, $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 1$
```

Wave-11 patch listed 5 sites. All renamed. ✓

### 3. `chapters/examples/k3e_cy3_programme.tex` — 9 κ_ch^{Heis} occurrences

```
333-334: Additivity clause — all three κ_ch with Heis superscript
983:  $\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3 = \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) + \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1$
1824: $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) + \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 2 + 3 = 5$
1825, 1827: κ_ch^{Heis}(K3) = 2, κ_ch^{Heis}(K3×E) = 3
1856: Same pattern
2607: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 2 + 2 = 4$
3052: K3×E additivity chain
```

Wave-11 patch listed 7 sites. All renamed. ✓

### 4. `chapters/examples/k3e_bkm_chapter.tex` — 12 κ_ch^{Heis} occurrences

```
9, 11, 540, 980, 1137, 1139-1140, 1241-1242, 1250, 1255, 1352
```

L980 preserves bare κ_ch(K3) = 2 with "(fiber)" annotation as mixed-route
Route-A keep-bare per Wave-11 patch directive. Wave-11 patch listed 6 sites;
actual landing improved coverage to include opening paragraphs L9, L11 and
other in-prose mentions. ✓

### 5. `chapters/examples/k3_chiral_algebra.tex` — 12 κ_ch^{Heis} occurrences

```
241: Table row "Additivity: 2 + 1"
447, 449, 452: $\chi_{\mathrm{top}}/24$ failure discussion
503-504, 506, 512: Numbered item list contrasting Route A / Route B
539-541: $\chi_{\mathrm{top}}/24 \neq$ κ_ch^{Heis} for E, K3, K3×E
744: κ_ch^{Heis}(E) = 1 rephrased "by rank-additivity on all
     Heisenberg-level presentations" per patch directive.
```

Wave-11 patch listed 8 sites. All renamed. ✓

### 6. `chapters/examples/quantum_group_reps.tex` — 1 κ_ch^{Heis} occurrence

```
932: BARE $\kappa_{\mathrm{ch}}(K3 \times E) = \chi^{\mathrm{Hodge}}(K3) \cdot
     \chi^{\mathrm{Hodge}}(E) = 2 \cdot 0 = 0$  [KEEP BARE — Route A Hodge]
1115: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$ (Heisenberg-level
      chiral algebra invariant)  [Route B rename applied]
```

Wave-11 patch prescribed exactly this discipline (1 rename + 1 keep-bare).
Both sites conform. ✓

## Cumulative grep gate (PROOF of landing)

```bash
grep -rn '\\kappa_{\\mathrm{ch}}(K3 \\times E) = 3' <6-target-files>
```

**Result: ZERO hits.** The bare Route-B pattern `κ_ch(K3 × E) = 3` is
absent from all six target files.

```bash
grep -rn '\\kappa_{\\mathrm{ch}}(E) = 1' <6-target-files>
```

**Result: ZERO hits.** The bare Route-B pattern `κ_ch(E) = 1` is absent.

```bash
grep -c '\\kappa_{\\mathrm{ch}}\^{\\mathrm{Heis}}' <6-target-files>
```

**Result (per file)**:
- preface.tex: 5
- introduction.tex: 8
- k3e_cy3_programme.tex: 9
- k3e_bkm_chapter.tex: 12
- k3_chiral_algebra.tex: 12
- quantum_group_reps.tex: 1
- **Total: 47** (exceeds Wave-11 patch's ~30 count because prose-embedded
  mentions in L9/L11/L540 of k3e_bkm were also rename-swept).

## Why the Wave-16 audit reported "zero hits"

Speculation, not verified: the Wave-16 query likely used a regex mismatch
(possibly searching for a pattern with single-backslash, missing LaTeX
double-backslash escaping) or limited the search path to a worktree that
was never merged. The substantive landings are on main HEAD via the
post-Wave-12 propagation commits (Waves 18/20/21/22). The Wave-12 agent
`a1b6e600` apparently DID merge its work to main but under a different
headline commit than a dedicated "H3 rename" commit.

## Recommendation

1. **No further rename edits required** on the 6 target files.
2. **Wave-16 AP316 flag retracted** for the H3 rename — false alarm.
3. **Residual audit action**: re-check the additional files listed in
   Wave-11 patch §"Route-B site inventory" beyond the 6 targets
   (`k3_yangian_chapter.tex`, `k3_quantum_toroidal_chapter.tex`,
   `quantum_chiral_algebras.tex`, `modular_koszul_bridge.tex`,
   `modular_trace.tex`, `cy_to_chiral.tex`, `main.tex`,
   `cy_c_six_routes_convergence.tex`) for any stragglers using the same
   grep gate. Out of scope for this re-execution mission.
4. **Commit plan**: NO commits from this audit session. This note is a
   verification artefact only.

## Discipline tags

- HZ-7 (Vol III κ-subscript mandatory): satisfied; `^{\mathrm{Heis}}`
  superscript is an approved HZ-7 extension per CLAUDE.md Wave-11
  landings.
- AP5 (cross-volume propagation): intra-Vol-III propagation complete for
  the 6 target files; cross-volume Vol I / Vol II consumer scan
  unrelated.
- AP149 (resolution propagation failure): does NOT fire — Wave-12 heal
  did land, contrary to Wave-16 flag.
- AP234 (two-Koszul-conductors-same-letter): unrelated.
- AP289 (Künneth-multiplicative vs additive): the rename enforces the
  correct discipline — Route A (Hodge supertrace) stays bare and is
  multiplicative; Route B (Heisenberg-level) carries `^{\mathrm{Heis}}`
  and is additive.
- AP-CY69 (H3 annotation): satisfied per Wave-11 prep.
- AP316 (worktree-isolated heal): **false positive retracted** for this
  particular flag.
- AP320 (re-sweep): closed for H3 rename on the 6 target files.
- PE-5 (Vol III kappa write template): no new κ edits performed, N/A.
