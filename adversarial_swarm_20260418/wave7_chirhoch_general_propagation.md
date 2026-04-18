# Wave-7 Propagation Heal: `prop:chirhoch2-affine-km-general` (2026-04-18)

## Mission

AP5/AP149/AP271 propagation of Wave-5 inscription of
`prop:chirhoch2-affine-km-general` at
`chapters/theory/chiral_center_theorem.tex:2221-2277`
(`\ClaimStatusProvedHere`), which upgrades
`dim ChirHoch^*(V_k(\fg)) = \dim(\fg) + 2`
from sl_2-witness-only to uniform across all simple \fg at generic
non-critical level.

## Step 1: Inscription verification — CONFIRMED

- Location: `chapters/theory/chiral_center_theorem.tex:2221`.
- Tag: `\ClaimStatusProvedHere`.
- Full proof body (lines 2233-2277) composes:
  (i) `thm:hochschild-polynomial-growth` (Theorem H, degree-\{0,1,2\} concentration)
  (ii) Koszul-duality identity `dim ChirHoch^2(A) = dim Z(A^!)`
       (at `subsec:chiral-hoch-cochain`, fiber-center description)
  (iii) `prop:chirhoch1-affine-km` (ChirHoch^1(V_k(\fg)) = \fg)
  (iv) chiral Feigin-Frenkel self-duality V_k(\fg)^! = V_{-k-2h^v}(\fg)
  (v) scalar Feigin-Frenkel center at non-critical dual level
      (Z polynomial only AT critical level k = -h^v; scalar off it).
- Falsification remark: `rem:chirhoch2-affine-km-general-falsification`
  (line 2279-2294) recommends extending
  `compute/lib/derived_center_explicit.py` to check
  `dim Z(V_{-k-2h^v}(\fg)) = 1` for sl_3, sl_4 at small integer k
  as an independent numerical triangulation path.

## Step 2: Consumer enumeration (live .tex only, all three volumes)

Grep pattern: `\ref{prop:chirhoch1-affine-km}|\ref{rem:sl2-chirhoch-dim5}|\ref{prop:chirhoch2-affine-km-general}`.

### Vol I (11 live sites, SOUND)

| file:line | ref | prose context | action |
|-----------|-----|---------------|--------|
| chapters/theory/chiral_center_theorem.tex:2218 | chirhoch2-affine-km-general | `rem:sl2-chirhoch-dim5` points forward to uniform witness | none (home of proposition) |
| chapters/theory/chiral_center_theorem.tex:2265 | chirhoch1-affine-km | proof body step (iii) | none |
| chapters/theory/chiral_center_theorem.tex:2288 | chirhoch2-affine-km-general | falsification-remark forward-ref | none |
| chapters/theory/chiral_center_theorem.tex:2313 | chirhoch1-affine-km | `prop:gerstenhaber-sl2-bracket` consumer | none |
| chapters/theory/chiral_center_theorem.tex:2441 | chirhoch1-affine-km | consumer (gerstenhaber general-g) | none |
| chapters/theory/chiral_center_theorem.tex:2519 | chirhoch1-affine-km | consumer | none |
| chapters/theory/chiral_hochschild_koszul.tex:1132 | chirhoch1-affine-km | sl_2 corollary (1,3,1) with Koszul duality dim^2 = dim Z(A^!) | none — already cites general identity |
| chapters/theory/three_hochschild_unification_platonic.tex:477 | chirhoch1-affine-km | unification consumer | none |
| chapters/theory/chiral_climax_platonic.tex:948 | chirhoch1-affine-km | Climax theorem: `dim ChirHoch^*(V_k(\fg)) = dim(\fg)+2` | already uniform statement |
| chapters/frame/preface.tex:1690 | chirhoch1-affine-km | preface Theorem H summary | already `P_{V_k(\fg)}(t) = 1 + (dim\fg)t + t^2` uniform |
| chapters/frame/preface.tex:3987 | chirhoch1-affine-km | preface Hilbert polynomial table | already uniform |
| chapters/examples/kac_moody.tex:115,:5267 | chirhoch1-affine-km | KM chapter summary + cross-ref | none |
| chapters/connections/concordance.tex:81,402,414,4833,7237-7239,9824 | chirhoch1-affine-km | concordance entries | none — concordance already states uniform `dim(\fg)+2` indirectly via Theorem H |

### Vol II (0 live `.tex` sites; only .md session artifacts)

Grep confirmed zero matches in `~/chiral-bar-cobar-vol2/**/*.tex`.

### Vol III (0 live `.tex` sites)

Grep confirmed zero matches.

## Step 3: AP5 propagation verdict

The manuscript prose was ALREADY AHEAD of the Wave-4 `prop:chirhoch2-affine-km-general` inscription. Specifically:

