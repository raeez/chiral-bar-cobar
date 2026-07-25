r"""Finite BCOV bar-carrier computations for Calabi--Yau manifolds.

Computes the graded carrier of the bar construction on the
cohomological or explicitly effective polyvector carriers of four
geometries:

    1. C^3 (flat space)
    2. Resolved conifold O(-1)+O(-1) -> P^1
    3. K3 x E (compact CY3)
    4. The quintic threefold

MATHEMATICAL FRAMEWORK
======================

The Dolbeault polyvector complex of a CY d-fold X is

    PV^{p,q}(X) = H^q(X, /\^p T_X)

It carries the Dolbeault differential and the Schouten--Nijenhuis
bracket.  A finite transferred L-infinity model additionally requires
explicit multilinear operations on the chosen carrier.  This module
records those operations only through a represented coderivation.

For a CY d-fold, the CY condition omega_X = O_X gives /\^p T_X = Omega^{d-p}_X,
so:
    PV^{p,q}(X) = H^{d-p,q}(X)   (by Hodge theory)

TOTAL SPACE: PV*(X) = bigoplus_{p,q} H^q(X, /\^p T_X) = bigoplus_{p,q} h^{d-p,q}

GRADING: The relevant grading for the L-infinity structure is the
GHOST NUMBER: gh(alpha) = p - 1 for alpha in PV^{p,q}. The total
BCOV degree is |alpha| = p + q - 1 (shifted by 1 for L-infinity).

The Schouten-Nijenhuis bracket has bidegree (-1, 0) in (p, q), giving
|[alpha, beta]_SN| = |alpha| + |beta| on the shifted grading. This is
the correct L-infinity convention: l_2 has degree 0 on g = PV*[1].

BAR CONSTRUCTION
================

The bar construction of the L-infinity algebra g = PV*(X) is:

    B(g) = (Sym^c(s^{-1} g), d_bar)

where:
    d_bar = d_1 + d_2 + d_3 + ...
    d_1 = internal differential (from dbar on X)
    d_2 = Chevalley-Eilenberg part from l_2 (Schouten bracket)
    d_k = higher parts from l_k (BCOV vertices)

For COMPACT CY with dbar-cohomology representatives, d_1 = 0 on
cohomology. The bar complex reduces to:

    B(H*(g)) = (Sym^c(s^{-1} H*(g)), d_2 + d_3 + ...)

The finite routines below determine the dimensions of
``Sym^k(s^{-1}H(PV(X)))``.  They determine a bar complex precisely when
a represented square-zero coderivation is also present.  The constant
polyvector model of C^3 carries the exact zero coderivation.  The
The conifold, K3 x E, and quintic profiles expose an open coderivation
slot; their finite coderivations and bar cohomology remain separate
construction problems.

COMPUTE-LANE SCALAR SHADOW:

The functions below use a named scalar-shadow input.  The
``euler_half_shadow`` lane has value chi(X)/2.  The BCOV one-loop
normalization chi(X)/24 is stored separately, as is the K3 x E BKM/BPS
automorphic readout.  These lane names prevent their numerical values
from being merged.

The independent scalar-shadow coefficients are, in the selected lane:
    F_g^{sc} = kappa_compute * lambda_g^{FP}.

The BCOV amplitudes require higher-arity projections of a represented
bar Maurer--Cartan element, including the Yukawa couplings C_{ijk} and
their higher-genus descendants.  The carrier calculation supplies the
domain for that construction; the scalar-shadow formula supplies an
independent one-dimensional projection.

OBJECT FIREWALL:

A, B(A), A^i, A^!, and the chiral derived centre are different objects.
This module computes polyvector carriers and the represented part of
the bar coalgebra on g = PV*(X).  The objects A^i, Verdier/Koszul dual
A^!, and the derived centre belong to their reconstruction layers. If
the holographic package H(T) is mentioned downstream,
it has seven entries:
    (A, A^i, A^!, C, r(z), Theta_A, nabla_hol)

C^3 SPECIFICS
=============

PV*(C^3) = C[x,y,z] tensor /\*(d_x, d_y, d_z)

This is infinite-dimensional. The L-infinity brackets are:
    l_2(f d_i, g d_j) = f (d_i g) d_j - g (d_j f) d_i   (Schouten bracket)
    l_3 from the Kodaira-Spencer cubic vertex ~ C_{ijk}

For the FORMAL neighborhood of the origin (constant + linear terms),
the truncated carrier is finite-dimensional.  The present module
constructs its coderivation on the constant-polyvector subspace.

For the COHOMOLOGICAL reduction (on the equivariant cohomology of
the torus action), PV*(C^3) reduces to a 1-dimensional space in
each sector, and kappa = 1.

CONIFOLD EFFECTIVE CARRIER
==========================

The resolved conifold is non-compact, so a finite polyvector
cohomology model depends on support and boundary conditions.  This
module retains a three-vector effective carrier with degrees -2, 0,
and 1 after desuspension.  A geometric comparison with compactly
supported or logarithmic polyvectors is an explicit open input.  The
topological value chi(P^1)=2 supplies the separate effective
Euler-half scalar one.

K3 x E SPECIFICS
================

PV*(K3 x E) decomposes via Kunneth:
    PV*(K3 x E) = PV*(K3) tensor PV*(E)

with PV*(K3) and PV*(E) computed from their Hodge diamonds.

K3 Hodge diamond: h^{0,0}=1, h^{1,1}=20, h^{2,0}=1, h^{0,2}=1, h^{2,2}=1
E Hodge diamond: h^{0,0}=1, h^{1,0}=1, h^{0,1}=1, h^{1,1}=1

For K3 (CY2): /\^p T_{K3} = Omega^{2-p}_{K3}, so:
    PV^{0,q}(K3) = H^{2,q}: dims 1,0,1  (q=0,1,2)
    PV^{1,q}(K3) = H^{1,q}: dims 0,20,0  (q=0,1,2)
    PV^{2,q}(K3) = H^{0,q}: dims 1,0,1  (q=0,1,2)

Total PV*(K3) = 24-dimensional.

For E (CY1): /\^p T_E = Omega^{1-p}_E, so:
    PV^{0,q}(E) = H^{1,q}: dims 1,1  (q=0,1)
    PV^{1,q}(E) = H^{0,q}: dims 1,1  (q=0,1)

Total PV*(E) = 4-dimensional.

K3 x E is a CY3. Its polyvector fields decompose through the product
formula:
    PV^{P,Q}(K3 x E) = bigoplus_{p1+p2=P, q1+q2=Q} PV^{p1,q1}(K3) tensor PV^{p2,q2}(E)

Total dimension = dim PV*(K3) * dim PV*(E) = 24 * 4 = 96.

CONVENTIONS (following Vol I):
    - Cohomological grading (|d| = +1)
    - Bar uses desuspension: |s^{-1}v| = |v| - 1
    - kappa is the selected compute-lane scalar, not a full VOA invariant
    - Schouten bracket is graded antisymmetric with Koszul signs
    - All Fraction arithmetic for exact computations

REFERENCES:
    Bershadsky-Cecotti-Ooguri-Vafa, CMP 165 (1994) 311.
    Barannikov-Kontsevich, alg-geom/9710032 (1997).
    Costello-Li, "Quantization of open-closed BCOV theory" (2016).
    Kontsevich, "Homological algebra of mirror symmetry" (1994).
    Manin, "Three constructions of Frobenius manifolds" (1999).
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, NamedTuple, Optional, Sequence, Tuple

F = Fraction


# =========================================================================
# Section 0: Hodge diamond and polyvector field spaces
# =========================================================================

class HodgeDiamond(NamedTuple):
    """Hodge diamond h^{p,q} for a compact Kahler manifold."""
    dim: int  # complex dimension
    data: Dict[Tuple[int, int], int]  # (p,q) -> h^{p,q}

    def h(self, p: int, q: int) -> int:
        return self.data.get((p, q), 0)

    @property
    def euler(self) -> int:
        """Topological Euler characteristic = sum (-1)^{p+q} h^{p,q}."""
        return sum((-1) ** (p + q) * v for (p, q), v in self.data.items())

    @property
    def chi_O(self) -> Fraction:
        """Holomorphic Euler characteristic chi(O_X) = sum (-1)^q h^{0,q}."""
        return Fraction(sum(
            (-1) ** q * self.h(0, q) for q in range(self.dim + 1)
        ))


def k3_hodge() -> HodgeDiamond:
    """K3 surface Hodge diamond."""
    return HodgeDiamond(dim=2, data={
        (0, 0): 1,
        (1, 0): 0, (0, 1): 0,
        (2, 0): 1, (1, 1): 20, (0, 2): 1,
        (2, 1): 0, (1, 2): 0,
        (2, 2): 1,
    })


def elliptic_hodge() -> HodgeDiamond:
    """Elliptic curve Hodge diamond."""
    return HodgeDiamond(dim=1, data={
        (0, 0): 1,
        (1, 0): 1, (0, 1): 1,
        (1, 1): 1,
    })


def product_hodge(h1: HodgeDiamond, h2: HodgeDiamond) -> HodgeDiamond:
    """Hodge diamond of the product X1 x X2 via Kunneth."""
    d = h1.dim + h2.dim
    data: Dict[Tuple[int, int], int] = defaultdict(int)
    for (p1, q1), v1 in h1.data.items():
        for (p2, q2), v2 in h2.data.items():
            data[(p1 + p2, q1 + q2)] += v1 * v2
    return HodgeDiamond(dim=d, data=dict(data))


def k3_times_e_hodge() -> HodgeDiamond:
    """Hodge diamond of K3 x E (CY3)."""
    return product_hodge(k3_hodge(), elliptic_hodge())


def quintic_hodge() -> HodgeDiamond:
    """Quintic CY3 Hodge diamond."""
    return HodgeDiamond(dim=3, data={
        (0, 0): 1,
        (1, 0): 0, (0, 1): 0,
        (2, 0): 0, (1, 1): 1, (0, 2): 0,
        (3, 0): 1, (2, 1): 101, (1, 2): 101, (0, 3): 1,
        (3, 1): 0, (2, 2): 1, (1, 3): 0,
        (3, 2): 0, (2, 3): 0,
        (3, 3): 1,
    })


# =========================================================================
# Section 1: Polyvector field spaces PV^{p,q}(X)
# =========================================================================

class PolyvectorSpace(NamedTuple):
    r"""Polyvector field cohomology PV^{p,q}(X) = H^q(X, /\^p T_X).

    For CY d-fold: /\^p T_X = Omega^{d-p}_X, so PV^{p,q} = h^{d-p,q}.
    """
    name: str
    cy_dim: int
    pv_dims: Dict[Tuple[int, int], int]  # (p,q) -> dim PV^{p,q}
    total_dim: int

    @property
    def ghost_graded_dims(self) -> Dict[int, int]:
        """Dimensions graded by ghost number gh = p - 1.

        The BCOV ghost number assigns gh(alpha) = p - 1 for alpha in PV^{p,q}.
        This is the grading relevant for the L-infinity structure:
        g = PV*(X) with the L-infinity brackets becomes a graded Lie algebra
        with degree |alpha|_{Linf} = gh(alpha) + q = p + q - 1.
        """
        dims: Dict[int, int] = defaultdict(int)
        for (p, q), d in self.pv_dims.items():
            gh = p - 1
            dims[gh] += d
        return dict(dims)

    @property
    def bcov_graded_dims(self) -> Dict[int, int]:
        """Dimensions graded by BCOV degree |alpha| = p + q - 1.

        This is the total degree for the L-infinity algebra.
        """
        dims: Dict[int, int] = defaultdict(int)
        for (p, q), d in self.pv_dims.items():
            deg = p + q - 1
            dims[deg] += d
        return dict(dims)


def polyvector_space(hd: HodgeDiamond, name: str = "") -> PolyvectorSpace:
    r"""Compute PV^{p,q}(X) = H^q(X, /\^p T_X) for a CY d-fold.

    Uses CY condition: /\^p T_X = Omega^{d-p}_X, giving PV^{p,q} = h^{d-p,q}.
    """
    d = hd.dim
    pv: Dict[Tuple[int, int], int] = {}
    total = 0

    for p in range(d + 1):
        for q in range(d + 1):
            val = hd.h(d - p, q)
            if val > 0:
                pv[(p, q)] = val
                total += val

    return PolyvectorSpace(name=name, cy_dim=d, pv_dims=pv, total_dim=total)


def pv_c3_truncated(max_deg: int = 1) -> PolyvectorSpace:
    r"""Polyvector fields on C^3 truncated to polynomial degree <= max_deg.

    PV*(C^3) = C[x,y,z] tensor /\*(d_x, d_y, d_z)

    We truncate the polynomial ring to degree <= max_deg.
    For max_deg = 0: constants only -> dim = 1 + 3 + 3 + 1 = 8
    For max_deg = 1: constants + linear -> each polynomial space has
        dim = binom(3 + deg, deg) summed to max_deg.

    For the Schouten bracket computation, the relevant truncation is
    to CONSTANT polyvector fields (max_deg = 0), since higher polynomial
    degrees decouple in the equivariant cohomology.

    Ghost number grading: /\^p has gh = p - 1 (but for C^3 we use
    the convention gh = p since there is no shift by CY dimension for
    non-compact spaces in the equivariant setting).

    In the C^3 B-model compute lane, the relevant object is the
    equivariant polyvector field space for the torus action. After
    localization, each sector contributes a copy of the ground field.
    The L-infinity structure on the equivariant cohomology reduces to
    the Schouten bracket on constant polyvectors.
    """
    # Number of monomials of degree exactly d in 3 variables: binom(d+2, 2)
    # Number of degree <= max_deg: sum_{d=0}^{max_deg} binom(d+2, 2)
    n_poly = sum(math.comb(d + 2, 2) for d in range(max_deg + 1))

    pv: Dict[Tuple[int, int], int] = {}
    total = 0

    # /\^p has dim binom(3, p) components, each tensored with n_poly
    # For C^3 (non-compact), q = 0 only (Dolbeault cohomology vanishes
    # in positive q for contractible spaces, up to growth conditions).
    for p in range(4):  # p = 0, 1, 2, 3
        dim_wedge = math.comb(3, p)
        dim = n_poly * dim_wedge
        if dim > 0:
            pv[(p, 0)] = dim
            total += dim

    return PolyvectorSpace(
        name=f"C3_trunc_{max_deg}",
        cy_dim=3,
        pv_dims=pv,
        total_dim=total,
    )


def pv_c3_constant() -> PolyvectorSpace:
    r"""Constant polyvector fields on C^3.

    /\^0 = C (1-dim, functions = constants)
    /\^1 = C^3 (d_x, d_y, d_z)
    /\^2 = C^3 (d_x ^ d_y, d_y ^ d_z, d_z ^ d_x)
    /\^3 = C (d_x ^ d_y ^ d_z)

    Total: 8-dimensional.

    The Schouten bracket on CONSTANT polyvectors is ZERO (the bracket
    involves derivatives, which vanish on constants). So the L-infinity
    algebra on constant polyvectors is abelian: l_2 = 0.

    The nontrivial structure comes from the linear polyvectors (l_2)
    and the cubic BCOV vertex (l_3).
    """
    return pv_c3_truncated(max_deg=0)


def pv_conifold_effective_carrier() -> PolyvectorSpace:
    r"""Three-vector effective carrier for the resolved conifold.

    The bidegrees ``(0,0)``, ``(1,1)``, and ``(3,0)`` are formal labels
    chosen to retain the unit, one middle generator, and the volume
    generator.  They give desuspended degrees ``-2``, ``0``, and ``1``.
    A support-sensitive geometric realization is a separate comparison
    problem, and the present profile leaves its coderivation open.
    """
    return PolyvectorSpace(
        name="conifold",
        cy_dim=3,
        pv_dims={
            (0, 0): 1,   # unit label
            (1, 1): 1,   # effective middle label
            (3, 0): 1,   # volume label
        },
        total_dim=3,
    )


def pv_k3() -> PolyvectorSpace:
    """Polyvector fields on K3 surface (CY2)."""
    return polyvector_space(k3_hodge(), "K3")


def pv_elliptic() -> PolyvectorSpace:
    """Polyvector fields on an elliptic curve (CY1)."""
    return polyvector_space(elliptic_hodge(), "E")


def pv_k3_times_e() -> PolyvectorSpace:
    """Polyvector fields on K3 x E (CY3)."""
    return polyvector_space(k3_times_e_hodge(), "K3xE")


def pv_quintic() -> PolyvectorSpace:
    """Polyvector fields on the quintic CY3."""
    return polyvector_space(quintic_hodge(), "quintic")


# =========================================================================
# Section 2: Schouten-Nijenhuis bracket on polyvector fields
# =========================================================================

class SchoutenBracketData(NamedTuple):
    """Structure constants for the Schouten-Nijenhuis bracket on PV*(X).

    The Schouten-Nijenhuis bracket on polyvector fields:
        [-,-]_SN: PV^{p1,q1} x PV^{p2,q2} -> PV^{p1+p2-1, q1+q2}

    has bidegree (-1, 0) in (p, q).

    For the L-infinity algebra g = PV*(X), this becomes l_2.
    The degree of l_2 on g[1] is 0 (as required for L-infinity).
    """
    name: str
    is_abelian: bool  # True if all brackets vanish
    nonzero_brackets: int  # count of nonzero structure constants


def schouten_bracket_c3_constant() -> SchoutenBracketData:
    """Schouten bracket on constant polyvector fields on C^3.

    The Schouten bracket [f d_{i1...ip}, g d_{j1...jq}]_SN involves
    derivatives of f and g by the vector fields. For CONSTANT f, g,
    these derivatives vanish, so the bracket is identically zero.

    This means the L-infinity algebra of constant polyvectors on C^3
    is ABELIAN at l_2. The nontrivial structure comes from:
    (a) including linear terms (which give nontrivial l_2)
    (b) the BCOV l_3 cubic vertex (Kodaira-Spencer)
    """
    return SchoutenBracketData(
        name="C3_constant",
        is_abelian=True,
        nonzero_brackets=0,
    )


def schouten_bracket_c3_linear() -> SchoutenBracketData:
    """Schouten bracket structure on C^3 with linear polyvectors.

    Including linear polynomials, the Schouten bracket is nontrivial.
    The key brackets on the linear sector:

    [x_i d_j, x_k d_l]_SN = delta_{jk} x_i d_l - delta_{li} x_k d_j

    This is the gl(3) Lie bracket on (1,1)-tensors = endomorphisms.
    The space of linear (1,0)-polyvector fields = gl(3) = 9-dimensional.

    The full bracket extends to all polyvector degrees via the
    Leibniz rule for the Schouten bracket.
    """
    # Count nonzero brackets in the linear sector
    # gl(3) has dim 9, bracket given by commutator
    # Number of nonzero [e_{ij}, e_{kl}] = nonzero structure constants of gl(3)
    # = 9 * 8 - (number of zero brackets)
    # For gl(3): [e_{ij}, e_{kl}] = delta_{jk} e_{il} - delta_{li} e_{kj}
    # Nonzero when j=k or l=i (but not both cancelling)
    count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    # [e_{ij}, e_{kl}] = delta_{jk} e_{il} - delta_{li} e_{kj}
                    result = {}
                    if j == k:
                        result[(i, l)] = result.get((i, l), 0) + 1
                    if l == i:
                        result[(k, j)] = result.get((k, j), 0) - 1
                    # Check if result is nonzero
                    if any(v != 0 for v in result.values()):
                        count += 1

    return SchoutenBracketData(
        name="C3_linear",
        is_abelian=False,
        nonzero_brackets=count,
    )


def schouten_bracket_k3_on_h11() -> SchoutenBracketData:
    """Schouten bracket structure on K3 restricted to PV^{1,1}.

    PV^{1,1}(K3) = H^1(T_{K3}) = 20-dimensional (deformation space).

    The Schouten bracket restricted to PV^{1,1} x PV^{1,1}:
        [-,-]_SN: PV^{1,1} x PV^{1,1} -> PV^{1,2}

    But PV^{1,2}(K3) = H^{1,2}(K3) = 0 for K3.

    So the bracket PV^{1,1} x PV^{1,1} -> PV^{1,2} is ZERO.

    The nontrivial brackets on K3 involve the holomorphic symplectic form:
        PV^{1,1} x PV^{1,1} -> PV^{1,2} = 0  (vanishes on K3)
        PV^{0,0} x PV^{2,2} -> PV^{1,2} = 0
        PV^{2,0} x PV^{1,1} -> PV^{2,1} = H^{0,1}(K3) = 0

    In fact, for K3, the Schouten bracket on cohomology is TRIVIAL
    (K3 has unobstructed deformations, the Bogomolov-Tian-Todorov
    theorem). The L-infinity algebra on H*(PV*(K3)) is formal with
    all l_k = 0 for k >= 2 at the cohomological level.
    """
    return SchoutenBracketData(
        name="K3_h11",
        is_abelian=True,
        nonzero_brackets=0,
    )


# =========================================================================
# Section 3: Finite carrier profiles and scalar lanes
# =========================================================================

class BCOVCarrierInput(NamedTuple):
    """Finite inputs available to the carrier engine.

    The record contains the selected polyvector carrier, the status of
    its full bar coderivation, and one named scalar lane.  A profile with
    ``coderivation_status='open'`` carries no bracket maps.
    """
    name: str
    pv: PolyvectorSpace
    coderivation_status: str
    scalar_lane: str
    scalar_value: Fraction
    bcov_one_loop_scalar: Optional[Fraction]
    shadow_depth_class: str  # G, L, C, or M

    @property
    def requires_coderivation_construction(self) -> bool:
        return self.coderivation_status == "open"


def bcov_input_c3() -> BCOVCarrierInput:
    """Finite BCOV carrier inputs for C^3.

    C^3 is the simplest CY3: flat, no compact cycles, no instantons.

    On the eight-dimensional constant-polyvector carrier, every
    Schouten bracket vanishes and the selected higher operations are
    zero.  Hence the represented coderivation is exactly zero.  The
    separate equivariant scalar lane has value one.

    Shadow depth class: G.  On constant polyvectors every represented
    bracket vanishes, so the exact bar coderivation is zero and the bar
    cohomology equals the full cofree carrier in every retained arity.

    The DT partition function is Z^{C^3} = M(-q) (MacMahon), which
    is the exponential of genus-g constant map contributions.
    """
    pv = pv_c3_constant()
    return BCOVCarrierInput(
        name="C3",
        pv=pv,
        coderivation_status="represented_zero",
        scalar_lane="equivariant_constant_map",
        scalar_value=F(1),
        bcov_one_loop_scalar=None,
        shadow_depth_class="G",
    )


def bcov_input_conifold() -> BCOVCarrierInput:
    """Finite BCOV carrier inputs for the resolved conifold.

    The three-dimensional carrier is an explicit effective truncation
    for the non-compact geometry.  Its bar coderivation is open.  The
    effective Euler-half scalar lane has value chi/2=1.  The auxiliary
    A-model prepotential cubic is recorded separately by
    :func:`yukawa_conifold` as an auxiliary comparison object.
    """
    pv = pv_conifold_effective_carrier()
    return BCOVCarrierInput(
        name="conifold",
        pv=pv,
        coderivation_status="open",
        scalar_lane="effective_euler_half_shadow",
        scalar_value=F(1),
        bcov_one_loop_scalar=None,
        shadow_depth_class="G",
    )


def bcov_input_k3_times_e() -> BCOVCarrierInput:
    r"""Finite BCOV carrier inputs for K3 x E.

    K3 x E is a compact CY3 with:
        chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0

    So the compact topological/BCOV Euler lane has value 0.

    The BPS/BKM scalar lane used by this engine is a different
    automorphic readout. For K3 x E:

        kappa_BKM(K3 x E) = 5 (weight of the primitive denominator Delta_5)

    This is the BKM/BPS automorphic value, not the compact total-space
    value kappa_cat(K3 x E)=0 and not the Heisenberg-Mukai chiral
    specialisation kappa_ch^{Heis}(K3 x E)=3.

    Independent compute-lane checks for kappa_BKM = 5:
    1. Weight of the primitive Gritsenko-Nikulin denominator Delta_5
    2. BKM superalgebra root multiplicities
    3. Borcherds product formula: c_{phi_{0,1}}(0)/2 = 10/2 = 5
    4. Igusa-square check: Phi_10^{un}=Delta_5^2 has weight 10

    The 96-dimensional Hodge-theoretic carrier is exact.  Its
    transferred multilinear operations and bar coderivation remain
    open data.  The auxiliary Kähler prepotential cubic is recorded
    separately by :func:`yukawa_k3_times_e`.

    Shadow depth class: M records the infinite BKM scalar-shadow tower
    controlled by the reciprocal Igusa square
    Phi_10^{-1}=Delta_5^{-2}.  The full finite coderivation is an
    additional operation.
    """
    pv = pv_k3_times_e()
    return BCOVCarrierInput(
        name="K3xE",
        pv=pv,
        coderivation_status="open",
        scalar_lane="BKM",
        scalar_value=F(5),
        bcov_one_loop_scalar=F(0),
        shadow_depth_class="M",
    )


def bcov_input_quintic() -> BCOVCarrierInput:
    """Finite BCOV carrier inputs for the quintic CY3.

    chi(quintic) = -200.
    The Euler-half shadow has value chi/2=-100.  The canonical BCOV
    one-loop scalar is stored separately as chi/24=-25/3.

    The quintic has h^{2,1} = 101 complex structure deformations
    and h^{1,1} = 1 Kahler modulus (for the B-model).

    The Hodge-theoretic carrier is exact.  Period-derived interaction
    tensors and the resulting bar coderivation remain open data.

    Shadow depth class: M (infinite GW tower).
    """
    pv = pv_quintic()
    return BCOVCarrierInput(
        name="quintic",
        pv=pv,
        coderivation_status="open",
        scalar_lane="euler_half_shadow",
        scalar_value=F(-100),
        bcov_one_loop_scalar=F(-25, 3),
        shadow_depth_class="M",
    )


# =========================================================================
# Section 4: Finite graded-symmetric bar carrier
# =========================================================================

BarBasisIndex = Tuple[int, int]
BarState = Dict[BarBasisIndex, Fraction]


@dataclass(frozen=True)
class RepresentedBarDifferential:
    """A finite square-zero differential on a chosen bar-carrier basis.

    ``carrier_dims[k]`` numbers the basis vectors in bar arity ``k``;
    ``basis_degrees[(k,i)]`` records their cohomological degrees.
    ``images[(k, i)]`` is the sparse image of the ``i``-th basis vector
    in that arity.  This object checks the actual state transition and
    the identity ``d^2=0``.  The flag ``coderivation_verified`` records
    whether the co-Leibniz identity has also been established on the
    represented carrier.  Within this module that stronger assertion is
    made intrinsically only for the zero differential.
    """

    carrier_dims: Mapping[int, int]
    basis_degrees: Mapping[BarBasisIndex, int]
    images: Mapping[BarBasisIndex, Mapping[BarBasisIndex, Fraction]]
    source: str
    coderivation_verified: bool = False
    uses_yukawa: bool = False

    def __post_init__(self) -> None:
        dims = dict(self.carrier_dims)
        if any(k < 1 or dim < 0 for k, dim in dims.items()):
            raise ValueError("bar arities and carrier dimensions must be nonnegative")
        expected_basis = {
            (arity, index)
            for arity, dim in dims.items()
            for index in range(dim)
        }
        if set(self.basis_degrees) != expected_basis:
            raise ValueError("basis_degrees must grade every represented carrier basis vector")
        for (arity, index), image in self.images.items():
            if arity not in dims or not 0 <= index < dims[arity]:
                raise ValueError("differential source index lies outside the carrier")
            for (target_arity, target_index), coefficient in image.items():
                if target_arity not in dims or not 0 <= target_index < dims[target_arity]:
                    raise ValueError("differential target index lies outside the carrier")
                Fraction(coefficient)
                if (
                    Fraction(coefficient)
                    and self.basis_degrees[(target_arity, target_index)]
                    != self.basis_degrees[(arity, index)] + 1
                ):
                    raise ValueError("represented differential must have cohomological degree +1")
        if self.coderivation_verified and not self.is_zero:
            raise ValueError(
                "nonzero coderivations require an explicit coproduct-level verifier"
            )
        if not self.square_zero:
            raise ValueError("represented bar differential must satisfy d^2=0")

    @property
    def is_zero(self) -> bool:
        return all(
            Fraction(coefficient) == 0
            for image in self.images.values()
            for coefficient in image.values()
        )

    def apply(self, state: Mapping[BarBasisIndex, Fraction]) -> BarState:
        """Apply the represented differential to a sparse carrier state."""
        result: BarState = {}
        for basis_index, coefficient in state.items():
            arity, index = basis_index
            if arity not in self.carrier_dims or not 0 <= index < self.carrier_dims[arity]:
                raise ValueError("state index lies outside the represented carrier")
            for target, matrix_coefficient in self.images.get(basis_index, {}).items():
                value = result.get(target, F(0)) + F(coefficient) * F(matrix_coefficient)
                if value:
                    result[target] = value
                elif target in result:
                    del result[target]
        return result

    @property
    def square_zero(self) -> bool:
        for arity, dim in self.carrier_dims.items():
            for index in range(dim):
                if self.apply(self.apply({(arity, index): F(1)})):
                    return False
        return True


def _basis_degrees_from_distribution(
    carrier_graded_dims: Mapping[int, Mapping[int, int]],
) -> Dict[BarBasisIndex, int]:
    """Choose a degree-ordered basis for each finite carrier arity."""
    result: Dict[BarBasisIndex, int] = {}
    for arity, degree_dims in carrier_graded_dims.items():
        index = 0
        for degree, dimension in sorted(degree_dims.items()):
            for _ in range(dimension):
                result[(arity, index)] = degree
                index += 1
    return result


def zero_bar_coderivation(
    carrier_graded_dims: Mapping[int, Mapping[int, int]],
    source: str,
) -> RepresentedBarDifferential:
    """Construct the exact zero coderivation on a finite bar carrier."""
    carrier_dims = {
        arity: sum(degree_dims.values())
        for arity, degree_dims in carrier_graded_dims.items()
    }
    return RepresentedBarDifferential(
        carrier_dims=carrier_dims,
        basis_degrees=_basis_degrees_from_distribution(carrier_graded_dims),
        images={},
        source=source,
        coderivation_verified=True,
        uses_yukawa=False,
    )


class BCOVBarCarrier(NamedTuple):
    """Finite bar-construction record with an explicit epistemic boundary.

    ``bar_carrier_graded_dims`` gives the actual cohomological grading
    of the cofree graded-symmetric carrier.  ``bar_cohomology_dims`` and
    its graded refinement are populated only on the exact
    zero-coderivation lane, where carrier and cohomology coincide.
    ``scalar_shadow_amplitudes`` are independent modular trace values;
    they are inputs to comparison with BCOV amplitudes rather than
    outputs of the bar differential.
    """

    name: str
    carrier_input: BCOVCarrierInput
    bar_carrier_dims: Dict[int, int]
    bar_carrier_graded_dims: Dict[int, Dict[int, int]]
    differential: Optional[RepresentedBarDifferential]
    bar_cohomology_dims: Optional[Dict[int, int]]
    bar_cohomology_graded_dims: Optional[Dict[int, Dict[int, int]]]
    max_bar_degree: int
    scalar_shadow_amplitudes: Dict[int, Fraction]

    @property
    def coderivation_constructed(self) -> bool:
        return bool(self.differential and self.differential.coderivation_verified)

    @property
    def yukawa_entered_coderivation(self) -> bool:
        return bool(self.differential and self.differential.uses_yukawa)

    @property
    def bar_cohomology_computed(self) -> bool:
        return self.bar_cohomology_dims is not None


def _graded_sym_dim(dims: Dict[int, int], k: int) -> int:
    """Dimension of Sym^k(V) for a graded vector space V.

    Even-degree generators contribute symmetric powers.
    Odd-degree generators contribute exterior powers (Koszul sign rule).
    """
    if k == 0:
        return 1

    degrees = sorted(dims.keys())
    if not degrees:
        return 0

    return _partition_sym(tuple(degrees), tuple(sorted(dims.items())), k, 0)


def _graded_sym_distribution(dims: Mapping[int, int], k: int) -> Dict[int, int]:
    """Cohomological-degree distribution of ``Sym^k(V)``.

    This is an independent Hilbert-series computation: even generators
    contribute symmetric powers and odd generators exterior powers.
    """
    states: Dict[Tuple[int, int], int] = {(0, 0): 1}
    for degree, multiplicity in sorted(dims.items()):
        updated: Dict[Tuple[int, int], int] = defaultdict(int)
        max_power = k if degree % 2 == 0 else min(k, multiplicity)
        for (used, total_degree), coefficient in states.items():
            for power in range(min(max_power, k - used) + 1):
                if degree % 2 == 0:
                    factor = math.comb(multiplicity + power - 1, power)
                else:
                    factor = math.comb(multiplicity, power)
                updated[(used + power, total_degree + power * degree)] += (
                    coefficient * factor
                )
        states = dict(updated)
    return {
        total_degree: dimension
        for (used, total_degree), dimension in states.items()
        if used == k and dimension
    }


@lru_cache(maxsize=8192)
def _partition_sym(degrees: tuple, dims_items: tuple, remaining: int, idx: int) -> int:
    """Recursive graded symmetric product dimension computation."""
    if idx >= len(degrees):
        return 1 if remaining == 0 else 0

    n = degrees[idx]
    d_n = dict(dims_items)[n]

    total = 0
    max_j = remaining
    if n % 2 == 1:
        # Odd degree: exterior powers, bounded by dimension
        max_j = min(remaining, d_n)

    for j in range(max_j + 1):
        if n % 2 == 0:
            # Even degree: symmetric power binom(d_n + j - 1, j)
            sym_dim = math.comb(d_n + j - 1, j)
        else:
            # Odd degree: exterior power binom(d_n, j)
            if j > d_n:
                continue
            sym_dim = math.comb(d_n, j)

        if sym_dim == 0:
            continue

        rest = _partition_sym(degrees, dims_items, remaining - j, idx + 1)
        total += sym_dim * rest

    return total


def _faber_pandharipande(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g on M_g.

    The scalar shadow convention used here takes lambda_g^{FP} to be the
    absolute value of the coefficient a_g in

        (x/2)/sinh(x/2) = sum_{g>=0} a_g x^{2g}.

    Thus lambda_1^{FP}=1/24, lambda_2^{FP}=7/5760, and
    lambda_3^{FP}=31/967680. The signed coefficients a_g enter the
    A-hat series; this helper returns their absolute values for the
    positive scalar amplitude factor.
    """
    if g < 1:
        return F(0)

    # Since sinh(x/2)/(x/2) = sum_{m>=0} x^{2m}/(4^m (2m+1)!),
    # the inverse-series coefficients satisfy:
    # a_0 = 1,
    # a_n = -sum_{m=1}^{n} a_{n-m}/(4^m (2m+1)!).
    a = [F(0)] * (g + 1)
    a[0] = F(1)
    for n in range(1, g + 1):
        s = F(0)
        for m in range(1, n + 1):
            denom = F(4) ** m * F(math.factorial(2 * m + 1))
            s += a[n - m] / denom
        a[n] = -s

    # a[g] is the signed coefficient of x^{2g}; the compute lane uses |a[g]|.
    return abs(a[g])


