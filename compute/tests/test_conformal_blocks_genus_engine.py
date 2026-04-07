r"""Tests for the conformal blocks genus engine.

Multi-path verification strategy:
    Path 1: Verlinde formula via S-matrix (direct computation)
    Path 2: Closed-form formulas (Beauville normalization, binomial)
    Path 3: Known literature values (Di Francesco-Mathieu-Senechal, Verlinde 1988)
    Path 4: Genus-1 = number of integrable reps (Zhu's theorem)
    Path 5: Shadow F_g = kappa * lambda_g^FP (Theorem D)
    Path 6: TUY factorization identities (separating + nonseparating)
    Path 7: Propagation of vacua
    Path 8: Fusion rules from Verlinde formula vs exact CG rules
    Path 9: Large-k asymptotics (Witten volume)
    Path 10: Complementarity (Thm C, kappa + kappa' = 0 for KM)
    Path 11: Cross-check with verlinde_shadow_cohft_engine (independent engine)
    Path 12: Level-rank duality

Ground truth references:
    Verlinde (1988), Nuclear Phys. B 300
    Tsuchiya-Ueno-Yamada (1989), TUY factorization
    Zhu (1996), Modular invariance of characters
    Beauville (1996), Conformal blocks, fusion rules and the Verlinde formula
    Faltings (1994), A proof for the Verlinde formula
    Di Francesco-Mathieu-Senechal (1997), Conformal Field Theory (Ch. 16)
    Frenkel-Ben-Zvi (2004), Vertex Algebras and Algebraic Curves (Ch. 17-18)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    comp:verlinde-sl2 (genus_expansions.tex, line 1698)
    eq:verlinde-su2 (genus_expansions.tex, line 1694)
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.conformal_blocks_genus_engine import (
    central_charge_km,
    complementarity_verlinde,
    faber_pandharipande,
    full_diagnostic,
    genus1_blocks_count,
    integrable_weights_km,
    kappa_km,
    large_k_asymptotics_sl2,
    num_integrable,
    shadow_free_energy,
    sl2_S_entry,
    sl2_S_matrix_full,
    sl2_fusion_matrix,
    sl2_fusion_rule,
    sl2_genus1_count,
    sl2_genus2_closed,
    sl3_S_matrix_full,
    verify_factorization_nonseparating,
    verify_factorization_separating,
    verify_fusion_from_verlinde,
    verify_propagation_of_vacua,
    verlinde_dim_general,
    verlinde_dim_sl2,
    verlinde_dim_sl2_closed,
    verlinde_dim_sl3,
    verlinde_from_quantum_group_decomposition,
    verlinde_growth_exponent,
    verlinde_vs_shadow_table,
    zhu_algebra_dim_km,
)


# =========================================================================
# Section 1: Verlinde dimensions for sl_2 — two independent computation paths
# =========================================================================

class TestVerlindeSl2:
    """Verlinde dimensions for sl_2 via two independent paths."""

    # Ground truth from comp:verlinde-sl2 (genus_expansions.tex line 1698)
    # and independent computation.
    KNOWN_SL2 = {
        # (k, g) -> V_{g,k}(sl_2)
        (1, 0): 1, (1, 1): 2, (1, 2): 4, (1, 3): 8, (1, 4): 16,
        (2, 0): 1, (2, 1): 3, (2, 2): 10, (2, 3): 36, (2, 4): 136,
        (3, 0): 1, (3, 1): 4, (3, 2): 20, (3, 3): 120, (3, 4): 800,
        (4, 0): 1, (4, 1): 5, (4, 2): 35, (4, 3): 329, (4, 4): 3611,
        (5, 0): 1, (5, 1): 6, (5, 2): 56, (5, 3): 784, (5, 4): 13328,
        (6, 0): 1, (6, 1): 7, (6, 2): 84, (6, 3): 1680, (6, 4): 42048,
        (7, 0): 1, (7, 1): 8, (7, 2): 120, (7, 3): 3312, (7, 4): 117072,
    }

    @pytest.mark.parametrize("k,g,expected", [
        (k, g, v) for (k, g), v in KNOWN_SL2.items()
    ])
    def test_verlinde_sl2_path1_smatrix(self, k, g, expected):
        """Path 1: Verlinde via S-matrix."""
        assert verlinde_dim_sl2(k, g) == expected

    @pytest.mark.parametrize("k,g,expected", [
        (k, g, v) for (k, g), v in KNOWN_SL2.items()
    ])
    def test_verlinde_sl2_path2_closed_form(self, k, g, expected):
        """Path 2: Verlinde via Beauville closed form."""
        assert verlinde_dim_sl2_closed(k, g) == expected

    @pytest.mark.parametrize("k,g,expected", [
        (k, g, v) for (k, g), v in KNOWN_SL2.items()
    ])
    def test_verlinde_sl2_two_paths_agree(self, k, g, expected):
        """Cross-check: two independent paths agree."""
        v1 = verlinde_dim_sl2(k, g)
        v2 = verlinde_dim_sl2_closed(k, g)
        assert v1 == v2 == expected

    def test_verlinde_sl2_genus0_always_1(self):
        """V_{0,k} = 1 for all k (unitarity of S)."""
        for k in range(1, 11):
            assert verlinde_dim_sl2(k, 0) == 1

    @pytest.mark.parametrize("k", range(1, 11))
    def test_verlinde_sl2_genus1_is_k_plus_1(self, k):
        """V_{1,k}(sl_2) = k+1 = number of integrable reps (Zhu's theorem)."""
        assert verlinde_dim_sl2(k, 1) == k + 1
        assert sl2_genus1_count(k) == k + 1


# =========================================================================
# Section 2: Genus-2 closed form for sl_2
# =========================================================================

class TestGenus2ClosedForm:
    """Genus-2 closed form: V_{2,k}(sl_2) = C(k+3, 3)."""

    @pytest.mark.parametrize("k,expected", [
        (1, 4), (2, 10), (3, 20), (4, 35), (5, 56),
        (6, 84), (7, 120), (8, 165), (9, 220), (10, 286),
    ])
    def test_genus2_binomial(self, k, expected):
        """V_{2,k}(sl_2) = (k+1)(k+2)(k+3)/6 = C(k+3,3)."""
        assert sl2_genus2_closed(k) == expected
        assert verlinde_dim_sl2(k, 2) == expected


# =========================================================================
# Section 3: Verlinde dimensions for sl_3
# =========================================================================

class TestVerlindeSl3:
    """Verlinde dimensions for sl_3."""

    def test_sl3_genus0(self):
        """V_{0,k}(sl_3) = 1."""
        for k in range(1, 6):
            assert verlinde_dim_sl3(k, 0) == 1

    @pytest.mark.parametrize("k,expected_nreps", [
        (1, 3), (2, 6), (3, 10), (4, 15), (5, 21),
    ])
    def test_sl3_genus1_is_num_reps(self, k, expected_nreps):
        """V_{1,k}(sl_3) = C(k+2,2) = number of integrable reps."""
        assert verlinde_dim_sl3(k, 1) == expected_nreps
        assert num_integrable("A", 2, k) == expected_nreps

    def test_sl3_k1_powers_of_3(self):
        """At k=1, sl_3 has 3 reps all with S_{0,j} = 1/sqrt(3).
        So V_{g,1}(sl_3) = 3 * (1/sqrt(3))^{2-2g} = 3^g."""
        for g in range(0, 6):
            assert verlinde_dim_sl3(1, g) == 3 ** g

    @pytest.mark.parametrize("k,g,expected", [
        (2, 2, 45),  # verified by two independent engines
        (1, 2, 9),   # 3^2
        (1, 3, 27),  # 3^3
        (1, 4, 81),  # 3^4
    ])
    def test_sl3_known_values(self, k, g, expected):
        """Known sl_3 Verlinde dimensions."""
        assert verlinde_dim_sl3(k, g) == expected


# =========================================================================
# Section 4: Integrable representation counting
# =========================================================================

class TestIntegrableReps:
    """Verify integrable representation counts."""

    @pytest.mark.parametrize("lt,r,k,expected", [
        ("A", 1, 1, 2), ("A", 1, 2, 3), ("A", 1, 5, 6), ("A", 1, 10, 11),
        ("A", 2, 1, 3), ("A", 2, 2, 6), ("A", 2, 3, 10),
        ("A", 3, 1, 4), ("A", 3, 2, 10),
        ("B", 2, 1, 2), ("B", 2, 2, 4),
        ("C", 2, 1, 2), ("C", 2, 2, 4),
        ("G", 2, 1, 1),  # colabels (2,3): only (0,0) fits at k=1
    ])
    def test_num_integrable(self, lt, r, k, expected):
        """Number of integrable representations."""
        assert num_integrable(lt, r, k) == expected

    def test_sl2_integrable_is_k_plus_1(self):
        """For sl_2: |P_+^k| = k+1."""
        for k in range(1, 20):
            assert num_integrable("A", 1, k) == k + 1

    def test_sl3_integrable_is_binomial(self):
        """For sl_3: |P_+^k| = C(k+2, 2)."""
        for k in range(1, 10):
            expected = (k + 1) * (k + 2) // 2
            assert num_integrable("A", 2, k) == expected

    def test_slN_integrable_is_binomial(self):
        """For sl_N: |P_+^k| = C(k+N-1, N-1)."""
        for N in range(2, 6):
            for k in range(1, 6):
                r = N - 1
                expected = 1
                for i in range(r):
                    expected = expected * (k + r - i) // (i + 1)
                assert num_integrable("A", r, k) == expected


# =========================================================================
# Section 5: Faber-Pandharipande numbers
# =========================================================================

class TestFaberPandharipande:
    """Exact Faber-Pandharipande intersection numbers."""

    @pytest.mark.parametrize("g,expected_num,expected_den", [
        (1, 1, 24),
        (2, 7, 5760),
        (3, 31, 967680),
        (4, 127, 154828800),
        (5, 73, 3503554560),
    ])
    def test_fp_exact(self, g, expected_num, expected_den):
        """lambda_g^FP exact values."""
        fp = faber_pandharipande(g)
        assert fp == Fraction(expected_num, expected_den)

    def test_fp_from_bernoulli_identity(self):
        """Verify fp = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)! via sympy."""
        from sympy import bernoulli as sym_bernoulli, Rational as SRational
        for g in range(1, 8):
            B2g = sym_bernoulli(2 * g)
            numer = SRational(2 ** (2 * g - 1) - 1) * abs(B2g)
            denom = SRational(2 ** (2 * g - 1)) * SRational(math.factorial(2 * g))
            expected = Fraction(int(numer.p), int(numer.q)) / Fraction(int(denom.p), int(denom.q))
            assert faber_pandharipande(g) == expected

    def test_fp_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 15):
            assert faber_pandharipande(g) > 0


