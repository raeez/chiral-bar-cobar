r"""Shadow Casimir energy and zeta-function regularization for chiral algebras.

For a chirally Koszul algebra A, the shadow obstruction tower {S_r}_{r>=2}
defines an algebraic analogue of the spectral zeta function:

    zeta_A(s) = sum_{r>=2} S_r(A) * r^{-s}

This is the shadow counterpart of the spectral zeta zeta_M(s) = sum lambda_n^{-s}
for a Laplacian on a manifold M. The shadow coefficients S_r play the role of
spectral data: they encode the arity-graded obstruction content of the bar complex.

SHADOW CASIMIR ENERGY:
    E^{sh}_Cas(A) = -(1/2) * zeta'_A(0) = -(1/2) * sum_{r>=2} S_r * log(r)

For class G (Heisenberg): E_Cas = -(kappa/2) * log(2).
For class L (affine KM): E_Cas = -(kappa/2) * log(2) - (alpha/2) * log(3).
For class M (Virasoro): infinite sum, regularized via analytic continuation
of the shadow generating function H(t) = t^2 * sqrt(Q_L(t)).

SHADOW HEAT KERNEL:
    K_A(t) = sum_{r>=2} S_r * e^{-rt}

Small-t asymptotic expansion: K_A(t) = sum_{k>=0} a_k(A) * t^k, where
    a_k = sum_{r>=2} S_r * (-r)^k / k!
These are the shadow analogues of heat kernel (Seeley-DeWitt) coefficients.

FUNCTIONAL DETERMINANT:
    det'(D_A) = exp(-zeta'_A(0)) = exp(2 * E_Cas)

This is the shadow analogue of the Ray-Singer analytic torsion.

SHADOW CONFORMAL ANOMALY:
    a(A) = zeta_A(-1) = sum_{r>=2} S_r * r     (shadow a-anomaly)
    The c-anomaly comes from zeta'_A(0).

COMPARISON WITH F_1:
    The genus-1 shadow amplitude F_1(A) = kappa(A)/24 (proved for all families).
    The one-loop effective action Gamma^{(1)} = -(1/2) * zeta'_A(0) = E_Cas.
    The ratio E_Cas / F_1 is a universal constant for each shadow class.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    cor:shadow-extraction (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs, I, N as Neval, Rational, S, Symbol, cancel, diff, exp, factor,
    gamma as sym_gamma, log, oo, pi, simplify, solve, sqrt, summation,
    zeta as riemann_zeta, bernoulli, factorial, polylog,
)

c = Symbol('c')
k = Symbol('k')
s = Symbol('s')


# ============================================================================
# 0. Shadow tower data for all standard families
# ============================================================================

def _virasoro_shadow_coeffs(max_r: int = 30) -> Dict[int, Any]:
    """Shadow tower coefficients S_r for Virasoro, symbolic in c.

    Uses the master recurrence from sigma_ring_finite_generation.
    S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)], and the bracket recurrence.
    """
    P = Rational(2) / c
    Sr = {}
    Sr[2] = c / 2
    Sr[3] = Rational(2)
    Sr[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_r + 1):
        o_r = Rational(0)
        for j in range(2, r + 1):
            kk = r + 2 - j
            if kk < 2 or kk > r or kk not in Sr:
                continue
            if j > kk:
                continue
            bracket = j * Sr[j] * P * kk * Sr[kk]
            if j == kk:
                o_r += Rational(1, 2) * bracket
            else:
                o_r += bracket
        Sr[r] = factor(-simplify(o_r) / (2 * r))
    return Sr


def standard_family_shadow_data(family: str, **params) -> Dict[str, Any]:
    """Shadow tower data for a standard family.

    Returns dict with keys: 'class', 'r_max', 'kappa', 'coeffs' (dict r -> S_r).

    Families:
        'heisenberg': params k (level, default 1). Class G, depth 2.
            S_2 = k, S_r = 0 for r >= 3. kappa = k.
        'lattice': params rank (default 1). Class G, depth 2.
            S_2 = rank, S_r = 0 for r >= 3. kappa = rank.
        'free_fermion': Class G, depth 2.
            S_2 = 1/2, S_r = 0 for r >= 3. kappa = 1/2.
        'affine': params dim_g, h_dual, level. Class L, depth 3.
            S_2 = kappa = dim_g * (level + h_dual) / (2 * h_dual).
            S_3 = alpha (Killing 3-cocycle contribution, normalized).
            S_r = 0 for r >= 4.
        'virasoro': params c_val (numeric central charge). Class M, depth inf.
            S_2 = c/2, S_3 = 2, S_4 = 10/(c(5c+22)), recursion for higher.
    """
    if family == 'heisenberg':
        kk = Rational(params.get('k', 1))
        return {
            'class': 'G', 'r_max': 2, 'kappa': kk,
            'coeffs': {2: kk},
        }
    elif family == 'lattice':
        rank = Rational(params.get('rank', 1))
        return {
            'class': 'G', 'r_max': 2, 'kappa': rank,
            'coeffs': {2: rank},
        }
    elif family == 'free_fermion':
        # Convention: complex fermion (c=1, kappa=1/2). For Majorana (c=1/2),
        # use kappa=1/4. AP48: kappa depends on the full algebra.
        return {
            'class': 'G', 'r_max': 2, 'kappa': Rational(1, 2),
            'coeffs': {2: Rational(1, 2)},
        }
    elif family == 'affine':
        dim_g = Rational(params.get('dim_g', 3))  # sl_2 default
        h_dual = Rational(params.get('h_dual', 2))
        level = Rational(params.get('level', 1))
        kappa = dim_g * (level + h_dual) / (2 * h_dual)
        # The cubic shadow alpha for affine KM: normalized Killing 3-cocycle.
        # For sl_2 at level k: alpha = 1 (universal normalization).
        alpha = Rational(params.get('alpha', 1))
        return {
            'class': 'L', 'r_max': 3, 'kappa': kappa,
            'coeffs': {2: kappa, 3: alpha},
        }
    elif family == 'virasoro':
        c_val = params.get('c_val', None)
        max_r = params.get('max_r', 30)
        if c_val is not None:
            c_v = Rational(c_val)
            P = Rational(2) / c_v
            Sr = {}
            Sr[2] = c_v / 2
            Sr[3] = Rational(2)
            Sr[4] = Rational(10) / (c_v * (5 * c_v + 22))
            for r in range(5, max_r + 1):
                o_r = Rational(0)
                for j in range(2, r + 1):
                    kk_idx = r + 2 - j
                    if kk_idx < 2 or kk_idx > r or kk_idx not in Sr:
                        continue
                    if j > kk_idx:
                        continue
                    bracket = j * Sr[j] * P * kk_idx * Sr[kk_idx]
                    if j == kk_idx:
                        o_r += Rational(1, 2) * bracket
                    else:
                        o_r += bracket
                Sr[r] = -o_r / (2 * r)
            return {
                'class': 'M', 'r_max': float('inf'),
                'kappa': c_v / 2, 'coeffs': Sr,
            }
        else:
            # Symbolic
            Sr = _virasoro_shadow_coeffs(max_r)
            return {
                'class': 'M', 'r_max': float('inf'),
                'kappa': c / 2, 'coeffs': Sr,
            }
    else:
        raise ValueError(f"Unknown family: {family}")


# ============================================================================
# 1. Shadow zeta function
# ============================================================================

def shadow_zeta_finite(coeffs: Dict[int, Any], s_val) -> Any:
    """Shadow zeta for finite-depth families (classes G and L).

    zeta_A(s) = sum_{r in coeffs} S_r * r^{-s}

    Exact since the sum is finite.
    """
    result = S.Zero
    for r, Sr in coeffs.items():
        result += Sr * Rational(r) ** (-s_val)
    return result


def shadow_zeta_truncated(coeffs: Dict[int, Any], s_val, max_r: int = None) -> Any:
    """Truncated shadow zeta for class M: sum_{r=2}^{max_r} S_r * r^{-s}.

    For numerical s_val and numerical coefficients, returns a float.
    For symbolic, returns a sympy expression.
    """
    if max_r is None:
        max_r = max(coeffs.keys())
    result = S.Zero
    for r in range(2, max_r + 1):
        if r in coeffs:
            result += coeffs[r] * Rational(r) ** (-s_val)
    return result


def shadow_zeta_numerical(coeffs: Dict[int, Any], s_val: complex,
                          max_r: int = None) -> complex:
    """Numerical shadow zeta evaluation at complex s.

    zeta_A(s) = sum_{r=2}^{max_r} S_r * r^{-s}

    For class M, convergence requires Re(s) large enough that |S_r * r^{-s}| -> 0.
    Since S_r ~ rho^r * r^{-5/2}, convergence requires Re(s) > 0 when rho < 1,
    but the sum ALWAYS has a finite analytic continuation (the GF is algebraic).
    """
    if max_r is None:
        max_r = max(coeffs.keys())
    result = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        if r in coeffs:
            sr = complex(float(coeffs[r]))
            result += sr * (r ** (-s_val))
    return result


# ============================================================================
# 2. Shadow Casimir energy
# ============================================================================

def shadow_casimir_energy(family: str, **params) -> Dict[str, Any]:
    r"""Shadow Casimir energy E^{sh}_Cas(A) = -(1/2) * zeta'_A(0).

    zeta'_A(0) = -sum_{r>=2} S_r * log(r)

    so E_Cas = (1/2) * sum_{r>=2} S_r * log(r).

    For Heisenberg (k=1): E_Cas = (1/2) * 1 * log(2) = log(2)/2.
    For affine sl_2 at k=1: E_Cas = (1/2)(3/2 * log(2) + 1 * log(3)).

    Returns dict with 'E_Cas' (symbolic or numerical), 'zeta_prime_0', etc.
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']
    kappa = data['kappa']

    # Compute zeta'(0) = -sum S_r log(r)
    # and E_Cas = -(1/2) zeta'(0) = (1/2) sum S_r log(r)
    zeta_prime_0 = S.Zero
    E_Cas = S.Zero
    for r, Sr in coeffs.items():
        zeta_prime_0 -= Sr * log(Rational(r))
        E_Cas += Sr * log(Rational(r)) / 2

    # Also compute zeta(0) = sum S_r (formal, needs regularization for class M)
    zeta_0 = S.Zero
    for r, Sr in coeffs.items():
        zeta_0 += Sr

    # F_1 = kappa / 24
    F_1 = kappa / 24

    # For class G/L (few terms), simplify symbolically.
    # For class M (many terms), skip expensive simplification.
    is_finite = data['class'] in ('G', 'L')

    if is_finite:
        E_Cas = simplify(E_Cas)
        zeta_prime_0 = simplify(zeta_prime_0)
        zeta_0 = simplify(zeta_0)

    # Ratio E_Cas / F_1 (if F_1 != 0)
    if F_1 != 0:
        ratio = simplify(E_Cas / F_1) if is_finite else E_Cas / F_1
    else:
        ratio = None

    return {
        'family': family,
        'class': data['class'],
        'kappa': kappa,
        'E_Cas': E_Cas,
        'zeta_prime_0': zeta_prime_0,
        'zeta_0': zeta_0,
        'F_1': F_1,
        'E_Cas_over_F_1': ratio,
        'det_prime': exp(-zeta_prime_0) if is_finite else None,
    }


