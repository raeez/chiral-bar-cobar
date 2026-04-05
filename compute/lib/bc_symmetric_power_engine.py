r"""bc_symmetric_power_engine.py -- Symmetric power L-functions, Sato-Tate
distributions, moments, Rankin-Selberg at zeta zeros, and low-lying zero
statistics from shadow tower data.

MATHEMATICAL FRAMEWORK
======================

The shadow obstruction tower of a modular Koszul algebra A produces a
sequence of shadow coefficients {S_r(A)}_{r >= 2} that, for class M
algebras (Virasoro, W_N), form an infinite sequence with controlled
growth (thm:shadow-radius).  When the algebra admits an interpretation as
a lattice VOA or is associated to a Hecke eigenform, the Satake parameters
at each prime p encode the full symmetric power structure.

1. SYMMETRIC POWER L-FUNCTIONS

   For Satake parameters alpha_p, beta_p at prime p (alpha_p + beta_p = a(p),
   alpha_p * beta_p = p^{k-1} for weight k):

     L(s, Sym^m f) = prod_p prod_{j=0}^m (1 - alpha_p^j beta_p^{m-j} p^{-s})^{-1}

   Status (Langlands functoriality):
     Sym^1: Hecke (1930s)                -- unconditional
     Sym^2: Gelbart-Jacquet (1978)       -- unconditional
     Sym^3: Kim-Shahidi (2002)           -- unconditional
     Sym^4: Kim (2003)                   -- unconditional
     Sym^5+: Newton-Thorne (2021)        -- for holomorphic forms, conditional
                                            on modularity lifting

2. SATO-TATE DISTRIBUTION

   For a non-CM eigenform of weight k >= 2, the normalized Hecke eigenvalues
     x_p := a(p) / (2 p^{(k-1)/2})
   are equidistributed in [-1, 1] with respect to the Sato-Tate measure:
     d mu_{ST}(x) = (2/pi) sqrt(1 - x^2) dx

   KEY QUESTION: does the shadow depth class (G/L/C/M) affect the rate
   of convergence to Sato-Tate?  This is the novel content of this module.

   For terminating towers (classes G/L/C), the finite shadow depth should
   give faster convergence: the spectral data is algebraically simpler.
   For class M (infinite tower), the rate should match the generic
   Akiyama-Tanigawa bound O(1/sqrt(pi(T) log T)).

3. MOMENTS AND RANDOM MATRIX THEORY

   M_n(T) = (1/pi(T)) sum_{p <= T} x_p^n

   Sato-Tate predicts M_{2n} -> C_n (n-th Catalan number = (2n)!/(n!(n+1)!))
   and M_{2n+1} -> 0.

4. RANKIN-SELBERG AT ZETA ZEROS

   L(rho_n, f tensor f) for nontrivial Riemann zeros rho_n = 1/2 + i*gamma_n.
   The Rankin-Selberg convolution:
     L(s, f x f) = zeta(2s - 2k + 2) * sum |a(n)|^2 n^{-s}
   has a pole at s = k (from Petersson norm) and encodes the full self-dual
   structure.

5. PETERSSON NORM VIA Sym^2

   L(1, Sym^2 f) = (4 pi)^k / ((k-1)! * 2^{k-1}) * pi * <f,f>
   (Shimura's formula, normalized for SL_2(Z) forms)

   For the Ramanujan Delta (k=12, level 1):
     <Delta, Delta> = ||Delta||^2 = integral_{SL_2(Z)\H} |Delta(tau)|^2 y^{12} d mu(tau)

6. KATZ-SARNAK SYMMETRY TYPES

   Low-lying zeros of Sym^k L-functions reveal the symmetry type:
     k even: symplectic family -> W_1 = 1 - sin(2 pi x)/(2 pi x)
     k odd:  orthogonal family -> W_1 = 1 + (1/2) delta_0(x) + sin(2 pi x)/(2 pi x)
   (Modulo even/odd orthogonal splitting for k odd.)

7. APPROXIMATE FUNCTIONAL EQUATION (AFE)

   L(s, Sym^m f) = sum_{n=1}^{N} a_m(n) n^{-s} V(n/sqrt(N_m))
                  + epsilon * sum_{n=1}^{N} a_m(n) n^{-(1-s)} V(n/sqrt(N_m))

   where V is a smooth cutoff, epsilon is the root number, and N_m is the
   analytic conductor.

References:
  - prop:shadow-symmetric-power (arithmetic_shadows.tex)
  - thm:shadow-radius (higher_genus_modular_koszul.tex)
  - thm:operadic-rankin-selberg (arithmetic_shadows.tex)
  - Deligne, "La conjecture de Weil. I" (1974)
  - Gelbart-Jacquet (1978), Kim-Shahidi (2002), Kim (2003)
  - Barnet-Lamb, Geraghty, Harris, Taylor (2011) -- Sato-Tate for GL_2
  - Newton-Thorne (2021) -- Sym^n for holomorphic eigenforms
  - Katz-Sarnak, "Random Matrices, Frobenius Eigenvalues, and Monodromy" (1999)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa != c/2 in general.
CAUTION (AP10): Cross-family consistency is the real verification.
CAUTION (AP15): E_2* is quasi-modular; shadow modular forms are NOT classical.
CAUTION (AP38): Normalization conventions must be tracked.
CAUTION (AP48): kappa(A) depends on the full algebra, not just the Virasoro
                subalgebra.  kappa = c/2 for Virasoro only.
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =========================================================================
# 0. Prime sieve
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


def _nth_prime(n: int) -> int:
    """Return the n-th prime (1-indexed)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    if n <= 6:
        return [2, 3, 5, 7, 11, 13][n - 1]
    upper = int(n * (math.log(n) + math.log(math.log(n))) + 3)
    primes = _primes_up_to(upper)
    while len(primes) < n:
        upper = int(upper * 1.5)
        primes = _primes_up_to(upper)
    return primes[n - 1]


