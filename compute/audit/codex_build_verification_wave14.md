# Build Verification Wave 14

Date: 2026-04-09
Author: Codex
Scope: build verification only; no `.tex` files modified; no commits made.

## Method

I ran the user-specified build commands serially, in order.

Exact commands requested:

1. Vol I: `pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast 2>&1 | tail -300`
2. Vol II: `cd /Users/raeez/chiral-bar-cobar-vol2 && make 2>&1 | tail -300`
3. Vol III: `cd /Users/raeez/calabi-yau-quantum-groups && make fast 2>&1 | tail -300`

Important environment note:

- The sandbox for this session is writable in `/Users/raeez/chiral-bar-cobar` and `/tmp`, but not in the Vol II and Vol III source trees.
- As a result, the exact Vol II and Vol III commands did not produce trustworthy fresh builds in-place.
- To complete the verification contract anyway, I copied those trees to `/tmp` and reran the same build target there on identical source snapshots:
  - Vol II snapshot: `/tmp/codex_vol2_snapshot.WyzZkb`
  - Vol III snapshot: `/tmp/codex_vol3_snapshot.Hxx31G`

I therefore report both:

- the exact-command exit code in the original directory, and
- the fresh snapshot-build result used for actual TeX diagnostics.

Severity convention used below:

- `CRITICAL`: exact requested build path did not yield a fresh verified PDF.
- `MODERATE`: PDF built, but unresolved references/citations or multiply-defined labels remain.
- `MINOR`: box warnings or destination warnings.

Counting convention:

- `CRITICAL` counts are issue-cluster counts.
- `MODERATE` counts use unique unresolved keys/labels plus explicit duplicate-label keys found by aux analysis.
- `MINOR` counts use warning-line counts (`Overfull`, `Underfull`, `pdfTeX warning (dest)`).

## Executive Table

| Volume | Exact Command Exit | Fresh Verification Build | Fresh PDF Verified | CRITICAL | MODERATE | MINOR |
|---|---:|---:|---|---:|---:|---:|
| Vol I | `0` | exact command | yes: `/Users/raeez/chiral-bar-cobar/main.pdf` | 0 | 43 | 502 |
| Vol II | `2` | snapshot `make` exit `0` | yes: `/tmp/codex_vol2_snapshot.WyzZkb/main.pdf` | 1 | 81 | 384 |
| Vol III | exact command never terminated cleanly; interrupted after lock wait, process exit `1` | snapshot `make fast` exit `0` | yes: `/tmp/codex_vol3_snapshot.Hxx31G/main.pdf` | 1 | 42 | 46 |

## Volume I

### Command result

- Exact command exit: `0`
- Build target: `make fast`
- Verified PDF:
  - `/Users/raeez/chiral-bar-cobar/main.pdf`
  - mtime: `2026-04-09 23:14:13`

### Fresh-build summary

- Fatal TeX lines `^! `: `0`
- Undefined references: `85` occurrences, `36` unique keys
- Undefined citations: `5` occurrences, `5` unique keys
- Multiply-defined labels:
  - log summary present
  - aux-level duplicate keys found: `2`
- Overfull `\hbox`: `157`
- Underfull `\hbox`/`\vbox`: `343`
- `pdfTeX warning (dest)`: `2`

No actual TeX fatal error was present. There is one bare `!` line at `main.log:4070`, but not a `! <message>` error line and not build-fatal.

### Findings

#### MODERATE 1: Annals build omits archive-only chapters, leaving unresolved forward references in annals-visible prose

Evidence:

- `main.tex:142` sets `\annalseditiontrue` by default.
- `make fast` therefore compiles the Annals surface, not the archive surface.
- Archive-only chapters are gated behind `\ifannalsedition\else` blocks, but many annals-visible chapters still reference their labels.
- Representative unresolved keys:
  - `thm:family-index` (`17` occurrences)
  - `ch:holographic-datum-master` (`5`)
  - `ch:derived-langlands` (`4`)
  - `thm:baxter-exact-triangles` (`7`)
  - `thm:pro-weyl-recovery` (`8`)
  - `ch:genus1-seven-faces` (`2`)
  - `ch:landscape-census` (`1`)
  - `thm:yangian-shadow-theorem` (`1`)
  - `cor:thqg-I-heisenberg-selberg` (`1`)
  - `thm:oper-bar-dl` (`1`)

Wave attribution hypothesis:

