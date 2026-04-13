r"""Tests for Vol II Part I rectification engine.

50+ tests verifying the core claims of Vol II Part I:
ordered bar = E_1 coalgebra on FM_k(C) x Conf_k(R), with the
Swiss-cheese datum on the derived-center pair.

Test structure follows the multi-path verification mandate:
every claim verified by at least 2 independent paths.
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_vol2_swiss_cheese_rectification_engine import (
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine,
    kappa_wn,
    arnold_relation_genus0,
    curvature_from_arnold_defect,
    verify_heisenberg_curvature_genus1,
    verify_affine_curvature_genus1,
    ope_to_lambda_bracket,
    verify_virasoro_lambda_bracket,
    collision_residue_pole_orders,
    verify_ap19_virasoro,
    verify_ap19_affine,
    verify_swiss_cheese_directionality,
    verify_three_models,
    verify_pva_descent,
    verify_cdg_compatibility,
    verify_moriwaki_compatibility,
    verify_koszul_decomposition,
    verify_desuspension_convention,
    verify_shadow_depth_classification,
    verify_cross_volume_kappa,
    verify_heisenberg_genus1_partition_function,
    verify_bulk_identification,
    run_all_verifications,
)


# ============================================================================
# Section 1: Modular characteristics (AP1 cross-check)
# ============================================================================

class TestModularCharacteristics:
    """Verify kappa formulas for all standard families."""

    def test_kappa_heisenberg_level_1(self):
        assert kappa_heisenberg(1) == 1

    def test_kappa_heisenberg_level_k(self):
        for k in [1, 2, 3, -1, Fraction(1, 2)]:
            assert kappa_heisenberg(k) == k

    def test_kappa_virasoro_c26(self):
        assert kappa_virasoro(26) == 13

    def test_kappa_virasoro_c0(self):
        assert kappa_virasoro(0) == 0

    def test_kappa_virasoro_c13_self_dual(self):
        """At c=13, Vir_c is self-dual: kappa = 13/2."""
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_kappa_affine_sl2_k1(self):
        """sl_2: dim=3, h^v=2. kappa = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_affine(3, 1, 2) == Fraction(9, 4)

    def test_kappa_affine_sl2_critical(self):
        """At critical level k=-h^v=-2: kappa = 3*(0)/(4) = 0 (bar complex flat)."""
        assert kappa_affine(3, -2, 2) == 0

    def test_kappa_affine_sl3_k1(self):
        """sl_3: dim=8, h^v=3. kappa = 8*(1+3)/(2*3) = 32/6 = 16/3."""
        assert kappa_affine(8, 1, 3) == Fraction(16, 3)

    def test_kappa_affine_e8_k1(self):
        """E_8: dim=248, h^v=30. kappa = 248*(1+30)/(2*30) = 248*31/60."""
        expected = Fraction(248 * 31, 60)
        assert kappa_affine(248, 1, 30) == expected

    def test_kappa_wn_virasoro_N2(self):
        """W_2 = Virasoro. H_2 = 1 + 1/2 = 3/2. kappa = c*(3/2 - 1) = c/2.
        Must match kappa_virasoro."""
        c = 26
        assert kappa_wn(c, 2) == kappa_virasoro(c)

    def test_kappa_wn_w3(self):
        """W_3: H_3 = 1 + 1/2 + 1/3 = 11/6. kappa = c*(11/6 - 1) = 5c/6."""
        c = Fraction(100)  # c=100 is the critical string for W_3
        expected = c * Fraction(5, 6)
        assert kappa_wn(c, 3) == expected


# ============================================================================
# Section 2: AP39 - kappa != c/2 for non-Virasoro families
# ============================================================================

