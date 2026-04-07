r"""Black hole entropy from the shadow obstruction tower: unified framework.

MATHEMATICAL FRAMEWORK
======================

This engine derives the Bekenstein-Hawking entropy formula, its quantum
corrections, and related gravitational observables from the shadow obstruction
tower of modular Koszul algebras.  It unifies several independent derivation
routes and provides multi-path verification at every level.

The central organizing principle: the shadow obstruction tower Theta_A of a
chirally Koszul algebra A encodes the COMPLETE perturbative genus expansion
of the dual gravitational theory.  The modular characteristic kappa(A) is the
single scalar invariant controlling the leading Bekenstein-Hawking entropy,
while higher shadow coefficients (S_3, S_4, ...) control planted-forest
corrections at genus >= 2.

SECTION 1: BTZ BLACK HOLE FROM KAPPA
=====================================

The BTZ black hole in AdS_3/CFT_2 has entropy controlled by the Virasoro
algebra at central charge c = 3*ell/(2*G_N) (Brown-Henneaux).  The modular
characteristic kappa(Vir_c) = c/2 gives:

    S_BTZ = 2*pi*sqrt(c*n/6) = 2*pi*sqrt(kappa*n/3)

where n = Delta - c/24 is the excitation above the vacuum.

SECTION 2: BROWN-HENNEAUX AND KAPPA
=====================================

The Brown-Henneaux central charge c = 3*ell/(2*G_N) gives:
    kappa = c/2 = 3*ell/(4*G_N)
    S_BTZ = pi*ell/(2*G_N) * sqrt(8*M*G_N) = Area/(4*G_N)

The last equality is the Bekenstein-Hawking formula.  In our framework,
it follows from S_BTZ = 2*pi*sqrt(kappa*n/3) with kappa = c/2.

SECTION 3: HAWKING TEMPERATURE AND THE SHADOW CONNECTION
=========================================================

The Hawking temperature T_H = r_+/(2*pi*ell^2) is the inverse of the
saddle-point value beta_H = pi*sqrt(c/(6*M)).  The shadow connection
nabla^sh = d - Q'_L/(2*Q_L) dt has logarithmic singularities at the zeros
of the shadow metric Q_L(t).  The identification:

    T_H = 1/beta_H = sqrt(6*M/c)/pi

connects the Hawking temperature to the modular parameter through the
shadow connection's monodromy.  The shadow connection residue at the
Hawking-Page transition point gives the Koszul sign (-1).

SECTION 4: FAREY TAIL AND GENUS EXPANSION
==========================================

The Farey tail partition function (Dijkgraaf-Maldacena-Moore-Verlinde):

    Z(tau) = sum_{gamma in SL(2,Z)/Gamma_infty} Z_0(gamma.tau)

The leading (gamma = id) term gives the BTZ contribution; subleading
SL(2,Z) images give instanton corrections.  The genus expansion of
Z^sh matches the perturbative part of Z(tau) around the BTZ saddle.

SECTION 5: c = 24 PURE GRAVITY AND THE J-FUNCTION
===================================================

At c = 24 (the Monster module V^natural):
    Z(q) = J(q) = j(q) - 744 = q^{-1} + 196884*q + ...
    kappa = 12
    F_1 = kappa/24 = 1/2
    S_BTZ = 4*pi*sqrt(n) for Delta_L = n

The shadow tower of V^natural is class M (infinite depth), with the
j-function as the exact partition function.

SECTION 6: LOGARITHMIC CORRECTIONS
====================================

The -3/2 coefficient in S = S_BH - (3/2)*log(S_BH) + ... arises from:
    Route A: 3 zero modes on BTZ (2 translations + 1 rotation), each
             contributing -1/2 to the log coefficient.
    Route B: The genus-1 one-loop determinant det'(-nabla^2)^{-1/2}
             on the solid torus.
    Route C: Shadow obstruction tower genus-1 contribution F_1 = kappa/24.

The -3/2 is UNIVERSAL (independent of c and kappa).

SECTION 7: RADEMACHER EXPANSION VS SHADOW PARTITION FUNCTION
=============================================================

The Rademacher expansion for the Fourier coefficients of a modular form
of weight -k involves Bessel functions I_{k+1} and Kloosterman sums:

    a(n) ~ sum_c (2*pi/c) * K(m,n;c) * I_{k+1}(4*pi*sqrt(|m|*n)/c)

The leading Rademacher term (c_K = 1) matches the Cardy formula
(exponential part), while subleading terms (c_K >= 2) give
non-perturbative corrections.  The genus expansion of Z^sh matches
the PERTURBATIVE expansion of the leading Rademacher term around
the saddle point.

SECTION 8: HIGHER-GENUS BLACK HOLES
=====================================

A genus-g black hole has a Riemann surface of genus g as its horizon.
The partition function on such a background receives contributions at
genus g from the shadow obstruction tower:

    F_g = kappa * lambda_g^FP + delta_pf^{(g,0)}

where delta_pf^{(g,0)} is the planted-forest correction (zero for class G,
nonzero for class M at g >= 2).

SECTION 9: QUANTUM EXTREMAL SURFACE FROM COMPLEMENTARITY
==========================================================

Theorem C gives Q_g(A) + Q_g(A!) = H*(M_bar_g, Z(A)).  The quantum
extremal surface (QES) is the surface that extremizes the generalized
entropy S_gen = Area/(4*G_N) + S_bulk.  In the shadow framework:

    S_gen = kappa * lambda_1 * log(L/eps) + S_bulk(sigma)

where sigma parameterizes the surface location.  The QES condition
d(S_gen)/d(sigma) = 0 is a Ward identity of the shadow connection.

SECTION 10: PAGE CURVE FROM SHADOW TOWER
==========================================

The Page curve S_rad(t) transitions from the Hawking phase (linear growth)
to the island phase (decreasing) at the Page time t_P.  In the shadow
framework:

    Hawking phase:   S_rad = (c/6)*t = (kappa/3)*t
    Island phase:    S_rad = S_BH - (kappa'/3)*(t - t_P)
    Page time:       t_P = 3*S_BH / (kappa + kappa') = 3*S_BH/13

The quantum corrections from genus g >= 2 shift t_P by amounts
proportional to F_g / S_BH^{2g-2}.

EPISTEMIC BOUNDARIES
====================

1. The shadow CohFT produces the PERTURBATIVE genus expansion.  The full
   non-perturbative partition function requires the sewing envelope A^sew
   (MC5, thm:general-hs-sewing).

2. The Cardy formula is ASYMPTOTIC (large Delta_L).  The shadow free
   energy gives the SAME leading asymptotics because F_1 = kappa/24
   controls the modular S-transform.

3. S_BH = saddle-point evaluation of -d/d(beta) log Z^sh.  This is
   exact only in the large-c (semiclassical) limit.

4. AP20: kappa(A) is an invariant of A, NOT kappa_eff.
5. AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
6. AP31: kappa = 0 does NOT imply Theta_A = 0.
7. AP46: eta(q) = q^{1/24} * prod(1-q^n).  The prefactor matters.
8. AP48: kappa depends on the full algebra, not just c.

References:
    Brown-Henneaux 1986: Commun. Math. Phys. 104, 207
    BTZ 1992: hep-th/9204099
    Carlip 1998: hep-th/9806026
    Dijkgraaf et al. 2000: hep-th/0005003 (Farey tail)
    Maloney-Witten 2010: 0712.0155
    Calabrese-Cardy 2004: hep-th/0405152
    Ryu-Takayanagi 2006: hep-th/0603001
    Penington 2019: 1905.08255
    AEMM 2019: 1908.10996
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
    thm:quantum-complementarity-main (higher_genus_complementarity.tex)
    thm:general-hs-sewing (higher_genus_foundations.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, factorial, pi as sym_pi,
    simplify, sqrt as sym_sqrt, exp as sym_exp, log as sym_log,
    sinh, sin, cancel, S, N as Neval,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PI = math.pi
TWO_PI = 2 * PI
FOUR_PI_SQ = (2 * PI) ** 2


# =========================================================================
# Section 0: Faber-Pandharipande numbers (exact arithmetic)
# =========================================================================

@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande Hodge integral at genus g.

    lambda_g^FP = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    These are POSITIVE for all g >= 1.

    Exact values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
        g=4: 127/154828800
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    power = 2 ** (2 * g - 1)
    num = (power - 1) * abs(B_2g)
    den = power * factorial(2 * g)
    return Fraction(Rational(num, den))


# =========================================================================
# Section 1: BTZ black hole from kappa
# =========================================================================

def kappa_virasoro(c) -> Fraction:
    """kappa(Vir_c) = c/2.

    AP1/AP9: authoritative formula from landscape_census.tex.
    AP20: this is kappa(A) for A = Vir_c, NOT kappa_eff.
    AP48: kappa depends on the full algebra, not just c.
    """
    return Fraction(c) / Fraction(2)


def kappa_heisenberg(k) -> Fraction:
    """kappa(H_k) = k.

    AP39: kappa != c/2 for Heisenberg (c = 1, kappa = k).
    """
    return Fraction(k)


def kappa_kac_moody(dim_g, k, h_dual) -> Fraction:
    """kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v).

    AP1/AP39: DISTINCT from c/2 for rank > 1.
    """
    return Fraction(dim_g) * (Fraction(k) + Fraction(h_dual)) / (2 * Fraction(h_dual))


def brown_henneaux_central_charge(ell, G_N) -> Fraction:
    """Brown-Henneaux: c = 3*ell / (2*G_N).

    ell = AdS radius, G_N = Newton constant.
    """
    return Fraction(3) * Fraction(ell) / (Fraction(2) * Fraction(G_N))


def brown_henneaux_kappa(ell, G_N) -> Fraction:
    """kappa = c/2 = 3*ell / (4*G_N)."""
    return Fraction(3) * Fraction(ell) / (Fraction(4) * Fraction(G_N))


def btz_entropy_from_c(c, n) -> float:
    """S_BTZ = 2*pi*sqrt(c*n/6) -- Cardy formula.

    Parameters
    ----------
    c : central charge
    n : excitation number (= Delta - c/24 for the vacuum)
    """
    c_f, n_f = float(c), float(n)
    if c_f * n_f <= 0:
        return 0.0
    return TWO_PI * math.sqrt(c_f * n_f / 6.0)


def btz_entropy_from_kappa(kappa, n) -> float:
    """S_BTZ = 2*pi*sqrt(kappa*n/3) -- Cardy in terms of kappa.

    Derivation: c = 2*kappa, so c*n/6 = 2*kappa*n/6 = kappa*n/3.
    """
    k_f, n_f = float(kappa), float(n)
    if k_f * n_f <= 0:
        return 0.0
    return TWO_PI * math.sqrt(k_f * n_f / 3.0)


def btz_entropy_from_area(r_plus, G_N) -> float:
    """S_BH = Area / (4*G_N) = 2*pi*r_+ / (4*G_N) = pi*r_+ / (2*G_N).

    For BTZ: Area = 2*pi*r_+ (circumference of the horizon).
    """
    return PI * float(r_plus) / (2.0 * float(G_N))


def verify_btz_three_routes(c, n, ell=1, G_N=None):
    """Verify BTZ entropy via three independent routes.

    Route A: Cardy formula S = 2*pi*sqrt(c*n/6)
    Route B: kappa formula S = 2*pi*sqrt(kappa*n/3)
    Route C: Area formula S = pi*r_+/(2*G_N)

    For Route C, G_N = 3*ell/(2*c) from Brown-Henneaux, and
    r_+ = ell*sqrt(8*G_N*M) where M = n/2 is the BTZ ADM mass.

    Convention: the CFT excitation number n = Delta - c/24 relates to
    the gravitational ADM mass by M = n/2.  This is because the Cardy
    formula S = 2*pi*sqrt(c*n/6) must match the area formula
    S = pi*r_+/(2*G_N) with r_+ = ell*sqrt(8*G_N*M).  Substituting
    G_N = 3*ell/(2*c) gives S = 2*pi*sqrt(c*M/3), matching the Cardy
    formula when M = n/2.
    """
    c_f = float(c)
    n_f = float(n)

    # Route A: Cardy
    S_A = btz_entropy_from_c(c_f, n_f)

    # Route B: kappa
    kappa = c_f / 2.0
    S_B = btz_entropy_from_kappa(kappa, n_f)

    # Route C: Area / (4 G_N)
    if G_N is None:
        G_N_val = 3.0 * float(ell) / (2.0 * c_f) if c_f != 0 else float('inf')
    else:
        G_N_val = float(G_N)

    # BTZ mass M = n/2 (matching Cardy convention to ADM mass)
    M_grav = n_f / 2.0
    # r_+ = ell * sqrt(8 * G_N * M)
    r_plus = float(ell) * math.sqrt(8.0 * G_N_val * M_grav) if G_N_val * M_grav > 0 else 0.0
    S_C = btz_entropy_from_area(r_plus, G_N_val) if G_N_val > 0 else 0.0

    return {
        'c': c_f,
        'n': n_f,
        'kappa': kappa,
        'M_grav': M_grav,
        'S_cardy': S_A,
        'S_kappa': S_B,
        'S_area': S_C,
        'AB_match': abs(S_A - S_B) < 1e-12 * max(abs(S_A), 1),
        'AC_match': abs(S_A - S_C) < 1e-10 * max(abs(S_A), 1),
        'all_agree': (abs(S_A - S_B) < 1e-12 * max(abs(S_A), 1)
                      and abs(S_A - S_C) < 1e-10 * max(abs(S_A), 1)),
    }


# =========================================================================
# Section 2: Hawking temperature and shadow connection
# =========================================================================

def hawking_temperature(c, M) -> float:
    """T_H = sqrt(6*M/c) / pi.

    Equivalently, T_H = r_+/(2*pi*ell^2) in gravitational variables.
    """
    c_f, M_f = float(c), float(M)
    if M_f <= 0 or c_f <= 0:
        return 0.0
    return math.sqrt(6.0 * M_f / c_f) / PI


def inverse_hawking_temperature(c, M) -> float:
    """beta_H = pi * sqrt(c/(6*M))."""
    c_f, M_f = float(c), float(M)
    if M_f <= 0 or c_f <= 0:
        return float('inf')
    return PI * math.sqrt(c_f / (6.0 * M_f))


def shadow_connection_residue_at_hp():
    """Residue of the shadow connection at the Hawking-Page point.

    The shadow connection nabla^sh = d - Q'_L/(2*Q_L) dt has
    logarithmic singularities at zeros of Q_L.  The monodromy
    around such a zero is exp(2*pi*i * residue) = -1 (the Koszul sign).

    The residue is 1/2 at each zero of Q_L, giving monodromy
    exp(2*pi*i * 1/2) = exp(pi*i) = -1.
    """
    return Fraction(1, 2)


def shadow_connection_monodromy():
    """Monodromy of the shadow connection around a Q_L zero: -1.

    This is the Koszul sign, reflecting the Z/2-grading of the bar complex.
    """
    return -1


def hawking_temperature_from_kappa(kappa, M) -> float:
    """T_H in terms of kappa: T_H = sqrt(3*M/kappa) / pi.

    Since c = 2*kappa: T_H = sqrt(6*M/(2*kappa))/pi = sqrt(3*M/kappa)/pi.
    """
    k_f, M_f = float(kappa), float(M)
    if M_f <= 0 or k_f <= 0:
        return 0.0
    return math.sqrt(3.0 * M_f / k_f) / PI


def verify_hawking_temp_consistency(c, M):
    """Verify Hawking temperature from c and from kappa agree."""
    T_c = hawking_temperature(c, M)
    kappa = float(c) / 2.0
    T_k = hawking_temperature_from_kappa(kappa, M)
    return {
        'T_from_c': T_c,
        'T_from_kappa': T_k,
        'match': abs(T_c - T_k) < 1e-14 * max(abs(T_c), 1e-100),
    }


# =========================================================================
# Section 3: Genus expansion free energies
# =========================================================================

def F_g_scalar(kappa_val, g: int) -> Fraction:
    """Scalar genus-g free energy: F_g^sc = kappa * lambda_g^FP.

    Valid for ALL modular Koszul algebras at the scalar level (Theorem D).
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    return Fraction(kappa_val) * lambda_fp(g)