def compute_bar_carrier(profile: BCOVCarrierInput,
                        max_bar_degree: int = 4,
                        max_genus: int = 5,
                        differential: Optional[RepresentedBarDifferential] = None,
                        ) -> BCOVBarCarrier:
    """Compute a finite bar carrier and attach represented differential data.

    The cofree carrier underlying B(g) for g = PV*(X) is:
        B^k = Sym^k(s^{-1} g)

    The desuspension s^{-1} shifts the BCOV degree down by 1 (AP45).

    For the constant-polyvector C^3 model, the vanishing operations supply
    the exact zero coderivation.  Every profile with open coderivation
    status returns its carrier together with an empty differential slot.  A supplied
    represented differential must match the computed carrier and satisfy
    ``d^2=0``; its co-Leibniz status remains visible in its type.
    """
    if max_bar_degree < 1:
        raise ValueError("max_bar_degree must be positive")
    if max_genus < 1:
        raise ValueError("max_genus must be positive")

    pv = profile.pv

    # Compute s^{-1}(PV*(X)) graded dimensions
    # BCOV degree of alpha in PV^{p,q} is |alpha| = p + q - 1
    # After desuspension: |s^{-1} alpha| = p + q - 2
    desuspended_dims: Dict[int, int] = defaultdict(int)
    for (p, q), d in pv.pv_dims.items():
        deg = p + q - 2  # desuspended BCOV degree
        desuspended_dims[deg] += d

    desuspended_dims = dict(desuspended_dims)

    # Compute the graded cofree carrier at each bar arity.
    carrier_dims: Dict[int, int] = {}
    carrier_graded_dims: Dict[int, Dict[int, int]] = {}
    for k in range(1, max_bar_degree + 1):
        degree_distribution = _graded_sym_distribution(desuspended_dims, k)
        carrier_graded_dims[k] = degree_distribution
        carrier_dims[k] = sum(degree_distribution.values())
        if carrier_dims[k] != _graded_sym_dim(desuspended_dims, k):
            raise ArithmeticError("graded Hilbert series disagrees with direct carrier count")

    if (
        differential is None
        and profile.coderivation_status == "represented_zero"
    ):
        differential = zero_bar_coderivation(
            carrier_graded_dims,
            source=f"{profile.name}: vanishing cohomological brackets",
        )

    if differential is not None and dict(differential.carrier_dims) != carrier_dims:
        raise ValueError("represented differential carrier does not match Sym^c(s^-1 g)")
    if differential is not None:
        for arity, expected_distribution in carrier_graded_dims.items():
            represented_distribution = Counter(
                degree
                for (basis_arity, _), degree in differential.basis_degrees.items()
                if basis_arity == arity
            )
            if represented_distribution != Counter(expected_distribution):
                raise ValueError(
                    "represented differential grading does not match the computed carrier"
                )

    cohomology_dims: Optional[Dict[int, int]] = None
    cohomology_graded_dims: Optional[Dict[int, Dict[int, int]]] = None
    if differential is not None and differential.coderivation_verified and differential.is_zero:
        cohomology_dims = dict(carrier_dims)
        cohomology_graded_dims = {
            arity: dict(degree_dims)
            for arity, degree_dims in carrier_graded_dims.items()
        }

    # Independent genus-g scalar-shadow coefficients.
    scalar_shadow: Dict[int, Fraction] = {}
    for g in range(1, max_genus + 1):
        scalar_shadow[g] = profile.scalar_value * _faber_pandharipande(g)

    return BCOVBarCarrier(
        name=profile.name,
        carrier_input=profile,
        bar_carrier_dims=carrier_dims,
        bar_carrier_graded_dims=carrier_graded_dims,
        differential=differential,
        bar_cohomology_dims=cohomology_dims,
        bar_cohomology_graded_dims=cohomology_graded_dims,
        max_bar_degree=max_bar_degree,
        scalar_shadow_amplitudes=scalar_shadow,
    )


