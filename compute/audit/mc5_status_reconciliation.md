# MC5 Status Reconciliation

Canonical source: `chapters/connections/editorial_constitution.tex:149-150, 179-191, 819`.

Canonical wording (editorial_constitution.tex:179-191):

> MC5 is not fully proved. What is proved at all genera is the analytic
> HS-sewing package (Theorem thm:general-hs-sewing: polynomial OPE growth
> + subexponential sector growth implies HS-sewing convergence;
> Theorem thm:heisenberg-sewing: Heisenberg sewing via Fredholm
> determinant). The remaining genuswise BV/BRST/bar identification is
> still conjectural; at genus 0 the algebraic BRST/bar comparison is
> proved (Theorem thm:algebraic-string-dictionary), while the tree-level
> amplitude pairing requires the additional hypothesis isolated in
> Corollary cor:string-amplitude-genus0. Periodicity is an orthogonal
> weak flank, not a link in this dependency chain.

## Files modified (Vol I)

### CLAUDE.md theorem status table (lines 399-400)
BEFORE:
`| MC1-5 | ALL PROVED | PBW, MC element, thick gen (all types), completion tower, analytic sewing |`
AFTER:
`| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower |`
`| MC5 | ANALYTIC PROVED, BV/BRST CONJECTURAL | HS-sewing (...); genuswise BV/BRST/bar conjectural; genus 0 algebraic BRST/bar proved; tree-level amplitude pairing conditional |`

### FRONTIER.md (lines 21-29)
BEFORE: `### MC1-MC5 (all proved)` and `| MC5 | PROVED | Analytic sewing (thm:general-hs-sewing, thm:heisenberg-sewing) |`
AFTER: `### MC1-MC4 proved; MC5 partially proved` and `| MC5 | ANALYTIC PART PROVED; BV/BRST/bar identification CONJECTURAL | Analytic HS-sewing at all genera (...); genus 0 algebraic BRST/bar comparison proved (...); tree-level amplitude pairing conditional on cor:string-amplitude-genus0; genuswise BV/BRST/bar identification open at g>=1 |`

### README.md (line 26)
BEFORE: `All five master conjectures (MC1-MC5) are resolved, including MC3 for all simple Lie types.`
AFTER: `Master conjectures MC1-MC4 are proved (including MC3 for all simple Lie types on the evaluation-generated core); MC5 is partially proved (analytic HS-sewing package at all genera), while the full genuswise BV/BRST/bar identification remains conjectural.`

### main.tex abstract (line 720)
BEFORE: `All five programme milestones MC1--5 are proved.`
AFTER: `Programme milestones MC1--MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural.`

### chapters/theory/introduction.tex (lines 1791, 1801)
BEFORE: `all five are proved` + table row `MC5 & Genus tower (analytic sewing) & \textbf{proved} & HS-sewing (Thm~\ref{thm:general-hs-sewing})`
AFTER: `MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera while the genuswise BV/BRST/bar identification remains conjectural` + table row `MC5 & Genus tower (analytic sewing) & \textbf{analytic part proved} & HS-sewing (Thm~\ref{thm:general-hs-sewing}); genuswise BV/BRST/bar identification conjectural; genus-$0$ algebraic BRST/bar proved (Thm~\ref{thm:algebraic-string-dictionary}), tree-level amplitude pairing conditional on Cor.~\ref{cor:string-amplitude-genus0}`

### standalone/introduction_full_survey.tex (lines 4711, 4721)
BEFORE/AFTER: identical to chapters/theory/introduction.tex edit.

### chapters/connections/concordance.tex (lines 10697-10718; earlier "Misleading" item)
BEFORE: `All five MC1--MC5 are proved: MC3 is proved for all simple types on the evaluation-generated core ...`
AFTER: `MC1 through MC4 are proved. MC5 is only partially proved: the analytic HS-sewing package is established at all genera (Theorem~\ref{thm:general-hs-sewing}), the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}; the genuswise BV/BRST/bar identification itself remains conjectural (Conjecture~\ref{conj:master-bv-brst}). MC3 is proved for all simple types on the evaluation-generated core ...`

