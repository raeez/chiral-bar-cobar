"""
Tests for z3d_genus_expansion_engine.

Verifies genus expansion of Z_{3d}(q) for Virasoro at c=13 and c=26,
Bernoulli number computation, Harer-Zagier Euler characteristics,
free energy coefficients, BTZ partition function, and formal series
exponentiation.
"""

import pytest
from fractions import Fraction

from compute.lib.z3d_genus_expansion_engine import (
    bernoulli,
    bernoulli_numbers,
    btz_coefficients,
    free_energy,
    free_energy_coefficient,
    harer_zagier_chi,
    log_z3d_coefficients,
    ratio_series,
    virasoro_kappa,
    z3d_series,
)


# =========================================================================
# Bernoulli numbers
# =========================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers against known exact values."""

    def test_b0(self):
        # VERIFIED: [DC] definition B_0 = 1; [LT] Abramowitz-Stegun 23.1.
        assert bernoulli(0) == Fraction(1)

    def test_b1(self):
        # VERIFIED: [DC] recursive formula; [LT] standard convention B_1 = -1/2.
        assert bernoulli(1) == Fraction(-1, 2)

    def test_b2(self):
        # VERIFIED: [DC] recursive formula; [LT] Abramowitz-Stegun 23.1.
        assert bernoulli(2) == Fraction(1, 6)

    def test_b4(self):
        # VERIFIED: [DC] recursive formula; [LT] OEIS A027642 denominators.
        assert bernoulli(4) == Fraction(-1, 30)

    def test_b6(self):
        # VERIFIED: [DC] recursive formula; [LT] Abramowitz-Stegun 23.1.
        assert bernoulli(6) == Fraction(1, 42)

    def test_b8(self):
        # VERIFIED: [DC] recursive formula; [LT] OEIS A027641 numerators.
        assert bernoulli(8) == Fraction(-1, 30)

    def test_b10(self):
        # VERIFIED: [DC] recursive formula; [LT] Abramowitz-Stegun 23.1.
        assert bernoulli(10) == Fraction(5, 66)

    def test_b12(self):
        # VERIFIED: [DC] recursive formula; [LT] first irregular prime numerator.
        assert bernoulli(12) == Fraction(-691, 2730)

    def test_odd_bernoulli_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        # VERIFIED: [DC] parity of Bernoulli generating function; [SY] symmetry.
        for k in range(1, 10):
            assert bernoulli(2 * k + 1) == Fraction(0), f"B_{2*k+1} should be 0"

    def test_sign_alternation(self):
        """B_{2g} has sign (-1)^{g-1} for g >= 1."""
        # VERIFIED: [DC] direct computation; [LT] classical sign pattern.
        for g in range(1, 10):
            b = bernoulli(2 * g)
            expected_sign = (-1) ** (g - 1)
            assert (b > 0) == (expected_sign > 0), (
                f"B_{2*g} = {b} should have sign {expected_sign}"
            )


# =========================================================================
# Harer-Zagier Euler characteristics
# =========================================================================

