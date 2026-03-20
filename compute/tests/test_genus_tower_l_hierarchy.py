"""
Tests for genus_tower_l_hierarchy.py — Genus tower of automorphic L-functions.

Tests the hierarchy: genus g shadow -> GSp(2g) L-functions of degree 2g.

  g=0: polynomial (no modular structure)
  g=1: GL(2) L-functions (degree 2)
  g=2: GSp(4) L-functions (degree 4)
  g=3: GSp(6) L-functions (degree 6)
  g:   GSp(2g) L-functions (degree 2g)

The shadow tower Theta_A = sum_g hbar^g Theta_A^{(g)} at genus g constrains
the spectral decomposition on Sp(2g,Z) backslash H_g.

Ground truth:
  concordance.tex, higher_genus_modular_koszul.tex,
  genus_expansion.py, genus2_shell_amplitudes.py,
  rankin_selberg_bridge.py.
"""

import pytest
import numpy as np
from sympy import Rational, Symbol

from compute.lib.genus_tower_l_hierarchy import (
    # Section 0: Kappa
    kappa_lattice, KAPPA_TABLE,
    # Section 1: Genus-1 Rankin-Selberg
    theta3_imaginary_axis, eta_imaginary_axis,
    genus1_rankin_selberg_VZ, genus1_rankin_selberg_VE8,
    genus1_l_function_degree,
    # Section 2: Genus-2 Siegel
    siegel_upper_half_space_dim,
    genus2_theta_Z_diagonal, genus2_theta_Z_general,
    genus2_theta_lattice_diagonal, genus2_nonfactorization_ratio,
    # Section 3: Genus-2 Rankin-Selberg
    genus2_l_function_degree, spinor_l_degree,
    genus2_rankin_selberg_VZ_dimensional,
    genus2_rankin_selberg_VE8_prediction,
    # Section 4: Shadow at genus 2
    lambda_fp, genus2_shadow_kappa_squared, genus2_curvature_class,
    # Section 5: Hierarchy table
    l_function_hierarchy_entry, l_function_hierarchy_table,
    # Section 6: Genus spectral sequence
    genus_spectral_sequence_E1, E1_heisenberg_arity2,
    genus_spectral_sequence_l_content,
    # Section 7: Independent L-function content
    independent_l_factors_VZ, cumulative_l_factor_count,
    # Section 8: Genus-tower closure
    genus_tower_total_l_content, shadow_genus_decomposition,
    # Section 9: Langlands connection
    langlands_group_at_genus, hecke_generators_count,
    # Section 10: Dimension counts
    moduli_space_dim, siegel_space_real_dim,
    hodge_bundle_rank, shadow_data_dimension,
    complete_hierarchy_summary,
    # Section 11-12: Verification
    verify_genus1_RS_VZ, verify_genus1_RS_VE8,
    verify_genus2_theta_diagonal_factorization,
    verify_genus2_nonfactorization, genus2_RS_VZ_degree_check,
    # Section 13: Shadow depth
    SHADOW_DEPTH_TABLE, shadow_depth_class, shadow_depth_l_interaction,
)


# ═══════════════════════════════════════════════════════════════════════════
# 0. Kappa values
# ═══════════════════════════════════════════════════════════════════════════

class TestKappaValues:
    """Verify kappa values for standard families."""

    def test_kappa_lattice_rank1(self):
        assert kappa_lattice(1) == Rational(1)

    def test_kappa_lattice_rank8(self):
        assert kappa_lattice(8) == Rational(8)

    def test_kappa_lattice_rank24(self):
        assert kappa_lattice(24) == Rational(24)

    def test_kappa_table_VZ(self):
        assert KAPPA_TABLE["V_Z"]() == Rational(1)

    def test_kappa_table_VE8(self):
        assert KAPPA_TABLE["V_E8"]() == Rational(8)

    def test_kappa_table_virasoro(self):
        assert KAPPA_TABLE["Virasoro"](c=26) == Rational(13)


