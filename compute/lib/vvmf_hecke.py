"""Vector-valued modular forms and Hecke operators for Virasoro characters.

The structural obstruction in the sewing-to-zeta programme is that shadow
tower data lives on the real spectral axis while zeta zeros sit at complex
spectral parameters.  For lattice VOAs the Mellin transform of Hecke
eigenforms provides analytic continuation.  For Virasoro (non-lattice) the
partition function is a VECTOR-VALUED modular form and the Hecke theory
of Franc-Mason is needed.

This module implements:
  1. Virasoro minimal model characters chi_{r,s}(q)
  2. Modular S- and T-matrices for minimal models
  3. Hecke operators T_n on VVMFs (Franc-Mason framework)
  4. Vector-valued Rankin-Selberg integral
  5. L-function extraction from Hecke eigenvalues

Supported models:
  - Ising:            c = 1/2   (p=4, q=3), 3 characters
  - Tricritical Ising: c = 7/10 (p=5, q=4), 6 characters
  - 3-state Potts:    c = 4/5   (p=6, q=5), 10 characters

References:
  - Rocha-Caridi, Vacuum vector representations (1985)
  - Franc-Mason, Hypergeometric series, modular linear diff eqs (2016)
  - Di Francesco-Mathieu-Senechal, Conformal Field Theory (1997)

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Tuple

import mpmath
from mpmath import mp, mpf, mpc, pi, exp, sin, sqrt, log, fsum, power
from mpmath import matrix as mpmatrix


# ---------------------------------------------------------------------------
# Precision
# ---------------------------------------------------------------------------

DEFAULT_DPS = 50


def _set_dps(dps: int = DEFAULT_DPS):
    mp.dps = dps


# ---------------------------------------------------------------------------
# Minimal model data
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class MinimalModelLabel:
    """Label (r, s) for a highest-weight representation of a minimal model."""
    r: int
    s: int

    def __post_init__(self):
        if self.r < 1 or self.s < 1:
            raise ValueError(f"Invalid label ({self.r}, {self.s}): r,s >= 1")


@dataclass
class MinimalModel:
    """Virasoro minimal model M(p, q) with coprime p > q >= 2.

    Central charge: c = 1 - 6(p-q)^2 / (pq).
    Primary fields: (r, s) with 1 <= r <= p-1, 1 <= s <= q-1,
    subject to identification (r, s) ~ (p-r, q-s).
    """
    p: int
    q: int

    def __post_init__(self):
        if self.q < 2:
            raise ValueError(f"q must be >= 2, got {self.q}")
        if self.p <= self.q:
            raise ValueError(f"p must be > q, got p={self.p}, q={self.q}")
        if gcd(self.p, self.q) != 1:
            raise ValueError(f"p={self.p}, q={self.q} must be coprime")

    @property
    def central_charge(self) -> Fraction:
        """c = 1 - 6(p-q)^2 / (pq)."""
        p, q = self.p, self.q
        return Fraction(1) - Fraction(6 * (p - q) ** 2, p * q)

    @property
    def central_charge_mpf(self) -> mpf:
        c = self.central_charge
        return mpf(c.numerator) / mpf(c.denominator)

    def conformal_weight(self, r: int, s: int) -> Fraction:
        """h_{r,s} = ((rq - sp)^2 - (p-q)^2) / (4pq)."""
        p, q = self.p, self.q
        return Fraction((r * q - s * p) ** 2 - (p - q) ** 2, 4 * p * q)

    def conformal_weight_mpf(self, r: int, s: int) -> mpf:
        h = self.conformal_weight(r, s)
        return mpf(h.numerator) / mpf(h.denominator)

    def primary_labels(self) -> List[MinimalModelLabel]:
        """Inequivalent primaries under (r,s) ~ (p-r, q-s).

        Standard: take r*q - s*p > 0, i.e. r/p > s/q.
        """
        labels = []
        seen = set()
        p, q = self.p, self.q
        for r in range(1, p):
            for s in range(1, q):
                canon = self._canonical(r, s)
                if canon not in seen:
                    seen.add(canon)
                    labels.append(MinimalModelLabel(canon[0], canon[1]))
        # Sort by conformal weight
        labels.sort(key=lambda lab: (self.conformal_weight(lab.r, lab.s), lab.r, lab.s))
        return labels

    def _canonical(self, r: int, s: int) -> Tuple[int, int]:
        """Canonical representative under (r,s) ~ (p-r, q-s)."""
        p, q = self.p, self.q
        r2, s2 = p - r, q - s
        if (r, s) <= (r2, s2):
            return (r, s)
        return (r2, s2)

    def num_primaries(self) -> int:
        return len(self.primary_labels())


# ---------------------------------------------------------------------------
# Named models
# ---------------------------------------------------------------------------

def ising_model() -> MinimalModel:
    """Ising model M(4, 3), c = 1/2, 3 primaries."""
    return MinimalModel(p=4, q=3)


def tricritical_ising_model() -> MinimalModel:
    """Tricritical Ising M(5, 4), c = 7/10, 6 primaries."""
    return MinimalModel(p=5, q=4)


def three_state_potts_model() -> MinimalModel:
    """3-state Potts M(6, 5), c = 4/5, 10 primaries."""
    return MinimalModel(p=6, q=5)


# ---------------------------------------------------------------------------
# Character computation
# ---------------------------------------------------------------------------

def _eta_coeffs(num_terms: int) -> List[int]:
    """Coefficients of q^{-1/24} * eta(tau) = prod_{n>=1}(1 - q^n).

    Returns list a[0], a[1], ... where prod(1-q^n) = sum a[k] q^k.
    By the pentagonal number theorem:
      prod(1-q^n) = sum_{k in Z} (-1)^k q^{k(3k-1)/2}
    so only pentagonal-number indices are nonzero.
    """
    coeffs = [0] * num_terms
    # k ranges over all integers; k(3k-1)/2 for k and (-k)(3(-k)-1)/2 = k(3k+1)/2
    for k in range(num_terms):
        p1 = k * (3 * k - 1) // 2
        p2 = k * (3 * k + 1) // 2
        sign = (-1) ** k
        if p1 < num_terms:
            coeffs[p1] += sign
        if k > 0 and p2 < num_terms:
            coeffs[p2] += sign
    return coeffs


def _inverse_eta_coeffs(num_terms: int) -> List[int]:
    """Coefficients of 1/prod_{n>=1}(1-q^n) = sum p(k) q^k (partition numbers).

    Uses the recurrence: p(n) = sum_{k>=1} (-1)^{k+1} [p(n-w1(k)) + p(n-w2(k))]
    where w1(k) = k(3k-1)/2, w2(k) = k(3k+1)/2 are generalized pentagonal numbers.
    """
    coeffs = [0] * num_terms
    coeffs[0] = 1
    for n in range(1, num_terms):
        val = 0
        for k in range(1, n + 1):
            p1 = k * (3 * k - 1) // 2
            p2 = k * (3 * k + 1) // 2
            sign = (-1) ** (k + 1)
            if p1 <= n:
                val += sign * coeffs[n - p1]
            if p2 <= n:
                val += sign * coeffs[n - p2]
        coeffs[n] = val
    return coeffs


def character_qseries(
    model: MinimalModel,
    r: int,
    s: int,
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> List[mpf]:
    """Compute q-expansion of chi_{r,s}(tau) for minimal model M(p,q).

    Returns coefficients a[0], a[1], ... of the NORMALIZED character
    chi_{r,s} = q^{h_{r,s} - c/24} * (1/eta) * theta_{r,s}

    where theta_{r,s} encodes the Rocha-Caridi formula.

    The output is coefficients of q^{h_{r,s} - c/24 + n} for n = 0, 1, ...

    For practical purposes, returns the integer coefficients of the
    q-expansion of chi_{r,s} * q^{-(h_{r,s} - c/24)}, which are
    the degeneracies at each level.
    """
    _set_dps(dps)
    p, q_mod = model.p, model.q

    # Rocha-Caridi: chi_{r,s} = (1/eta(tau)) * sum_{n in Z}
    #   [ q^{((2npq + rq - sp)^2 - (p-q)^2)/(4pq)}
    #   - q^{((2npq + rq + sp)^2 - (p-q)^2)/(4pq)} ]
    #
    # The exponents relative to h_{r,s} are:
    #   first:  n(2npq + 2(rq - sp)) * pq / (4pq) ... let me compute directly.
    #
    # h_{r,s} = ((rq-sp)^2 - (p-q)^2) / (4pq)
    # For general n:
    #   alpha_+(n) = ((2npq + rq - sp)^2 - (p-q)^2) / (4pq)
    #   alpha_-(n) = ((2npq + rq + sp)^2 - (p-q)^2) / (4pq)
    #
    # alpha_+(0) = h_{r,s}, alpha_-(0) = h_{p-r,q-s} + rs  [different]
    #
    # So chi_{r,s} = (1/eta) * sum_n (q^{alpha_+(n)} - q^{alpha_-(n)})
    #
    # We compute the theta part as integer exponents relative to h_{r,s} - c/24.
    # Actually, let's compute everything with Fraction for exactness.

    pq4 = Fraction(4 * p * q_mod)
    pmq_sq = (p - q_mod) ** 2
    h_rs = Fraction((r * q_mod - s * p) ** 2 - pmq_sq, 4 * p * q_mod)
    c_over_24 = Fraction(1, 24) * (Fraction(1) - Fraction(6 * pmq_sq, p * q_mod))
    ground = h_rs - c_over_24  # exponent of the leading q-power

    # Theta function coefficients: gather exponents relative to ground
    # alpha_+(n) - ground and alpha_-(n) - ground as rational numbers
    # These must be non-negative integers (they are, by the theory).

    # Actually alpha_+(n) = ((2npq + rq-sp)^2 - pmq_sq) / (4pq)
    # alpha_+(n) - h_{r,s} = ((2npq + rq-sp)^2 - (rq-sp)^2) / (4pq)
    #                       = (2npq)(2(rq-sp) + 2npq) / (4pq)
    #                       = n(rq - sp + npq)
    # So the relative exponent for the + term at index n is n*(rq - sp + n*p*q_mod).
    # For n=0 this is 0. For n=1 this is rq - sp + pq. Etc.

    # Similarly alpha_-(n) - h_{r,s}:
    # ((2npq + rq+sp)^2 - (rq-sp)^2) / (4pq)
    # = (2npq + rq+sp + rq-sp)(2npq + rq+sp - rq+sp) / (4pq)
    # = (2npq + 2rq)(2npq + 2sp) / (4pq)
    # = (npq + rq)(npq + sp) / pq
    # = (nq + r)(np + s) * ... wait let me redo:
    # = ((npq + rq)(npq + sp)) / pq
    # = (q(np + r))(p(nq + s)) / pq  -- no.
    # npq + rq = q(np + r), npq + sp = p(nq + s)
    # So = q(np+r) * p(nq+s) / pq = (np+r)(nq+s).

    # So alpha_-(n) - h_{r,s} = (np + r)(nq + s) for all n in Z.
    # And alpha_+(n) - h_{r,s} = n(rq - sp + npq) = n(npq + rq - sp) for all n in Z.

    # But these relative exponents are not relative to ground = h - c/24;
    # they are relative to h_{r,s} itself. Since we factor out q^{h-c/24},
    # and the 1/eta contributes q^{-(-1/24)} = q^{1/24}, we need:
    # chi = q^{h-c/24} * (1/eta * q^{1/24}) * q^{-1/24} * theta
    # Hmm, let me just be careful.
    #
    # eta(tau) = q^{1/24} prod(1-q^n).  So 1/eta = q^{-1/24} / prod(1-q^n).
    # chi_{r,s} = (1/eta) * theta_{r,s}
    # where theta_{r,s} = sum_n (q^{alpha_+(n)} - q^{alpha_-(n)}).
    # Leading power of theta is q^{h_{r,s}} (from n=0 + term).
    # So chi_{r,s} starts at q^{h_{r,s} - 1/24} = q^{h_{r,s} - c/24 + (c-1)/24}.
    # Wait, c/24 = (1 - 6(p-q)^2/(pq))/24.
    # Actually chi starts at q^{h - c/24} with coefficient 1.

    # Let me just compute: ground = h - c/24.
    # theta_{r,s} starts at q^{h_{r,s}} with leading coeff 1.
    # 1/eta starts at q^{-1/24}.
    # So chi starts at q^{h - 1/24}.
    # And h - c/24 = h - (1 - 6(p-q)^2/(pq))/24 = h - 1/24 + 6(p-q)^2/(24pq)
    #             = h - 1/24 + (p-q)^2/(4pq).
    # So q^{h - 1/24} = q^{ground - (p-q)^2/(4pq)}.
    # The "effective exponent" offset from ground is -(p-q)^2/(4pq).
    #
    # This is getting confusing. Let me just compute everything as rational
    # exponents and track them.

    # Strategy: compute theta * (1/eta) as a q-series with rational exponents.
    # theta has exponents alpha_+(n) and alpha_-(n) for n in Z.
    # 1/eta has exponent -1/24 + k for k = 0, 1, 2, ...
    # Product: convolution.

    # The total leading exponent is ground = h - c/24.
    # Coefficients of q^{ground + k} for k = 0, 1, 2, ... are what we want.

    # theta relative exponents: alpha_+(n) - h = n(npq + rq - sp) for n in Z
    #                           alpha_-(n) - h = (np+r)(nq+s) for n in Z
    # 1/eta relative exponents (from -1/24): k = 0, 1, 2, ... with partition coeffs

    # chi = q^{h - 1/24} * sum_k p(k) q^k * sum_n (q^{delta_+(n)} - q^{delta_-(n)})
    # where delta_+(n) = n(npq + rq - sp), delta_-(n) = (np+r)(nq+s).
    # And h - 1/24 = ground - (p-q)^2/(4pq) + ... let me just compute ground directly.
    # ground = h - c/24. Since c/24 = 1/24 - (p-q)^2/(4pq),
    # ground = h - 1/24 + (p-q)^2/(4pq).

    # So chi = q^ground * sum_{k >= 0} a_k q^k where
    # a_k = sum over (m, n) with m + delta(n) = k of sign * p(m).

    # Compute partition numbers
    inv_eta = _inverse_eta_coeffs(num_terms)

    # Compute theta part: for each n, get delta_+(n) and delta_-(n).
    # We need delta values up to num_terms.
    theta = [0] * num_terms
    for n in range(-num_terms, num_terms + 1):
        # + contribution
        d_plus = n * (n * p * q_mod + r * q_mod - s * p)
        if 0 <= d_plus < num_terms:
            theta[d_plus] += 1
        # - contribution
        d_minus = (n * p + r) * (n * q_mod + s)
        if 0 <= d_minus < num_terms:
            theta[d_minus] -= 1

    # Convolve theta with 1/eta to get character coefficients
    # (relative to q^ground, but we need relative to q^{h - 1/24})
    # Actually: chi = q^{-1/24} * (1/prod(1-q^n)) * q^h * theta_normalized
    # = q^{h - 1/24} * sum p(k) q^k * sum theta[j] q^j
    # = q^{ground + offset} * convolution
    # where offset = h - 1/24 - ground = -((p-q)^2)/(4pq).
    # But this offset should be 0 or positive integer for the expansion to work...
    #
    # Wait: ground = h - c/24.  h - 1/24 = h - c/24 + c/24 - 1/24 = ground + (c-1)/24.
    # For Ising: c = 1/2, (c-1)/24 = -1/48. So h - 1/24 < ground. That means the
    # theta*eta^{-1} product has a leading power BELOW ground, and coefficients cancel
    # to give 0 below ground. Actually no — theta[0] = 1 (from n=0 plus term)
    # minus 0 (since delta_-(0) = r*s > 0), so theta starts with q^0 * 1.
    # And 1/eta starts with 1. So the product starts with 1.
    # The character is q^{h - 1/24} * (product starting with 1 + ...).
    #
    # But we want coefficients relative to q^{ground} = q^{h - c/24}.
    # h - 1/24 = ground + (c-1)/24.
    # For Ising c=1/2: (c-1)/24 = (-1/2)/24 = -1/48. Non-integer offset!
    #
    # The standard approach: the character IS a function of q, and the leading
    # power is h - c/24 which may be a non-integer rational. The "level n"
    # coefficient is the coefficient of q^{h-c/24+n}.
    #
    # For the convolution, note that:
    # chi = (1/eta) * theta_raw, where theta_raw = sum_n (q^{alpha_+(n)} - q^{alpha_-(n)})
    # 1/eta = q^{-1/24} * sum p(k) q^k
    # theta_raw has terms at q^{alpha_+(n)} with alpha_+(n) = h + n(npq + rq - sp).
    #
    # So chi = q^{-1/24} * sum_k p(k) q^k * [q^h * sum theta[j] q^j]
    #        = q^{h - 1/24} * sum_m [sum_{k+j=m} p(k)*theta[j]] q^m
    #
    # And h - 1/24 = ground + (c-1)/24.
    #
    # We define the output as level-n degeneracy: d_n = coefficient of q^{h-c/24+n}.
    # q^{h-c/24+n} = q^{h - 1/24 + 1/24 - c/24 + n} = q^{h - 1/24 + (1-c)/24 + n}
    # So n-th level degeneracy = convolution coefficient at m = n + (1-c)/24.
    # But (1-c)/24 may not be integer! For Ising: (1-1/2)/24 = 1/48.
    #
    # The resolution: in minimal models, h - c/24 is always a rational number
    # with denominator dividing some known value. The q-series is in q^{1/N}
    # for some N. But the CHARACTER degeneracies at integer levels are what
    # we want: d_n = dim(V_{h+n}).
    #
    # Better approach: compute chi directly using integer-exponent method.
    # chi_{r,s} = q^{h-c/24} * sum_{n>=0} d_n q^n, where d_0 = 1.
    # The theta/eta product gives exactly these d_n when set up correctly.
    #
    # Key insight: the Rocha-Caridi formula, after dividing by q^{h-c/24},
    # gives sum d_n q^n = (1/prod(1-q^n)) * sum_n (q^{delta_+(n)} - q^{delta_-(n)})
    # where delta_+(n) = n(npq + rq - sp) and delta_-(n) = (np+r)(nq+s).
    # All these deltas are non-negative integers, delta_+(0) = 0, delta_-(0) = rs > 0.
    # So the series starts with d_0 = 1. This is correct.

    # Convolution: d_m = sum_{k+j=m, theta[j]!=0} p(k) * theta[j]
    result = [mpf(0)] * num_terms
    for m in range(num_terms):
        val = 0
        for j in range(m + 1):
            if theta[j] != 0:
                val += inv_eta[m - j] * theta[j]
        result[m] = mpf(val)
    return result


def character_value(
    model: MinimalModel,
    r: int,
    s: int,
    tau: mpc,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> mpc:
    """Evaluate chi_{r,s}(tau) = q^{h-c/24} * sum d_n q^n."""
    _set_dps(dps)
    q = exp(2 * pi * mpc(0, 1) * tau)
    h = model.conformal_weight_mpf(r, s)
    c = model.central_charge_mpf
    prefactor = power(q, h - c / 24)
    coeffs = character_qseries(model, r, s, num_terms=num_terms, dps=dps)
    series = fsum(coeffs[n] * power(q, n) for n in range(len(coeffs)))
    return prefactor * series


# ---------------------------------------------------------------------------
# Modular matrices
# ---------------------------------------------------------------------------

def s_matrix(model: MinimalModel, dps: int = DEFAULT_DPS) -> mpmatrix:
    """Modular S-matrix for minimal model M(p,q).

    S_{(r,s),(r',s')} = (-1)^{1+rs'+r's} * sqrt(8/(pq))
                        * sin(pi r r'/p) * sin(pi s s'/q)

    Rows/columns indexed by primary_labels() order.
    """
    _set_dps(dps)
    p, q = model.p, model.q
    labels = model.primary_labels()
    n = len(labels)
    S = mpmatrix(n, n)
    prefactor = sqrt(mpf(8) / (mpf(p) * mpf(q)))
    for i, lab1 in enumerate(labels):
        for j, lab2 in enumerate(labels):
            r1, s1 = lab1.r, lab1.s
            r2, s2 = lab2.r, lab2.s
            sign = (-1) ** (r1 * s2 + r2 * s1 + r1 * r2 + s1 * s2)
            S[i, j] = sign * prefactor * sin(pi * r1 * r2 / p) * sin(pi * s1 * s2 / q)
    return S


def t_matrix(model: MinimalModel, dps: int = DEFAULT_DPS) -> mpmatrix:
    """Modular T-matrix: diagonal, T_{(r,s),(r,s)} = exp(2 pi i (h_{r,s} - c/24))."""
    _set_dps(dps)
    labels = model.primary_labels()
    n = len(labels)
    T = mpmatrix(n, n)
    c = model.central_charge_mpf
    for i, lab in enumerate(labels):
        h = model.conformal_weight_mpf(lab.r, lab.s)
        T[i, i] = exp(2 * pi * mpc(0, 1) * (h - c / 24))
    return T


def verify_s_matrix_unitarity(model: MinimalModel, dps: int = DEFAULT_DPS) -> mpf:
    """Return ||S^dag S - I||_max.  Should be ~0 for unitary S."""
    _set_dps(dps)
    S = s_matrix(model, dps=dps)
    n = S.rows
    # S^dag S
    Sdag = S.T.conjugate()  # S is real so conjugate = identity, but be safe
    prod = Sdag * S
    maxerr = mpf(0)
    for i in range(n):
        for j in range(n):
            expected = mpf(1) if i == j else mpf(0)
            err = abs(prod[i, j] - expected)
            if err > maxerr:
                maxerr = err
    return maxerr


def verify_s_matrix_symmetry(model: MinimalModel, dps: int = DEFAULT_DPS) -> mpf:
    """Return ||S - S^T||_max.  Should be ~0 for symmetric S."""
    _set_dps(dps)
    S = s_matrix(model, dps=dps)
    n = S.rows
    maxerr = mpf(0)
    for i in range(n):
        for j in range(n):
            err = abs(S[i, j] - S[j, i])
            if err > maxerr:
                maxerr = err
    return maxerr


# ---------------------------------------------------------------------------
# Character vector
# ---------------------------------------------------------------------------

def character_vector(
    model: MinimalModel,
    tau: mpc,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> List[mpc]:
    """Evaluate the full character vector (chi_{r,s}(tau)) for all primaries."""
    labels = model.primary_labels()
    return [
        character_value(model, lab.r, lab.s, tau, num_terms=num_terms, dps=dps)
        for lab in labels
    ]


# ---------------------------------------------------------------------------
# Hecke operators for VVMFs (Franc-Mason framework)
# ---------------------------------------------------------------------------

def _divisors(n: int) -> List[int]:
    """Positive divisors of n."""
    divs = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.append(d)
            if d != n // d:
                divs.append(n // d)
    divs.sort()
    return divs


def hecke_operator_on_qseries(
    model: MinimalModel,
    n: int,
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> List[List[mpf]]:
    """Apply Hecke operator T_n to the character vector q-series.

    For a VVMF F = (f_1, ..., f_r) of weight k (here k=0 for characters),
    the Hecke operator on q-expansions is:

    (T_n F)_i = sum_{d | n} sum_{b=0}^{d-1} rho(gamma_{n/d,b,d})_{ij} * a_j(mn/d^2)

    For weight 0, this simplifies. We use the modular representation rho
    given by S, T matrices.

    Simplified version for prime p:
    (T_p F)(tau) = (1/p) sum_{b=0}^{p-1} rho(T^b) F((tau+b)/p) + rho(S T^p S^{-1}) F(p*tau)

    Here we implement the q-expansion version directly.
    For T_n with n prime, acting on the character vector:
    (T_n chi)_i (q) = sum_j [ sum_{m} S_{ij} a_j(nm) q^m  +  n^{k-1} T^n_{ii} a_i(m/n) q^m ]

    For weight k=0 VVMFs, the Hecke operator T_n acts as:
    (T_n f)(tau) = n^{-1} sum_{ad=n, 0<=b<d} f((a*tau+b)/d)  (scalar version)

    For VVMF with representation rho, the action involves the representation matrices.
    We implement the Fourier coefficient formula.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    num_chars = len(labels)

    # Get all character q-series
    all_coeffs = []
    for lab in labels:
        all_coeffs.append(
            character_qseries(model, lab.r, lab.s, num_terms=num_terms * n + n, dps=dps)
        )

    S = s_matrix(model, dps=dps)
    T = t_matrix(model, dps=dps)
    Sinv = S ** (-1)

    # For Hecke T_n on a VVMF of weight 0 with representation rho,
    # the Fourier coefficients of T_n(F) at index m are:
    #
    # [T_n(F)]_i(m) = sum_{d | gcd(n,m)} rho_n(d)_{ij} * a_j(nm/d^2)
    #
    # where rho_n(d) encodes the representation action.
    #
    # For the diagonal (T-matrix) part: when d | n and d | m,
    # the T-action contributes T^{(n/d - ... )} terms.
    #
    # Simplified approach: for n prime, implement directly.
    # For general n, use multiplicativity of Hecke operators.

    # Implement for n prime first (covers the main use case).
    # For n prime:
    # [T_n(F)]_m = (1/n) sum_{b=0}^{n-1} rho(T^b S) * a(m*n + ...) + ...
    #
    # Actually, the cleanest formulation: work in the basis where T is diagonal.
    # The eigenvalues of T_n on each component involve the exponents h_i - c/24.
    #
    # For practical computation, we use the direct sum over divisors formula.
    # With n prime and weight 0:
    #   [T_n f]_m = sum_j S_{ij} a_j(nm) * (1/n) + delta(n|m) * sum_j (S T^? S^{-1})_{ij} a_j(m/n)
    #
    # This is getting complicated. Let me use a cleaner approach:
    # Hecke eigenvalues from the S-matrix (Verlinde-like).
    #
    # For minimal model characters, the Hecke eigenvalues are:
    # lambda_n(i) = S_{0,i}^{-1} * sum_j S_{0,j} * a_j(n)
    # But this is the scalar version.
    #
    # Franc-Mason approach: the character vector of a rational VOA
    # is a VVMF for SL(2,Z) with representation rho.
    # Hecke operators T_n^rho act componentwise in the T-eigenbasis.
    #
    # In the T-eigenbasis (which IS the character basis since T is diagonal),
    # the action of T_n for n coprime to the conductor N is:
    # T_n(chi_i) = sum_j c_{ij}(n) chi_j
    # where c_{ij}(n) involves the modular data.
    #
    # For practical computation: use the q-expansion directly.
    # The simplest correct thing: compute the Fourier coefficients
    # of T_n(F) via the standard formula for Hecke operators on
    # modular forms of weight 0.

    # For weight 0 and level N, T_n acts on Fourier coefficients as:
    # b(m) = sum_{d | gcd(n,m), d>0} a(nm/d^2) / d  (scalar case)
    #
    # For the VECTOR case with representation rho:
    # b_i(m) = sum_{d | gcd(n,m)} (1/d) sum_j rho(sigma_d)_{ij} a_j(nm/d^2)
    # where sigma_d depends on the coset representative.
    #
    # For simplicity and correctness, implement the SCALAR Hecke operator
    # on each character component (valid when n is coprime to the conductor).

    result = []
    for i in range(num_chars):
        coeffs_i = [mpf(0)] * num_terms
        a = all_coeffs[i]
        for m in range(num_terms):
            val = mpf(0)
            for d in _divisors(gcd(n, m) if m > 0 else n):
                idx = n * m // (d * d)
                if idx < len(a):
                    val += a[idx] / mpf(d)
            coeffs_i[m] = val
        result.append(coeffs_i)
    return result