### chapters/connections/outlook.tex (lines 187-189, 256-261)
BEFORE (Ring 1): `Theorems~A--H, MC1--5 all proved, DK-0 through DK-3, ...`
AFTER: `Theorems~A--H, MC1--MC4 proved and MC5 analytically proved (HS-sewing package at all genera; genuswise BV/BRST/bar identification conjectural), DK-0 through DK-3, ...`

BEFORE (Open frontiers): `All five MC1--MC5 are proved. MC3 is resolved for all simple types ...`
AFTER: `MC1 through MC4 are proved. MC5 is partially proved: the analytic HS-sewing package is established at all genera, while the genuswise BV/BRST/bar identification remains conjectural. MC3 is resolved for all simple types ...`

### chapters/connections/thqg_introduction_supplement_body.tex (line 1736)
BEFORE: `All five MC1--MC5 are proved.`
AFTER: `MC1 through MC4 are proved; MC5 is partially proved (analytic HS-sewing package at all genera; genuswise BV/BRST/bar identification conjectural).`

### chapters/frame/preface.tex (line 3316)
BEFORE: `All five master conjectures are proved.`
AFTER: `MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package at all genera and the genuswise BV/BRST/bar identification conjectural.`

### chapters/frame/preface_sections10_13_draft.tex (line 368)
BEFORE/AFTER: same pattern as preface.tex.

### chapters/frame/guide_to_main_results.tex (line 126)
BEFORE: `All five MC conjectures are proved. MC3 is proved for all simple types on the evaluation-generated core; the residual DK-4/5 (extension beyond evaluation modules) is downstream. The full BV/BRST/bar identification at higher genus remains conjectural (Chapter~\ref{chap:editorial-constitution}).`
AFTER: `MC1 through MC4 are proved. MC5 is partially proved: the analytic HS-sewing package is established at all genera (Theorem~\ref{thm:general-hs-sewing}); at genus~$0$ the algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}) and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}; the full genuswise BV/BRST/bar identification at higher genus remains conjectural (Chapter~\ref{chap:editorial-constitution}). MC3 is proved for all simple types on the evaluation-generated core; the residual DK-4/5 (extension beyond evaluation modules) is downstream.`

### standalone/survey_track_a_compressed.tex (line 946)
BEFORE: `All five master conjectures MC1--MC5 are \emph{proved} (PBW concentration, MC element existence, thick generation in every type, completion tower, analytic sewing).`
AFTER: `Master conjectures MC1 through MC4 are \emph{proved} (PBW concentration, MC element existence, thick generation in every type, completion tower). MC5 is partially proved: the analytic HS-sewing package is established at all genera, while the genuswise BV/BRST/bar identification remains conjectural; at genus~$0$ the algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}) and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}.`

### standalone/survey_modular_koszul_duality_v2.tex (lines 1095, 4197, 4270)
BEFORE (three sites): `All five master conjectures MC1--MC5 are \emph{proved}` + status headline `all five master conjectures MC1--MC5 are proved` + MC5 paragraph `Proved. The algebraic genus tower is established together with the analytic sewing package.`
AFTER (three sites): "MC1 through MC4 proved, MC5 partially proved" phrasing with canonical nuance.

### standalone/survey_track_b_compressed.tex (lines 1682, 1755)
BEFORE: `Status: all five master conjectures MC1--MC5 are proved.` + MC5 paragraph `Proved. ...`
AFTER: `Status: master conjectures MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural.` + MC5 paragraph `Partially proved. ...`

### standalone/survey_modular_koszul_duality.tex (lines 7389, 7553)
BEFORE: `All five master conjectures are proved.` + MC5 `Proved.`
AFTER: canonical nuanced wording for both sites.

### standalone/programme_summary.tex (line 2216)
### standalone/programme_summary_sections9_14.tex (line 211)
BEFORE: `All five are proved.`
AFTER: `MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural.`

## Files modified (Vol II)

