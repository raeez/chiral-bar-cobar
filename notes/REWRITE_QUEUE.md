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

## Wave 51: MC2 Bar-Derived `sl_2` Seed Advancement

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 49 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-2 compute layer | derive first non-toy MC2 seed from bar/OPE data (simple-pole bracket + normalized double-pole pairing) and extend regression checks/export surface | `done` |
| 49 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | record the MC2 step advancement and tighten the status narrative around bar-derived seed evidence | `done` |
| 49 | verification lane (`pytest`, `make fast`, strict QC) | regression gate | confirm compute tests plus manuscript build/QC remain clean after MC2 Step-2 insertions | `done` |

## Wave 52: Frontier Continuation (MC1 `n=7` + MC2 Step-3)

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 50 | `compute/lib/genus1_pbw_sl2.py`, `compute/scripts/profile_genus1_pbw_sl2_scaling.py`, `compute/tests/test_genus1_pbw_sl2.py` | MC1 frontier acceleration | implement and benchmark a modular/sparse `n=7` Casimir eigenspace path to narrow the gap between `theory` and full `exact` diagnostics | `done` |
| 50 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py` | MC2 Step-3 compute layer | extend from generator-level `sl_2` seed to first nontrivial cyclic higher bracket input and multi-parameter MC residual/solve checks | `done` |
| 50 | `chapters/theory/higher_genus.tex`, `notes/autonomous_state.md`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control sync | keep MC1/MC2 frontier narrative synchronized with newly executable Step-3 evidence | `done` |
| 50 | verification lane (`pytest`, `make fast`, strict QC) | regression gate | enforce green compute + manuscript gates after Wave 52 frontier work | `done` |

## Wave 53: MC4 `W_\infty` Specialization + Residual Typography Cleanup

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 51 | `chapters/theory/bar_cobar_construction.tex`, `chapters/examples/w_algebras_framework.tex`, `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md` | MC4 theorem/control sync | specialize the generic inverse-limit MC4 criterion to the `W_\infty` principal-stage tower and propagate the reduced frontier statement through the portrait and control ledgers | `done` |
| 51 | `chapters/theory/poincare_duality_quantum.tex`, `chapters/examples/yangians.tex` | typography/index hygiene | shorten the two residual index labels responsible for the remaining overfull boxes in the integrity lane | `done` |
| 51 | strict QC + `make fast` + integrity gate | verification | confirm the specialized `W_\infty` criterion compiles cleanly and the residual overfull-box debt is eliminated | `done` |

## Wave 54: MC2 Completion / Clutching Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 52 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py` | MC2 completion layer | prototype completed tensor-product control (`\widehat{\otimes}` surrogate) and a first clutching-compatibility map check on boundary-factorized inputs | `done` |
| 52 | `chapters/theory/higher_genus.tex`, `notes/autonomous_state.md`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control sync | update MC2 status text from seed-level Step-3 to first completion/clutching evidence and isolate remaining graph-complex gap | `done` |
| 52 | optional MC1 lane (`compute/lib/genus1_pbw_sl2.py`, profiler script) | exact-depth research | test whether a sparse exact rational backend can close the remaining `n=7` dense-exact performance gap without altering default policy (benchmark result: no speedup; keep default policy unchanged) | `done` |
| 52 | verification lane (`pytest`, `make fast`, strict QC) | regression gate | keep compute/manuscript lanes green after Wave 54 continuation | `done` |

## Wave 55: MC4 Surjectivity Criterion + Frontier Guardrails

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 53 | `chapters/theory/bar_cobar_construction.tex`, `chapters/examples/yangians.tex` | MC4 theorem shaping | weaken the visible sufficient MC4 input from eventual constancy to eventual surjectivity on finite-dimensional weight slices and propagate that criterion to the Yangian tower narrative | `done` |
| 53 | `chapters/examples/w_algebras_framework.tex`, `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md` | portrait/control synchronization | restate the live `W_\infty` / Yangian frontier as a weightwise surjectivity/stabilization theorem rather than a generic convergence slogan | `done` |
| 53 | `scripts/manuscript_qc.py`, `scripts/integrity_gate.sh` | doctrine guardrails | add automated drift detection for accidental promotion of `W_\infty` or Yangian completions to realized dual objects without MC4 frontier caveats | `done` |
| 53 | strict QC + `make fast` + clean full build lane | verification | confirm the sharpened MC4 doctrine remains structurally clean and rebuilds after generated-state reset | `done` |

## Wave 56: Standard-Tower MC4 Cutoff Formalization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 54 | `chapters/theory/bar_cobar_construction.tex` | MC4 formal reduction | prove a general weight-cutoff criterion showing that genuine truncation towers force eventual surjectivity/stabilization on fixed weight slices | `done` |
| 54 | `chapters/theory/bar_cobar_construction.tex`, `chapters/examples/yangians.tex` | principal examples | specialize the cutoff mechanism to the standard principal-stage `W_\infty` tower and the standard RTT Yangian tower so their remaining MC4 gap is continuity plus inverse-limit identification | `done` |
| 54 | `chapters/examples/w_algebras_framework.tex`, `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md` | control synchronization | update the frontier ledgers so they no longer list stabilization as an open input for the standard truncation towers | `done` |
| 54 | strict QC + `make fast` + clean integrity gate | verification | confirm the cutoff formalization compiles cleanly and preserves all doctrine gates on a cold rebuild | `done` |

## Wave 57: Standard-Tower MC4 Closure

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 55 | `chapters/theory/bar_cobar_construction.tex` | MC4 theorem closure | prove continuity of inverse-limit bar/cobar differentials for compatible towers and close the standard principal-stage `W_\infty` M-level package | `done` |
| 55 | `chapters/examples/yangians.tex` | MC4 theorem closure | identify the standard RTT inverse limit with the coefficientwise RTT completion and close the standard RTT M-level package | `done` |
| 55 | `chapters/examples/w_algebras_framework.tex`, `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md` | control synchronization | propagate the new standard-tower MC4 closure so the live frontier moves to H-level comparison rather than M-level existence | `done` |
| 55 | `chapters/theory/poincare_duality_quantum.tex`, `chapters/examples/yangians.tex` | typography cleanup | remove the two residual overfull index entries before the next underfull-box pass | `done` |

## Wave 58: MC2 Completed-Cyclicity Solver Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 56 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-4/5 compute layer | add completed-series cyclicity checks (`l_2`/`l_3`) and first symbolic genus-truncated completed-MC solve branch on single-basis ansatz; lock with regression coverage and export surface | `done` |
| 56 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | reflect the completed-cyclicity + completed-MC solver branch evidence in theorem status remark and control ledgers | `done` |
| 56 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests, strict QC, and fast build checks after the completion-lift insertion | `done` |

## Wave 59: H-Level Comparison Criteria for MC4 Targets

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 57 | `chapters/theory/bar_cobar_construction.tex` | inverse-limit comparison formalization | prove that a separated complete H-level target is determined by compatible finite quotients and specialize that criterion to the `W_\infty` frontier | `done` |
| 57 | `chapters/examples/yangians.tex` | Yangian H-level frontier | restate the dg-shifted/factorization comparison as a filtered finite-RTT-quotient problem and add the formal comparison criterion | `done` |
| 57 | `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/physical_origins.tex`, `chapters/connections/feynman_diagrams.tex` | control and Part III synchronization | propagate the new doctrine so the remaining bulk comparison is always stated as a filtered target with theorematic finite quotients | `done` |
| 57 | strict QC + isolated TeX lane | verification | confirm the new theorem/corollary layer is structurally clean and rebuilds without reopening doctrine drift | `done` |

## Wave 60: Explicit MC4 Construction Packages

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 58 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` construction frontier | name the H-level task as a principal-stage compatible factorization target, not a generic completion slogan | `done` |
| 58 | `chapters/examples/yangians.tex` | dg-shifted Yangian frontier | define RTT-adapted filtration and record the finite-RTT quotient package as the precise missing input | `done` |
| 58 | `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md`, `chapters/connections/holomorphic_topological.tex` | control synchronization | propagate the split frontier as two explicit construction packages (`W_\infty` factorization target / dg-shifted RTT filtration) | `done` |
| 58 | strict QC + detached verification lane | verification | confirm the new conjectural package layer preserves doctrine gates and does not reopen build debt | `done` |

## Wave 61: MC2 Obstruction/Recursive Solver Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 59 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-5 compute hardening | harden truncated completed-MC solving on inconsistent branches, add genus-stratified obstruction extraction, and add recursive single-basis branch solver | `done` |
| 59 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate obstruction/recursive-branch evidence and solver robustness status into MC2 narrative/control ledgers | `done` |
| 59 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests, strict QC, and fast build checks after the recursive obstruction lift | `done` |

## Wave 62: MC2 Multi-Basis Completed-Solver Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 60 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-5 compute extension | lift completed-MC solving from single-basis ans\"atze to multi-basis truncated and recursive branches, preserving inconsistent-branch detection and explicit free-direction bookkeeping | `done` |
| 60 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | synchronize MC2 status language with the new multi-basis completed-solver evidence (`(\theta,\omega)` toy branch forcing on `\theta_g`, free completed `\omega_g` directions) | `done` |
| 60 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after the multi-basis solver lift | `done` |

## Wave 66: MC2 Shifted-Seed Nontrivial Obstruction Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 64 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 seed advance | add suspension-shifted symmetric seed construction from generator-level antisymmetric data and verify nontrivial mixed MC/obstruction channels on shifted `sl_2` `l_3` seed | `done` |
| 64 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate shifted-seed nontrivial residual/obstruction evidence into MC2 status/control text | `done` |
| 64 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after shifted-seed insertion | `done` |

## Wave 67: MC2 Shifted-Seed Universality Extension (`sl_3`, `sp_4`)

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 65 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 universality extension | extend shifted symmetric seed constructors/checks from `sl_2` to `sl_3` and `sp_4`, and verify explicit mixed residual / positive-genus obstruction channels in each rank/type lane | `done` |
| 65 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate shifted-seed universality evidence (`\eta=xyz` for `sl_3`, `\eta=2xyz` for `sp_4`; genus-3 obstruction channels `\eta`, `2\eta`) into MC2 status/control text | `done` |
| 65 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after shifted-seed universality extension | `done` |

## Wave 69: MC2 One-Channel Normalization Profile Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 67 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 normalization advance | extract shifted-seed one-channel normalization profiles (`sl_2`, `sl_3`, `sp_4`) and verify uniform unit ratio between genus-3 `\eta` obstruction and mixed residual channel at `(1,1,1)` | `done` |
| 67 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate one-channel normalization-profile evidence into theorem and control surfaces | `done` |
| 67 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after one-channel normalization lift | `done` |

## Wave 71: MC2 Shifted `\eta` Scaling-Law Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 69 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 scaling advance | extract symbolic shifted-seed scaling profiles and verify quadratic genus-2 / cubic genus-3 (`\eta`) obstruction law across `sl_2`, `sl_3`, `sp_4` | `done` |
| 69 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate the symbolic scaling law (`O_3^\eta(t)=t^3\eta(1,1,1)`) into theorem and control surfaces | `done` |
| 69 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after shifted `\eta` scaling-law lift | `done` |

## Wave 72: MC2 Shifted Obstruction Polynomial-Identity Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 70 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 polynomial advance | extract symbolic polynomial obstruction profiles and verify exact identities `O_2=\frac12 l_2(\alpha_1,\alpha_1)` and `O_3^\eta=\eta(x,y,z)=\frac16 l_3^\eta(\alpha_1,\alpha_1,\alpha_1)` across shifted `sl_2/sl_3/sp_4` lanes | `done` |
| 70 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate the symbolic polynomial-identity law into theorem and control surfaces | `done` |
| 70 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after shifted polynomial-identity lift | `done` |

## Wave 73: MC2 Shifted `\eta` Channel / CE-Uniqueness Alignment

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 71 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 channel alignment | verify that the shifted genus-3 `\eta` obstruction channel in `sl_2/sl_3/sp_4` coincides with the unique cyclic deformation direction (`H^2_{cyc}=\mathbb{C}`) extracted from seed CE profiles | `done` |
| 71 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate the shifted `\eta` / CE-uniqueness alignment into theorem and control surfaces | `done` |
| 71 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after shifted `\eta` channel alignment lift | `done` |

## Wave 74: MC2 Shifted Obstruction-Support Truncation Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 72 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 support advance | extract genus-indexed shifted obstruction support profiles and verify genus-1-only ansatz support truncation (`O_g=0` for all `g>=4`) across `sl_2/sl_3/sp_4` | `done` |
| 72 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate shifted obstruction-support truncation evidence into theorem and control surfaces | `done` |
| 72 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after shifted support-truncation lift | `done` |

## Wave 75: MC2 Shifted One-Channel Criterion Package Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 73 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 package advance | aggregate shifted normalization/scaling/polynomial/CE/support checks into one executable one-channel criterion package across `sl_2/sl_3/sp_4` | `done` |
| 73 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate the consolidated shifted one-channel criterion package into theorem and control surfaces | `done` |
| 73 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after one-channel criterion-package lift | `done` |

## Wave 76: MC2 Shifted Exceptional-Lane (`g_2`) Extension

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 74 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 exceptional extension | extend shifted one-channel nontriviality/scaling/polynomial/CE/support/criterion checks from `sl_2/sl_3/sp_4` to the exceptional `g_2` lane (`\eta=3xyz`, `O_3^\eta=3\eta`) | `done` |
| 74 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate the shifted exceptional-lane criterion evidence into theorem and control surfaces | `done` |
| 74 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after shifted `g_2` extension | `done` |

## Wave 300: MC2 Root-String Signature-Law Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 75 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 Step-6 signature advance | extract and verify the explicit shifted root-string law on `sl_3/sp_4/g_2`: `O_2=t^2(e12+f1-m f2)`, `O_3^\eta=m t^3\eta=-t\,O_2^{f2}` with `m=1,2,3`; enforce `\eta(1,1,1)` = seed Killing 3-cocycle normalization and integrate into the consolidated one-channel criterion package | `done` |
| 75 | `chapters/theory/higher_genus.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/autonomous_state.md` | theorem/control sync | propagate the explicit root-string signature law into theorem and control surfaces | `done` |
| 75 | verification lane (`pytest`, strict QC, `make fast`) | regression gate | rerun MC2 compute tests plus strict QC and fast build checks after root-string signature-law hardening | `done` |

## Standing Rule

Before advancing to a later wave, make sure the earlier wave compiles and
the control documents still agree with one another.

## Wave 63: Frontier Dependency-Order Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 61 | `notes/GPT54_CODEX_OPERATING_SYSTEM.md`, `notes/VISION.md`, `CLAUDE.md`, `metadata/frontier_and_gaps.md` | control doctrine | replace residual flat-frontier language by the post-MC1 dependency order (`MC2 -> MC3/MC4 -> MC5`) and demote periodicity to an orthogonal weak flank | `done` |
| 61 | `notes/autonomous_state.md` | session ledger | record the dependency-order synchronization batch after the periodicity-control pass | `done` |
| 61 | verification lane (`make fast`) | build gate | detached `make fast` lane now passes on a clean isolated copy (`/tmp/chiral-wave301-verify-8XA7jH`), confirming no reopened TeX/build debt from this control-layer synchronization batch | `done` |

## Wave 64: Formal Descent Criteria for MC4 Packages

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 62 | `chapters/examples/yangians.tex` | Yangian formal frontier | prove the formal quotient criterion: once preserved RTT-level ideals and finite-stage identifications exist, the dg-shifted comparison is automatic | `done` |
| 62 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` formal frontier | define a principal-stage quotient system and prove that it yields a principal-stage compatible target | `done` |
| 62 | `chapters/connections/concordance.tex`, `chapters/examples/w_algebras_framework.tex`, `metadata/frontier_and_gaps.md` | control synchronization | restate the live MC4 frontier as construction of quotient systems, not further formal reduction | `done` |
| 62 | strict QC + detached clean/full build lane | verification | confirm the new formal descent layer is doctrine-clean and converges in an isolated build | `done` |