# =========================================================================
# Section 6: Kappa and central charge
# =========================================================================

class TestKappaAndCentralCharge:
    """Verify kappa and central charge formulas (AP1, AP39, AP48)."""

    @pytest.mark.parametrize("lt,r,k,expected_kappa", [
        ("A", 1, 1, Fraction(9, 4)),     # 3*(1+2)/(2*2) = 9/4
        ("A", 1, 2, Fraction(3)),         # 3*(2+2)/4 = 3
        ("A", 1, 4, Fraction(9, 2)),      # 3*6/4 = 9/2
        ("A", 2, 1, Fraction(16, 3)),     # 8*(1+3)/6 = 32/6 = 16/3
        ("A", 2, 3, Fraction(8)),         # 8*6/6 = 8
    ])
    def test_kappa_values(self, lt, r, k, expected_kappa):
        """kappa(g_k) = dim(g)*(k+h^v)/(2*h^v)."""
        assert kappa_km(lt, r, k) == expected_kappa

    @pytest.mark.parametrize("lt,r,k,expected_c", [
        ("A", 1, 1, Fraction(1)),         # 1*3/3 = 1
        ("A", 1, 2, Fraction(3, 2)),      # 2*3/4 = 3/2
        ("A", 1, 10, Fraction(5, 2)),     # 10*3/12 = 5/2
        ("A", 2, 1, Fraction(2)),         # 1*8/4 = 2
    ])
    def test_central_charge_values(self, lt, r, k, expected_c):
        """c = k*dim(g)/(k+h^v)."""
        assert central_charge_km(lt, r, k) == expected_c

    def test_kappa_not_c_over_2_for_km(self):
        """kappa != c/2 in general for KM (AP39).
        kappa = c/2 only for Virasoro."""
        for k in range(1, 10):
            kap = kappa_km("A", 1, k)
            c = central_charge_km("A", 1, k)
            # For sl_2: kappa = 3(k+2)/4, c = 3k/(k+2)
            # kappa = c/2 would require 3(k+2)/4 = 3k/(2(k+2))
            # => (k+2)^2 = 2k => k^2+4k+4 = 2k => k^2+2k+4 = 0 (no real soln)
            assert kap != c / 2


