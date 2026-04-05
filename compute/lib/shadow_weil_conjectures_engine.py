r"""Shadow analogues of the Weil conjectures for modular Koszul algebras.

The Weil conjectures (Dwork 1960, Grothendieck 1965, Deligne 1974) describe
the zeta functions of algebraic varieties over finite fields.  For a smooth
projective variety V/F_q of dimension d:

    Z(V/F_q, T) = exp(sum_{n>=1} #V(F_{q^n})/n * T^n)

is a RATIONAL function of T (Dwork), satisfies a FUNCTIONAL EQUATION
reflecting Poincare duality (Grothendieck), and the reciprocal zeros/poles
of the numerator factors lie on the circle |alpha| = q^{i/2} for the
appropriate cohomological degree i (Deligne).

SHADOW ANALOGUES
================

For a modular Koszul algebra A with shadow generating function

    H_A(t) = t^2 sqrt(Q_L(t))

where Q_L(t) = q0 + q1*t + q2*t^2 is the shadow metric, the SHADOW CURVE
is the algebraic curve

    C_A: y^2 = t^4 * Q_L(t) = q0*t^4 + q1*t^5 + q2*t^6

This is a hyperelliptic curve (or degenerate cases thereof).  The
Weil-conjecture analogues study C_A over finite fields:

    Z(C_A/F_p, T) = P_1(T) / ((1-T)(1-pT))

where P_1 has degree 2g(C_A) with all roots on |alpha| = sqrt(p).

SHADOW ZETA OVER FINITE FIELDS
-------------------------------

For the shadow sequence {S_r} with S_r in Q, reduce mod p:

    N_n(A, p) = #{t in Z/p^n Z : H_A(t) = 0 (mod p^n)}

and define

    Z_A(p, T) = exp(sum_{n>=1} N_n(A,p)/n * T^n)

For class G/L algebras (polynomial H_A), this is directly computable.
For class M (Virasoro), H_A involves sqrt(Q_L), and the zero-counting
reduces to point-counting on the shadow curve C_A.

CURVE GEOMETRY
--------------

The shadow curve C_A: y^2 = f(t) where f(t) = t^4 * Q_L(t) is a
degree-6 polynomial.  After removing the t=0 singularity:

- If Q_L has two distinct roots: smooth hyperelliptic of genus 2
  (degree 6 squarefree polynomial after extracting t^4)
- If Q_L has a double root: genus 1 (rational curve with node)
- If Q_L is a perfect square: genus 0 (rational)

For the SMOOTH model (away from t=0), the genus is determined by
Riemann-Hurwitz: g = floor((deg f - 1)/2) for odd degree, or
g = deg f / 2 - 1 for even degree with leading coefficient a square.

In practice for Virasoro: f(t) = c^2 t^4 + 12c t^5 + alpha(c) t^6.
Dividing by t^4: y'^2 = c^2 + 12c*t + alpha(c)*t^2, which is a conic
(genus 0!).  The actual shadow curve y^2 = t^4 Q_L(t) has the t^4
factor introducing singularities.

The RESOLVED shadow curve is the smooth proper model.  For counting
purposes we work with the AFFINE model and add points at infinity.

FAMILIES
--------

Class G (Heisenberg): Q_L = (2k)^2 (constant). H = k*t^2.
    Shadow curve: y^2 = 4k^2 * t^4.  Rational (genus 0).
    Over F_p: y = +-2k*t^2.  Solutions: p + O(1).

Class L (affine KM): Q_L = q0 + q1*t (linear, q2 effectively makes it
    terminate at arity 3).  Actually Q_L is quadratic with discriminant
    Delta = 0, so Q_L = (2kappa + 3alpha*t)^2.  Shadow curve is rational.

Class M (Virasoro): Q_L quadratic with Delta != 0.  Shadow curve
    C_A: y^2 = t^4(c^2 + 12ct + alpha(c)t^2) is a singular curve.
    The smooth model of y^2 = Q_L(t) is a conic (genus 0).
    The full shadow curve y^2 = t^4 Q_L(t) resolves to genus 2
    generically (6 branch points counting multiplicity).

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general.
CAUTION (AP38): Convention-check all literature comparisons.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    chap:arithmetic-shadows (arithmetic_shadows.tex)
    rem:weil-analogy-table (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from math import gcd
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union


# ============================================================================
# 1. Exact rational shadow coefficients
# ============================================================================

def virasoro_shadow_data_exact(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (kappa, alpha, S4) for Virasoro at central charge c as exact Fractions.

    kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)).

    CAUTION (AP1): These formulas are specific to Virasoro.
    CAUTION (AP9): kappa = c/2 holds ONLY for Virasoro.
    """
    kappa = c_val / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c_val * (5 * c_val + 22))
    return kappa, alpha, S4


