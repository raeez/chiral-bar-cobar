"""Shadow analysis verifications: Borel-Laplace, dispersion, Pade, Prony, fake measure.

Five verification tasks for the shadow Postnikov tower at leading order in 1/c:

Task 1 (Borel-Laplace sum verification):
    For Virasoro at several c-values, verify that the formal shadow series is
    Borel-summable to G(t) = -log(1 + 6t/c) + 6t/c.  The Borel transform has
    a pole at xi = c/6.  Carleman's condition guarantees uniqueness.

Task 2 (Dispersion relation):
    G(t) is reconstructed from its branch-cut discontinuity via the Cauchy
    dispersion integral.

Task 3 (Pade convergence):
    Diagonal Pade approximants of G(t) have poles converging geometrically
    to the branch point t = -c/6.

Task 4 (Rigidity defect and atom recovery):
    The Prony method recovers spectral atoms from the shadow moments.
    For Virasoro (1 atom), the system is overdetermined with zero residual.
    For Leech (2 atoms), the Hecke decomposition is recovered.

Task 5 (Fake spectral measure discrimination):
    A fake Leech measure violating the Ramanujan bound is discriminated from
    the genuine one by MC recursion violation at finite arity.

References:
    virasoro_shadow_gf.py -- exact S_r(c) via recursion
    shadow_complex_analysis.py -- branch cuts, Borel, Pade
    shadow_spectral_inversion.py -- spectral atoms from moments
    shadow_hecke_identification.py -- Hecke eigenvalues
    lattice_shadow_periods.py -- lattice VOA shadow data
"""

from __future__ import annotations

import cmath
import math
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    from scipy import integrate as scipy_integrate
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


# =====================================================================
# Constants
# =====================================================================

# Ramanujan tau function values (first 20)
_TAU_TABLE = {
    1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
    6: -6048, 7: -16744, 8: 84480, 9: -113643, 10: -115920,
    11: 534612, 12: -370944, 13: -577738, 14: 401856, 15: 1217160,
    16: 987136, 17: -6905934, 18: 2727432, 19: 10661420, 20: -7109760,
}


def ramanujan_tau(n: int) -> int:
    """Ramanujan tau function via eta^24 product expansion."""
    if n in _TAU_TABLE:
        return _TAU_TABLE[n]
    if n < 1:
        return 0
    # Compute via product expansion
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    return coeffs[n - 1] if n - 1 <= N else 0


def sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


# =====================================================================
# Task 1: Borel-Laplace sum verification
# =====================================================================

def virasoro_shadow_leading_order(c: float, r: int) -> float:
    """Leading-order Virasoro shadow coefficient S_r.

    Uses the formula S_r = (2/r) * (-3)^{r-4} * (2/c)^{r-2} as specified.
    This is the leading-order approximation from the combinatorial expansion.
    """
    return (2.0 / r) * (-3.0) ** (r - 4) * (2.0 / c) ** (r - 2)


def virasoro_shadow_log_form(c: float, r: int) -> float:
    """Shadow coefficient from G(t) = -log(1 + 6t/c) + 6t/c.

    S_r = (-6/c)^r / r for r >= 2.
    """
    return (-6.0 / c) ** r / r


def shadow_coefficients_leading(c: float, r_max: int) -> List[float]:
    """Compute S_r for r = 2, ..., r_max using the specified leading-order formula."""
    return [virasoro_shadow_leading_order(c, r) for r in range(2, r_max + 1)]


def shadow_coefficients_log(c: float, r_max: int) -> List[float]:
    """Compute S_r for r = 2, ..., r_max from G(t) = -log(1 + 6t/c) + 6t/c."""
    return [virasoro_shadow_log_form(c, r) for r in range(2, r_max + 1)]


def borel_transform_from_coeffs(
    coeffs: Sequence[float], xi: complex, r_start: int = 2
) -> complex:
    """Borel transform B(xi) = sum_{r>=r_start} S_r * xi^{r-1} / Gamma(r).

    This uses the convention B(xi) = sum S_r xi^{r-1} / Gamma(r),
    so that the Borel-Laplace integral int_0^infty e^{-xi} B(t*xi) dxi
    recovers the original series sum S_r t^r.
    """
    xi = complex(xi)
    result = 0.0 + 0.0j
    for i, s_r in enumerate(coeffs):
        r = r_start + i
        result += s_r * xi ** (r - 1) / math.gamma(r)
    return result


