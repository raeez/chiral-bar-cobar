"""Tests for the standard W_infinity dual-candidate package."""

from sympy import Rational, Symbol, simplify

from compute.lib.w_infinity_dual_candidate import (
    completed_bar_candidate_descriptor,
    stage3_dual_constraint_report,
    stage4_higher_spin_constraint_map,
    stage4_virasoro_constraint_map,
    stage4_dual_constraint_report,
    stage4_residue_symbol_map,
    stage4_dual_defect_map,
    stage4_dual_goal_report,
    stage4_primitive_square_class_report,
    stage4_pairing_reduction_report,
    stage4_primitive_transport_report,
    stage4_borcherds_transport_report,
    stage4_two_primitive_square_closure_report,
    stage4_local_attack_order_report,
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
    stage4_target_packet_at_level,
    evaluate_stage4_dual_defects_at_level,
    stage4_defect_vanishing_report,
    stage5_dual_frontier_report,
    standard_winfinity_dual_candidate_report,
    verify_standard_winfinity_dual_candidate,
)


class TestCompletedBarCandidateDescriptor:
    def test_descriptor_shape(self):
        descriptor = completed_bar_candidate_descriptor()
        assert descriptor["kind"] == "inverse_limit_bar"
        assert descriptor["formula"] == "varprojlim_N barB(W_N)"
        assert len(descriptor["construction_steps"]) == 3


class TestStage3DualConstraints:
    def test_stage3_packet_is_fully_resolved(self):
        report = stage3_dual_constraint_report()
        assert report["stage"] == 3
        assert len(report["seed_packet"]) == 15
        assert len(report["nonzero_channels"]) == 3
        assert len(report["vanishing_channels"]) == 12
        assert report["coefficients"][(2, 2, 2, 2)] == 2
        assert report["coefficients"][(2, 3, 3, 2)] == 3
        assert report["coefficients"][(3, 3, 2, 4)] == 2


