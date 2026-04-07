"""
Cross-engine kappa verification tests.

This is the manuscript's immune system for the most error-prone quantity
in the project (AP1: 19 correction commits historically).

Tests verify:
  1. Canonical formulas are internally consistent
  2. Every engine that computes kappa agrees with the canonical value
  3. AP39 compliance: kappa != c/2 for affine KM at rank > 1
  4. AP48 compliance: kappa depends on full algebra, not Virasoro sub
  5. AP24 compliance: complementarity sums are correct
  6. Cross-family consistency: no formula copied between families
  7. Numerical evaluation at specific parameter values

Multi-path verification:
  Path 1: direct formula evaluation
  Path 2: consistency across engines
  Path 3: complementarity sum checks
  Path 4: genus-1 cross-check F_1 = kappa/24
  Path 5: limiting cases (k -> 0, c -> 0, N -> 2)
"""

import pytest
from fractions import Fraction

from compute.lib.rectification_kappa_cross_engine import (
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_slN,
    kappa_affine_general,
    kappa_wN,
    kappa_betagamma,
    kappa_lattice,
    kappa_free_fermion,
    kappa_bc_ghost,
    complementarity_heisenberg,
    complementarity_virasoro,
    complementarity_affine_slN,
    KNOWN_KAPPA_ERRORS,
)


# ============================================================================
# 1. CANONICAL FORMULA TESTS — verify each formula at multiple values
# ============================================================================

class TestCanonicalHeisenberg:
    """kappa(H_k) = k.  AP39: NOT k/2."""

    def test_k1(self):
        assert kappa_heisenberg(1) == Fraction(1)

    def test_k2(self):
        assert kappa_heisenberg(2) == Fraction(2)

    def test_k_half(self):
        assert kappa_heisenberg(Fraction(1, 2)) == Fraction(1, 2)

    def test_k_minus1(self):
        assert kappa_heisenberg(-1) == Fraction(-1)

    def test_not_k_over_2(self):
        """AP39: kappa(H_k) = k, NOT k/2."""
        for k in [1, 2, 3, 5, 10]:
            assert kappa_heisenberg(k) != Fraction(k, 2), \
                f"kappa(H_{k}) should be {k}, not {k}/2"

    def test_additivity(self):
        """kappa(H_{k1} + H_{k2}) = k1 + k2."""
        assert kappa_heisenberg(3) + kappa_heisenberg(5) == kappa_heisenberg(8)

    def test_genus1_crosscheck(self):
        """F_1 = kappa/24.  For H_1: F_1 = 1/24."""
        assert kappa_heisenberg(1) / 24 == Fraction(1, 24)


class TestCanonicalVirasoro:
    """kappa(Vir_c) = c/2."""

    def test_c1(self):
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_c13(self):
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_c26(self):
        assert kappa_virasoro(26) == Fraction(13)

    def test_c0(self):
        assert kappa_virasoro(0) == Fraction(0)

    def test_c_minus2(self):
        assert kappa_virasoro(-2) == Fraction(-1)

    def test_genus1_crosscheck(self):
        """F_1(Vir_c) = (c/2)/24 = c/48."""
        for c in [1, 2, 13, 26]:
            assert kappa_virasoro(c) / 24 == Fraction(c, 48)


