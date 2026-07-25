r"""Independent checks for the family-indexed Theorem-H engine.

The numerical oracles in this file use binomial coefficients directly.
They therefore test the implementation independently of its shared exterior-
power helper.  Bounded vertex calculations, completed chart calculations,
and perfect pairings occupy separate test surfaces.
"""

from math import comb

import pytest

from compute.lib.theorem_h_hochschild_polynomial import (
    AffineExteriorBound,
    BoundedToChartComparison,
    CohomologyAmbient,
    FAMILY_DATA,
    FamilySupportDatum,
    PerfectDegreePairing,
    affine_bounded_upper_bound,
    affine_slN_data,
    bar_complex_betti_abelian,
    bar_complex_betti_sl2,
    bounded_betti,
    bounded_poincare,
    cohomology_record,
    exterior_algebra_verification,
    exterior_two_term_dimension,
    generator_count,
    hochschild_betti,
    hochschild_euler_char,
    hochschild_poincare,
    hochschild_total_dim,
    koszul_dual_polynomial,
    superboson_bounded_dimension,
    theorem_h_scope_record,
    verify_palindromicity,
    verify_theorem_h,
    virasoro_bounded_dimension,
    virasoro_hochschild_dims,
    w3_hochschild_dims,
    wN_data,
)


def exterior_oracle(rank: int, degree: int) -> int:
    """Independent dimension of Lambda^n V plus Lambda^(n+1) V."""

    if degree < 0:
        return 0
    first = comb(rank, degree) if degree <= rank else 0
    second = comb(rank, degree + 1) if degree + 1 <= rank else 0
    return first + second


def comparison_for(record, status: str = "assumed") -> BoundedToChartComparison:
    return BoundedToChartComparison(
        family=record.key,
        map_name=f"chi_bd_{record.key}",
        source_complex=record.bounded.complex_name,
        target_complex=f"Q_{record.key}",
        quasi_isomorphism_status=status,
    )


def family_datum_for(record, dimensions=None, status: str = "assumed"):
    support = (0, 4) if dimensions is None else tuple(dimensions)
    return FamilySupportDatum(
        family=record.key,
        support=support,
        complete_chart_complex=f"Q_{record.key}",
        chart_comparison_map=f"gamma_{record.key}",
        support_model=f"K_{record.key}_S",
        inclusion=f"i_{record.key}",
        projection=f"p_{record.key}",
        contracting_homotopy=f"h_{record.key}",
        incidence_and_bar_face_compatibility=f"eta_{record.key}",
        completion_and_averaging_map=f"mu_{record.key}",
        model_dimensions=dimensions,
        status=status,
    )


class TestExteriorPowerOracle:
    @pytest.mark.parametrize("rank", range(0, 8))
    @pytest.mark.parametrize("degree", range(-1, 10))
    def test_shared_formula_matches_independent_binomial_oracle(self, rank, degree):
        expected = exterior_oracle(rank, degree)
        assert exterior_two_term_dimension(rank, degree) == expected
        assert superboson_bounded_dimension(rank, degree) == expected
        assert affine_bounded_upper_bound(rank, degree) == expected

    def test_rank_zero_limit(self):
        assert [superboson_bounded_dimension(0, n) for n in range(4)] == [1, 0, 0, 0]
        record = cohomology_record("superboson", rank=0)
        assert record.bounded.vector == (1,)
        assert record.bounded.support == (0,)

    def test_rank_one_limit_is_bdsk_vector(self):
        assert [superboson_bounded_dimension(1, n) for n in range(5)] == [2, 1, 0, 0, 0]
        assert bounded_poincare("heisenberg") == [2, 1]
        assert [bounded_betti("heisenberg", n) for n in range(5)] == [2, 1, 0, 0, 0]

    def test_rank_four_exterior_profile(self):
        expected = [5, 10, 10, 5, 1, 0]
        assert [superboson_bounded_dimension(4, n) for n in range(6)] == expected
        record = cohomology_record("superboson", rank=4)
        assert record.bounded.vector == tuple(expected[:-1])


class TestExplicitBDSKRows:
    def test_superboson_ambient_and_source(self):
        row = cohomology_record("heisenberg")
        assert row.bounded.ambient is CohomologyAmbient.BOUNDED_VERTEX
        assert row.bounded.support == (0, 1)
        assert dict(row.bounded.dimensions) == {0: 2, 1: 1}
        assert "Theorem 7.4" in row.bounded.source
        assert row.chart.ambient is CohomologyAmbient.COMPLETED_CURVE_CHART
        assert row.chart.dimensions is None

    def test_virasoro_bounded_row_retains_degree_three(self):
        expected = [1, 0, 1, 1, 0, 0]
        assert [virasoro_bounded_dimension(n) for n in range(6)] == expected
        row = cohomology_record("virasoro")
        assert row.bounded.support == (0, 2, 3)
        assert row.bounded.vector == (1, 0, 1, 1)
        assert row.bounded.total_dimension == 3
        assert row.bounded.euler_characteristic == 1
        assert "Theorem 7.2" in row.bounded.source

    def test_standard_mapping_carries_records(self):
        assert FAMILY_DATA["heisenberg"].regime == "family_indexed_support"
        assert FAMILY_DATA["heisenberg"]["poincare"] is None
        assert FAMILY_DATA["virasoro"].bounded.vector == (1, 0, 1, 1)


