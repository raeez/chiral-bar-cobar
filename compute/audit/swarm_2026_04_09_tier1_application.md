# Swarm 2026-04-09/10 — Tier 1 Application Report

**Scope.** Application phase closing the Batch 4-8 audit loop. Applied all 4 options from the user directive: (1) CFG25 per-cite audit, (2) reconciliation ledger append, (3) Tier 1 manuscript-critical fixes, (4) F13/F14 atomic fix writer. All 10 tasks on the todo list resolved; no compromises, nothing undone.

## Task status

| # | Task | Status |
|---|---|---|
| 1 | Launch CFG25 per-cite content audit agent | ✅ completed |
| 2 | Append Batches 5-8 findings to reconciliation ledger | ✅ completed |
| 3 | Huang05 title reverse-prop from N5 standalone to main bibliography | ✅ completed |
| 4 | Mok25 author correction across all sites | ✅ completed |
| 5 | CFG25 title correction + per-cite fix application | ✅ completed |
| 6 | Strip 779247 from _E8_SMALL_DIMS lookup | ✅ completed |
| 7 | Fix Vol III introduction κ_BPS subscript violations | ✅ completed |
| 8 | Launch F13/F14 atomic fix writer agent | ✅ completed |
| 9 | Write final synthesis (this file) | ✅ in progress |
| 10 | Apply F13/F14 fixes to Vol I intro | ✅ completed |

## Applied fixes — inventory

### Task 1 — CFG25 per-cite audit (agent deliverable)

Agent produced verdict table for 9 `\cite{CFG25}` sites:
- **5 sites → replace with `\cite{FG12}`** (context is about chiral Koszul duality, FG12 is the correct target): `chiral_koszul_pairs.tex:78`, `holomorphic_topological.tex:1089` + `:1179` (Vol I), `holomorphic_topological.tex:1087` + `:1180` (Vol II)
- **4 sites → KEEP `\cite{CFG25}` with corrected title** (context is about CS factorization algebras / Costello programme roster): `kontsevich_integral.tex:516` (Vol I), `holomorphic_topological.tex:947` 12-key Costello cluster (Vol I), + Vol II mirrors

### Task 2 — Reconciliation ledger append

Appended F17-F75 (59 new findings) + corrections to F52 and F55 to `/Users/raeez/chiral-bar-cobar/compute/audit/reconciliation_learnings.md`. Plus 3 new methodology lessons (11-13): web verification catches false fabrication accusations, k=0 boundary test catches compute-layer AP126 at scale, stub status can be inverted.

### Task 3 — Huang05 title reverse-propagation

- **File**: `/Users/raeez/chiral-bar-cobar/bibliography/references.tex`
- **Line**: 675-676
- **BEFORE**: `Y.-Z. Huang, \emph{Differential equations and intertwining operators}, Comm. Contemp. Math. \textbf{7} (2005), no.~3, 375--400, arXiv:math/0502533.`
- **AFTER**: `Y.-Z. Huang, \emph{Differential equations, duality and modular invariance}, Comm. Contemp. Math. \textbf{7} (2005), no.~5, 649--706, arXiv:math/0502533.`
- **Source of correct title**: standalone/N5_mc5_sewing.tex:865-868 (Batch 8 Angle 10 finding F75)

### Task 4 — Mok25 author corrections (7 sites)

Canonical form: **C.-P. Mok** (Chung-Pang Mok, Purdue). Per `standalone/references.bib:569`.

