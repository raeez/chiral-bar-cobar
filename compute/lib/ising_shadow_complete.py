r"""Complete shadow obstruction tower analysis for the Ising model (Virasoro c=1/2).

The Ising model M(3,4) is the simplest non-trivial 2d CFT:
  c = 1/2, three primary fields: 1 (h=0), epsilon (h=1/2), sigma (h=1/16).
  Fusion: sigma x sigma = 1 + epsilon, sigma x epsilon = sigma, epsilon x epsilon = 1.

As a Virasoro algebra at c=1/2, its shadow obstruction tower is determined by the
universal Virasoro shadow data:
  kappa = c/2 = 1/4
  S_3 = 2  (cubic shadow, c-independent for all Virasoro)
  S_4 = 10/[c(5c+22)] = 40/49
  Delta = 8*kappa*S_4 = 80/49

CRITICAL FINDING: The Ising model lies deep in the divergent regime.
  rho(Ising) = sqrt(7696/49) / (2 * 1/4) = 2*sqrt(481)/7
             ~ 12.533   (>> 1)
  The shadow arity series DIVERGES exponentially. Each successive shadow
  coefficient S_r grows roughly as rho^r ~ 12.5^r.

Physical interpretation: c = 1/2 is far below the critical central charge
c* ~ 6.125 where rho = 1. The Ising model's nonlinear shadow data is
non-perturbative -- the finite-arity truncations Theta^{<=r} provide
progressively WORSE approximations as r grows. The full MC element Theta_A
exists (thm:mc2-bar-intrinsic) but is not accessible by arity truncation.
Shadow amplitudes at all genera are well-defined individually but the arity
sum requires Borel or resurgent resummation.

The Koszul dual Vir_{25.5} at c = 51/2 has rho ~ 0.1337 (convergent).
This illustrates the complementarity principle: divergent tower <-> convergent dual.

Manuscript references:
  comp:ising-bar-interpretation (minimal_model_examples.tex)
  thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
  def:shadow-metric (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs,
    N as Neval,
    Rational,
    Symbol,
    bernoulli,
    cancel,
    cos as sym_cos,
    factorial,
    pi as sym_pi,
    simplify,
    sqrt,
)


# ============================================================================
# Constants
# ============================================================================

C_ISING = Rational(1, 2)
C_TRICRITICAL = Rational(7, 10)
C_KOSZUL_DUAL = Rational(51, 2)  # 26 - 1/2

PI = math.pi
TWO_PI_SQ = (2 * PI) ** 2


# ============================================================================
# 1. Shadow invariants (exact rational arithmetic)
# ============================================================================

def ising_shadow_data() -> Dict[str, Any]:
    """Complete shadow data for the Ising model at c = 1/2.

    Returns dict with all primary shadow invariants as exact sympy Rationals.

    NOTE on a common error: S_3 = 2 for ALL Virasoro algebras, regardless
    of c. The cubic shadow is c-independent (the coefficient 'alpha' in the
    shadow metric parametrization Q_L = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    has alpha = S_3 = 2). Writing S_3 = -6/(5c+22) is WRONG -- that formula
    does not appear in the shadow obstruction tower.
    """
    c = C_ISING
    kappa = c / 2  # = 1/4
    S3 = Rational(2)  # c-independent for Virasoro
    S4 = Rational(10) / (c * (5 * c + 22))  # = 10/(1/2 * 49/2) = 40/49
    Delta = 8 * kappa * S4  # = 80/49

    # Shadow metric Q_L(t) = q0 + q1*t + q2*t^2
    q0 = 4 * kappa ** 2  # = 1/4
    q1 = 12 * kappa * S3  # = 6
    q2 = 9 * S3 ** 2 + 16 * kappa * S4  # = 36 + 160/49 = 1924/49

    # Growth rate
    numer_sq = 9 * S3 ** 2 + 2 * Delta  # = 36 + 160/49 = 1924/49
    rho_sq = numer_sq / (4 * kappa ** 2)  # = (1924/49)/(1/4) = 7696/49
    rho = sqrt(rho_sq)  # = 2*sqrt(481)/7 ~ 12.533

    return {
        'c': c,
        'kappa': kappa,
        'S3': S3,
        'S4': cancel(S4),
        'Delta': cancel(Delta),
        'q0': q0,
        'q1': q1,
        'q2': cancel(q2),
        'rho_squared': cancel(rho_sq),
        'rho': rho,
        'rho_numerical': float(rho.evalf()),
        'convergent': False,  # rho >> 1
        'depth_class': 'M',
    }


def ising_shadow_tower(max_arity: int = 30) -> Dict[int, Rational]:
    """Compute the Ising shadow obstruction tower S_2, ..., S_{max_arity} exactly.

    Uses the convolution recursion from f^2 = Q_L:
      a_0 = sqrt(q0) = 1/2
      a_1 = q1/(2*a_0) = 6
      a_2 = (q2 - a_1^2)/(2*a_0) = (1924/49 - 36)/(1) = 160/49
      a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}   for n >= 3

    Then S_r = a_{r-2} / r.
    """
    c = C_ISING
    kappa = c / 2
    S3 = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * S3
    q2 = 9 * S3 ** 2 + 16 * kappa * S4

    max_n = max_arity - 2
    a = [Rational(0)] * (max_n + 1)
    a[0] = Rational(1, 2)  # sqrt(q0) = sqrt(1/4) = 1/2

    if max_n >= 1:
        a[1] = q1 / (2 * a[0])  # = 6/1 = 6
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a[0])

    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * a[0]))

    return {r: cancel(a[r - 2] / r) for r in range(2, max_arity + 1)}


def ising_shadow_tower_numerical(max_arity: int = 50) -> Dict[int, float]:
    """Numerical shadow obstruction tower using floating point for speed.

    Identical recursion as ising_shadow_tower but in float64 for high arities.
    """
    c = 0.5
    kappa = 0.25
    S3 = 2.0
    S4 = 10.0 / (c * (5.0 * c + 22.0))

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * S3
    q2 = 9.0 * S3 ** 2 + 16.0 * kappa * S4

    max_n = max_arity - 2
    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0)  # 0.5
    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2.0 * a[0])

    return {r: a[r - 2] / r for r in range(2, max_arity + 1)}


# ============================================================================
# 2. Shadow growth rate and convergence analysis
# ============================================================================

def ising_growth_rate_exact() -> Dict[str, Any]:
    """Exact shadow growth rate for the Ising model.

    rho^2 = (9*S_3^2 + 2*Delta) / (4*kappa^2)
          = (36 + 160/49) / (1/4)
          = 4 * 1924/49
          = 7696/49

    rho = sqrt(7696/49) = sqrt(7696)/7 = 4*sqrt(481)/7

    481 = 13 * 37  (product of two primes)

    Numerically: rho ~ 12.533
    """
    rho_sq = Rational(7696, 49)
    rho_exact = sqrt(rho_sq)

    # Factor: 7696 = 16 * 481 = 16 * 13 * 37
    # So rho = 4*sqrt(481)/7 = 4*sqrt(13*37)/7
    return {
        'rho_squared': rho_sq,
        'rho_exact': rho_exact,
        'rho_factored': '4*sqrt(13*37)/7',
        'rho_numerical': float(rho_exact.evalf()),
        'convergent': False,
        'divergence_rate_per_arity': float(rho_exact.evalf()),
        'inverse_rho': float((1 / rho_exact).evalf()),
    }


def ising_convergence_analysis(max_arity: int = 30) -> Dict[str, Any]:
    """Full convergence analysis: ratio test, partial sums, oscillation.

    The shadow obstruction tower diverges (rho >> 1). This analysis quantifies HOW it diverges.
    """
    tower = ising_shadow_tower_numerical(max_arity)
    rho_data = ising_growth_rate_exact()
    rho = rho_data['rho_numerical']

    # Ratio test: |S_{r+1}/S_r|
    ratios = {}
    for r in range(2, max_arity):
        if abs(tower[r]) > 1e-300:
            ratios[r] = abs(tower[r + 1] / tower[r])

    # Partial sums of |S_r|
    partial_sums = {}
    running = 0.0
    for r in range(2, max_arity + 1):
        running += abs(tower[r])
        partial_sums[r] = running

    # Detrended: S_r / rho^r
    detrended = {}
    for r in range(2, max_arity + 1):
        if abs(tower[r]) > 1e-300:
            detrended[r] = tower[r] / rho ** r

    # Oscillation phase from branch points
    c_val = 0.5
    kappa = 0.25
    S3 = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * S3
    q2 = 9.0 * S3 ** 2 + 16.0 * kappa * S4
    disc = q1 ** 2 - 4 * q0 * q2
    # disc < 0 for Delta > 0 (class M)
    t_plus = complex(-q1 + cmath.sqrt(disc)) / (2 * q2)
    t_minus = complex(-q1 - cmath.sqrt(disc)) / (2 * q2)
    theta = -cmath.phase(t_plus)

    return {
        'tower': tower,
        'rho': rho,
        'ratio_sequence': ratios,
        'ratio_limit': ratios.get(max_arity - 1, None),
        'partial_sums': partial_sums,
        'detrended': detrended,
        'oscillation_phase': theta,
        'branch_points': (t_plus, t_minus),
        'branch_point_modulus': abs(t_plus),
        'convergent': False,
        'borel_summable': True,  # algebraic GF => Gevrey-0
    }


# ============================================================================
# 3. Koszul dual: Vir_{c=51/2}
# ============================================================================

def koszul_dual_shadow_data() -> Dict[str, Any]:
    """Shadow data for the Koszul dual Vir_{51/2}.

    Koszul duality: c -> 26 - c, so c' = 51/2.
    This is NOT a minimal model (not rational).

    kappa' = c'/2 = 51/4
    kappa + kappa' = 1/4 + 51/4 = 52/4 = 13  (AP24 verification)
    """
    c_dual = C_KOSZUL_DUAL  # 51/2
    kappa_dual = c_dual / 2  # 51/4
    S3_dual = Rational(2)  # same for all Virasoro
    S4_dual = Rational(10) / (c_dual * (5 * c_dual + 22))
    # 5*51/2 + 22 = 255/2 + 22 = 299/2
    # c_dual * (5*c_dual + 22) = (51/2)*(299/2) = 15249/4
    # S4_dual = 10/(15249/4) = 40/15249

    Delta_dual = 8 * kappa_dual * S4_dual

    # Growth rate
    numer_sq_dual = 9 * S3_dual ** 2 + 2 * Delta_dual
    rho_sq_dual = numer_sq_dual / (4 * kappa_dual ** 2)
    rho_dual = sqrt(rho_sq_dual)

    return {
        'c': c_dual,
        'kappa': cancel(kappa_dual),
        'S3': S3_dual,
        'S4': cancel(S4_dual),
        'Delta': cancel(Delta_dual),
        'rho_squared': cancel(rho_sq_dual),
        'rho': rho_dual,
        'rho_numerical': float(rho_dual.evalf()),
        'convergent': float(rho_dual.evalf()) < 1.0,
        'depth_class': 'M',
        'complementarity_check': {
            'kappa_sum': cancel(Rational(1, 4) + kappa_dual),
            'expected': Rational(13),
        },
    }


def koszul_dual_shadow_tower(max_arity: int = 30) -> Dict[int, float]:
    """Numerical shadow obstruction tower for Koszul dual Vir_{51/2}."""
    c = 51.0 / 2.0
    kappa = c / 2.0
    S3 = 2.0
    S4 = 10.0 / (c * (5.0 * c + 22.0))

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * S3
    q2 = 9.0 * S3 ** 2 + 16.0 * kappa * S4

    max_n = max_arity - 2
    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0)
    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2.0 * a[0])

    return {r: a[r - 2] / r for r in range(2, max_arity + 1)}


# ============================================================================
# 4. Shadow partition function Z^sh through genus 5
# ============================================================================

def lambda_fp(g: int) -> Rational:
    """Faber-Pandharipande intersection number.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    First values: lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    numer = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    denom = 2 ** (2 * g - 1) * factorial(2 * g)
    return Rational(numer, denom)


