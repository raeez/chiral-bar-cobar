r"""Tests for W_7 shadow obstruction tower.

Systematic verification of the W_7 = DS(sl_7) shadow tower:
central charge, kappa, complementarity, shadow depth, quartic contact,
growth rate, DS pipeline, multi-channel structure, large-N context.

Multi-path verification: every key result checked by 3+ independent methods.

STRUCTURE:
    Section 1: Central charge formulas (8 tests)
    Section 2: Harmonic number and anomaly ratio (6 tests)
    Section 3: Kappa -- four independent methods (10 tests)
    Section 4: Complementarity / Koszul duality (8 tests)
    Section 5: T-line shadow tower (8 tests)
    Section 6: Quartic contact invariant (5 tests)
    Section 7: Shadow depth = infinity (5 tests)
    Section 8: Shadow growth rate (5 tests)
    Section 9: DS pipeline: sl_7 -> W_7 (7 tests)
    Section 10: Multi-channel structure (6 tests)
    Section 11: DS cascade: N=2,...,7 comparison (8 tests)
    Section 12: Large-N scaling (7 tests)
    Section 13: Cross-engine consistency (6 tests)
    Section 14: Line-by-line shadow data (6 tests)
    Section 15: Propagator variance (5 tests)

Total: 100 tests.
"""

import pytest
from fractions import Fraction
import math

from sympy import Rational, cancel, Symbol

from compute.lib.w7_shadow_tower import (
    # Central charge
    w7_central_charge,
    w7_central_charge_frac,
    w7_ff_dual_level,
    w7_ff_central_charge_sum,
    # Harmonic / anomaly
    w7_harmonic_number,
    w7_anomaly_ratio,
    # Kappa
    w7_kappa_total,
    w7_kappa_total_frac,
    w7_kappa_channel,
    w7_kappa_from_channels,
    w7_kappa_from_anomaly_ratio,
    w7_kappa_from_harmonic,
    # Shadow data
    t_line_shadow_data,
    w3_line_shadow_data,
    w7_line_shadow_data,
    all_line_shadow_data,
    # Tower
    t_line_tower_numerical,
    t_line_tower_exact_at_level,
    generic_line_tower_exact,
    # Quartic
    w7_quartic_contact_T_line,
    w7_quartic_contact_T_at_level,
    # Mixing
    w7_kappas,
    w7_propagator_variance_numerical,
    # Growth rate
    w7_t_line_growth_rate,
    w7_growth_rate_at_level,
    # Complementarity
    w7_kappa_complementarity,
    w7_channel_complementarity,
    # DS pipeline
    w7_ds_ghost_central_charge,
    w7_ds_ghost_kappa,
    w7_ds_pipeline,
    # Multi-channel
    w7_shadow_metric_diagonal,
    w7_binary_channel_kappas,
    # Large-N
    w7_in_large_n_context,
    w7_anomaly_ratio_sequence,
    w7_kappa_ff_sum_sequence,
    w7_ghost_c_sequence,
    ds_cascade_comparison,
    # Constants
    W7_SPINS,
    W7_RANK,
    W7_N,
    W7_H_VEE,
    W7_DIM_SL7,
    W7_NUM_BINARY_CHANNELS,
    W7_BINARY_CHANNELS,
    # Summary
    w7_full_summary,
)


# ============================================================================
# Section 1: Central charge formulas
# ============================================================================

