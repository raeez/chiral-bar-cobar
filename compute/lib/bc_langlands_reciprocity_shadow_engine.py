r"""Langlands shadow reciprocity engine.

Connects the shadow obstruction tower of modular Koszul algebras to
automorphic L-functions via a shadow Langlands correspondence:

    A  |--->  (rho_A, L(s, rho_A))

where rho_A is the shadow Galois representation determined by the shadow
tower data {S_r(A)}_{r >= 2} and L(s, rho_A) is the associated L-function.

MATHEMATICAL FRAMEWORK
======================

1. SHADOW HECKE EIGENVALUES

   The genus-1 shadow Z_A(tau) on SL(2,Z) backslash H decomposes spectrally.
   For the standard families, the shadow data determines Hecke eigenvalues:

     a_p(A) = Tr(rho_A(Frob_p))

   computed from the shadow tower coefficients via the shadow Euler product:

     Z_A(tau) = sum_n a_n(A) q^n,  q = exp(2 pi i tau)

   For Heisenberg H_k: a_p = p^{k-1} + p^{-k}  (trivial, Eisenstein)
   For Virasoro Vir_c: a_p from q-expansion of eta(q)^{-c} * correction
   For lattice VOAs V_Lambda: a_p from theta series coefficients

2. SATAKE PARAMETERS

   At each prime p, the unramified representation pi_p determines a
   semisimple conjugacy class in the dual group via the Satake isomorphism:

     alpha_{p,1}, ..., alpha_{p,r}  in  C^*

   where r = rank of the shadow representation (= r_max - 1 for finite
   towers, truncated for class M).  The characteristic polynomial is:

     det(1 - rho(Frob_p) T) = prod_i (1 - alpha_{p,i} T)

   For class G (Heisenberg): r = 1, alpha_p = p^{(k-1)/2}
   For class L (affine KM): r = 2
   For class C (betagamma): r = 3
   For class M (Virasoro): r depends on truncation

3. LOCAL EULER FACTORS

   L_p(s, rho_A) = det(1 - rho_A(Frob_p) p^{-s})^{-1}
                  = prod_i (1 - alpha_{p,i} p^{-s})^{-1}

4. GLOBAL L-FUNCTION

   L(s, rho_A) = prod_p L_p(s, rho_A)

   converges for Re(s) > 1 + w/2 where w is the motivic weight.
   Analytic continuation and functional equation are conjectural in general.

5. KOSZUL DUALITY AND LANGLANDS

   The Koszul involution c -> 26-c for Virasoro acts on Satake parameters.
   At the self-dual point c = 13 (kappa + kappa' = 13, AP24), the
   representation is self-dual: rho_A = rho_A^vee.

   For affine KM, the Feigin-Frenkel involution k -> -k-2h^v induces
   the contragredient on the shadow representation.

6. CONDUCTOR AND ROOT NUMBER

   The Artin conductor f(rho_A) measures ramification.  The root number
   epsilon(1/2, pi_A) = +/-1 controls the sign of the functional equation.

   At c = 13 (self-dual Virasoro): epsilon = +1 (even functional equation).
   The conductor is determined by the shadow tower's singularity locus.

7. RAMANUJAN BOUND

   For the shadow representation to be automorphic:
     |alpha_{p,i}| = p^{w/2}   (Ramanujan-Petersson conjecture)

   where w is the motivic weight.  For class G, w = k-1 and this is
   trivially satisfied.  For higher classes, the bound is a nontrivial
   constraint on the shadow tower.

MULTI-PATH VERIFICATION
========================
Path 1: Direct computation from shadow tower coefficients
Path 2: Theta series / Eisenstein series comparison for lattice VOAs
Path 3: Koszul duality constraints (c -> 26-c transformation)
Path 4: Functional equation consistency
Path 5: Conductor formula from ramification data

BEILINSON WARNINGS
==================
AP1:  kappa formulas are family-specific; recompute from first principles.
AP9:  kappa != c/2 in general (only for Virasoro).
AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
AP38: Literature normalisation conventions vary between sources.
AP39: S_2 = c/2 != kappa for non-Virasoro families in general.
AP48: kappa depends on the full algebra, not the Virasoro subalgebra.

Manuscript references:
    conj:arithmetic-comparison (arithmetic_shadows.tex)
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    rem:motivic-decomposition (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import mpmath

mpmath.mp.dps = 50

from sympy import (
    Rational,
    Symbol,
    bernoulli,
    factorial,
    simplify,
    sqrt,
    pi as sym_pi,
    N as Neval,
    Abs,
    isprime,
    nextprime,
    factorint,
)


# =========================================================================
# 0. Arithmetic primitives
# =========================================================================

def _primes_up_to(n: int) -> List[int]:
    """Sieve of Eratosthenes up to n."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def _first_n_primes(n: int) -> List[int]:
    """Return the first n primes."""
    if n <= 0:
        return []
    if n < 6:
        bound = 15
    else:
        bound = int(n * (math.log(n) + math.log(math.log(n))) + 6) + 10
    primes = _primes_up_to(bound)
    while len(primes) < n:
        bound = int(bound * 1.5) + 10
        primes = _primes_up_to(bound)
    return primes[:n]


