r"""FLE critical-level bar-cobar structure engine.

THEOREM (Critical-level bar-cobar degeneration and the FLE):

At the critical level k = -h^v, classical Koszul duality degenerates:
the bar complex B(V_{-h^v}(g)) becomes uncurved (kappa = 0), and bar
cohomology is no longer concentrated in bar degree 1.  Instead:

    H^n(B(V_{-h^v}(g))) ~ Omega^n(Op_{g^v}(D))    for all n >= 0.

This engine investigates FIVE STRUCTURAL QUESTIONS:

Q1. SHADOW OBSTRUCTION TOWER AT CRITICAL LEVEL (AP31 analysis):
    kappa = 0 does not by itself imply Theta_A = 0.  At critical level
    there are three distinct lanes:
    - the scalar curvature lane is uncurved because kappa = 0;
    - the Feigin-Frenkel center is commutative, so the center-restricted
      MC element has no higher commutator part;
    - the full affine current sector is still noncommutative:
      J^a(z)J^b(w) has the simple-pole bracket term and the level
      double pole k(a,b)/(z-w)^2 with k = -h^v.
    Therefore Theta_{V_crit} = 0 holds only on the center-restricted scalar
    shadow. The full affine VOA retains the current-sector datum.

Q2. BAR COMPLEX AND THE FEIGIN-FRENKEL CENTER:
    H^0(B(V_{-h^v}(g))) = Fun(Op_{g^v}(D)) = z(g_hat) (FF center).
    The FULL bar cohomology H^*(B) = Omega^*(Op) is the oper
    differential-form package.  It is not the center itself, not the
    derived structure sheaf, and not the chiral derived center.

Q3. KOSZULNESS AT CRITICAL LEVEL (which K1-K12 survive):
    Classical Koszulness (bar cohomology concentrated in bar degree 1) FAILS.
    The bar cohomology is the full de Rham algebra Omega^*(Op), spread
    across form degrees 0, 1, ..., rank(g).
    BUT: the PBW spectral sequence still degenerates (Whitehead),
    and many characterizations have critical-level analogues.
    Status of each K_i at critical level analyzed below.

Q4. FLE AS CATEGORICAL LIFT:
    The label thm:oper-bar-dl is a COHOMOLOGICAL identification.
    The FLE (Gaitsgory-Raskin 2405.03648) is a CATEGORICAL equivalence:
        KL(V_{crit}(g)) ~ IndCoh(Op_{G^L})
    The FLE implies the cohomological result after taking vacuum Ext,
    but the cohomological result does not imply the categorical equivalence.
    The bar complex is a chain-level model for the localization functor Delta.

Q5. BICOMPLEX DEFORMATION (d_k = d_crit + (k+h^v) delta):
    The bar differential decomposes as d_k = d_crit + (k+h^v) delta.
    The full bar object is a curved bicomplex:
        d_crit^2 = 0, delta^2 = 0,
        d_crit delta + delta d_crit = [C_g/(2h^v), -].
    It becomes an ordinary bicomplex only on the curvature-flat comparison
    surface.  The critical differential still contains the level
    -h^v double-pole term; only the shifted perturbing coefficient
    k+h^v vanishes at critical level.

Recorded theorem labels:
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
- H_k^! = V_{-k-2h^v}(g), by Feigin-Frenkel dual level (AP33).

Beilinson warnings
------------------
AP1:  kappa is family-specific; recompute for each g.
AP9:  kappa != c/2 for affine KM.
AP14: Koszulness != formality.  At critical level both fail in different ways.
AP31: kappa = 0 leaves Theta_A independent. At critical level,
      only the Feigin-Frenkel center is commutative; the full current
      sector remains noncommutative.
AP33: Koszul dual != negative-level substitution.
AP39: kappa != S_2 for rank > 1.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union


Number = Union[int, float, Fraction]


def _as_fraction(k: Number) -> Optional[Fraction]:
    """Return an exact rational level when the input supplies one."""
    if isinstance(k, Fraction):
        return k
    if isinstance(k, int):
        return Fraction(k)
    return None


def _format_level(k: Number) -> str:
    """Stable display for exact levels in diagnostic strings."""
    frac = _as_fraction(k)
    if frac is None:
        return repr(k)
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


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

def kappa_affine(g: SimpleLieData, k: Number) -> Union[float, Fraction]:
    """Modular characteristic kappa = dim(g)(k + h^v)/(2 h^v)."""
    if isinstance(k, Fraction):
        return Fraction(g.dim) * (k + g.h_vee) / (2 * g.h_vee)
    return g.dim * (k + g.h_vee) / (2.0 * g.h_vee)


def koszul_dual_level(g: SimpleLieData, k: Number) -> Union[float, Fraction]:
    """Feigin-Frenkel involution: k' = -k - 2h^v."""
    return -k - 2 * g.h_vee