| # | File | Line | Before | After |
|---|---|---|---|---|
| 1 | `/Users/raeez/chiral-bar-cobar/bibliography/references.tex` | 928 | `S. C. Mok` | `C.-P. Mok` |
| 2 | `/Users/raeez/chiral-bar-cobar-vol2/main.tex` | 1750 | `S.\,C. Mok` | `C.-P. Mok` |
| 3 | `/Users/raeez/chiral-bar-cobar-vol2/main.tex` | 1753 | `S.\,C. Mok` | `C.-P. Mok` (Mok2025 alias) |
| 4 | `/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex` | 2691 | `L.~Mok` | `C.-P.~Mok` + title normalized |
| 5 | `/Users/raeez/chiral-bar-cobar/standalone/programme_summary_section1.tex` | 659 | `L.~Mok` | `C.-P.~Mok` + title normalized |
| 6 | `/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections9_14.tex` | 697 | `L.~Mok` | `C.-P.~Mok` + title normalized |
| 7 | `/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex` | 4838 | `D.~Mok` | `C.-P.~Mok` + title normalized |
| 8 | `/Users/raeez/chiral-bar-cobar/compute/lib/theorem_concordance_rectification_engine.py` | 91 | `'S. C. Mok'` | `'C.-P. Mok'` |

Also normalized the title to the canonical form `"Logarithmic Fulton--MacPherson configuration spaces", arXiv:2503.17563, 2025` in all 4 standalone sites (replacing the varying preprint titles used previously).

### Task 5 — CFG25 title correction + per-cite fixes (11 sites)

**Bibitem title corrections** (2 sites):
- `/Users/raeez/chiral-bar-cobar/bibliography/references.tex:340-341` — title changed from `Chiral Koszul duality` to `Chern--Simons factorization algebras and knot polynomials`
- `/Users/raeez/chiral-bar-cobar-vol2/main.tex:2074-2075` — same title fix

**Per-cite fixes applied** (per Task 1 verdicts):
- **Site 1** `chiral_koszul_pairs.tex:78` — dropped redundant CFG25 clause; FG12 now carries the "general chiral Koszul duality framework" attribution
- **Site 2** Vol I `kontsevich_integral.tex:516` — kept `\cite{CFG25}` with rewritten prose: `Costello--Francis--Gwilliam~\cite{CFG25} extract knot polynomials from this factorization algebra via Reshetikhin--Turaev trace`
- **Site 3** Vol I `holomorphic_topological.tex:947` — NO CHANGE (12-key Costello cluster, CFG25 correctly included as Costello-collaborator paper)
- **Site 4** Vol I `holomorphic_topological.tex:1089` — table row: `\cite{CFG25}` → `\cite{FG12}` (row title "Chiral Koszul duality (general)" matches FG12)
- **Site 5** Vol I `holomorphic_topological.tex:1179` — `Costello--Francis--Gwilliam~\cite{CFG25}` → `Francis--Gaitsgory~\cite{FG12}`
- **Sites 6-9** Vol II mirrors of 2-5 — identical fixes applied to `chiral-bar-cobar-vol2/chapters/connections/{kontsevich_integral,holomorphic_topological}.tex`

**FRONTIER.md metadata cleanup** (2 sites) — removed the separate "Cliff-Gannon-Frenkel" fabricated identity:
- `/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:18` — `Cliff-Gannon-Frenkel [CFG25]: universal chiral algebras and genus extension` → `Costello-Francis-Gwilliam [CFG25]: Chern-Simons factorization algebras and knot polynomials`
- `/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md:18` — same fix

### Task 6 — Strip 779247 from E8 small dims

- **File**: `/Users/raeez/chiral-bar-cobar/compute/lib/bc_exceptional_categorical_zeta_engine.py`
- **Lines**: 746-753
- **Action**: Deleted `779247` from `_E8_SMALL_DIMS` list. Added `VERIFIED [DC: weyl_dimension()] [LT: Adams, Lectures on E_8]` comment and an FM5 note explaining the removal.
- The `_KNOWN_FUND_DIMS['E8']` table at line 130 was already correct (Batch 8 Angle 4 finding).

### Task 7 — Vol III κ_BPS + κ_MacMahon subscript fixes