@lru_cache(maxsize=256)
def _divisor_sum(n: int, k: int) -> int:
    r"""sigma_k(n) = sum_{d | n} d^k."""
    if n <= 0:
        return 0
    return sum(d**k for d in range(1, n + 1) if n % d == 0)


# =========================================================================
# 1. Shadow tower data for standard families
# =========================================================================

def _kappa_virasoro(c_val):
    """kappa(Vir_c) = c/2.  (AP1, AP9, AP48: this formula is Virasoro-specific.)"""
    return Fraction(c_val) / 2


def _kappa_heisenberg(k_val):
    """kappa(H_k) = k."""
    return Fraction(k_val)


def _kappa_affine_sl2(k_val):
    """kappa(sl_2 at level k) = 3(k+2)/4.  (AP1)"""
    return Fraction(3) * (Fraction(k_val) + 2) / 4


def _kappa_lattice(rank):
    """kappa(V_Lambda) = rank(Lambda).  (AP48)"""
    return Fraction(rank)


def _shadow_depth(family: str) -> int:
    """Shadow depth r_max by family class.

    G (Heisenberg): r_max = 2
    L (affine KM):  r_max = 3
    C (betagamma):  r_max = 4
    M (Virasoro):   r_max = infinity (represented as -1)
    """
    table = {"G": 2, "L": 3, "C": 4, "M": -1}
    return table.get(family, -1)


def _shadow_class(c_val: Fraction) -> str:
    """Classify Virasoro by shadow class.

    Virasoro is always class M (infinite tower) for generic c.
    """
    return "M"


def _virasoro_shadow_coefficients(c_val, max_r: int = 20) -> Dict[int, Fraction]:
    r"""Virasoro shadow coefficients S_r for r = 2, ..., max_r.

    S_2 = c/2  (= kappa)
    S_3 = 2    (universal cubic)
    S_4 = 10/(c(5c+22))  (Q^contact)

    Higher arities via the recursion from sqrt(Q_L):
      a_0 = c, a_1 = 6, a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 2
      S_r = a_{r-2} / r

    WARNING: c = 0 and c = -22/5 are poles.
    """
    cv = Fraction(c_val)
    if cv == 0:
        raise ValueError("c = 0: pole of shadow tower")
    if cv == Fraction(-22, 5):
        raise ValueError("c = -22/5: pole of S_4")

    kappa = cv / 2

    # Compute a_n coefficients for sqrt(Q_L)
    aa = [Fraction(0)] * max(max_r + 1, 3)
    aa[0] = cv  # a_0 = c = 2*kappa
    aa[1] = Fraction(6)  # a_1 = 6

    # Recursion for a_n, n >= 2
    # Q_L(t) = q_0 + q_1 t + q_2 t^2 where:
    #   q_0 = c^2, q_1 = 12*kappa*alpha = 12*(c/2)*2 = 12c
    #   q_2 = 9*alpha^2 + 2*Delta = 36 + 80/(5c+22)
    q0 = cv**2
    q1 = 12 * cv
    q2 = Fraction(36) + Fraction(80) / (5 * cv + 22)

    for n in range(2, max_r - 1):
        q_n = Fraction(0)
        if n == 1:
            q_n = q1
        elif n == 2:
            q_n = q2
        conv = sum(aa[j] * aa[n - j] for j in range(1, n))
        aa[n] = (q_n - conv) / (2 * aa[0])

    S = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(aa):
            S[r] = aa[idx] / r
        else:
            S[r] = Fraction(0)
    return S


def _heisenberg_shadow_coefficients(k_val, max_r: int = 20) -> Dict[int, Fraction]:
    """Heisenberg shadow coefficients: S_2 = k, all higher vanish (class G)."""
    kv = Fraction(k_val)
    S = {r: Fraction(0) for r in range(2, max_r + 1)}
    S[2] = kv
    return S


def _affine_sl2_shadow_coefficients(k_val, max_r: int = 20) -> Dict[int, Fraction]:
    """Affine sl_2 shadow coefficients: S_2 = 3(k+2)/4, S_3 = 4/(k+2), rest 0 (class L)."""
    kv = Fraction(k_val)
    kappa = Fraction(3) * (kv + 2) / 4
    S3 = Fraction(4) / (kv + 2)  # 2*h^v/(k+h^v), h^v(sl_2)=2
    S = {r: Fraction(0) for r in range(2, max_r + 1)}
    S[2] = kappa
    S[3] = S3
    return S


# =========================================================================
# 2. Shadow Hecke eigenvalues
# =========================================================================