# =========================================================================
# Section 5: Specific computations for the three geometries
# =========================================================================

def bar_carrier_c3(
    max_bar_degree: int = 4,
    max_genus: int = 5,
) -> BCOVBarCarrier:
    """Exact zero-differential bar complex on constant polyvectors of C^3.

    On constant polyvectors: 8-dimensional, all brackets zero.
    The bar carrier is the cofree coalgebra on s^{-1}(PV^*(C^3)):

    PV^{0,0} = 1-dim, BCOV degree -1, desuspended degree -2
    PV^{1,0} = 3-dim, BCOV degree 0, desuspended degree -1
    PV^{2,0} = 3-dim, BCOV degree 1, desuspended degree 0
    PV^{3,0} = 1-dim, BCOV degree 2, desuspended degree 1

    Bar degree 1: dim(s^{-1}g) = 8
    Bar degree 2: dim Sym^2(s^{-1}g)
      Degree -2: 1 even generator -> Sym powers
      Degree -1: 3 odd generators -> Ext powers
      Degree 0: 3 even generators -> Sym powers
      Degree 1: 1 odd generator -> Ext powers
    """
    return compute_bar_carrier(bcov_input_c3(), max_bar_degree, max_genus)


def bar_carrier_conifold(
    max_bar_degree: int = 4,
    max_genus: int = 5,
) -> BCOVBarCarrier:
    """Bar carrier of the cohomological BCOV model of the resolved conifold.

    3-dimensional PV space:
    PV^{0,0} = 1-dim, desuspended degree -2
    PV^{1,1} = 1-dim, desuspended degree 0
    PV^{3,0} = 1-dim, desuspended degree 1

    All three are in different degrees, with 1-dim each.  The Yukawa
    finite coderivation is required before bar cohomology is read.
    """
    return compute_bar_carrier(bcov_input_conifold(), max_bar_degree, max_genus)


