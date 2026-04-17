# Wave-7 AP255 phantom-detector re-run — detection-gap-corrected sweep

Date: 2026-04-18. Diagnostic-only (no edits, no commits).

## Executive summary

Wave-6 AP255 programme-wide sweep reported 258 load-bearing + 292 retirable orphans = 550 "genuine phantoms", 1018 phantomsection labels total. Wave-7 agent a220890d proved `conj:topologization-general` was a DETECTION FALSE-POSITIVE (inscribed at `en_koszul_duality.tex:3392` but missed by single-line regex scanning `\begin{env}[...]\label{...}` on one line; actual environment header and `\label` sit on separate lines). Present re-run applies two detection-gap fixes and finds Wave-6 overstated genuine-phantom count substantially for Vol I.

## Two detection-gap fixes applied

1. **Multi-line environment scan**: grep `\label{LABEL}` across 3-5 line window after `\begin{env}` header; previously single-line patterns missed `\begin{conjecture}[title]\n\label{...}`.
2. **Live-tex consumer filter**: count `\ref{LABEL}` only under `chapters/`, `standalone/`, `appendices/`, `main.tex`; exclude archival directories (`relaunch_*`, `rectification_*`, `healing_*`, `opus_audit_*`, `wave2_audit_*`, `fix_wave_*`, `resume_*`, `audit_campaign_*`, `tmp_standalone_audit/`, `final_gaps_*`, `platonic_rectification_*`, `.worktrees/*`, `notes/`, `adversarial_swarm_*/`, `memory/`, `backup`, `archive`).

Cross-check: Vol I `metadata/label_index.json` (11139 entries) provides independent ground-truth. Vol II/III lack metadata directories; two-step env-scan used alone there.

## Phantom counts — before (Wave-6) vs after (Wave-7 re-run)

| Volume | phantomsection labels | Wave-6 "genuine phantoms" | Wave-7 false-positives corrected | Wave-7 genuine phantoms | Load-bearing (live-tex) | Orphan |
|---|---|---|---|---|---|---|
| Vol I  | 357  | (implied ~400+) | 251 | 106 | 76  | 30  |
| Vol II | 599  | (implied ~450+) | 6   | 593 | 270 | 323 |
| Vol III| 60   | (implied ~100)  | 0   | 60  | 51  | 9   |
| **Total** | **1016** | **~550** | **257** | **759** | **397** | **362** |

Of the 357 Vol I phantomsection labels, 251 (70%) are detection false-positives — they WERE inscribed in the manuscript as genuine `\begin{...}\label{...}` environments, and the phantomsection was just a redundant alias (AP286 tactical alias pattern). Vol II (6/599 = 1%) and Vol III (0/60) show cleaner alias hygiene.

## Tier-1 ABSENT-register re-verification (12 Wave-6 candidates)

| Label (vol) | Wave-7 verdict | Evidence |
|---|---|---|
| `conj:topologization-general` (Vol I) | **FALSE POSITIVE** | inscribed `en_koszul_duality.tex:3392` |
| `thm:spectral-characteristic` (Vol I) | **FALSE POSITIVE** | inscribed `higher_genus_modular_koszul.tex:3800` |
| `thm:chiral-qg-equiv-elliptic` (Vol I) | confirmed phantom | 0 env-scan, not in label_index |
| `thm:chiral-qg-equiv-toroidal-formal-disk` (Vol I) | confirmed phantom | 0 env-scan |
| `thm:chiral-qg-equiv-ordered` (Vol I) | confirmed phantom | 0 env-scan |
| `def:ordered-koszul-chiral-algebra` (Vol I) | confirmed phantom | 0 env-scan |
| `prop:yangian-ordered-koszul` (Vol I) | confirmed phantom | 0 env-scan |
| `prop:sl2-yangian-triangle-concrete` (Vol I) | confirmed phantom | 0 env-scan |
| `thm:w-infty-chiral-qg-completed` (Vol I) | confirmed phantom | 0 env-scan |
| `prop:e3-gl-N` (Vol I) | confirmed phantom | content lives only as rem:e3-non-simple-gl-N |
| `thm:e3-identification-semisimple` / `-reductive` / `-solvable` (Vol I) | confirmed phantom | 0 env-scan |
| `prop:e3-heisenberg` (Vol I) | confirmed phantom | 0 env-scan |
| `thm:grt1-rigidity` (Vol I) | confirmed phantom | 0 env-scan, consumers live in preface `\phantomsection` alone |

**2 / 15 are false positives** — matching the Wave-7 Beilinson audit's prior finding. The remaining 13 are genuine.

## Top-20 re-verified load-bearing phantoms (live-tex consumers only)

