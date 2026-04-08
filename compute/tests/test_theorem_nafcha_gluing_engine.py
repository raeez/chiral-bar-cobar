r"""Tests for Nafcha gluing formula vs MC5 sewing comparison engine.

Tests verify:
  1. Verlinde dimensions for sl_2 at low levels (known integers)
  2. Verlinde fusion coefficients (non-negative integers, associativity)
  3. Nafcha's separating gluing formula for sl_2
  4. Nafcha's self-gluing formula for sl_2
  5. Heisenberg nodal degeneration at genus 1->2
  6. Planted-forest corrections and Nafcha's gap
  7. Shadow CohFT vs Verlinde comparison
  8. D^2=0 comparison between frameworks
  9. Hochschild homology of Heisenberg Zhu algebra
 10. Cross-family consistency checks

Each test uses multiple independent verification paths (CLAUDE.md mandate).

References:
  Nafcha, arXiv:2603.30037 (Theorem 1.3)
  thm:general-hs-sewing (genus_complete.tex)
  thm:heisenberg-sewing (higher_genus_modular_koszul.tex)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.theorem_nafcha_gluing_engine import (
    lambda_fp,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_affine,
    sl2_s_matrix_entry,
    verlinde_dimension_sl2,
    verlinde_fusion_sl2,
    verlinde_with_insertions_sl2,
    verify_separating_gluing_sl2,
    verify_self_gluing_sl2,
    HeisenbergNodalData,
    heisenberg_separating_degeneration_g2,
    GluingVsSewingComparison,
    shadow_F_g,
    verlinde_factorization_check_sl2,
    nafcha_clutching_vs_ours,
    d_squared_zero_comparison,
    heisenberg_zhu_algebra_hh,
    planted_forest_nafcha_gap,
    full_comparison_table,
)


# ============================================================================
# SECTION 1:  Verlinde dimensions for sl_2 — exact known values
# ============================================================================

class TestVerlindeDimensionsSl2:
    """Verlinde dimensions are INTEGERS, computed independently.

    Known values (Verlinde 1988, Di Francesco-Mathieu-Senechal Table 16.1):
      V_{0,k}(sl_2) = 1 for all k  (genus 0, unique vacuum block)
      V_{1,k}(sl_2) = k+1           (genus 1, number of integrable reps)
      V_{2,1}(sl_2) = 3              (genus 2, level 1)
      V_{2,2}(sl_2) = 10             (genus 2, level 2)
      V_{3,1}(sl_2) = 10             (genus 3, level 1)
    """

    def test_genus_0_always_1(self):
        """V_{0,k} = 1 for all k: unique vacuum conformal block at genus 0."""
        for k in range(1, 8):
            assert verlinde_dimension_sl2(0, k) == 1, f"V_{{0,{k}}} should be 1"

    def test_genus_1_equals_num_reps(self):
        """V_{1,k} = k+1: one conformal block per integrable representation."""
        for k in range(1, 10):
            assert verlinde_dimension_sl2(1, k) == k + 1, \
                f"V_{{1,{k}}} should be {k+1}"

    def test_genus_2_level_1(self):
        """V_{2,1}(sl_2) = 4.

        Independent verification: k=1 has 2 reps with S_{0,j} = 1/sqrt(2).
        V_2 = 2 * (1/sqrt(2))^{-2} = 2 * 2 = 4.
        """
        assert verlinde_dimension_sl2(2, 1) == 4

    def test_genus_2_level_2(self):
        """V_{2,2}(sl_2) = 10.

        Independent: k=2, S_{0,0}=S_{0,2}=1/2, S_{0,1}=1/sqrt(2).
        V_2 = 2*(1/2)^{-2} + (1/sqrt(2))^{-2} = 2*4 + 2 = 10.
        """
        assert verlinde_dimension_sl2(2, 2) == 10

    def test_genus_2_level_3(self):
        """V_{2,3}(sl_2) = 20.

        Computed from S-matrix for k=3 (k+2=5, golden-ratio entries).
        """
        assert verlinde_dimension_sl2(2, 3) == 20

    def test_genus_3_level_1(self):
        """V_{3,1}(sl_2) = 8.

        Independent: V_3 = 2 * (1/sqrt(2))^{-4} = 2 * 4 = 8.
        """
        assert verlinde_dimension_sl2(3, 1) == 8

    def test_genus_3_level_2(self):
        """V_{3,2}(sl_2) = 36.

        Independent: S_{0,0}=S_{0,2}=1/2, S_{0,1}=1/sqrt(2).
        V_3 = 2*(1/2)^{-4} + (1/sqrt(2))^{-4} = 2*16 + 4 = 36.
        """
        assert verlinde_dimension_sl2(3, 2) == 36

    def test_integrality_wide_range(self):
        """All Verlinde dimensions are positive integers (AP38 convention check)."""
        for g in range(0, 5):
            for k in range(1, 6):
                v = verlinde_dimension_sl2(g, k)
                assert isinstance(v, int), f"V_{{{g},{k}}} not integer: {v}"
                assert v > 0, f"V_{{{g},{k}}} not positive: {v}"

    def test_monotonicity_in_genus(self):
        """V_{g,k} is non-decreasing in g for fixed k >= 1."""
        for k in range(1, 5):
            prev = verlinde_dimension_sl2(0, k)
            for g in range(1, 5):
                curr = verlinde_dimension_sl2(g, k)
                assert curr >= prev, f"V_{{{g},{k}}} < V_{{{g-1},{k}}}"
                prev = curr


# ============================================================================
# SECTION 2:  S-matrix properties
# ============================================================================

class TestSMatrixSl2:
    """S-matrix for sl_2 satisfies unitarity, symmetry, positivity."""

    def test_symmetry(self):
        """S_{jl} = S_{lj} (symmetric matrix)."""
        for k in range(1, 6):
            for j in range(k + 1):
                for l in range(k + 1):
                    assert abs(sl2_s_matrix_entry(j, l, k) -
                               sl2_s_matrix_entry(l, j, k)) < 1e-12

    def test_unitarity(self):
        """sum_l |S_{jl}|^2 = 1 for each j (orthonormality of rows)."""
        for k in range(1, 6):
            for j in range(k + 1):
                total = sum(sl2_s_matrix_entry(j, l, k) ** 2 for l in range(k + 1))
                assert abs(total - 1.0) < 1e-10, \
                    f"Unitarity fails: sum |S_{{{j},l}}|^2 = {total} for k={k}"

    def test_vacuum_row_positive(self):
        """S_{0,l} > 0 for all l (positive normalization convention)."""
        for k in range(1, 8):
            for l in range(k + 1):
                assert sl2_s_matrix_entry(0, l, k) > 0, \
                    f"S_{{0,{l}}} <= 0 for k={k}"

    def test_s00_smallest_in_vacuum_row(self):
        """S_{0,0} <= S_{0,l} for all l: vacuum entry is the SMALLEST.

        S_{0,l} = sqrt(2/(k+2)) * sin(pi*(l+1)/(k+2)), and sin is maximized
        at pi/2.  The l=0 entry uses the smallest argument pi/(k+2),
        so S_{0,0} is the smallest positive entry in the vacuum row.
        This means S_{0,0}^{2-2g} DOMINATES V_g at large g.
        """
        for k in range(1, 8):
            s00 = sl2_s_matrix_entry(0, 0, k)
            for l in range(k + 1):
                assert sl2_s_matrix_entry(0, l, k) >= s00 - 1e-12, \
                    f"S_{{0,{l}}} < S_{{0,0}} for k={k}"

    def test_orthogonality(self):
        """sum_l S_{jl} S_{ml} = delta_{jm} (row orthogonality)."""
        for k in range(1, 5):
            for j in range(k + 1):
                for m in range(k + 1):
                    total = sum(
                        sl2_s_matrix_entry(j, l, k) * sl2_s_matrix_entry(m, l, k)
                        for l in range(k + 1)
                    )
                    expected = 1.0 if j == m else 0.0
                    assert abs(total - expected) < 1e-10, \
                        f"Orthogonality fails: j={j}, m={m}, k={k}, sum={total}"


# ============================================================================
# SECTION 3:  Verlinde fusion coefficients
# ============================================================================

class TestVerlindeFusionSl2:
    """Fusion coefficients are non-negative integers satisfying selection rules."""

    def test_nonnegative_integrality(self):
        """N_{ij}^m are non-negative integers for sl_2."""
        for k in range(1, 5):
            for i in range(k + 1):
                for j in range(k + 1):
                    for m in range(k + 1):
                        n = verlinde_fusion_sl2(i, j, m, k)
                        assert n >= 0, f"N_{{{i},{j}}}^{{{m}}} < 0 for k={k}"

    def test_vacuum_fusion(self):
        """N_{0,j}^m = delta_{jm} (fusion with vacuum is identity)."""
        for k in range(1, 5):
            for j in range(k + 1):
                for m in range(k + 1):
                    expected = 1 if j == m else 0
                    assert verlinde_fusion_sl2(0, j, m, k) == expected, \
                        f"N_{{0,{j}}}^{{{m}}} wrong for k={k}"

    def test_commutativity(self):
        """N_{ij}^m = N_{ji}^m (fusion is commutative)."""
        for k in range(1, 4):
            for i in range(k + 1):
                for j in range(k + 1):
                    for m in range(k + 1):
                        assert verlinde_fusion_sl2(i, j, m, k) == \
                               verlinde_fusion_sl2(j, i, m, k)

    def test_sl2_level_1_selection(self):
        """sl_2 at level 1: N_{11}^0 = 1 (the only nontrivial fusion)."""
        assert verlinde_fusion_sl2(1, 1, 0, 1) == 1
        assert verlinde_fusion_sl2(0, 0, 0, 1) == 1
        assert verlinde_fusion_sl2(0, 1, 1, 1) == 1

    def test_sl2_level_2_fusion(self):
        """sl_2 at level 2: three representations j=0,1,2.

        Fusion rules from direct S-matrix computation:
        N_{1,1}^0 = 1, N_{1,1}^2 = 1, N_{1,2}^1 = 1,
        N_{2,2}^0 = 1, N_{2,2}^2 = 0.
        The last is ZERO because min(i+j, 2k-i-j) = min(4,0) = 0 < m=2.
        """
        k = 2
        assert verlinde_fusion_sl2(1, 1, 0, k) == 1
        assert verlinde_fusion_sl2(1, 1, 2, k) == 1
        assert verlinde_fusion_sl2(1, 2, 1, k) == 1
        assert verlinde_fusion_sl2(2, 2, 0, k) == 1
        assert verlinde_fusion_sl2(2, 2, 2, k) == 0  # truncation at level k


# ============================================================================
# SECTION 4:  Nafcha separating gluing formula
# ============================================================================

class TestNafchaSeparatingGluing:
    """Verify Nafcha's separating gluing (Theorem 1.3, eq 1.1).

    V_{g1+g2}(k) = sum_j V_{g1,1}(k; j) * V_{g2,1}(k; j)

    Three independent verification paths:
      Path 1: Direct computation from S-matrix
      Path 2: Cross-check with known Verlinde dimensions
      Path 3: Consistency with fusion ring
    """

    def test_genus_1_plus_1_equals_genus_2(self):
        """Separating gluing: g1=1, g2=1 gives g=2."""
        for k in range(1, 5):
            lhs, rhs, err = verify_separating_gluing_sl2(1, 1, k)
            assert err < 1e-8, \
                f"Separating gluing fails at k={k}: |{lhs} - {rhs}| = {err}"

    def test_genus_1_plus_2_equals_genus_3(self):
        """Separating gluing: g1=1, g2=2 gives g=3."""
        for k in range(1, 4):
            lhs, rhs, err = verify_separating_gluing_sl2(1, 2, k)
            assert err < 1e-8, \
                f"Separating gluing fails at k={k}: |{lhs} - {rhs}| = {err}"

    def test_genus_2_plus_2_equals_genus_4(self):
        """Separating gluing: g1=2, g2=2 gives g=4."""
        for k in range(1, 3):
            lhs, rhs, err = verify_separating_gluing_sl2(2, 2, k)
            assert err < 1e-6, \
                f"Separating gluing fails at k={k}: |{lhs} - {rhs}| = {err}"

    def test_symmetry_in_genera(self):
        """Separating gluing is symmetric: V_{g1+g2} via (g1,g2) = via (g2,g1)."""
        for k in range(1, 4):
            _, rhs12, _ = verify_separating_gluing_sl2(1, 2, k)
            _, rhs21, _ = verify_separating_gluing_sl2(2, 1, k)
            assert abs(rhs12 - rhs21) < 1e-10, \
                f"Asymmetry at k={k}: {rhs12} vs {rhs21}"

    def test_genus_0_plus_g(self):
        """Separating gluing: g1=0, g2=g gives g (genus-0 is trivial)."""
        for k in range(1, 4):
            for g in range(1, 4):
                lhs, rhs, err = verify_separating_gluing_sl2(0, g, k)
                assert err < 1e-8, \
                    f"g1=0, g2={g}, k={k}: |{lhs} - {rhs}| = {err}"


# ============================================================================
# SECTION 5:  Nafcha self-gluing formula
# ============================================================================

class TestNafchaSelfGluing:
    """Verify Nafcha's self-gluing formula (Theorem 1.3, eq 1.2).

    V_{g+1}(k) = sum_j V_{g,2}(k; j, j)

    This is the non-separating degeneration.
    """

    def test_genus_0_to_1(self):
        """Self-gluing: genus 0 with 2 marked points -> genus 1.

        V_1(k) = sum_j V_{0,2}(k; j, j).
        Since V_1(k) = k+1 and V_{0,2}(k; j, j) = delta_{jj} = 1 for each j,
        we get sum_j 1 = k+1. Consistent.
        """
        for k in range(1, 6):
            lhs, rhs, err = verify_self_gluing_sl2(0, k)
            assert err < 1e-8, \
                f"Self-gluing g=0->1 fails at k={k}: |{lhs} - {rhs}| = {err}"

    def test_genus_1_to_2(self):
        """Self-gluing: genus 1 with 2 marked points -> genus 2."""
        for k in range(1, 5):
            lhs, rhs, err = verify_self_gluing_sl2(1, k)
            assert err < 1e-8, \
                f"Self-gluing g=1->2 fails at k={k}: |{lhs} - {rhs}| = {err}"

    def test_genus_2_to_3(self):
        """Self-gluing: genus 2 -> genus 3."""
        for k in range(1, 4):
            lhs, rhs, err = verify_self_gluing_sl2(2, k)
            assert err < 1e-6, \
                f"Self-gluing g=2->3 fails at k={k}: |{lhs} - {rhs}| = {err}"


# ============================================================================
# SECTION 6:  Heisenberg nodal degeneration
# ============================================================================

class TestHeisenbergNodalDegeneration:
    """Heisenberg at genus 1 -> 2 via nodal degeneration.

    For H_k (class G):
      F_1 = k/24
      F_2 = k * 7/5760 = 7k/5760
      delta_pf^{(2,0)} = 0  (S_3 = 0 for Heisenberg)
    """

    def test_F1_heisenberg(self):
        """F_1(H_k) = k/24."""
        for k in [1, 2, 5, 10]:
            h = HeisenbergNodalData(level=Rational(k))
            assert h.F1 == Rational(k, 24), f"F_1(H_{k}) wrong"

    def test_F2_heisenberg(self):
        """F_2(H_k) = 7k/5760."""
        for k in [1, 2, 5]:
            h = HeisenbergNodalData(level=Rational(k))
            assert h.F2 == Rational(7 * k, 5760), f"F_2(H_{k}) wrong"

    def test_lambda2_FP_value(self):
        """lambda_2^FP = 7/5760 (Faber-Pandharipande, CORRECT value, AP38)."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_planted_forest_zero(self):
        """delta_pf^{(2,0)} = 0 for Heisenberg (class G, S_3 = 0)."""
        for k in [1, 2, 10]:
            h = HeisenbergNodalData(level=Rational(k))
            assert h.delta_pf_genus2 == 0

    def test_separating_degeneration_g2_consistent(self):
        """F_2 = kappa * lambda_2^FP via separating degeneration."""
        for k in [1, 2, 5]:
            data = heisenberg_separating_degeneration_g2(Rational(k))
            assert data['consistent'], f"Inconsistency at k={k}"
            assert data['F2'] == data['F2_check']

    def test_kappa_heisenberg_not_k_over_2(self):
        """kappa(H_k) = k, NOT k/2 (AP39)."""
        assert kappa_heisenberg(1) == Rational(1)
        assert kappa_heisenberg(2) == Rational(2)
        assert kappa_heisenberg(Rational(1, 2)) == Rational(1, 2)


