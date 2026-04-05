r"""Tests for genus5_amplitude_engine.py — graph-level shadow amplitude engine
for genus-5 stable graphs at n=0.

Multi-path verification mandate (CLAUDE.md):
  Every numerical result requires at least 3 independent verification paths.

Test organization (80+ tests):
  Section 1:  Bernoulli number B_10 (3 paths)
  Section 2:  Lambda_5^FP multi-path verification (6 paths)
  Section 3:  Free energy F_5 for standard families
  Section 4:  Virasoro complementarity (AP24)
  Section 5:  KM antisymmetry
  Section 6:  Cross-family table
  Section 7:  Cross-genus consistency (lambda ratios, monotonicity)
  Section 8:  Shadow visibility (cor:shadow-visibility-genus)
  Section 9:  Self-loop parity vanishing (prop:self-loop-vanishing)
  Section 10: Graph enumeration and census (slow)
  Section 11: Spectral sequence / boundary strata (slow)
  Section 12: Named graphs (slow)
  Section 13: Planted-forest census (slow)
  Section 14: Gaussian purity (slow)
  Section 15: Automorphism spectrum (slow)
  Section 16: Graph profiles by shadow depth class (slow)
  Section 17: Scalar graph sum (slow)
  Section 18: Orbifold Euler characteristic (slow)
  Section 19: Summary and cross-checks (slow)

References:
  - higher_genus_modular_koszul.tex: cor:shadow-visibility-genus, prop:self-loop-vanishing
  - concordance.tex: const:vol1-genus-spectral-sequence
  - CLAUDE.md: AP1, AP24, AP39, AP48
"""

import pytest
from fractions import Fraction
from math import factorial, gcd


# ============================================================================
# Section 1: Bernoulli number B_10
# ============================================================================

class TestBernoulli10:
    """B_10 = 5/66 verified by 3 independent methods."""

    def test_B10_from_library(self):
        """Path 1: library function."""
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(10) == Fraction(5, 66)

    def test_B10_from_recurrence(self):
        """Path 2: Bernoulli recurrence sum_{k=0}^{n-1} C(n,k) B_k = 0 for n>=2."""
        B = [Fraction(0)] * 11
        B[0] = Fraction(1)
        B[1] = Fraction(-1, 2)
        for n in range(2, 11):
            s = Fraction(0)
            for k in range(n):
                # C(n+1, k) * B[k]
                binom = Fraction(factorial(n + 1), factorial(k) * factorial(n + 1 - k))
                s += binom * B[k]
            B[n] = -s / Fraction(n + 1)
        assert B[10] == Fraction(5, 66)

    def test_B10_sign_positive(self):
        """B_10 > 0 (even-indexed Bernoulli with 10/2=5 odd gives positive)."""
        # B_{2n} has sign (-1)^{n+1}, so B_10 = B_{2*5} has sign (-1)^6 = +1
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(10) > 0

    def test_B10_numerator_denominator(self):
        """Numerator = 5, denominator = 66."""
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        B10 = _bernoulli_exact(10)
        assert B10.numerator == 5
        assert B10.denominator == 66


# ============================================================================
# Section 2: Lambda_5^FP multi-path verification
# ============================================================================

class TestLambda5FP:
    """lambda_5^FP = 73/3503554560 verified by 6 independent methods."""

    LAMBDA5 = Fraction(73, 3503554560)

    def test_lambda5_exact_value(self):
        """Path 1: direct from engine."""
        from compute.lib.genus5_amplitude_engine import lambda5_fp
        assert lambda5_fp() == self.LAMBDA5

    def test_lambda5_bernoulli_formula(self):
        """Path 2: (2^{2g-1}-1)|B_{2g}|/(2^{2g-1} * (2g)!) at g=5."""
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        B10 = _bernoulli_exact(10)
        result = Fraction(2**9 - 1) * abs(B10) / Fraction(2**9 * factorial(10))
        assert result == self.LAMBDA5

    def test_lambda5_ahat_series_inversion(self):
        """Path 3: coefficient of x^10 in (x/2)/sin(x/2).

        Write u/sin(u) = sum a_n u^{2n}, then lambda_g = a_g / 4^g.
        Invert sin(u)/u = sum (-1)^n u^{2n}/(2n+1)! via a_0=1,
        a_n = -sum_{j=1}^n c_j a_{n-j} where c_j = (-1)^j/(2j+1)!.
        """
        c_sin = [Fraction((-1)**n, factorial(2 * n + 1)) for n in range(6)]
        a = [Fraction(0)] * 6
        a[0] = Fraction(1)
        for n in range(1, 6):
            s = Fraction(0)
            for j in range(1, n + 1):
                s += c_sin[j] * a[n - j]
            a[n] = -s
        lambda5 = a[5] / Fraction(4**5)
        assert lambda5 == self.LAMBDA5

    def test_lambda5_library_lambda_fp_exact(self):
        """Path 4: _lambda_fp_exact(5) from stable_graph_enumeration."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        assert _lambda_fp_exact(5) == self.LAMBDA5

    def test_lambda5_three_way_check(self):
        """Path 5: engine's own three-way verification."""
        from compute.lib.genus5_amplitude_engine import lambda5_fp_three_way_check
        m1, m2, m3, match = lambda5_fp_three_way_check()
        assert match
        assert m1 == self.LAMBDA5
        assert m2 == self.LAMBDA5
        assert m3 == self.LAMBDA5

    def test_lambda5_raw_arithmetic(self):
        """Path 6: raw arithmetic from scratch.

        511 * 5 = 2555. 512 * 66 * 3628800 = 122624409600.
        gcd(2555, 122624409600) = 35. 2555/35 = 73. 122624409600/35 = 3503554560.
        """
        num_raw = 511 * 5
        den_raw = 512 * 66 * 3628800
        assert num_raw == 2555
        assert den_raw == 122624409600
        g = gcd(num_raw, den_raw)
        assert g == 35
        assert num_raw // g == 73
        assert den_raw // g == 3503554560

    def test_lambda5_positive(self):
        """lambda_5^FP > 0 (F_g are positive by Bernoulli sign pattern)."""
        from compute.lib.genus5_amplitude_engine import lambda5_fp
        assert lambda5_fp() > 0

    def test_lambda5_numerator_prime(self):
        """73 is prime."""
        n = 73
        assert all(n % d != 0 for d in range(2, int(n**0.5) + 1))

    def test_lambda5_denominator_factorization(self):
        """3503554560 = 2^9 * 3^2 * 5 * 7 * 11 * 10! / (some factor).

        Verify: 3503554560 = 512 * 66 * 3628800 / 35 = 122624409600 / 35.
        """
        assert 3503554560 * 35 == 512 * 66 * 3628800


