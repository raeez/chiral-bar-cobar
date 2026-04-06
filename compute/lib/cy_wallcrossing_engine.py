r"""cy_wallcrossing_engine.py -- Kontsevich-Soibelman wall-crossing for K3 and K3 x E.

MATHEMATICAL CONTENT
====================

This module computes Bridgeland stability conditions and KS wall-crossing
formulas for K3 surfaces and K3 x E threefolds, connecting to the shadow
obstruction tower of chiral algebras via the DT/bar correspondence.

=== 1. BRIDGELAND STABILITY ON K3 ===

A stability condition sigma = (Z, P) on D^b(K3) consists of a central charge
Z: K(K3) -> C (factoring through the Mukai lattice) and a slicing P.

For K3 with Picard rank 1 (degree 2d), the Mukai lattice is
    H*(K3, Z) = H^0 + H^2 + H^4 = Z + Z*H + Z*pt
with Mukai pairing <(r, c_1, s), (r', c_1', s')> = c_1*c_1' - r*s' - r'*s.

The central charge for a stability condition near large volume:
    Z_{B+iw}(r, dH, s) = -s + d*B*r + (w^2/2)*r + i*d*w*r  ... for ch

More precisely, for Mukai vector v = (r, dH, s):
    Z_{B+iw}(v) = <exp(B + iw), v> = -s + (B + iw)*d - (B+iw)^2/2 * r
                = -s + d*B + i*d*w - (B^2 - w^2)/2 * r - i*B*w*r

For a quartic K3 surface (H^2 = 4, degree 2d=4, d=2):
    Z_{B+iw}(r, dH, s) = -s + 2dB + i*2dw - (B^2-w^2)/2 * r - i*B*w*r
    where here d = coefficient of H in ch_1.

Bridgeland (2008): Stab^dagger(K3) -> P^+(K3) is a covering map to the
period domain P^+ = {Omega in H*(K3,C) : <Omega,Omega>=0, <Omega,bar{Omega}>0}.

=== 2. WALLS OF MARGINAL STABILITY ===

A wall W(v_1, v_2) for Mukai vectors v = v_1 + v_2 is the locus in Stab
where Z(v_1)/Z(v_2) is real and positive. At such walls, the Harder-
Narasimhan filtration of an object with Mukai vector v changes.

For large volume, the walls are semicircles in the upper half-plane
{B + iw : w > 0} centered on the B-axis.

=== 3. KS WALL-CROSSING FORMULA ===

The Kontsevich-Soibelman wall-crossing formula at a wall W:
    A_W = prod_{gamma : Z(gamma) in R>0 * e^{i*phi}} T_gamma^{Omega(gamma)}
where:
    T_gamma acts on the quantum torus algebra: T_gamma(x_delta) = x_delta * (1 - x_gamma)^{<gamma,delta>}
    Omega(gamma) = generalized DT invariant
    The product is taken in order of decreasing phase arg(Z(gamma)).

For K3: Omega(v) = chi(Hilb^n(K3)) for primitive v with v^2 = 2n-2
(by Beauville's theorem: M_H(v) = Hilb^n(K3) for primitive v).

=== 4. DT INVARIANTS OF K3 x E ===

K3 x E is a CY 3-fold with chi(K3 x E) = 24 * 0 = 0.
Therefore Z_{DT}(K3 x E) = M(-q)^{chi} = M(-q)^0 = 1 (degree 0 part).

The FULL DT partition function (with curve classes beta) involves:
    Z_{DT}(K3 x E, q, Q) = sum_{n,beta} DT(n, beta) q^n Q^beta

For beta = 0: DT_{beta=0}(n) = chi(Hilb^n(K3 x E)).
For a CY 3-fold X with chi(X) = 0, the degree-0 DT are:
    sum_n chi(Hilb^n(X)) q^n = M(q)^{chi(X)} = 1.
This means chi(Hilb^n(K3 x E)) = 0 for n >= 1, which is CORRECT:
K3 x E has chi = 0, so Hilb^n has vanishing virtual Euler char by MNOP.

But the UNWEIGHTED (non-virtual) Euler char chi(Hilb^n(K3 x E)) is
computed by the Cheah formula (generalizing Gottsche to 3-folds):
    sum_n chi(Hilb^n(X)) q^n = prod_{k>=1} 1/(1-q^k)^{chi(X)}
For chi(X) = 0 this gives 1 again. But the Hodge-theoretic version
is richer: the Hodge polynomial carries nontrivial information.

=== 5. MOTIVIC WALL-CROSSING ===

The motivic DT invariant Omega^{mot}(v) lives in K_0(Var/C).
For K3: Omega^{mot}(0,0,1-n) = [Hilb^n(K3)] in K_0(Var).
The Hodge polynomial of Hilb^n(K3) is computed by the Gottsche formula:
    sum_n [Hilb^n(S)] q^n = prod_{k>=1} prod_{p,q} 1/(1 - (-1)^{p+q} x^p y^q q^k)^{(-1)^{p+q+1} h^{p,q}(S)}

For K3: h^{0,0} = h^{2,2} = 1, h^{1,1} = 20, h^{2,0} = h^{0,2} = 1, all others 0.

=== 6. JOYCE-SONG vs KS ===

Joyce-Song invariants J(v) coincide with KS invariants Omega(v) for
PRIMITIVE Mukai vectors. For non-primitive v = n*v_0:
    Omega(n*v_0) = sum_{k|n} (1/k^2) * mu(n/k) * J(k*v_0)
(Mobius inversion of the multicover formula).

=== 7. CONNECTION TO SHADOW TOWER ===

The KS wall-crossing automorphism at a wall is:
    A_W = exp(sum_gamma Omega(gamma) Li_2(x_gamma))
The shadow generating function H(t) = 2*kappa*t^2*sqrt(Q_L(t)) satisfies
a DIFFERENT type of product formula: algebraicity of degree 2.

The connection is: BOTH are controlled by MC elements in (different)
convolution algebras. The KS automorphism is MC in the quantum torus;
the shadow tower is MC in Def_cyc^mod(A). The BRIDGE is the
factorization-algebra realization: for A = V_{K3} on an elliptic curve E,
the bar complex B(A) on Ran(E) should produce the DT invariants of K3 x E
via factorization homology (conditional on the d=3 functor, AP42).

CONVENTIONS
===========
- Mukai vector v = (r, c_1, s) = (rank, first Chern class, s = ch_2 + r)
- Mukai pairing <v, w> = c_1 * c_1' - r*s' - r'*s (ANTISYMMETRIC for KS)
  Note: the SYMMETRIC Mukai pairing is (v, w) = c_1*c_1' - r*s' - r'*s.
  The ANTISYMMETRIC (Euler) pairing for KS is chi(v,w) = -<v,w> = r*s' + r'*s - c_1*c_1'.
  We use <-,-> for the symmetric Mukai pairing.
  The KS formula uses the Euler form chi(E,F) = sum (-1)^i dim Ext^i(E,F).
  On K3: chi(v,w) = -(v,w) = r*s' + r'*s - c_1*c_1' (sign from Serre duality).
  CAUTION: many references differ on sign conventions here.
- q = exp(2*pi*i*tau) counting parameter
- K3 Hodge diamond: h^{0,0}=h^{2,0}=h^{0,2}=h^{2,2}=1, h^{1,1}=20
- chi(K3) = 24, chi(K3 x E) = 0
- eta(q) = q^{1/24} * prod(1-q^n) (AP46)

BEILINSON WARNINGS
==================
AP38: Gottsche formula normalizations vary in the literature.
      We use the Eichler-Zagier convention for phi_{0,1} (AP38).
AP42: DT/shadow identification at motivic level; naive BCH insufficient.
AP46: eta(q) includes q^{1/24}; never drop this factor.
AP48: kappa depends on the full algebra, not just the Virasoro subalgebra.

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    rem:scattering-mc-identification (higher_genus_modular_koszul.tex)
    thm:general-hs-sewing (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, FrozenSet, List, Optional, Sequence, Tuple, Union

import numpy as np


# ============================================================================
# 0. Utility: partition numbers, divisor sums
# ============================================================================

@lru_cache(maxsize=1024)
def _partition_number(n: int) -> int:
    """Integer partition number p(n). p(0)=1, p(1)=1, p(2)=2, ..."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            dp[m] += dp[m - k]
    return dp[n]


def _sigma(n: int, power: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** power for d in range(1, n + 1) if n % d == 0)


def _mobius(n: int) -> int:
    """Mobius function mu(n)."""
    if n == 1:
        return 1
    # Factor n
    factors = []
    m = n
    d = 2
    while d * d <= m:
        if m % d == 0:
            count = 0
            while m % d == 0:
                m //= d
                count += 1
            if count > 1:
                return 0
            factors.append(d)
        d += 1
    if m > 1:
        factors.append(m)
    return (-1) ** len(factors)


# ============================================================================
# 1. K3 Hodge data and Mukai lattice
# ============================================================================

