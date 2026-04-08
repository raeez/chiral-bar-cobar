r"""Tests for c334_c444_arithmetic_engine.

Multi-path verification of the explicit arithmetic of the two curves
C_334 and C_444 controlling the rationality of delta_F2(W_4).

EVERY numerical value is checked by at least TWO independent paths
wherever possible (direct computation + formula derivation + limiting
case + cross-engine consistency with galois_w4_w5_engine).
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt

import pytest

from compute.lib.c334_c444_arithmetic_engine import (
    D334_COEFFS,
    D444_COEFFS,
    D334,
    D444,
    E_C334_LONG,
    ROOTS_334,
    ROOTS_444,
    SPECIFIC_C_VALUES,
    _det_int,
    _prime_divisors,
    all_3_pair_partitions,
    bad_primes_C334,
    bad_primes_C334_from_discriminant,
    bad_primes_C444,
    count_points_C444_mod_p,
    count_points_E_C334_mod_p,
    discriminant_polynomial,
    discriminant_short_C334,
    evaluate_polynomial,
    evaluate_specific_c_values,
    exceptional_C444_point,
    has_extra_involution_C444,
    hasse_a_p_C334,
    hasse_bound_holds_C334,
    hasse_weil_bound_holds_C444,
    infinity_point_rational_C334,
    infinity_point_rational_C444,
    is_perfect_square_int,
    is_rational_square,
    j_invariant_C334,
    jacobian_decomposition_C444,
    L_factor_C334_at_good_prime,
    leading_coefficient_D334,
    leading_coefficient_D444,
    long_form_invariants_C334,
    rational_sqrt,
    search_integer_points_C334,
    search_integer_points_C444,
    search_rational_points_C334,
    search_rational_points_C444,
    short_weierstrass_C334,
    simultaneous_rationality_at,
    simultaneous_rationality_locus_integer,
    simultaneous_rationality_locus_rational,
    squarefree_kernel_int,
    squarefree_part_lc_D334,
    squarefree_part_lc_D444,
    summary,
    two_torsion_subgroup_C334,
    two_torsion_x_coordinates_C334,
    verify_exceptional_C444_point,
    verify_two_torsion_C334,
)


# =============================================================================
# Path 1: Polynomial coefficient sanity and two-path evaluation.
# =============================================================================

class TestPolynomialExpansion:
    """D_334 and D_444 expansions cross-checked against direct factored form."""

    @pytest.mark.parametrize("c", [-30, -10, 0, 1, 5, 13, 24, 26, 100, 196_883])
    def test_D334_coeff_vs_factored(self, c):
        coeffs_val = evaluate_polynomial(D334_COEFFS, Fraction(c))
        factored_val = D334(Fraction(c))
        direct = 42 * (5 * c + 22) * (c + 24) * (7 * c + 68) * (3 * c + 46)
        assert coeffs_val == factored_val == Fraction(direct)

    @pytest.mark.parametrize("c", [0, 1, 5, 13, 24, 26, 100, -50, -100])
    def test_D444_coeff_vs_factored(self, c):
        coeffs_val = evaluate_polynomial(D444_COEFFS, Fraction(c))
        factored_val = D444(Fraction(c))
        direct = (7 * (2 * c - 1) * (3 * c + 46) * (c + 24)
                  * (7 * c + 68) * (10 * c + 197) * (5 * c + 3))
        assert coeffs_val == factored_val == Fraction(direct)

    def test_D334_degree(self):
        assert len(D334_COEFFS) == 5  # degree 4

    def test_D444_degree(self):
        assert len(D444_COEFFS) == 7  # degree 6

    def test_D334_leading_coefficient(self):
        # 42 * 5 * 1 * 7 * 3 = 4410
        assert leading_coefficient_D334() == 4410
        assert 4410 == 2 * 3 ** 2 * 5 * 7 ** 2

    def test_D444_leading_coefficient(self):
        # 7 * 2 * 3 * 1 * 7 * 10 * 5 = 14700
        assert leading_coefficient_D444() == 14700
        assert 14700 == 2 ** 2 * 3 * 5 ** 2 * 7 ** 2

    def test_D334_vanishes_at_roots(self):
        for r in ROOTS_334:
            assert D334(r) == 0

    def test_D444_vanishes_at_roots(self):
        for r in ROOTS_444:
            assert D444(r) == 0

    def test_D334_no_common_factor_with_D444_at_5c_plus_22(self):
        # (5c+22) divides D_334 but NOT D_444
        assert D334(Fraction(-22, 5)) == 0
        assert D444(Fraction(-22, 5)) != 0

    def test_D334_no_common_factor_with_D444_at_2c_minus_1(self):
        # (2c-1) divides D_444 but NOT D_334
        assert D444(Fraction(1, 2)) == 0
        assert D334(Fraction(1, 2)) != 0


# =============================================================================
# Path 2: Rational-square primitives.
# =============================================================================

class TestSquareTesting:

    @pytest.mark.parametrize("n,expected", [
        (0, True), (1, True), (2, False), (3, False), (4, True),
        (9, True), (16, True), (25, True), (100, True), (101, False),
        (-1, False), (-4, False),
    ])
    def test_is_perfect_square_int(self, n, expected):
        assert is_perfect_square_int(n) is expected

    @pytest.mark.parametrize("q,expected", [
        (Fraction(0), True),
        (Fraction(1), True),
        (Fraction(4, 9), True),
        (Fraction(9, 16), True),
        (Fraction(1, 2), False),
        (Fraction(-4, 9), False),
        (Fraction(50, 2), True),  # = 25
    ])
    def test_is_rational_square(self, q, expected):
        assert is_rational_square(q) is expected

    def test_rational_sqrt_positive(self):
        assert rational_sqrt(Fraction(49, 9)) == Fraction(7, 3)

    def test_rational_sqrt_zero(self):
        assert rational_sqrt(Fraction(0)) == Fraction(0)

    def test_rational_sqrt_raises_on_nonsquare(self):
        with pytest.raises(ValueError):
            rational_sqrt(Fraction(2))


# =============================================================================
# Path 3: Weierstrass long/short form + invariants of C_334.
# =============================================================================

class TestWeierstrassC334:

    def test_two_torsion_satisfies_cubic(self):
        """The 2-torsion x-coordinates are roots of the Weierstrass cubic."""
        assert verify_two_torsion_C334()

    def test_two_torsion_structure(self):
        info = two_torsion_subgroup_C334()
        assert info['structure'] == '(Z/2)^2'
        assert info['order'] == 4
        assert info['rational'] is True

    def test_two_torsion_x_coordinates_values(self):
        assert sorted(two_torsion_x_coordinates_C334()) == sorted([
            -546_000, -749_112, -1_234_800
        ])

    def test_long_form_b2_c4_c6_formulas(self):
        inv = long_form_invariants_C334()
        a2, a4, a6 = inv['a2'], inv['a4'], inv['a6']
        # Formulas for a1=a3=0 case
        assert inv['b2'] == 4 * a2
        assert inv['b4'] == 2 * a4
        assert inv['b6'] == 4 * a6
        assert inv['c4'] == inv['b2'] ** 2 - 24 * inv['b4']
        assert inv['c6'] == -inv['b2'] ** 3 + 36 * inv['b2'] * inv['b4'] - 216 * inv['b6']

    def test_delta_is_integer(self):
        inv = long_form_invariants_C334()
        assert (inv['c4'] ** 3 - inv['c6'] ** 2) % 1728 == 0
        assert inv['Delta'] == (inv['c4'] ** 3 - inv['c6'] ** 2) // 1728

    def test_short_weierstrass_discriminant_matches_long(self):
        """Short- and long-form discriminants must agree under the
        standard substitution (a2 -> 0) which does not change Delta."""
        short_delta = discriminant_short_C334()
        long_delta = long_form_invariants_C334()['Delta']
        assert short_delta == long_delta

    def test_short_weierstrass_values(self):
        """Short form Y^2 = X^3 + A X + B with A, B specific integers."""
        sw = short_weierstrass_C334()
        assert sw['A'] == -125_265_459_648
        assert sw['B'] == 10_963_320_236_438_528

    def test_delta_factorization(self):
        """Delta of E_{C334} has exactly these bad-reduction primes."""
        Delta = long_form_invariants_C334()['Delta']
        primes = sorted(_prime_divisors(abs(Delta)))
        assert primes == [2, 3, 5, 7, 13, 31, 41, 59]

    def test_j_invariant_nonintegral(self):
        """j is a nonintegral rational (CM is excluded)."""
        j = j_invariant_C334()
        assert isinstance(j, Fraction)
        assert j.denominator > 1

    def test_j_invariant_from_c4_and_delta(self):
        """j = c4^3 / Delta (definition)."""
        inv = long_form_invariants_C334()
        j = j_invariant_C334()
        assert j == Fraction(inv['c4'] ** 3, inv['Delta'])


# =============================================================================
# Path 4: Bad-reduction primes, two independent paths.
# =============================================================================

class TestBadPrimesC334:

    def test_bad_primes_from_Delta(self):
        assert bad_primes_C334() == [2, 3, 5, 7, 13, 31, 41, 59]

    def test_bad_primes_from_discriminant_match(self):
        """Two independent computations of the bad-prime set must agree."""
        assert bad_primes_C334() == bad_primes_C334_from_discriminant()

    def test_bad_primes_include_lc_primes(self):
        """Primes dividing lc(D_334) must be bad reduction primes."""
        lc_primes = _prime_divisors(leading_coefficient_D334())
        for p in lc_primes:
            assert p in bad_primes_C334()


class TestBadPrimesC444:

    def test_bad_primes_set(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 29, 43, 59, 101, 131, 191, 233]
        assert bad_primes_C444() == expected

    def test_bad_primes_include_131(self):
        """The prime 131 appears in the bad-prime set of C_444 because
        it divides D_444(72)/((small squares)) = 2^8 3^2 7^2 11^4 13^2 131^2
        -- the exceptional point c = 72 lives at this prime's arithmetic."""
        assert 131 in bad_primes_C444()

    def test_bad_primes_include_lc_primes_444(self):
        lc_primes = _prime_divisors(leading_coefficient_D444())
        for p in lc_primes:
            assert p in bad_primes_C444()