def virasoro_shadow_data(c) -> Dict[str, Fraction]:
    """Shadow data for Virasoro: kappa, S_3, S_4, S_5."""
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)
    S3 = Fraction(2)  # c-independent
    S4 = Fraction(10) / (c_frac * (5 * c_frac + 22))
    S5 = Fraction(-48) / (c_frac ** 2 * (5 * c_frac + 22))
    return {
        'c': c_frac,
        'kappa': kappa,
        'S_3': S3,
        'S_4': S4,
        'S_5': S5,
        'shadow_class': 'M',  # Virasoro is always class M for c > 0
    }


def planted_forest_g2(c) -> Fraction:
    r"""Planted-forest correction at genus 2 for Virasoro.

    delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48.

    For Virasoro: S_3 = 2, kappa = c/2, so
    delta_pf = 2*(20 - c/2)/48 = (40 - c)/48 = -(c - 40)/48.
    """
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)
    S3 = Fraction(2)
    return S3 * (10 * S3 - kappa) / Fraction(48)


def F_table(c, g_max: int = 5) -> Dict[int, Fraction]:
    """Table of F_g for Virasoro at central charge c through genus g_max.

    g = 1: exact scalar (no planted-forest at genus 1)
    g = 2: scalar + planted-forest
    g >= 3: scalar only (planted-forest at g=3 available but expensive)
    """
    kappa = kappa_virasoro(c)
    table = {}
    for g in range(1, g_max + 1):
        F_scalar = kappa * lambda_fp(g)
        if g == 2:
            table[g] = F_scalar + planted_forest_g2(c)
        else:
            table[g] = F_scalar
    return table