- Most likely Wave `10` opening/overview rewrites and Wave `5-3` Overture expansion in annals-visible chapters, because the unresolved keys are largely forward references from early theory/frame text into archive-only bridge/frontier chapters.
- This is configuration-sensitive rather than a pure label-deletion bug: the same source would likely resolve in the archive build.

Concrete fix:

- Add Annals-safe phantom aliases for every archive-only label still referenced by annals-visible text, especially `thm:family-index`, `ch:holographic-datum-master`, `ch:derived-langlands`, `ch:genus1-seven-faces`, `ch:landscape-census`, `thm:yangian-shadow-theorem`, `cor:thqg-I-heisenberg-selberg`, and `thm:oper-bar-dl`.
- Alternatively, gate those references behind `\ifannalsedition\else` and replace them with plain text in the Annals build.

#### MODERATE 2: Five citation keys are used in the manuscript but absent from `bibliography/references.tex`

Evidence:

- Missing keys:
  - `EtingofKazhdan00`
  - `Mochizuki2015`
  - `Sabbah2014`
  - `Kausch2000`
  - `Polchinski1998`
- Citations occur in:
  - `chapters/theory/introduction.tex:1418`
  - `chapters/theory/chiral_koszul_pairs.tex:2486`
  - `chapters/examples/logarithmic_w_algebras.tex:234`
  - `chapters/connections/bv_brst.tex:835`
- `rg` found no corresponding `\bibitem{...}` entries in `bibliography/references.tex`.

Wave attribution hypothesis:

- Likely Wave `9-7` mega-sweep plus later extraction/expansion edits, because the missing keys sit in recently touched introduction/theory/bridge prose rather than in older stable bibliography lanes.

Concrete fix:

- Add those five `\bibitem` entries to `bibliography/references.tex`, using the existing bibliography style and key naming conventions already used in Vol I.

#### MODERATE 3: duplicate labels are present in `yangians_drinfeld_kohno.tex`

Evidence:

- `chapters/examples/yangians_drinfeld_kohno.tex:4100-4103` repeats labels verbatim:
  - `thm:yangian-dk5-spectral-factorization-seed-mono`
  - `thm:yangian-dk5-spectral-factorization-seed-trig`
- `main.aux` contains each of those keys twice.

Wave attribution hypothesis:

- Strongly suggests Wave `9-7` mega-sweep or a same-file extraction/rejoin, because the duplicates are literal consecutive repeats in one recently modified block rather than drift across distant files.

Concrete fix:

- Remove the duplicate `\label{...}` lines, keeping one canonical occurrence per theorem.
- If aliases are intended, use distinct alias keys and place them once each.

#### MINOR: box and destination warnings

Evidence:

- `157` overfull boxes
- `343` underfull boxes
- `2` destination warnings:
  - `name{theorem.7.0.29}`
  - `name{convention.1.10.1}`

Concrete fix:

- Address only after the moderate issues are fixed, since many box/destination warnings are likely secondary to unresolved references.

## Volume II

### Exact command result in original directory

- Exact command exit: `2`
- Original PDFs/logs existed, but were stale from `2026-04-09 14:16:09`, so the exact command did not validate a fresh build.

Critical excerpt from the exact command tail:

```text
cp: out/ainfinity_chiral_algebras.pdf: Operation not permitted
cp: out/working_notes.pdf: Operation not permitted
/bin/sh: .build_logs/pass1.log: Operation not permitted
...
touch: .build_stamp: Operation not permitted
make: *** [.build_stamp] Error 1
```

Interpretation:

- The exact build failed because the source tree was not writable in this sandbox, not because TeX itself failed.

### Fresh snapshot-build result

- Snapshot path: `/tmp/codex_vol2_snapshot.WyzZkb`
- Snapshot command exit: `0`
- Verified PDFs:
  - `/tmp/codex_vol2_snapshot.WyzZkb/main.pdf`
  - `/tmp/codex_vol2_snapshot.WyzZkb/out/ainfinity_chiral_algebras.pdf`
  - `/tmp/codex_vol2_snapshot.WyzZkb/out/working_notes.pdf`

### Fresh-build summary

- Fatal TeX lines `^! `: `0`
- Undefined references: `6` occurrences, `4` unique keys
- Undefined citations: `2` occurrences, `2` unique keys
- Multiply-defined labels: `75` occurrences, `75` unique keys
- Overfull `\hbox`: `231`
- Underfull `\hbox`/`\vbox`: `152`
- `pdfTeX warning (dest)`: `1`

### Findings

#### CRITICAL 1: exact requested build path was not writable, so the original-directory build was not a valid verification build

Wave attribution hypothesis:

- Not manuscript-related. This is an execution-environment blocker.

