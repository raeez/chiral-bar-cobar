"""Independent guards for the repaired W-algebra arithmetic engine."""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.theorem_w_algebra_chapter_rectification_engine import (
    UnverifiedWInvariantError,
    bcd_anomaly_ratio,
    bcd_exponents,
    bcd_generator_weights,
    bp_central_charge_correct,
    bp_complementarity_correct,
    bp_generator_parities,
    bp_kappa_complementarity_correct,
    bp_kappa_correct,
    bp_modular_status_packet,
    bp_reciprocal_weight_diagnostic,
    bp_shifted_secondary_central_charge,
    bp_shifted_secondary_complementarity,
    conformal_extension_collapse_examples,
    hook_generator_content_sl_n,
    logarithmic_verlinde_status,
    minimal_so_central_charge,
    minimal_so_is_rational,
    minimal_so_status,
    partition_transpose,
    sl_centralizer_dimension,
    verify_anomaly_ratio_principal_wn,
    verify_bp_central_charge_at_admissible_levels,
    verify_wn_c_complementarity_formula,
    wn_anomaly_ratio,
    wn_central_charge,
    wn_complementarity_sum,
    wn_kappa,
)


k = Symbol("k")


class TestBershadskyPolyakovConvention:
    def test_standard_formula(self):
        expected = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
        assert simplify(bp_central_charge_correct(k) - expected) == 0

    @pytest.mark.parametrize(
        ("level", "expected"),
        [
            (Rational(-3, 2), 0),
            (Rational(-1, 3), 0),
            (Rational(-1), 1),
            (Rational(-1, 2), Rational(2, 5)),
            (Rational(0), -1),
            (Rational(1), -5),
        ],
    )
    def test_standard_values(self, level, expected):
        assert bp_central_charge_correct(level) == expected

    def test_standard_reflection_sum(self):
        assert bp_complementarity_correct(k) == 50

    def test_shifted_expression_is_separate(self):
        assert simplify(
            bp_central_charge_correct(k) - bp_shifted_secondary_central_charge(k)
        ) != 0
        assert bp_shifted_secondary_complementarity(k) == 196

    def test_all_generators_are_even(self):
        assert set(bp_generator_parities().values()) == {"even"}

    def test_reciprocal_weight_diagnostic(self):
        assert bp_reciprocal_weight_diagnostic() == Rational(17, 6)

    def test_modular_packet_is_open(self):
        packet = bp_modular_status_packet()
        assert packet["standard_central_conductor"] == 50
        assert packet["shifted_secondary_sum"] == 196
        assert packet["kappa"] is None
        assert packet["rho"] is None
        assert packet["K_kappa"] is None
        assert packet["status"] == "open"

    @pytest.mark.parametrize(
        "function",
        [bp_kappa_correct, bp_kappa_complementarity_correct],
    )
    def test_open_modular_apis_fail_loudly(self, function):
        with pytest.raises(UnverifiedWInvariantError):
            function(k)

    def test_level_packet_keeps_two_conventions(self):
        packet = verify_bp_central_charge_at_admissible_levels()
        assert packet[Rational(-3, 2)] == {
            "standard": 0,
            "shifted_secondary": -2,
        }
        assert packet[Rational(-1)] == {
            "standard": 1,
            "shifted_secondary": 2,
        }


class TestPrincipalTypeAArithmetic:
    def test_virasoro_formula(self):
        expected = 1 - 6 * (k + 1) ** 2 / (k + 2)
        assert simplify(wn_central_charge(2, k) - expected) == 0

    def test_w3_formula(self):
        expected = 2 - 24 * (k + 2) ** 2 / (k + 3)
        assert simplify(wn_central_charge(3, k) - expected) == 0

    @pytest.mark.parametrize(
        ("N", "reflection_sum"),
        [(2, 26), (3, 100), (4, 246), (5, 488)],
    )
    def test_reflection_identity(self, N, reflection_sum):
        assert wn_complementarity_sum(N) == reflection_sum

    def test_reflection_report_names_its_scope(self):
        report = verify_wn_c_complementarity_formula()
        assert all(item["all_match"] for item in report.values())
        assert all(
            item["interpretation"] == "arithmetic reflection identity"
            for item in report.values()
        )

    @pytest.mark.parametrize(
        ("N", "diagnostic"),
        [(2, Rational(1, 2)), (3, Rational(5, 6)), (4, Rational(13, 12))],
    )
    def test_reciprocal_weight_diagnostic(self, N, diagnostic):
        assert wn_anomaly_ratio(N) == diagnostic
        assert verify_anomaly_ratio_principal_wn(N)["match"]

    def test_kappa_requires_genus_one_comparison(self):
        with pytest.raises(UnverifiedWInvariantError):
            wn_kappa(3, k)


