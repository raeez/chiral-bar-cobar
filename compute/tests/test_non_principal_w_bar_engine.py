"""Oracle tests for the exact non-principal type-A W-algebra engine.

The tests separate four surfaces:

* Young-diagram and nilpotent-centralizer combinatorics;
* PBW strong-generator weights and parity;
* KRW central charges and the primary BP OPE convention;
* typed proof obligations for modular, bar, shadow, and duality claims.

The matrix-centralizer oracle is independent of the engine's tensor-product
formula for generator weights.  The BP and principal central-charge oracles
are hardcoded from primary-source formulas rather than engine output.
"""

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.non_principal_w_bar_engine import (
    ClaimPacket,
    ClaimStatus,
    OpenInvariantError,
    all_partitions_of,
    bershadsky_polyakov_anomaly_ratio,
    bershadsky_polyakov_central_charge,
    bershadsky_polyakov_kappa,
    bershadsky_polyakov_ope_data,
    bershadsky_polyakov_profile,
    bershadsky_polyakov_reciprocal_weight_diagnostic,
    bershadsky_polyakov_scalar_audit,
    bershadsky_polyakov_shifted_central_charge,
    ds_depth_comparison,
    ds_kappa_additivity_check,
    formal_level_reflection,
    hook_type_edge_compatibility,
    kappa_multi_path_verification,
    koszul_dual_pairs,
    nilpotent_classification_table,
    principal_w_n_profile,
    sl4_hook_211_profile,
    sl4_hook_duality_check,
    sl4_subregular_31_profile,
    sl6_full_classification,
    transport_propagation_summary,
    transpose_partition_pairs,
    type_a_generator_weight_multiplicities,
    type_a_krw_central_charge,
    type_a_krw_central_charge_data,
    type_a_strong_generators,
    w_algebra_bar_profile,
)
from compute.lib.nonprincipal_ds_orbits import (
    centralizer_dimension_sl_n,
    homogeneous_f_centralizer_basis_sl_n,
    partition_size,
    transpose_partition,
    type_a_partition_sl2_triple,
)


k = Symbol("k")


def _matrix_centralizer_weight_multiset(partition):
    """Independent linear-algebra oracle for the generator weights."""

    triple = type_a_partition_sl2_triple(partition)
    graded = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    return sorted(
        Rational(1) - Rational(grade, 2)
        for grade, basis in graded.items()
        for _ in basis
    )


def _engine_weight_multiset(partition):
    return sorted(generator.conformal_weight for generator in type_a_strong_generators(partition))


class TestPartitionOracles:
    @pytest.mark.parametrize(
        ("N", "partition_count"),
        [(1, 1), (2, 2), (3, 3), (4, 5), (5, 7), (6, 11), (7, 15)],
    )
    def test_partition_numbers(self, N, partition_count):
        """Hardcoded Euler partition numbers give a census oracle."""

        assert len(all_partitions_of(N)) == partition_count

    @pytest.mark.parametrize("N", range(2, 8))
    def test_transpose_is_size_preserving_involution(self, N):
        for partition in all_partitions_of(N):
            transposed = transpose_partition(partition)
            assert partition_size(transposed) == N
            assert transpose_partition(transposed) == partition

    @pytest.mark.parametrize(
        "partition",
        [(2, 1), (3, 1), (2, 1, 1), (2, 2), (3, 2, 1), (4, 2)],
    )
    def test_generator_count_matches_partition_centralizer_formula(self, partition):
        """The generator count equals ``sum(column_length^2)-1``."""

        columns = transpose_partition(partition)
        oracle = sum(column * column for column in columns) - 1
        profile = w_algebra_bar_profile(partition)
        assert profile.num_generators == oracle
        assert profile.num_generators == centralizer_dimension_sl_n(partition)

    def test_transpose_orbits_partition_the_sl6_census(self):
        pairs = transpose_partition_pairs(6)
        recovered = {
            partition
            for pair in pairs
            for partition in (pair["partition"], pair["transpose"])
        }
        assert recovered == set(all_partitions_of(6))
        assert sum(pair["type"] == "self-transpose" for pair in pairs) == 1
        assert len(pairs) == 6