def shadow_casimir_energy_numerical(family: str, **params) -> Dict[str, float]:
    """Numerical shadow Casimir energy."""
    result = shadow_casimir_energy(family, **params)
    out = {}
    for key in ['E_Cas', 'zeta_prime_0', 'zeta_0', 'F_1']:
        val = result[key]
        try:
            out[key] = float(val.evalf())
        except (AttributeError, TypeError):
            out[key] = float(val)
    out['family'] = result['family']
    out['class'] = result['class']
    if result['E_Cas_over_F_1'] is not None:
        try:
            out['E_Cas_over_F_1'] = float(result['E_Cas_over_F_1'].evalf())
        except (AttributeError, TypeError):
            out['E_Cas_over_F_1'] = float(result['E_Cas_over_F_1'])
    return out


# ============================================================================
# 3. Regularized shadow sum (zeta at s=0)
# ============================================================================

def regularized_shadow_sum(family: str, **params) -> Dict[str, Any]:
    r"""Regularized sum zeta_A(0) = sum_{r>=2} S_r.

    For class G: zeta_A(0) = S_2 = kappa.
    For class L: zeta_A(0) = S_2 + S_3 = kappa + alpha.
    For class M: the formal sum diverges; we regularize via the shadow
    generating function.

    The shadow GF is H(t) = sum_{r>=2} S_r * t^r = t^2 * sqrt(Q_L(t)).
    Setting t = 1: H(1) = sqrt(Q_L(1)) = the regularized sum sum S_r.

    But Q_L(1) = 4*kappa^2 + 12*kappa*alpha + 9*alpha^2 + 16*kappa*S_4
               = (2*kappa + 3*alpha)^2 + 2*Delta

    This gives a finite (possibly complex) regularization even when the
    raw series diverges.
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']
    kappa = data['kappa']

    if data['class'] in ('G', 'L'):
        # Exact finite sum
        reg_sum = S.Zero
        for r, Sr in coeffs.items():
            reg_sum += Sr
        return {
            'family': family,
            'class': data['class'],
            'zeta_0': simplify(reg_sum),
            'method': 'exact_finite_sum',
        }
    else:
        # Class M: use H(1) = sqrt(Q_L(1)) as regularization
        # Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
        # where Delta = 8*kappa*S_4
        S2 = coeffs[2]
        S3 = coeffs.get(3, S.Zero)
        S4 = coeffs.get(4, S.Zero)

        Q_at_1 = (2 * S2 + 3 * S3) ** 2 + 16 * S2 * S4
        H_at_1 = sqrt(Q_at_1)

        # Truncated partial sum for comparison
        trunc_sum = S.Zero
        for r in sorted(coeffs.keys()):
            trunc_sum += coeffs[r]

        return {
            'family': family,
            'class': data['class'],
            'zeta_0_regularized': simplify(H_at_1),
            'Q_L_at_1': simplify(Q_at_1),
            'truncated_sum': simplify(trunc_sum),
            'max_r_truncated': max(coeffs.keys()),
            'method': 'shadow_gf_analytic_continuation',
        }


# ============================================================================
# 4. Shadow heat kernel
# ============================================================================

def shadow_heat_kernel_coefficients(family: str, max_k: int = 20,
                                     **params) -> Dict[int, Any]:
    r"""Heat kernel coefficients a_k of the shadow heat kernel.

    K_A(t) = sum_{r>=2} S_r * e^{-rt} = sum_{k>=0} a_k * t^k

    where a_k = sum_{r>=2} S_r * (-r)^k / k!

    These are the shadow analogues of Seeley-DeWitt coefficients.

    a_0 = sum S_r              (= zeta_A(0), the regularized sum)
    a_1 = -sum r * S_r         (= -zeta_A(-1), the shadow a-anomaly)
    a_2 = sum r^2 * S_r / 2   (related to zeta_A(-2))

    In general: a_k = (-1)^k * zeta_A(-k) / k!
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']

    heat_coeffs = {}
    for kk in range(max_k + 1):
        a_k = S.Zero
        for r, Sr in coeffs.items():
            a_k += Sr * ((-r) ** kk)
        a_k = a_k / factorial(kk)
        heat_coeffs[kk] = simplify(a_k)

    return heat_coeffs


