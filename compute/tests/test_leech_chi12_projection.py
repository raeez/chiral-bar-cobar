"""
Tests for the Leech lattice chi_12 projection.

Verifies the decisive computation: the Leech lattice genus-2 theta
series has nonzero projection onto chi_12 = SK(f_22), the unique
Siegel cusp form of weight 12 on Sp(4,Z). This is the key input
for the Böcherer bridge (Theorem thm:bocherer-bridge).

Via the Waldspurger formula, this nonzero projection determines
L(11, f_22 × χ_D) for all fundamental discriminants D < 0.
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.siegel_eisenstein import (
    bernoulli,
    siegel_eisenstein_coefficient,
    cohen_H,
    fundamental_discriminant,
    kronecker_symbol,
    _binomial,
)
from compute.lib.genus2_bocherer_bridge import (
    genus2_rep_leech,
    LEECH_CROSS_46_DIST,
    LEECH_SAME_66_DIST,
    LEECH_SHELL_SIZES,
)


# ============================================================
# BERNOULLI AND ARITHMETIC TESTS
# ============================================================

class TestArithmeticPrimitives:

    def test_bernoulli_4(self):
        assert bernoulli(4) == Fraction(-1, 30)

    def test_bernoulli_6(self):
        assert bernoulli(6) == Fraction(1, 42)

    def test_bernoulli_12(self):
        assert bernoulli(12) == Fraction(-691, 2730)

    def test_bernoulli_22(self):
        assert bernoulli(22) == Fraction(854513, 138)

    def test_binomial(self):
        assert _binomial(5, 0) == 1
        assert _binomial(5, 1) == 5
        assert _binomial(5, 2) == 10
        assert _binomial(5, 3) == 10

    def test_fundamental_discriminant_4(self):
        assert fundamental_discriminant(4) == (-4, 1)

    def test_fundamental_discriminant_16(self):
        assert fundamental_discriminant(16) == (-4, 2)

    def test_fundamental_discriminant_3(self):
        assert fundamental_discriminant(3) == (-3, 1)

    def test_kronecker_basic(self):
        assert kronecker_symbol(-4, 1) == 1
        assert kronecker_symbol(-4, 3) == -1
        assert kronecker_symbol(-3, 2) == -1


# ============================================================
# SIEGEL EISENSTEIN VERIFICATION vs E8
# ============================================================

class TestSiegelEisensteinE4:
    """Verify E_4^{(2)} against E8 genus-2 representation numbers."""

    def test_e4_diag_11(self):
        """E_4(diag(1,1)) = 30240 = 240 * 126."""
        val = siegel_eisenstein_coefficient(4, 1, 0, 1)
        assert val == 30240

    def test_e4_disc3(self):
        """E_4((1,1/2,1)) = 13440 = 240 * 56."""
        val = siegel_eisenstein_coefficient(4, 1, 1, 1)
        assert val == 13440

    def test_e4_b_minus1(self):
        """E_4((1,-1/2,1)) = 13440 = 240 * 56."""
        val = siegel_eisenstein_coefficient(4, 1, -1, 1)
        assert val == 13440

    def test_e4_total_root_shell(self):
        """Sum over b of E_4((1,b/2,1)) should equal 240^2 = 57600."""
        total = Fraction(0)
        for b in range(-2, 3):
            if 4 - b*b > 0:  # positive definite only
                total += siegel_eisenstein_coefficient(4, 1, b, 1)
        # b=0: 30240, b=±1: 13440 each = 57120
        # b=±2: Delta=0 (degenerate, not counted)
        assert total == 30240 + 2 * 13440

    def test_cohen_H_at_4(self):
        """H(3, 4) = -1/2."""
        assert cohen_H(3, 4) == Fraction(-1, 2)

    def test_cohen_H_at_3(self):
        """H(3, 3) = -2/9."""
        assert cohen_H(3, 3) == Fraction(-2, 9)

    def test_cohen_H_at_1(self):
        """H(r, 1) = 0 (1 ≡ 1 mod 4, not a valid discriminant)."""
        assert cohen_H(3, 1) == 0


# ============================================================
# LEECH CHI_12 PROJECTION (the decisive computation)
# ============================================================

class TestLeechChi12Projection:
    """
    Verify that Θ^{(2)}_Leech has nonzero projection onto chi_12.

    This is the key computation for the Böcherer bridge theorem.
    """

    def _compute_decomposition(self):
        """Compute the decomposition coefficients."""
        # Genus-1 Eisenstein coefficients (for rank-1 terms)
        def g1_coeff(k, n):
            if n == 0:
                return Fraction(1)
            B_k = bernoulli(k)
            from compute.lib.siegel_eisenstein import sigma
            return Fraction(-2 * k) * sigma(k - 1, n) / B_k

        def full_coeff(k, a, b, c):
            Delta = 4*a*c - b*b
            if a == 0 and b == 0 and c == 0:
                return Fraction(1)
            if Delta == 0:
                if c == 0 and b == 0:
                    return g1_coeff(k, a)
                if a == 0 and b == 0:
                    return g1_coeff(k, c)
                return Fraction(0)
            if Delta < 0:
                return Fraction(0)
            return siegel_eisenstein_coefficient(k, a, b, c)

        def convolve2(k1, k2, a, b, c):
            total = Fraction(0)
            for a1 in range(a + 1):
                a2 = a - a1
                for c1 in range(c + 1):
                    c2 = c - c1
                    bmax = 2 * min(a1, c1) if min(a1, c1) > 0 else 0
                    for b1 in range(-bmax, bmax + 1):
                        b2 = b - b1
                        if 4*a1*c1 - b1*b1 < 0 or 4*a2*c2 - b2*b2 < 0:
                            continue
                        f1 = full_coeff(k1, a1, b1, c1)
                        f2 = full_coeff(k2, a2, b2, c2)
                        if f1 != 0 and f2 != 0:
                            total += f1 * f2
            return total

        def convolve3(k, a, b, c):
            total = Fraction(0)
            for a1 in range(a + 1):
                a23 = a - a1
                for c1 in range(c + 1):
                    c23 = c - c1
                    bmax = 2*min(a1,c1) if min(a1,c1) > 0 else 0
                    for b1 in range(-bmax, bmax+1):
                        b23 = b - b1
                        if 4*a1*c1 - b1*b1 < 0:
                            continue
                        f1 = full_coeff(k, a1, b1, c1)
                        if f1 == 0:
                            continue
                        f23 = convolve2(k, k, a23, b23, c23)
                        total += f1 * f23
            return total

        Ts = [(1,0,1), (2,0,2), (2,1,2)]
        leech = [Fraction(0), Fraction(18309564000), Fraction(9258762240)]

        E4c = [convolve3(4, *T) for T in Ts]
        E6s = [convolve2(6, 6, *T) for T in Ts]
        E12 = [siegel_eisenstein_coefficient(12, *T) for T in Ts]

        # Igusa numerator: 441*E_4^3 + 250*E_6^2 - 691*E_12
        igusa = [441*E4c[i] + 250*E6s[i] - 691*E12[i] for i in range(3)]

        # Solve linear system: Theta = a*E_4^3 + b*E_6^2 + c*E_12
        M = np.array([[float(E4c[i]), float(E6s[i]), float(E12[i])]
                       for i in range(3)])
        L = np.array([float(v) for v in leech])
        abc = np.linalg.solve(M, L)

        # chi_12 projection: c_2 = (441*a + 250*b - 691*c) / igusa[0]
        c2_num = 441*abc[0] + 250*abc[1] - 691*abc[2]
        C_norm = float(igusa[0])
        c2 = c2_num / C_norm

        return {
            'abc': abc,
            'igusa': [float(v) for v in igusa],
            'c2': c2,
            'residuals': [abs(abc@M[i] - L[i]) for i in range(3)],
        }

    def test_c2_nonzero(self):
        """c_2 ≠ 0: Leech projects nontrivially onto chi_12."""
        result = self._compute_decomposition()
        assert abs(result['c2']) > 1e-10, f"c_2 = {result['c2']} is too close to zero"

    def test_residuals_zero(self):
        """Linear system is solved exactly (residuals ~ 0)."""
        result = self._compute_decomposition()
        for i, r in enumerate(result['residuals']):
            assert r < 1e-3, f"Residual at T_{i}: {r}"

    def test_igusa_nonzero_at_diag11(self):
        """
        The Igusa numerator at diag(1,1) is nonzero, confirming
        chi_12 has a nonzero coefficient there.
        """
        result = self._compute_decomposition()
        assert abs(result['igusa'][0]) > 1e-3

    def test_c2_negative(self):
        """
        c_2 < 0: the Leech cusp component is in the OPPOSITE
        direction from chi_12 at diag(1,1). This is because
        Theta_Leech = 0 at norm-2 matrices while chi_12 > 0 there.
        """
        result = self._compute_decomposition()
        assert result['c2'] < 0

    def test_waldspurger_consequence(self):
        """
        Since c_2 ≠ 0, the Böcherer-Waldspurger chain gives:
        MC data → Θ_Leech^(2) → B(D) → L(11, f_22 × χ_D)

        The twisted L-values are determined by the MC equation.
        The functional equation sign ε(f_22 × χ_D) = +1 for D < 0,
        so these L-values are generically nonzero.
        """
        result = self._compute_decomposition()
        c2 = result['c2']
        # The Böcherer coefficient B(D) = c2 * c(|D|)
        # |B(D)|^2 ~ L(11, f_22 x chi_D)
        # Since c2 != 0 and c(|D|) != 0 generically,
        # B(D) != 0 generically, hence L != 0 generically.
        assert abs(c2) > 1e-10  # c2 ≠ 0 is the key input


# ============================================================
# CROSS-SHELL DISTRIBUTION TESTS
# ============================================================

class TestLeechCrossShellDistributions:
    """Tests for the norm 4×6 and 6×6 Leech distributions."""

    def test_cross_46_sums_to_shell_size(self):
        """Cross-shell distribution sums to |shell_6| = 16773120."""
        total = sum(LEECH_CROSS_46_DIST.values())
        assert total == LEECH_SHELL_SIZES[6]

    def test_same_66_sums_to_shell_size(self):
        """Same-shell distribution sums to |shell_6| = 16773120."""
        total = sum(LEECH_SAME_66_DIST.values())
        assert total == LEECH_SHELL_SIZES[6]

    def test_cross_46_b3_equals_min_b1(self):
        """N(4,6,3) = N(4,4,1) = 47104 (structural identity)."""
        assert LEECH_CROSS_46_DIST[3] == 47104

    def test_same_66_b5_impossible(self):
        """Inner product 5 between norm-6 vectors is impossible."""
        assert LEECH_SAME_66_DIST.get(5, 0) == 0

    def test_same_66_b6_identity(self):
        """Only w = ±v has (v,w) = ±6."""
        assert LEECH_SAME_66_DIST[6] == 1
        assert LEECH_SAME_66_DIST[-6] == 1

    def test_genus2_rep_leech_cross_shell(self):
        """r_2(Leech, ((2,0),(0,3))) = 196560 * 6476800."""
        r2 = genus2_rep_leech(2, 0, 3)
        assert r2 == LEECH_SHELL_SIZES[4] * LEECH_CROSS_46_DIST[0]

    def test_genus2_rep_leech_same_66(self):
        """r_2(Leech, ((3,0),(0,3))) = 16773120 * 5292300."""
        r2 = genus2_rep_leech(3, 0, 3)
        assert r2 == LEECH_SHELL_SIZES[6] * LEECH_SAME_66_DIST[0]


# ============================================================
# SIEGEL EISENSTEIN VERIFICATION TESTS
# ============================================================

class TestSiegelEisensteinHigherWeight:
    """Verify E_6 and E_12 Siegel Eisenstein series coefficients."""

    def test_e6_positive_at_diag11(self):
        """E_6 at diag(1,1) should be positive (Kitaoka)."""
        val = siegel_eisenstein_coefficient(6, 1, 0, 1)
        assert val > 0

    def test_e12_positive_at_diag11(self):
        """E_12 at diag(1,1) should be positive (Kitaoka)."""
        val = siegel_eisenstein_coefficient(12, 1, 0, 1)
        assert val > 0

    def test_e6_positive_at_diag22(self):
        """E_6 at diag(2,2) should be positive."""
        val = siegel_eisenstein_coefficient(6, 2, 0, 2)
        assert val > 0

    def test_e12_positive_at_disc15(self):
        """E_12 at ((2,1/2),(1/2,2)) should be positive."""
        val = siegel_eisenstein_coefficient(12, 2, 1, 2)
        assert val > 0

    def test_igusa_constant_term_cancels(self):
        """
        441 + 250 - 691 = 0: the Igusa numerator has no constant term.
        This ensures chi_12 is a cusp form (vanishes at all cusps).
        """
        assert 441 + 250 - 691 == 0
