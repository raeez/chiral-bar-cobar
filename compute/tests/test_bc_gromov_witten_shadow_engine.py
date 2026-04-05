r"""Tests for BC-87: Gromov-Witten invariants from the shadow obstruction tower.

Tests cover:
  1. Bernoulli numbers: two independent computation paths
  2. lambda_fp: three independent computation paths (recursive, sympy, series)
  3. Ahat generating function: Taylor series vs explicit formula
  4. Shadow free energies F_g: exact values, positivity, asymptotics
  5. Partition function Z_A: coefficient expansion, numerical evaluation
  6. Target = point: N_{g,d} = 0 for d >= 1 (theorem-level)
  7. MacMahon / DT comparison: shadow != DT (different objects)
  8. Virasoro constraints: trivially satisfied at n=0
  9. WDVV: trivially satisfied for point target
  10. Topological recursion: Airy != shadow (different spectral curves)
  11. Cross-family consistency: additivity, scaling, complementarity
  12. Kappa values: specific algebra families
  13. Asymptotics: F_g ~ 2*kappa/(2*pi)^{2g}

Multi-path verification (mandate: >= 3 paths per claim):
  Path 1: Recursive Bernoulli (Fraction, no sympy)
  Path 2: Sympy Bernoulli (sympy.bernoulli + Rational)
  Path 3: Taylor series of (x/2)/sin(x/2) (sympy.series)
  Path 4: Numerical evaluation of closed-form
  Path 5: Cross-family consistency (additivity, complementarity)
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational, factorial, bernoulli as sympy_bernoulli, Symbol, sin, series, pi

from compute.lib.bc_gromov_witten_shadow_engine import (
    bernoulli_recursive,
    bernoulli_sympy,
    lambda_fp_fraction,
    lambda_fp_sympy,
    ahat_coefficients_fraction,
    ahat_coefficients_from_series,
    shadow_Fg,
    shadow_Fg_table,
    shadow_gw_log_partition,
    shadow_gw_log_partition_truncated,
    shadow_gw_partition_coeffs,
    gw_degree_decomposition,
    verify_point_target_structure,
    macmahon_coefficients,
    macmahon_log_coefficients,
    shadow_vs_dt_comparison,
    virasoro_constraint_analysis,
    wdvv_analysis,
    airy_Fg,
    tr_shadow_comparison,
    shadow_Fg_asymptotic,
    shadow_Fg_asymptotics_table,
    kappa_virasoro,
    kappa_heisenberg,
    kappa_affine,
    shadow_gw_virasoro,
    shadow_gw_heisenberg,
    verify_lambda_fp_three_paths,
    verify_Fg_cross_family,
    verify_positivity,
    verify_generating_function_numerical,
    run_all_verifications,
)


# ====================================================================
# Section 1: Bernoulli numbers — two independent paths
# ====================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers via two independent methods."""

    @pytest.mark.parametrize("n,expected", [
        (0, Fraction(1)),
        (1, Fraction(-1, 2)),
        (2, Fraction(1, 6)),
        (4, Fraction(-1, 30)),
        (6, Fraction(1, 42)),
        (8, Fraction(-1, 30)),
        (10, Fraction(5, 66)),
        (12, Fraction(-691, 2730)),
    ])
    def test_bernoulli_recursive_known_values(self, n, expected):
        """Path 1: recursive Bernoulli against hand-checked values."""
        assert bernoulli_recursive(n) == expected

    @pytest.mark.parametrize("n,expected", [
        (0, Rational(1)),
        (1, Rational(1, 2)),      # sympy convention: B_1 = +1/2
        (2, Rational(1, 6)),
        (4, Rational(-1, 30)),
        (6, Rational(1, 42)),
        (8, Rational(-1, 30)),
        (10, Rational(5, 66)),
        (12, Rational(-691, 2730)),
    ])
    def test_bernoulli_sympy_known_values(self, n, expected):
        """Path 2: sympy Bernoulli against hand-checked values.

        Note: sympy uses B_1 = +1/2 convention.  This differs from the
        common convention B_1 = -1/2 but does NOT affect even Bernoulli
        numbers B_{2g}, which are the only ones used in lambda_fp.
        """
        assert bernoulli_sympy(n) == expected

    @pytest.mark.parametrize("n", [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    def test_bernoulli_two_paths_agree_even(self, n):
        """Cross-check: recursive and sympy Bernoulli agree for even n.

        Note: B_1 differs by convention (recursive: -1/2, sympy: +1/2).
        For even n >= 0, both conventions agree.  Since lambda_fp uses
        only B_{2g} (even indices), this is the relevant check.
        """
        rec = bernoulli_recursive(n)
        sym = bernoulli_sympy(n)
        assert Rational(rec.numerator, rec.denominator) == sym

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n >= 3 (classical result)."""
        for n in [3, 5, 7, 9, 11, 13, 15]:
            assert bernoulli_recursive(n) == 0

    def test_bernoulli_sign_alternation(self):
        """(-1)^{g+1} B_{2g} > 0 for g >= 1 (sign pattern)."""
        for g in range(1, 12):
            B2g = bernoulli_recursive(2 * g)
            assert ((-1) ** (g + 1) * B2g > 0), f"Sign wrong at g={g}"


# ====================================================================
# Section 2: lambda_fp — three independent paths
# ====================================================================

class TestLambdaFP:
    """Verify Faber-Pandharipande numbers via three independent methods."""

    @pytest.mark.parametrize("g,expected", [
        (1, Fraction(1, 24)),
        (2, Fraction(7, 5760)),
        (3, Fraction(31, 967680)),
        (4, Fraction(127, 154828800)),
        (5, Fraction(73, 3503554560)),
    ])
    def test_lambda_fp_fraction_known(self, g, expected):
        """Path 1: recursive Bernoulli -> exact Fraction values."""
        assert lambda_fp_fraction(g) == expected

    @pytest.mark.parametrize("g,expected", [
        (1, Rational(1, 24)),
        (2, Rational(7, 5760)),
        (3, Rational(31, 967680)),
        (4, Rational(127, 154828800)),
        (5, Rational(73, 3503554560)),
    ])
    def test_lambda_fp_sympy_known(self, g, expected):
        """Path 2: sympy Bernoulli -> exact Rational values."""
        assert lambda_fp_sympy(g) == expected

    @pytest.mark.parametrize("g", range(1, 8))
    def test_lambda_fp_three_paths_agree(self, g):
        """All three paths agree: recursive, sympy, Taylor series."""
        r = verify_lambda_fp_three_paths(g)
        assert r["all_agree"], f"Disagreement at g={g}: {r}"

    @pytest.mark.parametrize("g", range(1, 15))
    def test_lambda_fp_positive(self, g):
        """lambda_fp > 0 for all g >= 1 (AP22: F_g positive)."""
        assert lambda_fp_fraction(g) > 0

    def test_lambda_fp_invalid_genus(self):
        """lambda_fp raises for g < 1."""
        with pytest.raises(ValueError):
            lambda_fp_fraction(0)
        with pytest.raises(ValueError):
            lambda_fp_fraction(-1)

    def test_lambda_fp_monotone_decrease(self):
        """lambda_fp is strictly decreasing for g >= 1."""
        for g in range(1, 12):
            assert lambda_fp_fraction(g) > lambda_fp_fraction(g + 1)


# ====================================================================
# Section 3: Ahat generating function
# ====================================================================

class TestAhatGeneratingFunction:
    """Verify the A-hat genus generating function."""

    def test_ahat_constant_term(self):
        """Ahat(ix) starts with 1."""
        coeffs = ahat_coefficients_fraction(5)
        assert coeffs[0] == Fraction(1)

    def test_ahat_matches_lambda_fp(self):
        """Ahat(ix) coefficient at x^{2g} = lambda_fp(g)."""
        coeffs = ahat_coefficients_fraction(8)
        for g in range(1, 9):
            assert coeffs[g] == lambda_fp_fraction(g)

    def test_ahat_fraction_vs_series(self):
        """Two computation paths for Ahat agree."""
        frac_coeffs = ahat_coefficients_fraction(6)
        series_coeffs = ahat_coefficients_from_series(6)
        for k in range(7):
            assert Rational(frac_coeffs[k].numerator, frac_coeffs[k].denominator) == series_coeffs[k]

    def test_ahat_ix_equals_x_over_2_sin_x_over_2(self):
        """Verify Ahat(ix) = (x/2)/sin(x/2) by direct series expansion."""
        x = Symbol('x')
        expr = (x / 2) / sin(x / 2)
        s = series(expr, x, 0, n=12)
        # Check first few coefficients
        assert s.coeff(x, 0) == 1
        assert s.coeff(x, 2) == Rational(1, 24)
        assert s.coeff(x, 4) == Rational(7, 5760)
        assert s.coeff(x, 6) == Rational(31, 967680)

    def test_ahat_ap22_index_check(self):
        """AP22: Ahat(ix) - 1 starts at x^2, NOT x^0.

        The generating function sum F_g lam^{2g-2} = kappa/lam^2 * (Ahat(i*lam) - 1)
        has F_1 at lam^0 (from the x^2/lam^2 factor).
        """
        coeffs = ahat_coefficients_fraction(5)
        assert coeffs[0] == Fraction(1)  # Ahat(ix) starts at 1
        assert coeffs[1] > 0  # First nonconstant term at x^2
        # AP22: if we wrote sum F_g lam^{2g-2} = kappa * (Ahat - 1),
        # then F_1 at lam^0 matches Ahat_1 * 1/lam^2 * lam^2 = Ahat_1. Correct.


# ====================================================================
# Section 4: Shadow free energies F_g
# ====================================================================

class TestShadowFreeEnergies:
    """Verify F_g = kappa * lambda_fp."""

    def test_F1_virasoro_c26(self):
        """F_1(Vir_{c=26}) = 13/24."""
        assert shadow_Fg(Fraction(13), 1) == Fraction(13, 24)

    def test_F1_heisenberg_k1(self):
        """F_1(H_{k=1}) = 1/24."""
        assert shadow_Fg(Fraction(1), 1) == Fraction(1, 24)

    def test_F2_virasoro_c26(self):
        """F_2(Vir_{c=26}) = 13 * 7/5760 = 91/5760."""
        assert shadow_Fg(Fraction(13), 2) == Fraction(91, 5760)

    def test_F3_heisenberg_k2(self):
        """F_3(H_{k=2}) = 2 * 31/967680 = 31/483840."""
        assert shadow_Fg(Fraction(2), 3) == Fraction(31, 483840)

    def test_Fg_table(self):
        """F_g table is consistent with individual computations."""
        kappa = Fraction(5, 2)
        table = shadow_Fg_table(kappa, 8)
        for g in range(1, 9):
            assert table[g] == shadow_Fg(kappa, g)

    def test_Fg_linearity_in_kappa(self):
        """F_g is linear in kappa: F_g(a*k) = a * F_g(k)."""
        for g in range(1, 6):
            for a in [2, 3, Fraction(1, 2), Fraction(7, 3)]:
                k = Fraction(5)
                assert shadow_Fg(a * k, g) == a * shadow_Fg(k, g)

    def test_Fg_additivity(self):
        """F_g(k1 + k2) = F_g(k1) + F_g(k2)."""
        for g in range(1, 6):
            k1 = Fraction(3)
            k2 = Fraction(7, 2)
            assert shadow_Fg(k1 + k2, g) == shadow_Fg(k1, g) + shadow_Fg(k2, g)

    def test_Fg_all_positive(self):
        """F_g > 0 for kappa > 0 and all g >= 1."""
        kappa = Fraction(1)
        r = verify_positivity(15)
        assert all(r.values())


# ====================================================================
# Section 5: Partition function Z_A
# ====================================================================

class TestPartitionFunction:
    """Verify the shadow GW partition function."""

    def test_log_partition_small_lambda(self):
        """log Z at small lambda approaches kappa/24 (the F_1 term)."""
        # F = F_1 + F_2*lam^2 + ... so at lam->0, F -> F_1 = kappa/24
        kappa = 1.0
        val = shadow_gw_log_partition(kappa, 0.001, max_genus=20)
        assert abs(val - kappa / 24.0) < 1e-6

    def test_log_partition_closed_form_vs_sum(self):
        """Closed form = truncated sum at small lambda."""
        kappa = 2.5
        for lam in [0.1, 0.2, 0.3, 0.5]:
            closed = shadow_gw_log_partition(kappa, lam)
            # Truncated sum
            truncated = sum(
                float(shadow_Fg(Fraction(5, 2), g)) * lam ** (2 * g - 2)
                for g in range(1, 30)
            )
            assert abs(closed - truncated) < 1e-10, f"Mismatch at lam={lam}"

    def test_log_partition_zero_lambda(self):
        """log Z at lambda = 0 is 0 (by convention)."""
        assert shadow_gw_log_partition(1.0, 0.0) == 0.0

    def test_partition_coeffs_leading(self):
        """Z = exp(F_1) * (1 + F_2*u + ...) where u = lam^2."""
        kappa = Fraction(1)
        coeffs = shadow_gw_partition_coeffs(kappa, 5)
        assert coeffs[0] == Fraction(1)  # Leading coeff of exp(higher terms)
        assert coeffs[1] == shadow_Fg(kappa, 2)  # F_2 * u term

    def test_partition_coeffs_second_order(self):
        """Coefficient of u^2 = F_3 + F_2^2/2."""
        kappa = Fraction(1)
        coeffs = shadow_gw_partition_coeffs(kappa, 5)
        F2 = shadow_Fg(kappa, 2)
        F3 = shadow_Fg(kappa, 3)
        expected = F3 + F2 ** 2 / 2
        assert coeffs[2] == expected

    def test_log_partition_truncated_consistency(self):
        """Truncated log partition coefficients match F_g values."""
        kappa = Fraction(7, 3)
        trunc = shadow_gw_log_partition_truncated(kappa, 8)
        for g in range(1, 9):
            assert trunc[g - 1] == shadow_Fg(kappa, g)

    def test_generating_function_numerical(self):
        """Numerical generating function identity verified at 5 points."""
        r = verify_generating_function_numerical(0.5, max_genus=20, test_points=5)
        for key, val in r.items():
            if isinstance(val, dict):
                assert val["agree"], f"Failed at {key}"


# ====================================================================
# Section 6: Target = point (theorem-level)
# ====================================================================

class TestPointTarget:
    """Verify that the shadow GW theory is GW of a point."""

    def test_only_degree_zero(self):
        """N_{g,d} = 0 for d >= 1, N_{g,0} = F_g."""
        kappa = Fraction(3)
        for g in range(1, 6):
            decomp = gw_degree_decomposition(kappa, g)
            assert set(decomp.keys()) == {0}
            assert decomp[0] == shadow_Fg(kappa, g)

    def test_point_target_structure(self):
        """Full point-target verification for kappa = 1."""
        r = verify_point_target_structure(Fraction(1), 8)
        assert r["target_is_point"]
        for g in range(1, 6):
            assert r[f"g{g}_only_d0"]
            assert r[f"g{g}_linearity"]

    def test_no_kahler_dependence(self):
        """F_g is independent of any Kahler parameter (by construction).
        F_g is a Fraction, not a function of t."""
        for g in range(1, 8):
            fg = shadow_Fg(Fraction(1), g)
            assert isinstance(fg, Fraction)

    def test_point_gw_basic(self):
        """GW of a point: F_0 = 0 (no dim constraint in 0 dimensions),
        F_g for g >= 1 is kappa * lambda_fp."""
        kappa = Fraction(1, 2)
        # F_g is well-defined for g >= 1
        for g in range(1, 6):
            assert shadow_Fg(kappa, g) == kappa * lambda_fp_fraction(g)


# ====================================================================
# Section 7: MacMahon / DT comparison
# ====================================================================

class TestMacMahonDTComparison:
    """Verify shadow != DT and record the precise relationship."""

    def test_macmahon_known_values(self):
        """MacMahon plane partition numbers (OEIS A000219)."""
        known = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        computed = macmahon_coefficients(10)
        assert computed[:11] == known

    def test_macmahon_pp0_is_1(self):
        """pp(0) = 1 (empty plane partition)."""
        mm = macmahon_coefficients(0)
        assert mm[0] == 1

    def test_macmahon_pp1_is_1(self):
        """pp(1) = 1."""
        mm = macmahon_coefficients(1)
        assert mm[1] == 1

    def test_macmahon_pp5_is_24(self):
        """pp(5) = 24 (OEIS A000219)."""
        mm = macmahon_coefficients(5)
        assert mm[5] == 24

    def test_macmahon_log_coefficients(self):
        """log M(q) coefficients: sum_{k|m} m/k^2."""
        log_c = macmahon_log_coefficients(5)
        # m=1: sum_{k|1} 1/k^2 = 1
        assert log_c[1] == Fraction(1)
        # m=2: sum_{k|2} 2/k^2 = 2/1 + 2/4 = 2 + 1/2 = 5/2
        assert log_c[2] == Fraction(5, 2)
        # m=3: sum_{k|3} 3/k^2 = 3/1 + 3/9 = 3 + 1/3 = 10/3
        assert log_c[3] == Fraction(10, 3)
        # m=4: sum_{k|4} 4/k^2 = 4/1 + 4/4 + 4/16 = 4 + 1 + 1/4 = 21/4
        assert log_c[4] == Fraction(21, 4)

    def test_shadow_ne_dt(self):
        """Shadow partition function != DT partition function."""
        r = shadow_vs_dt_comparison(Fraction(1), max_genus=5)
        assert r["shadow_and_dt_are_different"]

    def test_shadow_ne_constant_map(self):
        """Shadow F_g != constant-map F_g^const for CY3.

        F_g^const involves B_{2g} * B_{2g-2},
        shadow lambda_fp involves only B_{2g}.
        """
        r = shadow_vs_dt_comparison(Fraction(1), max_genus=5)
        assert r["shadow_ne_constant_map"]

    def test_dt_vs_shadow_different_variables(self):
        """DT is a q-series, shadow is a lambda-series (different variables)."""
        # DT: Z_DT(q) = M(-q)^chi, q is counting parameter
        # Shadow: Z^sh(lambda) = exp(sum F_g lambda^{2g-2}), lambda is genus coupling
        # These cannot be directly compared without the GW/DT correspondence.
        r = shadow_vs_dt_comparison(Fraction(5), max_genus=5)
        assert "reason" in r


# ====================================================================
# Section 8: Virasoro constraints
# ====================================================================

class TestVirasoroConstraints:
    """Verify Virasoro constraint analysis."""

    def test_string_equation_trivial(self):
        """String equation (L_{-1}) is trivial at n=0."""
        r = virasoro_constraint_analysis(Fraction(1))
        assert r["string_equation_trivial_at_n0"]

    def test_dilaton_equation_trivial(self):
        """Dilaton equation (L_0) is trivial at n=0."""
        r = virasoro_constraint_analysis(Fraction(1))
        assert r["dilaton_equation_trivial_at_n0"]

    def test_L1_trivial(self):
        """L_1 is trivial at n=0."""
        r = virasoro_constraint_analysis(Fraction(1))
        assert r["L1_trivial_at_n0"]

    def test_tau0_genus1(self):
        """<tau_0>_1 = 1/24 = lambda_fp(1)."""
        r = virasoro_constraint_analysis(Fraction(1))
        assert r["tau_0_genus1_check"]

    def test_shadow_cohft_dvv(self):
        """Shadow CohFT satisfies DVV (theorem-level, thm:shadow-cohft)."""
        r = virasoro_constraint_analysis(Fraction(1))
        assert r["shadow_cohft_satisfies_dvv"]


# ====================================================================
# Section 9: WDVV equations
# ====================================================================

class TestWDVV:
    """Verify WDVV analysis for point target."""

    def test_wdvv_trivial_for_point(self):
        """WDVV is trivially satisfied for a point target (dim H = 1)."""
        r = wdvv_analysis(Fraction(1))
        assert r["wdvv_trivial_for_point"]
        assert r["target_dim_H"] == 1

    def test_mc_gives_wdvv(self):
        """MC equation at genus 0 gives WDVV (prop:wdvv-from-mc)."""
        r = wdvv_analysis(Fraction(1))
        assert r["mc_gives_wdvv"]

    def test_single_line_automatic(self):
        """For single-line shadow, WDVV is automatic in 1 dimension."""
        r = wdvv_analysis(Fraction(1))
        assert r["single_line_automatic"]


# ====================================================================
# Section 10: Topological recursion comparison
# ====================================================================

class TestTopologicalRecursion:
    """Verify Airy TR != shadow and record correct spectral curve."""

    def test_airy_ne_shadow(self):
        """Airy F_g != lambda_fp for g >= 2."""
        r = tr_shadow_comparison(8)
        assert r["airy_ne_shadow"]

    def test_airy_Fg_genus1(self):
        """Airy F_1 = 1/12 (|chi(M_{1,1})|)."""
        assert airy_Fg(1) == Fraction(1, 12)

    def test_airy_Fg_genus2(self):
        """Airy F_2 = |B_4|/(2*2*(2*2-2)) = (1/30)/(8) = 1/240."""
        assert airy_Fg(2) == Fraction(1, 240)

    def test_airy_Fg_genus3(self):
        """Airy F_3 = |B_6|/(2*3*(2*3-2)) = (1/42)/(24) = 1/1008."""
        assert airy_Fg(3) == Fraction(1, 1008)

    def test_airy_vs_shadow_ratio_decreases(self):
        """lambda_fp / airy_Fg decreases rapidly (different growth rates)."""
        ratios = []
        for g in range(2, 8):
            r = lambda_fp_fraction(g) / airy_Fg(g)
            ratios.append(float(r))
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] < ratios[i], f"Ratio not decreasing at g={i+3}"

    def test_shadow_not_from_airy(self):
        """Verify lambda_fp(g) != Airy F_g for g = 1, ..., 8."""
        for g in range(1, 9):
            assert lambda_fp_fraction(g) != airy_Fg(g)

    def test_correct_spectral_curve_reference(self):
        """The correct spectral curve is Bouchard-Marino / EMS (reference)."""
        r = tr_shadow_comparison()
        assert "Bouchard-Marino" in r["correct_spectral_curve_reference"]


# ====================================================================
# Section 11: Cross-family consistency
# ====================================================================

class TestCrossFamilyConsistency:
    """Verify additivity, scaling, and complementarity across families."""

    @pytest.mark.parametrize("g", range(1, 8))
    def test_additivity(self, g):
        """F_g(k1+k2) = F_g(k1) + F_g(k2)."""
        r = verify_Fg_cross_family(g)
        assert r["additivity"]

    @pytest.mark.parametrize("g", range(1, 8))
    def test_scaling(self, g):
        """F_g(c*k) = c * F_g(k)."""
        r = verify_Fg_cross_family(g)
        assert r["scaling"]

    @pytest.mark.parametrize("g", range(1, 8))
    def test_virasoro_complementarity(self, g):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_fp(g) (AP24)."""
        r = verify_Fg_cross_family(g)
        assert r["virasoro_complementarity"]

    def test_virasoro_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT 0; AP24)."""
        for c in [0, 1, Fraction(1, 2), 10, 13, 25, 26]:
            k = kappa_virasoro(Fraction(c))
            k_dual = kappa_virasoro(Fraction(26) - Fraction(c))
            assert k + k_dual == 13

    def test_heisenberg_not_virasoro_kappa(self):
        """kappa(H_k) = k != c/2 in general (AP39)."""
        # For Heisenberg at level k, c = k but kappa = k (not k/2)
        k = Fraction(4)
        assert kappa_heisenberg(k) == k
        assert kappa_virasoro(k) == k / 2
        assert kappa_heisenberg(k) != kappa_virasoro(k)

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(4), Fraction(10),
                                    Fraction(13), Fraction(25), Fraction(26)])
    def test_virasoro_selfdual_at_c13(self, c):
        """Virasoro is self-dual at c=13: kappa(Vir_13) = kappa(Vir_{26-13}) = 13/2."""
        k = kappa_virasoro(c)
        k_dual = kappa_virasoro(Fraction(26) - c)
        if c == Fraction(13):
            assert k == k_dual == Fraction(13, 2)
        elif c != Fraction(13):
            assert k != k_dual


# ====================================================================
# Section 12: Kappa values for standard families
# ====================================================================

class TestKappaValues:
    """Verify kappa for specific algebra families."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)
        assert kappa_virasoro(Fraction(0)) == Fraction(0)

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)
        assert kappa_heisenberg(Fraction(3, 2)) == Fraction(3, 2)

    def test_kappa_affine_sl2(self):
        """kappa(sl2_k) = 3(k+2)/4.  dim=3, h^v=2."""
        k = Fraction(1)
        assert kappa_affine(3, k, Fraction(2)) == Fraction(9, 4)

    def test_kappa_affine_sl3(self):
        """kappa(sl3_k) = 8(k+3)/6 = 4(k+3)/3.  dim=8, h^v=3."""
        k = Fraction(1)
        assert kappa_affine(8, k, Fraction(3)) == Fraction(32, 6)

    def test_kappa_affine_generic(self):
        """Generic affine: kappa = dim(g)(k+h^v)/(2h^v)."""
        # sl_N: dim = N^2-1, h^v = N
        for N in [2, 3, 4, 5]:
            dim_g = N * N - 1
            h_v = Fraction(N)
            k = Fraction(1)
            expected = Fraction(dim_g) * (k + h_v) / (2 * h_v)
            assert kappa_affine(dim_g, k, h_v) == expected