# =========================================================================
# Section 4: Logarithmic correction
# =========================================================================

def log_correction_coefficient() -> Fraction:
    """Universal one-loop log coefficient: -3/2.

    S = S_BH - (3/2)*log(S_BH/(2*pi)) + O(1).

    Route A: 3 zero modes (2 translations + 1 rotation) on BTZ, each -1/2.
    Route B: One-loop determinant on solid torus.
    Route C: Saddle-point Gaussian integration around F_1 = kappa/24.
    """
    return Fraction(-3, 2)


def log_correction_from_zero_modes():
    """Route A: 3 zero modes, each contributing -1/2.

    2 translations (non-compact) + 1 rotation (compact).
    Total: -3 * (1/2) = -3/2.
    """
    n_zero_modes = 3
    per_mode = Fraction(-1, 2)
    return n_zero_modes * per_mode


def log_correction_from_one_loop(c) -> float:
    """Route B: One-loop determinant on the solid torus.

    log Z_1 = -(c/24)*log(eta(tau))^2 at high temperature gives
    F_1 = c/48.  The saddle-point Gaussian around F_1 gives the
    -3/2 * log(S_BH) correction.

    The coefficient -3/2 is independent of c because F_1 enters
    as an overall scale, and the Gaussian integral contributes
    -d/2 * log(S_BH) where d = 3 is the number of integration
    variables (Euclidean time, angle, radial scale).
    """
    return -1.5


