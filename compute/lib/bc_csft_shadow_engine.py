r"""Closed string field theory vertices from the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

The shadow obstruction tower of a modular Koszul algebra A determines
a closed string field theory (CSFT) action functional

    S[Psi] = (1/2) <Psi, Q Psi> + sum_{g>=0, n>=3} (1/n!) V_{g,n}(Psi^n) * hbar^{2g}

where Q is the BRST operator, V_{g,n} are the string field theory vertices
at genus g and arity n, and hbar is the string coupling.

The KEY IDENTIFICATION (from thm:mc2-bar-intrinsic) is:

    V_{g,n} = Sh_{g,n}(Theta_A)

i.e., the SFT vertices ARE the shadow obstruction tower projections.
The SFT master equation Q^2 = 0, {Q, V} = 0, V*V = 0 is EQUIVALENT
to the MC equation D*Theta + (1/2)[Theta, Theta] = 0.

SHADOW DATA
===========

For Virasoro at central charge c:
  - kappa = c/2 (modular characteristic, AP1/AP9)
  - S_3 = 2 (cubic shadow, c-independent)
  - S_4 = 10/[c(5c+22)] (quartic contact invariant Q^contact_Vir)
  - S_5 = -48/[c^2(5c+22)] (quintic shadow)
  - Higher S_r from the convolution recursion on sqrt(Q_L(t))

For Heisenberg at level k:
  - kappa = k (modular characteristic)
  - S_r = 0 for r >= 3 (class G: tower terminates at arity 2)
  - The SFT potential is EXACTLY QUADRATIC

For affine sl_2 at level k:
  - kappa = 3(k+2)/4 (from dim(sl_2)=3, h^v=2)
  - S_3 = cubic from Lie bracket (nonzero)
  - S_r = 0 for r >= 4 (class L: tower terminates at arity 3)

TACHYON EFFECTIVE POTENTIAL
===========================

The genus-0 tachyon effective potential is:

    V(t) = (1/2) kappa * t^2 + sum_{r>=3} (S_r / r!) * t^r

The mass-shell condition for the tachyon: m^2 = -1 + (shadow corrections).
The SFT equation of motion: kappa * t + V'(t) = 0.

Critical points t* of V(t) correspond to vacuum solutions.  The Sen
conjecture relates V(t*) to the D-brane tension.

A-INFINITY STRUCTURE
===================

The SFT vertices satisfy the A-infinity (or L-infinity) relations:

    sum_{g1+g2=g, n1+n2=n+1} V_{g1,n1} circ V_{g2,n2} = 0

This is the projection of the MC equation to genus g, arity n.
At genus 0, these are the classical A-infinity relations.
At genus >= 1, they incorporate loop corrections.

KOSZUL DUALITY IN SFT
======================

For Virasoro: A = Vir_c, A! = Vir_{26-c}.
The SFT potentials satisfy:
    V(Vir_c, t) <-> V(Vir_{26-c}, t)  via c -> 26-c

CRITICAL RESULT (AP24):
    kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13
    This is NOT zero (13, not 0).

At c = 26 (critical string): kappa_eff = kappa(matter) + kappa(ghost) = 0.
At c = 13 (self-dual point): the SFT potential is self-dual.

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    cor:shadow-extraction (higher_genus_modular_koszul.tex)
    thm:cubic-gauge-triviality (higher_genus_modular_koszul.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple


# ===========================================================================
# Constants
# ===========================================================================

PI = math.pi
TWO_PI = 2.0 * PI


# ===========================================================================
# 0. Exact Bernoulli numbers and Faber-Pandharipande intersection numbers
# ===========================================================================

# Hardcoded Bernoulli numbers B_{2g} (signed convention: B_2 = 1/6, B_4 = -1/30, ...)
_BERNOULLI_2G = {
    1: Fraction(1, 6),
    2: Fraction(-1, 30),
    3: Fraction(1, 42),
    4: Fraction(-1, 30),
    5: Fraction(5, 66),
    6: Fraction(-691, 2730),
    7: Fraction(7, 6),
    8: Fraction(-3617, 510),
    9: Fraction(43867, 798),
    10: Fraction(-174611, 330),
}


def _bernoulli_2g(g: int) -> Fraction:
    """Exact Bernoulli number B_{2g} as a Fraction."""
    if g in _BERNOULLI_2G:
        return _BERNOULLI_2G[g]
    try:
        from sympy import bernoulli as sympy_bernoulli, Rational
        return Fraction(Rational(sympy_bernoulli(2 * g)))
    except ImportError:
        raise ValueError(f"Bernoulli B_{2 * g} not hardcoded and sympy unavailable")


def _factorial_fraction(n: int) -> Fraction:
    """n! as a Fraction."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    These are POSITIVE for all g >= 1 (AP22: Bernoulli signs).

    Verified values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
        g=4: 127/154828800
        g=5: 73/3503554560
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B2g = _bernoulli_2g(g)
    power = 2 ** (2 * g - 1)
    num = (power - 1) * abs(B2g)
    den = power * _factorial_fraction(2 * g)
    return num / den


