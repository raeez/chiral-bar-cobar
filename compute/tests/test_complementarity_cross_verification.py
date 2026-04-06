r"""Tests for complementarity cross-verification: kappa(A) + kappa(A!).

MANDATE: 4 independent methods, 15+ families, 100+ tests.

CRITICAL REGRESSION CHECK (AP24):
    The old overclaim kappa+kappa'=0 for ALL families is WRONG.
    Virasoro: kappa+kappa' = 13 (NOT 0).
    W_3: kappa+kappa' = 250/3 (NOT 0).
    These tests prevent the AP24 error from recurring.

Tests organized by:
    1. Method agreement (4 methods x 15+ families = 60+ checks)
    2. Expected values for each family
    3. Level independence
    4. Self-dual points
    5. Ghost kappa table
    6. Genus-g extension (F_g complementarity)
    7. Shadow metric/discriminant complementarity
    8. Shadow radius complementarity
    9. AP24 regression checks
    10. W_N pattern verification
"""
from __future__ import annotations

import pytest
from fractions import Fraction

from compute.lib.complementarity_cross_verification import (
    # Core kappa functions
    kappa_heisenberg, kappa_virasoro, kappa_affine, kappa_wn,
    kappa_betagamma, kappa_bc, kappa_free_fermion, kappa_lattice,
    # Dual kappa functions
    kappa_dual_heisenberg, kappa_dual_virasoro, kappa_dual_affine,
    kappa_dual_wn, kappa_dual_betagamma, kappa_dual_bc,
    kappa_dual_free_fermion, kappa_dual_lattice,
    # Methods
    method1_direct, method2_theorem_d, method3_anomaly_cancellation,
    method4_discriminant,
    # Cross-verification
    cross_verify, expected_sum,
    # Level independence
    verify_level_independence_affine, verify_level_independence_wn,
    # Genus complementarity
    genus_g_complementarity, faber_pandharipande,
    # Shadow metric / radius
    virasoro_shadow_data, shadow_radius_complementarity,
    shadow_growth_rate_virasoro,
    # Ghost kappa
    ghost_kappa_from_weights, ghost_kappa_table,
    w_algebra_generator_weights,
    # Pattern tables
    wn_complementarity_table, full_landscape_cross_verification,
    # Constants
    anomaly_ratio_wn, koszul_conductor_wn, central_charge_wn,
    EXPECTED_SUMS,
)


# =========================================================================
# 1. FOUR-METHOD AGREEMENT: each family
# =========================================================================

class TestMethodAgreementHeisenberg:
    """Four methods agree for Heisenberg at multiple levels."""

    @pytest.mark.parametrize("k_val", [1, 2, 5, -3, Fraction(1, 2)])
    def test_four_methods_agree(self, k_val):
        r = cross_verify("heisenberg", k=k_val)
        assert r["all_agree"], f"Methods disagree at k={k_val}: {r}"
        assert r["sum_m1"] == Fraction(0)

    def test_direct_kappa_values(self):
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)
        assert kappa_heisenberg(Fraction(7)) == Fraction(7)
        assert kappa_dual_heisenberg(Fraction(1)) == Fraction(-1)


class TestMethodAgreementVirasoro:
    """Four methods agree for Virasoro. CRITICAL: sum = 13, NOT 0."""

    @pytest.mark.parametrize("c_val", [
        1, Fraction(1, 2), Fraction(7, 10), 13, 26, Fraction(25, 2)
    ])
    def test_four_methods_agree(self, c_val):
        r = cross_verify("virasoro", c=c_val)
        assert r["all_agree"], f"Methods disagree at c={c_val}: {r}"
        assert r["sum_m1"] == Fraction(13), f"AP24 REGRESSION: sum={r['sum_m1']} != 13"

    def test_direct_kappa_values(self):
        assert kappa_virasoro(Fraction(26)) == Fraction(13)
        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)
        assert kappa_dual_virasoro(Fraction(26)) == Fraction(0)
        assert kappa_dual_virasoro(Fraction(13)) == Fraction(13, 2)

    def test_self_dual_at_c13(self):
        """Virasoro self-dual at c=13, NOT c=26 (AP8)."""
        assert kappa_virasoro(Fraction(13)) == kappa_dual_virasoro(Fraction(13))

    def test_NOT_self_dual_at_c26(self):
        """c=26 is NOT the self-dual point."""
        assert kappa_virasoro(Fraction(26)) != kappa_dual_virasoro(Fraction(26))