# ═══════════════════════════════════════════════════════════════════════════
# 1. Genus-1 Rankin-Selberg
# ═══════════════════════════════════════════════════════════════════════════

class TestGenus1RankinSelberg:
    """Verify genus-1 Rankin-Selberg integrals."""

    def test_theta3_at_y1(self):
        """theta_3(i) is well-known: approximately 1.0864..."""
        val = theta3_imaginary_axis(1.0)
        # theta_3(i) = 1 + 2*sum_{n>=1} exp(-pi*n^2)
        # = 1 + 2*exp(-pi) + 2*exp(-4pi) + ...
        # ~ 1 + 2*0.04322 + ... ~ 1.08644
        assert abs(val - 1.0864) < 0.001

    def test_theta3_positivity(self):
        for y in [0.5, 1.0, 2.0, 5.0]:
            assert theta3_imaginary_axis(y) > 0

    def test_eta_at_y1(self):
        """eta(i) is known: approximately 0.76823..."""
        val = eta_imaginary_axis(1.0)
        # eta(i) ~ 0.76823...
        assert abs(val - 0.7682) < 0.001

    def test_RS_VZ_at_s2(self):
        """epsilon^c_2(V_Z) = 4*zeta(4) = 4*pi^4/90."""
        import mpmath
        val = genus1_rankin_selberg_VZ(2.0)
        expected = float(4 * mpmath.zeta(4))
        assert abs(val - expected) < 1e-10

    def test_RS_VZ_at_s3(self):
        """epsilon^c_3(V_Z) = 4*zeta(6) = 4*pi^6/945."""
        import mpmath
        val = genus1_rankin_selberg_VZ(3.0)
        expected = float(4 * mpmath.zeta(6))
        assert abs(val - expected) < 1e-10

    def test_RS_VE8_at_s5(self):
        """epsilon^c_5(V_{E_8}) = 240 * 4^{-5} * zeta(5) * zeta(2)."""
        import mpmath
        val = genus1_rankin_selberg_VE8(5.0)
        expected = float(240 * mpmath.power(4, -5) * mpmath.zeta(5) * mpmath.zeta(2))
        assert abs(val - expected) < 1e-10

    def test_RS_VE8_at_s8(self):
        """epsilon^c_8(V_{E_8}) = 240 * 4^{-8} * zeta(8) * zeta(5)."""
        import mpmath
        val = genus1_rankin_selberg_VE8(8.0)
        expected = float(240 * mpmath.power(4, -8) * mpmath.zeta(8) * mpmath.zeta(5))
        assert abs(val - expected) < 1e-10

    def test_genus1_l_degree_VZ(self):
        assert genus1_l_function_degree("V_Z") == 1

    def test_genus1_l_degree_VE8(self):
        assert genus1_l_function_degree("V_E8") == 2

    def test_genus1_l_degree_Heisenberg(self):
        assert genus1_l_function_degree("Heisenberg") == 1

    def test_verify_RS_VZ(self):
        results = verify_genus1_RS_VZ()
        for r in results:
            assert r["match"], f"Mismatch at s={r['s']}"

    def test_verify_RS_VE8(self):
        results = verify_genus1_RS_VE8()
        for r in results:
            assert r["match"], f"Mismatch at s={r['s']}"


# ═══════════════════════════════════════════════════════════════════════════
# 2. Genus-2 Siegel theta functions
# ═══════════════════════════════════════════════════════════════════════════