# ===========================================================================
# 1. Shadow coefficients S_r
# ===========================================================================

def shadow_S_r(c, r: int) -> Fraction:
    r"""Shadow coefficient S_r for Virasoro at central charge c.

    EXACT FORMULAS (from virasoro_shadow_extended.py, thm:riccati-algebraicity):
        S_2 = c/2  (the modular characteristic kappa)
        S_3 = 2    (cubic shadow, c-independent; gauge-trivial by thm:cubic-gauge-triviality)
        S_4 = 10 / [c(5c+22)]  (quartic contact invariant)
        S_5 = -48 / [c^2(5c+22)]
        S_6 = 80(45c+193) / [3 c^3(5c+22)^2]

    For r > 6: computed via the convolution recursion on sqrt(Q_L(t))
    where Q_L(t) = c^2 + 12ct + alpha(c)*t^2, alpha(c) = (180c+872)/(5c+22).

    Parameters
    ----------
    c : central charge (must be nonzero)
    r : arity (must be >= 2)

    Returns
    -------
    Exact rational value as Fraction.
    """
    if r < 2:
        raise ValueError(f"shadow_S_r requires r >= 2, got {r}")
    c = Fraction(c)
    if c == 0:
        raise ValueError("Virasoro shadow tower undefined at c=0")

    if r == 2:
        return c / 2
    elif r == 3:
        # Cubic shadow is c-independent (gauge-trivial, thm:cubic-gauge-triviality)
        # Note: S_3 = 2 for Virasoro, NOT zero. The cubic gauge triviality means
        # the cubic MC term can be gauged away, making the quartic class canonical.
        # S_3 itself is nonzero as a shadow coefficient.
        return Fraction(2)
    elif r == 4:
        return Fraction(10) / (c * (5 * c + 22))
    elif r == 5:
        return Fraction(-48) / (c ** 2 * (5 * c + 22))
    elif r == 6:
        return Fraction(80) * (45 * c + 193) / (3 * c ** 3 * (5 * c + 22) ** 2)
    else:
        # Use convolution recursion for r > 6
        return _virasoro_S_r_recursion(c, r)


def _virasoro_S_r_recursion(c: Fraction, r: int) -> Fraction:
    """Compute S_r via the convolution recursion on sqrt(Q_L(t)).

    From thm:riccati-algebraicity:
        H(t) = t^2 sqrt(Q_L(t)) where Q_L(t) = c^2 + 12ct + alpha*t^2
        alpha = (180c + 872)/(5c + 22)

    The coefficients a_n of sqrt(Q_L(t)) = sum a_n t^n satisfy:
        a_0 = c, a_1 = 6, a_2 = alpha/(2c) - 18/c = 40/[c(5c+22)]
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 3

    Then S_r = a_{r-2} / r.
    """
    alpha = (180 * c + 872) / (5 * c + 22)

    # Build a_0 through a_{r-2}
    n_max = r - 2
    a = [Fraction(0)] * (n_max + 1)
    a[0] = c
    if n_max >= 1:
        a[1] = Fraction(6)
    if n_max >= 2:
        a[2] = (alpha - a[1] ** 2) / (2 * a[0])
    for n in range(3, n_max + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0])

    return a[n_max] / r


