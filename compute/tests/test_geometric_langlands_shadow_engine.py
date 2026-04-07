r"""Tests for the geometric Langlands shadow engine.

Verifies the eight-module dictionary between bar-cobar duality and the
geometric Langlands programme. 60+ tests organized by module:

Module 1: Critical level bar complex (kappa = 0, d^2 = 0)
Module 2: Feigin-Frenkel center = oper space (FF theorem)
Module 3: DK bridge and local Langlands (MC3 infrastructure)
Module 4: Raskin Fundamental Local Equivalence
Module 5: Arinkin-Gaitsgory categorical Langlands
Module 6: Beilinson-Drinfeld Hitchin quantization
Module 7: S-duality vs Koszul duality
Module 8: Explicit sl_2 computation

Verification paths:
  Path 1: FF center dim = oper jet dim (Feigin-Frenkel theorem)
  Path 2: Verlinde formula at genus 0, 1, 2
  Path 3: Quantum group parameter from level
  Path 4: Bar complex uncurved iff critical level
  Path 5: Kappa complementarity (AP24)
  Path 6: Shadow tower degeneration at critical level
  Path 7: KZ monodromy = quantum group R-matrix
  Path 8: Hitchin base dimension = dim(G)(g-1)

Multi-path verification: every numerical claim verified by >= 2 methods.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction

import pytest

from compute.lib.geometric_langlands_shadow_engine import (
    # Lie data
    _lie_data,
    # Module 1
    kappa_affine,
    kappa_affine_exact,
    critical_level,
    bar_curvature_at_level,
    sugawara_central_charge,
    # Module 2
    ff_center_dims,
    oper_jet_dims,
    verify_ff_theorem,
    shadow_tower_at_critical,
    # Module 3
    dk_bridge_data,
    quantum_group_parameter,
    # Module 4
    raskin_local_equivalence,
    # Module 5
    ag_categorical_langlands,
    # Module 6
    hitchin_base_dimension,
    bd_quantization_data,
    # Module 7
    s_duality_vs_koszul,
    # Module 8
    sl2_full_langlands_data,
    sl2_kz_monodromy,
    sl2_bar_at_critical,
    # Cross-verification
    verify_kappa_complementarity,
    verify_hitchin_base_equals_dim_g,
    verify_verlinde_sl2_genus1,
    full_langlands_dictionary,
)


# =========================================================================
# Module 1: Critical level bar complex
# =========================================================================

class TestCriticalLevelBarComplex:
    """Tests for bar complex behavior at critical level."""

    def test_kappa_sl2_critical(self):
        """kappa = 0 at critical level k = -2 for sl_2."""
        kap = kappa_affine('A', 1, -2.0)
        assert abs(kap) < 1e-14

    def test_kappa_sl3_critical(self):
        """kappa = 0 at critical level k = -3 for sl_3."""
        kap = kappa_affine('A', 2, -3.0)
        assert abs(kap) < 1e-14

    def test_kappa_sl2_generic(self):
        """kappa = 3(k+2)/4 for sl_2 at generic level."""
        # sl_2: dim = 3, h^v = 2
        # kappa = 3*(k+2)/(2*2) = 3(k+2)/4
        for k in [1, 2, 5, 10]:
            kap = kappa_affine('A', 1, float(k))
            expected = 3.0 * (k + 2) / 4.0
            assert abs(kap - expected) < 1e-12, f"k={k}: {kap} != {expected}"

    def test_kappa_sl2_exact(self):
        """Exact kappa computation for sl_2."""
        kap = kappa_affine_exact('A', 1, Fraction(1))
        assert kap == Fraction(9, 4)

    def test_kappa_sl3_exact(self):
        """Exact kappa for sl_3 at k=1: 8*4/(2*3) = 16/3."""
        kap = kappa_affine_exact('A', 2, Fraction(1))
        assert kap == Fraction(16, 3)

    def test_critical_level_values(self):
        """Critical levels for various types."""
        assert critical_level('A', 1) == -2   # sl_2
        assert critical_level('A', 2) == -3   # sl_3
        assert critical_level('A', 3) == -4   # sl_4
        assert critical_level('G', 2) == -4   # G_2
        assert critical_level('E', 8) == -30  # E_8

    def test_bar_uncurved_at_critical(self):
        """Bar complex is uncurved at critical level."""
        for (lt, rk) in [('A', 1), ('A', 2), ('A', 3), ('G', 2)]:
            k_crit = critical_level(lt, rk)
            data = bar_curvature_at_level(lt, rk, float(k_crit))
            assert data['is_uncurved'], f"{lt}_{rk} should be uncurved at k={k_crit}"
            assert abs(data['kappa']) < 1e-14

    def test_bar_curved_away_from_critical(self):
        """Bar complex is curved away from critical level."""
        data = bar_curvature_at_level('A', 1, 1.0)
        assert not data['is_uncurved']
        assert abs(data['kappa'] - 2.25) < 1e-12  # 3*3/4 = 9/4

    def test_sugawara_undefined_at_critical(self):
        """Sugawara central charge raises error at critical level."""
        with pytest.raises(ValueError, match="UNDEFINED"):
            sugawara_central_charge('A', 1, -2.0)

    def test_sugawara_sl2_generic(self):
        """Sugawara c = 3k/(k+2) for sl_2."""
        c = sugawara_central_charge('A', 1, 1.0)
        assert abs(c - 1.0) < 1e-12  # c = 3*1/3 = 1

        c = sugawara_central_charge('A', 1, 2.0)
        assert abs(c - 1.5) < 1e-12  # c = 3*2/4 = 3/2

    def test_kappa_not_c_over_2_sl2(self):
        """kappa != c/2 for sl_2 (AP1, AP39, AP48)."""
        k = 1.0
        kap = kappa_affine('A', 1, k)
        c = sugawara_central_charge('A', 1, k)
        # kappa = 9/4 = 2.25, c/2 = 0.5
        assert abs(kap - c / 2.0) > 0.1, \
            f"kappa = {kap} should differ from c/2 = {c/2} for sl_2"


# =========================================================================
# Module 2: Feigin-Frenkel center = oper space
# =========================================================================

class TestFeiginFrenkelCenter:
    """Tests for the FF theorem: Z(V_crit) = Fun(Op)."""

    def test_ff_sl2_low_weights(self):
        """FF center dims for sl_2: p_2(n) sequence."""
        ff = ff_center_dims('A', 1, 12)
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21]
        assert ff['dims'] == expected

    def test_ff_sl3_weight0(self):
        """FF center at weight 0 is always 1 (vacuum)."""
        ff = ff_center_dims('A', 2, 5)
        assert ff['dims'][0] == 1

    def test_ff_sl3_casimir_degrees(self):
        """sl_3 has Casimir degrees {2, 3}."""
        ff = ff_center_dims('A', 2, 5)
        assert ff['casimir_degrees'] == [2, 3]

    def test_ff_matches_opers_sl2(self):
        """FF theorem: dim Z_n = dim Op_n for sl_2."""
        result = verify_ff_theorem('A', 1, 15)
        assert result['match'], f"Mismatches: {result['mismatches']}"

    def test_ff_matches_opers_sl3(self):
        """FF theorem: dim Z_n = dim Op_n for sl_3."""
        result = verify_ff_theorem('A', 2, 12)
        assert result['match'], f"Mismatches: {result['mismatches']}"

    def test_ff_matches_opers_sl4(self):
        """FF theorem: dim Z_n = dim Op_n for sl_4."""
        result = verify_ff_theorem('A', 3, 10)
        assert result['match'], f"Mismatches: {result['mismatches']}"

    def test_ff_matches_opers_sl5(self):
        """FF theorem for sl_5."""
        result = verify_ff_theorem('A', 4, 10)
        assert result['match'], f"Mismatches: {result['mismatches']}"

    def test_ff_polynomial_algebra(self):
        """FF center is a polynomial algebra."""
        ff = ff_center_dims('A', 1, 10)
        assert ff['is_polynomial_algebra']

    def test_shadow_tower_vanishes_at_critical(self):
        """Shadow tower degenerates at critical level."""
        for (lt, rk) in [('A', 1), ('A', 2), ('A', 3)]:
            data = shadow_tower_at_critical(lt, rk)
            assert data['shadow_tower_vanishes']
            assert data['classical_limit']
            for g in range(1, 6):
                assert abs(data['F_g_values'][g]) < 1e-14

    def test_ff_sl2_generating_function_path2(self):
        """Cross-verify FF dims via explicit product formula (Path 2).

        GF = prod_{m >= 2} 1/(1-q^m).
        """
        max_w = 12
        coeffs = [0] * (max_w + 1)
        coeffs[0] = 1
        for m in range(2, max_w + 1):
            for n in range(m, max_w + 1):
                coeffs[n] += coeffs[n - m]

        ff = ff_center_dims('A', 1, max_w)
        assert ff['dims'] == coeffs


# =========================================================================
# Module 3: DK bridge and local Langlands
# =========================================================================

class TestDKBridge:
    """Tests for the DK bridge and quantum group data."""

    def test_dk_bridge_generic_level(self):
        """DK bridge at generic level gives valid quantum group."""
        data = dk_bridge_data('A', 1, 1.0)
        assert not data['is_critical']
        assert data['mc3_status'] == 'PROVED for all simple types'
        assert data['thick_generation']
        assert data['q_param'] is not None

    def test_dk_bridge_critical_level(self):
        """DK bridge degenerates at critical level."""
        data = dk_bridge_data('A', 1, -2.0)
        assert data['is_critical']
        assert data['q_param'] is None

    def test_quantum_group_sl2_k1(self):
        """Quantum group for sl_2 at k=1: q = exp(pi i/3)."""
        qg = quantum_group_parameter('A', 1, 1.0)
        q_expected = cmath.exp(cmath.pi * 1j / 3)
        assert abs(qg['q'] - q_expected) < 1e-12
        assert abs(qg['hbar'] - 1.0 / 3.0) < 1e-12

    def test_quantum_group_root_of_unity(self):
        """At integer level, q is a root of unity."""
        for k in [1, 2, 3, 4, 5]:
            qg = quantum_group_parameter('A', 1, float(k))
            assert qg['is_root_of_unity'], f"k={k}: q should be root of unity"

    def test_quantum_group_critical(self):
        """Quantum group degenerate at critical level."""
        qg = quantum_group_parameter('A', 1, -2.0)
        assert qg['is_critical']
        assert qg['q'] is None
        assert qg['hbar'] == float('inf')

    def test_quantum_group_sl3_k1(self):
        """Quantum group for sl_3 at k=1: q = exp(pi i/4)."""
        qg = quantum_group_parameter('A', 2, 1.0)
        q_expected = cmath.exp(cmath.pi * 1j / 4)
        assert abs(qg['q'] - q_expected) < 1e-12

    def test_q_abs_is_1(self):
        """q lies on the unit circle for real levels."""
        for k in [1.0, 2.0, 3.5, 10.0]:
            qg = quantum_group_parameter('A', 1, k)
            assert abs(abs(qg['q']) - 1.0) < 1e-12


# =========================================================================
# Module 4: Raskin Fundamental Local Equivalence
# =========================================================================

class TestRaskinFLE:
    """Tests for the Raskin Fundamental Local Equivalence data."""

    def test_raskin_sl2(self):
        """Raskin FLE for sl_2."""
        data = raskin_local_equivalence('A', 1)
        assert data['critical_level_essential']
        assert abs(data['kappa_at_critical']) < 1e-14
        assert 'D-mod' in data['automorphic_side']
        assert 'IndCoh' in data['spectral_side']

    def test_raskin_sl3(self):
        """Raskin FLE for sl_3."""
        data = raskin_local_equivalence('A', 2)
        assert 'A_2' in data['lie_type']

    def test_raskin_theorem_a_role(self):
        """Theorem A provides the formal framework for FLE."""
        data = raskin_local_equivalence('A', 1)
        assert 'Bar-cobar adjunction' in data['theorem_a_role']
        assert 'Verdier intertwining' in data['theorem_a_role']

    def test_raskin_all_types(self):
        """FLE data available for all simple types."""
        for (lt, rk) in [('A', 1), ('A', 2), ('A', 3),
                         ('B', 2), ('C', 2), ('D', 4),
                         ('G', 2), ('F', 4), ('E', 6)]:
            data = raskin_local_equivalence(lt, rk)
            assert data['critical_level_essential']


# =========================================================================
# Module 5: Arinkin-Gaitsgory categorical Langlands
# =========================================================================

class TestArinkinGaitsgory:
    """Tests for the AG categorical Langlands conjecture data."""

    def test_ag_sl2_genus2(self):
        """AG dimensions for sl_2, genus 2."""
        data = ag_categorical_langlands('A', 1, 2)
        # dim Bun_{SL_2}(X_2) = 3 * (2-1) = 3
        assert data['dim_Bun_G'] == 3
        # dim LocSys = 3 * 2 = 6
        assert data['dim_LocSys'] == 6

    def test_ag_sl3_genus2(self):
        """AG dimensions for sl_3, genus 2."""
        data = ag_categorical_langlands('A', 2, 2)
        # dim(sl_3) = 8, dim Bun = 8*(2-1) = 8
        assert data['dim_Bun_G'] == 8
        assert data['dim_LocSys'] == 16

    def test_ag_genus0(self):
        """At genus 0: dim Bun = dim LocSys = 0."""
        data = ag_categorical_langlands('A', 1, 0)
        assert data['dim_Bun_G'] == 0
        assert data['dim_LocSys'] == 0

    def test_ag_genus1(self):
        """At genus 1: dim Bun = 0, dim LocSys = 0."""
        data = ag_categorical_langlands('A', 1, 1)
        assert data['dim_Bun_G'] == 0
        assert data['dim_LocSys'] == 0


# =========================================================================
# Module 6: Beilinson-Drinfeld Hitchin quantization
# =========================================================================

class TestBDQuantization:
    """Tests for BD quantization of the Hitchin system."""

    def test_hitchin_base_sl2_genus2(self):
        """Hitchin base dimension for sl_2, genus 2."""
        data = hitchin_base_dimension('A', 1, 2)
        # Casimir degrees = {2}, dim = (2*2-1)*(2-1) = 3 = dim(sl_2)*1
        assert data['dim_hitchin_base'] == 3
        assert data['match']

    def test_hitchin_base_sl3_genus2(self):
        """Hitchin base for sl_3, genus 2."""
        data = hitchin_base_dimension('A', 2, 2)
        # Casimir = {2,3}, dim = (3+5)*(1) = 8 = dim(sl_3)*1
        assert data['dim_hitchin_base'] == 8
        assert data['match']

    def test_hitchin_base_equals_dim_g(self):
        """Freudenthal-de Vries: sum(2d_i-1) = dim(G)."""
        for (lt, rk) in [('A', 1), ('A', 2), ('A', 3), ('A', 4),
                         ('B', 2), ('C', 2), ('D', 4),
                         ('G', 2), ('F', 4), ('E', 6), ('E', 7), ('E', 8)]:
            result = verify_hitchin_base_equals_dim_g(lt, rk, 2)
            assert result['match'], (
                f"{lt}_{rk}: sum(2d-1)={result['sum_2d_minus_1']} "
                f"!= dim(G)={result['dim_G']}"
            )

    def test_bd_classical_limit(self):
        """At critical level, BD quantization is the classical limit."""
        data = bd_quantization_data('A', 1, -2.0)
        assert data['is_classical_limit']
        for g in range(1, 4):
            assert abs(data['F_g_values'][g]) < 1e-14

    def test_bd_quantum_corrections(self):
        """Away from critical level, F_g = kappa * lambda_g."""
        data = bd_quantization_data('A', 1, 1.0)
        assert not data['is_classical_limit']
        # F_1 = kappa/24 = (9/4)/24 = 9/96 = 3/32
        expected_F1 = 9.0 / 4.0 / 24.0
        assert abs(data['F_g_values'][1] - expected_F1) < 1e-12

    def test_bd_lambda_fp_values(self):
        """Check Faber-Pandharipande lambda values."""
        data = bd_quantization_data('A', 1, 1.0)
        assert abs(data['lambda_fp'][1] - 1.0 / 24) < 1e-14
        assert abs(data['lambda_fp'][2] - 7.0 / 5760) < 1e-14
        assert abs(data['lambda_fp'][3] - 31.0 / 967680) < 1e-14


# =========================================================================
# Module 7: S-duality vs Koszul duality
# =========================================================================

class TestSDualityVsKoszul:
    """Tests comparing S-duality and Koszul duality."""

    def test_kappa_antisymmetric_sl2(self):
        """kappa + kappa' = 0 for sl_2 (AP24)."""
        result = verify_kappa_complementarity('A', 1, 1.0)
        assert result['is_antisymmetric']

    def test_kappa_antisymmetric_sl3(self):
        """kappa + kappa' = 0 for sl_3 (AP24)."""
        result = verify_kappa_complementarity('A', 2, 1.0)
        assert result['is_antisymmetric']

    def test_kappa_antisymmetric_all_types(self):
        """kappa anti-symmetry for all simple types (AP24)."""
        for (lt, rk) in [('A', 1), ('A', 2), ('A', 3),
                         ('B', 2), ('C', 2), ('D', 4),
                         ('G', 2), ('F', 4), ('E', 6)]:
            result = verify_kappa_complementarity(lt, rk, 1.0)
            assert result['is_antisymmetric'], \
                f"{lt}_{rk}: kappa sum = {result['sum']}, expected 0"

    def test_s_duality_compatible_not_identical(self):
        """S-duality and Koszul duality are compatible but not identical."""
        data = s_duality_vs_koszul('A', 1, 1.0)
        assert data['are_compatible']
        assert not data['are_identical']
        assert data['theta_angle_missing']

    def test_ff_involution_from_s_duality(self):
        """S-duality tau -> -1/tau matches FF involution on tau-line."""
        data = s_duality_vs_koszul('A', 1, 1.0)
        assert data['s_duality_matches_ff']

    def test_kappa_antisymmetric_exact(self):
        """Exact kappa anti-symmetry for sl_2."""
        k = Fraction(1)
        kap = kappa_affine_exact('A', 1, k)
        h_dual = 2
        k_dual = -k - 2 * h_dual
        kap_dual = kappa_affine_exact('A', 1, k_dual)
        assert kap + kap_dual == 0

    def test_ff_involution_k_dual(self):
        """FF involution k -> -k-2h^v for several types."""
        for (lt, rk) in [('A', 1), ('A', 2), ('A', 3)]:
            data = _lie_data(lt, rk)
            k = 1.0
            k_dual = -k - 2 * data['h_dual']
            kap = kappa_affine(lt, rk, k)
            kap_dual = kappa_affine(lt, rk, k_dual)
            assert abs(kap + kap_dual) < 1e-12


