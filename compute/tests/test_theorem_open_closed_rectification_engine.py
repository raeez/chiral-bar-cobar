r"""Tests for open/closed rectification engine: four-stage architecture
audit against DNP, CDG, Safronov-Gunningham, Safronov.

CHAPTER UNDER AUDIT: thqg_open_closed_realization.tex

40+ tests organized in 8 sections:
  1. Heisenberg open/closed MC element (8 tests)
  2. Derived center for sl_2 at level 1 (7 tests)
  3. A_infty Yang-Baxter = MC at arity 3 (5 tests)
  4. DNP line operator bridge (5 tests)
  5. CDG boundary-bulk bridge (4 tests)
  6. Safronov CoHA bridge (4 tests)
  7. Four-stage architecture audit (4 tests)
  8. Cross-checks and consistency (9 tests)

Multi-path verification per claim:
  - Path 1: direct computation from engine
  - Path 2: alternative formula / known result
  - Path 3: cross-family consistency / duality
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_open_closed_rectification_engine import (
    kappa_family,
    kappa_dual,
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
        assert result["F_2"] == Fraction(7, 5760)

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


# ======================================================================
#  Section 4: DNP line operator bridge
# ======================================================================

class TestDNPLineOperatorBridge:
    """5 tests for DNP [2508.11749] line operator identification."""

    def test_sl2_integrable_count(self):
        """Affine sl_2 at level k: k+1 integrable representations."""
        for k in [1, 2, 3, 4]:
            dnp = DNPLineOperatorBridge("Affine_sl2", k=k)
            result = dnp.line_operator_count()
            assert result["n_integrable_reps"] == k + 1

    def test_heisenberg_continuous_modules(self):
        """Heisenberg: continuous family of Fock modules."""
        dnp = DNPLineOperatorBridge("Heisenberg", k=1)
        result = dnp.line_operator_count()
        assert result["n_integrable_reps"] == "continuous"

    def test_meromorphic_tensor_heisenberg(self):
        """DNP meromorphic tensor = bar coproduct for Heisenberg."""
        dnp = DNPLineOperatorBridge("Heisenberg", k=1)
        result = dnp.meromorphic_tensor_is_bar_coproduct()
        assert result["identification_holds"] is True
        assert result["is_abelian"] is True

    def test_meromorphic_tensor_sl2(self):
        """DNP meromorphic tensor = Yang R-matrix coproduct for sl_2."""
        dnp = DNPLineOperatorBridge("Affine_sl2", k=1)
        result = dnp.meromorphic_tensor_is_bar_coproduct()
        assert result["identification_holds"] is True
        assert result["is_abelian"] is False

    def test_meromorphic_tensor_virasoro(self):
        """DNP meromorphic tensor for Virasoro (higher-pole r-matrix)."""
        dnp = DNPLineOperatorBridge("Virasoro", c=26)
        result = dnp.meromorphic_tensor_is_bar_coproduct()
        assert result["identification_holds"] is True


# ======================================================================
#  Section 5: CDG boundary-bulk bridge
# ======================================================================

class TestCDGBoundaryBulkBridge:
    """4 tests for CDG [2005.00083] boundary-bulk consistency."""

    def test_bulk_is_derived_center(self):
        """CDG bulk = our derived center Z^der_ch(A)."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            cdg = CDGBoundaryBulkBridge(fam)
            result = cdg.bulk_is_derived_center()
            assert result["match"] is True

    def test_p0_equals_gerstenhaber(self):
        """CDG's P_0 structure = our Gerstenhaber structure."""
        cdg = CDGBoundaryBulkBridge("Heisenberg")
        result = cdg.bulk_algebra_structure()
        assert result["are_same"] is True

    def test_boundary_module_factors_through_universal(self):
        """CDG's boundary module structure factors through U(A)."""
        cdg = CDGBoundaryBulkBridge("Affine_sl2", k=1)
        result = cdg.boundary_module_structure()
        assert result["cdg_confirms_stage"] == 1

    def test_cdg_all_families(self):
        """CDG identification holds for all standard families."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            cdg = CDGBoundaryBulkBridge(fam)
            assert cdg.bulk_is_derived_center()["match"] is True
            assert cdg.bulk_algebra_structure()["are_same"] is True


# ======================================================================
#  Section 6: Safronov CoHA bridge
# ======================================================================

class TestSafronovCoHABridge:
    """4 tests for Safronov [2406.12838] and Safronov-Gunningham [2312.07595]."""

    def test_coha_bar_duality(self):
        """CoHA^* ~ B(A) identification confirmed."""
        for fam in ["Heisenberg", "Affine_sl2"]:
            bridge = SafronovCoHABridge(fam, k=1)
            result = bridge.coha_bar_duality_check()
            assert result["duality"] == "CoHA^* ~ B(A)"

    def test_complementarity_heisenberg(self):
        """Heisenberg: kappa + kappa_dual = 0 (transverse Lagrangian)."""
        bridge = SafronovCoHABridge("Heisenberg", k=1)
        result = bridge.complementarity_as_lagrangian()
        assert result["complement_sum"] == Fraction(0)
        assert result["lagrangian_intersection"] == "transverse"

    def test_complementarity_virasoro(self):
        """Virasoro: kappa + kappa_dual = 13 != 0 (AP24: excess Lagrangian).

        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
        This is NONZERO, unlike KM families.
        """
        bridge = SafronovCoHABridge("Virasoro", c=1)
        result = bridge.complementarity_as_lagrangian()
        assert result["complement_sum"] == Fraction(13)
        assert result["lagrangian_intersection"] == "excess"

    def test_complementarity_virasoro_c26(self):
        """At c=26 (critical): kappa = 13, kappa_dual = 0. Sum = 13."""
        bridge = SafronovCoHABridge("Virasoro", c=26)
        result = bridge.complementarity_as_lagrangian()
        assert result["kappa_A"] == Fraction(13)
        assert result["kappa_A_dual"] == Fraction(0)
        assert result["complement_sum"] == Fraction(13)


# ======================================================================
#  Section 7: Four-stage architecture audit
# ======================================================================

class TestFourStageArchitecture:
    """4 tests for the four-stage architecture comprehensive audit."""

    def test_all_stages_present(self):
        """All four stages present in the audit."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            audit = four_stage_audit(fam, k=1, c=26)
            assert set(audit["stages"].keys()) == {1, 2, 3, 4}

    def test_stage1_proved(self):
        """Stage 1 (local one-colour) is PROVED."""
        audit = four_stage_audit("Heisenberg", k=1)
        assert audit["stages"][1]["status"] == "PROVED"

    def test_stage2_meromorphic_match(self):
        """Stage 2: DNP meromorphic tensor matches."""
        audit = four_stage_audit("Affine_sl2", k=1)
        assert audit["stages"][2]["meromorphic_tensor_match"] is True

    def test_stage3_bulk_identification(self):
        """Stage 3: CDG bulk = derived center."""
        audit = four_stage_audit("Heisenberg", k=1)
        assert audit["stages"][3]["bulk_identification_match"] is True