def bar_carrier_k3_times_e(
    max_bar_degree: int = 4,
    max_genus: int = 5,
) -> BCOVBarCarrier:
    """Bar carrier of the cohomological BCOV model of K3 x E.

    96-dimensional PV space with rich structure.
    kappa_BKM = 5 (from the primitive Gritsenko-Nikulin denominator Delta_5).
    Its transferred finite coderivation remains an open construction.
    """
    return compute_bar_carrier(bcov_input_k3_times_e(), max_bar_degree, max_genus)


def bar_carrier_quintic(
    max_bar_degree: int = 4,
    max_genus: int = 5,
) -> BCOVBarCarrier:
    """Bar carrier of the quintic polyvector cohomology profile."""
    return compute_bar_carrier(bcov_input_quintic(), max_bar_degree, max_genus)


# =========================================================================
# Section 6: Yukawa couplings and the genus-0 prepotential
# =========================================================================

class YukawaCoupling(NamedTuple):
    """Genus-0 three-point function (Yukawa coupling) C_{ijk}.

    For a CY3 with Kahler moduli t^i (i = 1, ..., h^{1,1}):
        C_{ijk} = d^3 F_0 / dt^i dt^j dt^k

    where F_0 is the genus-0 prepotential.

    In the B-model: C_{ijk} is computed from period integrals.
    In the A-model: C_{ijk} = GW_{0,3}(beta) (genus-0, 3-point GW).
    """
    name: str
    n_moduli: int            # = h^{1,1} for Kahler, h^{2,1} for complex
    classical_cubic: Dict[Tuple[int, int, int], Fraction]
    has_instantons: bool


