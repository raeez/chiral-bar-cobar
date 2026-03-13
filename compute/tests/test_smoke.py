"""Cross-module smoke tests.

Verify that every public function in compute.lib can be called
with minimal valid inputs and produces non-trivial results.
"""

import pytest
from sympy import Rational, zeros

from compute.lib.ds_reduction import _nonprincipal_general_family_representative_items_in_range

GENERAL_SURVIVOR_COUPLED_SMOKE_RANKS = tuple(
    rank_n for rank_n in range(5, 13) if rank_n not in {10, 12}
)
GENERAL_SURVIVOR_COUPLED_RANK_10_REPRESENTATIVES = tuple(
    partition
    for partition, _ in _nonprincipal_general_family_representative_items_in_range(
        min_n=10,
        max_n=10,
    )
)
GENERAL_SURVIVOR_COUPLED_RANK_12_REPRESENTATIVES = tuple(
    partition
    for partition, _ in _nonprincipal_general_family_representative_items_in_range(
        min_n=12,
        max_n=12,
    )
)


def _assert_general_survivor_coupled_family_slice(
    rank_n: int,
    survivor_total_degree: int = 1,
) -> None:
    from compute.lib import (
        general_nonprincipal_survivor_coupled_family_holds_via_duality,
        verify_nonprincipal_general_survivor_coupled_family_via_duality_catalog,
    )

    assert all(
        verify_nonprincipal_general_survivor_coupled_family_via_duality_catalog(
            min_n=rank_n,
            max_n=rank_n,
            max_constraint_total_degree=1,
            survivor_total_degree=survivor_total_degree,
        ).values()
    )
    assert general_nonprincipal_survivor_coupled_family_holds_via_duality(
        min_n=rank_n,
        max_n=rank_n,
        max_constraint_total_degree=1,
        survivor_total_degree=survivor_total_degree,
    )


def _assert_general_survivor_coupled_representative_slice(
    partition: tuple[int, ...],
    survivor_total_degree: int = 1,
) -> None:
    from compute.lib.ds_reduction import (
        nonprincipal_partition_pair_survivor_coupled_representative_holds_via_duality,
    )

    assert nonprincipal_partition_pair_survivor_coupled_representative_holds_via_duality(
        partition,
        max_constraint_total_degree=1,
        survivor_total_degree=survivor_total_degree,
    )


class TestCoreTypes:
    def test_graded_vector_space(self):
        from compute.lib import GradedVectorSpace
        V = GradedVectorSpace({0: 1, 1: 3, 2: 5})
        assert V.dim(0) == 1
        assert V.dim(1) == 3

    def test_chain_complex(self):
        from compute.lib import GradedVectorSpace, ChainComplex
        spaces = GradedVectorSpace({0: 1, 1: 3, 2: 5})
        cc = ChainComplex(spaces)
        assert cc.spaces.dim(1) == 3

    def test_ope_algebra(self):
        from compute.lib import OPEAlgebra, Generator
        T = Generator("T", 2, 0)
        alg = OPEAlgebra([T], {}, name="test")
        assert len(alg.generators) == 1


class TestAlgebraConstructors:
    def test_heisenberg(self):
        from compute.lib import heisenberg_algebra
        H = heisenberg_algebra()
        assert len(H.generators) == 1

    def test_sl2(self):
        from compute.lib import sl2_algebra
        g = sl2_algebra()
        assert len(g.generators) == 3

    def test_virasoro(self):
        from compute.lib import virasoro_algebra
        V = virasoro_algebra()
        assert len(V.generators) == 1

    def test_free_fermion(self):
        from compute.lib import free_fermion_algebra
        F = free_fermion_algebra()
        assert len(F.generators) >= 1


class TestLieAlgebra:
    def test_cartan_data(self):
        from compute.lib import cartan_data
        cd = cartan_data("A", 1)
        assert cd.dim == 3
        assert cd.h_dual == 2

    def test_sugawara_c(self):
        from compute.lib import sugawara_c
        from sympy import Symbol
        k = Symbol('k')
        c = sugawara_c("A", 1, k)
        assert c.subs(k, 1) == 1

    def test_ff_dual_level(self):
        from compute.lib import ff_dual_level
        from sympy import Symbol, simplify
        k = Symbol('k')
        kp = ff_dual_level("A", 1, k)
        assert simplify(kp - (-k - 4)) == 0

    def test_kappa_km(self):
        from compute.lib import kappa_km
        from sympy import Symbol
        k = Symbol('k')
        kap = kappa_km("A", 1, k)
        assert kap is not None


class TestRegistries:
    def test_algebra_registry(self):
        from compute.lib import ALGEBRA_REGISTRY
        assert len(ALGEBRA_REGISTRY) == 11

    def test_known_bar_dims(self):
        from compute.lib import KNOWN_BAR_DIMS
        assert "sl2" in KNOWN_BAR_DIMS
        assert KNOWN_BAR_DIMS["sl2"][1] == 3

    def test_verify_bar_dim(self):
        from compute.lib import verify_bar_dim
        ok, msg = verify_bar_dim("sl2", 1, 3)
        assert ok


class TestKoszulHilbert:
    def test_riordan(self):
        from compute.lib import riordan
        # R(0)=1, R(1)=0, R(2)=1, R(3)=1, R(4)=3, R(5)=6
        assert riordan(4) == 3
        assert riordan(5) == 6
        assert riordan(6) == 15

    def test_motzkin(self):
        from compute.lib import motzkin
        assert motzkin(0) == 1
        assert motzkin(3) == 4
        assert motzkin(4) == 9

    def test_verify_koszul_sym_ext(self):
        from compute.lib import verify_koszul
        from math import comb
        h_sym = [comb(k + 2, k) for k in range(5)]
        h_ext = [comb(3, k) for k in range(4)] + [0]
        assert verify_koszul(h_sym, h_ext)


class TestOrlikSolomon:
    def test_os_dimension(self):
        from compute.lib import os_dimension
        assert os_dimension(2, 1) == 1
        assert os_dimension(3, 2) == 2

    def test_os_basis(self):
        from compute.lib import os_basis
        b = os_basis(3, 2)
        assert len(b) == 2

    def test_residue_map(self):
        from compute.lib import residue_map
        r = residue_map(3, 2, 0, 1)
        assert r is not None


class TestUtilities:
    def test_partition_number(self):
        from compute.lib import partition_number
        assert partition_number(0) == 1
        assert partition_number(5) == 7

    def test_lambda_fp(self):
        from compute.lib import lambda_fp
        from fractions import Fraction
        lam1 = lambda_fp(1)
        assert lam1 == Fraction(1, 24)

    def test_F_g(self):
        from compute.lib import F_g
        from fractions import Fraction
        f1 = F_g(1, 1)
        assert f1 == Fraction(1, 24)


