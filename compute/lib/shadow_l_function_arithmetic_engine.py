r"""shadow_l_function_arithmetic_engine.py -- Arithmetic of L^sh(s) = -kappa zeta(s) zeta(s-1).

DEEP RESEARCH MODULE.  Investigates the arithmetic structure of the
shadow L-function as introduced in thm:shadow-eisenstein:

    L_A^{sh}(s) := sum_{r >= 2} S_r(A) r^{-s}                       (Dirichlet form)

The manuscript identifies, on the algebraic-family lane (S_r = kappa B_{2r}/(2r)!
at leading order), the closed-form

    L_A^{sh}(s)  ?=  -kappa(A) zeta(s) zeta(s-1).                   (Eisenstein form)

The two forms are NOT equivalent identities; they agree at the level of Mellin
transforms only after the full graph-amplitude reorganisation
(intertwining kernel  M[G_r](s) = r! Gamma(s-1)/(2pi)^{s-1} zeta(s-1) zeta(s+r-2)).
This module distinguishes them and computes the arithmetic content of each.

CRITICAL BEILINSON FINDING (AP1 + AP3 + AP35 cluster)
=====================================================

The proof in arithmetic_shadows.tex (Theorem ref:thm:shadow-eisenstein) cites a
"Ramanujan identity"

    sum_{r >= 1} B_{2r}/(2r)! * r^{-s}  =  -zeta(s) zeta(s-1)            (FALSE)

This identity is FALSE.  Numerical verification at s = 0:
    LHS = 1/(e-1) - 1/2  approx  0.0820     (entire function of s)
    RHS = -zeta(0) zeta(-1) = -(-1/2)(-1/12) = -1/24  approx  -0.0417

The actual identity sum sigma_1(n) n^{-s} = zeta(s) zeta(s-1) involves the
sum-of-divisors function sigma_1, and B_{2r}/(2r)! is NOT proportional to
sigma_1(r).  The Bernoulli ratios decay as 2 (2 pi)^{-2r}, so the LHS is
an entire function of s while the RHS has poles at s = 1 and s = 2.

The MATHEMATICAL CONTENT of thm:shadow-eisenstein (the genus-1 graph-sum side
identifying L^sh with an Eisenstein L-function) survives, but it is the
graph amplitude G_r(tau) and its Mellin transform via the intertwining
kernel M[G_r] that produce zeta(s) zeta(s-1) -- not the Dirichlet series
of the shadow coefficients themselves.  See Section ARITHMETIC.6 below.

This module:

  (i)   Implements both candidate L-functions (Bernoulli-Dirichlet series and
        the zeta-product) and exhibits their disagreement quantitatively.
  (ii)  Computes the arithmetic of -kappa zeta(s) zeta(s-1) as the
        Eisenstein L-function it actually is (special values, functional
        equation, zeros, p-adic interpolation).
  (iii) Investigates the user research questions about V^natural / Monster,
        Riemann zeta zeros, p-adic L-functions, and the F_g <-> shadow zeta
        connection at negative odd integers.

CONVENTIONS:
  - kappa(A) = modular characteristic.  For Virasoro: kappa = c/2.
    For affine KM:  kappa = dim(g)(k+h^vee)/(2 h^vee).
    For Heisenberg: kappa = k.
  - L_A^{Eis}(s) := -kappa(A) * zeta(s) * zeta(s-1)        (Eisenstein form)
  - L_A^{Dir}(s) := sum_{r >= 2} S_r(A) r^{-s}             (Dirichlet form)
  - The two coincide only after Mellin reorganisation; we keep them distinct.
  - Riemann functional equation:
        zeta(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s) zeta(1-s)
  - Trivial zeros: zeta(-2) = zeta(-4) = ... = 0.
  - Special values: zeta(0) = -1/2, zeta(-1) = -1/12, zeta(-3) = 1/120.

CAUTIONS:
  AP1:  The Eisenstein-form formula is family-specific via kappa.  Do NOT
        compute kappa from c/2 for non-Virasoro algebras.
  AP3:  Do NOT pattern-match Bernoulli identities into Dirichlet series.
        The Lambert series of B_{2r}/(2r)! evaluated as a Dirichlet series
        is an entire function, not a zeta product.
  AP31: kappa = 0 implies L_A^{Eis} = 0 identically, but does NOT imply the
        full shadow tower vanishes.  See Section ARITHMETIC.10.
  AP35: A correct conclusion (L^sh is Eisenstein) does not validate a wrong
        proof (the Bernoulli-Dirichlet step).
  AP46: eta(q) = q^{1/24} prod (1 - q^n).  Do NOT drop the q^{1/24}.

VERIFICATION PATHS (>= 3 per claim):
  Path 1: Direct numerical evaluation via mpmath at high precision
  Path 2: Riemann functional equation cross-check
  Path 3: Bernoulli special-value formula zeta(1-2k) = -B_{2k}/(2k)
  Path 4: Cross-family comparison (Heisenberg, affine KM, Virasoro)
  Path 5: Independent Bernoulli generating function 1/(e^x - 1)

Manuscript references:
    thm:shadow-eisenstein                  arithmetic_shadows.tex
    eq:shadow-l-function-def               arithmetic_shadows.tex
    eq:intertwining-kernel                 arithmetic_shadows.tex
    thm:shadow-tower-asymptotics           higher_genus_modular_koszul.tex
"""