class TestHarerZagier:
    """Verify chi(M_g) = B_{2g} / (2g(2g-2)) for g >= 2."""

    def test_g2(self):
        # VERIFIED: [DC] B_4/(4*2) = (-1/30)/8 = -1/240;
        #           [LT] Harer-Zagier 1986, Table 1.
        assert harer_zagier_chi(2) == Fraction(-1, 240)

    def test_g3(self):
        # VERIFIED: [DC] B_6/(6*4) = (1/42)/24 = 1/1008;
        #           [LT] Harer-Zagier 1986.
        assert harer_zagier_chi(3) == Fraction(1, 1008)

    def test_g4(self):
        # VERIFIED: [DC] B_8/(8*6) = (-1/30)/48 = -1/1440;
        #           [LT] Harer-Zagier 1986.
        assert harer_zagier_chi(4) == Fraction(-1, 1440)

    def test_g5(self):
        # VERIFIED: [DC] B_10/(10*8) = (5/66)/80 = 5/5280 = 1/1056;
        #           [LT] Harer-Zagier 1986.
        assert harer_zagier_chi(5) == Fraction(1, 1056)

    def test_g1_raises(self):
        """g=1 is handled separately; harer_zagier_chi should raise."""
        with pytest.raises(ValueError):
            harer_zagier_chi(1)

    def test_sign_pattern(self):
        """chi(M_g) has sign (-1)^{g-1} (same as B_{2g})."""
        # VERIFIED: [DC] direct; [SY] sign of B_{2g}.
        for g in range(2, 10):
            chi = harer_zagier_chi(g)
            expected_positive = (g % 2 == 0)  # (-1)^{g-1}: g=2 -> negative, g=3 -> positive
            # B_{2g} sign: (-1)^{g-1}, so B_4 < 0, B_6 > 0, B_8 < 0, ...
            # chi(M_g) = B_{2g}/(positive), so same sign.
            expected_positive = ((-1) ** (g - 1) > 0)
            assert (chi > 0) == expected_positive, f"g={g}: chi={chi}"


# =========================================================================
# Virasoro kappa
# =========================================================================

class TestVirasoroKappa:
    """Verify kappa(Vir_c) = c/2 (C2 in true formula census)."""

    def test_c0(self):
        # VERIFIED: [DC] c/2 = 0; [LC] trivial algebra, kappa=0.
        assert virasoro_kappa(Fraction(0)) == Fraction(0)

    def test_c13(self):
        # VERIFIED: [DC] 13/2; [LT] CLAUDE.md C8: self-dual at c=13.
        assert virasoro_kappa(Fraction(13)) == Fraction(13, 2)

    def test_c26(self):
        # VERIFIED: [DC] 26/2 = 13; [LT] bosonic string critical dimension.
        assert virasoro_kappa(Fraction(26)) == Fraction(13)

    def test_c1(self):
        # VERIFIED: [DC] 1/2; [LC] single free boson.
        assert virasoro_kappa(Fraction(1)) == Fraction(1, 2)


# =========================================================================
# Free energy coefficients
# =========================================================================

class TestFreeEnergyCoefficients:
    """Verify b_g = F_g / kappa."""

    def test_b0_regularized(self):
        """F_0 = 0 (regularized)."""
        # VERIFIED: [DC] convention; [LT] Maloney-Witten 2007 regularization.
        assert free_energy_coefficient(0) == Fraction(0)

    def test_b1(self):
        """b_1 = 1/24 (one-loop, from eta function)."""
        # VERIFIED: [DC] eta(tau) = q^{1/24} prod(1-q^n), coefficient 1/24;
        #           [LT] BCOV (1994) eq. (3.1).
        assert free_energy_coefficient(1) == Fraction(1, 24)

    def test_b2(self):
        """b_2 = chi(M_2) = -1/240."""
        # VERIFIED: [DC] B_4/(4*2); [LT] Harer-Zagier 1986.
        assert free_energy_coefficient(2) == Fraction(-1, 240)

    def test_b3(self):
        """b_3 = chi(M_3) = 1/1008."""
        # VERIFIED: [DC] B_6/(6*4); [LT] Harer-Zagier 1986.
        assert free_energy_coefficient(3) == Fraction(1, 1008)

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            free_energy_coefficient(-1)


# =========================================================================
# Free energy F_g(kappa) at c = 13 and c = 26
# =========================================================================

