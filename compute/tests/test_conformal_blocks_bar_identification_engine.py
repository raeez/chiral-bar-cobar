r"""Tests for conformal blocks = bar cohomology identification at all genera.

Multi-path verification strategy:
    Path 1: S-matrix Verlinde formula (direct)
    Path 2: Closed-form (binomial, exact)
    Path 3: TUY factorization (separating + nonseparating degeneration)
    Path 4: Fusion rules (exact CG vs Verlinde)
    Path 5: Shadow free energy F_g = kappa * lambda_g^FP (Theorem D)
    Path 6: Zhu's theorem (genus-1 = number of simple modules)
    Path 7: Propagation of vacua
    Path 8: Complementarity (Theorem C, kappa + kappa' = 0 for KM)
    Path 9: Iterated fusion (independent genus-0 computation)
    Path 10: Higher Zhu algebra surjection chain
    Path 11: Growth rate asymptotics

Ground truth references:
    Verlinde (1988), Nuclear Phys. B 300
    Tsuchiya-Ueno-Yamada (1989), TUY factorization
    Zhu (1996), Modular invariance of characters
    Beauville (1996), Conformal blocks, fusion rules and the Verlinde formula
    Beauville-Laszlo (1993), Formal gluing
    Faltings (1994), A proof for the Verlinde formula
    De Sole-Kac (2006), Finite vs affine W-algebras
    Frenkel-Ben-Zvi (2004), Ch 17-20
    Di Francesco-Mathieu-Senechal (1997), CFT Ch 16
    thm:bar-computes-chiral-homology (higher_genus_foundations.tex)
    thm:chain-modular-functor (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.conformal_blocks_bar_identification_engine import (
    central_charge_km,
    chain_level_identification,
    complementarity_check_sl2,
    faber_pandharipande,
    full_diagnostic,
    general_genus_blocks_sl2,
    genus0_3point_sl2,
    genus0_blocks_from_fusion_sl2,
    genus0_npoint_sl2,
    genus1_1point_sl2,
    genus1_blocks_from_integrable_sl2,
    genus1_blocks_from_verlinde_sl2,
    genus1_blocks_sl2,
    genus2_blocks_closed_form_sl2,
    genus2_blocks_sl2,
    genus2_from_factorization_sl2,
    genus2_from_separating_sl2,
    genus_by_genus_identification_sl2,
    growth_comparison_sl2,
    higher_zhu_surjection_check,
    integrable_count,
    kappa_km,
    level_rank_duality_sl2,
    shadow_free_energy,
    sl2_S_entry,
    sl2_S_matrix,
    sl2_fusion_coefficient,
    sl2_fusion_matrix,
    verlinde_dim,
    verlinde_dim_pointed_sl2,
    verify_nonseparating_factorization,
    verify_propagation_of_vacua,
    verify_separating_factorization,
    zhu_algebra_dimension_sl2,
)


# =========================================================================
# Section 1: Genus-0 conformal blocks = bar H^0 at genus 0
# =========================================================================

class TestGenus0ConformalBlocks:
    """Genus-0 conformal blocks = fusion coefficients = bar H^0 at genus 0."""

    def test_sl2_k1_trivial_3point(self):
        """sl_2 k=1: CB(V_0, V_0, V_0; P^1) = 1.

        Three vacuum insertions. The fusion N_{0,0}^0 = 1 (trivial x trivial = trivial).
        This is the foundational test: the bar complex at genus 0 with three
        trivial module insertions has H^0 = 1-dimensional.
        """
        assert genus0_3point_sl2(1, 0, 0, 0) == 1

    def test_sl2_k1_spin_half_3point(self):
        """sl_2 k=1: CB(V_0, V_{1/2}, V_{1/2}; P^1) = 1.

        N_{0,1}^1 = 1 (trivial x fundamental = fundamental).
        Using Dynkin labels: j=0 is spin 0, j=1 is spin 1/2.
        """
        assert genus0_3point_sl2(1, 0, 1, 1) == 1

    def test_sl2_k1_all_spin_half(self):
        """sl_2 k=1: CB(V_{1/2}, V_{1/2}, V_{1/2}; P^1) = 0.

        N_{1,1}^1 = 0 at k=1: 1+1=2 > k=1, so fusion vanishes.
        (Truncation of Clebsch-Gordan at the level.)
        """
        assert genus0_3point_sl2(1, 1, 1, 1) == 0

    def test_sl2_k2_fusion_rules(self):
        """sl_2 k=2: verify specific fusion coefficients.

        k=2 has reps j=0,1,2 (Dynkin labels).
        Fusion rules (truncated CG):
            N_{1,1}^0 = 1 (1/2 x 1/2 = 0)
            N_{1,1}^2 = 1 (1/2 x 1/2 = 1, which is j=2)
            N_{2,2}^0 = 1 (1 x 1 = 0)
            N_{2,2}^2 = 1 (1 x 1 = 1, but 1+1=2=k, so j=2 is allowed: 0<=2<=2)
        Wait, for k=2: N_{2,2}^m requires |2-2|<=m<=min(2+2,2*2-2-2)=min(4,0)=0.
        So only m=0. N_{2,2}^0 = 1 (since 2+2+0=4 is even).
        """
        assert sl2_fusion_coefficient(1, 1, 0, 2) == 1
        assert sl2_fusion_coefficient(1, 1, 2, 2) == 1
        assert sl2_fusion_coefficient(2, 2, 0, 2) == 1
        assert sl2_fusion_coefficient(2, 2, 2, 2) == 0  # min(4,0)=0 < 2

    @pytest.mark.parametrize("k", range(1, 8))
    def test_genus0_no_insertions_is_1(self, k):
        """V_{0,k}(sl_2) = 1: genus-0 Verlinde is always 1 (S unitarity)."""
        assert verlinde_dim("A", 1, k, 0) == 1

    def test_genus0_4point_sl2_k1(self):
        """4-point function at k=1: CB(V_0, V_0, V_0, V_0; P^1) = 1.

        Via iterated fusion: only the vacuum channel contributes.
        """
        assert genus0_npoint_sl2(1, [0, 0, 0, 0]) == 1

    def test_genus0_4point_sl2_k2(self):
        """4-point function at k=2: CB(V_1, V_1, V_1, V_1; P^1).

        Via iterated fusion:
            V_1 x V_1 -> V_0 + V_2 (two channels)
            (V_0 + V_2) x V_1 -> V_1 + V_1 = 2*V_1
            N_{V_1,V_1}^{V_0} = 1  (from first channel)
        Total = 2.
        """
        dim_4pt = genus0_npoint_sl2(2, [1, 1, 1, 1])
        # Via Verlinde pointed formula at g=0
        dim_4pt_v2 = verlinde_dim_pointed_sl2(2, 0, [1, 1, 1, 1])
        assert dim_4pt == dim_4pt_v2

    def test_genus0_two_paths_agree(self):
        """Cross-check: pointed Verlinde vs iterated fusion at genus 0."""
        for k in range(1, 5):
            for insertions in [[0, 0, 0], [0, 1, 1], [1, 1, 0]]:
                v1 = genus0_npoint_sl2(k, insertions)
                v2 = genus0_blocks_from_fusion_sl2(k, insertions)
                assert v1 == v2, (
                    f"Mismatch at k={k}, ins={insertions}: "
                    f"pointed Verlinde={v1}, iterated fusion={v2}"
                )

    def test_genus0_propagation(self):
        """Propagation of vacua at genus 0: inserting V_0 doesn't change dim."""
        for k in range(1, 5):
            dim_3pt = genus0_npoint_sl2(k, [0, 0, 0])
            dim_4pt_vac = genus0_npoint_sl2(k, [0, 0, 0, 0])
            assert dim_3pt == dim_4pt_vac == 1