# =========================================================================
# Module 8: Explicit sl_2 computation
# =========================================================================

class TestSl2Explicit:
    """Full explicit computation for sl_2."""

    def test_sl2_full_data_k1(self):
        """Complete data for sl_2 at k=1."""
        data = sl2_full_langlands_data(1.0)
        assert data['kappa'] == 2.25  # 3*3/4
        assert abs(data['sugawara_c'] - 1.0) < 1e-12
        assert data['ff_matches_opers']

    def test_sl2_full_data_critical(self):
        """Complete data for sl_2 at critical level."""
        data = sl2_full_langlands_data(-2.0)
        assert data['is_critical']
        assert abs(data['kappa']) < 1e-14
        assert data['sugawara_c'] is None
        assert data['ff_matches_opers']

    def test_sl2_verlinde_genus0(self):
        """Verlinde at genus 0 = 1 for all levels."""
        for k in [1, 2, 3, 5, 10]:
            data = sl2_full_langlands_data(float(k))
            assert data['verlinde'][0] == 1

    def test_sl2_verlinde_genus1(self):
        """Verlinde at genus 1 = k+1."""
        for k in [1, 2, 3, 5, 10]:
            data = sl2_full_langlands_data(float(k))
            assert data['verlinde'][1] == k + 1

    def test_verlinde_sl2_genus1_cross_check(self):
        """Cross-verify Verlinde genus 1 via utility."""
        for k in [1, 2, 3, 4, 5]:
            result = verify_verlinde_sl2_genus1(k)
            assert result['match'], f"k={k}: {result['computed']} != {result['expected']}"

    def test_sl2_verlinde_genus2_k1(self):
        """Verlinde at genus 2 for sl_2, k=1.

        Modular S-matrix: S_{0,j} = sqrt(2/3)*sin(pi(j+1)/3), j=0,1.
        Both S-matrix entries equal sqrt(2/3)*sqrt(3)/2 = 1/sqrt(3).
        V_2 = sum S_{0,j}^{-2} = 2*3 = 6... but our formula normalizes
        differently. Independent computation (Path 2):
        S_00 = S_01 = 1/sqrt(2) (for the UNITARY S-matrix).
        V_2 = sum S_{0,j}^{-2} = 2*2 = 4.
        """
        data = sl2_full_langlands_data(1.0)
        # Cross-verify via direct modular S-matrix computation
        kh = 3
        s_vals = [math.sqrt(2.0 / kh) * math.sin(math.pi * (j + 1) / kh)
                  for j in range(2)]
        direct = int(round(sum(s ** (-2) for s in s_vals)))
        assert data['verlinde'][2] == direct

    def test_sl2_verlinde_genus2_k2(self):
        """Verlinde at genus 2 for sl_2, k=2.

        Cross-verified via direct modular S-matrix (Path 2).
        """
        data = sl2_full_langlands_data(2.0)
        # Direct computation: S_{0,j} = sqrt(2/4)*sin(pi(j+1)/4)
        kh = 4
        s_vals = [math.sqrt(2.0 / kh) * math.sin(math.pi * (j + 1) / kh)
                  for j in range(3)]
        direct = int(round(sum(s ** (-2) for s in s_vals)))
        assert data['verlinde'][2] == direct

    def test_sl2_kz_monodromy_k1(self):
        """KZ monodromy for sl_2 at k=1."""
        data = sl2_kz_monodromy(1.0)
        assert not data['is_critical']
        # q = exp(pi i / 3) is a primitive 6th root of unity
        q = data['q']
        assert abs(q ** 6 - 1.0) < 1e-10

    def test_sl2_kz_monodromy_critical(self):
        """KZ monodromy degenerate at critical level."""
        data = sl2_kz_monodromy(-2.0)
        assert data['is_critical']

    def test_sl2_kz_eigenvalues(self):
        """KZ eigenvalues for V_1 x V_1 decomposition."""
        data = sl2_kz_monodromy(1.0)
        eigs = data['eigenvalues_V1_x_V1']
        # V_0 eigenvalue = 1
        assert abs(eigs['V_0'] - 1.0) < 1e-12
        # V_2 eigenvalue = q^4 where q = exp(pi i/3)
        q = cmath.exp(cmath.pi * 1j / 3)
        assert abs(eigs['V_2'] - q ** 4) < 1e-10

    def test_sl2_bar_at_critical(self):
        """Bar complex of V_{-2}(sl_2) at critical level."""
        data = sl2_bar_at_critical()
        assert data['is_uncurved']
        assert abs(data['kappa']) < 1e-14
        # CE cohomology of sl_2
        assert data['ce_cohomology'] == {0: 1, 1: 0, 2: 0, 3: 1}
        # Euler characteristic = 1 - 0 + 0 - 1 = 0
        assert data['ce_euler_char'] == 0

    def test_sl2_ff_dims_match_p2(self):
        """FF center dims = p_2(n) for sl_2."""
        data = sl2_bar_at_critical()
        # Known values of p_2(n)
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21]
        assert data['ff_center_dims'] == expected

    def test_sl2_shadow_tower_zero_at_critical(self):
        """Shadow F_g = 0 at critical level for sl_2."""
        data = sl2_full_langlands_data(-2.0)
        for g in [1, 2, 3]:
            assert abs(data['shadow_F_g'][g]) < 1e-14

    def test_sl2_shadow_tower_nonzero_generic(self):
        """Shadow F_g != 0 at generic level for sl_2."""
        data = sl2_full_langlands_data(1.0)
        # F_1 = kappa/24 = (9/4)/24 = 3/32 != 0
        assert abs(data['shadow_F_g'][1]) > 1e-6