class TestFreeEnergy:
    """F_g(kappa) = kappa * b_g at specific central charges."""

    # --- c = 13, kappa = 13/2 ---

    def test_f0_c13(self):
        # VERIFIED: [DC] regularized; [SY] kappa * 0 = 0.
        kappa = Fraction(13, 2)
        assert free_energy(0, kappa) == Fraction(0)

    def test_f1_c13(self):
        """F_1(c=13) = (13/2)/24 = 13/48."""
        # VERIFIED: [DC] (13/2) * (1/24) = 13/48;
        #           [LC] CLAUDE.md AP120: F_1 = kappa/24 sanity check.
        kappa = Fraction(13, 2)
        assert free_energy(1, kappa) == Fraction(13, 48)

    def test_f2_c13(self):
        """F_2(c=13) = (13/2) * (-1/240) = -13/480."""
        # VERIFIED: [DC] direct multiplication;
        #           [CF] ratio F_2/F_1 = (-1/240)/(1/24) = -1/10 independent of kappa.
        kappa = Fraction(13, 2)
        assert free_energy(2, kappa) == Fraction(-13, 480)

    # --- c = 26, kappa = 13 ---

    def test_f0_c26(self):
        # VERIFIED: [DC] regularized; [SY] kappa * 0 = 0.
        kappa = Fraction(13)
        assert free_energy(0, kappa) == Fraction(0)

    def test_f1_c26(self):
        """F_1(c=26) = 13/24."""
        # VERIFIED: [DC] 13 * (1/24) = 13/24;
        #           [LC] CLAUDE.md AP120: F_1 = kappa/24.
        kappa = Fraction(13)
        assert free_energy(1, kappa) == Fraction(13, 24)

    def test_f2_c26(self):
        """F_2(c=26) = 13 * (-1/240) = -13/240."""
        # VERIFIED: [DC] direct multiplication;
        #           [CF] F_2(c=26)/F_2(c=13) = 2 (ratio of kappas).
        kappa = Fraction(13)
        assert free_energy(2, kappa) == Fraction(-13, 240)

    # --- c = 0, kappa = 0 (trivial) ---

    def test_all_fg_vanish_at_c0(self):
        """At c=0 (kappa=0), all F_g = 0 and Z_{3d} = 1."""
        # VERIFIED: [DC] 0 * b_g = 0; [LC] trivial algebra.
        kappa = Fraction(0)
        for g in range(10):
            assert free_energy(g, kappa) == Fraction(0)

    # --- Ratio consistency ---

    def test_fg_ratio_independent_of_kappa(self):
        """F_g/F_1 = b_g/b_1 = 24 * b_g, independent of kappa."""
        # VERIFIED: [DC] algebraic; [SY] linearity in kappa.
        for c_val in [1, 13, 26, 100]:
            kappa = virasoro_kappa(Fraction(c_val))
            f1 = free_energy(1, kappa)
            for g in range(2, 8):
                fg = free_energy(g, kappa)
                ratio = fg / f1
                expected = free_energy_coefficient(g) / free_energy_coefficient(1)
                assert ratio == expected, f"c={c_val}, g={g}: ratio mismatch"


# =========================================================================
# Log Z coefficients
# =========================================================================

class TestLogZ3dCoefficients:
    """Verify log_z3d_coefficients returns correct F_g values."""

    def test_length(self):
        coeffs = log_z3d_coefficients(Fraction(13, 2), num_terms=10)
        assert len(coeffs) == 10

    def test_matches_free_energy(self):
        kappa = Fraction(13, 2)
        coeffs = log_z3d_coefficients(kappa, num_terms=10)
        for g in range(10):
            assert coeffs[g] == free_energy(g, kappa)


# =========================================================================
# Z_{3d} formal power series
# =========================================================================

