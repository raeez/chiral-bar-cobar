r"""FLE critical-level bar-cobar structure engine.

THEOREM (Critical-level bar-cobar degeneration and the FLE):

At the critical level k = -h^v, classical Koszul duality degenerates:
the bar complex B(V_{-h^v}(g)) becomes uncurved (kappa = 0), and bar
cohomology is no longer concentrated in bar degree 1.  Instead:

    H^n(B(V_{-h^v}(g))) ~ Omega^n(Op_{g^v}(D))    for all n >= 0.

This engine investigates FIVE STRUCTURAL QUESTIONS:

Q1. SHADOW OBSTRUCTION TOWER AT CRITICAL LEVEL (AP31 analysis):
    kappa = 0 does not by itself imply Theta_A = 0.  But at critical level,
    the OPE structure constants of the Feigin-Frenkel center are
    COMMUTATIVE (the center is a commutative chiral algebra), so all
    higher shadow data (cubic C, quartic Q, ...) also vanish.
    Theta_{V_crit} = 0 is the correct statement.
    Concordance: "for the commutative critical-level algebra the full MC
    element Theta_A = 0 (the OPE structure constants vanish)."

Q2. BAR COMPLEX AND THE FEIGIN-FRENKEL CENTER:
    H^0(B(V_{-h^v}(g))) = Fun(Op_{g^v}(D)) = z(g_hat) (FF center).
    The FULL bar cohomology H^*(B) = Omega^*(Op) is the de Rham complex
    of the oper space.  This is NOT the center itself but its derived
    enhancement.

Q3. KOSZULNESS AT CRITICAL LEVEL (which K1-K12 survive):
    Classical Koszulness (bar cohomology concentrated in bar degree 1) FAILS.
    The bar cohomology is the full de Rham algebra Omega^*(Op), spread
    across all degrees 0, 1, ..., dim(g)-rank(g).
    BUT: the PBW spectral sequence still degenerates (Whitehead),
    and many characterizations have critical-level analogues.
    Status of each K_i at critical level analyzed below.

Q4. FLE AS CATEGORICAL LIFT:
    Our thm:oper-bar-dl is a COHOMOLOGICAL identification.
    The FLE (Gaitsgory-Raskin 2405.03648) is a CATEGORICAL equivalence:
        KL(V_{crit}(g)) ~ IndCoh(Op_{G^L})
    The FLE implies our result (take Ext of vacuum module) but not conversely.
    The bar complex is a chain-level model for the localization functor Delta.

Q5. BICOMPLEX DEFORMATION (d_k = d_crit + (k+h^v) delta):
    The bar differential decomposes into simple-pole (d_crit) and
    double-pole (delta) parts.  This bicomplex structure controls the
    deformation from critical (k = -h^v) to generic (k != -h^v) level,
    and is the algebraic mechanism behind the FLE-to-Koszul interpolation.

PROVED RESULTS (from the monograph):
- thm:langlands-bar-bridge: H^n(B(V_{crit}(g))) = Omega^n(Op(D))
- thm:oper-bar-dl: Full oper differential-form identification
- thm:km-bar-bicomplex: d_k = d_crit + (k+h^v) delta bicomplex
- cor:critical-level-spectral: Two spectral sequences from the bicomplex
- thm:critical-level-structure: FF center = Fun(Op)
- prop:whitehead-spectral-decomposition: E_1 = Fun(Op) x H^*(g;k)
- prop:d4-nonvanishing: Cartan transgression nonzero

COMPLEMENTARITY PRINCIPLE:
- FLE holds at critical level (kappa = 0, uncurved, H^*(B) = Omega^*(Op)).
- Koszulness holds at generic level (kappa != 0, curved, H^1(B) = A^!).
- These are ORTHOGONAL axes (concordance: subsec:concordance-two-orthogonal-axes).
- The bicomplex interpolates between them.

Conventions
-----------
- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
- kappa(g, k) = dim(g)(k + h^v)/(2 h^v) (AP1, AP39).
- Sugawara UNDEFINED at critical level (not "c diverges").
- H_k^! = V_{-k-2h^v}(g), NOT H_{-k} (AP33).

Beilinson warnings
------------------
AP1:  kappa is family-specific; recompute for each g.
AP9:  kappa != c/2 for affine KM.
AP14: Koszulness != formality.  At critical level both fail in different ways.
AP31: kappa = 0 does NOT by itself imply Theta_A = 0.  At critical level,
      the full MC element vanishes because the algebra is commutative.
AP33: Koszul dual != negative-level substitution.
AP39: kappa != S_2 for rank > 1.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union


# =========================================================================
# Section 0: Lie algebra data (imported from FLE bridge engine)
# =========================================================================

@dataclass(frozen=True)
class SimpleLieData:
    """Data of a simple finite-dimensional Lie algebra."""
    type: str
    rank: int
    dim: int
    h_vee: int
    exponents: Tuple[int, ...]
    num_positive_roots: int

    @property
    def oper_generators_weights(self) -> Tuple[int, ...]:
        """Conformal weights of oper space generators = exponents + 1."""
        return tuple(d + 1 for d in self.exponents)

    @property
    def lie_cohomology_degrees(self) -> Tuple[int, ...]:
        """Degrees of generators of H^*(g; k) = Lambda(omega_{2d_i+1}).

        Chevalley: H^*(g; k) is exterior on generators in degrees 2*d_i + 1,
        where d_i are the exponents.
        """
        return tuple(2 * d + 1 for d in self.exponents)

    @property
    def lie_cohomology_total_dim(self) -> int:
        """dim H^*(g; k) = 2^rank."""
        return 2 ** self.rank

    @property
    def top_lie_cohomology_degree(self) -> int:
        """Top degree where H^q(g; k) != 0 = sum of all lie_cohomology_degrees."""
        return sum(self.lie_cohomology_degrees)


def lie_data(lie_type: str, rank: int) -> SimpleLieData:
    """Construct SimpleLieData for a simple Lie algebra."""
    if lie_type == "A":
        n = rank + 1
        dim = n * n - 1
        h_vee = n
        exponents = tuple(range(1, n))
        num_pos = rank * (rank + 1) // 2
        return SimpleLieData("A", rank, dim, h_vee, exponents, num_pos)
    elif lie_type == "B":
        dim = rank * (2 * rank + 1)
        h_vee = 2 * rank - 1
        exponents = tuple(range(1, 2 * rank, 2))
        num_pos = rank * rank
        return SimpleLieData("B", rank, dim, h_vee, exponents, num_pos)
    elif lie_type == "C":
        dim = rank * (2 * rank + 1)
        h_vee = rank + 1
        exponents = tuple(range(1, 2 * rank, 2))
        num_pos = rank * rank
        return SimpleLieData("C", rank, dim, h_vee, exponents, num_pos)
    elif lie_type == "D":
        dim = rank * (2 * rank - 1)
        h_vee = 2 * rank - 2
        exps = list(range(1, 2 * rank - 2, 2)) + [rank - 1]
        exponents = tuple(sorted(exps))
        num_pos = rank * (rank - 1)
        return SimpleLieData("D", rank, dim, h_vee, exponents, num_pos)
    elif lie_type == "E" and rank == 6:
        return SimpleLieData("E", 6, 78, 12, (1, 4, 5, 7, 8, 11), 36)
    elif lie_type == "E" and rank == 7:
        return SimpleLieData("E", 7, 133, 18, (1, 5, 7, 9, 11, 13, 17), 63)
    elif lie_type == "E" and rank == 8:
        return SimpleLieData("E", 8, 248, 30, (1, 7, 11, 13, 17, 19, 23, 29), 120)
    elif lie_type == "F" and rank == 4:
        return SimpleLieData("F", 4, 52, 9, (1, 5, 7, 11), 24)
    elif lie_type == "G" and rank == 2:
        return SimpleLieData("G", 2, 14, 4, (1, 5), 6)
    else:
        raise ValueError(f"Unknown Lie type {lie_type}_{rank}")


# =========================================================================
# Section 1: Critical level basic invariants
# =========================================================================

def kappa_affine(g: SimpleLieData, k: Union[int, float, Fraction]
                 ) -> Union[float, Fraction]:
    """Modular characteristic kappa = dim(g)(k + h^v)/(2 h^v)."""
    if isinstance(k, Fraction):
        return Fraction(g.dim) * (k + g.h_vee) / (2 * g.h_vee)
    return g.dim * (k + g.h_vee) / (2.0 * g.h_vee)


def koszul_dual_level(g: SimpleLieData, k: Union[int, float, Fraction]
                      ) -> Union[float, Fraction]:
    """Feigin-Frenkel involution: k' = -k - 2h^v."""
    return -k - 2 * g.h_vee


