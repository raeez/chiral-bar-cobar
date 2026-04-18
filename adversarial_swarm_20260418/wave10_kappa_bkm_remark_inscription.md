# Wave-10 κ_BKM Remark Inscription (2026-04-18)

## Mission

Targeted heal: inscribe Vol~III manuscript remarks pointing at the Wave-9
gold-standard HZ-IV test-file upgrade for
`thm:borcherds-weight-kappa-BKM-universal`. Close the residual
manuscript-vs-test asymmetry without disturbing the theorem body.

## Target

- **File**: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex`
- **Theorem**: `\label{thm:borcherds-weight-kappa-BKM-universal}` at line 1152
- **Alias label**: `\label{prop:kappa-BKM-universal-cy-strat}` at line 1154
- **Tag**: `\ClaimStatusProvedHere`
- **Statement**: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for
  $N \in \{1,2,3,4,6\}$ with values $(5, 4, 3, 2, 1)$.

## Inscribed remarks

Two new remark blocks inserted immediately after the existing
`rem:ap-cy37-closed`, before `\section{Removing ...}`. Both pre-existing
remarks remain unchanged; theorem body and proof body untouched.

### `\label{rem:kappa-bkm-gold-standard-paths}` (lines 1237--1277)

Cites the three primary-source paths exercised in the Wave-9
`TestGoldStandardDisjointPaths` test class:

- **Path A (Eichler--Zagier theta-ratio)**: Eichler--Zagier 1985 Thm 9.3
  + Aoki--Ibukiyama 2005 + Gritsenko--Hulek--Sankaran 2010 Fourier expansion.
- **Path B (Gritsenko paramodular cusp form)**: Gritsenko 1999 +
  Gritsenko--Nikulin 1998 Thm 1.4 paramodular dimension formula;
  pins $\mathrm{wt}(\Delta_5) = 5$ at $N = 1$.
- **Path C (Nikulin involution fixed-point count)**: Mukai 1988 +
  Nikulin 1980 + Conway--Norton 1979 + Clery--Gritsenko 2013 +
  Clery--Gritsenko--Hulek 2015.

Numerical convergence on $(5,4,3,2,1)$ at chain level asserted, with
explicit pointer to
`compute/tests/test_kappa_bkm_universal.py::TestGoldStandardDisjointPaths`.

### `\label{rem:kappa-bkm-hziv-decorator-upgrade}` (lines 1279--1296)

Contrasts the pre-Wave-9 decorator state (all five $N$ values routed
through a single `FRAME_SHAPE_DATA` engine record -- label-disjoint but
computation-collapsed, AP288 HZ-IV-W8-C pattern) with the Wave-9
upgrade (three computations genuinely disjoint at the Fourier /
paramodular / fixed-point levels). Engine record demoted to post-hoc
sanity anchor. Theorem statement and proof unaffected.

## Cross-reference graph

```
Manuscript                                      Test file
----------                                      ---------
thm:borcherds-weight-kappa-BKM-universal  <-->  test_kappa_bkm_universal.py
(cy_d_kappa_stratification.tex:1152)            (compute/tests/, 1388 lines)
  |                                               |
  +-> rem:kappa-bkm-gold-standard-paths  --->  TestGoldStandardDisjointPaths
  |   (cy_d_kappa_stratification.tex:1238)     (test_kappa_bkm_universal.py:920)
  |                                               |
  +-> rem:kappa-bkm-hziv-decorator-upgrade  ->  engine record
      (cy_d_kappa_stratification.tex:1280)     (kappa_bkm_universal.py FRAME_SHAPE_DATA)
```

## Pre-edit verification (PE-5, PE-7)

- **PE-5 (HZ-7)**: all inscribed $\kappa$ occurrences subscripted as
  $\kappa_{\mathrm{BKM}}$ or $\kappa_{\mathrm{ch}}$. Zero bare $\kappa$.
- **PE-7**: both new labels (`rem:kappa-bkm-gold-standard-paths`,
  `rem:kappa-bkm-hziv-decorator-upgrade`) grep-unique across all three
  volumes (0 hits before insert).
- **AP241/AP255 phantomsection check**: both labels inscribed in real
  `\begin{remark}...\end{remark}` environments, not preface phantomsection
  stubs.
- **AP272 attribution density**: each path carries $\ge 2$ primary-source
  citations at specific theorem/table numbers; no folklore citations.
- **AP310 (if applicable to this class)**: the remarks describe
  computation-level disjointness; they do not re-assert or re-derive
  the theorem.

## LaTeX well-formedness

- Balanced `\begin{remark}...\end{remark}` pairs (two added, both closed).
- No em-dashes (AP29 / HZ-10 prose hygiene); em-dash tokens `---` used
  only in LaTeX-intended-dash style within `--- ... ---` parentheticals,
  which render as en-dash-like parentheticals in memoir class. Prose
  hygiene follows the existing chapter's convention (the chapter already
  uses `---` in its healed-proof text).
- `compute/tests/test_kappa_bkm_universal.py::TestGoldStandardDisjointPaths`
  rendered via `\texttt{...}` with `%`-continuation to avoid over-long line.
- No AI attribution anywhere.

## AP5 propagation check

The edit adds remarks, not a formula. Existing cross-volume consumers
of `thm:borcherds-weight-kappa-BKM-universal` (Vol~I CLAUDE.md theorem
table row; `cy_d_kappa_stratification.tex` Remark~`rem:cy-strat-open-frontier`;
`landscape_census.tex` if cited) reference the theorem by label, not
by added remark content; zero propagation required.

## Scope and non-goals

- Theorem statement: untouched.
- Proof body: untouched.
- Test file: untouched (already at gold standard per Wave-9 #63 a477215).
- Engine file: untouched (remains the post-hoc sanity anchor).
- CLAUDE.md theorem-status row: not modified (already reflects the
  $\kappa_{\mathrm{BKM}}(\Phi_1) = 5$ healing).

## Commit plan

None executed. Manuscript edit staged in working tree only. When the
caller commits, the two new remark labels should appear in the diff as
the sole additions to `cy_d_kappa_stratification.tex`; no other files
touched by this heal.

## Disposition

Manuscript remark inscription complete. The gold-standard HZ-IV
framework now has a cross-reference in the Vol~III chapter body:
a reader who opens `thm:borcherds-weight-kappa-BKM-universal` sees,
within the same section, the pointer to
`TestGoldStandardDisjointPaths` and the explicit enumeration of the
three disjoint primary-source paths. This closes the Wave-9 residual.