class TestStage4DualConstraints:
    def test_higher_spin_constraint_map(self):
        c = Symbol("c")
        constraints = stage4_higher_spin_constraint_map(c)
        assert set(constraints) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
            (3, 4, 3, 4),
            (3, 4, 4, 3),
        }
        assert constraints[(3, 4, 3, 4)]["sign_ratio_to_c334"] == Rational(-3, 4)
        assert simplify(
            constraints[(3, 4, 3, 4)]["expression"]
            / constraints[(3, 3, 4, 2)]["expression"]
        ) == Rational(9, 16)
        assert simplify(
            constraints[(3, 4, 4, 3)]["expression"]
            / constraints[(3, 3, 4, 2)]["expression"]
        ) == Rational(5, 7)

    def test_virasoro_constraints(self):
        constraints = stage4_virasoro_constraint_map()
        assert constraints[(4, 4, 2, 6)]["expression"] == 2
        assert constraints[(3, 4, 2, 5)]["expression"] == 0

    def test_full_stage4_report(self):
        report = stage4_dual_constraint_report()
        assert report["stage"] == 4
        assert len(report["exact_identity_packet"]) == 6
        assert set(report["constraints"]) == set(report["exact_identity_packet"])
        assert set(report["higher_spin_constraints"]) == set(report["higher_spin_channels"])
        assert set(report["virasoro_constraints"]) == set(report["virasoro_target_channels"])

    def test_stage4_residue_symbols(self):
        symbols = stage4_residue_symbol_map()
        assert symbols[(3, 3, 4, 2)]["kind"] == "residue_square_variable"
        assert symbols[(4, 4, 2, 6)]["kind"] == "residue_value_variable"

    def test_stage4_defect_map(self):
        defects = stage4_dual_defect_map()
        assert set(defects) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
            (3, 4, 3, 4),
            (3, 4, 4, 3),
            (4, 4, 2, 6),
            (3, 4, 2, 5),
        }
        assert defects[(4, 4, 2, 6)]["target_expression"] == 2
        assert defects[(3, 4, 2, 5)]["target_expression"] == 0

    def test_stage4_goal_report(self):
        report = stage4_dual_goal_report()
        assert report["goal"] == "vanish all six stage-4 defects"
        assert set(report["defects"]) == set(report["exact_identity_packet"])

    def test_stage4_primitive_square_class_report(self):
        report = stage4_primitive_square_class_report()
        assert report["primitive_count"] == 2
        assert report["forced_count"] == 2
        assert set(report["primitive_square_channels"]) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
        }
        assert report["forced_mixed_square_channels"][(3, 4, 3, 4)]["ratio_to_primitive"] == Rational(9, 16)
        assert report["forced_mixed_square_channels"][(3, 4, 4, 3)]["ratio_to_primitive"] == Rational(5, 7)

    def test_stage4_pairing_reduction_report(self):
        report = stage4_pairing_reduction_report()
        assert report["forced_channel"] == (3, 4, 3, 4)
        assert report["forced_by"] == (3, 3, 4, 2)
        assert report["sign_ratio"] == Rational(-3, 4)
        assert report["square_ratio"] == Rational(9, 16)
        assert len(report["independent_higher_spin_channels"]) == 3

    def test_stage4_primitive_transport_report(self):
        report = stage4_primitive_transport_report()
        assert set(report["independent_square_identity_channels"]) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
            (3, 4, 4, 3),
        }
        assert set(report["primitive_self_square_channels"]) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
        }
        assert report["transport_square_channel"]["ratio_to_c334"] == Rational(5, 7)
        assert report["automatic_square_channel"]["residue_square_ratio"] == Rational(9, 16)
        targets = report["square_identity_targets"]
        assert simplify(targets[(3, 4, 4, 3)] / targets[(3, 3, 4, 2)]) == Rational(5, 7)
        residue = stage4_residue_symbol_map()
        expected_gap = residue[(3, 4, 4, 3)]["expression"] - Rational(5, 7) * residue[(3, 3, 4, 2)]["expression"]
        assert simplify(report["next_transport_gap"]["relation_expression"] - expected_gap) == 0

    def test_stage4_borcherds_transport_report(self):
        report = stage4_borcherds_transport_report()
        assert report["assumption"] == "stage-4 Ward-normalized visible invariant pairing"
        assert report["relation_channel"] == (3, 4, 4, 3)
        assert report["forced_by_residue_channel"] == (3, 3, 4, 2)
        assert report["target_square_ratio"] == Rational(5, 7)
        assert set(report["equivalent_closure_channels"]) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
        }
        residue = stage4_residue_symbol_map()
        expected_gap = (
            residue[(3, 4, 4, 3)]["expression"]
            - Rational(5, 7) * residue[(3, 3, 4, 2)]["expression"]
        )
        assert simplify(report["relation_expression"] - expected_gap) == 0

    def test_stage4_two_primitive_square_closure_report(self):
        report = stage4_two_primitive_square_closure_report()
        assert set(report["independent_square_identity_channels"]) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
        }
        assert report["equivalent_transport_relation_channel"] == (3, 4, 4, 3)
        assert report["forced_transport_channel"]["square_ratio"] == Rational(5, 7)
        assert report["automatic_square_channel"]["square_ratio"] == Rational(9, 16)
        targets = report["primitive_square_targets"]
        assert set(targets) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
        }

    def test_stage4_local_attack_order_report(self):
        report = stage4_local_attack_order_report()
        assert report["stage"] == 4
        assert report["step_1"]["kind"] == "virasoro_target_normalization"
        assert report["step_1"]["report"]["channel"] == (4, 4, 2, 6)
        assert report["step_2"]["kind"] == "higher_spin_transport"
        assert report["step_2"]["report"]["relation_channel"] == (3, 4, 4, 3)
        assert report["step_2"]["report"]["target_square_ratio"] == Rational(5, 7)

    def test_stage4_target_packet_at_level(self):
        packet = stage4_target_packet_at_level(1)
        assert set(packet) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
            (3, 4, 3, 4),
            (3, 4, 4, 3),
            (4, 4, 2, 6),
            (3, 4, 2, 5),
        }
        assert packet[(4, 4, 2, 6)] == 2
        assert packet[(3, 4, 2, 5)] == 0

    def test_symbolic_stage4_defects_at_level(self):
        defects = evaluate_stage4_dual_defects_at_level(1)
        assert str(defects[(3, 3, 4, 2)]).startswith("R_334_sq - ")
        assert str(defects[(4, 4, 2, 6)]) == "R_442 - 2"

    def test_target_packet_kills_all_stage4_defects(self):
        packet = stage4_target_packet_at_level(1)
        report = stage4_defect_vanishing_report(1, packet)
        assert report["all_vanish"] is True
        assert all(report["channel_vanishing"].values())


