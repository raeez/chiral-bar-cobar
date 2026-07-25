r"""Independent-oracle tests for the typed Butson inverse-reduction engine."""

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.hook_type_w_duality import krw_central_charge
from compute.lib.nonprincipal_ds_orbits import (
    _partitions_of_n,
    homogeneous_f_centralizer_basis_sl_n,
    transpose_partition,
    type_a_partition_sl2_triple,
)
from compute.lib.theorem_butson_inverse_reduction_engine import (
    ButsonAnalysisSummary,
    CY3VertexAlgebraCandidate,
    ClaimPacket,
    ClaimStatus,
    InverseReductionEdge,
    KappaEdgeData,
    KoszulnessData,
    OpenInvariantError,
    TransposeVerificationData,
    TransportGraph,
    all_inverse_reduction_edges,
    anomaly_ratio_catalog,
    anomaly_ratio_transpose_relation,
    build_transport_graph,
    butson_analysis,
    central_charge_conductor,
    central_charge_conductor_catalog,
    cy3_candidate_catalog,
    dominance_order,
    formal_central_scalar_sum,
    inverse_reduction_edge,
    is_covering_relation,
    is_positive_coroot_step,
    kappa_along_edge,
    koszulness_certificate,
    orbit_hasse_diagram,
    orbit_hasse_edges,
    partition_root_step,
    type_a_centralizer_dimension,
    type_a_orbit_dimension,
    verify_all_partitions_transport,
    verify_transport_to_transpose,
)


k = Symbol("k")


def _dominance_oracle(lam, mu):
    width = max(len(lam), len(mu))
    left = lam + (0,) * (width - len(lam))
    right = mu + (0,) * (width - len(mu))
    return all(sum(left[:j]) >= sum(right[:j]) for j in range(1, width + 1))


def _centralizer_oracle(partition):
    columns = tuple(
        sum(row >= column for row in partition)
        for column in range(1, partition[0] + 1)
    )
    return sum(column * column for column in columns) - 1


def _matrix_weight_oracle(partition):
    triple = type_a_partition_sl2_triple(partition)
    centralizer = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    return tuple(sorted(
        Rational(1) - Rational(grade, 2)
        for grade, basis in centralizer.items()
        for _ in basis
    ))


def _reciprocal_weight_oracle(partition):
    return sum(Rational(1) / weight for weight in _matrix_weight_oracle(partition))


def _assert_unresolved(packet: ClaimPacket, status: ClaimStatus):
    assert packet.status is status
    assert packet.value is None
    assert packet.hypotheses
    with pytest.raises(OpenInvariantError):
        packet.require_value()


class TestDominanceAndHasseArithmetic:
    def test_dominance_matches_partial_sum_oracle(self):
        for n in range(2, 7):
            partitions = tuple(_partitions_of_n(n))
            for lam in partitions:
                for mu in partitions:
                    assert dominance_order(lam, mu) is _dominance_oracle(lam, mu)

    def test_dominance_partial_order_extrema(self):
        for n in range(2, 8):
            for partition in _partitions_of_n(n):
                assert dominance_order((n,), partition)
                assert dominance_order(partition, (1,) * n)
                assert dominance_order(partition, partition)

    def test_partition_size_is_part_of_the_type(self):
        with pytest.raises(ValueError):
            dominance_order((3,), (2,))
        with pytest.raises(ValueError):
            is_covering_relation((3,), (2,))
        with pytest.raises(ValueError):
            partition_root_step((3,), (2,))

    @pytest.mark.parametrize(
        ("n", "partition_count", "edge_count"),
        [(2, 2, 1), (3, 3, 2), (4, 5, 4), (5, 7, 6), (6, 11, 12), (7, 15, 17)],
    )
    def test_hasse_census(self, n, partition_count, edge_count):
        assert len(orbit_hasse_diagram(n)) == partition_count
        assert len(orbit_hasse_edges(n)) == edge_count

    def test_sl4_hasse_chain(self):
        assert set(orbit_hasse_edges(4)) == {
            ((4,), (3, 1)),
            ((3, 1), (2, 2)),
            ((2, 2), (2, 1, 1)),
            ((2, 1, 1), (1, 1, 1, 1)),
        }

    def test_sl5_hasse_chain(self):
        assert set(orbit_hasse_edges(5)) == {
            ((5,), (4, 1)),
            ((4, 1), (3, 2)),
            ((3, 2), (3, 1, 1)),
            ((3, 1, 1), (2, 2, 1)),
            ((2, 2, 1), (2, 1, 1, 1)),
            ((2, 1, 1, 1), (1, 1, 1, 1, 1)),
        }

    def test_sl6_branching_covers(self):
        edges = set(orbit_hasse_edges(6))
        assert ((4, 2), (4, 1, 1)) in edges
        assert ((4, 2), (3, 3)) in edges
        assert ((4, 1, 1), (3, 2, 1)) in edges
        assert ((3, 3), (3, 2, 1)) in edges
        assert ((3, 2, 1), (3, 1, 1, 1)) in edges
        assert ((3, 2, 1), (2, 2, 2)) in edges

    @pytest.mark.parametrize("n", range(2, 9))
    def test_every_hasse_cover_is_a_positive_coroot_step(self, n):
        for target, source in orbit_hasse_edges(n):
            step = partition_root_step(target, source)
            assert [entry for entry in step if entry] == [1, -1]
            assert is_positive_coroot_step(target, source)