def yukawa_conifold() -> YukawaCoupling:
    """Yukawa coupling for the conifold.

    Single modulus t. Classical prepotential F_0 = t^3/6.
    C_{ttt} = 1.

    Instanton corrections:
    F_0^{inst} = sum_{d>=1} Li_3(e^{-dt})
    (all GV invariants n_0^d = 1 for the conifold).
    """
    return YukawaCoupling(
        name="conifold",
        n_moduli=1,
        classical_cubic={(0, 0, 0): F(1)},
        has_instantons=True,
    )


def yukawa_k3_times_e() -> YukawaCoupling:
    """Yukawa coupling for K3 x E.

    Three types of Kahler moduli:
    - t: size of E
    - tau: B-field on K3
    - sigma: overall K3 volume

    The classical cubic prepotential has the intersection form:
    F_0^{classical} = t * C^{K3}_{ab} sigma^a sigma^b / 2

    where C^{K3}_{ab} is the K3 intersection form on H^{1,1}.
    For the generic K3 with Picard lattice H (hyperbolic plane):
    C^{K3} has the intersection matrix ((0,1),(1,0)) on the two generators.

    The simplest case: h^{1,1}(K3) = 2 (rho = 1 algebraic K3),
    giving 3 Kahler moduli for K3 x E.
    C_{t,tau,sigma} = 1 (the only nonzero classical triple coupling,
    up to symmetry).
    """
    # Using a simplified model with 3 moduli: {t, tau, sigma}
    # with labels 0 = t, 1 = tau, 2 = sigma
    return YukawaCoupling(
        name="K3xE",
        n_moduli=3,
        classical_cubic={
            (0, 1, 2): F(1),  # C_{t,tau,sigma} = 1 (intersection form)
        },
        has_instantons=True,
    )