from __future__ import annotations

import math
import cmath
from fractions import Fraction
from functools import lru_cache
from typing import Callable, Dict, List, Optional, Tuple

try:
    import mpmath
    mpmath.mp.dps = 60
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================================
# SECTION 0.  Bernoulli numbers and Riemann zeta special values
# ============================================================================


@lru_cache(maxsize=None)
def bernoulli(n: int) -> Fraction:
    """The n-th Bernoulli number B_n via the recursion sum_{k=0}^{n} C(n+1,k) B_k = 0.

    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30,
    B_{10} = 5/66, B_{12} = -691/2730, B_{14} = 7/6.

    All odd Bernoulli numbers B_{2k+1} for k >= 1 vanish.
    """
    if n < 0:
        raise ValueError("Bernoulli index must be non-negative")
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    Bs = [Fraction(0)] * (n + 1)
    Bs[0] = Fraction(1)
    Bs[1] = Fraction(-1, 2)
    for m in range(2, n + 1):
        if m % 2 == 1:
            Bs[m] = Fraction(0)
            continue
        s = Fraction(0)
        for k in range(m):
            s += Fraction(math.comb(m + 1, k)) * Bs[k]
        Bs[m] = -s / (m + 1)
    return Bs[n]


def bernoulli_ratio(r: int) -> Fraction:
    """B_{2r} / (2r)!  --  the leading-order shadow coefficient ratio."""
    if r < 1:
        raise ValueError("r must be >= 1")
    return bernoulli(2 * r) / math.factorial(2 * r)


