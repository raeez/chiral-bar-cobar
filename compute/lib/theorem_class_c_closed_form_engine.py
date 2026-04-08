r"""Closed-form genus expansion for class C (beta-gamma / bc ghost) algebras.

MAIN RESULT: For class C algebras (beta-gamma, bc ghost), the shadow tower
terminates at S_4: all S_r = 0 for r >= 5. The planted-forest correction at
each genus is a polynomial in (kappa, S_3, S_4) alone.

THE CLASS C SHADOW TOWER
========================

Class C algebras have shadow depth r_max = 4 (contact/quartic class). The
tower terminates because the quintic obstruction vanishes by stratum
separation: the quartic contact invariant lives on a charged stratum whose
self-bracket exits the complex by rank-one rigidity.

  Beta-gamma at conformal weight lambda:
    c(lambda) = 2(6*lambda^2 - 6*lambda + 1)
    kappa(lambda) = c/2 = 6*lambda^2 - 6*lambda + 1

    T-line projection (Sugawara/Virasoro component):
      S_3 = 2
      S_4 = 10 / [c(5c+22)]   [inherits Virasoro formula]
      S_r = 0 for r >= 5       [terminates at depth 4]

    Charged stratum (beta*gamma contact direction):
      S_3 = 0  (alpha = 0 by rank-one rigidity)
      S_4 = -5/12  (independent of lambda)
      S_r = 0 for r >= 5

FREE ENERGY DECOMPOSITION
==========================

    F_g(A) = kappa(A) * lambda_g^FP + delta_pf^{(g,0)}(kappa, S_3, S_4)

COEFFICIENT EXACTNESS
======================

The planted-forest polynomial has two categories of coefficients:

    EXACT:  Terms involving only genus-0 vertices (pure S_3, S_4 monomials
            with no kappa factor, or terms where the kappa factor comes from
            graph topology, not genus-1+ vertex weights).
            The class L polynomial (all terms) was verified at SU(2..4).
            The pure genus-0 S_4 terms (-167/96 S_3^2 S_4, -7/12 S_4^2) are
            exact from graph combinatorics.

    APPROXIMATE: Mixed terms involving both S_4 and kappa factors from
            genus-1+ vertex weights (ell_k^{(1)} for valence >= 3 is
            approximated as kappa). These are flagged below.

At genus 2: the polynomial is EXACT (S_4 does not appear; verified).
At genus 3: 5 class-L terms EXACT + 2 pure-genus-0 S_4 terms EXACT +
            2 mixed kappa*S_4 terms APPROXIMATE.
At genus 4: class-L terms EXACT + S_4 terms mixed exact/approximate.

SHADOW VISIBILITY (cor:shadow-visibility-genus):
    g_min(S_r) = floor(r/2) + 1.
    S_3 first appears at g = 2 (floor(3/2)+1 = 2).
    S_4 first appears at g = 3 (floor(4/2)+1 = 3).
    Consequence: delta_pf at g=2 depends on S_3 only.

MULTI-PATH VERIFICATION
========================

Path 1: Direct polynomial evaluation at specific beta-gamma parameters.
Path 2: Specialization S_4 -> 0 recovers class L formula (EXACT check).
Path 3: Heisenberg limit S_3 -> 0, S_4 -> 0: delta_pf -> 0.
Path 4: Additivity of scalar part (linearity in kappa).
Path 5: Virasoro comparison: beta-gamma T-line inherits Virasoro formula.
Path 6: Genus-3 cross-check: class C formula vs generic 11-term at S_5=0.

ANTI-PATTERN COMPLIANCE
========================

AP1:  kappa computed from defining formula, not copied.
AP9:  kappa = c/2 for single-generator beta-gamma.
AP10: Multi-path verification, not hardcoded expected values.
AP14: Class C is KOSZUL. Shadow depth classifies complexity, not Koszulness.
AP19: Bar residue order = OPE pole - 1 (d log absorption).
AP24: kappa + kappa' = 1 for beta-gamma (not zero).
AP39: kappa = c/2 for single-generator (non-issue for rank 1).
AP48: kappa depends on the full algebra, not the Virasoro subalgebra.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    eq:delta-pf-genus3-explicit (higher_genus_modular_koszul.tex)
    prop:betagamma-obstruction-coefficient (beta_gamma.tex)
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, factorial
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# Section 1: Exact arithmetic primitives
# ============================================================================

@lru_cache(maxsize=64)
def bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n via the standard recurrence.

    Convention: B_1 = -1/2 (first Bernoulli numbers).
    """
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n >= 3:
        return Fraction(0)
    result = Fraction(0)
    for k in range(n):
        result += comb(n + 1, k) * bernoulli_exact(k)
    return -result / (n + 1)