# =========================================================================
# Section 7: One-dimensional scalar-shadow coefficients
# =========================================================================

def scalar_shadow_genus1(kappa: Fraction) -> Fraction:
    """Return the genus-one scalar shadow ``kappa/24``."""
    return kappa * F(1, 24)


def scalar_shadow_genus2(kappa: Fraction) -> Fraction:
    """Return the genus-two scalar shadow ``7*kappa/5760``."""
    return kappa * F(7, 5760)


def bcov_quintic_constant_map_low_genus() -> Dict[int, Fraction]:
    r"""Compute the canonical quintic BCOV constants at genera one and two.

    The genus-one normalization is
    ``(chi/24) * (1/24)``.  At genus two the BCOV constant-map formula is

        (-1)^(g-1) |B_2g| |B_(2g-2)|
        -------------------------------- * chi/2,
           2g (2g-2) (2g-2)!

    with ``g=2``, ``|B_4|=1/30``, and ``|B_2|=1/6``.
    """
    chi = F(quintic_hodge().euler)
    one_loop_scalar = chi / F(24)
    genus_one = one_loop_scalar / F(24)
    genus_two = (
        -F(1, 30)
        * F(1, 6)
        / (F(4) * F(2) * F(math.factorial(2)))
        * (chi / F(2))
    )
    return {1: genus_one, 2: genus_two}


# =========================================================================
# Section 8: Independently supplied scalar-series comparison
# =========================================================================

class ScalarSeriesComparison(NamedTuple):
    """Comparison of a shadow series with a sourced BCOV series."""

    name: str
    shadow_lane: str
    bcov_lane: Optional[str]
    bcov_source: Optional[str]
    shadow_series: Dict[int, Fraction]
    bcov_series: Optional[Dict[int, Fraction]]
    compared_genera: Tuple[int, ...]
    discrepancies: Dict[int, Tuple[Fraction, Fraction]]
    status: str


def compare_shadow_to_bcov_series(
    name: str,
    shadow_lane: str,
    shadow_series: Mapping[int, Fraction],
    *,
    bcov_lane: Optional[str] = None,
    bcov_series: Optional[Mapping[int, Fraction]] = None,
    bcov_source: Optional[str] = None,
) -> ScalarSeriesComparison:
    """Compare a shadow series with caller-supplied, sourced BCOV data.

    Absence of BCOV data returns ``status='open'``.  Distinct scalar
    lanes return ``status='different_lanes'``.  Equality is tested only
    when both the lane and the independently supplied genus values agree.
    """
    shadow = {g: F(value) for g, value in shadow_series.items()}
    if bcov_series is None:
        return ScalarSeriesComparison(
            name=name,
            shadow_lane=shadow_lane,
            bcov_lane=bcov_lane,
            bcov_source=bcov_source,
            shadow_series=shadow,
            bcov_series=None,
            compared_genera=(),
            discrepancies={},
            status="open",
        )

    if not bcov_source:
        raise ValueError("a supplied BCOV series requires a provenance string")

    bcov = {g: F(value) for g, value in bcov_series.items()}
    common = tuple(sorted(set(shadow) & set(bcov)))
    discrepancies = {
        g: (shadow[g], bcov[g])
        for g in common
        if shadow[g] != bcov[g]
    }
    if bcov_lane != shadow_lane:
        status = "different_lanes"
    elif set(shadow) != set(bcov):
        status = "incomplete"
    elif discrepancies:
        status = "differs"
    else:
        status = "agrees"

    return ScalarSeriesComparison(
        name=name,
        shadow_lane=shadow_lane,
        bcov_lane=bcov_lane,
        bcov_source=bcov_source,
        shadow_series=shadow,
        bcov_series=bcov,
        compared_genera=common,
        discrepancies=discrepancies,
        status=status,
    )


# =========================================================================
# Section 9: Cross-geometry consistency checks
# =========================================================================