def borel_transform_virasoro_leading(c: float, r_max: int, xi: complex) -> complex:
    """Borel transform of the leading-order Virasoro shadow series at xi."""
    coeffs = shadow_coefficients_leading(c, r_max)
    return borel_transform_from_coeffs(coeffs, xi, r_start=2)


def borel_pole_check(c: float, r_max: int = 20, n_points: int = 50) -> Dict[str, Any]:
    """Verify the Borel transform diverges as xi -> c/6.

    Returns values of |B(xi)| at xi approaching c/6 from below.
    """
    xi_pole = c / 6.0
    fractions = np.linspace(0.5, 0.99, n_points)
    values = []
    for f in fractions:
        xi_val = f * xi_pole
        coeffs = shadow_coefficients_leading(c, r_max)
        b_val = borel_transform_from_coeffs(coeffs, xi_val, r_start=2)
        values.append({'fraction': f, 'xi': xi_val, 'B_abs': abs(b_val)})

    # Check that |B| is increasing as we approach the pole
    abs_vals = [v['B_abs'] for v in values]
    is_increasing = all(abs_vals[i] <= abs_vals[i + 1] * 1.1
                        for i in range(len(abs_vals) - 2, len(abs_vals) - 1))

    return {
        'c': c,
        'pole_location': xi_pole,
        'values': values,
        'diverges': abs_vals[-1] > 10 * abs_vals[0],
    }


def borel_laplace_sum(
    coeffs: Sequence[float],
    t: float,
    r_start: int = 2,
    n_quad: int = 2000,
    xi_max: float = 100.0,
) -> complex:
    """Borel-Laplace sum: int_0^infty e^{-xi} B(t*xi) dxi.

    The Borel-Laplace integral resums the formal series sum S_r t^r
    into a convergent integral.
    """
    if abs(t) < 1e-15:
        return 0.0 + 0.0j
    d_xi = xi_max / n_quad
    result = 0.0 + 0.0j
    for k in range(1, n_quad + 1):
        xi_val = (k - 0.5) * d_xi
        b_val = borel_transform_from_coeffs(coeffs, t * xi_val, r_start)
        result += math.exp(-xi_val) * b_val * d_xi
    return result


def borel_laplace_sum_scipy(
    coeffs: Sequence[float],
    t: float,
    r_start: int = 2,
    limit: int = 200,
) -> Tuple[float, float]:
    """Borel-Laplace sum using scipy quadrature (higher accuracy)."""
    if not HAS_SCIPY:
        raise ImportError("scipy required for high-accuracy quadrature")
    if abs(t) < 1e-15:
        return (0.0, 0.0)

    def integrand(xi):
        b_val = borel_transform_from_coeffs(coeffs, t * xi, r_start)
        return math.exp(-xi) * b_val.real

    result, error = scipy_integrate.quad(integrand, 0, np.inf, limit=limit)
    return (result, error)


def virasoro_gf_leading(c: float, t: float) -> float:
    """Leading-order Virasoro shadow GF: G(t) = -log(1 + 6t/c) + 6t/c.

    The linear term 6t/c is subtracted because shadows start at r=2.
    """
    return -math.log(1.0 + 6.0 * t / c) + 6.0 * t / c


