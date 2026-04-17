# Wave 9 VIII-A: Systemic Phantom `V1-*thqg-*` Sweep

**Date.** 2026-04-17
**Scope.** Systemic healing of phantom cross-volume `\ref{V1-*thqg*}` references across Vol II, flagged by Wave-8 #54 (`wave8_vol_ii_part_vi_attack_heal.md`) as a remaining debt of ~287 references in 14 files.
**Outcome.** Full closure. 222 phantom `V1-*thqg*` references eliminated; 141 disabled labels re-inscribed; 25 additional same-pathology refs (non-V1 but disabled-target) healed opportunistically; 8 truly missing slugs deferred to Wave 10.

## 1. The Pattern

Across Vol II `chapters/connections/`, 14 THQG files contained references of the form
```
\ref{V1-<PREFIX>:thqg-<BODY>}
```
with `V1-` prefix signalling (falsely) that the target lives in Vol I. Cross-volume grep verified that
**none of these targets exist in Vol I**; instead, each target was a Vol II label that had been
previously disabled by replacing the `\label{...}` command with a comment of the form
```
% label removed: <PREFIX>:thqg-<BODY>
```
either on a standalone line or inline with `\begin{equation}`. The content of the theorem /
definition / equation remained in the file body; only the `\label{...}` command was stripped.

The `linear_read_notes.md` cross-volume-externals gate was therefore tolerating a large block of
false positives: the LaTeX build did not emit `[?]` for cross-volume references (they are elided as
external links), so the debt had accumulated silently.

## 2. Inventory

Exhaustive enumeration of `\\ref\{V1-([^}]*thqg[^}]*)\}` across Vol II gave:

| metric | count |
|---|---|
| distinct phantom slugs | 143 |
| total phantom references | 222 |
| files affected | 12 |

Ref-site file distribution:

| file | refs |
|---|---|
| `thqg_perturbative_finiteness.tex` | 45 |
| `thqg_soft_graviton_theorems.tex` | 32 |
| `thqg_symplectic_polarization.tex` | 31 |
| `thqg_gravitational_s_duality.tex` | 28 |
| `thqg_modular_bootstrap.tex` | 26 |
| `thqg_gravitational_yangian.tex` | 21 |
| `thqg_gravitational_complexity.tex` | 15 |
| `thqg_fredholm_partition_functions.tex` | 12 |
| `thqg_holographic_reconstruction.tex` | 6 |
| `twisted_holography_quantum_gravity.tex` | 4 |
| `examples-complete-proved.tex` | 1 |
| `foundations_overclaims_resolved.tex` | 1 |

Note: Wave-8 #54's original estimate of 287 refs in 14 files slightly overcounted; the actual
figure restricted to the `V1-*thqg*` pattern is 222 refs in 12 files. The overcount came from
conflating `V1-` refs to non-thqg slugs inside the same THQG files.

## 3. Classification

Each of the 143 distinct slugs was classified by checking the target against the global Vol II
label index (15,654 Vol I active labels and 4,275 Vol III active labels also loaded for
completeness):

| class | description | slugs | refs |
|---|---|---|---|
| A | Self-disabled in Vol II (target has `% label removed:` marker in a Vol II file) | 141 | 219 |
| B | Mis-prefixed (target is active in Vol II already, without `V1-`) | 1 | 2 |
| C | Genuinely external (target active in Vol I) | 0 | 0 |
| D | In Vol III | 0 | 0 |
| E | Absent everywhere | 1 | 1 |

Class A dominates: every phantom that Wave-8 #54 predicted would be self-label-disabled indeed
is. Class B contains exactly `thm:thqg-swiss-cheese` (active in
`chapters/connections/3d_gravity.tex`). Class E contains `thm:thqg-I-heisenberg-partition`
(a drifted slug; nearest live target is `prop:thqg-I-heisenberg-detail`).

The duplicate-label risk check confirms that no Class A slug is simultaneously active elsewhere in
Vol II or Vol I or Vol III; re-inscription is safe.

## 4. Heal Protocol

For each slug, the heal is:

1. **Strip the `V1-` prefix at every ref site.** Regex: `\ref{V1-<SLUG>}` → `\ref{<SLUG>}`,
   guarded to act only when `thqg` appears in the slug body (preserving genuine `V1-` refs to
   non-thqg Vol I targets, of which none were found in this pattern).
2. **Re-inscribe the disabled label at the declaration site.** Three regex forms cover all
   observed variants:
   - Standalone: `^\s*% label removed: <SLUG>$` → `\label{<SLUG>}` (preserving leading indent).
   - Inline with environment opener: `\begin{equation}% label removed: <SLUG>` → `\begin{equation}\label{<SLUG>}`.
   - Trailing `%` (LaTeX line-continuation comment closer): `% label removed: <SLUG>%` → `\label{<SLUG>}%`.
   - `\item` prefix: `\item % label removed: <SLUG> ...` → `\item \label{<SLUG>} ...`.