### chapters/connections/concordance.tex (lines 144, 145, 392, 476, 504)
BEFORE:
- `MC5 (analytic sewing proved all genera; BRST=bar in $D^{co}$ all classes, ...; chain-level false for class M)`
- `MC5 (proved all genera, Vol I)`
- `MC5 is therefore proved at all genera.`
- `The five main conjectures MC1--MC5 of Volume~I are all proved.`
- `MC5 & \textbf{Proved.} Analytic sewing at all genera: ... BV/BRST = bar at g >= 1: resolved in $D^{co}$ for all shadow classes (...); chain-level false for class M.`

AFTER:
- `MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{co}$-level comparison for all shadow classes (...); chain-level false for class M)`
- `MC5 (analytic part proved at all genera, Vol I; genuswise BV/BRST/bar identification conjectural)`
- `The analytic lane of MC5 is therefore proved at all genera; the full genuswise BV/BRST/bar identification remains conjectural.`
- `Master conjectures MC1 through MC4 of Volume~I are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural.`
- `MC5 & \textbf{Analytic part proved.} Analytic HS-sewing at all genera ... The full genuswise BV/BRST/bar identification remains conjectural. At genus 0 the algebraic BRST/bar comparison is proved (thm:algebraic-string-dictionary); tree-level amplitude pairing conditional on cor:string-amplitude-genus0. At g >= 1 the comparison is resolved in $D^{co}$ ...`

### chapters/theory/introduction.tex (line 1570)
BEFORE: `MC5 is proved at all genera.`
AFTER: `the analytic lane of MC5 is proved at all genera, while the full genuswise BV/BRST/bar identification remains conjectural.`

### chapters/connections/ht_physical_origins.tex (lines 439, 759, 807, 1203)
BEFORE (4 sites): `MC5 is proved at all genera in Volume~I` / `MC4 and MC5 are both proved in Volume~I`
AFTER (4 sites): `the analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the full genuswise BV/BRST/bar identification remains conjectural)` (with minor phrasing adjustments per site).

### chapters/connections/spectral-braiding-frontier.tex (line 254)
### chapters/connections/spectral-braiding.tex (line 1915)
BEFORE: `nonabelian case requires the full MC5 identification (Theorem~\ref{rem:mc5-genus-zero-bridge}) applied to $\widehat{\mathfrak{g}}_k$, which is proved at all genera (Volume~I).`
AFTER: `nonabelian case requires the full MC5 identification ... contingent on the genuswise BV/BRST/bar identification of MC5 which remains conjectural in Volume~I beyond the analytic HS-sewing lane.`

## Files modified (Vol III)

### working_notes.tex (line 3328)
BEFORE: `The modular Koszul duality engine is now proved (Theorems A--D+H, MC1--5, 12-fold Koszulness characterization).`
AFTER: `The modular Koszul duality engine is now proved (Theorems A--D+H, MC1 through MC4, the analytic HS-sewing lane of MC5, and the 12-fold Koszulness characterization; the genuswise BV/BRST/bar identification of MC5 remains conjectural).`

## Files modified (compute layer, per AP128)

### compute/lib/theorem_concordance_rectification_engine.py
`MC_STATUS['MC5']` updated from `'PROVED'` to `'PARTIALLY_PROVED'` with inline comment pointing to editorial_constitution.tex canonical lines. Docstring header updated: `THEOREM STATUS CLAIMS: MC1-MC4 proved, MC5 partially proved (analytic HS-sewing lane at all genera; genuswise BV/BRST/bar identification conjectural)`.

### compute/lib/theorem_preface_positioning_engine.py
`MC_STATUS['MC5']` updated from `'proved'` to `'partially_proved'` with inline canonical-source comment. C35 docstring updated: `MC1-MC4 proved; MC5 partially proved`.

### compute/tests/test_theorem_concordance_rectification_engine.py
`test_mc5_proved` renamed to `test_mc5_partially_proved`; `test_all_five_mc_proved` renamed to `test_mc1_through_mc4_proved`; both docstrings cite canonical source.

