"""Tests for the conformal block shadow integral engine.

Verifies conformal block dimensions, shadow tower truncation,
spectral discriminant, and genus-g chiral homology integrals
for Heisenberg (class G, finite tower) and Virasoro (class M,
infinite tower).

WHAT IS TESTED (proved content only):

  LAYER I:   Shadow tower coefficients S_r
             Heisenberg: S_2 = k, S_r = 0 for r >= 3
             Virasoro: S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)]

  LAYER II:  Spectral discriminant Delta = 8*kappa*S_4
             Heisenberg: Delta = 0 (class G, finite tower)
             Virasoro: Delta = 40/(5c+22) != 0 (class M, infinite tower)

  LAYER III: Conformal block dimensions
             Heisenberg: dim CB_g(H_k) = k^g (Verlinde for U(1)_k)
             Virasoro: dim CB_0 = 1, partition numbers at g=1

  LAYER IV:  Genus-g chiral homology integral F_g = kappa * lambda_g^FP
             Theorem D (PROVED, uniform-weight). (UNIFORM-WEIGHT)

  LAYER V:   Shadow class and depth classification
             G/L/C/M correspondence with tower truncation behaviour.

All expected values independently derived (AP128: never from engine output).
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.conformal_block_shadow_integral_engine import (
    kappa_heisenberg,
    kappa_virasoro,
    r_matrix_heisenberg,
    r_matrix_virasoro,
    S2_heisenberg,
    S3_heisenberg,
    S4_heisenberg,
    Sr_heisenberg,
    S2_virasoro,
    S3_virasoro,
    S4_virasoro,
    delta_heisenberg,
    delta_virasoro,
    shadow_class_heisenberg,
    shadow_depth_heisenberg,
    shadow_class_virasoro,
    shadow_depth_virasoro,
    conformal_block_dim_heisenberg,
    conformal_block_dim_virasoro_genus0,
    conformal_block_dim_virasoro_genus1_vacuum,
    virasoro_partition_function_genus1_coeffs,
    lambda_fp,
    F_g_heisenberg,
    F_g_virasoro,
    verify_heisenberg_tower_terminates,
    verify_virasoro_tower_infinite,
    heisenberg_shadow_package,
    virasoro_shadow_package,
)


# ============================================================================
# LAYER I: KAPPA (obstruction coefficient)
# ============================================================================

class TestKappa:
    """Kappa values for Heisenberg and Virasoro."""

    def test_kappa_heisenberg_symbolic(self):
        """kappa(H_k) = k symbolically."""
        assert kappa_heisenberg() == Symbol('k')

    def test_kappa_heisenberg_numerical(self):
        """kappa(H_k) at specific levels."""
        # VERIFIED [DC] direct: kappa = level, [LC] k=0 -> 0
        assert kappa_heisenberg(0) == 0
        assert kappa_heisenberg(1) == 1
        assert kappa_heisenberg(5) == 5
        assert kappa_heisenberg(100) == 100

    def test_kappa_virasoro_symbolic(self):
        """kappa(Vir_c) = c/2 symbolically."""
        assert kappa_virasoro() == Symbol('c') / 2

    def test_kappa_virasoro_numerical(self):
        """kappa(Vir_c) at specific central charges."""
        # VERIFIED [DC] direct: kappa = c/2, [LC] c=0 -> 0, [SY] c=13 -> 13/2 self-dual
        assert kappa_virasoro(0) == 0
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(13) == Rational(13, 2)  # self-dual point (C8)
        assert kappa_virasoro(26) == 13

    def test_kappa_virasoro_not_c(self):
        """kappa(Vir_c) = c/2, NOT c (B8)."""
        for c_val in [1, 2, 13, 26]:
            assert kappa_virasoro(c_val) != c_val or c_val == 0


# ============================================================================
# LAYER II: R-MATRIX (AP126: level prefix mandatory)
# ============================================================================

class TestRMatrix:
    """Classical r-matrices with level prefix verification."""

    def test_heisenberg_r_matrix_ap126_k0(self):
        """AP126/AP141: r^Heis(z)|_{k=0} = 0."""
        z = Symbol('z')
        # VERIFIED [DC] direct substitution, [SY] abelian limit must vanish
        assert r_matrix_heisenberg(z, k_val=0) == 0

    def test_heisenberg_r_matrix_level_prefix(self):
        """r^Heis(z) = k/z has level prefix k."""
        z = Symbol('z')
        r = r_matrix_heisenberg(z)
        # VERIFIED [DC] formula, [LT] landscape_census.tex:Heis
        assert simplify(r - Symbol('k') / z) == 0

    def test_virasoro_r_matrix_cubic_not_quartic(self):
        """r^Vir(z) has z^{-3} term, NOT z^{-4} (AP19, B2)."""
        z = Symbol('z')
        r = r_matrix_virasoro(z)
        T = Symbol('T')
        c_sym = Symbol('c')
        # VERIFIED [DC] AP19 d-log absorption, [LT] CLAUDE.md C11
        expected = c_sym / 2 / z**3 + 2 * T / z
        assert simplify(r - expected) == 0


# ============================================================================
# LAYER III: SHADOW TOWER COEFFICIENTS
# ============================================================================

class TestShadowTower:
    """Shadow coefficients S_r for both families."""

    # --- Heisenberg (class G) ---

    def test_heisenberg_S2(self):
        """S_2(H_k) = k."""
        # VERIFIED [DC] S_2 = kappa for all families, [CF] matches genus_expansion.py
        assert S2_heisenberg(1) == 1
        assert S2_heisenberg(5) == 5

    def test_heisenberg_S3_vanishes(self):
        """S_3(H_k) = 0 (abelian: cubic shadow vanishes)."""
        # VERIFIED [DC] [h,h]=0 for abelian, [LT] affine_sl2_shadow_tower.py Cartan line
        assert S3_heisenberg() == 0

    def test_heisenberg_S4_vanishes(self):
        """S_4(H_k) = 0 (abelian: quartic contact vanishes)."""
        # VERIFIED [DC] Jacobi trivial for abelian, [SY] class G definition
        assert S4_heisenberg() == 0

    def test_heisenberg_tower_all_zero(self):
        """S_r(H_k) = 0 for all r >= 3 (class G truncation)."""
        # VERIFIED [DC] abelian => all higher brackets vanish, [SY] class G
        for r in range(3, 15):
            assert Sr_heisenberg(r) == 0

    # --- Virasoro (class M) ---

    def test_virasoro_S2(self):
        """S_2(Vir_c) = c/2."""
        # VERIFIED [DC] S_2 = kappa, [CF] matches virasoro_shadow_extended.py
        assert S2_virasoro(1) == Rational(1, 2)
        assert S2_virasoro(26) == 13

    def test_virasoro_S3(self):
        """S_3(Vir_c) = 2 (c-independent)."""
        # VERIFIED [DC] direct OPE computation, [LT] virasoro_shadow_extended.py:S3()
        assert S3_virasoro() == 2

    def test_virasoro_S4_formula(self):
        """S_4(Vir_c) = 10/[c(5c+22)]."""
        # VERIFIED [DC] quartic contact from T-T-T-T OPE,
        # [CF] virasoro_shadow_extended.py:S4(),
        # [NE] c=1: 10/(1*27) = 10/27
        assert S4_virasoro(1) == Rational(10, 27)
        assert S4_virasoro(13) == Rational(10, 13 * 87)  # 10/1131
        assert S4_virasoro(24) == Rational(10, 24 * 142)  # = 5/1704

    def test_virasoro_S4_nonzero_generic(self):
        """S_4(Vir_c) != 0 for generic c (confirms class M)."""
        for c_val in [1, 2, 5, 13, 24, 26]:
            assert S4_virasoro(c_val) != 0


# ============================================================================
# LAYER IV: SPECTRAL DISCRIMINANT Delta = 8*kappa*S_4
# ============================================================================

class TestDelta:
    """Spectral discriminant controlling tower truncation."""

    def test_delta_heisenberg_zero(self):
        """Delta(H_k) = 0 for all k (class G)."""
        # VERIFIED [DC] 8*k*0 = 0, [SY] class G <=> Delta = 0
        for k_val in [0, 1, 5, 100]:
            assert delta_heisenberg(k_val) == 0

    def test_delta_virasoro_formula(self):
        """Delta(Vir_c) = 40/(5c+22)."""
        # VERIFIED [DC] 8*(c/2)*10/[c(5c+22)] = 40/(5c+22),
        # [CF] celestial_arithmetic_engine.py, virasoro_shadow_extended.py
        assert delta_virasoro(1) == Rational(40, 27)
        assert delta_virasoro(13) == Rational(40, 87)
        assert delta_virasoro(24) == Rational(40, 142)  # = 20/71

    def test_delta_virasoro_nonzero(self):
        """Delta(Vir_c) != 0 for any c > 0 (class M)."""
        # VERIFIED [DC] 5c+22 > 0 for c > 0, [SY] class M <=> Delta != 0
        for c_val in [1, 2, 13, 24, 26, 100]:
            assert delta_virasoro(c_val) != 0

    def test_delta_virasoro_c24_matches_monster(self):
        """Delta(Vir_{c=24}) = 20/71, consistent with moonshine_shadow_depth.py."""
        # VERIFIED [CF] moonshine_shadow_depth.py line 365, [DC] 40/142 = 20/71
        assert delta_virasoro(24) == Rational(20, 71)

    def test_delta_consistency_8_kappa_S4(self):
        """Verify Delta = 8*kappa*S_4 by direct computation."""
        # VERIFIED [DC] algebraic identity, [NE] numerical evaluation
        for c_val in [1, 2, 5, 13]:
            cv = Rational(c_val)
            kv = cv / 2
            s4 = Rational(10) / (cv * (5 * cv + 22))
            delta_direct = 8 * kv * s4
            delta_formula = Rational(40) / (5 * cv + 22)
            assert delta_direct == delta_formula


# ============================================================================
# LAYER V: SHADOW CLASS AND DEPTH
# ============================================================================

class TestShadowClassification:
    """G/L/C/M classification and shadow depth."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G."""
        assert shadow_class_heisenberg() == 'G'

    def test_heisenberg_depth_2(self):
        """Shadow depth = 2 for Heisenberg."""
        # VERIFIED [DC] S_r=0 for r>=3, [SY] class G definition
        assert shadow_depth_heisenberg() == 2

    def test_virasoro_class_M(self):
        """Virasoro is class M."""
        assert shadow_class_virasoro() == 'M'

    def test_virasoro_depth_infinite(self):
        """Shadow depth = infinity for Virasoro."""
        # VERIFIED [DC] S_r != 0 for all r, [SY] class M definition
        assert shadow_depth_virasoro() == float('inf')

    def test_tower_terminates_heisenberg(self):
        """Heisenberg tower terminates (verified to depth 20)."""
        assert verify_heisenberg_tower_terminates(max_depth=20) is True

    def test_tower_infinite_virasoro(self):
        """Virasoro tower does NOT terminate (verified to depth 8)."""
        assert verify_virasoro_tower_infinite(c_val=1, max_depth=8) is True


