# CG-rectify REDO queue — Vol I — 2026-04-17

## Context

Previous session (2026-04-17) attempted to run `/chriss-ginzburg-rectify` on Vol I chapters but cut corners. Instead of executing the full 5-phase skill (Phase 1 full-file diagnostic → Phase 2 platonic restructuring → Phase 3 chunk-by-chunk 5-gate loop at 50–100 lines/chunk → Phase 4 RED/BLUE/GREEN parallel re-audit → Phase 5 final convergence with build+test), the session only ran a lightweight screening-grep pass: a single `rg` for the common prose-slop patterns (notably, crucially, em-dashes, empty cites, arity, signposts, LaTeX `\end{...>` typos). When the grep returned zero matches, the file was declared "CONVERGED (0 edits)". When it returned matches, cosmetic fixes were applied and the file declared "CONVERGED (N edits)".

**This is not the skill.** The skill requires mathematical verification from first principles: every formula recomputed against `landscape_census.tex`, every `\ClaimStatusProvedHere` checked against what the proof actually proves, every scope qualifier verified against edge cases (critical level, admissible level, self-dual point), every cross-reference resolved, every section's inevitability assessed, every physical identification labelled as theorem/heuristic/metaphor, every operadic conflation guarded against (AP25/AP34/AP50). None of that was done.

**Scope of redo**: every file touched in that session, including files that had editorial edits applied. Editorial fixes (FM7 `\end{...>` typos, AP176 arity→degree, empty cites, em-dashes, signposts) do not constitute a 5-phase rectification. The mathematical-truth/define-before-use/concept-motivation/physical-realization/reconstitution gates were never run.

## Queue

Format: `[ ]` pending, `[x]` done (full 5-phase), `[~]` partial (>3000 lines, chunked across multiple firings). The 2026-04-17 session's shallow-screen and editorial-fix passes do NOT count as done — the file is still `[ ]` until the full 5-phase audit lands.

### chapters/theory/ (8 files — editorial only in prior session, 5-phase pending)

- [ ] `chapters/theory/bar_construction.tex`  (prior: 2 FM94 cite fills)
- [ ] `chapters/theory/configuration_spaces.tex`  (prior: 13 FM94 cite fills)
- [ ] `chapters/theory/chiral_hochschild_koszul.tex`  (prior: 6 AP176 arity→degree + 1 em-dash + 3 empty cites)
- [ ] `chapters/theory/chiral_koszul_pairs.tex`  (prior: 1 signpost fix)
- [ ] `chapters/theory/poincare_duality_quantum.tex`  (prior: 1 Knudsen83 cite)
- [ ] `chapters/theory/climax_theorem.tex`  (prior: 1 em-dash cleanup)
- [ ] `chapters/theory/kappa_conductor.tex`  (prior: 1 em-dash cleanup)