class TestNilpotentPartitionCombinatorics:
    @pytest.mark.parametrize(
        ("partition", "transpose"),
        [
            ((3,), (1, 1, 1)),
            ((2, 1), (2, 1)),
            ((3, 1, 1), (3, 1, 1)),
            ((4, 1), (2, 1, 1, 1)),
        ],
    )
    def test_partition_transpose(self, partition, transpose):
        assert partition_transpose(partition) == transpose

    @pytest.mark.parametrize(
        ("partition", "dimension"),
        [((3,), 2), ((2, 1), 4), ((1, 1, 1), 8), ((3, 1, 1), 10)],
    )
    def test_sl_centralizer_dimension(self, partition, dimension):
        assert sl_centralizer_dimension(partition) == dimension

    def test_hook_dimension_closed_form(self):
        for N in range(3, 9):
            for r in range(N):
                packet = hook_generator_content_sl_n(N, r)
                assert packet["dim_slice"] == N - 1 + r * (r + 1)

    def test_principal_generator_packet(self):
        packet = hook_generator_content_sl_n(5, 0)
        assert packet["weights"] == (2, 3, 4, 5)
        assert packet["parities"] == ("even",) * 4

    def test_zero_orbit_affine_packet(self):
        packet = hook_generator_content_sl_n(4, 3)
        assert packet["weights"] == (1,) * 15
        assert packet["dim_slice"] == 15

    def test_intermediate_hook_keeps_shadow_open(self):
        packet = hook_generator_content_sl_n(5, 2)
        assert packet["weights"] is None
        assert packet["parities"] is None
        assert packet["shadow_class"] is None


class TestClassicalExponents:
    @pytest.mark.parametrize(
        ("lie_type", "rank", "exponents"),
        [
            ("B", 3, (1, 3, 5)),
            ("C", 3, (1, 3, 5)),
            ("D", 4, (1, 3, 3, 5)),
            ("D", 5, (1, 3, 4, 5, 7)),
        ],
    )
    def test_exponents_with_multiplicity(self, lie_type, rank, exponents):
        assert bcd_exponents(lie_type, rank) == exponents

    def test_generator_weights(self):
        assert bcd_generator_weights("D", 4) == (2, 4, 4, 6)

    def test_reciprocal_weight_sum_preserves_d4_multiplicity(self):
        assert bcd_anomaly_ratio("D", 4) == Rational(7, 6)


class TestPrimarySourceStatusPackets:
    def test_minimal_so_representation_scope(self):
        assert minimal_so_status(7)["representation_theorem"] is True
        assert minimal_so_status(8)["strongly_rational"] is True
        assert minimal_so_status(7)["strongly_rational"] is None
        assert minimal_so_status(6)["representation_theorem"] is False

    def test_boolean_compatibility_api_is_conservative(self):
        assert minimal_so_is_rational(8) is True
        assert minimal_so_is_rational(10) is True
        assert minimal_so_is_rational(7) is None
        assert minimal_so_is_rational(6) is None

    def test_unimplemented_krw_formula_fails_loudly(self):
        with pytest.raises(UnverifiedWInvariantError):
            minimal_so_central_charge(8, -1)

    def test_unverified_collapse_table_fails_loudly(self):
        with pytest.raises(UnverifiedWInvariantError):
            conformal_extension_collapse_examples()

    def test_logarithmic_verlinde_scope(self):
        packet = logarithmic_verlinde_status()
        assert packet["status"] == "proved under natural assumptions"
        assert packet["paper"] == "2411.11383"
        assert "singlet algebras" in packet["examples"]
        assert "admissible levels" in packet["examples"][1]
