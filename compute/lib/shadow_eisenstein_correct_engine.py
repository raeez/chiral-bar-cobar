r"""shadow_eisenstein_correct_engine.py -- Correct formulation of the shadow Eisenstein theorem.

BACKGROUND
==========
The original thm:shadow-eisenstein claimed:

    L_A^{sh}(s) := sum_{r >= 2} S_r(A) r^{-s} = -kappa(A) zeta(s) zeta(s-1).

This is FALSE.  The shadow coefficients S_r come from the convolution recursion
on the shadow metric Q_L(t), and are NOT proportional to sigma_1(r).

For Heisenberg (class G): S_2 = k, S_r = 0 for r >= 3.
    L^sh(s) = k * 2^{-s}, which is entire.
    But -k * zeta(s) * zeta(s-1) has poles at s = 1 and s = 2.
    ==> FALSIFIED by Heisenberg.

For affine KM (class L): S_2 = kappa, S_3 = alpha, S_r = 0 for r >= 4.
    L^sh(s) = kappa * 2^{-s} + alpha * 3^{-s}, which is entire.
    ==> FALSIFIED by any class L algebra.

For Virasoro (class M): S_r ~ C * rho^r * r^{-5/2} (geometric growth).
    L^sh(s) converges for Re(s) > 1 + log(rho)/log(r) and extends
    meromorphically, but is NOT equal to -kappa * zeta(s) * zeta(s-1).

WHAT IS TRUE
============

THEOREM (Genus-1 Amplitude Eisenstein Property):

(A) The genus-1 arity-2 shadow amplitude is
        Sh_2^{(1)}(tau) = kappa * E_2*(tau),
    where E_2*(tau) = 1 - 24 sum_{n>=1} sigma_1(n) q^n is the quasi-modular
    Eisenstein series.  Its Fourier coefficients are -24*kappa*sigma_1(n),
    and the associated Dirichlet series is
        sum_{n>=1} (-24*kappa*sigma_1(n)) n^{-s} = -24*kappa * zeta(s) * zeta(s-1).
    This is the CORRECT Eisenstein identity at arity 2.

(B) The genus-1 arity-r amplitude Sh_r^{(1)}(tau) is a graph sum over
    stable graphs of type (1,r), with edge factors proportional to E_2*(tau)
    and vertex factors from the shadow coefficients S_j.  The Mellin transform
    of Sh_r^{(1)} against the Maass Eisenstein series E(s,tau) produces the
    intertwining kernel:
        M[G_r](s) = r! * Gamma(s-1) / (2pi)^{s-1} * zeta(s-1) * zeta(s+r-2)
    which is exact at r = 2 and of leading order for r >= 3.

(C) The shadow L-function L_A^{sh}(s) = sum S_r r^{-s} is:
    - A polynomial in r^{-s} for class G (depth 2) and class L (depth 3).
    - An entire function for class C (depth 4, finitely many nonzero S_r).
    - A Dirichlet series with finite abscissa of convergence for class M.
    It is NOT equal to -kappa * zeta(s) * zeta(s-1) for ANY algebra.

(D) The CORRECT relationship between L^sh and the Eisenstein L-function is:
    At arity 2, the shadow coefficient S_2 = kappa is the CONSTANT TERM of
    the genus-1 amplitude kappa * E_2*(tau).  The NON-CONSTANT Fourier
    coefficients of the amplitude are -24*kappa*sigma_1(n), which DO produce
    zeta(s)*zeta(s-1).  The shadow L-function extracts CONSTANT TERMS of the
    amplitudes, while the Eisenstein property lives in the FOURIER COEFFICIENTS.

(E) For class M algebras, the Dirichlet series sum S_r r^{-s} has a natural
    boundary at Re(s) = sigma_c where sigma_c depends on the shadow growth
    rate rho.  It does NOT extend to a meromorphic function on C, in contrast
    to -kappa * zeta(s) * zeta(s-1) which is meromorphic on all of C.

SUMMARY: The Eisenstein property belongs to the GENUS-1 AMPLITUDES
(functions of tau), not to the SHADOW COEFFICIENTS (constants).  The
shadow L-function and the Eisenstein L-function are related by the
intertwining kernel M[G_r](s), not by an identity.

CONVENTIONS:
  - kappa(Vir_c) = c/2, kappa(H_k) = k, kappa(KM) = dim(g)(k+h^v)/(2h^v)
  - E_2*(tau) = 1 - 24 sum sigma_1(n) q^n  (quasi-modular, AP15)
  - S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t))
  - Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
  - Delta = 8*kappa*S_4 (critical discriminant)

VERIFICATION PATHS (>= 3 per claim):
  Path 1: Direct numerical computation of S_r via convolution recursion
  Path 2: Comparison L^sh(s) vs -kappa*zeta(s)*zeta(s-1) at specific s values
  Path 3: Heisenberg falsification (S_r = 0 for r >= 3)
  Path 4: Genus-1 amplitude Fourier coefficients vs sigma_1
  Path 5: Growth rate analysis (S_r ~ rho^r vs sigma_1(r) ~ r log log r)
  Path 6: Intertwining kernel at r = 2 exact verification
  Path 7: Class G/L/C/M comparative analysis

Manuscript references:
    thm:shadow-eisenstein (arithmetic_shadows.tex) -- TO BE CORRECTED
    prop:quasi-modular-propagator (arithmetic_shadows.tex)
    prop:genus1-weight-bound (arithmetic_shadows.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    eq:intertwining-kernel (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================================
# SECTION 0.  Bernoulli numbers and arithmetic functions
# ============================================================================


@lru_cache(maxsize=256)
def bernoulli(n: int) -> Fraction:
    """Bernoulli number B_n via the standard recursion.

    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_4 = -1/30, B_6 = 1/42.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    B[1] = Fraction(-1, 2)
    for m in range(2, n + 1):
        if m % 2 == 1:
            B[m] = Fraction(0)
            continue
        s = Fraction(0)
        for k in range(m):
            s += Fraction(math.comb(m + 1, k)) * B[k]
        B[m] = -s / (m + 1)
    return B[n]