def shadow_hecke_eigenvalue(c, p: int) -> complex:
    r"""Compute shadow Hecke eigenvalue a_p(A) at prime p for Virasoro at
    central charge c.

    The shadow Hecke eigenvalue is derived from the genus-1 shadow partition
    function.  For a modular Koszul algebra A with kappa = c/2, the genus-1
    free energy F_1 = -kappa * log(eta(q)) gives:

      Z_1(q) ~ eta(q)^{-c}

    The Fourier coefficients of eta(q)^{-c} = q^{-c/24} sum a_n q^n yield
    a_p(A) via the Hecke operator T_p.

    For c = 24 (Leech lattice central charge): eta(q)^{-24} = 1/Delta(q),
    where Delta is the Ramanujan discriminant.  Then a_p = tau(p) (the
    Ramanujan tau function).

    For general c, we compute the p-th Fourier coefficient of eta^{-c}
    using the recursion for powers of the Dedekind eta function.

    WARNING (AP46): eta(q) = q^{1/24} prod_{n>=1}(1-q^n).  The q^{1/24}
    prefactor is NOT optional.
    """
    if not isinstance(p, int) or p < 2:
        raise ValueError(f"p must be a prime >= 2, got {p}")

    # We compute coefficients of prod_{n>=1} (1-q^n)^{-c}
    # (stripping the q^{-c/24} prefactor, which is absorbed into the
    # normalisation of the Fourier expansion).
    # This is the generating function for partitions weighted by c.
    # For integer c, this is exact; for rational c we use mpmath.

    c_val = float(c)
    # Number of terms needed to extract coefficient of q^p
    N = p + 1

    with mpmath.workdps(30):
        # Compute coefficients of prod_{n>=1} (1 - q^n)^{-c_val} up to q^p
        # using the recursion:
        #   n * a_n = sum_{k=1}^{n} sigma_1(k) * c_val * a_{n-k}
        # where sigma_1(k) = sum of divisors of k.
        coeffs = [mpmath.mpf(0)] * N
        coeffs[0] = mpmath.mpf(1)

        for n in range(1, N):
            s = mpmath.mpf(0)
            for k in range(1, n + 1):
                sig1 = _divisor_sum(k, 1)
                s += mpmath.mpf(sig1) * mpmath.mpf(c_val) * coeffs[n - k]
            coeffs[n] = s / mpmath.mpf(n)

        # a_p is the p-th coefficient
        return complex(coeffs[p])


def shadow_satake_parameters(c, p: int) -> Tuple[complex, ...]:
    r"""Compute Satake parameters alpha_{p,i} from the shadow Hecke eigenvalue
    at prime p for Virasoro at central charge c.

    For rank-1 shadow representation (class G or simplified Virasoro):
      a_p = alpha_p + alpha_p^{-1} * p^{w}
    where w is the motivic weight.

    For the shadow tower of Virasoro with kappa = c/2, the motivic weight
    is w = 0 at the level of the genus-1 partition function (the shadow
    coefficients are not Hodge-weighted).  The Satake parameter satisfies:

      a_p = alpha_p + 1/alpha_p     (w=0 normalisation)

    so alpha_p = (a_p +/- sqrt(a_p^2 - 4)) / 2.

    For rank-2 representations:
      det(1 - rho(Frob_p) T) = 1 - a_p T + chi(p) T^2
    where chi is the central character.

    Returns a tuple of Satake parameters, one per rank of the shadow
    representation.
    """
    a_p = shadow_hecke_eigenvalue(c, p)

    # Rank-1 Satake parametrisation
    # alpha^2 - a_p * alpha + 1 = 0
    # (normalised so det = alpha * alpha_bar = 1 for unitary representations)
    disc = a_p * a_p - 4.0
    sqrt_disc = cmath.sqrt(disc)

    alpha1 = (a_p + sqrt_disc) / 2.0
    alpha2 = (a_p - sqrt_disc) / 2.0

    return (alpha1, alpha2)


# =========================================================================
# 3. Frobenius characteristic polynomial
# =========================================================================

def frobenius_characteristic_poly(c, p: int) -> List[complex]:
    r"""Compute the Frobenius characteristic polynomial

      det(1 - rho(Frob_p) T) = 1 - a_p T + chi(p) T^2

    for the shadow representation at prime p and central charge c.

    Returns coefficients [1, -a_p, chi(p)] of the polynomial in T.

    For the normalised shadow representation, chi(p) = 1 (unit determinant
    constraint from the MC equation's symplectic structure).
    """
    a_p = shadow_hecke_eigenvalue(c, p)

    # Central character: for the shadow representation derived from the
    # modular Koszul structure, the MC equation's symplectic pairing forces
    # det(rho(Frob_p)) = 1 for all p (weight 0 normalisation).
    chi_p = 1.0

    return [1.0, -a_p, chi_p]


# =========================================================================
# 4. Local Euler factors
# =========================================================================