# =============================================================================
# Path 5: Infinity points and squarefree leading coefficients.
# =============================================================================

class TestInfinityPoints:

    def test_lc_D334_squarefree_is_10(self):
        # 4410 = 2 * 3^2 * 5 * 7^2 -> squarefree part = 2 * 5 = 10
        assert squarefree_part_lc_D334() == 10

    def test_lc_D444_squarefree_is_3(self):
        # 14700 = 2^2 * 3 * 5^2 * 7^2 -> squarefree part = 3
        assert squarefree_part_lc_D444() == 3

    def test_infinity_C334_not_rational(self):
        assert infinity_point_rational_C334() is False

    def test_infinity_C444_not_rational(self):
        assert infinity_point_rational_C444() is False


# =============================================================================
# Path 6: Rational point search.
# =============================================================================

class TestRationalPointsC334:

    def test_integer_search_finds_trivial_roots(self):
        pts = search_integer_points_C334(-100, 100)
        c_values = [p[0] for p in pts]
        # Integer roots are -24 only (-22/5, -68/7, -46/3 aren't integers)
        assert -24 in c_values

    def test_integer_search_no_nontrivial_small(self):
        """There are NO nontrivial integer points on C_334 in a wide search."""
        pts = search_integer_points_C334(-5000, 5000)
        nontrivial = [(c, y) for (c, y) in pts if y != 0]
        assert nontrivial == []

    def test_rational_search_finds_all_affine_roots(self):
        """All four rational roots of D_334 are rational points of C_334."""
        pts = search_rational_points_C334(
            num_range=(-300, 300),
            denominators=[1, 2, 3, 4, 5, 6, 7],
        )
        c_values = {p[0] for p in pts}
        assert Fraction(-24, 1) in c_values
        assert Fraction(-22, 5) in c_values
        assert Fraction(-46, 3) in c_values
        assert Fraction(-68, 7) in c_values


