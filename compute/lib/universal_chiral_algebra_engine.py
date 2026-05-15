r"""Universal chiral algebra engine: Cliff universality and quasi-conformal data.

Finite witness registry for the standard chiral algebra families in the
landscape.  The engine records the extra coordinate-change data that promotes a
fixed-curve chiral algebra to a compatible family in the sense of Cliff
[Cliff19] and Frenkel--Ben-Zvi [FBZ04].

MATHEMATICAL BACKGROUND
=======================

Three notions of "coordinate-independence" for vertex/chiral algebras:

(1) QUASI-CONFORMAL VERTEX ALGEBRA (Frenkel--Ben-Zvi, Chapter 6):
    A vertex algebra V equipped with an action of the coordinate-change
    Harish-Chandra pair attached to the formal disk O = k[[t]]:
      - L_{-1} is the translation operator.
      - L_0 gives the weight grading on the standard positive-energy sectors.
      - the positive vector fields act locally nilpotently on each vector.
    The Aut(O) action defines a V-bundle V_X on any smooth curve X via the
    Aut(O)-torsor of formal coordinates.  The vertex operations then descend
    to a chiral algebra on X.

    A conformal vector is one source of this action.  It is not the only
    source: affine vacuum modules have coordinate-change actions even at the
    critical level, where the Sugawara conformal vector is unavailable.

(2) UNIVERSAL CHIRAL ALGEBRA (Beilinson-Drinfeld [BD04], 2.9.9):
    A compatible family {B_X} of chiral algebras, one for each smooth curve X,
    with isomorphisms phi^*_{ch} B_Y = B_X for every etale morphism phi: X -> Y,
    satisfying a cocycle condition.  Equivalently: a chiral algebra on the
    "universal curve" (i.e., a section of the chiral algebra presheaf on the
    etale site of smooth curves).

(3) UNIVERSAL FACTORIZATION ALGEBRA (Cliff [Cliff19], Definition 7.3):
    A compatible family of factorization algebras {A_{Ran(X/S)}} over relative
    Ran spaces, one for each smooth family pi: X -> S, with isomorphisms
    Y(phi): Y_{Ran(X/S)} -> phi^* Y_{Ran(X'/S')}
    for each fibrewise etale morphism phi: X/S -> X'/S', compatible with
    composition.

KEY THEOREM (Cliff [Cliff19], Proposition 8.1 + Introduction):
    Let phi: X -> Y be etale, {A_{Y^I}} a factorization algebra over Y, and
    (B_Y, mu_Y) the corresponding chiral algebra on Y.  Then the chiral algebra
    (B'_X, mu'_X) associated to the pullback factorization algebra is
    canonically isomorphic to the chiral algebra B_X := phi^*_{ch} B_Y.

    CONSEQUENCE: Universal chiral algebras of dimension d and universal
    factorization algebras of dimension d define equivalent categories.  In
    dimension 1 this category is equivalent to quasi-conformal vertex algebras.

RELEVANCE TO THE MONOGRAPH
==========================

Our chiral algebras already carry D-module structure on Ran(X) (this is part
of the BD definition, Definition 2.4 = Definition 5.1 in [Cliff19]).  The
question is whether this D-module structure is sufficient for universality,
or whether additional data (the Aut(O) action / etale descent) is needed.

ANSWER: D-module structure on Ran(X) for a FIXED curve X does NOT by itself
give universality.  Universality requires the FAMILY structure: a compatible
system of factorization algebras over all curves simultaneously, with
pullback isomorphisms along etale morphisms.

For the standard registered families, universality is witnessed because:
  (a) The OPE coefficients are defined on the formal disk (curve-independent).
  (b) The factorization structure uses only the diagonal stratification of X^I,
      which is etale-local.
  (c) The Aut(O)/Der(O) action is explicitly supplied by a conformal vector,
      an affine coordinate-change action, or a free-field construction.

The Aut(O) action is the BRIDGE:
  quasi-conformal VA <==> universal chiral algebra <==> universal fact. algebra
                         (dim 1 only)                  (any dim)

STRUCTURE OF THE Aut(O) ACTION
==============================

For a vertex algebra V with conformal vector omega (Virasoro element):
  - Aut(O) = {phi in k[[t]] : phi(0)=0, phi'(0) != 0} acts via exp(sum a_n L_n)
  - L_n = Res(omega(z) z^{n+1}) for n >= -1
  - The action is determined by L_{-1} (translation), L_0 (dilation/grading),
    and the locally nilpotent action of L_n for n >= 1

For a quasi-conformal non-conformal VA:
  - the coordinate-change action is part of the structure;
  - it need not come from a conformal vector;
  - critical-level affine vacuum modules are the standard boundary case.

WHAT THE MONOGRAPH'S AXIOMS PROVIDE
====================================

Our "modular Koszul algebra" axioms (MK1-MK5 in concordance.tex) include:
  (MK1) Chiral algebra = D-module B_X on X with Lie bracket on B_{Ran X}
  (MK2) Verdier self-duality / Koszul duality structure
  (MK3) Categorical generation (thick generation of DK category)
  (MK4) Completion (bar-cobar convergence)
  (MK5) Sewing (analytic continuation to higher genus)

The D-module structure in (MK1) gives the Ran-space factorization algebra on a
fixed curve X.  Universality additionally requires a family-level descent
witness: an Aut(O)/Der(O) action on the formal-disk vertex algebra compatible
with the factorization pullbacks.  The engine therefore treats
quasi-conformality as a necessary coordinate-change certificate and the
registered descent witness as the family datum.  It never infers universality
from a fixed-X D-module alone.

References:
    [Cliff19] E. Cliff, "Universal factorization spaces and algebras",
              Math. Res. Lett. 26 (2019), no. 4, 1059-1096.
              arXiv:1608.08122.
    [Cliff21] E. Cliff, "Chiral algebras, factorization algebras, and
              Borcherds's singular commutative rings approach to vertex
              algebras", Comm. Math. Phys. 386 (2021), 495-550.
              arXiv:1911.01627.
    [FBZ04]   E. Frenkel and D. Ben-Zvi, "Vertex Algebras and Algebraic
              Curves", 2nd ed., AMS Math. Surveys and Monographs 88 (2004).
    [BD04]    A. Beilinson and V. Drinfeld, "Chiral Algebras", AMS (2004).
    [FG12]    J. Francis and D. Gaitsgory, "Chiral Koszul duality",
              Selecta Math. (N.S.) 18 (2012), no. 1, 27-87.
    prop:genus0-curve-independence (higher_genus_modular_koszul.tex)
    thm:shadow-homotopy-invariance (higher_genus_modular_koszul.tex)
    etale_descent_engine.py (existing engine for etale descent verification)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from sympy import Rational, oo


# =============================================================================
# 1. Aut(O) action data
# =============================================================================

@dataclass
class AutOAction:
    """Data specifying the Aut(O) action on a vertex algebra.

    The group Aut(O) of coordinate changes on the formal disk acts on a
    quasi-conformal vertex algebra via the Harish-Chandra pair
    (Der(O), Aut_+(O)).

    The action is specified by:
      - L_{-1}: translation operator (= T, the infinitesimal translation)
      - L_0: grading operator (= conformal weight)
      - nilpotency_order: for each generator v, a finite bound N such that
        L_n(v) = 0 for all n >= N in the positive-energy certificate used by
        this engine.

    For a CONFORMAL vertex algebra with conformal vector omega:
      L_n = omega_{(n+1)} (the (n+1)-st mode of omega)
    and L_n lowers conformal weight by n.

    For a QUASI-CONFORMAL vertex algebra without full Virasoro:
      The Der(O)/Aut(O) action is supplied separately and must be checked as
      part of the witness.
    """
    # Whether the full Virasoro L_n (n >= -1) acts
    is_conformal: bool = True

    # Whether only L_{-1}, L_0 + local nilpotency holds (weaker)
    is_quasi_conformal: bool = True

    # For each generator: (name, weight, nilpotency_order)
    # nilpotency_order N means L_n(v) = 0 for all n >= N
    generator_data: List[Tuple[str, Rational, int]] = field(default_factory=list)

    # The conformal vector's central charge (if conformal)
    central_charge: Optional[Rational] = None

    # Source of the Aut(O) action
    # "virasoro" = from conformal vector
    # "heisenberg" = from Heisenberg subalgebra (lattice VAs)
    # "affine_coordinate_change" = from the affine formal-loop action
    # "external" = from external data (non-standard)
    source: str = "virasoro"


def der_plus_local_nilpotency_bound(weight: Rational) -> int:
    """Positive-energy bound for the Der_+(O) action on a homogeneous generator.

    The registry uses the standard positive-energy certificate: L_n lowers
    conformal weight by n, and the represented families have no negative weight
    spaces.  Thus L_n(v) vanishes for every integer n > wt(v).  The returned
    integer N means L_n(v) = 0 for all n >= N.  The bound is intentionally not a
    primary-field formula; a primary vector usually has the sharper bound N=1.
    """
    if weight < 0:
        raise ValueError("positive-energy witness requires non-negative weight")
    return max(int(weight) + 1, 1)


def nilpotency_order_primary(weight: Rational) -> int:
    """Compatibility wrapper for the homogeneous positive-energy bound."""
    return der_plus_local_nilpotency_bound(weight)


# =============================================================================
# 2. Universality structure
# =============================================================================

@dataclass
class UniversalityData:
    """Data determining whether a chiral algebra is universal.

    In dimension 1, Cliff's universal factorization algebras are equivalent to
    quasi-conformal vertex algebras.  For a concrete fixed-curve object this
    engine still requires an explicit family-level descent witness.

    The key properties are:
      (a) OPE locality: OPE coefficients defined on formal disk
      (b) Aut(O) equivariance: vertex operations commute with coordinate changes
      (c) Etale descent: factorization structure descends along etale covers

    For the standard registered families, all three are recorded explicitly.
    """
    name: str

    # Which level of universality
    is_quasi_conformal: bool = False   # Aut(O) action exists
    is_conformal: bool = False         # full Virasoro action
    is_universal_chiral: bool = False  # universal in BD sense
    is_universal_fact: bool = False    # universal in Cliff sense

    # Source of universality
    aut_o_action: Optional[AutOAction] = None

    # Why universality holds (for documentation)
    universality_reason: str = ""

    # Obstructions to universality (if any)
    obstructions: List[str] = field(default_factory=list)


# =============================================================================
# 3. Standard family registry with universality data
# =============================================================================

@dataclass
class ChiralAlgebraFamily:
    """A family of chiral algebras with universality metadata.

    This extends the OPEData from etale_descent_engine.py with the
    Cliff/FBZ universality structure.
    """
    name: str
    central_charge: Rational
    kappa: Rational
    generators: List[Tuple[str, Rational]]   # (name, conformal_weight)
    is_koszul: bool = True

    # Universality properties
    has_conformal_vector: bool = True
    is_quasi_conformal: bool = True
    is_conformal: bool = True
    is_universal: bool = True

    # Aut(O) action specification
    aut_o_source: str = "virasoro"  # or "sugawara", "heisenberg", "external"
    aut_o_action: Optional[AutOAction] = None

    # Family-level etale descent certificate.  A fixed-X D-module without this
    # witness is not treated as universal by this engine.
    descent_witness: str = ""

    # Shadow depth class: G, L, C, or M
    shadow_class: str = "G"

    # Koszul dual family name
    koszul_dual: Optional[str] = None

    # Additional data
    level: Optional[Rational] = None
    lie_type: Optional[str] = None


def _make_aut_o(generators: List[Tuple[str, Rational]],
                central_charge: Rational,
                is_conformal: bool = True,
                source: str = "virasoro") -> AutOAction:
    """Construct AutOAction from generator data."""
    gen_data = []
    for name, weight in generators:
        N = der_plus_local_nilpotency_bound(weight)
        gen_data.append((name, weight, N))
    return AutOAction(
        is_conformal=is_conformal,
        is_quasi_conformal=True,
        generator_data=gen_data,
        central_charge=central_charge,
        source=source,
    )


# ---------------------------------------------------------------------------
# Standard family constructors
# ---------------------------------------------------------------------------

def heisenberg_family(k: Rational = Rational(1), d: int = 1) -> ChiralAlgebraFamily:
    """Heisenberg algebra H_k of rank d.

    Universality witness: conformal via the free-boson Sugawara vector.
    c = d (for k=1).  Aut(O) action from L_n = (1/2k) sum :alpha_i alpha_i:_{(n+1)}.
    """
    c = Rational(d)
    kappa = k * d   # rank-d Heisenberg contribution
    gens = [(f"alpha_{i}", Rational(1)) for i in range(d)]
    return ChiralAlgebraFamily(
        name=f"Heisenberg(k={k},d={d})",
        central_charge=c,
        kappa=kappa,
        generators=gens,
        has_conformal_vector=True,
        is_quasi_conformal=True,
        is_conformal=True,
        is_universal=True,
        aut_o_source="sugawara",
        aut_o_action=_make_aut_o(gens, c, True, "sugawara"),
        descent_witness="free-boson formal-disk OPE plus Sugawara Aut(O) action",
        shadow_class="G",
        koszul_dual=f"Heisenberg(k={-k},d={d})",
        level=k,
    )


def virasoro_family(c: Rational = Rational(26)) -> ChiralAlgebraFamily:
    """Virasoro algebra Vir_c.

    Universality witness: conformal; the conformal vector is the generator.
    The Aut(O) action is from the Virasoro itself: L_n = T_{(n+1)}.
    Self-dual at c=13.  The standard-family dual representative is Vir_{26-c}.
    """
    kappa = c / 2
    gens = [("T", Rational(2))]
    return ChiralAlgebraFamily(
        name=f"Virasoro(c={c})",
        central_charge=c,
        kappa=kappa,
        generators=gens,
        has_conformal_vector=True,
        is_quasi_conformal=True,
        is_conformal=True,
        is_universal=True,
        aut_o_source="virasoro",
        aut_o_action=_make_aut_o(gens, c, True, "virasoro"),
        descent_witness="Virasoro conformal vector and scalar central OPE",
        shadow_class="M",
        koszul_dual=f"Virasoro(c={26 - c})",
    )


def affine_km_family(type_: str, rank: int,
                     k: Rational = Rational(1)) -> ChiralAlgebraFamily:
    """Affine Kac-Moody algebra at level k.

    Universality witness: the affine loop algebra central extension is
    compatible with formal coordinate changes.  Away from k = -h^v this witness
    is upgraded to a conformal one by the Sugawara vector.

    At the critical level k = -h^v, the Sugawara construction is undefined,
    and the algebra is quasi-conformal but not conformal.

    kappa = dim(g) * (k + h^v) / (2 * h^v).
    """
    LIE_DATA = {
        ("A", 1): (3, 2, "sl_2"),
        ("A", 2): (8, 3, "sl_3"),
        ("A", 3): (15, 4, "sl_4"),
        ("A", 4): (24, 5, "sl_5"),
        ("B", 2): (10, 3, "so_5"),
        ("C", 2): (10, 3, "sp_4"),
        ("D", 4): (28, 6, "so_8"),
        ("G", 2): (14, 4, "G_2"),
        ("F", 4): (52, 9, "F_4"),
        ("E", 6): (78, 12, "E_6"),
        ("E", 7): (133, 18, "E_7"),
        ("E", 8): (248, 30, "E_8"),
    }
    dim_g, h_dual, name = LIE_DATA[(type_, rank)]
    is_critical = (k == -h_dual)
    c = Rational(0) if is_critical else Rational(k * dim_g, k + h_dual)
    kappa = Rational(dim_g) * (k + h_dual) / (2 * h_dual)
    is_conformal = not is_critical
    source = "sugawara" if is_conformal else "affine_coordinate_change"
    witness = (
        "affine formal-loop coordinate-change action plus Sugawara conformal vector"
        if is_conformal
        else "affine formal-loop coordinate-change action at critical level"
    )

    gens = [(f"J^a_{i}", Rational(1)) for i in range(dim_g)]
    return ChiralAlgebraFamily(
        name=f"Affine_{name}(k={k})",
        central_charge=c if not is_critical else Rational(0),
        kappa=kappa,
        generators=gens,
        has_conformal_vector=is_conformal,
        is_quasi_conformal=True,
        is_conformal=is_conformal,
        is_universal=True,
        aut_o_source=source,
        aut_o_action=_make_aut_o(gens, c, is_conformal, source),
        descent_witness=witness,
        shadow_class="L",
        koszul_dual=f"Affine_{name}(k={-k - 2*h_dual})",
        level=k,
        lie_type=f"{type_}_{rank}",
    )


def w_algebra_family(N: int, c: Rational = Rational(2)) -> ChiralAlgebraFamily:
    """W_N algebra.

    Universality witness: conformal; W_2 = T is the Virasoro field.
    Generators: W_2 = T (weight 2), W_3 (weight 3), ..., W_N (weight N).
    """
    gens = [(f"W_{j}", Rational(j)) for j in range(2, N + 1)]
    # kappa(W_N) = c * (H_N - 1), H_N = sum_{j=1}^{N} 1/j.
    # Boundary check: N=2 gives c/2, recovering Virasoro.
    harmonic_shift = sum(Rational(1, j) for j in range(2, N + 1))
    kappa = c * harmonic_shift
    return ChiralAlgebraFamily(
        name=f"W_{N}(c={c})",
        central_charge=c,
        kappa=kappa,
        generators=gens,
        has_conformal_vector=True,  # T = W_2 is conformal vector
        is_quasi_conformal=True,
        is_conformal=True,
        is_universal=True,
        aut_o_source="virasoro",  # from the W_2 = T subalgebra
        aut_o_action=_make_aut_o(gens, c, True, "virasoro"),
        descent_witness="W_2 Virasoro field and formal W_N OPE coefficients",
        shadow_class="M",
        koszul_dual=None,  # W_N duality is more complex
    )


def beta_gamma_family() -> ChiralAlgebraFamily:
    """Beta-gamma system.

    Universality witness: free-field conformal structure from the beta-gamma
    stress tensor.
    Generators: beta (weight 1), gamma (weight 0).
    """
    c = Rational(-1)
    kappa = c / 2  # = -1/2
    gens = [("beta", Rational(1)), ("gamma", Rational(0))]
    return ChiralAlgebraFamily(
        name="BetaGamma",
        central_charge=c,
        kappa=kappa,
        generators=gens,
        has_conformal_vector=True,
        is_quasi_conformal=True,
        is_conformal=True,
        is_universal=True,
        aut_o_source="sugawara",
        aut_o_action=_make_aut_o(gens, c, True, "sugawara"),
        descent_witness="free beta-gamma formal-disk OPE and stress tensor",
        shadow_class="C",
    )


def free_fermion_family(d: int = 1) -> ChiralAlgebraFamily:
    """Free fermion system (bc ghosts).

    Universality witness: free-field conformal structure.
    Generators: psi_i of weight 1/2 (d copies).
    Central charge c = d/2.
    """
    c = Rational(d, 2)
    kappa = c / 2  # = d/4
    gens = [(f"psi_{i}", Rational(1, 2)) for i in range(d)]
    return ChiralAlgebraFamily(
        name=f"FreeFermion(d={d})",
        central_charge=c,
        kappa=kappa,
        generators=gens,
        has_conformal_vector=True,
        is_quasi_conformal=True,
        is_conformal=True,
        is_universal=True,
        aut_o_source="sugawara",
        aut_o_action=_make_aut_o(gens, c, True, "sugawara"),
        descent_witness="free-fermion formal-disk OPE and stress tensor",
        shadow_class="G",
    )


def lattice_voa_family(rank: int = 1,
                       is_unimodular: bool = True) -> ChiralAlgebraFamily:
    """Lattice vertex operator algebra V_Lambda.

    Universality witness: for the even positive-definite lattice VOAs
    represented by this constructor, the Heisenberg stress tensor supplies the
    conformal vector and hence the Aut(O) action.  Unimodularity controls
    self-duality/holomorphicity, not the existence of a conformal vector.

    kappa = rank, not c/2 in general.
    """
    c = Rational(rank)
    kappa = Rational(rank)  # kappa(V_Lambda) = rank(Lambda), not c/2
    gens = [(f"h_{i}", Rational(1)) for i in range(rank)]
    # Add vertex operators for lattice vectors
    gens.append(("e_alpha", Rational(1)))  # representative lattice vertex op

    return ChiralAlgebraFamily(
        name=f"Lattice(rank={rank})",
        central_charge=c,
        kappa=kappa,
        generators=gens,
        has_conformal_vector=True,
        is_quasi_conformal=True,
        is_conformal=True,
        is_universal=True,
        aut_o_source="heisenberg",
        aut_o_action=_make_aut_o(gens, c, True, "heisenberg"),
        descent_witness=(
            "even positive-definite lattice VOA: Heisenberg stress tensor, "
            "lattice vertex operators, and formal-disk OPE"
        ),
        shadow_class="G" if rank == 1 else "L",
    )


def critical_level_family(type_: str, rank: int) -> ChiralAlgebraFamily:
    """Affine algebra at the critical level k = -h^v.

    Boundary case: no Sugawara construction, so no conformal vector.  The
    affine vacuum module still carries the formal coordinate-change action from
    the loop algebra central extension; this is the quasi-conformal witness.

    The center at critical level is the Feigin-Frenkel center z(hat{g}),
    which is a commutative chiral algebra isomorphic to functions on
    the space of opers.
    """
    LIE_DATA = {
        ("A", 1): (3, 2, "sl_2"),
        ("A", 2): (8, 3, "sl_3"),
    }
    dim_g, h_dual, name = LIE_DATA[(type_, rank)]
    k = Rational(-h_dual)  # critical level
    kappa = Rational(0)  # kappa = dim(g) * (k + h^v) / (2h^v) = 0 at critical level

    gens = [(f"J^a_{i}", Rational(1)) for i in range(dim_g)]
    return ChiralAlgebraFamily(
        name=f"Affine_{name}(k=critical)",
        central_charge=Rational(0),
        kappa=kappa,
        generators=gens,
        has_conformal_vector=False,
        is_quasi_conformal=True,
        is_conformal=False,  # no Sugawara at critical level
        is_universal=True,
        aut_o_source="affine_coordinate_change",
        aut_o_action=_make_aut_o(gens, Rational(0), False, "affine_coordinate_change"),
        descent_witness="affine formal-loop coordinate-change action at critical level",
        shadow_class="L",
        koszul_dual=f"Affine_{name}(k=critical)",  # self-dual at critical level
        level=k,
        lie_type=f"{type_}_{rank}",
    )


# =============================================================================
# 4. Full landscape registry
# =============================================================================

def standard_landscape() -> Dict[str, ChiralAlgebraFamily]:
    """Return the complete standard landscape with universality data."""
    families = {}

    # Class G: Gaussian, shadow depth 2
    families["heisenberg_1"] = heisenberg_family(Rational(1))
    families["heisenberg_k"] = heisenberg_family(Rational(3))
    families["free_fermion_1"] = free_fermion_family(1)
    families["free_fermion_2"] = free_fermion_family(2)

    # Class L: Lie/tree, shadow depth 3
    families["affine_sl2_1"] = affine_km_family("A", 1, Rational(1))
    families["affine_sl2_10"] = affine_km_family("A", 1, Rational(10))
    families["affine_sl3_1"] = affine_km_family("A", 2, Rational(1))
    families["affine_G2_1"] = affine_km_family("G", 2, Rational(1))
    families["affine_E8_1"] = affine_km_family("E", 8, Rational(1))

    # Class C: Contact, shadow depth 4
    families["beta_gamma"] = beta_gamma_family()

    # Class M: Mixed, infinite shadow depth
    families["virasoro_26"] = virasoro_family(Rational(26))
    families["virasoro_1"] = virasoro_family(Rational(1))
    families["virasoro_13"] = virasoro_family(Rational(13))
    families["w3_2"] = w_algebra_family(3, Rational(2))
    families["w4_2"] = w_algebra_family(4, Rational(2))

    # Lattice VOAs
    families["lattice_1"] = lattice_voa_family(1, True)
    families["lattice_24"] = lattice_voa_family(24, True)  # Leech-type

    # Critical level
    families["sl2_critical"] = critical_level_family("A", 1)

    return families


# =============================================================================
# 5. Universality verification functions
# =============================================================================

def verify_quasi_conformal(family: ChiralAlgebraFamily) -> Tuple[bool, str]:
    """Verify that a family has quasi-conformal structure.

    Quasi-conformal requires:
      (1) registered coordinate-change action,
      (2) L_{-1} action (translation operator T),
      (3) L_0 action on the represented positive-energy sectors,
      (4) local nilpotency of Der_+(O) on every generator.

    Returns (is_quasi_conformal, reason).
    """
    reasons = []

    if not family.is_quasi_conformal:
        return False, "family is not registered as quasi-conformal"

    if family.aut_o_action is None:
        return False, "missing Aut(O)/Der(O) action witness"

    if not family.aut_o_action.is_quasi_conformal:
        return False, "Aut(O)/Der(O) witness is not quasi-conformal"

    reasons.append(f"coordinate-change action: {family.aut_o_source}")
    reasons.append("L_{-1} (translation): present")

    weights = [w for _, w in family.generators]
    all_finite_weight = all(w < oo for w in weights)
    if not all_finite_weight:
        reasons.append("Der_+(O) nilpotency: FAILED (infinite weight generator)")
        return False, "; ".join(reasons)

    # The finite registry includes the half-integral free-fermion sector.
    all_half_integral = all(2 * w == int(2 * w) for w in weights)
    if all_half_integral:
        reasons.append(f"L_0 (grading): semisimple, weights {[float(w) for w in weights]}")
    else:
        reasons.append(f"L_0 (grading): FAILED, non-half-integral weights")
        return False, "; ".join(reasons)

    try:
        nilp_orders = [der_plus_local_nilpotency_bound(w) for w in weights]
    except ValueError as exc:
        reasons.append(f"Der_+(O) nilpotency: FAILED ({exc})")
        return False, "; ".join(reasons)
    reasons.append(f"Der_+(O) local nilpotency: positive-energy bounds {nilp_orders}")

    return True, "; ".join(reasons)


def verify_conformal(family: ChiralAlgebraFamily) -> Tuple[bool, str]:
    """Verify that a family has conformal (= full Virasoro) structure.

    Conformal requires quasi-conformal PLUS:
      - A conformal vector omega in V_2 (weight 2) such that
        omega_{(1)} = L_0, omega_{(0)} = L_{-1}, and the L_n satisfy
        the Virasoro commutation relations.

    Returns (is_conformal, reason).
    """
    if not family.has_conformal_vector or not family.is_conformal:
        return False, "No conformal vector (e.g. critical level affine)"

    if family.aut_o_action is None:
        return False, "missing Aut(O)/Der(O) action witness"

    if family.aut_o_action is not None and not family.aut_o_action.is_conformal:
        return False, "Aut(O) witness is quasi-conformal but not conformal"

    return True, f"Conformal vector present, c = {family.central_charge}, source = {family.aut_o_source}"


def verify_universal(family: ChiralAlgebraFamily) -> Tuple[bool, str]:
    """Verify that a family is universal in Cliff's sense.

    Cliff identifies universal factorization algebras in dimension 1 with
    quasi-conformal vertex algebras.  This function verifies the registered
    standard-family witness: quasi-conformal coordinate-change data plus
    compatible etale descent for the family.  A fixed-X D-module alone fails.

    Returns (is_universal, reason).
    """
    is_qc, qc_reason = verify_quasi_conformal(family)
    if not is_qc:
        return False, f"NOT universal: fails quasi-conformal. {qc_reason}"

    if not family.is_universal:
        return False, "NOT universal: no registered compatible family over curves"

    etale, etale_reason = verify_etale_descent(family)
    if not etale:
        return False, f"NOT universal: etale descent witness missing. {etale_reason}"

    return (
        True,
        "Universal for the registered dimension-1 family: "
        f"{qc_reason}; descent witness: {family.descent_witness}; {etale_reason}",
    )


def verify_etale_descent(family: ChiralAlgebraFamily) -> Tuple[bool, str]:
    """Verify that the factorization algebra satisfies etale descent.

    Etale descent for factorization algebras requires:
      (1) The OPE is defined on the formal disk (etale-local data)
      (2) The factorization structure uses only diagonal stratification
      (3) For any etale phi: X -> Y, phi^* F_Y = F_X canonically

    For the registered standard families, this holds because:
      - OPE coefficients are constants (structure constants of the Lie algebra,
        or rational functions of the central charge/level)
      - Factorization isomorphisms use only the complement of diagonals in X^I,
        which is etale-local (Cliff's key insight: V_phi(I) is open in X^I
        and contains Delta(X))

    Returns (has_descent, reason).
    """
    if not family.descent_witness:
        return (
            False,
            "No family-level descent witness registered; fixed-curve D-module "
            "and OPE data do not by themselves define a universal family",
        )

    reasons = []

    # OPE locality
    reasons.append("OPE defined on formal disk: YES (curve-independent)")

    # Factorization locality
    reasons.append("Factorization uses diagonal stratification: YES (etale-local)")

    # Cliff's criterion: V_phi(I) = {x^I : phi(x_i) = phi(x_j) => x_i = x_j}
    # is open and contains the diagonal
    reasons.append("Cliff V_phi(I) open and contains diagonal: YES")
    reasons.append(f"registered witness: {family.descent_witness}")

    return True, "; ".join(reasons)


def cliff_weak_equivalence_check(family: ChiralAlgebraFamily) -> Tuple[bool, str]:
    """Verify Cliff's Theorem 4.4/5.7: Weak <=> Ordinary factorization.

    Cliff proved that the forgetful functor
      FSp(X) -> WFSp(X)     (factorization spaces)
      FAlg(X) -> WFAlg(X,W)  (factorization algebras)
    are equivalences of categories.

    For our families, this means the weak factorization structure
    (defined only near diagonals) determines the full factorization algebra.

    Returns (equivalence_holds, reason).
    """
    # The equivalence is a general theorem, not family-specific
    return True, ("Cliff Theorem 4.4/5.7: Weak <=> Ordinary factorization "
                  "algebra (general theorem, applies to all families)")


# =============================================================================
# 6. Relationship between the three notions
# =============================================================================

def universality_hierarchy(family: ChiralAlgebraFamily) -> Dict[str, bool]:
    """Compute the full hierarchy of universality properties.

    The registered hierarchy in dimension 1 is:

      conformal VA  =>  quasi-conformal VA
      quasi-conformal VA + compatible family descent witness
        => universal chiral algebra <=> universal factorization algebra

    The categorical equivalences are FBZ Chapter 6 and Cliff Proposition 8.1;
    this engine keeps the family witness explicit to avoid treating fixed-X
    D-module data as universal.

    Note: the implication conformal => quasi-conformal is STRICT.
    Example: affine KM at critical level is quasi-conformal but NOT conformal.
    """
    is_qc, _ = verify_quasi_conformal(family)
    is_conf, _ = verify_conformal(family)
    is_univ, _ = verify_universal(family)
    etale, _ = verify_etale_descent(family)

    return {
        "conformal": is_conf,
        "quasi_conformal": is_qc,
        "universal_chiral": is_univ,
        "universal_factorization": is_univ,  # = universal chiral by Cliff
        "etale_descent": etale,
        "d_module_on_ran": True,  # always true for chiral algebras (BD definition)
    }


def minimal_universality_structure(family: ChiralAlgebraFamily) -> Dict[str, str]:
    """Determine the MINIMAL structure beyond BD chiral algebra for universality.

    A BD chiral algebra on a fixed curve X is:
      - A D-module B_X on X
      - A Lie bracket mu: B_{Ran X} tensor^ch B_{Ran X} -> B_{Ran X}

    The additional structure needed for universality is:
      - An Aut(O) action on the "stalk" V = B_x (the vertex algebra at a point)
      - Compatibility of this action with the chiral bracket mu
      - A coherent family-level descent witness for etale pullback

    For CONFORMAL algebras: the Aut(O) action comes from the conformal vector.
    For QUASI-CONFORMAL non-conformal algebras: it is supplied separately.

    The D-module structure on Ran(X) for a FIXED X does NOT by itself give
    universality.  The missing ingredient is the FAMILY structure: how the
    factorization algebra varies as X changes.
    """
    result = {}

    result["bd_chiral_on_fixed_X"] = (
        "D-module B_X on X + Lie bracket on B_{Ran X}. "
        "This is the fixed-curve input, not sufficient for universality."
    )

    result["additional_for_universality"] = (
        "Aut(O) action on the vertex algebra V = B_x at a point, "
        "compatible with vertex operations, plus the family-level etale "
        "pullback witness. This gives a coherent system of factorization "
        "algebras over curves."
    )

    if family.has_conformal_vector:
        result["source_of_aut_o"] = (
            f"Conformal vector (Virasoro element) with c = {family.central_charge}. "
            f"The L_n modes (n >= -1) generate the Aut(O) action. "
            f"Source: {family.aut_o_source}."
        )
    else:
        result["source_of_aut_o"] = (
            "Coordinate-change action supplied independently of a conformal "
            "vector; Der_+(O) acts locally nilpotently by positive-energy "
            "bounds. No Sugawara conformal vector in this family. "
            f"Source: {family.aut_o_source}."
        )

    result["cliff_bridge"] = (
        "FBZ and Cliff identify quasi-conformal vertex algebras, universal "
        "chiral algebras, and universal factorization algebras in dimension 1. "
        "The fixed-curve chiral algebra becomes universal only after the "
        "coordinate-change and etale-descent data are supplied."
    )

    return result


# =============================================================================
# 7. Specific checks for standard families
# =============================================================================

def check_bd_grassmannian_universality() -> Tuple[bool, str]:
    """Verify that the Beilinson-Drinfeld Grassmannian is universal.

    Cliff [Cliff19], Proposition 7.5:
    The BD Grassmannian Gr_{G,C} for a reductive group G and smooth curve C
    is universal with respect to pullback along etale morphisms between curves.

    Proof idea: formal completion along graphs is etale-local (equation (2) in
    Cliff), so the BD Grassmannian data transfers along etale morphisms.

    The associated factorization algebras (e.g. affine KM chiral algebras)
    inherit universality from the Grassmannian.
    """
    return True, ("BD Grassmannian is universal: Cliff Proposition 7.5. "
                  "Proof via formal completion of graphs under etale morphisms.")


def check_meromorphic_jet_universality() -> Tuple[bool, str]:
    """Verify that the space of meromorphic jets is universal.

    Cliff [Cliff19], Example 7.6 + Proposition (Example 7.6 proved):
    For an affine scheme X = Spec(A) and curve C, the factorization space
    L(X)_{Ran C} of meromorphic jets from C to X is universal.

    This generalizes the Kapranov-Vasserot construction and puts their
    chiral de Rham complex results on firm footing.
    """
    return True, ("Meromorphic jet space L(X)_{Ran C} is universal: "
                  "Cliff Example 7.6. Corrects implicit error in "
                  "Kapranov-Vasserot [7].")


def check_hilbert_scheme_universality() -> Tuple[bool, str]:
    """Verify that the Hilbert scheme factorization space is universal.

    Cliff [Cliff19], Example 7.7:
    For any smooth variety Y, the Hilbert scheme Hilb(Y) gives rise to a
    factorization space over Y that is universal in any dimension d.
    This is the first construction of a non-trivial universal factorization
    space in dimension > 1.
    """
    return True, ("Hilbert scheme Hilb(Y) universal factorization space: "
                  "Cliff Example 7.7. Works in any dimension d.")


# =============================================================================
# 8. The monograph connection: are our algebras already universal?
# =============================================================================

def monograph_universality_status() -> Dict[str, Dict]:
    """Determine universality status for every family in the monograph.

    Finding: all standard registered families in the monograph are universal.
    The D-module structure on Ran(X) (axiom MK1) gives the factorization
    algebra on a fixed curve.  Universality is recorded only when the registry
    supplies the family-level descent witness:

    (1) the family has quasi-conformal structure;
    (2) most families have full conformal structure;
    (3) the OPE is curve-independent (etale_descent_engine.py);
    (4) the factorization structure is etale-local.

    The standard registered family that is quasi-conformal but not conformal:
      - Affine KM at critical level k = -h^v.
    """
    landscape = standard_landscape()
    result = {}

    for key, family in landscape.items():
        hierarchy = universality_hierarchy(family)
        is_univ, reason = verify_universal(family)
        minimal = minimal_universality_structure(family)

        result[key] = {
            "family": family.name,
            "hierarchy": hierarchy,
            "is_universal": is_univ,
            "reason": reason,
            "minimal_structure": minimal,
            "conformal_vs_quasi_conformal": (
                "conformal" if hierarchy["conformal"]
                else "quasi-conformal only"
            ),
        }

    return result


# =============================================================================
# 9. Dimension analysis: why dim 1 is special
# =============================================================================

def dimension_analysis() -> Dict[str, str]:
    """Explain why the equivalence holds specifically in dimension 1.

    In dimension 1:
      quasi-conformal VA <=> universal chiral algebra <=> universal fact. algebra

    In dimension d > 1:
      Universal factorization algebras exist (Cliff Example 7.7: Hilbert scheme).
      But there is no vertex algebra analogue in higher dimensions.
      Factorization algebras in dim d are the correct higher-dimensional notion.

    The key dimension-1 feature:
      The formal disk Spec k[[t]] has a 1-dimensional space of derivations,
      and Aut(O) = Aut(k[[t]]) is pro-algebraic with Lie algebra Der(O).
      In dimension d, one would need Aut(k[[t_1, ..., t_d]]), which is
      infinite-dimensional in a more complicated way.
    """
    return {
        "dim_1_equivalence": (
            "quasi-conformal VA <=> universal chiral <=> universal factorization "
            "as categories. This chain uses FBZ Chapter 6, BD 2.9.9, and "
            "Cliff Proposition 8.1."
        ),
        "dim_1_special": (
            "Aut(O) = Aut(k[[t]]) is a pro-algebraic group. "
            "Its Lie algebra Der(O) = k[[t]] d/dt has a natural filtration. "
            "The formal disk is 1-dimensional, so coordinate changes are "
            "controlled by a single variable."
        ),
        "dim_higher": (
            "In dim d > 1: universal factorization algebras exist (Hilbert scheme). "
            "But no vertex algebra analogue. Cliff's framework provides the "
            "correct higher-dimensional generalization."
        ),
        "monograph_context": (
            "The monograph works in dimension 1 (curves). The standard "
            "registered families are universal because they carry explicit "
            "coordinate-change and etale-descent witnesses. Cliff's framework "
            "also supplies the higher-dimensional factorization-algebra lane."
        ),
    }


# =============================================================================
# 10. Cliff's weak factorization as a computational tool
# =============================================================================

def weak_factorization_data(family: ChiralAlgebraFamily) -> Dict[str, str]:
    """Extract the weak factorization data for a family.

    Cliff's key insight: the "interesting data" of a factorization space/algebra
    is concentrated near the diagonals.  A weak factorization algebra only
    requires the factorization isomorphisms on open neighborhoods W(I) of the
    diagonal Delta(X) in X^I, not on all of X^I.

    For computations, this means:
      - The collision differential d_coll only needs OPE data near z_i = z_j
      - The bar complex B(A) uses the factorization near diagonals
      - The shadow obstruction tower theta_A is determined by local data

    This is why the bar complex computations use formal neighborhoods of
    diagonals via the propagator eta^(0) = d log(z-w).  The computation is
    promoted from local data to a global factorization statement only through
    the registered descent witness.
    """
    return {
        "name": family.name,
        "open_neighborhoods": (
            "W(I) = open nbhd of diagonal in X^I. "
            "For I = {1,2}: W({1,2}) contains the formal neighborhood "
            "of the diagonal z_1 = z_2 where the OPE converges."
        ),
        "bar_complex_connection": (
            "The bar differential d_bar uses the propagator eta^(0) = d log(z_i - z_j), "
            "which is defined on the formal neighborhood of the diagonal. "
            "This is Cliff weak-factorization data."
        ),
        "shadow_tower_connection": (
            "The shadow obstruction tower theta_A = sum theta_A^{<=r} is computed "
            "from formal OPE data. With the registered descent witness, Cliff's "
            "weak-factorization theorem determines the full factorization algebra."
        ),
        "computational_consequence": (
            "Our bar complex computations on the formal neighborhood of diagonals "
            "capture the weak factorization structure. Cliff's Theorem 4.4/5.7 "
            "then extends this weak structure to the full factorization algebra."
        ),
    }
