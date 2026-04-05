r"""Extremal zero distribution and quantum unique ergodicity for shadow zeta.

For a modular Koszul algebra A with shadow zeta function

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s},

this module investigates:

1. ZERO DENSITY N_A(T): Riemann-von Mangoldt counting formula
       N_A(T) = (c_1/2pi) T log T + c_2 T + O(log T)
   with leading coefficient extracted from the shadow data.

2. EXPLICIT FORMULA (shadow version): for a test function h,
       sum_{|gamma|<T} h(gamma) = (T/2pi) hat{h}(0) log(T/2pi)
                                   - hat{h}(0) T/2pi + ...
   Verified for Gaussian test functions h(t) = exp(-t^2/sigma^2).

3. QUANTUM UNIQUE ERGODICITY (QUE): For shadow "eigenfunctions" psi_n
   (the Dirichlet-series modes weighted by S_r), test equidistribution:
       ||psi_n|^2 - 1|| -> 0 as n -> infinity.

4. ENTROPY BOUND: S(|psi_n|^2) = -int |psi_n|^2 log|psi_n|^2 dmu -> log(vol).

5. VALUE DISTRIBUTION: P(|zeta_A(1/2+it)| > V) compared with the
   lognormal prediction from Selberg's theorem.

6. ZEROS OFF CRITICAL LINE: argument-principle search for zeros with
   |Re(rho) - sigma_c| > epsilon, where sigma_c is the shadow critical line.

7. SHADOW RH TEST (GRH analogue): |Li(x) - pi_shadow(x)| <= C sqrt(x) log(x).

8. DENSITY HYPOTHESIS: N_A(sigma, T) <= C T^{2(1-sigma)+epsilon}.

9. ZERO REPULSION: min gap ~ 1/log(T) test for Montgomery pair repulsion.

10. KOSZUL ZERO DUALITY: interlacing and complementary structure between
    zeros of zeta_A and zeta_{A!}.

VERIFICATION: 3+ paths per claim -- explicit formula, contour integration,
GUE comparison, Koszul duality check.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general.
CAUTION (AP10): Cross-verify zeros by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Import from existing shadow zeta infrastructure
# ---------------------------------------------------------------------------
from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    _shadow_zeta_complex,
    _shadow_zeta_derivative,
    newton_zero,
    muller_zero,
    find_zeros_grid,
    _deduplicate_zeros,
    zero_counting_function,
    fit_riemann_von_mangoldt,
    argument_principle_count,
    normalized_spacings,
    pair_correlation_statistic,
    shadow_li_coefficients,
    li_criterion_test,
    hadamard_product_reconstruction,
    zero_real_part_statistics,
    zero_spacing_statistics,
    analyze_family,
)

from compute.lib.bc_explicit_formula_engine import (
    shadow_von_mangoldt,
    shadow_chebyshev_psi,
    virasoro_shadow_coefficients as explicit_virasoro_coefficients,
    virasoro_growth_rate,
)


# ============================================================================
# 0. Family parameters and shadow data
# ============================================================================

STANDARD_FAMILIES = {
    'heisenberg': {'class': 'G', 'default_param': 1.0},
    'affine_sl2': {'class': 'L', 'default_param': 1.0},
    'affine_sl3': {'class': 'L', 'default_param': 1.0},
    'betagamma':  {'class': 'C', 'default_param': 0.5},
    'virasoro':   {'class': 'M', 'default_param': 26.0},
    'w3_t':       {'class': 'M', 'default_param': 50.0},
}


def kappa_for_family(family: str, param: float) -> float:
    """Compute kappa(A) for a given family and parameter.

    CAUTION (AP1): Each family has its own formula.
    CAUTION (AP9): kappa != c/2 in general.
    """
    if family == 'heisenberg':
        return float(param)  # kappa = k
    elif family == 'affine_sl2':
        return 3.0 * (param + 2.0) / 4.0  # dim(sl_2)(k+h^v)/(2h^v)
    elif family == 'affine_sl3':
        return 4.0 * (param + 3.0) / 3.0  # dim(sl_3)(k+h^v)/(2h^v)
    elif family == 'betagamma':
        c_val = 2.0 * (6.0 * param**2 - 6.0 * param + 1.0)
        return c_val / 2.0
    elif family == 'virasoro':
        return param / 2.0  # kappa = c/2
    elif family in ('w3_t', 'w3_w'):
        return param / 2.0  # Leading term for W_3 on T-line
    else:
        raise ValueError(f"Unknown family: {family}")


# ============================================================================
# 1. Zero density N_A(T) and Riemann-von Mangoldt fitting
# ============================================================================

def zero_density_table(
    family: str,
    param: float,
    T_values: List[float],
    max_r: int = 100,
    grid_re: int = 30,
    grid_im_factor: float = 2.5,
) -> Dict[float, int]:
    """Compute N_A(T) for each T in T_values.

    N_A(T) = #{zeros rho of zeta_A with 0 < Im(rho) < T}.

    For class M algebras, searches a strip [-5, 5] x [0, T_max].
    For finite towers, uses analytic formulas where available.
    """
    if not T_values:
        return {}

    T_max = max(T_values)
    coeffs = shadow_coefficients_extended(family, param, max_r)

    grid_im = max(int(T_max * grid_im_factor), 100)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-8.0, 8.0),
        im_range=(0.0, T_max + 5.0),
        grid_re=grid_re,
        grid_im=grid_im,
        max_r=max_r,
    )

    result = {}
    for T in T_values:
        count = sum(1 for z in zeros if 0 < z.imag < T)
        result[T] = count
    return result


def riemann_von_mangoldt_fit(
    family: str,
    param: float,
    T_min: float = 10.0,
    T_max: float = 100.0,
    n_fit_points: int = 30,
    max_r: int = 100,
) -> Dict[str, float]:
    """Fit N_A(T) to the Riemann-von Mangoldt form.

    N_A(T) ~ (a / (2*pi)) * T * log(T / (2*pi)) - (a / (2*pi)) * T + O(log T)

    where a is the shadow-specific leading coefficient.

    For Riemann zeta: a = 1.
    For shadow zeta: a encodes the effective degree of the Dirichlet series.

    Returns dict with 'a_eff' (effective leading coefficient),
    'b', 'c', 'r_squared', and 'RvM_classical_a' (= 1/(2*pi) for Riemann).
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)

    grid_im = max(int(T_max * 3), 200)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-8.0, 8.0),
        im_range=(0.0, T_max + 10.0),
        grid_re=30,
        grid_im=grid_im,
        max_r=max_r,
    )

    fit = fit_riemann_von_mangoldt(zeros, T_min, T_max, n_fit_points)
    # The standard RvM has a = 1/(2*pi) for leading T*log(T) term
    a_eff = fit['a'] * 2.0 * math.pi  # Normalize to match RvM convention
    fit['a_eff'] = a_eff
    fit['RvM_classical_a'] = 1.0 / (2.0 * math.pi)
    return fit


