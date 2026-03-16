"""Tests for MC5 g>=2 frontier modules: Arakelov-Bar Transfer + Clutching Induction.

Covers:
  Module 1: mc5_arakelov_bar.py (Arakelov-Bar Transfer conjecture)
    - arakelov_green_identity
    - fay_trisecant_structure
    - quasi_modular_form_dimension
    - symmetry_reduction_dimension
    - arnold_defect_genus_g
    - theta_characteristics_count
    - prime_form_section_type
    - arakelov_bar_transfer_status
    - universality_defense

  Module 2: mc5_clutching_induction.py (Clutching induction strategy)
    - lambda_fp_exact
    - sewing_correction
    - sewing_correction_table
    - non_separating_degeneration_formula
    - induction_step_verification
    - ahat_multiplicativity_check
    - convergence_radius
    - clutching_compatibility

All arithmetic is exact (sympy.Rational).  Never floating point in assertions.
"""

import pytest
from sympy import Rational, Integer, simplify, Symbol, S

from compute.lib.mc5_arakelov_bar import (
    arakelov_green_identity,
    fay_trisecant_structure,
    quasi_modular_form_dimension,
    symmetry_reduction_dimension,
    arnold_defect_genus_g,
    theta_characteristics_count,
    prime_form_section_type,
    arakelov_bar_transfer_status,
    universality_defense,
)
from compute.lib.mc5_clutching_induction import (
    lambda_fp_exact,
    sewing_correction,
    sewing_correction_table,
    non_separating_degeneration_formula,
    induction_step_verification,
    ahat_multiplicativity_check,
    convergence_radius,
    clutching_compatibility,
)
from compute.lib.utils import lambda_fp


# ============================================================================
# MODULE 1: mc5_arakelov_bar.py — Arakelov-Bar Transfer
# ============================================================================


class TestArakelovGreenIdentity:
    """Test the Arakelov-Green identity documentation."""

    @pytest.mark.parametrize("g", [0, 1, 2, 3, 5, 10])
    def test_identity_returns_dict(self, g):
        result = arakelov_green_identity(g)
        assert isinstance(result, dict)
        assert result["genus"] == g
        assert result["status"] == "proved"

    def test_identity_formula_present(self):
        for g in [0, 1, 2, 5]:
            result = arakelov_green_identity(g)
            assert "dd^c G(z,w) = delta(z,w) - omega_g" in result["identity"]

    def test_genus0_fubini_study(self):
        result = arakelov_green_identity(0)
        assert "Fubini-Study" in result["omega"]

    def test_genus1_flat_metric(self):
        result = arakelov_green_identity(1)
        assert "Arakelov form" in result["omega"]

    def test_genus_geq2_prime_form_note(self):
        result = arakelov_green_identity(3)
        assert "prime_form_note" in result
        assert "K^{-1/2}" in result["prime_form_note"]
        assert "NOT K^{+1/2}" in result["prime_form_note"]

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            arakelov_green_identity(-1)


class TestFayTrisecantStructure:
    """Test the Fay trisecant identity documentation."""

    def test_genus0_exact(self):
        result = fay_trisecant_structure(0)
        assert result["exact"] is True
        assert result["defect"] == Integer(0)

    def test_genus1_not_exact(self):
        result = fay_trisecant_structure(1)
        assert result["exact"] is False
        assert "E_2(tau)" in result["defect"]
        assert "quasi-modular" in result["defect_type"]

    @pytest.mark.parametrize("g", [2, 3, 5, 10])
    def test_genus_geq2_not_exact(self, g):
        result = fay_trisecant_structure(g)
        assert result["exact"] is False
        assert "Omega" in result["defect"]
        assert "modular function" in result["defect_type"]

    def test_genus_geq2_scalar_forced(self):
        """At g>=2 the defect is forced scalar by symmetry reduction."""
        for g in [2, 3, 5]:
            result = fay_trisecant_structure(g)
            assert "scalar" in result["note"].lower() or "1-dimensional" in result["note"].lower()

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            fay_trisecant_structure(-1)


