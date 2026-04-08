r"""Tests for the factorization Yangian unification engine.

Verifies that the three constructions of Yangian-type algebras (AN, DNP, MK)
produce the same R-matrix, the same YBE, and the same non-renormalization
condition at genus 0, while the MK genus-1 correction is consistent and
has no analogue in the other two.

Multi-path verification strategy (CLAUDE.md mandate: 3+ independent paths):
  Path 1: Direct matrix computation (AN vs DNP vs MK)
  Path 2: Eigenvalue/eigenspace analysis (sym/antisym decomposition)
  Path 3: Yang-Baxter equation in all three interpretations
  Path 4: Unitarity / inverse R-matrix identity
  Path 5: Genus-1 modular correction (MK exclusive)
  Path 6: Kappa consistency across frameworks
  Path 7: Degeneration limits (hbar -> 0, tau -> i*infty)
  Path 8: Transfer matrix commutativity

Ground truth references:
  - yangians_foundations.tex: prop:dg-shifted-comparison
  - yangians_drinfeld_kohno.tex: def:modular-yangian-pro
  - DNP arXiv:2508.11749, AN arXiv:2512.16996
  - ordered_modular_bar.py: genus-1 correction
  - landscape_census.tex: kappa values (AP1)
"""

import numpy as np
import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.theorem_factorization_yangian_unification_engine import (
    LIE_DATA,
    permutation_matrix,
    yang_r_matrix,
    yang_r_matrix_inverse,
    AbedinNiuYangian,
    DimofteNiuPyYangian,
    ModularYangianMK,
    verify_r_matrix_unification,
    verify_yang_baxter_unification,
    verify_nonrenormalization_unification,
    compute_genus1_modular_correction,
    verify_koszul_dual_r_matrix_unification,
    full_unification_summary,
    _embed_13,
    _weierstrass_p,
)


# ============================================================
#  Part 1: Permutation matrix and basic R-matrix properties
# ============================================================


class TestPermutationMatrix:
    """Test the permutation operator P on C^N tensor C^N."""

    def test_p_squared_is_identity_sl2(self):
        """P^2 = I for N = 2."""
        P = permutation_matrix(2)
        np.testing.assert_allclose(P @ P, np.eye(4), atol=1e-14)

    def test_p_squared_is_identity_sl3(self):
        """P^2 = I for N = 3."""
        P = permutation_matrix(3)
        np.testing.assert_allclose(P @ P, np.eye(9), atol=1e-14)

    def test_p_squared_is_identity_sl4(self):
        """P^2 = I for N = 4."""
        P = permutation_matrix(4)
        np.testing.assert_allclose(P @ P, np.eye(16), atol=1e-14)

    def test_p_eigenvalues(self):
        """P has eigenvalues +1 (sym) and -1 (antisym)."""
        for N in [2, 3, 4]:
            P = permutation_matrix(N)
            eigvals = np.sort(np.real(np.linalg.eigvals(P)))
            n_sym = N * (N + 1) // 2
            n_anti = N * (N - 1) // 2
            assert np.sum(np.abs(eigvals - 1) < 1e-10) == n_sym
            assert np.sum(np.abs(eigvals + 1) < 1e-10) == n_anti

    def test_p_trace(self):
        """tr(P) = N (number of diagonal elements e_i tensor e_i)."""
        for N in [2, 3, 4, 5]:
            P = permutation_matrix(N)
            assert abs(np.trace(P) - N) < 1e-14

    def test_p_is_symmetric(self):
        """P is a real symmetric matrix (P^T = P)."""
        for N in [2, 3, 4]:
            P = permutation_matrix(N)
            np.testing.assert_allclose(P, P.T, atol=1e-14)


# ============================================================
#  Part 2: R-matrix unification (AN = DNP = MK at genus 0)
# ============================================================