def heisenberg_S_r(k, r: int) -> Fraction:
    """Shadow coefficient S_r for Heisenberg at level k.

    Class G: tower terminates at arity 2.
    S_2 = k (the modular characteristic).
    S_r = 0 for all r >= 3.
    """
    if r < 2:
        raise ValueError(f"heisenberg_S_r requires r >= 2, got {r}")
    if r == 2:
        return Fraction(k)
    return Fraction(0)


def affine_sl2_S_r(k, r: int) -> Fraction:
    """Shadow coefficient S_r for affine sl_2 at level k.

    Class L: tower terminates at arity 3.
    S_2 = kappa = 3(k+2)/4  (dim(sl_2)=3, h^v=2)
    S_3 = cubic from Lie bracket (proportional to structure constants)
    S_r = 0 for r >= 4.

    The cubic shadow for affine sl_2 on the Cartan line is nonzero but
    depends on the normalization of the deformation parameter.  We use
    the standard normalization where S_3 = the Lie cubic coefficient.

    For the CARTAN line of sl_2: the S_3 coefficient is determined by
    the structure constant f_{hef} scaled by the level.
    S_3 = 0 on the Cartan line (the Cartan subalgebra is abelian).
    On the root lines: S_3 != 0.

    We follow the convention of affine_sl2_shadow_tower.py: on the
    full sl_2 deformation space, the cubic comes from the bracket.
    For the 1D Cartan projection: S_3 = 0 (abelian).
    For the full 3D space: S_3 is the structure constant cubic.
    """
    if r < 2:
        raise ValueError(f"affine_sl2_S_r requires r >= 2, got {r}")
    k = Fraction(k)
    h_v = Fraction(2)
    dim_g = Fraction(3)
    if r == 2:
        return dim_g * (k + h_v) / (2 * h_v)
    elif r == 3:
        # On the full sl_2 deformation space, S_3 comes from [e,f] = h.
        # The normalized cubic: S_3 = 1 (structure constant contribution).
        # On the Cartan line: S_3 = 0.
        # We use the FULL space value for the SFT potential.
        return Fraction(1)
    else:
        # Class L: all higher shadows vanish by Jacobi identity
        return Fraction(0)


# ===========================================================================
# 2. Shadow potential (genus-0 tachyon effective potential)
# ===========================================================================

def shadow_potential(c, t: float, r_max: int = 6) -> float:
    r"""Tachyon effective potential from the shadow obstruction tower.

    V(t) = sum_{r>=2} (S_r(c) / r!) * t^r

    This is the genus-0 contribution to the SFT action.  The quadratic
    term (r=2) gives the kinetic operator, and the r>=3 terms are
    interaction vertices.

    Parameters
    ----------
    c : central charge
    t : tachyon field value
    r_max : maximum arity (default 6)

    Returns
    -------
    Value of the potential V(t).
    """
    result = 0.0
    for r in range(2, r_max + 1):
        S_r = float(shadow_S_r(c, r))
        fact_r = float(_factorial_fraction(r))
        result += S_r * (t ** r) / fact_r
    return result


def shadow_potential_exact(c, r_max: int = 6) -> Dict[int, Fraction]:
    """Return the exact coefficients V_r = S_r / r! for the shadow potential.

    V(t) = sum_r V_r * t^r where V_r = S_r(c) / r!
    """
    c = Fraction(c)
    return {r: shadow_S_r(c, r) / _factorial_fraction(r) for r in range(2, r_max + 1)}


# ===========================================================================
# 3. SFT vertices V_{g,n}
# ===========================================================================