class TestGeneratorOracles:
    @pytest.mark.parametrize(
        "partition",
        [
            (2,),
            (3,),
            (2, 1),
            (3, 1),
            (2, 1, 1),
            (2, 2),
            (3, 2, 1),
        ],
    )
    def test_tensor_product_weights_match_matrix_centralizer(self, partition):
        """The combinatorial engine agrees with a matrix-kernel oracle."""

        assert _engine_weight_multiset(partition) == _matrix_centralizer_weight_multiset(partition)

    def test_bp_generator_ledger_is_primary_source_ledger(self):
        profile = bershadsky_polyakov_profile()
        assert [generator.label for generator in profile.generators] == ["J", "G+", "G-", "L"]
        assert [generator.conformal_weight for generator in profile.generators] == [
            Rational(1),
            Rational(3, 2),
            Rational(3, 2),
            Rational(2),
        ]
        assert profile.num_even == 4
        assert profile.num_odd == 0

    @pytest.mark.parametrize(
        "partition",
        [(2,), (3,), (2, 1), (3, 1), (2, 1, 1), (2, 2), (3, 2, 1)],
    )
    def test_type_a_strong_generators_are_even(self, partition):
        generators = type_a_strong_generators(partition)
        assert generators
        assert {generator.parity for generator in generators} == {"even"}

    def test_first_sl4_hook_weight_ledgers(self):
        minimal = sl4_hook_211_profile()
        subregular = sl4_subregular_31_profile()
        assert _engine_weight_multiset(minimal.partition) == [
            Rational(1), Rational(1), Rational(1), Rational(1),
            Rational(3, 2), Rational(3, 2), Rational(3, 2), Rational(3, 2),
            Rational(2),
        ]
        assert _engine_weight_multiset(subregular.partition) == [
            Rational(1), Rational(2), Rational(2), Rational(2), Rational(3),
        ]

    def test_principal_generator_weights(self):
        for N in range(2, 8):
            profile = principal_w_n_profile(N)
            assert _engine_weight_multiset(profile.partition) == list(range(2, N + 1))

    def test_weight_multiplicity_api_sums_to_centralizer_dimension(self):
        for N in range(2, 7):
            for partition in all_partitions_of(N):
                multiplicities = type_a_generator_weight_multiplicities(partition)
                assert sum(multiplicity for _, multiplicity in multiplicities) == (
                    centralizer_dimension_sl_n(partition)
                )


class TestKRWCentralCharge:
    def test_bp_krw_ingredients(self):
        """For BP, ``x=(1/2,0,-1/2)`` and the ghost polynomial sums to zero."""

        data = type_a_krw_central_charge_data((2, 1), k)
        assert data.x_diagonal == (Rational(1, 2), Rational(-1, 2), Rational(0)) or sorted(
            data.x_diagonal
        ) == [Rational(-1, 2), Rational(0), Rational(1, 2)]
        assert data.x_norm_squared == Rational(1, 2)
        assert sorted(data.positive_root_grades) == [Rational(1, 2), Rational(1, 2), Rational(1)]
        assert data.dim_g_half == 2
        assert simplify(data.charged_ghost_term) == 0

    def test_bp_standard_central_charge_matches_fkr_equation_2_2(self):
        """FKR (2021), equation (2.2), is the independent oracle."""

        expected = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
        assert simplify(type_a_krw_central_charge((2, 1), k) - expected) == 0
        assert simplify(bershadsky_polyakov_central_charge(k) - expected) == 0

    def test_virasoro_oracle(self):
        """Principal ``sl_2`` gives ``1-6(k+1)^2/(k+2)``."""

        expected = 1 - 6 * (k + 1) ** 2 / (k + 2)
        assert simplify(type_a_krw_central_charge((2,), k) - expected) == 0

    def test_principal_w3_oracle(self):
        """Principal ``sl_3`` gives ``2-24(k+2)^2/(k+3)``."""

        expected = 2 - 24 * (k + 2) ** 2 / (k + 3)
        assert simplify(type_a_krw_central_charge((3,), k) - expected) == 0

    def test_zero_nilpotent_affine_oracle(self):
        for N in range(2, 7):
            expected = (N * N - 1) * k / (k + N)
            assert simplify(type_a_krw_central_charge((1,) * N, k) - expected) == 0

    def test_rectangular_22_oracle(self):
        expected = 15 * k / (k + 4) - 12 * k - 8
        assert simplify(type_a_krw_central_charge((2, 2), k) - expected) == 0

    def test_profile_central_charge_is_typed_and_resolved(self):
        profile = w_algebra_bar_profile((3, 1))
        assert profile.central_charge.status is ClaimStatus.PROVED_ELSEWHERE
        assert profile.central_charge.resolved
        assert profile.central_charge.require_value() == type_a_krw_central_charge((3, 1), k)