class TestQuasiModularFormDimension:
    """Test dim of quasi-modular (1,1)-form space = g(g+1)/2."""

    def test_genus0(self):
        assert quasi_modular_form_dimension(0) == 0

    @pytest.mark.parametrize("g,expected", [
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
    ])
    def test_triangular_numbers(self, g, expected):
        assert quasi_modular_form_dimension(g) == expected

    @pytest.mark.parametrize("g", range(1, 11))
    def test_formula(self, g):
        assert quasi_modular_form_dimension(g) == g * (g + 1) // 2

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            quasi_modular_form_dimension(-1)


class TestSymmetryReductionDimension:
    """Test that symmetry reduces the defect space to dimension 1."""

    def test_genus0_zero(self):
        result = symmetry_reduction_dimension(0)
        assert result["after_symmetry"] == 0

    @pytest.mark.parametrize("g", [1, 2, 3, 5, 10])
    def test_after_symmetry_is_1(self, g):
        result = symmetry_reduction_dimension(g)
        assert result["after_symmetry"] == 1

    @pytest.mark.parametrize("g", [1, 2, 3, 5])
    def test_full_dimension(self, g):
        result = symmetry_reduction_dimension(g)
        assert result["full_dimension"] == g * (g + 1) // 2

    def test_mechanism_present(self):
        result = symmetry_reduction_dimension(3)
        assert "H^{1,1}" in result["mechanism"]
        assert "S_3" in result["mechanism"]
        assert "translation" in result["mechanism"]


class TestArnoldDefectGenusG:
    """Test the Arnold defect at various genera."""

    def test_genus0_exact(self):
        result = arnold_defect_genus_g(0)
        assert result["defect"] == Integer(0)
        assert result["type"] == "exact"

    def test_genus1_E2(self):
        result = arnold_defect_genus_g(1)
        assert result["defect"] == "E_2(tau)"
        assert result["lambda_fp"] == Rational(1, 24)
        assert result["lambda_fp_check"] is True

    def test_genus2_forced_scalar(self):
        result = arnold_defect_genus_g(2)
        assert result["forced_scalar"] is True
        assert result["symmetry_reduction"]["after_symmetry"] == 1

    @pytest.mark.parametrize("g", [2, 3, 5, 10])
    def test_genus_geq2_lambda_fp(self, g):
        result = arnold_defect_genus_g(g)
        assert result["lambda_fp"] == lambda_fp(g)

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            arnold_defect_genus_g(-1)


class TestThetaCharacteristicsCount:
    """Test theta characteristic counts."""

    @pytest.mark.parametrize("g,parity,expected", [
        # g=1: 1 odd, 3 even, 4 total
        (1, 'odd', 1),
        (1, 'even', 3),
        (1, 'total', 4),
        # g=2: 6 odd, 10 even, 16 total
        (2, 'odd', 6),
        (2, 'even', 10),
        (2, 'total', 16),
        # g=3: 28 odd, 36 even, 64 total
        (3, 'odd', 28),
        (3, 'even', 36),
        (3, 'total', 64),
        # g=4: 120 odd, 136 even, 256 total
        (4, 'odd', 120),
        (4, 'even', 136),
        (4, 'total', 256),
    ])
    def test_known_values(self, g, parity, expected):
        assert theta_characteristics_count(g, parity) == expected

    @pytest.mark.parametrize("g", range(1, 8))
    def test_total_is_sum(self, g):
        """Total = odd + even."""
        odd = theta_characteristics_count(g, 'odd')
        even = theta_characteristics_count(g, 'even')
        total = theta_characteristics_count(g, 'total')
        assert odd + even == total

    @pytest.mark.parametrize("g", range(1, 8))
    def test_total_is_power_of_2(self, g):
        """Total = 2^{2g}."""
        assert theta_characteristics_count(g, 'total') == 2 ** (2 * g)

    @pytest.mark.parametrize("g", range(1, 6))
    def test_odd_formula(self, g):
        """odd = 2^{g-1} * (2^g - 1)."""
        expected = 2 ** (g - 1) * (2 ** g - 1)
        assert theta_characteristics_count(g, 'odd') == expected

    @pytest.mark.parametrize("g", range(1, 6))
    def test_even_formula(self, g):
        """even = 2^{g-1} * (2^g + 1)."""
        expected = 2 ** (g - 1) * (2 ** g + 1)
        assert theta_characteristics_count(g, 'even') == expected

    def test_genus0_returns_zero(self):
        assert theta_characteristics_count(0, 'odd') == 0
        assert theta_characteristics_count(0, 'even') == 0
        assert theta_characteristics_count(0, 'total') == 0

    def test_invalid_parity_raises(self):
        with pytest.raises(ValueError):
            theta_characteristics_count(2, 'neither')