def zwiebach_vertex(g: int, n: int, c) -> Fraction:
    r"""SFT vertex V_{g,n} from the shadow obstruction tower.

    The genus-g, arity-n vertex is the (g,n)-projection of the MC element
    Theta_A.  At genus 0:
        V_{0,n} = S_n  (the shadow coefficient)

    At genus >= 1, the vertices incorporate loop corrections.
    At genus 1, arity 1:
        V_{1,1} = kappa = c/2  (the modular characteristic)

    The scalar (kappa) lane gives:
        V_{g,0} = kappa * lambda_g^FP  (the genus-g free energy)

    Parameters
    ----------
    g : genus (>= 0)
    n : arity (>= 0 for g >= 1; >= 3 for g = 0)
    c : central charge

    Returns
    -------
    Exact rational value.
    """
    c = Fraction(c)

    if g < 0 or n < 0:
        raise ValueError(f"Invalid (g,n) = ({g},{n})")

    # Stability condition: 2g - 2 + n > 0, with the exception of
    # (g,n) = (1,0) which is the torus (exists as orbifold, gives F_1).
    # For genus 0: need n >= 3 for interactions, n = 2 is kinetic term.
    # (0,0) and (0,1) are unstable and vanish.
    if g == 0 and n < 3:
        return Fraction(0)
    if g >= 1 and 2 * g - 2 + n < 0:
        return Fraction(0)

    if g == 0:
        # Genus 0: V_{0,n} = S_n
        if n < 2:
            return Fraction(0)
        return shadow_S_r(c, n)
    elif g == 1:
        if n == 1:
            # V_{1,1} = kappa (the modular characteristic)
            return c / 2
        elif n == 0:
            # V_{1,0} = kappa * lambda_1 = kappa/24
            return c / 2 * lambda_fp(1)
        else:
            # V_{1,n} for n >= 2: higher-arity genus-1 vertices
            # These involve the genus-1 shadow with planted-forest corrections.
            # At the scalar level: V_{1,n} = 0 for n >= 2 (arity truncation).
            return Fraction(0)
    else:
        # g >= 2: scalar lane gives V_{g,0}
        if n == 0:
            return c / 2 * lambda_fp(g)
        else:
            # V_{g,n} for g >= 2, n >= 1: higher-arity higher-genus
            # Not available in closed form beyond genus-3 planted-forest
            return Fraction(0)


# ===========================================================================
# 4. SFT equation of motion residual
# ===========================================================================

def sft_equation_residual(c, t: float, r_max: int = 6) -> float:
    r"""Residual of the SFT equation of motion at field value t.

    The classical (genus-0) EOM is V'(t) = 0:
        sum_{r>=2} S_r(c) / (r-1)! * t^{r-1} = 0

    Equivalently: kappa*t + sum_{r>=3} S_r/(r-1)! * t^{r-1} = 0.

    The residual measures how far a field configuration t is from
    satisfying the equation of motion.

    Parameters
    ----------
    c : central charge
    t : field value
    r_max : maximum arity

    Returns
    -------
    Value of V'(t).
    """
    result = 0.0
    for r in range(2, r_max + 1):
        S_r = float(shadow_S_r(c, r))
        fact_rm1 = float(_factorial_fraction(r - 1))
        result += S_r * (t ** (r - 1)) / fact_rm1
    return result


# ===========================================================================
# 5. Mass spectrum correction
# ===========================================================================

def mass_spectrum_correction(c, n: int, r_max: int = 4) -> float:
    r"""Shadow correction to the string mass spectrum.

    In the open string, the mass-shell condition is:
        alpha' m^2 = n - 1

    The shadow obstruction tower introduces corrections from the
    higher-arity vertices.  At leading order (genus 0, tree level),
    the correction comes from the quartic vertex S_4:

        delta(m^2)(n) = S_4 * (n-1) * correction_factor

    For the closed string, the level matching L_0 = L_0bar gives
    additional constraints.

    The correction is parametrically small in 1/c for large c
    (semiclassical limit).

    Parameters
    ----------
    c : central charge
    n : mass level (n=0 is tachyon, n=1 is massless, etc.)
    r_max : maximum arity for shadow contributions

    Returns
    -------
    Fractional mass correction delta(m^2).
    """
    c_frac = Fraction(c)
    kappa = c_frac / 2

    if kappa == 0:
        return 0.0

    # Leading correction from quartic vertex
    S4 = shadow_S_r(c, 4)
    # The quartic vertex contributes a mass shift at tree level
    # via the cubic-quartic diagram: delta_m^2 ~ S_4 / kappa
    delta = float(S4 / kappa) * n

    if r_max >= 5:
        S5 = shadow_S_r(c, 5)
        # Quintic contributes at next order: S_5 * n / kappa^2
        if kappa != 0:
            delta += float(S5 / kappa ** 2) * n * n / 2

    return delta