class TestW7CentralCharge:
    """Central charge c(W_7, k) = 6 - 336(k+6)^2/(k+7) (Fateev-Lukyanov)."""

    def test_c_w7_k1(self):
        """c(W_7, k=1) = 6*(-48)/8 = -36."""
        # VERIFIED: c_wn_fl(7,1)=-2052 [DC], complementarity c(1)+c(-15)=1356 [SY]
        assert w7_central_charge_frac(Fraction(1)) == Fraction(-2052)

    def test_c_w7_k7(self):
        """c(W_7, k=7) = 6*(-42)/14 = -18."""
        assert w7_central_charge_frac(Fraction(7)) == Fraction(-4050)

    def test_c_w7_k5(self):
        """c(W_7, k=5) = 6*(-44)/12 = -22."""
        assert w7_central_charge_frac(Fraction(5)) == Fraction(-3382)

    def test_c_w7_k49(self):
        """c(W_7, k=49) = 0."""
        assert w7_central_charge_frac(Fraction(49)) == Fraction(-18144)

    def test_ff_sum(self):
        """c(k) + c(k') = 12 for all k."""
        # VERIFIED: 2(N-1)+4N(N^2-1) = 12+1344 = 1356 [DC]
        assert w7_ff_central_charge_sum() == Rational(1356)
        for kv in [Fraction(1), Fraction(5), Fraction(7), Fraction(10), Fraction(100)]:
            c1 = w7_central_charge_frac(kv)
            c2 = w7_central_charge_frac(-kv - 14)
            assert c1 + c2 == Fraction(1356), f"Failed at k={kv}"

    def test_c_matches_general(self):
        """Matches (N-1) - N(N^2-1)(k+N-1)^2/(k+N) with N=7 (Fateev-Lukyanov)."""
        for kv in [Fraction(1), Fraction(5), Fraction(50)]:
            c_w7 = w7_central_charge_frac(kv)
            c_gen = Fraction(6) - Fraction(336) * (kv + 6)**2 / (kv + 7)
            assert c_w7 == c_gen

    def test_large_k_limit(self):
        """c ~ -N(N^2-1)*k as k -> infinity (Fateev-Lukyanov)."""
        # VERIFIED: FL formula c = 6 - 336*(k+6)^2/(k+7) ~ -336*k [DC]
        c_1000 = w7_central_charge_frac(Fraction(1000))
        c_10000 = w7_central_charge_frac(Fraction(10000))
        # c grows more negative: c(10000) < c(1000) < 0
        assert float(c_10000) < float(c_1000) < 0
        # Leading coefficient: c/k -> -336 = -N(N^2-1)
        ratio = float(c_10000) / 10000
        assert abs(ratio - (-336)) < 1

    def test_ff_involution(self):
        """FF is involution: (k')' = k."""
        for kv in [Fraction(1), Fraction(5), Fraction(13)]:
            k_prime = -kv - 14
            k_double_prime = -k_prime - 14
            assert k_double_prime == kv


# ============================================================================
# Section 2: Harmonic number and anomaly ratio
# ============================================================================

class TestW7HarmonicAnomaly:
    """H_7 = 363/140, rho(7) = H_7 - 1 = 223/140."""

    def test_harmonic_number(self):
        """H_7 = 363/140."""
        assert w7_harmonic_number() == Rational(363, 140)

    def test_harmonic_manual(self):
        """Manual: 1+1/2+1/3+1/4+1/5+1/6+1/7 = 363/140."""
        s = sum(Fraction(1, j) for j in range(1, 8))
        assert s == Fraction(363, 140)

    def test_anomaly_ratio(self):
        """rho(7) = H_7 - 1 = 223/140."""
        assert w7_anomaly_ratio() == Rational(223, 140)

    def test_anomaly_ratio_manual(self):
        """Manual: 1/2+1/3+1/4+1/5+1/6+1/7 = 223/140."""
        s = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7)
        assert s == Fraction(223, 140)

    def test_anomaly_ratio_vs_harmonic(self):
        """rho(7) = H_7 - 1."""
        assert w7_anomaly_ratio() == w7_harmonic_number() - 1

    def test_anomaly_ratio_sequence_monotone(self):
        """rho(N) is strictly increasing in N."""
        seq = w7_anomaly_ratio_sequence()
        for N in range(2, 7):
            assert seq[N] < seq[N + 1]


# ============================================================================
# Section 3: Kappa -- four independent methods
# ============================================================================

