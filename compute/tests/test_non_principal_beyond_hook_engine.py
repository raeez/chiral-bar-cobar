"""Independent-oracle tests for the typed beyond-hook engine."""

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.non_principal_beyond_hook_engine import (
    ClaimStatus,
    OpenInvariantError,
    brst_complex_analysis,
    complementarity_analysis,
    ds_kd_status,
    full_catalog,
    is_even_nilpotent,
    is_rectangular,
    non_hook_catalog,
    non_hook_duality_profile,
    numerical_c_complementarity,
    numerical_kappa_complementarity,
    partition_orbit_class,
    self_transpose_catalog,
    shadow_depth_analysis,
    transport_reachability,
    verify_self_transpose_c_complementarity,
)
from compute.lib.hook_type_w_duality import krw_central_charge, w_algebra_generator_data
from compute.lib.nonprincipal_ds_orbits import (
    _partitions_of_n,
    homogeneous_f_centralizer_basis_sl_n,
    transpose_partition,
    type_a_partition_sl2_triple,
)


k = Symbol("k")


def _matrix_weight_oracle(partition):
    triple = type_a_partition_sl2_triple(partition)
    centralizer = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    return sorted(
        Rational(1) - Rational(grade, 2)
        for grade, basis in centralizer.items()
        for _ in basis
    )


class TestPartitionClassification:
    @pytest.mark.parametrize("partition", [(4,), (3, 1), (2, 1, 1), (3, 1, 1)])
    def test_hooks(self, partition):
        assert partition_orbit_class(partition) == "hook"

    def test_rectangular_self_transpose(self):
        assert is_rectangular((2, 2))
        assert partition_orbit_class((2, 2)) == "self_transpose_rectangular"

    def test_nonrectangular_self_transpose(self):
        assert transpose_partition((3, 2, 1)) == (3, 2, 1)
        assert partition_orbit_class((3, 2, 1)) == "self_transpose_nonhook"

    @pytest.mark.parametrize("partition", [(3, 2), (2, 2, 1), (3, 3), (2, 2, 2)])
    def test_nonselftranspose_nonhooks(self, partition):
        assert partition_orbit_class(partition) == "non_self_transpose_nonhook"

    @pytest.mark.parametrize(
        ("partition", "expected"),
        [((2, 2), True), ((3, 3), True), ((2, 2, 2), True), ((3, 2), False), ((3, 2, 1), False)],
    )
    def test_even_nilpotent_criterion(self, partition, expected):
        assert is_even_nilpotent(partition) is expected

    def test_ds_kd_status_is_conditional(self):
        for partition in ((2, 2), (3, 2), (3, 2, 1), (3, 1)):
            packet = ds_kd_status(partition)
            assert packet.status is ClaimStatus.CONDITIONAL
            assert packet.value is None


class TestBRSTCombinatorics:
    @pytest.mark.parametrize(
        ("partition", "dimension", "grades", "abelian", "half_dimension"),
        [
            ((2, 2), 4, {Rational(1): 4}, True, 0),
            ((3, 2), 10, {Rational(1, 2): 4, Rational(1): 3, Rational(3, 2): 2, Rational(2): 1}, False, 4),
            ((2, 2, 1), 8, {Rational(1, 2): 4, Rational(1): 4}, False, 4),
            ((3, 2, 1), 14, {Rational(1, 2): 6, Rational(1): 5, Rational(3, 2): 2, Rational(2): 1}, False, 6),
            ((3, 3), 12, {Rational(1): 8, Rational(2): 4}, False, 0),
        ],
    )
    def test_good_grading_oracles(self, partition, dimension, grades, abelian, half_dimension):
        data = brst_complex_analysis(partition)
        assert data.n_plus_dim == dimension
        assert data.n_plus_grades == grades
        assert data.n_plus_is_abelian is abelian
        assert data.g_half_dim == half_dimension

    @pytest.mark.parametrize("partition", [(2, 2), (3, 2), (3, 2, 1), (3, 3)])
    def test_pbw_and_koszul_consequences_are_conditional(self, partition):
        data = brst_complex_analysis(partition)
        assert data.pbw_collapse.status is ClaimStatus.CONDITIONAL
        assert data.pbw_collapse.value is None
        assert data.is_koszul.status is ClaimStatus.CONDITIONAL
        assert data.is_koszul.value is None