Concrete fix:

- Re-run the exact command outside this sandbox or with write access to `/Users/raeez/chiral-bar-cobar-vol2`.
- If build verification must run in restricted environments, redirect `LOG_DIR`, `OUT_DIR`, and `STAMP` to a writable scratch area and avoid in-tree writes.

#### MODERATE 1: large duplicate-label cluster across the YM synthesis/boundary files

Evidence:

- `75` multiply-defined labels in the fresh log.
- Representative source collisions:
  - `chapters/connections/ym_synthesis_core.tex`
  - `chapters/connections/ym_boundary_theory.tex`
  - `chapters/connections/ym_synthesis_frontier.tex`
  - `chapters/connections/ym_instanton_screening.tex`
- Representative duplicated keys:
  - `thm:twisted-ym-boundary-brst`
  - `thm:grand-synthesis-principle`
  - `thm:screened-tangent-center`
  - many further `twisted-ym-*`, `relative-*`, `w-*`, `instanton-*` labels
- There is also an in-file duplicate phantom label in `main.tex`:
  - `V1-thm:feynman-involution` at lines `618` and `670`.

Wave attribution hypothesis:

- Most likely a same-day YM split/merge pass rather than the Drinfeld-double lane.
- File mtimes cluster on `2026-04-09`:
  - `ym_instanton_screening.tex` `02:46`
  - `ym_synthesis_core.tex` `04:27`
  - `ym_boundary_theory.tex` `04:28`
  - `ym_synthesis_frontier.tex` `13:36`
- So this looks like recent duplication introduced while core/frontier material was being redistributed.

Concrete fix:

- Choose a single canonical definition site for each theorem/definition.
- In the duplicate file(s), either:
  - rename the label with a file-local suffix, or
  - remove the label and refer back to the canonical theorem by `\ref`.
- Remove the repeated `V1-thm:feynman-involution` phantom label in `main.tex`.

#### MODERATE 2: stale chapter alias `chap:ordered-associative` is still referenced

Evidence:

- `chapters/connections/hochschild.tex:1498` and `1535` reference `\ref{chap:ordered-associative}`.
- The live label is `ch:ordered-associative-chiral-kd` in `chapters/connections/ordered_associative_chiral_kd_core.tex:37`.

Wave attribution hypothesis:

- Strong fit to Wave `4-2` re-enable/restructure of ordered-associative content.

Concrete fix:

- Update both references in `hochschild.tex` to `ch:ordered-associative-chiral-kd`, or add a backward-compatibility alias label `chap:ordered-associative` at the live chapter head.

#### MODERATE 3: stale Vol I cross-volume alias `rem:bar-ordered-primacy` is missing

Evidence:

- `chapters/theory/factorization_swiss_cheese.tex:1297` references `\ref{rem:bar-ordered-primacy}`.
- No live label with that key exists in the Vol II snapshot.

Wave attribution hypothesis:

- Likely fallout from Vol I extraction/rename work carried into Vol II by the Wave `4-2` reopening of the ordered/bar-complex lane.

Concrete fix:

- Add the intended Vol I phantom alias in the cross-volume label block, or retarget the reference to the current Vol I label that replaced `rem:bar-ordered-primacy`.

#### MODERATE 4: `AP:126` / `\ref*` breakage yields one explicit missing label plus two `Reference '*'` warnings

Evidence:

- Fresh log shows unresolved keys `AP:126` and `*`.
- Source site:
  - `chapters/connections/ordered_associative_chiral_kd_core.tex:2114`
  - text uses `Anti-Pattern~\ref*{AP:126}`.
- No label `AP:126` exists in the Vol II tree.

Wave attribution hypothesis:

- Fits the user-flagged part-label / AP-label breakage lane.

Concrete fix:

- Replace `\ref*{AP:126}` with plain text `AP126` if anti-pattern numbers are external, or define a real label for AP126 and use `\ref{...}` consistently.

#### MODERATE 5: two bibliography keys used in the Drinfeld-double/spectral-braiding lane are missing

Evidence:

- Missing keys:
  - `BeilinsonBernstein`
  - `BorelDmodules`
- Source:
  - `chapters/connections/spectral-braiding-frontier.tex:2593-2594`
- No corresponding `\bibitem` entries were found in the Vol II bibliography.

Wave attribution hypothesis:

- Strong fit to Wave `6-6`..`6-9`, because the offending citations sit inside the recently expanded `spectral-braiding-frontier.tex` / Drinfeld-double frontier lane.

Concrete fix:

