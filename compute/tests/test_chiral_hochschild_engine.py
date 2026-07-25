"""Independent guards for the typed chiral-Hochschild audit surface."""

from __future__ import annotations

from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.chiral_hochschild_engine import (
    BOUNDED_TO_CHART_OBLIGATION,
    THEOREM_H_REQUIRED_COMPONENTS,
    BoundedToChartComparison,
    FamilySupportDatum,
    KoszulDualityDatum,
    OpenChirHochComputation,
    _ope_derivation_check_heisenberg,
    _ope_derivation_check_virasoro,
    _ope_derivation_check_w3,
    affine_sl2_data,
    affine_sl3_data,
    affine_slN_data,
    all_deformations_unobstructed,
    bar_koszul_derived_center_firewall,
    bc_ghosts_data,
    betagamma_data,
    bounded_cohomology_benchmark,
    center_dimension,
    center_dimension_koszul_dual,
    compute_all_standard_families,
    compute_chirhoch,
    compute_hochschild_polynomial,
    compute_w_algebra_hochschild,
    deformation_obstruction_analysis,
    derivation_analysis,
    ff_involution_on_hochschild,
    free_fermion_data,
    hochschild_spectral_sequence_E2,
    holographic_package_entries,
    koszul_duality_check,
    modular_koszul_primary_projections,
    summary_table,
    verify_km_h1_equals_dim_g,
    verify_theorem_h_complete,
    verify_universal_polynomial,
    virasoro_data,
    w3_data,
    wN_data,
    whitehead_lemma_check,
    heisenberg_data,
)


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "compute/lib/chiral_hochschild_engine.py"


def _comparison(data, status="assumed"):
    benchmark = bounded_cohomology_benchmark(data)
    assert benchmark is not None
    return BoundedToChartComparison(
        family=data.name,
        map_name=f"chi_bd_{data.name}",
        source_complex=benchmark.complex_name,
        target_complex=f"Q_{data.name}",
        quasi_isomorphism_status=status,
    )


def _family_datum(family: str) -> FamilySupportDatum:
    return FamilySupportDatum(
        family=family,
        support=(-1, 2, 5),
        complete_chart_complex=f"Q_{family}",
        chart_comparison_map=f"gamma_{family}",
        support_model=f"K_{family},S",
        inclusion=f"i_{family}",
        projection=f"p_{family}",
        contracting_homotopy=f"h_{family}",
        incidence_and_bar_face_compatibility=f"incidence_{family}",
        completion_and_averaging_map=f"mu_{family}",
        model_dimensions={-1: 3, 2: 4, 5: 1},
    )


class TestExactFamilyArithmetic:
    @pytest.mark.parametrize("N", range(2, 9))
    def test_type_a_dimension_and_generator_count(self, N):
        data = affine_slN_data(N)
        assert data.lie_dim == N * N - 1
        assert data.n_generators == N * N - 1
        assert data.gen_weights == (1,) * (N * N - 1)
        assert data.dual_coxeter() == N

    @pytest.mark.parametrize(
        ("N", "level", "expected"),
        [(2, 1, Rational(1)), (3, 2, Rational(16, 5)), (4, 3, Rational(45, 7))],
    )
    def test_sugawara_central_charge(self, N, level, expected):
        assert affine_slN_data(N, level).central_charge == expected

    def test_symbolic_sugawara_formula(self):
        level = Symbol("k")
        assert simplify(affine_sl3_data().central_charge - 8 * level / (level + 3)) == 0

    def test_free_field_metadata(self):
        assert heisenberg_data().ope_summary["alpha_alpha_double_pole"] == Symbol("k")
        assert betagamma_data().ope_summary["beta_gamma_simple_pole"] == 1
        assert bc_ghosts_data().parity == (1, 1)
        assert free_fermion_data().central_charge == Rational(1, 2)

    def test_principal_w_generator_weights(self):
        for N in range(2, 8):
            data = wN_data(N)
            assert data.gen_weights == tuple(range(2, N + 1))
            assert data.n_generators == N - 1


class TestBoundedBenchmarks:
    def test_rank_one_even_superboson_vector(self):
        benchmark = bounded_cohomology_benchmark(heisenberg_data())
        assert benchmark.support == (0, 1)
        assert benchmark.dimensions == {0: 2, 1: 1}
        assert benchmark.vector == (2, 1)
        assert benchmark.prefix(5) == (2, 1, 0, 0, 0, 0)
        assert "Theorem 7.4" in benchmark.source

    def test_virasoro_support_and_dimensions(self):
        benchmark = bounded_cohomology_benchmark(virasoro_data())
        assert benchmark.support == (0, 2, 3)
        assert benchmark.dimensions == {0: 1, 2: 1, 3: 1}
        assert benchmark.vector == (1, 0, 1, 1)
        assert "Theorem 7.2" in benchmark.source

    @pytest.mark.parametrize(
        "data",
        [affine_sl2_data(), betagamma_data(), bc_ghosts_data(), w3_data()],
    )
    def test_other_family_vectors_are_withheld(self, data):
        assert bounded_cohomology_benchmark(data) is None


