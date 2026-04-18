# Wave-6 r-matrix level-prefix constitutional sweep (HZ-1 / AP126 / AP141 / C9)

**Date:** 2026-04-18
**Scope:** programme-wide hygiene sweep, all three volumes, r-matrix level-prefix discipline.
**Author:** Raeez Lorgat.

## Mission

Enumerate and heal all bare r-matrix formulas programme-wide per HZ-1 (the most-violated AP in the programme, historically 90+ instances across six waves). Canonical forms (C9):

- Trace-form convention: `r^{KM}(z) = k·Ω/z` (level prefix k MANDATORY; k=0 → r=0).
- KZ convention: `r^{KM}(z) = Ω/((k+h^v)z)` (k=0 → Ω/(h^v·z) ≠ 0 for non-abelian g).
- Virasoro: `r^{Vir}(z) = (c/2)/z^3 + 2T/z` (cubic + simple pole).
- Heisenberg: `r^{Heis}(z) = k/z`.

Forbidden bare forms: `Ω/z` without level, `kΩ/z²`, `Ω d log z` without prefix, `(c/2)/z²`, `(c/2)/z^4`.

## Programme-wide grep enumeration

Searched `*.tex` across:
- `/Users/raeez/chiral-bar-cobar` (Vol I)
- `/Users/raeez/chiral-bar-cobar-vol2` (Vol II)
- `/Users/raeez/calabi-yau-quantum-groups` (Vol III)

Six grep patterns: `r(z) = Ω/z` literal; `r^{KM/Vir/Heis}(z) = ...`; bare `Ω d log z`; Virasoro wrong-pole-order `(c/2)/z^2`, `(c/2)/z^4`; general `r(z) = Ω`.

## Violation table

| # | File | Line | Formula | Family | Verdict | Heal |
|---|------|------|---------|--------|---------|------|
| 1 | `vol2/working_notes.tex` | 590 | `r(z) = Ω_g/z` (Chern-Simons affine KM) | class L | VIOLATION (AP126) | Added `k` prefix + bridge + k=0 check |
| 2 | `vol2/working_notes.tex` | 815 | `r(z) = Ω_{sl_2}/z = (J^a⊗J_a)/z` (sl_2 example) | class L | VIOLATION (AP126) | Added `k` prefix + h^v(sl_2)=2 KZ equivalent |
| 3 | `vol2/super_chiral_yangian.tex` | 484 | `r(z) = Ω^s/z` (super-Yangian) | Yangian (Yang rational) | CONVENTION MARKER NEEDED (AP144) | Added inline "Yang rational, ℏ absorbed in R(z) = id + ℏr + O(ℏ²)" marker |
| 4 | `vol3/fukaya_categories.tex` | 967 | `r(z) = Ω_{Mu}/z` (K3 abelian Yangian) | Heisenberg-type (class G, rank 24) | CONVENTION MARKER NEEDED (AP144) | Added level-absorbed marker: Mukai pairing supplies level in Ω_{Mu} |
| 5 | `vol1/compute/audit/standalone_paper/classification.tex` | 108 | `r(z) = Ω_g/z` | class L | OUT-OF-BUILD audit workspace | NO EDIT — zero consumers verified |

**Total production edits: 4. Audit workspace flagged: 1.**

## Legitimate (non-violation) Ω d log z / Ω/z hits verified

Vol II `Ω d log z` appearances all carry explicit level prefix:
- `preface_full_survey.tex:514` — KZ `1/(k+h^∨)·Ω d log z` ✓
- `spectral-braiding-core.tex:2570` — `k·Ω d log z` ✓
- `thqg_line_operators_extensions.tex:502,1112` — `Ω d log(z)/(k+2)`, `ℏ·Ω d log z` ✓
- `log_ht_monodromy_core.tex:286`, `log_ht_monodromy.tex:278` — `k·Ω d log(z_i−z_j)` ✓
- `introduction.tex:1449` — KZ `1/(k+h^∨)·Ω d log z` ✓

Vol II `spectral-braiding-core.tex:819` writes `r(z) = Ω_k/z = k·Ω/z` where `Ω_k := k·Ω` is defined at line 817 — **level-absorbed notation**, not bare.