class TestAP39:
    """kappa and c/2 are distinct invariants that coincide only for rank-1 algebras."""

    def test_ap39_sl2_kappa_neq_c_over_2(self):
        """For sl_2 at k=1: c = 3*1/(1+2) = 1, c/2 = 1/2. kappa = 9/4 != 1/2."""
        dim_g, k, h_dual = 3, 1, 2
        kappa = kappa_affine(dim_g, k, h_dual)
        c = Fraction(k * dim_g, k + h_dual)
        assert kappa != Fraction(c, 2), f"AP39 violation: kappa={kappa} = c/2={c/2}"

    def test_ap39_sl3_kappa_neq_c_over_2(self):
        dim_g, k, h_dual = 8, 1, 3
        kappa = kappa_affine(dim_g, k, h_dual)
        c = Fraction(k * dim_g, k + h_dual)
        assert kappa != Fraction(c, 2)

    def test_ap39_heisenberg_kappa_eq_c_over_2(self):
        """For Heisenberg at level k: c = 1, kappa = k. c/2 = 1/2.
        kappa = c/2 only when k = 1/2, NOT in general."""
        # At k=1: kappa=1, c/2=1/2 -> not equal
        assert kappa_heisenberg(1) != Fraction(1, 2)
        # At k=1/2: kappa=1/2, c/2=1/2 -> equal (special case)
        assert kappa_heisenberg(Fraction(1, 2)) == Fraction(1, 2)


# ============================================================================
# Section 3: Arnold relation (genus 0)
# ============================================================================

class TestArnoldRelation:
    """The Arnold relation ensures d^2 = 0 at genus 0."""

    def test_arnold_all_paths_verified(self):
        result = arnold_relation_genus0()
        assert result["d_squared_zero_genus_0"]

    def test_arnold_partial_fraction(self):
        result = arnold_relation_genus0()
        assert result["partial_fraction_identity"]

    def test_arnold_topological(self):
        result = arnold_relation_genus0()
        assert result["topological_H2"]


# ============================================================================
# Section 4: Curvature d_fib^2 = kappa * omega_g
# ============================================================================

class TestCurvature:
    """The curvature at genus g >= 1 is kappa * omega_g."""

    def test_curvature_genus_0_vanishes(self):
        curv, coeff = curvature_from_arnold_defect(1, 0)
        assert curv == 0 and coeff == 0

    def test_curvature_genus_1_heisenberg(self):
        result = verify_heisenberg_curvature_genus1(1)
        assert result["all_paths_agree"]
        assert result["curvature_is_kappa_omega_1"]

    def test_curvature_genus_1_heisenberg_level_k(self):
        for k in [1, 2, 3, 5]:
            result = verify_heisenberg_curvature_genus1(k)
            assert result["path1_residue"] == k
            assert result["all_paths_agree"]

    def test_curvature_genus_1_sl2(self):
        result = verify_affine_curvature_genus1(3, 1, 2)
        assert result["all_paths_agree"]
        assert result["kappa_value"] == Fraction(9, 4)

    def test_curvature_genus_1_sl2_critical(self):
        """At critical level, kappa = 0 and bar complex is flat."""
        result = verify_affine_curvature_genus1(3, -2, 2)
        assert result["kappa_value"] == 0

    def test_curvature_ap39_check(self):
        result = verify_affine_curvature_genus1(3, 1, 2)
        assert result["AP39_kappa_neq_c_over_2"]

    def test_curvature_general_genus(self):
        """d_fib^2 = kappa * omega_g for any genus g >= 1."""
        kappa = Fraction(9, 4)
        for g in [1, 2, 3, 5]:
            curv, coeff = curvature_from_arnold_defect(kappa, g)
            assert coeff == kappa


# ============================================================================
# Section 5: AP44 - OPE to lambda-bracket conversion
# ============================================================================