class TestRationalPointsC444:

    def test_integer_search_finds_trivial_root(self):
        pts = search_integer_points_C444(-100, 100)
        c_values = [p[0] for p in pts]
        assert -24 in c_values

    def test_exceptional_point_72_found(self):
        """c = 72 is on C_444 (the only nontrivial integer point known)."""
        pts = search_integer_points_C444(0, 200)
        nontriv = [(c, y) for (c, y) in pts if y != 0]
        assert (72, 69_237_168) in nontriv

    def test_exceptional_point_verified_via_direct_evaluation(self):
        assert verify_exceptional_C444_point()

    def test_exceptional_point_factorization(self):
        """D_444(72) = 2^8 3^2 7^2 11^4 13^2 131^2, perfect square."""
        v = int(D444(Fraction(72)))
        assert v == 4_793_785_432_660_224
        # Factorization check
        assert v == (2 ** 8) * (3 ** 2) * (7 ** 2) * (11 ** 4) * (13 ** 2) * (131 ** 2)
        assert isqrt(v) ** 2 == v
        assert isqrt(v) == 2 ** 4 * 3 * 7 * 11 ** 2 * 13 * 131

    def test_no_other_integer_points_in_small_range(self):
        """Integer search confirms ONLY 6 trivial + (72) in [-1000, 1000]."""
        pts = search_integer_points_C444(-1000, 1000)
        nontriv = [(c, y) for (c, y) in pts if y != 0]
        assert nontriv == [(72, 69_237_168)]

    def test_rational_search_finds_all_six_trivial_roots(self):
        pts = search_rational_points_C444(
            num_range=(-300, 300),
            denominators=[1, 2, 3, 5, 7, 10],
        )
        c_values = {p[0] for p in pts}
        for r in ROOTS_444:
            assert r in c_values


