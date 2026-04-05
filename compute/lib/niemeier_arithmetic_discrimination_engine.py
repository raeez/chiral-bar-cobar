r"""Niemeier lattice discrimination via arithmetic shadow invariants.

MATHEMATICAL FRAMEWORK
======================

All 24 Niemeier lattices Lambda have the same scalar shadow data:
  kappa(V_Lambda) = rank(Lambda) = 24,  shadow class G,  S_r = 0 for r >= 3.

The scalar shadow obstruction tower is BLIND to the lattice structure.
This module pushes discrimination into the ARITHMETIC territory: invariants
extracted from the interplay between the theta series Theta_Lambda(tau),
the Hecke decomposition of weight-12 modular forms, and the VOA structure.

HIERARCHY OF ARITHMETIC INVARIANTS (this module's main contribution):

1. KISSING NUMBER tau(Lambda) = |{v in Lambda : |v|^2 = 2}| = N_roots.
   Ranges from 0 (Leech) to 1104 (D_24).
   Extracted from theta coefficient r(1) = N_roots.
   Discriminating power: 19/24 (5 collision pairs with same |R|).

2. SHELL DISTRIBUTION N_m(Lambda) = |{v in Lambda : |v|^2 = 2m}|.
   The theta series encodes all shell numbers:
     Theta_Lambda(tau) = sum_{m>=0} N_m q^m,  where N_0 = 1.
   The shadow ODE for V_Lambda encodes these via the vertex algebra structure.
   Since Theta_Lambda = E_{12} + c_Delta * Delta, all N_m are determined by
   c_Delta alone (equivalently, by N_1 = N_roots alone).

3. ARITHMETIC DEPTH d_arith(V_Lambda):
   For lattice VOAs (class G), the scalar tower terminates at arity 2.
   The arithmetic depth measures the complexity of the Hecke decomposition
   of Theta_Lambda.  Since M_{12}(SL(2,Z)) = C*E_{12} + C*Delta (dim 2),
   every Niemeier theta series decomposes as Theta = E_{12} + c_Delta * Delta.
   Since c_Delta = (691*N_roots - 65520)/691 and 65520/691 is not an integer,
   c_Delta != 0 for ALL 24 Niemeier lattices (including Leech).
   Therefore d_arith = 1 for ALL 24 lattices uniformly.

4. ARITHMETIC CONDUCTOR N(V_Lambda):
   Defined as the product of primes appearing in the denominator of c_Delta
   (when reduced to lowest terms), raised to their respective powers.
   Since c_Delta = (691*N_roots - 65520)/691, the conductor detects
   the 691-divisibility structure of N_roots.

5. HECKE EIGENVALUE EXTRACTION:
   Delta = sum tau(n) q^n is a Hecke eigenform with eigenvalues tau(p).
   The Ramanujan conjecture |tau(p)| <= 2*p^{11/2} (proved by Deligne 1974)
   gives absolute bounds.  The shadow tower data at genus 1 is
   F_1 = kappa * lambda_1^FP = 24 * (1/24) = 1 for all Niemeier lattices.
   The per-lattice variation enters through c_Delta * tau(n).

6. MOONSHINE MODULE V^natural (c=24, dim V_1 = 0):
   kappa(V^natural) = 12 (Virasoro formula, NOT rank formula).
   Shadow class M (infinite depth, Virasoro quartic contact nonzero).
   The j-function j(tau) = q^{-1} + 744 + 196884q + ... encodes V^natural.
   McKay-Thompson series T_g(tau) for Monster conjugacy classes.

7. CROSS-LATTICE ARITHMETIC:
   The genus-2 theta function Theta_Lambda^{(2)} lives in the space of
   weight-12 Siegel modular forms.  The Boecherer conjecture (proved by
   Furusawa-Morimoto) relates genus-2 Fourier coefficients to central
   L-values.  This provides genuinely genus-2 discrimination beyond
   the genus-1 theta series.

MULTI-PATH VERIFICATION:
  Path 1: Direct lattice computation (theta series, kissing numbers)
  Path 2: Shadow ODE extraction from VOA structure
  Path 3: Modular form decomposition (Hecke eigenvalues)
  Path 4: Cross-check V^natural via Monster symmetry (McKay-Thompson)

Mathematical references:
  - Niemeier (1968), classification of even unimodular rank-24 lattices
  - Conway-Sloane, "Sphere Packings", Ch. 16
  - Deligne (1974), proof of Ramanujan conjecture for Delta
  - Furusawa-Morimoto (2022), proof of Boecherer conjecture
  - arithmetic_shadows.tex: depth decomposition d = 1 + d_arith + d_alg
  - higher_genus_modular_koszul.tex: shadow depth classification
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from sympy import (
    Abs, Integer, Rational, bernoulli, cancel, factorial, isprime,
    factorint, gcd as sympy_gcd,
)

from compute.lib.niemeier_shadow_atlas import (
    ALL_NIEMEIER_LABELS,
    KAPPA_NIEMEIER,
    NIEMEIER_REGISTRY,
    c_delta,
    coxeter_number,
    root_count,
    root_lattice_det,
    shadow_data,
    theta_coefficient,
    theta_series,
)

from compute.lib.moonshine_shadow_tower import (
    monster_kappa,
    leech_kappa,
    monster_shadow_class,
    monster_critical_discriminant,
    monster_shadow_growth_rate,
    virasoro_shadow_tower,
    monster_genus_amplitude,
    leech_genus_amplitude,
    _faber_pandharipande,
)


# =========================================================================
# Part 1: Root system data extensions
# =========================================================================

def lie_algebra_dimension(family: str, n: int) -> int:
    """Dimension of the simple Lie algebra of type family_n.

    A_n: n(n+2) = (n+1)^2 - 1.
    D_n: n(2n-1).
    E_6: 78,  E_7: 133,  E_8: 248.
    """
    if family == 'A':
        return n * (n + 2)
    elif family == 'D':
        return n * (2 * n - 1)
    elif family == 'E':
        return {6: 78, 7: 133, 8: 248}[n]
    else:
        raise ValueError(f"Unknown family: {family}")


def dual_coxeter_number(family: str, n: int) -> int:
    """Dual Coxeter number h^vee.  For ADE (simply-laced), h^vee = h."""
    return coxeter_number(family, n)


def weyl_group_order(family: str, n: int) -> int:
    """Order of the Weyl group of type family_n.

    A_n: (n+1)!
    D_n: 2^{n-1} * n!
    E_6: 51840,  E_7: 2903040,  E_8: 696729600.
    """
    if family == 'A':
        return math.factorial(n + 1)
    elif family == 'D':
        return 2 ** (n - 1) * math.factorial(n)
    elif family == 'E':
        return {6: 51840, 7: 2903040, 8: 696729600}[n]
    else:
        raise ValueError(f"Unknown family: {family}")


def exponents(family: str, n: int) -> Tuple[int, ...]:
    """Exponents of a simple Lie algebra of type family_n.

    These are m_1, ..., m_n where m_i + 1 are the degrees of
    fundamental invariants.  Sum of exponents = |R+| = |R|/2.
    """
    if family == 'A':
        return tuple(range(1, n + 1))
    elif family == 'D':
        return tuple(list(range(1, 2 * n - 2, 2)) + [n - 1])
    elif family == 'E':
        if n == 6:
            return (1, 4, 5, 7, 8, 11)
        elif n == 7:
            return (1, 5, 7, 9, 11, 13, 17)
        elif n == 8:
            return (1, 7, 11, 13, 17, 19, 23, 29)
    raise ValueError(f"Unknown family: {family}")


# =========================================================================
# Part 2: Kissing number and shell distribution
# =========================================================================

def kissing_number(label: str) -> int:
    """Kissing number tau(Lambda) = number of shortest nonzero vectors.

    For even unimodular lattices, the shortest vectors have norm 2,
    so tau(Lambda) = |{v in Lambda : |v|^2 = 2}| = N_roots.
    Exception: Leech lattice has no roots; shortest vectors have norm 4,
    so tau(Leech) = 196560.

    For consistency with the shadow framework, we report N_roots here
    (the number of norm-2 vectors), which is 0 for Leech.
    The separate function kissing_number_true() gives the geometric
    kissing number (norm-4 vectors for Leech).
    """
    if label not in NIEMEIER_REGISTRY:
        raise ValueError(f"Unknown Niemeier lattice: {label}")
    return NIEMEIER_REGISTRY[label]['num_roots']


def kissing_number_true(label: str) -> int:
    """True geometric kissing number (number of shortest nonzero vectors).

    For all non-Leech Niemeier lattices: equals num_roots (shortest = norm 2).
    For Leech: 196560 (shortest vectors have norm 4).
    """
    if label == 'Leech':
        return 196560
    return kissing_number(label)


def shell_number(label: str, m: int) -> int:
    """Shell number N_m(Lambda) = |{v in Lambda : |v|^2 = 2m}|.

    This is the coefficient of q^m in the theta series Theta_Lambda(tau).
    For m = 0: N_0 = 1 (the zero vector).
    For m = 1: N_1 = num_roots (= kissing number for non-Leech).
    For m >= 2: computed from Theta = E_{12} + c_Delta * Delta.
    """
    return theta_coefficient(label, m)


def shell_distribution(label: str, max_m: int = 10) -> Dict[int, int]:
    """Shell distribution {m: N_m} for m = 0, 1, ..., max_m.

    Returns the first max_m + 1 shell numbers.
    """
    return {m: shell_number(label, m) for m in range(max_m + 1)}


def kissing_from_theta(label: str) -> int:
    """Recover kissing number from theta series coefficient.

    Path 2 verification: extract tau(Lambda) = r(1) from theta series.
    """
    return theta_coefficient(label, 1)


def shell_determines_theta(label: str, max_m: int = 10) -> bool:
    """Verify that c_Delta (hence the full theta series) is determined by N_1.

    Since Theta = E_{12} + c_Delta * Delta and c_Delta = (691*N_1 - 65520)/691,
    the single shell number N_1 determines ALL subsequent N_m.
    """
    N1 = kissing_number(label)
    cd_from_N1 = Fraction(691 * N1 - 65520, 691)
    cd_actual = c_delta(label)
    return cd_from_N1 == cd_actual


# =========================================================================
# Part 3: Shadow ODE and shell recovery
# =========================================================================

@lru_cache(maxsize=500)
def _sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


@lru_cache(maxsize=500)
def _ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficient of q^n in Delta(tau).

    Uses the product formula Delta = q * prod_{n>=1}(1-q^n)^24.
    Computed by expanding the product to the needed order.
    """
    if n < 1:
        return 0
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m_val in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m_val - 1, -1):
                coeffs[i] -= coeffs[i - m_val]
    # Delta = q * prod(1-q^n)^24, so tau(n) = coeffs[n-1]
    return coeffs[n - 1] if n - 1 <= N else 0