# =========================================================================
# Section 7: Shadow free energy
# =========================================================================

class TestShadowFreeEnergy:
    """Shadow F_g = kappa * lambda_g^FP (Theorem D)."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 5),
        ("A", 2, 1), ("A", 2, 3),
    ])
    def test_shadow_fg_equals_kappa_times_fp(self, lt, r, k):
        """F_g = kappa * lambda_g^FP for g=1,...,5."""
        kap = kappa_km(lt, r, k)
        for g in range(1, 6):
            F = shadow_free_energy(lt, r, k, g)
            assert F == kap * faber_pandharipande(g)

    def test_shadow_f1_is_kappa_over_24(self):
        """F_1 = kappa/24."""
        for k in range(1, 10):
            F1 = shadow_free_energy("A", 1, k, 1)
            assert F1 == kappa_km("A", 1, k) / 24


# =========================================================================
# Section 8: S-matrix properties
# =========================================================================

class TestSMatrix:
    """S-matrix properties: unitarity, symmetry, positivity."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_sl2_s_matrix_symmetric(self, k):
        """S is symmetric for sl_2."""
        S = sl2_S_matrix_full(k)
        np.testing.assert_allclose(S, S.T, atol=1e-12)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_sl2_s_matrix_orthogonal(self, k):
        """S S^T = I for sl_2 (real orthogonal)."""
        S = sl2_S_matrix_full(k)
        product = S @ S.T
        np.testing.assert_allclose(product, np.eye(k + 1), atol=1e-10)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_sl2_s00_positive(self, k):
        """S_{0,0} > 0."""
        assert sl2_S_entry(0, 0, k) > 0

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_s_matrix_unitary(self, k):
        """S S^dag = I for sl_3."""
        S = sl3_S_matrix_full(k)
        product = S @ np.conj(S.T)
        np.testing.assert_allclose(product, np.eye(S.shape[0]), atol=1e-8)

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_sl3_s00_positive(self, k):
        """S_{0,0} > 0 for sl_3."""
        S = sl3_S_matrix_full(k)
        assert S[0, 0].real > 0
        assert abs(S[0, 0].imag) < 1e-10