def shadow_heat_kernel_numerical(family: str, t_vals: List[float],
                                  max_r: int = None, **params) -> List[float]:
    r"""Numerical shadow heat kernel K_A(t) at given t values.

    K_A(t) = sum_{r>=2} S_r * exp(-r*t)
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']
    if max_r is None:
        max_r = max(coeffs.keys())

    results = []
    for t in t_vals:
        K = 0.0
        for r in range(2, max_r + 1):
            if r in coeffs:
                sr = float(coeffs[r])
                K += sr * math.exp(-r * t)
        results.append(K)
    return results


def heat_kernel_zeta_consistency(family: str, s_val: float,
                                  t_max: float = 10.0, n_points: int = 1000,
                                  **params) -> Dict[str, float]:
    r"""Verify heat kernel <-> zeta consistency via Mellin transform.

    zeta_A(s) = (1/Gamma(s)) * integral_0^infty K_A(t) * t^{s-1} dt

    We compute both sides numerically and compare.
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']
    max_r = max(coeffs.keys())

    # Direct zeta computation
    zeta_direct = shadow_zeta_numerical(coeffs, s_val, max_r)

    # Mellin transform (numerical integration by trapezoidal rule)
    dt = t_max / n_points
    integral = 0.0
    for i in range(1, n_points + 1):
        t = i * dt
        K = 0.0
        for r in range(2, max_r + 1):
            if r in coeffs:
                sr = float(coeffs[r])
                K += sr * math.exp(-r * t)
        integral += K * (t ** (s_val - 1)) * dt

    gamma_s = math.gamma(s_val)
    zeta_mellin = integral / gamma_s

    return {
        'zeta_direct': zeta_direct.real,
        'zeta_mellin': zeta_mellin,
        'relative_error': abs(zeta_direct.real - zeta_mellin) / (abs(zeta_direct.real) + 1e-30),
    }