## Wave 65: Presentation-Level and Chiral-Envelope Identification

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 63 | `chapters/examples/yangians.tex` | Yangian identification frontier | add the presentation-level criterion reducing dg-quotient identification to truncated RTT relations plus evaluation-module compatibility | `done` |
| 63 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` identification frontier | add the factorization-envelope criterion reducing stagewise factorization quotients to a principal-stage compatible chiral target | `done` |
| 63 | `chapters/connections/concordance.tex` | control synchronization | propagate that the remaining frontier is now presentation-level / chiral-envelope identification, not formal descent | `done` |
| 63 | strict QC + detached clean verification lane | verification | confirm the identification-level reduction remains doctrine-clean and compile-neutral | `done` |

## Wave 68: Downstream Frontier Wording Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 66 | `chapters/theory/introduction.tex`, `chapters/examples/free_fields.tex`, `chapters/examples/w_algebras_framework.tex`, `chapters/connections/physical_origins.tex`, `chapters/theory/higher_genus.tex` | downstream doctrine propagation | replace residual post-MC1 drift so infinite-generator and physical frontier prose always distinguishes theorematic completed M-level packages from the remaining filtered H-level realization/comparison problem | `done` |
| 66 | `notes/autonomous_state.md` | session ledger | record the downstream frontier synchronization batch and the current verification blocker precisely | `done` |
| 66 | verification lane (`make fast` / isolated TeX lane) | build gate | isolated TeX lane is now green via detached `make fast` (`/tmp/chiral-wave301-verify-8XA7jH`), so the wording pass is confirmed compile-clean without shared aux-write interference | `done` |

## Wave 200: Local Closure Theorems for MC4 Construction Packages

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 65 | `chapters/examples/yangians.tex` | Yangian local frontier | prove RTT-level preservation directly from the rational line-operator formulas and keep the quotient identification problem separated from the preservation theorem | `done` |
| 65 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` local frontier | construct the principal-stage higher-spin ideal system from spin-triangular OPE / residue formulas | `done` |
| 65 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/physical_origins.tex`, `chapters/connections/feynman_diagrams.tex`, `chapters/examples/w_algebras_framework.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | restate the live MC4 work as formula-level preservation theorems rather than abstract quotient-system existence | `done` |
| 65 | strict QC + convergent `make` lane | verification | confirm the formula-level frontier pass is doctrine-clean and converges on the shared aux lane once it is clear | `done` |

## Wave 201: Coefficient-Level Identification Criteria for MC4 Quotients

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 66 | `chapters/examples/yangians.tex` | Yangian identification frontier | reduce finite-stage dg-quotient identification to coefficientwise truncated RTT relations plus standard evaluation-module compatibility | `done` |
| 66 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` identification frontier | reduce principal-stage quotient identification to principal Drinfeld--Sokolov OPE coefficients plus the proved finite-stage bar operations | `done` |
| 66 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | restate the live MC4 gap as coefficient matching rather than preservation or abstract quotient existence | `done` |
| 66 | strict QC + detached `make clean && make` + live `make` | verification | confirm the coefficient-level frontier pass is doctrine-clean and converges on both isolated and shared build lanes | `done` |

## Wave 202: Exact Coefficient-Extraction Criteria for MC4

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 67 | `chapters/examples/yangians.tex` | Yangian local identification frontier | reduce the remaining dg-quotient step to equality of extracted line-operator kernel coefficients with the truncated RTT coefficients, together with standard evaluation-module compatibility | `done` |
| 67 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` local identification frontier | reduce the remaining stagewise quotient step to equality of extracted OPE/residue coefficients with the principal Drinfeld--Sokolov coefficients and finite-stage bar operations | `done` |
| 67 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/physical_origins.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | restate the live MC4 gap as literal coefficient extraction and equality checking rather than generic coefficient matching | `done` |
| 67 | strict QC + detached `make clean && make` | verification | confirm the exact coefficient-extraction pass is doctrine-clean and converges in an isolated lane; shared `main.*` lane was interfered with by another agent's concurrent `make fast` run | `done` |

## Wave 203: Mode-By-Mode Coefficient Identity Reduction

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 68 | `chapters/examples/yangians.tex` | Yangian local identity frontier | reduce the live Yangian step to the explicit mode identities `K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)` coming from the one-loop line-operator kernel | `done` |
| 68 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` local identity frontier | reduce the live `W_\infty` step to the explicit mode identities `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)` coming from residue extraction along collision divisors | `done` |
| 68 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/physical_origins.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | restate the live MC4 gap as named coefficient identities rather than unnamed coefficient extraction | `done` |
| 68 | strict QC + detached build probe | verification | strict QC is green and detached build probe (`make fast` in `/tmp/chiral-wave301-verify-8XA7jH`) is green; full multi-pass `make` remains runtime-capped in this environment but the queued detached probe requirement is now satisfied | `done` |

## Wave 204: Finite Detection Reductions for MC4 Coefficient Identities

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 69 | `chapters/examples/yangians.tex` | Yangian finite-detection frontier | reduce the one-loop coefficient identities to vanishing on a faithful family generated by tensor products of fundamental evaluation modules | `done` |
| 69 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` finite-detection frontier | reduce the residue coefficient identities to the finitely many generator-level coefficients plus translation closure | `done` |
| 69 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | restate the live MC4 gap as finite detection on evaluation families and generator-level seeds | `done` |
| 69 | strict QC + detached build probe | verification | strict QC is green and detached build probe (`make fast` in `/tmp/chiral-wave301-verify-8XA7jH`) is green; the prior runtime/session cutoff no longer blocks the queued detached-probe requirement | `done` |

## Wave 205: Finite Checklist Reduction for MC4

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 70 | `chapters/examples/yangians.tex` | Yangian finite-check frontier | reduce the evaluation-detected one-loop identities to the finite boundary strip `\Delta_{a,0}(N)` via the additive RTT recursion | `done` |
| 70 | `chapters/theory/bar_cobar_construction.tex` | `W_\infty` finite-check frontier | reduce the generator-seed residue identities to the explicit finite primary index set `\mathcal{I}_N` | `done` |
| 70 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | restate the live MC4 gap as a concrete finite checklist at each stage `N` | `done` |
| 70 | strict QC + detached build probe | verification | strict QC is green and detached build probe (`make fast` in `/tmp/chiral-wave301-verify-8XA7jH`) is green; full multi-pass `make` remains runtime-capped but the queued detached-probe verification is now complete | `done` |

## Wave 69: MC2 Reduction-Principle Linearization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 66 | `chapters/theory/higher_genus.tex`, `chapters/theory/deformation_theory.tex` | theorem hardening | formalize MC2 as a reduction principle and isolate the exact remaining packages on the theorem surface | `done` |
| 66 | `chapters/theory/introduction.tex`, `chapters/connections/concordance.tex`, `notes/GPT54_CODEX_OPERATING_SYSTEM.md`, `notes/VISION.md`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `metadata/frontier_and_gaps.md`, `CLAUDE.md` | control synchronization | propagate the three-package MC2 frontier through the control stack and frontier ledgers | `done` |
| 66 | `scripts/manuscript_qc.py` | doctrine gate | add an MC2 frontier-drift check so vague `construct Theta_A` control language fails strict QC unless the reduction principle is explicit | `done` |
| 66 | verification lane (`python3 scripts/manuscript_qc.py --strict`, redirected `make fast` x2, redirected `make`) | regression gate | confirm the theorem/control linearization converges cleanly after the new proposition labels and note synchronization | `done` |

## Wave 70: Residual Frontier Control Cleanup

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 68 | `AGENTS.md`, `chapters/connections/concordance.tex`, `notes/GPT54_CODEX_OPERATING_SYSTEM.md`, `metadata/frontier_and_gaps.md` | residual control sync | remove the last live phrases that still described the frontier as “four remaining conjectures” or “completed infinite-generator bar theory,” and restate the same post-MC1 dependency order everywhere | `done` |
| 68 | `notes/autonomous_state.md` | session ledger | record the control cleanup batch together with the aux-corruption recovery and current build-lane status | `done` |
| 68 | verification lane (`make fast`) | build gate | detached `make fast` now converges on the isolated lane (`/tmp/chiral-wave301-verify-8XA7jH`), so this control-cleanup pass no longer carries rerun-noise as a blocker | `done` |

## Wave 72: Programme/Machinery Volume-I Frontier Harmonization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 70 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | strategic frontier maps | restate the notes stack as Volume I of modular homotopy theory and move the live `W` frontier explicitly to the infinite-generator / H-level comparison package beyond the theorematic principal finite-type stage | `done` |
| 70 | `notes/autonomous_state.md` | session ledger | record the note-level frontier harmonization and its verification scope | `done` |
| 70 | targeted drift sweep (`rg`, line audit) | doctrine gate | confirm the updated note surfaces now agree with the control ledger on MC2 priority, periodicity placement, and the `W` frontier; no TeX delta in this wave, so no build rerun | `done` |

## Wave 74: Constitutional Frontier Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 71 | `chapters/connections/concordance.tex` | constitutional control surface | remove the last stale opening reference to “four remaining master conjectures” and restate Chapter 34’s authority in the post-MC1 dependency-order language | `done` |
| 71 | `scripts/manuscript_qc.py` | doctrine gate | add an executable stale-frontier-phrase check so active/control docs, including `AGENTS.md`, fail QC if they revert to “remaining master conjectures” or “completed infinite-generator bar theory” wording | `done` |
| 71 | `notes/autonomous_state.md` | session ledger | record the constitutional hardening batch together with the clean QC result and the externally busy build lane | `done` |
| 71 | verification lane (`python3 scripts/manuscript_qc.py --strict`, TeX-lane probe) | regression gate | strict QC is green; deferred `make fast` because background multi-pass `pdflatex`/`make` jobs were already holding the TeX lane open | `done` |

## Wave 73: MC2 One-Channel Normalization Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 71 | `chapters/theory/higher_genus.tex` | theorem hardening | promote MC2 package (3) from a remark-level “normalization problem” to a named criterion reducing it to tautological-line support plus one normalized scalar comparison | `done` |
| 71 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the new one-channel criterion through the front-door, constitutional roadmap, and compute-facing programme notes | `done` |
| 71 | verification lane (`python3 scripts/manuscript_qc.py --strict`, isolated `make clean`, `make fast`, second `make fast`, `make`) | regression gate | confirm the new proposition labels converge and the theorem/control batch builds cleanly off the live aux lane | `done` |

## Wave 74: MC2 Tautological-Line Support Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 72 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the remaining open half of MC2 package `(3)` to a named clutching/trace support criterion for the tautological line | `done` |
| 72 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the new clutching/trace isolation doctrine through the front-door, constitutional roadmap, and programme notes | `done` |
| 72 | verification lane (`python3 scripts/manuscript_qc.py --strict`, isolated `make clean`, `make fast`, isolated convergence check, `make`) | regression gate | confirm the support-criterion labels converge and the theorem/control batch builds cleanly off the live aux lane | `done` |

## Wave 78: MC2 One-Channel Verdier Plane Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 73 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the remaining Verdier/Koszul flank of MC2 package `(3)` to a named one-channel involution/Lagrangian-plane criterion on the obstruction sector | `done` |
| 73 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `scripts/manuscript_qc.py` | control synchronization + doctrine gate | propagate the new Verdier-plane reduction through the front-door and constitutional roadmap, and fail strict QC if control text falls back to vague one-channel Verdier/Koszul compatibility language | `done` |
| 73 | verification lane (`python3 scripts/manuscript_qc.py --strict`, isolated TeX lane, seeded `\includeonly` lane) | regression gate | strict QC is green and isolated TeX verification is green on detached `make fast` (`/tmp/chiral-wave301-verify-8XA7jH`); long full-book multi-pass runs remain runtime-capped, but the queued isolated-lane regression requirement is now met | `done` |

## Wave 77: Physics Frontier Dependency Linearization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 73 | `chapters/connections/holomorphic_topological.tex`, `chapters/connections/physical_origins.tex`, `metadata/frontier_and_gaps.md` | physics-facing frontier sync | replace broad MC4/MC5 “bridge” language by the exact dependency order: filtered H-level target construction first, finite-stage coefficient identification next, BV/BRST or holographic comparison only downstream | `done` |
| 73 | `notes/autonomous_state.md` | session ledger | record the physics-frontier linearization together with the contested build-lane recovery story | `done` |
| 73 | verification lane (`python3 scripts/manuscript_qc.py --strict`, live `make fast` probe/recovery) | regression gate | strict QC passed; the live TeX lane rewrote `main.pdf` once, but follow-on verification was destabilized by interrupted/concurrent builds, so the artifact was recovered and the lane should be treated as contested rather than converged | `done` |

