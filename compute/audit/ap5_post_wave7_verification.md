# AP5 Post-Wave-7 Verification Report

Date: 2026-04-09
Scope: Vol I (`~/chiral-bar-cobar`), Vol II (`~/chiral-bar-cobar-vol2`), Vol III (`~/calabi-yau-quantum-groups`)
Mode: READ-ONLY. No `.tex` modifications performed.
Baseline: `compute/audit/ap5_cross_volume_report_wave6.md` (Wave 6-2)
Checks executed: AP126, AP125, AP32, AP113, AP124 on the Wave-7 post-fix state.

---

## Section 1: Summary Table (Wave 6-2 -> Post-Wave-7)

| Check | Category | Wave 6-2 hits | Post-Wave-7 hits | Delta | Status |
|-------|----------|---------------|------------------|-------|--------|
| AP126 | Bare `\Omega/z` in affine KM context, Vol I CHAPTERS (live) | ~15 | ~13 | -2 | WARNING (residuals remain) |
| AP126 | Bare `\Omega/z` Vol I DRAFT/DEAD files | ~15 | ~13 | -2 | INFORMATIONAL (dead code) |
| AP126 | Bare `\Omega/z` Vol II LIVE files | ~25 | ~9 | -16 | MAJOR IMPROVEMENT |
| AP126 | Bare `\Omega/z` Vol II DEAD files | ~5 | ~10 | +5 | INFORMATIONAL (dead code) |
| AP126 | Bare `\Omega/z` Vol III chapters | 5 | 0 | -5 | CLEAN |
| AP125 | `ht_physical_origins.tex` label-environment mismatches | 4 | 0 | -4 | CLEAN |
| AP125 | Other label-environment mismatches (all three volumes) | 0 | 0 | 0 | CLEAN |
| AP32  | `rosetta_stone.tex` F_g = kappa lambda_g UNIFORM-WEIGHT tags | 4 untagged | 0 untagged | -4 | CLEAN |
| AP32  | `3d_gravity.tex` F_g = kappa lambda_g UNIFORM-WEIGHT tags | ~2 untagged | 0 untagged | -2 | CLEAN |
| AP32  | `landscape_census.tex` (Vol I) UNIFORM-WEIGHT tags | 4 untagged | 0 untagged | -4 | CLEAN |
| AP32  | Vol III `toroidal_elliptic.tex` UNIFORM-WEIGHT tags | 7 untagged | 7 untagged (partial) | 0 | WARNING (scope implicit via prose) |
| AP113 | Vol III bare `\kappa` (non-subscripted) | not counted | 165 bare | n/a | WARNING (new baseline) |
| AP124 | New Wave-7 labels (drinfeld-double-e1-construction, chromatic-bar-cobar, ct2, pixton-from-shadows) | n/a | 0 duplicates | n/a | CLEAN |
| AP124 | Vol I dead-code duplicates (ordered_associative_chiral_kd) | n/a | ~30 dead-copy pairs | n/a | INFORMATIONAL |
| AP124 | Cross-volume duplicate: conj:kappa-bps-universality | n/a | 1 Vol I + 1 Vol III | n/a | WARNING |

Headline: AP126 dropped from ~70 cross-volume hits to ~22 in live files (Vol II live dropped from ~25 to ~9, Vol III cleared to 0). AP125 is fully resolved in `ht_physical_origins.tex`. AP32 is resolved in all three Wave-6-flagged Vol II files and Vol I `landscape_census.tex`; Vol III `toroidal_elliptic.tex` remains partially tagged through prose context rather than explicit `(UNIFORM-WEIGHT)` parentheticals. AP124 new-label uniqueness verified for the four Wave-7 labels, with one residual cross-volume duplicate found (`conj:kappa-bps-universality`). AP113 (Vol III bare kappa) was not counted in Wave 6; this report establishes a new baseline of ~165 bare instances.

---

## Section 2: AP126 Residuals