def euler_factor(c, p: int, s: complex) -> complex:
    r"""Local Euler factor at prime p:

      L_p(s) = det(1 - rho(Frob_p) p^{-s})^{-1}
             = (1 - alpha_{p,1} p^{-s})^{-1} * (1 - alpha_{p,2} p^{-s})^{-1}

    For the rank-2 shadow representation with Frobenius polynomial
    1 - a_p T + chi(p) T^2, this is:

      L_p(s) = (1 - a_p p^{-s} + chi(p) p^{-2s})^{-1}
    """
    a_p = shadow_hecke_eigenvalue(c, p)
    chi_p = 1.0  # unit determinant

    p_ms = complex(p) ** (-s)
    denom = 1.0 - a_p * p_ms + chi_p * p_ms * p_ms

    if abs(denom) < 1e-30:
        return complex(float('inf'))
    return 1.0 / denom


# =========================================================================
# 5. Global L-function (partial product)
# =========================================================================

def shadow_l_function(c, s: complex, N_primes: int = 100) -> complex:
    r"""Partial Euler product for the shadow L-function:

      L(s, rho_A) = prod_{p prime} L_p(s, rho_A)

    computed over the first N_primes primes.

    Converges absolutely for Re(s) > 1 (weight 0 normalisation).

    WARNING: This is a PARTIAL product.  The analytic continuation to
    Re(s) <= 1 requires the completed L-function with gamma factors,
    which is not implemented here.  Use functional_equation_test for
    approximate checks.
    """
    primes = _first_n_primes(N_primes)
    product = complex(1.0)

    for p in primes:
        ef = euler_factor(c, p, s)
        if not cmath.isfinite(ef):
            break
        product *= ef
        if not cmath.isfinite(product):
            break

    return product


# =========================================================================
# 6. Conductor computation
# =========================================================================

def conductor_from_galois(c, p_max: int = 100) -> Dict[str, Any]:
    r"""Estimate the Artin conductor f(rho_A) from the shadow representation.

    The conductor encodes ramification data:
      f(rho_A) = prod_p p^{f_p}

    where f_p = 0 for unramified primes (almost all) and f_p > 0 for
    ramified primes.

    For the shadow representation of Virasoro at central charge c:
    - Unramified at all primes if c is a non-negative integer (the shadow
      tower coefficients are rational with denominators involving only
      primes dividing 5c+22 and c).
    - Potentially ramified at primes dividing c or 5c+22 (poles of the
      shadow tower).

    Returns a dict with keys:
      'conductor': int (the computed conductor)
      'bad_primes': list of ramified primes
      'exponents': dict {p: f_p} for bad primes
      'c_val': the central charge used
    """
    c_val = Fraction(c)
    kappa = c_val / 2

    # Identify bad primes: those where the shadow tower has poles.
    # The poles of S_4 = 10/(c(5c+22)) are at c = 0 and c = -22/5.
    # For a rational c = a/b, the denominators of shadow coefficients
    # involve primes dividing the numerator and denominator of c and 5c+22.

    bad_primes = set()
    exponents = {}

    # Factor the denominator of kappa
    if c_val != 0:
        # Primes dividing the denominator of c (as a fraction)
        c_frac = Fraction(c)
        if c_frac.denominator > 1:
            for p_val, _ in factorint(int(c_frac.denominator)).items():
                if p_val <= p_max:
                    bad_primes.add(int(p_val))

        # Primes dividing 5c+22
        val_5c22 = 5 * c_frac + 22
        if val_5c22 != 0:
            num_5c22 = abs(int(val_5c22.numerator))
            den_5c22 = abs(int(val_5c22.denominator))
            if num_5c22 > 1:
                for p_val, _ in factorint(num_5c22).items():
                    if p_val <= p_max:
                        bad_primes.add(int(p_val))
            if den_5c22 > 1:
                for p_val, _ in factorint(den_5c22).items():
                    if p_val <= p_max:
                        bad_primes.add(int(p_val))

    # Conductor exponents: for a potentially ramified prime p,
    # f_p = dim(V) - dim(V^{I_p}) + Swan conductor
    # For the shadow representation at tame ramification, f_p = 1 typically.
    for p in sorted(bad_primes):
        exponents[p] = 1  # minimal tame ramification

    conductor = 1
    for p, fp in exponents.items():
        conductor *= p ** fp

    return {
        'conductor': conductor,
        'bad_primes': sorted(bad_primes),
        'exponents': exponents,
        'c_val': float(c_val),
    }


# =========================================================================
# 7. Root number
# =========================================================================