# ============================================================================
# 5. Weyl asymptotics (shadow spectral dimension)
# ============================================================================

def shadow_weyl_data(family: str, **params) -> Dict[str, Any]:
    r"""Shadow Weyl law: asymptotic growth of S_r determines spectral dimension.

    For class M: S_r ~ C * rho^r * r^{-5/2} * cos(r*theta + phi).
    The "spectral growth rate" is rho (the shadow radius).
    The "spectral exponent" is -5/2 (universal for algebraic GFs of degree 2).

    The shadow spectral dimension d_sp is defined by analogy with the
    Weyl law N(lambda) ~ lambda^{d/2}: here the cumulative shadow sum
    N_A(R) = sum_{r<=R} |S_r| grows as rho^R * R^{-3/2}, giving
    d_sp = -2 * log(rho) (negative for convergent towers).

    For class G: d_sp = -infinity (only finitely many nonzero S_r).
    For class L: d_sp = -infinity.
    For class C: undefined (stratum separation).
    For class M: d_sp = -2 * log(rho).
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']

    if data['class'] in ('G', 'L'):
        return {
            'family': family,
            'class': data['class'],
            'd_sp': float('-inf'),
            'rho': 0,
            'exponent': None,
            'note': 'Finite tower: no spectral dimension in the Weyl sense',
        }
    elif data['class'] == 'C':
        return {
            'family': family,
            'class': 'C',
            'd_sp': None,
            'rho': None,
            'exponent': None,
            'note': 'Stratum separation: single-line Weyl law undefined',
        }
    else:
        # Class M: compute rho from shadow data
        S2 = coeffs[2]
        S3 = coeffs.get(3, S.Zero)
        S4 = coeffs.get(4, S.Zero)
        Delta = 8 * S2 * S4
        numer_sq = 9 * S3 ** 2 + 2 * Delta
        rho_sq = numer_sq / (4 * S2 ** 2)
        rho_val = float(sqrt(rho_sq).evalf())

        # Observed growth from numerical coefficients
        max_r = max(coeffs.keys())
        observed_ratios = []
        for r in range(3, max_r + 1):
            if r in coeffs and (r - 1) in coeffs:
                sr = float(coeffs[r])
                sr_prev = float(coeffs[r - 1])
                if abs(sr_prev) > 1e-50:
                    observed_ratios.append(abs(sr / sr_prev))

        return {
            'family': family,
            'class': 'M',
            'rho': rho_val,
            'd_sp': -2 * math.log(rho_val) if rho_val > 0 else float('inf'),
            'exponent': -5.0 / 2.0,
            'observed_ratios_tail': observed_ratios[-5:] if observed_ratios else [],
            'predicted_limiting_ratio': rho_val,
        }


# ============================================================================
# 6. Functional determinant (Ray-Singer shadow torsion)
# ============================================================================

def shadow_functional_determinant(family: str, **params) -> Dict[str, Any]:
    r"""Shadow functional determinant det'(D_A) = exp(-zeta'_A(0)).

    This is the shadow analogue of the Ray-Singer analytic torsion.

    det'(D_A) = exp(sum_{r>=2} S_r * log(r))
              = prod_{r>=2} r^{S_r}

    For Heisenberg (k=1): det' = 2^1 = 2.
    For affine sl_2 (k=1): det' = 2^{3/2} * 3^1 = 2*sqrt(2)*3 ~ 8.485.
    For Virasoro: det' = prod r^{S_r} (regularized infinite product).
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']

    # Symbolic: det' = prod r^{S_r}
    log_det = S.Zero
    for r, Sr in coeffs.items():
        log_det += Sr * log(Rational(r))

    is_finite = data['class'] in ('G', 'L')

    if is_finite:
        log_det = simplify(log_det)
        det_prime = simplify(exp(log_det))
        det_prime_num = float(det_prime.evalf())
    else:
        # Class M: compute numerically to avoid sympy timeout on exp(sum of logs)
        det_prime = None
        log_det_num = 0.0
        for r, Sr in coeffs.items():
            log_det_num += float(Sr) * math.log(r)
        det_prime_num = math.exp(log_det_num)

    return {
        'family': family,
        'class': data['class'],
        'log_det': simplify(log_det) if is_finite else log_det,
        'det_prime': det_prime,
        'det_prime_numerical': det_prime_num,
    }


# ============================================================================
# 7. Shadow zeta at Riemann zeros
# ============================================================================

# First 20 nontrivial zeros of the Riemann zeta function (imaginary parts)
RIEMANN_ZEROS = [
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
    67.079810529494173,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
]


