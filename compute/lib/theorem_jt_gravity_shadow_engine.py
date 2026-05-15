r"""JT gravity data versus the scalar shadow obstruction lane.

This engine keeps four lanes separate.

Scalar Bernoulli/A-hat lane.  The compute-certified scalar formula is

    F_g^{shadow}(Vir_c) = kappa(Vir_c) * lambda_g^{FP}
                         = (c/2) * lambda_g^{FP},

where

    lambda_g^{FP}
      = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!).

The scalar generating function is
``kappa * ((hbar/2)/sin(hbar/2) - 1)``.  Its radius ``2*pi`` is a
scalar A-hat statement.  JT gravity and the three-dimensional
gravitational path integral require separate Borel-summability input.

Finite Virasoro window.  On the non-singular Virasoro surface
``c(5c+22) != 0``,

    kappa(Vir_c) = c/2,
    S_3 = 2,
    S_4 = 10/(c(5c+22)),
    Delta = 8*kappa*S_4 = 40/(5c+22),

and

    Q_Vir(t) = (c + 6t)^2 + 2*Delta*t^2
             = (c + 6t)^2 + 80*t^2/(5c+22).

This finite scalar window supplies no JT sine curve, Eynard-Orantin
recursion package, or all-genus gravity partition function.

WP/JT lane.  The JT formulas used here are externally supplied analytic
gravity data: the sine spectral curve, the trumpet and disk amplitudes,
and a finite table of Weil-Petersson volumes in Mirzakhani convention.
The finite table is a comparison window, not an all-genus theorem.

Analytic firewall.  The module certifies algebraic non-identification
and low-genus ratio non-constancy.  Borel summability, BTZ closed-form
recovery from shadows, a full JT partition function, and an all-genus
three-dimensional gravity theorem require external analytic input.

Manuscript anchors:
    chapters/examples/landscape_census.tex
    chapters/examples/genus_expansions.tex
    chapters/connections/genus_complete.tex
    chapters/connections/entanglement_modular_koszul.tex

External anchors:
    [SSS19] Saad-Shenker-Stanford, JT gravity as a matrix integral.
    [Mir07] Mirzakhani, WP volumes and intersection numbers.
    [EO07]  Eynard-Orantin, Invariants of algebraic curves.
    [SW20]  Stanford-Witten, JT gravity and the ensembles.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli as sympy_bernoulli, factorial,
    simplify, sqrt as sym_sqrt, sin as sym_sin, cos as sym_cos,
    exp as sym_exp, pi as sym_pi, oo, Poly, expand, cancel,
    N as Neval, Integer, log as sym_log,
)

# ============================================================================
# Constants
# ============================================================================

PI = math.pi
PI2 = PI * PI
TWO_PI = 2.0 * PI
FOUR_PI2 = 4.0 * PI2

c_sym = Symbol('c', positive=True)
g_sym = Symbol('g', positive=True, integer=True)
t_sym = Symbol('t')
x_sym = Symbol('x')
hbar_sym = Symbol('hbar')

CERTIFIED = "certified"
CONDITIONAL = "conditional"
EXTERNAL_INPUT = "external_input"
FINITE_WINDOW = "finite_window"
NON_CERTIFIED = "non_certified"


def object_kernel_firewall() -> Dict[str, Any]:
    r"""Object and kernel firewalls used by this compute surface.

    The entries are source strings, not new computations.
    """
    return {
        'objects': ('A', 'B(A)', 'A^i', 'A^!', 'Z_ch^der(A)'),
        'bar_cobar_inversion': 'Omega(B(A)) = A',
        'bar_cobar_inversion_is_koszul_duality': False,
        'koszul_dual_branch': 'A^! is the Verdier/continuous-linear dual branch',
        'bulk_branch': 'Z_ch^der(A) is Hochschild/bulk data, not Koszul dual data',
        'kernels': {
            'affine_raw_trace_form': 'k*Omega_tr/z',
            'kz_connection': 'Omega/((k+h^vee)z)',
            'heisenberg': 'k/z',
            'virasoro': '(c/2)/z^3 + 2T/z',
        },
        'source': 'CLAUDE.md; chapters/examples/landscape_census.tex',
    }


def gravity_claim_certification() -> Dict[str, Any]:
    r"""Certification map for the JT/shadow comparison.

    A scalar shadow identity may be certified here without certifying the
    analytic gravity claim that usually sits next to it.
    """
    return {
        'scalar_bernoulli_ahat_lane': CERTIFIED,
        'virasoro_shadow_constants': CERTIFIED,
        'wp_jt_sine_curve_data': EXTERNAL_INPUT,
        'wp_jt_finite_window': {
            'status': FINITE_WINDOW,
            'certified_genera': (1, 2, 3),
        },
        'eo_recursion_from_shadow_curve': CONDITIONAL,
        'exact_scalar_radius_2pi': CERTIFIED,
        'jt_borel_summability': NON_CERTIFIED,
        'btz_closed_form_recovery_from_shadow': NON_CERTIFIED,
        'full_jt_partition_function_from_shadow': NON_CERTIFIED,
        'all_genus_3d_gravity_partition_theorem': NON_CERTIFIED,
    }


def _require_regular_virasoro_surface(c_val: float) -> None:
    """Reject Virasoro central charges where the canonical formula is singular."""
    if abs(c_val) < 1e-15 or abs(5.0 * c_val + 22.0) < 1e-15:
        raise ValueError(
            "Virasoro shadow constants are canonical only on c(5c+22) != 0; "
            "singular quotients require a separate renormalized calculation."
        )


def virasoro_shadow_constants(c_val: float) -> Dict[str, float]:
    r"""Canonical Virasoro shadow constants on ``c(5c+22) != 0``.

    Source: ``chapters/examples/landscape_census.tex``.
    """
    c_float = float(c_val)
    _require_regular_virasoro_surface(c_float)
    kappa = c_float / 2.0
    S3 = 2.0
    S4 = 10.0 / (c_float * (5.0 * c_float + 22.0))
    S5 = -48.0 / (c_float * c_float * (5.0 * c_float + 22.0))
    Delta = 8.0 * kappa * S4
    return {
        'c': c_float,
        'kappa': kappa,
        'S2': kappa,
        'S3': S3,
        'S4': S4,
        'S5': S5,
        'Delta': Delta,
        'Q_t2_extra_coefficient': 2.0 * Delta,
        'status': CERTIFIED,
    }


# ============================================================================
# Section 1: Bernoulli numbers (exact, standalone -- no circular imports)
# ============================================================================

@lru_cache(maxsize=256)
def bernoulli_exact(n: int) -> Fraction:
    """Bernoulli number B_n as exact Fraction. Convention: B_1 = -1/2."""
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        bk = bernoulli_exact(k)
        if bk != 0:
            s += Fraction(math.comb(n + 1, k)) * bk
    return -s / Fraction(n + 1)


@lru_cache(maxsize=128)
def lambda_fp_exact(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP (exact).

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Scalar generating function:
    sum_{g >= 1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    All values are positive.
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B2g = bernoulli_exact(2 * g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs(B2g) / Fraction(math.factorial(2 * g)))


def F_g_shadow(kappa, g: int):
    """Shadow free energy F_g(A) = kappa(A) * lambda_g^FP.

    This is the scalar uniform-weight lane once kappa(A) is supplied.
    """
    lfp = lambda_fp_exact(g)
    if isinstance(kappa, Rational):
        return kappa * Rational(lfp.numerator, lfp.denominator)
    return float(kappa) * float(lfp)


def F_g_shadow_virasoro(c_val, g: int):
    """Shadow free energy for Virasoro at central charge c.

    F_g(Vir_c) = (c/2) * lambda_g^FP.
    """
    kappa = Rational(c_val) / 2 if isinstance(c_val, (int, Rational, Integer)) else c_val / 2.0
    return F_g_shadow(kappa, g)


# ============================================================================
# Section 2: JT gravity free energies (Weil-Petersson volumes)
# ============================================================================

# The JT genus-g free energy for CLOSED surfaces is the WP volume:
#   F_g^{JT} = V_{g,0} = integral_{M_g} exp(2 pi^2 kappa_1)
#
# These finite-window values are rational multiples of powers of pi.
#
# We store them as float (including pi factors) from Zograf's tables.
#
# The standard reference: Zograf (2008), Do-Norbury (2006).
# Cross-checked: dilaton equation V_{g,1}(0) = (2g-2) * V_{g,0}.

def _wp_closed_volume_table() -> Dict[int, float]:
    r"""Finite WP comparison table for g = 1, 2, 3.

    V_{g,0} = integral_{M_g} exp(omega_{WP})

    In the Mirzakhani convention:
      V_{g,1}(0) = (2g-2) * V_{g,0}   (dilaton equation)

    From Zograf (2008) and Do-Norbury-Scott:
      V_{g,1}(0) is tabulated; V_{g,0} = V_{g,1}(0) / (2g-2).

    Authoritative values:
      V_{1,1}(0) = pi^2 / 12
      V_{2,1}(0) = 29 * pi^8 / 276480
      V_{2,0}    = 29 * pi^8 / 552960

    For g = 1: V_{1,0} is not well-defined (M_{1,0} is not stable:
    2*1-2+0 = 0, which is the stability boundary. The Euler characteristic
    chi(M_{1,1}) = -1/12 gives the orbifold volume. We use
    F_1^{JT} = pi^2/12 (from V_{1,1}(0) which plays the role of F_1).

    The JT genus expansion starts from the one-boundary sector.
    The "free energy" F_g^{JT} in the SSS sense is not V_{g,0} but rather
    a Laplace transform of V_{g,1}(b). For comparison with the shadow
    tower, we compare the tautological integrals directly.
    """
    p = PI2
    return {
        # g=1: use V_{1,1}(0) = pi^2/12 as the canonical genus-1 quantity.
        # V_{1,0} is not well-defined (stability boundary), so we use V_{1,1}(0).
        1: p / 12.0,
        # g=2: V_{2,0} = V_{2,1}(0)/2 = 29*pi^8/(2*276480) = 29*pi^8/552960
        # V_{2,1}(0) = 29*pi^8/276480 (Mirzakhani convention, verified).
        # Dilaton: V_{g,1}(0) = (2g-2)*V_{g,0}, so V_{2,0} = V_{2,1}(0)/2.
        2: 29.0 * p**4 / 552960.0,
        # g=3: V_{3,0} = V_{3,1}(0)/4
        # V_{3,1}(0) = 176557*pi^{14}/490497638400 (Mirzakhani convention).
        # Dilaton: V_{3,1}(0) = 4*V_{3,0}.
        3: 176557.0 * p**7 / 1961990553600.0,
        # g=4 is omitted: it needs an independent convention check between
        # Mirzakhani, Zograf, and Stanford-Witten normalizations.
    }


def F_g_JT(g: int) -> float:
    r"""Finite-window JT/WP tautological integral.

    For g = 1: F_1^{JT} = V_{1,1}(0) = pi^2/12.
    For g >= 2: F_g^{JT} = V_{g,0} = integral_{M_g} exp(omega_{WP}).

    These values are a low-genus comparison window.  They are not an
    all-genus JT partition theorem.

    These involve kappa-class intersections (exp(2 pi^2 kappa_1)),
    not lambda-class intersections. They are structurally different from
    the shadow free energies F_g^{shadow} = kappa * lambda_g^{FP}.
    """
    table = _wp_closed_volume_table()
    if g in table:
        return table[g]
    raise ValueError(f"F_g^JT not tabulated for g = {g}. Available: g = 1..3.")


# ============================================================================
# Section 3: The ratio F_g^JT / F_g^shadow
# ============================================================================

def ratio_JT_shadow(c_val: float, g: int) -> float:
    r"""Compute R_g(c) = F_g^{JT} / F_g^{shadow}(Vir_c).

    R_g = V_{g,0} / ((c/2) * lambda_g^{FP})

    This ratio is not constant in g. The reason:
    - F_g^{JT} involves kappa-class intersections (WP volumes)
    - F_g^{shadow} involves lambda-class intersections (FP numbers)
    - These are different tautological classes on M_{g,n}

    At genus 1: lambda_1 = kappa_1/12, so V_{1,1}(0) = 2 pi^2 * <kappa_1>_{1,1}
    and lambda_1^{FP} = 1/24. The ratio R_1 = (pi^2/12) / ((c/2)/24) = 4 pi^2 / c.

    At genus 2: V_{2,0} involves <kappa_1^3>_2 and lower terms from exp(2 pi^2 kappa_1),
    while lambda_2^{FP} = 7/5760. The ratio R_2 differs from R_1.
    """
    f_jt = F_g_JT(g)
    f_sh = F_g_shadow_virasoro(c_val, g)
    if isinstance(f_sh, Rational):
        f_sh = float(f_sh)
    if abs(f_sh) < 1e-300:
        raise ValueError(f"Shadow free energy vanishes at c = {c_val}")
    return f_jt / f_sh


def ratio_JT_shadow_normalized(g: int) -> float:
    r"""The ratio R_g = F_g^{JT} / (lambda_g^{FP}), independent of c.

    Since F_g^{shadow} = (c/2) * lambda_g^{FP}, we have
        R_g(c) = F_g^{JT} / ((c/2) * lambda_g^{FP}) = (2/c) * F_g^{JT} / lambda_g^{FP}

    The c-independent part is F_g^{JT} / lambda_g^{FP}.
    """
    f_jt = F_g_JT(g)
    lfp = float(lambda_fp_exact(g))
    return f_jt / lfp


def is_ratio_constant() -> Tuple[bool, Dict[int, float]]:
    r"""Test whether R_g = F_g^{JT} / lambda_g^{FP} is constant in g.

    Returns (is_constant, {g: R_g}).
    """
    ratios = {}
    for g in range(1, 4):
        try:
            ratios[g] = ratio_JT_shadow_normalized(g)
        except ValueError:
            pass
    if len(ratios) < 2:
        return (True, ratios)  # cannot determine with < 2 values
    vals = list(ratios.values())
    # Check if all ratios agree to within 1%
    ref = vals[0]
    constant = all(abs(v / ref - 1.0) < 0.01 for v in vals[1:])
    return (constant, ratios)


# ============================================================================
# Section 4: Genus-1 match (the only genus with a simple dictionary)
# ============================================================================

def genus_1_dictionary(c_val: float) -> Dict[str, Any]:
    r"""Genus-1 scalar comparison between JT/WP and the shadow lane.

    At genus 1, the Mumford relation lambda_1 = kappa_1/12 gives:

        F_1^{shadow} = (c/2) * lambda_1^{FP} = (c/2) * (1/24) = c/48

        F_1^{JT} = V_{1,1}(0) = pi^2/12

    The ratio: R_1 = (pi^2/12) / (c/48) = 4 pi^2 / c = (2 pi)^2 / c

    Setting R_1 = 1 (identifying the two): c_match = 4 pi^2 ~ 39.478

    This is a scalar normalization statement only.  In the usual JT genus
    expansion the genus-1 term carries weight e^{S_0(2-2g)} = 1, so this
    comparison does not determine the physical JT coupling S_0.

    The quantity c/(4*pi^2) below is therefore recorded as a scalar
    normalization ratio, not as a certified value of e^{S_0}.
    """
    kappa = c_val / 2.0
    f1_shadow = kappa * float(lambda_fp_exact(1))
    f1_jt = F_g_JT(1)
    ratio = f1_jt / f1_shadow if abs(f1_shadow) > 1e-300 else float('inf')
    c_match = 4.0 * PI2  # value of c where F_1^shadow = F_1^JT
    scalar_normalization = c_val / (4.0 * PI2)
    return {
        'c': c_val,
        'kappa': kappa,
        'F_1_shadow': f1_shadow,
        'F_1_JT': f1_jt,
        'ratio_R1': ratio,
        'c_match_genus_1': c_match,
        'scalar_normalization_to_JT_g1': scalar_normalization,
        'e_S0_genus_1': None,
        'e_S0_genus_1_status': NON_CERTIFIED,
        'jt_genus_weight_determines_S0': False,
    }


# ============================================================================
# Section 5: Spectral curves
# ============================================================================

def shadow_spectral_curve(c_val: float, t_val: float) -> float:
    r"""Shadow spectral curve y^2 = Q_L(t) for Virasoro at central charge c.

    Q_Vir(t) = (2*kappa + 3*S_3*t)^2 + 2*Delta*t^2

    where kappa = c/2, S_3 = 2, S_4 = 10/(c(5c+22)), Delta = 8*kappa*S_4.

    Q_Vir(t) = (c + 6t)^2 + 80*t^2/(5c+22)
    """
    const = virasoro_shadow_constants(c_val)
    return (
        (2.0 * const['kappa'] + 3.0 * const['S3'] * t_val) ** 2
        + 2.0 * const['Delta'] * t_val ** 2
    )


def jt_spectral_curve(x_val: float) -> float:
    r"""JT spectral curve y^2 = sin^2(2 pi sqrt(x)) / (16 pi^2).

    Defined for x >= 0. The spectral curve has zeros at x = n^2/4 (n = 0, 1, 2, ...).
    """
    if x_val < 0:
        return 0.0
    if x_val < 1e-20:
        return x_val / 4.0  # leading order: sin^2(u)/u^2 -> 1
    sq = math.sqrt(x_val)
    return math.sin(TWO_PI * sq) ** 2 / (16.0 * PI2)


def spectral_curve_comparison(c_val: float, x_val: float) -> Dict[str, float]:
    r"""Compare shadow and JT spectral curves at a point.

    The shadow curve is in the t-variable; JT is in the x-variable.  Setting
    t = x is only a diagnostic coordinate choice, not a canonical map.

    The shadow curve Q_Vir is a polynomial (degree 2 in t).
    The JT curve is transcendental (sin^2).

    For small x:
    JT: y^2 ~ x/4.
    Shadow: Q_Vir(0) = c^2 (constant, nonzero)

    The curves live in different spaces with different parametrizations.
    The comparison is structural, not pointwise.
    """
    q_shadow = shadow_spectral_curve(c_val, x_val)
    q_jt = jt_spectral_curve(x_val)
    return {
        'x': x_val,
        'c': c_val,
        'Q_shadow': q_shadow,
        'Q_JT': q_jt,
        'shadow_at_0': shadow_spectral_curve(c_val, 0.0),
        'JT_at_0': 0.0,  # sin^2(0) = 0
        'shadow_degree': 2,  # polynomial degree in t
        'JT_degree': 'transcendental',
        'same_curve_certified': False,
        'comparison_status': NON_CERTIFIED,
    }


def shadow_curve_zeros(c_val: float) -> List[float]:
    r"""Zeros of the shadow spectral curve Q_Vir(t) = 0.

    Q_Vir(t) = (c + 6t)^2 + 80*t^2/(5c+22)

    Setting Q = 0: (c + 6t)^2 = -80*t^2/(5c+22)

    For c > 0 and 5c+22 > 0: the RHS is <= 0 and the LHS >= 0.
    So Q = 0 requires both sides = 0, i.e. c + 6t = 0 AND t = 0,
    which requires c = 0.

    For c > 0: Q_Vir(t) > 0 for all real t. The shadow curve has
    NO REAL ZEROS. The spectral curve is positive definite.

    CONTRAST with JT: sin^2(2 pi sqrt(x)) = 0 at x = n^2/4.
    JT has INFINITELY MANY zeros. Shadow has NONE (for c > 0).
    """
    virasoro_shadow_constants(c_val)
    if c_val <= 0 or 5.0 * c_val + 22.0 <= 0:
        raise ValueError("real-zero certification is implemented only for c > 0")
    # Check: Q_Vir(t) = (c + 6t)^2 + 80*t^2/(5c+22) > 0 for all real t when c > 0
    kappa = c_val / 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    Delta = 8.0 * kappa * S4
    # Q = (c + 6t)^2 + 2*Delta*t^2.  Both terms non-negative for c > 0, Delta > 0.
    # Zero iff both vanish: c + 6t = 0 => t = -c/6, and 2*Delta*t^2 = 0 => t = 0.
    # Contradiction for c > 0.
    return []  # no real zeros for c > 0


def jt_curve_zeros(n_max: int = 10) -> List[float]:
    r"""Zeros of the JT spectral curve: x = n^2/4 for n = 0, 1, 2, ...

    sin^2(2 pi sqrt(x)) = 0 when 2 pi sqrt(x) = n*pi, i.e. sqrt(x) = n/2.
    """
    return [n * n / 4.0 for n in range(n_max + 1)]


# ============================================================================
# Section 6: Density of states
# ============================================================================

def jt_density_of_states(E: float) -> float:
    r"""JT density of states rho_JT(E) = sinh(2 pi sqrt(E)) / (4 pi^2).

    Defined for E >= 0. At E = 0: rho_JT(0) = 0.
    For large E: rho_JT(E) ~ exp(2 pi sqrt(E)) / (8 pi^2).
    """
    if E < 0:
        return 0.0
    if E < 1e-20:
        return math.sqrt(E) / (TWO_PI)  # leading order: sinh(u)/u -> 1
    sq = math.sqrt(E)
    return math.sinh(TWO_PI * sq) / FOUR_PI2


def shadow_density_of_states(c_val: float, E: float) -> float:
    r"""Shadow density of states for the shadow matrix model at central charge c.

    For the Gaussian shadow (class G), the eigenvalue density is the
    Wigner semicircle: rho(E) = (1/pi) sqrt(2*kappa - E^2) for |E| < sqrt(2*kappa).

    For class M (Virasoro), the spectral density is deformed by higher
    shadow coefficients. We compute the Gaussian approximation here.

    kappa = c/2, so the semicircle has radius sqrt(c) and area = kappa.
    """
    if c_val <= 0 or E < 0:
        return 0.0
    kappa = c_val / 2.0
    # Wigner semicircle with second moment kappa
    # rho(E) = (2/(pi*a^2)) * sqrt(a^2 - E) for 0 <= E <= a^2
    # where a^2 = 2*kappa (single-cut symmetric matrix model).
    # Wait: for a GUE with V(M) = (1/2)*M^2, the eigenvalue density
    # in the large-N limit is rho(x) = (1/(2*pi))*sqrt(4-x^2) (Wigner).
    # With V(M) = (kappa/2)*M^2, rescaling gives rho(x) = (kappa/(2*pi))*sqrt(4/kappa - x^2).
    # More precisely: the one-cut spectral density for the matrix model
    # with potential V(M) = (kappa/2)*M^2 has support on [-2/sqrt(kappa), 2/sqrt(kappa)]
    # and is semicircular. For the POSITIVE half (E >= 0):
    edge = 4.0 / kappa if kappa > 0 else 0.0
    if E > edge:
        return 0.0
    return (kappa / (2.0 * PI)) * math.sqrt(edge - E)


def density_comparison(c_val: float, E: float) -> Dict[str, float]:
    """Compare JT and shadow densities of states at a point."""
    return {
        'E': E,
        'c': c_val,
        'rho_JT': jt_density_of_states(E),
        'rho_shadow_Gaussian': shadow_density_of_states(c_val, E),
        'JT_support': 'all E >= 0',
        'shadow_support': f'E in [0, {4.0 / (c_val / 2.0):.4f}]' if c_val > 0 else 'E = 0',
    }


# ============================================================================
# Section 7: Trumpet partition functions
# ============================================================================

def jt_trumpet(beta: float, b: float) -> float:
    r"""JT trumpet partition function Z_trumpet(beta, b).

    Z_trumpet(beta, b) = exp(-b^2/(4*beta)) / sqrt(4*pi*beta)

    This is the Laplace-transformed propagator between a geodesic
    boundary of length b and an asymptotic boundary with renormalized
    length beta.
    """
    if beta <= 0:
        raise ValueError(f"beta must be > 0, got {beta}")
    return math.exp(-b * b / (4.0 * beta)) / math.sqrt(4.0 * PI * beta)


def jt_disk(beta: float) -> float:
    r"""JT disk amplitude Z_disk(beta).

    Z_disk(beta) = exp(2*pi^2/beta) / (4*pi*beta)^{3/2}
    """
    if beta <= 0:
        raise ValueError(f"beta must be > 0, got {beta}")
    return math.exp(2.0 * PI2 / beta) / (4.0 * PI * beta) ** 1.5


def shadow_trumpet_analogue(c_val: float, hbar: float, t: float) -> float:
    r"""Shadow trumpet analogue.

    The shadow "trumpet" is the one-point amplitude at arity 1:

        Z^{sh}_1(hbar, t) = sqrt(Q_L(t)) * ahat_gf(hbar)

    where ahat_gf(hbar) = (hbar/2)/sin(hbar/2) is the A-hat generating function.

    This is a scalar shadow amplitude.  It is not the JT trumpet and does
    not certify a gravitational boundary path integral.
    """
    Q = shadow_spectral_curve(c_val, t)
    if Q < 0:
        return 0.0
    if abs(hbar) < 1e-14:
        return math.sqrt(Q)
    half_h = hbar / 2.0
    sin_half = math.sin(half_h)
    if abs(sin_half) < 1e-300:
        return float('inf')
    ahat = half_h / sin_half
    return math.sqrt(Q) * ahat


# ============================================================================
# Section 8: c = 26 critical string analysis
# ============================================================================

def c26_analysis() -> Dict[str, Any]:
    r"""Full analysis at c = 26 (critical bosonic string).

    At c = 26: kappa(Vir_26) = 13.

    Shadow data:
        S_3 = 2, S_4 = 10/(26*152) = 5/1976, Delta = 8*13*5/1976 = 520/1976 = 65/247
        Q_Vir(t) = (26 + 6t)^2 + 2*(65/247)*t^2

    Shadow free energies:
        F_1 = 13/24, F_2 = 91/5760, F_3 = 403/967680, ...

    JT free energies:
        F_1^{JT} = pi^2/12, F_2^{JT} = 29*pi^8/552960, ...

    Ratios:
        R_1 = F_1^{JT}/F_1^{shadow} = (pi^2/12)/(13/24) = 2*pi^2/13

    The c = 26 shadow partition function:
        Z^{sh}(Vir_26, hbar) = 13 * ((hbar/2)/sin(hbar/2) - 1)
                              = 13 * (Ahat(i*hbar) - 1)

    This is not the JT partition function at any coupling.
    """
    c = 26.0
    constants = virasoro_shadow_constants(c)
    kappa = constants['kappa']

    shadow_energies = {}
    jt_energies = {}
    ratios = {}
    for g in range(1, 4):
        f_sh = F_g_shadow_virasoro(c, g)
        if isinstance(f_sh, Rational):
            f_sh = float(f_sh)
        shadow_energies[g] = f_sh
        try:
            f_jt = F_g_JT(g)
            jt_energies[g] = f_jt
            ratios[g] = f_jt / f_sh if abs(f_sh) > 1e-300 else float('inf')
        except ValueError:
            pass

    return {
        'c': c,
        'kappa': kappa,
        'S3': constants['S3'],
        'S4': constants['S4'],
        'Delta': constants['Delta'],
        'constants_status': constants['status'],
        'shadow_energies': shadow_energies,
        'jt_energies': jt_energies,
        'ratios': ratios,
        'ratio_constant': False,  # R_g varies with g
        'c_match_genus1': 4.0 * PI2,  # c where R_1 = 1
        'Q_at_0': shadow_spectral_curve(c, 0.0),  # = c^2 = 676
        'shadow_curve_zeros': shadow_curve_zeros(c),  # empty
        'jt_curve_zeros_first_5': jt_curve_zeros(5),
    }


# ============================================================================
# Section 9: Schwarzian limit (large c)
# ============================================================================

def schwarzian_limit_ratio(c_val: float, g: int) -> Dict[str, float]:
    r"""Conditional large-c diagnostic with an externally supplied JT scaling.

    In the Schwarzian limit c -> infinity:
        F_g^{shadow} = (c/2) * lambda_g^{FP}

    grows linearly in c, while F_g^{JT} is c-independent.

    The JT genus expansion includes an explicit coupling
    e^{S_0} at each genus:
        Z_JT = sum_g e^{S_0 (2-2g)} * Z_g(beta)

    The choice e^{S_0} = c/(4*pi^2) is not derived by this engine.
    It is a diagnostic scaling used to compare c-dependence.

    At genus 2: e^{S_0*(2-4)} = e^{-2*S_0} multiplies Z_2.
    Setting e^{S_0} = c/(4 pi^2):
        e^{-2*S_0} * V_{2,0} = (4 pi^2/c)^2 * V_{2,0}

    For the ratio to be 1:
        F_2^{shadow} = (c/2) * 7/5760 = 7c/11520
        e^{-2*S_0} * V_{2,0} = (4 pi^2/c)^2 * 29*pi^8/552960

    These scale differently with c: F_2^{shadow} ~ c, while the
    JT genus-2 with matching scales as ~ 1/c^2. They cannot agree
    at large c.

    The shadow and JT genus expansions involve different tautological
    integrals and different c-dependence.
    The shadow is a polynomial (degree 1) in c at each genus.
    The JT expansion is an asymptotic series in e^{-S_0} with c-independent
    coefficients, supplied by external WP/JT analysis.
    """
    f_sh = float(F_g_shadow_virasoro(c_val, g))
    try:
        f_jt = F_g_JT(g)
    except ValueError:
        return {'c': c_val, 'g': g, 'error': 'JT not tabulated'}

    # With genus counting parameter e^{S_0} = c/(4 pi^2)
    e_S0 = c_val / FOUR_PI2
    jt_weighted = e_S0 ** (2 - 2 * g) * f_jt

    return {
        'c': c_val,
        'g': g,
        'F_shadow': f_sh,
        'F_JT_bare': f_jt,
        'e_S0': e_S0,
        'F_JT_weighted': jt_weighted,
        'ratio': f_sh / jt_weighted if abs(jt_weighted) > 1e-300 else float('inf'),
        'scaling_status': CONDITIONAL,
        'jt_data_status': EXTERNAL_INPUT,
    }


# ============================================================================
# Section 10: Generating functions
# ============================================================================

def shadow_generating_function(kappa_val: float, hbar: float) -> float:
    r"""Shadow generating function sum_{g >= 1} F_g hbar^{2g}.

    Closed form: kappa * ((hbar/2)/sin(hbar/2) - 1).

    Scalar-lane convergence holds for |hbar| < 2*pi.  Poles occur at
    hbar = 2*pi*n.  JT Borel summability is a separate analytic input.
    """
    if abs(hbar) < 1e-14:
        return 0.0
    half = hbar / 2.0
    sin_half = math.sin(half)
    if abs(sin_half) < 1e-300:
        return float('inf')
    return kappa_val * (half / sin_half - 1.0)


def shadow_gf_virasoro(c_val: float, hbar: float) -> float:
    """Shadow generating function for Virasoro at central charge c."""
    return shadow_generating_function(c_val / 2.0, hbar)


def jt_partition_function_leading(beta: float, S0: float, g_max: int = 3) -> float:
    r"""Finite-window WP diagnostic with JT genus weights.

    Z_JT(beta) = sum_{g >= 0} e^{S_0*(2-2g)} * Z_g(beta)

    where Z_g(beta) involves the Laplace transform of V_{g,1}(b).

    This function does not compute the full beta-dependent JT partition
    function.  It returns the finite V_{g,0} comparison table with the usual
    genus weights, so it is useful only as a scaling diagnostic.
    Available for g = 1..3 (verified WP volumes in Mirzakhani convention).
    """
    # The full computation requires the Laplace transforms.
    result = 0.0
    for g in range(1, min(g_max, 3) + 1):
        try:
            Vg = F_g_JT(g)
            result += math.exp(S0 * (2 - 2 * g)) * Vg
        except ValueError:
            break
    return result


# ============================================================================
# Section 11: Matrix model at c = 26
# ============================================================================

def matrix_size_from_kappa(kappa_val: float) -> Dict[str, float]:
    r"""Matrix model interpretation of kappa.

    The Gaussian matrix model identification:
        F_g^{GUE}(N^2 = kappa) = kappa * lambda_g^{FP}

    gives the shadow free energy as a GUE genus expansion with N^2 = kappa.

    For Virasoro at c = 26: kappa = 13, so N^2 = 13, N = sqrt(13) ~ 3.606.

    This is not a physical matrix size (not an integer). The matrix model
    is the TOPOLOGICAL (formal) matrix model, where N is a continuous parameter.

    In the double-scaled limit (relevant for JT), N -> infinity with
    specific scaling. A finite-c shadow model needs separate analytic input
    to produce a double-scaled JT limit.
    """
    N_squared = kappa_val
    N = math.sqrt(kappa_val) if kappa_val >= 0 else float('nan')
    return {
        'kappa': kappa_val,
        'N_squared': N_squared,
        'N': N,
        'is_integer_N': abs(N - round(N)) < 1e-10,
        # For JT: N -> infinity (double-scaled limit)
        'JT_regime': 'N -> infinity (double-scaled)',
        'shadow_regime': f'N = {N:.6f} (finite)',
        'double_scaled_JT_limit_certified': False,
    }


# ============================================================================
# Section 12: Large-g asymptotics
# ============================================================================

def shadow_large_g_asymptotic(kappa_val: float, g: int) -> float:
    r"""Large-g asymptotic of the shadow free energy.

    F_g^{shadow} = kappa * lambda_g^{FP}
                 ~ kappa * 2 / (2*pi)^{2g}   (for g >> 1)

    The Bernoulli asymptotic: |B_{2g}| ~ 2 * (2g)! / (2*pi)^{2g}
    gives lambda_g^{FP} ~ 2 / (2*pi)^{2g} * (1 - 2^{1-2g}).

    The shadow free energy decays exponentially: F_g ~ C * (2*pi)^{-2g}.
    """
    return kappa_val * 2.0 / TWO_PI ** (2 * g)


def jt_large_g_asymptotic(g: int) -> float:
    r"""Logarithmic large-g diagnostic for JT/WP growth.

    From Zograf (2008): V_{g,0} ~ C * (2*pi^2)^{2g} * (2g)!^{-alpha}

    The WP volumes grow factorially in g (roughly like (2g)!),
    in sharp contrast with the shadow free energies which decay exponentially.

    This returns a log-scale diagnostic, not an exact volume and not a
    Borel-summability certificate.
    """
    # Rough asymptotic: V_{g,0} ~ C * (3g-3)! * (2*pi^2)^{3g-3} * (3g-3)^{-5/2}
    d = 3 * g - 3  # complex dimension of M_g
    if d < 0:
        return 0.0
    # Use a Zograf-type asymptotic scale:
    # V_{g,0} ~ C * Gamma(3g - 3/2) * (4*pi^2)^{2g-2} / (4*pi * (3g-3))
    # For large g: this grows as (3g)^{3g} roughly.
    # Numerical estimate:
    return math.lgamma(d + 0.5) + (2 * g - 2) * math.log(FOUR_PI2) - math.log(4.0 * PI * d)


def asymptotic_ratio(kappa_val: float, g: int) -> Dict[str, float]:
    r"""Ratio of JT to shadow free energies in the large-g regime.

    The difference:
    - Shadow: F_g^{shadow} ~ (2*pi)^{-2g}  (exponential decay)
    - JT:     F_g^{JT} ~ (2g)!-type growth (factorial growth)

    The divergence statement uses external WP asymptotics.  The engine can
    certify scalar Bernoulli decay and finite-window mismatches; it records
    the large-g JT comparison as an external diagnostic.
    """
    f_sh = float(F_g_shadow(kappa_val, g))
    f_sh_asymp = shadow_large_g_asymptotic(kappa_val, g)
    try:
        f_jt = F_g_JT(g)
        return {
            'g': g,
            'F_shadow': f_sh,
            'F_shadow_asymp': f_sh_asymp,
            'F_JT': f_jt,
            'ratio': f_jt / f_sh if abs(f_sh) > 1e-300 else float('inf'),
            'jt_asymptotic_status': EXTERNAL_INPUT,
        }
    except ValueError:
        return {
            'g': g,
            'F_shadow': f_sh,
            'F_shadow_asymp': f_sh_asymp,
            'F_JT': None,
            'ratio': None,
            'jt_asymptotic_status': EXTERNAL_INPUT,
        }


# ============================================================================
# Section 13: Summary structural comparison
# ============================================================================

def full_structural_comparison(c_val: float = 26.0) -> Dict[str, Any]:
    r"""Complete structural comparison between shadow and JT at given c.

    Returns computed quantities together with certification status for each
    analytic claim.
    """
    kappa = c_val / 2.0
    certification = gravity_claim_certification()

    # Free energies at each genus
    genus_data = {}
    for g in range(1, 4):
        f_sh = float(F_g_shadow_virasoro(c_val, g))
        try:
            f_jt = F_g_JT(g)
            ratio = f_jt / f_sh if abs(f_sh) > 1e-300 else float('inf')
        except ValueError:
            f_jt = None
            ratio = None
        genus_data[g] = {
            'F_shadow': f_sh,
            'F_JT': f_jt,
            'ratio': ratio,
        }

    # Check if ratio is constant
    ratios = [d['ratio'] for d in genus_data.values() if d['ratio'] is not None]
    ratio_constant = (len(ratios) >= 2 and
                      all(abs(r / ratios[0] - 1.0) < 0.01 for r in ratios[1:]))

    # Spectral curve data
    shadow_Q_at_0 = shadow_spectral_curve(c_val, 0.0)
    shadow_zeros = shadow_curve_zeros(c_val)
    jt_zeros = jt_curve_zeros(5)

    # Matrix model data
    mm = matrix_size_from_kappa(kappa)

    return {
        'c': c_val,
        'kappa': kappa,
        'genus_data': genus_data,
        'ratio_constant': ratio_constant,
        'ratio_values': ratios,
        'certification': certification,
        # Structural conclusions with explicit scope.
        'scalar_shadow_convergent': True,
        'scalar_shadow_convergence_status': CERTIFIED,
        'shadow_convergent': True,
        'shadow_convergent_scope': 'scalar Bernoulli/A-hat lane only',
        'scalar_convergence_radius': '2*pi',
        'exact_scalar_radius_status': CERTIFIED,
        'jt_asymptotic': None,
        'jt_asymptotic_status': EXTERNAL_INPUT,
        'borel_summability_status': NON_CERTIFIED,
        'shadow_curve_algebraic': True,
        'jt_curve_transcendental': True,
        'shadow_curve_has_zeros': len(shadow_zeros) > 0,
        'jt_curve_has_zeros': True,
        'jt_zeros_count': 'infinite',
        'shadow_zeros_count': len(shadow_zeros),
        'matrix_model': mm,
        'eo_recursion_from_shadow_curve_status': CONDITIONAL,
        'full_EO_recursion_certified_from_Q_L': False,
        'btz_closed_form_recovery_status': NON_CERTIFIED,
        'all_genus_3d_partition_theorem_status': NON_CERTIFIED,
        'shadow_equals_JT': False,
        'full_jt_partition_from_shadow': False,
        'reason': ('Shadow involves lambda-class intersections (A-hat GF, convergent). '
                   'JT involves kappa-class intersections (WP volumes, factorial). '
                   'The ratio R_g is not constant in g. '
                   'The spectral curves are algebraic vs transcendental. '
                   'Analytic JT and 3D gravity claims need external input.'),
    }


# ============================================================================
# Section 14: What IS the connection? (positive results)
# ============================================================================

def connection_via_topological_recursion(c_val: float) -> Dict[str, Any]:
    r"""Status of the topological-recursion comparison.

    The shadow and JT lanes use different spectral data:

    - Shadow: y^2 = Q_L(t) (polynomial, finite-order matrix model)
    - JT: y^2 = sin^2(2 pi sqrt(x))/(16 pi^2) (transcendental, double-scaled)

    An EO recursion for a shadow theory requires the spectral curve,
    Bergman kernel, local involution, loop equations, and recursion kernel.
    The quadratic shadow metric alone supplies only the first item.

    1. The shadow at finite c is a polynomial/algebraic matrix-model lane.
       For class G: Gaussian. For class M: infinite polynomial.

    2. JT is the double-scaled limit of a Hermitian matrix model.

    3. Any double-scaling identification between shadow data and a JT sector
       is external analytic input, not certified here.

    4. The genus-1 match is exact because lambda_1 = kappa_1/12 (Mumford).
       Higher genus matches require the full Mumford relations, which do not
       give a simple proportionality.

    They share the moduli-space substrate M_{g,n}, weighted differently
    (lambda classes versus kappa/WP classes).
    """
    kappa = c_val / 2.0
    return {
        'c': c_val,
        'kappa': kappa,
        # Genus-1 exact match (Mumford relation lambda_1 = kappa_1/12)
        'genus_1_match': True,
        'genus_1_match_status': CERTIFIED,
        'genus_1_proportionality': 4.0 * PI2 / c_val,  # R_1 = 4*pi^2/c
        # Higher genus: no simple proportionality
        'higher_genus_match': False,
        # Topological recursion status.
        'both_from_top_rec': None,
        'shadow_EO_status': CONDITIONAL,
        'jt_sine_curve_status': EXTERNAL_INPUT,
        'full_EO_recursion_from_shadow_curve': False,
        'double_scaled_JT_sector_certified': False,
        # On different spectral curves
        'same_spectral_curve': False,
        'shadow_curve_type': 'polynomial (algebraic)',
        'jt_curve_type': 'trigonometric (transcendental)',
        # The deep connection: same moduli space, different integrands
        'common_substrate': 'M_{g,n}',
        'shadow_integrand': 'lambda_g * psi^{2g-2} (A-hat class)',
        'jt_integrand': 'exp(2*pi^2*kappa_1) (WP form)',
        # The operational distinction
        'shadow_convergence': 'scalar A-hat lane convergent with radius 2*pi',
        'jt_convergence': 'external WP/JT asymptotic input; Borel summability not certified here',
        'borel_summability_status': NON_CERTIFIED,
    }


# ============================================================================
# Section 15: Verification utilities
# ============================================================================

def verify_lambda_fp_values() -> Dict[int, Tuple[Fraction, bool]]:
    r"""Cross-verify lambda_g^{FP} values at low genus.

    lambda_1 = 1/24       (B_2 = 1/6,  factor = 1/2)
    lambda_2 = 7/5760     (B_4 = -1/30, factor = 3/4)
    lambda_3 = 31/967680  (B_6 = 1/42,  factor = 7/8)
    """
    expected = {
        1: Fraction(1, 24),
        2: Fraction(7, 5760),
        3: Fraction(31, 967680),
    }
    results = {}
    for g, exp_val in expected.items():
        computed = lambda_fp_exact(g)
        results[g] = (computed, computed == exp_val)
    return results


def verify_jt_genus1() -> Dict[str, float]:
    r"""Cross-verify F_1^{JT} = V_{1,1}(0) = pi^2/12.

    Path 1: Direct formula pi^2/12.
    Path 2: From V_{1,1}(b) = (b^2 + 4*pi^2)/48, set b = 0.
    Path 3: From the WP symplectic form: V_{1,1}(0) = int_{M_{1,1}} exp(omega_WP)
            where M_{1,1} has dim_C = 1, so V_{1,1}(0) = 2*pi^2 * <kappa_1>_{1,1}
            = 2*pi^2 * (1/24) = pi^2/12.
    """
    direct = PI2 / 12.0
    from_polynomial = (0.0 + 4.0 * PI2) / 48.0
    from_intersection = 2.0 * PI2 * (1.0 / 24.0)
    return {
        'direct': direct,
        'from_polynomial': from_polynomial,
        'from_intersection': from_intersection,
        'all_agree': abs(direct - from_polynomial) < 1e-14 and abs(direct - from_intersection) < 1e-14,
    }


def verify_ratio_g1(c_val: float) -> Dict[str, float]:
    r"""Verify the genus-1 ratio R_1 = 4*pi^2/c.

    F_1^{JT} = pi^2/12.
    F_1^{shadow} = (c/2) * (1/24) = c/48.
    R_1 = (pi^2/12) / (c/48) = 4*pi^2/c.

    R_1 = F_1^JT / F_1^shadow = (pi^2/12) / (c/48)
         = (pi^2/12) * (48/c) = 4*pi^2/c.
    """
    f1_jt = PI2 / 12.0
    f1_sh = c_val / 48.0
    r1_computed = f1_jt / f1_sh
    r1_formula = 4.0 * PI2 / c_val
    return {
        'c': c_val,
        'F_1_JT': f1_jt,
        'F_1_shadow': f1_sh,
        'R_1_computed': r1_computed,
        'R_1_formula': r1_formula,
        'agree': abs(r1_computed - r1_formula) < 1e-12,
    }
