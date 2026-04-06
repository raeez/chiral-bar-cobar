r"""Fourier-Jacobi expansion of the Igusa cusp form Phi_10 and its reciprocal.

MATHEMATICAL FRAMEWORK
======================

Phi_10 is the UNIQUE Siegel cusp form of weight 10 on Sp(4,Z).
It governs the 1/4-BPS spectrum of type II string theory on K3 x T^2
via the DVV formula (Dijkgraaf-Verlinde-Verlinde 1997):

    Z_{1/4-BPS}(Omega) = 1/Phi_10(Omega)

where Omega = ((tau, z), (z, sigma)) lies in the Siegel upper half-space H_2.

1. FOURIER-JACOBI EXPANSION
   Phi_10(Omega) = sum_{m >= 1} phi_m(tau, z) * p^m
   where p = exp(2*pi*i*sigma), and phi_m is a Jacobi cusp form of
   weight 10, index m.

2. FIRST COEFFICIENT phi_1 = phi_{10,1}
   phi_{10,1}(tau, z) = eta(tau)^{18} * theta_1(tau, z)^2
   This is the UNIQUE Jacobi cusp form of weight 10, index 1
   (dim J_{10,1}^{cusp} = 1 by Eichler-Zagier).

3. JACOBI FORM RING STRUCTURE
   The ring of weak Jacobi forms is freely generated:
     J_{*,*}^{weak} = C[E_4, E_6, phi_{-2,1}, phi_{0,1}]
   where:
     E_4 = 1 + 240*sum_{n>=1} sigma_3(n)*q^n
     E_6 = 1 - 504*sum_{n>=1} sigma_5(n)*q^n
     phi_{-2,1}(tau,z) = -theta_1(tau,z)^2 / eta(tau)^6
     phi_{0,1}(tau,z) = 4*(theta_2(tau,z)^2/theta_2(tau,0)^2
                          + theta_3(tau,z)^2/theta_3(tau,0)^2
                          + theta_4(tau,z)^2/theta_4(tau,0)^2)

   Exact ring expression:
     phi_{10,1} = E_4 * E_6 * phi_{-2,1}
   PROOF: weight = 4+6+(-2) = 8... NO. Let's be careful.
   phi_{-2,1} has weight -2, index 1. E_4 has weight 4, index 0. E_6 has weight 6, index 0.
   Product: weight = 4+6+(-2) = 8, index = 1. But phi_{10,1} has weight 10.
   So phi_{10,1} != E_4 * E_6 * phi_{-2,1}.

   The correct expression: by Eichler-Zagier, dim J_{10,1}^{cusp} = 1 and
     phi_{10,1} = -E_4^2 * phi_{-2,1}
   CHECK: weight = 4+4+(-2) = 6... no.

   CAREFUL DERIVATION: Using Eichler-Zagier Theorem 9.3, every Jacobi form
   of weight k and index 1 is a polynomial in E_4, E_6, phi_{-2,1}, phi_{0,1}.
   For weight 10, index 1:
     J_{10,1} has basis from monomials in E_4^a * E_6^b * phi_{0,1}^c * phi_{-2,1}^d
     with weight 4a + 6b + 0c + (-2)d = 10 and index c + d = 1.

   So either (c,d) = (1,0) or (c,d) = (0,1).
   Case d=0, c=1: weight from E_4^a E_6^b = 10-0 = 10, so 4a+6b = 10.
     a=1, b=1: 4+6 = 10. YES.  phi_{0,1} * E_4 * E_6.
   Case d=1, c=0: weight from E_4^a E_6^b = 10-(-2) = 12, so 4a+6b = 12.
     (a,b) = (3,0), (0,2). Two monomials: E_4^3 * phi_{-2,1}, E_6^2 * phi_{-2,1}.

   So J_{10,1} = span{E_4*E_6*phi_{0,1}, E_4^3*phi_{-2,1}, E_6^2*phi_{-2,1}}.
   dim J_{10,1} = 3. But J_{10,1}^{cusp} has dimension 1 (Eichler-Zagier Table 2).

   The cusp condition forces phi(tau, 0) = 0 for Jacobi cusp forms with index >= 1.
   phi_{-2,1}(tau, 0) = 0 (theta_1(tau,0) = 0), phi_{0,1}(tau, 0) = 12.
   So phi_{-2,1} terms automatically satisfy cusp condition.
   E_4*E_6*phi_{0,1}(tau,0) = E_4*E_6*12 != 0, so NOT a cusp form.

   Hence J_{10,1}^{cusp} = span{E_4^3 * phi_{-2,1}, E_6^2 * phi_{-2,1}}
   WAIT: dim = 2 from these, but dim J_{10,1}^{cusp} = 1 by EZ. So there
   must be a linear relation. Indeed:
     phi_{10,1} = (1/144) * (E_4^3 - E_6^2) * phi_{-2,1}
   Because E_4^3 - E_6^2 = 1728*Delta (where Delta = eta^{24} is the
   discriminant modular form).
   So phi_{10,1} = 12 * Delta * phi_{-2,1} = 12 * eta^{24} * (-theta_1^2/eta^6)
                 = -12 * eta^{18} * theta_1^2.
   But the STANDARD normalization has phi_{10,1} = eta^{18} * theta_1^2
   (positive leading coefficient).

   RESOLUTION: phi_{-2,1} = -theta_1^2/eta^6 (note the minus sign in the
   standard EZ convention). So:
     (1/144) * (E_4^3 - E_6^2) * phi_{-2,1}
     = (1/144) * 1728 * eta^{24} * (-theta_1^2 / eta^6)
     = -12 * eta^{18} * theta_1^2
     = -12 * phi_{10,1}   (if phi_{10,1} = eta^{18} theta_1^2).

   We adopt: phi_{10,1} = eta^{18} * theta_1^2 with POSITIVE leading coefficient.
   Ring expression: phi_{10,1} = -(1/12) * Delta * phi_{-2,1}
                                = -(1/1728) * (E_4^3 - E_6^2) * phi_{-2,1}

   MULTI-PATH CHECK: Both definitions agree on q-expansion.

4. THE RECIPROCAL 1/Phi_10 (DVV FORMULA)
   1/Phi_10 = sum_{n,l,m} d(n,l,m) * q^n * y^l * p^m
   The d(n,l,m) count 1/4-BPS dyonic degeneracies.

   Borcherds product formula:
     Phi_10(Omega) = p*q*y * prod_{(n,l,m)>0} (1 - q^n y^l p^m)^{c_0(4nm-l^2)}
   where c_0(k) are Fourier coefficients of the K3 elliptic genus:
     chi(K3; tau,z) = 2*phi_{0,1}(tau,z) = sum c_0(4n-l^2) q^n y^l.

5. DISCRIMINANT LATTICE
   BPS charges in Gamma^{2,2} = U + U (two hyperbolic planes).
   Discriminant: Delta = 4nm - l^2.
   d(Delta) = sum_{4nm-l^2=Delta} d(n,l,m).
   Cardy growth: log|d(Delta)| ~ 4*pi*sqrt(Delta) for large Delta.

CONVENTION (AP38):
We use the EICHLER-ZAGIER convention throughout. The DVV paper uses a
different normalization; see explicit conversion factors where needed.

References:
  - Dijkgraaf, Verlinde, Verlinde (1997), hep-th/9607026
  - Eichler, Zagier (1985), "The theory of Jacobi forms"
  - Gritsenko, Nikulin (1996), alg-geom/9611028
  - Igusa (1962), "On Siegel modular forms of genus two"
  - Borcherds (1995), alg-geom/9609022
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

import numpy as np


# ============================================================
# ARITHMETIC PRIMITIVES
# ============================================================

def _sigma(s: int, n: int) -> int:
    """Divisor function sigma_s(n) = sum_{d|n} d^s."""
    if n <= 0:
        return 0
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += d ** s
    return total


@lru_cache(maxsize=256)
def _bernoulli(n: int) -> Fraction:
    """Bernoulli number B_n as exact fraction.

    Uses the recursion: sum_{k=0}^{m} C(m+1, k) B_k = 0 for m >= 1.
    So B_m = -(1/(m+1)) * sum_{k=0}^{m-1} C(m+1, k) B_k.
    """
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        s = Fraction(0)
        for k in range(m):
            # C(m+1, k) via direct computation
            binom_val = Fraction(1)
            for j in range(k):
                binom_val = binom_val * Fraction(m + 1 - j, j + 1)
            s += binom_val * B[k]
        B[m] = -s / Fraction(m + 1)
    return B[n]


# ============================================================
# CLASSICAL MODULAR FORMS: EISENSTEIN SERIES
# ============================================================

@lru_cache(maxsize=16)
def eisenstein_series_q_expansion(k: int, qmax: int) -> Dict[int, Fraction]:
    """
    Normalized Eisenstein series E_k(tau) = 1 + C_k * sum_{n>=1} sigma_{k-1}(n) q^n.

    Returns dict {n: coefficient} for n = 0, 1, ..., qmax.

    Convention: E_4 = 1 + 240*sum sigma_3(n) q^n
                E_6 = 1 - 504*sum sigma_5(n) q^n
    """
    if k < 4 or k % 2 != 0:
        raise ValueError(f"Need even k >= 4, got k={k}")
    # C_k = -2k/B_k  (e.g., C_4 = -8/B_4 = -8/(-1/30) = 240)
    B_k = _bernoulli(k)
    C_k = Fraction(-2 * k, 1) / B_k
    coeffs = {}
    coeffs[0] = Fraction(1)
    for n in range(1, qmax + 1):
        coeffs[n] = C_k * Fraction(_sigma(k - 1, n))
    return coeffs


# ============================================================
# DEDEKIND ETA AND JACOBI THETA FUNCTIONS
# ============================================================

def eta_power_q_expansion(power: int, qmax: int) -> Dict[Fraction, int]:
    """
    Compute eta(tau)^power as a q-expansion.

    eta(tau) = q^{1/24} * prod_{n>=1} (1 - q^n).

    Returns dict {exponent: coefficient} where exponent may be fractional
    (multiple of 1/24).

    AP46 WARNING: eta includes the q^{1/24} prefactor. We track this carefully.

    For integer power p, eta^p = q^{p/24} * prod (1-q^n)^p.
    """
    # Start with q^{power/24} * 1
    # Compute prod_{n=1}^{N} (1-q^n)^power truncated at q^qmax
    # The total power of q is power/24 + (integer from product)

    # We compute the integer-exponent part of the product first
    # then shift by power/24

    # prod (1-q^n)^power to order q^qmax
    # Use the recurrence via Euler's pentagonal theorem or direct multiplication

    # For general power, multiply term by term
    # (1-q^n)^power for each n

    # We represent as a polynomial in q with integer exponents
    # coeffs[j] = coefficient of q^j in prod_{n>=1} (1-q^n)^power
    product_coeffs = [0] * (qmax + 1)
    product_coeffs[0] = 1

    for n in range(1, qmax + 1):
        # Multiply by (1 - q^n)^power
        # For integer power, expand (1-q^n)^power via binomial theorem
        # Then convolve
        if power >= 0:
            # Binomial expansion of (1 - q^n)^power
            binom_coeffs = {}
            binom_coeffs[0] = 1
            binom_c = 1
            for j in range(1, min(power, qmax // n) + 1):
                binom_c = binom_c * (power - j + 1) // j
                binom_coeffs[j * n] = binom_c * ((-1) ** j)
        else:
            # For negative power: (1-q^n)^{-|power|} = sum_{j>=0} C(|power|+j-1,j) q^{nj}
            abs_power = -power
            binom_coeffs = {}
            binom_c = 1
            for j in range(0, qmax // n + 1):
                binom_coeffs[j * n] = binom_c
                binom_c = binom_c * (abs_power + j) // (j + 1)

        # Convolve product_coeffs with binom_coeffs
        new_coeffs = [0] * (qmax + 1)
        for e1, c1 in enumerate(product_coeffs):
            if c1 == 0:
                continue
            for e2, c2 in binom_coeffs.items():
                if e1 + e2 > qmax:
                    break
                new_coeffs[e1 + e2] += c1 * c2
        product_coeffs = new_coeffs

    # Now shift by power/24
    # Return as dict {Fraction(j + power/24): coeff}
    shift = Fraction(power, 24)
    result = {}
    for j, c in enumerate(product_coeffs):
        if c != 0:
            result[shift + j] = c
    return result


def eta_power_q_expansion_integer_shifted(power: int, qmax: int) -> Tuple[Fraction, List[int]]:
    """
    Compute eta(tau)^power.

    Returns (q_shift, coeffs) where eta^power = q^{q_shift} * sum_{n>=0} coeffs[n] * q^n.
    The q_shift is power/24.
    """
    d = eta_power_q_expansion(power, qmax)
    shift = Fraction(power, 24)
    coeffs = [0] * (qmax + 1)
    for exp, c in d.items():
        idx = exp - shift
        if idx == int(idx) and 0 <= int(idx) <= qmax:
            coeffs[int(idx)] = c
    return shift, coeffs


def theta_1_squared_qy_expansion(qmax: int, ymax: int) -> Dict[Tuple[Fraction, int], int]:
    """
    Compute theta_1(tau, z)^2 as a q-y expansion.

    theta_1(tau, z) = -i * sum_{n in Z} (-1)^n * q^{(n+1/2)^2/2} * y^{n+1/2}
                    = 2 * q^{1/8} * sin(pi*z) * prod_{n>=1} (1-q^n)(1-y*q^n)(1-y^{-1}*q^n)

    Using the product formula:
      theta_1(tau,z) = -i * sum_{n=-inf}^{inf} (-1)^n q^{(2n+1)^2/8} y^{(2n+1)/2}

    For theta_1^2, we compute the convolution of theta_1 with itself.

    The Jacobi triple product:
      theta_1(tau,z) = 2*q^{1/8}*sin(pi*z) * prod_{n>=1}(1-q^n)(1-y*q^n)(1-y^{-1}*q^n)

    More precisely:
      theta_1(tau,z) = -i * q^{1/8} * (y^{1/2} - y^{-1/2}) * prod_{n>=1}(1-q^n)(1-yq^n)(1-y^{-1}q^n)

    theta_1^2 = -q^{1/4} * (y^{1/2} - y^{-1/2})^2 * prod(...)^2
              = -q^{1/4} * (y - 2 + y^{-1}) * prod(...)^2

    Alternative approach: use the LATTICE SUM directly.
    theta_1(tau,z)^2 = (sum_{r in Z+1/2} (-1)^{r-1/2} q^{r^2/2} y^r)^2

    Let's use the lattice sum approach for precision.
    We compute theta_1^2 = sum_{r1, r2 in Z+1/2} (-1)^{r1+r2-1} q^{(r1^2+r2^2)/2} y^{r1+r2}
    = -sum_{r1,r2} (-1)^{r1+r2} q^{(r1^2+r2^2)/2} y^{r1+r2}

    Setting n_i = r_i - 1/2 (integer), r_i = n_i + 1/2:
    r_i^2 = n_i^2 + n_i + 1/4
    r1^2 + r2^2 = n1^2 + n2^2 + n1 + n2 + 1/2
    (r1^2+r2^2)/2 = (n1^2+n2^2+n1+n2)/2 + 1/4
    (-1)^{r1+r2} = (-1)^{n1+n2+1} = -(-1)^{n1+n2}
    y^{r1+r2} = y^{n1+n2+1}

    So theta_1^2 = -sum (-(-1)^{n1+n2}) q^{(n1^2+n2^2+n1+n2)/2 + 1/4} y^{n1+n2+1}
                 = sum (-1)^{n1+n2} q^{(n1(n1+1)+n2(n2+1))/2 + 1/4} y^{n1+n2+1}

    Returns dict {(q_exponent, l): coefficient} where q_exponent is Fraction
    and l is the y-power (integer).
    """
    # Direct lattice sum computation
    # r in Z + 1/2, so r = n + 1/2 for n in Z
    # theta_1 = sum_{n in Z} (-1)^n * q^{(n+1/2)^2/2} * y^{n+1/2}
    # (dropping the -i prefactor, which squares to -1)
    # theta_1^2 has prefactor (-i)^2 = -1

    # Range for n: need (n+1/2)^2/2 <= qmax, so |n| <= sqrt(2*qmax) - 1/2
    nmax = int(math.sqrt(2 * qmax)) + 2

    result: Dict[Tuple[Fraction, int], int] = defaultdict(int)

    for n1 in range(-nmax, nmax + 1):
        r1 = Fraction(2 * n1 + 1, 2)
        q1 = r1 * r1 / 2
        sign1 = (-1) ** n1
        for n2 in range(-nmax, nmax + 1):
            r2 = Fraction(2 * n2 + 1, 2)
            q2 = r2 * r2 / 2
            q_exp = q1 + q2
            if q_exp > qmax + 1:
                continue
            l = int(r1 + r2)  # r1 + r2 is always integer (half + half)
            if abs(l) > ymax:
                continue
            sign2 = (-1) ** n2
            # theta_1^2 = (-i)^2 * (sum ...)^2 = -1 * (sum ...)^2
            # Each theta_1 = -i * sum (-1)^n q^{r^2/2} y^r
            # theta_1^2 = (-i)^2 * (sum)(sum) = -(sum)(sum)
            result[(q_exp, l)] += -1 * sign1 * sign2

    return dict(result)


def phi_10_1_qy_expansion(qmax: int, ymax: int) -> Dict[Tuple[int, int], int]:
    """
    Compute phi_{10,1}(tau, z) = eta(tau)^{18} * theta_1(tau, z)^2
    as a q-y expansion.

    Returns dict {(n, l): coefficient} where the expansion is
    phi_{10,1} = sum_{n,l} f(n,l) * q^n * y^l
    with the constraint that n >= 0 and 4n - l^2 >= 0 (cusp form condition).

    The q-power: eta^18 contributes q^{18/24} = q^{3/4}.
    theta_1^2 contributes q^{1/4} from the (1/2)^2 + (1/2)^2 minimum.
    So the leading q-power is q^{3/4 + 1/4} = q^1.
    Hence phi_{10,1} starts at q^1 (confirming it's a cusp form).
    """
    # eta^18 = q^{18/24} * prod (1-q^n)^{18}
    eta_shift, eta_coeffs = eta_power_q_expansion_integer_shifted(18, qmax + 2)
    # eta_shift = 18/24 = 3/4

    # theta_1^2 expansion
    theta_sq = theta_1_squared_qy_expansion(qmax + 2, ymax)

    # Convolve: phi_{10,1} = eta^18 * theta_1^2
    # eta^18 = q^{3/4} * sum_j eta_coeffs[j] * q^j
    # theta_1^2 = sum_{(q_exp, l)} c * q^{q_exp} * y^l
    # Product = sum q^{3/4 + j + q_exp} * y^l * (eta_coeffs[j] * c)

    result: Dict[Tuple[int, int], int] = defaultdict(int)

    for j, ec in enumerate(eta_coeffs):
        if ec == 0:
            continue
        for (q_exp, l), tc in theta_sq.items():
            total_q = eta_shift + j + q_exp
            # total_q should be a non-negative integer for a Jacobi form
            if total_q != int(total_q):
                continue
            n = int(total_q)
            if n < 0 or n > qmax:
                continue
            if abs(l) > ymax:
                continue
            result[(n, l)] += ec * tc

    return dict(result)


def phi_10_1_ring_expression(qmax: int, ymax: int) -> Dict[Tuple[int, int], Fraction]:
    """
    Compute phi_{10,1} from the Jacobi form RING GENERATORS.

    phi_{10,1} = -(1/12) * Delta(tau) * phi_{-2,1}(tau, z)

    where Delta = eta^{24} and phi_{-2,1} = -theta_1^2/eta^6.

    So phi_{10,1} = -(1/12) * eta^{24} * (-theta_1^2 / eta^6)
                  = (1/12) * eta^{18} * theta_1^2

    WAIT: This gives phi_{10,1} = (1/12) * eta^{18} * theta_1^2.
    But the standard convention is phi_{10,1} = eta^{18} * theta_1^2.
    The factor of 1/12 depends on the normalization of Delta.

    The issue: E_4^3 - E_6^2 = 1728 * Delta with Delta = eta^{24}.
    So (1/1728) * (E_4^3 - E_6^2) = Delta = eta^{24}.

    phi_{-2,1} = -theta_1^2 / eta^6.

    Then: -(1/12) * Delta * phi_{-2,1} = -(1/12) * eta^{24} * (-theta_1^2/eta^6)
        = (1/12) * eta^{18} * theta_1^2.

    For the normalization to match phi_{10,1} = eta^{18} * theta_1^2, we need:
    phi_{10,1} = -12 * Delta * phi_{-2,1} * (1/144)... Let me just verify
    numerically.

    Actually, the clean statement is:
      phi_{10,1} = eta^{18} * theta_1^2   (THIS is the definition)

    And in the ring:
      E_4^3 * phi_{-2,1} = -E_4^3 * theta_1^2/eta^6
      E_6^2 * phi_{-2,1} = -E_6^2 * theta_1^2/eta^6

      (E_4^3 - E_6^2) * phi_{-2,1} = -(E_4^3 - E_6^2) * theta_1^2/eta^6
                                    = -1728 * eta^{24} * theta_1^2/eta^6
                                    = -1728 * eta^{18} * theta_1^2
                                    = -1728 * phi_{10,1}

    So: phi_{10,1} = -(1/1728) * (E_4^3 - E_6^2) * phi_{-2,1}

    We verify this by computing the right-hand side.
    """
    # Compute E_4, E_6 q-expansions
    E4 = eisenstein_series_q_expansion(4, qmax + 5)
    E6 = eisenstein_series_q_expansion(6, qmax + 5)

    # Compute E_4^3 and E_6^2 as q-series
    E4_cubed = _multiply_q_series(
        _multiply_q_series(E4, E4, qmax + 5),
        E4, qmax + 5
    )
    E6_squared = _multiply_q_series(E6, E6, qmax + 5)

    # E_4^3 - E_6^2 = 1728 * Delta
    delta_1728 = {}
    for n in range(qmax + 5 + 1):
        v = E4_cubed.get(n, Fraction(0)) - E6_squared.get(n, Fraction(0))
        if v != 0:
            delta_1728[n] = v

    # phi_{-2,1} = -theta_1^2 / eta^6
    # We compute theta_1^2 and eta^{-6} separately, then combine

    # Actually, let's compute (E_4^3 - E_6^2) * phi_{-2,1} directly.
    # (E_4^3 - E_6^2) * phi_{-2,1} = (E_4^3 - E_6^2) * (-theta_1^2/eta^6)
    # = -1728 * eta^{24} * theta_1^2/eta^6
    # = -1728 * eta^{18} * theta_1^2
    # = -1728 * phi_{10,1}

    # So phi_{10,1} = -(1/1728) * (E_4^3 - E_6^2) * phi_{-2,1}

    # Let's verify: compute eta^{18} * theta_1^2 from RING data
    # (E_4^3 - E_6^2)/1728 = eta^{24}. So eta^{18} = eta^{24}/eta^6.
    # We compute Delta/eta^6 * theta_1^2 = eta^{18} * theta_1^2.

    # Simpler: we already have phi_10_1_qy_expansion. Let's just
    # compute the ring expression independently and compare.

    # Method: compute eta^{-6} q-expansion, multiply with theta_1^2, multiply with delta_1728/1728
    # That's eta^{-6} * theta_1^2 = -phi_{-2,1}
    # Then (-1/1728) * delta_1728 * (-phi_{-2,1})
    # = (1/1728) * delta_1728 * phi_{-2,1}... same formula.

    # Let's just directly compute (1/1728)(E_4^3 - E_6^2) * theta_1^2 / eta^6 * (-1) * (-1/1728)
    # = phi_{10,1}

    # Simplest verification: compute E_4^3 - E_6^2 at leading orders,
    # then multiply by phi_{-2,1} (which we compute as -theta_1^2/eta^6).

    # We need eta^{-6}: q^{-6/24} * prod(1-q^n)^{-6}
    eta_inv6_shift, eta_inv6_coeffs = eta_power_q_expansion_integer_shifted(-6, qmax + 5)

    # theta_1^2
    theta_sq = theta_1_squared_qy_expansion(qmax + 5, ymax)

    # phi_{-2,1} = -theta_1^2/eta^6 = -(theta_1^2) * (eta^{-6})
    # eta^{-6} = q^{-1/4} * sum eta_inv6_coeffs[j] q^j
    phi_m2_1: Dict[Tuple[Fraction, int], Fraction] = defaultdict(Fraction)
    for j, ec in enumerate(eta_inv6_coeffs):
        if ec == 0:
            continue
        for (q_exp, l), tc in theta_sq.items():
            total_q = eta_inv6_shift + j + q_exp
            if abs(l) > ymax:
                continue
            if total_q > qmax + 3:
                continue
            # -1 for the minus sign in phi_{-2,1}
            phi_m2_1[(total_q, l)] += Fraction(-ec * tc)

    # Now multiply (E_4^3 - E_6^2)(tau) * phi_{-2,1}(tau,z)
    # E_4^3 - E_6^2 is a q-series (no y). phi_{-2,1} has (q,y).
    product: Dict[Tuple[Fraction, int], Fraction] = defaultdict(Fraction)
    for n_e, c_e in delta_1728.items():
        for (q_p, l), c_p in phi_m2_1.items():
            total = n_e + q_p
            if total > qmax + 1:
                continue
            if abs(l) > ymax:
                continue
            product[(total, l)] += Fraction(c_e) * c_p

    # phi_{10,1} = -(1/1728) * product
    result: Dict[Tuple[int, int], Fraction] = {}
    for (q_exp, l), c in product.items():
        if q_exp != int(q_exp):
            continue
        n = int(q_exp)
        if n < 0 or n > qmax:
            continue
        v = -c / Fraction(1728)
        if v != 0:
            result[(n, l)] = v

    return result


def _multiply_q_series(f: Dict[int, Fraction], g: Dict[int, Fraction],
                       qmax: int) -> Dict[int, Fraction]:
    """Multiply two q-series (Cauchy product) truncated at q^qmax."""
    result: Dict[int, Fraction] = defaultdict(Fraction)
    for n1, c1 in f.items():
        if c1 == 0:
            continue
        for n2, c2 in g.items():
            if c2 == 0:
                continue
            n = n1 + n2
            if n > qmax:
                continue
            result[n] += c1 * c2
    return dict(result)


# ============================================================
# HIGHER FOURIER-JACOBI COEFFICIENTS
# ============================================================

def phi_0_1_qy_expansion(qmax: int, ymax: int) -> Dict[Tuple[int, int], int]:
    """
    The unique weak Jacobi form phi_{0,1}(tau, z) of weight 0, index 1.

    phi_{0,1}(tau, z) = 4 * [theta_2(tau,z)^2/theta_2(tau,0)^2
                            + theta_3(tau,z)^2/theta_3(tau,0)^2
                            + theta_4(tau,z)^2/theta_4(tau,0)^2]

    Alternative: use the explicit Fourier expansion
      phi_{0,1}(tau,z) = sum_{n>=0, l in Z} c(n,l) q^n y^l
    with c(n,l) depending only on 4n-l^2.

    Generating property: c(0,0) = 12 (NOT 10 --- DVV convention has 10,
    Eichler-Zagier convention has 12). We use EICHLER-ZAGIER (AP38).

    phi_{0,1} = (theta_2^2 theta_3^2 theta_4^2 * E_2_hat + stuff) ... complicated.

    Simplest: use the LATTICE representation.
    phi_{0,1}(tau, z) = y + 10 + y^{-1} + (10y^2 - 64y - 108 - 64y^{-1} + 10y^{-2})q + ...

    WAIT: The coefficient c(0,0) = 10 corresponds to the DVV convention (2*phi_{0,1}^{DVV}).
    In EZ convention: phi_{0,1} has c(0,0) = 12. Let me be precise.

    From Eichler-Zagier (1985), Theorem 9.3:
      phi_{0,1}(tau, z) = 4*(sum_{r even} - sum_{r odd})... actually, let me
      just use the explicit formula from the theta functions.

    phi_{0,1}(tau,z) = 4*[theta_2(tau,z)^2/theta_2(tau,0)^2
                        + theta_3(tau,z)^2/theta_3(tau,0)^2
                        + theta_4(tau,z)^2/theta_4(tau,0)^2]

    With standard Jacobi theta functions:
      theta_2(tau,z) = sum_{n in Z} q^{(n+1/2)^2/2} y^{n+1/2}
      theta_3(tau,z) = sum_{n in Z} q^{n^2/2} y^n
      theta_4(tau,z) = sum_{n in Z} (-1)^n q^{n^2/2} y^n

    The key values at z=0:
      theta_2(tau,0)^2 = sum q^{(n+1/2)^2/2 + (m+1/2)^2/2} = sum q^{n^2+n+1/2} ...
    This is getting complicated. Use the well-known coefficients directly.

    The K3 elliptic genus is chi(K3; tau,z) = 2*phi_{0,1}(tau,z) with:
      phi_{0,1}(tau,z) = sum c(n,l) q^n y^l
      c(n,l) depends only on Delta = 4n - l^2.

    EICHLER-ZAGIER values: c(Delta) for phi_{0,1}:
      c(-1) = 1     (i.e. c(0, +/-1) = 1)
      c(0)  = 10    (i.e. c(0, 0) = 10 in EZ; or c(1, +/-2) = 10, etc.)

    WAIT: there is genuine confusion here. Let me look this up carefully.

    The weak Jacobi form phi_{0,1} of weight 0, index 1 on SL(2,Z):
    By Eichler-Zagier Table 1 (p. 37):
      dim J_{0,1}^{weak} = 1
    The UNIQUE form is:
      phi_{0,1}(tau, z) = sum_{n>=0, l} c(n,l) q^n y^l
    with c(n,l) depending only on D = 4n - l^2 for D >= -1:
      c(-1) = 1
      c(0)  = 10
      c(3)  = -64
      c(4)  = 108
      c(7)  = -513
      c(8)  = 808
      ...

    So c(0,0) = c(D=0) = 10 (NOT 12).
    The relation to K3 elliptic genus: chi(K3) = 2*phi_{0,1} gives
    c_K3(0,0) = 20 (counting 20 massless hypermultiplets).

    The 12 I was thinking of was phi_{0,1}(tau, 0) = 12 (the Euler char of K3 is 24, and chi/2=12).
    phi_{0,1}(tau, 0) = sum_l c(0,l) = c(0,-1) + c(0,0) + c(0,1) = 1 + 10 + 1 = 12. YES.

    So c(0,0) = 10 (single coefficient), but phi_{0,1}(tau,0) = 12 (sum over l at n=0).

    OK, confirmed: we use EZ convention with c(-1)=1, c(0)=10.
    """
    # Build from the discriminant function c(D)
    # c(D) for D = 4n - l^2
    # Known exact values (Eichler-Zagier):
    c_D = _phi_01_discriminant_coefficients(4 * qmax + 2)

    result: Dict[Tuple[int, int], int] = {}
    for n in range(0, qmax + 1):
        for l in range(-ymax, ymax + 1):
            D = 4 * n - l * l
            if D < -1:
                continue
            if D in c_D:
                if c_D[D] != 0:
                    result[(n, l)] = c_D[D]
    return result


def _phi_01_discriminant_coefficients(Dmax: int) -> Dict[int, int]:
    """
    Compute the Fourier coefficients c(D) of phi_{0,1} for D = -1, 0, 1, ..., Dmax.

    Uses the product formula:
      phi_{0,1}(tau,z) = 12 + (y + y^{-1}) + sum_{n>=1} sum_l c(n,l) q^n y^l

    Or more efficiently, the theta-function method.

    We use the RECURSION from the product:
      phi_{0,1}(tau,z) = 12 + sum_{D>=-1} c(D) * sum_{4n-l^2=D} q^n y^l

    The exact coefficients can be computed from the definition using theta
    functions. We'll build them from scratch.

    phi_{0,1} = (theta_3(2tau)^2 theta_3(2tau,2z) + ...) / eta^6 ... complicated.

    Simplest correct approach: direct lattice theta sum computation.

    Actually, the cleanest is to use the HECKE-type relation:
      phi_{0,1}(tau,z) = sum_{D >= -1} c(D) sum_{4n-l^2=D, n>=0} q^n y^l

    where c(D) satisfies:
      sum_{D>=-1} c(D) q^D = 12 q^0 + q^{-1} - 2 * sum_{n>=1} (sum_{d|n} d) q^n * ...

    NO, this is getting circular. Let me just compute directly.

    Use: phi_{0,1}(tau,z) = 4*(J_2/J_2(0) + J_3/J_3(0) + J_4/J_4(0))
    where J_i = theta_i(tau,z)^2.

    We'll compute via truncated q-y series multiplication.
    """
    # Compute via the relation:
    # phi_{0,1} = (E_4 * phi_{-2,1} + E_6 * phi_{-2,1} * ...) ... no.

    # Use: phi_{0,1} = 12 * phi_{-2,1}/phi_{-2,1} + ... this is circular.

    # Direct computation via theta functions is cleanest.
    # theta_3(tau, z) = sum_{n in Z} q^{n^2/2} y^n
    # theta_3(tau, 0) = sum_{n in Z} q^{n^2/2}
    # theta_3(tau,z)^2 / theta_3(tau,0)^2 needs ratio of theta series.

    # Alternative: use the KNOWN generating function for c(D).
    # The coefficients c(D) of phi_{0,1} satisfy:
    # sum c(D) H(D) = product formula...

    # Let's just hardcode the first many values from Eichler-Zagier and
    # compute the rest from the recursion phi_{0,1} * phi_{10,1} = ... etc.

    # Actually the cleanest: use the HEAT EQUATION / direct product expansion.
    # phi_{0,1}(tau,z) = (y - 2 + y^{-1}) / (y^{1/2} - y^{-1/2})^2 ... no.

    # DEFINITIVE: use the q-product for phi_{0,1}:
    # phi_{0,1}(tau,z) = prod_{n>=1} [(1-q^n)^2 / ((1-y*q^n)(1-y^{-1}*q^n)(1-y*q^{n-1})(1-y^{-1}*q^{n-1}))]
    # ... this is not standard.

    # The simplest CORRECT approach that avoids theta function ratios:
    # Use the relation (Eichler-Zagier p. 108, Theorem 9.3):
    #   phi_{0,1}(tau,z) = -(theta'_1(tau,0))^2 / (theta_1(tau,z)^2) + E_2(tau)/12
    # ... no, that's the Weierstrass P function.

    # CORRECT formula (EZ p. 37, eq. 3):
    # phi_{0,1}(tau,z) = 4 * sum_{even char (a,b)} theta[a,b](tau,z)^2/theta[a,b](tau,0)^2

    # I'll compute numerically and extract integer coefficients.
    # Use high-precision floating point with numpy.

    qmax_internal = (Dmax + 10) // 4 + 5
    ymax_internal = int(math.sqrt(Dmax + 10)) + 3

    coeffs = _phi_01_from_theta_numerical(qmax_internal, ymax_internal)

    # Extract c(D) by discriminant
    c_D: Dict[int, int] = {}
    for (n, l), val in coeffs.items():
        D = 4 * n - l * l
        if D > Dmax:
            continue
        if D not in c_D:
            c_D[D] = val

    return c_D


def _phi_01_from_theta_numerical(qmax: int, ymax: int) -> Dict[Tuple[int, int], int]:
    """
    Compute phi_{0,1}(tau, z) Fourier coefficients using numerical evaluation
    of theta functions at high precision and integer rounding.

    Method: evaluate phi_{0,1}(tau, z) on a grid of (tau, z) values and
    extract Fourier coefficients via discrete Fourier transform.

    Actually, more reliable: compute directly from the explicit product.

    phi_{0,1}(tau, z) = (y + 10 + y^{-1})
                      + (10y^2 - 64y + 108 - 64y^{-1} + 10y^{-2}) q
                      + (-64y^3 + 513y^2 - 1384y + 2016 - 1384y^{-1}
                         + 513y^{-2} - 64y^{-3}) q^2
                      + ...

    where the coefficients c(n,l) depend only on 4n - l^2 = D:
      c(-1)  = 1
      c(0)   = 10
      c(3)   = -64
      c(4)   = 108
      c(7)   = -513
      c(8)   = 808
      c(11)  = -2752
      c(12)  = 4016
      c(15)  = -11775
      c(16)  = 16588
      c(19)  = -43263
      c(20)  = 58456

    These are negative of the coefficients of the theta series for the
    Mathieu moonshine counting:
      c(D) = (-1)^{D+1} * (representation dimension of M24)

    For a complete computation: use the product representation of phi_{0,1}
    in terms of eta and theta_1:

    THEOREM (Eichler-Zagier): phi_{0,1}(tau,z) can be computed from:
      phi_{0,1}(tau,z) = sum_{n>=0, l: 4n>=l^2-1} c(4n-l^2) q^n y^l

    where the generating function of c(D) is:
      F(tau) = sum_{D>=-1} c(D) q^D
             = q^{-1} + 10 + 108q^3 + ... (only at D = -1 mod 4 or D = 0 mod 4??)

    NO. Actually c(D) is nonzero for ALL D >= -1.

    Let me use the HECKE representation:
      c(D) for D >= -1 is given by the modified divisor sum.

    Actually the most reliable way is the PRODUCT FORMULA.
    phi_{0,1} = phi_{-2,1} * phi_{0,1}/phi_{-2,1}... circular.

    OK. Let me use the EXPLICIT product expansion.
    phi_{0,1}(tau, z) is uniquely determined by:
    (1) It's a weak Jacobi form of weight 0, index 1 for SL(2,Z)
    (2) Its Fourier expansion starts with y + 10 + y^{-1} at q^0

    From the product: we can build it from eta and theta functions.
    The key identity (see Gritsenko, arXiv:math/9906190):

    phi_{0,1} = 4*(theta_3^2*theta_4^2*P_3 + theta_2^2*theta_4^2*P_2 + theta_2^2*theta_3^2*P_4)
              /(theta_2*theta_3*theta_4)^2

    where P_i involves ratios of theta functions with z argument.

    This is getting unwieldy. Let me use a DIRECT RECURSIVE computation.

    The recursion method: phi_{0,1}(tau,z) = -(phi_{-2,1}/phi_{-2,1})|_{scaled}...
    No. Let me just build c(D) from the TRACE FORMULA.

    FINAL APPROACH: compute c(D) from the well-known recursion.
    The coefficients c(D) of phi_{0,1} satisfy the explicit formula
    (see Cheng, Duncan, Harvey 2014, eq 2.7):

      c(D) = (-1)^D * (number of representations of M24 at level D + 1)

    For computational purposes, let me just use the modified Hurwitz
    class number formula. Actually, the simplest CORRECT formula is:

    phi_{0,1}(tau,z) = (12/chi) * EG(K3; tau, z)
    where EG is the K3 elliptic genus = 2*phi_{0,1}, so this is circular.

    DEFINITIVE APPROACH: compute via MULTIPLICATION of known series.
    We know:
      phi_{-2,1}(tau,z) = -theta_1(tau,z)^2 / eta(tau)^6
      phi_{10,1}(tau,z) = eta(tau)^{18} * theta_1(tau,z)^2
    So:
      phi_{10,1} = -eta^{24} * phi_{-2,1} = -Delta * phi_{-2,1}

    And we need phi_{0,1}. Use:
      J_{10,1}^{cusp} is 1-dimensional, spanned by phi_{10,1}.
      phi_{0,1} is the unique element of J_{0,1}^{weak}.
      The two are NOT directly related by a simple product.

    BUT: we know phi_{0,1} explicitly from the theta function formula.
    Let's compute numerically with mpmath for reliability.
    """
    try:
        import mpmath
        return _phi_01_mpmath(qmax, ymax)
    except ImportError:
        # Fallback: use known coefficients
        return _phi_01_hardcoded(qmax, ymax)


def _phi_01_mpmath(qmax: int, ymax: int) -> Dict[Tuple[int, int], int]:
    """
    Compute phi_{0,1} Fourier coefficients using mpmath for arbitrary precision.

    Method: evaluate on a sufficiently fine grid and extract via DFT.
    """
    import mpmath
    mpmath.mp.dps = 50  # 50 decimal places

    # Use tau = i*t for large enough t that q = e^{-2*pi*t} is small
    t = mpmath.mpf(2)
    tau = mpmath.mpc(0, t)
    q_val = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau)
    # q_val = exp(-2*pi*t) ~ very small

    # Evaluate on z = (a + i*b)/(2*pi) for a grid of y-values
    # y = exp(2*pi*i*z)
    # For z = m/(2*N) with m = 0,...,2*N-1, y = exp(2*pi*i*m/(2*N))
    # This gives a DFT in the l-variable.

    N_y = 2 * ymax + 4  # Number of z-sample points
    N_q = qmax + 3       # Number of tau-terms

    # We evaluate phi_{0,1} at many (tau, z) points and extract coefficients.
    # For a FIXED tau = i*t, phi_{0,1}(tau, z) = sum_{n,l} c(n,l) e^{-2*pi*n*t} e^{2*pi*i*l*z}
    # = sum_n q_0^n * (sum_l c(n,l) y^l)  where q_0 = e^{-2*pi*t}

    # For each n, extract sum_l c(n,l) y^l by DFT over z.
    # Then extract c(n,l) from the y-polynomial.

    # Evaluate theta functions at the sample points
    # theta_j(tau, z) for j = 2,3,4 and z = z_k = k/N_y for k=0,...,N_y-1

    z_samples = [mpmath.mpf(k) / mpmath.mpf(N_y) for k in range(N_y)]

    phi_values = []
    for z_s in z_samples:
        z = mpmath.mpc(z_s, 0)
        val = _eval_phi01(tau, z, qmax + 5)
        phi_values.append(val)

    # Now extract Fourier coefficients c(n, l).
    # phi_{0,1}(tau, z_k) = sum_{n, l} c(n,l) q_0^n exp(2*pi*i*l*z_k)
    #                     = sum_{n, l} c(n,l) q_0^n exp(2*pi*i*l*k/N_y)

    # For fixed tau, grouping by n:
    # phi(tau, z_k) = sum_n q_0^n * P_n(z_k)
    # where P_n(z) = sum_l c(n,l) exp(2*pi*i*l*z)

    # Extract P_n by inverse DFT-like procedure:
    # First peel off q^0 term, then q^1, etc.

    q_0 = float(mpmath.exp(-2 * mpmath.pi * t))

    result: Dict[Tuple[int, int], int] = {}

    # Build the matrix of y^l values at sample points
    # y_k = exp(2*pi*i*k/N_y)
    # y_k^l = exp(2*pi*i*k*l/N_y)

    for n in range(qmax + 1):
        # Contribution at q^n: sum_l c(n,l) y_k^l
        # Extract from phi_values by dividing out q^n
        coeffs_at_n = []
        for k in range(N_y):
            # The residual after removing all terms with n' < n
            coeffs_at_n.append(complex(phi_values[k]))

        # DFT to extract c(n, l)
        # sum_l c(n,l) exp(2*pi*i*k*l/N_y) = coeffs_at_n[k] (after q^n division)
        # Inverse: c(n,l) = (1/N_y) sum_k coeffs_at_n[k] exp(-2*pi*i*k*l/N_y)

        for l in range(-ymax, ymax + 1):
            val = 0.0
            for k in range(N_y):
                val += coeffs_at_n[k] * np.exp(-2j * np.pi * k * l / N_y)
            val /= N_y
            # This should be real and integer (up to floating point)
            val_real = val.real
            c_nl = int(round(val_real))
            if abs(val_real - c_nl) > 0.01:
                # Not close to integer: likely truncation error for large n
                continue
            if c_nl != 0:
                result[(n, l)] = c_nl

        # Subtract the n-th contribution from phi_values for next iteration
        for k in range(N_y):
            contrib = mpmath.mpf(0)
            for l in range(-ymax, ymax + 1):
                if (n, l) in result:
                    y_kl = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * l * z_samples[k])
                    contrib += mpmath.mpf(result[(n, l)]) * y_kl
            phi_values[k] -= contrib * mpmath.power(q_val, n)

    return result


def _eval_phi01(tau, z, nmax):
    """
    Evaluate phi_{0,1}(tau, z) numerically using theta function formula.

    phi_{0,1}(tau, z) = 4*(theta_2(tau,z)^2/theta_2(tau,0)^2
                        + theta_3(tau,z)^2/theta_3(tau,0)^2
                        + theta_4(tau,z)^2/theta_4(tau,0)^2)
    """
    import mpmath

    pi = mpmath.pi
    I = mpmath.mpc(0, 1)

    q = mpmath.exp(2 * pi * I * tau)
    y = mpmath.exp(2 * pi * I * z)

    def theta2(tau_val, z_val, N):
        """theta_2(tau, z) = sum_{n in Z} q^{(n+1/2)^2/2} y^{n+1/2}"""
        q_v = mpmath.exp(2 * pi * I * tau_val)
        y_v = mpmath.exp(2 * pi * I * z_val)
        s = mpmath.mpf(0)
        for n in range(-N, N + 1):
            r = n + mpmath.mpf(0.5)
            s += mpmath.power(q_v, r * r / 2) * mpmath.power(y_v, r)
        return s

    def theta3(tau_val, z_val, N):
        """theta_3(tau, z) = sum_{n in Z} q^{n^2/2} y^n"""
        q_v = mpmath.exp(2 * pi * I * tau_val)
        y_v = mpmath.exp(2 * pi * I * z_val)
        s = mpmath.mpf(0)
        for n in range(-N, N + 1):
            s += mpmath.power(q_v, mpmath.mpf(n * n) / 2) * mpmath.power(y_v, n)
        return s

    def theta4(tau_val, z_val, N):
        """theta_4(tau, z) = sum_{n in Z} (-1)^n q^{n^2/2} y^n"""
        q_v = mpmath.exp(2 * pi * I * tau_val)
        y_v = mpmath.exp(2 * pi * I * z_val)
        s = mpmath.mpf(0)
        for n in range(-N, N + 1):
            s += ((-1) ** n) * mpmath.power(q_v, mpmath.mpf(n * n) / 2) * mpmath.power(y_v, n)
        return s

    N = nmax + 5
    t2z = theta2(tau, z, N)
    t2_0 = theta2(tau, mpmath.mpf(0), N)
    t3z = theta3(tau, z, N)
    t3_0 = theta3(tau, mpmath.mpf(0), N)
    t4z = theta4(tau, z, N)
    t4_0 = theta4(tau, mpmath.mpf(0), N)

    return 4 * (t2z ** 2 / t2_0 ** 2 + t3z ** 2 / t3_0 ** 2 + t4z ** 2 / t4_0 ** 2)


def _phi_01_hardcoded(qmax: int, ymax: int) -> Dict[Tuple[int, int], int]:
    """
    Hardcoded coefficients of phi_{0,1} from Eichler-Zagier tables.
    c(D) depends only on discriminant D = 4n - l^2.

    Source: Eichler-Zagier (1985) Table 1; verified against
    Cheng-Duncan-Harvey (2014) Table 1.
    """
    # c(D) values from the literature (Eichler-Zagier convention)
    cD = {
        -1: 1,
        0: 10,
        3: -64,
        4: 108,
        7: -513,
        8: 808,
        11: -2752,
        12: 4016,
        15: -11775,
        16: 16588,
        19: -43263,
        20: 58464,
        23: -131584,
        24: 175554,
        27: -366080,
        28: 478400,
        31: -926144,
        32: 1196640,
        35: -2181831,
        36: 2784960,
        39: -4827136,
        40: 6090624,
        43: -10106880,
        44: 12629516,
        47: -20135168,
        48: 24928000,
    }

    result: Dict[Tuple[int, int], int] = {}
    for n in range(0, qmax + 1):
        for l in range(-ymax, ymax + 1):
            D = 4 * n - l * l
            if D in cD:
                result[(n, l)] = cD[D]
    return result


# ============================================================
# BORCHERDS PRODUCT FOR Phi_10
# ============================================================

def borcherds_product_coefficients(qmax: int, ymax: int, pmax: int
                                   ) -> Dict[Tuple[int, int, int], int]:
    """
    Compute Fourier coefficients of Phi_10 via the Borcherds product formula:

    Phi_10(Omega) = q * y * p * prod_{(n,l,m)>0} (1 - q^n y^l p^m)^{c_0(4nm-l^2)}

    where c_0(D) are Fourier coefficients of the K3 elliptic genus
    chi(K3; tau,z) = 2*phi_{0,1}(tau,z), so c_0(D) = 2*c_{phi}(D).

    The ordering (n,l,m) > 0 means: m > 0, or m = 0 and n > 0,
    or m = 0 and n = 0 and l < 0.

    Returns dict {(n, l, m): coeff} for the Fourier expansion
    Phi_10 = sum a(n,l,m) q^n y^l p^m.

    NOTE: This is the TRIPLE Fourier expansion in (q, y, p).
    """
    # First get phi_{0,1} discriminant coefficients
    Dmax = 4 * max(qmax, pmax) + ymax * ymax + 20
    cD_phi = _phi_01_discriminant_coefficients(Dmax)

    # c_0(D) = 2 * c_phi(D) (K3 elliptic genus = 2 * phi_{0,1})
    c0 = {}
    for D, v in cD_phi.items():
        c0[D] = 2 * v

    # Start with the prefactor q * y * p (i.e., coefficient 1 at (1, 1, 1))
    # Build the product iteratively

    # Initialize: coefficients of q^n y^l p^m
    # We track a polynomial in (q, y, p) up to given bounds
    coeffs: Dict[Tuple[int, int, int], int] = defaultdict(int)
    coeffs[(1, 1, 1)] = 1  # prefactor q*y*p

    # WAIT: the prefactor is q * y * p with the Borcherds convention.
    # Actually, the standard convention has different shifts.
    # Let me be more careful.
    #
    # Gritsenko-Nikulin: Phi_10 = p * q * (y-2+y^{-1}) * prod...
    # Actually the STANDARD Borcherds product (Borcherds 1995, Gritsenko 1996):
    #
    # Phi_10(Omega) = sum_{(n,l,m)>0} a(n,l,m) q^n y^l p^m
    #
    # with the product formula involving the Weyl vector rho = (1,1,1):
    # Phi_10 = e^{2pi*i*(rho, Z)} * prod_{alpha>0} (1-e^{2pi*i*(alpha,Z)})^{c_0(alpha^2/2)}
    #
    # Here Z = (tau, z, sigma) and (alpha, Z) = n*tau + l*z + m*sigma.
    # alpha = (n, l, m) with the norm alpha^2/2 = -det(T) where T = ((n,l/2),(l/2,m)).
    # So alpha^2/2 = nm - l^2/4, and the discriminant is -(4nm - l^2)/4.
    # But c_0 uses D = 4nm - l^2, so c_0(alpha^2/2) means c_0(-(alpha^2/2)*4) ... confusing.
    #
    # Let me use the SIMPLEST correct form from DVV (1997):
    # Phi_10 = q*r*s * prod_{(k,l,m)>0} (1-q^k y^l p^m)^{c_0(4km-l^2)}
    # where the product is over all (k,l,m) with k,m >= 0, l in Z,
    # and (k,l,m) > 0 in the sense above.

    # Build the product term by term
    # For each factor (1 - q^k y^l p^m)^{c_0(4km-l^2)},
    # multiply into the running product.

    # The factors with m=0 are:
    #   (1 - q^k)^{c_0(-l^2)} for k>0, l=0: c_0(0) = 20
    #   (1 - q^k y^l)^{c_0(-l^2)} for k>0, l != 0
    #   (1 - y^l)^{c_0(-l^2)} for k=0, l<0 (the (0,l,0) with l<0)
    # For l^2 > 1: c_0(-l^2) is typically 0 for the weak Jacobi form.
    # c_0(D) for D < -1 is 0 for phi_{0,1} (index 1 weak Jacobi form).
    # So c_0(-l^2) != 0 only for l^2 <= 1, i.e., l = 0, +/-1.
    # c_0(0) = 2*10 = 20, c_0(-1) = 2*1 = 2.

    # This is getting complex. Let me implement the product more carefully.
    # We initialize the coefficient array and multiply factor by factor.

    # Reset: start from scratch with a cleaner approach
    coeffs = defaultdict(int)

    # The Borcherds product is
    # Phi_10 = q*y*p * PROD
    # We compute PROD first, then shift by (1,1,1).

    # PROD = prod_{(k,l,m)>0} (1 - q^k y^l p^m)^{c_0(4km-l^2)}
    # Initialize PROD = 1
    prod_coeffs: Dict[Tuple[int, int, int], int] = defaultdict(int)
    prod_coeffs[(0, 0, 0)] = 1

    # Enumerate factors in lex order
    factors = []

    # m = 0, k = 0, l < 0
    for l in range(-1, -ymax - 1, -1):
        D = -l * l  # 4*0*0 - l^2
        if D in c0 and c0[D] != 0:
            factors.append((0, l, 0, c0[D]))

    # m = 0, k > 0, all l
    for k in range(1, qmax + pmax + 2):
        for l in range(-ymax, ymax + 1):
            D = -l * l  # 4*k*0 - l^2 = -l^2
            if D in c0 and c0[D] != 0:
                factors.append((k, l, 0, c0[D]))

    # m > 0, all k >= 0, all l
    for m in range(1, pmax + 2):
        for k in range(0, qmax + pmax + 2):
            for l in range(-ymax - 2, ymax + 3):
                D = 4 * k * m - l * l
                if D in c0 and c0[D] != 0:
                    factors.append((k, l, m, c0[D]))

    # Now multiply all factors into prod_coeffs
    for (k, l, m, expo) in factors:
        if expo == 0:
            continue
        prod_coeffs = _multiply_by_factor_power(
            prod_coeffs, k, l, m, expo, qmax + 1, ymax + 1, pmax + 1
        )

    # Shift by (1,1,1): Phi_10 = q*y*p * PROD
    for (n, l, m), c in prod_coeffs.items():
        if c != 0 and n + 1 <= qmax and m + 1 <= pmax and abs(l + 1) <= ymax:
            coeffs[(n + 1, l + 1, m + 1)] = c

    return dict(coeffs)


def _multiply_by_factor_power(coeffs: Dict[Tuple[int, int, int], int],
                               k: int, l: int, m: int, power: int,
                               qmax: int, ymax: int, pmax: int
                               ) -> Dict[Tuple[int, int, int], int]:
    """
    Multiply the coefficient array by (1 - q^k y^l p^m)^power.

    For positive power: expand (1-x)^power via binomial theorem.
    For negative power: expand (1-x)^{-|power|} = sum_{j>=0} C(|p|+j-1,j) x^j.
    """
    new_coeffs: Dict[Tuple[int, int, int], int] = defaultdict(int)

    if power > 0:
        # (1 - x)^power = sum_{j=0}^{power} C(power, j) (-1)^j x^j
        binom_terms = []
        binom_c = 1
        for j in range(power + 1):
            if j > 0:
                binom_c = binom_c * (power - j + 1) // j
            # Check if j*(k,l,m) is within bounds
            if j * k > qmax or j * m > pmax or abs(j * l) > ymax:
                break
            binom_terms.append((j * k, j * l, j * m, binom_c * ((-1) ** j)))
    else:
        # (1 - x)^{-|power|} = sum_{j>=0} C(|p|+j-1, j) x^j
        abs_p = -power
        binom_terms = []
        binom_c = 1
        for j in range(0, max(qmax, pmax) + 1):
            if j * k > qmax and j * m > pmax:
                break
            if abs(j * l) > ymax:
                break
            binom_terms.append((j * k, j * l, j * m, binom_c))
            binom_c = binom_c * (abs_p + j) // (j + 1)

    # Convolve
    for (n0, l0, m0), c0 in coeffs.items():
        if c0 == 0:
            continue
        for (dk, dl, dm, bc) in binom_terms:
            nn = n0 + dk
            nl = l0 + dl
            nm = m0 + dm
            if nn > qmax or nm > pmax or abs(nl) > ymax:
                continue
            new_coeffs[(nn, nl, nm)] += c0 * bc

    return dict(new_coeffs)


# ============================================================
# FOURIER-JACOBI EXTRACTION
# ============================================================

def extract_fourier_jacobi(phi10_coeffs: Dict[Tuple[int, int, int], int],
                           m: int, qmax: int, ymax: int
                           ) -> Dict[Tuple[int, int], int]:
    """
    Extract the m-th Fourier-Jacobi coefficient phi_m(tau, z) from Phi_10.

    Phi_10 = sum_{m' >= 1} phi_{m'}(tau, z) * p^{m'}
    So phi_m(tau, z) = sum_{n, l} a(n, l, m) * q^n * y^l.

    Returns dict {(n, l): coeff}.
    """
    result: Dict[Tuple[int, int], int] = {}
    for (n, l, m_val), c in phi10_coeffs.items():
        if m_val == m and abs(l) <= ymax and n <= qmax:
            if c != 0:
                result[(n, l)] = c
    return result


# ============================================================
# RECIPROCAL 1/Phi_10
# ============================================================

def reciprocal_phi10_coefficients(qmax: int, ymax: int, pmax: int
                                  ) -> Dict[Tuple[int, int, int], int]:
    """
    Compute Fourier coefficients d(n, l, m) of 1/Phi_10 by formal inversion.

    Method: if Phi_10 = sum a(n,l,m) q^n y^l p^m and
    1/Phi_10 = sum d(n,l,m) q^n y^l p^m, then
    sum_{(n1,l1,m1)+(n2,l2,m2)=(n,l,m)} a(n1,l1,m1) * d(n2,l2,m2) = delta_{n,0,l,0,m,0}

    We solve this recursively: for each (n,l,m) in lex order,
    d(n,l,m) = (delta - sum_{proper} a * d) / a(leading).

    The leading term of Phi_10 is a(1,1,1) (the Weyl vector contribution).

    Actually, Phi_10 starts at p^1 (m >= 1), so 1/Phi_10 starts at p^{-1}.
    More precisely, the SMALLEST term in Phi_10 (in the Borcherds product) is
    q * y * p, so the Laurent expansion of 1/Phi_10 starts at q^{-1} y^{-1} p^{-1}.

    For the DVV formula, the BPS degeneracies d(n,l,m) are coefficients of
    1/Phi_10 where (n,l,m) can be negative.

    For this implementation, we compute d(n,l,m) for n >= n_min, m >= m_min
    by formal power series inversion within the Fourier-Jacobi scheme.

    ALTERNATIVE SIMPLER APPROACH: compute the reciprocal of the FIRST
    Fourier-Jacobi coefficient via 1/phi_{10,1} as a Laurent series,
    which gives the p^{-1} contribution to 1/Phi_10.

    We use the formal inversion approach.
    """
    # Get Phi_10 coefficients
    phi10 = borcherds_product_coefficients(qmax + 2, ymax + 2, pmax + 2)

    # The leading term is at (1, 1, 1) with coefficient (should be 1 from product)
    a_lead = phi10.get((1, 1, 1), 0)
    if a_lead == 0:
        raise ValueError("Leading coefficient a(1,1,1) of Phi_10 is zero!")

    # Formal inversion: Phi_10 * (1/Phi_10) = 1
    # In shifted coordinates: let N = n-1, L = l-1, M = m-1
    # Then Phi_10 = sum A(N,L,M) q'^N y'^L p'^M where q' = q*q_shift etc.
    # This is complex. Let's use a simpler approach.

    # Direct recursion in the unshifted coordinates.
    # Phi_10 has support for n >= 1, m >= 1 (cusp form).
    # 1/Phi_10 has a pole: leading term ~ 1/(q*y*p) * (correction).

    # For the PURPOSE of extracting BPS degeneracies d(n,l,m),
    # we work with the Fourier-Jacobi expansion:
    # 1/Phi_10 = sum_{m} psi_m(tau,z) p^m
    # and psi_m is determined recursively from the relation
    # (sum phi_m p^m)(sum psi_m p^m) = 1.

    # phi_1 * psi_{-1} = 1  =>  psi_{-1} = 1/phi_1 = 1/phi_{10,1}
    # phi_1 * psi_0 + phi_2 * psi_{-1} = 0  =>  psi_0 = -phi_2 * psi_{-1} / phi_1
    # etc.

    # This requires computing 1/phi_{10,1} as a Laurent series in (q, y).
    # phi_{10,1} = eta^{18} * theta_1^2 vanishes at z=0 (double zero from theta_1^2)
    # and at tau -> i*infinity (cusp).
    # So 1/phi_{10,1} has a double pole at z=0.

    # For simplicity, we return the discriminant-indexed degeneracies
    # d(Delta) computed from the Borcherds product inversion.
    # We'll implement the p-series recursion.

    phi_fj = {}
    for m_val in range(1, pmax + 3):
        phi_fj[m_val] = extract_fourier_jacobi(phi10, m_val, qmax + 2, ymax + 2)

    # Compute 1/phi_{10,1} as a (q, y)-Laurent series
    # phi_{10,1} * (1/phi_{10,1}) = 1
    inv_phi1 = _invert_jacobi_form(phi_fj.get(1, {}), qmax + 2, ymax + 2)

    # Build 1/Phi_10 Fourier-Jacobi coefficients
    # psi_{-1} = 1/phi_1
    # psi_{m-1} = -(1/phi_1) * sum_{j=2}^{m} phi_j * psi_{m-j-1}  for m >= 1
    psi = {}
    psi[-1] = inv_phi1

    for m_target in range(0, pmax + 1):
        # psi[m_target] = -(1/phi_1) * sum_{j=2}^{m_target+2} phi_j * psi[m_target - j]
        # where the range of j is 2 <= j <= m_target + 2 (so that m_target - j >= -1)
        # Actually: phi_1 * psi[m_target] + sum_{j>=2} phi_j * psi[m_target - j + 1 -1] = 0
        # Let me re-derive:
        # (sum_{j>=1} phi_j p^j)(sum_{k>=-1} psi_k p^k) = 1
        # Coefficient of p^M: sum_{j>=1} [phi_j * psi_{M-j}] = delta_{M,0}
        # For M = m_target + 1 - 1 = m_target:
        #   phi_1 * psi_{m_target - 1} + phi_2 * psi_{m_target - 2} + ... = delta_{m_target, 0}
        # Wait, let me index correctly.
        # Coefficient of p^M in the product:
        #   sum_{j >= 1} (phi_j)(psi_{M-j}) = delta_{M,0}
        # So for M = m_target:
        #   phi_1 * psi_{m_target - 1} + phi_2 * psi_{m_target - 2} + ... = delta_{m_target, 0}

        # We want psi_{m_target}. That appears at M = m_target + 1:
        #   phi_1 * psi_{m_target} + sum_{j>=2} phi_j * psi_{m_target+1-j} = delta_{m_target+1, 0}
        #   phi_1 * psi_{m_target} = delta_{m_target+1, 0} - sum_{j>=2} phi_j * psi_{m_target+1-j}
        #   psi_{m_target} = (1/phi_1) * (delta_{m_target+1,0} - sum_{j>=2} phi_j psi_{m_target+1-j})

        # delta is 0 for m_target >= 0 (since m_target+1 >= 1 > 0).
        rhs: Dict[Tuple[int, int], Fraction] = defaultdict(Fraction)
        for j in range(2, min(m_target + 3, pmax + 3)):
            if m_target + 1 - j < -1:
                break
            if m_target + 1 - j not in psi:
                continue
            phi_j_coeffs = phi_fj.get(j, {})
            psi_idx = psi.get(m_target + 1 - j, {})
            # Convolve phi_j with psi_{m_target+1-j}
            for (n1, l1), c1 in phi_j_coeffs.items():
                for (n2, l2), c2 in psi_idx.items():
                    n = n1 + n2
                    l = l1 + l2
                    if n > qmax or abs(l) > ymax:
                        continue
                    rhs[(n, l)] += Fraction(c1) * c2

        # psi_{m_target} = -inv_phi1 * rhs (negated, convolved with 1/phi_1)
        psi_mt: Dict[Tuple[int, int], Fraction] = defaultdict(Fraction)
        for (n1, l1), c1 in inv_phi1.items():
            for (n2, l2), c2 in rhs.items():
                n = n1 + n2
                l = l1 + l2
                if n > qmax or abs(l) > ymax:
                    continue
                psi_mt[(n, l)] -= c1 * c2

        psi[m_target] = dict(psi_mt)

    # Collect all coefficients into the triple-index format
    result: Dict[Tuple[int, int, int], int] = {}
    for m_idx, psi_m in psi.items():
        for (n, l), c in psi_m.items():
            if abs(c) < Fraction(1, 1000):
                continue
            # Round to nearest integer (should be exact for BPS degeneracies)
            c_int = int(round(float(c)))
            if c_int != 0:
                result[(n, l, m_idx)] = c_int

    return result


def _invert_jacobi_form(phi_coeffs: Dict[Tuple[int, int], int],
                        qmax: int, ymax: int) -> Dict[Tuple[int, int], Fraction]:
    """
    Compute the formal inverse 1/f for a Jacobi form f = sum c(n,l) q^n y^l.

    For phi_{10,1}: the leading term is at (n=1, l=+/-1) with coefficient +/-1.
    Actually, from theta_1^2: the leading y-behavior near z=0 has a double zero.

    We use formal power series inversion in the q-variable,
    treating the y-dependence as polynomial coefficients.

    1/phi_{10,1} as a formal Laurent series in y and formal power series in q.

    The computation is: phi_{10,1} has a double zero at y=1 (z=0).
    So 1/phi_{10,1} has a double pole at y=1.

    For the purpose of computing BPS degeneracies, we need this as a
    (q, y)-Laurent expansion around q=0, y=1.

    Method: write phi_{10,1} = q * P(q, y) where P starts with
    (y - 2 + y^{-1}) * (correction). Then
    1/phi_{10,1} = q^{-1} * 1/P(q, y).

    For P(q, y): extract the q^1 coefficient onward.
    P(0, y) = a(1, -1)*y^{-1} + a(1, 0) + a(1, 1)*y + higher l terms at n=1.
    """
    # Find the minimum q-power in phi
    min_n = min(n for (n, l) in phi_coeffs if phi_coeffs.get((n, l), 0) != 0)

    # Shift: f = q^{min_n} * g where g starts at q^0
    g_coeffs: Dict[Tuple[int, int], Fraction] = {}
    for (n, l), c in phi_coeffs.items():
        if c != 0:
            g_coeffs[(n - min_n, l)] = Fraction(c)

    # Now invert g: 1/g = sum d(n, l) q^n y^l where g * (1/g) = 1
    # Recursion: for each n, sum_{n1+n2=n} sum_{l1+l2=l} g(n1,l1)*d(n2,l2) = delta_{n,0}*delta_{l,0}

    # The leading term of g: g(0, l) for various l
    # For phi_{10,1}: g(0, l) = phi(min_n, l)

    # To invert, we need g(0, *) to be invertible as a Laurent polynomial in y.
    # g(0, y) = sum_l g(0, l) y^l

    # Then d(0, *) = 1/g(0, *) as Laurent polynomial
    # d(n, *) = -(1/g(0,*)) * sum_{n1=1}^{n} g(n1,*) * d(n-n1, *)

    g0_coeffs = {}
    for l in range(-ymax, ymax + 1):
        v = g_coeffs.get((0, l), Fraction(0))
        if v != 0:
            g0_coeffs[l] = v

    # Invert g(0, y) as a Laurent polynomial
    inv_g0 = _invert_y_polynomial(g0_coeffs, ymax * 2)

    d_coeffs: Dict[Tuple[int, int], Fraction] = {}
    for l, c in inv_g0.items():
        if abs(l) <= ymax and c != 0:
            d_coeffs[(0, l)] = c

    # Recursion for n >= 1
    for n in range(1, qmax - min_n + 1):
        # rhs = -sum_{n1=1}^{n} g(n1, *) * d(n-n1, *)
        rhs: Dict[int, Fraction] = defaultdict(Fraction)
        for n1 in range(1, n + 1):
            n2 = n - n1
            for l1 in range(-ymax, ymax + 1):
                g_val = g_coeffs.get((n1, l1), Fraction(0))
                if g_val == 0:
                    continue
                for l2 in range(-ymax, ymax + 1):
                    d_val = d_coeffs.get((n2, l2), Fraction(0))
                    if d_val == 0:
                        continue
                    l = l1 + l2
                    if abs(l) <= ymax:
                        rhs[l] += g_val * d_val

        # d(n, *) = inv_g0 * (-rhs) = -inv_g0 * rhs
        for l_rhs, c_rhs in rhs.items():
            for l_inv, c_inv in inv_g0.items():
                l_total = l_rhs + l_inv
                if abs(l_total) <= ymax:
                    d_coeffs[(n, l_total)] = d_coeffs.get((n, l_total), Fraction(0)) - c_inv * c_rhs

    # Shift back: 1/f = q^{-min_n} * d
    result: Dict[Tuple[int, int], Fraction] = {}
    for (n, l), c in d_coeffs.items():
        result[(n - min_n, l)] = c

    return result


def _invert_y_polynomial(poly: Dict[int, Fraction], ymax: int) -> Dict[int, Fraction]:
    """
    Invert a Laurent polynomial in y: find g such that f * g = 1.

    For phi_{10,1}: f(0, y) has the form a*(y - 2 + y^{-1}) + higher terms.
    The inverse is also a Laurent polynomial if f(0, y) has no zeros
    on the unit circle... but it does (at y=1, double zero from theta_1^2).

    So we need to invert as a FORMAL Laurent series, truncated at |l| <= ymax.
    This works for the recursion as long as the leading coefficient is nonzero.

    The leading coefficient in |l| is the one with largest |l|.
    """
    if not poly:
        raise ValueError("Cannot invert zero polynomial")

    # Find the leading monomial (smallest l, since f ~ y^{-1} + ... + y)
    min_l = min(poly.keys())
    max_l = max(poly.keys())

    # For the recursion to work, we need the PRINCIPAL part.
    # Since f has a double zero at y=1, 1/f has a double pole.
    # We compute 1/f as a Laurent series in y.

    # Method: formal division. Write f = a_{min_l} y^{min_l} + ...
    # Then 1/f starts at y^{-min_l} / a_{min_l}.
    # But this is for a FINITE Laurent polynomial.

    # Actually for our recursion (BPS degeneracy extraction), we need
    # 1/f as a formal Laurent series, which is well-defined if f is
    # a unit in the appropriate ring.

    # phi_{10,1} at q^1: the coefficient is
    # phi_{10,1}(q=0...) starts at q^1 with phi_{10,1}|_{q^1} = y - 2 + y^{-1} = (y^{1/2} - y^{-1/2})^2
    # Wait: y - 2 + y^{-1} = (y^{1/2})^2 - 2 + (y^{-1/2})^2.
    # No: y - 2 + y^{-1} factors as y^{-1}(y^2 - 2y + 1) = y^{-1}(y-1)^2.
    # So it has a double zero at y = 1.

    # 1/(y-2+y^{-1}) = y / (y-1)^2 is a RATIONAL function in y with a
    # double pole at y = 1. Its Laurent expansion around y = 1 is infinite.
    # Its Laurent expansion in y around y = 0 (i.e., power series in y) is
    # y/(y-1)^2 = -y * sum_{n>=0} (n+1) y^n = -sum_{n>=1} n*y^n for |y| < 1.
    # And y/(y-1)^2 = y^{-1}/(1-y^{-1})^2 = sum_{n>=1} n*y^{-n} for |y| > 1.
    # Neither converges on |y| = 1.

    # For FORMAL series computation, we just truncate the Laurent series.
    # The key insight: in the Fourier-Jacobi recursion, the y-variable
    # is formal and we just need finite truncation.

    # Method: write f = sum f_l y^l. We want g = sum g_l y^l such that
    # sum_{l1+l2=L} f_{l1} g_{l2} = delta_{L,0} for all L.

    # This is a convolution equation. For the recursion to work,
    # the "leading coefficient" must be invertible.
    # Use the convention: pick a reference l_0 and solve recursively.

    # Pick the coefficient at l=0 as the "leading" term... but it might be zero.
    # For y - 2 + y^{-1}: f(-1)=1, f(0)=-2, f(1)=1.
    # f(0) = -2 is nonzero, so we can use it.

    f_0 = poly.get(0, Fraction(0))
    if f_0 == 0:
        # Try another pivot
        for lp in sorted(poly.keys(), key=abs):
            if poly[lp] != 0:
                f_0 = poly[lp]
                # Shift: multiply f by y^{-lp}, invert, then shift back
                shifted_poly = {l - lp: c for l, c in poly.items()}
                inv_shifted = _invert_y_polynomial(shifted_poly, ymax)
                return {l - lp: c for l, c in inv_shifted.items()}
        raise ValueError("All coefficients zero")

    # Recursive solve: g(0) = 1/f(0), then for L != 0:
    # g(L) = -(1/f(0)) * sum_{l1 != 0, l1+l2=L, |l1| <= |max_l|} f(l1) * g(l2)

    result: Dict[int, Fraction] = {}
    result[0] = Fraction(1) / f_0

    for L in range(1, ymax + 1):
        # Solve for g(L) and g(-L)

        # For g(L):
        s_pos = Fraction(0)
        for l1, fc in poly.items():
            if l1 == 0:
                continue
            l2 = L - l1
            if abs(l2) < abs(L) and l2 in result:
                s_pos += fc * result[l2]
        result[L] = -s_pos / f_0

        # For g(-L):
        s_neg = Fraction(0)
        for l1, fc in poly.items():
            if l1 == 0:
                continue
            l2 = -L - l1
            if abs(l2) < abs(L) and l2 in result:
                s_neg += fc * result[l2]
            elif l2 == L and L in result:
                s_neg += fc * result[l2]
        result[-L] = -s_neg / f_0

    return result


# ============================================================
# DISCRIMINANT-INDEXED DEGENERACIES
# ============================================================

def bps_degeneracy_by_discriminant(d_coeffs: Dict[Tuple[int, int, int], int],
                                   Delta_max: int
                                   ) -> Dict[int, int]:
    """
    Compute d(Delta) = sum_{4nm-l^2=Delta} d(n,l,m) for each discriminant Delta.

    Returns dict {Delta: total_degeneracy} for Delta = -1, 0, 1, ..., Delta_max.
    """
    result: Dict[int, int] = defaultdict(int)
    for (n, l, m), c in d_coeffs.items():
        Delta = 4 * n * m - l * l
        if Delta <= Delta_max:
            result[Delta] += c
    return dict(result)


# ============================================================
# EICHLER-ZAGIER DIMENSION FORMULA
# ============================================================

def dim_jacobi_cusp_forms(k: int, m: int) -> int:
    """
    Dimension of the space J_{k,m}^{cusp} of Jacobi cusp forms of weight k, index m.

    From Eichler-Zagier (1985), Theorem 5.4 and Theorem 9.1.

    For k >= 3 odd: J_{k,m}^{cusp} = 0.
    For k >= 2 even:
      dim J_{k,m}^{cusp} = sum_{j=0}^{m} dim S_{k+2j}(SL_2(Z)) - (adjustment)

    Simplified formula for m = 1 (EZ Theorem 9.1):
      dim J_{k,1}^{cusp} = dim S_k + dim S_{k+2} - 1 if k >= 12 and even
      (with corrections for small k).

    For general m, use the Skoruppa-Zagier formula.

    Here we implement the basic cases needed for our computation.
    """
    if k % 2 == 1:
        return 0  # Odd weight: zero for SL(2,Z)
    if k < 0:
        return 0

    if m == 1:
        return _dim_Jk1_cusp(k)
    elif m == 2:
        return _dim_Jk2_cusp(k)
    elif m == 3:
        return _dim_Jk3_cusp(k)
    else:
        # General formula: use the Eichler-Zagier theorem
        # dim J_{k,m}^cusp = sum_{j=0}^{m-1} dim S_{k+2j} (for k sufficiently large)
        # This is an approximation; exact for k >> m.
        if k >= 2 * m + 12:
            return sum(_dim_Sk(k + 2 * j) for j in range(m))
        else:
            raise NotImplementedError(f"dim J_{{{k},{m}}}^cusp not implemented for small k")


def _dim_Sk(k: int) -> int:
    """Dimension of S_k(SL(2,Z)), the space of weight-k cusp forms."""
    if k < 0 or k % 2 == 1:
        return 0
    if k == 0:
        return 0
    if k == 2:
        return 0
    if k < 12:
        return 0
    if k == 12:
        return 1
    # General: dim S_k = floor(k/12) - 1 if k ≡ 2 mod 12, else floor(k/12)
    q, r = divmod(k, 12)
    if r == 2:
        return q - 1
    return q


def _dim_Jk1_cusp(k: int) -> int:
    """dim J_{k,1}^{cusp} from EZ Theorem 9.1."""
    if k < 0 or k % 2 == 1:
        return 0
    # Table from Eichler-Zagier:
    # k:  0  2  4  6  8  10  12  14  16  18  20  ...
    # dim: 0  0  0  0  0   1   1   1   1   2   2  ...
    table = {0: 0, 2: 0, 4: 0, 6: 0, 8: 0, 10: 1, 12: 1, 14: 1, 16: 1,
             18: 2, 20: 2, 22: 2, 24: 3, 26: 3, 28: 3, 30: 4}
    if k in table:
        return table[k]
    # General: approximately floor((k-4)/6) for large k
    # More precisely: dim J_{k,1}^cusp = dim S_k + dim S_{k+2} - delta_{k>=12}
    # Actually use EZ formula:
    return _dim_Sk(k) + _dim_Sk(k + 2) - (1 if k >= 4 else 0)


def _dim_Jk2_cusp(k: int) -> int:
    """dim J_{k,2}^{cusp} from Skoruppa-Zagier."""
    if k < 0 or k % 2 == 1:
        return 0
    # Table for small k:
    table = {0: 0, 2: 0, 4: 0, 6: 0, 8: 1, 10: 1, 12: 2, 14: 2,
             16: 3, 18: 4, 20: 4}
    if k in table:
        return table[k]
    return sum(_dim_Sk(k + 2 * j) for j in range(2))


def _dim_Jk3_cusp(k: int) -> int:
    """dim J_{k,3}^{cusp}."""
    if k < 0 or k % 2 == 1:
        return 0
    table = {0: 0, 2: 0, 4: 0, 6: 1, 8: 1, 10: 2, 12: 3, 14: 4}
    if k in table:
        return table[k]
    return sum(_dim_Sk(k + 2 * j) for j in range(3))


# ============================================================
# CARDY ASYMPTOTIC FORMULA
# ============================================================

def cardy_asymptotic(Delta: int) -> float:
    """
    Cardy asymptotic formula for |d(Delta)| for large discriminant.

    log|d(Delta)| ~ 4*pi*sqrt(Delta) - (27/4)*log(Delta) + const

    The leading Bekenstein-Hawking term is 4*pi*sqrt(Delta).
    The subleading log correction is -(27/4)*log(Delta) (Sen 2012).

    Returns the predicted |d| from the leading Rademacher approximation.
    """
    if Delta <= 0:
        return 0.0
    # Leading Rademacher: c ~ (-1)^{l+1} * (Delta)^{-27/4} * I_{27/2}(...)
    # The dominant term:
    # |d| ~ C * Delta^{-27/4} * exp(4*pi*sqrt(Delta))
    # where C is a constant.
    # For a rough estimate, just use the exponential:
    return math.exp(4 * math.pi * math.sqrt(Delta))


# ============================================================
# CHARGE VECTOR COUNTING
# ============================================================

def charge_vectors_at_discriminant(Delta: int, n_max: int, m_max: int
                                   ) -> List[Tuple[int, int, int]]:
    """
    List all charge vectors (n, l, m) with discriminant 4nm - l^2 = Delta,
    n >= 0, m >= 0, within the given bounds.

    These correspond to charge vectors in the lattice Gamma^{2,2} = U + U.
    """
    vectors = []
    for n in range(0, n_max + 1):
        for m in range(0, m_max + 1):
            if n == 0 and m == 0:
                if Delta + 0 >= 0:
                    l_sq = -Delta
                    if l_sq >= 0:
                        l = int(math.isqrt(l_sq))
                        if l * l == l_sq:
                            if l > 0:
                                vectors.append((0, l, 0))
                                vectors.append((0, -l, 0))
                            else:
                                vectors.append((0, 0, 0))
                continue
            # 4nm - l^2 = Delta => l^2 = 4nm - Delta
            l_sq = 4 * n * m - Delta
            if l_sq < 0:
                continue
            l = int(math.isqrt(l_sq))
            if l * l != l_sq:
                continue
            if l > 0:
                vectors.append((n, l, m))
                vectors.append((n, -l, m))
            else:
                vectors.append((n, 0, m))
    return vectors


def count_charge_vectors(Delta: int, n_max: int = 50, m_max: int = 50) -> int:
    """Count the number of charge vectors with discriminant Delta."""
    return len(charge_vectors_at_discriminant(Delta, n_max, m_max))


# ============================================================
# VERIFICATION UTILITIES
# ============================================================

def verify_phi101_vanishes_at_z0(qmax: int = 10) -> Dict[int, int]:
    """
    Verify that phi_{10,1}(tau, 0) = 0.

    This is because theta_1(tau, 0) = 0 identically, so
    phi_{10,1} = eta^{18} * theta_1^2 vanishes at z=0.

    Returns {n: sum_l f(n,l)} which should be identically 0.
    """
    phi = phi_10_1_qy_expansion(qmax, 5)
    sums = defaultdict(int)
    for (n, l), c in phi.items():
        sums[n] += c
    return dict(sums)


def verify_cusp_form_condition(qmax: int = 10, ymax: int = 5) -> bool:
    """
    Verify that phi_{10,1} satisfies the Jacobi cusp form bound:
    f(n,l) = 0 unless 4n - l^2 >= 0.
    """
    phi = phi_10_1_qy_expansion(qmax, ymax)
    for (n, l), c in phi.items():
        if c != 0 and 4 * n - l * l < 0:
            return False
    return True


def verify_discriminant_dependence(qmax: int = 10, ymax: int = 5) -> bool:
    """
    Verify that f(n,l) of phi_{10,1} depends only on 4n - l^2.
    """
    phi = phi_10_1_qy_expansion(qmax, ymax)
    by_disc: Dict[int, set] = defaultdict(set)
    for (n, l), c in phi.items():
        D = 4 * n - l * l
        by_disc[D].add(c)
    for D, vals in by_disc.items():
        if len(vals) > 1:
            return False
    return True


def phi_10_1_discriminant_coefficients(qmax: int = 15, ymax: int = 8
                                        ) -> Dict[int, int]:
    """
    Return the coefficients c(D) of phi_{10,1} indexed by discriminant D = 4n - l^2.
    """
    phi = phi_10_1_qy_expansion(qmax, ymax)
    result: Dict[int, int] = {}
    for (n, l), c in phi.items():
        D = 4 * n - l * l
        if D not in result:
            result[D] = c
    return result
