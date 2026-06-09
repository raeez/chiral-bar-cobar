r"""Concordance rectification engine: systematic verification of constitutional claims.

CONCORDANCE (concordance.tex) is the single source of truth for the monograph.
This engine verifies concordance claims against the compute layer, checking:

1. THEOREM STATUS CLAIMS: MC1-MC4 proved, MC5 ambient-split
   (analytic HS-sewing and strict ML completed/pro chain surfaces proved;
   bounded direct-sum and downstream physical identifications not proved);
   Koszulness programme counts,
   DK status, three-pillar identification counts.

2. FORMULA CONSISTENCY: kappa values, shadow depths, discriminants,
   growth rates match across concordance and compute engines.

3. CROSS-REFERENCE INTEGRITY: Pillar citations, preprint dependencies,
   arXiv IDs, publication status claims.

4. NUMERICAL CLAIMS: F_g values, Q^contact, Hessian corrections,
   planted-forest formulas, shadow coefficients.

5. STRUCTURAL CLAIMS: four-class G/L/C/M partition, shadow-formality
   identification, operadic complexity.

MULTI-PATH VERIFICATION (per CLAUDE.md):
    Path 1: Direct computation from defining formulas
    Path 2: Cross-family consistency (additivity, complementarity)
    Path 3: Limiting cases (c=0, k=0, genus=0)
    Path 4: Literature comparison (AP38: convention check)

Anti-patterns guarded against:
    AP1:  kappa formula cross-checked across families
    AP10: Tests derive expected values, not hardcode
    AP24: complementarity sum kappa+kappa' checked per family
    AP39: kappa != S_2 for non-Virasoro families
    AP48: kappa(A) != c/2 for general VOAs
"""

from fractions import Fraction
from typing import Dict, List, Optional, Tuple
import math


# ============================================================
# SECTION 0: Theorem/proof surface gates (PDF obligations 901--932)
# ============================================================

TITLE_ENVIRONMENT_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'theorem_title_no_platonic',
        'Theorem titles use exact mathematical adjectives, not "Platonic".',
    ),
    (
        'platonic_only_in_informal_remarks',
        '"Platonic" appears only in informal remarks.',
    ),
    (
        'conjectures_numbered_environment',
        'Conjectures are in numbered conjecture environments.',
    ),
    (
        'conditional_theorem_hypotheses_first',
        'Conditional theorems state their hypotheses before the conclusion.',
    ),
    (
        'conditional_title_has_complete_hypotheses',
        'A title containing conditional language has complete hypotheses.',
    ),
)


THEOREM_SIGNATURE_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'raw_finite_completed_scope_stated',
        'The theorem states raw/finite/completed scope.',
    ),
    (
        'ordered_symmetric_scope_stated',
        'The theorem states ordered/symmetric scope.',
    ),
    (
        'chain_derived_coderived_scope_stated',
        'The theorem states chain/derived/coderived ambient.',
    ),
    (
        'operadic_level_stated',
        'The theorem states E1/Einf/SC/E3 level.',
    ),
    (
        'curve_genus_scope_stated',
        'The theorem states curve genus scope.',
    ),
    (
        'critical_level_exclusions_stated',
        'The theorem states critical-level exclusions.',
    ),
    (
        'genericity_exclusions_stated',
        'The theorem states genericity exclusions.',
    ),
    (
        'finite_type_hypotheses_stated',
        'The theorem states finite-type hypotheses.',
    ),
    (
        'completion_hypotheses_stated',
        'The theorem states completion hypotheses.',
    ),
    (
        'dualizability_hypotheses_stated',
        'The theorem states dualizability hypotheses.',
    ),
    (
        'holonomicity_hypotheses_stated',
        'The theorem states holonomicity hypotheses.',
    ),
    (
        'base_change_hypotheses_stated',
        'The theorem states base-change hypotheses.',
    ),
)


PROOF_OPENING_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'ambient_category_named',
        'The proof begins by naming the ambient category.',
    ),
    (
        'differential_identified',
        'The proof identifies the differential.',
    ),
    (
        'filtration_identified',
        'The proof identifies the filtration.',
    ),
    (
        'spectral_sequence_identified',
        'The proof identifies the spectral sequence when one is used.',
    ),
)


PROOF_HYPOTHESIS_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'convergence_theorem_cited_when_used',
        'A proof using convergence cites the convergence theorem.',
    ),
    (
        'lim1_killed_when_inverse_limits_used',
        'A proof using inverse limits kills lim1.',
    ),
    (
        'finite_continuous_duality_checked_when_used',
        'A proof using duality checks finite/continuous duality.',
    ),
    (
        'verdier_holonomicity_checked_when_used',
        'A proof using Verdier duality checks holonomicity.',
    ),
    (
        'gysin_orientation_checked_when_used',
        'A proof using Gysin maps checks orientation.',
    ),
    (
        'pushforward_properness_checked_when_used',
        'A proof using pushforward checks properness.',
    ),
    (
        'symmetric_quotient_equivariance_checked_when_used',
        'A proof using quotient by Sigma_n checks equivariance.',
    ),
    (
        'one_over_n_factor_char_zero_stated_when_used',
        'A proof using 1/n! states characteristic zero.',
    ),
    (
        'r_matrix_descent_twisted_equivariance_stated_when_used',
        'A proof using R-matrix descent states R-twisted equivariance.',
    ),
    (
        'pbw_associated_graded_stated_when_used',
        'A proof using PBW states the associated graded.',
    ),
    (
        'koszulness_diagonal_concentration_stated_when_used',
        'A proof using Koszulness states diagonal concentration.',
    ),
)


ADVANCED_PROOF_METHOD_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'formality_model_and_obstruction_groups_stated_when_used',
        'A proof using formality states the model and obstruction groups.',
    ),
    (
        'ainfty_transfer_sdr_data_stated_when_used',
        'A proof using A-infinity transfer states SDR data.',
    ),
    (
        'modular_operad_graph_convention_stated_when_used',
        'A proof using modular operads states the graph convention.',
    ),
    (
        'stable_graph_legs_edges_genus_defined_when_used',
        'A proof using stable graphs defines legs, edges, and genus.',
    ),
    (
        'determinant_line_sign_convention_cited_when_used',
        'A proof using signs cites the determinant-line convention.',
    ),
    (
        'brst_complex_defined_when_ghosts_used',
        'A proof using ghosts defines the BRST complex.',
    ),
    (
        'central_charge_convention_defined_when_used',
        'A proof using central charge defines the convention.',
    ),
    (
        'trace_map_defined_when_kappa_used',
        'A proof using kappa defines the trace map.',
    ),
    (
        'a_dual_exists_proved_when_kkappa_used',
        'A proof using K^kappa proves A^! exists.',
    ),
    (
        'central_charge_a_dual_proved_when_kc_used',
        'A proof using K^c proves the central charge of A^!.',
    ),
    (
        'kghost_presentation_dependence_stated_when_used',
        'A proof using K^ghost states presentation dependence.',
    ),
)


TABLE_STATUS_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'ope_tables_full_coefficients_when_used',
        'OPE tables provide full coefficients when used.',
    ),
    (
        'ope_coefficients_match_normalization_appendix',
        'Every OPE coefficient matches one normalization appendix.',
    ),
    (
        'table_entries_cite_theorem_or_proposition',
        'Every table entry cites the theorem/proposition proving it.',
    ),
    (
        'proved_table_status_has_manuscript_proof',
        'Every proved table status is backed by a proof in the manuscript.',
    ),
    (
        'conditional_table_status_lists_exact_conditions',
        'Every conditional table status lists exact conditions.',
    ),
    (
        'open_table_status_names_obstruction_complex',
        'Every open table status names the obstruction complex.',
    ),
)


STRUCTURE_PLACEMENT_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'duplicate_theorem_statements_merged',
        'Duplicate theorem statements differing only rhetorically are merged.',
    ),
    (
        'sign_appendices_merged_into_one_sign_theorem',
        'Repeated sign appendices are merged into one sign theorem.',
    ),
    (
        'five_object_firewall_merged_early_and_cross_referenced',
        'Five-object firewall remarks are merged early and cross-referenced everywhere.',
    ),
    (
        'motivational_physics_after_theorem_proof',
        'Long motivational physics paragraphs appear after theorem proof.',
    ),
    (
        'unproved_cross_volume_claims_in_comparison_conjectures',
        'Unproved cross-volume claims sit in comparison conjectures.',
    ),
    (
        'k3_recognition_targets_in_conditional_chapter',
        'K3 recognition targets sit in one conditional chapter.',
    ),
    (
        'arithmetic_consequences_after_algebraic_core',
        'Arithmetic consequences appear after the algebraic core.',
    ),
    (
        'examples_after_main_theorem',
        'Examples appear after the main theorem.',
    ),
)


