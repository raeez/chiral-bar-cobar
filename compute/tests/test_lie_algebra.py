"""Tests for compute/lib/lie_algebra.py — Cartan data, structure constants, formulas."""

import pytest
from sympy import Rational, Symbol

from compute.lib.lie_algebra import (
    cartan_data,
    structure_constants_sl2,
    structure_constants_sl3,
    killing_form_sl2,
    sugawara_c,
    ff_dual_level,
    kappa_km,
    sigma_invariant,
    virasoro_ds_c,
    w3_ds_c,
)


class TestCartanData:
    def test_sl2(self):
        data = cartan_data("A", 1)
        assert data.dim == 3
        assert data.h == 2
        assert data.h_dual == 2
        assert data.exponents == [1]
        assert data.rank == 1

    def test_sl3(self):
        data = cartan_data("A", 2)
        assert data.dim == 8
        assert data.h == 3
        assert data.h_dual == 3
        assert data.exponents == [1, 2]

    def test_G2(self):
        """G_2: dim=14, h=6, h*=4. CRITICAL: h != h*."""
        data = cartan_data("G", 2)
        assert data.dim == 14
        assert data.h == 6
        assert data.h_dual == 4
        assert data.h != data.h_dual  # non-simply-laced!
        assert data.exponents == [1, 5]

    def test_B2(self):
        """B_2 = so(5): dim=10, h=4, h*=3. Non-simply-laced."""
        data = cartan_data("B", 2)
        assert data.dim == 10
        assert data.h == 4
        assert data.h_dual == 3

    def test_positive_roots_sl2(self):
        data = cartan_data("A", 1)
        assert len(data.positive_roots) == 1  # just alpha

    def test_positive_roots_sl3(self):
        data = cartan_data("A", 2)
        # sl_3 has 3 positive roots: alpha_1, alpha_2, alpha_1 + alpha_2
        assert len(data.positive_roots) == 3

    def test_positive_roots_G2(self):
        data = cartan_data("G", 2)
        # G_2 has 6 positive roots
        assert len(data.positive_roots) == 6


class TestStructureConstants:
    def test_sl2_bracket(self):
        """[e, f] = h, [h, e] = 2e, [h, f] = -2f."""
        sc = structure_constants_sl2()
        assert sc[("e", "f")] == {"h": Rational(1)}
        assert sc[("h", "e")] == {"e": Rational(2)}
        assert sc[("h", "f")] == {"f": Rational(-2)}

    def test_sl2_antisymmetry(self):
        sc = structure_constants_sl2()
        # [f, e] = -[e, f] = -h
        assert sc[("f", "e")] == {"h": Rational(-1)}

    def test_sl3_bracket_e1_e2(self):
        """[e1, e2] = e12."""
        sc = structure_constants_sl3()
        assert sc[("e1", "e2")] == {"e12": Rational(1)}

    def test_sl3_cartan_action(self):
        """[h1, e1] = 2*e1 (from Cartan matrix A[0,0] = 2)."""
        sc = structure_constants_sl3()
        assert sc[("h1", "e1")] == {"e1": Rational(2)}


class TestKillingForm:
    def test_sl2(self):
        kf = killing_form_sl2()
        assert kf[("e", "f")] == Rational(1)
        assert kf[("h", "h")] == Rational(2)
        # e-e should not be in the form (zero)
        assert ("e", "e") not in kf


class TestSugawara:
    def test_sl2(self):
        """c(sl_2, k) = 3k/(k+2)."""
        k = Symbol("k")
        c = sugawara_c("A", 1, k)
        # 3*k / (k + 2)
        assert c == 3 * k / (k + 2)

    def test_sl2_numeric(self):
        """c(sl_2, k=1) = 3/3 = 1."""
        assert sugawara_c("A", 1, 1) == Rational(1)

    def test_critical_raises(self):
        """Sugawara is undefined at k = -h* = -2 for sl_2."""
        with pytest.raises(ValueError, match="critical"):
            sugawara_c("A", 1, -2)

    def test_G2(self):
        """c(G_2, k) = 14k/(k+4)."""
        k = Symbol("k")
        c = sugawara_c("G", 2, k)
        assert c == 14 * k / (k + 4)


class TestFFDual:
    def test_sl2(self):
        """FF dual of k for sl_2: k' = -k - 4 (since 2*h* = 4)."""
        k = Symbol("k")
        assert ff_dual_level("A", 1, k) == -k - 4

    def test_G2(self):
        """FF dual for G_2: k' = -k - 8 (since 2*h* = 8, NOT 2h=12)."""
        k = Symbol("k")
        assert ff_dual_level("G", 2, k) == -k - 8

    def test_ff_involution(self):
        """FF involution is an involution: (k')' = k."""
        k = Symbol("k")
        k_prime = ff_dual_level("A", 1, k)
        k_double_prime = ff_dual_level("A", 1, k_prime)
        from sympy import simplify
        assert simplify(k_double_prime - k) == 0


class TestKappa:
    def test_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        k = Symbol("k")
        assert kappa_km("A", 1, k) == 3 * (k + 2) / 4

    def test_sl2_numeric(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        assert kappa_km("A", 1, 1) == Rational(9, 4)

    def test_sl3(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        k = Symbol("k")
        kap = kappa_km("A", 2, k)
        from sympy import simplify
        assert simplify(kap - 4 * (k + 3) / 3) == 0

    def test_G2(self):
        """kappa(G_2, k) = 14(k+4)/8 = 7(k+4)/4."""
        k = Symbol("k")
        kap = kappa_km("G", 2, k)
        from sympy import simplify
        assert simplify(kap - 7 * (k + 4) / 4) == 0


class TestSigma:
    def test_sl2(self):
        """sigma(sl_2) = 1/(1+1) = 1/2."""
        assert sigma_invariant("A", 1) == Rational(1, 2)

    def test_sl3(self):
        """sigma(sl_3) = 1/2 + 1/3 = 5/6."""
        assert sigma_invariant("A", 2) == Rational(5, 6)

    def test_G2(self):
        """sigma(G_2) = 1/(1+1) + 1/(5+1) = 1/2 + 1/6 = 2/3."""
        assert sigma_invariant("G", 2) == Rational(2, 3)


class TestDSFormulas:
    def test_virasoro_ds(self):
        """Virasoro DS: c = 1 - 6(k+1)^2/(k+2). VF032."""
        # At k=0: c = 1 - 6*1/2 = 1 - 3 = -2
        assert virasoro_ds_c(0) == Rational(-2)
        # At k=1: c = 1 - 6*4/3 = 1 - 8 = -7
        assert virasoro_ds_c(1) == Rational(-7)

    def test_w3_ds(self):
        """W_3 DS: c = 2 - 24(k+2)^2/(k+3). VF033."""
        # At k=0: c = 2 - 24*4/3 = 2 - 32 = -30
        assert w3_ds_c(0) == Rational(-30)