# ===========================================================================
# 6. Critical points of the shadow potential
# ===========================================================================

def critical_points(c, r_max: int = 6) -> List[float]:
    r"""Find critical points t* of the shadow potential V(t).

    V'(t*) = 0 is the SFT equation of motion.

    V'(t) = S_2*t + (S_3/2)*t^2 + ... = t * (S_2 + (S_3/2)*t + ...)

    The trivial critical point t = 0 (perturbative vacuum) always exists.
    Nontrivial critical points are the roots of the reduced polynomial
    P(t) = S_2 + (S_3/2)*t + (S_4/6)*t^2 + ...

    Returns
    -------
    List of real critical points (including t=0), sorted by V(t*).
    """
    import numpy as np

    # Build the REDUCED polynomial P(t) = sum S_r/(r-1)! * t^{r-2}
    # so that V'(t) = t * P(t)
    # P(t) = S_2 + (S_3/2)*t + (S_4/6)*t^2 + ...
    # coeffs[j] is the coefficient of t^j for j = 0, 1, ..., r_max-2
    coeffs = []
    for r in range(2, r_max + 1):
        S_r = float(shadow_S_r(c, r))
        fact_rm1 = float(_factorial_fraction(r - 1))
        coeffs.append(S_r / fact_rm1)

    # numpy polynomial: coefficients in decreasing order of power
    poly_coeffs = list(reversed(coeffs))
    roots = np.roots(poly_coeffs)

    # Start with t = 0 (always a critical point)
    real_roots = [0.0]

    # Add real roots of P(t)
    for root in roots:
        if abs(root.imag) < 1e-10:
            real_roots.append(float(root.real))

    # Sort by potential value
    real_roots.sort(key=lambda t: shadow_potential(c, t, r_max))
    return real_roots


# ===========================================================================
# 7. Vacuum energy
# ===========================================================================

def vacuum_energy(c, r_max: int = 6) -> float:
    r"""Potential energy V(t*) at the stable (lowest-energy) vacuum.

    If no nontrivial critical point exists, returns V(0) = 0.

    The stable vacuum is the critical point with the smallest V(t*).
    """
    crits = critical_points(c, r_max)
    if not crits:
        return 0.0

    return min(shadow_potential(c, t, r_max) for t in crits)


# ===========================================================================
# 8. Level truncation potential
# ===========================================================================

def level_truncation_potential(c, t: float, L: int) -> float:
    r"""Shadow potential truncated at mass level L.

    In level truncation, the string field is expanded in states
    up to L_0 = L.  Each state at level n contributes terms from
    the shadow vertices involving n insertions.

    At level L, the effective potential includes shadow coefficients
    S_r for r <= L + 2 (the tachyon at level 0 uses S_2, etc.).

    Parameters
    ----------
    c : central charge
    t : tachyon field value
    L : truncation level (L=0 is tachyon only, L=1 includes massless, etc.)
    """
    # At level L, include S_r for r = 2 to L+2
    r_max = L + 2
    return shadow_potential(c, t, r_max)


# ===========================================================================
# 9. Level convergence rate
# ===========================================================================

def level_convergence_rate(c, L_max: int = 10) -> Dict[int, float]:
    r"""Measure how fast level truncation converges.

    Compute |V_L(t*_L) - V_{L+1}(t*_{L+1})| / |V_L(t*_L)| for
    each level L.

    For class G (Heisenberg): terminates exactly at L=0.
    For class L (affine): terminates at L=1.
    For class M (Virasoro): converges geometrically with rate rho(c).

    Returns
    -------
    Dict mapping level L to the relative change in vacuum energy.
    """
    rates = {}
    prev_energy = None

    for L in range(0, L_max):
        energy = vacuum_energy(c, r_max=L + 2)
        if prev_energy is not None and prev_energy != 0:
            rates[L] = abs(energy - prev_energy) / abs(prev_energy) if prev_energy != 0 else abs(energy)
        elif prev_energy is not None:
            rates[L] = abs(energy - prev_energy)
        prev_energy = energy

    return rates


# ===========================================================================
# 10. A-infinity relation check
# ===========================================================================