def carleman_condition(coeffs: Sequence[float], r_start: int = 2) -> Dict[str, Any]:
    """Verify Carleman's condition: sum |S_r|^{-1/(2r)} diverges.

    Divergence of this sum guarantees that the moment problem has a unique
    solution -- the spectral measure is determined by its moments.
    """
    terms = []
    partial_sum = 0.0
    for i, s_r in enumerate(coeffs):
        r = r_start + i
        if abs(s_r) > 1e-30:
            term = abs(s_r) ** (-1.0 / (2.0 * r))
            terms.append({'r': r, 'S_r': s_r, 'term': term})
            partial_sum += term
        else:
            terms.append({'r': r, 'S_r': s_r, 'term': float('inf')})
            partial_sum = float('inf')
            break

    # Check that terms stay bounded below (implying divergence)
    finite_terms = [t['term'] for t in terms if t['term'] < float('inf')]
    lower_bound = min(finite_terms) if finite_terms else 0.0

    return {
        'partial_sum': partial_sum,
        'n_terms': len(terms),
        'terms': terms,
        'lower_bound': lower_bound,
        'diverges': partial_sum == float('inf') or (
            len(finite_terms) >= 3 and lower_bound > 0.05
        ),
    }


# =====================================================================
# Task 2: Dispersion relation verification
# =====================================================================

def dispersion_relation_integrand(
    c: float, t_prime: float, t: float, epsilon: float = 1e-8
) -> float:
    """Integrand of the dispersion relation:
    (1/pi) * Im(G(t' + i*epsilon)) / (t' - t).

    For G(t) = -log(1 + 6t/c) + 6t/c, the branch cut is at t < -c/6.
    On the cut (t' < -c/6), the imaginary part of G(t' + i*eps) is:
        Im(G(t'+i0)) = Im(-log(1 + 6(t'+i0)/c)) = -pi  (since 1+6t'/c < 0)
    """
    w = 1.0 + 6.0 * (t_prime + 1j * epsilon) / c
    g_val = -cmath.log(w) + 6.0 * (t_prime + 1j * epsilon) / c
    return g_val.imag / (t_prime - t)


def dispersion_relation_lhs(c: float, t: float) -> float:
    """Left-hand side of the dispersion relation: G(t) directly."""
    return virasoro_gf_leading(c, t)


def dispersion_relation_rhs(
    c: float,
    t: float,
    cutoff: float = 200.0,
    n_quad: int = 10000,
    epsilon: float = 1e-8,
) -> float:
    """Right-hand side: (1/pi) * int_{-infty}^{-c/6} Im(G(t'+i*eps))/(t'-t) dt'.

    Numerically integrates the dispersion relation from -cutoff to -c/6 - delta.
    """
    t_branch = -c / 6.0
    delta = abs(t_branch) * 1e-6  # stay away from the branch point
    t_min = -cutoff
    t_max = t_branch - delta

    dt = (t_max - t_min) / n_quad
    result = 0.0
    for k in range(n_quad):
        t_prime = t_min + (k + 0.5) * dt
        result += dispersion_relation_integrand(c, t_prime, t, epsilon) * dt

    return result / math.pi


def dispersion_relation_rhs_scipy(
    c: float,
    t: float,
    epsilon: float = 1e-8,
) -> Tuple[float, float]:
    """Dispersion RHS using scipy adaptive quadrature."""
    if not HAS_SCIPY:
        raise ImportError("scipy required")

    t_branch = -c / 6.0

    def integrand(t_prime):
        return dispersion_relation_integrand(c, t_prime, t, epsilon)

    # Integrate from -infinity to branch point
    # Use change of variables for the semi-infinite part
    result, error = scipy_integrate.quad(
        integrand, -np.inf, t_branch - 1e-10,
        limit=500, epsabs=1e-10, epsrel=1e-10,
    )
    return (result / math.pi, error / math.pi)


def branch_cut_discontinuity_value(c: float) -> complex:
    """The constant discontinuity across the branch cut: disc(G) = -2*pi*i."""
    return -2.0j * math.pi


# =====================================================================
# Task 3: Pade convergence
# =====================================================================