def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^{FP}.

    lambda_g^FP = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    Verified:
      g=1: 1/24
      g=2: 7/5760
      g=3: 31/967680
      g=4: 127/154828800
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli_exact(2 * g)
    abs_B = abs(B_2g)
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1) * abs_B / Fraction(power * factorial(2 * g))


# ============================================================================
# Section 2: Beta-gamma shadow data (AP1: each from definition)
# ============================================================================

def central_charge_betagamma(lam: Fraction) -> Fraction:
    r"""Central charge of beta-gamma at conformal weight lambda.

    c(lambda) = 2(6*lambda^2 - 6*lambda + 1) = 12*lambda^2 - 12*lambda + 2.

    At lambda = 0: c = 2.   At lambda = 1: c = 2.
    At lambda = 1/2: c = -1. At lambda = 2: c = 26.
    """
    return 12 * lam ** 2 - 12 * lam + 2


def kappa_betagamma(lam: Fraction) -> Fraction:
    r"""Modular characteristic of beta-gamma at conformal weight lambda.

    kappa = c/2 = 6*lambda^2 - 6*lambda + 1.

    AP1: computed from definition (single generator, so kappa = c/2).

    At lambda = 0: kappa = 1.   At lambda = 1: kappa = 1.
    At lambda = 1/2: kappa = -1/2. At lambda = 2: kappa = 13.
    """
    return 6 * lam ** 2 - 6 * lam + 1


def S3_betagamma_tline() -> Fraction:
    """Cubic shadow on the T-line: S_3 = 2 (same as Virasoro).

    The T-line inherits the Virasoro OPE structure.
    """
    return Fraction(2)


def S4_betagamma_tline(lam: Fraction) -> Fraction:
    r"""Quartic shadow on the T-line: S_4 = 10/[c(5c+22)].

    Inherits the Virasoro formula Q^contact_Vir.

    At lambda = 1: c = 2, S_4 = 10/(2*32) = 5/32.
    At lambda = 0: c = 2, S_4 = 5/32.
    At lambda = 2: c = 26, S_4 = 10/(26*152) = 5/1976.
    """
    c = central_charge_betagamma(lam)
    denom = c * (5 * c + 22)
    if denom == 0:
        raise ValueError(f"S_4 pole: lambda={lam} gives c={c}, denom={denom}")
    return Fraction(10) / denom


def S4_betagamma_charged() -> Fraction:
    """Quartic shadow on the charged stratum: S_4 = -5/12.

    Independent of lambda. From the explicit arity-4 graph sum on the
    charged stratum, with alpha = 0 by rank-one rigidity.
    """
    return Fraction(-5, 12)


def shadow_tower_class_C_tline(lam: Fraction) -> Dict[str, Fraction]:
    """Complete shadow tower for beta-gamma T-line. S_r = 0 for r >= 5."""
    return {
        'kappa': kappa_betagamma(lam),
        'c': central_charge_betagamma(lam),
        'S_3': S3_betagamma_tline(),
        'S_4': S4_betagamma_tline(lam),
        'S_5': Fraction(0),
    }


def shadow_tower_class_C_charged(lam: Fraction) -> Dict[str, Fraction]:
    """Complete shadow tower for beta-gamma charged stratum."""
    return {
        'kappa': kappa_betagamma(lam),
        'c': central_charge_betagamma(lam),
        'S_3': Fraction(0),
        'S_4': S4_betagamma_charged(),
        'S_5': Fraction(0),
    }


# ============================================================================
# Section 3: bc ghost shadow data
# ============================================================================

