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
from typing import Dict, List, Tuple

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

    The highest sl_2-weight (spin) for module L(r,s):
        j_{r,s} = ((r-1) - (s-1)*p/q) / 2

    For s=1 (standard modules): j_{r,1} = (r-1)/2.

    The Sugawara conformal weight (L_0 eigenvalue on h.w. vector):
        h_{r,s} = j_{r,s}(j_{r,s}+1) / (k+2) = j_{r,s}(j_{r,s}+1) * q/p

    NOTE: This is the AFFINE sl_2 conformal weight, NOT the Virasoro
    Kac formula h = ((rq-sp)^2-(p-q)^2)/(4pq). The Kac formula gives
    conformal weights for the COSET (Virasoro) realization, which is
    a different quantity.
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

    Two regimes with DIFFERENT formulas:

    (A) Integrable levels (q=1): modules labeled by r=1,...,p-1.
        Standard SU(2)_k S-matrix (k = p-2):
            S_{r,r'} = sqrt(2/p) * sin(pi*r*r'/p)

    (B) Non-integrable admissible (q >= 2): modules labeled by (r,s)
        with 1 <= r <= p-1, 1 <= s <= q.
        Provisional formula (Kac-Wakimoto type):
            S_{(r,s),(r',s')} = (-1)^{rs'+r's} * (2/sqrt(pq))
                               * sin(pi*r*r'/p) * sin(pi*s*s'/q)

        CAVEAT: The precise sign convention and normalization for
        the admissible S-matrix depend on the choice of modular
        functor. The formula above is a standard ansatz that gives
        approximately integral Verlinde coefficients for small (p,q),
        but is NOT rigorously verified against all Creutzig-Ridout
        conventions. Use fusion integrality as a sanity check only.
    """
    p, q = level.p, level.q
    n = (p - 1) * q  # number of simple modules

    # Index the modules as (r,s) -> flat index
    indices = []
    for r in range(1, p):
        for s in range(1, q + 1):
            indices.append((r, s))

    S = np.zeros((n, n), dtype=complex)

    if q == 1:
        # Integrable: standard SU(2)_k S-matrix
        norm = np.sqrt(2.0 / p)
        for i, (r, _) in enumerate(indices):
            for j, (rp, _) in enumerate(indices):
                S[i, j] = norm * np.sin(np.pi * r * rp / p)
    else:
        # Non-integrable admissible: two-index formula
        norm = 2.0 / np.sqrt(p * q)
        for i, (r, s) in enumerate(indices):
            for j, (rp, sp) in enumerate(indices):
                sign = (-1) ** ((r * sp + rp * s) % 2)
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
    """Check whether Verlinde-type coefficients are approximately integral.

    IMPORTANT DISTINCTION:
    - At INTEGRABLE levels (q=1): the S-matrix formula is correct (standard
      SU(2)_k), and the Verlinde coefficients ARE non-negative integers
      (fusion multiplicities in a semisimple MTC). Tolerance: ~1e-10.

    - At NON-INTEGRABLE admissible levels (q >= 2): the S-matrix formula is
      PROVISIONAL, and the Verlinde formula computes Grothendieck ring
      structure constants (NOT fusion multiplicities). In non-semisimple
      categories, these CAN be negative. Use results with caution.
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

    # Use tight tolerance for integrable, loose for non-integrable
    if level.is_integrable:
        tol = 1e-10
    else:
        tol = 0.01  # provisional S-matrix; Grothendieck ring, not fusion

    return {
        "level": f"k = {level.k} (p={level.p}, q={level.q})",
        "n_simples": n,
        "max_imaginary_part": max_imag,
        "max_fractional_part": max_frac,
        "negative_coefficients": negative_count,
        "integer_up_to": max_frac,
        "is_integral": max_frac < tol and max_imag < tol,
        "integrable": level.is_integrable,
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
    # HEURISTIC: Ext^1 nonzero for Kac-table-adjacent pairs.
    # This is a rough approximation — the actual Ext groups depend on
    # the Loewy structure of projective covers (Adamovic, Creutzig-Ridout).
    # Adjacency in the Kac table is suggestive but not rigorous.
    for i, w1 in enumerate(weights):
        for j, w2 in enumerate(weights):
            if i >= j:
                continue
            dr = abs(w1.r - w2.r)
            ds = abs(w1.s - w2.s)
            if (dr == 0 and ds == 1) or (dr == 1 and ds == 0):
                extensions.append((w1.label, w2.label))
                ext1_dims[(i, j)] = 1  # heuristic

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

    TWO LOGICALLY DISTINCT ARGUMENTS:

    (A) At GENERIC level (proved, prop:nonprincipal-scalar-saturation):
        The OPE coefficients are rational functions of k, uniquely
        determined by the BRST construction. Therefore the deformation
        space is one-dimensional (the level direction).

    (B) At ADMISSIBLE level (partially proved):
        The DS reduction functor H^0_DS(-,f) is well-defined at all
        k != -h^vee. At admissible k, the reduction still produces
        a vertex algebra, and its OPE coefficients are obtained by
        specializing the generic rational functions to k = k_adm.
        Since the rational functions have no additional moduli,
        the specialization is unique.

        CAVEAT: This argument assumes the rational function description
        extends without extra poles or zeros at admissible k. At levels
        where the BRST complex has non-trivial higher cohomology (which
        CAN happen at admissible levels), additional moduli could
        appear. No counterexample is known, but the argument is not
        fully rigorous at all admissible levels.

    Manuscript status (rem:cyclic-rigidity-scope, line 15313-15315):
        "the BRST pullback for W-algebras covers all levels" — this
        refers to the EXISTENCE of scalar saturation, not a complete
        proof at every admissible level.
    """
    if level.is_integrable:
        kl = True
        mechanism = (
            "W-algebra at integrable level: module category semisimple, "
            "KL argument applies."
        )
        status = True
    else:
        kl = False
        mechanism = (
            f"W_{N} = DS(sl_{N}) at admissible level k = {level.k}: "
            f"the BRST reduction produces OPE coefficients that are "
            f"specializations of generic rational functions of k. "
            f"At generic k, uniqueness is proved (Fateev-Lukyanov). "
            f"At admissible k, uniqueness holds if no extra BRST "
            f"cohomology appears. No counterexample known, but the "
            f"argument has a gap at levels with non-trivial H^1_DS."
        )
        # Conservatively: proved at generic, strongly expected at admissible
        status = True  # manuscript treats this as proved (prop:nonprincipal)

    return CyclicCohomologyAnalysis(
        level=level,
        h2_cyc_level_component=1,
        h2_cyc_prim_upper_bound=0,
        h2_cyc_prim_lower_bound=0,
        whitehead_applies=True,
        kl_semisimplicity=kl,
        brst_rigidity=True,  # the alternative argument
        mechanism=mechanism,
        scalar_saturated=status,
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
    """Analyze H^2_cyc for W_N at small admissible levels.

    NOTE: We use sl_2-type admissible level DATA as stand-ins for the
    level parameter. The actual admissible levels of sl_N have the form
    k = p/q - N (h^vee = N for sl_N), not k = p/q - 2. The central
    charge and module count in the AdmissibleLevel object are for sl_2
    and should NOT be taken as valid for W_N. What IS valid: the
    structural analysis (BRST rigidity argument, scalar saturation
    conclusion) which depends on the LEVEL PARAMETER, not on sl_2-specific data.
    """
    results = []
    for N in [2, 3, 4]:
        for p, q in [(3, 2), (4, 3), (5, 2), (5, 3)]:
            if gcd(p, q) == 1 and p >= 2:
                level = admissible_level_sl2(p, q)  # stand-in for level data
                results.append(h2_cyc_analysis_w_algebra_admissible(N, level))
    return results


def frontier_analysis_extensions() -> List[CyclicCohomologyAnalysis]:
    """Analyze the genuine frontier: non-DS constructions at admissible levels.

    These include screening-kernel algebras (e.g., triplet algebras W(p))
    and certain extended affine VOAs. They are NOT simple current extensions
    (triplet algebras are logarithmic, non-rational constructions).

    The admissible level objects used here are stand-ins for the level
    parameter — the actual triplet algebra W(p) has c = 1 - 6(p-1)^2/p
    (Virasoro type), and its construction involves screening operators
    on a lattice VOA, not the sl_2 module category.
    """
    results = []

    # Triplet algebras W(p): screening-kernel constructions
    # Use sl_2 admissible levels as stand-ins for the level parameter
    triplet_levels = [
        (2, admissible_level_sl2(3, 2)),   # W(2), stand-in level k = -1/2
        (3, admissible_level_sl2(5, 2)),   # W(3), stand-in level k = 1/2
        (5, admissible_level_sl2(7, 2)),   # W(5), stand-in level k = 3/2
        (7, admissible_level_sl2(5, 3)),   # W(7), stand-in level k = -1/3
    ]
    for p_trip, level in triplet_levels:
        results.append(h2_cyc_analysis_extension_voa(
            f"W({p_trip}) triplet (screening-kernel)",
            level,
            n_extra_generators=1,  # W(p) has one extra generator
        ))

    return results


def comprehensive_saturation_analysis() -> Dict:
    """Master analysis of scalar saturation across all candidate classes.

    Summarizes the status of H^2_cyc,prim for:
    1. Pure Kac-Moody at admissible levels (PROVED: trivially 0)
    2. W-algebras at admissible levels (PROVED at generic k, EXPECTED at admissible)
    3. Screening-kernel / non-DS extensions (OPEN: genuine frontier)
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
            "mechanism": "BRST rigidity of DS reduction (generic k proved, admissible expected)",
            "status": "PROVED_GENERIC",
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
            "proved_classes": "Kac-Moody (all levels), W-algebras (generic level)",
            "open_class": "Non-DS extensions at admissible levels",
            "structural_reason": (
                "The conjecture reduces to: do non-DS constructions "
                "(screening-kernel algebras, extended affine VOAs) "
                "at admissible levels admit continuous deformations beyond "
                "the level? No example is known, but no proof exists."
            ),
        },
    }


# ========================================================================
# Categorical Ext computation
# ========================================================================

def ext_bound_from_fusion(level: AdmissibleLevel) -> Dict:
    """Summarize Ext group structure at an admissible level.

    Returns the module category data (semisimplicity, extension pairs)
    and documents the key distinction between module Ext^1 and
    bimodule Ext^2.

    NOTE: This function does NOT compute bounds from the Verlinde
    formula — it reports the heuristic Ext^1 data from the module
    category analysis. The name is historical.

    Key structural point: even when Ext^1_{mod} != 0 (non-semisimple),
    it's possible that Ext^2_{bimod} = 0 (no new deformations).
    The relevant group for scalar saturation is Ext^2_{A-bimod}(A, A),
    NOT Ext^1_{A-mod}(M, N).
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