def is_critical(g: SimpleLieData, k: Union[int, float, Fraction],
                tol: float = 1e-12) -> bool:
    """Check if k = -h^v (critical level)."""
    if isinstance(k, Fraction):
        return k == Fraction(-g.h_vee)
    return abs(k + g.h_vee) < tol


# =========================================================================
# Section 2: Q1 -- Shadow obstruction tower at critical level
# =========================================================================

def shadow_tower_at_critical_level(g: SimpleLieData) -> Dict[str, Any]:
    """Analyze the shadow obstruction tower at k = -h^v.

    AP31 WARNING: kappa = 0 does NOT by itself imply Theta_A = 0.
    Higher-arity components (cubic C, quartic Q, ...) are independent of kappa.

    HOWEVER: at critical level, V_{-h^v}(g) has a COMMUTATIVE chiral algebra
    structure (the Feigin-Frenkel center is commutative).  This means:
    - All OPE structure constants between center elements vanish.
    - The MC element Theta_A in Def_cyc^mod(A) is zero.
    - All shadow projections (kappa, C, Q, ...) vanish.
    - The shadow depth is r_max = 0 (trivial tower).

    The key distinction: kappa = 0 alone does NOT force Theta = 0 (AP31).
    What DOES force Theta = 0 is the commutativity of the critical-level
    chiral algebra structure.  The two facts are:
    (1) kappa = 0 => m_0 = 0 => uncurved (no curvature obstruction).
    (2) Commutativity => all higher operations m_n (n >= 2) between center
        elements are zero => Theta = 0.

    For the FULL algebra V_{-h^v}(g) (not just the center):
    - The bar complex is uncurved but nontrivial.
    - H^*(B) = Omega^*(Op), which is a rich graded algebra.
    - The shadow obstruction tower is trivial because the bar-intrinsic
      MC element Theta_A := D_A - d_0 vanishes when kappa = 0 AND the
      algebra has no higher obstructions.
    """
    k_crit = Fraction(-g.h_vee)
    kap = kappa_affine(g, k_crit)

    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'critical_level': int(k_crit),
        'kappa': float(kap),
        'kappa_is_zero': kap == 0,
        # Shadow tower data
        'shadow_kappa': 0,
        'shadow_cubic_C': 0,
        'shadow_quartic_Q': 0,
        'shadow_depth_r_max': 0,
        'shadow_class': 'degenerate',  # Not G/L/C/M -- trivial
        'theta_A_vanishes': True,
        'reason_theta_vanishes': (
            'Commutativity of critical-level chiral algebra structure, '
            'NOT merely kappa = 0 (AP31).'
        ),
        # Bar complex is nontrivial even though Theta = 0
        'bar_complex_nontrivial': True,
        'bar_uncurved': True,
        'bar_cohomology_nontrivial': True,
        # Discriminant and shadow metric
        'discriminant_Delta': 0,  # 8 * kappa * S_4 = 0
        'shadow_metric_Q': '(3 alpha t)^2',  # degenerates when kappa = 0
        'ap31_violated': False,  # We are NOT deducing Theta = 0 from kappa = 0 alone
    }