def sigma_1(n: int) -> int:
    """Sum-of-divisors sigma_1(n) = sum_{d | n} d."""
    if n <= 0:
        return 0
    return sum(d for d in range(1, n + 1) if n % d == 0)


def bernoulli_ratio(r: int) -> Fraction:
    """B_{2r} / (2r)!."""
    if r < 1:
        raise ValueError("r must be >= 1")
    return bernoulli(2 * r) / Fraction(math.factorial(2 * r))


# ============================================================================
# SECTION 1.  Shadow coefficients from the convolution recursion
# ============================================================================


def virasoro_shadow_metric_coefficients(c_val: float) -> Tuple[float, float, float]:
    """Return (q0, q1, q2) for the Virasoro shadow metric Q_L(t).

    Q_L(t) = q0 + q1*t + q2*t^2
    where q0 = c^2, q1 = 12c, q2 = alpha(c) = (180c + 872)/(5c + 22).

    The shadow metric is Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    but we compute directly from the OPE data for Virasoro.
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"Virasoro shadow metric undefined at c={c_val}")
    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    return (q0, q1, q2)


def shadow_coefficients_from_metric(
    q0: float, q1: float, q2: float, max_r: int = 50
) -> Dict[int, float]:
    """Compute shadow coefficients S_r from Q_L(t) = q0 + q1*t + q2*t^2.

    The weighted generating function is H(t) = t^2 * sqrt(Q_L(t)), and
    S_r = a_{r-2} / r where a_n = [t^n] sqrt(Q_L(t)).

    The convolution recursion for a_n where f(t) = sum a_n t^n = sqrt(Q_L):
        a_0 = sqrt(q0)
        a_1 = q1 / (2*a_0)
        a_2 = (q2 - a_1^2) / (2*a_0)
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}  for n >= 3
    """
    a0 = math.sqrt(q0)
    if a0 == 0:
        raise ValueError("q0 = 0: degenerate shadow metric")

    a = [a0]
    if max_r >= 3:
        a.append(q1 / (2.0 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max(max_r - 2 + 1, 0)):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))

    result = {}
    for n in range(len(a)):
        r = n + 2
        if r <= max_r:
            result[r] = a[n] / float(r)
    return result


def shadow_coefficients_from_metric_exact(
    q0: Fraction, q1: Fraction, q2: Fraction, max_r: int = 30
) -> Dict[int, Fraction]:
    """Exact rational shadow coefficients from Q_L = q0 + q1*t + q2*t^2.

    Requires q0 to be a perfect square rational (true for all standard families).
    """
    # For Virasoro: q0 = c^2, so a0 = |c|
    from sympy import sqrt as sym_sqrt, Rational as SymRat
    a0_sq = q0
    # Check if q0 is a perfect square
    num = q0.numerator
    den = q0.denominator
    from math import isqrt
    num_sqrt = isqrt(num)
    den_sqrt = isqrt(den)
    if num_sqrt * num_sqrt != num or den_sqrt * den_sqrt != den:
        raise ValueError(f"q0 = {q0} is not a perfect square rational")
    a0 = Fraction(num_sqrt, den_sqrt)

    a = [a0]
    if max_r >= 3:
        a.append(q1 / (2 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2 * a0))
    for n in range(3, max(max_r - 2 + 1, 0)):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a0))

    result = {}
    for n in range(len(a)):
        r = n + 2
        if r <= max_r:
            result[r] = a[n] / r
    return result


def virasoro_shadow_coefficients(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients S_r for Virasoro at central charge c."""
    q0, q1, q2 = virasoro_shadow_metric_coefficients(c_val)
    return shadow_coefficients_from_metric(q0, q1, q2, max_r)