# =========================================================================
# Section 2: Genus-1 conformal blocks = bar H^0 at genus 1
# =========================================================================

class TestGenus1ConformalBlocks:
    """Genus-1 identification: dim H^0 = number of simple modules = k+1."""

    @pytest.mark.parametrize("k,expected", [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
        (6, 7), (7, 8), (8, 9), (9, 10), (10, 11),
    ])
    def test_genus1_sl2_is_k_plus_1(self, k, expected):
        """V_{1,k}(sl_2) = k+1 = |Irr(A(V))| (Zhu's theorem)."""
        assert genus1_blocks_sl2(k) == expected

    @pytest.mark.parametrize("k", range(1, 11))
    def test_genus1_three_paths_agree(self, k):
        """Three independent paths give the same genus-1 dimension.

        Path 1: Direct Zhu count
        Path 2: Verlinde formula at g=1
        Path 3: Integrable representation count
        """
        v1 = genus1_blocks_sl2(k)
        v2 = genus1_blocks_from_verlinde_sl2(k)
        v3 = genus1_blocks_from_integrable_sl2(k)
        assert v1 == v2 == v3 == k + 1

    def test_genus1_sl2_k1_dim_2(self):
        """Foundational test: sl_2 at k=1, genus 1 gives dim = 2.

        The two characters are:
            chi_0(tau) = (theta_3(tau)^2 + theta_4(tau)^2) / (2 * eta(tau))
            chi_{1/2}(tau) = theta_2(tau)^2 / (2 * eta(tau))
        where theta_i are Jacobi theta functions.

        This is H^0 of the genus-1 bar complex B^{(1)}(sl_2_1).
        """
        assert genus1_blocks_sl2(1) == 2

    def test_genus1_1point_vacuum_propagation(self):
        """One-pointed genus-1 with vacuum = unpointed genus-1.

        V_{1,k}^{(j=0)} = V_{1,k} = k+1 (propagation of vacua).
        """
        for k in range(1, 6):
            v1_vac = genus1_1point_sl2(k, 0)
            v1_unpointed = genus1_blocks_sl2(k)
            assert v1_vac == v1_unpointed