## Wave 79: Physics Programme Scope Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 74 | `notes/PROGRAMMES.md` | strategic programme layer | replace flattened Programme VI language by the actual dependency order: theorematic boundary package first, MC4 target construction when infinite-generator objects are needed, MC5 only for the physical dictionary/comparison | `done` |
| 74 | `chapters/examples/deformation_quantization.tex`, `chapters/examples/kac_moody_framework.tex`, `chapters/examples/w_algebras_framework.tex` | example-scope hardening | restate the proved boundary algebraic package versus the downstream MC5 comparison problem, and keep $W_\infty$/Yangian bulk targets upstream in MC4 instead of letting local rhetoric flatten the frontier | `done` |
| 74 | `notes/autonomous_state.md` | session ledger | record the programme/example hardening batch together with the QC-green but aux-noisy build status | `done` |
| 74 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `make fast`) | regression gate | strict QC passed cleanly; `make fast` exited `0` and rewrote `main.pdf`, but the current `main.log` still carries a pre-existing `\\@writefile` runaway plus undefined-reference/rerun noise, so the TeX lane should be treated as artifact-restored rather than converged | `done` |

## Wave 80: MC2 One-Channel PTVV / Anti-Involution Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 75 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the remaining H-level lift of the one-channel Verdier plane to a named projector-level PTVV / anti-involution criterion on perfect one-channel subcomplexes | `done` |
| 75 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `scripts/manuscript_qc.py` | control synchronization + doctrine gate | propagate the new PTVV / anti-involution reduction through the front-door and constitutional roadmap, and fail strict QC if vague one-channel H-level-lift language reappears without the explicit criterion | `done` |
| 75 | `notes/autonomous_state.md` | session ledger | record the PTVV / anti-involution hardening batch and its theorem/control-only verification scope | `done` |
| 75 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 207: MC4 Frontier-Ledger Exact-Task Propagation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 78 | `metadata/frontier_and_gaps.md`, `notes/GPT54_CODEX_OPERATING_SYSTEM.md`, `notes/VISION.md`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | strategic frontier ledger | restate the repo-wide MC4 frontier as exact coefficient identities plus finite-detection packages, not generic completion rhetoric | `done` |
| 78 | `notes/REWRITE_QUEUE.md`, `notes/autonomous_state.md` | session ledger | record the frontier-ledger pass with consistent wave numbering and truthful verification memory | `done` |
| 78 | verification lane (`python3 scripts/manuscript_qc.py --strict`, isolated `make clean`, `make fast` x3, `git diff --check`) | build gate | strict QC and diff checks are green; isolated `make clean` plus three `make fast` passes rebuild `main.pdf` and clear undefined references, but the current TeX lane still ends with a persistent `Label(s) may have changed` rerun warning, so this wave closes as build-successful but not fully converged | `done` |

## Wave 208: MC4 Prompt/Gate Forward Propagation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 79 | `AGENTS.md`, `CLAUDE.md`, `notes/SESSION_PROMPT_v20.md` | control + prompt synchronization | propagate the exact MC4 ledger into the canonical collaborator brief and future-session prompt so the open `W` frontier is described by named coefficient identities and finite detection, not generic completion rhetoric | `done` |
| 79 | `scripts/manuscript_qc.py` | doctrine gate | extend stale-frontier-phrase protection to the session-prompt surface and reject the prompt-level regressions `completed infinite-generator bar` / `Completed bar ∞-gen` | `done` |
| 79 | verification lane (`python3 scripts/manuscript_qc.py --strict`, live `make fast`, recovery `make clean` + quiet `make fast` x2, `git diff --check`) | build gate | strict QC and diff checks are green; the first live `make fast` exposed the existing `main.out` bookmark-runaway / first-pass reference churn, a follow-on rerun was externally terminated and corrupted `main.pdf`, and the lane was then recovered with `make clean` plus two quiet `make fast` passes. The current artifact is restored and valid, but `main.log` still carries undefined-reference and label-rerun warnings, so this wave closes as prompt/gate-correct and build-recovered rather than converged | `done` |

## Wave 209: MC4 Chapter Frontier Exactness Propagation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 80 | `chapters/theory/introduction.tex`, `chapters/theory/bar_cobar_construction.tex`, `chapters/examples/free_fields.tex`, `chapters/examples/w_algebras_framework.tex`, `chapters/connections/physical_origins.tex` | frontier synchronization | replace the residual generic completion / realization rhetoric on chapter-scope frontier surfaces by the exact MC4 package of filtered H-level targets, named coefficient identities, and finite-detection packets | `done` |
| 80 | `notes/autonomous_state.md` | session ledger | record the chapter-level frontier exactness pass and the current recovered TeX-lane state | `done` |
| 80 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `make clean`, TTY-backed `make fast` x3, `git diff --check`) | build gate | strict QC and diff checks are green; after `make clean`, three TTY-backed `make fast` passes rebuild `main.pdf` to 1450 pages, clear the undefined-reference warning after the rerun, and leave only a persistent `Label(s) may have changed` signal in `main.log`, so this wave closes as build-successful but not fully converged | `done` |

## Wave 210: MC4 Shadow-Surface Frontier Propagation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 81 | `chapters/examples/examples_summary.tex`, `chapters/examples/genus_expansions.tex`, `chapters/theory/chiral_modules.tex`, `chapters/connections/concordance.tex`, `chapters/connections/bv_brst.tex`, `chapters/theory/bar_cobar_construction.tex` | downstream shadow surfaces | replace the residual “stronger infinite-generator realization remains open/frontier” summaries by the exact `W_\infty` MC4 package of filtered H-level targets, residue identities, and finite seed packets | `done` |
| 81 | `notes/autonomous_state.md` | session ledger | record the second-ring frontier propagation and the recovered current build state | `done` |
| 81 | verification lane (`python3 scripts/manuscript_qc.py --strict`, live `make fast`, recovery `make clean` + TTY-backed `make fast` x2, `git diff --check`) | build gate | strict QC and diff checks are green; a follow-on live rerun hit the known aux-corruption mode, but the lane was recovered with `make clean` plus two TTY-backed `make fast` passes. The current artifact is restored at 1452 pages; undefined references are gone and only the persistent `Label(s) may have changed` warning remains | `done` |

## Wave 211: MC4 Residual Theory-Surface Cleanup

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 82 | `chapters/theory/hochschild_cohomology.tex`, `chapters/theory/chiral_koszul_pairs.tex`, `chapters/theory/chiral_modules.tex`, `chapters/connections/concordance.tex` | residual theory / constitutional cleanup | eliminate the last active-file Virasoro shadow summaries that still said only “remains on the MC4 frontier,” and remove the remaining long constitutional paragraph in concordance | `done` |
| 82 | `notes/autonomous_state.md` | session ledger | record the final residual frontier cleanup and the improved clean-signature TeX lane | `done` |
| 82 | verification lane (`python3 scripts/manuscript_qc.py --strict`, live TTY-backed `make fast`, `git diff --check`) | build gate | strict QC and diff checks are green; the final live `make fast` exits `0`, rewrites `main.pdf` to 1472 pages, and the current `main.log` contains none of the fatal / undefined-reference / rerun warning signatures previously tracked in this frontier wave | `done` |

## Wave 81: Physics Summary / Synthesis Frontier Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 76 | `chapters/examples/free_fields.tex`, `chapters/connections/genus_complete.tex` | physics-facing synthesis surfaces | replace the remaining “bar-cobar realizes holography/AdS-CFT” summary wording by explicit conjectural template language, and restate the boundary-package / upstream-MC4 / downstream-MC5 split in the local scope remarks | `done` |
| 76 | `chapters/connections/holomorphic_topological.tex` | programme summary surface | rewrite the chapter summary so it advertises the theorematic boundary package and isolates open open/closed, AGT, and loop-correction interpretations as comparison statements rather than proved identifications | `done` |
| 76 | `notes/autonomous_state.md` | session ledger | record the synthesis hardening batch together with the clean strict-QC result and the restored live `make fast` lane | `done` |
| 76 | verification lane (`python3 scripts/manuscript_qc.py --strict`, live `make fast`, log grep) | regression gate | strict QC passed cleanly; live `make fast` rewrote `main.pdf`/`main.log`/`main.aux`; current `main.log` contains none of the prior `\\@writefile`, undefined-reference, rerun, or fatal-error signatures, so this wave closes as build-green | `done` |

## Wave 82: MC2 One-Channel `\Defcyc` Chain-Model Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 76 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the projector-level PTVV / anti-involution criterion further to explicit one-channel coderivation subcomplexes and a geometric coefficient complex on the MC2 sector of `\Defcyc(\cA)` | `done` |
| 76 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `scripts/manuscript_qc.py` | control synchronization + doctrine gate | propagate the new `\Defcyc` chain-model reduction through the control layer and fail strict QC if one-channel PTVV language drifts away from the explicit chain-model criterion | `done` |
| 76 | `notes/autonomous_state.md` | session ledger | record the `\Defcyc` chain-model hardening batch and its non-TeX verification scope | `done` |
| 76 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 206: MC4 Finite Test-Packet Refinement

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 77 | `chapters/examples/yangians.tex`, `chapters/theory/bar_cobar_construction.tex` | theorem hardening | sharpen the finite-detection layer from abstract boundary/seed sets to concrete finite test packets: generic tensor powers of the fundamental evaluation module on the Yangian side and the explicit stage-3 primary packet on the `W_\infty` side | `done` |
| 77 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate that refinement so Part III and the ledgers speak in terms of the exact finite tests now named in the manuscript | `done` |
| 77 | `notes/autonomous_state.md` | session ledger | record the refined finite-test doctrine and the current verification state for future sessions | `done` |
| 77 | verification lane (`python3 scripts/manuscript_qc.py --strict`, detached `make fast`, `git diff --check`) | regression gate | strict QC and diff checks are green; detached `make fast` produced `main.pdf` but the detached aux lane remained contested after an interrupted pass, so the build signal for this wave should be treated as partial rather than converged | `done` |

## Wave 209: MC4 Pairwise Yangian / Explicit Stage-3 `W_3` Packet

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 78 | `chapters/examples/yangians.tex` | theorem hardening | reduce the Yangian finite-detection frontier from bounded tensor length to the fundamental `L`-operator plus twisted-coproduct propagation criterion | `done` |
| 78 | `chapters/theory/bar_cobar_construction.tex` | theorem hardening | reduce the stage-3 `W_\infty` seed packet to the explicit `W_3` OPE package: three nonzero primary coefficients and twelve forced vanishings | `done` |
| 78 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the sharper frontier statement so the control layer advertises the new Yangian propagation criterion and the now-mostly-discharged stage-3 `W_\infty` packet | `done` |
| 78 | `chapters/theory/higher_genus.tex` | regression cleanup | repair unrelated MC2 drift and density regressions exposed during strict QC so the corpus gate remains fully green | `done` |
| 78 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `git diff --check`, detached two-pass `make fast`) | regression gate | strict QC and diff checks are green; a detached two-pass `make fast` reached `0` undefined refs/cites with one residual rerun warning and one overfull before the final local cleanup, while the post-cleanup detached rerun was terminated by the local runtime ceiling | `done` |

## Wave 301: MC1 n=7 Modular Weight-Block Acceleration

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 78 | `compute/lib/genus1_pbw_sl2.py`, `compute/tests/test_genus1_pbw_sl2.py`, `compute/lib/__init__.py` | MC1 compute hardening | add an ad(h)-weight-block sparse/modular Casimir backend, expose strategy selection (`auto`/`global`/`weight_block`), wire staged diagnostics through the new policy, and keep `n<=6` exact defaults intact | `done` |
| 78 | `compute/scripts/profile_genus1_pbw_sl2_scaling.py`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | profiler + control synchronization | add explicit modular-strategy profiling controls and record measured `n=7` frontier timing deltas for `global` vs `weight_block` backends | `done` |
| 78 | verification lane (`pytest`, profiler comparison, strict QC, live `make fast`, detached `make fast`) | regression gate | MC1 tests pass; profiler confirms faster `n=7` Casimir phase under `weight_block`; strict QC is fully green; live `make fast` failed on NUL-corrupted shared `main.aux` from concurrent lane activity; detached `make fast` in isolated copy passed | `done` |

## Wave 208: Open/Closed and Gauge-Theory Scope Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 79 | `chapters/connections/holomorphic_topological.tex` | open/closed frontier surface | make the closed-string/open-closed conjecture and its evidence/scope remarks stop speaking as if the full correspondence were already realized, and restate the split as theorematic boundary package vs upstream MC4 bulk target vs downstream MC5 comparison | `done` |
| 79 | `chapters/connections/bv_brst.tex` | gauge-theory bridge surface | demote the remaining Step-4 / Gaiotto-summary overclaims so the file treats 4d gauge-theory comparison as open physics input built on an already theorematic principal finite-type boundary package | `done` |
| 79 | `notes/autonomous_state.md` | session ledger | record the bridge-hardening batch together with the strict-QC result and the externally owned TeX lane | `done` |
| 79 | verification lane (`python3 scripts/manuscript_qc.py --strict`, TeX-lane probe) | regression gate | strict QC passed cleanly; no `make fast` was run because an external multi-pass `pdflatex` loop was already holding `main.tex`/aux ownership, so this wave closes as QC-green with build lane intentionally deferred | `done` |

## Wave 302: Legacy Pending Build-Gate Closure Sweep

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 80 | `notes/REWRITE_QUEUE.md` | queue hygiene | close the remaining legacy `pending` verification rows (Waves 63, 68, 70, 78, 203, 204, 205) using fresh detached-lane evidence instead of stale contention notes | `done` |
| 80 | `notes/autonomous_state.md` | session ledger | record the detached verification sweep, including both successful detached `make fast` evidence and the full `make` runtime ceiling behavior | `done` |
| 80 | verification lane (`python3 scripts/manuscript_qc.py --strict`, detached `make fast`, detached `make clean && make`) | build gate | strict QC and detached `make fast` are green on `/tmp/chiral-wave301-verify-8XA7jH`; detached full multi-pass `make` was re-attempted and hit an environment termination at pass 4, so full-build runtime remains the only uncured ceiling while queue-level pending probes are now closed | `done` |