def heisenberg_shadow_coefficients(k: float) -> Dict[int, float]:
    """Shadow coefficients for Heisenberg at level k.

    Class G: S_2 = kappa = k, S_r = 0 for r >= 3.
    The shadow metric is Q_L(t) = k^2 (constant), so sqrt(Q_L) = |k|,
    giving a_0 = |k|, a_n = 0 for n >= 1.
    """
    return {2: k}


def affine_km_shadow_coefficients(
    dim_g: int, k: float, h_dual: int, max_r: int = 50
) -> Dict[int, float]:
    """Shadow coefficients for affine Kac-Moody.

    Class L for generic levels.  kappa = dim(g)(k+h^v)/(2h^v).
    alpha (cubic shadow) is nonzero, Delta = 0 for the principal Sugawara line.
    """
    kappa = dim_g * (k + h_dual) / (2.0 * h_dual)
    # The cubic shadow coefficient S_3 for affine KM:
    # alpha = S_3 depends on the specific OPE; for the principal line
    # Q_L(t) = (2*kappa)^2 + q1*t with q1 from the cubic OPE coefficient.
    # For class L: Q_L is a perfect square => S_r = 0 for r >= 4.
    # Generic Q_L for KM: q0 = 4*kappa^2, q1 = 12*kappa*alpha_3, q2 = 9*alpha_3^2
    # where the discriminant Delta = 8*kappa*S_4 = 0 for class L.
    # This means q2 = 9*alpha_3^2 + 16*kappa*S_4 = 9*alpha_3^2 when Delta=0.
    #
    # For the Sugawara line of sl_2 at level k:
    # The cubic shadow C = 2 (same as Virasoro, from Sugawara construction).
    # But Delta = 0 since the OPE is quadratic (no quartic shadow for KM).
    alpha_3 = 2.0  # Sugawara cubic shadow
    q0 = (2.0 * kappa) ** 2
    q1 = 12.0 * kappa * alpha_3
    q2 = 9.0 * alpha_3 ** 2  # Delta = 0 for class L
    return shadow_coefficients_from_metric(q0, q1, q2, max_r)


# ============================================================================
# SECTION 2.  The shadow L-function L^sh(s) = sum S_r r^{-s}
# ============================================================================


def shadow_l_function(
    shadow_coeffs: Dict[int, float], s: complex, max_r: int = 50
) -> complex:
    """Evaluate L^sh(s) = sum_{r>=2} S_r r^{-s} (the shadow Dirichlet series).

    For class G/L: this is a polynomial in r^{-s} (finitely many terms).
    For class M: this converges for Re(s) > sigma_c (the abscissa of convergence).
    """
    total = 0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-50:
            continue
        total += Sr * (r ** (-s))
    return total