class TestExactInverseReductionEdges:
    def test_edge_dataclass_and_orientation(self):
        edge = inverse_reduction_edge(3, (1, 1, 1), (2, 1))
        assert isinstance(edge, InverseReductionEdge)
        assert edge.source == (1, 1, 1)
        assert edge.target == (2, 1)
        assert edge.root_step == (1, 0, -1)
        assert edge.is_positive_coroot_step

    def test_sl3_trivial_to_subregular_dimensions(self):
        edge = inverse_reduction_edge(3, (1, 1, 1), (2, 1))
        assert edge.source_centralizer_dim == 8
        assert edge.target_centralizer_dim == 4
        assert edge.source_orbit_dim == 0
        assert edge.target_orbit_dim == 4
        assert edge.centralizer_dimension_drop == 4
        assert edge.orbit_dimension_jump == 4
        assert edge.half_orbit_dimension_jump == 2

    @pytest.mark.parametrize("n", range(3, 8))
    def test_edge_dimensions_match_partition_oracles(self, n):
        for edge in all_inverse_reduction_edges(n):
            assert edge.source_centralizer_dim == _centralizer_oracle(edge.source)
            assert edge.target_centralizer_dim == _centralizer_oracle(edge.target)
            assert edge.source_orbit_dim == n * n - 1 - _centralizer_oracle(edge.source)
            assert edge.target_orbit_dim == n * n - 1 - _centralizer_oracle(edge.target)
            assert edge.centralizer_dimension_drop == edge.orbit_dimension_jump
            assert edge.orbit_dimension_jump == 2 * edge.half_orbit_dimension_jump

    @pytest.mark.parametrize("n", range(3, 7))
    def test_generator_counts_supply_an_independent_dimension_path(self, n):
        for edge in all_inverse_reduction_edges(n):
            assert edge.source_generators.f_centralizer_dimension == edge.source_centralizer_dim
            assert edge.target_generators.f_centralizer_dimension == edge.target_centralizer_dim
            assert edge.source_generators.n_odd == 0
            assert edge.target_generators.n_odd == 0

    def test_hook_edge_census_sl4(self):
        edges = all_inverse_reduction_edges(4)
        assert sum(edge.is_hook_edge for edge in edges) == 2
        assert sum(not edge.is_hook_edge for edge in edges) == 2

    def test_edge_scope_requires_a_cover(self):
        with pytest.raises(ValueError):
            inverse_reduction_edge(4, (2, 2), (4,))
        with pytest.raises(ValueError):
            inverse_reduction_edge(4, (3, 1), (2, 2))
        with pytest.raises(ValueError):
            inverse_reduction_edge(5, (2, 1, 1), (3, 1))

    @pytest.mark.parametrize("n", [3, 4, 5, 6])
    def test_inverse_reduction_and_bar_fields_are_conditional(self, n):
        for edge in all_inverse_reduction_edges(n):
            _assert_unresolved(edge.inverse_reduction, ClaimStatus.CONDITIONAL)
            _assert_unresolved(edge.auxiliary_free_fields, ClaimStatus.CONDITIONAL)
            _assert_unresolved(edge.bar_compatibility, ClaimStatus.CONDITIONAL)
            assert any("2508.18248" in item for item in edge.inverse_reduction.evidence)