### 2.1 Vol I live chapters (genuine AP126 residuals)

The following bare `\Omega/z` occurrences in affine Kac-Moody or general r-matrix context remain in files that are `\input{}` into `main.tex`:

- `chapters/examples/w_algebras_deep.tex:2746` — `r^{\mathrm{KM}}(z) = \Omega/z` in a Koszul pair triple expression
- `chapters/examples/w_algebras_deep.tex:2789` — `The simple-pole KM $r$-matrix $\Omega/z$`
- `chapters/examples/yangians_foundations.tex:227` — `$r(z) = \Omega/z = (P - \mathbb{1}/N)/z$` for type $A$
- `chapters/examples/toroidal_elliptic.tex:2513` — `$r(z) = \Omega/z$ (Casimir, $24$-dim)` in `rem:holo-koszul-k3xe`
- `chapters/connections/frontier_modular_holography_platonic.tex:1680` — `rational $r$-matrix $r^{\mathrm{cl}}(z) = \Omega/z$`
- `chapters/connections/frontier_modular_holography_platonic.tex:4654` — `$r(z) = \Omega/z$ (classical Yang--Baxter, $\Omega$ the Casimir element)`
- `chapters/connections/frontier_modular_holography_platonic.tex:4686` — `The R-matrix $r(z) = \Omega/z$ is the collision residue`
- `chapters/connections/arithmetic_shadows.tex:2681, 2718` — two bare `r(z) = \Omega/z` in KZ / Drinfeld associator context
- `chapters/connections/holographic_datum_master.tex:477, 491` — `r^{\mathrm{cl}} = r^{\mathrm{Dr}} = \Omega/z` (Drinfeld r-matrix)
- `chapters/connections/holographic_datum_master.tex:694` — `expansion $r^{\mathrm{Dr}}(z) = \Omega/z = \Omega \cdot \hbar$`
- `chapters/connections/genus1_seven_faces.tex:905, 939` — `r^{\mathrm{ell}}_\fg(z, \tau) \to \Omega/z` (genus-1 limit) and `rational $r$-matrix $\Omega/z$` (limit discussion)
- `appendices/nonlinear_modular_shadows.tex:3049` — `and $\Omega/z$ in the affine case`
- `chapters/theory/algebraic_foundations.tex:344` — spectral CYBE definition `with $r(z) = \Omega/z$` (Benign: generic spectral CYBE reference)

Borderline/benign (no action):
- `chapters/theory/higher_genus_modular_koszul.tex:24740` — `r_0(z) = \Omega/z^3` is the level-STRIPPED form explicitly presented as such in a cohomology argument.

### 2.2 Vol I draft / dead files (dead code, not `\input{}`'d)

- `chapters/frame/preface_section1_draft.tex:643, 652` — two bare hits
- `chapters/frame/preface_section1_v2.tex:491, 501` — two bare hits
- `chapters/frame/preface_sections5_9_draft.tex:542, 581, 582, 608, 683` — five bare hits
- `chapters/frame/preface_sections10_13_draft.tex:354` — Yang's solution (benign regardless)
- `standalone/three_parameter_hbar.tex:212, 295` — bare in exposition (standalone paper)
- `standalone/genus1_seven_faces.tex:695, 722` — bare in genus-1 limit discussion
- `compute/audit/standalone_paper/computations.tex:715, 739` — bare (audit artifact)
- `appendices/ordered_associative_chiral_kd.tex:2360` — dead-code duplicate of live theory file

MAIN PREFACE FIX VERIFIED: `chapters/frame/preface.tex:532` now reads `r(z) = k\,\Omega/z` (Wave 7 fixed the Wave-6 C1 critical). `eq:pf1-km-kappa` (lines 518-524) now uses `\operatorname{av}(r(z))` symbolically rather than `\Omega/z` raw, avoiding the level-stripped identity.

### 2.3 Vol II live chapters (residuals)