class TestCanonicalAffineKM:
    """kappa(sl_N, k) = (N^2-1)*(k+N)/(2N).  AP39: NOT c/2."""

    def test_sl2_k1(self):
        assert kappa_affine_slN(2, 1) == Fraction(9, 4)

    def test_sl2_k2(self):
        assert kappa_affine_slN(2, 2) == Fraction(3)

    def test_sl2_k5(self):
        assert kappa_affine_slN(2, 5) == Fraction(21, 4)

    def test_sl3_k1(self):
        # dim(sl_3) = 8, h_v = 3, kappa = 8*(1+3)/(2*3) = 32/6 = 16/3
        assert kappa_affine_slN(3, 1) == Fraction(16, 3)

    def test_sl3_k2(self):
        assert kappa_affine_slN(3, 2) == Fraction(8 * 5, 6)  # = 40/6 = 20/3

    def test_not_c_over_2(self):
        """AP39: kappa(sl_N, k) != c/2 for N >= 2."""
        for N in [2, 3, 4]:
            for k in [1, 2, 3]:
                dim_g = N * N - 1
                h_v = N
                c = Fraction(k * dim_g, k + h_v)
                c_half = c / 2
                kap = kappa_affine_slN(N, k)
                assert kap != c_half, \
                    f"kappa(sl_{N}, k={k}) = {kap} should NOT equal c/2 = {c_half}"

    def test_sl2_explicit_formula(self):
        """3*(k+2)/4 for sl_2."""
        for k in [1, 2, 3, 5, 10]:
            expected = Fraction(3) * (k + 2) / 4
            assert kappa_affine_slN(2, k) == expected

    def test_sl3_explicit_formula(self):
        """8*(k+3)/6 = 4*(k+3)/3 for sl_3."""
        for k in [1, 2, 3]:
            expected = Fraction(4) * (k + 3) / 3
            assert kappa_affine_slN(3, k) == expected

    def test_general_formula(self):
        """dim(g)*(k+h^v)/(2h^v)."""
        # G_2: dim = 14, h_v = 4
        assert kappa_affine_general(14, 4, 1) == Fraction(14 * 5, 8)
        # F_4: dim = 52, h_v = 9
        assert kappa_affine_general(52, 9, 1) == Fraction(52 * 10, 18)
        # E_8: dim = 248, h_v = 30
        assert kappa_affine_general(248, 30, 1) == Fraction(248 * 31, 60)


class TestCanonicalWN:
    """kappa(W_N) = c*(H_N - 1)."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: kappa = c*(H_2-1) = c*(3/2-1) = c/2."""
        for c in [1, 2, 13, 26]:
            assert kappa_wN(2, c) == kappa_virasoro(c), \
                f"W_2 at c={c} should equal Virasoro"

    def test_w3(self):
        """kappa(W_3) = 5c/6.  H_3 = 1+1/2+1/3 = 11/6, H_3-1 = 5/6."""
        for c in [1, 2, 6, 100]:
            expected = Fraction(5) * c / 6
            assert kappa_wN(3, c) == expected, \
                f"kappa(W_3, c={c}) = {kappa_wN(3,c)}, expected {expected}"

    def test_w3_not_c_over_2(self):
        """AP1: kappa(W_3) = 5c/6, NOT c/2."""
        for c in [1, 2, 6, 100]:
            assert kappa_wN(3, c) != kappa_virasoro(c), \
                f"W_3 kappa should NOT equal c/2 at c={c}"

    def test_w4(self):
        """kappa(W_4) = 13c/12.  H_4 = 25/12, H_4-1 = 13/12."""
        for c in [1, 12, 24]:
            expected = Fraction(13) * c / 12
            assert kappa_wN(4, c) == expected

    def test_w5(self):
        """H_5 = 137/60, H_5-1 = 77/60."""
        expected = Fraction(77) * 1 / 60
        assert kappa_wN(5, 1) == expected

    def test_harmonic_number_consistency(self):
        """H_N - 1 = 1/2 + 1/3 + ... + 1/N."""
        for N in range(2, 8):
            H_N = sum(Fraction(1, j) for j in range(1, N + 1))
            sigma = H_N - 1
            assert kappa_wN(N, 1) == sigma