def kappa_additivity_check() -> bool:
    """Verify that the BKM lane is not the Heisenberg product lane.

    For K3 x E, the lane conflation would assert:
        kappa_BKM(K3 x E) ?= kappa_ch(K3) + kappa_ch(E)

    The BKM automorphic lane is separate from the Heisenberg-Mukai
    product specialisation.
    For K3: kappa = chi(O_{K3}) = 2 (or, in the CY Euler char, kappa = 2).
    For E: kappa = 1 (Heisenberg at level 1).
    Sum: 2 + 1 = 3. But kappa_BKM(K3 x E) = 5.

    The correct split is
    kappa_cat(K3 x E)=0, kappa_ch^{Heis}(K3 x E)=3,
    kappa_BKM(Delta_5)=5, and kappa_fiber(K3)=24.
    """
    kappa_k3 = F(2)
    kappa_e = F(1)
    kappa_bkm_k3xe = F(5)

    # kappa_BKM is not the Heisenberg product/sum lane.
    assert kappa_k3 + kappa_e != kappa_bkm_k3xe, \
        "kappa_BKM should not be identified with the K3+E Heisenberg lane"

    # The old product trap 2*1=2 and the Heisenberg sum 2+1=3 both miss
    # the BKM weight 5.
    return True


def euler_characteristic_check() -> bool:
    """Verify Euler characteristic computations.

    chi(K3) = 24
    chi(E) = 0
    chi(K3 x E) = chi(K3) * chi(E) = 0 (multiplicative)

    chi(conifold) = 2
    chi(quintic) = -200
    """
    k3 = k3_hodge()
    e = elliptic_hodge()
    k3xe = k3_times_e_hodge()
    qui = quintic_hodge()

    assert k3.euler == 24
    assert e.euler == 0
    assert k3xe.euler == 0
    # The conifold is non-compact; its Hodge diamond is not a standard
    # compact one, so we skip the Euler check. The effective chi = 2
    # comes from topology (chi = 1 + 1 for the two-sphere), not from
    # the partial Hodge data we store.
    assert qui.euler == -200

    return True


def pv_dimension_check() -> bool:
    """Verify polyvector space dimensions.

    PV*(K3) = 24-dim (from Hodge diamond: 1+0+1+0+20+0+1+0+1 = 24)
    PV*(E) = 4-dim
    PV*(K3 x E) = sum of products = 96-dim

    PV^{0,q}(K3) = H^{2,q}: h^{2,0}=1, h^{2,1}=0, h^{2,2}=1. Sum: 2.
    PV^{1,q}(K3) = H^{1,q}: h^{1,0}=0, h^{1,1}=20, h^{1,2}=0. Sum: 20.
    PV^{2,q}(K3) = H^{0,q}: h^{0,0}=1, h^{0,1}=0, h^{0,2}=1. Sum: 2.
    Total PV*(K3) = 2 + 20 + 2 = 24.

    PV^{0,q}(E) = H^{1,q}: h^{1,0}=1, h^{1,1}=1. Sum: 2.
    PV^{1,q}(E) = H^{0,q}: h^{0,0}=1, h^{0,1}=1. Sum: 2.
    Total PV*(E) = 2 + 2 = 4.

    PV*(K3 x E) by Kunneth: 24 * 4 = 96. The computation uses all
    PV^{p,q} terms, not only a half-diamond truncation.
    """
    pv_k = pv_k3()
    pv_e = pv_elliptic()
    pv_kxe = pv_k3_times_e()
    pv_c3 = pv_c3_constant()
    pv_con = pv_conifold_effective_carrier()

    assert pv_k.total_dim == 24
    assert pv_e.total_dim == 4
    assert pv_kxe.total_dim == 96
    assert pv_c3.total_dim == 8
    assert pv_con.total_dim == 3

    return True


def ghost_number_check() -> bool:
    """Verify ghost number grading on PV spaces.

    For C^3 (constant polyvectors):
      gh = -1: PV^{0,0} = 1-dim (functions)
      gh = 0:  PV^{1,0} = 3-dim (vector fields)
      gh = 1:  PV^{2,0} = 3-dim (bivectors)
      gh = 2:  PV^{3,0} = 1-dim (trivectors)

    Euler characteristic by ghost number: 1 - 3 + 3 - 1 = 0.
    """
    pv = pv_c3_constant()
    gh = pv.ghost_graded_dims

    assert gh.get(-1, 0) == 1   # functions
    assert gh.get(0, 0) == 3    # vector fields
    assert gh.get(1, 0) == 3    # bivectors
    assert gh.get(2, 0) == 1    # trivectors

    # Euler char = 0
    euler = sum((-1) ** k * d for k, d in gh.items())
    assert euler == 0

    return True


# =========================================================================
# Section 10: Bar-carrier dimensions — explicit computation
# =========================================================================

def bar_carrier_dims_c3_explicit() -> Dict[int, int]:
    """Explicit bar-carrier dimensions for C^3.

    s^{-1}(PV*(C^3)) has dimensions:
      degree -2: 1 (even -> sym powers)
      degree -1: 3 (odd -> ext powers)
      degree 0:  3 (even -> sym powers)
      degree 1:  1 (odd -> ext powers)

    Bar degree 1: 1 + 3 + 3 + 1 = 8
    Bar degree 2: Sym^2 of the above.
      Partition 2 = 2+0+0+0: Sym^2(deg -2) * 1 * 1 * 1 = 1
      Partition 2 = 0+2+0+0: Ext^2(deg -1) * 1 * 1 * 1 = 3
      Partition 2 = 0+0+2+0: Sym^2(deg 0) * 1 * 1 * 1 = 6
      Partition 2 = 0+0+0+2: Ext^2(deg 1) * 1 * 1 * 1 = 0
      Partition 2 = 1+1+0+0: 1*3 = 3
      Partition 2 = 1+0+1+0: 1*3 = 3
      Partition 2 = 1+0+0+1: 1*1 = 1
      Partition 2 = 0+1+1+0: 3*3 = 9
      Partition 2 = 0+1+0+1: 3*1 = 3
      Partition 2 = 0+0+1+1: 3*1 = 3
      Total: 1+3+6+0+3+3+1+9+3+3 = 32

    Bar degree 3: Sym^3 of the above.
    """
    b = bar_carrier_c3(max_bar_degree=4)
    return b.bar_carrier_dims


def bar_carrier_dims_conifold_explicit() -> Dict[int, int]:
    """Explicit bar-carrier dimensions for the conifold.

    s^{-1}(PV*(conifold)) has dimensions:
      degree -2: 1 (from PV^{0,0}, even -> sym)
      degree 0:  1 (from PV^{1,1}, even -> sym)
      degree 1:  1 (from PV^{3,0}, odd -> ext)

    Bar degree 1: 1 + 1 + 1 = 3
    Bar degree 2:
      (2,0,0): Sym^2(1-dim even) = 1
      (0,2,0): Sym^2(1-dim even) = 1
      (0,0,2): Ext^2(1-dim odd) = 0
      (1,1,0): 1*1 = 1
      (1,0,1): 1*1 = 1
      (0,1,1): 1*1 = 1
      Total: 1+1+0+1+1+1 = 5
    """
    b = bar_carrier_conifold(max_bar_degree=4)
    return b.bar_carrier_dims


# =========================================================================
# Section 11: Schouten bracket on K3 x E polyvector fields
# =========================================================================