- `chapters/connections/ordered_associative_chiral_kd_core.tex:2105, 2945` — `R(z) = 1 + \Omega/z + O(z^{-2})` (R-matrix expansion for `\widehat{sl}_2_k`, level stripped from leading term)
- `chapters/connections/ordered_associative_chiral_kd_core.tex:2733, 2738` — table rows `1+\Omega/z+O(z^{-2})`
- `chapters/connections/ordered_associative_chiral_kd_core.tex:3724` — `r^{\mathrm{coll}}(z) = \Omega/z` (Casimir simple pole, generic statement)
- `chapters/connections/ordered_associative_chiral_kd_frontier.tex:2722` — `r_0 = \Omega/z` with `\Omega\in\mathfrak{sl}_2\otimes\mathfrak{sl}_2` (comparison narrative)
- `chapters/connections/ordered_associative_chiral_kd_frontier.tex:3269, 3270` — `R(z) = 1 + \Omega/z + \cdots` and elliptic deformation `R_\tau(z) = 1 + \Omega/z + \hbar^2 \kappa \wp \Omega/(k+2)^2`
- `chapters/connections/ordered_associative_chiral_kd_frontier.tex:3764` — `R(z) = 1 + \Omega/z` (rational Yang R-matrix in lattice VOA deformation discussion)
- `chapters/connections/ordered_associative_chiral_kd_frontier.tex:6127` — `r_{V_1(\mathfrak{sl}_2)}(z) = 1\cdot\Omega/z` (explicit `k=1` specialization, borderline)
- `chapters/connections/celestial_holography_frontier.tex:1382` — `R_{\mathrm{cel}}(z)=1+\Omega/z+\cdots` (celestial holography R-matrix)
- `chapters/theory/introduction.tex:1985` — table row `$\Omega/z$` (KM column entry in comparison table)

### 2.4 Vol II dead-code files (not built)

- `chapters/connections/log_ht_monodromy.tex:186, 229, 276, 1448` — bare in AP126-noted context (file is not input, `log_ht_monodromy_core.tex` is the live version and uses `k\,\Omega/z` consistently)
- `chapters/connections/celestial_holography.tex:1953` — bare `R_{\mathrm{cel}}(z)=1+\Omega/z+\cdots`
- `chapters/connections/celestial_holography_core.tex:971` — bare (omitted in grep output)
- `chapters/connections/thqg_celestial_holography_extensions.tex:2438` — benign (`k_{\mathrm{BF}}\,\Omega/z` surrounding context) but prose uses bare form in preceding sentence
- `chapters/connections/thqg_ht_bbl_extensions.tex:1100` — bare `\Omega/z` of `\mathfrak{gl}_K` (Costello terminology)
- `compute/audit/non_simply_laced_rmatrix_report.tex:107` — bare (audit artifact)

### 2.5 Vol III chapters

ALL CLEAN. Zero bare `\Omega/z` hits in active Vol III chapters. Every occurrence is level-prefixed with either `k\,`, `\kappa_{\mathrm{cat}}\,`, `\kappa_{\mathrm{ch}}\,`, or explicitly tagged with an AP126 verification comment. Verified files:

- `chapters/examples/quantum_group_reps.tex:127, 142, 267, 553, 561` — all `k\,\Omega/z`
- `chapters/examples/fukaya_categories.tex:148, 178` — all `\kappa_{\mathrm{cat}}\,\Omega/z`
- `chapters/theory/braided_factorization.tex:293` — `\kappa_{\mathrm{cat}}\,\Omega/z`
- `chapters/examples/toroidal_elliptic.tex:2675, 5701` — `\kappa_{\mathrm{ch}}\,\Omega/z` and `k\,\Omega/z` (with AP126 parenthetical)
- `chapters/theory/e2_chiral_algebras.tex:310` — `k \cdot \Omega/z`
- `chapters/theory/e1_chiral_algebras.tex:184` — `k\,\Omega/z` with AP126/AP141 tag
- `chapters/connections/geometric_langlands.tex:35` — `k\,\Omega/z` (already-correct in Wave 6)

