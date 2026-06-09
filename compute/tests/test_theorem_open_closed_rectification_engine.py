r"""Tests for open/closed rectification engine: four-stage architecture
witnesses against DNP, CDG, Safronov-Gunningham, Safronov.

CHAPTER ANCHOR: thqg_open_closed_realization.tex

40+ tests organized in 8 sections:
  1. Heisenberg open/closed MC element (8 tests)
  2. Derived center for sl_2 at level 1 (7 tests)
  3. A_infty Yang-Baxter = MC at arity 3 (5 tests)
  4. DNP line operator bridge (5 tests)
  5. CDG boundary-bulk bridge (4 tests)
  6. Safronov CoHA bridge (4 tests)
  7. Four-stage architecture witnesses (4 tests)
  8. Cross-checks and consistency (9 tests)

Multi-path verification per claim:
  - Path 1: direct computation from engine
  - Path 2: alternative formula / known result
  - Path 3: cross-family consistency / duality
"""

from fractions import Fraction
from pathlib import Path

import pytest

from compute.lib.theorem_open_closed_rectification_engine import (
    LAMBDA_1,
    LAMBDA_2_SCALAR,
    kappa_family,
    kappa_dual,
    open_closed_object_separation_witness,
    physical_bulk_comparison_check,
    factorization_equivalence_hypothesis_check,
    HeisenbergOpenClosedMC,
    DerivedCenterSl2Level1,
    ainfty_yang_baxter_arity3,
    DNPLineOperatorBridge,
    CDGBoundaryBulkBridge,
    SafronovCoHABridge,
    four_stage_audit,
    annulus_trace_cross_check,
    kappa_complementarity_check,
    ope_vs_rmatrix_pole_check,
    derived_center_three_term_check,
    open_closed_mc_decomposition_check,
    shadow_archetype_classification,
    virasoro_quartic_contact,
)


ROOT = Path(__file__).resolve().parents[2]
THQG_TEX = ROOT / "chapters" / "connections" / "thqg_open_closed_realization.tex"
FRONTIER_TEX = (
    ROOT / "chapters" / "connections" / "frontier_modular_holography_platonic.tex"
)
CONCORDANCE_TEX = ROOT / "chapters" / "connections" / "concordance.tex"
EDITORIAL_TEX = ROOT / "chapters" / "connections" / "editorial_constitution.tex"
PREFACE_TEX = ROOT / "chapters" / "frame" / "preface.tex"
INTRODUCTION_TEX = ROOT / "chapters" / "theory" / "introduction.tex"
ENGINE = ROOT / "compute" / "lib" / "theorem_open_closed_rectification_engine.py"


def test_completed_datum_terminology_is_not_ade_mckay():
    thqg = THQG_TEX.read_text(encoding="utf-8")
    active = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [THQG_TEX, FRONTIER_TEX, CONCORDANCE_TEX, EDITORIAL_TEX, ENGINE]
    )

    assert r"\begin{definition}[Completed modular Koszul datum]" in thqg
    assert "Terminology: completed datum, not ADE/McKay" in thqg
    assert "Platonic-solids/ADE/McKay usage" in thqg
    assert "not ADE/McKay or Platonic-solids data" in active
    assert "Completed modular Koszul datum (def:thqg-completed-platonic-datum)" in active

    forbidden = [
        "Completed 8-fold platonic datum",
        "Platonic summary",
        "The mature platonic theorem",
        "Platonic completion theorem",
        "platonic package|textbf",
    ]
    for phrase in forbidden:
        assert phrase not in active


def test_bd_algebraic_end_bridge_is_coordinate_dependent():
    thqg = THQG_TEX.read_text(encoding="utf-8")
    preface = PREFACE_TEX.read_text(encoding="utf-8")
    active = "\n".join([thqg, preface, ENGINE.read_text(encoding="utf-8")])

    assert r"\label{prop:bd-algebraic-bridge}" in thqg
    assert "coordinate-dependent isomorphism of non-$\\Sigma$ operads" in thqg
    for step in [
        "Formal-disk restriction.",
        "D-module trivialisation.",
        "Spectral-variable identification.",
        "Operadic composition.",
    ]:
        assert step in thqg
    assert r"\operatorname{Aut}(\mathcal{O})" in thqg
    assert "provides descent data" in thqg

    assert r"Proposition~\ref{prop:bd-algebraic-bridge}" in preface
    assert "not an equality of the\nglobal BD" in preface
    assert r"$\End^{\mathrm{ch}}_{A_p}$" in preface

    forbidden = [
        "BD chiral operad = algebraic",
        "BD chiral operad is the algebraic",
        "BD operad equals End^ch_A",
        "End^ch_A is the BD operad",
    ]
    for phrase in forbidden:
        assert phrase not in active


