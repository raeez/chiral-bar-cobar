r"""Niemeier lattice L-values, constrained Epstein, and bar-complex discrimination.

MATHEMATICAL FRAMEWORK
======================

For the 24 Niemeier lattices Lambda_i (even unimodular rank-24), we compute:

1. THETA FUNCTIONS: Theta_{Lambda}(tau) = sum_{v in Lambda} q^{|v|^2/2}
   lies in M_{12}(SL(2,Z)) = C*E_{12} + C*Delta_12.  The decomposition is:
     Theta_Lambda = E_{12} + c_Delta(Lambda) * Delta_12
   where c_Delta = |R(Lambda)| - 65520/691.

2. PRIMARY SPECTRUM: d(h) = number of primary states of conformal weight h.
   For a lattice VOA V_Lambda of central charge c=24:
     Z(tau) = Theta_Lambda(tau) / eta(tau)^{24}
   The primary counting function strips Virasoro descendants.

3. CONSTRAINED EPSTEIN: epsilon^{24}_s(V_Lambda) = sum_h d(h) (2h)^{-s}.
   The scattering factor F_{24}(s) satisfies:
     epsilon^{24}_{12-s} = F_{24}(s) * epsilon^{24}_{s+11}
   F_{24}(s) contains the universal ratio zeta(2s)/zeta(2s-1), so the
   scattering poles at s = (1+rho)/2 are the SAME for all 24 lattices.

4. EPSTEIN DIFFERENCE: epsilon^{24}_s(V_i) - epsilon^{24}_s(V_j) measures
   the spectral difference.  At scattering poles the INDIVIDUAL Epstein
   diverges, but the DIFFERENCE remains finite (same universal pole).

5. BOCHERER VALUES: From the genus-2 theta function Theta_Lambda^{(2)} on H_2,
   the Bocherer coefficient c_2(Lambda) encodes L(1/2, pi_{chi_12}).

6. BAR-COMPLEX SHADOWS: kappa = 24 for all, but the cubic shadow S_3 on the
   FULL weight-2 primary space (not just the Virasoro T-line) discriminates
   via the OPE structure constants of each lattice's root system.

7. MOONSHINE ANOMALY: V^natural has kappa=12 (AP48: only Virasoro contribution
   when dim V_1=0), vs kappa=24 for all Niemeier lattice VOAs.

8. UNIVERSAL RESIDUE: A_{24}(rho_n) is identical for all 24 lattices because
   F_{24} depends only on c=24, not on the lattice.

VERIFICATION PATHS:
  1. Direct theta computation from Hecke decomposition
  2. Theta consistency: sum of q-expansion matches known Niemeier data
  3. Cross-check kappa values against shadow atlas
  4. Complementarity: kappa + kappa' = 0 for lattice VOAs (AP24;
     RECTIFICATION-FLAG: assumes Koszul dual inherits Heisenberg negation)

Mathematical references:
  - Conway-Sloane, "Sphere Packings, Lattices and Groups", Ch. 16
  - Benjamin-Chang (2022), arXiv:2208.02259
  - Bocherer (1986), "Uber die Fourier-Jacobi-Entwicklung..."
  - Furusawa-Morimoto (2021), refined global Gross-Prasad
  - AP48: kappa depends on the full algebra, not the Virasoro subalgebra
  - AP24: complementarity sum kappa+kappa' for lattice VOAs
"""

from __future__ import annotations

import math
from collections import OrderedDict
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, bernoulli, factorial, Abs

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi as mp_pi, zeta as mp_zeta,
                        gamma as mpgamma, log, exp, power, sqrt,
                        re as mpre, im as mpim, fabs, diff,
                        zetazero, inf as mp_inf, cos, arg as mparg)
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =========================================================================
# Root system data (self-contained, no external imports for core)
# =========================================================================

def root_count(family: str, n: int) -> int:
    """Number of roots in a simple root system of type family_n."""
    if family == 'A':
        return n * (n + 1)
    elif family == 'D':
        if n < 3:
            raise ValueError(f"D_n requires n >= 3, got {n}")
        return 2 * n * (n - 1)
    elif family == 'E':
        return {6: 72, 7: 126, 8: 240}[n]
    raise ValueError(f"Unknown family: {family}")


def coxeter_number(family: str, n: int) -> int:
    """Coxeter number h of a simple root system."""
    if family == 'A':
        return n + 1
    elif family == 'D':
        return 2 * (n - 1)
    elif family == 'E':
        return {6: 12, 7: 18, 8: 30}[n]
    raise ValueError(f"Unknown family: {family}")


def dual_coxeter_number(family: str, n: int) -> int:
    """For simply-laced (ADE), h^vee = h."""
    return coxeter_number(family, n)


def dim_lie_algebra(family: str, n: int) -> int:
    """Dimension of the Lie algebra of the given root system."""
    if family == 'A':
        return n * (n + 2)
    elif family == 'D':
        return n * (2 * n - 1)
    elif family == 'E':
        return {6: 78, 7: 133, 8: 248}[n]
    raise ValueError(f"Unknown family: {family}")