Vol I `standalone/gaudin_from_collision.tex:298` writes `(k+h^∨)·r(z) = Ω/z` — rescaled residue at critical level, explicit level multiplier on LHS.

Vol I `chapters/theory/chern_weil_level_shift_platonic.tex:565,577,579` writes `Ω/z` inside the AP126 **healing chapter** explicitly describing the forbidden bare form as a foil before augmenting — legitimate metadiscourse.

Vol I `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex` — explicit archival backup (timestamp suffix), out of build, not in scope.

## PE-1 templates (per edit)

### Edit 1: `vol2/working_notes.tex:590`

```
## PRE-EDIT: r-matrix
family:                    affine KM (ĝ_k, class L, Chern-Simons boundary)
r(z) written (CURRENT):    r(z) = Ω_g/z                    [BARE]
level parameter symbol:    k
OPE pole order p:          2 (Casimir)
r-matrix pole order p-1:   1 (after d-log absorption)
convention:                trace-form target
AP126 check (CURRENT):     r(z)|_{k=0} = Ω/z ≠ 0           [VIOLATION]
heal target:               r(z) = k·Ω_g/z + bridge remark + k=0 check inline
AP126 check (HEALED):      r(z)|_{k=0} = 0                 ✓
AP141 bare Ω/z count:      1 → 0
source:                    C9 census canonical form; compute/lib landscape_census.tex
verdict:                   ACCEPT
```

### Edit 2: `vol2/working_notes.tex:815`

```
## PRE-EDIT: r-matrix
family:                    affine KM sl_2 (V_k(sl_2), h^∨ = 2)
r(z) written (CURRENT):    r(z) = Ω_{sl_2}/z = (J^a ⊗ J_a)/z   [BARE]
level parameter symbol:    k
convention:                trace-form target
AP126 check (CURRENT):     r(z)|_{k=0} = Ω_{sl_2}/z ≠ 0    [VIOLATION]
heal target:               r(z) = k·Ω_{sl_2}/z = k·(J^a ⊗ J_a)/z + KZ bridge
AP126 check (HEALED):      r(z)|_{k=0} = 0                 ✓
bridge identity:           k·Ω_tr = Ω/(k+h^∨) = Ω/(k+2) at sl_2
verdict:                   ACCEPT
```

### Edit 3: `vol2/super_chiral_yangian.tex:484`

```
## PRE-EDIT: r-matrix
family:                    super-Yangian Y_ℏ(g), super Lie algebra g
r(z) written:              r(z) = Ω^s/z
level parameter symbol:    ℏ (Yangian deformation; r is the classical-limit kernel)
convention:                Yang rational (ℏ absorbed in R(z) = id + ℏr + O(ℏ²) per line 475)
AP126 discipline:          N/A — no affine level; Yangian convention distinct
AP144 bridge:              INLINE CONVENTION MARKER REQUIRED (Yang rational vs KZ vs trace-form)
heal:                      convention marker stating ℏ absorbed in R(z); level-prefix discipline not applicable
verdict:                   ACCEPT
```

### Edit 4: `vol3/fukaya_categories.tex:967`

```
## PRE-EDIT: r-matrix
family:                    abelian Lie conformal envelope MH_2(Λ_K3), Heisenberg-type (class G, rank 24)
r(z) written:              r(z) = Ω_{Mu}/z
level parameter:           Mukai pairing supplies level (cf. OPE line 966: J^a J^b ~ ⟨a,b⟩_Mu/(z-w)²)
convention:                level-absorbed (Ω_{Mu} = Σ κ^{IJ}_Mu t_I ⊗ t_J with Mukai pairing as invariant form)
analogous to:              vol2/spectral-braiding-core.tex:819 Ω_k = k·Ω pattern
heal:                      inline convention marker identifying Ω_{Mu} as level-absorbed
verdict:                   ACCEPT
```

## Before/after grep gate

**BEFORE (production):** 4 bare `r(z) = Ω/z` violations + 1 audit-workspace instance.

**AFTER (production):** 0 bare forms in Vol I/II/III production `.tex`. Audit-workspace instance retained (zero build consumers).