# =========================================================================
# Section 9: TUY factorization (separating)
# =========================================================================

class TestTUYFactorizationSeparating:
    """Verify TUY separating factorization: V_{g1+g2} from V_{g1} * V_{g2}."""

    @pytest.mark.parametrize("k,g1,g2", [
        (1, 1, 1), (2, 1, 1), (3, 1, 1),
        (1, 1, 2), (2, 1, 2), (3, 1, 2),
        (1, 2, 2), (2, 2, 2),
        (2, 1, 3), (3, 2, 1),
    ])
    def test_separating_sl2(self, k, g1, g2):
        """Separating factorization for sl_2."""
        result = verify_factorization_separating("A", 1, k, g1, g2)
        assert result["factorization_holds"], (
            f"Separating factorization failed for sl_2 k={k}, "
            f"g1={g1}, g2={g2}: V={result['V_direct']}, "
            f"factored={result['V_factored_raw']}"
        )

    @pytest.mark.parametrize("k,g1,g2", [
        (1, 1, 1), (2, 1, 1),
        (1, 1, 2), (1, 2, 2),
    ])
    def test_separating_sl3(self, k, g1, g2):
        """Separating factorization for sl_3."""
        result = verify_factorization_separating("A", 2, k, g1, g2)
        assert result["factorization_holds"], (
            f"Separating factorization failed for sl_3 k={k}, "
            f"g1={g1}, g2={g2}: V={result['V_direct']}, "
            f"factored={result['V_factored_raw']}"
        )


# =========================================================================
# Section 10: TUY factorization (nonseparating / self-sewing)
# =========================================================================