class TestAP44:
    """Lambda-bracket coefficient at order n is a_{(n)}b / n!, NOT a_{(n)}b."""

    def test_ap44_virasoro_lambda_bracket(self):
        result = verify_virasoro_lambda_bracket(26)
        assert result["AP44_verified"]

    def test_ap44_order_3_factor_6(self):
        """The critical check: c/2 in OPE becomes c/12 in lambda-bracket."""
        result = verify_virasoro_lambda_bracket(26)
        assert result["correct_value_c_over_12"] == Fraction(26, 12)
        assert result["wrong_value_c_over_2"] == Fraction(26, 2)
        assert result["correct_value_c_over_12"] != result["wrong_value_c_over_2"]

    def test_ap44_general_conversion(self):
        """Test the general OPE -> lambda-bracket conversion."""
        ope = {0: 6, 1: 12, 2: 24, 3: 120}
        lam = ope_to_lambda_bracket(ope)
        assert lam[0] == 6       # 6/0! = 6
        assert lam[1] == 12      # 12/1! = 12
        assert lam[2] == 12      # 24/2! = 12
        assert lam[3] == 20      # 120/3! = 20

    def test_ap44_fractional(self):
        ope = {3: Fraction(1, 2)}
        lam = ope_to_lambda_bracket(ope)
        assert lam[3] == Fraction(1, 12)  # (1/2)/6 = 1/12


# ============================================================================
# Section 6: AP19 - Bar kernel pole absorption
# ============================================================================

class TestAP19:
    """The d log kernel absorbs one pole order."""

    def test_ap19_virasoro(self):
        result = verify_ap19_virasoro()
        assert result["AP19_verified"]
        assert result["no_even_poles_in_r_matrix"]

    def test_ap19_affine(self):
        result = verify_ap19_affine()
        assert result["AP19_verified"]

    def test_ap19_pole_reduction(self):
        """General test: pole order n -> n-1 after d log absorption."""
        assert collision_residue_pole_orders([4, 2, 1]) == [3, 1]
        assert collision_residue_pole_orders([2, 1]) == [1]
        assert collision_residue_pole_orders([1]) == []  # simple pole absorbed completely

    def test_ap19_heisenberg_trivial(self):
        """Heisenberg has OPE pole order 2 (double pole for the pairing).
        After absorption: pole order 1 in r-matrix = Omega/z."""
        assert collision_residue_pole_orders([2]) == [1]


# ============================================================================
# Section 7: Swiss-cheese directionality
# ============================================================================

class TestDirectionality:
    """The Swiss-cheese operad has strict bulk-to-boundary directionality."""

    def test_no_open_to_closed(self):
        result = verify_swiss_cheese_directionality()
        assert result["open_to_closed_empty"]

    def test_closed_to_open_exists(self):
        result = verify_swiss_cheese_directionality()
        assert result["closed_to_open_exists"]

    def test_genus_0_strict(self):
        result = verify_swiss_cheese_directionality()
        assert result["genus_0_strict_directionality"]


# ============================================================================
# Section 8: Three models
# ============================================================================

class TestThreeModels:
    """The three chain-level models of the genus-g bar complex."""

    def test_three_models_genus_0_all_flat(self):
        result = verify_three_models(1, 0)
        for name, model in result["models"].items():
            assert model["d_squared"] == 0

    def test_three_models_genus_1_curved(self):
        result = verify_three_models(1, 1)
        assert result["models"]["model_iii_curved"]["d_squared"] == 1  # kappa=1

    def test_three_models_gauge_equivalent(self):
        result = verify_three_models(1, 1)
        assert result["gauge_equivalent"]

    def test_curved_requires_coderived(self):
        result = verify_three_models(1, 1)
        assert result["curved_requires_coderived"]

    def test_flat_models_agree(self):
        result = verify_three_models(1, 1)
        assert result["flat_models_agree"]


# ============================================================================
# Section 9: PVA descent
# ============================================================================

class TestPVADescent:
    """H*(A, Q) is a (-1)-shifted PVA."""

    def test_pva_product_commutative(self):
        result = verify_pva_descent()
        assert result["product_commutative"]

    def test_pva_bracket_jacobi(self):
        result = verify_pva_descent()
        assert result["bracket_jacobi"]

    def test_pva_shift_minus_1(self):
        result = verify_pva_descent()
        assert result["shift"] == -1

    def test_pva_higher_ops_vanish(self):
        result = verify_pva_descent()
        assert result["higher_ops_vanish"]

    def test_pva_matches_cdg_shifted_poisson(self):
        result = verify_pva_descent()
        assert result["matches_CDG_shifted_poisson"]