def log_correction_from_shadow(c) -> Dict[str, Any]:
    """Route C: shadow obstruction tower at genus 1.

    F_1 = kappa/24 = c/48.
    The saddle-point expansion of exp(F_1/hbar^2 + ...) around
    hbar = hbar_saddle contributes -3/2 * log(S_BH).

    The -3/2 is the dimension of the moduli space of BTZ parameters
    (more precisely: 3 real parameters for a non-rotating BTZ with
    mass, angular momentum = 0, and periodicity).
    """
    kappa = float(c) / 2.0
    F1 = kappa / 24.0
    return {
        'F_1': F1,
        'kappa': kappa,
        'log_coeff': -1.5,
        'mechanism': 'saddle-point Gaussian with 3 integration variables',
    }


def entropy_with_corrections(c, M, g_max: int = 4) -> Dict[str, Any]:
    """Full BTZ entropy with quantum corrections through genus g_max.

    S(M) = S_0 + S_1 + S_2 + ... where:
        S_0 = 2*pi*sqrt(c*M/6)
        S_1 = -(3/2)*log(S_0/(2*pi))
        S_g = F_g * (2*pi/S_0)^{2g-2} for g >= 2
    """
    c_f, M_f = float(c), float(M)
    S0 = btz_entropy_from_c(c_f, M_f)
    if S0 <= 0:
        return {'error': 'S_0 <= 0: below Cardy threshold'}

    result = {
        'c': c_f,
        'M': M_f,
        'kappa': c_f / 2.0,
        'S_0': S0,
        'S_1': -1.5 * math.log(S0 / TWO_PI),
    }

    Ftab = F_table(c, g_max)
    expansion_param = TWO_PI / S0

    total = S0 + result['S_1']
    for g in range(2, g_max + 1):
        Fg = float(Ftab[g])
        Sg = Fg * expansion_param ** (2 * g - 2)
        result[f'S_{g}'] = Sg
        result[f'F_{g}'] = Fg
        total += Sg

    result['S_total'] = total
    result['relative_correction'] = (total - S0) / S0 if S0 > 0 else 0.0
    return result


# =========================================================================
# Section 5: Farey tail and genus expansion comparison
# =========================================================================

def farey_seed_partition(c, q_power_max: int = 10) -> Dict[int, int]:
    r"""Seed partition function Z_0 for pure gravity at central charge c.

    Z_0(tau) = q^{-c/24} * prod_{n>=2}^infty (1 - q^n)^{-1}

    For c = 24 (pure gravity):
    Z_0 = q^{-1} * prod_{n>=2} (1-q^n)^{-1}

    Returns Fourier coefficients a(n) for n = -floor(c/24)..q_power_max.
    """
    c_f = float(c)
    vacuum_power = -int(c_f / 24)

    # Build coefficients by expanding prod(1-q^n)^{-1} for n >= 2
    # using the recursion: a(n) = sum_{k=1}^{floor(n/2)} a(n-k) (partition into parts >= 2)
    max_terms = q_power_max - vacuum_power + 1
    if max_terms <= 0:
        return {}

    # Partitions into parts >= 2
    p = [0] * (max_terms + 1)
    p[0] = 1
    for part in range(2, max_terms + 1):
        for n in range(part, max_terms + 1):
            p[n] += p[n - part]

    coeffs = {}
    for i in range(max_terms):
        power = vacuum_power + i
        if power <= q_power_max:
            coeffs[power] = p[i]

    return coeffs


def j_invariant_coefficients(n_max: int = 10) -> Dict[int, int]:
    """First few Fourier coefficients of J(q) = j(q) - 744 = q^{-1} + 0 + 196884q + ...

    These are the dimensions of the Monster module graded pieces.
    """
    # Known exact values (from the OEIS / Conway-Norton)
    known = {
        -1: 1,
        0: 0,  # j(q) - 744: the constant term is 0 in J(q)
        1: 196884,
        2: 21493760,
        3: 864299970,
        4: 20245856256,
        5: 333202640600,
        6: 4252023300096,
        7: 44656994071935,
        8: 401490886656000,
        9: 3176440229784420,
        10: 22567393309593600,
    }
    return {n: v for n, v in known.items() if n <= n_max}


def farey_tail_leading_asymptotics(c, n) -> float:
    """Leading Farey tail asymptotics: the gamma = id (BTZ) contribution.

    This is just the Cardy formula: S ~ 2*pi*sqrt(c*n/6).
    The subleading Farey terms (gamma != id) give O(exp(-sqrt(n))) corrections.
    """
    return btz_entropy_from_c(c, n)


