r"""Prime-locality for lattice VOAs: Euler products, Hecke multiplicativity,
and the arithmetic structure of the sewing lift.

MATHEMATICAL FRAMEWORK
======================

For a lattice VOA V_Lambda with even lattice Lambda of rank r:

1. THETA FUNCTION: Theta_Lambda(tau) = sum_{n>=0} r_Lambda(n) q^n
   where r_Lambda(n) counts lattice vectors of half-norm n.

2. HECKE DECOMPOSITION: Theta_Lambda is a modular form of weight r/2.
   It decomposes into a sum of Hecke eigenforms:
     Theta_Lambda = c_0 * E_k + sum_j c_j * f_j
   where E_k is the Eisenstein series and f_j are cusp forms.

3. EULER PRODUCTS: Each Hecke eigenform has a Dirichlet series with
   Euler product:
     L(s, f) = prod_p (1 - a_p p^{-s} + p^{k-1-2s})^{-1}
   The theta function's Dirichlet series is a SUM of such Euler products,
   one per eigenform in the decomposition.

4. MULTIPLICATIVITY: The raw representation numbers r_Lambda(n) are
   multiplicative ONLY when Theta_Lambda is a single Hecke eigenform
   (up to a constant factor). This happens when:
   - dim M_k(SL_2(Z)) = 1, i.e. dim S_k = 0 (pure Eisenstein), OR
   - dim S_k = 1 and the Eisenstein coefficient matches to kill it.

5. SHADOW TOWER: All lattice VOAs are class G (Gaussian), with shadow
   depth 2 and S_r = 0 for r >= 3. The shadow obstruction tower terminates because
   the L_infinity algebra Def_inf^mod(V_Lambda) is formal (curvature-
   braiding orthogonality).

SPECIFIC LATTICES
=================

E_8 (rank 8, weight 4):
  Theta_{E_8} = E_4.  dim M_4 = 1, dim S_4 = 0.
  r_{E_8}(n) = 240 * sigma_3(n), sigma_3 is multiplicative.
  L(s, E_4) = zeta(s) * zeta(s-3).
  Hecke eigenvalues: a(p) = sigma_3(p) = 1 + p^3.
  PRIME-LOCALITY: PERFECT. Single Euler product.

D_4 (rank 4, weight 2):
  Theta_{D_4} has weight 2 for Gamma_0(2). dim M_2(SL_2(Z)) = 0
  (no weight-2 forms for the full group), but Theta_{D_4} lives
  on a congruence subgroup.
  r_{D_4}(n) = 24 * sigma_1^{odd}(n), sigma_1^{odd} is multiplicative.
  L(s, Theta_{D_4}) = 24 * zeta(s) * (1 - 2^{1-s}) * zeta(s-1).
  Hecke eigenvalues (primes p != 2): a(p) = sigma_1^{odd}(p) = 1 + p.
  At p = 2: a(2^a) = 1 for all a (level-2 phenomenon).
  PRIME-LOCALITY: PERFECT. Single Euler product (with level structure).

Leech (rank 24, weight 12):
  Theta_Leech = E_{12} - (65520/691) * Delta.
  dim M_12 = 2: one Eisenstein, one cusp form.
  r_Leech(n) = (65520/691) * (sigma_11(n) - tau(n)).
  The coefficients are NOT multiplicative: r_Leech is a LINEAR
  COMBINATION of two multiplicative sequences.
  L(s, Theta_Leech) = (65520/691) * [zeta(s)*zeta(s-11) - L(s, Delta)].
  This is a DIFFERENCE of Euler products, NOT a single Euler product.
  PRIME-LOCALITY: DECOMPOSED. Two Euler products (Eisenstein + cusp).

SEWING LIFT
===========

The sewing lift S_{V_Lambda}(u) encodes the modular sewing data:
  S(u) = sum_{n>=1} r_Lambda(n) * n^{-u}
This is the Dirichlet series of the theta coefficients.

For lattice VOAs:
  - E_8: S(u) = 240 * zeta(u) * zeta(u-3)  [single Euler product]
  - D_4: S(u) = 24 * zeta(u) * (1-2^{1-u}) * zeta(u-1)  [single EP]
  - Leech: S(u) = (65520/691) * [zeta(u)*zeta(u-11) - L(u, Delta)]
           [difference of two Euler products]

WHY PRIME-LOCALITY WORKS FOR LATTICE VOAs
==========================================

The reason: Theta_Lambda is ALWAYS a modular form, hence always
decomposes into finitely many Hecke eigenforms, each of which has
an Euler product. The shadow obstruction tower terminates (class G) because the
L_infinity structure is formal, so there are no higher obstructions
that could break the Hecke decomposition.

WHY IT FAILS FOR NON-LATTICE VOAs
==================================

For W-algebras (Virasoro, W_N, etc.):
  1. The partition function is NOT a theta function of a lattice.
  2. The q-expansion coefficients (dimensions of weight spaces) do not
     arise from a representation number problem.
  3. There is no Hecke theory: the Dirichlet series sum dim(V_n) n^{-s}
     has NO Euler product in general.
  4. The shadow obstruction tower does NOT terminate (class M): the L_infinity
     structure has genuine higher operations, generating an infinite
     sequence of obstruction classes.
  5. The sewing lift is controlled by the full shadow obstruction tower, not just
     by kappa.

References:
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - arithmetic_shadows.tex: thm:shadow-spectral-correspondence
  - higher_genus_modular_koszul.tex: shadow depth classification
  - concordance.tex: sec:concordance-spectral-continuation
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Any, Dict, List, Optional, Tuple


# =========================================================================
# Arithmetic functions
# =========================================================================

def sigma_k(n: int, k: int) -> int:
    r"""Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def sigma_1_odd(n: int) -> int:
    r"""Sum of odd divisors: sigma_1^{odd}(n) = sum_{d|n, d odd} d.

    This is the building block of the D_4 theta function:
    r_{D_4}(n) = 24 * sigma_1^{odd}(n).

    Key property: sigma_1^{odd} is MULTIPLICATIVE.
    For n = 2^a * m with m odd: sigma_1^{odd}(n) = sigma_1(m).
    """
    if n <= 0:
        return 0
    return sum(d for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)


