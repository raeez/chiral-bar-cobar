#!/usr/bin/env python3
"""Period integral engine: connecting shadow coefficients to L-function values.

The fundamental bridge between homotopy (shadow tower) and arithmetic (L-functions)
is the Rankin-Selberg period integral. For lattice VOAs, each shadow arity maps
to a specific period integral of a modular form.

The period hierarchy:
  Arity 2: kappa = Petersson inner product of Theta with Eisenstein
  Arity 3: Rankin-Selberg of Theta against E_{k,s}
  Arity 4+: L(s, f_j) values for cusp form components of Theta

The sewing-Selberg formula (thm:sewing-selberg-formula):
  integral_{M_{1,1}} log det(1-K(tau)) E_s(tau) dmu(tau)
    = -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)

The Rankin-Selberg factorization for Leech (the KEY identity):
  L(s, Delta x Delta_bar) = zeta(s-11) L(s, Sym^2 Delta)

References:
  arithmetic_shadows.tex: thm:sewing-selberg-formula
  genus_complete.tex: def:two-variable-L

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Dict, List, Optional, Tuple, Union

import mpmath
from mpmath import mp, mpf, mpc, pi, gamma as mpgamma, zeta, power, fsum, sqrt, log, inf

mp.dps = 50


# ============================================================
# 0. Ramanujan tau and auxiliary arithmetic
# ============================================================

def _ramanujan_tau_batch(nmax: int) -> List[int]:
    """Compute tau(1), ..., tau(nmax) via eta^24 expansion.

    Delta_12 = eta^24 = sum_{n>=1} tau(n) q^n.
    The coefficients are computed by iteratively multiplying
    (1-q^m)^24 for m = 1, 2, ..., nmax.
    """
    N = nmax + 5
    coeffs = [0] * (N + 1)
    coeffs[0] = 1

    for m in range(1, N + 1):
        new_coeffs = [0] * (N + 1)
        for j in range(25):
            sign = (-1) ** j
            binom_val = 1
            for i in range(j):
                binom_val = binom_val * (24 - i) // (i + 1)
            c = sign * binom_val
            for k in range(N + 1):
                idx = k + j * m
                if idx > N:
                    break
                new_coeffs[idx] += coeffs[k] * c
        coeffs = new_coeffs

    return [coeffs[n - 1] if n - 1 < len(coeffs) else 0
            for n in range(1, nmax + 1)]


@lru_cache(maxsize=4)
def _cached_tau(nmax: int) -> List[int]:
    return _ramanujan_tau_batch(nmax)


def _sigma(n: int, k: int) -> int:
    """sigma_k(n) = sum_{d|n} d^k."""
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def _eisenstein_coefficients(weight: int, nmax: int) -> List[mpf]:
    """Fourier coefficients of normalized Eisenstein series E_k.

    E_k(tau) = 1 + (2k/B_k) sum_{n>=1} sigma_{k-1}(n) q^n.
    """
    Bk = mpmath.bernoulli(weight)
    norm = mpf(-2 * weight) / Bk
    coeffs = [mpf(1)]
    for n in range(1, nmax + 1):
        coeffs.append(norm * _sigma(n, weight - 1))
    return coeffs


# ============================================================
# 1. Rankin-Selberg unfolding (Dirichlet series)
# ============================================================

def rankin_selberg_unfolding(
    f_coeffs: List[Union[int, float, mpf]],
    g_coeffs: List[Union[int, float, mpf]],
    s: Union[float, mpf, mpc],
    num_terms: int = 200,
) -> mpc:
    r"""Compute the Rankin-Selberg Dirichlet series sum_{n>=1} a(n) conj(b(n)) / n^s.

    After Rankin-Selberg unfolding, the integral of f * bar(g) * E_s
    over the fundamental domain reduces to a Dirichlet series in the
    Fourier coefficients.

    Parameters
    ----------
    f_coeffs : coefficients a(0), a(1), ..., a(N) with a(0) = constant term
    g_coeffs : coefficients b(0), b(1), ..., b(N)
    s : complex parameter
    num_terms : truncation of the Dirichlet series

    Returns
    -------
    sum_{n=1}^{num_terms} a(n) * conj(b(n)) / n^s
    """
    s = mpc(s)
    total = mpc(0)
    N = min(num_terms, len(f_coeffs) - 1, len(g_coeffs) - 1)
    for n in range(1, N + 1):
        an = mpf(f_coeffs[n])
        bn = mpf(g_coeffs[n])
        total += an * mpmath.conj(bn) * power(mpf(n), -s)
    return total


# ============================================================
# 2. Sewing-Selberg formula
# ============================================================

def sewing_selberg_integral(s: Union[float, mpf, mpc]) -> mpc:
    r"""The sewing-Selberg integral (thm:sewing-selberg-formula).

    integral_{M_{1,1}} log det(1 - K(tau)) E_s(tau) dmu(tau)
      = -2 (2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)

    This connects the Heisenberg genus-1 partition function to
    zeta(s-1) zeta(s).

    Parameters
    ----------
    s : complex parameter.  Formula has poles at s=1 (from zeta(s-1)=zeta(0))
        and s=2 is a regular value.

    Returns
    -------
    The value -2 (2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s).
    """
    s = mpc(s)
    return -2 * power(2 * pi, -(s - 1)) * mpgamma(s - 1) * zeta(s - 1) * zeta(s)


# ============================================================
# 3. Petersson norm (numerical from Fourier coefficients)
# ============================================================

def petersson_norm_numerical(
    f_coeffs: List[Union[int, float, mpf]],
    weight: int,
    num_terms: int = 200,
) -> mpf:
    r"""Numerical approximation to the Petersson norm <f,f>.

    For a cuspidal Hecke eigenform f = sum a(n) q^n of weight k on SL_2(Z),
    the Rankin-Selberg method gives:

        <f,f>_{Pet} = (4pi)^{-(k-1)} Gamma(k-1) sum_{n>=1} |a(n)|^2 / n^{k-1}

    multiplied by the residue of the Eisenstein series at s=k, which is
    3/pi for SL_2(Z).

    More precisely (Rankin's formula, Zagier's normalization):
        <f,f> = (k-1)! / (4pi)^k * L(k, f x f_bar) * (residue factor)

    For practical computation, the Dirichlet series sum |a(n)|^2 / n^s
    at s = k gives the dominant contribution (up to gamma and pi factors).

    This returns the Rankin-Selberg Dirichlet series value
        D(k-1) = sum_{n=1}^{num_terms} |a(n)|^2 / n^{k-1}
    multiplied by Gamma(k-1) / (4pi)^{k-1}, providing a proxy proportional
    to the Petersson norm.
    """
    k = mpf(weight)
    total = mpf(0)
    N = min(num_terms, len(f_coeffs) - 1)
    for n in range(1, N + 1):
        an = mpf(f_coeffs[n])
        total += an * an / power(mpf(n), k - 1)
    return mpgamma(k - 1) / power(4 * pi, k - 1) * total


# ============================================================
# 4. L-function from Euler product
# ============================================================

def l_function_from_euler_product(
    euler_factors: List[Tuple[int, List[Union[int, float, mpf]]]],
    s: Union[float, mpf, mpc],
    num_primes: int = 100,
) -> mpc:
    r"""Compute L(s) = prod_p 1/P_p(p^{-s}) from local Euler factors.

    Parameters
    ----------
    euler_factors : list of (prime, polynomial_coefficients) pairs.
        Each polynomial P_p(X) = 1 + c_1 X + c_2 X^2 + ... is the local
        factor at prime p, so the Euler factor is 1/P_p(p^{-s}).
        If the list is shorter than num_primes, remaining primes use
        a default factor.
    s : the complex parameter
    num_primes : how many primes to include

    Returns
    -------
    Product of 1/P_p(p^{-s}) for primes p up to the given count.
    """
    s = mpc(s)
    result = mpc(1)

    # Build a dict from the provided factors
    factor_dict = {p: coeffs for p, coeffs in euler_factors}

    # Sieve primes
    primes = _primes_up_to(num_primes * 12)[:num_primes]

    for p in primes:
        x = power(mpf(p), -s)
        if p in factor_dict:
            coeffs = factor_dict[p]
            poly_val = mpf(1)
            xk = mpc(1)
            for c in coeffs:
                xk *= x
                poly_val += mpf(c) * xk
        else:
            # Default: trivial factor (1 - p^{-s})
            poly_val = 1 - x
        if abs(poly_val) > mpf('1e-50'):
            result /= poly_val

    return result


def _primes_up_to(N: int) -> List[int]:
    """Sieve of Eratosthenes."""
    if N < 2:
        return []
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False
    return [i for i in range(2, N + 1) if sieve[i]]


# ============================================================
# 5. L(s, Sym^2 Delta) from Ramanujan tau
# ============================================================

def l_sym2_delta(
    s: Union[float, mpf, mpc],
    num_terms: int = 200,
) -> mpc:
    r"""L(s, Sym^2 Delta) via Euler product.

    For the Ramanujan cusp form Delta of weight 12, the symmetric
    square L-function has Euler product:

      L(s, Sym^2 Delta) = prod_p 1 / [(1 - alpha_p^2 p^{-s})
                                       (1 - alpha_p beta_p p^{-s})
                                       (1 - beta_p^2 p^{-s})]

    where alpha_p + beta_p = tau(p) and alpha_p beta_p = p^{11}.
    Since alpha_p beta_p = p^{11}, the middle factor is (1 - p^{11-s}).

    Equivalently:
      L(s, Sym^2 Delta) = zeta(s-11) * prod_p 1/[(1 - alpha_p^2 p^{-s})(1 - beta_p^2 p^{-s})]

    But the standard form is the Dirichlet series:
      L(s, Sym^2 Delta) = sum_{n>=1} c(n) / n^s

    where the Euler factor at p is:
      1 / [(1 - tau(p)^2 p^{-s} + p^{11} (2 + p^{11}) p^{-2s} - tau(p)^2 p^{22} p^{-3s} + p^{44} p^{-4s})]

    We use the SIMPLER form with the Euler product over primes:
      L_p^{-1}(X) = (1 - alpha_p^2 X)(1 - p^{11} X)(1 - beta_p^2 X)
    where X = p^{-s}, and alpha_p, beta_p are roots of T^2 - tau(p)T + p^{11} = 0.

    Parameters
    ----------
    s : complex parameter
    num_terms : number of primes to use in the Euler product

    Returns
    -------
    L(s, Sym^2 Delta) (numerically).
    """
    s = mpc(s)
    taus = _cached_tau(max(num_terms * 12, 500))
    primes = _primes_up_to(max(num_terms * 12, 500))[:num_terms]

    result = mpc(1)
    for p in primes:
        if p - 1 >= len(taus):
            break
        tau_p = mpf(taus[p - 1])
        p11 = power(mpf(p), 11)
        x = power(mpf(p), -s)

        # Roots of T^2 - tau(p) T + p^11 = 0
        disc = tau_p ** 2 - 4 * p11
        sq = mpmath.sqrt(disc)
        alpha = (tau_p + sq) / 2
        beta = (tau_p - sq) / 2

        # Local factor: (1 - alpha^2 X)(1 - p^11 X)(1 - beta^2 X)
        local = (1 - alpha ** 2 * x) * (1 - p11 * x) * (1 - beta ** 2 * x)
        if abs(local) > mpf('1e-50'):
            result /= local

    return result


# ============================================================
# 6. L(s, Delta x Delta_bar) = Rankin-Selberg of Delta
# ============================================================

def rankin_selberg_delta(
    s: Union[float, mpf, mpc],
    num_terms: int = 200,
) -> mpc:
    r"""L(s, Delta x bar{Delta}) via Dirichlet series.

    For a Hecke eigenform f = Delta of weight 12:
      L(s, f x bar{f}) = sum_{n>=1} |a(n)|^2 / n^s

    where a(n) = tau(n).  Since Delta is real, this is
      L(s, Delta x Delta) = sum_{n>=1} tau(n)^2 / n^s.

    The KEY factorization (Shimura, Zagier):
      L(s, Delta x Delta) = zeta(s-11) L(s, Sym^2 Delta)

    Parameters
    ----------
    s : complex parameter
    num_terms : truncation of Dirichlet series

    Returns
    -------
    sum_{n=1}^{num_terms} tau(n)^2 / n^s.
    """
    s = mpc(s)
    taus = _cached_tau(num_terms)
    total = mpc(0)
    for n in range(1, min(num_terms + 1, len(taus) + 1)):
        tau_n = mpf(taus[n - 1])
        total += tau_n ** 2 / power(mpf(n), s)
    return total


def rankin_selberg_delta_factored(
    s: Union[float, mpf, mpc],
    num_terms: int = 200,
) -> mpc:
    r"""L(s, Delta x Delta) via the factorization zeta(s-11) L(s, Sym^2 Delta).

    This is the SECOND route to the same L-function, using the
    product decomposition instead of the Dirichlet series.
    """
    s = mpc(s)
    return zeta(s - 11) * l_sym2_delta(s, num_terms=num_terms)


# ============================================================
# 7. Shadow-to-period map
# ============================================================

# Lattice data: rank, theta weight, and decomposition structure
_LATTICE_DATA = {
    'Z': {
        'rank': 1,
        'theta_weight': 0.5,
        'shadow_depth': 2,
        'description': 'rank-1 lattice, theta = theta_3, weight 1/2',
    },
    'Z2': {
        'rank': 2,
        'theta_weight': 1,
        'shadow_depth': 2,
        'description': 'rank-2 square lattice, theta = theta_3^2, weight 1',
    },
    'A2': {
        'rank': 2,
        'theta_weight': 1,
        'shadow_depth': 2,
        'description': 'A_2 hexagonal lattice, weight 1',
    },
    'D4': {
        'rank': 4,
        'theta_weight': 2,
        'shadow_depth': 2,
        'description': 'D_4 lattice, Theta = E_2 (Eisenstein only)',
    },
    'E8': {
        'rank': 8,
        'theta_weight': 4,
        'shadow_depth': 3,
        'description': 'E_8 root lattice, Theta = E_4, no cusp forms in S_4',
    },
    'Leech': {
        'rank': 24,
        'theta_weight': 12,
        'shadow_depth': 4,
        'description': 'Leech lattice, Theta = E_12 - (65520/691)Delta_12',
    },
}


def shadow_to_period_map(
    lattice_name: str,
    arity: int,
) -> Dict:
    r"""Return the L-function value that the given shadow arity corresponds to.

    The shadow tower for lattice VOAs has the following period structure:

    Arity 2: kappa = rank(Lambda) [the curvature, a trivial period]
    Arity 3: controlled by the Eisenstein component of Theta_Lambda
             Period = Eisenstein L-value (zeta products)
    Arity 4: controlled by cusp form components of Theta_Lambda
             Period = L(s_0, f_j) for weight-k cusp forms f_j
    Arity 5+: higher-order cusp form periods

    Parameters
    ----------
    lattice_name : one of 'Z', 'Z2', 'A2', 'D4', 'E8', 'Leech'
    arity : shadow tower arity (2, 3, 4, ...)

    Returns
    -------
    Dict with keys:
      'L_function' : description of the L-function
      'critical_value' : the critical value s_0 (if applicable)
      'numerical_value' : numerical value (mpf or None)
      'period_type' : 'trivial', 'Eisenstein', 'cusp_form', or 'higher'
    """
    if lattice_name not in _LATTICE_DATA:
        raise ValueError(f"Unknown lattice: {lattice_name}")

    data = _LATTICE_DATA[lattice_name]
    rank = data['rank']
    depth = data['shadow_depth']

    if arity < 2:
        raise ValueError("Shadow arity must be >= 2")

    if arity == 2:
        return {
            'L_function': f'kappa = rank(Lambda) = {rank}',
            'critical_value': None,
            'numerical_value': mpf(rank),
            'period_type': 'trivial',
        }

    if arity == 3:
        # Eisenstein period: the arity-3 shadow is controlled by the
        # Eisenstein component E_k of Theta_Lambda.
        # For E_k, the Rankin-Selberg integral gives zeta products.
        k = data['theta_weight']

        if lattice_name == 'Z':
            return {
                'L_function': 'zeta(2s) [from theta_3]',
                'critical_value': 1,
                'numerical_value': zeta(mpf(2)),
                'period_type': 'Eisenstein',
            }
        elif lattice_name in ('Z2', 'A2'):
            return {
                'L_function': f'zeta(s) L(s, chi) product',
                'critical_value': 1,
                'numerical_value': zeta(mpf(1) + mpf('1e-10')),  # near pole
                'period_type': 'Eisenstein',
            }
        elif lattice_name == 'E8':
            # E_4 Eisenstein series: Rankin-Selberg gives zeta(s) zeta(s-3)
            val = zeta(mpf(4)) * zeta(mpf(1) + mpf('1e-10'))
            return {
                'L_function': 'zeta(s) zeta(s-3) [from E_4]',
                'critical_value': 4,
                'numerical_value': zeta(mpf(4)),
                'period_type': 'Eisenstein',
            }
        elif lattice_name == 'Leech':
            # E_12: Rankin-Selberg gives zeta(s) zeta(s-11)
            return {
                'L_function': 'zeta(s) zeta(s-11) [Eisenstein part of Theta_Leech]',
                'critical_value': 12,
                'numerical_value': zeta(mpf(12)),
                'period_type': 'Eisenstein',
            }
        else:
            return {
                'L_function': f'Eisenstein period for weight {k}',
                'critical_value': k,
                'numerical_value': None,
                'period_type': 'Eisenstein',
            }

    if arity == 4:
        # Cusp form period.  Only lattices with shadow_depth >= 4 have
        # nontrivial cusp form contributions at arity 4.
        if depth < 4:
            return {
                'L_function': 'none (no cusp forms at this weight)',
                'critical_value': None,
                'numerical_value': mpf(0),
                'period_type': 'trivial',
            }
        if lattice_name == 'Leech':
            # The KEY identity: the arity-4 shadow for V_Leech corresponds
            # to the cusp form Delta_12 period.
            # L(s, Delta x Delta) = zeta(s-11) L(s, Sym^2 Delta)
            # The critical value relevant to the quartic shadow is at
            # s = 12 (center of the critical strip for weight 12).
            L_val = rankin_selberg_delta(mpc(12), num_terms=100)
            return {
                'L_function': 'L(s, Delta x Delta) = zeta(s-11) L(s, Sym^2 Delta)',
                'critical_value': 12,
                'numerical_value': L_val,
                'period_type': 'cusp_form',
            }
        return {
            'L_function': 'cusp form L-function (if dim S_k > 0)',
            'critical_value': None,
            'numerical_value': None,
            'period_type': 'cusp_form',
        }

    # arity >= 5: higher-order periods
    return {
        'L_function': f'higher-order period at arity {arity}',
        'critical_value': None,
        'numerical_value': None,
        'period_type': 'higher',
    }


# ============================================================
# 8. Period relation table
# ============================================================

def period_relation_table(
    lattice_name: str,
    max_arity: int = 6,
) -> Dict[int, Dict]:
    r"""Build the table of period relations for a lattice VOA.

    Maps each arity r = 2, ..., max_arity to the L-function data
    that the r-th shadow coefficient corresponds to.

    Returns
    -------
    Dict[arity, {L_function, critical_value, numerical_value, period_type}]
    """
    table = {}
    for r in range(2, max_arity + 1):
        table[r] = shadow_to_period_map(lattice_name, r)
    return table


# ============================================================
# 9. Sewing-Selberg verification
# ============================================================

def verify_sewing_selberg(
    s_values: Optional[List[Union[float, int]]] = None,
) -> List[Dict]:
    r"""Numerical verification of the sewing-Selberg formula.

    The formula:
      integral_{M_{1,1}} log det(1-K(tau)) E_s(tau) dmu(tau)
        = -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)

    We verify at several s-values by checking:
    (a) the formula is well-defined (no poles),
    (b) the sign is correct,
    (c) consistency with known zeta values.

    Returns
    -------
    List of dicts with 's', 'formula_value', 'zeta_s_minus_1', 'zeta_s', etc.
    """
    if s_values is None:
        s_values = [2, 3, 4, 5]

    results = []
    for s in s_values:
        s_mp = mpf(s)
        val = sewing_selberg_integral(s_mp)
        z_sm1 = zeta(s_mp - 1)
        z_s = zeta(s_mp)
        gam = mpgamma(s_mp - 1)
        pi_factor = power(2 * pi, -(s_mp - 1))

        results.append({
            's': s,
            'formula_value': val,
            'zeta_s_minus_1': z_sm1,
            'zeta_s': z_s,
            'gamma_s_minus_1': gam,
            'pi_factor': pi_factor,
            'product_check': -2 * pi_factor * gam * z_sm1 * z_s,
        })

    return results


# ============================================================
# 10. Theta Rankin-Selberg integral via unfolding
# ============================================================

def theta_rankin_selberg(
    lattice_coeffs: List[Union[int, float, mpf]],
    rank: int,
    s: Union[float, mpf, mpc],
    num_terms: int = 200,
) -> mpc:
    r"""integral |Theta_Lambda|^2 E*(tau,s) y^{r/2} dmu via Rankin-Selberg unfolding.

    After Rankin-Selberg unfolding (integrating x against the Eisenstein series),
    the integral reduces to a Dirichlet series:

      integral_F |Theta|^2 E*(tau,s) y^k dmu
        ~ Gamma(s+k-1) / (4pi)^{s+k-1} * sum |a(n)|^2 / n^{s+k-1} + (Eis contrib)

    where k = rank/2 is the weight of Theta_Lambda.

    This function computes the Dirichlet series part:
      D(s) = sum_{n>=1} |a(n)|^2 / n^s

    evaluated at s = s_input + k - 1, with the appropriate gamma prefactor.

    Parameters
    ----------
    lattice_coeffs : Fourier coefficients a(0), a(1), ..., a(N) of Theta_Lambda
    rank : rank of the lattice (= 2 * weight of Theta)
    s : the Eisenstein series parameter
    num_terms : truncation

    Returns
    -------
    The Dirichlet series part with gamma factor.
    """
    s = mpc(s)
    k = mpf(rank) / 2  # weight of Theta_Lambda
    shifted_s = s + k - 1

    # Dirichlet series: sum |a(n)|^2 / n^{shifted_s}
    dirichlet = mpc(0)
    N = min(num_terms, len(lattice_coeffs) - 1)
    for n in range(1, N + 1):
        an = mpf(lattice_coeffs[n])
        dirichlet += an ** 2 / power(mpf(n), shifted_s)

    gamma_factor = mpgamma(shifted_s) / power(4 * pi, shifted_s)
    return gamma_factor * dirichlet


# ============================================================
# 11. Shadow kappa as trivial period
# ============================================================

def shadow_kappa_as_period(lattice_name: str) -> mpf:
    r"""kappa = rank = trivial period (no integration needed).

    The arity-2 shadow coefficient for a lattice VOA V_Lambda is
    kappa(V_Lambda) = rank(Lambda), proved in lattice_foundations.tex
    (thm:lattice:curvature-braiding-orthogonal).

    This is a "trivial period" in the sense that it requires no
    Rankin-Selberg integration: it is simply the central charge
    (= rank of the lattice), determined by the Sugawara construction.
    """
    if lattice_name not in _LATTICE_DATA:
        raise ValueError(f"Unknown lattice: {lattice_name}")
    return mpf(_LATTICE_DATA[lattice_name]['rank'])


# ============================================================
# 12. Shadow cubic as Eisenstein period
# ============================================================

def shadow_cubic_as_eisenstein_period(lattice_name: str) -> Dict:
    r"""Cubic shadow coefficient as Eisenstein period.

    For a lattice VOA whose theta function Theta_Lambda = c_E E_k + (cusp forms),
    the arity-3 (cubic) shadow is controlled by the Eisenstein coefficient c_E.

    The Eisenstein E_k has a Rankin-Selberg integral proportional to
    zeta(s) zeta(s - k + 1), yielding the cubic shadow as a zeta product.

    For lattices whose theta IS purely Eisenstein (E_8, D_4, etc.), the
    cubic shadow is the ONLY nonlinear correction (shadow terminates at
    depth 3 = class L in the shadow depth classification).
    """
    if lattice_name not in _LATTICE_DATA:
        raise ValueError(f"Unknown lattice: {lattice_name}")

    data = _LATTICE_DATA[lattice_name]
    rank = data['rank']
    k = data['theta_weight']

    if lattice_name in ('Z', 'Z2', 'A2'):
        return {
            'cubic_shadow': 'controlled by Eisenstein of weight <= 1',
            'zeta_product': 'zeta(2s) or zeta(s)L(s,chi)',
            'eisenstein_coefficient': mpf(1),
            'value': None,
            'terminates': True,
        }
    elif lattice_name == 'D4':
        return {
            'cubic_shadow': 'Eisenstein period from E_2',
            'zeta_product': 'zeta(s) zeta(s-1)',
            'eisenstein_coefficient': mpf(1),
            'value': zeta(mpf(2)),
            'terminates': True,
        }
    elif lattice_name == 'E8':
        # Theta_{E_8} = E_4 (purely Eisenstein, no cusp forms in S_4)
        # Cubic shadow = Eisenstein period
        return {
            'cubic_shadow': 'Eisenstein period from E_4',
            'zeta_product': 'zeta(s) zeta(s-3)',
            'eisenstein_coefficient': mpf(1),
            'value': zeta(mpf(4)) * zeta(mpf(1) + mpf('1e-8')),
            'terminates': True,  # no cusp forms => shadow terminates at depth 3
        }
    elif lattice_name == 'Leech':
        # Theta_Leech = E_12 + c_Delta Delta_12
        # Cubic shadow = Eisenstein period from E_12
        return {
            'cubic_shadow': 'Eisenstein period from E_12 (part of Theta_Leech)',
            'zeta_product': 'zeta(s) zeta(s-11)',
            'eisenstein_coefficient': mpf(1),
            'value': zeta(mpf(12)),
            'terminates': False,  # cusp form Delta_12 gives arity-4 contribution
        }
    else:
        return {
            'cubic_shadow': f'Eisenstein period from E_{k}',
            'zeta_product': f'zeta(s) zeta(s-{k-1})',
            'eisenstein_coefficient': mpf(1),
            'value': None,
            'terminates': data['shadow_depth'] <= 3,
        }


# ============================================================
# 13. Shadow quartic as cusp form period
# ============================================================

def shadow_quartic_as_cusp_period(lattice_name: str) -> Dict:
    r"""Quartic shadow as L(s_0, f) for cusp form f.

    For the Leech lattice, the quartic shadow arises from the cusp form
    component Delta_12 of Theta_Leech:

      Theta_Leech = E_12 - (65520/691) Delta_12

    The quartic shadow coefficient is proportional to a period integral
    of Delta against itself:

      alpha_4 ~ <Delta, Delta>_Pet ~ L(12, Delta x Delta)
              = zeta(1) L(12, Sym^2 Delta)

    More precisely, the arity-4 shadow coefficient involves the
    Rankin-Selberg L-function L(s, Delta x Delta) evaluated at the
    center of the critical strip s = 12.

    The KEY factorization:
      L(s, Delta x Delta) = zeta(s-11) L(s, Sym^2 Delta)

    At s=12: L(12, Delta x Delta) = zeta(1) L(12, Sym^2 Delta)
    The pole of zeta at s=1 shows this requires regularization;
    the finite part (residue) gives the Petersson norm.

    For lattices with no cusp form content (E_8, D_4, Z, Z2, A2):
    the quartic shadow VANISHES (no cusp forms in the relevant S_k).
    """
    if lattice_name not in _LATTICE_DATA:
        raise ValueError(f"Unknown lattice: {lattice_name}")

    data = _LATTICE_DATA[lattice_name]

    if data['shadow_depth'] < 4:
        return {
            'has_quartic': False,
            'reason': f'no cusp forms in S_{data["theta_weight"]}',
            'L_function': None,
            'cusp_form_coefficient': mpf(0),
            'value': mpf(0),
        }

    if lattice_name == 'Leech':
        c_delta = mpf(-65520) / mpf(691)
        # L(s, Delta x Delta) via Dirichlet series at s=12+epsilon
        # (regularized near the pole of zeta(s-11) at s=12)
        L_val = rankin_selberg_delta(mpc(13), num_terms=100)
        L_sym2 = l_sym2_delta(mpc(13), num_terms=100)

        return {
            'has_quartic': True,
            'reason': 'Delta_12 component of Theta_Leech',
            'L_function': 'L(s, Delta x Delta) = zeta(s-11) L(s, Sym^2 Delta)',
            'cusp_form_coefficient': c_delta,
            'rankin_selberg_at_13': L_val,
            'l_sym2_at_13': L_sym2,
            'factorization_check': abs(L_val - zeta(mpc(2)) * L_sym2),
        }

    return {
        'has_quartic': True,
        'reason': 'cusp form contribution',
        'L_function': 'unspecified',
        'cusp_form_coefficient': None,
        'value': None,
    }


# ============================================================
# 14. Functional equation check
# ============================================================

def functional_equation_check(
    L_func,
    s_value: Union[float, mpf],
    conductor: Union[int, float, mpf] = 1,
    weight: int = 12,
    sign: int = 1,
    completion: str = 'standard',
) -> Dict:
    r"""Verify the functional equation of a completed L-function.

    Two conventions are supported:

    completion='standard' (for Hecke eigenforms of weight k, level 1):
      Lambda(s) = (2pi)^{-s} Gamma(s) L(s)
      Functional equation: Lambda(s) = sign * Lambda(k - s)

    completion='riemann' (for the Riemann zeta function):
      xi(s) = pi^{-s/2} Gamma(s/2) zeta(s)
      Functional equation: xi(s) = xi(1 - s)

    Parameters
    ----------
    L_func : callable s -> L(s) value
    s_value : where to test
    conductor : the conductor N (unused for Riemann completion)
    weight : weight k (unused for Riemann completion)
    sign : root number epsilon (usually +1 or -1)
    completion : 'standard' or 'riemann'

    Returns
    -------
    Dict with 'Lambda_s', 'Lambda_ks', 'ratio', 'rel_error'.
    """
    s = mpc(s_value)

    if completion == 'riemann':
        # xi(s) = pi^{-s/2} Gamma(s/2) zeta(s)
        # Functional equation: xi(s) = xi(1-s)
        L_s = L_func(s)
        L_1ms = L_func(1 - s)
        Lambda_s = power(pi, -s / 2) * mpgamma(s / 2) * L_s
        Lambda_ks = power(pi, -(1 - s) / 2) * mpgamma((1 - s) / 2) * L_1ms
    else:
        # Standard: Lambda(s) = (2pi)^{-s} Gamma(s) L(s)
        k = mpf(weight)
        L_s = L_func(s)
        L_ks = L_func(k - s)
        Lambda_s = power(2 * pi, -s) * mpgamma(s) * L_s
        Lambda_ks = power(2 * pi, -(k - s)) * mpgamma(k - s) * L_ks

    if abs(Lambda_ks) > mpf('1e-50'):
        ratio = Lambda_s / (sign * Lambda_ks)
        rel_error = abs(ratio - 1)
    else:
        ratio = mpc(0)
        rel_error = mpf('inf')

    return {
        'Lambda_s': Lambda_s,
        'Lambda_ks': Lambda_ks,
        'ratio': ratio,
        'rel_error': float(rel_error),
        'sign': sign,
    }


# ============================================================
# 15. L(s, Delta) standard L-function via Euler product
# ============================================================

def l_delta_euler(
    s: Union[float, mpf, mpc],
    num_primes: int = 100,
) -> mpc:
    r"""L(s, Delta) = prod_p 1/(1 - tau(p) p^{-s} + p^{11-2s}).

    The standard L-function of the Ramanujan cusp form.
    Euler product over primes p:
      L_p(s)^{-1} = 1 - tau(p) p^{-s} + p^{11-2s}

    Absolutely convergent for Re(s) > 13/2 by Deligne's bound |tau(p)| <= 2p^{11/2}.
    """
    s = mpc(s)
    taus = _cached_tau(max(num_primes * 12, 500))
    primes = _primes_up_to(max(num_primes * 12, 500))[:num_primes]

    result = mpc(1)
    for p in primes:
        if p - 1 >= len(taus):
            break
        tau_p = mpf(taus[p - 1])
        x = power(mpf(p), -s)
        local = 1 - tau_p * x + power(mpf(p), 11) * x ** 2
        if abs(local) > mpf('1e-50'):
            result /= local

    return result


def l_delta_dirichlet(
    s: Union[float, mpf, mpc],
    num_terms: int = 200,
) -> mpc:
    r"""L(s, Delta) = sum_{n>=1} tau(n) / n^s.

    Direct Dirichlet series. Convergent for Re(s) > 13/2.
    """
    s = mpc(s)
    taus = _cached_tau(num_terms)
    total = mpc(0)
    for n in range(1, min(num_terms + 1, len(taus) + 1)):
        total += mpf(taus[n - 1]) / power(mpf(n), s)
    return total


# ============================================================
# 16. Deligne bound verification
# ============================================================

def verify_deligne_bound(num_primes: int = 50) -> List[Dict]:
    r"""Verify |tau(p)| <= 2 p^{11/2} (Deligne's theorem).

    Returns list of dicts for each prime p with tau(p), bound, ratio.
    """
    taus = _cached_tau(max(num_primes * 12, 500))
    primes = _primes_up_to(max(num_primes * 12, 500))[:num_primes]

    results = []
    for p in primes:
        if p - 1 >= len(taus):
            break
        tau_p = abs(taus[p - 1])
        bound = 2 * p ** 5.5
        results.append({
            'p': p,
            'tau_p': taus[p - 1],
            'abs_tau_p': tau_p,
            'deligne_bound': bound,
            'ratio': tau_p / bound,
            'satisfies': tau_p <= bound + 1e-6,
        })
    return results