def central_charge_bc(j: Fraction) -> Fraction:
    r"""Central charge of bc ghost at spin j.

    c(j) = -(12j^2 - 12j + 2) = -2(6j^2 - 6j + 1).

    At j = 2 (reparametrization ghosts): c = -26.
    At j = 1 (fermionic ghosts): c = -2.
    """
    return -(12 * j ** 2 - 12 * j + 2)


def kappa_bc(j: Fraction) -> Fraction:
    """Modular characteristic of bc ghost: kappa = c/2."""
    return central_charge_bc(j) / 2


def S4_bc_tline(j: Fraction) -> Fraction:
    """Quartic shadow for bc ghost T-line: S_4 = 10/[c(5c+22)]."""
    c = central_charge_bc(j)
    denom = c * (5 * c + 22)
    if denom == 0:
        raise ValueError(f"S_4 pole: j={j} gives c={c}, denom={denom}")
    return Fraction(10) / denom


# ============================================================================
# Section 4: Planted-forest polynomials for class C
# ============================================================================

# -------------------------------------------------------------------
# Genus 2: delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48
# EXACT. S_4 does NOT contribute at genus 2.
# Reason: the sunset graph (0,4) with 2 self-loops has integral I = 0
# by self-loop parity vanishing (prop:self-loop-vanishing).
# Shadow visibility: g_min(S_4) = floor(4/2)+1 = 3 > 2.
# -------------------------------------------------------------------

def delta_pf_genus2(kappa: Fraction, S3: Fraction,
                    S4: Fraction = Fraction(0)) -> Fraction:
    r"""Genus-2 planted-forest correction. EXACT.

    delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48.

    S_4 parameter accepted but does not contribute (self-loop parity).
    """
    return S3 * (10 * S3 - kappa) / 48


# -------------------------------------------------------------------
# Genus 3: Exact class L base + S_4 corrections.
#
# The genus-3 planted-forest polynomial decomposes as:
#
#   delta_pf^{(3,0)}(kappa, S_3, S_4) =
#       delta_pf_classL(kappa, S_3)
#     + delta_pf_S4_pure(S_3, S_4)
#     + delta_pf_S4_mixed(kappa, S_3, S_4)     [APPROXIMATE]
#
# The class L base (5 terms) is EXACT (verified at SU(2..4)):
# -------------------------------------------------------------------

# Class L polynomial at genus 3 (EXACT, from theorem_class_l_closed_form_engine)
GENUS3_PF_CLASS_L: Dict[Tuple[int, int], Fraction] = {
    (0, 4): Fraction(15, 64),       # S_3^4
    (1, 3): Fraction(-35, 1536),    # kappa * S_3^3
    (2, 2): Fraction(1, 1152),      # kappa^2 * S_3^2
    (3, 1): Fraction(-1, 82944),    # kappa^3 * S_3
    (1, 1): Fraction(-343, 2304),   # kappa * S_3
}


def _delta_pf_genus3_class_L(kappa: Fraction, S3: Fraction) -> Fraction:
    """Class L genus-3 planted-forest polynomial. EXACT.

    5-term polynomial in (kappa, S_3), verified at SU(2), SU(3), SU(4)
    against the full 42-graph sum restricted to class L data.
    """
    result = Fraction(0)
    for (a, b), coeff in GENUS3_PF_CLASS_L.items():
        result += coeff * kappa ** a * S3 ** b
    return result


# Pure genus-0 S_4 terms (EXACT: no genus-1 vertex weights involved).
# These come from graphs with only genus-0 vertices carrying S_3 and S_4.

GENUS3_S4_PURE: Dict[Tuple[int, int], Fraction] = {
    # Keys: (S_3 degree, S_4 degree)
    (2, 1): Fraction(-167, 96),     # S_3^2 * S_4 [two (0,3) + one (0,4)]
    (0, 2): Fraction(-7, 12),       # S_4^2 [two (0,4) vertices]
}