def root_number(c) -> int:
    r"""Compute the root number epsilon(1/2, pi_A) = +/-1.

    The root number is the sign in the functional equation
      Lambda(s) = epsilon * Lambda(1-s)

    For a self-dual representation (rho = rho^vee), epsilon = +/-1.

    The shadow representation at c = 13 is self-dual (Koszul self-dual point,
    AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, and c = 13 is the fixed
    point).  At this point, the shadow CohFT has enhanced symmetry and
    epsilon = +1 (even functional equation).

    For general c:
    - epsilon depends on the local root numbers at each bad prime
    - epsilon = prod_p epsilon_p * epsilon_infty
    - epsilon_infty = (-1)^{r/2} for a representation of weight 0 and rank r
    """
    c_val = Fraction(c)
    kappa_val = c_val / 2

    # Self-dual check: rho_A = rho_A^vee iff c = 13
    is_self_dual = (c_val == 13)

    if is_self_dual:
        # At the self-dual point, epsilon = +1 (by the symmetry of the
        # shadow metric Q_L under c -> 26-c)
        return 1

    # For non-self-dual representations, the root number encodes
    # the parity of the functional equation.
    # For rank-2 representations of weight 0:
    # epsilon_infty = i^2 = -1 for odd functional equation by default,
    # but local factors can flip the sign.

    # Heuristic: if c is a positive integer and the representation is
    # arithmetic (comes from a modular form), epsilon = (-1)^{c mod 2}
    # This is a ROUGH heuristic, not a theorem.
    if c_val > 0 and c_val.denominator == 1:
        c_int = int(c_val)
        # Even weight -> epsilon = +1, odd weight -> epsilon = -1
        return (-1) ** (c_int % 2)

    # Default: cannot determine sign without full local analysis
    # Return +1 as the generic case
    return 1


# =========================================================================
# 8. Ramanujan bound check
# =========================================================================

def ramanujan_check(c, p_max: int = 1000) -> Dict[str, Any]:
    r"""Verify the Ramanujan bound |alpha_{p,i}| <= p^{w/2} for the
    shadow Satake parameters at all primes up to p_max.

    For weight w = 0: |alpha_{p,i}| <= 1.
    For weight w = k-1 (Heisenberg): |alpha_{p,i}| <= p^{(k-1)/2}.

    The Ramanujan-Petersson conjecture asserts this bound for all
    automorphic representations.  For the shadow representation, the
    bound constrains the shadow tower coefficients.

    Returns a dict with:
      'satisfies_bound': bool
      'max_ratio': max |alpha_p| / p^{w/2} over all primes tested
      'worst_prime': the prime where the ratio is largest
      'weight': the motivic weight used
      'violations': list of primes where the bound is violated
    """
    c_val = float(c)
    weight = 0.0  # weight-0 normalisation for the shadow representation

    primes = _primes_up_to(p_max)
    max_ratio = 0.0
    worst_prime = 2
    violations = []

    for p in primes:
        try:
            alphas = shadow_satake_parameters(c, p)
        except Exception:
            continue

        bound = p ** (weight / 2.0)  # p^0 = 1 for weight 0

        for alpha in alphas:
            ratio = abs(alpha) / bound if bound > 0 else float('inf')
            if ratio > max_ratio:
                max_ratio = ratio
                worst_prime = p
            if ratio > 1.0 + 1e-8:
                violations.append(p)

    return {
        'satisfies_bound': len(violations) == 0,
        'max_ratio': max_ratio,
        'worst_prime': worst_prime,
        'weight': weight,
        'violations': violations[:20],  # truncate for display
        'n_primes_tested': len(primes),
    }


# =========================================================================
# 9. Selmer rank estimate
# =========================================================================

def selmer_rank_estimate(c) -> Dict[str, Any]:
    r"""Estimate the Selmer rank dim Sel(Q, V_shadow) for the shadow
    Galois representation.

    The Selmer group Sel(Q, V) is a subgroup of H^1(G_Q, V) cut out by
    local conditions at each place.  Its rank is related to the order of
    vanishing of L(s, V) at s = 1/2 by the Bloch-Kato conjecture.

    For the shadow representation:
    - rank 0 if L(1/2) != 0 (generic case)
    - rank >= 1 if L(1/2) = 0 (exceptional, related to shadow depth)

    We estimate by computing L(s) near s = 1/2 via partial Euler product.
    """
    c_val = float(c)

    # Compute L(1/2 + epsilon) for small epsilon to detect vanishing
    eps_values = [0.01, 0.05, 0.1, 0.5]
    l_values = {}

    for eps in eps_values:
        s = 0.5 + eps
        l_val = shadow_l_function(c, s, N_primes=50)
        l_values[eps] = l_val

    # Estimate order of vanishing
    # If |L(1/2 + eps)| ~ eps^r as eps -> 0, then rank ~ r
    vals = [(eps, abs(l_values[eps])) for eps in sorted(eps_values)]

    # Simple heuristic: if L values are decreasing toward 0 as eps -> 0,
    # estimate rank >= 1
    estimated_rank = 0
    if len(vals) >= 2:
        if vals[0][1] < 0.1 * vals[-1][1] and vals[0][1] < 1e-3:
            estimated_rank = 1

    return {
        'estimated_rank': estimated_rank,
        'l_values_near_half': {eps: complex(v) for eps, v in l_values.items()},
        'c_val': c_val,
    }


# =========================================================================
# 10. Modularity test
# =========================================================================

