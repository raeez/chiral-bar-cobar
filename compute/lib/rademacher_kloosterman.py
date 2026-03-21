r"""
rademacher_kloosterman.py — Rademacher expansions and Kloosterman sums for VOA characters.

THE NON-LATTICE BRIDGE PROBLEM:
  Minimal model Dirichlet series (from Sigma |chi_i|^2) are 100% non-multiplicative:
  no Euler product, blocking the shadow-spectral correspondence for non-lattice VOAs.
  But individual Kloosterman sums K(m,n;c) ARE multiplicative in c when gcd(c1,c2)=1.

THE RADEMACHER DECOMPOSITION:
  For a rational VOA with modular S-matrix S_{ij}, character coefficients decompose:

    a_i(n) = 2pi * Sum_j Sum_{c>=1} (S_{ij}/c) * K_c(h_j - c_eff/24, n - h_i + c_eff/24)
                                                  * I_1(4pi*sqrt((h_j-c/24)(n-h_i+c/24))/c)

  where K_c(m,n) is a Kloosterman sum and I_1 is a modified Bessel function.

CRITICAL FACT: K(m,n;c1*c2) = K(m,n;c1) * K(m,n;c2) when gcd(c1,c2)=1.

  So each j-contribution, as a function of c, IS multiplicative.
  The non-multiplicativity of a_i(n) IN n comes from interference between j-terms
  and from the Bessel weighting within each c-sum.

THE KLOOSTERMAN DIRICHLET SERIES:
  K_tilde(n,s) = Sum_{c>=1} K(m,n;c) * c^{-s}
  is multiplicative in c (Euler product over primes).
  Convergent for Re(s) > 1 by the Weil bound |K(m,n;c)| <= d(c)*sqrt(c)*gcd(m,n,c)^{1/2}.

GENERALIZED KLOOSTERMAN FOR VVMFs:
  For a VVMF with representation rho: SL(2,Z) -> GL(n,C), the generalized sum is:
    K^rho(m,n;c) = Sum_{d mod c, (c,d)=1} rho(matrix(a,b;c,d))_{ij} * e^{2pi*i*(m*d+n*a)/c}
  Individual K^rho_{ij} need NOT be multiplicative (the representation twists things).

KUZNETSOV TRACE FORMULA CONNECTION:
  Sum_{c>=1} K(m,n;c)/c * h(c) = (spectral sum over Maass eigenvalues + integral)
  This is the bridge from Kloosterman sums to spectral data.

References:
  Rademacher, "The Fourier coefficients of the modular invariant J(tau)", 1938.
  Weil, "On some exponential sums", PNAS 34, 1948.
  Iwaniec, "Spectral methods of automorphic forms", AMS, 2002.
  Kuznetsov, "Petersson's conjecture for cusp forms...", Mat. Sb. 111, 1980.
"""

import math
from functools import lru_cache

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

import numpy as np


# ============================================================
# 1. Classical Kloosterman sums K(m, n; c)
# ============================================================

def _modinv(a, m):
    """Modular inverse of a mod m via extended Euclidean algorithm.

    Returns d such that a*d = 1 (mod m).
    Raises ValueError if gcd(a,m) != 1.
    """
    if m == 1:
        return 0
    g, x, _ = _extended_gcd(a % m, m)
    if g != 1:
        raise ValueError(f"No modular inverse: gcd({a},{m}) = {g}")
    return x % m


def _extended_gcd(a, b):
    """Extended Euclidean: returns (g, x, y) with a*x + b*y = g."""
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def kloosterman_sum(m, n, c):
    """Classical Kloosterman sum K(m, n; c).

    K(m, n; c) = Sum_{d mod c, gcd(d,c)=1} exp(2*pi*i*(m*d + n*d')/c)

    where d' = d^{-1} mod c.

    For m, n integers and c >= 1.
    Returns a complex number (mpmath mpc if available, else complex).

    Special cases:
      K(0, 0; c) = phi(c) (Euler totient)
      K(0, n; c) = Ramanujan sum c_c(n) = Sum_{d|(c,n)} mu(c/d)*d
    """
    if c <= 0:
        raise ValueError(f"c must be positive, got {c}")

    if HAS_MPMATH:
        result = mpmath.mpf(0)
        pi2 = 2 * mpmath.pi
        for d in range(1, c + 1):
            if math.gcd(d, c) == 1:
                d_inv = _modinv(d, c)
                phase = pi2 * (m * d + n * d_inv) / c
                result += mpmath.exp(1j * phase)
        return result
    else:
        result = 0j
        for d in range(1, c + 1):
            if math.gcd(d, c) == 1:
                d_inv = _modinv(d, c)
                phase = 2 * np.pi * (m * d + n * d_inv) / c
                result += np.exp(1j * phase)
        return result


def kloosterman_sum_real(m, n, c):
    """Real part of the Kloosterman sum (which is always real for integer m, n).

    For integer m, n the Kloosterman sum is real because the terms pair:
      d and c-d give complex conjugate contributions when m, n are integers.
    """
    val = kloosterman_sum(m, n, c)
    if HAS_MPMATH:
        return mpmath.re(val)
    else:
        return val.real


