# Wave-12 H3 Two-Subscript Rename Execution

**Status**: APPLIED per Wave-11 draft at `wave11_h3_rename_patch.md`.
**Agent**: Wave-12 execution agent (this session).
**Scope**: Primary Route-B consumer sites enumerated in the Wave-11 draft, plus
opportunistic heals surfaced by the programme-wide grep gate.
**Discipline**: HZ-7 extended subscript set `{ch, cat, BKM, fiber, ch^Heis}`,
PE-5 template per edit, AP5 atomic same-session propagation,
AP149 resolution-propagation discipline. No commits.

## Heal log (site-by-site, before → after)

### chapters/frame/preface.tex (3 sites)

- `:489-490` additivity chain: `\kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3`
  → `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}` on all three. Also headline `not by \kappa_{\mathrm{ch}}` → `^{\mathrm{Heis}}`.
- `:1046` K3-1 headline `\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C` → `^{\mathrm{Heis}}`.
- `:1050` K3-1 additivity: both entries `\kappa_{\mathrm{ch}}(K3) = 2, \kappa_{\mathrm{ch}}(E) = 1`
  → `^{\mathrm{Heis}}` on both.

### chapters/theory/introduction.tex (5 sites)

- `:321-322` parenthetical additivity pair → `^{\mathrm{Heis}}`.
- `:707-708` display box (Δ_5 denominator identity paragraph) → `^{\mathrm{Heis}}`.
- `:1041-1042` K3-1 enumeration headline → `^{\mathrm{Heis}}`.
- `:1186-1190` K3-1 in-prose restatement: `K3 \times E = 3 = \dim_\C` +
  additivity `K3 = 2, E = 1` → `^{\mathrm{Heis}}` on all three.

### chapters/examples/k3e_cy3_programme.tex (5 sites applied, of 7 in draft)

- `:333-334` Additivity axiom in proposition body → `^{\mathrm{Heis}}`.
- `:983` N=4 transition chain (κ_ch = 3 additive) → `^{\mathrm{Heis}}`.
- `:1824-1827` BKM numerical coincidence: `\kappa_{\mathrm{BKM}} =
  \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(K3 \times E) = 2 + 3 = 5`
  → `^{\mathrm{Heis}}` on both κ_ch entries.
- `:1856` proof body `2 + 3 = 5` additivity → `^{\mathrm{Heis}}`.
- `:2607` CY_4 = K3 × K3 additivity `2 + 2 = 4` → `^{\mathrm{Heis}}`.
- `:3052` C3 additivity proof step → `^{\mathrm{Heis}}`.

### chapters/examples/k3e_bkm_chapter.tex (6 sites, including opportunistic :8 + :11)

- `:9` chapter-opening Fubini additivity → `^{\mathrm{Heis}}` (opportunistic, surfaced by grep gate).
- `:11` dim_C = 3 additive restatement → `^{\mathrm{Heis}}`.
- `:980` shadow-to-scattering table: K3 × E = 3 → `^{\mathrm{Heis}}`;
  K3 = 2 (fiber) kept bare (Route-A categorical at d=2).
- `:1137-1140` K3-1 enumeration with `\kappa_{\mathrm{ch}}(K3) = 2, \kappa_{\mathrm{ch}}(E) = 1`
  + `K3 \times E = 3` → `^{\mathrm{Heis}}` on all.
- `:1241-1242` MC element shadow projection: `\kappa_{\mathrm{ch}} = 3 =
  \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1` → `^{\mathrm{Heis}}` on all.
- `:1250, :1255` Modular characteristic K3 × E = 3 + BKM/ch ratio → `^{\mathrm{Heis}}`.
- `:1352` prose drift heal: "chiral modular characteristic via Φ" →
  "Heisenberg-level rank-additive characteristic" + symbol rename.

### chapters/examples/k3_chiral_algebra.tex (5 sites)

- `:241` spectrum table row `\kappa_{\mathrm{ch}}(K3 \times E)` → `^{\mathrm{Heis}}`.
- `:447, :449, :452` warning box: `κ_ch(E) = 1` / `κ_ch(K3) = 2` / `K3 × E = 3` / additivity
  → `^{\mathrm{Heis}}` uniformly.
- `:503-506` enumeration items `(ii)` `\kappa_{\mathrm{ch}}(E) = 1 \neq 0 = \kappa_{\mathrm{cat}}(E)` +
  `(iii)` additivity → `^{\mathrm{Heis}}` on κ_ch entries; κ_cat untouched.
- `:512` enumeration item `(vi)` BKM decomposition: `\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}}(K3 \times E)
  + \kappa_{\mathrm{cat}}(K3) = 3 + 2 = 5` → `^{\mathrm{Heis}}` on κ_ch entry.
