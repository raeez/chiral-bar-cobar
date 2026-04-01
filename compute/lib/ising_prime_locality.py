r"""
ising_prime_locality.py -- Adversarial test of prime-locality for the Ising model.

The Ising model is M(4,3), c = 1/2, with three primaries:
    (1,1): h = 0        (identity)
    (2,1): h = 1/16     (spin field sigma)
    (1,2): h = 1/2      (energy operator epsilon)

The diagonal partition function is:
    Z_Ising(tau) = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2

ATTACK on prop:rational-cft-multiplicativity-failure:
1. Compute a_n = coefficients of |eta|^2 Z for n = 0,...,N
2. Test multiplicativity: a_{mn} = a_m * a_n for gcd(m,n) = 1
3. Verify the manuscript claim of 14 coprime failures with mn <= 20
4. Analyze whether a modified Dirichlet series is multiplicative
5. Test whether failures correlate with arithmetic of Q(sqrt(5))

TWO CONVENTIONS:
  Convention A (manuscript/existing code): the "flattened" coefficients.
    For each primary (r,s), compute theta_{r,s}^2 = (eta*chi_{r,s})^2
    at integer levels above the channel ground state, then sum across
    channels. This drops the fractional q-power offset between channels.
    The result has integer Fourier coefficients.
    This is what the manuscript means by "a_n" and is the basis for
    the "14 coprime failures" claim (with mn <= 20).

  Convention B (exact): |eta|^2 Z = sum_i |theta_i|^2 with exact
    fractional q-exponents. The exponents lie in Z (identity + energy)
    and Z + 1/8 (spin channel). These are genuinely different objects:
    Convention A sums terms at different q-powers as if they were at
    the same power.

FINDING: Convention A is mathematically INCORRECT as a q-expansion of
|eta|^2 Z, but the manuscript's claim about 14 failures is numerically
correct under Convention A.

Shadow tower at c = 1/2:
    kappa = 1/4, S_4 = 40/49, Delta = 80/49.
    sqrt(Delta) = 4*sqrt(5)/7 -- this is where Q(sqrt(5)) enters.
    The shadow metric discriminant disc(Q) = -160/49 involves sqrt(-10).

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt
from typing import Any, Dict, List, Optional, Tuple


# ===========================================================================
# Rocha-Caridi theta functions (exact integer arithmetic)
# ===========================================================================

def rocha_caridi_theta(
    p: int, q: int, r: int, s: int, num_terms: int,
) -> Dict[Fraction, int]:
    """Compute theta_{r,s} = eta * chi_{r,s} for M(p,q) via Rocha-Caridi.

    Returns {Fraction exponent: integer coefficient} where
    theta_{r,s}(tau) = sum_n [q^{alpha_+(n)} - q^{alpha_-(n)}],
    alpha_pm(n) = ((2npq +/- (rq-sp))^2 - (p-q)^2) / (4pq).
    """
    a = r * q - s * p
    b = r * q + s * p
    M = 2 * p * q
    pq4 = 4 * p * q

    n_max = isqrt(num_terms * pq4) // M + 5
    result: Dict[Fraction, int] = {}

    for n in range(-n_max, n_max + 1):
        # Positive term
        num_plus = (n * M + a) ** 2 - (p - q) ** 2
        if num_plus >= 0:
            exp_plus = Fraction(num_plus, pq4)
            if exp_plus < num_terms:
                result[exp_plus] = result.get(exp_plus, 0) + 1
        # Negative term
        num_minus = (n * M + b) ** 2 - (p - q) ** 2
        if num_minus >= 0:
            exp_minus = Fraction(num_minus, pq4)
            if exp_minus < num_terms:
                result[exp_minus] = result.get(exp_minus, 0) - 1

    return {e: c for e, c in result.items() if c != 0}


def ising_theta_functions(num_terms: int = 200) -> Dict[str, Dict[Fraction, int]]:
    """Theta functions for each Ising primary."""
    return {
        '0': rocha_caridi_theta(4, 3, 1, 1, num_terms),
        '1/16': rocha_caridi_theta(4, 3, 2, 1, num_terms),
        '1/2': rocha_caridi_theta(4, 3, 1, 2, num_terms),
    }


# ===========================================================================
# Series operations (exact)
# ===========================================================================

def _square_series(
    theta: Dict[Fraction, int], max_exp: int,
) -> Dict[Fraction, int]:
    """Compute theta^2 as a fractional-exponent power series."""
    result: Dict[Fraction, int] = {}
    exps = sorted(theta.keys())
    for i, e1 in enumerate(exps):
        c1 = theta[e1]
        if c1 == 0:
            continue
        for e2 in exps[i:]:
            c2 = theta[e2]
            if c2 == 0:
                continue
            E = e1 + e2
            if E >= max_exp:
                break
            contrib = c1 * c2 * (1 if e1 == e2 else 2)
            result[E] = result.get(E, 0) + contrib
    return {e: c for e, c in result.items() if c != 0}


# ===========================================================================
# Convention B: exact |eta|^2 Z with fractional exponents
# ===========================================================================

def ising_eta_sq_z_exact(num_terms: int = 200) -> Dict[Fraction, int]:
    """Exact |eta|^2 Z = sum_i |theta_i|^2 with fractional exponents."""
    thetas = ising_theta_functions(num_terms)
    result: Dict[Fraction, int] = {}
    for theta in thetas.values():
        sq = _square_series(theta, num_terms)
        for exp, coeff in sq.items():
            result[exp] = result.get(exp, 0) + coeff
    return {e: c for e, c in result.items() if c != 0}


def ising_integer_coeffs_exact(num_terms: int = 200) -> List[int]:
    """Integer-exponent part of |eta|^2 Z (identity + energy channels)."""
    full = ising_eta_sq_z_exact(num_terms)
    result = [0] * num_terms
    for exp, coeff in full.items():
        if exp.denominator == 1:
            k = int(exp)
            if 0 <= k < num_terms:
                result[k] += coeff
    return result


def ising_spin_coeffs_exact(num_terms: int = 200) -> Dict[int, int]:
    """Z+1/8 exponent part of |eta|^2 Z (spin channel).

    Returns {k: A_k} where the contribution is A_k * q^{k + 1/8}.
    """
    full = ising_eta_sq_z_exact(num_terms)
    result: Dict[int, int] = {}
    for exp, coeff in full.items():
        shifted = exp - Fraction(1, 8)
        if shifted.denominator == 1:
            k = int(shifted)
            result[k] = result.get(k, 0) + coeff
    return {k: c for k, c in result.items() if c != 0}


# ===========================================================================
# Convention A: flattened coefficients (matching manuscript/existing code)
# ===========================================================================

def ising_flattened_coeffs(num_terms: int = 200) -> List[int]:
    """Compute flattened Dirichlet coefficients (Convention A).

    For each primary, align theta_i^2 at the channel's ground state
    (stripping the fractional q-power), then sum across channels.
    Matches minimal_model_l_functions.py and the manuscript.
    """
    thetas = ising_theta_functions(num_terms)
    result = [0] * num_terms

    for theta in thetas.values():
        sq = _square_series(theta, num_terms)
        if not sq:
            continue
        min_exp = min(sq.keys())
        for exp, coeff in sq.items():
            offset = exp - min_exp
            if offset.denominator == 1:
                k = int(offset)
                if 0 <= k < num_terms:
                    result[k] += coeff
    return result


# ===========================================================================
# Multiplicativity testing
# ===========================================================================

def check_multiplicativity_product_bound(
    coeffs: List[int],
    max_product: int = 20,
) -> Tuple[bool, List[Tuple[int, int, int, int, int]]]:
    """Test a_{mn} = a_m * a_n for gcd(m,n) = 1 with mn <= max_product.

    This matches the existing code's convention where max_n controls
    the product bound (m*n < max_n + 1), not the individual m, n.

    Returns (is_mult, failures) where each failure is
    (m, n, a_mn, a_m*a_n, defect). Includes both orderings (m,n) and (n,m).
    """
    failures = []
    N = min(max_product + 1, len(coeffs))
    for m in range(2, N):
        for n in range(2, N):
            if m * n >= N:
                break
            if gcd(m, n) != 1:
                continue
            a_mn = coeffs[m * n]
            a_m_a_n = coeffs[m] * coeffs[n]
            if a_mn != a_m_a_n:
                failures.append((m, n, a_mn, a_m_a_n, a_mn - a_m_a_n))
    return (len(failures) == 0, failures)


def check_multiplicativity_individual_bound(
    coeffs: List[int],
    max_n: int = 30,
) -> Tuple[bool, List[Tuple[int, int, int, int, int]]]:
    """Test a_{mn} = a_m * a_n for gcd(m,n) = 1 with 2 <= m <= n <= max_n.

    Unordered pairs only (m <= n). Requires m*n < len(coeffs).
    """
    failures = []
    for m in range(2, max_n + 1):
        for n in range(m, max_n + 1):
            if m * n >= len(coeffs):
                break
            if gcd(m, n) != 1:
                continue
            a_mn = coeffs[m * n]
            a_m_a_n = coeffs[m] * coeffs[n]
            if a_mn != a_m_a_n:
                failures.append((m, n, a_mn, a_m_a_n, a_mn - a_m_a_n))
    return (len(failures) == 0, failures)


# ===========================================================================
# Arithmetic analysis
# ===========================================================================

def is_prime(n: int) -> bool:
    """Simple primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def legendre_symbol(a: int, p: int) -> int:
    """Legendre symbol (a/p) for odd prime p."""
    a = a % p
    if a == 0:
        return 0
    result = pow(a, (p - 1) // 2, p)
    return result if result <= 1 else result - p


def splitting_in_Q_sqrt5(p: int) -> str:
    """Splitting behavior of prime p in Q(sqrt(5)).

    disc(Q(sqrt(5))) = 5. By quadratic reciprocity:
    p = 2: 5 mod 8 = 5, so 2 is INERT.
    p = 5: ramifies.
    p odd != 5: splits iff (5/p) = 1 iff p = +/-1 mod 5.
    """
    if p == 5:
        return 'ramified'
    if p == 2:
        return 'inert'
    return 'split' if legendre_symbol(5, p) == 1 else 'inert'


def splitting_in_Q_sqrt_neg10(p: int) -> str:
    """Splitting behavior of prime p in Q(sqrt(-10)).

    disc = -40. p | 40 ramifies. Otherwise p splits iff (-10/p) = 1.
    """
    if p in (2, 5):
        return 'ramified'
    neg1 = legendre_symbol(-1, p)
    two = pow(2, (p - 1) // 2, p)
    if two > 1:
        two -= p
    five = legendre_symbol(5, p)
    return 'split' if neg1 * two * five == 1 else 'inert'


def prime_factors(n: int) -> List[int]:
    """Prime factors of n (with repetition)."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def analyze_failure_arithmetic(
    failures: List[Tuple[int, int, int, int, int]],
) -> Dict[str, Any]:
    """Analyze multiplicativity failures against Q(sqrt(5)) and Q(sqrt(-10))."""
    failure_primes = set()
    for m, n, _, _, _ in failures:
        for x in [m, n]:
            failure_primes.update(prime_factors(x))

    max_p = max(failure_primes) if failure_primes else 2
    all_primes = [p for p in range(2, max_p + 1) if is_prime(p)]

    def classify(primes, field_fn):
        data = {p: field_fn(p) for p in sorted(primes)}
        counts = {'split': 0, 'inert': 0, 'ramified': 0}
        for v in data.values():
            counts[v] += 1
        return data, counts

    fp_sorted = sorted(failure_primes)
    sqrt5_data, sqrt5_counts = classify(fp_sorted, splitting_in_Q_sqrt5)
    neg10_data, neg10_counts = classify(fp_sorted, splitting_in_Q_sqrt_neg10)
    _, base_sqrt5 = classify(all_primes, splitting_in_Q_sqrt5)
    _, base_neg10 = classify(all_primes, splitting_in_Q_sqrt_neg10)

    return {
        'failure_primes': fp_sorted,
        'Q_sqrt5': {
            'splitting': sqrt5_data,
            'counts': sqrt5_counts,
            'baseline': base_sqrt5,
        },
        'Q_sqrt_neg10': {
            'splitting': neg10_data,
            'counts': neg10_counts,
            'baseline': base_neg10,
        },
    }


# ===========================================================================
# Per-channel multiplicativity
# ===========================================================================

def per_channel_multiplicativity_test(
    num_terms: int = 200,
    max_n: int = 30,
) -> Dict[str, Any]:
    """Test multiplicativity of each Ising channel separately.

    For the identity channel, exponents are integers.
    For the spin channel, exponents are in Z + 1/8.
    For the energy channel, exponents are integers starting from 1.
    """
    thetas = ising_theta_functions(num_terms)
    results = {}

    for name, theta in thetas.items():
        sq = _square_series(theta, num_terms)
        if not sq:
            results[name] = {'note': 'empty'}
            continue

        denoms = set(e.denominator for e in sq)
        lcd = 1
        for d in denoms:
            lcd = lcd * d // gcd(lcd, d)

        max_k = min(num_terms * lcd, 2000)
        Q_coeffs = [0] * max_k
        for exp, coeff in sq.items():
            k = int(exp * lcd)
            if 0 <= k < max_k:
                Q_coeffs[k] += coeff

        test_max = min(max_n * lcd, max_k - 1)
        _, failures = check_multiplicativity_individual_bound(Q_coeffs, max_n=test_max)

        results[name] = {
            'lcd': lcd,
            'num_nonzero': sum(1 for c in Q_coeffs if c != 0),
            'is_multiplicative': len(failures) == 0,
            'num_failures': len(failures),
            'first_failures': failures[:5],
            'first_coeffs': [Q_coeffs[k] for k in range(min(20, max_k))],
        }

    return results


# ===========================================================================
# Modified Dirichlet series
# ===========================================================================

def hecke_recursion_test(
    coeffs: List[int],
) -> Dict[int, Dict[str, Any]]:
    """Test Hecke recursion at prime squares: a_{p^2} vs a_p^2.

    For a weight-k Hecke eigenform: a_{p^2} = a_p^2 - chi(p)*p^{k-1}.
    The defect d(p) = a_{p^2} - a_p^2 should factor as -chi(p)*p^{k-1}
    for some Dirichlet character chi and weight k.
    """
    primes = [p for p in range(2, 20) if is_prime(p)]
    result = {}
    for p in primes:
        if p * p < len(coeffs) and p < len(coeffs):
            a_p = coeffs[p]
            a_p2 = coeffs[p * p]
            defect = a_p2 - a_p * a_p
            result[p] = {
                'a_p': a_p,
                'a_{p^2}': a_p2,
                'a_p^2': a_p * a_p,
                'defect': defect,
            }
    return result


# ===========================================================================
# Shadow tower data
# ===========================================================================

def ising_shadow_data() -> Dict[str, Any]:
    """Shadow tower invariants at c = 1/2.

    kappa = 1/4, S_4 = 40/49, Delta = 80/49.
    sqrt(Delta) = 4*sqrt(5)/7, so Q(sqrt(5)) enters via Delta.
    But the shadow metric discriminant disc(Q) = -160/49 involves sqrt(-10).
    """
    c = Fraction(1, 2)
    kappa = c / 2                                    # 1/4
    S4 = Fraction(10) / (c * (5 * c + 22))           # 40/49
    Delta = 8 * kappa * S4                            # 80/49
    alpha_q = (180 * c + 872) / (5 * c + 22)         # 1924/49
    disc_Q = 4 * c * c * (36 - alpha_q)              # -160/49

    # Shadow radius: rho = sqrt(9*S_3^2 + 2*Delta) / (2*kappa)
    import math
    rho = math.sqrt(float(9 * 4 + 2 * Delta)) / (2 * float(kappa))

    return {
        'c': '1/2',
        'kappa': str(kappa),
        'S4': str(S4),
        'Delta': str(Delta),
        'sqrt_Delta': '4*sqrt(5)/7',
        'disc_shadow_metric': str(disc_Q),
        'disc_involves': 'sqrt(-10)',
        'shadow_radius': rho,
        'class': 'M (infinite tower)',
    }


# ===========================================================================
# Full adversarial report
# ===========================================================================

def full_ising_attack(
    num_terms: int = 200,
    max_test: int = 30,
) -> Dict[str, Any]:
    """Run full adversarial attack on Ising prime-locality."""
    report: Dict[str, Any] = {}

    # Convention A (flattened, matching manuscript)
    flat = ising_flattened_coeffs(num_terms)
    report['conv_A_coeffs'] = flat[:31]
    _, fail_A_product = check_multiplicativity_product_bound(flat, max_product=20)
    _, fail_A_individual = check_multiplicativity_individual_bound(flat, max_n=max_test)
    report['conv_A'] = {
        'product_bound_20_failures': len(fail_A_product),
        'manuscript_claims_14': len(fail_A_product) == 14,
        'individual_bound_failures': len(fail_A_individual),
        'first_product_failures': fail_A_product[:10],
        'first_individual_failures': fail_A_individual[:10],
    }

    # Convention B (exact)
    exact = ising_integer_coeffs_exact(num_terms)
    report['conv_B_coeffs'] = exact[:31]
    _, fail_B = check_multiplicativity_individual_bound(exact, max_n=max_test)
    report['conv_B'] = {
        'failures': len(fail_B),
        'first_failures': fail_B[:10],
    }

    report['conventions_agree'] = (flat[:31] == exact[:31])

    # Arithmetic
    report['arithmetic'] = analyze_failure_arithmetic(fail_A_individual)

    # Per-channel
    report['per_channel'] = per_channel_multiplicativity_test(num_terms, max_n=15)

    # Hecke
    report['hecke'] = hecke_recursion_test(flat)

    # Shadow
    report['shadow'] = ising_shadow_data()

    return report