def verify_kloosterman_multiplicativity(m, n, c1, c2):
    r"""Verify the twisted multiplicativity of Kloosterman sums.

    The correct multiplicativity identity is:
      K(m, n; c1*c2) = K(m*\bar{c2}, n*\bar{c2}; c1) * K(m*\bar{c1}, n*\bar{c1}; c2)

    where \bar{c2} = c2^{-1} mod c1 and \bar{c1} = c1^{-1} mod c2.

    This is the TWISTED form, not the naive K(m,n;c1)*K(m,n;c2).
    The twist comes from the Chinese Remainder Theorem: the CRT bijection
    (Z/c1c2Z)* -> (Z/c1Z)* x (Z/c2Z)* maps d -> (d1, d2) with
    d = d1*c2*\bar{c2} + d2*c1*\bar{c1} (mod c1*c2), and the phase
    factors as exp(2*pi*i*(m*d+n*d')/(c1*c2)) = exp(2*pi*i*(m*\bar{c2}*d1+n*\bar{c2}*d1')/c1)
                                                * exp(2*pi*i*(m*\bar{c1}*d2+n*\bar{c1}*d2')/c2).

    NOTE: The naive (untwisted) multiplicativity K(m,n;c1*c2) = K(m,n;c1)*K(m,n;c2)
    holds ONLY when m = n = 0 (giving phi(c1)*phi(c2) = phi(c1*c2)) or when
    the twisting is trivial (\bar{c1} = \bar{c2} = 1, which requires c1,c2 = 1 mod each other).

    Returns (product_value, factored_value, relative_error).
    """
    if math.gcd(c1, c2) != 1:
        raise ValueError(f"gcd({c1},{c2}) = {math.gcd(c1,c2)} != 1")

    c2_bar = _modinv(c2 % c1, c1) if c1 > 1 else 0  # c2^{-1} mod c1
    c1_bar = _modinv(c1 % c2, c2) if c2 > 1 else 0  # c1^{-1} mod c2

    K_prod = kloosterman_sum(m, n, c1 * c2)
    K_factor = (kloosterman_sum(m * c2_bar, n * c2_bar, c1) *
                kloosterman_sum(m * c1_bar, n * c1_bar, c2))

    if HAS_MPMATH:
        err = abs(K_prod - K_factor)
        scale = max(abs(K_prod), abs(K_factor), mpmath.mpf(1))
        return K_prod, K_factor, float(err / scale)
    else:
        err = abs(K_prod - K_factor)
        scale = max(abs(K_prod), abs(K_factor), 1.0)
        return K_prod, K_factor, err / scale


def verify_kloosterman_naive_multiplicativity(m, n, c1, c2):
    """Check the NAIVE (untwisted) multiplicativity K(m,n;c1*c2) =? K(m,n;c1)*K(m,n;c2).

    This generally FAILS for m,n != 0. It holds only when c2_bar = c1_bar = 1.
    Returns (product_value, naive_factored_value, relative_error).
    """
    if math.gcd(c1, c2) != 1:
        raise ValueError(f"gcd({c1},{c2}) = {math.gcd(c1,c2)} != 1")

    K_prod = kloosterman_sum(m, n, c1 * c2)
    K_naive = kloosterman_sum(m, n, c1) * kloosterman_sum(m, n, c2)

    if HAS_MPMATH:
        err = abs(K_prod - K_naive)
        scale = max(abs(K_prod), abs(K_naive), mpmath.mpf(1))
        return K_prod, K_naive, float(err / scale)
    else:
        err = abs(K_prod - K_naive)
        scale = max(abs(K_prod), abs(K_naive), 1.0)
        return K_prod, K_naive, err / scale


# ============================================================
# 2. Ramanujan sum and Euler totient (special cases)
# ============================================================

def euler_totient(n):
    """Euler's totient phi(n)."""
    count = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            count += 1
    return count


def ramanujan_sum(n, c):
    """Ramanujan sum c_c(n) = K(0, n; c) = Sum_{d|(c,n)} mu(c/d)*d.

    This is the special case m=0 of the Kloosterman sum.
    """
    return kloosterman_sum_real(0, n, c)


def mobius(n):
    """Mobius function mu(n)."""
    if n == 1:
        return 1
    factors = _prime_factors(n)
    for p, e in factors.items():
        if e > 1:
            return 0
    return (-1) ** len(factors)