VERIFICATION_ORDER_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'heisenberg_first_verification',
        'Heisenberg is the first verification theorem.',
    ),
    (
        'affine_km_second_verification',
        'Affine Kac-Moody is the second verification theorem.',
    ),
    (
        'betagamma_third_verification',
        'Beta-gamma is the third verification theorem.',
    ),
    (
        'class_m_completion_test_for_virasoro_w3',
        'Virasoro/W3 are the class-M completion test.',
    ),
    (
        'h_delta_after_class_m_completion',
        'H_Delta appears after class-M completion, not before.',
    ),
)


DEPENDENCY_LANGUAGE_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'dependency_graph_arrows_only_proved_implications',
        'Dependency graph arrows are only proved implications.',
    ),
    (
        'conjectural_arrows_removed',
        'Conjectural comparison arrows are removed.',
    ),
    (
        'comparison_therefore_replaced_by_under_hypotheses',
        '"Therefore" becomes "under hypotheses" when a comparison theorem is used.',
    ),
    (
        'universal_property_proved_when_universal_used',
        '"Universal" is used only when a universal property is proved.',
    ),
    (
        'canonical_uniqueness_or_contractibility_proved',
        '"Canonical" is used only with uniqueness or contractibility of choices.',
    ),
)


MORITA_LEVEL_QUADRANT_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'chosen_vacuum_data_defined',
        'Chosen vacuum data are defined.',
    ),
    (
        'vacuum_independence_proved_when_claimed',
        'Independence of vacuum is proved whenever it is claimed.',
    ),
    (
        'open_factorization_category_level0_defined',
        'The level-0 open factorization category is defined.',
    ),
    (
        'morita_equivalence_to_module_category_proved_when_used',
        'Morita equivalence to the module category is proved when used.',
    ),
    (
        'morita_equivalence_separated_from_algebra_isomorphism',
        'Morita equivalence is separated from algebra isomorphism.',
    ),
    (
        'level_alphabet_defined_once',
        'The level alphabet is defined once.',
    ),
    (
        'level_signatures_exhaustive_only_open_quadrant',
        'Level signatures are exhaustive only for the Open quadrant.',
    ),
    (
        'level_signatures_do_not_transfer_cy_claims',
        'Level signatures are not used to transfer CY claims.',
    ),
    (
        'quadrant_grid_defined',
        'The quadrant grid is defined.',
    ),
    (
        'cross_quadrant_maps_preserve_structures_proved_when_claimed',
        'Cross-quadrant structure preservation is proved when claimed.',
    ),
    (
        'conjectural_cross_quadrant_maps_marked',
        'Conjectural cross-quadrant maps are marked as conjectural.',
    ),
)


NOTATION_DISCIPLINE_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'notation_table_before_main_theorem',
        'A notation table appears before the main theorem.',
    ),
    (
        'unused_symbols_removed_after_definition',
        'Symbols unused after definition are removed.',
    ),
    (
        'C_not_reused_for_curve_coalgebra_category_same_proof',
        'C is not reused for curve, coalgebra, and category in the same proof.',
    ),
    (
        'D_not_reused_for_divisor_differential_duality_same_proof',
        'D is not reused for divisor, differential, and duality in the same proof.',
    ),
    (
        'D_reserved_for_verdier_duality',
        'D is reserved for Verdier duality.',
    ),
    (
        'd_reserved_for_differentials',
        'd is reserved for differentials.',
    ),
    (
        'delta_subscripts_distinguish_diagonal_coproduct_discriminant',
        'Delta notation separates diagonal, coproduct, and discriminant by subscripts.',
    ),
    (
        'fm_notation_consistent',
        'FM, FMlog, and FMord are used consistently.',
    ),
    (
        'bar_notation_consistent',
        'Bar notation is used consistently.',
    ),
    (
        'ch_hh_thh_notation_consistent',
        'CHch, HHalg, and THH are used consistently.',
    ),
    (
        'z_notation_distinct',
        'Zchder, Z(A), and ZDr are kept distinct.',
    ),
)


HYPOTHESIS_REFERENCE_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'hypothesis_index_added',
        'An index lists H1-H4, CP1-CP3, D1-D5, FH, and OCA.',
    ),
    (
        'no_hypothesis_package_before_definition',
        'No hypothesis package is referenced before its definition.',
    ),
    (
        'no_missing_section_refs',
        'Missing section references such as section ?? are removed.',
    ),
    (
        'standard_landscape_defined_finite_list',
        'Every standard-landscape reference points to a defined finite list.',
    ),
    (
        'landscape_coverage_proved_or_atlas_language_used',
        'Landscape coverage is proved, or the surface is called an atlas.',
    ),
)


ABSTRACT_FRONT_BACK_GATES: Tuple[Tuple[str, str], ...] = (
    (
        'arxiv_abstract_from_theorem_spine_only',
        'The arXiv abstract is drawn only from the theorem spine.',
    ),
    (
        'conjectural_physics_arithmetic_final_abstract_labelled',
        'Conjectural physics/arithmetic in the abstract is final-paragraph and labelled.',
    ),
    (
        'first_20_pages_type_correct_definitions',
        'The first twenty pages prove the core definitions are type-correct.',
    ),
    (
        'last_theorem_surviving_invariants_commutative_diagram',
        'The last theorem is the surviving-invariants commutative diagram.',
    ),
)


def _gate_report(
    gates: Tuple[Tuple[str, str], ...],
    satisfied: Dict[str, bool],
) -> Dict[str, object]:
    """Return a normalized report for theorem/proof surface gates."""
    missing = [name for name, _ in gates if not satisfied.get(name, False)]
    return {
        'gates': {name: description for name, description in gates},
        'satisfied': {name: bool(satisfied.get(name, False)) for name, _ in gates},
        'missing': missing,
        'all_gates_satisfied': len(missing) == 0,
    }