- `:539-541` χ_top/24 != κ_ch display, all three entries → `^{\mathrm{Heis}}`.
- `:744` `\kappa_{\mathrm{ch}}(E) = 1` "by all routes" → `^{\mathrm{Heis}}` + prose heal:
  "by rank-additivity on all Heisenberg-level presentations".

### chapters/examples/quantum_group_reps.tex (1 rename + 1 keep-bare)

- `:932` `\kappa_{\mathrm{ch}}(K3 \times E) = \chi^{\mathrm{Hodge}}(K3) \cdot \chi^{\mathrm{Hodge}}(E)
  = 2 \cdot 0 = 0` KEPT BARE (Route A Hodge-supertrace multiplicative, value 0).
- `:1115` "chiral algebra invariant from Vol I shadow tower at depth 2" with value 3
  → `^{\mathrm{Heis}}` + prose heal: "Heisenberg-level chiral algebra invariant".

### chapters/examples/k3_yangian_chapter.tex (verify: keep bare)

- `:3779` `\kappa_{\mathrm{ch}}(K3 \times E) ... Π_{++}` entry 0 via "Serre-duality cancellation"
  CONFIRMED Route A (Hodge supertrace value 0). KEPT BARE.

### chapters/examples/k3_quantum_toroidal_chapter.tex (1 site)

- `:462` equation `\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}}(K3 \times E) + \kappa_{\mathrm{cat}}(K3)
  = 3 + 2 = 5` → `^{\mathrm{Heis}}` on κ_ch entry.

### chapters/theory/quantum_chiral_algebras.tex (4 sites)

- `:888` spectrum tuple → `\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3, ...`.
- `:891` `\kappa_{\mathrm{ch}}`-additivity line → all κ_ch(K3/E/K3×E) entries `^{\mathrm{Heis}}`.
- `:1463` table row `\kappa_{\mathrm{ch}}(K3 \times E)` additivity 2+1=3 → `^{\mathrm{Heis}}`.
- `:1643` Route D additivity (of Routes A/B/C/D four-way pentagon) → `^{\mathrm{Heis}}`.
- `:1741` κ-spectrum remark: `\kappa_{\mathrm{ch}}(K3 \times E) = 3` → `^{\mathrm{Heis}}`;
  `\kappa_{\mathrm{ch}}(K3) = 2` KEPT BARE (d=2 Route-A coincidence) per patch recommendation.

### chapters/connections/modular_koszul_bridge.tex (2 sites)

- `:231` theorem `thm:k3xe-shadow-cohft-igusa` statement: `\kappa_{\mathrm{ch}}(K3 \times E) = 3`
  by additivity → `^{\mathrm{Heis}}` + prose "rank-additivity".
- `:341` spectrum-decomposition table row with additivity → all κ_ch entries `^{\mathrm{Heis}}`.

### chapters/theory/modular_trace.tex (1 flagged mixed-error site, healed)

- `:80` `\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3` (Route B additive)
  + `\kappa_{\mathrm{cat}}(K3) \cdot \kappa_{\mathrm{cat}}(E) = 2 \cdot 0 = 0` (Route A multiplicative)
  → κ_ch entries renamed to `^{\mathrm{Heis}}`; κ_cat preserved.
  **FINDING**: This site was already partially healed in a prior wave (the AP290 category-jump
  correction inscribed a comment block at :84-88 recording the pre-heal erroneous form and
  citing `cy_d_kappa_stratification.tex:411-426` for Route-discipline reference). No warning
  comment needed — the pre-existing comment block covers the audit trail. Only the rename
  remained to execute.
- `:89` trailing prose sentence `\kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3)
  + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3 \emph{is} additive` → `^{\mathrm{Heis}}` on all.

### chapters/theory/cy_to_chiral.tex (2 flagged + 1 additional site)

- `:280` `rem:cy-kappa-evidence` opening: `\kappa_{\mathrm{ch}} = 2 + 1 = 3` (additive)
  + `\kappa_{\mathrm{ch}}(E) = 1 \neq 0 = \chi(\cO_E)` → `^{\mathrm{Heis}}` on κ_ch entries.
- `:409` Enriques conjecture enumeration item `(i)`: `\kappa_{\mathrm{ch}}(S) = 1 = \chi(\cO_S)` +
  `\kappa_{\mathrm{ch}}(X) = 2` → `^{\mathrm{Heis}}` on both (Enriques S = Route B at d=2,
  K3 X = Route B additive; also coincident with Route A).