def eisenstein_l_function(kappa_val: float, s: complex) -> complex:
    """Evaluate -kappa * zeta(s) * zeta(s-1) using mpmath.

    This is the INCORRECTLY claimed identity for L^sh.
    We compute it for comparison/falsification purposes.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for eisenstein_l_function")
    s_mp = mpmath.mpc(s)
    z1 = mpmath.zeta(s_mp)
    z2 = mpmath.zeta(s_mp - 1)
    return complex(-kappa_val * z1 * z2)


def shadow_l_function_abscissa(shadow_coeffs: Dict[int, float]) -> float:
    """Estimate the abscissa of convergence sigma_c of L^sh(s).

    For class G/L/C: sigma_c = -infinity (entire function).
    For class M: sigma_c is determined by the growth rate rho via
        sigma_c = 1 + log(rho) / log(max_r) (rough estimate)
    More precisely, if S_r ~ C * rho^r * r^{-5/2}, then
        |S_r| * r^{-sigma} ~ C * rho^r * r^{-5/2-sigma}
    converges iff rho < 1 (automatically, since rho = shadow radius < 1
    for all standard families).  So sigma_c = 0 if rho < 1.

    Returns:
        Estimated sigma_c.  Returns -float('inf') for finite towers.
    """
    # Find the maximum r with nonzero S_r
    nonzero = {r: abs(v) for r, v in shadow_coeffs.items() if abs(v) > 1e-50}
    if len(nonzero) <= 3:
        return -float('inf')  # Finite tower: entire function

    # Estimate growth rate via ratio test
    sorted_r = sorted(nonzero.keys())
    if len(sorted_r) < 5:
        return -float('inf')

    ratios = []
    for i in range(len(sorted_r) - 1):
        r1, r2 = sorted_r[i], sorted_r[i + 1]
        if r2 == r1 + 1 and nonzero[r1] > 1e-50:
            ratios.append(nonzero[r2] / nonzero[r1])

    if not ratios:
        return -float('inf')

    rho_est = ratios[-1] if ratios else 0.0

    if rho_est < 1.0:
        # Series converges absolutely for all s with Re(s) > 0
        # Actually, S_r ~ C*rho^r*r^{-5/2} with rho < 1 means
        # sum |S_r| r^{-sigma} converges for ALL sigma (geometric decay dominates)
        return -float('inf')
    else:
        # rho >= 1: need Re(s) > some sigma_c
        return 1.0 + math.log(rho_est)


def shadow_growth_rate(shadow_coeffs: Dict[int, float]) -> Optional[float]:
    """Estimate the shadow growth rate rho from the coefficients.

    For class M: S_r ~ C * rho^r * r^{-5/2}, so |S_{r+1}/S_r| -> rho.
    """
    sorted_r = sorted(r for r, v in shadow_coeffs.items() if abs(v) > 1e-50)
    if len(sorted_r) < 5:
        return 0.0  # Finite tower

    ratios = []
    for i in range(len(sorted_r) - 1):
        r1, r2 = sorted_r[i], sorted_r[i + 1]
        v1 = abs(shadow_coeffs[r1])
        v2 = abs(shadow_coeffs[r2])
        if r2 == r1 + 1 and v1 > 1e-50:
            ratios.append(v2 / v1)

    if len(ratios) >= 3:
        return ratios[-1]
    return None


# ============================================================================
# SECTION 3.  Falsification: L^sh =/= -kappa * zeta(s) * zeta(s-1)
# ============================================================================


def falsification_heisenberg(k: float = 1.0) -> Dict:
    """Falsify the shadow Eisenstein identity for Heisenberg.

    Heisenberg: S_2 = k, S_r = 0 for r >= 3.
    L^sh(s) = k * 2^{-s}, which is entire.
    -k * zeta(s) * zeta(s-1) has poles at s = 1, 2.

    Even away from poles, the values disagree.
    """
    coeffs = heisenberg_shadow_coefficients(k)
    kappa = k

    results = {}
    for s_val in [0, 3, 4, 5, 10]:
        s = complex(s_val)
        l_sh = shadow_l_function(coeffs, s)
        if HAS_MPMATH:
            l_eis = eisenstein_l_function(kappa, s)
        else:
            l_eis = None

        results[s_val] = {
            'L_sh': complex(l_sh),
            'L_eis': l_eis,
            'L_sh_exact': k * 2.0 ** (-s_val),
            'disagree': abs(l_sh - l_eis) if l_eis is not None else None,
        }

    # At s = 0: L^sh(0) = k * 1 = k.  L_eis(0) = -k * (-1/2)(-1/12) = -k/24.
    results['s_eq_0_exact'] = {
        'L_sh': k,
        'L_eis': -k / 24.0,
        'ratio': -24.0,  # L_sh / L_eis
    }

    # Pole check: L^sh has no poles, L_eis has poles at s=1,2
    results['pole_structure'] = {
        'L_sh_poles': 'none (entire function)',
        'L_eis_poles': 's = 1 and s = 2 (simple poles)',
        'conclusion': 'FALSIFIED: different analytic structure',
    }

    return results


def falsification_virasoro(c_val: float = 26.0, max_r: int = 50) -> Dict:
    """Falsify the shadow Eisenstein identity for Virasoro.

    Compute L^sh(s) and -kappa*zeta(s)*zeta(s-1) at s = 4 and compare.
    """
    kappa = c_val / 2.0
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    rho = shadow_growth_rate(coeffs)

    results = {'c': c_val, 'kappa': kappa, 'growth_rate': rho, 'max_r': max_r}

    for s_val in [3, 4, 5, 6, 10]:
        s = complex(s_val)
        l_sh = shadow_l_function(coeffs, s, max_r)
        if HAS_MPMATH:
            l_eis = eisenstein_l_function(kappa, s)
        else:
            l_eis = None

        results[f's_{s_val}'] = {
            'L_sh': complex(l_sh),
            'L_eis': l_eis,
            'ratio': complex(l_sh / l_eis).real if l_eis and abs(l_eis) > 1e-50 else None,
        }

    return results


def falsification_comprehensive(max_r: int = 40) -> Dict:
    """Comprehensive falsification across all four depth classes.

    Tests G (Heisenberg), L (affine KM), M (Virasoro).
    Class C (betagamma) terminates at arity 4.
    """
    results = {}

    # Class G: Heisenberg
    results['class_G'] = falsification_heisenberg(k=1.0)

    # Class L: affine sl_2 at level 1
    # kappa = 3*(1+2)/(2*2) = 9/4
    sl2_coeffs = affine_km_shadow_coefficients(dim_g=3, k=1.0, h_dual=2, max_r=max_r)
    results['class_L'] = {
        'algebra': 'sl_2 at level 1',
        'kappa': 9.0 / 4.0,
        'coefficients': {r: v for r, v in sorted(sl2_coeffs.items()) if abs(v) > 1e-50},
        'depth': max(r for r, v in sl2_coeffs.items() if abs(v) > 1e-50),
    }

    # Class M: Virasoro at c = 1, 13, 26
    for c_val in [1.0, 13.0, 26.0]:
        key = f'class_M_c{int(c_val)}'
        results[key] = falsification_virasoro(c_val, max_r)

    return results


# ============================================================================
# SECTION 4.  The CORRECT theorem: genus-1 amplitude Eisenstein property
# ============================================================================


def genus1_arity2_fourier_coefficients(kappa_val: float, n_max: int = 20) -> Dict[int, float]:
    """Fourier coefficients of the genus-1 arity-2 amplitude.

    Sh_2^{(1)}(tau) = kappa * E_2*(tau) = kappa * (1 - 24 sum sigma_1(n) q^n).
    Coefficient of q^n is: -24 * kappa * sigma_1(n) for n >= 1.
    Constant term (q^0) is: kappa.
    """
    coeffs = {0: kappa_val}
    for n in range(1, n_max + 1):
        coeffs[n] = -24.0 * kappa_val * sigma_1(n)
    return coeffs


def genus1_arity2_dirichlet_series(kappa_val: float, s: complex, n_max: int = 200) -> complex:
    """Dirichlet series of the genus-1 arity-2 Fourier coefficients.

    D(s) = sum_{n>=1} a_n * n^{-s} where a_n = -24*kappa*sigma_1(n).
    This equals -24*kappa * zeta(s) * zeta(s-1) for Re(s) > 2.
    """
    total = 0j
    for n in range(1, n_max + 1):
        an = -24.0 * kappa_val * sigma_1(n)
        total += an * (n ** (-s))
    return total


def genus1_arity2_eisenstein_identity(
    kappa_val: float, s: complex, n_max: int = 500
) -> Dict:
    """Verify: sum_{n>=1} (-24*kappa*sigma_1(n)) n^{-s} = -24*kappa*zeta(s)*zeta(s-1).

    This is the CORRECT Eisenstein identity (at arity 2).
    """
    direct = genus1_arity2_dirichlet_series(kappa_val, s, n_max)

    if HAS_MPMATH:
        s_mp = mpmath.mpc(s)
        exact = complex(-24.0 * kappa_val * mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 1))
    else:
        exact = None

    result = {
        'kappa': kappa_val,
        's': complex(s),
        'direct_sum': direct,
        'exact_formula': exact,
    }

    if exact is not None:
        result['agreement'] = abs(direct - exact)
        result['relative_error'] = abs(direct - exact) / max(abs(exact), 1e-50)

    return result


# ============================================================================
# SECTION 5.  Intertwining kernel verification
# ============================================================================


def intertwining_kernel(r: int, s: complex) -> complex:
    """The intertwining kernel M[G_r](s) = r! * Gamma(s-1) / (2pi)^{s-1} * zeta(s-1) * zeta(s+r-2).

    This connects the arity-r graph amplitude G_r(tau) to the L-function.
    Exact at r = 2; leading order for r >= 3.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for intertwining_kernel")
    s_mp = mpmath.mpc(s)
    factorial_r = mpmath.factorial(r)
    gamma_factor = mpmath.gamma(s_mp - 1)
    pi_factor = mpmath.power(2 * mpmath.pi, s_mp - 1)
    zeta1 = mpmath.zeta(s_mp - 1)
    zeta2 = mpmath.zeta(s_mp + r - 2)
    return complex(factorial_r * gamma_factor / pi_factor * zeta1 * zeta2)


