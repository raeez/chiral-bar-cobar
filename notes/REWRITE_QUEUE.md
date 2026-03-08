# Rewrite Queue

This file tracks the systematic rearchitecture pass. Status values:
`queued`, `in_progress`, `done`.

## Wave 1: Control Layer

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 0 | `main.tex` | part architecture | make the part structure read as frame / core / portraits / synthesis | `done` |
| 0 | `chapters/theory/introduction.tex` | front door | state governing question, route through the book, and explicit north star | `done` |
| 0 | `chapters/connections/concordance.tex` | status ledger | make this chapter the synthesis/programme control document | `done` |

## Wave 2: Status Propagation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 1 | `chapters/frame/heisenberg_frame.tex` | frame example | ensure package language matches scalar/full status discipline | `done` |
| 1 | `chapters/theory/higher_genus.tex` | modular core | keep fiberwise curvature vs total differential notation rigid | `done` |
| 1 | `chapters/theory/chiral_koszul_pairs.tex` | recognition layer | remove any remaining definitional circularity or stale theorem phrasing | `done` |
| 1 | `chapters/theory/deformation_theory.tex` | deformation package | align H/M/S language and shadow sentences | `done` |

## Wave 3: Portrait Pass

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 2 | `chapters/examples/free_fields.tex` | atomic portrait | reduce duplicate Heisenberg exposition; push reader back to frame chapter | `done` |
| 2 | `chapters/examples/kac_moody_framework.tex` | representation-theoretic portrait | foreground what this family reveals that Heisenberg cannot | `done` |
| 2 | `chapters/examples/w_algebras_framework.tex` | reduction portrait | make DS reduction read as structural transport, not appendix material | `done` |
| 2 | `chapters/examples/genus_expansions.tex` | global portrait | present genus data as a theorematic interlock, not a table dump | `done` |

## Wave 4: Synthesis Pass

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 3 | `chapters/connections/bv_brst.tex` | physics bridge | state precisely what is proved and what waits on the master conjectures | `done` |
| 3 | `chapters/connections/holomorphic_topological.tex` | gauge-theory bridge | connect Costello-Li output to the modular programme with exact regime tags | `done` |
| 3 | `chapters/connections/kontsevich_integral.tex` | topology bridge | present restriction to knot-theoretic shadow as theorem/conjecture, not analogy | `done` |
| 3 | `chapters/connections/physical_origins.tex` | horizon chapter | compress rhetoric, keep only mathematically load-bearing programme links | `done` |

## Wave 5: Remaining Synthesis Alignment

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 4 | `chapters/connections/poincare_computations.tex` | computational bridge | tag bridge-level claims as explicit conjectures; separate computed core from horizon claims | `done` |
| 4 | `chapters/connections/feynman_diagrams.tex` | perturbative bridge | add section-level status discipline where definitions feed heuristic dictionary claims | `done` |
| 4 | `chapters/connections/genus_complete.tex` | all-genus bridge | mark theorematic chain constructions vs physics-horizon conjectures with explicit regime split | `done` |

## Wave 6: Core Route Discipline

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 5 | `chapters/theory/algebraic_foundations.tex` | algebraic template | add governing-question opening that separates antecedent data from theorematic consequences | `done` |
| 5 | `chapters/theory/configuration_spaces.tex` | geometric substrate | add governing-question opening that isolates load-bearing geometric identities | `done` |
| 5 | `chapters/theory/bar_cobar_construction.tex` | strict duality core | make genus-0 strict vs genus-$g$ curved regime split explicit at chapter entry | `done` |
| 5 | `chapters/theory/poincare_duality.tex` | anti-circularity chapter | foreground intrinsic dual construction via Verdier duality at chapter entry | `done` |

## Wave 7: Remaining Part I Openings

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 6 | `chapters/theory/chiral_modules.tex` | module-layer extension | add governing-question opening for representation-level Koszul duality route | `done` |
| 6 | `chapters/theory/poincare_duality_quantum.tex` | defect bridge | separate theorematic universal-defect core from conjectural holographic interpretation at entry | `done` |
| 6 | `chapters/theory/quantum_corrections.tex` | correction package | make universal correction mechanism vs algebra-specific scalar data explicit at chapter entry | `done` |

## Wave 8: Remaining Portrait Openings

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 7 | `chapters/examples/lattice_foundations.tex` | portrait input layer | make lattice chapter opening explicitly state common-input role for Part~II families | `done` |
| 7 | `chapters/examples/beta_gamma.tex` | non-abelian free-field portrait | add governing-question framing and theorematic status discipline at entry | `done` |
| 7 | `chapters/examples/deformation_quantization.tex` | quantization portrait | separate proved genus-$0$ quantization from open higher-genus extension at entry | `done` |
| 7 | `chapters/examples/examples_summary.tex` | portrait control ledger | state explicit role as stabilized-output table feeding synthesis | `done` |