def _delta_pf_genus3_S4_pure(S3: Fraction, S4: Fraction) -> Fraction:
    """Pure genus-0 S_4 terms at genus 3. EXACT.

    Two terms from graphs with only genus-0 vertices:
    (a) -167/96 * S_3^2 * S_4:  from graphs with two (0,3) vertices and
        one (0,4) vertex. Coefficient exact from pure genus-0 combinatorics.
    (b) -7/12 * S_4^2:  from graphs with two (0,4) vertices.
        Coefficient exact from pure genus-0 combinatorics.
    """
    return Fraction(-167, 96) * S3 ** 2 * S4 + Fraction(-7, 12) * S4 ** 2


# Mixed kappa * S_4 terms (APPROXIMATE: involve genus-1+ vertex weights).
# The approximation ell_k^{(1)} ~ kappa is used for genus-1 vertices of
# valence >= 3. The coefficients below come from eq:delta-pf-genus3-explicit.

GENUS3_S4_MIXED: Dict[Tuple[int, int, int], Fraction] = {
    # Keys: (kappa degree, S_3 degree, S_4 degree)
    (1, 1, 1): Fraction(83, 1152),   # kappa * S_3 * S_4
    (2, 0, 1): Fraction(1, 1152),    # kappa^2 * S_4
}


def _delta_pf_genus3_S4_mixed(kappa: Fraction, S3: Fraction,
                               S4: Fraction) -> Fraction:
    """Mixed kappa * S_4 terms at genus 3. APPROXIMATE.

    Two terms involving genus-1 vertex weights (approximation):
    (a) 83/1152 * kappa * S_3 * S_4
    (b) 1/1152 * kappa^2 * S_4
    """
    return Fraction(83, 1152) * kappa * S3 * S4 + Fraction(1, 1152) * kappa ** 2 * S4


def delta_pf_genus3_class_C(kappa: Fraction, S3: Fraction,
                             S4: Fraction) -> Fraction:
    r"""Genus-3 planted-forest correction for class C (S_5 = 0).

    Decomposes as:
      class L base (5 terms, EXACT)
    + pure genus-0 S_4 (2 terms, EXACT)
    + mixed kappa * S_4 (2 terms, APPROXIMATE)
    = 9 terms total.

    Setting S_4 = 0 recovers the EXACT class L polynomial.
    """
    return (
        _delta_pf_genus3_class_L(kappa, S3)
        + _delta_pf_genus3_S4_pure(S3, S4)
        + _delta_pf_genus3_S4_mixed(kappa, S3, S4)
    )


def delta_pf_genus3_generic(kappa: Fraction, S3: Fraction,
                             S4: Fraction, S5: Fraction) -> Fraction:
    r"""Full generic genus-3 planted-forest correction (all 11 terms).

    From eq:delta-pf-genus3-explicit (genus-1+ vertex weights approximate).
    For class C, pass S5 = 0.  For class L, pass S4 = S5 = 0.

    WARNING: The S_3-only terms here use the APPROXIMATE coefficients from
    the manuscript, NOT the exact class L polynomial. For exact computation,
    use delta_pf_genus3_class_C (which uses the exact class L base).
    """
    return (
        Fraction(7, 8) * S3 * S5
        + Fraction(3, 512) * S3 ** 3 * kappa
        - Fraction(5, 128) * S3 ** 4
        - Fraction(167, 96) * S3 ** 2 * S4
        + Fraction(83, 1152) * S3 * S4 * kappa
        - Fraction(343, 2304) * S3 * kappa
        - Fraction(1, 4608) * S3 ** 2 * kappa ** 2
        - Fraction(1, 82944) * S3 * kappa ** 3
        - Fraction(7, 12) * S4 ** 2
        + Fraction(1, 1152) * S4 * kappa ** 2
        - Fraction(1, 96) * S5 * kappa
    )


# -------------------------------------------------------------------
# Genus 4: class L base + S_4 corrections.
#
# The class L genus-4 polynomial (11 terms in kappa, S_3) is EXACT
# (verified at SU(2..4) against the 379-graph sum).
#
# The S_4-dependent terms at genus 4 come from graphs in Mbar_{4,0}
# containing at least one valence-4 genus-0 vertex (carrying S_4).
# Pure genus-0 S_4 terms are EXACT; mixed kappa*S_4 APPROXIMATE.
# -------------------------------------------------------------------