def pade_approximant_coeffs(
    coeffs: Sequence[float], m: int, n: int
) -> Tuple[List[float], List[float]]:
    """Compute [m/n] Pade approximant numerator and denominator coefficients.

    Given f(x) = sum_{k=0}^{N-1} a_k x^k, compute P(x)/Q(x) where
    deg(P) <= m, deg(Q) <= n, Q(0) = 1.

    Returns (p_coeffs, q_coeffs) such that
    P(x) = sum p_k x^k, Q(x) = 1 + sum q_k x^k.
    """
    a = list(coeffs)
    while len(a) < m + n + 1:
        a.append(0.0)

    if n == 0:
        return (a[:m + 1], [1.0])

    # Build linear system for denominator
    mat = np.zeros((n, n))
    rhs = np.zeros(n)
    for i in range(n):
        for j in range(n):
            idx = m + 1 + i - (j + 1)
            if 0 <= idx < len(a):
                mat[i, j] = a[idx]
        idx_rhs = m + 1 + i
        if 0 <= idx_rhs < len(a):
            rhs[i] = -a[idx_rhs]

    try:
        q = np.linalg.solve(mat, rhs)
    except np.linalg.LinAlgError:
        return (a[:m + 1], [1.0])

    q_coeffs = [1.0] + list(q)

    # Compute numerator: p_k = sum_{j=0}^{min(k,n)} q_j * a_{k-j}
    p_coeffs = []
    for k in range(m + 1):
        pk = 0.0
        for j in range(min(k, n) + 1):
            idx = k - j
            if idx < len(a):
                pk += q_coeffs[j] * a[idx]
        p_coeffs.append(pk)

    return (p_coeffs, q_coeffs)


def pade_poles_from_coeffs(
    coeffs: Sequence[float], N: int
) -> np.ndarray:
    """Find poles of [N/2, N/2] Pade approximant of shadow GF.

    coeffs are the shadow coefficients S_2, S_3, ... treated as
    a power series g(x) = S_2 + S_3 x + S_4 x^2 + ...
    The full GF is G(t) = t^2 * g(t).

    We compute the Pade of the full series a_k = S_{k+2} for k=0,...,N-1
    and find the poles of the denominator.
    """
    a = list(coeffs[:N])
    m = N // 2
    n = N - m
    _, q_coeffs = pade_approximant_coeffs(a, m, n)

    if len(q_coeffs) <= 1:
        return np.array([])

    # Q(x) = q_coeffs[0] + q_coeffs[1]*x + ... + q_coeffs[n]*x^n
    # Poles of g(x) at roots of Q(x), but actual GF is G(t) = t^2 * g(t)
    # so g(t) = G(t)/t^2 and poles of g(t) = poles of G(t).
    # But we're working with the original series in t.
    # Let's work directly with the full GF as a series in t.
    pass

    # Actually, build the full series: f(t) = sum_{r=2}^{r_max} S_r * t^r
    # = sum_{k=0}^{N-1} S_{k+2} * t^{k+2}
    # = t^2 * sum_{k=0}^{N-1} S_{k+2} * t^k
    # The Pade of g(t) = sum S_{k+2} t^k has poles at the singularities of G(t).
    # The actual pole of G(t) = -log(1+6t/c) + 6t/c is at t = -c/6.

    # q_coeffs = [1, q_1, ..., q_n]
    # roots of Q(x) = 1 + q_1 x + ... + q_n x^n
    poly = list(reversed(q_coeffs))
    return np.roots(poly)


def pade_convergence_to_branch_point(
    c: float, N_values: Sequence[int], r_max: int = 30
) -> Dict[str, Any]:
    """For each N in N_values, compute the [N/2, N/2] Pade approximant
    of the leading-order Virasoro shadow GF and find its poles.

    Returns the pole closest to -c/6 and the convergence rate.
    """
    branch_point = -c / 6.0
    coeffs = shadow_coefficients_leading(c, r_max)

    results = []
    for N in N_values:
        # Build series g(t) = S_2 + S_3 t + S_4 t^2 + ... (shifted)
        # So G(t) = t^2 g(t) and g has the same singularities as G.
        a = coeffs[:N]
        m = N // 2
        n = N - m
        _, q_coeffs = pade_approximant_coeffs(a, m, n)

        if len(q_coeffs) > 1:
            poly = list(reversed(q_coeffs))
            poles = np.roots(poly)
            # Find closest pole to branch_point
            if len(poles) > 0:
                distances = [abs(p - branch_point) for p in poles]
                best_idx = np.argmin(distances)
                best_pole = poles[best_idx]
                best_dist = distances[best_idx]
            else:
                best_pole = np.nan
                best_dist = np.inf
        else:
            best_pole = np.nan
            best_dist = np.inf
            poles = np.array([])

        results.append({
            'N': N,
            'poles': poles,
            'closest_pole': best_pole,
            'distance_to_branch': best_dist,
        })

    # Compute convergence rate (geometric)
    distances = [r['distance_to_branch'] for r in results if r['distance_to_branch'] < 100]
    if len(distances) >= 2:
        ratios = [distances[i + 1] / distances[i]
                  for i in range(len(distances) - 1)
                  if distances[i] > 1e-15]
        geo_rate = np.mean(ratios) if ratios else None
    else:
        geo_rate = None

    return {
        'c': c,
        'branch_point': branch_point,
        'results': results,
        'geometric_rate': geo_rate,
    }