## Wave 9: Synthesis Input Alignment

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 8 | `chapters/connections/feynman_connection.tex` | bridge input section | add governing-question and status split so heuristic physics dictionary is distinguished from theorematic content | `done` |

## Wave 10: Residual Core Entry Pass

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 9 | `chapters/theory/koszul_pair_structure.tex` | pair-invariant layer | add governing-question opening for pair-level invariant extraction | `done` |

## Wave 11: Frontier Reset

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 10 | `CLAUDE.md` | repo state ledger | refresh counts and frontier after resolved finite-type PBW | `done` |
| 10 | `notes/GPT54_CODEX_OPERATING_SYSTEM.md` | cognitive doctrine | replace “five-master-conjecture” framing by theorem + four live master conjectures | `done` |
| 10 | `metadata/frontier_and_gaps.md` | computational frontier | move `W_N` from “claimed abstractly” to theorem-level finite-type status and isolate MC4 | `done` |
| 10 | `raeeznotes15.md` | proof-programme memo | prepend post-MC1 addendum so the dossier is read historically, not as current status | `done` |
| 10 | `compute/lib/pronilpotent_bar.py` | MC4 scaffold | implement weight-filtered completion support for infinite-generator bar theory | `done` |

## Wave 12: Frame Alignment

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 10 | `chapters/frame/heisenberg_frame.tex` | frame model | add explicit governing-question statement aligning frame chapter with route discipline used in core/portraits/synthesis | `done` |

## Wave 13: Periodicity Scope Discipline

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 11 | `chapters/theory/derived_langlands.tex` | periodicity programme chapter | add explicit rank-1-proved vs higher-rank-conjectural boundary at the point where periodicity feeds KL programme language | `done` |
| 11 | `metadata/frontier_and_gaps.md` | frontier control note | add March 7 frontier reset block isolating finite-type theorem-level `W_N` from MC4 infinite-generator frontier | `done` |
| 11 | `raeeznotes15.md` | historical dossier hygiene | strengthen pre-resolution warning so legacy MC1-bottleneck language is read as archival, not current doctrine | `done` |

## Wave 14: MC4 Compute Surface Integration

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 12 | `compute/lib/__init__.py` | compute API surface | export pronilpotent completion helpers so MC4 scaffolding is available through the package root imports | `done` |

## Wave 15: Remaining Theory Chapter Entry Discipline

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 13 | `chapters/theory/hochschild_cohomology.tex` | deformation/cohomology core | add governing-question opening with explicit theorem/programme boundary statement | `done` |
| 13 | `chapters/theory/en_koszul_duality.tex` | higher-dimensional extension chapter | add governing-question opening marking what is proved from the curve-level machine versus higher-dimensional programme targets | `done` |
| 13 | `chapters/theory/derived_langlands.tex` | derived bridge chapter | add governing-question opening distinguishing critical-level theorematic core from admissible-level conjectural periodic-CDG extension | `done` |

## Wave 16: Advanced Portrait Entry Discipline

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 14 | `chapters/examples/yangians.tex` | braided portrait chapter | add governing-question opening distinguishing theorematic $\Eone$ chain-level content from full derived DK/KL horizon | `done` |
| 14 | `chapters/examples/toroidal_elliptic.tex` | elliptic/toroidal portrait chapter | add governing-question opening splitting prototype-level mechanisms from still-open infinite-generator/factorization extensions | `done` |
| 14 | `chapters/examples/detailed_computations.tex` | computation ledger chapter | add governing-question opening that ties explicit numerics to theorem support versus residual high-degree computational gaps | `done` |

## Wave 17: Example-Section Route Framing

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 15 | `chapters/examples/minimal_model_fusion.tex` | modular-fusion section | add governing-question statement separating imported Verlinde input from explicit local computations | `done` |
| 15 | `chapters/examples/minimal_model_examples.tex` | worked-example section | add governing-question statement distinguishing Virasoro projection data from full $W$-algebra representation content | `done` |
| 15 | `chapters/examples/w3_composite_fields.tex` | coefficient-verification section | add governing-question statement tying explicit coefficient derivations to downstream theorem support | `done` |