# ============================================================================
# LAYER VI: CONFORMAL BLOCK DIMENSIONS
# ============================================================================

class TestConformalBlockDimensions:
    """Conformal block dimensions controlled by shadow tower."""

    # --- Heisenberg: dim = k^g (Verlinde for U(1)_k) ---

    def test_heisenberg_genus0(self):
        """dim CB_0(H_k) = 1 for all k (unique vacuum on P^1)."""
        # VERIFIED [DC] k^0 = 1, [LT] Verlinde formula, [SY] genus-0 universality
        for k_val in [1, 2, 5, 10]:
            assert conformal_block_dim_heisenberg(k_val, 0) == 1

    def test_heisenberg_genus1(self):
        """dim CB_1(H_k) = k."""
        # VERIFIED [DC] k^1 = k, [LT] Verlinde: k simple objects for U(1)_k,
        # [CF] Z/kZ fusion rules give k blocks on torus
        assert conformal_block_dim_heisenberg(1, 1) == 1
        assert conformal_block_dim_heisenberg(2, 1) == 2
        assert conformal_block_dim_heisenberg(5, 1) == 5

    def test_heisenberg_genus2(self):
        """dim CB_2(H_k) = k^2."""
        # VERIFIED [DC] k^2, [LT] Verlinde multiplicativity
        assert conformal_block_dim_heisenberg(1, 2) == 1
        assert conformal_block_dim_heisenberg(2, 2) == 4
        assert conformal_block_dim_heisenberg(3, 2) == 9

    def test_heisenberg_genus3(self):
        """dim CB_3(H_k) = k^3."""
        # VERIFIED [DC] k^3, [LT] Verlinde
        assert conformal_block_dim_heisenberg(2, 3) == 8
        assert conformal_block_dim_heisenberg(3, 3) == 27

    def test_heisenberg_k1_all_genera(self):
        """dim CB_g(H_1) = 1 for all g (unique block at level 1)."""
        # VERIFIED [DC] 1^g = 1, [SY] trivial modular functor
        for g in range(6):
            assert conformal_block_dim_heisenberg(1, g) == 1

    def test_heisenberg_multiplicativity(self):
        """dim CB_{g1+g2}(H_k) = dim CB_{g1} * dim CB_{g2} (handle decomposition)."""
        # VERIFIED [DC] k^(g1+g2) = k^g1 * k^g2, [SY] multiplicativity of k^g
        for k_val in [2, 3, 5]:
            for g1 in range(4):
                for g2 in range(4):
                    assert (conformal_block_dim_heisenberg(k_val, g1 + g2)
                            == conformal_block_dim_heisenberg(k_val, g1)
                            * conformal_block_dim_heisenberg(k_val, g2))

    # --- Virasoro: genus 0 and genus 1 ---

    def test_virasoro_genus0(self):
        """dim CB_0(Vir_c) = 1 (unique vacuum block on P^1)."""
        # VERIFIED [DC] universal genus-0, [LT] BPZ/Zhu
        assert conformal_block_dim_virasoro_genus0() == 1

    def test_virasoro_genus1_vacuum(self):
        """dim CB_1(Vir_c, vacuum) = 1."""
        # VERIFIED [DC] single vacuum character, [LT] Zhu's theorem
        assert conformal_block_dim_virasoro_genus1_vacuum() == 1

    def test_virasoro_partition_coefficients(self):
        """Genus-1 partition function coefficients = partition numbers."""
        # VERIFIED [DC] direct DP computation, [LT] OEIS A000041,
        # [CF] Andrews "Theory of Partitions" Table 1.1
        coeffs = virasoro_partition_function_genus1_coeffs(1, num_terms=10)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
        assert coeffs == expected

    def test_virasoro_partition_growth(self):
        """Partition numbers grow without bound (infinite tower witness)."""
        coeffs = virasoro_partition_function_genus1_coeffs(1, num_terms=15)
        # Monotonically increasing after p(0)=p(1)=1
        for i in range(2, len(coeffs)):
            assert coeffs[i] > coeffs[i - 1]