# =============================================================================
# Path 7: Simultaneous rationality locus.
# =============================================================================

class TestSimultaneousRationalityLocus:

    def test_trivial_collision_minus_24(self):
        info = simultaneous_rationality_at(Fraction(-24))
        assert info['D334'] == 0
        assert info['D444'] == 0
        assert info['in_rationality_locus'] is True

    def test_trivial_collision_minus_68_over_7(self):
        info = simultaneous_rationality_at(Fraction(-68, 7))
        assert info['D334'] == 0
        assert info['D444'] == 0
        assert info['in_rationality_locus'] is True

    def test_trivial_collision_minus_46_over_3(self):
        info = simultaneous_rationality_at(Fraction(-46, 3))
        assert info['D334'] == 0
        assert info['D444'] == 0
        assert info['in_rationality_locus'] is True

    def test_72_not_in_rationality_locus(self):
        """c = 72 is on C_444 but NOT on C_334."""
        info = simultaneous_rationality_at(Fraction(72))
        assert info['D444_square'] is True
        assert info['D334_square'] is False
        assert info['in_rationality_locus'] is False

    def test_ising_not_in_locus(self):
        """c = 1/2 (Ising): D_444 = 0 but D_334 is not a square."""
        info = simultaneous_rationality_at(Fraction(1, 2))
        assert info['D444'] == 0
        assert info['D444_square'] is True
        assert info['D334_square'] is False

    def test_integer_locus_covers_minus_24_only(self):
        """Among integer c, only c = -24 is in the simultaneous locus."""
        locus = simultaneous_rationality_locus_integer(-2000, 2000)
        assert locus == [-24]

    def test_rational_locus_covers_three_trivial(self):
        """In a rational search, the three trivial collisions appear."""
        locus = simultaneous_rationality_locus_rational(
            num_range=(-200, 200), denominators=[1, 3, 7],
        )
        # -24 (denom 1), -46/3 (denom 3), -68/7 (denom 7)
        assert Fraction(-24, 1) in locus
        assert Fraction(-46, 3) in locus
        assert Fraction(-68, 7) in locus


# =============================================================================
# Path 8: Specific c values requested in the spec.
# =============================================================================

class TestSpecificCValues:

    @pytest.mark.parametrize("c,label,expected_locus", [
        (Fraction(-24, 1),     "trivial",   True),
        (Fraction(-22, 5),     "D334 root", False),  # D_444(-22/5) != square
        (Fraction(1, 2),       "Ising",     False),
        (Fraction(1, 1),       "c=1",       False),
        (Fraction(13, 1),      "Virasoro",  False),
        (Fraction(24, 1),      "Monster",   False),
        (Fraction(26, 1),      "bosonic",   False),
        (Fraction(72, 1),      "exceptional", False),
        (Fraction(100, 1),     "round",     False),
    ])
    def test_specific_c_rationality(self, c, label, expected_locus):
        info = simultaneous_rationality_at(c)
        assert info['in_rationality_locus'] is expected_locus

    def test_monster_dimension_196883_not_in_locus(self):
        info = simultaneous_rationality_at(Fraction(196_883))
        assert info['in_rationality_locus'] is False

    def test_evaluate_all_specific(self):
        rows = evaluate_specific_c_values()
        assert len(rows) == len(SPECIFIC_C_VALUES)
        # Exactly one row has in_rationality_locus = True (c = -24).
        in_locus = [r for r in rows if r['in_rationality_locus']]
        assert len(in_locus) == 1
        assert in_locus[0]['c'] == Fraction(-24)