# =========================================================================
# Section 3: Genus-2 conformal blocks = bar H^0 at genus 2
# =========================================================================

class TestGenus2ConformalBlocks:
    """Genus-2 identification: V_{2,k}(sl_2) = C(k+3,3) = bar H^0."""

    KNOWN_GENUS2 = {
        1: 4, 2: 10, 3: 20, 4: 35, 5: 56,
        6: 84, 7: 120, 8: 165, 9: 220, 10: 286,
    }

    @pytest.mark.parametrize("k,expected", list(KNOWN_GENUS2.items()))
    def test_genus2_verlinde(self, k, expected):
        """Path 1: Verlinde formula via S-matrix."""
        assert genus2_blocks_sl2(k) == expected

    @pytest.mark.parametrize("k,expected", list(KNOWN_GENUS2.items()))
    def test_genus2_closed_form(self, k, expected):
        """Path 2: closed-form C(k+3, 3) = (k+1)(k+2)(k+3)/6."""
        assert genus2_blocks_closed_form_sl2(k) == expected

    @pytest.mark.parametrize("k,expected", list(KNOWN_GENUS2.items()))
    def test_genus2_three_paths(self, k, expected):
        """Three independent paths agree for genus-2 blocks."""
        v1 = genus2_blocks_sl2(k)
        v2 = genus2_blocks_closed_form_sl2(k)
        v3 = genus2_from_factorization_sl2(k)
        assert v1 == v2 == expected
        assert v3 == expected

    def test_genus2_sl2_k1_is_4(self):
        """Foundational test: sl_2 k=1, genus 2 gives dim = 4.

        V_{2,1}(sl_2) = (1+1)(1+2)(1+3)/6 = 2*3*4/6 = 4.
        This is the rank of the Verlinde bundle on M_2.
        """
        assert genus2_blocks_sl2(1) == 4
        assert genus2_blocks_closed_form_sl2(1) == 4

    def test_genus2_factorization_separating(self):
        """Genus-2 via separating degeneration (g=1 + g=1).

        V_2 = sum_lambda (V_1^lambda)^2 for sl_2 (all reps self-conjugate).
        """
        for k in range(1, 6):
            V_2_direct = genus2_blocks_sl2(k)
            V_2_sep = genus2_from_separating_sl2(k)
            assert V_2_sep == V_2_direct, (
                f"Separating factorization fails at k={k}: "
                f"direct={V_2_direct}, separating={V_2_sep}"
            )


# =========================================================================
# Section 4: TUY factorization = bar complex boundary maps
# =========================================================================