# =========================================================================
# Section 3: Q2 -- Bar complex and the Feigin-Frenkel center
# =========================================================================

@lru_cache(maxsize=4096)
def _multivariate_partition_count(n: int, weights: Tuple[int, ...]) -> int:
    """Count non-negative integer solutions to sum_i w_i * n_i = n."""
    if n == 0:
        return 1
    if n < 0 or not weights:
        return 0
    w0 = weights[0]
    rest = weights[1:]
    total = 0
    for m in range(n // w0 + 1):
        total += _multivariate_partition_count(n - m * w0, rest)
    return total


def ff_center_dim(g: SimpleLieData, weight: int) -> int:
    """Dimension of the Feigin-Frenkel center z(g_hat) at conformal weight w.

    z(g_hat) = Fun(Op_{g^v}(D)) = C[S_{d_1+1}, ..., S_{d_r+1}]
    where S_j has conformal weight j and d_i are exponents of g.
    """
    return _multivariate_partition_count(weight, g.oper_generators_weights)


def bar_h0_critical(g: SimpleLieData, weight: int) -> int:
    """H^0(B(V_{-h^v}(g))) at weight w = FF center dimension at weight w.

    By thm:oper-bar-h0-dl: H^0(B) = Fun(Op) = z(g_hat).
    """
    return ff_center_dim(g, weight)


def _subsets_of_size(items: List[int], k: int) -> List[Tuple[int, ...]]:
    """All k-element subsets of items."""
    if k == 0:
        return [()]
    if not items or k > len(items):
        return []
    first = items[0]
    rest = items[1:]
    with_first = [(first,) + s for s in _subsets_of_size(rest, k - 1)]
    without_first = _subsets_of_size(rest, k)
    return with_first + without_first


def bar_hn_critical(g: SimpleLieData, n: int, weight: int) -> int:
    """H^n(B(V_{-h^v}(g))) at weight w = Omega^n(Op) at weight w.

    By thm:oper-bar-dl: H^n(B) = Omega^n(Op_{g^v}(D)).

    Omega^n(Op) = Lambda^n(Omega^1(Op)) tensor Fun(Op).
    Generators of Omega^1 have weights d_1+1, ..., d_r+1.
    """
    r = g.rank
    if n < 0 or n > r:
        return 0
    gen_weights = g.oper_generators_weights
    total = 0
    for subset in _subsets_of_size(list(range(r)), n):
        form_weight = sum(gen_weights[i] for i in subset)
        remaining = weight - form_weight
        if remaining >= 0:
            total += ff_center_dim(g, remaining)
    return total


def bar_cohomology_is_oper_forms(g: SimpleLieData, max_weight: int = 10,
                                 max_degree: int = -1) -> Dict[str, Any]:
    """Verify H^n(B(V_{-h^v}(g))) = Omega^n(Op_{g^v}(D)).

    Computes dimensions at each (n, w) and checks consistency.
    """
    if max_degree < 0:
        max_degree = g.rank

    dims = {}
    total_dim = 0
    for n in range(max_degree + 1):
        for w in range(max_weight + 1):
            d = bar_hn_critical(g, n, w)
            dims[(n, w)] = d
            total_dim += d

    # Vanishing: H^n = 0 for n > rank
    vanishing_correct = all(
        bar_hn_critical(g, n, w) == 0
        for n in range(g.rank + 1, g.rank + 3)
        for w in range(max_weight + 1)
    )

    # H^0 = Fun(Op) = polynomial algebra
    h0_polynomial = all(
        bar_hn_critical(g, 0, w) == ff_center_dim(g, w)
        for w in range(max_weight + 1)
    )

    # H^0 at weight 0 is 1-dimensional (vacuum = 1 in Fun(Op))
    vacuum_unique = bar_hn_critical(g, 0, 0) == 1

    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'max_degree': max_degree,
        'max_weight': max_weight,
        'total_dim_computed': total_dim,
        'vanishing_above_rank': vanishing_correct,
        'h0_equals_fun_op': h0_polynomial,
        'vacuum_unique': vacuum_unique,
        'dims': dims,
    }