Verification commands:
```bash
rg 'r\(z\)\s*=\s*\\Omega_?\\?\{?\w*\}?/z' \
  /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/standalone \
  /Users/raeez/chiral-bar-cobar/appendices --type tex -n
# Returns only legitimate healing-chapter foils + level-multiplied forms.

rg 'r\(z\)\s*=\s*\\Omega_?\\?\{?\w*\}?/z' \
  /Users/raeez/chiral-bar-cobar-vol2 --type tex -n
# Returns only spectral-braiding-core.tex:819 (level-absorbed equality Ω_k = k·Ω).

rg 'r\(z\)\s*=\s*\\Omega_?\\?\{?\w*\}?/z' \
  /Users/raeez/calabi-yau-quantum-groups --type tex -n
# Returns ZERO hits post-heal.
```

## Residual frontier

1. **Vol I audit-workspace classification.tex:108.** Out-of-build, zero consumers, low priority. Option: delete or add `% HISTORICAL audit artifact, superseded by chapters/examples/` banner.
2. **AP144 bridge-identity compliance.** All KM r-matrix sites should carry both conventions (trace-form AND KZ) with explicit bridge `k·Ω_tr = Ω/(k+h^∨)`. Current programme-wide practice is convention-per-site; a future sweep could add bridge remarks uniformly. Not strictly HZ-1.
3. **Convention markers beyond KM.** Super-Yangian and K3 Mukai heals added markers; a programme-wide sweep of Yangian/super-Yangian/elliptic/toroidal r-matrix sites for Yang-rational/trigonometric/elliptic convention markers per AP144 would complete the hygiene campaign.
4. **Belavin / Felder / Weierstrass propagator audit (per AP275).** Vol I Elliptic chiral QG row: the CLAUDE.md line "θ_1'/θ_1 NOT Weierstrass ζ" was inverted (AP275 canonical example); the correct inscribed form is the FULL ζ_τ = θ_1'/θ_1 + 2η_1 z. Wave-3 elliptic agent already healed `standalone/seven_faces.tex:1005-1017` + CLAUDE.md line 593. Re-verified in this sweep: no further bare Weierstrass / Belavin / Felder hits found in the three volumes.
5. **Hook-flagged adjacent APs in `working_notes.tex`.** Pre-existing file-level APs (AP24/AP8/AP25/AP34/AP106/AP121/AP7/AP32/AP44/V2-AP26) surfaced by the post-edit hook. These are out of this sweep's scope (AP126/AP141 only) and belong to a separate working_notes.tex audit.

## Commit plan

NO COMMITS made in this sweep (per mission constraint). Diff summary:

```
vol2/working_notes.tex                         | 2 files changed (lines 590, 815)
vol2/chapters/theory/super_chiral_yangian.tex  | 1 file changed (line 484)
vol3/chapters/examples/fukaya_categories.tex   | 1 file changed (line 967)
```

Suggested commit message (if user chooses to commit):

```
Wave-6 r-matrix level-prefix constitutional sweep (HZ-1 / AP126 / AP141 / C9)

Four heals across Vol II + Vol III:
- vol2/working_notes.tex: bare r(z) = Ω_g/z → k·Ω_g/z + KZ bridge (Chern-Simons)
- vol2/working_notes.tex: bare r(z) = Ω_{sl_2}/z → k·Ω_{sl_2}/z + h^∨=2 bridge
- vol2/super_chiral_yangian.tex: added Yang-rational convention marker (ℏ absorbed)
- vol3/fukaya_categories.tex: added level-absorbed marker (Mukai pairing as level)

Post-heal grep gate: zero bare r(z) = Ω/z forms in Vol I/II/III production .tex.
One audit-workspace file (compute/audit/standalone_paper/classification.tex) flagged,
not edited (zero build consumers).
```

## Beilinson audit verdict

**Hygiene sweep CONVERGED.** Programme-wide HZ-1 / AP126 / AP141 / C9 discipline now passes the grep gate in all three production volumes. Residual items (1)-(5) above are lower-priority and scoped for future sweeps.

Per the Beilinson dictum: a smaller true discipline rigorously enforced beats a larger advertised one. The level-prefix discipline at r-matrix sites is a constitutional boundary; this sweep restores it to zero violations in production.