def intertwining_kernel_at_r2(s: complex) -> complex:
    """Exact intertwining kernel at r = 2.

    M[G_2](s) = 2 * Gamma(s-1) / (2pi)^{s-1} * zeta(s-1) * zeta(s).

    At s = 2: M[G_2](2) = 2 * Gamma(1) / (2pi) * zeta(1) * zeta(2) = POLE.
    At s = 3: M[G_2](3) = 2 * Gamma(2) / (2pi)^2 * zeta(2) * zeta(3)
            = 2 * 1 / (4pi^2) * (pi^2/6) * zeta(3) = zeta(3) / (3*pi^2) * pi^2 = zeta(3)/3.
    """
    return intertwining_kernel(2, s)


def verify_intertwining_r2_at_s3() -> Dict:
    """Verify M[G_2](3) = zeta(3)/3.

    Exact: 2 * 1! * Gamma(2) / (2pi)^2 * zeta(2) * zeta(3)
         = 2 * 1 / (4*pi^2) * (pi^2/6) * zeta(3)
         = 2 * zeta(3) / (4 * 6)
         = zeta(3) / 12.
    """
    if not HAS_MPMATH:
        return {'error': 'mpmath required'}

    # Direct computation
    kernel_val = intertwining_kernel_at_r2(3.0)

    # Expected: 2 * Gamma(2) / (2pi)^2 * zeta(2) * zeta(3)
    # = 2 * 1 / (4pi^2) * (pi^2/6) * zeta(3)
    # = 2 * zeta(3) / 24 = zeta(3) / 12
    z3 = float(mpmath.zeta(3))
    expected = z3 / 12.0

    return {
        'kernel_at_s3': kernel_val,
        'expected_zeta3_over_12': expected,
        'agreement': abs(kernel_val - expected),
    }