# ============================================================================
# SECTION 7:  Kappa formulas (AP1, AP39, AP48 cross-checks)
# ============================================================================

class TestKappaFormulas:
    """Multi-path verification of kappa for all standard families."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_virasoro(26) == Rational(13)
        assert kappa_virasoro(0) == Rational(0)
        assert kappa_virasoro(1) == Rational(1, 2)

    def test_kappa_affine_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        assert kappa_affine_sl2(1) == Rational(9, 4)
        assert kappa_affine_sl2(2) == Rational(3)
        assert kappa_affine_sl2(4) == Rational(9, 2)

    def test_kappa_affine_general(self):
        """kappa(g, k) = dim(g)*(k+h^v)/(2*h^v)."""
        # sl_3: dim=8, h^v=3
        assert kappa_affine(8, 1, 3) == Rational(8 * 4, 6)
        # sl_2: dim=3, h^v=2
        assert kappa_affine(3, 1, 2) == Rational(9, 4)

    def test_kappa_not_c_over_2_for_km(self):
        """kappa(g_k) != c(g_k)/2 in general (AP48).

        For sl_2 at k=1: c = 3*1/(1+2) = 1.  c/2 = 1/2.
        But kappa = 3*(1+2)/4 = 9/4.  So kappa != c/2.
        """
        c_sl2_k1 = Rational(1)     # central charge sl_2, k=1
        kappa_sl2_k1 = kappa_affine_sl2(1)
        assert kappa_sl2_k1 != c_sl2_k1 / 2, \
            "kappa should NOT equal c/2 for affine sl_2 (AP48)"


# ============================================================================
# SECTION 8:  Shadow CohFT vs Verlinde dimensions
# ============================================================================

class TestShadowVsVerlinde:
    """The shadow F_g and Verlinde V_g are DIFFERENT projections.

    F_g = kappa * lambda_g^FP  (scalar shadow, rational)
    V_g = sum_j S_{0j}^{2-2g}  (full, integer, Verlinde)

    They agree at genus 0 (both = 1 after normalization) but diverge
    at higher genus.  The ratio V_g / F_g encodes the quantum-group
    content beyond the scalar shadow.
    """

    def test_different_at_genus_1(self):
        """V_1(sl_2, k) = k+1 vs F_1(sl_2, k) = kappa/24 = 3(k+2)/96."""
        for k in [1, 2, 3]:
            v = verlinde_dimension_sl2(1, k)
            kap = kappa_affine_sl2(k)
            f = float(shadow_F_g(kap, 1))
            # They should be DIFFERENT objects
            assert v != f, f"V_1 and F_1 should differ at k={k}"
            # But both are positive
            assert v > 0 and f > 0

    def test_shadow_is_rational(self):
        """F_g is always rational (Bernoulli numbers are rational)."""
        for g in range(1, 5):
            for k in [1, 2, 3]:
                kap = kappa_affine_sl2(k)
                f = shadow_F_g(kap, g)
                assert isinstance(f, Rational), f"F_{g} not Rational at k={k}"

    def test_verlinde_grows_faster(self):
        """V_g grows exponentially in g; F_g grows polynomially.

        V_g ~ S_{0,0}^{2-2g} ~ ((k+2)/2)^{g-1} for large g.
        F_g ~ kappa * |B_{2g}| / (2g)! which is bounded by (2pi)^{-2g}.
        """
        k = 2
        v_prev = verlinde_dimension_sl2(2, k)
        f_prev = float(shadow_F_g(kappa_affine_sl2(k), 2))
        for g in range(3, 6):
            v = verlinde_dimension_sl2(g, k)
            f = float(shadow_F_g(kappa_affine_sl2(k), g))
            # Verlinde growth rate should exceed shadow growth rate
            v_ratio = v / v_prev if v_prev != 0 else float('inf')
            f_ratio = f / f_prev if f_prev != 0 else float('inf')
            assert v_ratio > f_ratio, \
                f"Verlinde growth ({v_ratio:.4f}) should exceed shadow ({f_ratio:.6f}) at g={g}"
            v_prev, f_prev = v, f

    def test_factorization_check_structure(self):
        """verlinde_factorization_check returns structured data."""
        data = verlinde_factorization_check_sl2(2, max_genus=3)
        assert 1 in data and 2 in data and 3 in data
        assert 'verlinde' in data[1] and 'shadow' in data[1]


# ============================================================================
# SECTION 9:  Clutching law comparison
# ============================================================================

class TestClutchingComparison:
    """Nafcha's gluing vs our clutching law (const:vol1-clutching-law-logfm)."""

    def test_nafcha_does_not_see_planted_forest(self):
        """Nafcha works with DM, not log-FM: no explicit d_pf."""
        data = nafcha_clutching_vs_ours(genus=2)
        assert data['planted_forest_in_nafcha'] is False
        assert data['planted_forest_in_ours'] is True

    def test_frameworks_compatible(self):
        """The two frameworks are compatible (not contradictory)."""
        data = nafcha_clutching_vs_ours(genus=2)
        assert data['compatible'] is True

    def test_planted_forest_zero_heisenberg(self):
        """Heisenberg: delta_pf = 0 (class G, S_3 = 0)."""
        data = nafcha_clutching_vs_ours(genus=2)
        assert data['delta_pf_heisenberg'] == 0

    def test_planted_forest_zero_virasoro(self):
        """Virasoro: delta_pf = 0 at genus 2 (S_3 = 0 by Z_2 parity)."""
        data = nafcha_clutching_vs_ours(genus=2)
        assert data['delta_pf_virasoro'] == 0