- The Climax theorem (`chiral_climax_platonic.tex:946-947`) already stated
  `\dim\ChirHoch^*(V_k(\fg)) = \dim(\fg)+2` as the uniform fingerprint
  for affine Kac-Moody, citing `prop:chirhoch1-affine-km` with the
  understanding that `\dim^0 = \dim^2 = 1` was inherited from Theorem H.
- The preface (`preface.tex:3987-3992`) already tabulated the uniform
  Hilbert polynomial `P_{V_k(\fg)}(t) = 1 + (\dim\fg)t + t^2`
  (sibling to Heisenberg `1 + t + t^2` and Virasoro `1 + t^2`).
- The concordance (`concordance.tex:399-414`) already listed the uniform
  concentration with Theorem H + `prop:chirhoch1-affine-km`.
- The sl_2 corollary (`chiral_hochschild_koszul.tex:1122-1146`) already
  factored the proof as Whitehead + Koszul duality
  `dim ChirHoch^2 = dim Z(V_{k'}(\fg))`.

The Wave-4 inscription formalized the Koszul-duality + Feigin-Frenkel
center step into a dedicated proposition, closing the AP271 gap where
the CLAUDE.md status row asserted "total-dim formula sl_2 only" while
the preface / climax / concordance prose already read the uniform
statement. No prose edits required in live .tex.

## Step 4: CLAUDE.md update — COMPLETED

The CLAUDE.md Theorem Status row for `ChirHoch^1 KM` was ALREADY
upgraded in the working copy at line 590: it now reads
"PROVED at generic k for general simple g: ChirHoch^1(V_k(g)) = g
and dim ChirHoch^*(V_k(g)) = dim(g) + 2" with explicit citation to
both `prop:chirhoch1-affine-km` and `prop:chirhoch2-affine-km-general`.
The row also flags a candidate `rank(\fg) + dim(\fg) + 1` formula as
REFUTED (would require `\dim \ChirHoch^0` to scale with rank, which
contradicts scalar vacuum center at generic k) — this is a correct
AP-style false-lemma registration.

The quoted "FROM" text in the mission brief corresponds to a stale
local snapshot; the working-copy row was already rewritten.

No additional CLAUDE.md edits needed.

## Step 5: Engine update — COMPLETED (minimal)

`compute/lib/chirhoch_dimension_engine.py::chirhoch_affine_km(lie_algebra)`
was already uniform across simple types: `dim2=1` hard-coded with
[SY] Koszul-duality VERIFICATION comment; `dim1=dim_g`; `total=dim_g+2`.
Test harness (line 522-534) iterates over sl_2, sl_3, sl_4, G_2, E_8.

Added citation to `prop:chirhoch2-affine-km-general` in the `dim2=1`
VERIFIED comment block (lines 291-296 in patched file) recording the
manuscript inscription location and the Feigin-Frenkel self-duality
mechanism.

Predicted totals (from engine output):
- sl_2: 3 + 2 = 5
- sl_3: 8 + 2 = 10
- sl_4: 15 + 2 = 17
- sl_5: 24 + 2 = 26
- G_2: 14 + 2 = 16
- F_4: 52 + 2 = 54
- E_6: 78 + 2 = 80
- E_7: 133 + 2 = 135
- E_8: 248 + 2 = 250

## Step 6: AP register

- AP271 (reverse drift): a prior snapshot of the CLAUDE.md row asserted
  "sl_2 only" while the manuscript (preface, climax, concordance)
  already stated the uniform formula. The working-copy row is already
  corrected. Register: AP271 symptom was the stale snapshot, not the
  current CLAUDE.md.
- AP5 (cross-volume propagation): zero cross-volume consumers in Vol II
  or Vol III. Vol I consumers already sound.
- AP149 (resolution propagation): propagation complete at Wave-4; Wave-7
  is verification-only.

## Commit plan

None. This note is a verification + minor-patch report:
- 1 engine comment line added (verification-trail enhancement).
- 0 `.tex` edits.
- 0 CLAUDE.md edits (status row already correct as of Wave-4).
- 1 new `.md` (this note).

Author: Raeez Lorgat. No AI attribution.

## Residual items

1. **Engine triangulation (optional)**: extend `derived_center_explicit.py`
   to compute `Z(V_{-k-2h^v}(\fg))` via Kac-Shapovalov determinant for
   sl_3, sl_4 at small integer k ∈ {1, 2, 3}, per the falsification
   remark. This converts the proposition from "proved via general
   Koszul-duality machinery" to "proved with independent per-family
   numerical witness" (HZ-IV upgrade, not a closure requirement).

2. **`compute/lib/chirhoch_dimension_engine.py` predicted totals table**:
   consider adding an explicit test that iterates `chirhoch_affine_km`
   over simple types and verifies `total = dim_g + 2`, citing
   `prop:chirhoch2-affine-km-general` in the test docstring. Current
   test harness at line 522-534 exercises the engine but does not
   explicitly assert the uniform `dim(\fg)+2` pattern as a cross-type
   invariant.
