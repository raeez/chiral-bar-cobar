"""
Tests for quartic_contact_class.py

Verifies the quartic contact shadow Q^contact across the standard
landscape and its relationship to shadow depth classification.
"""

import pytest
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from quartic_contact_class import (
    ShadowClass,
    kappa_heisenberg, kappa_affine_sl2, kappa_virasoro,
    kappa_w3, kappa_betagamma,
    Q_contact_heisenberg, Q_contact_affine_sl2,
    Q_contact_betagamma, Q_contact_virasoro, Q_contact_w3,
    shadow_class_from_quartic,
    virasoro_complementarity_sum,
    kappa_complementarity_sum_virasoro,
    kappa_complementarity_sum_affine_sl2,
)


# ============================================================
# Modular characteristic κ
# ============================================================

class TestKappa:
    def test_heisenberg_k1(self):
        assert kappa_heisenberg(1) == Fraction(1)

    def test_heisenberg_k2(self):
        assert kappa_heisenberg(2) == Fraction(2)

    def test_affine_sl2_k1(self):
        """κ(sl_2, k=1) = 3(1+2)/4 = 9/4."""
        assert kappa_affine_sl2(1) == Fraction(9, 4)

    def test_affine_sl2_k_minus_2(self):
        """κ(sl_2, k=-2) = 3(-2+2)/4 = 0. Critical level."""
        assert kappa_affine_sl2(-2) == Fraction(0)

    def test_virasoro_c1(self):
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_virasoro_c26(self):
        assert kappa_virasoro(26) == Fraction(13)

    def test_w3_c100(self):
        """κ(W_3, c=100) = 5·100/6 = 250/3."""
        assert kappa_w3(100) == Fraction(250, 3)

    def test_betagamma(self):
        assert kappa_betagamma() == Fraction(1)


# ============================================================
# Quartic contact: vanishing pattern
# ============================================================

class TestQuarticVanishing:
    """q_4 = 0 for G, L, C families; q_4 ≠ 0 for M family."""

    def test_heisenberg_vanishes(self):
        for k in [1, 2, 5, 10]:
            assert Q_contact_heisenberg(k) == Fraction(0)

    def test_affine_sl2_vanishes(self):
        for k in [1, 2, 3, 5, -1, -3]:
            assert Q_contact_affine_sl2(k) == Fraction(0)

    def test_betagamma_vanishes(self):
        assert Q_contact_betagamma() == Fraction(0)

    def test_virasoro_nonzero(self):
        for c in [1, 2, 5, 10, 13, 25, 26, 100]:
            Q = Q_contact_virasoro(c)
            assert Q != Fraction(0), f"Q^contact(Vir_{c}) should be nonzero"
            assert Q > 0, f"Q^contact(Vir_{c}) should be positive for c > 0"

    def test_w3_nonzero(self):
        for c in [1, 2, 10, 50, 100]:
            Q = Q_contact_w3(c)
            assert Q != Fraction(0), f"Q^contact(W_3, c={c}) should be nonzero"


# ============================================================
# Explicit Virasoro quartic values
# ============================================================

class TestVirasoroQuarticExplicit:
    def test_formula(self):
        """Q^contact(Vir_c) = 10/[c(5c+22)]."""
        for c in [1, 2, 5, 10, 13, 26]:
            expected = Fraction(10, c * (5 * c + 22))
            assert Q_contact_virasoro(c) == expected

    def test_c1(self):
        """Q(1) = 10/(1·27) = 10/27."""
        assert Q_contact_virasoro(1) == Fraction(10, 27)

    def test_c2(self):
        """Q(2) = 10/(2·32) = 5/32."""
        assert Q_contact_virasoro(2) == Fraction(10, 64)
        assert Q_contact_virasoro(2) == Fraction(5, 32)

    def test_c13_self_dual(self):
        """Q(13) = 10/(13·87) = 10/1131."""
        assert Q_contact_virasoro(13) == Fraction(10, 1131)

    def test_c26(self):
        """Q(26) = 10/(26·152) = 5/1976."""
        assert Q_contact_virasoro(26) == Fraction(10, 3952)
        assert Q_contact_virasoro(26) == Fraction(5, 1976)

    def test_brown_henneaux_k1(self):
        """c=6: Q = 10/(6·52) = 5/156."""
        assert Q_contact_virasoro(6) == Fraction(10, 312)
        assert Q_contact_virasoro(6) == Fraction(5, 156)

    def test_brown_henneaux_formula(self):
        """At c=6k: Q = 5/[6k(15k+11)]."""
        for k in [1, 2, 3, 5, 10]:
            c = 6 * k
            Q_from_c = Q_contact_virasoro(c)
            Q_expected = Fraction(5, 6 * k * (15 * k + 11))
            assert Q_from_c == Q_expected, f"Mismatch at k={k}"

    def test_semiclassical_order(self):
        """In semiclassical limit k→∞: Q ~ 1/(18k²)."""
        k = 1000
        c = 6 * k
        Q = Q_contact_virasoro(c)
        # Q = 5/[6k(15k+11)] ≈ 5/(6k·15k) = 1/(18k²)
        approx = Fraction(1, 18 * k**2)
        ratio = Q / approx
        # ratio should be close to 1
        assert abs(float(ratio) - 1.0) < 0.01

    def test_pole_at_c0(self):
        with pytest.raises(ValueError):
            Q_contact_virasoro(0)