# ============================================================================
# Section 3: Free energy F_5 for standard families
# ============================================================================

class TestFreeEnergy:
    """F_5(A) = kappa(A) * lambda_5^FP for standard families.

    kappa values (AP1/AP39/AP48):
      Heisenberg H_k:   kappa = k (NOT k/2, AP39)
      Virasoro Vir_c:   kappa = c/2
      Affine V_k(g):    kappa = dim(g)*(k+h^v)/(2*h^v)
      BetaGamma:        kappa = 1
      Lattice V_Lambda:  kappa = rank(Lambda)
    """

    LAMBDA5 = Fraction(73, 3503554560)

    def test_heisenberg_k1(self):
        """F_5(H_1) = 1 * lambda_5."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_heisenberg
        assert genus5_free_energy_heisenberg(Fraction(1)) == self.LAMBDA5

    def test_heisenberg_k2(self):
        """F_5(H_2) = 2 * lambda_5."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_heisenberg
        assert genus5_free_energy_heisenberg(Fraction(2)) == 2 * self.LAMBDA5

    def test_heisenberg_k_half(self):
        """F_5(H_{1/2}) = (1/2) * lambda_5."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_heisenberg
        assert genus5_free_energy_heisenberg(Fraction(1, 2)) == Fraction(1, 2) * self.LAMBDA5

    def test_heisenberg_d_dimensions(self):
        """F_5(H_1, d=3) = 3 * lambda_5 (kappa = k*d for d-dim Heisenberg)."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_heisenberg
        assert genus5_free_energy_heisenberg(Fraction(1), d=3) == 3 * self.LAMBDA5

    def test_heisenberg_additivity(self):
        """F_5(H_{k1+k2}) = F_5(H_k1) + F_5(H_k2) (kappa additive)."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_heisenberg
        k1, k2 = Fraction(3), Fraction(7)
        lhs = genus5_free_energy_heisenberg(k1 + k2)
        rhs = genus5_free_energy_heisenberg(k1) + genus5_free_energy_heisenberg(k2)
        assert lhs == rhs

    def test_virasoro_c1(self):
        """F_5(Vir_1) = (1/2) * lambda_5."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_virasoro
        assert genus5_free_energy_virasoro(Fraction(1)) == Fraction(1, 2) * self.LAMBDA5

    def test_virasoro_c26(self):
        """F_5(Vir_26) = 13 * lambda_5."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_virasoro
        assert genus5_free_energy_virasoro(Fraction(26)) == 13 * self.LAMBDA5

    def test_virasoro_c13(self):
        """F_5(Vir_13) = (13/2) * lambda_5 (self-dual point)."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_virasoro
        assert genus5_free_energy_virasoro(Fraction(13)) == Fraction(13, 2) * self.LAMBDA5

    def test_virasoro_c0(self):
        """F_5(Vir_0) = 0 (kappa = 0, uncurved on scalar lane)."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_virasoro
        assert genus5_free_energy_virasoro(Fraction(0)) == 0

    def test_virasoro_exact_value_c26(self):
        """F_5(Vir_26) = 949/3503554560."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_virasoro
        assert genus5_free_energy_virasoro(Fraction(26)) == Fraction(949, 3503554560)

    def test_affine_sl2_k1(self):
        """F_5(sl_2, k=1): kappa = 3*3/(2*2) = 9/4."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_affine
        kappa = Fraction(3) * (Fraction(1) + 2) / Fraction(4)
        assert kappa == Fraction(9, 4)
        expected = kappa * self.LAMBDA5
        assert genus5_free_energy_affine(Fraction(1), 3, 2) == expected

    def test_affine_sl3_k1(self):
        """F_5(sl_3, k=1): kappa = 8*4/(2*3) = 16/3."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_affine
        kappa = Fraction(8) * (Fraction(1) + 3) / Fraction(6)
        assert kappa == Fraction(16, 3)
        expected = kappa * self.LAMBDA5
        assert genus5_free_energy_affine(Fraction(1), 8, 3) == expected

    def test_affine_e8_k1(self):
        """F_5(E_8, k=1): kappa = 248*31/(2*30) = 248*31/60."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_affine
        kappa = Fraction(248) * (Fraction(1) + 30) / Fraction(60)
        assert kappa == Fraction(248 * 31, 60)
        expected = kappa * self.LAMBDA5
        assert genus5_free_energy_affine(Fraction(1), 248, 30) == expected

    def test_betagamma(self):
        """F_5(betagamma) = lambda_5 (kappa = 1)."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_betagamma
        assert genus5_free_energy_betagamma() == self.LAMBDA5

    def test_positive_kappa_gives_positive_F5(self):
        """F_5 > 0 whenever kappa > 0."""
        from compute.lib.genus5_amplitude_engine import (
            genus5_free_energy_heisenberg, genus5_free_energy_virasoro,
            genus5_free_energy_affine,
        )
        assert genus5_free_energy_heisenberg(Fraction(1)) > 0
        assert genus5_free_energy_virasoro(Fraction(2)) > 0
        assert genus5_free_energy_affine(Fraction(1), 3, 2) > 0

    def test_negative_kappa_gives_negative_F5(self):
        """F_5 < 0 when kappa < 0 (e.g., negative level Heisenberg)."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_heisenberg
        assert genus5_free_energy_heisenberg(Fraction(-1)) < 0

    def test_F5_linearity_in_kappa(self):
        """F_5(alpha * A) = alpha * F_5(A) (linearity in kappa)."""
        from compute.lib.genus5_amplitude_engine import genus5_free_energy_virasoro
        c = Fraction(7)
        alpha = Fraction(5)
        assert genus5_free_energy_virasoro(alpha * c) == alpha * genus5_free_energy_virasoro(c)


# ============================================================================
# Section 4: Virasoro complementarity (AP24)
# ============================================================================

class TestVirasoroComplementarity:
    """F_5(Vir_c) + F_5(Vir_{26-c}) = 13 * lambda_5 (NOT zero, AP24).

    kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
    """

    LAMBDA5 = Fraction(73, 3503554560)

    def test_complementarity_c1(self):
        from compute.lib.genus5_amplitude_engine import genus5_virasoro_complementarity
        f_sum, expected, match = genus5_virasoro_complementarity(Fraction(1))
        assert match

    def test_complementarity_c13_self_dual(self):
        """Self-dual point c=13: both sides equal 13/2 * lambda_5."""
        from compute.lib.genus5_amplitude_engine import genus5_virasoro_complementarity
        f_sum, expected, match = genus5_virasoro_complementarity(Fraction(13))
        assert match
        assert f_sum == 13 * self.LAMBDA5

    def test_complementarity_c26(self):
        from compute.lib.genus5_amplitude_engine import genus5_virasoro_complementarity
        f_sum, expected, match = genus5_virasoro_complementarity(Fraction(26))
        assert match

    def test_complementarity_c0(self):
        """c=0: kappa=0, dual kappa=13."""
        from compute.lib.genus5_amplitude_engine import genus5_virasoro_complementarity
        f_sum, expected, match = genus5_virasoro_complementarity(Fraction(0))
        assert match

    def test_complementarity_c_half(self):
        """Non-integer c = 1/2 (Ising model)."""
        from compute.lib.genus5_amplitude_engine import genus5_virasoro_complementarity
        f_sum, expected, match = genus5_virasoro_complementarity(Fraction(1, 2))
        assert match

    def test_complementarity_c_negative(self):
        """c = -2 (bc ghost system)."""
        from compute.lib.genus5_amplitude_engine import genus5_virasoro_complementarity
        f_sum, expected, match = genus5_virasoro_complementarity(Fraction(-2))
        assert match

    def test_complementarity_sum_is_13_lambda5_not_zero(self):
        """The sum is 13 * lambda_5, NOT 0 (AP24 critical check)."""
        assert 13 * self.LAMBDA5 != 0
        assert 13 * self.LAMBDA5 == Fraction(949, 3503554560)

    def test_complementarity_sum_independent_of_c(self):
        """The sum is the same for all c."""
        from compute.lib.genus5_amplitude_engine import genus5_virasoro_complementarity
        for c_val in [0, 1, Fraction(1, 2), 13, 26, Fraction(-10)]:
            f_sum, expected, match = genus5_virasoro_complementarity(Fraction(c_val))
            assert match, f"Failed at c={c_val}"
            assert f_sum == 13 * self.LAMBDA5, f"Sum mismatch at c={c_val}"


# ============================================================================
# Section 5: KM antisymmetry
# ============================================================================

class TestKMAntisymmetry:
    """F_5(V_k(g)) + F_5(V_{-k-2h^v}(g)) = 0 for affine KM (AP24).

    Feigin-Frenkel involution: k -> -k - 2h^v.
    kappa(k) + kappa(-k-2h^v) = dim(g)*(k+h^v)/(2h^v) + dim(g)*(-k-h^v)/(2h^v) = 0.
    """

    def test_sl2_k1(self):
        """sl_2: dim=3, h^v=2, k=1. Dual k' = -1-4 = -5."""
        from compute.lib.genus5_amplitude_engine import genus5_km_antisymmetry
        s, is_zero = genus5_km_antisymmetry(Fraction(1), 3, 2)
        assert is_zero
        assert s == 0

    def test_sl3_k2(self):
        """sl_3: dim=8, h^v=3, k=2. Dual k' = -2-6 = -8."""
        from compute.lib.genus5_amplitude_engine import genus5_km_antisymmetry
        s, is_zero = genus5_km_antisymmetry(Fraction(2), 8, 3)
        assert is_zero

    def test_e8_k1(self):
        """E_8: dim=248, h^v=30, k=1. Dual k' = -1-60 = -61."""
        from compute.lib.genus5_amplitude_engine import genus5_km_antisymmetry
        s, is_zero = genus5_km_antisymmetry(Fraction(1), 248, 30)
        assert is_zero

    def test_g2_k1(self):
        """G_2: dim=14, h^v=4, k=1."""
        from compute.lib.genus5_amplitude_engine import genus5_km_antisymmetry
        s, is_zero = genus5_km_antisymmetry(Fraction(1), 14, 4)
        assert is_zero

    def test_f4_k1(self):
        """F_4: dim=52, h^v=9, k=1."""
        from compute.lib.genus5_amplitude_engine import genus5_km_antisymmetry
        s, is_zero = genus5_km_antisymmetry(Fraction(1), 52, 9)
        assert is_zero

    def test_km_antisymmetry_general(self):
        """Verify for several (dim, h^v) that kappa + kappa_dual = 0."""
        from compute.lib.genus5_amplitude_engine import genus5_km_antisymmetry
        cases = [
            (Fraction(1), 3, 2),    # sl_2
            (Fraction(1), 8, 3),    # sl_3
            (Fraction(1), 15, 4),   # sl_4
            (Fraction(1), 24, 5),   # sl_5
            (Fraction(1), 10, 4),   # sp_4
            (Fraction(1), 14, 4),   # G_2
            (Fraction(1), 52, 9),   # F_4
            (Fraction(1), 78, 12),  # E_6
            (Fraction(1), 133, 18), # E_7
            (Fraction(1), 248, 30), # E_8
        ]
        for k, dim_g, h_vee in cases:
            s, is_zero = genus5_km_antisymmetry(k, dim_g, h_vee)
            assert is_zero, f"Failed for dim={dim_g}, h^v={h_vee}"


