# Wave-9 build-log undefined-reference scan — BUILD-INFRASTRUCTURE FAILURE

Date: 2026-04-18. Diagnostic-only (no edits, no commits). Mission: run `make fast` per volume, extract `LaTeX Warning: Reference ... undefined` counts from build logs, cross-check against Wave-7 AP255 phantom-detector output.

## Status: BUILD-LOG ORACLE UNAVAILABLE — FALLBACK TO METADATA CROSS-REFERENCE

## Build-failure mode (all three volumes)

```
$ which pdflatex latex xelatex lualatex tlmgr
pdflatex not found
latex not found
xelatex not found
lualatex not found
tlmgr not found

$ ls /usr/local/texlive/ /Library/TeX/
(both absent — nothing)
```

PATH contains `/Library/TeX/texbin` (Homebrew/MacTeX default), but the target directory `/Library/TeX/` does NOT exist on this machine. MacTeX / TeX Live is NOT installed. No `pdflatex` binary is available anywhere on PATH or at standard locations (`/usr/local/texlive/*`, `/opt/homebrew/bin/pdflatex`, `/Library/TeX/`).

Consequently the authoritative build-log oracle requested by Wave-7 detection-gap correction (`make fast 2>&1 | grep "LaTeX Warning: Reference.*undefined"`) **cannot be executed on this harness**. All three volumes (`chiral-bar-cobar`, `chiral-bar-cobar-vol2`, `calabi-yau-quantum-groups`) share the same machine and would fail identically at `make fast` on first `pdflatex main.tex`.

Recovery advice per CLAUDE.md "Build" section: `pkill -9 -f pdflatex; sleep 2; make fast` is moot without a TeX installation; the user must first install MacTeX (`brew install --cask mactex-no-gui` or the full MacTeX installer) or TeX Live (`brew install texlive`). The `pkill` step is defensive against watcher-spawned competing `pdflatex` processes and is irrelevant when no binary exists.

## Fallback: cross-reference Wave-7 phantom-detector data (Vol I only has metadata)

Per mission step 7, falling back to Wave-7 data at `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/wave7_phantom_detector_rerun.md`. Vol II and Vol III lack `metadata/label_index.json`, so their phantom counts come from env-scan alone, not from build-log oracle.

### Per-volume phantom-ref counts (Wave-7 env-scan + live-tex filter)

| Volume | phantomsection labels | False-positives (Wave-7 corrected) | Genuine phantoms | Load-bearing (live-tex consumers) | Orphan |
|---|---|---|---|---|---|
| Vol I    | 357  | 251 | 106 | 76  | 30  |
| Vol II   | 599  | 6   | 593 | 270 | 323 |
| Vol III  | 60   | 0   | 60  | 51  | 9   |
| **Total**| **1016** | **257** | **759** | **397** | **362** |

The 397 load-bearing figure is the expected lower bound for `LaTeX Warning: Reference ... undefined` counts once a build is possible. Actual build-log counts will typically be HIGHER because (a) some labels defined in standalone `.tex` files not `\input`-ed into `main.tex` render `[?]` at build despite env-scan finding them (AP255 phantom-file-in-consumers, e.g. `thm:chiral-qg-equiv`), (b) forward-reference lemmas (AP242) render `[?]` on first pass and resolve only after a second `pdflatex`, and (c) bibkey phantoms (AP264/AP281) are NOT counted in these 397 but do appear as `Citation ... undefined` warnings (Vol I ~621 phantom cites at audit time per AP281).

### Top-20 live-tex phantom consumers (from Wave-7 rerun table)

| rank | label | vol | live refs | tier |
|---|---|---|---|---|
| 1 | `conj:master-bv-brst` | I | **86** | Tier-1 load-bearing |
| 2 | `V1-rem:sc-higher-genus` | II | 16 | AP291 candidate |
| 3 | `def:thqg-holographic-datum` | I | 14 | Tier-1 |
| 4 | `thm:complementarity` | I | 14 | Tier-1 |
| 5 | `V1-lem:degree-cutoff` | II | 12 | AP291 candidate |
| 6 | `chap:toroidal-elliptic` | I | 12 | chapter-head inscribe |
| 7 | `prop:vir-all-mk` | II | 11 | |
| 8 | `thm:topologization-tower` | I | 10 | AP286 alias tension |
| 9 | `thm:quantum-complementarity-main` | II | 10 | |
| 10 | `ch:k3-times-e` | III | 19 | chapter-head inscribe |
| 11 | `V1-thm:recursive-existence` | II | 9 | |
| 12 | `thm:bar-cobar-isomorphism-main` | II | 9 | |
| 13 | `thm:e-infinity-specialisation-Winfty` | II | 9 | |
| 14 | `thm:genus-universality` | II | 9 | |
| 15 | `ch:kontsevich-integral` | I | 8 | |
| 16 | `chap:infinite-fingerprint-classification` | I | 8 | |
| 17 | `conj:master-infinite-generator` | I | 8 | |
| 18 | `thm:delta-f-cross-w3-g2` | I | 8 | |
| 19 | `thm:derived-additive-kz` | I | 8 | |
| 20 | `thm:elliptic-vs-rational` | I | 8 | |