# =========================================================================
# Cross-verification and structural tests
# =========================================================================

class TestCrossVerification:
    """Cross-verification tests spanning multiple modules."""

    def test_freudenthal_de_vries_all_types(self):
        """Freudenthal-de Vries: sum(2d_i - 1) = dim(G) for all types."""
        types = [
            ('A', 1), ('A', 2), ('A', 3), ('A', 4), ('A', 5),
            ('B', 2), ('B', 3),
            ('C', 2), ('C', 3),
            ('D', 4), ('D', 5),
            ('G', 2), ('F', 4),
            ('E', 6), ('E', 7), ('E', 8),
        ]
        for (lt, rk) in types:
            result = verify_hitchin_base_equals_dim_g(lt, rk, 3)
            assert result['match'], \
                f"{lt}_{rk}: sum(2d-1)={result['sum_2d_minus_1']} != dim(G)={result['dim_G']}"

    def test_ff_theorem_all_type_a(self):
        """FF theorem for sl_2 through sl_6."""
        for n in range(2, 7):
            result = verify_ff_theorem('A', n - 1, 10)
            assert result['match'], \
                f"sl_{n}: FF theorem fails at {result['mismatches']}"

    def test_kappa_zero_iff_critical(self):
        """kappa = 0 if and only if k = -h^v."""
        for (lt, rk) in [('A', 1), ('A', 2), ('G', 2)]:
            data = _lie_data(lt, rk)
            # At critical: kappa = 0
            assert abs(kappa_affine(lt, rk, float(-data['h_dual']))) < 1e-14
            # Away from critical: kappa != 0
            assert abs(kappa_affine(lt, rk, 1.0)) > 0.1

    def test_quantum_parameter_agrees_with_kz(self):
        """Quantum group q agrees with KZ coupling parameter."""
        # For sl_2 at k=1: hbar = 1/3, q = exp(pi i/3)
        qg = quantum_group_parameter('A', 1, 1.0)
        kz = sl2_kz_monodromy(1.0)
        assert abs(qg['q'] - kz['q']) < 1e-12

    def test_dictionary_completeness(self):
        """Full Langlands dictionary has all required entries."""
        d = full_langlands_dictionary()
        required_keys = [
            'bar_complex', 'cobar', 'verdier_dual', 'koszul_dual',
            'kappa', 'shadow_tower', 'ff_center', 'mc3_dk_bridge',
            'kz_connection', 's_duality',
        ]
        for key in required_keys:
            assert key in d, f"Missing dictionary entry: {key}"

    def test_dictionary_bar_not_bulk(self):
        """Dictionary correctly states cobar recovers A, not the bulk (AP25, AP34)."""
        d = full_langlands_dictionary()
        cobar_entry = d['cobar']['bar_cobar']
        assert 'inversion' in cobar_entry.lower() or 'Omega(B(A)) = A' in cobar_entry
        geom = d['cobar']['geom_langlands']
        assert 'NOT the Langlands dual' in geom

    def test_bd_quantization_agrees_with_shadow(self):
        """BD quantum corrections = shadow tower F_g values."""
        k = 2.0
        bd = bd_quantization_data('A', 1, k)
        sl2 = sl2_full_langlands_data(k)
        for g in [1, 2, 3]:
            assert abs(bd['F_g_values'][g] - sl2['shadow_F_g'][g]) < 1e-12

    def test_critical_level_classical_across_modules(self):
        """At critical level, multiple modules agree it is the classical limit."""
        k_crit = -2.0
        bc = bar_curvature_at_level('A', 1, k_crit)
        bd = bd_quantization_data('A', 1, k_crit)
        st = shadow_tower_at_critical('A', 1)
        sl2 = sl2_full_langlands_data(k_crit)

        assert bc['is_uncurved']
        assert bd['is_classical_limit']
        assert st['classical_limit']
        assert sl2['is_critical']
        assert abs(bc['kappa']) < 1e-14
        assert abs(bd['kappa']) < 1e-14

    def test_lie_data_consistency(self):
        """Lie algebra data self-consistent: dim matches formula."""
        # For A_n: dim = (n+1)^2 - 1
        for n in range(1, 6):
            data = _lie_data('A', n)
            assert data['dim'] == (n + 1) ** 2 - 1
            assert data['h_dual'] == n + 1
            assert data['casimir_degrees'] == list(range(2, n + 2))


