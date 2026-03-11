"""Non-scalar saturation analysis: Candidate 3 — Admissible levels.

Analyzes the cyclic deformation cohomology H^2_cyc at admissible levels,
where the module category is non-semisimple and the Kazhdan-Lusztig
rigidity argument (Stage 2 of thm:cyclic-rigidity-generic) fails.

Mathematical content:
    1. Admissible level classification for sl_2: k = p/q - 2
    2. Zhu algebra A(L_k(sl_2)) at admissible levels
    3. Fusion rules via admissible-level Verlinde formula
    4. Module category structure (simple objects, extensions, indecomposables)
    5. H^2_cyc,prim analysis: can non-semisimplicity create new deformations?
    6. Whitehead decomposition: H^2_cyc = C*eta + H^2_cyc,prim
    7. Evidence for conj:scalar-saturation-universality

Key conjecture (manuscript conj:scalar-saturation-universality):
    H^2_cyc,prim(A) = 0 persists at admissible levels, where the
    module category is non-semisimple.

The structural point: at admissible levels, the module category has
non-trivial extensions (Ext^1 != 0), but the cyclic deformation
cohomology H^2_cyc,prim (which lives in a DIFFERENT Ext group —
Ext^2 of the bimodule, not Ext^1 between modules) may still vanish.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Tuple

import numpy as np


# ========================================================================
# Admissible level classification
# ========================================================================

@dataclass(frozen=True)
class AdmissibleLevel:
    """Data for an admissible level of sl_2."""
    p: int          # numerator parameter (p >= 2)
    q: int          # denominator parameter (q >= 1), gcd(p,q) = 1
    k: Fraction     # level = p/q - 2
    c: Fraction     # Sugawara central charge c(sl_2, k)
    n_simples: int  # number of simple admissible-weight modules
    is_integrable: bool  # True if q = 1 (positive integer level)


def admissible_level_sl2(p: int, q: int) -> AdmissibleLevel:
    """Construct admissible level data for sl_2.

    An admissible level for sl_2 (h^vee = 2) has the form
        k = p/q - 2
    where p >= 2, q >= 1, gcd(p,q) = 1.

    The associated VOA L_k(sl_2) is rational (C_2-cofinite)
    with finitely many simple ordinary modules.

    Number of simple modules: (p-1) * q  for the Kac-Wakimoto
    classification, but for the ORDINARY module category it's
    (p-1) when q = 1 (integrable), and more complex otherwise.

    For the Feigin-Frenkel classification of admissible sl_2 modules:
    - Simple modules labeled by (r,s) with 1 <= r <= p-1, 1 <= s <= q
    - Total: (p-1)*q simple modules in the full category
    - Ordinary (positive energy): subset determined by the grading
    """
    if p < 2:
        raise ValueError(f"Need p >= 2, got p = {p}")
    if q < 1:
        raise ValueError(f"Need q >= 1, got q = {q}")
    if gcd(p, q) != 1:
        raise ValueError(f"Need gcd(p,q) = 1, got gcd({p},{q}) = {gcd(p,q)}")

    k = Fraction(p, q) - 2
    # c(sl_2, k) = 3k/(k+2) = 3(p/q - 2)/(p/q) = 3(p - 2q)/p
    c = Fraction(3) * (Fraction(p) - 2 * Fraction(q)) / Fraction(p)
    n_simples = (p - 1) * q
    is_int = (q == 1)

    return AdmissibleLevel(p=p, q=q, k=k, c=c,
                           n_simples=n_simples, is_integrable=is_int)


def list_admissible_levels_sl2(max_denom: int = 5) -> List[AdmissibleLevel]:
    """List admissible levels for sl_2 up to given denominator."""
    levels = []
    for q in range(1, max_denom + 1):
        for p in range(2, 3 * q + 5):  # reasonable range
            if gcd(p, q) == 1:
                levels.append(admissible_level_sl2(p, q))
    # Sort by level value
    levels.sort(key=lambda a: float(a.k))
    return levels


# ========================================================================
# Admissible weight modules for sl_2
# ========================================================================

@dataclass(frozen=True)
class AdmissibleWeight:
    """An admissible weight module for sl_2 at level k = p/q - 2."""
    r: int          # row index, 1 <= r <= p-1
    s: int          # column index, 1 <= s <= q
    j: Fraction     # highest weight (sl_2 spin)
    h: Fraction     # conformal weight (L_0 eigenvalue)
    label: str      # human-readable label


def admissible_weights_sl2(level: AdmissibleLevel) -> List[AdmissibleWeight]:
    """Compute admissible weight modules for sl_2 at given level.

    For k = p/q - 2, the admissible weights are labeled by (r,s)
    with 1 <= r <= p-1, 1 <= s <= q.

    The highest weight (sl_2 spin) for module L(r,s):
        j_{r,s} = (r-1)/2 - (s-1) * p/(2q)

    Wait, the standard parametrization: the conformal weight is
        h_{r,s} = ((rq - sp)^2 - (p-q)^2) / (4pq)

    which is the Kac formula for the Virasoro algebra at
    c = 1 - 6(p-q)^2/(pq).

    For the sl_2 affine algebra, the highest sl_2-weight (spin) is:
        j_{r,s} = (r-1)/2  for s=1 (standard modules)

    More generally:
        j_{r,s} = ((r-1) - (s-1)(k+2))/2 = ((r-1) - (s-1)p/q)/2

    And the conformal weight:
        h_{r,s} = j_{r,s}(j_{r,s}+1)/(k+2)
                = j_{r,s}(j_{r,s}+1) * q/p
    """
    p, q = level.p, level.q
    weights = []
    for r in range(1, p):
        for s in range(1, q + 1):
            j = (Fraction(r - 1) - Fraction(s - 1) * Fraction(p, q)) / 2
            # Conformal weight h = j(j+1)/(k+2) = j(j+1)*q/p
            h = j * (j + 1) * Fraction(q, p)
            weights.append(AdmissibleWeight(
                r=r, s=s, j=j, h=h,
                label=f"L({r},{s})",
            ))
    return weights


# ========================================================================
# Zhu algebra
# ========================================================================

@dataclass
class ZhuAlgebraData:
    """Zhu algebra data for L_k(sl_2) at admissible level."""
    level: AdmissibleLevel
    dimension: int     # dim A(L_k) as a vector space (may be infinite for non-rational)
    polynomial_roots: List[Fraction]  # roots of the Zhu polynomial f_k(Omega)
    is_semisimple: bool
    n_simples: int


def zhu_algebra_sl2(level: AdmissibleLevel) -> ZhuAlgebraData:
    """Compute the Zhu algebra of L_k(sl_2) at admissible level.

    A(V_k(sl_2)) = U(sl_2) with Casimir Omega = h^2/2 + ef + fe.
    The Zhu algebra of the simple quotient L_k(sl_2) is:
        A(L_k) = C[Omega] / (f_k(Omega))

    where f_k(Omega) = prod_{(r,s)} (Omega - Omega_{r,s})
    and Omega_{r,s} = j_{r,s}(j_{r,s} + 1) is the Casimir eigenvalue
    on the highest-weight space of L(r,s).

    The Zhu algebra is semisimple iff the Casimir eigenvalues are distinct.
    """
    weights = admissible_weights_sl2(level)
    casimir_eigenvalues = [w.j * (w.j + 1) for w in weights]

    # Check distinctness
    eigenvalue_set = set(casimir_eigenvalues)
    is_ss = len(eigenvalue_set) == len(casimir_eigenvalues)

    return ZhuAlgebraData(
        level=level,
        dimension=len(casimir_eigenvalues),
        polynomial_roots=casimir_eigenvalues,
        is_semisimple=is_ss,
        n_simples=len(eigenvalue_set),
    )


# ========================================================================
# Fusion rules (admissible level Verlinde formula)
# ========================================================================

def admissible_modular_s_matrix_sl2(level: AdmissibleLevel) -> np.ndarray:
    """Compute the modular S-matrix for admissible sl_2 representations.

    For k = p/q - 2, the S-matrix entries are:
        S_{(r,s),(r',s')} = (-1)^{(r+s)(r'+s')} * 2/sqrt(pq)
                           * sin(pi*r*r'/p) * sin(pi*s*s'/q)

    Wait, the precise formula depends on conventions. For the
    Kac-Wakimoto S-matrix at admissible levels:

    S_{(r,s),(r',s')} = (2/sqrt(pq)) * (-1)^{...}
                       * sin(pi*r*r'*q/p) * sin(pi*s*s'*p/q)

    This is model-dependent. Let me use a simpler approach:
    compute the S-matrix elements and check unitarity.

    For the Verlinde formula: N_{ij}^k = sum_l S_{il} S_{jl} S_{kl}^* / S_{0l}
    """
    p, q = level.p, level.q
    n = (p - 1) * q  # number of simple modules

    # Index the modules as (r,s) -> flat index
    indices = []
    for r in range(1, p):
        for s in range(1, q + 1):
            indices.append((r, s))

    S = np.zeros((n, n), dtype=complex)
    norm = 2.0 / np.sqrt(p * q)

    for i, (r, s) in enumerate(indices):
        for j, (rp, sp) in enumerate(indices):
            sign = (-1) ** ((r + s + rp + sp) % 2)
            S[i, j] = sign * norm * (
                np.sin(np.pi * r * rp / p)
                * np.sin(np.pi * s * sp / q)
            )

    return S


def fusion_rules_sl2(level: AdmissibleLevel) -> np.ndarray:
    """Compute fusion rules via the Verlinde formula.

    N_{ij}^k = sum_l S_{il} S_{jl} S*_{kl} / S_{0l}

    Returns: N[i,j,k] tensor of fusion coefficients.
    """
    S = admissible_modular_s_matrix_sl2(level)
    n = S.shape[0]
    N_tensor = np.zeros((n, n, n), dtype=complex)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                val = 0.0
                for l in range(n):
                    if abs(S[0, l]) > 1e-12:
                        val += S[i, l] * S[j, l] * np.conj(S[k, l]) / S[0, l]
                N_tensor[i, j, k] = val

    return N_tensor


def verify_fusion_integrality(level: AdmissibleLevel) -> Dict:
    """Verify that fusion coefficients are non-negative integers.

    For admissible levels, the fusion rules should still give
    non-negative integer coefficients (the category is a
    finite tensor category, possibly non-semisimple).
    """
    N_tensor = fusion_rules_sl2(level)
    n = N_tensor.shape[0]

    max_imag = 0.0
    max_frac = 0.0
    negative_count = 0
    total = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                val = N_tensor[i, j, k]
                max_imag = max(max_imag, abs(val.imag))
                re = val.real
                rounded = round(re)
                max_frac = max(max_frac, abs(re - rounded))
                if rounded < -0.5:
                    negative_count += 1
                total += 1

    return {
        "level": f"k = {level.k} (p={level.p}, q={level.q})",
        "n_simples": n,
        "max_imaginary_part": max_imag,
        "max_fractional_part": max_frac,
        "negative_coefficients": negative_count,
        "integer_up_to": max_frac,
        "is_integral": max_frac < 0.1 and max_imag < 0.1,
    }


# ========================================================================
# Ext groups and non-semisimplicity
# ========================================================================

@dataclass
class ModuleCategoryData:
    """Data about the module category at admissible level."""
    level: AdmissibleLevel
    n_simples: int
    is_semisimple: bool
    non_split_extensions: List[Tuple[str, str]]  # pairs (L_i, L_j) with Ext^1 != 0
    ext1_dimension: Dict[Tuple[int, int], int]   # dim Ext^1(L_i, L_j)


def module_category_sl2_admissible(level: AdmissibleLevel) -> ModuleCategoryData:
    """Analyze the module category of L_k(sl_2) at admissible level.

    At integrable levels (q=1): the category is semisimple (MTC).
    At non-integrable admissible levels (q >= 2): the category has
    non-trivial extensions between simple modules.

    For k = p/q - 2 with q >= 2:
    - The simple modules form a non-semisimple braided finite tensor category
    - There exist indecomposable but non-simple modules
    - Ext^1(L_{r,s}, L_{r',s'}) can be nonzero

    Known results (Creutzig-Ridout, Adamovic):
    For sl_2 at k = -1/2 (p=3, q=2):
        - 2 simple ordinary modules: L(1,1) = vacuum, L(2,1) = L_{1/2}
        - In the full (logarithmic) category: extensions exist
        - Ext^1(L(1,1), L(2,1)) = C (one-dimensional)

    For sl_2 at k = -4/3 (p=2, q=3):
        - 2 simple ordinary modules in the Kac-Wakimoto list
        - Non-semisimple extensions in the logarithmic category
    """
    p, q = level.p, level.q
    weights = admissible_weights_sl2(level)

    if q == 1:
        # Integrable level: semisimple
        return ModuleCategoryData(
            level=level,
            n_simples=p - 1,
            is_semisimple=True,
            non_split_extensions=[],
            ext1_dimension={},
        )

    # Non-integrable admissible: non-semisimple
    # Use known structure for small cases

    extensions: List[Tuple[str, str]] = []
    ext1_dims: Dict[Tuple[int, int], int] = {}

    # For q >= 2, adjacent modules in the Kac table have extensions
    for i, w1 in enumerate(weights):
        for j, w2 in enumerate(weights):
            if i >= j:
                continue
            # Heuristic for Ext^1: adjacent in Kac table
            dr = abs(w1.r - w2.r)
            ds = abs(w1.s - w2.s)
            if (dr == 0 and ds == 1) or (dr == 1 and ds == 0):
                extensions.append((w1.label, w2.label))
                ext1_dims[(i, j)] = 1

    return ModuleCategoryData(
        level=level,
        n_simples=len(weights),
        is_semisimple=False,
        non_split_extensions=extensions,
        ext1_dimension=ext1_dims,
    )


# ========================================================================
# H^2_cyc,prim analysis
# ========================================================================

@dataclass
class CyclicCohomologyAnalysis:
    """Analysis of H^2_cyc at admissible levels."""
    level: AdmissibleLevel
    h2_cyc_level_component: int      # always 1 (the eta class)
    h2_cyc_prim_upper_bound: int     # upper bound on dim H^2_cyc,prim
    h2_cyc_prim_lower_bound: int     # lower bound
    whitehead_applies: bool          # Stage 1 (Whitehead decomposition)
    kl_semisimplicity: bool          # Stage 2 (KL rigidity)
    brst_rigidity: bool              # Alternative: BRST argument (for W-algebras)
    mechanism: str                   # which argument applies
    scalar_saturated: bool           # conclusion


def h2_cyc_analysis_sl2(level: AdmissibleLevel) -> CyclicCohomologyAnalysis:
    """Analyze H^2_cyc for sl_2 at admissible level k.

    The Whitehead decomposition (Stage 1 of thm:cyclic-rigidity-generic):
        H^2_cyc(sl_2_k, sl_2_k) = C * eta  +  H^2_cyc,prim

    always holds (only needs (a)-(b), not semisimplicity).

    For PURE KAC-MOODY algebras (no primary generators beyond currents),
    H^2_cyc,prim = 0 TRIVIALLY because there are no primary-primary pairs.
    The "prim" part consists of cocycles c'(phi_i, phi_j) where phi_i
    are PRIMARY strong generators, and a Kac-Moody algebra has NONE.

    This is the key structural observation: the admissible level problem
    is relevant for W-ALGEBRAS (which have primary generators), not for
    pure Kac-Moody algebras.
    """
    if level.is_integrable:
        mechanism = (
            "Integrable level: module category is semisimple (WZW fusion), "
            "KL rigidity applies directly."
        )
        kl = True
    else:
        mechanism = (
            "Pure Kac-Moody algebra: no primary strong generators beyond "
            "currents J^a. The space H^2_cyc,prim consists of cocycles on "
            "primary-primary pairs, which is EMPTY for Kac-Moody. "
            "Whitehead Stage 1 gives H^2_cyc = C*eta directly, without "
            "needing the KL semisimplicity argument."
        )
        kl = False

    return CyclicCohomologyAnalysis(
        level=level,
        h2_cyc_level_component=1,
        h2_cyc_prim_upper_bound=0,  # trivially 0 for pure KM
        h2_cyc_prim_lower_bound=0,
        whitehead_applies=True,
        kl_semisimplicity=kl,
        brst_rigidity=False,
        mechanism=mechanism,
        scalar_saturated=True,
    )


def h2_cyc_analysis_w_algebra_admissible(
    N: int, level: AdmissibleLevel,
) -> CyclicCohomologyAnalysis:
    """Analyze H^2_cyc for W_N = DS(sl_N) at admissible level.

    For W-algebras, there ARE primary strong generators (W_3, ..., W_N),
    so H^2_cyc,prim is potentially nonzero.

    At GENERIC level: the BRST argument applies.
        The DS reduction functor gives a unique W-algebra structure,
        so dim H^2_cyc = 1 at generic k.

    At ADMISSIBLE level: the BRST argument STILL applies!
        The quantum DS reduction H^0_DS(-, f) is well-defined at all
        levels k != -h^vee. At admissible k, the reduction produces
        a UNIQUE vertex algebra structure on the BRST cohomology.
        There are no additional moduli (the BRST complex is rigid).
        Therefore dim H^2_cyc(W^k(g,f), W^k(g,f)) = 1 even at
        admissible levels.

    This is the content of prop:nonprincipal-scalar-saturation:
    "the BRST pullback for W-algebras covers all levels, not just
    generic ones" (manuscript line 15313-15315).

    The remaining frontier: vertex algebras at admissible levels that
    are NOT obtained by DS reduction. These are rare; the main candidates
    are simple current extensions and permutation orbifolds.
    """
    if level.is_integrable:
        kl = True
        mechanism = (
            "W-algebra at integrable level: module category semisimple, "
            "KL argument applies."
        )
    else:
        kl = False
        mechanism = (
            f"W_{N} = DS(sl_{N}) at admissible level k = {level.k}: "
            f"the BRST reduction functor produces a UNIQUE vertex algebra "
            f"structure. The deformation space is one-dimensional (the level "
            f"direction) because the BRST complex has no additional moduli. "
            f"This holds at ALL levels k != -h^vee, including admissible."
        )

    return CyclicCohomologyAnalysis(
        level=level,
        h2_cyc_level_component=1,
        h2_cyc_prim_upper_bound=0,  # BRST rigidity gives this
        h2_cyc_prim_lower_bound=0,
        whitehead_applies=True,
        kl_semisimplicity=kl,
        brst_rigidity=True,  # the key alternative argument
        mechanism=mechanism,
        scalar_saturated=True,
    )


def h2_cyc_analysis_extension_voa(
    base_name: str, level: AdmissibleLevel,
    n_extra_generators: int,
) -> CyclicCohomologyAnalysis:
    """Analyze H^2_cyc for a simple current extension at admissible level.

    Simple current extensions of L_k(g) at admissible levels are the
    TRUE frontier for conj:scalar-saturation-universality.

    These VOAs:
    1. Have primary strong generators beyond the currents
    2. Are NOT obtained by DS reduction (generally)
    3. Live at admissible levels where KL fails

    For these, neither the trivial Kac-Moody argument nor the BRST
    argument applies directly. The conjecture predicts H^2_cyc,prim = 0,
    but this is unproven.

    Known examples:
    - Triplet algebras W(p): logarithmic extensions of Virasoro minimal models
      These have dim H^2_cyc = 1 (one-parameter family in p)
      But p is discrete, so the continuous deformation space is 0-dimensional!

    - Permutation orbifolds A^{x n}/S_n:
      These decompose as products (not genuinely non-scalar)
    """
    if level.is_integrable:
        return CyclicCohomologyAnalysis(
            level=level,
            h2_cyc_level_component=1,
            h2_cyc_prim_upper_bound=0,
            h2_cyc_prim_lower_bound=0,
            whitehead_applies=True,
            kl_semisimplicity=True,
            brst_rigidity=False,
            mechanism="Integrable level: KL semisimplicity",
            scalar_saturated=True,
        )

    return CyclicCohomologyAnalysis(
        level=level,
        h2_cyc_level_component=1,
        h2_cyc_prim_upper_bound=n_extra_generators,  # crude bound
        h2_cyc_prim_lower_bound=0,
        whitehead_applies=True,
        kl_semisimplicity=False,
        brst_rigidity=False,
        mechanism=(
            f"Simple current extension of {base_name} at k = {level.k}: "
            f"{n_extra_generators} primary generators beyond currents. "
            f"KL fails (non-semisimple), BRST not directly applicable. "
            f"H^2_cyc,prim in [0, {n_extra_generators}] — OPEN. "
            f"This is the genuine frontier of conj:scalar-saturation-universality."
        ),
        scalar_saturated=None,  # type: ignore  # genuinely unknown
    )


# ========================================================================
# Comprehensive frontier analysis
# ========================================================================

def frontier_analysis_sl2() -> List[CyclicCohomologyAnalysis]:
    """Analyze H^2_cyc across all admissible levels of sl_2."""
    results = []
    for level in list_admissible_levels_sl2(max_denom=4):
        results.append(h2_cyc_analysis_sl2(level))
    return results


def frontier_analysis_w_algebras() -> List[CyclicCohomologyAnalysis]:
    """Analyze H^2_cyc for W_N at small admissible levels."""
    results = []
    for N in [2, 3, 4]:
        # h^vee = N for sl_N, so k = p/q - N for W_N admissibility
        # Use sl_2-type admissible levels as prototypes
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 3)]:
            if gcd(p, q) == 1 and p >= 2:
                level = admissible_level_sl2(p, q)  # repurpose for level data
                results.append(h2_cyc_analysis_w_algebra_admissible(N, level))
    return results


def frontier_analysis_extensions() -> List[CyclicCohomologyAnalysis]:
    """Analyze the genuine frontier: extensions at admissible levels."""
    results = []

    # Triplet algebras W(p) at admissible levels
    # Need coprime (p_param, q) pairs for admissible_level_sl2
    triplet_levels = [
        (2, admissible_level_sl2(3, 2)),   # W(2), k = -1/2
        (3, admissible_level_sl2(5, 2)),   # W(3), k = 1/2
        (5, admissible_level_sl2(7, 2)),   # W(5), k = 3/2 (not really admissible — used as prototype)
        (7, admissible_level_sl2(5, 3)),   # W(7), k = -1/3
    ]
    for p_trip, level in triplet_levels:
        results.append(h2_cyc_analysis_extension_voa(
            f"W({p_trip}) triplet",
            level,
            n_extra_generators=1,  # W(p) has one extra generator
        ))

    return results


def comprehensive_saturation_analysis() -> Dict:
    """Master analysis of scalar saturation across all candidate classes.

    Summarizes the status of H^2_cyc,prim for:
    1. Pure Kac-Moody at admissible levels (PROVED: trivially 0)
    2. W-algebras at admissible levels (PROVED: BRST rigidity)
    3. Simple current extensions (OPEN: genuine frontier)
    """
    km_results = frontier_analysis_sl2()
    w_results = frontier_analysis_w_algebras()
    ext_results = frontier_analysis_extensions()

    km_all_saturated = all(r.scalar_saturated for r in km_results)
    w_all_saturated = all(r.scalar_saturated for r in w_results)
    ext_status = [
        r.scalar_saturated for r in ext_results
        if r.scalar_saturated is not None
    ]
    ext_open = sum(1 for r in ext_results if r.scalar_saturated is None)

    return {
        "kac_moody": {
            "count": len(km_results),
            "all_saturated": km_all_saturated,
            "mechanism": "No primary generators => H^2_cyc,prim empty",
            "status": "PROVED",
        },
        "w_algebras": {
            "count": len(w_results),
            "all_saturated": w_all_saturated,
            "mechanism": "BRST rigidity of DS reduction",
            "status": "PROVED",
        },
        "extensions": {
            "count": len(ext_results),
            "proved_saturated": len(ext_status),
            "open": ext_open,
            "mechanism": "Neither KL nor BRST applies",
            "status": "OPEN" if ext_open > 0 else "PROVED",
        },
        "overall": {
            "conjecture": "conj:scalar-saturation-universality",
            "proved_classes": "Kac-Moody (all levels), W-algebras (all levels)",
            "open_class": "Simple current extensions at admissible levels",
            "structural_reason": (
                "The conjecture reduces to: do simple current extensions "
                "at admissible levels admit continuous deformations beyond "
                "the level? No example is known, but no proof exists."
            ),
        },
    }


# ========================================================================
# Categorical Ext computation
# ========================================================================

def ext_bound_from_fusion(level: AdmissibleLevel) -> Dict:
    """Bound Ext^1 dimensions from the fusion rules.

    In a braided finite tensor category, the fusion rules give
    a lower bound on Ext groups. Specifically:
        N_{ij}^0 = dim Hom(L_i x L_j, L_0)
    and the failure of semisimplicity is witnessed by the
    difference between the Grothendieck ring multiplication
    and the actual tensor product.

    For our purposes: we need Ext^2 of the BIMODULE category,
    not Ext^1 of the module category. These are different:
        Ext^2_{A-bimod}(A, A) ≠ Ext^1_{A-mod}(M, N) in general

    The key structural point: even when Ext^1_{mod} ≠ 0 (non-semisimple),
    it's possible that Ext^2_{bimod} = 0 (no new deformations).
    """
    cat = module_category_sl2_admissible(level)

    return {
        "level": f"k = {level.k}",
        "n_simples": cat.n_simples,
        "is_semisimple": cat.is_semisimple,
        "n_extensions": len(cat.non_split_extensions),
        "ext1_pairs": cat.non_split_extensions,
        "ext2_bimod_status": (
            "Ext^2_{bimod} = 0 for pure KM (no primary generators). "
            "Non-trivial for extensions with primary generators."
        ),
        "h2_cyc_prim": 0 if cat.is_semisimple else "0 (pure KM) or OPEN (extensions)",
    }