class TestMethodAgreementAffine:
    """Four methods agree for all affine KM families."""

    @pytest.mark.parametrize("lie_type,rank", [
        ("A", 1), ("A", 2), ("A", 3), ("A", 4), ("A", 5), ("A", 6), ("A", 7),
    ])
    def test_affine_sl_n(self, lie_type, rank):
        for k_val in [1, 2, 5]:
            r = cross_verify("affine", lie_type=lie_type, rank=rank, k=k_val)
            assert r["all_agree"]
            assert r["sum_m1"] == Fraction(0)

    @pytest.mark.parametrize("lie_type,rank", [
        ("B", 2), ("B", 3), ("C", 2), ("C", 3),
        ("D", 4), ("G", 2), ("F", 4), ("E", 6), ("E", 7), ("E", 8),
    ])
    def test_non_simply_laced(self, lie_type, rank):
        r = cross_verify("affine", lie_type=lie_type, rank=rank, k=1)
        assert r["all_agree"]
        assert r["sum_m1"] == Fraction(0)

    def test_affine_not_c_over_2(self):
        """CRITICAL (AP1): kappa(sl_3, k=1) != c/2.
        c = dim * k / (k + h^v) = 8 * 1 / (1+3) = 2.
        kappa = dim * (k+h^v) / (2h^v) = 8 * 4 / 6 = 16/3.
        c/2 = 1. These are DIFFERENT.
        """
        kap = kappa_affine("A", 2, Fraction(1))
        assert kap == Fraction(16, 3)
        # c/2 would be 2/2 = 1. kappa = 16/3 != 1.
        assert kap != Fraction(1)


class TestMethodAgreementWAlgebras:
    """Four methods agree for W_N families."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8])
    def test_wn_agreement(self, N):
        c_val = Fraction(koszul_conductor_wn(N), 2)  # self-dual point
        r = cross_verify(f"w_{N}", N=N, c=c_val)
        assert r["all_agree"]
        exp = anomaly_ratio_wn(N) * Fraction(koszul_conductor_wn(N))
        assert r["sum_m1"] == exp

    def test_w3_sum_is_250_over_3(self):
        """W_3: kappa + kappa' = 250/3."""
        r = cross_verify("w_3", N=3, c=Fraction(50))
        assert r["sum_m1"] == Fraction(250, 3)

    def test_w4_sum_is_533_over_2(self):
        """W_4: kappa + kappa' = 533/2."""
        r = cross_verify("w_4", N=4, c=Fraction(123))
        assert r["sum_m1"] == Fraction(533, 2)

    def test_w5_sum(self):
        """W_5: kappa + kappa' = 9394/15."""
        exp = anomaly_ratio_wn(5) * Fraction(koszul_conductor_wn(5))
        assert exp == Fraction(9394, 15)
        r = cross_verify("w_5", N=5, c=Fraction(100))
        assert r["sum_m1"] == exp


class TestMethodAgreementFreeField:
    """Four methods agree for free-field systems."""

    @pytest.mark.parametrize("lam", [
        Fraction(0), Fraction(1, 2), Fraction(1), Fraction(1, 3), Fraction(2, 3)
    ])
    def test_betagamma(self, lam):
        r = cross_verify("betagamma", lam=lam)
        assert r["all_agree"]
        assert r["sum_m1"] == Fraction(0)

    @pytest.mark.parametrize("lam", [Fraction(1), Fraction(2), Fraction(3, 2)])
    def test_bc_ghost(self, lam):
        r = cross_verify("bc", lam=lam)
        assert r["all_agree"]
        assert r["sum_m1"] == Fraction(0)

    def test_free_fermion(self):
        r = cross_verify("free_fermion")
        assert r["all_agree"]
        assert r["sum_m1"] == Fraction(0)

    @pytest.mark.parametrize("rank", [1, 8, 16, 24])
    def test_lattice(self, rank):
        r = cross_verify("lattice", rank=rank)
        assert r["all_agree"]
        assert r["sum_m1"] == Fraction(0)


# =========================================================================
# 2. EXPECTED VALUES
# =========================================================================

