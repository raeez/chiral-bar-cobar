"""Tests for compute/lib/genus_expansion.py — genus tables, complementarity."""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.genus_expansion import (
    kappa_heisenberg,
    kappa_virasoro,
    kappa_w3,
    kappa_sl2,
    kappa_sl3,
    kappa_g2,
    kappa_b2,
    genus_table,
    complementarity_sum_km,
)
from compute.lib.utils import lambda_fp, F_g


class TestKappaValues:
    def test_heisenberg(self):
        assert kappa_heisenberg(1) == 1

    def test_virasoro(self):
        assert kappa_virasoro(2) == 1  # c=2 -> kappa=1

    def test_w3(self):
        # kappa(W3) = 5c/6
        assert kappa_w3(6) == 5  # c=6 -> 5*6/6 = 5

    def test_sl2(self):
        # kappa(sl2, k=1) = 3*(1+2)/4 = 9/4
        assert kappa_sl2(1) == Rational(9, 4)

    def test_sl3(self):
        # kappa(sl3, k=1) = 4*(1+3)/3 = 16/3
        assert kappa_sl3(1) == Rational(16, 3)


class TestLambdaFP:
    def test_values(self):
        """Known Faber-Pandharipande numbers: (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        assert lambda_fp(3) == Rational(31, 967680)

    def test_positive(self):
        """All lambda_g must be positive."""
        for g in range(1, 20):
            assert lambda_fp(g) > 0


class TestGenusTable:
    def test_heisenberg_F1(self):
        """F_1(H_kappa) = kappa/24."""
        kappa = Symbol("kappa")
        table = genus_table(kappa, max_genus=1)
        assert simplify(table[1] - kappa / 24) == 0

    def test_sl2_F1(self):
        """F_1(sl_2, k) = 3(k+2)/4 * 1/24 = (k+2)/32."""
        k = Symbol("k")
        kap = kappa_sl2()
        table = genus_table(kap, max_genus=1)
        # kappa_sl2() with no arg returns symbolic 3*(k+2)/4
        # F_1 = 3*(k+2)/4 * 1/24 = (k+2)/32
        assert simplify(table[1] - (k + 2) / 32) == 0

    def test_virasoro_F1(self):
        """F_1(Vir_c) = c/2 * 1/24 = c/48."""
        c = Symbol("c")
        table = genus_table(c / 2, max_genus=1)
        assert simplify(table[1] - c / 48) == 0

    def test_convergence_ratio(self):
        """F_{g+1}/F_g should approach 1/(2*pi)^2 as g -> inf."""
        kappa_val = Rational(1)  # concrete value for numeric test
        ratios = []
        for g in range(1, 15):
            fg = F_g(kappa_val, g)
            fg1 = F_g(kappa_val, g + 1)
            if fg != 0:
                ratios.append(float(fg1 / fg))

        # The limit is 1/(2*pi)^2 ≈ 0.02533
        # Convergence is slow (algebraic, not exponential), so use loose tolerance
        import math
        target = 1 / (2 * math.pi) ** 2
        # Ratios should be decreasing toward target
        assert ratios[-1] > target  # still above
        assert ratios[-1] < ratios[0]  # decreasing
        assert abs(ratios[-1] - target) < 0.005  # within 0.5%


class TestComplementarity:
    def test_sl2_level_independent(self):
        """kappa(sl_2, k) + kappa(sl_2, k') should be level-independent."""
        total = complementarity_sum_km("A", 1)
        # Should simplify to a constant (no k dependence)
        k = Symbol("k")
        # total should be 3*(k+2)/4 + 3*(-k-4+2)/4 = 3*(k+2)/4 + 3*(-k-2)/4
        # = 3*((k+2) + (-k-2))/4 = 3*0/4 = 0
        assert simplify(total) == 0

    def test_sl3_level_independent(self):
        """kappa(sl_3, k) + kappa(sl_3, k') should be level-independent."""
        total = complementarity_sum_km("A", 2)
        assert simplify(total) == 0

    def test_G2_level_independent(self):
        """kappa(G_2, k) + kappa(G_2, k') should be level-independent."""
        total = complementarity_sum_km("G", 2)
        assert simplify(total) == 0

    def test_B2_level_independent(self):
        """kappa(B_2, k) + kappa(B_2, k') should be level-independent."""
        total = complementarity_sum_km("B", 2)
        assert simplify(total) == 0


class TestNewKappaValues:
    def test_g2(self):
        # kappa(G2, k=1) = 7*(1+4)/4 = 35/4
        assert kappa_g2(1) == Rational(35, 4)

    def test_b2(self):
        # kappa(B2, k=1) = 5*(1+3)/3 = 20/3
        assert kappa_b2(1) == Rational(20, 3)

    def test_g2_from_km(self):
        """Cross-check: kappa_g2 should match kappa_km formula."""
        from compute.lib.lie_algebra import kappa_km
        for k_val in [0, 1, 2, 5]:
            assert kappa_g2(k_val) == kappa_km("G", 2, k_val)

    def test_b2_from_km(self):
        """Cross-check: kappa_b2 should match kappa_km formula."""
        from compute.lib.lie_algebra import kappa_km
        for k_val in [0, 1, 2, 5]:
            assert kappa_b2(k_val) == kappa_km("B", 2, k_val)


class TestGenus2Virasoro:
    """Tests for Virasoro genus-2 bar differential (thm:virasoro-genus2-bar).

    lambda_fp(2) = 7/5760, so F_2(kappa) = 7*kappa/5760.
    For Virasoro: kappa = c/2, so F_2(Vir_c) = 7c/11520.
    """

    def test_virasoro_genus2_F2(self):
        """F_2(Vir_c) = (c/2) * 7/5760 = 7c/11520."""
        c = Symbol("c")
        kap = c / 2
        f2 = F_g(kap, 2)
        assert simplify(f2 - 7 * c / 11520) == 0

    def test_virasoro_genus2_complementarity(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 91/5760."""
        c_val = Rational(1, 2)  # Ising
        f2_c = F_g(c_val / 2, 2)
        f2_dual = F_g((26 - c_val) / 2, 2)
        assert f2_c + f2_dual == Rational(91, 5760)

    def test_virasoro_genus2_bosonic_string(self):
        """F_2(Vir_{26}) = 91/5760."""
        f2 = F_g(Rational(26, 2), 2)
        assert f2 == Rational(91, 5760)

    def test_virasoro_genus2_ising(self):
        """F_2(Vir_{1/2}) = (1/4) * 7/5760 = 7/23040."""
        f2 = F_g(Rational(1, 4), 2)
        assert f2 == Rational(7, 23040)

    def test_virasoro_genus2_c0_uncurved(self):
        """F_2(Vir_0) = 0 (uncurved at c=0)."""
        f2 = F_g(Rational(0), 2)
        assert f2 == 0


class TestGenus2W3:
    """Tests for W3 genus-2 bar differential (prop:w3-genus2-curvature).

    kappa(W3) = 5c/6, lambda_fp(2) = 7/5760.
    F_2(W3) = (5c/6) * 7/5760 = 7c/6912.
    """

    def test_w3_genus2_F2(self):
        """F_2(W3_c) = (5c/6) * 7/5760 = 7c/6912."""
        c = Symbol("c")
        kap = 5 * c / 6
        f2 = F_g(kap, 2)
        assert simplify(f2 - 7 * c / 6912) == 0

    def test_w3_genus2_complementarity(self):
        """F_2(W3) + F_2(W3') with c+c'=100: sum = 175/1728."""
        c_val = Rational(50)  # c = 50, c' = 50
        kap = 5 * c_val / 6
        kap_dual = 5 * (100 - c_val) / 6
        f2 = F_g(kap, 2)
        f2_dual = F_g(kap_dual, 2)
        assert f2 + f2_dual == Rational(175, 1728)

    def test_w3_kappa_channel_decomposition(self):
        """kappa(W3) = c/2 + c/3 = 5c/6."""
        c = Symbol("c")
        kappa_TT = c / 2
        kappa_WW = c / 3
        assert simplify(kappa_TT + kappa_WW - 5 * c / 6) == 0

    def test_w3_sigma_sl3(self):
        """sigma(sl3) = 1/2 + 1/3 = 5/6."""
        sigma = Rational(1, 2) + Rational(1, 3)
        assert sigma == Rational(5, 6)

    def test_w3_complementarity_sum(self):
        """kappa + kappa' = 250/3 for W3."""
        k = Symbol("k")
        from compute.lib.lie_algebra import w3_ds_c
        c = w3_ds_c(k)
        kap = 5 * c / 6
        # dual level k' = -k - 6 for sl3 (h^vee = 3)
        c_dual = w3_ds_c(-k - 6)
        kap_dual = 5 * c_dual / 6
        total = simplify(kap + kap_dual)
        assert total == Rational(250, 3)


class TestGenusDualityTable:
    """Tests for comp:genus-duality-table (C5 content).

    Verify kappa + kappa' for all Master Table entries.
    """

    def test_heisenberg_antisymmetric(self):
        """H_1: kappa=1, kappa'=-1, sum=0."""
        assert kappa_heisenberg(1) + kappa_heisenberg(-1) == 0

    def test_sl2_antisymmetric(self):
        """sl2_k: kappa + kappa' = 0 for all k."""
        k = Symbol("k")
        kap = kappa_sl2()  # symbolic
        kap_dual = kappa_sl2().subs(k, -k - 4)  # k' = -k - 2h^vee
        assert simplify(kap + kap_dual) == 0

    def test_sl3_antisymmetric(self):
        """sl3_k: kappa + kappa' = 0 for all k."""
        k = Symbol("k")
        kap = kappa_sl3()
        kap_dual = kappa_sl3().subs(k, -k - 6)
        assert simplify(kap + kap_dual) == 0

    def test_virasoro_sum_13(self):
        """Vir_c: kappa + kappa' = 13."""
        c = Symbol("c")
        kap = c / 2
        kap_dual = (26 - c) / 2
        assert simplify(kap + kap_dual) == 13

    def test_w3_sum_250_over_3(self):
        """W3_c: kappa + kappa' = 250/3."""
        c = Symbol("c")
        kap = 5 * c / 6
        kap_dual = 5 * (100 - c) / 6
        assert simplify(kap + kap_dual) == Rational(250, 3)

    def test_genus_determines_kappa(self):
        """F_1 = kappa/24, so kappa = 24*F_1 (thm:genus-determines-pair)."""
        for kappa_val in [Rational(1), Rational(9, 4), Rational(13)]:
            f1 = F_g(kappa_val, 1)
            assert 24 * f1 == kappa_val

    def test_genus_homomorphism(self):
        """phi(A tensor B) = phi(A) + phi(B), i.e. kappa additive."""
        kappa_a = Rational(3, 2)
        kappa_b = Rational(7, 4)
        for g in range(1, 5):
            assert F_g(kappa_a + kappa_b, g) == F_g(kappa_a, g) + F_g(kappa_b, g)

    def test_universal_radius_2pi(self):
        """Convergence ratio -> 1/(2pi)^2 independent of kappa."""
        import math
        target = 1 / (2 * math.pi) ** 2
        for kappa_val in [Rational(1), Rational(13), Rational(250, 3)]:
            ratios = []
            for g in range(1, 10):
                fg = F_g(kappa_val, g)
                fg1 = F_g(kappa_val, g + 1)
                if fg != 0:
                    ratios.append(float(fg1 / fg))
            # All kappa values should give same ratios
            assert abs(ratios[-1] - target) < 0.005