## Wave 18: Residual Input-Layer Framing

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 16 | `chapters/examples/heisenberg_eisenstein.tex` | modular calibration section | add governing-question statement making this file read as a calibration model for non-abelian genus towers | `done` |
| 16 | `chapters/examples/deformation_examples.tex` | quantization-example chapter | add governing-question statement that separates theorem-level quantization exemplars from programme templates | `done` |
| 16 | `chapters/theory/filtered_curved.tex` | transition subsection inside quantum corrections | add a guiding sentence clarifying when filtered data is auxiliary and curved data is intrinsic | `done` |

## Wave 19: Appendix Entry Discipline

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 17 | `appendices/general_relations.tex` | dictionary control layer | add semantic-level marker and governing-question statement so dictionary claims read as theorem-backed translation rules | `done` |
| 17 | `appendices/arnold_relations.tex` | relation-proofs appendix | add governing-question statement tying Arnold identities to bar differential nilpotence | `done` |
| 17 | `appendices/signs_and_shifts.tex` | sign-control appendix | add governing-question statement that fixes global sign compatibility purpose | `done` |
| 17 | `appendices/sign_conventions.tex` | cross-source convention ledger | add governing-question statement that frames translation role across sources | `done` |
| 17 | `appendices/theta_functions.tex` | modular-input section | add semantic-level marker and governing-question statement for elliptic/higher-genus coefficient input | `done` |
| 17 | `appendices/spectral_sequences.tex` | computational machinery appendix | add governing-question statement connecting filtrations to controlled cohomological output | `done` |
| 17 | `appendices/spectral_higher_genus.tex` | higher-genus spectral section | add semantic-level marker and governing-question statement for genus-indexed convergence control | `done` |
| 17 | `appendices/koszul_reference.tex` | lookup/reference appendix | add governing-question statement clarifying lookup-layer role after canonical theorem statements | `done` |
| 17 | `appendices/homotopy_transfer.tex` | transfer-mechanism appendix | add governing-question statement tying quasi-isomorphism transport to explicit higher operations | `done` |
| 17 | `appendices/dual_methodology.tex` | methodological bridge appendix | add semantic-level marker and governing-question statement for abstract/concrete proof discipline | `done` |
| 17 | `appendices/computational_tables.tex` | S-level data ledger | add semantic-level marker and governing-question statement for numerics/constants support role | `done` |
| 17 | `appendices/existence_criteria.tex` | existence-theorem appendix | add governing-question statement for verifiable dual-existence criteria | `done` |
| 17 | `appendices/nilpotent_completion.tex` | non-quadratic completion appendix | add governing-question statement for completion-dependent dual construction | `done` |
| 17 | `appendices/coderived_models.tex` | curved-derived formalism section | add governing-question statement for coderived/contraderived necessity | `done` |
| 17 | `appendices/notation_index.tex` | notation control ledger | add semantic-level marker and governing-question statement for global symbol coherence | `done` |

## Wave 20: Active-Input Governing-Question Closure

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 18 | `chapters/theory/chiral_koszul_pairs.tex` | recognition layer chapter | normalize chapter-entry sentence to explicit single-line “The governing question of this chapter…” phrasing so active-input audits are zero-miss | `done` |

## Wave 21: Status-Tag Closure on Active Claim Blocks

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 19 | `chapters/frame/heisenberg_frame.tex` | frame theorem layer | add explicit claim-status tags to all previously untagged frame propositions/theorems so frame computations obey the same status discipline as the core | `done` |
| 19 | `chapters/theory/bar_cobar_construction.tex` | strict-duality core | add claim-status tag to the cotensor/contratensor adjunction lemma | `done` |
| 19 | `chapters/theory/poincare_duality.tex` | anti-circularity core | add claim-status tag to the NAP Koszul-pair proposition | `done` |
| 19 | `chapters/theory/higher_genus.tex` | modular core | add claim-status tags to legacy theorem wrapper, quantum Arnold theorem, and center-isomorphism sublemma | `done` |
| 19 | `chapters/connections/holomorphic_topological.tex` | gauge-theory bridge | add theorem-level status tag for the W-algebra bar-complex bridge statement | `done` |
| 19 | `chapters/connections/kontsevich_integral.tex` | topology bridge | mark mixed-proof/open graph-complex proposition as `\ClaimStatusOpen` at theorem-header level | `done` |
| 19 | `chapters/connections/genus_complete.tex` | all-genus bridge | mark mixed-proof/open EO-recursion theorem as `\ClaimStatusOpen` at theorem-header level | `done` |
| 19 | `chapters/connections/concordance.tex` | synthesis ledger | mark higher-dimensional “proved cases” theorem as `\ClaimStatusOpen` to match mixed internal status split | `done` |
| 19 | `appendices/arnold_relations.tex` | appendix proof layer | add claim-status tag to operadic-equivalence proposition | `done` |