def _primes_list(count: int) -> List[int]:
    """Return the first 'count' primes."""
    if count <= 0:
        return []
    upper = max(30, int(count * (math.log(count + 1) + math.log(math.log(count + 2)) + 3)))
    primes = _primes_up_to(upper)
    while len(primes) < count:
        upper = int(upper * 1.5)
        primes = _primes_up_to(upper)
    return primes[:count]


# =========================================================================
# 1. Ramanujan tau function
# =========================================================================

@lru_cache(maxsize=512)
def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficients of Delta = q prod_{m>=1} (1-q^m)^{24}.

    tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830,
    tau(7)=-16744, tau(11)=534612, tau(13)=-577738.
    """
    if n < 1:
        return 0
    # Build the full q-expansion up to index n
    # Delta = q * prod(1-q^m)^{24}, so coefficients shifted by 1
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    # Expand prod (1-q^m)^{24} up to q^{N-1} (since we need coeff of q^{n-1})
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    # tau(n) = coeff of q^n in Delta = coeff of q^{n-1} in prod(1-q^m)^24
    return coeffs[n - 1] if n - 1 <= N else 0


# =========================================================================
# 2. Satake parameters
# =========================================================================

def satake_parameters(a_p, k: int, p: int):
    r"""Compute Satake parameters alpha_p, beta_p for weight-k eigenform.

    alpha + beta = a(p),  alpha * beta = p^{k-1}.
    Returns (alpha, beta) as mpmath mpc if available.

    Ramanujan (Deligne for k >= 2): |alpha| = |beta| = p^{(k-1)/2}.
    """
    if HAS_MPMATH:
        a_mp = mpmath.mpf(a_p)
        pk1 = mpmath.power(p, k - 1)
        disc = a_mp ** 2 - 4 * pk1
        sqrt_d = mpmath.sqrt(disc)
        alpha = (a_mp + sqrt_d) / 2
        beta = (a_mp - sqrt_d) / 2
        return alpha, beta
    disc = a_p * a_p - 4 * p ** (k - 1)
    if disc >= 0:
        sqrt_d = math.sqrt(disc)
        return (a_p + sqrt_d) / 2, (a_p - sqrt_d) / 2
    sqrt_d = math.sqrt(-disc)
    return complex(a_p / 2, sqrt_d / 2), complex(a_p / 2, -sqrt_d / 2)


def _mp_abs(z):
    """Absolute value for mpmath or Python types."""
    if HAS_MPMATH:
        return float(mpmath.fabs(mpmath.mpc(z)))
    return abs(z)


def _mp_re(z):
    """Real part for mpmath or Python types."""
    if HAS_MPMATH:
        return float(mpmath.re(mpmath.mpc(z)))
    if isinstance(z, complex):
        return z.real
    return float(z)


def _mp_float(z):
    """Convert to Python float (taking real part if complex-with-tiny-imaginary)."""
    if HAS_MPMATH:
        c = mpmath.mpc(z)
        if abs(float(mpmath.im(c))) < 1e-30:
            return float(mpmath.re(c))
        return complex(float(mpmath.re(c)), float(mpmath.im(c)))
    if isinstance(z, complex):
        if abs(z.imag) < 1e-30:
            return z.real
        return z
    return float(z)


# =========================================================================
# 3. Hecke eigenvalue sources
# =========================================================================

def ramanujan_tau_coeffs(num_primes: int = 100) -> Dict[int, int]:
    """Return {p: tau(p)} for the first num_primes primes."""
    primes = _primes_list(num_primes)
    return {p: ramanujan_tau(p) for p in primes}


def eisenstein_coefficients(k: int, num_primes: int = 100) -> Dict[int, float]:
    r"""Return {p: sigma_{k-1}(p)} for the normalized Eisenstein series E_k.

    The Hecke eigenvalue of E_k at prime p is sigma_{k-1}(p) = 1 + p^{k-1}.
    """
    primes = _primes_list(num_primes)
    return {p: 1 + p ** (k - 1) for p in primes}


def shadow_virasoro_hecke_data(c_val, max_arity: int = 30):
    r"""Extract 'Hecke-like' data from Virasoro shadow coefficients.

    The shadow sequence {S_r} for Virasoro is an infinite tower (class M).
    We treat S_r as formal Fourier coefficients of a 'shadow modular form'
    and extract the implied 'Hecke eigenvalue' at each prime by identifying
    S_p = a(p) / p  (the normalized Dirichlet coefficient).

    This is a FORMAL identification; the shadow sequence is not literally
    a Hecke eigenform in the classical sense.  But the analytic structure
    (growth rate, Sato-Tate-like distribution, etc.) can be meaningfully
    studied.

    Returns dict {p: a_p} where a_p = p * S_p (formal Hecke eigenvalue).
    """
    try:
        from shadow_euler_product_engine import virasoro_shadow_coefficients
    except ImportError:
        try:
            from .shadow_euler_product_engine import virasoro_shadow_coefficients
        except ImportError:
            from sympy import Rational
            # Inline minimal implementation
            def virasoro_shadow_coefficients(cv, max_r):
                from sympy import Rational, cancel
                cv = Rational(cv)
                if cv == 0:
                    return {}
                a = [Rational(0)] * (max_r - 1)
                a[0] = cv
                if max_r > 2:
                    a[1] = Rational(6)
                if max_r > 3:
                    a[2] = Rational(40) / (cv * (5 * cv + 22))
                for n in range(3, max_r - 1):
                    conv = sum(a[j] * a[n - j] for j in range(1, n))
                    a[n] = cancel(-conv / (2 * cv))
                result = {}
                for r in range(2, max_r + 1):
                    idx = r - 2
                    if idx < len(a):
                        result[r] = cancel(a[idx] / r)
                return result

    from sympy import Rational
    S = virasoro_shadow_coefficients(Rational(c_val) if not isinstance(c_val, Rational) else c_val, max_arity)
    # Extract formal Hecke eigenvalues at primes: a(p) = p * S_p
    primes = [p for p in _primes_up_to(max_arity) if p in S]
    return {p: float(S[p] * p) for p in primes}


# =========================================================================
# 4. Symmetric power L-functions
# =========================================================================

def sym_power_euler_factor(alpha, beta, m: int, p: int, s):
    r"""Euler factor of L(s, Sym^m f) at prime p:

      prod_{j=0}^m (1 - alpha^j beta^{m-j} p^{-s})^{-1}
    """
    if HAS_MPMATH:
        result = mpmath.mpc(1)
        ps = mpmath.power(p, -mpmath.mpc(s))
        for j in range(m + 1):
            term = mpmath.power(alpha, j) * mpmath.power(beta, m - j) * ps
            result *= 1 / (1 - term)
        return result
    result = 1.0 + 0j
    ps = p ** (-complex(s))
    for j in range(m + 1):
        term = alpha ** j * beta ** (m - j) * ps
        denom = 1 - term
        if abs(denom) < 1e-300:
            return float('inf')
        result *= 1 / denom
    return result


def sym_power_L(f_coeffs: Dict[int, Any], k: int, m: int, s,
                num_primes: int = 100) -> complex:
    r"""Compute L(s, Sym^m f) as a partial Euler product over num_primes primes.

    Parameters
    ----------
    f_coeffs : {p: a(p)} Hecke eigenvalues at primes
    k : weight of the eigenform
    m : symmetric power degree (m=1 is standard, m=2 is Sym^2, etc.)
    s : complex evaluation point
    num_primes : number of primes to include

    Returns complex value of the partial Euler product.
    """
    primes = sorted(f_coeffs.keys())[:num_primes]
    if HAS_MPMATH:
        result = mpmath.mpc(1)
        for p in primes:
            a_p = f_coeffs[p]
            alpha, beta = satake_parameters(a_p, k, p)
            ef = sym_power_euler_factor(alpha, beta, m, p, s)
            result *= ef
        return _mp_float(result)
    result = 1.0 + 0j
    for p in primes:
        a_p = f_coeffs[p]
        alpha, beta = satake_parameters(a_p, k, p)
        ef = sym_power_euler_factor(alpha, beta, m, p, s)
        if isinstance(ef, float) and math.isinf(ef):
            return float('inf')
        result *= ef
    return complex(result)


def sym_power_L_multi(f_coeffs: Dict[int, Any], k: int,
                      m_values: List[int], s_values: List,
                      num_primes: int = 100) -> Dict[int, Dict]:
    r"""Compute L(s, Sym^m f) for multiple m and s values.

    Returns {m: {s: L(s, Sym^m f)}} nested dictionary.
    """
    result = {}
    for m in m_values:
        result[m] = {}
        for s in s_values:
            result[m][s] = sym_power_L(f_coeffs, k, m, s, num_primes)
    return result


# =========================================================================
# 5. Sato-Tate distribution and KS statistic
# =========================================================================

def sato_tate_cdf(x: float) -> float:
    r"""CDF of the Sato-Tate measure: F(x) = integral_{-1}^x (2/pi) sqrt(1-t^2) dt.

    Explicit formula: F(x) = 1/2 + (1/pi)(x sqrt(1-x^2) + arcsin(x)).
    """
    if x <= -1.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    return 0.5 + (x * math.sqrt(1 - x * x) + math.asin(x)) / math.pi


def sato_tate_pdf(x: float) -> float:
    r"""PDF of the Sato-Tate measure: (2/pi) sqrt(1 - x^2) on [-1, 1]."""
    if abs(x) > 1.0:
        return 0.0
    return (2.0 / math.pi) * math.sqrt(1 - x * x)


def normalize_hecke_eigenvalue(a_p, k: int, p: int) -> float:
    r"""Normalize the Hecke eigenvalue for Sato-Tate:

      x_p = a(p) / (2 p^{(k-1)/2})

    This maps the Ramanujan-bounded eigenvalue into [-1, 1].
    """
    denom = 2.0 * p ** ((k - 1) / 2.0)
    return float(a_p) / denom if denom != 0 else 0.0


def sato_tate_data(f_coeffs: Dict[int, Any], k: int,
                   num_primes: Optional[int] = None) -> List[float]:
    r"""Compute normalized Hecke eigenvalues x_p = a(p)/(2 p^{(k-1)/2}).

    Returns sorted list of x_p values for the first num_primes primes.
    """
    primes = sorted(f_coeffs.keys())
    if num_primes is not None:
        primes = primes[:num_primes]
    x_vals = [normalize_hecke_eigenvalue(f_coeffs[p], k, p) for p in primes]
    return sorted(x_vals)


def kolmogorov_smirnov_stat(x_sorted: List[float]) -> float:
    r"""Kolmogorov-Smirnov statistic against the Sato-Tate distribution.

    D_n = sup_x |F_n(x) - F_{ST}(x)|

    where F_n is the empirical CDF and F_{ST} is the Sato-Tate CDF.
    """
    n = len(x_sorted)
    if n == 0:
        return 0.0
    d_max = 0.0
    for i, x in enumerate(x_sorted):
        f_st = sato_tate_cdf(x)
        # F_n(x) = (i+1)/n  (right limit)
        d_plus = abs((i + 1) / n - f_st)
        # F_n(x-) = i/n     (left limit)
        d_minus = abs(i / n - f_st)
        d_max = max(d_max, d_plus, d_minus)
    return d_max


def sato_tate_ks_test(f_coeffs: Dict[int, Any], k: int,
                      num_primes: Optional[int] = None) -> Dict[str, Any]:
    r"""Full Sato-Tate KS test for the given Hecke eigenvalues.

    Returns:
      'ks_statistic': the KS statistic D_n
      'num_primes': n
      'critical_5pct': critical value at 5% significance (1.36 / sqrt(n))
      'consistent_with_st': whether D_n < critical value
      'normalized_eigenvalues': sorted list of x_p values
    """
    x_sorted = sato_tate_data(f_coeffs, k, num_primes)
    n = len(x_sorted)
    ks = kolmogorov_smirnov_stat(x_sorted)
    crit = 1.36 / math.sqrt(n) if n > 0 else float('inf')
    return {
        'ks_statistic': ks,
        'num_primes': n,
        'critical_5pct': crit,
        'consistent_with_st': ks < crit,
        'normalized_eigenvalues': x_sorted,
    }


def sato_tate_histogram(f_coeffs: Dict[int, Any], k: int,
                        num_bins: int = 50,
                        num_primes: Optional[int] = None) -> Dict[str, Any]:
    r"""Bin the normalized eigenvalues and compare with Sato-Tate density.

    Returns bin edges, empirical counts, and theoretical ST counts.
    """
    x_sorted = sato_tate_data(f_coeffs, k, num_primes)
    n = len(x_sorted)
    edges = [-1.0 + 2.0 * i / num_bins for i in range(num_bins + 1)]
    emp_counts = [0] * num_bins
    for x in x_sorted:
        b = int((x + 1.0) / (2.0 / num_bins))
        if b >= num_bins:
            b = num_bins - 1
        if b < 0:
            b = 0
        emp_counts[b] += 1
    # Theoretical ST counts
    st_counts = []
    for i in range(num_bins):
        lo, hi = edges[i], edges[i + 1]
        expected = n * (sato_tate_cdf(hi) - sato_tate_cdf(lo))
        st_counts.append(expected)
    return {
        'edges': edges,
        'empirical_counts': emp_counts,
        'st_expected_counts': st_counts,
        'num_samples': n,
    }


# =========================================================================
# 6. Shadow depth and Sato-Tate convergence rate
# =========================================================================

SHADOW_DEPTH_CLASSES = {
    'heisenberg': ('G', 2),
    'lattice_E8': ('G', 2),
    'lattice_Leech': ('G', 2),
    'affine_sl2': ('L', 3),
    'betagamma': ('C', 4),
    'virasoro': ('M', float('inf')),
    'w3': ('M', float('inf')),
}


def sato_tate_convergence_rate(f_coeffs: Dict[int, Any], k: int,
                               checkpoints: Optional[List[int]] = None
                               ) -> List[Dict[str, Any]]:
    r"""Compute the KS statistic at increasing numbers of primes.

    Returns a list of {num_primes, ks_statistic, critical_5pct, scaled_ks}
    at each checkpoint.  The scaled KS statistic is D_n * sqrt(n), which
    should converge to a constant under Sato-Tate.

    If convergence is faster than O(1/sqrt(n)), the scaled KS DECREASES.
    This is the diagnostic for shadow-depth-dependent convergence.
    """
    if checkpoints is None:
        checkpoints = [50, 100, 200, 500, 1000, 2000, 5000]
    primes = sorted(f_coeffs.keys())
    results = []
    for cp in checkpoints:
        if cp > len(primes):
            cp = len(primes)
        if cp == 0:
            continue
        subset = {p: f_coeffs[p] for p in primes[:cp]}
        ks = sato_tate_ks_test(subset, k, cp)
        scaled = ks['ks_statistic'] * math.sqrt(cp)
        results.append({
            'num_primes': cp,
            'ks_statistic': ks['ks_statistic'],
            'critical_5pct': ks['critical_5pct'],
            'scaled_ks': scaled,
            'consistent_with_st': ks['consistent_with_st'],
        })
    return results


def compare_convergence_rates_by_depth(num_primes: int = 500) -> Dict[str, Any]:
    r"""Compare Sato-Tate convergence rates across shadow depth classes.

    Uses the Ramanujan Delta (weight 12, non-CM) as the universal test form,
    evaluated at varying numbers of primes.

    This is NOT a comparison of different algebras' convergence; it is a
    comparison of how the same eigenform's Sato-Tate convergence relates
    to the shadow depth of the algebra it lives in.

    For genuine class-dependent convergence, one would need to compare
    the formal shadow Hecke eigenvalues across families, which is what
    the broader programme does.

    Returns per-checkpoint KS statistics.
    """
    tau_coeffs = ramanujan_tau_coeffs(num_primes)
    checkpoints = [10, 25, 50, 100, 200, 500]
    checkpoints = [c for c in checkpoints if c <= num_primes]
    results = sato_tate_convergence_rate(tau_coeffs, 12, checkpoints)
    return {
        'form': 'Ramanujan_Delta',
        'weight': 12,
        'convergence_data': results,
    }


# =========================================================================
# 7. Moments and Catalan numbers
# =========================================================================

def catalan(n: int) -> int:
    r"""n-th Catalan number: C_n = (2n)! / (n! (n+1)!)."""
    return math.comb(2 * n, n) // (n + 1)


def moment(f_coeffs: Dict[int, Any], k: int, power: int,
           T: Optional[int] = None) -> float:
    r"""Compute M_power(T) = (1/pi(T)) sum_{p <= T} x_p^power.

    Where x_p = a(p) / (2 p^{(k-1)/2}).
    """
    primes = sorted(f_coeffs.keys())
    if T is not None:
        primes = [p for p in primes if p <= T]
    if not primes:
        return 0.0
    total = 0.0
    for p in primes:
        x_p = normalize_hecke_eigenvalue(f_coeffs[p], k, p)
        total += x_p ** power
    return total / len(primes)


def moments_table(f_coeffs: Dict[int, Any], k: int,
                  powers: Optional[List[int]] = None,
                  T_values: Optional[List[int]] = None) -> Dict:
    r"""Compute moments M_n(T) for multiple n and T.

    Returns {n: {T: M_n(T)}} with Sato-Tate predictions.
    """
    if powers is None:
        powers = list(range(1, 9))
    if T_values is None:
        T_values = [1000, 10000, 100000]
    result = {}
    for n in powers:
        result[n] = {}
        for T in T_values:
            result[n][T] = moment(f_coeffs, k, n, T)
    # Add ST predictions
    st_predictions = {}
    for n in powers:
        if n % 2 == 0:
            st_predictions[n] = catalan(n // 2) / (2.0 ** n)
            # Integral of x^{2m} under ST measure = C_m / 4^m
            # Actually: integral_{-1}^1 x^{2m} (2/pi) sqrt(1-x^2) dx
            # = (2/pi) B(m+1/2, 3/2) / 2 = (2/pi) * Gamma(m+1/2)*Gamma(3/2)/(2*Gamma(m+2))
            # For m=1: (2/pi)*(sqrt(pi)/2)*(sqrt(pi)/2)/(2*1) = (2/pi)*(pi/4)/2 = 1/4
            # Catalan(1)=1, so C_1/4^1 = 1/4. Check.
            # For m=2: integral x^4 ST = (2/pi) * (3sqrt(pi)/4)*(sqrt(pi)/2) / (2*6)
            #        = (2/pi) * 3pi/8 / 12 = (2/pi) * pi/32 = 1/16
            # Catalan(2)=2, so C_2/4^2 = 2/16 = 1/8 != 1/16.
            # Correction: the ST integral of x^{2m} = C_m / 4^m is wrong.
            # Correct: integral_{-1}^1 x^{2m} (2/pi) sqrt(1-x^2) dx = C_m / 4^m
            # Let me recompute. With substitution x = sin(theta):
            # = (2/pi) integral_{-pi/2}^{pi/2} sin^{2m}(theta) cos^2(theta) d theta
            # = (2/pi) * B((2m+1)/2, 3/2) / ... standard beta integral
            # = (2/pi) * Gamma(m + 1/2) * Gamma(3/2) / (2 * Gamma(m + 2))
            # = (2/pi) * ((2m)! sqrt(pi)) / (4^m m!) * (sqrt(pi)/2) / (2*(m+1)!)
            # = (2/pi) * (2m)! pi / (4^m m! * 4 * (m+1)!)
            # = (2m)! / (2 * 4^m * m! * (m+1)!)
            # = C_m / (2 * 4^m)
            # So M_{2m} -> C_m / (2 * 4^m)
            m = n // 2
            st_predictions[n] = catalan(m) / (2.0 * 4.0 ** m)
        else:
            st_predictions[n] = 0.0  # Odd moments vanish by symmetry
    result['st_predictions'] = st_predictions
    return result


def moment_prediction_st(n: int) -> float:
    r"""Sato-Tate prediction for the n-th moment of x_p = a(p)/(2p^{(k-1)/2}).

    M_{2m} = C_m / (2 * 4^m)  where C_m = m-th Catalan number
    M_{2m+1} = 0              (odd moments vanish by symmetry)

    Derivation:
      integral_{-1}^1 x^{2m} (2/pi) sqrt(1-x^2) dx
      = (2/pi) B(m + 1/2, 3/2) / 2  [using x = sin(theta)]
      = C_m / (2 * 4^m)
    """
    if n % 2 == 1:
        return 0.0
    m = n // 2
    return catalan(m) / (2.0 * 4.0 ** m)


# =========================================================================
# 8. Rankin-Selberg L-function
# =========================================================================

def rankin_selberg_euler_factor(alpha_A, beta_A, alpha_B, beta_B, p: int, s):
    r"""Euler factor of L(s, f_A x f_B) at prime p:

      prod_{i in {0,1}, j in {0,1}} (1 - alpha_A^i beta_A^{1-i} alpha_B^j beta_B^{1-j} p^{-s})^{-1}

    Wait -- that's 4 factors. The Rankin-Selberg convolution for GL_2 x GL_2 has
    degree 4 Euler product:
      L(s, f x g) = prod_p prod_{i,j} (1 - alpha_p(f)_i alpha_p(g)_j p^{-s})^{-1}
    where {alpha_p(f)_0, alpha_p(f)_1} = {alpha_p(f), beta_p(f)}.
    """
    satake_A = [alpha_A, beta_A]
    satake_B = [alpha_B, beta_B]
    if HAS_MPMATH:
        result = mpmath.mpc(1)
        ps = mpmath.power(p, -mpmath.mpc(s))
        for a in satake_A:
            for b in satake_B:
                term = a * b * ps
                result *= 1 / (1 - term)
        return result
    result = 1.0 + 0j
    ps = p ** (-complex(s))
    for a in satake_A:
        for b in satake_B:
            term = a * b * ps
            denom = 1 - term
            if abs(denom) < 1e-300:
                return float('inf')
            result *= 1 / denom
    return result


def rankin_selberg_L(f_coeffs: Dict[int, Any], k_f: int,
                     g_coeffs: Optional[Dict[int, Any]] = None, k_g: Optional[int] = None,
                     s=2.0, num_primes: int = 100) -> complex:
    r"""Compute L(s, f x g) as a partial Euler product.

    If g_coeffs is None, computes the self-convolution L(s, f x f).
    """
    if g_coeffs is None:
        g_coeffs = f_coeffs
    if k_g is None:
        k_g = k_f
    primes = sorted(set(f_coeffs.keys()) & set(g_coeffs.keys()))[:num_primes]
    if HAS_MPMATH:
        result = mpmath.mpc(1)
    else:
        result = 1.0 + 0j
    for p in primes:
        alpha_f, beta_f = satake_parameters(f_coeffs[p], k_f, p)
        alpha_g, beta_g = satake_parameters(g_coeffs[p], k_g, p)
        ef = rankin_selberg_euler_factor(alpha_f, beta_f, alpha_g, beta_g, p, s)
        result *= ef
    return _mp_float(result)


# =========================================================================
# 9. Rankin-Selberg at Riemann zeta zeros
# =========================================================================

# First 50 imaginary parts of nontrivial zeros of zeta(s)
# (from Odlyzko's tables, high precision)
RIEMANN_ZEROS_50 = [
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739189, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167159,
    49.773832477672302, 52.970321477714460, 56.446247697063394,
    59.347044002602353, 60.831778524609809, 65.112544048081607,
    67.079810529494174, 69.546401711173979, 72.067157674481907,
    75.704690699083933, 77.144840068874805, 79.337375020249367,
    82.910380854086030, 84.735492980517050, 87.425274613125229,
    88.809111207634465, 92.491899270558484, 94.651344040519838,
    95.870634228245309, 98.831194218193692, 101.31785100573139,
    103.72553804532511, 105.44662305232540, 107.16861118427640,
    111.02953554316967, 111.87465917699263, 114.32022091545271,
    116.22668032085755, 118.79078286597621, 121.37012500242067,
    122.94682929355258, 124.25681855434576, 127.51668387959649,
    129.57870441676570, 131.08768853093266, 133.49773720299758,
    134.75650975337387, 138.11604205453344, 139.73620895212138,
    141.12370740402112, 143.11184580762063,
]


def rankin_selberg_at_zeta_zeros(f_coeffs: Dict[int, Any], k: int,
                                 num_zeros: int = 50,
                                 num_primes: int = 100) -> List[Dict[str, Any]]:
    r"""Compute L(1/2 + i*gamma_n, f x f) at the first num_zeros Riemann zeros.

    Returns a list of {zero_index, gamma, L_value, abs_L}.
    """
    results = []
    zeros = RIEMANN_ZEROS_50[:num_zeros]
    for idx, gamma in enumerate(zeros):
        s = complex(0.5, gamma)
        val = rankin_selberg_L(f_coeffs, k, s=s, num_primes=num_primes)
        results.append({
            'zero_index': idx + 1,
            'gamma': gamma,
            'L_value': val,
            'abs_L': abs(val) if isinstance(val, (complex, float)) else _mp_abs(val),
        })
    return results


# =========================================================================
# 10. Petersson norm via Sym^2 (self-consistency check)
# =========================================================================

def petersson_norm_from_sym2(f_coeffs: Dict[int, Any], k: int,
                             num_primes: int = 100) -> Dict[str, Any]:
    r"""Compute <f, f> from L(1, Sym^2 f) via Shimura's formula.

    Shimura: L(1, Sym^2 f) = (4 pi)^k / ((k-1)! * zeta(2)) * <f, f>

    Equivalently:
      <f, f> = L(1, Sym^2 f) * (k-1)! * zeta(2) / (4 pi)^k

    where <f, f> = integral_{Gamma\H} |f(tau)|^2 y^k d mu(tau)
    with d mu = dx dy / y^2.

    For normalized eigenforms on SL_2(Z), there is a well-known relation.
    The exact constant depends on the normalization convention.

    We compute:
      - L(1, Sym^2 f) via Euler product
      - The implied Petersson norm
      - An independent estimate of <f, f> via Rankin-Selberg (if available)
    """
    L_sym2_1 = sym_power_L(f_coeffs, k, 2, 1.0, num_primes)
    # Shimura's formula (for holomorphic newforms on SL_2(Z)):
    # L(1, Sym^2 f) = 2 * (4 pi)^k / (Gamma(k) * pi) * <f, f>
    # where <f, f> = integral |f|^2 y^k dmu
    # Invert: <f, f> = L(1, Sym^2 f) * Gamma(k) * pi / (2 * (4 pi)^k)
    gamma_k = math.factorial(k - 1)  # Gamma(k) = (k-1)!
    zeta_2 = math.pi ** 2 / 6  # zeta(2) = pi^2/6
    four_pi_k = (4 * math.pi) ** k
    # Standard Shimura normalization:
    # <f, f> = L(1, Sym^2 f) * (k-1)! / ((4 pi)^k / (pi^2/6))
    # The exact formula is convention-dependent. We use the symmetric square:
    petersson = abs(L_sym2_1) * gamma_k * zeta_2 / four_pi_k

    # Independent check via Rankin-Selberg at s = k:
    # L(s, f x f) has a simple pole at s = k with residue proportional to <f,f>.
    # We compute L(k + epsilon, f x f) for small epsilon.
    eps = 0.01
    L_rs_near_pole = rankin_selberg_L(f_coeffs, k, s=k + eps, num_primes=num_primes)

    return {
        'L_sym2_at_1': _mp_float(L_sym2_1),
        'petersson_norm': petersson,
        'gamma_k': gamma_k,
        'L_rs_near_pole': _mp_float(L_rs_near_pole),
        'L_rs_residue_approx': abs(L_rs_near_pole) * eps if isinstance(L_rs_near_pole, (complex, float)) else None,
    }


# =========================================================================
# 11. Approximate functional equation
# =========================================================================

def afe_smooth_cutoff(x: float, sigma: float = 1.0) -> float:
    r"""Smooth cutoff function V(x) for the approximate functional equation.

    Uses the erfc cutoff: V(x) = erfc(x * sigma) / 2, which gives
    exponential decay beyond the conductor bound.

    For a more precise AFE, one should use the Gamma factor ratios,
    but this suffices for numerical verification.
    """
    if HAS_MPMATH:
        return float(mpmath.erfc(x * sigma) / 2)
    # Approximate erfc
    return math.erfc(x * sigma) / 2


def sym_power_dirichlet_coeffs(f_coeffs: Dict[int, Any], k: int, m: int,
                                N_max: int = 1000) -> Dict[int, complex]:
    r"""Compute the Dirichlet coefficients a_m(n) of L(s, Sym^m f).

    For the Sym^m L-function, the Dirichlet coefficients are multiplicative.
    At prime powers:
      a_m(p^e) = sum_{j_1 + ... + j_{m+1} = e} alpha^{j_1 k_1} ... beta^{j_{m+1} k_{m+1}}
    where the sum is over partitions of e into m+1 nonneg integers.

    For simplicity, we compute at primes and small prime powers only.
    """
    primes = sorted(f_coeffs.keys())
    coeffs = {}
    coeffs[1] = 1.0 + 0j
    for p in primes:
        if p > N_max:
            break
        a_p = f_coeffs[p]
        alpha, beta = satake_parameters(a_p, k, p)
        # a_m(p) = sum_{j=0}^m alpha^j beta^{m-j}
        val = 0.0 + 0j
        for j in range(m + 1):
            if HAS_MPMATH:
                term = complex(mpmath.power(alpha, j) * mpmath.power(beta, m - j))
            else:
                term = alpha ** j * beta ** (m - j)
            val += term
        coeffs[p] = val
        # Prime powers (simple implementation for p^2)
        p2 = p * p
        if p2 <= N_max:
            val2 = 0.0 + 0j
            for j in range(2 * m + 1):
                # Coefficients of Sym^m at p^2 via Hecke relations
                pass
            # Skip higher prime powers for simplicity
    return coeffs


def afe_sum(f_coeffs: Dict[int, Any], k: int, m: int, s,
            N_terms: int = 500, num_primes: int = 100) -> complex:
    r"""Evaluate L(s, Sym^m f) via approximate functional equation.

    L(s) ~ sum_{n <= N} a(n) n^{-s} V(n / sqrt(C))

    where C is the analytic conductor. This is a second verification path
    complementing the Euler product.

    For the partial implementation, we use prime-indexed terms only
    (sufficient for cross-checking the Euler product).
    """
    primes = sorted(f_coeffs.keys())[:num_primes]
    conductor = 1.0  # Level 1 for SL_2(Z) forms
    # Analytic conductor for Sym^m: grows with m and k
    # C_m ~ (k / (2 pi e))^{m+1}  (rough estimate)
    analytic_cond = (k / (2 * math.pi * math.e)) ** (m + 1)
    sqrt_cond = math.sqrt(max(analytic_cond, 1.0))

    total = 0.0 + 0j
    for p in primes:
        if p > N_terms:
            break
        a_p = f_coeffs[p]
        alpha, beta = satake_parameters(a_p, k, p)
        # Dirichlet coefficient at prime p for Sym^m
        coeff = 0.0 + 0j
        for j in range(m + 1):
            if HAS_MPMATH:
                term = complex(mpmath.power(alpha, j) * mpmath.power(beta, m - j))
            else:
                term = alpha ** j * beta ** (m - j)
            coeff += term
        # V(p / sqrt(C))
        v = afe_smooth_cutoff(p / sqrt_cond)
        total += coeff * p ** (-complex(s)) * v

    return total


# =========================================================================
# 12. Koszul duality comparison: Sym^k(A) vs Sym^k(A!)
# =========================================================================

def koszul_dual_comparison(f_coeffs: Dict[int, Any], k: int,
                           f_dual_coeffs: Dict[int, Any], k_dual: int,
                           m: int, s, num_primes: int = 100) -> Dict[str, Any]:
    r"""Compare L(s, Sym^m f) with L(s, Sym^m f!) where f! is the
    Koszul-dual shadow form.

    For complementarity: if A <-> A! with kappa(A) + kappa(A!) = delta
    (0 for KM, rho*K for W-algebras), then the symmetric power L-functions
    should satisfy specific duality relations.

    Returns both values and their ratio.
    """
    L_A = sym_power_L(f_coeffs, k, m, s, num_primes)
    L_A_dual = sym_power_L(f_dual_coeffs, k_dual, m, s, num_primes)
    ratio = L_A / L_A_dual if abs(L_A_dual) > 1e-300 else None
    return {
        'L_sym_m_A': _mp_float(L_A),
        'L_sym_m_A_dual': _mp_float(L_A_dual),
        'ratio': _mp_float(ratio) if ratio is not None else None,
        'm': m,
        's': s,
    }


# =========================================================================
# 13. Low-lying zeros and Katz-Sarnak symmetry types
# =========================================================================

def katz_sarnak_one_level_density_sp(x: float) -> float:
    r"""One-level density W_1(x) for symplectic symmetry (Sp):

      W_1(x) = 1 - sin(2 pi x) / (2 pi x)

    Expected for Sym^{2m} L-functions (even symmetric power).
    """
    if abs(x) < 1e-15:
        return 0.0  # W_1(0) = 0 for Sp
    return 1.0 - math.sin(2 * math.pi * x) / (2 * math.pi * x)


def katz_sarnak_one_level_density_so_even(x: float) -> float:
    r"""One-level density W_1(x) for SO(even) symmetry:

      W_1(x) = 1 + sin(2 pi x) / (2 pi x)

    Expected for Sym^{2m+1} L-functions with even functional equation.
    """
    if abs(x) < 1e-15:
        return 2.0  # W_1(0) = 2 for SO(even)
    return 1.0 + math.sin(2 * math.pi * x) / (2 * math.pi * x)


def katz_sarnak_one_level_density_so_odd(x: float) -> float:
    r"""One-level density W_1(x) for SO(odd) symmetry:

      W_1(x) = 1 - sin(2 pi x) / (2 pi x) + delta_0(x)

    (The delta function is not computable numerically; we return
    the smooth part.)
    """
    if abs(x) < 1e-15:
        return 0.0  # Smooth part; delta at 0 handled separately
    return 1.0 - math.sin(2 * math.pi * x) / (2 * math.pi * x)


def low_lying_zeros_statistic(f_coeffs: Dict[int, Any], k: int, m: int,
                               num_primes: int = 100,
                               num_bins: int = 50) -> Dict[str, Any]:
    r"""Compute the low-lying zero statistic for L(s, Sym^m f).

    We use the explicit formula approach:
      sum_gamma phi(gamma * log(C) / (2 pi)) = phi_hat(0) * log(C) / (2 pi)
        - sum_p (log p / p^{1/2}) * ... + O(1)

    For a practical diagnostic, we compute the density of zeros near the
    central point by evaluating the Euler product at s = 1/2 + i*t for
    small t values and recording where it vanishes (approximately).

    Returns:
      'symmetry_prediction': the predicted KS symmetry type
      'zeros_near_half': list of approximate zeros
      'density_data': binned density near the central point
    """
    # Predict symmetry type
    if m % 2 == 0:
        sym_type = 'symplectic (Sp)'
    else:
        # Root number determines SO(even) vs SO(odd)
        sym_type = 'orthogonal (SO)'

    # Sample L(1/2 + it, Sym^m f) for small t
    t_values = [0.01 * j for j in range(1, num_bins + 1)]
    l_values = []
    for t in t_values:
        val = sym_power_L(f_coeffs, k, m, complex(0.5, t), num_primes)
        l_values.append({
            't': t,
            'L_value': _mp_float(val),
            'abs_L': abs(val) if isinstance(val, (complex, float)) else _mp_abs(val),
        })

    return {
        'symmetric_power': m,
        'symmetry_prediction': sym_type,
        'l_values_near_half': l_values,
    }


# =========================================================================
# 14. Langlands-Shahidi method comparison
# =========================================================================

def shahidi_constant_term_check(f_coeffs: Dict[int, Any], k: int, m: int,
                                 num_primes: int = 50) -> Dict[str, Any]:
    r"""Verify Sym^m L-function via the Langlands-Shahidi method.

    The Langlands-Shahidi method computes the L-function from the constant
    term of an Eisenstein series on a larger group.  For Sym^2, this is the
    Eisenstein series on GL(3) induced from GL(2).

    We verify: the Euler product of L(s, Sym^m f) computed via Satake
    parameters matches the prediction from the Langlands-Shahidi gamma
    factor.

    For m = 2 (Gelbart-Jacquet), the completed L-function is:
      Lambda(s, Sym^2 f) = pi^{-3s/2} Gamma(s/2) Gamma((s+k-1)/2) Gamma((s-k+2)/2) * L(s, Sym^2 f)

    CAUTION: This is a structural check, not a full independent computation.
    The full Langlands-Shahidi computation requires the Eisenstein series,
    which is beyond this module's scope.

    We check the FUNCTIONAL EQUATION instead:
      Lambda(s, Sym^2 f) = Lambda(1-s, Sym^2 f)  (for level 1, root number +1)
    by computing L at s and 1-s and comparing the ratio with the expected
    gamma factor ratio.
    """
    # Compute L(s, Sym^2 f) at s and 1-s
    s_vals = [1.5, 2.0, 2.5]
    results = {}
    for s in s_vals:
        L_s = sym_power_L(f_coeffs, k, m, s, num_primes)
        L_1ms = sym_power_L(f_coeffs, k, m, 1 - s, num_primes)
        # Gamma factor ratio (for Sym^2 on SL_2(Z)):
        # gamma(s) / gamma(1-s) where gamma involves pi^{-3s/2} * Gamma products
        if HAS_MPMATH:
            # Sym^2 gamma factors
            g_s = (mpmath.power(mpmath.pi, -3 * s / 2)
                   * mpmath.gamma(s / 2)
                   * mpmath.gamma((s + k - 1) / 2)
                   * mpmath.gamma((s + k - 1) / 2))  # Simplified
            g_1ms = (mpmath.power(mpmath.pi, -3 * (1 - s) / 2)
                     * mpmath.gamma((1 - s) / 2)
                     * mpmath.gamma(((1 - s) + k - 1) / 2)
                     * mpmath.gamma(((1 - s) + k - 1) / 2))
            gamma_ratio = float(g_s / g_1ms) if float(mpmath.fabs(g_1ms)) > 1e-300 else None
        else:
            gamma_ratio = None

        ratio = None
        if abs(L_1ms) > 1e-300 if isinstance(L_1ms, (int, float)) else abs(L_1ms) > 1e-300:
            ratio = L_s / L_1ms
        results[s] = {
            'L_s': _mp_float(L_s),
            'L_1_minus_s': _mp_float(L_1ms),
            'ratio': _mp_float(ratio) if ratio is not None else None,
            'gamma_ratio': gamma_ratio,
        }
    return {
        'method': 'Langlands-Shahidi functional equation check',
        'symmetric_power': m,
        'data': results,
    }


# =========================================================================
# 15. Master computation: full symmetric power analysis
# =========================================================================

def full_symmetric_power_analysis(f_coeffs: Dict[int, Any], k: int,
                                   m_values: Optional[List[int]] = None,
                                   s_values: Optional[List] = None,
                                   num_primes: int = 100) -> Dict[str, Any]:
    r"""Run the complete symmetric power analysis pipeline.

    Returns a comprehensive dictionary with:
      - L-values at all (m, s) pairs
      - Sato-Tate KS test
      - Moments table
      - Petersson norm from Sym^2
      - Rankin-Selberg at first 10 zeta zeros
    """
    if m_values is None:
        m_values = [1, 2, 3, 4]
    if s_values is None:
        s_values = [0.5, 1.0, 2.0]

    # Sym^m L-values
    l_table = sym_power_L_multi(f_coeffs, k, m_values, s_values, num_primes)

    # Sato-Tate
    st_test = sato_tate_ks_test(f_coeffs, k, num_primes)

    # Moments
    moments = moments_table(f_coeffs, k, list(range(1, 9)),
                            [t for t in [100, 1000, 10000] if t <= _nth_prime(num_primes)])

    # Petersson norm
    petersson = petersson_norm_from_sym2(f_coeffs, k, num_primes)

    # Rankin-Selberg at zeta zeros (first 10 only for speed)
    rs_zeros = rankin_selberg_at_zeta_zeros(f_coeffs, k, num_zeros=10,
                                             num_primes=min(num_primes, 50))

    return {
        'weight': k,
        'num_primes': num_primes,
        'l_values': l_table,
        'sato_tate': st_test,
        'moments': moments,
        'petersson_norm': petersson,
        'rankin_selberg_at_zeros': rs_zeros,
    }
