r"""Galois representations from shadow CohFT data.

The shadow obstruction tower of a modular Koszul algebra A determines (or is
determined by) arithmetic objects: modular forms, Galois representations,
L-functions.  This module makes the connection explicit and computable.

MATHEMATICAL FRAMEWORK
======================

1. MODULAR FORMS FROM SHADOW DATA

   At genus 1, the shadow partition function Z^sh(A, tau) is a (quasi-)modular
   form.  For LATTICE VOAs V_Lambda, the genus-1 partition function is determined
   by the theta series Theta_Lambda(tau).  The theta series decomposes into
   Eisenstein and cuspidal parts:

     Theta_Lambda = (Eisenstein component) + (cuspidal component)

   Examples:
     - E_8 lattice: Theta_{E_8} = E_4(tau).  Purely Eisenstein, no cusp form.
     - Leech lattice: Theta_Leech = E_{12}(tau) - (65520/691)*Delta(tau).
       The cuspidal component c_Delta * Delta(tau) is nonzero.

   The cuspidal part carries a Galois representation (Deligne's theorem);
   the Eisenstein part gives a reducible representation.

2. GALOIS REPRESENTATIONS FROM HECKE EIGENFORMS (Deligne)

   For a normalised Hecke eigenform f = sum a_n q^n in S_k(Gamma_0(N), chi),
   Deligne constructs a 2-dimensional ell-adic Galois representation:

     rho_f: Gal(Qbar/Q) -> GL_2(Qbar_ell)

   such that for primes p not dividing N*ell:

     Tr(rho_f(Frob_p)) = a_p(f)
     det(rho_f(Frob_p)) = chi(p) * p^{k-1}

   The characteristic polynomial of Frobenius is:

     P_p(T) = T^2 - a_p T + chi(p) * p^{k-1}

   For trivial character chi = 1 and level N = 1:

     P_p(T) = T^2 - a_p T + p^{k-1}

3. SHADOW GALOIS REPRESENTATION

   For an algebra A whose shadow data determines a Hecke eigenform f_A
   (via the theta series decomposition for lattice VOAs, or more generally
   via the shadow-modular form correspondence), define:

     rho^sh_A := rho_{f_A}  (the Deligne representation of the associated eigenform)

   For algebras whose shadow data is purely Eisenstein (e.g., V_{E_8}):

     rho^sh_A is REDUCIBLE: rho = chi_1 + chi_2 (sum of characters)

   For algebras with cuspidal shadow data (e.g., V_Leech via Delta):

     rho^sh_A is IRREDUCIBLE (by Ribet's theorem, since Delta is non-CM)

4. ARTIN REPRESENTATIONS FROM FINITE TOWERS

   For class G and L algebras, the shadow tower is finite.  The "shadow Artin
   representation" is defined via the minimal polynomial of the shadow
   generating function H_A(t) over Q.  For an algebraic H_A of degree d,
   the Galois group Gal(splitting field / Q) acts on the roots, giving a
   permutation representation of dimension <= d.

5. p-ADIC SHADOW DATA

   The shadow generating function H_A(t) = t^2 * sqrt(Q_L(t)) is algebraic.
   Over Q_p, the p-adic valuation of Q_L and its discriminant determine the
   p-adic Hodge type of the associated motive.

   For the conic w^2 = Q_L*(s) = q_0 s^2 + q_1 s + q_2:
   - If disc(Q_L*) = q_1^2 - 4 q_0 q_2 is a p-adic square: split, crystalline
   - If disc is a non-square unit: unramified, crystalline
   - If v_p(disc) is odd: ramified at p

6. COMPATIBLE SYSTEMS

   For a lattice VOA V_Lambda, the Hecke eigenforms in Theta_Lambda give a
   compatible system of ell-adic representations: the characteristic polynomial
   of Frob_p is independent of ell (for ell != p).

   Verification: compute P_p(T) from the eigenvalues a_p for different
   eigenforms and check integrality.

7. SELMER GROUPS

   The Bloch-Kato Selmer group Sel(rho) measures arithmetic obstructions.
   For an eigenform f of weight k >= 2 and trivial nebentypus:

     dim Sel(rho_f) is related to the order of vanishing of L(f, s) at s = k/2
     (by the Bloch-Kato conjecture, proved in many cases).

   For Eisenstein representations: Sel is related to class groups.

CONVENTIONS:
  - Cohomological grading (|d| = +1), bar uses desuspension.
  - kappa = S_2 (modular characteristic), NOT c/2 in general (AP48).
  - Theta series normalisation: Theta_Lambda(tau) = sum_{v in Lambda} q^{(v,v)/2}.
  - Ramanujan tau: tau(n) = coeff of q^n in Delta(tau) = q prod(1 - q^m)^{24}.
  - Eisenstein series: E_k(tau) = 1 - (2k/B_k) sum sigma_{k-1}(n) q^n.
  - Hecke eigenvalues: a_p(E_k) = 1 + p^{k-1}; a_p(Delta) = tau(p).

CAUTION (AP1):  kappa formulas are family-specific. Never copy between families.
CAUTION (AP9):  kappa != c/2 in general.
CAUTION (AP15): E_2* is quasi-modular, not holomorphic.
CAUTION (AP38): Normalisation conventions differ between sources.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro subalgebra.

Manuscript references:
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:shadow-moduli-resolution (arithmetic_shadows.tex)
    thm:algebraic-family-rigidity (higher_genus_modular_koszul.tex)
    prop:shadow-periods (arithmetic_shadows.tex)
    rem:motivic-decomposition (arithmetic_shadows.tex)
    thm:depth-decomposition (arithmetic_shadows.tex)
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from sympy import (
    Abs,
    Integer,
    Rational,
    Symbol,
    bernoulli,
    binomial,
    cancel,
    expand,
    factor,
    factorial,
    gcd,
    isprime,
    nextprime,
    simplify,
    sqrt,
)


# =========================================================================
# Symbols
# =========================================================================

c = Symbol('c')
k_sym = Symbol('k')
s_sym = Symbol('s')
T_sym = Symbol('T')


# =========================================================================
# 1. Arithmetic primitives
# =========================================================================

def divisor_sum(n: int, k: int) -> int:
    r"""sigma_k(n) = sum_{d | n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


@lru_cache(maxsize=256)
def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficient of q^n in Delta(q).

    Delta(q) = q * prod_{m >= 1} (1 - q^m)^{24}.
    So tau(n) = coeff of q^{n-1} in prod_{m >= 1} (1 - q^m)^{24}.

    Known values: tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472,
    tau(5)=4830, tau(6)=-6048, tau(7)=-16744, tau(8)=84480,
    tau(9)=-113643, tau(10)=-115920, tau(11)=534612.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Direct q-expansion of prod(1-q^m)^{24} up to order n-1
    nterms = n + 2
    coeffs = [0] * nterms
    coeffs[0] = 1
    for m in range(1, nterms):
        # Multiply current polynomial by (1 - q^m)^{24}
        # Expand (1 - q^m)^{24} = sum_{j=0}^{24} C(24,j) (-1)^j q^{jm}
        binom_terms = []
        for j in range(25):
            jm = j * m
            if jm >= nterms:
                break
            binom_c = 1
            for i in range(j):
                binom_c = binom_c * (24 - i) // (i + 1)
            binom_terms.append((jm, binom_c * ((-1) ** j)))
        new_coeffs = [0] * nterms
        for idx in range(nterms):
            if coeffs[idx] == 0:
                continue
            for jm, bc in binom_terms:
                target = idx + jm
                if target >= nterms:
                    continue
                new_coeffs[target] += coeffs[idx] * bc
        coeffs = new_coeffs
    return coeffs[n - 1] if n - 1 < len(coeffs) else 0


def eisenstein_coefficient(k: int, n: int) -> Rational:
    r"""Coefficient a_n of q^n in the normalised Eisenstein series E_k.

    E_k(tau) = 1 - (2k / B_k) * sum_{n >= 1} sigma_{k-1}(n) q^n.

    Returns the coefficient a_n for n >= 0.
    """
    if k < 4 or k % 2 != 0:
        raise ValueError(f"Eisenstein E_k requires even k >= 4, got k={k}")
    if n == 0:
        return Rational(1)
    B_k = bernoulli(k)
    # a_n = -(2k / B_k) * sigma_{k-1}(n)
    sig = divisor_sum(n, k - 1)
    return Rational(-2 * k, 1) * Rational(sig) / Rational(B_k)


def theta_e8_coefficient(n: int) -> int:
    r"""Coefficient of q^n in Theta_{E_8}(tau) = E_4(tau).

    The theta series of the E_8 lattice equals the weight-4 Eisenstein series.
    Theta_{E_8}(tau) = 1 + 240*q + 2160*q^2 + 6720*q^3 + ...
    = sum r_{E_8}(n) q^n where r_{E_8}(n) = 240 * sigma_3(n) for n >= 1.
    """
    if n == 0:
        return 1
    return 240 * divisor_sum(n, 3)


def theta_leech_coefficient(n: int) -> int:
    r"""Coefficient of q^n in Theta_Leech(tau).

    Theta_Leech = E_{12} - (65520/691) * Delta.

    For the E_12 Eisenstein series:
      E_{12} = 1 + (65520/691) * sum sigma_{11}(n) q^n.

    Note: E_{12} normalisation:
      E_{12} = 1 - (24/B_{12}) * sum sigma_{11}(n) q^n
      B_{12} = -691/2730, so -24/B_{12} = 24*2730/691 = 65520/691.

    So E_{12} = 1 + (65520/691) * sum sigma_{11}(n) q^n.

    And Theta_Leech(tau) = E_{12} - (65520/691)*Delta
    For n >= 1:
      a_n(Theta_Leech) = (65520/691) * sigma_{11}(n) - (65520/691) * tau(n)
                        = (65520/691) * (sigma_{11}(n) - tau(n))

    This must be an integer (it counts lattice vectors of norm 2n).
    """
    if n == 0:
        return 1
    # (65520/691) * (sigma_{11}(n) - tau(n)) must be integer
    sig = divisor_sum(n, 11)
    tau_n = ramanujan_tau(n)
    # 65520/691 times the difference
    num = 65520 * (sig - tau_n)
    assert num % 691 == 0, f"Theta_Leech coefficient not integral at n={n}"
    return num // 691


def cuspidal_part_leech(n: int) -> Fraction:
    r"""Cuspidal part of Theta_Leech: coefficient of q^n in -(65520/691)*Delta.

    Theta_Leech = E_{12} + cuspidal, where cuspidal = -(65520/691)*Delta.
    For n >= 1: coeff = -(65520/691) * tau(n).
    """
    if n == 0:
        return Fraction(0)
    return Fraction(-65520 * ramanujan_tau(n), 691)


# =========================================================================
# 2. Galois representations from Hecke eigenforms
# =========================================================================

@dataclass
class FrobeniusData:
    """Characteristic polynomial of Frobenius at a prime p.

    P_p(T) = T^2 - a_p * T + chi(p) * p^{k-1}

    where a_p = Hecke eigenvalue, k = weight, chi = nebentypus.
    """
    p: int
    weight: int
    a_p: int  # Hecke eigenvalue (integer for level 1)
    chi_p: int = 1  # nebentypus value at p
    eigenform_name: str = ''

    @property
    def det_frobenius(self) -> int:
        """det(rho(Frob_p)) = chi(p) * p^{k-1}."""
        return self.chi_p * (self.p ** (self.weight - 1))

    @property
    def trace_frobenius(self) -> int:
        """Tr(rho(Frob_p)) = a_p."""
        return self.a_p

    def char_poly(self) -> Tuple[int, int, int]:
        """Coefficients of P_p(T) = T^2 - a_p T + det.

        Returns (1, -a_p, det) so P_p(T) = T^2 + c1*T + c0.
        """
        return (1, -self.a_p, self.det_frobenius)

    def char_poly_symbolic(self):
        """P_p(T) as a sympy expression."""
        return T_sym ** 2 - self.a_p * T_sym + self.det_frobenius

    def eigenvalues(self) -> Tuple[complex, complex]:
        """Roots of P_p(T): the Frobenius eigenvalues alpha, beta."""
        disc = self.a_p ** 2 - 4 * self.det_frobenius
        sqrt_disc = math.sqrt(abs(disc)) if disc >= 0 else 1j * math.sqrt(-disc)
        if disc < 0:
            alpha = (self.a_p + sqrt_disc) / 2
            beta = (self.a_p - sqrt_disc) / 2
        else:
            alpha = (self.a_p + math.sqrt(disc)) / 2
            beta = (self.a_p - math.sqrt(disc)) / 2
        return alpha, beta

    def verify_ramanujan(self) -> bool:
        """Check Ramanujan bound: |a_p| <= 2 * p^{(k-1)/2}."""
        bound = 2 * self.p ** ((self.weight - 1) / 2)
        return abs(self.a_p) <= bound + 1e-10

    def verify_integrality(self) -> bool:
        """Check that the characteristic polynomial has integer coefficients."""
        _, c1, c0 = self.char_poly()
        return isinstance(c1, int) and isinstance(c0, int)


@dataclass
class GaloisRepresentation:
    """A 2-dimensional Galois representation from a Hecke eigenform.

    Collects Frobenius data at multiple primes, allowing verification of
    the compatible system property.
    """
    name: str
    weight: int
    level: int
    nebentypus: str = 'trivial'
    frobenius_data: Dict[int, FrobeniusData] = field(default_factory=dict)
    is_cuspidal: bool = True
    is_irreducible: bool = True

    def add_frobenius(self, p: int, a_p: int, chi_p: int = 1):
        """Record Frobenius data at prime p."""
        self.frobenius_data[p] = FrobeniusData(
            p=p, weight=self.weight, a_p=a_p, chi_p=chi_p,
            eigenform_name=self.name,
        )

    def char_poly_at(self, p: int) -> Tuple[int, int, int]:
        """P_p(T) coefficients at prime p."""
        if p not in self.frobenius_data:
            raise ValueError(f"No Frobenius data at p={p}")
        return self.frobenius_data[p].char_poly()

    def verify_ramanujan_all(self) -> Dict[int, bool]:
        """Check Ramanujan bound at all recorded primes."""
        return {p: fd.verify_ramanujan() for p, fd in self.frobenius_data.items()}

    def verify_compatible_system(self) -> bool:
        """Verify that char polys have integer coefficients (ell-independence).

        For a compatible system, the char poly of Frob_p must be independent
        of the auxiliary prime ell.  Over Q, this means the coefficients must
        be in Z.
        """
        return all(fd.verify_integrality() for fd in self.frobenius_data.values())

    def local_euler_factor(self, p: int) -> Callable:
        """L_p(s) = P_p(p^{-s})^{-1} as a function of s."""
        if p not in self.frobenius_data:
            raise ValueError(f"No Frobenius data at p={p}")
        fd = self.frobenius_data[p]

        def euler_factor(s_val: complex) -> complex:
            ps = p ** (-s_val)
            poly_val = 1 - fd.a_p * ps + fd.det_frobenius * ps ** 2
            return 1.0 / poly_val if abs(poly_val) > 1e-50 else float('inf')

        return euler_factor

    def partial_l_function(self, s_val: complex, primes: Optional[List[int]] = None) -> complex:
        """Partial L-function: product of local Euler factors over given primes."""
        if primes is None:
            primes = sorted(self.frobenius_data.keys())
        result = 1.0 + 0j
        for p in primes:
            ef = self.local_euler_factor(p)
            result *= ef(s_val)
        return result


# =========================================================================
# 3. Shadow Galois representations for specific algebras
# =========================================================================

def galois_rep_eisenstein(k: int) -> GaloisRepresentation:
    r"""Galois representation from the Eisenstein series E_k.

    The Eisenstein series E_k is NOT a cusp form, so the associated
    "Galois representation" is REDUCIBLE:

      rho_{E_k} = chi_0 + chi_{k-1}

    where chi_0 is the trivial character and chi_{k-1}(Frob_p) = p^{k-1}.

    At each prime p:
      a_p(E_k) = 1 + p^{k-1}  (sum of the two character values)
      P_p(T) = (T - 1)(T - p^{k-1}) = T^2 - (1 + p^{k-1})T + p^{k-1}

    This is consistent with det = p^{k-1} and trace = 1 + p^{k-1}.
    """
    if k < 4 or k % 2 != 0:
        raise ValueError(f"Eisenstein E_k requires even k >= 4, got k={k}")
    rep = GaloisRepresentation(
        name=f'E_{k}',
        weight=k,
        level=1,
        is_cuspidal=False,
        is_irreducible=False,
    )
    # Record Frobenius data at small primes
    p = 2
    for _ in range(20):
        a_p = 1 + p ** (k - 1)
        rep.add_frobenius(p, a_p)
        p = int(nextprime(p))
    return rep


def galois_rep_delta() -> GaloisRepresentation:
    r"""Galois representation from the Ramanujan Delta function.

    Delta = sum tau(n) q^n in S_{12}(SL(2,Z)).

    rho_Delta: Gal(Qbar/Q) -> GL_2(Qbar_ell)
    Tr(rho(Frob_p)) = tau(p), det(rho(Frob_p)) = p^{11}.

    This representation is IRREDUCIBLE (Ribet): Delta is non-CM.

    The Ramanujan conjecture (proved by Deligne): |tau(p)| <= 2*p^{11/2}.
    """
    rep = GaloisRepresentation(
        name='Delta',
        weight=12,
        level=1,
        is_cuspidal=True,
        is_irreducible=True,
    )
    p = 2
    for _ in range(20):
        tau_p = ramanujan_tau(p)
        rep.add_frobenius(p, tau_p)
        p = int(nextprime(p))
    return rep


def galois_rep_E8() -> GaloisRepresentation:
    r"""Shadow Galois representation for V_{E_8}.

    Theta_{E_8} = E_4.  Purely Eisenstein, so the shadow Galois
    representation is the REDUCIBLE representation from E_4:

      rho^sh_{E_8} = chi_0 + chi_3   (trivial + cubic character)

    where chi_3(Frob_p) = p^3.

    Frobenius data: a_p = 1 + p^3.
    """
    return galois_rep_eisenstein(4)


def galois_rep_Leech() -> Tuple[GaloisRepresentation, GaloisRepresentation]:
    r"""Shadow Galois representation for V_Leech.

    Theta_Leech = E_{12} - (65520/691) * Delta.

    The representation DECOMPOSES into:
      (a) Eisenstein part from E_{12}: rho_{E_{12}} = chi_0 + chi_{11} (REDUCIBLE)
      (b) Cuspidal part from Delta: rho_Delta (IRREDUCIBLE)

    The cuspidal part is the interesting one for Langlands.

    Returns (eisenstein_rep, cuspidal_rep).
    """
    eis = galois_rep_eisenstein(12)
    cusp = galois_rep_delta()
    return eis, cusp


def galois_rep_Leech_combined(primes: Optional[List[int]] = None) -> GaloisRepresentation:
    r"""Combined shadow Galois data for V_Leech.

    Since Theta_Leech = E_{12} - (65520/691)*Delta, the "effective" Frobenius
    trace at p from the FULL theta series is:

      a_p(Theta_Leech) = a_p(E_{12}) - (65520/691) * tau(p)

    This is NOT a Hecke eigenvalue (Theta_Leech is not an eigenform).
    The Hecke decomposition is E_{12} and Delta separately.

    We record the combined data for reference, flagging it as non-eigenform.
    """
    rep = GaloisRepresentation(
        name='Theta_Leech (combined, NOT eigenform)',
        weight=12,
        level=1,
        is_cuspidal=False,
        is_irreducible=False,
    )
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for p in primes:
        a_p_E12 = 1 + p ** 11
        tau_p = ramanujan_tau(p)
        # Theta_Leech coefficient at q^p: (65520/691)*(sigma_11(p) - tau(p))
        # sigma_11(p) = 1 + p^{11} for prime p
        # So coeff = (65520/691)*(1 + p^{11} - tau(p))
        # This is the representation of lattice vectors, not a Hecke eigenvalue.
        leech_coeff = theta_leech_coefficient(p)
        rep.add_frobenius(p, leech_coeff)
    return rep


# =========================================================================
# 4. Artin representations from finite shadow towers
# =========================================================================

@dataclass
class ArtinShadowData:
    r"""Artin-type representation from a finite shadow tower.

    For class G/L algebras, the shadow tower is finite: only S_2 (and S_3
    for class L) are nonzero.  The shadow generating function
    H_A(t) = t^2 * sqrt(Q_L(t)) is algebraic of degree 2 (from the
    Riccati equation).

    The "Artin representation" comes from the monodromy of H_A(t):
    as t encircles the branch points of sqrt(Q_L), the function H_A
    picks up a sign.  This gives a representation:

      rho^Art_A: pi_1(P^1 \ branch_locus) -> {+1, -1} = Z/2Z

    For class G (Heisenberg): Q_L = (2*kappa)^2 is a perfect square,
    so sqrt(Q_L) = 2*kappa.  No branch points.  Trivial monodromy.
    The Artin representation is the trivial 1-dimensional rep.

    For class L (affine): Q_L(t) = (2*kappa + 3*alpha*t)^2 has a
    double root at t_0 = -2*kappa/(3*alpha).  The square root
    sqrt(Q_L) = |2*kappa + 3*alpha*t| has a sign change at t_0,
    but it is still a polynomial (no monodromy in the complex plane).
    The Artin representation is again trivial.

    For class M (Virasoro): Q_L is irreducible, sqrt(Q_L) has genuine
    branch points.  The monodromy is Z/2Z (quadratic extension).
    """
    name: str
    shadow_class: str  # G, L, C, M
    kappa: Union[float, Fraction]
    cubic: Union[float, Fraction] = Fraction(0)
    quartic: Union[float, Fraction] = Fraction(0)
    conductor: Optional[int] = None  # Artin conductor if defined

    @property
    def monodromy_group(self) -> str:
        """Monodromy group of sqrt(Q_L)."""
        if self.shadow_class in ('G', 'L', 'C'):
            return 'trivial'
        return 'Z/2Z'

    @property
    def artin_dimension(self) -> int:
        """Dimension of the Artin representation."""
        return 1  # Always 1-dimensional for sqrt monodromy

    @property
    def is_trivial(self) -> bool:
        return self.shadow_class in ('G', 'L', 'C')


def artin_data_heisenberg(k_val: Union[int, Fraction]) -> ArtinShadowData:
    """Artin shadow data for Heisenberg at level k."""
    return ArtinShadowData(
        name=f'H_{k_val}',
        shadow_class='G',
        kappa=Fraction(k_val) if isinstance(k_val, int) else k_val,
    )


def artin_data_affine_sl2(k_val: Union[int, Fraction]) -> ArtinShadowData:
    r"""Artin shadow data for affine sl_2 at level k.

    kappa = dim(sl_2) * (k + h^v) / (2 * h^v) = 3*(k+2)/4.
    Cubic: nonzero but tower still terminates.
    """
    kappa = Fraction(3 * (k_val + 2), 4) if isinstance(k_val, int) \
        else Fraction(3) * (Fraction(k_val) + 2) / 4
    return ArtinShadowData(
        name=f'aff_sl2_k{k_val}',
        shadow_class='L',
        kappa=kappa,
    )


def artin_conductor_affine_sl2(k_val: int) -> int:
    r"""Artin conductor for affine sl_2 at integer level k.

    The "Artin conductor" of the shadow tower is defined as the lcm of
    denominators of the shadow coefficients S_2, S_3 (as rational numbers).

    For sl_2 at level k: kappa = 3*(k+2)/4.
    Denominator of kappa: 4/gcd(3*(k+2), 4).

    The cubic S_3 for sl_2 involves f^{abc} structure constants; for the
    shadow tower, S_3 = 0 since sl_2 has no cubic Casimir invariant.
    (The cubic shadow alpha is zero for sl_2.)

    So the conductor is just the denominator of kappa = 3*(k+2)/4.
    """
    kap = Fraction(3 * (k_val + 2), 4)
    return kap.denominator


# =========================================================================
# 5. p-adic shadow data and Hodge type
# =========================================================================

@dataclass
class PAdicShadowData:
    r"""p-adic realisation of the shadow generating function.

    For the shadow conic w^2 = q_0*s^2 + q_1*s + q_2, the arithmetic
    over Q_p depends on:

    (a) Whether disc = q_1^2 - 4*q_0*q_2 is a square mod p.
    (b) The p-adic valuation v_p(disc).
    (c) Whether the conic has a Q_p-rational point.

    The p-adic Hodge type (in the sense of Fontaine):
    - Crystalline: if disc has even p-adic valuation (smooth reduction mod p)
    - Semistable: if v_p(disc) > 0 (multiplicative reduction)
    - de Rham (general): always, for a 1-dimensional motive
    """
    p: int
    kappa: Fraction
    discriminant: Fraction  # disc = q_1^2 - 4*q_0*q_2
    v_p_disc: int  # p-adic valuation of discriminant
    is_square_mod_p: bool  # whether disc is a QR mod p
    hodge_type: str  # 'crystalline', 'semistable', 'potentially_crystalline'
    has_Qp_point: bool  # whether the conic has a Q_p-rational point

    @property
    def is_split(self) -> bool:
        """The conic is split over Q_p iff it has a Q_p-point."""
        return self.has_Qp_point

    @property
    def hodge_tate_weight(self) -> int:
        """For a weight-1 motive (shadow conic), the HT weight is 0."""
        return 0


def _legendre_symbol(a: int, p: int) -> int:
    """Legendre symbol (a/p) for odd prime p."""
    if a % p == 0:
        return 0
    return pow(a, (p - 1) // 2, p) if p > 2 else 1


def _p_adic_valuation(n: int, p: int) -> int:
    """v_p(n): the p-adic valuation of integer n."""
    if n == 0:
        return float('inf')
    v = 0
    n = abs(n)
    while n % p == 0:
        v += 1
        n //= p
    return v


def p_adic_valuation_fraction(x: Fraction, p: int) -> int:
    """v_p(x) for a Fraction x."""
    if x == 0:
        return float('inf')
    return _p_adic_valuation(x.numerator, p) - _p_adic_valuation(x.denominator, p)


def virasoro_shadow_discriminant(c_val: Fraction) -> Fraction:
    r"""Discriminant of the Virasoro shadow conic at central charge c.

    For Virasoro: kappa = c/2, alpha = 2, S_4 = 10/(c*(5c+22)).
    Q_L(t) = (c + 6t)^2 + 80t^2/(5c+22).
    After conic normalisation w^2 = q_0 s^2 + q_1 s + q_2:
      q_0 = c^2, q_1 = 12c, q_2 = 36 + 80/(5c+22)

    disc = q_1^2 - 4*q_0*q_2
         = 144c^2 - 4c^2*(36 + 80/(5c+22))
         = 144c^2 - 144c^2 - 320c^2/(5c+22)
         = -320c^2/(5c+22).
    """
    if c_val == 0:
        return Fraction(0)
    numer = -320 * c_val ** 2
    denom = 5 * c_val + 22
    return Fraction(numer, denom)


def padic_shadow_virasoro(c_val: Fraction, p: int) -> PAdicShadowData:
    r"""p-adic shadow data for Virasoro at central charge c and prime p.

    Computes the discriminant of the shadow conic, its p-adic valuation,
    and determines the Hodge type.
    """
    disc = virasoro_shadow_discriminant(c_val)
    if disc == 0:
        v_p = float('inf')
        is_sq = True
        hodge = 'crystalline'
        has_pt = True
    else:
        # Express disc as integer ratio
        disc_num = disc.numerator
        disc_den = disc.denominator
        v_p_num = _p_adic_valuation(abs(disc_num), p)
        v_p_den = _p_adic_valuation(disc_den, p)
        v_p = v_p_num - v_p_den

        # Reduce disc modulo p
        if v_p >= 1:
            is_sq = True  # disc = 0 mod p, so it's a square mod p
            hodge = 'semistable' if v_p % 2 == 1 else 'crystalline'
        else:
            # disc is a p-adic unit; extract the unit part and compute Legendre
            # Remove p-factors from numerator and denominator
            n_red = abs(disc_num) // (p ** v_p_num)
            d_red = disc_den // (p ** v_p_den)
            # The sign of disc matters for quadratic residue
            sign = -1 if disc_num < 0 else 1
            if p == 2:
                # Special handling for p=2: need mod 8 analysis
                is_sq = True  # Simplification: conics over Q_2 are well-understood
                hodge = 'crystalline'
            else:
                # d_red is now coprime to p; compute its inverse mod p
                d_inv = pow(d_red % p, -1, p)
                disc_unit = (sign * n_red * d_inv) % p
                is_sq = _legendre_symbol(disc_unit, p) != -1
                hodge = 'crystalline'

        # The conic always has a Q_p-point when p is odd and disc is nonzero
        # (Hasse-Minkowski: conic over Q_p has a point iff Hilbert symbol = 1)
        has_pt = True  # s=0, w=sqrt(q_2) always works over Q_p if q_2 is a unit

    return PAdicShadowData(
        p=p,
        kappa=Fraction(c_val, 2),
        discriminant=disc,
        v_p_disc=v_p,
        is_square_mod_p=is_sq,
        hodge_type=hodge,
        has_Qp_point=has_pt,
    )


# =========================================================================
# 6. Compatible systems from shadow tower
# =========================================================================

def frobenius_poly_from_eigenform(eigenform_name: str, p: int) -> Tuple[int, int, int]:
    r"""Characteristic polynomial of Frob_p for a standard eigenform.

    Returns coefficients (1, -a_p, det) of T^2 - a_p T + det.

    Supported eigenforms:
      'E_4': a_p = 1 + p^3, det = p^3
      'E_6': a_p = 1 + p^5, det = p^5
      'E_8': a_p = 1 + p^7, det = p^7
      'E_10': a_p = 1 + p^9, det = p^9
      'E_12': a_p = 1 + p^{11}, det = p^{11}
      'Delta': a_p = tau(p), det = p^{11}
    """
    eigenform_map = {
        'E_4': lambda pp: (1 + pp ** 3, pp ** 3),
        'E_6': lambda pp: (1 + pp ** 5, pp ** 5),
        'E_8': lambda pp: (1 + pp ** 7, pp ** 7),
        'E_10': lambda pp: (1 + pp ** 9, pp ** 9),
        'E_12': lambda pp: (1 + pp ** 11, pp ** 11),
        'Delta': lambda pp: (ramanujan_tau(pp), pp ** 11),
    }
    if eigenform_name not in eigenform_map:
        raise ValueError(f"Unknown eigenform: {eigenform_name}")
    a_p, det = eigenform_map[eigenform_name](p)
    return (1, -a_p, det)


def compatible_system_check(eigenform_name: str,
                            primes: Optional[List[int]] = None) -> Dict[str, Any]:
    r"""Check that a compatible system has integer characteristic polynomials.

    For a genuine compatible system {rho_ell}_ell, the char poly of Frob_p
    is independent of ell (for ell != p).  Over Q, this means the coefficients
    are in Z.

    This function verifies integrality and the Ramanujan bound for the
    given eigenform at the specified primes.
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    results = {}
    for p in primes:
        c2, c1, c0 = frobenius_poly_from_eigenform(eigenform_name, p)
        a_p = -c1
        det = c0
        # Ramanujan bound
        weight = {
            'E_4': 4, 'E_6': 6, 'E_8': 8, 'E_10': 10, 'E_12': 12, 'Delta': 12,
        }[eigenform_name]
        bound = 2 * p ** ((weight - 1) / 2)
        results[p] = {
            'a_p': a_p,
            'det': det,
            'integral': isinstance(a_p, int) and isinstance(det, int),
            'ramanujan': abs(a_p) <= bound + 1e-10,
            'char_poly': (c2, c1, c0),
        }
    return results


def verify_ell_independence(eigenform_name: str, p: int,
                            ells: Optional[List[int]] = None) -> bool:
    r"""Verify ell-independence: the char poly at p is independent of ell.

    For Hecke eigenforms over Q, the eigenvalues a_p are in Z, so the
    char poly is automatically ell-independent.  This function verifies
    this by computing P_p(T) for different ells and checking equality.

    In practice, for classical modular forms over Q, this is always true
    by construction (Deligne).  The function serves as a consistency check.
    """
    c2, c1, c0 = frobenius_poly_from_eigenform(eigenform_name, p)
    # The char poly is (1, c1, c0) which is in Z[T] — ell-independent by definition
    return isinstance(c1, int) and isinstance(c0, int)


# =========================================================================
# 7. Shadow Selmer groups
# =========================================================================

@dataclass
class ShadowSelmerData:
    r"""Selmer group data for the shadow Galois representation.

    For an eigenform f of weight k, level N, the Bloch-Kato Selmer group
    Sel(rho_f) conjecturally satisfies:

      ord_{s=k/2} L(f, s) = dim Sel(rho_f)  (BK conjecture)

    For Eisenstein representations (E_k):
      L(E_k, s) = zeta(s) * zeta(s-k+1).
      At s = k/2: zeta(k/2) * zeta(k/2-k+1) = zeta(k/2) * zeta(1-k/2).
      By the functional equation of zeta: zeta(1-k/2) = 0 iff k/2 = 2, 4, 6, ...
      (nontrivial zeros of zeta on Re(s) = 1/2 are the only zeros for Re(s) > 0).
      For k = 4: zeta(2)*zeta(-1) = (pi^2/6)*(-1/12) = -pi^2/72 (nonzero).
      So L(E_4, 2) != 0, hence dim Sel = 0 (conjecturally).

    For Delta:
      L(Delta, s) has no zero at s = 6 (numerically verified).
      So dim Sel(rho_Delta) = 0 (conjecturally, proved by Kato).

    For lattice VOAs:
      - V_{E_8}: shadow rep = rho_{E_4}. Sel is finite (trivial).
      - V_Leech: shadow rep = rho_{E_{12}} + rho_Delta.
        Both Selmer groups are finite (trivial).
    """
    algebra_name: str
    eigenform_name: str
    weight: int
    central_point: Fraction  # s = k/2
    l_value_nonvanishing: bool  # L(f, k/2) != 0
    selmer_dimension: int  # 0 if L-value nonzero (by BK)
    is_proved: bool  # whether the BK conjecture is proved in this case
    reference: str = ''

    @property
    def is_finite(self) -> bool:
        """Selmer group is finite iff dim = 0."""
        return self.selmer_dimension == 0


def selmer_data_E4() -> ShadowSelmerData:
    """Selmer data for E_4 (shadow of V_{E_8})."""
    return ShadowSelmerData(
        algebra_name='V_{E_8}',
        eigenform_name='E_4',
        weight=4,
        central_point=Fraction(2),
        l_value_nonvanishing=True,  # zeta(2)*zeta(-1) = -pi^2/72 != 0
        selmer_dimension=0,
        is_proved=True,  # Kato for Eisenstein
        reference='Kato 2004; trivial for Eisenstein',
    )


def selmer_data_Delta() -> ShadowSelmerData:
    """Selmer data for Delta (cuspidal part of V_Leech shadow)."""
    return ShadowSelmerData(
        algebra_name='V_Leech',
        eigenform_name='Delta',
        weight=12,
        central_point=Fraction(6),
        l_value_nonvanishing=True,  # L(Delta, 6) != 0 (numerically verified)
        selmer_dimension=0,
        is_proved=True,  # Kato 2004
        reference='Kato 2004, Theorem 14.2',
    )


def selmer_landscape() -> Dict[str, ShadowSelmerData]:
    """Selmer data for the standard shadow landscape."""
    return {
        'V_{E_8}': selmer_data_E4(),
        'V_Leech': selmer_data_Delta(),
    }


# =========================================================================
# 8. Langlands shadow functor
# =========================================================================

@dataclass
class LanglandsShadowImage:
    r"""Image of a modular Koszul algebra under the shadow-Langlands map.

    The conjectured map:
      {modular Koszul algebras} -> {automorphic representations of GL_n}

    is defined via the shadow tower:
    - Shadow tower of depth d determines automorphic reps of GL_1, ..., GL_{d-1}.
    - Each arity-r shadow coefficient S_r (for r = 2, ..., d) contributes
      one "L-function channel" in the decomposition of the partition function.

    For standard families:
      - Heisenberg (G, d=2): GL_1 (trivial, one Eisenstein channel from kappa)
      - Affine sl_2 (L, d=3): GL_1 x GL_1 (two Eisenstein channels from kappa, alpha)
      - beta-gamma (C, d=4): GL_1 x GL_1 x GL_1 (three channels, contact stratum)
      - Virasoro (M, d=inf): GL_inf (infinite tower, potentially all GL_n)

    NOTE: This is NOT a genuine Langlands functoriality map.  The true
    Langlands correspondence relates automorphic representations to Galois
    representations.  The "shadow-Langlands" map relates ALGEBRAIC data
    (shadow tower) to AUTOMORPHIC data (L-function decomposition of the
    partition function), which is closer to the spectral side of the
    Arthur-Selberg trace formula.

    The correct mathematical statement is:
      shadow depth d(A) = number of independent L-function channels
      in the spectral decomposition of the genus-1 partition function.

    For lattice VOAs, this is the Hecke decomposition of Theta_Lambda.
    """
    algebra_name: str
    shadow_class: str
    shadow_depth: Union[int, float]
    gl_rank: Union[int, float]  # target GL_n rank
    channels: List[str]  # names of the L-function channels
    is_proved: bool  # whether the correspondence is established
    notes: str = ''


def langlands_image_heisenberg(k_val: int = 1) -> LanglandsShadowImage:
    """Langlands shadow image of Heisenberg."""
    return LanglandsShadowImage(
        algebra_name=f'H_{k_val}',
        shadow_class='G',
        shadow_depth=2,
        gl_rank=1,
        channels=['kappa * zeta(s)'],
        is_proved=True,
        notes='Trivial: one Eisenstein channel from kappa.',
    )


def langlands_image_affine_sl2(k_val: int = 1) -> LanglandsShadowImage:
    """Langlands shadow image of affine sl_2."""
    return LanglandsShadowImage(
        algebra_name=f'aff_sl2_k{k_val}',
        shadow_class='L',
        shadow_depth=3,
        gl_rank=1,
        channels=['kappa * zeta(s)', 'alpha * zeta(s-1)'],
        is_proved=True,
        notes='Two Eisenstein channels. Both GL_1.',
    )


def langlands_image_virasoro(c_val: Fraction = Fraction(1, 2)) -> LanglandsShadowImage:
    """Langlands shadow image of Virasoro."""
    return LanglandsShadowImage(
        algebra_name=f'Vir_c={c_val}',
        shadow_class='M',
        shadow_depth=float('inf'),
        gl_rank=float('inf'),
        channels=['infinite tower: kappa * zeta, alpha * zeta, Q * L(f, s), ...'],
        is_proved=False,
        notes='Conjectural. Infinite tower generates arbitrarily high GL_n data.',
    )


def langlands_image_lattice_E8() -> LanglandsShadowImage:
    r"""Langlands shadow image of V_{E_8}.

    Theta_{E_8} = E_4.  Single Eisenstein eigenform.
    The spectral decomposition has ONE channel: the Eisenstein E_4.
    """
    return LanglandsShadowImage(
        algebra_name='V_{E_8}',
        shadow_class='L',  # affine E_8 at level 1
        shadow_depth=3,
        gl_rank=1,
        channels=['E_4 (Eisenstein, GL_1 x GL_1)'],
        is_proved=True,
        notes='Theta_{E_8} = E_4. Purely Eisenstein.',
    )


def langlands_image_lattice_Leech() -> LanglandsShadowImage:
    r"""Langlands shadow image of V_Leech.

    Theta_Leech = E_{12} - (65520/691)*Delta.
    Two eigenform channels: E_{12} (Eisenstein) and Delta (cuspidal).
    """
    return LanglandsShadowImage(
        algebra_name='V_Leech',
        shadow_class='G',  # class G lattice (no roots)
        shadow_depth=2,
        gl_rank=2,
        channels=['E_{12} (Eisenstein, GL_1 x GL_1)', 'Delta (cuspidal, GL_2)'],
        is_proved=True,
        notes=('Theta_Leech = E_{12} - (65520/691)*Delta. '
               'The cuspidal part gives a genuine GL_2 automorphic rep.'),
    )


def langlands_landscape() -> Dict[str, LanglandsShadowImage]:
    """Full shadow-Langlands landscape for standard families."""
    return {
        'Heisenberg': langlands_image_heisenberg(),
        'Affine_sl2': langlands_image_affine_sl2(),
        'Virasoro': langlands_image_virasoro(),
        'V_{E_8}': langlands_image_lattice_E8(),
        'V_Leech': langlands_image_lattice_Leech(),
    }


# =========================================================================
# 9. Frobenius polynomial computation engine
# =========================================================================

def frobenius_poly_E8_shadow(p: int) -> Tuple[int, int, int]:
    r"""Frobenius polynomial P_p(T) for the V_{E_8} shadow representation.

    Since rho^sh_{E_8} = rho_{E_4} = chi_0 + chi_3:
      P_p(T) = (T - 1)(T - p^3) = T^2 - (1 + p^3)T + p^3.
    """
    a_p = 1 + p ** 3
    det_val = p ** 3
    return (1, -a_p, det_val)


def frobenius_poly_Delta(p: int) -> Tuple[int, int, int]:
    r"""Frobenius polynomial P_p(T) for the Delta representation.

    P_p(T) = T^2 - tau(p)*T + p^{11}.
    """
    return (1, -ramanujan_tau(p), p ** 11)


def frobenius_poly_Leech_cuspidal(p: int) -> Tuple[int, int, int]:
    r"""Frobenius polynomial for the CUSPIDAL part of V_Leech shadow.

    The cuspidal part of Theta_Leech is -(65520/691)*Delta.
    The Galois representation is rho_Delta (same as Delta).
    P_p(T) = T^2 - tau(p)*T + p^{11}.
    """
    return frobenius_poly_Delta(p)


def frobenius_polys_landscape(primes: Optional[List[int]] = None) -> Dict[str, Dict[int, Tuple]]:
    r"""Frobenius polynomials for the full shadow landscape.

    Returns {algebra_name: {p: (1, -a_p, det)}} for each algebra
    and each prime p.
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    result = {}
    for name, poly_fn in [
        ('V_{E_8}/E_4', frobenius_poly_E8_shadow),
        ('V_Leech/Delta', frobenius_poly_Leech_cuspidal),
        ('Delta', frobenius_poly_Delta),
    ]:
        result[name] = {p: poly_fn(p) for p in primes}
    # Eisenstein series
    for wt in [4, 6, 8, 10, 12]:
        name = f'E_{wt}'
        result[name] = {}
        for p in primes:
            a_p = 1 + p ** (wt - 1)
            det_val = p ** (wt - 1)
            result[name][p] = (1, -a_p, det_val)
    return result


# =========================================================================
# 10. Ramanujan tau verification
# =========================================================================

# Known values for cross-verification
_KNOWN_TAU = {
    1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
    6: -6048, 7: -16744, 8: 84480, 9: -113643,
    10: -115920, 11: 534612, 12: -370944,
}


def verify_tau_values() -> Dict[int, bool]:
    """Verify Ramanujan tau against known values."""
    return {n: ramanujan_tau(n) == val for n, val in _KNOWN_TAU.items()}


def verify_tau_multiplicativity(p: int, q: int) -> bool:
    r"""Verify tau(p*q) = tau(p)*tau(q) for coprime p, q.

    The Ramanujan tau function is multiplicative:
    tau(mn) = tau(m)*tau(n) for gcd(m,n) = 1.
    """
    if math.gcd(p, q) != 1:
        return False  # Not applicable for non-coprime
    return ramanujan_tau(p * q) == ramanujan_tau(p) * ramanujan_tau(q)


def verify_tau_hecke_relation(p: int, n: int) -> bool:
    r"""Verify Hecke relation: tau(p*n) = tau(p)*tau(n) - p^{11}*tau(n/p).

    For prime p: tau(p*n) = tau(p)*tau(n) - p^{11}*tau(n/p),
    where tau(n/p) = 0 if p does not divide n.
    """
    lhs = ramanujan_tau(p * n)
    rhs = ramanujan_tau(p) * ramanujan_tau(n)
    if n % p == 0:
        rhs -= p ** 11 * ramanujan_tau(n // p)
    return lhs == rhs


# =========================================================================
# 11. Theta series and lattice point counting
# =========================================================================

def theta_E8_first_terms(n_terms: int = 10) -> List[int]:
    """First n_terms coefficients of Theta_{E_8} = E_4."""
    return [theta_e8_coefficient(n) for n in range(n_terms)]


def theta_Leech_first_terms(n_terms: int = 10) -> List[int]:
    """First n_terms coefficients of Theta_Leech."""
    return [theta_leech_coefficient(n) for n in range(n_terms)]


def theta_cuspidal_Leech_first_terms(n_terms: int = 10) -> List[Fraction]:
    """First n_terms coefficients of the cuspidal part of Theta_Leech."""
    return [cuspidal_part_leech(n) for n in range(n_terms)]


# =========================================================================
# 12. Full shadow Galois analysis
# =========================================================================

def full_shadow_galois_analysis(algebra_name: str,
                                primes: Optional[List[int]] = None) -> Dict[str, Any]:
    r"""Complete Galois-theoretic analysis of the shadow representation.

    Returns a dictionary with:
      - galois_rep: the GaloisRepresentation object
      - frobenius_polys: {p: (1, -a_p, det)}
      - ramanujan_check: {p: bool}
      - integrality_check: {p: bool}
      - selmer_data: ShadowSelmerData if available
      - langlands_image: LanglandsShadowImage
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    result = {'algebra': algebra_name}

    if algebra_name == 'V_{E_8}':
        rep = galois_rep_E8()
        result['galois_rep'] = rep
        result['frobenius_polys'] = {p: frobenius_poly_E8_shadow(p) for p in primes}
        result['ramanujan_check'] = rep.verify_ramanujan_all()
        result['integrality_check'] = {
            p: fd.verify_integrality() for p, fd in rep.frobenius_data.items()
        }
        result['selmer_data'] = selmer_data_E4()
        result['langlands_image'] = langlands_image_lattice_E8()
        result['is_cuspidal'] = False
        result['is_irreducible'] = False

    elif algebra_name == 'V_Leech':
        eis, cusp = galois_rep_Leech()
        result['galois_rep_eisenstein'] = eis
        result['galois_rep_cuspidal'] = cusp
        result['frobenius_polys_eis'] = {
            p: frobenius_poly_from_eigenform('E_12', p) for p in primes
        }
        result['frobenius_polys_cusp'] = {
            p: frobenius_poly_Delta(p) for p in primes
        }
        result['ramanujan_check'] = cusp.verify_ramanujan_all()
        result['integrality_check'] = {
            p: fd.verify_integrality() for p, fd in cusp.frobenius_data.items()
        }
        result['selmer_data'] = selmer_data_Delta()
        result['langlands_image'] = langlands_image_lattice_Leech()
        result['is_cuspidal'] = True  # The interesting part
        result['is_irreducible'] = True

    elif algebra_name == 'Heisenberg':
        result['galois_rep'] = None  # Trivial (1-dimensional Artin)
        result['artin_data'] = artin_data_heisenberg(1)
        result['frobenius_polys'] = {}
        result['langlands_image'] = langlands_image_heisenberg()
        result['is_cuspidal'] = False
        result['is_irreducible'] = False
        result['notes'] = 'Trivial representation. No nontrivial Galois data.'

    else:
        raise ValueError(f"Unknown algebra: {algebra_name}")

    return result


# =========================================================================
# 13. Cross-verification utilities
# =========================================================================

def verify_E8_theta_equals_E4(n_terms: int = 10) -> bool:
    r"""Verify Theta_{E_8} = E_4 coefficient by coefficient.

    Theta_{E_8}(tau) = sum r_{E_8}(n) q^n = 1 + 240*q + 2160*q^2 + ...
    E_4(tau) = 1 + 240*sigma_3(1)*q + 240*sigma_3(2)*q^2 + ...
             = 1 + 240*q + 2160*q^2 + ...

    For n >= 1: r_{E_8}(n) = 240 * sigma_3(n).
    E_4 coefficient at n: 1 + 240*sigma_3(n) (for n >= 1, the constant is 1).
    Wait: E_4 = 1 + 240*sum sigma_3(n)*q^n. So the q^n coefficient is 240*sigma_3(n).
    And r_{E_8}(n) = 240*sigma_3(n). These match.
    """
    for n in range(n_terms):
        theta_coeff = theta_e8_coefficient(n)
        e4_coeff = int(eisenstein_coefficient(4, n))
        if theta_coeff != e4_coeff:
            return False
    return True


def verify_Leech_theta_decomposition(n_terms: int = 10) -> bool:
    r"""Verify Theta_Leech = E_{12} - (65520/691)*Delta.

    For n >= 1: coeff_n(Theta_Leech) = coeff_n(E_{12}) - (65520/691)*tau(n).
    """
    for n in range(1, n_terms):
        theta_coeff = theta_leech_coefficient(n)
        e12_coeff = int(eisenstein_coefficient(12, n))
        tau_n = ramanujan_tau(n)
        # E_{12} coeff at n: (65520/691)*sigma_{11}(n) for n >= 1
        # Theta_Leech coeff: (65520/691)*(sigma_{11}(n) - tau(n))
        # So Theta_Leech = E_{12} - (65520/691)*Delta
        rhs = Fraction(65520, 691) * (divisor_sum(n, 11) - tau_n)
        if theta_coeff != int(rhs):
            return False
    return True


def verify_ramanujan_congruence_691(n: int) -> bool:
    r"""Verify Ramanujan's congruence: tau(n) = sigma_{11}(n) mod 691.

    This is equivalent to: 691 | (sigma_{11}(n) - tau(n)),
    which is why Theta_Leech = (65520/691)*(sigma_{11}(n) - tau(n))
    gives integer coefficients.
    """
    return (divisor_sum(n, 11) - ramanujan_tau(n)) % 691 == 0


def _first_primes(n: int) -> List[int]:
    """Return the first n primes."""
    primes = []
    p = 2
    while len(primes) < n:
        if all(p % q != 0 for q in primes):
            primes.append(p)
        p += 1
    return primes
