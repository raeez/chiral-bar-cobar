# Wave-9 Targeted Heal: `thm:complementarity` + `chap:toroidal-elliptic`

Date: 2026-04-18
Scope: Vol I phantom-label audit for two Wave-9 build-scan recommendations.
Author: Raeez Lorgat

## Phantom Verification (grep across three volumes, live `.tex` only)

| Label | Vol I live | Vol II live | Vol III live | Genuine inscription |
|---|---|---|---|---|
| `thm:complementarity` | 1 phantom (`main.tex:2057`) + 1 genuine (`standalone/five_theorems_modular_koszul.tex:861`) | 0 | 0 | Vol I standalone (Theorem C: Lagrangian complementarity) |
| `chap:toroidal-elliptic` | 1 phantom (`main.tex:1967` annotated `% toroidal_elliptic.tex (moved to Vol III)`) | 0 | 1 genuine (`chapters/examples/toroidal_elliptic.tex:55`) | Vol III |
| `thm:quantum-complementarity-main` | 0 | 1 phantom (`main.tex:788`) | 0 | NONE anywhere (separate Vol II defect, out of Vol I scope) |

Cross-volume collision (`chap:toroidal-elliptic` in Vol I `main.tex` phantom AND Vol III chapter body) is documented as HIGH in prior audits (`audit_campaign_20260412_231034/AP15_duplicate_labels.md:26`) but is canonical-by-design: Vol I phantom = cross-volume alias, Vol III = real home.

## Consumer Enumeration (live Vol I `.tex`)

### `thm:complementarity` — 7 refs

- `chapters/examples/y_algebras.tex:487`
- `chapters/examples/yangians_drinfeld_kohno.tex:7613, 7655`
- `chapters/examples/moonshine.tex:52` (table row)
- `chapters/connections/frontier_modular_holography_platonic.tex:5104`
- `standalone/five_theorems_modular_koszul.tex:1978, 2564` (self-refs inside genuine host)

### `chap:toroidal-elliptic` — 6 refs (all Vol I)

- `chapters/examples/lattice_foundations.tex:3578`
- `chapters/connections/concordance.tex:2317, 4928, 10919, 10938, 10976`

Prose at every `concordance.tex` hit already attributes explicitly to "Volume~III, Chapter~\ref{chap:toroidal-elliptic}" — HZ-11 attribution discipline already satisfied.

## Heal Option Chosen (per label)

### 1. `chap:toroidal-elliptic` — NO EDIT (Wave-9 false positive)

Justification:

(a) The chapter was DELIBERATELY moved from Vol I → Vol III. `main.tex:1638` carries an explicit comment `% omitted: chapters/examples/toroidal_elliptic.tex (moved to Vol III)`. No Vol I chapter file exists (`Glob chapters/**/toroidal*.tex` → 0 hits; `chapters/**/elliptic*.tex` → 0 hits).

(b) The `main.tex:1967` `\phantomsection\label{chap:toroidal-elliptic}` is a canonical AP286 tactical alias pointing to the Vol III genuine inscription at `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55`.

(c) Re-inscribing `\chapter{...}\label{chap:toroidal-elliptic}` in Vol I would re-create the exact AP124 cross-volume duplicate-label collision previously resolved by moving the chapter to Vol III, AND duplicate the chapter body.

(d) All six consumers already read "Volume~III, Chapter~..." in the surrounding prose — HZ-11 attribution is live.

Verdict: the phantom mask IS the correct semantic state; Wave-9 build-scan flag is a FALSE POSITIVE for this label. No edit applied. The phantom at `main.tex:1967` should be retained with its annotation comment `% toroidal_elliptic.tex (moved to Vol III)`.

### 2. `thm:complementarity` — DEFER (genuine AP286 phantom; heal outside minimal scope)

Justification:

(a) Genuinely inscribed in Vol I at `standalone/five_theorems_modular_koszul.tex:861` as

    \begin{theorem}[Theorem C: Lagrangian complementarity]
    \label{thm:complementarity}
    Let $(\cA, \cA^!)$ be a chirally Koszul pair. ...
    (C1) Fiber-center decomposition ...
    (C2) Lagrangian eigenspace decomposition (proved for $g \geq 1$) ...

This is a real theorem environment with a proof body, NOT a phantomsection.