def shadow_zeta_at_riemann_zeros(family: str, n_zeros: int = 10,
                                  **params) -> List[Dict[str, Any]]:
    r"""Shadow zeta evaluated at s = rho_n / 2 where rho_n = 1/2 + i*gamma_n.

    For Riemann hypothesis: rho_n = 1/2 + i*gamma_n, so s = rho_n/2 = 1/4 + i*gamma_n/2.

    For class G/L: finite sum at complex exponent (exact).
    For class M: truncated sum (convergent for Virasoro at c > c*).

    We also evaluate at the critical line s = 1/2 + i*t for comparison.
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']
    max_r = max(coeffs.keys())

    results = []
    for n in range(min(n_zeros, len(RIEMANN_ZEROS))):
        gamma_n = RIEMANN_ZEROS[n]
        # s = rho_n / 2 = 1/4 + i * gamma_n / 2
        s_val = 0.25 + 0.5j * gamma_n

        zeta_val = shadow_zeta_numerical(coeffs, s_val, max_r)

        results.append({
            'n': n + 1,
            'gamma_n': gamma_n,
            's': s_val,
            'zeta_A_at_s': zeta_val,
            'abs_zeta': abs(zeta_val),
            'arg_zeta': cmath.phase(zeta_val),
        })

    return results


def shadow_zeta_critical_line(family: str, t_vals: List[float] = None,
                               **params) -> List[Dict[str, Any]]:
    r"""Shadow zeta on the critical line s = 1/2 + i*t.

    For the standard Riemann zeta, the critical line s = 1/2 + it
    is where the zeros lie (RH). We evaluate the shadow zeta here
    for structural comparison.
    """
    if t_vals is None:
        t_vals = [0, 1, 2, 5, 10, 14.13, 21.02, 25.01]

    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']
    max_r = max(coeffs.keys())

    results = []
    for t in t_vals:
        s_val = 0.5 + 1j * t
        zeta_val = shadow_zeta_numerical(coeffs, s_val, max_r)
        results.append({
            't': t,
            's': s_val,
            'zeta_A': zeta_val,
            'abs_zeta': abs(zeta_val),
        })

    return results


# ============================================================================
# 8. Shadow conformal anomaly
# ============================================================================

def shadow_conformal_anomaly(family: str, **params) -> Dict[str, Any]:
    r"""Shadow conformal anomaly coefficients.

    a-anomaly:  a(A) = zeta_A(-1) = sum_{r>=2} S_r * r
    b-anomaly:  b(A) = zeta_A(-2) = sum_{r>=2} S_r * r^2
    c-anomaly:  related to zeta'_A(0) = -2 * E_Cas

    For Heisenberg (k=1):
        a = 1*2 = 2
        b = 1*4 = 4
        c = -2 * E_Cas = -log(2)

    For affine sl_2 (k=1):
        a = (3/2)*2 + 1*3 = 6
        b = (3/2)*4 + 1*9 = 15
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']

    # a-anomaly: zeta_A(-1) = sum S_r * r
    a_anom = S.Zero
    for r, Sr in coeffs.items():
        a_anom += Sr * r

    # b-anomaly: zeta_A(-2) = sum S_r * r^2
    b_anom = S.Zero
    for r, Sr in coeffs.items():
        b_anom += Sr * r ** 2

    is_finite = data['class'] in ('G', 'L')

    # Higher negative integer values
    neg_int_vals = {}
    for n in range(-6, 1):
        val = S.Zero
        for r, Sr in coeffs.items():
            val += Sr * Rational(r) ** (-n)
        neg_int_vals[n] = simplify(val) if is_finite else val

    # c-anomaly from zeta'(0)
    casimir = shadow_casimir_energy(family, **params)

    return {
        'family': family,
        'class': data['class'],
        'a_anomaly': simplify(a_anom) if is_finite else a_anom,
        'b_anomaly': simplify(b_anom) if is_finite else b_anom,
        'c_anomaly': -2 * casimir['E_Cas'],
        'zeta_neg_integers': neg_int_vals,
    }


# ============================================================================
# 9. One-loop effective action and Beilinson-Manin comparison
# ============================================================================

def one_loop_comparison(family: str, **params) -> Dict[str, Any]:
    r"""Compare one-loop effective action with F_1.

    Gamma^{(1)} = (1/2) * log det(D_A) = -(1/2) * zeta'_A(0) = E_Cas

    F_1(A) = kappa(A) / 24

    The ratio E_Cas / F_1 is:
        For Heisenberg: E_Cas = (k/2)*log(2), F_1 = k/24.
            Ratio = 12 * log(2) = 8.3178...
        For affine sl_2 (k=1): E_Cas = (3/4)*log(2) + (1/2)*log(3),
            F_1 = 3/48 = 1/16. Ratio = 12*log(2) + 8*log(3) = 17.11...
        For Virasoro at c=1: truncated approximation.

    The exact relation is that BOTH descend from Theta_A:
        F_1 = kappa * lambda_1^FP    (genus-1 projection of Theta)
        E_Cas = -(1/2) zeta'_A(0)    (regularized arity-graded trace of Theta)

    They measure different projections of the same universal MC element.
    """
    data = standard_family_shadow_data(family, **params)
    is_finite = data['class'] in ('G', 'L')

    if is_finite:
        casimir_data = shadow_casimir_energy(family, **params)
        E_Cas = casimir_data['E_Cas']
        F_1 = casimir_data['F_1']

        result = {
            'family': family,
            'E_Cas': simplify(E_Cas),
            'F_1': F_1,
            'Gamma_1': simplify(E_Cas),
        }

        if F_1 != 0:
            ratio = simplify(E_Cas / F_1)
            result['E_Cas_over_F_1'] = ratio
            try:
                result['E_Cas_over_F_1_numerical'] = float(ratio.evalf())
            except (TypeError, AttributeError):
                result['E_Cas_over_F_1_numerical'] = float(ratio)
    else:
        # Class M: use numerical computation to avoid sympy simplification timeout
        c_val = params.get('c_val')
        max_r = params.get('max_r', 30)
        if c_val is not None:
            num = virasoro_casimir_numerical(c_val, max_r)
            result = {
                'family': family,
                'E_Cas': S(num['E_Cas_truncated']),
                'F_1': S(num['F_1']),
                'Gamma_1': S(num['E_Cas_truncated']),
                'E_Cas_over_F_1': S(num['E_Cas_over_F_1']),
                'E_Cas_over_F_1_numerical': num['E_Cas_over_F_1'],
            }
        else:
            casimir_data = shadow_casimir_energy(family, **params)
            E_Cas = casimir_data['E_Cas']
            F_1 = casimir_data['F_1']
            result = {
                'family': family,
                'E_Cas': E_Cas,
                'F_1': F_1,
                'Gamma_1': E_Cas,
            }
            if F_1 != 0:
                result['E_Cas_over_F_1'] = E_Cas / F_1

    return result


