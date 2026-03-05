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
        """Known Faber-Pandharipande numbers."""
        assert lambda_fp(1) == Rational(1, 12)
        assert lambda_fp(2) == Rational(1, 240)
        assert lambda_fp(3) == Rational(1, 6048)

    def test_positive(self):
        """All lambda_g must be positive."""
        for g in range(1, 20):
            assert lambda_fp(g) > 0


class TestGenusTable:
    def test_heisenberg_F1(self):
        """F_1(H_kappa) = kappa/12."""
        kappa = Symbol("kappa")
        table = genus_table(kappa, max_genus=1)
        assert simplify(table[1] - kappa / 12) == 0

    def test_sl2_F1(self):
        """F_1(sl_2, k) = 3(k+2)/4 * 1/12 = (k+2)/16."""
        k = Symbol("k")
        kap = kappa_sl2()
        table = genus_table(kap, max_genus=1)
        # kappa_sl2() with no arg returns symbolic 3*(k+2)/4
        # F_1 = 3*(k+2)/4 * 1/12 = (k+2)/16
        assert simplify(table[1] - (k + 2) / 16) == 0

    def test_virasoro_F1(self):
        """F_1(Vir_c) = c/2 * 1/12 = c/24."""
        c = Symbol("c")
        table = genus_table(c / 2, max_genus=1)
        assert simplify(table[1] - c / 24) == 0

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

    Uses the code's lambda_fp(g) = |B_{2g}| / (2g*(2g-2)!).
    lambda_fp(2) = 1/240, so F_2(kappa) = kappa/240.
    """

    def test_virasoro_genus2_F2(self):
        """F_2(Vir_c) = (c/2) * lambda_fp(2) = c/480."""
        c = Symbol("c")
        kap = c / 2
        f2 = F_g(kap, 2)
        assert simplify(f2 - c / 480) == 0

    def test_virasoro_genus2_complementarity(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 13/240."""
        c_val = Rational(1, 2)  # Ising
        f2_c = F_g(c_val / 2, 2)
        f2_dual = F_g((26 - c_val) / 2, 2)
        assert f2_c + f2_dual == Rational(13, 240)

    def test_virasoro_genus2_bosonic_string(self):
        """F_2(Vir_{26}) = 13/240."""
        f2 = F_g(Rational(26, 2), 2)
        assert f2 == Rational(13, 240)

    def test_virasoro_genus2_ising(self):
        """F_2(Vir_{1/2}) = 1/960."""
        f2 = F_g(Rational(1, 4), 2)
        assert f2 == Rational(1, 960)

    def test_virasoro_genus2_c0_uncurved(self):
        """F_2(Vir_0) = 0 (uncurved at c=0)."""
        f2 = F_g(Rational(0), 2)
        assert f2 == 0


class TestGenus2W3:
    """Tests for W3 genus-2 bar differential (prop:w3-genus2-curvature).

    kappa(W3) = 5c/6, lambda_fp(2) = 1/240.
    F_2(W3) = (5c/6)/240 = c/288.
    """

    def test_w3_genus2_F2(self):
        """F_2(W3_c) = (5c/6) * 1/240 = c/288."""
        c = Symbol("c")
        kap = 5 * c / 6
        f2 = F_g(kap, 2)
        assert simplify(f2 - c / 288) == 0

    def test_w3_genus2_complementarity(self):
        """F_2(W3) + F_2(W3') with c+c'=100: sum = 25/72."""
        c_val = Rational(50)  # c = 50, c' = 50
        kap = 5 * c_val / 6
        kap_dual = 5 * (100 - c_val) / 6
        f2 = F_g(kap, 2)
        f2_dual = F_g(kap_dual, 2)
        assert f2 + f2_dual == Rational(25, 72)

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