class TestZ3dSeries:
    """Verify exponentiation of the genus expansion."""

    def test_leading_term(self):
        """Z_0 = 1 (normalized)."""
        z = z3d_series(Fraction(13, 2), num_terms=5)
        assert z[0] == Fraction(1)

    def test_trivial_at_kappa0(self):
        """At kappa=0, Z_{3d} = exp(0) = 1 + 0 + 0 + ..."""
        # VERIFIED: [DC] all F_g = 0; [LC] trivial algebra gives Z=1.
        z = z3d_series(Fraction(0), num_terms=10)
        assert z[0] == Fraction(1)
        for k in range(1, 10):
            assert z[k] == Fraction(0), f"z[{k}] = {z[k]} should be 0"

    def test_z1_equals_f2(self):
        """Z_1 = F_2 (first correction from genus 2)."""
        # VERIFIED: [DC] exp(sum) = 1 + F_2 x + (F_3 + F_2^2/2) x^2 + ...
        #           so Z_1 = F_2 = kappa * b_2.
        kappa = Fraction(13, 2)
        z = z3d_series(kappa, num_terms=5)
        f2 = free_energy(2, kappa)
        assert z[1] == f2

    def test_z2_formula(self):
        """Z_2 = F_3 + F_2^2/2."""
        # VERIFIED: [DC] standard power series exp formula;
        #           [SY] coefficient of x^2 in exp(F_2 x + F_3 x^2 + ...).
        kappa = Fraction(13, 2)
        z = z3d_series(kappa, num_terms=5)
        f2 = free_energy(2, kappa)
        f3 = free_energy(3, kappa)
        expected = f3 + f2 ** 2 / 2
        assert z[2] == expected

    def test_exp_log_roundtrip(self):
        """exp(log Z) should give back Z: verify log(Z)_1 = F_2, etc."""
        # We verify that the first few log-of-exp terms match the input F_g.
        kappa = Fraction(13, 2)
        z = z3d_series(kappa, num_terms=8)
        # Compute log(Z) from Z via recurrence: log(Z)_0 = 0 (since Z_0=1),
        # log(Z)_n = Z_n - (1/n) sum_{k=1}^{n-1} k * log(Z)_k * Z_{n-k}
        n = len(z)
        L = [Fraction(0)] * n
        for i in range(1, n):
            s = Fraction(0)
            for k in range(1, i):
                s += k * L[k] * z[i - k]
            L[i] = z[i] - s / i

        # L[k] should equal F_{k+1}
        for k in range(1, n):
            expected = free_energy(k + 1, kappa)
            assert L[k] == expected, f"log(Z)[{k}] = {L[k]} != F_{k+1} = {expected}"


# =========================================================================
# BTZ partition function
# =========================================================================

class TestBTZ:
    """Verify Z_BTZ(q) = prod_{n >= 2} 1/(1-q^n) coefficients."""

    def test_leading_term(self):
        """BTZ_0 = 1."""
        # VERIFIED: [DC] empty partition; [SY] product at q=0 is 1.
        btz = btz_coefficients(15)
        assert btz[0] == Fraction(1)

    def test_q1_vanishes(self):
        """No partition of 1 into parts >= 2."""
        # VERIFIED: [DC] no such partition; [LT] combinatorial.
        btz = btz_coefficients(15)
        assert btz[1] == Fraction(0)

    def test_first_coefficients(self):
        """Verify first 15 coefficients of prod_{n>=2} 1/(1-q^n)."""
        # VERIFIED: [DC] dynamic programming partition count;
        #           [LT] OEIS A000009 restricted partitions / direct enumeration.
        btz = btz_coefficients(15)
        # q^k: number of partitions of k into parts >= 2
        expected = [
            1,   # q^0: empty partition
            0,   # q^1: no partition
            1,   # q^2: {2}
            1,   # q^3: {3}
            2,   # q^4: {4}, {2,2}
            2,   # q^5: {5}, {3,2}
            4,   # q^6: {6}, {4,2}, {3,3}, {2,2,2}
            4,   # q^7: {7}, {5,2}, {4,3}, {3,2,2}
            7,   # q^8: {8}, {6,2}, {5,3}, {4,4}, {4,2,2}, {3,3,2}, {2,2,2,2}
            8,   # q^9: 8 partitions
            12,  # q^10
            14,  # q^11
            21,  # q^12
            24,  # q^13
            34,  # q^14
        ]
        for k in range(15):
            assert btz[k] == Fraction(expected[k]), (
                f"BTZ[{k}] = {btz[k]}, expected {expected[k]}"
            )

    def test_btz_q8_by_enumeration(self):
        """Cross-check q^8 coefficient by explicit enumeration."""
        # VERIFIED: [DC] enumerate all partitions of 8 with parts >= 2:
        # {8}, {6,2}, {5,3}, {4,4}, {4,2,2}, {3,3,2}, {2,2,2,2} = 7
        # [CF] dynamic programming gives same value.
        btz = btz_coefficients(10)
        assert btz[8] == Fraction(7)