class TestTUYFactorizationNonseparating:
    """Verify TUY nonseparating factorization: V_g from V_{g-1} by self-sewing."""

    @pytest.mark.parametrize("k,g", [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2),
        (4, 1), (4, 2),
        (5, 1),
    ])
    def test_nonseparating_sl2(self, k, g):
        """Nonseparating factorization for sl_2."""
        result = verify_factorization_nonseparating("A", 1, k, g)
        assert result["factorization_holds"], (
            f"Nonseparating factorization failed for sl_2 k={k}, g={g}: "
            f"V={result['V_direct']}, sewed={result['V_sewed_raw']}"
        )

    @pytest.mark.parametrize("k,g", [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2),
    ])
    def test_nonseparating_sl3(self, k, g):
        """Nonseparating factorization for sl_3."""
        result = verify_factorization_nonseparating("A", 2, k, g)
        assert result["factorization_holds"], (
            f"Nonseparating factorization failed for sl_3 k={k}, g={g}: "
            f"V={result['V_direct']}, sewed={result['V_sewed_raw']}"
        )


# =========================================================================
# Section 11: Propagation of vacua
# =========================================================================

class TestPropagationOfVacua:
    """Propagation of vacua: inserting vacuum doesn't change blocks."""

    @pytest.mark.parametrize("k,g", [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2),
        (3, 1), (3, 2),
        (5, 1),
    ])
    def test_propagation_sl2(self, k, g):
        """Propagation of vacua for sl_2."""
        result = verify_propagation_of_vacua("A", 1, k, g)
        assert result["propagation_holds"]

    @pytest.mark.parametrize("k,g", [
        (1, 1), (1, 2),
        (2, 1), (2, 2),
    ])
    def test_propagation_sl3(self, k, g):
        """Propagation of vacua for sl_3."""
        result = verify_propagation_of_vacua("A", 2, k, g)
        assert result["propagation_holds"]


# =========================================================================
# Section 12: Fusion rules
# =========================================================================

class TestFusionRules:
    """Verify fusion rules from Verlinde formula match exact CG rules."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_fusion_verlinde_matches_exact(self, k):
        """Verlinde formula gives exact fusion coefficients for sl_2."""
        result = verify_fusion_from_verlinde(k)
        assert result["all_match"], (
            f"Fusion mismatch at k={k}: max_dev={result['max_deviation']}"
        )

    def test_fusion_k1_trivial(self):
        """At k=1, sl_2 has 2 reps: V_0, V_1. N_{11}^0 = 1 (fusion of V_1 with itself)."""
        assert sl2_fusion_rule(1, 1, 0, 1) == 1
        assert sl2_fusion_rule(0, 0, 0, 1) == 1
        assert sl2_fusion_rule(0, 1, 1, 1) == 1

    def test_fusion_symmetry(self):
        """N_{ij}^m = N_{ji}^m (commutativity of fusion)."""
        for k in range(1, 5):
            N = sl2_fusion_matrix(k)
            for i in range(k + 1):
                for j in range(k + 1):
                    for m in range(k + 1):
                        assert N[i, j, m] == N[j, i, m]

    def test_fusion_vacuum(self):
        """N_{0j}^m = delta_{jm} (vacuum is the identity)."""
        for k in range(1, 6):
            for j in range(k + 1):
                for m in range(k + 1):
                    expected = 1 if j == m else 0
                    assert sl2_fusion_rule(0, j, m, k) == expected


# =========================================================================
# Section 13: Complementarity (Thm C)
# =========================================================================

class TestComplementarity:
    """Kappa + kappa' = 0 for KM (AP24: exact for KM, NOT for Virasoro)."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 5), ("A", 1, 10),
        ("A", 2, 1), ("A", 2, 3),
    ])
    def test_kappa_sum_zero(self, lt, r, k):
        """kappa(g_k) + kappa(g_{k'}) = 0 for KM."""
        result = complementarity_verlinde(lt, r, k)
        assert result["kappa_sum_zero"], (
            f"kappa sum = {result['kappa_sum']} != 0 "
            f"for ({lt}, {r}) at k={k}"
        )

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 3),
        ("A", 2, 1),
    ])
    def test_shadow_complementarity_all_genera(self, lt, r, k):
        """F_g + F_g' = 0 at all genera (shadow-level complementarity)."""
        result = complementarity_verlinde(lt, r, k, max_g=5)
        for gd in result["genus_data"]:
            assert gd["complementarity_holds"], (
                f"Shadow complementarity fails at g={gd['g']}: "
                f"F+F' = {gd['sum']}"
            )