Cross-match to Wave-7 top-20: **identical** (this IS Wave-7's top-20, reproduced from the rerun). A build-log comparison would test whether build `[?]` renders match these rankings; that comparison is deferred to a session with a working TeX install.

### Tier-1 ABSENT-register (13 genuine phantoms, all Vol I)

From Wave-7 Tier-1 table: `thm:chiral-qg-equiv-elliptic`, `thm:chiral-qg-equiv-toroidal-formal-disk`, `thm:chiral-qg-equiv-ordered`, `def:ordered-koszul-chiral-algebra`, `prop:yangian-ordered-koszul`, `prop:sl2-yangian-triangle-concrete`, `thm:w-infty-chiral-qg-completed`, `prop:e3-gl-N`, `thm:e3-identification-semisimple` / `-reductive` / `-solvable`, `prop:e3-heisenberg`, `thm:grt1-rigidity`. All would render `[?]` at build. Healing options per AP255/AP286: (a) inscribe locally in a chapter, (b) retire the advertised name and retarget consumers to the nearest canonical label.

## Recommended Wave-9+ heal priorities per volume

**Vol I** — 76 load-bearing live-tex consumers. Top-5 heal priorities:
1. `conj:master-bv-brst` (86 refs) — inscribe as master conjecture in `bv_brst.tex` or retarget to `thm:bv-bar-coderived` (Vol II) with AP287 attribution discipline.
2. `thm:complementarity` (14 refs) — disambiguate against `thm:quantum-complementarity-main` (Vol II rank 9); retarget or inscribe locally.
3. `def:thqg-holographic-datum` (14 refs) — inscribe in 3d HT holography chapter head.
4. `chap:toroidal-elliptic` (12 refs) — chapter-head `\chapter{}\label{}` inscribe.
5. `thm:topologization-tower` (10 refs) — AP286 semantic heal tension: currently `\phantomsection` alias at `preface.tex:5084` to Vol II `thm:iterated-sugawara-construction` + `thm:e-infinity-topologization-ladder`; prose treats as umbrella, alias covers only one. Inscribe an umbrella theorem in Vol I OR retarget each ref to the specific Vol II theorem it cites.

**Vol II** — 270 load-bearing live-tex consumers (highest by a factor of 3-4x). Priority investigation: `V1-rem:sc-higher-genus` (16 refs) and `V1-lem:degree-cutoff` (12 refs) — AP291 self-disabled-label or AP287 genuine cross-volume; verify via `% label removed:` grep per AP291 protocol. Vol II lacks `metadata/label_index.json`; building one is the single highest-leverage infrastructure improvement (supports every future AP255/AP291 audit).

**Vol III** — 51 load-bearing live-tex consumers, least debt. Priority: `ch:k3-times-e` (19 refs) — single chapter-head `\chapter{}\label{ch:k3-times-e}` inscription resolves all 19 consumers atomically.

## Follow-on actions

1. **Install TeX** — this machine needs MacTeX/TeX Live for any build-log oracle. Without it, the build-gate commit discipline (CLAUDE.md §Build + PreToolUse hook "build passes") cannot be satisfied.
2. **Build Vol II and Vol III `metadata/label_index.json`** via `scripts/generate_metadata.py` equivalent — Vol I has one (11139 entries); Vol II/III's absence forces expensive whole-directory grep for every phantom audit.
3. **Wave-9 phantom-detector re-run with build-log oracle** once TeX is installed — the per-volume build log gives ground-truth undefined-reference counts that triangulate against Wave-7 env-scan + live-tex-filter figures. Expected agreement within 10-20% (discrepancies come from AP242 forward-references resolving on second pass and standalone-only labels not reached by `main.tex` input chain).
4. **Canonical phantom registry at `notes/phantom_registry.md`** per Wave-7 recommendation 5 — durable cross-session artifact replacing one-shot diagnostic notes.

## Summary

Build-log oracle step (1-5) **NOT EXECUTED**: no TeX installation. Wave-7 phantom-detector data (759 genuine phantoms programme-wide, 397 load-bearing live-tex, 362 orphan; Vol I 76 / Vol II 270 / Vol III 51) stands as the best available proxy. Top-20 cross-match against build-log oracle is pending a TeX installation. No new APs surfaced by this diagnostic.