class TestRMatrixUnification:
    """Test that all three frameworks produce the same R-matrix."""

    def test_sl2_r_matrix_three_way(self):
        """AN = DNP = MK for sl_2 at specific spectral parameter."""
        result = verify_r_matrix_unification(N=2, u=3.0, hbar=1.0)
        assert result["path1_all_agree"]
        assert result["path3_unitarity_holds"]

    def test_sl3_r_matrix_three_way(self):
        """AN = DNP = MK for sl_3."""
        result = verify_r_matrix_unification(N=3, u=4.0, hbar=0.5)
        assert result["path1_all_agree"]
        assert result["path3_unitarity_holds"]

    def test_sl4_r_matrix_three_way(self):
        """AN = DNP = MK for sl_4."""
        result = verify_r_matrix_unification(N=4, u=5.0, hbar=1.0)
        assert result["path1_all_agree"]
        assert result["path3_unitarity_holds"]

    def test_r_matrix_identity_at_infinity(self):
        """R(u) -> I as u -> infinity (all three frameworks)."""
        for N in [2, 3, 4]:
            R = yang_r_matrix(N, 1e10, 1.0)
            np.testing.assert_allclose(R, np.eye(N * N), atol=1e-6)

    def test_r_matrix_eigenvalues_sl2(self):
        """sl_2 R-matrix eigenvalues: 1 - hbar/u on sym, 1 + hbar/u on anti."""
        u, hbar = 5.0, 1.0
        R = yang_r_matrix(2, u, hbar)
        eigvals = np.sort(np.real(np.linalg.eigvals(R)))
        expected_anti = 1 + hbar / u  # 1 antisym eigenvalue for sl_2
        expected_sym = 1 - hbar / u   # 3 sym eigenvalues for sl_2
        assert abs(eigvals[0] - expected_sym) < 1e-10
        assert abs(eigvals[-1] - expected_anti) < 1e-10

    def test_unitarity_condition(self):
        """R(u)R(-u) = (1 - hbar^2/u^2)I for all N."""
        for N in [2, 3]:
            u, hbar = 4.0, 1.0
            R_pos = yang_r_matrix(N, u, hbar)
            R_neg = yang_r_matrix(N, -u, hbar)
            product = R_pos @ R_neg
            expected = (1 - hbar ** 2 / u ** 2) * np.eye(N * N)
            np.testing.assert_allclose(product, expected, atol=1e-12)

    def test_r_matrix_pole_at_zero(self):
        """R(u) has a pole at u = 0."""
        with pytest.raises(ValueError, match="pole"):
            yang_r_matrix(2, 0.0)

    def test_multiple_hbar_values(self):
        """Unification holds for various hbar values."""
        for hbar in [0.1, 0.5, 1.0, 2.0, 5.0]:
            result = verify_r_matrix_unification(N=2, u=3.0, hbar=hbar)
            assert result["path1_all_agree"], f"Failed at hbar={hbar}"


# ============================================================
#  Part 3: Yang-Baxter equation (qKZ = A_infty YBE = MC)
# ============================================================


class TestYangBaxterUnification:
    """Test that YBE holds in all three interpretations."""

    def test_sl2_yb(self):
        """Yang-Baxter for sl_2."""
        result = verify_yang_baxter_unification(N=2, u=3.0, v=2.0)
        assert result["path1_yb_holds"]
        assert result["path2_vec_holds"]
        assert result["path3_transfer_commutes"]

    def test_sl3_yb(self):
        """Yang-Baxter for sl_3."""
        result = verify_yang_baxter_unification(N=3, u=4.0, v=1.5)
        assert result["path1_yb_holds"]
        assert result["path2_vec_holds"]

    def test_sl4_yb(self):
        """Yang-Baxter for sl_4."""
        result = verify_yang_baxter_unification(N=4, u=5.0, v=3.0)
        assert result["path1_yb_holds"]

    def test_yb_multiple_parameters(self):
        """YBE holds for various (u, v) pairs with u != v."""
        for u, v in [(3.0, 1.0), (5.0, 2.0), (7.0, 3.5), (10.0, 1.0)]:
            result = verify_yang_baxter_unification(N=2, u=u, v=v)
            assert result["path1_yb_holds"], f"YBE failed at u={u}, v={v}"

    def test_yb_interpretations_documented(self):
        """All three interpretations are present."""
        result = verify_yang_baxter_unification(N=2, u=3.0, v=2.0)
        assert result["an_interpretation"] == "qKZ flatness"
        assert result["dnp_interpretation"] == "A_infty YBE (genus-0 MC)"
        assert result["mk_interpretation"] == "stable-graph YBE genus-0 sector"


# ============================================================
#  Part 4: Non-renormalization = Koszulness
# ============================================================


class TestNonrenormalizationUnification:
    """Test the three-way non-renormalization identity."""

    def test_identification_present(self):
        """The identification string is correct."""
        result = verify_nonrenormalization_unification()
        assert "E_2-collapse" in result["identification"]
        assert "Koszul" in result["identification"]

    def test_scope_documented(self):
        """All three scopes are documented."""
        result = verify_nonrenormalization_unification()
        assert "cotangent" in result["scope"]["an"]
        assert "quasi-linear" in result["scope"]["dnp"]
        assert "PBW" in result["scope"]["mk"]

    def test_mk_extends_beyond(self):
        """MK extends to non-quadratic and higher-genus."""
        result = verify_nonrenormalization_unification()
        extensions = result["mk_extends_to"]
        assert any("Non-quadratic" in e for e in extensions)
        assert any("Higher-genus" in e for e in extensions)

    def test_dnp_is_strict(self):
        """DNP pure gauge is strict (m_k = 0 for k >= 3)."""
        dnp = DimofteNiuPyYangian("sl2", level=1)
        assert dnp.is_strict()
        assert dnp.nonrenormalization_holds()


