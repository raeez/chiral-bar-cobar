r"""Tests for theorem_yangian_consistency_engine.

Narrow cross-chapter notation/convention consistency tests between
yangians_foundations.tex and yangians_drinfeld_kohno.tex.  Roughly 30-40
tests covering:

- kappa_einfty(g,k) = dim(g)(k+h^vee)/(2h^vee) for all standard simple types,
- Yang R-matrix unitarity and QYBE on fundamental of sl_2 and sl_3,
- qKZ (difference form) reduces to KZ (differential form) at first order in hbar,
- kappa additivity, sign conventions, and rational-value consistency,
- explicit test value kappa^{E_1}(Y(sl_2)) = hbar at level k=1.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import pytest

from compute.lib.theorem_yangian_consistency_engine import (
    YangianConsistencyReport,
    kappa_additivity_residual,
    kappa_e1_yangian_test_value,
    kappa_einfty,
    kz_connection_twosite,
    permutation_matrix,
    qkz_first_order_coefficient,
    qybe_residual,
    run_consistency_report,
    unitarity_residual,
    yang_R,
)


# -----------------------------------------------------------------------------
# 1. kappa_einfty: closed-form values (Part I landscape_census convention)
# -----------------------------------------------------------------------------


class TestKappaEinfty:
    """Verify kappa(g_k) = dim(g)(k + h^vee)/(2 h^vee) across simple types."""

    def test_sl2_level1(self):
        # dim sl_2 = 3, h^vee = 2; kappa = 3 * 3 / 4 = 9/4
        assert kappa_einfty("sl2", 1) == Fraction(9, 4)

    def test_sl2_level2(self):
        # 3 * 4 / 4 = 3
        assert kappa_einfty("sl2", 2) == Fraction(3, 1)

    def test_sl3_level1(self):
        # dim sl_3 = 8, h^vee = 3; kappa = 8 * 4 / 6 = 16/3
        assert kappa_einfty("sl3", 1) == Fraction(16, 3)

    def test_sl3_level2(self):
        # 8 * 5 / 6 = 20/3
        assert kappa_einfty("sl3", 2) == Fraction(20, 3)

    def test_sl4_level1(self):
        # dim sl_4 = 15, h^vee = 4; 15 * 5 / 8 = 75/8
        assert kappa_einfty("sl4", 1) == Fraction(75, 8)

    def test_sl5_level1(self):
        # 24 * 6 / 10 = 72/5
        assert kappa_einfty("sl5", 1) == Fraction(72, 5)

    def test_so5_level1(self):
        # dim so_5 = 10, h^vee = 3; 10 * 4 / 6 = 20/3
        assert kappa_einfty("so5", 1) == Fraction(20, 3)

    def test_so8_level1(self):
        # dim so_8 = 28, h^vee = 6; 28 * 7 / 12 = 49/3
        assert kappa_einfty("so8", 1) == Fraction(49, 3)

    def test_g2_level1(self):
        # 14 * 5 / 8 = 35/4
        assert kappa_einfty("g2", 1) == Fraction(35, 4)

    def test_f4_level1(self):
        # 52 * 10 / 18 = 260/9
        assert kappa_einfty("f4", 1) == Fraction(260, 9)

    def test_e8_level1(self):
        # 248 * 31 / 60 = 7688/60 = 1922/15
        assert kappa_einfty("e8", 1) == Fraction(1922, 15)

    def test_kappa_positive_at_positive_level(self):
        for g in ["sl2", "sl3", "sl4", "so5", "so8", "g2", "f4", "e6", "e7", "e8"]:
            for k in [1, 2, 3, 5, 10]:
                assert kappa_einfty(g, k) > 0

    def test_kappa_linear_in_level(self):
        # kappa(g, k2) - kappa(g, k1) = dim(g) * (k2 - k1) / (2 h^vee)
        # In particular, kappa(g, k+1) - kappa(g, k) is independent of k.
        for g in ["sl2", "sl3", "sl4", "e8"]:
            diffs = [kappa_einfty(g, k + 1) - kappa_einfty(g, k) for k in [1, 2, 3, 4]]
            assert len(set(diffs)) == 1

    def test_kappa_unknown_type_raises(self):
        with pytest.raises(KeyError):
            kappa_einfty("sl42", 1)


# -----------------------------------------------------------------------------
# 2. Yang R-matrix: permutation, unitarity, QYBE
# -----------------------------------------------------------------------------


class TestPermutationMatrix:
    def test_permutation_involution_N2(self):
        P = permutation_matrix(2)
        assert np.allclose(P @ P, np.eye(4))

    def test_permutation_involution_N3(self):
        P = permutation_matrix(3)
        assert np.allclose(P @ P, np.eye(9))

    def test_permutation_trace_N(self):
        # tr(P) = N (diagonal entries e_i otimes e_i map to themselves)
        for N in [2, 3, 4, 5]:
            P = permutation_matrix(N)
            assert np.isclose(np.trace(P), N)


class TestYangRUnitarity:
    """R(u) R(-u) = (1 - hbar^2/u^2) I."""

    def test_unitarity_sl2_u1(self):
        assert unitarity_residual(2, 1.0 + 0j, 1.0 + 0j) < 1e-12

    def test_unitarity_sl2_u_large(self):
        assert unitarity_residual(2, 10.0 + 0j, 1.0 + 0j) < 1e-12

    def test_unitarity_sl3_u1(self):
        assert unitarity_residual(3, 1.5 + 0j, 1.0 + 0j) < 1e-12

    def test_unitarity_sl4(self):
        assert unitarity_residual(4, 2.7 + 0j, 1.0 + 0j) < 1e-12

    def test_unitarity_hbar_half(self):
        # hbar rescaling: unitarity still exact (scalar becomes 1 - 1/(4u^2)).
        assert unitarity_residual(2, 3.0 + 0j, 0.5 + 0j) < 1e-12

    def test_unitarity_complex_spectral(self):
        assert unitarity_residual(2, 1.0 + 1.0j, 1.0 + 0j) < 1e-12


class TestQYBE:
    """R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)."""

    def test_qybe_sl2_generic(self):
        assert qybe_residual(2, 1.1 + 0j, 2.3 + 0j, 1.0 + 0j) < 1e-12

    def test_qybe_sl2_second_pair(self):
        assert qybe_residual(2, 3.7 + 0j, 0.6 + 0j, 1.0 + 0j) < 1e-12

    def test_qybe_sl3(self):
        assert qybe_residual(3, 1.3 + 0j, 2.5 + 0j, 1.0 + 0j) < 1e-11

    def test_qybe_sl2_hbar_half(self):
        assert qybe_residual(2, 1.2 + 0j, 2.4 + 0j, 0.5 + 0j) < 1e-12

    def test_qybe_sl2_complex(self):
        assert qybe_residual(2, 1.0 + 0.5j, 2.0 - 0.3j, 1.0 + 0j) < 1e-11


class TestYangRBasicStructure:
    def test_yang_R_at_infinity_is_identity(self):
        # R(u) -> I as u -> infinity.
        R_large = yang_R(2, 1e8 + 0j, 1.0 + 0j)
        assert np.allclose(R_large, np.eye(4), atol=1e-6)

    def test_yang_R_has_simple_pole_at_zero(self):
        # Residue of R(u) at u=0 is -hbar P.
        small = 1e-6
        R = yang_R(2, small + 0j, 1.0 + 0j)
        expected_leading = -permutation_matrix(2) / small
        # Check that the singular part dominates.
        diff = R - (np.eye(4) + expected_leading)
        assert np.linalg.norm(diff) < 1e-6

    def test_yang_R_N3_shape(self):
        R = yang_R(3, 2.0 + 0j)
        assert R.shape == (9, 9)


# -----------------------------------------------------------------------------
# 3. KZ / qKZ consistency: differential vs difference at O(hbar)
# -----------------------------------------------------------------------------


class TestKzVsQkz:
    """qKZ reduces to KZ at first order in hbar.

    The chapter states: "KZ is the DIFFERENTIAL form; qKZ is the DIFFERENCE form.
    Related by Kazhdan equivalence: rational (KZ) <-> trigonometric (qKZ)."
    This test verifies the infinitesimal compatibility.
    """

    def test_kz_qkz_first_order_match_sl2(self):
        z1, z2 = 0.0 + 0j, 1.0 + 0j
        hbar = 1.0 + 0j
        kz = kz_connection_twosite(2, z1, z2, hbar=hbar)
        qkz = qkz_first_order_coefficient(2, z1, z2, hbar=hbar)
        # KZ connection = hbar times first-order qKZ Taylor coefficient
        assert np.allclose(kz, hbar * qkz)

    def test_kz_qkz_first_order_match_sl3(self):
        z1, z2 = 0.5 + 0j, 2.5 + 0j
        kz = kz_connection_twosite(3, z1, z2)
        qkz = qkz_first_order_coefficient(3, z1, z2)
        assert np.allclose(kz, qkz)

    def test_kz_scaling_with_hbar(self):
        # KZ scales linearly in hbar.
        kz1 = kz_connection_twosite(2, 0.0 + 0j, 1.0 + 0j, hbar=1.0 + 0j)
        kz2 = kz_connection_twosite(2, 0.0 + 0j, 1.0 + 0j, hbar=2.0 + 0j)
        assert np.allclose(2 * kz1, kz2)

    def test_kz_pole_structure(self):
        # -hbar P / (z_1 - z_2): simple pole at coincident points.
        kz_far = kz_connection_twosite(2, 0.0 + 0j, 10.0 + 0j)
        kz_near = kz_connection_twosite(2, 0.0 + 0j, 0.1 + 0j)
        # Near diagonal norm should be 100 times the far-diagonal norm.
        ratio = np.linalg.norm(kz_near) / np.linalg.norm(kz_far)
        assert np.isclose(ratio, 100.0, rtol=1e-10)


# -----------------------------------------------------------------------------
# 4. kappa additivity and cross-family consistency
# -----------------------------------------------------------------------------


class TestKappaAdditivity:
    def test_additivity_trivial(self):
        # Definitional tautology; guards against later refactor breakage.
        assert kappa_additivity_residual("sl2", 1, "sl3", 1) == 0

    def test_additivity_self(self):
        assert kappa_additivity_residual("sl2", 1, "sl2", 1) == 0

    def test_additivity_mixed_levels(self):
        assert kappa_additivity_residual("sl3", 2, "e8", 1) == 0


# -----------------------------------------------------------------------------
# 5. kappa^{E_1} test value and SEPARATION from kappa^{E_infty}
# -----------------------------------------------------------------------------


class TestKappaE1SeparateFromEInfty:
    """AP9 defence: kappa^{E_1} and kappa^{E_infty} are DIFFERENT invariants.

    kappa^{E_infty}(g_k) is a rational number.
    kappa^{E_1}(Y(sl_2)) = hbar is a deformation parameter.
    They must never be conflated.
    """

    def test_e1_test_value_default(self):
        assert kappa_e1_yangian_test_value() == 1.0

    def test_e1_test_value_rescales_with_hbar(self):
        assert kappa_e1_yangian_test_value(0.5) == 0.5
        assert kappa_e1_yangian_test_value(2.0) == 2.0

    def test_e1_vs_einfty_are_different(self):
        # kappa^{E_infty}(sl_2, k=1) = 9/4; kappa^{E_1}(Y(sl_2)) = 1.
        # The two invariants are NOT numerically equal; they are categorically distinct.
        k_inf = float(kappa_einfty("sl2", 1))
        k_e1 = kappa_e1_yangian_test_value(1.0)
        assert not np.isclose(k_inf, k_e1)


# -----------------------------------------------------------------------------
# 6. Consistency report (bundled cross-chapter check)
# -----------------------------------------------------------------------------


class TestConsistencyReport:
    def test_report_assembles(self):
        rpt = run_consistency_report()
        assert isinstance(rpt, YangianConsistencyReport)

    def test_report_is_consistent(self):
        rpt = run_consistency_report()
        assert rpt.is_consistent()

    def test_report_kappa_values(self):
        rpt = run_consistency_report()
        assert rpt.kappa_sl2_k1 == Fraction(9, 4)
        assert rpt.kappa_sl3_k1 == Fraction(16, 3)

    def test_report_residuals_small(self):
        rpt = run_consistency_report()
        assert rpt.qybe_residual_sl2 < 1e-10
        assert rpt.unitarity_residual_sl2 < 1e-10
        assert rpt.kz_qkz_first_order_matches