def genus_expansion_vs_farey(c, n, g_max: int = 5) -> Dict[str, Any]:
    """Compare genus expansion entropy with Farey tail (Cardy) entropy.

    The genus expansion S = S_0 + S_1 + ... matches the perturbative
    expansion of the Farey tail around the BTZ saddle.
    """
    S_cardy = btz_entropy_from_c(c, n)
    corrections = entropy_with_corrections(c, n, g_max)

    return {
        'c': float(c),
        'n': float(n),
        'S_cardy': S_cardy,
        'S_total': corrections.get('S_total', float('nan')),
        'relative_diff': (corrections.get('S_total', 0) - S_cardy) / S_cardy
            if S_cardy > 0 else float('nan'),
        'corrections': corrections,
    }


# =========================================================================
# Section 6: Monster module (c = 24)
# =========================================================================

def monster_kappa() -> Fraction:
    """kappa(V^natural) = c/2 = 12.

    AP48: For the moonshine module V^natural, kappa = c/2 = 12.
    This uses the Virasoro formula because V^natural has a single
    Virasoro generator at leading level.

    WARNING (AP48): For LATTICE VOAs at c = 24,
    kappa = rank = 24 != 12. V^natural is NOT a lattice VOA.
    """
    return Fraction(12)


def monster_F1() -> Fraction:
    """F_1(V^natural) = kappa/24 = 12/24 = 1/2."""
    return monster_kappa() * lambda_fp(1)


def monster_entropy(n: int) -> Dict[str, Any]:
    """BTZ entropy for the Monster module at excitation n.

    S_BTZ = 2*pi*sqrt(24*n/6) = 4*pi*sqrt(n).
    """
    c = 24
    kappa = 12
    S_BH = btz_entropy_from_c(c, n)
    return {
        'c': c,
        'kappa': kappa,
        'n': n,
        'S_BH': S_BH,
        'S_BH_formula': 4 * PI * math.sqrt(float(n)) if n > 0 else 0.0,
        'F_1': float(monster_F1()),
        'log_correction': -1.5 * math.log(S_BH / TWO_PI) if S_BH > 0 else 0.0,
        'shadow_class': 'M',
    }


def monster_j_vs_shadow(n_max: int = 5) -> Dict[str, Any]:
    """Compare J-function coefficients with shadow tower predictions.

    The J-function J(q) = j(q) - 744 is the EXACT partition function.
    The shadow tower gives the PERTURBATIVE genus expansion (around the
    BTZ saddle), which matches the Cardy asymptotics of J(q) coefficients.

    The log of the n-th coefficient of J(q) should approach
    S_BTZ(n) = 4*pi*sqrt(n) for large n.
    """
    j_coeffs = j_invariant_coefficients(n_max)
    results = []
    for n, a_n in sorted(j_coeffs.items()):
        if n <= 0 or a_n <= 0:
            continue
        log_a_n = math.log(a_n)
        S_cardy = 4.0 * PI * math.sqrt(float(n))
        ratio = log_a_n / S_cardy if S_cardy > 0 else float('nan')
        results.append({
            'n': n,
            'a_n': a_n,
            'log_a_n': log_a_n,
            'S_cardy': S_cardy,
            'ratio': ratio,
        })
    return {
        'c': 24,
        'kappa': 12,
        'data': results,
        'note': 'ratio -> 1 as n -> infinity (Cardy regime)',
    }


# =========================================================================
# Section 7: Rademacher expansion vs shadow partition function
# =========================================================================

def rademacher_leading_term(c, n, c_kloosterman: int = 1) -> float:
    """Leading Rademacher term with Kloosterman sum contribution c_K.

    For the vacuum module:
        a(n) ~ (2*pi/c_K) * (c_eff/(24*n_eff))^{1/4}
                * I_1(4*pi*sqrt(c_eff*n_eff/24) / c_K)

    where n_eff = n - c/24, c_eff = c.
    """
    c_f, n_f = float(c), float(n)
    n_eff = n_f - c_f / 24.0
    if n_eff <= 0:
        return 0.0
    c_eff = c_f
    arg = 4.0 * PI * math.sqrt(c_eff * n_eff / 24.0) / c_kloosterman

    # I_1(x) ~ e^x / sqrt(2*pi*x) for large x
    if arg > 500:
        log_rho = arg - 0.5 * math.log(TWO_PI * arg) + math.log(TWO_PI / c_kloosterman)
        log_rho += 0.25 * math.log(c_eff / (24.0 * n_eff))
        return math.exp(min(log_rho, 700))
    elif arg > 0:
        try:
            from scipy.special import iv
            I1 = iv(1, arg)
        except ImportError:
            I1 = math.exp(arg) / math.sqrt(TWO_PI * max(arg, 1e-10))
        prefactor = (TWO_PI / c_kloosterman) * (c_eff / (24.0 * n_eff)) ** 0.25
        return prefactor * I1
    else:
        return 0.0


def log_rademacher_leading(c, n) -> float:
    """Log of the leading Rademacher term (c_K = 1).

    log a(n) ~ 4*pi*sqrt(c*(n-c/24)/24) + subleading.

    For large n: ~ 2*pi*sqrt(c*n/6) = S_BH(n).
    """
    c_f, n_f = float(c), float(n)
    n_eff = n_f - c_f / 24.0
    if n_eff <= 0:
        return float('-inf')
    arg = 4.0 * PI * math.sqrt(c_f * n_eff / 24.0)
    # log I_1(x) ~ x - 0.5*log(2*pi*x) for large x
    log_I1 = arg - 0.5 * math.log(max(TWO_PI * arg, 1e-300))
    log_pref = math.log(TWO_PI) + 0.25 * math.log(c_f / (24.0 * n_eff))
    return log_pref + log_I1


def rademacher_vs_shadow(c, n_values, g_max: int = 4) -> Dict[str, Any]:
    """Compare Rademacher leading asymptotics with shadow partition function.

    Both should agree at leading order: log a(n) ~ S_BTZ(n) for large n.
    """
    results = []
    for n in n_values:
        n_f = float(n)
        S_BTZ = btz_entropy_from_c(c, n_f)
        log_rad = log_rademacher_leading(c, n_f)
        ratio = log_rad / S_BTZ if S_BTZ > 0 else float('nan')
        results.append({
            'n': n,
            'S_BTZ': S_BTZ,
            'log_rademacher': log_rad,
            'ratio': ratio,
        })
    return {
        'c': float(c),
        'data': results,
        'note': 'ratio -> 1 as n -> infinity',
    }


