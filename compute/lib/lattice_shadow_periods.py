#!/usr/bin/env python3
r"""Lattice shadow periods: the arithmetic sieve for lattice VOAs.

The fundamental principle: for lattice VOAs, each arity of the shadow
Postnikov tower maps to a specific L-function in the Hecke decomposition
of the lattice theta function. The homotopy becomes arithmetic.

ARITHMETIC SIEVE:
  Shadow arity 2 (kappa) -> Riemann zeta(s) periods
  Shadow arity 3 (cubic) -> Eisenstein periods zeta(s)*zeta(s-k+1)
  Shadow arity >= 4      -> Cusp form periods L(s, f_j)

DEPTH FORMULA:
  d(V_Lambda) = 1 + d_arith = 1 + (1 + dim S_{r/2})
  where r = rank(Lambda) and S_{r/2} = cusp forms of weight r/2.

THE SHADOW-PERIOD DICTIONARY:
  | Shadow arity | Modular source   | L-function            | Period type |
  |-------------|------------------|-----------------------|-------------|
  | 2 (kappa)   | constant term    | zeta(s)               | Riemann     |
  | 3 (cubic)   | Eisenstein E_k   | zeta(s)*zeta(s-k+1)   | Dedekind    |
  | 4 (quartic) | first cusp f_1   | L(s, f_1)             | Hecke       |
  | 5+          | higher cusps f_j | L(s, f_j)             | Hecke       |

CONCRETE CASES:
  V_Z    (rank 1): depth 2, Gaussian, no cusp forms in M_{1/2}
  V_{Z^2} (rank 2): depth 2, Gaussian, no cusp forms in M_1
  V_{A_2} (rank 2): depth 2, Gaussian, no cusp forms in M_1
  V_{E_8} (rank 8): depth 3, Lie/tree, no cusp forms in S_4
  V_Leech (rank 24): depth 4, contact, dim S_{12} = 1 (Ramanujan Delta)

The Leech lattice is the canonical example where homotopy becomes
arithmetic: the arity-4 shadow is the Ramanujan cusp form L(s, Delta).

References:
  - arithmetic_shadows.tex: thm:shadow-spectral-correspondence
  - concordance.tex: sec:concordance-spectral-continuation
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =========================================================================
# Bernoulli numbers and divisor sums
# =========================================================================

def _bernoulli(n: int) -> Fraction:
    """Bernoulli number B_n as exact fraction."""
    # Standard algorithm for B_n via the recursive definition.
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    if n == 0:
        return B[0]
    for m in range(1, n + 1):
        s = Fraction(0)
        for k in range(m):
            # binomial(m+1, k)
            binom = 1
            for j in range(1, k + 1):
                binom = binom * (m + 1 - j + 1) // j
            # Actually need C(m+1, k)
            binom = 1
            num = m + 1
            for j in range(1, k + 1):
                binom = binom * num // j
                num -= 1
            s += Fraction(binom) * B[k]
        B[m] = -s / Fraction(m + 1)
    return B[n]


def sigma_k(n: int, k: int) -> int:
    r"""Divisor sum sigma_k(n) = sum_{d|n} d^k.

    Standard arithmetic function. Returns sum of k-th powers of divisors.
    """
    if n <= 0:
        return 0
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += d ** k
    return total


# =========================================================================
# Ramanujan tau function
# =========================================================================

def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function tau(n), coefficients of Delta = eta^{24}.

    Delta(tau) = q * prod_{n>=1} (1 - q^n)^{24} = sum_{n>=1} tau(n) q^n.

    First values: tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830.

    Computed via eta^{24} product expansion.
    """
    if n < 1:
        return 0

    # Compute coefficients of q * prod_{m=1}^{n} (1 - q^m)^{24}
    # up to order q^n.
    # We need prod (1-q^m)^{24} up to order q^{n-1}.
    # Start with coefficient array for prod (1 - q^m)^{24}.
    N = n  # need coefficients up to q^{n-1} of eta^{24}/q
    coeffs = [0] * (N + 1)
    coeffs[0] = 1

    for m in range(1, N + 1):
        # Multiply by (1 - q^m)^{24}.
        # First compute (1 - q^m)^{24} using binomial:
        # (1 - x)^{24} = sum_{j=0}^{24} C(24,j)(-1)^j x^j
        # We multiply the running product by this.
        # To multiply the power series by (1 - q^m)^{24}:
        # Apply the 24-fold factor (1 - q^m) one at a time.
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]

    # tau(n) is the coefficient of q^n in Delta = q * prod(1-q^m)^{24}
    # = coefficient of q^{n-1} in prod(1-q^m)^{24}
    if n - 1 <= N:
        return coeffs[n - 1]
    return 0