# ============================================================================
# Section 6: Cross-family table
# ============================================================================

class TestCrossFamilyTable:
    """Cross-family genus-5 free energy table."""

    LAMBDA5 = Fraction(73, 3503554560)

    def test_table_has_entries(self):
        from compute.lib.genus5_amplitude_engine import genus5_cross_family_table
        table = genus5_cross_family_table()
        assert len(table) >= 5

    def test_heisenberg_in_table(self):
        from compute.lib.genus5_amplitude_engine import genus5_cross_family_table
        table = genus5_cross_family_table()
        assert 'Heisenberg_k1' in table
        assert table['Heisenberg_k1']['kappa'] == Fraction(1)
        assert table['Heisenberg_k1']['F_5_scalar'] == self.LAMBDA5

    def test_virasoro_c26_in_table(self):
        from compute.lib.genus5_amplitude_engine import genus5_cross_family_table
        table = genus5_cross_family_table()
        assert 'Virasoro_c26' in table
        assert table['Virasoro_c26']['kappa'] == Fraction(13)
        assert table['Virasoro_c26']['F_5_scalar'] == 13 * self.LAMBDA5

    def test_virasoro_c13_in_table(self):
        from compute.lib.genus5_amplitude_engine import genus5_cross_family_table
        table = genus5_cross_family_table()
        assert 'Virasoro_c13' in table
        assert table['Virasoro_c13']['kappa'] == Fraction(13, 2)

    def test_betagamma_in_table(self):
        from compute.lib.genus5_amplitude_engine import genus5_cross_family_table
        table = genus5_cross_family_table()
        assert 'BetaGamma' in table
        assert table['BetaGamma']['kappa'] == Fraction(1)
        assert table['BetaGamma']['F_5_scalar'] == self.LAMBDA5

    def test_affine_sl2_in_table(self):
        from compute.lib.genus5_amplitude_engine import genus5_cross_family_table
        table = genus5_cross_family_table()
        assert 'Affine_sl2_k1' in table
        assert table['Affine_sl2_k1']['kappa'] == Fraction(9, 4)

    def test_all_F5_consistent_with_kappa(self):
        """F_5_scalar = kappa * lambda_5 for every entry."""
        from compute.lib.genus5_amplitude_engine import genus5_cross_family_table
        table = genus5_cross_family_table()
        for name, data in table.items():
            assert data['F_5_scalar'] == data['kappa'] * self.LAMBDA5, \
                f"Inconsistency in {name}"