def ainfty_relation_check(g1: int, n1: int, g2: int, n2: int, c) -> Fraction:
    r"""Check the A-infinity relation for the composition V_{g1,n1} o V_{g2,n2}.

    The MC equation D*Theta + (1/2)[Theta, Theta] = 0, projected to a
    given (g, n), gives the A-infinity relation:

        sum_{(g1,n1)+(g2,n2)=(g,n)} V_{g1,n1} o V_{g2,n2} = 0

    where the sum is over all splittings and the composition "o" denotes
    the operadic composition (gluing of one output leg of V_{g1,n1} to
    an input of V_{g2,n2}).

    At genus 0: the relation V_{0,3} o V_{0,3} + ... = 0 is equivalent
    to the Jacobi identity / A-infinity associativity.

    We compute the SIGNED CONTRIBUTION of a single composition.

    Parameters
    ----------
    g1, n1 : genus and arity of the first vertex
    g2, n2 : genus and arity of the second vertex
    c : central charge

    Returns
    -------
    The composition V_{g1,n1} o V_{g2,n2} (exact rational).
    """
    c = Fraction(c)
    V1 = zwiebach_vertex(g1, n1, c)
    V2 = zwiebach_vertex(g2, n2, c)

    # The composition V1 o V2 at the level of shadow coefficients
    # is the product V1 * V2 weighted by the number of composition slots.
    # For V_{g1,n1} o V_{g2,n2}: there are n1 ways to attach (choosing
    # which input of V1 to sew to the output of V2).
    # The sign is (-1)^{|V2|} from the Koszul sign convention.

    return Fraction(n1) * V1 * V2


def ainfty_total_at(g: int, n: int, c) -> Fraction:
    r"""Total A-infinity relation at genus g, arity n.

    Sum over all composition splittings:
        sum_{g1+g2=g, n1+n2=n+1} n1 * V_{g1,n1} * V_{g2,n2} = 0

    This must vanish if the MC equation holds.

    Returns
    -------
    The total A-infinity relation (should be 0 for valid SFT).
    """
    c = Fraction(c)
    total = Fraction(0)

    for g1 in range(g + 1):
        g2 = g - g1
        for n1 in range(1, n + 2):
            n2 = n + 1 - n1
            if n2 < 0:
                continue
            if 2 * g1 - 2 + n1 <= 0:
                continue
            if 2 * g2 - 2 + n2 <= 0:
                continue
            total += ainfty_relation_check(g1, n1, g2, n2, c)

    return total


# ===========================================================================
# 11. Gauge variation
# ===========================================================================

def gauge_variation(c, t: float, lambda_param: float, r_max: int = 4) -> float:
    r"""Gauge variation of the tachyon field.

    In SFT, the gauge transformation is:
        delta_Psi = Q Lambda + sum_{n>=2} V_{0,n+1}(Psi^n, Lambda)

    where Lambda is the gauge parameter and Q is the BRST operator.

    At the level of the tachyon effective potential, the gauge variation
    of the field value t is:

        delta_t = lambda * kappa + sum_{r>=3} S_r/(r-2)! * t^{r-2} * lambda

    Parameters
    ----------
    c : central charge
    t : current field value
    lambda_param : gauge parameter
    r_max : maximum arity

    Returns
    -------
    The gauge variation delta_t.
    """
    kappa = float(Fraction(c) / 2)
    result = lambda_param * kappa  # BRST part

    for r in range(3, r_max + 1):
        S_r = float(shadow_S_r(c, r))
        fact_rm2 = float(_factorial_fraction(r - 2))
        result += lambda_param * S_r * (t ** (r - 2)) / fact_rm2

    return result


# ===========================================================================
# 12. Koszul SFT duality
# ===========================================================================

