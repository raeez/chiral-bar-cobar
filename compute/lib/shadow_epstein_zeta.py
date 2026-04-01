#!/usr/bin/env python3
r"""
shadow_epstein_zeta.py -- The Epstein zeta function of the shadow metric.

THE CONSTRUCTION:

The shadow metric Q_L(t) = 4kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2
is a quadratic polynomial in the arity parameter t, determined by three
OPE invariants: kappa (modular characteristic), alpha (cubic shadow),
S4 (quartic contact invariant).

Homogenizing Q_L to a BINARY QUADRATIC FORM in variables (m, n):

    Q(m,n) = 4*kappa^2 * m^2 + 12*kappa*alpha * m*n + (9*alpha^2 + 2*Delta) * n^2

where Delta = 8*kappa*S4 is the critical discriminant.

The discriminant of this binary form is:

    disc(Q) = (12*kappa*alpha)^2 - 4*(4*kappa^2)*(9*alpha^2 + 2*Delta) = -32*kappa^2*Delta

For Virasoro at central charge c:
    kappa = c/2, alpha = 2, S4 = 10/(c*(5c+22)), Delta = 40/(5c+22)
    disc(Q) = -320*c^2/(5c+22)

The EPSTEIN ZETA FUNCTION of Q is:

    eps_Q(s) = sum'_{(m,n) in Z^2} Q(m,n)^{-s}

This converges for Re(s) > 1. By Epstein (1903), it has meromorphic
continuation to all of C with a SINGLE simple pole at s = 1 (residue
= 2*pi / sqrt(|disc(Q)|)), and satisfies the FUNCTIONAL EQUATION:

    Xi_Q(s) = Xi_Q(1-s)

where the completed function is:

    Xi_Q(s) = (|disc|/4)^{s/2} * pi^{-s} * Gamma(s) * eps_Q(s)

Here |disc|/4 is Epstein's discriminant D_E = a*c - (b/2)^2 for the
form Q(m,n) = a*m^2 + b*m*n + c*n^2.

ANALYTIC CONTINUATION:

The Epstein zeta eps_Q(s) is computed via the Mellin transform of
the theta function theta_Q(t) = sum_{(m,n)} exp(-pi*t*Q(m,n)), with
the standard splitting trick at t = 1 using Poisson summation. This
gives a representation valid for ALL s (away from the pole at s = 1).

ARITHMETIC CONTENT:

The discriminant disc(Q) = -320*c^2/(5c+22) determines a quadratic
field K = Q(sqrt(d)) where d is the squarefree part of the integer
obtained by clearing denominators. The Epstein zeta decomposes as:

    eps_Q(s) = (2/w) * sum_{chi in Cl(d)^} chi(cl(Q)) * L(s, chi)

For class number h(d) = 1: eps_Q(s) is proportional to zeta_K(s).
For h(d) > 1: eps_Q depends on the specific ideal class selected
by the shadow metric. This is new arithmetic content.

Manuscript references:
    def:shadow-metric (higher_genus_modular_koszul.tex)
    eq:shadow-metric (standalone/riccati.tex)
    eq:critical-discriminant (standalone/riccati.tex)
"""

from fractions import Fraction
from typing import Dict, List, Optional, Tuple, Union
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ================================================================
# 1. Shadow metric data for standard families
# ================================================================

def virasoro_shadow_data(c):
    r"""Shadow data (kappa, alpha, S4, Delta) for Virasoro at central charge c.

    kappa = c/2, alpha = 2, S4 = 10/(c*(5c+22)), Delta = 40/(5c+22).
    """
    if isinstance(c, Fraction):
        kappa = c / 2
        alpha = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        Delta = Fraction(40) / (5 * c + 22)
    else:
        c_f = float(c)
        kappa = c_f / 2.0
        alpha = 2.0
        S4 = 10.0 / (c_f * (5 * c_f + 22))
        Delta = 40.0 / (5 * c_f + 22)
    return {'kappa': kappa, 'alpha': alpha, 'S4': S4, 'Delta': Delta}


def minimal_model_c(m):
    r"""Central charge c = 1 - 6/(m(m+1)) for M(m, m+1)."""
    return Fraction(1) - Fraction(6, m * (m + 1))