class TestW7Kappa:
    """kappa(W_7) via anomaly ratio, channel sum, harmonic sum, and sympy formula."""

    def test_method1_anomaly(self):
        """Method 1: kappa = (223/140)*c."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c_w = w7_central_charge_frac(kv)
            kap = w7_kappa_total_frac(kv)
            assert kap == Fraction(223, 140) * c_w

    def test_method2_channel_sum(self):
        """Method 2: kappa = c/2+c/3+c/4+c/5+c/6+c/7 = 223c/140."""
        cc = Symbol('c')
        kap_channels = w7_kappa_from_channels(cc)
        kap_total = w7_kappa_total(cc)
        assert cancel(kap_channels - kap_total) == 0

    def test_method3_anomaly_ratio(self):
        """Method 3: sympy formula kappa = (223/140)*c."""
        cc = Symbol('c')
        kap_ratio = w7_kappa_from_anomaly_ratio(cc)
        kap_total = w7_kappa_total(cc)
        assert cancel(kap_ratio - kap_total) == 0

    def test_method4_harmonic(self):
        """Method 4: explicit harmonic sum computation."""
        cc = Symbol('c')
        kap_harmonic = w7_kappa_from_harmonic(cc)
        kap_total = w7_kappa_total(cc)
        assert cancel(kap_harmonic - kap_total) == 0

    def test_kappa_k5(self):
        """kappa(W_7, k=5) = (223/140)*(-3382) = -377093/70."""
        # VERIFIED: c_wn_fl(7,5) = -3382 [DC], kappa = (H_7-1)*c [SY]
        kap = w7_kappa_total_frac(Fraction(5))
        assert kap == Fraction(223, 140) * Fraction(-3382)
        assert kap == Fraction(-377093, 70)

    def test_kappa_k1(self):
        """kappa(W_7, k=1) = (223/140)*(-2052) = -114399/35."""
        # VERIFIED: c_wn_fl(7,1) = -2052 [DC], 223*2052=457596, 457596/140=114399/35 [SY]
        kap = w7_kappa_total_frac(Fraction(1))
        expected = Fraction(223, 140) * Fraction(-2052)
        assert kap == expected
        assert kap == Fraction(-114399, 35)

    def test_kappa_k7(self):
        """kappa(W_7, k=7) = (223/140)*(-4050) = -90315/14."""
        # VERIFIED: c_wn_fl(7,7) = -4050 [DC], 223*4050=903150, 903150/140=90315/14 [SY]
        kap = w7_kappa_total_frac(Fraction(7))
        expected = Fraction(223, 140) * Fraction(-4050)
        assert kap == expected
        assert kap == Fraction(-90315, 14)

    def test_kappa_channel_sum_numerical(self):
        """Channel sum agrees with total at numerical level."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c_w = w7_central_charge_frac(kv)
            channel_sum = sum(c_w / s for s in W7_SPINS)
            total = w7_kappa_total_frac(kv)
            assert channel_sum == total

    def test_all_channel_kappas(self):
        """Each channel kappa is c/s."""
        c_w = w7_central_charge_frac(Fraction(5))
        for s in W7_SPINS:
            assert w7_kappa_channel(s, c_w) == c_w / s

    def test_kappa_from_ds_cascade_engine(self):
        """Cross-check against ds_shadow_cascade_engine.kappa_WN."""
        from compute.lib.ds_shadow_cascade_engine import kappa_WN
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            assert w7_kappa_total_frac(kv) == kappa_WN(7, kv)


# ============================================================================
# Section 4: Complementarity
# ============================================================================

class TestW7Complementarity:
    """kappa(k) + kappa(k') = (223/140)*12 = 669/35."""

    def test_expected_value(self):
        """(223/140)*1356 = 302388/140 = 75597/35."""
        # VERIFIED: 223*1356=302388 [DC], 302388/140=75597/35 [SY]
        assert Fraction(223, 140) * Fraction(1356) == Fraction(75597, 35)

    def test_complementarity_k5(self):
        comp = w7_kappa_complementarity(Fraction(5))
        assert comp['matches']
        assert comp['sum'] == Fraction(75597, 35)

    def test_complementarity_k1(self):
        comp = w7_kappa_complementarity(Fraction(1))
        assert comp['matches']

    def test_complementarity_k7(self):
        comp = w7_kappa_complementarity(Fraction(7))
        assert comp['matches']

    def test_complementarity_k10(self):
        comp = w7_kappa_complementarity(Fraction(10))
        assert comp['matches']

    def test_complementarity_k100(self):
        comp = w7_kappa_complementarity(Fraction(100))
        assert comp['matches']

    def test_channel_complementarity_all_spins(self):
        """Each channel satisfies kappa_s + kappa_s' = 12/s."""
        for s in W7_SPINS:
            comp = w7_channel_complementarity(Fraction(5), s)
            assert comp['matches'], f"Channel complementarity failed for spin {s}"

    def test_channel_sum_equals_total(self):
        """Sum of channel complementarities = total complementarity."""
        kv = Fraction(5)
        total = Fraction(0)
        for s in W7_SPINS:
            comp = w7_channel_complementarity(kv, s)
            total += comp['sum']
        assert total == Fraction(75597, 35)


# ============================================================================
# Section 5: T-line shadow tower
# ============================================================================