class TestModularEdgeSeparation:
    def test_edge_central_arithmetic_matches_krw(self):
        edge = inverse_reduction_edge(4, (2, 2), (3, 1))
        data = kappa_along_edge(edge, k)
        assert isinstance(data, KappaEdgeData)
        assert simplify(data.source_central_charge - krw_central_charge((2, 2), k)) == 0
        assert simplify(data.target_central_charge - krw_central_charge((3, 1), k)) == 0
        assert simplify(
            data.formal_central_difference
            - data.source_central_charge
            + data.target_central_charge
        ) == 0

    def test_reciprocal_diagnostics_match_matrix_weights(self):
        edge = inverse_reduction_edge(5, (3, 1, 1), (3, 2))
        data = kappa_along_edge(edge, k)
        assert data.source_reciprocal_weight_diagnostic == _reciprocal_weight_oracle(
            edge.source
        )
        assert data.target_reciprocal_weight_diagnostic == _reciprocal_weight_oracle(
            edge.target
        )

    @pytest.mark.parametrize(
        ("n", "source", "target"),
        [
            (3, (2, 1), (3,)),
            (4, (2, 2), (3, 1)),
            (5, (3, 1, 1), (3, 2)),
        ],
    )
    def test_modular_values_remain_typed(self, n, source, target):
        data = kappa_along_edge(inverse_reduction_edge(n, source, target), k)
        _assert_unresolved(data.source_rho, ClaimStatus.OPEN)
        _assert_unresolved(data.target_rho, ClaimStatus.OPEN)
        _assert_unresolved(data.source_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.target_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.kappa_deficit, ClaimStatus.OPEN)
        _assert_unresolved(data.modular_additivity, ClaimStatus.CONDITIONAL)


class TestTransposeArithmeticAndClaims:
    @pytest.mark.parametrize(
        ("partition", "transpose"),
        [
            ((2, 1), (2, 1)),
            ((3, 1), (2, 1, 1)),
            ((3, 2), (2, 2, 1)),
            ((3, 2, 1), (3, 2, 1)),
        ],
    )
    def test_transpose_and_formal_level(self, partition, transpose):
        data = verify_transport_to_transpose(partition, k)
        assert isinstance(data, TransposeVerificationData)
        assert data.transpose == transpose
        assert transpose_partition(data.transpose) == data.partition
        assert simplify(data.formal_reflected_level + k + 2 * sum(partition)) == 0

    @pytest.mark.parametrize(
        ("partition", "central_sum"),
        [
            ((2, 1), 50),
            ((2, 2), 110),
            ((3, 1, 1), 212),
            ((3, 2, 1), 320),
        ],
    )
    def test_self_transpose_formal_central_sums(self, partition, central_sum):
        data = verify_transport_to_transpose(partition, k)
        assert data.is_self_transpose
        assert data.formal_central_sum_k_independent
        assert simplify(data.formal_central_sum - central_sum) == 0

    def test_bp_uses_the_standard_primary_normalization(self):
        data = verify_transport_to_transpose((2, 1), k)
        expected = -(2 * k + 3) * (3 * k + 1) / (k + 3)
        assert simplify(data.source_central_charge - expected) == 0
        assert simplify(data.formal_central_sum - 50) == 0

    @pytest.mark.parametrize(
        ("partition", "expected"),
        [
            ((3, 1), 44 - 18 * k),
            ((2, 1, 1), 188 + 18 * k),
            ((3, 2), 110 - 18 * k),
            ((2, 2, 1), 290 + 18 * k),
        ],
    )
    def test_nonselftranspose_formal_central_sums(self, partition, expected):
        data = verify_transport_to_transpose(partition, k)
        assert simplify(data.formal_central_sum - expected) == 0
        assert data.formal_central_sum_k_independent is False

    @pytest.mark.parametrize("partition", [(2, 1), (3, 1), (3, 2), (3, 2, 1)])
    def test_generator_and_diagnostic_fields_are_exact(self, partition):
        data = verify_transport_to_transpose(partition, k)
        assert data.source_n_generators == _centralizer_oracle(partition)
        assert data.transpose_n_generators == _centralizer_oracle(data.transpose)
        assert data.source_reciprocal_weight_diagnostic == _reciprocal_weight_oracle(
            partition
        )
        assert data.transpose_reciprocal_weight_diagnostic == _reciprocal_weight_oracle(
            data.transpose
        )

    @pytest.mark.parametrize("partition", [(2, 1), (3, 1), (3, 2), (3, 2, 1)])
    def test_hasse_path_is_finite_combinatorial_data(self, partition):
        data = verify_transport_to_transpose(partition, k)
        assert data.graph_reaches_transpose
        assert data.hasse_path_to_transpose[0] == data.partition
        assert data.hasse_path_to_transpose[-1] == data.transpose
        for left, right in zip(data.hasse_path_to_transpose, data.hasse_path_to_transpose[1:]):
            assert is_covering_relation(left, right) or is_covering_relation(right, left)

    @pytest.mark.parametrize("partition", [(2, 1), (3, 1), (3, 2), (3, 2, 1)])
    def test_object_level_fields_remain_typed(self, partition):
        data = verify_transport_to_transpose(partition, k)
        _assert_unresolved(data.source_rho, ClaimStatus.OPEN)
        _assert_unresolved(data.transpose_rho, ClaimStatus.OPEN)
        _assert_unresolved(data.source_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.transpose_kappa, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.modular_conductor, ClaimStatus.OPEN)
        _assert_unresolved(data.categorical_transport, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.bar_compatibility, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.koszul_duality, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.ksdual_membership, ClaimStatus.CONDITIONAL)

    @pytest.mark.parametrize(("n", "count"), [(4, 5), (5, 7), (6, 11)])
    def test_all_partition_profiles(self, n, count):
        profiles = verify_all_partitions_transport(n, k)
        assert len(profiles) == count
        assert all(profile.graph_reaches_transpose for profile in profiles.values())
        assert all(
            profile.koszul_duality.status is ClaimStatus.CONDITIONAL
            for profile in profiles.values()
        )