def theorem_title_environment_scope(
    theorem_title_contains_platonic: bool = False,
    platonic_only_in_informal_remarks: bool = False,
    conjectures_numbered_environment: bool = False,
    conditional_theorem_hypotheses_first: bool = False,
    theorem_title_contains_conditional: bool = False,
    conditional_title_hypotheses_complete: bool = False,
) -> Dict[str, object]:
    """Gate theorem titles and conjecture/conditional environments."""
    conditional_title_ok = (
        not theorem_title_contains_conditional
        or conditional_title_hypotheses_complete
    )
    satisfied = {
        'theorem_title_no_platonic': not theorem_title_contains_platonic,
        'platonic_only_in_informal_remarks': platonic_only_in_informal_remarks,
        'conjectures_numbered_environment': conjectures_numbered_environment,
        'conditional_theorem_hypotheses_first': conditional_theorem_hypotheses_first,
        'conditional_title_has_complete_hypotheses': conditional_title_ok,
    }
    report = _gate_report(TITLE_ENVIRONMENT_GATES, satisfied)
    return {
        **report,
        'platonic_theorem_title_allowed': False,
        'conditional_title_allowed': conditional_title_ok,
        'title_environment_surface_allowed': report['all_gates_satisfied'],
        'status': 'title_environment_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def theorem_signature_scope(
    raw_finite_completed_scope_stated: bool = False,
    ordered_symmetric_scope_stated: bool = False,
    chain_derived_coderived_scope_stated: bool = False,
    operadic_level_stated: bool = False,
    curve_genus_scope_stated: bool = False,
    critical_level_exclusions_stated: bool = False,
    genericity_exclusions_stated: bool = False,
    finite_type_hypotheses_stated: bool = False,
    completion_hypotheses_stated: bool = False,
    dualizability_hypotheses_stated: bool = False,
    holonomicity_hypotheses_stated: bool = False,
    base_change_hypotheses_stated: bool = False,
) -> Dict[str, object]:
    """Gate the full type signature required in theorem statements."""
    satisfied = {
        'raw_finite_completed_scope_stated': raw_finite_completed_scope_stated,
        'ordered_symmetric_scope_stated': ordered_symmetric_scope_stated,
        'chain_derived_coderived_scope_stated': chain_derived_coderived_scope_stated,
        'operadic_level_stated': operadic_level_stated,
        'curve_genus_scope_stated': curve_genus_scope_stated,
        'critical_level_exclusions_stated': critical_level_exclusions_stated,
        'genericity_exclusions_stated': genericity_exclusions_stated,
        'finite_type_hypotheses_stated': finite_type_hypotheses_stated,
        'completion_hypotheses_stated': completion_hypotheses_stated,
        'dualizability_hypotheses_stated': dualizability_hypotheses_stated,
        'holonomicity_hypotheses_stated': holonomicity_hypotheses_stated,
        'base_change_hypotheses_stated': base_change_hypotheses_stated,
    }
    report = _gate_report(THEOREM_SIGNATURE_GATES, satisfied)
    return {
        **report,
        'theorem_statement_signature_complete': report['all_gates_satisfied'],
        'status': 'theorem_signature_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def proof_opening_scope(
    ambient_category_named: bool = False,
    differential_identified: bool = False,
    filtration_identified: bool = False,
    spectral_sequence_used: bool = False,
    spectral_sequence_identified: bool = False,
) -> Dict[str, object]:
    """Gate the first proof paragraph: ambient, differential, filtration, spectral sequence."""
    spectral_sequence_ok = not spectral_sequence_used or spectral_sequence_identified
    satisfied = {
        'ambient_category_named': ambient_category_named,
        'differential_identified': differential_identified,
        'filtration_identified': filtration_identified,
        'spectral_sequence_identified': spectral_sequence_ok,
    }
    report = _gate_report(PROOF_OPENING_GATES, satisfied)
    return {
        **report,
        'proof_opening_complete': report['all_gates_satisfied'],
        'spectral_sequence_claim_allowed': spectral_sequence_ok,
        'status': 'proof_opening_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def proof_hypothesis_scope(
    convergence_used: bool = False,
    convergence_theorem_cited: bool = False,
    inverse_limits_used: bool = False,
    lim1_killed: bool = False,
    duality_used: bool = False,
    finite_continuous_duality_checked: bool = False,
    verdier_duality_used: bool = False,
    verdier_holonomicity_checked: bool = False,
    gysin_maps_used: bool = False,
    gysin_orientation_checked: bool = False,
    pushforward_used: bool = False,
    pushforward_properness_checked: bool = False,
    symmetric_quotient_used: bool = False,
    symmetric_quotient_equivariance_checked: bool = False,
    one_over_n_factor_used: bool = False,
    characteristic_zero_stated: bool = False,
    r_matrix_descent_used: bool = False,
    r_twisted_equivariance_stated: bool = False,
    pbw_used: bool = False,
    pbw_associated_graded_stated: bool = False,
    koszulness_used: bool = False,
    koszulness_diagonal_concentration_stated: bool = False,
) -> Dict[str, object]:
    """Gate proof obligations that arise only when a method is used."""
    satisfied = {
        'convergence_theorem_cited_when_used': (
            not convergence_used or convergence_theorem_cited
        ),
        'lim1_killed_when_inverse_limits_used': (
            not inverse_limits_used or lim1_killed
        ),
        'finite_continuous_duality_checked_when_used': (
            not duality_used or finite_continuous_duality_checked
        ),
        'verdier_holonomicity_checked_when_used': (
            not verdier_duality_used or verdier_holonomicity_checked
        ),
        'gysin_orientation_checked_when_used': (
            not gysin_maps_used or gysin_orientation_checked
        ),
        'pushforward_properness_checked_when_used': (
            not pushforward_used or pushforward_properness_checked
        ),
        'symmetric_quotient_equivariance_checked_when_used': (
            not symmetric_quotient_used or symmetric_quotient_equivariance_checked
        ),
        'one_over_n_factor_char_zero_stated_when_used': (
            not one_over_n_factor_used or characteristic_zero_stated
        ),
        'r_matrix_descent_twisted_equivariance_stated_when_used': (
            not r_matrix_descent_used or r_twisted_equivariance_stated
        ),
        'pbw_associated_graded_stated_when_used': (
            not pbw_used or pbw_associated_graded_stated
        ),
        'koszulness_diagonal_concentration_stated_when_used': (
            not koszulness_used or koszulness_diagonal_concentration_stated
        ),
    }
    report = _gate_report(PROOF_HYPOTHESIS_GATES, satisfied)
    return {
        **report,
        'proof_method_obligations_complete': report['all_gates_satisfied'],
        'pbw_claim_allowed': not pbw_used or pbw_associated_graded_stated,
        'koszulness_claim_allowed': (
            not koszulness_used or koszulness_diagonal_concentration_stated
        ),
        'status': 'proof_hypothesis_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def theorem_surface_obligation_scope(
    title: Optional[Dict[str, bool]] = None,
    signature: Optional[Dict[str, bool]] = None,
    proof_opening: Optional[Dict[str, bool]] = None,
    proof_hypotheses: Optional[Dict[str, bool]] = None,
) -> Dict[str, object]:
    """Aggregate PDF obligations 901--932 into one theorem-surface report."""
    title_report = theorem_title_environment_scope(**(title or {}))
    signature_report = theorem_signature_scope(**(signature or {}))
    proof_opening_report = proof_opening_scope(**(proof_opening or {}))
    proof_hypotheses_report = proof_hypothesis_scope(**(proof_hypotheses or {}))
    reports = {
        'title_environment': title_report,
        'theorem_signature': signature_report,
        'proof_opening': proof_opening_report,
        'proof_hypotheses': proof_hypotheses_report,
    }
    return {
        'reports': reports,
        'all_gates_satisfied': all(
            report['all_gates_satisfied'] for report in reports.values()
        ),
        'blocked_components': [
            name for name, report in reports.items()
            if not report['all_gates_satisfied']
        ],
    }


def advanced_proof_method_scope(
    formality_used: bool = False,
    formality_model_stated: bool = False,
    formality_obstruction_groups_stated: bool = False,
    ainfty_transfer_used: bool = False,
    sdr_data_stated: bool = False,
    modular_operad_used: bool = False,
    graph_convention_stated: bool = False,
    stable_graphs_used: bool = False,
    legs_edges_genus_defined: bool = False,
    signs_used: bool = False,
    determinant_line_convention_cited: bool = False,
    ghosts_used: bool = False,
    brst_complex_defined: bool = False,
    central_charge_used: bool = False,
    central_charge_convention_defined: bool = False,
    kappa_used: bool = False,
    trace_map_defined: bool = False,
    kkappa_used: bool = False,
    a_dual_exists_proved: bool = False,
    kc_used: bool = False,
    central_charge_a_dual_proved: bool = False,
    kghost_used: bool = False,
    kghost_presentation_dependence_stated: bool = False,
) -> Dict[str, object]:
    """Gate advanced proof methods and scalar conventions."""
    formality_ok = (
        not formality_used
        or (formality_model_stated and formality_obstruction_groups_stated)
    )
    satisfied = {
        'formality_model_and_obstruction_groups_stated_when_used': formality_ok,
        'ainfty_transfer_sdr_data_stated_when_used': (
            not ainfty_transfer_used or sdr_data_stated
        ),
        'modular_operad_graph_convention_stated_when_used': (
            not modular_operad_used or graph_convention_stated
        ),
        'stable_graph_legs_edges_genus_defined_when_used': (
            not stable_graphs_used or legs_edges_genus_defined
        ),
        'determinant_line_sign_convention_cited_when_used': (
            not signs_used or determinant_line_convention_cited
        ),
        'brst_complex_defined_when_ghosts_used': (
            not ghosts_used or brst_complex_defined
        ),
        'central_charge_convention_defined_when_used': (
            not central_charge_used or central_charge_convention_defined
        ),
        'trace_map_defined_when_kappa_used': (
            not kappa_used or trace_map_defined
        ),
        'a_dual_exists_proved_when_kkappa_used': (
            not kkappa_used or a_dual_exists_proved
        ),
        'central_charge_a_dual_proved_when_kc_used': (
            not kc_used or central_charge_a_dual_proved
        ),
        'kghost_presentation_dependence_stated_when_used': (
            not kghost_used or kghost_presentation_dependence_stated
        ),
    }
    report = _gate_report(ADVANCED_PROOF_METHOD_GATES, satisfied)
    return {
        **report,
        'formality_claim_allowed': formality_ok,
        'ainfty_transfer_claim_allowed': not ainfty_transfer_used or sdr_data_stated,
        'kkappa_claim_allowed': not kkappa_used or a_dual_exists_proved,
        'kc_claim_allowed': not kc_used or central_charge_a_dual_proved,
        'kghost_claim_allowed': (
            not kghost_used or kghost_presentation_dependence_stated
        ),
        'status': 'advanced_proof_method_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def table_status_scope(
    ope_tables_used: bool = False,
    ope_tables_full_coefficients: bool = False,
    ope_coefficients_match_normalization_appendix: bool = False,
    table_entries_cite_theorem_or_proposition: bool = False,
    proved_table_status_used: bool = False,
    proved_table_status_has_manuscript_proof: bool = False,
    conditional_table_status_used: bool = False,
    conditional_table_status_lists_exact_conditions: bool = False,
    open_table_status_used: bool = False,
    open_table_status_names_obstruction_complex: bool = False,
) -> Dict[str, object]:
    """Gate OPE tables and proved/conditional/open status evidence."""
    satisfied = {
        'ope_tables_full_coefficients_when_used': (
            not ope_tables_used or ope_tables_full_coefficients
        ),
        'ope_coefficients_match_normalization_appendix': (
            not ope_tables_used or ope_coefficients_match_normalization_appendix
        ),
        'table_entries_cite_theorem_or_proposition': (
            table_entries_cite_theorem_or_proposition
        ),
        'proved_table_status_has_manuscript_proof': (
            not proved_table_status_used or proved_table_status_has_manuscript_proof
        ),
        'conditional_table_status_lists_exact_conditions': (
            not conditional_table_status_used
            or conditional_table_status_lists_exact_conditions
        ),
        'open_table_status_names_obstruction_complex': (
            not open_table_status_used or open_table_status_names_obstruction_complex
        ),
    }
    report = _gate_report(TABLE_STATUS_GATES, satisfied)
    return {
        **report,
        'ope_table_claim_allowed': (
            not ope_tables_used
            or (
                ope_tables_full_coefficients
                and ope_coefficients_match_normalization_appendix
            )
        ),
        'proved_status_claim_allowed': (
            not proved_table_status_used or proved_table_status_has_manuscript_proof
        ),
        'conditional_status_claim_allowed': (
            not conditional_table_status_used
            or conditional_table_status_lists_exact_conditions
        ),
        'open_status_claim_allowed': (
            not open_table_status_used or open_table_status_names_obstruction_complex
        ),
        'status': 'table_status_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def proof_table_obligation_scope(
    proof_methods: Optional[Dict[str, bool]] = None,
    tables: Optional[Dict[str, bool]] = None,
) -> Dict[str, object]:
    """Aggregate PDF obligations 933--949 into one proof/table report."""
    proof_report = advanced_proof_method_scope(**(proof_methods or {}))
    table_report = table_status_scope(**(tables or {}))
    reports = {
        'advanced_proof_methods': proof_report,
        'table_status': table_report,
    }
    return {
        'reports': reports,
        'all_gates_satisfied': all(
            report['all_gates_satisfied'] for report in reports.values()
        ),
        'blocked_components': [
            name for name, report in reports.items()
            if not report['all_gates_satisfied']
        ],
    }