# =============================================================================
# Path 9: Hasse-Weil L-factor of C_334.
# =============================================================================

class TestHasseWeilC334:

    @pytest.mark.parametrize("p", [11, 17, 19, 23, 29, 37, 43, 47, 53])
    def test_hasse_bound_good_primes(self, p):
        """|a_p| <= 2 sqrt(p) for all good primes."""
        assert hasse_bound_holds_C334(p) is True

    def test_a_p_known_values(self):
        """Values precomputed for cross-checking."""
        assert hasse_a_p_C334(11) == -4
        assert hasse_a_p_C334(17) == -6
        assert hasse_a_p_C334(19) == -4

    def test_L_factor_at_good_prime(self):
        """L_p(T) = 1 - a_p T + p T^2."""
        L = L_factor_C334_at_good_prime(11)
        assert L == (1, -(-4), 11)  # 1 + 4 T + 11 T^2

    def test_raises_on_bad_prime(self):
        with pytest.raises(ValueError):
            hasse_a_p_C334(13)


# =============================================================================
# Path 10: Point counts on C_444 mod p.
# =============================================================================

class TestPointCountsC444:

    @pytest.mark.parametrize("p", [23, 31, 37, 41, 47, 53, 61, 67, 71, 73])
    def test_hasse_weil_bound_good_primes(self, p):
        """For genus 2: |#C(F_p) - (p+1)| <= 4 sqrt(p), i.e. (diff)^2 <= 16 p."""
        assert hasse_weil_bound_holds_C444(p) is True

    @pytest.mark.parametrize("p", [23, 31, 37, 41, 47])
    def test_point_count_is_nonnegative(self, p):
        n = count_points_C444_mod_p(p)
        assert n >= 0
        assert n <= 2 * p + 2  # trivial upper bound


# =============================================================================
# Path 11: Jacobian decomposition of C_444.
# =============================================================================

class TestJacobianC444:

    def test_all_3_pair_partitions_count(self):
        """There are exactly 15 partitions of 6 items into 3 unordered pairs."""
        items = list(range(6))
        parts = all_3_pair_partitions([Fraction(x) for x in items])
        assert len(parts) == 15

    def test_no_extra_involution(self):
        """No Mobius involution swaps three pairs of the 6 rational Weierstrass
        points of C_444 -- Jac is geometrically simple."""
        assert has_extra_involution_C444() is False

    def test_jacobian_decomposition_simple(self):
        info = jacobian_decomposition_C444()
        assert info['simple'] is True
        assert info['partitions_tested'] == 15

    def test_extra_involution_would_cause_split(self):
        """Sanity: if we construct a FICTITIOUS set of 6 roots admitting a
        known involution (e.g., x -> -x swapping signs), has_extra_involution
        should detect it. We verify the detector itself works."""
        # A Mobius involution swapping pairs {a, -a}, {b, -b}, {c, -c} exists
        # (namely x -> -x). Test the _partition_admits_swap_involution on
        # this configuration.
        from compute.lib.c334_c444_arithmetic_engine import (
            _partition_admits_swap_involution)
        partition = [(Fraction(1), Fraction(-1)),
                     (Fraction(2), Fraction(-2)),
                     (Fraction(3), Fraction(-3))]
        assert _partition_admits_swap_involution(partition) is True


# =============================================================================
# Path 12: Cross-engine consistency with galois_w4_w5_engine.
# =============================================================================