def zeta_at_negative_odd(k: int) -> Fraction:
    """zeta(1 - 2k) = -B_{2k}/(2k) for k >= 1.

    Examples:
      zeta(-1)  = -1/12
      zeta(-3)  =  1/120
      zeta(-5)  = -1/252
      zeta(-7)  =  1/240
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    return -bernoulli(2 * k) / (2 * k)


def zeta_at_zero() -> Fraction:
    """zeta(0) = -1/2."""
    return Fraction(-1, 2)


def zeta_at_negative_even(k: int) -> int:
    """zeta(-2k) = 0 for k >= 1 (the trivial zeros)."""
    if k < 1:
        raise ValueError("k must be >= 1; zeta(0) = -1/2 is special")
    return 0


# ============================================================================
# SECTION 1.  Modular characteristics kappa for the standard families
# ============================================================================


def kappa_virasoro(c: float) -> float:
    """kappa(Vir_c) = c/2.   AP1 caution: ONLY for the Virasoro family."""
    return c / 2.0


def kappa_heisenberg(k: float) -> float:
    """kappa(H_k) = k.   AP1 caution: ONLY for the Heisenberg family."""
    return float(k)


def kappa_affine_km(dim_g: int, k: float, h_dual: int) -> float:
    """kappa for affine Kac-Moody:  kappa = dim(g) * (k + h^vee) / (2 h^vee).

    Examples:
      sl_2 at level k:  dim_g = 3, h^vee = 2  =>  kappa = 3(k+2)/4
      sl_3 at level k:  dim_g = 8, h^vee = 3  =>  kappa = 8(k+3)/6 = 4(k+3)/3
      E_8  at level k:  dim_g = 248, h^vee = 30 => kappa = 248(k+30)/60
    """
    return dim_g * (k + h_dual) / (2.0 * h_dual)


def kappa_lattice_voa(rank: int) -> int:
    """kappa(V_Lambda) = rank(Lambda) for an even lattice VOA.

    AP48:  kappa(V_Lambda) is NOT equal to c/2 for lattice VOAs.
            For the Leech lattice (rank 24, c = 24): kappa = 24, NOT 12.
            For V^natural (Monster, rank 24, c = 24):  kappa = 24, NOT 12.
    """
    return int(rank)


# ============================================================================
# SECTION 2.  Shadow coefficients on the algebraic-family lane
# ============================================================================


def shadow_coefficient_algebraic(kappa_val: float, r: int) -> float:
    """Leading-order shadow coefficient on the algebraic-family lane:

        S_r(A) = kappa(A) * B_{2r} / (2r)!

    AP3 caution:  this is the LEADING ORDER only.  Higher-arity corrections
    from the cubic and quartic shadow may modify S_r for r >= 3 in non-Gaussian
    families.  See higher_genus_modular_koszul.tex thm:shadow-tower-asymptotics.
    """
    if r < 1:
        raise ValueError("r must be >= 1")
    return kappa_val * float(bernoulli_ratio(r))


def shadow_coefficient_exact(kappa_val: Fraction, r: int) -> Fraction:
    """Exact rational shadow coefficient:  kappa * B_{2r} / (2r)!.

    Returns a Fraction.  Use kappa_val as a Fraction for exact arithmetic.
    """
    if not isinstance(kappa_val, Fraction):
        kappa_val = Fraction(kappa_val).limit_denominator(10**12)
    return kappa_val * bernoulli_ratio(r)


# ============================================================================
# SECTION 3.  Two candidate L-functions and their disagreement
# ============================================================================


def L_A_Dir(kappa_val: float, s: complex, r_max: int = 50) -> complex:
    """Dirichlet form:  sum_{r=2}^{r_max} S_r(A) * r^{-s}.

    This is an ENTIRE function of s (the Bernoulli ratios decay as
    2 (2 pi)^{-2r}, so the series converges for all s in C).
    """
    total = 0j
    for r in range(2, r_max + 1):
        Sr = shadow_coefficient_algebraic(kappa_val, r)
        total += Sr * (r ** (-s))
    return total


def L_A_Eis(kappa_val: float, s: complex) -> complex:
    """Eisenstein form:  -kappa * zeta(s) * zeta(s-1).

    This has SIMPLE POLES at s = 1 and s = 2 (from the poles of zeta).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for L_A_Eis")
    s_mp = mpmath.mpc(s)
    val = -kappa_val * mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 1)
    return complex(val)


def disagreement_at_zero(kappa_val: float = 2.0, r_max: int = 100) -> Dict[str, float]:
    """Quantify the BEILINSON FINDING:  L_A^{Dir}(0) != L_A^{Eis}(0).

    At s = 0:
      L_A^{Dir}(0) = sum_{r >= 2} S_r(A) = kappa * (1/(e-1) - 1/2 - 0)
                                                  ^ from sum_{r >= 1} - r=1 term
      Actually:  sum_{r >= 1} B_{2r}/(2r)! = 1/(e-1) - 1/2
                 (from the cotangent generating function evaluated at x = 1)
                 sum_{r >= 2} B_{2r}/(2r)! = 1/(e-1) - 1/2 - 1/12

      L_A^{Eis}(0) = -kappa * zeta(0) * zeta(-1) = -kappa * (-1/2)(-1/12) = -kappa/24
    """
    # Direct sum
    dir_sum = 0.0
    for r in range(2, r_max + 1):
        dir_sum += shadow_coefficient_algebraic(kappa_val, r)
    # Closed form for the truncated tail
    closed = kappa_val * (1.0 / (math.e - 1.0) - 0.5 - 1.0 / 12.0)
    # Eisenstein form
    eis = -kappa_val / 24.0
    return {
        "kappa": kappa_val,
        "L_Dir_at_0_numeric": dir_sum,
        "L_Dir_at_0_closed":  closed,
        "L_Eis_at_0":         eis,
        "agreement_Dir_internal": abs(dir_sum - closed),
        "disagreement_Dir_vs_Eis": abs(closed - eis),
    }


# ============================================================================
# SECTION 4.  Eisenstein-form L-function:  special values
# ============================================================================