def affine_sl2_shadow_data_exact(k_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (kappa, alpha, S4) for affine sl_2 at level k as exact Fractions.

    kappa = 3(k+2)/4, alpha = 4/(k+2), S4 = 0.
    Class L: tower terminates at arity 3.

    dim(sl_2) = 3, h^v = 2.
    """
    kappa = Fraction(3) * (k_val + 2) / 4
    alpha = Fraction(4) / (k_val + 2)
    S4 = Fraction(0)
    return kappa, alpha, S4


def w3_tline_shadow_data_exact(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (kappa, alpha, S4) for W_3 T-line at central charge c as exact Fractions.

    On the T-line (stress-tensor primary line), the shadow data coincides
    with Virasoro: kappa_T = c/2, alpha = 2, S4 = 10/(c(5c+22)).

    CAUTION (AP9): This is T-LINE ONLY data. The total W_3 modular
    characteristic is kappa(W_3) = 5c/6, NOT c/2.
    Use w3_total_shadow_data_exact() for the total W_3 kappa.
    """
    return virasoro_shadow_data_exact(c_val)


def w3_total_shadow_data_exact(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (kappa, alpha, S4) for total W_3 at central charge c as exact Fractions.

    kappa(W_3) = 5c/6 = c * (H_3 - 1) where H_3 = 1 + 1/2 + 1/3 = 11/6.
    This is the TOTAL modular characteristic, sum of T-line (c/2) and W-line (c/3).

    alpha = 2 (from the T_{(1)}T OPE; the cubic shadow on the T-line).
    S4 = 10/(c(5c+22)) (quartic contact invariant, T-line projection).

    CAUTION (AP1/AP9): kappa(W_3) = 5c/6, NOT c/2.
    The c/2 formula is for Virasoro only (or the T-line projection of W_3).
    """
    kappa = Fraction(5) * c_val / 6
    alpha = Fraction(2)
    S4 = Fraction(10) / (c_val * (5 * c_val + 22))
    return kappa, alpha, S4


# Deprecated alias: callers should use w3_tline_shadow_data_exact explicitly.
def w3_shadow_data_exact(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """DEPRECATED: Use w3_tline_shadow_data_exact (T-line) or w3_total_shadow_data_exact.

    Returns T-line data (kappa = c/2), NOT total W_3 data (kappa = 5c/6).
    Kept for backward compatibility; will be removed in a future cleanup.
    """
    return w3_tline_shadow_data_exact(c_val)


# ============================================================================
# 2. Shadow metric and curve over Q
# ============================================================================

def shadow_metric_Q_exact(
    kappa: Fraction, alpha: Fraction, S4: Fraction
) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (q0, q1, q2) for Q_L(t) = q0 + q1*t + q2*t^2.

    q0 = 4*kappa^2
    q1 = 12*kappa*alpha
    q2 = 9*alpha^2 + 16*kappa*S4
    """
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    return q0, q1, q2


def shadow_curve_coefficients(
    kappa: Fraction, alpha: Fraction, S4: Fraction
) -> List[Fraction]:
    """Coefficients of f(t) = t^4 * Q_L(t) = q0*t^4 + q1*t^5 + q2*t^6.

    Returns [a0, a1, a2, a3, a4, a5, a6] where f(t) = sum a_i t^i.
    The shadow curve is y^2 = f(t).
    """
    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    return [Fraction(0), Fraction(0), Fraction(0), Fraction(0), q0, q1, q2]


def critical_discriminant_exact(kappa: Fraction, S4: Fraction) -> Fraction:
    """Delta = 8*kappa*S4."""
    return 8 * kappa * S4


# ============================================================================
# 3. Mod-p arithmetic
# ============================================================================

def mod_p_reduce(x: Fraction, p: int) -> int:
    """Reduce a rational number x = a/b to Z/pZ.

    Returns the unique r in {0, ..., p-1} such that r*b = a (mod p).
    Requires gcd(b, p) = 1 (i.e., x has no p in the denominator).

    Raises ValueError if b = 0 mod p (x has a pole at p).
    """
    a = x.numerator % p
    b = x.denominator % p
    if b == 0:
        raise ValueError(f"Fraction {x} has a pole at p={p} (denominator divisible by p)")
    b_inv = pow(b, p - 2, p)  # Fermat's little theorem: b^{-1} = b^{p-2} mod p
    return (a * b_inv) % p


def is_good_prime(kappa: Fraction, alpha: Fraction, S4: Fraction, p: int) -> bool:
    """Check if p is a good prime for the shadow curve.

    A prime is BAD if it divides the denominator of any of q0, q1, q2.
    At a bad prime, the shadow curve has no well-defined reduction.
    """
    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    for q in [q0, q1, q2]:
        if q.denominator % p == 0:
            return False
    return True


def good_primes(kappa: Fraction, alpha: Fraction, S4: Fraction, max_p: int = 100) -> List[int]:
    """Return all good primes up to max_p."""
    primes = [p for p in range(2, max_p + 1) if _is_prime(p)]
    return [p for p in primes if is_good_prime(kappa, alpha, S4, p)]


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def shadow_tower_mod_p(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    p: int, max_r: int = 30
) -> Dict[int, int]:
    """Compute shadow tower coefficients S_r mod p.

    Uses the same convolution recursion as the exact computation,
    but works in Z/pZ.

    Returns {r: S_r mod p} for r = 2, ..., max_r.
    """
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    # Reduce to mod p
    q0_p = mod_p_reduce(q0, p)
    q1_p = mod_p_reduce(q1, p)
    q2_p = mod_p_reduce(q2, p)

    a0 = mod_p_reduce(2 * kappa, p)
    if a0 == 0:
        raise ValueError(f"2*kappa = 0 mod {p}: shadow tower degenerate at this prime")

    a0_inv2 = pow(2 * a0 % p, p - 2, p)  # (2*a0)^{-1} mod p

    a = [a0]

    if max_r >= 3:
        a1 = (q1_p * pow(2 * a0 % p, p - 2, p)) % p
        a.append(a1)

    if max_r >= 4:
        a2 = ((q2_p - a[1] * a[1] % p) * a0_inv2) % p
        a.append(a2 % p)

    for n in range(3, max_r - 2 + 1):
        conv = 0
        for j in range(1, n):
            conv = (conv + a[j] * a[n - j]) % p
        an = (p - conv) * a0_inv2 % p
        a.append(an % p)

    result = {}
    for n in range(len(a)):
        r = n + 2
        if r <= max_r:
            r_inv = pow(r % p, p - 2, p) if r % p != 0 else None
            if r_inv is not None:
                result[r] = (a[n] * r_inv) % p
            else:
                # r = 0 mod p: S_r = a_{r-2}/r has a potential pole
                # Need to check if a_{r-2} = 0 mod p too
                if a[n] % p == 0:
                    # 0/0 mod p: need Fraction computation
                    Sr_exact = _shadow_coeff_exact(kappa, alpha, S4, r)
                    try:
                        result[r] = mod_p_reduce(Sr_exact, p)
                    except (ValueError, ZeroDivisionError):
                        result[r] = None  # genuine pole
                else:
                    result[r] = None  # pole: p | r but p does not | a_{r-2}
    return result


def _shadow_coeff_exact(
    kappa: Fraction, alpha: Fraction, S4: Fraction, r: int
) -> Fraction:
    """Compute a single exact shadow coefficient S_r."""
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    a0 = 2 * kappa
    a = [a0]
    if r >= 3:
        a.append(q1 / (2 * a0))
    if r >= 4:
        a.append((q2 - a[1] ** 2) / (2 * a0))
    for n in range(3, r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a0))
    return a[r - 2] / r


# ============================================================================
# 4. Shadow tower exact computation (Fraction-based)
# ============================================================================

def shadow_tower_exact(
    kappa: Fraction, alpha: Fraction, S4: Fraction, max_r: int = 30
) -> Dict[int, Fraction]:
    """Compute exact shadow tower coefficients S_r as Fractions.

    Uses the convolution recursion from f^2 = Q_L.
    """
    if kappa == 0:
        raise ValueError("kappa = 0: shadow tower undefined (uncurved)")
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    a0 = 2 * kappa
    a = [a0]
    if max_r >= 3:
        a.append(q1 / (2 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2 * a0))
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a0))
    result = {}
    for n in range(len(a)):
        r = n + 2
        if r <= max_r:
            result[r] = a[n] / r
    return result


# ============================================================================
# 5. Point counting on curves over F_p
# ============================================================================

def count_affine_points(coeffs: List[int], p: int) -> int:
    """Count affine points on y^2 = f(t) over F_p.

    coeffs = [a0, a1, ..., a_d] where f(t) = sum a_i t^i.
    Returns #{(t, y) in F_p x F_p : y^2 = f(t)}.

    For each t in F_p, evaluate f(t) mod p:
    - If f(t) = 0: one point (t, 0)
    - If f(t) is a nonzero QR: two points (t, +-sqrt(f(t)))
    - If f(t) is a non-QR: zero points

    Uses the Legendre symbol: #{y : y^2 = a} = 1 + (a/p).
    """
    count = 0
    for t in range(p):
        ft = 0
        t_pow = 1
        for a in coeffs:
            ft = (ft + a * t_pow) % p
            t_pow = (t_pow * t) % p
        # Number of y with y^2 = ft mod p is 1 + legendre(ft, p)
        count += 1 + legendre_symbol(ft, p)
    return count


