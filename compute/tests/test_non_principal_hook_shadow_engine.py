r"""Independent-oracle tests for the typed hook-shadow engine."""

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.hook_type_w_duality import krw_central_charge
from compute.lib.non_principal_hook_shadow_engine import (
    ClaimPacket,
    ClaimStatus,
    OpenInvariantError,
    ds_cascade_check,
    ds_cascade_numerical,
    hook_anomaly_ratio_table,
    hook_c_conductor_table,
    hook_complementarity_constants,
    hook_cross_family_consistency,
    hook_generator_spectrum,
    hook_kappa_multi_path,
    hook_landscape,
    hook_quintic_shadow,
    hook_shadow_depth_table,
    hook_shadow_growth_landscape,
    hook_shadow_metric,
    hook_shadow_metric_numerical,
    hook_shadow_profile,
    hook_shadow_tower_landscape,
    minimal_hook_check,
    principal_limit_check,
    subregular_hook_check,
    transport_to_transpose_check,
)
from compute.lib.non_principal_w_bar_engine import bershadsky_polyakov_ope_data
from compute.lib.nonprincipal_ds_orbits import (
    homogeneous_f_centralizer_basis_sl_n,
    transpose_partition,
    type_a_partition_sl2_triple,
)


k = Symbol("k")


def _matrix_weight_oracle(partition):
    """Compute weights independently from the homogeneous matrix centralizer."""

    triple = type_a_partition_sl2_triple(partition)
    centralizer = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    return tuple(sorted(
        Rational(1) - Rational(grade, 2)
        for grade, basis in centralizer.items()
        for _ in basis
    ))


def _assert_unresolved(packet: ClaimPacket, status: ClaimStatus):
    assert packet.status is status
    assert packet.value is None
    assert packet.hypotheses
    with pytest.raises(OpenInvariantError):
        packet.require_value()


class TestExactHookProfiles:
    @pytest.mark.parametrize(
        ("N", "m", "partition", "transpose"),
        [
            (3, 0, (3,), (1, 1, 1)),
            (3, 1, (2, 1), (2, 1)),
            (4, 0, (4,), (1, 1, 1, 1)),
            (4, 1, (3, 1), (2, 1, 1)),
            (4, 2, (2, 1, 1), (3, 1)),
            (5, 1, (4, 1), (2, 1, 1, 1)),
            (5, 2, (3, 1, 1), (3, 1, 1)),
            (5, 3, (2, 1, 1, 1), (4, 1)),
        ],
    )
    def test_partition_and_transpose(self, N, m, partition, transpose):
        profile = hook_shadow_profile(N, m)
        assert profile.partition == partition
        assert profile.transpose == transpose
        assert transpose_partition(profile.transpose) == profile.partition
        assert profile.is_self_transpose is (partition == transpose)

    @pytest.mark.parametrize(
        ("partition", "N", "m"),
        [((2, 1), 3, 1), ((3, 1), 4, 1), ((2, 1, 1), 4, 2), ((3, 1, 1), 5, 2)],
    )
    def test_generator_weights_match_matrix_centralizer(self, partition, N, m):
        profile = hook_shadow_profile(N, m)
        assert profile.partition == partition
        assert profile.generator_weights == _matrix_weight_oracle(partition)
        assert profile.num_generators == len(profile.generator_weights)

    @pytest.mark.parametrize(("N", "m"), [(3, 0), (3, 1), (4, 1), (4, 2), (5, 2), (6, 3)])
    def test_type_a_generator_parity(self, N, m):
        profile = hook_shadow_profile(N, m)
        assert profile.num_even == profile.num_generators
        assert profile.num_odd == 0
        assert profile.num_bosonic == profile.num_even
        assert profile.num_fermionic == 0

    @pytest.mark.parametrize(("N", "m"), [(3, 0), (4, 1), (5, 2), (6, 4)])
    def test_central_charge_matches_direct_krw(self, N, m):
        profile = hook_shadow_profile(N, m)
        assert simplify(profile.central_charge - krw_central_charge(profile.partition, k)) == 0
        target = krw_central_charge(profile.transpose, -k - 2 * N)
        assert simplify(profile.formal_central_sum - profile.central_charge - target) == 0

    def test_self_transpose_sl5_central_scalar(self):
        profile = hook_shadow_profile(5, 2)
        assert profile.partition == (3, 1, 1)
        assert profile.formal_central_sum_k_independent
        assert simplify(profile.formal_central_sum - 212) == 0

    def test_parameter_range(self):
        with pytest.raises(ValueError):
            hook_shadow_profile(5, -1)
        with pytest.raises(ValueError):
            hook_shadow_profile(5, 4)