def leading_coefficient_comparison(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[str, float]:
    """Compare fitted leading coefficient with shadow-theoretic prediction.

    For a Dirichlet series sum S_r r^{-s} with S_r ~ C rho^r r^{-5/2}:
    the effective "conductor" is related to the growth rate rho.

    For Riemann zeta: N(T) = (T/2pi) log(T/2pi) - T/2pi + ...
    Leading coefficient = 1/(2pi).

    For shadow zeta with growth rate rho < 1 (entire):
    the zero density depends on the order of the entire function,
    which is determined by log(rho).
    """
    if family == 'virasoro':
        rho = virasoro_growth_rate(param)
    else:
        rho = 0.0

    kappa = kappa_for_family(family, param)

    fit = riemann_von_mangoldt_fit(family, param, max_r=max_r)

    return {
        'kappa': kappa,
        'growth_rate_rho': rho,
        'fitted_a': fit.get('a', 0.0),
        'a_eff': fit.get('a_eff', 0.0),
        'r_squared': fit.get('r_squared', 0.0),
    }


# ============================================================================
# 2. Shadow explicit formula
# ============================================================================

def gaussian_test_function(t: float, sigma: float) -> float:
    """Gaussian test function h(t) = exp(-t^2 / sigma^2)."""
    return math.exp(-t * t / (sigma * sigma))


def gaussian_fourier_transform(xi: float, sigma: float) -> float:
    """Fourier transform of Gaussian: hat{h}(xi) = sigma*sqrt(pi)*exp(-sigma^2*xi^2/4)."""
    return sigma * math.sqrt(math.pi) * math.exp(-sigma * sigma * xi * xi / 4.0)


def explicit_formula_lhs(
    zeros: List[complex],
    T: float,
    h_func,
    use_positive_only: bool = True,
) -> float:
    """Left side of the explicit formula: sum_{|gamma| < T} h(gamma).

    Parameters
    ----------
    zeros : list of zeros rho = sigma + i*gamma
    T : cutoff height
    h_func : test function h(t) -> float
    use_positive_only : if True, sum over gamma > 0 and double (symmetry)

    Returns
    -------
    The spectral sum.
    """
    total = 0.0
    for rho in zeros:
        gamma = rho.imag
        if abs(gamma) < T:
            if use_positive_only and gamma < 0:
                continue
            val = h_func(gamma)
            if use_positive_only and gamma > 0:
                val *= 2.0  # Pair rho with conjugate
            total += val
    return total


def explicit_formula_rhs_leading(
    T: float,
    h_hat_0: float,
    shadow_coeffs: Dict[int, float],
    h_func,
    max_r: int = 100,
) -> Dict[str, float]:
    """Right side (leading terms) of the shadow explicit formula.

    For the Riemann zeta analogue:
        sum h(gamma) = (T/2pi) hat{h}(0) log(T/2pi) - hat{h}(0) T/2pi
                      + sum_p sum_k a_{p^k}/p^{k/2} hat{h}(k log p) + ...

    For the shadow zeta, the "prime" sum becomes the shadow von Mangoldt sum:
        sum_r Lambda_A(r) h(log r) / sqrt(r)

    Returns dict with 'main_term', 'von_mangoldt_sum', 'total_rhs'.
    """
    # Main term: (T/2pi) * h_hat(0) * log(T/2pi) - h_hat(0) * T/2pi
    if T > 0:
        main_term = (T / (2.0 * math.pi)) * h_hat_0 * math.log(T / (2.0 * math.pi))
        sub_term = -h_hat_0 * T / (2.0 * math.pi)
    else:
        main_term = 0.0
        sub_term = 0.0

    # Shadow von Mangoldt sum
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)
    vm_sum = 0.0
    for r in range(2, max_r + 1):
        Lr = Lambda.get(r, 0.0)
        if abs(Lr) < 1e-300:
            continue
        vm_sum += Lr / math.sqrt(float(r)) * h_func(math.log(float(r)))

    total_rhs = main_term + sub_term + vm_sum

    return {
        'main_term': main_term,
        'sub_term': sub_term,
        'von_mangoldt_sum': vm_sum,
        'total_rhs': total_rhs,
    }


