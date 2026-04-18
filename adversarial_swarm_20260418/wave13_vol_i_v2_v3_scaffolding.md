# Wave-13 Vol I V2/V3 cross-volume phantomsection scaffolding

Date: 2026-04-18
AP lineage: AP253 continuation (Wave-12 a8fe4088 flagged Vol I V2/V3 scaffolding thin vs Vol II's ~476).
Discipline: PE-7 (label uniqueness) + PE-8 (cross-volume) + AP149/AP286/AP287 (HZ-11).

## Mission

Restore reciprocal V2-*/V3-* phantomsection alias symmetry in Vol I `main.tex`. Vol II/III
already carry extensive `\phantomsection\label{V1-*}` blocks so Vol II/III chapters can
`\ref{V1-thm:X}` unresolved at Vol I inscription; Vol I's counterpart infrastructure was
only 2 aliases. Mission: enumerate actual V2-*/V3- consumers in Vol I, verify each target
exists in its home volume, add alias for any gap, record status.

## Consumer enumeration (Vol I → V2/V3)

### V2- consumers (build-critical, i.e. `\ref{V2-...}` or `\ref*{V2-...}`)

Raw grep `\\ref\{V2-\|\\ref\*\{V2-` across `chapters/`, `standalone/`, `appendices/`,
`main.tex`:

| Label | Sites | Home |
| --- | --- | --- |
| `V2-thm:uch-main` | preface.tex:1715; part_iv:555 (\texttt, informational) | Vol II `chapters/connections/universal_celestial_holography.tex` |
| `V2-thm:chiral-higher-deligne` | preface.tex:1716 | Vol II `chapters/theory/chiral_higher_deligne.tex` |
| `V2-prop:modular-bootstrap-to-curved-dunn-bridge` | higher_genus_complementarity.tex:5115, 5156 | Vol II `chapters/theory/curved_dunn_higher_genus.tex:138` |
| `V2-rem:platonic-shadow-dichotomy` | concordance.tex:2840 | Vol II `chapters/examples/examples-worked.tex` |
| `V2-thm:gravitational-primitivity` | concordance.tex:2863 | Vol II `chapters/connections/3d_gravity.tex` |
| `V2-thm:iterated-sugawara-construction` | part_iv:268, 652 (\texttt, informational) | Vol II `chapters/connections/e_infinity_topologization.tex` |
| `V2-thm:e-infinity-topologization-ladder` | part_iv:651 (\texttt, informational) | Vol II `chapters/connections/e_infinity_topologization.tex` |
| `V2-conj:uch-gravity-chain-level` | part_iv:556 (\texttt, informational) | Vol II `main.tex` |

### V3- consumers

| Label | Sites | Home |
| --- | --- | --- |
| `V3-cor:class-m-higher-genus` | preface.tex:5082; programme_overview_platonic.tex:399 | Vol III `chapters/theory/en_factorization.tex` |

## Pre-heal alias count in Vol I main.tex

Grep `phantomsection.label{V[23]-` in `/Users/raeez/chiral-bar-cobar/main.tex`:
- `V2-thm:gravitational-primitivity` (line 2200)
- `V2-prop:modular-bootstrap-to-curved-dunn-bridge` (line 2201, HZ-11 heal 2026-04-17)

Total: 2.

## Missing-alias table (target verified in home volume)

| Alias | Target exists | Added |
| --- | --- | --- |
| `V2-thm:uch-main` | Y (Vol II universal_celestial_holography.tex) | Y |
| `V2-thm:chiral-higher-deligne` | Y (Vol II chiral_higher_deligne.tex) | Y |
| `V2-rem:platonic-shadow-dichotomy` | Y (Vol II examples-worked.tex) | Y |
| `V2-thm:iterated-sugawara-construction` | Y (Vol II e_infinity_topologization.tex) | Y |
| `V2-thm:e-infinity-topologization-ladder` | Y (Vol II e_infinity_topologization.tex) | Y |
| `V2-conj:uch-gravity-chain-level` | Y (Vol II main.tex) | Y |
| `V3-cor:class-m-higher-genus` | Y (Vol III en_factorization.tex) | Y |

All 7 targets independently verified with `grep '\\label{...}'` in their home volume. No
phantom targets; no AP255 (phantom-file) risk; AP264 (phantom-ref-to-nonexistent-label)
does not apply.

## Edit applied

`main.tex:2201` → inserted 7 lines after the existing HZ-11 heal entry (see block below,
alphabetical within V2-*, then V3-*, matching the Vol II convention):

```
 \phantomsection\label{V2-thm:gravitational-primitivity}% % Vol II 3d_gravity.tex
 \phantomsection\label{V2-prop:modular-bootstrap-to-curved-dunn-bridge}% % Vol II curved_dunn_higher_genus.tex:138 (HZ-11 heal 2026-04-17)
 % --- Wave-13 cross-volume scaffolding heal (2026-04-18, AP253 continuation) ---
 \phantomsection\label{V2-conj:uch-gravity-chain-level}%
 \phantomsection\label{V2-rem:platonic-shadow-dichotomy}%
 \phantomsection\label{V2-thm:chiral-higher-deligne}%
 \phantomsection\label{V2-thm:e-infinity-topologization-ladder}%
 \phantomsection\label{V2-thm:iterated-sugawara-construction}%
 \phantomsection\label{V2-thm:uch-main}%
 \phantomsection\label{V3-cor:class-m-higher-genus}%
\fi
```

Post-heal alias count: 9 (2 existing + 7 new).

## Resolution verification

The 4 build-critical `\ref{V2-...}` / `\ref*{V2-...}` sites (preface.tex:1715, :1716;
higher_genus_complementarity.tex:5115, :5156; concordance.tex:2840, :2863) now each
resolve to an inscribed `\phantomsection\label{...}` anchor within the same volume.
The 5 `\texttt{V2-...}` and `\texttt{V3-...}` sites in part_iv_platonic_introduction.tex
and programme_overview_platonic.tex are informational (typewriter-set label strings in
prose); they do not trigger `\ref` resolution but the aliases are now available should
a future pass upgrade the `\texttt` to `\ref*`.

`main.tex:5082` uses `\ref{V3-cor:class-m-higher-genus}` within a preface sentence; the
new phantomsection anchor eliminates the `[?]` marker the build would previously have
emitted.

Build not triggered this session (mission brief: no commits). A full build pass should
be run prior to any commit touching `main.tex` per the PRE-COMMIT hook.

## Discipline notes

AP286 (tactical phantomsection alias vs semantic heal). These aliases are TACTICAL —
they resolve `\ref{}` without inscribing the cited content in Vol I. This is the correct
disposition for cross-volume refs: the Vol II / Vol III theorem is the canonical
home; Vol I prose only needs the label to resolve for build hygiene. HZ-11 semantic
discipline applies at the CONSUMER side (every `ProvedHere` theorem whose proof invokes
a cross-volume lemma must carry `\ClaimStatusConditional` + `\begin{remark}[Attribution]`).
The phantomsection aliases here do NOT promote any Vol I theorem's scope; they only
repair the LaTeX-level `\ref` resolution.

AP287 (cross-volume theorem existence without HZ-11 attribution) check: inspected the
four build-critical `\ref{V2-...}` consumer sites:
- `preface.tex:1715-1716` — prose citation of Vol II theorems as context; no Vol I
  `\ClaimStatusProvedHere` theorem rides on this. No violation.
- `higher_genus_complementarity.tex:5115, 5156` — already documented HZ-11 heal
  2026-04-17 (clause (iv) downgraded to `\ClaimStatusConditional`). Compliant.
- `concordance.tex:2840, 2863` — concordance is a meta-narrative chapter (constitutional
  document, not a theorem vehicle). No theorem scope at risk. No violation.

## Commit plan (for future session, per PRE-COMMIT hook)

1. `pkill -9 -f pdflatex; sleep 2; make fast` — verify Vol I builds clean with new aliases.
2. `make test` — sanity check (test suite should be unaffected by build-only LaTeX label edits).
3. `git diff main.tex` — confirm only the targeted 8 lines (one comment + seven aliases)
   were added.
4. Commit message: "Vol I main.tex V2/V3 phantomsection scaffolding: seven aliases added
   (AP253 continuation / Wave-13), reciprocal parity with Vol II V1-* infrastructure,
   four build-critical `\ref{V2-*}` sites + one `\ref{V3-*}` site now resolve." Authored
   by Raeez Lorgat only; no AI attribution.

## Residual

The Wave-12 report claimed Vol II has 476 V1-* aliases. Vol I's corresponding consumer
surface is much smaller (9 distinct cross-volume labels, 7 newly aliased). The asymmetry
mostly reflects asymmetric consumption rather than asymmetric infrastructure: Vol II
foundations cite Vol I heavily (many V1-* consumers); Vol I prose cites Vol II/III
sparingly (few V2-*/V3- consumers). The Wave-13 heal brings Vol I to parity with its
actual consumer surface; no further scaffolding is warranted until new consumers
surface.

If a future wave adds new `\ref{V2-...}` or `\ref{V3-...}` in a Vol I chapter, the
template for registration is:
```
\phantomsection\label{V[23]-<prefix>:<name>}% % Vol <vol> <source_chapter>.tex[:<line>]
```
inserted in the Wave-13 block at `main.tex:2202-2210`, alphabetical within the V-suffix
group.