class TestSlodowyAndKoszulSurface:
    @pytest.mark.parametrize("partition", [(3,), (2, 1), (2, 2), (3, 2), (3, 2, 1)])
    def test_slodowy_dimension_and_generator_weights(self, partition):
        data = koszulness_certificate(partition)
        assert isinstance(data, KoszulnessData)
        assert data.slodowy_slice_dimension == _centralizer_oracle(partition)
        assert data.n_generators == _centralizer_oracle(partition)
        assert data.generator_weights == _matrix_weight_oracle(partition)
        assert data.n_even == data.n_generators
        assert data.n_odd == 0

    @pytest.mark.parametrize("partition", [(3,), (2, 1), (2, 2), (3, 2), (3, 2, 1)])
    def test_affine_geometry_and_typed_consequences(self, partition):
        data = koszulness_certificate(partition)
        assert data.slodowy_slice_is_affine_space
        assert data.arc_space_is_affine
        assert data.arc_space_affine
        _assert_unresolved(data.inverse_reduction, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.pbw_collapse, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.bar_comparison, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.koszulness, ClaimStatus.CONDITIONAL)
        _assert_unresolved(data.full_shadow_depth, ClaimStatus.OPEN)


class TestFiniteTransportGraph:
    @pytest.mark.parametrize(
        ("n", "partition_count", "edge_count"),
        [(3, 3, 2), (4, 5, 4), (5, 7, 6), (6, 11, 12), (7, 15, 17)],
    )
    def test_graph_census_and_reachability(self, n, partition_count, edge_count):
        graph = build_transport_graph(n)
        assert isinstance(graph, TransportGraph)
        assert len(graph.partitions) == partition_count
        assert len(graph.edges) == edge_count
        assert graph.combinatorial_full_reachability
        assert graph.full_reachability
        assert graph.reachable_from_hooks == frozenset(graph.partitions)

    def test_hook_vertices_sl4(self):
        graph = build_transport_graph(4)
        assert set(graph.hook_partitions) == {
            (4,), (3, 1), (2, 1, 1), (1, 1, 1, 1)
        }

    @pytest.mark.parametrize("n", [3, 4, 5, 6])
    def test_graph_reachability_and_categorical_transport_have_distinct_types(self, n):
        graph = build_transport_graph(n)
        assert graph.combinatorial_full_reachability
        _assert_unresolved(graph.inverse_reduction_surface, ClaimStatus.CONDITIONAL)
        _assert_unresolved(graph.categorical_transport, ClaimStatus.CONDITIONAL)
        assert all(edge.inverse_reduction.status is ClaimStatus.CONDITIONAL for edge in graph.edges)


class TestFormalCentralScalarSurface:
    def test_compatibility_name_matches_explicit_name(self):
        for partition in ((2, 1), (2, 2), (3, 1), (3, 2)):
            assert simplify(
                central_charge_conductor(partition, k)
                - formal_central_scalar_sum(partition, k)
            ) == 0

    @pytest.mark.parametrize(
        ("partition", "expected"),
        [
            ((2, 1), 50),
            ((2, 2), 110),
            ((3, 1, 1), 212),
            ((3, 2, 1), 320),
            ((3, 1), 44 - 18 * k),
            ((3, 2), 110 - 18 * k),
        ],
    )
    def test_exact_formal_sums(self, partition, expected):
        assert simplify(formal_central_scalar_sum(partition, k) - expected) == 0

    def test_catalog_cardinality(self):
        catalog = central_charge_conductor_catalog(6, k)
        assert len(catalog) == 3 + 5 + 7 + 11
        assert simplify(catalog[(2, 1)] - 50) == 0
        assert simplify(catalog[(3, 2, 1)] - 320) == 0