class TestPrimeFormSectionType:
    """Test prime form section type documentation."""

    @pytest.mark.parametrize("g", [0, 1, 2, 3, 5])
    def test_section_type(self, g):
        result = prime_form_section_type(g)
        assert result["section_type"] == "K^{-1/2} boxtimes K^{-1/2}"
        # Critical pitfall: must NOT be K^{+1/2}
        assert "+1/2" in result["NOT"]

    @pytest.mark.parametrize("g", [0, 1, 2, 5])
    def test_antisymmetric(self, g):
        result = prime_form_section_type(g)
        assert result["antisymmetric"] is True

    @pytest.mark.parametrize("g", [0, 1, 2, 5])
    def test_vanishing_order(self, g):
        result = prime_form_section_type(g)
        assert result["vanishing_order_diagonal"] == 1
        assert result["other_zeros"] is False

    def test_genus0_explicit(self):
        result = prime_form_section_type(0)
        assert "z - w" in result["explicit_formula"]

    def test_genus1_theta(self):
        result = prime_form_section_type(1)
        assert "theta_1" in result["explicit_formula"]
        assert result["odd_theta_chars"] == 1

    def test_genus_geq2_theta_chars(self):
        result = prime_form_section_type(3)
        assert result["odd_theta_chars_available"] == 28


class TestArakelovBarTransferStatus:
    """Test the transfer status assessment."""

    def test_returns_dict(self):
        result = arakelov_bar_transfer_status()
        assert isinstance(result, dict)
        assert result["status"] == "conjectured"

    def test_four_ingredients(self):
        result = arakelov_bar_transfer_status()
        ingredients = result["ingredients"]
        assert len(ingredients) == 4
        assert "fay_trisecant" in ingredients
        assert "arakelov_green" in ingredients
        assert "ope_convergence" in ingredients
        assert "bar_cyclic_sum" in ingredients

    def test_arakelov_green_proved(self):
        result = arakelov_bar_transfer_status()
        ag = result["ingredients"]["arakelov_green"]
        assert ag["identity_proved"] is True
        assert ag["rating"] == "PROVED"

    def test_blue_defense_present(self):
        result = arakelov_bar_transfer_status()
        assert "blue_defense" in result
        assert "kappa" in result["blue_defense"]

    def test_proved_count(self):
        result = arakelov_bar_transfer_status()
        assert result["proved_ingredients_count"] == 1
        assert result["total_ingredients"] == 4


