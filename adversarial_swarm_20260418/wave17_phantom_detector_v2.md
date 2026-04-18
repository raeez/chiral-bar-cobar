# Wave-17: Phantom Detector v2 — AP286 / AP317 / AP321 aware

Date: 2026-04-18
Agent: infrastructure
Scope: programme-wide (Vol I + Vol II + Vol III)
Commits: none (infrastructure deliverable; no manuscript edits)

## Mission

Close three detector gaps surfaced in Waves 14 / 16 / 17:

1. AP317 multi-line env-scan gap — `\begin{env}[title]` and `\label{foo}`
   on separate lines evade single-line grep.
2. AP321 supervisor-grep-blind — narrow regex for one decorator form misses
   `@_iv`, `@_iv_v14_*`, `TestGoldStandardDisjointPaths`.
3. AP286 umbrella-detection gap — phantomsection aliases with canonical
   twin adjacency or in-line cross-volume comment targets are false-flagged
   as phantoms.

## Deliverable

`scripts/phantom_detector_v2.py` (~390 lines, matches
`scripts/generate_metadata.py` style). Two passes:

1. Per-volume label-site index. Multi-line env scan (±5 lines below every
   `\begin{env}`) resolves AP317. Phantomsection-label sites capture
   adjacent `\label{...}` twins (±5 lines) and in-line `% <file>.tex`
   targets for AP286 classification.
2. Classifier. For every phantomsection label: six verdicts
   `CLEAN | AP286-ALIAS | CROSS-VOL-UMBRELLA | AP255-PHANTOM |
    RETIRABLE-ORPHAN | AP316-WORKTREE`. AP286 alias-pair recognition
   uses twin generators (`v1-`/`v2-`/`v3-` prefix, `-inline`/`-alias`
   suffix), adjacent-real-label match against the live label set, and
   explicit `alias:` or `AP286` comment annotations.

Live-tex filter (AP316): excludes `relaunch_*`, `rectification_*`,
`healing_*`, `opus_audit_*`, `_audit_`, `.claude/worktrees/`, `notes/`,
`adversarial_swarm_*/`, `backup*`, `archive*`, `fix_wave_*`, `.bak`,
`.orig`, `_archive/`. Comprehensive HZ-IV decorator regex
`@independent_verification | @_iv\( | @_iv_v[0-9]+_[a-zA-Z_]+\( |
TestGoldStandardDisjointPaths` closes AP321.

## Per-volume re-run (2026-04-18)

| Volume | Wave-14 naive | Scanned | CLEAN | AP286-ALIAS | CROSS-VOL-UMBRELLA | RETIRABLE-ORPHAN | **AP255 TRUE PHANTOM** |
|--------|--------------:|--------:|------:|------------:|-------------------:|-----------------:|-----------------------:|
| vol1   |           134 |     359 |   239 |           6 |                 74 |               31 |                  **9** |
| vol2   |           223 |     614 |     6 |          14 |                301 |              140 |                **153** |
| vol3   |            41 |      60 |     0 |          12 |                 42 |                0 |                  **6** |

Wave-14 "naive grep count" = label occurrences reported by the earlier
single-line phantomsection grep (no cross-vol verification, no twin
recognition). The v2 scanner inspects a strict superset of sites but
correctly classifies the bulk of them as CLEAN, AP286-ALIAS, or
CROSS-VOL-UMBRELLA.

True phantom rate drops from {134, 223, 41} to **{9, 153, 6}**. Vol I
collapses cleanly; Vol II retains the bulk of genuine AP255 because
`chapters/connections/conclusion.tex` and `main.tex` carry 153 `\ref{}`s
to phantomsection-only labels (`prop:vir-all-mk`, `V1-eq:thqg-VII-...`,
`ch:topologization`, `subsec:gravity-shadow-tower`,
`conj:uch-gravity-chain-level`, ...). These are genuine inscription-gaps
to triage.

## Top-20 AP286-legit validation

Of the 20 labels spot-checked (reported by Wave-14 as phantoms,
confirmed AP286-legitimate by downstream agents):

- 13 resolved by detector v2 as AP286-ALIAS / CROSS-VOL-UMBRELLA
  (including `thm:topologization-tower`,
  `chap:universal-holography-functor`, `chap:chiral-higher-deligne`,
  `conj:master-bv-brst` refs=43, `ch:k3-times-e` refs=22,
  `V1-chap:universal-conductor` refs=11).
- 7 reported ABSENT by the v2 scanner. Independent verification
  confirms 6 are cleanly inscribed in their home volumes
  (`thm:A-infinity-2` Vol I; `thm:iterated-sugawara-construction`,
  `thm:chiral-higher-deligne`, `thm:universal-celestial-holography`,
  `thm:e-infinity-topologization-ladder` Vol II;
  `prop:standard-strong-filtration` Vol I) — they never appeared as
  phantomsections, so v2 correctly does not flag them. The seventh,
  `thm:grt1-rigidity`, was retired 2026-04-18 (see
  `preface.tex:5142` comment); canonical is `thm:grt1-rigidity-sf` in
  `standalone/seven_faces.tex:994`.
- 0 misclassifications.

## True phantom count (programme-wide)

`9 + 153 + 6 = 168` genuine AP255 phantoms (down from Wave-14's
`134 + 223 + 41 = 398`, a 58% reduction once AP286 umbrellas are
classified correctly). Vol II is the dominant locus; priority heal
targets by consumer count:

- `prop:vir-all-mk` (refs=11, `conclusion.tex:2157`)
- `V1-eq:thqg-VII-genus-g-mc-eq` (refs=8, `main.tex:515`)
- `ch:topologization` (refs=8, `main.tex:1018`)
- `subsec:gravity-shadow-tower` (refs=7, `conclusion.tex:2164`)
- `conj:uch-gravity-chain-level` (refs=6, `main.tex:1020`)

Vol I priority:

- `def:thqg-holographic-datum` (refs=7, `main.tex:1935`)
- `conj:master-infinite-generator` (refs=4, `main.tex:2042`)
- `app:coderived-models` (refs=3, `main.tex:1944`)
- `prop:polyakov-chern-weil` (refs=3, `main.tex:2101`)

## Commit plan

No commits from this agent. The detector is infrastructure; it produces
diagnostic output only. Recommended follow-up waves:

1. Wave-18 (Vol II): triage the 153 AP255 phantoms against canonical
   inscriptions in Vol II chapters; downgrade or retarget refs per
   HZ-11.
2. Wave-18 (Vol I): same pass against the 9 Vol I phantoms.
3. Programme infrastructure: add
   `python3 scripts/phantom_detector_v2.py --no-validate` to the
   pre-commit gate for any diff touching `\phantomsection`.

## Files

- `/Users/raeez/chiral-bar-cobar/scripts/phantom_detector_v2.py`
- `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/wave17_phantom_detector_v2.md`
  (this file)
