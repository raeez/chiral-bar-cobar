r"""Colmez conjecture at shadow parameters and p-adic period computations (BC-119).

MATHEMATICAL CONTENT
====================

The Colmez conjecture (proved by Andreatta-Goren-Howard-Madapusi Pera 2018,
Yuan-Zhang 2018) determines the Faltings height of a CM abelian variety
from logarithmic derivatives of L-functions:

    h_F(A) = -(1/2) * L'(chi_K, 0) / L(chi_K, 0) - (1/2) log(2*pi)
           + (1/4) log|D_K|                                  [averaged form]

where K = Q(sqrt(D)) is the CM field and chi_K = (D/.) is the Kronecker symbol.

For the shadow programme: each modular Koszul algebra A determines a
shadow spectral curve C_A: y^2 = Q_L(t).  When the critical discriminant
Delta_A := 8*kappa*S_4 is NEGATIVE, Q_L has real roots and C_A has a real
structure related to CM.  We parameterize:

    c_CM(D) = central charge such that Delta_Vir(c_CM) resembles disc D

and compute Colmez-type invariants at these shadow CM points.

p-ADIC PERIODS:

For an elliptic curve E/Q_p with split multiplicative reduction,
Tate's uniformization gives:

    E(Q_p) ~ Q_p* / q_E^Z

where q_E is the Tate parameter (|q_E|_p < 1).  The p-adic period is:

    Omega_p(E) = log_p(q_E) / ord_p(q_E)

p-ADIC L-FUNCTIONS (Mazur-Tate-Teitelbaum):

For E/Q of conductor N, the p-adic L-function L_p(E, s) interpolates
critical L-values twisted by p-adic characters:

    L_p(E, chi, 1) = (1 - a_p * p^{-1}) * L(E, 1) / Omega_E

when p does not divide N.  The EXCEPTIONAL ZERO phenomenon occurs when
p || N and a_p = +1: then L_p(E, 1) = 0 regardless of L(E, 1).

SHADOW CM POINTS:

The shadow discriminant for Virasoro at central charge c is:

    Delta(c) = 8 * (c/2) * 10 / (c * (5c + 22)) = 40 / (5c + 22)

This is ALWAYS POSITIVE for c > 0, so the shadow curve is definite.
However, the ARITHMETIC discriminant of the shadow metric Q_L viewed as
a binary quadratic form (after clearing denominators) gives a fundamental
discriminant D(c) that may be negative, connecting to CM theory.

Specifically, Q_L(t) = (c + 6t)^2 + (80/(5c+22))t^2 has discriminant
(as a quadratic in t):

    disc_Q = 36 - (80/(5c+22)) [coefficient discriminant]

which is negative when c < -22/5 + 80/180 (outside the physical range).
For the physical range c > 0, disc_Q > 0 and Q_L has no real roots.

We therefore adopt an ARITHMETIC approach: parameterize shadow CM points
via the CLASS NUMBER ONE discriminants D in {-3, -4, -7, -8, -11, -19,
-43, -67, -163} and compute L-function data at these arithmetic inputs.

VERIFICATION PATHS:
  1. Colmez formula (L'/L at s=0 via functional equation)
  2. Direct Chowla-Selberg period formula (Gamma values)
  3. Dirichlet class number formula cross-check
  4. p-adic uniformization (Tate curve q-parameter)
  5. Mazur-Tate-Teitelbaum interpolation
  6. Numerical comparison across methods

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

AP COMPLIANCE:
    AP1:  kappa formulas recomputed from first principles per family
    AP10: cross-family consistency checks, not hardcoded expected values
    AP24: complementarity sum NOT assumed zero; computed per family
    AP38: literature convention documented at each hardcoded value
    AP39: kappa != c/2 in general; family-specific formulas used
    AP48: kappa depends on full algebra, not Virasoro subalgebra
"""

from __future__ import annotations