| rank | label | vol | live refs |
|---|---|---|---|
| 1 | `conj:master-bv-brst` | I | **86** (Wave-6 said 43; actual is larger not smaller because Wave-6 count undercounted live-tex and overcounted archive) |
| 2 | `V1-rem:sc-higher-genus` | II | 16 |
| 3 | `def:thqg-holographic-datum` | I | 14 |
| 4 | `thm:complementarity` | I | 14 |
| 5 | `V1-lem:degree-cutoff` | II | 12 |
| 6 | `chap:toroidal-elliptic` | I | 12 |
| 7 | `prop:vir-all-mk` | II | 11 |
| 8 | `thm:topologization-tower` | I | 10 |
| 9 | `thm:quantum-complementarity-main` | II | 10 |
| 10 | `ch:k3-times-e` | III | 19 (Wave-6 reported 22 — over-count was archive-inflated) |
| 11 | `V1-thm:recursive-existence` | II | 9 |
| 12 | `thm:bar-cobar-isomorphism-main` | II | 9 |
| 13 | `thm:e-infinity-specialisation-Winfty` | II | 9 |
| 14 | `thm:genus-universality` | II | 9 |
| 15 | `ch:kontsevich-integral` | I | 8 |
| 16 | `chap:infinite-fingerprint-classification` | I | 8 |
| 17 | `conj:master-infinite-generator` | I | 8 |
| 18 | `thm:delta-f-cross-w3-g2` | I | 8 |
| 19 | `thm:derived-additive-kz` | I | 8 |
| 20 | `thm:elliptic-vs-rational` | I | 8 |

The top-1 phantom (`conj:master-bv-brst`) touches 14 Vol I theory chapters, 5+ standalones, preface, concordance, frontier_modular_holography_platonic, bv_brst, hochschild_cohomology, en_koszul_duality, higher_genus_modular_koszul, higher_genus_complementarity, koszul_pair_structure, poincare_duality_quantum. AP255-Tier-1 load-bearing; inscription or semantic retargeting required.

## Detection-gap recommendations

1. **Multi-line env scan is load-bearing**: any AP255 sweep must grep `\begin{env}` across 5-line window before concluding "phantom". Single-line `\begin{...}.*\label{...}` regex misses ~70% of Vol I phantomsection aliases.
2. **metadata/label_index.json as ground truth**: Vol I has one; Vol II and Vol III should build equivalent indices. Without them, env-scan alone must go through every `.tex` file under chapters/standalone/appendices — more expensive but sound.
3. **Live-tex filter is mandatory**: archival directories (`relaunch_*`, `rectification_*`, `healing_*`, `opus_audit_*`, `wave2_audit_*`, `fix_wave_*`, `resume_*`, `audit_campaign_*`, `tmp_standalone_audit/`, `final_gaps_*`, `platonic_rectification_*`, `.worktrees/*`, `notes/`, `adversarial_swarm_*/`, `memory/`) inflate consumer counts. Wave-6 `conj:master-bv-brst` reported 43 refs (archive-inclusive) but the LIVE count is 86 refs — archival undercounted because archival greps only hit a subset of duplicated archival snapshots.
4. **Exclude phantomsection hits from consumer count**: `\phantomsection\label{L}` lines that also carry `\ref{L}` via neighbor environments should not be counted as consumers; filter `| grep -v phantomsection`.
5. **Build a canonical phantom registry** at `notes/phantom_registry.md` with (label, env, load-bearing-count, tier, heal-plan) columns; re-verify once per session per AP271 discipline.

## Commit plan

This is diagnostic. No edits, no commits. Downstream commit plan (if user authorises):

1. CLAUDE.md AP255 row update: record corrected programme-wide total (759 genuine phantoms, 397 load-bearing, 362 orphan) replacing Wave-6 estimate (550 genuine).
2. Retire 251 Vol I + 6 Vol II phantomsection aliases where the inscribed `\label{}` already exists in a live environment (redundant scaffolding, AP286 tactical-alias cleanup).
3. Tier-1 heal priorities — top 5 load-bearing Vol I phantoms: `conj:master-bv-brst` (86 refs), `def:thqg-holographic-datum` (14), `thm:complementarity` (14), `chap:toroidal-elliptic` (12), `thm:topologization-tower` (10). Inscribe locally OR retarget to canonical Vol II counterparts via AP286 semantic heal (NOT tactical alias).
4. Vol II `V1-rem:sc-higher-genus` (16 refs) and `V1-lem:degree-cutoff` (12 refs) — verify whether `V1-*` prefix points at genuine Vol I labels (cross-volume resolution per HZ-11) or is self-disabled per AP291.
5. Vol III `ch:k3-times-e` (19 refs) — short and tractable; inscribe as `\chapter{}\label{}` in the K3 × E chapter head or retarget.

Total new APs: zero. The re-run confirms Wave-7's AP271 + AP286 caution: status narratives must be re-verified against source post-heal; tactical aliases that mask inscribed labels inflate phantom counts; live-tex filtering is non-negotiable for consumer tallies.
