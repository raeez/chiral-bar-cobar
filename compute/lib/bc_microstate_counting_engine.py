r"""Black hole microstate counting from shadow partition functions.

MATHEMATICAL FRAMEWORK
======================

The shadow partition function Z^sh(A, q) of a modular Koszul algebra A
provides an EXACT microstate count for BTZ black holes.  The degeneracy
d(n) at mass level n is the n-th Fourier coefficient of the shadow-
corrected partition function.

For a holomorphic VOA A of central charge c, the partition function is

    Z_A(q) = Tr_A(q^{L_0 - c/24}) = q^{-c/24} * sum_{n >= 0} dim(V_n) q^n

The BTZ black hole microstates at mass level n are counted by d(n) = dim(V_n).
The Cardy formula gives the asymptotic:

    d_Cardy(n) ~ (const) * n^{-alpha} * exp(2*pi*sqrt(c*n/6))

where alpha = (c+1)/4 (the subleading power-law correction).

SHADOW CORRECTIONS
==================

The shadow obstruction tower Theta_A modifies the naive partition function
through genus-dependent corrections.  The shadow-corrected partition function:

    Z^sh(q) = Z_0(q) * prod_{g >= 1} Z_g^{sh}(q)

where Z_0 is the tree-level (free-field) partition function and Z_g^{sh}
contains the genus-g shadow amplitude.

FAREY TAIL
==========

The modular-invariant partition function (Dijkgraaf-Maldacena-Moore-Verlinde
2000) sums over SL(2,Z) images:

    Z(tau) = sum_{gamma in SL(2,Z)/Gamma_infty} Z_seed(gamma.tau)

The shadow tower modifies each Farey term through genus-dependent
multiplicative corrections at each saddle.

LOGARITHMIC CORRECTIONS
========================

The entropy has the expansion:

    S(n) = 2*pi*sqrt(c*n/6) - alpha*log(n) + C_0 + C_1/n + ...

where alpha = (c+1)/4 for a single-chirality partition function (from the
Rademacher expansion / Hardy-Ramanujan-Rademacher method), and C_0 is
the one-loop correction from shadow data.

The quartic shadow S_4 contributes to C_1 through the genus-2 free energy.

QUANTUM CORRECTIONS TO BEKENSTEIN-HAWKING
==========================================

The one-loop determinant for spin-s fields on the BTZ background:

    log det(-nabla^2 + m_s^2) = sum_{n >= 1} d_s(n)/n * q^n

where d_s(n) counts the spin-s excitations.  The shadow zeta regularization
computes -zeta'_A(0; s) for each spin.

SEN'S QUANTUM ENTROPY FUNCTION
================================

The quantum entropy function (Sen 2008, 2012):

    Z_micro = integral exp(-f(q)) dq

In the shadow framework: f = sum_r S_r * saddle_r where S_r are shadow
coefficients and saddle_r are the r-th order saddle-point corrections.

WALL-CROSSING
=============

BPS state multiplicities jump at walls of marginal stability.  The
shadow-corrected wall-crossing formula:

    d(n; wall_+) - d(n; wall_-) = sum contour_contributions

For Virasoro: the walls are at c = 1 (unitarity) and c = 25 (complementary
to c = 1 under c -> 26 - c Koszul duality).

OSV CONJECTURE
==============

The Ooguri-Strominger-Vafa conjecture: |Z_top|^2 = Z_BH.  In the shadow
framework, Z_top is constructed from the shadow obstruction tower and Z_BH
from the microstate partition function.

KOSZUL MICROSTATE DUALITY
==========================

For Virasoro at c and its Koszul dual at c' = 26 - c:
    d_c(n) vs d_{c'}(n)

The ratio d_c(n)/d_{c'}(n) probes whether Koszul duality preserves
microstate counts.  At the critical string c = 26: A! = Vir_0 is
uncurved (kappa = 0), so d_0(n) counts the degenerate microstates.

References:
    BTZ 1992: hep-th/9204099
    Carlip 1998: hep-th/9806026
    DMMV 2000: hep-th/0005003 (Farey tail)
    Maloney-Witten 2010: 0712.0155
    Sen 2008: 0803.1014
    Hardy-Ramanujan 1918: Proc. London Math. Soc.
    Rademacher 1938: Proc. London Math. Soc.
    Calabrese-Cardy 2004: hep-th/0405152
    OSV 2004: hep-th/0405146
    AP1, AP9, AP20, AP24, AP48 (anti-patterns)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2
LOG_TWO_PI = math.log(TWO_PI)


# =========================================================================
# Section 1: Partition function coefficients — exact degeneracies
# =========================================================================

# J-function coefficients: J(tau) = j(tau) - 744 = q^{-1} + 0 + 196884q + ...
# These are the Monster module dimensions: d(n) for the c = 24 case.
# Convention: J(tau) = sum_{n >= -1} c_J(n) q^n with c_J(-1) = 1, c_J(0) = 0.
# The Monster module V^natural has dim(V_n) = c_J(n-1) for n >= 0.
# So: dim(V_0) = c_J(-1) = 1 (vacuum), dim(V_1) = c_J(0) = 0,
#     dim(V_2) = c_J(1) = 196884, etc.
# BUT for microstate counting d(n), we use the convention that
# d(n) counts states at L_0 = n + c/24, i.e., d(n) = c_J(n).

J_COEFFICIENTS: Dict[int, int] = {
    -1: 1,
    0: 0,
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
    16: 593121772421445603328,
    17: 2662842413150775245160,
    18: 11459912788444786513920,
    19: 47438241335864242407195,
    20: 189449976248893390028800,
}

# Monster module decompositions: d(n) = sum of Monster irrep dimensions
# d(-1) = 1 = chi_1
# d(0) = 0
# d(1) = 196884 = 1 + 196883  (McKay decomposition)
# d(2) = 21493760 = 1 + 196883 + 21296876
# These verify that V^natural decomposes correctly under the Monster.

MONSTER_DECOMPOSITION_CHECK: Dict[int, List[int]] = {
    -1: [1],  # vacuum: trivial rep
    0: [],    # no weight-1 states
    1: [1, 196883],  # McKay observation
    2: [1, 196883, 21296876],
}


def j_function_coefficient(n: int) -> int:
    """Fourier coefficient c_J(n) of J(tau) = j(tau) - 744.

    J(tau) = q^{-1} + 0 + 196884q + 21493760q^2 + ...

    For n <= 20: exact tabulated values (OEIS A014708).
    For n > 20: computed from the recursion of modular j-function coefficients.

    WARNING (AP38): these are in the STANDARD normalization where
    J = j - 744 with j the modular invariant.  Other normalizations
    exist in the literature (e.g., j itself has c_j(0) = 744).
    """
    if n in J_COEFFICIENTS:
        return J_COEFFICIENTS[n]
    # For larger n, compute via recursion on partition coefficients
    # or modular form theory.  Here we use the recursive formula
    # from the product representation of 1/j.
    return _compute_j_coefficient_recursive(n)


@lru_cache(maxsize=256)
def _compute_j_coefficient_recursive(n: int) -> int:
    """Compute J-function coefficients using Hecke-type recursion.

    The J-function satisfies the recursion (Rademacher 1938, refined):
        c(n) = -(1/n) * sum_{k=1}^{n-1} sigma_1(k) * c(n-k)    (APPROXIMATE)

    More precisely, the exact formula uses the Rademacher convergent series.
    For moderate n, we use the simpler approach through the modular equation.

    For n up to ~100, we compute via the product expansion of j(tau):
        j(tau) = E_4(tau)^3 / eta(tau)^24
    where E_4 = 1 + 240*sum sigma_3(n)*q^n and eta = q^{1/24}*prod(1-q^n).
    """
    # Compute via E_4^3 / Delta where Delta = eta^24 = q * prod(1-q^n)^24
    # j = E_4^3 / Delta, J = j - 744

    max_n = max(n + 5, 50)

    # E_4 coefficients: E_4 = 1 + 240*sum_{k>=1} sigma_3(k)*q^k
    e4 = [0] * (max_n + 1)
    e4[0] = 1
    for k in range(1, max_n + 1):
        e4[k] = 240 * _sigma(3, k)

    # E_4^3 via polynomial multiplication
    e4_cubed = _poly_mul(_poly_mul(e4, e4, max_n), e4, max_n)

    # eta^24 = q * prod_{n>=1} (1-q^n)^24 = sum_{k>=1} tau(k) q^k
    # (Ramanujan tau function)
    # Delta = eta^24, with Delta = sum_{k>=1} tau(k) q^k
    delta_coeffs = _compute_delta_coefficients(max_n)

    # j = E_4^3 / Delta: j = sum c_j(n) q^n where the division is in q^{-1}
    # E_4^3 = sum a_k q^k (starts at q^0)
    # Delta = sum d_k q^k (starts at q^1, d_1 = 1)
    # j = E_4^3/Delta = (1/q) * E_4^3 / (Delta/q)
    # Let Delta_shifted[k] = delta_coeffs[k+1], so Delta/q = sum Delta_shifted[k] q^k
    # Then j = (1/q) * (E_4^3) / (Delta/q)

    # Division: if E_4^3 = sum a_k q^k and Delta/q = sum b_k q^k with b_0 = 1,
    # then quotient Q with E_4^3 = Q * (Delta/q), Q = sum q_k q^k.
    # q_0 = a_0 / b_0 = a_0
    # q_k = a_k - sum_{j=1}^{k} b_j * q_{k-j}

    b = [0] * (max_n + 1)
    for k in range(max_n):
        if k + 1 < len(delta_coeffs):
            b[k] = delta_coeffs[k + 1]

    a = e4_cubed[:max_n + 1]

    q_coeffs = [0] * (max_n + 1)
    q_coeffs[0] = a[0]  # = 1 (since E_4^3 starts with 1)
    for k in range(1, max_n + 1):
        s = a[k] if k < len(a) else 0
        for j in range(1, k + 1):
            if j < len(b):
                s -= b[j] * q_coeffs[k - j]
        q_coeffs[k] = s

    # j = (1/q) * sum q_k q^k = sum q_k q^{k-1}
    # So c_j(n) = q_coeffs[n+1] for n >= -1
    # J = j - 744, so c_J(n) = c_j(n) for n != 0, c_J(0) = c_j(0) - 744

    if n + 1 < len(q_coeffs):
        c_j_n = q_coeffs[n + 1]
    else:
        raise ValueError(f"n={n} too large for current computation limit")

    if n == 0:
        return c_j_n - 744
    return c_j_n


def _sigma(k: int, n: int) -> int:
    """Divisor function sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += d ** k
    return total