class TestGenus2SiegelTheta:
    """Verify genus-2 Siegel theta function computations."""

    def test_siegel_dim_g1(self):
        assert siegel_upper_half_space_dim(1) == 1

    def test_siegel_dim_g2(self):
        assert siegel_upper_half_space_dim(2) == 3

    def test_siegel_dim_g3(self):
        assert siegel_upper_half_space_dim(3) == 6

    def test_siegel_dim_formula(self):
        for g in range(1, 8):
            assert siegel_upper_half_space_dim(g) == g * (g + 1) // 2

    def test_genus2_theta_diagonal_factorizes(self):
        """At diagonal Omega, genus-2 theta = product of genus-1 thetas."""
        result = verify_genus2_theta_diagonal_factorization(y1=1.0, y2=1.0)
        assert result["match"]

    def test_genus2_theta_diagonal_various_y(self):
        """Diagonal factorization at various y values."""
        for y1, y2 in [(0.5, 0.5), (1.0, 2.0), (2.0, 0.8)]:
            result = verify_genus2_theta_diagonal_factorization(y1=y1, y2=y2)
            assert result["match"], f"Failed at y1={y1}, y2={y2}"

    def test_genus2_theta_nonfactorization(self):
        """At off-diagonal Omega, genus-2 theta does NOT factorize."""
        result = verify_genus2_nonfactorization(y1=1.0, y2=1.0, x12=0.25)
        assert result["nonfactorized"]

    def test_genus2_theta_nonfactorization_various(self):
        """Off-diagonal nonfactorization at various x12 values."""
        for x12 in [0.1, 0.25, 0.4]:
            result = verify_genus2_nonfactorization(y1=1.0, y2=1.0, x12=x12)
            assert result["nonfactorized"], f"Failed at x12={x12}"

    def test_genus2_theta_positivity(self):
        """Genus-2 theta is positive at diagonal points."""
        for y in [0.5, 1.0, 2.0]:
            val = genus2_theta_Z_diagonal(y, y)
            assert val > 0

    def test_genus2_theta_lattice_rank8(self):
        """Rank-8 lattice genus-2 theta at diagonal = theta_3^8 * theta_3^8."""
        y1, y2 = 1.0, 1.0
        val = genus2_theta_lattice_diagonal(8, y1, y2)
        t1 = theta3_imaginary_axis(y1) ** 8
        t2 = theta3_imaginary_axis(y2) ** 8
        assert abs(val - t1 * t2) < 1e-8

    def test_genus2_ratio_is_1_at_diagonal(self):
        """Nonfactorization ratio is exactly 1 at x12=0."""
        ratio = genus2_nonfactorization_ratio(1.0, 1.0, 0.0)
        assert abs(ratio - 1.0) < 1e-10

    def test_genus2_general_reduces_to_diagonal(self):
        """genus2_theta_Z_general with x12=0 equals genus2_theta_Z_diagonal."""
        y1, y2 = 1.5, 0.8
        general = genus2_theta_Z_general(y1, y2, 0.0, nmax=15)
        diagonal = genus2_theta_Z_diagonal(y1, y2, nmax=15)
        assert abs(general - diagonal) < 1e-6


# ═══════════════════════════════════════════════════════════════════════════
# 3. Genus-2 Rankin-Selberg and Spinor L-functions
# ═══════════════════════════════════════════════════════════════════════════

class TestGenus2RankinSelberg:
    """Verify genus-2 L-function structure."""

    def test_genus2_l_degree(self):
        assert genus2_l_function_degree() == 4

    def test_spinor_l_degree_g1(self):
        assert spinor_l_degree(1) == 2

    def test_spinor_l_degree_g2(self):
        assert spinor_l_degree(2) == 4

    def test_spinor_l_degree_g3(self):
        assert spinor_l_degree(3) == 6

    def test_spinor_l_degree_grows_linearly(self):
        for g in range(1, 10):
            assert spinor_l_degree(g) == 2 * g

    def test_genus2_RS_VZ_at_s5(self):
        """zeta(5)*zeta(4)*zeta(3)*zeta(2) is finite at s=5."""
        val = genus2_rankin_selberg_VZ_dimensional(5.0)
        assert np.isfinite(val)
        assert val > 0

    def test_genus2_RS_VZ_degree_check(self):
        """Check that the degree-4 product has correct pole structure."""
        result = genus2_RS_VZ_degree_check(s=5.0)
        assert result["degree"] == 4

    def test_genus2_RS_VE8_prediction_structure(self):
        pred = genus2_rankin_selberg_VE8_prediction()
        assert pred["genus_2_degree"] == 4
        assert len(pred["genus_2_prediction"]) == 4

    def test_genus2_RS_VZ_pole_behavior(self):
        """zeta(s)*zeta(s-1)*zeta(s-2)*zeta(s-3) diverges near s=4 (from zeta(s-3)->zeta(1))."""
        import mpmath
        # Near s=4: zeta(s-3) ~ zeta(1+epsilon) diverges
        # While zeta(4), zeta(3), zeta(2) are all finite and positive
        with mpmath.workdps(30):
            eps = 0.001
            val_near = abs(float(
                mpmath.zeta(4 + eps) * mpmath.zeta(3 + eps)
                * mpmath.zeta(2 + eps) * mpmath.zeta(1 + eps)
            ))
            val_far = abs(float(
                mpmath.zeta(6) * mpmath.zeta(5)
                * mpmath.zeta(4) * mpmath.zeta(3)
            ))
        # Near the pole at s=4, the product is much larger
        assert val_near > 100 * val_far


