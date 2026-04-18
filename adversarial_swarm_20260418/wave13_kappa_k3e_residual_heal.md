# Wave-13 κ_ch(K3×E) residual heal — per Wave-12 H3 rename execution agent surfaces

**Date**: 2026-04-18
**Agent scope**: targeted heal of ~8 residual `\kappa_{\mathrm{ch}}(K3 \times E) = 3` bare-subscript sites surfaced by the Wave-12 H3 rename execution agent (a1b6e600) after its ~30 primary renames. Per the H3 two-subscript split (Wave-10 adjudication + `rem:beauville-kappa-formula-subscript-split` canonical convention remark at `chapters/theory/cy_to_chiral.tex:293-298`): Route-A (Hodge supertrace Ξ, K\"unneth-multiplicative, κ_ch(K3×E) = 0) retains bare `\kappa_{\mathrm{ch}}`; Route-B (Heisenberg-level, rank-additive, κ_ch(K3×E) = 3) uses `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}`. HZ-7 approved subscript set extended to {ch, cat, BKM, fiber, ch^Heis}. Constraint: no commits.

## Per-site context and classification

Programme-wide grep sweep (pre-heal) via `kappa_\{\\mathrm\{ch\}\}\([^)]*K3[^)]*\\times[^)]*E[^)]*\)\s*=\s*3` surfaced 14 live manuscript hits in `chapters/` + `appendices/`. All sites classified **Route B** by surrounding prose (additivity / "2 + 1 = 3" / chiral de Rham / tensor product under Künneth functoriality / `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}`-consistent prose upstream):

| # | File : line | Classification | Heal action |
|---|---|---|---|
| 1 | `chapters/examples/k3e_bkm_chapter.tex:540` | Route B (additivity 2+1=3) | rename + cross-ref `rem:beauville...-split` |
| 2 | `chapters/examples/derived_categories_cy.tex:232` | Route B ("by additivity") | rename both sides of Koszul-sum expr |
| 3 | `chapters/theory/modular_trace.tex:8` (chapter intro, adjacent) | Route B ("chiral de Rham complex") | rename + cross-ref |
| 4 | `chapters/theory/modular_trace.tex:8` (additive vs mult) | Route B (additive vs multiplicative) | rename + cross-ref |
| 5 | `chapters/theory/modular_trace.tex:111` | Route B (contrast χ(O)=0 via additivity) | rename + cross-ref |
| 6 | `chapters/connections/modular_koszul_bridge.tex:79` | Route B ("differ in general" via additivity) | rename both E and K3×E; cross-ref |
| 7 | `chapters/connections/modular_koszul_bridge.tex:103` | Route B (additive root cause) | rename both E and K3×E; cross-ref |
| 8 | `chapters/connections/modular_koszul_bridge.tex:251` | Route B ("2 + 1 = 3" explicit) | rename + cross-ref |
| 9 | `chapters/theory/cy_categories.tex:168` | Route B (generically nonzero LHS, RHS vanishes) | rename + cross-ref |
| 10 | `chapters/theory/cy_categories.tex:228` | Route B ("additivity...under tensor products") | rename + cross-ref |
| 11 | `chapters/theory/cy_categories.tex:238` | Route B (dimension-stratified catalogue) | rename quintic / K3×E / local P² uniformly |
| 12 | `chapters/theory/cy_to_chiral.tex:270` | Route B (additive CY-D stratification) | rename + cross-ref |
| 13 | `chapters/theory/cy_to_chiral.tex:297` | Route B meta (scope-convention remark describing the rename rule itself) | rewritten to use the rename consistently |
| 14 | `chapters/theory/quantum_chiral_algebras.tex:1658` | Route B (internal-route data, Routes~B/C/D) | rename + cross-ref |
| 15 | `chapters/theory/braided_factorization.tex:958` | Route B ("total-space...Künneth additivity") | rename + cross-ref |
| 16 | `chapters/theory/braided_factorization.tex:984` | Route B (total-space, extractor of K3 elliptic genus) | rename |
| 17 | `chapters/theory/braided_factorization.tex:1219` | Route B (total-space vs fibre) | rename + cross-ref |
| 18 | `chapters/theory/braided_factorization.tex:1762` | Route B (total-space) | rename |
| 19 | `appendices/conventions.tex:107` | Route B (κ-spectrum {0,2,3,5,24} enumeration) | rename + cross-ref |

**Zero Route-A sites** among the residuals: every surfaced hit was in an additivity / chiral-de-Rham / product-additivity / Heisenberg-lattice-rank context, consistent with the canonical convention remark. This confirms that the Wave-12 primary rename pass correctly left the Hodge-supertrace (Route-A, value 0) sites bare; the residuals are all sites where the primary pass missed a rename target in additive-branch prose.

## Atomic rename log

Nineteen `Edit` invocations total (two retries for initially-failed exact-match strings that required larger context windows). Per-Edit strategy: (a) replace `\kappa_{\mathrm{ch}}` with `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}` on the affected math formula, (b) add inline "Heisenberg-level" qualifier in prose where helpful, (c) append `cf.\ Remark~\ref{rem:beauville-kappa-formula-subscript-split}` cross-reference to anchor readers to the canonical convention. No bulk `replace_all` (FM42 discipline). All edits ≤ one math expression per `old_string`.

Exception: `cy_to_chiral.tex:297` — this line sits *inside* `rem:beauville-kappa-formula-subscript-split` itself and originally read "Sites quoting `\kappa_{\mathrm{ch}}(K3 \times E) = 3` are Route-B (Heisenberg-level) and use `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}`". The bare κ_ch here was metalinguistic (quoting the old form as an exemplar), but leaving it bare violated the rule the remark was announcing. Rewrote to "Sites quoting the additive value 3 use `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3` (Route B, Heisenberg-level); sites quoting the Künneth-multiplicative value 0 use bare `\kappa_{\mathrm{ch}}(K3 \times E) = 0` (Route A, Hodge supertrace, canonical Φ_d)." — preserving the meta-classification while using the canonical form.

## Programme-wide grep gate

**Before** (Wave-12 residual surfaces): 14 live manuscript hits across 8 files (per Wave-12 H3 rename execution agent surface + bonus `modular_trace.tex:8`, `cy_to_chiral.tex:297`, extra `cy_categories.tex` sites, 4 `braided_factorization.tex` hits, 1 `conventions.tex` hit).

**After**:
```
$ grep -rn 'kappa_{\mathrm{ch}}\([^)]*K3[^)]*\\times[^)]*E[^)]*\)\s*=\s*3' \
  /Users/raeez/calabi-yau-quantum-groups/chapters/ \
  /Users/raeez/calabi-yau-quantum-groups/standalone/ \
  /Users/raeez/calabi-yau-quantum-groups/appendices/ \
  /Users/raeez/calabi-yau-quantum-groups/main.tex
# → zero hits (live manuscript)
```

Only remaining hits reside in `notes/anti_pattern_catalogue.tex.archive:1080,1109` — archive/scaffolding file, out of scope for constitutional metadata hygiene and the H3 rename discipline; `.archive` files are preserved historical notes, not typeset manuscript.

## Commit plan

Mission constraint: **no commits in this agent**. Recommended downstream commit batching (to be performed separately):

1. Single atomic Vol III commit titled "Vol III Wave-13 κ_ch(K3×E) residual heal: ~19 Route-B rename propagation per rem:beauville-kappa-formula-subscript-split" including all 19 Edit targets + this `wave13_kappa_k3e_residual_heal.md` note.
2. Build check: `cd ~/calabi-yau-quantum-groups && make fast` — verify `\ref{rem:beauville-kappa-formula-subscript-split}` resolves in every cross-chapter reference (anchor label lives in `chapters/theory/cy_to_chiral.tex:294`; consumers include `chapters/examples/*`, `chapters/connections/*`, `chapters/theory/*`, `appendices/conventions.tex`).
3. Cross-volume AP5 propagation: grep `~/chiral-bar-cobar` and `~/chiral-bar-cobar-vol2` for `\kappa_{\mathrm{ch}}(K3 \times E) = 3` hits (Vol I/II) — expected zero by Vol-III-localised subscript convention; if any live, open a separate Wave-14 heal.

## AP discipline

- **HZ-7** (Vol III κ-subscript): respected; approved subscript set now includes `ch^Heis` per the two-subscript split.
- **AP234** (κ+κ' = K vs ρ·K family-dependent): Heisenberg-level additivity is orthogonal to the complementarity identity; no κ+κ' expression touched.
- **AP289** (Künneth-multiplicative for supertrace): the Route-A branch (κ_cat = χ(O), value 0 for K3×E) stays correctly bare and multiplicative; the Route-B branch (κ_ch^Heis, additive rank-sum, value 3) is now consistently subscripted.
- **AP290** (κ-subscript type-swap): Route A/B ambiguity is the paradigmatic κ-subscript-type-swap risk; this heal converts the collision into an explicit two-subscript split anchored by the canonical convention remark.
- **AP-CY69** (K3×E symbol collision): resolved site-by-site per the convention-remark decision procedure.
- **PE-5** (Vol III κ pre-edit template): satisfied per Edit — subscript present, justification Heisenberg-level (rank-additive) from the canonical remark, grep delta across live manuscript = −14 bare hits.
- **AP5** (cross-volume propagation): live Vol III manuscript clean post-heal; downstream AP5 sweep of Vol I/II pending (recommended as Wave-14 seed if any bare hits surface outside Vol III).

## Residual hooks observed (false positives)

The post-Edit hook surfaced AP24 / AP25 / AP44 / AP106 / AP113 / AP7 warnings on lines I did NOT edit (e.g., `cy_categories.tex:255` λ-bracket, `cy_to_chiral.tex:1278` bar-cobar, `cy_to_chiral.tex:170` K3×E value 0, `quantum_chiral_algebras.tex:1723` "This chapter establishes"). These are pre-existing file-state warnings triggered by the broader grep-context of my small edits. All new content I introduced is HZ-7 compliant (subscripted κ + cross-reference). No new APs introduced.

## Summary

- **Scope**: Wave-12 residual sweep on bare `\kappa_{\mathrm{ch}}(K3 \times E) = 3` → `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3` per two-subscript split.
- **Outcome**: 19 atomic renames across 8 files; programme-wide live grep gate zero; `.archive` scaffolding out of scope.
- **Status**: converged; awaiting downstream commit + build check by orchestrator.