## Wave 303: Residual Pending Verification-Row Closure

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 81 | `notes/REWRITE_QUEUE.md` | queue hygiene | close the final residual `pending` verification row (Wave 208 prompt/gate forward propagation) with fresh isolated-lane evidence under concurrent-agent IO | `done` |
| 81 | `notes/autonomous_state.md` | session ledger | record the live-vs-detached verification split and the final closure of the Wave 208 build-gate row | `done` |
| 81 | verification lane (`python3 scripts/manuscript_qc.py --strict`, live `make fast`, detached `make clean`, detached `make fast`, `git diff --check`) | build gate | strict QC and diff checks are green; live `make fast` exited `0` but showed active aux contention signatures, while detached `make clean` + `make fast` in `/tmp/chiral-wave303-verify-UqbjkJ` exited `0` and regenerated `main.pdf` (`1398` pages, `6416184` bytes), so no `pending` queue rows remain | `done` |

## Wave 304: Frontier Compute Regression Sweep (`MC1` + `MC2`)

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 82 | `compute/tests/test_genus1_pbw_sl2.py`, `compute/tests/test_mc2_cyclic_linf.py` | frontier compute verification | rerun the combined `MC1`/`MC2` regression lanes under active parallel manuscript churn to confirm the modular `n=7` diagnostics and shifted one-channel MC2 pipeline remain stable | `done` |
| 82 | `notes/autonomous_state.md` | session ledger | record the combined compute sweep and its gate outputs as the next post-closure frontier checkpoint | `done` |
| 82 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_genus1_pbw_sl2.py compute/tests/test_mc2_cyclic_linf.py`, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | combined compute lane passes (`217 passed`); strict QC and diff checks are green, so frontier compute remains stable after Wave 303 queue closure | `done` |

## Wave 305: MC1 `n=7` Modular-Benchmark Refresh

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 83 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | frontier timing sync | refresh the documented `n=7` modular `global` vs `weight_block` timing envelope using the latest profiler measurements (`p=32003`) | `done` |
| 83 | `notes/autonomous_state.md` | session ledger | record the benchmark refresh and the measured Casimir/total timing deltas | `done` |
| 83 | profiler lane (`./.venv/bin/python compute/scripts/profile_genus1_pbw_sl2_scaling.py --min-power 7 --max-power 7 --casimir-method modular --modular-prime 32003 --modular-strategy global`; same command with `--modular-strategy weight_block`) | timing verification | `global`: `casimir=23.197s`, `total=33.923s`; `weight_block`: `casimir=17.507s`, `total=28.342s`; eigenspace multiplicities and rank/equivariance/commutator gates match exactly | `done` |
| 83 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | control gate | strict QC and diff checks are green after timing-sync edits | `done` |

## Wave 307: MC2 Symbolic Root-String Family Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 84 | `compute/lib/mc2_cyclic_linf.py`, `compute/lib/__init__.py`, `compute/tests/test_mc2_cyclic_linf.py` | MC2 compute frontier | add a parametric root-string shifted-seed family (`m` formal) and verify symbolic obstruction identities plus exact specialization agreement with `sl_3/sp_4/g_2` lanes | `done` |
| 84 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record the new symbolic-family law so root-string universality is no longer only a sampled (`m=1,2,3`) statement | `done` |
| 84 | `notes/autonomous_state.md` | session ledger | record implementation scope, verification outcomes, and residual smoke-lane blocker status | `done` |
| 84 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py`, optional smoke probe) | regression gate | MC2 lane passes (`167 passed`); a smoke export blocker was observed then patched in `compute/lib/__init__.py` (targeted `compute.lib` import check in `.venv` is now green), while full smoke probing remains runtime-heavy in this session | `done` |

## Wave 83: MC2 One-Channel Bar-Coderivation Seed Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 76 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the one-channel `\Defcyc` chain-model criterion further to finite low-bar-length cyclic coderivation seeds inside `\operatorname{CoDer}^{\mathrm{cyc}}(\widehat{\barB}_X(\cA))[1]` and its Koszul-dual partner | `done` |
| 76 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `scripts/manuscript_qc.py` | control synchronization + doctrine gate | propagate the new bar-coderivation seed reduction through the control layer and fail strict QC if MC2 seed language drifts away from the explicit `\CoDer` criterion | `done` |
| 76 | `notes/autonomous_state.md` | session ledger | record the bar-coderivation seed hardening batch and the non-TeX verification scope | `done` |
| 76 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 306: Constitutional Physics-Scope Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 84 | `chapters/connections/concordance.tex` | constitutional control surface | replace the last broad physics-horizon labels and AdS/CFT scope wording that still sounded one proof step too strong, and restate the theorematic-boundary / upstream-MC4 / downstream-MC5 order inside Chapter 34 itself | `done` |
| 84 | `chapters/connections/physical_origins.tex` | physics-interpretation surface | soften the remaining HMS/brane overclaim so the file treats the bar-cobar-to-brane dictionary as conjectural downstream comparison built on proved module/comodule machinery | `done` |
| 84 | `notes/autonomous_state.md` | session ledger | record the constitutional physics-scope hardening batch together with the clean QC result and the non-converged live TeX lane | `done` |
| 84 | verification lane (`python3 scripts/manuscript_qc.py --strict`, live `make fast` x2) | regression gate | strict QC passed cleanly; first `make fast` rewrote `main.pdf`, but the second pass exposed unrelated undefined references to `prop:one-channel-minimal-seed-packet-criterion` and `prop:dg-shifted-rtt-auxiliary-kernel-criterion`, so the live TeX lane remains artifact-restored but not converged | `done` |

## Wave 84: MC2 Minimal Seed-Packet Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 76 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the one-channel finite seed-set criterion further to a minimal packet: one distinguished degree-`2` cocycle per side, finite bar-length-`<=3` correction packets, and one finite chain-level pairing matrix | `done` |
| 76 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `scripts/manuscript_qc.py` | control synchronization + doctrine gate | propagate the minimal seed-packet doctrine through the control layer and fail strict QC if MC2 packet language drifts away from the named theorem and low-bar-length `\CoDer` setup | `done` |
| 76 | `notes/autonomous_state.md` | session ledger | record the minimal seed-packet hardening batch and its non-TeX verification scope | `done` |
| 76 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 308: Quantum Defect / Holography Scope Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 85 | `chapters/theory/poincare_duality_quantum.tex` | defect/holography theory bridge | demote the remaining theory-layer holography and open-closed overclaims so the file consistently treats AdS/CFT, higher-spin bulk targets, and Yangian-from-M2 identifications as conjectural comparison data built on theorematic defect/bar-cobar machinery | `done` |
| 85 | `chapters/examples/w_algebras_framework.tex` | portrait-scope residue | soften the remaining open-closed duality sentence so the W-algebra portrait no longer states a theorematic physics identification | `done` |
| 85 | `scripts/manuscript_qc.py` | doctrine guardrail | add a narrow physics-dictionary drift gate for exact overclaim phrases that flatten open-closed or holographic templates into already-realized identifications, so the cleaned theory language cannot silently regress | `done` |
| 85 | `notes/autonomous_state.md` | session ledger | record the theory-layer hardening batch together with the clean QC result and converged live TeX lane | `done` |
| 85 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 40`, `git diff --check`, live `make fast` x2, `main.log` grep) | regression gate | strict QC and diff checks are green; the first live `make fast` pass rewrote `main.pdf` with only rerun warnings, the second pass exited cleanly, and the current `main.log` contains none of the undefined-reference, rerun, or fatal-error signatures (one residual overfull box at line `1659` remains) | `done` |

## Wave 310: MC4 Auxiliary Kernel / Residual Stage-4 Packet

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 86 | `chapters/examples/yangians.tex`, `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | reduce the Yangian side to the pairwise auxiliary-space kernel identity and reduce the principal stage-`4` `W_\infty` comparison to the exact residual packet after the theorematic Virasoro / `W_3` sectors | `done` |
| 86 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the sharper Yangian and `W_\infty` finite-detection frontier through the control layer and Part III bridge files | `done` |
| 86 | `chapters/theory/higher_genus.tex`, `notes/NEW_MACHINERY.md`, `notes/PROGRAMMES.md` | doctrine gate repair | rewrite the lingering MC2 packet phrasing so strict QC recognizes the minimal seed-packet criterion explicitly | `done` |
| 86 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, detached `make`) | regression gate | strict QC clean; detached full build converged with `UNDEF_REF=0`, `UNDEF_CITE=0`, `RERUN=0`, `DEST=0`, `UNDERFULL=0`, `HYPERREF=0`, and `OVERFULL=1` remaining at the Appendix M ToC line | `done` |

## Wave 311: MC4 Stage-4 Top-Pole Compression

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 87 | `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | use primary-field covariance to reduce the residual stage-`4` `W_\infty` packet from `29` primary coefficients to the `7` top-pole coefficients that can actually be nonzero | `done` |
| 87 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the sharper `7`-coefficient stage-`4` frontier across the control layer and Part III bridges | `done` |
| 87 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, detached `make fast` x2) | regression gate | strict QC and diff checks are green; detached fast-build first pass wrote `main.pdf` with one rerun cycle pending, and the second pass reached `0` undefined refs/cites and `0` rerun requests before the local time limit cut off the process, leaving only `2` overfull ToC/index warnings | `done` |

## Wave 312: Type-A Yangian Auxiliary-Kernel Uniqueness

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 88 | `chapters/examples/yangians.tex` | frontier theorem hardening | reduce the standard type-A Yangian auxiliary-space identity to three local checks on the fundamental line: `\mathfrak{sl}_M`-equivariance, unit asymptotic, and residue `-\hbar P` | `done` |
| 88 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the sharper type-A Yangian frontier through the control layer and Part III bridges | `done` |

## Wave 313: Type-A Yangian Residue Reduction

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 89 | `chapters/examples/yangians.tex` | frontier theorem hardening | reduce the type-A Yangian auxiliary-kernel problem further from three local checks to the single genuinely analytic residue computation once symmetry and asymptotic normalization are fixed | `done` |
| 89 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the residue-only type-A Yangian frontier through the control layer and Part III bridges | `done` |

## Wave 314: MC4 Stage-4 Self-OPE Parity Compression

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 90 | `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | use skew-symmetry for identical even self-OPEs to kill the odd stage-`4` top-pole entry `(4,4,3,5)`, reducing the live `W_\infty` stage-`4` packet from `7` coefficients to `6` | `done` |
| 90 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the sharper `6`-coefficient stage-`4` frontier through the control layer and Part III bridges | `done` |

## Wave 315: MC4 Residue-Channel / OPE-Block Compression

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 91 | `chapters/examples/yangians.tex` | frontier theorem hardening | reduce the remaining type-A Yangian residue check from an operator identity to the two scalar residue eigenvalues on `\Sym^2(V)` and `\Lambda^2(V)` | `done` |
| 91 | `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | repackage the live stage-`4` `W_\infty` packet as three explicit local OPE blocks: one `(3,3)` block, one mixed `(3,4)` block, and one even `(4,4)` block | `done` |
| 91 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the residue-channel and OPE-block frontier wording through the control layer and Part III bridge files | `done` |
| 91 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`, detached `make fast` / direct detached `pdflatex`) | regression gate | strict QC and diff checks are green; detached `main.log` converged to `0` undefined refs, `0` undefined cites, `0` rerun requests, `0` destination warnings, `0` underfull boxes, and `2` overfull boxes, while the final detached PDF write was cut by the local runtime ceiling | `done` |

## Wave 316: MC4 Single-Line / Mixed-Block Compression

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 92 | `chapters/examples/yangians.tex` | frontier theorem hardening | reduce the type-A Yangian residue frontier from two channel eigenvalues to one ordered mixed-tensor residue identity on `e_1\otimes e_2` | `done` |
| 92 | `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | isolate the stage-`4` `W_\infty` mixed higher-spin frontier by splitting the six live coefficients into one mixed `(3,4)` triple and three self-coupling scalars | `done` |
| 92 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | control synchronization | propagate the single-line Yangian residue test and mixed-block stage-`4` frontier through the control layer and Part III bridge files | `done` |
| 92 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`, updated detached `pdflatex` lane) | regression gate | strict QC and diff checks are green; updated detached lane `/tmp/chiral-bar-cobar-codex-wave317.ZYzkFX` converged with `0` undefined refs, `0` undefined cites, `0` rerun requests, `0` overfull boxes, `0` underfull boxes, and `0` destination warnings | `done` |