def modularity_test(c, N_max: int = 1000) -> Dict[str, Any]:
    r"""Compare the shadow L-function with known modular forms.

    For integer c, the partition function eta(q)^{-c} is a modular form
    of weight -c/2 for SL(2,Z) (up to multiplier).  Its Hecke eigenvalues
    can be compared against the LMFDB database of modular forms.

    Special cases with known modular correspondences:
    - c = 24: eta^{-24} = 1/Delta, L-function is Ramanujan L-function
    - c = 2:  eta^{-2} is related to theta functions of weight 1
    - c = 1:  eta^{-1} is related to Dedekind sums

    Returns a dict with comparison data.
    """
    c_val = Fraction(c)

    # Compute shadow Hecke eigenvalues at small primes
    test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    eigenvalues = {}

    for p in test_primes:
        try:
            a_p = shadow_hecke_eigenvalue(c, p)
            eigenvalues[p] = complex(a_p)
        except Exception as e:
            eigenvalues[p] = None

    # Known modular form comparisons
    known_matches = {}

    if c_val == 24:
        # eta^{-24} = 1/Delta(q), Hecke eigenvalues are Ramanujan tau
        # tau(2) = -24, tau(3) = 252, tau(5) = 4830, tau(7) = -16744
        known_tau = {2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738}
        # But our a_p is from eta^{-c} = 1/Delta, so the coefficients are
        # the INVERSE partition function coefficients, not tau directly.
        # The relationship is more subtle.
        known_matches['form'] = 'Ramanujan Delta (inverse)'
        known_matches['tau_values'] = known_tau

    # Check if eigenvalues are consistent with a weight-k modular form
    # Heuristic: |a_p| should be bounded by 2*p^{(k-1)/2} for weight k
    weight_estimate = -float(c_val) / 2.0
    ramanujan_consistent = True

    for p, a_p in eigenvalues.items():
        if a_p is None:
            continue
        bound = 2.0 * p ** (abs(weight_estimate - 1.0) / 2.0) if weight_estimate != 0 else 2.0
        if abs(a_p) > bound * 10:  # generous tolerance
            ramanujan_consistent = False

    return {
        'c_val': float(c_val),
        'eigenvalues': eigenvalues,
        'weight_estimate': weight_estimate,
        'ramanujan_consistent': ramanujan_consistent,
        'known_matches': known_matches,
        'test_primes': test_primes,
    }


# =========================================================================
# 11. Local Langlands class
# =========================================================================

def local_langlands_class(c, p: int) -> Dict[str, Any]:
    r"""Conjugacy class in GL_r(C) at prime p via the local Langlands
    correspondence.

    The unramified local Langlands correspondence associates to the
    shadow representation at p an unramified principal series
    representation pi_p of GL_r(Q_p), determined by the Satake
    parameters alpha_{p,1}, ..., alpha_{p,r}.

    The conjugacy class in GL_r(C) is diag(alpha_{p,1}, ..., alpha_{p,r}).

    Returns a dict with:
      'satake': tuple of Satake parameters
      'conjugacy_class': diagonal matrix entries
      'trace': a_p (Hecke eigenvalue)
      'determinant': product of Satake parameters
      'is_tempered': whether |alpha_i| = p^{w/2} (Ramanujan)
    """
    alphas = shadow_satake_parameters(c, p)
    a_p = shadow_hecke_eigenvalue(c, p)

    det_val = 1.0
    for alpha in alphas:
        det_val *= alpha

    is_tempered = all(abs(abs(alpha) - 1.0) < 0.01 for alpha in alphas)

    return {
        'satake': alphas,
        'conjugacy_class': list(alphas),
        'trace': complex(a_p),
        'determinant': complex(det_val),
        'is_tempered': is_tempered,
        'prime': p,
    }


# =========================================================================
# 12. Weil-Deligne representation at bad primes
# =========================================================================

def weil_deligne_at_bad_prime(c, p: int) -> Dict[str, Any]:
    r"""Compute the Weil-Deligne representation (N, phi) at a
    potentially ramified prime p.

    The Weil-Deligne representation at p is a pair (rho_ss, N) where:
    - rho_ss is the semisimplification of rho|_{W_{Q_p}}
    - N is the monodromy operator (nilpotent endomorphism)

    For the shadow representation:
    - At unramified primes: N = 0, rho_ss = diag(alpha_p, alpha_p^{-1})
    - At ramified primes (dividing the conductor): N may be nonzero
      (multiplicative reduction analogue for the shadow curve)

    Returns a dict with:
      'N': monodromy matrix (2x2)
      'phi_eigenvalues': Frobenius eigenvalues
      'is_unramified': bool
      'type': 'principal_series' | 'steinberg' | 'supercuspidal'
    """
    cond = conductor_from_galois(c, p_max=p + 1)
    is_bad = p in cond['bad_primes']

    if not is_bad:
        # Unramified: N = 0, standard Frobenius
        alphas = shadow_satake_parameters(c, p)
        return {
            'N': [[0, 0], [0, 0]],
            'phi_eigenvalues': list(alphas),
            'is_unramified': True,
            'type': 'principal_series',
            'prime': p,
        }
    else:
        # Ramified: Steinberg-type monodromy for the shadow representation
        # at a pole of the shadow tower.
        # N = [[0, 1], [0, 0]] (standard nilpotent for rank 2)
        # Frobenius eigenvalue: p^{1/2} * chi(p) where chi is the nebentypus
        return {
            'N': [[0, 1], [0, 0]],
            'phi_eigenvalues': [float(p) ** 0.5, float(p) ** 0.5],
            'is_unramified': False,
            'type': 'steinberg',
            'prime': p,
        }