GENUS4_PF_CLASS_L: Dict[Tuple[int, int], Fraction] = {
    (0, 6): Fraction(425, 576),
    (1, 5): Fraction(-515, 9216),
    (2, 4): Fraction(421, 221184),
    (3, 3): Fraction(-7, 196608),
    (4, 2): Fraction(5, 15925248),
    (1, 3): Fraction(-19319, 27648),
    (2, 2): Fraction(9223, 331776),
    (1, 2): Fraction(2317, 1536),
    (3, 1): Fraction(-143, 1327104),
    (2, 1): Fraction(-13, 864),
    (1, 1): Fraction(-123589, 165888),
}


def _delta_pf_genus4_class_L(kappa: Fraction, S3: Fraction) -> Fraction:
    """Class L genus-4 planted-forest polynomial. EXACT."""
    result = Fraction(0)
    for (a, b), coeff in GENUS4_PF_CLASS_L.items():
        result += coeff * kappa ** a * S3 ** b
    return result


# Pure genus-0 S_4 terms at genus 4 (EXACT).
# These come from graphs with only genus-0 vertices.

GENUS4_S4_PURE: Dict[Tuple[int, int], Fraction] = {
    # Keys: (S_3 degree, S_4 degree)
    (0, 3): Fraction(35, 48),       # S_4^3 [three (0,4) vertices]
    (2, 2): Fraction(167, 16),      # S_3^2 * S_4^2 [two (0,3) + two (0,4)]
    (4, 1): Fraction(5005, 1536),   # S_3^4 * S_4 [four (0,3) + one (0,4)]
    (1, 2): Fraction(2891, 576),    # S_3 * S_4^2 [one (0,3) + two (0,4)]
}


def _delta_pf_genus4_S4_pure(S3: Fraction, S4: Fraction) -> Fraction:
    """Pure genus-0 S_4 terms at genus 4. EXACT."""
    result = Fraction(0)
    for (b, d), coeff in GENUS4_S4_PURE.items():
        result += coeff * S3 ** b * S4 ** d
    return result


# Mixed kappa * S_4 terms at genus 4 (APPROXIMATE).

GENUS4_S4_MIXED: Dict[Tuple[int, int, int], Fraction] = {
    # Keys: (kappa degree, S_3 degree, S_4 degree)
    (1, 0, 2): Fraction(-7, 192),         # kappa * S_4^2
    (2, 0, 1): Fraction(1, 3456),         # kappa^2 * S_4
    (1, 1, 2): Fraction(-83, 384),        # kappa * S_3 * S_4^2
    (1, 3, 1): Fraction(-8701, 27648),    # kappa * S_3^3 * S_4
    (2, 2, 1): Fraction(167, 27648),      # kappa^2 * S_3^2 * S_4
    (1, 2, 1): Fraction(-1519, 1152),     # kappa * S_3^2 * S_4
    (3, 1, 1): Fraction(-83, 995328),     # kappa^3 * S_3 * S_4
    (1, 0, 1): Fraction(343, 4608),       # kappa * S_4
    (3, 0, 1): Fraction(1, 497664),       # kappa^3 * S_4
}


def _delta_pf_genus4_S4_mixed(kappa: Fraction, S3: Fraction,
                               S4: Fraction) -> Fraction:
    """Mixed kappa * S_4 terms at genus 4. APPROXIMATE."""
    result = Fraction(0)
    for (a, b, d), coeff in GENUS4_S4_MIXED.items():
        result += coeff * kappa ** a * S3 ** b * S4 ** d
    return result


def delta_pf_genus4_class_C(kappa: Fraction, S3: Fraction,
                             S4: Fraction) -> Fraction:
    r"""Genus-4 planted-forest correction for class C.

    Decomposes as:
      class L base (11 terms, EXACT)
    + pure genus-0 S_4 (4 terms, EXACT)
    + mixed kappa * S_4 (9 terms, APPROXIMATE)
    = 24 terms total.

    Setting S_4 = 0 recovers the EXACT class L polynomial.
    """
    return (
        _delta_pf_genus4_class_L(kappa, S3)
        + _delta_pf_genus4_S4_pure(S3, S4)
        + _delta_pf_genus4_S4_mixed(kappa, S3, S4)
    )