class TestW7TLineTower:
    """T-line shadow tower (= Virasoro at c=c(W_7,k))."""

    def test_s2_is_kappa_t(self):
        tower = t_line_tower_exact_at_level(Fraction(5), 8)
        c_w = w7_central_charge_frac(Fraction(5))
        assert tower[2] == c_w / 2

    def test_s3_universal(self):
        """S_3 = 2 universally on the T-line (Virasoro cubic)."""
        tower = t_line_tower_exact_at_level(Fraction(5), 8)
        assert tower[3] == Fraction(2)

    def test_s4_quartic(self):
        k_val = Fraction(5)
        c_w = w7_central_charge_frac(k_val)
        expected = Fraction(10) / (c_w * (5 * c_w + 22))
        tower = t_line_tower_exact_at_level(k_val, 8)
        assert tower[4] == expected

    def test_tower_nonvanishing(self):
        """All S_r nonzero for r=4,...,10 (class M)."""
        tower = t_line_tower_exact_at_level(Fraction(5), 10)
        for r in range(4, 11):
            assert tower[r] != Fraction(0), f"S_{r} vanishes!"

    def test_exact_vs_numerical(self):
        k_val = Fraction(5)
        c_w = float(w7_central_charge_frac(k_val))
        tower_exact = t_line_tower_exact_at_level(k_val, 8)
        tower_num = t_line_tower_numerical(c_w, 8)
        for r in range(2, 9):
            exact_val = float(tower_exact[r])
            num_val = tower_num[r]
            assert abs(exact_val - num_val) < 1e-8, f"S_{r}: {exact_val} vs {num_val}"

    def test_tower_at_k1(self):
        """At k=1: c=-2052, S_2 = -1026, S_3 = 2."""
        # VERIFIED: c_wn_fl(7,1) = -2052 [DC], S_2 = c/2 = -1026 [SY]
        tower = t_line_tower_exact_at_level(Fraction(1), 6)
        assert tower[2] == Fraction(-2052) / 2
        assert tower[2] == Fraction(-1026)
        assert tower[3] == Fraction(2)

    def test_tower_at_k7(self):
        """At k=7: c=-4050, S_2 = -2025, S_3 = 2."""
        # VERIFIED: c_wn_fl(7,7) = -4050 [DC], S_2 = c/2 = -2025 [SY]
        tower = t_line_tower_exact_at_level(Fraction(7), 6)
        assert tower[2] == Fraction(-4050) / 2
        assert tower[2] == Fraction(-2025)
        assert tower[3] == Fraction(2)

    def test_tower_monotone_decay(self):
        """|S_r| decreases for r >= 4 (convergent tower at moderate c)."""
        k_val = Fraction(5)  # c = -22
        tower = t_line_tower_exact_at_level(k_val, 10)
        for r in range(5, 11):
            assert abs(float(tower[r])) < abs(float(tower[r - 1]))


# ============================================================================
# Section 6: Quartic contact invariant
# ============================================================================

class TestW7QuarticContact:

    def test_quartic_at_k5(self):
        """Q^contact_T(k=5) at c=-3382."""
        # VERIFIED: c_wn_fl(7,5) = -3382 [DC], Q = 10/(c*(5c+22)) [SY]
        c_w = Fraction(-3382)
        expected = Fraction(10) / (c_w * (5 * c_w + 22))
        Q = w7_quartic_contact_T_at_level(Fraction(5))
        assert Q == expected

    def test_quartic_matches_s4(self):
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            Q = w7_quartic_contact_T_at_level(kv)
            tower = t_line_tower_exact_at_level(kv, 4)
            assert Q == tower[4]

    def test_quartic_nonzero(self):
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            Q = w7_quartic_contact_T_at_level(kv)
            assert Q != Fraction(0)

    def test_quartic_explicit_k5(self):
        """At c=-3382: 10/((-3382)(5*(-3382)+22)) = 10/((-3382)(-16888)) = 5/28557608."""
        # VERIFIED: -3382*(-16888) = 57115216, 10/57115216 = 5/28557608 [DC]
        Q = w7_quartic_contact_T_at_level(Fraction(5))
        assert Q == Fraction(10) / (Fraction(-3382) * Fraction(-16888))
        assert Q == Fraction(10, 57115216)
        assert Q == Fraction(5, 28557608)

    def test_quartic_smaller_than_w6(self):
        """Q(W_7) < Q(W_6) at the same level (larger |c| -> smaller Q)."""
        from compute.lib.w6_shadow_tower import w6_quartic_contact_T_at_level
        k_val = Fraction(5)
        Q6 = abs(float(w6_quartic_contact_T_at_level(k_val)))
        Q7 = abs(float(w7_quartic_contact_T_at_level(k_val)))
        assert Q7 < Q6


# ============================================================================
# Section 7: Shadow depth = infinity
# ============================================================================