class TestCanonicalOther:
    """Tests for betagamma, lattice, free fermion, bc ghost."""

    def test_betagamma(self):
        assert kappa_betagamma() == Fraction(-1)

    def test_betagamma_is_c_over_2(self):
        """betagamma: c = -2, kappa = c/2 = -1."""
        assert kappa_betagamma() == Fraction(-2) / 2

    def test_lattice_e8(self):
        """kappa(V_{E_8}) = rank = 8, NOT c/2 = 12 (AP48)."""
        assert kappa_lattice(8) == 8
        assert kappa_lattice(8) != 4  # NOT rank/2

    def test_lattice_leech(self):
        """kappa(V_Leech) = 24, NOT 12."""
        assert kappa_lattice(24) == 24
        assert kappa_lattice(24) != 12  # NOT rank/2

    def test_lattice_d16(self):
        assert kappa_lattice(16) == 16

    def test_lattice_not_c_over_2(self):
        """AP48: for lattice VOA at c = rank, kappa = rank, NOT c/2 = rank/2."""
        for rank in [1, 8, 16, 24]:
            assert kappa_lattice(rank) != rank // 2 or rank == 1, \
                f"Lattice rank={rank}: kappa should be {rank}, not {rank//2}"

    def test_free_fermion(self):
        assert kappa_free_fermion() == Fraction(1, 4)

    def test_bc_ghost(self):
        assert kappa_bc_ghost() == Fraction(-13)


# ============================================================================
# 2. COMPLEMENTARITY TESTS — AP24
# ============================================================================

class TestComplementarity:
    """Verify complementarity sums."""

    def test_heisenberg_sum_zero(self):
        """kappa(H_k) + kappa(H_{-k}) = 0 for all k."""
        for k in [1, 2, 3, 5, Fraction(1, 2)]:
            assert complementarity_heisenberg(k) == 0

    def test_virasoro_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c.  AP24: NOT 0."""
        for c in [0, 1, 2, 13, 25, 26]:
            assert complementarity_virasoro(c) == 13

    def test_virasoro_sum_not_zero(self):
        """AP24: Virasoro complementarity sum is 13, NOT 0."""
        assert complementarity_virasoro(1) != 0

    def test_affine_sl2_sum_zero(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0."""
        for k in [1, 2, 3, 5]:
            assert complementarity_affine_slN(2, k) == 0

    def test_affine_sl3_sum_zero(self):
        """kappa(sl_3, k) + kappa(sl_3, -k-6) = 0."""
        for k in [1, 2, 3]:
            assert complementarity_affine_slN(3, k) == 0

    def test_w3_complementarity(self):
        """kappa(W_3, c) + kappa(W_3, 100-c) = 250/3."""
        for c in [1, 2, 50, 99]:
            total = kappa_wN(3, c) + kappa_wN(3, 100 - c)
            assert total == Fraction(250, 3), \
                f"W_3 complementarity at c={c}: {total} != 250/3"

    def test_betagamma_sum_zero(self):
        """kappa(bg) + kappa(bg!) = 0. bg! has c = 2, kappa = 1."""
        assert kappa_betagamma() + Fraction(1) == 0


# ============================================================================
# 3. CROSS-ENGINE CONSISTENCY — verify every engine agrees
# ============================================================================

class TestCrossEngineGrandSynthesis:
    """Verify grand_synthesis_engine canonical functions."""

    def test_heisenberg(self):
        from compute.lib.grand_synthesis_engine import kappa_heisenberg as gs
        for k in [1, 2, 5]:
            assert gs(k) == kappa_heisenberg(k)

    def test_virasoro(self):
        from compute.lib.grand_synthesis_engine import kappa_virasoro as gs
        for c in [1, 13, 26]:
            assert gs(c) == kappa_virasoro(c)

    def test_affine_sl2(self):
        from compute.lib.grand_synthesis_engine import kappa_affine_slN as gs
        for k in [1, 2, 5]:
            assert gs(2, k) == kappa_affine_slN(2, k)

    def test_affine_sl3(self):
        from compute.lib.grand_synthesis_engine import kappa_affine_slN as gs
        for k in [1, 2]:
            assert gs(3, k) == kappa_affine_slN(3, k)

    def test_w3(self):
        from compute.lib.grand_synthesis_engine import kappa_w3 as gs
        for c in [1, 2, 6]:
            assert gs(c) == kappa_wN(3, c)

    def test_wN(self):
        from compute.lib.grand_synthesis_engine import kappa_wN as gs
        for N in [2, 3, 4, 5]:
            assert gs(1, N) == kappa_wN(N, 1)

    def test_betagamma(self):
        from compute.lib.grand_synthesis_engine import kappa_betagamma as gs
        assert gs() == kappa_betagamma()

    def test_lattice(self):
        from compute.lib.grand_synthesis_engine import kappa_lattice as gs
        for r in [8, 16, 24]:
            assert gs(r) == kappa_lattice(r)