def ising_free_energy(max_genus: int = 10) -> Dict[int, Rational]:
    """Scalar free energy F_g(Ising) = kappa * lambda_g^FP.

    F_g = (1/4) * lambda_g^FP at the scalar (arity 2) level.

    F_1 = 1/4 * 1/24 = 1/96
    F_2 = 1/4 * 7/5760 = 7/23040
    F_3 = 1/4 * 31/967680 = 31/3870720
    """
    kappa = Rational(1, 4)
    return {g: kappa * lambda_fp(g) for g in range(1, max_genus + 1)}


def ising_shadow_partition_function(max_genus: int = 5) -> Dict[str, Any]:
    r"""Shadow partition function Z^sh through genus max_genus.

    Z^sh(hbar) = exp(sum_{g>=1} F_g * hbar^{2g})

    At the scalar level (arity 2 only):
      F_g = kappa * lambda_g^FP
      sum F_g hbar^{2g} = kappa * (Ahat(i*hbar) - 1)

    where Ahat(x) = (x/2)/sin(x/2), convergent for |hbar| < 2*pi.

    The arity-r corrections are weighted by S_r and lambda_g^FP (higher genus)
    but grow as rho^r ~ 12.5^r at each genus, so the full double sum in
    Convention S diverges in the arity direction.

    This function computes the SCALAR level only (proved, finite, convergent).
    """
    F = ising_free_energy(max_genus)

    # Partial sum of the exponent
    results = {
        'free_energies': F,
        'F_values': {g: float(F[g]) for g in F},
    }

    # Evaluate Z^sh(hbar) at specific points
    for hbar_val in [1.0, PI / 2, PI, 2.0]:
        exponent = sum(float(F[g]) * hbar_val ** (2 * g) for g in F)
        z_sh = math.exp(exponent)
        results[f'Z_sh(hbar={hbar_val:.4f})'] = z_sh
        results[f'exponent(hbar={hbar_val:.4f})'] = exponent

    # Convergence radius: the generating function
    # sum lambda_g x^{2g} = (x/2)/sin(x/2) - 1 has radius 2*pi
    results['convergence_radius'] = 2 * PI
    results['convergent_at_pi'] = True  # pi < 2*pi

    return results