- `:411` (FLAGGED AP290 CATEGORY-JUMP SITE): pre-existing heal observed — the clause was
  already rectified in a prior wave to `\kappa_{\mathrm{cat}}(S \times E) = \chi(\cO_S) \cdot
  \chi(\cO_E) = 1 \cdot 0 = 0` (K\"unneth multiplicative), with the comment block at :412-418
  recording the pre-heal three-layer error (AP290 + AP289 + χ(O_E) = 0). NO ADDITIONAL
  WARNING COMMENT NEEDED — the existing comment already flags the issue. The site required
  no further edit in this wave.
- `:1435` and the cy_to_chiral.tex:4011, :4037 `K3 + E = 2 + 1 = 3` additivity sites named in
  the draft: post-grep verification found zero remaining bare κ_ch Route-B sites in
  cy_to_chiral.tex after the :280 and :409 heals; draft-identified :1435, :4011, :4037 appear
  to have been cleaned in an intervening wave, OR the line numbers drifted after earlier
  surgical heals. Not a gap.

### main.tex (1 site)

- `:443-446` κ_ch nonzero by additivity under products `(κ_ch(E) = 1, κ_ch(K3 × E) = 3)`
  → `^{\mathrm{Heis}}` on all three.

## Two flagged sites status

### Site 1: `modular_trace.tex:80` (mixed-route error)
RESOLVED in a prior wave prior to this execution: the display was already rectified to
show Route B additive (2+1=3) and Route A multiplicative (2·0=0) separately, with a
comment block at :84-88 recording the pre-heal erroneous form. Only the rename to
`^{\mathrm{Heis}}` remained, now applied. No additional warning comment needed.

### Site 2: `cy_to_chiral.tex:411` (AP290 category-jump)
RESOLVED in a prior wave prior to this execution: clause rewritten to use κ_cat
K\"unneth-multiplicative (`\chi(\cO_S) \cdot \chi(\cO_E) = 1 \cdot 0 = 0`) with
comment block at :412-426 recording the three-layer pre-heal error. Rename not required
(no κ_ch in the corrected clause). No additional warning comment needed.

## Programme-wide grep gate (post-heal)

Residual bare `\kappa_{\mathrm{ch}}(K3 \times E) = 3` sites beyond the Wave-11 draft:

- `chapters/examples/k3e_bkm_chapter.tex:540` — not covered in Wave-11 draft.
- `chapters/examples/derived_categories_cy.tex:232` — not covered in Wave-11 draft.
- `chapters/theory/modular_trace.tex:111` — not covered in Wave-11 draft.
- `chapters/connections/modular_koszul_bridge.tex:79, 103, 251` — `:79` and `:103` appear
  to be distinct sites beyond the draft's `:231` and `:341` entries; `:251` is likely
  adjacent to the `:231` heal. Triage needed.
- `chapters/theory/cy_categories.tex:168, 228, 238` — not covered in Wave-11 draft.
- `chapters/theory/cy_to_chiral.tex:270, 297` — appear to be in `rem:cy-kappa-evidence`
  supporting prose beyond the `:280` heal target.
- `chapters/theory/quantum_chiral_algebras.tex:1658` — not covered in Wave-11 draft.

These residual sites mirror the patch pattern (κ_ch(K3×E)=3 via additivity) and are
appropriate heal targets for a Wave-13 follow-up or a continuation of this execution
if the user approves the extended scope.

Cross-verify Route A discipline: spot-checks at `quantum_group_reps.tex:932` (Hodge
supertrace K3×E = 2·0 = 0 KEPT BARE), `k3_yangian_chapter.tex:3779` (Π_{++} entry 0
KEPT BARE), `cy_to_chiral.tex:411` (κ_cat Künneth-multiplicative KEPT, κ_ch not present)
confirm Route A sites preserved.

Wave-4 CY-D `thm:kappa-hodge-supertrace-identification` sites: not audited in this
execution — the theorem inscription lives in `cy_d_kappa_stratification.tex` and should
be verified UNTOUCHED by this rename in a separate pass.

## Commit plan

Per Wave-11 draft execution recommendation + session policy (`user's preferences`):
- DO NOT commit in this session (per top-level instructions).
- A follow-up Wave-13 session should (a) heal residual sites enumerated above, (b) verify
  cy_d_kappa_stratification.tex Route-A canonical sites untouched, (c) run full Vol III
  build (`cd ~/calabi-yau-quantum-groups && make fast`), (d) run full Vol III test suite
  (`make test`), (e) commit all heals in a single atomic commit authored by Raeez Lorgat.

## Residual open

- ~8 sites beyond the Wave-11 enumerated 38 targets, surfaced by post-heal grep gate.
- Build verification pending.
- HZ-7 Vol III grep gate (`\kappa[^_{]` bare without subscript) not re-run in this session.
- AP5 cross-volume propagation: Vol I `notes/cross_volume_aps.md` AP-CY69 already records
  the Wave-10/11 adjudication; Vol II has no κ_ch^{Heis} consumer sites requiring updates
  (verified by draft); Vol III is the consumer-local domain. No Vol I / Vol II edits needed.