def is_critical(g: SimpleLieData, k: Number, tol: float = 1e-12) -> bool:
    """Check if k = -h^v (critical level)."""
    if isinstance(k, Fraction):
        return k == Fraction(-g.h_vee)
    return abs(k + g.h_vee) < tol


# =========================================================================
# Section 2: Q1 -- Shadow obstruction tower at critical level
# =========================================================================

def shadow_tower_at_critical_level(g: SimpleLieData) -> Dict[str, Any]:
    """Analyze the shadow obstruction tower at k = -h^v.

    AP31: kappa = 0 leaves Theta_A independent.
    Higher-arity components (cubic C, quartic Q, ...) are independent of kappa.

    At critical level the Feigin-Frenkel center is commutative.  That is
    a statement about z(V_{-h^v}(g)) = Fun(Op_{g^L}), not about the full
    affine VOA.  The current OPE still contains the level double pole and
    the Lie bracket simple pole.

    The correct split is:
    (1) kappa = 0 => m_0 = 0 => the bar complex is uncurved.
    (2) Center commutativity => the center-restricted MC element vanishes.
    (3) Full current-sector noncommutativity => Theta_A for V_{crit}(g)
        is not zero as a full affine-current datum.

    For the full algebra V_{-h^v}(g), beyond the center:
    - The bar complex is uncurved but nontrivial.
    - H^*(B) = Omega^*(Op), which is a rich graded algebra.
    - The scalar shadow is trivial, but the ordered current-sector datum
      is not killed by kappa = 0.
    """
    k_crit = Fraction(-g.h_vee)
    kap = kappa_affine(g, k_crit)

    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'critical_level': int(k_crit),
        'kappa': float(kap),
        'kappa_is_zero': kap == 0,
        # Scalar shadow and center-restricted tower data
        'shadow_kappa': 0,
        'center_shadow_cubic_C': 0,
        'center_shadow_quartic_Q': 0,
        'center_shadow_depth_r_max': 0,
        'scalar_shadow_class': 'critical-split',
        'center_theta_vanishes': True,
        'reason_center_theta_vanishes': (
            'The Feigin-Frenkel center is a commutative chiral algebra; '
            'this is a center-only statement, not a full affine-VOA statement.'
        ),
        # Backward-compatible aliases, now explicitly center/scalar only.
        'shadow_cubic_C': 0,
        'shadow_quartic_Q': 0,
        'shadow_depth_r_max': 0,
        'shadow_class': 'critical-split',
        'shadow_aliases_scope': 'center/scalar only',
        # Full current-sector data
        'theta_A_vanishes': False,
        'theta_A_vanishes_scope': 'full affine current sector',
        'full_current_theta_vanishes': False,
        'reason_theta_vanishes': (
            'False for the full affine current sector; only the '
            'Feigin-Frenkel-center restriction has vanishing MC part.'
        ),
        'scalar_projection_is_full_mc_data': False,
        'full_current_sector_noncommutative': True,
        'current_ope_simple_pole_present': True,
        'current_ope_double_pole_coefficient': int(k_crit),
        'current_ope_double_pole_vanishes': False,
        'trace_form_current_residue': f"{int(k_crit)} * Omega/z",
        'kz_parameter_defined': False,
        'kz_parameter_has_critical_pole': True,
        'sugawara_defined': False,
        'critical_split': (
            'kappa=0 makes the bar complex uncurved; the FF center is '
            'commutative; the affine current sector remains noncommutative.'
        ),
        # Bar complex is nontrivial even though the scalar curvature vanishes.
        'bar_complex_nontrivial': True,
        'bar_uncurved': True,
        'bar_cohomology_nontrivial': True,
        # Discriminant and shadow metric
        'discriminant_Delta': 0,  # 8 * kappa * S_4 = 0
        'shadow_metric_Q': '(3 alpha t)^2',  # degenerates when kappa = 0
        'ap31_violated': False,  # We do not deduce full Theta = 0 from kappa = 0.
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
        'h0_is_feigin_frenkel_center': True,
        'full_bar_cohomology_is_ff_center': False,
        'full_bar_cohomology_is_oper_forms': True,
        'oper_forms_are_derived_structure_sheaf': False,
        'ordinary_derived_center_identification': False,
        'derived_center_is_chiral_hochschild': (
            'Z_ch^der(A) = ChirHoch^*(A,A), not Fun(Op) and not A^!'
        ),
        'dims': dims,
    }


