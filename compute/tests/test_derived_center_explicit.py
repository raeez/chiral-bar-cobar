"""Exact-arithmetic and open-map guards for ``derived_center_explicit``."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import pytest

from compute.lib.derived_center_explicit import (
    AnnulusTrace,
    BulkBoundaryMaps,
    CHAIN_MODEL_OBLIGATION,
    DeformationQuantization,
    DerivedCenterStructureMaps,
    FAMILIES,
    HochschildCocycleEnumerator,
    OpenChainOperation,
    OpenClosedMCElement,
    _composition_count,
    _partition_count,
    affine_sl2_hh_at_levels,
    affine_sl2_hh_dimensions,
    chiral_hkr_dimension,
    full_derived_center_package,
    generator_weights,
    heisenberg_bounded_benchmark,
    heisenberg_hh_cocycles,
    kappa,
    morita_invariance_check,
    num_generators,
    verify_complementarity,
    verify_kappa_additivity,
    virasoro_bounded_benchmark,
    virasoro_hh2_weight_graded,
)


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "compute/lib/derived_center_explicit.py"


class TestExactScalarArithmetic:
    @pytest.mark.parametrize(
        ("level", "expected"),
        [(1, Fraction(1)), (2, Fraction(2)), (Fraction(1, 2), Fraction(1, 2))],
    )
    def test_heisenberg_kappa(self, level, expected):
        assert kappa("Heisenberg", k=level) == expected

    @pytest.mark.parametrize(
        ("level", "expected"),
        [(1, Fraction(9, 4)), (2, Fraction(3)), (3, Fraction(15, 4))],
    )
    def test_affine_sl2_kappa(self, level, expected):
        assert kappa("Affine_sl2", k=level) == expected

    @pytest.mark.parametrize(
        ("charge", "expected"),
        [(0, Fraction(0)), (1, Fraction(1, 2)), (13, Fraction(13, 2)), (26, Fraction(13))],
    )
    def test_virasoro_kappa(self, charge, expected):
        assert kappa("Virasoro", c=charge) == expected

    def test_w3_scalar_formula(self):
        assert kappa("W3", c=2) == Fraction(5, 3)
        assert kappa("W3", c=26) == Fraction(65, 3)

    def test_generator_weights(self):
        expected = {
            "Heisenberg": [1],
            "Affine_sl2": [1, 1, 1],
            "Virasoro": [2],
            "W3": [2, 3],
        }
        for family, weights in expected.items():
            assert generator_weights(family) == weights
            assert num_generators(family) == len(weights)


class TestFiniteCombinatorics:
    @pytest.mark.parametrize(
        ("weights", "target", "expected"),
        [([1], 4, 1), ([1, 2], 4, 3), ([2, 3], 7, 1), ([2, 3], 1, 0)],
    )
    def test_partition_counts(self, weights, target, expected):
        assert _partition_count(weights, target) == expected

    @pytest.mark.parametrize(
        ("n_vars", "total", "expected"),
        [(1, 5, 1), (2, 4, 5), (3, 2, 6), (4, 0, 1)],
    )
    def test_weak_composition_counts(self, n_vars, total, expected):
        assert _composition_count(n_vars, total) == expected

    def test_generator_ansatz_count_is_explicitly_precohomological(self):
        heis = HochschildCocycleEnumerator("Heisenberg", weight_bound=4)
        sl2 = HochschildCocycleEnumerator("Affine_sl2", weight_bound=4)
        assert heis.candidate_dimension(1, 0) == 1
        assert sl2.candidate_dimension(1, 0) == 9
        assert "distinct from" in HochschildCocycleEnumerator.__doc__


class TestBoundedAndChartSeparation:
    def test_superboson_bounded_vector(self):
        benchmark = heisenberg_bounded_benchmark()
        assert benchmark.support == (0, 1)
        assert benchmark.dimensions == {0: 2, 1: 1}
        assert benchmark.vector == (2, 1)
        assert benchmark.prefix(5) == (2, 1, 0, 0, 0, 0)

    def test_virasoro_bounded_support(self):
        benchmark = virasoro_bounded_benchmark()
        assert benchmark.support == (0, 2, 3)
        assert benchmark.dimensions == {0: 1, 2: 1, 3: 1}
        assert benchmark.vector == (1, 0, 1, 1)

    def test_heisenberg_chart_and_weight_split_are_open(self):
        status = heisenberg_hh_cocycles(max_weight=7)
        assert status.bounded_benchmark == heisenberg_bounded_benchmark()
        assert status.chart_support is None
        assert status.chart_dimensions is None
        assert status.conformal_weight_dimensions is None

    def test_virasoro_weight_graded_h2_is_open(self):
        status = virasoro_hh2_weight_graded(max_weight=9)
        assert status.bounded_benchmark == virasoro_bounded_benchmark()
        assert status.chart_support is None
        assert status.conformal_weight_dimensions is None

    @pytest.mark.parametrize("level", [1, 2, 3])
    def test_affine_chart_dimensions_are_open(self, level):
        status = affine_sl2_hh_dimensions(level)
        assert status.bounded_benchmark is None
        assert status.chart_dimensions is None
        assert status.chart_support is None

    def test_affine_level_table_contains_status_packets(self):
        table = affine_sl2_hh_at_levels()
        assert set(table) == {1, 2, 3}
        assert all(packet.chart_dimensions is None for packet in table.values())

    def test_affine_critical_level_has_separate_scope(self):
        with pytest.raises(ValueError, match="critical"):
            affine_sl2_hh_dimensions(-2)


class TestDerivedCentreOperations:
    @pytest.fixture
    def maps(self):
        return DerivedCenterStructureMaps("Heisenberg", k=2)

    @pytest.mark.parametrize(
        "operation",
        [
            lambda maps: maps.product("x", "y"),
            lambda maps: maps.gerstenhaber_bracket("x", "y"),
            lambda maps: maps.bv_operator("x"),
        ],
    )
    def test_chain_operations_are_open(self, maps, operation):
        packet = operation(maps)
        assert isinstance(packet, OpenChainOperation)
        assert packet.value is None
        assert packet.status == "open-explicit-chain-map"
        assert packet.resolution_obligation == CHAIN_MODEL_OBLIGATION

    def test_bv_relation_is_open(self, maps):
        packet = maps.verify_bv_relation("x", "y")
        assert packet["match"] is None

    def test_scalar_kappa_is_separate_from_operations(self, maps):
        assert maps.scalar_kappa == 2
        assert maps.product("x", "y").value is None


class TestAnnulusAndOpenClosedMaps:
    def test_annulus_trace_values_are_open(self):
        trace = AnnulusTrace("Virasoro", c=26)
        assert trace.scalar_kappa == 13
        assert trace.trace_on_identity().value is None
        assert trace.trace_on_hh1().value is None
        assert trace.trace_on_hh2().value is None

    def test_scalar_complement_does_not_construct_annulus_map(self):
        report = AnnulusTrace("Virasoro", c=7).verify_modularity()
        assert report["scalar_diagnostic"]["scalar_identity"] is True
        assert report["trace_equals_kappa"] is None

    def test_open_closed_components_and_mc_equation_are_open(self):
        element = OpenClosedMCElement("Heisenberg", k=1)
        assert element.theta_oc(1, 1).value is None
        report = element.verify_mc_equation(1, 1)
        assert report["MC_value"] is None
        assert report["MC_satisfied"] is None

    def test_bulk_boundary_maps_are_open(self):
        maps = BulkBoundaryMaps("Heisenberg", k=1)
        assert maps.restriction("vac").value is None
        assert maps.annulus_map("vac").value is None
        assert maps.composition_a_r("vac").value is None
        assert maps.verify_composition()["composition_equals_kappa_identity"] is None


class TestQuantizationAndMoritaScope:
    @pytest.mark.parametrize("weight", range(0, 8))
    def test_auxiliary_weyl_pbw_count(self, weight):
        quantization = DeformationQuantization("Heisenberg", k=1)
        expected = len([(a, weight - a) for a in range(weight + 1)])
        assert quantization.weyl_algebra_dimension(weight) == expected

    def test_weyl_comparison_to_derived_centre_is_open(self):
        quantization = DeformationQuantization("Heisenberg", k=1)
        assert quantization.classical_poisson_bracket("x", "p").value is None
        assert quantization.quantum_commutator("x", "p").value is None
        assert quantization.verify_quantization()["comparison"] is None

    @pytest.mark.parametrize("family", FAMILIES)
    def test_chiral_morita_comparison_is_open(self, family):
        report = morita_invariance_check(family, 2)
        assert report["HH_A"] is None
        assert report["HH_Mat_n_A"] is None
        assert report["morita_invariant"] is None

    @pytest.mark.parametrize("family", FAMILIES)
    def test_chiral_hkr_dimensions_are_withheld(self, family):
        for degree in range(5):
            assert chiral_hkr_dimension(family, degree) is None


class TestScalarInvolutions:
    @pytest.mark.parametrize(
        ("family", "params", "expected_sum"),
        [
            ("Heisenberg", {"k": 3}, Fraction(0)),
            ("Affine_sl2", {"k": 5}, Fraction(0)),
            ("Virasoro", {"c": 7}, Fraction(13)),
        ],
    )
    def test_exact_scalar_identity_and_open_duality(self, family, params, expected_sum):
        report = verify_complementarity(family, **params)
        assert report["sum"] == expected_sum
        assert report["scalar_identity"] is True
        assert report["chiral_duality"] is None

    def test_scalar_addition(self):
        report = verify_kappa_additivity(
            [("Heisenberg", {"k": 1}), ("Virasoro", {"c": 1})]
        )
        assert report["kappas"] == [Fraction(1), Fraction(1, 2)]
        assert report["sum"] == Fraction(3, 2)


class TestFullPackage:
    @pytest.mark.parametrize("family", FAMILIES)
    def test_package_preserves_arithmetic_and_withholds_chain_data(self, family):
        package = full_derived_center_package(family)
        assert package["kappa"] == kappa(family)
        assert package["generator_weights"] == generator_weights(family)
        assert package["HH_dimensions"] is None
        assert package["HH_support"] is None
        assert package["cup_product"] is None
        assert package["Gerstenhaber_bracket"] is None
        assert package["BV_operator"] is None
        assert package["annulus_trace_identity"] is None
        assert package["open_closed_MC"] is None
        assert package["morita_invariant_n2"] is None

    def test_bounded_benchmarks_appear_only_on_supported_rows(self):
        assert full_derived_center_package("Heisenberg")["bounded_benchmark"] is not None
        assert full_derived_center_package("Virasoro")["bounded_benchmark"] is not None
        assert full_derived_center_package("Affine_sl2")["bounded_benchmark"] is None
        assert full_derived_center_package("W3")["bounded_benchmark"] is None

    def test_retired_bureaucratic_stem_is_absent(self):
        assert ("cert" + "if") not in ENGINE.read_text(encoding="utf-8").lower()