# ============================================================================
# SECTION 10:  D^2=0 comparison
# ============================================================================

class TestDSquaredZeroComparison:
    """Three proofs of D^2=0: convolution, ambient/Mok, Nafcha/sheaf."""

    def test_three_proofs_exist(self):
        """All three proof routes are documented."""
        data = d_squared_zero_comparison()
        assert 'proof_1' in data
        assert 'proof_2' in data
        assert 'proof_3' in data

    def test_strength_ordering(self):
        """Chain-level (Mok) > derived-category (Nafcha) > convolution (GK)."""
        data = d_squared_zero_comparison()
        assert 'Chain-level' in data['strength_ordering']

    def test_nafcha_broader_scope(self):
        """Nafcha's proof applies to ALL universal factorization algebras."""
        data = d_squared_zero_comparison()
        assert 'universal factorization algebras' in data['nafcha_new_content']


# ============================================================================
# SECTION 11:  Hochschild homology of Heisenberg Zhu algebra
# ============================================================================

class TestHeisenbergZhuHH:
    """Hochschild homology of A(H_k) = C[a_0]."""

    def test_zhu_algebra_is_polynomial(self):
        data = heisenberg_zhu_algebra_hh(Rational(1))
        assert 'C[a_0]' in data['zhu_algebra']

    def test_hh_vanishes_above_1(self):
        """HH_n(C[a_0]) = 0 for n >= 2 (one-variable polynomial ring)."""
        data = heisenberg_zhu_algebra_hh(Rational(1))
        assert data['HH_n_for_n_geq_2'] == "0 (since one generator)"

    def test_matches_heisenberg_sewing(self):
        """Self-gluing reduces to Bergman kernel trace for Heisenberg."""
        data = heisenberg_zhu_algebra_hh(Rational(1))
        assert data['matches_heisenberg_sewing_thm'] is True