class TestBershadskyPolyakovPrimarySurface:
    def test_standard_and_shifted_scalar_surfaces_remain_distinct(self):
        assert simplify(
            bershadsky_polyakov_central_charge(k)
            - bershadsky_polyakov_shifted_central_charge(k)
        ) != 0

    def test_standard_central_scalar_sum_is_50(self):
        audit = bershadsky_polyakov_scalar_audit(k)
        assert audit.reflected_level == -k - 6
        assert simplify(audit.standard_sum - 50) == 0
        assert simplify(bershadsky_polyakov_central_charge(0) + bershadsky_polyakov_central_charge(-6) - 50) == 0

    def test_shifted_secondary_scalar_sum_is_196(self):
        audit = bershadsky_polyakov_scalar_audit(k)
        assert simplify(audit.shifted_sum - 196) == 0
        assert simplify(
            bershadsky_polyakov_shifted_central_charge(0)
            + bershadsky_polyakov_shifted_central_charge(-6)
            - 196
        ) == 0

    def test_reciprocal_weight_diagnostic_is_17_over_6(self):
        direct_oracle = Rational(1) + Rational(2, 3) + Rational(2, 3) + Rational(1, 2)
        assert bershadsky_polyakov_reciprocal_weight_diagnostic() == direct_oracle == Rational(17, 6)

    def test_formal_level_reflection_is_an_involution(self):
        for N in range(2, 8):
            reflected = formal_level_reflection(N, k)
            assert simplify(formal_level_reflection(N, reflected) - k) == 0

    def test_bp_ope_jj_and_gg_leading_coefficients(self):
        """FKR (2021), equation (2.1), supplies these hardcoded oracles."""

        ope = bershadsky_polyakov_ope_data(k)
        assert simplify(ope.coefficient("J", "J", 2) - (2 * k + 3) / 3) == 0
        assert simplify(ope.coefficient("G+", "G-", 3) - (k + 1) * (2 * k + 3)) == 0
        assert simplify(ope.coefficient("L", "L", 4) - bershadsky_polyakov_central_charge(k) / 2) == 0

    def test_bp_ope_weight_and_charge_channels(self):
        ope = bershadsky_polyakov_ope_data(k)
        assert ope.coefficient("L", "G+", 2) == Rational(3, 2) * Symbol("G_plus")
        assert ope.coefficient("L", "G-", 2) == Rational(3, 2) * Symbol("G_minus")
        assert ope.coefficient("J", "G+", 1) == Symbol("G_plus")
        assert ope.coefficient("J", "G-", 1) == -Symbol("G_minus")
        assert ope.terms("G+", "G+") == ()
        assert ope.terms("G-", "G-") == ()

    def test_bp_profile_uses_standard_central_charge(self):
        profile = bershadsky_polyakov_profile()
        assert simplify(profile.central_charge.require_value() - bershadsky_polyakov_central_charge(k)) == 0