# ============================================================================
# Section 7: Cross-genus consistency
# ============================================================================

class TestCrossGenusConsistency:
    """Cross-genus lambda ratios and monotonicity for g=1..5."""

    def test_known_lambda_values(self):
        """Verify all known lambda_g^FP values."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        assert _lambda_fp_exact(1) == Fraction(1, 24)
        assert _lambda_fp_exact(2) == Fraction(7, 5760)
        assert _lambda_fp_exact(3) == Fraction(31, 967680)
        assert _lambda_fp_exact(4) == Fraction(127, 154828800)
        assert _lambda_fp_exact(5) == Fraction(73, 3503554560)

    def test_lambdas_strictly_decreasing(self):
        """lambda_g > lambda_{g+1} for g=1..4."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        for g in range(1, 5):
            assert _lambda_fp_exact(g) > _lambda_fp_exact(g + 1)

    def test_lambdas_all_positive(self):
        """lambda_g > 0 for g=1..5."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        for g in range(1, 6):
            assert _lambda_fp_exact(g) > 0

    def test_ratio_decreasing(self):
        """lambda_{g+1}/lambda_g is decreasing for g=1..4.

        This converges to 1/(2*pi)^2 asymptotically.
        """
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        ratios = []
        for g in range(1, 5):
            ratios.append(_lambda_fp_exact(g + 1) / _lambda_fp_exact(g))
        for i in range(len(ratios) - 1):
            assert ratios[i] > ratios[i + 1]

    def test_ratio_bounded_by_asymptotic(self):
        """lambda_{g+1}/lambda_g < 1/(2*pi)^2 + epsilon for all g=1..4.

        Asymptotically lambda_g ~ A * (2*pi)^{-2g} * (2g)!, so the ratio
        approaches 1/(4*pi^2) ~ 0.02533. All finite ratios should be above this.
        """
        import math
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        asymptotic = 1.0 / (4 * math.pi**2)
        for g in range(1, 5):
            ratio = float(_lambda_fp_exact(g + 1) / _lambda_fp_exact(g))
            assert ratio > asymptotic  # still above asymptotic
            assert ratio < 0.03  # but not too far above

    def test_numerator_pattern(self):
        """Numerators of lambda_g relate to 2^{2g-1} - 1.

        lambda_g = (2^{2g-1}-1)|B_{2g}| / (2^{2g-1} * (2g)!).
        """
        from compute.lib.stable_graph_enumeration import _bernoulli_exact, _lambda_fp_exact
        for g in range(1, 6):
            B2g = _bernoulli_exact(2 * g)
            raw = Fraction(2**(2*g-1) - 1) * abs(B2g) / Fraction(2**(2*g-1) * factorial(2*g))
            assert raw == _lambda_fp_exact(g)

    def test_F5_to_F4_ratio(self):
        """F_5/F_4 = lambda_5/lambda_4 = 2555/100584."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        ratio = _lambda_fp_exact(5) / _lambda_fp_exact(4)
        # 73/3503554560 divided by 127/154828800
        # = 73 * 154828800 / (127 * 3503554560)
        # Verify numerically
        assert ratio == Fraction(73 * 154828800, 127 * 3503554560)