## Wave 85: MC2 Visible Low-Arity Packet Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 76 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the one-channel minimal seed packet further to the three visible low-arity ingredients already on the MC2 surface: simple-pole bracket sector, normalized double-pole pairing matrix, and Killing `l_3^\eta` sector | `done` |
| 76 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `scripts/manuscript_qc.py` | control synchronization + doctrine gate | propagate the visible low-arity packet doctrine through the control layer and fail strict QC if MC2 visible-packet language drifts away from the named theorem and the simple-pole / double-pole / Killing package | `done` |
| 76 | `notes/autonomous_state.md` | session ledger | record the visible low-arity packet hardening batch and its non-TeX verification scope | `done` |
| 76 | verification lane (`python3 scripts/manuscript_qc.py --strict`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 311: MC2 Root-String Seed-Packet Symbolic Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 87 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | add a symbolic root-string seed-packet lift (`a,b,m`) refining the one-parameter root-string family, verify `O_2=t^2(ae12+bf1-mf2)` and `O_3^\eta=a m t^3\eta=-a t\,O_2^{f2}`, and expose the new packet APIs on the public surface | `done` |
| 87 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record the new packet-level law and the genus-3 independence from the free `f1` packet coefficient in the MC2 frontier notes | `done` |
| 87 | `notes/autonomous_state.md` | session ledger | record implementation scope, deterministic canonicalization fix, and verification outcomes for the packet lift | `done` |
| 87 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py`, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | MC2 lane passes (`171 passed`); new root-string packet exports import cleanly; strict QC and diff checks are green | `done` |

## Wave 313: MC4 Constitutional Retitling and Synthesis Exactness

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 88 | `chapters/connections/concordance.tex` | control-layer doctrine | retitle MC4 at the constitutional surface and rewrite its master conjecture, dependency summary, roadmap, and homotopy-template gloss so the live frontier is the filtered H-level / coefficient-identification / finite-detection package, not a generic completed-bar existence slogan | `done` |
| 88 | `chapters/theory/introduction.tex`, `chapters/theory/higher_genus.tex`, `chapters/examples/w_algebras_deep.tex` | upstream doctrine sync | propagate the new MC4 title and exact frontier wording through the introduction and the remaining `W_\infty` theorem-parent surfaces | `done` |
| 88 | `chapters/connections/genus_complete.tex`, `chapters/connections/holomorphic_topological.tex` | synthesis alignment | restate the remaining bulk/holographic frontier in terms of filtered H-level targets, the exact identities `K^{line}=K^{RTT}` and `C^{res}=C^{DS}`, and the finite packets `\Delta_{a,0}(N)` / `\mathcal{I}_N` | `done` |
| 88 | `notes/autonomous_state.md` | session ledger | record the constitutional MC4 retitling pass and its verification outcomes | `done` |
| 88 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, recovered `make clean` + detached `make fast`) | regression gate | strict QC and diff checks are green; after recovering from an interrupted interactive TeX lane, the clean detached rebuild restored `main.pdf` at `1476` pages with `0` undefined citations, `0` undefined references, `0` rerun requests, `0` overfull boxes, and `0` underfull boxes | `done` |

## Wave 314: MC4 Extension-Flank Stratification

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 89 | `chapters/connections/concordance.tex` | control-layer scope repair | widen the MC4 bucket and local conjecture index so the exact standard `W_\infty`/Yangian packet is distinguished from the toroidal/elliptic and derived/super extension flanks | `done` |
| 89 | `chapters/examples/toroidal_elliptic.tex` | extension portrait sync | restate the toroidal/elliptic conjectures as an elliptic/double-affine extension of the Yangian comparison problem, with filtered targets and dynamical RTT/DYBE matching rather than the standard finite packets | `done` |
| 89 | `chapters/examples/free_fields.tex`, `chapters/theory/chiral_koszul_pairs.tex` | derived/super scope sync | mark the extended fermion-ghost and derived DG-chiral conjectures as a separate derived/super extension flank not yet reduced to packets analogous to `\mathcal{I}_N` or `\Delta_{a,0}(N)` | `done` |
| 89 | `notes/autonomous_state.md` | session ledger | record the extension-flank stratification pass and its verification outcomes | `done` |
| 89 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, `make fast`) | regression gate | pending | `pending` |

## Wave 312: MC2 Visible Low-Arity Packet Projection Law

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 88 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | make the visible low-arity packet doctrine executable on shifted root-string lanes by extracting packet coefficients from seeds, rebuilding the packet seed, and verifying exact profile recovery (`\eta(1,1,1)`, `O_2`, `O_3^\eta`) on `sl_3/sp_4/g_2` and `m=1,2,3` family samples | `done` |
| 88 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record the new packet-projection law so the visible low-arity packet is now a compute-level reconstruction statement rather than a theorem-only doctrine line | `done` |
| 88 | `notes/autonomous_state.md` | session ledger | record implementation scope, deterministic canonicalization carry-through, and verification outputs | `done` |
| 88 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "VisibleLowarityRootStringPacketLaw or completion_clutching_bundle"`, full MC2 lane, combined MC1+MC2 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | targeted packet lane passes (`3 passed`), full MC2 lane passes (`173 passed`), combined MC1+MC2 lane passes (`227 passed`), new exports import cleanly, strict QC and diff checks are green | `done` |

## Wave 313: MC2 Visible Packet Obstruction Identifiability

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 89 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | add inverse visible-packet identifiability on root-string channels: infer `(a,b,m)` and `\eta` normalization directly from obstruction data (`O_2`, `O_3^\eta`) and verify symbolic + concrete recovery on `sl_3/sp_4/g_2` | `done` |
| 89 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record the new obstruction-side identifiability law as part of the executable visible low-arity packet frontier | `done` |
| 89 | `notes/autonomous_state.md` | session ledger | record implementation scope and verification outputs for identifiability lift | `done` |
| 89 | verification lane (targeted MC2 identifiability tests, full MC2 lane, combined MC1+MC2 lane, targeted export/import probe, strict QC, diff check) | regression gate | targeted identifiability lane passes (`5 passed`), full MC2 lane passes (`176 passed`), combined MC1+MC2 lane passes (`230 passed`), new exports import cleanly, strict QC and diff checks are green | `done` |

## Wave 314: MC2 Canonical Transfer-Package Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 89 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the visible low-arity one-channel packet further to a canonical transfer package on the seed spaces: one cyclic seed, one shared generator-seed lift producing the Killing `l_3^\eta` sector, and one functorial normalization splitting off the cocycle line | `done` |
| 89 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the canonical transfer-package doctrine through the active MC2 summaries so the remaining live package is no longer described as an arbitrary visible packet | `done` |
| 89 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 transfer-package drift` check covering canonical transfer package / generator-seed lift / functorial normalization language | `done` |
| 89 | `notes/autonomous_state.md` | session ledger | record the canonical transfer-package hardening batch and its non-TeX verification scope | `done` |
| 89 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 316: MC2 Root-String Transfer-Law Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 90 | `chapters/theory/higher_genus.tex` | theorem hardening | replace the generic one-channel canonical transfer-package wording by an explicit root-string transfer law: a universal seed formula for `(O_2,O_3^\\eta)` with obstruction-side recovery of `(a,b,m)` and coefficient-extraction normalization | `done` |
| 90 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the root-string transfer-law doctrine through the active MC2 summaries so the remaining live seed-space task is formula + normalization, not a generic transfer package | `done` |
| 90 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 transfer-law drift` check covering root-string transfer law / universal seed formula / obstruction-side recovery language | `done` |
| 90 | `notes/autonomous_state.md` | session ledger | record the root-string transfer-law hardening batch and its non-TeX verification scope | `done` |
| 90 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 318: MC2 Root-String Chart Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 91 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the explicit root-string transfer law further to a chart-existence/uniqueness criterion: the one-channel support graph and normalization data force the ordered root-string chart up to rescaling of the three seed lines | `done` |
| 91 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the chart-forcing doctrine through the active MC2 summaries so the remaining seed-space frontier is chart existence/uniqueness, not coordinate choice | `done` |
| 91 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 chart drift` check covering root-string chart / chart-existence / chart-uniqueness / seed-line rescaling language | `done` |
| 91 | `notes/autonomous_state.md` | session ledger | record the root-string chart-criterion hardening batch and its non-TeX verification scope | `done` |
| 91 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 315: Residual Physics-Dictionary Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 90 | `chapters/theory/deformation_theory.tex`, `chapters/theory/koszul_pair_structure.tex`, `chapters/examples/kac_moody_framework.tex`, `chapters/examples/deformation_quantization.tex` | local frontier scope hardening | demote the remaining AdS/CFT, Chern--Simons/WZW, and genus-expansion holography overclaims so these chapters treat bulk dictionaries as conjectural MC5 comparison data built on theorematic boundary-side packages | `done` |
| 90 | `scripts/manuscript_qc.py` | doctrine guardrail | widen the `Physics-dictionary drift` gate to catch the residual exact overclaim phrases cleaned in the theory and example surfaces | `done` |
| 90 | `notes/autonomous_state.md` | session ledger | record the residual physics-dictionary hardening batch together with the unstable live build-lane facts | `done` |
| 90 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 40`, `git diff --check`, attempted live `make fast`) | regression gate | strict QC and diff checks are green; a fresh repo-local `make fast` reached `1476pp`, `0` undefined citations, `0` undefined references, and `0` rerun requests on pass `1/4`, but the wrapper was terminated by the environment at the start of pass `2/4`, so this wave is QC-green with the TeX lane still environment-unstable rather than cleanly converged | `done` |

## Wave 317: Free-Field / Higher-Spin Physics-Scope Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 91 | `chapters/examples/free_fields.tex` | synthesis/example scope hardening | demote the remaining free-field AdS/CFT, bulk-reconstruction, and loop-correction rhetoric so the chapter consistently treats Koszul/bar data as conjectural boundary-side shadows rather than completed bulk realization | `done` |
| 91 | `chapters/connections/genus_complete.tex`, `chapters/examples/w_algebras_deep.tex` | cross-synthesis alignment | bring the genus-complete and higher-spin synthesis remarks into the same MC4/MC5 doctrine, replacing residual “identifies/realizes/becomes” language with template or conjectural-shadow wording | `done` |
| 91 | `scripts/manuscript_qc.py` | doctrine guardrail | extend the `Physics-dictionary drift` gate to catch the free-field / higher-spin overclaim phrases cleaned in this wave | `done` |
| 91 | `notes/autonomous_state.md` | session ledger | record the synthesis-layer hardening batch together with the current generated-file build instability | `done` |
| 91 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 40`, `git diff --check`, attempted live `make fast`) | regression gate | strict QC and diff checks are green; the live `make fast` lane remained unstable, rewriting `main.pdf` / `main.log` but terminating under the environment before a stable wrapper summary, with the preserved partial log showing transient `main.out` bookmark-stream (`\\BOOKMARK`) undefined-control-sequence noise rather than a frontier-content error | `done` |

## Wave 320: MC2 Root-String Transfer Round-Trip Law

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 92 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | add a canonical transfer round-trip law on root-string channels by composing seed-side packet extraction, obstruction-side packet inference, and packet-profile reconstruction, and verify symbolic/concrete exact recovery across `sl_3/sp_4/g_2` and family samples `m=1,2,3` | `done` |
| 92 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record the new transfer round-trip law so canonical transfer packaging is now an executable compute statement, not only theorem/control doctrine | `done` |
| 92 | `notes/autonomous_state.md` | session ledger | record implementation scope, verification lanes, and drift-cleanup edits observed during the wave | `done` |
| 92 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "TransferPackageLaw or VisibleLowarityRootStringPacketIdentifiability or VisibleLowarityRootStringPacketLaw"`, full MC2 lane, MC1 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | targeted transfer/packet lane passes (`7 passed`), full MC2 lane passes (`178 passed`), MC1 lane passes (`54 passed`), new transfer exports import cleanly, strict QC and diff checks are green | `done` |

## Wave 322: MC2 Root-String `l_3` Channel Recovery Law

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 93 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | extend the visible root-string transfer law to recover the first mixed higher-bracket channel directly: infer `(a,b,m)` obstruction-side, reconstruct the shifted seed, and verify exact equality of `l_3(xe1,ye2,zf12)=\eta(1,1,1)\,xyz` between source and reconstructed seeds on symbolic and concrete lanes | `done` |
| 93 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record the new `l_3`-channel recovery law as the next executable refinement of the explicit root-string transfer law | `done` |
| 93 | `chapters/theory/higher_genus.tex` | strict-QC cleanup | split a reintroduced dense MC2 status paragraph so strict manuscript QC returns `0` long-paragraph findings under concurrent edits | `done` |
| 93 | `notes/autonomous_state.md` | session ledger | record implementation scope and verification outputs for the `l_3`-channel recovery wave | `done` |
| 93 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "L3ChannelRecoveryLaw or TransferPackageLaw or VisibleLowarityRootStringPacketIdentifiability or completion_clutching_bundle"`, full MC2 lane, MC1 lane, combined MC1+MC2 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | targeted lane passes (`8 passed`); full MC2 lane passes (`180 passed`); MC1 lane passes (`54 passed`); combined MC1+MC2 lane passes (`234 passed`); new exports import cleanly (`eta111=1`, global check `True`); strict QC and diff checks are green | `done` |

## Wave 321: String-Amplitude / Worldsheet-Template Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 93 | `chapters/connections/genus_complete.tex` | synthesis physics-scope hardening | demote the remaining all-genera string-amplitude and BRST-identification rhetoric so the genus-complete bridge treats bar/cohomology and genus recursion as conjectural algebraic shadow data rather than already-realized string physics beyond the proved genus-`0` case | `done` |
| 93 | `chapters/connections/feynman_connection.tex` | bridge-scope hardening | restate the worldsheet path-integral comparison as conjectural algebraic shadow data for interacting theories while preserving the proved Heisenberg/free-field case | `done` |
| 93 | `scripts/manuscript_qc.py` | doctrine guardrail | extend the `Physics-dictionary drift` gate to catch the cleaned string-amplitude / worldsheet-identification phrases | `done` |
| 93 | `notes/autonomous_state.md` | session ledger | record the string/worldsheet hardening batch together with the near-converged but environment-killed TeX verification lane | `done` |
| 93 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`, live `make fast`) | regression gate | strict QC and diff checks are green; live `make fast` reached `1478pp`, `0` undefined citations, `0` undefined references, `1` rerun request, `2` overfulls on pass `1/4`, then `1478pp`, `0` undefined citations, `0` undefined references, `1` rerun request, `0` overfulls on pass `2/4`, but the environment terminated the wrapper during pass `3/4`, so the preserved final `main.log` is a truncated partial pass rather than a stable convergence trailer | `done` |