def binary_quadratic_form(kappa, alpha, S4):
    r"""Binary quadratic form Q(m,n) = a*m^2 + b*m*n + c*n^2 from shadow data.

    Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2
    Homogenizing t = n/m:
        Q(m,n) = 4*kappa^2*m^2 + 12*kappa*alpha*m*n + (9*alpha^2 + 16*kappa*S4)*n^2

    Returns (a, b, c_coeff).
    """
    a = 4 * kappa ** 2
    b = 12 * kappa * alpha
    c_coeff = 9 * alpha ** 2 + 16 * kappa * S4
    return a, b, c_coeff


def quadratic_form_discriminant(a, b, c):
    r"""Discriminant D = b^2 - 4ac of am^2 + bmn + cn^2."""
    return b ** 2 - 4 * a * c


def virasoro_discriminant(c_val):
    r"""Discriminant of the Virasoro shadow metric: disc = -320c^2/(5c+22)."""
    if isinstance(c_val, Fraction):
        return Fraction(-320) * c_val ** 2 / (5 * c_val + 22)
    return -320.0 * float(c_val) ** 2 / (5 * float(c_val) + 22)


def virasoro_form(c_val):
    r"""Binary form from Virasoro shadow metric at c. Returns (a, b, c, disc)."""
    c_f = float(c_val)
    data = virasoro_shadow_data(c_f)
    a, b, cc = binary_quadratic_form(data['kappa'], data['alpha'], data['S4'])
    D = quadratic_form_discriminant(a, b, cc)
    return a, b, cc, D


# ================================================================
# 2. Theta function and Epstein zeta by Mellin-splitting
# ================================================================

def theta_binary_form(t, a_c, b_c, c_c, N=25):
    r"""theta(t) = sum_{(m,n) in Z^2} exp(-pi*t*Q(m,n)).

    Q(m,n) = a_c*m^2 + b_c*m*n + c_c*n^2.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    result = mpmath.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            Q = a_c * m * m + b_c * m * n + c_c * n * n
            result += mpmath.exp(-mpmath.pi * t * Q)
    return result


def _dual_form_coefficients(a_c, b_c, c_c):
    r"""Dual (adjoint) form Q^*(m,n) = (4/|D|)(c*m^2 - b*mn + a*n^2).

    Where D = b^2 - 4ac is the discriminant.
    Returns (a*, b*, c*) for the dual form.
    """
    D = b_c ** 2 - 4 * a_c * c_c
    abs_D = abs(D)
    DE = abs_D / 4.0  # Epstein's discriminant
    a_star = float(c_c) / DE
    b_star = -float(b_c) / DE
    c_star = float(a_c) / DE
    return a_star, b_star, c_star


def epstein_phi(s_val, a_c, b_c, c_c, N_theta=25):
    r"""Compute phi(s) = pi^{-s} * Gamma(s) * eps_Q(s) via theta splitting.

    Uses the Mellin transform of theta_Q with the standard splitting at t=1
    and Poisson summation for the t < 1 part. This gives analytic continuation
    to all s (away from the pole at s = 1).

    The Epstein zeta itself is recovered as:
        eps_Q(s) = pi^s / Gamma(s) * phi(s)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpf(s_val) if isinstance(s_val, (int, float)) else mpmath.mpc(s_val)

    D = b_c ** 2 - 4 * a_c * c_c
    abs_D = abs(D)
    DE = mpmath.mpf(abs_D) / 4
    factor = 1 / mpmath.sqrt(DE)  # = sqrt(4/|D|) = 2/sqrt(|D|)

    a_star, b_star, c_star = _dual_form_coefficients(a_c, b_c, c_c)

    def integrand_s(t):
        th = theta_binary_form(t, a_c, b_c, c_c, N_theta)
        return (th - 1) * mpmath.power(t, s_mp - 1)

    def integrand_dual(t):
        th = theta_binary_form(t, a_star, b_star, c_star, N_theta)
        return (th - 1) * mpmath.power(t, -s_mp)

    # Integrals from 1 to T (theta decays exponentially, T=10 is sufficient)
    I_s = mpmath.quad(integrand_s, [1, 10], maxdegree=8)
    I_dual = mpmath.quad(integrand_dual, [1, 10], maxdegree=8)

    # Pole terms from splitting
    R = factor / (s_mp - 1) - 1 / s_mp

    return I_s + factor * I_dual + R