# ============================================================================
# Section 10: CDG compatibility
# ============================================================================

class TestCDGCompatibility:
    """Compatibility with Costello-Dimofte-Gaiotto [2005.00083]."""

    def test_cdg_bulk_compatible(self):
        result = verify_cdg_compatibility()
        assert result["bulk_algebra"]["compatible"]

    def test_cdg_shift_matches(self):
        result = verify_cdg_compatibility()
        assert result["bulk_algebra"]["shift_matches"]

    def test_cdg_boundary_module(self):
        result = verify_cdg_compatibility()
        assert result["boundary_module"]["compatible"]

    def test_cdg_directionality(self):
        result = verify_cdg_compatibility()
        assert result["directionality"]["compatible"]


# ============================================================================
# Section 11: Moriwaki compatibility
# ============================================================================

class TestMoriwakiCompatibility:
    """Compatibility with Moriwaki [2410.02648]."""

    def test_moriwaki_convergence_compatible(self):
        result = verify_moriwaki_compatibility()
        assert result["ope_convergence"]["compatible"]

    def test_moriwaki_strengthens_vol2(self):
        result = verify_moriwaki_compatibility()
        assert result["ope_convergence"]["strengthens_vol2"]

    def test_moriwaki_swiss_cheese_compatible(self):
        result = verify_moriwaki_compatibility()
        assert result["swiss_cheese_action"]["compatible"]


# ============================================================================
# Section 12: Koszul decomposition
# ============================================================================

class TestKoszulDecomposition:
    """Koszul duality decomposes along C x R."""

    def test_kunneth_holds(self):
        result = verify_koszul_decomposition()
        assert result["kunneth_holds"]

    def test_r_direction_e1(self):
        result = verify_koszul_decomposition()
        assert result["R_direction"]["type"] == "E_1 Koszul duality"

    def test_c_direction_chiral(self):
        result = verify_koszul_decomposition()
        assert result["C_direction"]["type"] == "chiral Koszul duality"


# ============================================================================
# Section 13: AP45 desuspension
# ============================================================================

class TestAP45:
    """Desuspension lowers degree by 1."""

    def test_desuspension_convention(self):
        result = verify_desuspension_convention()
        assert result["AP45_verified"]

    def test_desuspension_lowers(self):
        result = verify_desuspension_convention()
        assert result["deg_s_inv_J"] == 0  # |s^{-1}J| = |J| - 1 = 1 - 1 = 0


# ============================================================================
# Section 14: Shadow depth classification
# ============================================================================

class TestShadowDepth:
    """The four-class shadow depth classification."""

    def test_all_classes_koszul(self):
        result = verify_shadow_depth_classification()
        assert result["all_classes_koszul"]

    def test_depth_not_koszulness(self):
        result = verify_shadow_depth_classification()
        assert result["depth_classifies_complexity_not_koszulness"]

    def test_class_G_terminates(self):
        result = verify_shadow_depth_classification()
        assert result["classification"]["G"]["r_max"] == 2

    def test_class_M_infinite(self):
        result = verify_shadow_depth_classification()
        assert result["classification"]["M"]["r_max"] == float('inf')


# ============================================================================
# Section 15: Cross-volume kappa consistency (AP49)
# ============================================================================

class TestCrossVolume:
    """Cross-volume consistency checks."""

    def test_cross_volume_heisenberg(self):
        result = verify_cross_volume_kappa()
        assert result["Heisenberg"]["match"]

    def test_cross_volume_virasoro(self):
        result = verify_cross_volume_kappa()
        assert result["Virasoro"]["match"]

    def test_cross_volume_affine(self):
        result = verify_cross_volume_kappa()
        assert result["Affine_KM"]["match"]

    def test_cross_volume_sl2_numerical(self):
        result = verify_cross_volume_kappa()
        assert result["sl2_k1"]["match"]


# ============================================================================
# Section 16: Genus-1 Heisenberg partition function
# ============================================================================