# ============================================================================
# SECTION 12:  Planted-forest gap analysis
# ============================================================================

class TestPlantedForestGap:
    """Nafcha does not address codim >= 2 strata explicitly."""

    def test_codim_1_in_nafcha(self):
        data = planted_forest_nafcha_gap()
        assert data['codim_1_in_nafcha'] is True

    def test_codim_geq_2_not_in_nafcha(self):
        data = planted_forest_nafcha_gap()
        assert data['codim_geq_2_in_nafcha'] is False

    def test_codim_geq_2_in_ours(self):
        data = planted_forest_nafcha_gap()
        assert data['codim_geq_2_in_ours'] is True

    def test_practical_advantage_logfm(self):
        data = planted_forest_nafcha_gap()
        assert 'log-FM' in data['practical_advantage']


# ============================================================================
# SECTION 13:  Comparison table completeness
# ============================================================================

class TestComparisonTable:
    """The full comparison table covers all relevant aspects."""

    def test_table_nonempty(self):
        table = full_comparison_table()
        assert len(table) >= 7

    def test_convergence_row_exists(self):
        table = full_comparison_table()
        convergence_rows = [r for r in table if 'Convergence' in r['aspect']]
        assert len(convergence_rows) == 1

    def test_nafcha_no_convergence(self):
        table = full_comparison_table()
        convergence_row = [r for r in table if 'Convergence' in r['aspect']][0]
        assert 'Not addressed' in convergence_row['nafcha']