class TestChartTransportTransitions:
    def test_default_chart_is_open(self):
        row = cohomology_record("heisenberg")
        assert row.chart.support is None
        assert row.chart.dimensions is None
        assert row.chart.status == "open-family-support-datum"
        assert hochschild_poincare("heisenberg") is None
        assert hochschild_betti("heisenberg", 0) is None
        assert hochschild_total_dim("heisenberg") is None
        assert hochschild_euler_char("heisenberg") is None

    def test_named_open_comparison_preserves_open_chart(self):
        base = cohomology_record("heisenberg")
        comparison = comparison_for(base, "open")
        row = cohomology_record("heisenberg", comparison=comparison)
        assert row.comparison == comparison
        assert row.chart.dimensions is None
        assert row.chart.status == "open-bounded-to-chart-comparison"

    @pytest.mark.parametrize("status", ["assumed", "proved-elsewhere"])
    def test_transport_status_carries_bounded_vector_to_chart(self, status):
        base = cohomology_record("heisenberg")
        comparison = comparison_for(base, status)
        row = cohomology_record("heisenberg", comparison=comparison)
        assert row.chart.support == (0, 1)
        assert row.chart.vector == (2, 1)
        assert row.chart.ambient is CohomologyAmbient.COMPLETED_CURVE_CHART
        assert status in row.chart.status
        assert hochschild_poincare("heisenberg", comparison=comparison) == [2, 1]
        assert hochschild_total_dim("heisenberg", comparison=comparison) == 3
        assert hochschild_euler_char("heisenberg", comparison=comparison) == 1

    def test_virasoro_transport_preserves_degree_three(self):
        base = cohomology_record("virasoro")
        comparison = comparison_for(base, "proved-elsewhere")
        assert hochschild_poincare("virasoro", comparison=comparison) == [1, 0, 1, 1]
        assert hochschild_betti("virasoro", 3, comparison=comparison) == 1
        assert virasoro_hochschild_dims(5, comparison=comparison) == [1, 0, 1, 1, 0, 0]

    def test_family_datum_supplies_support_and_dimensions(self):
        base = cohomology_record("w3")
        datum = family_datum_for(base, {0: 2, 4: 1})
        row = cohomology_record("w3", family_datum=datum)
        assert row.chart.support == (0, 4)
        assert dict(row.chart.dimensions) == {0: 2, 4: 1}
        assert hochschild_poincare("w3", family_datum=datum) == [2, 0, 0, 0, 1]
        assert w3_hochschild_dims(5, family_datum=datum) == [2, 0, 0, 0, 1, 0]

    def test_family_datum_can_determine_support_before_dimensions(self):
        base = cohomology_record("w3")
        datum = family_datum_for(base)
        row = cohomology_record("w3", family_datum=datum)
        assert row.chart.support == (0, 4)
        assert row.chart.dimension(1) == 0
        assert row.chart.dimension(0) is None
        assert row.chart.dimension(4) is None

    def test_comparison_family_and_source_are_typed(self):
        base = cohomology_record("heisenberg")
        foreign = BoundedToChartComparison(
            family="virasoro",
            map_name="chi",
            source_complex=base.bounded.complex_name,
            target_complex="Q",
            quasi_isomorphism_status="assumed",
        )
        with pytest.raises(ValueError, match="comparison family"):
            cohomology_record("heisenberg", comparison=foreign)


class TestAffineConjecturalBounds:
    def test_sl2_bound_is_exterior_oracle(self):
        row = affine_slN_data(2)
        bound = row.bounded_affine_bound
        assert isinstance(bound, AffineExteriorBound)
        assert bound.ambient is CohomologyAmbient.BOUNDED_VERTEX
        assert bound.status == "conjectural-BDSK-Conjecture-7.5-bound"
        assert bound.prefix(5) == tuple(exterior_oracle(3, n) for n in range(6))
        assert bound.prefix(5) == (4, 6, 4, 1, 0, 0)
        assert row.chart.dimensions is None

    def test_sl3_bound_uses_dim_sl3_eight(self):
        row = affine_slN_data(3)
        assert row.metadata["lie_dimension"] == 8
        assert row.metadata["known_inner_zero_mode_dimension"] == 8
        assert row.bounded_affine_bound.prefix(4) == tuple(
            exterior_oracle(8, n) for n in range(5)
        )

    def test_comparison_transports_bound_and_preserves_conjectural_status(self):
        base = affine_slN_data(2)
        comparison = comparison_for(base, "assumed")
        row = affine_slN_data(2, comparison=comparison)
        assert row.chart_affine_bound is not None
        assert row.chart_affine_bound.ambient is CohomologyAmbient.COMPLETED_CURVE_CHART
        assert "conjectural-BDSK-Conjecture-7.5" in row.chart_affine_bound.status
        assert row.chart_affine_bound.prefix(4) == (4, 6, 4, 1, 0)
        assert row.chart.dimensions is None