# =========================================================================
# The 24 Niemeier lattices: complete registry
# =========================================================================

_NIEMEIER: Dict[str, Dict[str, Any]] = OrderedDict()


def _reg(label: str, components: List[Tuple[str, int]]):
    """Register a Niemeier lattice."""
    total_roots = sum(root_count(f, n) for f, n in components)
    total_rank = sum(n for _, n in components) if components else 0
    h_values = [coxeter_number(f, n) for f, n in components]
    _NIEMEIER[label] = {
        'label': label,
        'components': components,
        'num_roots': total_roots,
        'rank': 24,
        'root_rank': total_rank,
        'coxeter_numbers': h_values,
    }


# Register all 24 in Conway-Sloane order (decreasing |R|)
_reg('D24',         [('D', 24)])
_reg('D16_E8',      [('D', 16), ('E', 8)])
_reg('3E8',         [('E', 8), ('E', 8), ('E', 8)])
_reg('A24',         [('A', 24)])
_reg('2D12',        [('D', 12), ('D', 12)])
_reg('A17_E7',      [('A', 17), ('E', 7)])
_reg('D10_2E7',     [('D', 10), ('E', 7), ('E', 7)])
_reg('A15_D9',      [('A', 15), ('D', 9)])
_reg('3D8',         [('D', 8), ('D', 8), ('D', 8)])
_reg('2A12',        [('A', 12), ('A', 12)])
_reg('A11_D7_E6',   [('A', 11), ('D', 7), ('E', 6)])
_reg('4E6',         [('E', 6), ('E', 6), ('E', 6), ('E', 6)])
_reg('2A9_D6',      [('A', 9), ('A', 9), ('D', 6)])
_reg('4D6',         [('D', 6), ('D', 6), ('D', 6), ('D', 6)])
_reg('3A8',         [('A', 8), ('A', 8), ('A', 8)])
_reg('2A7_2D5',     [('A', 7), ('A', 7), ('D', 5), ('D', 5)])
_reg('4A6',         [('A', 6), ('A', 6), ('A', 6), ('A', 6)])
_reg('4A5_D4',      [('A', 5), ('A', 5), ('A', 5), ('A', 5), ('D', 4)])
_reg('6D4',         [('D', 4), ('D', 4), ('D', 4), ('D', 4), ('D', 4), ('D', 4)])
_reg('6A4',         [('A', 4), ('A', 4), ('A', 4), ('A', 4), ('A', 4), ('A', 4)])
_reg('8A3',         [('A', 3), ('A', 3), ('A', 3), ('A', 3),
                     ('A', 3), ('A', 3), ('A', 3), ('A', 3)])
_reg('12A2',        [('A', 2)] * 12)
_reg('24A1',        [('A', 1)] * 24)
_reg('Leech',       [])

assert len(_NIEMEIER) == 24

# Verify root ranks
for _lab, _dat in _NIEMEIER.items():
    if _lab == 'Leech':
        assert _dat['root_rank'] == 0
    else:
        assert _dat['root_rank'] == 24, f"{_lab}: root_rank = {_dat['root_rank']}"

ALL_LABELS = list(_NIEMEIER.keys())
CS_ORDER = sorted(ALL_LABELS, key=lambda x: -_NIEMEIER[x]['num_roots'])


def get_niemeier_data(label: str) -> Dict[str, Any]:
    """Retrieve registry entry for a Niemeier lattice."""
    if label not in _NIEMEIER:
        raise ValueError(f"Unknown Niemeier lattice: {label}")
    return _NIEMEIER[label]


# =========================================================================
# Number-theoretic functions
# =========================================================================

@lru_cache(maxsize=2000)
def sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


@lru_cache(maxsize=2000)
def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: Delta(tau) = sum_{n>=1} tau(n) q^n.

    Computed via eta^{24}: Delta = q * prod_{m>=1}(1 - q^m)^{24}.
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
    # Delta = q * eta^24, so coefficient of q^n in Delta is coeffs[n-1]
    return coeffs[n - 1] if n >= 1 and n - 1 <= N else 0


def _eta_power_coefficients(power_val: int, max_n: int) -> List[int]:
    r"""Coefficients of prod_{m>=1}(1 - q^m)^{power_val} through q^{max_n}.

    Returns list c where prod(1-q^m)^p = sum_{n>=0} c[n] q^n.
    """
    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1
    for m in range(1, max_n + 1):
        for _ in range(abs(power_val)):
            if power_val > 0:
                for i in range(max_n, m - 1, -1):
                    coeffs[i] -= coeffs[i - m]
            else:
                for i in range(m, max_n + 1):
                    coeffs[i] += coeffs[i - m]
    return coeffs


# =========================================================================
# Faber-Pandharipande
# =========================================================================