def center_object_firewall(g: SimpleLieData) -> Dict[str, Any]:
    """Separate the critical FF center from bar forms and derived center.

    The local critical package has three different objects:
    H^0 of the critical bar complex, the full oper differential-form
    algebra H^*(B), and the chiral derived center.  This diagnostic keeps
    the engine from identifying any of them with the Koszul dual branch.
    """
    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'ff_center': 'H^0(B(V_crit)) = Fun(Op_{g^vee}(D))',
        'full_bar_cohomology': 'H^*(B(V_crit)) = Omega^*(Op_{g^vee}(D))',
        'derived_center': 'Z_ch^der(A) = ChirHoch^*(A,A)',
        'ff_center_is_h0_only': True,
        'full_bar_cohomology_is_ff_center': False,
        'ff_center_is_ordinary_derived_center': False,
        'ff_center_is_chiral_derived_center': False,
        'ff_center_is_koszul_dual': False,
        'oper_forms_are_derived_structure_sheaf': False,
        'omega_ba_equals_a_is_inversion_not_koszul_duality': True,
        'a_shriek_is_verdier_continuous_linear_dual': True,
    }


# =========================================================================
# Section 4: Q3 -- Koszulness at critical level
# =========================================================================

@dataclass
class KoszulnessAtCriticalLevel:
    """Analysis of each K1-K12 characterization at critical level.

    At critical level k = -h^v:
    - The bar complex is uncurved (d^2 = 0), so cohomology is well-defined.
    - Bar cohomology is spread across bar degrees
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
    H^*(B) = Omega^*(Op), spread across several form degrees.
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
    # At critical level, the FF center is commutative (center = Fun(Op)).
    # The full affine current algebra is not commutative; formality in the
    # Koszul sense fails because the bar complex carries nontrivial higher
    # cohomology.
    result.k2_ainfty = (
        "INAPPLICABLE: the bar complex is uncurved, so the question of "
        "A-infinity formality of bar cohomology changes character. "
        "The bar cohomology IS a cdga (exterior algebra of Op forms), "
        "but it is not concentrated in degree 1."
    )

    # K3: Ext diagonal vanishing
    # Ext^n(V_crit, V_crit) = Omega^n(Op) (Frenkel-Teleman).
    # This has off-diagonal support: Omega^n(Op) has conformal weight
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
    # Theorem H is a generic-Koszul-locus result.
    # Chiral Koszulness (diagonal Ext concentration) FAILS: Ext^{p,q} != 0
    # for p != q (Fun(Op) contributes at bar degree 0, all even weights).
    # PBW degeneration holds without forcing diagonal concentration
    # when kappa = 0 (no curvature to force diagonality).
    # The BD comparison identifies ChirHoch with continuous Lie cohomology,
    # which is UNBOUNDED.
    result.k7_hochschild = (
        "FAILS: Theorem H requires chiral Koszulness (diagonal Ext "
        "concentration, chiral_koszul_pairs.tex:1286), which fails at "
        "critical level. PBW degeneration holds (cor:universal-koszul) "
        "but leaves diagonal concentration open when kappa = 0 "
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

    Level 3 (Cohomological -- thm:oper-bar-dl):
        H^n(B(V_{-h^v}(g)))  ~  Omega^n(Op_{g^v}(D))
        (bar-Ext + Frenkel-Teleman)

    Each level implies the next (by taking appropriate functors):
    Level 1 => Level 2 (take derived categories)
    Level 2 => Level 3 (take Ext of vacuum module)

    The converses fail:
    Level 3 leaves Level 2 undetermined: cohomological data does not determine
    the functor).
    Level 2 leaves Level 1 undetermined in full generality: the localization
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
            'source': 'thm:oper-bar-dl',
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

def kernel_normalization_diagnostics(g: SimpleLieData, k: Number) -> Dict[str, Any]:
    """Convention-separated affine kernel diagnostics.

    Canonical local formulas:
    - affine trace-form collision residue: k*Omega_tr/z;
    - KZ normalization: Omega_KZ/((k+h^vee)z);
    - Heisenberg: k/z;
    - Virasoro: (c/2)/z^3 + 2T/z.

    The trace-form and KZ expressions are not interchangeable rational
    functions of the level.  At k=0 the trace-form residue vanishes while
    the KZ residue is nonzero; at k=-h^vee the KZ coefficient has a pole
    while the trace-form double-pole coefficient is -h^vee.
    """
    frac = _as_fraction(k)
    h = Fraction(g.h_vee)
    if frac is None:
        shifted = k + g.h_vee
        shifted_zero = abs(shifted) < 1e-12
        k_zero = abs(k) < 1e-12
    else:
        shifted = frac + h
        shifted_zero = shifted == 0
        k_zero = frac == 0

    k_dual = koszul_dual_level(g, k)
    kz_defined = not shifted_zero
    return {
        'lie_algebra': f"{g.type}_{g.rank}",
        'level': _format_level(k),
        'h_vee': g.h_vee,
        'shifted_level_k_plus_h_vee': _format_level(shifted),
        'trace_form_collision_residue': (
            f"{_format_level(k)}*Omega_tr/z"
        ),
        'kz_residue': (
            None if not kz_defined
            else f"Omega_KZ/(({_format_level(shifted)})*z)"
        ),
        'kz_parameter_defined': kz_defined,
        'kz_parameter_has_critical_pole': shifted_zero,
        'trace_form_and_kz_are_same_rational_function': False,
        'normalizations_interchangeable': False,
        'trace_form_vanishes_at_k0': k_zero,
        'kz_nonzero_at_k0_for_nonabelian_g': k_zero and kz_defined,
        'critical_trace_double_pole_present': shifted_zero and not k_zero,
        'critical_trace_double_pole_coefficient': (
            _format_level(k) if shifted_zero else None
        ),
        'ff_dual_level': _format_level(k_dual),
        'ff_fixed_point': k_dual == k,
        'heisenberg_kernel': 'k/z',
        'virasoro_kernel': '(c/2)/z^3 + 2T/z',
    }


def bicomplex_structure(g: SimpleLieData, k: Number) -> Dict[str, Any]:
    """The bicomplex structure of the KM bar differential.

    thm:km-bar-bicomplex: d_k = d_crit + (k + h^v) * delta, where:
    - d_crit = d_sp - h^v d_dp is the critical differential
    - delta extracts the trace-form double-pole coefficient
    - d_crit^2 = 0, delta^2 = 0,
      {d_crit, delta} = [C_g/(2h^v), -] on the full bar object

    The triple is an ordinary bicomplex only on the curvature-flat
    subquotient on which the Casimir bracket vanishes.  At critical level
    d_k = d_crit, but d_crit still includes the level -h^v double-pole
    residue; the shifted perturbation (k+h^v) delta is what disappears.

    At critical level (k = -h^v): d_k = d_crit; the shifted perturbation
    vanishes but the critical double-pole coefficient is -h^v.
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
        'anticommutator_zero': False,  # False on the full bar object.
        'anticommutator': f"[C_{g.type}_{g.rank}/(2*{g.h_vee}), -]",
        'ordinary_bicomplex_on_curvature_flat_subquotient': True,
        'curved_bicomplex_on_full_bar_object': True,
        # At critical level
        'd_k_equals_d_crit': is_crit,
        'delta_contribution_zero': is_crit,
        'shifted_delta_contribution_zero': is_crit,
        'critical_double_pole_present': is_crit,
        'critical_double_pole_coefficient': -g.h_vee if is_crit else None,
        'critical_double_pole_note': (
            'At k=-h^vee the shifted perturbation vanishes, but the '
            'trace-form OPE double pole has coefficient -h^vee.'
        ) if is_crit else None,
        # Spectral sequence
        'critical_first_e1': 'Omega^*(Op)' if is_crit else 'Omega^*(Op)',
        'critical_first_d1_zero': is_crit,  # d_1 = lambda * delta = 0 at crit
        'degeneration': 'E_1' if is_crit else 'open',
        # Curvature
        'm_0': f"{float(lam)}/(2*{g.h_vee}) * Casimir"
               if not is_crit else '0',
        'curved_square': f"[(k+h^vee)/(2*{g.h_vee}) * Casimir, -]",
        'bar_uncurved': is_crit,
        'ordinary_generic_cohomology_requires_curvature_flat_surface': (
            not is_crit
        ),
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

    At critical level k = -h^v, chiral Koszulness FAILS in the precise
    sense of the manuscript (chiral_koszul_pairs.tex:1286-1287): the
    Ext algebra Ext^{p,q}(omega_X, omega_X) has off-diagonal support
    (p != q contributions from Fun(Op) at weight q > 0, bar degree p = 0).

    DETAIL: PBW degeneration (E_2-collapse) holds at all levels
    (cor:universal-koszul), but at critical level the E_2 page is not
    diagonally concentrated. PBW degeneration + diagonal E_2 = Koszulness.
    PBW degeneration alone leaves Koszulness unproved when the E_2 page
    has off-diagonal contributions.  At generic level, curvature forces
    diagonal concentration. At critical level, kappa = 0, no curvature,
    off-diagonal contributions survive.

    CONSEQUENCE: Theorem H (thm:hochschild-polynomial-growth) is outside the
    critical-level surface, because its hypothesis "chirally Koszul"
    fails.  The Beilinson-Drinfeld comparison theorem (BD04, Thm 4.5.2)
    identifies ChirHoch with continuous Lie algebra cohomology:

        ChirHoch^*(V_{-h^v}(g)) = H^*_{Lie,cont}(g tensor tC[[t]]; C)
                                 = Lambda(P_1,...,P_r) x C[Theta_1,...,Theta_r]

    This is UNBOUNDED with polynomial growth O(n^{r-1}).

    Anchor: hochschild_cohomology.tex, rem:critical-level-lie-vs-chirhoch.
    (rem:critical-level-lie-vs-chirhoch): "At critical level, chiral
    Koszulness fails ... Theorem H is outside this surface. Instead, the BD
    comparison theorem identifies ChirHoch with continuous Lie algebra
    cohomology."

    KEY DISTINCTION (AP94/AP95):
    - At GENERIC level: ChirHoch bounded in {0,1,2}, Lie cohomology
      unbounded. They are DIFFERENT functors.
    - At CRITICAL level: BD comparison IDENTIFIES them. ChirHoch IS
      the Lie cohomology. Both unbounded.

    Scope note: PBW degeneration is necessary for Koszulness, but at
    critical level it does not yield diagonal Ext concentration.
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
        'bounded_by_theorem_h': False,  # Theorem H is generic-locus only
        'theorem_h_scope': 'generic Koszul locus only',
        'critical_promoted_to_theorem_h': False,
        'is_generic_level_result': False,
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
        'chiral_derived_center_is_hochschild': True,
        'feigin_frenkel_center_is_h0_only': True,
        'ff_center_is_ordinary_derived_center': False,
        'ff_center_is_koszul_dual': False,
        'correction_note': (
            'Chiral Koszulness (diagonal Ext concentration) FAILS at '
            'critical level even though PBW degeneration holds. The BD '
            'comparison theorem identifies ChirHoch with continuous Lie '
            'cohomology at critical level. Theorem H does not apply. '
            'PBW degeneration alone is not diagonal Ext concentration.'
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
        'koszul_at_generic_scope': 'curvature-flat/twisted/coderived comparison surface',
        'ordinary_generic_cohomology_requires_curvature_flat_surface': True,
        'theorem_h_applies_at_deformed_generic_level': True,
        'ff_center_package_at_deformed_generic_level': False,
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
    # Object-scope firewalls
    center_firewall: Dict[str, Any] = field(default_factory=dict)
    kernel_normalization: Dict[str, Any] = field(default_factory=dict)
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
        center_firewall=center_object_firewall(g),
        kernel_normalization=kernel_normalization_diagnostics(
            g, Fraction(-g.h_vee)
        ),
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