class TestCrossEngineDerivedCenter:
    """Verify derived_center_explicit kappa function."""

    def test_heisenberg(self):
        from compute.lib.derived_center_explicit import kappa as dc
        for k in [1, 2, 5]:
            assert dc('Heisenberg', k=k) == kappa_heisenberg(k)

    def test_virasoro(self):
        from compute.lib.derived_center_explicit import kappa as dc
        for c in [1, 13, 26]:
            assert dc('Virasoro', c=c) == kappa_virasoro(c)

    def test_affine_sl2(self):
        from compute.lib.derived_center_explicit import kappa as dc
        for k in [1, 2, 5]:
            assert dc('Affine_sl2', k=k) == kappa_affine_slN(2, k)

    def test_w3(self):
        from compute.lib.derived_center_explicit import kappa as dc
        for c in [1, 2, 6]:
            assert dc('W3', c=c) == kappa_wN(3, c)


class TestCrossEngineLatticeModel:
    """Verify lattice_model_shadow_engine kappa computation."""

    def test_heisenberg(self):
        from compute.lib.lattice_model_shadow_engine import ShadowLatticeDictionary
        d = ShadowLatticeDictionary(algebra='heisenberg', level=1.0)
        assert abs(d.kappa() - float(kappa_heisenberg(1))) < 1e-10

    def test_heisenberg_k5(self):
        from compute.lib.lattice_model_shadow_engine import ShadowLatticeDictionary
        d = ShadowLatticeDictionary(algebra='heisenberg', level=5.0)
        assert abs(d.kappa() - float(kappa_heisenberg(5))) < 1e-10

    def test_virasoro(self):
        from compute.lib.lattice_model_shadow_engine import ShadowLatticeDictionary
        d = ShadowLatticeDictionary(algebra='virasoro', level=26.0)
        assert abs(d.kappa() - float(kappa_virasoro(26))) < 1e-10

    def test_sl2(self):
        from compute.lib.lattice_model_shadow_engine import ShadowLatticeDictionary
        for k in [1, 2, 5]:
            d = ShadowLatticeDictionary(algebra='sl2', level=float(k))
            assert abs(d.kappa() - float(kappa_affine_slN(2, k))) < 1e-10, \
                f"lattice_model sl2 k={k}: {d.kappa()} != {float(kappa_affine_slN(2, k))}"

    def test_sl3(self):
        from compute.lib.lattice_model_shadow_engine import ShadowLatticeDictionary
        d = ShadowLatticeDictionary(algebra='sl3', level=1.0)
        assert abs(d.kappa() - float(kappa_affine_slN(3, 1))) < 1e-10


class TestCrossEngineKoszulEpstein:
    """Test koszul_epstein shadow data — FIXED."""

    def test_heisenberg_against_canonical(self):
        from compute.lib.koszul_epstein import shadow_data
        data = shadow_data('heisenberg', k=1)
        assert abs(data['kappa'] - float(kappa_heisenberg(1))) < 1e-10

    def test_w3_against_canonical(self):
        from compute.lib.koszul_epstein import shadow_data
        data = shadow_data('w3', c=6.0)
        assert abs(data['kappa'] - float(kappa_wN(3, 6))) < 1e-10

    def test_affine_sl2_against_canonical(self):
        from compute.lib.koszul_epstein import shadow_data
        data = shadow_data('affine_km', N=2, k=1)
        assert abs(data['kappa'] - float(kappa_affine_slN(2, 1))) < 1e-10

    def test_heisenberg_exact_against_canonical(self):
        from compute.lib.koszul_epstein import shadow_data_exact
        data = shadow_data_exact('heisenberg', k=Fraction(1))
        assert data['kappa'] == kappa_heisenberg(1)