3. **Class E retarget.** `\ref{thm:thqg-I-heisenberg-partition}` → `\ref{prop:thqg-I-heisenberg-detail}`
   at `thqg_perturbative_finiteness.tex:2653`. The sentence (“Substitute the determinant formula
   into the Heisenberg partition function”) is mathematically identical whether cast as a
   reference to the proposition that builds the Heisenberg partition function or to a theorem
   stating the same result; no substantive retargeting ambiguity.

The script is idempotent and purely mechanical: no mathematical judgment enters the heal beyond
the Class E retarget.

## 5. Execution

Two passes:

- **Pass 1** (regex forms 1 and 2 for re-inscription): 222 ref-strips + 133 label re-inscribes,
  spread across 12 files.
- **Pass 2** (regex forms 3 and 4 for the 8 residuals): 8 additional label re-inscribes in
  `thqg_perturbative_finiteness.tex` (2) and `thqg_fredholm_partition_functions.tex` (6).

Totals: **222 ref-strips + 141 label re-inscribes + 1 retarget**, matching inventory.

## 6. Opportunistic Secondary Heal

Post-heal validation surfaced 41 additional unresolved `\ref{...thqg...}` slugs (no `V1-`
prefix, but targets absent from the active-label index). Intersecting with the
`% label removed:` corpus showed that **25 of these 41** share the identical disabled-target
pathology (same heal mechanism). These are not V1- mis-prefixed — they are simply refs whose
targets were disabled by the same earlier sweep that produced the V1- phantoms — but the heal
plumbing is identical, so they were healed in the same wave for atomicity:

| file | re-inscribes |
|---|---|
| `thqg_bv_construction_extensions.tex` | 15 |
| `twisted_holography_quantum_gravity.tex` | 7 |
| `thqg_perturbative_finiteness.tex` | 2 |
| `thqg_gravitational_yangian.tex` | 1 |

Twenty-five previously broken `\ref` sites are now resolved.

## 7. Residual

Eight truly missing thqg slugs remain (targets absent from the manuscript entirely, not in
`% label removed:` form):

- `ch:thqg-3d-gravity-movements`, `ch:thqg-3d-gravity-vi-x`, `ch:thqg-critical-string`,
  `ch:thqg-gravitational-complexity`, `ch:thqg-perturbative-finiteness`, `ch:thqg-soft-graviton`
  (six chapter-level anchors that chapter files fail to declare themselves — their `\chapter{...}`
  commands are missing the companion `\label{ch:...}`).
- `subsec:thqg-genus2-fredholm`, `subsec:thqg-non-fredholm` (two subsection anchors in
  `thqg_fredholm_partition_functions.tex`).

These are genuinely missing, not disabled; healing requires either (a) inserting the
chapter-level / subsection-level labels at the right `\chapter` / `\subsection` declarations or
(b) retargeting the eight refs to sibling anchors. This is deferred to **Wave 10 VIII-B**.

The broader Vol II post-heal tally shows 419 non-V1/V3 broken `\ref` sites across 9,475
references overall — pre-existing debt outside the VIII-A phantom class, tracked separately.

## 8. Constitutional Hygiene

No AP / HZ / catalogue slug introduced in any typeset .tex; the heal touches only
`\label{}` commands and `\ref{}` arguments. Post-edit grep confirms no new
metadata-hygiene violations in the modified files.

## 9. Files Modified

Twelve Vol II files, all under `chapters/connections/` or `chapters/examples/` or
`chapters/theory/`:

```
chapters/connections/thqg_bv_construction_extensions.tex
chapters/connections/thqg_fredholm_partition_functions.tex
chapters/connections/thqg_gravitational_complexity.tex
chapters/connections/thqg_gravitational_s_duality.tex
chapters/connections/thqg_gravitational_yangian.tex
chapters/connections/thqg_holographic_reconstruction.tex
chapters/connections/thqg_modular_bootstrap.tex
chapters/connections/thqg_perturbative_finiteness.tex
chapters/connections/thqg_soft_graviton_theorems.tex
chapters/connections/thqg_symplectic_polarization.tex
chapters/connections/twisted_holography_quantum_gravity.tex
chapters/examples/examples-complete-proved.tex
chapters/theory/foundations_overclaims_resolved.tex
```

## 10. Cross-Volume Atomicity

No Vol I or Vol III file was modified. The phantoms were 100% Vol II self-references with
erroneous `V1-` prefix; the heal is self-contained within Vol II. No cross-volume propagation
step required (HZ-5 discipline: atomic sub-label rename is trivially satisfied when no sub-label
rename occurred — the label slugs were preserved, only the disabled/active status changed).

## 11. Verdict

**VIII-A closed.** Zero phantom `V1-*thqg*` references remain. Wave-9 total: 222 primary heals
+ 25 opportunistic secondary heals + 1 Class E retarget = 248 sites resolved across 13 Vol II
files. Eight truly missing chapter/subsection anchors deferred to Wave 10 VIII-B with explicit
target list above.
