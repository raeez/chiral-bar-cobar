"""Independent guards for the typed ``sl_3`` minimal/subregular BP bar audit."""

from __future__ import annotations

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.bp_koszul_conductor_engine import UnverifiedBPInvariantError
from compute.lib.sl3_subregular_bar import (
    BP_BAR_HYPOTHESES,
    BP_BAR_RESOLUTION_OBLIGATION,
    GENERATORS,
    GENERATOR_NAMES,
    PARTITION,
    bar_cohomology_generators,
    bar_spectral_sequence_e1,
    bp_anomaly_ratio,
    bp_central_charge,
    bp_dual_level,
    bp_is_chirally_koszul,
    bp_koszul_conductor,
    bp_koszul_dual,
    bp_nth_products,
    bp_primary_ope_normal_form,
    bp_reciprocal_weight_diagnostic,
    bp_shifted_central_charge,
    ds_bar_intertwining,
    kappa_all_paths_agree,
    kappa_deficit_analysis,
    kappa_path1_anomaly_ratio,
    kappa_path2_ds_from_affine,
    kappa_path3_complementarity,
    max_ope_generator_degree,
    n2_sca_structure,
    shadow_depth_classification,
    shadow_tower_on_T_line,
    verify_sl3_subregular_bar,
)


k = Symbol("k")
ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "compute" / "lib" / "sl3_subregular_bar.py"


class TestExactCentralAndGeneratorData:
    def test_standard_fkr_formula(self):
        expected = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
        assert simplify(bp_central_charge(k) - expected) == 0

    def test_standard_sample_values(self):
        assert bp_central_charge(0) == -1
        assert bp_central_charge(1) == -5
        assert bp_central_charge(Rational(-1, 2)) == Rational(2, 5)

    def test_shifted_formula_remains_separate(self):
        shifted = 2 - 24 * (k + 1) ** 2 / (k + 3)
        assert simplify(bp_shifted_central_charge(k) - shifted) == 0
        assert bp_shifted_central_charge(0) == -6
        assert bp_shifted_central_charge(Rational(-1, 2)) == Rational(-2, 5)

    @pytest.mark.parametrize("level", [0, 1, -1, 2, -4, Rational(1, 2)])
    def test_standard_companion_sum_is_50(self, level):
        direct = bp_central_charge(level) + bp_central_charge(bp_dual_level(level))
        assert simplify(direct) == 50

    def test_conductor_api_returns_exact_central_sum(self):
        assert simplify(bp_koszul_conductor() - 50) == 0

    def test_level_involution_and_pole(self):
        assert simplify(bp_dual_level(bp_dual_level(k)) - k) == 0
        assert bp_dual_level(-3) == -3
        with pytest.raises(ZeroDivisionError):
            bp_central_charge(-3)

    def test_partition_and_weights(self):
        assert PARTITION == (2, 1)
        assert tuple(GENERATORS) == GENERATOR_NAMES
        weights = sorted(datum["weight"] for datum in GENERATORS.values())
        assert weights == [1, Rational(3, 2), Rational(3, 2), 2]

    def test_all_generators_are_even(self):
        assert all(datum["parity"] == 0 for datum in GENERATORS.values())
        assert bp_reciprocal_weight_diagnostic() == Rational(17, 6)


class TestExactOPEPacket:
    def test_primary_normal_form(self):
        packet = bp_primary_ope_normal_form(k)
        assert simplify(packet["central_charge"] - bp_central_charge(k)) == 0
        assert simplify(packet["J_level"] - (2 * k + 3) / 3) == 0
        assert simplify(packet["G_pairing"] - (k + 1) * (2 * k + 3)) == 0
        assert simplify(packet["GJ_coefficient"] - 3 * (k + 1)) == 0
        assert packet["JJ_coefficient"] == 3
        assert simplify(packet["dJ_coefficient"] - 3 * (k + 1) / 2) == 0
        assert simplify(packet["T_coefficient"] + k + 3) == 0

    def test_all_sixteen_ordered_pairs_exist(self):
        products = bp_nth_products()
        assert set(products) == {(a, b) for a in GENERATOR_NAMES for b in GENERATOR_NAMES}

    def test_forward_mixed_ope(self):
        products = bp_nth_products()
        normal = bp_primary_ope_normal_form(k)
        forward = products[("G+", "G-")]
        assert simplify(forward[2]["vac"] - normal["G_pairing"]) == 0
        assert simplify(forward[1]["J"] - normal["GJ_coefficient"]) == 0
        assert forward[0]["JJ"] == 3

    def test_reverse_mixed_ope_uses_ordinary_skew_symmetry(self):
        products = bp_nth_products()
        normal = bp_primary_ope_normal_form(k)
        reverse = products[("G-", "G+")]
        assert simplify(reverse[2]["vac"] + normal["G_pairing"]) == 0
        assert simplify(reverse[1]["J"] - normal["GJ_coefficient"]) == 0
        assert reverse[0]["JJ"] == -3
        assert simplify(reverse[0]["T"] + normal["T_coefficient"]) == 0

    def test_same_charge_products_vanish_by_charge(self):
        products = bp_nth_products()
        assert products[("G+", "G+")] == {}
        assert products[("G-", "G-")] == {}

    def test_quadratic_generator_degree_is_input_not_collapse(self):
        assert max_ope_generator_degree() == 2
        assert bp_is_chirally_koszul()["canonical_arity"] is None


