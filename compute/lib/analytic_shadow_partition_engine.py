r"""Analytic shadow partition function: the non-perturbative completion.

MATHEMATICAL FRAMEWORK
======================

The shadow generating function Z^sh(A) = exp(sum_g hbar^{2g} F_g) is a
PERTURBATIVE series in the genus expansion parameter hbar.  The analytic
shadow partition function Z^an(A) is the NON-PERTURBATIVE object obtained
from the sewing envelope A^sew.

The sewing envelope A^sew is the Hausdorff completion of A for the
all-amplitude seminorm topology (raeeznotes89).  The HS-sewing condition
(thm:general-hs-sewing) ensures convergence for the entire standard
landscape: polynomial OPE growth + subexponential sector growth implies
convergence at all genera.

GENUS-1 EXACT PARTITION FUNCTIONS:

  Heisenberg at level k:
    Z_1^{an}(H_k)(tau) = 1/eta(tau)^k = q^{-k/24} / prod_{n>=1}(1-q^n)^k

  Affine KM g-hat_k:
    Z_1^{an}(g_k)(tau) = prod_{n>=1} (1-q^n)^{-dim(g)}
    (vacuum module at generic level)

  Virasoro at central charge c:
    Z_1^{an}(Vir_c)(tau) = chi_0(tau), the vacuum character

  Minimal model M(p,q):
    Z_1^{an}(tau) = chi_{1,1}(tau) = sum (modular-function formulae)

SHADOW vs EXACT DISCREPANCY:

  Delta_g(A) = log Z_g^{an} - log Z_g^{sh}

  For class G (Heisenberg): the shadow expansion IS the full log partition
  function at the scalar level.  The Fourier coefficients of log(1/eta^k)
  beyond the leading q^{-k/24} are the non-perturbative corrections.

FREDHOLM DETERMINANT STRUCTURE:

  The one-particle sewing reduction (thm:heisenberg-one-particle-sewing):
    Z_g(H_k) = det(1 - K_g)^{-k}
  where K_g is the genus-g Bergman sewing kernel.

  At genus 1: K_1 = diag(q, q^2, q^3, ...) and
    det(1 - K_1) = prod_{n>=1}(1 - q^n)

MODULAR PROPERTIES (AP15: holomorphic vs quasi-modular):

  Z_1^{an} transforms under SL(2,Z).  The transformation weight depends
  on the algebra:
    - Heisenberg rank k: weight -k/2 (eta^{-k} has modular weight -k/2)
    - Affine KM: integrable-rep character, modular matrix S_{ij}
    - Virasoro: vacuum character, weight 0 under modular kernel

CONVENTIONS:
  - q = e^{2 pi i tau}
  - kappa(A) = modular characteristic (NOT c; AP20/AP39)
  - kappa(Heisenberg level k) = k (AP39: kappa != c/2 in general)
  - kappa(Virasoro at c) = c/2
  - kappa(affine KM g_k) = dim(g)(k+h^v)/(2h^v)
  - eta(tau) = q^{1/24} prod(1-q^n) (AP46: the q^{1/24} is NOT optional)
  - E_2*(tau) is quasi-modular, NOT holomorphic (AP15)

Ground truth:
  thm:general-hs-sewing, thm:heisenberg-sewing,
  thm:heisenberg-one-particle-sewing, thm:shadow-double-convergence,
  prop:genus-expansion-convergence, fredholm_sewing_engine.py,
  affine_km_sewing_engine.py, shadow_pf_convergence.py,
  shadow_partition_function.py, concordance.tex (MC5).
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

from sympy import Rational, bernoulli, factorial, pi as sym_pi

from compute.lib.utils import lambda_fp, F_g


# ===========================================================================
# Constants
# ===========================================================================

PI = math.pi
TWO_PI = 2 * PI
TWO_PI_SQ = TWO_PI ** 2


# ===========================================================================
# Section 1: Dedekind eta and basic q-series
# ===========================================================================

@lru_cache(maxsize=512)
def _partitions(n: int) -> int:
    """Number of integer partitions of n."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    k = 1
    while True:
        w1 = n - k * (3 * k - 1) // 2
        w2 = n - k * (3 * k + 1) // 2
        if w1 < 0 and w2 < 0:
            break
        sign = (-1) ** (k + 1)
        if w1 >= 0:
            total += sign * _partitions(w1)
        if w2 >= 0:
            total += sign * _partitions(w2)
        k += 1
    return total


