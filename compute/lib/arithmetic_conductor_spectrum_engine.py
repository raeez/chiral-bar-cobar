r"""Arithmetic conductor spectrum of the shadow obstruction tower.

For a modular Koszul algebra A with shadow tower {S_r}_{r>=2}, define:

    N_r(A) = |denominator(S_r(A))|  (S_r in lowest terms)

    N(A) = lcm{N_r(A) : r >= 2}       (full arithmetic conductor)

    N_R(A) = lcm{N_r(A) : 2 <= r <= R}  (R-truncated conductor)

For finite towers (class G, L, C): N(A) is finite and equals N_R for R >= r_max.
For infinite towers (class M): N(A) may be infinite. The truncated conductor
N_R(A) and its growth rate gamma(A) = lim log(N_R)/R classify the prime-
arithmetic complexity of the shadow tower.

PRIME FACTORIZATION SPECTRUM:
    P(A) = {primes dividing N_R(A) for some R}

For Virasoro at c = p/q (rational):
    - S_2 = c/2 = p/(2q): primes from {2} union prime_factors(q)
    - S_4 = 10/(c(5c+22)): primes from prime_factors(c) union prime_factors(5c+22)
    - Higher S_r introduce new primes through the recursion a_n = -conv/(2*a_0)

CONDUCTOR-DISCRIMINANT COMPARISON:
    Delta(A) = 8*kappa*S_4 classifies shadow depth.
    N(A) encodes prime arithmetic. The relation N | den(Delta) is checked.

COMPLEMENTARITY:
    For a Koszul pair (A, A!): N(A) * N(A!) and gcd(N(A), N(A!)) are computed.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from functools import reduce
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from sympy import (
    Rational,
    factorint,
    gcd as sym_gcd,
    lcm as sym_lcm,
    Integer,
    Abs,
    N as Neval,
    oo,
    sqrt,
)


# =============================================================================
# 1. Exact rational shadow tower computation (Fraction-based for speed)
# =============================================================================

def shadow_tower_exact(
    kappa: Fraction,
    alpha: Fraction,
    S4: Fraction,
    max_r: int = 30,
) -> Dict[int, Fraction]:
    r"""Compute shadow tower coefficients S_2, ..., S_{max_r} as exact Fractions.

    Uses the convolution recursion for sqrt(Q_L(t)):
        a_0 = 2*kappa
        a_1 = q1 / (2*a_0) = 3*alpha
        a_2 = (q2 - a_1^2) / (2*a_0) = 4*S4
        a_n = -(sum_{j=1}^{n-1} a_j*a_{n-j}) / (2*a_0)  for n >= 3

    Then S_r = a_{r-2} / r.
    """
    if kappa == 0:
        raise ValueError("kappa = 0: shadow tower undefined (uncurved algebra)")

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    a0 = 2 * kappa
    a = [a0]

    max_n = max_r - 2

    if max_n >= 1:
        a1 = q1 / (2 * a0)  # = 3*alpha
        a.append(a1)

    if max_n >= 2:
        a2 = (q2 - a[1] ** 2) / (2 * a0)  # = 4*S4
        a.append(a2)

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        an = -conv / (2 * a0)
        a.append(an)

    result: Dict[int, Fraction] = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = a[idx] / r

    return result


# =============================================================================
# 2. Arithmetic conductor definitions
# =============================================================================

def denominator_abs(x: Fraction) -> int:
    """Absolute value of the denominator of x in lowest terms."""
    if x == 0:
        return 1
    f = Fraction(x).limit_denominator(10**30)
    return abs(f.denominator)


def conductor_at_arity(S_r: Fraction) -> int:
    """N_r = |den(S_r)| in lowest terms."""
    if S_r == 0:
        return 1  # denominator of 0 is 1
    return denominator_abs(S_r)


def _lcm(a: int, b: int) -> int:
    """Least common multiple of two positive integers."""
    return abs(a * b) // math.gcd(a, b)


def truncated_conductor(
    tower: Dict[int, Fraction],
    R: int,
) -> int:
    """N_R(A) = lcm{N_r(A) : 2 <= r <= R}."""
    result = 1
    for r in range(2, R + 1):
        if r in tower:
            nr = conductor_at_arity(tower[r])
            result = _lcm(result, nr)
    return result


def full_conductor(tower: Dict[int, Fraction]) -> int:
    """N(A) = lcm{N_r(A) : r in tower}."""
    result = 1
    for r in sorted(tower.keys()):
        nr = conductor_at_arity(tower[r])
        result = _lcm(result, nr)
    return result


def conductor_sequence(
    tower: Dict[int, Fraction],
    max_R: int = None,
) -> Dict[int, int]:
    """Compute N_R for R = 2, ..., max_R."""
    if max_R is None:
        max_R = max(tower.keys()) if tower else 2
    result: Dict[int, int] = {}
    running_lcm = 1
    for R in range(2, max_R + 1):
        if R in tower:
            nr = conductor_at_arity(tower[R])
            running_lcm = _lcm(running_lcm, nr)
        result[R] = running_lcm
    return result


# =============================================================================
# 3. Conductor growth rate
# =============================================================================

def conductor_growth_rate(
    conductor_seq: Dict[int, int],
    window: int = 5,
) -> float:
    r"""Exponential growth rate gamma = lim log(N_R) / R.

    Estimated from the tail of the conductor sequence.
    For class G/L/C: gamma = 0 (N_R stabilizes).
    For class M: gamma may be positive.
    """
    Rs = sorted(conductor_seq.keys())
    if len(Rs) < 2:
        return 0.0

    # Use the last `window` points for linear regression of log(N_R) vs R
    tail = Rs[-window:] if len(Rs) >= window else Rs
    log_vals = []
    for R in tail:
        N = conductor_seq[R]
        if N > 0:
            log_vals.append((R, math.log(N)))

    if len(log_vals) < 2:
        return 0.0

    # Simple linear regression
    n = len(log_vals)
    sum_x = sum(p[0] for p in log_vals)
    sum_y = sum(p[1] for p in log_vals)
    sum_xy = sum(p[0] * p[1] for p in log_vals)
    sum_xx = sum(p[0] ** 2 for p in log_vals)

    denom = n * sum_xx - sum_x ** 2
    if abs(denom) < 1e-15:
        return 0.0

    slope = (n * sum_xy - sum_x * sum_y) / denom
    return max(slope, 0.0)  # gamma >= 0


def conductor_stabilizes_at(conductor_seq: Dict[int, int]) -> Optional[int]:
    """Return the smallest R such that N_R = N_{R'} for all R' >= R, or None."""
    Rs = sorted(conductor_seq.keys())
    if len(Rs) < 2:
        return Rs[0] if Rs else None

    final_val = conductor_seq[Rs[-1]]
    # Check from the beginning: first R where N_R = final_val
    for R in Rs:
        if conductor_seq[R] == final_val:
            # Verify all subsequent are the same
            if all(conductor_seq[R2] == final_val for R2 in Rs if R2 >= R):
                return R
    return None


# =============================================================================
# 4. Prime factorization spectrum
# =============================================================================

def prime_factors(n: int) -> Set[int]:
    """Set of prime factors of |n|."""
    if n == 0:
        return set()
    n = abs(n)
    if n == 1:
        return set()
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors


def prime_spectrum(
    tower: Dict[int, Fraction],
    max_R: int = None,
) -> Set[int]:
    """P(A) = {primes dividing N_R for some R}."""
    if max_R is None:
        max_R = max(tower.keys()) if tower else 2
    primes: Set[int] = set()
    for r in range(2, max_R + 1):
        if r in tower:
            nr = conductor_at_arity(tower[r])
            primes |= prime_factors(nr)
    return primes


def prime_spectrum_by_arity(
    tower: Dict[int, Fraction],
    max_R: int = None,
) -> Dict[int, Set[int]]:
    """For each arity r, the set of new primes introduced at that arity."""
    if max_R is None:
        max_R = max(tower.keys()) if tower else 2
    seen: Set[int] = set()
    result: Dict[int, Set[int]] = {}
    for r in range(2, max_R + 1):
        if r in tower:
            nr = conductor_at_arity(tower[r])
            new_primes = prime_factors(nr) - seen
            result[r] = new_primes
            seen |= new_primes
        else:
            result[r] = set()
    return result


def prime_valuation_profile(
    tower: Dict[int, Fraction],
    p: int,
    max_R: int = None,
) -> Dict[int, int]:
    """v_p(N_r) for each arity r: the p-adic valuation of the conductor at arity r."""
    if max_R is None:
        max_R = max(tower.keys()) if tower else 2
    result: Dict[int, int] = {}
    for r in range(2, max_R + 1):
        if r in tower:
            nr = conductor_at_arity(tower[r])
            v = 0
            temp = nr
            while temp > 0 and temp % p == 0:
                v += 1
                temp //= p
            result[r] = v
        else:
            result[r] = 0
    return result


# =============================================================================
# 5. Discriminant-conductor comparison
# =============================================================================

def discriminant_conductor_relation(
    kappa: Fraction,
    S4: Fraction,
    tower: Dict[int, Fraction],
    max_R: int = None,
) -> Dict[str, Any]:
    r"""Compare conductor N(A) with discriminant Delta = 8*kappa*S4.

    Checks:
    - Whether N divides |numerator(Delta)| or |denominator(Delta)|
    - Common prime factors
    - N / gcd(N, den(Delta))
    """
    Delta = 8 * kappa * S4
    N = full_conductor(tower) if max_R is None else truncated_conductor(tower, max_R)

    Delta_num = abs(Delta.numerator)
    Delta_den = abs(Delta.denominator)

    N_primes = prime_factors(N)
    Delta_num_primes = prime_factors(Delta_num) if Delta_num != 0 else set()
    Delta_den_primes = prime_factors(Delta_den)

    return {
        'Delta': Delta,
        'Delta_numerator': Delta_num,
        'Delta_denominator': Delta_den,
        'N': N,
        'N_divides_Delta_den': (Delta_den % N == 0) if N > 0 else False,
        'Delta_den_divides_N': (N % Delta_den == 0) if Delta_den > 0 else False,
        'common_primes': N_primes & (Delta_num_primes | Delta_den_primes),
        'N_primes': N_primes,
        'Delta_primes': Delta_num_primes | Delta_den_primes,
        'excess_primes': N_primes - (Delta_num_primes | Delta_den_primes),
    }


# =============================================================================
# 6. Complementarity of conductors
# =============================================================================

def complementarity_conductors(
    tower_A: Dict[int, Fraction],
    tower_A_dual: Dict[int, Fraction],
    max_R: int = None,
) -> Dict[str, Any]:
    """Compare conductors of a Koszul pair (A, A!).

    Computes N(A), N(A!), product, gcd, lcm, and per-arity comparison.
    """
    N_A = full_conductor(tower_A) if max_R is None else truncated_conductor(tower_A, max_R)
    N_Ad = full_conductor(tower_A_dual) if max_R is None else truncated_conductor(tower_A_dual, max_R)

    product = N_A * N_Ad
    g = math.gcd(N_A, N_Ad)
    l = _lcm(N_A, N_Ad)

    # Check if product is a perfect square
    is_square = False
    if product > 0:
        s = int(math.isqrt(product))
        is_square = (s * s == product)

    # Per-arity comparison
    per_arity: Dict[int, Dict[str, int]] = {}
    all_arities = sorted(set(tower_A.keys()) | set(tower_A_dual.keys()))
    for r in all_arities:
        n_a = conductor_at_arity(tower_A.get(r, Fraction(0)))
        n_ad = conductor_at_arity(tower_A_dual.get(r, Fraction(0)))
        per_arity[r] = {
            'N_r_A': n_a,
            'N_r_dual': n_ad,
            'product': n_a * n_ad,
            'gcd': math.gcd(n_a, n_ad),
        }

    return {
        'N_A': N_A,
        'N_A_dual': N_Ad,
        'product': product,
        'product_is_perfect_square': is_square,
        'gcd': g,
        'lcm': l,
        'per_arity': per_arity,
    }


# =============================================================================
# 7. Standard family data (Fraction-based)
# =============================================================================

def heisenberg_shadow_data(k: Fraction) -> Dict[str, Any]:
    """Heisenberg H_k: kappa = k, alpha = 0, S4 = 0. Class G."""
    return {
        'name': f'H_{{{k}}}',
        'type': 'Heisenberg',
        'kappa': k,
        'alpha': Fraction(0),
        'S4': Fraction(0),
        'class': 'G',
        'kappa_dual': -k,
    }


def virasoro_shadow_data(c: Fraction) -> Dict[str, Any]:
    """Virasoro Vir_c: kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)). Class M."""
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    c_dual = 26 - c
    kappa_dual = c_dual / 2
    return {
        'name': f'Vir_{{{c}}}',
        'type': 'Virasoro',
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'M',
        'c_dual': c_dual,
        'kappa_dual': kappa_dual,
    }


def affine_sl2_shadow_data(k: Fraction) -> Dict[str, Any]:
    """Affine sl_2 at level k: kappa = 3(k+2)/4, alpha = 1, S4 = 0. Class L."""
    kappa = Fraction(3) * (k + 2) / 4
    alpha = Fraction(1)
    S4 = Fraction(0)
    k_dual = -k - 4  # FF involution: k -> -k - 2h^vee, h^vee(sl_2) = 2
    kappa_dual = Fraction(3) * (k_dual + 2) / 4
    c = Fraction(3) * k / (k + 2)
    return {
        'name': f'sl2_{{{k}}}',
        'type': 'affine_sl2',
        'k': k,
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'L',
        'k_dual': k_dual,
        'kappa_dual': kappa_dual,
    }


def affine_general_shadow_data(
    name: str,
    dim_g: int,
    h_vee: int,
    k: Fraction,
) -> Dict[str, Any]:
    """General affine KM: kappa = dim(g)*(k+h^vee)/(2h^vee), alpha = 1, S4 = 0. Class L."""
    kappa = Fraction(dim_g) * (k + h_vee) / (2 * h_vee)
    alpha = Fraction(1)
    S4 = Fraction(0)
    k_dual = -k - 2 * h_vee
    kappa_dual = Fraction(dim_g) * (k_dual + h_vee) / (2 * h_vee)
    c = Fraction(dim_g) * k / (k + h_vee)
    return {
        'name': f'{name}_{{{k}}}',
        'type': 'affine_KM',
        'k': k,
        'c': c,
        'dim_g': dim_g,
        'h_vee': h_vee,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'L',
        'k_dual': k_dual,
        'kappa_dual': kappa_dual,
    }


def w3_wline_shadow_data(c: Fraction) -> Dict[str, Any]:
    """W_3 W-line: kappa = c/3, alpha = 0, S4 = 2560/(c(5c+22)^3). Class M."""
    kappa = c / 3
    alpha = Fraction(0)
    S4 = Fraction(2560) / (c * (5 * c + 22) ** 3)
    return {
        'name': f'W3_{{{c}}}_Wline',
        'type': 'W_3_Wline',
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'M',
    }


def betagamma_shadow_data(lam: Fraction) -> Dict[str, Any]:
    """Beta-gamma: c = 2(6lam^2-6lam+1), kappa = c/2. T-line data. Global class C."""
    c = 2 * (6 * lam ** 2 - 6 * lam + 1)
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    return {
        'name': f'bg_{{{lam}}}',
        'type': 'betagamma',
        'c': c,
        'lambda': lam,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'C_global',  # T-line: class M; global: class C
        'kappa_dual': -kappa,
    }


def lattice_voa_shadow_data(rank: int) -> Dict[str, Any]:
    """Lattice VOA V_Lambda of rank d: kappa = rank, alpha = 1, S4 = 0. Class L.

    For a rank-d even unimodular lattice (exists for d = 0 mod 8).
    Central charge c = d. kappa = d (not c/2!  AP48).
    """
    kappa = Fraction(rank)
    alpha = Fraction(1)
    S4 = Fraction(0)
    return {
        'name': f'V_Lambda_{{rank={rank}}}',
        'type': 'lattice_VOA',
        'rank': rank,
        'c': Fraction(rank),
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'class': 'L',
    }


# =============================================================================
# 8. Full conductor analysis for a family
# =============================================================================

@dataclass
class ConductorAnalysis:
    """Full arithmetic conductor analysis for a single algebra."""

    name: str
    shadow_class: str
    kappa: Fraction
    alpha: Fraction
    S4: Fraction
    tower: Dict[int, Fraction]
    max_R: int
    conductor_seq: Dict[int, int]  # R -> N_R
    prime_spec: Set[int]
    prime_by_arity: Dict[int, Set[int]]
    growth_rate: float
    stabilization_R: Optional[int]
    discriminant_relation: Dict[str, Any]

    def full_conductor(self) -> int:
        """N(A) = N_{max_R}."""
        return self.conductor_seq.get(self.max_R, 1)

    def log_conductor_sequence(self) -> Dict[int, float]:
        """log(N_R) for each R."""
        return {R: math.log(N) if N > 1 else 0.0
                for R, N in self.conductor_seq.items()}


def analyze_conductor(
    data: Dict[str, Any],
    max_R: int = 20,
) -> ConductorAnalysis:
    """Run the full conductor analysis on a family's shadow data."""
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']
    name = data.get('name', 'unknown')
    shadow_cls = data.get('class', '?')

    # For Heisenberg (class G): tower is trivial
    if shadow_cls == 'G':
        tower = {2: kappa}
        for r in range(3, max_R + 1):
            tower[r] = Fraction(0)
    else:
        tower = shadow_tower_exact(kappa, alpha, S4, max_r=max_R)

    cond_seq = conductor_sequence(tower, max_R=max_R)
    p_spec = prime_spectrum(tower, max_R=max_R)
    p_by_arity = prime_spectrum_by_arity(tower, max_R=max_R)
    gamma = conductor_growth_rate(cond_seq)
    stab = conductor_stabilizes_at(cond_seq)
    disc_rel = discriminant_conductor_relation(kappa, S4, tower, max_R=max_R)

    return ConductorAnalysis(
        name=name,
        shadow_class=shadow_cls,
        kappa=kappa,
        alpha=alpha,
        S4=S4,
        tower=tower,
        max_R=max_R,
        conductor_seq=cond_seq,
        prime_spec=p_spec,
        prime_by_arity=p_by_arity,
        growth_rate=gamma,
        stabilization_R=stab,
        discriminant_relation=disc_rel,
    )