# ============================================================================
# 5. Virasoro characters at c = 1/2 (Rocha-Caridi formula)
# ============================================================================

def _rocha_caridi_theta(p: int, q: int, r: int, s: int,
                        max_exp: int) -> Dict[Fraction, int]:
    """Theta function theta_{r,s} = eta * chi_{r,s} for M(p,q).

    theta_{r,s}(tau) = sum_n [q^{alpha_+(n)} - q^{alpha_-(n)}]
    alpha_pm(n) = ((2npq +/- (rq-sp))^2 - (p-q)^2) / (4pq)
    """
    from math import isqrt

    a = r * q - s * p
    b = r * q + s * p
    M = 2 * p * q
    pq4 = 4 * p * q

    n_max = isqrt(max_exp * pq4) // M + 10
    result: Dict[Fraction, int] = {}

    for n in range(-n_max, n_max + 1):
        # Positive term
        num_plus = (n * M + a) ** 2 - (p - q) ** 2
        if num_plus >= 0:
            exp_plus = Fraction(num_plus, pq4)
            if exp_plus < max_exp:
                result[exp_plus] = result.get(exp_plus, 0) + 1
        # Negative term
        num_minus = (n * M + b) ** 2 - (p - q) ** 2
        if num_minus >= 0:
            exp_minus = Fraction(num_minus, pq4)
            if exp_minus < max_exp:
                result[exp_minus] = result.get(exp_minus, 0) - 1

    return {e: c for e, c in result.items() if c != 0}