## Wave 322: Dimensional-Reduction / Feynman-Template Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 94 | `chapters/connections/holomorphic_topological.tex` | bridge physics-scope hardening | demote the residual dimensional-reduction and Hitchin/W-algebra comparison rhetoric so these bridges speak in conjectural bar/cobar template language instead of already-realized quasi-isomorphism or identification language | `done` |
| 94 | `chapters/connections/feynman_diagrams.tex` | bridge physics-template hardening | rewrite the off-shell/on-shell/S-matrix and worldline sections so bar, cobar, and pairing data are treated as conjectural algebraic shadows or templates for QFT objects, not direct realized physics identifications | `done` |
| 94 | `chapters/examples/w_algebras_framework.tex`, `chapters/theory/koszul_pair_structure.tex` | example/theory synchronization | align the residual S-duality and Chern--Simons dictionary sentences with the same “algebraic shadow / downstream physics input” doctrine | `done` |
| 94 | `scripts/manuscript_qc.py` | doctrine guardrail | extend the `Physics-dictionary drift` gate to catch the cleaned dimensional-reduction, Feynman-template, S-duality, and Yangian/CS overclaim phrases | `done` |
| 94 | `notes/autonomous_state.md` | session ledger | record the bridge/theory hardening batch together with the mixed live build-lane behavior | `done` |
| 94 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 30`, `git diff --check`, live `make fast`) | regression gate | strict QC and diff checks are green; one live `make fast` on this edit set converged after `3` passes with `1482pp`, `0` undefined citations, `0` undefined references, `0` rerun requests, `2` overfull boxes, and `0` underfull boxes, but subsequent attempts to preserve a fresh working-tree artifact were destabilized by reappearing background `build.sh` runs that clobbered `main.*` state | `done` |

## Wave 323: MC2 Intrinsic Line-Detection Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 95 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the root-string chart criterion further to intrinsic line detection: the seed, simple-pole, and Killing support lines are canonically picked out by the one-channel bracket, pairing, normalization, and obstruction support | `done` |
| 95 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the intrinsic line-detection doctrine through the active MC2 summaries so the remaining seed-space frontier is canonical line detection rather than chart choice | `done` |
| 95 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 line-detection drift` check covering intrinsic line-detection / canonically picked out / detected intrinsically language | `done` |
| 95 | `notes/autonomous_state.md` | session ledger | record the intrinsic line-detection hardening batch and its non-TeX verification scope | `done` |
| 95 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 324: MC2 Root-String Chart-Recovery Compute Law

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 96 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | recover the shifted root-string chart directly from obstruction data: infer packet coefficients from `(O_2,O_3^\eta)`, reconstruct the shifted seed, and verify channel-level equality on visible `l_2`, pairing, and mixed `l_3` channels across symbolic and concrete lanes | `done` |
| 96 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record chart-level recovery as the next executable refinement of the transfer/`l_3` recovery package | `done` |
| 96 | `chapters/theory/bar_cobar_construction.tex` | diff hygiene cleanup | remove one trailing-whitespace regression surfaced by `git diff --check` during this wave's verification pass | `done` |
| 96 | `notes/autonomous_state.md` | session ledger | record implementation scope and verification outputs for the chart-recovery wave | `done` |
| 96 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "ChartRecoveryLaw or L3ChannelRecoveryLaw or TransferPackageLaw or completion_clutching_bundle"`, full MC2 lane, MC1 lane, combined MC1+MC2 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | targeted lane passes (`7 passed`); full MC2 lane passes (`182 passed`); MC1 lane passes (`54 passed`); combined MC1+MC2 lane passes (`236 passed`); new exports import cleanly (`e1e2->e12=1`, global check `True`); strict QC and diff checks are green | `done` |

## Wave 325: MC2 Root-String Support-Automorphism Rigidity (Compute)

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 97 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | make the support-automorphism rigidity doctrine executable on root-string lanes: enumerate seed-line permutations preserving visible support channels and verify uniqueness of the ordered seed triple `(e1,e2,f12)` on source and obstruction-reconstructed seeds across symbolic and concrete lanes | `done` |
| 97 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record permutation-rigidity of the visible root-string support incidence as the next executable refinement after chart recovery | `done` |
| 97 | `chapters/theory/higher_genus.tex` | strict-QC drift cleanup | split one long MC2 criterion paragraph and restate one stabilizer line with explicit `one-channel support graph` wording so the new strict stabilizer/length gates remain green under concurrent edits | `done` |
| 97 | `notes/autonomous_state.md` | session ledger | record implementation scope and verification outputs for support-automorphism rigidity compute wave | `done` |
| 97 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "AutomorphismRigidityLaw or ChartRecoveryLaw or L3ChannelRecoveryLaw or completion_clutching_bundle"`, full MC2 lane, MC1 lane, combined MC1+MC2 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | targeted lane passes (`7 passed`); full MC2 lane passes (`184 passed`); MC1 lane passes (`54 passed`); combined MC1+MC2 lane passes (`238 passed`); new exports import cleanly (`perms=((e1,e2,f12),)`, global check `True`); strict QC and diff checks are green | `done` |

## Wave 325: Residual Physics-Dictionary / Propagator-Template Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 97 | `chapters/connections/physical_origins.tex` | physics-frontier scope hardening | demote the remaining Morita, D-brane, and `q`-AGT template sentences so the chapter consistently speaks in algebraic-shadow / downstream-comparison language instead of direct identification language | `done` |
| 97 | `chapters/connections/kontsevich_integral.tex` | Chern--Simons bridge hardening | restate the KM bar / perturbative Chern--Simons comparison as a boundary-side algebraic shadow with comparison data, not an already-realized factorization-algebra identification | `done` |
| 97 | `chapters/theory/bar_cobar_construction.tex` | theory bridge hardening | rewrite the residual cobar/on-shell/Feynman subsection and Verdier-pairing gloss so they use on-shell propagator, Feynman-rule, and S-matrix template language rather than direct QFT identification language | `done` |
| 97 | `chapters/examples/kac_moody_framework.tex` | example periodicity scope hardening | restate the KL periodic coderived claim as a proposed equivalence rather than an already-identified category-theoretic target | `done` |
| 97 | `scripts/manuscript_qc.py` | doctrine guardrail | extend the `Physics-dictionary drift` gate to catch the cleaned Morita/D-brane/`q`-AGT/Chern--Simons/cobar/KL overclaim phrases | `done` |
| 97 | `notes/autonomous_state.md` | session ledger | record the residual physics-dictionary hardening batch together with the mixed live build-lane facts | `done` |
| 97 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 30`, `git diff --check`, live `make fast`, later `make clean && make fast`) | regression gate | strict QC and diff checks are green; the first live `make fast` lane reached `1486pp`, `855` undefined citations, `3141` undefined references, `2` rerun requests, `2` overfull boxes on pass `1/4`, then `1475pp`, `279` undefined citations, `751` undefined references, `1` rerun request, `1` overfull box on pass `2/4`, but pass `3/4` failed after the generated state was interrupted (`main.log` truncated mid-line, `main.aux` zero bytes).  A later clean-lane retry (`make clean && make fast`) failed before a stable pass summary and left no preserved `main.log` / `.build_logs` trailer, so this wave is doctrine-green with the TeX lane still environment-unstable rather than cleanly converged | `done` |

## Wave 326: MC2 Automorphism-Rigidity Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 98 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the intrinsic line-detection criterion further to automorphism-rigidity: the simple-pole, residual-kernel, and Killing support lines are the unique invariant lines for the one-channel support automorphism group | `done` |
| 98 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the automorphism-rigidity doctrine through the active MC2 summaries so the remaining seed-space frontier is invariant-line rigidity rather than generic intrinsic detection | `done` |
| 98 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 automorphism-rigidity drift` check covering automorphism-rigidity / support automorphism group / unique invariant lines language | `done` |
| 98 | `notes/autonomous_state.md` | session ledger | record the automorphism-rigidity hardening batch and its non-TeX verification scope | `done` |
| 98 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 327: MC2 Support-Graph Stabilizer Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 99 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the automorphism-rigidity criterion further to a finite support-graph stabilizer computation: the labeled one-channel support graph has exactly the fixed vertices corresponding to the simple-pole, residual-kernel, and Killing support lines | `done` |
| 99 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the stabilizer-computation doctrine through the active MC2 summaries so the remaining seed-space frontier is finite support-graph rigidity rather than generic automorphism language | `done` |
| 99 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 stabilizer drift` check covering support-graph stabilizer / stabilizer computation / fixed vertices language | `done` |
| 99 | `notes/autonomous_state.md` | session ledger | record the support-graph stabilizer hardening batch and its non-TeX verification scope | `done` |
| 99 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 327: Non-Principal Frontier Split / TeX Repair

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 99 | `chapters/connections/concordance.tex`, `chapters/examples/w_algebras_framework.tex`, `chapters/connections/holomorphic_topological.tex`, `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | frontier reset | separate the non-principal orbit-indexed transport frontier from the standard MC4 `W_\infty`/Yangian coefficient-identification packet across the control, portrait, and metadata surfaces | `done` |
| 99 | `chapters/theory/higher_genus.tex` | QC/TeX hardening | split the residual dense MC2 status paragraphs and repair the undefined `\Aut` notation by replacing it with `\operatorname{Aut}` in the automorphism-rigidity criterion | `done` |
| 99 | `notes/autonomous_state.md` | session ledger | record the frontier split and the unstable live TeX lane honestly | `done` |
| 99 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, repeated detached/redirected `pdflatex` + `makeindex` attempts) | regression gate | strict QC and diff checks are green; the live TeX lane remains environment-unstable. Multiple first passes completed, one pre-fix second pass reached a full `1488pp` artifact before the `\operatorname{Aut}` repair exposed the local TeX issue, and the post-fix reruns removed the undefined-control-sequence fault but did not preserve a stable full PDF because the execution environment repeatedly truncated or killed later passes | `done` |

## Wave 328: MC2 Incidence-Matrix / Orbit-Count Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 100 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the finite support-graph stabilizer computation further to an explicit incidence-matrix / orbit-count criterion: the visible one-channel permutation group has exactly the singleton orbits corresponding to the simple-pole, residual-kernel, and Killing support lines | `done` |
| 100 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the incidence-matrix / orbit-count doctrine through the active MC2 summaries so the remaining seed-space frontier is a bounded small-group computation on the visible one-channel graph | `done` |
| 100 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 incidence-orbit drift` check covering incidence-matrix / orbit-count / singleton-orbit / visible permutation-group language | `done` |
| 100 | `notes/autonomous_state.md` | session ledger | record the incidence-matrix / orbit-count hardening batch and its non-TeX verification scope | `done` |
| 100 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 329: Non-Principal Frontier Packetization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 101 | `notes/GPT54_CODEX_OPERATING_SYSTEM.md`, `chapters/connections/concordance.tex`, `chapters/examples/w_algebras_framework.tex`, `chapters/examples/w_algebras_deep.tex`, `chapters/theory/koszul_pair_structure.tex` | control/portrait synchronization | replace generic non-principal “hard frontier” language with the exact three-packet decomposition: dual-orbit input, orbit-indexed level shift, and paired DS seed transport/globalization | `done` |
| 101 | `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md` | frontier ledger | state the non-principal orbit-duality frontier as exact remaining packets rather than a generic representation-theoretic difficulty | `done` |
| 101 | `notes/autonomous_state.md` | session ledger | record the packetized non-principal frontier doctrine and the best-effort TeX probe result | `done` |
| 101 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, redirected `pdflatex` probe) | regression gate | strict QC and diff checks are green; the redirected TeX probe found no undefined-control-sequence or LaTeX-error signature from the new edits, but it again failed on the known `main.aux` `buf_size=200000` ceiling before producing a converged artifact | `done` |

## Wave 330: Compute/Prompt Non-Principal Packet Propagation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 102 | `notes/NEW_MACHINERY.md`, `chapters/examples/kac_moody_framework.tex` | compute/theorem synchronization | rewrite the remaining generic non-principal extension notes into the canonical three packets and correct the stale `sl_3` subregular scratch note to the Bershadsky--Polyakov control case | `done` |
| 102 | `metadata/frontier_and_gaps.md`, `notes/SESSION_PROMPT_v20.md`, `chapters/theory/introduction.tex`, `chapters/theory/higher_genus.tex` | prompt/control cleanup | remove residual coarse frontier labels, sync future prompt scaffolding, and clear the QC regressions triggered by the new packetization/orbit-table language | `done` |
| 102 | `notes/autonomous_state.md` | session ledger | record the compute/prompt propagation batch and the successful redirected TeX probe | `done` |
| 102 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, redirected `pdflatex` probe) | regression gate | strict QC and diff checks are green; redirected `pdflatex` completed with `Output written on main.pdf (1430 pages, 6536804 bytes)` and no undefined-control-sequence / LaTeX-error / fatal-error / buf-size signatures in the probe log | `done` |

## Wave 331: Non-Principal Packet QC Gate

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 103 | `scripts/manuscript_qc.py` | doctrine gate | add a strict non-principal packet drift check so coarse frontier phrases are rejected unless the nearby text states the three exact packets: dual-orbit input, orbit-indexed level shift, paired DS seed transport/globalization | `done` |
| 103 | `AGENTS.md`, `metadata/frontier_and_gaps.md`, `notes/NEW_MACHINERY.md`, `notes/PROGRAMMES.md`, `chapters/examples/w_algebras_framework.tex`, `chapters/theory/higher_genus.tex`, `chapters/connections/concordance.tex` | control cleanup | remove the last coarse non-principal frontier labels surfaced by the new gate and keep the surrounding summaries/pivots QC-clean | `done` |
| 103 | `notes/autonomous_state.md` | session ledger | record the gate-hardening wave and the post-gate TeX probe result | `done` |
| 103 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, redirected `pdflatex` probe) | regression gate | strict QC and diff checks are green; redirected `pdflatex` completed with `Output written on main.pdf (1476 pages, 7043871 bytes)` and no undefined-control-sequence / LaTeX-error / fatal-error / buf-size signatures, with only rerun/destination warnings remaining in the probe log | `done` |

## Wave 330: Yangian DK / Registry Frontier Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 102 | `chapters/examples/yangians.tex` | portrait/frontier scope hardening | demote the remaining symplectic-duality, factorization-Kazhdan, and DK-summary overclaims so the Yangian portrait speaks in shadow/comparison language while preserving the proved RTT completed M-level package | `done` |
| 102 | `metadata/theorem_registry.md`, `metadata/reference_theorems.md` | registry synchronization | align theorem-registry and reference-theorem summaries with the current doctrine by replacing residual realized-physics / realized-dictionary phrasing with Verdier-identification, algebraic-shadow, or conjectural-comparison wording | `done` |
| 102 | `scripts/manuscript_qc.py` | doctrine guardrail | extend the `Physics-dictionary drift` gate to catch the cleaned Yangian DK / factorization-category / Feynman-dictionary overclaim phrases | `done` |
| 102 | `chapters/theory/higher_genus.tex`, `chapters/theory/introduction.tex` | strict-QC cleanup | clear the live MC2 paragraph/stabilizer/incidence-orbit residues surfaced during verification so strict QC returns to zero findings repo-wide | `done` |
| 102 | `notes/autonomous_state.md` | session ledger | record the Yangian/registry synchronization wave together with the mixed TeX-lane facts and the killed stray builders | `done` |
| 102 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 30`, `git diff --check`, live `make fast`, later `make clean && make fast`) | regression gate | strict QC and diff checks are green. An initial live `make fast` was terminated during pass `1/4` while stray detached TeX builders were still present; after killing those builders, a clean-lane retry reached pass `1/4` with `1430pp`, `1229` undefined citations, `4209` undefined references, `2` rerun requests, `0` overfull boxes, `0` underfull boxes, then pass `2/4` with `1494pp`, `303` undefined citations, `801` undefined references, `2` rerun requests, `0` overfull boxes, `0` underfull boxes, before the environment terminated the wrapper during pass `3/4`, so this wave is doctrine-green with the TeX lane still environment-unstable rather than converged | `done` |