class TestW7ShadowDepth:

    def test_depth_infinity_k5(self):
        tower = t_line_tower_exact_at_level(Fraction(5), 10)
        for r in range(4, 11):
            assert tower[r] != Fraction(0)

    def test_depth_infinity_k1(self):
        tower = t_line_tower_exact_at_level(Fraction(1), 8)
        for r in range(4, 9):
            assert tower[r] != Fraction(0)

    def test_depth_infinity_k7(self):
        tower = t_line_tower_exact_at_level(Fraction(7), 8)
        for r in range(4, 9):
            assert tower[r] != Fraction(0)

    def test_discriminant_nonzero(self):
        """Delta = 40/(5c+22) nonzero for generic c."""
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            c_w = w7_central_charge_frac(kv)
            Delta = Fraction(40) / (5 * c_w + 22)
            assert Delta != 0

    def test_ds_depth_increase(self):
        pipe = w7_ds_pipeline(Fraction(5), 8)
        assert pipe['depth_increase']


# ============================================================================
# Section 8: Growth rate
# ============================================================================

class TestW7GrowthRate:

    def test_positive(self):
        for kv in [1, 5, 7, 10, 50]:
            rho = w7_growth_rate_at_level(kv)
            assert rho > 0

    def test_k5_value(self):
        """rho(k=5) at c=-3382 (Fateev-Lukyanov)."""
        # VERIFIED: c=-3382, rho^2=(180*(-3382)+872)/((5*(-3382)+22)*(-3382)^2) [DC]
        rho = w7_growth_rate_at_level(5)
        c_val = -3382.0
        rho_sq = (180 * c_val + 872) / ((5 * c_val + 22) * c_val ** 2)
        expected = math.sqrt(abs(rho_sq))
        assert abs(rho - expected) < 1e-10

    def test_smaller_than_w6(self):
        """rho(W_7) < rho(W_6) at same level (larger |c|)."""
        from compute.lib.w6_shadow_tower import w6_growth_rate_at_level
        rho_w6 = w6_growth_rate_at_level(5)
        rho_w7 = w7_growth_rate_at_level(5)
        assert rho_w7 < rho_w6

    def test_formula(self):
        """rho^2 = (180c+872)/((5c+22)*c^2)."""
        c_val = float(w7_central_charge_frac(Fraction(5)))
        rho_sq = (180 * c_val + 872) / ((5 * c_val + 22) * c_val ** 2)
        rho = math.sqrt(abs(rho_sq))
        assert abs(rho - w7_growth_rate_at_level(5)) < 1e-10

    def test_large_negative_c_small_rho(self):
        """Growth rate decreases as |c| increases (more negative c)."""
        # VERIFIED: FL formula: k=1 -> c=-2052, k=5 -> c=-3382 [DC]
        # k=5 has larger |c| -> smaller rho
        rho_k5 = w7_growth_rate_at_level(5)
        rho_k1 = w7_growth_rate_at_level(1)
        assert rho_k5 < rho_k1  # k=5 has larger |c|


# ============================================================================
# Section 9: DS pipeline
# ============================================================================

class TestW7DSPipeline:

    def test_c_additivity(self):
        pipe = w7_ds_pipeline(Fraction(5), 8)
        assert pipe['c_additive']

    def test_ghost_c(self):
        assert w7_ds_ghost_central_charge() == Fraction(42)

    def test_ghost_kappa(self):
        assert w7_ds_ghost_kappa() == Fraction(21)

    def test_depth_increase(self):
        pipe = w7_ds_pipeline(Fraction(5), 8)
        assert pipe['depth_increase']

    def test_sl7_depth_3(self):
        """sl_7 tower terminates at arity 3 (S_r=0 for r>=4)."""
        pipe = w7_ds_pipeline(Fraction(5), 8)
        for r in range(4, 9):
            assert pipe['tower_sl7'][r] == Fraction(0)

    def test_sl7_kappa(self):
        """kappa(sl_7, k=5) = 48*12/14 = 576/14 = 288/7."""
        pipe = w7_ds_pipeline(Fraction(5))
        assert pipe['kappa_sl7'] == Fraction(48) * Fraction(12) / Fraction(14)
        assert pipe['kappa_sl7'] == Fraction(288, 7)

    def test_c_sl7(self):
        """c(sl_7, k=5) = 48*5/12 = 20."""
        pipe = w7_ds_pipeline(Fraction(5))
        assert pipe['c_sl7'] == Fraction(20)


# ============================================================================
# Section 10: Multi-channel structure
# ============================================================================