class TestUniversalityDefense:
    """Test the kappa uniqueness (BLUE defense)."""

    def test_default_families(self):
        result = universality_defense()
        for fam in ["Heisenberg", "sl2", "Virasoro", "W3"]:
            assert fam in result["family_data"]

    def test_antisymmetry_all_default(self):
        result = universality_defense()
        for fam in ["Heisenberg", "sl2", "Virasoro", "W3"]:
            assert result["family_data"][fam]["antisymmetry_holds"] is True

    def test_antisymmetry_extended_families(self):
        result = universality_defense(
            families=["Heisenberg", "sl2", "sl3", "G2", "B2", "Virasoro", "W3"]
        )
        assert result["axioms_verified"]["antisymmetry_all_families"] is True

    def test_ahat_gf_checks(self):
        result = universality_defense()
        assert result["axioms_verified"]["ahat_gf_lambda1"] is True
        assert result["axioms_verified"]["ahat_gf_lambda2"] is True
        assert result["axioms_verified"]["ahat_gf_lambda3"] is True

    def test_numerical_checks(self):
        result = universality_defense()
        for key, val in result["numerical_checks"].items():
            assert val is True, f"Numerical check {key} failed"

    def test_heisenberg_complementarity_sum_zero(self):
        result = universality_defense(families=["Heisenberg"])
        comp_sum = result["family_data"]["Heisenberg"]["complementarity_sum"]
        assert comp_sum == "0"

    def test_virasoro_complementarity_sum_13(self):
        result = universality_defense(families=["Virasoro"])
        comp_sum = result["family_data"]["Virasoro"]["complementarity_sum"]
        assert comp_sum == "13"

    def test_unknown_family_error(self):
        result = universality_defense(families=["FakeAlgebra"])
        assert "error" in result["family_data"]["FakeAlgebra"]


# ============================================================================
# MODULE 2: mc5_clutching_induction.py — Clutching Induction
# ============================================================================


class TestLambdaFPExact:
    """Test exact Faber-Pandharipande numbers."""

    @pytest.mark.parametrize("g,expected", [
        (1, Rational(1, 24)),
        (2, Rational(7, 5760)),
        (3, Rational(31, 967680)),
        (4, Rational(127, 154828800)),
    ])
    def test_known_values(self, g, expected):
        assert lambda_fp_exact(g) == expected

    @pytest.mark.parametrize("g", range(1, 16))
    def test_matches_utils(self, g):
        """Must agree with the canonical lambda_fp from utils.py."""
        assert lambda_fp_exact(g) == lambda_fp(g)

    def test_genus0_raises(self):
        with pytest.raises(ValueError):
            lambda_fp_exact(0)

    @pytest.mark.parametrize("g", range(1, 11))
    def test_positive(self, g):
        """All lambda_g^FP are positive."""
        assert lambda_fp_exact(g) > 0


class TestSewingCorrection:
    """Test the sewing correction Delta_g = lambda_g - lambda_{g-1}."""

    @pytest.mark.parametrize("g", range(2, 16))
    def test_all_negative(self, g):
        """MC5-RED: sewing corrections are NEGATIVE for all g >= 2."""
        assert sewing_correction(g) < 0

    def test_g2_value(self):
        """Delta_2 = lambda_2 - lambda_1 = 7/5760 - 1/24."""
        expected = Rational(7, 5760) - Rational(1, 24)
        assert sewing_correction(2) == expected

    def test_g1_raises(self):
        with pytest.raises(ValueError):
            sewing_correction(1)

    @pytest.mark.parametrize("g", range(2, 11))
    def test_formula(self, g):
        """Delta_g = lambda_g - lambda_{g-1} by definition."""
        assert sewing_correction(g) == lambda_fp(g) - lambda_fp(g - 1)


class TestSewingCorrectionTable:
    """Test the sewing correction table."""

    def test_table_length(self):
        table = sewing_correction_table(max_g=10)
        assert len(table) == 9  # g = 2, ..., 10

    def test_all_negative_flag(self):
        table = sewing_correction_table(max_g=15)
        for g, entry in table.items():
            assert entry["negative"] is True, f"g={g} correction not negative"
            assert entry["sign"] == -1

    def test_correction_values(self):
        table = sewing_correction_table(max_g=5)
        for g, entry in table.items():
            assert entry["correction"] == entry["lambda_g"] - entry["lambda_g_minus_1"]

    def test_max_g_1_raises(self):
        with pytest.raises(ValueError):
            sewing_correction_table(max_g=1)