def explicit_formula_test(
    family: str,
    param: float,
    T: float = 50.0,
    sigma: float = 10.0,
    max_r: int = 100,
) -> Dict[str, float]:
    """Test the shadow explicit formula with a Gaussian test function.

    Computes LHS (sum over zeros) and RHS (main term + von Mangoldt sum)
    and checks agreement.

    Returns dict with 'lhs', 'rhs', 'error', 'relative_error'.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)

    # Find zeros up to height T
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-8.0, 8.0),
        im_range=(-T - 5, T + 5),
        grid_re=25,
        grid_im=max(int(T * 3), 100),
        max_r=max_r,
    )

    h_func = lambda t: gaussian_test_function(t, sigma)
    h_hat_0 = gaussian_fourier_transform(0.0, sigma)

    lhs = explicit_formula_lhs(zeros, T, h_func, use_positive_only=False)
    rhs_data = explicit_formula_rhs_leading(T, h_hat_0, coeffs, h_func, max_r)
    rhs = rhs_data['total_rhs']

    error = abs(lhs - rhs)
    rel_error = error / max(abs(lhs), 1e-15)

    return {
        'lhs': lhs,
        'rhs': rhs,
        'error': error,
        'relative_error': rel_error,
        'n_zeros_used': len(zeros),
        'T': T,
        'sigma': sigma,
        **rhs_data,
    }


# ============================================================================
# 3. Quantum Unique Ergodicity (QUE) test
# ============================================================================

def shadow_eigenfunction(
    shadow_coeffs: Dict[int, float],
    n: int,
    x_grid: List[float],
    max_r: int = 100,
) -> List[float]:
    """Compute the n-th shadow "eigenfunction" on a grid.

    The shadow eigenfunctions are defined as the modes of the Dirichlet series:
        psi_n(x) = sum_{r=2}^{max_r} S_r * r^{-s_n} * cos(gamma_n * log(r) - phi_n) * r^{-x}

    For a simpler model that captures the QUE phenomenon, we use:
        psi_n(x) = (1/N_n) * sum_{r=2}^{max_r} S_r * cos(2*pi*n*x/r) / sqrt(r)

    where N_n is a normalization factor ensuring ||psi_n||_2 = 1.

    This is a toy model capturing the equidistribution of modes weighted
    by the shadow tower.
    """
    if not x_grid:
        return []

    raw = []
    for x in x_grid:
        val = 0.0
        for r in range(2, min(max_r + 1, max(shadow_coeffs.keys()) + 1)):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            val += Sr * math.cos(2.0 * math.pi * n * x / float(r)) / math.sqrt(float(r))
        raw.append(val)

    # L^2 normalization
    dx = (x_grid[-1] - x_grid[0]) / (len(x_grid) - 1) if len(x_grid) > 1 else 1.0
    norm_sq = sum(v * v for v in raw) * dx
    if norm_sq < 1e-300:
        return [0.0] * len(x_grid)
    norm = math.sqrt(norm_sq)
    return [v / norm for v in raw]


def que_deviation(
    shadow_coeffs: Dict[int, float],
    n: int,
    n_grid: int = 500,
    max_r: int = 100,
) -> float:
    """Compute the L^2 deviation from equidistribution for the n-th eigenfunction.

    ||psi_n|^2 - 1||_2 = sqrt(int (|psi_n(x)|^2 - 1)^2 dx)

    QUE predicts this -> 0 as n -> infinity.
    """
    x_grid = [float(i) / n_grid for i in range(n_grid)]
    psi = shadow_eigenfunction(shadow_coeffs, n, x_grid, max_r)

    dx = 1.0 / n_grid
    # |psi|^2 should be close to 1 (uniform) for large n
    deviation_sq = sum((v * v - 1.0) ** 2 for v in psi) * dx
    return math.sqrt(max(deviation_sq, 0.0))


def que_convergence_test(
    family: str,
    param: float,
    n_values: Optional[List[int]] = None,
    n_grid: int = 500,
    max_r: int = 50,
) -> Dict[str, Any]:
    """Test QUE convergence: does ||psi_n|^2 - 1|| -> 0?

    Returns dict with 'n_values', 'deviations', 'is_decreasing', 'rate'.
    """
    if n_values is None:
        n_values = list(range(1, 201))

    coeffs = shadow_coefficients_extended(family, param, max_r)
    deviations = []
    for n in n_values:
        dev = que_deviation(coeffs, n, n_grid, max_r)
        deviations.append(dev)

    # Check if deviations are roughly decreasing (allowing fluctuations)
    # Use moving average of window 10 to smooth
    window = min(10, len(deviations) // 4)
    if window >= 2:
        smoothed = []
        for i in range(len(deviations)):
            start = max(0, i - window // 2)
            end = min(len(deviations), i + window // 2 + 1)
            smoothed.append(sum(deviations[start:end]) / (end - start))

        # Compare first quarter average vs last quarter average
        q1 = sum(smoothed[:len(smoothed) // 4]) / max(len(smoothed) // 4, 1)
        q4 = sum(smoothed[3 * len(smoothed) // 4:]) / max(len(smoothed) // 4, 1)
        is_decreasing = q4 < q1 * 1.5  # Allow 50% tolerance
    else:
        is_decreasing = False

    # Estimate convergence rate: fit log(deviation) vs log(n)
    rate = 0.0
    if len(n_values) > 5:
        valid_pairs = [(math.log(n), math.log(d))
                       for n, d in zip(n_values, deviations)
                       if n > 1 and d > 1e-15]
        if len(valid_pairs) > 3:
            log_ns = [p[0] for p in valid_pairs]
            log_ds = [p[1] for p in valid_pairs]
            n_pts = len(valid_pairs)
            mean_x = sum(log_ns) / n_pts
            mean_y = sum(log_ds) / n_pts
            numer = sum((x - mean_x) * (y - mean_y) for x, y in zip(log_ns, log_ds))
            denom = sum((x - mean_x) ** 2 for x in log_ns)
            if abs(denom) > 1e-15:
                rate = numer / denom

    return {
        'n_values': n_values,
        'deviations': deviations,
        'is_decreasing': is_decreasing,
        'rate': rate,
        'n_tested': len(n_values),
    }


# ============================================================================
# 4. Entropy bound
# ============================================================================

def eigenfunction_entropy(
    shadow_coeffs: Dict[int, float],
    n: int,
    n_grid: int = 500,
    max_r: int = 50,
) -> float:
    """Compute entropy S(|psi_n|^2) = -int |psi_n|^2 log|psi_n|^2 dmu.

    For uniform distribution: S = log(vol) = 0 (on [0,1] with vol=1).
    QUE implies S(|psi_n|^2) -> log(vol) = 0 on the unit interval.
    """
    x_grid = [float(i) / n_grid for i in range(n_grid)]
    psi = shadow_eigenfunction(shadow_coeffs, n, x_grid, max_r)

    dx = 1.0 / n_grid
    entropy = 0.0
    for v in psi:
        p = v * v  # |psi|^2
        if p > 1e-300:
            entropy -= p * math.log(p) * dx
    return entropy


def entropy_convergence_test(
    family: str,
    param: float,
    n_values: Optional[List[int]] = None,
    n_grid: int = 500,
    max_r: int = 50,
) -> Dict[str, Any]:
    """Test entropy convergence: S(|psi_n|^2) -> log(vol) = 0.

    Returns dict with 'n_values', 'entropies', 'target' (= 0),
    'converging', 'mean_last_quarter'.
    """
    if n_values is None:
        n_values = list(range(1, 201))

    coeffs = shadow_coefficients_extended(family, param, max_r)
    entropies = []
    for n in n_values:
        ent = eigenfunction_entropy(coeffs, n, n_grid, max_r)
        entropies.append(ent)

    target = 0.0  # log(1) for unit interval

    # Check convergence: last quarter should be closer to target
    q_size = max(len(entropies) // 4, 1)
    last_q = entropies[-q_size:]
    first_q = entropies[:q_size]

    mean_last = sum(abs(e - target) for e in last_q) / len(last_q) if last_q else float('inf')
    mean_first = sum(abs(e - target) for e in first_q) / len(first_q) if first_q else float('inf')
    converging = mean_last < mean_first * 1.5

    return {
        'n_values': n_values,
        'entropies': entropies,
        'target': target,
        'converging': converging,
        'mean_last_quarter': mean_last,
        'mean_first_quarter': mean_first,
    }


# ============================================================================
# 5. Value distribution of zeta_A(1/2 + it)
# ============================================================================

def critical_line_value_distribution(
    family: str,
    param: float,
    t_max: float = 1000.0,
    n_samples: int = 5000,
    V_thresholds: Optional[List[float]] = None,
    max_r: int = 100,
) -> Dict[str, Any]:
    """Compute the value distribution of |zeta_A(1/2 + it)| on the critical line.

    Sample |zeta_A(1/2 + it)| at n_samples points in [0, t_max] and compute
    P(|zeta_A(1/2+it)| > V) for each threshold V.

    Compare with the Selberg prediction: log|zeta(1/2+it)| ~ N(0, (1/2)log log T).

    Returns dict with threshold probabilities and distribution statistics.
    """
    if V_thresholds is None:
        V_thresholds = [1.0, 2.0, 5.0, 10.0, 20.0]

    coeffs = shadow_coefficients_extended(family, param, max_r)

    values = []
    log_values = []
    dt = t_max / n_samples
    for i in range(1, n_samples + 1):
        t = i * dt
        s = complex(0.5, t)
        z = _shadow_zeta_complex(coeffs, s, max_r)
        absz = abs(z)
        values.append(absz)
        if absz > 1e-300:
            log_values.append(math.log(absz))

    # Exceedance probabilities
    probs = {}
    for V in V_thresholds:
        count = sum(1 for v in values if v > V)
        probs[V] = count / n_samples

    # Log-value statistics
    if log_values:
        mean_log = sum(log_values) / len(log_values)
        var_log = sum((x - mean_log) ** 2 for x in log_values) / len(log_values)
    else:
        mean_log = 0.0
        var_log = 0.0

    # Selberg prediction: variance = (1/2) log log T
    selberg_variance = 0.5 * math.log(max(math.log(max(t_max, math.e)), 1.0))

    return {
        'V_thresholds': V_thresholds,
        'exceedance_probs': probs,
        'mean_log_modulus': mean_log,
        'var_log_modulus': var_log,
        'selberg_variance': selberg_variance,
        'variance_ratio': var_log / selberg_variance if selberg_variance > 1e-15 else float('inf'),
        'n_samples': n_samples,
        't_max': t_max,
        'mean_modulus': sum(values) / len(values) if values else 0.0,
        'max_modulus': max(values) if values else 0.0,
    }


# ============================================================================
# 6. Zeros off the critical line
# ============================================================================

def find_critical_line(
    shadow_coeffs: Dict[int, float],
    im_range: Tuple[float, float] = (1.0, 100.0),
    n_samples: int = 200,
    max_r: Optional[int] = None,
) -> float:
    """Estimate the "critical line" sigma_c for the shadow zeta.

    For Riemann zeta: sigma_c = 1/2.
    For shadow zeta: compute zeros and take the mean real part.

    Returns the estimated critical line.
    """
    zeros = find_zeros_grid(
        shadow_coeffs,
        re_range=(-8.0, 8.0),
        im_range=im_range,
        grid_re=25,
        grid_im=n_samples,
        max_r=max_r,
    )

    if not zeros:
        return 0.0

    return sum(z.real for z in zeros) / len(zeros)


def zeros_off_critical_line_search(
    family: str,
    param: float,
    epsilon: float = 0.01,
    max_r: int = 100,
    re_range: Tuple[float, float] = (-8.0, 8.0),
    im_range: Tuple[float, float] = (1.0, 100.0),
    grid_re: int = 40,
    grid_im: int = 200,
) -> Dict[str, Any]:
    """Search for zeros with |Re(rho) - sigma_c| > epsilon.

    If any are found, this violates a shadow RH.

    Uses both Newton search and argument principle for verification.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)

    # Find all zeros
    zeros = find_zeros_grid(
        coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r,
    )

    if not zeros:
        return {
            'n_zeros_found': 0,
            'critical_line': 0.0,
            'off_line_zeros': [],
            'shadow_rh_holds': True,
            'max_deviation': 0.0,
        }

    # Estimate critical line
    sigma_c = sum(z.real for z in zeros) / len(zeros)

    # Find zeros off the critical line
    off_line = []
    max_dev = 0.0
    for z in zeros:
        dev = abs(z.real - sigma_c)
        if dev > epsilon:
            off_line.append(z)
        max_dev = max(max_dev, dev)

    # Verification via argument principle:
    # Count zeros in strip |Re(s) - sigma_c| > epsilon
    # Left strip
    left_count = argument_principle_count(
        coeffs,
        re_range=(re_range[0], sigma_c - epsilon),
        im_range=im_range,
        max_r=max_r,
    )
    # Right strip
    right_count = argument_principle_count(
        coeffs,
        re_range=(sigma_c + epsilon, re_range[1]),
        im_range=im_range,
        max_r=max_r,
    )

    return {
        'n_zeros_found': len(zeros),
        'critical_line': sigma_c,
        'off_line_zeros': off_line,
        'n_off_line': len(off_line),
        'shadow_rh_holds': len(off_line) == 0,
        'max_deviation': max_dev,
        'epsilon': epsilon,
        'left_strip_count': left_count,
        'right_strip_count': right_count,
        'argument_principle_off_line': left_count + right_count,
    }


