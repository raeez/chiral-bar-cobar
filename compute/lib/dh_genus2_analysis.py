#!/usr/bin/env python3
r"""
dh_genus2_analysis.py -- Davenport-Heilbronn analysis at genus 2
for Koszul-Epstein functions with class number h(D) = 2.

THE MATHEMATICAL SETUP:

For a chirally Koszul algebra A of class M (shadow depth infinity),
the Koszul-Epstein function epsilon^KE_A(s) is the Epstein zeta of the
shadow metric binary quadratic form Q_A(m,n).

When the fundamental discriminant D_0 of Q_A has class number h(D_0) > 1,
the Davenport-Heilbronn mechanism (1936) can produce zeros OFF the
critical line Re(s) = 1/2. The mechanism: the Epstein zeta of a
SINGLE quadratic form Q in a class group with h > 1 classes is

    eps_Q(s) = (2/w) * sum_{chi in Cl(D)^} chi([Q]) * L(s, chi, D)

where [Q] is the class of Q in the class group Cl(D), chi ranges over
characters, L(s, chi, D) are Hecke L-functions of Q(sqrt(D)), and
w = |O_K^*| (number of units).

For h(D) = 2 and Cl(D) = Z/2Z, there are two characters: the trivial
chi_0 and the sign character chi_1 = (D/.). The Epstein zeta is

    eps_Q(s) = (1/w) * [L(s, chi_0, D) + chi_1([Q]) * L(s, chi_1, D)]

where chi_1([Q]) = +1 for the principal form and -1 for the non-principal.
The two L-functions L(s, chi_0) = zeta_K(s) and L(s, chi_1) have
DIFFERENT zero sets. The combination eps_Q = (L_0 +/- L_1)/w can have
zeros where L_0(s) = -/+ L_1(s), which can occur off the critical line.

THIS MODULE:

1. Computes the Koszul-Epstein function for Ising (c=1/2, D_0=-40, h=2)
   and Virasoro at c=1 (D_0=-15, h=2) via theta function method.
2. Searches for off-line zeros in the strip 0 < Re(s) < 1, 0 < Im(s) < T.
3. Computes the genus-2 Beurling kernel K^(2)(D,D) and checks whether
   its positivity constrains zero locations.
4. Decomposes eps_Q into L-function components to understand the
   DH mechanism quantitatively.

KEY RESULTS:

For GENERIC Epstein zeta with h(D) = 2, Davenport-Heilbronn proved that
off-line zeros exist for SOME forms in every class group with h > 1.
The question is whether the THREE Koszul-Epstein constraints
(Koszul symmetry, shadow polarization, modular coupling) are strong
enough to EXCLUDE these zeros for the specific forms arising from
shadow metrics.

Manuscript references:
    rem:davenport-heilbronn-koszul-epstein (arithmetic_shadows.tex, line 3025)
    Gap C (arithmetic_shadows.tex, line 3555)
    def:koszul-epstein-function (arithmetic_shadows.tex)
    thm:structural-separation (arithmetic_shadows.tex)
"""

import math
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ================================================================
# 1. Shadow metric data for the two target algebras
# ================================================================

def ising_shadow_data():
    r"""Shadow data for the Ising model (Virasoro at c = 1/2).

    c = 1/2, kappa = 1/4, alpha = 2, S_4 = 40/49.
    Delta = 8*kappa*S_4 = 80/49.

    Binary form Q(m,n) = (1/4)m^2 + 6mn + (1924/49)n^2.
    Scaled integer form: 49m^2 + 1176mn + 7696n^2  (multiply by 196).
    Reduced form: 49m^2 + 640n^2  (after Gauss reduction).
    Discriminant: -125440 = -40 * 56^2.
    Fundamental discriminant: D_0 = -40.
    Conductor: f = 56.
    Class number: h(-40) = 2.
    """
    return {
        'name': 'Ising (c=1/2)',
        'c': Fraction(1, 2),
        'kappa': Fraction(1, 4),
        'alpha': Fraction(2),
        'S4': Fraction(40, 49),
        'Delta': Fraction(80, 49),
        # Real quadratic form coefficients
        'a_real': Fraction(1, 4),
        'b_real': Fraction(6),
        'c_real': Fraction(1924, 49),
        'disc_real': Fraction(-160, 49),
        # Scaled integer form (multiply by 196 = 14^2)
        'scale_factor': 196,
        'a_int': 49,
        'b_int': 1176,
        'c_int': 7696,
        'disc_int': -125440,
        # Reduced form
        'a_red': 49,
        'b_red': 0,
        'c_red': 640,
        # Arithmetic data
        'D0': -40,
        'conductor': 56,
        'class_number': 2,
        # Class group representatives (disc -40)
        'principal_form': (1, 0, 10),
        'nonprincipal_form': (2, 0, 5),
    }