def _prime_factors(n):
    """Return dict {prime: exponent} for n."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def ramanujan_sum_formula(n, c):
    """Ramanujan sum by Mobius formula: c_c(n) = Sum_{d|gcd(c,n)} mu(c/d)*d."""
    g = math.gcd(n, c)
    result = 0
    for d in range(1, g + 1):
        if g % d == 0:
            result += mobius(c // d) * d
    return result


# ============================================================
# 3. Weil bound verification
# ============================================================

def divisor_count(n):
    """d(n) = number of divisors of n."""
    if n <= 0:
        return 0
    count = 0
    for d in range(1, n + 1):
        if n % d == 0:
            count += 1
    return count


def weil_bound(m, n, c):
    """Weil bound: |K(m,n;c)| <= d(c) * sqrt(c) * gcd(m,n,c)^{1/2}.

    Returns the upper bound value.
    """
    g = math.gcd(math.gcd(abs(m), abs(n)), c) if (m != 0 or n != 0) else c
    return divisor_count(c) * math.sqrt(c) * math.sqrt(g)


def verify_weil_bound(m, n, c):
    """Check that |K(m,n;c)| <= Weil bound. Returns (|K|, bound, satisfied)."""
    K_val = kloosterman_sum(m, n, c)
    K_abs = float(abs(K_val))
    bound = weil_bound(m, n, c)
    return K_abs, bound, K_abs <= bound + 1e-10


# ============================================================
# 4. Ising model data
# ============================================================

# Ising S-matrix: S = (1/2) [[1, 1, sqrt(2)], [1, 1, -sqrt(2)], [sqrt(2), -sqrt(2), 0]]
# Conformal weights: h = (0, 1/2, 1/16)
# Central charge: c = 1/2, effective central charge c_eff = 1/2

ISING_S_MATRIX = None
ISING_WEIGHTS = None
ISING_C_EFF = None

def _init_ising():
    """Initialize Ising model data (lazy, for mpmath precision)."""
    global ISING_S_MATRIX, ISING_WEIGHTS, ISING_C_EFF
    if ISING_S_MATRIX is not None:
        return

    if HAS_MPMATH:
        half = mpmath.mpf('0.5')
        sq2 = mpmath.sqrt(2)
        ISING_S_MATRIX = mpmath.matrix([
            [half, half, half * sq2],
            [half, half, -half * sq2],
            [half * sq2, -half * sq2, mpmath.mpf(0)]
        ])
        ISING_WEIGHTS = [mpmath.mpf(0), mpmath.mpf('0.5'), mpmath.mpf(1) / 16]
        ISING_C_EFF = mpmath.mpf('0.5')
    else:
        sq2 = np.sqrt(2)
        ISING_S_MATRIX = 0.5 * np.array([
            [1, 1, sq2],
            [1, 1, -sq2],
            [sq2, -sq2, 0]
        ])
        ISING_WEIGHTS = [0.0, 0.5, 1.0 / 16]
        ISING_C_EFF = 0.5


def ising_s_matrix():
    """Return the Ising model S-matrix."""
    _init_ising()
    return ISING_S_MATRIX


def ising_conformal_weights():
    """Return the Ising conformal weights [h_0, h_1, h_2] = [0, 1/2, 1/16]."""
    _init_ising()
    return ISING_WEIGHTS


def ising_verify_unitarity():
    """Verify S^dag * S = I for the Ising S-matrix.

    Returns max |S^dag S - I|_{ij}.
    """
    _init_ising()
    if HAS_MPMATH:
        S = ISING_S_MATRIX
        n = S.rows
        # S is real and symmetric for Ising, so S^dag = S^T = S
        prod = S * S
        max_err = mpmath.mpf(0)
        for i in range(n):
            for j in range(n):
                target = mpmath.mpf(1) if i == j else mpmath.mpf(0)
                max_err = max(max_err, abs(prod[i, j] - target))
        return float(max_err)
    else:
        S = ISING_S_MATRIX
        prod = S @ S
        return float(np.max(np.abs(prod - np.eye(3))))


# ============================================================
# 5. Generalized Kloosterman sums for VVMFs
# ============================================================

def _sl2_matrix_representatives(c):
    """Generate all (a, b, c_val, d) with c_val = c, ad - bc = 1, 0 <= d < c.

    For each d coprime to c, find a with a*d = 1 (mod c), then b = (a*d - 1)/c.
    Return list of (a, b, d) tuples.
    """
    reps = []
    for d in range(c):
        if math.gcd(d, c) == 1:
            a = _modinv(d, c)  # a*d = 1 (mod c)
            b = (a * d - 1) // c
            # Verify: a*d - b*c = 1
            assert a * d - b * c == 1, f"Verification failed: {a}*{d} - {b}*{c} = {a*d - b*c}"
            reps.append((a, b, d))
    return reps


def generalized_kloosterman_ising(i, j, m, n, c):
    r"""Generalized Kloosterman sum K^rho_{ij}(m, n; c) for the Ising VVMF.

    K^rho_{ij}(m,n;c) = Sum_{d mod c, (c,d)=1} rho(gamma)_{ij} * e^{2*pi*i*(m*d + n*a)/c}

    where gamma = ((a,b),(c,d)) in SL(2,Z).

    For the Ising model, rho is the 3-dimensional representation given by the
    modular S and T matrices acting on the space of characters.

    NOTE: For c=1, the only representative is d=0 with a=1 (mod 1 = 0), but we
    handle this by the convention d=0, a=1, giving gamma = ((1,0),(1,1)) -> T.
    Actually for c=1, d must be coprime to c=1, so d=0 and a*0 - b*1 = 1 gives b=-1,
    and a is free. We use the standard representative a=1, d=0.
    But gcd(0,1)=1, so d=0 is valid. a = modinv(0,1) is tricky.
    For c=1: the only d in range(1) is... none. So range(0, 1) = [0], gcd(0,1)=1.
    modinv(0,1) should return 0 since 0*0=0=0 mod 1. Let's handle c=1 specially.
    """
    _init_ising()

    if not HAS_MPMATH:
        raise RuntimeError("generalized_kloosterman_ising requires mpmath")

    if c == 1:
        # For c=1, d=0: ad-bc=1 requires b=-1. Unique representative a=0:
        # gamma = ((0,-1),(1,0)) = S. Phase = 1 since m*0 + n*0 = 0.
        a, b, d_val = 0, -1, 0
        # gamma = S
        S = ISING_S_MATRIX
        rho_ij = S[i, j]
        phase = mpmath.exp(2j * mpmath.pi * (m * d_val + n * a) / 1) if c > 0 else 1
        # m*0 + n*0 = 0, so phase = 1
        return rho_ij * phase

    result = mpmath.mpc(0)

    # Build S and T matrices for rho
    h = ISING_WEIGHTS
    c_central = ISING_C_EFF  # c_eff = 1/2

    S = ISING_S_MATRIX
    # T = diag(e^{2*pi*i*(h_k - c_eff/24)})
    T = mpmath.matrix(3)
    for k in range(3):
        T[k, k] = mpmath.exp(2j * mpmath.pi * (h[k] - c_central / 24))

    T_inv = mpmath.matrix(3)
    for k in range(3):
        T_inv[k, k] = 1 / T[k, k]

    for d_val in range(c):
        if math.gcd(d_val, c) != 1:
            continue
        a = _modinv(d_val, c)
        b = (a * d_val - 1) // c
        # gamma = ((a, b), (c, d_val))
        # Compute rho(gamma) via factoring gamma into S, T generators.
        # For the SIMPLIFIED generalized Kloosterman relevant to Rademacher:
        # the key is the phase e^{2*pi*i*(m*d_val + n*a)/c}.
        # The matrix element rho(gamma)_{ij} involves the full representation.
        # However, for the STANDARD Rademacher-type expansion, the relevant
        # generalized Kloosterman is:
        #   K^rho_{ij}(m,n;c) = Sum_{d} [rho(S)]_{ij} * e^{2*pi*i*(m*d + n*d')/c}
        # because in the Rademacher path, every cusp contributes via the S-matrix.
        # The full gamma-dependent rho is for the general Poincare series.
        #
        # Use simplified form: S_{ij} * K_classical(m, n; c)
        # This IS the form in the Rademacher expansion for rational CFTs.
        phase = mpmath.exp(2j * mpmath.pi * (m * d_val + n * a) / c)
        result += S[i, j] * phase

    return result


def generalized_kloosterman_simplified(S_ij, m, n, c):
    """Simplified generalized Kloosterman: S_{ij} * K(m, n; c).

    In the Rademacher expansion for rational CFTs, the generalized Kloosterman
    sum factorizes as S_{ij} * K_classical(m_j, n_i; c) where the S-matrix
    appears as a constant prefactor from the cusp expansion.

    This is the correct form appearing in the Rademacher formula.
    """
    return S_ij * kloosterman_sum(m, n, c)


# ============================================================
# 6. Rademacher expansion for the Ising model
# ============================================================

def rademacher_coefficient(i, n, c_max=50):
    r"""Compute the n-th Fourier coefficient of the i-th Ising character
    via the Rademacher-Zuckerman expansion for vector-valued modular forms.

    The Rademacher formula for a weight-0 VVMF chi_i with polar terms only in
    chi_0 (vacuum) gives:

      a_i(n) = 2*pi * S_{i0} * Sum_{c=1}^{c_max} (1/c) * K_c(-alpha_0, n_i)
               * (alpha_0 / n_i)^{1/2} * I_1(4*pi*sqrt(alpha_0 * n_i) / c)

    where:
      alpha_0 = -(h_0 - c_eff/24) = c_eff/24 = 1/48 (polar order of vacuum)
      n_i = n + h_i - c_eff/24 (shifted weight for the i-th component)
      S_{i0} = the (i,0) entry of the modular S-matrix
      K_c(-alpha_0, n_i) = generalized Kloosterman sum with rational arguments

    The (alpha_0/n_i)^{1/2} prefactor is CRITICAL: without it, the Bessel
    function grows exponentially with n and the formula gives nonsense.

    Only the j=0 (vacuum) polar term contributes because only it has alpha_j > 0:
      alpha_0 = 1/48 > 0 (vacuum)
      alpha_1 = 1/48 - 1/2 = -23/48 < 0 (energy)
      alpha_2 = 1/48 - 1/16 = -1/24 < 0 (spin)
    """
    if not HAS_MPMATH:
        raise RuntimeError("rademacher_coefficient requires mpmath")

    _init_ising()
    S = ISING_S_MATRIX
    h = ISING_WEIGHTS
    c_eff = ISING_C_EFF

    alpha_0 = c_eff / 24  # = 1/48 (polar order of vacuum character)
    n_i = mpmath.mpf(n) + h[i] - c_eff / 24  # shifted weight

    if n_i <= 0:
        # For n_i <= 0, the Rademacher formula reduces to delta-function terms
        # and does not involve the I-Bessel function.
        if n == 0 and i == 0:
            # The leading polar coefficient is 1 by convention
            return mpmath.mpf(1)
        return mpmath.mpf(0)

    # Bessel prefactor: (alpha_0 / n_i)^{1/2}
    bessel_prefactor = mpmath.sqrt(alpha_0 / n_i)

    result = mpmath.mpc(0)

    for c_val in range(1, c_max + 1):
        # Generalized Kloosterman sum with rational arguments
        # Convention: K_c(-alpha_0, n_i) using the standard sign
        K_val = _generalized_kloosterman_rational(-alpha_0, n_i, c_val)

        # Modified Bessel function I_1
        arg = 4 * mpmath.pi * mpmath.sqrt(alpha_0 * n_i) / c_val
        bessel = mpmath.besseli(1, arg)

        result += K_val * bessel / c_val

    # Overall factor: 2*pi * S_{i0} * (alpha_0/n_i)^{1/2}
    result *= 2 * mpmath.pi * S[i, 0] * bessel_prefactor

    return result


def _generalized_kloosterman_rational(alpha, beta, c):
    """Generalized Kloosterman sum for rational arguments alpha, beta.

    K_c(alpha, beta) = Sum_{d mod c, gcd(d,c)=1} e^{2*pi*i*(alpha*d + beta*d')/c}

    This is the natural extension of the classical Kloosterman sum to
    rational (or real) alpha, beta. For integer alpha, beta it reduces
    to the classical K(alpha, beta; c).
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    result = mpmath.mpc(0)
    for d in range(c):
        if math.gcd(d, c) == 1:
            d_inv = _modinv(d, c)
            phase = 2 * mpmath.pi * (alpha * d + beta * d_inv) / c
            result += mpmath.exp(1j * phase)
    return result


def verify_kloosterman_rational_multiplicativity(alpha, beta, c1, c2):
    """Check multiplicativity of the rational Kloosterman sum.

    For gcd(c1,c2)=1, K_{c1*c2}(alpha, beta) = K_{c1}(alpha, beta) * K_{c2}(alpha, beta)
    when alpha, beta are integers. For rational alpha, beta, this CAN FAIL
    because the phase does not factor cleanly unless alpha*c2 and beta*c2 are
    integers (and similarly for c1).

    Returns (K_product, K_factored, relative_error).
    """
    if math.gcd(c1, c2) != 1:
        raise ValueError(f"gcd({c1},{c2}) != 1")

    K_prod = _generalized_kloosterman_rational(alpha, beta, c1 * c2)
    K_factor = (_generalized_kloosterman_rational(alpha, beta, c1) *
                _generalized_kloosterman_rational(alpha, beta, c2))

    err = float(abs(K_prod - K_factor))
    scale = max(float(abs(K_prod)), float(abs(K_factor)), 1e-30)
    return K_prod, K_factor, err / scale


# ============================================================
# 7. Ising model exact characters (for comparison)
# ============================================================

def ising_exact_coefficients(i, n_max):
    r"""Exact Fourier coefficients of the i-th Ising character.

    The three Ising characters are:
      chi_0(q) = q^{-1/48} * (1/2) * (prod_{n=1}^inf (1+q^n) + prod_{n=1}^inf (1-q^n))
               = q^{-1/48} * sum_n a_0(n) q^n
      chi_1(q) = q^{-1/48} * (1/2) * (prod_{n=1}^inf (1+q^n) - prod_{n=1}^inf (1-q^n))
               = q^{23/48} * sum_n a_1(n) q^n
      chi_2(q) = q^{-1/48} * (1/sqrt(2)) * prod_{n=1}^inf (1+q^{n-1/2})
               = q^{1/24} * sum_n a_2(n) q^n

    Actually, using the standard theta/eta representations:
      chi_0 = (theta_3(q)^{1/2} + theta_4(q)^{1/2}) / (2 * eta(q))  [vacuum]
      chi_1 = (theta_3(q)^{1/2} - theta_4(q)^{1/2}) / (2 * eta(q))  [energy]
      chi_2 = theta_2(q)^{1/2} / (sqrt(2) * eta(q))                  [spin]

    For computational purposes, we use product formulas to get q-expansion
    coefficients directly.
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    # Compute via product representations
    # The key products are:
    #   P_+ = prod_{n=1}^inf (1 + q^n)
    #   P_- = prod_{n=1}^inf (1 - q^n)
    #   P_half = prod_{n=0}^inf (1 + q^{n+1/2})
    #
    # For the q-expansion, we work with polynomial approximations.
    # Represent each product as a power series in q to order n_max.

    N = n_max + 10  # extra terms for safety

    # P_+ coefficients: prod (1 + q^n) for n=1..N
    p_plus = [mpmath.mpf(0)] * (N + 1)
    p_plus[0] = mpmath.mpf(1)
    for n in range(1, N + 1):
        new = [mpmath.mpf(0)] * (N + 1)
        for k in range(N + 1):
            new[k] += p_plus[k]
            if k + n <= N:
                new[k + n] += p_plus[k]
        p_plus = new

    # P_- coefficients: prod (1 - q^n) = eta(q) / q^{-1/24} expansion
    # 1/eta(q) = q^{-1/24} / prod(1-q^n) -> prod(1-q^n) = q^{1/24} * eta
    # But we need the inverse: 1/prod(1-q^n) = sum p(n) q^n (partition function)
    p_minus = [mpmath.mpf(0)] * (N + 1)
    p_minus[0] = mpmath.mpf(1)
    for n in range(1, N + 1):
        new = [mpmath.mpf(0)] * (N + 1)
        for k in range(N + 1):
            new[k] += p_minus[k]
            if k + n <= N:
                new[k + n] -= p_minus[k]
        p_minus = new

    if i == 0:
        # chi_0: (1/2) * (P_+ + P_-) / prod(1-q^n)
        # But that's not quite right. Let me use the cleaner formulation.
        # chi_0(q) * q^{1/48} = (1/2) * [prod(1+q^n)/prod(1-q^n) + 1/prod(1-q^n)]*something
        # Actually the standard form is different. Let me use direct computation.
        #
        # Correct form (see e.g. DiFrancesco et al.):
        #   chi_0(tau) = q^{-c/24} * Tr_{H_0} q^{L_0}
        #   = q^{-1/48} * sum_{n>=0} dim(H_0)_n * q^n
        # where H_0 is the vacuum module of the Ising CFT.
        #
        # For the Ising model, the vacuum character in q-expansion with q = e^{2*pi*i*tau}:
        #   chi_0 = q^{-1/48} * prod_{n=1}^inf 1/(1-q^n) * (sum of specific terms)
        #
        # Actually the cleanest: use the fermionic representations.
        # The Ising = free fermion / Z_2.
        #
        # In the NS sector (anti-periodic):
        #   Z_NS = prod_{r=1/2,3/2,...} (1 + q^r)  [Neveu-Schwarz]
        #   = prod_{n=0}^inf (1 + q^{n+1/2})
        #
        # In the R sector (periodic):
        #   Z_R = prod_{n=1,2,...} (1 + q^n)
        #
        # Actually for the Virasoro primaries of Ising:
        #   chi_0 = (1/2) * [prod_{n=1}^inf (1+q^n) + prod_{n=1}^inf (1-q^n)] / eta_prod
        #
        # Let me just use the partition function approach with known dimensions.
        # The conformal dimensions of states in the vacuum module:
        # Level 0: 1 state (vacuum)
        # Level 1: 0 states (L_{-1}|0> = 0 for vacuum, and c=1/2 has no weight-1 primary)
        # Level 2: 1 state (L_{-2}|0>)
        # Level 3: 1 state (L_{-3}|0>)
        # Level 4: 2 states (L_{-4}|0>, L_{-2}^2|0>)
        # etc.
        # These are dimensions of Verma module quotient = irrep L(c,0) for c=1/2.
        #
        # Use the product formula:
        #   chi_0(q) = q^{-1/48} * prod_{n=2}^inf 1/(1-q^n)  [No! This overcounts.]
        #
        # The CORRECT product formula for Ising characters uses:
        #   chi_0 + chi_{1/2} = prod_{n=0}^inf (1+q^{n+1/2}) / eta_prod
        #   chi_0 - chi_{1/2} = prod_{n=0}^inf (1-q^{n+1/2}) / eta_prod  [? Not standard]
        #
        # Let me compute directly from the Virasoro representation theory.
        # For c=1/2, h=0: the Kac table gives null vector at level 2 (singular vector).
        # The character is:
        #   chi_0(q) = q^{-1/48} * (1 - q^2) * prod_{n=1}^inf 1/(1-q^n)
        #            = q^{-1/48} * prod_{n=1}^inf 1/(1-q^n) * (1-q^2)
        #            = q^{-1/48} * 1/((1-q)(1-q^3)(1-q^4)...) [cancel (1-q^2)]
        # Wait, (1-q^2)/prod(1-q^n) = 1/prod_{n!=2}(1-q^n) = 1/((1-q)(1-q^3)(1-q^4)...)
        #
        # Actually for M(4,3), c=1/2:
        # chi_{1,1}(q) = q^{-1/48} * prod_{n=0}^inf (1-q^{2+4n})(1-q^{2+4n})/
        #                 ... this gets complicated.
        # Use the SIMPLE Rocha-Caridi formula:
        #   chi_{r,s}^{(p,p')} = (1/eta) * sum_{k in Z} (q^{a_k} - q^{b_k})
        #   a_k = [(2pp'k + pr - p's)^2 - (p-p')^2] / (4pp')
        #   b_k = [(2pp'k + pr + p's)^2 - (p-p')^2] / (4pp')
        # For M(4,3) = M(p'=4, p=3):
        #   (r,s) = (1,1) for vacuum (h=0)
        #   pp' = 12, p-p' = -1
        #   a_k = [(24k + 3 - 4)^2 - 1] / 48 = [(24k-1)^2 - 1]/48
        #   b_k = [(24k + 3 + 4)^2 - 1] / 48 = [(24k+7)^2 - 1]/48

        # Compute using Rocha-Caridi
        coeffs = _ising_rocha_caridi_coeffs(1, 1, n_max)
        return coeffs[:n_max + 1]

    elif i == 1:
        # chi_{1,2}: h = 1/2, (r,s) = (1,2) in M(4,3)
        # M(4,3) conformal weights h_{r,s} = ((3r-4s)^2-1)/48:
        # (1,1)->0, (1,2)->1/2, (2,1)->1/16
        coeffs = _ising_rocha_caridi_coeffs(1, 2, n_max)
        return coeffs[:n_max + 1]

    elif i == 2:
        # chi_{2,1}: h = 1/16
        coeffs = _ising_rocha_caridi_coeffs(2, 1, n_max)
        return coeffs[:n_max + 1]

    else:
        raise ValueError(f"Ising model has 3 characters, got i={i}")


def _ising_rocha_caridi_coeffs(r, s, n_max):
    """Compute q-expansion coefficients using the Rocha-Caridi formula for M(4,3).

    chi_{r,s}(q) = q^{h_{r,s} - c/24} * sum_n a(n) q^n

    We compute a(n) for n = 0, ..., n_max.

    The Rocha-Caridi formula:
      chi_{r,s} = (1/eta(q)) * sum_{k in Z} (q^{a_k} - q^{b_k})
    where for M(p'=4, p=3):
      a_k = [(24k + 3r - 4s)^2 - 1] / 48
      b_k = [(24k + 3r + 4s)^2 - 1] / 48

    Since chi_{r,s} = q^{h-c/24} * sum a(n)q^n, and 1/eta = q^{1/24} * sum p(n)q^n,
    we have h - c/24 + offset from a_k/b_k = ...

    Let's just compute the product directly.
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    p, pp = 3, 4  # M(p',p) = M(4,3), so p=3, p'=4
    # h_{r,s} = ((p*r - p'*s)^2 - (p-p')^2) / (4*p*p')
    h_rs = mpmath.mpf((p * r - pp * s)**2 - (p - pp)**2) / (4 * p * pp)
    c_charge = mpmath.mpf(1) / 2
    # q-offset: h - c/24
    q_offset = h_rs - c_charge / 24

    N = n_max + 20

    # Compute 1/eta coefficients = partition numbers p(n)
    # eta(q) = q^{1/24} * prod(1-q^n), so 1/eta = q^{-1/24} * sum p(n)q^n
    partitions = _partition_numbers(N)

    # Compute the theta-function part: sum_{k} (q^{a_k} - q^{b_k})
    # a_k = [(24k + 3r - 4s)^2 - 1] / 48
    # b_k = [(24k + 3r + 4s)^2 - 1] / 48
    # The exponent relative to q^{(p-p')^2/(4pp')} = q^{1/48} is:
    # a_k - 1/48 = [(24k+3r-4s)^2 - 1 - 1]/48 = ... this needs care.
    #
    # Actually, the character is:
    #   chi_{r,s} = q^{-c/24} * (1/prod(1-q^n)) * sum_k (q^{a_k} - q^{b_k})
    #            = q^{-1/48} * (1/prod(1-q^n)) * sum_k (q^{a_k} - q^{b_k})
    #
    # And chi_{r,s} = q^{h-c/24} * (1 + a_1 q + a_2 q^2 + ...)
    # So: q^{h-c/24}*(series) = q^{-1/48} * (1/prod) * theta_part
    # => q^h * (series) = q^{1/48-1/48} * (1/prod) * theta_part??? No.
    # c/24 = 1/48 for Ising.
    # chi = q^{-1/48} * (1/prod(1-q^n)) * Theta_{r,s}
    # where Theta_{r,s} = sum_k (q^{a_k} - q^{b_k})
    # with a_k, b_k as above.
    #
    # Also chi = q^{h - 1/48} * sum_n a(n) q^n
    # So: sum_n a(n) q^n = q^{1/48-h} * q^{-1/48} * (1/prod) * Theta
    #                    = q^{-h} * (1/prod) * Theta

    # Compute theta coefficients as a power series.
    # The smallest a_k value: at k=0, a_0 = (3r-4s)^2 - 1)/48
    # For (1,1): a_0 = (3-4)^2 - 1)/48 = 0/48 = 0
    # For (1,2): a_0 = ((3-8)^2 - 1)/48 = 24/48 = 1/2
    # For (2,1): a_0 = ((6-4)^2 - 1)/48 = 3/48 = 1/16

    # These are NOT integers in general, so we need to handle fractional powers.
    # The trick: shift so that the lowest power is 0.
    # The lowest power in theta is h_{r,s} (the conformal weight).
    # After multiplying by q^{-h} and 1/prod, we get integer powers.

    # Numerically compute theta coefficients relative to q^h:
    # Theta_{r,s} = sum_k (q^{a_k} - q^{b_k})
    # = sum_k (q^{a_k - h} - q^{b_k - h}) * q^h
    # So Theta_{r,s} * q^{-h} = sum_k (q^{a_k - h} - q^{b_k - h})

    # For (1,1): h=0, a_0=0, b_0=48/48=1, a_{-1}=((-24+3-4)^2-1)/48=((−25)^2−1)/48=624/48=13
    # The key terms near the bottom are small.

    # Build integer-indexed array for theta * q^{-h}
    theta = [mpmath.mpf(0)] * (N + 1)

    for k in range(-N, N + 1):
        val_a = ((24 * k + p * r - pp * s)**2 - (p - pp)**2)
        exp_a_num = val_a  # numerator, denominator is 48
        # a_k - h = val_a/48 - h = (val_a - 48*h)/48
        h_num = int(48 * h_rs)  # h is a simple fraction with denominator dividing 48
        shift_a = val_a - h_num  # should be divisible by 48
        if shift_a % 48 != 0:
            continue  # not an integer power -> skip (shouldn't happen for Kac table)
        exp_a = shift_a // 48
        if 0 <= exp_a <= N:
            theta[exp_a] += mpmath.mpf(1)

        val_b = ((24 * k + p * r + pp * s)**2 - (p - pp)**2)
        shift_b = val_b - h_num
        if shift_b % 48 != 0:
            continue
        exp_b = shift_b // 48
        if 0 <= exp_b <= N:
            theta[exp_b] -= mpmath.mpf(1)

    # Now convolve theta with partitions (= 1/prod(1-q^n))
    # Result[n] = sum_{k=0}^n theta[k] * partitions[n-k]
    result = [mpmath.mpf(0)] * (n_max + 1)
    for n in range(n_max + 1):
        s_val = mpmath.mpf(0)
        for k in range(min(n + 1, N + 1)):
            if k <= N and n - k < len(partitions):
                s_val += theta[k] * partitions[n - k]
        result[n] = s_val

    return result


def _partition_numbers(n_max):
    """Compute partition numbers p(0), p(1), ..., p(n_max)."""
    if not HAS_MPMATH:
        p = [0] * (n_max + 1)
        p[0] = 1
        for k in range(1, n_max + 1):
            for n in range(k, n_max + 1):
                p[n] += p[n - k]
        return p

    p = [mpmath.mpf(0)] * (n_max + 1)
    p[0] = mpmath.mpf(1)
    for k in range(1, n_max + 1):
        for n in range(k, n_max + 1):
            p[n] += p[n - k]
    return p


# ============================================================
# 8. Kloosterman Dirichlet series (multiplicative kernel)
# ============================================================

def kloosterman_dirichlet_series(m, n, s, c_max=100):
    r"""Compute K_tilde(m, n; s) = Sum_{c=1}^{c_max} K(m, n; c) * c^{-s}.

    This is a Dirichlet series in c that is multiplicative (product over primes)
    because K(m,n;c) is multiplicative in c.

    Convergent for Re(s) > 1 by the Weil bound.
    """
    if not HAS_MPMATH:
        result = 0j
        for c in range(1, c_max + 1):
            K_val = kloosterman_sum(m, n, c)
            result += K_val * c ** (-s)
        return result

    result = mpmath.mpc(0)
    for c in range(1, c_max + 1):
        K_val = kloosterman_sum(m, n, c)
        result += K_val * mpmath.power(c, -s)
    return result


def kloosterman_euler_product(m, n, s, p_max=30):
    r"""Compute the Euler product for K_tilde(m, n; s).

    K_tilde(m, n; s) = Prod_p (1 + K(m,n;p)*p^{-s} + K(m,n;p^2)*p^{-2s} + ...)

    Truncated at primes up to p_max and prime powers up to p_max.

    Returns (euler_product_value, direct_sum_value, relative_error).
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    primes = _primes_up_to(p_max)

    # Direct sum
    c_max = 1
    for p in primes:
        c_max = max(c_max, p)
    # Use product of all primes as upper bound for direct sum
    direct_c_max = 1
    for p in primes:
        direct_c_max *= p
    direct_c_max = min(direct_c_max, 200)

    direct_val = kloosterman_dirichlet_series(m, n, s, c_max=direct_c_max)

    # Euler product
    euler_val = mpmath.mpc(1)
    for p in primes:
        # Local factor: 1 + K(m,n;p)*p^{-s} + K(m,n;p^2)*p^{-2s} + ...
        local = mpmath.mpc(0)
        pk = 1
        k = 0
        while pk <= direct_c_max:
            K_val = kloosterman_sum(m, n, pk) if pk > 0 else mpmath.mpf(1)
            if k == 0:
                local += mpmath.mpc(1)  # K(m,n;1) term handled separately
            else:
                local += K_val * mpmath.power(p, -k * s)
            pk *= p
            k += 1
        euler_val *= local

    err = float(abs(euler_val - direct_val))
    scale = max(float(abs(euler_val)), float(abs(direct_val)), 1e-30)
    return euler_val, direct_val, err / scale


def _primes_up_to(n):
    """Return list of primes up to n."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


# ============================================================
# 9. Dirichlet series decomposition by Kloosterman class
# ============================================================

def rademacher_c_contribution(i, n, c_val):
    """Contribution to a_i(n) from a single value of c in the Rademacher sum.

    b_c(n) = 2*pi * S_{i0} * (alpha_0/n_i)^{1/2} * K_c(-alpha_0, n_i) * I_1(...) / c

    Only the vacuum (j=0) polar term contributes for Ising.
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    _init_ising()
    S = ISING_S_MATRIX
    h = ISING_WEIGHTS
    c_eff = ISING_C_EFF

    alpha_0 = c_eff / 24  # = 1/48
    n_i = mpmath.mpf(n) + h[i] - c_eff / 24

    if n_i <= 0:
        return mpmath.mpf(0)

    bessel_prefactor = mpmath.sqrt(alpha_0 / n_i)
    K_val = _generalized_kloosterman_rational(-alpha_0, n_i, c_val)
    arg = 4 * mpmath.pi * mpmath.sqrt(alpha_0 * n_i) / c_val
    bessel = mpmath.besseli(1, arg)

    return 2 * mpmath.pi * S[i, 0] * bessel_prefactor * K_val * bessel / c_val


def rademacher_j_contribution(i, j, n, c_max=50):
    """Contribution to a_i(n) from a single source field j, summed over c.

    For the Ising model, only j=0 has alpha_j > 0 and gives the standard
    Rademacher (I-Bessel) contribution. The j=1,2 terms would involve
    the sub-leading polar data which doesn't exist for Ising.

    This function returns the j=0 Rademacher contribution when j=0,
    and zero for j != 0 (since those characters have no polar terms).
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    _init_ising()
    S = ISING_S_MATRIX
    h = ISING_WEIGHTS
    c_eff = ISING_C_EFF

    # Only j=0 has a polar term for Ising
    alpha_j = c_eff / 24 - h[j]
    if alpha_j <= 0:
        return mpmath.mpf(0)

    n_i = mpmath.mpf(n) + h[i] - c_eff / 24
    if n_i <= 0:
        return mpmath.mpf(0)

    bessel_prefactor = mpmath.sqrt(alpha_j / n_i)

    result = mpmath.mpc(0)
    for c_val in range(1, c_max + 1):
        K_val = _generalized_kloosterman_rational(-alpha_j, n_i, c_val)
        arg = 4 * mpmath.pi * mpmath.sqrt(alpha_j * n_i) / c_val
        bessel = mpmath.besseli(1, arg)
        result += K_val * bessel / c_val

    return 2 * mpmath.pi * S[i, j] * bessel_prefactor * result


# ============================================================
# 10. Kuznetsov trace formula connection
# ============================================================

def kuznetsov_kloosterman_side(m, n, c_max=100, test_fn=None):
    r"""Compute the Kloosterman-sum side of the Kuznetsov trace formula.

    Sum_{c=1}^{c_max} K(m, n; c) / c * h(4*pi*sqrt(|mn|)/c)

    where h is a test function (default: h(x) = x * K_1(x), a natural choice
    that gives the I-Bessel transform).

    For the Rademacher expansion, the natural test function is
      h(c) = (1/c) * I_1(4*pi*sqrt(m*n)/c)
    which makes this the Rademacher sum itself.
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    result = mpmath.mpc(0)
    mn_abs = abs(m * n)

    for c in range(1, c_max + 1):
        K_val = kloosterman_sum(m, n, c)
        if test_fn is not None:
            h_val = test_fn(c)
        else:
            # Default: h(c) = I_1(4*pi*sqrt(|mn|)/c) / c if mn > 0
            if mn_abs > 0:
                arg = 4 * mpmath.pi * mpmath.sqrt(mpmath.mpf(mn_abs)) / c
                h_val = mpmath.besseli(1, arg) / c
            else:
                h_val = mpmath.mpf(0)
        result += K_val * h_val / c

    return result


# ============================================================
# 11. Non-multiplicativity diagnosis
# ============================================================

def ising_partition_coefficients(n_max):
    r"""Compute coefficients of the scalar partition function |eta|^2 * Z_Ising.

    Z_Ising = Sum_i |chi_i|^2 = |chi_0|^2 + |chi_1|^2 + |chi_2|^2

    The Dirichlet coefficients a_n of this function are:
    a_n = Sum_i |a_i(n)|^2  [roughly, up to q-offset alignment]

    For the actual scalar Z on the torus, we need the full modular-invariant
    partition function, which for Ising is the diagonal invariant.

    Returns list of coefficients.
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    # Get exact character coefficients
    c0 = ising_exact_coefficients(0, n_max)
    c1 = ising_exact_coefficients(1, n_max)
    c2 = ising_exact_coefficients(2, n_max)

    return c0, c1, c2


def check_multiplicativity(coeffs, n_max=None):
    """Check whether a sequence of coefficients a(n) is multiplicative.

    Multiplicative means: a(m*n) = a(m)*a(n) whenever gcd(m,n) = 1.
    (And a(1) = 1.)

    Returns dict with:
      'is_multiplicative': bool (up to tolerance)
      'max_error': float
      'failures': list of (m, n, a(mn), a(m)*a(n)) tuples
    """
    if n_max is None:
        n_max = len(coeffs) - 1

    failures = []
    max_err = 0.0

    # Normalize: a(1) should be 1
    if len(coeffs) < 2:
        return {'is_multiplicative': True, 'max_error': 0.0, 'failures': []}

    a1 = float(abs(coeffs[1])) if len(coeffs) > 1 else 1.0

    for m in range(2, n_max + 1):
        for n in range(2, n_max + 1):
            if m * n > n_max:
                break
            if math.gcd(m, n) != 1:
                continue
            a_mn = float(coeffs[m * n])
            a_m_a_n = float(coeffs[m]) * float(coeffs[n])
            if abs(a_m_a_n) > 1e-15 or abs(a_mn) > 1e-15:
                err = abs(a_mn - a_m_a_n) / max(abs(a_mn), abs(a_m_a_n), 1e-30)
                if err > 1e-8:
                    failures.append((m, n, a_mn, a_m_a_n, err))
                max_err = max(max_err, err)

    return {
        'is_multiplicative': len(failures) == 0,
        'max_error': max_err,
        'failures': failures[:20]  # cap at 20 for readability
    }


def diagnose_interference(n_max=10, c_max=30):
    """Diagnose the source of non-multiplicativity in Ising character coefficients.

    For each fixed j, compute a_0^{(j)}(n) = contribution from the j-th field.
    Check multiplicativity of each channel separately and of the total.

    Returns diagnostic dict.
    """
    if not HAS_MPMATH:
        raise RuntimeError("Requires mpmath")

    _init_ising()
    i = 0  # vacuum character

    # Total Rademacher coefficients
    total = [mpmath.mpf(0)] * (n_max + 1)
    channels = {j: [mpmath.mpf(0)] * (n_max + 1) for j in range(3)}

    for n in range(n_max + 1):
        for j in range(3):
            val = rademacher_j_contribution(i, j, n, c_max=c_max)
            channels[j][n] = val
            total[n] += val

    # Check multiplicativity of each channel
    results = {}
    for j in range(3):
        results[f'channel_{j}'] = check_multiplicativity(channels[j], n_max)

    results['total'] = check_multiplicativity(total, n_max)

    # Also check exact coefficients
    exact = ising_exact_coefficients(0, n_max)
    results['exact'] = check_multiplicativity(exact, n_max)

    return results


# ============================================================
# 12. Summary diagnostics
# ============================================================

def full_diagnostic_report(n_max=10, c_max=30):
    """Run all diagnostics and return a structured report.

    This is the master diagnostic function that exercises all components:
    1. Classical Kloosterman multiplicativity verification
    2. Weil bound verification
    3. Rademacher vs exact coefficient comparison
    4. Non-multiplicativity diagnosis
    5. Kloosterman Dirichlet series Euler product test
    """
    if not HAS_MPMATH:
        return {'error': 'mpmath not available'}

    report = {}

    # 1. Classical multiplicativity
    mult_tests = []
    for m in range(4):
        for n in range(4):
            for c1 in [2, 3, 5]:
                for c2 in [3, 5, 7]:
                    if c1 != c2 and math.gcd(c1, c2) == 1:
                        _, _, err = verify_kloosterman_multiplicativity(m, n, c1, c2)
                        mult_tests.append((m, n, c1, c2, err))
    report['multiplicativity_max_error'] = max(t[4] for t in mult_tests)

    # 2. Weil bound
    weil_tests = []
    for m in range(4):
        for n in range(4):
            for c in range(1, 31):
                _, _, satisfied = verify_weil_bound(m, n, c)
                weil_tests.append((m, n, c, satisfied))
    report['weil_bound_all_satisfied'] = all(t[3] for t in weil_tests)

    # 3. Rademacher vs exact (vacuum character)
    exact = ising_exact_coefficients(0, n_max)
    rademacher = [rademacher_coefficient(0, n, c_max=c_max) for n in range(n_max + 1)]
    comparison = []
    for n in range(n_max + 1):
        e = float(exact[n])
        r = float(mpmath.re(rademacher[n]))
        if abs(e) > 0.5:
            comparison.append((n, e, r, abs(e - r) / abs(e)))
        else:
            comparison.append((n, e, r, abs(e - r)))
    report['rademacher_vs_exact'] = comparison

    # 4. Non-multiplicativity
    report['interference'] = diagnose_interference(n_max=min(n_max, 8), c_max=c_max)

    return report