def schouten_bracket_k3xe_structure() -> Dict[str, Any]:
    """Analyze the Schouten bracket structure on PV*(K3 x E).

    Bogomolov-Tian-Todorov gives unobstructed complex deformations for
    compact CY manifolds. In the cohomological minimal model used by
    this compute lane:

    1. The quadratic obstruction is killed in cohomology, so the stored
       l_2 datum is zero.

    2. The first nonzero structure retained by the scalar BCOV lane is
       l_3.

    3. l_3 = C_{ijk} (Yukawa coupling) is the leading nontrivial
       bracket.

    For K3 x E, the CY3 polyvector decomposition is:
    h^{3-P, Q}(K3 x E) = sum_{(p1,q1)+(p2,q2)=(3-P,Q)} h^{p1,q1}(K3) * h^{p2,q2}(E)

    Therefore PV^{P,Q}(K3 x E) = h^{3-P, Q}(K3 x E).
    """
    hd = k3_times_e_hodge()
    pv = pv_k3_times_e()

    # Compute PV^{p,q} decomposition
    pv_decomp: Dict[Tuple[int, int], int] = {}
    for (p, q), d in pv.pv_dims.items():
        if d > 0:
            pv_decomp[(p, q)] = d

    # The deformation space is PV^{1,1} = H^1(T_{K3xE})
    # = H^1(TX) where TX is the tangent bundle of K3 x E
    # h^{2,1}(K3 x E) = number of complex structure deformations
    # From the product Hodge diamond: h^{2,1} = sum h^{p1,q1}*h^{p2,q2}
    # with p1+p2=2, q1+q2=1, so PV^{1,1} = h^{3-1, 1} = h^{2,1}.

    h21 = hd.h(2, 1)

    # The cohomological minimal model stores the BTT-killed l_2 obstruction as zero.
    bracket_vanishes = True

    return {
        "pv_decomposition": pv_decomp,
        "total_dim": pv.total_dim,
        "deformation_dim": h21,  # = PV^{1,1} = h^{2,1}(K3xE)
        "bracket_vanishes_on_cohomology": bracket_vanishes,
        "reason": "BTT minimal-model obstruction vanishing",
        "leading_nontrivial_bracket": "l_3 (Yukawa coupling)",
    }


# =========================================================================
# Section 12: BCOV genus-0 prepotential and F_g comparison
# =========================================================================

def f0_conifold(t: Fraction, n_inst: int = 5) -> Fraction:
    """Genus-0 prepotential for the conifold.

    F_0 = t^3/6 + sum_{d=1}^{n_inst} Li_3(e^{-dt})

    Since we work formally: F_0^{classical} = t^3/6.
    The instanton sum gives the GV contribution with n_0^d = 1.

    Returns the classical part only (exact rational arithmetic).
    """
    return t ** 3 / F(6)


def f1_from_kappa(kappa: Fraction) -> Fraction:
    """F_1 = kappa / 24 from the scalar shadow tower.

    This is the constant-map contribution at genus 1.
    For the B-model: F_1 = -log(det G_{ij}) + ... (holomorphic anomaly).
    At the scalar level: F_1 = kappa * a_hat_1 = kappa/24.
    """
    return kappa / F(24)


def f2_from_kappa(kappa: Fraction) -> Fraction:
    """F_2 = kappa * 7/5760 from the scalar shadow tower.

    This is the constant-map contribution at genus 2.
    """
    return kappa * F(7, 5760)


# =========================================================================
# Section 13: Complete analysis for all three geometries
# =========================================================================

def full_analysis_c3(max_bar: int = 4, max_genus: int = 5) -> Dict[str, Any]:
    """Finite carrier, zero coderivation, and scalar analysis for C^3."""
    profile = bcov_input_c3()
    bar = bar_carrier_c3(max_bar, max_genus)
    comp = compare_shadow_to_bcov_series(
        "C3",
        profile.scalar_lane,
        bar.scalar_shadow_amplitudes,
    )

    return {
        "geometry": "C^3",
        "scalar_lane": profile.scalar_lane,
        "scalar_value": profile.scalar_value,
        "bcov_one_loop_scalar": profile.bcov_one_loop_scalar,
        "shadow_class": profile.shadow_depth_class,
        "pv_total_dim": profile.pv.total_dim,
        "pv_ghost_graded": profile.pv.ghost_graded_dims,
        "coderivation_status": profile.coderivation_status,
        "bar_carrier_dims": bar.bar_carrier_dims,
        "bar_carrier_graded_dims": bar.bar_carrier_graded_dims,
        "coderivation_constructed": bar.coderivation_constructed,
        "bar_cohomology_dims": bar.bar_cohomology_dims,
        "bar_cohomology_graded_dims": bar.bar_cohomology_graded_dims,
        "scalar_shadow_amplitudes": bar.scalar_shadow_amplitudes,
        "bcov_comparison": comp,
    }


def full_analysis_conifold(max_bar: int = 4, max_genus: int = 5) -> Dict[str, Any]:
    """Finite carrier and scalar analysis for the resolved conifold."""
    profile = bcov_input_conifold()
    bar = bar_carrier_conifold(max_bar, max_genus)
    comp = compare_shadow_to_bcov_series(
        "conifold",
        profile.scalar_lane,
        bar.scalar_shadow_amplitudes,
    )

    return {
        "geometry": "resolved conifold",
        "scalar_lane": profile.scalar_lane,
        "scalar_value": profile.scalar_value,
        "bcov_one_loop_scalar": profile.bcov_one_loop_scalar,
        "shadow_class": profile.shadow_depth_class,
        "pv_total_dim": profile.pv.total_dim,
        "pv_ghost_graded": profile.pv.ghost_graded_dims,
        "coderivation_status": profile.coderivation_status,
        "bar_carrier_dims": bar.bar_carrier_dims,
        "bar_carrier_graded_dims": bar.bar_carrier_graded_dims,
        "coderivation_constructed": bar.coderivation_constructed,
        "bar_cohomology_dims": bar.bar_cohomology_dims,
        "bar_cohomology_graded_dims": bar.bar_cohomology_graded_dims,
        "scalar_shadow_amplitudes": bar.scalar_shadow_amplitudes,
        "bcov_comparison": comp,
        "yukawa": yukawa_conifold(),
    }


def full_analysis_k3xe(max_bar: int = 4, max_genus: int = 5) -> Dict[str, Any]:
    """Finite carrier and BKM scalar analysis for K3 x E."""
    profile = bcov_input_k3_times_e()
    bar = bar_carrier_k3_times_e(max_bar, max_genus)
    comp = compare_shadow_to_bcov_series(
        "K3xE",
        profile.scalar_lane,
        bar.scalar_shadow_amplitudes,
        bcov_lane="BCOV_one_loop",
    )
    schouten = schouten_bracket_k3xe_structure()

    return {
        "geometry": "K3 x E",
        "scalar_lane": profile.scalar_lane,
        "scalar_value": profile.scalar_value,
        "bcov_one_loop_scalar": profile.bcov_one_loop_scalar,
        "shadow_class": profile.shadow_depth_class,
        "pv_total_dim": profile.pv.total_dim,
        "pv_bcov_graded": profile.pv.bcov_graded_dims,
        "coderivation_status": profile.coderivation_status,
        "bar_carrier_dims": bar.bar_carrier_dims,
        "bar_carrier_graded_dims": bar.bar_carrier_graded_dims,
        "coderivation_constructed": bar.coderivation_constructed,
        "bar_cohomology_dims": bar.bar_cohomology_dims,
        "bar_cohomology_graded_dims": bar.bar_cohomology_graded_dims,
        "scalar_shadow_amplitudes": bar.scalar_shadow_amplitudes,
        "bcov_comparison": comp,
        "schouten_structure": schouten,
        "yukawa": yukawa_k3_times_e(),
    }


def full_analysis_quintic(max_bar: int = 4, max_genus: int = 5) -> Dict[str, Any]:
    """Finite carrier plus independent low-genus BCOV arithmetic for Q_5."""
    profile = bcov_input_quintic()
    bar = bar_carrier_quintic(max_bar, max_genus)
    bcov_constants = bcov_quintic_constant_map_low_genus()
    comparison = compare_shadow_to_bcov_series(
        "quintic",
        profile.scalar_lane,
        {
            genus: value
            for genus, value in bar.scalar_shadow_amplitudes.items()
            if genus in bcov_constants
        },
        bcov_lane="BCOV_constant_map",
        bcov_series=bcov_constants,
        bcov_source="landscape_census.tex:prop:canonical-bcov-quintic",
    )
    return {
        "geometry": "quintic",
        "scalar_lane": profile.scalar_lane,
        "scalar_value": profile.scalar_value,
        "bcov_one_loop_scalar": profile.bcov_one_loop_scalar,
        "pv_total_dim": profile.pv.total_dim,
        "coderivation_status": profile.coderivation_status,
        "bar_carrier_dims": bar.bar_carrier_dims,
        "bar_carrier_graded_dims": bar.bar_carrier_graded_dims,
        "bar_cohomology_dims": bar.bar_cohomology_dims,
        "scalar_shadow_amplitudes": bar.scalar_shadow_amplitudes,
        "bcov_constant_map_low_genus": bcov_constants,
        "bcov_comparison": comparison,
    }