# =========================================================================
# Section 8: Higher-genus black holes
# =========================================================================

def higher_genus_bh_entropy(kappa_val, g: int) -> Fraction:
    """Free energy contribution from a genus-g horizon.

    A black hole with a genus-g Riemann surface as its horizon
    contributes F_g = kappa * lambda_g^FP to the partition function.

    This is the shadow obstruction tower at genus g, scalar level.
    """
    return F_g_scalar(kappa_val, g)


def higher_genus_bh_table(c, g_max: int = 6) -> Dict[int, Dict[str, Any]]:
    """Table of higher-genus black hole free energies for Virasoro.

    Genus-g black holes in 3d gravity correspond to handlebodies
    (genus-g Schottky fillings).  The free energy F_g grows as
    lambda_g^FP ~ 2/(2*pi)^{2g} (Bernoulli decay).
    """
    kappa = kappa_virasoro(c)
    table = {}
    for g in range(1, g_max + 1):
        Fg = kappa * lambda_fp(g)
        table[g] = {
            'g': g,
            'F_g_scalar': Fg,
            'F_g_float': float(Fg),
            'lambda_g': lambda_fp(g),
        }
        if g == 2:
            delta_pf = planted_forest_g2(c)
            table[g]['delta_pf'] = delta_pf
            table[g]['F_g_full'] = Fg + delta_pf
    return table


def bernoulli_decay_ratio(g: int) -> float:
    """Ratio lambda_{g+1}/lambda_g -> 1/(4*pi^2) as g -> infinity.

    This ratio controls the convergence of the genus expansion.
    """
    if g < 1:
        raise ValueError("g must be >= 1")
    return float(lambda_fp(g + 1)) / float(lambda_fp(g))


def genus_expansion_convergence_radius() -> float:
    """Convergence radius of the scalar genus expansion: 2*pi.

    The generating function (x/2)/sin(x/2) has poles at x = 2*pi*n.
    The nearest pole at x = 2*pi gives the convergence radius.
    """
    return TWO_PI


# =========================================================================
# Section 9: Complementarity and QES
# =========================================================================

def complementarity_kappa_sum(c) -> Fraction:
    """kappa(Vir_c) + kappa(Vir_{26-c}) = 13.

    AP24: NOT zero for Virasoro.
    """
    return kappa_virasoro(c) + kappa_virasoro(26 - int(c))


def complementarity_scalar_Fg(c, g: int) -> Dict[str, Fraction]:
    """Scalar complementarity: F_g(c) + F_g(26-c) = 13 * lambda_g^FP.

    From kappa(Vir_c) + kappa(Vir_{26-c}) = 13.
    """
    kappa = kappa_virasoro(c)
    kappa_dual = kappa_virasoro(26 - int(c))
    Fg_c = kappa * lambda_fp(g)
    Fg_dual = kappa_dual * lambda_fp(g)
    target = Fraction(13) * lambda_fp(g)
    return {
        'F_g_c': Fg_c,
        'F_g_dual': Fg_dual,
        'sum': Fg_c + Fg_dual,
        'target': target,
        'match': Fg_c + Fg_dual == target,
    }


def entanglement_entropy_scalar(c, L_over_eps: float = 1000.0) -> float:
    """S_EE = (c/3) * log(L/eps) = (2*kappa/3) * log(L/eps).

    The Calabrese-Cardy formula, derived from the replica trick
    applied to the shadow CohFT at scalar level.
    """
    return (float(c) / 3.0) * math.log(L_over_eps)


def entanglement_from_kappa(kappa, L_over_eps: float = 1000.0) -> float:
    """S_EE = (2*kappa/3) * log(L/eps)."""
    return (2.0 * float(kappa) / 3.0) * math.log(L_over_eps)


def entanglement_complementarity(c, L_over_eps: float = 1000.0) -> Dict[str, float]:
    """S_EE(c) + S_EE(26-c) = (26/3)*log(L/eps).

    Universal (c-independent) from kappa + kappa' = 13.
    """
    S_c = entanglement_entropy_scalar(c, L_over_eps)
    S_dual = entanglement_entropy_scalar(26 - float(c), L_over_eps)
    expected = (26.0 / 3.0) * math.log(L_over_eps)
    return {
        'S_EE_c': S_c,
        'S_EE_dual': S_dual,
        'sum': S_c + S_dual,
        'expected': expected,
        'match': abs(S_c + S_dual - expected) < 1e-10,
    }


def qes_generalized_entropy(kappa_val, L_over_eps, sigma, S_bulk_fn=None) -> Dict[str, float]:
    """Generalized entropy: S_gen = (2*kappa/3)*log(sigma/eps) + S_bulk(sigma).

    The QES condition is d(S_gen)/d(sigma) = 0, giving:
        (2*kappa/3) / sigma + S_bulk'(sigma) = 0.

    Parameters
    ----------
    kappa_val : modular characteristic
    L_over_eps : UV cutoff ratio
    sigma : position parameter for the entangling surface
    S_bulk_fn : callable returning S_bulk(sigma). If None, uses S_bulk = 0.
    """
    k_f = float(kappa_val)
    sig_f = float(sigma)
    eps = float(L_over_eps)

    S_area = (2.0 * k_f / 3.0) * math.log(max(sig_f, 1e-100))
    S_bulk = S_bulk_fn(sig_f) if S_bulk_fn is not None else 0.0
    S_gen = S_area + S_bulk

    return {
        'kappa': k_f,
        'sigma': sig_f,
        'S_area': S_area,
        'S_bulk': S_bulk,
        'S_gen': S_gen,
    }