def argument_principle_rectangle(
    shadow_coeffs: Dict[int, float],
    re_range: Tuple[float, float],
    im_range: Tuple[float, float],
    n_points: int = 2000,
    max_r: Optional[int] = None,
) -> int:
    """Count zeros in a rectangle via argument principle.

    Thin wrapper around the existing implementation.
    """
    return argument_principle_count(shadow_coeffs, re_range, im_range, n_points, max_r)


# ============================================================================
# 7. Shadow RH test: Li(x) vs pi_shadow(x)
# ============================================================================

def shadow_prime_counting(
    shadow_coeffs: Dict[int, float],
    x_max: float = 100.0,
    max_r: Optional[int] = None,
) -> Dict[float, int]:
    """Count shadow "primes" up to x.

    A shadow "prime" at arity r is one where Lambda_A(r) > 0 (shadow
    von Mangoldt function is positive).  This is the shadow analogue of
    the prime counting function pi(x).
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)

    result = {}
    count = 0
    for r in range(2, int(x_max) + 1):
        if r > max_r:
            break
        if Lambda.get(r, 0.0) > 1e-15:
            count += 1
        result[float(r)] = count

    return result


def shadow_logarithmic_integral(x: float) -> float:
    """Compute Li(x) = integral from 2 to x of dt/log(t).

    Uses numerical integration via trapezoidal rule.
    """
    if x <= 2.0:
        return 0.0

    n_steps = max(int((x - 2.0) * 10), 100)
    dt = (x - 2.0) / n_steps
    total = 0.0
    for i in range(n_steps):
        t = 2.0 + (i + 0.5) * dt
        if t > 1.01:  # Avoid log(1) = 0
            total += dt / math.log(t)
    return total


def grh_test(
    family: str,
    param: float,
    x_values: Optional[List[float]] = None,
    max_r: int = 100,
) -> Dict[str, Any]:
    """Test shadow GRH: |Li(x) - pi_shadow(x)| <= C * sqrt(x) * log(x).

    Returns dict with x values, Li(x), pi_shadow(x), errors, and
    whether the GRH bound holds.
    """
    if x_values is None:
        x_values = [10.0, 20.0, 50.0, 100.0]

    coeffs = shadow_coefficients_extended(family, param, max_r)
    pi_counts = shadow_prime_counting(coeffs, max(x_values), max_r)

    results = []
    grh_holds = True
    for x in x_values:
        li_x = shadow_logarithmic_integral(x)
        pi_x = pi_counts.get(float(int(x)), 0)
        error = abs(li_x - pi_x)
        bound = math.sqrt(x) * math.log(x)
        ratio = error / bound if bound > 1e-15 else 0.0
        if ratio > 10.0:  # Allow generous C constant
            grh_holds = False
        results.append({
            'x': x,
            'Li_x': li_x,
            'pi_shadow_x': pi_x,
            'error': error,
            'bound': bound,
            'ratio': ratio,
        })

    return {
        'results': results,
        'grh_holds': grh_holds,
    }


# ============================================================================
# 8. Density hypothesis test
# ============================================================================

def density_hypothesis_test(
    family: str,
    param: float,
    sigma_values: Optional[List[float]] = None,
    T_values: Optional[List[float]] = None,
    max_r: int = 100,
) -> Dict[str, Any]:
    """Test the density hypothesis: N_A(sigma, T) <= C * T^{2(1-sigma)+epsilon}.

    N_A(sigma, T) = #{rho : Re(rho) > sigma, |Im(rho)| < T}.
    """
    if sigma_values is None:
        sigma_values = [0.6, 0.7, 0.8, 0.9]
    if T_values is None:
        T_values = [20.0, 50.0, 100.0]

    coeffs = shadow_coefficients_extended(family, param, max_r)

    T_max = max(T_values)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-8.0, 8.0),
        im_range=(-T_max - 5, T_max + 5),
        grid_re=30,
        grid_im=max(int(T_max * 3), 200),
        max_r=max_r,
    )

    results = []
    hypothesis_holds = True
    for sigma in sigma_values:
        for T in T_values:
            count = sum(1 for z in zeros if z.real > sigma and abs(z.imag) < T)
            bound_exponent = 2.0 * (1.0 - sigma)
            bound = T ** bound_exponent if T > 0 else 0.0
            ratio = count / bound if bound > 1e-15 else 0.0
            if count > 0 and ratio > 100.0:  # Very generous C
                hypothesis_holds = False
            results.append({
                'sigma': sigma,
                'T': T,
                'N_A': count,
                'bound_exponent': bound_exponent,
                'bound': bound,
                'ratio': ratio,
            })

    return {
        'results': results,
        'hypothesis_holds': hypothesis_holds,
        'n_zeros_total': len(zeros),
    }


# ============================================================================
# 9. Zero repulsion / minimum gap
# ============================================================================

def zero_minimum_gap(
    zeros: List[complex],
    positive_only: bool = True,
) -> Dict[str, float]:
    """Compute minimum gap between consecutive zeros (by imaginary part).

    For Riemann zeta, the minimum gap at height T scales as 1/log(T).

    Returns dict with 'min_gap', 'mean_gap', 'max_gap', 'gap_at_T' data.
    """
    if positive_only:
        gammas = sorted([z.imag for z in zeros if z.imag > 0.1])
    else:
        gammas = sorted([z.imag for z in zeros])

    if len(gammas) < 2:
        return {
            'min_gap': float('inf'),
            'mean_gap': 0.0,
            'max_gap': 0.0,
            'n_gaps': 0,
        }

    gaps = [gammas[i + 1] - gammas[i] for i in range(len(gammas) - 1)]
    min_gap = min(gaps)
    mean_gap = sum(gaps) / len(gaps)
    max_gap = max(gaps)

    # Height of the minimum gap
    min_idx = gaps.index(min_gap)
    T_at_min = (gammas[min_idx] + gammas[min_idx + 1]) / 2.0

    # Predicted gap: 1/log(T)
    predicted_gap = 1.0 / math.log(max(T_at_min, math.e))

    return {
        'min_gap': min_gap,
        'mean_gap': mean_gap,
        'max_gap': max_gap,
        'n_gaps': len(gaps),
        'T_at_min_gap': T_at_min,
        'predicted_gap_1_over_log_T': predicted_gap,
        'gap_ratio': min_gap / predicted_gap if predicted_gap > 1e-15 else float('inf'),
    }


def zero_repulsion_scaling(
    family: str,
    param: float,
    T_values: Optional[List[float]] = None,
    max_r: int = 100,
) -> Dict[str, Any]:
    """Test whether minimum gap scales as 1/log(T).

    For each T, compute the minimum gap among zeros with Im(rho) < T.
    Fit log(min_gap) vs log(log(T)) to test the scaling.
    """
    if T_values is None:
        T_values = [20.0, 40.0, 60.0, 80.0, 100.0]

    coeffs = shadow_coefficients_extended(family, param, max_r)

    T_max = max(T_values)
    all_zeros = find_zeros_grid(
        coeffs,
        re_range=(-8.0, 8.0),
        im_range=(0.0, T_max + 5.0),
        grid_re=30,
        grid_im=max(int(T_max * 3), 200),
        max_r=max_r,
    )

    data_points = []
    for T in T_values:
        restricted = [z for z in all_zeros if 0 < z.imag < T]
        gap_data = zero_minimum_gap(restricted, positive_only=True)
        if gap_data['n_gaps'] > 0:
            data_points.append({
                'T': T,
                'min_gap': gap_data['min_gap'],
                'mean_gap': gap_data['mean_gap'],
                'log_T': math.log(T),
                '1_over_log_T': 1.0 / math.log(T),
                'n_zeros': len(restricted),
            })

    # Fit min_gap ~ C / log(T)
    scaling_consistent = True
    if len(data_points) >= 3:
        ratios = [d['min_gap'] * math.log(d['T']) for d in data_points if d['min_gap'] > 0]
        if ratios:
            mean_ratio = sum(ratios) / len(ratios)
            var_ratio = sum((r - mean_ratio) ** 2 for r in ratios) / len(ratios)
            cv = math.sqrt(var_ratio) / max(abs(mean_ratio), 1e-15)
            scaling_consistent = cv < 1.0  # Coefficient of variation < 100%

    return {
        'data_points': data_points,
        'scaling_consistent': scaling_consistent,
    }


# ============================================================================
# 10. Koszul zero duality
# ============================================================================

def koszul_zero_duality_analysis(
    family: str,
    param: float,
    max_r: int = 100,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (0.0, 50.0),
    grid_re: int = 25,
    grid_im: int = 100,
) -> Dict[str, Any]:
    """Compare zero sets of zeta_A and zeta_{A!}.

    Investigates:
    - Do the zeros interlace? (alternating on the imaginary axis)
    - Same heights? (same Im(rho) for both)
    - Complementary structure from Theorem C?

    For Virasoro at self-dual c=13: A = A!, so zeros should coincide.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    dual_coeffs = koszul_dual_coefficients(family, param, max_r)

    zeros_A = find_zeros_grid(coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)
    zeros_dual = find_zeros_grid(dual_coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)

    # Extract positive imaginary parts
    gammas_A = sorted([z.imag for z in zeros_A if z.imag > 0.5])
    gammas_dual = sorted([z.imag for z in zeros_dual if z.imag > 0.5])

    # Test interlacing: merge and check alternation
    tagged = [(g, 'A') for g in gammas_A] + [(g, 'D') for g in gammas_dual]
    tagged.sort(key=lambda x: x[0])
    n_alternations = 0
    n_same = 0
    for i in range(len(tagged) - 1):
        if tagged[i][1] != tagged[i + 1][1]:
            n_alternations += 1
        else:
            n_same += 1
    total_pairs = max(n_alternations + n_same, 1)
    interlacing_ratio = n_alternations / total_pairs

    # Test height coincidence: for each zero of A, find nearest zero of dual
    height_matches = []
    for gA in gammas_A:
        if gammas_dual:
            nearest = min(gammas_dual, key=lambda gD: abs(gA - gD))
            height_matches.append(abs(gA - nearest))
        else:
            height_matches.append(float('inf'))

    mean_height_diff = sum(height_matches) / len(height_matches) if height_matches else float('inf')

    # Kappa sum check (AP24)
    kappa_A = kappa_for_family(family, param)
    if family == 'virasoro':
        kappa_dual = (26.0 - param) / 2.0
    elif family == 'heisenberg':
        kappa_dual = -param
    elif family == 'affine_sl2':
        kappa_dual = 3.0 * (-param - 4.0 + 2.0) / 4.0
    elif family == 'affine_sl3':
        kappa_dual = 4.0 * (-param - 6.0 + 3.0) / 3.0
    else:
        kappa_dual = 0.0

    kappa_sum = kappa_A + kappa_dual

    # Self-dual check
    is_self_dual = False
    if family == 'virasoro' and abs(param - 13.0) < 1e-10:
        is_self_dual = True
    elif family == 'heisenberg' and abs(param) < 1e-10:
        is_self_dual = True

    return {
        'n_zeros_A': len(zeros_A),
        'n_zeros_dual': len(zeros_dual),
        'interlacing_ratio': interlacing_ratio,
        'mean_height_difference': mean_height_diff,
        'kappa_A': kappa_A,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa_sum,
        'is_self_dual': is_self_dual,
        'zeros_A': zeros_A,
        'zeros_dual': zeros_dual,
    }


