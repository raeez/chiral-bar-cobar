r"""bc_bridgeland_stability_engine.py -- Bridgeland stability conditions
from the shadow zero distribution of modular Koszul algebras.

MATHEMATICAL CONTENT
====================

A Bridgeland stability condition sigma = (Z, P) on a triangulated category D
consists of a central charge Z: K(D) -> C (group homomorphism) and a slicing
P (a collection of full additive subcategories P(phi) for phi in R, satisfying
Harder-Narasimhan and compatibility axioms).  The space Stab(D) of stability
conditions is a complex manifold.

For the shadow programme, we define a SHADOW STABILITY CONDITION on the
K-theory of the bar complex:

=== 1. SHADOW CENTRAL CHARGE ===

    Z_A(gamma_r) = -S_r(A) * exp(i * pi * r / R)

where S_r(A) is the arity-r shadow coefficient, gamma_r is the K-theory
generator at arity r, and R = r_max (shadow depth) is the normalization.
For class M algebras with R = infinity, we use a truncation R_eff.

The central charge encodes:
  - |Z_A(gamma_r)| = |S_r(A)| (the "mass")
  - arg(Z_A(gamma_r)) = pi + pi*r/R (mod 2*pi) (the "phase")

=== 2. PHASE FUNCTION AND SPECTRUM ===

    phi(E) = (1/pi) * arg Z(E) in (0, 1]

For shadow: phi_r = (1/pi) * arg Z_A(gamma_r).
The shadow phase spectrum {phi_r : r = 2, ..., N} encodes the angular
distribution of charges in the stability condition.

=== 3. HARDER-NARASIMHAN FILTRATION ===

For a formal object E = sum_r a_r * gamma_r, the HN filtration under Z_A
is computed by ordering the summands by decreasing phase and grouping
consecutive summands into semistable factors.

=== 4. MASS SPECTRUM AND SHADOW ZEROS ===

The mass M(E) = |Z(E)|.  Massless objects (M = 0) occur exactly when
Z(gamma) = 0, which happens at the ZEROS of the shadow zeta function.
This provides the bridge:

    ZEROS OF zeta_A(s)  <-->  MASSLESS STATES IN BRIDGELAND STABILITY

=== 5. AUTOEQUIVALENCES FROM COMPLEMENTARITY ===

Koszul duality A -> A! induces Phi*Z_A = Z_{A!}, giving:
    Phi* sigma_c = sigma_{26-c}  (Virasoro)
with fixed point at c = 13 (self-dual stability condition).

=== 6. SUPPORT PROPERTY ===

The support property requires |Z(E)| >= C * ||E|| for some norm ||.||
and constant C > 0.  This is the analogue of the BPS bound.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:complementarity (higher_genus_complementarity.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP39): kappa = c/2 for Virasoro only; NOT general.
CAUTION (AP48): kappa depends on the full algebra, not just c.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np

# ---------------------------------------------------------------------------
# Import shadow coefficient providers from existing engines
# ---------------------------------------------------------------------------
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    w3_w_line_shadow_coefficients,
    shadow_zeta_numerical,
)


# ============================================================================
# 1.  Shadow coefficient dispatch
# ============================================================================

def shadow_coefficients(
    family: str,
    param: float,
    max_r: int = 50,
) -> Dict[int, float]:
    """Compute shadow coefficients S_r for a given family and parameter.

    Parameters
    ----------
    family : one of 'heisenberg', 'affine_sl2', 'affine_sl3',
             'betagamma', 'virasoro', 'w3_t', 'w3_w'
    param : family parameter (k for Heis/affine, lambda for betagamma,
            c for Virasoro/W3)
    max_r : maximum arity

    Returns
    -------
    Dict mapping arity r to S_r(A).
    """
    dispatch = {
        'heisenberg': lambda: heisenberg_shadow_coefficients(param, max_r),
        'affine_sl2': lambda: affine_sl2_shadow_coefficients(param, max_r),
        'affine_sl3': lambda: affine_sl3_shadow_coefficients(param, max_r),
        'betagamma': lambda: betagamma_shadow_coefficients(param, max_r),
        'virasoro': lambda: virasoro_shadow_coefficients_numerical(param, max_r),
        'w3_t': lambda: w3_t_line_shadow_coefficients(param, max_r),
        'w3_w': lambda: w3_w_line_shadow_coefficients(param, max_r),
    }
    if family not in dispatch:
        raise ValueError(f"Unknown family: {family}. Choose from {list(dispatch.keys())}")
    return dispatch[family]()


def koszul_dual_shadow_coefficients(
    family: str,
    param: float,
    max_r: int = 50,
) -> Dict[int, float]:
    """Shadow coefficients of the Koszul dual A!.

    Virasoro: Vir_c^! = Vir_{26-c}.
    Heisenberg: H_k^! has kappa = -k at shadow level (AP33: H_k^! != H_{-k}).
    Affine sl_2: V_k^! corresponds to level -k - 2h^v = -k - 4.
    Affine sl_3: V_k^! corresponds to level -k - 2h^v = -k - 6.

    CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
    CAUTION (AP33): H_k^! = Sym^ch(V*) != H_{-k}.
    """
    if family == 'heisenberg':
        result = {2: -float(param)}
        for r in range(3, max_r + 1):
            result[r] = 0.0
        return result
    elif family == 'affine_sl2':
        return affine_sl2_shadow_coefficients(-param - 4.0, max_r)
    elif family == 'affine_sl3':
        return affine_sl3_shadow_coefficients(-param - 6.0, max_r)
    elif family == 'virasoro':
        return virasoro_shadow_coefficients_numerical(26.0 - param, max_r)
    elif family == 'betagamma':
        c_val = 2.0 * (6.0 * param ** 2 - 6.0 * param + 1.0)
        return virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)
    elif family in ('w3_t', 'w3_w'):
        if family == 'w3_t':
            return w3_t_line_shadow_coefficients(26.0 - param, max_r)
        else:
            return w3_w_line_shadow_coefficients(26.0 - param, max_r)
    else:
        raise ValueError(f"Unknown family: {family}")


def shadow_depth(coeffs: Dict[int, float], tol: float = 1e-12) -> Optional[int]:
    """Return the shadow depth r_max, or None for infinite tower.

    r_max = max{r : |S_r| > tol}.  If the tail shows no exact-zero block
    of length >= 5, the tower is classified as infinite (class M).

    For class M algebras (Virasoro, W_N), the shadow coefficients decay
    exponentially as rho^r * r^{-5/2}, so they may fall below tol for
    large r even though the tower is genuinely infinite.  We distinguish
    genuine termination (a consecutive block of EXACT zeros S_r = 0.0)
    from numerical underflow (small but nonzero values).
    """
    max_key = max(coeffs.keys())

    # Count consecutive exact zeros at the tail
    # "Exact zero" means the coefficient was SET to 0.0 by the provider
    # (as opposed to being a tiny nonzero number from the recursion)
    consecutive_zeros_at_tail = 0
    for r in range(max_key, 1, -1):
        if coeffs.get(r, 0.0) == 0.0:
            consecutive_zeros_at_tail += 1
        else:
            break

    # If fewer than 5 consecutive exact zeros at the tail, tower is infinite
    if consecutive_zeros_at_tail < 5:
        return None

    # Find the last nonzero arity
    last_nonzero = 2
    for r in range(2, max_key + 1):
        if abs(coeffs.get(r, 0.0)) > tol:
            last_nonzero = r
    return last_nonzero


# ============================================================================
# 2.  Shadow central charge Z_A
# ============================================================================

def central_charge(
    coeffs: Dict[int, float],
    r: int,
    R_eff: Optional[int] = None,
) -> complex:
    """Evaluate the shadow central charge Z_A(gamma_r).

    Z_A(gamma_r) = -S_r(A) * exp(i * pi * r / R_eff)

    Parameters
    ----------
    coeffs : shadow coefficients {r: S_r}
    r : arity of the K-theory generator
    R_eff : effective normalization depth.  If None, uses max(coeffs.keys()).

    Returns
    -------
    Complex value Z_A(gamma_r).
    """
    if R_eff is None:
        R_eff = max(coeffs.keys())
    S_r = coeffs.get(r, 0.0)
    return -S_r * cmath.exp(1j * math.pi * r / R_eff)


def central_charge_vector(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    R_eff: Optional[int] = None,
) -> Dict[int, complex]:
    """Compute Z_A(gamma_r) for r = r_min, ..., r_max.

    Returns
    -------
    Dict mapping arity r to Z_A(gamma_r).
    """
    if r_max is None:
        r_max = max(coeffs.keys())
    if R_eff is None:
        R_eff = r_max
    return {r: central_charge(coeffs, r, R_eff) for r in range(r_min, r_max + 1)}


def central_charge_linear(
    coeffs: Dict[int, float],
    a: Dict[int, float],
    R_eff: Optional[int] = None,
) -> complex:
    """Evaluate Z_A on a formal K-theory element E = sum_r a_r * gamma_r.

    Z_A(E) = sum_r a_r * Z_A(gamma_r).

    Parameters
    ----------
    coeffs : shadow coefficients
    a : formal K-theory element {r: a_r}
    R_eff : effective normalization depth
    """
    total = 0.0 + 0.0j
    for r, a_r in a.items():
        total += a_r * central_charge(coeffs, r, R_eff)
    return total


# ============================================================================
# 3.  Phase function
# ============================================================================

def phase(z: complex) -> float:
    """Compute the Bridgeland phase phi = (1/pi) * arg(z) in (0, 1].

    Convention: arg(z) in (0, pi] for the upper half-plane,
    extended to (0, 2*pi) and then divided by pi to get (0, 2].
    For stability conditions, we use the standard convention phi in (0, 1].

    If z = 0, returns NaN (undefined phase for massless object).
    """
    if abs(z) < 1e-30:
        return float('nan')
    angle = cmath.phase(z)  # in (-pi, pi]
    # Map to (0, 2*pi]
    if angle <= 0:
        angle += 2 * math.pi
    return angle / math.pi  # in (0, 2]


def phase_spectrum(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    R_eff: Optional[int] = None,
) -> Dict[int, float]:
    """Compute the shadow phase spectrum {phi_r : r = r_min, ..., r_max}.

    Returns
    -------
    Dict mapping arity r to phase phi_r in (0, 2].
    """
    Z_vec = central_charge_vector(coeffs, r_min, r_max, R_eff)
    return {r: phase(z) for r, z in Z_vec.items()}


def phase_gap(
    phases: Dict[int, float],
) -> Tuple[float, float, float]:
    """Find the maximal gap in the phase spectrum.

    Returns (gap_start, gap_end, gap_size) for the largest interval
    in (0, 2] not containing any phase value.  If all phases are NaN
    (massless), returns (0, 2, 2).
    """
    valid = sorted(p for p in phases.values() if not math.isnan(p))
    if len(valid) == 0:
        return (0.0, 2.0, 2.0)
    if len(valid) == 1:
        gap_size = 2.0 - 0.0  # the whole circle minus one point
        return (valid[0], valid[0] + 2.0, 2.0)

    # Gaps between consecutive phases (sorted on the circle [0, 2])
    gaps = []
    for i in range(len(valid) - 1):
        gaps.append((valid[i], valid[i + 1], valid[i + 1] - valid[i]))
    # Wraparound gap
    wrap_gap = (valid[-1], valid[0] + 2.0, (valid[0] + 2.0) - valid[-1])
    gaps.append(wrap_gap)

    best = max(gaps, key=lambda g: g[2])
    return best


def phase_density_test(
    phases: Dict[int, float],
    n_bins: int = 20,
) -> Dict[str, Any]:
    """Test whether phases are approximately uniformly distributed in (0, 2].

    Uses a simple chi-squared-like statistic.

    Returns
    -------
    dict with keys: 'n_phases', 'chi_sq', 'p_uniform_reject',
                    'bin_counts', 'expected_per_bin'.
    """
    valid = [p for p in phases.values() if not math.isnan(p)]
    n = len(valid)
    if n < 5:
        return {
            'n_phases': n,
            'chi_sq': float('nan'),
            'p_uniform_reject': False,
            'bin_counts': [],
            'expected_per_bin': 0.0,
        }

    # Bin phases into [0, 2] with n_bins bins
    bin_width = 2.0 / n_bins
    counts = [0] * n_bins
    for p in valid:
        idx = min(int(p / bin_width), n_bins - 1)
        counts[idx] += 1

    expected = n / n_bins
    chi_sq = sum((c - expected) ** 2 / expected for c in counts)
    # Rough threshold: chi_sq > 2 * n_bins suggests non-uniform
    reject = chi_sq > 2.0 * n_bins

    return {
        'n_phases': n,
        'chi_sq': chi_sq,
        'p_uniform_reject': reject,
        'bin_counts': counts,
        'expected_per_bin': expected,
    }


# ============================================================================
# 4.  Mass spectrum
# ============================================================================

def mass(z: complex) -> float:
    """Mass of an object with central charge z: M = |Z|."""
    return abs(z)


def mass_spectrum(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    R_eff: Optional[int] = None,
) -> Dict[int, float]:
    """Compute the mass spectrum M(gamma_r) = |Z_A(gamma_r)| for each arity.

    Since Z_A(gamma_r) = -S_r * exp(i*pi*r/R), we have |Z_A(gamma_r)| = |S_r|.
    """
    Z_vec = central_charge_vector(coeffs, r_min, r_max, R_eff)
    return {r: mass(z) for r, z in Z_vec.items()}


def massless_arities(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    tol: float = 1e-12,
) -> List[int]:
    """Find arities r where S_r = 0 (massless objects).

    These are the "zeros" of the shadow tower — where M(gamma_r) = 0.
    """
    if r_max is None:
        r_max = max(coeffs.keys())
    return [r for r in range(r_min, r_max + 1)
            if abs(coeffs.get(r, 0.0)) < tol]


def mass_vanishing_central_charges(
    family: str,
    r_target: int,
    c_min: float = 0.5,
    c_max: float = 25.5,
    n_points: int = 1000,
    tol: float = 1e-8,
    max_r: int = 50,
) -> List[float]:
    """Find values of the central charge parameter c where S_r(c) vanishes.

    These are "walls of marginal stability" in the c-parameter space.

    Uses a sign-change scan followed by bisection refinement.

    Parameters
    ----------
    family : algebra family
    r_target : arity at which to look for vanishing
    c_min, c_max : parameter range to scan
    n_points : number of scan points
    tol : tolerance for bisection
    max_r : max arity for coefficient computation

    Returns
    -------
    List of c values where S_{r_target}(c) approximately vanishes.
    """
    c_vals = np.linspace(c_min, c_max, n_points)
    S_vals = []
    for c in c_vals:
        try:
            coeffs = shadow_coefficients(family, float(c), max_r)
            S_vals.append(coeffs.get(r_target, 0.0))
        except (ValueError, ZeroDivisionError):
            S_vals.append(float('nan'))

    zeros = []
    for i in range(len(S_vals) - 1):
        if math.isnan(S_vals[i]) or math.isnan(S_vals[i + 1]):
            continue
        if S_vals[i] * S_vals[i + 1] < 0:
            # Bisect
            lo, hi = float(c_vals[i]), float(c_vals[i + 1])
            for _ in range(60):
                mid = (lo + hi) / 2.0
                try:
                    coeffs = shadow_coefficients(family, mid, max_r)
                    S_mid = coeffs.get(r_target, 0.0)
                except (ValueError, ZeroDivisionError):
                    break
                if S_mid * S_vals[i] < 0:
                    hi = mid
                else:
                    lo = mid
            zeros.append((lo + hi) / 2.0)

    return zeros


# ============================================================================
# 5.  Harder-Narasimhan filtration
# ============================================================================

@dataclass
class HNFactor:
    """A semistable factor in the Harder-Narasimhan filtration."""
    arities: List[int]
    coefficients: Dict[int, float]
    Z_value: complex
    phase_value: float
    mass_value: float


def hn_filtration(
    coeffs: Dict[int, float],
    a: Dict[int, float],
    R_eff: Optional[int] = None,
) -> List[HNFactor]:
    """Compute the Harder-Narasimhan filtration of E = sum_r a_r * gamma_r.

    In the shadow stability picture, the generators gamma_r are "simple"
    objects.  The HN filtration orders them by decreasing phase.

    For a direct sum E = E_1 + ... + E_n, the HN filtration is obtained
    by ordering the summands by decreasing phase of Z_A(E_i).

    Since each gamma_r is already "semistable" (rank 1 in K-theory),
    the HN filtration simply orders the nonzero summands by decreasing phase.

    Parameters
    ----------
    coeffs : shadow coefficients {r: S_r}
    a : formal K-theory element {r: a_r}
    R_eff : effective normalization depth

    Returns
    -------
    List of HNFactor objects ordered by strictly decreasing phase.
    """
    if R_eff is None:
        R_eff = max(coeffs.keys())

    # Compute phase for each nonzero summand
    factors = []
    for r, a_r in sorted(a.items()):
        if abs(a_r) < 1e-30:
            continue
        z = a_r * central_charge(coeffs, r, R_eff)
        phi = phase(z)
        if math.isnan(phi):
            continue
        factors.append(HNFactor(
            arities=[r],
            coefficients={r: a_r},
            Z_value=z,
            phase_value=phi,
            mass_value=abs(z),
        ))

    # Sort by decreasing phase
    factors.sort(key=lambda f: -f.phase_value)

    # Group consecutive factors with equal phase (semistable)
    if len(factors) <= 1:
        return factors

    merged = [factors[0]]
    for f in factors[1:]:
        if abs(f.phase_value - merged[-1].phase_value) < 1e-10:
            # Merge into the previous semistable factor
            merged[-1].arities.extend(f.arities)
            merged[-1].coefficients.update(f.coefficients)
            merged[-1].Z_value += f.Z_value
            merged[-1].mass_value = abs(merged[-1].Z_value)
        else:
            merged.append(f)

    return merged


def hn_filtration_is_valid(factors: List[HNFactor]) -> bool:
    """Check that the HN filtration has strictly decreasing phases."""
    if len(factors) <= 1:
        return True
    for i in range(len(factors) - 1):
        if factors[i].phase_value <= factors[i + 1].phase_value + 1e-12:
            return False
    return True


# ============================================================================
# 6.  Support property
# ============================================================================

def support_constant_direct(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    R_eff: Optional[int] = None,
) -> float:
    """Compute the support property constant C directly.

    C = min_{r : a_r != 0} |Z_A(gamma_r)| / ||gamma_r||

    where ||gamma_r|| = 1 (unit norm on K-theory generators).
    For generators, C = min_r |S_r| over nonzero arities.

    Returns float('inf') if no nonzero coefficients exist.
    """
    if r_max is None:
        r_max = max(coeffs.keys())

    min_mass = float('inf')
    for r in range(r_min, r_max + 1):
        S_r = coeffs.get(r, 0.0)
        if abs(S_r) > 1e-30:
            m = abs(S_r)  # |Z_A(gamma_r)| = |S_r|
            if m < min_mass:
                min_mass = m
    return min_mass


def support_constant_optimization(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    R_eff: Optional[int] = None,
    n_trials: int = 200,
) -> float:
    """Compute the support property constant C via random sampling.

    C = inf_{E != 0} |Z_A(E)| / ||E||

    where the infimum is over all nonzero formal K-theory elements.
    We sample random elements E = sum_r a_r gamma_r and compute the ratio.

    For a linear central charge, this is equivalent to finding the minimum
    of |Z_A(gamma_r)| / ||gamma_r|| over generators (by triangle inequality
    argument), so this should agree with support_constant_direct.

    However, for verification we check that the sampled infimum approaches
    the direct value.

    Returns
    -------
    Estimated support constant C.
    """
    if r_max is None:
        r_max = max(coeffs.keys())
    if R_eff is None:
        R_eff = r_max

    rng = np.random.RandomState(42)
    min_ratio = float('inf')

    for _ in range(n_trials):
        # Random element with 1-3 nonzero arities
        n_arities = rng.randint(1, min(4, r_max - r_min + 2))
        chosen = rng.choice(range(r_min, r_max + 1), size=n_arities, replace=False)
        a = {}
        for r_val in chosen:
            a[int(r_val)] = rng.randn()

        Z_E = central_charge_linear(coeffs, a, R_eff)
        norm_E = math.sqrt(sum(v ** 2 for v in a.values()))

        if norm_E < 1e-30:
            continue

        ratio = abs(Z_E) / norm_E
        if ratio < min_ratio:
            min_ratio = ratio

    return min_ratio


def support_property_holds(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    R_eff: Optional[int] = None,
) -> Tuple[bool, float]:
    """Check whether the support property holds.

    The support property requires C > 0, i.e., the central charge does
    not vanish on any nonzero K-theory element.

    For generators: this requires S_r != 0 for all r in [r_min, r_max].
    For general elements: the central charge is linear, so the support
    property on generators implies it on all elements when the phases
    are pairwise distinct (no cancellation possible).

    Returns (holds, C) where holds is True if C > 0, and C is the constant.
    """
    if r_max is None:
        r_max = max(coeffs.keys())

    C = support_constant_direct(coeffs, r_min, r_max, R_eff)
    holds = C > 1e-30 and not math.isinf(C)
    return holds, C


# ============================================================================
# 7.  Stability manifold dimension
# ============================================================================

def effective_stability_dimension(
    coeffs: Dict[int, float],
    r_min: int = 2,
    r_max: Optional[int] = None,
    tol: float = 1e-12,
) -> int:
    """Compute the effective dimension of the stability manifold.

    dim Stab = rank K_0 = number of nonzero generators.
    For truncation at arity <= r_max: dim = number of r in [r_min, r_max]
    with S_r != 0.

    Class G (Heisenberg): dim = 1 (single arity).
    Class L (affine KM):  dim = 2 (arities 2, 3).
    Class C (beta-gamma): dim = 3 (arities 2, 3, 4).
    Class M (Virasoro):   dim = r_max - r_min + 1 (all arities nonzero).
    """
    if r_max is None:
        r_max = max(coeffs.keys())
    return sum(1 for r in range(r_min, r_max + 1)
               if abs(coeffs.get(r, 0.0)) > tol)


# ============================================================================
# 8.  Deformation of stability across central charge
# ============================================================================

def stability_deformation_trajectory(
    family: str,
    r_target: int,
    param_min: float,
    param_max: float,
    n_points: int = 200,
    max_r: int = 50,
) -> List[Tuple[float, complex]]:
    """Trace Z_A(gamma_r) in C as the central charge parameter varies.

    Returns a list of (param_value, Z_value) pairs.
    """
    trajectory = []
    for param in np.linspace(param_min, param_max, n_points):
        try:
            coeffs = shadow_coefficients(family, float(param), max_r)
            z = central_charge(coeffs, r_target)
            trajectory.append((float(param), z))
        except (ValueError, ZeroDivisionError):
            continue
    return trajectory


def koszul_duality_monodromy(
    family: str,
    r_target: int,
    c_center: float,
    c_radius: float,
    n_points: int = 200,
    max_r: int = 50,
) -> Dict[str, Any]:
    """Compute the monodromy of sigma_c around the self-dual point.

    For Virasoro: c -> 26-c is the duality involution, with fixed point c=13.
    Going around c=13 via c = 13 + epsilon * exp(i*theta) for theta in [0, 2*pi]
    is a real-parameter path.  We compute how Z_{Vir_c}(gamma_r) transforms.

    In the real parameter space, the "loop" is the path from c_center - c_radius
    to c_center + c_radius and back (since c is real).  The monodromy is
    measured by comparing Z_A(gamma_r) at c and Z_{A!}(gamma_r) at 26-c.

    Returns dict with trajectory data and monodromy information.
    """
    # Forward path: c from c_center - c_radius to c_center + c_radius
    forward = []
    reverse = []  # Koszul dual path
    c_vals = np.linspace(c_center - c_radius, c_center + c_radius, n_points)

    for c in c_vals:
        try:
            coeffs = shadow_coefficients(family, float(c), max_r)
            coeffs_dual = koszul_dual_shadow_coefficients(family, float(c), max_r)
            z = central_charge(coeffs, r_target)
            z_dual = central_charge(coeffs_dual, r_target)
            forward.append((float(c), z))
            reverse.append((float(c), z_dual))
        except (ValueError, ZeroDivisionError):
            continue

    # At the self-dual point: compare Z_A and Z_{A!}
    try:
        coeffs_sd = shadow_coefficients(family, c_center, max_r)
        coeffs_sd_dual = koszul_dual_shadow_coefficients(family, c_center, max_r)
        z_sd = central_charge(coeffs_sd, r_target)
        z_sd_dual = central_charge(coeffs_sd_dual, r_target)
        sd_ratio = z_sd / z_sd_dual if abs(z_sd_dual) > 1e-30 else complex('nan')
    except (ValueError, ZeroDivisionError):
        sd_ratio = complex('nan')

    return {
        'forward_trajectory': forward,
        'dual_trajectory': reverse,
        'self_dual_Z': z_sd if 'z_sd' in dir() else None,
        'self_dual_Z_dual': z_sd_dual if 'z_sd_dual' in dir() else None,
        'self_dual_ratio': sd_ratio,
        'c_center': c_center,
        'c_radius': c_radius,
    }


# ============================================================================
# 9.  Walls of marginal stability
# ============================================================================

def wall_of_marginal_stability(
    family: str,
    r1: int,
    r2: int,
    param_min: float = 0.5,
    param_max: float = 25.5,
    n_points: int = 500,
    max_r: int = 50,
) -> List[float]:
    """Find parameter values where phi(gamma_{r1}) = phi(gamma_{r2}).

    These are walls of marginal stability: the phases of two generators
    coincide, so a bound state can form or decay.

    Returns
    -------
    List of parameter values at the walls.
    """
    params = np.linspace(param_min, param_max, n_points)
    phase_diffs = []
    for p in params:
        try:
            coeffs = shadow_coefficients(family, float(p), max_r)
            Z1 = central_charge(coeffs, r1)
            Z2 = central_charge(coeffs, r2)
            phi1 = phase(Z1)
            phi2 = phase(Z2)
            if math.isnan(phi1) or math.isnan(phi2):
                phase_diffs.append(float('nan'))
            else:
                phase_diffs.append(phi1 - phi2)
        except (ValueError, ZeroDivisionError):
            phase_diffs.append(float('nan'))

    walls = []
    for i in range(len(phase_diffs) - 1):
        if math.isnan(phase_diffs[i]) or math.isnan(phase_diffs[i + 1]):
            continue
        if phase_diffs[i] * phase_diffs[i + 1] < 0:
            # Bisect
            lo, hi = float(params[i]), float(params[i + 1])
            for _ in range(60):
                mid = (lo + hi) / 2.0
                try:
                    coeffs = shadow_coefficients(family, mid, max_r)
                    Z1 = central_charge(coeffs, r1)
                    Z2 = central_charge(coeffs, r2)
                    phi_mid1 = phase(Z1)
                    phi_mid2 = phase(Z2)
                    d = phi_mid1 - phi_mid2
                except (ValueError, ZeroDivisionError):
                    break
                if d * phase_diffs[i] < 0:
                    hi = mid
                else:
                    lo = mid
            walls.append((lo + hi) / 2.0)

    return walls


# ============================================================================
# 10.  Self-duality and complementarity analysis
# ============================================================================

def self_duality_check(
    family: str,
    c_self_dual: float,
    max_r: int = 50,
    tol: float = 1e-6,
) -> Dict[str, Any]:
    """Check self-duality of the stability condition at the self-dual point.

    For Virasoro at c=13: Vir_13^! = Vir_13, so Z_A = Z_{A!}.

    Returns dict with comparison data.
    """
    coeffs = shadow_coefficients(family, c_self_dual, max_r)
    coeffs_dual = koszul_dual_shadow_coefficients(family, c_self_dual, max_r)

    max_diff = 0.0
    diffs = {}
    for r in range(2, max_r + 1):
        S_r = coeffs.get(r, 0.0)
        S_r_dual = coeffs_dual.get(r, 0.0)
        diff = abs(S_r - S_r_dual)
        diffs[r] = diff
        if diff > max_diff:
            max_diff = diff

    is_self_dual = max_diff < tol
    return {
        'is_self_dual': is_self_dual,
        'max_coefficient_diff': max_diff,
        'diffs': diffs,
        'c': c_self_dual,
    }


def complementarity_sum_kappa(
    family: str,
    param: float,
) -> float:
    """Compute kappa(A) + kappa(A!) for a given family and parameter.

    For Virasoro: kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13 (AP24).
    For Heisenberg: kappa(k) + kappa(-k) = k + (-k) = 0.
    For affine sl_2: kappa(k) + kappa(-k-4) = 3(k+2)/4 + 3(-k-2)/4 = 0.
    """
    coeffs = shadow_coefficients(family, param, 5)
    coeffs_dual = koszul_dual_shadow_coefficients(family, param, 5)
    return coeffs.get(2, 0.0) + coeffs_dual.get(2, 0.0)


# ============================================================================
# 11.  Comprehensive stability analysis
# ============================================================================

@dataclass
class StabilityAnalysis:
    """Complete stability analysis for a shadow algebra."""
    family: str
    param: float
    coefficients: Dict[int, float]
    central_charges: Dict[int, complex]
    phases: Dict[int, float]
    masses: Dict[int, float]
    phase_gap_data: Tuple[float, float, float]
    support_holds: bool
    support_constant: float
    stability_dimension: int
    depth: Optional[int]
    massless_arities_list: List[int]


def full_stability_analysis(
    family: str,
    param: float,
    max_r: int = 50,
) -> StabilityAnalysis:
    """Run the complete stability analysis for a given algebra.

    Returns a StabilityAnalysis dataclass with all computed data.
    """
    coeffs = shadow_coefficients(family, param, max_r)
    Z_vec = central_charge_vector(coeffs, 2, max_r)
    phi_vec = {r: phase(z) for r, z in Z_vec.items()}
    M_vec = {r: mass(z) for r, z in Z_vec.items()}
    gap = phase_gap(phi_vec)
    holds, C = support_property_holds(coeffs, 2, max_r)
    dim = effective_stability_dimension(coeffs, 2, max_r)
    depth = shadow_depth(coeffs)
    massless = massless_arities(coeffs, 2, max_r)

    return StabilityAnalysis(
        family=family,
        param=param,
        coefficients=coeffs,
        central_charges=Z_vec,
        phases=phi_vec,
        masses=M_vec,
        phase_gap_data=gap,
        support_holds=holds,
        support_constant=C,
        stability_dimension=dim,
        depth=depth,
        massless_arities_list=massless,
    )