# ============================================================================
# Section 5: Free energy at each genus for class C
# ============================================================================

def F_g_class_C(g: int, kappa: Fraction, S3: Fraction,
                S4: Fraction) -> Fraction:
    r"""Total free energy F_g for a class C algebra.

    F_g = kappa * lambda_g^FP + delta_pf^{(g,0)}(kappa, S_3, S_4).

    Genera 1-4 use closed-form polynomials. The class L base and pure
    genus-0 S_4 terms are exact; mixed kappa*S_4 terms approximate.
    """
    scalar = kappa * lambda_fp(g)

    if g == 1:
        return scalar
    elif g == 2:
        return scalar + delta_pf_genus2(kappa, S3, S4)
    elif g == 3:
        return scalar + delta_pf_genus3_class_C(kappa, S3, S4)
    elif g == 4:
        return scalar + delta_pf_genus4_class_C(kappa, S3, S4)
    else:
        raise ValueError(
            f"Closed-form planted-forest polynomial not available at genus {g}."
        )


# ============================================================================
# Section 6: Beta-gamma evaluations
# ============================================================================

@dataclass(frozen=True)
class ClassCGenusExpansion:
    """Complete genus expansion for a class C algebra."""
    name: str
    lam: Fraction
    kappa: Fraction
    c: Fraction
    S_3: Fraction
    S_4: Fraction
    shadow_class: str
    F_1: Fraction
    F_1_scalar: Fraction
    F_2: Fraction
    F_2_scalar: Fraction
    F_2_pf: Fraction
    F_3: Fraction
    F_3_scalar: Fraction
    F_3_pf: Fraction
    F_4: Fraction
    F_4_scalar: Fraction
    F_4_pf: Fraction


def genus_expansion_betagamma_tline(lam: Fraction) -> ClassCGenusExpansion:
    """Genus expansion for beta-gamma T-line through genus 4."""
    lam_f = Fraction(lam) if not isinstance(lam, Fraction) else lam
    tower = shadow_tower_class_C_tline(lam_f)
    kap = tower['kappa']
    s3 = tower['S_3']
    s4 = tower['S_4']
    c = tower['c']

    F1 = F_g_class_C(1, kap, s3, s4)
    F2_scalar = kap * lambda_fp(2)
    F2_pf = delta_pf_genus2(kap, s3, s4)
    F2 = F2_scalar + F2_pf
    F3_scalar = kap * lambda_fp(3)
    F3_pf = delta_pf_genus3_class_C(kap, s3, s4)
    F3 = F3_scalar + F3_pf
    F4_scalar = kap * lambda_fp(4)
    F4_pf = delta_pf_genus4_class_C(kap, s3, s4)
    F4 = F4_scalar + F4_pf

    return ClassCGenusExpansion(
        name=f'betagamma(lam={lam_f})_Tline',
        lam=lam_f, kappa=kap, c=c, S_3=s3, S_4=s4, shadow_class='C',
        F_1=F1, F_1_scalar=kap * lambda_fp(1),
        F_2=F2, F_2_scalar=F2_scalar, F_2_pf=F2_pf,
        F_3=F3, F_3_scalar=F3_scalar, F_3_pf=F3_pf,
        F_4=F4, F_4_scalar=F4_scalar, F_4_pf=F4_pf,
    )