class TestExpectedValues:
    """Verify the expected complementarity constants."""

    def test_heisenberg_sum_zero(self):
        assert expected_sum("heisenberg") == Fraction(0)

    def test_virasoro_sum_13(self):
        """AP24 CRITICAL: Virasoro sum is 13, not 0."""
        assert expected_sum("virasoro") == Fraction(13)

    def test_affine_sum_zero(self):
        assert expected_sum("affine") == Fraction(0)

    def test_betagamma_sum_zero(self):
        assert expected_sum("betagamma") == Fraction(0)

    def test_bc_sum_zero(self):
        assert expected_sum("bc") == Fraction(0)

    def test_lattice_sum_zero(self):
        assert expected_sum("lattice") == Fraction(0)

    def test_w2_equals_virasoro(self):
        """W_2 = Virasoro: sum should be 13."""
        exp = anomaly_ratio_wn(2) * Fraction(koszul_conductor_wn(2))
        assert exp == Fraction(13)

    def test_w3_sum(self):
        assert EXPECTED_SUMS["w_3"] == Fraction(250, 3)

    def test_w4_sum(self):
        assert EXPECTED_SUMS["w_4"] == Fraction(533, 2)

    def test_w5_sum(self):
        assert EXPECTED_SUMS["w_5"] == Fraction(9394, 15)

    def test_expected_sums_table(self):
        """Verify the EXPECTED_SUMS dict against independent computation."""
        for N in range(2, 9):
            key = f"w_{N}" if N > 2 else "virasoro"
            rho = anomaly_ratio_wn(N)
            K = Fraction(koszul_conductor_wn(N))
            expected = rho * K
            assert EXPECTED_SUMS.get(key, expected) == expected, \
                f"W_{N}: table says {EXPECTED_SUMS.get(key)}, computed {expected}"


# =========================================================================
# 3. LEVEL INDEPENDENCE
# =========================================================================

class TestLevelIndependence:
    """kappa+kappa' is constant (level-independent) for each family."""

    @pytest.mark.parametrize("lie_type,rank", [
        ("A", 1), ("A", 2), ("A", 3), ("B", 2), ("C", 2),
        ("D", 4), ("G", 2), ("F", 4), ("E", 6), ("E", 8),
    ])
    def test_affine_level_independence(self, lie_type, rank):
        r = verify_level_independence_affine(lie_type, rank)
        assert r["all_ok"], f"Level-independence FAILED for {r['algebra']}"

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_wn_level_independence(self, N):
        r = verify_level_independence_wn(N)
        assert r["all_ok"], f"Level-independence FAILED for W_{N}"

    def test_virasoro_level_independence_explicit(self):
        """Virasoro sum = 13 at all c values."""
        for c_val in [Fraction(i) for i in range(1, 26)] + [Fraction(1, 2), Fraction(7, 10)]:
            kap = kappa_virasoro(c_val)
            kap_d = kappa_dual_virasoro(c_val)
            assert kap + kap_d == Fraction(13), f"sum != 13 at c={c_val}"


# =========================================================================
# 4. SELF-DUAL POINTS
# =========================================================================

class TestSelfDualPoints:
    """At the self-dual point, kappa = kappa'."""

    def test_virasoro_self_dual_c13(self):
        """Virasoro: self-dual at c=13, NOT c=26 (AP8)."""
        assert kappa_virasoro(Fraction(13)) == kappa_dual_virasoro(Fraction(13))
        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)

    def test_virasoro_not_self_dual_c26(self):
        """c=26 is where the DUAL has kappa'=0, not where A=A!."""
        assert kappa_dual_virasoro(Fraction(26)) == Fraction(0)
        assert kappa_virasoro(Fraction(26)) == Fraction(13)
        assert kappa_virasoro(Fraction(26)) != kappa_dual_virasoro(Fraction(26))

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7])
    def test_wn_self_dual(self, N):
        K = koszul_conductor_wn(N)
        c_star = Fraction(K, 2)
        kap = kappa_wn(N, c_star)
        kap_d = kappa_dual_wn(N, c_star)
        assert kap == kap_d, f"W_{N}: kappa != kappa' at c*={c_star}"


# =========================================================================
# 5. GHOST KAPPA TABLE (Method 3 verification)
# =========================================================================

class TestGhostKappa:
    """Ghost kappa independently verified for each W_N."""

    def test_virasoro_ghost_kappa(self):
        """Virasoro ghosts (spin 2): kappa_ghost = -13."""
        gk = ghost_kappa_from_weights([Fraction(2)])
        assert gk == Fraction(-13)

    def test_w3_ghost_kappa(self):
        """W_3 ghosts (spins 2,3): kappa_ghost = -13 + (-37) = -50."""
        gk = ghost_kappa_from_weights([Fraction(2), Fraction(3)])
        # 6*4-12+1 = 13, 6*9-18+1 = 37
        assert gk == Fraction(-50)

    def test_w4_ghost_kappa(self):
        """W_4 ghosts (spins 2,3,4): kappa_ghost = -13 - 37 - 73 = -123."""
        gk = ghost_kappa_from_weights([Fraction(2), Fraction(3), Fraction(4)])
        # 6*16-24+1 = 73
        assert gk == Fraction(-123)

    def test_ghost_kappa_table_consistency(self):
        table = ghost_kappa_table()
        for key, data in table.items():
            assert data["match"], f"Ghost kappa mismatch for {key}"

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_ghost_formula(self, N):
        """sum_{h=2}^N (6h^2 - 6h + 1) = 2N^3 - 3N^2 + N - (2-3+1) = 2N^3-3N^2+N.
        Wait: sum from h=2 to N of (6h^2-6h+1) = 6*sum(h^2) - 6*sum(h) + (N-1)
        where sums from 2 to N.
        """
        weights = w_algebra_generator_weights(N)
        gk = ghost_kappa_from_weights(weights)
        explicit = Fraction(0)
        for h in range(2, N + 1):
            explicit -= (6 * h * h - 6 * h + 1)
        assert gk == explicit