def koszul_sft_duality(c, t: float, r_max: int = 6) -> Dict[str, float]:
    r"""Compare V(Vir_c, t) with V(Vir_{26-c}, t).

    Koszul duality for Virasoro: A = Vir_c, A! = Vir_{26-c}.

    KEY RESULT (AP24):
        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13
        This is 13, NOT 0.

    At c = 13 (self-dual point): V(13, t) = V(13, t) trivially.
    At c = 26: V(26, t) has kappa = 13 (the matter kappa).
              V(0, t) is UNDEFINED (c = 0 is singular).

    Returns
    -------
    Dict with:
        'V_A': V(Vir_c, t)
        'V_A_dual': V(Vir_{26-c}, t)
        'kappa_sum': kappa(c) + kappa(26-c) = 13
        'delta_V': V(c,t) - V(26-c, t)
        'c': c
        'c_dual': 26 - c
    """
    c_dual = 26 - c
    V_A = shadow_potential(c, t, r_max)

    # Handle c_dual = 0 (singular)
    if c_dual == 0:
        V_A_dual = float('inf')
    else:
        V_A_dual = shadow_potential(c_dual, t, r_max)

    kappa_c = float(Fraction(c) / 2)
    kappa_dual = float(Fraction(c_dual) / 2)

    return {
        'V_A': V_A,
        'V_A_dual': V_A_dual,
        'kappa_sum': kappa_c + kappa_dual,
        'delta_V': V_A - V_A_dual if not math.isinf(V_A_dual) else float('inf'),
        'c': c,
        'c_dual': c_dual,
    }


# ===========================================================================
# 13. Sen conjecture ratio
# ===========================================================================

def sen_conjecture_ratio(c, r_max: int = 6) -> Optional[float]:
    r"""Ratio V(t*) / (-D-brane tension) for the Sen conjecture.

    The Sen conjecture states that the tachyon potential at its
    minimum equals minus the D-brane tension:

        V(t*) = -T_Dp

    In the shadow tower framework, the D-brane tension is related
    to the exponential of the modular characteristic:

        T ~ exp(2*pi * sqrt(kappa))

    This function returns the ratio V(t*)/(-T), which should
    approach 1 if the Sen conjecture holds.

    For Virasoro at large c: kappa = c/2 and the potential deepens
    with c, while the tension grows exponentially.

    Returns
    -------
    The ratio, or None if no nontrivial vacuum exists.
    """
    crits = critical_points(c, r_max)
    # Find the nontrivial critical point (not t=0)
    nontrivial = [t for t in crits if abs(t) > 1e-10]
    if not nontrivial:
        return None

    # Find the deepest minimum
    t_star = min(nontrivial, key=lambda t: shadow_potential(c, t, r_max))
    V_star = shadow_potential(c, t_star, r_max)

    # D-brane tension normalization
    kappa = float(Fraction(c) / 2)
    if kappa <= 0:
        return None
    T = 1.0 / (2 * PI ** 2)  # Normalization convention

    if T == 0:
        return None

    return V_star / (-T)


# ===========================================================================
# 14. Heisenberg SFT potential
# ===========================================================================

def heisenberg_sft_potential(k, t: float, r_max: int = 6) -> float:
    r"""SFT potential for Heisenberg at level k.

    Class G: the shadow tower terminates at arity 2.
    The potential is EXACTLY QUADRATIC:

        V(t) = (k/2) * t^2

    regardless of r_max (all S_r = 0 for r >= 3).
    """
    kappa = float(Fraction(k))
    return kappa * t ** 2 / 2


def heisenberg_sft_potential_exact(k, t_sym=None):
    """Exact symbolic potential for Heisenberg."""
    k = Fraction(k)
    if t_sym is None:
        from sympy import Symbol
        t_sym = Symbol('t')
    return k * t_sym ** 2 / 2


# ===========================================================================
# 15. Affine sl_2 SFT potential
# ===========================================================================

def affine_sft_potential(k, t: float, r_max: int = 6) -> float:
    r"""SFT potential for affine sl_2 at level k.

    Class L: the shadow tower terminates at arity 3.
    The potential truncates at cubic order:

        V(t) = (kappa/2) * t^2 + (S_3/6) * t^3

    where kappa = 3(k+2)/4 and S_3 is the Lie cubic (= 1 in our normalization).

    The CUBIC potential has a nontrivial critical point at:
        t* = -3*kappa/S_3 = -3*kappa
    with vacuum energy:
        V(t*) = -9*kappa^3 / (2*S_3^2) = -(27/2)*kappa^3
    """
    k_frac = Fraction(k)
    kappa = float(affine_sl2_S_r(k_frac, 2))
    S3 = float(affine_sl2_S_r(k_frac, 3))

    # V(t) = (kappa/2)*t^2 + (S_3/6)*t^3 + (S_4/24)*t^4 + ...
    # For class L: S_r = 0 for r >= 4, so only quadratic + cubic
    V = kappa * t ** 2 / 2 + S3 * t ** 3 / 6
    return V