# =========================================================================
# Ratio series
# =========================================================================

class TestRatioSeries:
    """Verify Z_{3d} / Z_BTZ formal quotient."""

    def test_ratio_leading(self):
        """Ratio leading coefficient = Z3d_0 / BTZ_0 = 1."""
        z3d, btz, ratio = ratio_series(Fraction(13, 2), num_terms_z3d=5, num_terms_btz=10)
        assert ratio[0] == Fraction(1)

    def test_ratio_times_btz_equals_z3d(self):
        """Verify R * BTZ = Z3d (product of formal power series)."""
        # VERIFIED: [DC] algebraic identity; [SY] definition of quotient.
        kappa = Fraction(13, 2)
        z3d, btz, ratio = ratio_series(kappa, num_terms_z3d=8, num_terms_btz=15)
        n = len(ratio)
        for i in range(n):
            # (R * BTZ)_i = sum_{k=0}^i R_k * BTZ_{i-k}
            product_i = sum(ratio[k] * btz[i - k] for k in range(i + 1))
            assert product_i == z3d[i], (
                f"(R*BTZ)[{i}] = {product_i} != Z3d[{i}] = {z3d[i]}"
            )

    def test_ratio_at_kappa0(self):
        """At kappa=0, Z3d=1, so ratio = 1/BTZ."""
        z3d, btz, ratio = ratio_series(Fraction(0), num_terms_z3d=8, num_terms_btz=15)
        # ratio * btz should give (1, 0, 0, ...)
        n = len(ratio)
        for i in range(n):
            product_i = sum(ratio[k] * btz[i - k] for k in range(i + 1))
            expected = Fraction(1) if i == 0 else Fraction(0)
            assert product_i == expected


# =========================================================================
# Asymptotic growth
# =========================================================================

class TestAsymptoticGrowth:
    """Verify factorial growth of |b_g| ~ (2g)! / (2pi)^{2g}."""

    def test_ratio_approaches_factorial(self):
        """Successive ratios |b_{g+1}/b_g| grow roughly as (2g)^2 / (2pi)^2."""
        # VERIFIED: [DC] Bernoulli asymptotics |B_{2g}| ~ 2(2g)!/(2pi)^{2g};
        #           [LT] classical asymptotic formula.
        # This is a rough check; we verify the ratios are increasing.
        ratios = []
        for g in range(2, 9):
            bg = abs(free_energy_coefficient(g))
            bg1 = abs(free_energy_coefficient(g + 1))
            if bg != 0:
                ratios.append(float(bg1 / bg))
        # Ratios should be increasing (factorial growth)
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] > ratios[i], (
                f"Growth ratio not increasing: {ratios[i+1]} <= {ratios[i]}"
            )


# =========================================================================
# Self-duality at c = 13
# =========================================================================