class TestAnomalyAndCY3Typing:
    def test_anomaly_catalog_contains_open_packets(self):
        catalog = anomaly_ratio_catalog(6)
        expected_count = sum(len(tuple(_partitions_of_n(n))) - 1 for n in range(2, 7))
        assert len(catalog) == expected_count
        assert all(packet.status is ClaimStatus.OPEN for packet in catalog.values())
        assert all(packet.value is None for packet in catalog.values())

    def test_transpose_relation_separates_diagnostics_from_rho(self):
        relation = anomaly_ratio_transpose_relation((3, 1))
        assert relation["transpose"] == (2, 1, 1)
        assert relation["source_reciprocal_weight_diagnostic"] == Rational(17, 6)
        assert relation["transpose_reciprocal_weight_diagnostic"] == Rational(43, 6)
        _assert_unresolved(relation["source_rho"], ClaimStatus.OPEN)
        _assert_unresolved(relation["transpose_rho"], ClaimStatus.OPEN)
        _assert_unresolved(relation["rho_comparison"], ClaimStatus.OPEN)
        _assert_unresolved(relation["modular_conductor"], ClaimStatus.OPEN)

    def test_cy3_catalog_records_construction_and_frontier_separately(self):
        candidates = cy3_candidate_catalog()
        assert len(candidates) == 4
        assert all(isinstance(candidate, CY3VertexAlgebraCandidate) for candidate in candidates)
        for candidate in candidates:
            assert candidate.construction.status is ClaimStatus.PROVED_ELSEWHERE
            assert candidate.construction.require_value() is True
            assert any("2312.03648" in item for item in candidate.construction.evidence)
            _assert_unresolved(candidate.identification, ClaimStatus.OPEN)
            _assert_unresolved(candidate.free_generation, ClaimStatus.OPEN)
            _assert_unresolved(candidate.modular_characteristic, ClaimStatus.OPEN)
            _assert_unresolved(candidate.koszulness, ClaimStatus.CONDITIONAL)


class TestButsonSummary:
    @pytest.mark.parametrize(
        ("n", "partitions", "edges", "hook_edges", "nonhook_edges"),
        [(3, 3, 2, 2, 0), (4, 5, 4, 2, 2), (5, 7, 6, 2, 4), (6, 11, 12, 2, 10)],
    )
    def test_exact_summary_census(self, n, partitions, edges, hook_edges, nonhook_edges):
        summary = butson_analysis(n, k)
        assert isinstance(summary, ButsonAnalysisSummary)
        assert summary.total_partitions == partitions
        assert summary.total_edges == edges
        assert summary.hook_edges == hook_edges
        assert summary.non_hook_edges == nonhook_edges
        assert summary.combinatorial_full_reachability
        assert summary.all_edges_are_positive_coroot_steps
        assert summary.self_transpose_central_sums_constant

    @pytest.mark.parametrize("n", [3, 4, 5, 6])
    def test_summary_consequences_are_conditional(self, n):
        summary = butson_analysis(n, k)
        _assert_unresolved(summary.inverse_reduction_surface, ClaimStatus.CONDITIONAL)
        _assert_unresolved(summary.bar_compatibility, ClaimStatus.CONDITIONAL)
        _assert_unresolved(summary.pbw_collapse, ClaimStatus.CONDITIONAL)
        _assert_unresolved(summary.koszulness, ClaimStatus.CONDITIONAL)
        _assert_unresolved(summary.categorical_transport, ClaimStatus.CONDITIONAL)
        _assert_unresolved(summary.transpose_duality, ClaimStatus.CONDITIONAL)


def test_source_excludes_legacy_promotions():
    source = Path("compute/lib/theorem_butson_inverse_reduction_engine.py").read_text()
    fragments = (
        "def _kappa_for_partition",
        "pbw_collapse=" + "True",
        "koszul_at_generic_level=" + "True",
        "all_koszul_at_generic",
        "shadow_class",
        "kappa_sum_simplified",
        "bp_central_charge",
        "rho_src + rho_dual",
        "complete bidirectional transport",
    )
    assert all(source.find(fragment) == -1 for fragment in fragments)