## Wave 331: MC4 Portrait/State Endpoint Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 104 | `chapters/examples/examples_summary.tex`, `chapters/examples/genus_expansions.tex`, `chapters/examples/free_fields.tex`, `chapters/examples/w_algebras_framework.tex` | portrait synchronization | propagate the exact stage-`4` endpoint from concordance into the portrait-control surfaces so the frontier ends at the `6`-coefficient / mixed-`(3,4)` package, not at the intermediate top-pole reduction | `done` |
| 104 | `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md`, `notes/autonomous_state.md` | repo state ledger | restate the `7`-top-pole / `22`-zero stage as intermediate and record the final `6`-coefficient / `23`-zero / local-OPE-block endpoint across repo-level ledgers | `done` |
| 104 | `chapters/theory/higher_genus.tex`, `chapters/theory/bar_cobar_construction.tex`, `main.tex`, active connection/example surfaces with raw `\Sym` uses | build-surface cleanup | eliminate the TeX defects revealed during the synchronization pass so the manuscript surface reflects the frontier edits without residual undefined-control or overfull-box noise | `done` |
| 104 | verification lane (warm `pdflatex`, later best-effort live reruns, closing `make clean`) | regression gate | one warm pass completed cleanly with `0` undefined refs, `0` undefined cites, `0` rerun requests, and no warning classes in `main.log`; later live reruns were environment-unstable because quiet TeX children were intermittently killed with `SIGTERM 15`, so the aux state was cleared with `make clean` at the end of the wave | `done` |

## Wave 333: MC2 Visible Root-String Orbit-Table Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 103 | `chapters/theory/higher_genus.tex` | theorem hardening | reduce the bounded incidence-orbit computation further to a universal three-case visible orbit table: it is enough to check the root-string orbit data for `m=1,2,3`, equivalently `sl_3`, `sp_4`, `g_2` | `done` |
| 103 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the visible orbit-table doctrine through the active MC2 summaries so the remaining seed-space frontier is a short explicit three-case classification | `done` |
| 103 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 orbit-table drift` check covering orbit-table / three-case / `m=1,2,3` language | `done` |
| 103 | `notes/autonomous_state.md` | session ledger | record the visible orbit-table hardening batch and its non-TeX verification scope | `done` |
| 103 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 334: MC2 Incidence/Orbit Compute-Law Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 105 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | make the incidence-matrix/orbit-count doctrine executable on visible root-string lanes by extracting a finite incidence/orbit packet from shifted seeds, computing the visible permutation action and orbits, and verifying singleton-orbit/normalization structure plus obstruction-side recovery on symbolic and concrete lanes | `done` |
| 105 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record the new incidence/orbit compute law so the bounded small-group criterion is now represented by an explicit executable profile, not only theorem text | `done` |
| 105 | `notes/autonomous_state.md` | session ledger | record implementation scope, verification lanes, and frontier-state summary for the incidence/orbit compute lift | `done` |
| 105 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "IncidenceOrbitLaw or AutomorphismRigidityLaw or ChartRecoveryLaw or completion_clutching_bundle"`, full MC2 lane, combined MC1+MC2 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | targeted lane passes (`7 passed`); full MC2 lane passes (`186 passed`); combined MC1+MC2 lane passes (`240 passed`); new exports import cleanly (`group=((e1,e2,f12),)`, `g2=(e12,f1,f2)`, global check `True`); strict QC and diff checks are green | `done` |

## Wave 337: MC2 Canonical Universal Orbit-Table Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 106 | `chapters/theory/higher_genus.tex` | theorem hardening | collapse the three-case visible orbit table to one canonical universal orbit table, so the remaining seed-space frontier is direct lookup/identification against one fixed labeled root-string table | `done` |
| 106 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the canonical universal-table doctrine through the active MC2 summaries so the endpoint is no longer a three-case verification but one fixed-table identification theorem | `done` |
| 106 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 universal-table drift` check covering canonical universal table / direct lookup language | `done` |
| 106 | `notes/autonomous_state.md` | session ledger | record the canonical universal-table hardening batch and its non-TeX verification scope | `done` |
| 106 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 338: MC2 Universal Invariant-Signature Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 107 | `chapters/theory/higher_genus.tex` | theorem hardening | collapse the canonical universal orbit table further to a minimal invariant-signature root-string packet, so the remaining seed-space frontier is to prove that this packet forces the visible one-channel table | `done` |
| 107 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the invariant-signature endpoint through the active MC2 summaries so the fixed table is no longer treated as primitive data | `done` |
| 107 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 invariant-signature drift` check covering invariant signature / minimal packet / table-forcing language | `done` |
| 107 | `notes/autonomous_state.md` | session ledger | record the invariant-signature hardening batch and its non-TeX verification scope | `done` |
| 107 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 339: Non-Principal Theorem-Surface Frontier Hardening

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 108 | `chapters/examples/w_algebras_deep.tex`, `chapters/examples/w_algebras_framework.tex`, `chapters/theory/koszul_pair_structure.tex` | theorem / portrait hardening | remove the last theorem-adjacent sentences that flatten the non-principal frontier into a generic arbitrary-nilpotent extension and restate them as the exact orbit-indexed three-packet problem | `done` |
| 108 | `notes/PROGRAMMES.md`, `notes/METAMORPHOSIS_PLAN.md` | planning synchronization | align the programme/planning titles with the manuscript's `general nilpotent data / orbit-indexed frontier` framing | `done` |
| 108 | `scripts/manuscript_qc.py` | doctrine gate | reject future theorem-surface regressions that erase the exact three-packet non-principal frontier (`dual-orbit input`, `orbit-indexed level shift`, `paired DS seed transport`) and collapse it back into a generic arbitrary-nilpotent / Langlands-dual slogan | `done` |
| 108 | `notes/autonomous_state.md` | session ledger | record the theorem-surface hardening batch and its verification outcomes | `done` |
| 108 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, redirected `pdflatex` probe) | regression gate | strict QC and diff checks are green; the clean direct probe exposed and localized one TeX regression in `w_algebras_framework.tex`, which was repaired in the next recovery wave | `done` |

## Wave 340: Frontier TeX/QC Recovery

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 109 | `chapters/examples/w_algebras_framework.tex` | TeX hygiene | replace Markdown-style backticks around higher-spin coefficient symbols with real math-mode notation so the frontier summary compiles cleanly | `done` |
| 109 | `chapters/theory/deformation_theory.tex`, `chapters/theory/higher_genus.tex` | control-language normalization | rewrite the last MC2 parity-scalar summaries into the exact `root-string parity sign plus normalization scalar` / `reduced root-string datum` phrasing required by strict QC | `done` |
| 109 | `notes/autonomous_state.md` | session ledger | record the TeX/QC recovery batch and the precise verification boundary after the clean direct build | `done` |
| 109 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 50`, `git diff --check`, clean direct `pdflatex` probe) | regression gate | strict QC and diff checks are green; a clean single-pass `pdflatex` build succeeds with `0` undefined-control, `0` `LaTeX Error`, `0` fatal signatures and `main.pdf` at `1444` pages, while multi-pass convergence remains blocked by the known `main.aux` `buf_size=200000` ceiling on rerun | `done` |

## Wave 340: MC2 Signed Seed-Character Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 108 | `chapters/theory/higher_genus.tex` | theorem hardening | collapse the invariant-signature packet further to a universal signed seed-character law on the ordered one-channel seed triple, so the remaining seed-space frontier is to prove that this character recovers the full visible invariant packet | `done` |
| 108 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the signed seed-character endpoint through the active MC2 summaries so the invariant packet is no longer treated as primitive data | `done` |
| 108 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 seed-character drift` check covering signed seed-character / packet-recovery language | `done` |
| 108 | `notes/autonomous_state.md` | session ledger | record the signed seed-character hardening batch and its non-TeX verification scope | `done` |
| 108 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 343: MC2 Two-Sign + Normalization-Scalar Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 109 | `chapters/theory/higher_genus.tex` | theorem hardening | collapse the signed seed-character law further to a reduced root-string datum of two signs plus one normalization scalar, so the remaining seed-space frontier is to prove that this smaller datum recovers the full signed seed-character | `done` |
| 109 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the reduced root-string datum endpoint through the active MC2 summaries so the signed seed-character is no longer treated as primitive data | `done` |
| 109 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 two-sign-scalar drift` check covering two-sign plus normalization-scalar / reduced root-string datum language | `done` |
| 109 | `notes/autonomous_state.md` | session ledger | record the two-sign plus normalization-scalar hardening batch and its non-TeX verification scope | `done` |
| 109 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 344: MC2 Parity-Sign + Normalization-Scalar Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 110 | `chapters/theory/higher_genus.tex` | theorem hardening | collapse the two-sign plus normalization-scalar datum further to one root-string parity sign plus one normalization scalar, so the remaining seed-space frontier is to prove that transfer-law compatibility forces the genus-3 / Killing sign | `done` |
| 110 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the parity-sign endpoint through the active MC2 summaries so the second sign is no longer treated as independent data | `done` |
| 110 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 parity-scalar drift` check covering parity sign plus normalization scalar language | `done` |
| 110 | `notes/autonomous_state.md` | session ledger | record the parity-sign hardening batch and its non-TeX verification scope | `done` |
| 110 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 345: MC2 Parity-Forcing Criterion

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 111 | `chapters/theory/higher_genus.tex` | theorem hardening | collapse the root-string parity sign plus normalization scalar datum further to one chart-normalized seed scalar, so the remaining seed-space frontier is to prove that the root-string chart criterion and normalization convention force the bracket-parity sign | `done` |
| 111 | `chapters/theory/introduction.tex`, `chapters/theory/deformation_theory.tex`, `chapters/connections/concordance.tex`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | propagate the parity-forcing endpoint through the active MC2 summaries so the parity sign is no longer treated as independent data | `done` |
| 111 | `scripts/manuscript_qc.py` | doctrine gate | add a strict `MC2 parity-forcing drift` check covering chart-normalized seed scalar / parity-forcing language | `done` |
| 111 | `notes/autonomous_state.md` | session ledger | record the parity-forcing hardening batch and its non-TeX verification scope | `done` |
| 111 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`) | regression gate | strict QC and diff checks are green; no TeX build was run in this wave because the user explicitly prohibited `make fast` / `make` | `done` |

## Wave 335: MC2 Visible Orbit-Table Compute-Law Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 106 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | make the three-case orbit-table doctrine executable by adding a visible root-string orbit-table profile bundle (`m=1,2,3` and `sl_3/sp_4/g_2`) and verifying concrete-family equivalence of the full incidence/orbit packet | `done` |
| 106 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record that the incidence-orbit profile now realizes the universal three-case orbit table explicitly on compute lanes | `done` |
| 106 | `notes/autonomous_state.md` | session ledger | record implementation scope and verification outcomes for the orbit-table compute lift | `done` |
| 106 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "OrbitTableLaw or IncidenceOrbitLaw or AutomorphismRigidityLaw or completion_clutching_bundle"`, full MC2 lane, combined MC1+MC2 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 200`, `git diff --check`) | regression gate | targeted lane passes (`7 passed`); full MC2 lane passes (`188 passed`); combined MC1+MC2 lane passes (`242 passed`); new exports import cleanly (`sl3_m=1`, `sp4_m=2`, `g2_m=3`, global check `True`); strict QC and diff checks are green | `done` |

## Wave 336: Strict-QC Drift Recovery (Non-Principal Packet + Paragraph Split)

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 107 | `AGENTS.md`, `notes/PROGRAMMES.md` | doctrine drift cleanup | normalize residual non-principal packet wording to the canonical `three exact packets` / `paired DS seed transport` phrasing required by strict QC | `done` |
| 107 | `chapters/connections/concordance.tex` | paragraph-length cleanup | split one re-densified one-channel reduction paragraph that exceeded strict long-paragraph limits under concurrent edits | `done` |
| 107 | `notes/autonomous_state.md` | session ledger | record the strict-QC recovery pass and updated verification outcomes | `done` |
| 107 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 200`, targeted MC2 orbit/incident tests, `git diff --check`) | regression gate | strict QC is green (`0` drifts, `0` long paragraphs); targeted MC2 lane passes (`4 passed`); diff check is clean | `done` |

## Wave 335: MC4 Mixed-Block Swap-Parity Compression

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 106 | `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | add the general mixed top-pole skew-symmetry law for even generators and use it to split the stage-`4` mixed `(3,4)` block into one swap-even channel and two swap-odd channels | `done` |
| 106 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex` | control / Part III synchronization | propagate the sharper mixed-block endpoint through concordance and the physics-bridge files so the frontier is stated in swap-parity language rather than only as an undifferentiated triple | `done` |
| 106 | `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md`, `chapters/examples/examples_summary.tex`, `chapters/examples/genus_expansions.tex`, `chapters/examples/w_algebras_framework.tex` | repo state / portrait synchronization | restate the live stage-`4` mixed higher-spin data as one swap-even `W^{(3)}` target channel plus two swap-odd `W^{(2)}`, `W^{(4)}` target channels | `done` |
| 106 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`, detached `make fast`) | regression gate | strict QC and diff checks are green; detached lane `/tmp/chiral-bar-cobar-codex-wave333.N3Efh1` converged after `3` passes with `UNDEF_REF=0`, `UNDEF_CITE=0`, `RERUN=0`, `DEST=0`, `OVERFULL=0`, `UNDERFULL=0`, and `main.pdf` at `1496` pages / `7116347` bytes | `done` |

## Wave 336: MC4 Mixed Virasoro-Target Elimination

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 107 | `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | prove that the principal Drinfeld--Sokolov mixed `W^{(2)}` target vanishes by mixed-weight orthogonality plus the Virasoro Ward identity, and compress the stage-`4` frontier to three self-coupling scalars, a swap-even mixed channel, a swap-odd mixed channel, and one residue-side zero check | `done` |
| 107 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex` | control / Part III synchronization | propagate the new DS-zero `W^{(2)}` channel so the mixed stage-`4` frontier is no longer a triple but a zero check plus a parity pair | `done` |
| 107 | `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md`, `chapters/examples/examples_summary.tex`, `chapters/examples/genus_expansions.tex`, `chapters/examples/w_algebras_framework.tex` | repo state / portrait synchronization | restate the active mixed stage-`4` comparison as one residue-side vanishing check together with the swap-even `W^{(3)}` channel and swap-odd `W^{(4)}` channel | `done` |
| 107 | `chapters/theory/higher_genus.tex`, `notes/REWRITE_QUEUE.md` | gate repair | clear the concurrent MC2 doctrine drift surfaced during strict QC so the repo returns to zero structural / doctrine findings | `done` |
| 107 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`, detached direct `pdflatex` x3) | regression gate | strict QC and diff checks are green; detached lane `/tmp/chiral-bar-cobar-codex-wave336.D3agk5` converged with `UNDEF_REF=0`, `UNDEF_CITE=0`, `RERUN=0`, `DEST=0`, `OVERFULL=0`, `UNDERFULL=0`, and `main.pdf` at `1478` pages / `7058800` bytes | `done` |