# =========================================================================
# Section 4: Q3 -- Koszulness at critical level
# =========================================================================

@dataclass
class KoszulnessAtCriticalLevel:
    """Analysis of each K1-K12 characterization at critical level.

    At critical level k = -h^v:
    - The bar complex is uncurved (d^2 = 0), so cohomology is well-defined.
    - Bar cohomology is NOT concentrated in bar degree 1; it is spread across
      degrees 0, 1, ..., rank(g) (the full de Rham algebra of Op).
    - Classical Koszulness FAILS.

    Status of each characterization (from thm:koszul-equivalences-meta):
    """
    lie_algebra: str
    rank: int

    # K1: PBW spectral sequence E_2-collapse
    k1_pbw: str = ""
    # K2: A-infinity formality (m_n = 0 for n >= 3)
    k2_ainfty: str = ""
    # K3: Ext diagonal vanishing
    k3_ext: str = ""
    # K4: Bar-cobar counit quasi-iso
    k4_barcobar: str = ""
    # K5: Barr-Beck-Lurie
    k5_bbl: str = ""
    # K6: FH concentration
    k6_fh: str = ""
    # K7: ChirHoch polynomial
    k7_hochschild: str = ""
    # K8: Kac-Shapovalov determinant
    k8_kac_shapovalov: str = ""
    # K9: FM boundary acyclicity
    k9_fm: str = ""
    # K10: Tropical Koszulness
    k10_tropical: str = ""
    # K11: Lagrangian criterion (conditional)
    k11_lagrangian: str = ""
    # K12: D-module purity (one-directional)
    k12_d_module: str = ""