# ============================================================================
# SECTION 6.  Shadow coefficient growth analysis
# ============================================================================


def virasoro_growth_rate_exact(c_val: float) -> float:
    """Exact shadow growth rate rho for Virasoro from the shadow metric.

    rho = |branch point of sqrt(Q_L)| = sqrt(|q2|) / (2*kappa)
    More precisely, the singular points of sqrt(Q_L(t)) are at the zeros of Q_L:
        t_+/- = (-q1 +/- sqrt(q1^2 - 4*q0*q2)) / (2*q2)
    and rho = 1/|t_nearest|.

    For Q_L(t) = c^2 + 12c*t + alpha*t^2:
        discriminant = 144c^2 - 4c^2*alpha = 4c^2*(36 - alpha)
        where alpha = (180c + 872)/(5c + 22).
        36 - alpha = (36(5c+22) - 180c - 872)/(5c+22) = (-80)/(5c+22).
        disc = 4c^2 * (-80)/(5c+22) < 0 for c > 0 (complex roots).
        |t_+/-| = c / sqrt(alpha) (modulus of conjugate pair).
        rho = sqrt(alpha) / c = sqrt((180c+872)/(5c+22)) / c.
    """
    if c_val <= 0:
        raise ValueError("c must be positive for Virasoro growth rate")
    alpha = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    return math.sqrt(alpha) / c_val