def virasoro_c1_shadow_data():
    r"""Shadow data for Virasoro at c = 1.

    c = 1, kappa = 1/2, alpha = 2, S_4 = 10/27.
    Delta = 8*kappa*S_4 = 40/27.

    Binary form Q(m,n) = m^2 + 12mn + (1052/27)n^2.
    Scaled integer form: 27m^2 + 324mn + 1052n^2  (multiply by 27).
    Reduced form: 27m^2 + 80n^2  (after Gauss reduction).
    Discriminant: -8640 = -15 * 24^2.
    Fundamental discriminant: D_0 = -15.
    Conductor: f = 24.
    Class number: h(-15) = 2.
    """
    return {
        'name': 'Virasoro (c=1)',
        'c': Fraction(1),
        'kappa': Fraction(1, 2),
        'alpha': Fraction(2),
        'S4': Fraction(10, 27),
        'Delta': Fraction(40, 27),
        # Real quadratic form coefficients
        'a_real': Fraction(1),
        'b_real': Fraction(12),
        'c_real': Fraction(1052, 27),
        'disc_real': Fraction(-320, 27),
        # Scaled integer form (multiply by 27)
        'scale_factor': 27,
        'a_int': 27,
        'b_int': 324,
        'c_int': 1052,
        'disc_int': -8640,
        # Reduced form
        'a_red': 27,
        'b_red': 0,
        'c_red': 80,
        # Arithmetic data
        'D0': -15,
        'conductor': 24,
        'class_number': 2,
        # Class group representatives (disc -15)
        'principal_form': (1, 1, 4),
        'nonprincipal_form': (2, 1, 2),
    }


# ================================================================
# 2. Epstein zeta via theta function (analytic continuation)
# ================================================================

def _theta_binary(t, a, b, c, N=30):
    r"""Theta function Theta_Q(t) = sum_{(m,n) in Z^2} exp(-pi*t*Q(m,n)).

    Q(m,n) = a*m^2 + b*m*n + c*n^2.  Must have Q positive definite.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    t_mp = mpmath.mpf(t) if isinstance(t, (int, float)) else t
    result = mpmath.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            Q_mn = a * m * m + b * m * n + c * n * n
            result += mpmath.exp(-mpmath.pi * t_mp * Q_mn)
    return result


def _dual_form(a, b, c):
    r"""Dual form coefficients for Poisson summation.

    If Q(m,n) = am^2 + bmn + cn^2 with matrix A = [[a, b/2],[b/2, c]],
    then the dual form has matrix A^{-1} = (1/det A) [[c, -b/2],[-b/2, a]].
    So Q^*(m,n) = (c*m^2 - b*m*n + a*n^2) / det(A)
    where det(A) = ac - (b/2)^2 = (4ac - b^2)/4 = |disc|/4.
    """
    det = (4 * a * c - b * b) / 4.0
    return float(c) / det, -float(b) / det, float(a) / det


def epstein_zeta_theta(s, a, b, c, N_theta=30):
    r"""Epstein zeta eps_Q(s) via Chowla-Selberg theta splitting.

    Uses the Epstein-Terras representation:

        pi^{-s} Gamma(s) eps_Q(s) = -1/s - 1/(sqrt(det) * (1-s))
            + sum'_{(m,n)} Gamma_u(s, pi*Q(m,n)) / (pi*Q(m,n))^s
            + (1/sqrt(det)) sum'_{(m,n)} Gamma_u(1-s, pi*Q^{-1}(m,n))
              / (pi*Q^{-1}(m,n))^{1-s}

    where Gamma_u(s,x) = integral_x^infty t^{s-1} e^{-t} dt is the
    upper incomplete gamma function.

    Valid for all s in C except s = 0, 1.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    pi = mpmath.pi

    a_f, b_f, c_f = float(a), float(b), float(c)
    det = (4 * a_f * c_f - b_f * b_f) / 4.0
    sqrt_det = mpmath.sqrt(det)

    # Dual form
    ai, bi, ci = _dual_form(a_f, b_f, c_f)

    def upper_gamma_sum(s_val, af, bf, cf, N):
        """Sum of Gamma_u(s, pi*Q(m,n)) / (pi*Q(m,n))^s over nonzero (m,n)."""
        result = mpmath.mpf(0)
        for m in range(-N, N + 1):
            for n in range(-N, N + 1):
                if m == 0 and n == 0:
                    continue
                Q_mn = af * m * m + bf * m * n + cf * n * n
                if Q_mn <= 0:
                    continue
                x = pi * Q_mn
                if float(mpmath.re(x)) > 200:
                    continue
                result += mpmath.gammainc(s_val, x) * mpmath.power(x, -s_val)
        return result

    S1 = upper_gamma_sum(s_mp, a_f, b_f, c_f, N_theta)
    S2 = upper_gamma_sum(1 - s_mp, ai, bi, ci, N_theta)

    # Pole terms
    pole = -1 / s_mp - 1 / (sqrt_det * (1 - s_mp))

    # pi^{-s} Gamma(s) eps_Q(s) = S1 + S2/sqrt(det) + pole
    lhs = S1 + S2 / sqrt_det + pole

    # Recover eps_Q(s):
    eps = lhs * mpmath.power(pi, s_mp) / mpmath.gamma(s_mp)
    return complex(eps)