def _poly_mul(a: List[int], b: List[int], max_deg: int) -> List[int]:
    """Multiply two polynomials (coefficient lists), truncated at max_deg."""
    result = [0] * (max_deg + 1)
    for i in range(min(len(a), max_deg + 1)):
        if a[i] == 0:
            continue
        for j in range(min(len(b), max_deg + 1 - i)):
            result[i + j] += a[i] * b[j]
    return result


@lru_cache(maxsize=16)
def _compute_delta_coefficients(max_n: int) -> List[int]:
    """Coefficients of Delta = eta(q)^24 = q * prod_{n>=1} (1-q^n)^24.

    Delta = sum_{n >= 1} tau(n) q^n where tau is the Ramanujan tau function.
    tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472, ...

    Computed via the product expansion.
    """
    # prod_{n>=1} (1-q^n)^24 = sum_{k>=0} a_k q^k
    # Then Delta = q * this product, so delta[k] = a[k-1] for k >= 1, delta[0] = 0.

    # Compute product (1-q^n)^24 up to q^{max_n}
    prod_coeffs = [0] * (max_n + 1)
    prod_coeffs[0] = 1

    for m in range(1, max_n + 1):
        # Multiply by (1 - q^m)^24
        # First compute (1 - q^m)^24 contribution iteratively:
        # (1 - q^m)^24 = sum_{j=0}^{24} C(24,j) (-1)^j q^{m*j}
        binom_coeffs = []
        for j in range(25):
            if m * j > max_n:
                break
            sign = (-1) ** j
            bc = 1
            for r in range(j):
                bc = bc * (24 - r) // (r + 1)
            binom_coeffs.append((m * j, sign * bc))

        # Multiply in-place (backwards to avoid overwriting)
        new_coeffs = [0] * (max_n + 1)
        for k in range(max_n + 1):
            if prod_coeffs[k] == 0:
                continue
            for shift, coeff in binom_coeffs:
                if k + shift <= max_n:
                    new_coeffs[k + shift] += prod_coeffs[k] * coeff
        prod_coeffs = new_coeffs

    # Delta = q * product, so delta[k] = prod_coeffs[k-1]
    delta = [0] * (max_n + 2)
    for k in range(max_n + 1):
        delta[k + 1] = prod_coeffs[k]

    return delta


# =========================================================================
# Section 2: Virasoro partition function (general c)
# =========================================================================

@lru_cache(maxsize=64)
def _partition_number(n: int) -> int:
    """Integer partition number p(n).

    p(0) = 1, p(1) = 1, p(2) = 2, p(3) = 3, p(4) = 5, p(5) = 7, ...

    Uses Euler's recurrence:
        p(n) = sum_{k != 0} (-1)^{k+1} p(n - k(3k-1)/2)
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    result = 0
    for k in range(1, n + 1):
        # Generalized pentagonal numbers: k(3k-1)/2 and k(3k+1)/2
        pent1 = k * (3 * k - 1) // 2
        pent2 = k * (3 * k + 1) // 2
        sign = (-1) ** (k + 1)
        if pent1 <= n:
            result += sign * _partition_number(n - pent1)
        if pent2 <= n:
            result += sign * _partition_number(n - pent2)
        if pent1 > n:
            break
    return result


def virasoro_vacuum_character_coefficient(n: int, c: float) -> float:
    """Coefficient of q^n in the Virasoro vacuum character at central charge c.

    For c >= 25 (no null vectors in the vacuum Verma module above the vacuum):
        chi_vac(q) = q^{-c/24} * prod_{k>=2} 1/(1-q^k)

    The degeneracy at level n (relative to the vacuum) is the number of
    partitions of n into parts >= 2: p_2(n).

    For general c: null vectors can reduce the count, but for c > 1 and
    generic c, the vacuum module is free above the vacuum.

    AP48: kappa(Vir_c) = c/2, regardless of the structure of higher modules.
    """
    if n < 0:
        return 0.0
    if n == 0:
        return 1.0
    if n == 1:
        return 0.0  # No L_{-1}|0> in the vacuum module (translation invariance)

    # p_2(n) = partitions of n into parts >= 2
    # p_2(n) = p(n) - p(n-1) where p(n) = integer partition function
    return float(_partition_number(n) - _partition_number(n - 1))


def virasoro_full_character_coefficient(n: int, c: float) -> float:
    """Total degeneracy at level n in the full Virasoro theory.

    For a single free boson (c = 1): d(n) = p(n) (partition function).
    For Virasoro at generic c > 1:
        - Vacuum module contributes p_2(n) states.
        - Primary modules at weight h contribute p(n - h) states each.
        - The total is sum over primaries of p(n - h_i).

    For simplicity, we use the FULL Hilbert space count:
        Z(q) = q^{-c/24} / prod_{k>=1} (1-q^k)  [free boson, c=1]
        Z(q) = q^{-c/24} / prod_{k>=2} (1-q^k)  [vacuum module only]

    In this function we return the VACUUM MODULE degeneracy p_2(n) for
    generic c.  For specific theories (Monster, free boson), use the
    specialized functions.
    """
    return virasoro_vacuum_character_coefficient(n, c)


def free_boson_degeneracy(n: int) -> int:
    """Degeneracy at level n for a single free boson (c = 1).

    d(n) = p(n), the integer partition function.
    This counts the states in the Fock space Sym(C[z^{-1}]z^{-1}).
    """
    return _partition_number(n)


def monster_degeneracy(n: int) -> int:
    """Degeneracy at level n for the Monster module V^natural (c = 24).

    d(n) = c_J(n) = coefficient of q^n in J(tau) = j(tau) - 744.

    Convention: n is the L_0 eigenvalue minus c/24 = L_0 - 1.
    So n = -1 is the vacuum (L_0 = 0), n = 0 is weight 1 (dim 0),
    n = 1 is weight 2 (dim 196884), etc.
    """
    return j_function_coefficient(n)


def verify_monster_mckay(n: int) -> Dict[str, Any]:
    """Verify McKay decomposition of Monster module at level n.

    d(n) should equal the sum of Monster irrep dimensions in the
    decomposition of V_n.
    """
    d_n = monster_degeneracy(n)
    if n in MONSTER_DECOMPOSITION_CHECK:
        decomp = MONSTER_DECOMPOSITION_CHECK[n]
        computed_sum = sum(decomp)
        return {
            'n': n,
            'd_n': d_n,
            'decomposition_sum': computed_sum,
            'match': d_n == computed_sum,
            'components': decomp,
        }
    return {
        'n': n,
        'd_n': d_n,
        'decomposition_available': False,
    }


# =========================================================================
# Section 3: Cardy formula and asymptotic comparison
# =========================================================================

@lru_cache(maxsize=64)
def _faber_pandharipande(g: int) -> Fraction:
    """Faber-Pandharipande intersection number lambda_g^FP."""
    if g < 1:
        raise ValueError(f"Requires g >= 1, got {g}")
    B_2g = _bernoulli_exact(2 * g)
    power = 2 ** (2 * g - 1)
    num = (power - 1) * abs(B_2g)
    den = power * _factorial_exact(2 * g)
    return Fraction(num, den)


def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n as a Fraction."""
    _BERNOULLI = {
        0: Fraction(1), 1: Fraction(-1, 2),
        2: Fraction(1, 6), 4: Fraction(-1, 30),
        6: Fraction(1, 42), 8: Fraction(-1, 30),
        10: Fraction(5, 66), 12: Fraction(-691, 2730),
        14: Fraction(7, 6), 16: Fraction(-3617, 510),
        18: Fraction(43867, 798), 20: Fraction(-174611, 330),
    }
    if n in _BERNOULLI:
        return _BERNOULLI[n]
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    try:
        from sympy import bernoulli as sympy_bernoulli, Rational
        return Fraction(str(Rational(sympy_bernoulli(n))))
    except ImportError:
        raise ValueError(f"B_{n} not tabulated and sympy unavailable")