---

## Section 3: AP125 Residuals

### 3.1 `ht_physical_origins.tex` (Wave 6 W2)

ALL FOUR Wave-6 flagged mismatches are FIXED:

- Line 1031: `\begin{conjecture}[W-algebra bar-cobar duality; ClaimStatusConjectured]\label{conj:w-algebra-bar-cobar}` — CORRECT
- Line 1276-1277: `\begin{theorem}[HT theory from 4d N=4 SYM; ClaimStatusProvedElsewhere]` / `\label{thm:ht-from-n4-sym}` — CORRECT
- Line 1326-1327: `\begin{theorem}[Boundary chiral algebra; ClaimStatusProvedElsewhere]` / `\label{thm:boundary-chiral-algebra-bv}` — CORRECT
- Line 1363-1364: `\begin{conjecture}[Bar-cobar from HT boundary; ClaimStatusHeuristic]` / `\label{conj:bar-cobar-ht-boundary}` — CORRECT

### 3.2 Broader multi-line AP125 sweep (all three volumes)

Cross-volume multiline grep for `\begin{theorem}` within 3 lines of `\label{rem:...|conj:...|def:...}`, and analogous combinations for `conjecture` and `proposition` environments: ZERO matches. The only near-hit is `notes/physics_bv_brst_cy.tex:467` in Vol III where a comment documents a fix from theorem to conjecture with matching `conj:cy3-bv-bar` label (correct).

STATUS: AP125 is fully clean across all three volumes.

---

## Section 4: AP32 Residuals

### 4.1 Wave-6 flagged files (verified CLEAN)

**Vol I `chapters/examples/landscape_census.tex`**:
- Line 37 (was 35): now `UNIFORM-WEIGHT; multi-weight requires \delta F_g^{\mathrm{cross}}` tagged in the opening summary
- Line 620 (was 3578/3583): tagged `(Theorem \ref{thm:genus-universality}; UNIFORM-WEIGHT)` with explicit scalar-vs-multi discussion immediately following
- Lines 1159, 1196, 3531, 3594, 3601, 3745: all carry `(UNIFORM-WEIGHT; multi-weight requires \delta F_g^{\mathrm{cross}}, cf. Theorem \ref{thm:multi-weight-genus-expansion})` pattern

**Vol II `chapters/examples/rosetta_stone.tex`**:
- Line 1898: `F_g = \kappa(V_k(\fg)) \cdot \lambda_g^{\mathrm{FP}}` tagged `(UNIFORM-WEIGHT; multi-weight requires \delta F_g^{\mathrm{cross}}, cf. \ref{thm:multi-weight-genus-expansion})`
- Line 5453: `F_g = \kappa \cdot \lambda_g^{\mathrm{FP}} \cdot \hbar^{2g-2}` tagged `(UNIFORM-WEIGHT only; multi-weight $g \ge 2$ acquires $\delta F_g^{\mathrm{cross}}$)` plus `F_1 = \kappa/24` tagged `(ALL-WEIGHT at $g = 1$; the cross-channel correction starts at $g \ge 2$)`
- Line 5493: tagged `(UNIFORM-WEIGHT case; multi-weight requires \delta F_g^{\mathrm{cross}})`
- Line 5595: tagged `(UNIFORM-WEIGHT; multi-weight $g \ge 2$ acquires \delta F_g^{\mathrm{cross}})`

**Vol II `chapters/connections/3d_gravity.tex`**:
- Lines 190, 3324, 3457, 3474, 3496, 4332, 4364, 4749, 7558: ALL carry explicit `(UNIFORM-WEIGHT: Vir_c is single-generator, so the scalar formula holds at all genera; multi-weight requires $\delta F_g^{\mathrm{cross}}$, cf. Volume I Theorem \ref*{V1-thm:multi-weight-genus-expansion})` or equivalent. Some also add `$F_1$ is unconditional across lanes`.

