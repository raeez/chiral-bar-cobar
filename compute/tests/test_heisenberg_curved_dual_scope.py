"""Typed guards for the Heisenberg curved-dual and chart-comparison lanes."""

from __future__ import annotations

from fractions import Fraction

from compute.lib.bar_presentation_koszul_dual_engine import (
    bar_koszul_object_firewall,
    heisenberg_dual_ope,
    identify_heisenberg_generators,
)
from compute.lib.chiral_hochschild_engine import (
    KoszulDualityDatum,
    bar_koszul_derived_center_firewall,
    center_dimension_koszul_dual,
    compute_chirhoch,
    heisenberg_data,
    koszul_duality_check,
)
from compute.lib.derived_center_explicit import heisenberg_hh_cocycles
from compute.lib.sc_bar_cobar_inversion_engine import sector_ledger


class TestObjectSeparation:
    def test_chiral_hochschild_firewall_names_distinct_roles(self):
        roles = bar_koszul_derived_center_firewall()
        assert roles["B(A)"] == "ordered bar coalgebra before cohomology"
        assert roles["A^i"] == "bar-cohomology coalgebra H^*(B(A))"
        assert "Verdier/continuous-linear dual branch" in roles["A^!"]
        assert roles["Omega(B(A))"] == "bar--cobar reconstruction of A"
        assert roles["Z_ch^der(A)"].startswith("RHom_{A^e}(A,A)")

    def test_bar_presentation_firewall_separates_reconstruction_and_duality(self):
        roles = bar_koszul_object_firewall("H_k", "H_k^!")
        assert roles["bar_complex"] == "B(H_k): ordered bar coalgebra"
        assert roles["bar_dual_coalgebra"] == "H_k^i = H^*(B(H_k))"
        assert "Verdier/continuous linear dual" in roles["koszul_dual_algebra"]
        assert roles["bar_cobar_inversion"] == "Omega(B(H_k)) = H_k"
        assert roles["derived_center"] == "Z_ch^der(H_k): closed-sector actor"

    def test_public_sector_ledger_records_two_independent_maps(self):
        ledger = sector_ledger()
        assert ledger.universal_reconstruction == (
            "epsilon_A: Omega_X Bar_X(A) -> A"
        )
        assert ledger.verdier_object == "D_Ran Bar_X(A)"
        assert ledger.status["universal_reconstruction"] == (
            "proved-by-FG in pro-nilpotent Ran"
        )
        assert "H_VD" in ledger.status["verdier_object"]
        assert ledger.quadratic_comparison == "q_A: A^i -> Bar_X(A)"


class TestCurvedPresentationArithmetic:
    def test_presentation_records_curvature_and_typed_branch(self):
        presentation = identify_heisenberg_generators(Fraction(1))
        assert presentation.dual_name == "curved Sym^ch(V*[1])"
        assert presentation.generators == {1: ["J*"]}
        assert presentation.kappa_A == 1
        assert presentation.kappa_dual == -1
        assert presentation.complementarity_sum == 0
        assert "H^*(B(" in presentation.bar_dual_name
        assert "Verdier" in presentation.duality_branch
        assert "finite-type" in presentation.verdier_hypotheses
        assert "Omega(B(A))=A" in presentation.verdier_hypotheses

    def test_curvature_coefficient_is_exact(self):
        for level in (Fraction(1), Fraction(3), Fraction(-2)):
            ope = heisenberg_dual_ope(level)
            assert ope["curvature"] == -level
            assert ope["ope"][("J*", "J*")][2] == -level


class TestBoundedAndChartScope:
    def test_default_chart_packet_retains_only_bounded_benchmark(self):
        result = compute_chirhoch(heisenberg_data(k=1))
        assert result.bounded_benchmark is not None
        assert result.bounded_benchmark.support == (0, 1)
        assert result.bounded_benchmark.dimensions == {0: 2, 1: 1}
        assert result.bounded_benchmark.prefix(5) == (2, 1, 0, 0, 0, 0)
        assert result.support is None
        assert result.dimensions is None
        assert result.dim_H0 is None
        assert result.dim_H1 is None
        assert result.dim_H2 is None
        assert result.status == "open-family-support-datum"

    def test_derived_center_companion_withholds_chart_weight_split(self):
        status = heisenberg_hh_cocycles(Fraction(1), max_weight=4)
        assert status.bounded_benchmark is not None
        assert status.bounded_benchmark.vector == (2, 1)
        assert status.chart_support is None
        assert status.chart_dimensions is None
        assert status.conformal_weight_dimensions is None
        assert status.status == "open-bounded-to-chart-comparison"

    def test_duality_datum_alone_leaves_degree_two_open(self):
        data = heisenberg_data(k=1)
        pairing = KoszulDualityDatum(
            family=data.name,
            dual_family="curved Sym^ch(V*[1])",
            pairing_map="q_H",
            cohomological_shift=2,
            perfectness_status="open",
        )
        assert center_dimension_koszul_dual(data) is None
        assert center_dimension_koszul_dual(
            data, duality_datum=pairing
        ) is None

    def test_family_labels_leave_duality_comparison_open(self):
        relation = koszul_duality_check(
            heisenberg_data(k=1), heisenberg_data(k=-1)
        )
        assert relation.betti_A is None
        assert relation.betti_A_dual is None
        assert relation.relation_satisfied is None
        assert relation.status == "open-perfect-pairing-and-chart-comparison"
        assert "completed perfect pairing" in relation.resolution_obligation