def ising_characters(max_terms: int = 25) -> Dict[str, Dict[int, int]]:
    """Virasoro characters at c = 1/2.

    Ising = M(4,3) with primaries:
      (1,1): h = 0        (vacuum, identity 1)
      (2,1): h = 1/16     (spin field sigma)
      (1,2): h = 1/2      (energy operator epsilon)

    Returns integer-indexed coefficients: d_n where
    chi_h(q) = q^{h - c/24} * sum_{n>=0} d_n q^n.

    For the Ising model:
      chi_0:     q^{-1/48} * (1 + q^2 + q^3 + 2q^4 + ...)
      chi_{1/2}: q^{23/48} * (1 + q + q^2 + q^3 + 2q^4 + ...)
      chi_{1/16}: q^{1/24} * (1 + q + q^2 + 2q^3 + 2q^4 + ...)

    Method: compute theta_{r,s} = eta * chi_{r,s} via Rocha-Caridi.
    Then divide by eta (= q^{1/24} * prod(1-q^n)) to get chi.
    The theta functions have fractional exponents; we extract integer-
    indexed relative coefficients by identifying the minimal exponent.
    """
    # Compute eta relative coefficients: prod(1-q^n) = sum c_n q^n
    eta_coeffs = _eta_coefficients(max_terms + 20)

    # Theta functions from Rocha-Caridi
    thetas = {
        '0': _rocha_caridi_theta(4, 3, 1, 1, max_terms + 20),
        '1/16': _rocha_caridi_theta(4, 3, 2, 1, max_terms + 20),
        '1/2': _rocha_caridi_theta(4, 3, 1, 2, max_terms + 20),
    }

    characters = {}
    for label, theta in thetas.items():
        if not theta:
            characters[label] = {n: 0 for n in range(max_terms)}
            continue

        # Find the minimal exponent of theta
        min_exp = min(theta.keys())

        # theta_rel[n]: coefficient of q^{min_exp + n} in theta
        theta_rel: Dict[int, int] = {}
        for exp, coeff in theta.items():
            diff = exp - min_exp
            # diff should be a non-negative integer (or close to it)
            n = int(diff)
            if abs(diff - n) < Fraction(1, 1000):
                theta_rel[n] = theta_rel.get(n, 0) + coeff

        # chi = theta / eta (both as power series, relative to leading powers)
        # theta = eta * chi
        # theta_rel[n] = sum_{k=0}^n eta_coeffs[k] * chi_rel[n-k]
        # => chi_rel[0] = theta_rel[0] / eta_coeffs[0]
        # => chi_rel[n] = (theta_rel[n] - sum_{k=1}^n eta[k]*chi[n-k]) / eta[0]

        chi_rel: Dict[int, int] = {}
        eta0 = eta_coeffs.get(0, 1)  # = 1

        for n in range(max_terms):
            theta_n = theta_rel.get(n, 0)
            correction = sum(
                eta_coeffs.get(k, 0) * chi_rel.get(n - k, 0)
                for k in range(1, n + 1)
            )
            # Integer division since all values should be exact integers
            val = theta_n - correction
            chi_rel[n] = val // eta0 if eta0 != 0 else 0

        characters[label] = chi_rel

    return characters