class TestOpenKappaFirewall:
    @pytest.mark.parametrize(
        "function",
        [
            bp_anomaly_ratio,
            kappa_path1_anomaly_ratio,
            kappa_path2_ds_from_affine,
            kappa_path3_complementarity,
        ],
    )
    def test_numeric_kappa_apis_fail_loudly(self, function):
        with pytest.raises(UnverifiedBPInvariantError, match="genus-one"):
            function()

    def test_three_path_packet_exposes_one_open_obligation(self):
        packet = kappa_all_paths_agree()
        assert packet["path1"] is None
        assert packet["path2"] is None
        assert packet["path3"] is None
        assert packet["all_agree"] is None
        assert packet["status"] == "open-genus-one-computation"

    def test_deficit_is_withheld(self):
        packet = kappa_deficit_analysis()
        assert packet["kappa_bp"] is None
        assert packet["deficit"] is None
        assert simplify(packet["total_DS_conformal_shift"] + 6 * k + 1) == 0


class TestBarAndDualityStatus:
    def test_pbw_evidence_does_not_promote_koszulness(self):
        packet = bp_is_chirally_koszul()
        assert packet["is_koszul"] is None
        assert packet["canonical_arity"] is None
        assert packet["n_generators"] == 4
        assert packet["bar_collapse_status"] == "open-strong-convergence-and-diagonal-homology"
        assert packet["hypothesis_package"] == BP_BAR_HYPOTHESES

    def test_bar_spectral_sequence_withholds_page_and_collapse(self):
        packet = bar_spectral_sequence_e1()
        assert packet["dim_V"] == 4
        assert packet["e1_page"] is None
        assert packet["collapses_at"] is None
        assert packet["bar_cohomology"] is None
        assert packet["resolution_obligation"] == BP_BAR_RESOLUTION_OBLIGATION

    def test_bar_cohomology_generators_are_open(self):
        packet = bar_cohomology_generators()
        assert packet["n_generators"] is None
        assert packet["generators"] is None
        assert simplify(packet["dual_level"] + k + 6) == 0

    def test_self_transpose_partition_does_not_prove_same_family_dual(self):
        packet = bp_koszul_dual()
        assert packet["partition_self_transpose"] is True
        assert packet["central_conductor"] == 50
        assert packet["same_family_duality_status"] == "conditional-H_BP_DS_bar"
        assert packet["dual_kappa"] is None
        assert packet["kappa_sum"] is None

    def test_ds_bar_intertwining_is_open_with_exact_total_shift(self):
        packet = ds_bar_intertwining()
        assert simplify(packet["total_DS_conformal_shift"] + 6 * k + 1) == 0
        assert packet["total_shift_check"] is True
        assert packet["charged_neutral_improvement_decomposition"] is None
        assert packet["ds_preserves_koszulness"] is None
        assert packet["ds_preserves_swiss_cheese_formality"] is None
        assert packet["intertwiner_status"] == "open-filtered-DS-bar-comparison"


class TestShadowScope:
    def test_t_line_packet_contains_only_certified_initial_value(self):
        packet = shadow_tower_on_T_line(6)
        assert packet["max_arity_requested"] == 6
        assert simplify(packet["S2_T"] - bp_central_charge(k) / 2) == 0
        assert packet["higher_coefficients"] is None

    def test_full_bp_shadow_class_is_withheld(self):
        packet = shadow_depth_classification()
        assert packet["generic_class"] is None
        assert packet["generic_depth"] is None
        assert packet["critical_level"] == -3
        assert packet["status"] == "open-full-shadow-tower-computation"
        for root in packet["T_line_c_zero_levels"]:
            assert simplify(bp_central_charge(root)) == 0
        for root in packet["T_line_5c_plus_22_zero_levels"]:
            assert simplify(5 * bp_central_charge(root) + 22) == 0

    def test_legacy_n2_wrapper_returns_even_bp_structure(self):
        packet = n2_sca_structure()
        assert packet["is_n2_sca"] is False
        assert packet["is_feigin_semikhatov_bp"] is True
        assert packet["all_generators_even"] is True
        assert packet["charge_conservation"] is True


class TestFullAudit:
    def test_every_certified_check_passes(self):
        checks = verify_sl3_subregular_bar()
        assert checks
        assert all(checks.values()), checks

    def test_source_contains_no_retired_promotions(self):
        source = ENGINE.read_text(encoding="utf-8")
        for stale in (
            "BP_k is chirally Koszul",
            "DS preserves Koszulness",
            "kappa_sum_value",
            "kappa(BP_k) = (1/6)",
            '"generic_class": "M"',
            '"collapses_at": "E_1"',
        ):
            assert stale not in source

    def test_every_bar_hypothesis_is_named(self):
        packet = bp_is_chirally_koszul()
        for hypothesis in (
            "completed_BP_bar_complex_constructed",
            "bar_spectral_sequence_strongly_convergent",
            "comparison_q_BP_quasi_isomorphism",
            "DS_bar_intertwiner_constructed_and_filtered",
        ):
            assert hypothesis in packet["hypothesis_package"]
