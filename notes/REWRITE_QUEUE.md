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

## Standing Rule

Before advancing to a later wave, make sure the earlier wave compiles and
the control documents still agree with one another.