class TestCentralScalarAndModularSeparation:
    def test_22_formal_central_sum(self):
        data = complementarity_analysis((2, 2), k)
        assert data.is_self_transpose
        assert data.c_sum_k_independent
        assert simplify(data.c_sum - 110) == 0
        assert simplify(data.formal_central_midpoint - 55) == 0

    def test_321_formal_central_sum(self):
        data = complementarity_analysis((3, 2, 1), k)
        assert data.is_self_transpose
        assert data.c_sum_k_independent
        assert simplify(data.c_sum - 320) == 0
        assert simplify(data.formal_central_midpoint - 160) == 0

    @pytest.mark.parametrize(
        ("partition", "expected"),
        [((3, 2), 110 - 18 * k), ((2, 2, 1), 290 + 18 * k), ((3, 3), 148 - 30 * k)],
    )
    def test_nonselftranspose_central_sums(self, partition, expected):
        data = complementarity_analysis(partition, k)
        assert simplify(data.c_sum - expected) == 0
        assert not data.c_sum_k_independent

    @pytest.mark.parametrize(
        ("partition", "diagnostic"),
        [((2, 2), Rational(5)), ((3, 2), Rational(67, 15)), ((3, 2, 1), Rational(39, 5))],
    )
    def test_reciprocal_weight_diagnostics(self, partition, diagnostic):
        data = complementarity_analysis(partition, k)
        assert data.reciprocal_weight_diagnostic_source == diagnostic
        assert data.rho_source.status is ClaimStatus.OPEN
        assert data.rho_source.value is None

    @pytest.mark.parametrize("partition", [(2, 2), (3, 2), (3, 2, 1)])
    def test_kappa_and_modular_conductor_are_typed(self, partition):
        data = complementarity_analysis(partition, k)
        assert data.kappa_source.status is ClaimStatus.CONDITIONAL
        assert data.kappa_source.value is None
        assert data.modular_conductor.status is ClaimStatus.OPEN
        assert data.modular_conductor.value is None
        with pytest.raises(OpenInvariantError):
            data.modular_conductor.require_value()

    def test_central_charge_paths_match_direct_krw(self):
        for partition in ((2, 2), (3, 2), (3, 2, 1)):
            data = complementarity_analysis(partition, k)
            reflected = -k - 2 * sum(partition)
            assert simplify(data.c_source - krw_central_charge(partition, k)) == 0
            assert simplify(
                data.c_transpose_reflected
                - krw_central_charge(transpose_partition(partition), reflected)
            ) == 0


class TestGeneratorAndShadowSurface:
    @pytest.mark.parametrize("partition", [(2, 2), (3, 2), (2, 2, 1), (3, 2, 1), (3, 3)])
    def test_generator_weights_match_matrix_centralizer(self, partition):
        data = shadow_depth_analysis(partition)
        assert list(data.generator_weights) == _matrix_weight_oracle(partition)

    @pytest.mark.parametrize("partition", [(2, 2), (3, 2), (2, 2, 1), (3, 2, 1), (3, 3)])
    def test_generators_are_even_and_full_depth_is_open(self, partition):
        data = shadow_depth_analysis(partition)
        assert data.n_even == len(data.generator_weights)
        assert data.n_odd == 0
        assert data.virasoro_line_present
        assert data.full_shadow_depth.status is ClaimStatus.OPEN
        assert data.full_shadow_depth.value is None
        assert data.rho.status is ClaimStatus.OPEN
        assert data.kappa.status is ClaimStatus.CONDITIONAL

    def test_weight_one_and_high_weight_flags_are_exact(self):
        data_22 = shadow_depth_analysis((2, 2))
        assert data_22.n_weight_1 == 3
        assert data_22.has_weight_1_generators
        assert not data_22.has_weight_ge_3
        data_32 = shadow_depth_analysis((3, 2))
        assert data_32.n_weight_1 == 1
        assert data_32.has_weight_ge_3