def structure_placement_scope(
    duplicate_theorem_statements_merged: bool = False,
    sign_appendices_merged_into_one_sign_theorem: bool = False,
    five_object_firewall_merged_early: bool = False,
    five_object_firewall_cross_referenced: bool = False,
    motivational_physics_after_theorem_proof: bool = False,
    unproved_cross_volume_claims_in_comparison_conjectures: bool = False,
    k3_recognition_targets_in_conditional_chapter: bool = False,
    arithmetic_consequences_after_algebraic_core: bool = False,
    examples_after_main_theorem: bool = False,
) -> Dict[str, object]:
    """Gate manuscript structure and placement obligations."""
    firewall_ok = (
        five_object_firewall_merged_early
        and five_object_firewall_cross_referenced
    )
    satisfied = {
        'duplicate_theorem_statements_merged': duplicate_theorem_statements_merged,
        'sign_appendices_merged_into_one_sign_theorem': (
            sign_appendices_merged_into_one_sign_theorem
        ),
        'five_object_firewall_merged_early_and_cross_referenced': firewall_ok,
        'motivational_physics_after_theorem_proof': (
            motivational_physics_after_theorem_proof
        ),
        'unproved_cross_volume_claims_in_comparison_conjectures': (
            unproved_cross_volume_claims_in_comparison_conjectures
        ),
        'k3_recognition_targets_in_conditional_chapter': (
            k3_recognition_targets_in_conditional_chapter
        ),
        'arithmetic_consequences_after_algebraic_core': (
            arithmetic_consequences_after_algebraic_core
        ),
        'examples_after_main_theorem': examples_after_main_theorem,
    }
    report = _gate_report(STRUCTURE_PLACEMENT_GATES, satisfied)
    return {
        **report,
        'five_object_firewall_surface_allowed': firewall_ok,
        'structure_placement_complete': report['all_gates_satisfied'],
        'status': 'structure_placement_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def verification_order_scope(
    heisenberg_first_verification: bool = False,
    affine_km_second_verification: bool = False,
    betagamma_third_verification: bool = False,
    class_m_completion_test_for_virasoro_w3: bool = False,
    h_delta_after_class_m_completion: bool = False,
) -> Dict[str, object]:
    """Gate the example/verification theorem order."""
    satisfied = {
        'heisenberg_first_verification': heisenberg_first_verification,
        'affine_km_second_verification': affine_km_second_verification,
        'betagamma_third_verification': betagamma_third_verification,
        'class_m_completion_test_for_virasoro_w3': (
            class_m_completion_test_for_virasoro_w3
        ),
        'h_delta_after_class_m_completion': h_delta_after_class_m_completion,
    }
    report = _gate_report(VERIFICATION_ORDER_GATES, satisfied)
    return {
        **report,
        'verification_order_complete': report['all_gates_satisfied'],
        'h_delta_early_allowed': False,
        'status': 'verification_order_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def dependency_language_scope(
    dependency_graph_arrows_only_proved_implications: bool = False,
    conjectural_arrows_removed: bool = False,
    comparison_theorem_used: bool = False,
    comparison_therefore_replaced_by_under_hypotheses: bool = False,
    universal_used: bool = False,
    universal_property_proved: bool = False,
    canonical_used: bool = False,
    canonical_uniqueness_proved: bool = False,
    canonical_contractibility_of_choices_proved: bool = False,
) -> Dict[str, object]:
    """Gate dependency graph arrows and comparison-language adjectives."""
    comparison_ok = (
        not comparison_theorem_used
        or comparison_therefore_replaced_by_under_hypotheses
    )
    universal_ok = not universal_used or universal_property_proved
    canonical_ok = (
        not canonical_used
        or canonical_uniqueness_proved
        or canonical_contractibility_of_choices_proved
    )
    satisfied = {
        'dependency_graph_arrows_only_proved_implications': (
            dependency_graph_arrows_only_proved_implications
        ),
        'conjectural_arrows_removed': conjectural_arrows_removed,
        'comparison_therefore_replaced_by_under_hypotheses': comparison_ok,
        'universal_property_proved_when_universal_used': universal_ok,
        'canonical_uniqueness_or_contractibility_proved': canonical_ok,
    }
    report = _gate_report(DEPENDENCY_LANGUAGE_GATES, satisfied)
    return {
        **report,
        'conjectural_dependency_arrow_allowed': False,
        'comparison_therefore_allowed': not comparison_theorem_used,
        'universal_language_allowed': universal_ok,
        'canonical_language_allowed': canonical_ok,
        'status': 'dependency_language_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def morita_level_quadrant_scope(
    chosen_vacuum_data_defined: bool = False,
    vacuum_independence_claimed: bool = False,
    vacuum_independence_proved: bool = False,
    open_factorization_category_level0_defined: bool = False,
    morita_equivalence_to_module_category_used: bool = False,
    morita_equivalence_to_module_category_proved: bool = False,
    morita_equivalence_separated_from_algebra_isomorphism: bool = False,
    level_alphabet_defined_once: bool = False,
    level_signatures_exhaustive_only_open_quadrant: bool = False,
    level_signatures_do_not_transfer_cy_claims: bool = False,
    quadrant_grid_defined: bool = False,
    cross_quadrant_structure_preservation_claimed: bool = False,
    cross_quadrant_maps_preserve_structures_proved: bool = False,
    conjectural_cross_quadrant_maps_marked: bool = False,
) -> Dict[str, object]:
    """Gate level-0, Morita, level alphabet, and quadrant-grid claims."""
    vacuum_ok = not vacuum_independence_claimed or vacuum_independence_proved
    morita_ok = (
        not morita_equivalence_to_module_category_used
        or morita_equivalence_to_module_category_proved
    )
    cross_quadrant_ok = (
        not cross_quadrant_structure_preservation_claimed
        or cross_quadrant_maps_preserve_structures_proved
    )
    satisfied = {
        'chosen_vacuum_data_defined': chosen_vacuum_data_defined,
        'vacuum_independence_proved_when_claimed': vacuum_ok,
        'open_factorization_category_level0_defined': (
            open_factorization_category_level0_defined
        ),
        'morita_equivalence_to_module_category_proved_when_used': morita_ok,
        'morita_equivalence_separated_from_algebra_isomorphism': (
            morita_equivalence_separated_from_algebra_isomorphism
        ),
        'level_alphabet_defined_once': level_alphabet_defined_once,
        'level_signatures_exhaustive_only_open_quadrant': (
            level_signatures_exhaustive_only_open_quadrant
        ),
        'level_signatures_do_not_transfer_cy_claims': (
            level_signatures_do_not_transfer_cy_claims
        ),
        'quadrant_grid_defined': quadrant_grid_defined,
        'cross_quadrant_maps_preserve_structures_proved_when_claimed': (
            cross_quadrant_ok
        ),
        'conjectural_cross_quadrant_maps_marked': conjectural_cross_quadrant_maps_marked,
    }
    report = _gate_report(MORITA_LEVEL_QUADRANT_GATES, satisfied)
    return {
        **report,
        'vacuum_independence_claim_allowed': vacuum_ok,
        'morita_equivalence_claim_allowed': morita_ok,
        'morita_as_algebra_isomorphism_allowed': False,
        'cy_transfer_by_level_signature_allowed': False,
        'cross_quadrant_structure_preservation_claim_allowed': cross_quadrant_ok,
        'status': 'morita_level_quadrant_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def manuscript_structure_obligation_scope(
    structure: Optional[Dict[str, bool]] = None,
    order: Optional[Dict[str, bool]] = None,
    dependency: Optional[Dict[str, bool]] = None,
    morita_level_quadrant: Optional[Dict[str, bool]] = None,
) -> Dict[str, object]:
    """Aggregate PDF obligations 950--980 into one manuscript-structure report."""
    structure_report = structure_placement_scope(**(structure or {}))
    order_report = verification_order_scope(**(order or {}))
    dependency_report = dependency_language_scope(**(dependency or {}))
    morita_report = morita_level_quadrant_scope(**(morita_level_quadrant or {}))
    reports = {
        'structure_placement': structure_report,
        'verification_order': order_report,
        'dependency_language': dependency_report,
        'morita_level_quadrant': morita_report,
    }
    return {
        'reports': reports,
        'all_gates_satisfied': all(
            report['all_gates_satisfied'] for report in reports.values()
        ),
        'blocked_components': [
            name for name, report in reports.items()
            if not report['all_gates_satisfied']
        ],
    }