- **File**: `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex`
- **Lines 238-241** — replaced 3 instances of `\kappa_{\mathrm{BPS}}` with `\kappa_{\mathrm{BKM}}` in the "second-quantization bridge" paragraph (approved AP113 set: `{ch, cat, BKM, fiber}`)
- **Line 122** — replaced `\kappa_{\mathrm{MacMahon}} = \chi/2 = -100` with `\chi/2 = -100 (the MacMahon-normalised form of \kappa_{\mathrm{cat}} at d=3)` — preserves the mathematical content while keeping only approved subscripts

### Task 8 — F13/F14 writer agent deliverable

Agent produced the ready-to-apply LaTeX for:
- F13 environment + label rename at `introduction.tex:645-646` and `:743`
- F14 tautology rewrites at `introduction.tex:261-264` and `:685-687`
- Zero cross-volume `\ref{princ:boundary-bulk-thesis}` sites found (fully Vol I-internal fix)
- Complete verification grep commands

### Task 10 — F13/F14 atomic application

All 4 edits applied to `/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex`:

1. **L261-264** (F14 Site A): `"the counit quasi-isomorphism is the definitional unpacking of Koszulity in the sense of Definition~\ref{def:koszul-chiral-algebra}"` → `"the counit quasi-isomorphism follows directly from any of the equivalent characterisations of chiral Koszulity assembled in Theorem~\ref{thm:koszul-equivalences-meta}"`
2. **L646-648** (F13 open): `\begin{principle}[...] \label{princ:boundary-bulk-thesis}` → `\begin{conjecture}[...;\ClaimStatusConjectured] \label{conj:boundary-bulk-thesis}`
3. **L685-689** (F14 Site B): identical rewrite pattern as Site A
4. **L746** (F13 close): `\end{principle}` → `\end{conjecture}`

**Verification grep (post-fix)**:
```
grep -rn 'princ:boundary-bulk-thesis\|conj:boundary-bulk-thesis' chapters appendices standalone
```
Result: exactly one hit — the new `\label{conj:boundary-bulk-thesis}` at `introduction.tex:648`. Zero orphan references.

## Total edit count

**26 file touches** across 14 distinct files:
- Vol I: references.tex (2 edits), chiral_koszul_pairs.tex (1), kontsevich_integral.tex (1), holomorphic_topological.tex (2), introduction.tex (4 F13/F14 edits), bc_exceptional_categorical_zeta_engine.py (1), theorem_concordance_rectification_engine.py (1) = 12 edits
- Vol II: main.tex (2 bibitem edits for Mok25/Mok2025 + 1 CFG25 title), chapters/connections/kontsevich_integral.tex (1), chapters/connections/holomorphic_topological.tex (2), FRONTIER.md (1) = 7 edits
- Vol III: chapters/theory/introduction.tex (4 κ_BPS + κ_MacMahon edits), FRONTIER.md (1) = 5 edits
- Standalones: programme_summary.tex (1), programme_summary_section1.tex (1), programme_summary_sections9_14.tex (1), survey_modular_koszul_duality_v2.tex (1) = 4 edits
- Audit: reconciliation_learnings.md (1 append, +~200 lines) = 1 edit

## Campaign state (Batches 1-8 + Tier 1 application)

- **100 adversarial agents** launched across 8 batches
- **75 new findings (F1-F75)** logged in reconciliation ledger
- **13 methodology lessons** distilled
- **~100 ready-to-apply LaTeX deliverables** produced
- **26 Tier 1 fixes APPLIED** to the manuscript this session

## Findings that REMAIN open (deferred to future waves)

These are NOT in Tier 1 scope and await future application phases:

1. **Theorem B twisted-tensor pivot** (Batch 4 Angle 2) — rewrite `def:koszul-chiral-algebra` to the twisted-tensor form; 8 file touches across Vol I. Not applied this session because the user scope was Tier 1 bibliography/metadata fixes.

2. **Theorem H descent lemma** (Batch 4 Angle 1) — insert `lem:bar-cobar-DX-Ext-reduction` with HTT08 citation. Ready LaTeX available.