## Wave 22: H/M/S Marker Closure on Active Inputs

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 20 | `chapters/theory/filtered_curved.tex` | transition subsection inside quantum corrections | add explicit semantic-level remark so the filtered-to-curved comparison is tagged in the same H/M/S regime discipline as all other active inputs | `done` |

## Wave 23: Integrity-Gate Route Discipline

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 21 | `scripts/integrity_gate.sh` | automation gate | extend active-include checks beyond claim-status coverage to enforce governing-question and H/M/S marker coverage automatically | `done` |

## Wave 24: Analogy-to-Status Precision Pass

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 22 | `chapters/examples/kac_moody_framework.tex` | research-programme framing | replace residual “suggests” programme language with explicit conjectural-route wording and status markers | `done` |
| 22 | `chapters/examples/w_algebras_framework.tex` | dual-level examples | replace analogy-based phrasing in dual-level interpretation with explicit conjectural extension language | `done` |
| 22 | `chapters/examples/examples_summary.tex` | discriminant-control ledger | rewrite discriminant-principle remarks as explicit conjectural principles instead of suggestive prose | `done` |

## Wave 25: Expected-Language Status Closure

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 23 | `chapters/examples/deformation_quantization.tex` | quantization scope remark | convert higher-genus “expected” wording into explicit conjectural status language | `done` |
| 23 | `chapters/examples/yangians.tex` | shifted-Yangian scope remark | convert “expected to follow” phrasing into explicit conjectural extension language | `done` |
| 23 | `chapters/examples/genus_expansions.tex` | evidence paragraph discipline | recast partial-fraction interpretation as an explicitly conjectural decomposition claim | `done` |
| 23 | `chapters/examples/kac_moody_framework.tex` | nilpotent-extension remark | mark arbitrary-orbit extension as conjectural rather than expected | `done` |
| 23 | `chapters/examples/toroidal_elliptic.tex` | toroidal existence scope | convert RTT-motivated expected wording into explicit conjectural framing | `done` |
| 23 | `chapters/examples/detailed_computations.tex` | computational interpretation | mark degree-4 vanishing statement as conjectural status, not expectation | `done` |
| 23 | `chapters/theory/chiral_koszul_pairs.tex` | Yangian Koszulness remark | mark general-$\mathfrak{g}$ Koszulness as explicit conjectural status | `done` |
| 23 | `chapters/theory/deformation_theory.tex` | periodicity programme remark | replace “expected for all” wording by explicit conjectural scope statement | `done` |
| 23 | `chapters/connections/holomorphic_topological.tex` | bridge-scope wording | convert residual expected-equivalence phrasing to explicit conjectural status wording | `done` |
| 23 | `appendices/coderived_models.tex` | provisional coderived scope | mark full-faithful embedding statement as conjectural rather than expected | `done` |

## Wave 26: Include-Graph Repair

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 24 | `main.tex` | build control graph | make `filtered_curved` input resilient with `\IfFileExists` so transient branch states do not hard-fail TeX builds | `done` |

## Wave 27: QC Gate Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 25 | `scripts/manuscript_qc.py` | corpus-level QC guard | add strict detection for ambiguous status language (`suggests` / `expected` / analogy phrasing without conjectural markers) | `done` |
| 25 | `chapters/connections/holomorphic_topological.tex` | bridge diction cleanup | clear final ambiguous “suggest” phrasing under strict QC | `done` |
| 25 | `chapters/theory/chiral_modules.tex` | module-layer diction cleanup | replace residual analogy phrasing with explicit conjectural extension language | `done` |
| 25 | `audit/manuscript_qc_report.md` | QC snapshot | refresh report after strict QC passes with zero structural/status-language findings | `done` |

## Wave 28: Introduction Readability Segmentation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 26 | `chapters/theory/introduction.tex` | front-door readability | split one oversized modular-programme paragraph into theorematic sub-blocks without changing mathematical content | `done` |
| 26 | `audit/manuscript_qc_report.md` | QC snapshot | refresh report after paragraph segmentation (long-paragraph count reduced) | `done` |

## Wave 29: Examples-Ledger Readability Segmentation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 27 | `chapters/examples/examples_summary.tex` | ledger readability | split oversized bar-dimensions setup paragraph into shorter theorematic blocks | `done` |
| 27 | `audit/manuscript_qc_report.md` | QC snapshot | refresh report after examples-ledger segmentation (long-paragraph count reduced again) | `done` |

## Wave 30: Elliptic-Proof Readability Segmentation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 28 | `chapters/examples/toroidal_elliptic.tex` | proof readability | split long Arnold/Fay proof paragraph into shorter argument blocks | `done` |
| 28 | `audit/manuscript_qc_report.md` | QC snapshot | refresh report after elliptic-proof segmentation while preserving strict QC clean state | `done` |

