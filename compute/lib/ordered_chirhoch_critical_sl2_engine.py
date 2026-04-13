r"""Ordered chiral Hochschild cohomology of V_{-2}(sl_2) at critical level.

MATHEMATICAL FRAMEWORK
======================

At the critical level k = -h^v = -2 for sl_2, six dramatic structural
changes occur simultaneously:

(1) KAPPA VANISHES: kappa(V_{-2}(sl_2)) = dim(sl_2)*(k+h^v)/(2*h^v)
    = 3*(0)/(4) = 0.  The modular characteristic is zero; the bar complex
    is UNCURVED (d^2 = 0 unconditionally, no Hodge curvature).

(2) KZ CONNECTION DIVERGES: The KZ connection form is
    nabla_KZ = d - Omega/((k+2)*z) dz
    (KZ convention, C9/AP148).  At k = -2, the denominator k+2 = 0 and
    the connection DIVERGES.  This is the Sugawara singularity: the
    Sugawara element T = (1/(2*(k+h^v))) * sum :J^a J^a: is undefined.

(3) FEIGIN-FRENKEL CENTER JUMPS: The center of V_k(sl_2) at generic k
    is C (just scalars).  At critical level, the center JUMPS to
    Z(V_{-2}(sl_2)) = Fun(Op_{sl_2}(D)) = C[S_2]
    a polynomial algebra on one generator S_2 of conformal weight 2
    (the oper = projective connection on the formal disk).

(4) BAR COHOMOLOGY SPREADS: At generic k, H^n(B(V_k(sl_2))) is
    concentrated at n=1 with dim = 3 = dim(sl_2) (Koszulness).
    At critical level, H^*(B(V_{-2}(sl_2))) = Omega^*(Op_{sl_2}(D))
    = C[S_2] tensor Lambda(dS_2), which has H^0 = C[S_2] (infinite-dim)
    and H^1 = C[S_2]*dS_2 (infinite-dim).  Bar Koszulness FAILS.

(5) SHADOW TOWER COLLAPSES: The MC element Theta_A = 0 because both
    kappa = 0 (uncurved) AND the critical-level algebra is commutative.
    The entire shadow obstruction tower is trivial (AP31).

(6) AVERAGING MAP DEGENERATES: The averaging map av: g^{E1}_A -> g^{mod}_A
    satisfies av(r(z)) = kappa at degree 2 for abelian algebras.  For
    non-abelian KM (trace-form): av(r(z)) = k*dim(g)/(2*h^v) = kappa_dp.
    The full kappa includes the Sugawara shift: kappa = kappa_dp + dim(g)/2.
    At critical level: kappa_dp = 0 * 3/4 = 0, but kappa = 0 + 3/2 = 3/2?
    NO: kappa(V_{-2}(sl_2)) = 3*0/4 = 0.  The Sugawara shift is dim(g)/2
    = 3/2 ONLY at generic level; at critical level the Sugawara element
    is undefined and the shift mechanism breaks.  kappa = 0 exactly.

    ker(av) at arity n: at generic level, dim ker(av_n|V^{tensor n})
    = d^n - C(n+d-1, d-1) where d = dim(V).  This formula depends only
    on d = dim(V), not on k.  So ker(av) on the REPRESENTATION side is
    level-independent.  But the ALGEBRAIC effect of ker(av) changes:
    at generic level, kappa != 0 forces curvature and the shadow tower
    carries information; at critical level, kappa = 0 and the averaged
    image is trivial.

ORDERED CHIRAL HOMOLOGY AT CRITICAL LEVEL
==========================================

The ordered chiral homology H_*^{ord}(E_tau, V_{-2}(sl_2)) at arity n
on an elliptic curve E_tau is computed by the ordered bar complex
tensored with the de Rham complex of Conf_n^{ord}(E_tau), twisted by
the KZB local system.

CRITICAL PHENOMENON: The KZB connection at k = -2 has IRREGULAR
singularity.  The connection form nabla = d - r(z) dz with
r(z) = Omega/((k+2)*z) DIVERGES.  This changes the de Rham cohomology:

  At generic k (regular singular):
    - Monodromy is a well-defined representation of pi_1
    - Local system is determined by monodromy
    - de Rham cohomology = Betti cohomology with local coefficients

  At critical k = -2 (irregular singular):
    - The connection has an essential singularity at z = 0
    - Stokes phenomenon occurs
    - The local system picture breaks down
    - Must use IRREGULAR de Rham theory (Deligne, Malgrange, Sabbah)

However, the ORDERED bar complex approach provides an alternative:
the bar differential d_k = d_crit + (k+2)*delta decomposes, and at
k = -2 only d_crit survives.  The bar complex with d_crit computes
Omega^*(Op) at arity 0.

ARITY-BY-ARITY ANALYSIS AT CRITICAL LEVEL
==========================================

n=0: The center Z(V_{-2}(sl_2)) = Fun(Op) = C[S_2].
     Graded pieces: dim_w = number of partitions of w into parts of size 2
     = floor(w/2) + 1 for even w, 0 for odd w.
     Wait: S_2 has weight 2, so Fun(Op) = C[S_2] with dim_w = 1 if w even
     (namely S_2^{w/2}), 0 if w odd.
     Generating function: 1/(1-q^2).

n=1: H^*(E_tau) tensor s^{-1}(bar cohomology).
     At generic level: s^{-1}g = C^3 (three generators at weight 1).
     At critical level: the bar cohomology H^*(B) = Omega^*(Op) is
     infinite-dimensional.  The arity-1 ordered chiral homology involves
     H^*(E_tau, V_{-2}(sl_2)^bar) where V_{-2}(sl_2)^bar = ker(epsilon).
     The E_1 bar complex at arity 1 is s^{-1}(V_{-2}(sl_2)^bar),
     which at critical level has cohomology = s^{-1}(Omega^*(Op) shifted).
     BUT: the arity-1 computation uses the UNIVERSAL bar complex of the
     VERTEX ALGEBRA V_k(sl_2), not the quotient by the center.
     At arity 1, the ordered chiral homology is:
       H^*_{ord,1}(E_tau, V_{-2}(sl_2))
       = H^*(E_tau) tensor H^1(B(V_{-2}(sl_2)))
       = H^*(E_tau) tensor {s^{-1}g + critical corrections}

     Key subtlety: H^1(B(V_k(sl_2))) at generic level = s^{-1}g = C^3
     (Koszul concentration).  At critical level, H^1(B) is PART of
     Omega^*(Op), specifically the degree-1 forms.  But the CE computation
     from bar_cohomology_sl2_explicit_engine.py shows H^1 = C^3 at
     weight 1 for ALL k (the PBW spectral sequence E_2 page is
     k-independent).  The critical-level change is that H^0 != C
     (it is Fun(Op)) and the higher bar cohomology is nontrivial.

     Conclusion: at arity 1, dim = 3 * 4 = 12 for the weight-1 contribution
     (level-independent).  But there are ADDITIONAL contributions from the
     infinite-dimensional H^0(B) = Fun(Op) piece at higher weights.

n=2: At generic level, the KZB local system on E_tau \\ {0} has rank 4
     (= dim V^{tensor 2} = 2^2) with regular singularity.
     At critical level, the singularity becomes IRREGULAR.
     The ordered configuration space Conf_2^{ord}(E_tau) = E_tau \\ {0}
     (one puncture from the collision diagonal).
     The irregular connection changes the de Rham cohomology dramatically.

n>=3: chi(Conf_n^{ord}(E_tau)) = 0 for n >= 1 (topological).
     The rank of the local system at generic level is 2^n.
     At critical level: irregular de Rham theory.

Conventions
-----------
- Cohomological grading (|d| = +1)
- Bar uses desuspension: |s^{-1}v| = |v| - 1 (AP45)
- kappa(V_k(sl_2)) = 3*(k+2)/4 (AP1; k=0 -> 3/2, k=-2 -> 0)
- B(A) = T^c(s^{-1} A-bar), A-bar = ker(epsilon) (AP132)
- r-matrix trace-form: r(z) = k*Omega/z (AP126; k=0 -> r=0)
- r-matrix KZ form: r(z) = Omega/((k+2)*z) (AP148; k=-2 -> DIVERGES)
- Sugawara: T = (1/(2*(k+2))) sum :J^a J^a: (UNDEFINED at k=-2)
- FF center: Z(V_{-2}(sl_2)) = C[S_2], S_2 = Sugawara limit = oper

References
----------
  Feigin-Frenkel (1992), "Affine Kac-Moody algebras at the critical level
    and Gelfand-Dikii algebras"
  Frenkel (2005), "Wakimoto modules, opers and the center at critical level"
  Gaitsgory-Raskin (2024), arXiv:2405.03648, "The FLE"
  Frenkel-Teleman (2006), "Self-extensions of Verma modules ..."
  Bernard (1988), "On the WZW models on the torus"
  thm:oper-bar-dl, thm:km-bar-bicomplex (this monograph)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union


# =========================================================================
# 0.  Lie algebra constants for sl_2
# =========================================================================

SL2_DIM = 3
SL2_RANK = 1
SL2_H_VEE = 2  # dual Coxeter number of sl_2
SL2_EXPONENTS = (1,)  # exponents of sl_2
SL2_OPER_GEN_WEIGHTS = (2,)  # oper generators at weight d_i + 1 = 2
SL2_FUND_DIM = 2  # dim of fundamental representation V = C^2


def kappa_sl2(k: Union[int, float, Fraction]) -> Union[float, Fraction]:
    r"""Modular characteristic kappa(V_k(sl_2)) = dim(sl_2)*(k+h^v)/(2*h^v).

    = 3*(k+2)/4.

    AP1: kappa is family-specific; verified:
      k=0  -> 3*2/4 = 3/2   (NOT zero)
      k=-2 -> 3*0/4 = 0     (critical level)
      k=1  -> 3*3/4 = 9/4   (integrable level 1)
    """
    if isinstance(k, Fraction):
        return Fraction(SL2_DIM) * (k + SL2_H_VEE) / (2 * SL2_H_VEE)
    return SL2_DIM * (k + SL2_H_VEE) / (2.0 * SL2_H_VEE)


def central_charge_sl2(k: Union[int, float, Fraction]) -> Union[float, Fraction]:
    r"""Central charge c(V_k(sl_2)) = 3k/(k+2).

    Sugawara formula; UNDEFINED (pole) at k = -2.
    """
    if isinstance(k, Fraction):
        denom = k + 2
        if denom == 0:
            return None  # undefined at critical level
        return Fraction(3) * k / denom
    if abs(k + 2) < 1e-15:
        return None  # pole
    return 3.0 * k / (k + 2)


def koszul_dual_level_sl2(k: Union[int, float, Fraction]
                          ) -> Union[float, Fraction]:
    r"""Feigin-Frenkel involution: k' = -k - 2h^v = -k - 4.

    At critical level k = -2: k' = 2 - 4 = -2 (FIXED POINT).
    """
    return -k - 2 * SL2_H_VEE


# =========================================================================
# 1.  Feigin-Frenkel center at critical level
# =========================================================================

def ff_center_dim_sl2(weight: int) -> int:
    r"""Dimension of the FF center Z(V_{-2}(sl_2)) at conformal weight w.

    Z(V_{-2}(sl_2)) = Fun(Op_{sl_2}(D)) = C[S_2]
    where S_2 has conformal weight 2.

    dim_w = 1 if w >= 0 and w is even, else 0.
    Generating function: 1/(1-q^2) = 1 + q^2 + q^4 + ...

    VERIFIED: [DC] C[S_2] is polynomial in one variable of weight 2;
    monomials S_2^m have weight 2m, so dim_{2m} = 1, dim_{odd} = 0.
    [LT] Frenkel (2005), "Wakimoto modules, opers and the center at
    critical level", Theorem 9.5.2.
    """
    if weight < 0:
        return 0
    if weight % 2 != 0:
        return 0
    return 1


def ff_center_hilbert_series(max_weight: int) -> Dict[int, int]:
    r"""Hilbert series of Z(V_{-2}(sl_2)) = C[S_2] up to weight max_weight.

    Returns dict: weight -> dimension.
    """
    return {w: ff_center_dim_sl2(w) for w in range(max_weight + 1)}


def ff_center_total_dim(max_weight: int) -> int:
    r"""Total dimension of Z(V_{-2}(sl_2)) up to weight max_weight.

    = floor(max_weight/2) + 1.
    """
    return sum(ff_center_dim_sl2(w) for w in range(max_weight + 1))


# =========================================================================
# 2.  Bar cohomology at critical level: H^*(B) = Omega^*(Op)
# =========================================================================

def bar_cohom_critical_sl2(bar_deg: int, weight: int) -> int:
    r"""H^n(B(V_{-2}(sl_2))) at bar degree n and conformal weight w.

    By thm:oper-bar-dl:
        H^n(B(V_{-2}(sl_2))) = Omega^n(Op_{sl_2}(D))

    For sl_2: rank = 1, one oper generator S_2 of weight 2.
    Op = Spec C[S_2], so Omega^1(Op) = C[S_2] * dS_2.

    H^0 = Fun(Op) = C[S_2]:
        dim_{w} = 1 if w even and w >= 0, else 0.

    H^1 = Omega^1(Op) = C[S_2] * dS_2:
        dS_2 has weight 2 (the oper generator has weight 2, so its
        de Rham differential inherits weight 2).
        dim_{w} = 1 if w even and w >= 2, else 0.
        Equivalently: the free C[S_2]-module on dS_2.

    H^n = 0 for n >= 2 (rank 1, so Omega^n = 0 for n > 1).

    CROSS-CHECK: At generic level k != -2, H^1(B) = C^3 at weight 1,
    H^n = 0 for n != 1.  At critical level, H^1 is infinite-dimensional
    and H^0 is also infinite-dimensional.

    VERIFIED: [DC] Omega^*(Spec C[x]) = C[x] in degree 0, C[x]dx in
    degree 1, zero in higher degrees.  Weight of dx = weight of x = 2.
    [LT] Frenkel-Teleman (2006), Theorem 1.1.
    """
    if bar_deg < 0 or bar_deg > SL2_RANK:
        return 0
    if weight < 0:
        return 0

    if bar_deg == 0:
        # H^0 = Fun(Op) = C[S_2]
        return ff_center_dim_sl2(weight)

    if bar_deg == 1:
        # H^1 = Omega^1(Op) = C[S_2] * dS_2
        # dS_2 has weight 2, S_2^m * dS_2 has weight 2m + 2
        # So dim_{w} = 1 if w >= 2 and w even, else 0
        if weight < 2:
            return 0
        if weight % 2 != 0:
            return 0
        return 1

    return 0


def bar_cohom_critical_total(max_weight: int) -> Dict[Tuple[int, int], int]:
    r"""Full bigraded table H^n(B(V_{-2}(sl_2)))_{w} for n in {0,1}, w <= max_weight."""
    result = {}
    for n in range(SL2_RANK + 1):
        for w in range(max_weight + 1):
            d = bar_cohom_critical_sl2(n, w)
            if d > 0:
                result[(n, w)] = d
    return result


def bar_cohom_generic_sl2(bar_deg: int, weight: int) -> int:
    r"""H^n(B(V_k(sl_2))) at generic level (k != -2).

    By Koszulness: concentrated at bar degree 1, weight 1.
    H^1 = s^{-1}g = C^3 at weight 1.
    H^n = 0 for n != 1.
    H^0 = C (vacuum) at weight 0.

    Actually: H^0 = C at weight 0 is the augmentation, not bar cohomology.
    Bar cohomology of the augmentation ideal: H^1 = C^3, H^n = 0 for n >= 2.

    The CE computation (bar_cohomology_sl2_explicit_engine.py) shows:
    H^n is concentrated at weight n(n+1)/2 with dim 2n+1.
    But this is the CE cohomology of g_-, which equals bar cohomology
    by PBW degeneration.  At generic level, the PBW spectral sequence
    collapses, giving Koszul concentration at n=1.

    For the FULL H^* at generic level (NOT just Koszul-relevant):
    H^1 = C^3 at weight 1 (the Koszul dual generators).
    All higher H^n are also nonzero but are killed by the curvature.

    CORRECTION: at generic level, bar cohomology IS concentrated at n=1
    with dim = 3 (this is EXACTLY what Koszulness means).  The CE
    computation gives the E_2 page of the PBW spectral sequence,
    which collapses to the bar cohomology.  The result:
    H^1(B(V_k(sl_2))) = C^3 (weight 1) for k generic.
    H^n = 0 for n != 1 (Koszul concentration).

    Wait: H^0(B(A)) for an augmented algebra is always C (the vacuum).
    For the REDUCED bar complex: H^0 = 0, H^1 = C^3.
    """
    # Full bar complex (including augmentation)
    if bar_deg == 0 and weight == 0:
        return 1  # vacuum
    if bar_deg == 1 and weight == 1:
        return 3  # s^{-1}g at weight 1
    return 0


# =========================================================================
# 3.  KZ connection and the critical-level divergence
# =========================================================================

@dataclass
class KZCriticalAnalysis:
    """Analysis of the KZ connection at and near critical level."""
    k: Union[float, Fraction]
    # Connection data
    kz_denominator: Union[float, Fraction]  # k + h^v = k + 2
    kz_diverges: bool
    # r-matrix data (trace-form convention: r(z) = k * Omega / z)
    r_matrix_level_prefix: Union[float, Fraction]
    r_matrix_vanishes_at_k0: bool
    # Sugawara data
    sugawara_denominator: Union[float, Fraction]  # 2*(k + h^v)
    sugawara_defined: bool
    # Curvature
    kappa: Union[float, Fraction]
    bar_uncurved: bool
    # Spectral sequence
    bicomplex_lambda: Union[float, Fraction]  # k + h^v
    d_crit_only: bool


def kz_critical_analysis(k: Union[int, float, Fraction]) -> KZCriticalAnalysis:
    r"""Analyze the KZ connection at level k for sl_2.

    KZ convention (AP148/C9): r(z) = Omega / ((k+h^v) * z) = Omega / ((k+2) * z).
    At k = -2: denominator = 0, connection DIVERGES.

    Trace-form convention (AP126): r(z) = k * Omega / z.
    At k = -2: r(z) = -2 * Omega / z (finite, nonzero).
    At k = 0: r(z) = 0 (vanishes, AP141 check passes).

    The trace-form r-matrix does NOT diverge at critical level.
    The KZ form diverges because it absorbs the Sugawara normalization
    1/(k+h^v) into the connection.  The divergence signals the breakdown
    of the Sugawara construction, not of the OPE.

    The OPE J^a(z) J^b(w) ~ k*(a,b)/(z-w)^2 + [a,b]^c J_c(w)/(z-w)
    is perfectly well-defined at k = -2.  The double pole has coefficient
    k = -2 (nonzero).  The simple pole has structure constants f^{ab}_c
    (level-independent).  What breaks is the SUGAWARA construction
    T = (1/(2(k+2))) sum :J^a J^a:, not the OPE.
    """
    kf = Fraction(k) if isinstance(k, int) else k
    h_vee = Fraction(SL2_H_VEE)

    kz_denom = kf + h_vee
    sug_denom = 2 * (kf + h_vee)
    lam = kf + h_vee
    kap = kappa_sl2(kf)

    is_crit = (kz_denom == 0) if isinstance(kz_denom, Fraction) else abs(float(kz_denom)) < 1e-15

    return KZCriticalAnalysis(
        k=kf,
        kz_denominator=kz_denom,
        kz_diverges=is_crit,
        r_matrix_level_prefix=kf,
        r_matrix_vanishes_at_k0=(kf == 0) if isinstance(kf, Fraction) else abs(float(kf)) < 1e-15,
        sugawara_denominator=sug_denom,
        sugawara_defined=not is_crit,
        kappa=kap,
        bar_uncurved=is_crit,
        bicomplex_lambda=lam,
        d_crit_only=is_crit,
    )


# =========================================================================
# 4.  Averaging map at critical level
# =========================================================================

def ker_av_dim(d: int, n: int) -> int:
    r"""Dimension of ker(av_n) on V^{tensor n} for dim(V) = d.

    ker(av_n) = d^n - C(n+d-1, d-1).

    This formula depends ONLY on d = dim(V), not on the level k.
    The kernel of the Reynolds averaging map is a representation-theoretic
    quantity, not an algebraic one.

    VERIFIED: [DC] Reynolds projector image = Sym^n(V), dim = C(n+d-1,d-1)
    [SY] formula is Sigma_n-representation-theoretic, level-independent.
    """
    if d < 1 or n < 1:
        return 0
    return d ** n - math.comb(n + d - 1, d - 1)


def averaging_analysis_critical(max_arity: int = 8) -> Dict[str, Any]:
    r"""Analyze the averaging map av: g^{E1} -> g^{mod} at critical level.

    KEY INSIGHT: The averaging map av has TWO components:

    (A) REPRESENTATION-LEVEL av: the Reynolds projector
        V^{tensor n} -> Sym^n(V), kernel dim = d^n - C(n+d-1,d-1).
        This is LEVEL-INDEPENDENT (depends only on dim V = 2).

    (B) ALGEBRAIC-LEVEL av: the map av(r(z)) gives the degree-2 scalar shadow.
        For non-abelian KM (trace-form): av(r(z)) = k*dim(g)/(2*h^v).
        Full kappa = av(r) + dim(g)/2 (Sugawara shift, C13).
        At critical level k = -2:
          av(r(z)) = (-2)*3/4 = -3/2   (trace-form average of double pole)
          Sugawara shift = 3/2          (UNDEFINED at critical level!)
          kappa = av(r) + shift = -3/2 + 3/2 = 0  (IF Sugawara were valid)

        The resolution: at critical level, kappa = 0 by direct computation
        kappa = dim(g)*(k+h^v)/(2*h^v) = 3*0/4 = 0.  The two terms
        (-3/2 and +3/2) that cancel at generic level become separately
        ill-defined at critical level (the Sugawara shift requires
        k+h^v != 0), but their SUM is well-defined as a limit: kappa -> 0.

    CONSEQUENCE FOR ker(av):
        At generic level: ker(av) at degree 2 carries the ORDERED data
        that is lost when projecting r(z) -> kappa.  This kernel has
        dim = d^2 - d*(d+1)/2 = d*(d-1)/2 = 1 for d=2.
        (The antisymmetric part of V tensor V.)

        At critical level: kappa = 0, so the averaged image is TRIVIAL.
        The entire convolution algebra g^{mod} at degree 2 vanishes.
        But g^{E1} at degree 2 is NONTRIVIAL (the r-matrix r(z) = -2*Omega/z
        is nonzero in trace-form).  So the kernel of av is LARGER in the
        algebraic sense: it now includes the entire ordered data, not just
        the antisymmetric part.

        More precisely: at generic level, the full kappa = av(r(z)) + dim(g)/2
        is nonzero, so the
        ordered datum r(z) projects to a nonzero scalar kappa.  The kernel
        of av at the algebraic level is the "shape" of r(z) modulo its
        scalar average.  At critical level, kappa = 0 and the entire
        r-matrix data lives in ker(av) in the algebraic sense.
    """
    d = SL2_FUND_DIM  # dim V = 2

    arity_data = {}
    for n in range(1, max_arity + 1):
        total = d ** n
        sym = math.comb(n + d - 1, d - 1)
        kernel = total - sym
        ratio = Fraction(kernel, total)

        arity_data[n] = {
            'total_dim': total,
            'sym_dim': sym,
            'ker_dim': kernel,
            'ratio': ratio,
            'ratio_float': float(ratio),
        }

    # Algebraic-level analysis at critical level
    k_crit = Fraction(-2)
    kappa_crit = kappa_sl2(k_crit)
    # Trace-form: r(z) = k * Omega / z = -2 * Omega / z at critical level
    r_matrix_coefficient = k_crit  # = -2

    # Average of double-pole channel at critical level
    # av(r(z)) = k * dim(g) / (2 * h^v) = (-2) * 3 / 4 = -3/2
    # This is the kappa_dp (double-pole channel contribution)
    kappa_dp = r_matrix_coefficient * SL2_DIM / (2 * SL2_H_VEE)

    return {
        'fundamental_dim': d,
        'arity_data': arity_data,
        'critical_level': int(k_crit),
        'kappa_critical': float(kappa_crit),
        'kappa_is_zero': kappa_crit == 0,
        'r_matrix_coefficient_critical': float(r_matrix_coefficient),
        'r_matrix_nonzero_at_critical': r_matrix_coefficient != 0,
        'kappa_dp_critical': float(kappa_dp),
        'sugawara_shift': Fraction(SL2_DIM, 2),
        'sugawara_shift_float': SL2_DIM / 2.0,
        'sugawara_defined_at_critical': False,
        'kappa_as_limit': 'lim_{k->-2} kappa(k) = 0 (well-defined as limit)',
        'algebraic_ker_av_grows': True,
        'reason': (
            'At critical level kappa = 0: the averaged image of r(z) in '
            'g^{mod} is zero.  The entire r-matrix datum r(z) = -2*Omega/z '
            'lives in ker(av) algebraically, even though the representation-'
            'theoretic ker(av) is level-independent.'
        ),
    }


# =========================================================================
# 5.  Ordered chiral Hochschild at critical level: arity-by-arity
# =========================================================================

@dataclass
class CriticalArityData:
    """Data at a single arity for ordered chiral homology at critical level."""
    arity: int
    # Generic level data (for comparison)
    generic_description: str
    generic_dim: Optional[int]
    # Critical level data
    critical_description: str
    critical_dim: Optional[int]  # None if infinite
    critical_infinite: bool
    # Euler characteristic
    euler_char: Optional[int]
    # Local system data
    local_system_regular: bool  # True at generic, False at critical
    local_system_rank_generic: Optional[int]
    # Structural notes
    notes: str


def ordered_chirhoch_arity0_critical() -> CriticalArityData:
    r"""Arity 0: the center.

    Generic: Z(V_k(sl_2)) = C (scalars).  dim = 1.
    Critical: Z(V_{-2}(sl_2)) = C[S_2] = Fun(Op_{sl_2}(D)).  dim = infinity.

    The center JUMP at critical level is the Feigin-Frenkel phenomenon.
    It is the single most dramatic structural change.
    """
    return CriticalArityData(
        arity=0,
        generic_description='Z(V_k(sl_2)) = C (scalars)',
        generic_dim=1,
        critical_description=(
            'Z(V_{-2}(sl_2)) = Fun(Op_{sl_2}(D)) = C[S_2], '
            'polynomial algebra on one generator of weight 2'),
        critical_dim=None,
        critical_infinite=True,
        euler_char=None,
        local_system_regular=True,
        local_system_rank_generic=None,
        notes=(
            'CENTER JUMP: the single most dramatic structural change at '
            'critical level.  From dim 1 (generic) to infinite (critical).  '
            'Source: Feigin-Frenkel center = functions on opers.'
        ),
    )


def ordered_chirhoch_arity1_critical() -> CriticalArityData:
    r"""Arity 1: generators.

    Generic: H^*(E_tau) tensor s^{-1}g = C^4 tensor C^3 = C^12.
    The 3 comes from H^1(B(V_k(sl_2))) = s^{-1}g at weight 1.
    dim = 12 (level-independent for the weight-1 contribution).

    Critical: The bar cohomology H^*(B(V_{-2}(sl_2))) has
    H^0 = C[S_2] (infinite) and H^1 = C[S_2]*dS_2 (infinite).
    The arity-1 ordered chiral homology involves BOTH H^0 and H^1
    of the bar complex, tensored with H^*(E_tau).

    The weight-1 contribution (from H^1 at weight 1) gives the same
    C^3 tensor H^*(E_tau) = C^12 as generic level.  But additional
    contributions from higher weights in H^0 and H^1 make the total
    infinite-dimensional.

    The weight-1 piece of H^1(B) at critical level:
    H^1(B)_{w=1} = Omega^1(Op)_{w=1} = 0 (since dS_2 has weight 2,
    the minimum weight in Omega^1 is 2).

    CORRECTION: At critical level, H^1 has DIFFERENT weight support
    than at generic level!  At generic level, H^1 = C^3 at weight 1
    (from the Koszul dual generators s^{-1}e, s^{-1}h, s^{-1}f).
    At critical level, Omega^1(Op)_{w=1} = 0.

    This means the arity-1 ordered chiral homology at critical level
    does NOT have the familiar C^12 at weight 1.  Instead:
    - From H^0(B) = C[S_2]: contributes C^4 at weight 0 (vacuum),
      C^0 at weight 1 (no odd-weight elements in C[S_2]).
    - From H^1(B) = C[S_2]*dS_2: first contribution at weight 2.

    Wait: this analysis conflates bar cohomology of V_{-2}(sl_2) with
    bar cohomology of the CE complex of g_-.

    RESOLUTION: The bar cohomology H^*(B(V_k(sl_2))) is computed by
    the PBW spectral sequence.  The E_2 page is H^*_{CE}(g_-, C).
    At GENERIC level, the spectral sequence collapses at E_2 and
    H^1 = C^3 (weight 1).  At CRITICAL level, the spectral sequence
    STILL collapses at E_2 (Whitehead), but the ABUTMENT changes:
    there are additional classes in H^0 from the FF center that are
    NOT visible in the CE cohomology of g_-.

    The key distinction: H^*_{CE}(g_-, C) is the SAME at all levels
    (k-independent, as proved in bar_cohomology_sl2_explicit_engine.py).
    But the bar cohomology of V_k(sl_2) (the FULL vertex algebra, not
    just the loop algebra) differs at critical level because the FF
    center contributes additional H^0 classes.

    For the ORDERED chiral homology at arity 1, the relevant input is
    the vertex algebra bar complex, not just the CE complex.

    At generic level: H^1(B(V_k)) = C^3 (weight 1), H^0 = C.
    At critical level: H^0(B(V_{-2})) = C[S_2] (infinite),
    H^1(B(V_{-2})) includes C[S_2]*dS_2 plus the CE H^1 = C^3.

    Arity-1 ordered chiral homology = H^*(E_tau) tensor H^*(B(V_k))
    (the bar complex provides the coefficient sheaf).

    Critical-level total: infinite (from the infinite H^0 = C[S_2]).
    """
    return CriticalArityData(
        arity=1,
        generic_description='H*(E_tau) tensor s^{-1}g = C^12',
        generic_dim=12,
        critical_description=(
            'H*(E_tau) tensor H*(B(V_{-2}(sl_2))): the bar cohomology '
            'includes H^0 = C[S_2] (infinite) and H^1 contributions.  '
            'The weight-1 piece (CE H^1 = C^3) persists, but additional '
            'infinite-dimensional contributions from FF center appear.'),
        critical_dim=None,
        critical_infinite=True,
        euler_char=0,  # chi(E_tau) = 0
        local_system_regular=True,  # arity 1: no collision, no singularity
        local_system_rank_generic=SL2_FUND_DIM,
        notes=(
            'The CE cohomology H^1_{CE}(g_-, C) = C^3 at weight 1 is '
            'level-independent and persists at critical level.  The new '
            'phenomenon is the infinite-dimensional H^0 = C[S_2] from '
            'the Feigin-Frenkel center, which contributes to arity 1 '
            'through the bar complex augmentation.'
        ),
    )


def ordered_chirhoch_arity2_critical() -> CriticalArityData:
    r"""Arity 2: the critical-level KZB singularity.

    Generic: The KZB local system on E_tau \\ {0} has rank 4 = dim(V^{tensor 2}).
    The connection nabla_KZ = d - Omega/((k+2)*z) dz has REGULAR singularity
    at z = 0 with monodromy exp(2*pi*i*Omega/(k+2)).
    chi(E_tau \\ {0}) = -1, so chi(H^*) = rank * chi = 4 * (-1) = -4.
    H^0 = 0 (nontrivial monodromy), H^2 = 0 (open surface), H^1 = C^4.

    Critical (k = -2): The KZ connection Omega/((k+2)*z) DIVERGES.
    In the KZ convention, the connection has a pole of order 1 with
    residue Omega/(k+2) -> infinity.  This is an IRREGULAR singularity.

    In the trace-form convention: r(z) = k*Omega/z = -2*Omega/z.
    The connection 1-form is r(z)*dz = -2*Omega*dz/z, which is a
    regular singular connection with residue -2*Omega.  The eigenvalues
    of -2*Omega on V tensor V are:
      -2 * (1/2) = -1   on Sym^2(V) (Casimir eigenvalue 1/2)
      -2 * (-3/2) = 3   on wedge^2(V) (Casimir eigenvalue -3/2)

    Monodromy: M = exp(2*pi*i * (-2*Omega))
      On Sym^2: exp(2*pi*i*(-1)) = exp(-2*pi*i) = 1  (TRIVIAL!)
      On wedge^2: exp(2*pi*i*3) = exp(6*pi*i) = 1    (TRIVIAL!)

    At critical level in the trace-form convention, the A-cycle monodromy
    is TRIVIAL (all eigenvalues are integers, giving exp(2*pi*i*n) = 1).

    This means: H^0 of the local system is NONZERO at critical level
    (monodromy-invariant sections exist).

    chi(E_tau \\ {0}, V^{tensor 2}) = rank * chi(E_tau \\ {0}) = 4*(-1) = -4.
    H^0 = dim(monodromy invariants).

    On Sym^2(V): M = I, so invariants = all of Sym^2 = C^3.
    On wedge^2(V): M = I, so invariants = all of wedge^2 = C^1.
    Total H^0 = 3 + 1 = 4.

    H^2 = 0 (open surface, no compactly supported cohomology in top degree
    for a punctured torus).

    chi = H^0 - H^1 + H^2 = 4 - H^1 + 0 = -4, so H^1 = 8.

    DRAMATIC CHANGE: at generic level, H^0 = 0, H^1 = 4.
    At critical level, H^0 = 4, H^1 = 8.
    The total dimension DOUBLES from 4 to 12.

    NOTE: This analysis uses the trace-form convention for the connection.
    In the KZ convention, the connection diverges and requires regularization.
    The trace-form analysis gives the correct finite answer because the
    vertex algebra OPE is well-defined at critical level.
    """
    # Casimir eigenvalues on V tensor V for sl_2
    casimir_sym = Fraction(1, 2)   # Omega|_{Sym^2(C^2)} = 1/2
    casimir_alt = Fraction(-3, 2)  # Omega|_{wedge^2(C^2)} = -3/2

    # Residue of trace-form connection: -2 * Omega
    k_crit = Fraction(-2)
    res_sym = k_crit * casimir_sym   # = -2 * 1/2 = -1
    res_alt = k_crit * casimir_alt   # = -2 * (-3/2) = 3

    # A-cycle monodromy: exp(2*pi*i * residue)
    # For residue = integer n: exp(2*pi*i*n) = 1
    mono_sym_trivial = (res_sym.denominator == 1)   # -1 is integer
    mono_alt_trivial = (res_alt.denominator == 1)    # 3 is integer

    # H^0 = monodromy invariants
    dim_sym2 = SL2_FUND_DIM * (SL2_FUND_DIM + 1) // 2  # = 3
    dim_alt2 = SL2_FUND_DIM * (SL2_FUND_DIM - 1) // 2  # = 1
    H0_sym = dim_sym2 if mono_sym_trivial else 0
    H0_alt = dim_alt2 if mono_alt_trivial else 0
    H0 = H0_sym + H0_alt

    # chi(E_tau \\ {0}) = chi(E_tau) - 1 = 0 - 1 = -1
    chi_base = -1
    rank = SL2_FUND_DIM ** 2  # = 4
    chi_total = rank * chi_base  # = -4

    # H^2 = 0 (punctured surface)
    H2 = 0

    # H^1 from chi = H^0 - H^1 + H^2
    H1 = H0 - chi_total - H2  # H0 - chi = H0 + 4

    return CriticalArityData(
        arity=2,
        generic_description=(
            f'KZB local system on E_tau \\\\ {{0}}, rank {rank}, '
            f'H^0=0, H^1=4, H^2=0, chi=-4'),
        generic_dim=4,
        critical_description=(
            f'Trace-form connection -2*Omega*dz/z: monodromy TRIVIAL '
            f'(residue eigenvalues {int(res_sym)}, {int(res_alt)} are integers).  '
            f'H^0={H0}, H^1={H1}, H^2={H2}, chi={chi_total}.  '
            f'Dimension DOUBLES from 4 to {H0 + H1 + H2}.'),
        critical_dim=H0 + H1 + H2,
        critical_infinite=False,
        euler_char=chi_total,
        local_system_regular=False,  # KZ convention diverges
        local_system_rank_generic=rank,
        notes=(
            f'The trace-form connection is regular singular at critical level '
            f'with integer residue eigenvalues ({int(res_sym)}, {int(res_alt)}), '
            f'giving TRIVIAL monodromy.  This is the critical-level analogue '
            f'of the integrable-level finite monodromy phenomenon, but more '
            f'extreme: ALL monodromy is trivial, not just finite-order.  '
            f'H^0 jumps from 0 to {H0}, H^1 from 4 to {H1}.'
        ),
    )


def ordered_chirhoch_arity_n_critical(n: int) -> CriticalArityData:
    r"""Arity n >= 3: higher ordered chiral homology at critical level.

    The ordered configuration space Conf_n^{ord}(E_tau) has
    chi(Conf_n^{ord}(E_tau)) = 0 for n >= 1 (topological invariant).

    At generic level: the KZB local system has rank 2^n.
    The monodromy is generically nontrivial, so H^0 contributes nothing
    and the Euler characteristic constraint chi = 0 forces H^1 = 0
    (since H^0 = H^2 = 0 on a punctured surface of chi = 0 ... no,
    this is wrong for n >= 3).

    Actually: Conf_n^{ord}(E_tau) for n >= 2 is a smooth variety of
    complex dimension n, obtained by removing diagonals from E_tau^n.
    Its Euler characteristic is n! * chi(Conf_n(E_tau)) where
    chi(Conf_n(E_tau)) = 0 for n >= 1 on a torus.

    At critical level: the monodromy of the trace-form connection
    around each collision diagonal is exp(2*pi*i * k * Omega_{ij})
    = exp(-4*pi*i * Omega_{ij}).  The eigenvalues of Omega_{ij} on
    V^{tensor n} decomposed by pairs {i,j} have Casimir eigenvalues
    1/2 and -3/2.  The exponentials exp(-4*pi*i * 1/2) = exp(-2*pi*i) = 1
    and exp(-4*pi*i * (-3/2)) = exp(6*pi*i) = 1 are BOTH trivial.

    So at critical level: ALL monodromy is trivial for ALL arities.
    The local system is TRIVIAL (isomorphic to the constant sheaf V^{tensor n}).
    """
    if n < 3:
        raise ValueError(f"Use specific arity function for n={n}")

    rank = SL2_FUND_DIM ** n

    # At critical level: trivial monodromy, so H^0 = V^{tensor n}
    # chi(Conf_n^{ord}(E_tau)) = 0
    # H^*(Conf_n^{ord}(E_tau), V^{tensor n}) with trivial coefficients
    # = H^*(Conf_n^{ord}(E_tau)) tensor V^{tensor n}

    # For n >= 2 on a torus: Conf_n^{ord}(E_tau) is the complement of
    # diagonals in E_tau^n.  With trivial local system:
    # chi = 0 (torus Euler char identity)
    # H^0 = C^{rank} (trivial local system)

    return CriticalArityData(
        arity=n,
        generic_description=(
            f'KZB on Conf_{n}^{{ord}}(E_tau), rank {rank}, chi=0, '
            f'nontrivial monodromy'),
        generic_dim=None,  # chi = 0, individual dims level-dependent
        critical_description=(
            f'TRIVIAL local system (all monodromy trivial): '
            f'H^*(Conf_{n}^{{ord}}(E_tau), C^{{{rank}}}) = '
            f'H^*(Conf_{n}^{{ord}}(E_tau)) tensor C^{{{rank}}}'),
        critical_dim=None,  # depends on Betti numbers of config space
        critical_infinite=False,
        euler_char=0,
        local_system_regular=False,
        local_system_rank_generic=rank,
        notes=(
            f'At critical level, the trace-form connection has integer '
            f'Casimir residues (-1 on Sym^2, +3 on wedge^2), so ALL '
            f'pairwise monodromy is trivial.  The local system becomes '
            f'constant.  The ordered chiral homology reduces to '
            f'H^*(Conf_{n}^{{ord}}(E_tau)) tensor V^{{tensor {n}}}.'
        ),
    )


# =========================================================================
# 6.  Critical-level limit analysis: k -> -2
# =========================================================================

@dataclass
class CriticalLimitData:
    """Data tracking the critical-level limit k -> -2."""
    k: float
    kappa: float
    c: Optional[float]
    kz_residue_sym: float    # residue on Sym^2 channel
    kz_residue_alt: float    # residue on wedge^2 channel
    mono_sym: complex        # A-cycle monodromy on Sym^2
    mono_alt: complex        # A-cycle monodromy on wedge^2
    mono_sym_order: Optional[int]  # order of monodromy (None if irrational)
    mono_alt_order: Optional[int]
    H0_arity2: int           # dimension of monodromy invariants
    H1_arity2: int           # from chi constraint


def critical_limit_sequence(n_points: int = 20) -> List[CriticalLimitData]:
    r"""Compute invariants along a sequence k -> -2.

    This tracks how the monodromy, Euler characteristics, and dimensions
    evolve as k approaches the critical level.

    The sequence uses k = -2 + 1/m for m = 1, 2, 3, ... (from above)
    and k = -2 - 1/m for m = 1, 2, 3, ... (from below).
    """
    results = []
    # Approach from above: k = -2 + 1/m
    for m in range(1, n_points + 1):
        k = -2.0 + 1.0 / m
        kap = kappa_sl2(k)
        c = central_charge_sl2(k)

        # Trace-form residues: k * Casimir
        res_sym = k * 0.5
        res_alt = k * (-1.5)

        # Monodromy: exp(2*pi*i * residue)
        mono_sym = cmath.exp(2j * math.pi * res_sym)
        mono_alt = cmath.exp(2j * math.pi * res_alt)

        # Order of monodromy
        def _order(z, max_n=1000):
            for n in range(1, max_n + 1):
                if abs(z ** n - 1.0) < 1e-10:
                    return n
            return None

        order_sym = _order(mono_sym)
        order_alt = _order(mono_alt)

        # H^0 at arity 2: monodromy invariants
        H0_sym = 3 if abs(mono_sym - 1.0) < 1e-10 else 0
        H0_alt = 1 if abs(mono_alt - 1.0) < 1e-10 else 0
        H0 = H0_sym + H0_alt

        # chi = -4, H^2 = 0
        H1 = H0 + 4  # from chi = H0 - H1 = -4

        results.append(CriticalLimitData(
            k=k, kappa=kap, c=c,
            kz_residue_sym=res_sym, kz_residue_alt=res_alt,
            mono_sym=mono_sym, mono_alt=mono_alt,
            mono_sym_order=order_sym, mono_alt_order=order_alt,
            H0_arity2=H0, H1_arity2=H1,
        ))

    return results


import cmath


def critical_limit_monodromy_analysis() -> Dict[str, Any]:
    r"""Analyze how monodromy degenerates as k -> -2.

    At k = -2 + epsilon:
    - Sym^2 residue: (-2 + eps) * 1/2 = -1 + eps/2
    - wedge^2 residue: (-2 + eps) * (-3/2) = 3 - 3*eps/2

    Monodromy:
    - Sym^2: exp(2*pi*i*(-1 + eps/2)) = exp(pi*i*eps)
    - wedge^2: exp(2*pi*i*(3 - 3*eps/2)) = exp(-3*pi*i*eps)

    As eps -> 0:
    - Both monodromy eigenvalues -> 1 (trivial)
    - The monodromy group degenerates from infinite (generic) to trivial
    - This is the OPPOSITE of the integrable-level phenomenon (where
      monodromy becomes finite but nontrivial)

    At integrable levels k = positive integer:
    - Monodromy is finite (roots of unity)
    - Fusion truncation occurs

    At critical level k = -2:
    - Monodromy is trivial (= 1)
    - FF center appears
    - These are related: trivial monodromy means MORE invariant sections,
      and the FF center provides the "extra" scalars.
    """
    # Compute monodromy at several nearby levels
    epsilons = [1.0, 0.5, 0.1, 0.01, 0.001, 0.0001, 0.0]
    data = []
    for eps in epsilons:
        k = -2.0 + eps
        res_sym = k * 0.5
        res_alt = k * (-1.5)

        if eps > 0:
            mono_sym = cmath.exp(2j * math.pi * res_sym)
            mono_alt = cmath.exp(2j * math.pi * res_alt)
        else:
            mono_sym = complex(1.0, 0.0)
            mono_alt = complex(1.0, 0.0)

        H0_sym = 3 if abs(mono_sym - 1.0) < 1e-10 else 0
        H0_alt = 1 if abs(mono_alt - 1.0) < 1e-10 else 0

        data.append({
            'epsilon': eps,
            'k': k,
            'kappa': kappa_sl2(k),
            'res_sym': res_sym,
            'res_alt': res_alt,
            'mono_sym_abs': abs(mono_sym),
            'mono_sym_arg': cmath.phase(mono_sym),
            'mono_alt_abs': abs(mono_alt),
            'mono_alt_arg': cmath.phase(mono_alt),
            'mono_sym_near_1': abs(mono_sym - 1.0),
            'mono_alt_near_1': abs(mono_alt - 1.0),
            'H0_arity2': H0_sym + H0_alt,
            'H1_arity2': H0_sym + H0_alt + 4,
        })

    return {
        'approach_data': data,
        'limiting_behavior': {
            'mono_sym_limit': 1.0,
            'mono_alt_limit': 1.0,
            'H0_limit': 4,
            'H1_limit': 8,
            'monodromy_trivial_at_critical': True,
        },
        'contrast_with_integrable': (
            'At integrable level k = positive integer: monodromy is finite '
            '(roots of unity), fusion truncates, center remains C.  '
            'At critical level k = -2: monodromy is trivial (= 1), '
            'no fusion truncation, but center JUMPS to C[S_2] (infinite).  '
            'These are opposite phenomena: integrable = finite monodromy + '
            'finite center; critical = trivial monodromy + infinite center.'
        ),
    }


# =========================================================================
# 7.  Structural comparison: generic vs critical vs integrable
# =========================================================================

@dataclass
class ThreeLevelComparison:
    """Comparison of generic, integrable, and critical level data."""
    # Kappa
    kappa_generic: str  # "3*(k+2)/4, nonzero"
    kappa_integrable_k1: float  # 9/4
    kappa_critical: float  # 0
    # Center
    center_generic: str
    center_integrable_k1: str
    center_critical: str
    # Bar cohomology
    bar_generic: str
    bar_integrable_k1: str
    bar_critical: str
    # Monodromy at arity 2
    mono_generic: str
    mono_integrable_k1: str
    mono_critical: str
    # H^0 at arity 2
    H0_generic: int
    H0_integrable_k1: int
    H0_critical: int
    # H^1 at arity 2
    H1_generic: int
    H1_integrable_k1: int
    H1_critical: int
    # Shadow tower
    shadow_generic: str
    shadow_integrable_k1: str
    shadow_critical: str
    # Koszulness
    koszul_generic: bool
    koszul_integrable_k1: bool
    koszul_critical: bool


def three_level_comparison() -> ThreeLevelComparison:
    r"""Compare the three characteristic levels for V_k(sl_2).

    (1) Generic level (k not special): Koszul, finite bar cohomology,
        nontrivial monodromy, finite center, nontrivial shadow tower.

    (2) Integrable level k = 1: finite monodromy (roots of unity),
        fusion truncation, center C, Koszul, nontrivial shadow tower.

    (3) Critical level k = -2: trivial monodromy, NO fusion truncation,
        center = C[S_2] (infinite), NOT Koszul, trivial shadow tower.
    """
    return ThreeLevelComparison(
        kappa_generic='3*(k+2)/4, nonzero for k != -2',
        kappa_integrable_k1=9.0 / 4,
        kappa_critical=0.0,
        center_generic='C (scalars)',
        center_integrable_k1='C (scalars, same as generic)',
        center_critical='C[S_2] = Fun(Op_{sl_2}(D)), infinite-dim',
        bar_generic='H^1 = C^3, H^n = 0 for n != 1 (Koszul)',
        bar_integrable_k1='H^1 = C^3, H^n = 0 for n != 1 (Koszul)',
        bar_critical='H^0 = C[S_2], H^1 = C[S_2]*dS_2 (NOT Koszul)',
        mono_generic='Infinite monodromy group (dense in U(n))',
        mono_integrable_k1='Finite monodromy (roots of unity, order | 6)',
        mono_critical='TRIVIAL monodromy (all eigenvalues = 1)',
        H0_generic=0,
        H0_integrable_k1=0,
        H0_critical=4,
        H1_generic=4,
        H1_integrable_k1=4,
        H1_critical=8,
        shadow_generic='Nontrivial: class L (affine), r_max = 3',
        shadow_integrable_k1='Nontrivial: kappa = 9/4, same class L',
        shadow_critical='TRIVIAL: Theta = 0 (commutativity, not just kappa=0)',
        koszul_generic=True,
        koszul_integrable_k1=True,
        koszul_critical=False,
    )


# =========================================================================
# 8.  Full critical-level analysis
# =========================================================================

@dataclass
class FullCriticalAnalysis:
    """Complete analysis of ordered chiral Hochschild at critical level."""
    # Basic data
    k: Fraction
    kappa: Fraction
    c: Optional[float]
    # KZ analysis
    kz_analysis: KZCriticalAnalysis
    # FF center
    ff_center_gen_func: str
    ff_center_dims: Dict[int, int]
    # Bar cohomology
    bar_cohom_table: Dict[Tuple[int, int], int]
    # Arity-by-arity
    arity_data: Dict[int, CriticalArityData]
    # Averaging
    averaging_analysis: Dict[str, Any]
    # Monodromy analysis
    monodromy_analysis: Dict[str, Any]
    # Three-level comparison
    comparison: ThreeLevelComparison


def full_critical_analysis(max_weight: int = 20,
                           max_arity: int = 5) -> FullCriticalAnalysis:
    r"""Compute the complete critical-level ordered chiral Hochschild analysis.

    This is the master function that assembles all components.
    """
    k_crit = Fraction(-2)
    kap = kappa_sl2(k_crit)
    c = central_charge_sl2(k_crit)

    # KZ analysis
    kz = kz_critical_analysis(k_crit)

    # FF center
    ff_dims = ff_center_hilbert_series(max_weight)

    # Bar cohomology
    bar_table = bar_cohom_critical_total(max_weight)

    # Arity-by-arity
    arity_data = {}
    arity_data[0] = ordered_chirhoch_arity0_critical()
    arity_data[1] = ordered_chirhoch_arity1_critical()
    arity_data[2] = ordered_chirhoch_arity2_critical()
    for n in range(3, max_arity + 1):
        arity_data[n] = ordered_chirhoch_arity_n_critical(n)

    # Averaging
    avg = averaging_analysis_critical()

    # Monodromy
    mono = critical_limit_monodromy_analysis()

    # Comparison
    comp = three_level_comparison()

    return FullCriticalAnalysis(
        k=k_crit,
        kappa=kap,
        c=c,
        kz_analysis=kz,
        ff_center_gen_func='1/(1-q^2)',
        ff_center_dims=ff_dims,
        bar_cohom_table=bar_table,
        arity_data=arity_data,
        averaging_analysis=avg,
        monodromy_analysis=mono,
        comparison=comp,
    )


# =========================================================================
# 9.  Bicomplex deformation: interpolation from critical to generic
# =========================================================================

def bicomplex_critical_to_generic(
    levels: Optional[List[Fraction]] = None,
) -> List[Dict[str, Any]]:
    r"""Track the bicomplex d_k = d_crit + (k+2)*delta from critical to generic.

    thm:km-bar-bicomplex: d_k = d_crit + lambda * delta where
    lambda = k + h^v = k + 2.

    d_crit: extracts simple-pole residues (structure constants [e,f]=h etc.)
    delta: extracts double-pole residues (level k bilinear form)

    d_crit^2 = 0, delta^2 = 0, {d_crit, delta} = 0 (anticommutator).

    The critical-first spectral sequence:
    E_0 = (B(V_k(sl_2)), d_crit)
    E_1 = H*(B, d_crit) = Omega^*(Op) (independent of k)
    d_1 = lambda * [delta] on E_1
    E_2 = H*(Omega^*(Op), lambda * [delta])

    At lambda = 0 (critical): E_1 = E_infinity = Omega^*(Op).
    At lambda != 0 (generic): the spectral sequence collapses at E_2
    to the Koszul dual (H^1 = C^3 concentrated at weight 1).
    """
    if levels is None:
        levels = [
            Fraction(-2),           # critical (lambda = 0)
            Fraction(-2, 1) + Fraction(1, 10),  # near-critical
            Fraction(-2, 1) + Fraction(1, 2),   # half-step
            Fraction(-1),           # one step (lambda = 1)
            Fraction(0),            # k = 0 (lambda = 2)
            Fraction(1),            # integrable k = 1 (lambda = 3)
        ]

    results = []
    for k in levels:
        lam = k + 2  # lambda = k + h^v = k + 2
        kap = kappa_sl2(k)
        is_crit = (lam == 0)

        # At the E_1 page: H*(B, d_crit) = Omega^*(Op) regardless of k.
        # The d_1 differential is lambda * [delta] on E_1.
        # For lambda = 0: d_1 = 0, so E_2 = E_1 = Omega^*(Op).
        # For lambda != 0: d_1 contracts the de Rham complex of Op,
        # killing all higher cohomology and leaving H^1 = C^3.

        results.append({
            'k': float(k),
            'lambda': float(lam),
            'kappa': float(kap),
            'is_critical': is_crit,
            'E1_page': 'Omega^*(Op_{sl_2}(D))',
            'd1_differential': f'{float(lam)} * [delta]',
            'd1_zero': is_crit,
            'E2_page': (
                'Omega^*(Op) (full de Rham, no contraction)'
                if is_crit else
                'C^3 at bar degree 1, weight 1 (Koszul concentration)'
            ),
            'bar_koszul': not is_crit,
            'bar_cohom_h0_dim': ('infinite (C[S_2])' if is_crit else '1 (C)'),
            'bar_cohom_h1_dim': ('infinite (C[S_2]*dS_2)' if is_crit else '3'),
            'interpretation': (
                'Critical level: d_1 = 0, spectral sequence degenerates at E_1. '
                'The full de Rham algebra of Op survives as bar cohomology. '
                'This is the algebraic shadow of the Feigin-Frenkel center.'
                if is_crit else
                f'Generic level (lambda = {float(lam)}): d_1 contracts the '
                f'de Rham complex, leaving only H^1 = C^3 (Koszul dual = '
                f's^{{-1}}sl_2).'
            ),
        })

    return results


# =========================================================================
# 10.  Summary table
# =========================================================================

def summary_table() -> str:
    r"""Generate a human-readable summary table of the critical-level analysis."""
    lines = []
    lines.append("=" * 72)
    lines.append("ORDERED CHIRAL HOCHSCHILD OF V_{-2}(sl_2) AT CRITICAL LEVEL")
    lines.append("=" * 72)
    lines.append("")

    # Basic data
    lines.append("BASIC DATA:")
    lines.append(f"  k = -2 (critical level, k = -h^v)")
    lines.append(f"  kappa = {kappa_sl2(Fraction(-2))} (ZERO)")
    lines.append(f"  c = UNDEFINED (Sugawara singularity)")
    lines.append(f"  FF involution: k' = -k - 4 = -2 (FIXED POINT)")
    lines.append(f"  Center: Z(V_{{-2}}(sl_2)) = C[S_2] = Fun(Op)")
    lines.append("")

    # Bar cohomology
    lines.append("BAR COHOMOLOGY H^*(B(V_{-2}(sl_2))) = Omega^*(Op_{sl_2}(D)):")
    lines.append(f"  H^0 = C[S_2]: dims 1, 0, 1, 0, 1, 0, ... (weight 0, 2, 4, ...)")
    lines.append(f"  H^1 = C[S_2]*dS_2: dims 0, 0, 1, 0, 1, 0, ... (weight 2, 4, ...)")
    lines.append(f"  H^n = 0 for n >= 2 (rank 1)")
    lines.append(f"  CONTRAST generic: H^1 = C^3 (weight 1), all other H^n = 0")
    lines.append("")

    # KZ connection
    lines.append("KZ CONNECTION:")
    lines.append(f"  KZ form: Omega/((k+2)*z) DIVERGES at k = -2")
    lines.append(f"  Trace form: r(z) = -2*Omega/z (finite, nonzero)")
    lines.append(f"  Residue eigenvalues: -1 (Sym^2), +3 (wedge^2)")
    lines.append(f"  Monodromy: TRIVIAL (integer residues -> exp(2*pi*i*n) = 1)")
    lines.append("")

    # Arity table
    arity2 = ordered_chirhoch_arity2_critical()
    lines.append("ORDERED CHIRAL HOMOLOGY (arity-by-arity on E_tau):")
    lines.append(f"  {'n':>3} | {'Generic':>12} | {'Critical':>12} | Notes")
    lines.append(f"  {'-'*3}-+-{'-'*12}-+-{'-'*12}-+-{'-'*30}")
    lines.append(f"  {'0':>3} | {'1':>12} | {'inf (C[S2])':>12} | FF center jump")
    lines.append(f"  {'1':>3} | {'12':>12} | {'inf':>12} | FF center contributes")
    lines.append(f"  {'2':>3} | {'4':>12} | {arity2.critical_dim:>12} | Monodromy trivializes")
    lines.append(f"  {'3+':>3} | {'chi=0':>12} | {'chi=0':>12} | Trivial local system")
    lines.append("")

    # Averaging
    lines.append("AVERAGING MAP av: g^{E1} -> g^{mod}:")
    lines.append(f"  Representation-level ker(av_n): d^n - C(n+d-1,d-1), d=2")
    lines.append(f"    n=2: ker = 4 - 3 = 1 (antisymmetric)")
    lines.append(f"    n=3: ker = 8 - 4 = 4")
    lines.append(f"    n=4: ker = 16 - 5 = 11")
    lines.append(f"  Algebraic-level: av(r(z)) = -3/2 and the Sugawara shift is +3/2, so kappa = 0")
    lines.append(f"  The entire r-matrix datum r(z) = -2*Omega/z is in ker(av)")
    lines.append("")

    # Shadow tower
    lines.append("SHADOW OBSTRUCTION TOWER:")
    lines.append(f"  Theta_A = 0 (commutativity of FF center, not just kappa=0)")
    lines.append(f"  All shadow invariants (kappa, C, Q, ...) vanish")
    lines.append(f"  Shadow class: DEGENERATE (not G/L/C/M)")
    lines.append(f"  Shadow depth: 0 (trivial)")
    lines.append("")

    # Bicomplex
    lines.append("BICOMPLEX d_k = d_crit + (k+2)*delta:")
    lines.append(f"  At k = -2: d_k = d_crit (pure simple-pole)")
    lines.append(f"  Critical-first SS: E_1 = Omega^*(Op), d_1 = 0")
    lines.append(f"  At generic k: d_1 = (k+2)*[delta] contracts de Rham")
    lines.append(f"  Result: Omega^*(Op) collapses to C^3 (Koszul dual)")
    lines.append("")

    lines.append("=" * 72)
    return "\n".join(lines)