# ============================================================================
# LAYER VII: GENUS-g CHIRAL HOMOLOGY INTEGRAL (Theorem D)
# ============================================================================

class TestGenusIntegral:
    """F_g(A) = kappa(A) * lambda_g^FP (Theorem D, uniform-weight)."""

    def test_lambda_fp_values(self):
        """lambda_g^FP at small genera."""
        # VERIFIED [DC] Bernoulli numbers, [LT] Faber-Pandharipande,
        # [CF] genus_expansion.py:lambda_fp
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        assert lambda_fp(3) == Rational(31, 967680)

    def test_F_g_heisenberg_k1(self):
        """F_g(H_1) = lambda_g^FP (kappa = 1)."""
        # VERIFIED [DC] 1 * lambda_g, [CF] genus_expansion.py
        for g in range(1, 5):
            assert F_g_heisenberg(1, g) == lambda_fp(g)

    def test_F_g_heisenberg_k0(self):
        """F_g(H_0) = 0 for all g (kappa = 0 => uncurved)."""
        # VERIFIED [DC] 0 * lambda_g = 0, [SY] kappa=0 => m_0=0
        for g in range(1, 5):
            assert F_g_heisenberg(0, g) == 0

    def test_F_g_virasoro_c1(self):
        """F_g(Vir_1) = (1/2) * lambda_g^FP."""
        # VERIFIED [DC] kappa(Vir_1) = 1/2, [CF] genus_expansion.py
        assert F_g_virasoro(1, 1) == Rational(1, 48)  # (1/2)*(1/24)
        assert F_g_virasoro(1, 2) == Rational(7, 11520)  # (1/2)*(7/5760)

    def test_F_g_virasoro_c13_selfdual(self):
        """F_g(Vir_13) = (13/2) * lambda_g^FP (self-dual point)."""
        # VERIFIED [DC] kappa = 13/2, [SY] c=13 self-dual (C8),
        # [CF] genus_expansion.py:kappa_virasoro(13)
        assert F_g_virasoro(13, 1) == Rational(13, 48)

    def test_F_g_virasoro_c26(self):
        """F_g(Vir_26) = 13 * lambda_g^FP."""
        # VERIFIED [DC] kappa(Vir_26) = 13, [CF] string ghost cancellation c=26
        assert F_g_virasoro(26, 1) == Rational(13, 24)