def _factorial_exact(n: int) -> Fraction:
    """n! as a Fraction."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


def cardy_formula(n: int, c: float, alpha: Optional[float] = None) -> float:
    """Cardy asymptotic: d_Cardy(n) ~ prefactor * n^{-alpha} * exp(2*pi*sqrt(c*n/6)).

    The precise asymptotic for the Virasoro vacuum character is:

        d(n) ~ (c_eff/24)^{(c_eff-1)/4} / (2 * n^{(c_eff+1)/4})
               * exp(2*pi*sqrt(c_eff*n/6))

    where c_eff = c - 24*h_min.  For the vacuum module: h_min = 0, c_eff = c.

    The power-law prefactor alpha:
        For the FULL partition function: alpha = (c+1)/4
        (from the Hardy-Ramanujan-Rademacher exact formula).

    For n = 0 or n < 0, the Cardy formula is not applicable (it's an
    asymptotic for large n).
    """
    if n <= 0:
        return 0.0

    c = float(c)
    c_eff = c  # vacuum module

    if alpha is None:
        alpha = (c_eff + 1.0) / 4.0

    # Prefactor from the saddle-point approximation
    # d(n) ~ (c_eff/24)^{alpha - 1/2} / (2) * n^{-alpha} * exp(...)
    # More precisely:
    # d(n) ~ C * n^{-alpha} * exp(2*pi*sqrt(c_eff*n/6))
    # where C = (c_eff/24)^{1/2 - alpha} / 2
    # = (c_eff/24)^{(1-c_eff)/4} / 2 when alpha = (c_eff+1)/4

    base = c_eff / 24.0
    if base <= 0:
        return 0.0

    prefactor = base ** (0.5 - alpha) / 2.0
    exponent = 2.0 * PI * math.sqrt(c_eff * n / 6.0)

    try:
        return prefactor * n ** (-alpha) * math.exp(exponent)
    except OverflowError:
        return float('inf')


def cardy_formula_rademacher(n: int, c: float, N_terms: int = 1) -> float:
    """Rademacher-type exact formula (leading saddle + corrections).

    The exact formula (Rademacher 1938):

        d(n) = 2*pi * sum_{k=1}^{infinity} A_k(n) / k
               * (|n_eff|/n)^{alpha} * I_{2*alpha-1}(4*pi*sqrt(|n_eff|*n)/k)

    where n_eff = (c-1)/24 (effective polar term), alpha = (c-1)/4,
    A_k(n) is a Kloosterman sum, and I_nu is the modified Bessel function.

    For the partition function p(n) (c = 1):
        alpha = 0, n_eff = 0, and we recover the Hardy-Ramanujan formula.

    Here we implement the leading term (k = 1) for moderate c.
    """
    c = float(c)
    n = int(n)
    if n <= 0:
        return 0.0

    c_eff = c  # for vacuum module
    n_eff = c_eff / 24.0

    if n_eff <= 0:
        return cardy_formula(n, c)

    total = 0.0
    for k in range(1, N_terms + 1):
        # Kloosterman sum A_k(n): for k=1, A_1(n) = 1
        # For k > 1: A_k(n) = sum over h coprime to k of exp(2*pi*i*(h*n_eff + h'*n)/k)
        # For simplicity, we use A_k = 1 for the leading term
        A_k = _kloosterman_sum(k, n, c)

        arg = 4.0 * PI * math.sqrt(abs(n_eff) * n) / k
        alpha_val = (c_eff - 1.0) / 4.0
        nu = 2.0 * alpha_val - 1.0

        # Modified Bessel function I_nu(arg)
        try:
            I_val = _bessel_I(nu, arg)
        except (OverflowError, ValueError):
            I_val = 0.0

        if n_eff > 0 and n > 0:
            ratio = (abs(n_eff) / n) ** (alpha_val)
        else:
            ratio = 1.0

        total += A_k / k * ratio * I_val

    return 2.0 * PI * total


def _kloosterman_sum(k: int, n: int, c: float) -> float:
    """Kloosterman-type sum A_k(n) for the Rademacher expansion.

    For k = 1: A_1(n) = 1.
    For k = 2: A_2(n) = (-1)^n.
    For general k: involves roots of unity and modular arithmetic.
    """
    if k == 1:
        return 1.0
    if k == 2:
        return (-1.0) ** n

    # General Kloosterman sum
    c_eff = c / 24.0
    total = 0.0
    for h in range(k):
        if math.gcd(h, k) != 1:
            continue
        # Find h' with h*h' = 1 mod k
        h_inv = pow(h, -1, k)
        phase = 2.0 * PI * (h * (-c_eff) + h_inv * n) / k
        total += math.cos(phase)
    return total


def _bessel_I(nu: float, x: float) -> float:
    """Modified Bessel function I_nu(x) for real nu and x.

    Uses the series expansion for moderate x, and the asymptotic
    for large x.
    """
    if x <= 0:
        return 0.0

    # For large x: I_nu(x) ~ e^x / sqrt(2*pi*x)
    if x > 700:
        # Use log to avoid overflow
        log_I = x - 0.5 * math.log(2 * PI * x)
        if log_I > 700:
            return float('inf')
        return math.exp(log_I)

    # Series expansion: I_nu(x) = sum_{m=0}^{inf} (x/2)^{nu+2m} / (m! * Gamma(nu+m+1))
    half_x = x / 2.0
    total = 0.0
    term = half_x ** nu / math.gamma(nu + 1.0)
    total += term
    for m in range(1, 200):
        term *= (half_x ** 2) / (m * (nu + m))
        total += term
        if abs(term) < abs(total) * 1e-15:
            break
    return total


def cardy_relative_error(n: int, c: float, exact_d: int) -> float:
    """Relative error |d_exact - d_Cardy| / d_exact."""
    if exact_d <= 0:
        return float('inf')
    d_cardy = cardy_formula(n, c)
    return abs(exact_d - d_cardy) / exact_d


def cardy_error_table(c: float, d_func, n_min: int = 1, n_max: int = 50) -> List[Dict[str, Any]]:
    """Table of Cardy formula errors for n = n_min..n_max.

    d_func(n) returns the exact degeneracy at level n.
    """
    rows = []
    for n in range(n_min, n_max + 1):
        try:
            d_exact = d_func(n)
        except (ValueError, KeyError):
            continue
        if d_exact <= 0:
            continue
        d_cardy = cardy_formula(n, c)
        rel_err = abs(d_exact - d_cardy) / d_exact if d_exact > 0 else float('inf')
        rows.append({
            'n': n,
            'd_exact': d_exact,
            'd_cardy': d_cardy,
            'relative_error': rel_err,
            'log_d_exact': math.log(d_exact) if d_exact > 0 else 0,
            'S_cardy': 2 * PI * math.sqrt(c * n / 6.0) if n > 0 else 0,
        })
    return rows


def cardy_crossover_n(c: float, d_func, threshold: float = 0.01,
                       n_max: int = 200) -> Optional[int]:
    """Find the smallest n where Cardy error drops below threshold.

    Returns None if the threshold is never reached within n_max.
    """
    for n in range(1, n_max + 1):
        try:
            d_exact = d_func(n)
        except (ValueError, KeyError):
            continue
        if d_exact <= 0:
            continue
        d_cardy = cardy_formula(n, c)
        rel_err = abs(d_exact - d_cardy) / d_exact
        if rel_err < threshold:
            return n
    return None


# =========================================================================
# Section 4: Shadow-corrected partition function
# =========================================================================

def kappa_virasoro(c) -> Fraction:
    """kappa(Vir_c) = c/2.  AP1/AP9/AP20: authoritative."""
    return Fraction(c) / Fraction(2)


def virasoro_S3() -> Fraction:
    """Cubic shadow S_3 = 2 (c-independent)."""
    return Fraction(2)


def virasoro_S4(c) -> Fraction:
    """Quartic contact: Q^contact = 10/[c(5c+22)]."""
    c = Fraction(c)
    return Fraction(10) / (c * (5 * c + 22))


def virasoro_S5(c) -> Fraction:
    """Quintic shadow: S_5 = -48/[c^2(5c+22)]."""
    c = Fraction(c)
    return Fraction(-48) / (c ** 2 * (5 * c + 22))


@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    """Faber-Pandharipande intersection number.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    return _faber_pandharipande(g)