# ═══════════════════════════════════════════════════════════════════════════
# 4. Shadow at genus 2
# ═══════════════════════════════════════════════════════════════════════════

class TestGenus2Shadow:
    """Verify genus-2 shadow computations."""

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        val = lambda_fp(3)
        expected = Rational(2**5 - 1, 2**5) * abs(Rational(1, 42)) / Rational(720)
        # (2^5-1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/(32*42*720)
        # = 31/967680
        assert val == Rational(31, 967680)

    def test_kappa_squared_heisenberg(self):
        """For Heisenberg (kappa=1): kappa^2 = 1."""
        result = genus2_shadow_kappa_squared(Rational(1))
        assert result["kappa_squared"] == 1
        assert result["F_2"] == Rational(7, 5760)

    def test_kappa_squared_E8(self):
        """For V_{E_8} (kappa=8): kappa^2 = 64."""
        result = genus2_shadow_kappa_squared(Rational(8))
        assert result["kappa_squared"] == 64
        assert result["F_2"] == Rational(8) * Rational(7, 5760)

    def test_genus2_curvature_heisenberg(self):
        result = genus2_curvature_class(Rational(1))
        assert result["genus_2_curvature"] == 1
        assert result["iterated_genus1"] == 1

    def test_genus2_curvature_sl2_k1(self):
        """sl_2 at k=1: kappa = 3*3/4 = 9/4."""
        kappa = Rational(3) * (Rational(1) + 2) / 4
        assert kappa == Rational(9, 4)
        result = genus2_curvature_class(kappa)
        assert result["iterated_genus1"] == kappa ** 2


# ═══════════════════════════════════════════════════════════════════════════
# 5. L-function hierarchy table
# ═══════════════════════════════════════════════════════════════════════════

class TestHierarchyTable:
    """Verify the L-function hierarchy table."""

    def test_genus0_entry(self):
        e = l_function_hierarchy_entry(0)
        assert e["l_function_degree"] == 0
        assert e["automorphic_group"] == "trivial"

    def test_genus1_entry(self):
        e = l_function_hierarchy_entry(1)
        assert e["l_function_degree"] == 2
        assert e["moduli_dim"] == 1
        assert "GSp(2)" in e["automorphic_group"]

    def test_genus2_entry(self):
        e = l_function_hierarchy_entry(2)
        assert e["l_function_degree"] == 4
        assert e["moduli_dim"] == 3
        assert "GSp(4)" in e["automorphic_group"]

    def test_genus3_entry(self):
        e = l_function_hierarchy_entry(3)
        assert e["l_function_degree"] == 6
        assert e["moduli_dim"] == 6

    def test_hierarchy_table_length(self):
        table = l_function_hierarchy_table(g_max=5)
        assert len(table) == 6

    def test_hierarchy_table_degrees_grow(self):
        table = l_function_hierarchy_table(g_max=5)
        for i in range(1, len(table)):
            assert table[i]["l_function_degree"] > table[i-1]["l_function_degree"]

    def test_hierarchy_degree_is_2g(self):
        for g in range(1, 8):
            e = l_function_hierarchy_entry(g)
            assert e["l_function_degree"] == 2 * g