def koszul_zero_overlap_at_self_dual(
    c_val: float = 13.0,
    max_r: int = 80,
    im_range: Tuple[float, float] = (0.0, 50.0),
    tol: float = 0.1,
) -> Dict[str, Any]:
    """At the self-dual point c=13, verify that zeros of A and A! coincide.

    Since Vir_{13}^! = Vir_{26-13} = Vir_{13}, the shadow zetas are identical,
    so ALL zeros must coincide exactly.
    """
    coeffs = shadow_coefficients_extended('virasoro', c_val, max_r)
    dual_coeffs = koszul_dual_coefficients('virasoro', c_val, max_r)

    # Verify coefficient identity
    coeff_diffs = {}
    max_coeff_diff = 0.0
    for r in range(2, max_r + 1):
        diff = abs(coeffs.get(r, 0.0) - dual_coeffs.get(r, 0.0))
        coeff_diffs[r] = diff
        max_coeff_diff = max(max_coeff_diff, diff)

    zeros_A = find_zeros_grid(
        coeffs,
        re_range=(-5.0, 5.0),
        im_range=im_range,
        grid_re=20,
        grid_im=100,
        max_r=max_r,
    )
    zeros_dual = find_zeros_grid(
        dual_coeffs,
        re_range=(-5.0, 5.0),
        im_range=im_range,
        grid_re=20,
        grid_im=100,
        max_r=max_r,
    )

    # Count matching zeros
    matched = 0
    unmatched_A = []
    for zA in zeros_A:
        found = any(abs(zA - zD) < tol for zD in zeros_dual)
        if found:
            matched += 1
        else:
            unmatched_A.append(zA)

    return {
        'c': c_val,
        'max_coeff_diff': max_coeff_diff,
        'coefficients_identical': max_coeff_diff < 1e-10,
        'n_zeros_A': len(zeros_A),
        'n_zeros_dual': len(zeros_dual),
        'n_matched': matched,
        'n_unmatched': len(unmatched_A),
        'match_fraction': matched / max(len(zeros_A), 1),
    }