# =============================================================================
# 9. Shadow ODE recurrence path (independent verification)
# =============================================================================

def shadow_tower_via_ode(
    kappa: Fraction,
    alpha: Fraction,
    S4: Fraction,
    max_r: int = 20,
) -> Dict[int, Fraction]:
    r"""Independent computation via the shadow metric ODE.

    The shadow metric Q_L(t) = (2kappa + 3alpha*t)^2 + 2*Delta*t^2
    where Delta = 8*kappa*S4.

    H(t) = t^2 * sqrt(Q_L(t)) and S_r = [t^r] G(t) where G(t) = sum S_r t^r.

    Since H(t) = sum r*S_r*t^r, we have:
        G(t) = integral_0^t H(u)/u^2 du ... no, that's wrong.
        H(t) = t * d/dt G(t) if G = sum S_r t^r, since t d/dt (S_r t^r) = r S_r t^r.
        So H(t) = t G'(t).

    Alternative: from H(t) = t^2 sqrt(Q_L(t)):
        H(t) = sum_{r>=2} r S_r t^r

    Squaring:
        H(t)^2 = t^4 Q_L(t)
        (sum_{r>=2} r S_r t^r)^2 = t^4 (q0 + q1 t + q2 t^2)

    This gives a system of equations for S_r.

    This function uses the SAME convolution recursion but implemented
    with a different code path for cross-verification.
    """
    if kappa == 0:
        raise ValueError("kappa = 0")

    Delta = 8 * kappa * S4

    # Q_L(t) = (2k + 3a*t)^2 + 2*Delta*t^2
    #        = 4k^2 + 12k*a*t + (9a^2 + 2*Delta)*t^2
    # Note: 9a^2 + 2*Delta = 9a^2 + 16k*S4 = q2 from the main recursion

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 2 * Delta

    # f(t) = sqrt(Q_L(t)) = sum b_n t^n
    # f^2 = Q_L => b_0^2 = q0, 2*b_0*b_1 = q1, 2*b_0*b_2 + b_1^2 = q2
    # For n >= 3: 2*b_0*b_n + sum_{j=1}^{n-1} b_j*b_{n-j} = 0

    b0 = 2 * kappa  # signed square root
    b = [b0]

    max_n = max_r - 2
    if max_n >= 1:
        b.append(q1 / (2 * b0))
    if max_n >= 2:
        b.append((q2 - b[1] ** 2) / (2 * b0))

    for n in range(3, max_n + 1):
        conv = sum(b[j] * b[n - j] for j in range(1, n))
        b.append(-conv / (2 * b0))

    result: Dict[int, Fraction] = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(b):
            result[r] = b[idx] / r

    return result


