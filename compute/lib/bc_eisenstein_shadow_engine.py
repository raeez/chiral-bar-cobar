r"""bc_eisenstein_shadow_engine.py -- BC-104: Shadow Eisenstein series construction.

Classical Eisenstein series E_k(tau) = 1 + (normalization) * sum sigma_{k-1}(n) q^n
encode the "average" modular form at weight k.  This module constructs the
shadow Eisenstein series and related objects:

MATHEMATICAL CONTENT
====================

1. SHADOW EISENSTEIN SERIES
   E^{sh}_A(tau, s) = sum_{r>=2} S_r(A) * E_r(tau) * r^{-s}
   where S_r are shadow coefficients and E_r are normalized Eisenstein series.
   For even r >= 4, E_r is a genuine modular form of weight r.
   For r = 2, E_2 is QUASI-modular (AP15).
   For odd r, E_r vanishes identically on SL(2,Z).

2. SHADOW MODULAR FORM (s=0)
   F^{sh}_A(tau) = sum S_r * E_r(tau)
   This has MIXED WEIGHT: it is NOT a modular form.  Each E_r has weight r,
   and different r contribute at different weights.

3. SHADOW L-VALUES via Rankin unfolding
   For a cusp form f in S_k: S_k(A) * L(f, k/2) = <F^{sh}_A, f>
   relating shadow coefficients to central L-values.

4. SHADOW HECKE EIGENVALUES
   T_p(E_k) = (1 + p^{k-1}) * E_k, so the shadow Hecke operator acts diagonally
   on each weight component.

5. SHADOW E_2 PROBLEM (AP15)
   The arity-2 contribution kappa * E_2(tau) is quasi-modular.
   Anomaly: E_2(-1/tau) = tau^2 E_2(tau) + 12*tau/(2*pi*i).
   Shadow modular anomaly = kappa * 12/(2*pi*i).

6. NON-HOLOMORPHIC COMPLETION
   E_2*(tau) = E_2(tau) - 3/(pi*Im(tau)) transforms correctly but is not holomorphic.
   F^{sh,*}_A(tau) = kappa*E_2*(tau) + sum_{r>=4, even} S_r * E_r(tau).

7. SHADOW MAASS FORM
   Using the Maass Eisenstein series E(tau, s) = sum Im(gamma*tau)^s.

8. L-FUNCTION COMPARISON
   Formal Mellin: zeta_A(s) ~ integral of (F^{sh}_A(it) - constant) * t^{s-1} dt.

CONVENTIONS:
  - q = e^{2*pi*i*tau}
  - Cohomological grading (|d| = +1), bar uses desuspension
  - kappa(Vir_c) = c/2 (AP9: NOT c/2 for general VOAs, AP48)
  - E_2 is QUASI-modular (AP15): E_2* = E_2 - 3/(pi*Im(tau))
  - Odd-weight Eisenstein series vanish on SL(2,Z)
  - E_k for even k >= 4 are Hecke eigenforms with eigenvalue 1 + p^{k-1}

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general.
CAUTION (AP10): Tests must verify by multiple independent paths.
CAUTION (AP15): E_2* is quasi-modular. Do NOT apply holomorphic dim formulas.
CAUTION (AP38): Normalize conventions carefully for literature comparisons.
CAUTION (AP46): eta(q) = q^{1/24} * prod(1-q^n); do NOT drop q^{1/24}.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:depth-decomposition (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# ============================================================================
# 0.  Arithmetic utilities
# ============================================================================


def sigma_k(n: int, k: int) -> int:
    r"""Divisor sum sigma_k(n) = sum_{d | n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def bernoulli_number(n: int) -> Fraction:
    """Compute the n-th Bernoulli number B_n as an exact fraction.

    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_4 = -1/30, B_6 = 1/42,
    B_8 = -1/30, B_10 = 5/66, B_12 = -691/2730.
    """
    if n < 0:
        return Fraction(0)
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        B[m] = Fraction(0)
        for k in range(m):
            B[m] -= Fraction(math.comb(m, k), m - k + 1) * B[k]
    return B[n]


_BERNOULLI_CACHE: Dict[int, Fraction] = {}


def _bernoulli_cached(n: int) -> Fraction:
    if n not in _BERNOULLI_CACHE:
        _BERNOULLI_CACHE[n] = bernoulli_number(n)
    return _BERNOULLI_CACHE[n]


# ============================================================================
# 1.  Eisenstein series: coefficients and evaluation
# ============================================================================


def eisenstein_coefficient(k: int, n: int) -> Fraction:
    r"""The n-th Fourier coefficient of E_k(tau).

    E_k(tau) = 1 + (-2k/B_k) * sum_{n>=1} sigma_{k-1}(n) q^n

    For even k >= 2. Returns exact fraction.

    Examples:
        E_4: a_0 = 1, a_1 = 240 (since -8/B_4 = -8/(-1/30) = 240)
        E_6: a_0 = 1, a_1 = -504 (since -12/B_6 = -12/(1/42) = -504)
        E_2: a_0 = 1, a_1 = -24  (since -4/B_2 = -4/(1/6) = -24)
    """
    if k < 2 or k % 2 != 0:
        return Fraction(0)
    if n == 0:
        return Fraction(1)
    if n < 0:
        return Fraction(0)
    Bk = _bernoulli_cached(k)
    if Bk == 0:
        return Fraction(0)
    norm = Fraction(-2 * k) / Bk
    return norm * Fraction(sigma_k(n, k - 1))


def eisenstein_q_expansion(k: int, nmax: int = 50) -> List[Fraction]:
    r"""Return Fourier coefficients [a_0, a_1, ..., a_{nmax}] of E_k.

    E_k(tau) = sum_{n=0}^{inf} a_n q^n.
    """
    return [eisenstein_coefficient(k, n) for n in range(nmax + 1)]


def eisenstein_numerical(k: int, tau: complex, nmax: int = 200) -> complex:
    r"""Evaluate E_k(tau) numerically.

    For even k >= 2.  For k = 2, this is QUASI-modular (AP15).
    For odd k on SL(2,Z), E_k = 0 identically.
    """
    if k % 2 != 0 or k < 2:
        return 0.0 + 0j
    if tau.imag <= 0:
        raise ValueError(f"tau must be in upper half-plane, got Im(tau)={tau.imag}")

    q = cmath.exp(2 * cmath.pi * 1j * tau)
    Bk = float(_bernoulli_cached(k))
    norm = -2.0 * k / Bk
    result = 1.0 + 0j
    qn = q
    for n in range(1, nmax + 1):
        sig = sigma_k(n, k - 1)
        term = norm * sig * qn
        result += term
        if abs(term) < 1e-15:
            break
        qn *= q
    return result


def E2_nonholomorphic(tau: complex, nmax: int = 200) -> complex:
    r"""Non-holomorphic completion E_2*(tau) = E_2(tau) - 3/(pi*Im(tau)).

    E_2* transforms as a genuine weight-2 (non-holomorphic) modular form:
        E_2*(-1/tau) = tau^2 * E_2*(tau)  (no anomaly)

    But E_2* is NOT holomorphic: it depends on Im(tau) = y.
    """
    E2 = eisenstein_numerical(2, tau, nmax)
    return E2 - 3.0 / (math.pi * tau.imag)


# ============================================================================
# 2.  Virasoro shadow coefficients
# ============================================================================


def kappa_virasoro(c_val: float) -> float:
    """kappa(Vir_c) = c/2."""
    return c_val / 2.0


def virasoro_shadow_coefficients(c_val: float, max_r: int = 30) -> Dict[int, float]:
    r"""Shadow coefficients S_r for Virasoro Vir_c via convolution recursion.

    S_r = a_{r-2} / r where a_n = [t^n] sqrt(Q_L(t)),
    Q_L(t) = c^2 + 12c*t + alpha(c)*t^2, alpha = (180c+872)/(5c+22).

    Class M: infinite tower, S_r ~ rho^r r^{-5/2}.
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")

    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    a0 = abs(c_val)  # sqrt(c^2) = |c|
    a = [a0]
    if max_r >= 3:
        a.append(q1 / (2.0 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))

    result = {}
    for n in range(len(a)):
        r = n + 2
        result[r] = a[n] / float(r)
    return result


def virasoro_shadow_exact(r: int, c_val: Fraction) -> Fraction:
    r"""Exact shadow coefficient S_r(Vir_c) as a rational function of c.

    Uses the same convolution recursion but with exact arithmetic.
    """
    if c_val == 0 or 5 * c_val + 22 == 0:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")

    q0 = c_val ** 2
    q1 = Fraction(12) * c_val
    q2 = (Fraction(180) * c_val + 872) / (Fraction(5) * c_val + 22)

    a = [abs(c_val)]
    if r >= 3:
        a.append(q1 / (2 * a[0]))
    if r >= 4:
        a.append((q2 - a[1] ** 2) / (2 * a[0]))
    for n in range(3, r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a[0]))

    n = r - 2
    if n < len(a):
        return a[n] / r
    return Fraction(0)


# ============================================================================
# 3.  Shadow Eisenstein series
# ============================================================================


def shadow_eisenstein_series(
    shadow_coeffs: Dict[int, float],
    tau: complex,
    s: float,
    max_r: int = 30,
    nmax: int = 200,
) -> complex:
    r"""Compute E^{sh}_A(tau, s) = sum_{r>=2} S_r(A) * E_r(tau) * r^{-s}.

    Only even r >= 2 contribute (odd Eisenstein vanish on SL(2,Z)).
    For r = 2, E_2 is quasi-modular (AP15) but still well-defined as a function.

    Parameters:
        shadow_coeffs: dict {r: S_r}
        tau: upper half-plane point
        s: complex exponent for r^{-s}
        max_r: maximum arity
        nmax: Fourier expansion depth for each E_r

    Returns:
        E^{sh}_A(tau, s) as complex number.
    """
    result = 0.0 + 0j
    for r in range(2, max_r + 1):
        if r % 2 != 0:
            continue  # Odd Eisenstein vanish on SL(2,Z)
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-30:
            continue
        Ek = eisenstein_numerical(r, tau, nmax)
        result += Sr * Ek * r ** (-s)
    return result


def shadow_eisenstein_virasoro(
    c_val: float,
    tau: complex,
    s: float,
    max_r: int = 30,
    nmax: int = 200,
) -> complex:
    r"""Shadow Eisenstein for Virasoro at central charge c."""
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    return shadow_eisenstein_series(coeffs, tau, s, max_r, nmax)


# ============================================================================
# 4.  Shadow modular form F^{sh}_A (s = 0 specialization)
# ============================================================================


def shadow_modular_form(
    shadow_coeffs: Dict[int, float],
    tau: complex,
    max_r: int = 30,
    nmax: int = 200,
) -> complex:
    r"""F^{sh}_A(tau) = sum_{r>=2, even} S_r * E_r(tau).

    This has MIXED WEIGHT: it is NOT a modular form, since E_r has weight r
    and different r contribute at different weights.  Still, it is a
    well-defined holomorphic function on H (upper half-plane).
    """
    return shadow_eisenstein_series(shadow_coeffs, tau, 0.0, max_r, nmax)


def shadow_modular_form_completed(
    shadow_coeffs: Dict[int, float],
    tau: complex,
    max_r: int = 30,
    nmax: int = 200,
) -> complex:
    r"""F^{sh,*}_A(tau) = kappa*E_2*(tau) + sum_{r>=4, even} S_r * E_r(tau).

    Non-holomorphic completion: replaces E_2 with E_2* = E_2 - 3/(pi*y).
    This transforms correctly under SL(2,Z) weight-by-weight but is NOT holomorphic.
    """
    kappa = shadow_coeffs.get(2, 0.0)
    # arity-2 contribution: kappa * E_2*(tau)
    result = kappa * E2_nonholomorphic(tau, nmax)
    # arity >= 4, even: genuine modular forms
    for r in range(4, max_r + 1):
        if r % 2 != 0:
            continue
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-30:
            continue
        Ek = eisenstein_numerical(r, tau, nmax)
        result += Sr * Ek
    return result


# ============================================================================
# 5.  Shadow modular anomaly (E_2 quasi-modularity)
# ============================================================================


def shadow_modular_anomaly(kappa_val: float) -> complex:
    r"""The quasi-modular anomaly from the arity-2 shadow contribution.

    E_2(-1/tau) = tau^2 E_2(tau) + 12*tau/(2*pi*i).
    The anomaly term is 12/(2*pi*i), scaled by kappa.

    shadow anomaly = kappa * 12 / (2*pi*i)

    For Virasoro: kappa = c/2, so anomaly = c * 6 / (2*pi*i) = 6c/(2*pi*i).
    """
    return kappa_val * 12.0 / (2.0 * math.pi * 1j)


def shadow_modular_anomaly_virasoro(c_val: float) -> complex:
    """Shadow modular anomaly for Virasoro at central charge c."""
    return shadow_modular_anomaly(c_val / 2.0)


# ============================================================================
# 6.  Shadow L-values (Rankin unfolding)
# ============================================================================


def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: tau(n) = coeff of q^n in Delta(q) = q*prod(1-q^m)^{24}.

    Known values: tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830.
    """
    if n <= 0:
        return 0
    N = n + 1
    coeffs = [0] * N
    coeffs[0] = 1
    for m in range(1, N):
        new_coeffs = [0] * N
        for j in range(25):
            sign = (-1) ** j
            binom = math.comb(24, j)
            shift = j * m
            if shift >= N:
                break
            for i in range(N - shift):
                new_coeffs[i + shift] += sign * binom * coeffs[i]
        coeffs = new_coeffs
    if n - 1 < len(coeffs):
        return coeffs[n - 1]
    return 0


def delta_L_function(s: float, nmax: int = 500) -> float:
    r"""L(Delta, s) = sum_{n>=1} tau(n) * n^{-s}.

    Converges for Re(s) > 13/2 (Ramanujan conjecture: |tau(p)| < 2*p^{11/2}).
    Critical strip: 0 < Re(s) < 12.  Center: s = 6.

    We compute the partial sum to nmax terms.
    """
    result = 0.0
    for n in range(1, nmax + 1):
        result += ramanujan_tau(n) * n ** (-s)
    return result


def petersson_norm_eisenstein(k: int) -> float:
    r"""Approximate Petersson norm <E_k, E_k> for SL(2,Z).

    For the normalized Eisenstein series E_k, the Petersson inner product
    against itself is:

    <E_k, E_k> = 3 * (k-2)! / (2^{2k-1} * pi^{k+1}) * |B_k|^{-2} * zeta(k)^2 * volume

    This is not used for modularity (E_k is not a cusp form so the Petersson
    norm diverges), but the REGULARIZED inner product can be defined.

    For practical purposes, we return the Rankin-Selberg integral normalization
    factor that relates <f, E_k> to L(f, k-1) for a cusp form f of weight k.

    The Rankin unfolding gives: <f, E_k>_{reg} = L(f, k-1) * Gamma(k-1) / (4*pi)^{k-1}
    (with appropriate volume normalization).

    We return a symbolic placeholder; the actual computation uses the L-function.
    """
    # The regularized Petersson inner product of E_k with itself
    # involves the residue of the Rankin-Selberg zeta at the pole.
    # <E_k, E_k>_{reg} = 3/pi * Gamma(k) * zeta(k) * zeta(k-1) / (4*pi)^k
    # This is approximate; we compute numerically.
    from math import gamma as math_gamma
    gk = math_gamma(k)
    zk = _riemann_zeta_approx(k)
    zkm1 = _riemann_zeta_approx(k - 1)
    return 3.0 / math.pi * gk * zk * zkm1 / (4.0 * math.pi) ** k


def _riemann_zeta_approx(s: float, nmax: int = 10000) -> float:
    """Approximate Riemann zeta for real s > 1."""
    if s <= 1:
        raise ValueError(f"zeta(s) needs s > 1, got s={s}")
    return sum(n ** (-s) for n in range(1, nmax + 1))


def shadow_L_value_delta(c_val: float, nmax: int = 200) -> Dict[str, float]:
    r"""For f = Delta (weight 12 cusp form), compute:
        S_12(Vir_c) * L(Delta, 6)

    This equals <F^{sh}_{Vir_c}, Delta> by Rankin unfolding.

    Returns dict with S_12, L_Delta_6, and their product.
    """
    coeffs = virasoro_shadow_coefficients(c_val, max_r=14)
    S12 = coeffs.get(12, 0.0)
    L_6 = delta_L_function(6.0, nmax)
    return {
        'S_12': S12,
        'L_Delta_6': L_6,
        'product': S12 * L_6,
        'c': c_val,
    }


# ============================================================================
# 7.  Shadow Hecke eigenvalues
# ============================================================================


def hecke_eigenvalue_eisenstein(p: int, k: int) -> int:
    r"""Hecke eigenvalue of E_k for the operator T_p.

    T_p(E_k) = (1 + p^{k-1}) * E_k.
    So lambda_p(E_k) = 1 + p^{k-1} = sigma_{k-1}(p).
    """
    return 1 + p ** (k - 1)


def shadow_hecke_eigenvalue(
    shadow_coeffs: Dict[int, float],
    p: int,
    s: float,
    max_r: int = 30,
) -> complex:
    r"""Shadow Hecke eigenvalue: weighted average of Hecke eigenvalues.

    T_p^{sh} E^{sh}_A = sum_r S_r * (1 + p^{r-1}) * E_r * r^{-s}

    The "shadow Hecke eigenvalue" for the full shadow:
        lambda_p^{sh}(A, s) = sum_r S_r * (1 + p^{r-1}) * r^{-s}
                               / sum_r S_r * r^{-s}

    i.e. the ratio of the Hecke-acted shadow zeta to the shadow zeta.

    Returns the eigenvalue (complex, since the denominator may be complex
    when evaluated at complex s).
    """
    numerator = 0.0
    denominator = 0.0
    for r in range(2, max_r + 1):
        if r % 2 != 0:
            continue
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-30:
            continue
        weight = Sr * r ** (-s)
        denominator += weight
        numerator += weight * (1 + p ** (r - 1))

    if abs(denominator) < 1e-30:
        return float('nan')
    return numerator / denominator


def shadow_hecke_eigenvalue_virasoro(
    c_val: float,
    p: int,
    s: float,
    max_r: int = 30,
) -> complex:
    """Shadow Hecke eigenvalue for Virasoro at central charge c."""
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    return shadow_hecke_eigenvalue(coeffs, p, s, max_r)


def shadow_hecke_acted_zeta(
    shadow_coeffs: Dict[int, float],
    p: int,
    s: float,
    max_r: int = 30,
) -> float:
    r"""Numerator: sum_r S_r * (1 + p^{r-1}) * r^{-s} (even r only)."""
    result = 0.0
    for r in range(2, max_r + 1):
        if r % 2 != 0:
            continue
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-30:
            continue
        result += Sr * (1 + p ** (r - 1)) * r ** (-s)
    return result


def shadow_zeta(
    shadow_coeffs: Dict[int, float],
    s: float,
    max_r: int = 30,
) -> float:
    r"""Shadow zeta: sum_r S_r * r^{-s} (all r >= 2)."""
    result = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        result += Sr * r ** (-s)
    return result


def shadow_zeta_even(
    shadow_coeffs: Dict[int, float],
    s: float,
    max_r: int = 30,
) -> float:
    r"""Shadow zeta restricted to even arities: sum_{r>=2, even} S_r * r^{-s}."""
    result = 0.0
    for r in range(2, max_r + 1, 2):
        Sr = shadow_coeffs.get(r, 0.0)
        result += Sr * r ** (-s)
    return result


# ============================================================================
# 8.  Maass Eisenstein series
# ============================================================================


def maass_eisenstein_numerical(tau: complex, s: float, nmax: int = 500) -> complex:
    r"""Approximate the real-analytic Eisenstein series E(tau, s).

    E(tau, s) = (1/2) sum_{(c,d)=1, (c,d) != (0,0)} (Im(tau))^s / |c*tau + d|^{2s}

    For Re(s) > 1, converges absolutely.  The sum ranges over coprime (c, d)
    with the convention that (c, d) and (-c, -d) are identified.

    The Laplacian eigenvalue is s(1-s).

    We approximate by summing over |c|, |d| <= nmax with gcd(c,d) = 1.
    """
    y = tau.imag
    if y <= 0:
        raise ValueError("tau must be in upper half-plane")

    result = 0.0 + 0j
    # (c, d) = (0, 1): contributes y^s
    result += y ** s

    for c_abs in range(1, nmax + 1):
        for d in range(-nmax, nmax + 1):
            if math.gcd(c_abs, abs(d)) != 1:
                continue
            # c = c_abs
            ct = c_abs * tau + d
            result += y ** s / abs(ct) ** (2.0 * s)
            # c = -c_abs (equivalent to (c_abs, -d) by negation, but we
            # should not double-count since we identify (c,d) ~ (-c,-d))
            # Actually the convention includes both signs.
            # The standard sum is over c >= 0 with (c,d) != (0,0) and
            # for c = 0: d = 1 only (already counted above).
            # For c > 0: sum over all d coprime to c.
            # So we DON'T add c = -c_abs.

    return result


def shadow_maass_series(
    shadow_coeffs: Dict[int, float],
    tau: complex,
    s2: float,
    max_r: int = 20,
    nmax: int = 100,
) -> complex:
    r"""Shadow Maass series: E^{sh,Maass}_A(tau, s2) = sum_r S_r * E(tau, r/2) * r^{-s2}.

    Uses the real-analytic Maass Eisenstein E(tau, s) at s = r/2.
    Only even r >= 4 contribute (for the Maass Eisenstein to converge, need s > 1,
    so r >= 4; r = 2 gives s = 1 which is the pole).
    """
    result = 0.0 + 0j
    for r in range(4, max_r + 1):
        if r % 2 != 0:
            continue
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-30:
            continue
        E_maass = maass_eisenstein_numerical(tau, r / 2.0, nmax)
        result += Sr * E_maass * r ** (-s2)
    return result


# ============================================================================
# 9.  E_2 transformation verification
# ============================================================================


def verify_E2_transformation(tau: complex, nmax: int = 200) -> Dict[str, Any]:
    r"""Verify E_2(-1/tau) = tau^2 * E_2(tau) + 12*tau/(2*pi*i).

    Returns dict with LHS, RHS, and difference.
    """
    E2_tau = eisenstein_numerical(2, tau, nmax)
    tau_inv = -1.0 / tau
    E2_inv = eisenstein_numerical(2, tau_inv, nmax)

    lhs = E2_inv
    rhs = tau ** 2 * E2_tau + 12.0 * tau / (2.0 * math.pi * 1j)
    return {
        'lhs': lhs,
        'rhs': rhs,
        'difference': abs(lhs - rhs),
        'tau': tau,
    }


def verify_E2star_transformation(tau: complex, nmax: int = 200) -> Dict[str, Any]:
    r"""Verify E_2*(-1/tau) = tau^2 * E_2*(tau).

    E_2*(tau) = E_2(tau) - 3/(pi*Im(tau)) is the non-holomorphic completion.
    """
    E2star_tau = E2_nonholomorphic(tau, nmax)
    tau_inv = -1.0 / tau
    E2star_inv = E2_nonholomorphic(tau_inv, nmax)

    lhs = E2star_inv
    rhs = tau ** 2 * E2star_tau
    return {
        'lhs': lhs,
        'rhs': rhs,
        'difference': abs(lhs - rhs),
        'tau': tau,
    }


def verify_Ek_modular_transformation(
    k: int, tau: complex, nmax: int = 200
) -> Dict[str, Any]:
    r"""Verify E_k(-1/tau) = tau^k * E_k(tau) for even k >= 4.

    This is the standard modular transformation for Eisenstein series.
    """
    Ek_tau = eisenstein_numerical(k, tau, nmax)
    tau_inv = -1.0 / tau
    Ek_inv = eisenstein_numerical(k, tau_inv, nmax)

    lhs = Ek_inv
    rhs = tau ** k * Ek_tau
    return {
        'lhs': lhs,
        'rhs': rhs,
        'difference': abs(lhs - rhs),
        'tau': tau,
    }


# ============================================================================
# 10. Completed shadow Eisenstein transformation
# ============================================================================


def verify_completed_shadow_transformation(
    shadow_coeffs: Dict[int, float],
    tau: complex,
    max_r: int = 20,
    nmax: int = 200,
) -> Dict[str, Any]:
    r"""Verify F^{sh,*}_A(-1/tau) transforms correctly.

    Each weight-k piece transforms as tau^k, so:
        F^{sh,*}_A(-1/tau) = kappa * tau^2 * E_2*(tau)
                            + sum_{r>=4,even} S_r * tau^r * E_r(tau)

    There is no universal modular property since weights are mixed,
    but each piece transforms correctly.

    Returns per-weight verification.
    """
    tau_inv = -1.0 / tau
    verifications = {}

    kappa = shadow_coeffs.get(2, 0.0)
    if abs(kappa) > 1e-30:
        check = verify_E2star_transformation(tau, nmax)
        verifications[2] = {
            'coefficient': kappa,
            'error': check['difference'],
        }

    for r in range(4, max_r + 1):
        if r % 2 != 0:
            continue
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-30:
            continue
        check = verify_Ek_modular_transformation(r, tau, nmax)
        verifications[r] = {
            'coefficient': Sr,
            'error': check['difference'],
        }

    total_error = sum(v['error'] for v in verifications.values())
    return {
        'per_weight': verifications,
        'total_error': total_error,
        'tau': tau,
    }


# ============================================================================
# 11. Eisenstein values at special points
# ============================================================================


def eisenstein_at_special_points(k: int, nmax: int = 300) -> Dict[str, complex]:
    r"""Evaluate E_k at the two special CM points.

    tau = i  (self-dual under S: tau -> -1/tau)
    tau = rho = e^{2*pi*i/3}  (sixth root of unity, fixed by ST)

    Known EXACT values (k even, k >= 4):
        E_4(i) = 12 * Gamma(1/4)^8 / (2*pi)^6  (real, positive)
        E_6(i) = 0  (zero by the S-transformation: E_6(i) = i^6 E_6(i) = -E_6(i))
        E_4(rho) = 0  (zero by ST-transformation at order 3)
        E_6(rho) = real, nonzero

    General: E_k(i) = 0 if k = 2 mod 4 (since i^k = -1 forces E_k(i) = 0).
             E_k(rho) = 0 if k = 2 mod 6 or k = 4 mod 6.
    """
    tau_i = complex(0, 1)
    tau_rho = cmath.exp(2.0 * cmath.pi * 1j / 3.0)

    return {
        'tau_i': eisenstein_numerical(k, tau_i, nmax),
        'tau_rho': eisenstein_numerical(k, tau_rho, nmax),
    }


# ============================================================================
# 12. Shadow constant term and Mellin transform (formal)
# ============================================================================


def shadow_constant_term(shadow_coeffs: Dict[int, float], max_r: int = 30) -> float:
    r"""Constant term of F^{sh}_A: sum_{r>=2, even} S_r * E_r(q=0).

    Since E_k(q=0) = 1 for all k, this is simply sum_{r>=2, even} S_r.
    """
    return sum(
        shadow_coeffs.get(r, 0.0)
        for r in range(2, max_r + 1)
        if r % 2 == 0
    )


def shadow_mellin_integrand(
    shadow_coeffs: Dict[int, float],
    t: float,
    s: float,
    max_r: int = 30,
    nmax: int = 200,
) -> float:
    r"""Integrand for the formal Mellin transform:
        zeta_A(s) ~ integral_0^infty (F^{sh}_A(it) - constant) * t^{s-1} dt

    Evaluates (F^{sh}_A(it) - constant term) * t^{s-1}.

    CONVERGENCE WARNING: this integral may not converge.
    """
    if t <= 0:
        raise ValueError("t must be positive")
    tau = complex(0, t)
    F_val = shadow_modular_form(shadow_coeffs, tau, max_r, nmax)
    const = shadow_constant_term(shadow_coeffs, max_r)
    return (F_val.real - const) * t ** (s - 1)


def shadow_mellin_numerical(
    shadow_coeffs: Dict[int, float],
    s: float,
    max_r: int = 20,
    nmax: int = 100,
    t_min: float = 0.1,
    t_max: float = 10.0,
    n_points: int = 100,
) -> Dict[str, float]:
    r"""Numerical approximation of the Mellin transform integral.

    Uses trapezoidal rule on [t_min, t_max] with n_points.
    WARNING: The full Mellin integral over (0, infty) may diverge.
    This computes only the truncated integral.
    """
    dt = (t_max - t_min) / n_points
    total = 0.0
    for i in range(n_points + 1):
        t = t_min + i * dt
        w = 0.5 if (i == 0 or i == n_points) else 1.0
        val = shadow_mellin_integrand(shadow_coeffs, t, s, max_r, nmax)
        total += w * val * dt

    # Compare with direct shadow zeta
    zeta_direct = shadow_zeta(shadow_coeffs, s, max_r)

    return {
        's': s,
        'mellin_truncated': total,
        'zeta_direct': zeta_direct,
        't_range': (t_min, t_max),
        'n_points': n_points,
    }


# ============================================================================
# 13. Known Eisenstein special values (for verification)
# ============================================================================


def E4_at_i_exact() -> float:
    r"""E_4(i) = 3 * Gamma(1/4)^8 / (64 * pi^6).

    Derivation: E_4(tau) = (3/(4*pi^4)) * g_2({1,tau}).
    For tau = i, the lattice Z[i] has g_2(Z[i]) = Gamma(1/4)^8 / (16*pi^2).
    Hence E_4(i) = (3/(4*pi^4)) * Gamma(1/4)^8 / (16*pi^2)
                 = 3*Gamma(1/4)^8 / (64*pi^6).

    Numerically: E_4(i) ~ 1.4558.
    """
    g14 = 3.6256099082219083
    return 3.0 * g14 ** 8 / (64.0 * math.pi ** 6)


def E6_at_rho_exact() -> float:
    r"""E_6(rho) where rho = e^{2*pi*i/3}.

    E_6(rho) = 27 * Gamma(1/3)^{18} / (512 * pi^{12}).

    Derivation: from E_6(rho) * (2*pi)^{12} / Gamma(1/3)^{18} = 216 = 6^3.
    So E_6(rho) = 216 * Gamma(1/3)^{18} / (2*pi)^{12}
               = 27 * Gamma(1/3)^{18} / (512 * pi^{12}).

    Numerically: E_6(rho) ~ 2.8815411.
    """
    g13 = 2.6789385347077476
    return 27.0 * g13 ** 18 / (512.0 * math.pi ** 12)


# ============================================================================
# 14. Summary computation for specified parameter sets
# ============================================================================


def compute_full_shadow_eisenstein_table(
    c_values: List[float] = None,
    tau_values: Dict[str, complex] = None,
    s_values: List[float] = None,
    p_values: List[int] = None,
    max_r: int = 20,
) -> Dict[str, Any]:
    r"""Compute a full table of shadow Eisenstein data.

    Default parameters from the task specification:
        c = 1, 13, 25
        tau = i, e^{2*pi*i/3}
        s = 2, 3, 4
        p = 2, 3, 5, 7
    """
    if c_values is None:
        c_values = [1.0, 13.0, 25.0]
    if tau_values is None:
        tau_values = {
            'i': complex(0, 1),
            'rho': cmath.exp(2 * cmath.pi * 1j / 3),
        }
    if s_values is None:
        s_values = [2.0, 3.0, 4.0]
    if p_values is None:
        p_values = [2, 3, 5, 7]

    results = {}
    for c_val in c_values:
        c_key = f"c={c_val}"
        results[c_key] = {}
        coeffs = virasoro_shadow_coefficients(c_val, max_r)

        # Shadow Eisenstein at each (tau, s)
        for tau_name, tau_val in tau_values.items():
            for s_val in s_values:
                key = f"E_sh(tau={tau_name}, s={s_val})"
                results[c_key][key] = shadow_eisenstein_series(
                    coeffs, tau_val, s_val, max_r
                )

        # Shadow Hecke eigenvalues
        for p in p_values:
            for s_val in s_values:
                key = f"lambda_{p}^sh(s={s_val})"
                results[c_key][key] = shadow_hecke_eigenvalue(
                    coeffs, p, s_val, max_r
                )

        # Shadow anomaly
        results[c_key]['anomaly'] = shadow_modular_anomaly(c_val / 2.0)

        # L-value data
        results[c_key]['L_delta'] = shadow_L_value_delta(c_val)

    return results