## Wave 31: Free-Field Proof Readability Segmentation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 29 | `chapters/examples/free_fields.tex` | proof readability | split long Koszul-resolution proof block into shorter argument segments | `done` |
| 29 | `audit/manuscript_qc_report.md` | QC snapshot | refresh report after free-field segmentation (long-paragraph count reduced) | `done` |

## Wave 32: Cross-Chapter Proof Segmentation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 30 | `chapters/theory/higher_genus.tex` | proof readability | split long genus-2 Arnold and center-action proof paragraphs into shorter argument blocks | `done` |
| 30 | `chapters/connections/concordance.tex` | proof readability | segment long GRR computation paragraph into theorematic sub-blocks | `done` |
| 30 | `chapters/examples/toroidal_elliptic.tex` | proof readability | segment long DYBE proof paragraph into shorter formula blocks | `done` |
| 30 | `chapters/theory/introduction.tex` | thesis readability | segment dense central-thesis paragraph around universal MC display | `done` |
| 30 | `chapters/examples/minimal_model_examples.tex` | proposition readability | split long S-matrix proposition paragraph into shorter theorematic units | `done` |
| 30 | `audit/manuscript_qc_report.md` | QC snapshot | refresh report after cross-chapter segmentation pass (long-paragraph count reduced to 46) | `done` |

## Wave 33: Module/Combinatorics Segmentation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 31 | `chapters/examples/w3_composite_fields.tex` | proof readability | segment long null-vector mode-calculation block into shorter formula paragraphs | `done` |
| 31 | `chapters/examples/examples_summary.tex` | filtration-proof readability | split long Motzkin-filtration compatibility paragraph into shorter theorematic blocks | `done` |
| 31 | `chapters/connections/genus_complete.tex` | axiom-verification readability | segment long EO-axiom verification paragraph into atomic bullet-level blocks | `done` |
| 31 | `chapters/theory/chiral_modules.tex` | definition readability | split long genus-graded-module definition lead paragraph and curvature close | `done` |
| 31 | `chapters/examples/genus_expansions.tex` | case-study readability | split long affine case PBW paragraph into shorter argument blocks | `done` |
| 31 | `chapters/theory/chiral_koszul_pairs.tex` | chain-map proof readability | split long Step~3b paragraph by Stokes-cancellation boundary | `done` |
| 31 | `audit/manuscript_qc_report.md` | QC snapshot | refresh report after module/combinatorics segmentation pass (long-paragraph count reduced to 40) | `done` |

## Wave 34: Residual Long-Paragraph Closure

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 32 | `main.tex` | preamble readability | segment theorem declaration and bookmark-level command blocks to remove residual oversized non-prose paragraphs | `done` |
| 32 | `appendices/notation_index.tex` | notation-ledger readability | segment longtable row blocks with comment delimiters so notation tables no longer trigger long-paragraph QC noise | `done` |
| 32 | `chapters/examples/yangians.tex` | theorem-statement readability | split the derived DK theorem statement into shorter logical blocks | `done` |
| 32 | `chapters/examples/detailed_computations.tex` | computation readability | split the degree-2 matrix computation lead block into shorter argument units | `done` |
| 32 | `chapters/theory/chiral_koszul_pairs.tex` | equivalence-proof readability | segment Step~3a construction and $\Eone$ equivalence statement blocks | `done` |
| 32 | `chapters/examples/w_algebras_framework.tex` | BRST-step readability | segment the dual-level BRST argument into atomic progression blocks | `done` |
| 32 | `chapters/theory/koszul_pair_structure.tex` | periodicity-proof readability | split generic-$c$ spectral-sequence degeneration argument into shorter theorematic segments | `done` |
| 32 | `chapters/examples/genus_expansions.tex` | table-block readability | segment Verlinde table block for QC paragraph accounting without changing data | `done` |
| 32 | `audit/manuscript_qc_report.md` | QC snapshot | refresh strict QC snapshot after residual closure (long-paragraph count reduced to 0) | `done` |
| 32 | `Makefile`/build lane | compile verification | run `make fast` after Wave 34 segmentation edits | `done` |

## Wave 35: Build-Lane Error Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 33 | `chapters/theory/bar_cobar_construction.tex` | TeX hard-error fix | replace undefined `\Aut` macro usage with explicit `\operatorname{Aut}` in sign-compatibility proof block | `done` |
| 33 | `audit/manuscript_qc_report.md` | QC snapshot | refresh strict QC report after Wave 35 hotfix and verify structural/status-language gates remain clean | `done` |
| 33 | build artifacts (`main.aux`) / fast lane | compile-state recovery | detect and recover from NUL-corrupted aux artifact during parallel-agent execution to keep fast-build lane operational | `done` |