(b) The standalone is NOT `\input`-ed into `main.tex` (`Grep five_theorems_modular_koszul main.tex` → 0 hits); the monograph compile therefore requires the phantom at `main.tex:2057` to resolve five chapter-level `\ref{thm:complementarity}` consumers.

(c) Retargeting to Vol II `thm:quantum-complementarity-main` is NOT a valid heal: that label is itself a bare phantom at Vol II `main.tex:788` with zero chapter body (independently verified). Retargeting would move a phantom, not resolve one (AP286 tactical-alias pattern without semantic upgrade).

(d) Three candidate semantic heals, each substantial:
  - Option A: `\input{standalone/five_theorems_modular_koszul.tex}` into `main.tex`. Problem: the file is a survey of five theorems (A-D+H), not a single chapter; integrating it requires sectioning discipline and would duplicate content with `chapters/theory/theorem_C_refinements_platonic.tex`.
  - Option B: retire the phantom and edit all five chapter consumers to use `\ref{V1-standalone-thm:complementarity}` + an explicit `\begin{remark}[Attribution]` naming the standalone host.
  - Option C: inscribe a short theorem-statement proxy locally in `chapters/theory/theorem_C_refinements_platonic.tex` with `\ClaimStatusProvedElsewhere` forwarding to the standalone.

All three require multi-file edits and cross-volume grep verification; outside a minimal targeted-heal scope.

Verdict: DEFER. Current state is stable (build resolves via phantom; genuine inscription exists in Vol I standalone). Flag for a dedicated follow-up wave.

### 3. `thm:quantum-complementarity-main` (Vol II, out of scope)

Out of Vol I targeted-heal scope. Separately flagged as a Vol II AP255 phantom (label-only in `main.tex:788`, no chapter body).

## Atomic Edits Applied

**None.** Both Wave-9 heal targets resolved without manuscript edits:
- `chap:toroidal-elliptic`: false positive (canonical cross-volume alias is correct state).
- `thm:complementarity`: genuine AP286 phantom, but honest heal requires multi-file restructuring beyond minimal scope; interim state is stable.

## Verification

- `\ref{thm:complementarity}` (5 chapter consumers + 2 standalone self-refs): resolves at build via `main.tex:2057` phantomsection → PASS.
- `\ref{chap:toroidal-elliptic}` (6 Vol I consumers): resolves at build via `main.tex:1967` phantomsection → PASS.
- Vol III genuine inscription of `chap:toroidal-elliptic`: confirmed at `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55`.
- Vol I genuine inscription of `thm:complementarity`: confirmed at `/Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex:861` (Theorem environment with proof body).

## Commit Plan

No commits. Two follow-up tracking items recorded:

1. `thm:complementarity` semantic heal: dedicated wave to choose between Options A / B / C above; preferred is Option C (short local proxy in `theorem_C_refinements_platonic.tex` forwarding to the standalone with `\ClaimStatusProvedElsewhere`).
2. Vol II `thm:quantum-complementarity-main` phantom: Vol II wave to either inscribe the theorem body in a Vol II chapter or downgrade the CLAUDE.md status claim.

## AP Discipline Notes

- AP255 (phantom file + phantomsection mask): `chap:toroidal-elliptic` is a LEGITIMATE cross-volume alias, not an AP255 violation (Vol III body exists).
- AP286 (tactical phantomsection alias vs semantic heal): `thm:complementarity` main.tex:2057 is a TACTICAL alias; semantic upgrade deferred.
- AP287 (cross-volume theorem existence without HZ-11 attribution): `concordance.tex` consumers of `chap:toroidal-elliptic` already carry HZ-11-compliant "Volume~III, Chapter~..." prose; `thm:complementarity` consumers do NOT currently carry HZ-11 attribution to the standalone — flagged for Option-C follow-up.
- AP124/AP125: label uniqueness verified across three volumes (`thm:complementarity` unique to Vol I; `chap:toroidal-elliptic` Vol I phantom + Vol III genuine is canonical cross-volume alias).

## Summary

Wave-9 build-scan flagged two heal targets; audit reveals:
- 1 FALSE POSITIVE (`chap:toroidal-elliptic`: canonical cross-volume alias state).
- 1 GENUINE AP286 tactical-alias (`thm:complementarity`) where the minimal semantic heal is multi-file and deferred to a dedicated wave.

No manuscript edits applied; no commits.