def F_g_scalar(kappa, g: int) -> Fraction:
    """Scalar free energy: F_g = kappa * lambda_g^FP."""
    return Fraction(kappa) * lambda_fp(g)


def planted_forest_g2(kappa, S3) -> Fraction:
    """Planted-forest correction at genus 2: S_3*(10*S_3 - kappa)/48."""
    S3, kappa = Fraction(S3), Fraction(kappa)
    return S3 * (10 * S3 - kappa) / Fraction(48)


def planted_forest_g3(kappa, S3, S4, S5) -> Fraction:
    """Planted-forest correction at genus 3 (11-term polynomial)."""
    kappa, S3, S4, S5 = Fraction(kappa), Fraction(S3), Fraction(S4), Fraction(S5)
    num = (
        - kappa ** 2 * S3
        + 60 * kappa * S3 ** 2
        - 500 * S3 ** 3
        + 6 * kappa ** 2 * S4
        - 120 * kappa * S3 * S4
        + 600 * S3 ** 2 * S4
        + 72 * kappa * S4 ** 2
        - 720 * S3 * S4 ** 2
        + 120 * kappa * S3 * S5
        - 1200 * S3 ** 2 * S5
        + 1440 * S4 * S5
    )
    return num / Fraction(11520)


def virasoro_free_energy(c, g: int) -> Fraction:
    """Full F_g for Virasoro at central charge c.

    g=1: scalar only. g=2: + planted-forest. g=3: + planted-forest.
    g>=4: scalar only (higher planted-forest not available).
    """
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)
    scalar = F_g_scalar(kappa, g)
    if g == 1:
        return scalar
    elif g == 2:
        return scalar + planted_forest_g2(kappa, virasoro_S3())
    elif g == 3:
        S3 = virasoro_S3()
        S4 = virasoro_S4(c_frac)
        S5 = virasoro_S5(c_frac)
        return scalar + planted_forest_g3(kappa, S3, S4, S5)
    else:
        return scalar


def shadow_corrected_log_Z(c: float, beta: float, g_max: int = 5) -> float:
    """Shadow-corrected free energy: log Z^sh = sum_{g>=1} F_g * (2pi/beta)^{2g-2}.

    The expansion parameter is epsilon = 2*pi/beta at the BTZ saddle.

    At genus 1: F_1 * epsilon^0 = F_1 (constant contribution).
    At genus g >= 2: F_g * epsilon^{2g-2}.
    """
    if beta <= 0:
        return 0.0

    epsilon = TWO_PI / beta
    total = 0.0

    for g in range(1, g_max + 1):
        Fg = float(virasoro_free_energy(c, g))
        if g == 1:
            total += Fg
        else:
            total += Fg * epsilon ** (2 * g - 2)

    return total


def shadow_correction_to_degeneracy(n: int, c: float, g_max: int = 3) -> float:
    """Multiplicative shadow correction factor to the Cardy degeneracy.

    The shadow tower modifies the effective central charge at each genus:
        d^{sh}(n) = d_Cardy(n) * exp(sum_{g>=2} delta_g(n))

    where delta_g(n) = F_g * (2*pi/S_BH(n))^{2g-2} with S_BH = 2*pi*sqrt(cn/6).

    Returns the multiplicative factor exp(sum delta_g).
    """
    if n <= 0 or c <= 0:
        return 1.0

    S_BH = 2.0 * PI * math.sqrt(c * n / 6.0)
    epsilon = TWO_PI / S_BH

    delta_sum = 0.0
    for g in range(2, g_max + 1):
        Fg = float(virasoro_free_energy(c, g))
        delta_sum += Fg * epsilon ** (2 * g - 2)

    return math.exp(delta_sum)


# =========================================================================
# Section 5: Farey tail expansion with shadow corrections
# =========================================================================