# ============================================================
#  Part 5: Kappa consistency across frameworks
# ============================================================


class TestKappaConsistency:
    """Test that kappa values agree across all three frameworks."""

    def test_sl2_kappa_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        an = AbedinNiuYangian("sl2", level=1)
        dnp = DimofteNiuPyYangian("sl2", level=1)
        mk = ModularYangianMK("sl2", level=1)
        expected = Rational(9, 4)
        assert an.kappa() == expected
        assert dnp.kappa() == expected
        assert mk.kappa() == expected

    def test_sl3_kappa_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        for cls in [AbedinNiuYangian, DimofteNiuPyYangian, ModularYangianMK]:
            obj = cls("sl3", level=1)
            assert obj.kappa() == Rational(16, 3)

    def test_sl2_kappa_k2(self):
        """kappa(sl_2, k=2) = 3*(2+2)/(2*2) = 3."""
        for cls in [AbedinNiuYangian, DimofteNiuPyYangian, ModularYangianMK]:
            obj = cls("sl2", level=2)
            assert obj.kappa() == Rational(3, 1)

    def test_kappa_positivity(self):
        """kappa > 0 for all standard families at positive level."""
        for g in ["sl2", "sl3", "sl4"]:
            for k in [1, 2, 3, 5]:
                mk = ModularYangianMK(g, level=k)
                assert mk.kappa() > 0

    def test_full_summary_kappa_agreement(self):
        """Full summary reports kappa agreement."""
        result = full_unification_summary("sl2", level=1)
        assert result["kappa_all_agree"]


# ============================================================
#  Part 6: Genus-1 modular correction (MK exclusive)
# ============================================================


class TestGenus1ModularCorrection:
    """Test the genus-1 correction r_1(z; tau) = kappa * wp(z; tau)."""

    def test_reconstruction_from_r0_r1(self):
        """R^mod = r_0 + hbar^2 * r_1 to leading order."""
        result = compute_genus1_modular_correction(
            g="sl2", level=1, z=0.3, tau=0.5j, hbar=0.1
        )
        assert result["path1_valid"]
        assert result["path1_reconstruction_error"] < 1e-12

    def test_genus1_average_equals_kappa_over_24(self):
        """F_1 = kappa/24 (genus-1 shadow)."""
        result = compute_genus1_modular_correction(g="sl2", level=1)
        assert result["path3_F1_matches"]
        assert abs(result["path3_F1"] - 9.0 / 4.0 / 24.0) < 1e-12

    def test_mk_exclusive(self):
        """Genus-1 correction exists ONLY in MK, not AN or DNP."""
        result = compute_genus1_modular_correction()
        assert result["correction_is_mk_exclusive"]
        assert not result["an_has_genus1"]
        assert not result["dnp_has_genus1"]

    def test_r1_nonzero(self):
        """r_1 is nonzero for generic z, tau."""
        mk = ModularYangianMK("sl2", level=1)
        r1 = mk.r1_weierstrass(0.3, 0.5j)
        assert abs(r1) > 1e-3  # Definitely nonzero

    def test_r1_proportional_to_kappa(self):
        """r_1 scales linearly with kappa (i.e. with level)."""
        z, tau = 0.25, 0.7j
        mk1 = ModularYangianMK("sl2", level=1)
        mk2 = ModularYangianMK("sl2", level=2)
        r1_k1 = mk1.r1_weierstrass(z, tau)
        r1_k2 = mk2.r1_weierstrass(z, tau)
        ratio = r1_k2 / r1_k1
        expected_ratio = float(mk2.kappa()) / float(mk1.kappa())
        assert abs(ratio - expected_ratio) < 1e-10

    def test_genus1_average_sl3(self):
        """F_1(sl_3, k=1) = kappa/24 = (16/3)/24 = 2/9."""
        mk = ModularYangianMK("sl3", level=1)
        avg = mk.genus1_average()
        assert avg["kappa"] == Rational(16, 3)
        assert avg["F1"] == Rational(16, 3) * Rational(1, 24)
        assert avg["F1"] == Rational(2, 9)


# ============================================================
#  Part 7: Weierstrass p-function properties
# ============================================================