# ═══════════════════════════════════════════════════════════════════════════
# 6. Genus spectral sequence E_1 page
# ═══════════════════════════════════════════════════════════════════════════

class TestGenusSpectralSequence:
    """Verify the genus spectral sequence E_1 page."""

    def test_E1_heisenberg_tree_level(self):
        """E_1^{0,2} = kappa = 1 for Heisenberg."""
        entries = E1_heisenberg_arity2()
        assert entries[(0, 2)] == Rational(1)

    def test_E1_heisenberg_genus1(self):
        """E_1^{1,2} = lambda_1^FP = 1/24 for Heisenberg (kappa=1)."""
        entries = E1_heisenberg_arity2()
        assert entries[(1, 2)] == Rational(1, 24)

    def test_E1_heisenberg_genus2(self):
        """E_1^{2,2} = lambda_2^FP = 7/5760 for Heisenberg (kappa=1)."""
        entries = E1_heisenberg_arity2()
        assert entries[(2, 2)] == Rational(7, 5760)

    def test_E1_entries_decrease(self):
        """Higher genus entries are smaller (in absolute value)."""
        entries = E1_heisenberg_arity2(g_max=5)
        vals = [entries[(g, 2)] for g in range(1, 6)]
        for i in range(len(vals) - 1):
            assert abs(vals[i]) > abs(vals[i+1])

    def test_l_content_genus0(self):
        content = genus_spectral_sequence_l_content(0)
        assert "polynomial" in content.lower()

    def test_l_content_genus1(self):
        content = genus_spectral_sequence_l_content(1)
        assert "GL(2)" in content

    def test_l_content_genus2(self):
        content = genus_spectral_sequence_l_content(2)
        assert "GSp(4)" in content


# ═══════════════════════════════════════════════════════════════════════════
# 7. Independent L-function content
# ═══════════════════════════════════════════════════════════════════════════

class TestIndependentLContent:
    """Verify independent L-function content by genus."""

    def test_VZ_genus0_no_factors(self):
        result = independent_l_factors_VZ(0)
        assert result["total_zeta_factors"] == 0

    def test_VZ_genus1_one_factor(self):
        result = independent_l_factors_VZ(1)
        assert result["total_zeta_factors"] == 1
        assert "zeta(2s)" in result["factors"]

    def test_VZ_genus2_four_factors(self):
        result = independent_l_factors_VZ(2)
        assert result["total_zeta_factors"] == 4

    def test_VZ_genus3_six_factors(self):
        result = independent_l_factors_VZ(3)
        assert result["total_zeta_factors"] == 6

    def test_VZ_new_factors_at_genus_g(self):
        """Each genus >= 2 adds exactly 2 new factors."""
        for g in range(2, 7):
            result = independent_l_factors_VZ(g)
            assert result["new_at_this_genus"] == 2

    def test_cumulative_count_values(self):
        counts = cumulative_l_factor_count(g_max=5)
        assert counts[0] == 0
        assert counts[1] == 1
        # For g >= 2: 2g - 1
        for g in range(2, 6):
            assert counts[g] == 2 * g - 1


# ═══════════════════════════════════════════════════════════════════════════
# 8. Genus-tower closure
# ═══════════════════════════════════════════════════════════════════════════