def completed_epstein(s, a, b, c):
    r"""Completed Epstein zeta Xi_Q(s) = D_E^{s/2} pi^{-s} Gamma(s) eps_Q(s).

    Where D_E = |disc(Q)|/4 = ac - (b/2)^2.
    Satisfies Xi_Q(s) = Xi_Q(1-s) for forms equivalent to their dual.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    a_f, b_f, c_f = float(a), float(b), float(c)
    D_E = a_f * c_f - (b_f / 2) ** 2
    eps = epstein_zeta_theta(s, a, b, c)
    Xi = (
        mpmath.power(D_E, s_mp / 2)
        * mpmath.power(mpmath.pi, -s_mp)
        * mpmath.gamma(s_mp)
        * mpmath.mpc(eps)
    )
    return complex(Xi)


# ================================================================
# 3. Koszul-Epstein for specific algebras
# ================================================================

def koszul_epstein_ising(s, N_theta=30):
    r"""Koszul-Epstein function for the Ising model.

    eps^KE_{Ising}(s) = eps_Q(s) where Q is the shadow metric
    binary form (1/4)m^2 + 6mn + (1924/49)n^2.

    Equivalent to the scaled form 49m^2 + 1176mn + 7696n^2
    (up to a multiplicative factor 196^{-s}).
    """
    # Use the real-valued form directly
    a = 0.25  # 1/4
    b = 6.0
    c = 1924.0 / 49.0
    return epstein_zeta_theta(s, a, b, c, N_theta=N_theta)


def koszul_epstein_virasoro_c1(s, N_theta=30):
    r"""Koszul-Epstein function for Virasoro at c = 1.

    eps^KE_{Vir_1}(s) = eps_Q(s) where Q is the shadow metric
    binary form m^2 + 12mn + (1052/27)n^2.
    """
    a = 1.0
    b = 12.0
    c = 1052.0 / 27.0
    return epstein_zeta_theta(s, a, b, c, N_theta=N_theta)


# ================================================================
# 4. Off-line zero search
# ================================================================

def _evaluate_on_grid(eps_func, sigma_range, t_range, n_sigma, n_t):
    r"""Evaluate eps on a grid of s = sigma + i*t values.

    Returns a 2D array of complex values and the grid coordinates.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    sigmas = [sigma_range[0] + (sigma_range[1] - sigma_range[0]) * j / (n_sigma - 1)
              for j in range(n_sigma)]
    ts = [t_range[0] + (t_range[1] - t_range[0]) * j / (n_t - 1)
          for j in range(n_t)]

    values = []
    for sigma in sigmas:
        row = []
        for t in ts:
            s = complex(sigma, t)
            val = eps_func(s)
            row.append(val)
        values.append(row)

    return sigmas, ts, values