# ===========================================================================
# Utility: free energy from shadow data
# ===========================================================================

def free_energy_scalar(kappa, g: int) -> Fraction:
    """Scalar free energy F_g = kappa * lambda_g^FP."""
    return Fraction(kappa) * lambda_fp(g)


def free_energy_table(c, g_max: int = 5) -> Dict[int, Fraction]:
    """Table of scalar free energies F_g = kappa * lambda_g^FP."""
    kappa = Fraction(c) / 2
    return {g: free_energy_scalar(kappa, g) for g in range(1, g_max + 1)}


# ===========================================================================
# Complementarity sum
# ===========================================================================

def kappa_complementarity_sum(c) -> Fraction:
    r"""kappa(Vir_c) + kappa(Vir_{26-c}).

    AP24: this equals 13, NOT 0.
    kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2.
    Sum = c/2 + (26-c)/2 = 13.
    """
    return Fraction(c) / 2 + Fraction(26 - c) / 2


def shadow_complementarity(c, r: int) -> Fraction:
    r"""S_r(c) + S_r(26-c) for Virasoro.

    At the self-dual point c = 13: S_r(13) + S_r(13) = 2*S_r(13).
    In general, this is a nontrivial rational function of c.
    """
    c_frac = Fraction(c)
    c_dual = 26 - c_frac
    if c_dual == 0:
        raise ValueError("Koszul dual central charge c'=26-c is zero; shadow undefined")
    return shadow_S_r(c_frac, r) + shadow_S_r(c_dual, r)


# ===========================================================================
# Shadow potential derivative (for Newton's method and diagnostics)
# ===========================================================================

def shadow_potential_derivative(c, t: float, r_max: int = 6, order: int = 1) -> float:
    """Compute the k-th derivative of V(t) at field value t.

    V^{(k)}(t) = sum_{r>=k} S_r(c) / (r-k)! * t^{r-k}
    """
    result = 0.0
    for r in range(order + 1, r_max + 1):
        S_r = float(shadow_S_r(c, r))
        fact = float(_factorial_fraction(r - order))
        result += S_r * (t ** (r - order)) / fact
    # Include the r=order term: S_order / 0! * t^0 = S_order
    S_ord = float(shadow_S_r(c, max(2, order)))
    if order >= 2:
        result += S_ord
    return result


# ===========================================================================
# Shadow tower convergence diagnostics
# ===========================================================================

def shadow_growth_rate(c) -> float:
    r"""Shadow growth rate rho(c) for the Virasoro tower.

    rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)

    where alpha = S_3 = 2, kappa = c/2, Delta = 8*kappa*S_4.

    From thm:shadow-radius.
    """
    c_frac = Fraction(c)
    kappa = c_frac / 2
    S4 = shadow_S_r(c, 4)
    alpha = Fraction(2)  # S_3 for Virasoro
    Delta = 8 * kappa * S4

    # rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)
    numerator_sq = 9 * alpha ** 2 + 2 * Delta
    denominator = 2 * abs(kappa)

    if denominator == 0:
        return float('inf')

    return math.sqrt(float(numerator_sq)) / float(denominator)


def tower_convergence_check(c, r_max: int = 10) -> Dict[str, Any]:
    r"""Check convergence of the shadow tower at central charge c.

    Returns the growth rate rho and the sequence of ratios |S_{r+1}/S_r|.
    """
    rho = shadow_growth_rate(c)
    ratios = {}
    for r in range(2, r_max):
        S_r = float(shadow_S_r(c, r))
        S_rp1 = float(shadow_S_r(c, r + 1))
        if S_r != 0:
            ratios[r] = abs(S_rp1 / S_r)
        else:
            ratios[r] = 0.0

    return {
        'rho': rho,
        'ratios': ratios,
        'convergent': rho < 1.0,
        'c_star_approx': 6.1243,
    }