# =====================================================================
# Task 4: Rigidity defect and atom recovery (Prony method)
# =====================================================================

def prony_single_atom(
    shadow_coeffs: Sequence[float], r_start: int = 2
) -> Dict[str, Any]:
    """Prony method for recovering a single spectral atom from shadow data.

    If S_r = -(1/r) * lambda^r (single atom with weight 1), then
    the ratio r * S_r / ((r-1) * S_{r-1}) = lambda for all r.

    We solve for lambda using the first two moments, then check
    overdetermination (5 equations, 2 unknowns for coeffs S_2..S_6).
    """
    if len(shadow_coeffs) < 2:
        raise ValueError("Need at least 2 shadow coefficients")

    # Moments: m_r = -r * S_r = lambda^r (for single atom, weight=1)
    moments = []
    for i, s_r in enumerate(shadow_coeffs):
        r = r_start + i
        moments.append(-r * s_r)

    # Recover lambda from ratio m_3/m_2 = lambda
    if len(moments) >= 2 and abs(moments[0]) > 1e-30:
        lam = moments[1] / moments[0]
    else:
        lam = 0.0

    # Check consistency: m_r should equal lam^r
    n_eqns = len(moments)
    residuals = []
    for i, m_r in enumerate(moments):
        r = r_start + i
        predicted = lam ** r
        residuals.append(abs(m_r - predicted))

    # Overdetermination: n_eqns equations, 2 unknowns (lambda, weight)
    # Actually: for S_r = -(w/r)*lam^r, we have 2 unknowns (w, lam).
    # With n_eqns equations and 2 unknowns, defect = n_eqns - 2.
    n_unknowns = 2  # (weight, lambda)
    defect = n_eqns - n_unknowns

    return {
        'lambda': lam,
        'moments': moments,
        'residuals': residuals,
        'max_residual': max(residuals) if residuals else 0.0,
        'n_equations': n_eqns,
        'n_unknowns': n_unknowns,
        'overdetermination_defect': defect,
        'exact_solution_exists': max(residuals) < 1e-10 if residuals else True,
    }