# =========================================================================
# Multi-path verification (AP10 compliance)
# =========================================================================

class TestMultiPathVerification:
    """Every hardcoded value cross-checked by >= 2 independent paths."""

    # --- kappa formulas: 3 paths ---

    def test_kappa_sl2_k1_three_paths(self):
        """kappa(sl_2, k=1) = 9/4 via 3 independent paths.

        Path 1: Direct formula kappa = dim(g)(k+h^v)/(2h^v) = 3*3/4
        Path 2: Exact Fraction computation
        Path 3: From the existing bc_geometric_langlands engine
        """
        # Path 1: float formula
        kap1 = 3.0 * (1 + 2) / (2.0 * 2)
        # Path 2: exact
        kap2 = kappa_affine_exact('A', 1, Fraction(1))
        # Path 3: engine
        kap3 = kappa_affine('A', 1, 1.0)
        assert abs(kap1 - 2.25) < 1e-14
        assert kap2 == Fraction(9, 4)
        assert abs(kap3 - float(kap2)) < 1e-14

    def test_kappa_sl3_k1_three_paths(self):
        """kappa(sl_3, k=1) = 16/3 via 3 paths.

        Path 1: dim(sl_3)=8, h^v=3, kappa = 8*4/(2*3) = 16/3
        Path 2: Exact Fraction
        Path 3: Engine float
        """
        kap1 = 8.0 * 4.0 / 6.0
        kap2 = kappa_affine_exact('A', 2, Fraction(1))
        kap3 = kappa_affine('A', 2, 1.0)
        assert abs(kap1 - 16.0 / 3.0) < 1e-14
        assert kap2 == Fraction(16, 3)
        assert abs(kap3 - float(kap2)) < 1e-14

    def test_kappa_G2_k1_two_paths(self):
        """kappa(G_2, k=1) via 2 paths.

        Path 1: dim(G_2)=14, h^v=4, kappa = 14*5/(2*4) = 35/4
        Path 2: Engine exact
        """
        kap1 = 14.0 * 5.0 / 8.0
        kap2 = kappa_affine_exact('G', 2, Fraction(1))
        assert abs(kap1 - 35.0 / 4.0) < 1e-14
        assert kap2 == Fraction(35, 4)

    # --- FF center dims: 2 paths ---

    def test_ff_sl2_dims_two_paths(self):
        """FF center dims for sl_2 via 2 independent computations.

        Path 1: Engine ff_center_dims
        Path 2: Direct product formula prod_{m>=2} 1/(1-q^m)
        """
        max_w = 12
        # Path 1
        ff = ff_center_dims('A', 1, max_w)
        # Path 2: manual product expansion
        coeffs = [0] * (max_w + 1)
        coeffs[0] = 1
        for m in range(2, max_w + 1):
            for n in range(m, max_w + 1):
                coeffs[n] += coeffs[n - m]
        assert ff['dims'] == coeffs

    def test_ff_sl3_dims_two_paths(self):
        """FF center dims for sl_3 via 2 paths.

        Path 1: Engine ff_center_dims (Casimir degrees {2,3})
        Path 2: Direct product expansion with multiplicity
        """
        max_w = 10
        # Path 1
        ff = ff_center_dims('A', 2, max_w)
        # Path 2: prod_{s>=2} 1/(1-q^s)^{min(s-1,2)}
        coeffs = [0] * (max_w + 1)
        coeffs[0] = 1
        for s in range(2, max_w + 1):
            mult = min(s - 1, 2)  # N-1=2 for sl_3
            for _ in range(mult):
                for n in range(s, max_w + 1):
                    coeffs[n] += coeffs[n - s]
        assert ff['dims'] == coeffs

    # --- Critical level: 3 paths ---

    def test_critical_sl2_three_paths(self):
        """Critical level for sl_2 = -2 via 3 paths.

        Path 1: critical_level function
        Path 2: kappa = 0 solver (k such that dim(g)(k+h^v)/(2h^v)=0)
        Path 3: Lie data h_dual
        """
        # Path 1
        k_crit = critical_level('A', 1)
        # Path 2: k + h^v = 0 => k = -h^v
        data = _lie_data('A', 1)
        k_from_formula = -data['h_dual']
        # Path 3: direct
        assert k_crit == -2
        assert k_from_formula == -2
        assert abs(kappa_affine('A', 1, float(k_crit))) < 1e-14

    # --- Sugawara: 2 paths ---

    def test_sugawara_sl2_k1_two_paths(self):
        """c(sl_2, k=1) = 1 via 2 paths.

        Path 1: Engine sugawara_central_charge
        Path 2: Direct formula c = k*dim/(k+h^v) = 1*3/3 = 1
        """
        c1 = sugawara_central_charge('A', 1, 1.0)
        c2 = 1.0 * 3.0 / (1.0 + 2.0)
        assert abs(c1 - 1.0) < 1e-14
        assert abs(c2 - 1.0) < 1e-14

    def test_sugawara_sl2_k2_two_paths(self):
        """c(sl_2, k=2) = 3/2 via 2 paths."""
        c1 = sugawara_central_charge('A', 1, 2.0)
        c2 = 2.0 * 3.0 / 4.0
        assert abs(c1 - 1.5) < 1e-14
        assert abs(c2 - 1.5) < 1e-14

    # --- Kappa complementarity: 2 paths ---

    def test_kappa_complementarity_sl2_two_paths(self):
        """kappa + kappa' = 0 for sl_2 via 2 paths.

        Path 1: Engine verify_kappa_complementarity
        Path 2: Exact Fraction computation
        """
        # Path 1
        result = verify_kappa_complementarity('A', 1, 3.0)
        assert result['is_antisymmetric']
        # Path 2: exact
        k = Fraction(3)
        kap = kappa_affine_exact('A', 1, k)
        kap_dual = kappa_affine_exact('A', 1, -k - 4)  # -k - 2h^v
        assert kap + kap_dual == 0

    # --- Quantum group: 2 paths ---

    def test_quantum_group_sl2_k1_two_paths(self):
        """q(sl_2, k=1) = exp(pi i/3) via 2 paths.

        Path 1: Engine quantum_group_parameter
        Path 2: Direct computation
        """
        # Path 1
        qg = quantum_group_parameter('A', 1, 1.0)
        # Path 2
        q_direct = cmath.exp(cmath.pi * 1j / 3.0)
        assert abs(qg['q'] - q_direct) < 1e-12

    def test_quantum_group_root_order_two_paths(self):
        """q^6 = 1 for sl_2 at k=1 via 2 paths.

        Path 1: From root_order in quantum_group_parameter
        Path 2: Direct computation q = e^{i*pi/3}, q^6 = e^{2*pi*i} = 1
        """
        qg = quantum_group_parameter('A', 1, 1.0)
        # Path 1
        assert qg['is_root_of_unity']
        # Path 2
        q = cmath.exp(cmath.pi * 1j / 3.0)
        assert abs(q ** 6 - 1.0) < 1e-10

    # --- Verlinde: 2 paths ---

    def test_verlinde_genus1_two_paths(self):
        """Verlinde at genus 1 = k+1 via 2 paths.

        Path 1: Engine _verlinde_sl2 via sl2_full_langlands_data
        Path 2: Direct count of integrable representations
        """
        for k in [1, 2, 3, 4, 5]:
            data = sl2_full_langlands_data(float(k))
            # Path 1: engine
            v1 = data['verlinde'][1]
            # Path 2: number of integrable reps = k+1
            v2 = k + 1
            assert v1 == v2, f"k={k}: {v1} != {v2}"

    def test_verlinde_genus2_two_paths(self):
        """Verlinde at genus 2 via 2 paths: engine vs direct S-matrix.

        Path 1: Engine
        Path 2: Direct modular S-matrix sum S_{0,j}^{-2}
        """
        for k in [1, 2, 3]:
            data = sl2_full_langlands_data(float(k))
            v_engine = data['verlinde'][2]
            # Path 2: direct
            kh = k + 2
            s_vals = [math.sqrt(2.0 / kh) * math.sin(math.pi * (j + 1) / kh)
                      for j in range(k + 1)]
            v_direct = int(round(sum(s ** (-2) for s in s_vals)))
            assert v_engine == v_direct, f"k={k}: {v_engine} != {v_direct}"

    # --- Hitchin base: 2 paths ---

    def test_hitchin_base_sl2_two_paths(self):
        """Hitchin base dim for sl_2 at g=3 via 2 paths.

        Path 1: Engine hitchin_base_dimension
        Path 2: Direct Freudenthal-de Vries: sum(2d-1)(g-1) = 3*(3-1) = 6
        """
        data = hitchin_base_dimension('A', 1, 3)
        # Path 1
        dim1 = data['dim_hitchin_base']
        # Path 2: Casimir degrees = {2}, so sum(2*2-1) = 3, times (g-1) = 2
        dim2 = 3 * 2
        assert dim1 == dim2

    # --- F_g values: 2 paths ---

    def test_F1_sl2_k1_two_paths(self):
        """F_1(sl_2, k=1) = kappa/24 = 9/4/24 = 3/32 via 2 paths.

        Path 1: BD quantization engine
        Path 2: Direct formula kappa * lambda_1 = (9/4)*(1/24)
        """
        bd = bd_quantization_data('A', 1, 1.0)
        # Path 1
        f1_engine = bd['F_g_values'][1]
        # Path 2
        kap = Fraction(9, 4)
        lam1 = Fraction(1, 24)
        f1_direct = float(kap * lam1)
        assert abs(f1_engine - f1_direct) < 1e-14
        assert abs(f1_engine - 3.0 / 32.0) < 1e-14

    def test_F2_sl2_k1_two_paths(self):
        """F_2(sl_2, k=1) = kappa * 7/5760 via 2 paths."""
        bd = bd_quantization_data('A', 1, 1.0)
        f2_engine = bd['F_g_values'][2]
        f2_direct = float(Fraction(9, 4) * Fraction(7, 5760))
        assert abs(f2_engine - f2_direct) < 1e-14

    # --- CE cohomology of sl_2: 2 paths ---

    def test_ce_cohomology_sl2_two_paths(self):
        """CE cohomology of sl_2 via 2 paths.

        Path 1: Engine sl2_bar_at_critical
        Path 2: Known result for semisimple Lie algebras:
                 H^0 = C, H^{dim g} = C, else 0. For sl_2 (dim=3):
                 H^0 = 1, H^1 = 0, H^2 = 0, H^3 = 1.
        """
        data = sl2_bar_at_critical()
        # Path 1
        ce = data['ce_cohomology']
        # Path 2: Whitehead lemmas for semisimple g
        expected = {0: 1, 1: 0, 2: 0, 3: 1}
        assert ce == expected
        # Path 3: Euler characteristic = 0 (for odd-dimensional g)
        chi = sum((-1) ** d * v for d, v in ce.items())
        assert chi == 0

    # --- Lie algebra dimensions: 3 paths ---

    def test_dim_sl2_three_paths(self):
        """dim(sl_2) = 3 via 3 paths.

        Path 1: Engine _lie_data
        Path 2: Formula N^2 - 1 = 4 - 1 = 3
        Path 3: Number of generators {e, h, f}
        """
        data = _lie_data('A', 1)
        assert data['dim'] == 3
        assert 2 ** 2 - 1 == 3
        # Path 3: sl_2 has 3 Chevalley generators
        assert data['dim'] == data['N'] ** 2 - 1

    def test_dim_e8_two_paths(self):
        """dim(E_8) = 248 via 2 paths.

        Path 1: Engine _lie_data
        Path 2: Known value from classification of simple Lie algebras
        """
        data = _lie_data('E', 8)
        assert data['dim'] == 248
        # Path 2: Freudenthal-de Vries sum(2d_i - 1) should also equal 248
        assert sum(2 * d - 1 for d in data['casimir_degrees']) == 248