(Whatever else lives under `chapters/theory/` that wasn't touched: enumerate via `ls chapters/theory/` and add to queue.)

### chapters/examples/ (29 files — all 0-edit shallow-screen or editorial only)

- [ ] `chapters/examples/lattice_foundations.tex`  (5134 lines, chunk)
- [ ] `chapters/examples/level1_bridge.tex`
- [ ] `chapters/examples/logarithmic_w_algebras.tex`
- [ ] `chapters/examples/minimal_model_examples.tex`
- [ ] `chapters/examples/minimal_model_fusion.tex`
- [ ] `chapters/examples/moonshine.tex`
- [ ] `chapters/examples/n2_superconformal.tex`
- [ ] `chapters/examples/shadow_tower_extended_families.tex`
- [ ] `chapters/examples/symmetric_orbifolds.tex`
- [ ] `chapters/examples/w_algebras.tex`
- [ ] `chapters/examples/w_algebras_deep.tex`
- [ ] `chapters/examples/w3_composite_fields.tex`
- [ ] `chapters/examples/w3_holographic_datum.tex`
- [ ] `chapters/examples/y_algebras.tex`
- [ ] `chapters/examples/yangians.tex`
- [ ] `chapters/examples/yangians_computations.tex`
- [ ] `chapters/examples/yangians_drinfeld_kohno.tex`
- [ ] `chapters/examples/yangians_foundations.tex`
- [ ] `chapters/examples/bar_complex_tables.tex`
- [ ] `chapters/examples/deformation_quantization.tex`  (prior: 1 FM94 cite fill)
- [ ] `chapters/examples/deformation_quantization_examples.tex`
- [ ] `chapters/examples/genus_expansions.tex`
- [ ] `chapters/examples/bershadsky_polyakov.tex`
- [ ] `chapters/examples/beta_gamma.tex`
- [ ] `chapters/examples/chiral_moonshine_unified.tex`  (prior: 13 FM7 `\end{...>` fixes)
- [ ] `chapters/examples/exceptional_yangian_koszul_duality_platonic.tex`
- [ ] `chapters/examples/free_fields.tex`
- [ ] `chapters/examples/heisenberg_eisenstein.tex`
- [ ] `chapters/examples/kac_moody.tex`
- [ ] `chapters/examples/landscape_census.tex`

### chapters/connections/ (all — 7 shallow-screened, 14 untouched)

Shallow-screened:

- [ ] `chapters/connections/editorial_constitution.tex`
- [ ] `chapters/connections/entanglement_modular_koszul.tex`
- [ ] `chapters/connections/frontier_modular_holography_platonic.tex`
- [ ] `chapters/connections/genus_complete.tex`
- [ ] `chapters/connections/holographic_codes_koszul.tex`
- [ ] `chapters/connections/master_concordance.tex`
- [ ] `chapters/connections/outlook.tex`

Untouched in prior session:

- [ ] `chapters/connections/poincare_computations.tex`
- [ ] `chapters/connections/semistrict_modular_higher_spin_w3.tex`
- [ ] `chapters/connections/subregular_hook_frontier.tex`
- [ ] `chapters/connections/thqg_entanglement_programme.tex`
- [ ] `chapters/connections/thqg_introduction_supplement.tex`
- [ ] `chapters/connections/thqg_introduction_supplement_body.tex`
- [ ] `chapters/connections/concordance.tex`
- [ ] `chapters/connections/feynman_connection.tex`
- [ ] `chapters/connections/feynman_diagrams.tex`
- [ ] `chapters/connections/genus1_seven_faces.tex`
- [ ] `chapters/connections/holographic_datum_master.tex`
- [ ] `chapters/connections/bv_brst.tex`
- [ ] `chapters/connections/arithmetic_shadows.tex`
- [ ] `chapters/connections/thqg_open_closed_realization.tex`

### chapters/frame/ (skip abstract, preface, introduction)

Enumerate `ls chapters/frame/*.tex`, remove `abstract.tex`, `preface.tex`, `introduction.tex`; queue the rest.

### Standalone papers (after manuscript body)

Enumerate `ls standalone/*.tex`; queue all.

## Completion log

Each entry: `YYYY-MM-DD HH:MM  <file>  commit=<sha>  notes`

(Prior 2026-04-17 editorial and shallow-screen passes are logged in git history but do NOT count as completions — those files remain `[ ]` above.)

## What counts as done (bar for `[x]`)

Per the skill's five phases:

1. **Phase 1**: file read end-to-end (every line). Produce 7-heading diagnostic: narrative thread, motivation gaps, define-before-use violations, opening/closing, physical insight labels, prose slop, AP1–AP233 formula red flags.
2. **Phase 2**: platonic-ideal assessment (organizing question, climax, section sequence, cut list, missing list, scope envelope per AP7/AP32). Execute structural edits if needed (reorder/merge/split/move with `% MOVED TO` stubs — never delete mathematical content).
3. **Phase 3**: chunk-by-chunk 5-gate loop at ~50–100 lines/chunk. Gates 2 and 3 are HARD (define-before-use, concept motivation) — an undefined symbol or unmotivated definition blocks chunk convergence. Gate 1 requires recomputing every formula from first principles against `landscape_census.tex` and compute/ layer, not pattern-matching. Gate 4 verifies physical claims are correctly labelled. Gate 5 is the Chriss-Ginzburg standard (inevitability, synthesis, courage).
4. **Phase 4**: spawn three parallel adversarial agents (RED/BLUE/GREEN) via the `Agent` tool with `run_in_background=true`. Merge findings. Re-enter Phase 3 on affected chunks if any agent finds issues at severity ≥ MODERATE.
5. **Phase 5**: re-read with fresh eyes; build Vol I (`pkill -9 -f pdflatex; sleep 2; cd ~/chiral-bar-cobar && make fast`); build Vol II and Vol III if formula changes propagated; run `make test`. Report: chunks, iterations, findings by severity, gate failure distribution, RECTIFICATION-FLAGs left open, Phase 4 verdicts, build/test status.

Shallow-screening (a single rg pass, fixing whatever cosmetic matches come up) is NOT any of these phases.