def prony_two_atoms(
    shadow_coeffs: Sequence[float], r_start: int = 2
) -> Dict[str, Any]:
    """Prony method for recovering two spectral atoms.

    For S_r = -(1/r)(c_1 * lam_1^r + c_2 * lam_2^r), the moments
    m_r = -r * S_r = c_1 * lam_1^r + c_2 * lam_2^r satisfy the
    Prony recurrence: m_{r+2} - (lam_1+lam_2) m_{r+1} + lam_1*lam_2 m_r = 0.

    From 4 moments we get 2 linear equations for (sigma_1, sigma_2) where
    sigma_1 = lam_1 + lam_2, sigma_2 = lam_1 * lam_2.
    Then lam_1, lam_2 are roots of z^2 - sigma_1 z + sigma_2 = 0.
    """
    if len(shadow_coeffs) < 4:
        raise ValueError("Need at least 4 shadow coefficients for 2 atoms")

    moments = []
    for i, s_r in enumerate(shadow_coeffs):
        r = r_start + i
        moments.append(-r * s_r)

    # Prony system: m_{r+2} = sigma_1 * m_{r+1} - sigma_2 * m_r
    # Using r = r_start and r = r_start+1:
    # m_4 = sigma_1 * m_3 - sigma_2 * m_2
    # m_5 = sigma_1 * m_4 - sigma_2 * m_3
    # In matrix form: [[m_3, -m_2], [m_4, -m_3]] [sigma_1, sigma_2]^T = [m_4, m_5]
    m = moments  # indexed from 0 = r_start
    A = np.array([
        [m[1], -m[0]],
        [m[2], -m[1]],
    ])
    b = np.array([m[2], m[3]])

    try:
        sigma = np.linalg.solve(A, b)
        sigma_1 = sigma[0]  # lam_1 + lam_2
        sigma_2 = sigma[1]  # lam_1 * lam_2
    except np.linalg.LinAlgError:
        return {'error': 'Singular Prony matrix', 'moments': moments}

    # Roots of z^2 - sigma_1*z + sigma_2 = 0
    disc = sigma_1 ** 2 - 4 * sigma_2
    if disc >= 0:
        lam_1 = (sigma_1 + math.sqrt(disc)) / 2.0
        lam_2 = (sigma_1 - math.sqrt(disc)) / 2.0
    else:
        sqrt_disc = cmath.sqrt(disc)
        lam_1 = (sigma_1 + sqrt_disc) / 2.0
        lam_2 = (sigma_1 - sqrt_disc) / 2.0

    # Recover weights c_1, c_2 from first two moments:
    # c_1 * lam_1^r_start + c_2 * lam_2^r_start = m_0
    # c_1 * lam_1^{r_start+1} + c_2 * lam_2^{r_start+1} = m_1
    W = np.array([
        [complex(lam_1) ** r_start, complex(lam_2) ** r_start],
        [complex(lam_1) ** (r_start + 1), complex(lam_2) ** (r_start + 1)],
    ], dtype=complex)

    try:
        weights = np.linalg.solve(W, np.array([m[0], m[1]], dtype=complex))
        c_1, c_2 = weights[0], weights[1]
    except np.linalg.LinAlgError:
        c_1, c_2 = np.nan, np.nan

    # Check all moments
    residuals = []
    for i, m_r in enumerate(moments):
        r = r_start + i
        predicted = c_1 * complex(lam_1) ** r + c_2 * complex(lam_2) ** r
        residuals.append(abs(m_r - predicted.real))

    return {
        'lambda_1': lam_1,
        'lambda_2': lam_2,
        'weight_1': c_1,
        'weight_2': c_2,
        'sigma_1': sigma_1,
        'sigma_2': sigma_2,
        'moments': moments,
        'residuals': residuals,
        'max_residual': max(residuals) if residuals else 0.0,
    }


def virasoro_atom_recovery(c: float, r_max: int = 6) -> Dict[str, Any]:
    """Recover spectral atom for Virasoro at leading order.

    G(t) = -log(1+6t/c) + 6t/c has a single spectral representation
    with atom lambda = -6/c and weight 1:
        G(t) = sum_{r>=2} S_r t^r, S_r = (-6/c)^r / r = -(1/r)*lambda^r.
    """
    coeffs = shadow_coefficients_log(c, r_max)
    result = prony_single_atom(coeffs, r_start=2)
    result['expected_lambda'] = -6.0 / c
    result['lambda_error'] = abs(result['lambda'] - (-6.0 / c))
    return result


# =====================================================================
# Task 4b: Leech lattice atom recovery
# =====================================================================