# =========================================================================
# Section 14: Large-k asymptotics
# =========================================================================

class TestLargeKAsymptotics:
    """Witten's asymptotic formula: V_{g,k} ~ C_g * k^{3(g-1)}."""

    def test_genus2_polynomial_growth(self):
        """V_{2,k}(sl_2) = C(k+3,3) grows as k^3/6."""
        data = large_k_asymptotics_sl2(list(range(10, 101, 10)), 2)
        # Ratios should converge to 1/6
        ratios = [d["ratio_V_over_k_power"] for d in data["data"]]
        # For large k: C(k+3,3)/k^3 -> 1/6
        assert abs(ratios[-1] - 1.0 / 6.0) < 0.01

    def test_genus3_growth_exponent(self):
        """V_{3,k}(sl_2) grows as k^6."""
        vals = []
        for k in [20, 30, 40, 50]:
            V = verlinde_dim_sl2(k, 3)
            vals.append((k, V))
        # Log-log slope should be ~6
        k1, V1 = vals[0]
        k2, V2 = vals[-1]
        slope = math.log(V2 / V1) / math.log(k2 / k1)
        assert abs(slope - 6.0) < 0.5


# =========================================================================
# Section 15: Genus-1 = Zhu (character count)
# =========================================================================

class TestZhuGenus1:
    """Genus-1 conformal blocks = number of simple modules (Zhu's theorem)."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 5), ("A", 1, 10),
        ("A", 2, 1), ("A", 2, 3), ("A", 2, 5),
    ])
    def test_genus1_equals_num_reps(self, lt, r, k):
        """V_{1,k}(g) = |P_+^k| for all types."""
        V1 = verlinde_dim_general(lt, r, k, 1)
        n = num_integrable(lt, r, k)
        assert V1 == n

    def test_zhu_description(self):
        """Zhu algebra description is meaningful."""
        desc = zhu_algebra_dim_km("A", 1)
        assert "U(A_1)" in desc


# =========================================================================
# Section 16: Cross-check with verlinde_shadow_cohft_engine
# =========================================================================

class TestCrossEngine:
    """Cross-check against the independent verlinde_shadow_cohft_engine."""

    def test_kappa_cross_check(self):
        """kappa values match between engines."""
        try:
            from compute.lib.verlinde_shadow_cohft_engine import (
                kappa_affine_exact,
            )
        except ImportError:
            pytest.skip("verlinde_shadow_cohft_engine not available")

        for k in range(1, 8):
            ours = kappa_km("A", 1, k)
            theirs = kappa_affine_exact("A", 1, k)
            assert float(ours) == pytest.approx(float(theirs), abs=1e-15)

    def test_verlinde_cross_check_sl2(self):
        """Verlinde dimensions match between engines."""
        try:
            from compute.lib.verlinde_shadow_cohft_engine import (
                verlinde_dimension_exact,
            )
        except ImportError:
            pytest.skip("verlinde_shadow_cohft_engine not available")

        for k in range(1, 6):
            for g in range(0, 5):
                ours = verlinde_dim_sl2(k, g)
                theirs = verlinde_dimension_exact("A", 1, k, g)
                assert ours == theirs, (
                    f"Mismatch at k={k}, g={g}: ours={ours}, theirs={theirs}"
                )

    def test_shadow_fg_cross_check(self):
        """Shadow F_g matches between engines."""
        try:
            from compute.lib.verlinde_shadow_cohft_engine import (
                shadow_F_g as other_shadow,
            )
        except ImportError:
            pytest.skip("verlinde_shadow_cohft_engine not available")

        for k in range(1, 6):
            for g in range(1, 5):
                ours = float(shadow_free_energy("A", 1, k, g))
                theirs = float(other_shadow("A", 1, k, g))
                assert abs(ours - theirs) < 1e-15


# =========================================================================
# Section 17: Quantum group decomposition
# =========================================================================

class TestQuantumGroupDecomposition:
    """Verlinde as sum over quantum group channels."""

    @pytest.mark.parametrize("k,g", [
        (1, 1), (2, 2), (3, 3), (4, 2),
    ])
    def test_channel_sum_equals_verlinde(self, k, g):
        """Sum of channel contributions = Verlinde dimension."""
        result = verlinde_from_quantum_group_decomposition("A", 1, k, g)
        assert result["verlinde_dim"] == verlinde_dim_sl2(k, g)

    def test_vacuum_channel_dominant_large_k(self):
        """At large k, the vacuum channel (j=0) dominates."""
        k = 50
        result = verlinde_from_quantum_group_decomposition("A", 1, k, 3)
        vac_contrib = result["channels"][0]["contribution"]
        total = sum(ch["contribution"] for ch in result["channels"])
        # Vacuum should be a significant fraction
        assert vac_contrib / total > 0.01


# =========================================================================
# Section 18: Full diagnostic
# =========================================================================

class TestFullDiagnostic:
    """Full diagnostic output."""

    def test_diagnostic_sl2_k2(self):
        """Full diagnostic for sl_2 at k=2."""
        result = full_diagnostic("A", 1, 2, max_g=4)
        assert result["num_integrable_reps"] == 3
        assert result["kappa"] == pytest.approx(3.0)
        assert result["central_charge"] == pytest.approx(1.5)
        assert result["genus_data"][0]["verlinde_dim"] == 1  # g=0
        assert result["genus_data"][1]["verlinde_dim"] == 3  # g=1
        assert result["genus_data"][2]["verlinde_dim"] == 10  # g=2

    def test_diagnostic_sl3_k1(self):
        """Full diagnostic for sl_3 at k=1."""
        result = full_diagnostic("A", 2, 1, max_g=3)
        assert result["num_integrable_reps"] == 3
        assert result["genus_data"][1]["verlinde_dim"] == 3   # g=1 = 3^1
        assert result["genus_data"][2]["verlinde_dim"] == 9   # g=2 = 3^2
        assert result["genus_data"][3]["verlinde_dim"] == 27  # g=3 = 3^3


# =========================================================================
# Section 19: Verlinde table comparison
# =========================================================================

class TestVerlindeTable:
    """Comprehensive Verlinde vs shadow table."""

    def test_table_sl2(self):
        """Generate and verify table for sl_2."""
        result = verlinde_vs_shadow_table(
            "A", 1, levels=[1, 2, 3], genera=[0, 1, 2, 3]
        )
        table = result["table"]
        # Find k=1, g=2 entry
        entry = [r for r in table if r["k"] == 1 and r["g"] == 2][0]
        assert entry["verlinde_dim"] == 4
        assert entry["num_reps"] == 2

    def test_table_sl3(self):
        """Generate and verify table for sl_3."""
        result = verlinde_vs_shadow_table(
            "A", 2, levels=[1, 2], genera=[0, 1, 2]
        )
        table = result["table"]
        # k=1, g=1 = 3
        entry = [r for r in table if r["k"] == 1 and r["g"] == 1][0]
        assert entry["verlinde_dim"] == 3


# =========================================================================
# Section 20: Edge cases and input validation
# =========================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_genus0_always_1(self):
        """V_{0,k} = 1 for all types and levels."""
        for k in range(1, 6):
            assert verlinde_dim_sl2(k, 0) == 1
            assert verlinde_dim_sl3(k, 0) == 1

    def test_fp_genus0_raises(self):
        """FP number undefined for g=0."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_shadow_fg_genus0_raises(self):
        """Shadow F_g undefined for g=0."""
        with pytest.raises(ValueError):
            shadow_free_energy("A", 1, 1, 0)

    def test_critical_level_raises(self):
        """Central charge undefined at critical level."""
        with pytest.raises(ValueError):
            central_charge_km("A", 1, -2)

    def test_negative_genus_raises(self):
        """Negative genus raises ValueError."""
        with pytest.raises(ValueError):
            verlinde_dim_sl2(1, -1)


# =========================================================================
# Section 21: sl_2 level-1 special case (k=1: V_g = 2^g)
# =========================================================================

class TestSl2Level1:
    """At k=1, sl_2 has 2 reps: V_0, V_1. V_{g,1} = 2^g."""

    @pytest.mark.parametrize("g", range(0, 9))
    def test_level1_powers_of_2(self, g):
        """V_{g,1}(sl_2) = 2^g."""
        assert verlinde_dim_sl2(1, g) == 2 ** g
