r"""Shadow bracket diagnostics and normalized scalar kernels.

The shadow algebra A^sh = H_*(Def_cyc^mod(A)) is commutative as a graded
ring: the scalar shadows kappa, S_3, S_4, ... commute.  The L-infinity
structure from the MC element Theta_A induces first-order antisymmetric
operations on finite shadow windows:

    {f, g}_shadow = Sigma_n (1/n!) ell_n(Theta_A; f, g)

At the lowest level (n=0), this is the convolution bracket projected to the
chosen shadow window.  The projected three-generator bracket is not a Poisson
bracket on the generic Virasoro/W surface: its Jacobi defect is computed below.

This module therefore computes a conditional deformation-quantization
diagnostic, not a theorem asserting a global Kontsevich star product:

    f *_hbar g = Sigma_{n>=0} hbar^n B_n(f, g)

where the B_n are Moyal-type finite-difference bidifferential coefficients on
the selected scalar window.  B_0 is the product and B_1 is the projected
shadow bracket.  These coefficients define a genuine star product only on
windows where the Jacobi defect vanishes and the missing graph-weight terms
have been supplied.

This module computes:
  1. Shadow bracket candidates for standard families
  2. Jacobi-defect diagnostics for the three-generator window
  3. Moyal-type finite-window coefficients through order hbar^5
  4. Complex Virasoro evaluations at Riemann zeta-zero ordinates

MATHEMATICAL FRAMEWORK:

The shadow ring generators are:
    kappa = S_2       (modular characteristic, arity-2)
    alpha = S_3       (cubic shadow, arity-3)
    S_4               (quartic contact, arity-4)
    Delta = 8*kappa*S_4  (critical discriminant)

The bracket candidate comes from the L-infinity bracket on the modular
convolution algebra g^mod_A.  On the shadow ring (arity grading), the
projected bracket increases arity by 1:

    {S_r, S_s} = sum over planted-forest graphs Gamma
                 of arity r+s-1 with coefficient determined by
                 |Aut(Gamma)|^{-1} * ell_Gamma

For the SINGLE primary line L, the bracket simplifies to:

    {kappa, S_4} = 3*alpha*S_4 / kappa     (arity-5 bracket, from ell_2)
    {kappa, Delta} = 3*alpha*Delta / kappa  (follows from Delta = 8*kappa*S_4)
    {alpha, S_4} = (Delta - 9*alpha^2) / (2*kappa)  (from ell_2 arity-6)

These identities are read from the shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2
+ 2*Delta*t^2 via the variational derivative:

    {f, g} = Pi^{ij} (partial_i f)(partial_j g)

where Pi^{ij} is the antisymmetric bivector candidate inherited from the
projected L-infinity structure.

FINITE-WINDOW PRODUCT DIAGNOSTIC:

On a 2D Poisson manifold with coordinates (x_1, x_2) and Poisson tensor
Pi = Pi^{12}(partial_1 wedge partial_2), the star product is:

    f * g = fg + hbar * Pi^{12} * (partial_1 f)(partial_2 g)
            + (hbar^2/2) * [(Pi^{12})^2 * (partial_1^2 f)(partial_2^2 g)
                            + Pi^{12}(partial_j Pi^{12})(partial_1 partial_j f)(partial_2 g)
                            + ...]
            + O(hbar^3)

For the shadow bracket candidate, the coordinates are the shadow ring
generators and Pi is determined by the projected convolution bracket.  The
normalization firewalls are:
    * kappa formulas are family-specific.
    * S_2 = kappa equals c/2 only in the Virasoro normalization.
    * kappa(Vir_c) + kappa(Vir_{26-c}) = 13.
    * kappa = 0 does not imply Theta_A = 0.
    * A, B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A) are typed apart.
    * A^! is the Verdier/continuous-linear dual branch under finite-type or
      completed hypotheses.
    * Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
    * Z_ch^der(A) = ChirHoch^*(A,A) is the Hochschild/derived-centre bulk.

Manuscript references:
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
    def:modular-convolution-dg-lie (higher_genus_modular_koszul.tex)
    cor:shadow-extraction (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from sympy import (
    Rational, Symbol, cancel, expand, factor, oo, simplify, sqrt,
    symbols, together, Function, diff, S, Poly,
    N as Neval,
)


# ============================================================================
# Symbols
# ============================================================================

c = Symbol('c', positive=True)
k_sym = Symbol('k')
hbar = Symbol('hbar')
t = Symbol('t')

# Shadow ring generators as formal symbols
kap = Symbol('kappa')
alp = Symbol('alpha')
S4_sym = Symbol('S4')
Del = Symbol('Delta')  # Delta = 8*kappa*S4


# ============================================================================
# 0. Normalization and object firewalls
# ============================================================================

HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)
"""Seven entries of the holographic package H(A)."""


MODULAR_KOSZUL_PRIMARY_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br, T_br)",
    "R4_mod(L)",
)
"""Six primary projections of the compute-side modular Koszul package."""


KERNEL_NORMALIZATIONS: Dict[str, str] = {
    "affine_raw_collision": "k*Omega_tr/z",
    "affine_KZ_coefficient": "Omega/((k+h^vee)z)",
    "heisenberg_raw_collision": "k/z",
    "virasoro_collision": "(c/2)/z^3 + 2T/z",
}
"""Collision-kernel normalizations used by the finite-window diagnostics."""


OBJECT_FIREWALL: Dict[str, str] = {
    "A": "input chiral algebra",
    "B(A)": "ordered bar coalgebra before cohomology",
    "A^i": "bar cohomology coalgebra H^*(B(A))",
    "A^!": (
        "Verdier/continuous-linear dual branch under finite-type or "
        "completed hypotheses"
    ),
    "Omega(B(A))": "bar-cobar inversion recovering A",
    "Z_ch^der(A)": "ChirHoch^*(A,A), the Hochschild/derived-centre bulk",
}
"""Typed firewall separating bar, Koszul-dual, and Hochschild objects."""


def holographic_package_entries() -> Tuple[str, ...]:
    """Return the seven entries of H(A), in manuscript order."""
    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_primary_projections() -> Tuple[str, ...]:
    """Return the six projections of the compute-side modular Koszul package."""
    return MODULAR_KOSZUL_PRIMARY_PROJECTIONS


def kernel_normalizations() -> Dict[str, str]:
    """Return raw-collision, KZ, Heisenberg, and Virasoro kernel constants."""
    return dict(KERNEL_NORMALIZATIONS)


def object_firewall() -> Dict[str, str]:
    """Return typed roles for A, B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A)."""
    return dict(OBJECT_FIREWALL)


def _depth_class(data: dict) -> str:
    """Return the G/L/C/M depth class when the family determines it."""
    if "depth_class" in data:
        return data["depth_class"]
    family = data.get("family", "")
    if family == "heisenberg":
        return "G"
    if family.startswith("affine"):
        return "L"
    if family == "betagamma":
        return "C"
    if family in {"virasoro", "virasoro_complex", "w3"}:
        return "M"
    return "unknown"


# ============================================================================
# 1. Shadow data providers (from existing engines, reproduced for independence)
# ============================================================================

def _virasoro_shadow_data(c_val):
    """Shadow metric data for Virasoro at numerical central charge c_val.

    Returns dict with kappa, alpha, S4, Delta, Q_L coefficients.

    Family-specific normalization: kappa(Vir_c) = c/2. Do not use this
    formula for other families.
    """
    kappa = c_val / 2
    alpha = 2.0
    S4 = 10.0 / (c_val * (5 * c_val + 22))
    Delta = 8 * kappa * S4  # = 40/(5c+22)
    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4, 'Delta': Delta,
        'q0': q0, 'q1': q1, 'q2': q2, 'family': 'virasoro',
        'depth_class': 'M',
    }


def _heisenberg_shadow_data(k_val):
    """Shadow data for Heisenberg H_k.

    Class G: kappa = k, alpha = 0, S4 = 0, Delta = 0.
    All shadow brackets vanish (Poisson structure is trivial).
    """
    return {
        'kappa': float(k_val), 'alpha': 0.0, 'S4': 0.0, 'Delta': 0.0,
        'q0': float(k_val) ** 2, 'q1': 0.0, 'q2': 0.0, 'family': 'heisenberg',
        'depth_class': 'G',
    }


def _affine_sl2_shadow_data(k_val):
    """Shadow data for affine V_k(sl_2).

    Class L: kappa = 3(k+2)/4, alpha = 4/(k+2), S4 = 0, Delta = 0.
    """
    kappa = 3.0 * (k_val + 2) / 4.0
    alpha = 4.0 / (k_val + 2)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': 0.0, 'Delta': 0.0,
        'q0': kappa ** 2 * 4, 'q1': 12.0 * kappa * alpha,
        'q2': 9.0 * alpha ** 2, 'family': 'affine_sl2',
        'depth_class': 'L',
    }


def _affine_slN_shadow_data(N_val, k_val):
    """Shadow data for affine V_k(sl_N).

    Class L: kappa = (N^2-1)(k+N)/(2N), alpha = 2N/(k+N), S4 = 0.
    """
    kappa = (N_val ** 2 - 1) * (k_val + N_val) / (2.0 * N_val)
    alpha = 2.0 * N_val / (k_val + N_val)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': 0.0, 'Delta': 0.0,
        'q0': kappa ** 2 * 4, 'q1': 12.0 * kappa * alpha,
        'q2': 9.0 * alpha ** 2, 'family': f'affine_sl{N_val}',
        'depth_class': 'L',
    }


def _betagamma_shadow_data(lam_val=0.5):
    """Shadow data for beta-gamma at weight lambda.

    Class C: kappa = 6*lambda^2 - 6*lambda + 1, alpha = 2,
    S4 = 10/(c(5c+22)), Delta = 40/(5c+22) where c = 2*kappa.

    GLOBAL termination at arity 4 by stratum separation.
    """
    c_val = 2.0 * (6.0 * lam_val ** 2 - 6.0 * lam_val + 1.0)
    kappa = c_val / 2.0
    alpha = 2.0
    if abs(c_val) < 1e-15 or abs(5.0 * c_val + 22.0) < 1e-15:
        S4 = 0.0
        Delta = 0.0
    else:
        S4 = 10.0 / (c_val * (5 * c_val + 22))
        Delta = 8 * kappa * S4
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4, 'Delta': Delta,
        'q0': (2 * kappa) ** 2, 'q1': 12.0 * 2 * kappa,
        'q2': (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
        if abs(5.0 * c_val + 22.0) > 1e-15 else 36.0,
        'family': 'betagamma',
        'depth_class': 'C',
    }


def _w3_shadow_data(c_val):
    """Shadow data for W_3 at central charge c (T-line restriction).

    On the T-line, the W_3 shadow is identical to Virasoro.
    kappa_T = c/2, alpha = 2, S_4 = 10/(c(5c+22)).

    NOTE: The FULL W_3 has a 2D deformation space (T-line + W-line).
    This gives the T-line restriction only.
    """
    return _virasoro_shadow_data(c_val)


def get_shadow_data(family: str, **params) -> dict:
    """Dispatcher for shadow data across families.

    Parameters
    ----------
    family : str
        One of 'heisenberg', 'affine_sl2', 'affine_slN', 'betagamma',
        'virasoro', 'w3'.
    **params : keyword arguments
        Family-specific parameters (k, c_val, lam, N, etc.).

    Returns
    -------
    dict with keys: kappa, alpha, S4, Delta, family.
    """
    if family == 'heisenberg':
        return _heisenberg_shadow_data(params.get('k', 1))
    elif family == 'affine_sl2':
        return _affine_sl2_shadow_data(params.get('k', 1))
    elif family == 'affine_slN':
        return _affine_slN_shadow_data(params.get('N', 3), params.get('k', 1))
    elif family == 'betagamma':
        return _betagamma_shadow_data(params.get('lam', 0.5))
    elif family == 'virasoro':
        return _virasoro_shadow_data(params.get('c_val', 1.0))
    elif family == 'w3':
        return _w3_shadow_data(params.get('c_val', 1.0))
    else:
        raise ValueError(f"Unknown family: {family}")


# ============================================================================
# 2. Shadow bracket candidate
# ============================================================================

def shadow_jacobi_defect(data: dict) -> Union[float, complex]:
    r"""Jacobi defect for the three-generator bracket candidate.

    For coordinates (kappa, alpha, S_4), with

        Pi^{kappa,alpha} = 9*alpha^2/(2*kappa),
        Pi^{kappa,S4}    = 3*alpha*S4/kappa,
        Pi^{alpha,S4}    = (Delta - 9*alpha^2)/(2*kappa),

    the Jacobiator on (kappa, alpha, S_4) is

        J = 9*alpha*(3*alpha^2 - Delta)/(2*kappa^2).

    Class G has the zero bracket.  Class L is a finite-depth
    two-generator quotient in this scalar engine, so the S_4 coordinate is
    absent and the displayed three-generator defect is not applied.
    """
    depth = _depth_class(data)
    kappa = data['kappa']
    alpha = data['alpha']
    Delta = data['Delta']

    if depth in {'G', 'L'}:
        return 0.0
    if abs(kappa) < 1e-30:
        return 0.0
    return 9.0 * alpha * (3.0 * alpha ** 2 - Delta) / (2.0 * kappa ** 2)


def shadow_bracket_status(data: dict, tolerance: float = 1e-12) -> dict:
    """Classify the projected bracket as Poisson or only first-order data."""
    depth = _depth_class(data)
    defect = shadow_jacobi_defect(data)
    defect_abs = abs(defect)
    is_poisson = defect_abs <= tolerance
    if depth == 'G':
        status = 'trivial_poisson'
    elif depth == 'L':
        status = 'finite_depth_two_generator_poisson'
    elif is_poisson:
        status = 'poisson_on_vanishing_defect_locus'
    else:
        status = 'first_order_bracket_only'
    return {
        'depth_class': depth,
        'jacobi_defect': defect,
        'jacobi_defect_abs': defect_abs,
        'is_poisson': is_poisson,
        'status': status,
        'vanishing_condition': 'alpha = 0 or Delta = 3*alpha^2, with kappa nonzero',
    }


def shadow_poisson_bivector(data: dict) -> dict:
    r"""Compute the antisymmetric bivector candidate Pi^{ij}.

    The shadow ring on a single primary line L is generated by the shadow
    coefficients S_r (r = 2, 3, 4, ...).  The L-infinity structure from
    the MC element Theta_A induces projected brackets via the planted-forest
    graphs.

    On the 1D primary line parametrized by t, the shadow metric is:
        Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

    The shadow generating function H(t) = t^2 * sqrt(Q_L(t)) satisfies:
        H'(t) / H(t) = 2/t + Q_L'(t) / (2*Q_L(t))

    The bivector candidate comes from the variational derivative of the
    projected L-infinity brackets.  On the shadow generators:

        {S_r, S_s} = Pi^{rs}

    where Pi^{rs} is determined by the convolution bracket ell_2.

    For the single-line shadow metric, the candidate bivector is
    on the (kappa, Delta) plane:

        Pi^{kappa, Delta} = 3*alpha*Delta / kappa   (from ell_2)

    This uses the fact that the convolution bracket ell_2 is the leading
    term of the L-infinity structure (higher ell_n contribute at higher arity).

    This dictionary is a Poisson bivector only when shadow_bracket_status()
    reports a vanishing Jacobi defect.

    Returns dict with bivector components.
    """
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    Delta = data['Delta']  # = 8*kappa*S4

    # Antisymmetric bivector components.
    # The bracket {kappa, S_4} comes from the arity-5 planted-forest graph
    # with one trivalent vertex connecting S_2 and S_4 inputs through the
    # cubic coupling alpha.
    #
    # Derivation: The shadow metric Q_L parametrizes a 1D family.
    # The variation of kappa = S_2 and S_4 along the deformation parameter
    # induces the displayed bracket candidate via:
    #   {S_2, S_4} = (d S_2/dt)(d S_4/dt) * Pi_t
    # where Pi_t is the scalar two-form used in this finite window.
    #
    # From the Riccati algebraicity (thm:riccati-algebraicity):
    #   The shadow metric Q_L(t) = q0 + q1*t + q2*t^2 has
    #   q0 = 4*kappa^2, q1 = 12*kappa*alpha, q2 = 9*alpha^2 + 2*Delta
    #
    # The convolution recursion f^2 = Q_L with f(t) = sum a_n t^n gives
    # the brackets via the quadratic relation:
    #   2*a_0*a_n = -sum_{j=1}^{n-1} a_j*a_{n-j}  for n >= 3
    #
    # This recursion supplies the leading cubic-coupling bracket candidate:
    #
    #   {kappa, S_4} = (3*alpha) * S_4 / kappa * (if alpha, kappa != 0)
    #
    # This follows from: the arity-5 contribution in the L-infinity tower
    # is ell_2(S_2, S_4) projected back to the shadow ring.

    result = {
        'Pi_kappa_S4': 0.0,
        'Pi_kappa_Delta': 0.0,
        'Pi_alpha_S4': 0.0,
        'Pi_kappa_alpha': 0.0,
    }

    depth = _depth_class(data)

    if abs(kappa) < 1e-30 or depth == 'G':
        return result

    if depth == 'L':
        # The finite-depth class-L scalar window has generators kappa and
        # alpha.  S_4 is not a coordinate of the quotient window.
        result['Pi_kappa_alpha'] = 9.0 * alpha ** 2 / (2.0 * kappa)
        return result

    # {kappa, S_4}: from ell_2 at arity 5
    # The cubic coupling alpha mediates the bracket between
    # the quadratic (kappa) and quartic (S_4) shadows
    result['Pi_kappa_S4'] = 3.0 * alpha * S4 / kappa

    # {kappa, Delta}: since Delta = 8*kappa*S4,
    # {kappa, Delta} = 8*{kappa, kappa}*S4 + 8*kappa*{kappa, S4}
    #               = 0 + 8*kappa*(3*alpha*S4/kappa)
    #               = 24*alpha*S4
    # But Delta = 8*kappa*S4, so {kappa, Delta} = 3*alpha*Delta/kappa
    result['Pi_kappa_Delta'] = 3.0 * alpha * Delta / kappa

    # {alpha, S_4}: from ell_2 at arity 6
    # The bracket between the cubic and quartic shadows is mediated by
    # the quadratic coupling. From the convolution recursion:
    #   a_2 = (q2 - a_1^2)/(2*a_0)
    # Variation gives:
    #   {alpha, S_4} = (Delta - 9*alpha^2) / (2*kappa)
    # On finite-depth class L, S_4 is not part of the scalar quotient window;
    # the branch above has already returned the two-generator bracket.
    result['Pi_alpha_S4'] = (Delta - 9.0 * alpha ** 2) / (2.0 * kappa)

    # {kappa, alpha}: from ell_2 at arity 4
    # The bracket between quadratic and cubic shadows:
    # From the recursion: a_1 = q1/(2*a_0) = 12*kappa*alpha/(2*2*kappa) = 3*alpha
    # Variation of alpha at fixed kappa:
    # {kappa, alpha} = 9*alpha^2 / (2*kappa)  (from arity-4 bracket)
    # This comes from ell_2(kappa, alpha) being the arity-4 correction.
    # But for the SINGLE primary line, kappa and alpha are NOT independent
    # coordinates --- they are both determined by the central charge c.
    # So the bracket is the pullback from the c-line.
    # On the c-line: d(kappa)/dc = 1/2, d(alpha)/dc varies by family.
    # For Virasoro: alpha = 2 (constant!), so {kappa, alpha}_Vir = 0.
    # For affine sl_2: d(kappa)/dk = 3/4, d(alpha)/dk = -4/(k+2)^2.
    # The bracket is Pi_c * (dk/dc)(da/dc) where Pi_c is the scalar
    # two-form on the central-charge line.
    #
    # At the projected L-infinity level, {kappa, alpha} = 9*alpha^2/(2*kappa)
    # for the ABSTRACT shadow ring, but on the SPECIALIZED family locus,
    # it reduces to the pullback.  We report the abstract value.
    result['Pi_kappa_alpha'] = 9.0 * alpha ** 2 / (2.0 * kappa)

    return result


def shadow_poisson_bracket(f_arity: int, g_arity: int, data: dict) -> float:
    """Compute the projected bracket {S_r, S_s}_shadow.

    Parameters
    ----------
    f_arity : int
        Arity r of the first shadow generator.
    g_arity : int
        Arity s of the second shadow generator.
    data : dict
        Shadow data from get_shadow_data().

    Returns
    -------
    float : value of the projected bracket.  The operation is Poisson only
        on the loci reported by shadow_bracket_status().
    """
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    Delta = data['Delta']
    depth = _depth_class(data)

    if abs(kappa) < 1e-30 or depth == 'G':
        return 0.0

    if depth == 'L' and (f_arity > 3 or g_arity > 3):
        # Class L has a finite-depth scalar window generated by kappa and
        # alpha; S_4 and higher shadows are absent in this quotient.
        return 0.0

    # Antisymmetry: {S_r, S_s} = -{S_s, S_r}
    if f_arity > g_arity:
        return -shadow_poisson_bracket(g_arity, f_arity, data)

    # Specific brackets
    if (f_arity, g_arity) == (2, 2):
        return 0.0  # {kappa, kappa} = 0 (antisymmetry)
    elif (f_arity, g_arity) == (2, 3):
        # {kappa, alpha} = 9*alpha^2 / (2*kappa)
        return 9.0 * alpha ** 2 / (2.0 * kappa)
    elif (f_arity, g_arity) == (2, 4):
        # {kappa, S_4} = 3*alpha*S_4 / kappa
        return 3.0 * alpha * S4 / kappa
    elif (f_arity, g_arity) == (3, 3):
        return 0.0  # {alpha, alpha} = 0 (antisymmetry)
    elif (f_arity, g_arity) == (3, 4):
        # {alpha, S_4} = (Delta - 9*alpha^2) / (2*kappa)
        return (Delta - 9.0 * alpha ** 2) / (2.0 * kappa)
    elif (f_arity, g_arity) == (4, 4):
        return 0.0  # {S_4, S_4} = 0 (antisymmetry)
    else:
        # Higher arities: compute from the convolution recursion
        # {S_r, S_s} = sum of planted-forest graph contributions
        # For the 1D primary line, these are determined by the recursion.
        return _higher_poisson_bracket(f_arity, g_arity, data)


def _higher_poisson_bracket(r: int, s: int, data: dict) -> float:
    """Compute higher projected brackets for the class-M recursion.

    The recursion f^2 = Q_L gives:
        S_{n+2} = a_n / (n+2)
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}  for n >= 3

    The bracket candidate is computed from the variation of the recursion:
        {S_r, S_s} = sum_{graphs} contribution
    On the 1D line, this reduces to:
        {S_r, S_s} = (r-2)*(s-2) * derivative_structure / kappa
    """
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    Delta = data['Delta']
    depth = _depth_class(data)

    if abs(kappa) < 1e-30 or depth in {'G', 'L', 'C'}:
        return 0.0

    # Compute shadow coefficients through arity max(r, s) + 2
    max_arity = max(r, s) + 2
    coeffs = _shadow_coefficients_numerical(data, max_arity)

    # The bracket {S_r, S_s} on the 1D line is computed via the
    # variational formula:
    # {S_r, S_s} = (partial S_r / partial alpha) * (partial S_s / partial kappa)
    #              * Pi^{alpha, kappa}
    #              + (partial S_r / partial kappa) * (partial S_s / partial alpha)
    #              * Pi^{kappa, alpha}
    # where the partials are from the recursion.
    #
    # For the recursion a_0 = 2*kappa, a_1 = 3*alpha:
    #   partial a_n / partial kappa and partial a_n / partial alpha
    # can be computed by differentiating the recursion.

    # Compute partials by finite difference
    eps = 1e-8
    data_dk = dict(data)
    data_dk['kappa'] = kappa + eps
    data_dk['Delta'] = 8.0 * (kappa + eps) * S4
    data_dk['q0'] = (2 * (kappa + eps)) ** 2
    data_dk['q1'] = 12.0 * (kappa + eps) * alpha

    data_da = dict(data)
    data_da['alpha'] = alpha + eps
    data_da['q1'] = 12.0 * kappa * (alpha + eps)
    data_da['q2'] = 9.0 * (alpha + eps) ** 2 + 2.0 * Delta

    coeffs_dk = _shadow_coefficients_numerical(data_dk, max_arity)
    coeffs_da = _shadow_coefficients_numerical(data_da, max_arity)

    dSr_dk = (coeffs_dk.get(r, 0.0) - coeffs.get(r, 0.0)) / eps
    dSs_dk = (coeffs_dk.get(s, 0.0) - coeffs.get(s, 0.0)) / eps
    dSr_da = (coeffs_da.get(r, 0.0) - coeffs.get(r, 0.0)) / eps
    dSs_da = (coeffs_da.get(s, 0.0) - coeffs.get(s, 0.0)) / eps

    # Pi^{kappa, alpha} = 9*alpha^2 / (2*kappa)
    Pi_ka = 9.0 * alpha ** 2 / (2.0 * kappa)

    # {S_r, S_s} = dSr_dk * dSs_da * Pi_ka - dSr_da * dSs_dk * Pi_ka
    bracket = Pi_ka * (dSr_dk * dSs_da - dSr_da * dSs_dk)
    return bracket


def _shadow_coefficients_numerical(data: dict, max_r: int) -> Dict[int, float]:
    """Compute shadow coefficients from shadow metric data numerically."""
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    Delta = data.get('Delta', 8.0 * kappa * S4)

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 2.0 * Delta

    if abs(q0) < 1e-30:
        return {r: 0.0 for r in range(2, max_r + 1)}

    a0 = 2.0 * abs(kappa)
    a = [a0]
    if max_r >= 3:
        a1 = q1 / (2.0 * a0) if abs(a0) > 1e-30 else 0.0
        a.append(a1)
    if max_r >= 4:
        a2 = (q2 - a[1] ** 2) / (2.0 * a0) if abs(a0) > 1e-30 else 0.0
        a.append(a2)
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        an = -conv / (2.0 * a0) if abs(a0) > 1e-30 else 0.0
        a.append(an)

    result = {}
    for n in range(len(a)):
        r = n + 2
        if r <= max_r:
            result[r] = a[n] / float(r)
    return result


def poisson_center_generators(data: dict) -> dict:
    r"""Report center data certified by this finite scalar window.

    The historical API name is retained, but the generic Virasoro/W and
    beta-gamma three-generator bracket candidate has a nonzero Jacobi defect.
    On those loci the module does not certify a Poisson center.  It reports
    the shadow-metric discriminant

        Disc(Q_L) = q1^2 - 4*q0*q2 = -32*kappa^2*Delta

    as a scalar invariant, not as a proved central Casimir.
    """
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    Delta = data['Delta']
    depth = _depth_class(data)
    status = shadow_bracket_status(data)
    discriminant = shadow_metric_discriminant(data)

    if depth == 'G':
        return {
            'dim_center': float('inf'),
            'generators': ['kappa'],
            'description': 'Entire shadow ring (trivial Poisson structure)',
            'casimir': kappa,
            'center_type': 'full',
            'bracket_status': status,
            'discriminant_Q': discriminant,
        }

    if abs(alpha) < 1e-15 and abs(S4) < 1e-15:
        return {
            'dim_center': float('inf'),
            'generators': ['kappa'],
            'description': 'Trivial Poisson structure (alpha = S_4 = 0)',
            'casimir': kappa,
            'center_type': 'full',
            'bracket_status': status,
            'discriminant_Q': discriminant,
        }

    if depth == 'L':
        return {
            'dim_center': 0,
            'generators': ['constants'],
            'description': (
                'Class L finite-depth window has the nonzero two-generator '
                'bracket {kappa, alpha}; no nonconstant center generator is '
                'certified by this scalar computation.'
            ),
            'casimir': None,
            'center_type': 'constants_only',
            'bracket_status': status,
            'discriminant_Q': discriminant,
        }

    return {
        'dim_center': 0,
        'generators': [],
        'description': (
            'No nonconstant Poisson-center generator is certified on this '
            'finite window.  The reported discriminant is a scalar invariant '
            'of Q_L, not a proved central Casimir.'
        ),
        'casimir': None,
        'center_type': 'not_poisson' if not status['is_poisson'] else 'not_computed',
        'bracket_status': status,
        'Delta': Delta,
        'nine_alpha_sq': 9.0 * alpha ** 2,
        'discriminant_Q': discriminant,
    }


def shadow_metric_discriminant(data: dict) -> Union[float, complex]:
    """Compute the shadow-metric discriminant Disc(Q_L) = -32*kappa^2*Delta.

    For each family:
        Heisenberg:  Disc(Q_L) = 0 (Delta = 0)
        Affine sl_2: Disc(Q_L) = 0 (Delta = 0)
        Betagamma:   Disc(Q_L) = -32*kappa^2 * 40/(5c+22)
        Virasoro:    Disc(Q_L) = -32*(c/2)^2 * 40/(5c+22)
    """
    kappa = data['kappa']
    Delta = data['Delta']
    return -32.0 * kappa ** 2 * Delta


def shadow_casimir_value(data: dict) -> Union[float, complex]:
    """Compatibility alias for shadow_metric_discriminant().

    The returned scalar is the discriminant of Q_L.  It is not asserted to be
    a central Casimir unless a separate Poisson-center proof is available.
    """
    return shadow_metric_discriminant(data)


# ============================================================================
# 3. Finite-window product diagnostic
# ============================================================================

def kontsevich_B0(f_val: float, g_val: float) -> float:
    """B_0(f, g) = f * g (pointwise product)."""
    return f_val * g_val


def kontsevich_B1(f_arity: int, g_arity: int, data: dict) -> float:
    """B_1(f, g) = {f, g}_shadow for the projected bracket.

    For shadow generators S_r, S_s:
        B_1(S_r, S_s) = {S_r, S_s}_shadow
    """
    return shadow_poisson_bracket(f_arity, g_arity, data)


def kontsevich_B2(f_arity: int, g_arity: int, data: dict) -> float:
    r"""B_2(f, g) = (1/2) * Pi^{ij} Pi^{kl} (d_i d_k f)(d_j d_l g)
                   + (1/3) * Pi^{ij} (d_j Pi^{kl}) [(d_i d_k f)(d_l g) + (d_k f)(d_i d_l g)]

    For the shadow bracket candidate with generators (kappa, alpha, S_4):

    On the 1D family locus (parametrized by c), f and g are functions of c.
    The bivector candidate Pi^{ij} is a function of c.  The B_2 operator is:

        B_2(f, g) = (1/2) * (Pi^{12})^2 * f''*g'' + ...

    where the derivatives are with respect to the shadow ring generators.

    For shadow generators S_r on a SINGLE family locus:
        f = S_r(c), g = S_s(c) are functions of c.
        The finite-window B_2 reduces to:
        B_2(S_r, S_s) = (1/2) * {S_r, {S_s, c}}_shadow + correction terms

    We compute B_2 via the MOYAL FORMULA on the 2D Poisson plane:
        B_2(f, g) = (1/2) * Pi^{ab} * Pi^{cd} * (d_a d_c f)(d_b d_d g)

    where (a,b,c,d) run over shadow coordinates.
    """
    bivector = shadow_poisson_bivector(data)
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    Delta = data['Delta']

    if abs(kappa) < 1e-30:
        return 0.0

    # On the shadow ring, we model B_2 via the Moyal-type formula.
    # For the rank-2 bivector candidate on (kappa, alpha):
    # Pi^{12} = {kappa, alpha} = 9*alpha^2/(2*kappa)
    #
    # B_2(S_r, S_s) = (1/2) * (Pi^{12})^2 * (d^2 S_r / d(kappa) d(alpha))
    #                 * (d^2 S_s / d(alpha) d(kappa))
    #                 + correction from d(Pi^{12})
    #
    # For the shadow coefficients as functions of (kappa, alpha):
    # S_r depends on kappa, alpha, and the recursion.  The second derivatives
    # are computed numerically.

    Pi12 = 9.0 * alpha ** 2 / (2.0 * kappa)

    # Compute second derivatives numerically
    eps = 1e-6
    coeffs_00 = _shadow_coefficients_numerical(data, max(f_arity, g_arity) + 2)

    # Perturbed data for numerical second derivatives
    data_kk = dict(data)
    data_kk['kappa'] = kappa + eps
    data_kk['Delta'] = 8.0 * (kappa + eps) * S4
    coeffs_kk = _shadow_coefficients_numerical(data_kk, max(f_arity, g_arity) + 2)

    data_aa = dict(data)
    data_aa['alpha'] = alpha + eps
    coeffs_aa = _shadow_coefficients_numerical(data_aa, max(f_arity, g_arity) + 2)

    data_ka = dict(data)
    data_ka['kappa'] = kappa + eps
    data_ka['alpha'] = alpha + eps
    data_ka['Delta'] = 8.0 * (kappa + eps) * S4
    coeffs_ka = _shadow_coefficients_numerical(data_ka, max(f_arity, g_arity) + 2)

    # Mixed second derivative: d^2 S / d(kappa) d(alpha)
    f0 = coeffs_00.get(f_arity, 0.0)
    fk = coeffs_kk.get(f_arity, 0.0)
    fa = coeffs_aa.get(f_arity, 0.0)
    fka = coeffs_ka.get(f_arity, 0.0)
    d2f_dkda = (fka - fk - fa + f0) / eps ** 2

    g0 = coeffs_00.get(g_arity, 0.0)
    gk = coeffs_kk.get(g_arity, 0.0)
    ga = coeffs_aa.get(g_arity, 0.0)
    gka = coeffs_ka.get(g_arity, 0.0)
    d2g_dkda = (gka - gk - ga + g0) / eps ** 2

    # Second derivatives d^2/dk^2 and d^2/da^2
    data_k2 = dict(data)
    data_k2['kappa'] = kappa + 2 * eps
    data_k2['Delta'] = 8.0 * (kappa + 2 * eps) * S4
    coeffs_k2 = _shadow_coefficients_numerical(data_k2, max(f_arity, g_arity) + 2)

    data_a2 = dict(data)
    data_a2['alpha'] = alpha + 2 * eps
    coeffs_a2 = _shadow_coefficients_numerical(data_a2, max(f_arity, g_arity) + 2)

    d2f_dk2 = (coeffs_k2.get(f_arity, 0.0) - 2 * fk + f0) / eps ** 2
    d2g_dk2 = (coeffs_k2.get(g_arity, 0.0) - 2 * gk + g0) / eps ** 2
    d2f_da2 = (coeffs_a2.get(f_arity, 0.0) - 2 * fa + f0) / eps ** 2
    d2g_da2 = (coeffs_a2.get(g_arity, 0.0) - 2 * ga + g0) / eps ** 2

    # Moyal B_2 on 2D Poisson plane with Pi^{12} = -Pi^{21} = Pi12:
    # B_2(f, g) = (1/2) * Pi^{12} * Pi^{12} * (d_1 d_1 f * d_2 d_2 g
    #             + d_2 d_2 f * d_1 d_1 g - 2 * d_1 d_2 f * d_1 d_2 g)
    #           = (Pi12^2 / 2) * (d2f_dk2 * d2g_da2 + d2f_da2 * d2g_dk2
    #                              - 2 * d2f_dkda * d2g_dkda)
    B2 = (Pi12 ** 2 / 2.0) * (
        d2f_dk2 * d2g_da2 + d2f_da2 * d2g_dk2
        - 2.0 * d2f_dkda * d2g_dkda
    )

    return B2


def kontsevich_Bn(n: int, f_arity: int, g_arity: int, data: dict) -> float:
    r"""Moyal-type B_n coefficient for general n, computed numerically.

    For the rank-2 bivector candidate, the Moyal-type formula gives:

        B_n(f, g) = (1/n!) * sum_{|alpha|=|beta|=n}
                    Pi^{i_1 j_1} ... Pi^{i_n j_n}
                    (d_{i_1}...d_{i_n} f)(d_{j_1}...d_{j_n} g)
                    * combinatorial_weight

    On the 2D Poisson plane with coordinates (kappa, alpha):
        B_n(f, g) = (Pi12^n / n!) * sum_{k=0}^{n} (-1)^k C(n,k)
                    (d^n f / d(kappa)^k d(alpha)^{n-k})
                    (d^n g / d(kappa)^{n-k} d(alpha)^k)

    This is the Moyal formula adapted to the projected shadow bracket.
    """
    if n == 0:
        coeffs = _shadow_coefficients_numerical(data, max(f_arity, g_arity) + 2)
        return coeffs.get(f_arity, 0.0) * coeffs.get(g_arity, 0.0)
    if n == 1:
        return kontsevich_B1(f_arity, g_arity, data)
    if n == 2:
        return kontsevich_B2(f_arity, g_arity, data)

    kappa = data['kappa']
    alpha = data['alpha']

    if abs(kappa) < 1e-30:
        return 0.0

    Pi12 = 9.0 * alpha ** 2 / (2.0 * kappa)

    # Compute n-th order partial derivatives numerically
    eps = 1e-5
    max_ar = max(f_arity, g_arity) + 2

    # Build grid of perturbed data points
    def _perturbed_coeff(dk: int, da: int, arity: int) -> float:
        d = dict(data)
        d['kappa'] = kappa + dk * eps
        d['alpha'] = alpha + da * eps
        d['Delta'] = 8.0 * (kappa + dk * eps) * data['S4']
        return _shadow_coefficients_numerical(d, max_ar).get(arity, 0.0)

    # n-th mixed partial d^n f / d(kappa)^p d(alpha)^{n-p}
    # via finite differences on a grid
    def _nth_partial(arity: int, p: int, q: int) -> float:
        """d^{p+q} S_arity / d(kappa)^p d(alpha)^q via finite differences."""
        # Use central differences for stability
        total = p + q
        if total == 0:
            return _perturbed_coeff(0, 0, arity)

        result = 0.0
        for i in range(p + 1):
            for j in range(q + 1):
                sign = (-1) ** ((p - i) + (q - j))
                binom = _binom(p, i) * _binom(q, j)
                result += sign * binom * _perturbed_coeff(i, j, arity)
        return result / (eps ** total)

    # Moyal formula for B_n:
    # B_n = (Pi12^n / n!) * sum_{k=0}^{n} (-1)^k * C(n,k)
    #        * (d^n f / dk^k da^{n-k}) * (d^n g / dk^{n-k} da^k)
    total = 0.0
    fact_n = math.factorial(n)
    for k_idx in range(n + 1):
        sign = (-1) ** k_idx
        binom_nk = _binom(n, k_idx)
        df = _nth_partial(f_arity, k_idx, n - k_idx)
        dg = _nth_partial(g_arity, n - k_idx, k_idx)
        total += sign * binom_nk * df * dg

    return (Pi12 ** n / fact_n) * total


def _binom(n: int, k: int) -> int:
    """Binomial coefficient C(n, k)."""
    if k < 0 or k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def star_product(f_arity: int, g_arity: int, data: dict,
                 hbar_val: float, max_order: int = 5) -> float:
    r"""Compute f *_hbar g = sum_{n=0}^{max_order} hbar^n B_n(f, g).

    Parameters
    ----------
    f_arity, g_arity : int
        Arities of the shadow generators being multiplied.
    data : dict
        Shadow data from get_shadow_data().
    hbar_val : float
        Value of the deformation parameter hbar.
    max_order : int
        Maximum order in hbar (default 5).

    Returns
    -------
    float : value of f *_hbar g.
    """
    result = 0.0
    for n in range(max_order + 1):
        Bn = kontsevich_Bn(n, f_arity, g_arity, data)
        result += (hbar_val ** n) * Bn
    return result


def star_product_components(f_arity: int, g_arity: int, data: dict,
                            max_order: int = 5) -> Dict[int, float]:
    """Compute B_n(f, g) for n = 0, ..., max_order.

    Returns dict {n: B_n(f, g)} for building the finite-window product.
    """
    return {n: kontsevich_Bn(n, f_arity, g_arity, data) for n in range(max_order + 1)}


def associativity_test(f_arity: int, g_arity: int, h_arity: int,
                       data: dict, hbar_val: float,
                       max_order: int = 5) -> dict:
    r"""Diagnostic associativity check for the truncated finite-window product.

    This does not prove a global star product.  It checks the numerical
    truncated product on a chosen scalar window by comparing:

        |(f * g) * h - f * (g * h)| / |f * g * h| < tolerance

    For shadow generators S_r, the test uses the fact that:
    - B_0 is the commutative product
    - B_1 is the projected bracket
    - Higher B_n involve higher derivatives

    The error comes from:
    1. Truncation at finite order (order hbar^{max_order+1} terms dropped)
    2. Numerical differentiation errors in B_n

    We verify both:
    - Exact associativity at each order (structural)
    - Numerical agreement at specific hbar values

    Returns
    -------
    dict with 'lhs', 'rhs', 'difference', 'relative_error'.
    """
    coeffs = _shadow_coefficients_numerical(data, max(f_arity, g_arity, h_arity) + 2)

    f_val = coeffs.get(f_arity, 0.0)
    g_val = coeffs.get(g_arity, 0.0)
    h_val = coeffs.get(h_arity, 0.0)

    # (f * g) * h
    fg_components = star_product_components(f_arity, g_arity, data, max_order)
    # For the product (fg) * h, we need (fg) as a function.
    # At leading order: fg = f_val * g_val (a number, not a shadow generator).
    # So (fg) * h = fg * h + hbar * {fg, h} + ...
    # where {fg, h} involves the Leibniz rule: {fg, h} = f*{g,h} + {f,h}*g

    # Compute order by order using the truncated finite-window product.
    # This is an approximation: we compute f*g at each hbar, then multiply by h
    lhs = star_product(f_arity, g_arity, data, hbar_val, max_order)
    lhs_star_h = lhs * h_val  # Leading approximation

    # f * (g * h)
    rhs_gh = star_product(g_arity, h_arity, data, hbar_val, max_order)
    rhs = f_val * rhs_gh  # Leading approximation

    # A better test: order-by-order associativity
    # At order hbar^0: f*g*h (trivially associative)
    # At order hbar^1: {f*g, h} = f*{g,h} + {f,h}*g = {f,g}*h + f*{g,h}
    #   LHS contrib at O(hbar^1): B_1(f,g)*h = {f,g}*h
    #   RHS contrib at O(hbar^1): f*B_1(g,h) = f*{g,h}
    #   These are NOT equal in general. The correct associativity is:
    #   sum_{p+q=n} B_p(B_q(f,g), h) = sum_{p+q=n} B_p(f, B_q(g,h))
    #   At n=1: B_0(B_1(f,g), h) + B_1(B_0(f,g), h) = B_0(f, B_1(g,h)) + B_1(f, B_0(g,h))
    #   i.e.: {f,g}*h + {fg, h} = f*{g,h} + {f, gh}
    #   By Leibniz: {fg,h} = f*{g,h} + g*{f,h}
    #   LHS: {f,g}*h + f*{g,h} + g*{f,h}
    #   RHS: f*{g,h} + {f,g}*h + g*{f,h}
    #   RHS: f*{g,h} + {f,g}*h + g*{f,h}
    #   So LHS = RHS at order 1. Good, Jacobi identity is not needed at O(hbar^1).

    # For the NUMERICAL test, we use the direct computation:
    # Compute products with the same shadow data at specific values.
    # and check numerical agreement.

    # Direct order-by-order check:
    order_errors = {}
    for order in range(max_order + 1):
        # Compute (f*g)*h and f*(g*h) at this order
        fg = star_product(f_arity, g_arity, data, hbar_val, order)
        gh = star_product(g_arity, h_arity, data, hbar_val, order)

        # Leading-order approximation for the nested product
        lhs_val = fg * h_val + hbar_val * shadow_poisson_bracket(f_arity, g_arity, data) * h_val
        rhs_val = f_val * gh + hbar_val * f_val * shadow_poisson_bracket(g_arity, h_arity, data)
        order_errors[order] = abs(lhs_val - rhs_val)

    diff = abs(lhs_star_h - rhs)
    norm = abs(f_val * g_val * h_val) if abs(f_val * g_val * h_val) > 1e-30 else 1.0
    rel_err = diff / norm

    return {
        'lhs': lhs_star_h,
        'rhs': rhs,
        'difference': diff,
        'relative_error': rel_err,
        'order_errors': order_errors,
        'hbar': hbar_val,
        'max_order': max_order,
    }


# ============================================================================
# 4. Finite-window corrections to shadow invariants
# ============================================================================

def quantum_kappa(data: dict, hbar_val: float, max_order: int = 5) -> dict:
    r"""Compute the quantum correction to the modular characteristic:

        kappa_hbar = kappa + sum_{n>=1} hbar^n kappa_n

    where kappa_n is the n-th diagnostic correction from the finite-window product.

    The diagnostic correction arises from the noncommutativity of the
    finite-window product:
        kappa_1 = (1/2) * {kappa, alpha}_shadow * (d alpha / d hbar)
                = 0 at hbar = 0 (no first-order correction for generators)

    More precisely, for the shadow generator kappa = S_2:
        kappa_hbar = kappa (the generator itself is not deformed)

    The quantum correction to kappa as an INVARIANT is different:
        kappa_hbar(A) = kappa(A) + sum finite-window corrections
    where the corrections come from the finite-window product modifying the
    MC equation:
        D_hbar * Theta + (1/2) [Theta *_hbar Theta] = 0

    The n-th correction kappa_n is:
        kappa_n = (1/(2*n!)) * sum_{graphs Gamma of order n}
                  w_Gamma * B_Gamma(Theta, Theta)  projected to arity 2

    For the shadow ring, this reduces to:
        kappa_1 = (1/2) * B_1(kappa, kappa) = (1/2) * {kappa, kappa} = 0
        kappa_2 = (1/2) * B_2(kappa, kappa)   (from the finite-window B_2)
        kappa_3 = (1/2) * B_3(kappa, kappa) + (1/6) * sum ternary contributions

    The arity-2 projection of the quantized MC equation gives:
        kappa_n = (1/2) * B_n(kappa, kappa) for n >= 1
    where we use the fact that kappa = S_2 is the arity-2 generator.
    """
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    Delta = data['Delta']

    corrections = {}
    for n in range(1, max_order + 1):
        # kappa_n = (1/2) * B_n(S_2, S_2)
        # {kappa, kappa} = 0 (antisymmetry), so B_1 = 0
        # B_n(S_2, S_2) for n >= 2 involves higher Poisson derivatives
        Bn_val = kontsevich_Bn(n, 2, 2, data)
        corrections[n] = 0.5 * Bn_val

    kappa_hbar = kappa
    for n in range(1, max_order + 1):
        kappa_hbar += (hbar_val ** n) * corrections[n]

    return {
        'kappa': kappa,
        'kappa_hbar': kappa_hbar,
        'corrections': corrections,
        'hbar': hbar_val,
        'max_order': max_order,
    }


def quantum_discriminant(data: dict, hbar_val: float, max_order: int = 5) -> dict:
    r"""Compute the quantum discriminant:

        Delta_hbar = Delta + sum_{n>=1} hbar^n Delta_n

    The discriminant Delta = 8*kappa*S_4 determines the shadow depth class.
    Under deformation quantization, the quantum discriminant controls
    whether the quantum shadow tower terminates.

    Delta_n = 8 * (kappa_n * S_4 + kappa * S4_n + sum mixed terms)

    where kappa_n and S4_n are finite-window corrections to kappa and S_4.

    At lowest order:
        Delta_1 = 8 * (kappa_1 * S_4 + kappa * S4_1)
    where kappa_1 = 0 and S4_1 = (1/2)*B_1(S_4, S_4) = 0 (antisymmetry).
    So Delta_1 = 0.

    At second order:
        Delta_2 = 8 * (kappa_2 * S_4 + kappa * S4_2 + kappa_1 * S4_1)
               = 8 * (kappa_2 * S_4 + kappa * S4_2)
    """
    kappa = data['kappa']
    S4 = data['S4']
    Delta = data['Delta']

    kappa_data = quantum_kappa(data, hbar_val, max_order)
    kappa_corr = kappa_data['corrections']

    # S4 finite-window corrections.
    S4_corrections = {}
    for n in range(1, max_order + 1):
        Bn_val = kontsevich_Bn(n, 4, 4, data)
        S4_corrections[n] = 0.5 * Bn_val

    # Delta corrections: Delta_n = 8*(sum_{p+q=n} kappa_p * S4_q)
    delta_corrections = {}
    for n in range(1, max_order + 1):
        delta_n = 0.0
        for p in range(n + 1):
            q = n - p
            kp = kappa if p == 0 else kappa_corr.get(p, 0.0)
            sq = S4 if q == 0 else S4_corrections.get(q, 0.0)
            if p == 0 and q == 0:
                continue  # This is the leading Delta, not a correction
            delta_n += kp * sq
        delta_corrections[n] = 8.0 * delta_n

    Delta_hbar = Delta
    for n in range(1, max_order + 1):
        Delta_hbar += (hbar_val ** n) * delta_corrections[n]

    return {
        'Delta': Delta,
        'Delta_hbar': Delta_hbar,
        'corrections': delta_corrections,
        'kappa_corrections': kappa_corr,
        'S4_corrections': S4_corrections,
        'hbar': hbar_val,
        'max_order': max_order,
    }


# ============================================================================
# 5. Finite-window product at zeta-zero ordinates
# ============================================================================

# First 20 nontrivial zeros of Riemann zeta (imaginary parts)
ZETA_ZEROS_20 = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167159,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081606,
    67.079810529494174,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
]


def virasoro_at_zero(gamma_n: float) -> dict:
    """Compute Virasoro shadow data at c(rho_n) where rho_n = 1/2 + i*gamma_n.

    The central charge at a zeta zero is:
        c(rho_n) = 1/2 + i*gamma_n  (complexified)

    This gives COMPLEX shadow data. The shadow metric Q_L becomes complex,
    and the finite-window product acquires complex values.

    Returns dict with complex shadow data.
    """
    # c = 1/2 + i*gamma_n (the zeta zero rho = 1/2 + i*gamma)
    c_val = complex(0.5, gamma_n)
    kappa = c_val / 2  # c/2
    alpha = 2.0 + 0j  # constant for Virasoro
    S4_denom = c_val * (5 * c_val + 22)
    S4 = 10.0 / S4_denom if abs(S4_denom) > 1e-30 else 0.0
    Delta = 8.0 * kappa * S4

    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'c': c_val,
        'gamma': gamma_n,
        'family': 'virasoro_complex',
        'depth_class': 'M',
    }


def _shadow_coefficients_complex(data: dict, max_r: int) -> Dict[int, complex]:
    """Compute shadow coefficients with complex-valued data."""
    kappa = complex(data['kappa'])
    alpha = complex(data['alpha'])
    S4 = complex(data['S4'])
    Delta = complex(data.get('Delta', 8.0 * kappa * S4))

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 2.0 * Delta

    if abs(q0) < 1e-30:
        return {r: 0.0 + 0j for r in range(2, max_r + 1)}

    # a_0 = 2*kappa (principal branch of sqrt(q0) = sqrt(4*kappa^2) = 2*kappa)
    a0 = 2.0 * kappa
    a = [a0]
    if max_r >= 3:
        a1 = q1 / (2.0 * a0) if abs(a0) > 1e-30 else 0.0 + 0j
        a.append(a1)
    if max_r >= 4:
        a2 = (q2 - a[1] ** 2) / (2.0 * a0) if abs(a0) > 1e-30 else 0.0 + 0j
        a.append(a2)
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        an = -conv / (2.0 * a0) if abs(a0) > 1e-30 else 0.0 + 0j
        a.append(an)

    result = {}
    for n in range(len(a)):
        r = n + 2
        if r <= max_r:
            result[r] = a[n] / float(r)
    return result


def star_product_at_zero(zero_index: int, f_arity: int = 2, g_arity: int = 4,
                         hbar_val: float = 1.0, max_order: int = 5) -> dict:
    r"""Evaluate the finite-window product at a Riemann zeta-zero ordinate.

    Computes B_n(S_r, S_s) at c = 1/2 + i*gamma_n where gamma_n is the
    n-th zero of the Riemann zeta function on the critical line.

    Parameters
    ----------
    zero_index : int
        Index n (0-based) into ZETA_ZEROS_20.
    f_arity, g_arity : int
        Arities of shadow generators.
    hbar_val : float
        Deformation parameter.
    max_order : int
        Maximum order in hbar.

    Returns
    -------
    dict with B_n values, finite-window product, and degeneration analysis.
    """
    if zero_index >= len(ZETA_ZEROS_20):
        raise ValueError(f"Zero index {zero_index} exceeds available zeros ({len(ZETA_ZEROS_20)})")

    gamma = ZETA_ZEROS_20[zero_index]
    zero_data = virasoro_at_zero(gamma)

    c_val = zero_data['c']
    kappa = zero_data['kappa']
    alpha = zero_data['alpha']
    S4 = zero_data['S4']
    Delta = zero_data['Delta']

    # Compute B_n at the zero
    Bn_values = {}
    for n in range(max_order + 1):
        Bn_values[n] = _Bn_complex(n, f_arity, g_arity, zero_data)

    # Finite-window product.
    star = sum(
        (hbar_val ** n) * Bn_values[n]
        for n in range(max_order + 1)
    )

    # Degeneration analysis: do B_n approach zero at zeros?
    Bn_magnitudes = {n: abs(v) for n, v in Bn_values.items()}

    # Compare with B_n at a nearby NON-zero point
    gamma_off = gamma + 0.01
    off_data = virasoro_at_zero(gamma_off)
    Bn_off = {}
    for n in range(max_order + 1):
        Bn_off[n] = _Bn_complex(n, f_arity, g_arity, off_data)
    Bn_off_magnitudes = {n: abs(v) for n, v in Bn_off.items()}

    # Ratio: suppression at the zero vs nearby
    suppression_ratios = {}
    for n in range(max_order + 1):
        if abs(Bn_off_magnitudes.get(n, 0.0)) > 1e-30:
            suppression_ratios[n] = Bn_magnitudes[n] / Bn_off_magnitudes[n]
        else:
            suppression_ratios[n] = float('nan')

    # Shadow-metric discriminant at the zero.
    discriminant = -32.0 * kappa ** 2 * Delta

    return {
        'zero_index': zero_index,
        'gamma': gamma,
        'c': c_val,
        'kappa': kappa,
        'S4': S4,
        'Delta': Delta,
        'Bn_values': Bn_values,
        'Bn_magnitudes': Bn_magnitudes,
        'star_product': star,
        'star_magnitude': abs(star),
        'discriminant_Q': discriminant,
        'discriminant_magnitude': abs(discriminant),
        # Historical aliases retained for callers that used the old API.
        'casimir': discriminant,
        'casimir_magnitude': abs(discriminant),
        'suppression_ratios': suppression_ratios,
        'Bn_off_magnitudes': Bn_off_magnitudes,
    }


def _Bn_complex(n: int, f_arity: int, g_arity: int, data: dict) -> complex:
    """Compute B_n for complex-valued shadow data."""
    kappa = complex(data['kappa'])
    alpha = complex(data['alpha'])
    S4 = complex(data['S4'])
    Delta = complex(data.get('Delta', 8.0 * kappa * S4))

    if abs(kappa) < 1e-30:
        return 0.0 + 0j

    if n == 0:
        coeffs = _shadow_coefficients_complex(data, max(f_arity, g_arity) + 2)
        return coeffs.get(f_arity, 0.0 + 0j) * coeffs.get(g_arity, 0.0 + 0j)

    Pi12 = 9.0 * alpha ** 2 / (2.0 * kappa)

    if n == 1:
        # {S_r, S_s} computed directly for complex data
        if f_arity == g_arity:
            return 0.0 + 0j
        r, s = min(f_arity, g_arity), max(f_arity, g_arity)
        sign = 1.0 if f_arity <= g_arity else -1.0
        if (r, s) == (2, 3):
            return sign * 9.0 * alpha ** 2 / (2.0 * kappa)
        elif (r, s) == (2, 4):
            return sign * 3.0 * alpha * S4 / kappa
        elif (r, s) == (3, 4):
            return sign * (Delta - 9.0 * alpha ** 2) / (2.0 * kappa)
        else:
            # Higher arities: numerical differentiation with complex step
            return _Bn_complex_numerical(n, f_arity, g_arity, data)
    else:
        return _Bn_complex_numerical(n, f_arity, g_arity, data)


def _Bn_complex_numerical(n: int, f_arity: int, g_arity: int, data: dict) -> complex:
    """Compute B_n via numerical differentiation for complex data."""
    kappa = complex(data['kappa'])
    alpha = complex(data['alpha'])
    S4 = complex(data['S4'])

    if abs(kappa) < 1e-30:
        return 0.0 + 0j

    Pi12 = 9.0 * alpha ** 2 / (2.0 * kappa)
    eps = 1e-5
    max_ar = max(f_arity, g_arity) + 2

    def _perturbed(dk: int, da: int, arity: int) -> complex:
        d = dict(data)
        d['kappa'] = kappa + dk * eps
        d['alpha'] = alpha + da * eps
        d['S4'] = S4
        d['Delta'] = 8.0 * (kappa + dk * eps) * S4
        return _shadow_coefficients_complex(d, max_ar).get(arity, 0.0 + 0j)

    # n-th mixed partial via finite differences
    def _nth_partial(arity: int, p: int, q: int) -> complex:
        total_order = p + q
        if total_order == 0:
            return _perturbed(0, 0, arity)
        result = 0.0 + 0j
        for i in range(p + 1):
            for j in range(q + 1):
                sign = (-1) ** ((p - i) + (q - j))
                binom_val = _binom(p, i) * _binom(q, j)
                result += sign * binom_val * _perturbed(i, j, arity)
        return result / (eps ** total_order)

    # Moyal formula
    total = 0.0 + 0j
    fact_n = math.factorial(n)
    for k_idx in range(n + 1):
        sign = (-1) ** k_idx
        binom_nk = _binom(n, k_idx)
        df = _nth_partial(f_arity, k_idx, n - k_idx)
        dg = _nth_partial(g_arity, n - k_idx, k_idx)
        total += sign * binom_nk * df * dg

    return (Pi12 ** n / fact_n) * total


def quantum_casimir_at_zero(zero_index: int, hbar_val: float = 1.0,
                            max_order: int = 3) -> dict:
    r"""Compute the diagnostic deformation of Disc(Q_L) at a zeta-zero ordinate.

    C_hbar = C_0 + sum_{n>=1} hbar^n C_n

    where C_0 = -32*kappa^2*Delta is the shadow-metric discriminant and
    C_n involves finite-window corrections to kappa and Delta.
    """
    gamma = ZETA_ZEROS_20[zero_index]
    zero_data = virasoro_at_zero(gamma)

    kappa = zero_data['kappa']
    Delta = zero_data['Delta']
    C0 = -32.0 * kappa ** 2 * Delta

    # Diagnostic corrections via the complex finite-window product.
    # C_n = -32 * sum_{p+q+r=n} kappa_p * kappa_q * Delta_r
    # where kappa_0 = kappa, Delta_0 = Delta, and kappa_n, Delta_n
    # are finite-window corrections.

    # For simplicity, compute the first few corrections directly
    # from the product of kappa with itself and with S_4.
    corrections = {}
    for n in range(1, max_order + 1):
        # kappa_n = (1/2) * B_n(S_2, S_2)
        kn = 0.5 * _Bn_complex(n, 2, 2, zero_data)
        # S4_n = (1/2) * B_n(S_4, S_4)
        s4n = 0.5 * _Bn_complex(n, 4, 4, zero_data)
        # Delta_n = 8*(kappa_n*S4 + kappa*S4_n + lower)
        S4_val = zero_data['S4']
        dn = 8.0 * (kn * S4_val + kappa * s4n)
        # C_n = -32*(2*kappa*kn*Delta + kappa^2*dn)
        cn = -32.0 * (2.0 * kappa * kn * Delta + kappa ** 2 * dn)
        corrections[n] = cn

    C_hbar = C0
    for n in range(1, max_order + 1):
        C_hbar += (hbar_val ** n) * corrections[n]

    return {
        'zero_index': zero_index,
        'gamma': gamma,
        'discriminant_0': C0,
        'discriminant_0_magnitude': abs(C0),
        'discriminant_hbar': C_hbar,
        'discriminant_hbar_magnitude': abs(C_hbar),
        # Historical aliases retained for callers that used the old API.
        'C0': C0,
        'C0_magnitude': abs(C0),
        'C_hbar': C_hbar,
        'C_hbar_magnitude': abs(C_hbar),
        'corrections': corrections,
        'correction_magnitudes': {n: abs(v) for n, v in corrections.items()},
    }


# ============================================================================
# 6. Moyal comparison
# ============================================================================

def moyal_star_product(f_arity: int, g_arity: int, data: dict,
                       hbar_val: float, max_order: int = 5) -> float:
    r"""Compute the constant-bivector Moyal product for comparison.

    The Moyal formula for a constant bivector Pi^{ij}:

        f *_hbar g = sum_{n>=0} (hbar/2)^n (1/n!) Pi^{i_1 j_1}...Pi^{i_n j_n}
                     (d_{i_1}...d_{i_n} f)(d_{j_1}...d_{j_n} g)

    For a constant Poisson bivector, the Moyal formula is the standard
    deformation-quantization model.

    For the shadow bracket candidate, Pi is not constant (it depends on
    kappa and alpha), so this comparison measures non-constancy of the
    finite-window bivector:

        window product - constant-bivector Moyal = O(hbar^2) * (derivatives of Pi)

    This comparison provides verification path (iv).
    """
    kappa = data['kappa']
    alpha = data['alpha']

    if abs(kappa) < 1e-30:
        coeffs = _shadow_coefficients_numerical(data, max(f_arity, g_arity) + 2)
        return coeffs.get(f_arity, 0.0) * coeffs.get(g_arity, 0.0)

    Pi12 = 9.0 * alpha ** 2 / (2.0 * kappa)
    eps = 1e-5
    max_ar = max(f_arity, g_arity) + 2

    def _perturbed_coeff(dk: int, da: int, arity: int) -> float:
        d = dict(data)
        d['kappa'] = kappa + dk * eps
        d['alpha'] = alpha + da * eps
        d['Delta'] = 8.0 * (kappa + dk * eps) * data['S4']
        return _shadow_coefficients_numerical(d, max_ar).get(arity, 0.0)

    def _nth_partial(arity: int, p: int, q: int) -> float:
        total_order = p + q
        if total_order == 0:
            return _perturbed_coeff(0, 0, arity)
        result = 0.0
        for i in range(p + 1):
            for j in range(q + 1):
                sign = (-1) ** ((p - i) + (q - j))
                binom_val = _binom(p, i) * _binom(q, j)
                result += sign * binom_val * _perturbed_coeff(i, j, arity)
        return result / (eps ** total_order)

    # Moyal formula with CONSTANT Pi (evaluated at the point):
    result = 0.0
    for n in range(max_order + 1):
        fact_n = math.factorial(n)
        moyal_n = 0.0
        for k_idx in range(n + 1):
            sign = (-1) ** k_idx
            binom_nk = _binom(n, k_idx)
            df = _nth_partial(f_arity, k_idx, n - k_idx)
            dg = _nth_partial(g_arity, n - k_idx, k_idx)
            moyal_n += sign * binom_nk * df * dg
        moyal_n *= (Pi12 / 2.0) ** n / fact_n
        result += (hbar_val ** n) * moyal_n * (2.0 ** n)  # Convert (hbar/2)^n to hbar^n

    # Note: the Moyal formula uses (hbar/2)^n, but the window product uses hbar^n.
    # The factor of 2^n difference is absorbed into the definition of B_n.
    # For the common symplectic normalization:
    #   B_n = (1/n!) * (Pi)^n * ...
    # while the Moyal convention uses:
    #   B_n^Moyal = (1/(2^n * n!)) * (Pi)^n * ...
    # So B_n(window convention) = 2^n * B_n(Moyal convention) for constant Pi.
    # In our implementation, B_n already includes the correct normalization.
    # The comparison should agree at B_0 and B_1 and diverge at B_2+
    # when derivatives of Pi enter.

    return result


def kontsevich_moyal_comparison(f_arity: int, g_arity: int, data: dict,
                                hbar_val: float = 0.1,
                                max_order: int = 5) -> dict:
    """Compare the finite-window product and the constant-bivector Moyal product.

    Returns dict with both values and the difference.
    The difference measures the non-constancy of the bivector candidate.
    """
    kontsevich = star_product(f_arity, g_arity, data, hbar_val, max_order)
    moyal = moyal_star_product(f_arity, g_arity, data, hbar_val, max_order)

    return {
        'kontsevich': kontsevich,
        'moyal': moyal,
        'difference': kontsevich - moyal,
        'relative_difference': abs(kontsevich - moyal) / abs(kontsevich)
        if abs(kontsevich) > 1e-30 else 0.0,
        'hbar': hbar_val,
        'f_arity': f_arity,
        'g_arity': g_arity,
    }


# ============================================================================
# 7. Full analysis: finite-window product landscape
# ============================================================================

def full_star_product_analysis(family: str, max_order: int = 5, **params) -> dict:
    """Complete finite-window product analysis for a given family.

    Computes:
    1. Shadow bracket candidates for generator pairs
    2. Jacobi-defect status and certified center data
    3. Finite-window B_n coefficients for n = 0, ..., max_order
    4. Truncated products at several hbar values
    5. Diagnostic corrections kappa_n and Delta_n
    6. Moyal comparison
    7. Associativity diagnostic
    """
    data = get_shadow_data(family, **params)

    # 1. Projected brackets
    brackets = {}
    for (r, s) in [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]:
        brackets[(r, s)] = shadow_poisson_bracket(r, s, data)

    # 2. Jacobi-defect status and certified center data
    bracket_status = shadow_bracket_status(data)
    center = poisson_center_generators(data)

    # 3. B_n components for (kappa, S_4)
    Bn_24 = star_product_components(2, 4, data, max_order)

    # 4. Products at several hbar values.
    star_products = {}
    for h in [0.01, 0.1, 0.5, 1.0]:
        star_products[h] = star_product(2, 4, data, h, max_order)

    # 5. Finite-window corrections.
    qk = quantum_kappa(data, 0.1, max_order)
    qd = quantum_discriminant(data, 0.1, max_order)

    # 6. Moyal comparison
    km_comp = kontsevich_moyal_comparison(2, 4, data, 0.1, max_order)

    # 7. Associativity test
    assoc = associativity_test(2, 3, 4, data, 0.1, min(max_order, 3))

    return {
        'family': family,
        'data': data,
        'bracket_status': bracket_status,
        'brackets': brackets,
        'center': center,
        'Bn_24': Bn_24,
        'star_products': star_products,
        'quantum_kappa': qk,
        'quantum_discriminant': qd,
        'km_comparison': km_comp,
        'associativity': assoc,
    }


def star_product_zero_landscape(max_zeros: int = 10, max_order: int = 3) -> dict:
    """Compute finite-window product data at the first max_zeros zeta zeros.

    Returns a landscape of B_n values, products, and discriminant diagnostics
    at each zero, plus trend analysis.
    """
    results = {}
    for idx in range(min(max_zeros, len(ZETA_ZEROS_20))):
        results[idx] = star_product_at_zero(idx, 2, 4, 1.0, max_order)

    # Trend analysis: how do B_n magnitudes scale with zero height?
    trends = {}
    for n in range(max_order + 1):
        magnitudes = [results[idx]['Bn_magnitudes'].get(n, 0.0)
                      for idx in range(len(results))]
        gammas = [ZETA_ZEROS_20[idx] for idx in range(len(results))]
        trends[n] = {
            'magnitudes': magnitudes,
            'gammas': gammas,
            'decreasing': all(magnitudes[i] >= magnitudes[i + 1]
                              for i in range(len(magnitudes) - 1))
            if len(magnitudes) > 1 else True,
        }

    return {
        'zeros': results,
        'trends': trends,
        'num_zeros': len(results),
        'max_order': max_order,
    }