# ====================================================================
# Section 13: Specific algebra GW data
# ====================================================================

class TestAlgebraGWData:
    """Test shadow GW data for specific algebras."""

    def test_virasoro_c26_data(self):
        """Shadow GW for Virasoro at c=26 (critical string)."""
        data = shadow_gw_virasoro(Fraction(26), max_genus=5)
        assert data["kappa"] == Fraction(13)
        assert data["kappa_dual"] == Fraction(0)  # Vir_0 has kappa=0
        assert data["kappa_sum"] == Fraction(13)  # AP24
        assert data["free_energies"][1] == Fraction(13, 24)

    def test_virasoro_c13_selfdual(self):
        """Shadow GW for Virasoro at c=13 (self-dual point)."""
        data = shadow_gw_virasoro(Fraction(13), max_genus=5)
        assert data["kappa"] == Fraction(13, 2)
        assert data["kappa_dual"] == Fraction(13, 2)
        # F_g same for A and A! at self-dual point
        for g in range(1, 6):
            assert data["free_energies"][g] == data["free_energies_dual"][g]

    def test_virasoro_c0_vanishing(self):
        """Shadow GW for Virasoro at c=0: kappa=0, all F_g = 0."""
        data = shadow_gw_virasoro(Fraction(0), max_genus=5)
        assert data["kappa"] == Fraction(0)
        for g in range(1, 6):
            assert data["free_energies"][g] == Fraction(0)

    def test_heisenberg_k1_data(self):
        """Shadow GW for Heisenberg at k=1."""
        data = shadow_gw_heisenberg(Fraction(1), max_genus=5)
        assert data["kappa"] == Fraction(1)
        assert data["free_energies"][1] == Fraction(1, 24)

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (Gaussian, depth 2)."""
        data = shadow_gw_heisenberg(Fraction(1), max_genus=5)
        assert "G" in data["shadow_class"]


# ====================================================================
# Section 14: Asymptotic analysis
# ====================================================================

class TestAsymptotics:
    """Verify asymptotic behavior of F_g."""

    def test_asymptotic_estimate(self):
        """F_g ~ 2*kappa/(2*pi)^{2g} for large g."""
        kappa = 1.0
        # For large g, the ratio exact/asymptotic -> 1
        table = shadow_Fg_asymptotics_table(Fraction(1), 20)
        # At g=20, the ratio should be close to 1 (within 1%)
        assert abs(table[20]["ratio"] - 1.0) < 0.01

    def test_asymptotic_ratio_converges(self):
        """The ratio exact/asymptotic converges to 1."""
        table = shadow_Fg_asymptotics_table(Fraction(1), 15)
        ratios = [table[g]["ratio"] for g in range(5, 16)]
        # Ratios should approach 1 monotonically (eventually)
        # Check that the last ratio is closer to 1 than the first
        assert abs(ratios[-1] - 1.0) < abs(ratios[0] - 1.0)

    def test_asymptotic_decay_rate(self):
        """F_g decays like 1/(2*pi)^{2g}, not like (2g)!."""
        kappa = Fraction(1)
        # F_g / F_{g-1} should approach 1/(2*pi)^2 ~ 0.0253
        for g in range(5, 12):
            fg = float(shadow_Fg(kappa, g))
            fg1 = float(shadow_Fg(kappa, g - 1))
            ratio = fg / fg1
            # Should be near 1/(2*pi)^2 = 0.02533...
            assert 0.01 < ratio < 0.05

    def test_shadow_convergent(self):
        """The shadow genus series sum F_g lam^{2g} converges for |lam| < 2*pi."""
        # The generating function (x/2)/sin(x/2) has poles at x = 2*pi*n,
        # so radius of convergence is 2*pi ~ 6.28.
        # At lam=3 (well inside), convergence is fast.
        kappa = 1.0
        lam = 3.0  # Well within radius of convergence
        partial_sums = []
        s = 0.0
        for g in range(1, 30):
            s += float(shadow_Fg(Fraction(1), g)) * lam ** (2 * g)
            partial_sums.append(s)
        # Should converge: successive differences shrink
        assert abs(partial_sums[-1] - partial_sums[-2]) < 1e-10


# ====================================================================
# Section 15: Partition function for specific c values
# ====================================================================

class TestPartitionFunctionSpecificC:
    """Compute Z^{GW}_A through genus 10 for specified c values."""

    @pytest.mark.parametrize("c,kappa_expected", [
        (1, Fraction(1, 2)),
        (4, Fraction(2)),
        (10, Fraction(5)),
        (13, Fraction(13, 2)),
        (25, Fraction(25, 2)),
        (26, Fraction(13)),
    ])
    def test_kappa_values(self, c, kappa_expected):
        """Verify kappa = c/2 for Virasoro."""
        assert kappa_virasoro(Fraction(c)) == kappa_expected

    @pytest.mark.parametrize("c", [1, 4, 10, 13, 25, 26])
    def test_free_energies_through_genus10(self, c):
        """Compute F_g for g = 1, ..., 10 and verify positivity."""
        kappa = kappa_virasoro(Fraction(c))
        table = shadow_Fg_table(kappa, 10)
        for g in range(1, 11):
            fg = table[g]
            if c > 0:
                assert fg > 0, f"F_{g} not positive at c={c}"
            elif c == 0:
                assert fg == 0

    @pytest.mark.parametrize("c", [1, 4, 10, 13, 25, 26])
    def test_partition_coeffs_through_genus10(self, c):
        """Compute Z^{GW} coefficients through genus 10."""
        kappa = kappa_virasoro(Fraction(c))
        coeffs = shadow_gw_partition_coeffs(kappa, 10)
        # Z_0 = 1 (leading coefficient)
        assert coeffs[0] == Fraction(1)
        # All coefficients should be positive (exp of positive series)
        for k in range(10):
            if c > 0:
                assert coeffs[k] >= 0, f"Negative coeff at k={k}, c={c}"

    def test_c13_selfdual_symmetry(self):
        """At c=13 (self-dual), F_g(A) = F_g(A!)."""
        kappa = kappa_virasoro(Fraction(13))
        kappa_dual = kappa_virasoro(Fraction(13))  # 26-13 = 13
        for g in range(1, 11):
            assert shadow_Fg(kappa, g) == shadow_Fg(kappa_dual, g)

    def test_c26_critical_string(self):
        """At c=26, kappa = 13, kappa_dual = 0.

        F_g(Vir_26) = 13 * lambda_fp(g).
        F_g(Vir_0) = 0 (kappa = 0 implies all F_g vanish).
        AP31: kappa=0 does NOT imply Theta=0 (only scalar part vanishes).
        """
        kappa26 = kappa_virasoro(Fraction(26))
        kappa0 = kappa_virasoro(Fraction(0))
        assert kappa26 == Fraction(13)
        assert kappa0 == Fraction(0)
        for g in range(1, 11):
            assert shadow_Fg(kappa26, g) == Fraction(13) * lambda_fp_fraction(g)
            assert shadow_Fg(kappa0, g) == Fraction(0)


# ====================================================================
# Section 16: Comprehensive verification suite
# ====================================================================

class TestComprehensiveVerification:
    """Run the full multi-path verification suite."""

    def test_run_all(self):
        """Full verification suite passes."""
        r = run_all_verifications(8)
        for key, val in r.items():
            assert val, f"Verification failed: {key}"

    def test_all_three_paths_g1_through_g7(self):
        """Three-path agreement for lambda_fp at g = 1, ..., 7."""
        for g in range(1, 8):
            r = verify_lambda_fp_three_paths(g)
            assert r["all_agree"], f"Disagreement at g={g}"

    def test_full_positivity(self):
        """Positivity through g = 20."""
        r = verify_positivity(20)
        assert all(r.values())


# ====================================================================
# Section 17: Edge cases and error handling
# ====================================================================

class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_lambda_fp_g0_raises(self):
        """lambda_fp(0) should raise ValueError."""
        with pytest.raises(ValueError):
            lambda_fp_fraction(0)

    def test_lambda_fp_negative_raises(self):
        """lambda_fp(-1) should raise ValueError."""
        with pytest.raises(ValueError):
            lambda_fp_fraction(-1)

    def test_airy_g0_raises(self):
        """airy_Fg(0) should raise ValueError."""
        with pytest.raises(ValueError):
            airy_Fg(0)

    def test_shadow_Fg_g0_raises(self):
        """shadow_Fg(k, 0) should raise ValueError."""
        with pytest.raises(ValueError):
            shadow_Fg(Fraction(1), 0)

    def test_kappa_zero_gives_zero_Fg(self):
        """kappa = 0 implies F_g = 0 for all g."""
        for g in range(1, 11):
            assert shadow_Fg(Fraction(0), g) == Fraction(0)

    def test_kappa_negative(self):
        """Negative kappa gives negative F_g (consistent with linearity)."""
        for g in range(1, 6):
            assert shadow_Fg(Fraction(-1), g) < 0

    def test_large_genus(self):
        """lambda_fp computable at large genus (g = 30)."""
        val = lambda_fp_fraction(30)
        assert val > 0
        assert val < Fraction(1, 10**30)  # Very small


# ====================================================================
# Section 18: Anti-pattern guards (AP checks)
# ====================================================================

class TestAntiPatternGuards:
    """Tests specifically guarding against known anti-patterns."""

    def test_ap22_generating_function_index(self):
        """AP22: Ahat(ix)-1 starts at x^2, F_1 is at lam^0.

        The mapping: sum F_g lam^{2g-2} = kappa/lam^2 * (Ahat(i*lam) - 1).
        At g=1: F_1 * lam^0 = kappa * lambda_fp(1).
        Ahat-1 starts at x^2, divided by lam^2 gives lam^0. Consistent.
        """
        coeffs = ahat_coefficients_fraction(3)
        assert coeffs[0] == Fraction(1)  # Ahat starts at 1
        assert coeffs[1] == Fraction(1, 24)  # x^2 term
        # F_1 at lam^0 matches (1/24) * lam^2 / lam^2 = 1/24. Correct.

    def test_ap24_complementarity_not_zero(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c in range(0, 27):
            k = kappa_virasoro(Fraction(c))
            k_d = kappa_virasoro(Fraction(26 - c))
            assert k + k_d == Fraction(13), f"Failed at c={c}"

    def test_ap39_kappa_ne_c_over_2(self):
        """AP39: kappa != c/2 in general (only for Virasoro)."""
        # Heisenberg: kappa = k, c = k, so kappa = c but kappa != c/2
        assert kappa_heisenberg(Fraction(4)) != kappa_virasoro(Fraction(4))
        # Affine sl2 at k=1: kappa = 3*3/4 = 9/4, c = 3*1/3 = 1, c/2 = 1/2
        k_sl2 = kappa_affine(3, Fraction(1), Fraction(2))
        assert k_sl2 != Fraction(1, 2)  # c/2 for sl2_1 is wrong for kappa

    def test_ap46_eta_has_prefactor(self):
        """AP46: eta(q) = q^{1/24} prod(1-q^n), the q^{1/24} is NOT optional."""
        # This is a conceptual check: our formulas use lambda_fp = 1/24 at g=1.
        # The eta function's q^{1/24} factor and the 1/24 in lambda_fp(1) are
        # related: F_1 = kappa/24 and the genus-1 partition function involves
        # eta(q)^{-2kappa}.  The 1/24 in eta and in lambda_fp share a common root.
        assert lambda_fp_fraction(1) == Fraction(1, 24)

    def test_ap20_kappa_is_algebra_invariant(self):
        """AP20: kappa(A) is an invariant of A, not of a system.

        F_g(A) = kappa(A) * lambda_fp(g).  The argument of kappa is A.
        """
        # kappa(Vir_c) = c/2, kappa(H_k) = k, kappa(g_k) = dim(g)(k+h^v)/(2h^v)
        # These are three different formulas for three different algebras.
        assert kappa_virasoro(Fraction(26)) == Fraction(13)
        assert kappa_heisenberg(Fraction(26)) == Fraction(26)
        assert kappa_virasoro(Fraction(26)) != kappa_heisenberg(Fraction(26))

    def test_ap31_kappa_zero_does_not_imply_theta_zero(self):
        """AP31: kappa = 0 implies F_g = 0, but NOT Theta_A = 0.

        At c = 0: kappa(Vir_0) = 0, so all scalar F_g vanish.
        But higher-arity components of Theta could be nonzero
        (Virasoro has infinite shadow depth r_max = infinity).
        This test only checks the scalar level.
        """
        kappa0 = kappa_virasoro(Fraction(0))
        assert kappa0 == Fraction(0)
        for g in range(1, 6):
            assert shadow_Fg(kappa0, g) == Fraction(0)
        # NOTE: shadow_Fg captures only the scalar (kappa) level.
        # Higher-arity corrections could be nonzero. See AP31.


# ====================================================================
# Section 19: Numerical precision tests
# ====================================================================

class TestNumericalPrecision:
    """Test numerical evaluation precision."""

    def test_closed_form_at_lambda_01(self):
        """Closed-form evaluation at lambda = 0.1."""
        # (0.05)/sin(0.05) - 1 should be ~ 0.05^2/6 = 0.000416...
        # Exact: (0.05)/sin(0.05) = 1/cos'(0) ... no.
        # sin(0.05) = 0.04998..., (0.05)/sin(0.05) = 1.0000416...,
        # so (Ahat-1) ~ 4.166e-4, divided by 0.01 = 0.04166...
        kappa = 1.0
        val = shadow_gw_log_partition(kappa, 0.1)
        # F_1/lam^0 = 1/24 ~ 0.04167
        assert abs(val - 1.0 / 24.0) < 1e-4

    def test_closed_form_at_lambda_1(self):
        """Closed-form evaluation at lambda = 1.0."""
        kappa = 1.0
        closed = shadow_gw_log_partition(kappa, 1.0)
        # Truncated sum
        truncated = sum(
            float(lambda_fp_fraction(g)) * 1.0 ** (2 * g - 2)
            for g in range(1, 50)
        )
        assert abs(closed - truncated) < 1e-12

    def test_closed_form_at_lambda_5(self):
        """Closed-form evaluation at lambda = 5.0 (near convergence radius)."""
        kappa = 1.0
        closed = shadow_gw_log_partition(kappa, 5.0)
        # Should be finite (within radius of convergence 2*pi ~ 6.28)
        assert math.isfinite(closed)
        # Truncated sum with many terms
        truncated = sum(
            float(lambda_fp_fraction(g)) * 5.0 ** (2 * g - 2)
            for g in range(1, 80)
        )
        assert abs(closed - truncated) / abs(closed) < 1e-8

    def test_high_genus_exact(self):
        """Exact computation at g = 15."""
        val = lambda_fp_fraction(15)
        assert val > 0
        # Check it's a valid Fraction
        assert isinstance(val, Fraction)
        assert val.denominator > 0


# ====================================================================
# Section 20: Structural theorems
# ====================================================================

class TestStructuralTheorems:
    """Test theorem-level structural observations."""

    def test_shadow_gw_is_gw_of_point(self):
        """THEOREM: The shadow GW theory is GW of a point, weighted by kappa.

        Proof: F_g(A) = kappa * lambda_fp(g) is a constant (no Kahler
        dependence), so N_{g,d} = 0 for d >= 1.
        """
        kappa = Fraction(7, 3)
        for g in range(1, 8):
            decomp = gw_degree_decomposition(kappa, g)
            # Only degree 0
            assert set(decomp.keys()) == {0}
            # Value matches F_g
            assert decomp[0] == shadow_Fg(kappa, g)

    def test_shadow_ne_dt_macmahon(self):
        """THEOREM: Shadow partition function != DT/MacMahon.

        The shadow gives Ahat coefficients.
        DT gives M(-q)^chi (MacMahon to the chi power).
        These are different mathematical objects in different variables.
        """
        r = shadow_vs_dt_comparison(Fraction(1))
        assert r["shadow_and_dt_are_different"]
        assert r["shadow_ne_constant_map"]

    def test_shadow_convergent_series(self):
        """THEOREM: The shadow genus expansion converges for |lambda| < 2*pi.

        The generating function (x/2)/sin(x/2) has poles at x = 2*pi*n,
        so radius of convergence is 2*pi.
        """
        # At lambda = 6 < 2*pi ~ 6.28, should converge
        kappa = 1.0
        val = shadow_gw_log_partition(kappa, 6.0)
        assert math.isfinite(val)

    def test_shadow_diverges_near_2pi(self):
        """The generating function grows without bound as lambda -> 2*pi.

        (x/2)/sin(x/2) has a pole at x = 2*pi (sin(pi) = 0).
        In floating point, sin(pi) ~ 1.2e-16 (not exactly 0), so the
        value is extremely large but finite near the pole.
        """
        kappa = 1.0
        # Near the pole: the value should be very large
        val = shadow_gw_log_partition(kappa, 2.0 * math.pi - 0.001)
        assert val > 100  # Very large near the pole
        # Further from the pole: moderately large
        val2 = shadow_gw_log_partition(kappa, 2.0 * math.pi - 0.1)
        assert val2 > 1.0
        # The value increases as we approach the pole
        assert val > val2

    def test_virasoro_constraints_trivial(self):
        """THEOREM: Virasoro constraints are trivially satisfied at n=0."""
        r = virasoro_constraint_analysis(Fraction(1))
        assert r["string_equation_trivial_at_n0"]
        assert r["dilaton_equation_trivial_at_n0"]
        assert r["L1_trivial_at_n0"]

    def test_wdvv_trivial_for_point(self):
        """THEOREM: WDVV is trivially satisfied for point target."""
        r = wdvv_analysis(Fraction(1))
        assert r["wdvv_trivial_for_point"]