def epstein_zeta(s_val, a_c, b_c, c_c, N_theta=25):
    r"""Epstein zeta eps_Q(s) = sum'_{(m,n)} Q(m,n)^{-s}.

    Valid for all s via analytic continuation (theta splitting).
    Has a simple pole at s = 1.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpf(s_val) if isinstance(s_val, (int, float)) else mpmath.mpc(s_val)
    phi = epstein_phi(s_val, a_c, b_c, c_c, N_theta)
    return mpmath.power(mpmath.pi, s_mp) / mpmath.gamma(s_mp) * phi


def epstein_zeta_lattice_sum(s, a, b, c_coeff, N=100):
    r"""Epstein zeta by direct lattice sum. Converges only for Re(s) > 1."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    result = mpmath.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            Q_mn = a * m ** 2 + b * m * n + c_coeff * n ** 2
            if Q_mn > 0:
                result += mpmath.power(mpmath.mpf(Q_mn), -s_mp)
    return complex(result)


def epstein_zeta_virasoro(s, c_val, N_theta=25):
    r"""Epstein zeta of the Virasoro shadow metric at central charge c."""
    a, b, cc, D = virasoro_form(c_val)
    return complex(epstein_zeta(s, a, b, cc, N_theta))


# ================================================================
# 3. Completed Epstein zeta and functional equation
# ================================================================

def completed_epstein(s_val, a_c, b_c, c_c, N_theta=25):
    r"""Completed Epstein zeta:

    Xi_Q(s) = D_E^{s/2} * pi^{-s} * Gamma(s) * eps_Q(s)
            = D_E^{s/2} * phi(s)

    where D_E = |disc(Q)|/4 is Epstein's discriminant.
    Satisfies Xi_Q(s) = Xi_Q(1-s) when the form is equivalent to its dual
    (always true for class number 1, or for the principal form).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpf(s_val) if isinstance(s_val, (int, float)) else mpmath.mpc(s_val)
    D = b_c ** 2 - 4 * a_c * c_c
    DE = abs(D) / 4.0
    phi = epstein_phi(s_val, a_c, b_c, c_c, N_theta)
    return mpmath.power(DE, s_mp / 2) * phi


def completed_epstein_virasoro(s, c_val, N_theta=25):
    r"""Completed Epstein zeta for the Virasoro shadow metric."""
    a, b, cc, D = virasoro_form(c_val)
    return complex(completed_epstein(s, a, b, cc, N_theta))


def functional_equation_test(s_val, a_c, b_c, c_c, N_theta=25):
    r"""Test Xi_Q(s) = Xi_Q(1-s). Returns relative error."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    Xi_s = completed_epstein(s_val, a_c, b_c, c_c, N_theta)
    Xi_1s = completed_epstein(1 - s_val, a_c, b_c, c_c, N_theta)
    denom = max(abs(Xi_s), abs(Xi_1s), mpmath.mpf('1e-300'))
    rel_err = float(abs(Xi_s - Xi_1s) / denom)
    return {
        's': s_val,
        'Xi_s': complex(Xi_s),
        'Xi_1ms': complex(Xi_1s),
        'rel_err': rel_err,
        'passes': rel_err < 0.001,
    }


# ================================================================
# 4. Number-theoretic utilities
# ================================================================

def squarefree_part(n):
    r"""Squarefree part of n."""
    if n == 0:
        return 0
    sign = 1 if n > 0 else -1
    n = abs(n)
    result = 1
    d = 2
    while d * d <= n:
        count = 0
        while n % d == 0:
            n //= d
            count += 1
        if count % 2 == 1:
            result *= d
        d += 1
    result *= n
    return sign * result


def _is_fundamental_discriminant(d):
    r"""Check if d is a fundamental discriminant."""
    if d == 0 or d == 1:
        return False
    if d % 4 == 1:
        return squarefree_part(d) == d
    elif d % 4 == 0:
        m = d // 4
        return (m % 4 in (2, 3)) and squarefree_part(m) == m
    return False


def fundamental_discriminant(D):
    r"""Given D < 0, find (d, f) with D = d*f^2, d fundamental."""
    if D >= 0:
        raise ValueError(f"Expected D < 0, got {D}")
    abs_D = abs(D)
    f = 1
    while f * f <= abs_D:
        if abs_D % (f * f) == 0:
            d_cand = D // (f * f)
            if _is_fundamental_discriminant(d_cand):
                return d_cand, f
        f += 1
    return D, 1


def class_number_small(d):
    r"""Class number h(d) for small negative fundamental discriminants."""
    if d >= 0 or not _is_fundamental_discriminant(d):
        raise ValueError(f"{d} is not a negative fundamental discriminant")
    abs_d = abs(d)
    bound = int(math.sqrt(abs_d / 3.0)) + 1
    count = 0
    for a in range(1, bound + 1):
        for b in range(-a, a + 1):
            num = b * b - d
            if num % (4 * a) != 0:
                continue
            c = num // (4 * a)
            if c < a:
                continue
            if abs(b) > a:
                continue
            if abs(b) == a or a == c:
                if b < 0:
                    continue
            count += 1
    return count