def prime_factorization(n: int) -> Dict[int, int]:
    """Return prime factorization of n as {prime: exponent}."""
    if n <= 0:
        raise ValueError(f"Expected positive integer, got {n}")
    factors: Dict[int, int] = {}
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors


def is_prime(n: int) -> bool:
    """Check if n is prime."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def primes_up_to(n: int) -> List[int]:
    """List of primes up to n."""
    return [p for p in range(2, n + 1) if is_prime(p)]


# =========================================================================
# Ramanujan tau function
# =========================================================================

def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficients of Delta = eta^{24}.

    Delta(tau) = q * prod_{m>=1} (1-q^m)^{24} = sum_{n>=1} tau(n) q^n.

    tau is multiplicative: tau(mn) = tau(m)*tau(n) when gcd(m,n) = 1.
    Hecke recursion: tau(p^{r+1}) = tau(p)*tau(p^r) - p^{11}*tau(p^{r-1}).
    """
    if n < 1:
        return 0
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    return coeffs[n - 1] if n - 1 <= N else 0


# =========================================================================
# Representation numbers for specific lattices
# =========================================================================

def r_e8(n: int) -> int:
    r"""Number of vectors of half-norm n in E_8: r_{E_8}(n) = 240 * sigma_3(n).

    Since Theta_{E_8} = E_4, and E_4 = 1 + 240*sum sigma_3(n) q^n.
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return 240 * sigma_k(n, 3)


def r_d4(n: int) -> int:
    r"""Number of vectors of half-norm n in D_4: r_{D_4}(n) = 24 * sigma_1^{odd}(n).

    The D_4 theta function satisfies r(n) = 24 * sigma_1^{odd}(n)
    (Jacobi four-square theorem variant for D_4).
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return 24 * sigma_1_odd(n)