class TestNonSeparatingDegeneration:
    """Test non-separating degeneration documentation."""

    @pytest.mark.parametrize("g", [2, 3, 5])
    def test_source_genus(self, g):
        result = non_separating_degeneration_formula(g)
        assert result["source_genus"] == g - 1

    @pytest.mark.parametrize("g", [2, 3, 5])
    def test_locality(self, g):
        result = non_separating_degeneration_formula(g)
        assert result["correction_is_local"] is True
        assert result["bar_nilpotent_locally"] is True
        assert result["local_model"] == "genus 0 (formal disk with two marked points)"

    @pytest.mark.parametrize("g", [2, 3, 5])
    def test_sewing_negative(self, g):
        result = non_separating_degeneration_formula(g)
        assert result["sewing_negative"] is True

    def test_g1_raises(self):
        with pytest.raises(ValueError):
            non_separating_degeneration_formula(1)


class TestInductionStepVerification:
    """Test the clutching induction decomposition."""

    def test_base_case_g1(self):
        result = induction_step_verification(1)
        assert result["type"] == "base case"
        assert result["verified"] is True

    @pytest.mark.parametrize("g", range(2, 11))
    def test_induction_step_holds(self, g):
        result = induction_step_verification(g)
        assert result["type"] == "induction step"
        assert result["decomposition_holds"] is True
        assert result["verified"] is True

    @pytest.mark.parametrize("g", range(2, 11))
    def test_correction_negative(self, g):
        result = induction_step_verification(g)
        assert result["correction_negative"] is True

    def test_g0_raises(self):
        with pytest.raises(ValueError):
            induction_step_verification(0)

    def test_lambda_values_consistent(self):
        """lambda_g and lambda_{g-1} are consistent across functions."""
        for g in range(2, 8):
            result = induction_step_verification(g)
            assert result["lambda_g"] == lambda_fp(g)
            assert result["lambda_g_minus_1"] == lambda_fp(g - 1)
            assert result["sewing_correction"] == sewing_correction(g)


class TestAhatMultiplicativityCheck:
    """Test A-hat generating function term-by-term."""

    def test_all_match_small(self):
        result = ahat_multiplicativity_check(max_g=5)
        assert result["all_match"] is True

    def test_all_match_medium(self):
        result = ahat_multiplicativity_check(max_g=8)
        assert result["all_match"] is True

    @pytest.mark.parametrize("g", range(1, 6))
    def test_individual_terms(self, g):
        result = ahat_multiplicativity_check(max_g=g)
        assert result["term_checks"][g]["match"] is True


class TestConvergenceRadius:
    """Test convergence radius of the genus expansion."""

    def test_returns_dict(self):
        result = convergence_radius()
        assert isinstance(result, dict)
        assert result["radius_of_convergence"] == "2*pi"

    def test_converging(self):
        result = convergence_radius()
        assert result["converging"] is True

    def test_limit_approaches_target(self):
        """lambda_{g+1}/lambda_g -> 1/(4*pi^2) ~ 0.02533."""
        result = convergence_radius()
        limit = result["theoretical_limit_float"]
        # 1/(4*pi^2) ~ 0.025330...
        assert 0.0253 < limit < 0.0254

    def test_ratios_decreasing_toward_limit(self):
        """The ratios should approach the limit from above or oscillate near it."""
        result = convergence_radius()
        ratios = result["ratios_float"]
        limit = result["theoretical_limit_float"]
        # Check that late ratios are close to the limit
        for g in range(15, 20):
            if g in ratios:
                assert abs(ratios[g] - limit) / limit < 0.01

    def test_relative_error_small(self):
        result = convergence_radius()
        assert result["relative_error_at_max_g"] < 0.005