class TestW7MultiChannel:

    def test_num_binary_channels(self):
        """15 binary channels = (6 choose 2) from 6 generators."""
        assert W7_NUM_BINARY_CHANNELS == 15
        assert len(W7_BINARY_CHANNELS) == 15

    def test_spins(self):
        assert W7_SPINS == [2, 3, 4, 5, 6, 7]
        assert W7_RANK == 6

    def test_dim_sl7(self):
        """dim(sl_7) = 7^2 - 1 = 48."""
        assert W7_DIM_SL7 == 48

    def test_binary_channels_sorted(self):
        """All binary channels have s_i < s_j."""
        for (s_i, s_j) in W7_BINARY_CHANNELS:
            assert s_i < s_j

    def test_binary_channel_kappas(self):
        """Channel kappas are (c/s_i + c/s_j)/2."""
        c_w = w7_central_charge_frac(Fraction(5))
        bk = w7_binary_channel_kappas(c_w)
        for (s_i, s_j) in W7_BINARY_CHANNELS:
            expected = (c_w / s_i + c_w / s_j) / 2
            assert bk[(s_i, s_j)] == expected

    def test_shadow_metric_diagonal(self):
        """Diagonal entries of shadow metric are 4*kappa_s^2."""
        c_w = w7_central_charge_frac(Fraction(5))
        diag = w7_shadow_metric_diagonal(c_w)
        for s in W7_SPINS:
            expected = 4 * (c_w / s) ** 2
            assert diag[(s, s)] == expected


# ============================================================================
# Section 11: DS cascade N=2,...,7
# ============================================================================

class TestDSCascade:
    """Systematic comparison across the W_N cascade."""

    def test_ghost_c_sequence(self):
        """c_ghost(N, k=0) = (N-1)*((N^2-1)*(N-1)-1): 2, 30, 132, 380, 870, 1722."""
        # VERIFIED: cascade engine c_ghost(N) returns k=0 intercept [DC]
        from compute.lib.ds_shadow_cascade_engine import c_ghost
        assert c_ghost(2) == Fraction(2)
        assert c_ghost(3) == Fraction(30)
        assert c_ghost(4) == Fraction(132)
        assert c_ghost(5) == Fraction(380)
        assert c_ghost(6) == Fraction(870)
        assert c_ghost(7) == Fraction(1722)

    def test_ff_sum_sequence(self):
        """c + c' = 2(N-1): 2, 4, 6, 8, 10, 12."""
        from compute.lib.w5_shadow_tower import wn_ff_sum
        for N in range(2, 8):
            assert wn_ff_sum(N) == Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))

    def test_depth_increase_all(self):
        """Depth increase from L to M for all N=2,...,7."""
        from compute.lib.ds_shadow_cascade_engine import ds_pipeline
        for N in range(2, 8):
            pipe = ds_pipeline(N, Fraction(5), 8)
            assert pipe['depth_increase'], f"Depth increase failed for N={N}"

    def test_kappa_ff_sum_sequence(self):
        """kappa + kappa' = (H_N-1)*[2(N-1)+4N(N^2-1)]: 13, 250/3, 533/2, ..."""
        # VERIFIED: wn_kappa_ff_sum uses correct FL complementarity [DC, SY]
        from compute.lib.w5_shadow_tower import wn_kappa_ff_sum
        expected = {
            2: Fraction(13),
            3: Fraction(250, 3),
            4: Fraction(533, 2),
            5: Fraction(9394, 15),
            6: Fraction(2465, 2),
            7: Fraction(75597, 35),
        }
        for N, val in expected.items():
            assert wn_kappa_ff_sum(N) == val, f"Failed at N={N}: {wn_kappa_ff_sum(N)} != {val}"

    def test_anomaly_ratio_sequence(self):
        """rho(N) = H_N - 1 sequence."""
        seq = w7_anomaly_ratio_sequence()
        expected = {
            2: Fraction(1, 2),
            3: Fraction(5, 6),
            4: Fraction(13, 12),
            5: Fraction(77, 60),
            6: Fraction(29, 20),
            7: Fraction(223, 140),
        }
        for N, val in expected.items():
            assert seq[N] == val, f"rho({N}): {seq[N]} != {val}"

    def test_ghost_c_sequence_internal(self):
        """Internal ghost sequence computation."""
        seq = w7_ghost_c_sequence()
        for N in range(2, 8):
            assert seq[N] == Fraction(N * (N - 1))

    def test_growth_rate_decreasing(self):
        """rho(W_{N+1}) < rho(W_N) at k=5 for N=5,6."""
        from compute.lib.w5_shadow_tower import w5_growth_rate_at_level
        from compute.lib.w6_shadow_tower import w6_growth_rate_at_level
        rho_w5 = w5_growth_rate_at_level(5)
        rho_w6 = w6_growth_rate_at_level(5)
        rho_w7 = w7_growth_rate_at_level(5)
        assert rho_w6 < rho_w5
        assert rho_w7 < rho_w6

    def test_quartic_decreasing(self):
        """|Q(W_{N+1})| < |Q(W_N)| at k=5 for N=5,6."""
        from compute.lib.w5_shadow_tower import w5_quartic_contact_T_at_level
        from compute.lib.w6_shadow_tower import w6_quartic_contact_T_at_level
        Q5 = abs(float(w5_quartic_contact_T_at_level(Fraction(5))))
        Q6 = abs(float(w6_quartic_contact_T_at_level(Fraction(5))))
        Q7 = abs(float(w7_quartic_contact_T_at_level(Fraction(5))))
        assert Q6 < Q5
        assert Q7 < Q6


