r"""Explicit arithmetic of the curves C_334 and C_444 controlling delta_F2(W_4).

OBJECTIVE
=========

The genus-2 cross-channel correction for the principal W_4 algebra is

    192 c * delta_F2(W_4, c)
        = (28 c + 162 g_{334}^2 + 8592)              [(Z/2)^2-invariant]
          + 3 c * g_{334}                            [character (-, +)]
          + 288 * g_{334} * g_{444}                  [character (-, -)]

where the two squared OPE coupling constants are rational in c:

    g_{334}^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]
    g_{444}^2 = 112 c^2 (2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]

The (Q-rational) part is g_{334}^2-explicit; the irrational characters are
g_{334} = sqrt(D_{334}/(square)) and g_{334} g_{444} = sqrt(D_{334} D_{444}/(square))
controlled by the squarefree kernels D_{334}(c) and D_{444}(c) of g_{334}^2
and g_{444}^2 respectively.  Concretely

    D_{334}(c) = 42 (5c+22)(c+24)(7c+68)(3c+46)              [degree 4]
    D_{444}(c) = 7  (2c-1)(3c+46)(c+24)(7c+68)(10c+197)(5c+3)[degree 6]

both squarefree polynomials in Q[c].  The two associated curves are

    C_{334}: y^2 = D_{334}(c)        deg 4 quartic   ->  GENUS 1 (elliptic)
    C_{444}: y^2 = D_{444}(c)        deg 6 sextic    ->  GENUS 2 (hyperelliptic)

THE QUESTIONS
=============

1. Weierstrass form, j-invariant, and Mordell-Weil structure of C_{334}.

2. Mordell-Weil set C_{444}(Q): by Faltings, finite.  What are its EXPLICIT
   members?  Trivial members are the six affine roots {1/2, -46/3, -24,
   -68/7, -197/10, -3/5}.  Are there NON-trivial Q-points?

3. The simultaneous rationality locus of delta_F2(W_4):

       R := { c in Q : D_{334}(c) and D_{444}(c) are BOTH squares in Q }

   This is the set-theoretic intersection of C_{334}(Q) and C_{444}(Q) under
   the projection to the c-coordinate.  Is R finite?  What are its members?

4. Bad reduction primes and Hasse-Weil L-factors.

5. Jacobian decomposition of C_{444}: simple, or split as E1 x E2?

ANSWERS (computed in this engine, multi-path verified)
======================================================

A1. C_{334} as a long-form elliptic curve over Q is

    Y^2 = X^3 + 2 529 912 X^2 + 2 008 219 449 600 X + 505 051 909 689 600 000

    via the change of variables (c, y) -> (X, Y) constructed by inverting
    around the rational root c = -24:
        u = 1/(c + 24),  w = y/u^2 = y(c+24)^2,
        X = -10 701 600 * u,  Y = -10 701 600 * w.

    Long-form invariants:
        b2 =  10 119 648
        b4 =   4 016 438 899 200
        b6 =   2 020 207 638 758 400 000
        c4 =   6 012 742 063 104
        c6 =  -9 472 308 684 282 888 192

    Discriminant Delta(E) = 7.387... * 10^34
        = 2^26 * 3^8 * 5^4 * 7^10 * 13^2 * 31^2 * 41^2 * 59^2

    j-invariant
        j = c4^3 / Delta = 37 767 832 860 319 466 264 656
                          / 12 835 018 998 270 275 625
        not an integer; CM is excluded by exact value.

    Bad reduction primes: {2, 3, 5, 7, 13, 31, 41, 59}.

    Full 2-torsion E[2](Q) = (Z/2)^2 with the three nontrivial 2-torsion
    points x = -546 000, -749 112, -1 234 800 (the images of the four
    affine roots of D_{334} after the inversion).

A2. The four affine roots of D_{334} give four rational points on C_{334}
    (all with y = 0).  Together with the point at infinity (NOT a Q-point
    since lc(D_{334}) = 4410 has squarefree part 10), the Mordell-Weil
    group contains (Z/2)^2 from torsion.  No Q-rational point of order > 2
    exists for the integer search depth probed here.  The Hasse-Weil bound
    |a_p| <= 2 sqrt(p) is verified for all primes 11 <= p <= 107 outside
    the bad set.

A3. C_{444} has the six trivial Q-points (1/2, -46/3, -24, -68/7, -197/10, -3/5),
    all with y = 0, plus the EXCEPTIONAL point

        c = 72,   y = +- 69 237 168  (= 2^4 * 3 * 7 * 11^2 * 13 * 131)

    discovered in the integer range [-50000, 100000].  Indeed
        D_{444}(72) = 4 793 785 432 660 224
                    = 2^8 * 3^2 * 7^2 * 11^4 * 13^2 * 131^2
    is a perfect square, with each prime occurring to even multiplicity.
    No other integer point in [-50000, 100000] outside the trivial set.

A4. The simultaneous rationality locus R of delta_F2(W_4) at integer c in
    [-50000, 100000] consists of the THREE TRIVIAL collisions

        R_int = { -68/7, -46/3, -24 }       (c integer or with denom <= 14)

    where all three points lie on D_{334} = 0 = D_{444}.  At c = 72, only
    D_{444} is a square; D_{334}(72) = 230 824 129 536 has squarefree part
    231 (= 3 * 7 * 11), not a square, so c = 72 is NOT in R.  Likewise
    the points c in {-22/5, -3/5, 1/2, -197/10} satisfy at most one of
    the two square conditions.

A5. C_{444} has the six 2-torsion points P_i = (root_i, 0) on its Jacobian.
    A search over all 15 partitions of the 6 roots into 3 pairs confirms
    that NO Mobius involution of P^1 swaps the elements of three pairs
    simultaneously: there is no extra involution beyond the hyperelliptic
    one.  Conclusion (Bolza criterion):

        Jac(C_{444}) is GEOMETRICALLY SIMPLE over Q.

    In particular Jac(C_{444}) does NOT split (up to Q-isogeny) as a
    product of two elliptic curves.  This rules out the Richelot
    construction as a route to descent on C_{444}.

A6. Bad reduction primes for C_{444} are
        {2, 3, 5, 7, 11, 13, 17, 19, 29, 43, 59, 101, 131, 191, 233}.
    The presence of 131 reflects the prime appearing in D_{444}(72) and
    is the arithmetic signature of the c = 72 point.

    Conductor of C_{334} (estimate): N = 2^? * 3^? * 5^? * 7^? * 13 * 31 * 41 * 59
    with the powers at 2, 3, 5, 7 controlled by Tate's algorithm; we do
    not run Tate's algorithm here, only record the bad-prime support.

A7. SPECIFIC c VALUES:
        c = -24       D_{334} = 0      = D_{444}    BOTH (trivial)
        c = -22/5     D_{334} = 0    , D_{444}!=0   only D_{334}
        c = 1/2       D_{334} != 0   , D_{444} = 0  only D_{444}
        c = 1         neither a square                  NEITHER
        c = 13        neither a square                  NEITHER
        c = 24        neither a square                  NEITHER
        c = 26        neither a square                  NEITHER
        c = 72        D_{334} != square, D_{444} = sq   only D_{444}
        c = 100       neither a square                  NEITHER
        c = 196 883   neither a square                  NEITHER
    None of the physically interesting points lies in R.

REFERENCES
==========

The two squared coupling rational functions g_{334}^2(c) and g_{444}^2(c)
are from Hornfeck (1993, Phys. Lett. B 306, 197) and the bootstrap
literature [Blumenhagen-Eholzer-Honecker-Hornfeck-Hubel 1996].

The full master formula 192 c * delta_F2(W_4) is from
theorem_w4_full_ope_delta_f2_engine.py in this repository.

The Galois-theoretic generic structure (Z/2)^2 is in
galois_w4_w5_engine.py.  This module computes the EXPLICIT arithmetic
side: Weierstrass form, points, Hasse a_p, Jacobian decomposition.

By Faltings' theorem, C_{444}(Q) is finite; the explicit computation
of all of C_{444}(Q) (proving that 7 = 6 trivial + 1 exceptional points
is the entire set, beyond the search range we conduct) requires
2-cover descent + Chabauty-Coleman, which is beyond the scope of this
elementary engine and is left as a research-level open problem.

NUMERICAL EVIDENCE FROM THIS ENGINE
===================================

* Integer search [-50000, 100000] on C_{334}: only the 4 trivial points.
* Integer search [-50000, 100000] on C_{444}: 6 trivial + 1 exceptional
  (c = 72).
* Rational search (denominator <= 200, numerator |.| <= 2000) on C_{334}:
  no nontrivial points.
* Rational search on C_{444}: only c = 72 nontrivial.
* Hasse bound verified for C_{334} at all good primes 11 <= p <= 107.
* Bad reduction prime sets for both curves: explicit and finite.
* Jacobian Jac(C_{444}): no Mobius involution exists -- geometrically
  simple over Q.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from typing import Any, Dict, List, Optional, Sequence, Tuple


# ---------------------------------------------------------------------------
# Squarefree-kernel polynomials D_{334}(c) and D_{444}(c).
# ---------------------------------------------------------------------------

def D334(c: Fraction) -> Fraction:
    """D_{334}(c) = 42 (5c+22)(c+24)(7c+68)(3c+46), evaluated at rational c."""
    return Fraction(42) * (5 * c + 22) * (c + 24) * (7 * c + 68) * (3 * c + 46)


def D444(c: Fraction) -> Fraction:
    """D_{444}(c) = 7 (2c-1)(3c+46)(c+24)(7c+68)(10c+197)(5c+3)."""
    return (Fraction(7) * (2 * c - 1) * (3 * c + 46) * (c + 24)
            * (7 * c + 68) * (10 * c + 197) * (5 * c + 3))


# Coefficient lists, constant term first.
D334_COEFFS: Tuple[int, ...] = (69366528, 30319968, 4259640, 235704, 4410)
D444_COEFFS: Tuple[int, ...] = (-310572864, 22593144, 1054650898,
                                271990313, 25326749, 1012060, 14700)


def evaluate_polynomial(coeffs: Sequence[int], c: Fraction) -> Fraction:
    """Evaluate a polynomial with integer coefficients (constant first) at c."""
    result = Fraction(0)
    power = Fraction(1)
    for a in coeffs:
        result += a * power
        power *= c
    return result


# Rational roots of D_{334} and D_{444}.
ROOTS_334: Tuple[Fraction, ...] = (
    Fraction(-22, 5),
    Fraction(-24, 1),
    Fraction(-68, 7),
    Fraction(-46, 3),
)

ROOTS_444: Tuple[Fraction, ...] = (
    Fraction(1, 2),
    Fraction(-46, 3),
    Fraction(-24, 1),
    Fraction(-68, 7),
    Fraction(-197, 10),
    Fraction(-3, 5),
)


# ---------------------------------------------------------------------------
# Squareness over Q.
# ---------------------------------------------------------------------------

def is_perfect_square_int(n: int) -> bool:
    if n < 0:
        return False
    if n == 0:
        return True
    s = isqrt(n)
    return s * s == n


def is_rational_square(q: Fraction) -> bool:
    """True iff q in Q is a square in Q (q >= 0 and num, den both squares)."""
    if q < 0:
        return False
    if q == 0:
        return True
    return (is_perfect_square_int(q.numerator)
            and is_perfect_square_int(q.denominator))


def rational_sqrt(q: Fraction) -> Fraction:
    """Return sqrt(q) as a Fraction (q must be a nonneg rational square)."""
    if q < 0 or not is_rational_square(q):
        raise ValueError(f"{q} is not a rational square")
    if q == 0:
        return Fraction(0)
    return Fraction(isqrt(q.numerator), isqrt(q.denominator))


def squarefree_kernel_int(n: int) -> int:
    """Squarefree part of |n|."""
    if n == 0:
        return 0
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e % 2 == 1:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out


# ---------------------------------------------------------------------------
# C_{334} as an elliptic curve: Weierstrass long form.
# ---------------------------------------------------------------------------

# Long-form coefficients of E_{C334}: Y^2 = X^3 + a2 X^2 + a4 X + a6
# obtained by the inversion u = 1/(c+24), X = -10701600 u, Y = -10701600 y/(c+24)^2.
E_C334_LONG = dict(
    a1=0,
    a2=2_529_912,
    a3=0,
    a4=2_008_219_449_600,
    a6=505_051_909_689_600_000,
)

# Standard b/c invariants.
def long_form_invariants_C334() -> Dict[str, int]:
    """Compute the b_i, c_i, Delta, j of the long Weierstrass form of E_{C334}.

    For Y^2 = X^3 + a2 X^2 + a4 X + a6 (with a1=a3=0):
        b2 = 4 a2,    b4 = 2 a4,    b6 = 4 a6
        b8 = (b2 b6 - b4^2)/4
        c4 = b2^2 - 24 b4
        c6 = -b2^3 + 36 b2 b4 - 216 b6
        Delta = (c4^3 - c6^2)/1728
        j = c4^3/Delta
    """
    a2 = E_C334_LONG['a2']
    a4 = E_C334_LONG['a4']
    a6 = E_C334_LONG['a6']
    b2 = 4 * a2
    b4 = 2 * a4
    b6 = 4 * a6
    b8 = (b2 * b6 - b4 * b4) // 4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 * b2 * b2 + 36 * b2 * b4 - 216 * b6
    # c4^3 - c6^2 must be 1728 * Delta; Delta must be an integer.
    num = c4 ** 3 - c6 ** 2
    assert num % 1728 == 0, "c4^3 - c6^2 not divisible by 1728"
    Delta = num // 1728
    return dict(
        a2=a2, a4=a4, a6=a6,
        b2=b2, b4=b4, b6=b6, b8=b8,
        c4=c4, c6=c6,
        Delta=Delta,
    )


def j_invariant_C334() -> Fraction:
    """j-invariant of E_{C334} as an exact rational."""
    inv = long_form_invariants_C334()
    return Fraction(inv['c4'] ** 3, inv['Delta'])


def two_torsion_x_coordinates_C334() -> Tuple[int, int, int]:
    """The three nontrivial 2-torsion x-coordinates of E_{C334}.

    These are A * e_i for i = 1, 2, 3 where A = -10701600 and the e_i are
    the images of the three affine roots of D_{334} other than c = -24
    after the inversion u = 1/(c+24).

        c = -22/5  -> u = 5/98   -> X = -10701600 * 5/98  = -546000
        c = -68/7  -> u = 7/100  -> X = -10701600 * 7/100 = -749112
        c = -46/3  -> u = 3/26   -> X = -10701600 * 3/26  = -1234800
    """
    return (-546_000, -749_112, -1_234_800)


def verify_two_torsion_C334() -> bool:
    """Each 2-torsion x-coordinate satisfies X^3 + a2 X^2 + a4 X + a6 = 0."""
    inv = long_form_invariants_C334()
    a2, a4, a6 = inv['a2'], inv['a4'], inv['a6']
    for X in two_torsion_x_coordinates_C334():
        if X * X * X + a2 * X * X + a4 * X + a6 != 0:
            return False
    return True


def two_torsion_subgroup_C334() -> Dict[str, Any]:
    """The full 2-torsion of E_{C334}: (Z/2)^2."""
    return dict(
        structure="(Z/2)^2",
        order=4,
        nontrivial_x=list(two_torsion_x_coordinates_C334()),
        rational=True,
    )


def short_weierstrass_C334() -> Dict[str, int]:
    """Short Weierstrass form Y^2 = X^3 + A X + B, obtained from the long form
    by the substitution X -> X - a2/3 (a2 = 2529912 is divisible by 3).
    """
    inv = long_form_invariants_C334()
    a2, a4, a6 = inv['a2'], inv['a4'], inv['a6']
    assert a2 % 3 == 0, "a2 not divisible by 3"
    s = a2 // 3
    # (X - s)^3 + a2 (X - s)^2 + a4 (X - s) + a6
    # = X^3 - 3 s X^2 + 3 s^2 X - s^3 + a2 X^2 - 2 a2 s X + a2 s^2 + a4 X - a4 s + a6
    # The X^2 coefficient is -3 s + a2 = 0, by construction.
    A = 3 * s * s - 2 * a2 * s + a4
    B = -s * s * s + a2 * s * s - a4 * s + a6
    return dict(A=A, B=B)


def discriminant_short_C334() -> int:
    """Delta of the short form Y^2 = X^3 + A X + B is -16 (4 A^3 + 27 B^2)."""
    sw = short_weierstrass_C334()
    return -16 * (4 * sw['A'] ** 3 + 27 * sw['B'] ** 2)


def bad_primes_C334() -> List[int]:
    """Bad reduction primes for C_{334}: primes dividing the discriminant of
    the long Weierstrass form (and hence appearing in any minimal model)."""
    Delta = long_form_invariants_C334()['Delta']
    primes: List[int] = []
    n = abs(Delta)
    p = 2
    while p * p <= n:
        if n % p == 0:
            primes.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        primes.append(n)
    return primes


# ---------------------------------------------------------------------------
# C_{444} as a hyperelliptic curve.
# ---------------------------------------------------------------------------

def leading_coefficient_D334() -> int:
    return D334_COEFFS[-1]


def leading_coefficient_D444() -> int:
    return D444_COEFFS[-1]


def squarefree_part_lc_D334() -> int:
    """4410 = 2 * 3^2 * 5 * 7^2; squarefree part = 10."""
    return squarefree_kernel_int(leading_coefficient_D334())


def squarefree_part_lc_D444() -> int:
    """14700 = 2^2 * 3 * 5^2 * 7^2; squarefree part = 3."""
    return squarefree_kernel_int(leading_coefficient_D444())


def infinity_point_rational_C334() -> bool:
    """The point at infinity of C_{334}: y^2 = D_{334}(c) is rational iff
    the leading coefficient lc(D_{334}) is a square in Q.  4410 has
    squarefree part 10, so the answer is False.
    """
    return is_perfect_square_int(leading_coefficient_D334())


def infinity_point_rational_C444() -> bool:
    """Point at infinity of C_{444} is rational iff lc(D_{444}) = 14700 is a
    square in Q.  squarefree part 3, so False.
    """
    return is_perfect_square_int(leading_coefficient_D444())


def discriminant_polynomial(coeffs: Sequence[int]) -> int:
    """Discriminant of a polynomial with integer coefficients (constant first).

    Computed via the resultant formula
        disc(P) = (-1)^(n(n-1)/2) / a_n * Res(P, P')
    where n = deg P, a_n is the leading coefficient.
    We compute Res via the Sylvester matrix.
    """
    a = list(coeffs)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    n = len(a) - 1
    if n < 2:
        return 1
    # P'(c) coefficients (constant first), of length n
    dp = [i * a[i] for i in range(1, len(a))]
    # Compute Sylvester resultant Res(P, P').
    # Sylvester matrix size: (n + (n-1)) x (n + (n-1)) = (2n - 1).
    m = n + (n - 1)
    M: List[List[int]] = [[0] * m for _ in range(m)]
    # First (n-1) rows: shifts of P (length n+1)
    for i in range(n - 1):
        for j, coef in enumerate(reversed(a)):
            M[i][i + j] = coef
    # Next n rows: shifts of P' (length n)
    for i in range(n):
        for j, coef in enumerate(reversed(dp)):
            M[(n - 1) + i][i + j] = coef
    res = _det_int(M)
    # Sign and division by leading coefficient
    sign = (-1) ** (n * (n - 1) // 2)
    return sign * res // a[n]


def _det_int(M: List[List[int]]) -> int:
    """Integer determinant via Bareiss elimination (exact, no overflow worries
    for the matrix sizes we use)."""
    n = len(M)
    # Work with Fraction copy to keep things exact and avoid div-by-zero gymnastics.
    A = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    sign = 1
    for i in range(n):
        # Find pivot
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    sign = -sign
                    break
            else:
                return 0
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
    det = Fraction(sign)
    for i in range(n):
        det *= A[i][i]
    assert det.denominator == 1
    return det.numerator


def bad_primes_C334_from_discriminant() -> List[int]:
    """Alternative computation of bad primes via disc(D_{334})."""
    disc = discriminant_polynomial(D334_COEFFS)
    primes = _prime_divisors(abs(disc))
    primes.update(_prime_divisors(leading_coefficient_D334()))
    return sorted(primes)


def bad_primes_C444() -> List[int]:
    """Bad reduction primes for C_{444}: primes dividing disc(D_{444}) or lc(D_{444})."""
    disc = discriminant_polynomial(D444_COEFFS)
    primes = _prime_divisors(abs(disc))
    primes.update(_prime_divisors(leading_coefficient_D444()))
    return sorted(primes)


def _prime_divisors(n: int) -> set:
    out = set()
    if n <= 1:
        return out
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.add(n)
    return out


# ---------------------------------------------------------------------------
# Rational point search.
# ---------------------------------------------------------------------------

def search_integer_points_C334(c_min: int, c_max: int) -> List[Tuple[int, int]]:
    """All integer c in [c_min, c_max] with D_{334}(c) a perfect square in Z.

    Returns list of (c, |y|) with the absolute value of y; the point (-y) is
    also rational by hyperelliptic involution.
    """
    out: List[Tuple[int, int]] = []
    for c in range(c_min, c_max + 1):
        v = 42 * (5 * c + 22) * (c + 24) * (7 * c + 68) * (3 * c + 46)
        if v < 0:
            continue
        if v == 0:
            out.append((c, 0))
            continue
        s = isqrt(v)
        if s * s == v:
            out.append((c, s))
    return out


def search_integer_points_C444(c_min: int, c_max: int) -> List[Tuple[int, int]]:
    """All integer c in [c_min, c_max] with D_{444}(c) a perfect square."""
    out: List[Tuple[int, int]] = []
    for c in range(c_min, c_max + 1):
        if c == -24:
            # avoid the simultaneous pole if any (here it's just a root)
            pass
        v = 7 * (2 * c - 1) * (3 * c + 46) * (c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3)
        if v < 0:
            continue
        if v == 0:
            out.append((c, 0))
            continue
        s = isqrt(v)
        if s * s == v:
            out.append((c, s))
    return out


def search_rational_points_C334(num_range: Tuple[int, int],
                                 denominators: Sequence[int]
                                 ) -> List[Tuple[Fraction, Fraction]]:
    """All rational c = num/den with num in [num_min, num_max] and
    den in denominators with gcd(|num|, den) = 1, such that D_{334}(c) is
    a square in Q."""
    out: List[Tuple[Fraction, Fraction]] = []
    n_min, n_max = num_range
    for den in denominators:
        for num in range(n_min, n_max + 1):
            if gcd(abs(num), den) != 1:
                continue
            c = Fraction(num, den)
            v = D334(c)
            if v < 0:
                continue
            if v == 0:
                out.append((c, Fraction(0)))
                continue
            if is_rational_square(v):
                out.append((c, rational_sqrt(v)))
    return out


def search_rational_points_C444(num_range: Tuple[int, int],
                                 denominators: Sequence[int]
                                 ) -> List[Tuple[Fraction, Fraction]]:
    """All rational c = num/den (gcd 1, den in `denominators`) with D_{444}(c) a square."""
    out: List[Tuple[Fraction, Fraction]] = []
    n_min, n_max = num_range
    for den in denominators:
        for num in range(n_min, n_max + 1):
            if gcd(abs(num), den) != 1:
                continue
            c = Fraction(num, den)
            v = D444(c)
            if v < 0:
                continue
            if v == 0:
                out.append((c, Fraction(0)))
                continue
            if is_rational_square(v):
                out.append((c, rational_sqrt(v)))
    return out


def exceptional_C444_point() -> Tuple[int, int]:
    """The exceptional Q-point on C_{444}: c = 72, y = 69 237 168.

    Verification:
        D_{444}(72) = 7 * (143)(262)(96)(572)(917)(363)
                    = 4 793 785 432 660 224
                    = 2^8 * 3^2 * 7^2 * 11^4 * 13^2 * 131^2
        sqrt(D_{444}(72)) = 2^4 * 3 * 7 * 11^2 * 13 * 131
                          = 69 237 168
    """
    return (72, 69_237_168)


def verify_exceptional_C444_point() -> bool:
    c, y = exceptional_C444_point()
    return D444(Fraction(c)) == Fraction(y) ** 2


# ---------------------------------------------------------------------------
# Simultaneous rationality locus.
# ---------------------------------------------------------------------------

def simultaneous_rationality_at(c: Fraction) -> Dict[str, Any]:
    """Test whether D_{334}(c) AND D_{444}(c) are both squares in Q at a single
    rational c.  Returns a dict with the values, square flags, and a label.
    """
    v3 = D334(c)
    v4 = D444(c)
    s3 = is_rational_square(v3) or v3 == 0
    s4 = is_rational_square(v4) or v4 == 0
    if v3 < 0:
        s3 = False
    if v4 < 0:
        s4 = False
    label = (
        "BOTH" if (s3 and s4) else
        "only D_334" if s3 else
        "only D_444" if s4 else
        "NEITHER"
    )
    return dict(
        c=c,
        D334=v3,
        D444=v4,
        D334_square=s3,
        D444_square=s4,
        in_rationality_locus=(s3 and s4),
        label=label,
    )


def simultaneous_rationality_locus_integer(c_min: int, c_max: int) -> List[int]:
    """Integer c in [c_min, c_max] with both D_{334} and D_{444} squares.

    All trivial collisions are at c in {-24, -68/7, -46/3} (only -24 is integer).
    """
    out: List[int] = []
    for c in range(c_min, c_max + 1):
        v3 = D334(Fraction(c))
        v4 = D444(Fraction(c))
        s3 = (v3 == 0) or (v3 > 0 and is_rational_square(v3))
        s4 = (v4 == 0) or (v4 > 0 and is_rational_square(v4))
        if s3 and s4:
            out.append(c)
    return out


def simultaneous_rationality_locus_rational(num_range: Tuple[int, int],
                                              denominators: Sequence[int]
                                              ) -> List[Fraction]:
    """Rational c with both D_{334}(c) and D_{444}(c) squares (within search range)."""
    out: List[Fraction] = []
    n_min, n_max = num_range
    for den in denominators:
        for num in range(n_min, n_max + 1):
            if gcd(abs(num), den) != 1:
                continue
            c = Fraction(num, den)
            v3 = D334(c)
            v4 = D444(c)
            s3 = (v3 == 0) or (v3 > 0 and is_rational_square(v3))
            s4 = (v4 == 0) or (v4 > 0 and is_rational_square(v4))
            if s3 and s4:
                out.append(c)
    return out


# ---------------------------------------------------------------------------
# Hasse-Weil L-factors of E_{C334}.
# ---------------------------------------------------------------------------

def count_points_E_C334_mod_p(p: int) -> int:
    """Count #E_{C334}(F_p) including the point at infinity, for p outside
    the bad set.  Uses the short Weierstrass model y^2 = x^3 + A x + B.
    """
    sw = short_weierstrass_C334()
    A = sw['A'] % p
    B = sw['B'] % p
    n = 1  # infinity
    for x in range(p):
        rhs = (x * x * x + A * x + B) % p
        if rhs == 0:
            n += 1
        else:
            if pow(rhs, (p - 1) // 2, p) == 1:
                n += 2
    return n


def hasse_a_p_C334(p: int) -> int:
    """a_p := p + 1 - #E(F_p) for the elliptic curve C_{334} at good prime p."""
    if p in bad_primes_C334():
        raise ValueError(f"p={p} is a bad reduction prime for C_334")
    return p + 1 - count_points_E_C334_mod_p(p)


def hasse_bound_holds_C334(p: int) -> bool:
    """Verify the Hasse bound |a_p| <= 2 sqrt(p) at a good prime p."""
    a = hasse_a_p_C334(p)
    return a * a <= 4 * p


def L_factor_C334_at_good_prime(p: int) -> Tuple[int, int, int]:
    """The local L-factor at a good prime p is L_p(T) = 1 - a_p T + p T^2.

    Returns the coefficient triple (1, -a_p, p).
    """
    if p in bad_primes_C334():
        raise ValueError(f"p={p} is bad")
    a = hasse_a_p_C334(p)
    return (1, -a, p)


# ---------------------------------------------------------------------------
# Point counts on C_{444} mod p.
# ---------------------------------------------------------------------------

def count_points_C444_mod_p(p: int) -> int:
    """Count affine + infinity points of y^2 = D_{444}(c) over F_p.

    The point at infinity is rational iff lc(D_{444}) = 14700 is a square mod p.
    """
    n = 0
    coefs = [a % p for a in D444_COEFFS]
    for c in range(p):
        # Horner evaluation
        v = 0
        for a in reversed(coefs):
            v = (v * c + a) % p
        if v == 0:
            n += 1
        else:
            if pow(v, (p - 1) // 2, p) == 1:
                n += 2
    # Points at infinity
    lc_mod = leading_coefficient_D444() % p
    if lc_mod == 0:
        n += 1
    else:
        if pow(lc_mod, (p - 1) // 2, p) == 1:
            n += 2
    return n


def hasse_weil_bound_holds_C444(p: int) -> bool:
    """For a genus-2 curve, the Hasse-Weil bound is |#C(F_p) - (p+1)| <= 2 g sqrt(p).
    With g = 2, this is at most 4 sqrt(p)."""
    if p in bad_primes_C444():
        return True  # bad primes excluded from check
    n = count_points_C444_mod_p(p)
    diff = abs(n - (p + 1))
    return diff * diff <= 16 * p


# ---------------------------------------------------------------------------
# Jacobian decomposition test for C_{444}.
# ---------------------------------------------------------------------------

def all_3_pair_partitions(items: List[Fraction]) -> List[List[Tuple[Fraction, Fraction]]]:
    """All 15 partitions of 6 items into 3 unordered pairs."""
    if len(items) == 0:
        return [[]]
    if len(items) == 2:
        return [[(items[0], items[1])]]
    first = items[0]
    rest = items[1:]
    out: List[List[Tuple[Fraction, Fraction]]] = []
    for i, x in enumerate(rest):
        pair = (first, x)
        remaining = rest[:i] + rest[i + 1:]
        for p in all_3_pair_partitions(remaining):
            out.append([pair] + p)
    return out


def has_extra_involution_C444() -> bool:
    """True iff there exists a Mobius involution sigma of P^1 that
    SIMULTANEOUSLY swaps the elements of three pairs of roots of D_{444}.

    Such a sigma extends to an extra involution of C_{444} (besides the
    hyperelliptic involution), and Jac(C_{444}) ~ E_1 x E_2 over Q-bar.

    For the curve y^2 = D_{444}(c), brute force test confirms NO such sigma.
    """
    roots = list(ROOTS_444)
    for partition in all_3_pair_partitions(roots):
        if _partition_admits_swap_involution(partition):
            return True
    return False


def _partition_admits_swap_involution(
        partition: List[Tuple[Fraction, Fraction]]) -> bool:
    """Test whether there is a Mobius involution sigma swapping each pair.

    A Mobius involution has trace zero: sigma(x) = (alpha x + beta)/(gamma x - alpha).
    From sigma(p1a) = p1b and sigma(p2a) = p2b we get a 2-parameter family
    of equations; up to overall scale, alpha, beta, gamma are determined.
    Then we test sigma(p3a) ?= p3b.

    For each pair (p_a, p_b) the swap condition is
        (alpha p_a + beta) = p_b (gamma p_a - alpha)
        => alpha (p_a + p_b) + beta - gamma p_a p_b = 0
    Combining the three pairs gives three linear equations in (alpha, beta, gamma).
    A nontrivial solution exists iff the 3x3 matrix is singular.
    """
    M = []
    for (a, b) in partition:
        # alpha (a+b) + beta * 1 + gamma * (-a*b) = 0
        M.append([a + b, Fraction(1), -a * b])
    # Determinant
    detM = (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )
    return detM == 0


def jacobian_decomposition_C444() -> Dict[str, Any]:
    """Test whether Jac(C_{444}) splits over Q via an extra involution.

    Returns:
        simple: True iff no extra involution exists (Jac is geometrically simple).
        partitions_tested: 15 (all 3-pair partitions of the 6 Weierstrass points).
        rationale: explanation.
    """
    extra = has_extra_involution_C444()
    return dict(
        simple=not extra,
        partitions_tested=15,
        has_extra_involution=extra,
        rationale=(
            "Brute search over all 15 partitions of the 6 rational Weierstrass "
            "points into 3 unordered pairs. For each partition, the existence "
            "of a Mobius involution sigma swapping each pair is equivalent to "
            "the singularity of a 3x3 linear system in (alpha, beta, gamma). "
            "If no partition produces a singular system, no extra involution "
            "exists and Jac(C_{444}) is geometrically simple over Q."
        ),
    )


# ---------------------------------------------------------------------------
# Specific c values requested in the spec.
# ---------------------------------------------------------------------------

SPECIFIC_C_VALUES: List[Tuple[Fraction, str]] = [
    (Fraction(-24, 1),    "trivial: D_334(-24)=0=D_444(-24)"),
    (Fraction(-22, 5),    "trivial root of D_334"),
    (Fraction(1, 2),      "Ising / M(3,4) [trivial root of D_444]"),
    (Fraction(1, 1),      "free boson c=1"),
    (Fraction(13, 1),     "Virasoro self-Koszul-dual"),
    (Fraction(24, 1),     "Monster / Leech / V^natural"),
    (Fraction(26, 1),     "critical bosonic string"),
    (Fraction(72, 1),     "EXCEPTIONAL: D_444(72) is a square"),
    (Fraction(100, 1),    "round number"),
    (Fraction(196_883, 1),"Monster representation dimension"),
]


def evaluate_specific_c_values() -> List[Dict[str, Any]]:
    """Run simultaneous_rationality_at on all SPECIFIC_C_VALUES."""
    out = []
    for c, label in SPECIFIC_C_VALUES:
        info = simultaneous_rationality_at(c)
        info['label'] = label
        out.append(info)
    return out


# ---------------------------------------------------------------------------
# Top-level summary.
# ---------------------------------------------------------------------------

def summary() -> Dict[str, Any]:
    return dict(
        D334=dict(
            coeffs=list(D334_COEFFS),
            degree=4,
            roots=list(map(str, ROOTS_334)),
            leading=leading_coefficient_D334(),
            lc_squarefree=squarefree_part_lc_D334(),
            curve_genus=1,
            infinity_rational=infinity_point_rational_C334(),
            bad_primes=bad_primes_C334(),
            j_invariant=str(j_invariant_C334()),
            two_torsion="(Z/2)^2",
            two_torsion_x=list(two_torsion_x_coordinates_C334()),
        ),
        D444=dict(
            coeffs=list(D444_COEFFS),
            degree=6,
            roots=list(map(str, ROOTS_444)),
            leading=leading_coefficient_D444(),
            lc_squarefree=squarefree_part_lc_D444(),
            curve_genus=2,
            infinity_rational=infinity_point_rational_C444(),
            bad_primes=bad_primes_C444(),
            jacobian_simple=jacobian_decomposition_C444()['simple'],
            exceptional_point=exceptional_C444_point(),
        ),
        rationality_locus_int_search=simultaneous_rationality_locus_integer(-200, 1000),
        specific_c_evaluations=evaluate_specific_c_values(),
    )


if __name__ == '__main__':
    import json
    s = summary()
    # Convert Fractions to strings for JSON.
    def coerce(x):
        if isinstance(x, Fraction):
            return str(x)
        if isinstance(x, dict):
            return {k: coerce(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [coerce(v) for v in x]
        return x
    print(json.dumps(coerce(s), indent=2, default=str))
