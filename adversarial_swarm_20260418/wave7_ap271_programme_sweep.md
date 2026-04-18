# Wave-7 AP271 Programme-Wide Reverse-Drift Sweep

Date: 2026-04-18. Scope: CLAUDE.md Theorem Status table (rows 578-630, 53 rows of math content).
Discipline: AP271 (CLAUDE.md stale-behind-manuscript) and AP305 (CLAUDE.md overstating deficit).

## Methodology

For each row, three-check audit:
(a) Line-drift: does cited `file:line` still hold the advertised `\label{}`?
(b) Status-downgrade-missing: does row status match inscribed `\ClaimStatus*` tag?
(c) Scope-match: does row scope claim match inscribed theorem scope?

Categories: CLEAN | AP271-LINE-DRIFT | AP271-STATUS-DOWNGRADE-MISSING | AP271-SCOPE-WIDER | AP305-SCOPE-NARROWER | AP271-REFERENCE-STALE.

## Row audit (selected; full table below)

| Row (L#) | Advertised | Inscribed | Category | Heal |
|---|---|---|---|---|
| A (578) | PROVED fixed curve; modular-family CONDITIONAL | `thm:A-infinity-2` at `theorem_A_infinity_2.tex:730` + `rem:A-infinity-2-modular-family-scope` at :890 | CLEAN | — |
| B (579) | PROVED weight-completed | `thm:chiral-positselski-weight-completed` at `theorem_B_scope_platonic.tex:245` (correct) | AP271-REFERENCE-STALE: phantom-flag sentence about `-7-2` / `-5-3` obsolete after Wave-6 AP286 co-location at :246-247 | APPLIED: rewrote "Phantom flag" sentence → "Alias notice (AP286 Option-A)" pointing at co-located phantomsection aliases |
| C (580) | Mixed statuses per clause | `theorem_C_refinements_platonic.tex` exists | CLEAN (post-Wave-5 rectification) | — |
| D (581) | g=1 unconditional; g=2 scalar-diagonal; g≥3 conditional | matches Wave-1 F1-F7 inscription | CLEAN | — |
| H (582) | PROVED sharp Hilbert; E_1 inscribed | `thm:hochschild-concentration-E1` inscribed | CLEAN | — |
| MC1-4 (583) | Eval-core; conditional elsewhere | matches Wave-9 five-family heal | CLEAN | — |
| MC5 (584) | PROVED 3 ambients; direct-sum false | matches Wave-1 audit healing | CLEAN | — |
| Koszul (585) | 8 + 1 + 1 + 1 honest count | chapter opening at :77-89 carries honest count; header at :2348 still legacy "10 unconditional" | AP271-SCOPE-WIDER (row text acknowledges; header pending) | DEFERRED — requires re-alignment of theorem header text (not a single-line edit) |
| D^2=0 (586) | PROVED | standard | CLEAN | — |
| Theta_A (587) | PROVED | standard | CLEAN | — |
| SC-formal (588) | Forward unconditional; converse CONDITIONAL | `rem:sc-formal-open-transfer-frontier` cited; Wave-5 heal inscribed | CLEAN (post-Wave-5) | — |
| Depth gap (589) | PROVED | d_alg scope inscribed only on Koszul locus; off-locus chain-level d_alg open per roadmap | AP271-SCOPE-WIDER | APPLIED: added "on the chirally Koszul standard landscape" scope qualifier |
| ChirHoch^1 KM (590) | PROVED general simple g | `prop:chirhoch1-affine-km` at `:2133` (row cited `:2132`); `prop:chirhoch2-affine-km-general` at `:2223` (row cited `:2221`) | AP271-LINE-DRIFT (2-line drift) | APPLIED: corrected to `:2133` and `:2223` |
| Topologization (591) | G/critical orig; L Q_tot-cohom; M weight-completed | matches Wave-1 audit + `conj:topologization-general` at `en_koszul_duality.tex:3392` | CLEAN | — |
| E_3 identification (592) | Simple g PROVED; gl_N remark-level + phantom gaps | Wave-5 AP255 phantom audit inscribed | CLEAN (honest) | — |
| Elliptic chiral QG (593) | Belavin PROVED sl_2; Felder↔KZB CONJECTURAL orphan | per AP275 HOT ZONE correction | CLEAN | — |
| CY_4 p_1-twisted (594) | CONSTRUCTED + CONJECTURED; negative proved | matches Vol III audit | CLEAN | — |
| Toroidal (595) | Formal disk PROVED; global conditional; AP255 orphan noted | matches Vol I+III inscription | CLEAN | — |
| Chiral QG equiv (596) | Ordered base PROVED Koszul locus; elliptic/toroidal standalone-only per AP255 | matches | CLEAN | — |
| Non-principal W (597) | Koszulness PROVED per nilpotent; hook-type CONDITIONAL | per Wave-7 heal | CLEAN | — |
| gl_N chiral QG (598) | N=2 unconditional; N≥3 conditional on JKL26 | freshly healed 2026-04-18 (same-day swarm) | CLEAN | — |
| Verlinde (599) | ProvedElsewhere at boundary genera; g≥2 conditional | freshly healed 2026-04-18 | CLEAN | — |
| ker(av) (600) | Scope WIDER than simple g | Wave-4 ker(av) heal inscribed | CLEAN | — |
| Miura coefficient (602) | PROVED (Ψ-1)/Ψ all spins | `thm:miura-cross-universality` + Wave-3 structural mirror | CLEAN | — |
| DS intertwining (619) | VERIFIED (bare) | `compute/lib/ds_coproduct_intertwining_engine.py:103-104` admits degree-1 tautology | AP271-STATUS-DOWNGRADE-MISSING | APPLIED: rewrote row to "VERIFIED at degree ≥ 2 (non-trivial); degree 1 tautological" + engine-docstring citation |

## Category breakdown

- CLEAN: 21 rows spot-checked (≈ 80% of audited sample)
- AP271-LINE-DRIFT: 1 (ChirHoch^1 KM: 2-line off for both prop refs) — HEALED
- AP271-REFERENCE-STALE: 1 (Thm B phantom flag) — HEALED
- AP271-SCOPE-WIDER: 2 (Depth gap; Koszul header count) — 1 HEALED, 1 DEFERRED (requires header-text realignment, multi-site propagation)
- AP271-STATUS-DOWNGRADE-MISSING: 1 (DS intertwining) — HEALED
- AP305-SCOPE-NARROWER: 0 detected in this sample
- Not audited in depth (deferred to future waves): the 30+ rows from lines 603-630 (Z_g closed forms, W_N Stokes, Shadow=GW(C³), Conformal anomaly, Chiral Higher Deligne, SC^{ch,top} heptagon, UCH, Periodic CDG, E_∞-Topologization, Thm A^{∞,2}, CY-D dimension stratification, BP Koszul-conductor, Critical level jump, Genus-2 degree decomp, Antipode non-lifting, AP128 bar H^2, qdet ordering, E_3 via Dunn, E_3 for gl_N, 6d hCS defect, DDYBE, ChirHoch*(H_k), Drinfeld-double-vs-derived-center, Toroidal formal disk, Coderived E_3, KZB flatness).

## Heals applied this wave

1. ChirHoch^1 KM: line-number corrections `:2132 → :2133` and `:2221 → :2223` (AP271-LINE-DRIFT, atomic).
2. Theorem B: stale "Phantom flag" sentence about `-7-2`/`-5-3` rewritten to "Alias notice (AP286 Option-A)" reflecting post-Wave-6 co-location of phantomsection aliases with canonical theorem (AP271-REFERENCE-STALE).
3. Depth gap: added "on the chirally Koszul standard landscape" scope qualifier + off-locus-open note (AP271-SCOPE-WIDER).
4. DS intertwining: bare "VERIFIED" → "VERIFIED at degree ≥ 2 (non-trivial); degree 1 tautological" with engine-docstring citation (AP271-STATUS-DOWNGRADE-MISSING / AP256/AP257 discipline).

Total heals: 4 atomic, all in-place single-line rewrites of CLAUDE.md, no math content changed, no cross-volume propagation needed.

## Residual open / deferred

- Koszul row "10 unconditional" legacy header at `chiral_koszul_pairs.tex:2348`: deferred; requires atomic edit to chapter header text + propagation sweep across 9 files (`landscape_census.tex`, `working_notes.tex`, four surveys, Vol II `thqg_introduction_supplement_body.tex`) per AP273 already catalogued. Not in single-line heal scope.
- Rows 603-630 (25 rows): deferred to future Wave-7+ continuations. Priority targets for next wave:
  - Chiral Higher Deligne / SC^{ch,top} heptagon / UCH / Periodic CDG (Vol II freshly inscribed, high consumer load)
  - CY-D dimension stratification (Vol III cross-volume)
  - BP Koszul-conductor (convention caveat 196 vs 50 already in place; verify row text still matches source)
  - Critical level jump / Genus-2 degree decomp / qdet ordering / AP128 bar H^2 (older claims with compact row text; low likelihood of drift but low audit cost)

## Commit plan

No commit this wave. All four heals are content-neutral single-line rewrites of CLAUDE.md. Recommend batching this wave's heals with the pending Koszul-row header re-alignment in a future dedicated commit titled "Vol I CLAUDE.md Wave-7 AP271 reverse-drift sweep: 4 atomic heals + Koszul header realignment" once the Koszul realignment is separately executed.

## Cross-wave provenance

This sweep tracks flags raised by:
- Wave-4 ker(av) heal (ker(av) row healed upstream, verified CLEAN here)
- Wave-4 depth gap agent (scope qualifier flagged, HEALED here)
- Wave-4 chirhoch_1_km propagation (line numbers were updated upstream but drifted to :2132/:2221 before Wave-4's :2133/:2223 re-inscription; HEALED here)
- Wave-5 DS intertwining agent (AP271 flag, HEALED here)
- Wave-5 SC formality heal (verified CLEAN)
- Wave-6 Theorem B phantom audit (AP286 Option-A co-location completed, CLAUDE.md stale; HEALED here)
- Wave-7 topologization_general_phantom_heal (verified CLEAN; row already correct)

## Sanity note

The reverse-drift rate in the audited sample (≈ 15%, 4 heals over ≈ 26 rows inspected) confirms AP271's programme-wide signal: even after repeated heal waves, CLAUDE.md lags manuscript inscriptions by 1-3 waves. Commit-gate recommendation (already in AP271 counter): before every CLAUDE.md status-table edit, grep cited theorem's chapter for `\begin{remark}[Scope`, `\ClaimStatusConditional`, new `\label` line numbers, and sibling `\phantomsection` aliases; propagate same session.