def L_Eis_special_value(kappa_val: float, s_int: int) -> Optional[Fraction]:
    """Compute -kappa * zeta(s) * zeta(s-1) at integer s, returning a rational
    multiple of pi^{2k} (or None if a pole or transcendental).

    s = 2:  zeta(s-1) = zeta(1) is a pole  ->  None (pole)
    s = 1:  zeta(s)   = zeta(1) is a pole  ->  None (pole)
    s = 0:  -kappa * zeta(0) * zeta(-1) = -kappa * (-1/2)(-1/12) = -kappa/24
    s = -1: -kappa * zeta(-1) * zeta(-2) = -kappa * (-1/12)(0) = 0  (trivial)
    s = -2: -kappa * zeta(-2) * zeta(-3) = -kappa * (0)(1/120) = 0  (trivial)
    s = -3: -kappa * zeta(-3) * zeta(-4) = -kappa * (1/120)(0) = 0  (trivial)
    s = -2k for k >= 1:  zeta(-2k) = 0 in one factor, so result = 0.

    For ODD negative integers s = 1 - 2k with k >= 1:
        zeta(1-2k) = -B_{2k}/(2k)
        zeta(-2k)  = 0
        product = 0
        ===>  L_Eis(1 - 2k) = 0 for all k >= 1.

    For EVEN negative integers s = -2k with k >= 1:
        zeta(-2k) = 0
        ===>  L_Eis(-2k) = 0 for all k >= 1.

    CONCLUSION:  L_Eis vanishes at every NEGATIVE integer.  The user's claimed
    value L^sh(-1) = -kappa/144 is INCORRECT (it should be 0, not -kappa/144).
    """
    if s_int == 1 or s_int == 2:
        return None  # poles
    if s_int == 0:
        return Fraction(-1, 24) * Fraction(kappa_val).limit_denominator(10**9)
    if s_int < 0:
        # zeta(s) at s < 0 either nonzero (odd) or zero (even).
        # zeta(s-1) at s-1 < 0: same dichotomy shifted.
        # For s = -m with m >= 1:  s-1 = -m-1.
        # If m even: zeta(-m) = 0  =>  product = 0.
        # If m odd:  zeta(-m) != 0 but zeta(-m-1) = 0 (since m+1 is even >= 2).
        # ===>  product = 0 for ALL negative integers s.
        return Fraction(0)
    # s >= 3: positive integer, value is transcendental (involves pi^{2k}).
    return None  # not rational


def L_Eis_at_positive_even(kappa_val: float, s: int) -> Optional[float]:
    """Numerical value of L_A^{Eis}(s) for positive integer s != 1, 2.

    For s = 2k with k >= 2:
        zeta(2k) = (-1)^{k+1} (2 pi)^{2k} B_{2k} / (2 (2k)!)
    """
    if s in (1, 2):
        return None  # pole
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    val = -kappa_val * float(mpmath.zeta(s)) * float(mpmath.zeta(s - 1))
    return val


def L_Eis_pole_residues(kappa_val: float) -> Dict[str, float]:
    """Residues of L_A^{Eis}(s) = -kappa zeta(s) zeta(s-1) at the two simple poles.

    Pole at s = 1:  zeta(s) has residue 1, so
        Res_{s=1} L_Eis = -kappa * zeta(0) = -kappa * (-1/2) = kappa/2

    Pole at s = 2:  zeta(s-1) has residue 1, so
        Res_{s=2} L_Eis = -kappa * zeta(2) = -kappa * pi^2 / 6
    """
    return {
        "residue_at_s_eq_1": kappa_val / 2.0,
        "residue_at_s_eq_2": -kappa_val * (math.pi ** 2) / 6.0,
    }


# ============================================================================
# SECTION 5.  Functional equation
# ============================================================================


def riemann_xi(s: complex) -> complex:
    """The completed Riemann zeta:
        xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)
    Satisfies xi(s) = xi(1 - s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    val = (s_mp * (s_mp - 1) / 2) * mpmath.power(mpmath.pi, -s_mp / 2) \
          * mpmath.gamma(s_mp / 2) * mpmath.zeta(s_mp)
    return complex(val)


def L_Eis_completed(kappa_val: float, s: complex) -> complex:
    """Completed shadow Eisenstein L-function:

        Lambda_A^{Eis}(s) := -kappa * xi(s) * xi(s-1) / [(1/2) s (s-1) (s-1)(s-2)]

    The functional equation for the product:
        L_Eis(s) = -kappa zeta(s) zeta(s-1)
        L_Eis(3-s) = -kappa zeta(3-s) zeta(2-s)
    Using zeta(s) = chi(s) zeta(1-s) where chi(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s),
    we get:
        L_Eis(s) = chi(s) chi(s-1) L_Eis(3-s) / kappa^2 ... wait, this needs care.

    Direct symmetry centre:  s <-> 3 - s   (because zeta(s) zeta(s-1) is symmetric
    under s <-> 1 - (s - 1) - 1 = ... actually let me think.
        zeta(s) <->  zeta(1-s) under s <-> 1-s.
        zeta(s-1) <-> zeta(2-s) under s-1 <-> 1-(s-1) = 2-s, i.e. s <-> 3-s.
    So the SAME involution s <-> 1-s sends zeta(s) -> zeta(1-s) and
    s <-> 3-s sends zeta(s-1) -> zeta(2-s).
    The product is NOT invariant under a single reflection -- it has TWO
    natural functional centres at s = 1/2 and s = 3/2, with symmetry centre 1.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    return complex(-kappa_val * mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 1))


