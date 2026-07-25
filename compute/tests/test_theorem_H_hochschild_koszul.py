"""Typed checks for the family-indexed Theorem-H compute surface.

The executable facts in this file are the two bounded calculations of
Bakalov--De Sole--Kac and elementary Lie arithmetic.  A completed
curve-level chiral Hochschild group appears only after a named
bounded-to-chart quasi-isomorphism or a complete family datum
``H_H(A; S)``.  Koszul-dual perfectness is a further, independent input.
"""

from __future__ import annotations

from compute.lib.chiral_hochschild_engine import (
    BoundedToChartComparison,
    KoszulDualityDatum,
    center_dimension_koszul_dual,
    compute_chirhoch,
    heisenberg_data,
    koszul_duality_check as chart_koszul_duality_check,
    virasoro_data,
)
from compute.lib.chirhoch_dimension_engine import (
    chirhoch_affine_km,
    chirhoch_heisenberg,
    chirhoch_virasoro,
    dim_simple_lie_algebra,
    koszul_duality_check as dimension_koszul_duality_check,
)


class TestBoundedBDSKBenchmarks:
    def test_rank_one_even_superboson_vector(self):
        row = chirhoch_heisenberg()
        assert row.bounded_support == (0, 1)
        assert row.bounded_dimensions == {0: 2, 1: 1}
        assert row.bounded_prefix(5) == (2, 1, 0, 0, 0, 0)
        assert row.chart_support is None
        assert row.chart_dimensions is None
        assert row.hilbert_triple is None

    def test_virasoro_vector(self):
        row = chirhoch_virasoro()
        assert row.bounded_support == (0, 2, 3)
        assert row.bounded_dimensions == {0: 1, 2: 1, 3: 1}
        assert row.bounded_prefix(5) == (1, 0, 1, 1, 0, 0)
        assert row.chart_support is None
        assert row.chart_dimensions is None
        assert row.hilbert_triple is None


class TestAffineArithmeticAndOpenQuotient:
    def test_zero_modes_supply_inner_subspace_metadata(self):
        for name, expected in (("sl_2", 3), ("sl_3", 8), ("G2", 14)):
            row = chirhoch_affine_km(name)
            assert dim_simple_lie_algebra(name) == expected
            assert row.prequotient_dimension == expected
            assert row.known_inner_zero_mode_dimension == expected
            assert row.dim1 is None
            assert row.chart_dimensions is None
            assert row.chart_status == "open-family-support-datum"


class TestChartTransport:
    def test_default_heisenberg_chart_fields_are_open(self):
        result = compute_chirhoch(heisenberg_data(k=1))
        assert result.bounded_benchmark is not None
        assert result.bounded_benchmark.vector == (2, 1)
        assert result.support is None
        assert result.dimensions is None
        assert result.poincare_polynomial is None
        assert result.status == "open-family-support-datum"

    def test_open_bounded_map_withholds_chart_dimensions(self):
        data = heisenberg_data(k=1)
        benchmark = compute_chirhoch(data).bounded_benchmark
        assert benchmark is not None
        comparison = BoundedToChartComparison(
            family=data.name,
            map_name="gamma_H",
            source_complex=benchmark.complex_name,
            target_complex="Q_H",
            quasi_isomorphism_status="open",
        )
        result = compute_chirhoch(data, bounded_to_chart=comparison)
        assert result.support is None
        assert result.dimensions is None
        assert result.status == "open-bounded-to-chart-comparison"

class TestDualityRequiresItsOwnMap:
    def test_parameter_pair_supplies_no_betti_comparison(self):
        relation = chart_koszul_duality_check(
            heisenberg_data(k=1), heisenberg_data(k=-1)
        )
        assert relation.betti_A is None
        assert relation.betti_A_dual is None
        assert relation.relation_satisfied is None
        assert relation.status == "open-perfect-pairing-and-chart-comparison"

        bounded_relation = dimension_koszul_duality_check(
            chirhoch_virasoro(), chirhoch_virasoro()
        )
        assert bounded_relation is None

    def test_pairing_datum_alone_supplies_no_degree_two_number(self):
        data = heisenberg_data(k=1)
        pairing = KoszulDualityDatum(
            family=data.name,
            dual_family="curved second-kind Heisenberg dual",
            pairing_map="q_H",
            cohomological_shift=2,
            perfectness_status="open",
        )
        assert center_dimension_koszul_dual(data, duality_datum=pairing) is None

    def test_virasoro_support_retains_degree_three(self):
        result = compute_chirhoch(virasoro_data(c=26))
        assert result.bounded_benchmark is not None
        assert result.bounded_benchmark.support == (0, 2, 3)
        assert result.support is None
        assert result.w_hochschild is not None
        assert result.w_hochschild.amplitude is None