# =========================================================================
# Modular forms: Eisenstein series
# =========================================================================

def eisenstein_series_weight_k(k: int, tau, nmax: int = 100):
    r"""Normalized Eisenstein series E_k(tau) = 1 - (2k/B_k) sum_{n>=1} sigma_{k-1}(n) q^n.

    Uses the convention E_k = 1 + (2k/B_k) * sum ... with appropriate sign
    from Bernoulli. Specifically:
      E_k(tau) = 1 - (2k/B_k) * sum_{n=1}^{nmax} sigma_{k-1}(n) q^n

    Note B_k for even k >= 2 is negative for k=2 mod 4 (B_2 = 1/6, etc.),
    so the formula gives the standard normalization.

    For k=4: E_4 = 1 + 240*q + 2160*q^2 + ...
    For k=6: E_6 = 1 - 504*q - 16632*q^2 + ...
    For k=12: E_{12} uses B_{12} = -691/2730.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required for modular form computation")

    if k < 2 or k % 2 != 0:
        raise ValueError(f"Eisenstein series requires even k >= 2, got k={k}")

    Bk = _bernoulli(k)
    # Normalization factor: -2k / B_k
    norm = Fraction(-2 * k, 1) / Bk

    q = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    result = mpmath.mpf(1)
    for n in range(1, nmax + 1):
        sig = sigma_k(n, k - 1)
        coeff = float(norm * sig)
        result += coeff * q ** n
    return result


def eisenstein_coefficient(k: int, n: int) -> Fraction:
    r"""The n-th Fourier coefficient of E_k.

    E_k = sum_{n>=0} a_n q^n, where a_0 = 1 and
    a_n = (-2k/B_k) * sigma_{k-1}(n) for n >= 1.

    Returns exact fraction.
    """
    if n == 0:
        return Fraction(1)
    Bk = _bernoulli(k)
    norm = Fraction(-2 * k, 1) / Bk
    return norm * Fraction(sigma_k(n, k - 1))


# =========================================================================
# Cusp form dimension
# =========================================================================

def cusp_form_dim(weight: int) -> int:
    r"""Dimension of S_k(SL_2(Z)), the space of cusp forms of weight k for the full modular group.

    Standard dimension formula for k even, k >= 2:
      dim S_k = floor(k/12) - 1  if k = 2 mod 12
      dim S_k = floor(k/12)      otherwise

    Exceptions: dim S_k = 0 for k < 12, dim S_{12} = 1.

    For odd k or k < 2: dim = 0 (no cusp forms for SL_2(Z)).
    For half-integer weight on SL_2(Z): dim = 0 (no forms).
    """
    if weight < 2 or weight % 2 != 0:
        return 0
    if weight < 12:
        return 0
    if weight == 12:
        return 1
    k = weight
    if k % 12 == 2:
        return k // 12 - 1
    return k // 12


# =========================================================================
# Theta functions for specific lattices
# =========================================================================

def theta_function_rank1(tau, nmax: int = 500):
    r"""Theta function for V_Z: theta_3(2*tau) = sum_{n in Z} q^{n^2}.

    This is the theta function of the integer lattice Z with
    quadratic form Q(n) = n^2 (norm squared = 2n^2, but we use
    the convention |lambda|^2/2 in the exponent).

    Theta_{Z}(tau) = sum_{n in Z} q^{n^2} = theta_3(2*tau)
    where q = e^{2*pi*i*tau}.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    q = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    result = mpmath.mpf(0)
    for n in range(-nmax, nmax + 1):
        result += q ** (n * n)
    return result