# ============================================================================
# 10. Heisenberg exact results (verification anchor)
# ============================================================================

def heisenberg_exact(kk: int = 1) -> Dict[str, Any]:
    r"""Complete exact results for Heisenberg at level k.

    Heisenberg has S_2 = k, S_r = 0 for r >= 3.
    All shadow zeta invariants are computed in closed form.

    zeta_H(s) = k * 2^{-s}
    zeta_H(0) = k
    zeta'_H(0) = -k * log(2)
    E_Cas = (k/2) * log(2)
    det'(D_H) = 2^k
    K_H(t) = k * e^{-2t}
    a_n = k * (-2)^n / n!
    a-anomaly = 2k
    """
    k_val = Rational(kk)

    return {
        'family': 'heisenberg',
        'level': kk,
        'kappa': k_val,
        'zeta_s': f'{kk} * 2^(-s)',
        'zeta_0': k_val,
        'zeta_prime_0': -k_val * log(2),
        'E_Cas': k_val * log(2) / 2,
        'E_Cas_numerical': float((k_val * log(2) / 2).evalf()),
        'det_prime': 2 ** k_val,
        'F_1': k_val / 24,
        'E_Cas_over_F_1': 12 * log(2),
        'E_Cas_over_F_1_numerical': float((12 * log(2)).evalf()),
        'a_anomaly': 2 * k_val,
        'b_anomaly': 4 * k_val,
        'heat_coeff_0': k_val,
        'heat_coeff_1': -2 * k_val,
        'heat_coeff_2': 2 * k_val,
        'heat_coeff_n': lambda n: k_val * (-2) ** n / factorial(n),
    }


# ============================================================================
# 11. Affine KM exact results
# ============================================================================

def affine_exact(dim_g: int = 3, h_dual: int = 2, level: int = 1,
                 alpha: int = 1) -> Dict[str, Any]:
    r"""Complete exact results for affine V_k(g).

    Affine has S_2 = kappa = dim_g * (k + h^v) / (2*h^v), S_3 = alpha, S_r=0 for r>=4.

    zeta_aff(s) = kappa * 2^{-s} + alpha * 3^{-s}
    zeta_aff(0) = kappa + alpha
    zeta'_aff(0) = -(kappa * log(2) + alpha * log(3))
    E_Cas = (kappa * log(2) + alpha * log(3)) / 2
    det'(D_aff) = 2^kappa * 3^alpha
    a-anomaly = 2*kappa + 3*alpha

    For sl_2 at k=1: dim_g=3, h^v=2, kappa=9/4, alpha=1.
    """
    dim_g_r = Rational(dim_g)
    h_dual_r = Rational(h_dual)
    level_r = Rational(level)
    alpha_r = Rational(alpha)

    kappa = dim_g_r * (level_r + h_dual_r) / (2 * h_dual_r)

    return {
        'family': 'affine',
        'dim_g': dim_g,
        'h_dual': h_dual,
        'level': level,
        'kappa': kappa,
        'alpha': alpha_r,
        'zeta_0': kappa + alpha_r,
        'zeta_prime_0': -(kappa * log(2) + alpha_r * log(3)),
        'E_Cas': (kappa * log(2) + alpha_r * log(3)) / 2,
        'det_prime': 2 ** kappa * 3 ** alpha_r,
        'F_1': kappa / 24,
        'a_anomaly': 2 * kappa + 3 * alpha_r,
        'b_anomaly': 4 * kappa + 9 * alpha_r,
    }


# ============================================================================
# 12. Virasoro numerical results
# ============================================================================