- Add `\bibitem{BeilinsonBernstein}` and `\bibitem{BorelDmodules}` to the bibliography, or replace them with existing house keys if those references already exist under different names.

#### MINOR: box and destination warnings

Evidence:

- `231` overfull boxes
- `152` underfull boxes
- `1` pdf destination warning

Concrete fix:

- Defer until the duplicate-label and unresolved-reference cleanup is done.

## Volume III

### Exact command result in original directory

- Exact command: `make fast`
- The command did not terminate cleanly in the original tree.
- I observed persistent lock-wait behavior caused by the unwritable `.build_logs` directory, then interrupted the waiting process.
- Captured process exit after interrupt: `1`
- Original `main.pdf` and `main.log` existed, but were stale from `2026-04-09 14:14:39`.

Critical excerpt from the exact command tail:

```text
-- Fast build (up to 4 passes) --
Waiting for existing build lock: .build_logs/.build.lock
^C
```

Interpretation:

- `scripts/build.sh` acquires the lock by `mkdir "$LOCK_DIR"`.
- In this sandbox the parent directory was not writable, so the script interpreted write failure as lock contention and waited indefinitely.

### Fresh snapshot-build result

- Snapshot path: `/tmp/codex_vol3_snapshot.Hxx31G`
- Snapshot command exit: `0`
- Verified PDF:
  - `/tmp/codex_vol3_snapshot.Hxx31G/main.pdf`

### Fresh-build summary

- Fatal TeX lines `^! `: `0`
- Undefined references: `18` occurrences, `14` unique keys
- Undefined citations: `49` occurrences, `28` unique keys
- Multiply-defined labels: `0`
- Overfull `\hbox`: `20`
- Underfull `\hbox`/`\vbox`: `26`

### Findings

#### CRITICAL 1: exact requested build path was not writable, so the original-directory build never reached TeX

Wave attribution hypothesis:

- Not manuscript-related. This is an execution-environment blocker.

Concrete fix:

- Re-run the exact command outside this sandbox or grant write access to `/Users/raeez/calabi-yau-quantum-groups`.
- If future restricted builds are required, adjust the build script to distinguish lock contention from directory write failure.

#### MODERATE 1: bibliography is globally disabled, causing a broad unresolved-citation surface

Evidence:

- `main.tex:509` has:

```tex
\bibliographystyle{alpha}
% \bibliography{references}
```

- No bibliography file was found by `rg --files | rg 'bib|references|bibliography'`.
- Fresh build has `49` citation warnings across `28` unique keys, including:
  - `Costello2005`
  - `Kontsevich1994`
  - `Keller2006`
  - `Seidel2008`
  - `Caldararu2005`
  - `KontsevichSoibelman2009`
  - `LurieHA`
  - `BeilinsonDrinfeld`
  - `FBZ04`
  - `DI97`
  - `Fay73`
  - `Zhu96`
  - `SV13`
  - `Gannon16`
  - `DMVV`
  - `Costello17`
  - `VolII`

Wave attribution hypothesis:

- Most likely recent stub-audit / packaging cleanup rather than a single chapter wave, because the failure is global and rooted in `main.tex` rather than in one chapter.

Concrete fix:

- Restore the bibliography source and uncomment `\bibliography{references}`, or inline a `thebibliography` environment.
- Ensure all cited keys above exist before rerunning.

#### MODERATE 2: chapter-label renames were not propagated

Evidence:

- `chapters/theory/e1_chiral_algebras.tex` references `ch:cy-chiral-functor`, but the live label is `ch:cy-to-chiral` in `chapters/theory/cy_to_chiral.tex:2`.
- `chapters/examples/quantum_group_reps.tex:506` references `ch:toroidal-elliptic`, but the live label is `chap:toroidal-elliptic` in `chapters/examples/toroidal_elliptic.tex:47`.
- `chapters/theory/cy_categories.tex:197` references `ch:coha`, but the live toric CoHA chapter label is `ch:toric-coha`.

Wave attribution hypothesis:

- Strong fit to Wave `4-2` restructuring of `quantum_groups_foundations` / `braided_factorization` and the surrounding chapter renaming.

Concrete fix:

- Update the stale references to the live labels, or add backward-compatibility alias labels at the live chapter heads.

#### MODERATE 3: commented-out chapter inputs leave live references pointing at chapters that are not in the build

Evidence:

- `main.tex:459` comments out `\input{chapters/examples/derived_categories_cy}`.
- The stub file itself still carries `\label{ch:derived-cy}`.
- `chapters/examples/fukaya_categories.tex:500` references `ch:derived-cy`.
- `main.tex:464` also comments out `matrix_factorizations.tex`, yet that stub references `ch:derived-cy` too.