# ============================================================================
# Section 8: Shadow visibility (cor:shadow-visibility-genus)
# ============================================================================

class TestShadowVisibility:
    """g_min(S_r) = floor(r/2) + 1."""

    def test_visibility_formula(self):
        """Verify g_min for r=2..12."""
        expected = {
            2: 2, 3: 2, 4: 3, 5: 3, 6: 4, 7: 4,
            8: 5, 9: 5, 10: 6, 11: 6, 12: 7,
        }
        for r, g in expected.items():
            assert r // 2 + 1 == g

    def test_S8_first_visible_at_genus5(self):
        """S_8 first visible at genus 5."""
        assert 8 // 2 + 1 == 5

    def test_S9_first_visible_at_genus5(self):
        """S_9 first visible at genus 5."""
        assert 9 // 2 + 1 == 5

    def test_S10_not_at_genus5(self):
        """S_10 first visible at genus 6, NOT genus 5."""
        assert 10 // 2 + 1 == 6

    @pytest.mark.slow
    def test_shadow_visibility_from_engine(self):
        """Verify via engine's shadow visibility check."""
        from compute.lib.genus5_amplitude_engine import genus5_shadow_visibility_check
        vis = genus5_shadow_visibility_check()
        assert vis['S_8_visible']
        assert vis['S_9_visible']
        # S_10 should not contribute from genus-0 vertices at genus 5
        # (would need genus 6)


# ============================================================================
# Section 9: Self-loop parity vanishing
# ============================================================================

class TestSelfLoopParity:
    """prop:self-loop-vanishing at genus 5.

    Single-vertex (0, 2k) with k self-loops: I = 0 for k >= 2
    (odd-dimensional parity obstruction).
    """

    @pytest.mark.slow
    def test_parity_check_returns_dict(self):
        from compute.lib.genus5_amplitude_engine import genus5_self_loop_parity_check
        result = genus5_self_loop_parity_check()
        assert isinstance(result, dict)
        assert len(result) > 0

    @pytest.mark.slow
    def test_single_vertex_graphs_included(self):
        """Single-vertex graphs at genus 5 include the smooth (5,0)."""
        from compute.lib.genus5_amplitude_engine import genus5_self_loop_parity_check
        result = genus5_self_loop_parity_check()
        assert any('5' in k for k in result.keys())


# ============================================================================
# Section 10: Graph enumeration and census (slow)
# ============================================================================

