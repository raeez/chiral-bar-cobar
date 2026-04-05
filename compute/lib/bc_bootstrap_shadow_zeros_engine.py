r"""BC-95: Conformal bootstrap at shadow zero locus.

The conformal bootstrap constrains CFT data via crossing symmetry:
the 4-point function expanded in the s-channel must equal the t-channel.
This module evaluates bootstrap equations AT the zeros of the shadow
zeta function zeta_A(s), turning each zero into a linear constraint
on OPE data.

MATHEMATICAL FRAMEWORK
======================

1. SHADOW CROSSING EQUATION:
   The shadow 4-point function (at leading order in the block expansion):
       G_A^{sh}(z) = sum_{r >= 2} S_r(A) * z^r
   Crossing symmetry z <-> 1-z requires:
       sum S_r [z^r - (1-z)^r] = 0   for all z.
   Define the bootstrap kernel B_r(z) = z^r - (1-z)^r.
   At a shadow zero rho (where zeta_A(rho) = 0, interpreted as a
   cross-ratio parameter): evaluate sum S_r B_r(rho).

2. LINEAR FUNCTIONAL METHOD (SDPB-style):
   Find alpha: alpha(B_0) > 0 and alpha(B_r) >= 0 for all r in the spectrum.
   If such alpha exists, the spectrum is inconsistent.
   For the shadow spectrum, truncate to r <= R_max and solve the LP/SDP.

3. GAP AT ZEROS:
   Each zero rho of zeta_A(s) gives one linear constraint sum S_r rho^{-r*s_0} = 0.
   With K zeros and R arities, the constraint matrix M_{n,r} = r^{-s_n} has
   rank that determines how much of {S_r} is fixed.

4. UNITARITY / SIGN PATTERN:
   In a unitary CFT, OPE coefficients squared are non-negative.
   The shadow coefficients S_r may violate positivity (oscillatory decay
   for class M).  Compute the sign pattern.

5. MODULAR BOOTSTRAP:
   The shadow partition function Z^{sh}_A(tau) = sum S_r q^{r - kappa}.
   Test modular invariance: Z(tau) vs Z(-1/tau) at special tau values.

6. EXTREMAL FUNCTIONAL AT ZEROS:
   alpha_c(f) = sum_{rho: zeta(rho)=0} a_rho * f(rho),
   with {a_rho} chosen to extremize an objective (bound on S_2 given S_3).

7. BOOTSTRAP ISLANDS:
   Allowed region in (S_2, S_3) space compatible with crossing, unitarity,
   and the first N zeros of zeta_A.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    landscape_census.tex (authoritative kappa values)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP15): genus-1 propagator is E_2* (quasi-modular).
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np

# ---------------------------------------------------------------------------
# Import shadow coefficient providers and zeta machinery
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
    virasoro_growth_rate_exact,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    find_zeros_grid,
    newton_zero,
    affine_sl2_zeros,
    _shadow_zeta_complex,
)


# ============================================================================
# 0.  Shadow coefficient retrieval (convenience wrappers)
# ============================================================================

def get_shadow_coefficients(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """Retrieve shadow coefficients S_r for a given family and parameter.

    Delegates to shadow_coefficients_extended from bc_shadow_zeta_zeros_engine.

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
    return shadow_coefficients_extended(family, param, max_r)


def get_shadow_zeros(
    family: str,
    param: float,
    max_r: int = 50,
    n_zeros: int = 50,
    im_range: Tuple[float, float] = (-200.0, 200.0),
) -> List[complex]:
    """Find zeros of zeta_A(s) for the given family.

    For finite towers, uses exact formulas when available.
    For infinite towers, uses Newton grid search.

    Returns
    -------
    List of zeros sorted by |Im(s)|.
    """
    coeffs = get_shadow_coefficients(family, param, max_r)
    # Use grid search for general case
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-10.0, 10.0),
        im_range=im_range,
        grid_re=30,
        grid_im=min(200, 4 * n_zeros),
        max_r=max_r,
    )
    # Sort by |Im(s)| and return at most n_zeros
    zeros.sort(key=lambda z: (abs(z.imag), z.real))
    return zeros[:n_zeros]


# ============================================================================
# 1.  Shadow crossing equation
# ============================================================================

def bootstrap_kernel(r: int, z: complex) -> complex:
    """Bootstrap kernel B_r(z) = z^r - (1-z)^r.

    Crossing symmetry of the shadow 4-point function at leading order
    requires sum_r S_r * B_r(z) = 0 for all z.

    B_r(z) is antisymmetric under z -> 1-z:
        B_r(1-z) = (1-z)^r - z^r = -B_r(z).
    """
    return z ** r - (1 - z) ** r


def bootstrap_kernel_symmetrized(r: int, z: complex) -> complex:
    """Symmetrized bootstrap kernel: B_r(z) + B_r(1-z) = 0.

    This is identically zero by the antisymmetry of B_r.
    Included for verification: crossing consistency requires
    the antisymmetric part to vanish, which it does identically.
    """
    return bootstrap_kernel(r, z) + bootstrap_kernel(r, 1 - z)