class TestCrossEngineKoszulEpsteinMomentMatrix:
    """Test koszul_epstein_moment_matrix — FIXED."""

    def test_heisenberg_against_canonical(self):
        from compute.lib.koszul_epstein_moment_matrix import heisenberg_shadow_data
        kap, alpha, s4 = heisenberg_shadow_data(k=Fraction(1))
        assert kap == kappa_heisenberg(1)


class TestCrossEngineEnFactorization:
    """Test en_factorization_shadow — FIXED."""

    def test_kappa_en_free_heisenberg(self):
        from compute.lib.en_factorization_shadow import kappa_en_free
        assert kappa_en_free(1, Fraction(1)) == kappa_heisenberg(1)

    def test_swiss_cheese_heisenberg(self):
        from compute.lib.en_factorization_shadow import swiss_cheese_shadow_heisenberg
        data = swiss_cheese_shadow_heisenberg(Fraction(1))
        assert data['kappa_total'] == kappa_heisenberg(1)

    def test_kappa_en_affine_correct(self):
        """The affine version should be correct."""
        from compute.lib.en_factorization_shadow import kappa_en_affine
        assert kappa_en_affine(1, 3, Fraction(1), 2) == kappa_affine_slN(2, 1)

    def test_kappa_en_virasoro_correct(self):
        from compute.lib.en_factorization_shadow import kappa_en_virasoro
        assert kappa_en_virasoro(1, Fraction(26)) == kappa_virasoro(26)


class TestCrossEngineE3:
    """Test e3_bar_cobar_engine — FIXED."""

    def test_heisenberg(self):
        from compute.lib.e3_bar_cobar_engine import e3_bar_heisenberg
        data = e3_bar_heisenberg(level=1)
        assert abs(data['kappa'] - float(kappa_heisenberg(1))) < 1e-10


class TestCrossEngineArithmeticComparison:
    """Test arithmetic_comparison_test — fixed from rank/2 to rank."""

    def test_e8_kappa(self):
        from compute.lib.arithmetic_comparison_test import extract_arithmetic_from_mc_e8
        data = extract_arithmetic_from_mc_e8()
        assert abs(data['kappa'] - float(kappa_lattice(8))) < 1e-10


# ============================================================================
# 4. AP39 COMPLIANCE — kappa != c/2 for non-Virasoro
# ============================================================================

class TestAP39:
    """AP39: kappa != c/2 for families other than Virasoro (and bg)."""

    def test_heisenberg_not_c_over_2(self):
        """Heisenberg: c = k, but kappa = k != k/2 = c/2."""
        for k in [1, 2, 3, 5]:
            c = k  # c(H_k) = k for rank-1
            assert kappa_heisenberg(k) != Fraction(c, 2)

    def test_sl2_not_c_over_2(self):
        """sl_2: c = 3k/(k+2), kappa = 3(k+2)/4 != c/2."""
        for k in [1, 2, 3, 5]:
            dim_g, h_v = 3, 2
            c = Fraction(k * dim_g, k + h_v)
            assert kappa_affine_slN(2, k) != c / 2

    def test_sl3_not_c_over_2(self):
        for k in [1, 2]:
            dim_g, h_v = 8, 3
            c = Fraction(k * dim_g, k + h_v)
            assert kappa_affine_slN(3, k) != c / 2

    def test_w3_not_c_over_2(self):
        for c in [1, 2, 6]:
            assert kappa_wN(3, c) != Fraction(c, 2)

    def test_w4_not_c_over_2(self):
        for c in [1, 12]:
            assert kappa_wN(4, c) != Fraction(c, 2)

    def test_lattice_not_c_over_2(self):
        """Lattice: c = rank, kappa = rank, NOT rank/2 = c/2."""
        for rank in [8, 16, 24]:
            assert kappa_lattice(rank) != rank // 2


# ============================================================================
# 5. AP48 COMPLIANCE — kappa depends on full algebra
# ============================================================================