def _eta_coefficients(max_n: int) -> Dict[int, int]:
    """Coefficients of eta(tau)/q^{1/24} = prod_{n>=1}(1 - q^n).

    Uses the Euler pentagonal theorem:
    prod(1-q^n) = sum_{k=-inf}^{inf} (-1)^k q^{k(3k-1)/2}

    Returns {n: coefficient of q^n} for n = 0, 1, ..., max_n.
    """
    result: Dict[int, int] = {}
    # Pentagonal numbers: k(3k-1)/2 for k = 0, +-1, +-2, ...
    for k in range(-max_n, max_n + 1):
        m = k * (3 * k - 1) // 2
        if 0 <= m <= max_n:
            result[m] = result.get(m, 0) + (-1) ** k
    return result


def ising_partition_function_coefficients(max_n: int = 25) -> Dict[str, Any]:
    """Compute diagonal partition function Z = sum_h |chi_h|^2.

    Returns the q-expansion coefficients for each character and the
    combined partition function.
    """
    chars = ising_characters(max_n)
    return {
        'characters': chars,
        'c': Fraction(1, 2),
        'primaries': ['0', '1/16', '1/2'],
        'conformal_weights': {
            '0': Fraction(0),
            '1/16': Fraction(1, 16),
            '1/2': Fraction(1, 2),
        },
    }


# ============================================================================
# 6. Fusion rules and arity-3 shadow
# ============================================================================

def ising_fusion_rules() -> Dict[Tuple[str, str], List[str]]:
    """Ising fusion rules.

    sigma x sigma = 1 + epsilon
    sigma x epsilon = sigma
    epsilon x epsilon = 1
    """
    return {
        ('sigma', 'sigma'): ['1', 'epsilon'],
        ('sigma', 'epsilon'): ['sigma'],
        ('epsilon', 'sigma'): ['sigma'],
        ('epsilon', 'epsilon'): ['1'],
        ('1', 'sigma'): ['sigma'],
        ('1', 'epsilon'): ['epsilon'],
        ('1', '1'): ['1'],
        ('sigma', '1'): ['sigma'],
        ('epsilon', '1'): ['epsilon'],
    }


def ising_structure_constants() -> Dict[str, Rational]:
    """OPE structure constants for the Ising model.

    C_{sigma sigma epsilon} = 1/2  (the only independent nonzero structure constant)
    C_{epsilon epsilon epsilon} = 0  (Z_2 symmetry)
    C_{sigma sigma 1} = 1  (normalization)
    C_{epsilon epsilon 1} = 1  (normalization)
    """
    return {
        'C_sigma_sigma_epsilon': Rational(1, 2),
        'C_epsilon_epsilon_epsilon': Rational(0),
        'C_sigma_sigma_1': Rational(1),
        'C_epsilon_epsilon_1': Rational(1),
        'C_sigma_epsilon_sigma': Rational(1, 2),
    }