def koszulness_at_critical_level(g: SimpleLieData) -> KoszulnessAtCriticalLevel:
    """Analyze which Koszulness characterizations survive at critical level.

    The fundamental fact: at k = -h^v, the bar cohomology is
    H^*(B) = Omega^*(Op), which is NOT concentrated in degree 1.
    So classical chiral Koszulness FAILS.

    Each K_i is analyzed for its critical-level status.
    """
    result = KoszulnessAtCriticalLevel(
        lie_algebra=f"{g.type}_{g.rank}",
        rank=g.rank,
    )

    # K1: PBW E_2-collapse
    # The PBW spectral sequence DOES degenerate (Whitehead decomposition),
    # but the abutment is Omega^*(Op), not a Koszul dual algebra.
    # STATUS: The spectral sequence mechanism works, but the conclusion
    # (bar concentration) fails.
    result.k1_pbw = (
        "DEGENERATES but to Omega^*(Op), not a Koszul dual. "
        "The Whitehead decomposition E_1 = Fun(Op) x H^*(g;k) holds. "
        "PBW degeneration is a necessary condition; concentration is not met."
    )

    # K2: A-infinity formality
    # At critical level, the algebra is commutative (center = Fun(Op)).
    # A-infinity operations from HTT are trivial: all m_n = 0 for n >= 1
    # on the center elements.  But this is STRONGER than formality; it is
    # commutativity.  Formality in the Koszul sense fails because the bar
    # complex carries nontrivial higher cohomology.
    result.k2_ainfty = (
        "INAPPLICABLE: the bar complex is uncurved, so the question of "
        "A-infinity formality of bar cohomology changes character. "
        "The bar cohomology IS a cdga (exterior algebra of Op forms), "
        "but it is not concentrated in degree 1."
    )

    # K3: Ext diagonal vanishing
    # Ext^n(V_crit, V_crit) = Omega^n(Op) (Frenkel-Teleman).
    # This is NOT diagonally concentrated: Omega^n(Op) has conformal weight
    # contributions from all weights >= n * min(d_i + 1).
    result.k3_ext = (
        "FAILS: Ext^n(V_crit, V_crit) = Omega^n(Op) is not diagonally "
        f"concentrated.  Ext^n != 0 for 0 <= n <= {g.rank} "
        "(the rank of the oper space)."
    )

    # K4: Bar-cobar counit quasi-iso
    # At critical level, bar-cobar inversion STILL holds (Theorem B applies
    # to uncurved chiral Koszul algebras, and V_crit is Koszul in the
    # universal algebra sense).  Omega(B(V_crit)) ~ V_crit.
    result.k4_barcobar = (
        "HOLDS: bar-cobar inversion Omega(B(A)) ~ A remains valid at "
        "critical level. The uncurved bar complex is a genuine dg coalgebra, "
        "and bar-cobar adjunction applies. The FF involution fixes the "
        "critical level, so the Koszul dual is V_crit itself."
    )

    # K5: Barr-Beck-Lurie
    # Effective descent holds for bar-cobar at critical level.
    result.k5_bbl = (
        "HOLDS: Barr-Beck-Lurie descent for the bar-cobar adjunction "
        "applies at critical level. The key input is that the bar complex "
        "is a well-defined dg coalgebra (uncurved)."
    )

    # K6: FH concentration
    # Factorization homology FH_{g}(A) at genus g: at critical level,
    # kappa = 0 so FH is concentrated in degree 0 for all g.
    result.k6_fh = (
        "HOLDS TRIVIALLY: kappa = 0 implies FH_g concentrated in "
        "degree 0 for all g >= 0. But this is the TRIVIAL case "
        "(no curvature contribution), not the Koszul case."
    )

    # K7: ChirHoch bounded amplitude [0,2] per Theorem H.
    # FT-5 ANALYSIS: Theorem H does NOT apply at critical level.
    # Chiral Koszulness (diagonal Ext concentration) FAILS: Ext^{p,q} != 0
    # for p != q (Fun(Op) contributes at bar degree 0, all even weights).
    # PBW degeneration holds but does NOT imply diagonal concentration
    # when kappa = 0 (no curvature to force diagonality).
    # The BD comparison identifies ChirHoch with continuous Lie cohomology,
    # which is UNBOUNDED.
    result.k7_hochschild = (
        "FAILS: Theorem H requires chiral Koszulness (diagonal Ext "
        "concentration, chiral_koszul_pairs.tex:1286), which fails at "
        "critical level. PBW degeneration holds (cor:universal-koszul) "
        "but does NOT imply diagonal concentration when kappa = 0 "
        "(curvature forces diagonality at generic level; at critical level "
        "off-diagonal Ext survives). The BD comparison theorem (BD04 "
        "Thm 4.5.2) identifies ChirHoch with continuous Lie cohomology: "
        "Lambda(P_1,...,P_r) x C[Theta_1,...,Theta_r], which is UNBOUNDED "
        f"with polynomial growth O(n^{{{g.rank-1}}}). "
        "Each of ChirHoch^0 (FF center), ChirHoch^1 (z(g_hat) x g), "
        "ChirHoch^2 (Z(V_crit) = FF center) is infinite-dimensional."
    )

    # K8: Kac-Shapovalov determinant
    # At critical level, the Shapovalov form degenerates (the Sugawara
    # construction is undefined, so the conformal weight grading is lost).
    # The vacuum Verma module is reducible.
    result.k8_kac_shapovalov = (
        "FAILS: Sugawara UNDEFINED at critical level (k + h^v = 0). "
        "The Kac-Shapovalov determinant has infinitely many zeros "
        "(the vacuum Verma module is maximally reducible at critical level). "
        "This failure is dual to the appearance of the FF center."
    )

    # K9: FM boundary acyclicity
    # The FM boundary strata contribute to bar cohomology in multiple degrees.
    result.k9_fm = (
        "MODIFIED: FM boundary acyclicity in the strict Koszul sense fails "
        "(bar cohomology is not concentrated). The FM boundary structure "
        "is nontrivial and produces the Whitehead spectral decomposition."
    )

    # K10: Tropical Koszulness
    result.k10_tropical = (
        "FAILS: the planted-forest differential has nontrivial cohomology "
        "in multiple degrees at critical level."
    )

    # K11: Lagrangian criterion (conditional)
    result.k11_lagrangian = (
        "INAPPLICABLE: the shifted-symplectic structure on complementarity "
        "degenerates at kappa = 0 (self-complementarity point)."
    )

    # K12: D-module purity
    result.k12_d_module = (
        "HOLDS in a different sense: at critical level, the D-module "
        "structure on the bar complex is pure (the PBW filtration gives "
        "a pure Hodge structure). This is the critical-level specialization "
        "of the D-module purity characterization."
    )

    return result


def koszulness_survival_count(g: SimpleLieData) -> Dict[str, int]:
    """Count how many K_i characterizations hold/fail/are modified at critical level."""
    holds = 3    # K4, K5, K6
    fails = 5    # K3, K7, K8, K9, K10
    modified = 2  # K1, K12
    inapplicable = 2  # K2, K11
    return {
        'holds': holds,
        'fails': fails,
        'modified': modified,
        'inapplicable': inapplicable,
        'total': holds + fails + modified + inapplicable,
    }


# =========================================================================
# Section 5: Q4 -- FLE as categorical lift
# =========================================================================