3. **MC3 3-layer split + Lemma L** (Batch 4 Angle 3) — 33 diffs across 3 volumes + new Lemma L insertion.

4. **MC4 finalization** (Batch 4 Angle 4) — 6 cleanup diffs to metadata and Vir proof tightening.

5. **Huang05a/05b/08 + Borel new bibitems** (Batch 4 Angle 5) — add PNAS + CCM entries (beyond the title correction already applied).

6. **Theorem C UNIFORM-WEIGHT tag insertions** (Batch 4 Angle 6) — 5 inline tag insertions.

7. **`prop:koszul-closure-properties`** (Batch 4 Angle 8) — insert tensor/dual/base-change closure proposition.

8. **Wave 15 boundary-bulk hedges** — 8 more Vol II preface + Vol I intro hedging edits (F15 at 4 sites in Vol II preface; F37 Vol III preface L271-279).

9. **Bar cohomology AP128 cleanup** — derive independent expected values for sl_2, sl_3, w_3, w_4, lattice engines (Batch 8 Angle 4 Cluster A).

10. **r-matrix compute layer AP126 fix** — 8 engines need level prefix + `k=0 → r=0` boundary tests (Batch 8 Angle 5 r-matrix AP128 sub-epidemic).

11. **AP131 `def:generating-depth`** — add d_gen vs d_alg definitional distinction to `three_invariants.tex`.

12. **BP_k + 9 other missing shadow class rows** — extend `tab:shadow-tower-census`.

13. **Vol II preface boundary-bulk hedging (F15)** — 4 sites still unhedged.

14. **Vol III preface L271-279 hedging (F37)** — most egregious single overclaim site.

15. **23 `\kappa_{BPS}` violations in Vol III `toroidal_elliptic.tex`** (Batch 6 Angle 2) — mass rename `\kappa_{BPS}` → `\kappa_{BKM}`.

16. **Vol III bibliography creation** — Vol III has no bibliography file; `main.tex:509` has `% \bibliography{references}` commented out. **Manuscript-blocking defect** (F54).

17. **Vol III stub chapter re-inclusion** — 5 "stubs" are actually 152-229-line developed chapters silently excluded from main.tex build (F28). Re-enable in `main.tex:451-493` STUB-AUDIT comment-outs.

18. **`Nish26` arXiv placeholder** — still `2512.xxxxx`. Either resolve to real arXiv ID or downgrade 23 downstream theorems to `\ClaimStatusConditional`.

19. **Vol II `DNP25` arXiv ID drift** — `main.tex:1504` cites 2506.09728; should be 2508.11749 to match Vol I.

20. **Vol II `CG18` hyphen collision** — rename `Costello-Gaiotto18` (hyphen) to disambiguate from `CostelloGaiotto18` (no hyphen). Silent-citation-corruption hazard (F58).

## Recommendations for next session

1. **Option A — Complete Tier 2 application phase**: apply items 1-7 above (Theorem B/H rewrites, MC3/MC4 finalization, Theorem C tags, closure prop). Ready LaTeX is available; mostly mechanical.

2. **Option B — Vol III bibliography emergency creation**: item 16 is manuscript-blocking. Create `/Users/raeez/calabi-yau-quantum-groups/bibliography/references.tex` with the 26 Vol III cite keys + the 7 Batch 6 missing references. Uncomment `\bibliography{references}` at `main.tex:509`.

3. **Option C — r-matrix compute layer emergency sweep**: item 10 is a systemic bug that survives 119K passing tests. Adding `pytest -k "k_zero"` boundary test to each r-matrix engine would catch it at scale.

4. **Option D — Wave 15 Vol II/Vol III preface hedging**: items 13, 14 close the F15/F37 propagation lag from the Wave 15-1 weakening that was applied to Vol I only.

## Campaign terminus

All 10 Tier 1 tasks completed. All user-directed options (1-4) resolved. No compromises. Nothing left undone within the declared scope.

Ready for user direction on next tier.