class TestInfiniteGeneratorFrontier:
    def test_pronilpotent_completion_exports(self):
        from compute.lib import (
            w_infinity_weight_sector,
            verify_w_infinity_completion,
        )
        assert (2, 2) in w_infinity_weight_sector(4)[2]
        assert all(verify_w_infinity_completion(6).values())

    def test_w_infinity_ope_exports(self):
        from compute.lib import (
            TruncatedWinfinityOPE,
            TruncatedWinfinitySupportComplex,
            verify_truncated_w_infinity_ope,
            verify_w_infinity_support_complex,
            completed_bar_candidate_descriptor,
            stage4_dual_goal_report,
            stage4_primitive_square_class_report,
            stage4_pairing_reduction_report,
            stage4_primitive_transport_report,
            stage4_borcherds_transport_report,
            stage4_two_primitive_square_closure_report,
            stage4_local_attack_order_report,
            stage4_target_packet_at_level,
            stage4_defect_vanishing_report,
            stage5_dual_frontier_report,
            stage5_local_attack_order_report,
            stage5_visible_pairing_normal_form_report,
            stage5_principal_one_coefficient_normal_form_report,
            stage5_principal_target5_no_new_independent_data_report,
            stage5_principal_residual_front_one_coefficient_report,
            stage5_principal_one_coefficient_factorization_report,
            stage5_effective_independent_frontier_report,
            stage5_one_coefficient_reduction_report,
            stage5_one_defect_family_report,
            stage5_conjecture_defect_dictionary_report,
            stage5_exact_remaining_input_report,
            stage5_visible_conjecture_network_collapse_report,
            stage5_one_coefficient_comparison_report,
            standard_winfinity_dual_candidate_report,
            verify_standard_winfinity_dual_candidate,
        )
        model = TruncatedWinfinityOPE(max_spin=5)
        support = TruncatedWinfinitySupportComplex(max_spin=5)
        descriptor = completed_bar_candidate_descriptor()
        goal = stage4_dual_goal_report()
        square_class = stage4_primitive_square_class_report()
        pairing = stage4_pairing_reduction_report()
        primitive_transport = stage4_primitive_transport_report()
        borcherds = stage4_borcherds_transport_report()
        two_primitive = stage4_two_primitive_square_closure_report()
        attack_order = stage4_local_attack_order_report()
        packet = stage4_target_packet_at_level(1)
        vanishing = stage4_defect_vanishing_report(1, packet)
        stage5 = stage5_dual_frontier_report()
        stage5_attack = stage5_local_attack_order_report()
        stage5_normal_form = stage5_visible_pairing_normal_form_report()
        stage5_principal_normal_form = stage5_principal_one_coefficient_normal_form_report()
        stage5_principal_target5 = stage5_principal_target5_no_new_independent_data_report()
        stage5_principal_residual = stage5_principal_residual_front_one_coefficient_report()
        stage5_principal_factorization = stage5_principal_one_coefficient_factorization_report()
        stage5_effective = stage5_effective_independent_frontier_report()
        stage5_reduction = stage5_one_coefficient_reduction_report()
        stage5_defect_family = stage5_one_defect_family_report()
        stage5_defect_dictionary = stage5_conjecture_defect_dictionary_report()
        stage5_exact = stage5_exact_remaining_input_report()
        stage5_network_collapse = stage5_visible_conjecture_network_collapse_report()
        stage5_one = stage5_one_coefficient_comparison_report()
        report = standard_winfinity_dual_candidate_report()
        assert model.generator_spins == (2, 3, 4, 5)
        assert support.weight_sector_basis(4) == ((4,), (2, 2))
        assert descriptor["kind"] == "inverse_limit_bar"
        assert goal["goal"] == "vanish all six stage-4 defects"
        assert square_class["primitive_count"] == 2
        assert pairing["sign_ratio"] == Rational(-3, 4)
        assert primitive_transport["transport_square_channel"]["ratio_to_c334"] == Rational(5, 7)
        assert borcherds["target_square_ratio"] == Rational(5, 7)
        assert len(two_primitive["independent_square_identity_channels"]) == 2
        assert attack_order["step_2"]["report"]["relation_channel"] == (3, 4, 4, 3)
        assert vanishing["all_vanish"] is True
        assert stage5["prerequisite_goal"] == "vanish all six stage-4 defects"
        assert stage5["reduced_packet_size"] == 11
        assert stage5_attack["visible_pairing_refinement"]["effective_transport_attack_order"] == (4, 3)
        assert stage5_normal_form["parameter"]["channel"] == (3, 5, 4, 4)
        assert stage5_normal_form["channel_normal_form"][(3, 4, 5, 2)]["ratio_to_A5"] == Rational(-5, 4)
        assert stage5_principal_normal_form["parameter"]["channel"] == (3, 5, 4, 4)
        assert stage5_principal_normal_form["channel_normal_form"][(4, 5, 3, 6)]["ratio_to_A5_DS"] == Rational(-3, 4)
        assert stage5_principal_target5["tail_ratio_to_target3"] == Rational(5, 3)
        assert stage5_principal_residual["determined_nonzero_channel"]["channel"] == (4, 5, 3, 6)
        assert stage5_principal_factorization["representative_channel"] == (3, 5, 4, 4)
        assert stage5_effective["representative_channel"] == (3, 5, 4, 4)
        assert stage5_reduction["reduction_goal"]["channel"] == (3, 5, 4, 4)
        assert stage5_defect_family["representative_defect"]["channel"] == (3, 5, 4, 4)
        assert stage5_defect_family["channel_defects"][(3, 4, 5, 2)]["ratio_to_D5"] == Rational(-5, 4)
        assert stage5_defect_dictionary["equivalent_surfaces"][
            "conj:winfty-stage5-block-45"
        ]["ratio_to_D5"] == Rational(-3, 4)
        assert stage5_defect_dictionary["automatic_surfaces"][
            "conj:winfty-stage5-transport-target-5"
        ]["defect_expression"] == 0
        assert stage5_exact["singleton_identity"]["channel"] == (3, 5, 4, 4)
        assert stage5_exact["principal_target5_corridor"]["representative_channel"] == (3, 5, 4, 4)
        assert stage5_network_collapse["comparison_goal"]["channel"] == (3, 5, 4, 4)
        assert stage5_network_collapse["automatic_surfaces"]["conj:winfty-stage5-block-55"]["channel"] == (
            5,
            5,
            4,
            6,
        )
        assert stage5_one["comparison_goal"]["channel"] == (3, 5, 4, 4)
        assert stage5_one["conjecture_defect_dictionary"]["representative_channel"] == (
            3,
            5,
            4,
            4,
        )
        assert report["stage4"]["virasoro_constraints"][(4, 4, 2, 6)]["expression"] == 2
        assert all(verify_truncated_w_infinity_ope(5, 7).values())
        assert all(verify_w_infinity_support_complex(5, 7).values())
        assert all(verify_standard_winfinity_dual_candidate().values())