def roots_of_unity(d):
    r"""Number of roots of unity w in Q(sqrt(d))."""
    if d == -3:
        return 6
    elif d == -4:
        return 4
    return 2


# ================================================================
# 5. Dirichlet L-functions
# ================================================================

def _jacobi_symbol(a, n):
    r"""Jacobi symbol (a/n) for odd n > 0."""
    if n <= 0 or n % 2 == 0:
        raise ValueError(f"n must be odd positive, got {n}")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0


def kronecker_symbol(d, n):
    r"""Kronecker symbol (d/n)."""
    if n == 0:
        return 1 if abs(d) == 1 else 0
    if n == 1:
        return 1
    if n < 0:
        n = -n
        if d < 0:
            return -kronecker_symbol(d, n)
        return kronecker_symbol(d, n)
    result = 1
    # Factor of 2
    while n % 2 == 0:
        n //= 2
        if d % 2 == 0:
            return 0
        d8 = d % 8
        if d8 == 3 or d8 == 5:
            result *= -1
    if n > 1:
        result *= _jacobi_symbol(d, n)
    return result


def dirichlet_l_function(s, d, n_terms=10000):
    r"""L(s, chi_d) = sum_{n>=1} chi_d(n) * n^{-s}."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    result = mpmath.mpf(0)
    for n in range(1, n_terms + 1):
        chi = kronecker_symbol(d, n)
        if chi != 0:
            result += chi * mpmath.power(n, -s_mp)
    return complex(result)


def dedekind_zeta(s, d, n_terms=10000):
    r"""Dedekind zeta zeta_K(s) = zeta(s) * L(s, chi_d) for K = Q(sqrt(d))."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    return complex(mpmath.zeta(s_mp)) * dirichlet_l_function(s, d, n_terms)


# ================================================================
# 6. Scaled integer form for number-theoretic operations
# ================================================================

def scaled_integer_form(m):
    r"""Scale the shadow metric to integer coefficients.

    Returns (A, B, C, scale) where scale*Q(m,n) = A*m^2+B*mn+C*n^2.
    """
    c = minimal_model_c(m)
    data = virasoro_shadow_data(c)
    a_frac, b_frac, c_frac = binary_quadratic_form(
        data['kappa'], data['alpha'], data['S4'])

    def to_frac(x):
        return x if isinstance(x, Fraction) else Fraction(x).limit_denominator(10 ** 15)

    af, bf, cf = to_frac(a_frac), to_frac(b_frac), to_frac(c_frac)

    from math import gcd
    def lcm(x, y):
        return x * y // gcd(x, y)

    lcd = lcm(af.denominator, lcm(bf.denominator, cf.denominator))
    A = int(af * lcd)
    B = int(bf * lcd)
    C = int(cf * lcd)
    return A, B, C, int(lcd)


def quadratic_field_from_disc(c_val):
    r"""Determine the quadratic field Q(sqrt(d)) from disc(Q).

    disc(Q) = p/q in lowest terms.
    As an element of Q*/Q*^2: disc ~ p*q (mod squares).
    The field is Q(sqrt(sqfree(p*q))).
    """
    if isinstance(c_val, Fraction):
        disc = virasoro_discriminant(c_val)
    else:
        disc = Fraction(virasoro_discriminant(c_val)).limit_denominator(10 ** 15)

    p, q = disc.numerator, disc.denominator
    pq = p * q
    sf = squarefree_part(pq)
    fund_disc = sf if sf % 4 == 1 else 4 * sf

    try:
        h = class_number_small(fund_disc)
    except Exception:
        h = None
    w = roots_of_unity(fund_disc)

    return {
        'disc_rational': disc,
        'pq': pq,
        'squarefree': sf,
        'fund_disc': fund_disc,
        'class_number': h,
        'roots_of_unity': w,
    }


# ================================================================
# 7. Minimal model analysis
# ================================================================