### compute/tests/test_theorem_preface_positioning_engine.py
`TestC35MCStatus` split into `test_mc1_through_mc4_proved` and `test_mc5_partially_proved` with canonical source cited.

### compute/audit/complete_frontier_status_2026_04_08.md
### compute/audit/exhaustive_gap_analysis_2026_04_08.md
### compute/audit/representation_theory_thread_2026_03_31.md
### compute/audit/session_state_2026_04_01_swarm.md
### compute/audit/chriss_ginzburg_gap_inventory_2026_03_31.md
### compute/audit/holistic_beilinson_assessment_2026_04_01.md (two sites)
Summary lines `MC1-5: All proved` / `MC1-5 complete` / `MC1-5` in PROVED-core tuples all replaced with `MC1-MC4 proved; MC5 partially proved (analytic HS-sewing lane at all genera; genuswise BV/BRST/bar identification conjectural)`.

## Preserved without change (legitimate residual mentions)

- `chapters/examples/heisenberg_eisenstein.tex:2514` "All five are proved in preceding chapters" refers to a local list of five properties of the Heisenberg thqg construction (open/closed MC equation etc.), NOT to MC1-MC5.
- `chapters/connections/concordance.tex:3153` "all five MC levels" is about the rectification mechanism that underlies MC1-MC5, not a status claim.
- `chapters/connections/thqg_entanglement_programme.tex:455` "the sewing construction (MC5) ... which is proved" references the analytic HS-sewing lane specifically (accurate).
- `chapters/connections/twisted_holography_quantum_gravity.tex:953, 2504` reference "sewing machinery of MC5" and "convergence of the two-dimensional tower ... proved by MC5" — both the analytic HS-sewing lane (accurate).
- `compute/lib/*.py` references to `MC5 sewing` in topological vertex / K3 engines (Vol III) refer to the sewing lane only.
- `compute/audit/bv_brst_bar_frontier_report.md` and `compute/audit/codex_survey_v2_math_review_wave14.md` already describe MC5 correctly.
- `compute/audit/kickstart_prompt.md`, `compute/audit/modular_envelope_construction_2026_04_05.md`, `compute/audit/master_infinite_generator_assessment.md`, `compute/audit/analytic_realization_assessment.md`, `compute/audit/algebraic_integration/derived_global_sections.md` reference MC5 analytically, all accurate.
- `editorial_constitution.tex` itself — canonical source, NOT modified.
- Vol II `CLAUDE.md:83` already has nuanced `Proved g=0; conj g>=1` status.

## Verification

Post-fix grep across all three volumes for overclaiming patterns:

```
pattern="MC1-5|MC1--5|MC1--MC5.*proved|MC1-MC5.*proved|all five master|all five MC.*proved|all five are proved"
```

Vol I `.tex`: zero overclaiming hits. Remaining matches are:
- Canonical nuanced wording in `editorial_constitution.tex` (canonical source, preserved).
- Corrected `MC1 through MC4 are proved; MC5 is partially proved` phrasing (new, accurate).
- `chapters/examples/heisenberg_eisenstein.tex:2514` false-positive (local list of five properties).
- `chapters/connections/concordance.tex:3153` false-positive (mechanism, not status).

Vol II `.tex`: zero overclaiming hits. All remaining "MC5 ... proved" mentions are qualified as `analytic HS-sewing lane of MC5 is proved` or reference the sewing machinery specifically.

Vol III: zero overclaiming hits. The single `MC1--5` reference in `working_notes.tex:3328` is corrected.

## Dependency notes

- Theorem labels cited in the canonical wording: `thm:general-hs-sewing`, `thm:heisenberg-sewing`, `thm:algebraic-string-dictionary`, `cor:string-amplitude-genus0`, `conj:master-bv-brst`.
- Vol II cross-references should use `V1-` prefix (e.g. `V1-thm:algebraic-string-dictionary`, `V1-cor:string-amplitude-genus0`).
- The canonical source is `editorial_constitution.tex:149-150, 179-191, 819` (three independent locations that all agree on the nuanced "analytic part proved, BV/BRST conjectural" status).