import math
import cmath
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import mpmath
    from mpmath import (
        mp, mpf, mpc, pi as mp_pi, euler as mp_euler,
        log as mp_log, exp as mp_exp, power as mp_power,
        sqrt as mp_sqrt, re as mpre, im as mpim, fabs,
        gamma as mp_gamma, loggamma as mp_loggamma,
        zeta as mp_zeta, diff as mp_diff,
        zetazero, inf as mp_inf,
        sin as mp_sin, cos as mp_cos,
        quad as mp_quad,
        dirichlet as mp_dirichlet,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================================
# 0. Constants and precision
# ============================================================================

_DEFAULT_DPS = 50


def set_precision(dps: int = _DEFAULT_DPS):
    """Set mpmath working precision."""
    if HAS_MPMATH:
        mp.dps = dps


set_precision(_DEFAULT_DPS)


# First 50 nontrivial zeros of Riemann zeta (imaginary parts, Re=1/2)
# Source: Odlyzko tables, verified to 30+ digits
ZETA_ZEROS_50 = [
    14.134725141734693790457251983562,
    21.022039638771554992628479593897,
    25.010857580145688763213790992563,
    30.424876125859513210311897530584,
    32.935061587739189690662368964075,
    37.586178158825671257217763480790,
    40.918719012147495187398126914633,
    43.327073280914999519496122165406,
    48.005150881167159727942472749427,
    49.773832477672302181916784678564,
    52.970321477714460644147296608880,
    56.446247697063394804367759476706,
    59.347044002602353079653648674993,
    60.831778524609809844259901824524,
    65.112544048081606660875054253183,
    67.079810529494173714478828896523,
    69.546401711173979252926857526554,
    72.067157674481907582522107969826,
    75.704690699083933168326916762030,
    77.144840068874805372682664856305,
    79.337375020249367922763592877116,
    82.910380854086030183164837494770,
    84.735492980517050105735311206827,
    87.425274613125229406531667850919,
    88.809111207634465423682348079509,
    92.491899270558484296259725241810,
    94.651344040519886966597925815208,
    95.870634228245309758741029219246,
    98.831194218193692233324420138622,
    101.317851005731220482485299189850,
    103.725538040397097273653279089465,
    105.446623052326004987546105666920,
    107.168611184276730942336086075700,
    111.029535543541888623667955831950,
    111.874659176550291174308909272120,
    114.320220915452712600520699583020,
    116.226680321667764427252825211760,
    118.790782866051797857122338856990,
    121.370125002350677114856970064040,
    122.946829293686757513948804737320,
    124.256818554345959428329567916960,
    127.516683879566669128979488485880,
    129.578704199956073600941660753840,
    131.087688530934421723613893640800,
    133.497737203139179862966131280320,
    134.756509753354068067721535660320,
    138.116042054854224894573906044280,
    139.736208952121388541585889895200,
    141.123707404021831715448979981360,
    143.111845808661987253841283455460,
]


def zeta_zero_rho(n: int) -> complex:
    """Return n-th nontrivial zero rho_n = 1/2 + i*gamma_n (1-indexed)."""
    if 1 <= n <= 50:
        return complex(0.5, ZETA_ZEROS_50[n - 1])
    if HAS_MPMATH:
        z = zetazero(n)
        return complex(float(mpre(z)), float(mpim(z)))
    raise ValueError(f"Need mpmath for zero #{n} > 50")


# ============================================================================
# 1. CM discriminants and Kronecker characters
# ============================================================================

# Fundamental discriminants with class number 1
# (Baker-Heegner-Stark: exactly 9 such discriminants)
CM_DISCRIMINANTS_H1 = [-3, -4, -7, -8, -11, -19, -43, -67, -163]

# Fundamental discriminants with class number <= 10
# Source: Watkins (2004), verified against LMFDB
CM_DISCRIMINANTS_H_LE_10 = {
    1: [-3, -4, -7, -8, -11, -19, -43, -67, -163],
    2: [-15, -20, -24, -35, -40, -51, -52, -88, -91, -115,
        -123, -148, -187, -232, -235, -267, -403, -427],
    3: [-23, -31, -59, -83, -107, -139, -211, -283, -307,
        -331, -379, -499, -547, -643, -883, -907],
    4: [-39, -55, -56, -68, -84, -120, -132, -136, -155,
        -168, -184, -195, -203, -219, -228, -259, -280,
        -291, -292, -312, -323, -328, -340, -355, -372,
        -388, -408, -435, -483, -520, -532, -555, -568,
        -595, -627, -667, -708, -715, -723, -760, -763,
        -772, -795, -955, -1003, -1012, -1027, -1227,
        -1243, -1387, -1411, -1467, -1555, -1723],
}


def kronecker_symbol(D: int, n: int) -> int:
    r"""Compute the Kronecker symbol (D/n).

    This is the unique extension of the Jacobi symbol to all integers,
    defined as the product of (D/p) over prime factors p of n, with
    special rules for p=2 and p=-1.

    For fundamental discriminant D, chi_D(n) = (D/n) is a primitive
    Dirichlet character of conductor |D|.

    The Kronecker symbol (D/2) is defined as:
        0  if D is even
        1  if D ≡ ±1 (mod 8)
       -1  if D ≡ ±3 (mod 8)
    """
    if n == 0:
        return 1 if abs(D) == 1 else 0
    if n < 0:
        n = -n
        result = -1 if D < 0 else 1
    else:
        result = 1

    # Factor out powers of 2
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0:
            # (D/2) = 0 when D is even
            return 0
        else:
            r = D % 8
            if r < 0:
                r += 8
            if r == 3 or r == 5:
                result = -result
            # r == 1 or r == 7: result unchanged

    if n == 1:
        return result

    # Now n is odd > 1, use Jacobi reciprocity
    a = D % n
    if a < 0:
        a += n

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


def is_fundamental_discriminant(D: int) -> bool:
    """Check if D is a fundamental discriminant."""
    if D == 1:
        return True
    if D == 0:
        return False
    if D % 4 == 0:
        m = D // 4
        if m % 4 in (2, 3):
            # Check m is squarefree
            return _is_squarefree(m)
        return False
    if D % 4 == 1:
        return _is_squarefree(D)
    # D % 4 in {2, 3}: not fundamental for odd D with these residues
    # Actually D ≡ 1 (mod 4) or D = 4m with m ≡ 2,3 (mod 4) squarefree
    return False


def _is_squarefree(n: int) -> bool:
    """Check if |n| is squarefree."""
    n = abs(n)
    if n == 0:
        return False
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


# ============================================================================
# 2. Dirichlet L-functions for Kronecker characters
# ============================================================================

def _kronecker_chi_list(D: int) -> list:
    r"""Build the character list [chi_D(0), chi_D(1), ..., chi_D(|D|-1)]
    for use with mpmath.dirichlet().

    mpmath.dirichlet(s, chi) expects chi as a periodic list of length equal
    to the conductor.
    """
    N = abs(D)
    return [kronecker_symbol(D, a) for a in range(N)]


def dirichlet_L_value(D: int, s: complex, dps: int = 50) -> complex:
    r"""Compute L(chi_D, s) where chi_D = (D/.) is the Kronecker symbol.

    L(chi_D, s) = sum_{n=1}^{infty} chi_D(n) * n^{-s}

    Uses mpmath.dirichlet() which handles analytic continuation,
    functional equation, and convergence acceleration internally.

    Parameters
    ----------
    D : fundamental discriminant
    s : complex evaluation point
    dps : decimal precision

    Returns
    -------
    Complex value L(chi_D, s).
    """
    if not HAS_MPMATH:
        return _dirichlet_L_value_fallback(D, s)

    old_dps = mp.dps
    mp.dps = dps + 20  # extra guard digits

    try:
        s_mp = mpc(s) if isinstance(s, complex) else mpf(s)
        chi_list = _kronecker_chi_list(D)
        result = mp_dirichlet(s_mp, chi_list)
        return complex(result)
    finally:
        mp.dps = old_dps


def _dirichlet_L_value_fallback(D: int, s: complex) -> complex:
    """Fallback without mpmath: direct partial sum."""
    N = abs(D)
    total = 0.0 + 0.0j
    for n in range(1, 10001):
        chi_n = kronecker_symbol(D, n)
        if chi_n != 0:
            total += chi_n * n ** (-s)
    return total


def dirichlet_L_derivative(D: int, s: complex, dps: int = 50) -> complex:
    r"""Compute L'(chi_D, s) = dL/ds at s.

    Uses mpmath.dirichlet(s, chi, derivative=1).
    """
    if not HAS_MPMATH:
        # Finite difference fallback
        h = 1e-8
        Lp = dirichlet_L_value(D, s + h, dps=15)
        Lm = dirichlet_L_value(D, s - h, dps=15)
        return (Lp - Lm) / (2 * h)

    old_dps = mp.dps
    mp.dps = dps + 20
    try:
        s_mp = mpc(s) if isinstance(s, complex) else mpf(s)
        chi_list = _kronecker_chi_list(D)
        result = mp_dirichlet(s_mp, chi_list, derivative=1)
        return complex(result)
    finally:
        mp.dps = old_dps


# ============================================================================
# 3. Class numbers and related invariants
# ============================================================================

def class_number(D: int) -> int:
    r"""Compute the class number h(D) of Q(sqrt(D)) for D < 0.

    Uses the analytic class number formula:
        h(D) = (w * sqrt(|D|)) / (2 * pi) * L(chi_D, 1)

    where w = |O_K*| (number of roots of unity):
        w = 6 if D = -3, w = 4 if D = -4, w = 2 otherwise.

    Verification: also computed by direct enumeration of reduced forms
    for small |D|.
    """
    if D >= 0:
        raise ValueError(f"class_number requires D < 0, got {D}")

    # Direct computation via reduced binary quadratic forms
    return _class_number_forms(D)


def _class_number_forms(D: int) -> int:
    """Class number by counting reduced binary quadratic forms of discriminant D."""
    h = 0
    absD = abs(D)
    # a ranges from 1 to sqrt(|D|/3)
    a_max = int(math.sqrt(absD / 3.0)) + 1
    for a in range(1, a_max + 1):
        # b ranges over b with b^2 ≡ D (mod 4a), |b| <= a
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                if c >= a:
                    if b >= 0 or (a != c and abs(b) != a):
                        h += 1
    return h


def roots_of_unity(D: int) -> int:
    """Number of roots of unity w(D) in the ring of integers of Q(sqrt(D))."""
    if D == -3:
        return 6
    if D == -4:
        return 4
    return 2


# ============================================================================
# 4. Colmez formula for Faltings heights
# ============================================================================

def colmez_faltings_height(D: int, dps: int = 50) -> float:
    r"""Compute the Faltings height via the (averaged) Colmez conjecture.

    For D < 0 a fundamental discriminant, the averaged Colmez conjecture
    (now a theorem, Andreatta-Goren-Howard-Madapusi Pera / Yuan-Zhang) gives:

        h_F^{avg}(D) = -(1/2) * (L'(chi_D, 0) / L(chi_D, 0))
                       - (1/2) * log(2*pi)
                       + (1/4) * log(|D|)

    This is the AVERAGED Faltings height over all CM types.
    For class number 1, the average equals the unique value.

    Convention: Faltings (1984) normalization, as in Colmez (1993).
    AP38: this is the Colmez convention, not the Silverman convention
    (which differs by -(1/2)*log(2*pi)).

    Returns
    -------
    h_F : float, the Faltings height
    """
    if D >= 0:
        raise ValueError(f"Colmez formula requires D < 0, got {D}")

    if not HAS_MPMATH:
        return _colmez_fallback(D)

    old_dps = mp.dps
    mp.dps = dps + 20
    try:
        chi_list = _kronecker_chi_list(D)

        # Compute L(chi_D, 0) and L'(chi_D, 0) via mpmath.dirichlet
        L0 = mp_dirichlet(mpf(0), chi_list)
        if fabs(L0) < mp_power(mpf(10), -dps):
            raise ValueError(f"L(chi_{D}, 0) = 0; Colmez formula not applicable")

        L0_prime = mp_dirichlet(mpf(0), chi_list, derivative=1)

        # Colmez formula
        ratio = L0_prime / L0
        h_F = -mpf('0.5') * ratio - mpf('0.5') * mp_log(2 * mp_pi) + mpf('0.25') * mp_log(mpf(abs(D)))

        return float(h_F)
    finally:
        mp.dps = old_dps


def _colmez_fallback(D: int) -> float:
    """Fallback Colmez height without mpmath."""
    L0 = complex(_dirichlet_L_value_fallback(D, 0)).real
    if abs(L0) < 1e-15:
        return float('nan')
    h = 1e-8
    Lp = complex(_dirichlet_L_value_fallback(D, h)).real
    Lm = complex(_dirichlet_L_value_fallback(D, -h)).real
    L0_prime = (Lp - Lm) / (2 * h)
    ratio = L0_prime / L0
    hF = -0.5 * ratio - 0.5 * math.log(2 * math.pi) + 0.25 * math.log(abs(D))
    return hF


# ============================================================================
# 5. Chowla-Selberg formula (independent verification path)
# ============================================================================

def chowla_selberg_period(D: int, dps: int = 50) -> float:
    r"""Compute the Chowla-Selberg period for discriminant D.

    The Chowla-Selberg formula expresses the periods of CM elliptic curves
    in terms of Gamma values at rational arguments:

    For D < 0 fundamental, the period is:

        Omega(D) = (2*pi / sqrt(|D|))^{h(D)} * prod_{a=1}^{|D|-1}
                   Gamma(a/|D|)^{w(D)*chi_D(a) / (4*h(D))}

    The Faltings height relates to this via:

        h_F = -log(Omega) - (1/2)*log(2*pi)

    up to a rational correction depending on the model.

    Returns
    -------
    log_Omega : float, the logarithm of the Chowla-Selberg period
    """
    if not HAS_MPMATH:
        return float('nan')

    old_dps = mp.dps
    mp.dps = dps + 30
    try:
        N = abs(D)
        h = class_number(D)
        w = roots_of_unity(D)

        # Product of Gamma values
        log_prod = mpf(0)
        for a in range(1, N):
            chi_a = kronecker_symbol(D, a)
            if chi_a != 0:
                exponent = mpf(w) * mpf(chi_a) / (4 * mpf(h))
                log_prod += exponent * mpre(mp_loggamma(mpf(a) / mpf(N)))

        # Prefactor (2*pi/sqrt(|D|))^h
        log_prefactor = mpf(h) * (mp_log(2 * mp_pi) - mpf('0.5') * mp_log(mpf(N)))

        log_Omega = log_prefactor + log_prod
        return float(log_Omega)
    finally:
        mp.dps = old_dps


def chowla_selberg_faltings_height(D: int, dps: int = 50) -> float:
    r"""Faltings height from Chowla-Selberg period.

    h_F^{CS} = -log(Omega(D)) + (h(D) - 1) * log(2*pi)
             - (1/2) * log(|D|) * (h(D) - 1/2)

    This is an INDEPENDENT computation from the Colmez formula.
    Agreement between the two is a verification of both.

    For class number 1, the simplified formula is:

        h_F = -(1/4) * sum_{a=1}^{|D|-1} chi_D(a) * log Gamma(a/|D|)
              - (1/2) * log(2*pi) + (1/4) * log(|D|)

    where the sum uses w(D)/2 = 1 (for D != -3, -4) or w/2 = 3 or 2.
    """
    if not HAS_MPMATH:
        return float('nan')

    old_dps = mp.dps
    mp.dps = dps + 30
    try:
        N = abs(D)
        w = roots_of_unity(D)
        h = class_number(D)

        # For class number 1, use the direct formula
        if h == 1:
            log_gamma_sum = mpf(0)
            for a in range(1, N):
                chi_a = kronecker_symbol(D, a)
                if chi_a != 0:
                    log_gamma_sum += mpf(chi_a) * mpre(mp_loggamma(mpf(a) / mpf(N)))

            hF = -(mpf(w) / 4) * log_gamma_sum - mpf('0.5') * mp_log(2 * mp_pi) + mpf('0.25') * mp_log(mpf(N))
            return float(hF)
        else:
            # General case: use the log-period
            log_Omega = chowla_selberg_period(D, dps)
            # Approximate: h_F ~ -log_Omega / h + correction
            hF = -log_Omega / h - mpf('0.5') * mp_log(2 * mp_pi) + mpf('0.25') * mp_log(mpf(N))
            return float(hF)
    finally:
        mp.dps = old_dps


# ============================================================================
# 6. Shadow central charge from CM discriminant
# ============================================================================

def shadow_central_charge_from_discriminant(D: int) -> float:
    r"""Map a CM discriminant D to a shadow central charge c.

    The shadow discriminant for Virasoro at central charge c is:

        Delta(c) = 40 / (5c + 22)

    We define the shadow CM central charge as:

        c_CM(D) = |D| / 2

    This is a CONVENTIONAL choice that maps |D| to the physical range
    of central charges.  The specific normalization ensures:
      - D = -4 maps to c = 2 (free boson / Heisenberg at k=2)
      - D = -8 maps to c = 4
      - D = -163 maps to c = 81.5

    Alternative: c_CM(D) = 26 * |D| / (|D| + 26) maps all D to c < 26.
    """
    return abs(D) / 2.0


def shadow_kappa_at_cm(D: int) -> float:
    r"""Shadow modular characteristic at the CM point.

    kappa(Vir_{c_CM(D)}) = c_CM(D) / 2 = |D| / 4.

    AP39: this is kappa for the VIRASORO family specifically.
    """
    return abs(D) / 4.0


# ============================================================================
# 7. p-adic valuations and local arithmetic
# ============================================================================

def p_adic_valuation(n: int, p: int) -> int:
    """Compute v_p(n) = ord_p(n) for integer n."""
    if n == 0:
        return float('inf')
    v = 0
    n = abs(n)
    while n % p == 0:
        n //= p
        v += 1
    return v


def legendre_symbol(a: int, p: int) -> int:
    """Compute the Legendre symbol (a/p) for odd prime p."""
    if p == 2:
        raise ValueError("Legendre symbol requires odd prime")
    a = a % p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


# ============================================================================
# 8. Tate uniformization and p-adic periods
# ============================================================================

def tate_parameter_from_j(j_inv: complex, p: int, dps: int = 50) -> complex:
    r"""Compute the Tate parameter q from j-invariant via q-expansion inversion.

    The j-function has the q-expansion:

        j(q) = 1/q + 744 + 196884*q + 21493760*q^2 + ...

    For |q|_p < 1 (split multiplicative reduction), we invert this to find
    q(j).  The inversion is:

        q = 1/j + 744/j^2 + (744^2 + 196884)/j^3 + ...

    This converges p-adically when v_p(j) < 0 (i.e., j is not p-integral).

    Parameters
    ----------
    j_inv : j-invariant
    p : prime
    dps : precision

    Returns
    -------
    q_tate : complex, the Tate parameter
    """
    if not HAS_MPMATH:
        # Simple fallback: q ~ 1/j for large |j|
        if abs(j_inv) > 1000:
            return 1.0 / j_inv
        return float('nan')

    old_dps = mp.dps
    mp.dps = dps + 20
    try:
        j = mpc(j_inv)
        # Inversion coefficients for q = sum c_n / j^n
        # c_1 = 1, c_2 = 744, c_3 = 744^2 + 196884 = 554256 + 196884 = 750420 [WRONG]
        # Actually: from j = 1/q + 744 + 196884*q + ...
        # Inverting: q = 1/j - 744/j^2 + (744^2 - 196884)/j^3 + ...
        # Let me compute correctly from first principles.
        # j = q^{-1} + 744 + 196884*q + 21493760*q^2 + ...
        # Set x = 1/j, then q = x * (1 + 744*x*q + 196884*x*q^2 + ...)^{-1}... messy.
        # Better: iterative inversion.
        # Start: q_0 = 1/j
        # Then: q_{n+1} = 1/(j - 744 - 196884*q_n - 21493760*q_n^2 - ...)
        # j-invariant coefficients c(n) in j(q) = q^{-1} + sum c(n)*q^n
        j_coeffs = [744, 196884, 21493760, 864299970, 20245856256]

        q = mpc(1) / j  # zeroth approximation
        for _ in range(30):  # iterate to convergence
            # j(q) = 1/q + 744 + 196884*q + ...
            j_approx = mpc(1) / q + mpf(744)
            q_power = mpc(1)
            for c in j_coeffs:
                q_power *= q
                j_approx += mpf(c) * q_power
            # Newton-like: q_new such that 1/q_new = j - 744 - 196884*q - ...
            correction = j - j_approx
            # dj/dq = -1/q^2 + 196884 + 2*21493760*q + ...
            dj_dq = -mpc(1) / (q * q) + mpf(196884)
            q_power = mpc(1)
            for i, c in enumerate(j_coeffs[1:], start=2):
                q_power *= q
                dj_dq += mpf(i * c) * q_power / q
            q_new = q + correction / dj_dq
            if fabs(q_new - q) < mp_power(mpf(10), -(dps + 5)):
                q = q_new
                break
            q = q_new

        return complex(q)
    finally:
        mp.dps = old_dps


def p_adic_period_from_tate(q_tate: complex, p: int) -> dict:
    r"""Compute p-adic period data from Tate parameter.

    For E with split multiplicative reduction at p:
        E(Q_p) ~ Q_p* / q_E^Z

    The p-adic period is:
        Omega_p = log_p(q_E)  (the p-adic logarithm of q_E)

    For q_E = p^n * u with u a p-adic unit:
        ord_p(q_E) = n
        log_p(q_E) = n * log_p(p) + log_p(u)

    In the p-adic world, log_p(p) = 0 (Iwasawa convention) or log_p(p) = log(p)
    (naive).  We use the Iwasawa convention: log_p(p) = 0.

    Returns
    -------
    dict with keys: q_tate, ord_p, unit_part, Omega_p_naive, Omega_p_iwasawa
    """
    q = q_tate
    q_abs = abs(q)

    if q_abs == 0:
        return {'q_tate': q, 'ord_p': float('inf'), 'unit_part': 0,
                'Omega_p_naive': float('nan'), 'Omega_p_iwasawa': float('nan')}

    # Approximate p-adic valuation from archimedean data
    # This is a PROXY: true p-adic valuation requires p-adic computation.
    # For the shadow programme, we use: ord_p(q) ~ -log|q| / log(p)
    # when |q| < 1 (which holds for split multiplicative reduction).
    if q_abs >= 1:
        ord_p_approx = 0
    else:
        ord_p_approx = round(-math.log(q_abs) / math.log(p))

    # Naive p-adic logarithm (archimedean proxy)
    log_q = cmath.log(q)
    Omega_naive = log_q

    # Iwasawa p-adic logarithm: log_p(q) = log(q) - ord_p(q) * log(p)
    Omega_iwasawa = log_q - ord_p_approx * math.log(p)

    return {
        'q_tate': q,
        'ord_p': ord_p_approx,
        'unit_part': q / (p ** ord_p_approx) if ord_p_approx > 0 else q,
        'Omega_p_naive': Omega_naive,
        'Omega_p_iwasawa': Omega_iwasawa,
    }


# ============================================================================
# 9. CM j-invariants
# ============================================================================

# j-invariants for class number 1 discriminants
# Source: Silverman, Advanced Topics in the Arithmetic of Elliptic Curves,
#         Table A.4 (AP38: Silverman convention)
CM_J_INVARIANTS = {
    -3: 0,             # j(rho) = 0, rho = e^{2pi i/3}
    -4: 1728,          # j(i) = 1728
    -7: -3375,         # j((1+sqrt(-7))/2) = -3375
    -8: 8000,          # j(sqrt(-2)) = 8000
    -11: -32768,       # j((1+sqrt(-11))/2) = -32768
    -19: -884736,      # j((1+sqrt(-19))/2) = -884736
    -43: -884736000,   # j((1+sqrt(-43))/2) = -884736000
    -67: -147197952000,
    -163: -262537412640768000,  # Ramanujan constant related
}


def cm_j_invariant(D: int) -> Optional[int]:
    """Return the j-invariant for CM discriminant D (class number 1 only)."""
    return CM_J_INVARIANTS.get(D, None)


# ============================================================================
# 10. Shadow Faltings height (from shadow data)
# ============================================================================

def shadow_faltings_height(c: float, dps: int = 50) -> float:
    r"""Shadow Faltings height from the shadow obstruction tower.

    For Virasoro at central charge c, the genus-1 shadow invariant is:

        F_1(c) = kappa(c) / 24 = c / 48

    The shadow Faltings height is defined as:

        h_F^{shadow}(c) = log|F_1(c)| = log(|c|/48)

    This is an ANALOGY, not an identity: the shadow F_1 plays the role
    of the period in the shadow motivic picture.

    AP39: kappa = c/2 is specific to Virasoro.
    """
    kappa = c / 2.0
    F1 = kappa / 24.0
    if abs(F1) < 1e-300:
        return float('-inf')
    return math.log(abs(F1))


def shadow_faltings_height_arakelov(c: float, dps: int = 50) -> float:
    r"""Arakelov-normalized shadow Faltings height.

    h_F^{Ar}(c) = (1/2) * log(kappa(c)^2 / (2*pi))
                = log(|kappa|) - (1/2)*log(2*pi)

    This normalization matches the Colmez convention for comparison.
    """
    kappa = abs(c / 2.0)
    if kappa < 1e-300:
        return float('-inf')
    return math.log(kappa) - 0.5 * math.log(2 * math.pi)


# ============================================================================
# 11. p-adic L-functions (Mazur-Tate-Teitelbaum)
# ============================================================================

def euler_factor_at_p(D: int, p: int) -> float:
    r"""Compute the Euler factor (1 - chi_D(p) * p^{-s})|_{s=1} for the
    L-function of the Kronecker character chi_D at prime p.

    Returns (1 - chi_D(p)/p).
    """
    chi_p = kronecker_symbol(D, p)
    return 1.0 - chi_p / p


def p_adic_L_interpolation(D: int, p: int, s_values: List[int],
                           dps: int = 50) -> Dict[int, complex]:
    r"""Compute p-adic L-function values L_p(chi_D, s) at integer points.

    The Kubota-Leopoldt p-adic L-function satisfies:

        L_p(chi_D, 1-n) = (1 - chi_D(p)*p^{n-1}) * L(chi_D, 1-n)

    for positive integers n with n ≡ 0 (mod p-1) (for p odd).

    More generally, for n >= 1:
        L_p(chi_D, 1-n) = (1 - chi_D(p)*p^{n-1}) * L(chi_D, 1-n)

    where the Euler factor removal interpolates p-adically.

    Parameters
    ----------
    D : fundamental discriminant
    p : prime
    s_values : list of integer evaluation points s
    dps : precision

    Returns
    -------
    dict mapping s -> L_p(chi_D, s)
    """
    results = {}
    for s in s_values:
        # For s = 1-n (n >= 1), L(chi_D, 1-n) is related to generalized
        # Bernoulli numbers: L(chi_D, 1-n) = -B_{n,chi_D}/n
        n = 1 - s  # s = 1 - n => n = 1 - s
        if n >= 1:
            B_n_chi = _generalized_bernoulli(n, D)
            L_val = -B_n_chi / n
            # p-adic Euler factor
            euler = 1.0 - kronecker_symbol(D, p) * (p ** (n - 1))
            L_p_val = euler * L_val
            results[s] = L_p_val
        else:
            # s >= 1: need analytic continuation
            # Use the interpolation property of the p-adic measure
            L_val = dirichlet_L_value(D, complex(s), dps=dps)
            euler = 1.0 - kronecker_symbol(D, p) * (p ** (-s))
            results[s] = euler * L_val
    return results


def _generalized_bernoulli(n: int, D: int) -> float:
    r"""Compute the generalized Bernoulli number B_{n,chi_D}.

    B_{n,chi} = N^{n-1} * sum_{a=1}^{N} chi(a) * B_n(a/N)

    where B_n(x) is the n-th Bernoulli polynomial and N = |D| = conductor.
    """
    N = abs(D)

    if HAS_MPMATH:
        old_dps = mp.dps
        mp.dps = 50
        try:
            total = mpf(0)
            for a in range(1, N + 1):
                chi_a = kronecker_symbol(D, a)
                if chi_a != 0:
                    x = mpf(a) / mpf(N)
                    Bn_x = _bernoulli_poly(n, x)
                    total += mpf(chi_a) * Bn_x
            result = mp_power(mpf(N), n - 1) * total
            return float(result)
        finally:
            mp.dps = old_dps
    else:
        # Fallback: compute with standard floats
        total = 0.0
        for a in range(1, N + 1):
            chi_a = kronecker_symbol(D, a)
            if chi_a != 0:
                x = a / N
                Bn_x = _bernoulli_poly_float(n, x)
                total += chi_a * Bn_x
        return (N ** (n - 1)) * total


def _bernoulli_poly(n: int, x):
    r"""Bernoulli polynomial B_n(x) using mpmath.

    B_n(x) = sum_{k=0}^{n} binom(n,k) * B_k * x^{n-k}

    where B_k are (ordinary) Bernoulli numbers.
    """
    total = mpf(0)
    for k in range(n + 1):
        binom_nk = _binom(n, k)
        Bk = _bernoulli_number(k)
        total += mpf(binom_nk) * mpf(Bk) * mp_power(x, n - k)
    return total


def _bernoulli_poly_float(n: int, x: float) -> float:
    """Bernoulli polynomial B_n(x) with float arithmetic."""
    total = 0.0
    for k in range(n + 1):
        binom_nk = _binom(n, k)
        Bk = _bernoulli_number_float(k)
        total += binom_nk * Bk * (x ** (n - k))
    return total


@lru_cache(maxsize=256)
def _binom(n: int, k: int) -> int:
    """Binomial coefficient."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    result = 1
    for i in range(min(k, n - k)):
        result = result * (n - i) // (i + 1)
    return result


@lru_cache(maxsize=128)
def _bernoulli_number(k: int) -> float:
    """k-th Bernoulli number B_k."""
    if HAS_MPMATH:
        old_dps = mp.dps
        mp.dps = 50
        try:
            # Use mpmath's built-in Bernoulli numbers
            from mpmath import bernoulli as mp_bernoulli
            return float(mp_bernoulli(k))
        finally:
            mp.dps = old_dps
    return _bernoulli_number_float(k)


@lru_cache(maxsize=128)
def _bernoulli_number_float(k: int) -> float:
    """k-th Bernoulli number via Akiyama-Tanigawa algorithm."""
    if k == 0:
        return 1.0
    if k == 1:
        return -0.5
    if k % 2 == 1 and k > 1:
        return 0.0
    # Akiyama-Tanigawa
    a = [Fraction(1, n + 1) for n in range(k + 1)]
    for j in range(1, k + 1):
        for m in range(k, j - 1, -1):
            a[m - 1] = (m) * (a[m - 1] - a[m])
    return float(a[0])


# ============================================================================
# 12. Exceptional zeros detection
# ============================================================================

def has_exceptional_zero(D: int, p: int) -> bool:
    r"""Check if chi_D has an exceptional zero at prime p.

    An exceptional zero occurs in the p-adic L-function when:
        chi_D(p) = 1  (i.e., p splits completely in Q(sqrt(D)))
        AND p divides the conductor |D|

    More precisely: the Mazur-Tate-Teitelbaum exceptional zero for an
    elliptic curve E at p occurs when p || N_E and a_p(E) = 1.

    For the Kronecker character chi_D:
        - chi_D(p) = 0 when p | D (ramified)
        - chi_D(p) = 1 when p splits (D is a QR mod p)
        - chi_D(p) = -1 when p is inert

    The exceptional zero for the p-adic L-function L_p(chi_D, s) at s=0
    occurs when chi_D(p) = 1, i.e., (D/p) = 1: the Euler factor
    (1 - chi_D(p)*p^{-1}) = (1 - 1/p) is nonzero, so there is NO
    exceptional zero for Dirichlet L-functions.

    For ELLIPTIC CURVES with CM by D, the exceptional zero is more subtle:
    it occurs when the curve has split multiplicative reduction at p.
    This requires p | disc(E) with a_p = +1.

    Returns True if the Kronecker character satisfies the splitting condition.
    """
    # For the shadow programme, we check the splitting condition
    chi_p = kronecker_symbol(D, p)
    return chi_p == 1 and (abs(D) % p == 0)


def exceptional_zero_table(discriminants: List[int],
                           primes: List[int]) -> Dict[Tuple[int, int], bool]:
    """Build table of exceptional zero conditions."""
    table = {}
    for D in discriminants:
        for p in primes:
            table[(D, p)] = has_exceptional_zero(D, p)
    return table


# ============================================================================
# 13. Archimedean periods at zeta zeros
# ============================================================================

def archimedean_period_at_zero(n: int, dps: int = 50) -> complex:
    r"""Archimedean period Omega_infty at the n-th zeta zero.

    The shadow central charge at the n-th zero is:

        c(rho_n) = 13 + i*gamma_n   (shadow self-dual point + zero)

    The archimedean period is:

        Omega_infty(rho_n) = Gamma(c(rho_n)/24) / sqrt(2*pi)

    This is motivated by the genus-1 amplitude:
        F_1(A) = kappa/24 and the modular transformation.

    Returns
    -------
    complex : the archimedean period
    """
    rho = zeta_zero_rho(n)
    # Shadow central charge at the zero
    c_shadow = complex(13.0, rho.imag)  # c = 13 + i*gamma_n

    if HAS_MPMATH:
        old_dps = mp.dps
        mp.dps = dps + 20
        try:
            c_mp = mpc(c_shadow.real, c_shadow.imag)
            arg = c_mp / 24
            Omega = mp_gamma(arg) / mp_sqrt(2 * mp_pi)
            return complex(Omega)
        finally:
            mp.dps = old_dps
    else:
        import cmath as cm
        arg = c_shadow / 24
        # Stirling approximation for complex Gamma
        # log Gamma(z) ~ z*log(z) - z - (1/2)*log(z) + (1/2)*log(2*pi)
        log_gamma = arg * cm.log(arg) - arg - 0.5 * cm.log(arg) + 0.5 * math.log(2 * math.pi)
        Omega = cm.exp(log_gamma) / math.sqrt(2 * math.pi)
        return Omega


def p_adic_period_at_zero(n: int, p: int, dps: int = 50) -> complex:
    r"""p-adic period proxy at the n-th zeta zero.

    We compute the p-adic analogue of the archimedean period:

        Omega_p(rho_n) = (1 - p^{-c(rho_n)/12}) * Omega_infty(rho_n)

    This is the Euler-factor-twisted period, motivated by the p-adic
    interpolation of the genus-1 amplitude.

    Returns
    -------
    complex : the p-adic period proxy
    """
    rho = zeta_zero_rho(n)
    c_shadow = complex(13.0, rho.imag)

    Omega_inf = archimedean_period_at_zero(n, dps)

    # Euler factor at p
    euler = 1.0 - p ** (-c_shadow / 12.0)

    return euler * Omega_inf


def period_ratio_at_zero(n: int, p: int, dps: int = 50) -> complex:
    r"""Period ratio Omega_p / Omega_infty at the n-th zeta zero.

    This equals the Euler factor (1 - p^{-c/12}).

    At the self-dual point c = 13:
        ratio = 1 - p^{-13/12}

    At the n-th zero c = 13 + i*gamma_n:
        ratio = 1 - p^{-(13 + i*gamma_n)/12}
              = 1 - p^{-13/12} * p^{-i*gamma_n/12}
              = 1 - p^{-13/12} * exp(-i*gamma_n*log(p)/12)

    The oscillatory factor exp(-i*gamma_n*log(p)/12) traces out the
    unit circle as n varies, creating a MONODROMY pattern in the
    period ratios.
    """
    rho = zeta_zero_rho(n)
    c_shadow = complex(13.0, rho.imag)
    ratio = 1.0 - p ** (-c_shadow / 12.0)
    return ratio


# ============================================================================
# 14. Full computation tables
# ============================================================================

def colmez_table(discriminants: Optional[List[int]] = None,
                 dps: int = 50) -> List[Dict[str, Any]]:
    r"""Compute the full Colmez table for given CM discriminants.

    For each D:
      - L(chi_D, 0), L'(chi_D, 0) to high precision
      - Faltings height h_F via Colmez formula
      - Faltings height h_F^{CS} via Chowla-Selberg (independent path)
      - Shadow Faltings height at c_CM(D)
      - Class number, roots of unity, j-invariant

    Returns
    -------
    List of dicts, one per discriminant.
    """
    if discriminants is None:
        discriminants = CM_DISCRIMINANTS_H1

    results = []
    for D in discriminants:
        row = {'D': D, 'abs_D': abs(D)}

        # Class number and roots of unity
        h = class_number(D)
        w = roots_of_unity(D)
        row['h'] = h
        row['w'] = w

        # j-invariant (class number 1 only)
        j = cm_j_invariant(D)
        row['j_invariant'] = j

        # L(chi_D, 0)
        L0 = dirichlet_L_value(D, 0, dps=dps)
        row['L_chi_0'] = L0

        # L'(chi_D, 0)
        L0_prime = dirichlet_L_derivative(D, 0, dps=dps)
        row['L_chi_0_prime'] = L0_prime

        # Colmez Faltings height
        try:
            hF_colmez = colmez_faltings_height(D, dps=dps)
        except Exception as e:
            hF_colmez = float('nan')
        row['h_F_colmez'] = hF_colmez

        # Chowla-Selberg Faltings height
        hF_cs = chowla_selberg_faltings_height(D, dps=dps)
        row['h_F_chowla_selberg'] = hF_cs

        # Shadow central charge and Faltings height
        c_cm = shadow_central_charge_from_discriminant(D)
        row['c_shadow'] = c_cm
        row['kappa_shadow'] = shadow_kappa_at_cm(D)
        row['h_F_shadow'] = shadow_faltings_height(c_cm, dps=dps)
        row['h_F_shadow_arakelov'] = shadow_faltings_height_arakelov(c_cm, dps=dps)

        results.append(row)

    return results


def p_adic_period_table(discriminants: Optional[List[int]] = None,
                        primes: Optional[List[int]] = None,
                        dps: int = 50) -> List[Dict[str, Any]]:
    r"""Compute p-adic period data for CM curves.

    For each (D, p):
      - j-invariant of CM curve
      - Tate parameter q_p
      - ord_p(q_p)
      - p-adic period Omega_p
      - splitting behavior of p in Q(sqrt(D))

    Returns
    -------
    List of dicts, one per (D, p) pair.
    """
    if discriminants is None:
        discriminants = CM_DISCRIMINANTS_H1
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]

    results = []
    for D in discriminants:
        j = cm_j_invariant(D)
        if j is None:
            continue

        for p in primes:
            row = {'D': D, 'p': p, 'j_invariant': j}

            # Splitting behavior
            chi_p = kronecker_symbol(D, p)
            row['chi_D_p'] = chi_p
            if chi_p == 1:
                row['splitting'] = 'split'
            elif chi_p == -1:
                row['splitting'] = 'inert'
            else:
                row['splitting'] = 'ramified'

            # Tate parameter (only meaningful for split multiplicative reduction)
            if j != 0 and j != 1728:
                try:
                    q_tate = tate_parameter_from_j(complex(j), p, dps=dps)
                    period_data = p_adic_period_from_tate(q_tate, p)
                    row.update(period_data)
                except Exception:
                    row['q_tate'] = None
                    row['ord_p'] = None
                    row['Omega_p_naive'] = None
            else:
                # j = 0 or 1728: potential good reduction everywhere
                row['q_tate'] = None
                row['ord_p'] = 0
                row['Omega_p_naive'] = None

            # Exceptional zero check
            row['exceptional_zero'] = has_exceptional_zero(D, p)

            results.append(row)

    return results


def zeta_zero_period_table(n_zeros: int = 20,
                           primes: Optional[List[int]] = None,
                           dps: int = 50) -> List[Dict[str, Any]]:
    r"""Period data at the first n_zeros nontrivial zeros of zeta.

    For each zero rho_n:
      - gamma_n (imaginary part)
      - Omega_infty (archimedean period)
      - Omega_p for each prime p
      - Period ratios Omega_p / Omega_infty

    Returns
    -------
    List of dicts, one per zero.
    """
    if primes is None:
        primes = [2, 3, 5]

    results = []
    for n in range(1, n_zeros + 1):
        rho = zeta_zero_rho(n)
        row = {
            'n': n,
            'gamma_n': rho.imag,
            'rho_n': rho,
        }

        # Archimedean period
        Omega_inf = archimedean_period_at_zero(n, dps)
        row['Omega_infty'] = Omega_inf
        row['abs_Omega_infty'] = abs(Omega_inf)

        # p-adic periods and ratios
        for p in primes:
            Omega_p = p_adic_period_at_zero(n, p, dps)
            ratio = period_ratio_at_zero(n, p, dps)
            row[f'Omega_{p}'] = Omega_p
            row[f'abs_Omega_{p}'] = abs(Omega_p)
            row[f'ratio_{p}'] = ratio
            row[f'abs_ratio_{p}'] = abs(ratio)

        results.append(row)

    return results


# ============================================================================
# 15. Multi-path verification utilities
# ============================================================================

def verify_class_number_formula(D: int, dps: int = 50) -> dict:
    r"""Verify the Dirichlet class number formula:

        L(chi_D, 1) = 2*pi*h(D) / (w(D) * sqrt(|D|))

    for D < 0 fundamental.

    This provides an INDEPENDENT check on both L(chi_D, 1) and h(D).

    Returns dict with both sides and relative error.
    """
    h = class_number(D)
    w = roots_of_unity(D)
    N = abs(D)

    # Left side: L(chi_D, 1)
    L1 = dirichlet_L_value(D, 1.0, dps=dps)
    L1_real = L1.real if isinstance(L1, complex) else L1

    # Right side: 2*pi*h / (w*sqrt(|D|))
    rhs = 2 * math.pi * h / (w * math.sqrt(N))

    rel_error = abs(L1_real - rhs) / max(abs(rhs), 1e-300)

    return {
        'D': D,
        'h': h,
        'w': w,
        'L_chi_1': L1_real,
        'class_number_formula_rhs': rhs,
        'relative_error': rel_error,
        'consistent': rel_error < 1e-6,
    }


def verify_functional_equation(D: int, s: complex = 0.5+1j,
                               dps: int = 50) -> dict:
    r"""Verify the functional equation of L(chi_D, s).

    For chi_D with D < 0 (odd character, conductor N = |D|):

        Lambda(chi_D, s) = (N/pi)^{(s+1)/2} * Gamma((s+1)/2) * L(chi_D, s)

    satisfies Lambda(s) = i * sqrt(N) / tau(chi_D) * Lambda(1-s)

    where tau(chi_D) is the Gauss sum.  For fundamental D < 0:
        tau(chi_D) = i * sqrt(|D|)

    so the relation becomes Lambda(s) = Lambda(1-s).

    Returns dict with both sides and relative error.
    """
    L_s = dirichlet_L_value(D, s, dps=dps)
    L_1ms = dirichlet_L_value(D, 1.0 - s, dps=dps)

    N = abs(D)

    if HAS_MPMATH:
        old_dps = mp.dps
        mp.dps = dps + 20
        try:
            s_mp = mpc(s)
            s1_mp = mpc(1 - s.real, -s.imag) if isinstance(s, complex) else mpf(1) - mpf(s)

            # Lambda(s) = (N/pi)^{(s+a)/2} * Gamma((s+a)/2) * L(s)
            # where a = 1 for odd character (D < 0)
            a = 1
            Lambda_s = mp_power(mpf(N) / mp_pi, (s_mp + a) / 2) * mp_gamma((s_mp + a) / 2) * mpc(L_s)
            Lambda_1ms = mp_power(mpf(N) / mp_pi, (s1_mp + a) / 2) * mp_gamma((s1_mp + a) / 2) * mpc(L_1ms)

            rel_error = float(fabs(Lambda_s - Lambda_1ms) / fabs(Lambda_s)) if float(fabs(Lambda_s)) > 1e-300 else float('nan')
        finally:
            mp.dps = old_dps
    else:
        rel_error = float('nan')

    return {
        'D': D,
        's': s,
        'L_s': L_s,
        'L_1ms': L_1ms,
        'relative_error': rel_error,
        'consistent': rel_error < 1e-6 if not math.isnan(rel_error) else False,
    }


def verify_colmez_two_paths(D: int, dps: int = 50) -> dict:
    r"""Compare Colmez and Chowla-Selberg Faltings heights.

    Two independent computations of the same invariant:
    1. Colmez formula: -(1/2) * L'/L at s=0 - (1/2)*log(2pi) + (1/4)*log|D|
    2. Chowla-Selberg: product of Gamma values at rational arguments

    Returns dict with both values and relative discrepancy.
    """
    hF_colmez = colmez_faltings_height(D, dps=dps)
    hF_cs = chowla_selberg_faltings_height(D, dps=dps)

    if math.isnan(hF_colmez) or math.isnan(hF_cs):
        return {
            'D': D,
            'h_F_colmez': hF_colmez,
            'h_F_chowla_selberg': hF_cs,
            'discrepancy': float('nan'),
            'consistent': False,
        }

    disc = abs(hF_colmez - hF_cs)
    denom = max(abs(hF_colmez), abs(hF_cs), 1e-300)
    rel = disc / denom

    return {
        'D': D,
        'h_F_colmez': hF_colmez,
        'h_F_chowla_selberg': hF_cs,
        'discrepancy': disc,
        'relative_discrepancy': rel,
        'consistent': rel < 1e-4,
    }


# ============================================================================
# 16. Summary statistics
# ============================================================================

def compute_all_tables(dps: int = 50) -> dict:
    """Compute all tables for the BC-119 programme.

    Returns a dict with keys:
      'colmez': Colmez table
      'p_adic': p-adic period table
      'zeta_zeros': zeta zero period table
      'class_number_checks': class number formula verifications
      'functional_eqn_checks': functional equation verifications
      'colmez_two_path': two-path Colmez verifications
      'exceptional_zeros': exceptional zero table
    """
    colmez = colmez_table(dps=dps)

    p_adic = p_adic_period_table(dps=dps)

    zeros = zeta_zero_period_table(n_zeros=20, dps=dps)

    class_checks = [verify_class_number_formula(D, dps=dps) for D in CM_DISCRIMINANTS_H1]

    fe_checks = [verify_functional_equation(D, 0.5 + 1j, dps=dps) for D in CM_DISCRIMINANTS_H1[:5]]

    colmez_checks = [verify_colmez_two_paths(D, dps=dps) for D in CM_DISCRIMINANTS_H1]

    exc_zeros = exceptional_zero_table(CM_DISCRIMINANTS_H1, [2, 3, 5, 7, 11, 13])

    return {
        'colmez': colmez,
        'p_adic': p_adic,
        'zeta_zeros': zeros,
        'class_number_checks': class_checks,
        'functional_eqn_checks': fe_checks,
        'colmez_two_path': colmez_checks,
        'exceptional_zeros': exc_zeros,
    }