# ======================================================================
#  Section 1: Heisenberg open/closed MC element
# ======================================================================

class TestHeisenbergOpenClosedMC:
    """8 tests for the Heisenberg open/closed MC element."""

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1."""
        mc = HeisenbergOpenClosedMC(Fraction(1))
        assert mc.kappa == Fraction(1)

    def test_kappa_heisenberg_k2(self):
        """kappa(H_2) = 2."""
        mc = HeisenbergOpenClosedMC(Fraction(2))
        assert mc.kappa == Fraction(2)

    def test_r_matrix_pole_order(self):
        """AP19: r-matrix for Heisenberg has pole order 1 (OPE has order 2)."""
        mc = HeisenbergOpenClosedMC(Fraction(1))
        result = mc.theta_closed_genus0_arity2()
        assert result["pole_order"] == 1
        assert result["ope_pole_order"] == 2

    def test_genus1_curvature(self):
        """F_1(H_k) = k/24 (kappa * lambda_1)."""
        for k in [1, 2, 3, 5]:
            mc = HeisenbergOpenClosedMC(Fraction(k))
            result = mc.theta_closed_genus1_arity0()
            assert result["F_1"] == Fraction(k, 24)

    def test_genus2_curvature(self):
        """F_2(H_k) = k * 7/5760 (uniform-weight, no cross-channel)."""
        mc = HeisenbergOpenClosedMC(Fraction(1))
        result = mc.theta_closed_genus2_arity0()
        assert result["F_2"] == LAMBDA_2_SCALAR
        assert result["lane"] == "uniform_weight_scalar"
        assert result["not_full_free_energy_for_multi_weight"] is True

    def test_annulus_trace(self):
        """Annulus trace: Delta_ns(Tr) = kappa * lambda_1.

        Three-path verification:
        Path 1: Direct from engine
        Path 2: kappa * 1/24 formula
        Path 3: Cross-check with genus-1 curvature
        """
        for k in [1, 2, 3]:
            mc = HeisenbergOpenClosedMC(Fraction(k))
            trace = mc.annulus_trace()
            # Path 1
            assert trace["annulus_trace_value"] == Fraction(k, 24)
            # Path 2
            assert trace["lambda_1"] == LAMBDA_1
            assert trace["kappa"] * trace["lambda_1"] == Fraction(k, 24)
            # Path 3: must equal F_1
            f1 = mc.theta_closed_genus1_arity0()["F_1"]
            assert trace["annulus_trace_value"] == f1

    def test_mc_equation_genus0(self):
        """MC equation at genus 0 for Heisenberg (abelian => trivial)."""
        mc = HeisenbergOpenClosedMC(Fraction(1))
        result = mc.mc_equation_genus0()
        assert result["mc_holds"] is True
        assert result["cybe_lhs"] == Fraction(0)

    def test_open_sector_class_g(self):
        """Heisenberg is class G: higher A_infty operations vanish."""
        mc = HeisenbergOpenClosedMC(Fraction(1))
        # mu_2 is nonzero (the OPE action)
        assert mc.open_sector_module_structure(2)["vanishes"] is False
        # mu_n = 0 for n >= 3 (class G)
        for n in range(3, 8):
            assert mc.open_sector_module_structure(n)["vanishes"] is True


# ======================================================================
#  Section 2: Derived center for sl_2 at level 1
# ======================================================================

class TestDerivedCenterSl2Level1:
    """7 tests for the derived center Z^der_ch(hat{sl}_2, k=1)."""

    def test_dimensions(self):
        """Z^0 = 1, Z^1 = 3, Z^2 = 1 at generic level."""
        dc = DerivedCenterSl2Level1(k=1)
        dims = dc.derived_center_dimensions()
        assert dims[0] == 1
        assert dims[1] == 3
        assert dims[2] == 1

    def test_dimensions_level2(self):
        """Same dimensions at level 2 (generic level independence)."""
        dc = DerivedCenterSl2Level1(k=2)
        dims = dc.derived_center_dimensions()
        assert dims == {0: 1, 1: 3, 2: 1}

    def test_critical_level_raises(self):
        """Critical level k = -2: center infinite-dimensional."""
        dc = DerivedCenterSl2Level1(k=-2)
        with pytest.raises(ValueError, match="Critical level"):
            dc.derived_center_dimensions()

    def test_gerstenhaber_bracket_sl2(self):
        """Gerstenhaber bracket on Z^1 reproduces sl_2 Lie bracket."""
        dc = DerivedCenterSl2Level1(k=1)
        bracket = dc.gerstenhaber_bracket_z1z1()
        assert bracket["[e,f]"] == ("h", Fraction(1))
        assert bracket["[h,e]"] == ("e", Fraction(2))
        assert bracket["[h,f]"] == ("f", Fraction(-2))
        assert bracket["is_standard_bracket"] is True

    def test_annulus_trace_sl2(self):
        """Annulus trace for sl_2 at level 1: kappa = 9/4.

        kappa(sl_2, k=1) = dim(sl_2) * (k + h^v) / (2 * h^v)
                         = 3 * (1 + 2) / (2 * 2) = 9/4.
        Delta_ns(Tr) = 9/4 * 1/24 = 3/32.
        """
        dc = DerivedCenterSl2Level1(k=1)
        trace = dc.annulus_trace_kappa()
        assert trace["kappa"] == Fraction(9, 4)
        assert trace["annulus_trace_value"] == Fraction(9, 4) * Fraction(1, 24)
        assert trace["annulus_trace_value"] == Fraction(3, 32)

    def test_koszul_dual_complementarity(self):
        """kappa + kappa_dual = 0 for affine sl_2 (AP24: correct for KM).

        k = 1: kappa = 9/4
        k_dual = -1 - 4 = -5: kappa_dual = 3*(-5+2)/4 = -9/4
        Sum = 0.
        """
        dc = DerivedCenterSl2Level1(k=1)
        kappa_d = dc.koszul_dual_level()
        assert dc.kappa + kappa_d == Fraction(0)

    def test_cup_product_nondegenerate(self):
        """Cup product on Z^1 x Z^1 -> Z^2 is nondegenerate (Killing form)."""
        dc = DerivedCenterSl2Level1(k=1)
        cup = dc.cup_product_z1z1()
        assert cup["is_nondegenerate"] is True
        assert cup["dimension_Z2"] == 1


# ======================================================================
#  Section 3: A_infty Yang-Baxter = MC at arity 3
# ======================================================================

class TestAInftyYangBaxter:
    """5 tests for A_infty YBE = MC equation at arity 3."""

    def test_heisenberg_cybe_trivial(self):
        """Heisenberg: abelian => CYBE trivially satisfied."""
        result = ainfty_yang_baxter_arity3("Heisenberg", k=1)
        assert result["cybe_satisfied"] is True
        assert result["lhs_value"] == Fraction(0)

    def test_sl2_cybe_rational_rmatrix(self):
        """Affine sl_2: standard rational r-matrix satisfies CYBE."""
        result = ainfty_yang_baxter_arity3("Affine_sl2", k=1)
        assert result["cybe_satisfied"] is True
        assert result["infinitesimal_braid_check"] is True
        assert result["witness_type"] == "closed_collision_cybe"
        assert result["full_open_closed_factorization"] is False

    def test_sl2_casimir_fundamental(self):
        """Quadratic Casimir of sl_2 on fundamental = 3/4."""
        result = ainfty_yang_baxter_arity3("Affine_sl2", k=1)
        assert result["casimir_fundamental"] == Fraction(3, 4)

    def test_virasoro_arity3_mc(self):
        """Virasoro: arity-3 MC equation holds, cubic shadow is gauge-trivial."""
        result = ainfty_yang_baxter_arity3("Virasoro", c=26)
        assert result["arity3_mc_holds"] is True
        assert result["cubic_gauge_trivial"] is True

    def test_virasoro_rmatrix_poles(self):
        """AP19: Virasoro r-matrix has poles at z^{-3} and z^{-1} (not z^{-4}, z^{-2})."""
        result = ainfty_yang_baxter_arity3("Virasoro", c=26)
        assert result["r_matrix_pole_orders"] == [3, 1]
        assert result["ope_pole_orders"] == [4, 2, 1]
        assert result["engine_verifies_full_mc"] is False


# ======================================================================
#  Section 4: DNP line operator bridge
# ======================================================================

class TestDNPLineOperatorBridge:
    """5 tests for DNP [2508.11749] line operator identification."""

    def test_sl2_integrable_count(self):
        """Affine sl_2 at level k: boundary integrables are not the line count."""
        for k in [1, 2, 3, 4]:
            dnp = DNPLineOperatorBridge("Affine_sl2", k=k)
            result = dnp.line_operator_count()
            assert result["n_integrable_reps"] == k + 1
            assert result["dual_level"] == -k - 4
            assert result["dual_level_integrable_reps"] == 0
            assert result["line_operator_count_is_integrable_count"] is False

    def test_heisenberg_continuous_modules(self):
        """Heisenberg: continuous family of Fock modules."""
        dnp = DNPLineOperatorBridge("Heisenberg", k=1)
        result = dnp.line_operator_count()
        assert result["n_integrable_reps"] == "continuous"

    def test_meromorphic_tensor_heisenberg(self):
        """DNP meromorphic tensor has the Heisenberg R-matrix scalar witness."""
        dnp = DNPLineOperatorBridge("Heisenberg", k=1)
        result = dnp.meromorphic_tensor_is_bar_coproduct()
        assert result["scalar_witness_holds"] is True
        assert result["identification_holds"] is False
        assert result["full_factorization_equivalence"] is False
        assert result["is_abelian"] is True

    def test_meromorphic_tensor_sl2(self):
        """DNP meromorphic tensor has the sl_2 R-matrix scalar witness."""
        dnp = DNPLineOperatorBridge("Affine_sl2", k=1)
        result = dnp.meromorphic_tensor_is_bar_coproduct()
        assert result["scalar_witness_holds"] is True
        assert result["identification_holds"] is False
        assert result["full_factorization_equivalence"] is False
        assert result["is_abelian"] is False

    def test_meromorphic_tensor_virasoro(self):
        """DNP meromorphic tensor for Virasoro (higher-pole r-matrix)."""
        dnp = DNPLineOperatorBridge("Virasoro", c=26)
        result = dnp.meromorphic_tensor_is_bar_coproduct()
        assert result["scalar_witness_holds"] is True
        assert result["identification_holds"] is False
        assert result["full_factorization_equivalence"] is False


# ======================================================================
#  Section 5: CDG boundary-bulk bridge
# ======================================================================

class TestCDGBoundaryBulkBridge:
    """4 tests for CDG [2005.00083] boundary-bulk consistency."""

    def test_bulk_is_derived_center(self):
        """CDG cochain shadow is not physical bulk equivalence without data."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            cdg = CDGBoundaryBulkBridge(fam)
            result = cdg.bulk_is_derived_center()
            assert result["cochain_closed_sector_match"] is True
            assert result["match"] is False
            assert result["physical_bulk_identification"] is False
            assert "quasi_isomorphism" in result["missing_hypotheses"]

    def test_p0_equals_gerstenhaber(self):
        """CDG's P_0 structure = our Gerstenhaber structure."""
        cdg = CDGBoundaryBulkBridge("Heisenberg")
        result = cdg.bulk_algebra_structure()
        assert result["are_same"] is True
        assert result["cochain_shadow_structure_match"] is True
        assert result["physical_bulk_reconstructed"] is False

    def test_boundary_module_factors_through_universal(self):
        """CDG's boundary module structure factors through U(A)."""
        cdg = CDGBoundaryBulkBridge("Affine_sl2", k=1)
        result = cdg.boundary_module_structure()
        assert result["cdg_confirms_stage"] == 1
        assert result["universal_action_classified"] is True
        assert result["physical_bulk_identification"] is False

    def test_cdg_all_families(self):
        """CDG cochain comparison holds while physical-bulk equality is typed."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            cdg = CDGBoundaryBulkBridge(fam)
            assert cdg.bulk_is_derived_center()["cochain_closed_sector_match"] is True
            assert cdg.bulk_is_derived_center()["match"] is False
            assert cdg.bulk_algebra_structure()["are_same"] is True


# ======================================================================
#  Section 6: Safronov CoHA bridge
# ======================================================================

class TestSafronovCoHABridge:
    """4 tests for Safronov [2406.12838] and Safronov-Gunningham [2312.07595]."""

    def test_coha_bar_duality(self):
        """CoHA/bar comparison is a finite shadow witness here."""
        for fam in ["Heisenberg", "Affine_sl2"]:
            bridge = SafronovCoHABridge(fam, k=1)
            result = bridge.coha_bar_duality_check()
            assert result["bar_comultiplication_witness"] is True
            assert result["full_duality_proved_by_engine"] is False

    def test_complementarity_heisenberg(self):
        """Heisenberg: kappa + kappa_dual = 0 as scalar witness."""
        bridge = SafronovCoHABridge("Heisenberg", k=1)
        result = bridge.complementarity_as_lagrangian()
        assert result["complement_sum"] == Fraction(0)
        assert result["scalar_lagrangian_witness"] == "transverse"
        assert result["full_lagrangian_intersection_proved_by_engine"] is False

    def test_complementarity_virasoro(self):
        """Virasoro: kappa + kappa_dual = 13 != 0 (AP24: excess Lagrangian).

        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
        This is NONZERO, unlike KM families.
        """
        bridge = SafronovCoHABridge("Virasoro", c=1)
        result = bridge.complementarity_as_lagrangian()
        assert result["complement_sum"] == Fraction(13)
        assert result["scalar_lagrangian_witness"] == "excess"
        assert result["full_lagrangian_intersection_proved_by_engine"] is False

    def test_complementarity_virasoro_c26(self):
        """At c=26 (critical): kappa = 13, kappa_dual = 0. Sum = 13."""
        bridge = SafronovCoHABridge("Virasoro", c=26)
        result = bridge.complementarity_as_lagrangian()
        assert result["kappa_A"] == Fraction(13)
        assert result["kappa_A_dual"] == Fraction(0)
        assert result["complement_sum"] == Fraction(13)


# ======================================================================
#  Section 7: Four-stage architecture witnesses
# ======================================================================

class TestFourStageArchitecture:
    """Four-stage architecture witness tests."""

    def test_all_stages_present(self):
        """All four stages present in the witness."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            witness = four_stage_audit(fam, k=1, c=26)
            assert set(witness["stages"].keys()) == {1, 2, 3, 4}

    def test_stage1_proved(self):
        """Stage 1 gives a cochain universal-action witness."""
        witness = four_stage_audit("Heisenberg", k=1)
        assert witness["stages"][1]["cochain_universal_action"] is True
        assert witness["stages"][1]["physical_bulk_identification"] is False

    def test_stage2_meromorphic_match(self):
        """Stage 2 separates R-matrix witness from full equivalence."""
        witness = four_stage_audit("Affine_sl2", k=1)
        assert witness["stages"][2]["scalar_rmatrix_witness"] is True
        assert witness["stages"][2]["meromorphic_tensor_match"] is False
        assert witness["stages"][2]["full_factorization_equivalence"] is False

    def test_stage3_bulk_identification(self):
        """Stage 3 has cochain match, not physical-bulk identification."""
        witness = four_stage_audit("Heisenberg", k=1)
        assert witness["stages"][3]["cochain_closed_sector_match"] is True
        assert witness["stages"][3]["bulk_identification_match"] is False
        assert witness["stages"][3]["physical_bulk_identification"] is False


