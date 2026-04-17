# Wave-10 VIII-B Relaunch: thqg anchor inscription

**Date**: 2026-04-17
**Scope**: 8 missing `ch:thqg-*` / `subsec:thqg-*` slugs from Wave-9 #58 VIII-A residue
**Protocol**: Inscribe alias labels as sibling `\label{ch:...}` / `\label{subsec:...}`
immediately after the governing `\section{...}` or `\subsection{...}` declaration,
following the Wave-9 convention established in
`thqg_holographic_reconstruction.tex:6` and `thqg_symplectic_polarization.tex:27`.

## Per-slug outcomes

| # | Slug | File | Outcome | Site |
|---|------|------|---------|------|
| 1 | `ch:thqg-3d-gravity-movements` | `thqg_3d_gravity_movements_vi_x.tex` | INSCRIBED as alias under `\subsection{Movement VI: gravitational $S$-duality}` | L8 |
| 2 | `ch:thqg-3d-gravity-vi-x` | `thqg_3d_gravity_movements_vi_x.tex` | INSCRIBED as alias under same Movement VI heading (synonym of #1) | L9 |
| 3 | `ch:thqg-critical-string` | `thqg_critical_string_dichotomy.tex` | INSCRIBED as alias under `\section{Critical string dichotomy}` | L6 |
| 4 | `ch:thqg-gravitational-complexity` | `thqg_gravitational_complexity.tex` | INSCRIBED as alias under `\section{Gravitational complexity}` | L12 |
| 5 | `ch:thqg-perturbative-finiteness` | `thqg_perturbative_finiteness.tex` | INSCRIBED as alias under `\section{Perturbative finiteness}` | L11 |
| 6 | `ch:thqg-soft-graviton` | `thqg_soft_graviton_theorems.tex` | INSCRIBED as alias under `\section{The celestial soft hierarchy from the shadow obstruction tower}` | L18 |
| 7 | `subsec:thqg-genus2-fredholm` | `thqg_fredholm_partition_functions.tex` | INSCRIBED as alias under `\subsubsection{Genus 2: two handles and the Siegel modular form}` | L1107 |
| 8 | `subsec:thqg-non-fredholm` | `thqg_fredholm_partition_functions.tex` | INSCRIBED as alias under `\subsection{Non-Fredholm corrections for classes L, C, M}` (sibling to existing `subsec:thqg-X-non-fredholm`) | L1735 |

## Verification

- `grep -rn '\\label\{ch:thqg-(3d-gravity-movements|3d-gravity-vi-x|critical-string|gravitational-complexity|perturbative-finiteness|soft-graviton)\}'` returns exactly 6 hits, one per slug, each on the expected file.
- `grep -rn '\\label\{subsec:thqg-(genus2-fredholm|non-fredholm)\}'` returns exactly 2 hits in `thqg_fredholm_partition_functions.tex`.
- Cross-volume uniqueness: none of the 8 new slugs appear in `~/chiral-bar-cobar` or `~/calabi-yau-quantum-groups`.
- No chapter needed retargeting or deletion; all six "chapter" anchors in
  Vol~II's `connections/` directory are in fact `\section{...}`-level nodes
  (the files are `\input`-ed into a parent Twisted Holography and Quantum
  Gravity chapter), so the alias pattern from Wave-9 #58 applies uniformly.

## Hook warnings (pre-existing, not introduced)

The PostToolUse hook surfaced several AP24 / AP8 / AP14 / AP7 warnings on
lines far from the insertion sites (e.g., L1020, L1230, L2802, L2725 in
various files). All predate this heal and concern pre-existing manuscript
content outside the VIII-B scope. Forwarded for downstream rectification;
not addressed here.

## No commit performed

Per task instructions.