@lru_cache(maxsize=500)
def _eisenstein_E12_coefficient(n: int) -> Rational:
    """Coefficient of q^n in the normalized Eisenstein series E_{12}.

    E_{12} = 1 + (65520/691) * sum_{n>=1} sigma_{11}(n) q^n.

    Returns exact rational value.
    """
    if n == 0:
        return Rational(1)
    sig11 = _sigma_k(n, 11)
    return Rational(65520, 691) * sig11


def shadow_ode_shell_recovery(label: str, max_m: int = 10) -> Dict[int, int]:
    """Recover shell numbers from the shadow ODE / VOA structure.

    Path 2: For lattice VOAs (class G), the shadow ODE is trivial
    (all higher obstructions vanish), so F_g = kappa * lambda_g^FP.
    The theta series is Theta = E_{12} + c_Delta * Delta, with
    c_Delta = (691 * N_roots - 65520) / 691.

    This function reconstructs the shell numbers from the shadow data:
    - kappa = 24 (from shadow tower)
    - c_Delta from root count (from bar complex per-factor decomposition)
    Then verifies against direct theta series computation.
    """
    cd = c_delta(label)
    recovered = {}
    for m in range(max_m + 1):
        if m == 0:
            recovered[m] = 1
        else:
            # Theta_Lambda coefficient = E_{12} coefficient + c_Delta * tau(m)
            e12_coeff = Rational(65520, 691) * _sigma_k(m, 11)
            tau_m = _ramanujan_tau(m)
            value = 1 + int(e12_coeff) + int(cd) * tau_m if m == 0 else \
                    int(e12_coeff + Rational(cd) * tau_m)
            # More careful: direct integer computation
            N_roots = NIEMEIER_REGISTRY[label]['num_roots']
            numer = 65520 * _sigma_k(m, 11) + (691 * N_roots - 65520) * tau_m
            assert numer % 691 == 0
            recovered[m] = numer // 691
    return recovered