# ======================================================================
#  Section 8: Cross-checks and consistency
# ======================================================================

class TestCrossChecks:
    """9 tests for cross-checks and consistency."""

    def test_annulus_trace_three_paths(self):
        """Three independent paths for annulus trace all agree."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            params = {"k": 1} if fam != "Virasoro" else {"c": 26}
            result = annulus_trace_cross_check(fam, **params)
            assert result["all_agree"] is True

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

    def test_open_closed_mc_decomposition(self):
        """Theta^oc = Theta_A + sum mu^{M_j} decomposition."""
        for fam in ["Heisenberg", "Affine_sl2", "Virasoro"]:
            params = {"k": 1} if fam != "Virasoro" else {"c": 26}
            result = open_closed_mc_decomposition_check(fam, **params)
            assert result["all_sectors_from_single_mc"] is True

    def test_shadow_archetype_classification(self):
        """Shadow archetypes: G/L/C/M correctly assigned."""
        assert shadow_archetype_classification("Heisenberg")["archetype"] == "G"
        assert shadow_archetype_classification("Affine_sl2")["archetype"] == "L"
        assert shadow_archetype_classification("Virasoro", c=26)["archetype"] == "M"
        assert shadow_archetype_classification("W3", c=2)["archetype"] == "M"

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

        kappa(H_k) = k (NOT k/2, NOT c/2)
        kappa(Vir_c) = c/2 (NOT c, NOT k)
        kappa(sl_2, k) = 3(k+2)/4 (NOT k, NOT c/2)

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