# ============================================================================
# LAYER VIII: SHADOW-CONTROLLED CONTRAST
# ============================================================================

class TestShadowContrast:
    """The fundamental contrast: class G (finite) vs class M (infinite)."""

    def test_heisenberg_finite_virasoro_infinite(self):
        """Heisenberg tower terminates; Virasoro does not."""
        assert delta_heisenberg(1) == 0
        assert delta_virasoro(1) != 0
        assert shadow_depth_heisenberg() < float('inf')
        assert shadow_depth_virasoro() == float('inf')

    def test_conformal_block_finite_vs_growing(self):
        """Heisenberg blocks are k^g; Virasoro partition fn grows unboundedly."""
        # Heisenberg at k=2: finite, predictable
        dims_heis = [conformal_block_dim_heisenberg(2, g) for g in range(5)]
        assert dims_heis == [1, 2, 4, 8, 16]  # VERIFIED [DC] 2^g, [SY] powers of 2
        # Virasoro: partition numbers grow
        coeffs = virasoro_partition_function_genus1_coeffs(1, 12)
        assert coeffs[-1] > 50  # p(11) = 56

    def test_heisenberg_package_consistency(self):
        """Heisenberg shadow package is internally consistent."""
        pkg = heisenberg_shadow_package(3)
        assert pkg['kappa'] == 3
        assert pkg['shadow_class'] == 'G'
        assert pkg['Delta'] == 0
        assert pkg['tower_terminates'] is True
        assert pkg['conformal_block_dims'][2] == 9  # VERIFIED [DC] 3^2

    def test_virasoro_package_consistency(self):
        """Virasoro shadow package is internally consistent."""
        pkg = virasoro_shadow_package(1)
        assert pkg['kappa'] == Rational(1, 2)
        assert pkg['shadow_class'] == 'M'
        assert pkg['Delta'] == Rational(40, 27)  # VERIFIED [DC] 40/(5+22)
        assert pkg['tower_terminates'] is False
        assert pkg['conformal_block_dim_g0'] == 1

    def test_delta_linear_in_kappa(self):
        """C30: Delta = 8*kappa*S_4 is LINEAR in kappa, not quadratic."""
        # VERIFIED [DC] algebraic, [LT] CLAUDE.md C30
        # For Virasoro: Delta = 40/(5c+22) is independent of kappa directly,
        # but the formula 8*kappa*S_4 = 8*(c/2)*10/[c(5c+22)] cancels the c,
        # showing linearity in kappa (which is c/2).
        c1 = Rational(2)
        c2 = Rational(4)
        # kappa doubles: c/2 goes from 1 to 2
        delta1 = delta_virasoro(c1)  # 40/(10+22) = 40/32 = 5/4
        delta2 = delta_virasoro(c2)  # 40/(20+22) = 40/42 = 20/21
        # Delta does NOT double when kappa doubles (because S_4 also depends on c)
        # But the formula is still linear in kappa for FIXED S_4.
        # Verify the algebraic identity directly:
        for cv in [1, 2, 5, 13]:
            kv = Rational(cv) / 2
            s4 = Rational(10) / (Rational(cv) * (5 * Rational(cv) + 22))
            assert 8 * kv * s4 == delta_virasoro(cv)