class TestStage5Frontier:
    def test_stage5_attack_order(self):
        report = stage5_dual_frontier_report()
        assert report["stage"] == 5
        assert report["prerequisite_stage"] == 4
        assert report["prerequisite_goal"] == "vanish all six stage-4 defects"
        assert set(report["prerequisite_exact_packet"]) == {
            (3, 3, 4, 2),
            (4, 4, 4, 4),
            (3, 4, 3, 4),
            (3, 4, 4, 3),
            (4, 4, 2, 6),
            (3, 4, 2, 5),
        }
        assert report["reduced_packet_size"] == 11
        assert report["transport_attack_order"] == (5, 4, 3)
        assert report["higher_spin_count"] == 8
        assert len(report["higher_spin_channels"]) == 8
        assert report["virasoro_target_count"] == 3
        assert set(report["virasoro_target_channels"]) == {
            (3, 5, 2, 6),
            (4, 5, 2, 7),
            (5, 5, 2, 8),
        }
        assert set(report["entry_singletons"]) == {(3, 4), (5, 5)}

    def test_stage5_local_attack_order_report(self):
        report = stage5_local_attack_order_report()
        assert report["stage"] == 5
        assert report["step_1"]["kind"] == "entry_packet"
        assert report["step_1"]["singleton_order"] == ((3, 4, 5, 2), (5, 5, 4, 6))
        assert report["step_2"]["kind"] == "target5_corridor"
        assert report["step_2"]["tail_singleton"] == (3, 4, 5, 2)
        assert report["step_2"]["residual_singleton_order"] == ((3, 5, 5, 3), (4, 5, 5, 4))
        assert report["step_3"]["target_order"] == (5, 4, 3)
        assert report["visible_pairing_refinement"]["target5_corridor_no_new_independent_data"] is True
        assert report["visible_pairing_refinement"]["independent_entry_channel"] == (5, 5, 4, 6)
        assert report["visible_pairing_refinement"]["effective_transport_attack_order"] == (4, 3)
        corridor = report["visible_pairing_refinement"]["dependent_target5_corridor"]
        assert corridor["tail_channel"] == (3, 4, 5, 2)
        assert corridor["determined_by_target4_channel"]["ratio"] == Rational(-5, 4)
        assert corridor["determined_by_target3_channel"]["ratio"] == Rational(5, 3)
        assert set(corridor["vanishing_transport_channels"]) == {
            (3, 5, 5, 3),
            (4, 5, 5, 4),
        }

    def test_stage5_effective_independent_frontier_report(self):
        report = stage5_effective_independent_frontier_report()
        assert report["stage"] == 5
        assert report["effective_independent_count"] == 1
        assert report["parameter"]["channel"] == (3, 5, 4, 4)
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert report["independent_entry_channel"] == (5, 5, 4, 6)
        assert report["independent_order"] == ((5, 5, 4, 6), "target4_ladder", "target3_ladder")
        assert report["effective_transport_attack_order"] == (4, 3)
        assert report["eliminated_target5_corridor"] == ((3, 4, 5, 2), (3, 5, 5, 3), (4, 5, 5, 4))
        assert set(report["vanishing_channels"]) == {
            (3, 5, 5, 3),
            (4, 5, 5, 4),
            (5, 5, 4, 6),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
        }
        determined = report["determined_nonzero_channels"]
        assert determined[(3, 4, 5, 2)]["forced_by"] == (3, 5, 4, 4)
        assert determined[(3, 4, 5, 2)]["ratio"] == Rational(-5, 4)
        assert determined[(4, 5, 3, 6)]["forced_by"] == (3, 5, 4, 4)
        assert determined[(4, 5, 3, 6)]["ratio"] == Rational(-3, 4)
        assert report["channel_normal_form"][(3, 5, 4, 4)]["expression"] == Symbol("A_5")

    def test_stage5_visible_pairing_normal_form_report(self):
        report = stage5_visible_pairing_normal_form_report()
        assert report["stage"] == 5
        assert report["parameter"]["name"] == "A_5"
        assert report["parameter"]["channel"] == (3, 5, 4, 4)
        normal_form = report["channel_normal_form"]
        assert set(normal_form) == {
            (3, 4, 5, 2),
            (3, 5, 5, 3),
            (4, 5, 5, 4),
            (5, 5, 4, 6),
            (3, 5, 4, 4),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
            (4, 5, 3, 6),
        }
        assert normal_form[(3, 5, 4, 4)]["kind"] == "parameter"
        assert normal_form[(3, 5, 4, 4)]["expression"] == Symbol("A_5")
        assert normal_form[(3, 4, 5, 2)]["ratio_to_A5"] == Rational(-5, 4)
        assert normal_form[(3, 4, 5, 2)]["expression"] == Rational(-5, 4) * Symbol("A_5")
        assert normal_form[(4, 5, 3, 6)]["ratio_to_A5"] == Rational(-3, 4)
        assert normal_form[(4, 5, 3, 6)]["expression"] == Rational(-3, 4) * Symbol("A_5")
        assert normal_form[(5, 5, 4, 6)]["expression"] == 0
        assert normal_form[(4, 5, 4, 5)]["expression"] == 0
        assert normal_form[(3, 5, 3, 5)]["expression"] == 0

    def test_stage5_principal_one_coefficient_normal_form_report(self):
        report = stage5_principal_one_coefficient_normal_form_report()
        assert report["stage"] == 5
        assert report["parameter"]["name"] == "A_5_DS"
        assert report["parameter"]["channel"] == (3, 5, 4, 4)
        normal_form = report["channel_normal_form"]
        assert normal_form[(3, 5, 4, 4)]["kind"] == "parameter"
        assert normal_form[(3, 5, 4, 4)]["expression"] == Symbol("A_5_DS")
        assert normal_form[(3, 4, 5, 2)]["ratio_to_A5_DS"] == Rational(-5, 4)
        assert normal_form[(4, 5, 3, 6)]["ratio_to_A5_DS"] == Rational(-3, 4)
        assert normal_form[(3, 5, 5, 3)]["expression"] == 0
        assert normal_form[(5, 5, 4, 6)]["expression"] == 0

    def test_stage5_principal_target5_no_new_independent_data_report(self):
        report = stage5_principal_target5_no_new_independent_data_report()
        assert report["stage"] == 5
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert report["corridor_channels"] == ((3, 4, 5, 2), (3, 5, 5, 3), (4, 5, 5, 4))
        assert report["neighboring_target3_channel"] == (4, 5, 3, 6)
        assert report["tail_ratio_to_representative"] == Rational(-5, 4)
        assert report["tail_ratio_to_target3"] == Rational(5, 3)

    def test_stage5_principal_residual_front_one_coefficient_report(self):
        report = stage5_principal_residual_front_one_coefficient_report()
        assert report["stage"] == 5
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert set(report["residual_front_channels"]) == {
            (5, 5, 4, 6),
            (3, 5, 4, 4),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
            (4, 5, 3, 6),
        }
        assert set(report["vanishing_channels"]) == {
            (5, 5, 4, 6),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
        }
        assert report["determined_nonzero_channel"]["channel"] == (4, 5, 3, 6)
        assert report["determined_nonzero_channel"]["ratio_to_representative"] == Rational(-3, 4)

    def test_stage5_principal_one_coefficient_factorization_report(self):
        report = stage5_principal_one_coefficient_factorization_report()
        assert report["stage"] == 5
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert report["factorization_inputs"] == (
            "principal_target5_no_new_independent_data",
            "principal_residual_front_one_coefficient",
        )
        assert report["principal_target5_corridor"]["representative_channel"] == (3, 5, 4, 4)
        assert report["principal_residual_front"]["representative_channel"] == (3, 5, 4, 4)

    def test_stage5_one_coefficient_reduction_report(self):
        report = stage5_one_coefficient_reduction_report()
        assert report["stage"] == 5
        assert set(report["higher_spin_packet"]) == {
            (3, 4, 5, 2),
            (3, 5, 5, 3),
            (4, 5, 5, 4),
            (5, 5, 4, 6),
            (3, 5, 4, 4),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
            (4, 5, 3, 6),
        }
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert report["residue_parameter"]["channel"] == (3, 5, 4, 4)
        assert report["principal_parameter"]["channel"] == (3, 5, 4, 4)
        assert report["reduction_goal"]["channel"] == (3, 5, 4, 4)
        ratios = report["shared_channel_ratios"]
        assert ratios[(3, 4, 5, 2)] == {
            "residue_ratio": Rational(-5, 4),
            "principal_ratio": Rational(-5, 4),
        }
        assert ratios[(4, 5, 3, 6)] == {
            "residue_ratio": Rational(-3, 4),
            "principal_ratio": Rational(-3, 4),
        }
        assert ratios[(3, 5, 5, 3)] == {
            "residue_ratio": Rational(0),
            "principal_ratio": Rational(0),
        }

    def test_stage5_one_defect_family_report(self):
        report = stage5_one_defect_family_report()
        assert report["stage"] == 5
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert report["representative_defect"]["name"] == "D_5"
        assert report["representative_defect"]["expression"] == Symbol("D_5")
        defects = report["channel_defects"]
        assert set(defects) == {
            (3, 4, 5, 2),
            (3, 5, 5, 3),
            (4, 5, 5, 4),
            (5, 5, 4, 6),
            (3, 5, 4, 4),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
            (4, 5, 3, 6),
        }
        assert defects[(3, 5, 4, 4)]["ratio_to_D5"] == 1
        assert defects[(3, 5, 4, 4)]["defect_expression"] == Symbol("D_5")
        assert defects[(3, 4, 5, 2)]["ratio_to_D5"] == Rational(-5, 4)
        assert defects[(3, 4, 5, 2)]["defect_expression"] == Rational(-5, 4) * Symbol("D_5")
        assert defects[(4, 5, 3, 6)]["ratio_to_D5"] == Rational(-3, 4)
        assert defects[(4, 5, 3, 6)]["defect_expression"] == Rational(-3, 4) * Symbol("D_5")
        assert defects[(3, 5, 5, 3)]["defect_expression"] == 0
        assert defects[(5, 5, 4, 6)]["defect_expression"] == 0

    def test_stage5_visible_conjecture_network_collapse_report(self):
        report = stage5_visible_conjecture_network_collapse_report()
        assert report["stage"] == 5
        assert report["comparison_goal"]["channel"] == (3, 5, 4, 4)
        assert report["equivalent_surfaces"]["conj:winfty-stage5-entry-identities"][
            "nontrivial_channel"
        ] == (3, 4, 5, 2)
        assert report["equivalent_surfaces"]["conj:winfty-stage5-block-45"][
            "ratio_to_representative"
        ] == Rational(-3, 4)
        assert report["automatic_surfaces"]["conj:winfty-stage5-block-55"]["channel"] == (
            5,
            5,
            4,
            6,
        )

    def test_stage5_conjecture_defect_dictionary_report(self):
        report = stage5_conjecture_defect_dictionary_report()
        assert report["stage"] == 5
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert report["representative_defect"]["expression"] == Symbol("D_5")
        equivalent = report["equivalent_surfaces"]
        automatic = report["automatic_surfaces"]
        assert equivalent["conj:winfty-stage5-higher-spin-identities"]["defect_channel"] == (
            3,
            5,
            4,
            4,
        )
        assert equivalent["conj:winfty-stage5-entry-identities"]["ratio_to_D5"] == Rational(-5, 4)
        assert equivalent["conj:winfty-stage5-entry-identities"]["defect_expression"] == (
            Rational(-5, 4) * Symbol("D_5")
        )
        assert equivalent["conj:winfty-stage5-block-45"]["ratio_to_D5"] == Rational(-3, 4)
        assert automatic["conj:winfty-stage5-transport-target-5"]["defect_expression"] == 0
        assert automatic["conj:winfty-stage5-block-55"]["ratio_to_D5"] == 0

    def test_stage5_exact_remaining_input_report(self):
        report = stage5_exact_remaining_input_report()
        assert report["stage"] == 5
        assert set(report["higher_spin_packet"]) == {
            (3, 4, 5, 2),
            (3, 5, 5, 3),
            (4, 5, 5, 4),
            (5, 5, 4, 6),
            (3, 5, 4, 4),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
            (4, 5, 3, 6),
        }
        assert report["principal_target5_corridor"]["representative_channel"] == (3, 5, 4, 4)
        assert report["principal_residual_front"]["representative_channel"] == (3, 5, 4, 4)
        assert report["principal_factorization"]["representative_channel"] == (3, 5, 4, 4)
        assert report["singleton_identity"]["channel"] == (3, 5, 4, 4)
        assert report["remaining_input_package"] == (
            "principal_target5_no_new_independent_data",
            "principal_residual_front_one_coefficient",
            "singleton_identity",
        )

    def test_stage5_one_coefficient_comparison_report(self):
        report = stage5_one_coefficient_comparison_report()
        assert report["stage"] == 5
        assert report["representative_channel"] == (3, 5, 4, 4)
        assert report["comparison_goal"]["channel"] == (3, 5, 4, 4)
        assert (
            report["comparison_goal"]["identity"]
            == "C^res_{3,5;4;0,4}(5) = C^DS_{3,5;4;0,4}(5)"
        )
        assert report["residue_normal_form"]["parameter"]["channel"] == (3, 5, 4, 4)
        assert report["principal_normal_form"]["parameter"]["channel"] == (3, 5, 4, 4)
        assert report["principal_target5_corridor"]["representative_channel"] == (3, 5, 4, 4)
        assert report["principal_residual_front"]["representative_channel"] == (3, 5, 4, 4)
        assert report["principal_factorization"]["representative_channel"] == (3, 5, 4, 4)
        assert report["comparison_reduction"]["reduction_goal"]["channel"] == (3, 5, 4, 4)
        assert report["defect_family"]["representative_defect"]["channel"] == (3, 5, 4, 4)
        assert report["conjecture_defect_dictionary"]["representative_defect"]["channel"] == (
            3,
            5,
            4,
            4,
        )
        assert report["exact_remaining_input"]["singleton_identity"]["channel"] == (3, 5, 4, 4)
        assert report["conjecture_network_collapse"]["comparison_goal"]["channel"] == (3, 5, 4, 4)
        assert report["effective_residue_frontier"]["effective_independent_count"] == 1


class TestStandardDualCandidateReport:
    def test_report_sections(self):
        report = standard_winfinity_dual_candidate_report()
        assert set(report) == {
            "completed_bar_candidate",
            "stage3",
            "stage4",
            "stage4_goal",
            "stage4_square_class",
            "stage4_pairing_reduction",
            "stage4_primitive_transport",
            "stage4_borcherds_transport",
            "stage4_two_primitive_closure",
            "stage4_local_attack_order",
            "stage4_level_contract",
            "stage5_frontier",
            "stage5_local_attack_order",
            "stage5_visible_pairing_normal_form",
            "stage5_principal_one_coefficient_normal_form",
            "stage5_principal_target5_no_new_independent_data",
            "stage5_principal_residual_front_one_coefficient",
            "stage5_principal_one_coefficient_factorization",
            "stage5_effective_independent_frontier",
            "stage5_one_coefficient_reduction",
            "stage5_one_defect_family",
            "stage5_conjecture_defect_dictionary",
            "stage5_exact_remaining_input",
            "stage5_visible_conjecture_network_collapse",
            "stage5_one_coefficient_comparison",
        }

    def test_verification_bundle(self):
        assert all(verify_standard_winfinity_dual_candidate().values())