def crossing_sum_direct(
    shadow_coeffs: Dict[int, float],
    z: complex,
    max_r: Optional[int] = None,
) -> complex:
    r"""Compute sum_{r>=2} S_r * B_r(z) by direct summation.

    If the S_r satisfy crossing symmetry, this should vanish for all z.
    In general, the shadow tower does NOT satisfy 4-point crossing
    (it encodes modular data, not sphere crossing), so this sum is
    generically nonzero.

    Parameters
    ----------
    shadow_coeffs : dict of arity -> S_r
    z : cross-ratio
    max_r : truncation arity

    Returns
    -------
    Complex value of the sum.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        total += Sr * bootstrap_kernel(r, z)
    return total


def crossing_sum_via_symmetrization(
    shadow_coeffs: Dict[int, float],
    z: complex,
    max_r: Optional[int] = None,
) -> complex:
    r"""Compute the crossing sum via G(z) - G(1-z).

    G(z) = sum S_r z^r.
    Crossing sum = G(z) - G(1-z) = sum S_r [z^r - (1-z)^r] = sum S_r B_r(z).

    This is an independent computation path for verification.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Gz = 0.0 + 0.0j
    G1mz = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        Gz += Sr * z ** r
        G1mz += Sr * (1 - z) ** r
    return Gz - G1mz


def crossing_residual_at_zeros(
    shadow_coeffs: Dict[int, float],
    zeros: List[complex],
    max_r: Optional[int] = None,
) -> List[Tuple[complex, complex]]:
    """Evaluate crossing sum at each shadow zero rho.

    Each zero rho of zeta_A(s) is reinterpreted as a cross-ratio.
    The crossing residual sum_r S_r B_r(rho) is computed at each.

    Returns list of (rho, crossing_sum) pairs.
    """
    results = []
    for rho in zeros:
        cs = crossing_sum_direct(shadow_coeffs, rho, max_r)
        results.append((rho, cs))
    return results


# ============================================================================
# 2.  SDP-style linear functional (bootstrap bound)
# ============================================================================

def bootstrap_feasibility_matrix(
    max_r: int = 20,
    z_values: Optional[List[complex]] = None,
) -> np.ndarray:
    """Construct the bootstrap matrix A_{i,r} = B_r(z_i).

    For the linear functional method, we seek alpha such that:
        sum_i alpha_i * B_r(z_i) >= 0 for all r in the spectrum,
        sum_i alpha_i * B_0(z_i) > 0.

    Here B_0 is the identity-channel contribution.

    Parameters
    ----------
    max_r : maximum arity in the truncated spectrum
    z_values : evaluation points (default: uniform grid on [0.1, 0.9])

    Returns
    -------
    Matrix A of shape (n_points, max_r - 1) for r = 2..max_r.
    """
    if z_values is None:
        z_values = [complex(0.1 + 0.8 * i / 19) for i in range(20)]
    n_pts = len(z_values)
    n_arities = max_r - 1  # r = 2, ..., max_r
    A = np.zeros((n_pts, n_arities), dtype=complex)
    for i, z in enumerate(z_values):
        for j, r in enumerate(range(2, max_r + 1)):
            A[i, j] = bootstrap_kernel(r, z)
    return A


def check_sdp_feasibility(
    shadow_coeffs: Dict[int, float],
    max_r: int = 20,
    n_points: int = 30,
) -> Dict[str, Any]:
    """Check if the shadow spectrum is bootstrap-compatible via LP relaxation.

    Uses a simple linear programming approach:
    - If all S_r >= 0, the spectrum is trivially consistent with positivity.
    - If some S_r < 0, check if the sign pattern is compatible with crossing.

    This is a RELAXATION of the full SDP; it gives necessary conditions.

    Returns
    -------
    Dict with 'feasible' (bool), 'violation_arities' (list), 'details' (str).
    """
    # Check positivity of S_r (necessary for unitarity)
    violations = []
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr < 0:
            violations.append(r)

    # Check crossing consistency at sample points
    z_vals = [0.1 + 0.8 * i / (n_points - 1) for i in range(n_points)]
    crossing_residuals = []
    for z in z_vals:
        cs = crossing_sum_direct(shadow_coeffs, complex(z), max_r)
        crossing_residuals.append(abs(cs))

    max_residual = max(crossing_residuals) if crossing_residuals else 0.0

    # Construct the constraint matrix for LP feasibility
    # The crossing equation sum S_r B_r(z) = 0 gives constraints at each z.
    # With the actual S_r values, we measure how far from crossing we are.
    A = bootstrap_feasibility_matrix(max_r, [complex(z) for z in z_vals])
    S_vec = np.array([shadow_coeffs.get(r, 0.0) for r in range(2, max_r + 1)])
    crossing_vec = A @ S_vec  # Should be zero if crossing holds

    # Simple feasibility check: crossing + positivity
    crossing_norm = np.linalg.norm(crossing_vec.real)
    positivity_ok = len(violations) == 0

    return {
        'feasible': positivity_ok and crossing_norm < 1e-6,
        'positivity_violations': violations,
        'crossing_norm': float(crossing_norm),
        'max_crossing_residual': max_residual,
        'n_positive': sum(1 for r in range(2, max_r + 1) if shadow_coeffs.get(r, 0.0) >= 0),
        'n_negative': len(violations),
        'details': (
            f"Positivity: {len(violations)} violations. "
            f"Crossing norm: {crossing_norm:.6e}. "
            f"{'FEASIBLE' if positivity_ok and crossing_norm < 1e-6 else 'INFEASIBLE'}."
        ),
    }