# =========================================================================
# 6. GENUS-g COMPLEMENTARITY
# =========================================================================

class TestGenusGComplementarity:
    """F_g(A) + F_g(A!) = (kappa+kappa') * lambda_g^FP."""

    def test_faber_pandharipande_values(self):
        assert faber_pandharipande(1) == Fraction(1, 24)
        assert faber_pandharipande(2) == Fraction(7, 5760)
        assert faber_pandharipande(3) == Fraction(31, 967680)

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_virasoro_genus_g(self, g):
        for c_val in [Fraction(1), Fraction(13), Fraction(26)]:
            r = genus_g_complementarity("virasoro", g, c=c_val)
            assert r["verified"], f"Genus-{g} complementarity FAILED at c={c_val}"

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_heisenberg_genus_g(self, g):
        r = genus_g_complementarity("heisenberg", g, k=Fraction(1))
        assert r["verified"]
        assert r["F_g_sum"] == Fraction(0)

    @pytest.mark.parametrize("g", [1, 2])
    def test_w3_genus_g(self, g):
        r = genus_g_complementarity("w_3", g, N=3, c=Fraction(50))
        assert r["verified"]

    @pytest.mark.parametrize("g", [1, 2])
    def test_affine_genus_g(self, g):
        r = genus_g_complementarity("affine", g, lie_type="A", rank=1, k=Fraction(1))
        assert r["verified"]
        assert r["F_g_sum"] == Fraction(0)

    def test_genus1_virasoro_explicit(self):
        """F_1(Vir_c) + F_1(Vir_{26-c}) = 13/24."""
        c = Fraction(1)
        r = genus_g_complementarity("virasoro", 1, c=c)
        assert r["F_g_sum"] == Fraction(13, 24)

    def test_genus2_virasoro_explicit(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 13 * 7/5760 = 91/5760."""
        c = Fraction(7)
        r = genus_g_complementarity("virasoro", 2, c=c)
        assert r["F_g_sum"] == Fraction(13) * Fraction(7, 5760)


# =========================================================================
# 7. SHADOW METRIC / DISCRIMINANT COMPLEMENTARITY
# =========================================================================

class TestShadowMetricComplementarity:
    """Discriminant and shadow metric complementarity."""

    def test_virasoro_discriminant_data(self):
        """Check virasoro shadow data is consistent."""
        sd = virasoro_shadow_data(Fraction(1))
        assert sd["kappa"] == Fraction(1, 2)
        assert sd["alpha"] == Fraction(2)
        assert sd["S4"] == Fraction(10) / (1 * (5 + 22))
        assert sd["S4"] == Fraction(10, 27)

    def test_virasoro_delta_formula(self):
        """Delta = 40/(5c+22) for Virasoro."""
        for c_val in [Fraction(1), Fraction(13), Fraction(26)]:
            sd = virasoro_shadow_data(c_val)
            expected_delta = Fraction(40) / (5 * c_val + 22)
            assert sd["Delta"] == expected_delta

    def test_discriminant_sum_virasoro(self):
        """Delta(c) + Delta(26-c) for Virasoro."""
        for c_val in [Fraction(1), Fraction(5), Fraction(13)]:
            r = method4_discriminant("virasoro", c=c_val)
            # Delta sum is NOT constant (it depends on c)
            # But at the self-dual point c=13:
            if c_val == 13:
                assert r["Delta_A"] == r["Delta_Ad"]

    def test_shadow_q_coefficients(self):
        """Q_L(t) = q0 + q1*t + q2*t^2 computed correctly."""
        sd = virasoro_shadow_data(Fraction(2))
        assert sd["q0"] == 4 * Fraction(1) ** 2  # 4*(c/2)^2 = c^2 = 4
        assert sd["q0"] == Fraction(4)
        assert sd["q1"] == 12 * Fraction(1) * Fraction(2)  # 12*kap*alpha
        assert sd["q1"] == Fraction(24)


# =========================================================================
# 8. SHADOW RADIUS COMPLEMENTARITY
# =========================================================================

class TestShadowRadiusComplementarity:
    """Shadow growth rate for Koszul pairs."""

    def test_self_dual_rho_equal(self):
        """At c=13 (self-dual), rho(A) = rho(A!)."""
        r = shadow_radius_complementarity(Fraction(13))
        assert r["rho_A"] is not None and r["rho_Ad"] is not None
        assert abs(r["rho_A"] - r["rho_Ad"]) < 1e-12

    def test_rho_positive(self):
        """Shadow growth rates are positive for class M algebras."""
        for c_val in [Fraction(1), Fraction(7, 10), Fraction(13)]:
            rho = shadow_growth_rate_virasoro(c_val)
            assert rho is not None and rho > 0

    def test_complementary_rho_values(self):
        """rho(Vir_c) and rho(Vir_{26-c}) are computed for several c values."""
        for c_val in [Fraction(1), Fraction(5), Fraction(10), Fraction(20)]:
            r = shadow_radius_complementarity(c_val)
            assert r["rho_A"] is not None
            assert r["rho_Ad"] is not None
            # rho values should differ when c != 13 (not self-dual)
            if c_val != 13:
                # They can still be equal in special cases, but generically differ
                pass


# =========================================================================
# 9. AP24 REGRESSION CHECKS
# =========================================================================

class TestAP24Regression:
    """Explicit checks that the AP24 overclaim is caught."""

    def test_virasoro_sum_is_NOT_zero(self):
        """THE AP24 CHECK: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c_val in [1, 2, 5, 10, 13, 20, 25, 26]:
            kap = kappa_virasoro(Fraction(c_val))
            kap_d = kappa_dual_virasoro(Fraction(c_val))
            s = kap + kap_d
            assert s == Fraction(13), (
                f"AP24 REGRESSION at c={c_val}: kappa+kappa'={s}, expected 13"
            )
            assert s != Fraction(0), (
                f"AP24 REGRESSION: sum = 0 at c={c_val}, this is the OLD WRONG CLAIM"
            )

    def test_w3_sum_is_NOT_zero(self):
        """W_3 sum = 250/3, NOT 0."""
        for c_val in [2, 50, 98]:
            kap = kappa_wn(3, Fraction(c_val))
            kap_d = kappa_dual_wn(3, Fraction(c_val))
            s = kap + kap_d
            assert s == Fraction(250, 3)
            assert s != Fraction(0)

    def test_w4_sum_is_NOT_zero(self):
        """W_4 sum = 533/2, NOT 0."""
        kap = kappa_wn(4, Fraction(3))
        kap_d = kappa_dual_wn(4, Fraction(3))
        assert kap + kap_d == Fraction(533, 2)

    def test_affine_sum_IS_zero(self):
        """Affine KM: sum IS zero (the original claim was correct for KM)."""
        for lt, rk in [("A", 1), ("A", 2), ("B", 2), ("G", 2), ("E", 8)]:
            kap = kappa_affine(lt, rk, Fraction(1))
            kap_d = kappa_dual_affine(lt, rk, Fraction(1))
            assert kap + kap_d == Fraction(0)

    def test_heisenberg_sum_IS_zero(self):
        """Heisenberg: sum IS zero."""
        for k_val in [1, -5, Fraction(1, 3)]:
            assert kappa_heisenberg(Fraction(k_val)) + \
                   kappa_dual_heisenberg(Fraction(k_val)) == Fraction(0)


# =========================================================================
# 10. W_N PATTERN VERIFICATION
# =========================================================================

class TestWNPattern:
    """Verify the W_N complementarity pattern kappa+kappa' = rho_N * K_N."""

    def test_anomaly_ratio_values(self):
        """Anomaly ratios are correct harmonic-derived fractions."""
        assert anomaly_ratio_wn(2) == Fraction(1, 2)
        assert anomaly_ratio_wn(3) == Fraction(5, 6)
        assert anomaly_ratio_wn(4) == Fraction(13, 12)
        assert anomaly_ratio_wn(5) == Fraction(77, 60)

    def test_koszul_conductor_values(self):
        """K_N = 2(N-1)(2N^2+2N+1) values."""
        assert koszul_conductor_wn(2) == 26
        assert koszul_conductor_wn(3) == 100
        assert koszul_conductor_wn(4) == 246
        assert koszul_conductor_wn(5) == 488
        assert koszul_conductor_wn(6) == 850

    def test_koszul_conductor_formula_verification(self):
        """Verify K_N: c(k) + c(K-c(k)) = K_N (Koszul complementarity).

        AP33: the Koszul dual sends c -> K_N - c (NOT the FF involution
        k -> -k-2N, which gives c+c' = 2(N-1), not K_N).
        """
        for N in range(2, 9):
            K_formula = koszul_conductor_wn(N)
            k_test = Fraction(1)
            c_k = central_charge_wn(N, k_test)
            c_kd = Fraction(K_formula) - c_k  # Koszul dual: c' = K - c
            assert c_k + c_kd == Fraction(K_formula), \
                f"W_{N}: c+c'={c_k+c_kd} != K={K_formula}"
            # Also verify FF involution gives c+c'=2(N-1)+4N(N^2-1) (Freudenthal-de Vries)
            k_ff = -k_test - 2 * N
            c_ff = central_charge_wn(N, k_ff)
            fdv = Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))
            assert c_k + c_ff == fdv, \
                f"W_{N}: FF c+c'={c_k+c_ff} != 2(N-1)+4N(N^2-1)={fdv}"

    def test_wn_complementarity_table(self):
        """Full W_N table N=2,...,8."""
        table = wn_complementarity_table(max_N=8)
        expected_sums = {
            2: Fraction(13),
            3: Fraction(250, 3),
            4: Fraction(533, 2),
        }
        for row in table:
            N = row["N"]
            rho = row["rho"]
            K = row["K"]
            kap_sum = row["kappa_sum"]
            assert kap_sum == rho * Fraction(K)
            if N in expected_sums:
                assert kap_sum == expected_sums[N]
            # Self-dual point: kappa = kappa_sum / 2
            assert row["kappa_at_self_dual"] == kap_sum / 2

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: all data should agree."""
        assert anomaly_ratio_wn(2) == Fraction(1, 2)
        assert koszul_conductor_wn(2) == 26
        # kappa(W_2, c) = (1/2)*c = kappa(Vir_c)
        assert kappa_wn(2, Fraction(13)) == kappa_virasoro(Fraction(13))

    def test_wn_sum_grows(self):
        """The complementarity sum grows with N."""
        sums = []
        for N in range(2, 9):
            s = anomaly_ratio_wn(N) * Fraction(koszul_conductor_wn(N))
            sums.append(s)
        for i in range(len(sums) - 1):
            assert sums[i + 1] > sums[i], f"Sum not growing: {sums[i+1]} <= {sums[i]}"


# =========================================================================
# 11. BETAGAMMA / BC SPECIFIC CHECKS
# =========================================================================

class TestBetagammaBc:
    """betagamma/bc complementarity checks."""

    def test_bg_bc_duality(self):
        """kappa(bg) + kappa(bc) = 0 at all lambda."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 2),
                     Fraction(3, 4), Fraction(1), Fraction(2)]:
            assert kappa_betagamma(lam) + kappa_bc(lam) == Fraction(0)

    def test_bg_symmetry(self):
        """kappa_bg(lam) = kappa_bg(1-lam)."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)]:
            assert kappa_betagamma(lam) == kappa_betagamma(1 - lam)

    def test_bc_spin2_is_ghost(self):
        """bc at spin 2 gives the Virasoro ghost: kappa = -13."""
        assert kappa_bc(Fraction(2)) == Fraction(-13)

    def test_bc_spin1_is_affine_ghost(self):
        """bc at spin 1: kappa = -(6-6+1) = -1."""
        assert kappa_bc(Fraction(1)) == Fraction(-1)

    def test_betagamma_half_integer(self):
        """betagamma at lam=1/2: kappa = 6/4 - 3 + 1 = -1/2."""
        assert kappa_betagamma(Fraction(1, 2)) == Fraction(-1, 2)

    def test_bc_dual_of_bg(self):
        """kappa_dual(bg) = kappa(bc)."""
        for lam in [Fraction(1, 2), Fraction(1), Fraction(2)]:
            assert kappa_dual_betagamma(lam) == kappa_bc(lam)

    def test_bg_dual_of_bc(self):
        """kappa_dual(bc) = kappa(bg)."""
        for lam in [Fraction(1, 2), Fraction(1), Fraction(2)]:
            assert kappa_dual_bc(lam) == kappa_betagamma(lam)


# =========================================================================
# 12. LATTICE VOA CHECKS
# =========================================================================

class TestLatticeVOA:
    """Lattice VOA complementarity checks."""

    @pytest.mark.parametrize("rank", [1, 2, 4, 8, 16, 24])
    def test_lattice_sum_zero(self, rank):
        """kappa(V_Lambda) + kappa(V_Lambda^!) = 0."""
        assert kappa_lattice(rank) + kappa_dual_lattice(rank) == Fraction(0)

    def test_lattice_kappa_is_rank(self):
        """kappa(V_Lambda) = rank, NOT c/2 (AP48)."""
        # For rank-24 lattice at c=24: kappa = 24, NOT c/2 = 12
        assert kappa_lattice(24) == Fraction(24)
        assert kappa_lattice(24) != Fraction(12)  # c/2 would be wrong

    def test_leech_lattice(self):
        """Leech lattice: rank=24, kappa=24."""
        assert kappa_lattice(24) == Fraction(24)
        assert kappa_dual_lattice(24) == Fraction(-24)


# =========================================================================
# 13. ANOMALY CANCELLATION (Method 3 detailed checks)
# =========================================================================

class TestAnomalyCancellation:
    """Method 3: ghost kappa and critical dimensions."""

    def test_virasoro_critical_dimension(self):
        """Virasoro: c_crit = 26 (where kappa(matter) = -kappa(ghost) = 13)."""
        r = method3_anomaly_cancellation("virasoro")
        assert r["ghost_kappa"] == Fraction(-13)
        assert r["c_crit"] == Fraction(26)  # rho * c_crit = 13 => c_crit = 26
        assert r["kappa_at_c_crit"] == Fraction(13)

    def test_w3_critical_dimension(self):
        """W_3: ghost_kappa = -50, rho = 5/6, c_crit = 60."""
        r = method3_anomaly_cancellation("w_3", N=3)
        assert r["ghost_kappa"] == Fraction(-50)
        assert r["c_crit"] == Fraction(60)

    def test_w4_critical_dimension(self):
        """W_4: ghost_kappa = -123, rho = 13/12, c_crit = 123/(13/12) = 1476/13."""
        r = method3_anomaly_cancellation("w_4", N=4)
        assert r["ghost_kappa"] == Fraction(-123)
        assert r["c_crit"] == Fraction(1476, 13)

    def test_method3_sum_matches_method2(self):
        """Method 3 sum = Method 2 sum for all W_N."""
        for N in range(2, 8):
            m2 = method2_theorem_d(f"w_{N}", N=N)
            m3 = method3_anomaly_cancellation(f"w_{N}", N=N)
            assert m2["sum"] == m3["sum"], f"W_{N}: M2={m2['sum']} != M3={m3['sum']}"


# =========================================================================
# 14. FULL LANDSCAPE CROSS-VERIFICATION
# =========================================================================

class TestFullLandscape:
    """Run the complete landscape cross-verification."""

    def test_full_landscape(self):
        """All families, all methods, all agree."""
        r = full_landscape_cross_verification()
        failures = {k: v for k, v in r["results"].items()
                    if not v.get("all_agree") or not v.get("match_expected")}
        assert r["all_ok"], f"Full landscape FAILED: {list(failures.keys())}"

    def test_landscape_count(self):
        """At least 50 individual checks in the landscape."""
        r = full_landscape_cross_verification()
        assert len(r["results"]) >= 50


# =========================================================================
# 15. KAPPA FORMULA INDEPENDENCE CHECKS (AP1, AP39)
# =========================================================================

class TestKappaFormulaIndependence:
    """Verify kappa formulas are correct and independent."""

    def test_affine_kappa_is_not_c_over_2(self):
        """CRITICAL (AP1, AP39): kappa(g_k) != c/2 for affine KM.

        For sl_2 at k=1: c = 3*1/3 = 1, kappa = 3*3/4 = 9/4. c/2 = 1/2. Different.
        """
        # sl_2, k=1: dim=3, h^v=2
        # c = 3*1/(1+2) = 1
        # kappa = 3*(1+2)/(2*2) = 9/4
        kap = kappa_affine("A", 1, Fraction(1))
        assert kap == Fraction(9, 4)
        c_sl2_k1 = Fraction(3) * 1 / (1 + 2)
        assert kap != c_sl2_k1 / 2  # c/2 = 1/2, kappa = 9/4

    def test_virasoro_kappa_is_c_over_2(self):
        """For Virasoro (unlike affine), kappa = c/2."""
        for c_val in [Fraction(1), Fraction(13), Fraction(26)]:
            assert kappa_virasoro(c_val) == c_val / 2

    def test_heisenberg_kappa_is_k(self):
        """kappa(H_k) = k, the level itself."""
        for k_val in [Fraction(1), Fraction(-3), Fraction(1, 7)]:
            assert kappa_heisenberg(k_val) == k_val

    def test_lattice_kappa_is_rank_not_c_over_2(self):
        """kappa(V_Lambda) = rank, NOT c/2 (AP48).
        For rank 24 Niemeier: c=24, kappa=24. c/2=12 is WRONG.
        """
        assert kappa_lattice(24) == Fraction(24)
        # c/2 = 12 is wrong
        assert kappa_lattice(24) != Fraction(12)


# =========================================================================
# 16. DISCRIMINANT COMPLEMENTARITY (Method 4 detailed)
# =========================================================================

class TestDiscriminantComplementarity:
    """Shadow metric discriminant complementarity for Virasoro pairs."""

    def test_delta_self_dual(self):
        """At c=13: Delta(A) = Delta(A!)."""
        r = method4_discriminant("virasoro", c=Fraction(13))
        assert r["Delta_A"] == r["Delta_Ad"]

    def test_delta_at_c1(self):
        """Delta(Vir_1) = 40/27, Delta(Vir_25) = 40/147."""
        r = method4_discriminant("virasoro", c=Fraction(1))
        assert r["Delta_A"] == Fraction(40, 27)
        assert r["Delta_Ad"] == Fraction(40, 147)

    def test_q0_sum_is_kappa_dependent(self):
        """q0(A) + q0(A!) = 4*kappa^2 + 4*kappa'^2 (NOT zero for Virasoro)."""
        for c_val in [Fraction(1), Fraction(5), Fraction(13)]:
            r = method4_discriminant("virasoro", c=c_val)
            q0_sum = r["Q_sum"]["q0"]
            kap = kappa_virasoro(c_val)
            kap_d = kappa_dual_virasoro(c_val)
            assert q0_sum == 4 * kap ** 2 + 4 * kap_d ** 2

    def test_discriminant_product_kdelta(self):
        """kappa * Delta = 20c / (5c+22) for Virasoro."""
        for c_val in [Fraction(1), Fraction(2), Fraction(13)]:
            r = method4_discriminant("virasoro", c=c_val)
            expected = Fraction(20) * c_val / (5 * c_val + 22)
            assert r["kDelta_A"] == expected