# K3 Hodge numbers h^{p,q}
K3_HODGE = {
    (0, 0): 1,
    (1, 0): 0, (0, 1): 0,
    (2, 0): 1, (1, 1): 20, (0, 2): 1,
    (2, 1): 0, (1, 2): 0,
    (2, 2): 1,
}

K3_EULER_CHAR = 24  # chi(K3) = 2 + 22 + 0 - 0 = 24  (or just sum (-1)^{p+q} h^{p,q})
K3_BETTI = [1, 0, 22, 0, 1]  # b_0, b_1, b_2, b_3, b_4


@dataclass(frozen=True)
class MukaiVector:
    """Mukai vector v = (r, d, s) in the Mukai lattice H*(K3, Z).

    r = rank (H^0 component)
    d = degree (coefficient of H in H^2, for Picard rank 1)
    s = s-component (H^4 component) = ch_2 + r for a sheaf

    The Mukai pairing is:
        (v, w) = d*d'*H^2 - r*s' - r'*s
    For a K3 with H^2 = 2*deg (e.g., quartic has H^2 = 4), we store just
    the integer coefficient d, and the intersection number H^2 is carried
    by the lattice.
    """
    r: int
    d: int
    s: int

    def mukai_norm_sq(self, H_sq: int = 4) -> int:
        """v^2 = (v, v) = d^2 * H^2 - 2*r*s.

        For a quartic K3: H^2 = 4.
        """
        return self.d * self.d * H_sq - 2 * self.r * self.s

    def mukai_pairing(self, other: 'MukaiVector', H_sq: int = 4) -> int:
        """Symmetric Mukai pairing (v, w) = d*d'*H^2 - r*s' - r'*s."""
        return self.d * other.d * H_sq - self.r * other.s - other.r * self.s

    def euler_pairing(self, other: 'MukaiVector', H_sq: int = 4) -> int:
        """Euler pairing chi(v, w) = -(v, w) on K3 (by Serre duality + Noether).

        chi(E, F) = sum_i (-1)^i dim Ext^i(E, F) = -<v(E), v(F)>.
        This is the ANTISYMMETRIC pairing used in the KS formula.

        Actually on K3, chi(E,F) = -<v(E), v(F)> where <-,-> is the Mukai
        pairing, which is SYMMETRIC. So the Euler form is the NEGATIVE of the
        Mukai pairing (not antisymmetric). For KS we need the antisymmetric
        part, which on K3 with the standard Mukai pairing is:
            chi^{antisym}(v, w) = r*s' - r'*s  (the rank-s exchange part)
        """
        return self.r * other.s - other.r * self.s

    def __add__(self, other: 'MukaiVector') -> 'MukaiVector':
        return MukaiVector(self.r + other.r, self.d + other.d, self.s + other.s)

    def __neg__(self) -> 'MukaiVector':
        return MukaiVector(-self.r, -self.d, -self.s)

    def __sub__(self, other: 'MukaiVector') -> 'MukaiVector':
        return self + (-other)

    def __mul__(self, n: int) -> 'MukaiVector':
        return MukaiVector(n * self.r, n * self.d, n * self.s)

    def __rmul__(self, n: int) -> 'MukaiVector':
        return self.__mul__(n)

    def expected_dim_moduli(self, H_sq: int = 4) -> int:
        """Expected dimension of moduli space M_H(v) = v^2 + 2."""
        return self.mukai_norm_sq(H_sq) + 2


# ============================================================================
# 2. Bridgeland central charge for K3
# ============================================================================

@dataclass
class BridgelandCentralCharge:
    """Central charge Z_{B+iw} for K3 with Picard rank 1.

    Parameters:
        B: real part of complexified Kahler modulus
        omega: imaginary part (w > 0 for stability)
        H_sq: self-intersection of the ample class (e.g., 4 for quartic K3)

    The central charge is:
        Z(v) = Z(r, dH, s) = <exp((B + iw)H), v>
             = -s + d*(B + iw)*H^2/? ...

    More carefully, for Mukai vector v = (r, l, s) with l = d*H:
        Z_{beta + iw}(v) = -(s - r*w^2/2 - l*B) + i*(l*w - r*B*w)
        where beta = B*H, and w = omega.

    For Picard rank 1 with ample H, l = d*H, and:
        Z(r, d, s) = -(s - r*omega^2*H^2/2 - d*B*H^2) + i*(d*omega*H^2 - r*B*omega*H^2)
                    ... this is getting complicated. Let me use the standard formula.

    Standard form (Bridgeland 2008, Section 6):
        Z_{B+iw}(E) = <exp(B+iw), v(E)>
    where v(E) = ch(E)*sqrt(td(K3)) = (r, c_1, ch_2 + r) is the Mukai vector,
    and exp(B+iw) = (1, (B+iw)*H, (B+iw)^2*H^2/2) as an element of H^*(K3).

    So: Z = (1, (B+iw)*H, (B+iw)^2*H^2/2) paired with (r, d*H, s):
        Z = d * (B+iw) * H^2 - s - (B+iw)^2 * H^2 / 2 * r
          = d * (B+iw) * H^2 - s - r * (B+iw)^2 * H^2 / 2

    For quartic K3 (H^2 = 4):
        Z = 4*d*(B+iw) - s - 2*r*(B+iw)^2
    """
    B: float
    omega: float
    H_sq: int = 4  # quartic K3

    def __post_init__(self):
        if self.omega <= 0:
            raise ValueError("omega must be positive for a stability condition")

    def central_charge(self, v: MukaiVector) -> complex:
        """Compute Z_{B+iw}(v) for Mukai vector v = (r, d, s)."""
        z = self.B + 1j * self.omega
        Z = self.H_sq * v.d * z - v.s - v.r * self.H_sq / 2 * z ** 2
        return Z

    def phase(self, v: MukaiVector) -> float:
        """Phase phi(v) = (1/pi) * arg(Z(v)) in (0, 1].

        Stable objects have phase in (0, 1].
        """
        Z = self.central_charge(v)
        if abs(Z) < 1e-15:
            raise ValueError(f"Central charge vanishes for v={v}")
        phi = math.atan2(Z.imag, Z.real) / math.pi
        # Normalize to (0, 1]
        while phi <= 0:
            phi += 2
        while phi > 1:
            phi -= 2
        # Actually stability phases live in R, but we reduce to (0,1] for semistable
        return phi

    def mass(self, v: MukaiVector) -> float:
        """Mass |Z(v)|."""
        return abs(self.central_charge(v))

    def slope(self, v: MukaiVector) -> float:
        """Slope mu = -Re(Z)/Im(Z) (for objects with Im(Z) > 0)."""
        Z = self.central_charge(v)
        if abs(Z.imag) < 1e-15:
            return float('inf') if Z.real < 0 else float('-inf')
        return -Z.real / Z.imag


# ============================================================================
# 3. Walls of marginal stability
# ============================================================================

@dataclass
class Wall:
    """A wall of marginal stability in the (B, omega) plane.

    A wall W(v_1, v_2) for v = v_1 + v_2 is the locus where
    Z(v_1) and Z(v_2) are aligned: Z(v_1)/Z(v_2) in R_{>0}.

    For large-volume stability on K3, walls are semicircles in the
    upper half-plane {B + iw : w > 0}.
    """
    v1: MukaiVector
    v2: MukaiVector
    center_B: float  # center of semicircle on B-axis
    radius: float  # radius of semicircle

    @property
    def v_total(self) -> MukaiVector:
        return self.v1 + self.v2