# =============================================================================
# 10. Langlands conductor comparison
# =============================================================================

def langlands_conductor_comparison(
    tower_A: Dict[int, Fraction],
    automorphic_level: int,
    max_R: int = 20,
) -> Dict[str, Any]:
    """Compare shadow conductor N(A) with automorphic conductor/level.

    For affine sl_2 at level k:
    - The automorphic form on SL_2(Z) has Hecke level related to k
    - The shadow conductor N(sl2_k) encodes denominator arithmetic

    This computes the ratio and common prime structure.
    """
    N = truncated_conductor(tower_A, max_R)
    g = math.gcd(N, automorphic_level)
    return {
        'shadow_conductor': N,
        'automorphic_level': automorphic_level,
        'gcd': g,
        'ratio_N_over_level': Fraction(N, automorphic_level) if automorphic_level > 0 else None,
        'common_primes': prime_factors(g),
        'shadow_only_primes': prime_factors(N) - prime_factors(automorphic_level),
        'level_only_primes': prime_factors(automorphic_level) - prime_factors(N),
    }


# =============================================================================
# 11. Full landscape conductor analysis
# =============================================================================

def standard_landscape_conductors(max_R: int = 20) -> Dict[str, ConductorAnalysis]:
    """Compute conductor analysis for all standard families."""
    results: Dict[str, ConductorAnalysis] = {}

    # Heisenberg at various levels
    for k_val in [Fraction(1), Fraction(2), Fraction(1, 2), Fraction(1, 3)]:
        data = heisenberg_shadow_data(k_val)
        results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Virasoro at standard central charges
    for c_val in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5),
                  Fraction(1), Fraction(2), Fraction(25), Fraction(26)]:
        data = virasoro_shadow_data(c_val)
        results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Affine sl_2 at integer and admissible levels
    for k_val in [Fraction(1), Fraction(2), Fraction(3), Fraction(5),
                  Fraction(10), Fraction(-1, 2), Fraction(-4, 3)]:
        data = affine_sl2_shadow_data(k_val)
        results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Affine sl_3 at k=1
    data = affine_general_shadow_data('sl3', dim_g=8, h_vee=3, k=Fraction(1))
    results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Affine G_2 at k=1
    data = affine_general_shadow_data('G2', dim_g=14, h_vee=4, k=Fraction(1))
    results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Affine E_8 at k=1
    data = affine_general_shadow_data('E8', dim_g=248, h_vee=30, k=Fraction(1))
    results[data['name']] = analyze_conductor(data, max_R=max_R)

    # W_3 W-line
    for c_val in [Fraction(2), Fraction(50)]:
        data = w3_wline_shadow_data(c_val)
        results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Beta-gamma
    data = betagamma_shadow_data(Fraction(1, 3))
    results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Lattice VOA rank 8 (E_8 root lattice)
    data = lattice_voa_shadow_data(8)
    results[data['name']] = analyze_conductor(data, max_R=max_R)

    # Lattice VOA rank 24 (Leech)
    data = lattice_voa_shadow_data(24)
    results[data['name']] = analyze_conductor(data, max_R=max_R)

    return results


# =============================================================================
# 12. Summary and reporting
# =============================================================================

def conductor_summary(analysis: ConductorAnalysis) -> str:
    """Human-readable summary of a conductor analysis."""
    lines = [
        f"Arithmetic Conductor Analysis: {analysis.name}",
        f"  Shadow class: {analysis.shadow_class}",
        f"  kappa = {analysis.kappa}, alpha = {analysis.alpha}, S4 = {analysis.S4}",
        f"  Full conductor N_{analysis.max_R} = {analysis.full_conductor()}",
        f"  Prime spectrum P = {sorted(analysis.prime_spec)}",
        f"  Growth rate gamma = {analysis.growth_rate:.6f}",
    ]
    if analysis.stabilization_R is not None:
        lines.append(f"  Conductor stabilizes at R = {analysis.stabilization_R}")
    else:
        lines.append(f"  Conductor does NOT stabilize by R = {analysis.max_R}")

    lines.append(f"  Conductor sequence (first 10):")
    for R in range(2, min(12, analysis.max_R + 1)):
        if R in analysis.conductor_seq:
            lines.append(f"    N_{R} = {analysis.conductor_seq[R]}")

    return "\n".join(lines)