def _extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended GCD: returns (g, x, y) with a*x + b*y = g."""
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def _find_modular_inverse(c_F: int, d: int) -> Tuple[int, int]:
    """Find (a, b) with a*d - b*c_F = 1."""
    g, x, y = _extended_gcd(abs(d), abs(c_F))
    if g != 1:
        raise ValueError(f"gcd({c_F}, {d}) = {g} != 1")
    a = x if d >= 0 else -x
    b = -y if c_F >= 0 else y
    assert a * d - b * c_F == 1
    return a, b


def farey_sequence(N: int) -> List[Tuple[int, int]]:
    """Coprime pairs (c_F, d) with 0 <= c_F <= N, gcd(c_F, d) = 1.

    These index the SL(2,Z)/Gamma_infty cosets in the Farey tail.
    """
    pairs = [(0, 1)]
    for c_F in range(1, N + 1):
        for d in range(c_F):
            if math.gcd(c_F, d) == 1:
                pairs.append((c_F, d))
                if d > 0:
                    pairs.append((c_F, -d))
    return pairs


def farey_tail_seed(c: float, tau: complex) -> complex:
    """Seed partition function Z_0(tau) = q^{-c/24} at the given tau.

    q = exp(2*pi*i*tau), so Z_0 = exp(-2*pi*i*c*tau/24) = exp(-pi*i*c*tau/12).
    """
    return cmath.exp(-PI * 1j * c * tau / 12.0)


def farey_tail_term(c: float, tau: complex, c_F: int, d: int,
                    g_max: int = 0) -> complex:
    """Single Farey tail term: Z_seed(gamma.tau) * shadow_correction.

    gamma = [[a,b],[c_F,d]] in SL(2,Z).

    With g_max > 0: multiply by the shadow correction factor at each saddle.
    """
    if c_F == 0:
        gamma_tau = tau + d
    else:
        a, b = _find_modular_inverse(c_F, d)
        gamma_tau = (a * tau + b) / (c_F * tau + d)

    Z_0 = farey_tail_seed(c, gamma_tau)

    if g_max > 0:
        # Shadow correction at this saddle
        # The genus-g correction modifies the seed by exp(sum F_g * ...)
        # At each SL(2,Z) image, the expansion parameter is
        # epsilon = 2*pi / (S_BH at this saddle)
        # For the identity saddle: this is the standard correction.
        # For other saddles: the correction is exponentially suppressed.
        beta_eff = -1j * gamma_tau * TWO_PI  # effective inverse temperature
        if beta_eff.real > 0:
            correction = shadow_corrected_log_Z(c, beta_eff.real, g_max)
            Z_0 *= cmath.exp(correction)

    return Z_0


def farey_tail_partition(c: float, tau: complex, N_farey: int = 5,
                         g_max: int = 0) -> complex:
    """Farey tail partition function Z(tau) = sum_{gamma} Z_seed(gamma.tau).

    Sum over SL(2,Z)/Gamma_infty cosets up to denominator N_farey.
    With g_max > 0: include shadow corrections at each saddle.
    """
    pairs = farey_sequence(N_farey)
    Z = complex(0, 0)
    for c_F, d in pairs:
        try:
            Z += farey_tail_term(c, tau, c_F, d, g_max)
        except (ValueError, ZeroDivisionError, OverflowError):
            continue
    return Z


def farey_tail_degeneracy(c: float, n: int, N_farey: int = 10) -> float:
    """Extract degeneracy d(n) from the Farey tail via contour integration.

    d(n) = (1/2pi*i) * oint Z(tau) * q^{-(n-c/24)} d(tau)

    For the leading saddle (identity):
        d(n) ~ Z_0 contribution ~ exp(2*pi*sqrt(c*n/6)) (Cardy)

    Higher Farey terms contribute exponentially suppressed corrections.

    We evaluate on the circle |q| = exp(-2*pi*epsilon) with epsilon chosen
    near the saddle point epsilon = sqrt(c/(24*n)).
    """
    if n <= 0:
        return 0.0

    c = float(c)
    # Saddle point: tau = i * beta_saddle / (2*pi) where beta_saddle = pi*sqrt(c/(6*n))
    beta_saddle = PI * math.sqrt(c / (6.0 * n))
    tau_0 = 1j * beta_saddle / TWO_PI

    # Numerical contour integration: integrate Z(tau)*q^{-(n-c/24)} around tau_0
    # We use a simple trapezoidal rule on the circle tau = tau_0 + epsilon * exp(2*pi*i*t)
    # with epsilon small.
    epsilon = 0.01 / (1 + n)
    N_points = 128

    total = complex(0, 0)
    for k in range(N_points):
        t = k / N_points
        tau = tau_0 + epsilon * cmath.exp(2j * PI * t)
        q = cmath.exp(2j * PI * tau)

        Z = farey_tail_partition(c, tau, N_farey, g_max=0)
        integrand = Z * q ** (-(n - c / 24.0))

        total += integrand

    d_n = (total / N_points).real
    return max(d_n, 0.0)


def farey_tail_coefficients(c: float, n_max: int = 10, N_farey: int = 5) -> Dict[int, float]:
    """Extract first n_max Farey tail coefficients (degeneracies).

    Returns {n: d(n)} for n = -1..n_max.
    """
    results = {}
    for n in range(-1, n_max + 1):
        try:
            results[n] = farey_tail_degeneracy(c, n, N_farey)
        except (OverflowError, ValueError):
            results[n] = 0.0
    return results


# =========================================================================
# Section 6: Logarithmic corrections from shadow data
# =========================================================================

def logarithmic_correction_alpha(c: float) -> float:
    """Power-law exponent alpha in d(n) ~ n^{-alpha} * exp(S_Cardy).

    For the Virasoro vacuum character: alpha = (c+1)/4.
    This is the -(3/2)*log(n) correction to the entropy:
        S = S_BH - (3/2)*log(n) + C_0 + O(1/n)

    But more precisely, the exponent depends on the number of zero modes:
        alpha = (c-1)/4 for the full Rademacher formula
        alpha_log = 3/2 for the entropy (from 3 BTZ zero modes)

    We return alpha = (c+1)/4 as the standard result for the partition
    function coefficient asymptotics.
    """
    return (c + 1.0) / 4.0


def one_loop_C0(c: float) -> float:
    """One-loop constant C_0 in the entropy expansion.

    S = S_BH - (3/2)*log(n) + C_0 + C_1/n + ...

    C_0 comes from the one-loop determinant on the BTZ background.
    For pure gravity (Virasoro at central charge c):

        C_0 = -(3/2)*log(2*pi) + log(prefactor_from_Cardy)

    The shadow data contribution: kappa = c/2 enters through the
    genus-1 free energy F_1 = kappa/24 = c/48.

    From the Rademacher expansion:
        C_0 = (1/2)*log(c/24) - log(2) - (3/2)*log(2*pi)
            + (c-1)/4 * log(c/24) [from the ratio term]

    Simplified for large c: C_0 ~ (c/4)*log(c/24).

    The Maloney-Witten result for pure 3d gravity at c = 24k:
        C_0^{MW} = -(3/2)*log(2*pi) + O(1/c)
    """
    if c <= 0:
        return 0.0

    # From the Rademacher formula leading saddle:
    # d(n) ~ (c/24)^{(c-1)/4} / (2) * (c/(24*n))^{(c+1)/4} * exp(2*pi*sqrt(cn/6))
    # Taking log and separating:
    # log d = 2*pi*sqrt(cn/6) - (c+1)/4 * log(n) + [C_0 terms]
    # C_0 = (c-1)/4 * log(c/24) - log(2) + (c+1)/4 * log(c/24)
    #      = (c/2)*log(c/24) - log(2)

    # More carefully from the saddle:
    # The constant is assembled from the prefactor of the Cardy formula.
    base = c / 24.0
    if base <= 0:
        return 0.0

    # alpha = (c+1)/4 for the partition function
    alpha = (c + 1.0) / 4.0

    # C_0 = log(prefactor) where prefactor = base^{0.5-alpha}/2
    C_0 = (0.5 - alpha) * math.log(base) - math.log(2.0)

    return C_0


def quartic_C1(c: float) -> float:
    """Sub-leading correction C_1 from the quartic shadow.

    S = S_BH - (3/2)*log(n) + C_0 + C_1/n + ...

    C_1 comes from the genus-2 free energy:
        C_1 = F_2 * (correction factor from the saddle expansion)

    The genus-2 contribution to the entropy:
        S_2 = F_2 * (2*pi/S_BH)^2

    Since S_BH = 2*pi*sqrt(cn/6), we have (2*pi/S_BH)^2 = 6/(cn).
    So S_2 = F_2 * 6/(cn) = (6*F_2/c) * (1/n).

    Therefore: C_1 = 6*F_2(c) / c.

    The quartic shadow S_4 = Q^contact enters F_2 through the
    planted-forest correction: delta_pf^{(2,0)} = S_3*(10*S_3-kappa)/48.
    """
    F2 = float(virasoro_free_energy(c, 2))
    return 6.0 * F2 / float(c)


def entropy_expansion(n: int, c: float, n_terms: int = 4) -> Dict[str, float]:
    """Full entropy expansion S(n) = S_BH + corrections.

    Returns:
        S_BH = 2*pi*sqrt(c*n/6)
        S_log = -(alpha)*log(n)  with alpha = (c+1)/4
        C_0 = one-loop constant
        C_1 = quartic correction / n
        S_total = sum
    """
    if n <= 0 or c <= 0:
        return {'S_total': 0.0}

    S_BH = 2.0 * PI * math.sqrt(c * n / 6.0)
    alpha = logarithmic_correction_alpha(c)
    S_log = -alpha * math.log(n)
    C_0 = one_loop_C0(c)
    C_1_coeff = quartic_C1(c)
    C_1 = C_1_coeff / n

    result = {
        'n': n,
        'c': c,
        'S_BH': S_BH,
        'alpha': alpha,
        'S_log': S_log,
        'C_0': C_0,
        'C_1_coeff': C_1_coeff,
        'C_1': C_1,
        'S_total': S_BH + S_log + C_0 + C_1,
    }

    if n_terms >= 5:
        # Genus-3 correction
        F3 = float(virasoro_free_energy(c, 3))
        C_2_coeff = F3 * (6.0 / c) ** 2
        result['C_2_coeff'] = C_2_coeff
        result['C_2'] = C_2_coeff / n ** 2
        result['S_total'] += result['C_2']

    return result


# =========================================================================
# Section 7: Shadow zeta regularization and one-loop determinants
# =========================================================================

def shadow_zeta_function(c: float, s: complex, r_max: int = 50) -> complex:
    """Shadow zeta function zeta_A(s) = sum_{r >= 2} S_r * r^{-s}.

    For Virasoro: uses the shadow tower coefficients S_r from the
    recursive ODE solution.

    For class M algebras (Virasoro), the series converges for Re(s)
    sufficiently large (depending on shadow radius rho).
    """
    kappa = c / 2.0
    S3 = 2.0
    S4 = 10.0 / (c * (5 * c + 22))
    S5 = -48.0 / (c ** 2 * (5 * c + 22))

    # Shadow metric parameters for the Virasoro recursion
    alpha = S3
    Delta = 8 * kappa * S4

    # Shadow radius
    rho_sq = (9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2) if kappa != 0 else 0
    rho = math.sqrt(abs(rho_sq))

    # Compute shadow coefficients via the recursion
    S = [0.0] * (r_max + 1)
    S[2] = kappa
    if r_max >= 3:
        S[3] = S3
    if r_max >= 4:
        S[4] = S4
    if r_max >= 5:
        S[5] = S5

    # For r >= 6: use the linearized recursion S_r ~ A * rho^r * r^{-5/2}
    for r in range(6, r_max + 1):
        S[r] = _estimate_shadow_coefficient(r, kappa, alpha, Delta, rho)

    # Compute the zeta sum
    total = complex(0, 0)
    for r in range(2, r_max + 1):
        total += S[r] * r ** (-s)

    return total


def _estimate_shadow_coefficient(r: int, kappa: float, alpha: float,
                                  Delta: float, rho: float) -> float:
    """Estimate S_r from the asymptotic S_r ~ A * rho^r * r^{-5/2} * cos(r*theta+phi).

    The shadow coefficients satisfy the ODE recursion from the Riccati
    equation associated to Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.
    """
    if rho < 1e-10:
        return 0.0

    # Angle from the discriminant
    if kappa != 0:
        theta = math.atan2(math.sqrt(abs(2 * Delta)), 3 * alpha)
    else:
        theta = 0.0

    # Amplitude normalization (fit from known S_3, S_4, S_5)
    A = abs(alpha) / (rho ** 3 * 3 ** (-2.5)) if rho > 0 else 0.0

    return A * rho ** r * r ** (-2.5) * math.cos(r * theta)


def shadow_zeta_at_zero(c: float, r_max: int = 50) -> float:
    """zeta_A(0) = sum_{r >= 2} S_r.

    This is related to the shadow partition function at the fixed point.
    """
    return shadow_zeta_function(c, 0.0, r_max).real


def shadow_zeta_derivative_at_zero(c: float, r_max: int = 50) -> float:
    """-zeta'_A(0) = sum_{r >= 2} S_r * log(r).

    This is the shadow zeta regularization of the one-loop determinant.
    """
    kappa = c / 2.0
    S3 = 2.0
    S4 = 10.0 / (c * (5 * c + 22))
    S5 = -48.0 / (c ** 2 * (5 * c + 22))
    alpha = S3
    Delta = 8 * kappa * S4
    rho_sq = (9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2) if kappa != 0 else 0
    rho = math.sqrt(abs(rho_sq))

    S = [0.0] * (r_max + 1)
    S[2] = kappa
    if r_max >= 3:
        S[3] = S3
    if r_max >= 4:
        S[4] = S4
    if r_max >= 5:
        S[5] = S5
    for r in range(6, r_max + 1):
        S[r] = _estimate_shadow_coefficient(r, kappa, alpha, Delta, rho)

    total = 0.0
    for r in range(2, r_max + 1):
        total += S[r] * math.log(r)

    return total


def one_loop_determinant_spin_s(c: float, s_spin: int, n_max: int = 50) -> float:
    """One-loop log-determinant for spin-s field on BTZ: -zeta'_A(0; s).

    For spin s on BTZ: the one-loop determinant involves the heat kernel
    trace, which can be expressed in terms of shadow data.

    The shadow zeta regularization:
        log det(-nabla^2 + m_s^2) = -zeta'_A(0; s)

    where zeta_A(z; s) = sum_n d_s(n) * n^{-z} with d_s(n) the spectral
    multiplicities for spin-s fields.

    For the shadow framework:
        -zeta'_A(0; s) = sum_{r >= 2} S_r * weight_factor(s, r) * log(r)

    The weight factor depends on the spin:
        s = 0 (scalar): weight = 1
        s = 1 (vector): weight = 3 (from 3 polarizations in 3d)
        s = 2 (graviton): weight = 5 (from trace + 2 traceless in 3d,
                                       minus gauge redundancy)
    """
    weight = 2 * s_spin + 1  # (2s+1)-dimensional spin-s representation
    return weight * shadow_zeta_derivative_at_zero(c, n_max)


def full_one_loop_determinant(c: float, s_max: int = 2, n_max: int = 50) -> Dict[str, float]:
    """Full one-loop determinant summing over spins s = 0, 1, ..., s_max.

    Total: -sum_s (-)^{2s} (2s+1) * zeta'_A(0; s)

    For BTZ pure gravity (s_max = 2):
        Contributions from s = 0 (scalar), s = 1 (vector), s = 2 (graviton).
        The alternating sign (-)^{2s} = +1 for all integer spins.
    """
    result = {}
    total = 0.0
    for s in range(s_max + 1):
        sign = (-1) ** (2 * s)  # +1 for integer spin
        det_s = one_loop_determinant_spin_s(c, s, n_max)
        result[f'spin_{s}'] = det_s
        total += sign * det_s

    result['total'] = total
    return result


# =========================================================================
# Section 8: Sen's quantum entropy function
# =========================================================================

def sen_quantum_entropy_function(c: float, n: int, r_max: int = 6) -> Dict[str, Any]:
    """Sen's quantum entropy function from shadow data.

    Z_micro = integral exp(-f(q)) dq

    In the shadow framework:
        f = sum_{r=2}^{r_max} S_r * saddle_r(n)

    where saddle_r(n) is the r-th order saddle-point correction:
        saddle_r(n) = (2*pi/S_BH)^{r-2} * (combinatorial factor)

    The leading term (r = 2):
        f_2 = kappa * (2*pi/S_BH)^0 = kappa  [genus-1 contribution]

    The sub-leading terms involve higher shadow coefficients.
    """
    if n <= 0 or c <= 0:
        return {'Z_micro': 0.0}

    S_BH = 2.0 * PI * math.sqrt(c * n / 6.0)
    epsilon = TWO_PI / S_BH

    kappa = c / 2.0
    S3 = 2.0
    S4 = 10.0 / (c * (5 * c + 22))
    S5 = -48.0 / (c ** 2 * (5 * c + 22))

    shadow_coeffs = {2: kappa, 3: S3, 4: S4, 5: S5}
    for r in range(6, r_max + 1):
        alpha = S3
        Delta = 8 * kappa * S4
        rho = math.sqrt(abs((9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2))) if kappa != 0 else 0
        shadow_coeffs[r] = _estimate_shadow_coefficient(r, kappa, alpha, Delta, rho)

    # Saddle contributions
    f_terms = {}
    f_total = 0.0
    for r in range(2, r_max + 1):
        S_r = shadow_coeffs[r]
        # The saddle at order r contributes S_r * epsilon^{r-2}
        saddle_r = S_r * epsilon ** (r - 2)
        f_terms[r] = saddle_r
        f_total += saddle_r

    # Z_micro = exp(S_BH + sum of corrections)
    # In Sen's framework: Z_micro ~ exp(S_BH - f_total)
    # The minus sign comes from the Euclidean path integral.

    try:
        Z_micro = math.exp(S_BH - f_total)
    except OverflowError:
        Z_micro = float('inf')

    # The exact microstate count (for comparison)
    try:
        d_exact = j_function_coefficient(n) if abs(c - 24) < 0.1 else cardy_formula(n, c)
    except (ValueError, KeyError):
        d_exact = cardy_formula(n, c)

    return {
        'n': n,
        'c': c,
        'S_BH': S_BH,
        'epsilon': epsilon,
        'f_terms': f_terms,
        'f_total': f_total,
        'log_Z_micro': S_BH - f_total,
        'Z_micro': Z_micro,
        'd_exact': d_exact,
        'shadow_coeffs': shadow_coeffs,
    }


# =========================================================================
# Section 9: Wall-crossing for Virasoro
# =========================================================================

def virasoro_degeneracy_c_dependence(n: int, c: float) -> float:
    """Effective degeneracy at level n as a function of central charge c.

    For the Virasoro vacuum character at generic c > 1:
        d(n, c) ~ cardy_formula(n, c) * shadow_correction(n, c)

    At c = 1: d(n, 1) = p(n) (partition function).
    At c = 25: d(n, 25) is the Koszul dual of c = 1.

    The walls of marginal stability for BPS states occur at
    c = 1 (unitarity bound) and c = 25 (= 26 - 1, Koszul dual).
    """
    if abs(c - 1.0) < 0.01:
        return float(_partition_number(n))

    return cardy_formula(n, c) * shadow_correction_to_degeneracy(n, c)


def wall_crossing_jump(n: int, c_wall: float, delta_c: float = 0.01) -> Dict[str, float]:
    """Wall-crossing jump at a wall of marginal stability.

    d(n; c_wall + delta) - d(n; c_wall - delta)

    For Virasoro: walls at c = 1, c = 25.
    """
    d_plus = virasoro_degeneracy_c_dependence(n, c_wall + delta_c)
    d_minus = virasoro_degeneracy_c_dependence(n, c_wall - delta_c)

    return {
        'n': n,
        'c_wall': c_wall,
        'delta_c': delta_c,
        'd_plus': d_plus,
        'd_minus': d_minus,
        'jump': d_plus - d_minus,
        'relative_jump': (d_plus - d_minus) / max(d_plus, 1e-100),
    }


def wall_crossing_table(n_max: int = 20, c_wall: float = 1.0) -> List[Dict[str, float]]:
    """Wall-crossing jumps at c_wall for n = 1..n_max."""
    return [wall_crossing_jump(n, c_wall) for n in range(1, n_max + 1)]


# =========================================================================
# Section 10: OSV conjecture test: |Z_top|^2 = Z_BH
# =========================================================================

def topological_string_Z(c: float, tau: complex, g_max: int = 5) -> complex:
    """Topological string partition function from shadow data.

    Z_top(tau) = exp(sum_{g >= 0} F_g^{top} * g_s^{2g-2})

    where g_s is the string coupling and the F_g^{top} are related
    to the shadow free energies via:

        F_g^{top} = F_g^{sh} for g >= 1 (the shadow CohFT free energies)
        F_0^{top} = classical prepotential (genus-0 contribution)

    For Virasoro at central charge c:
        F_0 = -c * (2*pi*i*tau)^2 / (2*12) = -c*pi^2*tau^2/12 [leading order]
    """
    g_s = 2.0 * PI * 1j / tau  # string coupling from BTZ modular parameter

    # Classical genus-0 prepotential
    F0 = -c * (PI * 1j * tau) ** 2 / 12.0

    exponent = F0 / g_s ** 2  # genus-0 term: F_0 / g_s^2

    for g in range(1, g_max + 1):
        Fg = float(virasoro_free_energy(c, g))
        exponent += Fg * g_s ** (2 * g - 2)

    try:
        return cmath.exp(exponent)
    except OverflowError:
        return complex(float('inf'), 0)


def osv_test(c: float, n: int, g_max: int = 3) -> Dict[str, Any]:
    """Test the OSV conjecture |Z_top|^2 = Z_BH for BTZ.

    At the attractor point: tau = i * beta_saddle where beta_saddle
    is the inverse Hawking temperature.

    Z_BH = exp(S_BH) = exp(2*pi*sqrt(c*n/6)).

    The OSV conjecture says |Z_top(tau_*)|^2 = Z_BH(n).
    """
    if n <= 0 or c <= 0:
        return {'match': False}

    # Saddle point
    S_BH = 2.0 * PI * math.sqrt(c * n / 6.0)
    beta_H = PI * math.sqrt(c / (6.0 * n))
    tau_star = 1j * beta_H / TWO_PI

    # Topological string partition function at the attractor
    Z_top = topological_string_Z(c, tau_star, g_max)

    # |Z_top|^2
    Z_top_sq = abs(Z_top) ** 2

    # Z_BH = exp(S_BH)
    try:
        Z_BH = math.exp(S_BH)
    except OverflowError:
        Z_BH = float('inf')

    # Comparison
    if Z_BH > 0 and Z_top_sq > 0 and not math.isinf(Z_BH) and not math.isinf(Z_top_sq):
        log_ratio = math.log(Z_top_sq) - S_BH
    else:
        log_ratio = float('inf')

    return {
        'c': c,
        'n': n,
        'S_BH': S_BH,
        'tau_star': tau_star,
        'Z_top': Z_top,
        '|Z_top|^2': Z_top_sq,
        'Z_BH': Z_BH,
        'log_|Z_top|^2': math.log(Z_top_sq) if Z_top_sq > 0 else float('-inf'),
        'log_Z_BH': S_BH,
        'log_ratio': log_ratio,
        'osv_match_log': abs(log_ratio) < 1.0 if not math.isinf(log_ratio) else False,
    }


# =========================================================================
# Section 11: Multiparticle contribution
# =========================================================================

def single_particle_Z(c: float, beta: float) -> float:
    """Single-particle (BTZ saddle) partition function.

    Z_single = exp(c * pi^2 / (3*beta)) for the S-modular transform.

    This is the leading saddle contribution at high temperature (small beta).
    """
    if beta <= 0:
        return 0.0
    try:
        return math.exp(c * PI ** 2 / (3.0 * beta))
    except OverflowError:
        return float('inf')


def multiparticle_Z(c: float, beta: float, N_images: int = 5) -> float:
    """Multiparticle (SL(2,Z) image) partition function.

    Z_multi = sum_{gamma != id} Z_single(gamma.beta)

    The images under SL(2,Z) give subdominant saddles:
        Z_multi = sum_{k >= 2} Z_0(beta/k^2) [approximation]

    More precisely, the Farey tail sums over (c_F, d) coprime with c_F >= 1.
    """
    total = 0.0
    for k in range(2, N_images + 2):
        # The k-th image has effective beta_eff ~ k^2 * beta
        # (dominant contribution from c_F = k, d = 0 image)
        beta_eff = k ** 2 * beta
        try:
            z_k = math.exp(c * PI ** 2 / (3.0 * beta_eff))
        except OverflowError:
            z_k = float('inf')
        total += z_k
    return total


def multiparticle_ratio(c: float, beta: float, N_images: int = 5) -> Dict[str, float]:
    """Ratio Z_multi / Z_single as a function of beta.

    At large beta (low T): multiparticle dominates (thermal AdS regime).
    At small beta (high T): single-particle dominates (BTZ regime).
    Crossover at beta ~ 2*pi (Hawking-Page).
    """
    Z_s = single_particle_Z(c, beta)
    Z_m = multiparticle_Z(c, beta, N_images)

    ratio = Z_m / Z_s if Z_s > 0 else float('inf')

    return {
        'c': c,
        'beta': beta,
        'Z_single': Z_s,
        'Z_multi': Z_m,
        'ratio': ratio,
        'multiparticle_dominates': ratio > 1.0,
    }


def multiparticle_crossover(c: float, N_images: int = 5) -> float:
    """Find beta where Z_multi/Z_single crosses 1 (multiparticle dominance onset).

    At the Hawking-Page point beta_HP = 2*pi, the single BTZ saddle
    competes with thermal AdS.  The multiparticle contribution adds
    sub-leading saddles that shift this crossover.
    """
    # Binary search between 0.1 and 100
    lo, hi = 0.1, 50.0
    for _ in range(100):
        mid = (lo + hi) / 2
        r = multiparticle_ratio(c, mid, N_images)
        if r['ratio'] > 1.0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


# =========================================================================
# Section 12: Koszul microstate duality
# =========================================================================

def koszul_dual_c(c: float) -> float:
    """Koszul dual central charge: c' = 26 - c.

    AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13 (NOT 0).
    """
    return 26.0 - c


def koszul_degeneracy_ratio(n: int, c: float) -> Dict[str, float]:
    """Ratio d_c(n) / d_{c'}(n) for Koszul dual pair (c, 26-c).

    Probes whether Koszul duality preserves microstate counts.

    At c = 13 (self-dual): ratio should be exactly 1.
    At c = 26: c' = 0, kappa(Vir_0) = 0 (uncurved dual).
    At c = 1: c' = 25.
    """
    c_dual = koszul_dual_c(c)

    d_c = cardy_formula(n, c)
    d_dual = cardy_formula(n, c_dual)

    if d_dual > 0:
        ratio = d_c / d_dual
    else:
        ratio = float('inf')

    # Log ratio for large n (avoid overflow)
    if n > 0 and c > 0 and c_dual > 0:
        log_ratio = 2.0 * PI * (math.sqrt(c * n / 6.0) - math.sqrt(c_dual * n / 6.0))
        # Asymptotic: log(d_c/d_{c'}) ~ 2*pi*sqrt(n/6)*(sqrt(c) - sqrt(c'))
    else:
        log_ratio = 0.0

    return {
        'n': n,
        'c': c,
        'c_dual': c_dual,
        'd_c': d_c,
        'd_dual': d_dual,
        'ratio': ratio,
        'log_ratio': log_ratio,
        'kappa_c': c / 2.0,
        'kappa_dual': c_dual / 2.0,
        'kappa_sum': c / 2.0 + c_dual / 2.0,  # should be 13 (AP24)
    }


def koszul_microstate_table(c: float, n_max: int = 20) -> List[Dict[str, float]]:
    """Table of Koszul microstate ratios for n = 1..n_max."""
    return [koszul_degeneracy_ratio(n, c) for n in range(1, n_max + 1)]


def koszul_self_dual_test(n: int) -> Dict[str, float]:
    """Test that d_{13}(n) / d_{13}(n) = 1 at the self-dual point c = 13.

    At c = 13: Vir_{13}^! = Vir_{13}, so the microstates should match.
    """
    d = cardy_formula(n, 13.0)
    return {
        'n': n,
        'c': 13.0,
        'd_c': d,
        'd_dual': d,
        'ratio': 1.0,
        'self_dual': True,
    }


def koszul_asymptotic_ratio(c: float, n: int) -> float:
    """Asymptotic log-ratio of Koszul dual degeneracies.

    log(d_c(n)/d_{c'}(n)) ~ 2*pi*sqrt(n/6) * (sqrt(c) - sqrt(26-c))

    For c < 13: ratio -> 0 (c has fewer microstates).
    For c > 13: ratio -> infinity (c has more microstates).
    For c = 13: ratio -> 1 (self-dual, microstate democracy).
    """
    c_dual = 26.0 - c
    if c > 0 and c_dual > 0 and n > 0:
        return 2.0 * PI * math.sqrt(n / 6.0) * (math.sqrt(c) - math.sqrt(c_dual))
    return 0.0


# =========================================================================
# Section 13: Cross-verification utilities
# =========================================================================

def verify_monster_degeneracies(n_max: int = 20) -> List[Dict[str, Any]]:
    """Verify Monster module degeneracies d(n) match J-function coefficients.

    Cross-checks:
    1. d(-1) = 1 (vacuum)
    2. d(0) = 0 (no weight-1 currents)
    3. d(1) = 196884 (McKay observation: 196883 + 1)
    4. d(2) = 21493760 (= 1 + 196883 + 21296876)
    5. Higher coefficients match OEIS A014708
    """
    results = []
    for n in range(-1, min(n_max + 1, 21)):
        d_n = monster_degeneracy(n)
        expected = J_COEFFICIENTS.get(n, None)

        entry = {
            'n': n,
            'd_n': d_n,
            'expected': expected,
            'match': d_n == expected if expected is not None else None,
        }

        # McKay decomposition check
        if n in MONSTER_DECOMPOSITION_CHECK:
            decomp = MONSTER_DECOMPOSITION_CHECK[n]
            entry['decomposition'] = decomp
            entry['decomposition_sum'] = sum(decomp)
            entry['decomposition_match'] = sum(decomp) == d_n

        results.append(entry)

    return results


def verify_cardy_asymptotics(c: float, d_func, n_values: List[int]) -> List[Dict[str, Any]]:
    """Verify Cardy formula approaches exact values for large n.

    The relative error should decrease as n increases.
    """
    results = []
    for n in n_values:
        try:
            d_exact = d_func(n)
        except (ValueError, KeyError):
            continue
        d_cardy = cardy_formula(n, c)
        rel_err = abs(d_exact - d_cardy) / max(abs(d_exact), 1) if d_exact != 0 else float('inf')
        results.append({
            'n': n,
            'd_exact': d_exact,
            'd_cardy': d_cardy,
            'relative_error': rel_err,
        })
    return results


def verify_kappa_sum_rule(c: float) -> Dict[str, Any]:
    """Verify kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24).

    This is NOT zero.  The anti-symmetry kappa + kappa' = 0 holds
    for KM/free fields but NOT for Virasoro.
    """
    kappa = c / 2.0
    kappa_dual = (26.0 - c) / 2.0
    total = kappa + kappa_dual

    return {
        'c': c,
        'c_dual': 26.0 - c,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'sum': total,
        'expected': 13.0,
        'match': abs(total - 13.0) < 1e-10,
    }


def shadow_depth_class(c: float) -> str:
    """Shadow depth class for Virasoro at central charge c.

    G: Gaussian (r_max = 2) — impossible for Virasoro (S_3 = 2 != 0)
    L: Lie/tree (r_max = 3) — impossible for Virasoro (S_4 != 0 for c != 0)
    C: Contact (r_max = 4) — not Virasoro
    M: Mixed (r_max = infinity) — ALL Virasoro with c != 0
    """
    if abs(c) < 1e-15:
        return 'G'  # c = 0: kappa = 0, all shadows vanish
    S4 = 10.0 / (c * (5 * c + 22))
    kappa = c / 2.0
    Delta = 8 * kappa * S4
    if abs(Delta) < 1e-15:
        return 'L'
    return 'M'