class TestCrossEngineConsistency:

    def test_coeffs_match_galois_engine(self):
        """D_334 coefficients must match galois_w4_w5_engine's expansion."""
        from compute.lib.galois_w4_w5_engine import discriminant_polynomial_334
        c334, const = discriminant_polynomial_334()
        assert tuple(c334) == D334_COEFFS
        assert const == 42

    def test_D444_coeffs_match_galois_engine(self):
        from compute.lib.galois_w4_w5_engine import discriminant_polynomial_444
        c444, const = discriminant_polynomial_444()
        assert tuple(c444) == D444_COEFFS
        assert const == 7

    def test_g334_sq_value_matches(self):
        """g_{334}^2(c) and D_{334}(c) differ by a rational square.

        Specifically:
            g_{334}^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]
            D_{334}   = 42 (5c+22)(c+24)(7c+68)(3c+46)
        So g_{334}^2 * D_{334} = 42^2 c^2 (5c+22)^2 = [42 c (5c+22)]^2,
        i.e., their product is a square in Q(c).  Equivalently, in
        Q^*/Q^{*2}, the classes of g_{334}^2 and D_{334} coincide.
        """
        from compute.lib.galois_w4_w5_engine import g334_sq
        c = Fraction(100)  # generic value, no pole
        v_g = g334_sq(c)
        v_D = D334(c)
        product = v_g * v_D
        assert is_rational_square(product)

    def test_g444_sq_value_matches(self):
        """Same consistency check for g_{444}^2 and D_{444}."""
        from compute.lib.galois_w4_w5_engine import g444_sq
        c = Fraction(100)
        v_g = g444_sq(c)
        v_D = D444(c)
        product = v_g * v_D
        assert is_rational_square(product)


# =============================================================================
# Path 13: Discriminant of polynomials (auxiliary Sylvester resultant).
# =============================================================================

class TestDiscriminantComputation:

    def test_quadratic_discriminant(self):
        """disc(c^2 + b c + c0) = b^2 - 4 c0."""
        # P(x) = x^2 + 3x + 2, disc = 9 - 8 = 1
        coeffs = [2, 3, 1]  # constant first
        assert discriminant_polynomial(coeffs) == 1

    def test_quadratic_discriminant_2(self):
        # P(x) = 2 x^2 + 4x + 2, roots both at -1 (double root), disc = 0
        coeffs = [2, 4, 2]
        assert discriminant_polynomial(coeffs) == 0

    def test_cubic_discriminant_single_root(self):
        # (x-1)^3 = x^3 - 3 x^2 + 3x - 1, disc = 0
        coeffs = [-1, 3, -3, 1]
        assert discriminant_polynomial(coeffs) == 0

    def test_cubic_discriminant_distinct_roots(self):
        # x^3 - x = x(x-1)(x+1), disc = 4 * 0^3 - 27 * 0^2 for monic depressed,
        # but a general cubic ax^3+bx^2+cx+d has disc = 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2
        # Here a=1,b=0,c=-1,d=0: disc = 0 - 0 + 0 - 4*(-1)^3 - 0 = 4
        coeffs = [0, -1, 0, 1]  # x^3 - x
        assert discriminant_polynomial(coeffs) == 4

    def test_D334_discriminant_integer(self):
        """disc(D_334) is a specific nonzero integer."""
        d = discriminant_polynomial(D334_COEFFS)
        assert isinstance(d, int)
        assert d != 0

    def test_D444_discriminant_integer(self):
        d = discriminant_polynomial(D444_COEFFS)
        assert isinstance(d, int)
        assert d != 0


# =============================================================================
# Path 14: Integer det_int helper.
# =============================================================================

class TestDetInt:

    def test_identity_det(self):
        M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        assert _det_int(M) == 1

    def test_zero_det(self):
        M = [[1, 2], [2, 4]]
        assert _det_int(M) == 0

    def test_known_det(self):
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
        # det = 1(50-48) - 2(40-42) + 3(32-35) = 2 + 4 - 9 = -3
        assert _det_int(M) == -3


# =============================================================================
# Path 15: Summary sanity.
# =============================================================================

class TestSummary:

    def test_summary_runs(self):
        s = summary()
        assert 'D334' in s
        assert 'D444' in s
        assert 'rationality_locus_int_search' in s
        assert 'specific_c_evaluations' in s

    def test_summary_D334_bad_primes(self):
        s = summary()
        assert s['D334']['bad_primes'] == [2, 3, 5, 7, 13, 31, 41, 59]

    def test_summary_D444_jacobian_simple(self):
        s = summary()
        assert s['D444']['jacobian_simple'] is True

    def test_summary_D444_exceptional_point(self):
        s = summary()
        assert s['D444']['exceptional_point'] == (72, 69_237_168)

    def test_summary_locus_only_minus_24(self):
        s = summary()
        assert s['rationality_locus_int_search'] == [-24]