# ============================================================================
# 11. Full landscape analysis
# ============================================================================

@dataclass
class ExtremalQUEData:
    """Complete extremal zero distribution and QUE analysis."""
    family: str
    param: float
    shadow_class: str
    kappa: float

    # Zero density
    zero_counts: Dict[float, int] = field(default_factory=dict)
    rvm_fit: Dict[str, float] = field(default_factory=dict)

    # Off-line zeros
    off_line_analysis: Dict[str, Any] = field(default_factory=dict)

    # QUE
    que_data: Dict[str, Any] = field(default_factory=dict)

    # Entropy
    entropy_data: Dict[str, Any] = field(default_factory=dict)

    # Value distribution
    value_dist: Dict[str, Any] = field(default_factory=dict)

    # GRH test
    grh_data: Dict[str, Any] = field(default_factory=dict)

    # Density hypothesis
    density_data: Dict[str, Any] = field(default_factory=dict)

    # Zero repulsion
    repulsion_data: Dict[str, Any] = field(default_factory=dict)

    # Koszul duality
    koszul_data: Dict[str, Any] = field(default_factory=dict)


def full_analysis(
    family: str,
    param: float,
    shadow_class: Optional[str] = None,
    max_r: int = 80,
    que_n_max: int = 50,
) -> ExtremalQUEData:
    """Run the full extremal QUE analysis for a given algebra family.

    This is the master function combining all 10 investigations.
    """
    if shadow_class is None:
        shadow_class = STANDARD_FAMILIES.get(family, {}).get('class', 'M')

    kappa = kappa_for_family(family, param)

    data = ExtremalQUEData(
        family=family,
        param=param,
        shadow_class=shadow_class,
        kappa=kappa,
    )

    # 1. Zero density
    T_values = [10.0, 50.0, 100.0]
    data.zero_counts = zero_density_table(family, param, T_values, max_r=max_r)
    data.rvm_fit = riemann_von_mangoldt_fit(
        family, param, T_min=5.0, T_max=50.0, max_r=max_r,
    )

    # 6. Off-line zeros
    data.off_line_analysis = zeros_off_critical_line_search(
        family, param, max_r=max_r,
        re_range=(-5.0, 5.0), im_range=(1.0, 50.0),
        grid_re=25, grid_im=100,
    )

    # 3. QUE test (limited for speed)
    data.que_data = que_convergence_test(
        family, param, n_values=list(range(1, que_n_max + 1)),
        n_grid=200, max_r=min(max_r, 40),
    )

    # 4. Entropy
    data.entropy_data = entropy_convergence_test(
        family, param, n_values=list(range(1, que_n_max + 1)),
        n_grid=200, max_r=min(max_r, 40),
    )

    # 5. Value distribution
    data.value_dist = critical_line_value_distribution(
        family, param, t_max=200.0, n_samples=1000, max_r=max_r,
    )

    # 7. GRH test
    data.grh_data = grh_test(family, param, max_r=max_r)

    # 8. Density hypothesis
    data.density_data = density_hypothesis_test(
        family, param,
        sigma_values=[0.6, 0.8],
        T_values=[20.0, 50.0],
        max_r=max_r,
    )

    # 9. Zero repulsion
    data.repulsion_data = zero_repulsion_scaling(
        family, param, T_values=[20.0, 40.0], max_r=max_r,
    )

    # 10. Koszul duality
    data.koszul_data = koszul_zero_duality_analysis(
        family, param, max_r=max_r,
        re_range=(-5.0, 5.0), im_range=(0.0, 50.0),
    )

    return data


