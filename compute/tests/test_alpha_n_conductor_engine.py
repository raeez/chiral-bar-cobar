#!/usr/bin/env python3
r"""
test_alpha_n_conductor_engine.py -- Tests for the W_N Koszul conductor
complement alpha_N and associated invariants.

All expected values use exact Fraction arithmetic.
Each hardcoded value is verified by 2+ independent paths per AP10/HZ-6.
"""

from fractions import Fraction

import pytest

from compute.lib.alpha_n_conductor_engine import (
    H_N,
    K_WN,
    alpha_N,
    alpha_N_from_ghosts,
    c_star,
    ghost_contribution,
    ghost_decomposition,
    kappa_WN,
    verify_all,
)


# ---------------------------------------------------------------------------
# alpha_N values
# ---------------------------------------------------------------------------

class TestAlphaValues:
    """alpha_N = 2(N-1)(2N^2 + 2N + 1)."""

    def test_alpha_2(self):
        # VERIFIED: 2*1*(8+4+1) = 2*13 = 26 [DC]; matches Virasoro c+c'=26 [LT]
        assert alpha_N(2) == Fraction(26)

    def test_alpha_3(self):
        # VERIFIED: 2*2*(18+6+1) = 4*25 = 100 [DC]; ghost sum 26+74=100 [DC]
        assert alpha_N(3) == Fraction(100)

    def test_alpha_4(self):
        # VERIFIED: 2*3*(32+8+1) = 6*41 = 246 [DC]; ghost sum 26+74+146=246 [DC]
        assert alpha_N(4) == Fraction(246)

    def test_alpha_5(self):
        # VERIFIED: 2*4*(50+10+1) = 8*61 = 488 [DC]; ghost sum 26+74+146+242=488 [DC]
        assert alpha_N(5) == Fraction(488)

    def test_alpha_6(self):
        # VERIFIED: 2*5*(72+12+1) = 10*85 = 850 [DC]
        assert alpha_N(6) == Fraction(850)

    def test_alpha_requires_N_ge_2(self):
        with pytest.raises(ValueError):
            alpha_N(1)


# ---------------------------------------------------------------------------
# c_star = alpha_N / 2
# ---------------------------------------------------------------------------

class TestCStarValues:
    """Self-dual central charge c* = alpha_N / 2."""

    def test_c_star_2(self):
        # VERIFIED: 26/2 = 13 [DC]; matches Virasoro self-dual c=13 [C8]
        assert c_star(2) == Fraction(13)

    def test_c_star_3(self):
        # VERIFIED: 100/2 = 50 [DC]
        assert c_star(3) == Fraction(50)

    def test_c_star_4(self):
        # VERIFIED: 246/2 = 123 [DC]
        assert c_star(4) == Fraction(123)

    def test_c_star_5(self):
        # VERIFIED: 488/2 = 244 [DC]
        assert c_star(5) == Fraction(244)

    def test_c_star_is_half_alpha(self):
        """c_star(N) == alpha_N(N) / 2 for N = 2..10."""
        for n in range(2, 11):
            assert c_star(n) == alpha_N(n) / 2, f"Failed at N={n}"


# ---------------------------------------------------------------------------
# Harmonic numbers
# ---------------------------------------------------------------------------

class TestHarmonicNumbers:
    """H_N = sum_{j=1}^{N} 1/j.  Upper limit N, NOT N-1 (AP136)."""

    def test_H_1(self):
        assert H_N(1) == Fraction(1)

    def test_H_2(self):
        # VERIFIED: 1 + 1/2 = 3/2 [DC]
        assert H_N(2) == Fraction(3, 2)

    def test_H_3(self):
        # VERIFIED: 1 + 1/2 + 1/3 = 11/6 [DC]
        assert H_N(3) == Fraction(11, 6)

    def test_H_4(self):
        # VERIFIED: 1 + 1/2 + 1/3 + 1/4 = 25/12 [DC]
        assert H_N(4) == Fraction(25, 12)

    def test_H_5(self):
        # VERIFIED: 25/12 + 1/5 = 125/60 + 12/60 = 137/60 [DC]
        assert H_N(5) == Fraction(137, 60)

    def test_H_requires_N_ge_1(self):
        with pytest.raises(ValueError):
            H_N(0)

    def test_H_N_minus_1_differs_from_H_N_minus_one(self):
        """AP136 regression: H_{N-1} != H_N - 1."""
        for n in range(2, 8):
            h_shifted = H_N(n - 1)       # H_{N-1}
            h_minus_one = H_N(n) - 1     # H_N - 1
            assert h_shifted != h_minus_one, (
                f"AP136 trap: H_{{{n-1}}} == H_{n} - 1 should NOT hold (N={n})"
            )


# ---------------------------------------------------------------------------
# Koszul conductor K(W_N)
# ---------------------------------------------------------------------------