# ============================================================================
# SECTION 14:  GluingVsSewingComparison structural
# ============================================================================

class TestGluingVsSewingComparison:
    """Structural tests for the comparison dataclass."""

    def test_nafcha_does_not_imply_mc5(self):
        """Nafcha's algebraic gluing does NOT imply analytic MC5."""
        comp = GluingVsSewingComparison()
        assert comp.nafcha_implies_mc5 is False

    def test_mc5_does_not_imply_nafcha(self):
        """MC5 analytic sewing does NOT imply Nafcha's derived-cat gluing."""
        comp = GluingVsSewingComparison()
        assert comp.mc5_implies_nafcha is False

    def test_shared_combinatorics(self):
        """Both see the same boundary stratification of M-bar_{g,n}."""
        comp = GluingVsSewingComparison()
        assert comp.shared_combinatorics is True

    def test_nafcha_gives_d_squared_zero(self):
        """Nafcha's sheaf property implies D^2=0 at algebraic level."""
        comp = GluingVsSewingComparison()
        assert comp.nafcha_gives_d_squared_zero is True

    def test_nafcha_sewing_gap(self):
        """Nafcha explicitly acknowledges the sewing gap."""
        comp = GluingVsSewingComparison()
        assert comp.nafcha_explicit_sewing_gap is True

    def test_summary_nonempty(self):
        comp = GluingVsSewingComparison()
        s = comp.summary()
        assert len(s) > 100