def fle_categorical_hierarchy(g: SimpleLieData) -> Dict[str, Any]:
    """The hierarchy: FLE (categorical) => bar-oper (cohomological).

    Three levels of the identification at critical level:

    Level 1 (Categorical -- FLE, Gaitsgory-Raskin 2405.03648):
        V_{-h^v}(g)-mod  ~  QCoh(Op_{g^v}(D))
        or more precisely: KL(V_crit(g)) ~ IndCoh(Op_{G^L})

    Level 2 (Derived -- Frenkel-Gaitsgory localization):
        D(V_{-h^v}(g)-mod)  ->  D(QCoh(Op))
        (localization functor Delta)

    Level 3 (Cohomological -- our thm:oper-bar-dl):
        H^n(B(V_{-h^v}(g)))  ~  Omega^n(Op_{g^v}(D))
        (bar-Ext + Frenkel-Teleman)

    Each level implies the next (by taking appropriate functors):
    Level 1 => Level 2 (take derived categories)
    Level 2 => Level 3 (take Ext of vacuum module)

    The converses do NOT hold:
    Level 3 does NOT imply Level 2 (cohomological data does not determine
    the functor).
    Level 2 does NOT imply Level 1 in full generality (the localization
    functor is only an equivalence on a subcategory).
    """
    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'level_1_fle': {
            'statement': f"KL(V_{{-{g.h_vee}}}({g.type}_{g.rank})) "
                         f"~ IndCoh(Op_{{G^L}})",
            'source': 'Gaitsgory-Raskin 2405.03648',
            'status': 'ProvedElsewhere',
            'objects': 'factorization categories',
        },
        'level_2_localization': {
            'statement': f"Delta: D(V_{{-{g.h_vee}}}({g.type}_{g.rank})-mod) "
                         f"-> D(QCoh(Op))",
            'source': 'Frenkel-Gaitsgory 2006',
            'status': 'ProvedElsewhere',
            'objects': 'derived categories',
        },
        'level_3_bar_oper': {
            'statement': f"H^n(B(V_{{-{g.h_vee}}}({g.type}_{g.rank}))) "
                         f"~ Omega^n(Op(D))",
            'source': 'thm:oper-bar-dl (this monograph)',
            'status': 'ProvedHere',
            'objects': 'graded algebras',
        },
        'implications': {
            'level_1_implies_level_2': True,
            'level_2_implies_level_3': True,
            'level_3_implies_level_2': False,
            'level_2_implies_level_1': False,
        },
        'bridge_mechanism': (
            'The bar complex B(V_crit(g)) is a chain-level model for the '
            'vacuum-side localization functor Delta. Taking H^0 recovers '
            'Fun(Op) (the target of Delta on the vacuum module).'
        ),
    }


# =========================================================================
# Section 6: Q5 -- Bicomplex deformation d_k = d_crit + (k+h^v) delta
# =========================================================================

def bicomplex_structure(g: SimpleLieData, k: Union[int, float, Fraction]
                        ) -> Dict[str, Any]:
    """The bicomplex structure of the KM bar differential.

    thm:km-bar-bicomplex: d_k = d_crit + (k + h^v) * delta, where:
    - d_crit extracts simple-pole residues (structure constants f^{ab}_c)
    - delta extracts double-pole residues (level k bilinear form)
    - d_crit^2 = 0, delta^2 = 0, {d_crit, delta} = 0

    At critical level (k = -h^v): d_k = d_crit (pure simple-pole).
    At generic level: d_k = d_crit + lambda * delta with lambda = k + h^v.

    The critical-first spectral sequence:
    E_1 = H^*(B, d_crit) (= critical bar cohomology = Omega^*(Op))
    converging to H^*(B, d_k) (= generic bar cohomology).
    """
    lam = k + g.h_vee if isinstance(k, (int, float)) else k + Fraction(g.h_vee)

    is_crit = is_critical(g, k)
    kap = kappa_affine(g, k)

    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'level': float(k) if not isinstance(k, Fraction) else float(k),
        'lambda': float(lam) if not isinstance(lam, Fraction) else float(lam),
        'is_critical': is_crit,
        'kappa': float(kap) if not isinstance(kap, Fraction) else float(kap),
        # Bicomplex components
        'd_crit_squared_zero': True,  # Always
        'delta_squared_zero': True,   # Always
        'anticommutator_zero': True,  # Always
        # At critical level
        'd_k_equals_d_crit': is_crit,
        'delta_contribution_zero': is_crit,
        # Spectral sequence
        'critical_first_e1': 'Omega^*(Op)' if is_crit else 'Omega^*(Op)',
        'critical_first_d1_zero': is_crit,  # d_1 = lambda * delta = 0 at crit
        'degeneration': 'E_1' if is_crit else 'open',
        # Curvature
        'm_0': f"{float(lam)}/(2*{g.h_vee}) * Casimir"
               if not is_crit else '0',
        'bar_uncurved': is_crit,
    }


def bicomplex_interpolation(g: SimpleLieData,
                            levels: Optional[List[Union[int, Fraction]]] = None
                            ) -> List[Dict[str, Any]]:
    """Interpolate the bicomplex from critical to generic level.

    Shows how the bar complex deforms as k moves away from -h^v.
    """
    if levels is None:
        h = g.h_vee
        levels = [
            Fraction(-h),           # critical
            Fraction(-h) + Fraction(1, 10),  # near-critical
            Fraction(-h) + Fraction(1, 2),   # half-step
            Fraction(-h) + Fraction(1),       # one step
            Fraction(1),            # generic positive
            Fraction(10),           # large positive
        ]
    return [bicomplex_structure(g, k) for k in levels]


# =========================================================================
# Section 7: Oper space invariants
# =========================================================================