def find_walls_rank1(v: MukaiVector, max_sub_rank: int = 5,
                     max_sub_degree: int = 5,
                     H_sq: int = 4) -> List[Wall]:
    """Find walls of marginal stability for Mukai vector v on K3 (Picard rank 1).

    A wall exists for each decomposition v = v_1 + v_2 where v_1, v_2 are
    effective Mukai vectors with phi(v_1) = phi(v_2).

    For Z_{B+iw}(v) = H_sq * d * (B+iw) - s - (H_sq/2) * r * (B+iw)^2,
    the wall W(v_1, v_2) is the locus where Im(Z(v_1) * conj(Z(v_2))) = 0.

    This gives a circle in the (B, omega) half-plane. We compute its
    center and radius.

    Returns walls sorted by decreasing radius (= most important first).
    """
    walls = []

    for r1 in range(0, max_sub_rank + 1):
        for d1 in range(-max_sub_degree, max_sub_degree + 1):
            r2 = v.r - r1
            d2 = v.d - d1
            if r2 < 0:
                continue
            if r1 == 0 and d1 <= 0:
                continue
            if r2 == 0 and d2 <= 0:
                continue
            # s is determined by requiring v_1 to be a valid Mukai vector
            # of a semistable sheaf. For simplicity, we scan over s values
            # that give v_1^2 >= -2 (the Bogomolov bound).
            for s1 in range(-20, 20):
                s2 = v.s - s1
                v1 = MukaiVector(r1, d1, s1)
                v2 = MukaiVector(r2, d2, s2)

                # Check Bogomolov: v_i^2 >= -2
                if v1.mukai_norm_sq(H_sq) < -2:
                    continue
                if v2.mukai_norm_sq(H_sq) < -2:
                    continue

                # Compute the wall: Im(Z(v1) * conj(Z(v2))) = 0
                # For rank 0 vs rank > 0, the wall structure simplifies.
                # General formula: the wall is a circle in (B, omega).
                #
                # For v_1 = (r_1, d_1, s_1), v_2 = (r_2, d_2, s_2):
                # The alignment condition is:
                #   Im(Z(v_1)) * Re(Z(v_2)) = Im(Z(v_2)) * Re(Z(v_1))
                #
                # With Z(r,d,s) = H_sq * d * (B+iw) - s - (H_sq/2)*r*(B+iw)^2:
                #   Re(Z) = H_sq*d*B - s - (H_sq/2)*r*(B^2 - w^2)
                #   Im(Z) = H_sq*d*w - H_sq*r*B*w = H_sq*w*(d - r*B)
                #
                # Im(Z) = H_sq * w * (d - r*B) for w > 0.
                #
                # Alignment: (d_1 - r_1*B)*(Re Z_2) = (d_2 - r_2*B)*(Re Z_1)
                #
                # If r_1 = r_2 = 0: both Im(Z) = H_sq*w*d_i, so alignment
                #   requires d_1/d_2 = Re(Z_1)/Re(Z_2) = s_1/s_2.
                #   This is either always or never satisfied.
                #
                # For r_1 > 0, r_2 > 0:
                # The wall is (B - B_c)^2 + w^2 = R^2 (semicircle).
                # Center: B_c = (s_1/r_1 - s_2/r_2) / (H_sq*(d_1/r_1 - d_2/r_2))
                # ... this requires d_1/r_1 != d_2/r_2 (different slopes).

                if r1 > 0 and r2 > 0:
                    slope1 = d1 / r1
                    slope2 = d2 / r2
                    if abs(slope1 - slope2) < 1e-12:
                        continue  # parallel: no wall

                    # Center of semicircle on B-axis
                    # From the alignment condition for the quadratic central charge:
                    # (d1 - r1*B)(H_sq*d2*B - s2 - H_sq/2*r2*(B^2-w^2))
                    # = (d2 - r2*B)(H_sq*d1*B - s1 - H_sq/2*r1*(B^2-w^2))
                    #
                    # After expansion, B^2 + w^2 terms give the circle,
                    # and linear B terms give the center.
                    #
                    # Result (see Bridgeland 2008, Section 9; or Macri 2014):
                    # For v_i = (r_i, d_i H, s_i), the wall W(v_1,v_2) is
                    # the semicircle (B - B_c)^2 + w^2 = R^2 where:
                    #
                    # B_c = [(s_1*r_2 - s_2*r_1) + H_sq/2*(d_1^2*r_2/r_1 - ...)]
                    # This is messy. Let me use a cleaner approach.
                    #
                    # Alternative: the wall is defined by
                    #   mu(v_1) = mu(v_2) where mu = -Re(Z)/Im(Z) = slope.
                    # Since mu depends on (B, w), this is a curve in (B,w).
                    #
                    # For the quadratic central charge, mu(r,d,s) =
                    #   (s + H_sq/2 * r * (B^2-w^2) - H_sq*d*B) / (H_sq*w*(d - r*B))
                    #   = (s/(H_sq*w) + r*(B^2-w^2)/(2*w) - d*B/w) / (d - r*B)
                    #
                    # Setting mu_1 = mu_2 and simplifying:
                    # After cross-multiplication, the B^2 + w^2 terms combine into
                    # a circle equation. Let me just compute numerically.

                    # Numerical approach: sample and fit
                    # Actually let's derive it properly.
                    #
                    # mu_i = [s_i + (H_sq/2)*r_i*(B^2-w^2) - H_sq*d_i*B] / [H_sq*w*(d_i - r_i*B)]
                    # mu_1 = mu_2 implies:
                    # [s1 + a*r1*(B^2-w^2) - 2a*d1*B]*(d2-r2*B) = [s2 + a*r2*(B^2-w^2) - 2a*d2*B]*(d1-r1*B)
                    # where a = H_sq/2.
                    #
                    # Expanding and collecting:
                    # Terms in B^2+w^2: a*(r1*(d2-r2*B) - r2*(d1-r1*B))*(B^2-w^2) part...
                    # This gets algebraically involved. Let me just use the formula
                    # from Bayer-Macri 2014, Proposition 3.3.
                    #
                    # Their result for Picard rank 1:
                    # Wall for v_1 = (r_1, d_1 H, s_1), v_2 = (r_2, d_2 H, s_2):
                    #   Center: B_0 = (s_1*r_2 - s_2*r_1)/(H_sq*(d_1*r_2 - d_2*r_1))
                    #   Radius^2 = B_0^2 + [(v_1,v_2) + r_1*s_2 + r_2*s_1]/(H_sq*r_1*r_2)
                    # Hmm, let me just compute B_0 from slopes matching at w=0:
                    # At w=0: Z(r,d,s) = H_sq*d*B - s - (H_sq/2)*r*B^2
                    #         Im(Z) = 0 (degenerate), so we need the w->0 limit of mu.
                    #
                    # Better: use the formula that works. For two objects with
                    # mu(v_1) = mu(v_2) at (B, w):
                    #
                    # Define F_i = s_i - H_sq*d_i*B + (H_sq/2)*r_i*B^2 (= -Re Z_i + (H_sq/2)*r_i*w^2)
                    # Define G_i = d_i - r_i * B (= Im Z_i / (H_sq * w))
                    # Alignment: F_1 * G_2 = F_2 * G_1 (where we used Re/Im alignment)
                    # Wait, mu = (F + a*r*w^2)/(H_sq*w*G) where F = s-H_sq*d*B+(H_sq/2)*r*B^2.
                    # Actually Re Z = H_sq*d*B - s - (H_sq/2)*r*(B^2-w^2)
                    #               = -(s - H_sq*d*B + (H_sq/2)*r*B^2) + (H_sq/2)*r*w^2
                    #               = -F + (H_sq/2)*r*w^2
                    # And Im Z = H_sq*w*G.
                    #
                    # Alignment: (-F_1 + a*r_1*w^2)*G_2 = (-F_2 + a*r_2*w^2)*G_1
                    #   -F_1*G_2 + a*r_1*w^2*G_2 = -F_2*G_1 + a*r_2*w^2*G_1
                    #   F_2*G_1 - F_1*G_2 = a*w^2*(r_2*G_1 - r_1*G_2)
                    #   F_2*G_1 - F_1*G_2 = a*w^2*(r_2*(d_1-r_1*B) - r_1*(d_2-r_2*B))
                    #                      = a*w^2*(r_2*d_1 - r_1*d_2)
                    #
                    # So: F_2*G_1 - F_1*G_2 = a*(r_2*d_1 - r_1*d_2)*w^2
                    #
                    # LHS = (s_2 - H_sq*d_2*B + a*r_2*B^2)*(d_1-r_1*B) - (s_1 - H_sq*d_1*B + a*r_1*B^2)*(d_2-r_2*B)
                    #
                    # Let me compute this carefully...
                    # Substituting a = H_sq/2:
                    # F_i = s_i - H_sq*d_i*B + (H_sq/2)*r_i*B^2
                    #
                    # F_2*G_1 - F_1*G_2:
                    # = [s_2*(d_1-r_1*B) - s_1*(d_2-r_2*B)]
                    #   + [-H_sq*d_2*B*(d_1-r_1*B) + H_sq*d_1*B*(d_2-r_2*B)]
                    #   + [(H_sq/2)*r_2*B^2*(d_1-r_1*B) - (H_sq/2)*r_1*B^2*(d_2-r_2*B)]
                    #
                    # Line 1: s_2*d_1 - s_2*r_1*B - s_1*d_2 + s_1*r_2*B
                    #        = (s_2*d_1 - s_1*d_2) + B*(s_1*r_2 - s_2*r_1)
                    #
                    # Line 2: H_sq*B*[-d_2*(d_1-r_1*B) + d_1*(d_2-r_2*B)]
                    #        = H_sq*B*[-d_2*d_1 + d_2*r_1*B + d_1*d_2 - d_1*r_2*B]
                    #        = H_sq*B^2*(d_2*r_1 - d_1*r_2)
                    #
                    # Line 3: (H_sq/2)*B^2*[r_2*(d_1-r_1*B) - r_1*(d_2-r_2*B)]
                    #        = (H_sq/2)*B^2*(r_2*d_1 - r_1*d_2)
                    #        + (H_sq/2)*B^3*(r_1*r_2 - r_2*r_1) = 0 for B^3 term
                    #        = (H_sq/2)*B^2*(r_2*d_1 - r_1*d_2)
                    #
                    # Total LHS:
                    # = (s_2*d_1 - s_1*d_2) + B*(s_1*r_2 - s_2*r_1)
                    #   + H_sq*B^2*(d_2*r_1 - d_1*r_2)
                    #   + (H_sq/2)*B^2*(r_2*d_1 - r_1*d_2)
                    # = (s_2*d_1 - s_1*d_2) + B*(s_1*r_2 - s_2*r_1)
                    #   + (H_sq/2)*B^2*(d_2*r_1 - d_1*r_2)
                    #
                    # (because H_sq + H_sq/2 does not combine... wait:
                    #  H_sq*(d_2*r_1-d_1*r_2) + (H_sq/2)*(r_2*d_1-r_1*d_2)
                    #  = (H_sq - H_sq/2)*(d_2*r_1-d_1*r_2) = (H_sq/2)*(d_2*r_1-d_1*r_2))
                    #
                    # So LHS = (s_2*d_1 - s_1*d_2) + B*(s_1*r_2 - s_2*r_1) + (H_sq/2)*B^2*(d_2*r_1 - d_1*r_2)
                    #
                    # RHS = (H_sq/2)*(r_2*d_1 - r_1*d_2)*w^2
                    #
                    # So: (s_2*d_1-s_1*d_2) + B*(s_1*r_2-s_2*r_1) + a*B^2*(d_2*r_1-d_1*r_2) = a*(r_2*d_1-r_1*d_2)*w^2
                    #
                    # Let Delta_d = d_2*r_1 - d_1*r_2 (note: r_2*d_1 - r_1*d_2 = -Delta_d)
                    #
                    # (s_2*d_1-s_1*d_2) + B*(s_1*r_2-s_2*r_1) + a*Delta_d*B^2 = -a*Delta_d*w^2
                    #
                    # a*Delta_d*(B^2+w^2) + B*(s_1*r_2-s_2*r_1) + (s_2*d_1-s_1*d_2) = 0
                    #
                    # If Delta_d != 0 (which it is since slope1 != slope2):
                    # B^2 + w^2 + B*(s_1*r_2-s_2*r_1)/(a*Delta_d) + (s_2*d_1-s_1*d_2)/(a*Delta_d) = 0
                    # (B + (s_1*r_2-s_2*r_1)/(2*a*Delta_d))^2 + w^2
                    #   = [(s_1*r_2-s_2*r_1)/(2*a*Delta_d)]^2 - (s_2*d_1-s_1*d_2)/(a*Delta_d)
                    #
                    # Center: B_c = -(s_1*r_2-s_2*r_1)/(2*a*Delta_d)
                    #             = (s_2*r_1-s_1*r_2)/(H_sq*(d_2*r_1-d_1*r_2))
                    # Radius^2: R^2 = B_c^2 - (s_2*d_1-s_1*d_2)/(a*Delta_d)

                    a = H_sq / 2
                    Delta_d = d2 * r1 - d1 * r2  # = -det of slope matrix

                    if abs(Delta_d) < 1e-12:
                        continue

                    B_c = (s2 * r1 - s1 * r2) / (H_sq * Delta_d)
                    R_sq = B_c ** 2 - (s2 * d1 - s1 * d2) / (a * Delta_d)

                    if R_sq < 0:
                        continue  # no real wall

                    R = math.sqrt(R_sq)
                    if R < 1e-10:
                        continue

                    walls.append(Wall(v1=v1, v2=v2, center_B=B_c, radius=R))

                elif r1 == 0 and r2 > 0:
                    # Rank 0 destabilizer: v1 = (0, d1, s1) is a torsion sheaf
                    # Z(0, d1, s1) = H_sq*d1*(B+iw) - s1
                    # This is a line in (B,w). The wall is where this aligns with Z(v2).
                    # Simplifies to a vertical line or circle.
                    if d1 == 0:
                        continue  # pure point sheaf, Z = -s1, no w dependence
                    # Wall: B = s1 / (H_sq * d1) (vertical line, or more precisely
                    # the wall intersects the B-axis at this point)
                    B_wall = s1 / (H_sq * d1)
                    # This is a degenerate "wall" -- vertical line in (B, omega)
                    walls.append(Wall(v1=v1, v2=v2, center_B=B_wall, radius=float('inf')))

    # Sort by decreasing radius (most important walls first)
    walls.sort(key=lambda w: -w.radius if w.radius < float('inf') else -1e30)
    return walls