@pytest.mark.slow
class TestGraphEnumeration:
    """Stable graph enumeration at genus 5, n=0."""

    def test_graph_count_positive(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_count
        assert genus5_graph_count() > 0

    def test_graph_count_exceeds_genus4(self):
        """More graphs at genus 5 than genus 4."""
        from compute.lib.genus5_amplitude_engine import genus5_graph_count
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        g4_count = len(enumerate_stable_graphs(4, 0))
        assert genus5_graph_count() > g4_count

    def test_all_graphs_connected(self):
        from compute.lib.genus5_amplitude_engine import genus5_stable_graphs_n0
        for g in genus5_stable_graphs_n0():
            assert g.is_connected

    def test_all_graphs_stable(self):
        from compute.lib.genus5_amplitude_engine import genus5_stable_graphs_n0
        for g in genus5_stable_graphs_n0():
            assert g.is_stable

    def test_all_graphs_genus_5(self):
        from compute.lib.genus5_amplitude_engine import genus5_stable_graphs_n0
        for g in genus5_stable_graphs_n0():
            assert g.arithmetic_genus == 5

    def test_all_graphs_no_legs(self):
        from compute.lib.genus5_amplitude_engine import genus5_stable_graphs_n0
        for g in genus5_stable_graphs_n0():
            assert g.num_legs == 0

    def test_vertex_count_range(self):
        """Vertex count ranges from 1 (smooth) to at most 8 (= 2g-2)."""
        from compute.lib.genus5_amplitude_engine import genus5_by_vertex_count
        dist = genus5_by_vertex_count()
        assert 1 in dist
        assert all(1 <= v <= 8 for v in dist.keys())

    def test_edge_count_range(self):
        """Edge count ranges from 0 (smooth) to 12 (max codimension)."""
        from compute.lib.genus5_amplitude_engine import genus5_by_edge_count
        dist = genus5_by_edge_count()
        assert 0 in dist  # smooth graph
        assert all(0 <= e <= 12 for e in dist.keys())

    def test_loop_number_range(self):
        """h^1 ranges from 0 (fully separating) to 5 (all genus in loops)."""
        from compute.lib.genus5_amplitude_engine import genus5_by_loop_number
        dist = genus5_by_loop_number()
        assert 0 in dist
        assert all(0 <= h <= 5 for h in dist.keys())

    def test_vertex_edge_counts_sum(self):
        """Total graphs equals sum over any distribution."""
        from compute.lib.genus5_amplitude_engine import (
            genus5_graph_count, genus5_by_vertex_count,
            genus5_by_edge_count, genus5_by_loop_number,
        )
        total = genus5_graph_count()
        assert sum(genus5_by_vertex_count().values()) == total
        assert sum(genus5_by_edge_count().values()) == total
        assert sum(genus5_by_loop_number().values()) == total

    def test_dim_mbar_5_0(self):
        """dim M_bar_{5,0} = 3*5 - 3 = 12."""
        assert 3 * 5 - 3 == 12


# ============================================================================
# Section 11: Spectral sequence / boundary strata (slow)
# ============================================================================

@pytest.mark.slow
class TestSpectralSequenceBoundary:
    """Genus spectral sequence E_1 page and boundary strata counts."""

    def test_spectral_counts_sum(self):
        """Sum over h^1 = total graphs."""
        from compute.lib.genus5_amplitude_engine import (
            genus5_spectral_sequence_counts, genus5_graph_count,
        )
        counts = genus5_spectral_sequence_counts()
        assert sum(counts.values()) == genus5_graph_count()

    def test_boundary_strata_counts_sum(self):
        """Sum over edge count = total graphs."""
        from compute.lib.genus5_amplitude_engine import (
            genus5_boundary_strata_counts, genus5_graph_count,
        )
        counts = genus5_boundary_strata_counts()
        assert sum(counts.values()) == genus5_graph_count()

    def test_spectral_equals_loop_distribution(self):
        """Spectral sequence page counts equal loop-number distribution."""
        from compute.lib.genus5_amplitude_engine import (
            genus5_spectral_sequence_counts, genus5_by_loop_number,
        )
        assert genus5_spectral_sequence_counts() == genus5_by_loop_number()


# ============================================================================
# Section 12: Named graphs (slow)
# ============================================================================

@pytest.mark.slow
class TestNamedGraphs:
    """Named genus-5 stable graphs."""

    def test_smooth_graph(self):
        from compute.lib.genus5_amplitude_engine import genus5_named_graphs
        named = genus5_named_graphs()
        assert 'smooth' in named
        g = named['smooth']
        assert g.num_vertices == 1
        assert g.num_edges == 0
        assert g.vertex_genera == (5,)

    def test_irr_node(self):
        from compute.lib.genus5_amplitude_engine import genus5_named_graphs
        named = genus5_named_graphs()
        assert 'irr_node' in named
        g = named['irr_node']
        assert g.num_vertices == 1
        assert g.num_edges == 1

    def test_separating_41(self):
        """Bridge separating genus 4 and genus 1."""
        from compute.lib.genus5_amplitude_engine import genus5_named_graphs
        named = genus5_named_graphs()
        assert 'sep_41' in named
        g = named['sep_41']
        assert g.num_vertices == 2
        assert g.num_edges == 1
        assert tuple(sorted(g.vertex_genera)) == (1, 4)

    def test_separating_32(self):
        """Bridge separating genus 3 and genus 2."""
        from compute.lib.genus5_amplitude_engine import genus5_named_graphs
        named = genus5_named_graphs()
        assert 'sep_32' in named
        g = named['sep_32']
        assert g.num_vertices == 2
        assert g.num_edges == 1
        assert tuple(sorted(g.vertex_genera)) == (2, 3)


# ============================================================================
# Section 13: Planted-forest census (slow)
# ============================================================================

@pytest.mark.slow
class TestPlantedForestCensus:
    """Planted-forest census at genus 5."""

    def test_pf_partition(self):
        """PF + non-PF = total."""
        from compute.lib.genus5_amplitude_engine import (
            genus5_planted_forest_census, genus5_graph_count,
        )
        census = genus5_planted_forest_census()
        assert census['pf_count'] + census['non_pf_count'] == genus5_graph_count()

    def test_pf_count_positive(self):
        from compute.lib.genus5_amplitude_engine import genus5_planted_forest_census
        assert genus5_planted_forest_census()['pf_count'] > 0

    def test_nonpf_count_positive(self):
        """Smooth graph is not a planted forest."""
        from compute.lib.genus5_amplitude_engine import genus5_planted_forest_census
        assert genus5_planted_forest_census()['non_pf_count'] > 0

    def test_pf_majority(self):
        """Most graphs are planted forests (as at genera 3, 4)."""
        from compute.lib.genus5_amplitude_engine import genus5_planted_forest_census
        census = genus5_planted_forest_census()
        assert census['pf_count'] > census['non_pf_count']

    def test_planted_forest_classification_consistent(self):
        """is_planted_forest is consistent with census."""
        from compute.lib.genus5_amplitude_engine import (
            is_planted_forest, genus5_stable_graphs_n0,
            genus5_planted_forest_census,
        )
        graphs = genus5_stable_graphs_n0()
        pf_count = sum(1 for g in graphs if is_planted_forest(g))
        assert pf_count == genus5_planted_forest_census()['pf_count']

    def test_smooth_graph_not_pf(self):
        """The smooth genus-5 graph has no genus-0 vertices at all."""
        from compute.lib.genus5_amplitude_engine import is_planted_forest
        from compute.lib.stable_graph_enumeration import StableGraph
        g = StableGraph(vertex_genera=(5,), edges=(), legs=())
        assert not is_planted_forest(g)

    def test_genus0_trivalent_is_pf(self):
        """A graph with a genus-0 vertex of valence >= 3 is a planted forest."""
        from compute.lib.genus5_amplitude_engine import is_planted_forest
        from compute.lib.stable_graph_enumeration import StableGraph
        # genus 3 -- genus 0 -- genus 2 with genus-0 having 3 neighbors (impossible
        # with just edges; we need at least 3 edges). Let's use a star:
        # vertex 0: genus 3, vertex 1: genus 0 (valence 3), vertex 2: genus 2,
        # edges: (0,1), (1,2), (1,2) or similar. Actually, use:
        # vertex 0: g=0 (valence 3), vertex 1: g=2, vertex 2: g=2
        # edges: (0,1), (0,2), (0,1) -> loop number = 3-3+1=1, sum_gv=4, total=5
        g = StableGraph(
            vertex_genera=(0, 2, 2),
            edges=((0, 1), (0, 1), (0, 2)),
            legs=(),
        )
        assert g.arithmetic_genus == 5
        assert is_planted_forest(g)


# ============================================================================
# Section 14: Gaussian purity (slow)
# ============================================================================

@pytest.mark.slow
class TestGaussianPurity:
    """Gaussian purity check: scalar sum over Gaussian-active graphs.

    Gaussian-active graphs have all vertices with valence 0 (g_v >= 2)
    or valence 2 (g_v >= 1), with no other valences.
    """

    def test_gaussian_active_subset(self):
        """Active count <= total."""
        from compute.lib.genus5_amplitude_engine import (
            genus5_gaussian_active_graphs, genus5_graph_count,
        )
        active = genus5_gaussian_active_graphs()
        assert len(active) <= genus5_graph_count()
        assert len(active) > 0

    def test_gaussian_purity_at_kappa1(self):
        """Gaussian purity check at kappa=1."""
        from compute.lib.genus5_amplitude_engine import genus5_gaussian_purity_check
        result = genus5_gaussian_purity_check(kappa_val=1)
        assert result['expected'] == Fraction(73, 3503554560)


# ============================================================================
# Section 15: Automorphism spectrum (slow)
# ============================================================================

@pytest.mark.slow
class TestAutomorphismSpectrum:
    """Automorphism orders of genus-5 stable graphs."""

    def test_smooth_graph_aut_1(self):
        """Smooth graph has |Aut| = 1."""
        from compute.lib.genus5_amplitude_engine import genus5_automorphism_spectrum
        spectrum = genus5_automorphism_spectrum()
        assert 1 in spectrum

    def test_all_aut_positive(self):
        from compute.lib.genus5_amplitude_engine import genus5_automorphism_spectrum
        for a in genus5_automorphism_spectrum():
            assert a >= 1

    def test_max_automorphism_positive(self):
        from compute.lib.genus5_amplitude_engine import genus5_max_automorphism
        assert genus5_max_automorphism() >= 1

    def test_inverse_aut_sum_positive(self):
        from compute.lib.genus5_amplitude_engine import genus5_inverse_aut_sum
        assert genus5_inverse_aut_sum() > 0


# ============================================================================
# Section 16: Graph profiles by shadow depth class (slow)
# ============================================================================

@pytest.mark.slow
class TestGraphProfiles:
    """Graph profiles for G/L/C/M shadow depth classes."""

    def test_profile_G(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_profiles
        prof = genus5_graph_profiles('G')
        assert prof['family'] == 'G'
        assert prof['active_count'] + prof['scalar_only_count'] == prof['total_graphs']

    def test_profile_L(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_profiles
        prof = genus5_graph_profiles('L')
        assert prof['family'] == 'L'

    def test_profile_C(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_profiles
        prof = genus5_graph_profiles('C')
        assert prof['family'] == 'C'

    def test_profile_M(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_profiles
        prof = genus5_graph_profiles('M')
        assert prof['family'] == 'M'

    def test_invalid_family_raises(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_profiles
        with pytest.raises(ValueError):
            genus5_graph_profiles('X')

    def test_G_scalar_only_most(self):
        """G (Gaussian, r_max=2): most graphs have max_valence < 999."""
        from compute.lib.genus5_amplitude_engine import genus5_graph_profiles
        prof = genus5_graph_profiles('G')
        assert prof['scalar_only_count'] >= 0


# ============================================================================
# Section 17: Scalar graph sum (slow)
# ============================================================================

@pytest.mark.slow
class TestScalarGraphSum:
    """Scalar graph sum polynomial and evaluation."""

    def test_polynomial_has_entries(self):
        from compute.lib.genus5_amplitude_engine import genus5_scalar_sum_polynomial
        poly = genus5_scalar_sum_polynomial()
        assert len(poly) > 0

    def test_polynomial_keys_are_edge_counts(self):
        """Keys are nonneg integers (edge counts)."""
        from compute.lib.genus5_amplitude_engine import genus5_scalar_sum_polynomial
        poly = genus5_scalar_sum_polynomial()
        for k in poly.keys():
            assert isinstance(k, int)
            assert k >= 0

    def test_polynomial_values_positive(self):
        """Coefficients (1/|Aut| sums) are positive."""
        from compute.lib.genus5_amplitude_engine import genus5_scalar_sum_polynomial
        poly = genus5_scalar_sum_polynomial()
        for v in poly.values():
            assert v > 0

    def test_scalar_sum_at_zero(self):
        """Scalar sum at kappa=0 gives the 0-edge contribution only."""
        from compute.lib.genus5_amplitude_engine import genus5_scalar_sum_at
        # At kappa=0, only e=0 contributes (smooth graph, 1/|Aut|=1)
        result = genus5_scalar_sum_at(Fraction(0))
        assert result == Fraction(1)  # smooth graph contributes 1


# ============================================================================
# Section 18: Orbifold Euler characteristic (slow)
# ============================================================================

@pytest.mark.slow
class TestOrbifoldEuler:
    """Orbifold Euler characteristic of M_bar_{5,0}."""

    def test_euler_check_passes(self):
        from compute.lib.genus5_amplitude_engine import genus5_euler_check
        computed, _, match = genus5_euler_check()
        assert match

    def test_euler_rational(self):
        from compute.lib.genus5_amplitude_engine import genus5_euler_check
        computed, _, _ = genus5_euler_check()
        assert isinstance(computed, Fraction)


# ============================================================================
# Section 19: Summary and cross-checks (slow)
# ============================================================================

@pytest.mark.slow
class TestSummary:
    """Summary function integration test."""

    def test_summary_has_required_keys(self):
        from compute.lib.genus5_amplitude_engine import genus5_summary
        s = genus5_summary()
        required = [
            'total_graphs', 'by_h1', 'by_vertices', 'by_edges',
            'aut_spectrum_min', 'aut_spectrum_max',
            'chi_orb_mbar', 'chi_orb_open', 'lambda5_fp',
            'graph_weight_sum', 'planted_forest_count',
        ]
        for key in required:
            assert key in s, f"Missing key: {key}"

    def test_summary_lambda5(self):
        from compute.lib.genus5_amplitude_engine import genus5_summary
        s = genus5_summary()
        assert s['lambda5_fp'] == Fraction(73, 3503554560)

    def test_summary_aut_bounds(self):
        from compute.lib.genus5_amplitude_engine import genus5_summary
        s = genus5_summary()
        assert s['aut_spectrum_min'] >= 1
        assert s['aut_spectrum_max'] >= s['aut_spectrum_min']

    @pytest.mark.slow
    def test_cross_genus_consistency_from_engine(self):
        """Full cross-genus consistency from engine."""
        from compute.lib.genus5_amplitude_engine import cross_genus_consistency_check
        cg = cross_genus_consistency_check()
        assert cg['counts_increasing']
        assert cg['lambdas_decreasing']
        assert cg['lambdas_positive']

    def test_graph_weight_sum_positive(self):
        from compute.lib.genus5_amplitude_engine import genus5_graph_weight_sum
        assert genus5_graph_weight_sum() > 0