class TestTypedFrontierClaims:
    @pytest.mark.parametrize(
        "field",
        [
            "rho",
            "modular_characteristic",
            "modular_conductor",
            "full_shadow_depth",
            "bar_collapse",
            "ksdual_membership",
        ],
    )
    def test_profile_open_invariants_have_typed_none(self, field):
        packet = getattr(bershadsky_polyakov_profile(), field)
        assert isinstance(packet, ClaimPacket)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None
        with pytest.raises(OpenInvariantError):
            packet.require_value()

    @pytest.mark.parametrize(
        "field",
        ["ds_bar_commutation", "koszul_duality_candidate"],
    )
    def test_profile_comparison_claims_are_conditional(self, field):
        packet = getattr(bershadsky_polyakov_profile(), field)
        assert packet.status is ClaimStatus.CONDITIONAL
        assert packet.value is None
        assert packet.hypotheses

    def test_bp_numeric_modular_apis_return_open_packets(self):
        for packet in (
            bershadsky_polyakov_kappa(k),
            bershadsky_polyakov_anomaly_ratio(),
            bershadsky_polyakov_scalar_audit(k).modular_conductor,
        ):
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None

    @pytest.mark.parametrize("partition", [(2, 1), (3, 1), (2, 1, 1), (3, 1, 1)])
    def test_ds_modular_and_multipath_apis_expose_obligations(self, partition):
        ds_packet = ds_kappa_additivity_check(partition)
        verification_packet = kappa_multi_path_verification(partition)
        assert ds_packet.status is ClaimStatus.CONDITIONAL
        assert ds_packet.value is None
        assert verification_packet.status is ClaimStatus.OPEN
        assert verification_packet.value is None

    def test_virasoro_line_keeps_full_shadow_depth_open(self):
        packet = ds_depth_comparison((2, 1))
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None
        assert "Maurer--Cartan" in packet.hypotheses[0]

    def test_self_transpose_bp_keeps_object_level_fixed_point_open(self):
        profile = bershadsky_polyakov_profile()
        assert profile.is_self_transpose
        assert profile.transpose == (2, 1)
        assert profile.ksdual_membership.status is ClaimStatus.OPEN
        assert profile.ksdual_membership.value is None

    def test_sl4_transpose_relation_and_duality_status_are_separate(self):
        data = sl4_hook_duality_check()
        assert data["are_transposes"]
        assert data["formal_level_reflection"] == -k - 8
        assert data["koszul_duality"].status is ClaimStatus.CONDITIONAL
        assert data["koszul_duality"].value is None

    def test_koszul_compatibility_api_returns_transpose_orbits_with_status(self):
        pairs = koszul_dual_pairs(6)
        assert len(pairs) == 6
        assert all(pair["koszul_duality"].status is ClaimStatus.CONDITIONAL for pair in pairs)
        assert all(pair["koszul_duality"].value is None for pair in pairs)


class TestCensusAndTransport:
    def test_sl6_census_has_exact_even_generator_ledgers(self):
        table = sl6_full_classification()
        assert len(table) == 11
        for entry in table:
            assert entry["num_generators"] == entry["num_even"]
            assert entry["num_odd"] == 0
            assert entry["central_charge"].resolved
            assert entry["kappa"].status is ClaimStatus.OPEN

    def test_classification_preserves_every_partition(self):
        for N in range(2, 7):
            table = nilpotent_classification_table(N)
            assert [entry["partition"] for entry in table] == list(all_partitions_of(N))

    def test_hook_edges_are_exact_transpose_edges_with_conditional_transport(self):
        for N in range(3, 8):
            edges = hook_type_edge_compatibility(N)
            assert len(edges) == N - 2
            for edge in edges:
                assert transpose_partition(edge["partition"]) == edge["transpose"]
                assert edge["transpose_involution"]
                assert edge["duality_candidate"].status is ClaimStatus.CONDITIONAL

    def test_transport_summary_reports_census_and_obligation(self):
        summary = transport_propagation_summary(6)
        assert [entry["N"] for entry in summary] == [3, 4, 5, 6]
        for entry in summary:
            assert entry["num_partitions"] == len(all_partitions_of(entry["N"]))
            assert entry["transport"].status is ClaimStatus.CONDITIONAL
            assert entry["transport"].value is None


def test_engine_source_has_no_legacy_numeric_promotions():
    source = Path("compute/lib/non_principal_w_bar_engine.py").read_text()
    for legacy_surface in (
        "98" + "/3",
        "kappa_" + "complementarity",
        "all_paths_" + "consistent",
        "shadow_depth_" + "on_T_line",
        "ds_kappa_" + "from_affine",
        "koszul_dual_" + "partition",
    ):
        assert source.find(legacy_surface) == -1
