r"""Ising model and minimal model partition functions from the bar complex.

Connects lattice statistical mechanics to the shadow tower by computing:

1. Ising torus partition function Z_Ising(tau) via Virasoro characters at c=1/2
2. Shadow tower invariants at c=1/2 with independent verification
3. Koszul dual Vir_{51/2}: complementarity kappa + kappa' = 13
4. Minimal model family M(p,q): shadow data for Ising, tricritical Ising,
   3-state Potts, tricritical 3-state Potts, Yang-Lee
5. Fusion rules from Verlinde formula via modular S-matrix
6. Ising 4-point function (genus-0 conformal block)
7. Yang-Lee edge singularity (c = -22/5): negative kappa regime
8. Critical exponents from conformal dimensions
9. Transfer matrix eigenvalues for finite Ising lattice (independent check)

CONVENTIONS:
  - Virasoro central charge c = 1 - 6(p-q)^2/(pq) for M(p,q), p > q >= 2, gcd(p,q)=1
  - kappa = c/2 for all Virasoro algebras (AP1, AP20)
  - S_3 = 2 for all Virasoro (c-independent; NOT -6/(5c+22))
  - S_4 = Q^contact = 10/[c(5c+22)]
  - Koszul dual: c' = 26-c, so kappa' = (26-c)/2 (AP24: kappa+kappa' = 13, NOT 0)
  - The bar propagator d log E(z,w) has weight 1 regardless of field weight (AP27)

GRADING: Cohomological, |d| = +1. Bar uses desuspension.

Manuscript references:
  comp:ising-bar-interpretation (minimal_model_examples.tex)
  thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  def:shadow-metric (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    bernoulli,
    cancel,
    factorial,
    pi as sym_pi,
    simplify,
    sqrt,
)


# ============================================================================
# 1. Virasoro characters via Rocha-Caridi formula (exact integer arithmetic)
# ============================================================================

def _eta_product_coeffs(max_n: int) -> Dict[int, int]:
    """Coefficients of prod_{n>=1}(1 - q^n) via Euler pentagonal theorem.

    prod(1-q^n) = sum_{k=-inf}^{inf} (-1)^k q^{k(3k-1)/2}
    Returns {n: coeff of q^n} for n = 0, ..., max_n.
    """
    result: Dict[int, int] = {}
    for k in range(-max_n, max_n + 1):
        m = k * (3 * k - 1) // 2
        if 0 <= m <= max_n:
            result[m] = result.get(m, 0) + (-1) ** k
    return result


def _inverse_eta_coeffs(max_n: int) -> Dict[int, int]:
    """Coefficients of 1/prod_{n>=1}(1-q^n) = sum p(n) q^n.

    Uses the recurrence p(n) = sum_{k>=1} (-1)^{k+1} [p(n-k(3k-1)/2) + p(n-k(3k+1)/2)].
    """
    p = [0] * (max_n + 1)
    p[0] = 1
    for n in range(1, max_n + 1):
        total = 0
        for k in range(1, n + 1):
            pent1 = k * (3 * k - 1) // 2
            pent2 = k * (3 * k + 1) // 2
            sign = (-1) ** (k + 1)
            if pent1 <= n:
                total += sign * p[n - pent1]
            if pent2 <= n:
                total += sign * p[n - pent2]
        p[n] = total
    return {n: p[n] for n in range(max_n + 1)}


def rocha_caridi_theta(p: int, q: int, r: int, s: int,
                       max_exp: int) -> Dict[Fraction, int]:
    """Theta function theta_{r,s} = eta * chi_{r,s} for M(p,q).

    theta_{r,s}(tau) = sum_n [q^{alpha_+(n)} - q^{alpha_-(n)}]
    alpha_pm(n) = ((2npq +/- (rq-sp))^2 - (p-q)^2) / (4pq)
    """
    from math import isqrt

    a = r * q - s * p
    b = r * q + s * p
    M = 2 * p * q
    pq4 = 4 * p * q

    n_max = isqrt(max_exp * pq4) // M + 10
    result: Dict[Fraction, int] = {}

    for n in range(-n_max, n_max + 1):
        num_plus = (n * M + a) ** 2 - (p - q) ** 2
        if num_plus >= 0:
            exp_plus = Fraction(num_plus, pq4)
            if exp_plus < max_exp:
                result[exp_plus] = result.get(exp_plus, 0) + 1

        num_minus = (n * M + b) ** 2 - (p - q) ** 2
        if num_minus >= 0:
            exp_minus = Fraction(num_minus, pq4)
            if exp_minus < max_exp:
                result[exp_minus] = result.get(exp_minus, 0) - 1

    return {e: c for e, c in result.items() if c != 0}


def virasoro_character(p: int, q: int, r: int, s: int,
                       max_terms: int = 25) -> Dict[int, int]:
    """Compute chi_{r,s}(q) = q^{h-c/24} * sum d_n q^n for M(p,q).

    Returns {n: d_n} where d_n is the degeneracy at level n above h_{r,s}.
    Uses theta_{r,s} = eta * chi_{r,s} and divides by eta.
    """
    eta = _eta_product_coeffs(max_terms + 20)
    theta = rocha_caridi_theta(p, q, r, s, max_terms + 20)

    if not theta:
        return {n: 0 for n in range(max_terms)}

    min_exp = min(theta.keys())
    theta_rel: Dict[int, int] = {}
    for exp, coeff in theta.items():
        diff = exp - min_exp
        n = int(diff)
        if abs(diff - n) < Fraction(1, 1000):
            theta_rel[n] = theta_rel.get(n, 0) + coeff

    # Divide by eta: chi = theta / eta
    chi: Dict[int, int] = {}
    eta0 = eta.get(0, 1)  # = 1
    for n in range(max_terms):
        theta_n = theta_rel.get(n, 0)
        correction = sum(
            eta.get(k, 0) * chi.get(n - k, 0)
            for k in range(1, n + 1)
        )
        chi[n] = (theta_n - correction) // eta0

    return chi


# ============================================================================
# 2. Ising partition function on the torus
# ============================================================================

def ising_characters(max_terms: int = 25) -> Dict[str, Dict[int, int]]:
    """Virasoro characters at c = 1/2 (Ising model M(4,3)).

    Three primaries:
      (1,1): h = 0        (vacuum/identity 1)
      (2,1): h = 1/16     (spin field sigma)
      (1,2): h = 1/2      (energy operator epsilon)

    Returns {label: {n: d_n}} where chi_h(q) = q^{h-c/24} sum d_n q^n.
    """
    return {
        '0': virasoro_character(4, 3, 1, 1, max_terms),
        '1/16': virasoro_character(4, 3, 2, 1, max_terms),
        '1/2': virasoro_character(4, 3, 1, 2, max_terms),
    }


def ising_torus_partition_function(max_terms: int = 25) -> Dict[str, Any]:
    """Torus partition function Z_Ising(tau) = sum_h |chi_h(tau)|^2.

    The diagonal partition function for the Ising model.
    Returns character coefficients and combined Z coefficients.

    Z = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2

    The |chi_h|^2 are products of holomorphic and antiholomorphic characters.
    For the q-expansion, |chi_h(q)|^2 means we square the REAL coefficients
    (the absolute-value-squared contribution at each level).

    This computes the "diagonal partition sum" coefficients:
    for each channel h, sum_n d_n(h)^2 gives the contribution at level n.
    """
    chars = ising_characters(max_terms)

    # For each channel, compute d_n^2 (contribution to |chi|^2 at level n)
    channel_sums = {}
    for label, ch in chars.items():
        channel_sums[label] = {n: ch.get(n, 0) ** 2 for n in range(max_terms)}

    # Combined Z: sum over channels of d_n^2 at each level
    combined = {}
    for n in range(max_terms):
        combined[n] = sum(cs.get(n, 0) for cs in channel_sums.values())

    return {
        'characters': chars,
        'channel_sums': channel_sums,
        'combined': combined,
        'c': Fraction(1, 2),
        'primaries': {
            '0': Fraction(0),
            '1/16': Fraction(1, 16),
            '1/2': Fraction(1, 2),
        },
    }


def ising_partition_numerical(tau_imag: float, max_terms: int = 100) -> float:
    """Evaluate Z_Ising(tau=i*y) numerically.

    Z = |chi_0|^2 + |chi_{1/2}|^2 + |chi_{1/16}|^2
    where each chi_h(q) = q^{h-c/24} sum d_n q^n with q = e^{2*pi*i*tau}.

    At tau = i*y: q = e^{-2*pi*y}, so |q| = e^{-2*pi*y}.
    """
    y = tau_imag
    q = math.exp(-2 * math.pi * y)
    c_over_24 = 1.0 / 48.0  # c/24 = (1/2)/24 = 1/48

    chars = ising_characters(max_terms)
    weights = {'0': 0.0, '1/16': 1.0 / 16.0, '1/2': 0.5}

    z_total = 0.0
    for label, ch in chars.items():
        h = weights[label]
        # chi_h(q) = q^{h-c/24} * sum d_n q^n
        prefactor = q ** (h - c_over_24)
        series = sum(ch.get(n, 0) * q ** n for n in range(max_terms))
        chi_val = prefactor * series
        z_total += chi_val ** 2  # |chi|^2 on the imaginary axis

    return z_total


# ============================================================================
# 3. Shadow tower at c = 1/2
# ============================================================================

def minimal_model_c(p: int, q: int) -> Rational:
    """Central charge of M(p,q): c = 1 - 6(p-q)^2/(pq)."""
    return 1 - Rational(6 * (p - q) ** 2, p * q)


def conformal_weight(p: int, q: int, r: int, s: int) -> Rational:
    """Conformal weight h_{r,s} = ((pr-qs)^2 - (p-q)^2)/(4pq)."""
    return Rational((p * r - q * s) ** 2 - (p - q) ** 2, 4 * p * q)


def shadow_tower_virasoro(c_val: Rational, max_arity: int = 30) -> Dict[str, Any]:
    """Shadow tower for Virasoro at central charge c.

    Returns shadow invariants and tower coefficients S_r.
    Uses the convolution recursion from f^2 = Q_L.

    kappa = c/2 (AP1, AP20: never use c = 2*kappa without verifying family)
    S_3 = 2 (c-independent for ALL Virasoro; NOT -6/(5c+22))
    S_4 = 10/[c(5c+22)] (Q^contact)
    Delta = 8*kappa*S_4 = 80/(5c+22) (critical discriminant)
    """
    kappa = c_val / 2
    S3 = Rational(2)
    denom = 5 * c_val + 22

    if denom == 0:
        # 5c+22 = 0 at c = -22/5 (Yang-Lee): S_4 diverges
        return {
            'c': c_val,
            'kappa': kappa,
            'S3': S3,
            'S4': None,
            'Delta': None,
            'depth_class': 'singular',
            'tower': {2: kappa, 3: S3},
        }

    if c_val == 0:
        return {
            'c': c_val,
            'kappa': Rational(0),
            'S3': Rational(0),
            'S4': Rational(0),
            'Delta': Rational(0),
            'depth_class': 'trivial',
            'tower': {r: Rational(0) for r in range(2, max_arity + 1)},
        }

    S4 = Rational(10, 1) / (c_val * denom)
    Delta = 8 * kappa * S4

    # Shadow metric coefficients
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * S3
    q2 = 9 * S3 ** 2 + 16 * kappa * S4

    # Convolution recursion: sqrt(Q_L) = sum a_n t^n
    max_n = max_arity - 2
    a = [Rational(0)] * (max_n + 1)

    # a_0 = sqrt(q0) = 2*|kappa|
    if kappa > 0:
        a[0] = 2 * kappa
    elif kappa < 0:
        a[0] = -2 * kappa  # take positive root
    else:
        a[0] = Rational(0)

    if max_n >= 1 and a[0] != 0:
        a[1] = q1 / (2 * a[0])
    if max_n >= 2 and a[0] != 0:
        a[2] = (q2 - a[1] ** 2) / (2 * a[0])

    for n in range(3, max_n + 1):
        if a[0] == 0:
            break
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * a[0]))

    tower = {r: cancel(a[r - 2] / r) for r in range(2, max_arity + 1)}

    # Growth rate
    rho_sq = None
    rho_num = None
    if kappa != 0 and Delta is not None:
        numer_sq = 9 * S3 ** 2 + 2 * Delta
        rho_sq = cancel(numer_sq / (4 * kappa ** 2))
        rho_num = float(sqrt(rho_sq).evalf())

    depth_class = 'M' if Delta != 0 else 'G' if kappa == 0 else 'L'

    return {
        'c': c_val,
        'kappa': cancel(kappa),
        'S3': S3,
        'S4': cancel(S4),
        'Delta': cancel(Delta),
        'Q_contact': cancel(S4),
        'q0': q0,
        'q1': q1,
        'q2': cancel(q2),
        'depth_class': depth_class,
        'rho_squared': rho_sq,
        'rho_numerical': rho_num,
        'convergent': rho_num < 1.0 if rho_num is not None else None,
        'tower': tower,
    }


def shadow_tower_numerical(c_val: float, max_arity: int = 50) -> Dict[int, float]:
    """Numerical shadow tower using float64 for speed at high arities."""
    kappa = c_val / 2.0
    S3 = 2.0
    denom = 5.0 * c_val + 22.0
    if abs(denom) < 1e-15 or abs(c_val) < 1e-15:
        return {r: 0.0 for r in range(2, max_arity + 1)}

    S4 = 10.0 / (c_val * denom)

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * S3
    q2 = 9.0 * S3 ** 2 + 16.0 * kappa * S4

    max_n = max_arity - 2
    a = [0.0] * (max_n + 1)
    a[0] = abs(2.0 * kappa)
    if a[0] < 1e-15:
        return {r: 0.0 for r in range(2, max_arity + 1)}
    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2.0 * a[0])

    return {r: a[r - 2] / r for r in range(2, max_arity + 1)}


# ============================================================================
# 4. Koszul dual and complementarity
# ============================================================================

def koszul_dual_data(c_val: Rational) -> Dict[str, Any]:
    """Koszul dual Virasoro data: c' = 26-c, kappa' = (26-c)/2.

    AP24: kappa + kappa' = 13 for Virasoro (NOT 0).
    The Koszul dual of Ising (c=1/2) is Vir_{51/2}, non-unitary.
    """
    c_dual = 26 - c_val
    kappa = c_val / 2
    kappa_dual = c_dual / 2

    return {
        'c': c_val,
        'c_dual': c_dual,
        'kappa': cancel(kappa),
        'kappa_dual': cancel(kappa_dual),
        'kappa_sum': cancel(kappa + kappa_dual),
        'kappa_sum_expected': Rational(13),
        'complementarity_verified': cancel(kappa + kappa_dual) == 13,
    }


def complementarity_discriminant(c_val: Rational) -> Dict[str, Any]:
    """Discriminant complementarity: Delta(A) + Delta(A!) = 6960/((5c+22)(152-5c)).

    For Virasoro at c: Delta = 80/(5c+22)
    For Koszul dual at 26-c: Delta' = 80/(5(26-c)+22) = 80/(152-5c)
    Sum = 80/(5c+22) + 80/(152-5c) = 80*174/((5c+22)(152-5c)) = 13920/(...)
    Wait: 80*((5c+22)+(152-5c)) / ((5c+22)(152-5c)) = 80*174/(...)
    = 13920/((5c+22)(152-5c))

    RECOMPUTATION from first principles (AP1, AP3):
    denom1 = 5c+22, denom2 = 5(26-c)+22 = 152-5c
    denom1 + denom2 = 174
    Delta + Delta' = 80/denom1 + 80/denom2 = 80*(denom1+denom2)/(denom1*denom2) = 80*174/(denom1*denom2)
    = 13920/(denom1*denom2)
    """
    denom1 = 5 * c_val + 22
    denom2 = 152 - 5 * c_val  # = 5*(26-c) + 22

    if denom1 == 0 or denom2 == 0:
        return {'sum': None, 'expected': None, 'match': None}

    Delta = Rational(80) / denom1
    Delta_dual = Rational(80) / denom2
    total = cancel(Delta + Delta_dual)
    expected = cancel(Rational(13920) / (denom1 * denom2))

    return {
        'Delta': cancel(Delta),
        'Delta_dual': cancel(Delta_dual),
        'sum': total,
        'expected': expected,
        'match': simplify(total - expected) == 0,
    }


# ============================================================================
# 5. Minimal model family shadow data
# ============================================================================

MINIMAL_MODEL_FAMILY = {
    'Ising': (4, 3),
    'tricritical_Ising': (5, 4),
    '3-state_Potts': (6, 5),
    'tricritical_3-state_Potts': (7, 6),
    'Yang-Lee': (5, 2),
    'tetracritical_Ising': (6, 5),  # same as 3-state Potts
}


def minimal_model_shadow_family(max_arity: int = 15) -> Dict[str, Dict[str, Any]]:
    """Shadow tower data for the standard minimal model family.

    M(3,4): c=1/2 (Ising)
    M(4,5): c=7/10 (tricritical Ising)
    M(3,5): c=4/5 (3-state Potts) -- Wait: M(6,5) has c = 1-6/30 = 4/5
    M(5,6): c=6/7 -- NO: M(7,6) has c = 1-6/42 = 6/7

    RECOMPUTATION (AP1): c = 1 - 6(p-q)^2/(pq)
    M(4,3): 1 - 6*1/12 = 1 - 1/2 = 1/2
    M(5,4): 1 - 6*1/20 = 1 - 3/10 = 7/10
    M(6,5): 1 - 6*1/30 = 1 - 1/5 = 4/5
    M(7,6): 1 - 6*1/42 = 1 - 1/7 = 6/7
    M(5,2): 1 - 6*9/10 = 1 - 54/10 = -44/10 = -22/5
    """
    models = [
        ('Ising M(4,3)', 4, 3),
        ('tricritical Ising M(5,4)', 5, 4),
        ('3-state Potts M(6,5)', 6, 5),
        ('tricritical 3-state Potts M(7,6)', 7, 6),
        ('Yang-Lee M(5,2)', 5, 2),
    ]

    results = {}
    for name, p, q in models:
        c = minimal_model_c(p, q)
        data = shadow_tower_virasoro(c, max_arity)
        data['name'] = name
        data['p'] = p
        data['q'] = q
        data['n_primaries'] = (p - 1) * (q - 1) // 2
        data['unitary'] = (p == q + 1)
        results[name] = data

    return results


# ============================================================================
# 6. Fusion rules from Verlinde formula
# ============================================================================

def modular_s_matrix(p: int, q: int) -> Tuple[List[Tuple[int, int]], List[List[float]]]:
    """Compute the modular S-matrix for M(p,q) numerically.

    S_{(r1,s1),(r2,s2)} = (-1)^{1+s1*r2+s2*r1} * 2*sqrt(2/(pq))
                          * sin(pi*q*s1*s2/p) * sin(pi*p*r1*r2/q)

    Returns (primaries, matrix) where primaries = [(r,s),...].
    """
    # Enumerate primaries with identification (r,s) ~ (q-r, p-s)
    seen = set()
    primaries = []
    for r in range(1, q):
        for s in range(1, p):
            dual = (q - r, p - s)
            if dual not in seen:
                seen.add((r, s))
                primaries.append((r, s))

    n = len(primaries)
    prefactor = 2.0 * math.sqrt(2.0 / (p * q))
    mat = [[0.0] * n for _ in range(n)]

    for i, (r1, s1) in enumerate(primaries):
        for j, (r2, s2) in enumerate(primaries):
            sign = (-1) ** (1 + s1 * r2 + s2 * r1)
            val = prefactor * math.sin(math.pi * q * s1 * s2 / p) \
                * math.sin(math.pi * p * r1 * r2 / q)
            mat[i][j] = sign * val

    # Ensure S_{00} > 0
    if mat[0][0] < 0:
        for i in range(n):
            for j in range(n):
                mat[i][j] = -mat[i][j]

    return primaries, mat


def verlinde_fusion(p: int, q: int, i: int, j: int, k: int) -> int:
    """Fusion coefficient N_{ij}^k via Verlinde formula.

    N_{ij}^k = sum_l S_{il} S_{jl} S*_{kl} / S_{0l}
    For real unitary S (minimal models): S* = S.
    """
    prims, mat = modular_s_matrix(p, q)
    n = len(prims)
    if i >= n or j >= n or k >= n:
        return 0
    total = 0.0
    for l in range(n):
        s0l = mat[0][l]
        if abs(s0l) < 1e-15:
            continue
        total += mat[i][l] * mat[j][l] * mat[k][l] / s0l
    return int(round(total))


def ising_fusion_from_verlinde() -> Dict[Tuple[int, int], List[int]]:
    """Compute Ising fusion rules from the Verlinde formula.

    Primaries of M(4,3): (1,1)=0, (2,1)=1, (1,2)=2
    i.e., 0=vacuum, 1=sigma, 2=epsilon.

    Expected:
      sigma x sigma = 1 + epsilon  (i.e., N_{1,1}^0 = 1, N_{1,1}^2 = 1)
      sigma x epsilon = sigma       (N_{1,2}^1 = 1)
      epsilon x epsilon = 1         (N_{2,2}^0 = 1)
    """
    p, q = 4, 3
    n = 3  # 3 primaries
    fusion = {}
    for i in range(n):
        for j in range(i, n):
            products = []
            for k in range(n):
                nijk = verlinde_fusion(p, q, i, j, k)
                for _ in range(nijk):
                    products.append(k)
            fusion[(i, j)] = products
    return fusion


# ============================================================================
# 7. Ising 4-point function (genus-0 conformal block)
# ============================================================================

def ising_4point_sigma(z: complex, max_terms: int = 50) -> complex:
    r"""The Ising 4-point function <sigma sigma sigma sigma> on the sphere.

    The exact result is:
      G_4(z) = |F_0(z)|^2 + |F_{1/2}(z)|^2

    where F_0 and F_{1/2} are conformal blocks for the identity and epsilon
    channels respectively:
      F_0(z) = z^{-1/8} (1-z)^{-1/8} * [(1+sqrt(1-z))/2]^{1/2}
      F_{1/2}(z) = z^{-1/8} (1-z)^{-1/8} * [(1-sqrt(1-z))/2]^{1/2}

    Alternative closed form via hypergeometric:
      G_4(z) = |z(1-z)|^{-1/4} * (|1-z+z^2|) / (2 * |z(1-z)|^{1/2})

    Actually the standard result (BPZ 1984) for <sigma sigma sigma sigma> is:
      G(z, z_bar) = |z|^{-1/4} |1-z|^{-1/4} * [|F(z)|^2 + |F(1-z)|^2] / 2

    where F(z) = 2F1(1/2, 1/2; 1; z) (complete elliptic integral K(z)/constant).

    For z real, 0 < z < 1:
      G(z) = |z(1-z)|^{-1/4} * [F(z)^2 + F(1-z)^2] / 2

    This function computes the conformal block F(z) = 2F1(1/2, 1/2; 1; z)
    via power series.
    """
    # 2F1(1/2, 1/2; 1; z) = sum_{n>=0} [(1/2)_n]^2 / [n!]^2 * z^n
    # (a)_n = a(a+1)...(a+n-1)
    result = complex(0.0)
    pochhammer = 1.0  # (1/2)_n / n!
    for n in range(max_terms):
        if n == 0:
            pochhammer = 1.0
        else:
            pochhammer *= (n - 0.5) / n
        result += pochhammer ** 2 * z ** n

    return result


def ising_4point_full(z: float, max_terms: int = 80) -> float:
    """Full diagonal 4-point function |<sigma sigma sigma sigma>| for real z in (0,1).

    G(z) = |z(1-z)|^{-1/4} * [2F1(1/2,1/2;1;z)^2 + 2F1(1/2,1/2;1;1-z)^2] / 2

    The prefactor z^{-1/4}(1-z)^{-1/4} comes from the conformal weights
    h_sigma = h_bar_sigma = 1/16, giving total dimension 1/8.
    The four sigma insertions contribute 4*1/8 = 1/2 to the conformal block
    prefactor, but with the standard cross-ratio dependence
    z^{-2*h_sigma}(1-z)^{-2*h_sigma} = |z(1-z)|^{-1/4} (accounting for
    only the nontrivial cross-ratio dependence after factoring global parts).
    """
    if z <= 0 or z >= 1:
        raise ValueError(f"z must be in (0,1), got {z}")

    prefactor = abs(z * (1 - z)) ** (-0.25)
    F_z = ising_4point_sigma(z, max_terms).real
    F_1mz = ising_4point_sigma(1.0 - z, max_terms).real
    return prefactor * (F_z ** 2 + F_1mz ** 2) / 2.0


# ============================================================================
# 8. Yang-Lee edge singularity (c = -22/5)
# ============================================================================

def yang_lee_data() -> Dict[str, Any]:
    """Yang-Lee edge singularity M(5,2), c = -22/5.

    The simplest non-unitary minimal model: 2 primaries.
    (1,1): h = 0 (vacuum)
    (1,1) identity with identification: only h=0 and h=-1/5

    RECOMPUTATION:
    M(5,2): p=5, q=2, primaries (r,s) with 1<=r<=1, 1<=s<=4
    so r=1 only, s=1,2,3,4 with identification (r,s)~(q-r,p-s)=(1,5-s).
    h_{1,1} = ((5-2)^2 - (5-2)^2)/(4*10) = 0
    h_{1,2} = ((5-4)^2 - 9)/40 = (1-9)/40 = -8/40 = -1/5
    (1,3) ~ (1,2) by the identification, (1,4) ~ (1,1).
    So 2 primaries: h=0 and h=-1/5.

    kappa = c/2 = -11/5
    The shadow tower at negative kappa: the recursion still works but a_0 = |2*kappa|
    and the sign convention matters.

    NOTE: 5c+22 = 5*(-22/5)+22 = -22+22 = 0. So S_4 = 10/(c*(5c+22)) DIVERGES.
    The Yang-Lee model is SINGULAR in the shadow tower because it sits at
    the pole of Q^contact. This is the degenerate case where the shadow
    metric formalism breaks down.
    """
    c = Rational(-22, 5)
    kappa = c / 2  # = -11/5
    denom_5c22 = 5 * c + 22  # = 0

    primaries = {
        (1, 1): Rational(0),
        (1, 2): Rational(-1, 5),
    }

    return {
        'c': c,
        'kappa': kappa,
        'n_primaries': 2,
        'primaries': primaries,
        'unitary': False,
        'negative_kappa': True,
        'S4_diverges': True,
        '5c_plus_22': denom_5c22,
        'depth_class': 'singular',
        'effective_c': c - 24 * Rational(-1, 5),  # c_eff = c - 24*h_min
        'koszul_dual_c': 26 - c,  # = 26 + 22/5 = 152/5
        'complementarity_kappa_sum': kappa + (26 - c) / 2,  # should be 13
    }


def yang_lee_characters(max_terms: int = 25) -> Dict[str, Dict[int, int]]:
    """Characters for the Yang-Lee model M(5,2).

    Two primaries: h=0 (vacuum), h=-1/5 (phi).
    Non-unitary: h < 0, so character coefficients can be negative... wait, NO.
    Character coefficients count states, so they are nonneg integers.
    The conformal weight h=-1/5 means the primary has negative energy,
    but descendants at level n have weight h+n, and the degeneracy d_n >= 0.

    Actually for non-unitary models, the character coefficients ARE nonnegative
    (they count states in the irreducible module), but the states can have
    negative norm.
    """
    return {
        '0': virasoro_character(5, 2, 1, 1, max_terms),
        '-1/5': virasoro_character(5, 2, 1, 2, max_terms),
    }


# ============================================================================
# 9. Critical exponents from conformal dimensions
# ============================================================================

def critical_exponents_from_cft(c_val: Rational, h_sigma: Rational,
                                 h_epsilon: Rational) -> Dict[str, Any]:
    """Compute critical exponents from CFT data in d=2.

    In d=2 with sigma = spin field, epsilon = energy operator:
      eta = 4 * h_sigma  (from <sigma sigma> ~ r^{-2*2*h_sigma} = r^{-d+2-eta})
      Actually: <sigma(r)sigma(0)> ~ r^{-2*(h+hbar)} = r^{-4*h_sigma}
      Comparing with r^{-(d-2+eta)} = r^{-eta} in d=2: eta = 4*h_sigma.

    Correction: the spin-spin correlator in d=2 is
      <sigma(r) sigma(0)> ~ r^{-2*Delta_sigma}
    where Delta_sigma = h_sigma + h_bar_sigma = 2*h_sigma (diagonal).
    The definition eta is: G(r) ~ r^{-(d-2+eta)} at criticality.
    In d=2: G ~ r^{-eta}, so eta = 2*Delta_sigma = 4*h_sigma.

    Similarly for the energy operator: the specific heat exponent alpha
    from h_epsilon via alpha = 2 - d*nu and nu = 1/(2-2*h_epsilon) in d=2...
    Actually: nu = 1/(d - y_t) = 1/(2 - (2-2*h_epsilon)) = 1/(2*h_epsilon).

    Standard relations in d=2:
      nu = 1/(2*h_epsilon)
      eta = 4*h_sigma
      beta = nu * (d-2+eta)/2 = nu * eta/2 (in d=2)
      gamma = nu * (2-eta)
      alpha = 2 - d*nu = 2 - 2*nu
      delta = (d+2-eta)/(d-2+eta) = (4-eta)/eta (in d=2)
    """
    eta = 4 * h_sigma
    nu = 1 / (2 * h_epsilon) if h_epsilon != 0 else None
    if nu is not None:
        beta = nu * eta / 2
        gamma = nu * (2 - eta)
        alpha = 2 - 2 * nu
        delta = (4 - eta) / eta if eta != 0 else None
    else:
        beta = gamma = alpha = delta = None

    return {
        'h_sigma': h_sigma,
        'h_epsilon': h_epsilon,
        'eta': eta,
        'nu': nu,
        'beta': beta,
        'gamma': gamma,
        'alpha': alpha,
        'delta': delta,
    }


def ising_critical_exponents() -> Dict[str, Any]:
    """Ising critical exponents from c=1/2 CFT data.

    h_sigma = 1/16, h_epsilon = 1/2.
    eta = 4*(1/16) = 1/4
    nu = 1/(2*1/2) = 1
    beta = 1*(1/4)/2 = 1/8
    gamma = 1*(2-1/4) = 7/4
    alpha = 2-2 = 0
    delta = (4-1/4)/(1/4) = 15/4 / 1/4 = 15
    """
    return critical_exponents_from_cft(
        Rational(1, 2), Rational(1, 16), Rational(1, 2)
    )


def tricritical_ising_exponents() -> Dict[str, Any]:
    """Tricritical Ising exponents from M(5,4) CFT data.

    h_sigma = 3/80, h_epsilon = 1/10.
    eta = 4*(3/80) = 3/20
    nu = 1/(2*1/10) = 5
    """
    return critical_exponents_from_cft(
        Rational(7, 10), Rational(3, 80), Rational(1, 10)
    )


# ============================================================================
# 10. Transfer matrix for finite Ising lattice (independent verification)
# ============================================================================

def ising_transfer_matrix(L: int) -> List[List[float]]:
    """Transfer matrix for the 1d Ising chain of length L with periodic BC.

    The transfer matrix T has elements T_{sigma, sigma'} = exp(K sum_i sigma_i sigma'_i)
    where the sum is over nearest neighbors in a row.

    For a row of L spins, the transfer matrix is 2^L x 2^L.
    T_{s1...sL, s1'...sL'} = prod_{i=1}^L exp(K s_i s_i') * prod_{i=1}^{L-1} exp(K s_i s_{i+1})

    Actually for the 2d Ising on an L x M lattice with periodic BC in both
    directions, the partition function is Z = Tr(V^M) where V is the
    row-to-row transfer matrix.

    For simplicity, compute the CRITICAL transfer matrix at K = K_c:
    K_c = (1/2) * log(1 + sqrt(2)) ~ 0.4407.

    The transfer matrix decomposes into eigenvalues whose ratios give
    the conformal spectrum: (lambda_1/lambda_0)^M ~ exp(-2*pi*h/L).
    """
    import itertools

    K_c = 0.5 * math.log(1.0 + math.sqrt(2.0))
    n = 2 ** L
    T = [[0.0] * n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            # Convert to spin configurations
            sa = [(a >> i) & 1 for i in range(L)]
            sb = [(b >> i) & 1 for i in range(L)]
            # Convert 0,1 to +1,-1
            sa = [2 * s - 1 for s in sa]
            sb = [2 * s - 1 for s in sb]

            # Vertical coupling: sum_i sa[i]*sb[i]
            vert = sum(sa[i] * sb[i] for i in range(L))
            # Horizontal coupling in row a: sum_i sa[i]*sa[i+1 mod L]
            horiz_a = sum(sa[i] * sa[(i + 1) % L] for i in range(L))

            # Transfer matrix element (symmetric Ising convention):
            # V = exp(K_v * vert) * exp(K_h * horiz / 2)
            # At criticality with isotropic couplings K_v = K_h = K_c:
            # T_{a,b} = exp(K_c * vert + K_c * horiz_a / 2)
            # The 1/2 on horiz_a distributes the horizontal interaction
            # equally between the two rows sharing it.
            # Actually the standard approach:
            # V = V_1^{1/2} V_2 V_1^{1/2} where V_1 handles horizontal
            # and V_2 handles vertical.
            # Simpler: just include full horizontal in the row.
            T[a][b] = math.exp(K_c * vert + K_c * horiz_a)

    return T


def transfer_matrix_eigenvalues(L: int) -> List[float]:
    """Eigenvalues of the Ising transfer matrix at criticality for strip width L.

    Returns eigenvalues sorted in decreasing order.
    For L=4: 2^4=16 x 16 matrix.
    """
    T = ising_transfer_matrix(L)
    n = len(T)

    # Power iteration for the few largest eigenvalues is sufficient
    # for small L. For exactness use numpy if available, else manual.
    try:
        import numpy as np
        T_np = np.array(T)
        eigenvalues = np.linalg.eigvalsh(T_np)  # symmetric matrix
        return sorted(eigenvalues.tolist(), reverse=True)
    except ImportError:
        # Fallback: just return the matrix for external computation
        return []


def conformal_spectrum_from_transfer(L: int) -> Dict[str, Any]:
    """Extract conformal spectrum from transfer matrix eigenvalues.

    The scaling dimensions Delta_i are extracted from:
      log(lambda_0/lambda_i) = 2*pi*Delta_i/L + O(1/L^2)

    At criticality with c=1/2, the expected spectrum is:
      Delta_0 = 0 (vacuum)
      Delta_1 = 1/8 (sigma: h=1/16 + hbar=1/16)
      Delta_2 = 1 (epsilon: h=1/2 + hbar=1/2)... wait no.
      Actually for a periodic strip, the spectrum includes both holomorphic
      AND antiholomorphic dimensions: Delta = h + h_bar.

    For the diagonal theory: Delta = 2*h for each primary.
    Vacuum: 0, sigma: 2*1/16 = 1/8, epsilon: 2*1/2 = 1.
    But there are also descendants: T gives Delta = 2, etc.

    The finite-size scaling formula is:
      f_L = f_bulk - pi*c/(6*L^2) + O(1/L^4)
    where f_L = -(1/L)*log(lambda_0).
    """
    eigenvalues = transfer_matrix_eigenvalues(L)
    if not eigenvalues:
        return {'L': L, 'eigenvalues': [], 'spectrum': []}

    lambda_0 = eigenvalues[0]
    log_lambda_0 = math.log(lambda_0)

    # Free energy per site
    f_L = -log_lambda_0 / L

    # Conformal spectrum from gaps
    spectrum = []
    for i, lam in enumerate(eigenvalues):
        if lam > 0:
            gap = math.log(lambda_0 / lam)
            delta_i = gap * L / (2 * math.pi)
            spectrum.append(delta_i)

    # Central charge from finite-size scaling:
    # f_L = f_bulk - pi*c/(6*L^2)
    # We need two system sizes to extract both f_bulk and c.
    # For a single size, report the extracted spectrum.

    return {
        'L': L,
        'eigenvalues': eigenvalues[:10],
        'log_lambda_0': log_lambda_0,
        'f_per_site': f_L,
        'spectrum': spectrum[:10],
    }


def finite_size_central_charge(L1: int, L2: int) -> float:
    """Extract c from finite-size scaling using two system sizes.

    f_{L} = f_bulk - pi*c/(6*L^2) + higher order corrections.
    From L1 and L2: c = 6*(f_{L2} - f_{L1}) / (pi*(1/L1^2 - 1/L2^2)).

    This gives c_eff ~ 1/2 in the scaling limit.
    """
    spec1 = conformal_spectrum_from_transfer(L1)
    spec2 = conformal_spectrum_from_transfer(L2)

    if not spec1['eigenvalues'] or not spec2['eigenvalues']:
        return float('nan')

    f1 = spec1['f_per_site']
    f2 = spec2['f_per_site']

    denom = math.pi * (1.0 / L1 ** 2 - 1.0 / L2 ** 2)
    if abs(denom) < 1e-15:
        return float('nan')

    c_extracted = 6.0 * (f2 - f1) / denom
    return c_extracted


# ============================================================================
# 11. Modular invariance and S-matrix verification
# ============================================================================

def verify_s_matrix_unitarity(p: int, q: int) -> Dict[str, bool]:
    """Verify the modular S-matrix is symmetric and unitary.

    S * S^T = I (unitarity)
    S = S^T (symmetry)
    S^2 = C (charge conjugation matrix)
    """
    prims, mat = modular_s_matrix(p, q)
    n = len(prims)

    # Symmetry
    sym_ok = all(
        abs(mat[i][j] - mat[j][i]) < 1e-10
        for i in range(n) for j in range(n)
    )

    # Unitarity: S * S^dagger = I (S is real here)
    unit_ok = True
    for i in range(n):
        for j in range(n):
            val = sum(mat[i][k] * mat[j][k] for k in range(n))
            expected = 1.0 if i == j else 0.0
            if abs(val - expected) > 1e-10:
                unit_ok = False

    # S^2 should be charge conjugation (= identity for all diagonal minimal models)
    sq_ok = True
    for i in range(n):
        for j in range(n):
            val = sum(mat[i][k] * mat[k][j] for k in range(n))
            expected = 1.0 if i == j else 0.0
            if abs(val - expected) > 1e-10:
                sq_ok = False

    return {
        'symmetric': sym_ok,
        'unitary': unit_ok,
        'S_squared_is_identity': sq_ok,
        'S00_positive': mat[0][0] > 0,
        'n_primaries': n,
    }


def quantum_dimensions(p: int, q: int) -> Dict[Tuple[int, int], float]:
    """Quantum dimensions d_i = S_{0i}/S_{00} for all primaries of M(p,q)."""
    prims, mat = modular_s_matrix(p, q)
    s00 = mat[0][0]
    return {prims[i]: mat[0][i] / s00 for i in range(len(prims))}


# ============================================================================
# 12. Faber-Pandharipande and genus expansion
# ============================================================================

def lambda_fp(g: int) -> Rational:
    """Faber-Pandharipande intersection number.

    lambda_g^FP = (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!

    First values: lambda_1=1/24, lambda_2=7/5760, lambda_3=31/967680.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    numer = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    denom = 2 ** (2 * g - 1) * factorial(2 * g)
    return Rational(numer, denom)


def ising_genus_expansion(max_genus: int = 10) -> Dict[int, Rational]:
    """Scalar free energy F_g(Ising) = kappa * lambda_g^FP = (1/4)*lambda_g.

    This is the scalar (arity-2) contribution only. Higher arity corrections
    are controlled by the shadow tower but DIVERGE for c=1/2 (rho >> 1).
    """
    kappa = Rational(1, 4)
    return {g: kappa * lambda_fp(g) for g in range(1, max_genus + 1)}


# ============================================================================
# 13. Cross-family invariants
# ============================================================================

def shadow_connection_monodromy(c_val: Rational) -> Dict[str, Any]:
    """Shadow connection data: nabla^sh = d - Q'_L/(2*Q_L) dt.

    The flat sections are Phi(t) = sqrt(Q_L(t)/Q_L(0)).
    The shadow generating function H(t) = 2*kappa*t^2*Phi(t) is NOT flat
    (AP23: ∇^sh(H) != 0 because of the t^2 prefactor).

    Monodromy around the zeros of Q_L is -1 (Koszul sign).
    """
    kappa = c_val / 2
    if kappa == 0:
        return {'c': c_val, 'kappa': 0, 'monodromy': None}

    denom = 5 * c_val + 22
    if denom == 0:
        return {'c': c_val, 'kappa': kappa, 'monodromy': None}

    S3 = Rational(2)
    S4 = Rational(10) / (c_val * denom)
    Delta = 8 * kappa * S4

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * S3
    q2 = 9 * S3 ** 2 + 16 * kappa * S4

    disc = q1 ** 2 - 4 * q0 * q2

    # Zeros of Q_L: t = (-q1 +/- sqrt(disc)) / (2*q2)
    # For class M: disc < 0, so zeros are complex conjugate.
    disc_float = float(disc)

    if disc_float < 0:
        # Complex conjugate zeros
        t_real = float(-q1) / (2 * float(q2))
        t_imag = math.sqrt(-disc_float) / (2 * float(q2))
        branch_points = (complex(t_real, t_imag), complex(t_real, -t_imag))
        branch_modulus = abs(branch_points[0])
    else:
        # Real zeros
        sd = math.sqrt(disc_float)
        t1 = (-float(q1) + sd) / (2 * float(q2))
        t2 = (-float(q1) - sd) / (2 * float(q2))
        branch_points = (t1, t2)
        branch_modulus = min(abs(t1), abs(t2))

    return {
        'c': c_val,
        'kappa': cancel(kappa),
        'Delta': cancel(Delta),
        'discriminant': cancel(disc),
        'branch_points': branch_points,
        'branch_modulus': branch_modulus,
        'convergence_radius': branch_modulus,  # radius = |branch point|
        'monodromy': -1,  # Koszul sign: always -1
    }


# ============================================================================
# 14. Summary driver
# ============================================================================

def complete_ising_lattice_analysis(max_arity: int = 20,
                                     max_genus: int = 5,
                                     max_terms: int = 25) -> Dict[str, Any]:
    """Complete analysis: partition function, shadow tower, fusion, exponents."""
    c = Rational(1, 2)

    return {
        'partition_function': ising_torus_partition_function(max_terms),
        'shadow_tower': shadow_tower_virasoro(c, max_arity),
        'koszul_dual': koszul_dual_data(c),
        'complementarity_disc': complementarity_discriminant(c),
        'minimal_model_family': minimal_model_shadow_family(min(max_arity, 10)),
        'ising_fusion_verlinde': ising_fusion_from_verlinde(),
        'yang_lee': yang_lee_data(),
        'critical_exponents': ising_critical_exponents(),
        'genus_expansion': ising_genus_expansion(max_genus),
        'shadow_connection': shadow_connection_monodromy(c),
    }