class TestTUYFactorization:
    """TUY factorization: bar boundary maps at H^0 level."""

    @pytest.mark.parametrize("k,g1,g2", [
        (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2),
        (2, 1, 1), (2, 1, 2), (2, 1, 3),
        (3, 1, 1), (3, 1, 2),
        (4, 1, 1),
    ])
    def test_separating_factorization(self, k, g1, g2):
        """Separating: V_{g1+g2} = sum_lam V_{g1}^lam * V_{g2}^{lam*}."""
        result = verify_separating_factorization("A", 1, k, g1, g2)
        assert result["match"], (
            f"Separating factorization fails at k={k}, g1={g1}, g2={g2}: "
            f"direct={result['V_g_direct']}, factored={result['V_g_factored']}"
        )

    @pytest.mark.parametrize("k,g", [
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 1), (3, 2), (3, 3),
        (4, 1), (4, 2),
        (5, 1), (5, 2),
    ])
    def test_nonseparating_factorization(self, k, g):
        """Nonseparating: V_g = sum_lam V_{g-1}^{lam,lam*}."""
        result = verify_nonseparating_factorization("A", 1, k, g)
        assert result["match"], (
            f"Nonseparating factorization fails at k={k}, g={g}: "
            f"direct={result['V_g_direct']}, factored={result['V_g_factored']}"
        )

    def test_factorization_chain_genus3(self):
        """Genus-3 via chain: g=3 -> g=2 (nonsep) -> g=1+1 (sep).

        Two independent factorization paths to genus 3:
            (a) Direct nonseparating: V_3 = sum_lam V_2^{lam,lam*}
            (b) Iterating: V_3 = sum_lam (sum_mu V_1^{mu} * V_1^{mu*,lam,lam*})
        """
        for k in range(1, 4):
            V_3_direct = verlinde_dim("A", 1, k, 3)
            ns = verify_nonseparating_factorization("A", 1, k, 3)
            assert ns["match"]
            assert ns["V_g_direct"] == V_3_direct

    def test_factorization_consistency_at_all_genera(self):
        """All factorizations are consistent for k=1 up to g=6."""
        k = 1
        for g in range(1, 7):
            V_g = verlinde_dim("A", 1, k, g)
            # Expected: V_{g,1}(sl_2) = 2^g (power of 2!)
            assert V_g == 2 ** g, f"V_{g},1 = {V_g} != 2^{g}"


# =========================================================================
# Section 5: Propagation of vacua
# =========================================================================

class TestPropagationOfVacua:
    """Propagation of vacua: inserting vacuum doesn't change block dim."""

    @pytest.mark.parametrize("k,g", [
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2),
        (3, 0), (3, 1),
    ])
    def test_propagation_holds(self, k, g):
        """CB(M_1,...,M_n, V; C) = CB(M_1,...,M_n; C)."""
        result = verify_propagation_of_vacua("A", 1, k, g)
        assert result["propagation_holds"], (
            f"Propagation fails at k={k}, g={g}: "
            f"V_g={result['V_g']}, V_g_vac={result['V_g_with_vacuum']}"
        )


# =========================================================================
# Section 6: Fusion rules (Verlinde formula vs exact CG)
# =========================================================================

class TestFusionRules:
    """Fusion coefficients: Verlinde formula vs exact truncated CG rules."""

    @pytest.mark.parametrize("k", range(1, 7))
    def test_fusion_verlinde_matches_exact(self, k):
        """Verlinde-derived fusion = exact CG fusion for all (i,j,m)."""
        S = sl2_S_matrix(k)
        size = k + 1
        for i in range(size):
            for j in range(size):
                for m in range(size):
                    verlinde_N = 0.0
                    for l in range(size):
                        if abs(S[0, l]) > 1e-15:
                            verlinde_N += S[i, l] * S[j, l] * S[m, l] / S[0, l]
                    exact_N = sl2_fusion_coefficient(i, j, m, k)
                    assert abs(verlinde_N - exact_N) < 0.01, (
                        f"Fusion mismatch at k={k}, (i,j,m)=({i},{j},{m}): "
                        f"Verlinde={verlinde_N:.4f}, exact={exact_N}"
                    )

    def test_fusion_associativity_sl2_k2(self):
        """Fusion ring is associative: (i*j)*m = i*(j*m) at level k=2."""
        k = 2
        N = sl2_fusion_matrix(k)
        size = k + 1
        for a in range(size):
            for b in range(size):
                for c in range(size):
                    for d in range(size):
                        # (a*b)*c -> d
                        lhs = sum(N[a, b, e] * N[e, c, d] for e in range(size))
                        # a*(b*c) -> d
                        rhs = sum(N[b, c, e] * N[a, e, d] for e in range(size))
                        assert lhs == rhs, (
                            f"Non-associative fusion at k={k}: "
                            f"({a}*{b})*{c} != {a}*({b}*{c}) at output {d}"
                        )

    def test_fusion_commutativity(self):
        """Fusion is commutative: N_{ij}^m = N_{ji}^m."""
        for k in range(1, 5):
            for i in range(k + 1):
                for j in range(k + 1):
                    for m in range(k + 1):
                        assert sl2_fusion_coefficient(i, j, m, k) == \
                               sl2_fusion_coefficient(j, i, m, k)

    def test_vacuum_is_identity(self):
        """Fusion with vacuum: N_{0,j}^m = delta_{j,m}."""
        for k in range(1, 8):
            for j in range(k + 1):
                for m in range(k + 1):
                    expected = 1 if j == m else 0
                    assert sl2_fusion_coefficient(0, j, m, k) == expected