def virasoro_casimir_numerical(c_val, max_r: int = 30) -> Dict[str, float]:
    r"""Numerical shadow Casimir energy for Virasoro at central charge c_val.

    Uses truncated sum through arity max_r. Convergence improves with max_r
    when rho < 1 (c > c* ~ 6.12), and is exact in the limit max_r -> infty.
    For c < c*, the partial sums oscillate and do not converge; the
    regularized value is obtained from the analytic continuation H(1).
    """
    data = standard_family_shadow_data('virasoro', c_val=c_val, max_r=max_r)
    coeffs = data['coeffs']

    kappa = float(data['kappa'])
    F_1 = kappa / 24.0

    # Direct truncated sums
    E_Cas = 0.0
    zeta_0 = 0.0
    a_anom = 0.0
    log_det = 0.0
    for r in range(2, max_r + 1):
        if r in coeffs:
            sr = float(coeffs[r])
            E_Cas += sr * math.log(r) / 2
            zeta_0 += sr
            a_anom += sr * r
            log_det += sr * math.log(r)

    # Regularized zeta(0) via H(1)
    c_v = Rational(c_val)
    S2 = c_v / 2
    S3 = Rational(2)
    S4 = Rational(10) / (c_v * (5 * c_v + 22))
    Q_at_1 = float(((2 * S2 + 3 * S3) ** 2 + 16 * S2 * S4).evalf())
    zeta_0_reg = math.sqrt(abs(Q_at_1))  # |H(1)|

    # Shadow radius for convergence info
    rho_sq = float(((180 * c_v + 872) / ((5 * c_v + 22) * c_v ** 2)).evalf())
    rho = math.sqrt(rho_sq) if rho_sq > 0 else 0.0

    return {
        'c': float(c_val),
        'kappa': kappa,
        'E_Cas_truncated': E_Cas,
        'zeta_0_truncated': zeta_0,
        'zeta_0_regularized': zeta_0_reg,
        'a_anomaly_truncated': a_anom,
        'log_det_truncated': log_det,
        'det_prime_truncated': math.exp(log_det) if abs(log_det) < 700 else float('inf'),
        'F_1': F_1,
        'E_Cas_over_F_1': E_Cas / F_1 if F_1 != 0 else float('inf'),
        'rho': rho,
        'convergent': rho < 1.0,
        'max_r': max_r,
    }


# ============================================================================
# 13. Cross-family comparison table
# ============================================================================

def casimir_comparison_table() -> List[Dict[str, Any]]:
    r"""Cross-family comparison of shadow Casimir energies.

    This table enables cross-family consistency checks (AP10 guard):
    each family's E_Cas / F_1 ratio is independently computable and
    must be consistent with the shadow tower structure.
    """
    table = []

    # Heisenberg at several levels
    for kk in [1, 2, 5, 24]:
        h = heisenberg_exact(kk)
        table.append({
            'family': f'Heisenberg k={kk}',
            'class': 'G',
            'kappa': float(h['kappa']),
            'E_Cas': h['E_Cas_numerical'],
            'F_1': float(h['F_1']),
            'E_Cas_over_F_1': h['E_Cas_over_F_1_numerical'],
            'det_prime': float(h['det_prime']),
        })

    # Affine sl_2 at several levels
    for lev in [1, 2, 10]:
        a = affine_exact(dim_g=3, h_dual=2, level=lev, alpha=1)
        table.append({
            'family': f'Affine sl_2 k={lev}',
            'class': 'L',
            'kappa': float(a['kappa']),
            'E_Cas': float(a['E_Cas'].evalf()),
            'F_1': float(a['F_1']),
            'E_Cas_over_F_1': float((a['E_Cas'] / a['F_1']).evalf()),
            'det_prime': float(a['det_prime'].evalf()),
        })

    # Virasoro at special central charges (convergent regime)
    for c_val in [13, 25, 26]:
        v = virasoro_casimir_numerical(c_val, max_r=15)
        table.append({
            'family': f'Virasoro c={c_val}',
            'class': 'M',
            'kappa': v['kappa'],
            'E_Cas': v['E_Cas_truncated'],
            'F_1': v['F_1'],
            'E_Cas_over_F_1': v['E_Cas_over_F_1'],
            'rho': v['rho'],
        })

    return table


# ============================================================================
# 14. Shadow zeta special values and functional equation probe
# ============================================================================

def shadow_zeta_special_values(family: str, **params) -> Dict[str, Any]:
    r"""Special values of the shadow zeta function.

    zeta_A(n) for n = -6, -5, ..., 0, 1, 2, ..., 6 and n = 1/2.

    For the Riemann zeta, special values at negative integers are
    related to Bernoulli numbers: zeta(-n) = -B_{n+1}/(n+1).
    The shadow zeta has analogous special values determined by the
    shadow tower data, but there is no a priori functional equation
    (the shadow zeta is a finite or algebraic Dirichlet series, not
    an Euler product).
    """
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']

    is_finite = data['class'] in ('G', 'L')

    values = {}
    for n in range(-6, 7):
        val = S.Zero
        for r, Sr in coeffs.items():
            val += Sr * Rational(r) ** (-n)
        values[n] = simplify(val) if is_finite else val

    # Half-integer values
    for half in [Rational(1, 2), Rational(3, 2), Rational(5, 2)]:
        val = S.Zero
        for r, Sr in coeffs.items():
            val += Sr * sqrt(Rational(r)) ** (-2 * half)
        values[f's={half}'] = simplify(val) if is_finite else val

    return {
        'family': family,
        'class': data['class'],
        'special_values': values,
    }


# ============================================================================
# 15. Heat kernel small-t expansion via shadow GF (Path 2 verification)
# ============================================================================

def heat_kernel_from_gf(family: str, max_k: int = 20,
                         **params) -> Dict[int, Any]:
    r"""Heat kernel coefficients from the shadow generating function.

    K_A(t) = sum_{r>=2} S_r * e^{-rt}

    For class G/L, this is just the finite sum.
    For class M, use the GF: H(x) = x^2 * sqrt(Q_L(x)), then
    K_A(t) = integral representation via inverse Laplace.

    Alternative: since a_k = (-1)^k * zeta_A(-k) / k! and
    zeta_A(-k) = sum S_r * r^k = coefficient of x^k in sum S_r * e^{rx}
    evaluated at x=0... But more directly, a_k is just the Taylor
    coefficient, which we compute from the recurrence.

    This provides Path 2 verification against direct computation.
    """
    # Direct computation
    direct = shadow_heat_kernel_coefficients(family, max_k, **params)

    # Verification: a_k = (-1)^k * zeta_A(-k) / k!
    data = standard_family_shadow_data(family, **params)
    coeffs = data['coeffs']

    from_zeta = {}
    for kk in range(max_k + 1):
        zeta_neg_k = S.Zero
        for r, Sr in coeffs.items():
            zeta_neg_k += Sr * Rational(r) ** kk
        from_zeta[kk] = simplify((-1) ** kk * zeta_neg_k / factorial(kk))

    # Check agreement
    agreement = {}
    for kk in range(max_k + 1):
        agreement[kk] = simplify(direct[kk] - from_zeta[kk]) == 0

    return {
        'direct': direct,
        'from_zeta_identity': from_zeta,
        'agreement': agreement,
    }