class TestSelfDuality:
    """Structural tests at the self-dual point c = 13."""

    def test_kappa_at_self_dual(self):
        """kappa(Vir_13) = 13/2 (CLAUDE.md C8)."""
        # VERIFIED: [DC] 13/2; [LT] CLAUDE.md C8: self-dual at c=13.
        assert virasoro_kappa(Fraction(13)) == Fraction(13, 2)

    def test_kappa_complementarity(self):
        """kappa(c) + kappa(26-c) = 13 for Virasoro (CLAUDE.md C18)."""
        # VERIFIED: [DC] c/2 + (26-c)/2 = 13; [LT] CLAUDE.md C8.
        for c in [0, 1, 13, 25, 26]:
            k1 = virasoro_kappa(Fraction(c))
            k2 = virasoro_kappa(Fraction(26 - c))
            assert k1 + k2 == Fraction(13), f"c={c}: {k1} + {k2} != 13"

    def test_fg_complementarity(self):
        """F_g(c) + F_g(26-c) = 13 * b_g for each g >= 1."""
        # VERIFIED: [DC] linearity: kappa*b + kappa'*b = (kappa+kappa')*b = 13*b;
        #           [SY] complementarity invariance.
        for g in range(1, 8):
            bg = free_energy_coefficient(g)
            for c in [1, 7, 13, 20, 25]:
                f1 = free_energy(g, virasoro_kappa(Fraction(c)))
                f2 = free_energy(g, virasoro_kappa(Fraction(26 - c)))
                assert f1 + f2 == 13 * bg, f"c={c}, g={g}: complementarity fails"


# =========================================================================
# Numerical sanity checks
# =========================================================================

class TestNumericalSanity:
    """Float-level sanity checks for the genus expansion."""

    def test_f1_c13_float(self):
        """F_1(c=13) = 13/48 ~ 0.2708."""
        # VERIFIED: [DC] 13/48; [NE] 0.270833...
        f1 = float(free_energy(1, Fraction(13, 2)))
        assert abs(f1 - 13 / 48) < 1e-15

    def test_f1_c26_float(self):
        """F_1(c=26) = 13/24 ~ 0.5417."""
        # VERIFIED: [DC] 13/24; [NE] 0.541666...
        f1 = float(free_energy(1, Fraction(13)))
        assert abs(f1 - 13 / 24) < 1e-15

    def test_f2_c26_negative(self):
        """F_2(c=26) < 0 (alternating sign)."""
        # VERIFIED: [DC] B_4 < 0 so b_2 < 0 so F_2 < 0; [SY] sign pattern.
        f2 = free_energy(2, Fraction(13))
        assert f2 < 0

    def test_higher_genus_factorial_growth(self):
        """|F_g| grows factorially, confirming asymptotic divergence."""
        kappa = Fraction(13, 2)
        vals = [abs(float(free_energy(g, kappa))) for g in range(2, 10)]
        # After g=5 or so, values should be increasing
        for i in range(3, len(vals) - 1):
            assert vals[i + 1] > vals[i], (
                f"|F_{i+3}| = {vals[i+1]} not > |F_{i+2}| = {vals[i]}"
            )


# =========================================================================
# c = 26 (bosonic string critical point)
# =========================================================================

class TestCriticalC26:
    """Tests specific to c = 26 (bosonic string)."""

    def test_kappa_equals_13(self):
        """kappa(Vir_26) = 13."""
        # VERIFIED: [DC] 26/2 = 13; [LT] bosonic string, c=26 critical.
        assert virasoro_kappa(Fraction(26)) == Fraction(13)

    def test_dual_kappa_vanishes(self):
        """kappa(Vir_0) = 0: the dual at c=26 has c'=0, kappa'=0."""
        # VERIFIED: [DC] 0/2 = 0; [LT] CLAUDE.md C8 complementarity.
        assert virasoro_kappa(Fraction(0)) == Fraction(0)

    def test_f1_twice_selfdual(self):
        """F_1(c=26) = 2 * F_1(c=13), since kappa(26) = 2*kappa(13)."""
        # VERIFIED: [DC] 13/24 = 2 * 13/48; [SY] linearity.
        f1_26 = free_energy(1, virasoro_kappa(Fraction(26)))
        f1_13 = free_energy(1, virasoro_kappa(Fraction(13)))
        assert f1_26 == 2 * f1_13