class TestBershadskyPolyakovPacket:
    def test_exact_scalar_and_diagnostic_data(self):
        profile = hook_shadow_profile(3, 1)
        assert profile.partition == (2, 1)
        assert profile.is_self_transpose
        assert profile.generator_weights == (1, Rational(3, 2), Rational(3, 2), 2)
        assert profile.reciprocal_weight_diagnostic == Rational(17, 6)
        assert profile.formal_central_sum_k_independent
        assert simplify(profile.formal_central_sum - 50) == 0
        assert simplify(profile.shifted_secondary_sum - 196) == 0

    def test_ope_pole_orders_match_primary_packet(self):
        profile = hook_shadow_profile(3, 1)
        direct = {
            (left, right): max((term.pole_order for term in terms), default=0)
            for left, right, terms in bershadsky_polyakov_ope_data(k).singular_products
        }
        assert dict(((left, right), pole) for left, right, pole in profile.exact_ope_pole_orders) == direct
        assert direct[("G+", "G-")] == 3
        assert direct[("L", "L")] == 4
        assert profile.ope_completion.status is ClaimStatus.PROVED_ELSEWHERE
        assert profile.ope_completion.value == bershadsky_polyakov_ope_data(k)

    def test_generic_hook_ope_completion_is_open(self):
        _assert_unresolved(hook_shadow_profile(4, 1).ope_completion, ClaimStatus.OPEN)


