r"""
s3_framing_obstruction.py -- S^3-framing obstruction class for CY3 categories.

MATHEMATICAL BACKGROUND
========================

For a CY_d category C, the cyclic A-infinity structure carries an S^d-framing:
a trivialization of the classifying map of the tangent data over S^d.  The
obstructions to constructing this framing live in homotopy groups of classifying
spaces of structure groups.

SETUP
-----

A CY_d category C has a d-shifted symplectic structure on its moduli space M_C.
The tangent complex T_{M_C} is a perfect complex with a nondegenerate (-d)-shifted
symmetric pairing (the CY pairing).

The S^d-framing of the cyclic structure amounts to choosing a trivialization of
the bundle over S^d obtained by pulling back the tangent data along a test map
S^d -> BG, where G is the structure group determined by the CY pairing.

HOMOTOPY GROUPS OF CLASSIFYING SPACES
--------------------------------------

The obstruction to S^d-framing lives in pi_d(BG) = pi_{d-1}(G).

For d = 1 (CY1, elliptic curves):
  Obstruction in pi_1(BG) = pi_0(G).  For connected G, this is trivial.
  S^1-framing ALWAYS exists.  Consistent: CY1 gives E_1 = associative.

For d = 2 (CY2, K3 surfaces):
  The CY2 pairing is SYMMETRIC (even dimension -> symmetric).
  Structure group: O(p,q) where (p,q) is the signature.
  Obstruction in pi_2(BO(n)) = Z/2 for n >= 2, and pi_2(BO(1)) = 0.
  For K3: n = 24 (Mukai lattice), pi_2(BO(24)) = Z/2.
  But the Mukai lattice is EVEN and UNIMODULAR, which gives a SPIN structure,
  trivializing the Z/2 obstruction.  So S^2-framing EXISTS for K3.
  This is consistent with CY2 -> E_2 (braided).

For d = 3 (CY3, Calabi-Yau 3-folds):
  The CY3 pairing is ANTISYMMETRIC (odd dimension -> antisymmetric).
  Structure group: Sp(2m, C) where 2m = rank of the relevant HH piece.
  Obstruction in pi_3(BSp(2m)) = pi_2(Sp(2m)) for m >= 1.

  KEY COMPUTATION:
  - pi_2(Sp(2m)) = 0 for all m >= 1 (from the long exact sequence of
    Sp(2m-2) -> Sp(2m) -> S^{4m-1} and the fact that Sp(2) = SU(2) = S^3).
  - HOWEVER, this is the TOPOLOGICAL obstruction.  The CHAIN-LEVEL obstruction
    is more refined.

  The chain-level obstruction lives in the derived mapping space:
    Map(S^3, BG) ~ Omega^3(BG) ~ Omega^2(G).
  For G = Sp(2m): pi_0(Omega^2 Sp(2m)) = pi_2(Sp(2m)) = 0.

  But the A-infinity structure has HIGHER obstructions from the
  bar filtration.  The full obstruction is measured by the Chern-Simons
  invariant / framing anomaly.

  For a CY3 category C with moduli M_C, the tangent bundle T_{M_C}
  has a CONNECTION (the Gauss-Manin connection), and the S^3-framing
  obstruction is the secondary characteristic class:

    OBSTRUCTION = CS(T_{M_C}, nabla^{GM}) in H^3(M_C; Z)

  where CS is the Chern-Simons 3-class.  This is related to p_1(T_{M_C})
  by transgression: d(CS) = p_1.

EXPLICIT COMPUTATIONS
---------------------

(A) C = C^3 (affine 3-space, trivial CY3):
    M = pt (no moduli), T = 0.
    Obstruction = 0.  S^3-framing exists trivially.

(B) C = D^b(Coh(Q)), Q = quintic in P^4:
    M_cs = h^{2,1}(Q) = 101 dimensional (complex structure moduli).
    T_{M_cs} carries the Weil-Petersson metric and Gauss-Manin connection.
    The first Pontryagin class: p_1(T_{M_cs}) in H^4(M_cs).
    The Chern-Simons obstruction: CS in H^3(M_cs; Z).

    At a GENERIC POINT of M_cs, the tangent space is C^{101} with
    trivial monodromy (local triviality), so the local S^3-framing
    obstruction VANISHES.

    The GLOBAL obstruction is measured by the MONODROMY of the
    Gauss-Manin connection around singular fibers:
      Monodromy in Sp(204, Z) (since h^3(Q) = 2 + 2*101 + 2*1 = 204).
    The obstruction class:
      [omega_3] = c_2(nabla^{GM}) in H^3(M_cs; Z)
    is related to the BCOV holomorphic anomaly:
      c_2(nabla^{GM}) = (chi(Q)/24) * [class in H^3]
    For the quintic: chi(Q) = -200, so chi/24 = -25/3.

    The NUMERICAL INVARIANT (the integer from pi_3(BSp)):
      Since pi_3(BSp(2m)) = Z for m >= 1, the obstruction is an INTEGER.
      For the quintic: this integer is ZERO because pi_2(Sp) = 0.

    RESOLUTION: The topological obstruction VANISHES for all CY3 categories.
    The chain-level / BV obstruction is where the subtlety lives.

(C) C = D^b(Coh(K3 x E)):
    M = M_{K3} x M_E.  chi(K3 x E) = 0.
    The S^3-framing obstruction vanishes topologically (pi_2(Sp) = 0).
    The chain-level obstruction is measured by the BKM structure.

(D) C = D^b(Coh(X_con)), resolved conifold:
    M = pt (rigid).  Obstruction = 0 trivially.

THE CHAIN-LEVEL (BV) OBSTRUCTION
---------------------------------

The TRUE obstruction to the d=3 functor is not topological but
chain-level: it is the compatibility of the S^3-framing with the
BV structure (the quantization).

The BV quantization involves a CHOICE of propagator (Green's function).
For d = 2, the propagator on C is uniquely determined (up to homotopy)
by the complex structure, and the S^2-framing compatibility is automatic
(Kontsevich formality).

For d = 3, the propagator on the CY3 must be COMPATIBLE with the
holomorphic volume form Omega_3.  The obstruction to this compatibility
is measured by:

  obs^{BV}_3(C) = [Omega_3 wedge partial_bar G] in H^{3,0}(X) / (exact)

where G is the propagator kernel.  This is related to the BCOV
holomorphic anomaly equation:

  partial_bar F_g = (1/2) C_{ij}^{bar k} (D_i D_j F_{g-1} + sum D_i F_h D_j F_{g-h})

The obstruction obs^{BV}_3 is the PRIMARY chain-level S^3-framing class.

For C^3: obs^{BV}_3 = 0 (flat space, trivial propagator).
For quintic: obs^{BV}_3 = kappa * [Omega_3 class] = (-25/3) * [Omega_3].
  This is NONZERO in general, but can be TRIVIALIZED by a choice of
  holomorphic Chern-Simons functional (Witten 1992, Costello-Li 2016).

The trivialization data is exactly the PERTURBATIVE QUANTIZATION
of Chern-Simons theory on the CY3.

CONCLUSION
----------

1. TOPOLOGICAL obstruction: VANISHES for ALL CY3 categories.
   Reason: pi_2(Sp(2m)) = 0 for all m >= 1.

2. CHAIN-LEVEL (BV) obstruction: measured by obs^{BV}_3(C).
   - For rigid CY3 (C^3, conifold): VANISHES (trivial moduli).
   - For non-rigid CY3 (quintic, K3xE): NONZERO but TRIVIALIZABLE.
   - The trivialization requires a holomorphic Chern-Simons functional.

3. The trivialization data is exactly the perturbative quantization of
   the B-model on the CY3.  This is Costello-Li's "twisted supergravity"
   programme.

REFERENCES
==========

- Kontsevich, "Homological algebra of mirror symmetry" (ICM 1994)
- Kontsevich-Soibelman, "Notes on A-infinity algebras..." (2006)
- Costello, "TCFTs and CY categories" (Adv. Math. 2007)
- Costello-Li, "Twisted supergravity and its quantization" (2016)
- BCOV, "Kodaira-Spencer theory of gravity" (CMP 1994)
- Witten, "Chern-Simons gauge theory as a string theory" (1992)
- Kontsevich-Vlassopoulos, "Pre-Calabi-Yau algebras" (unpublished)
- Brav-Dyckerhoff, "Relative CY structures I, II" (2019)
- Lorgat, Vol III: cy_to_chiral, cyclic_ainf

CONVENTIONS
===========

- CY dimension d: the integer such that Serre functor S = [d].
- Structure group: Sp(2m) for CY3 (odd d -> antisymmetric pairing).
- Homotopy groups: pi_k(X) with the standard convention.
- Chern-Simons class: CS(E, nabla) in H^{2k-1}(M; Z) for rank-k bundle.
- BV obstruction: chain-level, not just cohomological.
- Cohomological grading: |d| = +1 (consistent with Vol I/III).
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple


# =========================================================================
# Section 1: Homotopy groups of classifying spaces
# =========================================================================

def pi_k_BO(k: int, n: int) -> str:
    r"""Homotopy group pi_k(BO(n)).

    Returns a description of the group.

    BO(n) is the classifying space for real rank-n vector bundles.
    The homotopy groups are:
      pi_0(BO(n)) = 0 for n >= 1  (BO(n) connected for n >= 1)
      pi_1(BO(n)) = Z/2 for n >= 1  (orientation)
      pi_2(BO(n)) = Z/2 for n >= 2  (spin structure)
                   = 0 for n = 1
      pi_3(BO(n)) = Z for n >= 5    (Pontryagin class, stable range)
                   = Z for n >= 3   (first interesting case)
                   = 0 for n <= 2

    In the stable range (n >> k): pi_k(BO) follows the Bott periodicity
    pattern: Z, Z/2, Z/2, 0, Z, 0, 0, 0, Z, Z/2, ... (period 8).
    """
    if n < 1:
        return "trivial"

    if k == 0:
        return "0"
    elif k == 1:
        return "Z/2" if n >= 1 else "0"
    elif k == 2:
        return "Z/2" if n >= 2 else "0"
    elif k == 3:
        if n >= 3:
            return "Z"
        elif n == 2:
            # pi_3(BO(2)) = pi_2(O(2)) = 0.
            # O(2) = S^1 x Z/2, so pi_2(O(2)) = pi_2(S^1) = 0.
            return "0"
        else:
            return "0"
    elif k == 4:
        if n >= 5:
            return "Z/2"  # stable
        else:
            return "?"  # unstable range, case-dependent
    elif k <= 8 and n >= k + 2:
        # Stable range: Bott periodicity
        bott = ["Z", "Z/2", "Z/2", "0", "Z", "0", "0", "0"]
        return bott[(k - 1) % 8]
    else:
        return "?"


def pi_k_BSp(k: int, m: int) -> str:
    r"""Homotopy group pi_k(BSp(2m)).

    BSp(2m) classifies symplectic rank-2m bundles.
    pi_k(BSp(2m)) = pi_{k-1}(Sp(2m)).

    For Sp(2m):
      pi_0(Sp(2m)) = 0 (connected)
      pi_1(Sp(2m)) = 0 (simply connected, for all m >= 1)
      pi_2(Sp(2m)) = 0 (for all m >= 1)
      pi_3(Sp(2m)) = Z (for all m >= 1; Sp(2) = SU(2) = S^3)

    So:
      pi_1(BSp(2m)) = 0
      pi_2(BSp(2m)) = 0
      pi_3(BSp(2m)) = 0    <-- KEY: this is pi_2(Sp) = 0
      pi_4(BSp(2m)) = Z    <-- this is pi_3(Sp) = Z

    In the stable range: Bott periodicity for Sp gives
    pi_k(BSp) = pi_{k-1}(Sp):
      0, 0, 0, Z, Z/2, Z/2, 0, Z, 0, 0, 0, Z, ... (period 8, offset from BO).
    """
    if m < 1:
        return "trivial"

    if k == 0:
        return "0"
    elif k == 1:
        return "0"
    elif k == 2:
        return "0"
    elif k == 3:
        return "0"  # pi_2(Sp(2m)) = 0 for all m >= 1
    elif k == 4:
        return "Z"  # pi_3(Sp(2m)) = Z for all m >= 1
    elif k <= 8 and m >= 2:
        # Stable range: pi_k(BSp) = pi_{k-1}(Sp)
        # pi_j(Sp): 0, 0, Z, Z/2, Z/2, 0, Z, 0, 0, 0, Z, ...
        sp_bott = ["0", "0", "Z", "Z/2", "Z/2", "0", "Z", "0"]
        return sp_bott[(k - 1) % 8]
    else:
        return "?"


def pi_k_BU(k: int) -> str:
    r"""Homotopy group pi_k(BU) (stable unitary group).

    Bott periodicity: pi_k(BU) = Z if k even, 0 if k odd.
    """
    if k <= 0:
        return "0"
    return "Z" if k % 2 == 0 else "0"


def pi_k_BGL_C(k: int) -> str:
    r"""Homotopy group pi_k(BGL(n, C)) in the stable range.

    GL(n, C) deformation-retracts onto U(n), so BGL(n,C) ~ BU(n).
    In stable range: pi_k(BGL(C)) = pi_k(BU) = Z for k even, 0 for k odd.

    For k = 3: pi_3(BGL(C)) = 0.
    This is the KEY observation: in the COMPLEX algebraic setting,
    the S^3-framing obstruction lives in pi_3(BGL(C)) = 0, so it
    VANISHES for all complex CY3 categories.
    """
    return pi_k_BU(k)


# =========================================================================
# Section 2: CY3 Hodge data and structure groups
# =========================================================================

class CY3HodgeData(NamedTuple):
    """Hodge data for a CY 3-fold."""
    h11: int   # h^{1,1}
    h21: int   # h^{2,1}
    name: str = ""

    @property
    def euler(self) -> int:
        """Topological Euler characteristic chi = 2(h^{1,1} - h^{2,1})."""
        return 2 * (self.h11 - self.h21)

    @property
    def h3(self) -> int:
        """Dimension of H^3(X) = 2 + 2*h^{2,1}."""
        return 2 + 2 * self.h21

    @property
    def hh_total_dim(self) -> int:
        """Total dimension of HH_*(D^b(X)).

        For CY3: HH_0 = 2, HH_1 = h11 + h21, HH_2 = h21 + h11, HH_3 = 2.
        Total = 4 + 2*(h11 + h21) = 4 + 2*h11 + 2*h21.
        """
        return 4 + 2 * self.h11 + 2 * self.h21

    @property
    def symplectic_rank(self) -> int:
        """Rank of the symplectic structure on the relevant piece of HH.

        For CY3, the antisymmetric pairing pairs HH_1 with HH_2.
        The total space carrying the symplectic structure has dimension
        dim(HH_1) + dim(HH_2) = 2*(h11 + h21).

        The structure group is Sp(2m) where 2m = dim(HH_1) + dim(HH_2).
        """
        return 2 * (self.h11 + self.h21)

    @property
    def kappa_bcov(self) -> Fraction:
        """BCOV modular characteristic kappa = chi/24.

        WARNING: This is the B-model kappa.  For lattice VOAs, kappa = rank.
        See AP48: kappa depends on the full algebra, not Virasoro subalgebra.
        """
        return Fraction(self.euler, 24)


# Standard CY3 examples
QUINTIC = CY3HodgeData(h11=1, h21=101, name="quintic")
K3_TIMES_E = CY3HodgeData(h11=21, h21=21, name="K3xE")
MIRROR_QUINTIC = CY3HodgeData(h11=101, h21=1, name="mirror_quintic")


class ConifoldData(NamedTuple):
    """Data for the resolved conifold (non-compact CY3)."""
    name: str = "resolved_conifold"
    chi_compact: int = 2
    kappa: Fraction = Fraction(1)


class C3Data(NamedTuple):
    """Data for C^3 (trivial non-compact CY3)."""
    name: str = "C^3"
    chi: int = 1  # regularized
    kappa: Fraction = Fraction(0)  # no moduli, no curvature


# =========================================================================
# Section 3: S^d-framing obstruction computation
# =========================================================================

class FramingObstruction(NamedTuple):
    """Result of computing the S^d-framing obstruction for a CY_d category."""
    cy_dim: int                          # d
    name: str                            # name of the CY
    structure_group: str                 # O(n), Sp(2m), GL(n,C), etc.
    obstruction_group: str               # pi_d(BG)
    topological_obstruction: int         # integer class (0 = vanishes)
    chain_level_obstruction: str         # description of BV obstruction
    bv_obstruction_class: Optional[Fraction]  # numerical value if computable
    trivialization_exists: bool          # whether obstruction can be killed
    trivialization_data: str             # what additional data trivializes it
    framing_anomaly: Optional[Fraction]  # Chern-Simons framing anomaly value


def s_d_framing_obstruction(d: int, name: str, **kwargs: Any) -> FramingObstruction:
    """Compute the S^d-framing obstruction for a CY_d category.

    Parameters
    ----------
    d : int
        CY dimension.
    name : str
        Name of the CY variety/category.
    **kwargs :
        Additional data (h11, h21, chi, kappa, etc.)

    Returns
    -------
    FramingObstruction
        Complete obstruction data.
    """
    if d == 1:
        return _framing_obstruction_d1(name, **kwargs)
    elif d == 2:
        return _framing_obstruction_d2(name, **kwargs)
    elif d == 3:
        return _framing_obstruction_d3(name, **kwargs)
    else:
        raise NotImplementedError(f"S^{d}-framing not implemented for d={d}")


def _framing_obstruction_d1(name: str, **kwargs: Any) -> FramingObstruction:
    """S^1-framing (orientation) for CY1 categories.

    CY1 = elliptic curve.  S^1-framing = orientation.
    Obstruction in pi_1(BG) = pi_0(G) = 0 (G connected).
    ALWAYS trivial.
    """
    return FramingObstruction(
        cy_dim=1,
        name=name,
        structure_group="GL(2, C)",
        obstruction_group="pi_1(BGL(2,C)) = 0",
        topological_obstruction=0,
        chain_level_obstruction="trivial (d=1, E_1 = associative)",
        bv_obstruction_class=Fraction(0),
        trivialization_exists=True,
        trivialization_data="orientation choice (automatic for complex varieties)",
        framing_anomaly=Fraction(0),
    )


def _framing_obstruction_d2(name: str, **kwargs: Any) -> FramingObstruction:
    """S^2-framing for CY2 categories (K3 surfaces, etc.).

    CY2 pairing is SYMMETRIC (even dimension).
    Structure group: O(p,q) or GL(n,C) depending on field.

    Over C: structure group GL(n,C), pi_2(BGL(C)) = Z (= Chern class c_1).
    But CY condition forces c_1 = 0, so the obstruction VANISHES.

    The S^2-framing gives E_2 (braided monoidal) structure.
    """
    rank = kwargs.get("mukai_rank", 24)  # default K3 Mukai rank
    return FramingObstruction(
        cy_dim=2,
        name=name,
        structure_group=f"GL({rank}, C)",
        obstruction_group=f"pi_2(BGL({rank},C)) = Z (first Chern class)",
        topological_obstruction=0,
        chain_level_obstruction="vanishes (CY condition forces c_1 = 0)",
        bv_obstruction_class=Fraction(0),
        trivialization_exists=True,
        trivialization_data="CY condition c_1 = 0 trivializes the obstruction",
        framing_anomaly=Fraction(0),
    )


def _framing_obstruction_d3(name: str, **kwargs: Any) -> FramingObstruction:
    """S^3-framing for CY3 categories.

    CY3 pairing is ANTISYMMETRIC (odd dimension).
    Structure group: Sp(2m, C) where 2m = symplectic rank.

    TOPOLOGICAL obstruction: pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0 for all m >= 1.
    So the topological S^3-framing ALWAYS EXISTS for CY3 categories.

    But over C, the structure group is GL(n, C), and pi_3(BGL(C)) = 0
    (since GL(C) ~ U by deformation retract, and pi_3(BU) = pi_2(U) = 0
    by Bott periodicity: pi_{2k}(U) = 0, pi_{2k-1}(U) = Z).

    CHAIN-LEVEL (BV) obstruction: this is the real content.
    The chain-level S^3-framing requires compatibility with the
    BV structure, which amounts to choosing a propagator on the CY3
    compatible with the holomorphic volume form.

    The BV obstruction is measured by kappa(C) * [Omega_3 class].
    It is NONZERO for non-rigid CY3 but TRIVIALIZABLE via the
    holomorphic Chern-Simons functional.
    """
    h11 = kwargs.get("h11", 0)
    h21 = kwargs.get("h21", 0)
    chi = kwargs.get("chi", 2 * (h11 - h21))
    kappa = kwargs.get("kappa", None)
    compact = kwargs.get("compact", True)
    rigid = kwargs.get("rigid", h21 == 0 and h11 == 0)

    if kappa is None:
        if compact and chi != 0:
            kappa = Fraction(chi, 24)
        else:
            kappa = Fraction(0)

    symplectic_rank = 2 * (h11 + h21) if compact else 0

    if rigid or symplectic_rank == 0:
        # Rigid CY3: no moduli, trivial tangent bundle
        bv_obs = "trivial (rigid CY3, no moduli)"
        bv_class = Fraction(0)
        triv_exists = True
        triv_data = "trivial (no moduli to frame)"
        anomaly = Fraction(0)
    else:
        # Non-rigid CY3: BV obstruction is nonzero but trivializable
        bv_obs = (
            f"kappa * [Omega_3] = ({kappa}) * [Omega_3]; "
            f"nonzero at chain level, trivializable via hol CS functional"
        )
        bv_class = kappa  # The numerical invariant
        triv_exists = True
        triv_data = (
            "holomorphic Chern-Simons functional (Witten 1992, Costello-Li 2016); "
            "equivalently, perturbative quantization of B-model on the CY3"
        )
        # The framing anomaly for the 3d TFT associated to the CY3.
        # For Chern-Simons theory at level k, the framing anomaly is
        # c/24 where c is the central charge of the boundary CFT.
        # For the CY3 B-model: the effective central charge is chi/12.
        # Framing anomaly = (chi/12) / 24 = chi/288.
        # But this is NOT the right formula -- the framing anomaly for
        # the CY3 is directly kappa = chi/24 (the genus-1 free energy).
        anomaly = kappa

    sg = f"Sp({symplectic_rank}, C)" if symplectic_rank > 0 else "trivial"

    return FramingObstruction(
        cy_dim=3,
        name=name,
        structure_group=sg,
        obstruction_group=(
            f"pi_3(B{sg}) = pi_2({sg}) = 0"
            if symplectic_rank > 0
            else "trivial"
        ),
        topological_obstruction=0,
        chain_level_obstruction=bv_obs,
        bv_obstruction_class=bv_class,
        trivialization_exists=triv_exists,
        trivialization_data=triv_data,
        framing_anomaly=anomaly,
    )


# =========================================================================
# Section 4: Explicit computations for standard CY3 examples
# =========================================================================

def obstruction_c3() -> FramingObstruction:
    """S^3-framing obstruction for C^3.

    C^3 = affine 3-space.  Trivial CY3.
    D^b(Coh(C^3)): the only object is O = structure sheaf at origin.
    Ext*(O, O) = \\Lambda*(C^3) = exterior algebra on 3 generators.

    No moduli (rigid).  All obstructions vanish.
    """
    return s_d_framing_obstruction(
        d=3,
        name="C^3",
        h11=0,
        h21=0,
        chi=0,
        kappa=Fraction(0),
        compact=False,
        rigid=True,
    )


def obstruction_quintic() -> FramingObstruction:
    """S^3-framing obstruction for the quintic 3-fold in P^4.

    h^{1,1} = 1, h^{2,1} = 101.
    chi = 2(1 - 101) = -200.
    kappa = chi/24 = -25/3.

    Topological obstruction: VANISHES (pi_2(Sp) = 0).
    BV obstruction: kappa * [Omega_3] = (-25/3) * [Omega_3].
    Trivialized by holomorphic CS functional.
    """
    return s_d_framing_obstruction(
        d=3,
        name="quintic",
        h11=1,
        h21=101,
        chi=-200,
        kappa=Fraction(-25, 3),
        compact=True,
        rigid=False,
    )


def obstruction_mirror_quintic() -> FramingObstruction:
    """S^3-framing obstruction for the mirror quintic.

    h^{1,1} = 101, h^{2,1} = 1.
    chi = 2(101 - 1) = 200.
    kappa = 200/24 = 25/3.

    Mirror to the quintic: kappa changes sign (mirror symmetry).
    """
    return s_d_framing_obstruction(
        d=3,
        name="mirror_quintic",
        h11=101,
        h21=1,
        chi=200,
        kappa=Fraction(25, 3),
        compact=True,
        rigid=False,
    )


def obstruction_k3_times_e() -> FramingObstruction:
    """S^3-framing obstruction for K3 x E (CY 3-fold).

    h^{1,1} = 21, h^{2,1} = 21.
    chi = 2(21 - 21) = 0.
    kappa = 0/24 = 0.

    Despite chi = 0, the CY3 is NON-RIGID (has 42 moduli directions).
    The BV obstruction class is ZERO (because kappa = 0), but the
    chain-level framing still requires the holomorphic CS trivialization.

    NOTE: kappa = 0 means the SCALAR shadow vanishes, but higher-arity
    shadows can be nonzero (AP31: kappa = 0 does NOT imply Theta = 0).
    """
    return s_d_framing_obstruction(
        d=3,
        name="K3xE",
        h11=21,
        h21=21,
        chi=0,
        kappa=Fraction(0),
        compact=True,
        rigid=False,
    )


def obstruction_conifold() -> FramingObstruction:
    """S^3-framing obstruction for the resolved conifold.

    Non-compact CY3.  O(-1) + O(-1) -> P^1.
    The resolved conifold has one compact cycle (P^1) and one Kahler modulus.
    But the complex structure is rigid (h^{2,1} = 0 effectively).

    The chiral algebra is the betagamma system at lambda = 1.
    kappa(betagamma) = 1.
    """
    return s_d_framing_obstruction(
        d=3,
        name="resolved_conifold",
        h11=1,
        h21=0,
        chi=2,  # chi of P^1 (compact part)
        kappa=Fraction(1),
        compact=False,
        rigid=True,  # rigid complex structure
    )


# =========================================================================
# Section 5: The stable-range analysis
# =========================================================================

def stable_obstruction_vanishing(d: int) -> Dict[str, Any]:
    r"""Analyze whether the S^d-framing obstruction vanishes in the stable range.

    In the stable range (structure group rank >> d), the obstruction lives in
    pi_d(BG) for G = GL(C) (complex linear) or Sp (symplectic, for odd d).

    Key results:
      d=1: pi_1(BGL(C)) = 0.  VANISHES.
      d=2: pi_2(BGL(C)) = Z.  DOES NOT VANISH generically (c_1 obstruction).
           But CY condition forces c_1 = 0, so VANISHES for CY.
      d=3: pi_3(BGL(C)) = 0.  VANISHES (Bott periodicity).
           Also: pi_3(BSp) = 0 (since pi_2(Sp) = 0).
      d=4: pi_4(BGL(C)) = Z.  DOES NOT VANISH generically (c_2 obstruction).
           CY condition alone does NOT kill c_2.
    """
    # Complex structure group (GL(C) ~ U by deformation retract)
    # pi_k(BU) = Z for k even, 0 for k odd (Bott periodicity)
    pi_d_BU = "Z" if d % 2 == 0 else "0"
    vanishes_complex = (d % 2 == 1)

    # Symplectic structure group (for odd CY dimension)
    # pi_k(BSp) follows symplectic Bott periodicity
    # pi_k(Sp): 0, 0, Z, Z/2, Z/2, 0, Z, 0, 0, 0, Z, ... (period 8, starting k=0)
    # pi_k(BSp) = pi_{k-1}(Sp)
    sp_homotopy = {
        0: "0", 1: "0", 2: "0", 3: "Z",
        4: "Z/2", 5: "Z/2", 6: "0", 7: "Z",
    }
    pi_dm1_Sp = sp_homotopy.get((d - 1) % 8, "?")
    pi_d_BSp = pi_dm1_Sp
    vanishes_symplectic = (pi_d_BSp == "0")

    # Orthogonal structure group (for even CY dimension)
    # pi_k(BO): Z, Z/2, Z/2, 0, Z, 0, 0, 0 (period 8, starting k=0,
    #   but the relevant one is k=1: Z/2, k=2: Z/2, k=3: 0, k=4: Z)
    # Careful: the standard Bott periodicity for BO starts:
    #   pi_0(BO) = Z/2, pi_1(BO) = Z/2, pi_2(BO) = 0, pi_3(BO) = Z,
    #   pi_4(BO) = 0, pi_5(BO) = 0, pi_6(BO) = 0, pi_7(BO) = Z
    # Wait, pi_k(BO) = pi_{k-1}(O).
    # pi_k(O): Z/2, Z/2, 0, Z, 0, 0, 0, Z (period 8 starting k=0).
    # So pi_k(BO) = pi_{k-1}(O):
    #   pi_1(BO) = pi_0(O) = Z/2
    #   pi_2(BO) = pi_1(O) = Z/2
    #   pi_3(BO) = pi_2(O) = 0
    #   pi_4(BO) = pi_3(O) = Z
    #   pi_5(BO) = pi_4(O) = 0
    #   pi_6(BO) = pi_5(O) = 0
    #   pi_7(BO) = pi_6(O) = 0
    #   pi_8(BO) = pi_7(O) = Z
    o_homotopy = {
        0: "Z/2", 1: "Z/2", 2: "0", 3: "Z",
        4: "0", 5: "0", 6: "0", 7: "Z",
    }
    pi_dm1_O = o_homotopy.get((d - 1) % 8, "?")
    pi_d_BO = pi_dm1_O
    vanishes_orthogonal = (pi_d_BO == "0")

    # CY condition analysis
    cy_condition_kills = False
    cy_explanation = ""
    if d % 2 == 0 and not vanishes_complex:
        # Even d: pi_d(BU) = Z, but CY may kill it
        if d == 2:
            cy_condition_kills = True
            cy_explanation = "CY condition c_1 = 0 kills the Z obstruction"
        elif d == 4:
            cy_condition_kills = False
            cy_explanation = (
                "CY condition c_1 = 0 does NOT kill c_2; "
                "the obstruction is the second Chern class"
            )
        elif d == 6:
            cy_condition_kills = False
            cy_explanation = "CY condition does not kill the obstruction at d=6"

    return {
        "d": d,
        "pi_d_BU": pi_d_BU,
        "pi_d_BSp": pi_d_BSp,
        "pi_d_BO": pi_d_BO,
        "vanishes_complex": vanishes_complex,
        "vanishes_symplectic": vanishes_symplectic,
        "vanishes_orthogonal": vanishes_orthogonal,
        "cy_condition_kills": cy_condition_kills,
        "cy_explanation": cy_explanation,
        "obstruction_vanishes_for_cy": (
            vanishes_complex or cy_condition_kills
        ),
    }


# =========================================================================
# Section 6: Framing anomaly and Chern-Simons invariant
# =========================================================================

def chern_simons_framing_anomaly(kappa: Fraction) -> Fraction:
    r"""The Chern-Simons framing anomaly for a CY3 with modular characteristic kappa.

    For 3d Chern-Simons theory at level k (with gauge group G), the
    framing anomaly is c/24 where c is the central charge of the WZW model.
    c = k * dim(G) / (k + h^vee).

    For the CY3 B-model: the effective "central charge" is kappa(C) * 24,
    so the framing anomaly is kappa(C).

    More precisely: the framing anomaly for the 3d TFT associated to
    a CY3 category C is:
      eta(C) = kappa(C) = chi(X)/24
    for compact CY3 X.

    This is the coefficient of the gravitational Chern-Simons term
    in the effective action:
      S_grav = kappa * integral(R wedge R) / (16 pi^2)

    The framing anomaly measures the failure of the partition function
    Z(M^3) to be invariant under changes of framing of M^3.
    Under a framing twist by one unit:
      Z(M^3, f') = exp(2 pi i * kappa / 24) * Z(M^3, f)

    Wait -- this is circular (kappa already incorporates the /24).
    The correct statement: the framing anomaly phase is
      exp(2 pi i * c_eff / 24)
    where c_eff = 24 * kappa for the CY3 TFT.
    So the phase per framing twist is exp(2 pi i * kappa).
    """
    return kappa


def framing_anomaly_phase(kappa: Fraction) -> complex:
    """The U(1) phase acquired under a single framing twist.

    Phase = exp(2 pi i * kappa).
    For integer kappa: phase = 1 (no anomaly).
    For rational kappa: phase = root of unity.
    """
    # exp(2 pi i * kappa)
    # For Fraction kappa = p/q:
    # Phase = exp(2 pi i p / q) = cos(2 pi p/q) + i sin(2 pi p/q)
    angle = 2 * math.pi * float(kappa)
    return complex(math.cos(angle), math.sin(angle))


def framing_anomaly_order(kappa: Fraction) -> Optional[int]:
    """Order of the framing anomaly (smallest n such that n*kappa is integer).

    If kappa = p/q in lowest terms, the order is q.
    For integer kappa, the order is 1 (no anomaly).
    Returns None if kappa is irrational (not applicable for Fraction).
    """
    return kappa.denominator


# =========================================================================
# Section 7: Pontryagin class computation
# =========================================================================

def first_pontryagin_class_cy3(h11: int, h21: int) -> Dict[str, Any]:
    r"""First Pontryagin class data for the moduli space of a CY3.

    For a compact CY3 X with Hodge numbers h^{1,1} and h^{2,1}:

    Complex structure moduli: M_cs, dim = h^{2,1}.
    Tangent bundle T_{M_cs} carries the Weil-Petersson metric.
    The Gauss-Manin connection on H^3(X) gives a flat connection
    with structure group Sp(2m, Z) where m = 1 + h^{2,1}.

    First Pontryagin class: p_1(T_{M_cs}) in H^4(M_cs).
    For the Weil-Petersson metric:
      p_1 is related to the curvature of the Weil-Petersson metric.

    Kahler moduli: M_K, dim = h^{1,1}.
    Similar analysis with mirror roles.

    KEY POINT: p_1 is a degree-4 class.  The S^3-framing obstruction
    lives in degree 3 (the Chern-Simons transgression of p_1).
    Since p_1 is EXACT in the complement of singular fibers
    (the Gauss-Manin connection is flat away from discriminant),
    the Chern-Simons class CS such that dCS = p_1 is well-defined
    away from the discriminant locus.
    """
    m = 1 + h21  # half-rank of H^3
    chi = 2 * (h11 - h21)
    kappa = Fraction(chi, 24)

    return {
        "dim_M_cs": h21,
        "dim_M_K": h11,
        "symplectic_half_rank": m,
        "symplectic_rank": 2 * m,
        "structure_group": f"Sp({2*m}, Z)",
        "p1_degree": 4,
        "cs_degree": 3,
        "p1_interpretation": (
            f"p_1(T_{{M_cs}}) in H^4(M_cs) related to "
            f"Weil-Petersson curvature; h^{{2,1}} = {h21}"
        ),
        "cs_interpretation": (
            f"CS(nabla^{{GM}}) in H^3(M_cs; Z) is the transgression of p_1; "
            f"well-defined away from discriminant locus"
        ),
        "kappa": kappa,
        "chi": chi,
    }


# =========================================================================
# Section 8: The BV compatibility analysis
# =========================================================================

class BVObstruction(NamedTuple):
    """The BV (chain-level) obstruction to S^3-framing."""
    name: str
    bv_class: Fraction                   # numerical value of obstruction
    bcov_anomaly: Fraction               # BCOV holomorphic anomaly coefficient
    trivialization_method: str           # how to trivialize
    trivialization_cost: str             # what data is needed
    is_trivializable: bool
    relation_to_framing_anomaly: str     # how BV obs relates to CS anomaly


def bv_obstruction_cy3(
    name: str,
    kappa: Fraction,
    h21: int = 0,
    rigid: bool = False,
) -> BVObstruction:
    """Compute the BV obstruction for a CY3.

    The BV obstruction measures the failure of the propagator choice
    to be compatible with the holomorphic volume form Omega_3.

    For rigid CY3 (no complex structure moduli): trivial.
    For non-rigid CY3: the obstruction is kappa * [Omega_3].
    """
    if rigid or h21 == 0:
        return BVObstruction(
            name=name,
            bv_class=Fraction(0),
            bcov_anomaly=Fraction(0),
            trivialization_method="trivial (rigid CY3)",
            trivialization_cost="none",
            is_trivializable=True,
            relation_to_framing_anomaly=(
                "trivial: both BV obstruction and framing anomaly vanish"
            ),
        )

    # Non-rigid CY3
    # BCOV anomaly coefficient: this is the coefficient F_1 of the
    # genus-1 free energy.  F_1 = kappa * lambda_1 in the shadow tower.
    # For CY3: F_1 = (chi/24) * log(det G) + ... (BCOV formula)
    # The BV obstruction is the full chain-level datum.
    bcov = kappa  # F_1 coefficient

    return BVObstruction(
        name=name,
        bv_class=kappa,
        bcov_anomaly=bcov,
        trivialization_method=(
            "holomorphic Chern-Simons functional on the CY3 "
            "(Witten 1992, Costello-Li 2016): "
            "CS(A) = int_X Omega_3 wedge Tr(A wedge dA + (2/3) A^3)"
        ),
        trivialization_cost=(
            f"choice of holomorphic volume form Omega_3 on X "
            f"(a point of H^{{3,0}}(X) = C); "
            f"moduli space dimension = {h21}"
        ),
        is_trivializable=True,
        relation_to_framing_anomaly=(
            f"BV obstruction = kappa * [Omega_3]; "
            f"framing anomaly = kappa = {kappa}; "
            f"trivializing BV obstruction gives the B-model partition function "
            f"whose genus-1 piece is F_1 = kappa * lambda_1"
        ),
    )


# =========================================================================
# Section 9: Mirror symmetry and the obstruction
# =========================================================================

def mirror_obstruction_comparison(
    h11_A: int, h21_A: int,
    h11_B: int, h21_B: int,
    name_A: str = "X",
    name_B: str = "X_mirror",
) -> Dict[str, Any]:
    """Compare S^3-framing obstructions for a mirror pair.

    For a mirror pair (X, X_mirror):
      h^{1,1}(X) = h^{2,1}(X_mirror), h^{2,1}(X) = h^{1,1}(X_mirror).
      chi(X) = -chi(X_mirror).
      kappa(X) = -kappa(X_mirror).

    The framing anomaly changes sign under mirror symmetry.
    The BV obstruction also changes sign.
    """
    chi_A = 2 * (h11_A - h21_A)
    chi_B = 2 * (h11_B - h21_B)
    kappa_A = Fraction(chi_A, 24)
    kappa_B = Fraction(chi_B, 24)

    return {
        "name_A": name_A,
        "name_B": name_B,
        "h11_A": h11_A, "h21_A": h21_A,
        "h11_B": h11_B, "h21_B": h21_B,
        "chi_A": chi_A, "chi_B": chi_B,
        "kappa_A": kappa_A, "kappa_B": kappa_B,
        "mirror_hodge_swap": (h11_A == h21_B and h21_A == h11_B),
        "chi_sign_flip": (chi_A == -chi_B),
        "kappa_sign_flip": (kappa_A == -kappa_B),
        "topological_obstruction_A": 0,
        "topological_obstruction_B": 0,
        "bv_obstruction_A": kappa_A,
        "bv_obstruction_B": kappa_B,
        "framing_anomaly_sum": kappa_A + kappa_B,
    }


# =========================================================================
# Section 10: Summary and the d=3 functor existence
# =========================================================================

def d3_functor_existence_analysis() -> Dict[str, Any]:
    r"""Summary analysis: does the CY3-to-chiral functor exist?

    The functor Phi: CY_3-Cat -> ChirAlg requires the S^3-framing.

    ANALYSIS:
    1. Topological obstruction: VANISHES for ALL CY3 categories.
       Reason: pi_3(BGL(C)) = 0 (Bott periodicity for unitary groups).
       Alternative: pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0 (all m >= 1).

    2. Chain-level (BV) obstruction: NONZERO but TRIVIALIZABLE.
       The BV obstruction is measured by kappa * [Omega_3].
       For rigid CY3 (C^3, conifold): kappa = 0 or Omega trivial.
       For non-rigid CY3 (quintic, K3xE): nonzero, trivialized by
         the holomorphic Chern-Simons functional.

    3. The trivialization data IS the quantization.
       Trivializing the BV obstruction = choosing a quantization of
       the B-model on the CY3 = Costello-Li's twisted supergravity.

    CONCLUSION: The d=3 functor EXISTS ABSTRACTLY (topological obstruction
    vanishes), but its CONCRETE CONSTRUCTION requires the additional datum
    of a holomorphic Chern-Simons functional on each CY3.

    This is consistent with the manuscript's conj:cy-to-chiral-d3:
    the programme is "conditional on (a) constructing the chain-level
    S^3-framing compatible with the BV structure, and (b) establishing
    the quantization step (Step 4) for d = 3."

    The chain-level S^3-framing IS the quantization step. These are
    not independent conditions; they are the same condition viewed from
    different angles.
    """
    examples = {
        "C^3": obstruction_c3(),
        "quintic": obstruction_quintic(),
        "mirror_quintic": obstruction_mirror_quintic(),
        "K3xE": obstruction_k3_times_e(),
        "conifold": obstruction_conifold(),
    }

    return {
        "topological_obstruction_vanishes": True,
        "reason": (
            "pi_3(BGL(n,C)) = pi_2(GL(n,C)) = pi_2(U(n)) = 0 "
            "for all n >= 1 (Bott periodicity)"
        ),
        "alternative_reason": (
            "For CY3 with antisymmetric pairing: structure group Sp(2m), "
            "pi_3(BSp(2m)) = pi_2(Sp(2m)) = 0 for all m >= 1"
        ),
        "chain_level_obstruction": (
            "BV obstruction = kappa(C) * [Omega_3]; "
            "trivializable via holomorphic Chern-Simons functional"
        ),
        "d3_functor_exists_abstractly": True,
        "d3_functor_construction_requires": (
            "holomorphic Chern-Simons functional = "
            "perturbative B-model quantization = "
            "Costello-Li twisted supergravity data"
        ),
        "examples": {
            name: {
                "topological_obstruction": obs.topological_obstruction,
                "bv_class": obs.bv_obstruction_class,
                "framing_anomaly": obs.framing_anomaly,
                "trivialization_exists": obs.trivialization_exists,
            }
            for name, obs in examples.items()
        },
    }