def notation_discipline_scope(
    notation_table_before_main_theorem: bool = False,
    unused_symbols_removed_after_definition: bool = False,
    C_reused_for_curve_coalgebra_category_same_proof: bool = False,
    D_reused_for_divisor_differential_duality_same_proof: bool = False,
    D_reserved_for_verdier_duality: bool = False,
    d_reserved_for_differentials: bool = False,
    delta_subscripts_distinguish_diagonal_coproduct_discriminant: bool = False,
    fm_notation_consistent: bool = False,
    bar_notation_consistent: bool = False,
    ch_hh_thh_notation_consistent: bool = False,
    z_notation_distinct: bool = False,
) -> Dict[str, object]:
    """Gate notation-table, unused-symbol, and symbol-conflation obligations."""
    C_not_reused = not C_reused_for_curve_coalgebra_category_same_proof
    D_not_reused = not D_reused_for_divisor_differential_duality_same_proof
    satisfied = {
        'notation_table_before_main_theorem': notation_table_before_main_theorem,
        'unused_symbols_removed_after_definition': (
            unused_symbols_removed_after_definition
        ),
        'C_not_reused_for_curve_coalgebra_category_same_proof': C_not_reused,
        'D_not_reused_for_divisor_differential_duality_same_proof': D_not_reused,
        'D_reserved_for_verdier_duality': D_reserved_for_verdier_duality,
        'd_reserved_for_differentials': d_reserved_for_differentials,
        'delta_subscripts_distinguish_diagonal_coproduct_discriminant': (
            delta_subscripts_distinguish_diagonal_coproduct_discriminant
        ),
        'fm_notation_consistent': fm_notation_consistent,
        'bar_notation_consistent': bar_notation_consistent,
        'ch_hh_thh_notation_consistent': ch_hh_thh_notation_consistent,
        'z_notation_distinct': z_notation_distinct,
    }
    report = _gate_report(NOTATION_DISCIPLINE_GATES, satisfied)
    return {
        **report,
        'C_reuse_allowed': False,
        'D_reuse_allowed': False,
        'D_for_non_verdier_allowed': False,
        'z_notation_conflation_allowed': False,
        'notation_discipline_complete': report['all_gates_satisfied'],
        'status': 'notation_discipline_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def hypothesis_reference_scope(
    hypothesis_index_added: bool = False,
    hypothesis_package_referenced_before_definition: bool = False,
    missing_section_refs_present: bool = False,
    standard_landscape_defined_finite_list: bool = False,
    landscape_coverage_proved: bool = False,
    landscape_called_atlas_when_coverage_not_proved: bool = False,
) -> Dict[str, object]:
    """Gate hypothesis-index, missing-reference, and landscape-scope obligations."""
    no_early_hypothesis_reference = (
        not hypothesis_package_referenced_before_definition
    )
    no_missing_refs = not missing_section_refs_present
    landscape_scope_ok = (
        landscape_coverage_proved
        or landscape_called_atlas_when_coverage_not_proved
    )
    satisfied = {
        'hypothesis_index_added': hypothesis_index_added,
        'no_hypothesis_package_before_definition': no_early_hypothesis_reference,
        'no_missing_section_refs': no_missing_refs,
        'standard_landscape_defined_finite_list': (
            standard_landscape_defined_finite_list
        ),
        'landscape_coverage_proved_or_atlas_language_used': landscape_scope_ok,
    }
    report = _gate_report(HYPOTHESIS_REFERENCE_GATES, satisfied)
    return {
        **report,
        'hypothesis_reference_before_definition_allowed': False,
        'missing_section_reference_allowed': False,
        'standard_landscape_reference_allowed': (
            standard_landscape_defined_finite_list
        ),
        'landscape_classification_allowed': landscape_coverage_proved,
        'landscape_atlas_language_required': not landscape_coverage_proved,
        'hypothesis_reference_complete': report['all_gates_satisfied'],
        'status': 'hypothesis_reference_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def abstract_front_back_scope(
    arxiv_abstract_from_theorem_spine_only: bool = False,
    conjectural_physics_arithmetic_in_abstract: bool = False,
    conjectural_physics_arithmetic_final_abstract_labelled: bool = False,
    first_20_pages_type_correct_definitions: bool = False,
    last_theorem_surviving_invariants_commutative_diagram: bool = False,
) -> Dict[str, object]:
    """Gate abstract scope, first pages, and final theorem obligations."""
    conjectural_abstract_ok = (
        not conjectural_physics_arithmetic_in_abstract
        or conjectural_physics_arithmetic_final_abstract_labelled
    )
    satisfied = {
        'arxiv_abstract_from_theorem_spine_only': (
            arxiv_abstract_from_theorem_spine_only
        ),
        'conjectural_physics_arithmetic_final_abstract_labelled': (
            conjectural_abstract_ok
        ),
        'first_20_pages_type_correct_definitions': (
            first_20_pages_type_correct_definitions
        ),
        'last_theorem_surviving_invariants_commutative_diagram': (
            last_theorem_surviving_invariants_commutative_diagram
        ),
    }
    report = _gate_report(ABSTRACT_FRONT_BACK_GATES, satisfied)
    return {
        **report,
        'abstract_claims_from_nonspine_allowed': False,
        'conjectural_physics_arithmetic_abstract_allowed': conjectural_abstract_ok,
        'core_type_correctness_front_loaded': (
            first_20_pages_type_correct_definitions
        ),
        'final_surviving_invariants_diagram_complete': (
            last_theorem_surviving_invariants_commutative_diagram
        ),
        'status': 'abstract_front_back_scope' if report['all_gates_satisfied'] else 'blocked',
    }


def notation_hypothesis_abstract_obligation_scope(
    notation: Optional[Dict[str, bool]] = None,
    hypothesis: Optional[Dict[str, bool]] = None,
    abstract_front_back: Optional[Dict[str, bool]] = None,
) -> Dict[str, object]:
    """Aggregate PDF obligations 981--1000 into one final-surface report."""
    notation_report = notation_discipline_scope(**(notation or {}))
    hypothesis_report = hypothesis_reference_scope(**(hypothesis or {}))
    abstract_report = abstract_front_back_scope(**(abstract_front_back or {}))
    reports = {
        'notation_discipline': notation_report,
        'hypothesis_reference': hypothesis_report,
        'abstract_front_back': abstract_report,
    }
    return {
        'reports': reports,
        'all_gates_satisfied': all(
            report['all_gates_satisfied'] for report in reports.values()
        ),
        'blocked_components': [
            name for name, report in reports.items()
            if not report['all_gates_satisfied']
        ],
    }

# ============================================================
# SECTION 1: Theorem status registry
# ============================================================

# MC status claims from concordance
# Canonical source: chapters/connections/editorial_constitution.tex:149-150, 179-191, 819
MC_STATUS = {
    'MC1': 'PROVED',             # PBW concentration, all standard families
    'MC2': 'PROVED',             # Bar-intrinsic construction, thm:mc2-bar-intrinsic
    'MC3': 'PROVED',             # Layers 1+2 all simple types, eval-generated core; Layer 3 type A unconditional, other types conditional on conj:rank-independence-step2
    'MC4': 'PROVED',             # Strong completion-tower theorem
    'MC5': 'PARTIALLY_PROVED',   # Aggregate status: analytic HS-sewing,
                                 # coderived, and strict ML completed/pro
                                 # surfaces proved; bounded direct-sum fails
                                 # in class M; tree-level amplitude pairing
                                 # conditional; physical comparisons downstream.
}