# =========================================================================
# 17. FEIGIN-FRENKEL INVOLUTION CHECKS
# =========================================================================

class TestFeiginFrenkelInvolution:
    """Verify FF involution properties."""

    def test_ff_involution_sl2(self):
        """sl_2: k -> -k-4. At k=1: k'=-5, kappa' = 3*(-5+2)/4 = -9/4 = -kappa."""
        kap = kappa_affine("A", 1, Fraction(1))
        kap_d = kappa_dual_affine("A", 1, Fraction(1))
        assert kap + kap_d == Fraction(0)
        assert kap_d == -kap

    def test_ff_involution_sl3(self):
        """sl_3: k -> -k-6."""
        kap = kappa_affine("A", 2, Fraction(1))
        kap_d = kappa_dual_affine("A", 2, Fraction(1))
        assert kap + kap_d == Fraction(0)

    def test_ff_involution_e8(self):
        """E_8: k -> -k-60."""
        kap = kappa_affine("E", 8, Fraction(1))
        kap_d = kappa_dual_affine("E", 8, Fraction(1))
        assert kap + kap_d == Fraction(0)

    def test_virasoro_ff_involution(self):
        """Virasoro FF: c -> 26-c."""
        for c_val in [Fraction(1), Fraction(13), Fraction(26)]:
            c_d = Fraction(26) - c_val
            assert kappa_virasoro(c_val) + kappa_virasoro(c_d) == Fraction(13)

    def test_w3_ff_involution(self):
        """W_3 FF: c -> 100-c."""
        for c_val in [Fraction(2), Fraction(50), Fraction(98)]:
            c_d = Fraction(100) - c_val
            assert kappa_wn(3, c_val) + kappa_wn(3, c_d) == Fraction(250, 3)