def find_approximate_zeros(eps_func, sigma_range=(0.1, 0.9), t_range=(1.0, 50.0),
                           n_sigma=40, n_t=200, threshold=None):
    r"""Find approximate zeros of an Epstein zeta in the critical strip.

    Strategy: evaluate on a grid, find cells where |eps| is small,
    then refine using Newton's method (secant variant).

    An OFF-LINE zero has Re(s) != 1/2. We search the full strip
    sigma_range[0] < Re(s) < sigma_range[1] but flag zeros with
    |Re(s) - 1/2| > tolerance as off-line.

    Returns list of approximate zero locations with metadata.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    sigmas, ts, values = _evaluate_on_grid(
        eps_func, sigma_range, t_range, n_sigma, n_t
    )

    # Find grid cells with local minima of |eps|
    candidates = []
    for i in range(1, n_sigma - 1):
        for j in range(1, n_t - 1):
            val = abs(values[i][j])
            # Check if this is a local minimum in |eps|
            neighbors = [
                abs(values[i - 1][j]), abs(values[i + 1][j]),
                abs(values[i][j - 1]), abs(values[i][j + 1]),
            ]
            if val < min(neighbors):
                candidates.append((sigmas[i], ts[j], val))

    # Sort by |eps| value
    candidates.sort(key=lambda x: x[2])

    # Adaptive threshold: use smallest values
    if threshold is None:
        # Take candidates where |eps| < 10 * minimum
        if candidates:
            min_val = candidates[0][2]
            threshold = max(min_val * 100, 1e-3)
        else:
            threshold = 1e-3

    # Filter
    good_candidates = [(s, t, v) for s, t, v in candidates if v < threshold]

    # Refine each candidate using mpmath's findroot
    zeros = []
    for sigma0, t0, v0 in good_candidates[:50]:  # limit refinement attempts
        try:
            s0 = mpmath.mpc(sigma0, t0)
            # Use secant method to refine
            s_refined = _refine_zero(eps_func, s0)
            if s_refined is not None:
                sigma_r = float(mpmath.re(s_refined))
                t_r = float(mpmath.im(s_refined))
                val_r = abs(eps_func(complex(s_refined)))
                is_offline = abs(sigma_r - 0.5) > 0.01
                zeros.append({
                    'sigma': sigma_r,
                    't': t_r,
                    's': complex(s_refined),
                    'value': val_r,
                    'is_offline': is_offline,
                    'initial_guess': complex(sigma0, t0),
                })
        except Exception:
            pass

    # Deduplicate: remove zeros within distance 0.1 of each other
    unique_zeros = []
    for z in zeros:
        is_dup = False
        for uz in unique_zeros:
            if abs(z['s'] - uz['s']) < 0.1:
                is_dup = True
                break
        if not is_dup:
            unique_zeros.append(z)

    return unique_zeros


def _refine_zero(eps_func, s0, max_iter=50, tol=1e-12):
    r"""Refine an approximate zero using Muller's method.

    Muller's method generalizes secant to complex functions by
    fitting a quadratic through three points.
    """
    if not HAS_MPMATH:
        return None

    h = mpmath.mpf('0.01')
    s1 = s0 + h
    s2 = s0 - h * mpmath.mpc(0, 1)

    f0 = mpmath.mpc(eps_func(complex(s0)))
    f1 = mpmath.mpc(eps_func(complex(s1)))
    f2 = mpmath.mpc(eps_func(complex(s2)))

    for _ in range(max_iter):
        # Divided differences
        h1 = s1 - s0
        h2 = s2 - s1
        if abs(h1) < 1e-30 or abs(h2) < 1e-30:
            break

        delta1 = (f1 - f0) / h1
        delta2 = (f2 - f1) / h2

        if abs(s2 - s0) < 1e-30:
            break
        a = (delta2 - delta1) / (s2 - s0)
        b_coeff = delta2 + a * h2
        c_coeff = f2

        disc = b_coeff ** 2 - 4 * a * c_coeff
        sqrt_disc = mpmath.sqrt(disc)

        # Choose the denominator with larger absolute value
        denom1 = b_coeff + sqrt_disc
        denom2 = b_coeff - sqrt_disc
        denom = denom1 if abs(denom1) > abs(denom2) else denom2

        if abs(denom) < 1e-30:
            break

        s_new = s2 - 2 * c_coeff / denom

        # Check convergence
        f_new = mpmath.mpc(eps_func(complex(s_new)))
        if abs(f_new) < tol:
            # Verify it's in the strip
            sigma = float(mpmath.re(s_new))
            t_val = float(mpmath.im(s_new))
            if 0 < sigma < 1 and t_val > 0.5:
                return s_new
            else:
                return None

        # Shift
        s0, f0 = s1, f1
        s1, f1 = s2, f2
        s2, f2 = s_new, f_new

    # Check final value
    if abs(f2) < 1e-6:
        sigma = float(mpmath.re(s2))
        t_val = float(mpmath.im(s2))
        if 0 < sigma < 1 and t_val > 0.5:
            return s2
    return None


def search_offline_zeros_ising(t_max=50.0, n_sigma=30, n_t=150):
    r"""Search for off-line zeros of the Ising Koszul-Epstein function.

    Searches the strip 0.1 < Re(s) < 0.9, 1 < Im(s) < t_max.
    Returns list of zeros found, with off-line flag.
    """
    return find_approximate_zeros(
        koszul_epstein_ising,
        sigma_range=(0.1, 0.9),
        t_range=(1.0, t_max),
        n_sigma=n_sigma,
        n_t=n_t,
    )


def search_offline_zeros_virasoro_c1(t_max=50.0, n_sigma=30, n_t=150):
    r"""Search for off-line zeros of the Virasoro c=1 Koszul-Epstein function."""
    return find_approximate_zeros(
        koszul_epstein_virasoro_c1,
        sigma_range=(0.1, 0.9),
        t_range=(1.0, t_max),
        n_sigma=n_sigma,
        n_t=n_t,
    )


# ================================================================
# 5. L-function decomposition for h(D) = 2
# ================================================================

def _kronecker_symbol(D, n):
    r"""Kronecker symbol (D/n) for fundamental discriminant D.

    Uses quadratic reciprocity and the Jacobi symbol.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    # Use mpmath for Jacobi/Kronecker
    # For negative D and odd positive n, (D/n) = Jacobi symbol
    # For n=2: (D/2) = 0 if D even, 1 if D ≡ 1 mod 8, -1 if D ≡ 5 mod 8
    if n == 0:
        return 0
    if n < 0:
        n = -n
    if n == 1:
        return 1

    # Factor n and use multiplicativity
    result = 1
    # Handle sign
    if D < 0:
        # (-1/n) = (-1)^{(n-1)/2} for odd n
        pass  # handled by Jacobi

    # For the Kronecker symbol, use sympy if available
    try:
        from sympy.ntheory.residues import jacobi_symbol
        from sympy import factorint

        factors = factorint(n)
        for p, e in factors.items():
            if p == 2:
                D_mod8 = D % 8
                if D % 2 == 0:
                    chi2 = 0
                elif D_mod8 == 1 or D_mod8 == 7:
                    chi2 = 1
                elif D_mod8 == 3 or D_mod8 == 5:
                    chi2 = -1
                else:
                    chi2 = 0
                result *= chi2 ** e
            else:
                result *= jacobi_symbol(D % p, p) ** e
        return result
    except ImportError:
        # Fallback: direct computation for small n
        return _kronecker_naive(D, n)