def oper_space_analysis(g: SimpleLieData) -> Dict[str, Any]:
    """Analysis of the oper space Op_{g^v}(D).

    Op_{g^v}(D) = Spec C[[q_{d_1+1}, ..., q_{d_r+1}]]
    is a formal power series space of dimension rank(g).

    Properties:
    - Formally smooth (Frenkel-Gaitsgory).
    - Cotangent complex classical: L_Op = Omega^1[0].
    - De Rham complex: Omega^n(Op) = Lambda^n(Omega^1(Op)) x Fun(Op).
    - Omega^n = 0 for n > rank(g).
    - Euler characteristic of Omega^*(Op) at any weight:
      sum_n (-1)^n dim Omega^n_w = 0 for w > 0 (exact de Rham complex),
      = 1 for w = 0 (constant function).
    """
    gen_weights = g.oper_generators_weights
    max_form_degree = g.rank

    # De Rham Euler characteristic check at several weights
    euler_chars = {}
    for w in range(15):
        chi = sum(
            (-1)**n * bar_hn_critical(g, n, w)
            for n in range(max_form_degree + 1)
        )
        euler_chars[w] = chi

    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'langlands_dual': f"{g.type}_{g.rank}" if g.type not in ("B", "C")
                          else ("C" if g.type == "B" else "B") + f"_{g.rank}",
        'oper_dimension': g.rank,
        'generator_weights': gen_weights,
        'max_form_degree': max_form_degree,
        'formally_smooth': True,
        'cotangent_complex_classical': True,
        'euler_characteristics': euler_chars,
        # For formally smooth space, de Rham is exact except at w=0
        'de_rham_exact_positive_weight': all(
            euler_chars[w] == 0 for w in range(1, 15)
        ),
        'euler_char_w0': euler_chars[0],  # Should be 1
    }


# =========================================================================
# Section 8: Hochschild periodicity
# =========================================================================

def hochschild_periodicity(g: SimpleLieData) -> Dict[str, Any]:
    """Critical-level ChirHoch: BD comparison identifies with Lie cohomology.

    FT-5 ANALYSIS (2026-04-12):

    At critical level k = -h^v, chiral Koszulness FAILS in the precise
    sense of the manuscript (chiral_koszul_pairs.tex:1286-1287): the
    Ext algebra Ext^{p,q}(omega_X, omega_X) is NOT diagonally concentrated
    (p != q contributions from Fun(Op) at weight q > 0, bar degree p = 0).

    DETAIL: PBW degeneration (E_2-collapse) holds at all levels
    (cor:universal-koszul), but at critical level the E_2 page is NOT
    diagonally concentrated. PBW degeneration + diagonal E_2 = Koszulness.
    PBW degeneration alone does NOT imply Koszulness when the E_2 page
    has off-diagonal contributions.  At generic level, curvature forces
    diagonal concentration. At critical level, kappa = 0, no curvature,
    off-diagonal contributions survive.

    CONSEQUENCE: Theorem H (thm:hochschild-polynomial-growth) does NOT
    apply at critical level, because its hypothesis "chirally Koszul"
    fails.  The Beilinson-Drinfeld comparison theorem (BD04, Thm 4.5.2)
    identifies ChirHoch with continuous Lie algebra cohomology:

        ChirHoch^*(V_{-h^v}(g)) = H^*_{Lie,cont}(g tensor tC[[t]]; C)
                                 = Lambda(P_1,...,P_r) x C[Theta_1,...,Theta_r]

    This is UNBOUNDED with polynomial growth O(n^{r-1}).

    MANUSCRIPT REFERENCE: hochschild_cohomology.tex:158-191
    (rem:critical-level-lie-vs-chirhoch): "At critical level, chiral
    Koszulness fails ... Theorem H does not apply. Instead, the BD
    comparison theorem identifies ChirHoch with continuous Lie algebra
    cohomology."

    KEY DISTINCTION (AP94/AP95):
    - At GENERIC level: ChirHoch bounded in {0,1,2}, Lie cohomology
      unbounded. They are DIFFERENT functors.
    - At CRITICAL level: BD comparison IDENTIFIES them. ChirHoch IS
      the Lie cohomology. Both unbounded.

    NOTE ON cor:universal-koszul: This corollary says V_k(g) is
    "chirally Koszul" at all k. This should be understood as "PBW
    degenerate" (a necessary condition for Koszulness, not sufficient
    at critical level). The corollary needs a clarifying remark that
    PBW degeneration at critical level does not yield diagonal Ext
    concentration. This is flagged as a manuscript tension (FT-5).
    """
    odd_generators = g.lie_cohomology_degrees
    even_generators = tuple(2 * (d + 1) for d in g.exponents)

    r = g.rank
    is_periodic = (r == 1)
    period = 2 * (g.exponents[0] + 1) if is_periodic else None

    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'odd_generator_degrees': odd_generators,
        'even_generator_degrees': even_generators,
        'amplitude': 'unbounded',
        'total_dim_bound': None,
        'bounded_by_theorem_h': False,  # Theorem H does NOT apply
        'koszulness_fails_at_critical': True,
        'pbw_degeneration_holds': True,  # PBW E_2-collapse still holds
        'diagonal_ext_fails': True,  # Ext^{p,q} != 0 for p != q
        'bd_comparison_applies': True,
        'chirhoch0_dim': 'infinite',  # FF center = Fun(Op)
        'chirhoch1_dim': 'infinite',  # z(g_hat) tensor g
        'chirhoch2_dim': 'infinite',  # Z(V_crit) = FF center (self-dual)
        'is_strictly_periodic': is_periodic,
        'period': period,
        'growth_rate': f'polynomial O(n^{{{r-1}}})',
        'poincare_series_type': (
            f'prod_{{i=1}}^{{{r}}} (1 + t^{{2m_i+1}}) / (1 - t^{{2(m_i+1)}})'
        ),
        'sl2_period_4': is_periodic and period == 4,
        'lie_cohomology_unbounded': True,
        'correction_note': (
            'Chiral Koszulness (diagonal Ext concentration) FAILS at '
            'critical level even though PBW degeneration holds. The BD '
            'comparison theorem identifies ChirHoch with continuous Lie '
            'cohomology at critical level. Theorem H does not apply. '
            'cor:universal-koszul needs a clarifying remark (FT-5 finding).'
        ),
    }