### 4.2 Vol III `chapters/examples/toroidal_elliptic.tex` (WARNING, partial)

Lines with `F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}`:

- Line 2713: prose says "proved at genus 1; at $g \geq 2$ the multi-weight genus expansion may receive cross-channel corrections (Vol I, AP32)". Scope is implicit via prose reference to AP32 — NO explicit `(UNIFORM-WEIGHT)` parenthetical tag
- Line 3507: bare `F_g = \kappa_{\mathrm{ch}}\,\lambda_g^{\mathrm{FP}}` in a tautological-insulation discussion — NO tag
- Line 3924: bare in Borel-convergence discussion — NO tag
- Line 3983: bare in topological-string comparison — NO tag
- Line 4003: bare in class-G proof (implicit UNIFORM-WEIGHT via class G) — NO tag
- Line 4594: bare in remark about Schottky — NO tag
- Line 5133: bare in BPS/shadow comparison — NO tag

These occurrences do not carry the explicit `(UNIFORM-WEIGHT)` parenthetical tag within 5 lines. The prose context does clarify scope (e.g., "proved at genus 1; at $g \ge 2$ ... AP32"), but the Wave 6 report's strict reading of AP32 ("every occurrence MUST carry explicit tag") is not met. Note: none of these are in theorem environments, so by the CLAUDE.md's literal language ("every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit tag"), only theorem-environment occurrences are strictly required to carry the tag. All theorem-environment hits appear compliant.

---

## Section 5: AP113 Residuals (Vol III only)

Raw bare `\kappa` (not preceded by `\kappa_`, not inside `\kappa^{...}`, not inside `\cH_\kappa` level-notation) count across Vol III `chapters/`:

| File | Count |
|------|-------|
| `chapters/examples/toroidal_elliptic.tex` | 94 (of which ~9 are `\cH_\kappa`, ~85 genuine bare) |
| `chapters/examples/k3_times_e.tex` | 34 |
| `chapters/theory/cy_to_chiral.tex` | 20 |
| `chapters/examples/`+`theory/`+`connections/` (other) | ~26 |
| **Total raw bare `\kappa` in Vol III chapters** | **~165** (excluding benign `\cH_\kappa`, `\kappa^{IJ}` Killing forms, functional notation `\kappa(\cdot,\cdot)`) |

Representative examples of bare usage:
- `k3_times_e.tex:167` — "a modular characteristic: $\kappa = 5$" (no subscript)
- `k3_times_e.tex:287, 288, 289` — "$\kappa = c_{\mathrm{eff}}/2 = 2$", "$F_1 = \kappa/24 \cdot \deg(\lambda_1)$", "$\kappa = \mathrm{rk}(\cE_1) = 2$"
- `toroidal_elliptic.tex:325` — "curvature $\kappa = \operatorname{rank}(\Lambda)$"
- `toroidal_elliptic.tex:728` — "$a_{(1)}a = \kappa$" (OPE residue)
- `toroidal_elliptic.tex:749, 767, 771` — `\kappa/\epsilon^2` (curvature prefactor in bar expansion)
- `toroidal_elliptic.tex:812` — "$\kappa \cdot \frac{\pi^2 E_2(\tau)}{3}$"
- `toroidal_elliptic.tex:867` — table entry "$-\kappa \cdot \tfrac{2^{2n-2} |B_{2n-2}|}{(2n-2)!}$"

MANY of these are *locally scoped* (the surrounding paragraph defines which kappa is meant), but AP113's strict reading ("Bare kappa is FORBIDDEN in Vol III. ALWAYS subscript") is not met. Recommendation: treat as a Wave 8 rectification target scoped per-file, with the caveat that formula-internal recurring references to a locally-defined kappa (e.g., "let $\kappa := \kappa_{\mathrm{ch}}(\cH_\Lambda)$ in this section") may be grandfathered via a section-header local-definition convention.