Wave attribution hypothesis:

- This is a direct consequence of the `2026-04-08` stub-audit noted in `main.tex`.

Concrete fix:

- Either restore the chapter input, or rewrite those references to a live chapter that now owns the content.
- For stub files left out of the build, remove or quarantine cross-references that assume the chapter is present.

#### MODERATE 4: several referenced labels simply do not exist anywhere in the Vol III build

Evidence:

- Missing keys include:
  - `ch:cha-yangian`
  - `thm:k3-e-bkm-chiral`
  - `prop:e1-descent-unobstructed`
  - `thm:htt-general`
  - `sec:working-notes`
- `rg` found no label definitions for those keys in the built tree.

Wave attribution hypothesis:

- Likely a mixture of recent architectural reshaping and incomplete stub migration, because the missing keys span theory, examples, and notes.

Concrete fix:

- For each key:
  - if it was renamed, update the reference;
  - if it should exist, add the missing `\label`;
  - if the target was removed, replace the `\ref` with plain descriptive text.

#### MODERATE 5: cross-volume references are being treated as local labels

Evidence:

- `chapters/theory/e2_chiral_algebras.tex:173` references `part:e1-core`, which exists in Vol II (`/tmp/codex_vol2_snapshot.WyzZkb/main.tex:1234`) but not in Vol III.
- `chapters/theory/introduction.tex:120` and `chapters/theory/cy_to_chiral.tex:304` reference `sec:analytic-sewing`, which is a Vol I concept, not a live Vol III label.

Wave attribution hypothesis:

- Fits the architectural cross-reference lane the user flagged for Vol III.

Concrete fix:

- Use explicit cross-volume phantom labels in Vol III for external anchors that must be referable internally, or replace them with plain text such as “Volume II, Part II” / “Volume I analytic sewing section”.

#### MINOR: box warnings

Evidence:

- `20` overfull boxes
- `26` underfull boxes

Concrete fix:

- Defer until the bibliography and label surface is repaired.

## Top 5 Most Serious Issues Across All Volumes

1. Vol II exact build in the original directory is not currently verifiable in this sandbox because the build system writes to `.build_logs`, `out/`, and `.build_stamp` in-tree.
2. Vol III exact build in the original directory stalls in its lock-acquisition loop because write denial is interpreted as an existing build lock.
3. Vol III has a global bibliography outage: `\bibliography{references}` is commented out, causing `49` unresolved citations at once.
4. Vol II has a `75`-label multiply-defined cluster in the YM synthesis/boundary/frontier lane.
5. Vol I’s default Annals build leaks archive-only references into the public surface, producing `85` unresolved-reference warnings in the exact requested `make fast` configuration.

## Recommended Fix Order

1. Restore a writable original-directory build environment for Vol II and Vol III, or adapt the build wrappers to support scratch directories.
2. Vol III: restore bibliography infrastructure and rerun.
3. Vol II: remove duplicate labels in the YM lane and the duplicate phantom in `main.tex`.
4. Vol I: add Annals-safe phantoms or gate archive-only references.
5. Clean up the remaining small ref/citation alias mismatches in Vol II and Vol III.
6. Only then spend time on box warnings.

## Estimated Effort

- Vol I cleanup: `2` to `4` hours
  - add Annals phantom labels / gating
  - add `5` bibliography entries
  - remove `2` duplicate label keys
- Vol II cleanup: `1` focused day
  - deduplicate the `75`-label YM cluster
  - fix `chap:ordered-associative`, `rem:bar-ordered-primacy`, and `AP126`
  - add `2` bibliography entries
- Vol III cleanup: `0.5` to `1` day
  - restore bibliography plumbing
  - repair `14` label targets, many of which are straightforward renames or commented-out chapter references
- Total estimate to reach clean fresh builds on all three volumes:
  - manuscript fixes: about `1.5` to `2.5` engineer days
  - plus environment time if the exact in-place build paths must also pass under restricted execution

## Verification Close

Internally proved by this audit:

- Vol I exact `make fast` in the writable repo builds a PDF and exits `0`, but not cleanly.
- Vol II and Vol III manuscript sources can still be freshly compiled on identical snapshots in `/tmp`.

Supported computationally by fresh build logs:

- Vol II and Vol III unresolved warning surfaces reported above.

Still conditional on environment / not settled by this run:

- exact in-place verification for Vol II and Vol III in their original source trees under this sandbox.