def ising_arity3_shadow() -> Dict[str, Any]:
    """The genus-0, arity-3 shadow amplitude.

    S_3 = 2 for the Virasoro algebra. This is the genus-0 cubic shadow
    on the T-line (stress tensor). It does NOT directly give fusion
    coefficients -- the fusion rules are encoded in the MODULE CATEGORY
    (the collection of Vir-modules and their tensor products), not in
    the vacuum shadow obstruction tower.

    The shadow obstruction tower is a property of the CHIRAL ALGEBRA itself
    (the OPE of the stress tensor T with itself). The fusion rules
    are properties of the REPRESENTATION CATEGORY.

    Relationship: S_3 = 2 controls the genus-0 cubic correction to the
    stress tensor self-coupling. The fusion coefficient N_{sigma,sigma}^epsilon = 1
    is a separate datum from the module category.
    """
    return {
        'S_3': Rational(2),
        'interpretation': 'cubic shadow of T-T-T self-coupling',
        'fusion_relation': 'fusion rules are module-category data, not vacuum shadow data',
        'N_sigma_sigma_epsilon': 1,
        'N_sigma_sigma_1': 1,
        'N_epsilon_epsilon_1': 1,
    }


# ============================================================================
# 7. Critical exponents and the kappa = eta coincidence
# ============================================================================

def ising_critical_exponents() -> Dict[str, Any]:
    """Ising critical exponents and their relation to shadow invariants.

    Standard Ising exponents (2d):
      alpha = 0  (specific heat, logarithmic)
      beta = 1/8  (order parameter)
      gamma = 7/4  (susceptibility)
      delta = 15  (critical isotherm)
      nu = 1  (correlation length)
      eta = 1/4  (anomalous dimension)

    The coincidence kappa = eta = 1/4 is STRUCTURAL, not accidental:

    The anomalous dimension eta controls the power-law decay of the
    two-point function: <sigma(x) sigma(0)> ~ |x|^{-(d-2+eta)} = |x|^{-eta}
    in d=2. This is equivalent to h_sigma = eta/4 for a scalar primary
    in the sigma sector -- but h_sigma = 1/16 = (1/4)/4 = eta/4. CHECK.

    Wait: h_sigma = 1/16, and eta/4 = 1/16. So h_sigma = eta/4. But
    eta = 2*h_sigma * d / (d - 1) -- NO, eta = 2*dim_sigma in d=2 for
    spin-spin correlation. Actually, eta appears in:
      <sigma(r) sigma(0)> ~ r^{-2*Delta_sigma}
    with Delta_sigma = h_sigma + h_bar_sigma = 2*h_sigma (diagonal).
    In d=2: Delta_sigma = 2*(1/16) = 1/8 = beta.
    And eta = 2 - gamma/nu = 2 - 7/4 = 1/4.

    The coincidence kappa = c/2 = 1/4 = eta is NOT deep:
      kappa = c/2 is a property of the ALGEBRA (stress tensor OPE).
      eta = 1/4 is a property of the spin-spin CORRELATOR (module data).
      They coincide numerically at c = 1/2 because c = 2*eta = 2*(2-gamma/nu).
      This gives c = 4 - 2*gamma/nu, which is c-dependent (not universal).
      For the tricritical Ising (c=7/10, eta=3/20): kappa = 7/20 != eta = 3/20.
    """
    exponents = {
        'alpha': 0,
        'beta': Rational(1, 8),
        'gamma': Rational(7, 4),
        'delta': 15,
        'nu': 1,
        'eta': Rational(1, 4),
    }
    kappa = Rational(1, 4)

    # Tricritical check: c = 7/10
    kappa_tri = Rational(7, 20)
    eta_tri = Rational(3, 20)  # from h_sigma' = 3/80, eta = 2 - gamma/nu

    return {
        'exponents': exponents,
        'kappa': kappa,
        'kappa_equals_eta': kappa == exponents['eta'],  # True at c=1/2
        'coincidence_structural': False,  # NOT structural
        'proof': 'kappa = c/2, eta = 2 - gamma/nu. Coincidence at c=1/2 only.',
        'tricritical_check': {
            'c': Rational(7, 10),
            'kappa': kappa_tri,
            'eta': eta_tri,
            'kappa_equals_eta': kappa_tri == eta_tri,  # False
        },
    }