class TestAP48:
    """AP48: kappa depends on the full algebra, not the Virasoro subalgebra."""

    def test_moonshine_not_c_over_2(self):
        """V^nat has c=24 but kappa=12 (Virasoro formula),
        while Niemeier lattice VOAs have c=24 but kappa=24 (lattice formula).
        These are DIFFERENT."""
        kappa_moonshine_vir = kappa_virasoro(24)  # = 12
        kappa_niemeier_lattice = kappa_lattice(24)  # = 24
        assert kappa_moonshine_vir != kappa_niemeier_lattice

    def test_e8_lattice_vs_virasoro(self):
        """E_8 lattice VOA: c=8, kappa=8.  Virasoro at c=8: kappa=4."""
        assert kappa_lattice(8) == 8
        assert kappa_virasoro(8) == 4
        assert kappa_lattice(8) != kappa_virasoro(8)

    def test_affine_e8_vs_virasoro(self):
        """Affine E_8 at k=1: c=8, kappa=248*31/60.  Not c/2=4."""
        kap = kappa_affine_general(248, 30, 1)
        assert kap != kappa_virasoro(8)


# ============================================================================
# 6. LIMITING CASES — boundary behavior
# ============================================================================

class TestLimitingCases:
    """Verify kappa at special/limiting parameter values."""

    def test_virasoro_at_c0(self):
        assert kappa_virasoro(0) == 0

    def test_heisenberg_at_k0(self):
        assert kappa_heisenberg(0) == 0

    def test_sl2_at_k0(self):
        """At k=0: kappa = 3*2/4 = 3/2."""
        assert kappa_affine_slN(2, 0) == Fraction(3, 2)

    def test_sl2_at_critical(self):
        """At k = -h^v = -2: kappa = 3*0/4 = 0.  Sugawara undefined."""
        assert kappa_affine_slN(2, -2) == 0

    def test_wN_reduces_to_virasoro(self):
        """W_2 = Virasoro."""
        for c in [1, 13, 26]:
            assert kappa_wN(2, c) == kappa_virasoro(c)

    def test_w_large_N_grows(self):
        """kappa(W_N, c=1) grows as H_N - 1 ~ log(N)."""
        k5 = kappa_wN(5, 1)
        k10 = kappa_wN(10, 1)
        k20 = kappa_wN(20, 1)
        assert k5 < k10 < k20


# ============================================================================
# 7. GENUS-1 CROSS-CHECK — F_1 = kappa * lambda_1^FP = kappa/24
# ============================================================================

class TestGenus1CrossCheck:
    """F_1 = kappa/24 provides an independent cross-check."""

    def test_heisenberg_f1(self):
        """H_1: F_1 = 1/24."""
        assert kappa_heisenberg(1) * Fraction(1, 24) == Fraction(1, 24)

    def test_virasoro_f1(self):
        """Vir_c: F_1 = c/48."""
        for c in [1, 2, 26]:
            assert kappa_virasoro(c) * Fraction(1, 24) == Fraction(c, 48)

    def test_sl2_k1_f1(self):
        """sl_2 at k=1: F_1 = 9/4 * 1/24 = 9/96 = 3/32."""
        assert kappa_affine_slN(2, 1) * Fraction(1, 24) == Fraction(3, 32)

    def test_w3_c1_f1(self):
        """W_3 at c=1: F_1 = (5/6)/24 = 5/144."""
        assert kappa_wN(3, 1) * Fraction(1, 24) == Fraction(5, 144)


# ============================================================================
# 8. CROSS-FAMILY CONSISTENCY — no formula mixing
# ============================================================================