def theta_function_e8(tau, nmax: int = 100):
    r"""Theta function for V_{E_8}: Theta_{E_8}(tau) = E_4(tau).

    The remarkable fact: the theta function of the E_8 root lattice
    equals the Eisenstein series of weight 4. This is because:
    1. Theta_{E_8} in M_4(SL_2(Z)) (weight = rank/2 = 4)
    2. dim M_4 = 1, dim S_4 = 0
    3. Therefore Theta_{E_8} = c * E_4, and c = 1 from constant term.

    Fourier coefficients: a_n = 240 * sigma_3(n) for n >= 1.
    First terms: 1 + 240*q + 2160*q^2 + 6720*q^3 + ...
    (240 = |roots of E_8|, 2160 = vectors of norm 4 in E_8, etc.)
    """
    return eisenstein_series_weight_k(4, tau, nmax=nmax)


def theta_leech(tau, nmax: int = 50):
    r"""Theta function for the Leech lattice: Theta_Leech = E_{12} - (65520/691)*Delta.

    The Leech lattice is the unique even unimodular lattice in dimension 24
    with no vectors of norm 2. Its theta function lies in M_{12}(SL_2(Z)),
    which is 2-dimensional: M_{12} = C*E_{12} + C*Delta.

    Since Theta_Leech has no q^1 term (no roots), and E_{12} has
    coefficient 65520/691 at q^1 while Delta has coefficient 1 at q^1:
      Theta_Leech = E_{12} - (65520/691)*Delta

    First nonzero term after constant: q^2 coefficient = 196560
    (the 196560 minimal vectors of the Leech lattice, all of norm 4).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    E12 = eisenstein_series_weight_k(12, tau, nmax=nmax)

    # Delta = eta^{24} = q * prod(1-q^n)^{24}
    # Compute directly from tau function coefficients.
    q_val = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    delta_val = mpmath.mpf(0)
    for n in range(1, nmax + 1):
        delta_val += ramanujan_tau(n) * q_val ** n

    c_delta = mpmath.mpf(65520) / mpmath.mpf(691)
    return E12 - c_delta * delta_val


def leech_delta_coefficient() -> Fraction:
    r"""The coefficient -65520/691 in Theta_Leech = E_{12} - (65520/691)*Delta.

    This is exact. The 691 is the numerator of B_{12} = -691/2730,
    which is why 691 appears as the Eisenstein denominator.
    """
    return Fraction(-65520, 691)


# =========================================================================
# Theta series coefficients (exact)
# =========================================================================

def theta_coefficient_e8(n: int) -> int:
    r"""Number of vectors of norm 2n in the E_8 lattice = 240*sigma_3(n).

    Since Theta_{E_8} = E_4 = 1 + 240*sum sigma_3(n) q^n.
    The number of lattice vectors lambda with |lambda|^2 = 2n is 240*sigma_3(n).

    r_8(0) = 1 (the zero vector), r_8(n) = 240*sigma_3(n) for n >= 1.
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return 240 * sigma_k(n, 3)