class TestDefaultChartFirewall:
    @pytest.mark.parametrize(
        "data",
        [
            heisenberg_data(),
            affine_sl2_data(),
            betagamma_data(),
            bc_ghosts_data(),
            virasoro_data(),
            w3_data(),
        ],
    )
    def test_default_result_contains_no_chart_dimensions(self, data):
        result = compute_chirhoch(data)
        assert result.dim_H0 is None
        assert result.dim_H1 is None
        assert result.dim_H2 is None
        assert result.support is None
        assert result.dimensions is None
        assert result.all_unobstructed is None
        assert result.status.startswith("open")
        assert result.hypothesis_package == THEOREM_H_REQUIRED_COMPONENTS

    def test_numeric_compatibility_entry_points_are_open(self):
        data = heisenberg_data()
        assert center_dimension(data) is None
        assert center_dimension_koszul_dual(data) is None

    def test_polynomial_has_open_coefficients(self):
        polynomial = compute_hochschild_polynomial(affine_sl2_data())
        assert polynomial.coefficients == [None, None, None]
        assert polynomial.total_dimension is None
        assert polynomial.euler_characteristic is None
        assert polynomial.is_palindromic is None
        with pytest.raises(OpenChirHochComputation):
            polynomial.evaluate(1)

    def test_w3_packet_has_generator_data_and_open_chart(self):
        packet = compute_w_algebra_hochschild(w3_data())
        assert packet.gen_degrees == (2, 3)
        assert packet.bounded_benchmark is None
        assert packet.chart_support is None
        assert packet.chart_dimensions is None
        assert packet.dim_n(0) is None
        assert packet.total_dim is None


class TestExplicitTransport:
    def test_open_comparison_does_not_transport_bounded_values(self):
        data = virasoro_data()
        result = compute_chirhoch(data, bounded_to_chart=_comparison(data, "open"))
        assert result.support is None
        assert result.dimensions is None
        assert result.status == "open-bounded-to-chart-comparison"

    def test_assumed_virasoro_comparison_gives_conditional_chart_values(self):
        data = virasoro_data()
        result = compute_chirhoch(data, bounded_to_chart=_comparison(data))
        assert result.status == "conditional-assumed-bounded-to-chart"
        assert result.support == (0, 2, 3)
        assert result.dimensions == {0: 1, 2: 1, 3: 1}
        assert result.dim_H0 == 1
        assert result.dim_H1 == 0
        assert result.dim_H2 == 1

    def test_assumed_superboson_comparison_gives_conditional_vector(self):
        data = heisenberg_data()
        result = compute_chirhoch(data, bounded_to_chart=_comparison(data))
        assert result.support == (0, 1)
        assert result.dimensions == {0: 2, 1: 1}
        assert result.poincare_polynomial == [2, 1, 0]

    def test_family_support_datum_controls_arbitrary_support(self):
        data = affine_sl2_data()
        result = compute_chirhoch(data, family_datum=_family_datum(data.name))
        assert result.status == "conditional-assumed-H_H"
        assert result.support == (-1, 2, 5)
        assert result.dimensions == {-1: 3, 2: 4, 5: 1}
        assert result.poincare_polynomial is None

    def test_family_support_datum_names_every_required_component(self):
        datum = _family_datum("affine_sl2")
        assert set(datum.named_components) == set(THEOREM_H_REQUIRED_COMPONENTS)

    def test_family_support_datum_requires_matching_family(self):
        with pytest.raises(ValueError, match="differs"):
            compute_chirhoch(
                heisenberg_data(), family_datum=_family_datum("affine_sl2")
            )


class TestDerivationScope:
    @pytest.mark.parametrize("N", (2, 3, 4, 5, 8))
    def test_affine_zero_modes_are_known_inner_subspace_only(self, N):
        analysis = derivation_analysis(affine_slN_data(N))
        expected = N * N - 1
        assert analysis.known_inner_zero_mode_dimension == expected
        assert analysis.exact_ope_constraints["adjoint_zero_mode_dimension"] == expected
        assert analysis.total_derivations is None
        assert analysis.inner_derivations is None
        assert analysis.outer_derivations is None
        assert analysis.dim_chirhoch1 is None

    def test_legacy_affine_report_withholds_h1(self):
        report = verify_km_h1_equals_dim_g()
        assert report["all_passed"] is None
        for row in report["families"].values():
            assert row["dim_H1"] is None
            assert row["dim_g"] == row["known_inner_zero_mode_dimension"]

    def test_heisenberg_ope_candidate_is_separate_from_chart_class(self):
        packet = _ope_derivation_check_heisenberg()
        assert packet["shift_singular_part"] == 0
        assert packet["shift_is_generator_level_ope_compatible"] is True
        assert packet["chart_outer_quotient_dim"] is None

    def test_virasoro_ope_constraint_and_bounded_support(self):
        packet = _ope_derivation_check_virasoro()
        assert packet["ope_constraint"] == "D(c)=2ac"
        assert packet["bounded_support"] == (0, 2, 3)
        assert packet["chart_outer_quotient_dim"] is None

    def test_w3_low_weight_ansatz_stays_open(self):
        packet = _ope_derivation_check_w3()
        assert packet["state_space_basis_weight_3"] == ("dT", "W")
        assert packet["chart_outer_quotient_dim"] is None