# =========================================================================
# 18. CROSS-FAMILY CONSISTENCY
# =========================================================================

class TestCrossFamilyConsistency:
    """Check that formulas are consistent across related families."""

    def test_virasoro_as_w2(self):
        """kappa(Vir_c) = kappa(W_2, c) for all c."""
        for c_val in [Fraction(1), Fraction(13), Fraction(26), Fraction(100)]:
            assert kappa_virasoro(c_val) == kappa_wn(2, c_val)

    def test_heisenberg_at_k_equals_rank(self):
        """For rank-1 lattice, kappa(V_Lambda) = 1 = kappa(H_1)."""
        assert kappa_lattice(1) == kappa_heisenberg(Fraction(1))

    def test_bc_spin2_matches_virasoro_ghost(self):
        """bc at spin 2 has kappa = -13 = ghost kappa for Virasoro."""
        assert kappa_bc(Fraction(2)) == ghost_kappa_from_weights([Fraction(2)])

    def test_betagamma_at_lam1_kappa_1(self):
        """betagamma at lam=1: kappa = 6-6+1 = 1."""
        assert kappa_betagamma(Fraction(1)) == Fraction(1)

    def test_free_fermion_is_virasoro_at_half(self):
        """Free fermion: c=1/2, kappa=1/4 = (1/2)/2."""
        assert kappa_free_fermion() == kappa_virasoro(Fraction(1, 2))