@pytest.mark.slow
class TestNonprincipalFrontier:
    def test_nonprincipal_exports(self):
        from compute.lib import (
            hook_partition,
            subregular_partition,
            type_a_bv_dual,
            nonprincipal_hook_cases,
            hook_orbit_pair_profile,
            hook_orbit_pair_profile_catalog,
            nonprincipal_general_cases,
            verify_hook_orbit_pair_profile_catalog,
            verify_nonprincipal_general_orbit_scaffold,
            verify_nonprincipal_ds_orbit_scaffold,
        )
        assert hook_partition(5, 2) == (3, 1, 1)
        assert subregular_partition(4) == (3, 1)
        assert type_a_bv_dual((3, 1)) == (2, 1, 1)
        assert nonprincipal_hook_cases(5)
        assert nonprincipal_general_cases(6)
        assert hook_orbit_pair_profile(6, 2).source_positive_simple_root_count == 3
        assert len(hook_orbit_pair_profile_catalog(5)) == 6
        assert all(verify_hook_orbit_pair_profile_catalog(7).values())
        assert all(verify_nonprincipal_general_orbit_scaffold(7).values())
        assert all(verify_nonprincipal_ds_orbit_scaffold(7).values())

    def test_nonprincipal_ds_seed_exports(self):
        from sympy import Rational
        from compute.lib import (
            bp_dual_level,
            bp_residual_sl2_level,
            bp_complementarity_constant,
            sl3_subregular_good_grading_multiplicities,
            bp_current_presentation,
            bp_strong_presentation,
            first_nonselfdual_hook_pair_nilpotent_matrices,
            first_nonselfdual_hook_pair_centralizer_bases,
            first_nonselfdual_hook_pair_f_centralizer_bases,
            first_nonselfdual_hook_pair_sl2_triples,
            ad_h_graded_basis_labels_sl_n,
            ad_h_grade_multiplicities_sl_n,
            matrix_centralizer_basis_sl_n,
            standard_traceless_basis_sl_n,
            nilpotent_partition_from_matrix,
            type_a_hook_nilpotent_matrix,
            hook_constraint_count_ansatz_type_a,
            hook_pair_constraint_counts_ansatz_type_a,
            verify_hook_constraint_count_ansatz,
            two_row_nonhook_partition,
            nonprincipal_two_row_case,
            nonprincipal_two_row_cases,
            nonprincipal_general_cases,
            nonprincipal_orbit_level_shift_type_a,
            type_a_general_nonprincipal_partitions,
            verify_nonprincipal_two_row_orbit_scaffold,
            verify_nonprincipal_general_orbit_scaffold,
            nonprincipal_hook_seed_catalog,
            nonprincipal_general_seed,
            nonprincipal_general_seed_catalog,
            nonprincipal_two_row_seed_catalog,
            verify_nonprincipal_general_seed_catalog,
            verify_nonprincipal_two_row_seed_catalog,
            verify_nonprincipal_hook_seed_catalog,
            verify_nonprincipal_ds_reduction_seed,
            hook_pair_constraints,
            hook_pair_positive_nilpotent_brackets,
            hook_pair_quadratic_ghost_term_support,
            hook_pair_current_action_terms,
            hook_pair_survivor_action_terms,
            hook_pair_survivor_coupled_blocks,
            hook_pair_mixed_blocks_match_under_dual_swap,
            hook_pair_nonlinear_blocks_match_under_dual_swap,
            hook_pair_survivor_coupled_blocks_match_under_dual_swap,
            nonprincipal_partition_pair_survivor_coupled_blocks,
            nonprincipal_partition_pair_mixed_blocks_match_under_dual_swap,
            nonprincipal_partition_pair_nonlinear_blocks_match_under_dual_swap,
            nonprincipal_partition_pair_survivor_coupled_blocks_match_under_dual_swap,
            nonprincipal_two_row_mixed_constraint_ghost_blocks,
            nonprincipal_two_row_nonlinear_mixed_constraint_ghost_blocks,
            nonprincipal_two_row_survivor_coupled_blocks,
            nonprincipal_two_row_mixed_blocks_match_under_dual_swap,
            nonprincipal_two_row_nonlinear_blocks_match_under_dual_swap,
            nonprincipal_two_row_survivor_coupled_blocks_match_under_dual_swap,
            hook_pair_mixed_family_holds_via_duality,
            verify_hook_pair_mixed_family_via_duality_catalog,
            hook_pair_nonlinear_family_holds_via_duality,
            verify_hook_pair_nonlinear_family_via_duality_catalog,
            hook_pair_survivor_coupled_family_holds_via_duality,
            verify_hook_pair_survivor_coupled_family_via_duality_catalog,
            nonprincipal_two_row_mixed_family_holds_via_duality,
            verify_nonprincipal_two_row_mixed_family_via_duality_catalog,
            nonprincipal_two_row_nonlinear_family_holds_via_duality,
            verify_nonprincipal_two_row_nonlinear_family_via_duality_catalog,
            nonprincipal_two_row_survivor_coupled_family_holds_via_duality,
            verify_nonprincipal_two_row_survivor_coupled_family_via_duality_catalog,
            general_nonprincipal_mixed_family_holds_via_duality,
            verify_nonprincipal_general_mixed_family_via_duality_catalog,
            general_nonprincipal_nonlinear_family_holds_via_duality,
            verify_nonprincipal_general_nonlinear_family_via_duality_catalog,
            hook_pair_surviving_field_candidates,
            hook_pair_reduced_brackets,
            survivor_coupled_block_has_square_zero,
            survivor_coupled_block_is_acyclic,
            centralizer_dimension_sl_n,
        )
        assert bp_dual_level(0) == -6
        assert bp_residual_sl2_level(0) == Rational(1, 2)
        assert bp_complementarity_constant() == 76
        assert sl3_subregular_good_grading_multiplicities()[0] == 2
        assert len(bp_current_presentation()) == 5
        assert len(bp_strong_presentation()) == 4
        assert nilpotent_partition_from_matrix(type_a_hook_nilpotent_matrix(4, 1)) == (3, 1)
        first_source, first_target = first_nonselfdual_hook_pair_nilpotent_matrices()
        assert len(matrix_centralizer_basis_sl_n(first_source)) == 5
        source_centralizer, target_centralizer = first_nonselfdual_hook_pair_centralizer_bases()
        source_f_centralizer, target_f_centralizer = first_nonselfdual_hook_pair_f_centralizer_bases()
        source_triple, target_triple = first_nonselfdual_hook_pair_sl2_triples()
        assert len(standard_traceless_basis_sl_n(4)) == 15
        assert nilpotent_partition_from_matrix(first_source) == (3, 1)
        assert nilpotent_partition_from_matrix(first_target) == (2, 1, 1)
        assert len(source_centralizer) == 5
        assert len(target_centralizer) == 9
        assert sum(len(items) for items in source_f_centralizer.values()) == 5
        assert sum(len(items) for items in target_f_centralizer.values()) == 9
        assert ad_h_graded_basis_labels_sl_n(source_triple.h)[4] == ("E13",)
        assert ad_h_grade_multiplicities_sl_n(source_triple.h)[4] == 1
        assert ad_h_grade_multiplicities_sl_n(target_triple.h)[1] == 4
        assert hook_constraint_count_ansatz_type_a(6, 2) == 3
        assert hook_pair_constraint_counts_ansatz_type_a(6, 2) == (3, 2)
        assert all(verify_hook_constraint_count_ansatz(7).values())
        assert two_row_nonhook_partition(6, 2) == (4, 2)
        assert nonprincipal_two_row_case(6, 2).dual_partition == (2, 2, 1, 1)
        assert nonprincipal_two_row_cases(7)
        assert type_a_general_nonprincipal_partitions(6)
        assert nonprincipal_general_cases(6)
        assert nonprincipal_orbit_level_shift_type_a((4, 2), 0) == -13
        assert nonprincipal_orbit_level_shift_type_a((3, 2, 1), 0) == -13
        assert all(verify_nonprincipal_two_row_orbit_scaffold(8).values())
        assert all(verify_nonprincipal_general_orbit_scaffold(7).values())
        source_constraints, target_constraints = hook_pair_constraints(6, 2)
        assert len(source_constraints) == 3
        assert len(target_constraints) == 2
        source_brackets, target_brackets = hook_pair_positive_nilpotent_brackets(6, 2)
        source_quad, target_quad = hook_pair_quadratic_ghost_term_support(6, 2)
        source_action, target_action = hook_pair_current_action_terms(6, 2)
        assert len(source_quad) == len(source_brackets)
        assert len(target_quad) == len(target_brackets)
        assert len(source_action) == 2 * len(source_brackets)
        assert len(target_action) == 2 * len(target_brackets)
        source_survivor_action, target_survivor_action = hook_pair_survivor_action_terms(6, 2)
        source_survivor_blocks, target_survivor_blocks = hook_pair_survivor_coupled_blocks(
            6,
            2,
            max_constraint_total_degree=1,
            survivor_total_degree=1,
        )
        assert source_survivor_action
        assert target_survivor_action
        assert all(
            survivor_coupled_block_has_square_zero(block) and survivor_coupled_block_is_acyclic(block)
            for block in source_survivor_blocks + target_survivor_blocks
        )
        assert hook_pair_mixed_blocks_match_under_dual_swap(6, 2, max_constraint_total_degree=1)
        assert hook_pair_nonlinear_blocks_match_under_dual_swap(6, 2, max_constraint_total_degree=1)
        assert hook_pair_survivor_coupled_blocks_match_under_dual_swap(
            6,
            2,
            max_constraint_total_degree=1,
            survivor_total_degree=1,
        )
        assert hook_pair_mixed_family_holds_via_duality(7, 1)
        assert all(
            verify_hook_pair_mixed_family_via_duality_catalog(
                max_n=7,
                max_constraint_total_degree=1,
            ).values()
        )
        assert hook_pair_nonlinear_family_holds_via_duality(7, 1)
        assert all(
            verify_hook_pair_nonlinear_family_via_duality_catalog(
                max_n=7,
                max_constraint_total_degree=1,
            ).values()
        )
        assert hook_pair_survivor_coupled_family_holds_via_duality(5, 1, 1)
        assert all(
            verify_hook_pair_survivor_coupled_family_via_duality_catalog(
                max_n=5,
                max_constraint_total_degree=1,
                survivor_total_degree=1,
            ).values()
        )
        assert hook_pair_survivor_coupled_family_holds_via_duality(6, 1, 3)
        assert all(
            verify_hook_pair_survivor_coupled_family_via_duality_catalog(
                max_n=6,
                max_constraint_total_degree=1,
                survivor_total_degree=3,
            ).values()
        )
        two_row_source_blocks, two_row_target_blocks = nonprincipal_two_row_mixed_constraint_ghost_blocks(
            6,
            2,
            max_constraint_total_degree=1,
        )
        two_row_source_nonlinear, two_row_target_nonlinear = (
            nonprincipal_two_row_nonlinear_mixed_constraint_ghost_blocks(
                6,
                2,
                max_constraint_total_degree=1,
            )
        )
        two_row_source_survivor, two_row_target_survivor = (
            nonprincipal_two_row_survivor_coupled_blocks(
                6,
                2,
                max_constraint_total_degree=1,
                survivor_total_degree=1,
            )
        )
        assert two_row_source_blocks
        assert two_row_target_blocks
        assert two_row_source_nonlinear
        assert two_row_target_nonlinear
        assert all(
            survivor_coupled_block_has_square_zero(block) and survivor_coupled_block_is_acyclic(block)
            for block in two_row_source_survivor + two_row_target_survivor
        )
        assert nonprincipal_two_row_mixed_blocks_match_under_dual_swap(
            6,
            2,
            max_constraint_total_degree=1,
        )
        assert nonprincipal_two_row_nonlinear_blocks_match_under_dual_swap(
            6,
            2,
            max_constraint_total_degree=1,
        )
        assert nonprincipal_two_row_survivor_coupled_blocks_match_under_dual_swap(
            6,
            2,
            max_constraint_total_degree=1,
            survivor_total_degree=1,
        )
        assert nonprincipal_two_row_mixed_family_holds_via_duality(9, 1)
        assert all(
            verify_nonprincipal_two_row_mixed_family_via_duality_catalog(
                max_n=9,
                max_constraint_total_degree=1,
            ).values()
        )
        assert nonprincipal_two_row_nonlinear_family_holds_via_duality(9, 1)
        assert all(
            verify_nonprincipal_two_row_nonlinear_family_via_duality_catalog(
                max_n=9,
                max_constraint_total_degree=1,
            ).values()
        )
        assert nonprincipal_two_row_survivor_coupled_family_holds_via_duality(8, 1, 1)
        assert all(
            verify_nonprincipal_two_row_survivor_coupled_family_via_duality_catalog(
                max_n=8,
                max_constraint_total_degree=1,
                survivor_total_degree=1,
            ).values()
        )
        general_seed = nonprincipal_general_seed((3, 2, 1))
        general_source_survivor, general_target_survivor = (
            nonprincipal_partition_pair_survivor_coupled_blocks(
                (3, 2, 1),
                max_constraint_total_degree=1,
                survivor_total_degree=1,
            )
        )
        assert general_seed.dual_partition == (3, 2, 1)
        assert all(
            survivor_coupled_block_has_square_zero(block) and survivor_coupled_block_is_acyclic(block)
            for block in general_source_survivor + general_target_survivor
        )
        assert nonprincipal_partition_pair_mixed_blocks_match_under_dual_swap(
            (3, 2, 1),
            max_constraint_total_degree=1,
        )
        assert nonprincipal_partition_pair_nonlinear_blocks_match_under_dual_swap(
            (3, 2, 1),
            max_constraint_total_degree=1,
        )
        assert nonprincipal_partition_pair_survivor_coupled_blocks_match_under_dual_swap(
            (3, 2, 1),
            max_constraint_total_degree=1,
            survivor_total_degree=1,
        )
        assert all(
            verify_nonprincipal_general_mixed_family_via_duality_catalog(
                max_n=9,
                max_constraint_total_degree=1,
            ).values()
        )
        assert general_nonprincipal_mixed_family_holds_via_duality(
            max_n=9,
            max_constraint_total_degree=1,
        )
        assert all(
            verify_nonprincipal_general_nonlinear_family_via_duality_catalog(
                max_n=9,
                max_constraint_total_degree=1,
            ).values()
        )
        assert general_nonprincipal_nonlinear_family_holds_via_duality(
            max_n=9,
            max_constraint_total_degree=1,
        )
        source_candidates, target_candidates = hook_pair_surviving_field_candidates(5, 2)
        source_reduced, target_reduced = hook_pair_reduced_brackets(5, 2)
        assert len(source_candidates) == centralizer_dimension_sl_n((3, 1, 1))
        assert len(target_candidates) == centralizer_dimension_sl_n((3, 1, 1))
        assert source_reduced
        assert target_reduced
        assert len(nonprincipal_hook_seed_catalog(5)) == 6
        assert nonprincipal_general_seed_catalog(6)
        assert nonprincipal_two_row_seed_catalog(7)
        assert all(verify_nonprincipal_hook_seed_catalog(7).values())
        assert all(verify_nonprincipal_general_seed_catalog(7).values())
        assert all(verify_nonprincipal_two_row_seed_catalog(7).values())
        assert all(verify_nonprincipal_ds_reduction_seed().values())

    @pytest.mark.parametrize("rank_n", GENERAL_SURVIVOR_COUPLED_SMOKE_RANKS)
    def test_nonprincipal_general_survivor_coupled_catalog_degree_one_by_rank(
        self,
        rank_n,
    ):
        _assert_general_survivor_coupled_family_slice(rank_n)

    @pytest.mark.parametrize(
        "partition",
        GENERAL_SURVIVOR_COUPLED_RANK_10_REPRESENTATIVES,
        ids=lambda partition: "_".join(str(part) for part in partition),
    )
    def test_nonprincipal_general_survivor_coupled_catalog_degree_one_rank_10_by_partition(
        self,
        partition,
    ):
        _assert_general_survivor_coupled_representative_slice(partition)

    @pytest.mark.parametrize(
        "partition",
        GENERAL_SURVIVOR_COUPLED_RANK_12_REPRESENTATIVES,
        ids=lambda partition: "_".join(str(part) for part in partition),
    )
    def test_nonprincipal_general_survivor_coupled_catalog_degree_one_rank_12_by_partition(
        self,
        partition,
    ):
        _assert_general_survivor_coupled_representative_slice(partition)

    def test_nonprincipal_corrected_semidirect_exports(self):
        from compute.lib import (
            partition_pair_corrected_survivor_action_terms,
            partition_pair_corrected_survivor_derivation_defects,
            nonprincipal_partition_pair_corrected_semidirect_survivor_blocks,
            nonprincipal_partition_pair_corrected_semidirect_blocks_match_under_dual_swap,
            general_nonprincipal_corrected_semidirect_family_holds_via_duality,
            verify_nonprincipal_general_corrected_semidirect_family_via_duality_catalog,
            nonprincipal_two_row_survivor_coupled_family_holds_via_duality,
            verify_nonprincipal_two_row_survivor_coupled_family_via_duality_catalog,
            nonprincipal_two_row_corrected_semidirect_survivor_blocks,
            nonprincipal_two_row_corrected_semidirect_blocks_match_under_dual_swap,
            nonprincipal_two_row_corrected_semidirect_family_holds_via_duality,
            verify_nonprincipal_two_row_corrected_semidirect_family_via_duality_catalog,
            semidirect_survivor_block_has_square_zero,
        )

        general_source_action, general_target_action = partition_pair_corrected_survivor_action_terms(
            (3, 2, 1)
        )
        general_source_defects, general_target_defects = (
            partition_pair_corrected_survivor_derivation_defects((3, 2, 1))
        )
        general_corrected_source, general_corrected_target = (
            nonprincipal_partition_pair_corrected_semidirect_survivor_blocks(
                (3, 2, 1),
                max_constraint_total_degree=0,
                survivor_total_degree=1,
                max_internal_ce_degree=1,
            )
        )
        two_row_corrected_source, two_row_corrected_target = (
            nonprincipal_two_row_corrected_semidirect_survivor_blocks(
                6,
                2,
                max_constraint_total_degree=0,
                survivor_total_degree=1,
                max_internal_ce_degree=1,
            )
        )

        assert general_source_action == ()
        assert general_target_action == ()
        assert general_source_defects == {}
        assert general_target_defects == {}
        assert all(
            semidirect_survivor_block_has_square_zero(block)
            for block in general_corrected_source
            + general_corrected_target
            + two_row_corrected_source
            + two_row_corrected_target
        )
        assert nonprincipal_partition_pair_corrected_semidirect_blocks_match_under_dual_swap(
            (3, 2, 1),
            max_constraint_total_degree=0,
            survivor_total_degree=1,
            max_internal_ce_degree=1,
        )
        assert nonprincipal_two_row_corrected_semidirect_blocks_match_under_dual_swap(
            6,
            2,
            max_constraint_total_degree=0,
            survivor_total_degree=1,
            max_internal_ce_degree=1,
        )
        assert nonprincipal_two_row_corrected_semidirect_family_holds_via_duality(8, 0, 1, 1)
        assert all(
            verify_nonprincipal_two_row_corrected_semidirect_family_via_duality_catalog(
                8,
                0,
                1,
                1,
            ).values()
        )
        assert nonprincipal_two_row_survivor_coupled_family_holds_via_duality(8, 1, 3)
        assert all(verify_nonprincipal_two_row_survivor_coupled_family_via_duality_catalog(8, 1, 3).values())
        assert nonprincipal_two_row_corrected_semidirect_family_holds_via_duality(8, 0, 3, 1)
        assert all(
            verify_nonprincipal_two_row_corrected_semidirect_family_via_duality_catalog(
                8,
                0,
                3,
                1,
            ).values()
        )
        _assert_general_survivor_coupled_family_slice(6, survivor_total_degree=3)
        assert general_nonprincipal_corrected_semidirect_family_holds_via_duality(8, 0, 1, 1)
        assert all(
            verify_nonprincipal_general_corrected_semidirect_family_via_duality_catalog(
                8,
                0,
                1,
                1,
            ).values()
        )
        assert general_nonprincipal_corrected_semidirect_family_holds_via_duality(5, 0, 3, 1)
        assert all(
            verify_nonprincipal_general_corrected_semidirect_family_via_duality_catalog(
                5,
                0,
                3,
                1,
            ).values()
        )
        assert nonprincipal_two_row_survivor_coupled_family_holds_via_duality(8, 1, 1)
        assert all(verify_nonprincipal_two_row_survivor_coupled_family_via_duality_catalog(8, 1, 1).values())

    def test_bv_and_ds_seed_exports(self):
        from compute.lib import (
            first_nonselfdual_type_a_hook_pair,
            verify_bv_duality_scaffold,
            sl3_subregular_bp_seed,
            verify_nonprincipal_ds_reduction_seed,
            bp_shift_to_target_sum,
            verify_nonprincipal_ds_normalization,
            sl3_subregular_ad_e_image_basis,
            sl3_subregular_ad_e_image_witnesses,
            sl3_subregular_basis_matrices,
            sl3_subregular_basis_profile,
            sl3_subregular_constraints,
            sl3_subregular_brst_blueprint,
            sl3_subregular_truncated_brst_complex,
            sl3_subregular_linear_constraint_blocks,
            sl3_subregular_mixed_constraint_ghost_blocks,
            sl3_subregular_nonlinear_mixed_constraint_ghost_blocks,
            sl3_subregular_survivor_action_terms,
            sl3_subregular_survivor_action_lift_witnesses,
            sl3_subregular_derivation_defect_witnesses,
            sl3_subregular_first_transfer_correction_witnesses,
            sl3_subregular_first_transfer_correction_terms,
            sl3_subregular_corrected_survivor_action_terms,
            sl3_subregular_corrected_survivor_derivation_defects,
            sl3_subregular_survivor_coupled_blocks,
            sl3_subregular_corrected_semidirect_survivor_blocks,
            sl3_subregular_project_basis_label_to_strong_candidates,
            sl3_subregular_projected_strong_brackets,
            sl3_subregular_strong_generator_candidates,
            ds_basis_expression_matrix,
            matrix_commutator,
            QuadraticGhostTermEntry,
            SurvivorActionTermEntry,
            quadratic_ghost_differential,
            ghost_brst_differential,
            build_ghost_brst_complex,
            build_mixed_constraint_ghost_brst_block,
            current_action_differential,
            survivor_action_differential,
            build_survivor_coupled_brst_block,
            build_internal_survivor_ce_block,
            build_semidirect_survivor_brst_block,
            combine_survivor_action_terms,
            relabel_quadratic_ghost_terms,
            relabel_current_action_terms,
            relabel_truncated_brst_complex,
            relabel_mixed_constraint_ghost_block,
            hook_pair_ds_seed_catalog,
            hook_pair_survivor_action_terms,
            hook_pair_first_transfer_correction_witnesses,
            hook_pair_first_transfer_correction_terms,
            hook_pair_corrected_survivor_action_terms,
            hook_pair_corrected_survivor_derivation_defects,
            hook_pair_survivor_coupled_blocks,
            hook_pair_corrected_semidirect_survivor_blocks,
            hook_pair_survivor_coupled_blocks_match_under_dual_swap,
            verify_hook_pair_first_transfer_correction_catalog,
            hook_pair_survivor_coupled_family_holds_via_duality,
            verify_hook_pair_survivor_coupled_family_via_duality_catalog,
            hook_pair_corrected_semidirect_family_holds_via_duality,
            verify_hook_pair_corrected_semidirect_family_via_duality_catalog,
            first_nonselfdual_hook_pair_ds_seed,
            verify_hook_pair_ds_seed_catalog,
            verify_hook_pair_seed_alignment,
            first_nonselfdual_hook_pair_basis_profiles,
            first_nonselfdual_hook_pair_brst_blueprints,
            first_nonselfdual_hook_pair_ghost_profiles,
            first_nonselfdual_hook_pair_constraint_characters,
            first_nonselfdual_hook_pair_constraints,
            first_nonselfdual_hook_pair_current_action_terms,
            first_nonselfdual_hook_pair_survivor_action_terms,
            first_nonselfdual_hook_pair_positive_nilpotent_brackets,
            first_nonselfdual_hook_pair_quadratic_ghost_term_support,
            first_nonselfdual_hook_pair_ghost_label_map,
            first_nonselfdual_hook_pair_ghost_side_map,
            first_nonselfdual_hook_pair_ghost_complexes_match_under_relabeling,
            first_nonselfdual_hook_pair_linear_constraint_blocks,
            first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks,
            first_nonselfdual_hook_pair_mixed_blocks_match_under_relabeling,
            first_nonselfdual_hook_pair_nonlinear_mixed_constraint_ghost_blocks,
            first_nonselfdual_hook_pair_nonlinear_blocks_match_under_relabeling,
            first_nonselfdual_hook_pair_survivor_coupled_blocks_match_under_relabeling,
            first_nonselfdual_hook_pair_survivor_coupled_blocks,
            first_nonselfdual_hook_pair_surviving_field_candidates,
            first_nonselfdual_hook_pair_reduced_brackets,
            complex_has_nilpotent_differential,
            chain_homology_dimensions,
            mixed_constraint_ghost_block_basis,
            mixed_constraint_ghost_brst_differential,
            mixed_constraint_ghost_block_homology_dimensions,
            mixed_constraint_ghost_block_has_square_zero,
            mixed_constraint_ghost_block_is_acyclic,
            survivor_coupled_block_basis,
            survivor_coupled_block_homology_dimensions,
            survivor_coupled_block_has_square_zero,
            survivor_coupled_block_is_acyclic,
            internal_survivor_ce_block_basis,
            internal_survivor_ce_h0_basis,
            internal_survivor_ce_block_homology_dimensions,
            internal_survivor_ce_block_has_square_zero,
            internal_survivor_ce_block_is_acyclic,
            internal_survivor_h0_monomial_labels,
            internal_survivor_linear_h0_labels,
            semidirect_survivor_block_has_square_zero,
            linear_constraint_block_has_contracting_homotopy,
            linear_constraint_block_is_positive_acyclic,
            first_nonselfdual_hook_pair_specialized_complexes,
            truncated_cohomology_dimensions,
            complex_is_acyclic,
            sl3_subregular_ds_seed,
            sl3_subregular_internal_survivor_ce_blocks,
            sl3_subregular_semidirect_survivor_blocks,
            sl3_subregular_survivor_derivation_defects,
            first_nonselfdual_hook_pair_internal_survivor_ce_blocks,
            first_nonselfdual_hook_pair_survivor_action_lift_witnesses,
            first_nonselfdual_hook_pair_derivation_defect_witnesses,
            first_nonselfdual_hook_pair_first_transfer_correction_witnesses,
            first_nonselfdual_hook_pair_first_transfer_correction_terms,
            first_nonselfdual_hook_pair_corrected_survivor_action_terms,
            first_nonselfdual_hook_pair_corrected_survivor_derivation_defects,
            first_nonselfdual_hook_pair_corrected_semidirect_survivor_blocks,
            first_nonselfdual_hook_pair_semidirect_survivor_blocks,
            first_nonselfdual_hook_pair_survivor_derivation_defects,
            verify_ds_reduction_seed,
        )
        n, r, pair = first_nonselfdual_type_a_hook_pair()
        seed = sl3_subregular_bp_seed()
        ad_e_basis = sl3_subregular_ad_e_image_basis()
        ad_e_witnesses = sl3_subregular_ad_e_image_witnesses()
        basis_matrices = sl3_subregular_basis_matrices()
        basis = sl3_subregular_basis_profile()
        constraints = sl3_subregular_constraints()
        blueprint = sl3_subregular_brst_blueprint()
        strong_candidates = sl3_subregular_strong_generator_candidates()
        subregular_complex = sl3_subregular_truncated_brst_complex()
        subregular_blocks = sl3_subregular_linear_constraint_blocks(2)
        subregular_mixed_blocks = sl3_subregular_mixed_constraint_ghost_blocks(2)
        subregular_nonlinear_mixed_blocks = sl3_subregular_nonlinear_mixed_constraint_ghost_blocks(2)
        subregular_survivor_action = sl3_subregular_survivor_action_terms()
        subregular_action_lifts = sl3_subregular_survivor_action_lift_witnesses()
        subregular_defect_witnesses = sl3_subregular_derivation_defect_witnesses()
        subregular_correction_witnesses = (
            sl3_subregular_first_transfer_correction_witnesses()
        )
        subregular_first_correction = sl3_subregular_first_transfer_correction_terms()
        subregular_corrected_action = sl3_subregular_corrected_survivor_action_terms()
        subregular_corrected_defects = sl3_subregular_corrected_survivor_derivation_defects()
        subregular_survivor_blocks = sl3_subregular_survivor_coupled_blocks(1, 1)
        subregular_internal_blocks = sl3_subregular_internal_survivor_ce_blocks(1)
        subregular_semidirect_blocks = sl3_subregular_semidirect_survivor_blocks(0, 1, 1)
        subregular_corrected_semidirect_blocks = sl3_subregular_corrected_semidirect_survivor_blocks(0, 1, 1)
        subregular_derivation_defects = sl3_subregular_survivor_derivation_defects()
        hook_catalog = hook_pair_ds_seed_catalog(5)
        generic_source_survivor_action, generic_target_survivor_action = (
            hook_pair_survivor_action_terms(6, 2)
        )
        generic_source_correction_witnesses, generic_target_correction_witnesses = (
            hook_pair_first_transfer_correction_witnesses(4, 1)
        )
        generic_source_survivor_blocks, generic_target_survivor_blocks = (
            hook_pair_survivor_coupled_blocks(
                6,
                2,
                max_constraint_total_degree=1,
                survivor_total_degree=1,
            )
        )
        hook_pair_seed = first_nonselfdual_hook_pair_ds_seed()
        hook_source_basis, hook_target_basis = first_nonselfdual_hook_pair_basis_profiles()
        hook_source_blueprint, hook_target_blueprint = first_nonselfdual_hook_pair_brst_blueprints()
        hook_source_profile, hook_target_profile = first_nonselfdual_hook_pair_ghost_profiles()
        hook_source_character, hook_target_character = first_nonselfdual_hook_pair_constraint_characters()
        hook_source_constraints, hook_target_constraints = first_nonselfdual_hook_pair_constraints()
        hook_source_positive_brackets, hook_target_positive_brackets = (
            first_nonselfdual_hook_pair_positive_nilpotent_brackets()
        )
        hook_source_action, hook_target_action = first_nonselfdual_hook_pair_current_action_terms()
        hook_source_survivor_action, hook_target_survivor_action = (
            first_nonselfdual_hook_pair_survivor_action_terms()
        )
        hook_source_quadratic, hook_target_quadratic = (
            first_nonselfdual_hook_pair_quadratic_ghost_term_support()
        )
        hook_label_map = first_nonselfdual_hook_pair_ghost_label_map()
        hook_side_map = first_nonselfdual_hook_pair_ghost_side_map()
        hook_source_candidates, hook_target_candidates = first_nonselfdual_hook_pair_surviving_field_candidates()
        hook_source_brackets, hook_target_brackets = first_nonselfdual_hook_pair_reduced_brackets()
        hook_source_blocks, hook_target_blocks = first_nonselfdual_hook_pair_linear_constraint_blocks(2)
        hook_source_mixed_blocks, hook_target_mixed_blocks = (
            first_nonselfdual_hook_pair_mixed_constraint_ghost_blocks(1)
        )
        hook_source_nonlinear_blocks, hook_target_nonlinear_blocks = (
            first_nonselfdual_hook_pair_nonlinear_mixed_constraint_ghost_blocks(1)
        )
        hook_source_survivor_blocks, hook_target_survivor_blocks = (
            first_nonselfdual_hook_pair_survivor_coupled_blocks(1, 1)
        )
        hook_source_internal_blocks, hook_target_internal_blocks = (
            first_nonselfdual_hook_pair_internal_survivor_ce_blocks(1)
        )
        hook_source_semidirect_blocks, hook_target_semidirect_blocks = (
            first_nonselfdual_hook_pair_semidirect_survivor_blocks(0, 1, 1)
        )
        hook_source_derivation_defects, hook_target_derivation_defects = (
            first_nonselfdual_hook_pair_survivor_derivation_defects()
        )
        hook_source_action_lifts, hook_target_action_lifts = (
            first_nonselfdual_hook_pair_survivor_action_lift_witnesses()
        )
        hook_source_defect_witnesses, hook_target_defect_witnesses = (
            first_nonselfdual_hook_pair_derivation_defect_witnesses()
        )
        hook_source_correction_witnesses, hook_target_correction_witnesses = (
            first_nonselfdual_hook_pair_first_transfer_correction_witnesses()
        )
        hook_source_first_correction, hook_target_first_correction = (
            first_nonselfdual_hook_pair_first_transfer_correction_terms()
        )
        hook_source_corrected_action, hook_target_corrected_action = (
            first_nonselfdual_hook_pair_corrected_survivor_action_terms()
        )
        hook_source_corrected_defects, hook_target_corrected_defects = (
            first_nonselfdual_hook_pair_corrected_survivor_derivation_defects()
        )
        hook_source_corrected_semidirect_blocks, hook_target_corrected_semidirect_blocks = (
            first_nonselfdual_hook_pair_corrected_semidirect_survivor_blocks(0, 1, 1)
        )
        ds_seed = sl3_subregular_ds_seed()
        assert n == 4 and r == 1
        assert pair.source_orbit == (3, 1) and pair.target_orbit == (2, 1, 1)
        assert seed.partition == (2, 1) and seed.dual_partition == (2, 1)
        assert len(basis) == 8
        assert len(ad_e_basis) == 4
        assert sorted(ad_e_witnesses) == ["E12", "E13", "F23", "H1"]
        assert len(constraints) == 2
        assert blueprint.positive_nilpotent_is_abelian
        assert len(strong_candidates) == 4
        assert matrix_commutator(
            basis_matrices["F12"],
            ds_basis_expression_matrix(strong_candidates[0].source_terms, basis_matrices),
        ) == zeros(3, 3)
        assert sl3_subregular_project_basis_label_to_strong_candidates("H2") == {"J": 1}
        assert sl3_subregular_projected_strong_brackets()[("G+", "G-")] == {"T": 1}
        assert subregular_complex.source_tag == "A2_subregular_seed"
        assert chain_homology_dimensions(subregular_blocks[0]) == {0: 1}
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in subregular_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in subregular_blocks[1:])
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in subregular_mixed_blocks)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in subregular_mixed_blocks)
        assert all(mixed_constraint_ghost_block_has_square_zero(block) for block in subregular_nonlinear_mixed_blocks)
        assert all(mixed_constraint_ghost_block_is_acyclic(block) for block in subregular_nonlinear_mixed_blocks)
        assert len(subregular_survivor_action) == 2
        assert all(survivor_coupled_block_has_square_zero(block) for block in subregular_survivor_blocks)
        assert all(survivor_coupled_block_is_acyclic(block) for block in subregular_survivor_blocks)
        assert all(internal_survivor_ce_block_has_square_zero(block) for block in subregular_internal_blocks)
        assert not all(internal_survivor_ce_block_is_acyclic(block) for block in subregular_internal_blocks)
        assert not any(semidirect_survivor_block_has_square_zero(block) for block in subregular_semidirect_blocks)
        assert any(
            item.c_ghost == "c_alpha1+alpha2"
            and item.source_survivor_label == "G-"
            and item.ad_e_witness_preimage == (("F12", Rational(1, 2)),)
            for item in subregular_action_lifts
        )
        assert any(
            item.c_ghost == "c_alpha1+alpha2"
            and item.left_survivor_label == "J"
            and item.right_survivor_label == "T"
            and item.projected_defect_terms == (("G+", Rational(3, 2)),)
            for item in subregular_defect_witnesses
        )
        assert len(subregular_correction_witnesses) == 2
        assert combine_survivor_action_terms(
            subregular_survivor_action,
            subregular_first_correction,
        ) == subregular_corrected_action
        assert subregular_corrected_action == ()
        assert subregular_corrected_defects == {}
        assert all(
            semidirect_survivor_block_has_square_zero(block)
            for block in subregular_corrected_semidirect_blocks
        )
        assert subregular_derivation_defects["c_alpha1+alpha2"][("G+", "G-")] == {"G+": Rational(1, 2)}
        assert hook_pair_seed.source_partition == (3, 1)
        assert hook_pair_seed.target_partition == (2, 1, 1)
        assert len(hook_source_profile) == 5
        assert len(hook_target_profile) == 5
        assert len(hook_source_basis) == 15
        assert len(hook_target_basis) == 15
        assert hook_source_blueprint.quadratic_ghost_term_present
        assert hook_target_blueprint.quadratic_ghost_term_present
        assert hook_source_character["E13"] == 0
        assert hook_source_character["E12"] == 1
        assert hook_target_character["E12"] == 0
        assert hook_target_character["E13"] == 1
        assert len(hook_source_constraints) == 5
        assert len(hook_target_constraints) == 5
        assert hook_source_positive_brackets == (("E12", "E23", "E13"), ("E14", "E43", "E13"))
        assert hook_target_positive_brackets == (("E13", "E32", "E12"), ("E14", "E42", "E12"))
        assert len(hook_source_action) == 4
        assert len(hook_target_action) == 4
        assert len(hook_source_survivor_action) == 6
        assert len(hook_target_survivor_action) == 14
        assert generic_source_survivor_action
        assert generic_target_survivor_action
        assert generic_source_correction_witnesses or generic_target_correction_witnesses
        assert len(hook_source_quadratic) == 2
        assert len(hook_target_quadratic) == 2
        assert len(hook_source_candidates) == 5
        assert len(hook_target_candidates) == 9
        assert len(hook_catalog) == 6
        assert complex_has_nilpotent_differential(subregular_complex)
        assert complex_has_nilpotent_differential(hook_pair_seed.source_complex)
        assert complex_has_nilpotent_differential(hook_pair_seed.target_complex)
        assert quadratic_ghost_differential(
            hook_pair_seed.source_complex.ghost_labels,
            hook_pair_seed.source_complex.quadratic_ghost_terms,
            1,
        ).shape == (10, 5)
        assert ghost_brst_differential(
            hook_pair_seed.source_complex.ghost_labels,
            hook_pair_seed.source_complex.chi_vector,
            hook_pair_seed.source_complex.quadratic_ghost_terms,
            1,
        ) == hook_pair_seed.source_complex.differentials[1]
        rebuilt_hook_source = build_ghost_brst_complex(
            hook_pair_seed.source_complex.ghost_labels,
            hook_pair_seed.source_complex.chi_vector,
            hook_pair_seed.source_complex.quadratic_ghost_terms,
            "rebuilt_hook_source",
        )
        rebuilt_hook_mixed = build_mixed_constraint_ghost_brst_block(
            shifted_current_labels=tuple(
                f"u_source_{item.root_label}" for item in hook_source_constraints
            ),
            c_ghost_labels=tuple(item.c_ghost for item in hook_source_constraints),
            b_ghost_labels=tuple(item.b_ghost for item in hook_source_constraints),
            chi_vector=tuple(item.character_value for item in hook_source_constraints),
            quadratic_terms=hook_source_quadratic,
            constraint_total_degree=1,
            source_tag="rebuilt_hook_mixed",
        )
        rebuilt_hook_nonlinear = build_mixed_constraint_ghost_brst_block(
            shifted_current_labels=tuple(
                f"u_source_{item.root_label}" for item in hook_source_constraints
            ),
            c_ghost_labels=tuple(item.c_ghost for item in hook_source_constraints),
            b_ghost_labels=tuple(item.b_ghost for item in hook_source_constraints),
            chi_vector=tuple(item.character_value for item in hook_source_constraints),
            quadratic_terms=hook_source_quadratic,
            constraint_total_degree=1,
            source_tag="rebuilt_hook_nonlinear",
            current_action_terms=hook_source_action,
        )
        rebuilt_hook_survivor = build_survivor_coupled_brst_block(
            shifted_current_labels=tuple(
                f"u_source_{item.root_label}" for item in hook_source_constraints
            ),
            survivor_labels=tuple(item.label for item in hook_source_candidates),
            c_ghost_labels=tuple(item.c_ghost for item in hook_source_constraints),
            b_ghost_labels=tuple(item.b_ghost for item in hook_source_constraints),
            chi_vector=tuple(item.character_value for item in hook_source_constraints),
            quadratic_terms=hook_source_quadratic,
            current_action_terms=hook_source_action,
            survivor_action_terms=hook_source_survivor_action,
            constraint_total_degree=1,
            survivor_total_degree=1,
            source_tag="rebuilt_hook_survivor",
        )
        rebuilt_subregular_internal = build_internal_survivor_ce_block(
            survivor_labels=tuple(item.label for item in strong_candidates),
            c_ghost_labels=tuple(f"c_survivor_{item.label}" for item in strong_candidates),
            b_ghost_labels=tuple(f"b_survivor_{item.label}" for item in strong_candidates),
            quadratic_terms=(
                QuadraticGhostTermEntry("c_survivor_J", "c_survivor_G+", "b_survivor_G+", Rational(3, 2)),
                QuadraticGhostTermEntry("c_survivor_J", "c_survivor_G-", "b_survivor_G-", Rational(-3, 2)),
                QuadraticGhostTermEntry("c_survivor_G+", "c_survivor_G-", "b_survivor_T", 1),
            ),
            survivor_action_terms=(
                SurvivorActionTermEntry("c_survivor_J", "G+", "G+", Rational(3, 2)),
                SurvivorActionTermEntry("c_survivor_J", "G-", "G-", Rational(-3, 2)),
                SurvivorActionTermEntry("c_survivor_G+", "J", "G+", Rational(-3, 2)),
                SurvivorActionTermEntry("c_survivor_G+", "G-", "T", 1),
                SurvivorActionTermEntry("c_survivor_G-", "J", "G-", Rational(3, 2)),
                SurvivorActionTermEntry("c_survivor_G-", "G+", "T", -1),
            ),
            survivor_polynomial_degree=1,
            source_tag="rebuilt_subregular_internal",
        )
        rebuilt_subregular_semidirect = build_semidirect_survivor_brst_block(
            shifted_current_labels=tuple(f"u_{item.root_label}" for item in constraints),
            survivor_labels=tuple(item.label for item in strong_candidates),
            c_ghost_labels=tuple(item.c_ghost for item in constraints),
            b_ghost_labels=tuple(item.b_ghost for item in constraints),
            internal_c_ghost_labels=tuple(f"c_survivor_{item.label}" for item in strong_candidates),
            internal_b_ghost_labels=tuple(f"b_survivor_{item.label}" for item in strong_candidates),
            chi_vector=tuple(item.character_value for item in constraints),
            quadratic_terms=(),
            current_action_terms=(),
            survivor_action_terms=subregular_survivor_action,
            internal_quadratic_terms=(
                QuadraticGhostTermEntry("c_survivor_J", "c_survivor_G+", "b_survivor_G+", Rational(3, 2)),
                QuadraticGhostTermEntry("c_survivor_J", "c_survivor_G-", "b_survivor_G-", Rational(-3, 2)),
                QuadraticGhostTermEntry("c_survivor_G+", "c_survivor_G-", "b_survivor_T", 1),
            ),
            internal_survivor_action_terms=(
                SurvivorActionTermEntry("c_survivor_J", "G+", "G+", Rational(3, 2)),
                SurvivorActionTermEntry("c_survivor_J", "G-", "G-", Rational(-3, 2)),
                SurvivorActionTermEntry("c_survivor_G+", "J", "G+", Rational(-3, 2)),
                SurvivorActionTermEntry("c_survivor_G+", "G-", "T", 1),
                SurvivorActionTermEntry("c_survivor_G-", "J", "G-", Rational(3, 2)),
                SurvivorActionTermEntry("c_survivor_G-", "G+", "T", -1),
            ),
            constraint_total_degree=0,
            survivor_total_degree=1,
            max_internal_ce_degree=1,
            source_tag="rebuilt_subregular_semidirect",
        )
        relabeled_hook_source = relabel_truncated_brst_complex(
            hook_pair_seed.source_complex,
            hook_label_map,
            side_map=hook_side_map,
            source_tag=hook_pair_seed.target_complex.source_tag,
        )
        relabeled_hook_mixed = relabel_mixed_constraint_ghost_block(
            hook_source_mixed_blocks[1],
            hook_label_map,
            side_map=hook_side_map,
            source_tag=hook_target_mixed_blocks[1].source_tag,
        )
        relabeled_hook_nonlinear = relabel_mixed_constraint_ghost_block(
            hook_source_nonlinear_blocks[1],
            hook_label_map,
            side_map=hook_side_map,
            source_tag=hook_target_nonlinear_blocks[1].source_tag,
        )
        assert complex_has_nilpotent_differential(rebuilt_hook_source)
        assert relabel_quadratic_ghost_terms(
            hook_pair_seed.source_complex.quadratic_ghost_terms,
            hook_label_map,
            side_map=hook_side_map,
        ) == hook_pair_seed.target_complex.quadratic_ghost_terms
        assert relabeled_hook_source.differentials == hook_pair_seed.target_complex.differentials
        assert first_nonselfdual_hook_pair_ghost_complexes_match_under_relabeling()
        assert len(mixed_constraint_ghost_block_basis(5, 1, 0)) == 30
        assert mixed_constraint_ghost_brst_differential(
            rebuilt_hook_mixed.shifted_current_labels,
            rebuilt_hook_mixed.c_ghost_labels,
            rebuilt_hook_mixed.b_ghost_labels,
            tuple(item.character_value for item in hook_source_constraints),
            hook_source_quadratic,
            1,
            0,
        ) == rebuilt_hook_mixed.differentials[0]
        assert current_action_differential(
            rebuilt_hook_nonlinear.shifted_current_labels,
            rebuilt_hook_nonlinear.c_ghost_labels,
            rebuilt_hook_nonlinear.b_ghost_labels,
            hook_source_action,
            1,
            0,
        ).rank() > 0
        assert survivor_action_differential(
            rebuilt_hook_survivor.survivor_labels,
            rebuilt_hook_survivor.c_ghost_labels,
            rebuilt_hook_survivor.b_ghost_labels,
            hook_source_survivor_action,
            1,
            1,
            0,
        ).rank() > 0
        assert mixed_constraint_ghost_block_has_square_zero(rebuilt_hook_mixed)
        assert mixed_constraint_ghost_block_is_acyclic(rebuilt_hook_mixed)
        assert mixed_constraint_ghost_block_has_square_zero(rebuilt_hook_nonlinear)
        assert mixed_constraint_ghost_block_is_acyclic(rebuilt_hook_nonlinear)
        assert survivor_coupled_block_has_square_zero(rebuilt_hook_survivor)
        assert survivor_coupled_block_is_acyclic(rebuilt_hook_survivor)
        assert mixed_constraint_ghost_block_homology_dimensions(hook_source_mixed_blocks[0]) == {
            degree: 0 for degree in range(6)
        }
        assert len(survivor_coupled_block_basis(5, 5, 1, 1, 0)) == 150
        assert len(internal_survivor_ce_block_basis(4, 1, 1)) == 16
        assert internal_survivor_ce_h0_basis(rebuilt_subregular_internal) == (
            (((0, 0, 0, 1), 1),),
        )
        assert internal_survivor_h0_monomial_labels(rebuilt_subregular_internal) == (
            ((((("T", 1),), 1),)),
        )
        assert internal_survivor_linear_h0_labels(rebuilt_subregular_internal) == ((("T", 1),),)
        assert internal_survivor_ce_block_homology_dimensions(rebuilt_subregular_internal) == {
            0: 1,
            1: 2,
            2: 2,
            3: 2,
            4: 1,
        }
        assert not semidirect_survivor_block_has_square_zero(rebuilt_subregular_semidirect)
        assert survivor_coupled_block_homology_dimensions(hook_source_survivor_blocks[1]) == {
            -1: 0,
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
        }
        assert internal_survivor_ce_block_homology_dimensions(hook_source_internal_blocks[1]) == {
            0: 2,
            1: 5,
            2: 5,
            3: 5,
            4: 5,
            5: 2,
        }
        assert internal_survivor_ce_block_homology_dimensions(hook_target_internal_blocks[1]) == {
            0: 1,
            1: 2,
            2: 2,
            3: 2,
            4: 2,
            5: 3,
            6: 2,
            7: 0,
            8: 1,
            9: 1,
        }
        assert not any(semidirect_survivor_block_has_square_zero(block) for block in hook_source_semidirect_blocks)
        assert not any(semidirect_survivor_block_has_square_zero(block) for block in hook_target_semidirect_blocks)
        assert hook_source_derivation_defects["c_source_E12"][("source_gm2_2", "source_gm2_3")] == {
            "source_gm2_1": Rational(-1, 2)
        }
        assert hook_target_derivation_defects["c_target_E13"][("target_g0_1", "target_gm1_3")] == {
            "target_g0_1": -1
        }
        assert any(
            item.c_ghost == "c_source_E12"
            and item.source_survivor_label == "source_gm4_1"
            and item.ad_e_witness_preimage == (("E31", Rational(1, 2)),)
            for item in hook_source_action_lifts
        )
        assert any(
            item.c_ghost == "c_target_E13"
            and item.source_survivor_label == "target_gm1_3"
            and item.ad_e_witness_preimage == (("E21", Rational(1, 2)),)
            for item in hook_target_action_lifts
        )
        assert all(
            dict(item.projected_defect_terms)
            == hook_source_derivation_defects[item.c_ghost][
                (item.left_survivor_label, item.right_survivor_label)
            ]
            for item in hook_source_defect_witnesses
        )
        assert all(
            dict(item.projected_defect_terms)
            == hook_target_derivation_defects[item.c_ghost][
                (item.left_survivor_label, item.right_survivor_label)
            ]
            for item in hook_target_defect_witnesses
        )
        assert hook_source_correction_witnesses
        assert hook_target_correction_witnesses
        assert len(hook_source_first_correction) == len(hook_source_survivor_action)
        assert len(hook_target_first_correction) == len(hook_target_survivor_action)
        assert hook_source_corrected_action == ()
        assert hook_target_corrected_action == ()
        assert hook_source_corrected_defects == {}
        assert hook_target_corrected_defects == {}
        assert all(
            semidirect_survivor_block_has_square_zero(block)
            for block in hook_source_corrected_semidirect_blocks
            + hook_target_corrected_semidirect_blocks
        )
        assert mixed_constraint_ghost_block_has_square_zero(hook_target_mixed_blocks[1])
        assert mixed_constraint_ghost_block_has_square_zero(hook_target_nonlinear_blocks[1])
        assert survivor_coupled_block_has_square_zero(hook_target_survivor_blocks[1])
        assert all(
            survivor_coupled_block_has_square_zero(block) and survivor_coupled_block_is_acyclic(block)
            for block in generic_source_survivor_blocks + generic_target_survivor_blocks
        )
        assert internal_survivor_ce_block_has_square_zero(hook_target_internal_blocks[1])
        assert relabeled_hook_mixed.differentials == hook_target_mixed_blocks[1].differentials
        assert relabel_current_action_terms(
            hook_source_nonlinear_blocks[1].current_action_terms,
            hook_label_map,
            side_map=hook_side_map,
        ) == hook_target_nonlinear_blocks[1].current_action_terms
        assert relabeled_hook_nonlinear.differentials == hook_target_nonlinear_blocks[1].differentials
        assert first_nonselfdual_hook_pair_mixed_blocks_match_under_relabeling(1)
        assert first_nonselfdual_hook_pair_nonlinear_blocks_match_under_relabeling(1)
        assert first_nonselfdual_hook_pair_survivor_coupled_blocks_match_under_relabeling(1, 1)
        assert hook_pair_survivor_coupled_blocks_match_under_dual_swap(
            6,
            2,
            max_constraint_total_degree=1,
            survivor_total_degree=1,
        )
        assert hook_pair_survivor_coupled_family_holds_via_duality(5, 1, 1)
        assert all(
            verify_hook_pair_survivor_coupled_family_via_duality_catalog(
                max_n=5,
                max_constraint_total_degree=1,
                survivor_total_degree=1,
            ).values()
        )
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in hook_source_blocks[1:])
        assert all(linear_constraint_block_has_contracting_homotopy(block) for block in hook_target_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in hook_source_blocks[1:])
        assert all(linear_constraint_block_is_positive_acyclic(block) for block in hook_target_blocks[1:])
        assert len(hook_source_blocks[0].ghost_labels) == 5
        assert len(hook_target_blocks[0].ghost_labels) == 5
        assert hook_source_brackets[("source_gm2_2", "source_gm2_3")] == {"source_gm4_1": 1}
        assert hook_target_brackets[("target_gm1_1", "target_gm1_3")] == {"target_gm2_1": 1}
        assert truncated_cohomology_dimensions(subregular_complex) == {0: 0, 1: 0, 2: 0}
        assert complex_is_acyclic(subregular_complex)
        source_spec, target_spec = first_nonselfdual_hook_pair_specialized_complexes(
            source_chi=(0, 1, 0, 0, 0),
            target_chi=(0, 1, 0, 0, 0),
        )
        assert complex_is_acyclic(source_spec)
        assert complex_is_acyclic(target_spec)
        assert ds_seed.partition == (2, 1)
        assert bp_shift_to_target_sum(22) == -27
        assert all(verify_bv_duality_scaffold(7).values())
        assert all(verify_nonprincipal_ds_reduction_seed().values())
        assert all(verify_nonprincipal_ds_normalization().values())
        assert all(verify_hook_pair_ds_seed_catalog(7).values())
        assert all(verify_hook_pair_seed_alignment(7).values())
        assert all(verify_hook_pair_first_transfer_correction_catalog(5).values())
        assert hook_pair_corrected_semidirect_family_holds_via_duality(5, 0, 1, 1)
        assert all(
            verify_hook_pair_corrected_semidirect_family_via_duality_catalog(
                5,
                0,
                1,
                1,
            ).values()
        )
        assert hook_pair_corrected_semidirect_family_holds_via_duality(6, 0, 3, 1)
        assert all(
            verify_hook_pair_corrected_semidirect_family_via_duality_catalog(
                6,
                0,
                3,
                1,
            ).values()
        )
        assert all(verify_ds_reduction_seed().values())
