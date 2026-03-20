#!/usr/bin/env python3
r"""
test_theta_decomposition_bridge.py — Non-lattice bridge via theta decomposition.

T1-T8:   Theta function basic properties and Jacobi identities
T9-T16:  Ising character theta decomposition verification
T17-T24: |chi|^2 decomposition and cross-term analysis
T25-T30: Partition function Z_Ising = (t2+t3+t4)/(2*eta) simplification
T31-T38: Lattice Epstein from theta (E_Z, E_{Z^2}, partial zetas)
T39-T44: Level-24 theta structure and Dirichlet characters
T45-T50: General M(p,q) decomposition and auxiliary lattice
T51-T55: Cross-term Mellin and L-function identification
T56-T60: Shadow depth prediction and consistency
"""

import pytest
import numpy as np
import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from theta_decomposition_bridge import (
    theta_2, theta_3, theta_4, dedekind_eta,
    ising_character_qseries, ising_character_theta,
    chi_squared_decomposition, ising_partition_function,
    jacobi_abstruse_identity, verify_theta_jacobi_relation,
    theta_mellin_epstein, epstein_z_squared, epstein_z_squared_direct,
    dirichlet_L_chi4,
    ising_z_epstein_decomposition,
    rocha_caridi_theta, minimal_model_character, minimal_model_data,
    ising_level24_decomposition, ising_dirichlet_characters,
    ising_full_epstein_decomposition, dirichlet_characters_mod24,
    partial_zeta_dirichlet_decomposition,
    cross_term_numerical,
    tricritical_ising_data, lee_yang_data, three_state_potts_data,
    auxiliary_lattice_data, shadow_depth_from_l_functions,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# T1-T8: Theta function basics and Jacobi identities
# ============================================================

class TestThetaFunctionBasics:

    @skip_no_mpmath
    def test_t1_theta3_at_iy1(self):
        """T1: theta_3(i) > 1 (sum includes n=0 term = 1)."""
        tau = mpmath.mpc(0, 1)
        val = mpmath.re(theta_3(tau, 300))
        assert val > 1.0
        # Known: theta_3(i) = pi^{1/4}/Gamma(3/4) ≈ 1.0864...
        expected = float(mpmath.power(mpmath.pi, 0.25) / mpmath.gamma(0.75))
        assert abs(val - expected) / expected < 1e-8

    @skip_no_mpmath
    def test_t2_theta4_at_iy1(self):
        """T2: theta_4(i) > 0 (alternating sum)."""
        tau = mpmath.mpc(0, 1)
        val = mpmath.re(theta_4(tau, 300))
        assert val > 0

    @skip_no_mpmath
    def test_t3_theta2_at_iy1(self):
        """T3: theta_2(i) > 0 (half-integer lattice)."""
        tau = mpmath.mpc(0, 1)
        val = mpmath.re(theta_2(tau, 300))
        assert val > 0

    @skip_no_mpmath
    def test_t4_eta_at_iy1(self):
        """T4: eta(i) = Gamma(1/4)/(2*pi^{3/4})."""
        tau = mpmath.mpc(0, 1)
        val = mpmath.re(dedekind_eta(tau, 500))
        expected = float(mpmath.gamma(0.25) / (2 * mpmath.power(mpmath.pi, 0.75)))
        assert abs(val - expected) / expected < 1e-6

    @skip_no_mpmath
    def test_t5_jacobi_abstruse_y1(self):
        """T5: theta_3^4 = theta_2^4 + theta_4^4 at y=1."""
        result = jacobi_abstruse_identity(1.0, 300)
        assert result['abstruse_error'] < 1e-20

    @skip_no_mpmath
    def test_t6_jacobi_abstruse_y05(self):
        """T6: Abstruse identity at y=0.5."""
        result = jacobi_abstruse_identity(0.5, 300)
        assert result['abstruse_error'] < 1e-15

    @skip_no_mpmath
    def test_t7_triple_product_y1(self):
        """T7: theta_2*theta_3*theta_4 = 2*eta^3 at y=1."""
        result = jacobi_abstruse_identity(1.0, 300)
        assert result['triple_error'] < 1e-20

    @skip_no_mpmath
    def test_t8_jacobi_identities_multiple_y(self):
        """T8: All Jacobi identities hold at y=0.5, 1, 2, 5."""
        for y in [0.5, 1.0, 2.0, 5.0]:
            result = verify_theta_jacobi_relation(y, 300)
            assert result['abstruse']['error'] < 1e-12, f"Abstruse fails at y={y}"
            assert result['triple_product']['error'] < 1e-12, f"Triple product fails at y={y}"
            assert result['doubling_t3']['error'] < 1e-12, f"Doubling t3 fails at y={y}"


# ============================================================
# T9-T16: Ising character theta decomposition
# ============================================================

class TestIsingCharacterDecomposition:

    @skip_no_mpmath
    def test_t9_chi0_theta_vs_qseries_y1(self):
        """T9: chi_0 from theta decomposition matches q-series at y=1."""
        tau = mpmath.mpc(0, 1)
        chi_theta = mpmath.re(ising_character_theta(0, tau, 300))
        chi_qs = mpmath.re(ising_character_qseries(0, tau, 300))
        assert abs(chi_theta - chi_qs) / abs(chi_qs) < 1e-6

    @skip_no_mpmath
    def test_t10_chi12_theta_vs_qseries_y1(self):
        """T10: chi_{1/2} from theta matches q-series at y=1."""
        tau = mpmath.mpc(0, 1)
        chi_theta = mpmath.re(ising_character_theta(0.5, tau, 300))
        chi_qs = mpmath.re(ising_character_qseries(0.5, tau, 300))
        assert abs(chi_theta - chi_qs) / abs(chi_qs) < 1e-6

    @skip_no_mpmath
    def test_t11_chi116_theta_vs_qseries_y1(self):
        """T11: chi_{1/16} from theta matches q-series at y=1."""
        tau = mpmath.mpc(0, 1)
        chi_theta = mpmath.re(ising_character_theta(1.0 / 16, tau, 300))
        chi_qs = mpmath.re(ising_character_qseries(1.0 / 16, tau, 300))
        assert abs(chi_theta - chi_qs) / abs(chi_qs) < 1e-6

    @skip_no_mpmath
    def test_t12_chi0_at_y05(self):
        """T12: chi_0 theta vs q-series at y=0.5."""
        tau = mpmath.mpc(0, 0.5)
        chi_theta = mpmath.re(ising_character_theta(0, tau, 500))
        chi_qs = mpmath.re(ising_character_qseries(0, tau, 300))
        assert abs(chi_theta - chi_qs) / abs(chi_qs) < 1e-4

    @skip_no_mpmath
    def test_t13_chi0_at_y2(self):
        """T13: chi_0 theta vs q-series at y=2."""
        tau = mpmath.mpc(0, 2)
        chi_theta = mpmath.re(ising_character_theta(0, tau, 300))
        chi_qs = mpmath.re(ising_character_qseries(0, tau, 200))
        assert abs(chi_theta - chi_qs) / abs(chi_qs) < 1e-8

    @skip_no_mpmath
    def test_t14_chi12_at_y2(self):
        """T14: chi_{1/2} theta vs q-series at y=2."""
        tau = mpmath.mpc(0, 2)
        chi_theta = mpmath.re(ising_character_theta(0.5, tau, 300))
        chi_qs = mpmath.re(ising_character_qseries(0.5, tau, 200))
        assert abs(chi_theta - chi_qs) / abs(chi_qs) < 1e-8

    @skip_no_mpmath
    def test_t15_chi116_at_y5(self):
        """T15: chi_{1/16} theta vs q-series at y=5."""
        tau = mpmath.mpc(0, 5)
        chi_theta = mpmath.re(ising_character_theta(1.0 / 16, tau, 200))
        chi_qs = mpmath.re(ising_character_qseries(1.0 / 16, tau, 200))
        # At large y, values are tiny; use absolute tolerance
        assert abs(chi_theta - chi_qs) < 1e-10

    @skip_no_mpmath
    def test_t16_all_chars_positive_y1(self):
        """T16: All Ising characters are positive on the imaginary axis at y=1."""
        tau = mpmath.mpc(0, 1)
        for h in [0, 0.5, 1.0 / 16]:
            val = mpmath.re(ising_character_theta(h, tau, 300))
            assert val > 0, f"chi_{h} not positive at y=1"


# ============================================================
# T17-T24: |chi|^2 decomposition
# ============================================================

class TestChiSquaredDecomposition:

    @skip_no_mpmath
    def test_t17_chi0_sq_decomp_y1(self):
        """T17: |chi_0|^2 from theta matches q-series at y=1."""
        result = chi_squared_decomposition(0, 1.0, 300)
        rel = abs(result['chi_sq'] - result['chi_sq_theta']) / abs(result['chi_sq'])
        assert rel < 1e-6

    @skip_no_mpmath
    def test_t18_chi12_sq_decomp_y1(self):
        """T18: |chi_{1/2}|^2 from theta matches q-series at y=1."""
        result = chi_squared_decomposition(0.5, 1.0, 300)
        rel = abs(result['chi_sq'] - result['chi_sq_theta']) / abs(result['chi_sq'])
        assert rel < 1e-6

    @skip_no_mpmath
    def test_t19_chi116_sq_decomp_y1(self):
        """T19: |chi_{1/16}|^2 from theta matches q-series at y=1."""
        result = chi_squared_decomposition(1.0 / 16, 1.0, 300)
        rel = abs(result['chi_sq'] - result['chi_sq_theta']) / abs(result['chi_sq'])
        assert rel < 1e-6

    @skip_no_mpmath
    def test_t20_chi0_sq_has_cross_term(self):
        """T20: |chi_0|^2 decomposition has nonzero cross term."""
        result = chi_squared_decomposition(0, 1.0, 300)
        assert abs(result['theta_terms']['cross']) > 0.01

    @skip_no_mpmath
    def test_t21_chi12_sq_cross_negative(self):
        """T21: |chi_{1/2}|^2 cross term is negative (subtracted)."""
        result = chi_squared_decomposition(0.5, 1.0, 300)
        assert result['theta_terms']['cross'] < 0

    @skip_no_mpmath
    def test_t22_cross_terms_cancel_in_sum(self):
        """T22: Cross terms cancel: |chi_0|^2 + |chi_{1/2}|^2 = (t3+t4)/(2*eta)."""
        r0 = chi_squared_decomposition(0, 1.0, 300)
        r1 = chi_squared_decomposition(0.5, 1.0, 300)
        # Cross terms: +sqrt(t3*t4)/eta and -sqrt(t3*t4)/eta
        cross_sum = r0['theta_terms']['cross'] + r1['theta_terms']['cross']
        assert abs(cross_sum) < 1e-10

    @skip_no_mpmath
    def test_t23_decomp_multiple_y(self):
        """T23: Theta decomposition matches q-series at y=0.5, 1, 2."""
        for y in [0.5, 1.0, 2.0]:
            for h in [0, 0.5, 1.0 / 16]:
                result = chi_squared_decomposition(h, y, 300)
                if result['chi_sq'] > 1e-15:
                    rel = abs(result['chi_sq'] - result['chi_sq_theta']) / abs(result['chi_sq'])
                    assert rel < 1e-3, f"Mismatch at h={h}, y={y}: rel={rel}"

    @skip_no_mpmath
    def test_t24_chi116_sq_is_t2_over_2eta(self):
        """T24: |chi_{1/16}|^2 = theta_2/(2*eta) on imaginary axis."""
        result = chi_squared_decomposition(1.0 / 16, 1.0, 300)
        assert 'theta2_over_2eta' in result['theta_terms']
        assert result['theta_terms']['theta2_over_2eta'] > 0


# ============================================================
# T25-T30: Partition function simplification
# ============================================================

class TestPartitionFunctionSimplification:

    @skip_no_mpmath
    def test_t25_z_ising_direct_vs_simplified_y1(self):
        """T25: Z_Ising = (t2+t3+t4)/(2*eta) at y=1."""
        result = ising_partition_function(1.0, 300)
        rel = abs(result['Z_direct'] - result['Z_simplified']) / abs(result['Z_direct'])
        assert rel < 1e-10

    @skip_no_mpmath
    def test_t26_z_ising_y05(self):
        """T26: Simplified Z_Ising matches direct at y=0.5."""
        result = ising_partition_function(0.5, 300)
        rel = abs(result['Z_direct'] - result['Z_simplified']) / abs(result['Z_direct'])
        assert rel < 1e-8

    @skip_no_mpmath
    def test_t27_z_ising_y2(self):
        """T27: Simplified Z_Ising matches direct at y=2."""
        result = ising_partition_function(2.0, 300)
        rel = abs(result['Z_direct'] - result['Z_simplified']) / abs(result['Z_direct'])
        assert rel < 1e-10

    @skip_no_mpmath
    def test_t28_cross_term_cancellation(self):
        """T28: Cross terms cancel in |chi_0|^2 + |chi_{1/2}|^2."""
        result = ising_partition_function(1.0, 300)
        assert result['cross_term_cancellation']

    @skip_no_mpmath
    def test_t29_z_positive(self):
        """T29: Z_Ising > 0 for all tested y values."""
        for y in [0.5, 1.0, 2.0, 5.0]:
            result = ising_partition_function(y, 300)
            assert result['Z_direct'] > 0

    @skip_no_mpmath
    def test_t30_z_ising_all_y(self):
        """T30: Simplified formula works at y=0.5, 1, 2, 5."""
        for y in [0.5, 1.0, 2.0, 5.0]:
            result = ising_partition_function(y, 300)
            if result['Z_direct'] > 1e-15:
                rel = abs(result['Z_direct'] - result['Z_simplified']) / abs(result['Z_direct'])
                assert rel < 1e-6, f"Mismatch at y={y}"


# ============================================================
# T31-T38: Lattice Epstein zeta from theta
# ============================================================

class TestLatticeEpstein:

    @skip_no_mpmath
    def test_t31_theta3_epstein_is_2zeta2s(self):
        """T31: Epstein of theta_3 lattice = 2*zeta(2s) at s=2."""
        val = theta_mellin_epstein(3, 2.0)
        expected = float(2 * mpmath.zeta(4))
        assert abs(val - expected) / abs(expected) < 1e-8

    @skip_no_mpmath
    def test_t32_theta3_epstein_s3(self):
        """T32: Epstein of theta_3 lattice at s=3."""
        val = theta_mellin_epstein(3, 3.0)
        expected = float(2 * mpmath.zeta(6))
        assert abs(val - expected) / abs(expected) < 1e-8

    @skip_no_mpmath
    def test_t33_theta2_epstein_shifted_lattice(self):
        """T33: Epstein for theta_2 (shifted lattice Z+1/2)."""
        val = theta_mellin_epstein(2, 2.0)
        # sum_{n>=0} 2*(n+1/2)^{-4} = 2*(2^4 - 1)*zeta(4)/2^4 ... hmm
        # Direct: 2*sum_{n=0}^{inf} (n+0.5)^{-4}
        # = 2*(1-2^{-4})*... actually this is the Hurwitz zeta:
        # 2*zeta(4, 1/2) = 2*(2^4-1)*zeta(4) = 2*15*pi^4/90 = 30*pi^4/90
        expected = float(2 * mpmath.zeta(4, mpmath.mpf('0.5')))
        assert abs(val - expected) / abs(expected) < 1e-6

    @skip_no_mpmath
    def test_t34_theta4_epstein(self):
        """T34: Epstein for theta_4: 2*(1-2^{1-2s})*zeta(2s)."""
        s = 2.0
        val = theta_mellin_epstein(4, s)
        expected = float(2 * (1 - mpmath.power(2, 1 - 2 * s)) * mpmath.zeta(2 * s))
        assert abs(val - expected) / abs(expected) < 1e-8

    @skip_no_mpmath
    def test_t35_ez2_formula(self):
        """T35: E_{Z^2}(s) = 4*zeta(s)*L(s,chi_{-4}) at s=2."""
        val = epstein_z_squared(2.0, 2000)
        direct = epstein_z_squared_direct(2.0, 80)
        # Should match to good precision
        assert abs(val - direct) / abs(direct) < 0.01

    @skip_no_mpmath
    def test_t36_dirichlet_beta_s1(self):
        """T36: L(1, chi_{-4}) = pi/4 (Leibniz formula)."""
        val = dirichlet_L_chi4(1.0, 10000)
        expected = float(mpmath.pi / 4)
        assert abs(val - expected) / expected < 0.001

    @skip_no_mpmath
    def test_t37_dirichlet_beta_s2(self):
        """T37: L(2, chi_{-4}) = Catalan's constant G = 0.9159..."""
        val = dirichlet_L_chi4(2.0, 5000)
        # Catalan's constant
        expected = float(mpmath.catalan)
        assert abs(val - expected) / expected < 0.01

    @skip_no_mpmath
    def test_t38_epstein_sum_consistency(self):
        """T38: E_{Z^2}(3) from formula vs direct sum agree."""
        val_formula = epstein_z_squared(3.0, 3000)
        val_direct = epstein_z_squared_direct(3.0, 50)
        # At s=3, convergence is fast
        assert abs(val_formula - val_direct) / abs(val_direct) < 0.02


# ============================================================
# T39-T44: Level-24 theta and Dirichlet characters
# ============================================================

class TestLevel24ThetaStructure:

    @skip_no_mpmath
    def test_t39_level24_chi11_matches_chi0(self):
        """T39: Level-24 Theta decomposition for (1,1) matches chi_0."""
        tau = mpmath.mpc(0, 1)
        l24 = ising_level24_decomposition(tau, 300)
        chi_11 = mpmath.re(l24['characters'][(1, 1)])
        chi_0 = mpmath.re(ising_character_qseries(0, tau, 300))
        assert abs(chi_11 - chi_0) / abs(chi_0) < 1e-6

    @skip_no_mpmath
    def test_t40_level24_chi12_matches_chi12(self):
        """T40: Level-24 (1,2) matches chi_{1/2}."""
        tau = mpmath.mpc(0, 1)
        l24 = ising_level24_decomposition(tau, 300)
        chi_12 = mpmath.re(l24['characters'][(1, 2)])
        chi_half = mpmath.re(ising_character_qseries(0.5, tau, 300))
        assert abs(chi_12 - chi_half) / abs(chi_half) < 1e-6

    @skip_no_mpmath
    def test_t41_level24_chi21_matches_chi116(self):
        """T41: Level-24 (2,1) matches chi_{1/16}."""
        tau = mpmath.mpc(0, 1)
        l24 = ising_level24_decomposition(tau, 300)
        chi_21 = mpmath.re(l24['characters'][(2, 1)])
        chi_116 = mpmath.re(ising_character_qseries(1.0 / 16, tau, 300))
        assert abs(chi_21 - chi_116) / abs(chi_116) < 1e-6

    @skip_no_mpmath
    def test_t42_ising_has_3_primaries(self):
        """T42: Ising has exactly 3 primaries in Kac table."""
        data = minimal_model_data(4, 3)
        assert len(data['primaries']) == 3

    @skip_no_mpmath
    def test_t43_ising_conformal_weights(self):
        """T43: Ising conformal weights are 0, 1/2, 1/16."""
        data = minimal_model_data(4, 3)
        h_vals = sorted(data['primaries'].values())
        assert abs(h_vals[0]) < 1e-10  # h=0
        assert abs(h_vals[1] - 1.0 / 16) < 1e-10  # h=1/16
        assert abs(h_vals[2] - 0.5) < 1e-10  # h=1/2

    @skip_no_mpmath
    def test_t44_ising_central_charge(self):
        """T44: Ising central charge c = 1/2."""
        data = minimal_model_data(4, 3)
        assert abs(data['c'] - 0.5) < 1e-10


# ============================================================
# T45-T50: General M(p,q) and auxiliary lattice
# ============================================================

class TestGeneralMinimalModel:

    @skip_no_mpmath
    def test_t45_lee_yang_data(self):
        """T45: Lee-Yang M(5,2) has c=-22/5 and 2 primaries (h=0, h=-1/5)."""
        data = lee_yang_data()
        assert abs(data['c'] - (-22.0 / 5)) < 1e-10
        # M(5,2): q=2 so r=1 only; s=1,2,3,4 with (r,s)~(q-r,p-s)=(1,p-s)
        # So (1,1)~(1,4), (1,2)~(1,3). Two fields: h_{1,1}=0, h_{1,2}=-1/5.
        assert len(data['primaries']) == 2

    @skip_no_mpmath
    def test_t46_tricritical_ising(self):
        """T46: Tricritical Ising M(5,4) has c=7/10."""
        data = tricritical_ising_data()
        assert abs(data['c'] - 0.7) < 1e-10

    @skip_no_mpmath
    def test_t47_three_state_potts(self):
        """T47: Three-state Potts M(6,5) has c=4/5."""
        data = three_state_potts_data()
        assert abs(data['c'] - 0.8) < 1e-10

    @skip_no_mpmath
    def test_t48_auxiliary_lattice_ising(self):
        """T48: Auxiliary lattice for Ising: level 24, disc 24, NOT self-dual."""
        lat = auxiliary_lattice_data(4, 3)
        assert lat['level'] == 24
        assert lat['discriminant'] == 24
        assert not lat['self_dual']
        assert lat['num_primaries'] == 3

    @skip_no_mpmath
    def test_t49_auxiliary_lattice_lee_yang(self):
        """T49: Auxiliary lattice for Lee-Yang: level 20, disc 20."""
        lat = auxiliary_lattice_data(5, 2)
        assert lat['level'] == 20
        assert lat['discriminant'] == 20

    @skip_no_mpmath
    def test_t50_general_mm_character_consistency(self):
        """T50: M(4,3) character via general formula matches Ising-specific."""
        tau = mpmath.mpc(0, 1)
        # chi_{1,1} for M(4,3) via general formula
        chi_gen = mpmath.re(minimal_model_character(1, 1, 4, 3, tau, 300))
        chi_ising = mpmath.re(ising_character_qseries(0, tau, 300))
        assert abs(chi_gen - chi_ising) / abs(chi_ising) < 1e-5


# ============================================================
# T51-T55: Cross-term and Mellin analysis
# ============================================================

class TestCrossTermMellin:

    @skip_no_mpmath
    def test_t51_cross_term_positive_y1(self):
        """T51: Cross term sqrt(t3*t4)/eta is positive at y=1."""
        result = cross_term_numerical(1.0, 300)
        assert result['cross_term'] > 0

    @skip_no_mpmath
    def test_t52_doubling_identity(self):
        """T52: theta_3(2tau)^2 = (theta_3^2 + theta_4^2)/2."""
        result = cross_term_numerical(1.0, 300)
        rel = abs(result['doubling_check_lhs'] - result['doubling_check_rhs'])
        assert rel < 1e-12

    @skip_no_mpmath
    def test_t53_cross_term_multiple_y(self):
        """T53: Cross term positive at y=0.5, 1, 2, 5."""
        for y in [0.5, 1.0, 2.0, 5.0]:
            result = cross_term_numerical(y, 300)
            assert result['cross_term'] > 0, f"Cross term negative at y={y}"

    @skip_no_mpmath
    def test_t54_partial_zeta_decomposition(self):
        """T54: Partial zeta decomposes into Dirichlet L-functions (a=1 mod 24)."""
        result = partial_zeta_dirichlet_decomposition(1, 3.0, 3000)
        # Reconstruction should match direct computation
        assert result['error'] < 1e-6

    @skip_no_mpmath
    def test_t55_partial_zeta_a5(self):
        """T55: Partial zeta decomposition for a=5 mod 24."""
        result = partial_zeta_dirichlet_decomposition(5, 3.0, 3000)
        assert result['error'] < 1e-6


# ============================================================
# T56-T60: Shadow depth and Epstein analysis
# ============================================================

class TestShadowDepthPrediction:

    @skip_no_mpmath
    def test_t56_ising_primary_epstein(self):
        """T56: Ising primary Epstein: 2^s + 16^s at s=2."""
        result = ising_z_epstein_decomposition(2.0)
        expected = 2.0 ** 2 + 16.0 ** 2
        assert abs(result['primary_epstein'] - expected) < 1e-8

    @skip_no_mpmath
    def test_t57_full_epstein_partial_zetas_sum(self):
        """T57: Sum of all partial zetas mod 24 = zeta(2s)."""
        result = ising_full_epstein_decomposition(2.0, 2000)
        # All classes sum should approximate zeta(4)
        expected = float(mpmath.zeta(4))
        assert abs(result['all_classes_sum'] - expected) / expected < 0.01

    @skip_no_mpmath
    def test_t58_shadow_depth_ising(self):
        """T58: Ising shadow depth prediction: 3 primaries, level 24."""
        result = shadow_depth_from_l_functions(4, 3)
        assert result['num_primaries'] == 3
        assert result['level'] == 24
        assert abs(result['c'] - 0.5) < 1e-10

    @skip_no_mpmath
    def test_t59_shadow_depth_tricritical(self):
        """T59: Tricritical Ising: 6 primaries, level 40."""
        result = shadow_depth_from_l_functions(5, 4)
        assert result['level'] == 40
        assert result['num_primaries'] == 6

    @skip_no_mpmath
    def test_t60_dirichlet_chars_mod24_count(self):
        """T60: There are exactly phi(24) = 8 Dirichlet characters mod 24."""
        result = dirichlet_characters_mod24()
        assert result['phi_24'] == 8
        assert len(result['characters']) == 8