# ============================================================
# Complementarity
# ============================================================

class TestComplementarity:
    def test_kappa_virasoro_complementarity(self):
        """κ(c) + κ(26-c) = 13 for all c."""
        for c in [1, 2, 5, 10, 13, 20, 25]:
            assert kappa_complementarity_sum_virasoro(c) == Fraction(13)

    def test_kappa_affine_sl2_complementarity(self):
        """κ(k) + κ(-k-4) = 0 for affine sl_2."""
        for k in [1, 2, 3, 5, 10]:
            assert kappa_complementarity_sum_affine_sl2(k) == Fraction(0)

    def test_virasoro_quartic_self_dual(self):
        """At c=13: Q(13) + Q(13) = 20/1131."""
        total = virasoro_complementarity_sum(13)
        assert total == Fraction(20, 1131)

    def test_virasoro_quartic_complementarity_rational(self):
        """Q(c) + Q(26-c) is a well-defined rational function for c ≠ 0, 26."""
        for c in [1, 2, 5, 10, 20, 25]:
            total = virasoro_complementarity_sum(c)
            assert isinstance(total, Fraction)
            # Should be positive for 0 < c < 26
            if 0 < c < 26:
                assert total > 0

    def test_virasoro_quartic_c1_c25(self):
        """Explicit: Q(1) + Q(25) = 10/27 + 10/(25·147) = 10/27 + 2/735."""
        Q1 = Q_contact_virasoro(1)
        Q25 = Q_contact_virasoro(25)
        assert Q1 == Fraction(10, 27)
        assert Q25 == Fraction(10, 25 * 147)
        total = Q1 + Q25
        # 10/27 + 10/3675 = (10·3675 + 10·27)/(27·3675) = 37020/99225
        expected = Fraction(10, 27) + Fraction(10, 3675)
        assert total == expected


# ============================================================
# Shadow class assignment
# ============================================================

class TestShadowClass:
    def test_heisenberg_is_G(self):
        assert shadow_class_from_quartic('heisenberg') == ShadowClass.G

    def test_affine_is_L(self):
        assert shadow_class_from_quartic('affine') == ShadowClass.L

    def test_betagamma_is_C(self):
        assert shadow_class_from_quartic('betagamma') == ShadowClass.C

    def test_virasoro_is_M(self):
        assert shadow_class_from_quartic('virasoro') == ShadowClass.M

    def test_w3_is_M(self):
        assert shadow_class_from_quartic('w3') == ShadowClass.M

    def test_vanishing_matches_class(self):
        """G, L, C have q_4 = 0; M has q_4 ≠ 0."""
        assert Q_contact_heisenberg(1) == 0  # G
        assert Q_contact_affine_sl2(1) == 0  # L
        assert Q_contact_betagamma() == 0     # C
        assert Q_contact_virasoro(1) != 0     # M
        assert Q_contact_w3(1) != 0           # M


# ============================================================
# Hessian correction
# ============================================================

class TestHessianCorrection:
    """δ_H^(1) = 120/[c²(5c+22)] for Virasoro."""

    def test_hessian_formula(self):
        for c in [1, 2, 5, 13, 26]:
            dH = Fraction(120, c**2 * (5 * c + 22))
            assert dH > 0

    def test_hessian_brown_henneaux(self):
        """δ_H(c=6k) = 5/[3k²(15k+11)]."""
        for k in [1, 2, 3, 5]:
            c = 6 * k
            dH_from_c = Fraction(120, c**2 * (5 * c + 22))
            dH_expected = Fraction(5, 3 * k**2 * (15 * k + 11))
            assert dH_from_c == dH_expected, f"Hessian mismatch at k={k}"

    def test_hessian_semiclassical(self):
        """In semiclassical limit: δ_H ~ 1/(9k³)."""
        k = 1000
        c = 6 * k
        dH = Fraction(120, c**2 * (5 * c + 22))
        approx = Fraction(1, 9 * k**3)
        ratio = dH / approx
        assert abs(float(ratio) - 1.0) < 0.01