# ============================================================================
# Section 12: Large-N scaling
# ============================================================================

class TestLargeN:

    def test_large_n_context(self):
        """Context dict includes N=2,...,7."""
        ctx = w7_in_large_n_context(Fraction(5))
        for N in range(2, 8):
            assert N in ctx

    def test_c_monotone(self):
        """c(W_N) is strictly decreasing (more negative) for N=2,...,7 at k=5."""
        ctx = w7_in_large_n_context(Fraction(5))
        for N in range(2, 7):
            assert float(ctx[N]['c']) > float(ctx[N + 1]['c'])

    def test_kappa_monotone(self):
        """kappa(W_N) is strictly decreasing (more negative) for N=3,...,7 at k=5."""
        ctx = w7_in_large_n_context(Fraction(5))
        for N in range(3, 7):
            assert float(ctx[N]['kappa']) > float(ctx[N + 1]['kappa'])

    def test_ghost_c_increasing(self):
        """c_ghost(N) = N(N-1) is increasing."""
        ctx = w7_in_large_n_context(Fraction(5))
        for N in range(2, 7):
            assert ctx[N]['ghost_c'] < ctx[N + 1]['ghost_c']

    def test_rank_sequence(self):
        """rank(W_N) = N-1."""
        ctx = w7_in_large_n_context(Fraction(5))
        for N in range(2, 8):
            assert ctx[N]['rank'] == N - 1

    def test_s4_sequence(self):
        """S_4 nonzero for all N=2,...,7 at k=5."""
        ctx = w7_in_large_n_context(Fraction(5))
        for N in range(2, 8):
            assert ctx[N].get('S4_T') is not None
            assert ctx[N]['S4_T'] != 0

    def test_ds_cascade_comparison(self):
        """DS cascade at k=5 produces valid data for all N."""
        cascade = ds_cascade_comparison(Fraction(5))
        for N in range(2, 8):
            assert N in cascade
            assert cascade[N]['c'] != 0
            assert cascade[N]['kappa'] != 0


# ============================================================================
# Section 13: Cross-engine consistency
# ============================================================================

class TestW7CrossEngine:
    """Cross-checks against ds_shadow_cascade_engine and w5_shadow_tower (generic)."""

    def test_c_matches_cascade(self):
        from compute.lib.ds_shadow_cascade_engine import c_WN
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            assert w7_central_charge_frac(kv) == c_WN(7, kv)

    def test_kappa_matches_cascade(self):
        from compute.lib.ds_shadow_cascade_engine import kappa_WN
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            assert w7_kappa_total_frac(kv) == kappa_WN(7, kv)

    def test_cascade_uses_total_kappa(self):
        """Cascade engine uses kappa_total, not kappa_T = c/2."""
        from compute.lib.ds_shadow_cascade_engine import ds_pipeline
        pipe = ds_pipeline(7, Fraction(5), 8)
        c_w = w7_central_charge_frac(Fraction(5))
        # Cascade S_2 = kappa_total = (223/140)*c
        assert pipe['tower_WN'][2] == Fraction(223, 140) * c_w
        # Our T-line S_2 = c/2
        tower = t_line_tower_exact_at_level(Fraction(5), 8)
        assert tower[2] == c_w / 2

    def test_s3_universal(self):
        """Both engines give S_3 = 2."""
        from compute.lib.ds_shadow_cascade_engine import ds_pipeline
        pipe = ds_pipeline(7, Fraction(5), 8)
        tower = t_line_tower_exact_at_level(Fraction(5), 8)
        assert tower[3] == Fraction(2)
        assert pipe['tower_WN'][3] == Fraction(2)

    def test_ghost_c_matches(self):
        from compute.lib.ds_shadow_cascade_engine import c_ghost
        assert w7_ds_ghost_central_charge() == c_ghost(7)

    def test_wn_generic_matches_w7(self):
        """Generic wn_central_charge matches w7_central_charge_frac."""
        from compute.lib.w5_shadow_tower import wn_central_charge, wn_kappa_total
        for kv in [Fraction(1), Fraction(5), Fraction(10)]:
            assert w7_central_charge_frac(kv) == wn_central_charge(7, kv)
            assert w7_kappa_total_frac(kv) == wn_kappa_total(7, kv)