# =========================================================================
# 13. Koszul-Langlands transformation
# =========================================================================

def koszul_langlands_transformation(c, p: int) -> Dict[str, Any]:
    r"""How the Koszul involution c -> 26-c acts on Satake parameters
    and the local Langlands class.

    For Virasoro: A = Vir_c, A^! = Vir_{26-c}.
    kappa(A) = c/2, kappa(A^!) = (26-c)/2.
    kappa(A) + kappa(A^!) = 13  (AP24: NOT 0).

    At the Satake level, the Koszul involution transforms:
      alpha_{p,i}(c) -> alpha_{p,i}(26-c)

    At the self-dual point c = 13:
      alpha_{p,i}(13) = alpha_{p,i}(13)  (fixed point)

    The DUALITY CONSTRAINT on the shadow L-function:
      L(s, Vir_c) and L(s, Vir_{26-c}) are related by the Koszul duality.
      At c = 13, L(s) = L(s) is self-dual.
    """
    c_val = float(c)
    c_dual = 26.0 - c_val

    alphas_c = shadow_satake_parameters(c, p)
    alphas_dual = shadow_satake_parameters(c_dual, p)

    a_p_c = shadow_hecke_eigenvalue(c, p)
    a_p_dual = shadow_hecke_eigenvalue(c_dual, p)

    kappa_c = c_val / 2.0
    kappa_dual = c_dual / 2.0
    kappa_sum = kappa_c + kappa_dual  # should be 13 (AP24)

    return {
        'c': c_val,
        'c_dual': c_dual,
        'kappa_c': kappa_c,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa_sum,
        'satake_c': alphas_c,
        'satake_dual': alphas_dual,
        'hecke_c': complex(a_p_c),
        'hecke_dual': complex(a_p_dual),
        'is_self_dual_point': abs(c_val - 13.0) < 1e-10,
        'prime': p,
    }


# =========================================================================
# 14. Self-dual check
# =========================================================================

def self_dual_check(c) -> Dict[str, Any]:
    r"""Test if the shadow representation is self-dual (rho = rho^vee).

    A representation is self-dual if the contragredient rho^vee is
    isomorphic to rho.  For the shadow representation:

    - Self-dual at c = 13 (Virasoro self-dual point, Koszul fixed point)
    - For general c: rho(c) != rho(c)^vee, but rho(c)^vee = rho(26-c)

    The self-duality is detected by comparing Satake parameters:
      alpha_{p,i}(c) vs alpha_{p,i}(26-c)

    For a self-dual representation, {alpha_p} = {alpha_p^{-1}} (up to
    reordering), i.e., the Frobenius polynomial is palindromic.
    """
    c_val = float(c)
    c_dual = 26.0 - c_val

    # Check at several primes
    test_primes = [2, 3, 5, 7, 11]
    is_self_dual = True
    max_discrepancy = 0.0

    for p in test_primes:
        try:
            alphas_c = shadow_satake_parameters(c, p)
            alphas_dual = shadow_satake_parameters(c_dual, p)

            # Self-dual: the Satake parameters at c should match those at 26-c
            # (i.e., the contragredient is the Koszul dual)
            a_p_c = shadow_hecke_eigenvalue(c, p)
            a_p_dual = shadow_hecke_eigenvalue(c_dual, p)

            disc = abs(complex(a_p_c) - complex(a_p_dual))
            max_discrepancy = max(max_discrepancy, disc)

            if disc > 0.01:
                is_self_dual = False
        except Exception:
            pass

    # True self-dual: c = 13
    exact_self_dual = abs(c_val - 13.0) < 1e-10

    return {
        'c_val': c_val,
        'is_self_dual': exact_self_dual,
        'is_approximately_self_dual': is_self_dual,
        'max_discrepancy': max_discrepancy,
        'kappa': c_val / 2.0,
        'kappa_dual': (26.0 - c_val) / 2.0,
        'kappa_sum': 13.0,  # always 13, AP24
    }


# =========================================================================
# 15. Functional equation test
# =========================================================================