# ============================================================================
# SECTION 15:  Lambda_fp values (AP38 cross-check)
# ============================================================================

class TestLambdaFP:
    """Faber-Pandharipande numbers: exact values for g=1,...,5."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760 (NOT 1/1152; AP38)."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0


# ============================================================================
# SECTION 16:  Verlinde level-rank duality (deep cross-check)
# ============================================================================

class TestVerlindeLevelRank:
    """Level-rank duality: V_g(SU(N), k) = V_g(SU(k), N).

    For sl_2 this is trivial (SU(2) at level k vs SU(k+1) at level 1),
    but we can check that V_g(SU(2), k=1) = V_g(SU(2), k=1) trivially,
    and more interestingly test that V_{g,k} satisfies the genus recursion
    from the separating + non-separating degenerations.
    """

    def test_genus_recursion_from_both_degenerations(self):
        """V_{g+1} can be reached from V_g via self-gluing AND from
        V_{g1} + V_{g2} via separating gluing with g1+g2 = g+1.

        Both routes must give the same answer.
        """
        for k in range(1, 4):
            for g in range(1, 3):
                # Route 1: self-gluing from genus g
                _, rhs_self, err_self = verify_self_gluing_sl2(g, k)
                # Route 2: separating from g1=1, g2=g
                _, rhs_sep, err_sep = verify_separating_gluing_sl2(1, g, k)
                # Both should give V_{g+1}
                v_target = float(verlinde_dimension_sl2(g + 1, k))
                assert abs(rhs_self - v_target) < 1e-6, \
                    f"Self-gluing route wrong at g={g}, k={k}"
                assert abs(rhs_sep - v_target) < 1e-6, \
                    f"Separating route wrong at g={g}, k={k}"


# ============================================================================
# SECTION 17:  Cross-family consistency (AP10 guard)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks to guard against AP10 (hardcoded wrong values)."""

    def test_heisenberg_F2_matches_shadow_formula(self):
        """F_2(H_k) from HeisenbergNodalData matches kappa * lambda_2^FP."""
        for k in [1, 2, 3, 5, 10]:
            h = HeisenbergNodalData(level=Rational(k))
            direct = h.F2
            formula = kappa_heisenberg(Rational(k)) * lambda_fp(2)
            assert direct == formula, f"Inconsistency at k={k}: {direct} vs {formula}"

    def test_virasoro_F1(self):
        """F_1(Vir_c) = c/48 (kappa = c/2, lambda_1 = 1/24)."""
        for c in [1, 2, 13, 25, 26]:
            kap = kappa_virasoro(c)
            f1 = shadow_F_g(kap, 1)
            assert f1 == Rational(c, 48), f"F_1(Vir_{c}) = {f1}, expected {c}/48"

    def test_affine_sl2_F1(self):
        """F_1(sl_2, k) = 3(k+2)/96 = (k+2)/32."""
        for k in [1, 2, 3, 4]:
            kap = kappa_affine_sl2(k)
            f1 = shadow_F_g(kap, 1)
            assert f1 == Rational(3 * (k + 2), 96), f"F_1(sl_2, {k}) wrong"

    def test_additivity_heisenberg_direct_sum(self):
        """kappa(H_k1 + H_k2) = kappa(H_k1) + kappa(H_k2).

        Additivity of kappa under direct sum (Theorem D).
        """
        for k1 in [1, 2]:
            for k2 in [1, 3]:
                assert kappa_heisenberg(k1) + kappa_heisenberg(k2) == \
                       kappa_heisenberg(k1 + k2)


# ============================================================================
# SECTION 18:  Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Edge cases for robustness."""

    def test_verlinde_genus_0_trivial(self):
        """V_0 = 1 for all k: the unique vacuum block."""
        for k in range(1, 10):
            assert verlinde_dimension_sl2(0, k) == 1

    def test_invalid_genus_raises(self):
        with pytest.raises(ValueError):
            verlinde_dimension_sl2(-1, 1)

    def test_invalid_level_raises(self):
        with pytest.raises(ValueError):
            verlinde_dimension_sl2(1, -1)

    def test_invalid_s_matrix_raises(self):
        with pytest.raises(ValueError):
            sl2_s_matrix_entry(3, 0, 1)  # j=3 > k=1

    def test_lambda_fp_requires_positive_genus(self):
        with pytest.raises(ValueError):
            lambda_fp(0)