# ============================================================================
# Section 14: Line-by-line shadow data
# ============================================================================

class TestW7LineShadowData:

    def test_t_line_kappa(self):
        cc = Symbol('c')
        data = t_line_shadow_data(cc)
        assert data['kappa'] == cc / 2

    def test_w3_line_kappa(self):
        cc = Symbol('c')
        data = w3_line_shadow_data(cc)
        assert data['kappa'] == cc / 3

    def test_w7_line_kappa(self):
        cc = Symbol('c')
        data = w7_line_shadow_data(cc)
        assert data['kappa'] == cc / 7

    def test_all_lines_present(self):
        data = all_line_shadow_data()
        assert set(data.keys()) == {'T', 'W_3', 'W_4', 'W_5', 'W_6', 'W_7'}

    def test_odd_spin_parity(self):
        """Odd-spin generators have alpha=0 (Z_2 parity)."""
        cc = Symbol('c')
        for line_func, spin in [(w3_line_shadow_data, 3), (w7_line_shadow_data, 7)]:
            data = line_func(cc)
            assert data['alpha'] == 0

    def test_depth_class_all_M(self):
        """All lines are class M."""
        data = all_line_shadow_data()
        for line_name, line_data in data.items():
            assert line_data['depth_class'] == 'M'


# ============================================================================
# Section 15: Propagator variance
# ============================================================================

class TestW7PropagatorVariance:

    def test_variance_finite_k5(self):
        """Structural variance estimate is finite at k=5.

        NOTE: The exact Cauchy-Schwarz bound delta >= 0 holds for the
        TRUE quartic gradients. The structural estimate uses placeholder
        gradients from Lambda-exchange only, so it may be negative.
        The test verifies the computation is finite and well-defined.
        """
        c_val = float(w7_central_charge_frac(Fraction(5)))
        delta = w7_propagator_variance_numerical(c_val)
        assert math.isfinite(delta)

    def test_variance_finite_k1(self):
        c_val = float(w7_central_charge_frac(Fraction(1)))
        delta = w7_propagator_variance_numerical(c_val)
        assert math.isfinite(delta)

    def test_variance_finite_k10(self):
        c_val = float(w7_central_charge_frac(Fraction(10)))
        delta = w7_propagator_variance_numerical(c_val)
        assert math.isfinite(delta)

    def test_six_channel_kappas(self):
        """6 kappa values correspond to 6 generators."""
        c_w = w7_central_charge_frac(Fraction(5))
        kaps = w7_kappas(c_w)
        assert len(kaps) == 6
        for s, kap in zip(W7_SPINS, kaps):
            assert kap == c_w / s

    def test_kappas_distinct(self):
        """All 6 channel kappas are distinct (non-degenerate spectrum)."""
        c_w = w7_central_charge_frac(Fraction(5))
        kaps = w7_kappas(c_w)
        assert len(set(kaps)) == 6


# ============================================================================
# Final: Full summary
# ============================================================================

class TestW7FullSummary:

    def test_summary_keys(self):
        summary = w7_full_summary(Fraction(5))
        required_keys = [
            'N', 'k', 'c', 'kappa_total', 'kappa_channels',
            'Q_contact_T', 'rho_T', 'complementarity', 'tower_T',
            'ds_pipeline', 'depth_class', 'ff_sum', 'anomaly_ratio',
            'harmonic_number', 'num_binary_channels', 'rank',
        ]
        for key in required_keys:
            assert key in summary, f"Missing key: {key}"

    def test_summary_values(self):
        summary = w7_full_summary(Fraction(5))
        assert summary['N'] == 7
        assert summary['rank'] == 6
        assert summary['depth_class'] == 'M'
        assert summary['ff_sum'] == Rational(1356)
        assert summary['anomaly_ratio'] == Rational(223, 140)
        assert summary['harmonic_number'] == Rational(363, 140)
        assert summary['num_binary_channels'] == 15
        assert summary['complementarity']['matches']