class TestHeisenbergGenus1:
    """Genus-1 Heisenberg verification."""

    def test_partition_function_level_1(self):
        result = verify_heisenberg_genus1_partition_function(1)
        assert result["match"]
        assert result["free_energy_F1"] == Fraction(1, 24)

    def test_partition_function_level_k(self):
        for k in [1, 2, 3, 5]:
            result = verify_heisenberg_genus1_partition_function(k)
            assert result["match"]
            assert result["free_energy_F1"] == Fraction(k, 24)


# ============================================================================
# Section 17: Bulk identification (AP-OC, AP25, AP34)
# ============================================================================

class TestBulkIdentification:
    """The bulk is the derived center, NOT the bar complex."""

    def test_ap_oc(self):
        result = verify_bulk_identification()
        assert result["AP_OC_verified"]

    def test_ap25(self):
        result = verify_bulk_identification()
        assert result["AP25_verified"]

    def test_ap34(self):
        result = verify_bulk_identification()
        assert result["AP34_verified"]

    def test_bulk_morita_invariant(self):
        result = verify_bulk_identification()
        assert result["bulk_is_morita_invariant"]

    def test_bulk_cohomology_gerstenhaber(self):
        result = verify_bulk_identification()
        assert result["bulk_on_cohomology"] == "Gerstenhaber algebra (= CDG shifted Poisson)"


# ============================================================================
# Section 18: Full suite run
# ============================================================================

class TestFullSuite:
    """Run the full verification suite."""

    def test_full_suite_runs(self):
        results = run_all_verifications()
        assert results is not None
        assert len(results) > 0

    def test_full_suite_kappa_values(self):
        results = run_all_verifications()
        assert results["kappa_heisenberg_1"] == 1
        assert results["kappa_virasoro_26"] == 13
        assert results["kappa_sl2_1"] == Fraction(9, 4)


# ============================================================================
# Section 19: Complementarity checks (AP24)
# ============================================================================

class TestComplementarity:
    """AP24: kappa + kappa! is NOT universally zero."""

    def test_heisenberg_complementarity_zero(self):
        """For Heisenberg: kappa(H_k) + kappa(H_k^!) = k + (-k) = 0."""
        k = 3
        kappa_A = kappa_heisenberg(k)
        kappa_dual = kappa_heisenberg(-k)
        assert kappa_A + kappa_dual == 0

    def test_virasoro_complementarity_13(self):
        """For Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13."""
        c = 10
        kappa_A = kappa_virasoro(c)
        kappa_dual = kappa_virasoro(26 - c)
        assert kappa_A + kappa_dual == 13

    def test_affine_complementarity_zero(self):
        """For affine KM: kappa(g_hat_k) + kappa(g_hat_{-k-2h^v}) = 0.
        This is the Feigin-Frenkel involution k -> -k-2h^v."""
        dim_g, k, h_dual = 3, 1, 2
        kappa_A = kappa_affine(dim_g, k, h_dual)
        kappa_dual = kappa_affine(dim_g, -k - 2 * h_dual, h_dual)
        assert kappa_A + kappa_dual == 0


# ============================================================================
# Section 20: Numerical spot checks
# ============================================================================

class TestNumericalSpotChecks:
    """Specific numerical values from Vol II."""

    def test_virasoro_c26_kappa_13(self):
        """At c=26: kappa = 13 (critical string)."""
        assert kappa_virasoro(26) == 13

    def test_virasoro_c0_kappa_0(self):
        """At c=0: kappa = 0 (uncurved)."""
        assert kappa_virasoro(0) == 0

    def test_virasoro_c1_kappa_half(self):
        """At c=1: kappa = 1/2."""
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_sl2_k0_vacuum_anomaly(self):
        """At k=0: kappa = dim(g)/2 = 3/2 (pure vacuum anomaly).
        Vol II line 400."""
        assert kappa_affine(3, 0, 2) == Fraction(3, 2)

    def test_e8_k1_kappa(self):
        """E_8 at k=1: kappa = 248*31/60 = 7688/60 = 1922/15."""
        kappa = kappa_affine(248, 1, 30)
        assert kappa == Fraction(248 * 31, 60)
        assert kappa == Fraction(1922, 15)