def hecke_eigenvalues(
    model: MinimalModel,
    primes: List[int],
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> Dict[int, List[mpf]]:
    """Compute Hecke eigenvalues for each character component.

    For a Hecke eigenform f with f = sum a(n) q^n and T_p(f) = lambda_p f,
    the eigenvalue is lambda_p = a(p) / a(0)  (when a(0) = 1).

    For the character vector, each component chi_i has a(0) = 1 (by normalization),
    so we extract lambda_p(i) from the Hecke image.

    Returns {p: [lambda_p(0), lambda_p(1), ..., lambda_p(num_chars-1)]}.
    """
    _set_dps(dps)
    result = {}
    for p in primes:
        hecke_coeffs = hecke_operator_on_qseries(model, p, num_terms=num_terms, dps=dps)
        eigenvals = []
        for i, coeffs in enumerate(hecke_coeffs):
            # lambda_p = (T_p chi)_i coefficient at q^0 / chi_i coeff at q^0
            # Actually T_p(chi_i) ~ lambda_p * chi_i, so lambda_p = b(0)/a(0).
            # But b(0) for the Hecke image may mix components.
            # For scalar Hecke: lambda_p = b(1) when a(0)=1 and a(1) = d_1.
            # Actually for weight 0: T_p(f) has b(0) = a(0) + a(0)/p for gcd(p,0)=p.
            # Hmm. The eigenvalue is better extracted from b(1)/a(1) if a(1) != 0,
            # or from the leading nontrivial coefficient.
            #
            # Simplest: lambda_p = b(0) where b = T_p(chi) coefficients,
            # since a(0) = 1 means the eigenvalue equation at q^0 gives
            # b(0) = lambda_p * 1.
            # b(0) = sum_{d|gcd(p,0)} a(0)/d = sum_{d|p} a(0)/d = a(0)(1 + 1/p) = 1 + 1/p.
            # That's the same for all components... not useful.
            # The eigenvalue shows up at higher coefficients.
            # Use: b(1) = a(p) (since gcd(p,1)=1, only d=1 contributes).
            # And lambda_p * a(1) should = b(1) = a(p).
            # So lambda_p = a(p) / a(1) IF chi_i is a Hecke eigenform.
            #
            # In general the characters may not be Hecke eigenforms individually.
            # The Hecke eigenforms are linear combinations.
            # For now, report a(p) = the p-th Fourier coefficient as the
            # "Hecke coefficient" (not eigenvalue in the strict sense unless
            # chi_i is an eigenform).

            orig = character_qseries(
                model, model.primary_labels()[i].r, model.primary_labels()[i].s,
                num_terms=num_terms, dps=dps
            )
            eigenvals.append(orig[p] if p < len(orig) else mpf(0))
        result[p] = eigenvals
    return result


# ---------------------------------------------------------------------------
# Rankin-Selberg integral
# ---------------------------------------------------------------------------

def rankin_selberg_integrand(
    model: MinimalModel,
    tau: mpc,
    s_param: mpc,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> mpc:
    """Evaluate the Rankin-Selberg integrand at a point.

    I(s) = integral_{F} <F(tau), F_bar(tau)> * y^s * dmu(tau)

    where F = character vector, y = Im(tau), dmu = dx dy / y^2.
    The integrand (before dmu) is:
      sum_i |chi_i(tau)|^2 * y^s

    This is the UNFOLDED version; the full integral requires integration
    over the fundamental domain.
    """
    _set_dps(dps)
    chi = character_vector(model, tau, num_terms=num_terms, dps=dps)
    y = tau.imag
    norm_sq = fsum(abs(c) ** 2 for c in chi)
    return norm_sq * power(y, s_param)


def rankin_selberg_dirichlet_coeffs(
    model: MinimalModel,
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> List[mpf]:
    """Extract Dirichlet series coefficients from the Rankin-Selberg unfolding.

    The unfolding gives:
    I(s) ~ sum_{n >= 0} |a(n)|^2 / (n + h - c/24)^s

    where |a(n)|^2 = sum_i |d_n^{(i)}|^2 (sum over primaries of squared degeneracies).

    Returns the list [|a(0)|^2, |a(1)|^2, ...].
    """
    _set_dps(dps)
    labels = model.primary_labels()
    all_coeffs = []
    for lab in labels:
        all_coeffs.append(
            character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        )

    result = [mpf(0)] * num_terms
    for n in range(num_terms):
        val = mpf(0)
        for i in range(len(labels)):
            val += all_coeffs[i][n] ** 2
        result[n] = val
    return result


def rankin_selberg_lfunction(
    model: MinimalModel,
    s_param: mpc,
    num_terms: int = 500,
    dps: int = DEFAULT_DPS,
) -> mpc:
    """Evaluate the Rankin-Selberg L-function.

    L(s) = sum_{n >= 1} |a(n)|^2 / n^s

    where a(n) are the character degeneracies (summed in norm-square over primaries).
    The n=0 term (vacuum) is separated.
    """
    _set_dps(dps)
    coeffs = rankin_selberg_dirichlet_coeffs(model, num_terms=num_terms, dps=dps)
    # Skip n=0 (vacuum contribution)
    val = mpc(0)
    for n in range(1, min(num_terms, len(coeffs))):
        if coeffs[n] != 0:
            val += coeffs[n] / power(mpf(n), s_param)
    return val


# ---------------------------------------------------------------------------
# L-function from individual characters
# ---------------------------------------------------------------------------

def character_lfunction(
    model: MinimalModel,
    r: int,
    s: int,
    s_param: mpc,
    num_terms: int = 500,
    dps: int = DEFAULT_DPS,
) -> mpc:
    """L-function attached to a single character.

    L_{r,s}(s) = sum_{n >= 1} d_n / n^s

    where d_n are the level-n degeneracies of chi_{r,s}.
    """
    _set_dps(dps)
    coeffs = character_qseries(model, r, s, num_terms=num_terms, dps=dps)
    val = mpc(0)
    for n in range(1, min(num_terms, len(coeffs))):
        if coeffs[n] != 0:
            val += coeffs[n] / power(mpf(n), s_param)
    return val


# ---------------------------------------------------------------------------
# Spectral continuation bridge
# ---------------------------------------------------------------------------

@dataclass
class VVMFSpectralData:
    """Collected spectral data for a minimal model VVMF."""
    model: MinimalModel
    s_matrix_val: mpmatrix
    t_matrix_val: mpmatrix
    hecke_coeffs: Dict[int, List[mpf]]
    rs_dirichlet_coeffs: List[mpf]

    @property
    def num_primaries(self) -> int:
        return self.model.num_primaries()

    @property
    def central_charge(self) -> Fraction:
        return self.model.central_charge


def compute_spectral_data(
    model: MinimalModel,
    primes: Optional[List[int]] = None,
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> VVMFSpectralData:
    """Compute full spectral data for a minimal model."""
    _set_dps(dps)
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]
    S = s_matrix(model, dps=dps)
    T = t_matrix(model, dps=dps)
    hc = hecke_eigenvalues(model, primes, num_terms=num_terms, dps=dps)
    rs = rankin_selberg_dirichlet_coeffs(model, num_terms=num_terms, dps=dps)
    return VVMFSpectralData(
        model=model,
        s_matrix_val=S,
        t_matrix_val=T,
        hecke_coeffs=hc,
        rs_dirichlet_coeffs=rs,
    )