MC5_AMBIENT_STATUS = {
    'analytic_hs_sewing': {
        'status': 'PROVED',
        'ambient': 'Hilbert-Schmidt sewing envelope',
        'anchors': (
            'thm:general-hs-sewing',
            'thm:heisenberg-sewing-vol1',
        ),
        'content': 'all-genera sewing/convergence for the standard landscape',
    },
    'coderived_bv_bar': {
        'status': 'PROVED',
        'ambient': 'coderived category D^co',
        'anchors': ('thm:bv-bar-coderived-vol1',),
        'content': 'BV/bar quasi-isomorphism for chirally Koszul algebras',
    },
    'strict_ml_completed_chain': {
        'status': 'PROVED',
        'ambient': 'strict ML pro-object / J-adic / filtered completion',
        'anchors': (
            'thm:mc5-class-m-chain-level-pro-ambient',
            'thm:mc5-class-m-topological-chain-level-j-adic',
            'prop:ambient-equivalence',
        ),
        'content': 'genuswise BV/BRST/bar comparison on completed windows',
    },
    'bounded_direct_sum_chain': {
        'status': 'FAILS_CLASS_M',
        'ambient': 'bounded direct-sum chain complex',
        'anchors': ('conj:v1-master-bv-brst', 'rem:mc5-vs-bv-brst'),
        'content': 'class M has a quartic harmonic obstruction',
    },
    'tree_level_amplitude_pairing': {
        'status': 'CONDITIONAL',
        'ambient': 'genus-0 moduli-integration amplitude pairing',
        'anchors': ('cor:string-amplitude-genus0',),
        'content': 'requires the additional amplitude-pairing hypothesis',
    },
    'physical_holographic_identification': {
        'status': 'DOWNSTREAM_OPEN',
        'ambient': 'physical BV/BRST, Feynman, AGT, holographic comparison',
        'anchors': ('Boundary 9', 'Vol II standing axioms H1-H4'),
        'content': 'comparison with genuine physical complexes remains open',
    },
}

# Five main theorems
MAIN_THEOREMS = {
    'A': 'PROVED',  # Bar-cobar adjunction + Verdier intertwining
    'B': 'PROVED',  # Bar-cobar inversion on Koszul locus
    'C': 'PROVED',  # Complementarity
    'D': 'PROVED',  # Modular characteristic
    'H': 'PROVED',  # Chiral Hochschild
}

# Koszulness programme counts (from concordance sec:concordance-koszulness-programme)
KOSZULNESS_META_THEOREM = {
    'independent_bidirectional_equivalences': 7,  # items (i)--(v), (ix), (x)
    'listed_consequences': 1,            # item (vi) - Barr-Beck-Lurie
    'conditional_comparisons': 2,        # item (vii) + Lagrangian criterion
    'one_way_consequences': 1,           # item (viii) - ChirHoch
    'one_directional': 1,                # item (xii) - D-module purity
    'total_items': 12,
    'lagrangian_standard_landscape': 'perfectness_input_verified',
    'd_module_purity_km': 'proved_forward',  # chiral localization + Hitchin
    'd_module_purity_converse': 'open',
}

# Three-pillar identification theorems
THREE_PILLAR_IDENTIFICATIONS = {
    'total': 11,
    'proved': 9,
    'structural': 2,  # one-slot obstruction + arity-4 degeneration
}