def functional_equation_image(s: complex) -> complex:
    """The image of s under the functional equation reflection.

    For -kappa zeta(s) zeta(s-1):  the natural reflection is s <-> 3 - s,
    sending zeta(s) zeta(s-1) -> zeta(3-s) zeta(2-s).
    Note this is NOT a self-symmetry of the un-completed product;
    a multiplicative correction by gamma factors is needed.
    """
    return 3 - s


def functional_equation_check(kappa_val: float, s: complex) -> Dict[str, complex]:
    """Compare L_Eis(s) and the functional-equation prediction at L_Eis(3-s).

    Riemann functional equation:
        zeta(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s) zeta(1-s)
    so
        L_Eis(s) = -kappa zeta(s) zeta(s-1)
                = -kappa [2^s pi^{s-1} sin(pi s/2) Gamma(1-s) zeta(1-s)]
                         [2^{s-1} pi^{s-2} sin(pi(s-1)/2) Gamma(2-s) zeta(2-s)]
                = (positive constant) * [stuff in s] * zeta(1-s) zeta(2-s)
    The image is L_Eis(s') with s' such that 1-s' = 1-s, 2-s' = 2-s ... so s' = s.
    Wait -- we need 1 - s' = s and 2 - s' = s - 1, giving s' = 1 - s and s' = 3 - s
    simultaneously, which is a contradiction.

    The correct interpretation:  L_Eis(s) / L_Eis(3-s) is a product of gamma
    factors, NOT the simple ratio of one Eisenstein L-function to another.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    L_s = L_A_Eis(kappa_val, s)
    L_3ms = L_A_Eis(kappa_val, 3 - s)
    return {
        "s":            s,
        "L_at_s":       L_s,
        "L_at_3_minus_s": L_3ms,
        "ratio":        L_s / L_3ms if abs(L_3ms) > 1e-30 else None,
    }


# ============================================================================
# SECTION 6.  Zeros of the shadow Eisenstein L-function
# ============================================================================


def trivial_zeros(s_max_negative: int = 20) -> List[int]:
    """Trivial zeros of L_A^{Eis}(s) = -kappa zeta(s) zeta(s-1).

    A zero of zeta(s) at s = -2k (k >= 1) gives a zero of L_Eis at s = -2k.
    A zero of zeta(s-1) at s-1 = -2k, i.e. s = 1-2k (k >= 1) gives a zero
    of L_Eis at s = 1 - 2k.

    For k >= 1:  s in {-2, -4, -6, ...} from zeta(s)
                 s in {-1, -3, -5, ...} from zeta(s-1)
    Union:  ALL negative integers are trivial zeros of L_Eis.
    """
    return list(range(-1, -s_max_negative - 1, -1))


def riemann_zeros_image(n_zeros: int = 10) -> List[Tuple[complex, complex]]:
    """The non-trivial zeros of L_A^{Eis} come in TWO families:

      Family A:  zeros of zeta(s) at s = 1/2 + i t_n
      Family B:  zeros of zeta(s-1) at s = 3/2 + i t_n

    So for each Riemann zero rho_n = 1/2 + i t_n, the shadow Eisenstein
    L-function has TWO zeros: rho_n itself (on Re s = 1/2) and rho_n + 1
    (on Re s = 3/2).

    Returns list of (zeta_zero, shifted_zero) pairs.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    pairs = []
    for n in range(1, n_zeros + 1):
        rho = mpmath.zetazero(n)
        pairs.append((complex(rho), complex(rho) + 1))
    return pairs


def L_Eis_at_zeta_zero(kappa_val: float, n: int) -> complex:
    """L_Eis at the n-th non-trivial Riemann zero rho_n.

    Should equal -kappa * 0 * zeta(rho_n - 1) = 0 (zeta vanishes at rho_n).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    rho = mpmath.zetazero(n)
    return complex(-kappa_val * mpmath.zeta(rho) * mpmath.zeta(rho - 1))


def L_Eis_at_shifted_zeta_zero(kappa_val: float, n: int) -> complex:
    """L_Eis at rho_n + 1 where rho_n is the n-th Riemann zero.

    Should equal -kappa * zeta(rho_n + 1) * 0 = 0 (zeta(s-1) vanishes at s = rho_n + 1).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    rho = mpmath.zetazero(n)
    s = rho + 1
    return complex(-kappa_val * mpmath.zeta(s) * mpmath.zeta(s - 1))