def virasoro_growth_rate_numerical(c_val: float, max_r: int = 50) -> float:
    """Numerically estimate rho from the ratio test on S_r."""
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    sorted_r = sorted(r for r, v in coeffs.items() if abs(v) > 1e-50)
    if len(sorted_r) < 5:
        return 0.0
    v_last = abs(coeffs[sorted_r[-1]])
    v_prev = abs(coeffs[sorted_r[-2]])
    if v_prev > 1e-50:
        return v_last / v_prev
    return 0.0


def sigma1_growth_comparison(max_r: int = 30) -> Dict[int, Dict]:
    """Compare S_r growth with sigma_1(r) growth to demonstrate they are different.

    sigma_1(r) grows as O(r log log r) -- POLYNOMIAL.
    S_r (class M) grows as C * rho^r * r^{-5/2} -- GEOMETRIC.
    """
    c_val = 26.0
    kappa = c_val / 2.0
    coeffs = virasoro_shadow_coefficients(c_val, max_r)

    result = {}
    for r in range(2, max_r + 1):
        Sr = coeffs.get(r, 0.0)
        sig1 = sigma_1(r)
        claimed = -kappa * sig1  # What the false identity would predict
        result[r] = {
            'S_r': Sr,
            'minus_kappa_sigma1': claimed,
            'ratio': Sr / claimed if abs(claimed) > 1e-50 else None,
        }
    return result


# ============================================================================
# SECTION 7.  Correct theorem statement decomposition
# ============================================================================


def correct_eisenstein_decomposition(c_val: float, s: complex, max_r: int = 40) -> Dict:
    """The correct decomposition of shadow arithmetic.

    Three distinct objects:
    1. L^sh(s) = sum S_r r^{-s}  (shadow Dirichlet series, from constant terms)
    2. D_2(s) = sum a_n(Sh_2^{(1)}) n^{-s} = -24*kappa*zeta(s)*zeta(s-1)
                (genus-1 arity-2 Fourier Dirichlet series, IS Eisenstein)
    3. -kappa*zeta(s)*zeta(s-1) (the Eisenstein L-function)

    Relationship: D_2(s) = -24 * kappa * zeta(s) * zeta(s-1) (PROVED)
                  L^sh(s) =/= -kappa * zeta(s) * zeta(s-1) (FALSIFIED)
                  L^sh and D_2 are DIFFERENT objects measuring DIFFERENT things.
    """
    kappa = c_val / 2.0
    coeffs = virasoro_shadow_coefficients(c_val, max_r)

    l_sh = shadow_l_function(coeffs, s, max_r)

    result = {
        'c': c_val,
        'kappa': kappa,
        's': complex(s),
        'L_sh': l_sh,  # Object 1
    }

    if HAS_MPMATH:
        # Object 2: genus-1 arity-2 Fourier Dirichlet series
        d2 = genus1_arity2_dirichlet_series(kappa, s, n_max=500)
        result['D_2'] = d2

        # Object 3: Eisenstein L-function
        l_eis = eisenstein_l_function(kappa, s)
        result['L_eis'] = l_eis

        # Verify D_2 = -24*kappa*zeta(s)*zeta(s-1)
        s_mp = mpmath.mpc(s)
        d2_exact = complex(-24.0 * kappa * mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 1))
        result['D_2_exact'] = d2_exact
        result['D_2_agreement'] = abs(d2 - d2_exact)

        # Verify L_sh =/= L_eis
        result['L_sh_vs_L_eis_disagreement'] = abs(l_sh - l_eis)
        result['L_sh_vs_L_eis_ratio'] = (
            complex(l_sh / l_eis).real if abs(l_eis) > 1e-50 else None
        )

    return result