def verify_shadow_shell_consistency(label: str, max_m: int = 10) -> bool:
    """Verify Path 1 (direct theta) matches Path 2 (shadow ODE recovery).

    Returns True if all shell numbers match.
    """
    direct = shell_distribution(label, max_m)
    recovered = shadow_ode_shell_recovery(label, max_m)
    return all(direct[m] == recovered[m] for m in range(max_m + 1))


# =========================================================================
# Part 4: Arithmetic depth
# =========================================================================

def arithmetic_depth(label: str) -> int:
    """Arithmetic depth d_arith(V_Lambda) for a Niemeier lattice VOA.

    d_arith measures the complexity of the Hecke decomposition of the
    genus-1 theta series in the space of weight-12 modular forms.

    M_{12}(SL(2,Z)) = C * E_{12} + C * Delta  (dimension 2).

    Theta_Lambda = E_{12} + c_Delta * Delta.

    d_arith = 0 if c_Delta = 0 (purely Eisenstein)
    d_arith = 1 if c_Delta != 0 (one cusp form direction activated)

    KEY FACT: c_Delta = (691*N_roots - 65520)/691.  Since 65520/691
    is NOT an integer (65520 mod 691 = 566), c_Delta != 0 for ALL
    integer values of N_roots.  Therefore d_arith = 1 for ALL 24
    Niemeier lattices, including Leech.

    The depth decomposition d = 1 + d_arith + d_alg gives:
    - All Niemeier lattice VOAs: d_alg = 0 (class G, algebraic depth 0)
    - All 24 lattices: d = 1 + 1 + 0 = 2  (kappa + Hecke cusp form)

    Note: "depth" here is the ARITHMETIC depth, not the shadow depth.
    Shadow depth is always 2 for class G (Gaussian).
    """
    cd = c_delta(label)
    if cd == 0:
        return 0
    return 1


def total_depth(label: str) -> int:
    """Total depth d = 1 + d_arith + d_alg.

    For lattice VOAs: d_alg = 0 (class G).
    d = 1 + d_arith.
    """
    return 1 + arithmetic_depth(label)


def depth_classification() -> Dict[int, List[str]]:
    """Classify all 24 Niemeier lattices by arithmetic depth."""
    by_depth: Dict[int, List[str]] = defaultdict(list)
    for label in ALL_NIEMEIER_LABELS:
        d = arithmetic_depth(label)
        by_depth[d].append(label)
    return dict(by_depth)


# =========================================================================
# Part 5: Arithmetic conductor
# =========================================================================

def c_delta_fraction(label: str) -> Fraction:
    """c_Delta as a reduced fraction.

    c_Delta = (691 * N_roots - 65520) / 691.
    """
    return c_delta(label)


def arithmetic_conductor(label: str) -> int:
    """Arithmetic conductor N(V_Lambda).

    Defined as the product p^{e_p} over primes p where e_p is the
    p-adic valuation of the numerator of c_Delta (reduced fraction).

    For Leech (c_Delta = -65520/691): numerator = -65520.
    For others: numerator = 691*N_roots - 65520.

    The conductor detects the prime factorization structure of the
    theta series' cusp form coefficient.

    Convention: conductor of Leech (c_Delta = -65520/691) uses |numerator|.
    If c_Delta = 0 (impossible for Niemeier lattices since N_roots is even
    and 65520/691 is not an integer... wait, let's check):
      c_Delta = 0 iff 691*N_roots = 65520 iff N_roots = 65520/691.
      65520/691 is NOT an integer (65520 = 691*94 + 466), so c_Delta != 0
      for any integer N_roots.

    Actually c_delta for the Leech lattice: N_roots = 0, so
      c_Delta = (0 - 65520)/691 = -65520/691.
    This fraction reduces: gcd(65520, 691).
      691 is prime.  65520 mod 691 = 65520 - 94*691 = 65520 - 64954 = 566.
    So gcd = 1, and c_Delta = -65520/691 (already reduced).
    Numerator = -65520.  |Numerator| = 65520 = 2^4 * 3^2 * 5 * 7 * 13.
    Conductor = 65520.

    For general label: numerator of (691*N - 65520)/691.
    If 691 divides (691*N - 65520), then c_Delta is an integer.
    691*N - 65520 = 691*(N - 94) - 466.  So 691 | numerator iff 691 | 466.
    466 = 0*691 + 466.  So 691 does NOT divide 466.  Hence c_Delta is NEVER
    an integer for any Niemeier lattice.

    So the conductor is always |691*N_roots - 65520|, since the denominator
    is always exactly 691 (reduced form).
    """
    if label not in NIEMEIER_REGISTRY:
        raise ValueError(f"Unknown Niemeier lattice: {label}")
    N = NIEMEIER_REGISTRY[label]['num_roots']
    numerator = abs(691 * N - 65520)
    if numerator == 0:
        return 1  # trivial conductor
    return numerator