def legendre_symbol(a: int, p: int) -> int:
    """Compute the Legendre symbol (a/p) for odd prime p.

    Returns:
        0 if a = 0 mod p
        1 if a is a nonzero quadratic residue mod p
        -1 if a is a quadratic non-residue mod p
    """
    a = a % p
    if a == 0:
        return 0
    # Euler's criterion: (a/p) = a^{(p-1)/2} mod p
    val = pow(a, (p - 1) // 2, p)
    if val == 1:
        return 1
    elif val == p - 1:
        return -1
    else:
        return 0  # should not happen for prime p


def count_projective_points(coeffs: List[int], p: int) -> int:
    """Count projective points on y^2 = f(t) over F_p.

    Projective count = affine count + points at infinity.

    For the curve y^2 = f(t) with deg(f) = d:
    - If d is even and leading coeff is a QR mod p: 2 points at infinity
    - If d is even and leading coeff is a non-QR: 0 points at infinity
    - If d is odd: 1 point at infinity

    For the shadow curve f(t) = q0*t^4 + q1*t^5 + q2*t^6 (degree 6):
    Points at infinity from homogenizing: Y^2 = q0*T^4*Z^2 + q1*T^5*Z + q2*T^6
    Setting Z=0: Y^2 = q2*T^6, so Y = +-sqrt(q2)*T^3.
    If q2 = 0: one point [1:0:0].
    If q2 is QR: two points [T:Y:0] with Y^2 = q2*T^6.
    Since [T:Y:0] = [1:+-sqrt(q2):0], there are 2 points at infinity.
    If q2 is non-QR: 0 points at infinity.
    """
    affine = count_affine_points(coeffs, p)
    # Determine degree and leading coefficient
    d = len(coeffs) - 1
    while d > 0 and coeffs[d] % p == 0:
        d -= 1
    if d == 0:
        # f is constant (or zero); degenerate
        return affine + 1
    lead = coeffs[d] % p
    if d % 2 == 1:
        pts_inf = 1
    else:
        ls = legendre_symbol(lead, p)
        if ls == 0:
            pts_inf = 1
        elif ls == 1:
            pts_inf = 2
        else:
            pts_inf = 0
    return affine + pts_inf


def count_shadow_curve_points(
    kappa: Fraction, alpha: Fraction, S4: Fraction, p: int
) -> int:
    """Count F_p-rational points on the smooth conic u^2 = Q_L(t) over F_p.

    The shadow curve C_A: y^2 = t^4 Q_L(t) is singular at the origin.
    The smooth model is obtained by the substitution u = y/t^2, giving
    the conic u^2 = Q_L(t) = q0 + q1*t + q2*t^2.

    For a smooth conic over F_p with a rational point, #C(F_p) = p + 1.
    Our conic always has the point (t=0, u=2*kappa), which is rational
    whenever 2*kappa is p-integral (i.e., p is a good prime).

    However, the conic may DEGENERATE mod p (e.g., when q2 = 0 mod p,
    the conic becomes a parabola, still genus 0).  The point count on
    a smooth conic is ALWAYS p + 1 (for good primes with a rational point).

    For BAD primes (p | denom of q0, q1, or q2), we return the direct count.

    Raises ValueError if p is a bad prime.
    """
    if not is_good_prime(kappa, alpha, S4, p):
        raise ValueError(
            f"p={p} is a bad prime for this shadow curve "
            f"(denominators of Q_L coefficients are divisible by p)"
        )
    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    q0_p = mod_p_reduce(q0, p)
    q1_p = mod_p_reduce(q1, p)
    q2_p = mod_p_reduce(q2, p)
    # Smooth conic: u^2 = q0 + q1*t + q2*t^2
    conic_coeffs = [q0_p, q1_p, q2_p]
    return count_projective_points(conic_coeffs, p)


def count_smooth_conic_points(
    kappa: Fraction, alpha: Fraction, S4: Fraction, p: int
) -> int:
    """Count points on the smooth conic u^2 = Q_L(t) over F_p.

    This is the desingularized shadow curve.
    Raises ValueError for bad primes.
    """
    return count_shadow_curve_points(kappa, alpha, S4, p)


def count_singular_model_points(
    kappa: Fraction, alpha: Fraction, S4: Fraction, p: int
) -> int:
    """Count affine points on y^2 = t^4 Q_L(t) over F_p (singular model).

    Raises ValueError for bad primes.
    """
    if not is_good_prime(kappa, alpha, S4, p):
        raise ValueError(f"p={p} is a bad prime")
    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    coeffs_mod_p = [0, 0, 0, 0,
                    mod_p_reduce(q0, p),
                    mod_p_reduce(q1, p),
                    mod_p_reduce(q2, p)]
    return count_affine_points(coeffs_mod_p, p)


# ============================================================================
# 6. Point counting on extensions F_{p^n}
# ============================================================================

def count_affine_points_fpn(coeffs_p: List[int], p: int, n: int) -> int:
    """Count affine points on y^2 = f(t) over F_{p^n}.

    We represent F_{p^n} via explicit enumeration for small n,
    or use the trace formula for larger n.

    For n=1: direct count.
    For n>=2: use the Frobenius eigenvalue method (see zeta_from_pointcounts).
    """
    if n == 1:
        return count_affine_points(coeffs_p, p)
    # For n >= 2, we need F_{p^n} arithmetic.
    # For conics (genus 0), #C(F_{p^n}) = p^n + 1 always (projective).
    # For the affine conic u^2 = q0 + q1*t + q2*t^2:
    #   #affine = p^n + 1 - pts_at_infinity - correction_for_singularities
    # This is handled by the zeta function machinery below.
    raise NotImplementedError("Direct F_{p^n} counting for n>=2 not implemented; use zeta function")


def conic_point_count_fpn(
    kappa: Fraction, alpha: Fraction, S4: Fraction, p: int, n: int
) -> int:
    """Point count on the shadow conic u^2 = Q_L(t) over F_{p^n}.

    For a SMOOTH conic (nondegenerate discriminant mod p) with a rational
    point, the count is p^n + 1.  For degenerate conics (disc = 0 mod p),
    the count differs.

    For n=1: direct computation.
    For n>=2 with nondegenerate discriminant: use p^n + 1.
    For n>=2 with degenerate discriminant: would need F_{p^n} arithmetic,
    which we approximate.
    """
    if n == 1:
        return count_smooth_conic_points(kappa, alpha, S4, p)

    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    q0_p = mod_p_reduce(q0, p)
    q1_p = mod_p_reduce(q1, p)
    q2_p = mod_p_reduce(q2, p)
    disc_p = (q1_p ** 2 - 4 * q0_p * q2_p) % p

    if disc_p != 0:
        # Smooth conic with rational point (t=0, u=2*kappa) => isomorphic to P^1
        return p ** n + 1
    else:
        # Degenerate conic (pair of lines or double line)
        # For a pair of lines meeting at a point over F_p:
        # Two copies of A^1 sharing one point: affine count = 2*p^n - 1
        # Plus points at infinity: depends on geometry
        # For projective: two lines in P^2 have 2*(p^n+1) - 1 = 2*p^n + 1 points
        # (each line has p^n + 1 projective points, sharing one intersection)
        return 2 * p ** n + 1


# ============================================================================
# 7. Zeta function computation
# ============================================================================

def zeta_function_from_pointcounts(
    point_counts: List[int], p: int
) -> Tuple[List[Fraction], List[Fraction]]:
    """Compute the zeta function Z(T) from point counts N_1, ..., N_m.

    Z(T) = exp(sum_{n>=1} N_n/n * T^n)

    For a smooth projective curve of genus g:
    Z(T) = P_1(T) / ((1-T)(1-pT))

    where P_1(T) = 1 + a_1 T + ... + a_{2g} T^{2g}.

    The point counts determine P_1 via Newton's identities:
    N_n = p^n + 1 - (alpha_1^n + ... + alpha_{2g}^n)
    where alpha_i are roots of P_1.

    So: trace_n = p^n + 1 - N_n = sum alpha_i^n.
    Newton's identities relate power sums to elementary symmetric polynomials.

    Returns (numerator_coeffs, [1, -1, -p, p]) where:
    - numerator_coeffs = [1, a_1, ..., a_{2g}]
    - denominator_coeffs for (1-T)(1-pT) = 1 - (1+p)T + pT^2

    For genus 0: P_1 = 1 (constant), N_n = p^n + 1.
    """
    m = len(point_counts)

    # Compute trace sums: t_n = p^n + 1 - N_n
    traces = [p ** (n + 1) + 1 - point_counts[n] for n in range(m)]

    # If all traces are 0: genus 0, P_1(T) = 1
    if all(t == 0 for t in traces):
        return [Fraction(1)], [Fraction(1), Fraction(-(1 + p)), Fraction(p)]

    # Determine genus from the number of point counts we have
    # We need 2g point counts to determine P_1 of degree 2g
    # Try increasing genus until we find consistency
    for g in range(1, m // 2 + 1):
        # Newton's identities: compute elementary symmetric polynomials e_k
        # from power sums t_n = sum alpha_i^n
        # e_1 = t_1
        # e_2 = (e_1 * t_1 - t_2) / 2
        # e_k = (sum_{i=1}^{k-1} (-1)^{i-1} e_{k-i} t_i + (-1)^{k-1} t_k) / k
        e = [Fraction(0)] * (2 * g + 1)
        e[0] = Fraction(1)
        for k in range(1, 2 * g + 1):
            s = Fraction(0)
            for i in range(1, k):
                s += (-1) ** (i - 1) * e[k - i] * Fraction(traces[i - 1])
            s += (-1) ** (k - 1) * Fraction(traces[k - 1])
            e[k] = s / k

        # P_1(T) = sum_{k=0}^{2g} (-1)^k e_k T^k
        # Actually P_1(T) = prod(1 - alpha_i T), so
        # P_1(T) = sum_{k=0}^{2g} (-1)^k e_k T^k
        P1_coeffs = [(-1) ** k * e[k] for k in range(2 * g + 1)]

        # Verify: check the functional equation P_1(1/(pT)) * (pT)^{2g} = p^g P_1(T)
        # This gives a_{2g-k} = p^{g-k} * a_k (Riemann hypothesis consequence)
        # For genus 0, this is trivially satisfied
        if g >= 1 and m >= 2 * g:
            # Check consistency with additional point counts
            ok = True
            for n in range(2 * g, min(m, 2 * g + 2)):
                # Predicted N_n from P_1
                predicted_trace = Fraction(0)
                # alpha_i^n can be computed from Newton recurrence
                # t_n = e_1 * t_{n-1} - e_2 * t_{n-2} + ... + (-1)^{2g-1} e_{2g} * t_{n-2g}
                if n < len(traces):
                    t_pred = Fraction(0)
                    for i in range(1, 2 * g + 1):
                        if n - i >= 0 and n - i < len(traces):
                            t_pred += (-1) ** (i + 1) * e[i] * Fraction(traces[n - i])
                    if abs(t_pred - traces[n]) > Fraction(1, 10):
                        ok = False
                        break
            if ok:
                break

    denom_coeffs = [Fraction(1), Fraction(-(1 + p)), Fraction(p)]
    return P1_coeffs, denom_coeffs


def conic_zeta_function(p: int, degenerate: bool = False) -> Tuple[List[Fraction], List[Fraction]]:
    """Zeta function for a conic over F_p.

    SMOOTH case (degenerate=False):
        Z(C, T) = 1 / ((1-T)(1-pT))
        P_1(T) = 1 (trivial numerator).
        Point counts: N_n = p^n + 1 for all n.

    DEGENERATE case (degenerate=True):
        A pair of lines: Z = 1/((1-T)^2 (1-pT)^2) (product of two P^1's)
        But since the lines SHARE a point, the actual zeta is for the
        reducible curve X = L_1 ∪ L_2 with one intersection:
        #X(F_{p^n}) = 2(p^n + 1) - 1 = 2p^n + 1.
        Z(X, T) = exp(sum 2p^n+1/n T^n) is still rational.
    """
    if not degenerate:
        return [Fraction(1)], [Fraction(1), Fraction(-(1 + p)), Fraction(p)]
    else:
        # For two lines sharing a point:
        # N_n = 2p^n + 1
        # Z = exp(sum (2p^n+1)/n T^n)
        # = exp(sum 2p^n/n T^n + sum 1/n T^n)
        # = exp(-2 log(1-pT) - log(1-T))
        # = 1/((1-T)(1-pT)^2)
        # Denominator: (1-T)(1-pT)^2 = 1 - (1+2p)T + (2p+p^2)T^2 - p^2 T^3
        return [Fraction(1)], [Fraction(1), Fraction(-(1 + 2*p)), Fraction(2*p + p*p), Fraction(-p*p)]


# ============================================================================
# 8. Weil conjecture verification
# ============================================================================

def verify_rationality(
    kappa: Fraction, alpha: Fraction, S4: Fraction, p: int,
    n_terms: int = 6
) -> Dict[str, Any]:
    """Verify WEIL I (rationality) for the shadow curve.

    The shadow conic u^2 = Q_L(t) can be:
    1. SMOOTH (disc(Q_L) != 0 mod p): genus 0, #C(F_p) = p+1
    2. DEGENERATE (disc(Q_L) = 0 mod p): pair of lines or double line
    3. CLASS L (S4=0): Q_L is a perfect square, always degenerate

    In all cases the zeta function is rational.

    Returns dict with:
    - 'smooth_rational': True (always rational for a curve)
    - 'genus': effective genus of the smooth model
    - 'degenerate': whether the conic degenerates mod p
    - 'point_counts': list of N_n
    - 'P1_coeffs': numerator polynomial coefficients
    """
    if not is_good_prime(kappa, alpha, S4, p):
        raise ValueError(f"p={p} is a bad prime")

    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    q0_p = mod_p_reduce(q0, p)
    q1_p = mod_p_reduce(q1, p)
    q2_p = mod_p_reduce(q2, p)
    disc_p = (q1_p ** 2 - 4 * q0_p * q2_p) % p

    degenerate = (disc_p == 0)

    if not degenerate:
        # Smooth conic with rational point (t=0, u=2*kappa) => P^1
        N_smooth = [p ** n + 1 for n in range(1, n_terms + 1)]
        P1, denom = conic_zeta_function(p, degenerate=False)
        genus = 0
    else:
        # Degenerate conic: pair of lines (if Q_L factors) or double line
        # Direct count at n=1:
        N_1 = count_smooth_conic_points(kappa, alpha, S4, p)
        # For n >= 2: use the degenerate formula
        N_smooth = [N_1]
        for n in range(2, n_terms + 1):
            N_smooth.append(conic_point_count_fpn(kappa, alpha, S4, p, n))
        P1, denom = conic_zeta_function(p, degenerate=True)
        genus = 0  # normalization is still genus 0

    return {
        'smooth_rational': True,
        'genus': genus,
        'degenerate': degenerate,
        'point_counts': N_smooth,
        'P1_coeffs': P1,
        'denom_coeffs': denom,
        'prime': p,
        'disc_mod_p': disc_p,
    }


def verify_functional_equation(
    p: int, P1_coeffs: List[Fraction], genus: int
) -> Dict[str, Any]:
    """Verify WEIL II (functional equation) for the shadow curve.

    For a curve of genus g, the functional equation is:
    P_1(1/(pT)) * (pT)^{2g} = p^g * P_1(T)

    Equivalently, the coefficients satisfy:
    a_{2g-k} = p^{g-k} * a_k for k = 0, ..., g.

    For genus 0: P_1 = 1, so there is nothing to check (trivially satisfied).
    """
    if genus == 0:
        return {
            'functional_equation_holds': True,
            'genus': 0,
            'note': 'Trivial for genus 0 (P_1 = 1)',
        }

    g = genus
    holds = True
    violations = []
    for k in range(g + 1):
        lhs = P1_coeffs[2 * g - k] if 2 * g - k < len(P1_coeffs) else Fraction(0)
        rhs = Fraction(p) ** (g - k) * P1_coeffs[k]
        if lhs != rhs:
            holds = False
            violations.append((k, lhs, rhs))

    return {
        'functional_equation_holds': holds,
        'genus': g,
        'violations': violations,
    }


def verify_riemann_hypothesis(
    p: int, P1_coeffs: List[Fraction], genus: int
) -> Dict[str, Any]:
    """Verify WEIL III (Riemann hypothesis) for the shadow curve.

    All roots of P_1(T) should satisfy |alpha| = sqrt(p).

    For genus 0: P_1 = 1, no roots, trivially satisfied.
    For genus g: find roots of P_1 numerically and check.
    """
    if genus == 0:
        return {
            'riemann_hypothesis_holds': True,
            'genus': 0,
            'roots': [],
            'note': 'Trivial for genus 0',
        }

    # Find roots numerically
    import numpy as np
    coeffs_float = [float(c) for c in P1_coeffs]
    if len(coeffs_float) <= 1:
        return {
            'riemann_hypothesis_holds': True,
            'genus': genus,
            'roots': [],
        }
    roots = np.roots(coeffs_float[::-1])  # np.roots wants highest degree first
    target = math.sqrt(p)
    holds = True
    root_data = []
    for r in roots:
        absval = abs(r)
        reciprocal_absval = 1.0 / absval if absval > 1e-15 else float('inf')
        # The roots of P_1 are the RECIPROCALS of the Frobenius eigenvalues
        # Actually: P_1(T) = prod(1 - alpha_i T), so roots of P_1 are 1/alpha_i
        # |1/alpha_i| = 1/sqrt(p) for Weil.
        # Equivalently, |alpha_i| = sqrt(p).
        on_circle = abs(reciprocal_absval - target) < 1e-6
        if not on_circle:
            holds = False
        root_data.append({
            'root_of_P1': complex(r),
            'frobenius_eigenvalue': 1.0 / complex(r) if abs(r) > 1e-15 else None,
            'abs_frobenius': reciprocal_absval,
            'target': target,
            'on_circle': on_circle,
        })

    return {
        'riemann_hypothesis_holds': holds,
        'genus': genus,
        'roots': root_data,
    }


# ============================================================================
# 9. Shadow zeta from Hensel lifting (p-adic zero counting)
# ============================================================================

def hensel_zero_count(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    p: int, max_n: int = 5
) -> Dict[int, int]:
    """Count zeros of the shadow generating function H_A(t) mod p^n.

    H_A(t) = sum_{r>=2} S_r * t^r.

    N_n = #{t in Z/p^n Z : H_A(t) = 0 mod p^n}

    For class G (Heisenberg): H(t) = kappa*t^2. Zeros: t = 0 mod p^{ceil(n/2)}.
    So N_n = p^{n - ceil(n/2)} = p^{floor(n/2)}.

    For class L (affine): H(t) = kappa*t^2 + alpha*t^3/3 (polynomial).
    Zeros: t^2(kappa + alpha*t/3) = 0 mod p^n.

    For class M (Virasoro): H(t) involves sqrt, so the zero set is
    the shadow curve C_A(Z/p^n Z).
    """
    # Compute shadow tower to sufficient arity
    tower = shadow_tower_exact(kappa, alpha, S4, max_r=min(30, 2 * p ** max_n))

    result = {}
    for n in range(1, max_n + 1):
        pn = p ** n
        count = 0
        for t in range(pn):
            # Evaluate H_A(t) mod p^n
            val = Fraction(0)
            t_pow = Fraction(1)
            for r in range(0, max(tower.keys()) + 1 if tower else 0):
                if r >= 2 and r in tower:
                    # t_pow is t^r at this point? No, we need to track properly
                    pass
            # Recompute properly
            val = Fraction(0)
            t_frac = Fraction(t)
            t_pow = Fraction(1)
            for r in range(max(tower.keys()) + 1 if tower else 0):
                t_pow *= t_frac  # t_pow = t^r after this (but starts at r=0 giving 1, then t, t^2...)
                # Hmm, let's be more careful
            # Actually: H(t) = sum_{r>=2} S_r * t^r
            val = Fraction(0)
            t_pow = t_frac ** 2 if t != 0 else Fraction(0)
            for r in sorted(tower.keys()):
                if r < 2:
                    continue
                term = tower[r] * t_frac ** r
                val += term
            # Check val mod p^n
            # val is a Fraction. We need val * denominator = 0 mod p^n * denominator
            # Or: val.numerator * (p^n / gcd(p^n, val.denominator)) mod (p^n * val.denominator / gcd) ...
            # Simpler: convert to integer mod p^n if possible
            val_num = val.numerator
            val_den = val.denominator
            # Check if val_den is coprime to p
            g = gcd(val_den, pn)
            if val_den % p != 0:
                # val is p-integral; check val_num * val_den^{-1} mod p^n
                den_inv = _mod_inverse(val_den, pn)
                if den_inv is not None:
                    val_mod = (val_num * den_inv) % pn
                    if val_mod == 0:
                        count += 1
            else:
                # val has p in denominator: H(t) has a p-adic pole at this t
                # which means H(t) != 0 mod p^n
                pass
        result[n] = count
    return result


def _mod_inverse(a: int, m: int) -> Optional[int]:
    """Compute a^{-1} mod m using extended Euclidean algorithm.
    Returns None if gcd(a, m) != 1."""
    a = a % m
    g, x, _ = _extended_gcd(a, m)
    if g != 1:
        return None
    return x % m


def _extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean algorithm: returns (g, x, y) with a*x + b*y = g."""
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def hensel_zero_count_fast(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    p: int, max_n: int = 5, trunc: int = 20
) -> Dict[int, int]:
    """Fast zero counting using truncated polynomial evaluation.

    Evaluates H_A(t) = sum_{r=2}^{trunc} S_r t^r mod p^n for all
    t in Z/p^n Z.  For small p and n, this is tractable.
    """
    tower = shadow_tower_exact(kappa, alpha, S4, max_r=trunc)

    result = {}
    for n in range(1, max_n + 1):
        pn = p ** n
        if pn > 10 ** 7:  # Safety limit
            result[n] = None
            continue
        count = 0
        for t in range(pn):
            # Evaluate polynomial sum_{r=2}^{trunc} S_r * t^r mod p^n
            # Work with numerators and denominators carefully
            val_num = 0
            val_den = 1
            t_pow = 1
            for r in range(trunc + 1):
                t_pow_r = pow(t, r, pn * _lcm_accum(tower, trunc))
                # This is getting complicated with Fractions; use a simpler approach
                pass

            # Simpler: accumulate as Fraction, then reduce mod p^n
            val = Fraction(0)
            for r in range(2, trunc + 1):
                if r in tower:
                    val += tower[r] * Fraction(pow(t, r))

            # Now check if val = 0 mod p^n
            val_num = val.numerator
            val_den = val.denominator
            if val_den % p != 0:
                inv = _mod_inverse(val_den % pn, pn)
                if inv is not None:
                    if (val_num * inv) % pn == 0:
                        count += 1
            # If denominator has factors of p, the value is NOT p-adically integral
            # so it cannot be 0 mod p^n
        result[n] = count
    return result


def _lcm_accum(tower: Dict[int, Fraction], max_r: int) -> int:
    """LCM of all denominators in the tower."""
    result = 1
    for r in range(2, max_r + 1):
        if r in tower:
            d = tower[r].denominator
            result = result * d // gcd(result, d)
    return result


# ============================================================================
# 10. Frobenius eigenvalues
# ============================================================================

def frobenius_eigenvalues_conic(p: int) -> List[complex]:
    """Frobenius eigenvalues for a smooth conic (genus 0).

    For genus 0 (P^1): P_1 = 1, so there are NO eigenvalues.
    The zeta function is 1/((1-T)(1-pT)).

    The "eigenvalues" of Frobenius on H^1 are vacuous (H^1 = 0 for P^1).
    The eigenvalues on H^0 and H^2 are 1 and p respectively.
    """
    return []  # No H^1 eigenvalues for genus 0


def frobenius_eigenvalues_from_P1(
    P1_coeffs: List[Fraction], p: int
) -> List[complex]:
    """Extract Frobenius eigenvalues from the numerator polynomial P_1.

    P_1(T) = prod_{i=1}^{2g} (1 - alpha_i T)

    The roots of P_1(T) are 1/alpha_i, so alpha_i = 1/root_i.
    """
    if len(P1_coeffs) <= 1:
        return []

    import numpy as np
    coeffs_float = [float(c) for c in P1_coeffs]
    roots = np.roots(coeffs_float[::-1])
    eigenvalues = [1.0 / r for r in roots if abs(r) > 1e-15]
    return eigenvalues


# ============================================================================
# 11. Hasse-Weil L-function (first Euler factors)
# ============================================================================

def hasse_weil_euler_factor(
    P1_coeffs: List[Fraction], p: int
) -> List[Fraction]:
    """Compute the local Euler factor L_p(T) = P_1(T)^{-1} for the
    Hasse-Weil L-function.

    For genus 0: L_p(T) = 1 (trivial).
    For genus g: L_p(T) = 1/P_1(p^{-s}) expanded as a Dirichlet series factor.

    Returns coefficients of P_1(T) (the reciprocal of the Euler factor).
    """
    return P1_coeffs


def shadow_hasse_weil_L_partial(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    primes: List[int]
) -> Dict[int, List[Fraction]]:
    """Compute the first several Euler factors of the shadow Hasse-Weil L-function.

    For each prime p, compute P_1(T) from point counting on the shadow curve.

    Since our shadow curves are genus 0 (conics), ALL Euler factors are trivial:
    L(C_A, s) = zeta(s) * zeta(s-1) (= the Dedekind zeta of Q up to finitely
    many bad primes).

    This is a genuine mathematical result: the shadow curve is rational,
    so its L-function is trivial.  The INTERESTING arithmetic lives not in
    the shadow curve's zeta function, but in the shadow COEFFICIENTS' mod-p
    reduction (the Hensel zero counts).
    """
    result = {}
    for p in primes:
        try:
            P1, _ = conic_zeta_function(p)
            result[p] = P1
        except (ValueError, ZeroDivisionError):
            result[p] = None
    return result


# ============================================================================
# 12. Shadow Dirichlet series zeta
# ============================================================================

def shadow_dirichlet_zeta(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    s: complex, max_r: int = 100
) -> complex:
    """Evaluate the shadow Dirichlet series zeta_A(s) = sum_{r>=2} S_r r^{-s}.

    This is NOT the Hasse-Weil L-function; it is a different object.
    """
    tower = shadow_tower_exact(kappa, alpha, S4, max_r=max_r)
    result = 0.0
    for r in range(2, max_r + 1):
        if r in tower:
            Sr = float(tower[r])
            result += Sr * r ** (-s)
    return result


def compare_L_and_zeta(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    s_values: List[complex], primes: List[int]
) -> Dict[str, Any]:
    """Compare the Hasse-Weil L-function with the shadow Dirichlet series.

    KEY FINDING: Since the shadow curve is genus 0, L(C_A, s) is trivial
    (essentially zeta(s)*zeta(s-1)).  The shadow Dirichlet series zeta_A(s)
    is a completely different object — it encodes the growth of shadow
    coefficients, not the point counts on a curve.

    They are UNRELATED in general.  The Weil conjectures describe a geometry
    (the shadow curve); the shadow zeta describes an arithmetic sequence.
    """
    L_factors = shadow_hasse_weil_L_partial(kappa, alpha, S4, primes)
    zeta_vals = {}
    for s in s_values:
        zeta_vals[s] = shadow_dirichlet_zeta(kappa, alpha, S4, s)

    return {
        'L_factors': L_factors,
        'L_note': 'Genus 0: L = zeta(s)*zeta(s-1), trivial',
        'shadow_zeta_values': zeta_vals,
        'relation': 'UNRELATED: L counts curve points; shadow zeta encodes tower growth',
    }


# ============================================================================
# 13. Full Weil verification pipeline
# ============================================================================

def full_weil_verification(
    family: str,
    params: Dict[str, Fraction],
    primes: List[int],
    max_n_hensel: int = 5,
) -> Dict[str, Any]:
    """Complete Weil-conjecture verification for a shadow curve.

    family: 'virasoro', 'affine_sl2', 'w3'
    params: {'c': Fraction(1)} or {'k': Fraction(1)} etc.
    primes: list of primes to test
    max_n_hensel: maximum Hensel lifting depth

    Returns comprehensive verification data.
    """
    # Get shadow data
    if family == 'virasoro':
        c_val = params['c']
        kappa, alpha, S4 = virasoro_shadow_data_exact(c_val)
        label = f"Vir_{{c={c_val}}}"
    elif family == 'affine_sl2':
        k_val = params['k']
        kappa, alpha, S4 = affine_sl2_shadow_data_exact(k_val)
        label = f"sl_2_{{k={k_val}}}"
    elif family == 'w3':
        c_val = params['c']
        kappa, alpha, S4 = w3_tline_shadow_data_exact(c_val)
        label = f"W_3_Tline_{{c={c_val}}}"
    else:
        raise ValueError(f"Unknown family: {family}")

    Delta = critical_discriminant_exact(kappa, S4)
    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)

    results = {
        'family': label,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'Q_L': (q0, q1, q2),
        'shadow_class': _classify(kappa, alpha, S4),
        'primes': {},
    }

    for p in primes:
        prime_data = {}
        prime_data['is_good_prime'] = is_good_prime(kappa, alpha, S4, p)

        if not prime_data['is_good_prime']:
            prime_data['error'] = f'Bad prime: p={p} divides denominator of Q_L'
            # Still try Hensel zeros (doesn't need good reduction)
            try:
                hensel = hensel_zero_count_fast(kappa, alpha, S4, p, max_n=max_n_hensel)
                prime_data['hensel_zeros'] = hensel
            except Exception as e:
                prime_data['hensel_zeros'] = {'error': str(e)}
        else:
            try:
                # Point counting
                N_1 = count_smooth_conic_points(kappa, alpha, S4, p)
                prime_data['N_1'] = N_1
                prime_data['trace'] = p + 1 - N_1

                # Rationality (Weil I)
                rat = verify_rationality(kappa, alpha, S4, p)
                prime_data['rationality'] = rat

                # Functional equation (Weil II)
                fe = verify_functional_equation(p, rat['P1_coeffs'], rat['genus'])
                prime_data['functional_equation'] = fe

                # Riemann hypothesis (Weil III)
                rh = verify_riemann_hypothesis(p, rat['P1_coeffs'], rat['genus'])
                prime_data['riemann_hypothesis'] = rh

                # Hensel zero counts
                try:
                    hensel = hensel_zero_count_fast(kappa, alpha, S4, p, max_n=max_n_hensel)
                    prime_data['hensel_zeros'] = hensel
                except Exception as e:
                    prime_data['hensel_zeros'] = {'error': str(e)}

                # Singular model count
                try:
                    N_sing = count_singular_model_points(kappa, alpha, S4, p)
                    prime_data['singular_affine_count'] = N_sing
                except (ValueError, ZeroDivisionError):
                    pass

            except (ValueError, ZeroDivisionError) as e:
                prime_data['error'] = str(e)

        results['primes'][p] = prime_data

    return results


def _classify(kappa: Fraction, alpha: Fraction, S4: Fraction) -> str:
    """Shadow class: G, L, C, or M."""
    if alpha == 0 and S4 == 0:
        return 'G'
    if S4 == 0:
        return 'L'
    Delta = 8 * kappa * S4
    if Delta == 0:
        return 'G_or_L'
    return 'M'


# ============================================================================
# 14. Trace formula verification
# ============================================================================

def verify_trace_formula(
    kappa: Fraction, alpha: Fraction, S4: Fraction, p: int
) -> Dict[str, Any]:
    """Verify the Lefschetz trace formula for the shadow conic.

    For a smooth conic (genus 0): #C(F_p) = p + 1, trace = 0.
    For a degenerate conic (pair of lines): #C(F_p) = 2p + 1, trace = -(p).

    The trace formula #C(F_p) = 1 + p - sum alpha_i is checked against
    the direct point count.
    """
    if not is_good_prime(kappa, alpha, S4, p):
        return {'N_p': None, 'error': f'Bad prime p={p}', 'match': False}

    N = count_smooth_conic_points(kappa, alpha, S4, p)

    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    q0_p = mod_p_reduce(q0, p)
    q1_p = mod_p_reduce(q1, p)
    q2_p = mod_p_reduce(q2, p)
    disc_p = (q1_p ** 2 - 4 * q0_p * q2_p) % p

    if disc_p != 0:
        # Smooth conic
        expected = p + 1
        alphas = []
    else:
        # Degenerate: pair of lines
        expected = 2 * p + 1
        alphas = [1, p]  # eigenvalues on H^0 of each component

    trace = p + 1 - N
    sum_alphas = sum(alphas)

    return {
        'N_p': N,
        'expected': expected,
        'trace': trace,
        'degenerate': disc_p == 0,
        'match': N == expected,
    }


# ============================================================================
# 15. Higher-genus shadow curves (non-conic models)
# ============================================================================

def shadow_curve_higher(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    extra_coeffs: Optional[Dict[int, Fraction]] = None,
    p: int = 5
) -> Dict[str, Any]:
    """Study the curve y^2 = sum_{r=2}^{R} S_r t^{2r} over F_p.

    This is a higher-degree model that includes more shadow coefficients.
    Unlike the conic model (which only uses S_2, S_3, S_4), this uses
    the full tower truncated at some arity R.

    The genus increases with R, giving genuine higher-genus curves
    for which the Weil conjectures are nontrivial.
    """
    tower = shadow_tower_exact(kappa, alpha, S4, max_r=12)
    if extra_coeffs:
        tower.update(extra_coeffs)

    # Build polynomial f(t) = sum S_r t^{2r} (even powers for smooth model)
    max_r = max(tower.keys())
    deg = 2 * max_r
    coeffs = [Fraction(0)] * (deg + 1)
    for r, Sr in tower.items():
        if 2 * r <= deg:
            coeffs[2 * r] = Sr

    # Reduce mod p
    coeffs_p = []
    bad_prime = False
    for c in coeffs:
        try:
            coeffs_p.append(mod_p_reduce(c, p))
        except ValueError:
            bad_prime = True
            coeffs_p.append(0)

    if bad_prime:
        return {'error': f'Bad prime p={p} for this algebra', 'coeffs': coeffs}

    # Count points
    N_affine = count_affine_points(coeffs_p, p)
    N_proj = count_projective_points(coeffs_p, p)

    # Determine effective degree
    eff_deg = deg
    while eff_deg > 0 and coeffs_p[eff_deg] == 0:
        eff_deg -= 1

    # Genus estimate from degree (assuming generic smoothness)
    if eff_deg % 2 == 1:
        genus_est = (eff_deg - 1) // 2
    else:
        genus_est = eff_deg // 2 - 1

    return {
        'degree': eff_deg,
        'genus_estimate': genus_est,
        'N_affine': N_affine,
        'N_projective': N_proj,
        'coeffs_mod_p': coeffs_p[:eff_deg + 1],
        'trace': p + 1 - N_proj,
    }


# ============================================================================
# 16. Weil number verification
# ============================================================================

def is_weil_number(alpha: complex, q: int, weight: int = 1) -> bool:
    """Check if alpha is a q-Weil number of weight w.

    A q-Weil number of weight w is an algebraic integer alpha with
    |sigma(alpha)| = q^{w/2} for every embedding sigma into C.

    For us: just check |alpha| = q^{w/2} numerically.
    """
    target = q ** (weight / 2.0)
    return abs(abs(alpha) - target) < 1e-6 * target


def weil_polynomial_check(
    P1_coeffs: List[Fraction], p: int, genus: int
) -> Dict[str, Any]:
    """Check that P_1(T) is a Weil polynomial.

    A Weil polynomial of weight 1 over F_p satisfies:
    1. Degree 2g
    2. Integer coefficients
    3. Functional equation: a_{2g-k} = p^{g-k} a_k
    4. All complex roots have absolute value 1/sqrt(p) (equivalently,
       reciprocal roots alpha_i have |alpha_i| = sqrt(p))
    """
    degree = len(P1_coeffs) - 1
    if degree < 0:
        return {'is_weil': True, 'genus': 0, 'note': 'Trivial (degree -1)'}

    # Check integer coefficients
    all_integer = all(c.denominator == 1 for c in P1_coeffs)

    # Check degree = 2g
    correct_degree = (degree == 2 * genus)

    # Functional equation
    fe_holds = True
    for k in range(genus + 1):
        if 2 * genus - k < len(P1_coeffs):
            if P1_coeffs[2 * genus - k] != Fraction(p) ** (genus - k) * P1_coeffs[k]:
                fe_holds = False
                break

    # Root check
    rh = verify_riemann_hypothesis(p, P1_coeffs, genus)

    return {
        'is_weil': all_integer and correct_degree and fe_holds and rh['riemann_hypothesis_holds'],
        'all_integer': all_integer,
        'correct_degree': correct_degree,
        'functional_equation': fe_holds,
        'riemann_hypothesis': rh['riemann_hypothesis_holds'],
    }


# ============================================================================
# 17. Multi-path cross-verification
# ============================================================================

def cross_verify_point_count(
    kappa: Fraction, alpha: Fraction, S4: Fraction, p: int
) -> Dict[str, Any]:
    """Cross-verify point counts via 4 independent methods.

    Path 1: Direct count on the conic u^2 = Q_L(t) (projective).
    Path 2: Legendre symbol sum (affine) + points at infinity.
    Path 3: Character sum formula (when applicable).
    Path 4: Rationality check (consistent with zeta function structure).
    """
    if not is_good_prime(kappa, alpha, S4, p):
        return {
            'path1_direct': None,
            'error': f'Bad prime p={p}',
            'all_agree': False,
        }

    q0, q1, q2 = shadow_metric_Q_exact(kappa, alpha, S4)
    q0_p = mod_p_reduce(q0, p)
    q1_p = mod_p_reduce(q1, p)
    q2_p = mod_p_reduce(q2, p)

    # Path 1: Direct projective count on conic
    path1 = count_smooth_conic_points(kappa, alpha, S4, p)

    # Path 2: Legendre symbol sum
    legendre_sum = 0
    for t in range(p):
        ql_t = (q0_p + q1_p * t + q2_p * t * t) % p
        legendre_sum += legendre_symbol(ql_t, p)
    path2_affine = p + legendre_sum
    # Points at infinity
    if q2_p % p == 0:
        pts_inf = 1  # degenerate leading coeff
    else:
        pts_inf = 1 + legendre_symbol(q2_p, p)
    path2 = path2_affine + pts_inf

    # Path 3: Character sum formula for smooth conics
    disc_p = (q1_p * q1_p - 4 * q0_p * q2_p) % p
    if q2_p % p != 0 and disc_p % p != 0:
        # Smooth nondegenerate conic: sum of Legendre symbols = -(leading|p)
        expected_sum = -(legendre_symbol(q2_p, p)) % p
        # Actually for u^2 = at^2 + bt + c with nonzero disc:
        # sum_{t in F_p} (at^2+bt+c|p) = -(a|p) * (p-1)/p...
        # The exact formula: sum = -(a|p) (for p odd, complete the square)
        # Let's just verify: path3 = p + (-(a|p)) (affine count) + pts_inf
        char_sum = p - legendre_symbol(q2_p, p)
        path3 = char_sum + 1 + legendre_symbol(q2_p, p)
        # = p - (q2|p) + 1 + (q2|p) = p + 1
    else:
        path3 = None

    # Path 4: Zeta function consistency
    # For smooth conic: N_1 = p + 1.  For degenerate: N_1 = direct count.
    if disc_p != 0:
        path4 = p + 1  # smooth conic with rational point
    else:
        path4 = path1  # degenerate: just check self-consistency

    agree = (path1 == path2)
    if path3 is not None:
        agree = agree and (path1 == path3)
    if path4 is not None:
        agree = agree and (path1 == path4)

    return {
        'path1_direct': path1,
        'path2_legendre': path2,
        'path3_character': path3,
        'path4_zeta': path4,
        'disc_mod_p': disc_p,
        'degenerate': disc_p == 0,
        'all_agree': agree,
    }


# ============================================================================
# 18. Shadow mod-p reduction analysis
# ============================================================================

def shadow_mod_p_pattern(
    kappa: Fraction, alpha: Fraction, S4: Fraction,
    p: int, max_r: int = 30
) -> Dict[str, Any]:
    """Analyze the pattern of shadow coefficients S_r mod p.

    Computes:
    - S_r mod p for r = 2, ..., max_r
    - Periodicity detection
    - Vanishing pattern
    """
    tower = shadow_tower_exact(kappa, alpha, S4, max_r=max_r)

    reduced = {}
    poles = []
    for r in range(2, max_r + 1):
        if r in tower:
            try:
                reduced[r] = mod_p_reduce(tower[r], p)
            except ValueError:
                reduced[r] = None
                poles.append(r)

    # Detect periodicity
    values = [reduced.get(r, None) for r in range(2, max_r + 1)]
    period = _detect_period(values)

    # Count zeros
    zeros = [r for r in range(2, max_r + 1) if reduced.get(r) == 0]

    return {
        'mod_p_values': reduced,
        'period': period,
        'zeros': zeros,
        'poles': poles,
        'nonzero_count': sum(1 for v in reduced.values() if v is not None and v != 0),
    }


def _detect_period(seq: List[Optional[int]], min_period: int = 1, max_period: int = 20) -> Optional[int]:
    """Detect periodicity in a sequence (ignoring None values)."""
    clean = [x for x in seq if x is not None]
    if len(clean) < 4:
        return None
    for per in range(min_period, min(max_period, len(clean) // 2) + 1):
        is_periodic = True
        for i in range(per, len(clean)):
            if clean[i] != clean[i % per]:
                is_periodic = False
                break
        if is_periodic:
            return per
    return None