def r_leech(n: int) -> int:
    r"""Number of vectors of half-norm n in the Leech lattice.

    Theta_Leech = E_{12} - (65520/691)*Delta.
    r_Leech(n) = (65520/691)*(sigma_11(n) - tau(n)) for n >= 1.
    r_Leech(0) = 1, r_Leech(1) = 0 (no roots).
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    s11 = sigma_k(n, 11)
    tau_n = ramanujan_tau(n)
    result = Fraction(65520, 691) * (s11 - tau_n)
    assert result.denominator == 1, f"Non-integer Leech coefficient at n={n}: {result}"
    return int(result)


# =========================================================================
# Multiplicativity verification
# =========================================================================

def check_multiplicativity(
    coeffs_func,
    max_n: int = 30,
) -> Tuple[bool, List[Tuple[int, int, int, int]]]:
    r"""Test if a coefficient function a(n) is multiplicative.

    Multiplicative: a(mn) = a(m)*a(n) whenever gcd(m,n) = 1.
    Requires a(1) = 1 for true multiplicativity.

    Returns (is_mult, failures) where each failure is (m, n, a(mn), a(m)*a(n)).
    """
    failures = []
    a1 = coeffs_func(1)
    if a1 != 1:
        # Raw representation numbers have a(1) != 1 in general.
        # We can still check the normalized version.
        pass

    for m in range(2, max_n + 1):
        for n in range(2, max_n + 1):
            if m * n > max_n:
                break
            if gcd(m, n) != 1:
                continue
            amn = coeffs_func(m * n)
            am_an = coeffs_func(m) * coeffs_func(n)
            if amn != am_an:
                failures.append((m, n, amn, am_an))
    return (len(failures) == 0, failures)


def check_normalized_multiplicativity(
    coeffs_func,
    max_n: int = 30,
) -> Tuple[bool, List[Tuple[int, int, float, float]]]:
    r"""Test if normalized coefficients a(n)/a(1) are multiplicative.

    For lattice theta functions, the raw r(n) typically has r(1) != 1
    (e.g. r_{E_8}(1) = 240, r_{D_4}(1) = 24). The normalized sequence
    a(n) = r(n)/r(1) is the Hecke eigenvalue sequence, which should
    be multiplicative when the theta function is a single eigenform.
    """
    a1 = coeffs_func(1)
    if a1 == 0:
        return (False, [(-1, -1, 0, 0)])  # Cannot normalize if a(1) = 0

    failures = []
    for m in range(2, max_n + 1):
        for n in range(2, max_n + 1):
            if m * n > max_n:
                break
            if gcd(m, n) != 1:
                continue
            # Use Fraction for exact comparison
            amn = Fraction(coeffs_func(m * n), a1)
            am = Fraction(coeffs_func(m), a1)
            an = Fraction(coeffs_func(n), a1)
            am_an = am * an
            if amn != am_an:
                failures.append((m, n, float(amn), float(am_an)))
    return (len(failures) == 0, failures)


# =========================================================================
# Hecke recursion verification
# =========================================================================

def verify_hecke_recursion(
    coeffs_func,
    weight: int,
    p: int,
    max_power: int = 6,
    level_prime: Optional[int] = None,
) -> Tuple[bool, List[Tuple[int, int, int]]]:
    r"""Verify the Hecke recursion at prime p for a weight-k eigenform.

    For a normalized Hecke eigenform of weight k:
      a(p^{r+1}) = a(p)*a(p^r) - p^{k-1}*a(p^{r-1})

    If level_prime is set and p equals level_prime, the recursion
    changes: for p|N (the level), the Hecke operator U_p gives
    a(p^r) = a(p)^r (completely multiplicative at bad primes).

    Returns (all_pass, failures) where each failure is (r, lhs, rhs).
    """
    failures = []

    if level_prime is not None and p == level_prime:
        # At bad primes (p|N), check a(p^r) = a(p)^r
        ap = coeffs_func(p)
        for r in range(2, max_power + 1):
            lhs = coeffs_func(p ** r)
            rhs = ap ** r
            if lhs != rhs:
                failures.append((r, lhs, rhs))
        return (len(failures) == 0, failures)

    # Standard Hecke recursion for good primes
    for r in range(1, max_power):
        pr1 = p ** (r + 1)
        pr = p ** r
        pr_1 = p ** (r - 1)
        lhs = coeffs_func(pr1)
        rhs = coeffs_func(p) * coeffs_func(pr) - p ** (weight - 1) * coeffs_func(pr_1)
        if lhs != rhs:
            failures.append((r, lhs, rhs))
    return (len(failures) == 0, failures)


# =========================================================================
# Euler product computation
# =========================================================================

def euler_factor_e8(p: int, s: complex) -> complex:
    r"""Local Euler factor of L(s, E_4) at prime p.

    L(s, E_4) = prod_p 1/(1 - sigma_3(p)*p^{-s} + p^{3-2s})
              = prod_p 1/((1 - p^{-s})(1 - p^{3-s}))
              = zeta(s) * zeta(s-3).

    The factored form uses sigma_3(p) = 1 + p^3.
    """
    ps = p ** (-s)
    return 1.0 / ((1 - ps) * (1 - p ** 3 * ps))


def euler_factor_d4(p: int, s: complex) -> complex:
    r"""Local Euler factor of L(s, Theta_{D_4}) at prime p.

    For odd primes p:
      L_p(s) = 1/((1 - p^{-s})(1 - p^{1-s}))
    For p = 2 (level prime):
      L_2(s) = 1/(1 - 2^{-s})

    Full Euler product:
      L(s, Theta_{D_4}) = zeta(s) * (1 - 2^{1-s}) * zeta(s-1)
    """
    ps = p ** (-s)
    if p == 2:
        # At the level prime, the factor is 1/(1 - 2^{-s})
        return 1.0 / (1 - ps)
    else:
        return 1.0 / ((1 - ps) * (1 - p * ps))


def euler_factor_leech_eisenstein(p: int, s: complex) -> complex:
    r"""Eisenstein component of the Leech L-function at prime p.

    L_p(s, E_{12}) = 1/((1 - p^{-s})(1 - p^{11-s}))
    """
    ps = p ** (-s)
    return 1.0 / ((1 - ps) * (1 - p ** 11 * ps))


def euler_factor_leech_cusp(p: int, s: complex) -> complex:
    r"""Cusp component of the Leech L-function at prime p.

    L_p(s, Delta) = 1/(1 - tau(p)*p^{-s} + p^{11-2s})
    """
    ps = p ** (-s)
    tau_p = ramanujan_tau(p)
    return 1.0 / (1 - tau_p * ps + p ** 11 * ps * ps)


# =========================================================================
# Sewing lift (Dirichlet series)
# =========================================================================

def sewing_lift_e8(s: complex, num_terms: int = 200) -> complex:
    r"""Sewing lift for E_8 lattice VOA: S(s) = sum r_{E_8}(n) n^{-s}.

    This equals 240 * zeta(s) * zeta(s-3) by the Hecke decomposition.
    Computed by direct summation for verification.
    """
    return sum(r_e8(n) * n ** (-s) for n in range(1, num_terms + 1))


def sewing_lift_d4(s: complex, num_terms: int = 200) -> complex:
    r"""Sewing lift for D_4 lattice VOA: S(s) = sum r_{D_4}(n) n^{-s}.

    This equals 24 * zeta(s) * (1 - 2^{1-s}) * zeta(s-1).
    """
    return sum(r_d4(n) * n ** (-s) for n in range(1, num_terms + 1))


def sewing_lift_leech(s: complex, num_terms: int = 100) -> complex:
    r"""Sewing lift for Leech lattice VOA: S(s) = sum r_Leech(n) n^{-s}.

    This equals (65520/691) * [zeta(s)*zeta(s-11) - L(s, Delta)].
    The sewing lift is a DIFFERENCE of two Euler products.
    """
    return sum(r_leech(n) * n ** (-s) for n in range(1, num_terms + 1))


def sewing_lift_euler_product(
    lattice: str,
    s: complex,
    primes: Optional[List[int]] = None,
) -> complex:
    r"""Compute the sewing lift via Euler product.

    For E_8: uses 240 * prod_p euler_factor_e8(p, s).
    For D_4: uses 24 * prod_p euler_factor_d4(p, s).
    For Leech: NOT a single Euler product; returns the Eisenstein
    component only (with a flag).

    The 'primes' parameter controls which primes to include in the
    finite Euler product approximation.
    """
    if primes is None:
        primes = primes_up_to(50)

    if lattice == 'E8':
        result = 240.0
        for p in primes:
            result *= euler_factor_e8(p, s)
        return result
    elif lattice == 'D4':
        result = 24.0
        for p in primes:
            result *= euler_factor_d4(p, s)
        return result
    elif lattice == 'Leech':
        # Leech is NOT a single Euler product.
        # Return the Eisenstein component: (65520/691) * prod_p L_p(s, E_12)
        c = 65520.0 / 691.0
        eis_prod = 1.0
        cusp_prod = 1.0
        for p in primes:
            eis_prod *= euler_factor_leech_eisenstein(p, s)
            cusp_prod *= euler_factor_leech_cusp(p, s)
        return c * (eis_prod - cusp_prod)
    else:
        raise ValueError(f"Unknown lattice: {lattice}")


# =========================================================================
# Shadow obstruction tower verification
# =========================================================================

def shadow_tower_data(lattice: str) -> Dict[str, Any]:
    r"""Shadow obstruction tower data for a lattice VOA.

    ALL lattice VOAs are class G (Gaussian):
      - Shadow depth = 2
      - S_r = 0 for all r >= 3
      - kappa = rank
      - Q_L = (2*kappa)^2 (perfect square, constant)
      - Delta = 0 (critical discriminant vanishes)

    The termination is a consequence of the L_infinity formality of
    the modular deformation complex: the curvature-braiding orthogonality
    theorem (thm:lattice:curvature-braiding-orthogonal) implies that all
    transferred higher brackets are coboundaries.
    """
    lattice_info = {
        'E8': {'rank': 8, 'det': 1, 'unimodular': True, 'roots': 240},
        'D4': {'rank': 4, 'det': 4, 'unimodular': False, 'roots': 24},
        'Leech': {'rank': 24, 'det': 1, 'unimodular': True, 'roots': 0},
        'Z': {'rank': 1, 'det': 1, 'unimodular': True, 'roots': 2},
        'A2': {'rank': 2, 'det': 3, 'unimodular': False, 'roots': 6},
    }
    if lattice not in lattice_info:
        raise ValueError(f"Unknown lattice: {lattice}")

    info = lattice_info[lattice]
    kappa = info['rank']

    return {
        'lattice': lattice,
        'rank': info['rank'],
        'kappa': kappa,
        'shadow_class': 'G',
        'shadow_depth': 2,
        'S_3': 0,
        'S_4': 0,
        'S_5': 0,
        'alpha': 0,
        'Delta': 0,
        'Q_L': 4 * kappa ** 2,
        'is_perfect_square': True,
        'all_higher_vanish': True,
        'unimodular': info['unimodular'],
        'det': info['det'],
        'roots': info['roots'],
    }


# =========================================================================
# Prime-locality diagnostic
# =========================================================================

def prime_locality_diagnostic(lattice: str) -> Dict[str, Any]:
    r"""Comprehensive prime-locality analysis for a lattice VOA.

    Reports:
      - Whether the theta function is a single Hecke eigenform
      - Whether the raw/normalized coefficients are multiplicative
      - The Hecke decomposition (Eisenstein + cusp parts)
      - The form of the Euler product (or its absence)
      - Shadow class and depth
      - Why prime-locality works/fails
    """
    data = shadow_tower_data(lattice)

    if lattice == 'E8':
        # Single eigenform (dim S_4 = 0)
        is_single_eigenform = True
        weight = 4
        hecke_decomp = {'eisenstein': ('E_4', 1), 'cusp': []}
        euler_product_type = 'single'
        euler_formula = 'L(s) = 240 * zeta(s) * zeta(s-3)'
        raw_mult = check_multiplicativity(r_e8, 20)
        norm_mult = check_normalized_multiplicativity(r_e8, 20)
        eigenvalues_at_primes = {
            p: sigma_k(p, 3) for p in [2, 3, 5, 7, 11, 13]
        }

    elif lattice == 'D4':
        is_single_eigenform = True  # On Gamma_0(2)
        weight = 2
        hecke_decomp = {'eisenstein': ('E_2^*', 1), 'cusp': []}
        euler_product_type = 'single_with_level'
        euler_formula = 'L(s) = 24 * zeta(s) * (1-2^{1-s}) * zeta(s-1)'
        raw_mult = check_multiplicativity(r_d4, 20)
        norm_mult = check_normalized_multiplicativity(r_d4, 20)
        eigenvalues_at_primes = {
            p: sigma_1_odd(p) for p in [2, 3, 5, 7, 11, 13]
        }

    elif lattice == 'Leech':
        is_single_eigenform = False  # Two eigenforms
        weight = 12
        hecke_decomp = {
            'eisenstein': ('E_12', Fraction(1)),
            'cusp': [('Delta', Fraction(-65520, 691))],
        }
        euler_product_type = 'decomposed'
        euler_formula = ('L(s) = (65520/691) * '
                         '[zeta(s)*zeta(s-11) - L(s, Delta)]')
        raw_mult = check_multiplicativity(r_leech, 15)
        norm_mult = (False, [])  # r_Leech(1) = 0, cannot normalize
        eigenvalues_at_primes = {
            p: {'sigma_11': sigma_k(p, 11), 'tau': ramanujan_tau(p)}
            for p in [2, 3, 5, 7, 11, 13]
        }

    else:
        raise ValueError(f"Unknown lattice for diagnostic: {lattice}")

    return {
        **data,
        'weight': weight,
        'is_single_eigenform': is_single_eigenform,
        'hecke_decomposition': hecke_decomp,
        'euler_product_type': euler_product_type,
        'euler_formula': euler_formula,
        'raw_multiplicative': raw_mult[0],
        'raw_failures': raw_mult[1][:5],  # first 5 failures
        'normalized_multiplicative': norm_mult[0],
        'normalized_failures': norm_mult[1][:5],
        'eigenvalues_at_primes': eigenvalues_at_primes,
    }


# =========================================================================
# Cross-lattice comparison
# =========================================================================

def prime_locality_comparison_table() -> List[Dict[str, Any]]:
    r"""Comparison table of prime-locality across lattice VOAs.

    Shows how Hecke structure, multiplicativity, and shadow depth
    interact to produce (or prevent) Euler products.
    """
    results = []
    for lattice in ['E8', 'D4', 'Leech']:
        diag = prime_locality_diagnostic(lattice)
        results.append({
            'lattice': lattice,
            'rank': diag['rank'],
            'weight': diag['weight'],
            'shadow_class': diag['shadow_class'],
            'shadow_depth': diag['shadow_depth'],
            'single_eigenform': diag['is_single_eigenform'],
            'euler_type': diag['euler_product_type'],
            'raw_mult': diag['raw_multiplicative'],
            'norm_mult': diag['normalized_multiplicative'],
        })
    return results


# =========================================================================
# Why prime-locality fails for non-lattice
# =========================================================================

def non_lattice_obstruction_analysis() -> Dict[str, str]:
    r"""Analysis of why prime-locality fails for non-lattice VOAs.

    For each obstruction, explains what goes wrong and connects it
    to the shadow obstruction tower structure.
    """
    return {
        'obstruction_1_no_theta': (
            'Non-lattice VOAs (Virasoro, W_N, etc.) do not have a theta '
            'function. Their partition functions are not modular forms of '
            'the type Theta_Lambda = sum r(n) q^n arising from a lattice '
            'representation number problem.'
        ),
        'obstruction_2_no_hecke': (
            'Without a lattice structure, there is no Hecke theory: the '
            'Dirichlet series sum dim(V_n) n^{-s} has no reason to have '
            'an Euler product. The coefficients dim(V_n) count dimensions '
            'of weight spaces, not lattice vectors, and are NOT '
            'multiplicative in general.'
        ),
        'obstruction_3_infinite_shadow': (
            'Non-lattice VOAs of class M (Virasoro, W_N) have infinite '
            'shadow depth: S_r != 0 for all r. Each shadow arity generates '
            'a new obstruction class in the cyclic deformation complex. '
            'In the lattice case, all S_r = 0 for r >= 3 because the '
            'L_infinity structure is formal (curvature-braiding '
            'orthogonality). In the W-algebra case, the L_infinity '
            'structure has genuine higher operations.'
        ),
        'obstruction_4_non_formality': (
            'The shadow obstruction tower termination for lattices (class G, depth 2) '
            'is equivalent to L_infinity formality. For class M algebras, '
            'the discriminant Delta = 8*kappa*S_4 != 0, so the shadow '
            'metric Q_L is irreducible and the tower cannot terminate. '
            'This non-formality is the homotopy obstruction that prevents '
            'an Euler product.'
        ),
        'lattice_escape': (
            'Lattice VOAs escape all four obstructions: (1) they have a '
            'theta function by construction, (2) Hecke theory applies via '
            'modular forms, (3) the shadow obstruction tower terminates (class G), '
            '(4) the L_infinity structure is formal. These four conditions '
            'are EQUIVALENT for lattice VOAs but independent in general.'
        ),
    }