class TestGenusTowerClosure:
    """Verify genus-tower closure properties."""

    def test_total_l_content_g1(self):
        result = genus_tower_total_l_content(1)
        assert result["number_of_l_functions"] == 2  # g=0 and g=1
        assert result["total_degree"] == 2  # 0 + 2

    def test_total_l_content_g2(self):
        result = genus_tower_total_l_content(2)
        assert result["number_of_l_functions"] == 3
        assert result["total_degree"] == 6  # 0 + 2 + 4

    def test_total_l_content_g5(self):
        result = genus_tower_total_l_content(5)
        assert result["number_of_l_functions"] == 6
        assert result["total_degree"] == 30  # 5*6

    def test_total_degree_formula(self):
        """Total degree = g_max * (g_max + 1)."""
        for g in range(1, 8):
            result = genus_tower_total_l_content(g)
            assert result["total_degree"] == g * (g + 1)

    def test_shadow_decomposition_heisenberg(self):
        """Shadow decomposition for Heisenberg (kappa=1)."""
        entries = shadow_genus_decomposition(Rational(1), g_max=3)
        assert entries[0]["F_g"] == 0
        assert entries[1]["F_g"] == Rational(1, 24)
        assert entries[2]["F_g"] == Rational(7, 5760)

    def test_shadow_cumulative_positive(self):
        """Cumulative free energy is positive and increasing."""
        entries = shadow_genus_decomposition(Rational(1), g_max=5)
        for i in range(2, len(entries)):
            assert entries[i]["cumulative"] > entries[i-1]["cumulative"]


# ═══════════════════════════════════════════════════════════════════════════
# 9. Langlands connection
# ═══════════════════════════════════════════════════════════════════════════

class TestLanglandsConnection:
    """Verify Langlands data at each genus."""

    def test_langlands_genus0(self):
        result = langlands_group_at_genus(0)
        assert result["automorphic_group"] == "trivial"
        assert result["satake_parameters"] == 0

    def test_langlands_genus1(self):
        result = langlands_group_at_genus(1)
        assert "GSp(2)" in result["automorphic_group"]
        assert result["satake_parameters"] == 1

    def test_langlands_genus2(self):
        result = langlands_group_at_genus(2)
        assert "GSp(4)" in result["automorphic_group"]
        assert "GSpin(5)" in result["langlands_dual"]
        assert result["satake_parameters"] == 2

    def test_langlands_satake_grows(self):
        for g in range(1, 8):
            result = langlands_group_at_genus(g)
            assert result["satake_parameters"] == g

    def test_hecke_generators_genus0(self):
        assert hecke_generators_count(0) == 0

    def test_hecke_generators_genus1(self):
        assert hecke_generators_count(1) == 2

    def test_hecke_generators_genus2(self):
        assert hecke_generators_count(2) == 3

    def test_hecke_generators_formula(self):
        for g in range(1, 8):
            assert hecke_generators_count(g) == g + 1


# ═══════════════════════════════════════════════════════════════════════════
# 10. Dimension counts
# ═══════════════════════════════════════════════════════════════════════════

class TestDimensionCounts:
    """Verify dimension formulas for moduli spaces and Siegel spaces."""

    def test_moduli_dim_g0(self):
        assert moduli_space_dim(0) == 0

    def test_moduli_dim_g1(self):
        assert moduli_space_dim(1) == 1

    def test_moduli_dim_g2(self):
        assert moduli_space_dim(2) == 3

    def test_moduli_dim_g3(self):
        assert moduli_space_dim(3) == 6

    def test_moduli_dim_g4(self):
        assert moduli_space_dim(4) == 9

    def test_moduli_dim_g5(self):
        assert moduli_space_dim(5) == 12

    def test_moduli_dim_3g_minus_3(self):
        """For g >= 2: dim M_g = 3g - 3."""
        for g in range(2, 10):
            assert moduli_space_dim(g) == 3 * g - 3

    def test_siegel_real_dim(self):
        for g in range(1, 8):
            assert siegel_space_real_dim(g) == g * (g + 1)

    def test_hodge_rank(self):
        for g in range(1, 8):
            assert hodge_bundle_rank(g) == g

    def test_shadow_data_dim_arity2(self):
        """At arity 2: 0 at g=0, 1 at g>=1."""
        assert shadow_data_dimension(0, arity=2) == 0
        for g in range(1, 5):
            assert shadow_data_dimension(g, arity=2) == 1

    def test_complete_summary_length(self):
        summary = complete_hierarchy_summary(g_max=4)
        assert len(summary) == 5  # g=0,1,2,3,4