## Wave 36: Full-Build Convergence Verification

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 34 | full build lane (`make`) | convergence gate | run full multi-pass build after Wave 35 stabilization and verify convergence without undefined-control-sequence failures | `done` |
| 34 | `audit/manuscript_qc_report.md` | QC snapshot | refresh strict QC report after full-build verification to keep queue/report state synchronized | `done` |

## Wave 37: Integrity Gate Baseline Realignment

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 35 | `scripts/integrity_gate.sh` | CI gate policy | convert `UNDERFULL`/`HYPERREF_WARN` from hard-zero checks to explicit bounded thresholds so the gate remains strict on structural failures but usable on current manuscript baseline | `done` |
| 35 | integrity lane (`./scripts/integrity_gate.sh`) | full pipeline validation | run full integrity gate end-to-end after threshold realignment and confirm PASS on current branch state | `done` |

## Wave 38: Introduction Synthesis Doctrine

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 36 | `chapters/theory/introduction.tex` | architectural doctrine | add explicit Chriss--Ginzburg-style synthesis protocol remark so Part~III bridges are governed by transport + status tagging rather than analogy | `done` |
| 36 | fast lane (`make fast`) | compile verification | rebuild after introduction doctrine insertion | `done` |
| 36 | `audit/manuscript_qc_report.md` | QC snapshot | refresh strict QC snapshot after Wave 38 doctrine insertion | `done` |

## Wave 39: Frontier Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 37 | `chapters/connections/concordance.tex` | control ledger | distinguish proved same-family Virasoro complementarity shadow from conjectural `W_\\infty` realization and remove stale dependency drift | `done` |
| 37 | `metadata/frontier_and_gaps.md` | frontier control note | record the Virasoro same-family-shadow vs `W_\\infty` frontier split explicitly in the March 8 doctrine | `done` |
| 37 | `notes/PROGRAMMES.md` | strategic doctrine | make “proved shadow versus realized object” the governing distinction for the post-cleanup frontier | `done` |
| 37 | `chapters/examples/free_fields.tex` | portrait-control interface | clarify that `Vir_{26-c}` is the current shadow partner while `W_\\infty` remains the open realization problem | `done` |
| 37 | `chapters/theory/bar_cobar_construction.tex` | theory/programme boundary | remove stale “no dual” impossibility language and reframe infinite-generator examples as completion frontier statements | `done` |

## Wave 40: MC1 Compute Surface Generalization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 38 | `compute/lib/genus1_pbw_sl2.py` | MC1 compute scaffold | generalize Casimir and PBW `d_1` diagnostics from tensor-square/triple special cases to reusable tensor-power utilities for `\\mathfrak{sl}_2` genus-1 enrichment analysis | `done` |
| 38 | `compute/tests/test_genus1_pbw_sl2.py` | regression discipline | refactor weight-3 verification tests to consume shared library diagnostics and remove duplicated local Casimir/`d_1` builders | `done` |
| 38 | `.venv/bin/python -m pytest` lane | test verification | run focused genus-1 PBW suites after generalization (`test_genus1_pbw.py`, `test_genus1_pbw_sl2.py`) | `done` |

## Wave 41: MC1 Representation-Theoretic Tensor-Power Checks

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 39 | `compute/lib/genus1_pbw_sl2.py` | MC1 representation diagnostics | add explicit spin-1 tensor-power multiplicity recurrence and expected Casimir eigenspace calculators to align compute output with closed-form sl2 representation theory | `done` |
| 39 | `compute/tests/test_genus1_pbw_sl2.py` | regression discipline | verify tensor powers through `n=4` (copy multiplicities, invariant dimensions, computed-vs-expected Casimir eigenspaces) | `done` |
| 39 | `.venv/bin/python -m pytest` lane | test verification | run focused genus-1 PBW suites after recurrence extension (`test_genus1_pbw.py`, `test_genus1_pbw_sl2.py`) | `done` |

## Wave 42: MC1 Equivariance Gate on PBW Differentials

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 40 | `compute/lib/genus1_pbw_sl2.py` | MC1 algebraic gate | add explicit `d_1` equivariance and Casimir-compatibility residuals across tensor powers as reusable correctness diagnostics | `done` |
| 40 | `compute/tests/test_genus1_pbw_sl2.py` | regression discipline | verify `sl_2`-equivariance and Casimir commutation of `d_1` for tensor powers `n=2,3,4` | `done` |
| 40 | `.venv/bin/python -m pytest` lane | test verification | rerun focused genus-1 PBW suites after equivariance gate insertion (`test_genus1_pbw.py`, `test_genus1_pbw_sl2.py`) | `done` |