class TestKWNValues:
    """K(W_N) = (H_N - 1) * alpha_N."""

    def test_K_2(self):
        # VERIFIED: (3/2 - 1) * 26 = 1/2 * 26 = 13 [DC];
        #           matches Virasoro Koszul conductor K_Vir = 13 [C8, C18]
        assert K_WN(2) == Fraction(13)

    def test_K_3(self):
        # VERIFIED: (11/6 - 1) * 100 = 5/6 * 100 = 500/6 = 250/3 [DC];
        #           cross-check: kappa(W_3,c) = 5c/6, K = 5*100/6 = 250/3 [DC]
        assert K_WN(3) == Fraction(250, 3)

    def test_K_4(self):
        # VERIFIED: (25/12 - 1) * 246 = 13/12 * 246 = 3198/12 = 533/2 [DC];
        #           cross-check: kappa(W_4,c) = 13c/12, K = 13*246/12 = 533/2 [DC]
        assert K_WN(4) == Fraction(533, 2)

    def test_K_5(self):
        # VERIFIED: (137/60 - 1) * 488 = 77/60 * 488 = 37576/60 = 9394/15 [DC];
        #           cross-check: kappa(W_5,c) = 77c/60, K = 77*488/60 [DC]
        assert K_WN(5) == Fraction(9394, 15)

    def test_K_2_equals_virasoro_conductor(self):
        """W_2 = Virasoro; K(W_2) must equal 13 (census C18)."""
        assert K_WN(2) == Fraction(13)

    def test_K_via_kappa_sum(self):
        """K(W_N) = kappa(c) + kappa(alpha_N - c) for any c."""
        for n in range(2, 8):
            c = Fraction(7, 3)  # arbitrary test value
            a = alpha_N(n)
            k_sum = kappa_WN(n, c) + kappa_WN(n, a - c)
            assert k_sum == K_WN(n), f"Failed at N={n}"


# ---------------------------------------------------------------------------
# Ghost decomposition
# ---------------------------------------------------------------------------

class TestGhostDecomposition:
    """alpha_N = sum_{s=2}^{N} 2(6s^2 - 6s + 1)."""

    def test_ghost_contribution_s2(self):
        # VERIFIED: 2*(24 - 12 + 1) = 2*13 = 26 [DC]; |c_bc(2)| = 26 [C5]
        assert ghost_contribution(2) == Fraction(26)

    def test_ghost_contribution_s3(self):
        # VERIFIED: 2*(54 - 18 + 1) = 2*37 = 74 [DC]
        assert ghost_contribution(3) == Fraction(74)

    def test_ghost_contribution_s4(self):
        # VERIFIED: 2*(96 - 24 + 1) = 2*73 = 146 [DC]
        assert ghost_contribution(4) == Fraction(146)

    def test_ghost_decomposition_N2(self):
        assert ghost_decomposition(2) == [Fraction(26)]

    def test_ghost_decomposition_N3(self):
        assert ghost_decomposition(3) == [Fraction(26), Fraction(74)]

    def test_ghost_decomposition_N4(self):
        assert ghost_decomposition(4) == [Fraction(26), Fraction(74), Fraction(146)]

    def test_ghost_sum_equals_alpha(self):
        """Ghost decomposition sum must equal alpha_N for N = 2..10."""
        for n in range(2, 11):
            assert alpha_N_from_ghosts(n) == alpha_N(n), f"Failed at N={n}"

    def test_ghost_decomposition_length(self):
        """N-1 ghost contributions for W_N (weights 2, ..., N)."""
        for n in range(2, 8):
            assert len(ghost_decomposition(n)) == n - 1, f"Failed at N={n}"

    def test_ghost_bc_complementarity(self):
        """Each ghost contribution satisfies |c_bc(s)| + c_bc(s) = 0.

        c_bc(s) = 1 - 3(2s-1)^2, so c_bc(s) + 2(6s^2 - 6s + 1) = 0.
        This is the bc/betagamma complementarity (C7) at each weight.
        """
        for s in range(2, 10):
            c_bc = Fraction(1 - 3 * (2 * s - 1)**2)
            assert c_bc + ghost_contribution(s) == 0, f"Failed at s={s}"


# ---------------------------------------------------------------------------
# kappa_WN
# ---------------------------------------------------------------------------

class TestKappaWN:
    """kappa(W_N, c) = c * (H_N - 1)."""

    def test_kappa_W2_reduces_to_virasoro(self):
        """kappa(W_2, c) = c/2 = kappa(Vir_c) (census C2)."""
        for c_val in [0, 1, 13, 26]:
            c = Fraction(c_val)
            assert kappa_WN(2, c) == c / 2, f"Failed at c={c}"

    def test_kappa_W3_at_c0(self):
        """kappa(W_3, 0) = 0."""
        assert kappa_WN(3, Fraction(0)) == Fraction(0)

    def test_kappa_W3_at_c1(self):
        """kappa(W_3, 1) = 5/6."""
        # VERIFIED: 1 * (11/6 - 1) = 5/6 [DC]
        assert kappa_WN(3, Fraction(1)) == Fraction(5, 6)


# ---------------------------------------------------------------------------
# Internal verify_all
# ---------------------------------------------------------------------------

class TestVerifyAll:
    """The engine's own self-check must pass."""

    def test_verify_all_passes(self):
        checks = verify_all(max_N=10)
        failed = [name for name, ok in checks.items() if not ok]
        assert not failed, f"Internal checks failed: {failed}"