def colored_partitions(n: int, colors: int) -> int:
    """Coefficient of q^n in prod_{m>=1}(1-q^m)^{-colors}."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    if colors == 1:
        return _partitions(n)
    dims = [0] * (n + 1)
    dims[0] = 1
    for m in range(1, n + 1):
        for _ in range(colors):
            for j in range(m, n + 1):
                dims[j] += dims[j - m]
    return dims[n]


def eta_product(q: complex, N: int = 300) -> complex:
    r"""prod_{n>=1}(1-q^n).

    Note (AP46): eta(tau) = q^{1/24} * this product.
    The q^{1/24} prefactor is NOT optional.
    """
    prod_val = complex(1.0, 0.0)
    for n in range(1, N + 1):
        qn = q ** n
        if abs(qn) < 1e-50:
            break
        prod_val *= (1.0 - qn)
    return prod_val


def eta_function(tau: complex, N: int = 300) -> complex:
    r"""Dedekind eta: eta(tau) = q^{1/24} prod_{n>=1}(1-q^n).

    AP46: the q^{1/24} prefactor is NOT optional.
    """
    q = cmath.exp(2j * PI * tau)
    return q ** (1.0 / 24.0) * eta_product(q, N)


def eta_function_from_q(q: complex, N: int = 300) -> complex:
    r"""eta(tau) given q = e^{2*pi*i*tau}."""
    return q ** (1.0 / 24.0) * eta_product(q, N)


def log_eta(tau: complex, N: int = 300) -> complex:
    r"""log eta(tau) = (2*pi*i*tau)/24 + sum_{n>=1} log(1-q^n).

    Returns the principal branch of the logarithm.
    """
    q = cmath.exp(2j * PI * tau)
    result = 2j * PI * tau / 24.0
    for n in range(1, N + 1):
        qn = q ** n
        if abs(qn) < 1e-50:
            break
        result += cmath.log(1.0 - qn)
    return result


# ===========================================================================
# Section 2: Jacobi theta functions (for minimal model characters)
# ===========================================================================

def theta_3(tau: complex, N: int = 200) -> complex:
    r"""theta_3(tau) = sum_{n in Z} e^{pi*i*tau*n^2}.

    Standard convention uses q_{1/2} = e^{pi*i*tau}, so
    theta_3 = sum_{n in Z} q_{1/2}^{n^2}.

    Note: this is NOT q = e^{2*pi*i*tau}. The Jacobi theta functions
    use the HALF-period nome q_{1/2} = e^{pi*i*tau}.
    """
    q_half = cmath.exp(1j * PI * tau)
    total = complex(1.0, 0.0)  # n=0 term
    for n in range(1, N + 1):
        qn2 = q_half ** (n * n)
        if abs(qn2) < 1e-50:
            break
        total += 2 * qn2  # n and -n both contribute
    return total


def theta_4(tau: complex, N: int = 200) -> complex:
    r"""theta_4(tau) = sum_{n in Z} (-1)^n e^{pi*i*tau*n^2}."""
    q_half = cmath.exp(1j * PI * tau)
    total = complex(1.0, 0.0)
    for n in range(1, N + 1):
        qn2 = q_half ** (n * n)
        if abs(qn2) < 1e-50:
            break
        total += 2 * ((-1) ** n) * qn2
    return total


def theta_2(tau: complex, N: int = 200) -> complex:
    r"""theta_2(tau) = 2 q_{1/2}^{1/4} sum_{n>=0} q_{1/2}^{n(n+1)}.

    Uses q_{1/2} = e^{pi*i*tau}.
    """
    q_half = cmath.exp(1j * PI * tau)
    total = complex(0.0, 0.0)
    for n in range(0, N + 1):
        qpow = q_half ** (n * (n + 1))
        if abs(qpow) < 1e-50:
            break
        total += qpow
    return 2 * q_half ** 0.25 * total


# ===========================================================================
# Section 3: Kappa values (modular characteristic, AP1/AP39)
# ===========================================================================

def kappa_heisenberg(k: float) -> float:
    r"""kappa(H_k) = k.

    AP39: kappa != c/2 in general.  For Heisenberg: c = k, kappa = k.
    Wait: kappa(H_k) = k.  Verification: F_1 = kappa/24 = k/24.
    The genus-1 partition function is 1/eta^k with leading behavior
    q^{-k/24}, giving F_1 = k/24.  Correct.
    """
    return k


def kappa_virasoro(c: float) -> float:
    r"""kappa(Vir_c) = c/2.

    This is the ONE case where kappa = c/2 holds (AP39).
    """
    return c / 2.0


def kappa_affine_km(dim_g: int, h_dual: int, level: float) -> float:
    r"""kappa(g-hat_k) = dim(g) * (k + h^v) / (2 * h^v).

    AP1/AP39: this is NOT c/2.
    """
    return dim_g * (level + h_dual) / (2.0 * h_dual)


# ===========================================================================
# Section 4: Genus-1 analytic partition functions
# ===========================================================================

def heisenberg_partition_genus1(tau: complex, k: int = 1,
                                 N: int = 300) -> complex:
    r"""Z_1^{an}(H_k)(tau) = 1/eta(tau)^k.

    = q^{-k/24} / prod_{n>=1}(1-q^n)^k.

    The shadow expansion at the scalar level:
      log Z_1^{sh} = F_1 = kappa/24 = k/24
    captures ONLY the q^{-k/24} leading behavior.  The full partition
    function 1/eta^k has ALL Fourier coefficients.
    """
    eta_val = eta_function(tau, N)
    if abs(eta_val) < 1e-300:
        return complex(float('inf'), 0.0)
    return eta_val ** (-k)


def heisenberg_partition_genus1_from_q(q: complex, k: int = 1,
                                        N: int = 300) -> complex:
    r"""Same as above but takes q = e^{2*pi*i*tau} directly."""
    eta_val = eta_function_from_q(q, N)
    if abs(eta_val) < 1e-300:
        return complex(float('inf'), 0.0)
    return eta_val ** (-k)


def affine_km_partition_genus1(tau: complex, dim_g: int,
                                N: int = 300) -> complex:
    r"""Z_1^{an}(g-hat_k)(tau) = prod_{n>=1}(1-q^n)^{-dim(g)}.

    At the vacuum module level for generic k, the partition function
    is dim(g) copies of the Heisenberg partition function.

    Note: this OMITS the q^{-c/24} prefactor (we compute the product
    part only).  The full character with prefactor is:
      chi_0(tau) = q^{-c/24} * prod(1-q^n)^{-dim(g)}
    """
    q = cmath.exp(2j * PI * tau)
    prod_val = eta_product(q, N)
    if abs(prod_val) < 1e-300:
        return complex(float('inf'), 0.0)
    return prod_val ** (-dim_g)


def virasoro_vacuum_character_generic(tau: complex, c: float,
                                       N: int = 300) -> complex:
    r"""Vacuum character chi_0(tau) for Virasoro at generic c >= 1.

    chi_0(tau) = q^{-c/24} * prod_{n>=2}(1-q^n)^{-1}
               = q^{-c/24} * (1-q)^{-1 -> wrong, this is for Verma module}

    For the Verma module (no null vectors, generic c):
      chi_0^{Verma}(tau) = q^{-c/24} / prod_{n>=1}(1-q^n)
                         = q^{-(c-1)/24} / eta(tau)

    The (c-1)/24 shift: the Virasoro generators L_{-n} for n >= 1
    create a Fock space with generating function 1/prod(1-q^n).
    But L_0|0> = 0 and the true vacuum character of the irreducible
    module EXCLUDES the null vector at level 1 (from L_{-1}|0> = 0):
      chi_0^{irred}(tau) = q^{-c/24} * (1-q) / prod_{n>=1}(1-q^n)
                         = q^{-c/24} * prod_{n>=2}(1-q^n)^{-1}

    For c >= 25 (no further null vectors at generic c):
      chi_0(tau) = q^{-c/24} * (1-q) * prod_{n>=1}(1-q^n)^{-1}
    """
    q = cmath.exp(2j * PI * tau)
    q_prefactor = q ** (-c / 24.0)

    # prod_{n>=1}(1-q^n)^{-1}
    prod_inv = 1.0 / eta_product(q, N)

    # Null vector subtraction: L_{-1}|0> = 0 removes one state at level 1
    # chi_0 = q^{-c/24} * (1 - q) * prod_{n>=1}(1-q^n)^{-1}
    null_correction = (1.0 - q)

    return q_prefactor * null_correction * prod_inv


def ising_vacuum_character(tau: complex, N: int = 200) -> complex:
    r"""Vacuum character chi_{1,1} for the Ising model (c = 1/2).

    For the minimal model M(3,4), the vacuum character is:
      chi_{1,1}(tau) = (1/2)(sqrt(theta_3(tau)/eta(tau)) + sqrt(theta_4(tau)/eta(tau)))

    More precisely, the Rocha-Caridi formula:
      chi_{r,s}^{(p,p')} = (1/eta) sum_{n in Z} (q^{a_{+,n}} - q^{a_{-,n}})
    where a_{+/-,n} = ((2pp'n + pr - p's)^2 - (p-p')^2) / (4pp').

    For (p,p') = (3,4) and (r,s) = (1,1):
      chi_{1,1} = q^{-1/48} (1/eta) sum_{n} (q^{(24n+1)^2/48} - q^{(24n+7)^2/48})

    Simpler formula via theta functions:
      chi_{1,1} = (1/2)(sqrt(theta_3/eta) + sqrt(theta_4/eta))
    """
    eta_val = eta_function(tau, N)
    th3 = theta_3(tau, N)
    th4 = theta_4(tau, N)

    if abs(eta_val) < 1e-300:
        return complex(float('inf'), 0.0)

    return 0.5 * (cmath.sqrt(th3 / eta_val) + cmath.sqrt(th4 / eta_val))


def minimal_model_vacuum_character(p: int, pp: int, tau: complex,
                                    N: int = 200) -> complex:
    r"""Vacuum character chi_{1,1} for minimal model M(p, p').

    Central charge: c = 1 - 6(p - p')^2/(p*p').

    Uses the Rocha-Caridi formula:
      chi_{1,1} = (1/eta(tau)) sum_{n in Z}
                  (q^{((2pp'n + p - p')^2 - (p-p')^2)/(4pp')}
                   - q^{((2pp'n + p + p')^2 - (p-p')^2)/(4pp')})

    Valid for p < p', gcd(p, p') = 1.
    """
    if p >= pp:
        raise ValueError(f"Need p < p', got p={p}, p'={pp}")

    c = 1.0 - 6.0 * (p - pp) ** 2 / (p * pp)
    q = cmath.exp(2j * PI * tau)
    eta_val = eta_function(tau, N)

    if abs(eta_val) < 1e-300:
        return complex(float('inf'), 0.0)

    total = complex(0.0, 0.0)
    for n in range(-N, N + 1):
        # a_{+,n}: r=1, s=1
        num_plus = (2 * p * pp * n + p - pp) ** 2 - (p - pp) ** 2
        exp_plus = num_plus / (4.0 * p * pp)

        num_minus = (2 * p * pp * n + p + pp) ** 2 - (p - pp) ** 2
        exp_minus = num_minus / (4.0 * p * pp)

        q_plus = q ** exp_plus
        q_minus = q ** exp_minus

        if abs(q_plus) < 1e-50 and abs(q_minus) < 1e-50 and n > 0:
            break

        total += q_plus - q_minus

    return total / eta_val


# ===========================================================================
# Section 5: Shadow expansion (perturbative)
# ===========================================================================

def shadow_free_energy(kappa_val: float, max_genus: int = 30) -> Dict[int, float]:
    r"""F_g^{scalar}(A) = kappa * lambda_g^{FP} for g = 1, ..., max_genus.

    The scalar (arity-2) shadow contribution.  This is the perturbative
    shadow expansion.
    """
    result = {}
    for g in range(1, max_genus + 1):
        result[g] = float(F_g(Rational(kappa_val).limit_denominator(10**9), g))
    return result


def shadow_log_partition(kappa_val: float, hbar: float = 1.0,
                          max_genus: int = 50) -> float:
    r"""log Z^{sh} = sum_{g>=1} F_g hbar^{2g} = kappa * (A-hat(i*hbar) - 1).

    The closed form is kappa * ((hbar/2)/sin(hbar/2) - 1).
    Valid for |hbar| < 2*pi.
    """
    if abs(hbar) < 1e-15:
        return 0.0
    return kappa_val * ((hbar / 2.0) / math.sin(hbar / 2.0) - 1.0)


def shadow_log_partition_series(kappa_val: float, hbar: float = 1.0,
                                 max_genus: int = 50) -> float:
    r"""Partial sum of the shadow genus series."""
    total = 0.0
    for g in range(1, max_genus + 1):
        fg = float(F_g(Rational(kappa_val).limit_denominator(10**9), g))
        total += fg * hbar ** (2 * g)
    return total


# ===========================================================================
# Section 6: Shadow vs exact discrepancy
# ===========================================================================

@dataclass
class DiscrepancyResult:
    """Shadow vs exact discrepancy at genus g."""
    algebra: str
    genus: int
    log_Z_an: complex
    log_Z_sh: float
    discrepancy: complex  # log_Z_an - log_Z_sh
    relative_discrepancy: float
    description: str = ""


def genus1_discrepancy_heisenberg(tau: complex, k: int = 1,
                                    N: int = 300) -> DiscrepancyResult:
    r"""Discrepancy Delta_1(H_k) = log Z_1^{an} - log Z_1^{sh}.

    Z_1^{an} = 1/eta(tau)^k, so log Z_1^{an} = -k * log eta(tau).
    Z_1^{sh} at hbar=1: F_1 = kappa/24 = k/24.

    The discrepancy is:
      Delta_1 = -k * log eta(tau) - k/24
              = -k * [log eta(tau) + 1/24]
              = -k * sum_{n>=1} log(1-q^n)  - k*(2*pi*i*tau)/24 - k/24

    At tau = it (purely imaginary), q = e^{-2*pi*t}:
      log Z_1^{an} = -k * ((2*pi*i*tau)/24 + sum log(1-q^n))
                    = k*pi*t/12 - k * sum log(1-e^{-2*pi*n*t})

    For large t (q -> 0): the sum vanishes and log Z_1^{an} ~ k*pi*t/12.
    The shadow expansion F_1 = k/24 captures the COEFFICIENT of log q = 2*pi*i*tau,
    not the full tau-dependent expression.

    The correct comparison: the shadow PF at the scalar level is tau-INDEPENDENT.
    log Z_1^{sh} = F_1 = k/24 is a constant.  The analytic partition function
    log Z_1^{an}(tau) is a function of tau.  The "discrepancy" is the tau-dependent
    part plus the higher Fourier modes.
    """
    log_Z_an = -k * log_eta(tau, N)
    log_Z_sh = float(k) / 24.0

    disc = log_Z_an - log_Z_sh
    rel = abs(disc) / max(abs(log_Z_an), 1e-30)

    return DiscrepancyResult(
        algebra=f"Heisenberg_k={k}",
        genus=1,
        log_Z_an=log_Z_an,
        log_Z_sh=log_Z_sh,
        discrepancy=disc,
        relative_discrepancy=rel,
        description=(
            "For Heisenberg, the shadow expansion captures ONLY the leading "
            "log q coefficient.  The full 1/eta^k contains all Fourier modes."
        ),
    )


def genus1_discrepancy_virasoro(tau: complex, c: float,
                                 N: int = 300) -> DiscrepancyResult:
    r"""Discrepancy for Virasoro at generic c.

    Z_1^{an}(Vir_c) = chi_0(tau) = q^{-c/24} (1-q) prod_{n>=1}(1-q^n)^{-1}
    log Z_1^{sh} = kappa/24 = c/48

    Note: the vacuum character has log chi_0 = -c/24 * log q + log(1-q) - sum log(1-q^n)
    """
    Z_an = virasoro_vacuum_character_generic(tau, c, N)

    if abs(Z_an) < 1e-300:
        return DiscrepancyResult(
            algebra=f"Virasoro_c={c}",
            genus=1,
            log_Z_an=complex(float('-inf'), 0.0),
            log_Z_sh=c / 48.0,
            discrepancy=complex(float('-inf'), 0.0),
            relative_discrepancy=float('inf'),
        )

    log_Z_an = cmath.log(Z_an)
    log_Z_sh = c / 48.0

    disc = log_Z_an - log_Z_sh
    rel = abs(disc) / max(abs(log_Z_an), 1e-30)

    return DiscrepancyResult(
        algebra=f"Virasoro_c={c}",
        genus=1,
        log_Z_an=log_Z_an,
        log_Z_sh=log_Z_sh,
        discrepancy=disc,
        relative_discrepancy=rel,
        description=(
            "The Virasoro shadow PF is tau-independent; the vacuum character "
            "carries the full tau-dependence."
        ),
    )


# ===========================================================================
# Section 7: Fredholm determinant structure
# ===========================================================================

def fredholm_genus1_scalar(q_abs: float, N: int = 500) -> float:
    r"""det(1 - K_1) = prod_{n>=1}(1-q^n) for the scalar sewing kernel.

    At genus 1, the sewing kernel is diagonal: K_1 = diag(q, q^2, q^3, ...).
    Each eigenvalue is q^n with multiplicity 1 (one-particle).
    """
    result = 1.0
    for n in range(1, N + 1):
        val = q_abs ** n
        if val < 1e-50:
            break
        result *= (1.0 - val)
    return result


def fredholm_genus1_heisenberg(q_abs: float, k: int = 1,
                                N: int = 500) -> Dict[str, float]:
    r"""Fredholm determinant for Heisenberg at genus 1.

    The Fredholm determinant of the sewing kernel is:
      det(1 - K_1) = prod(1-q^n)^k

    The partition function INCLUDING the vacuum energy is:
      Z_1(H_k) = q^{-k/24} * det(1 - K_1)^{-1}
               = q^{-k/24} * prod(1-q^n)^{-k}
               = 1/eta(q)^k

    The q^{-k/24} vacuum energy prefactor is NOT part of the Fredholm
    determinant; it comes from the L_0 zero-point energy (AP46).

    Returns both the raw Fredholm det (no vacuum energy) and the full
    partition function (with vacuum energy).
    """
    eta_prod = fredholm_genus1_scalar(q_abs, N)
    fred_det = eta_prod ** k

    Z1_product = fred_det ** (-1) if abs(fred_det) > 1e-300 else float('inf')

    # Full partition function including vacuum energy
    vacuum_energy = q_abs ** (-k / 24.0)
    Z1_full = vacuum_energy * Z1_product

    # Direct computation for cross-check
    Z1_direct = 1.0
    for n in range(1, N + 1):
        val = q_abs ** n
        if val < 1e-50:
            break
        Z1_direct *= (1.0 - val) ** (-k)

    return {
        'fredholm_det': fred_det,
        'partition_function_product': Z1_product,  # without q^{-k/24}
        'partition_function': Z1_full,  # with q^{-k/24} = 1/eta^k
        'vacuum_energy': vacuum_energy,
        'partition_function_direct': Z1_direct,
        'agreement': abs(Z1_product - Z1_direct) / max(abs(Z1_product), 1e-30),
        'log_Z': math.log(Z1_full) if Z1_full > 0 else float('-inf'),
        'q': q_abs,
        'k': k,
    }


def fredholm_genus1_affine(q_abs: float, dim_g: int,
                            N: int = 500) -> Dict[str, float]:
    r"""Fredholm determinant for affine KM at genus 1.

    Product part (no vacuum energy):
      prod(1-q^n)^{-dim(g)}

    The full character including vacuum energy is:
      q^{-c/24} * prod(1-q^n)^{-dim(g)}
    but c depends on k and h^v, which are not passed here.
    We return the product part only.
    """
    eta_prod = fredholm_genus1_scalar(q_abs, N)
    fred_det = eta_prod ** dim_g
    Z1_product = fred_det ** (-1) if abs(fred_det) > 1e-300 else float('inf')

    return {
        'fredholm_det': fred_det,
        'partition_function': Z1_product,  # product part only
        'log_Z': math.log(Z1_product) if Z1_product > 0 else float('-inf'),
        'dim_g': dim_g,
        'q': q_abs,
    }


def fredholm_eigenvalue_spectrum(q_abs: float, max_level: int = 50,
                                  colors: int = 1) -> List[Dict]:
    r"""Eigenvalue spectrum of the genus-1 sewing kernel.

    At level n: eigenvalue = q^n, multiplicity = colored_partitions(n, colors).
    For Heisenberg (colors=1): mult = p(n) (partition numbers).
    For affine g-hat (colors=dim(g)): mult = colored_partitions(n, dim_g).
    """
    spectrum = []
    for n in range(1, max_level + 1):
        mult = colored_partitions(n, colors)
        eigenval = q_abs ** n
        spectrum.append({
            'level': n,
            'eigenvalue': eigenval,
            'multiplicity': mult,
            'contribution': mult * eigenval,
        })
    return spectrum


# ===========================================================================
# Section 8: Genus-2 sewing (plumbing construction)
# ===========================================================================

def genus2_partition_heisenberg(q1: float, q2: float, qp: float,
                                 k: int = 1, N: int = 100) -> Dict:
    r"""Genus-2 partition function for Heisenberg via plumbing.

    The genus-2 surface is obtained by sewing two tori with a plumbing
    fixture.  The partition function is:

      Z_2(Omega) = sum_{n>=0} p_k(n) * q_p^n * Z_1(tau_1) * Z_1(tau_2)

    where p_k(n) are k-colored partitions (the dimension of the weight-n
    subspace of H_k), q_p is the plumbing parameter, and Z_1(tau_i)
    are the genus-1 partition functions on each torus.

    The leading term (n=0) is Z_1(tau_1) * Z_1(tau_2).
    The plumbing corrections involve higher states propagating through
    the handle.

    In the degeneration limit qp -> 0:
      Z_2 -> Z_1(tau_1) * Z_1(tau_2)
    which is the factorization property.
    """
    # Genus-1 partition functions
    Z1_left = 1.0
    Z1_right = 1.0
    for n in range(1, N + 1):
        if q1 ** n < 1e-50:
            break
        Z1_left *= (1.0 - q1 ** n) ** (-k)
    for n in range(1, N + 1):
        if q2 ** n < 1e-50:
            break
        Z1_right *= (1.0 - q2 ** n) ** (-k)

    # Plumbing sum: each level n contributes p_k(n) * qp^n
    # The plumbing operator is sum_n |n><n| * qp^n where |n> runs over
    # a basis of weight-n states.
    plumbing_sum = 0.0
    for n in range(0, N + 1):
        mult = colored_partitions(n, k)
        term = mult * qp ** n
        if abs(term) < 1e-50 and n > 0:
            break
        plumbing_sum += term

    Z2 = Z1_left * Z1_right * plumbing_sum

    # Factorization limit
    Z2_factorized = Z1_left * Z1_right

    return {
        'Z2': Z2,
        'Z1_left': Z1_left,
        'Z1_right': Z1_right,
        'plumbing_sum': plumbing_sum,
        'Z2_factorized': Z2_factorized,
        'factorization_ratio': Z2 / Z2_factorized if Z2_factorized != 0 else 0,
        'q1': q1,
        'q2': q2,
        'qp': qp,
        'k': k,
    }


# ===========================================================================
# Section 9: HS-sewing convergence
# ===========================================================================

def hs_sewing_norm(q_abs: float, algebra: str, **kwargs) -> Dict[str, Any]:
    r"""Hilbert-Schmidt sewing norm.

    The HS-sewing condition (thm:general-hs-sewing):
      sum_{a,b,c} q^{a+b+c} ||m_{a,b}^c||^2_{HS} < infinity

    For Heisenberg at level k:
      m_{a,b}^c = delta_{a+b,c} * (OPE coefficient)
    so ||m_{a,b}^c||_HS = delta_{a+b,c} * sqrt(k) / sqrt(normalization)

    The HS norm simplifies to:
      sum_{n>=1} dim(V_n)^2 * q^{2n}
    which converges for all |q| < 1.

    For affine KM:
      dim(V_n) = colored_partitions(n, dim_g) ~ exp(C*sqrt(n))
    which is subexponential -> convergence guaranteed for |q| < 1.
    """
    k = kwargs.get('k', 1)
    dim_g = kwargs.get('dim_g', 1)

    if algebra == 'heisenberg':
        colors = k
    elif algebra == 'affine_km':
        colors = dim_g
    elif algebra == 'virasoro':
        colors = 1  # single generator at weight 2
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    total_hs = 0.0
    terms = []
    max_n = kwargs.get('max_n', 100)
    for n in range(1, max_n + 1):
        dn = colored_partitions(n, colors)
        term = dn ** 2 * q_abs ** (2 * n)
        total_hs += term
        terms.append({'n': n, 'dim_n': dn, 'term': term})
        if term < 1e-50:
            break

    # Check convergence: the terms should decrease exponentially
    converged = len(terms) >= 2 and terms[-1]['term'] < 1e-30

    return {
        'algebra': algebra,
        'hs_norm': total_hs,
        'converged': converged,
        'num_terms': len(terms),
        'terms': terms[:20],
        'q': q_abs,
    }


def hs_convergence_landscape(q_abs: float = 0.1) -> Dict[str, Any]:
    r"""Verify HS-sewing convergence across the standard landscape.

    thm:general-hs-sewing: polynomial OPE growth + subexponential
    sector growth -> convergence at all genera.

    All standard families have polynomial OPE growth (finite number of
    generators with polynomial structure constants in n) and subexponential
    sector growth (dim V_n ~ exp(C*sqrt(n)) from Hardy-Ramanujan).
    """
    families = {
        'heisenberg_k1': {'algebra': 'heisenberg', 'k': 1},
        'heisenberg_k2': {'algebra': 'heisenberg', 'k': 2},
        'virasoro': {'algebra': 'virasoro'},
        'sl2_level1': {'algebra': 'affine_km', 'dim_g': 3},
        'sl3_level1': {'algebra': 'affine_km', 'dim_g': 8},
        'e8_level1': {'algebra': 'affine_km', 'dim_g': 248},
    }

    results = {}
    for name, params in families.items():
        alg = params.pop('algebra')
        result = hs_sewing_norm(q_abs, alg, **params)
        params['algebra'] = alg
        results[name] = {
            'hs_norm': result['hs_norm'],
            'converged': result['converged'],
        }

    all_converged = all(r['converged'] for r in results.values())

    return {
        'q': q_abs,
        'results': results,
        'all_converged': all_converged,
    }


# ===========================================================================
# Section 10: Modular transformations
# ===========================================================================

def modular_s_transform_eta(tau: complex, N: int = 300) -> Dict[str, complex]:
    r"""Verify eta(-1/tau) = sqrt(-i*tau) * eta(tau).

    The S-transformation of the Dedekind eta function.
    """
    eta_tau = eta_function(tau, N)
    eta_s = eta_function(-1.0 / tau, N)
    sqrt_factor = cmath.sqrt(-1j * tau)
    predicted = sqrt_factor * eta_tau

    return {
        'eta_tau': eta_tau,
        'eta_s_tau': eta_s,
        'predicted': predicted,
        'ratio': eta_s / predicted if abs(predicted) > 1e-30 else complex(0),
        'agreement': abs(eta_s - predicted) / max(abs(eta_s), 1e-30),
    }


def modular_weight_check_heisenberg(tau: complex, k: int = 1,
                                      N: int = 300) -> Dict[str, Any]:
    r"""Check modular weight of Z_1(H_k) = 1/eta^k.

    Under tau -> -1/tau:
      1/eta(-1/tau)^k = 1/(sqrt(-i*tau) * eta(tau))^k
                      = (-i*tau)^{-k/2} * 1/eta(tau)^k

    So Z_1(H_k) has modular weight -k/2.
    """
    Z_tau = heisenberg_partition_genus1(tau, k, N)
    Z_s = heisenberg_partition_genus1(-1.0 / tau, k, N)

    modular_factor = (-1j * tau) ** (-k / 2.0)
    predicted_Z_s = modular_factor * Z_tau

    agreement = abs(Z_s - predicted_Z_s) / max(abs(Z_s), 1e-30)

    return {
        'Z_tau': Z_tau,
        'Z_s_tau': Z_s,
        'predicted_Z_s': predicted_Z_s,
        'modular_weight': -k / 2.0,
        'modular_factor': modular_factor,
        'agreement': agreement,
    }


def modular_t_transform_heisenberg(tau: complex, k: int = 1,
                                     N: int = 300) -> Dict[str, Any]:
    r"""Check T-transformation: Z_1(tau+1) = e^{-2*pi*i*k/24} Z_1(tau).

    Under tau -> tau + 1:
      eta(tau+1) = e^{2*pi*i/24} * eta(tau)
      1/eta^k -> e^{-2*pi*i*k/24} / eta(tau)^k
    """
    Z_tau = heisenberg_partition_genus1(tau, k, N)
    Z_t = heisenberg_partition_genus1(tau + 1.0, k, N)

    phase = cmath.exp(-2j * PI * k / 24.0)
    predicted = phase * Z_tau

    agreement = abs(Z_t - predicted) / max(abs(Z_t), 1e-30)

    return {
        'Z_tau': Z_tau,
        'Z_tau_plus_1': Z_t,
        'predicted': predicted,
        'phase': phase,
        'agreement': agreement,
    }


# ===========================================================================
# Section 11: Analytic continuation in central charge
# ===========================================================================

def analytic_continuation_c(c_values: List[float], tau: complex,
                             N: int = 300) -> Dict[str, Any]:
    r"""Evaluate the vacuum character at different central charges.

    The Virasoro vacuum character at generic c is:
      chi_0(tau, c) = q^{-c/24} (1-q) / prod(1-q^n)

    This is ANALYTIC in c (it's linear in q^{-c/24} = e^{-c/12 * 2*pi*i*tau}).
    """
    results = {}
    for c in c_values:
        Z = virasoro_vacuum_character_generic(tau, c, N)
        kappa = kappa_virasoro(c)
        shadow = c / 48.0  # F_1 = kappa/24 = c/48

        results[c] = {
            'Z': Z,
            'abs_Z': abs(Z),
            'log_abs_Z': math.log(abs(Z)) if abs(Z) > 0 else float('-inf'),
            'kappa': kappa,
            'shadow_F1': shadow,
        }

    # Check smoothness: |Z(c)| should vary smoothly with c
    c_sorted = sorted(results.keys())
    smoothness = True
    for i in range(1, len(c_sorted) - 1):
        c_prev = c_sorted[i - 1]
        c_curr = c_sorted[i]
        c_next = c_sorted[i + 1]
        val_prev = results[c_prev]['abs_Z']
        val_curr = results[c_curr]['abs_Z']
        val_next = results[c_next]['abs_Z']
        # Check that the middle value is between or near the average
        avg = (val_prev + val_next) / 2.0
        if avg > 0 and abs(val_curr - avg) / avg > 5.0:
            smoothness = False

    return {
        'tau': tau,
        'c_values': c_values,
        'results': results,
        'smooth': smoothness,
    }


# ===========================================================================
# Section 12: Large-tau asymptotics
# ===========================================================================

def large_tau_asymptotics(k: int = 1, t_values: Optional[List[float]] = None,
                           N: int = 300) -> Dict[str, Any]:
    r"""Verify shadow expansion matches large-tau asymptotics.

    For tau = i*t with t >> 1 (i.e., q = e^{-2*pi*t} << 1):
      log Z_1^{an}(H_k) = -k * log eta(i*t)
                         = -k * ((-2*pi*t)/24 + sum log(1-e^{-2*pi*n*t}))
                         = k*pi*t/12 + exponentially small corrections

    The shadow F_1 = k/24 captures the COEFFICIENT:
      F_1 = lim_{t->infty} d/d(2*pi*t) log Z_1^{an} = k/24

    More precisely: log Z_1^{an} = -k*(2*pi*i*tau)/24 + O(q)
                                 = k*pi*t/12 + O(e^{-2*pi*t})
    """
    if t_values is None:
        t_values = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    results = {}
    for t in t_values:
        tau = complex(0, t)
        q_abs = math.exp(-2 * PI * t)

        # Full log Z
        log_Z = -k * log_eta(tau, N)

        # Leading asymptotic: k * pi * t / 12
        leading = k * PI * t / 12.0

        # Correction: the non-leading Fourier modes
        correction = log_Z.real - leading

        # Shadow F_1 check: the coefficient of 2*pi*t in log Z
        # log Z = k * (2*pi*t) / 24 = k*pi*t/12
        # So d(log Z)/d(2*pi*t) = k/24 = F_1.  Correct!
        shadow_F1 = float(k) / 24.0

        results[t] = {
            'tau': tau,
            'q_abs': q_abs,
            'log_Z_real': log_Z.real,
            'leading': leading,
            'correction': correction,
            'relative_correction': abs(correction) / abs(leading) if leading != 0 else 0,
            'shadow_F1': shadow_F1,
        }

    return {
        'k': k,
        'results': results,
    }


# ===========================================================================
# Section 13: Full analysis combining all paths
# ===========================================================================

@dataclass
class AnalyticPartitionResult:
    """Complete analytic shadow partition function analysis."""
    algebra: str
    params: Dict[str, Any]
    genus1_exact: complex
    genus1_shadow: float
    discrepancy: DiscrepancyResult
    fredholm: Dict[str, float]
    modular_check: Dict[str, Any]
    convergence: Dict[str, Any]
    description: str = ""


def full_analysis_heisenberg(k: int = 1,
                              tau: complex = complex(0, 1.0),
                              N: int = 300) -> AnalyticPartitionResult:
    r"""Complete multi-path verification for Heisenberg at level k.

    Six verification paths:
    1. Sewing construction (Fredholm determinant)
    2. Shadow expansion (perturbative)
    3. Exact partition function (1/eta^k)
    4. Modular transformation
    5. Fredholm determinant
    6. Large-tau asymptotics
    """
    q_abs = abs(cmath.exp(2j * PI * tau))

    # Path 1 & 3: exact partition function
    Z1 = heisenberg_partition_genus1(tau, k, N)

    # Path 2: shadow expansion
    kap = kappa_heisenberg(k)
    shadow_F1 = kap / 24.0

    # Path 5: Fredholm determinant
    fred = fredholm_genus1_heisenberg(q_abs, k, N)

    # Path 6: discrepancy
    disc = genus1_discrepancy_heisenberg(tau, k, N)

    # Path 4: modular check
    mod_check = modular_weight_check_heisenberg(tau, k, N)

    # Convergence
    conv = hs_sewing_norm(q_abs, 'heisenberg', k=k)

    return AnalyticPartitionResult(
        algebra=f"Heisenberg_k={k}",
        params={'k': k, 'tau': tau, 'kappa': kap},
        genus1_exact=Z1,
        genus1_shadow=shadow_F1,
        discrepancy=disc,
        fredholm=fred,
        modular_check=mod_check,
        convergence=conv,
        description=(
            f"Heisenberg at level k={k}. Class G (shadow depth 2). "
            f"kappa={kap}. Exact partition function is 1/eta^{k}."
        ),
    )


def full_analysis_virasoro(c: float = 25.0,
                            tau: complex = complex(0, 1.0),
                            N: int = 300) -> AnalyticPartitionResult:
    r"""Complete analysis for Virasoro at central charge c."""
    q_abs = abs(cmath.exp(2j * PI * tau))

    Z1 = virasoro_vacuum_character_generic(tau, c, N)
    kap = kappa_virasoro(c)
    shadow_F1 = kap / 24.0
    disc = genus1_discrepancy_virasoro(tau, c, N)

    fred = fredholm_genus1_heisenberg(q_abs, 1, N)  # single Fock space
    conv = hs_sewing_norm(q_abs, 'virasoro')

    return AnalyticPartitionResult(
        algebra=f"Virasoro_c={c}",
        params={'c': c, 'tau': tau, 'kappa': kap},
        genus1_exact=Z1,
        genus1_shadow=shadow_F1,
        discrepancy=disc,
        fredholm=fred,
        modular_check={},
        convergence=conv,
        description=(
            f"Virasoro at c={c}. Class M (infinite shadow depth). "
            f"kappa={kap}=c/2."
        ),
    )


# ===========================================================================
# Section 14: Fourier coefficient extraction
# ===========================================================================

def fourier_coefficients_eta_inv(k: int = 1, max_n: int = 50) -> List[int]:
    r"""Fourier coefficients of 1/eta(tau)^k = q^{-k/24} sum a_n q^n.

    a_n = colored_partitions(n, k) = number of k-colored partitions of n.

    For k=1: a_n = p(n) (ordinary partitions).
    For k=24: a_n = tau(n+1) + ... (related to Ramanujan tau, but NOT equal).
    """
    return [colored_partitions(n, k) for n in range(max_n + 1)]


def fourier_growth_check(k: int = 1, max_n: int = 100) -> Dict[str, Any]:
    r"""Verify asymptotic growth of Fourier coefficients.

    Hardy-Ramanujan: p(n) ~ exp(pi*sqrt(2n/3)) / (4*n*sqrt(3)) as n -> infinity.
    For k-colored partitions: p_k(n) ~ C(k) * n^{-(k+3)/4} * exp(pi*sqrt(2kn/3)).
    """
    coeffs = fourier_coefficients_eta_inv(k, max_n)

    growth_data = []
    for n in range(1, min(max_n + 1, len(coeffs))):
        if coeffs[n] > 0:
            log_an = math.log(coeffs[n])
            predicted_exponent = PI * math.sqrt(2 * k * n / 3.0)
            growth_data.append({
                'n': n,
                'a_n': coeffs[n],
                'log_a_n': log_an,
                'predicted_exponent': predicted_exponent,
                'ratio': log_an / predicted_exponent if predicted_exponent > 0 else 0,
            })

    # The ratio log(a_n) / (pi*sqrt(2kn/3)) -> 1 as n -> infinity
    return {
        'k': k,
        'max_n': max_n,
        'coefficients': coeffs[:30],
        'growth_data': growth_data[-10:] if growth_data else [],
        'asymptotic_ratio_final': growth_data[-1]['ratio'] if growth_data else 0,
    }


# ===========================================================================
# Section 15: Genus-2 shadow vs exact comparison
# ===========================================================================

def genus2_shadow_free_energy(kappa_val: float) -> float:
    r"""F_2^{scalar}(A) = kappa * lambda_2^{FP} = kappa * 7/5760.

    This is the genus-2 scalar shadow contribution.
    """
    return float(F_g(Rational(kappa_val).limit_denominator(10**9), 2))


def genus2_shadow_vs_plumbing(k: int = 1,
                               q1: float = 0.1, q2: float = 0.1,
                               qp: float = 0.01,
                               N: int = 100) -> Dict[str, Any]:
    r"""Compare genus-2 shadow prediction with plumbing construction.

    The shadow expansion at genus 2:
      F_2 = kappa * 7/5760

    The plumbing construction gives the EXACT genus-2 partition function
    (in a specific degeneration limit).

    In the degeneration limit qp -> 0:
      log Z_2 -> log Z_1(tau_1) + log Z_1(tau_2) + log(plumbing_sum)
    and the genus-2 corrections are captured by the plumbing_sum.
    """
    kap = kappa_heisenberg(k)
    F2_shadow = genus2_shadow_free_energy(kap)

    plumbing = genus2_partition_heisenberg(q1, q2, qp, k, N)

    # The plumbing sum captures genus-2 corrections
    log_plumbing = math.log(plumbing['plumbing_sum']) if plumbing['plumbing_sum'] > 0 else 0

    return {
        'k': k,
        'kappa': kap,
        'F2_shadow': F2_shadow,
        'log_plumbing_sum': log_plumbing,
        'plumbing': plumbing,
        'description': (
            "F2_shadow is the genus-2 scalar free energy. "
            "The plumbing sum captures the exact genus-2 partition function "
            "in the degeneration limit."
        ),
    }


# ===========================================================================
# Section 16: Shadow depth and class analysis
# ===========================================================================

def shadow_class_partition_function(algebra: str, tau: complex,
                                     N: int = 300, **kwargs) -> Dict[str, Any]:
    r"""Compute the analytic partition function and classify by shadow depth.

    Class G (r_max=2): Heisenberg, lattice VOAs. Shadow IS exact at scalar level.
    Class L (r_max=3): affine KM. One cubic correction.
    Class C (r_max=4): beta-gamma. Cubic + quartic corrections.
    Class M (r_max=inf): Virasoro, W_N. Infinite tower.

    For class G: Delta_g = 0 (shadow is exact at scalar level).
    For class L: Delta_g involves instanton corrections from the OPE.
    For class M: Delta_g involves the full non-perturbative structure.
    """
    if algebra == 'heisenberg':
        k = kwargs.get('k', 1)
        Z = heisenberg_partition_genus1(tau, k, N)
        kap = kappa_heisenberg(k)
        shadow_class = 'G'
        r_max = 2
    elif algebra == 'virasoro':
        c = kwargs.get('c', 25.0)
        Z = virasoro_vacuum_character_generic(tau, c, N)
        kap = kappa_virasoro(c)
        shadow_class = 'M'
        r_max = float('inf')
    elif algebra == 'affine_km':
        dim_g = kwargs.get('dim_g', 3)
        Z = affine_km_partition_genus1(tau, dim_g, N)
        h_dual = kwargs.get('h_dual', 2)
        level = kwargs.get('level', 1.0)
        kap = kappa_affine_km(dim_g, h_dual, level)
        shadow_class = 'L'
        r_max = 3
    elif algebra == 'ising':
        Z = ising_vacuum_character(tau, N)
        kap = kappa_virasoro(0.5)
        shadow_class = 'M'
        r_max = float('inf')
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    shadow_F1 = kap / 24.0
    log_Z = cmath.log(Z) if abs(Z) > 1e-300 else complex(float('-inf'), 0)

    return {
        'algebra': algebra,
        'partition_function': Z,
        'log_Z': log_Z,
        'kappa': kap,
        'shadow_F1': shadow_F1,
        'shadow_class': shadow_class,
        'r_max': r_max,
        'tau': tau,
    }


# ===========================================================================
# Section 17: Partition function Fourier decomposition
# ===========================================================================

def partition_function_q_expansion(algebra: str, max_n: int = 30,
                                    **kwargs) -> Dict[str, Any]:
    r"""Compute the q-expansion of the partition function.

    Returns coefficients a_n in Z(tau) = q^{h_0} sum_n a_n q^n
    where h_0 = -c/24 is the vacuum conformal weight.
    """
    if algebra == 'heisenberg':
        k = kwargs.get('k', 1)
        # Z = 1/eta^k = q^{-k/24} sum p_k(n) q^n
        coeffs = fourier_coefficients_eta_inv(k, max_n)
        h0 = -k / 24.0
        kap = kappa_heisenberg(k)
    elif algebra == 'virasoro':
        c = kwargs.get('c', 25.0)
        # Z = q^{-c/24} (1-q) / prod(1-q^n)
        # Coefficients: a_0 = 1, a_1 = 0 (null subtraction), a_n = p(n) - p(n-1)
        base = fourier_coefficients_eta_inv(1, max_n)
        coeffs = [0] * (max_n + 1)
        for n in range(max_n + 1):
            coeffs[n] = base[n] - (base[n - 1] if n >= 1 else 0)
        h0 = -c / 24.0
        kap = kappa_virasoro(c)
    elif algebra == 'affine_km':
        dim_g = kwargs.get('dim_g', 3)
        level = kwargs.get('level', 1.0)
        h_dual = kwargs.get('h_dual', 2)
        c = level * dim_g / (level + h_dual)
        coeffs = [colored_partitions(n, dim_g) for n in range(max_n + 1)]
        h0 = -c / 24.0
        kap = kappa_affine_km(dim_g, h_dual, level)
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    return {
        'algebra': algebra,
        'coefficients': coeffs,
        'vacuum_weight': h0,
        'kappa': kap,
        'max_n': max_n,
    }


# ===========================================================================
# Section 18: Multi-path verification summary
# ===========================================================================

def multi_path_verification(algebra: str = 'heisenberg',
                             tau: complex = complex(0, 1.0),
                             N: int = 300,
                             **kwargs) -> Dict[str, Any]:
    r"""Run all six verification paths and compare.

    Path 1: Sewing (Fredholm determinant)
    Path 2: Shadow expansion (perturbative)
    Path 3: Exact partition function
    Path 4: Modular transformation check
    Path 5: Large-tau asymptotics
    Path 6: Fourier coefficient growth
    """
    q_abs = abs(cmath.exp(2j * PI * tau))

    results = {'algebra': algebra, 'tau': tau}

    if algebra == 'heisenberg':
        k = kwargs.get('k', 1)
        kap = kappa_heisenberg(k)

        # Path 1: Fredholm
        fred = fredholm_genus1_heisenberg(q_abs, k, N)
        results['path1_fredholm'] = fred

        # Path 2: Shadow
        results['path2_shadow'] = {
            'F1': kap / 24.0,
            'F2': float(F_g(Rational(kap).limit_denominator(10**9), 2)),
        }

        # Path 3: Exact
        Z1 = heisenberg_partition_genus1(tau, k, N)
        results['path3_exact'] = {'Z1': Z1, 'abs_Z1': abs(Z1)}

        # Path 4: Modular
        results['path4_modular'] = modular_weight_check_heisenberg(tau, k, N)

        # Path 5: Asymptotics
        if tau.imag > 0:
            results['path5_asymptotics'] = large_tau_asymptotics(k, [tau.imag], N)

        # Path 6: Fourier
        results['path6_fourier'] = fourier_growth_check(k, 50)

        # Cross-check: Fredholm Z1 vs exact Z1
        Z1_fred = fred['partition_function']
        Z1_exact = abs(Z1)
        # The Fredholm computation uses |q|, the exact uses q = e^{2pi i tau}
        # They should agree when tau is purely imaginary
        if abs(tau.real) < 1e-10:
            results['fredholm_exact_agreement'] = (
                abs(Z1_fred - Z1_exact) / max(Z1_exact, 1e-30)
            )

    elif algebra == 'virasoro':
        c = kwargs.get('c', 25.0)
        kap = kappa_virasoro(c)

        Z1 = virasoro_vacuum_character_generic(tau, c, N)
        results['path3_exact'] = {'Z1': Z1, 'abs_Z1': abs(Z1)}
        results['path2_shadow'] = {'F1': kap / 24.0}
        results['path6_fourier'] = partition_function_q_expansion(
            'virasoro', c=c, max_n=30
        )

    return results