class TestTypedModularAndCategoricalClaims:
    @pytest.mark.parametrize(("N", "m"), [(3, 1), (4, 1), (4, 2), (5, 2)])
    def test_profile_claim_statuses(self, N, m):
        profile = hook_shadow_profile(N, m)
        _assert_unresolved(profile.rho, ClaimStatus.OPEN)
        _assert_unresolved(profile.kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(profile.modular_conductor, ClaimStatus.OPEN)
        _assert_unresolved(profile.full_shadow_depth, ClaimStatus.OPEN)
        _assert_unresolved(profile.ds_bar_commutation, ClaimStatus.CONDITIONAL)
        _assert_unresolved(profile.koszul_duality, ClaimStatus.CONDITIONAL)
        _assert_unresolved(profile.ksdual_membership, ClaimStatus.CONDITIONAL)
        assert profile.anomaly_ratio is profile.rho

    @pytest.mark.parametrize(("N", "m"), [(3, 1), (4, 1), (5, 2)])
    def test_metric_coefficients_are_open(self, N, m):
        metric = hook_shadow_metric(N, m)
        for packet in (
            metric.quadratic_coefficient,
            metric.quartic_coefficient,
            metric.discriminant,
            metric.growth_rate,
        ):
            _assert_unresolved(packet, ClaimStatus.OPEN)

    def test_metric_numerical_specializes_only_central_charge(self):
        result = hook_shadow_metric_numerical(4, 1, 2)
        profile = hook_shadow_profile(4, 1)
        assert result["partition"] == (3, 1)
        assert result["level"] == 2
        assert result["central_charge"] == simplify(profile.central_charge.subs(k, 2))
        _assert_unresolved(result["quadratic_coefficient"], ClaimStatus.OPEN)
        _assert_unresolved(result["growth_rate"], ClaimStatus.OPEN)

    def test_kappa_multi_path_is_an_obligation(self):
        _assert_unresolved(hook_kappa_multi_path(5, 2), ClaimStatus.OPEN)


class TestCascadeAndTransport:
    @pytest.mark.parametrize(
        ("N", "m", "source", "target"),
        [
            (4, 0, (4,), (3, 1)),
            (4, 1, (3, 1), (2, 1, 1)),
            (5, 2, (3, 1, 1), (2, 1, 1, 1)),
            (5, 3, (2, 1, 1, 1), (2, 1, 1, 1)),
        ],
    )
    def test_exact_cascade_indices_and_typed_comparison(self, N, m, source, target):
        cascade = ds_cascade_check(N, m)
        assert cascade.source_partition == source
        assert cascade.target_partition == target
        assert simplify(cascade.source_central_charge - krw_central_charge(source, k)) == 0
        assert simplify(cascade.target_central_charge - krw_central_charge(target, k)) == 0
        _assert_unresolved(cascade.cascade, ClaimStatus.CONDITIONAL)
        _assert_unresolved(cascade.depth_comparison, ClaimStatus.OPEN)
        _assert_unresolved(cascade.ds_bar_commutation, ClaimStatus.CONDITIONAL)

    def test_numerical_cascade_specializes_exact_fields(self):
        result = ds_cascade_numerical(5, 2, 1)
        assert result["source_partition"] == (3, 1, 1)
        assert result["target_partition"] == (2, 1, 1, 1)
        assert result["source_central_charge"] == krw_central_charge((3, 1, 1), 1)
        assert result["target_central_charge"] == krw_central_charge((2, 1, 1, 1), 1)
        _assert_unresolved(result["cascade"], ClaimStatus.CONDITIONAL)
        _assert_unresolved(result["depth_comparison"], ClaimStatus.OPEN)

    @pytest.mark.parametrize(("N", "m"), [(3, 1), (4, 1), (5, 2), (6, 3)])
    def test_transport_separates_exact_arithmetic_from_category(self, N, m):
        evidence = transport_to_transpose_check(N, m)
        assert evidence.transpose == transpose_partition(evidence.partition)
        assert evidence.transpose_involution
        assert simplify(evidence.formal_reflected_level + k + 2 * N) == 0
        _assert_unresolved(evidence.source_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(evidence.target_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(evidence.modular_conductor, ClaimStatus.OPEN)
        _assert_unresolved(evidence.transport, ClaimStatus.CONDITIONAL)
        _assert_unresolved(evidence.ds_bar_commutation, ClaimStatus.CONDITIONAL)
        _assert_unresolved(evidence.koszul_duality, ClaimStatus.CONDITIONAL)
        _assert_unresolved(evidence.ksdual_membership, ClaimStatus.CONDITIONAL)


class TestTablesAndLandscapes:
    def test_shadow_tower_landscape_has_exact_and_typed_fields(self):
        rows = hook_shadow_tower_landscape(5, 1, max_arity=7)
        assert len(rows) == 4
        assert [row["partition"] for row in rows] == [
            (5,), (4, 1), (3, 1, 1), (2, 1, 1, 1)
        ]
        for row in rows:
            assert row["central_charge"] == krw_central_charge(row["partition"], 1)
            _assert_unresolved(row["rho"], ClaimStatus.OPEN)
            _assert_unresolved(row["kappa"], ClaimStatus.CONDITIONAL)
            _assert_unresolved(row["shadow_tower"], ClaimStatus.OPEN)
            _assert_unresolved(row["full_shadow_depth"], ClaimStatus.OPEN)

    def test_depth_table_cardinality_and_claims(self):
        rows = hook_shadow_depth_table(6)
        assert len(rows) == sum(N - 1 for N in range(3, 7))
        assert all(row["num_even"] == row["num_generators"] for row in rows)
        assert all(row["num_odd"] == 0 for row in rows)
        assert all(row["rho"].status is ClaimStatus.OPEN for row in rows)
        assert all(row["full_shadow_depth"].status is ClaimStatus.OPEN for row in rows)

    def test_generator_spectrum_is_exact_and_even(self):
        spectrum = hook_generator_spectrum(4, 2)
        assert spectrum["partition"] == (2, 1, 1)
        assert spectrum["generator_weights"] == _matrix_weight_oracle((2, 1, 1))
        assert spectrum["n_odd"] == 0
        assert sum(row["even"] for row in spectrum["weight_distribution"].values()) == 9
        assert sum(row["odd"] for row in spectrum["weight_distribution"].values()) == 0
        assert sum(value for _, value in spectrum["reciprocal_weight_contributions"]) == spectrum[
            "reciprocal_weight_diagnostic"
        ]
        _assert_unresolved(spectrum["rho"], ClaimStatus.OPEN)

    def test_limit_checks_preserve_exact_fields(self):
        principal = principal_limit_check(6)
        assert principal["partition"] == (6,)
        assert principal["is_principal"]
        assert principal["central_charge_matches_krw"]
        assert principal["generators_match"]
        _assert_unresolved(principal["rho"], ClaimStatus.OPEN)

        subregular = subregular_hook_check(6)
        assert subregular["partition"] == (5, 1)
        assert subregular["is_subregular"]
        assert subregular["transpose"] == (2, 1, 1, 1, 1)

        minimal = minimal_hook_check(6)
        assert minimal["partition"] == (2, 1, 1, 1, 1)
        assert minimal["is_minimal"]
        assert minimal["transpose_is_subregular"]

    def test_hook_landscape_records_transpose_orbits(self):
        landscape = hook_landscape(5)
        assert landscape["num_hooks"] == 4
        assert len(landscape["profiles"]) == 4
        assert landscape["transpose_orbits"] == [
            {
                "type": "transpose-pair",
                "partition": (5,),
                "transpose": (1, 1, 1, 1, 1),
                "duality": landscape["transpose_orbits"][0]["duality"],
            },
            {
                "type": "transpose-pair",
                "partition": (4, 1),
                "transpose": (2, 1, 1, 1),
                "duality": landscape["transpose_orbits"][1]["duality"],
            },
            {
                "type": "self-transpose",
                "partition": (3, 1, 1),
                "transpose": (3, 1, 1),
                "duality": landscape["transpose_orbits"][2]["duality"],
            },
        ]
        assert all(
            orbit["duality"].status is ClaimStatus.CONDITIONAL
            for orbit in landscape["transpose_orbits"]
        )
        assert all(
            row.transport.status is ClaimStatus.CONDITIONAL
            for row in landscape["transport_evidence"]
        )

    def test_anomaly_table_keeps_diagnostic_and_rho_separate(self):
        rows = hook_anomaly_ratio_table(5)
        bp = next(row for row in rows if row["partition"] == (2, 1))
        assert bp["reciprocal_weight_diagnostic"] == Rational(17, 6)
        _assert_unresolved(bp["rho"], ClaimStatus.OPEN)
        assert all(row["num_odd"] == 0 for row in rows)

    def test_complementarity_and_central_tables_have_distinct_types(self):
        modular_rows = hook_complementarity_constants(5)
        assert all(row["modular_conductor"].status is ClaimStatus.OPEN for row in modular_rows)
        central_rows = hook_c_conductor_table(5)
        bp = next(row for row in central_rows if row["partition"] == (2, 1))
        self_transpose_sl5 = next(row for row in central_rows if row["partition"] == (3, 1, 1))
        assert bp["central_sum_k_independent"]
        assert simplify(bp["central_sum"] - 50) == 0
        assert self_transpose_sl5["central_sum_k_independent"]
        assert simplify(self_transpose_sl5["central_sum"] - 212) == 0

    def test_quintic_and_growth_fields_are_open(self):
        quintic = hook_quintic_shadow(5, 2)
        assert quintic["partition"] == (3, 1, 1)
        _assert_unresolved(quintic["quintic_shadow"], ClaimStatus.OPEN)
        growth = hook_shadow_growth_landscape(5, 1)
        assert len(growth) == 4
        for row in growth:
            assert row["central_charge"] == krw_central_charge(row["partition"], 1)
            _assert_unresolved(row["growth_rate"], ClaimStatus.OPEN)

    def test_cross_family_consistency_keeps_object_claims_typed(self):
        result = hook_cross_family_consistency(6)
        assert result["all_generators_even"]
        assert result["all_transposes_involutive"]
        assert result["principal_limit"]["generators_match"]
        assert all(packet.status is ClaimStatus.OPEN for packet in result["modular_claims"])
        assert all(packet.status is ClaimStatus.OPEN for packet in result["full_shadow_claims"])
        assert all(packet.status is ClaimStatus.CONDITIONAL for packet in result["transport_claims"])


def test_source_has_no_legacy_numeric_promotions():
    source = Path("compute/lib/non_principal_hook_shadow_engine.py").read_text()
    for legacy in (
        "shadow_class",
        "rho_contributions",
        "all_consistent",
        "koszul_pairs",
        "transport_verified",
        "depth_increases",
    ):
        assert legacy not in source