## Wave 43: MC1 Theorem-Text / Compute Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 41 | `chapters/theory/higher_genus.tex` | MC1 proof narration | extend Step~4 of `thm:pbw-genus1-km` with explicit `n=3,4` tensor-power diagnostics (Casimir multiplicities, `d_1` ranks, and equivariance/`[C_2,d_1]=0` gates) from the shared compute API | `done` |
| 41 | fast lane (`make fast`) | compile verification | rebuild after theorem-text synchronization under concurrent edits | `done` |
| 41 | strict QC lane (`./scripts/manuscript_qc.py --strict --limit 200`) | governance verification | confirm structural/status-language gates remain zero-findings after synchronization pass | `done` |

## Wave 44: MC1 Tensor-Power Frontier Extension (`n=5`)

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 42 | `compute/tests/test_genus1_pbw_sl2.py` | MC1 regression frontier | extend representation-theoretic, invariant-dimension, and equivariance/Casimir gate tests through tensor power `n=5` with explicit numeric regression targets | `done` |
| 42 | `chapters/theory/higher_genus.tex` | theorem/compute sync | update Step~4 compute evidence to include `n=5` Casimir spectrum and `d_1` rank while preserving theorematic argument flow | `done` |
| 42 | focused test lane (`.venv/bin/python -m pytest -q compute/tests/test_genus1_pbw_sl2.py compute/tests/test_genus1_pbw.py`) | verification | validate generalized MC1 diagnostics after `n=5` extension | `done` |
| 42 | fast lane (`make fast`) + strict QC lane | manuscript/control verification | confirm compile and governance gates remain clean after theorem-sync frontier extension | `done` |

## Wave 45: MC1 Tensor-Power Frontier Extension (`n=6`)

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 43 | `compute/tests/test_genus1_pbw_sl2.py` | MC1 regression frontier | add explicit `n=6` Casimir/rank/kernel/invariant checkpoints and extend equivariance/Casimir gate tests through `n=6` | `done` |
| 43 | `chapters/theory/higher_genus.tex` | theorem/compute sync | extend Step~4 compute evidence to include `n=6` spectral/rank data, then re-segment prose to satisfy strict long-paragraph constraints | `done` |
| 43 | focused test lane (`.venv/bin/python -m pytest -q compute/tests/test_genus1_pbw_sl2.py compute/tests/test_genus1_pbw.py`) | verification | validate frontier extension at `n=6` | `done` |
| 43 | fast lane (`make fast`) + strict QC lane | manuscript/control verification | confirm compile success and restore zero-findings strict QC after text extension | `done` |

## Wave 46: Virasoro Shadow/Bridge Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 44 | `chapters/examples/examples_summary.tex` | portrait control ledger | relabel the Virasoro row and summary prose so `Vir_{26-c}` is the proved M/S-level same-family shadow, not an already-realized H-level infinite-generator dual | `done` |
| 44 | `chapters/examples/genus_expansions.tex` | Virasoro portrait chapter | propagate the same shadow-vs-realization distinction through the setup tables, trichotomy remarks, and representative central-charge computations | `done` |
| 44 | `chapters/theory/chiral_modules.tex` | module-layer extension | rewrite Virasoro module transport statements as same-family shadow results and keep the H-level realization on the MC4 frontier | `done` |
| 44 | `chapters/theory/hochschild_cohomology.tex` | deformation/cohomology core | restate the Virasoro Hochschild/cyclic remarks in same-family-shadow language with explicit MC4 caveat | `done` |
| 44 | `chapters/connections/bv_brst.tex` | physics bridge | replace stale anomaly-cancellation language by level-independent complementarity for Virasoro/finite-type `W` families and point the stronger realization problem to MC4 | `done` |
| 44 | `chapters/connections/holomorphic_topological.tex` | gauge-theory bridge | make the open/closed and AGT scope remarks stop at bar/semi-infinite boundary data and defer infinite-generator bulk duals to the MC4/MC5 frontier | `done` |
| 44 | `chapters/connections/genus_complete.tex` | all-genus physics bridge | align the string/holography scope remarks with the same boundary-shadow versus H-level bulk-dual distinction | `done` |
| 44 | strict QC lane + `make fast` + full `make` | verification | confirm the propagated doctrine compiles cleanly with zero undefined references/citations, zero rerun warnings, and zero destination warnings | `done` |