class TestOpenStandardFamilies:
    @pytest.mark.parametrize(
        "family,params",
        [
            ("betagamma", {}),
            ("bc_ghosts", {}),
            ("w3", {}),
            ("wN", {"N": 5}),
            ("lattice", {"rank": 24}),
        ],
    )
    def test_family_rows_await_explicit_support_data(self, family, params):
        row = cohomology_record(family, **params)
        assert row.chart.dimensions is None
        assert row.chart.support is None
        assert row.chart.status == "open-family-support-datum"

    def test_generator_metadata_remains_exact(self):
        assert generator_count("heisenberg") == 1
        assert generator_count("virasoro") == 1
        assert generator_count("affine_sl2") == 3
        assert generator_count("affine_sl3") == 8
        assert generator_count("wN", N=5) == 4
        assert wN_data(5).generator_weights == (2, 3, 4, 5)


class TestPairingSeparation:
    def test_pairing_alone_supplies_no_chart_dimensions(self):
        base = cohomology_record("heisenberg")
        pairing = PerfectDegreePairing(
            family=base.key,
            dual_family="curved_heisenberg_dual",
            pairing_map="q_H",
            cohomological_degree=2,
            perfectness_status="assumed",
        )
        row = cohomology_record("heisenberg", perfect_pairing=pairing)
        assert row.perfect_pairing == pairing
        assert row.chart.dimensions is None
        assert koszul_dual_polynomial("heisenberg", perfect_pairing=pairing) is None

    def test_pairing_and_chart_data_enable_a_separate_palindromicity_check(self):
        base = cohomology_record("w3")
        datum = family_datum_for(base, {0: 1, 2: 1})
        pairing = PerfectDegreePairing(
            family=base.key,
            dual_family=base.key,
            pairing_map="q_W3",
            cohomological_degree=2,
            perfectness_status="assumed",
        )
        result = verify_palindromicity(
            "w3", family_datum=datum, perfect_pairing=pairing
        )
        assert result["passed"] is True
        assert koszul_dual_polynomial(
            "w3", family_datum=datum, perfect_pairing=pairing
        ) == [1, 0, 1]

    def test_dual_family_comparison_uses_its_chart_dimensions(self):
        base = cohomology_record("w3")
        datum = family_datum_for(base, {0: 2, 2: 1})
        pairing = PerfectDegreePairing(
            family=base.key,
            dual_family="w3_dual_level",
            pairing_map="q_W3_dual",
            cohomological_degree=2,
            perfectness_status="assumed",
        )
        open_result = verify_palindromicity(
            "w3", family_datum=datum, perfect_pairing=pairing
        )
        assert open_result["passed"] is None

        compared = verify_palindromicity(
            "w3",
            family_datum=datum,
            perfect_pairing=pairing,
            dual_chart_dimensions={0: 1, 2: 2},
        )
        assert compared["passed"] is True
        assert compared["degree_reflection_checks"] == {0: True, 2: True}


class TestScopeAndCompatibility:
    def test_scope_statement_is_family_indexed(self):
        scope = theorem_h_scope_record("virasoro")
        assert scope["claim"] == "H_H(A;S) implies Supp ChirHoch(A) subset S"
        assert scope["chart_ambient"] == "completed_curve_chart"
        assert scope["support"] is None
        assert scope["dimensions"] is None

    def test_verification_tracks_supplied_chart_data(self):
        open_result = verify_theorem_h("heisenberg")
        assert open_result["passed"] is None
        base = cohomology_record("heisenberg")
        transported = verify_theorem_h(
            "heisenberg", comparison=comparison_for(base)
        )
        assert transported["passed"] is True
        assert transported["chart"].vector == (2, 1)

    def test_exterior_verification_uses_bounded_ambient(self):
        result = exterior_algebra_verification("superboson", rank=5)
        assert result["ambient"] == "bounded_vertex_complex"
        assert result["passed"] is True

    def test_exact_ce_rows_keep_chart_fields_open(self):
        abelian = bar_complex_betti_abelian(rank=1, max_n=4)
        assert abelian["ce_dimensions"] == {0: 1, 1: 1}
        assert abelian["bounded_vertex_prefix"] == (2, 1, 0, 0, 0)
        assert abelian["chart_dimensions"] is None

        sl2 = bar_complex_betti_sl2()
        assert sl2["ce_cohomology"] == {0: 1, 1: 0, 2: 0, 3: 1}
        assert sl2["bounded_affine_upper_bound"] == (4, 6, 4, 1, 0)
        assert sl2["chart_dimensions"] is None