class TestDeformationAndDualityFirewalls:
    def test_formal_parameter_family_is_separate_from_chart_class(self):
        lanes = deformation_obstruction_analysis(virasoro_data())
        formal, chart = lanes
        assert formal.is_unobstructed is True
        assert formal.cohomological_degree is None
        assert chart.is_unobstructed is None
        assert chart.obstruction_class is None
        assert all_deformations_unobstructed(virasoro_data()) is None

    def test_dual_betti_relation_remains_open(self):
        relation = koszul_duality_check(betagamma_data(), bc_ghosts_data())
        assert relation.betti_A is None
        assert relation.betti_A_dual is None
        assert relation.relation_satisfied is None

    def test_degree_two_dual_lane_requires_support_and_pairing_data(self):
        data = heisenberg_data()
        comparison = _comparison(data)
        assert center_dimension_koszul_dual(
            data, bounded_to_chart=comparison
        ) is None
        pairing = KoszulDualityDatum(
            family=data.name,
            dual_family="curved_second_kind_dual",
            pairing_map="pair_H",
            cohomological_shift=2,
        )
        assert center_dimension_koszul_dual(
            data,
            duality_datum=pairing,
            bounded_to_chart=comparison,
        ) == 0

    def test_affine_parameter_involution_is_exact(self):
        data = affine_sl2_data(k=3)
        packet = ff_involution_on_hochschild(data)
        assert packet["h_dual"] == 2
        assert packet["dual_level"] == -7
        assert packet["parameter_involution_check"] is True
        assert packet["dimensions_match"] is None

    def test_virasoro_companion_parameter_does_not_supply_dimensions(self):
        packet = ff_involution_on_hochschild(virasoro_data(c=7))
        assert packet["dual_central_charge_candidate"] == 19
        assert packet["dimensions_match"] is None


class TestTypedObjectsAndFiniteChecks:
    def test_object_firewall(self):
        firewall = bar_koszul_derived_center_firewall()
        assert firewall["B(A)"] == "ordered bar coalgebra before cohomology"
        assert firewall["A^i"] == "bar-cohomology coalgebra H^*(B(A))"
        assert firewall["Omega(B(A))"] == "bar--cobar reconstruction of A"
        assert firewall["Z_ch^der(A)"].startswith("RHom_{A^e}(A,A)")
        assert firewall["A^!"] != firewall["Z_ch^der(A)"]

    def test_package_entry_counts(self):
        assert len(holographic_package_entries()) == 7
        assert len(modular_koszul_primary_projections()) == 6
        assert set(holographic_package_entries()) != set(
            modular_koszul_primary_projections()
        )

    def test_whitehead_calculation_is_type_separated(self):
        sl2 = whitehead_lemma_check("A", 1)
        sl3 = whitehead_lemma_check("A", 2)
        assert (sl2["dim_g"], sl3["dim_g"]) == (3, 8)
        assert sl2["H1_g_g"] == sl2["H2_g_g"] == 0
        assert sl2["chiral_H1"] is None

    def test_spectral_sequence_page_is_withheld(self):
        packet = hochschild_spectral_sequence_E2(heisenberg_data(), 5, 3)
        assert packet["shape"] == (6, 4)
        assert packet["E2_page"] is None
        assert packet["collapse"] is None


class TestStatusReports:
    def test_all_standard_rows_are_open_by_default(self):
        rows = compute_all_standard_families()
        assert rows
        for result in rows.values():
            assert result.dimensions is None
            assert result.status.startswith("open")

    def test_theorem_report_names_hypotheses(self):
        report = verify_theorem_h_complete(virasoro_data())
        assert report["passed"] is None
        assert report["support"] is None
        assert report["hypothesis_package"] == THEOREM_H_REQUIRED_COMPONENTS
        assert BOUNDED_TO_CHART_OBLIGATION in report["resolution_obligation"]

    def test_universal_polynomial_is_withheld(self):
        report = verify_universal_polynomial()
        assert report["all_passed"] is None
        assert all(row["polynomial"] is None for row in report["families"].values())

    def test_summary_contains_open_fields(self):
        table = summary_table()
        assert table
        assert all(row["dim_H0"] is None for row in table)
        assert all(row["support"] is None for row in table)

    def test_retired_bureaucratic_stem_is_absent(self):
        source = ENGINE.read_text(encoding="utf-8").lower()
        assert ("cert" + "if") not in source
