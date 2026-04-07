r"""C2-cofiniteness / chiral Koszulness bridge engine.

Investigates the precise relationship between Zhu's C_2-cofiniteness
condition and chiral Koszulness (def:chiral-koszul-morphism).

MATHEMATICAL FRAMEWORK
======================

C_2-COFINITENESS (Zhu 1996, Li 1999):
  For a vertex algebra V, define C_2(V) = span{a_{(-2)}b : a,b in V}.
  V is C_2-cofinite if dim(V / C_2(V)) < infinity.
  Equivalently, the associated variety X_V = Specm(R_V) has dim X_V = 0,
  where R_V = gr^F V = V / C_2(V) is the Zhu C_2 algebra (= Li associated
  graded at the leading level).

  The associated variety X_V = Specm(R_V / sqrt(0)) = Specm(R_V^red).
  C_2-cofiniteness is equivalent to X_V = {0} (the associated variety
  is a single point).

  Li's theorem (Li 1999): C_2(V) = F_1 V in the Li filtration, so
  V/C_2(V) = gr_0^F V = R_V at filtration level 0. But the FULL
  Li associated graded R_V = gr^F V is a commutative vertex algebra
  (with Poisson bracket from the 0-product).

KEY THEOREMS ON C_2-COFINITENESS:
  - Zhu (1996): C_2-cofinite + CFT-type => characters are modular functions
    for some congruence subgroup.
  - Huang (2008): C_2-cofinite + rational => genus-g conformal blocks form
    a vector bundle with flat connection for all g.
  - Miyamoto (2004): C_2-cofinite => module category has finitely many
    irreducibles.
  - Arakawa (2012, 2015): Associated variety of W-algebras =
    Slodowy slice intersected with nilpotent cone. C_2-cofiniteness of
    L_k(g) at admissible level iff X_{L_k} = {0}.

CHIRAL KOSZULNESS (this monograph):
  V is chirally Koszul if bar cohomology H*(B(V)) is concentrated in
  bar degree 1 (def:chiral-koszul-morphism). Equivalently, any of the
  10 unconditional equivalences of thm:koszul-equivalences-meta:
  PBW E_2 collapse, A_infinity formality, Ext diagonal vanishing,
  bar-cobar inversion, factorization homology concentration, etc.

THE BRIDGE:
  (1) Koszulness => C_2-cofiniteness? NO in general.
      Counterexample: V_k(g) (universal affine) is Koszul at ALL k
      (cor:universal-koszul) but is NOT C_2-cofinite for generic k
      (the associated variety X_{V_k} = g* is the full dual Lie algebra,
      not {0}).
      The universal Virasoro Vir_c is Koszul but NOT C_2-cofinite
      (X_{Vir_c} = C, one-dimensional).

  (2) C_2-cofiniteness => Koszulness? NO in general, and the obstruction
      is well understood.
      The C_2-cofinite simple quotients L_k(g) at admissible levels have
      X_{L_k} = {0} (Arakawa), but Koszulness requires bar concentration,
      which is obstructed by null vectors in the bar-relevant range
      (thm:kac-shapovalov-koszulness). Minimal models are C_2-cofinite
      but NOT Koszul (null vectors break PBW).

  (3) The intersection: algebras that are BOTH C_2-cofinite AND Koszul.
      Known examples:
      - L_k(sl_2) at all admissible levels (rem:admissible-koszul-status:
        Koszulness proved for sl_2, C_2-cofiniteness by Arakawa).
      - Lattice VOAs (C_2-cofinite + Koszul by lattice filtration).
      - (Conjecturally) L_k(g) at non-degenerate admissible levels for
        all simple g, but Koszulness OPEN for rank >= 2.

  (4) The gap: what C_2-cofiniteness gives for the bar complex.
      C_2-cofiniteness (X_V = {0}) implies the Li--bar spectral sequence
      has a finite-dimensional E_0 page at filtration level 0 (since
      R_V is a finite-dimensional Poisson algebra). This is a FINITENESS
      condition on the bar complex, weaker than diagonal concentration.
      Specifically:
      - dim(V/C_2(V)) < infinity => dim(R_V) < infinity (at each weight)
      - The Li--bar E_1 page is the bar complex of a finite-dim algebra
      - But this does NOT force E_2 collapse (diagonal concentration)

  (5) The role of the associated variety in the Li--bar SS:
      thm:associated-variety-koszulness shows:
      - X_V = {0} (C_2-cofinite) => R_V is finite-dim Poisson algebra
      - The Li--bar d_1 is determined by the Poisson bracket on R_V
      - C_2-cofinite + diagonal concentration of Li--bar E_2 => Koszul
      So C_2-cofiniteness is a NECESSARY INPUT for the associated-variety
      criterion (condition (ii)), but not sufficient.

  (6) For the monograph's validity at all genera:
      C_2-cofiniteness guarantees well-behaved conformal blocks at all genera
      (Huang). Chiral Koszulness guarantees the bar-cobar inversion and the
      shadow obstruction tower has controlled finite-order truncations.
      The genus-g factorization homology int_{Sigma_g} A being concentrated
      in degree 0 is one of the 10 Koszul equivalences (item (vii) of
      thm:koszul-equivalences-meta).
      So: C_2-cofinite + Koszul => full genus-g validity of both the
      Zhu/Huang conformal block theory AND the bar-cobar shadow tower.

CRITICAL DISTINCTIONS:
  - C_2-cofiniteness is about the SIZE of V/C_2(V) (finiteness).
  - Koszulness is about the SHAPE of H*(B(V)) (concentration).
  - C_2 quotient V/C_2(V) = R_V|_{level 0} is the degree-0 piece.
  - Bar cohomology H*(B(V)) involves ALL degrees and higher products.
  - C_2-cofiniteness is a property of the MODULE CATEGORY (finiteness
    of irreducibles, modular invariance of characters).
  - Koszulness is a property of the FACTORIZATION ALGEBRA structure
    (bar-cobar inversion, Ext diagonal vanishing).
  These are DIFFERENT properties of DIFFERENT aspects of V.

ANTI-PATTERN GUARDS:
  AP7:  Universal V_k(g) is Koszul but NOT C_2-cofinite. Never write
        "Koszul implies C_2-cofinite."
  AP14: Koszulness (bar concentration) is different from Swiss-cheese
        formality (shadow depth). C_2-cofiniteness is a THIRD condition,
        independent of both.
  AP39: kappa = c/2 only for Virasoro. For KM: kappa = dim(g)*(k+h^v)/(2h^v).
  AP48: kappa depends on the full algebra, not the Virasoro subalgebra.

References:
  Zhu (1996): Modular invariance of characters of vertex operator algebras.
  Li (1999): Determining fusion rules by A(V)-modules and bimodules.
  Huang (2008): Vertex operator algebras and the Verlinde conjecture.
  Miyamoto (2004): Modular invariance of vertex operator algebras satisfying
    C_2-cofiniteness.
  Arakawa (2012): A remark on the C_2-cofiniteness condition on vertex algebras.
  Arakawa (2015): Associated varieties of modules over Kac-Moody algebras
    and C_2-cofiniteness of W-algebras.
  Arakawa (2017): Rationality of admissible affine vertex algebras in the
    category O.
  Van Ekeren-Heluani (2019): Chiral homology of elliptic curves and Zhu's
    algebra (shows chiral homology encodes C_2 data).
  Manuscript: thm:associated-variety-koszulness, rem:rationality-not-koszul-criterion,
    constr:li-bar-spectral-sequence, thm:koszul-equivalences-meta.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from fractions import Fraction
from math import gcd
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, Symbol, oo, simplify, binomial


# ============================================================================
# C_2-cofiniteness status
# ============================================================================

class C2Status(Enum):
    """C_2-cofiniteness status."""
    C2_COFINITE = "C2_cofinite"
    NOT_C2_COFINITE = "not_C2_cofinite"
    OPEN = "open"


class AssociatedVarietyType(Enum):
    """Type of the associated variety X_V = Specm(R_V^red)."""
    POINT = "point"           # X_V = {0}, C_2-cofinite
    NILPOTENT_ORBIT = "nilpotent_orbit_closure"  # X_V = closure(O)
    FULL_DUAL = "full_dual"   # X_V = g* (full dual Lie algebra)
    AFFINE_LINE = "affine_line"  # X_V = C (Virasoro universal)
    OTHER = "other"


class KoszulStatus(Enum):
    """Chiral Koszulness status."""
    KOSZUL = "koszul"
    NOT_KOSZUL = "not_koszul"
    OPEN = "open"


class BridgeRelation(Enum):
    """Classification of the (C2, Koszul) pair."""
    BOTH = "both_C2_and_Koszul"
    C2_ONLY = "C2_cofinite_but_not_Koszul"
    KOSZUL_ONLY = "Koszul_but_not_C2_cofinite"
    NEITHER = "neither"
    OPEN_KOSZUL = "C2_cofinite_Koszul_open"
    OPEN_C2 = "Koszul_C2_open"


# ============================================================================
# Algebra bridge data
# ============================================================================

@dataclass
class C2KoszulBridgeData:
    """Complete C2/Koszul comparison for a vertex algebra.

    Fields:
        name: human-readable name
        algebra_type: 'universal', 'simple_quotient', 'lattice', 'free_field'
        c2_status: C_2-cofiniteness status
        koszul_status: chiral Koszulness status
        bridge_relation: the combined classification
        associated_variety: type of X_V
        associated_variety_dim: dim X_V (0 for C_2-cofinite)
        c2_quotient_dim: dim(V/C_2(V)) if finite, else None
        generators: list of generator names
        generator_weights: conformal weights
        central_charge: c
        kappa: modular characteristic
        li_bar_e1_finiteness: whether the Li--bar E_1 page is finite-dim
        li_bar_e2_diagonal: whether E_2 is diagonally concentrated
        null_vectors_in_bar_range: whether there are nulls in bar range
        has_modular_characters: whether characters have modular invariance
        genus_g_conformal_blocks: whether genus-g blocks are well-defined
        notes: mathematical justification
    """
    name: str
    algebra_type: str
    c2_status: C2Status
    koszul_status: KoszulStatus
    bridge_relation: BridgeRelation
    associated_variety: AssociatedVarietyType
    associated_variety_dim: int
    c2_quotient_dim: Optional[int]
    generators: List[str]
    generator_weights: List[Any]
    central_charge: Any
    kappa: Any
    li_bar_e1_finiteness: bool
    li_bar_e2_diagonal: bool
    null_vectors_in_bar_range: bool
    has_modular_characters: bool
    genus_g_conformal_blocks: bool
    notes: str

    @property
    def is_c2_cofinite(self) -> bool:
        return self.c2_status == C2Status.C2_COFINITE

    @property
    def is_koszul(self) -> bool:
        return self.koszul_status == KoszulStatus.KOSZUL


# ============================================================================
# C_2 quotient dimension computations
# ============================================================================

def c2_quotient_dim_heisenberg(weight_bound: int) -> int:
    """Dimension of V/C_2(V) for Heisenberg H_k, truncated at weight bound.

    For H_k: V = C[a_{-1}, a_{-2}, ...] with |a_{-n}| = n.
    C_2(V) = span{a_{(-2)}b} = span{a_{-2}b, a_{-3}b, ...}.
    The C_2 quotient V/C_2(V) is spanned by normally ordered monomials
    in a_{-1} only (since a_{-n} for n >= 2 can be written as
    a_{(-n-1)}|0> and a_{(-n-1)} = (1/(n-1)!) d^{n-1} a_{(-2)},
    which lies in C_2 for n >= 2).

    So V/C_2(V) = C[a_{-1}] = polynomial ring in one variable.
    This is INFINITE-dimensional. H_k is NOT C_2-cofinite.

    At weight h, the C_2 quotient has dimension = number of partitions
    of h into parts all equal to 1, which is 1 if h <= weight_bound, 0 else.
    But for the FULL quotient (all weights), it is infinite.
    """
    # V/C_2(V) = C[a_{-1}] has one basis element at each weight h >= 0
    # Truncated to weight <= weight_bound:
    return weight_bound + 1  # dimensions 0, 1, ..., weight_bound


def c2_quotient_dim_virasoro(weight_bound: int) -> int:
    """Dimension of V/C_2(V) for universal Virasoro Vir_c, up to weight bound.

    For Vir_c: V = C[L_{-1}, L_{-2}, ...] with |L_{-n}| = n.
    C_2(V) = span{a_{(-2)}b} contains all L_{-n}|0> for n >= 3
    (since L_{-n}|0> = L_{(-n-1)}|0> and (-n-1) <= -2 for n >= 2,
    but more precisely T_{(-2)}v = L_{-3}v + ...).

    The C_2 quotient V/C_2(V) is the polynomial ring C[L_{-2}] since
    L_{-n} for n >= 3 lies in C_2(V) via L_{(-2)}|0> = L_{-3}|0>.
    So V/C_2(V) = C[L_{-2}] = polynomial ring in one variable (L_{-2}
    has weight 2).

    This is INFINITE-dimensional. The universal Virasoro is NOT C_2-cofinite.
    (Associated variety = Spec C[L_{-2}] = affine line.)
    """
    # V/C_2(V) = C[L_{-2}], one basis element at each even weight 0, 2, 4, ...
    return weight_bound // 2 + 1


def c2_quotient_dim_affine_universal(N: int, weight_bound: int) -> int:
    """Dimension of V/C_2(V) for V_k(sl_N) at generic k, up to weight bound.

    For V_k(sl_N): V = Sym(sl_N tensor t^{-1}C[t^{-1}]) as graded vector space.
    C_2(V) = span{a_{(-2)}b} contains J^a_{-n}|0> for n >= 2.
    So V/C_2(V) = Sym(sl_N) = C[J^1_{-1}, ..., J^{dim(g)}_{-1}].
    This is the polynomial ring in dim(g) = N^2-1 variables at weight 1.

    V/C_2(V) = Sym(g) = O(g*) = coordinate ring of g*.
    This is INFINITE-dimensional. X_V = g* = full dual Lie algebra.
    NOT C_2-cofinite.
    """
    dim_g = N * N - 1
    # Number of monomials of total degree <= weight_bound in dim_g variables
    # = C(weight_bound + dim_g, dim_g)
    total = 0
    for d in range(weight_bound + 1):
        total += int(binomial(d + dim_g - 1, dim_g - 1))
    return total


def c2_quotient_dim_minimal_model(p: int, q: int) -> int:
    """Dimension of V/C_2(V) for minimal model L(c_{p,q}, 0).

    For a C_2-cofinite VOA, V/C_2(V) is finite-dimensional.
    For the Virasoro minimal model L(c_{p,q}, 0):
    V/C_2(V) = C[L_{-2}] / (singular vector relation)

    The Zhu C_2 algebra R_V = C[x] / (f(x)) where f is a polynomial
    of degree related to the null vector structure.

    For the (p,q) minimal model, the associated variety X_V = {0}
    (Arakawa/Zhu). The C_2 quotient dimension is:

    dim(V/C_2(V)) = (p-1)(q-1)/2  (number of primary fields)

    This is the dimension of Zhu's algebra A(V) for the minimal model,
    which equals the number of irreducible modules.
    """
    if p < 2 or q < 2 or gcd(p, q) != 1 or p >= q:
        raise ValueError(f"Invalid minimal model parameters: p={p}, q={q}")
    return (p - 1) * (q - 1) // 2


def c2_quotient_dim_admissible_sl2(p: int, q: int) -> int:
    """Dimension of Zhu's algebra A(L_k(sl_2)) at admissible level k = p/q - 2.

    For L_k(sl_2) at admissible level, the associated variety is {0}
    (Arakawa 2017: admissible affine VOAs are rational and C_2-cofinite).

    The number of irreducible modules is p*q (from Kac-Wakimoto theory).
    The Zhu algebra A(V) = End(bigoplus V_i) has dimension sum d_i^2
    where d_i are the dimensions of the irrep blocks.

    For sl_2 admissible: the irreducible modules are parametrized by
    (r,s) with 1 <= r <= p-1, 1 <= s <= q, and highest weight
    h_{r,s} = [(rq - sp)^2 - (p-q)^2] / (4pq).
    Number of such modules: (p-1)*q.

    The dimension of V/C_2(V) is harder to compute in general, but
    for C_2-cofinite VOAs it equals dim Zhu(V) = number of irreducibles
    (for semisimple Zhu algebra).
    """
    if p < 2 or q < 1 or gcd(p, q) != 1:
        raise ValueError(f"Invalid admissible parameters: p={p}, q={q}")
    return (p - 1) * q


def c2_quotient_dim_lattice(rank: int) -> str:
    """C_2 quotient description for lattice VOA V_Lambda.

    For a positive-definite even lattice Lambda of rank r:
    V_Lambda is C_2-cofinite (lattice VOAs are rational).
    V/C_2(V) = Sym(h) tensor C[Lambda] / (relations from C_2).

    The associated variety X_{V_Lambda} = {0} (since the lattice VOA
    is rational).

    dim(V/C_2(V)) = |Lambda / 2*Lambda| = 2^r * det(Lambda)^{1/2} ... (complex)
    For simplicity we return a description.
    """
    return f"finite (rank-{rank} lattice VOA is C_2-cofinite)"


# ============================================================================
# Associated variety computations
# ============================================================================

def associated_variety_universal_affine(N: int) -> Tuple[AssociatedVarietyType, int, str]:
    """Associated variety of V_k(sl_N) at generic k.

    X_{V_k(g)} = g* (full dual Lie algebra).
    dim X_V = dim g = N^2 - 1.
    NOT C_2-cofinite.
    """
    dim_g = N * N - 1
    return (AssociatedVarietyType.FULL_DUAL, dim_g,
            f"g* = sl_{N}*, dim = {dim_g}")


def associated_variety_simple_admissible(g_type: str, k_num: int, k_den: int,
                                          nilpotent_orbit: str = "zero") -> Tuple[AssociatedVarietyType, int, str]:
    """Associated variety of L_k(g) at admissible level.

    By Arakawa (2015, 2017):
    - At non-degenerate admissible levels: X_{L_k} = {0}
    - At degenerate admissible levels: X_{L_k} = closure(O_f) for some
      nilpotent f determined by the level.

    For sl_2: all admissible levels are non-degenerate, so X = {0}.
    For sl_N, N >= 3: degenerate admissible levels can have X = closure(O)
    for various nilpotent orbits.
    """
    if nilpotent_orbit == "zero":
        return (AssociatedVarietyType.POINT, 0,
                f"X_{{L_k({g_type})}} = {{0}} (non-degenerate admissible)")
    else:
        return (AssociatedVarietyType.NILPOTENT_ORBIT, -1,
                f"X_{{L_k({g_type})}} = closure({nilpotent_orbit})")


def associated_variety_virasoro_universal() -> Tuple[AssociatedVarietyType, int, str]:
    """Associated variety of universal Virasoro.

    R_{Vir_c} = C[L_{-2}], so X_{Vir_c} = Spec C[x] = affine line.
    dim X = 1. NOT C_2-cofinite.
    """
    return (AssociatedVarietyType.AFFINE_LINE, 1,
            "X_{Vir_c} = Spec C[x] = affine line, dim = 1")


def associated_variety_minimal_model(p: int, q: int) -> Tuple[AssociatedVarietyType, int, str]:
    """Associated variety of minimal model L(c_{p,q}, 0).

    X_{L(c_{p,q})} = {0}. C_2-cofinite.
    """
    return (AssociatedVarietyType.POINT, 0,
            f"X_{{L(c_{{{p},{q}}})}} = {{0}}")


def associated_variety_w_algebra_principal(N: int) -> Tuple[AssociatedVarietyType, int, str]:
    """Associated variety of universal principal W-algebra W^k(sl_N).

    R_{W^k(sl_N)} = C[g_1, ..., g_{N-1}] where g_i are generators at
    weights 2, 3, ..., N. This is a polynomial ring in N-1 variables.
    X = C^{N-1}. NOT C_2-cofinite.
    """
    return (AssociatedVarietyType.OTHER, N - 1,
            f"X_{{W^k(sl_{N})}} = C^{{{N-1}}}, dim = {N-1}")


# ============================================================================
# Li--bar spectral sequence analysis
# ============================================================================

def li_bar_e1_finite_dim(c2_cofinite: bool) -> bool:
    """Whether the Li--bar E_1 page is finite-dimensional (at each weight).

    If V is C_2-cofinite, then R_V = gr^F V is finite-dimensional at
    each weight (the associated graded is a finitely generated commutative
    algebra with X_V = {0}).

    The Li--bar E_0 page = bar complex of R_V. If R_V is finite-dim
    at each weight, so is the E_0 page, and hence the E_1 page.

    This is a FINITENESS condition, weaker than diagonal concentration.
    """
    return c2_cofinite


def li_bar_d1_from_poisson(c2_cofinite: bool, poisson_trivial: bool) -> str:
    """Describes the d_1 differential on the Li--bar E_1 page.

    By prop:li-bar-poisson-differential:
    d_1 is determined by the Poisson bracket on R_V.

    If the Poisson bracket is trivial (e.g., R_V = polynomial algebra
    with no bracket), then d_1 = 0.

    For C_2-cofinite VOAs with X_V = {0}, R_V is a local Artinian
    Poisson algebra. The Poisson bracket may still be nontrivial
    (e.g., for admissible affine VOAs, the Poisson bracket on R_V
    is induced from the Lie bracket of g).
    """
    if not c2_cofinite:
        return "R_V infinite-dimensional; Li--bar SS may not converge usefully"
    if poisson_trivial:
        return "d_1 = 0 (trivial Poisson bracket); E_2 = E_1"
    return "d_1 nontrivial (Poisson bracket nonzero on R_V); E_2 requires computation"


# ============================================================================
# The bridge: all standard families
# ============================================================================

def heisenberg_bridge(k=None) -> C2KoszulBridgeData:
    """Heisenberg H_k: Koszul but NOT C_2-cofinite."""
    if k is None:
        k = Symbol('k')
    return C2KoszulBridgeData(
        name="Heisenberg H_k",
        algebra_type="free_field",
        c2_status=C2Status.NOT_C2_COFINITE,
        koszul_status=KoszulStatus.KOSZUL,
        bridge_relation=BridgeRelation.KOSZUL_ONLY,
        associated_variety=AssociatedVarietyType.FULL_DUAL,
        associated_variety_dim=1,  # X = Spec C[a_{-1}] = C
        c2_quotient_dim=None,  # infinite
        generators=["J"],
        generator_weights=[1],
        central_charge=1,
        kappa=k,
        li_bar_e1_finiteness=False,
        li_bar_e2_diagonal=True,  # Koszul => E_2 diagonal
        null_vectors_in_bar_range=False,
        has_modular_characters=False,  # not C_2-cofinite
        genus_g_conformal_blocks=False,  # not in the C_2 sense
        notes=(
            "Heisenberg H_k: freely strongly generated, Koszul by "
            "PBW universality. Associated variety X = C (affine line): "
            "V/C_2(V) = C[a_{-1}] is infinite-dimensional, so NOT "
            "C_2-cofinite. This is the simplest example showing "
            "Koszulness does NOT imply C_2-cofiniteness."
        ),
    )


def universal_affine_sl2_bridge(k=None) -> C2KoszulBridgeData:
    """V_k(sl_2): Koszul but NOT C_2-cofinite."""
    if k is None:
        k = Symbol('k')
    return C2KoszulBridgeData(
        name="V_k(sl_2) (universal)",
        algebra_type="universal",
        c2_status=C2Status.NOT_C2_COFINITE,
        koszul_status=KoszulStatus.KOSZUL,
        bridge_relation=BridgeRelation.KOSZUL_ONLY,
        associated_variety=AssociatedVarietyType.FULL_DUAL,
        associated_variety_dim=3,  # X = sl_2* = C^3
        c2_quotient_dim=None,  # infinite: Sym(sl_2) = C[e,h,f]
        generators=["e", "h", "f"],
        generator_weights=[1, 1, 1],
        central_charge=3 * k / (k + 2) if isinstance(k, Symbol) else Rational(3) * k / (k + 2),
        kappa=Rational(3, 4) * (k + 2) if not isinstance(k, Symbol) else Rational(3, 4) * (k + 2),
        li_bar_e1_finiteness=False,
        li_bar_e2_diagonal=True,  # Koszul => E_2 diagonal
        null_vectors_in_bar_range=False,
        has_modular_characters=False,
        genus_g_conformal_blocks=False,
        notes=(
            "Universal V_k(sl_2): Koszul at ALL k by PBW universality. "
            "X = sl_2* = C^3 (dim 3). V/C_2(V) = Sym(sl_2) = C[e,h,f], "
            "infinite-dimensional. NOT C_2-cofinite. Shows Koszulness "
            "does not imply C_2-cofiniteness even for 'nice' algebras."
        ),
    )


def virasoro_universal_bridge() -> C2KoszulBridgeData:
    """Universal Vir_c: Koszul but NOT C_2-cofinite."""
    c = Symbol('c')
    return C2KoszulBridgeData(
        name="Vir_c (universal)",
        algebra_type="universal",
        c2_status=C2Status.NOT_C2_COFINITE,
        koszul_status=KoszulStatus.KOSZUL,
        bridge_relation=BridgeRelation.KOSZUL_ONLY,
        associated_variety=AssociatedVarietyType.AFFINE_LINE,
        associated_variety_dim=1,
        c2_quotient_dim=None,  # infinite: C[L_{-2}]
        generators=["T"],
        generator_weights=[2],
        central_charge=c,
        kappa=c / 2,
        li_bar_e1_finiteness=False,
        li_bar_e2_diagonal=True,
        null_vectors_in_bar_range=False,
        has_modular_characters=False,
        genus_g_conformal_blocks=False,
        notes=(
            "Universal Virasoro: Koszul by PBW universality. "
            "X = Spec C[L_{-2}] = affine line (dim 1). "
            "V/C_2(V) = C[L_{-2}], infinite-dimensional. "
            "NOT C_2-cofinite."
        ),
    )


def minimal_model_bridge(p: int, q: int) -> C2KoszulBridgeData:
    """Virasoro minimal model L(c_{p,q}): C_2-cofinite but NOT Koszul."""
    if p < 2 or q < 2 or gcd(p, q) != 1 or p >= q:
        raise ValueError(f"Invalid minimal model: p={p}, q={q}")

    c_val = Rational(1) - 6 * Rational((p - q)**2, p * q)
    kappa_val = c_val / 2
    h_null = p * q - p - q + 1
    null_in_range = h_null >= 4  # bar-relevant range for weight-2 generator

    # Special case: (2,3) trivial model
    is_trivial = (p == 2 and q == 3)

    return C2KoszulBridgeData(
        name=f"L(c_{{{p},{q}}}) minimal model",
        algebra_type="simple_quotient",
        c2_status=C2Status.C2_COFINITE,
        koszul_status=KoszulStatus.NOT_KOSZUL if null_in_range else KoszulStatus.OPEN,
        bridge_relation=(BridgeRelation.C2_ONLY if null_in_range
                         else BridgeRelation.OPEN_KOSZUL),
        associated_variety=AssociatedVarietyType.POINT,
        associated_variety_dim=0,
        c2_quotient_dim=c2_quotient_dim_minimal_model(p, q),
        generators=["T"],
        generator_weights=[2],
        central_charge=c_val,
        kappa=kappa_val,
        li_bar_e1_finiteness=True,  # C_2-cofinite => finite E_1
        li_bar_e2_diagonal=False,  # NOT diagonal: null vectors
        null_vectors_in_bar_range=null_in_range,
        has_modular_characters=True,  # Zhu's theorem
        genus_g_conformal_blocks=True,  # Huang's theorem
        notes=(
            f"Minimal model c_{{{p},{q}}}: C_2-cofinite (X = {{0}}), "
            f"rational. dim(V/C_2(V)) = {c2_quotient_dim_minimal_model(p, q)}. "
            f"First null at h = {h_null}. "
            f"{'NOT' if null_in_range else 'Possibly'} Koszul: "
            f"null vectors in bar range block PBW. "
            f"Has modular characters (Zhu) and genus-g conformal blocks (Huang). "
            f"This is the canonical example: C_2-cofinite but NOT Koszul."
        ),
    )


def admissible_sl2_bridge(p: int, q: int) -> C2KoszulBridgeData:
    """L_k(sl_2) at admissible level k = p/q - 2: C_2-cofinite AND Koszul."""
    if p < 2 or q < 1 or gcd(p, q) != 1:
        raise ValueError(f"Invalid admissible: p={p}, q={q}")

    k = Fraction(p, q) - 2
    c_val = Rational(3) * Rational(p, q) / (Rational(p, q))  # 3k/(k+2) = 3(p/q-2)/(p/q)
    # Correct: c = 3k/(k+2) = 3*(p/q - 2) / (p/q) = 3*(p - 2q) / p
    c_val = Rational(3 * (p - 2 * q), p)
    kappa_val = Rational(3 * p, 4 * q)

    return C2KoszulBridgeData(
        name=f"L_{{k={p}/{q}-2}}(sl_2) admissible",
        algebra_type="simple_quotient",
        c2_status=C2Status.C2_COFINITE,  # Arakawa 2017
        koszul_status=KoszulStatus.KOSZUL,  # rem:admissible-koszul-status
        bridge_relation=BridgeRelation.BOTH,
        associated_variety=AssociatedVarietyType.POINT,
        associated_variety_dim=0,
        c2_quotient_dim=c2_quotient_dim_admissible_sl2(p, q),
        generators=["e", "h", "f"],
        generator_weights=[1, 1, 1],
        central_charge=c_val,
        kappa=kappa_val,
        li_bar_e1_finiteness=True,
        li_bar_e2_diagonal=True,  # Koszul proved for sl_2
        null_vectors_in_bar_range=True,  # nulls present but don't block
        has_modular_characters=True,
        genus_g_conformal_blocks=True,
        notes=(
            f"L_k(sl_2) at k = {p}/{q} - 2: BOTH C_2-cofinite (Arakawa 2017) "
            f"AND Koszul (rem:admissible-koszul-status). "
            f"X = {{0}} (non-degenerate admissible). "
            f"dim(V/C_2(V)) = {c2_quotient_dim_admissible_sl2(p, q)}. "
            f"The null vectors ARE in the bar range but the quotient bar "
            f"spectral sequence still degenerates at E_2 (structural argument "
            f"from single-weight null vector + Kac-Wakimoto character formula). "
            f"This is the key example: C_2-cofinite AND Koszul."
        ),
    )


def admissible_sl3_bridge(p: int, q: int) -> C2KoszulBridgeData:
    """L_k(sl_3) at admissible level: C_2-cofinite, Koszulness OPEN."""
    if p < 3 or q < 1 or gcd(p, q) != 1:
        raise ValueError(f"Invalid admissible sl_3: p={p}, q={q}")

    c_val = Rational(8 * (p - 3 * q), p)  # c = dim(g) * k / (k + h^v)
    # Actually c(hat{sl_3}_k) = 8k/(k+3) with k = p/q - 3
    # = 8*(p/q - 3)/(p/q) = 8*(p - 3q)/p
    kappa_val = Rational(8 * p, 6 * q)  # kappa = dim(g)*(k+h^v)/(2h^v) = 8*(p/q)/(2*3) = 4p/(3q)

    return C2KoszulBridgeData(
        name=f"L_{{k={p}/{q}-3}}(sl_3) admissible",
        algebra_type="simple_quotient",
        c2_status=C2Status.C2_COFINITE,  # Arakawa 2017
        koszul_status=KoszulStatus.OPEN,
        bridge_relation=BridgeRelation.OPEN_KOSZUL,
        associated_variety=AssociatedVarietyType.POINT,
        associated_variety_dim=0,
        c2_quotient_dim=None,  # complex to compute for sl_3
        generators=["e1", "h1", "f1", "e2", "h2", "f2", "e12", "f12"],
        generator_weights=[1] * 8,
        central_charge=c_val,
        kappa=kappa_val,
        li_bar_e1_finiteness=True,
        li_bar_e2_diagonal=False,  # not proved
        null_vectors_in_bar_range=True,
        has_modular_characters=True,
        genus_g_conformal_blocks=True,
        notes=(
            f"L_k(sl_3) at admissible level: C_2-cofinite (Arakawa 2017) "
            f"and rational. Koszulness OPEN for rank >= 2 "
            f"(rem:admissible-koszul-status). The structural argument "
            f"for sl_2 (single-weight null vector) fails for sl_3 "
            f"(null vectors at multiple conformal weights). "
            f"The Li--bar spectral sequence approach via "
            f"thm:associated-variety-koszulness is the most promising "
            f"route: X = {{0}} => R_V finite-dim Poisson, need to verify "
            f"diagonal concentration of Li--bar E_2."
        ),
    )


def lattice_voa_bridge(rank: int, det: int = 1) -> C2KoszulBridgeData:
    """Lattice VOA V_Lambda: BOTH C_2-cofinite AND Koszul."""
    return C2KoszulBridgeData(
        name=f"V_Lambda (rank-{rank} lattice VOA)",
        algebra_type="lattice",
        c2_status=C2Status.C2_COFINITE,
        koszul_status=KoszulStatus.KOSZUL,
        bridge_relation=BridgeRelation.BOTH,
        associated_variety=AssociatedVarietyType.POINT,
        associated_variety_dim=0,
        c2_quotient_dim=None,  # finite but complex
        generators=[f"J^{i}" for i in range(1, rank + 1)] + ["e^alpha_i"],
        generator_weights=[1] * rank + [1],  # simplified
        central_charge=rank,
        kappa=rank,  # kappa(lattice VOA) = rank (AP48)
        li_bar_e1_finiteness=True,
        li_bar_e2_diagonal=True,
        null_vectors_in_bar_range=False,
        has_modular_characters=True,
        genus_g_conformal_blocks=True,
        notes=(
            f"Lattice VOA V_Lambda (rank {rank}): BOTH C_2-cofinite "
            f"(lattice VOAs are rational) AND Koszul "
            f"(thm:lattice:koszul-morphism via lattice weight filtration). "
            f"kappa = rank = {rank} (AP48: NOT c/2 in general for lattice VOAs). "
            f"Has modular characters and well-defined genus-g conformal blocks."
        ),
    )


def betagamma_bridge() -> C2KoszulBridgeData:
    """Beta-gamma system: Koszul but NOT C_2-cofinite."""
    return C2KoszulBridgeData(
        name="beta-gamma at lambda=1",
        algebra_type="free_field",
        c2_status=C2Status.NOT_C2_COFINITE,
        koszul_status=KoszulStatus.KOSZUL,
        bridge_relation=BridgeRelation.KOSZUL_ONLY,
        associated_variety=AssociatedVarietyType.OTHER,
        associated_variety_dim=2,  # X = C^2 (two generators)
        c2_quotient_dim=None,
        generators=["beta", "gamma"],
        generator_weights=[1, 0],
        central_charge=Rational(2),
        kappa=Rational(1),
        li_bar_e1_finiteness=False,
        li_bar_e2_diagonal=True,
        null_vectors_in_bar_range=False,
        has_modular_characters=False,
        genus_g_conformal_blocks=False,
        notes=(
            "Beta-gamma system: Koszul by PBW universality. "
            "Associated variety = C^2 (two free-field generators). "
            "NOT C_2-cofinite. Shadow class C (contact), depth 4."
        ),
    )


def w3_universal_bridge() -> C2KoszulBridgeData:
    """Universal W_3: Koszul but NOT C_2-cofinite."""
    c = Symbol('c')
    return C2KoszulBridgeData(
        name="W_3 (universal)",
        algebra_type="universal",
        c2_status=C2Status.NOT_C2_COFINITE,
        koszul_status=KoszulStatus.KOSZUL,
        bridge_relation=BridgeRelation.KOSZUL_ONLY,
        associated_variety=AssociatedVarietyType.OTHER,
        associated_variety_dim=2,  # X = C^2 (generators T, W)
        c2_quotient_dim=None,
        generators=["T", "W"],
        generator_weights=[2, 3],
        central_charge=c,
        kappa=5 * c / 6,
        li_bar_e1_finiteness=False,
        li_bar_e2_diagonal=True,
        null_vectors_in_bar_range=False,
        has_modular_characters=False,
        genus_g_conformal_blocks=False,
        notes=(
            "Universal W_3: Koszul by PBW + Feigin-Frenkel. "
            "X = C^2 (polynomial ring in two generators). "
            "NOT C_2-cofinite. kappa = 5c/6 (AP1: not c/2)."
        ),
    )


# ============================================================================
# Full landscape comparison
# ============================================================================

def full_landscape() -> List[C2KoszulBridgeData]:
    """Return bridge data for all standard families."""
    return [
        heisenberg_bridge(),
        universal_affine_sl2_bridge(),
        virasoro_universal_bridge(),
        minimal_model_bridge(2, 5),   # Yang-Lee: C_2-cofinite, NOT Koszul
        minimal_model_bridge(3, 4),   # Ising: C_2-cofinite, NOT Koszul
        minimal_model_bridge(2, 7),   # (2,7) model
        minimal_model_bridge(3, 5),   # (3,5) model
        admissible_sl2_bridge(2, 1),  # k=0: L_0(sl_2), C_2 + Koszul
        admissible_sl2_bridge(3, 2),  # k=-1/2
        admissible_sl2_bridge(4, 3),  # k=-2/3
        admissible_sl3_bridge(4, 1),  # sl_3 admissible, Koszul OPEN
        lattice_voa_bridge(1),        # Rank-1 lattice
        lattice_voa_bridge(8),        # E_8 lattice
        lattice_voa_bridge(24),       # Leech lattice
        betagamma_bridge(),
        w3_universal_bridge(),
    ]


def classify_landscape() -> Dict[str, List[str]]:
    """Classify all standard families by bridge relation."""
    landscape = full_landscape()
    result: Dict[str, List[str]] = {
        "BOTH": [],
        "C2_ONLY": [],
        "KOSZUL_ONLY": [],
        "NEITHER": [],
        "OPEN_KOSZUL": [],
    }
    for data in landscape:
        if data.bridge_relation == BridgeRelation.BOTH:
            result["BOTH"].append(data.name)
        elif data.bridge_relation == BridgeRelation.C2_ONLY:
            result["C2_ONLY"].append(data.name)
        elif data.bridge_relation == BridgeRelation.KOSZUL_ONLY:
            result["KOSZUL_ONLY"].append(data.name)
        elif data.bridge_relation == BridgeRelation.NEITHER:
            result["NEITHER"].append(data.name)
        elif data.bridge_relation == BridgeRelation.OPEN_KOSZUL:
            result["OPEN_KOSZUL"].append(data.name)
    return result


# ============================================================================
# Theoretical bridge analysis
# ============================================================================

def implication_c2_implies_koszul() -> Dict[str, Any]:
    """Analysis: does C_2-cofiniteness imply Koszulness?

    ANSWER: NO.

    Counterexamples: Virasoro minimal models L(c_{p,q}).
    These are C_2-cofinite (X = {0}, rational) but NOT Koszul
    (null vectors in bar-relevant range break PBW collapse).

    The obstruction: C_2-cofiniteness gives finiteness of V/C_2(V),
    which means the Li--bar E_1 page is finite-dimensional.
    But finiteness does NOT imply diagonal concentration of E_2.
    The null vectors in the bar-relevant range create off-diagonal
    bar cohomology that persists through the spectral sequence.
    """
    return {
        "implication": "C_2-cofinite => Koszul",
        "holds": False,
        "counterexamples": [
            "L(c_{2,5}) Yang-Lee model (c = -22/5)",
            "L(c_{3,4}) Ising model (c = 1/2)",
            "L(c_{3,5}) (c = -3/5)",
            "All Virasoro minimal models L(c_{p,q}) with pq - p - q + 1 >= 4",
        ],
        "obstruction": (
            "C_2-cofiniteness gives finite-dim Li--bar E_1 page, "
            "but null vectors in bar-relevant range create off-diagonal "
            "bar cohomology. E_2 diagonal concentration FAILS."
        ),
        "what_c2_gives": (
            "Finiteness of V/C_2(V) => Li--bar E_1 finite-dim => "
            "spectral sequence converges. But convergence != collapse."
        ),
    }


def implication_koszul_implies_c2() -> Dict[str, Any]:
    """Analysis: does Koszulness imply C_2-cofiniteness?

    ANSWER: NO.

    Counterexamples: V_k(g) universal affine at generic k.
    These are Koszul (cor:universal-koszul) but X = g* is the full
    dual Lie algebra (dim g > 0), so NOT C_2-cofinite.

    Also: universal Virasoro Vir_c (Koszul, X = C, not C_2-cofinite).
    Also: beta-gamma, free fermion, etc.

    The key: Koszulness is about the SHAPE of bar cohomology
    (concentration in degree 1). C_2-cofiniteness is about the SIZE
    of the associated graded (finite-dimensionality). These are
    independent geometric properties.
    """
    return {
        "implication": "Koszul => C_2-cofinite",
        "holds": False,
        "counterexamples": [
            "V_k(sl_2) at generic k (X = sl_2* = C^3)",
            "Universal Virasoro Vir_c (X = C)",
            "Heisenberg H_k (X = C)",
            "Beta-gamma (X = C^2)",
            "W_3 universal (X = C^2)",
            "Any universal vertex algebra from Feigin-Frenkel free generation",
        ],
        "obstruction": (
            "Koszulness is bar concentration (shape of H*(B(V))). "
            "C_2-cofiniteness is finiteness of V/C_2(V) (size of X_V). "
            "Universal algebras V_k(g) are Koszul at ALL levels "
            "including those where X = g* has positive dimension."
        ),
        "key_insight": (
            "PBW universality (prop:pbw-universality) gives Koszulness "
            "for ALL freely strongly generated vertex algebras, regardless "
            "of the size of their associated variety."
        ),
    }


def intersection_analysis() -> Dict[str, Any]:
    """Analysis of the intersection: C_2-cofinite AND Koszul.

    The intersection is nonempty and mathematically important:
    - L_k(sl_2) at all admissible levels
    - Lattice VOAs V_Lambda for positive-definite even lattices
    - (Conjecturally) L_k(g) for non-degenerate admissible and rank >= 2

    For algebras in the intersection, BOTH theories apply:
    1. Zhu/Huang: modular invariance, genus-g conformal blocks
    2. Bar-cobar: shadow obstruction tower, Koszul duality

    This is the KEY RESULT for the monograph: on the intersection,
    the bar-cobar machinery and the Zhu/Huang conformal block theory
    are SIMULTANEOUSLY valid, giving two independent approaches to
    higher-genus data.
    """
    return {
        "intersection_nonempty": True,
        "proved_examples": [
            "L_k(sl_2) at all admissible levels (Koszul + Arakawa C_2)",
            "Lattice VOAs V_Lambda (lattice Koszul + rational C_2)",
        ],
        "conjectural_examples": [
            "L_k(sl_N) at non-degenerate admissible for N >= 3 (C_2 proved, Koszul OPEN)",
        ],
        "significance": (
            "On the intersection, both Zhu/Huang (modular invariance, "
            "genus-g conformal blocks) and bar-cobar (Koszul duality, "
            "shadow obstruction tower, MC element) are valid. The two "
            "theories give INDEPENDENT approaches to higher-genus data, "
            "and their agreement is a powerful consistency check."
        ),
        "factorization_homology_bridge": (
            "Item (vii) of thm:koszul-equivalences-meta: Koszul => "
            "factorization homology int_{Sigma_g} A concentrated in degree 0. "
            "Van Ekeren-Heluani (2019): chiral homology of C_2-cofinite VOAs "
            "on elliptic curves recovers Zhu's algebra data. These are "
            "COMPATIBLE but not identical statements: factorization homology "
            "concentration is about the derived category, while Zhu's modular "
            "invariance is about characters."
        ),
    }


def gap_analysis() -> Dict[str, Any]:
    """Analysis of the gap between C_2-cofiniteness and Koszulness.

    The gap has TWO sides:

    GAP A: C_2-cofinite, NOT Koszul (e.g., minimal models).
      These algebras have well-behaved modular theory (Zhu/Huang)
      but the bar-cobar machinery does NOT apply in full.
      The bar complex H*(B(V)) has cohomology outside degree 1.
      The shadow obstruction tower does not truncate cleanly.

    GAP B: Koszul, NOT C_2-cofinite (e.g., universal algebras).
      These algebras have full bar-cobar machinery but the Zhu/Huang
      modular theory does NOT apply (characters are not modular in
      the classical sense). The shadow obstruction tower works at
      all finite orders, but the analytic completion (MC5) requires
      separate treatment.

    WHAT CLOSES THE GAP:
    For Gap A: the Li--bar spectral sequence
    (thm:associated-variety-koszulness) provides a PATH from
    C_2-cofiniteness to Koszulness, conditional on diagonal
    concentration of the Li--bar E_2 page. The missing ingredient
    is a GEOMETRIC criterion for when the Poisson d_1 differential
    produces diagonal concentration.

    For Gap B: the analytic sewing programme (MC5, thm:general-hs-sewing)
    provides convergent partition functions for Koszul algebras
    even without C_2-cofiniteness, using the HS-sewing condition
    (polynomial OPE growth + subexponential sector growth).
    """
    return {
        "gap_A": {
            "description": "C_2-cofinite but NOT Koszul",
            "examples": ["Virasoro minimal models L(c_{p,q})"],
            "what_works": "Zhu modular invariance, Huang genus-g blocks",
            "what_fails": "Bar-cobar inversion, shadow obstruction tower",
            "closing_strategy": (
                "Li--bar spectral sequence: C_2-cofinite gives finite E_1 page. "
                "Need: geometric criterion for Li--bar E_2 diagonal concentration "
                "from the Poisson structure on X_V."
            ),
        },
        "gap_B": {
            "description": "Koszul but NOT C_2-cofinite",
            "examples": [
                "Universal V_k(g)", "Universal Vir_c",
                "Heisenberg H_k", "beta-gamma",
            ],
            "what_works": "Bar-cobar, shadow tower, MC element, Koszul duality",
            "what_fails": "Zhu modular invariance (no finite irrep theory)",
            "closing_strategy": (
                "MC5 analytic sewing: HS-sewing condition gives convergent "
                "partition functions via thm:general-hs-sewing, bypassing "
                "the C_2-cofiniteness requirement."
            ),
        },
    }


def c2_bar_complex_relation(c2_cofinite: bool, koszul: bool) -> Dict[str, str]:
    """What C_2-cofiniteness implies about the bar complex B(A).

    This is the precise technical connection.
    """
    result = {}

    if c2_cofinite:
        result["li_bar_e1"] = "finite-dimensional at each weight (X_V = {0})"
        result["li_bar_d1"] = (
            "determined by Poisson bracket on R_V = gr^F V, "
            "which is a finite-dimensional Poisson algebra"
        )
        result["bar_cohomology"] = (
            "H*(B(V)) is finitely generated at each weight. "
            "But concentration in degree 1 NOT guaranteed."
        )
        result["spectral_sequence"] = (
            "Li--bar SS converges (finite E_1 page). "
            "Collapse at E_2 iff Poisson differential produces "
            "diagonal concentration."
        )
    else:
        result["li_bar_e1"] = "infinite-dimensional in general"
        result["bar_cohomology"] = (
            "H*(B(V)) can be computed via PBW SS if V is Koszul. "
            "The Li--bar SS is less useful when R_V is infinite-dim."
        )

    if koszul:
        result["bar_concentration"] = "H*(B(V)) concentrated in bar degree 1 (PROVED)"
        result["bar_cobar_inversion"] = "Omega(B(V)) -> V is quasi-iso (PROVED)"
        result["ext_diagonal"] = "Ext^{p,q}(omega, omega) = 0 for p != q (PROVED)"
    else:
        result["bar_concentration"] = "NOT concentrated: H*(B(V)) has components in degree > 1"
        result["bar_cobar_inversion"] = "FAILS in general"

    return result