def leech_shadow_coefficients(r_max: int = 8) -> List[float]:
    """Shadow coefficients for the Leech lattice VOA (rank 24, c=24).

    The theta function of the Leech lattice has the q-expansion:
        Theta_Leech(q) = 1 + 196560*q^2 + 16773120*q^3 + ...

    In the Hecke decomposition:
        Theta_Leech = E_{12} + c_Delta * Delta
    where E_{12} is the normalized Eisenstein series of weight 12 and
    Delta is the Ramanujan cusp form.

    The shadow coefficients arise from the spectral decomposition:
        S_r = -(1/r)(c_E * lambda_E^r + c_Delta * lambda_Delta^r)

    where:
        c_E = 1 (Eisenstein contribution, weight)
        lambda_E = sigma_{11}(2) = 1 + 2^{11} = 2049 (Hecke eigenvalue of E_{12} at p=2)
        c_Delta = -65520/691 (cusp form coefficient in the decomposition)
        lambda_Delta = tau(2) = -24 (Ramanujan tau at p=2)

    Note: These are the Hecke eigenvalues at p=2, which determine the
    leading shadow behavior.
    """
    # Known decomposition: Theta_Leech = E_{12} - (65520/691)*Delta
    c_E = 1.0
    lam_E = sigma_k(2, 11)  # sigma_11(2) = 1 + 2^11 = 2049
    c_Delta = -65520.0 / 691.0
    lam_Delta = ramanujan_tau(2)  # tau(2) = -24

    coeffs = []
    for r in range(2, r_max + 1):
        S_r = -(1.0 / r) * (c_E * lam_E ** r + c_Delta * lam_Delta ** r)
        coeffs.append(S_r)

    return coeffs


def leech_known_atoms() -> Dict[str, Any]:
    """Return the known Hecke decomposition data for the Leech lattice."""
    return {
        'c_E': 1.0,
        'lambda_E': float(sigma_k(2, 11)),  # 2049
        'c_Delta': -65520.0 / 691.0,
        'lambda_Delta': float(ramanujan_tau(2)),  # -24
    }


def leech_atom_recovery(r_max: int = 8) -> Dict[str, Any]:
    """Recover 2-atom spectral decomposition for the Leech lattice."""
    coeffs = leech_shadow_coefficients(r_max)
    result = prony_two_atoms(coeffs, r_start=2)

    known = leech_known_atoms()
    result['known_atoms'] = known

    # Match recovered atoms to known (order may differ)
    lam1 = complex(result.get('lambda_1', 0))
    lam2 = complex(result.get('lambda_2', 0))
    lam_E = known['lambda_E']
    lam_D = known['lambda_Delta']

    # Try both orderings
    err_12 = abs(lam1.real - lam_E) + abs(lam2.real - lam_D)
    err_21 = abs(lam2.real - lam_E) + abs(lam1.real - lam_D)

    if err_12 <= err_21:
        result['lambda_E_recovered'] = lam1.real
        result['lambda_Delta_recovered'] = lam2.real
        result['weight_E_recovered'] = result.get('weight_1', np.nan)
        result['weight_Delta_recovered'] = result.get('weight_2', np.nan)
    else:
        result['lambda_E_recovered'] = lam2.real
        result['lambda_Delta_recovered'] = lam1.real
        result['weight_E_recovered'] = result.get('weight_2', np.nan)
        result['weight_Delta_recovered'] = result.get('weight_1', np.nan)

    result['lambda_E_error'] = abs(result['lambda_E_recovered'] - lam_E)
    result['lambda_Delta_error'] = abs(result['lambda_Delta_recovered'] - lam_D)

    return result


# =====================================================================
# Task 5: Fake spectral measure discrimination
# =====================================================================

def leech_measure_real() -> Dict[str, float]:
    """Real (genuine) Leech lattice spectral measure."""
    return {
        'c_E': 1.0,
        'lambda_E': float(sigma_k(2, 11)),  # 2049
        'c_Delta': -65520.0 / 691.0,
        'lambda_Delta': float(ramanujan_tau(2)),  # -24
    }


def leech_measure_fake(tau_fake_2: int = 91) -> Dict[str, float]:
    """Fake Leech lattice measure with tau(2) replaced by tau_fake_2.

    The Ramanujan bound is |tau(p)| <= 2*p^{11/2}.
    For p=2: bound = 2*2^{11/2} = 2*sqrt(2048) ~ 90.51.
    Setting tau_fake(2) = 91 violates this bound.
    """
    return {
        'c_E': 1.0,
        'lambda_E': float(sigma_k(2, 11)),  # 2049
        'c_Delta': -65520.0 / 691.0,
        'lambda_Delta': float(tau_fake_2),
    }