class TestCrossFamilyConsistency:
    """Verify no formula has been copied between families (AP1)."""

    def test_heisenberg_vs_virasoro_differ(self):
        """At k=c=1: kappa(H_1)=1, kappa(Vir_1)=1/2."""
        assert kappa_heisenberg(1) != kappa_virasoro(1)

    def test_heisenberg_vs_sl2_differ(self):
        """At k=1: kappa(H_1)=1, kappa(sl_2,1)=9/4."""
        assert kappa_heisenberg(1) != kappa_affine_slN(2, 1)

    def test_virasoro_vs_w3_differ(self):
        """At c=6: kappa(Vir)=3, kappa(W_3)=5."""
        assert kappa_virasoro(6) != kappa_wN(3, 6)

    def test_virasoro_vs_sl2_differ(self):
        """At c=1, k=1: kappa(Vir_1)=1/2, kappa(sl_2,1)=9/4."""
        assert kappa_virasoro(1) != kappa_affine_slN(2, 1)

    def test_lattice_vs_virasoro_differ(self):
        """At rank=c=8: lattice kappa=8, Vir kappa=4."""
        assert kappa_lattice(8) != kappa_virasoro(8)

    def test_all_families_distinct_at_natural_values(self):
        """At k=c=rank=1: all families give different kappa."""
        vals = {
            'Heis': kappa_heisenberg(1),
            'Vir': kappa_virasoro(1),
            'sl_2': kappa_affine_slN(2, 1),
            'W_3': kappa_wN(3, 1),
        }
        values = list(vals.values())
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                assert values[i] != values[j], \
                    f"Families should have distinct kappa at param=1"


# ============================================================================
# 9. KNOWN ERROR DOCUMENTATION
# ============================================================================

class TestKnownErrors:
    """Document that we are aware of all known errors."""

    def test_error_count(self):
        """We have documented 12 known executable code errors."""
        assert len(KNOWN_KAPPA_ERRORS) == 12

    def test_all_critical(self):
        """All known kappa errors are CRITICAL severity."""
        for e in KNOWN_KAPPA_ERRORS:
            assert e['severity'] == 'CRITICAL'

    def test_anti_patterns_covered(self):
        """Errors span AP1, AP39, AP48."""
        aps = {e['anti_pattern'] for e in KNOWN_KAPPA_ERRORS}
        assert 'AP1' in aps
        assert 'AP39' in aps
        assert 'AP48' in aps


# ============================================================================
# 10. NUMERICAL SPOT CHECKS — specific values for the full standard landscape
# ============================================================================

class TestNumericalSpotChecks:
    """Exact numerical values for every standard family at canonical parameters."""

    # Heisenberg
    def test_heis_k1(self):
        assert kappa_heisenberg(1) == 1

    def test_heis_k2(self):
        assert kappa_heisenberg(2) == 2

    # Virasoro
    def test_vir_c1(self):
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_vir_c13(self):
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_vir_c26(self):
        assert kappa_virasoro(26) == 13

    # sl_2
    def test_sl2_k1(self):
        assert kappa_affine_slN(2, 1) == Fraction(9, 4)

    def test_sl2_k2(self):
        assert kappa_affine_slN(2, 2) == 3

    def test_sl2_k5(self):
        assert kappa_affine_slN(2, 5) == Fraction(21, 4)

    # sl_3
    def test_sl3_k1(self):
        assert kappa_affine_slN(3, 1) == Fraction(16, 3)

    # W_3
    def test_w3_c1(self):
        assert kappa_wN(3, 1) == Fraction(5, 6)

    def test_w3_c6(self):
        assert kappa_wN(3, 6) == 5

    # betagamma
    def test_bg(self):
        assert kappa_betagamma() == -1

    # Lattice E_8
    def test_e8(self):
        assert kappa_lattice(8) == 8

    # Exceptional Lie algebras at k=1
    def test_g2_k1(self):
        # G_2: dim=14, h^v=4
        assert kappa_affine_general(14, 4, 1) == Fraction(14 * 5, 8)  # = 35/4

    def test_f4_k1(self):
        # F_4: dim=52, h^v=9
        assert kappa_affine_general(52, 9, 1) == Fraction(52 * 10, 18)  # = 260/9

    def test_e6_k1(self):
        # E_6: dim=78, h^v=12
        assert kappa_affine_general(78, 12, 1) == Fraction(78 * 13, 24)  # = 1014/24 = 169/4

    def test_e7_k1(self):
        # E_7: dim=133, h^v=18
        assert kappa_affine_general(133, 18, 1) == Fraction(133 * 19, 36)  # = 2527/36

    def test_e8_affine_k1(self):
        # E_8: dim=248, h^v=30
        assert kappa_affine_general(248, 30, 1) == Fraction(248 * 31, 60)  # = 7688/60 = 1922/15