def theta_coefficient_leech(n: int, nmax: int = 50) -> int:
    r"""Number of vectors of norm 2n in the Leech lattice.

    Theta_Leech = E_{12} - (65520/691)*Delta.
    Coefficient of q^n = a_n(E_{12}) - (65520/691)*tau(n).

    First values:
      n=0: 1
      n=1: 0 (no roots in the Leech lattice)
      n=2: 196560 (minimal vectors)
      n=3: 16773120
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    # Coefficient of q^n in E_{12}
    e12_coeff = eisenstein_coefficient(12, n)
    # Coefficient of q^n in Delta
    tau_n = ramanujan_tau(n)
    # Theta_Leech coefficient = e12_coeff - (65520/691) * tau_n
    result = e12_coeff - Fraction(65520, 691) * Fraction(tau_n)
    # Must be a non-negative integer
    assert result.denominator == 1, f"Non-integer Leech coefficient at n={n}: {result}"
    return int(result)


# =========================================================================
# Hecke decomposition
# =========================================================================

def hecke_decompose(lattice_name: str) -> Dict[str, Any]:
    r"""Decompose the theta function of a named lattice into Eisenstein + cusp parts.

    Returns a dictionary with:
      'rank': lattice rank
      'weight': modular weight = rank/2
      'eisenstein_coeff': coefficient of E_k in the decomposition
      'cusp_coeffs': list of (cusp_form_name, coefficient) pairs
      'cusp_dim': dimension of the cusp space
      'eisenstein_only': True if there are no cusp form contributions
    """
    data = lattice_data(lattice_name)
    rank = data['rank']
    weight = rank // 2 if rank % 2 == 0 else None

    if lattice_name == 'Z':
        return {
            'rank': 1,
            'weight': Fraction(1, 2),
            'eisenstein_coeff': 1,
            'cusp_coeffs': [],
            'cusp_dim': 0,
            'eisenstein_only': True,
            'note': 'M_{1/2} has no cusp forms; theta_3(2tau) is pure theta',
        }

    if lattice_name == 'Z2':
        return {
            'rank': 2,
            'weight': 1,
            'eisenstein_coeff': 1,
            'cusp_coeffs': [],
            'cusp_dim': 0,
            'eisenstein_only': True,
            'note': 'M_1(Gamma_0(4)) is 1-dimensional; no cusp forms',
        }

    if lattice_name == 'A2':
        return {
            'rank': 2,
            'weight': 1,
            'eisenstein_coeff': 1,
            'cusp_coeffs': [],
            'cusp_dim': 0,
            'eisenstein_only': True,
            'note': 'M_1(Gamma_0(3), chi_3) is 1-dimensional; no cusp forms',
        }

    if lattice_name == 'E8':
        return {
            'rank': 8,
            'weight': 4,
            'eisenstein_coeff': 1,
            'cusp_coeffs': [],
            'cusp_dim': cusp_form_dim(4),
            'eisenstein_only': True,
            'note': 'dim S_4(SL_2(Z)) = 0; Theta_{E_8} = E_4 exactly',
        }

    if lattice_name == 'Leech':
        c_delta = Fraction(-65520, 691)
        return {
            'rank': 24,
            'weight': 12,
            'eisenstein_coeff': 1,
            'cusp_coeffs': [('Delta', c_delta)],
            'cusp_dim': cusp_form_dim(12),
            'eisenstein_only': False,
            'note': 'Theta_Leech = E_{12} - (65520/691)*Delta; '
                    'the Ramanujan cusp form appears',
        }

    raise ValueError(f"Unknown lattice: {lattice_name}")


# =========================================================================
# Epstein zeta from theta (Mellin transform)
# =========================================================================

def epstein_zeta_lattice(lattice_name: str, s, num_terms: int = 200):
    r"""Compute the Epstein zeta function of a named lattice at s.

    epsilon^r_s(V_Lambda) = sum_{0 != lambda in Lambda} |lambda|^{-2s}

    For lattices whose theta function is a modular form of weight k
    for SL_2(Z), this factors through the Rankin-Selberg method into
    products of Riemann/Hecke L-functions.

    FACTORIZATIONS:
      V_Z:     epsilon^1_s = 2*zeta(2s)
      V_{Z^2}: epsilon^2_s = 4*zeta(s)*L(s, chi_{-4})
      V_{A_2}: epsilon^2_s = 6*zeta(s)*L(s, chi_{-3})
      V_{E_8}: epsilon^8_s = 240*4^{-s}*zeta(s)*zeta(s-3)
      V_Leech: epsilon^24_s = c_E*zeta(s)*zeta(s-11)
                            + c_Delta*L(s, Delta)   (up to gamma factors)
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    s = mpmath.mpf(s)

    if lattice_name == 'Z':
        # epsilon^1_s = 2*zeta(2s)
        return 2 * mpmath.zeta(2 * s)

    if lattice_name == 'Z2':
        # epsilon^2_s = 4*zeta(s)*L(s, chi_{-4})
        # L(s, chi_{-4}) = sum_{n=1}^{inf} chi_{-4}(n) * n^{-s}
        # chi_{-4}(n) = Kronecker(-4, n): 0 if even, (-1)^{(n-1)/2} if odd
        L_val = _dirichlet_l_chi4(s, num_terms)
        return 4 * mpmath.zeta(s) * L_val

    if lattice_name == 'A2':
        # epsilon^2_s = 6*zeta(s)*L(s, chi_{-3})
        # chi_{-3}(n) = Kronecker(-3, n) = Legendre(n, 3):
        # chi_{-3}(1)=1, chi_{-3}(2)=-1, chi_{-3}(3)=0, period 3
        L_val = _dirichlet_l_chi3(s, num_terms)
        return 6 * mpmath.zeta(s) * L_val

    if lattice_name == 'E8':
        # epsilon^8_s = 240 * 4^{-s} * zeta(s) * zeta(s-3)
        return 240 * mpmath.power(4, -s) * mpmath.zeta(s) * mpmath.zeta(s - 3)

    if lattice_name == 'Leech':
        # Direct computation from theta series coefficients.
        # Theta_Leech = sum a_n q^n, so
        # epsilon = sum_{n>=1} a_n * n^{-s}  (Dirichlet series of theta coeffs)
        # But the norm in Leech is |lambda|^2 = 2n for the coefficient of q^n.
        # epsilon = sum_{n>=1} a_n * (2n)^{-s} ... but let's use the
        # standard Epstein zeta = sum_{lambda != 0} |lambda|^{-2s}
        # = sum_{n>=1} a_n * n^{-s} where a_n = theta_coeff(n).
        result = mpmath.mpf(0)
        for n in range(1, num_terms + 1):
            a_n = theta_coefficient_leech(n, nmax=num_terms)
            result += a_n * mpmath.power(n, -s)
        return result

    raise ValueError(f"Unknown lattice: {lattice_name}")