class TestTransportGraph:
    @pytest.mark.parametrize(
        ("N", "partitions", "hooks"),
        [(4, 5, 4), (5, 7, 5), (6, 11, 6), (7, 15, 7)],
    )
    def test_finite_graph_reachability(self, N, partitions, hooks):
        data = transport_reachability(N)
        assert data.total_partitions == partitions
        assert data.n_hook == hooks
        assert data.hook_graph_closure_size == partitions
        assert data.graph_reaches_all_partitions
        assert data.graph_unreachable == ()
        assert data.categorical_transport.status is ClaimStatus.CONDITIONAL
        assert data.categorical_transport.value is None

    def test_graph_distance_is_combinatorial(self):
        data = transport_reachability(6)
        assert data.partition_data[(3, 2, 1)]["graph_distance_from_hooks"] == 1
        assert data.partition_data[(2, 2, 2)]["graph_distance_from_hooks"] == 2
        assert data.partition_data[(3, 2, 1)]["transport_claim"].status is ClaimStatus.CONDITIONAL


class TestProfilesAndCatalogs:
    @pytest.mark.parametrize("partition", [(2, 2), (3, 2), (3, 2, 1)])
    def test_profile_keeps_object_claims_conditional(self, partition):
        profile = non_hook_duality_profile(partition, k)
        assert profile.graph_reachable_from_hooks
        assert profile.categorical_transport.status is ClaimStatus.CONDITIONAL
        assert profile.ds_bar_commutation.status is ClaimStatus.CONDITIONAL
        assert profile.koszul_duality.status is ClaimStatus.CONDITIONAL
        assert profile.ksdual_membership.status is ClaimStatus.CONDITIONAL

    def test_nonhook_catalog_counts(self):
        assert len(non_hook_catalog(4)) == 1
        assert len(non_hook_catalog(5)) == 2
        assert len(non_hook_catalog(6)) == 5
        assert len(full_catalog(6)) == 11

    def test_catalog_dispatches_named_comparison_packages(self):
        hook = non_hook_duality_profile((3, 1), k)
        nonhook = non_hook_duality_profile((2, 2), k)
        assert any("H_hook" in item for item in hook.categorical_transport.hypotheses)
        assert any("H_nonhook" in item for item in nonhook.categorical_transport.hypotheses)

    def test_selftranspose_catalog_and_central_audit(self):
        profiles = self_transpose_catalog(6)
        partitions = {profile.partition for profile in profiles}
        assert {(2, 1), (2, 2), (3, 1, 1), (3, 2, 1)} <= partitions
        audit = verify_self_transpose_c_complementarity(6)
        assert all(row["central_sum_k_independent"] for row in audit)
        assert all(row["duality_claim"].status is ClaimStatus.CONDITIONAL for row in audit)


class TestNumericalHelpers:
    def test_numeric_central_sum_for_22(self):
        rows = numerical_c_complementarity((2, 2), [Rational(0), Rational(1), Rational(5)])
        assert {row["c_sum"] for row in rows} == {Rational(110)}

    def test_numeric_central_sum_for_32_varies(self):
        rows = numerical_c_complementarity((3, 2), [Rational(0), Rational(1), Rational(2)])
        assert [row["c_sum"] for row in rows] == [110, 92, 74]

    def test_numeric_kappa_helper_is_open(self):
        packet = numerical_kappa_complementarity((2, 2))
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None


def test_source_excludes_legacy_promotions():
    source = Path("compute/lib/non_principal_beyond_hook_engine.py").read_text()
    fragments = (
        "pbw_collapse=" + "True",
        "is_koszul=" + "True",
        "proved_self_" + "dual_rect",
        "source_n_" + "fermionic",
        "shadow_class=" + "'M'",
        "rho_match=" + "(rho_s == rho_d)",
    )
    assert all(source.find(fragment) == -1 for fragment in fragments)