# ======================================================================
#  Section 8: Cross-checks and consistency
# ======================================================================

class TestCrossChecks:
    """Cross-checks, object separation, and consistency."""

    def test_open_closed_object_separation(self):
        """Bar, Verdier dual, derived center, and physical bulk are distinct."""
        witness = open_closed_object_separation_witness()
        assert witness["all_forbidden_equalities_rejected"] is True
        assert witness["forbidden_equalities"]["bar_equals_derived_center"] is False
        assert witness["forbidden_equalities"]["koszul_dual_equals_derived_center"] is False
        assert witness["objects"]["bar_cobar_inverse"]["symbol"] == "Omega(B(A)) -> A"
        assert witness["objects"]["derived_center"]["producer"] == "Hochschild cohomology"

    def test_algebraic_closed_actor_not_physical_bulk(self):
        """The derived center is the algebraic closed actor, not physical bulk without OCA."""
        notation = open_closed_object_separation_witness()["algebraic_sector_notation"]
        assert notation["closed_actor"] == "Z_ch^der(A)"
        assert notation["physical_bulk_symbol_reserved"] == "Obs^bulk(T)"
        assert notation["derived_center_is_physical_bulk_without_oca"] is False
        assert notation["one_boundary_one_physical_bulk_target"] is True
        assert notation["centers_are_computational_models_not_bulk_theories"] is True
        assert notation["drinfeld_center_equals_bulk_status"].startswith("conjectural")

    def test_drinfeld_center_bulk_closure_remains_conjectural(self):
        """Center comparisons are evidence for one bulk target, not proved closures."""
        active = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [PREFACE_TEX, INTRODUCTION_TEX, THQG_TEX, ENGINE]
        )
        assert "Finite-window evidence and" in active
        assert "conditional center-comparison checks exist" in active
        assert "physical-bulk equivalence remains" in active
        assert "one boundary bulk target, not separate physical bulk theories" in active
        assert "centers_are_computational_models_not_bulk_theories" in active

        for forbidden in [
            "conj:drinfeld-center-equals-bulk}$, proved for Heisenberg",
            "\\emph{proved} for Heisenberg",
            "two different bulk theories",
            "are separate physical bulk theories",
        ]:
            assert forbidden not in active

    def test_physical_bulk_comparison_requires_typed_data(self):
        """Physical bulk is identified with the center only after all hypotheses."""
        empty = physical_bulk_comparison_check()
        assert empty["universal_action_classified"] is False
        assert empty["physical_bulk_identified_with_derived_center"] is False
        assert "brace_map" in empty["missing_hypotheses"]

        action = physical_bulk_comparison_check(
            boundary_identification=True,
            local_operator_shadow=True,
            brace_map=True,
        )
        assert action["universal_action_classified"] is True
        assert action["physical_bulk_identified_with_derived_center"] is False
        assert action["missing_hypotheses"] == ["quasi_isomorphism", "completion"]

        equivalence = physical_bulk_comparison_check(
            boundary_identification=True,
            local_operator_shadow=True,
            brace_map=True,
            quasi_isomorphism=True,
            completion=True,
        )
        assert equivalence["physical_bulk_identified_with_derived_center"] is True

    def test_factorization_equivalence_needs_more_than_rmatrix(self):
        """An R-matrix scalar check does not build C_op equivalence."""
        missing = factorization_equivalence_hypothesis_check()
        assert missing["full_factorization_equivalence"] is False
        assert "associator_coherence" in missing["missing_hypotheses"]

        full = factorization_equivalence_hypothesis_check(
            braided_monoidal_functor=True,
            associator_coherence=True,
            boundary_cosheaf_descent=True,
            completion=True,
            quasi_equivalence=True,
        )
        assert full["full_factorization_equivalence"] is True

    def test_annulus_trace_three_paths(self):
        """Three paths for annulus trace agree as a scalar witness."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            params = {"k": 1} if fam != "Virasoro" else {"c": 26}
            result = annulus_trace_cross_check(fam, **params)
            assert result["all_agree"] is True
            assert result["finite_scalar_witness_only"] is True
            assert result["proves_full_open_closed_factorization"] is False

    def test_kappa_complementarity_km(self):
        """kappa + kappa_dual = 0 for KM families (AP24)."""
        for fam in ["Heisenberg", "Affine_sl2"]:
            params = {"k": 1}
            result = kappa_complementarity_check(fam, **params)
            assert result["sum"] == Fraction(0)
            assert result["match"] is True

    def test_kappa_complementarity_virasoro(self):
        """kappa + kappa_dual = 13 for Virasoro (AP24).

        Three-path verification:
        Path 1: c/2 + (26-c)/2 = 13 (direct)
        Path 2: At c=13 (self-dual): kappa = 13/2, kappa_dual = 13/2, sum = 13
        Path 3: At c=0: kappa = 0, kappa_dual = 13, sum = 13
        """
        # Path 1: generic c
        result = kappa_complementarity_check("Virasoro", c=1)
        assert result["sum"] == Fraction(13)
        # Path 2: self-dual point
        result = kappa_complementarity_check("Virasoro", c=13)
        assert result["kappa"] == Fraction(13, 2)
        assert result["kappa_dual"] == Fraction(13, 2)
        assert result["sum"] == Fraction(13)
        # Path 3: c=0
        result = kappa_complementarity_check("Virasoro", c=0)
        assert result["kappa"] == Fraction(0)
        assert result["kappa_dual"] == Fraction(13)
        assert result["sum"] == Fraction(13)

    def test_ap19_pole_shift_all_families(self):
        """AP19: r-matrix poles one less than OPE for all families."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            result = ope_vs_rmatrix_pole_check(fam)
            assert result["ap19_satisfied"] is True
            assert result["pole_shift"] == 1

    def test_derived_center_concentrated_012(self):
        """Theorem H: derived center concentrated in degrees {0, 1, 2}."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro", "W3"]:
            result = derived_center_three_term_check(fam)
            assert result["concentrated_in_012"] is True
            assert result["theorem_h_satisfied"] is True

    def test_derived_center_critical_level_rejected(self):
        """Critical affine level fails the generic-level hypothesis."""
        result = derived_center_three_term_check("Affine_sl2", k=-2)
        assert result["concentrated_in_012"] is False
        assert result["theorem_h_satisfied"] is False
        assert result["failed_hypothesis"] == "generic_level"

    def test_open_closed_mc_decomposition(self):
        """Theta^oc requires admissible open/closed extension data."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            params = {"k": 1} if fam != "Virasoro" else {"c": 26}
            result = open_closed_mc_decomposition_check(fam, **params)
            assert result["closed_projection_available"] is True
            assert result["all_sectors_from_single_mc"] is False
            assert "mixed_maps" in result["missing_hypotheses"]

            full_params = {
                **params,
                "module_structures": True,
                "mixed_maps": True,
                "boundary_compatibility": True,
                "completion": True,
            }
            full = open_closed_mc_decomposition_check(fam, **full_params)
            assert full["admissible_extension"] is True
            assert full["all_sectors_from_single_mc"] is True

    def test_shadow_archetype_classification(self):
        """Shadow archetypes: G/L/C/M correctly assigned."""
        assert shadow_archetype_classification("Heisenberg")["archetype"] == "G"
        assert shadow_archetype_classification("Affine_sl2")["archetype"] == "L"
        assert shadow_archetype_classification("Virasoro", c=26)["archetype"] == "M"
        assert shadow_archetype_classification("W3", c=2)["archetype"] == "M"
        assert (
            shadow_archetype_classification("Virasoro", c=26)[
                "swiss_cheese_formality_proved_by_scalar"
            ]
            is False
        )

    def test_virasoro_quartic_contact(self):
        """Q^ct_Vir = 10/(c(5c+22)) at specific c values.

        Three-path verification:
        Path 1: Direct formula
        Path 2: Check at c=26: Q = 10/(26*152) = 10/3952 = 5/1976
        Path 3: Check poles at c=0 and c=-22/5
        """
        # Path 1
        assert virasoro_quartic_contact(Fraction(26)) == Fraction(10, 3952)
        assert virasoro_quartic_contact(Fraction(26)) == Fraction(5, 1976)
        # Path 2
        assert virasoro_quartic_contact(Fraction(1)) == Fraction(10, 27)
        # Path 3: poles
        with pytest.raises(ValueError):
            virasoro_quartic_contact(Fraction(0))
        with pytest.raises(ValueError):
            virasoro_quartic_contact(Fraction(-22, 5))

    def test_kappa_formula_consistency(self):
        """kappa formula consistent across all families (AP1 cross-check).

        kappa(H_k) = k.
        kappa(Vir_c) = c/2.
        kappa(sl_2, k) = 3(k+2)/4.

        Path 1: Direct computation
        Path 2: Check Heisenberg at k=1 gives c=1 but kappa=1 (not 1/2)
        Path 3: Check sl_2 at k=1 gives c=1 but kappa=9/4 (not 1/2)
        """
        # Path 1
        assert kappa_family("Heisenberg", k=1) == Fraction(1)
        assert kappa_family("Virasoro", c=1) == Fraction(1, 2)
        assert kappa_family("Affine_sl2", k=1) == Fraction(9, 4)
        # Path 2: kappa(H_k) != c(H_k)/2 in general
        # For H_k: c = 1 (one free boson), kappa = k
        # At k=2: kappa = 2 but c/2 = 1/2. DIFFERENT!
        assert kappa_family("Heisenberg", k=2) == Fraction(2)
        assert kappa_family("Heisenberg", k=2) != Fraction(1, 2)
        # Path 3: kappa(sl_2) != c(sl_2)/2 in general (AP39)
        # At k=1: c(sl_2) = 3*1/(1+2) = 1, kappa = 9/4
        assert kappa_family("Affine_sl2", k=1) == Fraction(9, 4)
        assert kappa_family("Affine_sl2", k=1) != Fraction(1, 2)