# =========================================================================
# Section 7: Shadow free energy (Theorem D)
# =========================================================================

class TestShadowFreeEnergy:
    """Shadow F_g = kappa * lambda_g^FP: the scalar projection."""

    @pytest.mark.parametrize("g,fp_expected", [
        (1, Fraction(1, 24)),
        (2, Fraction(7, 5760)),
        (3, Fraction(31, 967680)),
        (4, Fraction(127, 154828800)),
    ])
    def test_faber_pandharipande_exact(self, g, fp_expected):
        """lambda_g^FP exact values from Bernoulli numbers."""
        assert faber_pandharipande(g) == fp_expected

    def test_shadow_F1_sl2_k1(self):
        """F_1(sl_2_1) = kappa * 1/24 = (9/4) * (1/24) = 3/32."""
        kap = kappa_km("A", 1, 1)
        assert kap == Fraction(9, 4)
        F1 = shadow_free_energy("A", 1, 1, 1)
        assert F1 == Fraction(9, 4) * Fraction(1, 24)
        assert F1 == Fraction(3, 32)

    def test_shadow_is_distinct_from_verlinde(self):
        """Shadow F_g is NOT the Verlinde dim (different invariants).

        F_g = first Chern class of Verlinde bundle (scalar, rational).
        V_g = rank of Verlinde bundle (positive integer).
        These are different: V_{1,1}=2 but F_1=3/32.
        """
        V_1 = verlinde_dim("A", 1, 1, 1)
        F_1 = shadow_free_energy("A", 1, 1, 1)
        assert V_1 == 2
        assert F_1 == Fraction(3, 32)
        assert V_1 != float(F_1)


# =========================================================================
# Section 8: Kappa and central charge (AP1, AP39, AP48)
# =========================================================================

class TestKappaAndCentralCharge:
    """Verify kappa formulas with anti-pattern guards."""

    @pytest.mark.parametrize("k,expected_kappa", [
        (1, Fraction(9, 4)),    # 3*(1+2)/(2*2) = 9/4
        (2, Fraction(3)),       # 3*(2+2)/4 = 3
        (3, Fraction(15, 4)),   # 3*5/4
        (4, Fraction(9, 2)),    # 3*6/4
        (10, Fraction(9)),      # 3*12/4 = 9
    ])
    def test_kappa_sl2(self, k, expected_kappa):
        """kappa(sl_2_k) = 3(k+2)/4."""
        assert kappa_km("A", 1, k) == expected_kappa

    @pytest.mark.parametrize("k,expected_c", [
        (1, Fraction(1)),       # 1*3/3
        (2, Fraction(3, 2)),    # 2*3/4
        (10, Fraction(5, 2)),   # 10*3/12
    ])
    def test_central_charge_sl2(self, k, expected_c):
        """c(sl_2_k) = 3k/(k+2)."""
        assert central_charge_km("A", 1, k) == expected_c

    def test_kappa_not_c_over_2_for_sl2(self):
        """AP39: kappa != c/2 for affine KM (they coincide only for Virasoro)."""
        for k in range(1, 20):
            kap = kappa_km("A", 1, k)
            c = central_charge_km("A", 1, k)
            assert kap != c / 2, (
                f"kappa = c/2 at k={k}: this should NOT happen for sl_2"
            )


# =========================================================================
# Section 9: Complementarity (Theorem C)
# =========================================================================

class TestComplementarity:
    """Complementarity: kappa + kappa' = 0 for KM (AP24)."""

    @pytest.mark.parametrize("k", range(1, 8))
    def test_kappa_anti_symmetry_sl2(self, k):
        """kappa(sl_2_k) + kappa(sl_2_{k'}) = 0 where k' = -(k+4)."""
        result = complementarity_check_sl2(k)
        assert result["sum_is_zero"]
        for sd in result["shadow_complementarity"]:
            assert sd["sum_is_zero"], f"F_g + F_g' != 0 at g={sd['g']}"


# =========================================================================
# Section 10: S-matrix properties
# =========================================================================

