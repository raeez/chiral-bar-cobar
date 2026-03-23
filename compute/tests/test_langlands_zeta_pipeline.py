#!/usr/bin/env python3
r"""
test_langlands_zeta_pipeline.py — End-to-end pipeline: shadow tower -> zeta zeros.

Tests the full 6-stage chain:
  Shadow tower Theta_A^{<=r} -> partition function -> constrained Epstein
    -> Hecke decomposition -> L-functions -> zeros

T1-T10:   Stage 1 — Shadow extraction
T11-T18:  Stage 2 — Partition function
T19-T28:  Stage 3 — Constrained Epstein (exact vs direct)
T29-T37:  Stage 4 — Hecke decomposition
T38-T47:  Stage 5 — Zero location
T48-T53:  Stage 6 — Shadow-spectral verification
T54-T60:  Full pipeline integration
T61-T68:  Gap analysis (Virasoro/Ising)
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from langlands_zeta_pipeline import (
    voa_spec, extract_shadow_tower,
    compute_partition_function, eta_real, theta3_real, sigma_k,
    eisenstein_series_q, j_invariant,
    constrained_epstein_exact, constrained_epstein_direct,
    hecke_decompose, hecke_verify_numerically,
    compute_zeta_zeros, compute_L_function_zeros,
    verify_shadow_spectral,
    run_pipeline,
    virasoro_gap_analysis,
    pipeline_summary_table,
    SHADOW_DEPTH_CLASSES,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# Stage 1: Shadow extraction (T1-T10)
# ============================================================

class TestStage1ShadowExtraction:

    def test_t1_heisenberg_kappa(self):
        """T1: Heisenberg kappa = rank = 1."""
        spec = voa_spec('heisenberg')
        shadow = extract_shadow_tower(spec)
        assert shadow['kappa'] == 1

    def test_t2_v_z_kappa(self):
        """T2: V_Z kappa = rank = 1."""
        spec = voa_spec('V_Z')
        shadow = extract_shadow_tower(spec)
        assert shadow['kappa'] == 1

    def test_t3_v_e8_kappa(self):
        """T3: V_{E_8} kappa = rank = 8."""
        spec = voa_spec('V_E8')
        shadow = extract_shadow_tower(spec)
        assert shadow['kappa'] == 8

    def test_t4_v_leech_kappa(self):
        """T4: V_{Leech} kappa = rank = 24."""
        spec = voa_spec('V_Leech')
        shadow = extract_shadow_tower(spec)
        assert shadow['kappa'] == 24

    def test_t5_virasoro_kappa(self):
        """T5: Virasoro at c=25 has kappa = 12.5."""
        spec = voa_spec('virasoro', c=25)
        shadow = extract_shadow_tower(spec)
        assert shadow['kappa'] == 12.5

    def test_t6_shadow_depth_classes(self):
        """T6: Shadow depth classification G/L/C/M present."""
        assert 'G' in SHADOW_DEPTH_CLASSES
        assert 'L' in SHADOW_DEPTH_CLASSES
        assert 'C' in SHADOW_DEPTH_CLASSES
        assert 'M' in SHADOW_DEPTH_CLASSES
        assert SHADOW_DEPTH_CLASSES['G']['r_max'] == 2
        assert SHADOW_DEPTH_CLASSES['L']['r_max'] == 3
        assert SHADOW_DEPTH_CLASSES['C']['r_max'] == 4
        assert SHADOW_DEPTH_CLASSES['M']['r_max'] == float('inf')

    def test_t7_heisenberg_depth_2(self):
        """T7: Heisenberg has shadow depth 2 (class G)."""
        spec = voa_spec('heisenberg')
        shadow = extract_shadow_tower(spec)
        assert shadow['depth'] == 2
        assert shadow['shadow_class'] == 'G'

    def test_t8_e8_depth_3(self):
        """T8: V_{E_8} has shadow depth 3 (class L)."""
        spec = voa_spec('V_E8')
        shadow = extract_shadow_tower(spec)
        assert shadow['depth'] == 3
        assert shadow['shadow_class'] == 'L'

    def test_t9_leech_depth_4(self):
        """T9: V_{Leech} has shadow depth >= 4."""
        spec = voa_spec('V_Leech')
        shadow = extract_shadow_tower(spec)
        assert shadow['depth'] >= 4

    def test_t10_virasoro_q_contact(self):
        """T10: Virasoro Q^contact = 10/[c(5c+22)]."""
        for c in [0.5, 1.0, 2.0, 13.0, 25.0]:
            spec = voa_spec('virasoro', c=c)
            shadow = extract_shadow_tower(spec)
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(shadow['Q_contact'] - expected) < 1e-14, (
                f"Q_contact mismatch at c={c}"
            )


# ============================================================
# Stage 2: Partition function (T11-T18)
# ============================================================

class TestStage2PartitionFunction:

    def test_t11_eta_positive(self):
        """T11: eta(iy) is positive for y > 0."""
        for y in [0.1, 0.5, 1.0, 2.0, 5.0]:
            assert eta_real(y) > 0

    def test_t12_theta3_ge_1(self):
        """T12: theta_3(iy) >= 1 for all y > 0."""
        for y in [0.1, 0.5, 1.0, 2.0, 10.0]:
            assert theta3_real(y) >= 1.0

    def test_t13_v_z_partition_positive(self):
        """T13: V_Z partition function is positive."""
        spec = voa_spec('V_Z')
        shadow = extract_shadow_tower(spec)
        for y in [0.5, 1.0, 2.0]:
            result = compute_partition_function(spec, shadow, y)
            assert result['Z'] > 0

    def test_t14_v_z_partition_formula(self):
        """T14: V_Z partition Z = theta_3^2 / eta^2."""
        spec = voa_spec('V_Z')
        shadow = extract_shadow_tower(spec)
        for y in [0.5, 1.0, 2.0]:
            result = compute_partition_function(spec, shadow, y)
            expected = theta3_real(y) ** 2 / eta_real(y) ** 2
            assert abs(result['Z'] - expected) / expected < 1e-10

    def test_t15_primary_counting_positive(self):
        """T15: hat{Z} = y^{c/2} |eta|^{2c} Z is positive."""
        for voa_type in ['V_Z', 'V_E8']:
            spec = voa_spec(voa_type)
            shadow = extract_shadow_tower(spec)
            result = compute_partition_function(spec, shadow, 1.0)
            assert result['Z_hat'] > 0, f"Z_hat negative for {voa_type}"

    @skip_no_mpmath
    def test_t16_e8_partition_from_e4(self):
        """T16: V_{E_8} partition involves E_4."""
        spec = voa_spec('V_E8')
        shadow = extract_shadow_tower(spec)
        y = 1.0
        result = compute_partition_function(spec, shadow, y)
        # E_4^2 / eta^16
        E4 = eisenstein_series_q(4, y)
        eta_val = eta_real(y)
        expected = E4 ** 2 / eta_val ** 16
        assert abs(result['Z'] - expected) / abs(expected) < 1e-8

    def test_t17_virasoro_partition_formula(self):
        """T17: Virasoro partition Z = |chi_c|^2 = |q^{(c-1)/24}/eta|^2."""
        c = 2.0
        spec = voa_spec('virasoro', c=c)
        shadow = extract_shadow_tower(spec)
        y = 1.0
        result = compute_partition_function(spec, shadow, y)
        import math
        eta_val = eta_real(y)
        q_power = math.exp(-2 * math.pi * y * (c - 1) / 24)
        expected = (q_power / eta_val) ** 2
        assert abs(result['Z'] - expected) / abs(expected) < 1e-10

    def test_t18_sigma_k_basic(self):
        """T18: sigma_k function correctness."""
        # sigma_0(6) = 4 (divisors: 1,2,3,6)
        assert sigma_k(6, 0) == 4
        # sigma_1(6) = 1+2+3+6 = 12
        assert sigma_k(6, 1) == 12
        # sigma_3(1) = 1
        assert sigma_k(1, 3) == 1
        # sigma_3(2) = 1 + 8 = 9
        assert sigma_k(2, 3) == 9


# ============================================================
# Stage 3: Constrained Epstein (T19-T28)
# ============================================================

class TestStage3ConstrainedEpstein:

    @skip_no_mpmath
    def test_t19_v_z_epstein_exact(self):
        """T19: V_Z epsilon^1_s = 4*zeta(2s) at s=2."""
        spec = voa_spec('V_Z')
        val = constrained_epstein_exact(spec, 2.0)
        expected = complex(4 * mpmath.zeta(4))
        assert abs(val - expected) / abs(expected) < 1e-12

    @skip_no_mpmath
    def test_t20_v_z_exact_vs_direct(self):
        """T20: V_Z exact and direct summation agree."""
        spec = voa_spec('V_Z')
        for s in [2.0, 3.0, 4.5]:
            exact = constrained_epstein_exact(spec, s)
            direct = constrained_epstein_direct(spec, s, nmax=500)
            assert abs(exact - direct) / abs(exact) < 1e-3, (
                f"V_Z epstein disagreement at s={s}: exact={exact}, direct={direct}"
            )

    @skip_no_mpmath
    def test_t21_e8_epstein_exact(self):
        """T21: V_{E_8} epsilon = 240*4^{-s}*zeta(s)*zeta(s-3)."""
        spec = voa_spec('V_E8')
        s = 5.0
        val = constrained_epstein_exact(spec, s)
        expected = complex(
            240 * mpmath.power(4, -s) * mpmath.zeta(s) * mpmath.zeta(s - 3)
        )
        assert abs(val - expected) / abs(expected) < 1e-12

    @skip_no_mpmath
    def test_t22_e8_exact_vs_direct(self):
        """T22: V_{E_8} exact and direct summation agree."""
        spec = voa_spec('V_E8')
        for s in [5.0, 6.0, 8.0]:
            exact = constrained_epstein_exact(spec, s)
            direct = constrained_epstein_direct(spec, s, nmax=200)
            if abs(exact) > 1e-10:
                rel_err = abs(exact - direct) / abs(exact)
                assert rel_err < 0.05, (
                    f"E8 epstein disagreement at s={s}: rel_err={rel_err}"
                )

    @skip_no_mpmath
    def test_t23_leech_epstein_computable(self):
        """T23: V_{Leech} Epstein zeta is computable."""
        spec = voa_spec('V_Leech')
        val = constrained_epstein_exact(spec, 15.0)
        assert np.isfinite(val.real)

    @skip_no_mpmath
    def test_t24_leech_exact_vs_direct(self):
        """T24: V_{Leech} exact and direct summation agree (lower precision)."""
        spec = voa_spec('V_Leech')
        s = 15.0
        exact = constrained_epstein_exact(spec, s)
        direct = constrained_epstein_direct(spec, s, nmax=100)
        if abs(exact) > 1e-10:
            rel_err = abs(exact - direct) / abs(exact)
            assert rel_err < 0.1, (
                f"Leech epstein disagreement at s={s}: rel_err={rel_err}"
            )

    def test_t25_virasoro_epstein_fails(self):
        """T25: Virasoro has no exact Epstein formula (expected failure)."""
        spec = voa_spec('virasoro', c=0.5)
        with pytest.raises(ValueError, match="non-lattice"):
            constrained_epstein_exact(spec, 2.0)

    @skip_no_mpmath
    def test_t26_v_z_zeta_relation(self):
        """T26: V_Z Epstein is 4*zeta(2s) — fundamental identity."""
        spec = voa_spec('V_Z')
        for s_val in [1.5, 2.0, 3.0, 5.0]:
            eps = constrained_epstein_exact(spec, s_val)
            zeta_val = complex(4 * mpmath.zeta(2 * s_val))
            assert abs(eps - zeta_val) / abs(zeta_val) < 1e-12

    @skip_no_mpmath
    def test_t27_e8_convergence_with_nmax(self):
        """T27: E8 direct summation converges as nmax increases."""
        spec = voa_spec('V_E8')
        s = 6.0
        exact = constrained_epstein_exact(spec, s)
        prev_err = float('inf')
        for nmax in [50, 100, 200]:
            direct = constrained_epstein_direct(spec, s, nmax=nmax)
            err = abs(exact - direct) / abs(exact)
            assert err < prev_err or err < 1e-6
            prev_err = err

    @skip_no_mpmath
    def test_t28_heisenberg_equals_v_z(self):
        """T28: Heisenberg and V_Z give identical Epstein zeta."""
        spec_h = voa_spec('heisenberg')
        spec_z = voa_spec('V_Z')
        for s_val in [2.0, 3.5, 5.0]:
            eps_h = constrained_epstein_exact(spec_h, s_val)
            eps_z = constrained_epstein_exact(spec_z, s_val)
            assert abs(eps_h - eps_z) < 1e-14


# ============================================================
# Stage 4: Hecke decomposition (T29-T37)
# ============================================================

class TestStage4HeckeDecomposition:

    def test_t29_v_z_one_factor(self):
        """T29: V_Z Hecke decomposition has 1 L-factor."""
        spec = voa_spec('V_Z')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        assert hecke['n_factors'] == 1

    def test_t30_e8_two_factors(self):
        """T30: V_{E_8} Hecke decomposition has 2 L-factors."""
        spec = voa_spec('V_E8')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        assert hecke['n_factors'] == 2

    def test_t31_leech_three_factors(self):
        """T31: V_{Leech} Hecke decomposition has 3 L-factors."""
        spec = voa_spec('V_Leech')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        assert hecke['n_factors'] == 3

    def test_t32_virasoro_has_gap(self):
        """T32: Virasoro Hecke decomposition identifies the gap."""
        spec = voa_spec('virasoro', c=0.5)
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        assert hecke['n_factors'] == 0
        assert 'gap' in hecke
        assert hecke['gap'] == 'VVMF_Hecke'

    def test_t33_v_z_critical_line(self):
        """T33: V_Z has 1 critical line at Re(s) = 1/4."""
        spec = voa_spec('V_Z')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        assert len(hecke['critical_lines']) == 1
        assert abs(hecke['critical_lines'][0] - 0.25) < 1e-12

    def test_t34_e8_critical_lines(self):
        """T34: V_{E_8} has critical lines at Re(s) = 1/2 and 7/2."""
        spec = voa_spec('V_E8')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        lines = sorted(hecke['critical_lines'])
        assert len(lines) == 2
        assert abs(lines[0] - 0.5) < 1e-12
        assert abs(lines[1] - 3.5) < 1e-12

    def test_t35_leech_critical_lines(self):
        """T35: V_{Leech} has critical lines at Re(s) = 1/2, 6, 23/2."""
        spec = voa_spec('V_Leech')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        lines = sorted(hecke['critical_lines'])
        assert len(lines) == 3
        assert abs(lines[0] - 0.5) < 1e-12
        assert abs(lines[1] - 6.0) < 1e-12
        assert abs(lines[2] - 11.5) < 1e-12

    @skip_no_mpmath
    def test_t36_hecke_numerical_verification_v_z(self):
        """T36: V_Z Hecke factorization verified numerically."""
        spec = voa_spec('V_Z')
        exact, factored, rel_err = hecke_verify_numerically(spec, s_test=3.0)
        assert rel_err < 1e-12

    @skip_no_mpmath
    def test_t37_hecke_numerical_verification_e8(self):
        """T37: V_{E_8} Hecke factorization verified numerically."""
        spec = voa_spec('V_E8')
        exact, factored, rel_err = hecke_verify_numerically(spec, s_test=5.0)
        assert rel_err < 1e-12


# ============================================================
# Stage 5: Zero location (T38-T47)
# ============================================================

class TestStage5ZeroLocation:

    @skip_no_mpmath
    def test_t38_first_zeta_zero(self):
        """T38: First Riemann zeta zero at gamma_1 ~ 14.1347."""
        zeros = compute_zeta_zeros(n_zeros=1)
        assert len(zeros) == 1
        gamma1 = zeros[0].imag
        assert abs(gamma1 - 14.134725) < 0.001

    @skip_no_mpmath
    def test_t39_twenty_zeta_zeros(self):
        """T39: First 20 zeta zeros all on Re(s) = 1/2."""
        zeros = compute_zeta_zeros(n_zeros=20)
        assert len(zeros) == 20
        for z in zeros:
            assert abs(z.real - 0.5) < 1e-10

    @skip_no_mpmath
    def test_t40_v_z_zeros_at_quarter(self):
        """T40: V_Z zeros at Re(s) = 1/4 (from zeta(2s))."""
        spec = voa_spec('V_Z')
        zeros = compute_L_function_zeros(spec, n_zeros=5)
        factor_zeros = zeros['zeta(2s)']
        assert len(factor_zeros) == 5
        for z in factor_zeros:
            assert abs(z.real - 0.25) < 1e-10

    @skip_no_mpmath
    def test_t41_e8_zeros_line_half(self):
        """T41: V_{E_8} has zeros on Re(s) = 1/2 (from zeta(s))."""
        spec = voa_spec('V_E8')
        zeros = compute_L_function_zeros(spec, n_zeros=5)
        for z in zeros['zeta(s)']:
            assert abs(z.real - 0.5) < 1e-10

    @skip_no_mpmath
    def test_t42_e8_zeros_line_three_half(self):
        """T42: V_{E_8} has zeros on Re(s) = 7/2 (from zeta(s-3))."""
        spec = voa_spec('V_E8')
        zeros = compute_L_function_zeros(spec, n_zeros=5)
        for z in zeros['zeta(s-3)']:
            assert abs(z.real - 3.5) < 1e-10

    @skip_no_mpmath
    def test_t43_e8_zero_imaginary_parts_match(self):
        """T43: E8 zeros from zeta(s) and zeta(s-3) share imaginary parts."""
        spec = voa_spec('V_E8')
        zeros = compute_L_function_zeros(spec, n_zeros=10)
        gammas_line1 = sorted([z.imag for z in zeros['zeta(s)']])
        gammas_line2 = sorted([z.imag for z in zeros['zeta(s-3)']])
        for g1, g2 in zip(gammas_line1, gammas_line2):
            assert abs(g1 - g2) < 1e-8

    @skip_no_mpmath
    def test_t44_leech_zeros_three_families(self):
        """T44: V_{Leech} zeros come from 3 L-function families."""
        spec = voa_spec('V_Leech')
        zeros = compute_L_function_zeros(spec, n_zeros=5)
        assert 'zeta(s)' in zeros
        assert 'zeta(s-11)' in zeros
        assert 'L(s, Delta_12)' in zeros

    @skip_no_mpmath
    def test_t45_leech_zeta_zeros_on_half(self):
        """T45: V_{Leech} zeta(s) zeros on Re(s) = 1/2."""
        spec = voa_spec('V_Leech')
        zeros = compute_L_function_zeros(spec, n_zeros=5)
        for z in zeros['zeta(s)']:
            assert abs(z.real - 0.5) < 1e-10

    @skip_no_mpmath
    def test_t46_leech_shifted_zeta_on_11_5(self):
        """T46: V_{Leech} zeta(s-11) zeros on Re(s) = 11.5."""
        spec = voa_spec('V_Leech')
        zeros = compute_L_function_zeros(spec, n_zeros=5)
        for z in zeros['zeta(s-11)']:
            assert abs(z.real - 11.5) < 1e-10

    @skip_no_mpmath
    def test_t47_virasoro_zeros_gap(self):
        """T47: Virasoro zero computation identifies the gap."""
        spec = voa_spec('virasoro', c=0.5)
        zeros = compute_L_function_zeros(spec, n_zeros=5)
        assert 'gap' in zeros

    @skip_no_mpmath
    def test_t47b_leech_ramanujan_L_zeros(self):
        """T47b: V_{Leech} L(s, Delta_12) zeros near Re(s) = 6."""
        spec = voa_spec('V_Leech')
        zeros = compute_L_function_zeros(spec, n_zeros=3)
        L_zeros = zeros.get('L(s, Delta_12)', [])
        # The Ramanujan L-function has zeros on Re(s)=6 (center of critical strip)
        # Due to finite truncation in the Dirichlet series, we check approximate location
        if len(L_zeros) > 0:
            for z in L_zeros:
                # Should be approximately on Re(s)=6 (within truncation error)
                assert abs(z.real - 6.0) < 0.5, (
                    f"L(s,Delta_12) zero at s={z}, expected Re(s) near 6"
                )


# ============================================================
# Stage 6: Shadow-spectral verification (T48-T53)
# ============================================================

class TestStage6Verification:

    def test_t48_v_z_depth_lines_match(self):
        """T48: V_Z: depth 2 -> 1 critical line."""
        spec = voa_spec('V_Z')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        result = verify_shadow_spectral(spec, shadow, hecke)
        assert result['verified'] is True
        assert result['depth'] == 2
        assert result['critical_lines'] == 1

    def test_t49_e8_depth_lines_match(self):
        """T49: V_{E_8}: depth 3 -> 2 critical lines."""
        spec = voa_spec('V_E8')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        result = verify_shadow_spectral(spec, shadow, hecke)
        assert result['verified'] is True
        assert result['depth'] == 3
        assert result['critical_lines'] == 2

    def test_t50_leech_depth_lines_match(self):
        """T50: V_{Leech}: depth 4 -> 3 critical lines."""
        spec = voa_spec('V_Leech')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        result = verify_shadow_spectral(spec, shadow, hecke)
        assert result['verified'] is True
        assert result['depth'] == 4
        assert result['critical_lines'] == 3

    def test_t51_virasoro_not_applicable(self):
        """T51: Virasoro verification returns NOT_APPLICABLE."""
        spec = voa_spec('virasoro', c=0.5)
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        result = verify_shadow_spectral(spec, shadow, hecke)
        assert result['status'] == 'NOT_APPLICABLE'

    def test_t52_all_lattice_algebras_pass(self):
        """T52: All lattice VOAs pass shadow-spectral verification."""
        for voa_type in ['V_Z', 'V_E8', 'V_Leech']:
            spec = voa_spec(voa_type)
            shadow = extract_shadow_tower(spec)
            hecke = hecke_decompose(spec, shadow)
            result = verify_shadow_spectral(spec, shadow, hecke)
            assert result['verified'] is True, f"Failed for {voa_type}"
            assert result['status'] == 'PASS'

    def test_t53_heisenberg_same_as_v_z(self):
        """T53: Heisenberg verification identical to V_Z."""
        spec = voa_spec('heisenberg')
        shadow = extract_shadow_tower(spec)
        hecke = hecke_decompose(spec, shadow)
        result = verify_shadow_spectral(spec, shadow, hecke)
        assert result['verified'] is True
        assert result['depth'] == 2
        assert result['critical_lines'] == 1


# ============================================================
# Full pipeline integration (T54-T60)
# ============================================================

class TestFullPipeline:

    @skip_no_mpmath
    def test_t54_v_z_full_pipeline(self):
        """T54: V_Z full pipeline completes without gaps."""
        result = run_pipeline('V_Z', y=1.0, n_zeros=5)
        assert result['pipeline_complete'] is True
        assert len(result['gaps']) == 0
        assert result['stage3_epstein']['status'] == 'OK'
        assert result['stage6_verification']['verified'] is True

    @skip_no_mpmath
    def test_t55_e8_full_pipeline(self):
        """T55: V_{E_8} full pipeline completes without gaps."""
        result = run_pipeline('V_E8', y=1.0, n_zeros=5)
        assert result['pipeline_complete'] is True
        assert result['stage6_verification']['verified'] is True

    @skip_no_mpmath
    def test_t56_leech_full_pipeline(self):
        """T56: V_{Leech} full pipeline completes without gaps."""
        result = run_pipeline('V_Leech', y=1.0, n_zeros=3)
        assert result['pipeline_complete'] is True
        assert result['stage6_verification']['verified'] is True

    @skip_no_mpmath
    def test_t57_virasoro_pipeline_has_gaps(self):
        """T57: Virasoro pipeline identifies gaps."""
        result = run_pipeline('virasoro', y=1.0, n_zeros=5, c=0.5)
        assert result['pipeline_complete'] is False
        assert len(result['gaps']) > 0

    @skip_no_mpmath
    def test_t58_epstein_agreement_all_lattice(self):
        """T58: Exact vs direct Epstein agree for all lattice VOAs."""
        for voa_type in ['V_Z', 'V_E8']:
            result = run_pipeline(voa_type, y=1.0, n_zeros=3)
            eps = result['stage3_epstein']
            assert eps['status'] == 'OK'
            assert eps['agreement'] < 0.05, (
                f"Epstein agreement > 5% for {voa_type}: {eps['agreement']}"
            )

    @skip_no_mpmath
    def test_t59_pipeline_stages_consistent(self):
        """T59: Pipeline stages are mutually consistent."""
        result = run_pipeline('V_E8', y=1.0, n_zeros=5)
        # Shadow depth from stage 1
        depth = result['stage1_shadow']['depth']
        # Critical lines from stage 4
        n_lines = len(result['stage4_hecke']['critical_lines'])
        # Verification from stage 6
        assert result['stage6_verification']['depth'] == depth
        assert result['stage6_verification']['critical_lines'] == n_lines
        assert depth - 1 == n_lines

    @skip_no_mpmath
    def test_t60_heisenberg_identical_to_v_z(self):
        """T60: Heisenberg pipeline results match V_Z."""
        h_result = run_pipeline('heisenberg', y=1.0, n_zeros=5)
        z_result = run_pipeline('V_Z', y=1.0, n_zeros=5)
        assert h_result['pipeline_complete'] == z_result['pipeline_complete']
        assert (
            h_result['stage1_shadow']['kappa']
            == z_result['stage1_shadow']['kappa']
        )


# ============================================================
# Gap analysis (T61-T68)
# ============================================================

class TestGapAnalysis:

    def test_t61_ising_gap_at_stage_3(self):
        """T61: Ising model (c=1/2) Approach A obstructed at stage 3."""
        analysis = virasoro_gap_analysis(c=0.5)
        assert analysis['first_failure_stage'] == 3
        assert analysis['stage1']['status'] == 'OK'
        assert analysis['stage3']['status'] == 'OBSTRUCTION'

    def test_t62_ising_kappa_correct(self):
        """T62: Ising kappa = c/2 = 1/4."""
        analysis = virasoro_gap_analysis(c=0.5)
        assert analysis['stage1']['kappa'] == 0.25

    def test_t63_ising_q_contact(self):
        """T63: Ising Q^contact = 10/(0.5 * (2.5+22)) = 10/(0.5*24.5) = 10/12.25."""
        analysis = virasoro_gap_analysis(c=0.5)
        c = 0.5
        expected = 10.0 / (c * (5 * c + 22))
        assert abs(analysis['stage1']['Q_contact'] - expected) < 1e-14
        # Numerical value: 10/12.25 = 40/49 ~ 0.8163
        assert abs(expected - 40.0 / 49.0) < 1e-14

    def test_t64_ising_spectrum_finite(self):
        """T64: Ising primary spectrum is finite (3 primaries)."""
        analysis = virasoro_gap_analysis(c=0.5)
        primaries = analysis['stage3']['ising_spectrum']['primaries']
        assert len(primaries) == 3
        assert 0 in primaries
        assert 0.5 in primaries

    def test_t65_gap_identifies_obstruction(self):
        """T65: Gap analysis identifies multiplicativity + VVMF obstruction."""
        analysis = virasoro_gap_analysis(c=0.5)
        desc = analysis['obstruction_description']
        assert 'multiplicativity' in desc
        assert 'VVMF Hecke' in desc or 'Roelcke-Selberg' in desc

    def test_t66_stage4_blocked_for_approach_a(self):
        """T66: Stage 4 Approach A blocked; Approaches B/D resolve it."""
        analysis = virasoro_gap_analysis(c=0.5)
        assert analysis['stage4']['status'] == 'BLOCKED_FOR_APPROACH_A'
        assert len(analysis['stage4']['resolved_by']) >= 2

    def test_t67_generic_virasoro_same_obstruction(self):
        """T67: Generic Virasoro c=25.5 has same obstruction structure."""
        analysis = virasoro_gap_analysis(c=25.5)
        assert analysis['first_failure_stage'] == 3
        assert analysis['stage1']['status'] == 'OK'
        assert analysis['stage3']['status'] == 'OBSTRUCTION'

    def test_t68_gap_needed_and_resolved_lists(self):
        """T68: Stage 4 identifies needed inputs AND resolution approaches."""
        analysis = virasoro_gap_analysis(c=0.5)
        needed = analysis['stage4']['needed_for_approach_A']
        assert len(needed) >= 3
        assert any('Franc-Mason' in n for n in needed)
        resolved = analysis['stage4']['resolved_by']
        assert len(resolved) >= 2
        assert any('Roelcke-Selberg' in r or 'VVMF' in r for r in resolved)


# ============================================================
# Summary table and structural tests (T69-T73)
# ============================================================

class TestStructural:

    def test_t69_summary_table(self):
        """T69: Pipeline summary table is complete."""
        table = pipeline_summary_table()
        assert len(table) >= 4  # V_Z, V_E8, V_Leech, virasoro(s)

    def test_t70_all_lattice_complete(self):
        """T70: All lattice algebras show COMPLETE status."""
        table = pipeline_summary_table()
        for row in table:
            if 'virasoro' not in row['algebra']:
                assert row['pipeline_status'] == 'COMPLETE', (
                    f"Expected COMPLETE for {row['algebra']}, got {row['pipeline_status']}"
                )

    def test_t71_virasoro_show_gap(self):
        """T71: Virasoro entries show GAP status."""
        table = pipeline_summary_table()
        for row in table:
            if 'virasoro' in row['algebra']:
                assert row['pipeline_status'] == 'GAP'

    def test_t72_kappa_positive_for_standard_families(self):
        """T72: kappa > 0 for all standard families in the summary table."""
        table = pipeline_summary_table()
        for row in table:
            assert row['kappa'] > 0, f"kappa should be positive for {row['algebra']}"

    def test_t73_depth_vs_critical_lines(self):
        """T73: For complete pipelines, #(critical lines) = depth - 1."""
        table = pipeline_summary_table()
        for row in table:
            if row['pipeline_status'] == 'COMPLETE':
                assert len(row['critical_lines']) == row['depth'] - 1, (
                    f"Mismatch for {row['algebra']}: "
                    f"{len(row['critical_lines'])} lines vs depth {row['depth']}"
                )