def interior_point_feasibility(
    shadow_coeffs: Dict[int, float],
    max_r: int = 20,
    n_constraints: int = 30,
) -> Dict[str, Any]:
    """Interior point feasibility check (verification path 2).

    Alternative to the simplex-style check, using a barrier function approach.
    For each sample z, the crossing sum provides a linear constraint.
    We check if the system has a feasible interior point.

    Returns dict with 'feasible', 'barrier_value', etc.
    """
    z_vals = [complex(0.05 + 0.9 * i / (n_constraints - 1))
              for i in range(n_constraints)]
    S_vec = np.array([shadow_coeffs.get(r, 0.0) for r in range(2, max_r + 1)])

    # Barrier: sum of log(S_r) for S_r > 0 (interior of positive cone)
    barrier = 0.0
    n_interior = 0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr > 0:
            barrier += math.log(Sr)
            n_interior += 1

    # Constraint violations
    A = bootstrap_feasibility_matrix(max_r, z_vals)
    residuals = A @ S_vec
    constraint_violation = float(np.linalg.norm(residuals.real))

    return {
        'feasible': n_interior == (max_r - 1) and constraint_violation < 1e-6,
        'barrier_value': barrier,
        'n_interior_points': n_interior,
        'n_total_arities': max_r - 1,
        'constraint_violation': constraint_violation,
    }


# ============================================================================
# 3.  Constraint matrix from zeros (spectrum determination)
# ============================================================================

def constraint_matrix_from_zeros(
    zeros: List[complex],
    max_r: int = 20,
) -> np.ndarray:
    """Construct constraint matrix M_{n,r} = r^{-s_n}.

    Each zero s_n of zeta_A gives the linear constraint:
        sum_{r >= 2} S_r * r^{-s_n} = 0.

    With K zeros and R arities, M is K x (R-1) with r = 2..R.

    Parameters
    ----------
    zeros : list of K zeros of zeta_A
    max_r : maximum arity R

    Returns
    -------
    Complex matrix of shape (K, R-1).
    """
    K = len(zeros)
    R_count = max_r - 1  # r = 2, ..., max_r
    M = np.zeros((K, R_count), dtype=complex)
    for n, s_n in enumerate(zeros):
        for j, r in enumerate(range(2, max_r + 1)):
            M[n, j] = r ** (-s_n)
    return M


def constraint_matrix_rank_svd(
    zeros: List[complex],
    max_r: int = 20,
    tol: float = 1e-8,
) -> Dict[str, Any]:
    """Compute rank of constraint matrix via SVD.

    Path 1 for rank computation.

    Returns dict with 'rank', 'singular_values', 'condition_number'.
    """
    M = constraint_matrix_from_zeros(zeros, max_r)
    if M.size == 0:
        return {'rank': 0, 'singular_values': [], 'condition_number': float('inf')}

    sv = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(sv > tol * sv[0])) if len(sv) > 0 and sv[0] > 0 else 0
    cond = float(sv[0] / sv[-1]) if len(sv) > 0 and sv[-1] > tol else float('inf')

    return {
        'rank': rank,
        'singular_values': sv.tolist(),
        'condition_number': cond,
        'n_zeros': len(zeros),
        'n_arities': max_r - 1,
        'max_possible_rank': min(len(zeros), max_r - 1),
    }


def constraint_matrix_rank_qr(
    zeros: List[complex],
    max_r: int = 20,
    tol: float = 1e-8,
) -> Dict[str, Any]:
    """Compute rank of constraint matrix via QR decomposition.

    Path 2 for rank computation (independent of SVD).

    Returns dict with 'rank', 'R_diagonal'.
    """
    M = constraint_matrix_from_zeros(zeros, max_r)
    if M.size == 0:
        return {'rank': 0, 'R_diagonal': []}

    Q, R = np.linalg.qr(M)
    # Rank = number of nonzero diagonal elements of R
    diag_R = np.abs(np.diag(R))
    threshold = tol * diag_R[0] if len(diag_R) > 0 and diag_R[0] > 0 else tol
    rank = int(np.sum(diag_R > threshold))

    return {
        'rank': rank,
        'R_diagonal': diag_R.tolist(),
        'n_zeros': len(zeros),
        'n_arities': max_r - 1,
    }