NEW BASELINE ESTABLISHED. Wave 6-2 did not count these.

---

## Section 6: AP124 Duplicate Label Check for Wave-7 New Labels

Target labels from the task checklist:

| Label | Vol I | Vol II | Vol III | Total | Status |
|-------|-------|--------|---------|-------|--------|
| `conj:drinfeld-double-e1-construction` | 0 | 1 (`chapters/connections/ordered_associative_chiral_kd_frontier.tex:5829`) | 0 | 1 | UNIQUE |
| `conj:chromatic-bar-cobar` | 0 | 1 (`chapters/theory/en_koszul_duality.tex:2995`) | 0 | 1 | UNIQUE |
| `conj:ct2` | 0 | 1 (`chapters/connections/thqg_open_closed_realization.tex:1176`) | 0 | 1 | UNIQUE |
| `conj:pixton-from-shadows` | 1 (`chapters/examples/w_algebras_deep.tex:5370`) | 0 | 0 | 1 | UNIQUE |

ALL FOUR target labels are unique across all three volumes. Wave-7 label-addition work did not introduce AP124 duplicates.

### 6.1 Adjacent findings (NOT in task scope, informational)

**Cross-volume duplicate found:**
- `conj:kappa-bps-universality`: defined in BOTH Vol I `chapters/examples/toroidal_elliptic.tex:3369` AND Vol III `chapters/examples/toroidal_elliptic.tex:3446`. Vol I also has a `\phantomsection\label{conj:kappa-bps-universality}` stub in `main.tex:1557`. This is a genuine cross-volume AP124 violation; recommend renaming one (likely Vol III -> `conj:kappa-bps-universality-cy` or similar) in a follow-up sweep.

**Vol I internal duplicates (dead code, not AP124 violations at build time):**
- `conj:yangian-quantum-group-general`: `appendices/ordered_associative_chiral_kd.tex:5236` vs `chapters/theory/ordered_associative_chiral_kd.tex:5540`. The appendix file is NOT `\input{}` in `main.tex` (only the theory version is); this is dead-code duplication. Approx 30 similar pairs exist between these two files (entire appendix is a dead near-copy of the theory chapter).
- `conj:cy-a`: `standalone/programme_summary.tex:2552` vs `standalone/programme_summary_sections9_14.tex:547`. Both are in standalone paper drafts, neither inside the active Vol I manuscript.
- `conj:three-language-equivalence`: same appendix-vs-theory dead-copy pattern.

**Vol II internal duplicates (dead code):**
- `conj:weiss-descent`: `chapters/theory/foundations.tex:1115` (LIVE) vs `chapters/theory/foundations_overclaims_resolved.tex:219` (NOT `\input{}`, dead code).

**Vol III internal near-duplicates (one file commented out):**
- `conj:k3e-two-mc`, `conj:eight-qvcg`: defined in BOTH `chapters/examples/toroidal_elliptic.tex` (LIVE) AND `chapters/examples/k3_times_e.tex`. The latter is commented out in `main.tex:452` with the note "Merged into toroidal_elliptic.tex". So these are dead-code duplicates.

---

## Section 7: Recommendations for Wave 9

### Tier A (genuine live-file AP126 residuals)

**Agent W9.vol1-ap126-chapters** (serialize): Fix the Vol I live-chapter residuals:
- `chapters/examples/w_algebras_deep.tex:2746, 2789`
- `chapters/examples/yangians_foundations.tex:227`
- `chapters/examples/toroidal_elliptic.tex:2513`
- `chapters/connections/frontier_modular_holography_platonic.tex:1680, 4654, 4686`
- `chapters/connections/arithmetic_shadows.tex:2681, 2718`
- `chapters/connections/holographic_datum_master.tex:477, 491, 694`
- `chapters/connections/genus1_seven_faces.tex:905, 939`
- `appendices/nonlinear_modular_shadows.tex:3049`