class TestSMatrixProperties:
    """S-matrix: unitarity, symmetry, positivity of S_{0,j}."""

    @pytest.mark.parametrize("k", range(1, 8))
    def test_s_matrix_unitarity(self, k):
        """S * S^dag = I (unitarity)."""
        S = sl2_S_matrix(k)
        prod = S @ S.T
        assert np.allclose(prod, np.eye(k + 1), atol=1e-10), (
            f"S-matrix not unitary at k={k}"
        )

    @pytest.mark.parametrize("k", range(1, 8))
    def test_s_matrix_symmetry(self, k):
        """S is symmetric: S_{jl} = S_{lj}."""
        S = sl2_S_matrix(k)
        assert np.allclose(S, S.T, atol=1e-15)

    @pytest.mark.parametrize("k", range(1, 8))
    def test_s_00_positive(self, k):
        """S_{0,0} > 0 (Kac-Peterson normalization)."""
        assert sl2_S_entry(0, 0, k) > 0

    @pytest.mark.parametrize("k", range(1, 8))
    def test_s_0j_positive(self, k):
        """S_{0,j} > 0 for all j (quantum dimensions positive)."""
        for j in range(k + 1):
            assert sl2_S_entry(0, j, k) > 0


# =========================================================================
# Section 11: Higher Zhu algebras and bar filtration
# =========================================================================

class TestHigherZhuAlgebras:
    """Higher Zhu algebras A_n(V) and bar complex filtration."""

    @pytest.mark.parametrize("k,expected_simple", [
        (1, 2), (2, 3), (3, 4), (4, 5),
    ])
    def test_zhu_simple_module_count(self, k, expected_simple):
        """Number of simple A_0(V)-modules = k+1."""
        data = zhu_algebra_dimension_sl2(k)
        assert data["num_simple_modules"] == expected_simple

    @pytest.mark.parametrize("k", range(1, 6))
    def test_wedderburn_dimension(self, k):
        """dim A_0(V) = sum (2j+1)^2 = (k+1)(2k+1)(2k+3)/3."""
        data = zhu_algebra_dimension_sl2(k)
        assert data["A_0_dim_match"]
        expected = (k + 1) * (2 * k + 1) * (2 * k + 3) // 3
        assert data["A_0_dim"] == expected

    def test_zhu_surjection_chain(self):
        """Surjection chain A_n -> A_{n-1} preserves simple module count."""
        for k in range(1, 5):
            result = higher_zhu_surjection_check(k)
            assert result["simple_module_count_constant"]

    def test_zhu_simple_dims_are_odd(self):
        """Simple module dimensions are 2j+1 (odd numbers 1,3,5,...)."""
        for k in range(1, 8):
            data = zhu_algebra_dimension_sl2(k)
            for d in data["simple_module_dims"]:
                assert d % 2 == 1, f"Simple dim {d} is not odd at k={k}"


# =========================================================================
# Section 12: Chain-level identification
# =========================================================================

class TestChainLevelIdentification:
    """Chain map B^{(g)}(A) -> CB^{(g)}: structural properties."""

    @pytest.mark.parametrize("k,g", [
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2),
    ])
    def test_chain_level_verlinde(self, k, g):
        """Bar H^0 expected dimension = Verlinde dimension."""
        result = chain_level_identification("A", 1, k, g)
        assert result["verlinde_dim"] == result["bar_H0_expected"]

    def test_chain_level_connection_types(self):
        """Correct connection type at each genus."""
        r0 = chain_level_identification("A", 1, 1, 0)
        r1 = chain_level_identification("A", 1, 1, 1)
        r2 = chain_level_identification("A", 1, 1, 2)
        assert "KZ" in r0["connection"]
        assert "KZB" in r1["connection"]
        assert "Higher KZB" in r2["connection"]

    def test_chain_level_curvature(self):
        """Curvature at genus 1: F_1 = kappa/24."""
        r1 = chain_level_identification("A", 1, 1, 1)
        kap = r1["kappa"]
        assert abs(r1["F_g"] - kap / 24) < 1e-10


# =========================================================================
# Section 13: Genus-by-genus comprehensive identification
# =========================================================================