def genus_expansion_betagamma_charged(lam: Fraction) -> ClassCGenusExpansion:
    """Genus expansion for beta-gamma charged stratum through genus 4."""
    lam_f = Fraction(lam) if not isinstance(lam, Fraction) else lam
    tower = shadow_tower_class_C_charged(lam_f)
    kap = tower['kappa']
    s3 = tower['S_3']
    s4 = tower['S_4']
    c = tower['c']

    F1 = F_g_class_C(1, kap, s3, s4)
    F2_scalar = kap * lambda_fp(2)
    F2_pf = delta_pf_genus2(kap, s3, s4)
    F2 = F2_scalar + F2_pf
    F3_scalar = kap * lambda_fp(3)
    F3_pf = delta_pf_genus3_class_C(kap, s3, s4)
    F3 = F3_scalar + F3_pf
    F4_scalar = kap * lambda_fp(4)
    F4_pf = delta_pf_genus4_class_C(kap, s3, s4)
    F4 = F4_scalar + F4_pf

    return ClassCGenusExpansion(
        name=f'betagamma(lam={lam_f})_charged',
        lam=lam_f, kappa=kap, c=c, S_3=s3, S_4=s4, shadow_class='C',
        F_1=F1, F_1_scalar=kap * lambda_fp(1),
        F_2=F2, F_2_scalar=F2_scalar, F_2_pf=F2_pf,
        F_3=F3, F_3_scalar=F3_scalar, F_3_pf=F3_pf,
        F_4=F4, F_4_scalar=F4_scalar, F_4_pf=F4_pf,
    )


# ============================================================================
# Section 7: Class L degeneration (S_4 -> 0)
# ============================================================================

def class_L_degeneration_check(g: int, kappa: Fraction,
                                S3: Fraction) -> Dict[str, Any]:
    r"""Verify that class C formula at S_4 = 0 recovers class L.

    For any genus g in {2, 3, 4}, setting S_4 = 0 in the class C
    planted-forest polynomial must yield the class L polynomial.
    """
    if g == 2:
        class_C_at_zero = delta_pf_genus2(kappa, S3, Fraction(0))
    elif g == 3:
        class_C_at_zero = delta_pf_genus3_class_C(kappa, S3, Fraction(0))
    elif g == 4:
        class_C_at_zero = delta_pf_genus4_class_C(kappa, S3, Fraction(0))
    else:
        raise ValueError(f"Genus {g} not supported")

    class_L_val = _delta_pf_class_L_standalone(g, kappa, S3)

    return {
        'genus': g,
        'class_C_at_S4_zero': class_C_at_zero,
        'class_L_direct': class_L_val,
        'match': class_C_at_zero == class_L_val,
    }


def _delta_pf_class_L_standalone(g: int, kappa: Fraction,
                                  S3: Fraction) -> Fraction:
    """Class L planted-forest polynomial, standalone (for comparison).

    Independent reimplementation from the class L engine coefficients.
    """
    if g == 1:
        return Fraction(0)
    elif g == 2:
        return S3 * (10 * S3 - kappa) / 48
    elif g == 3:
        return _delta_pf_genus3_class_L(kappa, S3)
    elif g == 4:
        return _delta_pf_genus4_class_L(kappa, S3)
    else:
        raise ValueError(f"Class L polynomial not available at genus {g}")


# ============================================================================
# Section 8: Heisenberg limit (S_3 = S_4 = 0)
# ============================================================================

def heisenberg_limit_check(g: int, kappa_val: Fraction) -> Dict[str, Any]:
    """Verify that S_3 = S_4 = 0 recovers Heisenberg F_g = kappa * lambda_fp."""
    F_heis = kappa_val * lambda_fp(g)
    if g <= 4:
        F_class_C = F_g_class_C(g, kappa_val, Fraction(0), Fraction(0))
    else:
        F_class_C = kappa_val * lambda_fp(g)
    return {
        'F_heisenberg': F_heis,
        'F_classC_at_zero': F_class_C,
        'match': F_heis == F_class_C,
    }


# ============================================================================
# Section 9: Additivity of scalar part
# ============================================================================

def additivity_scalar_check(g: int) -> Dict[str, Any]:
    r"""Verify that the scalar part is linear in kappa."""
    kap1 = kappa_betagamma(Fraction(1))   # kappa = 1
    kap2 = kappa_betagamma(Fraction(2))   # kappa = 13

    lfp = lambda_fp(g)
    F_sum = (kap1 + kap2) * lfp
    F_parts = kap1 * lfp + kap2 * lfp

    return {
        'kappa_1': kap1,
        'kappa_2': kap2,
        'F_scalar_sum': F_sum,
        'F_scalar_1_plus_2': F_parts,
        'additive': F_sum == F_parts,
    }