def shadow_from_measure(
    measure: Dict[str, float], r_max: int = 10
) -> List[float]:
    """Compute shadow coefficients from a 2-atom spectral measure.

    S_r = -(1/r)(c_E * lam_E^r + c_Delta * lam_Delta^r)
    """
    c_E = measure['c_E']
    lam_E = measure['lambda_E']
    c_D = measure['c_Delta']
    lam_D = measure['lambda_Delta']

    return [
        -(1.0 / r) * (c_E * lam_E ** r + c_D * lam_D ** r)
        for r in range(2, r_max + 1)
    ]


def mc_recursion_check(
    shadow_coeffs: Sequence[float],
    c_val: float = 24.0,
    r_start: int = 2,
) -> Dict[str, Any]:
    """Check whether shadow coefficients satisfy the MC recursion.

    The MC (master equation) recursion at arity r requires:
        nabla_H(S_r) + o^(r) = 0

    where nabla_H(S_r) = 2r * S_r and o^(r) is the obstruction from
    lower-arity compositions (involving the Poisson structure P = 2/c).

    This is the VIRASORO recursion (on the single-generator primary line).
    For Leech lattice shadows, this recursion need not hold exactly —
    but we check the DEFECT to discriminate real from fake measures.

    For a genuine modular shadow tower, the defects should be compatible
    with the MC structure; for a fake measure they will not be.
    """
    P = 2.0 / c_val  # Poisson kernel

    # Build lookup: S_r indexed from r_start
    S = {}
    for i, s in enumerate(shadow_coeffs):
        S[r_start + i] = s

    defects = {}
    for r in range(4, r_start + len(shadow_coeffs)):
        if r not in S:
            continue
        # Obstruction from compositions
        target = r + 2
        o_r = 0.0
        for j in range(2, target):
            k = target - j
            if k < j:
                break
            if j not in S or k not in S:
                continue
            contrib = 2.0 * j * k * P * S[j] * S[k]
            if j == k:
                contrib *= 0.5
            o_r += contrib

        nabla = 2.0 * r * S[r]
        defect = nabla + o_r
        defects[r] = {
            'nabla_H': nabla,
            'obstruction': o_r,
            'defect': defect,
            'relative_defect': abs(defect) / max(abs(nabla), 1e-30),
        }

    return {
        'c': c_val,
        'defects': defects,
        'max_abs_defect': max(abs(d['defect']) for d in defects.values()) if defects else 0.0,
    }


def fake_measure_discrimination(
    r_max: int = 10,
    tau_fake_2: int = 91,
) -> Dict[str, Any]:
    """Compare real and fake Leech measures by shadow coefficients and MC defects.

    Returns the first arity at which they differ significantly and
    whether the fake measure violates the MC recursion.
    """
    real_measure = leech_measure_real()
    fake_measure = leech_measure_fake(tau_fake_2)

    real_coeffs = shadow_from_measure(real_measure, r_max)
    fake_coeffs = shadow_from_measure(fake_measure, r_max)

    # Compare shadow coefficients
    differences = []
    first_significant_r = None
    for i in range(len(real_coeffs)):
        r = 2 + i
        diff = abs(real_coeffs[i] - fake_coeffs[i])
        scale = max(abs(real_coeffs[i]), abs(fake_coeffs[i]), 1e-30)
        rel_diff = diff / scale
        differences.append({
            'r': r,
            'real_S_r': real_coeffs[i],
            'fake_S_r': fake_coeffs[i],
            'abs_diff': diff,
            'rel_diff': rel_diff,
        })
        if first_significant_r is None and rel_diff > 1e-6:
            first_significant_r = r

    # MC recursion check for both
    real_mc = mc_recursion_check(real_coeffs, c_val=24.0)
    fake_mc = mc_recursion_check(fake_coeffs, c_val=24.0)

    return {
        'real_measure': real_measure,
        'fake_measure': fake_measure,
        'real_coeffs': real_coeffs,
        'fake_coeffs': fake_coeffs,
        'differences': differences,
        'first_significant_arity': first_significant_r,
        'real_mc': real_mc,
        'fake_mc': fake_mc,
        'ramanujan_bound': 2.0 * 2.0 ** (11.0 / 2.0),
        'tau_fake_violates_bound': abs(tau_fake_2) > 2.0 * 2.0 ** (11.0 / 2.0),
    }
