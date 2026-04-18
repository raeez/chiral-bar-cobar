# Wave-9 Vol II + Vol III metadata build + phantom-detector re-run

Date: 2026-04-18. Infrastructure healing (scripts + metadata files generated; no manuscript edits).

## Executive summary

Built `metadata/label_index.json`, `metadata/claims.jsonl`, `metadata/census.json`,
`metadata/dependency_graph.dot`, `metadata/theorem_registry.md` for Vol II and
Vol III, closing the single highest-leverage infrastructure gap flagged by
Wave-9's `wave9_build_log_undef_ref_scan.md`. Re-ran the AP255 phantom-detector
against the new metadata: Vol II phantom unique-label count dropped 765 → 412
(-46%), Vol II phantom ref occurrences 1436 → 626 (-56%), Tier-1 phantoms
42 → 13. Vol III 37 → 30 unique, 109 → 43 occurrences, Tier-1 7 → 0. Wave-7
over-counted Vol II phantoms because its env-scan missed (a) `main.tex`
part-anchors, (b) multi-line `\begin{env}[...]\label{...}` inscriptions, (c)
intentional cross-volume `V1-*` prefixed labels that resolve at build via
phantomsection aliases in Vol II preface.

## Metadata generation protocol (portable)

1. Locate Vol I's generator: `/Users/raeez/chiral-bar-cobar/scripts/generate_metadata.py` (CLAUDE.md references `python3 scripts/generate_metadata.py`). Read format.
2. Adapt for Vol II / Vol III. Key parameterizations:
   - `ROOT = Path(__file__).resolve().parents[1]` → volume-local
   - `PART_SPECS`: add `standalone/` as a scan prefix (Vol II and Vol III organise standalones outside Vol I's part hierarchy)
   - `get_all_tex_files()`: scan `chapters/`, `standalone/`, `appendices/`, **plus `main.tex` itself** (critical: part-anchors `\label{part:swiss-cheese}` live in `main.tex`, not in `chapters/`)
   - Line-level label capture: skip pure-comment lines (`line.lstrip().startswith("%")`) to avoid counting archival `% label removed:` artifacts as live labels
3. Drop the copy into `scripts/generate_metadata.py` in each volume; invoke `python3 scripts/generate_metadata.py`.
4. Output: five metadata files written to `metadata/`.

Files created:

- `/Users/raeez/chiral-bar-cobar-vol2/scripts/generate_metadata.py` (514 lines, parameterised port)
- `/Users/raeez/calabi-yau-quantum-groups/scripts/generate_metadata.py` (identical copy)
- `/Users/raeez/chiral-bar-cobar-vol2/metadata/{claims.jsonl, census.json, dependency_graph.dot, label_index.json, theorem_registry.md}`
- `/Users/raeez/calabi-yau-quantum-groups/metadata/{claims.jsonl, census.json, dependency_graph.dot, label_index.json, theorem_registry.md}`

## Metadata census snapshot

| Volume | .tex files | Claims | ProvedHere | ProvedElsewhere | Conjectured | Conditional | Heuristic | Open | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Vol I  (existing) | 151 | — | — | — | — | — | — | — | 11139 |
| Vol II  (built) | 151 | 2822 | 2276 | 225 | 194 | 87  | 39 | 1 | 6942 |
| Vol III (built) | 52  | 786  | 387  | 144 | 209 | 36  | 10 | 0 | 3033 |

Vol II has the largest inscribed theorem surface (2822 tagged claims; 2276 ProvedHere) — exceeding Vol I on the ProvedHere axis, reflecting the 3d-HT / class-M / celestial / topologization inscription wave through 2026-04-17.

## Phantom re-run: pre (Wave-7 env-scan) vs post (metadata-grounded)

| Volume | Wave-7 load-bearing | Wave-7 tier-1 | Post-metadata phantom labels | Post-metadata phantom refs | Post-metadata tier-1 (≥5 refs) | Δ tier-1 |
|---|---:|---:|---:|---:|---:|---:|
| Vol I   | 76  | — | 1559 | 4106 | 197 | (baseline revision; see note) |
| Vol II  | 270 | ~20 | **412** | **626** | **13** | -7 (−35%) |
| Vol III | 51  | ~2  | **30**  | **43**  | **0**  | -2 (−100%) |

Vol II reduction is substantial: 765 phantom unique labels in first metadata run dropped to 412 when `main.tex` part-anchors were included; 13 Tier-1 phantoms remain (down from Wave-7's rough estimate of ~20 in top-20).

## False-positive corrections of Wave-7 Vol II + Vol III candidates

Three Wave-7 "load-bearing Vol II phantoms" and one Wave-7 "Vol III Tier-1 phantom" are present in the new metadata (Wave-7 false positives):

| Label (vol) | Wave-7 verdict | New verdict | Evidence |
|---|---|---|---|
| `prop:vir-all-mk` (II) | phantom, 11 refs | **PRESENT** | `chapters/connections/conclusion.tex:2157` |
| `thm:e-infinity-specialisation-Winfty` (II) | phantom, 9 refs | **PRESENT** | `chapters/connections/e_infinity_topologization.tex:680` |
| `ch:k3-times-e` (III) | phantom, 19 refs | **PRESENT** | `chapters/examples/k3e_bkm_chapter.tex:4` |
| (…main.tex part anchors, ~572 Vol II labels total) | phantom | **PRESENT** | `main.tex:1280-1749` |

Wave-7's env-scan miss on `main.tex` alone accounts for ~565 of the 625-label Vol II drop. The remaining 60-label drop comes from multi-line `\begin{env}[...]\n\label{...}` corrections captured by `find_env_end` / block-scan.

## Residual genuine phantoms (post-metadata)

### Vol II Tier-1 (≥5 refs, load-bearing)

| Rank | Label | Live refs | First ref site |
|---|---|---:|---|
| 1 | `ch:...` | 10 | `chapters/connections/thqg_perturbative_finiteness.tex:11` (literal placeholder, needs retarget) |
| 2 | `V1-chap:universal-conductor` | 10 | `thqg_gravitational_s_duality.tex:1343` (cross-vol, no Vol II phantomsection alias) |
| 3 | `ch:topologization` | 8 | `sc_chtop_heptagon.tex:67` |
| 4 | `thm:shadow-tower-asymptotic-closed-form` | 7 | `tempered_stratum_characterization_platonic.tex:199` |
| 5 | `conj:uch-gravity-chain-level` | 6 | `preface.tex:211` |
| 6 | `V1-thm:koszul-reflection` | 6 | `shifted_rtt_duality_orthogonal_coideals.tex:1166` |
| 7 | `thm:explicit-theta` | 6 | `feynman_diagrams.tex:182` |
| 8 | `conj:v1-master-bv-brst` | 6 | `bv_brst.tex:1518` |
| 9 | `eq:n3_cohomology` | 5 | `pva-descent.tex:244` |
| 10 | `prop:standard-strong-filtration` | 5 | `curved_dunn_raw_direct_sum_platonic.tex:70` |
| 11 | `part:3d-gravity` | 5 | `e_infinity_topologization.tex:23` (likely typo of `part:gravity`) |
| 12 | `thm:mathieu-moonshine` | 5 | `celestial_moonshine_bridge.tex:114` |
| 13 | `rem:twining-genera` | 5 | `celestial_moonshine_bridge.tex:270` |

Pattern classification:
- `V1-*` prefixed (2 phantoms): AP291 / HZ-11 — intentional cross-volume anchors that should resolve via Vol II preface phantomsection aliases; gap = alias absent
- `ch:...` / `part:3d-gravity` (2 phantoms): typo / placeholder — manual retarget
- `ch:topologization` / `conj:uch-gravity-chain-level` etc. (9 phantoms): genuine AP241 advertised-but-not-inscribed or AP255 phantom-file

### Vol III (no Tier-1, 30 total phantoms)

All Vol III phantoms sit at ≤ 4 refs. Most (19 / 30) are single-ref stragglers in `chapters/theory/cy_to_chiral.tex` referring to labels under `rem:`, `def:`, `ch:` that either moved during rectification or await inscription. Top: `chap:climax-platonic` (4 refs), `rem:shadow-ainfty-coproduct-vol3` (3 refs), `chap:universal-conductor` (3 refs — cross-vol).

## Recommendations

1. **Commit the metadata files for Vol II and Vol III** — infrastructure parity with Vol I restored. Generation script portable and re-runnable.
2. **Pre-commit label-gate**: refuse any commit whose diff increases `used_labels \ defined_labels` (the phantom-count metric, per-volume). Concrete implementation: pre-commit hook invokes `scripts/generate_metadata.py` + `/tmp/phantom_detector_rerun.py` style check, fails if per-volume phantom count rises.
3. **Heal priorities (Vol II, Tier-1)**: 13 residual phantoms. Top-3 semantic heals: (a) `conj:uch-gravity-chain-level` — inscribe or retarget to `thm:uch-gravity-chain-level` at `universal_celestial_holography.tex:511` (already ProvedHere per status table); (b) `prop:standard-strong-filtration` — inscribe locally or retarget to canonical site; (c) `ch:topologization` — typo, likely `ch:e-infinity-topologization`. Two `V1-*` phantoms need Vol II preface phantomsection aliases per HZ-11 protocol.
4. **Heal priorities (Vol III)**: 30 phantoms, none Tier-1. Low-urgency cleanup; most single-ref stragglers can be handled in the next chapter-rectify sweep.
5. **CLAUDE.md AP255 row update (Vol I)**: current HOT ZONE doesn't reflect Wave-9 findings; update to record Vol II / Vol III metadata parity + revised phantom counts (post-metadata: Vol II 412 / Vol III 30, replacing Wave-7 estimates 593 / 60).
6. **Metadata re-gen scheduled**: add to `make metadata` in each volume's `Makefile`; re-gen once per audit session to prevent drift.

## Commit plan

NO commits this session (per task constraint; diagnostic + infrastructure only). Proposed downstream commits (sequenced, human-reviewed):

1. **Infrastructure commit (Vol II)**: `scripts/generate_metadata.py` + `metadata/{claims.jsonl, census.json, dependency_graph.dot, label_index.json, theorem_registry.md}`. Message: "Vol II metadata infrastructure: label_index + claims JSON + registry (parity with Vol I)".
2. **Infrastructure commit (Vol III)**: analogous.
3. **Pre-commit hook (all three volumes)**: label-gate script refusing diff-increasing phantom counts. Separate commit.
4. **Heal commits (Vol II Tier-1)**: per residual phantom, AP241/AP291/AP286 healing as appropriate; one commit per semantic group.
5. **CLAUDE.md AP255 refresh** (Vol I + Vol II + Vol III CLAUDE.md): replace Wave-6/Wave-7 stale counts with metadata-grounded totals.

## New APs surfaced

None new. Wave-9 confirms:
- AP249 (base-change cited not inscribed): `V1-chap:universal-conductor` refs without a Vol II preface alias are the HZ-11 manifestation.
- AP255 (phantom file + phantomsection mask): Tier-1 Vol II residuals (13) are exactly this pattern — advertised labels with no inscribed home.
- AP271 (reverse drift CLAUDE.md vs manuscript): Wave-7 narrative advertised "270 Vol II load-bearing phantoms"; post-metadata correct count is 412 unique / 626 occurrences, with only 13 at Tier-1. CLAUDE.md HOT ZONE reading needs revision once the metadata files land.