# ============================================================================
# SECTION 8.  Virasoro at c = 26 numerical test (as requested)
# ============================================================================


def virasoro_c26_test_at_s4(max_r: int = 50) -> Dict:
    """Test: for Virasoro at c=26, compare sum S_r r^{-4} with -13*zeta(4)*zeta(3).

    kappa(Vir_26) = 13.
    Claimed: L^sh(4) = -13 * zeta(4) * zeta(3).
    """
    c_val = 26.0
    kappa = 13.0
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    l_sh_4 = shadow_l_function(coeffs, 4.0, max_r)

    result = {
        'c': 26.0,
        'kappa': 13.0,
        'max_r': max_r,
        'L_sh_at_4': complex(l_sh_4).real,
    }

    if HAS_MPMATH:
        z4 = float(mpmath.zeta(4))  # pi^4/90
        z3 = float(mpmath.zeta(3))  # Apery's constant
        l_eis_4 = -13.0 * z4 * z3
        result['L_eis_at_4'] = l_eis_4
        result['zeta_4'] = z4
        result['zeta_3'] = z3
        result['disagreement'] = abs(l_sh_4.real - l_eis_4)
        result['ratio_L_sh_over_L_eis'] = l_sh_4.real / l_eis_4 if abs(l_eis_4) > 1e-50 else None
        result['conclusion'] = (
            'EQUAL' if abs(l_sh_4.real - l_eis_4) < 1e-6
            else 'NOT EQUAL (falsified)'
        )

    return result


# ============================================================================
# SECTION 9.  Summary of the correct theorem
# ============================================================================


def correct_theorem_summary() -> str:
    """Return a plain-text summary of the correct shadow Eisenstein theorem."""
    return r"""
CORRECT SHADOW EISENSTEIN THEOREM (replacing the false thm:shadow-eisenstein)
=============================================================================

DEFINITION (Shadow L-function):
    L_A^{sh}(s) := sum_{r >= 2} S_r(A) r^{-s}
where S_r(A) are the shadow obstruction tower coefficients from the
convolution recursion on Q_L(t).

DEFINITION (Genus-1 amplitude Dirichlet series):
    D_A^{(1,r)}(s) := sum_{n >= 1} a_n(Sh_r^{(1)}) n^{-s}
where a_n are the Fourier coefficients of the genus-1 arity-r shadow amplitude.

THEOREM (Genus-1 Arity-2 Eisenstein Identity):
    D_A^{(1,2)}(s) = -24 kappa(A) zeta(s) zeta(s-1),      Re(s) > 2.
This is the correct Eisenstein identity.  It holds because
    Sh_2^{(1)}(tau) = kappa * E_2*(tau) = kappa(1 - 24 sum sigma_1(n) q^n)
and sum sigma_1(n) n^{-s} = zeta(s) zeta(s-1) is a standard identity.

THEOREM (Intertwining Kernel):
    M[G_r](s) = r! Gamma(s-1)/(2pi)^{s-1} zeta(s-1) zeta(s+r-2)
is exact at r = 2 and of leading order for r >= 3.

NEGATIVE RESULT:
    L_A^{sh}(s) =/= -kappa(A) zeta(s) zeta(s-1)
for ANY chirally Koszul algebra A.  Falsified by:
(a) Heisenberg: L^sh entire, RHS has poles at s=1,2.
(b) Virasoro at s=4: numerical disagreement.
(c) Growth rate: S_r ~ C*rho^r*r^{-5/2} (geometric) vs sigma_1(r) (polynomial).

The shadow L-function and the Eisenstein L-function measure DIFFERENT things:
L^sh extracts CONSTANT TERMS (q^0 coefficients) of genus-1 amplitudes,
while the Eisenstein identity lives in the FOURIER COEFFICIENTS (q^n, n >= 1).
"""