class TestWeierstrassP:
    """Test the Weierstrass p-function implementation."""

    def test_wp_is_real_on_real_axis(self):
        """wp(z; tau) is real-valued for real z and purely imaginary tau."""
        tau = 1j
        for z in [0.1, 0.2, 0.3, 0.4]:
            wp = _weierstrass_p(z, tau, n_terms=50)
            assert abs(wp.imag) < 1e-10, f"wp({z}) has nonzero imag: {wp.imag}"

    def test_wp_degeneration(self):
        """As Im(tau) -> infty, wp approaches the trigonometric limit."""
        z = 0.2
        # At large Im(tau), q = exp(2*pi*i*tau) -> 0
        # wp(z; tau) -> (2*pi)^2 * [-1/12 + 0 + ...] = -(2*pi)^2/12
        # (up to exponentially small corrections)
        tau_values = [2j, 5j, 10j, 20j]
        wp_values = [_weierstrass_p(z, tau) for tau in tau_values]
        # Should converge as Im(tau) increases
        diffs = [abs(wp_values[i + 1] - wp_values[i])
                 for i in range(len(wp_values) - 1)]
        # Differences should decrease (convergence)
        assert diffs[-1] < diffs[0]

    def test_wp_is_even(self):
        """wp(-z) = wp(z) (even function)."""
        tau = 0.5j
        z = 0.15
        wp_pos = _weierstrass_p(z, tau)
        wp_neg = _weierstrass_p(-z, tau)
        assert abs(wp_pos - wp_neg) < 1e-10


# ============================================================
#  Part 8: Koszul dual R-matrix
# ============================================================


class TestKoszulDualRMatrix:
    """Test Koszul dual R-matrix R^{-1}(u)."""

    def test_r_times_rinv_is_identity_sl2(self):
        """R(u) * R^{-1}(u) = I for sl_2."""
        result = verify_koszul_dual_r_matrix_unification(N=2, u=2.5)
        assert result["path1_inverse_exact"]

    def test_r_times_rinv_is_identity_sl3(self):
        """R(u) * R^{-1}(u) = I for sl_3."""
        result = verify_koszul_dual_r_matrix_unification(N=3, u=3.0)
        assert result["path1_inverse_exact"]

    def test_rinv_eigenvalues(self):
        """R^{-1} eigenvalues: u/(u-hbar) on sym, u/(u+hbar) on anti."""
        u, hbar = 3.0, 1.0
        R_inv = yang_r_matrix_inverse(2, u, hbar)
        eigvals = np.sort(np.real(np.linalg.eigvals(R_inv)))
        # For sl_2: 3 sym eigenvalues at u/(u-hbar) = 3/2
        # and 1 anti eigenvalue at u/(u+hbar) = 3/4
        # Sorted: [3/4, 3/2, 3/2, 3/2]
        assert abs(eigvals[0] - u / (u + hbar)) < 1e-10   # anti (smallest)
        assert abs(eigvals[-1] - u / (u - hbar)) < 1e-10  # sym (largest)


# ============================================================
#  Part 9: Full unification summary
# ============================================================


class TestFullUnification:
    """Test the complete unification summary."""

    def test_summary_structure(self):
        """Summary has all required sections."""
        result = full_unification_summary("sl2", level=1)
        assert "genus_0_unification" in result
        assert "yang_baxter" in result
        assert "nonrenormalization" in result
        assert "mk_exclusive" in result

    def test_genus0_all_agree(self):
        """All three frameworks agree at genus 0."""
        result = full_unification_summary("sl2", level=1)
        assert result["genus_0_unification"]["all_agree"]

    def test_mk_exclusive_content(self):
        """MK has exclusive genus-1 and complementarity content."""
        result = full_unification_summary("sl2", level=1)
        exclusive = result["mk_exclusive"]
        assert "wp" in exclusive["genus_1_correction"]
        assert "complementarity" in exclusive["complementarity"].lower() or \
               "Q_g" in exclusive["complementarity"]

    def test_summary_sl3(self):
        """Summary works for sl_3."""
        result = full_unification_summary("sl3", level=1)
        assert result["kappa_all_agree"]
        assert result["kappa_mk"] == Rational(16, 3)


# ============================================================
#  Part 10: Embedding and tensor product infrastructure
# ============================================================


class TestEmbedding:
    """Test the tensor product embedding functions."""

    def test_embed_13_identity(self):
        """Embedding identity into spaces 1,3 gives identity on full space."""
        N = 2
        I2 = np.eye(N * N)
        result = _embed_13(I2, N)
        # embed_13(I) should be identity on N^3 space
        np.testing.assert_allclose(result, np.eye(N ** 3), atol=1e-14)

    def test_embed_consistency(self):
        """R_{12}(u) R_{23}(v) computed via embeddings is consistent."""
        N = 2
        u, v = 3.0, 2.0
        I_N = np.eye(N)
        R_u = yang_r_matrix(N, u)
        R_v = yang_r_matrix(N, v)

        embed_12 = np.kron(R_u, I_N)
        embed_23 = np.kron(I_N, R_v)

        product = embed_12 @ embed_23
        assert product.shape == (N ** 3, N ** 3)
        # Should not be identity (u != v in general)
        assert np.linalg.norm(product - np.eye(N ** 3)) > 0.01