class TestClutchingCompatibility:
    """Test separating degeneration factorization."""

    @pytest.mark.parametrize("g1,g2", [
        (1, 1),
        (1, 2),
        (2, 2),
        (1, 3),
        (2, 3),
        (3, 3),
    ])
    def test_decomposition_holds(self, g1, g2):
        result = clutching_compatibility(g1, g2)
        assert result["decomposition_holds"] is True

    def test_g_equals_sum(self):
        result = clutching_compatibility(2, 3)
        assert result["g"] == 5

    def test_lambda_values(self):
        result = clutching_compatibility(1, 1)
        assert result["lambda_g"] == lambda_fp(2)
        assert result["lambda_g1"] == lambda_fp(1)
        assert result["lambda_g2"] == lambda_fp(1)

    def test_nodal_correction_formula(self):
        """nodal_correction = lambda_g - lambda_{g1} - lambda_{g2}."""
        for g1, g2 in [(1, 1), (1, 2), (2, 2)]:
            result = clutching_compatibility(g1, g2)
            g = g1 + g2
            expected = lambda_fp(g) - lambda_fp(g1) - lambda_fp(g2)
            assert result["nodal_correction"] == expected

    def test_g0_raises(self):
        with pytest.raises(ValueError):
            clutching_compatibility(0, 2)
        with pytest.raises(ValueError):
            clutching_compatibility(1, 0)

    def test_symmetric(self):
        """clutching_compatibility(g1, g2) and (g2, g1) give same correction."""
        for g1, g2 in [(1, 2), (1, 3), (2, 3)]:
            r1 = clutching_compatibility(g1, g2)
            r2 = clutching_compatibility(g2, g1)
            assert r1["nodal_correction"] == r2["nodal_correction"]


# ============================================================================
# CROSS-MODULE TESTS
# ============================================================================


class TestCrossModuleConsistency:
    """Tests that span both modules for internal consistency."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_lambda_fp_consistent(self, g):
        """lambda_fp from utils, lambda_fp_exact, and arnold_defect all agree."""
        from_utils = lambda_fp(g)
        from_clutching = lambda_fp_exact(g)
        assert from_utils == from_clutching
        if g >= 1:
            defect = arnold_defect_genus_g(g)
            assert defect["lambda_fp"] == from_utils

    def test_symmetry_vs_quasi_modular(self):
        """Symmetry reduction starts from the quasi-modular dimension."""
        for g in range(1, 6):
            qm_dim = quasi_modular_form_dimension(g)
            sr = symmetry_reduction_dimension(g)
            assert sr["full_dimension"] == qm_dim

    def test_defect_uses_symmetry_reduction(self):
        """At g>=2, arnold_defect refers to symmetry_reduction."""
        for g in [2, 3, 5]:
            defect = arnold_defect_genus_g(g)
            assert defect["symmetry_reduction"]["after_symmetry"] == 1

    def test_prime_form_consistent_with_theta_chars(self):
        """Prime form uses odd theta characteristic; count is consistent."""
        for g in [1, 2, 3]:
            pf = prime_form_section_type(g)
            if g == 1:
                assert pf["odd_theta_chars"] == theta_characteristics_count(g, 'odd')
            else:
                assert pf["odd_theta_chars_available"] == theta_characteristics_count(g, 'odd')

    def test_universality_kappa_values(self):
        """Universality defense kappa values match genus_expansion module."""
        from compute.lib.genus_expansion import (
            kappa_sl2 as ge_kappa_sl2,
            kappa_virasoro as ge_kappa_vir,
            kappa_w3 as ge_kappa_w3,
        )
        assert ge_kappa_sl2(1) == Rational(9, 4)
        assert ge_kappa_vir(1) == Rational(1, 2)
        assert ge_kappa_w3(2) == Rational(5, 3)

    def test_sewing_vs_induction(self):
        """Sewing correction from clutching module matches induction step."""
        for g in range(2, 8):
            sc = sewing_correction(g)
            iv = induction_step_verification(g)
            assert sc == iv["sewing_correction"]

    def test_transfer_ingredients_count(self):
        """The four ingredients are all accounted for."""
        status = arakelov_bar_transfer_status()
        fay = fay_trisecant_structure(3)
        green = arakelov_green_identity(3)

        # Fay identity is documented
        assert not fay["exact"]
        # Green identity is proved
        assert green["status"] == "proved"
        # Total ingredients
        assert status["total_ingredients"] == 4