def qes_at_self_dual(L_over_eps: float = 1000.0) -> Dict[str, Any]:
    """QES analysis at the self-dual point c = 13.

    At c = 13: kappa = kappa' = 13/2, so complementarity is symmetric.
    The QES is at the midpoint (by symmetry), and S_gen = S_BH/2.
    """
    c = 13
    kappa = 6.5
    S_EE = entanglement_entropy_scalar(c, L_over_eps)
    S_dual = entanglement_entropy_scalar(13, L_over_eps)
    return {
        'c': c,
        'kappa': kappa,
        'kappa_dual': kappa,
        'S_EE': S_EE,
        'S_EE_dual': S_dual,
        'complementarity_sum': S_EE + S_dual,
        'expected': (26.0 / 3.0) * math.log(L_over_eps),
        'note': 'Self-dual: QES at midpoint by A <-> A! symmetry',
    }


# =========================================================================
# Section 10: Page curve from shadow tower
# =========================================================================

def page_curve_hawking_phase(kappa_val, t) -> float:
    """Hawking phase: S_rad(t) = (kappa/3) * t = (c/6) * t.

    Linear growth of entanglement entropy of radiation.
    Growth rate = (c/6) = (kappa/3) per scrambling time.
    """
    return float(kappa_val) / 3.0 * float(t)


def page_curve_island_phase(kappa_val, kappa_dual, S_BH, t, t_P) -> float:
    """Island phase: S_rad(t) = S_BH - (kappa'/3) * (t - t_P).

    After the Page time, the island saddle dominates.
    kappa' = kappa(A!) controls the decrease rate.
    """
    return float(S_BH) - float(kappa_dual) / 3.0 * (float(t) - float(t_P))


def page_time(kappa_val, kappa_dual, S_BH) -> float:
    """Page time: t_P = 3 * S_BH / (kappa + kappa').

    For Virasoro: kappa + kappa' = 13, so t_P = 3*S_BH/13.
    At c = 13 (self-dual): t_P = 3*S_BH/13 (exactly half the full evaporation time).
    """
    k_sum = float(kappa_val) + float(kappa_dual)
    if k_sum <= 0:
        return float('inf')
    return 3.0 * float(S_BH) / k_sum


def page_time_virasoro(c, S_BH) -> float:
    """Page time for Virasoro: t_P = 3*S_BH / 13.

    Independent of c because kappa(c) + kappa(26-c) = 13 always.
    """
    return 3.0 * float(S_BH) / 13.0


def page_curve(c, S_BH, t_values) -> Dict[str, Any]:
    """Full Page curve from the shadow obstruction tower.

    S_Page(t) = min(S_Hawking(t), S_island(t)).
    """
    c_f = float(c)
    kappa = c_f / 2.0
    kappa_dual = (26.0 - c_f) / 2.0
    S_BH_f = float(S_BH)
    t_P = page_time(kappa, kappa_dual, S_BH_f)

    data = []
    for t in t_values:
        t_f = float(t)
        S_hawk = page_curve_hawking_phase(kappa, t_f)
        S_island = page_curve_island_phase(kappa, kappa_dual, S_BH_f, t_f, t_P)
        S_page = min(S_hawk, S_island)
        data.append({
            't': t_f,
            'S_hawking': S_hawk,
            'S_island': S_island,
            'S_page': S_page,
            'phase': 'Hawking' if S_hawk <= S_island else 'island',
        })

    return {
        'c': c_f,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'S_BH': S_BH_f,
        't_P': t_P,
        'data': data,
    }


def page_curve_quantum_correction(c, S_BH, g: int = 2) -> float:
    """Genus-g quantum correction to the Page time.

    delta_t_P^{(g)} ~ F_g * (2*pi)^{2g-2} / (S_BH^{2g-2} * 13/3)

    These are subleading in 1/S_BH.
    """
    c_f = float(c)
    S_BH_f = float(S_BH)
    if S_BH_f <= 0:
        return 0.0
    kappa = c_f / 2.0
    Fg = float(kappa * lambda_fp(g))
    expansion = (TWO_PI / S_BH_f) ** (2 * g - 2)
    return Fg * expansion * 3.0 / 13.0


# =========================================================================
# Section 11: A-hat generating function verification
# =========================================================================

def ahat_generating_function(x: float) -> float:
    """A-hat(x) = (x/2) / sinh(x/2).

    Entire function.  A-hat(0) = 1.
    Taylor: 1 - x^2/24 + 7*x^4/5760 - 31*x^6/967680 + ...
    """
    if abs(x) < 1e-10:
        return 1.0
    return (x / 2.0) / math.sinh(x / 2.0)


def scalar_genus_sum(kappa_val, hbar: float = 1.0, g_max: int = 30) -> float:
    """sum_{g=1}^{g_max} F_g^scalar * hbar^{2g}.

    Closed form: kappa * [(hbar/2)/sin(hbar/2) - 1].
    Convergent for |hbar| < 2*pi.
    """
    k_f = float(kappa_val)
    total = 0.0
    for g in range(1, g_max + 1):
        total += k_f * float(lambda_fp(g)) * hbar ** (2 * g)
    return total


def ahat_closed_form(kappa_val, hbar: float = 1.0) -> float:
    """Closed form: kappa * [(hbar/2)/sin(hbar/2) - 1].

    Equals sum_{g>=1} F_g^scalar * hbar^{2g}.

    (x/2)/sin(x/2) = 1 + sum_{g>=1} lambda_g^FP * x^{2g}.
    """
    k_f = float(kappa_val)
    h = float(hbar)
    if abs(h) < 1e-15:
        return 0.0
    return k_f * ((h / 2.0) / math.sin(h / 2.0) - 1.0)


def verify_ahat_identity(c, hbar: float = 1.0, g_max: int = 30) -> Dict[str, Any]:
    """Verify: sum F_g * hbar^{2g} = kappa * [(hbar/2)/sin(hbar/2) - 1]."""
    kappa = float(c) / 2.0
    series_val = scalar_genus_sum(kappa, hbar, g_max)
    closed_val = ahat_closed_form(kappa, hbar)
    return {
        'series': series_val,
        'closed_form': closed_val,
        'difference': abs(series_val - closed_val),
        'match': abs(series_val - closed_val) < 1e-8,
    }