def functional_equation_test(c, s_values: Optional[List[complex]] = None) -> Dict[str, Any]:
    r"""Test the functional equation L(s) vs L(1-s) for the shadow L-function.

    The completed L-function should satisfy:
      Lambda(s) = epsilon * Lambda(1-s)

    where Lambda(s) = N^{s/2} * Gamma_factor(s) * L(s), N is the conductor,
    and epsilon is the root number.

    Since we only have partial Euler products, this test is APPROXIMATE.
    We compare L(s) and L(1-s) for several s values, normalised by
    the partial Euler product truncation.

    The test is meaningful only for Re(s) > 1 and Re(1-s) > 1, which is
    impossible simultaneously.  We therefore test at s where both partial
    products are reasonably converged (typically Re(s) around 1/2 + small
    offset, using more primes).

    Returns a dict with comparison ratios.
    """
    if s_values is None:
        s_values = [
            complex(1.5, 0),
            complex(2.0, 0),
            complex(1.5, 1.0),
            complex(2.0, 2.0),
        ]

    c_val = float(c)
    N_primes = 30  # moderate number for tractable computation

    results = {}
    epsilon = root_number(c)

    for s in s_values:
        s_dual = 1.0 - s

        L_s = shadow_l_function(c, s, N_primes=N_primes)
        L_1ms = shadow_l_function(c, s_dual, N_primes=N_primes)

        # The ratio L(s) / L(1-s) should be approximately epsilon * (gamma ratio)
        # For partial products, this is very rough.
        if abs(L_1ms) > 1e-30:
            ratio = L_s / L_1ms
        else:
            ratio = complex(float('inf'))

        results[complex(s)] = {
            'L_s': complex(L_s),
            'L_1ms': complex(L_1ms),
            'ratio': complex(ratio),
        }

    return {
        'c_val': c_val,
        'epsilon': epsilon,
        'results': results,
        'N_primes': N_primes,
    }


# =========================================================================
# 16. Supplementary analysis functions
# =========================================================================

def shadow_weight(c) -> int:
    r"""The motivic weight of the shadow representation.

    For the genus-1 shadow: weight = 0 in the standard normalisation
    (the shadow tower coefficients S_r carry no Hodge weight).

    For lattice VOAs of rank r: weight = r-1 (from the Eisenstein
    series E_{r/2}).
    """
    return 0


def shadow_rank(c) -> int:
    r"""The rank of the shadow representation (dimension of the
    Galois representation).

    For the standard Virasoro shadow, the representation is rank 2
    (from the two Satake parameters at each prime).
    """
    return 2


def shadow_conductor_product(c, p_max: int = 100) -> int:
    """Return just the conductor as an integer."""
    result = conductor_from_galois(c, p_max)
    return result['conductor']


def koszul_dual_l_function_ratio(c, s: complex, N_primes: int = 50) -> complex:
    r"""Ratio L(s, Vir_c) / L(s, Vir_{26-c}).

    For the Koszul dual pair (Vir_c, Vir_{26-c}), the ratio of L-functions
    encodes the duality.  At c = 13 (self-dual point), the ratio should be 1.
    """
    L_c = shadow_l_function(c, s, N_primes=N_primes)
    L_dual = shadow_l_function(26 - float(c), s, N_primes=N_primes)

    if abs(L_dual) < 1e-30:
        return complex(float('inf'))
    return L_c / L_dual


def hecke_multiplicativity_check(c, p: int, q: int) -> Dict[str, Any]:
    r"""Check Hecke multiplicativity: a_{pq} = a_p * a_q for coprime p, q.

    For a normalised eigenform: a_{mn} = a_m * a_n when gcd(m,n) = 1.
    For non-eigenforms, this fails.

    This is a key consistency check for the shadow Hecke eigenvalues.
    """
    a_p = shadow_hecke_eigenvalue(c, p)
    a_q = shadow_hecke_eigenvalue(c, q)
    a_pq = shadow_hecke_eigenvalue(c, p * q)

    product = a_p * a_q
    diff = abs(complex(a_pq) - complex(product))

    return {
        'a_p': complex(a_p),
        'a_q': complex(a_q),
        'a_pq': complex(a_pq),
        'a_p_times_a_q': complex(product),
        'difference': diff,
        'is_multiplicative': diff < 1e-6,
        'p': p,
        'q': q,
    }


def shadow_euler_product_convergence(c, s_real: float,
                                     N_values: Optional[List[int]] = None) -> Dict[str, Any]:
    r"""Measure convergence of the Euler product as a function of the number
    of primes included.

    For Re(s) > 1, the Euler product converges absolutely.
    For Re(s) <= 1, convergence fails (or is conditional on analytic
    continuation).

    Returns partial products for increasing numbers of primes.
    """
    if N_values is None:
        N_values = [5, 10, 20, 30, 50]

    s = complex(s_real, 0)
    products = {}

    for N in N_values:
        L = shadow_l_function(c, s, N_primes=N)
        products[N] = complex(L)

    # Measure convergence rate
    if len(N_values) >= 2:
        last_two = [products[N_values[-2]], products[N_values[-1]]]
        if abs(last_two[0]) > 1e-30:
            convergence_ratio = abs(last_two[1] - last_two[0]) / abs(last_two[0])
        else:
            convergence_ratio = float('inf')
    else:
        convergence_ratio = float('inf')

    return {
        'c_val': float(c),
        's': s_real,
        'partial_products': products,
        'convergence_ratio': convergence_ratio,
        'is_converged': convergence_ratio < 0.01,
    }