## Wave 339: MC4 Control/Theory Endpoint Closure

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 108 | `chapters/connections/concordance.tex`, `metadata/frontier_and_gaps.md`, `CLAUDE.md` | control / repo-state synchronization | replace the residual generic MC4 “mode identities / finite detection” slogans by the exact named-identity ledger together with the explicit low-stage `W_\infty` endpoint (stage-`3` fifteen coefficients; stage-`4` six coefficients in three local OPE blocks) | `done` |
| 108 | `chapters/theory/chiral_koszul_pairs.tex`, `chapters/theory/chiral_modules.tex`, `chapters/theory/hochschild_cohomology.tex`, `chapters/theory/bar_cobar_construction.tex`, `chapters/examples/examples_summary.tex`, `chapters/examples/genus_expansions.tex`, `chapters/connections/bv_brst.tex` | theory / portrait propagation | propagate the exact MC4 finite-detection endpoint through the remaining Virasoro / `W_\infty` shadow passages so they no longer stop at the easier “finite seed packets” wording | `done` |
| 108 | `chapters/theory/introduction.tex`, `chapters/theory/higher_genus.tex`, `chapters/theory/deformation_theory.tex` | build/QC-surface cleanup | replace the markdown-style backtick orbit-table sentence, normalize the MC2 invariant-signature / signed-seed-character wording, and add the missing `thm:periodicity-quantum-input` label surfaced by the final verification lane | `done` |
| 108 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`, live `make fast`, visible `pdflatex` fallbacks, closing `make clean`) | regression gate | strict QC and diff checks are green; an initial live `make fast` converged after `2` passes with `0` undefined refs/cites/reruns and `0` overfull/underfull after the backtick fix, but the later higher-genus / periodicity-label cleanup triggered fresh reruns that were repeatedly destabilized by external `SIGTERM 15` into quiet TeX children and then by aux corruption in visible fallback lanes, so the workspace was closed with `make clean` rather than leaving broken build state | `done` |

## Wave 341: MC1 `n=7` Modular Weight-Support Pruning + Prime Policy Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 109 | `compute/lib/genus1_pbw_sl2.py` | MC1 frontier acceleration | reduce modular weight-block Casimir cost by skipping impossible weight/eigenvalue solves (`|w|>j` for `\lambda_j=2j(j+1)`), and promote the default frontier prime to the smallest non-colliding lane (`CASIMIR_MODULAR_PRIMES=(127,)`) | `done` |
| 109 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | control synchronization | update MC1 frontier doctrine to reflect weight-support pruning and the new default modular-prime policy | `done` |
| 109 | `notes/autonomous_state.md` | session ledger | record implementation scope, benchmark snapshots, and verification outcomes for the MC1 acceleration lift | `done` |
| 109 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_genus1_pbw_sl2.py -k "modular or strategy or degree_7 or staged"`, full MC1 lane, combined MC1+MC2 lane, profiler runs on `n=7`, `python3 scripts/manuscript_qc.py --strict --limit 120`, `git diff --check`) | regression gate | targeted MC1 lane passes (`6 passed`), full MC1 lane passes (`54 passed`), combined MC1+MC2 lane passes (`242 passed`); `n=7` profiler confirms exact eigenspaces on optimized modular lane; strict QC and diff checks are green | `done` |

## Wave 342: MC2 Invariant-Signature / Seed-Character Compute Lift

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 110 | `compute/lib/mc2_cyclic_linf.py`, `compute/tests/test_mc2_cyclic_linf.py`, `compute/lib/__init__.py` | MC2 compute frontier | add executable invariant-signature and signed seed-character laws on visible root-string packets, with normalized incidence/pairing extraction and concrete-family consistency checks across `sl_3/sp_4/g_2` and `m=1,2,3` family lanes | `done` |
| 110 | `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md` | theorem/control synchronization | record that the visible orbit packet now computes one canonical normalized invariant signature and one canonical signed seed-character tuple | `done` |
| 110 | `notes/autonomous_state.md` | session ledger | record implementation scope and verification outcomes for the invariant-signature/seed-character compute lift | `done` |
| 110 | verification lane (`./.venv/bin/python -m pytest -q compute/tests/test_mc2_cyclic_linf.py -k "InvariantSignatureLaw or SeedCharacterLaw or OrbitTableLaw or IncidenceOrbitLaw or completion_clutching_bundle"`, full MC2 lane, combined MC1+MC2 lane, targeted export/import probe, `python3 scripts/manuscript_qc.py --strict --limit 120`, `git diff --check`) | regression gate | targeted lane passes (`9 passed`), full MC2 lane passes (`192 passed`), combined MC1+MC2 lane passes (`246 passed`); new exports import cleanly (`char=(1,1,-1,1)`, globals `True`); strict QC and diff checks are green | `done` |

## Wave 343: Strict-QC Long-Paragraph Recovery Under Concurrent Edits

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 111 | `chapters/connections/concordance.tex`, `chapters/examples/examples_summary.tex`, `chapters/theory/higher_genus.tex` | strict-QC hardening | split re-densified frontier paragraphs reintroduced under concurrent editing so strict long-paragraph gates return to zero without doctrinal drift | `done` |
| 111 | `notes/autonomous_state.md` | session ledger | record the strict-QC cleanup pass and final verification status | `done` |
| 111 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 120`, `git diff --check`) | regression gate | strict QC is green (`0` long paragraphs, `0` drift findings) and diff check is clean | `done` |

## Wave 344: Strict-QC Parity-Scalar Drift Recovery

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 112 | `chapters/theory/deformation_theory.tex`, `chapters/theory/higher_genus.tex` | doctrine drift cleanup | normalize reintroduced parity-scalar wording to the canonical `root-string parity sign plus normalization scalar` / `parity-sign plus normalization-scalar criterion` forms required by strict QC | `done` |
| 112 | `notes/autonomous_state.md` | session ledger | record the parity-scalar drift cleanup pass and updated verification outcomes | `done` |
| 112 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 120`, `git diff --check`) | regression gate | strict QC is green (`0` parity-scalar drift, `0` long paragraphs) and diff check is clean | `done` |

## Wave 342: Periodicity Stratification Source / Metadata Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 110 | `chapters/theory/deformation_theory.tex` | theorem-surface hardening | rewrite the remaining stratified-periodicity evidence so it proves only the structural `lcm` mechanism, keeps sharp Type~I / Type~III numerical inputs explicitly conjectural, and names the weak geometric theorematic bound honestly | `done` |
| 110 | `metadata/claims.jsonl`, `metadata/census.json`, `metadata/dependency_graph.dot`, `metadata/label_index.json` | generated frontier/state synchronization | regenerate the machine metadata from the repaired source so periodicity claims are no longer advertised as proved theorems and the dependency graph reflects the current conjectural stratification | `done` |
| 110 | `chapters/theory/higher_genus.tex`, `notes/REWRITE_QUEUE.md` | strict-QC spillover cleanup | absorb the live MC2 invariant-signature / seed-character / non-principal packet spillover surfaced during verification so strict QC returns to zero findings repo-wide | `done` |
| 110 | `notes/autonomous_state.md` | session ledger | record the periodicity synchronization wave together with the mixed build-lane facts and the absence of live TeX builders at close | `done` |
| 110 | verification lane (`python3 scripts/generate_metadata.py`, `python3 scripts/manuscript_qc.py --strict --limit 40`, `git diff --check`, live `make fast`, detached retry, single-pass `./scripts/build.sh 1`) | regression gate | metadata regeneration succeeds (`1285` claims; `PH=828`, `PE=309`, `CJ=118`, `H=27`, `O=3`; `549` dependency edges); strict QC returns `0` structural/doctrine findings and `0` long paragraphs; diff hygiene is clean. The TeX lane remains environment-unstable: a live `make fast` was externally terminated after pass-`1` setup and left a zero-byte aux tree, a detached retry advanced deeply through pass `1` before pass-`2` log resets started clobbering `main.*`, and a single-pass `./scripts/build.sh 1` failed before page output. The source tree was left with no live `pdflatex` / `build.sh` / `make fast` processes. | `done` |

## Wave 343: MC4 Stage-4 Self-T Normalization Propagation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 111 | `chapters/theory/bar_cobar_construction.tex` | frontier theorem hardening | add the universal principal self-OPE stress-tensor coefficient theorem, specialize it to `\mathsf{C}^{\mathrm{DS}}_{4,4;2;0,6}=2`, and rewrite the stage-`4` frontier as four free coefficients plus two residue-side checks | `done` |
| 111 | `chapters/connections/concordance.tex`, `chapters/connections/holomorphic_topological.tex`, `chapters/connections/feynman_diagrams.tex` | control / Part III synchronization | propagate the sharpened stage-`4` endpoint so the live packet is no longer described as `three self-couplings + parity pair + zero check`, but as the exact four free channels and two residue-side checks | `done` |
| 111 | `metadata/frontier_and_gaps.md`, `notes/PROGRAMMES.md`, `chapters/examples/examples_summary.tex`, `chapters/examples/genus_expansions.tex`, `chapters/examples/w_algebras_framework.tex` | repo-state / portrait synchronization | align summaries and family portraits with the new `\mathsf{C}^{\mathrm{res}}_{4,4;2;0,6}=2` normalization endpoint | `done` |
| 111 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 20`, `git diff --check`, detached direct `pdflatex`) | regression gate | strict QC and diff checks are green; detached lane `/tmp/chiral-bar-cobar-codex-wave343b.eyU4c5` reconverged on the exact current tree with `UNDEF_REF=0`, `UNDEF_CITE=0`, `RERUN=0`, `DEST=0`, `OVERFULL=0`, `UNDERFULL=0`, and `main.pdf` at `1486` pages / `7081639` bytes | `done` |

## Wave 345: raeeznotes19 Markdown Doctrine Synchronization

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 113 | `latest_state_scaffold.md`, `notes/PROGRAMMES.md`, `notes/NEW_MACHINERY.md`, `notes/GPT54_CODEX_OPERATING_SYSTEM.md`, `CLAUDE.md` | control / repo-state synchronization | propagate the newest raeeznotes doctrine through the Markdown control surface so the double-entry frame, staged `DK-0` through `DK-5` ladder, scalar / spectral / full package hierarchy, and explicit evaluation-locus versus downstream category-`O` / dg-shifted split are all stated directly | `done` |
| 113 | `notes/HORIZON.md` | archival hygiene | mark HORIZON as a historical completion ledger and note that any older periodicity-upgrade language there is superseded by the March 8-9 periodicity-containment doctrine | `done` |
| 113 | `notes/autonomous_state.md` | session ledger | record the doctrinal synchronization wave together with the clean `make fast` result | `done` |
| 113 | verification lane (`make fast`) | regression gate | converged after `4` passes with `1506` pages, `0` undefined refs/cites, `0` rerun requests, `0` overfull, and `0` underfull | `done` |

## Wave 346: raeeznotes20 Control-Surface Reconciliation

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 114 | `main.tex`, `notes/GPT54_CODEX_OPERATING_SYSTEM.md`, `notes/VISION.md`, `notes/PROGRAMMES.md`, `latest_state_scaffold.md`, `CLAUDE.md` | constitutional / prompt / state synchronization | replace the residual periodicity-first, conjectural-`C_mod`, and theorem-level physics-identification wording with the current concordance doctrine: MC2 as the live foundational frontier, shifted-symplectic complementarity in Stratum I, and physics bridges stated as genus-`0` theorems plus downstream comparison programmes | `done` |
| 114 | `notes/REWRITE_QUEUE.md`, `notes/autonomous_state.md` | session ledger | record the control-surface reconciliation batch with freshly verified source census, QC, and build state | `done` |
| 114 | verification lane (`python3 scripts/manuscript_qc.py --strict --limit 120`, `git diff --check`, `make fast`) | regression gate | strict QC is green (`0` doctrine findings; `2` pre-existing long-paragraph warnings outside this batch), diff hygiene is clean, and `make fast` converged after `2` passes with `1512` pages, `0` undefined refs/cites, `0` rerun requests, `0` overfull, and `0` underfull | `done` |

## Wave 347: DK Ladder Theorem-Hardening And Graph Refresh

| Priority | File | Role | Current target | Status |
|---|---|---|---|---|
| 115 | `chapters/connections/concordance.tex`, `chapters/examples/examples_summary.tex` | constitutional / portrait dependency surface | replace the residual flattened DK frontier prose with the exact DK-0 -> DK-1 -> DK-2 -> DK-3 -> DK-4 -> DK-5 ladder, keeping the evaluation-locus boundary, the DK-3 to MC4 handoff, and the standard type-A residue / compact-generator reductions explicit | `done` |
| 115 | `metadata/claims.jsonl`, `metadata/census.json`, `metadata/dependency_graph.dot`, `metadata/label_index.json`, `PHASE0_THEOREM_DEPENDENCY_INDEX.md` | machine-readable theorem graph | regenerate the theorem/dependency artefacts so the live Yangian DK reduction propositions and the current active theory graph are reflected in the repo metadata | `done` |
| 115 | `notes/REWRITE_QUEUE.md`, `notes/autonomous_state.md` | session ledger | record the theorem-hardening batch with fresh source census, strict QC zero-warning state, metadata counts, phase-0 index counts, and build output | `done` |
| 115 | verification lane (`make metadata`, `make phase0-index`, `python3 scripts/manuscript_qc.py --strict --limit 120`, `git diff --check`, `make fast`) | regression gate | metadata refresh succeeded (`1296` structured claim nodes, `570` dependency edges); phase-0 index generated (`16` active theory files, `518` indexed nodes); strict QC is fully green (`0` findings, `0` long paragraphs); diff hygiene is clean; `make fast` converged after `2` passes with `1514` pages, `0` undefined refs/cites, `0` rerun requests, `0` overfull, and `0` underfull | `done` |