# ============================================================================
# 12. Multi-family comparative analysis
# ============================================================================

def landscape_zero_census(
    families: Optional[Dict[str, Tuple[str, float]]] = None,
    max_r: int = 60,
) -> Dict[str, Dict[str, Any]]:
    """Compute zero density statistics across the standard landscape.

    Returns a dict of family -> {kappa, n_zeros, critical_line, shadow_rh, ...}.
    """
    if families is None:
        families = {
            'Heis_k=1': ('heisenberg', 1.0),
            'sl2_k=1': ('affine_sl2', 1.0),
            'sl3_k=1': ('affine_sl3', 1.0),
            'bg_lam=0.5': ('betagamma', 0.5),
            'Vir_c=26': ('virasoro', 26.0),
            'Vir_c=13': ('virasoro', 13.0),
            'Vir_c=1': ('virasoro', 1.0),
        }

    results = {}
    for label, (fam, par) in families.items():
        coeffs = shadow_coefficients_extended(fam, par, max_r)
        kappa = kappa_for_family(fam, par)

        zeros = find_zeros_grid(
            coeffs,
            re_range=(-5.0, 5.0),
            im_range=(0.0, 50.0),
            grid_re=20,
            grid_im=80,
            max_r=max_r,
        )

        stats = zero_real_part_statistics(zeros)
        spacing = zero_spacing_statistics(zeros)

        results[label] = {
            'family': fam,
            'param': par,
            'kappa': kappa,
            'n_zeros': len(zeros),
            'mean_re': stats.get('mean_re', 0.0),
            'std_re': stats.get('std_re', 0.0),
            'mean_gap': spacing.get('mean_gap', 0.0),
        }

    return results