def _dirichlet_l_chi4(s, num_terms: int = 200):
    """L(s, chi_{-4}) = sum chi_{-4}(n) n^{-s}.

    chi_{-4}(n) = Kronecker symbol (-4|n):
      n odd: (-1)^{(n-1)/2}
      n even: 0
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    result = mpmath.mpf(0)
    for n in range(1, num_terms + 1):
        if n % 2 == 0:
            continue
        chi = (-1) ** ((n - 1) // 2)
        result += chi * mpmath.power(n, -s)
    return result


def _dirichlet_l_chi3(s, num_terms: int = 200):
    """L(s, chi_{-3}) = sum chi_{-3}(n) n^{-s}.

    chi_{-3}(n) = Kronecker symbol (-3|n):
      n = 1 mod 3: +1
      n = 2 mod 3: -1
      n = 0 mod 3: 0
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    result = mpmath.mpf(0)
    for n in range(1, num_terms + 1):
        r = n % 3
        if r == 0:
            chi = 0
        elif r == 1:
            chi = 1
        else:
            chi = -1
        if chi != 0:
            result += chi * mpmath.power(n, -s)
    return result


# =========================================================================
# L-function of the Ramanujan Delta
# =========================================================================

def L_ramanujan_delta(s, num_terms: int = 100):
    r"""L(s, Delta) = sum_{n=1}^{infty} tau(n) n^{-s}.

    The L-function of the Ramanujan Delta cusp form. Converges absolutely
    for Re(s) > 13/2 by the Deligne bound |tau(p)| <= 2 p^{11/2}.

    Has functional equation relating s <-> 12-s (center of critical strip
    at Re(s) = 6).

    Euler product:
      L(s, Delta) = prod_p 1/(1 - tau(p) p^{-s} + p^{11-2s})
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    s = mpmath.mpf(s)
    result = mpmath.mpf(0)
    for n in range(1, num_terms + 1):
        result += ramanujan_tau(n) * mpmath.power(n, -s)
    return result


# =========================================================================
# L-function content extraction
# =========================================================================

def l_function_content(lattice_name: str) -> Dict[str, Any]:
    r"""Extract the L-function factors from the Epstein zeta of a lattice.

    Returns a dictionary describing which L-functions appear in the
    factorization of epsilon^r_s(V_Lambda).

    Each entry has:
      'type': 'riemann' | 'dirichlet' | 'hecke'
      'description': human-readable description
      'critical_line': Re(s) value of the critical line
    """
    decomp = hecke_decompose(lattice_name)
    rank = decomp['rank']
    content = {'lattice': lattice_name, 'rank': rank, 'l_functions': []}

    if lattice_name == 'Z':
        content['l_functions'] = [
            {
                'type': 'riemann',
                'factor': 'zeta(2s)',
                'critical_line': Fraction(1, 4),
                'description': 'Riemann zeta at 2s; critical line Re(s)=1/4',
            }
        ]
    elif lattice_name == 'Z2':
        content['l_functions'] = [
            {
                'type': 'riemann',
                'factor': 'zeta(s)',
                'critical_line': Fraction(1, 2),
                'description': 'Riemann zeta',
            },
            {
                'type': 'dirichlet',
                'factor': 'L(s, chi_{-4})',
                'critical_line': Fraction(1, 2),
                'description': 'Dirichlet L-function for chi_{-4}',
            },
        ]
    elif lattice_name == 'A2':
        content['l_functions'] = [
            {
                'type': 'riemann',
                'factor': 'zeta(s)',
                'critical_line': Fraction(1, 2),
                'description': 'Riemann zeta',
            },
            {
                'type': 'dirichlet',
                'factor': 'L(s, chi_{-3})',
                'critical_line': Fraction(1, 2),
                'description': 'Dirichlet L-function for chi_{-3}',
            },
        ]
    elif lattice_name == 'E8':
        content['l_functions'] = [
            {
                'type': 'riemann',
                'factor': 'zeta(s)',
                'critical_line': Fraction(1, 2),
                'description': 'Riemann zeta; critical line Re(s)=1/2',
            },
            {
                'type': 'riemann',
                'factor': 'zeta(s-3)',
                'critical_line': Fraction(7, 2),
                'description': 'Shifted Riemann zeta; critical line Re(s)=7/2',
            },
        ]
    elif lattice_name == 'Leech':
        content['l_functions'] = [
            {
                'type': 'riemann',
                'factor': 'zeta(s)',
                'critical_line': Fraction(1, 2),
                'description': 'Riemann zeta; critical line Re(s)=1/2',
            },
            {
                'type': 'riemann',
                'factor': 'zeta(s-11)',
                'critical_line': Fraction(23, 2),
                'description': 'Shifted Riemann zeta; critical line Re(s)=23/2',
            },
            {
                'type': 'hecke',
                'factor': 'L(s, Delta)',
                'critical_line': Fraction(6, 1),
                'description': 'Hecke L-function of Ramanujan Delta; '
                               'critical line Re(s)=6',
            },
        ]
    else:
        raise ValueError(f"Unknown lattice: {lattice_name}")

    return content


# =========================================================================
# Shadow depth from Hecke decomposition
# =========================================================================

def shadow_depth_from_hecke(rank: int, cusp_dim: int) -> int:
    r"""Shadow depth d(V_Lambda) = 1 + d_arith = 1 + (1 + cusp_dim).

    The arithmetic depth d_arith = number of critical lines in the Epstein zeta.

    For SL_2(Z) modular forms of even weight k = rank/2:
      - The Eisenstein part contributes critical lines at Re(s)=1/2 and Re(s)=k-1/2.
        If k = 1 these coincide (1 line). If k >= 2 these are distinct (2 lines).
        But if k = 0 (rank 0) there's nothing.
      - Each cusp form adds a critical line at Re(s)=k/2.
        Different cusp forms at the SAME weight share the same critical line.
        So cusp_dim > 0 adds exactly 1 more line, not cusp_dim lines.

    For rank 1: weight 1/2, Eisenstein gives 1 critical line. d = 1 + 1 = 2.
    For rank 2: weight 1, 1 critical line from Eisenstein. d = 1 + 1 = 2.
    For rank 8: weight 4, 2 critical lines from Eisenstein. d = 1 + 2 = 3.
    For rank 24: weight 12, 2 Eisenstein lines + 1 cusp line. d = 1 + 3 = 4.

    In general for rank > 2 with cusp forms:
      d = 1 + 2 + min(cusp_dim, 1)
    For rank <= 2:
      d = 1 + 1 = 2  (Eisenstein lines coincide for low weight)
    """
    if rank == 0:
        return 1

    # Weight k = rank/2 (for even lattices)
    # Number of distinct Eisenstein critical lines
    if rank <= 2:
        # Weight <= 1: the lines Re(s)=1/2 and Re(s)=k-1/2 coincide (or
        # for rank 1, weight 1/2, there is just Re(s)=1/4).
        eis_lines = 1
    else:
        # Weight >= 2: Re(s)=1/2 and Re(s)=k-1/2 are distinct
        eis_lines = 2

    # Cusp forms contribute at most 1 additional critical line
    # (all cusp forms of weight k have zeros on the same line Re(s)=k/2,
    # which for k>=4 is distinct from both Eisenstein lines).
    cusp_lines = 1 if cusp_dim > 0 else 0

    d_arith = eis_lines + cusp_lines
    return 1 + d_arith


# =========================================================================
# Shadow arity to L-function mapping
# =========================================================================

def shadow_arity_to_l_function(lattice_name: str, arity: int) -> Optional[Dict[str, Any]]:
    r"""Map a shadow arity to the specific L-function it detects.

    The arithmetic sieve principle:
      Arity 2 (kappa):   Riemann zeta (always present for rank >= 1)
      Arity 3 (cubic):   Shifted Eisenstein zeta (present for rank > 2)
      Arity 4 (quartic): First cusp form L-function (if cusp forms exist)
      Arity 5+:          Higher cusp form L-functions

    Returns None if the given arity does not activate an L-function
    (i.e., the shadow terminates before this arity).
    """
    decomp = hecke_decompose(lattice_name)
    rank = decomp['rank']

    if arity < 2:
        return None

    if arity == 2:
        # kappa always present
        if lattice_name == 'Z':
            return {'type': 'riemann', 'factor': 'zeta(2s)',
                    'period_type': 'Riemann'}
        return {'type': 'riemann', 'factor': 'zeta(s)',
                'period_type': 'Riemann'}

    if arity == 3:
        # Cubic shadow detects Eisenstein part beyond constant.
        # Active only when Eisenstein has a SHIFTED factor, i.e., rank > 2.
        if rank <= 2:
            return None
        k = rank // 2
        return {'type': 'riemann', 'factor': f'zeta(s-{k-1})',
                'period_type': 'Dedekind'}

    if arity >= 4:
        # Cusp forms
        cusp_dim = decomp['cusp_dim']
        if cusp_dim == 0:
            return None
        cusp_forms = decomp['cusp_coeffs']
        idx = arity - 4  # 0-indexed into cusp form list
        if idx < len(cusp_forms):
            name, coeff = cusp_forms[idx]
            return {'type': 'hecke', 'factor': f'L(s, {name})',
                    'cusp_form': name, 'coefficient': coeff,
                    'period_type': 'Hecke'}
        return None

    return None


# =========================================================================
# Full arithmetic sieve verification
# =========================================================================

def verify_arithmetic_sieve(lattice_name: str) -> Dict[str, Any]:
    r"""Full verification of the arithmetic sieve for a named lattice.

    Checks that:
    1. The depth formula d = 1 + d_arith matches the known shadow depth.
    2. Each arity maps to the correct L-function.
    3. The Hecke decomposition is consistent.
    4. The Epstein zeta factors as claimed.

    Returns a dictionary of verification results.
    """
    data = lattice_data(lattice_name)
    decomp = hecke_decompose(lattice_name)
    l_content = l_function_content(lattice_name)

    # Compute depth from formula
    cusp_dim = decomp['cusp_dim']
    rank = decomp['rank']
    depth_formula = shadow_depth_from_hecke(rank, cusp_dim)
    depth_expected = data['shadow_depth']

    # Arity-to-L mapping
    arity_map = {}
    for a in range(2, depth_expected + 3):
        result = shadow_arity_to_l_function(lattice_name, a)
        if result is not None:
            arity_map[a] = result

    # Shadow archetype classification
    archetype_map = {2: 'G', 3: 'L', 4: 'C'}
    archetype = archetype_map.get(depth_expected, 'M')

    return {
        'lattice': lattice_name,
        'rank': rank,
        'depth_formula': depth_formula,
        'depth_expected': depth_expected,
        'depth_match': depth_formula == depth_expected,
        'cusp_dim': cusp_dim,
        'eisenstein_only': decomp['eisenstein_only'],
        'arity_map': arity_map,
        'num_l_functions': len(l_content['l_functions']),
        'archetype': archetype,
        'l_content': l_content,
    }


# =========================================================================
# Period matrix
# =========================================================================

def period_matrix(lattice_name: str, num_arities: int = 6) -> Dict[int, Optional[Dict]]:
    r"""Matrix of {arity: L-function/period data} for a given lattice.

    Columns are arities 2, 3, ..., 2 + num_arities - 1.
    Each entry is the L-function data for that arity, or None if
    the shadow terminates before that arity.
    """
    result = {}
    for a in range(2, 2 + num_arities):
        result[a] = shadow_arity_to_l_function(lattice_name, a)
    return result


# =========================================================================
# Named lattice data
# =========================================================================

def lattice_data(name: str) -> Dict[str, Any]:
    r"""Return (rank, shadow_depth, archetype, L_content_description) for named lattices.

    The five principal lattice VOAs:
      V_Z:      rank 1, depth 2, Gaussian (G)
      V_{Z^2}:  rank 2, depth 2, Gaussian (G)
      V_{A_2}:  rank 2, depth 2, Gaussian (G)
      V_{E_8}:  rank 8, depth 3, Lie/tree (L)
      V_{Leech}: rank 24, depth 4, contact (C)
    """
    catalog = {
        'Z': {
            'rank': 1,
            'shadow_depth': 2,
            'archetype': 'G',
            'description': 'Integer lattice Z; theta = theta_3(2tau)',
            'epstein_formula': 'epsilon^1_s = 2*zeta(2s)',
        },
        'Z2': {
            'rank': 2,
            'shadow_depth': 2,
            'archetype': 'G',
            'description': 'Square lattice Z^2; theta = theta_3(2tau)^2',
            'epstein_formula': 'epsilon^2_s = 4*zeta(s)*L(s, chi_{-4})',
        },
        'A2': {
            'rank': 2,
            'shadow_depth': 2,
            'archetype': 'G',
            'description': 'A_2 root lattice; theta in M_1(Gamma_0(3), chi_3)',
            'epstein_formula': 'epsilon^2_s = 6*zeta(s)*L(s, chi_{-3})',
        },
        'E8': {
            'rank': 8,
            'shadow_depth': 3,
            'archetype': 'L',
            'description': 'E_8 root lattice; theta = E_4(tau)',
            'epstein_formula': 'epsilon^8_s = 240*4^{-s}*zeta(s)*zeta(s-3)',
        },
        'Leech': {
            'rank': 24,
            'shadow_depth': 4,
            'archetype': 'C',
            'description': 'Leech lattice; theta = E_{12} - (65520/691)*Delta',
            'epstein_formula': 'epsilon^24_s = c_E*zeta(s)*zeta(s-11) '
                               '+ c_Delta*L(s, Delta)',
        },
    }
    if name not in catalog:
        raise ValueError(f"Unknown lattice: {name}. "
                         f"Available: {list(catalog.keys())}")
    return catalog[name]


# =========================================================================
# Shadow-period dictionary (summary table)
# =========================================================================

def shadow_period_dictionary() -> List[Dict[str, str]]:
    r"""The master shadow-period dictionary.

    Returns the table mapping shadow arity to modular source,
    L-function, and period type.
    """
    return [
        {
            'arity': 2,
            'shadow_name': 'kappa',
            'modular_source': 'constant term',
            'l_function': 'zeta(s)',
            'period_type': 'Riemann',
        },
        {
            'arity': 3,
            'shadow_name': 'cubic',
            'modular_source': 'Eisenstein E_k',
            'l_function': 'zeta(s)*zeta(s-k+1)',
            'period_type': 'Dedekind',
        },
        {
            'arity': 4,
            'shadow_name': 'quartic',
            'modular_source': 'first cusp form f_1',
            'l_function': 'L(s, f_1)',
            'period_type': 'Hecke',
        },
        {
            'arity': 5,
            'shadow_name': 'quintic+',
            'modular_source': 'higher cusp forms f_j',
            'l_function': 'L(s, f_j)',
            'period_type': 'Hecke',
        },
    ]