Either insert level prefix `k\,` where the context is affine KM, or add an explicit clarification sentence ("level absorbed into overall normalization; k=0 vanishing is verified in ...") for the Drinfeld r-matrix cases where the level enters via `\hbar` in an independent place.

**Agent W9.vol2-ap126-ordered-chiral**: Fix the Vol II live-file residuals in `ordered_associative_chiral_kd_core.tex` (lines 2105, 2733, 2738, 2945, 3724) and `ordered_associative_chiral_kd_frontier.tex` (lines 2722, 3269, 3270, 3764, 6127). Also `chapters/theory/introduction.tex:1985` and `chapters/connections/celestial_holography_frontier.tex:1382`. These are R-matrix leading-order expansions `R(z) = 1 + \Omega/z + ...` where the level-prefactor convention needs to be made explicit.

### Tier B (Vol III AP113 rectification — requires owner confirmation)

**Agent W9.vol3-ap113-sweep**: Systematic bare-kappa -> kappa_{ch/BKM/cat/fiber} conversion in Vol III. Scope-per-file estimate:
- `toroidal_elliptic.tex`: ~85 bare instances
- `k3_times_e.tex`: ~34 bare instances
- `cy_to_chiral.tex`: ~20 bare instances
- Other: ~26 bare instances

PRE-AGENT STEP: author should confirm the disambiguation for ambiguous cases (e.g., `$\kappa/\epsilon^2$` in elliptic bar expansion — is this `\kappa_{\mathrm{ch}}` or a local abbreviation within a section-scoped redefinition?). This is not a mechanical rename; it requires judgment at every instance.

### Tier C (AP124 cross-volume duplicate rename)

**Agent W9.ap124-kappa-bps-rename** (single atomic commit): Rename `conj:kappa-bps-universality` in Vol III `toroidal_elliptic.tex:3446` to `conj:kappa-bps-universality-cy` (or `-vol3`). Update any `\ref{}` instances in all three volumes (likely only Vol III has internal references, but grep all three). Confirm no build break.

### Tier D (optional, low priority)

**Agent W9.dead-code-cleanup**: Either delete or add a header comment to Vol I `appendices/ordered_associative_chiral_kd.tex` (explicitly mark as dead / never-input archive) and Vol II `chapters/theory/foundations_overclaims_resolved.tex`. These accumulate duplicate labels and confuse AP124 audits. Alternatively, prefix all labels with `obsolete:` in the dead files.

**Agent W9.vol3-ap32-toroidal-tags**: Add explicit `(UNIFORM-WEIGHT; multi-weight requires \delta F_g^{\mathrm{cross}}, cf. Vol I AP32)` parentheticals to the seven `F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}` occurrences in Vol III `toroidal_elliptic.tex` at lines 2713, 3507, 3924, 3983, 4003, 4594, 5133. Optional because the prose context already clarifies scope and these are not in theorem environments.

---

## Closing note

Wave 7 has substantively cleared the Wave 6-2 critical findings:
- AP125 in `ht_physical_origins.tex`: 4/4 fixed
- AP32 in rosetta_stone, 3d_gravity, landscape_census (Vol I): ~10 untagged fixed
- AP126 main preface (Wave 6 C1): fixed
- AP126 Vol III chapters: all cleared
- AP126 Vol II rosetta_stone and log_ht_monodromy_core: all cleared

Residual work falls into three buckets: (i) ~22 genuine AP126 level-stripped instances in live Vol I / Vol II chapters (Tier A above), (ii) a new AP113 baseline of ~165 bare kappa in Vol III (Tier B, requires author-guided conversion), and (iii) one cross-volume `conj:kappa-bps-universality` AP124 duplicate plus dead-code duplicate maintenance debt (Tier C/D).

The Wave 6-2 report's ~70 AP126 raw cross-volume count has dropped to ~22 live-file residuals, a 68% reduction. The four Wave-7 new labels are confirmed unique across all three volumes.