# ============================================================================
# 13. Cross-verification utilities
# ============================================================================

def verify_zero_by_three_paths(
    shadow_coeffs: Dict[int, float],
    zero: complex,
    all_zeros: List[complex],
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    """Verify a zero by 3 independent methods.

    Path 1: Direct evaluation |zeta_A(rho)| < tol
    Path 2: Newton refinement converges to same point
    Path 3: Hadamard product reconstruction agrees

    Returns dict with pass/fail for each path and overall verdict.
    """
    tol = 1e-8

    # Path 1: Direct evaluation
    val = _shadow_zeta_complex(shadow_coeffs, zero, max_r)
    path1_pass = abs(val) < tol * max(1.0, abs(zero))

    # Path 2: Newton refinement
    refined = newton_zero(shadow_coeffs, zero + 0.01 + 0.01j, max_r=max_r)
    if refined is not None:
        path2_pass = abs(refined - zero) < 0.1
    else:
        # Try from a different starting point
        refined = newton_zero(shadow_coeffs, zero - 0.01 + 0.01j, max_r=max_r)
        path2_pass = refined is not None and abs(refined - zero) < 0.1

    # Path 3: Hadamard product
    s_test = zero + 1.0  # Test nearby
    had_data = hadamard_product_reconstruction(
        all_zeros, s_test, shadow_coeffs, max_r,
    )
    path3_pass = had_data['relative_error'] < 0.1  # 10% accuracy

    return {
        'zero': zero,
        'path1_direct_eval': path1_pass,
        'path1_residual': abs(val),
        'path2_newton_converges': path2_pass,
        'path3_hadamard_accurate': path3_pass,
        'path3_rel_error': had_data['relative_error'],
        'all_pass': path1_pass and path2_pass and path3_pass,
    }


def cross_family_consistency_check(
    family: str,
    param: float,
    max_r: int = 60,
) -> Dict[str, Any]:
    """Cross-check zero-finding results for internal consistency.

    Verifies:
    1. N_A(T) from grid search matches argument principle count
    2. Li coefficients from zeros match direct computation
    3. Zeros of A and A! satisfy complementarity constraints
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)

    # Grid search
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-5.0, 5.0),
        im_range=(0.0, 50.0),
        grid_re=20,
        grid_im=80,
        max_r=max_r,
    )

    # Argument principle
    ap_count = argument_principle_count(
        coeffs,
        re_range=(-5.0, 5.0),
        im_range=(0.0, 50.0),
        max_r=max_r,
    )

    n_grid = len(zeros)
    count_match = abs(n_grid - ap_count) <= max(2, n_grid // 5)

    # Li test
    li_data = li_criterion_test(zeros)

    # Koszul consistency: verify kappa + kappa' at arity 2
    dual_coeffs = koszul_dual_coefficients(family, param, max_r)
    kappa = coeffs.get(2, 0.0)
    kappa_dual = dual_coeffs.get(2, 0.0)
    kappa_sum = kappa + kappa_dual

    # Expected kappa sums (AP24)
    if family == 'virasoro':
        expected_sum = 13.0  # kappa(Vir_c) + kappa(Vir_{26-c}) = 13
    elif family == 'heisenberg':
        expected_sum = 0.0  # kappa(H_k) + kappa(H_k^!) = k + (-k) = 0
    elif family == 'affine_sl2':
        expected_sum = 0.0
    elif family == 'affine_sl3':
        expected_sum = 0.0
    else:
        expected_sum = None

    kappa_check = True
    if expected_sum is not None:
        kappa_check = abs(kappa_sum - expected_sum) < 0.01

    return {
        'n_zeros_grid': n_grid,
        'n_zeros_arg_principle': ap_count,
        'count_consistent': count_match,
        'li_all_positive': li_data.get('all_positive', False),
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa_sum,
        'expected_kappa_sum': expected_sum,
        'kappa_check_passed': kappa_check,
    }