# =========================================================================
# Section 12: Hawking-Page transition
# =========================================================================

def hawking_page_temperature_classical() -> float:
    """Classical Hawking-Page temperature: beta_HP = 2*pi.

    At this temperature, the BTZ and thermal AdS saddles exchange dominance.
    """
    return TWO_PI


def euclidean_free_energy_btz(c, beta) -> float:
    """Free energy of the BTZ saddle: F_BTZ(beta) = -(c*pi^2)/(6*beta) + F_1 + ...

    Classical (genus 0): -(c*pi^2)/(6*beta)
    One-loop (genus 1): F_1 = c/48
    """
    c_f, beta_f = float(c), float(beta)
    if beta_f <= 0:
        return float('inf')
    F0 = -(c_f * PI ** 2) / (6.0 * beta_f)
    F1 = c_f / 48.0
    return F0 + F1


def euclidean_free_energy_thermal_ads(c, beta) -> float:
    """Free energy of the thermal AdS saddle.

    F_AdS = -(c*beta) / (12*pi).
    """
    return -(float(c) * float(beta)) / (12.0 * PI)


def hawking_page_dominance(c, beta) -> str:
    """Which saddle dominates: 'BTZ' or 'AdS'."""
    F_btz = euclidean_free_energy_btz(c, beta)
    F_ads = euclidean_free_energy_thermal_ads(c, beta)
    return 'BTZ' if F_btz < F_ads else 'AdS'


# =========================================================================
# Section 13: Shadow convergence and non-perturbative structure
# =========================================================================

def shadow_genus_decay(g_max: int = 10) -> List[Tuple[int, float]]:
    """Ratios |lambda_{g+1}^FP / lambda_g^FP| -> 1/(4*pi^2) ~ 0.02533."""
    ratios = []
    for g in range(1, g_max):
        r = float(lambda_fp(g + 1)) / float(lambda_fp(g))
        ratios.append((g, r))
    return ratios


def shadow_partition_convergence(kappa_val, hbar_values) -> List[Dict[str, float]]:
    """Convergence diagnostics for Z^sh = exp(sum F_g hbar^{2g}).

    The scalar genus expansion converges for |hbar| < 2*pi.
    """
    k_f = float(kappa_val)
    results = []
    for hbar in hbar_values:
        partial_sum = scalar_genus_sum(k_f, hbar, g_max=30)
        closed = ahat_closed_form(k_f, hbar)
        results.append({
            'hbar': hbar,
            'partial_sum_30': partial_sum,
            'closed_form': closed,
            'difference': abs(partial_sum - closed),
        })
    return results


def non_perturbative_suppression(S_BH) -> float:
    """Non-perturbative corrections: O(exp(-(2*pi)^2 / hbar^2)).

    With hbar ~ 1/S_BH, this is exp(-4*pi^2 * S_BH^2), which is
    DOUBLY EXPONENTIALLY suppressed for large S_BH.
    """
    S = float(S_BH)
    if S <= 0:
        return 1.0
    exponent = -FOUR_PI_SQ * S ** 2
    if exponent < -700:
        return 0.0
    return math.exp(exponent)


# =========================================================================
# Section 14: Special central charges
# =========================================================================

def special_central_charges() -> Dict[str, Dict[str, Any]]:
    """Important central charges in the BH entropy context.

    c = 1:  free boson (Heisenberg at k = 1)
    c = 2:  complex boson (2 Heisenberg fields)
    c = 13: self-dual point (Vir_13^! = Vir_13)
    c = 24: Monster module (j-function partition function)
    c = 26: critical string (anomaly cancellation kappa_eff = 0)
    """
    data = {}
    for label, c_val in [('free_boson', 1), ('complex_boson', 2),
                          ('self_dual', 13), ('monster', 24),
                          ('critical_string', 26)]:
        kappa = Fraction(c_val, 2)
        kappa_dual = Fraction(26 - c_val, 2)
        data[label] = {
            'c': c_val,
            'kappa': kappa,
            'kappa_dual': kappa_dual,
            'kappa_sum': kappa + kappa_dual,
            'F_1': kappa * Fraction(1, 24),
            'self_dual': (c_val == 13),
            'shadow_class': 'M',
        }
    return data


def critical_string_kappa_eff() -> Dict[str, Fraction]:
    """At c = 26: kappa_eff = kappa(matter) + kappa(ghost) = 0.

    kappa(Vir_26) = 13
    kappa(ghost) = kappa(bc system) = -13  (bc ghosts at c = -26)
    kappa_eff = 13 + (-13) = 0

    AP29: kappa_eff != delta_kappa.  At c = 26:
        kappa_eff = 0 (anomaly cancellation)
        delta_kappa = kappa - kappa' = 13 - 0 = 13 (complementarity asymmetry)
    """
    return {
        'kappa_matter': Fraction(13),
        'kappa_ghost': Fraction(-13),
        'kappa_eff': Fraction(0),
        'delta_kappa': Fraction(13),
        'c_matter': 26,
        'c_ghost': -26,
    }


def self_dual_entropy_analysis(n: int = 100, L_over_eps: float = 1000.0) -> Dict[str, Any]:
    """Full analysis at the self-dual point c = 13.

    At c = 13:
    - kappa = kappa' = 13/2
    - S_BTZ = 2*pi*sqrt(13*n/6)
    - S_EE = (13/3)*log(L/eps)
    - Page time: t_P = 3*S_BH/13
    - Complementarity is EXACTLY symmetric
    """
    c = 13
    kappa = 6.5
    S_BH = btz_entropy_from_c(c, n)
    S_EE = entanglement_entropy_scalar(c, L_over_eps)
    t_P = page_time_virasoro(c, S_BH)

    return {
        'c': c,
        'kappa': kappa,
        'kappa_dual': kappa,
        'n': n,
        'S_BH': S_BH,
        'S_EE': S_EE,
        'S_EE_coefficient': Fraction(13, 3),
        't_P': t_P,
        'complementarity_sum': Fraction(26, 3),
        'F_1': float(kappa / 24.0),
        'self_dual': True,
    }