def minimal_model_epstein_data(m):
    r"""Complete Epstein zeta data for M(m, m+1)."""
    c = minimal_model_c(m)
    c_f = float(c)
    data = virasoro_shadow_data(c)
    a, b, cc = binary_quadratic_form(data['kappa'], data['alpha'], data['S4'])
    disc = quadratic_form_discriminant(a, b, cc)

    field_data = quadratic_field_from_disc(c)

    return {
        'm': m,
        'c': c,
        'c_float': c_f,
        'kappa': data['kappa'],
        'alpha': data['alpha'],
        'S4': data['S4'],
        'Delta': data['Delta'],
        'form_a': a,
        'form_b': b,
        'form_c': cc,
        'disc': disc,
        'disc_float': float(disc),
        'field_data': field_data,
    }


def verify_functional_equation_virasoro(c_val, s_test=None, N_theta=20):
    r"""Verify Xi_Q(s) = Xi_Q(1-s) for the Virasoro shadow metric at c."""
    if s_test is None:
        s_test = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

    a, b, cc, D = virasoro_form(c_val)
    results = []
    for s in s_test:
        result = functional_equation_test(s, a, b, cc, N_theta)
        result['c'] = float(c_val)
        results.append(result)
    return results


# ================================================================
# 8. Full analysis
# ================================================================

def full_analysis(c_val, label='', N_theta=20):
    r"""Complete Epstein zeta analysis for Virasoro at c."""
    c_f = float(c_val)
    a, b, cc, D = virasoro_form(c_f)

    result = {
        'label': label,
        'c': c_f,
        'kappa': c_f / 2,
        'alpha': 2.0,
        'S4': 10.0 / (c_f * (5 * c_f + 22)),
        'Delta': 40.0 / (5 * c_f + 22),
        'form': (a, b, cc),
        'disc': D,
    }

    if isinstance(c_val, Fraction):
        field_data = quadratic_field_from_disc(c_val)
        result['field_data'] = field_data
        h = field_data['class_number']
        fd = field_data['fund_disc']
        w = field_data['roots_of_unity']

        if h == 1:
            result['l_function'] = f'L(s, chi_{fd})'
        elif h is not None:
            result['l_function'] = f'Hecke decomposition (h={h})'

    if HAS_MPMATH:
        fe = verify_functional_equation_virasoro(c_f, N_theta=N_theta)
        result['functional_equation'] = fe
        result['fe_all_pass'] = all(r['passes'] for r in fe)

    return result


# ================================================================
# 9. Deeper L-function investigation
# ================================================================

def deeper_l_function_investigation():
    r"""For each minimal model, determine class number and L-function content.

    When h = 1: L-function is L(s, chi_d), a standard Dirichlet L-function.
    When h > 1: the Epstein zeta depends on the ideal class selected by the
    shadow metric, giving FINER arithmetic data via Hecke characters.
    """
    results = []
    for m in range(3, 21):
        data = minimal_model_epstein_data(m)
        fd = data['field_data']
        results.append({
            'm': m,
            'c': str(data['c']),
            'fund_disc': fd['fund_disc'],
            'class_number': fd['class_number'],
            'roots_of_unity': fd['roots_of_unity'],
            'squarefree': fd['squarefree'],
        })

    h1 = [r for r in results if r['class_number'] == 1]
    h_gt_1 = [r for r in results if isinstance(r['class_number'], int)
              and r['class_number'] > 1]

    return {
        'models': results,
        'h1_count': len(h1),
        'h_gt_1_count': len(h_gt_1),
        'h1_models': [(r['m'], r['fund_disc']) for r in h1],
        'h_gt_1_models': [(r['m'], r['class_number'], r['fund_disc'])
                          for r in h_gt_1],
    }


if __name__ == '__main__':
    print("Shadow Epstein Zeta: Minimal Model Survey")
    print("=" * 60)

    for m in range(3, 13):
        data = minimal_model_epstein_data(m)
        fd = data['field_data']
        print(f"\nM({m},{m + 1}): c = {data['c']}")
        print(f"  disc = {data['disc']}")
        print(f"  Q(sqrt({fd['squarefree']})), fund disc = {fd['fund_disc']}")
        print(f"  h = {fd['class_number']}, w = {fd['roots_of_unity']}")

    if HAS_MPMATH:
        print("\n" + "=" * 60)
        print("Functional Equation Verification")
        for m in [3, 5, 9]:
            c = minimal_model_c(m)
            results = verify_functional_equation_virasoro(float(c))
            print(f"\nM({m},{m + 1}): c = {c}")
            for r in results:
                status = "PASS" if r['passes'] else "FAIL"
                print(f"  s={r['s']:.1f}: rel_err={r['rel_err']:.2e} {status}")