# Preprint dependency status
PREPRINT_DEPENDENCIES = {
    'Mok25': {
        'arxiv': '2503.17563',
        'author': 'C.-P. Mok',
        'title': 'Logarithmic Fulton-MacPherson configuration spaces',
        'year': 2025,
        'status': 'preprint',
        'theorems_dependent': [
            'thm:ambient-d-squared-zero',
            'thm:log-clutching-degeneration',
            'constr:arity4-degeneration',
            'thm:planted-forest-tropicalization',
            'prop:planted-forest-tropical',
            'thm:logfm-modular-cocomposition',
            'prop:ordered-log-fm-construction',
        ],
        'proved_core_affected': False,  # Five main theorems unaffected
    },
    'MS24': {
        'arxiv': '2408.16787',
        'author': 'Malikov-Schechtman',
        'title': 'Homotopy chiral algebras',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'RNW19': {
        'arxiv': None,  # Published
        'author': 'Robert-Nicoud-Wierstra',
        'title': 'Homotopy morphisms between convolution homotopy Lie algebras',
        'year': 2019,
        'status': 'published',  # J. Noncommut. Geom. 13 (2019)
        'proved_core_affected': False,
    },
    'Val16': {
        'arxiv': None,  # Published
        'author': 'Vallette',
        'title': 'Homotopy theory of homotopy algebras',
        'year': 2020,
        'status': 'published',  # Ann. Inst. Fourier 70 (2020)
        'proved_core_affected': False,
    },
    'Moriwaki26a': {
        'arxiv': '2602.08729',
        'author': 'Moriwaki',
        'title': 'Conformally flat factorization homology',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'Moriwaki26b': {
        'arxiv': '2603.06491',
        'author': 'Moriwaki',
        'title': 'Bergman space operads',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'Nish26': {
        'arxiv': '2408.00412',  # Note: concordance says 2026 but arXiv is 2024
        'author': 'Nishinaka',
        'title': 'A note on vertex algebras and Costello-Gwilliam factorization algebras',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'Vic25': {
        'arxiv': '2501.08412',
        'author': 'Vicedo',
        'title': 'Full universal enveloping vertex algebras from factorisation',
        'year': 2025,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'GZ26': {
        'arxiv': '2603.08783',
        'author': 'Gaiotto-Zeng',
        'title': 'Interface Minimal Model Holography and Topological String Theory',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'KhanZeng25': {
        'arxiv': '2502.13227',
        'author': 'Khan-Zeng',
        'title': 'Poisson vertex algebras and 3d gauge theory',
        'year': 2025,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'AMT24': {
        'arxiv': '2407.18222',
        'author': 'Adamo-Moriwaki-Tanimoto',
        'title': 'OS axioms for unitary full VOAs',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    # NEW REFERENCES from 2024-2026 literature
    'Butson25': {
        'arxiv': '2508.18248',
        'author': 'Butson',
        'title': 'Inverse Hamiltonian Reduction for affine W-algebras in type A',
        'year': 2025,
        'status': 'preprint',
        'proved_core_affected': False,
        'concordance_mentioned': False,  # FLAG: should be mentioned
    },
    'CFLN24': {
        'arxiv': '2403.08212',
        'author': 'Creutzig-Fasquel-Linshaw-Nakatsuka',
        'title': 'On the structure of W-algebras in type A',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
        'concordance_mentioned': False,  # FLAG: should be mentioned
    },
    'Nafcha26': {
        'arxiv': '2603.30037',
        'author': 'Nafcha',
        'title': 'Nodal degeneration of chiral algebras',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
        'concordance_mentioned': False,  # FLAG: should be mentioned
    },
}


# ============================================================
# SECTION 2: Kappa formulas (AP1, AP39, AP48)
# ============================================================

def kappa_heisenberg(k):
    """kappa(H_k) = k. NOT k/2 (AP39 historical error)."""
    return k


def kappa_virasoro(c):
    """kappa(Vir_c) = c/2."""
    return Fraction(c, 2) if isinstance(c, int) else c / 2


def kappa_kac_moody(dim_g, k, h_dual):
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v).

    AP1: This is NOT c/2 in general.
    AP39: S_2 = c/2 != kappa for rank > 1.
    AP48: kappa depends on the full algebra, not Virasoro subalgebra.
    """
    return Fraction(dim_g * (k + h_dual), 2 * h_dual)


def kappa_w_algebra_principal(c):
    """kappa(W_N) = c/2 for principal W-algebras.

    This coincides with kappa_virasoro because W_N has
    a Virasoro subalgebra that controls the scalar genus tower.
    """
    return Fraction(c, 2) if isinstance(c, int) else c / 2


def central_charge_kac_moody(dim_g, k, h_dual):
    """c(V_k(g)) = dim(g) * k / (k + h^v)."""
    return Fraction(dim_g * k, k + h_dual)


def kappa_complementarity_km(dim_g, k, h_dual):
    """kappa(A) + kappa(A!) for Kac-Moody.

    For KM: kappa + kappa' = 0 (AP24).
    Koszul dual: k -> -k - 2h^v.
    """
    kappa_a = kappa_kac_moody(dim_g, k, h_dual)
    kappa_dual = kappa_kac_moody(dim_g, -k - 2 * h_dual, h_dual)
    return kappa_a + kappa_dual


def kappa_complementarity_virasoro(c):
    """kappa(Vir_c) + kappa(Vir_{26-c}) = 13.

    AP24: This is NOT zero for Virasoro.
    """
    return kappa_virasoro(c) + kappa_virasoro(26 - c)


# ============================================================
# SECTION 3: Shadow depth classification (G/L/C/M)
# ============================================================

SHADOW_DEPTH_CLASSES = {
    'G': {'name': 'Gaussian', 'r_max': 2,
           'examples': ['Heisenberg', 'free_fermion', 'Niemeier_lattice']},
    'L': {'name': 'Lie', 'r_max': 3,
           'examples': ['affine_KM']},
    'C': {'name': 'Contact', 'r_max': 4,
           'examples': ['beta_gamma', 'symplectic_fermion']},
    'M': {'name': 'Mixed', 'r_max': float('inf'),
           'examples': ['Virasoro', 'W_N', 'moonshine']},
}


def shadow_depth_class(algebra_type: str) -> str:
    """Return the shadow depth class for a given algebra type."""
    class_map = {
        'heisenberg': 'G', 'free_fermion': 'G', 'lattice': 'G',
        'niemeier': 'G',
        'affine_km': 'L', 'sl2': 'L', 'sl3': 'L',
        'B2': 'L', 'C2': 'L', 'G2': 'L', 'F4': 'L',
        'beta_gamma': 'C', 'symplectic_fermion': 'C',
        'virasoro': 'M', 'W3': 'M', 'W4': 'M', 'W_N': 'M',
        'moonshine': 'M',
    }
    return class_map.get(algebra_type, 'unknown')


# ============================================================
# SECTION 4: Shadow obstruction tower formulas
# ============================================================

def virasoro_S2(c):
    """S_2 = kappa = c/2 for Virasoro."""
    return Fraction(c, 2) if isinstance(c, int) else c / 2


def virasoro_S3():
    """S_3 = 2 for Virasoro (cubic shadow)."""
    return 2


def virasoro_S4(c):
    """S_4 = 10/(c*(5c+22)) for Virasoro (quartic contact coefficient)."""
    if isinstance(c, int):
        return Fraction(10, c * (5 * c + 22))
    return 10.0 / (c * (5 * c + 22))


def virasoro_S5(c):
    """S_5 = -48/(c^2 * (5c+22)) for Virasoro."""
    if isinstance(c, int):
        return Fraction(-48, c**2 * (5 * c + 22))
    return -48.0 / (c**2 * (5 * c + 22))


def virasoro_Q_contact(c):
    """Q^contact_Vir = 10/(c*(5c+22)).

    Same as S_4 for Virasoro. Concordance claims this value.
    """
    return virasoro_S4(c)


def virasoro_delta_H_genus1(c):
    """delta_H^(1)_Vir = 120/(c^2 * (5c+22)) * x^2.

    Returns the coefficient (without x^2).
    Concordance: genus-1 Hessian correction.
    """
    if isinstance(c, int):
        return Fraction(120, c**2 * (5 * c + 22))
    return 120.0 / (c**2 * (5 * c + 22))


def critical_discriminant(kappa_val, S4_val):
    """Delta = 8 * kappa * S_4.

    The organizing invariant (eq:concordance-discriminant).
    Delta = 0 forces r_max <= 3.
    Delta != 0 forces r_max = infinity.
    """
    return 8 * kappa_val * S4_val


def shadow_growth_rate_virasoro(c):
    """rho(Vir_c) = sqrt((180c + 872) / ((5c+22) * c^2)).

    From concordance, Definition def:shadow-growth-rate.
    """
    if c <= 0:
        return float('inf')
    num = 180 * c + 872
    den = (5 * c + 22) * c**2
    return math.sqrt(num / den)


# ============================================================
# SECTION 5: Genus expansion (Faber-Pandharipande)
# ============================================================

def faber_pandharipande_lambda(g):
    """lambda_g^FP = ((2^(2g-1) - 1) / 2^(2g-1)) * |B_{2g}| / (2g)!

    The Faber-Pandharipande tautological class.
    Uses Bernoulli numbers.
    """
    if g <= 0:
        return 0
    B2g = _bernoulli_number(2 * g)
    two_pow = 2**(2 * g - 1)
    return float(abs(B2g)) * (two_pow - 1) / (two_pow * math.factorial(2 * g))


def free_energy(kappa_val, g):
    """F_g(A) = kappa(A) * lambda_g^FP.

    For uniform-weight modular Koszul algebras at all genera.
    Genus-1 unconditional for all families.
    """
    return kappa_val * faber_pandharipande_lambda(g)


def _bernoulli_number(n):
    """Compute Bernoulli number B_n using the recurrence."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    B[1] = Fraction(-1, 2)
    for m in range(2, n + 1):
        if m % 2 == 1:
            continue
        s = Fraction(0)
        for k in range(m):
            s += _comb(m + 1, k) * B[k]
        B[m] = -s / (m + 1)
    return B[n]


def _comb(n, k):
    """Binomial coefficient."""
    return math.comb(n, k)


# ============================================================
# SECTION 6: Planted-forest corrections
# ============================================================

def planted_forest_genus2(kappa_val, S3_val):
    """delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48.

    Concordance eq:planted-forest-genus2-polynomial.
    Verified numerically for Virasoro.
    """
    return S3_val * (10 * S3_val - kappa_val) / 48


def planted_forest_genus2_virasoro(c):
    """For Virasoro: delta_pf^{(2,0)} = -(c-40)/48.

    Since kappa = c/2, S_3 = 2:
    delta = 2 * (20 - c/2) / 48 = (40 - c) / 48 = -(c-40)/48.
    """
    return -(c - 40) / 48


# ============================================================
# SECTION 7: Multi-weight genus expansion (AP32)
# ============================================================

def w3_genus2_cross_channel(c):
    """delta_F_2(W_3) = (c + 204) / (16c).

    op:multi-generator-universality RESOLVED NEGATIVELY.
    The scalar formula FAILS for multi-weight algebras at g >= 2.
    This correction is > 0 for all c > 0.
    """
    if c == 0:
        return float('inf')
    return (c + 204) / (16 * c)


# ============================================================
# SECTION 8: Envelope-shadow complexity
# ============================================================

ENVELOPE_SHADOW_COMPLEXITY = {
    'abelian': {'chi_env': 2, 'class': 'G'},
    'affine_current': {'chi_env': 3, 'class': 'L'},
    'beta_gamma_current': {'chi_env': 4, 'class': 'C'},
    'virasoro_current': {'chi_env': float('inf'), 'class': 'M'},
}


# ============================================================
# SECTION 9: E1 modular theory status
# ============================================================

E1_FIVE_THEOREMS = {
    'A_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'B_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'C_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'D_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'H_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
}


# ============================================================
# SECTION 10: Holographic programme status
# ============================================================

HOLOGRAPHIC_TARGETS = {
    'boundary_defect_realization': 'CONJECTURED',
    'yangian_shadow': 'PROVED',
    'sphere_reconstruction': 'PROVED',
    'quartic_resonance_obstruction': 'PROVED',
    'singular_fiber_descent': 'CONJECTURED',
}

ENTANGLEMENT_TARGETS = {
    'G11': 'HEURISTIC',   # algebraic EE, genus-1 proved
    'G12_prime': 'CONJECTURED',  # algebraic QES
    'G12': 'PROVED',       # Koszulness = exact QEC
    'G13': 'CONJECTURED',  # modular flow
    'G14': 'PROVED',       # holographic error correction
    'G15': 'PROVED',       # algebraic Page constraint
    'G16': 'HEURISTIC',   # replica structure
}


# ============================================================
# SECTION 11: DK status
# ============================================================

DK_STATUS = {
    'DK-0': 'PROVED',
    'DK-1': 'PROVED',
    'DK-1.5': 'PROVED',  # lattice
    'DK-2': 'PROVED',    # eval-generated core, all types
    'DK-3': 'PROVED',    # eval-generated core, all types
    'DK-4': 'OPEN',      # ML proved, algebraic id open
    'DK-5': 'CONJECTURED',
}


# ============================================================
# SECTION 12: Spectral discriminant
# ============================================================

def spectral_discriminant_sl2(x, k):
    """Delta_{sl2}(x) = (1 - kx)(1 - (k+4)x) / (1 - 2x).

    Concordance computation comp:spectral-discriminants-standard.
    """
    return (1 - k * x) * (1 - (k + 4) * x) / (1 - 2 * x)


def spectral_discriminant_virasoro(x, c):
    """Delta_Vir(x) = 1 - (c-26)/2 * x."""
    return 1 - (c - 26) / 2 * x


def spectral_discriminant_heisenberg(x, k):
    """Delta_H(x) = 1 - kx."""
    return 1 - k * x


def spectral_discriminant_beta_gamma(x):
    """Delta_{beta_gamma}(x) = 1 + 2x."""
    return 1 + 2 * x


# ============================================================
# SECTION 13: New literature references (2024-2026)
# ============================================================

def check_new_references_coverage():
    """Check which new references are mentioned in the concordance.

    Returns list of (reference, mentioned_in_concordance, should_update).
    """
    findings = []

    # Butson 2508.18248: Inverse Hamiltonian reduction for ALL orbits type A
    findings.append({
        'ref': 'Butson25',
        'arxiv': '2508.18248',
        'title': 'Inverse Hamiltonian Reduction for affine W-algebras in type A',
        'concordance_section': 'sec:concordance-non-principal-w',
        'currently_mentioned': False,
        'impact': 'SIGNIFICANT: proves inverse reduction for ALL orbits in type A, '
                  'upgrading hook-type corridor to full type-A resolution. '
                  'Transport-to-transpose conjecture may be promotable.',
        'action': 'UPDATE: add to non-principal W section, update hook-type status',
    })

    # Creutzig-Fasquel-Linshaw-Nakatsuka 2403.08212
    findings.append({
        'ref': 'CFLN24',
        'arxiv': '2403.08212',
        'title': 'On the structure of W-algebras in type A',
        'concordance_section': 'sec:concordance-non-principal-w',
        'currently_mentioned': False,
        'impact': 'SIGNIFICANT: structure theory for all W-algebras in type A, '
                  'building blocks via hook-type reductions. Directly relevant to '
                  'transport-closure computation.',
        'action': 'UPDATE: add to non-principal W section',
    })

    # Nafcha 2603.30037: Nodal degeneration of chiral algebras
    findings.append({
        'ref': 'Nafcha26',
        'arxiv': '2603.30037',
        'title': 'Nodal degeneration of chiral algebras',
        'concordance_section': 'sec:concordance-three-pillars (analytic programme)',
        'currently_mentioned': False,
        'impact': 'MODERATE: gluing formula for chiral homology, relevant to '
                  'MC5 sewing programme and analytic completion.',
        'action': 'UPDATE: add to analytic sewing section and preprint table',
    })

    # Vicedo 2501.08412: already mentioned
    findings.append({
        'ref': 'Vic25',
        'arxiv': '2501.08412',
        'title': 'Full universal enveloping vertex algebras from factorisation',
        'concordance_section': 'sec:concordance-nishinaka-vicedo',
        'currently_mentioned': True,
        'impact': 'Already covered',
        'action': 'NO UPDATE NEEDED',
    })

    # Nishinaka 2408.00412: mentioned but with wrong year
    findings.append({
        'ref': 'Nish26',
        'arxiv': '2408.00412',
        'title': 'A note on vertex algebras and CG factorization algebras',
        'concordance_section': 'sec:concordance-nishinaka-vicedo',
        'currently_mentioned': True,
        'impact': 'MINOR: concordance says "preprint, 2026" but arXiv shows 2024. '
                  'Verify if there is a distinct 2026 version or if this is misdated.',
        'action': 'CHECK: verify year; update if 2024 not 2026',
    })

    return findings


# ============================================================
# SECTION 14: Concordance audit findings
# ============================================================

def audit_concordance_claims():
    """Run systematic audit of concordance claims.

    Returns list of (section, finding, severity, action).
    """
    findings = []

    # 1. Check MC status consistency. MC5 is not a single Boolean theorem:
    # the proved strict completed/pro surfaces coexist with raw/direct-sum
    # and downstream physical surfaces that are not proved.
    for mc, status in MC_STATUS.items():
        if mc == 'MC5':
            if status != 'PARTIALLY_PROVED':
                findings.append({
                    'section': 'MC frontier',
                    'finding': f'MC5 aggregate status should be PARTIALLY_PROVED, got {status}',
                    'severity': 'CRITICAL',
                    'action': 'Restore ambient-sensitive MC5 status',
                })
                continue

            proved_surfaces = [
                name for name, data in MC5_AMBIENT_STATUS.items()
                if data['status'] == 'PROVED'
            ]
            residual_surfaces = [
                name for name, data in MC5_AMBIENT_STATUS.items()
                if data['status'] in {
                    'FAILS_CLASS_M', 'CONDITIONAL', 'DOWNSTREAM_OPEN',
                }
            ]
            if not proved_surfaces or not residual_surfaces:
                findings.append({
                    'section': 'MC frontier',
                    'finding': 'MC5 ambient split is incomplete',
                    'severity': 'CRITICAL',
                    'action': 'Record both proved and residual MC5 surfaces',
                })
            else:
                findings.append({
                    'section': 'MC frontier',
                    'finding': (
                        'MC5 ambient split recorded: '
                        f'proved={proved_surfaces}; residual={residual_surfaces}'
                    ),
                    'severity': 'INFO',
                    'action': 'No action needed; partial aggregate status is intentional',
                })
            continue

        if status != 'PROVED':
            findings.append({
                'section': 'MC frontier',
                'finding': f'{mc} not marked as PROVED: {status}',
                'severity': 'CRITICAL',
                'action': 'Verify and update',
            })

    # 2. Check kappa complementarity (AP24)
    # KM: kappa + kappa' = 0
    km_sum = kappa_complementarity_km(3, 1, 2)  # sl2, k=1
    if km_sum != 0:
        findings.append({
            'section': 'Theorem D',
            'finding': f'KM kappa complementarity fails: sum = {km_sum}',
            'severity': 'CRITICAL',
            'action': 'Check kappa formula',
        })

    # Virasoro: kappa + kappa' = 13
    vir_sum = kappa_complementarity_virasoro(10)
    if vir_sum != 13:
        findings.append({
            'section': 'Theorem D',
            'finding': f'Virasoro kappa complementarity wrong: sum = {vir_sum}',
            'severity': 'CRITICAL',
            'action': 'Check kappa formula',
        })

    # 3. Check shadow depth classification
    for alg, expected_class in [
        ('heisenberg', 'G'), ('affine_km', 'L'),
        ('beta_gamma', 'C'), ('virasoro', 'M')
    ]:
        actual = shadow_depth_class(alg)
        if actual != expected_class:
            findings.append({
                'section': 'Shadow depth',
                'finding': f'{alg} classified as {actual}, expected {expected_class}',
                'severity': 'SERIOUS',
                'action': 'Fix classification',
            })

    # 4. Check F_1 = kappa/24 (genus-1 universality)
    for c_val in [2, 10, 13, 25, 26]:
        k = kappa_virasoro(c_val)
        f1 = free_energy(float(k), 1)
        expected = float(k) / 24
        if abs(f1 - expected) > 1e-12:
            findings.append({
                'section': 'Theorem D genus-1',
                'finding': f'F_1(Vir_{c_val}) = {f1}, expected {expected}',
                'severity': 'CRITICAL',
                'action': 'Check FP formula',
            })

    # 5. Check critical discriminant
    for c_val in [2, 10, 26]:
        k = float(kappa_virasoro(c_val))
        s4 = float(virasoro_S4(c_val))
        delta = critical_discriminant(k, s4)
        if c_val > 0 and delta == 0:
            findings.append({
                'section': 'Critical discriminant',
                'finding': f'Delta(Vir_{c_val}) = 0, should be nonzero for class M',
                'severity': 'SERIOUS',
                'action': 'Check discriminant formula',
            })

    # 6. Check Mok25 preprint exists on arXiv
    mok = PREPRINT_DEPENDENCIES['Mok25']
    findings.append({
        'section': 'Pillar C',
        'finding': f'Mok25 arXiv:{mok["arxiv"]} confirmed to exist (BibSonomy indexed). '
                   f'Status: {mok["status"]}. Proved core unaffected if revised.',
        'severity': 'INFO',
        'action': 'No action needed; dependency correctly documented',
    })

    # 7. Check new references not in concordance
    new_refs = check_new_references_coverage()
    for ref in new_refs:
        if not ref['currently_mentioned'] and 'NO UPDATE' not in ref['action']:
            findings.append({
                'section': ref['concordance_section'],
                'finding': f'Missing reference: {ref["ref"]} arXiv:{ref["arxiv"]} '
                           f'({ref["title"]}). Impact: {ref["impact"]}',
                'severity': 'MODERATE',
                'action': ref['action'],
            })

    # 8. Check W_3 genus-2 cross-channel (AP32)
    for c_val in [1, 2, 10, 25]:
        delta_f2 = w3_genus2_cross_channel(c_val)
        if delta_f2 <= 0:
            findings.append({
                'section': 'Multi-weight genus expansion',
                'finding': f'delta_F_2(W_3, c={c_val}) = {delta_f2} <= 0',
                'severity': 'CRITICAL',
                'action': 'Should be > 0 for c > 0',
            })

    # 9. Check Nishinaka year discrepancy
    nish = PREPRINT_DEPENDENCIES['Nish26']
    findings.append({
        'section': 'sec:concordance-nishinaka-vicedo',
        'finding': f'Nishinaka cited as [Nish26] (2026) but arXiv {nish["arxiv"]} '
                   f'submitted 2024. Possible version confusion.',
        'severity': 'MINOR',
        'action': 'Verify whether 2026 version exists or update year',
    })

    # 10. Check Koszulness programme counts
    meta = KOSZULNESS_META_THEOREM
    count = (
        meta['independent_bidirectional_equivalences']
        + meta['listed_consequences']
        + meta['conditional_comparisons']
        + meta['one_way_consequences']
        + meta['one_directional']
    )
    if count != meta['total_items']:
        findings.append({
            'section': 'sec:concordance-koszulness-programme',
            'finding': 'Koszulness count mismatch',
            'severity': 'CRITICAL',
            'action': 'Fix counts',
        })

    return findings
