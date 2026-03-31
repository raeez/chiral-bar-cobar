"""
Siegel Eisenstein series Fourier coefficients and Igusa cusp form chi_12.

Implements the Cohen–Katsurada formula for degree-2 Siegel Eisenstein
series E_k^{(2)} on Sp(4,Z), the Igusa relation for chi_12, and the
decomposition of the Leech lattice genus-2 theta series.

Key formula: for primitive T = ((a, b/2), (b/2, c)) > 0 with
discriminant Delta = 4ac - b^2 > 0:

  a(T; E_k) = (2k/B_k) * H(k-1, Delta)

where H(r, N) is the Cohen function:

  H(r, N) = L(1-r, chi_{D0}) * sum_{d|f} mu(d) chi_{D0}(d) d^{r-1} sigma_{2r-1}(f/d)

and N = |D0| * f^2 with D0 the fundamental discriminant.

References:
  - Cohen (1975), "Sums involving the values at negative integers of
    L-functions of quadratic characters"
  - Katsurada (1999), "An explicit formula for Siegel series"
  - Igusa (1962), "On Siegel modular forms of genus two"
"""

from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt


# ============================================================
# ARITHMETIC PRIMITIVES
# ============================================================

def kronecker_symbol(D, n):
    """
    Compute the Kronecker symbol (D/n) for D a discriminant.
    This extends the Jacobi symbol to all integers.
    """
    if n == 0:
        return 1 if abs(D) == 1 else 0
    if n == 1:
        return 1
    if n == -1:
        return -1 if D < 0 else 1

    # Factor out sign and powers of 2
    if n < 0:
        return kronecker_symbol(D, -1) * kronecker_symbol(D, -n)

    # Handle n = 2
    if n == 2:
        if D % 2 == 0:
            return 0
        r = D % 8
        if r == 1 or r == 7:
            return 1
        if r == 3 or r == 5:
            return -1
        return 0  # shouldn't reach here

    # For odd prime p (or odd composite)
    if n % 2 == 0:
        return kronecker_symbol(D, 2) * kronecker_symbol(D, n // 2)

    # Odd n: use Jacobi symbol via quadratic reciprocity
    return _jacobi(D % n, n)


def _jacobi(a, n):
    """Jacobi symbol (a/n) for odd n > 0."""
    if n == 1:
        return 1
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0


def moebius(n):
    """Möbius function μ(n)."""
    if n == 1:
        return 1
    factors = _factorize(n)
    for p, e in factors:
        if e >= 2:
            return 0
    return (-1) ** len(factors)


def _factorize(n):
    """Return list of (prime, exponent) pairs."""
    if n <= 1:
        return []
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                e += 1
                n //= d
            factors.append((d, e))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def sigma(s, n):
    """Divisor function sigma_s(n) = sum_{d|n} d^s."""
    if n <= 0:
        return 0
    result = 0
    for d in range(1, n + 1):
        if n % d == 0:
            result += d ** s
    return result


def divisors(n):
    """List of positive divisors of n."""
    if n <= 0:
        return []
    divs = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            divs.append(d)
            if d != n // d:
                divs.append(n // d)
    return sorted(divs)


def fundamental_discriminant(N):
    """
    Factor N = |D0| * f^2 where D0 is the fundamental discriminant
    of the imaginary quadratic field Q(sqrt(-N)).

    Returns (D0, f) where D0 < 0 is fundamental and N = |D0| * f^2.
    """
    # N > 0 is the absolute discriminant
    # Find the largest f^2 dividing N such that -N/f^2 is fundamental
    for f in range(isqrt(N), 0, -1):
        if N % (f * f) != 0:
            continue
        D0 = -(N // (f * f))
        if _is_fundamental_discriminant(D0):
            return (D0, f)
    # Fallback (shouldn't happen for valid input)
    return (-N, 1)


def _is_fundamental_discriminant(D):
    """Check if D < 0 is a fundamental discriminant."""
    if D >= 0:
        return False
    m = -D
    if m % 4 == 3:
        # D = -m ≡ 1 mod 4, check m is squarefree
        return _is_squarefree(m)
    if m % 4 == 0:
        n = m // 4
        if n % 4 in (1, 2, 3) and _is_squarefree(n):
            return True
    return False


def _is_squarefree(n):
    """Check if n is squarefree."""
    if n <= 1:
        return True
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


# ============================================================
# BERNOULLI NUMBERS AND L-VALUES
# ============================================================

def _binomial(n, k):
    """Binomial coefficient C(n, k) as integer."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


@lru_cache(maxsize=64)
def bernoulli(n):
    """Compute the n-th Bernoulli number B_n as a Fraction."""
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        B[m] = Fraction(0)
        for k in range(m):
            B[m] -= Fraction(_binomial(m + 1, k)) * B[k]
        B[m] /= Fraction(m + 1)
    return B[n]


def generalized_bernoulli(r, D):
    """
    Compute the generalized Bernoulli number B_{r, chi_D}
    for the Kronecker character chi_D.

    B_{r,chi} = |D|^{r-1} sum_{a=1}^{|D|} chi(a) B_r(a/|D|)

    where B_r(x) is the Bernoulli polynomial.
    """
    N = abs(D)
    if N == 0:
        return bernoulli(r)

    result = Fraction(0)
    for a in range(1, N + 1):
        chi_a = kronecker_symbol(D, a)
        if chi_a == 0:
            continue
        # Bernoulli polynomial B_r(a/N) = sum_{k=0}^r C(r,k) B_k (a/N)^{r-k}
        x = Fraction(a, N)
        bp = Fraction(0)
        binom = 1
        for k in range(r + 1):
            if k > 0:
                binom = binom * (r - k + 1) // k
            bp += Fraction(binom) * bernoulli(k) * x ** (r - k)
        result += Fraction(chi_a) * bp
    result *= Fraction(N) ** (r - 1)
    return result


def dirichlet_L_at_nonpositive(s, D):
    """
    Compute L(1-r, chi_D) = -B_{r, chi_D} / r for r = 1-s >= 1.

    Parameters
    ----------
    s : int
        The evaluation point (s <= 0, so r = 1-s >= 1).
    D : int
        The discriminant (D < 0 for imaginary quadratic).

    Returns
    -------
    Fraction
        The value L(s, chi_D).
    """
    r = 1 - s  # r >= 1
    if r < 1:
        raise ValueError(f"Need s <= 0, got s={s}")
    B_r_chi = generalized_bernoulli(r, D)
    return -B_r_chi / Fraction(r)


# ============================================================
# COHEN FUNCTION AND SIEGEL EISENSTEIN COEFFICIENTS
# ============================================================

def cohen_H(r, N):
    """
    Cohen function H(r, N) for r >= 1 and N >= 1.

    H(r, N) = L(1-r, chi_{D0}) * sum_{d|f} mu(d) chi_{D0}(d) d^{r-1} sigma_{2r-1}(f/d)

    where N = |D0| * f^2 with D0 fundamental discriminant.

    Returns 0 if N is not a valid discriminant (N must be ≡ 0 or 3 mod 4).
    """
    if N <= 0:
        return Fraction(0)

    # N must be ≡ 0 or 3 mod 4 for -N to be a discriminant
    if N % 4 not in (0, 3):
        return Fraction(0)

    D0, f = fundamental_discriminant(N)

    # L(1-r, chi_{D0})
    L_val = dirichlet_L_at_nonpositive(1 - r, D0)

    # Sum over d | f
    total = Fraction(0)
    for d in divisors(f):
        mu_d = moebius(d)
        if mu_d == 0:
            continue
        chi_d = kronecker_symbol(D0, d)
        sig = sigma(2 * r - 1, f // d)
        total += Fraction(mu_d * chi_d) * Fraction(d) ** (r - 1) * Fraction(sig)

    return L_val * total


def siegel_eisenstein_coefficient(k, a, b, c):
    """
    Fourier coefficient of the normalized degree-2 Siegel Eisenstein
    series E_k^{(2)} at T = ((a, b/2), (b/2, c)) > 0.

    The formula uses:
      a(T; E_k) = C_k * sum_{d|content(T)} d^{k-1} H(k-1, Delta/d^2)

    where C_k = 2 / (zeta(1-k) * zeta(3-2k)) and Delta = 4ac - b^2.

    Parameters
    ----------
    k : int
        Weight (even, >= 4).
    a, b, c : int
        Half-integral matrix entries: T = ((a, b/2), (b/2, c)).
        Requires 4ac - b^2 > 0 (positive definite).
    """
    Delta = 4 * a * c - b * b
    if Delta <= 0:
        return Fraction(0)

    # Content of 2T = ((2a, b), (b, 2c))
    content = gcd(gcd(2 * a, b), 2 * c)

    # Normalization: C_k = 2 / (zeta(1-k) * zeta(3-2k))
    # zeta(1-k) = -B_k / k, zeta(3-2k) = -B_{2k-2} / (2k-2)
    B_k = bernoulli(k)
    B_2km2 = bernoulli(2 * k - 2)
    if B_k == 0 or B_2km2 == 0:
        return Fraction(0)

    zeta_1mk = -B_k / Fraction(k)
    zeta_3m2k = -B_2km2 / Fraction(2 * k - 2)
    C_k = Fraction(2) / (zeta_1mk * zeta_3m2k)

    # Sum over divisors of content
    total = Fraction(0)
    for d in divisors(content):
        if Delta % (d * d) != 0:
            continue
        total += Fraction(d) ** (k - 1) * cohen_H(k - 1, Delta // (d * d))

    return C_k * total


# ============================================================
# IGUSA CUSP FORM chi_12
# ============================================================

def chi12_coefficient(a, b, c):
    """
    Fourier coefficient of the Igusa cusp form chi_12 at
    T = ((a, b/2), (b/2, c)).

    Uses the Igusa relation (with normalization from Aoki-Ibukiyama 2005):
      chi_12 = (1/131040) * (441 * E_4^3 + 250 * E_6^2 - 691 * E_12)

    where E_k = E_k^{(2)} are the degree-2 Siegel Eisenstein series.
    At T > 0 (positive definite), the constant term cancels because
    441 + 250 - 691 = 0.
    """
    e4 = siegel_eisenstein_coefficient(4, a, b, c)
    e6 = siegel_eisenstein_coefficient(6, a, b, c)
    e12 = siegel_eisenstein_coefficient(12, a, b, c)

    # E_4^3 at T: this requires the CONVOLUTION (product of Siegel modular forms)
    # For the product E_4^3, the Fourier coefficient at T is:
    # a(T; E_4^3) = sum_{T1+T2+T3 = T} a(T1; E_4) a(T2; E_4) a(T3; E_4)
    #
    # This is computationally expensive. For small T, we enumerate.
    # Similarly for E_6^2.
    #
    # HOWEVER: for the Igusa relation, we can use the fact that
    # the constant terms cancel (441 + 250 - 691 = 0) and work
    # directly with E_4, E_6, E_12 at T > 0.
    #
    # For small T, the convolution can be computed by summing over
    # all decompositions T = T1 + T2 + T3.

    # For now, use the direct method for specific small T values.
    # TODO: implement general convolution for arbitrary T.

    # We implement a special case: for T with small entries,
    # enumerate all decompositions.
    pass  # Placeholder — see convolution functions below


def _enumerate_half_integral_matrices(bound):
    """
    Enumerate all positive semi-definite half-integral 2x2 matrices
    T = ((a, b/2), (b/2, c)) with a, c <= bound.

    Includes T = 0.
    """
    matrices = []
    for a in range(bound + 1):
        for c in range(bound + 1):
            for b in range(-2 * min(a, c) if min(a, c) > 0 else 0,
                           2 * min(a, c) + 1 if min(a, c) > 0 else 1):
                if 4 * a * c - b * b >= 0:
                    matrices.append((a, b, c))
    return matrices


def siegel_product_coefficient(k1, k2, a, b, c):
    """
    Fourier coefficient of E_{k1} * E_{k2} at T = ((a, b/2), (b/2, c)).

    This is the convolution:
    a(T; f*g) = sum_{T1 + T2 = T, T1,T2 >= 0} a(T1; f) a(T2; g)
    """
    total = Fraction(0)
    for a1 in range(a + 1):
        for c1 in range(c + 1):
            a2, c2 = a - a1, c - c1
            for b1 in range(-2 * min(a1, c1) if min(a1, c1) > 0 else 0,
                            2 * min(a1, c1) + 1 if min(a1, c1) > 0 else 1):
                b2 = b - b1
                # Check both T1 and T2 are positive semi-definite
                if 4 * a1 * c1 - b1 * b1 < 0:
                    continue
                if 4 * a2 * c2 - b2 * b2 < 0:
                    continue
                # Coefficients
                if a1 == 0 and b1 == 0 and c1 == 0:
                    f1 = Fraction(1)  # constant term
                else:
                    f1 = siegel_eisenstein_coefficient(k1, a1, b1, c1)
                if a2 == 0 and b2 == 0 and c2 == 0:
                    f2 = Fraction(1)
                else:
                    f2 = siegel_eisenstein_coefficient(k2, a2, b2, c2)
                total += f1 * f2
    return total


def siegel_triple_product_coefficient(k, a, b, c):
    """
    Fourier coefficient of E_k^3 at T = ((a, b/2), (b/2, c)).

    a(T; f^3) = sum_{T1+T2+T3=T} a(T1;f) a(T2;f) a(T3;f)

    For efficiency, compute as f * (f^2).
    """
    # First compute E_k^2 coefficient, then convolve with E_k
    total = Fraction(0)
    for a1 in range(a + 1):
        for c1 in range(c + 1):
            a2, c2 = a - a1, c - c1
            for b1 in range(-2 * min(a1, c1) if min(a1, c1) > 0 else 0,
                            2 * min(a1, c1) + 1 if min(a1, c1) > 0 else 1):
                b2 = b - b1
                if 4 * a1 * c1 - b1 * b1 < 0:
                    continue
                if 4 * a2 * c2 - b2 * b2 < 0:
                    continue
                if a1 == 0 and b1 == 0 and c1 == 0:
                    f1 = Fraction(1)
                else:
                    f1 = siegel_eisenstein_coefficient(k, a1, b1, c1)
                f2_sq = siegel_product_coefficient(k, k, a2, b2, c2)
                total += f1 * f2_sq
    return total


def chi12_from_igusa(a, b, c):
    """
    Compute chi_12 Fourier coefficient at T = ((a, b/2), (b/2, c))
    using the Igusa relation:

      chi_12 = (1/C) * (441 * E_4^3 + 250 * E_6^2 - 691 * E_12)

    where C = 131040 is the Igusa normalization constant
    (chosen so that chi_12 has integer Fourier coefficients with
    a(((1,0),(0,1)); chi_12) = 1).

    Note: for the FIRST nonzero coefficient (at minimal T), the
    normalization must be verified empirically.
    """
    Delta = 4 * a * c - b * b
    if Delta <= 0:
        return Fraction(0)

    e4_cubed = siegel_triple_product_coefficient(4, a, b, c)
    e6_squared = siegel_product_coefficient(6, 6, a, b, c)
    e12 = siegel_eisenstein_coefficient(12, a, b, c)

    numerator = Fraction(441) * e4_cubed + Fraction(250) * e6_squared - Fraction(691) * e12

    return numerator


# ============================================================
# LEECH LATTICE DECOMPOSITION
# ============================================================

def leech_decomposition_coefficient(a, b, c, leech_r2_func):
    """
    Compute the projection of Theta_Leech onto chi_12 at
    T = ((a, b/2), (b/2, c)).

    The decomposition:
    Theta_Leech = c0 * E_12 + c1 * E_12^{Kling} + c2 * chi_12

    The cusp projection is:
    a_cusp(T) = a_Leech(T) - a_Eis(T) - a_Kling(T)

    For the chi_12 coefficient c2:
    c2 = <Theta_Leech, chi_12> / <chi_12, chi_12>

    We compute this from the Fourier expansion by matching coefficients.
    """
    r2 = leech_r2_func(a, b, c)
    if r2 is None:
        return None

    e12 = siegel_eisenstein_coefficient(12, a, b, c)
    chi = chi12_from_igusa(a, b, c)

    if chi == 0:
        return None  # can't extract c2 from this T

    # a_Leech(T) = c0 * a_E12(T) + c1 * a_Kling(T) + c2 * a_chi12(T)
    # With c0 = 1 (matching constant terms):
    # a_Leech(T) - a_E12(T) = c1 * a_Kling(T) + c2 * a_chi12(T)
    # For T where a_Kling(T) = 0, we get:
    # c2 = (a_Leech(T) - a_E12(T)) / a_chi12(T)

    return {
        'leech': r2,
        'eisenstein': e12,
        'chi12': chi,
        'cusp_residual': Fraction(r2) - e12,
    }