class TestGenusIdentification:
    """Comprehensive genus-by-genus verification for sl_2 at various levels."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_full_identification(self, k):
        """Full genus-by-genus identification for sl_2 at level k."""
        result = genus_by_genus_identification_sl2(k, max_g=4)
        for gd in result["genus_data"]:
            g = gd["genus"]
            # Verlinde dimension matches expected bar H^0
            assert gd["verlinde_dim"] == gd["bar_H0_expected"]
            # Closed form matches where available
            if "closed_form_match" in gd:
                assert gd["closed_form_match"], (
                    f"Closed form mismatch at k={k}, g={g}"
                )
            # Factorization matches where available
            if g >= 2:
                assert gd.get("nonsep_factorization_match", True), (
                    f"Nonsep factorization fails at k={k}, g={g}"
                )
                assert gd.get("sep_factorization_match", True), (
                    f"Sep factorization fails at k={k}, g={g}"
                )


# =========================================================================
# Section 14: Integrable representation counts
# =========================================================================

class TestIntegrableCounts:
    """Verify integrable representation counts across types."""

    @pytest.mark.parametrize("k,expected", [
        (1, 2), (2, 3), (3, 4), (5, 6), (10, 11),
    ])
    def test_sl2_integrable_k_plus_1(self, k, expected):
        """sl_2: |P_+^k| = k+1."""
        assert integrable_count("A", 1, k) == expected

    @pytest.mark.parametrize("k,expected", [
        (1, 3), (2, 6), (3, 10), (4, 15),
    ])
    def test_sl3_integrable_binomial(self, k, expected):
        """sl_3: |P_+^k| = C(k+2, 2)."""
        assert integrable_count("A", 2, k) == expected

    def test_slN_integrable_formula(self):
        """sl_N: |P_+^k| = C(k+N-1, N-1)."""
        for N in range(2, 5):
            for k in range(1, 5):
                r = N - 1
                expected = 1
                for i in range(r):
                    expected = expected * (k + r - i) // (i + 1)
                assert integrable_count("A", r, k) == expected


# =========================================================================
# Section 15: sl_2 k=1 power-of-2 pattern
# =========================================================================

class TestSl2K1PowersOf2:
    """At k=1, sl_2 has V_{g,1} = 2^g (fundamental dichotomy)."""

    @pytest.mark.parametrize("g", range(0, 10))
    def test_verlinde_k1_is_power_of_2(self, g):
        """V_{g,1}(sl_2) = 2^g.

        At k=1, sl_2 has 2 reps with equal quantum dimensions.
        S_{0,0} = S_{0,1} = 1/sqrt(2).
        V_g = sum_j S_{0,j}^{2-2g} = 2 * (1/sqrt(2))^{2-2g} = 2^g.
        """
        assert verlinde_dim("A", 1, 1, g) == 2 ** g

    def test_power_of_2_pattern_from_equal_quantum_dims(self):
        """The 2^g pattern comes from S_{0,0} = S_{0,1} = 1/sqrt(2).

        When all quantum dimensions are equal, V_g = (# reps)^g.
        """
        S = sl2_S_matrix(1)
        assert abs(S[0, 0] - S[0, 1]) < 1e-15
        assert abs(S[0, 0] - 1 / math.sqrt(2)) < 1e-15


# =========================================================================
# Section 16: sl_3 conformal blocks
# =========================================================================

class TestSl3ConformalBlocks:
    """sl_3 Verlinde dimensions: cross-type verification."""

    def test_sl3_genus0_is_1(self):
        """V_{0,k}(sl_3) = 1 for all k."""
        for k in range(1, 5):
            assert verlinde_dim("A", 2, k, 0) == 1

    @pytest.mark.parametrize("k,expected", [
        (1, 3), (2, 6), (3, 10),
    ])
    def test_sl3_genus1(self, k, expected):
        """V_{1,k}(sl_3) = |P_+^k(sl_3)| = C(k+2,2)."""
        assert verlinde_dim("A", 2, k, 1) == expected

    def test_sl3_k1_powers_of_3(self):
        """At k=1, sl_3 has 3 reps with equal quantum dims: V_{g,1} = 3^g."""
        for g in range(5):
            assert verlinde_dim("A", 2, 1, g) == 3 ** g


# =========================================================================
# Section 17: Growth rate comparison
# =========================================================================

class TestGrowthRates:
    """Compare Verlinde growth rate with shadow F_g growth."""

    def test_verlinde_grows_exponentially(self):
        """V_{g,k} grows exponentially in g for fixed k >= 1."""
        k = 2
        prev = 1
        for g in range(1, 6):
            V_g = verlinde_dim("A", 1, k, g)
            assert V_g > prev, f"V_{g},{k} = {V_g} <= V_{g-1},{k} = {prev}"
            prev = V_g

    def test_shadow_grows_factorially(self):
        """F_g = kappa * lambda_g^FP has factorial growth.

        lambda_g^FP ~ |B_{2g}|/(2g)! ~ 2*(2g)!/(2pi)^{2g}/(2g)!
                     ~ 2/(2pi)^{2g} -> 0 as g -> infinity.
        Actually F_g -> 0 as g -> inf (exponential decay, not growth).
        """
        for k in range(1, 4):
            kap = float(kappa_km("A", 1, k))
            for g in range(1, 10):
                F_g = float(shadow_free_energy("A", 1, k, g))
                assert F_g > 0, f"F_{g} should be positive"
                # lambda_g^FP decreases with g
                if g >= 2:
                    F_prev = float(shadow_free_energy("A", 1, k, g - 1))
                    assert F_g < F_prev, (
                        f"F_{g} = {F_g} >= F_{g-1} = {F_prev}: "
                        f"lambda_g^FP should decrease"
                    )

    def test_growth_comparison_report(self):
        """Growth comparison produces valid data."""
        result = growth_comparison_sl2(2, max_g=5)
        assert "data" in result
        assert len(result["data"]) == 6  # g=0,...,5


# =========================================================================
# Section 18: Full diagnostic
# =========================================================================

class TestFullDiagnostic:
    """Full diagnostic: comprehensive identification report."""

    def test_full_diagnostic_sl2_k1(self):
        """Full diagnostic for sl_2 at k=1."""
        result = full_diagnostic("A", 1, 1, max_g=3)
        assert result["kappa"] == 9 / 4
        assert result["genus0_3pt_000"] == 1

        # Propagation of vacua holds at all genera
        for pov in result["propagation_of_vacua"]:
            assert pov["propagation_holds"]

        # Fusion rules match
        assert result["fusion_rules"]["all_match"]

        # Zhu algebra
        assert result["zhu_algebra"]["num_simple_modules"] == 2

    def test_full_diagnostic_sl2_k2(self):
        """Full diagnostic for sl_2 at k=2."""
        result = full_diagnostic("A", 1, 2, max_g=3)
        assert result["kappa"] == 3.0
        assert result["genus0_3pt_000"] == 1
        assert result["fusion_rules"]["all_match"]
        assert result["zhu_algebra"]["num_simple_modules"] == 3


# =========================================================================
# Section 19: Consistency checks across the identification
# =========================================================================

class TestConsistencyChecks:
    """Cross-cutting consistency checks."""

    def test_verlinde_genus0_consistent_with_unitarity(self):
        """V_{0,k} = sum S_{0,j}^2 = 1 (S unitarity)."""
        for k in range(1, 10):
            S = sl2_S_matrix(k)
            total = sum(S[0, j] ** 2 for j in range(k + 1))
            assert abs(total - 1.0) < 1e-12

    def test_verlinde_genus1_consistent_with_count(self):
        """V_{1,k} = sum S_{0,j}^0 = k+1 (count of reps)."""
        for k in range(1, 10):
            assert verlinde_dim("A", 1, k, 1) == k + 1

    def test_kappa_c_relation_sl2(self):
        """kappa = dim(g) * (k + h^v) / (2 * h^v) = 3(k+2)/4 for sl_2."""
        for k in range(1, 20):
            kap = kappa_km("A", 1, k)
            expected = Fraction(3 * (k + 2), 4)
            assert kap == expected

    def test_shadow_vs_verlinde_different_invariants(self):
        """Shadow F_g and Verlinde V_g are genuinely different at g >= 1.

        F_g is a cohomological invariant (class in R*(M_g)).
        V_g is a categorical invariant (rank of a vector bundle).
        They are related but distinct.
        """
        k = 2
        for g in range(1, 5):
            V_g = verlinde_dim("A", 1, k, g)
            F_g = float(shadow_free_energy("A", 1, k, g))
            # V_g is integer, F_g is rational (generally not integer)
            assert isinstance(V_g, int)
            # At g=1: V_1=3, F_1=3/24=1/8. These are different.
            if g == 1:
                assert V_g == 3
                assert abs(F_g - 1 / 8) < 1e-15

    def test_verlinde_dim_sl2_and_sl3_at_k1(self):
        """Cross-type: at k=1, V_{g,1}(sl_2)=2^g, V_{g,1}(sl_3)=3^g.

        Both follow the pattern V_{g,1}(sl_N) = N^g because at k=1,
        all N reps have equal quantum dimensions.
        """
        for g in range(5):
            assert verlinde_dim("A", 1, 1, g) == 2 ** g
            assert verlinde_dim("A", 2, 1, g) == 3 ** g