# ============================================================================
# 16. Koszul duality and Casimir energy
# ============================================================================

def koszul_casimir_comparison(c_val, max_r: int = 30) -> Dict[str, Any]:
    r"""Compare shadow Casimir energies of a Koszul pair.

    For Virasoro: Vir_c <-> Vir_{26-c}.
    E_Cas(A) + E_Cas(A!) is NOT zero in general (unlike kappa + kappa' which
    vanishes for KM but equals 13 for Virasoro by AP24).

    For Heisenberg: H_k <-> H_{-k}. Both have the same |kappa|, so
    E_Cas(H_k) = E_Cas(H_{-k}) = |k|/2 * log(2).
    """
    c_v = Rational(c_val)
    c_dual = 26 - c_v

    E = virasoro_casimir_numerical(c_v, max_r)
    E_dual = virasoro_casimir_numerical(c_dual, max_r)

    return {
        'c': float(c_v),
        'c_dual': float(c_dual),
        'kappa': E['kappa'],
        'kappa_dual': E_dual['kappa'],
        'kappa_sum': E['kappa'] + E_dual['kappa'],  # should be 13 for Virasoro
        'E_Cas': E['E_Cas_truncated'],
        'E_Cas_dual': E_dual['E_Cas_truncated'],
        'E_Cas_sum': E['E_Cas_truncated'] + E_dual['E_Cas_truncated'],
        'rho': E['rho'],
        'rho_dual': E_dual['rho'],
    }


# ============================================================================
# 17. Shadow spectral determinant landscape
# ============================================================================

def spectral_determinant_landscape() -> Dict[str, Dict[str, Any]]:
    r"""Functional determinant landscape for all standard families.

    For class G: det' = 2^kappa (exact).
    For class L: det' = 2^kappa * 3^alpha (exact).
    For class M: det' = prod_{r>=2} r^{S_r} (regularized).
    """
    landscape = {}

    # Class G
    for kk in [1, 2, 24]:
        h = heisenberg_exact(kk)
        landscape[f'Heisenberg k={kk}'] = {
            'class': 'G',
            'det_prime': float(h['det_prime']),
            'log_det': float((h['kappa'] * log(2)).evalf()),
            'exact': True,
        }

    # Class L
    for lev in [1, 2]:
        a = affine_exact(dim_g=3, h_dual=2, level=lev)
        landscape[f'Affine sl_2 k={lev}'] = {
            'class': 'L',
            'det_prime': float(a['det_prime'].evalf()),
            'log_det': float((a['kappa'] * log(2) + log(3)).evalf()),
            'exact': True,
        }

    # Class M (truncated)
    for c_val in [1, 13, 26]:
        v = virasoro_casimir_numerical(c_val, max_r=15)
        landscape[f'Virasoro c={c_val}'] = {
            'class': 'M',
            'det_prime': v['det_prime_truncated'],
            'log_det': v['log_det_truncated'],
            'exact': False,
            'rho': v['rho'],
            'max_r': 30,
        }

    return landscape


if __name__ == '__main__':
    print("=" * 70)
    print("SHADOW CASIMIR ENERGY AND ZETA-FUNCTION REGULARIZATION")
    print("=" * 70)

    # Heisenberg
    h = heisenberg_exact(1)
    print(f"\nHeisenberg k=1:")
    print(f"  E_Cas = (1/2)*log(2) = {h['E_Cas_numerical']:.8f}")
    print(f"  F_1 = 1/24 = {float(h['F_1']):.8f}")
    print(f"  E_Cas/F_1 = 12*log(2) = {h['E_Cas_over_F_1_numerical']:.8f}")
    print(f"  det' = 2^1 = {float(h['det_prime']):.1f}")

    # Affine sl_2
    a = affine_exact(dim_g=3, h_dual=2, level=1)
    print(f"\nAffine sl_2 k=1:")
    print(f"  kappa = {float(a['kappa'])}")
    print(f"  E_Cas = {float(a['E_Cas'].evalf()):.8f}")
    print(f"  det' = {float(a['det_prime'].evalf()):.6f}")

    # Virasoro at c=26
    v = virasoro_casimir_numerical(26, max_r=30)
    print(f"\nVirasoro c=26:")
    print(f"  kappa = {v['kappa']}")
    print(f"  E_Cas (truncated r<=30) = {v['E_Cas_truncated']:.8f}")
    print(f"  F_1 = {v['F_1']:.8f}")
    print(f"  rho = {v['rho']:.6f}")

    # Comparison table
    print("\n" + "=" * 70)
    print("CROSS-FAMILY COMPARISON")
    print("=" * 70)
    table = casimir_comparison_table()
    for row in table:
        print(f"  {row['family']:25s}  kappa={row['kappa']:8.3f}  "
              f"E_Cas={row['E_Cas']:10.6f}  E/F1={row.get('E_Cas_over_F_1', 'N/A'):10s}")