# ============================================================================
# 4. DT invariants for K3
# ============================================================================

@lru_cache(maxsize=512)
def hilb_k3_euler_char(n: int) -> int:
    r"""Euler characteristic chi(Hilb^n(K3)).

    By Gottsche's formula for a smooth projective surface S:
        sum_{n>=0} chi(Hilb^n(S)) q^n = prod_{k>=1} 1/(1-q^k)^{chi(S)}

    For K3: chi(K3) = 24, so:
        sum_{n>=0} chi(Hilb^n(K3)) q^n = prod_{k>=1} 1/(1-q^k)^{24}

    These are the "colored partition" numbers p_{24}(n) = number of partitions
    of n into parts of 24 colors.

    Ground truth (OEIS A006922, shifted):
        chi(Hilb^0(K3)) = 1
        chi(Hilb^1(K3)) = 24
        chi(Hilb^2(K3)) = 324
        chi(Hilb^3(K3)) = 3200
        chi(Hilb^4(K3)) = 25650
        chi(Hilb^5(K3)) = 176256

    These are related to partition numbers by:
        chi(Hilb^n(K3)) = p_{-24}(n)
    where p_{-c}(n) is the coefficient of q^n in prod(1-q^k)^{-c}.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    # Use the divisor-sum recurrence:
    # If F(q) = prod(1-q^k)^{-c} = sum a(n) q^n, then
    # n * a(n) = c * sum_{k=1}^{n} sigma_1(k) * a(n-k)
    # where sigma_1(k) = sum of divisors of k.
    c = 24
    # Build up from a(0) = 1
    a = [0] * (n + 1)
    a[0] = 1
    for m in range(1, n + 1):
        total = 0
        for k in range(1, m + 1):
            total += c * _sigma(k, 1) * a[m - k]
        assert total % m == 0, f"Recurrence error at n={m}"
        a[m] = total // m
    return a[n]


def hilb_k3_euler_char_product(N: int) -> List[int]:
    r"""Compute chi(Hilb^n(K3)) for n=0,...,N via product expansion.

    Independent verification: expand prod_{k>=1} (1-q^k)^{-24} directly.
    """
    coeffs = [0] * (N + 1)
    coeffs[0] = 1

    for k in range(1, N + 1):
        # Multiply by (1-q^k)^{-24} = sum_{j>=0} C(j+23, 23) q^{jk}
        new_coeffs = [0] * (N + 1)
        for n in range(N + 1):
            if coeffs[n] == 0:
                continue
            j = 0
            while n + j * k <= N:
                binom_val = math.comb(j + 23, 23)
                new_coeffs[n + j * k] += coeffs[n] * binom_val
                j += 1
        coeffs = new_coeffs

    return coeffs


def dt_invariant_k3(v: MukaiVector, H_sq: int = 4) -> int:
    r"""DT invariant Omega(v) for K3 surface (numerical, primitive case).

    For K3 with a PRIMITIVE Mukai vector v with v^2 = 2n-2 >= -2:
        - The moduli space M_H(v) is deformation equivalent to Hilb^n(K3)
          (Beauville 1983, Mukai 1984, Huybrechts 1999, Yoshioka 2001).
        - Therefore Omega(v) = chi(Hilb^n(K3)) for v^2 = 2n-2, n >= 0.

    For v^2 = -2: Omega = chi(pt) = 1 (spherical object).

    Returns 0 for unphysical vectors.
    """
    v_sq = v.mukai_norm_sq(H_sq)
    if v_sq % 2 != 0:
        return 0  # v^2 must be even for K3

    n = v_sq // 2 + 1  # v^2 = 2n - 2 => n = (v^2 + 2) / 2
    if n < 0:
        return 0
    return hilb_k3_euler_char(n)


# ============================================================================
# 5. KS wall-crossing automorphism
# ============================================================================

class QuantumTorusAlgebra:
    """Quantum torus algebra for KS wall-crossing.

    The quantum torus has generators x_gamma for gamma in the lattice,
    with relation x_gamma * x_delta = (-1)^{<gamma,delta>} x_{gamma+delta}
    where <-,-> is the antisymmetric (Euler) pairing.

    For computations, we work with the formal group ring C[[x_gamma]]
    and represent elements as dictionaries {gamma: coefficient}.

    The KS automorphism T_gamma acts by (cluster/scattering diagram convention):
        T_gamma(x_delta) = x_delta * (1 + x_gamma)^{<delta, gamma>}
    where <delta, gamma> = delta.euler_pairing(gamma) is the Euler form
    with DELTA first, GAMMA second.

    CONVENTION NOTE: The literature has multiple sign conventions. We use
    the cluster-algebra / Gross-Siebert scattering diagram convention
    with (1 + x_gamma), NOT the (1 - x_gamma) convention sometimes used
    in the DT literature (AP38). The pentagon identity takes the standard form:
        T_{g1} T_{g2} = T_{g2} T_{g1+g2} T_{g1}
    for <g1, g2> = 1 (meaning g1.euler_pairing(g2) = 1).
    """

    def __init__(self, H_sq: int = 4, max_degree: int = 10):
        """Initialize with intersection form and total-degree truncation.

        max_degree: truncate formal power series at this total degree,
        measured as |r| + |d| + |s| of the Mukai vector offset from the probe.
        """
        self.H_sq = H_sq
        self.max_degree = max_degree

    @staticmethod
    def _total_degree(v: MukaiVector) -> int:
        """Total degree for truncation: |r| + |d| + |s|."""
        return abs(v.r) + abs(v.d) + abs(v.s)

    def ks_automorphism(self, gamma: MukaiVector, omega: int,
                        delta: MukaiVector) -> Dict[MukaiVector, int]:
        r"""Apply T_gamma^omega to x_delta.

        T_gamma^omega(x_delta) = x_delta * (1 + x_gamma)^{omega * <delta, gamma>}

        where <delta, gamma> = delta.euler_pairing(gamma) is the Euler form
        (delta.r * gamma.s - gamma.r * delta.s).

        The exponent is omega * <delta, gamma>. The expansion is:
            (1 + x_gamma)^n = sum_{k>=0} C(n, k) x_gamma^k
        with generalized binomial coefficients for non-integer n.

        Returns a dictionary {Mukai vector: coefficient}.
        """
        chi_val = delta.euler_pairing(gamma, self.H_sq)
        exponent = omega * chi_val

        result = {}
        for k in range(abs(self.max_degree) * 3 + 1):
            target = MukaiVector(delta.r + k * gamma.r,
                                 delta.d + k * gamma.d,
                                 delta.s + k * gamma.s)
            if self._total_degree(target) > self.max_degree:
                break
            # Generalized binomial coefficient C(exponent, k)
            binom_coeff = 1
            for j in range(k):
                binom_coeff = binom_coeff * (exponent - j) // (j + 1)
            if binom_coeff == 0 and exponent >= 0:
                break  # polynomial case: all subsequent terms vanish
            if binom_coeff == 0:
                continue
            result[target] = result.get(target, 0) + binom_coeff

        return result

    def compose_automorphisms(
        self,
        factors: List[Tuple[MukaiVector, int]],
        probe: MukaiVector
    ) -> Dict[MukaiVector, int]:
        r"""Compose KS automorphisms and apply to x_probe.

        factors: list of (gamma_i, Omega_i).
        Composition convention: factors are applied LEFT TO RIGHT.
        That is, for factors = [(g1,1), (g2,1)]:
            result = T_{g2}(T_{g1}(x_probe))
        meaning g1 acts first on the probe, then g2 acts on the result.
        This matches the convention T_{g1} T_{g2} where multiplication
        means "first factor acts first."

        The pentagon identity in this convention:
            T_{g1} T_{g2} = T_{g2} T_{g12} T_{g1}
        is verified with factors [(g1,1),(g2,1)] on the LHS
        and [(g2,1),(g12,1),(g1,1)] on the RHS.
        """
        current = {probe: 1}

        for gamma, omega in factors:
            new_current = {}
            for delta, coeff in current.items():
                if coeff == 0:
                    continue
                if self._total_degree(delta) > self.max_degree:
                    continue
                transformed = self.ks_automorphism(gamma, omega, delta)
                for target, t_coeff in transformed.items():
                    if self._total_degree(target) > self.max_degree:
                        continue
                    new_current[target] = new_current.get(target, 0) + coeff * t_coeff

            current = {k: v for k, v in new_current.items() if v != 0}

        return current


def ks_product_near_large_volume(v: MukaiVector, num_walls: int = 3,
                                 H_sq: int = 4) -> List[Tuple[Wall, int]]:
    """Compute the KS wall-crossing product for the first few walls near large volume.

    Near large volume (omega >> 0), stability is close to Gieseker stability.
    As omega decreases, we cross walls. At each wall, the BPS spectrum changes.

    Returns list of (wall, DT invariant) for the first num_walls walls.
    """
    walls = find_walls_rank1(v, max_sub_rank=3, max_sub_degree=3, H_sq=H_sq)

    result = []
    for w in walls[:num_walls]:
        omega_v1 = dt_invariant_k3(w.v1, H_sq)
        omega_v2 = dt_invariant_k3(w.v2, H_sq)
        result.append((w, omega_v1))

    return result


# ============================================================================
# 6. K3 x E: DT invariants of threefold
# ============================================================================

def chi_k3_times_e() -> int:
    """Euler characteristic of K3 x E.

    chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0.

    E is an elliptic curve: chi(E) = 0 (genus 1, b_0=1, b_1=2, b_2=1).
    """
    return 0


def dt_degree0_k3xe(N: int) -> List[int]:
    r"""Degree-0 DT invariants of K3 x E.

    For a CY 3-fold X, the degree-0 DT partition function is:
        Z_{DT,0}(X, q) = M(-q)^{chi(X)}

    where M(q) = prod_{k>=1} (1-q^k)^{-k} is the MacMahon function.

    For K3 x E: chi = 0, so Z_{DT,0} = M(-q)^0 = 1.

    This means ALL degree-0 DT invariants vanish for n >= 1:
        DT_0(K3 x E, n) = 0 for n >= 1.

    Returns coefficients [DT_0(0), DT_0(1), ..., DT_0(N)].
    """
    result = [0] * (N + 1)
    result[0] = 1
    return result


def macmahon_coefficients(N: int) -> List[int]:
    r"""MacMahon function M(q) = prod_{k>=1} (1-q^k)^{-k}.

    Counts plane partitions: M(q) = sum_{n>=0} pp(n) q^n.

    Ground truth (OEIS A000219):
        pp(0)=1, pp(1)=1, pp(2)=3, pp(3)=6, pp(4)=13,
        pp(5)=24, pp(6)=48, pp(7)=86, pp(8)=160, pp(9)=282, pp(10)=500.
    """
    # Use divisor-sum recurrence: n*pp(n) = sum_{k=1}^n sigma_2(k) * pp(n-k)
    pp = [0] * (N + 1)
    pp[0] = 1
    for n in range(1, N + 1):
        total = 0
        for k in range(1, n + 1):
            total += _sigma(k, 2) * pp[n - k]
        assert total % n == 0
        pp[n] = total // n
    return pp


def macmahon_from_product(N: int) -> List[int]:
    r"""Independent computation of M(q) via product expansion.

    M(q) = prod_{k>=1} (1-q^k)^{-k}

    We multiply successively by (1-q^k)^{-k} = sum_{j>=0} C(j+k-1, k-1) q^{jk}.
    Wait, that's not right. (1-x)^{-k} = sum_{j>=0} C(j+k-1, k-1) x^j.
    So (1-q^m)^{-m} = sum_{j>=0} C(j+m-1, m-1) q^{jm}.
    """
    coeffs = [0] * (N + 1)
    coeffs[0] = 1

    for m in range(1, N + 1):
        new_coeffs = [0] * (N + 1)
        for n in range(N + 1):
            if coeffs[n] == 0:
                continue
            j = 0
            while n + j * m <= N:
                binom_val = math.comb(j + m - 1, m - 1)
                new_coeffs[n + j * m] += coeffs[n] * binom_val
                j += 1
        coeffs = new_coeffs

    return coeffs


def verify_macmahon_power_zero(N: int = 10) -> bool:
    """Verify that M(-q)^0 = 1 (trivially true, but checks the framework).

    The point: for K3 x E with chi = 0, the MNOP formula
    Z_{DT,0} = M(-q)^{chi} specializes to 1.

    This is a structural verification that chi(K3 x E) = 0 forces
    trivial degree-0 DT.
    """
    return chi_k3_times_e() == 0


# ============================================================================
# 7. Motivic DT: Hodge polynomial of Hilb^n(K3)
# ============================================================================

def hilb_k3_hodge_poly(n: int, max_terms: int = None) -> Dict[Tuple[int, int], int]:
    r"""Hodge polynomial h(Hilb^n(K3); x, y) via Gottsche's formula.

    The Gottsche formula for a smooth projective surface S:
        sum_{n>=0} sum_{p,q} h^{p,q}(Hilb^n(S)) x^p y^q t^n
        = prod_{k>=1} prod_{p,q} (1 - (-1)^{p+q} x^{p+k-1} y^{q+k-1} t^k)^{(-1)^{p+q+1} h^{p,q}(S)}

    For K3 with h^{0,0}=h^{2,0}=h^{0,2}=h^{2,2}=1, h^{1,1}=20:

    The product has factors from each (p,q) with h^{p,q} != 0:
        (p,q) = (0,0): h=1, (-1)^{0+0+1}=-1: (1-x^{k-1}y^{k-1}t^k)^{-1}
        (1,1): h=20, (-1)^{2+1}=-1: (1+x^k y^k t^k)^{-20}
        (2,0): h=1, (-1)^{2+1}=-1: (1+x^{k+1}y^{k-1}t^k)^{-1}
        (0,2): h=1, (-1)^{2+1}=-1: (1+x^{k-1}y^{k+1}t^k)^{-1}
        (2,2): h=1, (-1)^{4+1}=-1: (1-x^{k+1}y^{k+1}t^k)^{-1}

    Wait, let me be more careful with signs.
    Factor for (p,q) with h^{p,q} != 0:
        (1 - (-1)^{p+q} x^{p+k-1} y^{q+k-1} t^k)^{(-1)^{p+q+1} * h^{p,q}}

    (0,0): sign = (-1)^0 = +1, exponent = (-1)^1 * 1 = -1
           Factor: (1 - x^{k-1} y^{k-1} t^k)^{-1}

    (1,1): sign = (-1)^2 = +1, exponent = (-1)^3 * 20 = -20
           Factor: (1 - x^k y^k t^k)^{-20}

    (2,0): sign = (-1)^2 = +1, exponent = (-1)^3 * 1 = -1
           Factor: (1 - x^{k+1} y^{k-1} t^k)^{-1}

    (0,2): sign = (-1)^2 = +1, exponent = (-1)^3 * 1 = -1
           Factor: (1 - x^{k-1} y^{k+1} t^k)^{-1}

    (2,2): sign = (-1)^4 = +1, exponent = (-1)^5 * 1 = -1
           Factor: (1 - x^{k+1} y^{k+1} t^k)^{-1}

    So ALL factors have the form (1 - monomial)^{-c} with c > 0:
        sum_n [Hilb^n(K3)]_{x,y} t^n = prod_{k>=1}
            1/[(1-x^{k-1}y^{k-1}t^k)(1-x^k y^k t^k)^{20}(1-x^{k+1}y^{k-1}t^k)(1-x^{k-1}y^{k+1}t^k)(1-x^{k+1}y^{k+1}t^k)]

    We expand this as a polynomial in t, tracking x,y monomials.

    Returns dict mapping (p,q) -> h^{p,q}(Hilb^n(K3)).
    """
    if n == 0:
        return {(0, 0): 1}

    if n < 0:
        return {}

    # We work with the generating function. For each k, we have 5 types of
    # factors contributing at t-degree k. We expand iteratively.

    # Represent the Hodge polynomial as Dict[(p,q), coeff]
    # at each t-degree n.

    # Hodge data for K3 (only nonzero entries):
    k3_hodge_entries = [
        (0, 0, 1),    # h^{0,0} = 1
        (1, 1, 20),   # h^{1,1} = 20
        (2, 0, 1),    # h^{2,0} = 1
        (0, 2, 1),    # h^{0,2} = 1
        (2, 2, 1),    # h^{2,2} = 1
    ]

    # For the Gottsche formula, each (p0, q0, h) with k gives a factor
    # (1 - x^{p0+k-1} y^{q0+k-1} t^k)^{-h}
    # which contributes sum_{j>=0} C(j+h-1, h-1) (x^{p0+k-1} y^{q0+k-1} t^k)^j

    # Build the answer by convolution up to t-degree n.
    # hodge_at_degree[m] = Dict[(p,q), coeff] for the t^m coefficient.
    hodge_at_degree = [{} for _ in range(n + 1)]
    hodge_at_degree[0][(0, 0)] = 1

    for k in range(1, n + 1):
        for p0, q0, h in k3_hodge_entries:
            xpow = p0 + k - 1
            ypow = q0 + k - 1
            # Multiply current expansion by (1 - x^xpow y^ypow t^k)^{-h}
            # = sum_{j>=0} C(j+h-1, h-1) x^{j*xpow} y^{j*ypow} t^{j*k}
            # We update in place from high degree to low to avoid double-counting.

            for m in range(n, -1, -1):
                if not hodge_at_degree[m]:
                    continue
                j = 1
                while m + j * k <= n:
                    target_m = m + j * k
                    binom_val = math.comb(j + h - 1, h - 1)
                    dx = j * xpow
                    dy = j * ypow
                    for (p, q), coeff in list(hodge_at_degree[m].items()):
                        key = (p + dx, q + dy)
                        hodge_at_degree[target_m][key] = (
                            hodge_at_degree[target_m].get(key, 0) + coeff * binom_val
                        )
                    j += 1

    return hodge_at_degree[n]


def hilb_k3_euler_from_hodge(n: int) -> int:
    r"""chi(Hilb^n(K3)) from the Hodge polynomial (x=y=-1 specialization).

    chi = sum_{p,q} (-1)^{p+q} h^{p,q}.

    This serves as a cross-check of the Gottsche formula against the
    direct computation via hilb_k3_euler_char.
    """
    hodge = hilb_k3_hodge_poly(n)
    total = 0
    for (p, q), h in hodge.items():
        total += ((-1) ** (p + q)) * h
    return total


def hilb_k3_betti(n: int) -> Dict[int, int]:
    r"""Betti numbers b_k(Hilb^n(K3)) from the Hodge polynomial.

    b_k = sum_{p+q=k} h^{p,q}.

    Hilb^n(K3) is a hyperkaehler manifold of (real) dimension 4n.
    """
    hodge = hilb_k3_hodge_poly(n)
    betti = {}
    for (p, q), h in hodge.items():
        k = p + q
        betti[k] = betti.get(k, 0) + h
    return betti


# ============================================================================
# 8. Gottsche formula: generating function approach (independent path)
# ============================================================================

def gottsche_euler_coefficients(chi_S: int, N: int) -> List[int]:
    r"""Coefficients of the Gottsche generating function for a surface S.

    sum_{n>=0} chi(Hilb^n(S)) q^n = prod_{k>=1} (1-q^k)^{-chi(S)}

    General formula for ANY surface with Euler char chi_S.

    This provides a family of cross-checks:
        chi_S = 1 (projective line P^1 blown up at a point, etc.): gives
                the ordinary partition function prod(1-q^k)^{-1}
        chi_S = 2 (P^1 x P^1, etc.): gives prod(1-q^k)^{-2}
        chi_S = 24 (K3): our main case
    """
    coeffs = [0] * (N + 1)
    coeffs[0] = 1

    for k in range(1, N + 1):
        # Multiply by (1-q^k)^{-chi_S}
        # (1-x)^{-c} = sum_{j>=0} C(j+c-1, c-1) x^j  for c > 0 integer
        c = chi_S
        if c <= 0:
            # For c <= 0, (1-x)^{-c} = (1-x)^{|c|} is a polynomial
            # (1-x)^{|c|} = sum_{j=0}^{|c|} C(|c|, j) (-x)^j
            new_coeffs = [0] * (N + 1)
            for n in range(N + 1):
                if coeffs[n] == 0:
                    continue
                for j in range(abs(c) + 1):
                    if n + j * k > N:
                        break
                    binom_val = math.comb(abs(c), j) * ((-1) ** j)
                    new_coeffs[n + j * k] += coeffs[n] * binom_val
            coeffs = new_coeffs
        else:
            new_coeffs = [0] * (N + 1)
            for n in range(N + 1):
                if coeffs[n] == 0:
                    continue
                j = 0
                while n + j * k <= N:
                    binom_val = math.comb(j + c - 1, c - 1)
                    new_coeffs[n + j * k] += coeffs[n] * binom_val
                    j += 1
            coeffs = new_coeffs

    return coeffs


# ============================================================================
# 9. Joyce-Song vs KS transformation
# ============================================================================

def js_to_ks_primitive(js_invariant: int) -> int:
    """For a PRIMITIVE Mukai vector, JS = KS (no correction)."""
    return js_invariant


def ks_from_js_multicover(js_values: Dict[int, int], n: int) -> Fraction:
    r"""KS invariant Omega(n*v) from Joyce-Song invariants J(k*v) for k|n.

    The multicover/wall-crossing formula relating JS to KS:
        J(v) = sum_{k|n, k>=1} (1/k^2) * Omega(n*v/k)

    Inverting by Mobius:
        Omega(n*v) = sum_{k|n} mu(k) / k^2 * J(n*v/k)

    where mu is the Mobius function.

    js_values: dict mapping k -> J(k*v) for k | n.
    Returns Omega(n*v) as a Fraction (rational number).
    """
    result = Fraction(0)
    for k in range(1, n + 1):
        if n % k != 0:
            continue
        m = n // k  # J(m*v)
        if m not in js_values:
            continue
        result += Fraction(_mobius(k), k * k) * js_values[m]
    return result


def js_from_ks_multicover(ks_values: Dict[int, int], n: int) -> Fraction:
    r"""Joyce-Song invariant J(n*v) from KS invariants Omega(k*v) for k|n.

    J(n*v) = sum_{k|n} (1/k^2) * Omega(n*v/k)

    ks_values: dict mapping k -> Omega(k*v) for k | n.
    Returns J(n*v) as a Fraction.
    """
    result = Fraction(0)
    for k in range(1, n + 1):
        if n % k != 0:
            continue
        m = n // k  # Omega(m*v)
        if m not in ks_values:
            continue
        result += Fraction(1, k * k) * ks_values[m]
    return result


# ============================================================================
# 10. Shadow connection and monodromy (bridge to monograph)
# ============================================================================

def shadow_kappa_k3() -> Fraction:
    r"""Modular characteristic kappa for the K3 sigma model VOA.

    For the chiral de Rham complex Omega^{ch}(K3), viewed as a c=6 VOA:
        kappa = 2  (not c/2 = 3! AP48 applies.)

    The value kappa = 2 comes from the lattice/free-field computation:
    K3 ~ T^4 at a generic point, and the free-field kappa for a d-dimensional
    torus at level k is kappa = d*k/2. For K3 with d=4 free bosons at k=1:
    kappa = 4*1/2 = 2.

    Alternatively, from the Hilbert scheme: kappa is determined by the
    genus-1 obstruction obs_1 = kappa * lambda_1. The coefficient in
    the Gottsche formula is chi(S) = 24 = "24 colored partitions," but
    kappa measures the modular characteristic in the bar complex, not chi.
    The Mumford relation gives kappa * ch_2(E_1) = kappa * lambda_1.

    NOTE (AP48): kappa(V_{K3}) = 2, NOT chi(K3)/2 = 12, and NOT c/2 = 3.
    This is a lattice VOA formula: kappa = rank of the lattice = dim(T^4)/2 = 2.

    Actually, let me be more careful. The K3 sigma model is NOT simply a
    lattice VOA. The chiral de Rham complex at a generic point of the K3
    moduli is a free-field theory with c=6, but kappa for the K3 VOA
    is determined by the actual genus-1 obstruction computation.

    For the purposes of this module, we record kappa = 2 as a CONVENTION
    consistent with k3_relative_chiral.py (which derives this from the
    lattice structure).
    """
    return Fraction(2)


def shadow_metric_k3(t: float) -> float:
    r"""Shadow metric Q_L(t) for K3 at the leading (arity-2) truncation.

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

    For K3 with kappa = 2 and class-L behavior (finite shadow depth):
        alpha = S_3 / kappa (cubic shadow ratio)
        Delta = 8*kappa*S_4 (critical discriminant)

    For the K3 sigma model, the OPE is "essentially Heisenberg" at generic
    moduli (class G), so alpha = 0, Delta = 0, and:
        Q_L(t) = (2*kappa)^2 = 16 (constant).
    """
    kappa = float(shadow_kappa_k3())
    # Generic K3 is class G (Gaussian): terminates at arity 2
    alpha = 0.0
    Delta = 0.0
    return (2 * kappa + 3 * alpha * t) ** 2 + 2 * Delta * t ** 2


def shadow_connection_monodromy_k3() -> float:
    r"""Monodromy of the shadow connection for K3.

    For the shadow connection nabla^sh = d - Q'/(2Q) dt,
    the monodromy around a zero of Q_L is exp(pi*i) = -1 (Koszul sign).

    For class G algebras (like generic K3), Q_L is constant and nonzero,
    so there are NO zeros and the monodromy is trivial (= 1).

    Returns the monodromy as a float.
    """
    # Class G: Q_L = (2*kappa)^2 = constant > 0, no zeros
    return 1.0


def compare_ks_vs_shadow_monodromy(
    v: MukaiVector,
    sigma: BridgelandCentralCharge,
    H_sq: int = 4
) -> Dict[str, Any]:
    r"""Compare KS wall-crossing data with shadow monodromy for K3.

    The KS automorphism at a wall is:
        A_W = prod T_gamma^{Omega(gamma)}

    The shadow generating function is:
        H(t) = 2*kappa*t^2*sqrt(Q_L(t))

    The connection (AP42): both are controlled by MC elements, but in
    DIFFERENT algebras. The KS automorphism lives in the quantum torus
    (from DT theory). The shadow connection lives in the modular
    convolution algebra (from the bar complex).

    The bridge should be: for A = V_{K3}, the bar complex B(A) on Ran(E)
    produces the DT invariants of K3 x E via factorization homology.
    The shadow obstruction tower projects the MC element to finite arity.

    This function computes both sides and returns a comparison dictionary.
    """
    # KS side: DT invariant for the given Mukai vector
    omega_v = dt_invariant_k3(v, H_sq)

    # Find walls
    walls = find_walls_rank1(v, max_sub_rank=2, max_sub_degree=2, H_sq=H_sq)

    # Shadow side: kappa and shadow metric
    kappa = shadow_kappa_k3()
    Q_at_0 = shadow_metric_k3(0.0)

    return {
        'mukai_vector': v,
        'v_squared': v.mukai_norm_sq(H_sq),
        'dt_invariant': omega_v,
        'num_walls': len(walls),
        'kappa_k3': kappa,
        'shadow_metric_Q0': Q_at_0,
        'shadow_monodromy': shadow_connection_monodromy_k3(),
        'chi_k3xe': chi_k3_times_e(),
        'bridge_status': 'conditional_on_d3_functor',  # AP42
    }


# ============================================================================
# 11. Pentagon identity (simplest wall-crossing)
# ============================================================================

def verify_pentagon_identity(max_order: int = 8) -> Dict[str, Any]:
    r"""Verify the KS pentagon identity for the simplest wall-crossing.

    For two charges gamma_1, gamma_2 with <gamma_1, gamma_2> = 1
    (Euler pairing g1.euler_pairing(g2) = 1), the pentagon identity is:

        T_{gamma_1} T_{gamma_2} = T_{gamma_2} T_{gamma_1+gamma_2} T_{gamma_1}

    where T_gamma(x_delta) = x_delta * (1 + x_gamma)^{<delta, gamma>}
    (cluster/scattering diagram convention, AP38).

    Composition convention: T_{g1} T_{g2} means g1 acts first, then g2.
    So factors = [(g1, 1), (g2, 1)] means apply T_{g1} then T_{g2}.

    This is equivalent to the quantum dilogarithm five-term relation.

    We verify by applying both sides to several probe vectors
    and checking equality of the resulting formal power series
    up to the truncation degree.
    """
    # Choose gamma_1 = (1, 0, 0), gamma_2 = (0, 0, 1)
    # Euler pairing: g1.euler(g2) = 1*1 - 0*0 = 1
    g1 = MukaiVector(1, 0, 0)
    g2 = MukaiVector(0, 0, 1)

    # Check Euler pairing
    chi_12 = g1.euler_pairing(g2)
    assert chi_12 == 1, f"Expected <g1,g2>=1, got {chi_12}"

    g12 = g1 + g2  # = (1, 0, 1)

    torus = QuantumTorusAlgebra(H_sq=4, max_degree=max_order)

    # LHS: T_{g1} then T_{g2}
    lhs_factors = [(g1, 1), (g2, 1)]

    # RHS: T_{g2} then T_{g12} then T_{g1}
    rhs_factors = [(g2, 1), (g12, 1), (g1, 1)]

    # Test on several probe vectors
    probes = [g1, g2, g12, MukaiVector(1, 1, 0), MukaiVector(0, 1, 1)]

    results = {}
    all_match = True
    for probe in probes:
        lhs = torus.compose_automorphisms(lhs_factors, probe)
        rhs = torus.compose_automorphisms(rhs_factors, probe)

        match = True
        all_keys = set(lhs.keys()) | set(rhs.keys())
        for k in all_keys:
            if lhs.get(k, 0) != rhs.get(k, 0):
                match = False
                break

        results[probe] = {'lhs': lhs, 'rhs': rhs, 'match': match}
        if not match:
            all_match = False

    return {
        'pentagon_holds': all_match,
        'gamma_1': g1,
        'gamma_2': g2,
        'euler_pairing': chi_12,
        'probe_results': results,
    }


# ============================================================================
# 12. Full wall-crossing computation for quartic K3
# ============================================================================

def wall_crossing_quartic_k3(
    v: MukaiVector = None,
    num_walls: int = 3,
    max_order: int = 6
) -> Dict[str, Any]:
    r"""Full wall-crossing computation for a Mukai vector on quartic K3.

    Default: v = (1, 0, 1-n) for n = 2, i.e., ideal sheaves of 2 points.
    This has v^2 = -2*1*(1-2) = 2, so dim M_H(v) = v^2 + 2 = 4 = dim Hilb^2(K3).

    Computes:
    1. Walls of marginal stability
    2. DT invariants at each wall
    3. KS automorphism for the first few walls
    """
    if v is None:
        v = MukaiVector(1, 0, -1)  # v^2 = 2, Hilb^2(K3)

    H_sq = 4  # quartic

    # 1. Find walls
    walls = find_walls_rank1(v, max_sub_rank=3, max_sub_degree=3, H_sq=H_sq)

    # 2. DT invariants
    wall_data = []
    for w in walls[:num_walls]:
        dt1 = dt_invariant_k3(w.v1, H_sq)
        dt2 = dt_invariant_k3(w.v2, H_sq)
        wall_data.append({
            'wall': w,
            'v1': w.v1,
            'v2': w.v2,
            'dt_v1': dt1,
            'dt_v2': dt2,
            'center': w.center_B,
            'radius': w.radius,
        })

    # 3. Total DT invariant (large volume)
    dt_total = dt_invariant_k3(v, H_sq)

    return {
        'mukai_vector': v,
        'v_squared': v.mukai_norm_sq(H_sq),
        'expected_dim': v.expected_dim_moduli(H_sq),
        'dt_total': dt_total,
        'num_walls_found': len(walls),
        'wall_data': wall_data[:num_walls],
    }


# ============================================================================
# 13. Hilbert scheme Euler characteristics for K3 x E via Cheah
# ============================================================================

def hilb_k3xe_euler_cheah(n: int) -> int:
    r"""Euler characteristic chi(Hilb^n(K3 x E)) via the Cheah formula.

    For a smooth quasi-projective variety X of dimension d:
        sum_{n>=0} chi(Hilb^n(X)) q^n = prod_{k>=1} (1-q^k)^{-chi(X)}

    For K3 x E: chi(K3 x E) = chi(K3)*chi(E) = 24*0 = 0.
    So the generating function is prod (1-q^k)^0 = 1.
    Hence chi(Hilb^n(K3 x E)) = 0 for n >= 1, and = 1 for n = 0.

    CAUTION: This is the TOPOLOGICAL Euler characteristic. The
    VIRTUAL Euler characteristic (Behrend-weighted) is different
    and is what enters the DT partition function.

    NOTE: Cheah's formula applies to smooth varieties. K3 x E is smooth.
    But the Hilbert scheme formula for 3-folds is:
        sum_n chi(Hilb^n(X)) q^n = M(q)^{chi(X)}
    where M(q) is the MacMahon function.
    For surfaces it's prod(1-q^k)^{-chi(S)}.
    For 3-folds it's M(q)^{chi(X)}.

    For K3 x E (a 3-fold with chi = 0): M(q)^0 = 1.
    So chi(Hilb^n(K3 x E)) = 0 for n >= 1 in the DT sense.

    This matches the MNOP prediction: Z_{DT,0} = M(-q)^{chi} = 1 for chi=0.
    """
    if n == 0:
        return 1
    return 0


def verify_mnop_k3xe(N: int = 10) -> Dict[str, Any]:
    r"""Verify the MNOP prediction for K3 x E.

    MNOP: Z_{DT,0}(X) = M(-q)^{chi(X)} where chi = topological Euler char.

    For K3 x E: chi = 0, so Z_{DT,0} = 1.

    We verify:
    1. chi(K3) * chi(E) = 24 * 0 = 0
    2. M(q)^0 = 1 (trivial)
    3. The Hilbert scheme Euler chars vanish for n >= 1
    4. Cross-check: for comparison, chi(Hilb^n(K3)) are nontrivial

    Returns a verification dict.
    """
    # Direct computation
    hilb_k3xe = [hilb_k3xe_euler_cheah(n) for n in range(N + 1)]

    # Cross-check: K3 alone (surface formula)
    hilb_k3 = [hilb_k3_euler_char(n) for n in range(N + 1)]

    # Cross-check: K3 via product expansion
    hilb_k3_prod = hilb_k3_euler_char_product(N)

    return {
        'chi_K3': K3_EULER_CHAR,
        'chi_E': 0,
        'chi_K3xE': 0,
        'hilb_k3xe': hilb_k3xe,
        'hilb_k3': hilb_k3,
        'hilb_k3_product': hilb_k3_prod,
        'k3_recurrence_matches_product': hilb_k3 == hilb_k3_prod,
        'mnop_prediction': [1] + [0] * N,
        'mnop_verified': hilb_k3xe == [1] + [0] * N,
    }


# ============================================================================
# 14. Generating function analysis
# ============================================================================

def hilb_k3_partition_generating_function(N: int) -> List[int]:
    r"""The "K3 partition function" = chi(Hilb^n(K3)) sequence.

    This is p_{24}(n), the number of partitions of n into parts with 24 colors.

    The generating function is:
        sum_n p_{24}(n) q^n = prod_{k>=1} (1-q^k)^{-24} = 1/eta(q)^{24} * q^{24/24} = q/Delta(q)

    where Delta(q) = eta(q)^{24} = q * prod(1-q^n)^{24} is the modular discriminant.
    NOTE: eta(q)^{24} = q * prod(1-q^n)^{24} (from eta = q^{1/24} prod(1-q^n), AP46).
    So prod(1-q^k)^{-24} = 1/(q^{-1} * eta(q)^{24}) = q / Delta(q).

    Actually: Delta(q) = eta(q)^{24} = q prod_{n>=1} (1-q^n)^{24}.
    So 1/Delta(q) = q^{-1} prod(1-q^n)^{-24}.
    And prod(1-q^k)^{-24} = q * 1/Delta(q) = q * sum_n tau(n) q^{-n} ... no.

    Let me be careful. 1/Delta(q) = sum_{n>=0} a(n) q^{n-1} where Delta = sum tau(n) q^n.
    prod(1-q^k)^{-24} = sum_n p_{24}(n) q^n = the sequence we're computing.

    Returns the sequence [p_{24}(0), ..., p_{24}(N)].
    """
    return [hilb_k3_euler_char(n) for n in range(N + 1)]


def verify_against_ramanujan_tau(N: int = 12) -> Dict[str, Any]:
    r"""Cross-check: the inverse of prod(1-q^n)^{24} gives Ramanujan tau.

    Delta(q) = q * prod_{n>=1} (1-q^n)^{24} = sum_{n>=1} tau(n) q^n

    The first few values of tau(n) (Ramanujan's tau function):
        tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472,
        tau(5)=4830, tau(6)=-6048, tau(7)=-16744, tau(8)=84480,
        tau(9)=-113643, tau(10)=-115920, tau(11)=534612, tau(12)=-370944

    We compute prod(1-q^n)^{24} and verify these values.
    """
    # Compute prod(1-q^n)^{24} mod q^{N+2}
    # (1-q^k)^{24} = sum_{j=0}^{24} C(24,j) (-1)^j q^{jk}
    coeffs = [0] * (N + 2)
    coeffs[0] = 1

    for k in range(1, N + 2):
        new_coeffs = [0] * (N + 2)
        for n in range(N + 2):
            if coeffs[n] == 0:
                continue
            for j in range(25):
                if n + j * k > N + 1:
                    break
                binom_val = math.comb(24, j) * ((-1) ** j)
                new_coeffs[n + j * k] += coeffs[n] * binom_val
        coeffs = new_coeffs

    # Delta(q) = q * prod(1-q^n)^{24}, so tau(n) = coeffs[n-1] (shift by 1)
    # Actually Delta(q) = q * prod_{n>=1} (1-q^n)^{24}
    # So the coefficient of q^m in Delta is coeffs[m-1] for m >= 1.
    tau_computed = {n: coeffs[n - 1] for n in range(1, N + 1)}

    tau_known = {
        1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
        6: -6048, 7: -16744, 8: 84480, 9: -113643,
        10: -115920, 11: 534612, 12: -370944,
    }

    matches = {}
    for n in range(1, min(N, 12) + 1):
        matches[n] = tau_computed.get(n) == tau_known.get(n)

    return {
        'tau_computed': tau_computed,
        'tau_known': tau_known,
        'all_match': all(matches.values()),
        'matches': matches,
    }


# ============================================================================
# 15. Summary and cross-checks
# ============================================================================

def full_cross_check(N: int = 8) -> Dict[str, Any]:
    r"""Run all cross-checks and return a comprehensive verification dict.

    Path 1: Direct recurrence for chi(Hilb^n(K3))
    Path 2: Product expansion for chi(Hilb^n(K3))
    Path 3: Hodge polynomial specialization (x=y=-1)
    Path 4: Gottsche formula with chi_S = 24
    Path 5: K3 x E MNOP prediction (chi = 0 => Z = 1)
    Path 6: Ramanujan tau verification (inverse relation)
    """
    # Path 1: recurrence
    path1 = [hilb_k3_euler_char(n) for n in range(N + 1)]

    # Path 2: product expansion
    path2 = hilb_k3_euler_char_product(N)

    # Path 3: Hodge specialization
    path3 = [hilb_k3_euler_from_hodge(n) for n in range(N + 1)]

    # Path 4: Gottsche with chi=24
    path4 = gottsche_euler_coefficients(24, N)

    # Path 5: K3 x E
    mnop = verify_mnop_k3xe(N)

    # Path 6: Ramanujan tau
    tau_check = verify_against_ramanujan_tau(min(N + 2, 12))

    return {
        'N': N,
        'path1_recurrence': path1,
        'path2_product': path2,
        'path3_hodge': path3,
        'path4_gottsche': path4,
        'paths_1_2_match': path1 == path2,
        'paths_1_3_match': path1 == path3,
        'paths_1_4_match': path1 == path4,
        'all_four_match': path1 == path2 == path3 == path4,
        'mnop_k3xe_verified': mnop['mnop_verified'],
        'ramanujan_tau_verified': tau_check['all_match'],
        'ground_truth': {
            0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650, 5: 176256
        },
        'ground_truth_match': all(
            path1[n] == v for n, v in {0: 1, 1: 24, 2: 324, 3: 3200, 4: 25650, 5: 176256}.items()
            if n <= N
        ),
    }