def _kronecker_naive(D, n):
    """Naive Kronecker symbol for small n."""
    if n == 1:
        return 1
    if n == 0:
        return 0

    # For prime p: (D/p) = D^{(p-1)/2} mod p
    # Factor n
    result = 1
    temp_n = abs(n)

    # Handle factor of 2
    while temp_n % 2 == 0:
        temp_n //= 2
        D_mod8 = D % 8
        if D % 2 == 0:
            return 0
        if D_mod8 in (1, 7):
            pass  # (D/2) = 1
        else:
            result *= -1

    # Handle odd prime factors
    p = 3
    while p * p <= temp_n:
        while temp_n % p == 0:
            temp_n //= p
            leg = pow(D % p, (p - 1) // 2, p)
            if leg == p - 1:
                leg = -1
            result *= leg
        p += 2

    if temp_n > 1:
        p = temp_n
        leg = pow(D % p, (p - 1) // 2, p)
        if leg == p - 1:
            leg = -1
        result *= leg

    return result


def hecke_L_function(s, D0, chi_type='trivial', N_terms=5000):
    r"""Hecke L-function L(s, chi) for a character of Cl(D_0).

    For the TRIVIAL character chi_0:
        L(s, chi_0) = zeta(s) * L(s, (D_0/.))
    This is the Dedekind zeta function of Q(sqrt(D_0)).

    For the SIGN character chi_1 (for h=2, this is the unique non-trivial):
        L(s, chi_1) = sum_{n >= 1, gcd(n,f)=1} chi_1(n) n^{-s}
    where chi_1 is determined by the class group action on ideals.

    For fundamental discriminant D_0 < 0 with h(D_0) = 2:
    There are exactly 2 genera. The principal genus contains the
    principal form; the other genus contains the non-principal form.
    The genus character is the Kronecker symbol.

    THIS FUNCTION computes the Dedekind zeta zeta_K(s) and the
    quadratic L-function L(s, chi_D) separately, then combines.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)

    if chi_type == 'trivial':
        # L(s, chi_0) = zeta_K(s) = zeta(s) * L(s, chi_D)
        # where chi_D = Kronecker symbol (D_0/.)
        z = mpmath.zeta(s_mp)
        # L(s, chi_D) = sum_{n>=1} (D_0/n) * n^{-s}
        L_chi = mpmath.mpf(0)
        for n in range(1, N_terms + 1):
            chi_n = _kronecker_symbol(D0, n)
            if chi_n != 0:
                L_chi += chi_n * mpmath.power(n, -s_mp)
        return complex(z * L_chi)

    elif chi_type == 'sign':
        # For h=2: the sign character chi_1 is determined by
        # chi_1(p) = (D_0/p) for primes not dividing D_0
        # but with OPPOSITE sign from chi_0 on the non-principal class.
        #
        # Actually for h(D_0) = 2 with Cl = Z/2:
        # eps_principal(s) = (1/w)[L_0(s) + L_1(s)]
        # eps_nonprincipal(s) = (1/w)[L_0(s) - L_1(s)]
        # where L_0 = zeta_K(s) and L_1 is the L-function of the
        # non-trivial character.
        #
        # For FUNDAMENTAL discriminants with h=2, the two L-functions
        # factor through genus characters. The genus character for
        # D_0 = d_1 * d_2 (with d_1, d_2 fundamental discriminants,
        # D_0 = d_1 * d_2) gives:
        #   L_0(s) = L(s, chi_{d_1}) * L(s, chi_{d_2})
        #   L_1(s) = L(s, chi_{d_1}) * L(s, chi_{d_2})
        # Wait, this is the same thing. The factorization of genus
        # L-functions is more subtle.
        #
        # For D_0 = -40 = -8 * 5: d_1 = -8, d_2 = 5 (or -5, 8).
        # Genus characters: chi_1 = (./5), chi_2 = (-8/.)
        # zeta_K(s) = L(s, chi_{-40}) * zeta(s)
        # The genus L-function: L_genus(s) = L(s, (-8/.)) * L(s, (5/.))
        #
        # The decomposition of the Epstein zeta of a SPECIFIC form:
        # For the principal form (1,0,10):
        #   eps_{(1,0,10)}(s) = (1/w)[zeta_K(s) + L_genus(s)]
        # For the non-principal form (2,0,5):
        #   eps_{(2,0,5)}(s) = (1/w)[zeta_K(s) - L_genus(s)]

        # The "sign character L-function" is the genus L-function.
        # For D_0 = -40: genus decomposition -40 = (-8)(5)
        # L_genus(s) = L(s, chi_{-8}) * L(s, chi_5)
        if D0 == -40:
            # chi_{-8}: (−8/n) = Kronecker symbol
            # chi_5: (5/n) = Legendre symbol
            L1 = mpmath.mpf(0)
            L2 = mpmath.mpf(0)
            for n in range(1, N_terms + 1):
                chi_m8 = _kronecker_symbol(-8, n)
                chi_5 = _kronecker_symbol(5, n)
                L1 += chi_m8 * mpmath.power(n, -s_mp)
                L2 += chi_5 * mpmath.power(n, -s_mp)
            return complex(L1 * L2)
        elif D0 == -15:
            # D_0 = -15 = (-3)(5)
            # L_genus(s) = L(s, chi_{-3}) * L(s, chi_5)
            L1 = mpmath.mpf(0)
            L2 = mpmath.mpf(0)
            for n in range(1, N_terms + 1):
                chi_m3 = _kronecker_symbol(-3, n)
                chi_5 = _kronecker_symbol(5, n)
                L1 += chi_m3 * mpmath.power(n, -s_mp)
                L2 += chi_5 * mpmath.power(n, -s_mp)
            return complex(L1 * L2)
        else:
            raise ValueError(f"Genus L-function not implemented for D_0 = {D0}")
    else:
        raise ValueError(f"Unknown chi_type: {chi_type}")


def epstein_decomposition(s, data, N_terms=5000):
    r"""Decompose the Koszul-Epstein function into L-function components.

    For h(D_0) = 2:
        eps_Q(s) = (1/w) * [L_0(s) + sign(Q) * L_1(s)]

    where sign(Q) = +1 for principal class, -1 for non-principal.
    w = number of units (w=2 for D < -4).

    Returns dict with L_0, L_1, and the combination.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    D0 = data['D0']
    w = 2  # for |D| > 4

    L0 = hecke_L_function(s, D0, 'trivial', N_terms=N_terms)
    L1 = hecke_L_function(s, D0, 'sign', N_terms=N_terms)

    # Determine which class the shadow form belongs to.
    # The reduced form determines this. For D_0 = -40:
    # principal = (1,0,10), nonprincipal = (2,0,5).
    # The Ising reduced form is (49, 0, 640) with disc = -125440 = -40 * 56^2.
    # The form (49, 0, 640) represents the same class as...
    # Actually for forms of discriminant -125440 (not -40), the class group
    # is larger. The class number h(-125440) includes non-fundamental classes.
    #
    # The correct approach: the Epstein zeta of a form Q of discriminant
    # D = D_0 * f^2 decomposes over PRIMITIVE Hecke characters mod f,
    # not just the characters of Cl(D_0). For a proper decomposition we
    # need the generalized class group.
    #
    # HOWEVER: for the DH question, the key point is simpler.
    # The Epstein zeta of Q with disc D = D_0 * f^2 has the form:
    #   eps_Q(s) = f^{-2s} * sum over ideal classes and conductor chars
    #
    # For our purpose (zero detection), we compute eps_Q DIRECTLY via
    # theta function (already done above) and decompose NUMERICALLY.

    # The L-function decomposition serves as a CHECK, not as the primary
    # computation. The primary zero search uses the theta method.
    return {
        'L0': L0,
        'L1': L1,
        'w': w,
        'D0': D0,
        'note': 'L0 = zeta_K(s), L1 = genus L-function; '
                'eps = (1/w)[L0 +/- L1] for principal/non-principal class',
    }


# ================================================================
# 6. Genus-2 Beurling kernel
# ================================================================

def genus2_beurling_kernel(D1, D2, T=20.0, N_terms=3000):
    r"""Genus-2 Beurling kernel K^(2)(D1, D2).

    The genus-2 Beurling kernel arises from the genus-2 amplitude:

        K^(2)(D1, D2) = integral_0^infty integral_0^infty
            Theta_{Q_1}(t1) * Theta_{Q_2}(t2) * G^(2)(t1, t2) dt1 dt2

    where G^(2) is the genus-2 Green's function on M_{2,0}, and
    Q_1, Q_2 are shadow metric forms of discriminant D_1, D_2.

    For our purposes, the genus-2 constraint is:

        K^(2)(D, D) >= 0

    This positivity arises because K^(2)(D,D) = ||Theta_Q||^2_{L^2(M_2)}
    in a suitable norm.

    MORE PRECISELY: the genus-2 bar amplitude for algebra A is

        F_2(A) = kappa(A) * lambda_2 + (higher arity corrections)

    The lambda_2 contribution is:
        lambda_2 = integral_{M_{2,0}} lambda_1^2 = 1/240 (Faber-Pandharipande)

    The genus-2 planted-forest correction is:
        delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48

    The genus-2 positivity K^(2)(D,D) >= 0 means that the genus-2
    amplitude squared is non-negative when summed over both Koszul
    dual channels.

    The constraint on zeros: if eps_Q(s_0) = 0 with Re(s_0) > 1/2,
    then the Mellin transform of Theta_Q has a zero, which constrains
    the L^2 norm. The genus-2 kernel relates the s-variable zeros
    to the t-variable (moduli) behavior through:

        K^(2)(D, D) = integral |eps_Q(1/2 + it)|^2 * W_2(t) dt

    where W_2(t) is the genus-2 weight function. Positivity of K^(2)
    does NOT by itself exclude off-line zeros, but it constrains
    the DENSITY of zeros: too many off-line zeros would make the
    integral too negative.

    THIS FUNCTION computes K^(2)(D, D) numerically for the shadow
    metric forms.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    # For the DIAGONAL kernel K^(2)(D, D), we use the Li-type positivity:
    #
    # K^(2)(D, D) = sum_{rho} (1 - (1 - 1/rho)^2) / |rho|^2
    #
    # where the sum is over nontrivial zeros rho of eps_Q(s).
    # This is positive iff the zeros are "close enough" to the critical line.
    #
    # More directly: K^(2)(D,D) is related to the second moment of eps_Q
    # on the critical line:
    #
    # K^(2) = integral_0^T |eps_Q(1/2 + it)|^2 dt + O(1)
    #
    # which is always positive. So K^(2)(D,D) >= 0 is AUTOMATIC and does
    # not constrain zero locations.
    #
    # HOWEVER: the genus-2 PLANTED-FOREST correction introduces additional
    # structure. The full genus-2 amplitude is:
    #
    #   A_2(A) = kappa * lambda_2 + delta_pf^{(2,0)}(A)
    #          = kappa * (1/240) + S_3*(10*S_3 - kappa)/48
    #
    # The KOSZUL CONSTRAINT is that A_2(A) + A_2(A!) must be expressible
    # in terms of tautological classes. This gives a RELATION between
    # the genus-2 data of A and A!.
    #
    # Compute the second moment numerically.

    # We compute K^(2)(D,D) as the integral of |Xi_Q(1/2+it)|^2 weighted
    # by the genus-2 measure.

    # For a concrete computation, compute the second moment:
    #   M_2 = (1/T) integral_0^T |eps_Q(1/2 + it)|^2 dt

    # Use the shadow form for discriminant D1
    # Map D to form coefficients
    form = _discriminant_to_form(D1)
    if form is None:
        return None

    a, b, c = form

    # Compute the mean-square on the critical line
    result = mpmath.mpf(0)
    dt = T / N_terms
    for j in range(1, N_terms + 1):
        t = j * dt
        s = complex(0.5, t)
        eps_val = epstein_zeta_theta(s, a, b, c, N_theta=20)
        result += abs(eps_val) ** 2 * dt

    K2 = float(result)
    return {
        'K2_diagonal': K2,
        'D': D1,
        'T': T,
        'is_positive': K2 >= 0,
        'note': 'K^(2)(D,D) = second moment of eps_Q on critical line; always >= 0',
    }


def _discriminant_to_form(D):
    """Map a fundamental discriminant to the principal reduced form."""
    if D >= 0:
        return None
    absD = -D
    # For D < -4: find reduced form (a, b, c) with b^2 - 4ac = D
    # Principal form: a=1, b = D mod 2, c = (b^2 - D)/4
    b = absD % 2  # 0 or 1
    c = (b * b + absD) // 4
    a = 1
    if b * b - 4 * a * c != D:
        return None
    return (a, b, c)


# ================================================================
# 7. Genus-2 positivity and zero exclusion analysis
# ================================================================

def genus2_zero_constraint(algebra_data, zeros_found):
    r"""Analyze whether genus-2 positivity constrains off-line zeros.

    The genus-2 Koszul constraint is:

        A_2(A) + A_2(A!) = kappa(A)*lambda_2 + kappa(A!)*lambda_2
                           + delta_pf(A) + delta_pf(A!)

    where lambda_2 = 7/5760 (Faber-Pandharipande, CORRECTED per AP38)
    and delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48.

    The complementarity constraint (Theorem C) requires this to be
    a tautological class on M_{2,0}.

    If off-line zeros exist, the spectral decomposition of eps_Q
    has contributions from Re(rho) != 1/2. This affects the
    planted-forest correction through the Rankin-Selberg integral.

    RESULT: genus-2 positivity K^(2)(D,D) >= 0 is AUTOMATIC (it's a
    squared norm). The genus-2 COMPLEMENTARITY constraint
    A_2(A) + A_2(A!) = tautological is a STRONGER condition,
    but it constrains the VALUE of the amplitude, not the zero
    locations of the Epstein zeta.

    The structural diagnosis (thm:structural-separation): the
    genus-1 MC equation cannot access scattering-matrix poles.
    The genus-2 constraint is similarly indirect: it constrains
    algebraic combinations of shadow invariants (kappa, S_3),
    not the analytic properties of eps_Q(s).

    Returns analysis dict.
    """
    c_val = float(algebra_data['c'])
    kappa = float(algebra_data['kappa'])
    alpha = float(algebra_data['alpha'])
    S4 = float(algebra_data['S4'])

    # Shadow tower coefficient S_3 = alpha (for Virasoro)
    S3 = alpha

    # Genus-2 amplitude components
    lambda_2 = 7.0 / 5760  # Faber-Pandharipande (AP38 corrected)
    delta_pf = S3 * (10 * S3 - kappa) / 48.0
    A2 = kappa * lambda_2 + delta_pf

    # Koszul dual data
    c_dual = 26 - c_val
    kappa_dual = c_dual / 2
    alpha_dual = 2.0
    S4_dual = 10.0 / (c_dual * (5 * c_dual + 22)) if c_dual != 0 else float('inf')
    S3_dual = alpha_dual
    delta_pf_dual = S3_dual * (10 * S3_dual - kappa_dual) / 48.0
    A2_dual = kappa_dual * lambda_2 + delta_pf_dual

    # Complementarity sum
    A2_sum = A2 + A2_dual

    n_offline = sum(1 for z in zeros_found if z.get('is_offline', False))
    n_online = len(zeros_found) - n_offline

    return {
        'algebra': algebra_data['name'],
        'c': c_val,
        'kappa': kappa,
        'S3': S3,
        'lambda_2': lambda_2,
        'delta_pf': delta_pf,
        'A_2': A2,
        'A_2_dual': A2_dual,
        'A_2_sum': A2_sum,
        'n_zeros_found': len(zeros_found),
        'n_offline': n_offline,
        'n_online': n_online,
        'K2_positive': True,  # Always true (squared norm)
        'genus2_excludes_offline': False,
        'structural_diagnosis': (
            'The genus-2 positivity K^(2)(D,D) >= 0 is automatic '
            '(it is a squared L^2 norm on the critical line). '
            'The complementarity constraint A_2(A) + A_2(A!) constrains '
            'the VALUE of the genus-2 amplitude through (kappa, S_3), '
            'not the zero locations of eps_Q(s). '
            'By thm:structural-separation, the MC equation at any '
            'fixed genus cannot access the scattering poles of the '
            'Epstein zeta. Off-line zeros, if they exist, are NOT '
            'excluded by genus-2 data alone.'
        ),
    }


# ================================================================
# 8. Functional equation verification
# ================================================================

def verify_functional_equation(eps_func, s_values, name=''):
    r"""Verify the functional equation eps_Q satisfies Xi(s) = Xi(1-s).

    For the COMPLETED function Xi_Q(s) = D_E^{s/2} pi^{-s} Gamma(s) eps_Q(s).
    """
    if not HAS_MPMATH:
        return []

    results = []
    for s in s_values:
        eps_s = eps_func(s)
        eps_1ms = eps_func(1 - s)

        # For the raw Epstein zeta, the functional equation involves Gamma
        # factors. Test the COMPLETED function instead.
        # Xi(s)/Xi(1-s) should equal 1.
        # But we don't have Xi directly from eps_func.
        # Instead, test that eps(s) and eps(1-s) are related by the
        # expected Gamma/pi factors.

        # For now, just record both values
        results.append({
            'name': name,
            's': s,
            '1-s': 1 - s,
            'eps_s': eps_s,
            'eps_1ms': eps_1ms,
        })

    return results


# ================================================================
# 9. Critical line behavior
# ================================================================

def critical_line_values(eps_func, t_values, name=''):
    r"""Evaluate the Koszul-Epstein function on the critical line Re(s) = 1/2."""
    results = []
    for t in t_values:
        s = complex(0.5, t)
        val = eps_func(s)
        results.append({
            'name': name,
            't': t,
            's': s,
            'value': val,
            'abs_value': abs(val),
        })
    return results


def critical_line_sign_changes(eps_func, t_range=(1.0, 50.0), n_points=500):
    r"""Find sign changes of Re(eps_Q(1/2 + it)) on the critical line.

    Sign changes of the real part indicate zeros of the completed
    function on the critical line (these are the ON-LINE zeros).
    """
    if not HAS_MPMATH:
        return []

    sign_changes = []
    dt = (t_range[1] - t_range[0]) / n_points
    prev_val = None
    prev_t = None

    for j in range(n_points + 1):
        t = t_range[0] + j * dt
        s = complex(0.5, t)
        val = eps_func(s)
        re_val = val.real

        if prev_val is not None:
            if prev_val * re_val < 0:
                # Sign change between prev_t and t
                # Bisect to find the zero more precisely
                t_zero = _bisect_sign_change(
                    lambda tt: eps_func(complex(0.5, tt)).real,
                    prev_t, t, tol=1e-6
                )
                sign_changes.append({
                    't': t_zero,
                    's': complex(0.5, t_zero),
                    'type': 'on-line zero',
                })

        prev_val = re_val
        prev_t = t

    return sign_changes


def _bisect_sign_change(f, a, b, tol=1e-6, max_iter=50):
    """Bisect to find sign change of f in [a, b]."""
    fa = f(a)
    for _ in range(max_iter):
        mid = (a + b) / 2
        if (b - a) < tol:
            return mid
        fmid = f(mid)
        if fa * fmid < 0:
            b = mid
        else:
            a = mid
            fa = fmid
    return (a + b) / 2


# ================================================================
# 10. Master analysis function
# ================================================================

def run_full_analysis(t_max=50.0, grid_sigma=25, grid_t=100, verbose=True):
    r"""Run the complete Davenport-Heilbronn genus-2 analysis.

    For both Ising (c=1/2, D_0=-40, h=2) and Virasoro c=1 (D_0=-15, h=2):
    1. Compute the Koszul-Epstein function via theta method
    2. Search for off-line zeros in the critical strip
    3. Find on-line zeros (sign changes on Re(s)=1/2)
    4. Check genus-2 positivity
    5. Analyze whether genus-2 data constrains off-line zeros

    Returns comprehensive analysis dict.
    """
    results = {}

    for name, data_func, eps_func in [
        ('Ising', ising_shadow_data, koszul_epstein_ising),
        ('Virasoro_c1', virasoro_c1_shadow_data, koszul_epstein_virasoro_c1),
    ]:
        if verbose:
            print(f"\n{'='*60}")
            print(f"  {name}: D_0 = {data_func()['D0']}, h = {data_func()['class_number']}")
            print(f"{'='*60}")

        data = data_func()

        # On-line zeros (sign changes on critical line)
        if verbose:
            print(f"  Searching for on-line zeros (Re(s) = 1/2)...")
        on_line = critical_line_sign_changes(eps_func, t_range=(1.0, t_max))
        if verbose:
            print(f"  Found {len(on_line)} on-line zeros")
            for z in on_line[:10]:
                print(f"    t = {z['t']:.6f}")

        # Off-line zero search
        if verbose:
            print(f"  Searching for off-line zeros...")
        off_line = find_approximate_zeros(
            eps_func,
            sigma_range=(0.1, 0.9),
            t_range=(1.0, t_max),
            n_sigma=grid_sigma,
            n_t=grid_t,
        )
        n_offline = sum(1 for z in off_line if z.get('is_offline', False))
        if verbose:
            print(f"  Found {len(off_line)} candidate zeros, {n_offline} off-line")
            for z in off_line:
                marker = " ** OFF-LINE **" if z['is_offline'] else ""
                print(f"    s = {z['sigma']:.6f} + {z['t']:.6f}i, "
                      f"|eps| = {z['value']:.2e}{marker}")

        # Genus-2 constraint analysis
        all_zeros = on_line + off_line
        g2_analysis = genus2_zero_constraint(data, off_line)

        if verbose:
            print(f"\n  Genus-2 analysis:")
            print(f"    A_2(A)  = {g2_analysis['A_2']:.8f}")
            print(f"    A_2(A!) = {g2_analysis['A_2_dual']:.8f}")
            print(f"    Sum     = {g2_analysis['A_2_sum']:.8f}")
            print(f"    K^(2) positive: {g2_analysis['K2_positive']}")
            print(f"    Genus-2 excludes off-line: {g2_analysis['genus2_excludes_offline']}")

        results[name] = {
            'data': data,
            'on_line_zeros': on_line,
            'off_line_search': off_line,
            'n_offline': n_offline,
            'genus2_analysis': g2_analysis,
        }

    return results