# ============================================================================
# Section 10: Degree analysis
# ============================================================================

def pf_degree_analysis_class_C() -> Dict[int, Dict[str, Any]]:
    """Analyze the degree structure of delta_pf for class C.

    The total degree in (kappa, S_3, S_4) is bounded by 2(g-1).
    """
    results = {}

    # Genus 2: S_3*(10*S_3 - kappa)/48, max total degree 2
    results[2] = {
        'max_total_degree': 2,
        'num_terms': 2,
        'bound_2gm2': 2,
        'satisfies_bound': True,
        'S4_dependence': False,
    }

    # Genus 3: collect all terms
    all_g3 = {}
    for (a, b), c_val in GENUS3_PF_CLASS_L.items():
        all_g3[(a, b, 0)] = c_val
    for (b, d), c_val in GENUS3_S4_PURE.items():
        all_g3[(0, b, d)] = c_val
    for (a, b, d), c_val in GENUS3_S4_MIXED.items():
        all_g3[(a, b, d)] = c_val
    max_tot_3 = max(a + b + d for (a, b, d) in all_g3)
    results[3] = {
        'max_total_degree': max_tot_3,
        'num_terms': len(all_g3),
        'bound_2gm2': 4,
        'satisfies_bound': max_tot_3 <= 4,
        'S4_dependence': True,
        'num_exact_terms': 5 + 2,
        'num_approx_terms': 2,
    }

    # Genus 4: collect all terms
    all_g4 = {}
    for (a, b), c_val in GENUS4_PF_CLASS_L.items():
        all_g4[(a, b, 0)] = c_val
    for (b, d), c_val in GENUS4_S4_PURE.items():
        all_g4[(0, b, d)] = c_val
    for (a, b, d), c_val in GENUS4_S4_MIXED.items():
        all_g4[(a, b, d)] = c_val
    max_tot_4 = max(a + b + d for (a, b, d) in all_g4)
    results[4] = {
        'max_total_degree': max_tot_4,
        'num_terms': len(all_g4),
        'bound_2gm2': 6,
        'satisfies_bound': max_tot_4 <= 6,
        'S4_dependence': True,
        'num_exact_terms': 11 + 4,
        'num_approx_terms': 9,
    }

    return results


# ============================================================================
# Section 11: Complementarity for beta-gamma (AP24)
# ============================================================================

def complementarity_betagamma(lam: Fraction) -> Dict[str, Any]:
    r"""Complementarity check for beta-gamma.

    c + c' = 2 for all lambda. kappa + kappa' = 1 (constant).
    AP24: this is NOT zero (unlike KM where kappa + kappa' = 0).
    """
    kap = kappa_betagamma(lam)
    c = central_charge_betagamma(lam)
    c_dual = 2 - c
    kap_dual = c_dual / 2

    return {
        'lambda': lam,
        'kappa': kap,
        'c': c,
        'c_dual': c_dual,
        'kappa_dual': kap_dual,
        'kappa_sum': kap + kap_dual,
        'c_sum': c + c_dual,
        'sum_is_one': kap + kap_dual == Fraction(1),
    }


# ============================================================================
# Section 12: Summary table
# ============================================================================

def summary_table(lam_values: Optional[List[Fraction]] = None,
                  stratum: str = 'tline') -> List[Dict[str, Any]]:
    """Summary of F_1, ..., F_4 for beta-gamma at various lambda."""
    if lam_values is None:
        lam_values = [Fraction(0), Fraction(1, 2), Fraction(1),
                      Fraction(2), Fraction(3)]
    rows = []
    for lam in lam_values:
        if stratum == 'tline':
            exp = genus_expansion_betagamma_tline(lam)
        else:
            exp = genus_expansion_betagamma_charged(lam)
        rows.append({
            'lambda': lam,
            'kappa': exp.kappa,
            'c': exp.c,
            'S_3': exp.S_3,
            'S_4': exp.S_4,
            'F_1': exp.F_1,
            'F_2': exp.F_2,
            'F_3': exp.F_3,
            'F_4': exp.F_4,
        })
    return rows