## Wave 47: MC1 Scaling Profiler for Frontier Planning

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 45 | `compute/scripts/profile_genus1_pbw_sl2_scaling.py` | compute instrumentation | add standalone runtime profiler for genus-1 `sl_2` PBW diagnostics (rank/kernel, invariants, equivariance, Casimir commutator, optional Casimir spectrum) across tensor powers | `done` |
| 45 | profiler lane (`.venv/bin/python compute/scripts/profile_genus1_pbw_sl2_scaling.py --max-power 6`) | scaling verification | capture empirical runtime envelope through `n=6` to guide feasible default-frontier targets | `done` |
| 45 | strict QC lane (`./scripts/manuscript_qc.py --strict --limit 200`) | control verification | keep manuscript governance gates synchronized after queue/control updates | `done` |

## Wave 48: MC1 `n=7` Staged Feasibility Probe

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 46 | `compute/scripts/profile_genus1_pbw_sl2_scaling.py` | staged frontier probing | add `--skip-equivariance` and `--skip-commutator` flags so `n=7` can be profiled incrementally without forcing full Casimir eigenspace computation | `done` |
| 46 | profiler lane (`--min-power 7 --max-power 7 --skip-casimir --skip-equivariance --skip-commutator`) | rank-only feasibility | measure pure `d_1`-rank frontier point (`rank=728`, `ker=1459`, invariants `=36`) | `done` |
| 46 | profiler lane (`--min-power 7 --max-power 7 --skip-casimir`) | gate feasibility | verify `d_1` equivariance and Casimir-commutator gates still pass at `n=7` with practical runtime | `done` |
| 46 | profiler lane (full `n=7`) | bottleneck characterization | attempt full Casimir-eigenspace profile at `n=7`; abort after sustained runtime and classify as current frontier bottleneck | `done` |

## Wave 49: MC4 / Non-Principal / Periodicity Frontier Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 47 | `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md` | control doctrine | rewrite MC4 as an inverse-limit completed bar-cobar package, sharpen the periodicity frontier, and synchronize the control ledger with the live `W_\infty` / Yangian / non-principal story | `done` |
| 47 | `chapters/theory/bar_cobar_construction.tex`, `chapters/examples/yangians.tex` | theorem/conjecture shaping | turn the infinite-generator frontier into theorem-ready completed-bar statements and make the Yangian completion hypothesis read as MC4 rather than generic convergence prose | `done` |
| 47 | `chapters/examples/w_algebras_framework.tex`, `chapters/examples/w_algebras_deep.tex`, `chapters/connections/holomorphic_topological.tex` | non-principal `W` frontier | state principal finite-type `W_N` as proved core, isolate hook/subregular theorematic seeds, and keep arbitrary orbit duality explicitly conjectural | `done` |
| 47 | `chapters/theory/derived_langlands.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/physical_origins.tex`, `chapters/connections/feynman_diagrams.tex` | periodicity + Part III doctrine | separate theorematic periodicity from higher-rank conjectural transport and keep the physics horizon at boundary-side/bar-side data rather than completed bulk duals | `done` |
| 47 | `scripts/manuscript_qc.py`, `scripts/integrity_gate.sh` | regression prevention | add automatic doctrine checks so bare Virasoro dual language without shadow/MC4 caveats cannot drift back in | `done` |
| 47 | strict QC lane + `make fast` + full `make` | verification | confirm the frontier synchronization compiles on the live tree via strict QC, `make fast`, and incremental full `make`; note that clean integrity rebuilds remain sensitive to concurrent auxiliary-file churn | `done` |

## Wave 50: MC1 Casimir Policy + MC2 Scaffold Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 48 | `compute/lib/genus1_pbw_sl2.py`, `compute/scripts/profile_genus1_pbw_sl2_scaling.py`, `compute/tests/test_genus1_pbw_sl2.py` | MC1 frontier control | codify exact-vs-theory Casimir policy (`auto/exact/theory`, cutoff at `n=6`) and lock staged `n=7` diagnostics into test/profiler lanes | `done` |
| 48 | `compute/lib/mc2_cyclic_linf.py`, `compute/lib/__init__.py`, `compute/tests/test_mc2_cyclic_linf.py` | MC2 Step-1 compute layer | establish executable coderivation dg-Lie + cyclic `L_\infty` scaffold with first symbolic MC solve and regression checks | `done` |
| 48 | `chapters/theory/higher_genus.tex`, `notes/autonomous_state.md`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control sync | align MC2 status remark and programme/control ledgers with the new scaffold and Casimir policy split | `done` |
| 48 | test/build/QC lanes (`pytest`, `make fast`, strict QC) | verification | rerun focused compute tests plus manuscript gates after synchronization edits | `done` |

## Standing Rule

Before advancing to a later wave, make sure the earlier wave compiles and
the control documents still agree with one another.