# ============================================================================
# 8. Entanglement entropy with shadow corrections
# ============================================================================

def ising_entanglement_entropy() -> Dict[str, Any]:
    """Entanglement entropy for the Ising model.

    Leading (scalar) term:
      S_EE = (c/3) * log(L/epsilon) = (1/6) * log(L/epsilon)
      S_n = (c/12)(1+1/n) * log(L/epsilon)  (Renyi)

    Shadow corrections from the full tower:
      delta S_EE = sum_{r>=3} contribution from S_r
    These are controlled by the shadow growth rate rho ~ 12.5.
    At c = 1/2 the correction series DIVERGES (rho >> 1), so
    perturbative shadow corrections are meaningless -- one must
    resum the entire tower or use the exact Ising solution.

    The EXACT entanglement entropy is known from the Ising lattice
    solution (Peschel 2003, Calabrese-Cardy 2004):
      S_EE = (1/6) * log(L/epsilon) + s_1
    where s_1 is a non-universal constant.
    """
    c = Rational(1, 2)
    kappa = c / 2

    renyi = {}
    for n in [2, 3, 4, 5, 10]:
        renyi[n] = {
            'formula': f'({c}/12)*(1+1/{n})*log(L/eps)',
            'coefficient': c * (1 + Rational(1, n)) / 12,
        }

    return {
        'c': c,
        'kappa': kappa,
        'S_EE_coefficient': Rational(1, 6),  # c/3
        'S_EE_formula': '(1/6)*log(L/epsilon)',
        'renyi_coefficients': renyi,
        'complementarity': {
            'kappa_A': kappa,
            'kappa_dual': Rational(51, 4),
            'sum': kappa + Rational(51, 4),  # = 13
            'S_EE_sum_coefficient': Rational(13, 3),  # (kappa + kappa')*2/3
        },
        'shadow_corrections_divergent': True,
        'rho': float(sqrt(Rational(7696, 49)).evalf()),
        'resummation_required': True,
    }


def ising_renyi_entropy_coefficient(n: int) -> Rational:
    """Renyi entropy coefficient: S_n = alpha_n * log(L/epsilon).

    alpha_n = (c/12)(1 + 1/n) = (1/24)(1 + 1/n) = (n+1)/(24n).
    """
    c = Rational(1, 2)
    return c * (1 + Rational(1, n)) / 12


# ============================================================================
# 9. Comparison: Ising vs tricritical Ising (c=7/10)
# ============================================================================

def tricritical_ising_shadow_data() -> Dict[str, Any]:
    """Shadow data for the tricritical Ising model M(5,4), c = 7/10.

    kappa = 7/20
    S_3 = 2
    S_4 = 10/[(7/10)*(5*7/10 + 22)] = 10/[(7/10)*(57/2)] = 10/(399/20) = 200/399
    Delta = 8*(7/20)*(200/399) = 8*1400/7980 = 11200/7980 = 1600/1140 = 160/114 = 80/57
    """
    c = C_TRICRITICAL
    kappa = c / 2  # 7/20
    S3 = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    Delta = 8 * kappa * S4

    numer_sq = 9 * S3 ** 2 + 2 * Delta
    rho_sq = numer_sq / (4 * kappa ** 2)
    rho = sqrt(rho_sq)

    return {
        'c': c,
        'name': 'tricritical Ising M(5,4)',
        'kappa': cancel(kappa),
        'S3': S3,
        'S4': cancel(S4),
        'Delta': cancel(Delta),
        'rho_squared': cancel(rho_sq),
        'rho_numerical': float(rho.evalf()),
        'convergent': float(rho.evalf()) < 1.0,
        'depth_class': 'M',
    }


def tricritical_ising_shadow_tower(max_arity: int = 30) -> Dict[int, float]:
    """Numerical shadow obstruction tower for tricritical Ising at c = 7/10."""
    c = 0.7
    kappa = c / 2.0
    S3 = 2.0
    S4 = 10.0 / (c * (5.0 * c + 22.0))

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * S3
    q2 = 9.0 * S3 ** 2 + 16.0 * kappa * S4

    max_n = max_arity - 2
    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0)
    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2.0 * a[0])

    return {r: a[r - 2] / r for r in range(2, max_arity + 1)}