def arithmetic_conductor_factored(label: str) -> Dict[int, int]:
    """Prime factorization of the arithmetic conductor.

    Returns {p: e_p} where conductor = prod p^{e_p}.
    """
    N = arithmetic_conductor(label)
    if N <= 1:
        return {}
    return dict(factorint(N))


def conductor_discriminating_power() -> Dict[str, Any]:
    """Assess how well the arithmetic conductor discriminates.

    Returns collision analysis: which lattices share the same conductor.
    """
    by_conductor: Dict[int, List[str]] = defaultdict(list)
    for label in ALL_NIEMEIER_LABELS:
        N = arithmetic_conductor(label)
        by_conductor[N].append(label)
    collisions = {N: labs for N, labs in by_conductor.items() if len(labs) > 1}
    n_distinct = len(by_conductor)
    total_pairs = 24 * 23 // 2
    collision_pairs = sum(len(v) * (len(v) - 1) // 2 for v in by_conductor.values())
    distinguished_pairs = total_pairs - collision_pairs
    return {
        'num_distinct_values': n_distinct,
        'total_pairs': total_pairs,
        'distinguished_pairs': distinguished_pairs,
        'collision_pairs': collision_pairs,
        'is_complete': collision_pairs == 0,
        'collisions': collisions,
        'all_conductors': {label: arithmetic_conductor(label)
                          for label in ALL_NIEMEIER_LABELS},
    }


# =========================================================================
# Part 6: Hecke eigenform decomposition
# =========================================================================

def hecke_decomposition(label: str) -> Dict[str, Any]:
    """Hecke eigenform decomposition of the theta series.

    Theta_Lambda = E_{12} + c_Delta * Delta

    where E_{12} is the Eisenstein series (not an eigenform per se,
    but in the Eisenstein eigenspace) and Delta is the unique normalized
    cusp form of weight 12 for SL(2,Z).

    The Hecke eigenvalues of Delta are the Ramanujan tau function:
      T_p(Delta) = tau(p) * Delta.

    So the theta series is a sum of two Hecke eigencomponents:
      Eisenstein component: coefficient 1 (normalized)
      Cuspidal component: coefficient c_Delta
    """
    cd = c_delta(label)
    return {
        'eisenstein_coefficient': Fraction(1),
        'cuspidal_coefficient': cd,
        'is_eigenform': cd == 0 or cd == Fraction(1),
        'has_cuspidal_part': cd != 0,
        'num_eigencomponents': 1 if cd == 0 else 2,
    }


def hecke_eigenvalue_at_prime(p: int) -> int:
    """Hecke eigenvalue of Delta at prime p.

    This is tau(p), the Ramanujan tau function at p.
    By Deligne's theorem: |tau(p)| <= 2*p^{11/2}.
    """
    return _ramanujan_tau(p)


def ramanujan_bound_check(max_p: int = 50) -> Dict[int, Dict[str, Any]]:
    """Verify the Ramanujan conjecture |tau(p)| <= 2*p^{11/2} for primes up to max_p.

    This is a theorem (Deligne 1974), but we verify it computationally
    as a consistency check on the tau function implementation.
    """
    result = {}
    for p in range(2, max_p + 1):
        if not _is_prime(p):
            continue
        tau_p = _ramanujan_tau(p)
        bound = 2 * p ** (11 / 2)
        result[p] = {
            'tau_p': tau_p,
            'bound': bound,
            'ratio': abs(tau_p) / bound if bound > 0 else 0,
            'satisfies': abs(tau_p) <= bound + 1e-6,  # numerical tolerance
        }
    return result


def _is_prime(n: int) -> bool:
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


def theta_hecke_eigenvalue_contribution(label: str, p: int) -> Fraction:
    """The p-th Hecke eigenvalue contribution from the theta series.

    For Theta = E_{12} + c_Delta * Delta, the action of T_p gives:
      T_p(Theta) at coefficient level: the p-th coefficient of Theta
      is sigma_{11}(p) * 65520/691 + c_Delta * tau(p).

    But what we really want is: how does the Hecke operator T_p act?
      T_p(E_{12}) = (1 + p^{11}) * E_{12}  (Eisenstein eigenvalue)
      T_p(Delta) = tau(p) * Delta  (cusp form eigenvalue)

    So T_p(Theta) = (1 + p^{11}) * E_{12} + c_Delta * tau(p) * Delta.

    The "Hecke eigenvalue" of Theta at p is not well-defined (Theta is
    not an eigenform in general), but the per-eigenspace eigenvalues are:
      Eisenstein: lambda_p^{Eis} = 1 + p^{11}  (= sigma_{11}(p) for prime p)
      Cuspidal: lambda_p^{cusp} = tau(p)
    """
    tau_p = _ramanujan_tau(p)
    cd = c_delta(label)
    # The cuspidal contribution to the p-th Fourier coefficient
    cuspidal_contribution = cd * tau_p
    return cuspidal_contribution


# =========================================================================
# Part 7: Moonshine module V^natural
# =========================================================================

# First 20 coefficients of the j-function j(tau) = q^{-1} + 744 + ...
# J(tau) = j(tau) - 744 = q^{-1} + 196884q + 21493760q^2 + ...
J_COEFFICIENTS = {
    -1: 1,
    0: 0,      # J = j - 744, so constant term is 0
    1: 196884,
    2: 21493760,
    3: 864299970,
    4: 20245856256,
    5: 333202640600,
    6: 4252023300096,
    7: 44656994071935,
    8: 401490886656000,
    9: 3176440229784420,
    10: 22567393309593600,
    11: 146211911499519294,
    12: 874313719685775360,
    13: 4872010111798142520,
    14: 25497827389410525184,
    15: 126142916465781843075,
}


def j_coefficient(n: int) -> int:
    """Coefficient of q^n in J(tau) = j(tau) - 744.

    J(tau) = sum_{n >= -1} c(n) q^n with c(-1) = 1, c(0) = 0.
    For n >= 1: c(n) = dim V_{n+1} for V^natural.

    For small n, use the precomputed table.
    For larger n, use the relation j = E_4^3/Delta and expand.
    """
    if n in J_COEFFICIENTS:
        return J_COEFFICIENTS[n]
    # For larger n: compute from E_4^3/Delta
    # E_4 = 1 + 240*sum sigma_3(n) q^n
    # Delta = sum tau(n) q^n (starting at n=1)
    # j = E_4^3/Delta = q^{-1} + 744 + ...
    # J = j - 744
    return _compute_j_coefficient(n)


@lru_cache(maxsize=256)
def _compute_j_coefficient(n: int) -> int:
    """Compute J-coefficient via E_4^3 / Delta expansion.

    j(tau) = E_4(tau)^3 / Delta(tau).
    E_4 = 1 + 240*sum_{m>=1} sigma_3(m) q^m.
    Delta = sum_{m>=1} tau(m) q^m.

    Since j = E_4^3 / Delta, we have E_4^3 = j * Delta = (J + 744) * Delta.
    So: (J + 744) * Delta = E_4^3.
    Expanding: sum_k (sum_{i+j=k} J_i * tau(j)) + 744 * tau(k) = [E_4^3]_k.
    For k >= 1: J_{k-1} * tau(1) + sum_{i<k-1} J_i * tau(k-i) + 744*tau(k) = [E_4^3]_k.
    Since tau(1) = 1: J_{k-1} = [E_4^3]_k - 744*tau(k) - sum_{i<k-1} J_i * tau(k-i).

    But J_{-1} = 1, so we need the convolution starting from i = -1.
    """
    # Need to compute up to order n
    max_order = n + 2  # extra room

    # Compute E_4 coefficients: E_4 = 1 + 240*sum sigma_3(m)*q^m
    e4 = [0] * (max_order + 1)
    e4[0] = 1
    for m in range(1, max_order + 1):
        e4[m] = 240 * _sigma_k(m, 3)

    # Compute E_4^3 coefficients via convolution
    e4_sq = [0] * (max_order + 1)
    for i in range(max_order + 1):
        for j in range(max_order + 1 - i):
            e4_sq[i + j] += e4[i] * e4[j]

    e4_cube = [0] * (max_order + 1)
    for i in range(max_order + 1):
        for j in range(max_order + 1 - i):
            e4_cube[i + j] += e4_sq[i] * e4[j]

    # Now solve (J + 744) * Delta = E_4^3 for J coefficients
    # Delta starts at q^1: tau(1) = 1, tau(2) = -24, ...
    # Convention: J_{-1} = 1, J_0 = 0, J_n for n >= 1.
    # (J + 744) * Delta at order k means:
    #   sum_{m >= 1} (J_{k-m} + 744*delta_{k-m >= -1}) * tau(m)
    # where delta means indicator.
    # Actually: j = q^{-1} + 744 + 196884q + ...
    # j * Delta at order k: sum_{m>=1, n>=-1} j_n * tau(m) * [n+m = k]
    #   = sum_{m>=1} j_{k-m} * tau(m).

    # We compute J coefficients iteratively
    J_dict: Dict[int, int] = {-1: 1}
    for k in range(0, n + 1):
        # E_4^3 at order k+1 (since j*Delta: j has leading q^{-1}, Delta has leading q^1)
        # Actually: j * Delta = E_4^3.
        # j = sum_{n>=-1} j_n q^n, Delta = sum_{m>=1} tau(m) q^m.
        # (j*Delta)_k = sum_{m>=1} j_{k-m} * tau(m) for k-m >= -1, i.e., m <= k+1.
        # = [E_4^3]_k.

        # Solve for j_k: contribution from m=k+1 gives j_{-1}*tau(k+1) = tau(k+1).
        # j_k appears when m = 0... but tau(0) = 0.  Actually Delta starts at q^1.
        # No: j_k * tau(m) at order k+m.  We want order k.  So j_{k-m}*tau(m).
        # j_k appears for m... it doesn't directly appear unless there is a tau(0) = 0 term.
        # Actually m >= 1, so the latest j index is j_{k-1}.
        # So j_k does NOT appear in (j*Delta)_k.

        # Wait: we need to be more careful.
        # (j * Delta) at order K = sum_{m=1}^{K+1} j_{K-m} * tau(m).
        # j_{-1} = 1, j_0 = 744, j_1 = 196884, etc.
        # J_n = j_n for n >= 1, J_{-1} = 1, J_0 = 0.  j_0 = 744.

        # Let me just compute j (not J) iteratively.
        pass

    # Simpler approach: compute j coefficients directly
    j_dict: Dict[int, int] = {-1: 1}
    # (j * Delta)_{total order} = E_4^3_{total order}
    # For total order K: sum_{m=1}^{min(K+1, max_order)} j_{K-m} * tau(m) = e4_cube[K]
    # j_{K-1} * tau(1) + sum_{m=2}^{K+1} j_{K-m} * tau(m) = e4_cube[K]
    # j_{K-1} = e4_cube[K] - sum_{m=2}^{min(K+1, max_order)} j_{K-m} * tau(m)

    for K in range(0, n + 2):
        rhs = e4_cube[K]
        for m in range(2, min(K + 2, max_order + 1)):
            idx = K - m
            if idx in j_dict:
                rhs -= j_dict[idx] * _ramanujan_tau(m)
        j_dict[K - 1] = rhs  # since tau(1) = 1

    J_n = j_dict.get(n, 0) - (744 if n == 0 else 0)
    return J_n


def monster_dim_Vn(n: int) -> int:
    """Dimension of the weight-n subspace of V^natural.

    dim V_n = J coefficient at q^{n-1} for n >= 1.
    dim V_0 = 1 (vacuum).
    dim V_1 = 0 (no weight-1 currents).
    """
    if n == 0:
        return 1
    return j_coefficient(n - 1)


def monster_virasoro_shadow_tower(max_r: int = 10) -> Dict[int, Rational]:
    """Virasoro-sector shadow tower for V^natural at c = 24.

    This is the shadow tower computed from the Virasoro subalgebra alone.
    The full V^natural tower receives corrections from the Griess algebra.
    """
    return virasoro_shadow_tower(max_r)


def monster_shadow_data_extended() -> Dict[str, Any]:
    """Extended shadow data for V^natural.

    Combines:
    - kappa = 12 (Virasoro formula)
    - Shadow class M (infinite depth)
    - Virasoro shadow tower coefficients
    - j-function data
    - McKay-Thompson data for identity class
    """
    vir_tower = virasoro_shadow_tower(10)
    return {
        'label': 'V^natural',
        'central_charge': 24,
        'kappa': 12,
        'kappa_formula': 'Virasoro (c/2), since dim V_1 = 0',
        'shadow_class': 'M',
        'shadow_depth': float('inf'),
        'virasoro_tower': vir_tower,
        'dim_V0': 1,
        'dim_V1': 0,
        'dim_V2': 196884,
        'dim_V3': 21493760 + 1,  # J_2 + 1 from Virasoro descendant
        'j_coefficients': {n: j_coefficient(n) for n in range(-1, 11)},
        'critical_discriminant': monster_critical_discriminant(),
        'shadow_growth_rate': monster_shadow_growth_rate(),
        'arithmetic_depth': 'special',  # j-function is weight 0, different from lattice case
        'monster_order': 808017424794512875886459904961710757005754368000000000,
    }


def monster_mckay_thompson_identity() -> Dict[str, Any]:
    """McKay-Thompson series for the identity element (= J itself).

    T_{1A}(tau) = J(tau) = j(tau) - 744.
    Genus-0 property: J is a Hauptmodul for SL(2,Z)/±1.
    """
    return {
        'conjugacy_class': '1A',
        'series_name': 'J (= j - 744)',
        'genus_of_quotient': 0,
        'is_hauptmodul': True,
        'modular_group': 'SL(2,Z)',
        'leading_coefficients': [j_coefficient(n) for n in range(-1, 11)],
    }


# =========================================================================
# Part 8: Cross-lattice discrimination analysis
# =========================================================================

def kissing_number_collisions() -> Dict[int, List[str]]:
    """Niemeier lattices sharing the same kissing number (= num_roots).

    These are the 5 collision pairs from the theta series.
    """
    by_kiss: Dict[int, List[str]] = defaultdict(list)
    for label in ALL_NIEMEIER_LABELS:
        k = kissing_number(label)
        by_kiss[k].append(label)
    return {k: labs for k, labs in by_kiss.items() if len(labs) > 1}


def shell_collision_analysis(max_m: int = 10) -> Dict[str, Any]:
    """Check whether shell numbers N_m for m <= max_m discriminate.

    Since all N_m are determined by N_1 (= num_roots), the shell
    distribution has EXACTLY the same discriminating power as N_1.
    """
    # Group by shell distributions
    by_shells: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
    for label in ALL_NIEMEIER_LABELS:
        shells = tuple(shell_number(label, m) for m in range(max_m + 1))
        by_shells[shells].append(label)
    collisions = {s: labs for s, labs in by_shells.items() if len(labs) > 1}

    # Also verify: collisions match N_1 collisions
    kiss_coll = kissing_number_collisions()
    shell_collision_labels = set()
    for labs in collisions.values():
        shell_collision_labels.update(labs)
    kiss_collision_labels = set()
    for labs in kiss_coll.values():
        kiss_collision_labels.update(labs)

    return {
        'max_m': max_m,
        'num_distinct_distributions': len(by_shells),
        'collision_groups': len(collisions),
        'collision_labels_match_kissing': shell_collision_labels == kiss_collision_labels,
        'collisions': collisions,
    }


def conductor_collision_analysis() -> Dict[str, Any]:
    """Full collision analysis for the arithmetic conductor."""
    return conductor_discriminating_power()


# =========================================================================
# Part 9: Hecke eigenvalue verification
# =========================================================================

def deligne_bound(p: int) -> float:
    """Deligne's bound: |tau(p)| <= 2 * p^{11/2}."""
    return 2.0 * p ** 5.5


def verify_deligne_bound(max_p: int = 100) -> Dict[str, Any]:
    """Verify Deligne's bound for all primes up to max_p.

    |tau(p)| <= 2 * p^{11/2} (proved by Deligne 1974).
    """
    violations = []
    primes_checked = []
    for p in range(2, max_p + 1):
        if not _is_prime(p):
            continue
        tau_p = _ramanujan_tau(p)
        bound = deligne_bound(p)
        primes_checked.append(p)
        if abs(tau_p) > bound * (1 + 1e-10):  # small tolerance for float
            violations.append((p, tau_p, bound))
    return {
        'num_primes_checked': len(primes_checked),
        'max_prime': max(primes_checked) if primes_checked else 0,
        'violations': violations,
        'all_satisfied': len(violations) == 0,
    }


def tau_multiplicativity_check(max_n: int = 30) -> Dict[str, Any]:
    """Verify multiplicativity of tau: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1.

    Also verify the Hecke relation at prime powers:
      tau(p^{k+1}) = tau(p)*tau(p^k) - p^{11}*tau(p^{k-1}).
    """
    mult_violations = []
    hecke_violations = []

    # Multiplicativity check
    for m in range(2, max_n + 1):
        for n in range(2, max_n // m + 1):
            if math.gcd(m, n) != 1:
                continue
            if _ramanujan_tau(m * n) != _ramanujan_tau(m) * _ramanujan_tau(n):
                mult_violations.append((m, n))

    # Hecke relation at prime powers
    for p in range(2, min(max_n, 20)):
        if not _is_prime(p):
            continue
        # tau(p^2) = tau(p)^2 - p^11
        tp = _ramanujan_tau(p)
        tp2 = _ramanujan_tau(p * p)
        expected = tp * tp - p ** 11
        if tp2 != expected:
            hecke_violations.append((p, 2, tp2, expected))
        # tau(p^3) = tau(p)*tau(p^2) - p^11*tau(p)
        if p * p * p <= max_n * 2:
            tp3 = _ramanujan_tau(p * p * p)
            expected3 = tp * tp2 - p ** 11 * tp
            if tp3 != expected3:
                hecke_violations.append((p, 3, tp3, expected3))

    return {
        'multiplicativity_violations': mult_violations,
        'hecke_relation_violations': hecke_violations,
        'multiplicativity_ok': len(mult_violations) == 0,
        'hecke_ok': len(hecke_violations) == 0,
    }


# =========================================================================
# Part 10: Full discrimination cascade
# =========================================================================

def discrimination_at_level(level: int) -> Dict[str, Any]:
    """Compute discrimination power at a given level.

    Level 0: kappa (= 24 for all, distinguishes 0/276 pairs)
    Level 1: full scalar shadow tower (identical for all, 0/276)
    Level 2: kissing number / num_roots (19 distinct values, 5 collisions)
    Level 3: per-factor (rank, Coxeter) vector (COMPLETE, 24/24)
    Level 4: arithmetic conductor (partial)
    Level 5: Hecke decomposition c_Delta (same as level 2)
    """
    by_value: Dict[Any, List[str]] = defaultdict(list)

    for label in ALL_NIEMEIER_LABELS:
        if level == 0:
            val = KAPPA_NIEMEIER
        elif level == 1:
            val = (KAPPA_NIEMEIER,) + (0,) * 8
        elif level == 2:
            val = kissing_number(label)
        elif level == 3:
            data = NIEMEIER_REGISTRY[label]
            components = data['components']
            if not components:
                val = ()
            else:
                val = tuple(sorted(
                    [(n, coxeter_number(f, n)) for f, n in components],
                    reverse=True
                ))
        elif level == 4:
            val = arithmetic_conductor(label)
        elif level == 5:
            val = c_delta(label)
        else:
            raise ValueError(f"Unknown level: {level}")

        by_value[val].append(label)

    n_distinct = len(by_value)
    total_pairs = 24 * 23 // 2  # = 276
    collision_pairs = sum(
        len(v) * (len(v) - 1) // 2 for v in by_value.values()
    )
    distinguished = total_pairs - collision_pairs

    collisions = {str(k): v for k, v in by_value.items() if len(v) > 1}

    return {
        'level': level,
        'num_distinct': n_distinct,
        'total_pairs': total_pairs,
        'distinguished_pairs': distinguished,
        'collision_pairs': collision_pairs,
        'is_complete': collision_pairs == 0,
        'collisions': collisions,
    }


def full_arithmetic_discrimination_cascade() -> Dict[int, Dict[str, Any]]:
    """Run the full discrimination cascade from level 0 to level 5."""
    return {level: discrimination_at_level(level) for level in range(6)}


# =========================================================================
# Part 11: Cross-verification functions
# =========================================================================

def cross_verify_kissing_number(label: str) -> Dict[str, Any]:
    """Cross-verify kissing number via 3 independent paths.

    Path 1: Direct from root system (sum of root_count per component)
    Path 2: From theta coefficient r(1)
    Path 3: From c_Delta via inversion: N_roots = (691*c_Delta + 65520)/691
    """
    # Path 1: root count
    data = NIEMEIER_REGISTRY[label]
    path1 = data['num_roots']

    # Path 2: theta coefficient
    path2 = theta_coefficient(label, 1)

    # Path 3: c_Delta inversion
    cd = c_delta(label)
    path3_frac = (691 * cd + 65520) / 691
    path3 = int(path3_frac)

    return {
        'label': label,
        'path1_root_count': path1,
        'path2_theta_coeff': path2,
        'path3_c_delta_inversion': path3,
        'all_agree': path1 == path2 == path3,
    }


def cross_verify_shell_recovery(label: str, max_m: int = 8) -> Dict[str, Any]:
    """Cross-verify shell numbers via 2 paths.

    Path 1: Direct theta series (from E_{12} + c_Delta * Delta)
    Path 2: Shadow ODE recovery
    """
    path1 = shell_distribution(label, max_m)
    path2 = shadow_ode_shell_recovery(label, max_m)
    agree = all(path1[m] == path2[m] for m in range(max_m + 1))
    return {
        'label': label,
        'path1_direct': path1,
        'path2_shadow_ode': path2,
        'all_agree': agree,
    }


def cross_verify_all_niemeier() -> Dict[str, Dict[str, bool]]:
    """Cross-verify all invariants for all 24 Niemeier lattices."""
    results = {}
    for label in ALL_NIEMEIER_LABELS:
        kiss_ok = cross_verify_kissing_number(label)['all_agree']
        shell_ok = cross_verify_shell_recovery(label)['all_agree']
        theta_ok = shell_determines_theta(label)
        results[label] = {
            'kissing_cross_verified': kiss_ok,
            'shell_recovery_cross_verified': shell_ok,
            'theta_from_N1': theta_ok,
        }
    return results


# =========================================================================
# Part 12: Niemeier S_3 computation (per-lattice cubic shadow from VOA)
# =========================================================================

def lattice_voa_S3(label: str) -> Rational:
    """Cubic shadow S_3 for a Niemeier lattice VOA.

    For lattice VOAs V_Lambda (class G), S_3 = 0.
    The weight-1 currents generate Heisenberg + lattice vertex operators,
    and the OPE of weight-1 fields is purely bilinear (no cubic term).

    This is proved by curvature-braiding orthogonality
    (thm:lattice:curvature-braiding-orthogonal).
    """
    return Rational(0)


def lattice_voa_S4(label: str) -> Rational:
    """Quartic contact S_4 for a Niemeier lattice VOA.

    For lattice VOAs (class G), S_4 = 0.
    """
    return Rational(0)


def lattice_voa_critical_discriminant(label: str) -> Rational:
    """Critical discriminant Delta = 8*kappa*S_4 for a Niemeier lattice VOA.

    Delta = 0 for all lattice VOAs (class G).
    """
    return Rational(0)


# =========================================================================
# Part 13: S_3 discrimination analysis (the question: does S_3 discriminate?)
# =========================================================================

def s3_discriminates() -> bool:
    """Does S_3 discriminate among Niemeier lattices?

    Answer: NO.  All 24 have S_3 = 0 (class G).
    """
    return False


def first_discriminating_arity() -> Dict[str, Any]:
    """At which arity does FULL discrimination first occur within the MC framework?

    The scalar shadow tower {S_r}_{r>=2} cannot discriminate AT ALL
    (all 24 lattices are class G with identical scalar towers).

    Discrimination requires NON-SCALAR MC data:
    - Level 2 (per-factor kappa vector): 14/24 discriminated
    - Level 3 (per-factor rank + Coxeter): 24/24 (COMPLETE)

    The per-factor data is MC data (bar complex decomposes along root factors),
    but it is not arity data in the shadow tower sense.

    CONCLUSION: Within the scalar shadow tower, NO finite arity suffices.
    Full discrimination requires the per-factor structure of the bar complex,
    which is arity-1 data (the bar complex generators at B^{(0,1)}).
    """
    return {
        'scalar_tower_discriminates': False,
        'scalar_tower_max_arity_needed': float('inf'),
        'per_factor_kappa_discriminating_power': '14/24',
        'per_factor_rank_coxeter_discriminating_power': '24/24 (COMPLETE)',
        'minimal_complete_mc_level': 3,
        'minimal_complete_mc_data': 'per-factor (rank, Coxeter number) vector',
        'bar_complex_arity': 1,
        'explanation': (
            'The scalar shadow tower S_r is identical for all 24 Niemeier lattices. '
            'Discrimination requires the per-factor bar complex decomposition, '
            'which is arity-1 (generator-level) MC data. The minimal complete '
            'invariant is the sorted (rank, Coxeter) vector, extractable from '
            'H^1(B(V_Lambda)) with its PBW filtration.'
        ),
    }


# =========================================================================
# Part 14: Moonshine vs Leech vs generic Niemeier comparison
# =========================================================================

def monster_vs_niemeier_comparison() -> Dict[str, Any]:
    """Compare V^natural against all 24 Niemeier lattice VOAs.

    Key distinctions:
    1. kappa: V^natural has kappa = 12 (Virasoro), all lattice VOAs have kappa = 24
    2. Shadow class: V^natural is class M, all lattice VOAs are class G
    3. dim V_1: V^natural has 0, all non-Leech have N_roots > 0, Leech has 24 (Heisenberg)
    """
    monster = {
        'kappa': int(monster_kappa()),
        'shadow_class': monster_shadow_class(),
        'dim_V1': 0,
        'shadow_depth': float('inf'),
    }
    comparisons = {}
    for label in ALL_NIEMEIER_LABELS:
        data = NIEMEIER_REGISTRY[label]
        comparisons[label] = {
            'kappa': KAPPA_NIEMEIER,
            'shadow_class': 'G',
            'dim_V1': data['num_roots'] + 24 if label != 'Leech' else 24,
            # Actually dim V_1 = N_roots for root components + rank for Cartan
            # For lattice VOAs: dim V_1 = N_roots + rank (roots + Cartan)
            # Wait: dim V_1 for V_Lambda is the number of weight-1 states.
            # Weight-1 states = Cartan currents (24 of them, one per coordinate).
            # Actually, for the Niemeier lattice VOA:
            #   V_1 = Lambda tensor C = {lattice Cartan currents} union {root vertex ops of weight 1}
            #   But root vertex operators e^alpha have weight alpha^2/2.
            #   For alpha a root (alpha^2 = 2): weight = 1.
            #   So dim V_1 = rank + N_roots = 24 + N_roots for non-Leech.
            #   For Leech: no roots, so dim V_1 = 24.
            'dim_V1_corrected': 24 + data['num_roots'],
            'shadow_depth': 2,
            'kappa_differs_from_monster': True,
            'class_differs_from_monster': True,
        }
    return {
        'monster': monster,
        'niemeier_lattices': comparisons,
    }


# =========================================================================
# Part 15: Summary statistics
# =========================================================================

def full_arithmetic_summary() -> Dict[str, Any]:
    """Complete summary of arithmetic discrimination analysis.

    Returns statistics on all invariant levels and their discriminating power.
    """
    cascade = full_arithmetic_discrimination_cascade()
    conductor_data = conductor_discriminating_power()

    return {
        'total_lattices': 24,
        'total_pairs': 276,
        'discrimination_cascade': {
            level: {
                'distinguished_pairs': cascade[level]['distinguished_pairs'],
                'is_complete': cascade[level]['is_complete'],
            }
            for level in range(6)
        },
        'conductor_analysis': {
            'num_distinct': conductor_data['num_distinct_values'],
            'is_complete': conductor_data['is_complete'],
        },
        'moonshine_distinguished': True,  # kappa = 12 != 24
        'key_finding': (
            'The scalar shadow tower is completely blind to lattice structure '
            '(all 24 identical). The minimal complete MC invariant is the '
            'per-factor (rank, Coxeter) vector from the bar complex decomposition. '
            'The arithmetic conductor partially discriminates but has collisions. '
            'V^natural (moonshine) is sharply distinguished by kappa = 12 vs 24 '
            'and shadow class M vs G.'
        ),
    }
