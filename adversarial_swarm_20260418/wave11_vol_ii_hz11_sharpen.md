# Wave-11 Vol~II HZ-11 attribution sharpening

Targeted-heal for two consumer classes identified by Wave-10 Tier-1 phantom
heal agent `ab2835b2`. Objective: convert five bare `\ref{prop:standard-strong-filtration}`
consumer sites in Vol~II into HZ-11-compliant cross-volume attributions, add
the required `V1-` phantomsection alias, and verify the Class~2
`rem:twining-genera` consumers already satisfy AP287 discipline.

## Canonical anchors (verified)

- Vol~I `chapters/theory/bar_cobar_adjunction_curved.tex:1115-1116`:
  `\begin{proposition}[Standard weight truncations and the induced bar filtration]`
  `\label{prop:standard-strong-filtration}`.
  Proposition covers `V_k(\fg)` (k != -h^v), `Vir_c`, `W^k(g, f_prin)`
  non-critical, `V_Lambda` positive-definite even lattice — matches Vol~II
  consumer usage (class-M weight-completed bar filtration).
- Vol~III `chapters/examples/k3e_cy3_programme.tex:583`:
  `\label{rem:twining-genera}`. Frame-shape table of M_24 with twining genera.

## Class 1: `prop:standard-strong-filtration` (5 consumers)

Pre-heal state: 5 bare `\ref{prop:standard-strong-filtration}` in Vol~II with
no `V1-` alias in `vol2/main.tex`; all five rendered `[?]` at build (no label
resolution path in Vol~II).

Sites (actual paths — note: the spec gave `chapters/connections/` for
`curved_dunn_raw_direct_sum_platonic.tex` but the file lives at
`chapters/theory/`):

1. `vol2/chapters/theory/curved_dunn_raw_direct_sum_platonic.tex:70`
2. `vol2/chapters/theory/curved_dunn_raw_direct_sum_platonic.tex:245`
3. `vol2/chapters/connections/bv_brst.tex:2344` (already had
   `\textup{(}Volume~I\textup{)}` prose prefix from Wave-10, but bare label)
4. `vol2/chapters/connections/bv_brst.tex:2363`
5. `vol2/chapters/connections/bv_brst.tex:2424`

### Heal

1. Added phantomsection alias at `vol2/main.tex:886` in alphabetical position
   (between `V1-prop:standard-examples-modular-koszul` and
   `V1-prop:swiss-cheese-nonformality-by-class`):
   `\phantomsection\label{V1-prop:standard-strong-filtration}%`.
2. Rewrote all five consumer refs to `\ref{V1-prop:standard-strong-filtration}`
   with explicit `Volume~I` / `Vol~I` prose prefix matching the
   `bv_brst.tex:2344` Wave-10 template (`\textup{(}Volume~I\textup{)}`).
3. Also sharpened the companion Theorem ref at
   `curved_dunn_raw_direct_sum_platonic.tex:69`
   (`thm:completed-bar-cobar-strong` -> `V1-thm:completed-bar-cobar-strong`)
   since it lives in the same parenthetical and the `V1-` alias for that
   theorem already exists at `main.tex:945`.

### Post-heal verification

- `grep '\\ref{prop:standard-strong-filtration}' vol2/` -> zero hits.
- `grep '\\ref{V1-prop:standard-strong-filtration}' vol2/` -> 5 hits matching
  the five healed sites.
- Alias `V1-prop:standard-strong-filtration` present in `vol2/main.tex:886`.

All five sites now carry (a) the `V1-` label form to resolve via phantomsection
alias, (b) explicit `Volume~I` / `Vol~I` prose prefix per HZ-11 attribution
discipline. Consistent with the existing Wave-10 template at `bv_brst.tex:2344`
and with the existing `V1-thm:completed-bar-cobar-strong` usage pattern
elsewhere in Vol~II (`thqg_gravitational_yangian.tex:2791`,
`thqg_holographic_reconstruction.tex:1490`, etc.).

## Class 2: `rem:twining-genera` (5 consumers)

Pre-heal state: `rem:twining-genera` phantomsection alias ALREADY EXISTS at
`vol2/main.tex:1028-1029` (Wave-10 inscribed, as the companion comment at
main.tex:1024-1027 documents: "Cross-volume (Vol~III) HZ-11 aliases (AP287
attribution)"). Consumer sites:

1. `vol2/chapters/connections/celestial_moonshine_bridge.tex:270` — carries
   `Vol~III` prose prefix on line 269.
2. `vol2/chapters/connections/celestial_moonshine_bridge.tex:304` — carries
   `Vol~III` prose prefix on line 303.
3. `vol2/chapters/connections/celestial_moonshine_bridge.tex:392` — carries
   `Vol~III` prose prefix on line 391.
4. `vol2/chapters/connections/celestial_moonshine_bridge.tex:482` — full
   canonical form `Vol~III Remark~\ref{rem:twining-genera}`.
5. `vol2/chapters/connections/celestial_moonshine_bridge.tex:527` — carries
   `Vol~III` prose prefix on line 526.

All five consumer sites ALREADY carry explicit `Vol~III` prose prefix in
surrounding prose, satisfying AP287 HZ-11 attribution discipline. Alias
resolves. NO EDITS NEEDED for Class 2.

## Residual observations (not healed this pass)

- The Class 1 consumer note at `bv_brst.tex:2344` used `\textup{(}Volume~I\textup{)}`
  prose prefix with bare label before this heal; the asymmetry with the 2363
  and 2424 bare refs in the same file reflected the Wave-10 heal being scoped
  narrowly to the first-occurrence sentence. This Wave-11 pass unifies all
  three `bv_brst.tex` sites + the two `curved_dunn_raw` sites under the same
  `V1-` label + Vol~I prose prefix template.
- No new `\label{rem:twining-genera}`-class labels were introduced; the
  Wave-10 alias block at `main.tex:1024-1029` continues to carry AP287 comment
  documenting the cross-volume attribution convention.

## Phantom refs and aliases (summary)

| label | canonical home | alias in vol2/main.tex | consumer count |
|-------|----------------|------------------------|----------------|
| `prop:standard-strong-filtration` | Vol~I `bar_cobar_adjunction_curved.tex:1116` | `V1-prop:standard-strong-filtration` at `main.tex:886` (added this pass) | 5 (all sharpened) |
| `rem:twining-genera` | Vol~III `k3e_cy3_programme.tex:583` | `rem:twining-genera` (unprefixed) at `main.tex:1029` (Wave-10) | 5 (all already attribute) |

## Commit plan

- Files modified this pass (6 edits across 3 files, 1 alias addition):
  - `vol2/main.tex` — +1 phantomsection alias at line 886.
  - `vol2/chapters/theory/curved_dunn_raw_direct_sum_platonic.tex` — 2 ref
    sharpens (lines 69-70 and 244-246 blocks).
  - `vol2/chapters/connections/bv_brst.tex` — 3 ref sharpens (lines 2344, 2363,
    2424).
- No commit yet; await build + test verification per session protocol.
- Commit message draft (single logical change):
  `Vol~II Wave-11 HZ-11 sharpen: prop:standard-strong-filtration cross-vol`
  `attribution — add V1- phantomsection alias to vol2/main.tex:886;`
  `convert 5 bare \ref{} consumer sites to V1-prop:standard-strong-filtration`
  `with Volume~I prose prefix (curved_dunn_raw_direct_sum_platonic.tex:70,245;`
  `bv_brst.tex:2344,2363,2424). Class 2 rem:twining-genera consumers already`
  `satisfy AP287 via existing Wave-10 alias + Vol~III prose prefix.`