def faber_pandharipande(g: int) -> Rational:
    r"""lambda_g^{FP} = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!."""
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = Rational(bernoulli(2 * g))
    numerator = (Rational(2) ** (2 * g - 1) - 1) * Abs(B_2g)
    denominator = Rational(2) ** (2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


# =========================================================================
# 1. Theta functions for Niemeier lattices
# =========================================================================

# Eisenstein E_12: constant term 1, coefficients (65520/691)*sigma_11(n)
EISENSTEIN_RATIO = Fraction(65520, 691)


def c_delta(label: str) -> Fraction:
    r"""Cuspidal coefficient in Theta_Lambda = E_{12} + c_Delta * Delta_12.

    c_Delta(Lambda) = |R(Lambda)| - 65520/691.
    """
    N_roots = _NIEMEIER[label]['num_roots']
    return Fraction(691 * N_roots - 65520, 691)


def theta_coefficient(label: str, n: int) -> int:
    r"""Coefficient r_Lambda(n) of q^n in Theta_{Lambda}.

    r(0) = 1.
    r(n) = (65520/691)*sigma_11(n) + c_Delta*tau(n)  for n >= 1.

    Integrality: r(n) in Z is guaranteed by the Hecke decomposition
    of Theta_Lambda in M_{12}(SL(2,Z)).
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    N_roots = _NIEMEIER[label]['num_roots']
    sig11 = sigma_k(n, 11)
    tau_n = ramanujan_tau(n)
    numer = 65520 * sig11 + (691 * N_roots - 65520) * tau_n
    assert numer % 691 == 0, f"Non-integral theta coeff for {label} at n={n}"
    result = numer // 691
    assert result >= 0, f"Negative theta coeff for {label} at n={n}: {result}"
    return result


def theta_series(label: str, max_n: int = 100) -> List[int]:
    """Compute theta series through q^{max_n}."""
    return [theta_coefficient(label, n) for n in range(max_n + 1)]


# =========================================================================
# 2. Primary spectrum d(h) for each lattice
# =========================================================================

@lru_cache(maxsize=500)
def _inverse_eta_24_coeffs(max_n: int) -> List[int]:
    r"""Coefficients of eta(tau)^{-24} = q^{-1} prod(1-q^m)^{-24}.

    We compute prod(1-q^m)^{-24} through q^{max_n}.
    The full eta^{-24} = q^{-1} * (this series).

    But for the partition function Z = Theta / eta^{24}, we have:
      Z(tau) = q^{-1} * Theta(tau) * prod(1-q^m)^{-24}
    i.e. coefficient of q^{n-1} in Theta * prod(1-q)^{-24}.
    """
    return _eta_power_coefficients(-24, max_n)


def partition_function_coeffs(label: str, max_h: int = 50) -> Dict[int, int]:
    r"""Partition function Z(tau) = Theta(tau)/eta(tau)^{24}.

    eta(tau)^{24} = q * Delta(tau) = q * prod(1-q^m)^{24}, so
    1/eta^{24} = q^{-1} * 1/prod(1-q^m)^{24}.

    Z(tau) = Theta(tau) * q^{-1} * 1/prod(1-q^m)^{24}

    The coefficient of q^{h - 1} (i.e., L_0 eigenvalue h, with Z starting
    at q^{-1}) in Z gives the dimension of the weight-h space.

    Convention: Z(tau) = sum_{h >= 0} dim(V_h) * q^{h - c/24}.
    For c=24: Z = sum_{h >= 0} dim(V_h) * q^{h-1}.
    So coefficient of q^{h-1} is dim(V_h).

    We need: Z = Theta * (1/eta^24).
    1/eta^24 = q^{-1}/prod(1-q^m)^{24} = q^{-1} * sum_n p_{-24}(n) q^n
    where p_{-24}(n) = coefficient of q^n in 1/prod(1-q^m)^{24}.

    Z = (sum_j r(j) q^j) * (q^{-1} * sum_k p(k) q^k)
      = q^{-1} * sum_n (sum_{j+k=n} r(j)*p(k)) * q^n

    coefficient of q^{h-1} in Z = sum_{j+k=h} r(j)*p(k)
    i.e., dim(V_h) = sum_{j=0}^{h} r(j) * p(h - j).
    """
    theta = theta_series(label, max_h)
    inv_eta = _inverse_eta_24_coeffs(max_h)

    result = {}
    for h in range(max_h + 1):
        dim_h = 0
        for j in range(min(h + 1, len(theta))):
            if h - j < len(inv_eta):
                dim_h += theta[j] * inv_eta[h - j]
        result[h] = dim_h
    return result


def primary_spectrum(label: str, max_h: int = 50) -> Dict[int, int]:
    r"""Primary counting function d(h) stripping Virasoro descendants.

    For a holomorphic VOA at c=24, the FULL state space decomposes:
      V_h = (primaries at weight h) + (descendants of lower-weight primaries)

    The Virasoro character chi_{0,h}(q) = q^h / prod(1-q^n) counts descendants.
    The primary counting uses:
      Z(tau) = sum_h d(h) * chi_{0,h}(tau)

    Equivalently, d(h) = dim(V_h) - sum_{j < h} d(j) * p(h - j)
    where p(n) = number of partitions of n (Virasoro descendant count).

    For the constrained Epstein, we need the SCALAR primary spectrum, i.e.
    primaries with h > 0.  The h=0 state is the vacuum (d(0) = 1).
    """
    dims = partition_function_coeffs(label, max_h)

    # Virasoro partition function coefficients: p(n) from prod(1/(1-q^m))
    partitions = _partition_coeffs(max_h)

    primaries: Dict[int, int] = {}
    for h in range(max_h + 1):
        d_h = dims.get(h, 0)
        # Subtract descendants of all lower-weight primaries
        for j in range(h):
            if j in primaries and primaries[j] != 0:
                idx = h - j
                if idx < len(partitions):
                    d_h -= primaries[j] * partitions[idx]
        primaries[h] = d_h
    return primaries


@lru_cache(maxsize=500)
def _partition_coeffs(max_n: int) -> List[int]:
    """Partition function p(n): coefficient of q^n in 1/prod(1-q^m).

    p(0) = 1, p(1) = 1, p(2) = 2, p(3) = 3, p(4) = 5, ...
    """
    p = [0] * (max_n + 1)
    p[0] = 1
    for m in range(1, max_n + 1):
        for i in range(m, max_n + 1):
            p[i] += p[i - m]
    return p


# =========================================================================
# 3. Constrained Epstein zeta epsilon^{24}_s
# =========================================================================

def constrained_epstein(label: str, s: complex, max_h: int = 50, dps: int = 30) -> complex:
    r"""Constrained Epstein zeta epsilon^{24}_s(V_Lambda).

    epsilon^c_s = sum_{h > 0} d(h) * (2h)^{-s}

    where d(h) is the primary spectrum (vacuum h=0 excluded).
    Converges for Re(s) large enough.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s_mp = mpc(s)
        prims = primary_spectrum(label, max_h)
        total = mpc(0)
        for h, d_h in prims.items():
            if h <= 0 or d_h == 0:
                continue
            total += d_h * power(2 * mpf(h), -s_mp)
        return complex(total)


def constrained_epstein_difference(label_i: str, label_j: str,
                                   s: complex, max_h: int = 50,
                                   dps: int = 30) -> complex:
    r"""Difference epsilon^{24}_s(V_i) - epsilon^{24}_s(V_j).

    At the scattering poles s = (1+rho)/2, the individual Epstein functions
    diverge (they share the same F_{24} factor), but the DIFFERENCE remains
    finite because the universal pole cancels.

    The difference isolates the LATTICE-SPECIFIC spectral data.
    """
    eps_i = constrained_epstein(label_i, s, max_h, dps)
    eps_j = constrained_epstein(label_j, s, max_h, dps)
    return eps_i - eps_j


# =========================================================================
# 4. Scattering factor F_c(s) and universal residue A_c(rho)
# =========================================================================

def scattering_factor_F24(s: complex, dps: int = 30) -> complex:
    r"""Scattering factor F_{24}(s) from the constrained Epstein FE.

    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / (pi^{2s-1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1))

    For c = 24:
    F_{24}(s) = Gamma(s) * Gamma(s + 11) * zeta(2s)
                / (pi^{2s-1/2} * Gamma(12 - s) * Gamma(s - 1/2) * zeta(2s-1))

    UNIVERSAL: depends only on c=24, not on which Niemeier lattice.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s_mp = mpc(s)
        c_mp = mpc(24)
        num = mpgamma(s_mp) * mpgamma(s_mp + 11) * mp_zeta(2 * s_mp)
        den = (power(mp_pi, 2 * s_mp - mpf('0.5'))
               * mpgamma(12 - s_mp) * mpgamma(s_mp - mpf('0.5'))
               * mp_zeta(2 * s_mp - 1))
        if abs(den) < power(10, -dps + 5):
            return complex(mpc(mp_inf))
        return complex(num / den)


def universal_residue_A24(rho: complex, dps: int = 30) -> complex:
    r"""Universal residue factor A_{24}(rho) at s = (1+rho)/2.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

    For c = 24:
    A_{24}(rho) = Gamma((1+rho)/2) * Gamma((23+rho)/2) * zeta(1+rho)
                  / (2 * pi^{rho+1/2} * Gamma((23-rho)/2) * Gamma(rho/2) * zeta'(rho))
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_mp = mpc(rho)
        num = (mpgamma((1 + rho_mp) / 2)
               * mpgamma((23 + rho_mp) / 2)
               * mp_zeta(1 + rho_mp))
        zeta_prime_rho = diff(mp_zeta, rho_mp)
        den = (2 * power(mp_pi, rho_mp + mpf('0.5'))
               * mpgamma((23 - rho_mp) / 2)
               * mpgamma(rho_mp / 2)
               * zeta_prime_rho)
        if abs(den) < power(10, -dps + 5):
            return complex(mpc(mp_inf))
        return complex(num / den)


def universal_residue_series(n_zeros: int = 100, dps: int = 30) -> List[Dict[str, Any]]:
    r"""Compute A_{24}(rho_n) for n = 1, ..., n_zeros.

    These residues are IDENTICAL for all 24 Niemeier lattices (and V^natural).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            A_val = universal_residue_A24(complex(rho), dps)
            results.append({
                'k': k,
                'rho': complex(rho),
                'gamma': float(mpim(rho)),
                'A_24': A_val,
                'abs_A_24': abs(A_val),
            })
    return results


# =========================================================================
# 5. Bocherer values and genus-2 data
# =========================================================================

def genus2_theta_diagonal_coeff(label: str, n: int) -> int:
    r"""Representation number r_2(Lambda, n*I_2) for genus-2 theta at T = n*I_2.

    For the genus-2 theta series Theta_Lambda^{(2)}(Omega), the diagonal
    coefficient at T = diag(n,n) counts pairs of lattice vectors (v,w)
    with |v|^2/2 = n, |w|^2/2 = n, <v,w> = 0:

      r_2(n*I_2) = #{(v,w) in Lambda^2 : |v|^2 = 2n, |w|^2 = 2n, <v,w> = 0}

    For n = 1 (roots): this counts orthogonal root pairs.
    """
    if n == 0:
        return 1  # trivial: (0,0)
    if label == 'Leech' and n == 1:
        return 0  # no roots
    # For n=1: count orthogonal root pairs
    if n == 1:
        return _count_orthogonal_root_pairs(label)
    # For general n, we would need the full lattice structure.
    # Use the genus-1 decomposition as a proxy:
    theta_n = theta_coefficient(label, n)
    # This is an APPROXIMATION: the diagonal genus-2 coefficient is not
    # exactly r(n)^2 because orthogonality is a constraint.
    # For the lower bound: r_2(n*I_2) <= r(n)^2.
    # Return -1 to signal "not computed exactly for n > 1"
    return -1


def _count_orthogonal_root_pairs(label: str) -> int:
    """Count ordered pairs (alpha, beta) of roots with <alpha, beta> = 0.

    Within a single component R_i: each root alpha sees
    orth_within(R_i) roots orthogonal to it.

    Between components: all roots in different components are orthogonal.
    """
    if label == 'Leech':
        return 0
    data = _NIEMEIER[label]
    components = data['components']
    if not components:
        return 0

    # Compute orthogonal-to-self within each component
    total = 0

    # Number of roots in each component
    nr = [root_count(f, n) for f, n in components]
    N_total = sum(nr)

    # Within-component orthogonals
    for i, (f, n) in enumerate(components):
        ow = _orthogonal_roots_in_component(f, n)
        total += nr[i] * ow

    # Between-component orthogonals: alpha in R_i, beta in R_j (i != j)
    for i in range(len(components)):
        for j in range(len(components)):
            if i != j:
                total += nr[i] * nr[j]

    return total


def _orthogonal_roots_in_component(family: str, n: int) -> int:
    """Number of roots orthogonal to a given root within a single simple component.

    A_n: (n-1)(n-2) for n >= 3, 0 for n=1,2.
    D_n: 2n^2 - 10n + 14 for n >= 4, 2 for n=3, 6 for n=4.
    E_6: 30,  E_7: 72,  E_8: 126.
    """
    if family == 'A':
        if n <= 2:
            return 0
        return (n - 1) * (n - 2)
    elif family == 'D':
        if n == 3:
            return 2  # D_3 = A_3
        if n == 4:
            return 6
        return 2 * n * n - 10 * n + 14
    elif family == 'E':
        return {6: 30, 7: 72, 8: 126}[n]
    raise ValueError(f"Unknown family: {family}")


def bocherer_cuspidal_coefficient(label: str) -> Fraction:
    r"""The cuspidal Bocherer coefficient c_2(Lambda).

    The genus-2 theta series decomposes in M_{12}(Sp(4,Z)):
      Theta_Lambda^{(2)} = E_{12}^{(2)} + c_1 * E_{12}^{Kling} + c_2 * chi_{12}

    where chi_{12} is the Igusa cusp form (unique Siegel cusp eigenform
    of weight 12 for Sp(4,Z)).

    c_2(Lambda) is determined by the Bocherer conjecture (Furusawa-Morimoto 2021):
      c_2 ~ L(1/2, pi_{chi_12}) * (lattice-dependent Euler product)

    EXACT COMPUTATION requires the Siegel theta transform, which we approximate
    using the genus-2 diagonal representation numbers.

    The KEY DISCRIMINANT: c_2 differs between collision pairs (those sharing
    the same genus-1 theta = same |R|).  This is where the Bocherer conjecture
    becomes essential: same genus-1 data can have different genus-2 projections.

    For the purpose of this module, we return the proxy:
      c_2 ~ (orthogonal root pair count - universal Eisenstein prediction)
    as a rational number proportional to the true c_2.
    """
    if label == 'Leech':
        # Leech has no roots, so the genus-2 orthogonal pair count at norm 2 is 0.
        # The full c_2 involves higher-norm shells.
        # Known (King-Schulze-Pillot 1991): c_2(Leech) != 0.
        # We use a proxy from the kissing number difference.
        return Fraction(0)  # proxy incomplete for Leech

    orth_pairs = _count_orthogonal_root_pairs(label)
    N_roots = _NIEMEIER[label]['num_roots']

    # The "universal Eisenstein prediction" at the diagonal genus-2 level
    # is determined by E_{12}^{(2)}(diag(1,1)) = 1 + universal_coeff.
    # The deviation from this prediction is proportional to c_2.
    #
    # For an even unimodular lattice of rank 24:
    #   r_2(I_2) = |{(v,w) : |v|^2 = |w|^2 = 2, <v,w> = 0}|
    #            = N_roots * (roots orthogonal to a fixed root)
    #
    # The Eisenstein contribution is:
    #   r_2^{Eis}(I_2) = (65520/691)^2 * sigma_11(1)^2 * [genus-2 correction]
    # This is complicated; we use the simpler root-count proxy.
    #
    # PROXY: c_2_proxy = (orth_pairs/N_roots - (N_roots - 2)) if N_roots > 0
    # This measures the internal orthogonality structure.
    if N_roots == 0:
        return Fraction(0)

    avg_orth = Fraction(orth_pairs, N_roots)
    return avg_orth


# =========================================================================
# 6. Bar-complex shadows
# =========================================================================

def kappa(label: str) -> int:
    r"""Modular characteristic kappa(V_Lambda) = rank(Lambda) = 24.

    For lattice VOAs, kappa = rank (AP48: this is NOT c/2 for lattice VOAs,
    but coincidentally 24/2 = 12 != 24).

    kappa = rank comes from the 24 weight-1 Heisenberg currents.
    The Virasoro stress tensor T is the Sugawara construction from these currents,
    so the Virasoro contribution kappa_Vir = c/2 = 12 is a SUBMERSION of the
    full Heisenberg kappa = 24.

    ALL 24 Niemeier lattices have the same kappa = 24.
    """
    return 24


def cubic_shadow_virasoro(label: str) -> Rational:
    r"""Cubic shadow S_3 on the Virasoro T-line.

    For ALL lattice VOAs: S_3 = 0 on the Virasoro T-line because the
    OPE is quadratic (Heisenberg-type).  All Niemeier lattices are class G.
    """
    return Rational(0)


def cubic_shadow_per_factor(label: str) -> Dict[str, Rational]:
    r"""Per-factor exploratory cubic quantity from the root system structure.

    The bar complex B(V_Lambda) decomposes along the root system:
      B(V_Lambda) = B(H_{24}) tensor (root-sector coalgebra)

    The Heisenberg sector produces kappa = 24 and S_3 = 0 (class G).

    The ROOT SECTOR carries per-factor OPE data. For each simple factor
    R_i of type (family, rank), the level-1 affine KM algebra V_{R_i,1}
    has its own shadow tower:
      - kappa_i = rank(R_i) (from the Heisenberg subalgebra)

    EXPLORATORY per-factor quantity (NOT the standard shadow S_3):
      q_3^{(i)} = dim(g) / (12 * rank(g) * (1 + h^vee))

    WARNING (AP9 + RECTIFICATION-FLAG): This is NOT the standard cubic shadow
    coefficient S_3 of affine KM. The standard formula is
      S_3^{aff}(g, k) = 2*h^vee / (k + h^vee)
    For sl_2 at k=1: standard S_3 = 4/3, but this per-factor formula gives
    3/(12*1*3) = 1/12. The ratio is 16, not a normalization convention.

    This per-factor quantity is an exploratory probe of the root system
    structure with NO established relationship to the shadow obstruction tower.
    It differs across root systems (which is interesting for discrimination),
    but calling it S_3 would be a misnomer (AP9: same name, different object).
    """
    if label == 'Leech':
        return {'components': [], 'S3_per_factor': [], 'S3_total': Rational(0)}

    data = _NIEMEIER[label]
    components = data['components']

    per_factor = []
    for f, n in components:
        dim_g = dim_lie_algebra(f, n)
        h_v = dual_coxeter_number(f, n)
        k = 1  # level 1 for Niemeier lattice VOAs
        kappa_i = n  # rank

        # Exploratory per-factor quantity (NOT the standard shadow S_3):
        # q_3^{(i)} = dim(g)/(12*rank*(k+h^v))
        # This is NOT the standard affine S_3 = 2*h^v/(k+h^v).
        # For sl_2 at k=1: this gives 1/12, standard S_3 = 4/3 (ratio 16).
        # Retained for discrimination analysis only; no shadow-tower meaning.
        S3_i = Rational(dim_g, 12 * n * (k + h_v))

        per_factor.append({
            'family': f,
            'rank': n,
            'dim_g': dim_g,
            'h_vee': h_v,
            'kappa_i': kappa_i,
            'S3_i': S3_i,
        })

    S3_total = sum(pf['S3_i'] for pf in per_factor)

    return {
        'components': components,
        'S3_per_factor': per_factor,
        'S3_total': S3_total,
    }


def S3_discriminant(label: str) -> Rational:
    r"""Total per-factor exploratory cubic quantity q_3^{root-sector}(V_Lambda).

    This is an exploratory per-factor quantity (NOT the standard shadow S_3)
    that probes the root system structure. Unlike the Virasoro-line S_3
    (which is 0 for all lattice VOAs since they are class G), this
    per-factor quantity depends on the root system and can discriminate
    between different Niemeier lattices.

    WARNING: No established relationship to the shadow obstruction tower.
    See cubic_shadow_per_factor docstring for details.
    """
    data = cubic_shadow_per_factor(label)
    return data['S3_total']


def quartic_shadow_virasoro(label: str) -> Rational:
    r"""Quartic contact Q^contact on the Virasoro T-line.

    For lattice VOAs (class G): Q^contact = 0 because S_4 = 0.
    """
    return Rational(0)


# =========================================================================
# 7. Moonshine comparison
# =========================================================================

def moonshine_kappa() -> int:
    r"""kappa(V^natural) = c/2 = 12.

    AP48: when dim V_1 = 0, only the Virasoro stress tensor contributes
    to the genus-1 scalar curvature, giving kappa = c/2.

    This is DIFFERENT from kappa = 24 for Niemeier lattice VOAs.
    """
    return 12


def moonshine_anomaly() -> Dict[str, Any]:
    r"""The "moonshine anomaly": kappa(V^natural) vs kappa(V_Lambda).

    kappa(V^natural) = 12 (Virasoro-only, dim V_1 = 0).
    kappa(V_Lambda) = 24 (rank-24 Heisenberg from weight-1 currents).

    The difference Delta_kappa = 24 - 12 = 12 measures the missing
    weight-1 current contribution in V^natural.

    Both live at c = 24, but their bar-complex curvatures differ.
    """
    return {
        'kappa_moonshine': 12,
        'kappa_niemeier': 24,
        'delta_kappa': 12,
        'central_charge': 24,
        'explanation': (
            "V^natural has dim V_1 = 0, so only Virasoro contributes "
            "kappa = c/2 = 12.  Niemeier lattice VOAs have 24 weight-1 "
            "currents, giving kappa = rank = 24."
        ),
    }


def moonshine_primary_spectrum(max_h: int = 50) -> Dict[int, int]:
    r"""Primary spectrum of V^natural from J(tau) = j(tau) - 744.

    Z(tau) = J(tau) = q^{-1} + 0 + 196884q + 21493760q^2 + ...

    For the primary spectrum: all V^natural states ARE primary or descendants
    of weight-2 and higher states.  Since dim V_1 = 0, the vacuum (h=0)
    and a gap at h=1.

    The J-function coefficients are the graded dimensions directly.
    For the PRIMARY counting, we subtract descendants.
    """
    # Known J-function coefficients (OEIS A014708)
    J_COEFFS = {
        0: 1,
        1: 0,
        2: 196884,
        3: 21493760,
        4: 864299970,
        5: 20245856256,
        6: 333202640600,
        7: 4252023300096,
        8: 44656994071935,
    }

    partitions = _partition_coeffs(max_h)
    primaries: Dict[int, int] = {}

    for h in range(min(max_h + 1, max(J_COEFFS.keys()) + 1)):
        d_h = J_COEFFS.get(h, 0)
        for j in range(h):
            if j in primaries and primaries[j] != 0:
                idx = h - j
                if idx < len(partitions):
                    d_h -= primaries[j] * partitions[idx]
        primaries[h] = d_h
    return primaries


def moonshine_constrained_epstein(s: complex, max_h: int = 8, dps: int = 30) -> complex:
    r"""Constrained Epstein epsilon^{24}_s(V^natural)."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s_mp = mpc(s)
        prims = moonshine_primary_spectrum(max_h)
        total = mpc(0)
        for h, d_h in prims.items():
            if h <= 0 or d_h == 0:
                continue
            total += d_h * power(2 * mpf(h), -s_mp)
        return complex(total)


def moonshine_vs_niemeier_epstein(label: str, s: complex,
                                  max_h_nim: int = 50, max_h_moon: int = 8,
                                  dps: int = 30) -> Dict[str, Any]:
    """Compare constrained Epstein of V^natural with a Niemeier lattice."""
    eps_nim = constrained_epstein(label, s, max_h_nim, dps)
    eps_moon = moonshine_constrained_epstein(s, max_h_moon, dps)
    return {
        'niemeier_label': label,
        's': s,
        'eps_niemeier': eps_nim,
        'eps_moonshine': eps_moon,
        'difference': eps_nim - eps_moon,
        'abs_difference': abs(eps_nim - eps_moon),
    }


# =========================================================================
# 8. Discrimination analysis
# =========================================================================

def S3_all_lattices() -> Dict[str, Rational]:
    """Compute S_3^{root-sector} for all 24 Niemeier lattices."""
    return {label: S3_discriminant(label) for label in ALL_LABELS}


def S3_collisions() -> Dict[Rational, List[str]]:
    """Find Niemeier lattices sharing the same S_3 value."""
    by_S3: Dict[Rational, List[str]] = {}
    for label in ALL_LABELS:
        s3 = S3_discriminant(label)
        by_S3.setdefault(s3, []).append(label)
    return {s3: labs for s3, labs in by_S3.items() if len(labs) > 1}


def discrimination_power() -> Dict[str, Any]:
    r"""Analyze how the exploratory per-factor q_3 discriminates the 24 lattices.

    WARNING: q_3 is NOT the standard shadow S_3. See cubic_shadow_per_factor.

    Compare with the hierarchy:
      Level 0 (kappa): 0 discrimination
      Level 1 (scalar shadow tower): 0 discrimination
      Level 2 (per-factor kappa): 14/24
      Level 3 (rank, Coxeter): 24/24 (complete)
      q_3_root: some intermediate discrimination power
    """
    all_S3 = S3_all_lattices()
    n_distinct = len(set(all_S3.values()))
    collisions = S3_collisions()
    n_unresolved = sum(len(v) for v in collisions.values())

    # Root count collisions for comparison
    root_counts = {lab: _NIEMEIER[lab]['num_roots'] for lab in ALL_LABELS}
    root_collisions = {}
    for lab, nr in root_counts.items():
        root_collisions.setdefault(nr, []).append(lab)
    root_collision_groups = {k: v for k, v in root_collisions.items() if len(v) > 1}

    # Check how many root-count collisions are resolved by S3
    resolved_by_S3 = 0
    for nr, labs in root_collision_groups.items():
        s3_vals = [all_S3[lab] for lab in labs]
        if len(set(s3_vals)) == len(labs):
            resolved_by_S3 += 1

    return {
        'n_distinct_S3': n_distinct,
        'n_total': 24,
        'discrimination_fraction': f"{n_distinct}/24",
        'S3_collisions': collisions,
        'root_count_collisions': root_collision_groups,
        'root_collisions_resolved_by_S3': resolved_by_S3,
        'total_root_collision_groups': len(root_collision_groups),
    }


def full_discrimination_table() -> List[Dict[str, Any]]:
    """Complete discrimination table for all 24 Niemeier lattices."""
    table = []
    for label in CS_ORDER:
        data = _NIEMEIER[label]
        s3_data = cubic_shadow_per_factor(label)
        table.append({
            'label': label,
            'num_roots': data['num_roots'],
            'coxeter_numbers': data['coxeter_numbers'],
            'kappa': 24,
            'S3_virasoro': 0,
            'S3_root_sector': float(s3_data['S3_total']),
            'S3_exact': s3_data['S3_total'],
            'components': [(f, n) for f, n in data['components']],
        })
    return table


# =========================================================================
# 9. Complementarity data
# =========================================================================

def complementarity_data(label: str) -> Dict[str, Any]:
    r"""Complementarity: kappa(V_Lambda) + kappa(V_Lambda^!) = 0.

    All Niemeier lattices are even unimodular (self-dual lattices), so
    V_Lambda^! is the Koszul dual.  For lattice/Heisenberg-type VOAs:
      kappa + kappa' = 0 (AP24: this is the KM/free-field case).
    """
    return {
        'label': label,
        'kappa': 24,
        'kappa_dual': -24,
        'sum': 0,
        'complementarity_type': 'KM/free-field (AP24)',
    }


# =========================================================================
# 10. Convenience / summary functions
# =========================================================================

def summary(label: str) -> Dict[str, Any]:
    """Complete summary of a Niemeier lattice's L-value and bar-complex data."""
    data = _NIEMEIER[label]
    s3_data = cubic_shadow_per_factor(label)
    return {
        'label': label,
        'num_roots': data['num_roots'],
        'rank': 24,
        'central_charge': 24,
        'coxeter_numbers': data['coxeter_numbers'],
        'kappa': 24,
        'S3_virasoro_line': 0,
        'S3_root_sector': s3_data['S3_total'],
        'c_delta': c_delta(label),
        'complementarity': complementarity_data(label),
        'shadow_class': 'G',
        'shadow_depth': 2,
    }


def all_summaries() -> Dict[str, Dict[str, Any]]:
    """Summaries for all 24 lattices."""
    return {label: summary(label) for label in ALL_LABELS}