# ═══════════════════════════════════════════════════════════════════════════
# 11. Shadow depth and L-function interaction
# ═══════════════════════════════════════════════════════════════════════════

class TestShadowDepthLInteraction:
    """Verify shadow depth classification and L-function interaction."""

    def test_shadow_depth_heisenberg(self):
        assert SHADOW_DEPTH_TABLE["Heisenberg"] == 2

    def test_shadow_depth_VZ(self):
        assert SHADOW_DEPTH_TABLE["V_Z"] == 2

    def test_shadow_depth_virasoro(self):
        assert SHADOW_DEPTH_TABLE["Virasoro"] == float('inf')

    def test_shadow_class_G(self):
        assert shadow_depth_class("Heisenberg") == "G"
        assert shadow_depth_class("V_Z") == "G"
        assert shadow_depth_class("V_E8") == "G"

    def test_shadow_class_L(self):
        assert shadow_depth_class("affine_sl2") == "L"

    def test_shadow_class_C(self):
        assert shadow_depth_class("betagamma") == "C"

    def test_shadow_class_M(self):
        assert shadow_depth_class("Virasoro") == "M"
        assert shadow_depth_class("W3") == "M"

    def test_shadow_l_interaction_gaussian(self):
        """Gaussian class: scalar-saturated at all genera."""
        for g in range(1, 5):
            result = shadow_depth_l_interaction("V_Z", g)
            assert result["scalar_saturated"]
            assert result["l_degree"] == 2 * g

    def test_shadow_l_interaction_mixed(self):
        """Mixed class: NOT scalar-saturated."""
        result = shadow_depth_l_interaction("Virasoro", 2)
        assert not result["scalar_saturated"]
        assert result["l_degree"] == 4


# ═══════════════════════════════════════════════════════════════════════════
# 12. Cross-consistency checks
# ═══════════════════════════════════════════════════════════════════════════

class TestCrossConsistency:
    """Cross-consistency between different parts of the hierarchy."""

    def test_hierarchy_degree_equals_spinor_degree(self):
        """The hierarchy table degree matches spinor_l_degree."""
        for g in range(1, 7):
            entry = l_function_hierarchy_entry(g)
            assert entry["l_function_degree"] == spinor_l_degree(g)

    def test_siegel_dim_in_hierarchy(self):
        """Siegel dimension in hierarchy table matches standalone function."""
        for g in range(7):
            entry = l_function_hierarchy_entry(g)
            assert entry["siegel_dim"] == siegel_upper_half_space_dim(g)

    def test_genus_decomposition_sums_correctly(self):
        """Cumulative F equals sum of individual F_g."""
        kappa = Rational(3)
        entries = shadow_genus_decomposition(kappa, g_max=5)
        running_sum = Rational(0)
        for e in entries:
            running_sum += e["F_g"]
            assert running_sum == e["cumulative"]

    def test_lambda_fp_alternating_sign(self):
        """lambda_g^FP has alternating signs in Bernoulli but is always positive."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP decreases with g (for g >= 1)."""
        for g in range(1, 7):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_genus_tower_degrees_sum(self):
        """sum_{h=0}^g 2h = g(g+1)."""
        for g in range(1, 8):
            result = genus_tower_total_l_content(g)
            expected_sum = sum(2 * h for h in range(g + 1))
            assert result["total_degree"] == expected_sum
            assert result["total_degree"] == g * (g + 1)

    def test_E1_heisenberg_matches_shadow_decomposition(self):
        """E_1 entries for Heisenberg match shadow decomposition at arity 2."""
        e1 = E1_heisenberg_arity2(g_max=4)
        decomp = shadow_genus_decomposition(Rational(1), g_max=4)
        for g in range(1, 5):
            assert e1[(g, 2)] == decomp[g]["F_g"]