def compare_ising_tricritical() -> Dict[str, Any]:
    """Side-by-side comparison of Ising (c=1/2) vs tricritical Ising (c=7/10).

    Both are unitary minimal models (class M, infinite shadow depth).
    Both have divergent shadow obstruction towers (c < c* ~ 6.12).
    The tricritical model has 6 primaries vs 3 for Ising.
    """
    ising_data = ising_shadow_data()
    tri_data = tricritical_ising_shadow_data()

    ising_tower = ising_shadow_tower_numerical(20)
    tri_tower = tricritical_ising_shadow_tower(20)

    return {
        'ising': {
            'c': Rational(1, 2),
            'kappa': Rational(1, 4),
            'rho': ising_data['rho_numerical'],
            'S_4': float(Rational(40, 49)),
            'Delta': float(Rational(80, 49)),
            'first_5': {r: ising_tower[r] for r in range(2, 7)},
        },
        'tricritical': {
            'c': Rational(7, 10),
            'kappa': float(Rational(7, 20)),
            'rho': tri_data['rho_numerical'],
            'S_4': float(tri_data['S4']),
            'Delta': float(tri_data['Delta']),
            'first_5': {r: tri_tower[r] for r in range(2, 7)},
        },
        'both_divergent': True,
        'ising_more_divergent': ising_data['rho_numerical'] > tri_data['rho_numerical'],
    }


# ============================================================================
# 10. Onsager exact solution comparison
# ============================================================================

def ising_onsager_comparison() -> Dict[str, Any]:
    """Compare shadow obstruction tower predictions with the exact Onsager solution.

    The Onsager solution gives the EXACT free energy of the 2d Ising model
    on a torus. The shadow partition function gives the PERTURBATIVE
    expansion in arity of the bar complex MC element.

    Key point: these are DIFFERENT objects.
      - Onsager: exact thermodynamic free energy F_thermo.
      - Shadow PF: Z^sh = exp(sum F_g hbar^{2g}) where F_g = kappa * lambda_g.

    The shadow PF captures the ALGEBRAIC structure (the MC element Theta_A)
    but not the thermodynamic limit directly. The connection goes through:
      1. Ising CFT partition function Z_CFT = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2
      2. The shadow PF encodes the BAR COMPLEX of the chiral algebra
      3. The relation to physics goes through genus expansion of the worldsheet

    At genus 1 (torus): F_1 = kappa/24 = 1/96 (shadow prediction)
    The actual torus partition function Z_torus = Z_CFT(tau) depends on the
    modular parameter tau, while F_1 is the INTEGRATED value int_{M_{1,1}} psi lambda_1.

    Onsager's exact critical temperature: T_c = 2J / (k_B * log(1 + sqrt(2)))
    where J is the coupling constant.
    """
    kappa = Rational(1, 4)
    F1 = kappa / 24

    return {
        'F_1_shadow': F1,
        'F_1_numerical': float(F1),
        'comparison': 'shadow F_g are tautological integrals, not thermodynamic free energies',
        'onsager_T_c': 'T_c = 2J/(k_B * log(1+sqrt(2)))',
        'relationship': (
            'The shadow partition function is the generating function of '
            'tautological intersection numbers weighted by kappa. '
            'The physical partition function is Z_CFT(tau). '
            'They are related by the factorization-homology functor at genus g.'
        ),
    }


# ============================================================================
# 11. Complete analysis driver
# ============================================================================

def complete_ising_analysis(max_arity: int = 20, max_genus: int = 5) -> Dict[str, Any]:
    """Run the complete Ising shadow analysis.

    Returns all shadow invariants, growth rates, characters, and comparisons.
    """
    return {
        'shadow_data': ising_shadow_data(),
        'shadow_tower': ising_shadow_tower(min(max_arity, 15)),
        'growth_rate': ising_growth_rate_exact(),
        'convergence': ising_convergence_analysis(max_arity),
        'koszul_dual': koszul_dual_shadow_data(),
        'shadow_pf': ising_shadow_partition_function(max_genus),
        'free_energies': ising_free_energy(max_genus),
        'fusion_rules': ising_fusion_rules(),
        'structure_constants': ising_structure_constants(),
        'critical_exponents': ising_critical_exponents(),
        'entanglement': ising_entanglement_entropy(),
        'comparison': compare_ising_tricritical(),
    }