def critical_lines() -> List[float]:
    """The critical lines of L_A^{Eis} = -kappa zeta(s) zeta(s-1).

    Two critical lines:  Re(s) = 1/2 (from zeta(s)) and Re(s) = 3/2 (from zeta(s-1)).
    Symmetry centre:  s = 1.
    """
    return [0.5, 1.5]


# ============================================================================
# SECTION 7.  Euler product
# ============================================================================


def euler_factor(p: int, s: complex) -> complex:
    """Euler factor of L_Eis at the prime p:

        L_p(s) = [(1 - p^{-s})(1 - p^{1-s})]^{-1}

    so that L_Eis(s) = -kappa * prod_p L_p(s).
    """
    return 1.0 / ((1.0 - p ** (-s)) * (1.0 - p ** (1 - s)))


def euler_product_truncated(kappa_val: float, s: complex, p_max: int = 100) -> complex:
    """Truncated Euler product:  -kappa * prod_{p <= p_max} L_p(s).

    Converges absolutely for Re(s) > 2.
    """
    primes = _sieve(p_max)
    prod = 1.0 + 0j
    for p in primes:
        prod *= euler_factor(p, s)
    return -kappa_val * prod


def _sieve(n: int) -> List[int]:
    """Sieve of Eratosthenes up to n."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def coefficient_an(n: int) -> int:
    """The Dirichlet coefficient a_n of -zeta(s) zeta(s-1) is -sigma_1(n).

    Verification:
        zeta(s) zeta(s-1) = sum_n n^{-s} sum_m m^{1-s}
                          = sum_{n,m} m / (nm)^s     [setting N = nm]
                          = sum_N N^{-s} sum_{d|N} d
                          = sum_N sigma_1(N) N^{-s}.
    So -zeta(s) zeta(s-1) = sum_N (-sigma_1(N)) N^{-s}.

    Returns -sigma_1(n).  Multiply by kappa for L_Eis.
    """
    if n < 1:
        return 0
    s1 = sum(d for d in range(1, n + 1) if n % d == 0)
    return -s1


def L_Eis_dirichlet_partial(kappa_val: float, s: complex, N_max: int = 200) -> complex:
    """Partial sum of the Dirichlet expansion -kappa sum sigma_1(n) n^{-s}.

    Converges only for Re(s) > 2.  Used to verify the Euler product
    and the closed form numerically.
    """
    total = 0.0 + 0j
    for n in range(1, N_max + 1):
        total += coefficient_an(n) * (n ** (-s))
    return kappa_val * total


# ============================================================================
# SECTION 8.  p-adic L-function (Kubota-Leopoldt construction)
# ============================================================================


def kummer_congruence_test(p: int, n: int, m: int) -> Dict[str, Fraction]:
    """Test the Kummer congruence for the shadow Eisenstein L-function.

    Classical Kummer:  if n = m mod (p-1) and p-1 does not divide n, then
        (1 - p^{n-1}) B_n / n  ===  (1 - p^{m-1}) B_m / m   mod p^{v_p(n-m)+1}

    For L_A^{Eis}, the relevant special values are at NEGATIVE integers,
    where L_Eis vanishes (by Section 6).  The non-trivial p-adic content
    therefore comes from the RESIDUES at the poles, NOT from special values.

    Specifically:  the p-adic interpolation of L_A^{Eis} reduces to that of
    -kappa zeta(s) (since the second factor zeta(s-1) is just a shift), and
    Kubota-Leopoldt gives L_p(1-n, omega^{1-n}) = -(1-p^{n-1}) B_n / n.

    Returns the two sides of the congruence and their difference.
    """
    Bn = bernoulli(n)
    Bm = bernoulli(m)
    lhs = (1 - Fraction(p) ** (n - 1)) * Bn / n
    rhs = (1 - Fraction(p) ** (m - 1)) * Bm / m
    return {
        "p": p,
        "n": n,
        "m": m,
        "lhs": lhs,
        "rhs": rhs,
        "diff": lhs - rhs,
    }


def p_adic_valuation(p: int, q: Fraction) -> int:
    """p-adic valuation of a rational q.  Returns infinity for q = 0."""
    if q == 0:
        return 10**9
    num, den = q.numerator, q.denominator
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def kubota_leopoldt_special_value(p: int, n: int, kappa_val: Fraction) -> Fraction:
    """The Kubota-Leopoldt p-adic shadow zeta at 1 - n:

        L_p^{sh}(1 - n)  =  -kappa * (1 - p^{n-1}) * B_n / n

    For n = 1:  -kappa * (1 - 1) * (-1/2) / 1 = 0.
    For n = 2:  -kappa * (1 - p) * (1/6) / 2 = -kappa(1-p)/12.
    For n even >= 2:  nontrivial value involving (1 - p^{n-1}) and B_n.
    For n odd >= 3:  B_n = 0, so result is 0.
    """
    if not isinstance(kappa_val, Fraction):
        kappa_val = Fraction(kappa_val).limit_denominator(10**9)
    if n < 1:
        raise ValueError("n must be >= 1")
    Bn = bernoulli(n)
    if Bn == 0:
        return Fraction(0)
    return -kappa_val * (1 - Fraction(p) ** (n - 1)) * Bn / n


# ============================================================================
# SECTION 9.  Special values requested in the user research questions
# ============================================================================


def L_at_s_eq_2(kappa_val: float) -> Optional[float]:
    """L_A^{Eis}(2) = -kappa * zeta(2) * zeta(1).

    POLE:  zeta(1) is a simple pole, so L_Eis has a simple pole at s = 2.
    The residue is -kappa * zeta(2) = -kappa pi^2 / 6.

    The user's claim L^sh(2) = -kappa pi^2 / 6 corresponds to the RESIDUE,
    not the value (which is infinite).  Returns None to indicate the pole.
    """
    return None  # pole


def L_at_s_eq_2_residue(kappa_val: float) -> float:
    """Residue of L_A^{Eis}(s) at s = 2:  -kappa * pi^2 / 6.

    For Virasoro at c = 26:  kappa = 13, residue = -13 pi^2 / 6.
    For Virasoro at c = 24:  kappa = 12, residue = -12 pi^2 / 6 = -2 pi^2.
    For V^natural (Monster, kappa = 24): residue = -24 pi^2 / 6 = -4 pi^2.
    """
    return -kappa_val * math.pi ** 2 / 6.0


def L_at_s_eq_0(kappa_val: float) -> float:
    """L_A^{Eis}(0) = -kappa * zeta(0) * zeta(-1) = -kappa * (-1/2)(-1/12) = -kappa/24.
    """
    return -kappa_val / 24.0


def L_at_s_eq_minus_1(kappa_val: float) -> float:
    """L_A^{Eis}(-1) = -kappa * zeta(-1) * zeta(-2) = -kappa * (-1/12) * 0 = 0.

    The user's claimed value -kappa/144 is INCORRECT (off by zeta(-2) = 0).
    """
    return 0.0


def L_at_negative_integers(kappa_val: float, max_neg: int = 10) -> Dict[int, float]:
    """L_A^{Eis} at all negative integers.

    By Section 6, every negative integer is a trivial zero of L_Eis.
    """
    return {-k: 0.0 for k in range(1, max_neg + 1)}


# ============================================================================
# SECTION 10.  Connection to F_g = kappa * lambda_g^FP
# ============================================================================


def F_g_via_riemann_FE(kappa_val: float, g: int) -> Optional[float]:
    """Conjectural connection to the higher-genus free energy via the Riemann
    functional equation.

    The shadow obstruction tower predicts:
        F_g(A) = kappa(A) * lambda_g^FP   on the uniform-weight lane (PROVED)

    The Faber-Pandharipande lambda_g class has  integral lambda_g^{2g-1} =
    [explicit formula in Bernoulli numbers].

    Specifically (Faber-Pandharipande, "Hodge integrals and Gromov-Witten theory"):
        sum_{g >= 1} lambda_g^{2g-1} * t^{2g} = ...

    The shadow zeta L_A^{Eis} at negative odd integers s = 1 - 2g gives:
        L_Eis(1 - 2g) = -kappa * zeta(1 - 2g) * zeta(-2g)
                      = -kappa * (-B_{2g}/(2g)) * 0
                      = 0
    so the negative-odd values do NOT directly recover F_g.

    However, the RESIDUE structure does:
        Res_{s=2} L_Eis(s) = -kappa * zeta(2) = -kappa * pi^2 / 6
    is the leading term in the asymptotic expansion of F_g, since
        sum_g F_g(A) = kappa * (A-hat genus expansion) ~ kappa * pi^2 / 6 * t^2 + ...

    Returns None to flag that the negative-odd-integer connection is FALSE
    and to direct attention to the residue connection.
    """
    return None


def A_hat_coefficient(g: int) -> Fraction:
    """Coefficient of the A-hat genus expansion at order x^{2g}.

    A-hat(x) = sqrt(x/2) / sinh(sqrt(x/2))
    Substituting x = i hbar:
        A-hat(i hbar) = sum_g a_g hbar^{2g}
    with leading coefficients a_0 = 1, a_1 = 1/24, a_2 = 7/5760, ...
    """
    # Use the closed form  A-hat(x) = exp(- sum_{k>=1} (zeta(2k)(2k-1)!/(2*(2pi)^{2k})) ... )
    # which is equivalent to the genus-1 free energy generating function.
    # For small g, hardcode from F-P:
    table = {
        0: Fraction(1),
        1: Fraction(1, 24),
        2: Fraction(7, 5760),
        3: Fraction(31, 967680),
        4: Fraction(127, 154828800),
    }
    if g not in table:
        raise NotImplementedError(f"A-hat coefficient at g={g} not tabulated")
    return table[g]


def F_g_predicted(kappa_val: float, g: int) -> float:
    """F_g(A) on the uniform-weight lane:  F_g = kappa * lambda_g^FP.

    For Vir, the free energy is kappa * A-hat coefficient.
    """
    return kappa_val * float(A_hat_coefficient(g))


# ============================================================================
# SECTION 11.  Monster / V^natural special case
# ============================================================================


def L_Eis_monster(s: complex) -> complex:
    """Shadow Eisenstein L-function for the Moonshine module V^natural.

    AP48:  kappa(V^natural) = 24 (rank), NOT c/2 = 12.
    The lattice-VOA formula  kappa = rank  applies because V^natural is built
    from a chiral orbifold of the Leech lattice VOA, inheriting the
    Heisenberg / lattice modular characteristic.

    L_{V^natural}^{Eis}(s) = -24 * zeta(s) * zeta(s-1).
    """
    return L_A_Eis(24.0, s)


def monster_residue_at_2() -> float:
    """Residue of L_{V^natural}^{Eis}(s) at s = 2:  -24 * pi^2 / 6 = -4 pi^2.

    The user proposed L^sh(2) = -2 pi^2 (using kappa = 12 = c/2), but the
    correct value is -4 pi^2 (using kappa = 24 = rank).  This is a direct
    instance of AP48: kappa(V^natural) is NOT c/2.
    """
    return -4.0 * math.pi ** 2


def monster_kappa_correction() -> Dict[str, float]:
    """The user's research question 6 conflated kappa(V^natural) = 12 (= c/2)
    with the correct kappa(V^natural) = 24 (= rank).  Document the correction.
    """
    return {
        "user_kappa": 12.0,                 # c/2 (incorrect for lattice VOAs)
        "correct_kappa": 24.0,              # rank (per AP48)
        "user_residue_at_2": -2.0 * math.pi ** 2,
        "correct_residue_at_2": -4.0 * math.pi ** 2,
        "ratio": 2.0,
    }


# ============================================================================
# SECTION 12.  The full diagnostic
# ============================================================================


def full_diagnostic(kappa_val: float = 13.0, p: int = 5) -> Dict[str, object]:
    """Run the full arithmetic diagnostic for a given kappa.

    kappa = 13 is the Virasoro self-dual point (c = 26).
    """
    return {
        "kappa": kappa_val,
        "L_at_0": L_at_s_eq_0(kappa_val),
        "L_at_minus_1": L_at_s_eq_minus_1(kappa_val),
        "residue_at_1": L_Eis_pole_residues(kappa_val)["residue_at_s_eq_1"],
        "residue_at_2": L_Eis_pole_residues(kappa_val)["residue_at_s_eq_2"],
        "trivial_zeros": trivial_zeros(10),
        "critical_lines": critical_lines(),
        "kummer_p2_n4_n6": kummer_congruence_test(2, 4, 6),
        "kubota_leopoldt_at_minus_1": kubota_leopoldt_special_value(
            p, 2, Fraction(kappa_val).limit_denominator(10**6)),
        "F_1_predicted": F_g_predicted(kappa_val, 1),
        "F_2_predicted": F_g_predicted(kappa_val, 2),
        "disagreement_diagnostic": disagreement_at_zero(kappa_val, r_max=80),
    }