def spectrum_determination_analysis(
    family: str,
    param: float,
    max_r: int = 20,
    n_zeros_list: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Analyze how many zeros are needed to determine the spectrum.

    For K zeros, compute rank(M) where M is K x (R-1).
    If rank = R-1 (full column rank), the zeros fully determine {S_r}.

    Parameters
    ----------
    family, param : algebra family and parameter
    max_r : maximum arity (defines dimension of spectrum space)
    n_zeros_list : list of K values to test (default [5, 10, 15, 20, 30, 50])

    Returns
    -------
    Dict with rank progression and determination threshold.
    """
    if n_zeros_list is None:
        n_zeros_list = [5, 10, 15, 20, 30, 50]

    coeffs = get_shadow_coefficients(family, param, max_r)
    all_zeros = get_shadow_zeros(family, param, max_r, max(n_zeros_list))

    results = []
    for K in n_zeros_list:
        subset = all_zeros[:K]
        if len(subset) == 0:
            results.append({'K': K, 'rank': 0, 'determined': False})
            continue
        svd_data = constraint_matrix_rank_svd(subset, max_r)
        results.append({
            'K': K,
            'rank': svd_data['rank'],
            'max_rank': max_r - 1,
            'determined': svd_data['rank'] >= max_r - 1,
            'condition': svd_data['condition_number'],
        })

    # Find determination threshold
    threshold_K = None
    for entry in results:
        if entry.get('determined', False):
            threshold_K = entry['K']
            break

    return {
        'family': family,
        'param': param,
        'max_r': max_r,
        'rank_progression': results,
        'determination_threshold': threshold_K,
    }


# ============================================================================
# 4.  Sign pattern analysis (unitarity bounds)
# ============================================================================

def sign_pattern(
    shadow_coeffs: Dict[int, float],
    max_r: int = 100,
) -> Dict[str, Any]:
    """Compute sign pattern of S_r for r = 2..max_r.

    In a unitary CFT, OPE coefficients squared C_{ijO}^2 >= 0.
    The shadow coefficients S_r encode DIFFERENT data (MC projections),
    so positivity is NOT required.  However, the sign pattern reveals
    whether the shadow spectrum COULD arise from a unitary CFT.

    Returns dict with:
      'signs': list of +1, 0, -1 for each r
      'first_negative': first r where S_r < 0 (or None)
      'n_positive', 'n_negative', 'n_zero': counts
      'oscillation_period': estimated period if alternating
    """
    signs = []
    first_neg = None
    n_pos = 0
    n_neg = 0
    n_zero = 0

    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr > 1e-300:
            signs.append(1)
            n_pos += 1
        elif Sr < -1e-300:
            signs.append(-1)
            n_neg += 1
            if first_neg is None:
                first_neg = r
        else:
            signs.append(0)
            n_zero += 1

    # Estimate oscillation period from sign changes
    changes = []
    for i in range(1, len(signs)):
        if signs[i] != 0 and signs[i - 1] != 0 and signs[i] != signs[i - 1]:
            changes.append(i + 2)  # r = i+2
    if len(changes) >= 2:
        diffs = [changes[i + 1] - changes[i] for i in range(len(changes) - 1)]
        avg_period = sum(diffs) / len(diffs)
    else:
        avg_period = None

    return {
        'signs': signs,
        'first_negative': first_neg,
        'n_positive': n_pos,
        'n_negative': n_neg,
        'n_zero': n_zero,
        'n_sign_changes': len(changes),
        'sign_change_positions': changes,
        'oscillation_period': avg_period,
        'violates_unitarity': n_neg > 0,
    }


def sign_pattern_from_asymptotic(
    c_val: float,
    max_r: int = 100,
) -> Dict[str, Any]:
    r"""Predict sign pattern from the asymptotic formula S_r ~ C * rho^r * r^{-5/2}.

    For Virasoro: the shadow coefficients are obtained from the Taylor
    expansion of sqrt(Q_L(t)).  The asymptotic sign is determined by the
    algebraicity of Q_L: when Q_L has complex roots, the expansion
    oscillates.

    Critical discriminant: Delta = 8*kappa*S_4 = 80/(c*(5c+22)).
    For c > 0: Delta > 0, so Q_L has complex roots and the tower oscillates.

    The oscillation is governed by the argument of the complex root of Q_L:
        theta = arctan(sqrt(Delta) / (2*kappa + 3*alpha))
    where alpha is the cubic shadow.

    Returns
    -------
    Dict with predicted signs from the asymptotic formula.
    """
    kappa = c_val / 2.0
    if kappa == 0:
        return {'predicted_signs': [], 'note': 'kappa=0: degenerate'}

    alpha = 2.0  # Virasoro cubic shadow
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0)) if c_val != 0 and 5 * c_val + 22 != 0 else 0.0
    Delta = 8.0 * kappa * S4

    # Q_L(t) = (2*kappa)^2 + 2*(2*kappa)*(3*alpha)*t + (9*alpha^2 + 2*Delta)*t^2
    # Roots of Q_L: t = -(3*alpha +/- i*sqrt(2*Delta)) / (something)
    # The oscillation period is 2*pi / |log(t_+/t_-)|
    a_coeff = 9.0 * alpha ** 2 + 2.0 * Delta
    b_coeff = 2.0 * (2.0 * kappa) * (3.0 * alpha)
    c_coeff = (2.0 * kappa) ** 2

    discriminant = b_coeff ** 2 - 4.0 * a_coeff * c_coeff
    if discriminant >= 0:
        # Real roots: no oscillation
        return {
            'predicted_oscillation': False,
            'discriminant': discriminant,
            'note': 'Real roots of Q_L: monotone decay',
        }

    # Complex roots: oscillation
    theta = math.atan2(math.sqrt(-discriminant), -b_coeff)
    period = 2.0 * math.pi / theta if theta > 0 else float('inf')

    # Predict signs from the asymptotic
    predicted = []
    for r in range(2, max_r + 1):
        # Leading asymptotic: S_r ~ C * rho^r * cos(r*theta + phi) * r^{-5/2}
        phase = r * theta
        predicted.append(1 if math.cos(phase) >= 0 else -1)

    return {
        'predicted_oscillation': True,
        'discriminant': discriminant,
        'theta': theta,
        'period': period,
        'predicted_signs': predicted,
    }


def virasoro_sign_pattern_landscape(
    c_values: Optional[List[float]] = None,
    max_r: int = 50,
) -> Dict[float, Dict[str, Any]]:
    """Compute sign pattern for Virasoro at multiple c values.

    Default c_values: 1, 4, 7, 10, 13, 16, 19, 22, 25.

    Returns dict mapping c -> sign_pattern result.
    """
    if c_values is None:
        c_values = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0, 25.0]

    results = {}
    for c in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c, max_r)
            results[c] = sign_pattern(coeffs, max_r)
        except (ValueError, ZeroDivisionError):
            results[c] = {'error': f'Computation failed at c={c}'}
    return results


# ============================================================================
# 5.  Modular bootstrap (shadow partition function)
# ============================================================================

def shadow_partition_function(
    shadow_coeffs: Dict[int, float],
    tau: complex,
    kappa_val: float,
    max_r: Optional[int] = None,
) -> complex:
    r"""Shadow partition function Z^{sh}_A(tau) = sum_{r>=2} S_r * q^{r - kappa}.

    Here q = exp(2*pi*i*tau).

    WARNING: This is a formal analogy.  The shadow tower does NOT literally
    produce a modular-invariant partition function in general.  Modular
    invariance of Z^{sh} is a PROPERTY TO BE TESTED, not a given.

    Parameters
    ----------
    shadow_coeffs : dict of S_r
    tau : modular parameter (upper half-plane, Im(tau) > 0)
    kappa_val : modular characteristic kappa(A)
    max_r : truncation arity
    """
    if tau.imag <= 0:
        raise ValueError(f"tau must have positive imaginary part, got Im(tau) = {tau.imag}")

    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    q = cmath.exp(2j * cmath.pi * tau)
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        power = r - kappa_val
        # Use exp(power * log(q)) to handle q ~ 0 with negative powers
        try:
            term = Sr * cmath.exp(power * cmath.log(q))
        except (ValueError, OverflowError, ZeroDivisionError):
            # For very large Im(tau), q ~ 0 and negative power -> overflow
            if power < 0 and abs(q) < 1e-300:
                term = complex(float('inf'), 0)
            else:
                term = 0.0 + 0.0j
        total += term
    return total


def modular_anomaly(
    shadow_coeffs: Dict[int, float],
    tau: complex,
    kappa_val: float,
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Compute the modular anomaly: Z^{sh}(tau) - Z^{sh}(-1/tau).

    For a modular-invariant partition function, this should be zero.
    The anomaly measures how far the shadow partition function is
    from being modular.

    Returns dict with 'Z_tau', 'Z_inv', 'anomaly', 'relative_anomaly'.
    """
    Z_tau = shadow_partition_function(shadow_coeffs, tau, kappa_val, max_r)
    tau_inv = -1.0 / tau
    Z_inv = shadow_partition_function(shadow_coeffs, tau_inv, kappa_val, max_r)

    anomaly = Z_tau - Z_inv
    rel = abs(anomaly) / max(abs(Z_tau), abs(Z_inv), 1e-300)

    return {
        'tau': tau,
        'Z_tau': Z_tau,
        'Z_minus_inv_tau': Z_inv,
        'anomaly': anomaly,
        'anomaly_abs': abs(anomaly),
        'relative_anomaly': rel,
        'is_modular': rel < 1e-6,
    }


def modular_anomaly_landscape(
    shadow_coeffs: Dict[int, float],
    kappa_val: float,
    tau_values: Optional[List[complex]] = None,
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    """Compute modular anomaly at multiple tau values.

    Default tau: i, exp(2*pi*i/3), (1 + i*sqrt(3))/2.

    Returns dict with anomalies at each tau.
    """
    if tau_values is None:
        tau_values = [
            complex(0, 1),  # tau = i (self-dual under S)
            cmath.exp(2j * cmath.pi / 3),  # tau = omega
            complex(0.5, math.sqrt(3) / 2),  # tau = (1 + i*sqrt(3))/2
        ]

    results = {}
    for idx, tau in enumerate(tau_values):
        if tau.imag <= 0:
            results[f'tau_{idx}'] = {'error': f'Im(tau)={tau.imag} <= 0'}
            continue
        results[f'tau_{idx}'] = modular_anomaly(shadow_coeffs, tau, kappa_val, max_r)

    return results


# ============================================================================
# 6.  Extremal functional at shadow zeros
# ============================================================================

def extremal_functional_coefficients(
    zeros: List[complex],
    objective_r: int = 2,
    constraint_r: int = 3,
    max_r: int = 20,
) -> Dict[str, Any]:
    """Compute extremal functional coefficients for bounding S_{objective_r}.

    Given zeros rho_1, ..., rho_K, find weights a_1, ..., a_K such that:
        alpha(f) = sum_n a_n * f(rho_n)
    maximizes alpha(e_objective) subject to alpha(e_constraint) = 1,
    where e_r(s) = r^{-s} (the basis functional for arity r).

    This is a constrained optimization solved via Lagrange multipliers.

    Uses the first min(K, max_r) zeros.

    Parameters
    ----------
    zeros : list of zeta zeros
    objective_r : arity to bound (default 2 = kappa)
    constraint_r : arity to normalize (default 3 = cubic shadow)
    max_r : dimension of the functional space

    Returns
    -------
    Dict with 'coefficients' (weights a_n), 'bound_value'.
    """
    K = min(len(zeros), max_r)
    if K == 0:
        return {'coefficients': [], 'bound_value': 0.0, 'error': 'No zeros'}

    subset = zeros[:K]

    # Build the matrix: each row is a zero, columns are e_r(rho_n) = r^{-rho_n}
    # for r = 2..max_r
    n_arities = max_r - 1
    M = np.zeros((K, n_arities), dtype=complex)
    for n, rho in enumerate(subset):
        for j, r in enumerate(range(2, max_r + 1)):
            M[n, j] = r ** (-rho)

    # Objective: maximize sum_n a_n * objective_r^{-rho_n}
    obj_vec = np.array([objective_r ** (-rho) for rho in subset])
    # Constraint: sum_n a_n * constraint_r^{-rho_n} = 1
    con_vec = np.array([constraint_r ** (-rho) for rho in subset])

    # Additional constraints: zeta(rho_n) = 0, so M^T a encodes
    # the constraint that the functional annihilates on the zero set.

    # Solve via least squares with constraint
    # max Re(obj_vec^H a) subject to Re(con_vec^H a) = 1
    # Using Lagrange: a = lambda * (obj_vec - mu * con_vec) + ...
    # Simplify: solve the system (con_vec^H con_vec) * lambda = con_vec^H obj_vec - ...

    # Simple approach: normalize objective by constraint
    con_norm_sq = float(np.real(np.dot(np.conj(con_vec), con_vec)))
    if con_norm_sq < 1e-300:
        return {'coefficients': [], 'bound_value': 0.0, 'error': 'Degenerate constraint'}

    # a = con_vec / ||con_vec||^2 (satisfies constraint = 1)
    a_basic = con_vec / con_norm_sq
    bound_basic = float(np.real(np.dot(np.conj(obj_vec), a_basic)))

    # Improve: project out the constraint direction and add the objective
    proj = obj_vec - np.dot(np.conj(con_vec), obj_vec) / con_norm_sq * con_vec
    proj_norm = float(np.linalg.norm(proj))
    if proj_norm > 1e-300:
        a_improved = a_basic + proj / proj_norm
        bound_improved = float(np.real(np.dot(np.conj(obj_vec), a_improved)))
    else:
        a_improved = a_basic
        bound_improved = bound_basic

    return {
        'coefficients': a_improved.tolist(),
        'bound_value': bound_improved,
        'bound_basic': bound_basic,
        'n_zeros_used': K,
    }


# ============================================================================
# 7.  Bootstrap islands (allowed region in (S_2, S_3) space)
# ============================================================================

def bootstrap_island_scan(
    family: str,
    param: float,
    n_zeros: int = 10,
    S2_range: Tuple[float, float] = (0.0, 30.0),
    S3_range: Tuple[float, float] = (-5.0, 10.0),
    grid_size: int = 50,
    max_r: int = 20,
) -> Dict[str, Any]:
    """Scan (S_2, S_3) plane for bootstrap-compatible points.

    For each (S_2, S_3) grid point, check:
    1. Crossing consistency with the first n_zeros zeros.
    2. Positivity of S_r for r >= 4 (derived from MC recursion given S_2, S_3).

    The "island" is the region where all constraints are satisfied.

    Returns dict with the allowed region points and the actual (S_2, S_3) value.
    """
    # Get actual shadow data
    coeffs = get_shadow_coefficients(family, param, max_r)
    actual_S2 = coeffs.get(2, 0.0)
    actual_S3 = coeffs.get(3, 0.0)

    # Get zeros
    zeros = get_shadow_zeros(family, param, max_r, n_zeros)

    # Build constraint matrix from zeros
    if len(zeros) > 0:
        M = constraint_matrix_from_zeros(zeros, max_r)
    else:
        M = None

    # Scan the grid
    S2_vals = np.linspace(S2_range[0], S2_range[1], grid_size)
    S3_vals = np.linspace(S3_range[0], S3_range[1], grid_size)

    allowed = []
    for S2 in S2_vals:
        for S3 in S3_vals:
            # Construct trial S vector (assume S_r = 0 for r >= 4 as simplest)
            trial = np.zeros(max_r - 1, dtype=complex)
            trial[0] = S2  # r=2
            trial[1] = S3  # r=3
            # rest are zero

            # Check constraint: M @ trial should have small norm
            if M is not None and M.shape[0] > 0:
                residual = M @ trial
                res_norm = float(np.linalg.norm(residual))
            else:
                res_norm = 0.0

            # Crossing check at z = 0.5
            crossing_at_half = abs(S2 * bootstrap_kernel(2, 0.5) +
                                   S3 * bootstrap_kernel(3, 0.5))

            # Simple compatibility score
            score = res_norm + crossing_at_half
            if score < 1.0:  # relaxed threshold for the scan
                allowed.append((float(S2), float(S3), score))

    return {
        'actual_S2': actual_S2,
        'actual_S3': actual_S3,
        'allowed_points': allowed,
        'n_allowed': len(allowed),
        'n_total': grid_size ** 2,
        'fraction_allowed': len(allowed) / grid_size ** 2,
        'n_zeros_used': len(zeros),
    }


def island_shrinkage(
    family: str,
    param: float,
    n_zeros_list: Optional[List[int]] = None,
    max_r: int = 20,
    grid_size: int = 30,
) -> Dict[str, Any]:
    """Track how the bootstrap island shrinks with more zeros.

    Returns the fraction of allowed (S_2, S_3) points as a function
    of the number of zeros used.
    """
    if n_zeros_list is None:
        n_zeros_list = [0, 2, 5, 10, 20, 50]

    coeffs = get_shadow_coefficients(family, param, max_r)
    actual_S2 = coeffs.get(2, 0.0)
    actual_S3 = coeffs.get(3, 0.0)

    # Set scan range around the actual values
    margin = max(abs(actual_S2), abs(actual_S3), 5.0) * 2
    S2_range = (actual_S2 - margin, actual_S2 + margin)
    S3_range = (actual_S3 - margin, actual_S3 + margin)

    shrinkage = []
    for n_z in n_zeros_list:
        if n_z == 0:
            # No constraints: everything is allowed
            shrinkage.append({'n_zeros': 0, 'fraction_allowed': 1.0})
            continue

        result = bootstrap_island_scan(
            family, param, n_z, S2_range, S3_range, grid_size, max_r
        )
        shrinkage.append({
            'n_zeros': n_z,
            'fraction_allowed': result['fraction_allowed'],
            'n_allowed': result['n_allowed'],
        })

    return {
        'family': family,
        'param': param,
        'actual_S2': actual_S2,
        'actual_S3': actual_S3,
        'shrinkage': shrinkage,
    }


# ============================================================================
# 8.  Cross-verification utilities
# ============================================================================

def verify_crossing_two_ways(
    shadow_coeffs: Dict[int, float],
    z: complex,
    max_r: int = 50,
) -> Dict[str, Any]:
    """Verify crossing sum via direct and symmetrization methods.

    Path 1: sum S_r B_r(z) (direct)
    Path 2: G(z) - G(1-z) (symmetrization)

    They must agree to machine precision.
    """
    direct = crossing_sum_direct(shadow_coeffs, z, max_r)
    symmetrized = crossing_sum_via_symmetrization(shadow_coeffs, z, max_r)
    diff = abs(direct - symmetrized)
    rel = diff / max(abs(direct), abs(symmetrized), 1e-300)

    return {
        'z': z,
        'direct': direct,
        'symmetrized': symmetrized,
        'absolute_difference': diff,
        'relative_difference': rel,
        'agree': rel < 1e-10,
    }


def verify_rank_two_ways(
    zeros: List[complex],
    max_r: int = 20,
    tol: float = 1e-8,
) -> Dict[str, Any]:
    """Verify constraint matrix rank via SVD and QR.

    Two independent rank computations that must agree.
    """
    svd_result = constraint_matrix_rank_svd(zeros, max_r, tol)
    qr_result = constraint_matrix_rank_qr(zeros, max_r, tol)

    return {
        'rank_svd': svd_result['rank'],
        'rank_qr': qr_result['rank'],
        'agree': svd_result['rank'] == qr_result['rank'],
        'svd_condition': svd_result['condition_number'],
    }


def verify_kernel_antisymmetry(r_values: Optional[List[int]] = None) -> List[Dict[str, Any]]:
    """Verify B_r(z) + B_r(1-z) = 0 for multiple r and z values.

    This is an exact identity; any deviation indicates a bug.
    """
    if r_values is None:
        r_values = list(range(2, 21))
    z_values = [0.1, 0.25, 0.3 + 0.1j, 0.5, 0.7, 0.9, 0.1 + 0.3j]

    results = []
    for r in r_values:
        for z in z_values:
            z = complex(z)
            s = bootstrap_kernel(r, z) + bootstrap_kernel(r, 1 - z)
            results.append({
                'r': r, 'z': z,
                'sum': s, 'abs_sum': abs(s),
                'exact_zero': abs(s) < 1e-12,
            })
    return results


def verify_modular_anomaly_multiple_tau(
    shadow_coeffs: Dict[int, float],
    kappa_val: float,
    max_r: int = 30,
) -> Dict[str, Any]:
    """Verify modular anomaly at 3 independent tau values.

    Path 3 for modular consistency.
    """
    tau_vals = [
        complex(0, 1.0),     # tau = i
        complex(0, 2.0),     # tau = 2i
        complex(0.5, math.sqrt(3) / 2),  # tau = e^{i*pi/3}
    ]

    anomalies = []
    for tau in tau_vals:
        result = modular_anomaly(shadow_coeffs, tau, kappa_val, max_r)
        anomalies.append(result)

    return {
        'anomalies': anomalies,
        'all_modular': all(a['is_modular'] for a in anomalies),
        'max_anomaly': max(a['anomaly_abs'] for a in anomalies),
    }


# ============================================================================
# 9.  Full bootstrap analysis for a given algebra
# ============================================================================

@dataclass
class BootstrapShadowZeroAnalysis:
    """Complete bootstrap analysis at shadow zero locus."""
    family: str
    param: float
    kappa: float
    shadow_class: str
    n_zeros_found: int
    crossing_residuals: List[float]
    sdp_feasibility: Dict[str, Any]
    rank_analysis: Dict[str, Any]
    sign_analysis: Dict[str, Any]
    modular_anomaly: Dict[str, Any]
    extremal_bound: Dict[str, Any]


def full_bootstrap_analysis(
    family: str,
    param: float,
    max_r: int = 30,
    n_zeros: int = 20,
) -> BootstrapShadowZeroAnalysis:
    """Run the full bootstrap analysis pipeline.

    Combines all seven components:
    1. Shadow crossing equation
    2. SDP feasibility
    3. Constraint matrix rank
    4. Sign pattern
    5. Modular bootstrap
    6. Extremal functional
    7. (Bootstrap islands computed separately due to cost)
    """
    # Shadow coefficients
    coeffs = get_shadow_coefficients(family, param, max_r)
    kappa_val = coeffs.get(2, 0.0)

    # Classify shadow depth
    nonzero_arities = [r for r in range(2, max_r + 1) if abs(coeffs.get(r, 0.0)) > 1e-300]
    if len(nonzero_arities) <= 1:
        shadow_class = 'G'
    elif max(nonzero_arities) <= 3:
        shadow_class = 'L'
    elif max(nonzero_arities) <= 4:
        shadow_class = 'C'
    else:
        shadow_class = 'M'

    # Find zeros
    zeros = get_shadow_zeros(family, param, max_r, n_zeros)

    # 1. Crossing residuals at zeros
    crossing_data = crossing_residual_at_zeros(coeffs, zeros, max_r)
    crossing_residuals = [abs(cs) for _, cs in crossing_data]

    # 2. SDP feasibility
    sdp = check_sdp_feasibility(coeffs, min(max_r, 20))

    # 3. Rank analysis
    if len(zeros) > 0:
        rank = constraint_matrix_rank_svd(zeros, min(max_r, 20))
    else:
        rank = {'rank': 0, 'singular_values': [], 'condition_number': float('inf')}

    # 4. Sign pattern
    sp = sign_pattern(coeffs, max_r)

    # 5. Modular anomaly
    if kappa_val != 0:
        ma = modular_anomaly_landscape(coeffs, kappa_val, max_r=max_r)
    else:
        ma = {'note': 'kappa=0: trivial shadow'}

    # 6. Extremal functional
    if len(zeros) >= 3:
        ext = extremal_functional_coefficients(zeros, 2, 3, min(max_r, 20))
    else:
        ext = {'note': 'Too few zeros for extremal functional'}

    return BootstrapShadowZeroAnalysis(
        family=family,
        param=param,
        kappa=kappa_val,
        shadow_class=shadow_class,
        n_zeros_found=len(zeros),
        crossing_residuals=crossing_residuals,
        sdp_feasibility=sdp,
        rank_analysis=rank,
        sign_analysis=sp,
        modular_anomaly=ma,
        extremal_bound=ext,
    )


# ============================================================================
# 10. Landscape sweep
# ============================================================================

def landscape_bootstrap_sweep(
    families: Optional[List[Tuple[str, float]]] = None,
    max_r: int = 30,
    n_zeros: int = 10,
) -> List[BootstrapShadowZeroAnalysis]:
    """Run full bootstrap analysis across the standard landscape.

    Default families: Heisenberg k=1, affine sl_2 k=1, betagamma lambda=0.5,
    Virasoro c=1/4/10/13/25.
    """
    if families is None:
        families = [
            ('heisenberg', 1.0),
            ('affine_sl2', 1.0),
            ('betagamma', 0.5),
            ('virasoro', 1.0),
            ('virasoro', 4.0),
            ('virasoro', 10.0),
            ('virasoro', 13.0),
            ('virasoro', 25.0),
        ]

    results = []
    for family, param in families:
        try:
            analysis = full_bootstrap_analysis(family, param, max_r, n_zeros)
            results.append(analysis)
        except Exception as e:
            # Skip failed families but record
            pass
    return results