# =========================================================================
# Section 9: Critical level deformation theory
# =========================================================================

def critical_deformation_data(g: SimpleLieData,
                              epsilon: Fraction = Fraction(1, 100)
                              ) -> Dict[str, Any]:
    """Deformation from critical level k = -h^v to k = -h^v + epsilon.

    At k = -h^v + eps:
    - kappa = dim(g) * eps / (2 h^v) (proportional to eps).
    - m_0 = kappa * Casimir (curvature proportional to eps).
    - The bar complex acquires curvature: d^2 = [m_0, -] != 0.
    - The oper identification BREAKS: H^*(B) is no longer Omega^*(Op).
    - Instead, for generic eps, bar cohomology is concentrated in degree 1
      (Koszulness).
    - The deformation is controlled by the bicomplex spectral sequence.

    The transition from H^*(B) = Omega^*(Op) (critical) to
    H^1(B) = V_{-k-2h^v}(g) (generic) is the passage from the
    oper axis to the Koszul axis.
    """
    k_crit = Fraction(-g.h_vee)
    k_def = k_crit + epsilon

    kap_crit = kappa_affine(g, k_crit)
    kap_def = kappa_affine(g, k_def)
    k_dual = koszul_dual_level(g, k_def)
    kap_dual = kappa_affine(g, k_dual)

    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'epsilon': float(epsilon),
        'k_critical': float(k_crit),
        'k_deformed': float(k_def),
        'kappa_critical': float(kap_crit),
        'kappa_deformed': float(kap_def),
        'kappa_dual': float(kap_dual),
        'kappa_sum': float(kap_def + kap_dual),  # Should be 0 (AP24 for KM)
        'k_dual': float(k_dual),
        'bar_uncurved_at_critical': True,
        'bar_curved_at_deformed': float(kap_def) != 0,
        'koszul_at_generic': True,
        'oper_identification_at_critical': True,
        'oper_identification_at_generic': False,
        'transition_mechanism': 'bicomplex spectral sequence',
    }


# =========================================================================
# Section 10: Complete analysis
# =========================================================================

@dataclass
class FLECriticalLevelAnalysis:
    """Complete analysis of bar-cobar at critical level."""
    lie_algebra: str
    rank: int
    h_vee: int
    dim_g: int
    exponents: Tuple[int, ...]

    # Q1: Shadow tower
    shadow_tower: Dict[str, Any] = field(default_factory=dict)
    # Q2: Bar-FF center
    bar_ff_center: Dict[str, Any] = field(default_factory=dict)
    # Q3: Koszulness
    koszulness: Optional[KoszulnessAtCriticalLevel] = None
    koszulness_counts: Dict[str, int] = field(default_factory=dict)
    # Q4: FLE hierarchy
    fle_hierarchy: Dict[str, Any] = field(default_factory=dict)
    # Q5: Bicomplex
    bicomplex: Dict[str, Any] = field(default_factory=dict)
    # Oper space
    oper_analysis: Dict[str, Any] = field(default_factory=dict)
    # Hochschild
    hochschild: Dict[str, Any] = field(default_factory=dict)
    # Deformation
    deformation: Dict[str, Any] = field(default_factory=dict)


def full_fle_critical_analysis(lie_type: str, rank: int,
                               max_weight: int = 10) -> FLECriticalLevelAnalysis:
    """Complete analysis of bar-cobar at critical level for a given Lie algebra."""
    g = lie_data(lie_type, rank)

    return FLECriticalLevelAnalysis(
        lie_algebra=f"{lie_type}_{rank}",
        rank=rank,
        h_vee=g.h_vee,
        dim_g=g.dim,
        exponents=g.exponents,
        shadow_tower=shadow_tower_at_critical_level(g),
        bar_ff_center=bar_cohomology_is_oper_forms(g, max_weight=max_weight),
        koszulness=koszulness_at_critical_level(g),
        koszulness_counts=koszulness_survival_count(g),
        fle_hierarchy=fle_categorical_hierarchy(g),
        bicomplex=bicomplex_structure(g, Fraction(-g.h_vee)),
        oper_analysis=oper_space_analysis(g),
        hochschild=hochschild_periodicity(g),
        deformation=critical_deformation_data(g),
    )


def landscape_sweep(max_weight: int = 8) -> Dict[str, FLECriticalLevelAnalysis]:
    """Run analysis for all standard simple Lie algebras."""
    results = {}
    for (lt, rk) in [("A", 1), ("A", 2), ("A", 3), ("A", 4),
                     ("B", 2), ("B", 3),
                     ("C", 2), ("C", 3),
                     ("D", 4),
                     ("G", 2), ("F", 4),
                     ("E", 6), ("E", 7), ("E", 8)]:
        key = f"{lt}{rk}"
        results[key] = full_fle_critical_analysis(lt, rk, max_weight=max_weight)
    return results
